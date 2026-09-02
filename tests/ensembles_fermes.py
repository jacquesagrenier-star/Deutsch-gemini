# -*- coding: utf-8 -*-
"""Les ensembles fermes du cours sont-ils complets ?

Le calendrier ne l'etait pas : quatre mois sur douze, deux jours sur sept, et
personne ne l'avait vu parce qu'un trou PARTIEL se cache derriere ce qui est
la. Celui qui a revise « Januar » croit connaitre les mois.

On verifie donc les autres ensembles a bord ferme -- ceux dont on peut ecrire
la liste complete de memoire.
"""
import io
import os
import sys

RACINE = r"C:\Users\jacqu\OneDrive\Desktop\Mes Projets\DeutschAI"
sys.path.insert(0, os.path.join(RACINE, "tests"))
import listes_examen as X                                   # noqa: E402

ENSEMBLES = {
    "mois": "Januar Februar M\u00e4rz April Mai Juni Juli August September "
            "Oktober November Dezember",
    "jours": "Montag Dienstag Mittwoch Donnerstag Freitag Samstag Sonntag",
    "saisons": "Fr\u00fchling Sommer Herbst Winter",
    "couleurs": "rot blau gelb gr\u00fcn schwarz wei\u00df grau braun rosa orange "
                "lila bunt hell dunkel",
    "corps": "Kopf Haar Auge Ohr Nase Mund Zahn Hals Schulter Arm Hand Finger "
             "Bauch R\u00fccken Bein Knie Fu\u00df Herz Haut Blut",
    "famille": "Vater Mutter Sohn Tochter Bruder Schwester Gro\u00dfvater "
               "Gro\u00dfmutter Onkel Tante Cousin Cousine Neffe Nichte Enkel "
               "Ehemann Ehefrau Kind Eltern Geschwister",
    "reperes": "Norden S\u00fcden Osten Westen links rechts oben unten vorne hinten",
    "repas": "Fr\u00fchst\u00fcck Mittagessen Abendessen Vorspeise Nachtisch",
    "meteo": "Sonne Regen Schnee Wind Wolke Nebel Gewitter Sturm Eis Hitze K\u00e4lte",
    # Trouves incomplets au palier 1, apres le calendrier. Les jours en -s
    # n'avaient que \u00ab montags \u00bb ; les ordinaux d'enumeration manquaient
    # \u00ab erstens \u00bb, qu'AUCUNE des trois listes ne reclame -- le controle de
    # couverture ne pouvait donc pas le signaler. Un ensemble ferme se verifie
    # sur lui-meme, pas contre une liste exterieure.
    "jours -s": "montags dienstags mittwochs donnerstags freitags samstags sonntags",
    "ordinaux": "erstens zweitens drittens viertens",
    "multiples": "einmal zweimal dreimal viermal f\u00fcnfmal",
}


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    corpus = X.corpus()
    for nom, liste in ENSEMBLES.items():
        mots = liste.split()
        manque = [m for m in mots if m not in corpus]
        etat = "complet" if not manque else "MANQUE %d" % len(manque)
        print("  %-10s %2d/%-2d  %-10s %s"
              % (nom, len(mots) - len(manque), len(mots), etat, " ".join(manque)))


if __name__ == "__main__":
    main()
