# -*- coding: utf-8 -*-
"""Poser les exercices russes (russe/exercices/corr_*.json) dans exercices.json.

    python russe/outils/poser_exos.py <racine_du_depot> [dossier_des_corrections]

On ne recopie pas la logique de tests/lot_exos.py : on charge CE fichier-la,
celui du depot vise, et on s'en sert tel quel (lire, controle aller-retour a
l'octet, recopier_formes, poser, a_faire). Seule la table CHAMEAU ignore
encore le russe : on lui ajoute "ru" -> "Ru" en memoire, comme le fera le
cablage (cablage_ru.py) dans le fichier lui-meme.

Ordre :
  1. controle aller-retour (exercices.json se reproduit a l'octet pres) ;
  2. recopier_formes : les tuiles qui sont de l'ALLEMAND (correctTr == correct)
     sont recopiees telles quelles en correctRu / optionsRu ;
  3. poser chaque corr_<jeu>.json (sans --remplacer : rien d'existant n'est
     ecrase) ;
  4. bilan : il ne doit plus rester un seul exercice a faire en russe.
Toute anomalie arrete le script avec un code d'erreur.
"""
import glob
import importlib.util
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))


def charger_lot_exos(racine):
    chemin = os.path.join(racine, "tests", "lot_exos.py")
    if not os.path.exists(chemin):
        sys.exit("introuvable : " + chemin)
    spec = importlib.util.spec_from_file_location("lot_exos_cible", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    if os.path.abspath(m.RACINE) != os.path.abspath(racine):
        sys.exit("lot_exos.py vise %s, pas %s" % (m.RACINE, racine))
    m.CHAMEAU.setdefault("ru", "Ru")
    return m


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    racine = os.path.abspath(sys.argv[1])
    dossier = (os.path.abspath(sys.argv[2]) if len(sys.argv) > 2
               else os.path.join(os.path.dirname(ICI), "exercices"))
    m = charger_lot_exos(racine)

    donnees, brut = m.lire()
    ok, detail = m.controle_aller_retour(donnees, brut)
    if not ok:
        sys.exit("ALLER-RETOUR REFUSE, rien n'a ete touche :\n    " + detail)

    m.recopier_formes(donnees, brut, "ru")
    fichiers = sorted(glob.glob(os.path.join(dossier, "corr_*.json")))
    if not fichiers:
        sys.exit("aucun corr_*.json dans " + dossier)
    for f in fichiers:
        # poser() sort lui-meme (sys.exit) sur une question absente ou ambigue.
        m.poser(donnees, brut, "ru", f, False)

    reste = sum(1 for liste in donnees["jeux"].values()
                for e in liste if m.a_faire(e, "ru"))
    total = sum(len(l) for l in donnees["jeux"].values())
    print("  ru : %d jeux poses, %d exercices a faire sur %d" % (len(fichiers), reste, total))
    if reste:
        m.etat(donnees, "ru")
        sys.exit(1)


if __name__ == "__main__":
    main()
