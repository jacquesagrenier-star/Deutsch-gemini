# -*- coding: utf-8 -*-
"""LA SEANCE DU JOUR JUSQU'A L'ACCUEIL, PAR CHAQUE CHEMIN (Jacques, 12 nov. 2026, espagnol, A1, v1176 : « J'ai fait une
seance du jour [...] puis j'ai demande de reviser des mots. Ce que j'avais manque. Ca a fonctionne, mais ensuite, ca m'a
ramene a une ligne complete de progression vide dans ma seance du jour A1. » ; « Une fois qu'on a revise nos mots qu'on
avait manques, on devrait [...] nous demander si on veut continuer avec une nouvelle seance. Ou non. » ; la revue A a Z
du meme jour ; le fond de nuit qui ne suivait pas pendant la seance).

Un compte A1 hors Premiers pas (es, puis de) joue la seance du jour en ratant deux mots, puis suit un chemin jusqu'a
l'accueil, ou la sonde lit le bouton et la ligne de la carte de la seance :
  sans           : « Terminer »                         -> l'accueil dit « Encore une seance » et « seance faite » ;
  refaire-non    : « Les refaire », la question, Non      -> idem, sans seance de plus ;
  revoir-non     : « Revoir les cartes non maitrisees »   -> les cartes de la seance seules, jamais un mot neuf, sous
                   « Apres la seance · Revoir mes mots », la question, Non -> idem ;
  revoir-oui     : la meme reprise, puis Oui               -> une seance nouvelle s'ouvre ;
  milieu         : « ‹ » a la 4e carte, l'ecran court, « Revenir a l'accueil » -> « Continuer la seance » ; l'anneau de
                   l'ecran court ne repete pas le compte du jour ;
  deux           : la seance finie, l'accueil, « Encore une seance » de l'accueil -> la meme seance que « Encore une
                   seance » de l'ecran de fin (meme taille, a une carte pres), jamais une seance de 3 cartes.
Plus : le passage jour / nuit pendant la seance redessine le fond de chaque partie, dans les deux sens ; « Revoir les
cartes maitrisees » n'apparait pas sans carte maitrisee.
Usage : python tests/revision_apres_seance.py [--racine DOSSIER] [--port 8809] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
        localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true })); }
"""

ETAT = r"""
() => {
  const scr = (document.querySelector('.screen.active') || {}).id;
  const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
  const tx = id => { const e = document.getElementById(id); return e ? e.textContent.replace(/\s+/g, ' ').trim() : null; };
  return {
    ecran: scr, finPaquet: vis('flashcardEnd'), question: vis('finRevision'), finCourte: vis('finCourte'),
    finies: seancesFiniesAujourdhui(), nbSeances: lireSeances().length,
    cartes: (currentCards || []).length, rang: currentFlashcard,
    kicker: tx('flashKicker'), titre: tx('flashThemeTitle'),
    bouton: tx('spPlayTxt'), sens: tx('spSens'),
    attendus: { commencer: t('seance_commencer_long'), continuer: t('seance_continuer_long'), encore: t('legere_encore'), faite: t('legere_fin_une') }
  };
}
"""

JOUER = r"""
async ([rater, limite]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const encore = new Set(), fois = new Map();
  let n = 0, cartes = 0;
  for(let pas = 0; pas < 400; pas++){
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
    if(c.mode === 'phrase'){ try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){} nextFlashcard(); }
    else {
      if(!fois.get(c) && encore.size < rater && !document.querySelector('#flashcardActions.presentation')){ encore.add(c); fois.set(c, 1); reviewAgain(); }
      else reviewGood();
      n++;
    }
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  await pause(900);
  return n;
}
"""

REPRISE = r"""
() => {
  const seance = (SEANCE_PARTS && SEANCE_PARTS.paquet) || [];
  const cles = new Set(seance.filter(c => c && c.word).map(c => c.themeId + ':' + c.index));
  const cartes = currentCards || [];
  return { n: cartes.length, neufs: cartes.filter(c => c && estNeuf(getWordState(c.themeId, c.index))).length,
           horsSeance: cartes.filter(c => c && !cles.has(c.themeId + ':' + c.index)).length };
}
"""

JOUR_NUIT = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1500);
  const fond = () => { const f = document.getElementById('seanceFond'); return f ? f.style.background : ''; };
  const parts = ['mots', 'rev', 'conj', 'scene', 'theme', 'son', 'pp'].concat(typeof TEINTES_PAYSAGE !== 'undefined' && TEINTES_PAYSAGE.conv ? ['conv'] : []);
  const res = {};
  for(const cle of parts){
    setAppTheme('light'); await pause(60);
    PAYSAGE_MONTRE = null; paysageSeance(cle); await pause(60);
    const jour = fond();
    setAppTheme('dark'); await pause(120);
    const nuit = fond();
    setAppTheme('light'); await pause(120);
    const retour = fond();
    setAppTheme('dark'); await pause(60); PAYSAGE_MONTRE = null; paysageSeance(cle); await pause(60);
    const nuit2 = fond(); setAppTheme('light'); await pause(120); const jour2 = fond();
    res[cle] = { change: !!jour && nuit !== jour, revient: retour === jour, inverse: nuit2 !== jour2 && jour2 === jour };
  }
  setAppTheme('light');
  return res;
}
"""

VIS = "(s) => { const b = document.querySelector(s); return !!(b && !b.classList.contains('hidden') && b.offsetHeight > 0); }"
CLIC = "(s) => { const b = document.querySelector(s); if(!b || b.classList.contains('hidden') || !b.offsetHeight) return false; b.click(); return true; }"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8809)
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

    def ouvrir(nav, appris):
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
        return ctx, page, err

    def accueil(page):
        if page.evaluate("() => (document.querySelector('.screen.active') || {}).id") != "home":
            page.evaluate("() => { try{ handleFlashcardBack(); }catch(e){} }")
            page.wait_for_timeout(1500)
        if page.evaluate("() => (document.querySelector('.screen.active') || {}).id") != "home":
            page.evaluate("() => { try{ goHome(); }catch(e){} }")
            page.wait_for_timeout(1500)
        return page.evaluate(ETAT)

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in ("es", "de"):
            # le passage jour / nuit pendant la seance
            ctx, page, err = ouvrir(nav, appris)
            jn = page.evaluate(JOUR_NUIT)
            mauvais = [k for k, v in jn.items() if not (v["change"] and v["revient"] and v["inverse"])]
            page.evaluate("async () => { setAppTheme('light'); PAYSAGE_MONTRE = null; paysageSeance('rev'); await new Promise(r => setTimeout(r, 100)); setAppTheme('dark'); }")
            page.wait_for_timeout(400)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, "%s-jour-nuit-revisions.png" % appris))
            fautes += 1 if mauvais else 0
            print("== %s jour-nuit     %s" % (appris, "ok" if not mauvais else "FAUTE, fond inchange : " + ", ".join(mauvais)), flush=True)
            ctx.close()

            tailles = {}
            for chemin in ("sans", "refaire-non", "revoir-non", "revoir-oui", "milieu", "deux-accueil", "deux-fin"):
                ctx, page, err = ouvrir(nav, appris)

                def cap(nom):
                    if a.captures:
                        page.screenshot(path=os.path.join(a.captures, "%s-%s-%s.png" % (appris, chemin, nom)))
                e0 = page.evaluate(ETAT)
                page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
                page.wait_for_timeout(1500)
                juge, lignes = [], [("accueil avant", e0)]
                att = e0["attendus"]
                if chemin == "milieu":
                    page.evaluate(JOUER, [0, 4])
                    page.evaluate("() => { try{ handleFlashcardBack(); }catch(e){} }")
                    page.wait_for_timeout(900)
                    ec = page.evaluate(ETAT)
                    court = page.evaluate("() => { const fc = document.getElementById('finCourte'); return fc ? fc.innerText.replace(/\\s+/g, ' ').trim().slice(0, 160) : ''; }")
                    cap("1-ecran-court")
                    lignes.append(("ecran court", {"visible": ec["finCourte"], "texte": court}))
                    import re
                    if re.search(r"(\d+) \1 ", court):
                        juge.append("l'ecran court repete le compte (%s)" % court[:40])
                    page.evaluate("() => { try{ quitterSeanceCourte(); }catch(e){} }")
                    page.wait_for_timeout(1500)
                    e5 = accueil(page)
                    cap("5-accueil")
                    lignes.append(("accueil", e5))
                    if e5["bouton"] != att["continuer"]:
                        juge.append("l'accueil dit « %s » au lieu de « %s »" % (e5["bouton"], att["continuer"]))
                else:
                    n = page.evaluate(JOUER, [2, 0])
                    e1 = page.evaluate(ETAT)
                    cap("1-fin-seance")
                    lignes.append(("fin de seance", e1))
                    if chemin == "sans":
                        vm = page.evaluate(VIS, "#flashcardEnd button[onclick='retryMastered()']")
                        nm = page.evaluate("() => (typeof cartesDeLaSeanceFinie === 'function' ? cartesDeLaSeanceFinie() : (currentCardsFull || [])).filter(it => getWordState(it.themeId, it.index).mastered).length")
                        if vm and not nm:
                            juge.append("« Revoir les cartes maitrisees » affiche sans carte maitrisee")
                    if chemin in ("refaire-non", "revoir-non", "revoir-oui"):
                        sel = ".fin-erreurs-refaire" if chemin == "refaire-non" else "#flashcardEnd button[onclick='retryUnmastered()']"
                        if not page.evaluate(CLIC, sel):
                            juge.append("bouton introuvable (%s)" % sel)
                        page.wait_for_timeout(900)
                        rep = page.evaluate(REPRISE)
                        e2 = page.evaluate(ETAT)
                        cap("2-reprise")
                        lignes.append(("reprise ouverte", dict(e2, reprise=rep)))
                        if rep["neufs"]:
                            juge.append("%d mot(s) neuf(s) dans la reprise" % rep["neufs"])
                        if rep["horsSeance"]:
                            juge.append("%d carte(s) hors de la seance (%d en tout)" % (rep["horsSeance"], rep["n"]))
                        if page.evaluate("() => t('seance_titre')") in (e2["kicker"] or "") or page.evaluate("() => t('seance_titre')") in (e2["titre"] or ""):
                            juge.append("la reprise garde le titre de la seance (%s · %s)" % (e2["kicker"], e2["titre"]))
                        page.evaluate(JOUER, [0, 0])
                        e3 = page.evaluate(ETAT)
                        cap("3-fin-reprise")
                        lignes.append(("reprise finie", e3))
                        if not e3["question"]:
                            juge.append("pas de question a la fin de la reprise")
                        if chemin == "revoir-oui":
                            page.evaluate(CLIC, "#finRevision button.primary")
                            page.wait_for_timeout(2500)
                            e4 = page.evaluate(ETAT)
                            cap("4-oui")
                            lignes.append(("oui", e4))
                            if e4["ecran"] != "flashcards" or e4["nbSeances"] != e1["nbSeances"] + 1:
                                juge.append("« Oui » n'ouvre pas une seance nouvelle")
                        else:
                            page.evaluate(CLIC, "#finRevision button.secondary")
                            page.wait_for_timeout(1500)
                    if chemin == "deux-fin":
                        page.evaluate(CLIC, "#encoreNeufsBtn")
                        page.wait_for_timeout(2500)
                        tailles["fin"] = page.evaluate("() => (currentCards || []).length")
                        cap("4-deuxieme")
                        lignes.append(("2e seance (ecran de fin)", page.evaluate(ETAT)))
                    elif chemin != "revoir-oui":
                        e5 = accueil(page)
                        cap("5-accueil")
                        lignes.append(("accueil", e5))
                        if e5["ecran"] != "home":
                            juge.append("pas revenu a l'accueil (%s)" % e5["ecran"])
                        plan = page.evaluate("() => { const e = document.querySelector('#seancePilule .pa-contenu'); return e ? e.textContent : ''; }")
                        e5["plan"] = plan
                        if e5["bouton"] != att["encore"] or att["faite"] not in plan or e5["sens"] == plan:
                            juge.append("l'accueil ne dit pas la seance faite (« %s » / « %s »)" % (e5["bouton"], (e5["sens"] or "")[:40]))
                        if e5["finies"] != e1["finies"] or e5["nbSeances"] != e1["nbSeances"]:
                            juge.append("le compte des seances a change (%s/%s -> %s/%s)" % (e1["finies"], e1["nbSeances"], e5["finies"], e5["nbSeances"]))
                        if chemin == "deux-accueil":
                            page.evaluate(CLIC, "#seancePilule .pa-play")
                            page.wait_for_timeout(2500)
                            tailles["accueil"] = page.evaluate("() => (currentCards || []).length")
                            cap("6-deuxieme")
                            lignes.append(("2e seance (accueil)", page.evaluate(ETAT)))
                fautes += 1 if juge else 0
                print("== %s %-12s %s" % (appris, chemin, "ok" if not juge else "FAUTE " + " ; ".join(juge)), flush=True)
                for nom, e in lignes:
                    e = {k: v for k, v in e.items() if k != "attendus"}
                    print("   %-24s %s" % (nom, json.dumps(e, ensure_ascii=False)[:340]), flush=True)
                er = sorted(set(x for x in err if "synonymes" not in x))
                if er:
                    print("   erreurs JS :", er[:3], flush=True)
                ctx.close()
            ta, tf_ = tailles.get("accueil"), tailles.get("fin")
            ok = ta is not None and tf_ is not None and abs(ta - tf_) <= 1 and ta >= 8
            fautes += 0 if ok else 1
            print("== %s deuxieme seance : accueil %s cartes, ecran de fin %s cartes  %s" % (appris, ta, tf_, "ok" if ok else "FAUTE"), flush=True)
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
