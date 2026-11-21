# -*- coding: utf-8 -*-
"""L'origine des noms d'etoiles (ligne 160, livraison B) : RELEVE, a relancer seulement pour rafraichir.

    python etoiles/outils/wgsn_origines.py [page.html]

Le catalogue des noms d'etoiles de l'Union astronomique internationale, tenu par son groupe de travail WGSN, donne pour
chaque nom son origine, sa langue et sa reference (le plus souvent Kunitzsch & Smart 2006, A Dictionary of Modern Star
Names) : https://exopla.net/star-names/modern-iau-star-names/ (version du 15 oct. 2026, relevee le 20 nov.).
Ecrit etoiles/sources/wgsn_origines.tsv : une ligne par etoile nommee de ciel.json (nom, designation WGSN, origine, langue,
reference, date d'adoption). Les lignes affichees sont ecrites a nos mots dans etoiles/outils/origines.py, d'apres ce
fichier ; une etoile sans origine sure (absente du catalogue, ou « unknown ») n'en a pas.
"""
import csv
import html
import json
import os
import re
import sys
import time
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
URL = "https://exopla.net/star-names/modern-iau-star-names/"


def lignes(page):
    tab = {}
    for r in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        c = [html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x))).strip() for x in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
        if len(c) > 10 and c[0]:
            tab[c[0]] = c
    return tab


def main():
    if len(sys.argv) > 1:
        page = open(sys.argv[1], encoding="utf-8").read()
    else:
        with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "wortando-etoiles/1.0"}), timeout=120) as r:
            page = r.read().decode("utf-8")
    tab = lignes(page)
    ciel = json.load(open(os.path.join(RACINE, "ciel.json"), encoding="utf-8"))
    noms = []
    for c in ciel["constellations"].values():
        for e in c["etoiles"]:
            if not e.get("noms") and e["nom"] not in noms:
                noms.append(e["nom"])
    sortie = os.path.join(RACINE, "sources", "wgsn_origines.tsv")
    with open(sortie, "w", encoding="utf-8", newline="") as f:
        f.write("# Origine des noms d'etoiles, catalogue de l'UAI (WGSN), %s, releve du %s par etoiles/outils/wgsn_origines.py.\n" % (URL, time.strftime("%Y-%m-%d")))
        f.write("# Colonnes : nom, designation, origine (texte du WGSN), langue, reference, date d'adoption. Absent = pas dans le catalogue.\n")
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["nom", "designation", "origine", "langue", "reference", "adopte"])
        absents = []
        for n in noms:
            c = tab.get(n)
            if not c:
                absents.append(n)
                w.writerow([n, "", "", "absent", "", ""])
                continue
            w.writerow([n, c[4], c[7], c[8], c[9], c[10]])
    print("%d noms, %d dans le catalogue, absents : %s" % (len(noms), len(noms) - len(absents), absents))


if __name__ == "__main__":
    main()
