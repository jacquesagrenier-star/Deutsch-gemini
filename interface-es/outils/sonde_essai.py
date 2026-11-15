# -*- coding: utf-8 -*-
"""Sonde de l'essai « espagnol, langue d'interface de l'allemand » (lot 0, 15 nov. 2026).

    python interface-es/outils/sonde_essai.py [--port 8806]

Ce qu'elle prouve, dans un navigateur sans compte (donc pas l'admin) :
  1. allemand appris, telephone en es-MX, SANS la cle d'essai : rien ne change --
     « es » n'est pas dans UI_LANGS, l'app s'ouvre en anglais comme avant, les
     boutons « Español » restent caches ;
  2. allemand appris AVEC la cle d'essai : « es » entre dans UI_LANGS, l'app
     s'ouvre en espagnol, t() parle espagnol, une carte sans traduction
     espagnole retombe sur l'anglais (repli es -> en -> fr) ;
  3. espagnol appris (?apprendre=es) en es-MX : ses langues d'interface ne
     bougent pas, meme avec la cle d'essai posee ;
  4. anglais appris (?apprendre=en) : le repli de l'espagnol reste es -> fr.

Sous le verrou des navigateurs (~/.wortando/REGLE-VERROU-PARCOURS.txt) : le
prendre avant, le rendre apres. Port propre (jamais 8791, celui des parcours).
"""
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8806


class Silencieux(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serveur():
    gest = functools.partial(Silencieux, directory=RACINE)
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gest)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


RELEVE = """() => ({
    apprise: LANGUE_APPRISE,
    uiLangs: UI_LANGS.join(","),
    ui: getUiLang(),
    lang: document.documentElement.lang,
    essai: typeof ESSAI_INTERFACE_ES === "undefined" ? null : ESSAI_INTERFACE_ES,
    repliEs: (REPLI_LANGUE.es || []).join(","),
    boutonsEsVisibles: Array.from(document.querySelectorAll('.setup-choice[onclick*="selectUiLangChoice(\\'es\\')"]'))
        .filter(b => !b.classList.contains("hidden")).length,
    titre: t("plc_titre"),
    carte: (() => {
        try{
            const th = themesComptes()[0]; const lv = th.levels[Object.keys(th.levels)[0]];
            const w = lv.words[0];
            return w[0] + " -> " + texteCarte(w, "nomen", "traduction", getUiLang()) + " [" + langueCarte(w, "nomen", "traduction", getUiLang()) + "]";
        }catch(e){ return "?" + e; }
    })()
})"""


def ouvrir(nav, chemin, avant=None):
    ctx = nav.new_context(locale="es-MX", viewport={"width": 390, "height": 844}, service_workers="block")
    page = ctx.new_page()
    erreurs = []
    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
    page.goto("http://127.0.0.1:%d/%s" % (PORT, chemin))
    page.wait_for_load_state("networkidle")
    if avant:
        page.evaluate(avant)
        page.reload()
        page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2500)
    r = page.evaluate(RELEVE)
    r["erreurs"] = erreurs
    ctx.close()
    return r


def main():
    srv = serveur()
    fautes = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        cas = [
            ("1. allemand, es-MX, sans essai", "index.html", None),
            ("2. allemand, es-MX, avec essai", "index.html",
             "() => localStorage.setItem('deutschAI_essaiInterfaceEs', '1')"),
            ("3. espagnol appris, es-MX, cle d'essai posee", "index.html?apprendre=es",
             "() => localStorage.setItem('deutschAI_essaiInterfaceEs', '1')"),
            ("4. anglais appris, es-MX", "index.html?apprendre=en", None),
        ]
        res = {}
        for nom, chemin, avant in cas:
            r = ouvrir(nav, chemin, avant)
            res[nom] = r
            print(nom)
            print("   " + json.dumps(r, ensure_ascii=False))
        nav.close()
    srv.shutdown()

    a, b, c, d = (res[k] for k, _, _ in cas)
    def attendu(cond, msg):
        if not cond:
            fautes.append(msg)
    attendu(a["uiLangs"] == "fr,en,tr,uk,fa,ar,pt,pl,ru", "1 : UI_LANGS a change sans l'essai")
    attendu(a["ui"] == "en", "1 : un telephone es-MX ne s'ouvre plus en anglais")
    attendu(a["boutonsEsVisibles"] == 0, "1 : un bouton Español est visible sans l'essai")
    attendu(a["essai"] is False, "1 : l'essai est ouvert sans la cle")
    attendu(b["uiLangs"].endswith(",ru,es") and b["ui"] == "es", "2 : l'essai n'ouvre pas l'espagnol")
    attendu(b["lang"] == "es", "2 : <html lang> n'est pas es")
    attendu(b["boutonsEsVisibles"] == 2, "2 : les deux boutons Español ne sont pas visibles")
    attendu(b["repliEs"] == "es,en,fr", "2 : le repli de l'espagnol n'est pas es,en,fr")
    attendu(b["titre"] == "Encuentra tu nivel", "2 : t() ne parle pas espagnol")
    attendu(c["uiLangs"] == "fr,en,pt,ar,de" and c["essai"] is False, "3 : l'espagnol appris a change")
    attendu(d["uiLangs"] == "fr,es" and d["repliEs"] == "es,fr", "4 : l'anglais appris a change")
    for k, r in res.items():
        if r["erreurs"]:
            fautes.append("%s : erreurs JavaScript %s" % (k, r["erreurs"][:3]))
    print()
    if fautes:
        print("ECHEC :\n  " + "\n  ".join(fautes))
        sys.exit(1)
    print("OK : l'essai est inerte sans la cle, et l'espagnol s'ouvre avec elle.")


if __name__ == "__main__":
    main()
