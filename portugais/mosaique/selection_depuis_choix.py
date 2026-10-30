"""selection.json de la mosaique PORTUGAISE, a partir du choix de Jacques
(page de choix « Tableaux portugais », colle dans la conversation et recopie
dans decisions/DECISIONS.md). « 12 » = num du groupe « libre » de
candidats.json (peintre mort avant 1926) ; « E12 » = num du groupe « europe »
(mort entre 1926 et 1955). Depuis le 30 oct. (variante bresilienne), « B12 » et
« BE12 » sont les memes groupes pour les peintres du BRESIL (candidats-bresil.json). L'ordre de la liste est l'ordre d'apparition pour
l'apprenant.

  python portugais/mosaique/selection_depuis_choix.py  ->  selection.json
"""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))

# A remplir avec le choix de Jacques, tel qu'il le colle (« n° 3, 12, E4 ... »).
CHOIX = "n° 1, 2, 5, 6, 7, 9, 10, 12, 15, 17, 21, 22, 30, 31, 35, 36, 37, 40, 41, 50, 47, 52, 53, 57, 59, 60, 62, 66, 69, 74, E3, E4, E5, E6, E7, E8, E11, E13, E14, E15, E16, E20, E22, E23, E25, E27, E28, E31, E32, E33, E36, E37, E41, E43, E48, E46, E47, E50, E49, E53, E57, E65, E68, E72, E77, E79"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    candidats = {}
    for f, pays in (("candidats.json", "Portugal"), ("candidats-bresil.json", "Brésil")):
        for t in json.load(open(os.path.join(ICI, f), encoding="utf-8")):
            candidats[t["num"]] = dict(t, pays=pays)
    numeros = [n.strip().upper() for n in CHOIX.replace("n°", "").split(",") if n.strip()]
    assert numeros, "CHOIX est vide : y coller le choix de Jacques"
    assert len(numeros) == len(set(numeros)), "un numero en double"
    inconnus = [n for n in numeros if n not in candidats]
    assert not inconnus, "numeros absents des candidats : %s" % ", ".join(inconnus)
    tableaux = []
    for rang, n in enumerate(numeros, 1):
        t = candidats[n]
        tableaux.append({"rang": rang, "candidat": n, "pays": t["pays"], "groupe": t["groupe"], "peintre": t["peintre"],
                         "wikidata_peintre": t["wikidata_peintre"], "mort": t["mort"],
                         "titre": t["titre"], "titre_fr": t["titre_fr"], "annee": t["annee"],
                         "fichier_commons": t["fichier"], "page": t["page"], "original": t["original"],
                         "licence": t["licence"], "collection": t["collection"], "wikidata": t["wikidata"],
                         "l": t["l"], "h": t["h"]})
        print("%2d %-5s %-28s %s" % (rang, n, t["peintre"], t["titre"][:60]))
    assert len({t["wikidata"] for t in tableaux}) == len(tableaux), "un tableau en double"
    json.dump({"_note": "Collection portugaise choisie et ordonnee par Jacques (page de choix ; "
                        "Portugal : sans prefixe = morts avant 1926, E = morts entre 1926 et 1955 ; "
                        "Bresil : B et BE, memes regles). "
                        "rang = ordre d'apparition pour l'apprenant.",
               "choix": CHOIX, "tableaux": tableaux},
              open(os.path.join(ICI, "selection.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(tableaux), "tableaux ;", sum(t["pays"] == "Brésil" for t in tableaux), "du Bresil ;",
          sum(t["groupe"] == "europe" for t in tableaux), "a decider (morts entre 1926 et 1955)")


if __name__ == "__main__":
    main()
