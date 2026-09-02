# -*- coding: utf-8 -*-
"""Ajoute au fichier des ecartes tout ce qui reste au palier 1, classe par cause.

Les 391 mots restants sont du bruit d'extraction : ils n'auraient jamais du
sortir du PDF. Les laisser dans le compteur ferait croire a un travail
inacheve, et le prochain qui regardera le chiffre recommencera le tri.
"""
import io
import os
import sys

RACINE = r"C:\Users\jacqu\OneDrive\Desktop\Mes Projets\DeutschAI"
sys.path.insert(0, os.path.join(RACINE, "tests"))
import tri_inconnus as T                                    # noqa: E402
import paliers_examen as P                                  # noqa: E402
import listes_examen as X                                   # noqa: E402

TITRES = {
    "FLECHI": ("FORMES FLECHIES DE VERBES DEJA AU COURS",
               "Preterits et participes echappes des lignes de conjugaison du\n"
               "PDF. tests/tri_inconnus.py ne les retient que si leur infinitif\n"
               "figure DEJA au cours : on ne devine pas un mot, on constate\n"
               "qu'il en existe deja un."),
    "MORCEAU": ("MORCEAUX DE MOTS",
                "Coupes en fin de colonne par la mise en page : le trait\n"
                "d'union est reste, la moitie du mot est partie."),
    "CRIE":    ("TITRES DE SECTION ET PAGE DE GARDE",
                "Tout en capitales. L'extraction geometrique a pris la page de\n"
                "garde du PDF pour du vocabulaire."),
    "COLLE":   ("MOTS COLLES PAR LA MISE EN PAGE",
                "Deux entrees voisines soudees : « Doppeldiesdiesmal » est\n"
                "« Doppel » + « dies » + « diesmal »."),
    "A VOIR":  ("BRUIT RESTANT, RELU A L'OEIL",
                "Surtout des preterits forts que l'heuristique ne savait pas\n"
                "ramener a leur infinitif -- bekam, fiel, traf, hielt, kam --\n"
                "plus quelques variantes orthographiques de mots deja poses\n"
                "(Abo/Abonnement, nochmal/nochmals, zirka/circa,\n"
                "Erdgeschoss/Erdgeschoss) et « Friede », autre nominatif de\n"
                "« Frieden », deja au cours."),
}


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    tete = P.wikdict()
    verbes = T.infinitifs()
    corpus = X.corpus()

    tas = {k: [] for k in TITRES}
    for mot in P.paliers()[1]:
        if mot.startswith("-") or mot.endswith("-") or len(mot) < 3:
            tas["MORCEAU"].append(mot)
        elif T.CRIE.match(mot):
            tas["CRIE"].append(mot)
        elif T.racines_possibles(mot) & verbes:
            tas["FLECHI"].append(mot)
        elif T.COLLE.search(mot) or (len(mot) > 13 and mot not in corpus):
            tas["COLLE"].append(mot)
        else:
            tas["A VOIR"].append(mot)

    lignes = ["", "# " + "=" * 73,
              "# PALIER 1 -- BRUIT D'EXTRACTION (%d)"
              % sum(len(v) for v in tas.values()),
              "# " + "=" * 73,
              "#",
              "# Ces mots ne sont pas du vocabulaire. Ils sont consignes ici pour que",
              "# le compteur de paliers tombe a zero et dise la verite : il ne reste",
              "# rien a ecrire. Sans cette liste, le prochain qui regarde le chiffre",
              "# recommence le meme tri.",
              "#",
              "# Le classement vient de tests/tri_inconnus.py, relu a l'oeil.", ""]
    for cle in ("FLECHI", "MORCEAU", "CRIE", "COLLE", "A VOIR"):
        if not tas[cle]:
            continue
        titre, note = TITRES[cle]
        lignes.append("")
        lignes.append("## %s (%d)" % (titre, len(tas[cle])))
        lignes.append("#")
        for l in note.split("\n"):
            lignes.append("# " + l)
        lignes.append("")
        lignes.extend(sorted(tas[cle]))

    chemin = os.path.join(RACINE, "ajouts", "noyau-00-ecartes.txt")
    with io.open(chemin, "a", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lignes) + "\n")
    for cle in ("FLECHI", "MORCEAU", "CRIE", "COLLE", "A VOIR"):
        print("  %-8s %4d" % (cle, len(tas[cle])))


if __name__ == "__main__":
    main()
