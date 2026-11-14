# -*- coding: utf-8 -*-
"""LA PARTIE IMAGES AVANCE PENDANT LA SCENE (Jacques, 12 nov. 2026, espagnol : « quand je suis passe a image, les images
n'avancent pas. Donc, la barre image reste noire. »).

Le bandeau du cadre (#sceneParts) recopie la barre de la seance. La sonde ouvre la seance du jour, va a la scene puis au
theme, et, depuis la page en cadre, envoie les messages qu'une vraie question envoie (« exercice », autant que le nombre
prevu, puis « fini ») ; en Premiers pas, le jour d'une etape, la conversation (« avance » apres chaque replique). Apres
chaque message, la part remplie de la partie en cours : elle doit monter a chaque question, ne jamais reculer, etre
pleine a la fin ; au retour aux cartes, la vraie barre ne doit pas etre en dessous. Le premier message est verifie
autrement : la page de scene l'envoie bien (on y repond a une vraie question, la premiere).
de et es, jour et nuit ; captures du bandeau a mi-scene.
Usage : python tests/images_avancent.py [--racine DOSSIER] [--port 8816] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
([pp]) => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(!pp) localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  else localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true })); }
"""
POSITION_ETAPE = """
async () => { await chargerPremiersPas(); const seq = sequencePremiersPas(); const i = seq.findIndex(x => x.forme === 'pp_scene' && x.jourPP === 0);
  const s = lirePremiersPas(); s.p = Math.max(0, i - 6); ecrirePremiersPas(s); }
"""
# La part remplie de la partie en cours, dans le bandeau et dans la barre des cartes.
BANDEAU = r"""
() => { const b = document.querySelector('#sceneParts i.ici'); const q = b ? parseFloat(b.style.getPropertyValue('--q')) : null;
  const pleins = document.querySelectorAll('#sceneParts i.fait').length;
  const fond = b ? getComputedStyle(b).backgroundImage.slice(0, 40) : '';
  return { q: q, fait: pleins, fond: fond }; }
"""
BARRE = r"""
() => { const b = document.querySelector('#seanceParts i.ici'); return { q: b ? parseFloat(b.style.getPropertyValue('--q')) : null,
  fait: document.querySelectorAll('#seanceParts i.fait').length, ecran: (document.querySelector('.screen.active') || {}).id }; }
"""
ALLER = r"""
async ([forme]) => {
  const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : partsPremiersPas(currentCards);
  const k = currentCards.findIndex(c => c && c.forme === forme);
  if(k < 0) return null;
  segmentsSeance(currentCards, parts).forEach(x => PASSAGES_VUS.add(x.p));
  currentFlashcard = k; loadFlashcard();
  await new Promise(r => setTimeout(r, 2500));
  const c = currentCards[k];
  return { k, nb: forme === 'theme_arret' ? (c.nb || 6) : forme === 'conv_arret' ? 0 : questionsSeance(),
           ecran: (document.querySelector('.screen.active') || {}).id, depuis: sceneOuverteDepuis };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8816)
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
            if f != page.main_frame and ("seance=1" in f.url or "pp=1" in f.url or "conversation" in f.url):
                return f
        return None

    def envoyer(page, type_, extra=None):
        f = cadre(page)
        msg = dict({"source": "wortando-scene", "type": type_}, **(extra or {}))
        f.evaluate("([m]) => parent.postMessage(m, '*')", [msg])
        page.wait_for_timeout(250)

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in ("de", "es"):
            for nuit in (False, True):
                for cas in ("seance", "pp-etape"):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    err = []
                    page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.evaluate(PREPARER, [cas != "seance"])
                    page.evaluate("([n]) => localStorage.setItem(THEME_STORAGE_KEY, n ? 'dark' : 'light')", [nuit])
                    page.reload()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1500)
                    if cas == "pp-etape":
                        page.evaluate(POSITION_ETAPE)
                    page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
                    page.wait_for_timeout(1500)
                    tag = "%s-%s-%s" % (appris, cas, "nuit" if nuit else "jour")
                    juge, vu = [], []
                    arrets = ["scene_arret", "theme_arret"] if cas == "seance" else ["theme_arret", "pp_scene", "conv_arret"]
                    for forme in arrets:
                        info = page.evaluate(ALLER, [forme])
                        if not info:
                            vu.append("%s absent" % forme)
                            continue
                        if info["ecran"] != "sceneSeance" or not cadre(page):
                            juge.append("%s : pas de cadre (%s)" % (forme, info["ecran"]))
                            continue
                        page.wait_for_timeout(800)
                        suite = [page.evaluate(BANDEAU)["q"]]
                        if forme == "conv_arret":
                            for f in (0.25, 0.5, 0.75, 1):
                                envoyer(page, "avance", {"f": f})
                                suite.append(page.evaluate(BANDEAU)["q"])
                        else:
                            for k in range(info["nb"]):
                                envoyer(page, "exercice", {"juste": k % 3 != 1})
                                if k % 3 != 1:
                                    envoyer(page, "bonne")
                                suite.append(page.evaluate(BANDEAU)["q"])
                                if a.captures and k == 1:
                                    page.screenshot(path=os.path.join(a.captures, "images-%s-%s-mi.png" % (tag, forme)))
                        if a.captures and forme == "conv_arret":
                            page.screenshot(path=os.path.join(a.captures, "images-%s-%s-fin.png" % (tag, forme)))
                        avant_fini = suite[-1]
                        bd = page.evaluate(BANDEAU)
                        # monte a chaque question, ne recule jamais
                        if any(y is None for y in suite):
                            juge.append("%s : pas de partie en cours dans le bandeau %s" % (forme, suite))
                        elif any(suite[i + 1] <= suite[i] for i in range(len(suite) - 1)):
                            juge.append("%s : la partie n'avance pas a chaque question %s" % (forme, suite))
                        if "gradient" not in bd["fond"]:
                            juge.append("%s : aplat au lieu du remplissage (%s)" % (forme, bd["fond"]))
                        envoyer(page, "fini", {"bons": 3, "faits": 5})
                        page.wait_for_timeout(1200)
                        apres = page.evaluate(BARRE)
                        # au retour, la barre des cartes : pas en dessous de ce que montrait le bandeau
                        if apres["ecran"] == "flashcards" and apres["q"] is not None and avant_fini is not None and apres["q"] + 0.5 < avant_fini and apres["fait"] == bd["fait"]:
                            juge.append("%s : la barre recule au retour (%s -> %s)" % (forme, avant_fini, apres["q"]))
                        vu.append("%s %s -> retour %s" % (forme, "/".join(str(int(x)) if x is not None else "?" for x in suite), apres))
                    er = sorted(set(x for x in err if "synonymes" not in x))
                    if er:
                        juge.append("erreurs JS %s" % er[:2])
                    fautes += 1 if juge else 0
                    print("== %-18s %s" % (tag, "ok" if not juge else "FAUTE " + " ; ".join(juge)), flush=True)
                    for v in vu:
                        print("     ", v, flush=True)
                    ctx.close()

        # La vraie page de scene envoie bien « exercice » a chaque question : on repond a la premiere.
        for appris in ("de", "es"):
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
            page = ctx.new_page()
            page.on("dialog", lambda d: d.dismiss())
            page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
            page.wait_for_load_state("networkidle")
            page.evaluate(PREPARER, [False])
            page.reload()
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1500)
            page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
            page.wait_for_timeout(1200)
            page.evaluate(ALLER, ["scene_arret"])
            page.wait_for_timeout(1500)
            f = cadre(page)
            q0 = page.evaluate(BANDEAU)["q"]
            touche = None
            if f:
                # Decouvrir d'abord s'il y en a un : on le passe ; puis on touche n'importe quelle zone (juste ou non,
                # chaque question envoie « exercice »).
                for _ in range(30):
                    page.wait_for_timeout(400)
                    # 14 nov. : on repond par la page elle-meme (toucher() sur une zone de la cible) -- un clic au
                    # centre de l'image ne tombait pas toujours sur une zone, et rien n'etait repondu.
                    rep = f.evaluate("""() => { try{ if(typeof attenteToucher !== 'undefined' && attenteToucher && !verrou){
                        const z = zonesDe(attenteToucher); if(z.length){ toucher(z[0], null); return 'toucher ' + attenteToucher; } } }catch(e){ return 'erreur ' + e; } return null; }""")
                    if rep:
                        touche = rep
                        page.wait_for_timeout(1500)
                        break
                    touche = f.evaluate("""() => { const b = [...document.querySelectorAll('button')].find(x => x.offsetHeight > 0 && /passer|commencer|continuer|weiter|empezar|start/i.test(x.textContent));
                        if(b){ b.click(); return 'bouton ' + b.textContent.trim().slice(0, 20); }
                        const z = document.querySelector('[data-mot], .zone, svg [data-z], canvas'); return z ? 'zone' : null; }""")
                    if touche == "zone":
                        box = f.evaluate("() => { const z = document.querySelector('[data-mot], .zone, svg [data-z], canvas'); const r = z.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; }")
                        fr = page.query_selector("#sceneCadre").bounding_box()
                        page.mouse.click(fr["x"] + box[0], fr["y"] + box[1])
                        page.wait_for_timeout(1500)
                        break
            q1 = page.evaluate(BANDEAU)["q"]
            ok = q0 is not None and q1 is not None and q1 > q0
            fautes += 0 if ok else 1
            print("== vraie scene %s %s  bandeau %s -> %s (%s)" % (appris, "ok" if ok else "A VOIR", q0, q1, touche), flush=True)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, "images-%s-vraie-scene.png" % appris))
            ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
