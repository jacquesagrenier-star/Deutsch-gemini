# -*- coding: utf-8 -*-
"""Pour chaque jeu, ce qu'il reste a traduire dans une langue une fois les
tuiles allemandes recopiees (simulation, en memoire). Ecrit un fichier par jeu.

    python exos_dump.py <racine du depot> [langue=pl] [dossier de sortie]

Ecrit pour pt, generalise pour pl : la langue fixe les suffixes (_pl, Pl)."""
import io, json, os, sys

RAC = sys.argv[1]
L = sys.argv[2] if len(sys.argv) > 2 else "pl"
SORTIE = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(__file__))
CH = L[0].upper() + L[1:]
d = json.load(io.open(os.path.join(RAC, "exercices.json"), encoding="utf-8"))
SOUL = ["question", "translation", "hint", "explanation"]
CHAM = ["correct", "options"]
total = {}
for jeu, liste in d["jeux"].items():
    lignes = []
    for i, e in enumerate(liste):
        besoin = {}
        for b in SOUL:
            tr = e.get(b + "_tr")
            if tr and not e.get(b + "_" + L) and tr != e.get(b):
                besoin[b] = e.get(b, "")
        for b in CHAM:
            tr = e.get(b + "Tr")
            if tr and not e.get(b + CH) and tr != e.get(b):
                besoin[b] = {"fr": e.get(b), "en": e.get(b + "En"), "tr": tr}
        if besoin:
            besoin["_q"] = e.get("question", "")
            if sum(1 for x in liste if x.get("question") == e.get("question")) > 1:
                besoin["_cle"] = e.get("translation", "")
            lignes.append(besoin)
    total[jeu] = len(lignes)
    io.open(os.path.join(SORTIE, jeu + ".txt"), "w", encoding="utf-8").write(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in lignes))
for k, v in sorted(total.items(), key=lambda x: x[1]):
    print("%-40s %d" % (k, v))
print("total", sum(total.values()))
