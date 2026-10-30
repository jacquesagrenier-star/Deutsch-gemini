"""selection.json de la mosaique PORTUGAISE, a partir du choix de Jacques
(page de choix « Tableaux portugais », colle dans la conversation et recopie
dans decisions/DECISIONS.md). « 12 » = num du groupe « libre » de
candidats.json (peintre mort avant 1926) ; « E12 » = num du groupe « europe »
(mort entre 1926 et 1955). L'ordre de la liste est l'ordre d'apparition pour
l'apprenant.

  python portugais/mosaique/selection_depuis_choix.py  ->  selection.json
"""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))

# A remplir avec le choix de Jacques, tel qu'il le colle (« n° 3, 12, E4 ... »).
CHOIX = ""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    candidats = {t["num"]: t for t in json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))}
    numeros = [n.strip().upper() for n in CHOIX.replace("n°", "").split(",") if n.strip()]
    assert numeros, "CHOIX est vide : y coller le choix de Jacques"
    assert len(numeros) == len(set(numeros)), "un numero en double"
    inconnus = [n for n in numeros if n not in candidats]
    assert not inconnus, "numeros absents de candidats.json : %s" % ", ".join(inconnus)
    tableaux = []
    for rang, n in enumerate(numeros, 1):
        t = candidats[n]
        tableaux.append({"rang": rang, "candidat": n, "groupe": t["groupe"], "peintre": t["peintre"],
                         "wikidata_peintre": t["wikidata_peintre"], "mort": t["mort"],
                         "titre": t["titre"], "titre_fr": t["titre_fr"], "annee": t["annee"],
                         "fichier_commons": t["fichier"], "page": t["page"], "original": t["original"],
                         "licence": t["licence"], "collection": t["collection"], "wikidata": t["wikidata"],
                         "l": t["l"], "h": t["h"]})
        print("%2d %-4s %-28s %s" % (rang, n, t["peintre"], t["titre"][:60]))
    assert len({t["wikidata"] for t in tableaux}) == len(tableaux), "un tableau en double"
    json.dump({"_note": "Collection portugaise choisie et ordonnee par Jacques (page de choix ; "
                        "sans prefixe = morts avant 1926, E = morts entre 1926 et 1955). "
                        "rang = ordre d'apparition pour l'apprenant.",
               "choix": CHOIX, "tableaux": tableaux},
              open(os.path.join(ICI, "selection.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(tableaux), "tableaux ;", sum(t["groupe"] == "europe" for t in tableaux), "du groupe europe")


if __name__ == "__main__":
    main()
