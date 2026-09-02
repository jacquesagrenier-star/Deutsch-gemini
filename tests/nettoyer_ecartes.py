# -*- coding: utf-8 -*-
"""Retire du fichier des ecartes les mots qui ont fini par recevoir une carte.

    python tests/nettoyer_ecartes.py --verifier
    python tests/nettoyer_ecartes.py

POURQUOI CE SCRIPT EXISTE. Le fichier des ecartes s'est retrouve a se
contredire : 77 mots y etaient listes comme « pas de carte, et voici
pourquoi », alors qu'ils en avaient une. On avait ecarte les mots-outils en
disant qu'une carte « fuer = pour » ne teste rien -- puis on s'est apercu que
cette carte n'existe pas, que celle du cours porte le cas et une phrase, et on
les a marques. Le fichier, lui, est reste sur la decision d'avant.

UNE LISTE DE DECISIONS QUI MENT EST PIRE QUE PAS DE LISTE. Elle sera relue
dans six mois par quelqu'un qui la croira, et qui refera l'arbitrage a
l'envers. On la remet donc d'accord avec les donnees, sans rien perdre : les
lignes retirees vont dans une section datee, avec la raison du retrait.

Le script ne juge rien : il compare le fichier au corpus, et tout mot qui a une
carte sort de la liste des ecartes. C'est la donnee qui tranche.
"""
import io
import os
import sys
from datetime import date

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import listes_examen as X                                   # noqa: E402

CHEMIN = os.path.join(RACINE, "ajouts", "noyau-00-ecartes.txt")


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    verifier = "--verifier" in sys.argv

    corpus = X.corpus()
    lignes = io.open(CHEMIN, encoding="utf-8", newline="").read().split("\n")

    gardees, retirees = [], []
    for l in lignes:
        mot = l.strip()
        if mot and not mot.startswith("#") and mot in corpus:
            retirees.append(mot)
        else:
            gardees.append(l)

    if not retirees:
        print("  le fichier est d'accord avec les donnees, rien a retirer")
        return 0

    print("  %d mot(s) %s de la liste des ecartes :"
          % (len(retirees), "a retirer" if verifier else "retire(s)"))
    print("    " + " ".join(sorted(retirees)))

    if verifier:
        return 0

    # Les lignes retirees ne disparaissent pas : elles migrent dans une section
    # qui dit ce qui s'est passe. Une decision annulee est une information.
    bloc = [
        "",
        "# " + "=" * 73,
        "# REVENUS DANS LE COURS -- decision annulee le %s (%d)" % (date.today(), len(retirees)),
        "# " + "=" * 73,
        "#",
        "# Ces mots avaient ete ecartes au motif qu'une carte « fuer = pour » ne",
        "# teste rien. C'etait faux : cette carte n'existe pas. Celle du cours",
        "# porte le CAS (« toujours Akkusativ ») et une phrase d'exemple, celle",
        "# de « weil » montre le verbe rejete a la fin. Les cartes etaient la",
        "# depuis toujours, dans funktionswort.json ; seule la marque `pruefung`",
        "# manquait, et le compteur de couverture ne lisait meme pas ce fichier.",
        "#",
        "# Ils sont donc COUVERTS, pas ecartes. Cette section garde la trace de",
        "# l'arbitrage annule, pour qu'on ne le refasse pas a l'envers.",
        "",
    ] + sorted(retirees)

    with io.open(CHEMIN, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(gardees).rstrip("\n") + "\n" + "\n".join(bloc) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
