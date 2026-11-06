"""Verse les lectures en lettres de l'ecoute du telc dans audio/lectures/de.json ({ecrit: dit}), comme
visuel/prototype/dtz/outils/lectures_dtz.py pour le DTZ.

    python visuel/prototype/telc/outils/lectures_ecouter.py

Regle du depot (28 oct. 2026) : les nombres se disent en lettres ; le texte affiche garde ses chiffres, la voix recoit
une lecture ecrite et relue a la main. Les lectures de l'ecoute sont ecrites a cote de chaque replique (champ « dit »
de donnees/hoeren.json et hoeren-schreiben.json) ; ce script les recopie, sans toucher aux autres.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
TABLE = os.path.join(DEPOT, "audio", "lectures", "de.json")


def lignes(o):
    if isinstance(o, dict):
        if "text" in o and o.get("dit"):
            yield o
        for v in o.values():
            yield from lignes(v)
    elif isinstance(o, list):
        for v in o:
            yield from lignes(v)


def main():
    table = json.load(io.open(TABLE, encoding="utf-8"))
    ajoutees = changees = 0
    for nom in ("hoeren.json", "hoeren-schreiben.json"):
        d = json.load(io.open(os.path.join(TELC, "donnees", nom), encoding="utf-8"))
        for l in lignes(d):
            if not re.search(r"\d", l["text"]):
                continue
            if re.search(r"\d", l["dit"]):
                sys.exit("lecture encore chiffree : " + l["dit"][:80])
            if table.get(l["text"]) == l["dit"]:
                continue
            if l["text"] in table:
                changees += 1
            else:
                ajoutees += 1
            table[l["text"]] = l["dit"]
    io.open(TABLE, "w", encoding="utf-8", newline="\n").write(json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    print("audio/lectures/de.json : %d lecture(s) ajoutee(s), %d changee(s)." % (ajoutees, changees))


if __name__ == "__main__":
    main()
