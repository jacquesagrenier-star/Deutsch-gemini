# -*- coding: utf-8 -*-
"""Les mots allemands A2-C1 encore absents de l'anglais, en cumule.

    python anglais/outils/manques_allemand.py            (le bilan)
    python anglais/outils/manques_allemand.py B1 noms    (la liste d'un niveau)

Un mot allemand du niveau N compte comme present si sa traduction anglaise
(une de ses variantes) est en anglais au niveau N OU PLUS BAS : l'eleve de B1
connait deja ses mots A1 et A2. C'est la mesure de la consigne de Jacques du
27 oct. 2026 (« tous les mots »), complement de couverture.py (niveau par niveau).

Les mots ecartes expres (propres a l'Allemagne, composes sans equivalent
anglais) sont listes et justifies dans anglais/PLAN-A2-C1.md ; ce script les
montre encore, pour qu'aucun ne disparaisse sans trace.
"""
import io, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import couverture as C

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CATS = ("noms", "verbes", "adjectifs", "adverbes", "expressions")


def variantes(niv):
    """Les mots britanniques du niveau (datos-gb) : « pensioner » est couvert
    par « retiree », sa forme americaine."""
    s = set()
    for t in C.lire("anglais/datos-gb/themes.json")["themes"]:
        if t["niveau"] == niv:
            s |= {m["mot"].lower() for m in t["mots"]}
    for f in ("verbes", "adjectifs", "adverbes", "expressions"):
        s |= {e["mot"].lower().strip("!?.") for e in C.lire("anglais/datos-gb/%s.json" % f).get(niv, [])}
    return s


def manques():
    tout, res = set(), {}
    for niv in NIVEAUX:
        _, tous = C.anglais(niv)
        nouveaux = tous | variantes(niv)
        # « to make a decision » (anglais) = « make a decision » (tete allemande).
        tout |= nouveaux | {x[3:] for x in nouveaux if x.startswith("to ")}
        de = C.allemand(niv)
        for cat in CATS:
            res[(niv, cat)] = (len(de[cat]), [e for e in de[cat] if C.tetes(e.get("traduction_en"))
                                              and not any(x in tout for x in C.tetes(e.get("traduction_en")))])
    return res


def francais(e):
    fr = (e.get("traduction") or "").strip()
    art = e.get("article_fr")
    if art and not fr.startswith(("le ", "la ", "les ", "l'")):
        fr = art + fr
    return fr


def main():
    res = manques()
    if len(sys.argv) > 2:
        niv, cat = sys.argv[1].upper(), sys.argv[2]
        for e in res[(niv, cat)][1]:
            print("%s | %s | %s" % (C.tetes(e.get("traduction_en"))[0], francais(e), e.get("mot") or e.get("infinitif")))
        return
    for niv in NIVEAUX[1:]:
        print(niv, " ; ".join("%s %d/%d absents" % (cat, len(res[(niv, cat)][1]), res[(niv, cat)][0]) for cat in CATS))


if __name__ == "__main__":
    main()
