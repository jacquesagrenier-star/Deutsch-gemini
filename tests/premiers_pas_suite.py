# -*- coding: utf-8 -*-
"""PREMIERS PAS JUSQU'A L'ACCUEIL (revue A a Z, rapport 2, 12 nov. 2026).

Un compte neuf en Premiers pas (es, puis de) :
  milieu  : 5 cartes passees, « ‹ », l'ecran court, « Revenir a l'accueil » ; l'accueil dit « Continuer la seance » ; la
            seance rouverte reprend la SUITE -- aucune carte du parcours deja passee n'y revient ;
  refaire : la seance jouee avec un seul mot rate, « Le refaire », la carte, puis la question « Continuer avec une
            nouvelle seance ? » ; Non : l'accueil, le compte des seances du jour inchange (1) ;
  libelle : le bouton de l'ecran de fin dit « Encore une seance », comme en A1.
Usage : python tests/premiers_pas_suite.py [--racine DOSSIER] [--port 8811] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
        localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true })); }
"""
ETAT = r"""
() => {
  const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
  const tx = id => { const e = document.getElementById(id); return e ? e.textContent.replace(/\s+/g, ' ').trim() : null; };
  return { ecran: (document.querySelector('.screen.active') || {}).id, question: vis('finRevision'), finPaquet: vis('flashcardEnd'),
           finies: seancesFiniesAujourdhui(), nbSeances: lireSeances().length, position: positionPremiersPas(),
           bouton: tx('spPlayTxt'), encore: tx('encoreNeufsBtn'),
           attendus: { continuer: t('seance_continuer_long'), encore: t('legere_encore') } };
}
"""
# joue jusqu'a `limite` cartes (0 : toute la seance) ; rend les ppPos des cartes du parcours passees
JOUER = r"""
async ([rater, limite]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const passees = [], fois = new Map(); let rates = 0, cartes = 0;
  for(let pas = 0; pas < 300; pas++){
    await pause(50);
    const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
    if(vis('flashcardEnd') || vis('finRevision')) break;
    if(currentFlashcard >= currentCards.length) break;
    if(limite && cartes >= limite) break;
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr === 'sceneSeance'){ revenirDeLArret(); await pause(220); continue; }
    if(scr !== 'flashcards') break;
    const n0 = currentFlashcard, q0 = currentCards;
    cartes++;
    if(typeof c.ppPos === 'number') passees.push(c.ppPos);
    if(c.mode === 'phrase'){ try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){} nextFlashcard(); }
    else if(!fois.get(c) && rates < rater && !document.querySelector('#flashcardActions.presentation')){ fois.set(c, 1); rates++; reviewAgain(); }
    else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  await pause(900);
  return passees;
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8811)
    ap.add_argument("--captures")
    a = ap.parse_args()

    class Serveur(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def handle(self):
            try:
                super().handle()
            except (ConnectionError, OSError):
                pass

    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", a.port), functools.partial(Serveur, directory=a.racine))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)
    from playwright.sync_api import sync_playwright
    fautes = 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in ("es", "de"):
            for chemin in ("milieu", "refaire"):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                err = []
                page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
                page.wait_for_load_state("networkidle")
                page.evaluate(PREPARER)
                page.reload()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(1500)

                def cap(nom):
                    if a.captures:
                        page.screenshot(path=os.path.join(a.captures, "pp-%s-%s-%s.png" % (appris, chemin, nom)))
                juge, lignes = [], []
                page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
                page.wait_for_timeout(1500)
                if chemin == "milieu":
                    passees = page.evaluate(JOUER, [0, 5])
                    page.evaluate("() => { try{ handleFlashcardBack(); }catch(e){} }")
                    page.wait_for_timeout(900)
                    page.evaluate("() => { try{ quitterSeanceCourte(); }catch(e){} }")
                    page.wait_for_timeout(1500)
                    if page.evaluate("() => (document.querySelector('.screen.active') || {}).id") != "home":
                        page.evaluate("() => { try{ goHome(); }catch(e){} }")
                        page.wait_for_timeout(1200)
                    e1 = page.evaluate(ETAT)
                    cap("1-accueil")
                    lignes.append(("accueil", e1))
                    if e1["bouton"] != e1["attendus"]["continuer"]:
                        juge.append("l'accueil dit « %s »" % e1["bouton"])
                    page.evaluate("() => { const b = document.querySelector('#seancePilule .pa-play'); if(b) b.click(); }")
                    page.wait_for_timeout(2500)
                    rouverte = page.evaluate("() => (currentCards || []).filter(c => c && typeof c.ppPos === 'number').map(c => c.ppPos)")
                    cap("2-rouverte")
                    revenues = sorted(set(rouverte) & set(passees))
                    lignes.append(("passees", {"ppPos": passees}))
                    lignes.append(("rouverte", {"n": len(rouverte), "debut": rouverte[:8], "deja_passees": revenues}))
                    if revenues:
                        juge.append("la seance rouverte refait %d carte(s) deja passee(s)" % len(revenues))
                else:
                    page.evaluate(JOUER, [1, 0])
                    e1 = page.evaluate(ETAT)
                    cap("1-fin")
                    lignes.append(("fin de seance", e1))
                    if e1["encore"] and e1["encore"] != e1["attendus"]["encore"]:
                        juge.append("le bouton de fin dit « %s »" % e1["encore"])
                    ok = page.evaluate("() => { const b = document.querySelector('.fin-erreurs-refaire'); if(!b || !b.offsetHeight) return false; b.click(); return true; }")
                    if not ok:
                        juge.append("« Le refaire » introuvable")
                    page.wait_for_timeout(900)
                    page.evaluate(JOUER, [0, 0])
                    e2 = page.evaluate(ETAT)
                    cap("2-fin-reprise")
                    lignes.append(("reprise finie", e2))
                    if not e2["question"]:
                        juge.append("pas de question a la fin de la reprise")
                    page.evaluate("() => { const b = document.querySelector('#finRevision button.secondary'); if(b) b.click(); }")
                    page.wait_for_timeout(1500)
                    e3 = page.evaluate(ETAT)
                    cap("3-accueil")
                    lignes.append(("accueil", e3))
                    if e3["finies"] != e1["finies"]:
                        juge.append("la reprise compte comme une seance (%s -> %s)" % (e1["finies"], e3["finies"]))
                fautes += 1 if juge else 0
                print("== %s %-8s %s" % (appris, chemin, "ok" if not juge else "FAUTE " + " ; ".join(juge)), flush=True)
                for nom, e in lignes:
                    e = {k: v for k, v in e.items() if k != "attendus"}
                    print("   %-14s %s" % (nom, json.dumps(e, ensure_ascii=False)[:300]), flush=True)
                er = sorted(set(x for x in err if "synonymes" not in x))
                if er:
                    print("   erreurs JS :", er[:3], flush=True)
                ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
