# -*- coding: utf-8 -*-
"""La charge REELLE, une fois la seance plafonnee a 40 cartes.

    python tests/charge_plafond.py

⚠️ POURQUOI CE FICHIER EXISTE A COTE DE charge.py
    charge.py simule la DEMANDE : tout ce qui echoit un jour donne. Il a servi
    a mesurer le mur de l'absence (285 cartes apres une semaine). Mais depuis
    la v523 la seance est plafonnee a 40 cartes : les jours ou la demande
    depasse 40, le surplus attend son tour. Or charge.py annoncait « A1 fini au
    54e jour » en supposant que tout etait traite le jour meme -- c'est
    optimiste, et il fallait le dire plutot que de le laisser croire.

    Ici, on simule ce que l'app SERT vraiment :
      - les echues d'abord, les plus en retard en tete,
      - plafonnees a TAILLE_SEANCE,
      - les mots neufs seulement sur la place qui reste, et au plus
        PLAFOND_NEUFS par jour.

    Le reste attend, exactement comme dans cartesDeSession().
"""
import argparse
import sys

sys.stdout.reconfigure(encoding="utf-8")
APPRENTISSAGE = [1, 3, 7]
ENTRETIEN = [16, 35, 90, 180, 365, 730]
TAILLE_SEANCE = 40
PLAFOND_NEUFS = 15


def simuler(jours, neufs_jour, corpus, taille=TAILLE_SEANCE, premier=1):
    ech = [premier] + APPRENTISSAGE[1:]
    file = []            # [echeance, rang] -- une entree par carte
    restant, lignes = corpus, []
    for j in range(1, jours + 1):
        # Les echues, les plus en retard d'abord (echeance la plus ancienne).
        dues = sorted([c for c in file if c[0] <= j], key=lambda c: c[0])
        servies = dues[:taille]
        for c in servies:
            file.remove(c)
            r = c[1] + 1
            d = ech[r] if r < len(ech) else ENTRETIEN[min(r - len(ech),
                                                          len(ENTRETIEN) - 1)]
            file.append([j + d, r])
        place = min(taille - len(servies), neufs_jour, restant)
        place = max(0, place)
        restant -= place
        for _ in range(place):
            file.append([j + ech[0], 0])
        lignes.append((j, len(servies), place, len(servies) + place,
                       corpus - restant, len(dues) - len(servies)))
    return lignes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=int, default=797)
    ap.add_argument("--jours", type=int, default=400)
    a = ap.parse_args()

    print("\n  SEANCE PLAFONNEE A %d CARTES -- corpus de %d\n"
          % (TAILLE_SEANCE, a.corpus))
    print("  %-22s %8s %9s %10s %10s"
          % ("", "jour 2", "corpus vu", "attente max", "jours pleins"))
    print("  " + "-" * 64)
    for n in (10, 15, 20, 25):
        l = simuler(a.jours, n, a.corpus)
        fin = next((x[0] for x in l if x[4] >= a.corpus), None)
        attente = max(x[5] for x in l)
        pleins = sum(1 for x in l if x[3] >= TAILLE_SEANCE)
        print("  %-22s %8d %9s %10d %10d"
              % ("%d mots neufs/jour" % n, l[1][3],
                 str(fin) if fin else "> %d" % a.jours, attente, pleins))

    print("\n  ET SI LA SEANCE ETAIT PLUS GRANDE (15 mots neufs/jour)\n")
    print("  %-22s %8s %9s %10s %10s"
          % ("", "jour 2", "corpus vu", "attente max", "jours pleins"))
    print("  " + "-" * 64)
    for t in (30, 40, 60, 80):
        l = simuler(a.jours, 15, a.corpus, taille=t)
        fin = next((x[0] for x in l if x[4] >= a.corpus), None)
        attente = max(x[5] for x in l)
        pleins = sum(1 for x in l if x[3] >= t)
        print("  %-22s %8d %9s %10d %10d"
              % ("seance de %d cartes" % t, l[1][3],
                 str(fin) if fin else "> %d" % a.jours, attente, pleins))

    print("\n  « attente max » = le plus grand nombre de cartes ayant du attendre")
    print("  un jour de plus. « jours pleins » = journees ou la seance est pleine.")
    print("  ⚠️ Plancher : toutes les reponses supposees bonnes.\n")


if __name__ == "__main__":
    main()
