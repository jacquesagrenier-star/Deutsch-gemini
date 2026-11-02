# -*- coding: utf-8 -*-
"""Les scenes au telephone (375 x 812) : chaque zone touchee en « Decouvrir »,
son etiquette mesuree.

    python retours/qualite-es-de/scenes_visuel.py --app de --langues fr,ar,ru [--captures dossier]

  zone_vide        le masque de la zone n'a aucun pixel (on ne peut pas la toucher)
  zone_cadre       le cadre de la zone sort de l'image
  zone_cachee      au centre de son cadre, le doigt tombe sur une AUTRE zone et
                   jamais sur celle-ci (signal faible : un objet en L n'a pas de centre)
  etiquette_hors   l'etiquette sort de l'ecran ou de la scene
  etiquette_bas    l'etiquette passe sous la barre du bas
  etiquette_vide   l'etiquette n'a pas de texte
  sens             ar / fa : la page n'est pas en droite a gauche
Une capture par scene et par langue est prise si --captures (etiquette du
premier objet affichee).
"""
import argparse
import functools
import glob
import http.server
import json
import os
import socketserver
import sys
import threading

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MESURE = r"""
() => {
  const out = [];
  const sc = document.querySelector('#scene') || document.querySelector('.scene');
  const c = sc ? sc.getBoundingClientRect() : {left: 0, right: innerWidth, top: 0, bottom: innerHeight};
  const bas = [...document.querySelectorAll('.bas')].filter(b => b.getClientRects().length)
                .map(b => b.getBoundingClientRect().top).sort((a, b) => a - b)[0] || innerHeight;
  if ((document.documentElement.lang === 'ar' || document.documentElement.lang === 'fa') && document.documentElement.dir !== 'rtl')
    out.push({code: 'sens'});
  for (const p of ZONES){
    if (!p.pixels) { out.push({code: 'zone_vide', zone: p.id, mot: p.mot}); continue; }
    const [x, y, w, h] = p.cadre;
    if (x < -0.5 || y < -0.5 || x + w > 100.5 || y + h > 100.5) out.push({code: 'zone_cadre', zone: p.id, mot: p.mot, detail: p.cadre.map(Math.round).join(',')});
    const s = sous(x + w / 2, y + h / 2);
    const tout = [...s.exact, ...s.proche];
    if (tout.length && !tout.includes(p) && !p.sur) out.push({code: 'zone_cachee', zone: p.id, mot: p.mot, detail: 'centre sur ' + tout[0].mot});
    try { toucher(p.id, null); } catch (e) { out.push({code: 'erreur', zone: p.id, detail: String(e).slice(0, 80)}); continue; }
    const e = document.querySelector('.etiquette');
    if (!e) { out.push({code: 'etiquette_absente', zone: p.id, mot: p.mot}); continue; }
    const r = e.getBoundingClientRect(), t = e.innerText.trim();
    if (!t) out.push({code: 'etiquette_vide', zone: p.id, mot: p.mot});
    if (r.left < -1 || r.right > innerWidth + 1 || r.left < c.left - 1 || r.right > c.right + 1 || r.top < c.top - 1)
      out.push({code: 'etiquette_hors', zone: p.id, mot: p.mot, texte: t.slice(0, 60), detail: [r.left, r.top, r.right, r.bottom].map(Math.round).join(',')});
    else if (r.bottom > Math.min(bas, c.bottom) + 1 && r.top < bas)
      out.push({code: 'etiquette_bas', zone: p.id, mot: p.mot, texte: t.slice(0, 60), detail: Math.round(r.bottom) + '>' + Math.round(Math.min(bas, c.bottom))});
  }
  return {zones: ZONES.length, signalements: out};
}
"""


def serveur(port):
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    h.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", port), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def scenes(app):
    noms = []
    for f in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "*.points.json"))):
        n = os.path.basename(f)[:-len(".points.json")]
        js = os.path.join(RACINE, "visuel", "prototype", "scene-%s%s.js" % (n, ".es" if app == "es" else ""))
        if os.path.exists(js):
            noms.append(n)
    return noms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", choices=["de", "es"], required=True)
    ap.add_argument("--langues", default="fr")
    ap.add_argument("--port", type=int, default=8797)
    ap.add_argument("--sortie")
    ap.add_argument("--captures")
    ap.add_argument("--scenes")
    a = ap.parse_args()
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)
    from playwright.sync_api import sync_playwright
    srv = serveur(a.port)
    res = {}
    liste = a.scenes.split(",") if a.scenes else scenes(a.app)
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for lg in a.langues.split(","):
                ctx = nav.new_context(viewport={"width": 375, "height": 812}, is_mobile=True, has_touch=True,
                                      device_scale_factor=2, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0][:150]))
                n_sig = 0
                for nom in liste:
                    url = "http://127.0.0.1:%d/visuel/prototype/index.html?scene=%s&lang=%s%s" % (
                        a.port, nom, lg, "&apprendre=es" if a.app == "es" else "")
                    erreurs.clear()
                    try:
                        page.goto(url)
                        page.wait_for_load_state("networkidle", timeout=15000)
                        page.wait_for_timeout(600)
                        m = page.evaluate(MESURE)
                    except Exception as e:
                        m = {"zones": 0, "signalements": [{"code": "erreur", "detail": str(e).split("\n")[0][:150]}]}
                    m["erreurs_js"] = list(erreurs)
                    res["%s|%s" % (nom, lg)] = m
                    n_sig += len(m["signalements"])
                    if a.captures:
                        try:
                            page.evaluate("() => { try{ effacer(); toucher(ZONES[0].id, null); }catch(e){} }")
                            page.wait_for_timeout(200)
                            page.screenshot(path=os.path.join(a.captures, "scene-%s-%s-%s.png" % (a.app, nom, lg)))
                        except Exception:
                            pass
                print("%s %s : %d scenes, %d signalements" % (a.app, lg, len(liste), n_sig), flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    if a.sortie:
        json.dump(res, open(a.sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
