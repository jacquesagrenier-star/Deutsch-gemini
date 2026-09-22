# -*- coding: utf-8 -*-
"""Serrer une image deja payee sur un visage, sans en racheter une.

    python video/recadrer.py video/episode-03-auf-dem-radweg/01-images/dame-trottoir.png \\
        --x 300 --y 41 --hauteur 2012

POURQUOI CET OUTIL EXISTE
    Le 22 septembre 2026, dame-trottoir est revenue avec la bonne geographie
    -- trottoir devant, bordure, bande rouge derriere -- mais une tete a
    13,6 % de la hauteur. Les images de cette serie qui partent chez
    OmniHuman tournent autour de 18 a 23 % (dame-feu 17,5 %, mark-moyen-serre
    23 %). Une reprise coute 0,15 $ ET remet en jeu la geographie, qui avait
    justement mis trois prises a venir. Un recadrage ne remet rien en jeu.

CE QU'IL NE SAIT PAS FAIRE
    Inventer des pixels. La fenetre est agrandie a la taille d'origine par
    LANCZOS : on perd du piqué en proportion du zoom. A 1,36x sur une image
    2K, la sortie reste au-dessus du 1080x1920 du montage, donc la perte ne
    se voit pas au final. Au-dela de 1,6x environ, reprendre plutot.

LA FENETRE GARDE LE RAPPORT DE LA SOURCE
    On donne la HAUTEUR voulue et le coin haut-gauche ; la largeur se deduit.
    Le rapport 9:16 de l'episode est ainsi conserve sans calcul a la main.

⚠️ LA PRISE D'ORIGINE N'EST PAS ECRASEE. Elle est rangee en -BRUT, comme
   deux-bandes-BRUT.png : c'est elle qu'on relit le jour ou le recadrage se
   revele trop serre, et elle seule porte ce que le modele a vraiment rendu.
"""
import argparse
import os
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")


def recadrer(chemin, x, y, hauteur):
    im = Image.open(chemin)
    L, H = im.size
    largeur = int(round(hauteur * L / float(H)))
    if x + largeur > L or y + hauteur > H:
        sys.exit("  la fenetre sort de l'image (%dx%d demandes en %d,%d "
                 "dans %dx%d)." % (largeur, hauteur, x, y, L, H))
    brut = "%s-BRUT%s" % os.path.splitext(chemin)
    if not os.path.exists(brut):
        im.save(brut)
        print("  prise d'origine rangee : %s" % os.path.basename(brut))
    vue = im.crop((x, y, x + largeur, y + hauteur)).resize((L, H),
                                                           Image.LANCZOS)
    vue.save(chemin)
    print("  fenetre %dx%d en (%d,%d), agrandie %.2fx -> %s"
          % (largeur, hauteur, x, y, L / float(largeur),
             os.path.basename(chemin)))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("image")
    p.add_argument("--x", type=int, required=True,
                   help="bord gauche de la fenetre, en pixels")
    p.add_argument("--y", type=int, required=True,
                   help="bord haut de la fenetre, en pixels")
    p.add_argument("--hauteur", type=int, required=True,
                   help="hauteur de la fenetre ; la largeur en decoule")
    a = p.parse_args()
    if not os.path.exists(a.image):
        sys.exit("  introuvable : %s" % a.image)
    recadrer(a.image, a.x, a.y, a.hauteur)


if __name__ == "__main__":
    main()
