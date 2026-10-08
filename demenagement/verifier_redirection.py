# -*- coding: utf-8 -*-
"""Controle du depot de redirection, avant de le copier dans le nouveau depot.

    python demenagement/verifier_redirection.py

Aucune dependance, lecture seule. Ne remplace pas l'essai dans un navigateur
(JOUR-J.md, etape « Verifier ») : il attrape les oublis de copie.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(ICI, "depot-redirection")
CIBLE = "https://deutsch-gemini.pages.dev/"


def lire(*p):
    with open(os.path.join(D, *p), encoding="utf-8") as f:
        return f.read()


def main():
    pb = []
    for f in ["index.html", "404.html", "firebase-messaging-sw.js",
              os.path.join("espanol", "sw.js"), "version.json",
              os.path.join("espanol", "version.json"), ".nojekyll"]:
        if not os.path.isfile(os.path.join(D, f)):
            pb.append("fichier absent : " + f)
    if pb:
        print("\n".join(pb))
        return 1

    # 404.html sert toutes les adresses absentes : il doit etre la meme page.
    if lire("index.html") != lire("404.html"):
        pb.append("index.html et 404.html different (ils doivent etre identiques)")
    # Les deux anciens service workers sont remplaces par le meme fichier.
    if lire("firebase-messaging-sw.js") != lire("espanol", "sw.js"):
        pb.append("firebase-messaging-sw.js et espanol/sw.js different")
    sw = lire("firebase-messaging-sw.js")
    for mot in ["unregister", "caches.delete", "skipWaiting"]:
        if mot not in sw:
            pb.append("service worker de remplacement : « %s » absent" % mot)
    if re.search(r'addEventListener\(\s*"fetch"', sw):
        pb.append("le service worker de remplacement ne doit PAS intercepter les requetes")

    page = lire("index.html")
    adresses = set(re.findall(r"https://[a-z0-9.-]+\.pages\.dev/", page))
    if adresses != {CIBLE}:
        pb.append("adresse cible inattendue dans la page : %s" % sorted(adresses))
    if "location.replace" not in page or 'http-equiv="refresh"' not in page:
        pb.append("la page doit avoir location.replace ET la balise refresh")

    # Un numero tres haut : les anciennes apps encore ouvertes rechargent avec
    # ?v=..., qui court-circuite leur cache et les amene sur la redirection.
    for v in ["version.json", os.path.join("espanol", "version.json")]:
        try:
            n = int(json.loads(lire(v))["version"])
            if n < 100000:
                pb.append(v + " : numero trop bas (%d)" % n)
        except Exception as e:
            pb.append(v + " illisible : %s" % e)

    # La constante de l'app : son etat, pour qu'on sache ou on en est.
    with open(os.path.join(ICI, "..", "index.html"), encoding="utf-8") as f:
        app = f.read()
    m = re.search(r'const ADRESSE_DEFINITIVE = "([^"]*)";', app)
    if not m:
        pb.append("index.html : ADRESSE_DEFINITIVE introuvable")
    elif m.group(1) and not (m.group(1).startswith("https://") and m.group(1).endswith("/")):
        pb.append("index.html : ADRESSE_DEFINITIVE doit commencer par https:// et finir par /")

    if pb:
        print("\n".join(pb))
        return 1
    etat = (m.group(1) or "vide (inerte)")
    print("Depot de redirection : aucun probleme. ADRESSE_DEFINITIVE : " + etat)
    return 0


if __name__ == "__main__":
    sys.exit(main())
