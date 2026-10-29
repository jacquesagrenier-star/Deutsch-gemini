"""selection.json de la mosaique ANGLAISE, a partir du choix de Jacques du
29 oct. 2026 (page a cocher du chef d'orchestre, recopie dans
decisions/DECISIONS.md). « C12 » = num de candidats-couleur.json (deuxieme
recolte, plus coloree) ; « 12 » = num de candidats.json (premiere recolte).
L'ordre de la liste est l'ordre d'apparition pour l'apprenant.

  python anglais/mosaique/selection_depuis_choix.py  ->  selection.json
"""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))

CHOIX = ("C4, C5, C15, C16, C22, C23, C24, C35, C55, C52, C69, C85, C95, C101, C119, C116, "
         "12, 22, 21, 27, 29, 33, 57, 70, 66, 67, 72, 71, 73, 78, 77, 76, 83, 85, 89, 90, 93, 96, "
         "97, 107, 105, 106, 115, 117, 116, 119, 120, C1, C7, C9, C20, C21, C34, C40, C43, C42, "
         "C48, C46, C50, C58, C60, C61, C73, C79, C78, C80, C86")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lire = lambda f: {t["num"]: t for t in json.load(open(os.path.join(ICI, f), encoding="utf-8"))}
    premiere, couleur = lire("candidats.json"), lire("candidats-couleur.json")
    numeros = [n.strip() for n in CHOIX.split(",")]
    assert len(numeros) == len(set(numeros)) == 67, "67 numeros distincts attendus"
    tableaux = []
    for rang, n in enumerate(numeros, 1):
        t = couleur[int(n[1:])] if n.startswith("C") else premiere[int(n)]
        tableaux.append({"rang": rang, "candidat": n, "peintre": t["peintre"], "mort": t["mort"],
                         "titre": t["titre"], "annee": t["annee"], "fichier_commons": t["fichier"],
                         "page": t["page"], "original": t["original"], "licence": t["licence"],
                         "collection": t["collection"], "wikidata": t["wikidata"], "eclat": t["eclat"]})
        print("%2d %-4s %-24s %s" % (rang, n, t["peintre"], t["titre"][:60]))
    assert len({t["wikidata"] for t in tableaux}) == 67, "un tableau en double"
    json.dump({"_note": "Collection anglaise choisie et ordonnee par Jacques le 29 oct. 2026 (page a "
                        "cocher, deux recoltes : C = candidats-couleur.json, sans C = candidats.json). "
                        "rang = ordre d'apparition pour l'apprenant.",
               "choix": CHOIX, "tableaux": tableaux},
              open(os.path.join(ICI, "selection.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
