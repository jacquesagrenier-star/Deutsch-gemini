# -*- coding: utf-8 -*-
"""LA GRAMMAIRE DANS LES SEANCES A ETAPES (retour de Jacques du 14 nov. 2026 sur la v1189 : « deuxieme seance, etape 2
sur 12, Manger dehors », que des cartes, aucune partie grammaire).

Le chemin de Jacques, joue de bout en bout, en de et en es : un compte neuf, Premiers pas fini, l'A1 voyage ; une seance
par jour (l'horloge des revisions avancee d'un jour a chaque fois), tout reussi, jusqu'a la premiere seance de l'escale 2
(« Manger dehors ») ; puis la DEUXIEME seance du meme jour (« Encore une seance »).
Ce qui doit tenir :
  - la premiere seance de chaque escale montre le tableau de l'escale (la carte du tableau, partie Grammaire) --
    jusqu'a la v1189, l'heure de l'ecriture rangee sous « t » (« tableau vu ») le cachait des la 2e escale ;
  - la deuxieme seance a une partie Grammaire (trois questions tirees du tableau de l'escale), annoncee dans la barre
    des la premiere carte, et qui s'ouvre quand on y arrive.
Captures (--captures) : la premiere carte de la 2e seance (en-tete et barre), l'ecran de passage de la Grammaire, puis
sa premiere carte.
Usage : python tests/grammaire_etapes.py [--racine DOSSIER] [--port 8821] [--captures DOSSIER] [--langues de,es]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SEMER = r"""
() => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  localStorage.setItem(PROFIL_KEY, JSON.stringify({ r: 'cours', f: 'tout' }));
  fixerNiveauSeance('A1', true);
  return { niveau: niveauSeance(), voyage: a1VoyageEnCours() };
}
"""

# Une seance du jour JOUR, tout reussi ; les cartes de l'A1 voyage marquees comme a l'affichage.
JOUR = r"""
async ([jour]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  await ouvrirSeanceDuJour(); await pause(1500);
  const cartes = currentCards.slice();
  const av = lireA1Voyage();
  const r = { e: av.e || 0, n: cartes.length, tableau: cartes.filter(c => c.avTableau).length,
              gram: cartes.filter(c => c.forme === 'gram').length };
  cartes.forEach(c => {
    try{
      if(c.av){ try{ marquerCarteA1V(c); }catch(e){} }
      if(c.mode === 'phrase'){ if(c.cible) repondrePhrase(c, true); return; }
      if(!c.word || c.themeId === undefined) return;
      const st = getWordState(c.themeId, c.index);
      if(!estNeuf(st) && (st.due || 0) > Date.now()) return;
      st.vu = true; appliquerReussite(st); setWordState(c.themeId, c.index, st);
    }catch(e){}
  });
  return r;
}
"""

# La deuxieme seance du meme jour : la premiere comptee finie, puis « Encore une seance ».
DEUXIEME = r"""
async ([jour]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  try{ localStorage.setItem(SEANCES_LEGERES_KEY, JSON.stringify({ j: getTodayStr(), n: 1 })); }catch(e){}
  await encoreUneSeance(); await pause(1800);
  return true;
}
"""

ETAT = r"""
() => {
  const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : null;
  const segs = parts ? segmentsSeance(currentCards, parts).map(s => s.p) : null;
  const noms = [...document.querySelectorAll('#seancePartsNoms > *')].map(x => x.textContent.trim());
  const ecran = document.querySelector('.screen.active');
  const texte = ecran ? ecran.innerText.split('\n').map(x => x.trim()).filter(Boolean).slice(0, 6) : [];
  const gram = parts ? currentCards.filter(c => parts.get(c) === 'grammaire')
      .map(c => c.forme + (c.gramTableau ? '/tableau' : '') + (c.avTableau ? '/tableau-escale' : '') + (c.ex ? ' « ' + c.ex.question + ' »' : '')) : [];
  const av = lireA1Voyage();
  return { segs, noms, n: currentCards.length, gram, texte, escale: av.e || 0,
           lieu: (escalesA1Voyage()[av.e || 0] || {}).id || null, rang: seancesFiniesAujourdhui() };
}
"""

# Avance carte a carte jusqu'a la partie Grammaire : l'ecran de passage, puis sa premiere carte.
VERS_GRAMMAIRE = r"""
async ([etape]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  for(let pas = 0; pas < 120; pas++){
    await pause(60);
    const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : null;
    const c = currentCards[currentFlashcard];
    const scr = (document.querySelector('.screen.active') || {}).id;
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    const partie = parts && c ? parts.get(c) : null;
    if(go && go.offsetHeight > 0){
      if(partie === 'grammaire'){
        if(etape === 'passage') return { ou: 'passage', partie, forme: c.forme };
        go.click(); await pause(500);
        return { ou: 'carte', partie, forme: c.forme, question: c.ex ? c.ex.question : null };
      }
      go.click(); await pause(150); continue;
    }
    if(partie === 'grammaire' && scr === 'flashcards') return { ou: 'carte', partie, forme: c.forme, question: c.ex ? c.ex.question : null };
    if(scr === 'sceneSeance'){ try{ revenirDeLArret(); }catch(e){} await pause(250); continue; }
    if(scr !== 'flashcards' || !c) return { ou: 'perdu', scr, partie };
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){
      if(c.forme === 'gram'){ const b = document.querySelector('#cartePhrase .cp-choix button'); if(b){ b.click(); await pause(150); } }
      try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){}
      nextFlashcard();
    } else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  return { ou: 'jamais' };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8821)
    ap.add_argument("--captures", default=None)
    ap.add_argument("--langues", default="de,es")
    ap.add_argument("--etiquette", default="")
    ap.add_argument("--jours-max", type=int, default=20)
    a = ap.parse_args()
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)

    class S(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def handle(self):
            try:
                super().handle()
            except (ConnectionError, OSError):
                pass

    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", a.port), functools.partial(S, directory=a.racine))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = []
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for langue in a.langues.split(","):
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
            page = ctx.new_page()
            err = []
            page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
            page.on("dialog", lambda d: d.dismiss())
            url = "http://127.0.0.1:%d/index.html?apprendre=%s" % (a.port, langue)
            page.goto(url)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1200)
            try:
                page.evaluate("() => { try{ if(typeof CODIGOS_VALIDOS !== 'undefined' && typeof CLAVE_ACCESO !== 'undefined') localStorage.setItem(CLAVE_ACCESO, CODIGOS_VALIDOS[0]); }catch(e){} }")
            except Exception:
                pass
            print("%s SEME %s" % (langue, json.dumps(page.evaluate(SEMER))), flush=True)
            jour, tableaux, arrive = 0, {}, None
            while jour < a.jours_max:
                page.goto(url)
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(700)
                r = page.evaluate(JOUR, [jour])
                print("   jour %d : escale %d, %d cartes, tableau de l'escale %d, gram %d" % (jour, r["e"] + 1, r["n"], r["tableau"], r["gram"]), flush=True)
                tableaux.setdefault(r["e"], 0)
                tableaux[r["e"]] += r["tableau"]
                if r["e"] >= 1:
                    arrive = jour
                    break
                jour += 1
            if arrive is None:
                fautes.append("%s : l'escale 2 jamais atteinte en %d jours" % (langue, a.jours_max))
                ctx.close()
                continue
            print("   tableau de l'escale montre a la 1re seance : escale 1 %d fois, escale 2 %d fois" % (tableaux.get(0, 0), tableaux.get(1, 0)), flush=True)
            if not tableaux.get(1):
                fautes.append("%s : la 1re seance de l'escale 2 n'a pas montre le tableau de l'escale" % langue)
            # La deuxieme seance du meme jour, sans recharger (l'horloge reste au meme jour).
            page.evaluate(DEUXIEME, [arrive])
            e = page.evaluate(ETAT)
            print("   2e SEANCE : %s" % json.dumps(e, ensure_ascii=False), flush=True)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, "%s%s-2e-seance-1re-carte.png" % (a.etiquette, langue)))
            if not e["segs"] or "grammaire" not in e["segs"]:
                fautes.append("%s : la barre de la 2e seance n'a pas de partie Grammaire (%s)" % (langue, e["segs"]))
            if len(e["gram"]) < 3:
                fautes.append("%s : %d carte(s) de grammaire dans la 2e seance" % (langue, len(e["gram"])))
            if e["lieu"] != "manger":
                fautes.append("%s : la 2e seance n'est pas a l'escale « manger » (%s)" % (langue, e["lieu"]))
            if e["segs"] and "grammaire" in e["segs"]:
                v = page.evaluate(VERS_GRAMMAIRE, ["passage"])
                print("   vers la Grammaire : %s" % json.dumps(v, ensure_ascii=False), flush=True)
                if a.captures and v.get("ou") == "passage":
                    page.screenshot(path=os.path.join(a.captures, "%s%s-2e-seance-passage-grammaire.png" % (a.etiquette, langue)))
                v2 = page.evaluate(VERS_GRAMMAIRE, ["carte"])
                print("   la Grammaire ouverte : %s" % json.dumps(v2, ensure_ascii=False), flush=True)
                page.wait_for_timeout(500)
                if a.captures:
                    page.screenshot(path=os.path.join(a.captures, "%s%s-2e-seance-grammaire-ouverte.png" % (a.etiquette, langue)))
                if v2.get("ou") != "carte":
                    fautes.append("%s : la partie Grammaire ne s'ouvre pas (%s)" % (langue, v2))
            if err:
                print("   erreurs JavaScript : %s" % err[:5], flush=True)
            ctx.close()
        nav.close()
    srv.shutdown()
    print()
    if fautes:
        print("ECHEC (%d)" % len(fautes))
        for f in fautes:
            print("  - " + f)
        sys.exit(1)
    print("OK : la 1re seance de l'escale 2 montre son tableau ; la 2e seance a sa partie Grammaire, qui s'ouvre.")


if __name__ == "__main__":
    main()
