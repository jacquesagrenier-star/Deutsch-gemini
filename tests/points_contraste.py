# -*- coding: utf-8 -*-
"""LES QUATRE POINTS ET LEUR MOT SUR LE FOND DE CHAQUE PARTIE (retour de Jacques, 11 nov. 2026 : « dans la revision,
on ne voyait pas bien, mais dans les mots, on voit suffisamment » ; « c'est vraiment une question de visibilite »).

Au verso d'une carte de la seance, le bouton « Je savais » porte la bille, les quatre points et, apres un ✓, le mot du
point (Vu, Revu, Retenu, Maitrise). Le bouton est un verre presque transparent : ce qu'on voit derriere, c'est le
paysage de la partie. Pour chaque partie (mots, revisions, verbes, son, Premiers pas, scene, theme), de jour et de nuit,
la sonde pose le paysage, allume un point et ecrit le mot, puis mesure le contraste de chacun contre le fond REELLEMENT
peint derriere lui (une capture de la zone, points et mot caches, sa couleur moyenne).

Seuil : celui de la partie Mots, que Jacques juge assez visible (voir SEUIL).
Usage : python tests/points_contraste.py [--racine DOSSIER] [--port 8805] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PARTIES = ["mots", "rev", "conj", "son", "pp", "scene", "theme"]
# Le seuil : celui de la partie Mots de jour, que Jacques juge assez visible (« dans les mots, on voit suffisamment »),
# mesure a 2,99:1 pour le mot. On corrige ce qui passe dessous ; 4,5:1 (le seuil WCAG d'un petit texte) est affiche a part.
SEUIL = 2.95

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
        localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true })); }
"""
OUVRIR = """
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1500);
  const k = currentCards.findIndex(c => c && c.mode !== 'phrase' && !c.forme);
  if(k < 0) return { faute: 'pas de carte de mot' };
  // un mot deja vu une fois : un point allume, trois vides
  const c = currentCards[k], st = getWordState(c.themeId, c.index); st.vu = true; st.srsHits = 1; st.reviews = 1; setWordState(c.themeId, c.index, st);
  currentFlashcard = k; loadFlashcard(); await pause(500);
  flipCard(); await pause(700);
  return { k };
}
"""
POSER = """
async ([cle, nuit]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  setAppTheme(nuit ? 'dark' : 'light'); await pause(150);
  PAYSAGE_MONTRE = null; paysageSeance(cle); await pause(150);
  majEcheances(1); await pause(600);
  const pips = [...document.querySelectorAll('#flashcardActions .judge-good .srs-pip')];
  const on = pips.find(p => p.classList.contains('on')), off = pips.find(p => !p.classList.contains('on'));
  const txt = document.querySelector('#flashcardActions .judge-good .srs-ladder-text');
  const r = el => { const b = el.getBoundingClientRect(); return { x: b.left, y: b.top, w: b.width, h: b.height }; };
  const bouton = document.querySelector('#flashcardActions .judge-good');
  return { on: on ? getComputedStyle(on).backgroundColor : null, off: off ? getComputedStyle(off).backgroundColor : null,
           mot: txt ? getComputedStyle(txt).color : null, texte: txt ? txt.textContent : '',
           rPips: r(document.querySelector('#flashcardActions .judge-good .srs-pips')), rMot: txt ? r(txt) : null, rBouton: r(bouton) };
}
"""
CACHER = """([v]) => { document.querySelectorAll('#flashcardActions .judge-good .srs-pips, #flashcardActions .judge-good .srs-ladder-text, #flashcardActions .judge-good .judge-bille')
  .forEach(e => { e.style.visibility = v ? 'hidden' : ''; }); }"""


def rgb(s):
    if not s:
        return None
    v = s[s.index("(") + 1:s.index(")")].split(",")
    return tuple(float(x) for x in v[:3]) + ((float(v[3]),) if len(v) > 3 else (1.0,))


def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return round((la + 0.05) / (lb + 0.05), 2)


def melange(c, fond):
    a = c[3]
    return tuple(c[i] * a + fond[i] * (1 - a) for i in range(3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8805)
    ap.add_argument("--captures")
    ap.add_argument("--langues", default="de,es")
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
    from PIL import Image
    import io
    fautes = 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in a.langues.split(","):
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, device_scale_factor=2, service_workers="block")
            page = ctx.new_page()
            erreurs = []
            page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
            page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else ""))
            page.wait_for_load_state("networkidle")
            page.evaluate(PREPARER)
            page.reload()
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1200)
            o = page.evaluate(OUVRIR)
            if "faute" in o:
                print("==", appris, o)
                fautes += 1
                continue
            for nuit in (False, True):
                for cle in PARTIES:
                    m = page.evaluate(POSER, [cle, nuit])
                    page.evaluate(CACHER, [True])
                    def moyenne(r):
                        if not r or r["w"] < 1:
                            return None
                        png = page.screenshot(clip={"x": r["x"], "y": r["y"], "width": r["w"], "height": r["h"]})
                        im = Image.open(io.BytesIO(png)).convert("RGB")
                        px = list(im.get_flattened_data()) if hasattr(im, 'get_flattened_data') else list(im.getdata())
                        return tuple(sum(c[i] for c in px) / len(px) for i in range(3))
                    fp, fm = moyenne(m["rPips"]), moyenne(m["rMot"])
                    page.evaluate(CACHER, [False])
                    on, off, mot = rgb(m["on"]), rgb(m["off"]), rgb(m["mot"])
                    q_on = ratio(melange(on, fp), fp) if on and fp else None
                    q_off = ratio(melange(off, fp), fp) if off and fp else None
                    q_mot = ratio(melange(mot, fm), fm) if mot and fm else None
                    ok = (q_on or 0) >= SEUIL and (q_mot or 0) >= SEUIL
                    fautes += 0 if ok else 1
                    print("%s %-5s %-6s %s  mot %-5s %5s:1  point %5s:1  vide %5s:1  fond %s" % (
                        "ok   " if ok else "FAUX ", appris, cle, "nuit" if nuit else "jour", m["texte"], q_mot, q_on, q_off,
                        tuple(round(x) for x in fp) if fp else None), flush=True)
                    if a.captures:
                        b = m["rBouton"]
                        page.screenshot(path=os.path.join(a.captures, "points-%s-%s-%s.png" % (appris, cle, "nuit" if nuit else "jour")),
                                        clip={"x": max(0, b["x"] - 8), "y": max(0, b["y"] - 8), "width": b["w"] + 16, "height": b["h"] + 16})
            err = sorted(set(e for e in erreurs if "synonymes" not in e))
            if err:
                print("   erreurs JS :", err[:4], flush=True)
            ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas sous le seuil" % fautes)


if __name__ == "__main__":
    main()
