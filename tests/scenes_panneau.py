# -*- coding: utf-8 -*-
"""Le panneau « Les scenes » en anglais et en portugais (retour d'une testeuse, 8 nov. 2026 : une barre blanche).

    python tests/scenes_panneau.py

Ces deux langues suivent une LISTE BLANCHE CSS (html[data-apprendre="en"] .orb-opt:not(...)) : une action qui n'y est
pas disparait sans rien dire. Sur un navigateur vierge, donc sans compte admin :
  - le panneau montre toutes les scenes moins les ecartees, et aucune ecartee ;
  - chaque ligne a son fichier scene-<nom>.<langue>.js ;
  - la premiere, celle du milieu et la derniere s'ouvrent : le cadre charge leur fichier, sans erreur.
Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
"""
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("SCENES_PORT", "8799"))
ECARTEES = {
    "en": ["kreuzung", "ubahn", "zug", "stadtplatz", "weihnachtsmarkt", "post"],
    "pt": ["winter"],
}


class Silencieux(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


PANNEAU = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  openOrbPanel('scenes'); await pause(500);
  const toutes = SCENES_TOUTES.map(s => ({ nom: s.nom, ouvrir: s.ouvrir }));
  const lignes = [...document.querySelectorAll('#orbPanelBody .orb-opt')];
  const vues = lignes.filter(o => o.offsetHeight > 0);
  const nomDe = o => { const c = o.getAttribute('onclick') || ''; const s = toutes.find(x => new RegExp('\\b' + x.ouvrir + '\\b').test(c)); return s ? s.nom : '?' + c; };
  return { apprendre: LANGUE_APPRISE, toutes: toutes.length, dom: lignes.length, noms: vues.map(nomDe),
           titre: document.getElementById('orbPanelTitle').textContent, hauteur: Math.round(document.getElementById('orbPanelBody').getBoundingClientRect().height) };
}
"""

OUVRIR = r"""
async ([rang]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  openOrbPanel('scenes'); await pause(500);
  const vues = [...document.querySelectorAll('#orbPanelBody .orb-opt')].filter(o => o.offsetHeight > 0);
  vues[rang].click();
  await pause(4000);
  const cadre = document.getElementById('sceneCadre'), actif = (document.querySelector('.screen.active') || {}).id;
  let texte = '';
  try{ texte = cadre.contentDocument.body.innerText.replace(/\s+/g, ' ').slice(0, 90); }catch(e){ texte = 'cadre illisible'; }
  return { actif, src: cadre.getAttribute('src').replace(/&t=\d+/, ''), texte };
}
"""


def main():
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Silencieux, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = 0

    def nouvelle(nav, app, journal):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 780}, service_workers="block")
        page = ctx.new_page()
        page.on("pageerror", lambda e: journal["erreurs"].append(str(e).split("\n")[0]))
        page.on("response", lambda r: journal["reponses"].append((r.status, r.url)))
        page.on("dialog", lambda d: d.dismiss())
        page.goto("http://127.0.0.1:%d/index.html?apprendre=%s" % (PORT, app))
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        return ctx, page

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for app in ("en", "pt"):
                journal = {"erreurs": [], "reponses": []}
                ctx, page = nouvelle(nav, app, journal)
                res = page.evaluate(PANNEAU)
                ctx.close()
                noms = res["noms"]
                attendu = res["toutes"] - len(ECARTEES[app])
                vues_ecartees = [n for n in noms if n in ECARTEES[app]]
                sans_fichier = [n for n in noms if not os.path.exists(os.path.join(RACINE, "visuel", "prototype", "scene-%s.%s.js" % (n, app)))]
                ok = res["apprendre"] == app and len(noms) == attendu and not vues_ecartees and not sans_fichier and not any(n.startswith("?") for n in noms)
                if not ok:
                    fautes += 1
                print("== %s %s : %d lignes visibles sur %d attendues (%d scenes, %d dans le panneau), ecartees visibles %s, sans fichier %s, hauteur %d px" % (
                    app, "ok" if ok else "FAUTE", len(noms), attendu, res["toutes"], res["dom"], vues_ecartees, sans_fichier, res["hauteur"]), flush=True)
                print("   " + " ".join(noms), flush=True)
                rangs = sorted({0, len(noms) // 2, len(noms) - 1}) if noms else []
                for rang in rangs:
                    journal = {"erreurs": [], "reponses": []}
                    ctx, page = nouvelle(nav, app, journal)
                    o = page.evaluate(OUVRIR, [rang])
                    fichier = "scene-%s.%s.js" % (noms[rang], app)
                    charge = [s for s, u in journal["reponses"] if fichier in u]
                    bon = o["actif"] == "sceneSeance" and ("scene=" + noms[rang]) in o["src"] and 200 in [s if s != 304 else 200 for s in charge] and not journal["erreurs"]
                    if not bon:
                        fautes += 1
                    print("   ouvre %-22s %s %s, fichier %s, erreurs %s" % (noms[rang], "ok" if bon else "FAUTE", json.dumps(o, ensure_ascii=False)[:230], charge, sorted(set(journal["erreurs"]))[:3]), flush=True)
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not fautes else "%d defaut(s)" % fautes))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
