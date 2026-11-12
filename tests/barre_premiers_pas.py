# -*- coding: utf-8 -*-
"""La barre de progression de la seance : Premiers pas, et son epaisseur (decisions de Jacques, 9 nov. 2026).

    python tests/barre_premiers_pas.py                 (de et es)
    python tests/barre_premiers_pas.py --captures DOSSIER

« On ne voit pas la barre de progression de seance pour les premiers pas. » Sur un navigateur vierge, sans compte :
  - Premiers pas : la barre est la des la premiere carte, elle avance, ne se pose pas sur l'en-tete, et le paquet garde son ordre ;
  - un seul element CSS pour toutes les barres : la meme epaisseur en Premiers pas et en seance du jour ;
  - 320 et 360 px, clair et nuit, RTL : pas de debordement.
Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
"""
import argparse
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
PORT = int(os.environ.get("BARRE_PP_PORT", "8803"))

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1'); localStorage.setItem(NIVEAU_DECLARE_KEY, 'zero'); }
"""

MESURE = r"""
async ([quoi]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas(); await chargerCiel();
  const lire = () => { const b = document.getElementById('seanceParts'), r = b.getBoundingClientRect(), f = b.children[0], ligne = document.querySelector('#flashcards .title-row').getBoundingClientRect();
    return { visible: !b.classList.contains('hidden') && r.height > 0, segs: [...b.children].map(x => x.className || '_').join(','), q: (b.querySelector('.ici') || { style: { getPropertyValue(){ return ''; } } }).style.getPropertyValue('--q'),
             epais: f ? Math.round(f.getBoundingClientRect().height) : 0, sous_entete: r.top >= ligne.bottom - 1, debord: document.documentElement.scrollWidth > window.innerWidth, large: Math.round(r.width), page: Math.round(document.querySelector('#flashcards').getBoundingClientRect().width), kicker: document.getElementById('flashKicker').textContent, titre: document.getElementById('flashThemeTitle').textContent }; };
  if(quoi === 'jour'){
    localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
    await ouvrirSeanceDuJour(); await pause(1400);
    return { depart: lire() };
  }
  if(!premiersPasEnCours()) ecrirePremiersPas({ a: true, p: 0 });
  await ouvrirPremiersPas(); await pause(1200);
  const avant = currentCards.slice();
  const formes = avant.map(c => c.forme || c.mode);
  const depart = lire();
  // on avance de 3 cartes, sans passer par une scene
  let etapes = 0;
  for(let k = 0; k < 3 && !/arret|pp_scene/.test(currentCards[currentFlashcard + 1].forme || ''); k++){ nextFlashcard(); await pause(200); etapes++; }
  const milieu = lire();
  const ouvert = (document.querySelector('.screen.active') || {}).id;
  return { formes: formes.slice(-4), taille: avant.length, memeOrdre: avant.every((c, i) => c === currentCards[i]), depart, etapes, milieu, ouvert, passage: !!document.querySelector('#cartePhrase .cp-passage') };
}
"""


def juger(r, quoi, largeur):
    f = []
    d = r["depart"]
    if not d["visible"]:
        f.append("barre absente")
    # 7 px depuis la decision de Jacques du 10 nov. 2026 (« je mettrai la barre de progression un peu moins large.
    # Donc, moins haute ») ; cette sonde du 9 nov. attendait encore 10.
    if d["epais"] != 7:
        f.append("epaisseur %s" % d["epais"])
    if not d["sous_entete"]:
        f.append("barre sur l'en-tete")
    if d["debord"]:
        f.append("debordement")
    if quoi == "pp":
        m = r["milieu"]
        if not m["visible"]:
            f.append("barre perdue en route")
        if r["etapes"] and m["q"] == d["q"]:
            f.append("la barre n'avance pas : %s" % m["q"])
        if not r["memeOrdre"]:
            f.append("l'ordre du paquet a change")
        if r["passage"]:
            f.append("un ecran de passage")
    return f


class Serveur(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *x, **k):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Serveur, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    total = 0
    CAS = [("de", "fr", "light", 360, "pp"), ("de", "fr", "dark", 320, "pp"), ("de", "ar", "dark", 320, "pp"), ("de", "ar", "light", 360, "pp"),
           ("es", "fr", "light", 360, "pp"), ("es", "fr", "dark", 320, "pp"), ("de", "fr", "light", 320, "jour"), ("de", "ar", "dark", 320, "jour"), ("es", "fr", "dark", 360, "jour")]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui, theme, largeur, quoi in CAS:
                ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": 780}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
                page.wait_for_load_state("networkidle")
                page.evaluate(PREPARER)
                page.evaluate("([l]) => localStorage.setItem(UI_LANG_KEY, l)", [ui])
                page.reload()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(1200)
                page.evaluate("([t]) => document.body.setAttribute('data-theme', t)", [theme])
                nom = "%s-%s-%s-%d-%s" % (appris, ui, theme, largeur, quoi)
                try:
                    r = page.evaluate(MESURE, [quoi])
                    fautes = juger(r, quoi, largeur)
                except Exception as e:
                    r = None
                    fautes = [str(e).split("\n")[0][:300]]
                total += 1 if fautes else 0
                print("== %s %s %s" % (nom, "ok" if not fautes else "FAUTE", fautes), flush=True)
                print("   " + json.dumps(r, ensure_ascii=False)[:800], flush=True)
                erreurs = [e for e in erreurs if "synonymes" not in e]
                if erreurs:
                    print("   erreurs JS", sorted(set(erreurs))[:4], flush=True)
                if a.captures and r:
                    os.makedirs(a.captures, exist_ok=True)
                    page.screenshot(path=os.path.join(a.captures, nom + ".png"))
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
