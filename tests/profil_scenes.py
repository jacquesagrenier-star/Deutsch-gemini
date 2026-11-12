# -*- coding: utf-8 -*-
"""LE PROFIL ET LES SCENES (decision de Jacques du 12 nov. 2026, « Oui, les deux »).
  « images » (ce que je vois) : DEUX scenes differentes par seance du jour, avant le theme -- la partie Images plus
  longue, la meme barre ; en Premiers pas, deux scenes (celle de l'etape compte) ;
  « tout », « oreille », « regles » : une scene ; en Premiers pas, une scene toutes les 8 cartes (plus 12).
Pour chaque profil (de et es), une seance ordinaire et une seance de Premiers pas (premiere seance, puis la seance qui
finit l'etape 1) : le nombre de scenes, leurs noms (deux differentes), la barre fixee du debut a la fin, et la partie
Images qui avance jusqu'au bout -- a chaque arret, la page en cadre envoie ses messages (« exercice », « avance »), et
le bandeau doit monter ; au dernier arret des images, il finit plein. La ligne du plan, sur l'accueil, dit « deux
scenes » au profil images.
Usage : python tests/profil_scenes.py [--racine DOSSIER] [--port 8817] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
([pp, profil]) => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(!pp) localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  else localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true }));
  if(profil) localStorage.setItem(PROFIL_KEY, JSON.stringify({ f: profil })); }
"""
POSITION_ETAPE = """
async () => { await chargerPremiersPas(); const seq = sequencePremiersPas(); const i = seq.findIndex(x => x.forme === 'pp_scene' && x.jourPP === 0);
  const s = lirePremiersPas(); s.p = Math.max(0, i - 14); ecrirePremiersPas(s); }
"""
ETAT = r"""
() => {
  const enPP = currentTheme && currentTheme.id === 'seance_premiers_pas';
  const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : enPP ? partsPremiersPas(currentCards) : null;
  const segs = parts ? segmentsSeance(currentCards, parts).map(s => s.p) : null;
  const scenes = currentCards.filter(c => c && /^(scene_arret|pp_scene)$/.test(c.forme || '')).map(c => c.scene ? (c.scene.nom || c.scene) : '?');
  return { segs, scenes, themes: currentCards.filter(c => c && c.forme === 'theme_arret').length,
           convs: currentCards.filter(c => c && c.forme === 'conv_arret').length, n: currentCards.length };
}
"""
BANDEAU = r"""
() => { const b = document.querySelector('#sceneParts i.ici'); return b ? parseFloat(b.style.getPropertyValue('--q')) : null; }
"""
JOUER_CARTES = r"""
async () => {
  // joue les cartes jusqu'au prochain arret (ou la fin) ; rend l'arret atteint
  const pause = ms => new Promise(r => setTimeout(r, ms));
  for(let pas = 0; pas < 200; pas++){
    await pause(40);
    const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
    if(vis('flashcardEnd') || vis('finRevision')) return { fin: true };
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    if(scr === 'sceneSeance') return { arret: c ? c.forme : '?', k: currentFlashcard, nb: c && c.forme === 'theme_arret' ? (c.nb || 6) : questionsSeance() };
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr !== 'flashcards' || !c) return { fin: true, ecran: scr };
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){
      if(/^(scene_arret|theme_arret|conv_arret|pp_scene)$/.test(c.forme || '')){ loadFlashcard(); await pause(1500); continue; }
      if(c.forme === 'gram'){ const b = document.querySelector('#cartePhrase .cp-choix button'); if(b){ b.click(); await pause(120); } }
      try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){}
      nextFlashcard();
    } else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(40);
  }
  return { fin: true, trop: true };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8817)
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

    def cadre(page):
        for f in page.frames:
            if f != page.main_frame and ("seance=1" in f.url or "conversation" in f.url or "pp=" in f.url or "scene=" in f.url):
                return f
        fr = [f for f in page.frames if f != page.main_frame and f.url and f.url != "about:blank"]
        return fr[-1] if fr else None

    def envoyer(page, type_, extra=None):
        f = cadre(page)
        if not f:
            return False
        f.evaluate("([m]) => parent.postMessage(m, '*')", [dict({"source": "wortando-scene", "type": type_}, **(extra or {}))])
        page.wait_for_timeout(200)
        return True

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in ("de", "es"):
            for profil in ("images", "tout", "oreille", "regles"):
                for cas in ("ordinaire", "pp-jour1", "pp-etape"):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    err = []
                    page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.evaluate(PREPARER, [cas != "ordinaire", profil])
                    page.reload()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1800)
                    if cas == "pp-etape":
                        page.evaluate(POSITION_ETAPE)
                    plan = page.evaluate("() => { try{ PLAN_CACHE = null; return planSeanceDuJour(); }catch(e){ return 'err ' + e; } }")
                    page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
                    page.wait_for_timeout(1500)
                    tag = "%s-%s-%s" % (appris, profil, cas)
                    debut = page.evaluate(ETAT)
                    juge = []
                    d = debut["segs"] or []
                    sc = debut["scenes"]
                    if cas == "ordinaire":
                        attendu = 2 if profil == "images" else 1
                        if len(sc) != attendu:
                            juge.append("%d scene(s) au lieu de %d %s" % (len(sc), attendu, sc))
                        if profil == "images" and "deux" not in str(plan) and "dos" not in str(plan):
                            juge.append("le plan ne dit pas deux scenes : %s" % plan)
                        if profil != "images" and ("deux" in str(plan)):
                            juge.append("le plan dit deux scenes : %s" % plan)
                    else:
                        if len(sc) > (2 if profil == "images" else 1):
                            juge.append("%d scenes en Premiers pas %s" % (len(sc), sc))
                    if len(set(sc)) != len(sc):
                        juge.append("deux fois la meme scene %s" % sc)
                    if "images" not in d:
                        juge.append("pas de partie Images %s" % d)
                    # la seance jouee : la barre ne change pas, la partie Images avance jusqu'au bout
                    suites, derniere = [], None
                    for _ in range(8):
                        r = page.evaluate(JOUER_CARTES)
                        e = page.evaluate(ETAT)
                        if e["segs"] and e["segs"] != d:
                            juge.append("la barre change %s -> %s" % (d, e["segs"]))
                            break
                        if r.get("fin"):
                            break
                        page.wait_for_timeout(900)
                        q = [page.evaluate(BANDEAU)]
                        if r["arret"] == "conv_arret":
                            for f in (0.5, 1):
                                envoyer(page, "avance", {"f": f})
                                q.append(page.evaluate(BANDEAU))
                        else:
                            for k in range(r["nb"]):
                                envoyer(page, "exercice", {"juste": True})
                                q.append(page.evaluate(BANDEAU))
                        if a.captures and r["arret"] in ("scene_arret", "pp_scene"):
                            page.screenshot(path=os.path.join(a.captures, "profil-%s-%s-%d.png" % (tag, r["arret"], r["k"])))
                        suites.append((r["arret"], q))
                        if any(x is None for x in q) or any(q[i + 1] < q[i] for i in range(len(q) - 1)) or q[-1] <= q[0]:
                            juge.append("%s : la partie n'avance pas %s" % (r["arret"], q))
                        envoyer(page, "fini", {"bons": 1, "faits": 1})
                        page.wait_for_timeout(1500)
                        if r["arret"] in ("scene_arret", "theme_arret", "pp_scene"):
                            derniere = q[-1]
                    if derniere is not None and derniere < 99.5:
                        juge.append("Images ne finit pas pleine (%s)" % derniere)
                    er = sorted(set(x for x in err if "synonymes" not in x))
                    if er:
                        juge.append("erreurs JS %s" % er[:2])
                    fautes += 1 if juge else 0
                    print("== %-26s %s  barre %s  scenes %s  themes %d  conv %d  %d cartes" % (tag, "ok" if not juge else "FAUTE " + " ; ".join(juge), d, sc, debut["themes"], debut["convs"], debut["n"]), flush=True)
                    if cas == "ordinaire":
                        print("      plan :", plan, flush=True)
                    for arr, q in suites:
                        print("      %-12s %s" % (arr, "/".join(str(int(x)) if x is not None else "?" for x in q)), flush=True)
                    ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
