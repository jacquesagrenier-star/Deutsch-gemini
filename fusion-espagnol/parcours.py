# -*- coding: utf-8 -*-
"""Le filet de la fusion : ouvre chaque tuile de l'accueil et chaque option
de son panneau, et releve ce que l'app affiche.

Pourquoi : a chaque etape de la fusion (voir PLAN.md), l'app allemande doit
rester IDENTIQUE pour ses testeurs. On ne le juge pas a l'oeil : on compare ce
releve a une reference prise avant de toucher quoi que ce soit.

    python fusion-espagnol/parcours.py --app de --sortie releve.json
    python fusion-espagnol/parcours.py --app es --sortie releve-es.json
    python fusion-espagnol/parcours.py --comparer reference.json releve.json

Ce que le releve contient, pour chaque chemin (tuile, puis tuile > option) :
l'ecran actif, son texte visible, et les erreurs JavaScript survenues.

⚠️ CE QUI LE REND FIABLE, et sans quoi une comparaison ne voudrait rien dire :
  - l'heure est FIGEE (horloge de Playwright) : salutation, dates, « il y a
    3 jours », adresses ?v=... ne bougent plus d'un passage a l'autre ;
  - le hasard est FIGE (Math.random remplace par un generateur a graine,
    remis a zero avant chaque chemin) : le meme paquet, les memes exercices
    dans le meme ordre ;
  - chaque chemin part d'un accueil neuf, dans un navigateur vierge (aucun
    stockage) : ce qu'un chemin a fait ne deteint pas sur le suivant.
On le verifie en le lancant DEUX FOIS sur la meme version : la comparaison
doit etre vide. Tant qu'elle ne l'est pas, l'instrument n'est pas etalonne.

Il ne se connecte PAS : l'app allemande exige un compte, mais ses ecrans
s'ouvrent par leurs fonctions, et aucun identifiant ne part chez Firebase.
L'app espagnole (le fork) a une porte a code : on y pose l'empreinte d'un
code valide lue dans la page elle-meme, sur le serveur local seulement.
"""
import argparse
import difflib
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8791
HEURE_FIGEE = "2026-10-10T09:00:00"

HASARD_FIGE = r"""
(() => {
  let graine = 20261010;
  const suivant = () => {            // mulberry32
    graine |= 0; graine = (graine + 0x6D2B79F5) | 0;
    let t = Math.imul(graine ^ (graine >>> 15), 1 | graine);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  Math.random = suivant;
  window.__regrainer = (g) => { graine = g; };
})();
"""

ETAT_ECRAN = r"""
() => {
  const s = document.querySelector(".screen.active");
  const texte = s ? s.innerText.replace(/[ \t ]+/g, " ").replace(/\n\s*\n+/g, "\n").trim() : "";
  return { ecran: s ? s.id : "(aucun)", texte };
}
"""


def serveur():
    gestion = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    gestion.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def releve(app):
    from playwright.sync_api import sync_playwright
    chemin_app = {"de": "index.html", "es": "espanol/index.html",
                  "es-moteur": "index.html?apprendre=es"}[app]
    adresse = "http://127.0.0.1:%d/%s" % (PORT, chemin_app)
    srv = serveur()
    resultats = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844},
                                  service_workers="block")
            ctx.add_init_script(HASARD_FIGE)
            page = ctx.new_page()
            page.clock.set_fixed_time(HEURE_FIGEE)
            erreurs = []
            page.on("pageerror", lambda e: erreurs.append("pageerror: " + str(e).split("\n")[0]))
            # Un fichier manquant : la console ne dit que « 404 », sans l'adresse.
            # On la prend dans la reponse, sans la partie ?v=... qui change.
            page.on("console", lambda m: erreurs.append("console: " + m.text[:200])
                    if m.type == "error" and not m.text.startswith("Failed to load resource") else None)
            page.on("response", lambda r: erreurs.append("HTTP %d %s" % (r.status, r.url.split("?")[0].replace("http://127.0.0.1:%d/" % PORT, "")))
                    if r.status >= 400 else None)
            page.on("dialog", lambda d: d.dismiss())

            page.goto(adresse)
            page.wait_for_load_state("networkidle")
            if app == "es":
                # La porte du fork : l'empreinte d'un code valide, lue dans la page.
                page.evaluate("() => localStorage.setItem(CLAVE_ACCESO, CODIGOS_VALIDOS[0])")
                page.reload()
                page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1500)

            def attendre():
                try:
                    page.wait_for_load_state("networkidle", timeout=8000)
                except Exception:
                    pass
                page.wait_for_timeout(400)

            def accueil():
                page.evaluate("() => { window.__regrainer(20261010); goHome(); }")
                attendre()

            def noter(chemin):
                etat = page.evaluate(ETAT_ECRAN)
                etat["chemin"] = chemin
                etat["erreurs"] = list(erreurs)
                erreurs.clear()
                resultats.append(etat)
                print("  %-55s %s" % (chemin[:55], etat["ecran"]))

            accueil()
            erreurs.clear()
            noter("accueil")
            tuiles = page.evaluate("""() => [...document.querySelectorAll('#home [data-orbid]')]
                .filter(e => e.offsetParent !== null).map(e => e.dataset.orbid)""")
            for orb in tuiles:
                accueil()
                erreurs.clear()
                page.evaluate("(id) => document.querySelector('#home [data-orbid=\"' + id + '\"]').click()", orb)
                attendre()
                noter(orb)
                n = page.evaluate("""() => document.querySelector('.screen.active') &&
                    document.querySelector('.screen.active').id === 'orbPanel'
                    ? document.querySelectorAll('#orbPanel .orb-opt').length : 0""")
                for i in range(n):
                    accueil()
                    page.evaluate("(id) => document.querySelector('#home [data-orbid=\"' + id + '\"]').click()", orb)
                    attendre()
                    nom = page.evaluate("(i) => document.querySelectorAll('#orbPanel .orb-opt')[i].innerText.split('\\n')[0].trim()", i)
                    erreurs.clear()
                    page.evaluate("(i) => document.querySelectorAll('#orbPanel .orb-opt')[i].click()", i)
                    attendre()
                    noter("%s > %d %s" % (orb, i + 1, nom))
            nav.close()
    finally:
        srv.shutdown()
    return resultats


def comparer(a, b):
    ra = {r["chemin"]: r for r in json.load(open(a, encoding="utf-8"))}
    rb = {r["chemin"]: r for r in json.load(open(b, encoding="utf-8"))}
    ecarts = 0
    for c in ra:
        if c not in rb:
            print("ABSENT de %s : %s" % (b, c)); ecarts += 1
    for c in rb:
        if c not in ra:
            print("NOUVEAU dans %s : %s" % (b, c)); ecarts += 1
    for c in ra:
        if c not in rb:
            continue
        x, y = ra[c], rb[c]
        if x["ecran"] != y["ecran"]:
            print("ECRAN %s : %s -> %s" % (c, x["ecran"], y["ecran"])); ecarts += 1
        if x["texte"] != y["texte"]:
            ecarts += 1
            print("TEXTE %s :" % c)
            for l in list(difflib.unified_diff(x["texte"].split("\n"), y["texte"].split("\n"), lineterm="", n=0))[2:14]:
                print("    " + l[:160])
        if x["erreurs"] != y["erreurs"]:
            ecarts += 1
            print("ERREURS %s : %s -> %s" % (c, x["erreurs"], y["erreurs"]))
    print("\n%d chemins, %d ecart(s)." % (len(ra), ecarts))
    return ecarts


def main():
    ap = argparse.ArgumentParser()
    # es = l'app espagnole actuelle (le fork, espanol/) ; es-moteur = le moteur
    # commun regle sur l'espagnol (?apprendre=es), qui doit la rattraper.
    ap.add_argument("--app", choices=["de", "es", "es-moteur"])
    ap.add_argument("--sortie")
    ap.add_argument("--comparer", nargs=2)
    a = ap.parse_args()
    if a.comparer:
        sys.exit(1 if comparer(*a.comparer) else 0)
    r = releve(a.app)
    with open(a.sortie, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    n_err = sum(len(x["erreurs"]) for x in r)
    print("\n%d chemins releves, %d erreur(s) JavaScript -> %s" % (len(r), n_err, a.sortie))


if __name__ == "__main__":
    main()
