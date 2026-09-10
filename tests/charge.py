# -*- coding: utf-8 -*-
"""Combien de cartes par jour, vraiment ? Une simulation, pas une intuition.

    python tests/charge.py
    python tests/charge.py --neufs 10 --premier 2

Question de Jacques : « si on fait dix minutes, puis demain, et qu'on pense
toute la serie de vingt, ca veut dire que le lendemain on va juste revoir les
vingt de la veille ». Oui -- PLUS les quinze nouveaux du jour. Mais la vraie
question derriere est : combien ca fait de cartes par jour au bout de deux
mois, et est-ce tenable.

⚠️ CE QUE CETTE SIMULATION SUPPOSE, ET QUI LA REND OPTIMISTE
    Elle suppose que TOUTES les reponses sont bonnes. Un echec renvoie le mot
    au debut de l'echelle et ajoute des revisions : la charge reelle est plus
    lourde que ces chiffres, jamais plus legere. C'est donc un PLANCHER.
"""
import argparse
import sys

sys.stdout.reconfigure(encoding="utf-8")
# L'echelle reelle d'index.html. Le palier de 10 minutes n'apparait pas ici :
# il retombe dans la meme seance, donc il ne cree pas de journee de plus.
APPRENTISSAGE = [1, 3, 7]
ENTRETIEN = [16, 35, 90, 180, 365, 730]


def simuler(jours, neufs_par_jour, corpus, premier):
    echelle = [premier] + APPRENTISSAGE[1:]
    a_faire = {}          # jour -> nombre de cartes dues, par rang
    restant = corpus
    lignes = []
    for j in range(1, jours + 1):
        dus = a_faire.pop(j, [])
        revisions = sum(n for n, _ in dus)
        neufs = min(neufs_par_jour, restant)
        restant -= neufs
        # Chaque carte revue monte d'un rang et se reprogramme.
        for n, rang in dus:
            suivant = rang + 1
            if suivant < len(echelle):
                a_faire.setdefault(j + echelle[suivant], []).append((n, suivant))
            else:
                k = suivant - len(echelle)
                if k < len(ENTRETIEN):
                    a_faire.setdefault(j + ENTRETIEN[k], []).append((n, suivant))
                else:
                    a_faire.setdefault(j + ENTRETIEN[-1], []).append((n, suivant))
        if neufs:
            a_faire.setdefault(j + echelle[0], []).append((neufs, 0))
        lignes.append((j, revisions, neufs, revisions + neufs, corpus - restant))
    return lignes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--neufs", type=int, default=15)
    ap.add_argument("--corpus", type=int, default=797, help="A1 = 797 entrees")
    ap.add_argument("--jours", type=int, default=180)
    ap.add_argument("--premier", type=int, default=1,
                    help="le premier barreau en jours (1 aujourd'hui)")
    a = ap.parse_args()

    lignes = simuler(a.jours, a.neufs, a.corpus, a.premier)
    print("\n  %d mots neufs par jour, corpus de %d, premier barreau a %d jour(s)"
          % (a.neufs, a.corpus, a.premier))
    print("\n  %5s %11s %8s %8s %10s" % ("jour", "revisions", "neufs", "TOTAL",
                                         "vus"))
    print("  " + "-" * 48)
    for j, r, n, t, vus in lignes:
        if j <= 8 or j in (10, 15, 20, 30, 45, 60, 90, 120, 150, 180):
            print("  %5d %11d %8d %8d %10d" % (j, r, n, t, vus))

    fin = next((j for j, r, n, t, vus in lignes if vus >= a.corpus), None)
    pointe = max(lignes, key=lambda x: x[3])
    trente = [x[3] for x in lignes[29:]] or [0]
    print("\n  corpus entierement PRESENTE au jour %s" % (fin or "> %d" % a.jours))
    print("  journee la plus chargee : %d cartes (jour %d)" % (pointe[3], pointe[0]))
    print("  moyenne apres le 30e jour : %d cartes" % (sum(trente) / len(trente)))
    print("\n  ⚠️ Plancher : la simulation suppose toutes les reponses bonnes.")


if __name__ == "__main__":
    main()
