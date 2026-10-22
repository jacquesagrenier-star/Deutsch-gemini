# -*- coding: utf-8 -*-
"""Cherche du TEXTE INCRUSTE par le modele dans une prise (faux sous-titres). Gratuit.

    python video/texte_incruste.py video/episode-es-0*/_essai-avatar/plan*-kling.mp4

POURQUOI (21 oct. 2026). Kling Avatar a incruste sur la poitrine d'Ana (es-01,
plan 13) deux lignes de lettres blanches illisibles, de 2,8 s a la fin de la
prise. Rien dans le prompt ne parlait de texte ; rien dans le retour ne le
signalait. Vu en regardant une bande d'images -- donc on le mesure, a chaque
prise, avant de la retenir.

LA MESURE. Des lettres blanches sous-titrees sont des pixels presque blancs
(> 235) entoures de pixels sombres : un BORD tres contraste. Sur chaque image,
dans les deux tiers bas du cadre, on compte les pixels presque blancs qui ont
un voisin a moins de 120 : un tee-shirt blanc ou un mur clair n'en a presque
pas (pas de bord net), une lettre en a partout. On compare a la PREMIERE image,
qui est l'image de depart, propre par construction.

ETALONNAGE (21 oct.) : es-01 plan 13 avec texte 270 ; propres : es-01 plan 05
(Kling) 2, es-01 plan 19 (H3, rue de nuit) 10, es-02 plan 09 (H3, tee-shirt
blanc et sourire a pleines dents) 29 -- d'ou le seuil a 60, entre les deux.
"""
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
L, H = 240, 427
SEUIL = 60


def images(f):
    b = subprocess.run(["ffmpeg", "-v", "quiet", "-i", f, "-vf",
                        "fps=10,scale=%d:%d,format=gray" % (L, H), "-f", "rawvideo", "-"],
                       capture_output=True, check=True).stdout
    return np.frombuffer(b, dtype=np.uint8).reshape(-1, H, L).astype(np.int16)


def bords_blancs(img):
    bas = img[H // 3:]
    blanc = bas > 235
    sombre = bas < 120
    voisin = np.zeros_like(sombre)
    for dy, dx in ((0, 2), (0, -2), (2, 0), (-2, 0)):
        voisin |= np.roll(np.roll(sombre, dy, 0), dx, 1)
    return int((blanc & voisin).sum())


def main():
    pire = 0
    for f in sys.argv[1:]:
        x = images(f)
        base = bords_blancs(x[0])
        ecarts = [bords_blancs(i) - base for i in x]
        m = max(ecarts)
        t = ecarts.index(m) / 10.0
        verdict = "TEXTE PROBABLE" if m > SEUIL else "propre"
        print("  %-28s  ecart max %4d a %.1f s   %s" % (f.replace("\\", "/").split("/")[-1], m, t, verdict))
        pire = max(pire, m)
    sys.exit(1 if pire > SEUIL else 0)


if __name__ == "__main__":
    main()
