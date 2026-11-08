# -*- coding: utf-8 -*-
"""Cherche ce qui APPARAIT sur le mur pendant une prise (une tete fantome au bord, un faux caractere). Gratuit.

    python video/apparition_sur_mur.py video/episode-telc-oral/_essai-avatar/plan*-kling.mp4

POURQUOI (8 nov. 2026, oral du telc). Deux defauts que rien d'autre ne voit, et qu'une planche de 8 images ne montre
que par chance : au plan 34, une chevelure sombre a glisse dans le bord gauche, a la fin d'une replique qui se termine
par une question (regle « interlocuteur-fantome ») ; au plan 12, un caractere noir, grand comme une main, a flotte sur
le mur pendant moins de deux secondes. texte_incruste.py ne cherche que du BLANC, sur la poitrine.

intrus_au_bord.py, lui, ne regarde que les bandes du bord, une image par demi-seconde : le faux caractere du plan 12
etait au large du bord, et n'a dure que 0,7 s. Les deux se completent.

LA MESURE. Le mur est fixe. Deux colonnes de chaque cote du personnage, au-dessus des bras et de la table, comparees
image par image a la premiere prise : une case de 30 px qui s'en ecarte de plus de SEUIL, c'est que quelque chose y
est entre. Une main levee peut declencher : la sortie donne les temps, on REGARDE ces images avant de juger.
"""
import argparse
import sys

import cv2
import numpy as np

COLONNE = 150     # px de large de chaque cote, sur une prise de 720 (la tete de Mark, penchee, reste entre les deux)
BAS = 620         # on ne regarde pas plus bas : epaules, bras, table
PAS = 30          # cote des cases
SEUIL = 45.0      # ecart moyen d'une case a la premiere image (0-255)


def intrus(chemin):
    """(liste des temps touches, cote du premier, ecart max)."""
    cap = cv2.VideoCapture(chemin)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    ok, ref = cap.read()
    if not ok:
        raise SystemExit("  illisible : %s" % chemin)
    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY).astype(np.float32)
    h, l = ref.shape
    bas = BAS * h // 1280
    col = COLONNE * l // 720
    n, temps, cote_trouve, maxi = 0, [], None, 0.0
    while True:
        ok, im = cap.read()
        if not ok:
            break
        n += 1
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
        touche = False
        for cote, x0, x1 in (("gauche", 0, col), ("droite", l - col, l)):
            d = np.abs(g[:bas, x0:x1] - ref[:bas, x0:x1])
            for y in range(0, bas - PAS, PAS):
                for x in range(0, x1 - x0 - PAS, PAS):
                    e = float(d[y:y + PAS, x:x + PAS].mean())
                    maxi = max(maxi, e)
                    if e > SEUIL:
                        touche = True
                        cote_trouve = cote_trouve or cote
        if touche:
            temps.append(n / fps)
    cap.release()
    return temps, cote_trouve, maxi


def main():
    p = argparse.ArgumentParser()
    p.add_argument("clips", nargs="+")
    a = p.parse_args()
    touches = 0
    for c in a.clips:
        t, cote, maxi = intrus(c)
        print("  %-24s ecart max %5.1f   %s" % (c.replace("\\", "/").split("/")[-1], maxi,
              "INTRUS a %s : %.2f a %.2f s (%d images)" % (cote, t[0], t[-1], len(t)) if t else "propre"))
        touches += bool(t)
    print("  %d prise(s) sur %d a regarder" % (touches, len(a.clips)))
    sys.exit(0)


if __name__ == "__main__":
    main()
