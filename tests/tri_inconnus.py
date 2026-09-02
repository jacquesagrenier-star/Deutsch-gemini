# -*- coding: utf-8 -*-
"""Propose un tri des mots que WikDict ne reconnait pas, pour relecture humaine.

    python tests/tri_inconnus.py

CE SCRIPT NE DECIDE RIEN, IL RANGE. Chaque tas est ensuite relu a l'oeil, et
c'est volontaire : la seule fois ou une heuristique a decide seule du sort de
ces mots, elle a retire 671 entrees du DTZ dont « erste » et « dritte ». Le
commentaire de listes_examen.py raconte l'histoire.

CE QU'IL SAIT RECONNAITRE, et pourquoi c'est sur :

  FLECHI    la forme se ramene a un infinitif QUE LE COURS ENSEIGNE DEJA.
            « bedeutete » -> bedeuten, « geflossen » -> fliessen. On ne
            devine pas un mot : on constate qu'il en existe deja un.
  MORCEAU   commence ou finit par un trait d'union, ou fait moins de trois
            lettres. Le PDF coupe ses mots en fin de colonne.
  CRIE      tout en capitales : ce sont les titres de section et la page de
            garde du PDF -- IMPRESSUM, PROJEKTTEAM, WORTGRUPPEN.
  COLLE     deux majuscules a l'interieur du mot, ou une longueur absurde
            sans qu'aucun morceau ne soit connu : « Doppeldiesdiesmal »,
            « Lieblingsmeinen ». Deux entrees voisines soudees par la mise
            en page.
  A VOIR    tout le reste. C'est le seul tas qui compte, et il se lit.
"""
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import listes_examen as X                                   # noqa: E402
import paliers_examen as P                                  # noqa: E402


def infinitifs():
    """Les verbes que le cours enseigne, sous toutes leurs formes utiles."""
    import json
    out = set()
    d = json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8"))
    for niveau in ("A1", "A2", "B1", "B2", "C1"):
        for v in d.get(niveau, []):
            inf = (v.get("infinitif") or "").replace("sich ", "").strip()
            if inf:
                out.add(inf)
    return out


def racines_possibles(mot):
    """Les infinitifs dont ce mot POURRAIT etre une forme flechie.

    On ne rend que des candidats. C'est la presence au cours qui tranche --
    une racine inventee qui ne correspond a aucun verbe est ignoree.
    """
    out = set()
    b = mot
    if b.startswith("ge") and (b.endswith("t") or b.endswith("en")):
        n = b[2:]
        out |= {n.rstrip("t") + "en", n[:-2] + "en" if n.endswith("en") else n + "en"}
    for suf, rem in (("te", 2), ("ete", 3), ("t", 1), ("st", 2), ("en", 2)):
        if b.endswith(suf) and len(b) > rem + 2:
            out.add(b[:-rem] + "en")
    out.add(b + "en")
    # Voyelle du preterit fort : « floss » -> fliessen, « fand » -> finden.
    for a, z in (("a", "i"), ("o", "ie"), ("i", "ei"), ("u", "ie"), ("a", "e")):
        if a in b:
            out.add(b.replace(a, z, 1) + "en")
    return {r for r in out if len(r) > 3}


CRIE = re.compile(r"^[A-ZÄÖÜ][A-ZÄÖÜ\-]+$")
COLLE = re.compile(r"[a-zäöüß][A-ZÄÖÜ]")


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    tete = P.wikdict()
    verbes = infinitifs()
    corpus = X.corpus()

    tas = {"FLECHI": [], "MORCEAU": [], "CRIE": [], "COLLE": [], "A VOIR": []}
    for mot in P.paliers()[1]:
        if tete.get(mot):
            continue                     # deja classe par le fichier de palier
        if mot.startswith("-") or mot.endswith("-") or len(mot) < 3:
            tas["MORCEAU"].append(mot)
        elif CRIE.match(mot):
            tas["CRIE"].append(mot)
        elif racines_possibles(mot) & verbes:
            tas["FLECHI"].append(mot)
        elif COLLE.search(mot) or (len(mot) > 13 and mot not in corpus):
            tas["COLLE"].append(mot)
        else:
            tas["A VOIR"].append(mot)

    for nom in ("MORCEAU", "CRIE", "FLECHI", "COLLE", "A VOIR"):
        print("\n## %s (%d)" % (nom, len(tas[nom])))
        print("   " + " ".join(tas[nom]))
    print()
    print("  %d mots, dont %d a relire" % (sum(len(v) for v in tas.values()),
                                           len(tas["A VOIR"])))


if __name__ == "__main__":
    main()
