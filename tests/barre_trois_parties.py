# -*- coding: utf-8 -*-
"""LA BARRE DE LA SEANCE EN TROIS PARTIES, PLUS CONVERSATIONS (decision de Jacques du 12 nov. 2026, proposition 5).

La barre est fixee des la premiere carte et ne change plus ; ses parties : Cartes, Grammaire, Images, et Conversations
le jour ou une etape se termine ; une carte ratee revient dans sa propre partie. La sonde joue la seance entiere (trois
« Encore ») et releve la barre a CHAQUE carte :
  ordinaire : un compte A1 hors Premiers pas ;
  pp-jour1  : Premiers pas, premiere seance ;
  pp-etape  : Premiers pas, la seance qui finit l'etape 1 (la conversation des passeports).
Ce qui doit tenir : la meme suite de parties du debut a la fin, toutes parmi cartes / grammaire / images / conv, dans cet
ordre, les noms sous la barre dans la langue d'interface ; pp-etape a ses Conversations ; captures jour et nuit.
Usage : python tests/barre_trois_parties.py [--racine DOSSIER] [--port 8813] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
([cas]) => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(cas === 'ordinaire') localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  else localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true })); }
"""
POSITION = """
async () => { await chargerPremiersPas(); const seq = sequencePremiersPas(); const i = seq.findIndex(x => x.forme === 'pp_scene' && x.jourPP === 0);
  const s = lirePremiersPas(); s.p = Math.max(0, i - 6); ecrirePremiersPas(s); return { i, p: s.p }; }
"""
BARRE = r"""
() => {
  const enPP = currentTheme && currentTheme.id === 'seance_premiers_pas';
  const segs = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts)
             : enPP ? segmentsSeance(currentCards, partsPremiersPas(currentCards)) : null;
  const noms = [...document.querySelectorAll('#seancePartsNoms > *')].map(x => x.textContent);
  return { segs: segs ? segs.map(s => s.p) : null, noms, titre: (document.getElementById('flashThemeTitle') || {}).textContent };
}
"""
JOUER = r"""
async ([rater]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const releves = [], fois = new Map(); let rates = 0;
  const barre = """ + BARRE.strip() + r""";
  for(let pas = 0; pas < 260; pas++){
    await pause(50);
    const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
    if(vis('flashcardEnd') || vis('finRevision')) break;
    if(currentFlashcard >= currentCards.length) break;
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr === 'sceneSeance'){
      releves.push(Object.assign(barre(), { carte: (c && c.forme) || 'arret' }));
      if(c && c.forme === 'pp_scene'){ break; }       // la fin de la scene de l'etape rouvre Premiers pas
      revenirDeLArret(); await pause(220); continue;
    }
    if(scr !== 'flashcards') break;
    releves.push(Object.assign(barre(), { carte: c.forme || c.mode }));
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){ try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){} nextFlashcard(); }
    else if(!fois.get(c) && rates < rater && !document.querySelector('#flashcardActions.presentation')){ fois.set(c, 1); rates++; reviewAgain(); }
    else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  return releves;
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8813)
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
    PERMIS = ["cartes", "grammaire", "images", "conv"]
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in ("de", "es"):
            for cas in ("ordinaire", "grammaire", "pp-jour1", "pp-etape"):
                for nuit in (False, True):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    err = []
                    page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.evaluate(PREPARER, ["ordinaire" if cas in ("ordinaire", "grammaire") else "pp"])
                    page.evaluate("([n]) => localStorage.setItem(THEME_STORAGE_KEY, n ? 'dark' : 'light')", [nuit])
                    page.reload()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1500)
                    if cas == "pp-etape":
                        page.evaluate(POSITION)
                    if cas == "grammaire":
                        # le cinquieme jour : les reperes et le son du jour entrent dans la seance
                        page.evaluate("() => { jourDApprentissage = () => 5; }")
                    page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
                    page.wait_for_timeout(1600)
                    tag = "%s-%s-%s" % (appris, cas, "nuit" if nuit else "jour")
                    if a.captures:
                        page.screenshot(path=os.path.join(a.captures, "barre-%s-1-debut.png" % tag))
                    debut = page.evaluate(BARRE)
                    if cas == "grammaire" and a.captures:
                        page.evaluate("async () => { const P = SEANCE_PARTS; const k = P.paquet.findIndex(c => P.parts.get(c) === 'grammaire'); if(k > 0){ segmentsSeance(P.paquet, P.parts).forEach(x => PASSAGES_VUS.add(x.p)); currentFlashcard = k; loadFlashcard(); await new Promise(r => setTimeout(r, 600)); } }")
                        page.screenshot(path=os.path.join(a.captures, "barre-%s-1b-grammaire.png" % tag))
                        page.evaluate("async () => { currentFlashcard = 0; loadFlashcard(); await new Promise(r => setTimeout(r, 400)); }")
                    rel = page.evaluate(JOUER, [3])
                    if a.captures:
                        page.screenshot(path=os.path.join(a.captures, "barre-%s-2-fin.png" % tag))
                    juge = []
                    d = debut["segs"] or []
                    if not d:
                        juge.append("pas de barre")
                    if any(x not in PERMIS for x in d):
                        juge.append("partie hors des quatre : %s" % d)
                    if [x for x in PERMIS if x in d] != d:
                        juge.append("ordre faux : %s" % d)
                    changes = [r for r in rel if r["segs"] and r["segs"] != d]
                    if changes:
                        juge.append("la barre change en route (%d fois, ex. %s)" % (len(changes), changes[0]["segs"]))
                    if cas == "grammaire" and "grammaire" not in d:
                        juge.append("pas de Grammaire le jour 5")
                    if cas == "pp-etape" and "conv" not in d:
                        juge.append("pas de Conversations le jour de l'etape")
                    er = sorted(set(x for x in err if "synonymes" not in x))
                    if er:
                        juge.append("erreurs JS %s" % er[:2])
                    fautes += 1 if juge else 0
                    print("== %-22s %s  barre %s  noms %s  (%d cartes relevees)" % (tag, "ok" if not juge else "FAUTE " + " ; ".join(juge), d, debut["noms"], len(rel)), flush=True)
                    ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
