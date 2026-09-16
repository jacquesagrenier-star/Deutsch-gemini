# -*- coding: utf-8 -*-
"""Deplacer la frontiere entre deux surfaces, en retirant une tranche.

    python video/retrecir_bande.py --dans deux-bandes-v3.png \\
        --sortie deux-bandes.png --couper 780,1040

POURQUOI CET OUTIL EXISTE.

Jacques, 16 septembre 2026 : << refais le plan 12 avec les deux bandes a
parts egales >>. Le plan porte la phrase que l'episode veut qu'on retienne --
Rot fuer Raeder, Grau fuer Menschen -- et une moitie ecrasee rend une des
deux regles secondaire.

DEUX PROMPTS ONT ECHOUE, et l'echec est la lecon :
  1. << split in half down the middle... through the exact centre... each half
     takes the same width >>  ->  67 a 70 % de rouge, mesure sur cinq
     hauteurs. Une proportion abstraite ne se commande pas.
  2. << the photographer is standing astride that painted edge, one foot on
     the red and one foot on the grey >>  ->  le modele a DESSINE UNE BARRE
     NOIRE au milieu de l'image. Pris au mot, litteralement.

Le modele compose, il ne mesure pas. Or ici la mesure est tout le propos.

CE QUE FAIT L'OUTIL, ET POURQUOI C'EST HONNETE. Les deux surfaces existent
deja dans l'image, avec leur vraie matiere et leur vraie lumiere. On retire
simplement une TRANCHE VERTICALE de rouge uni -- prise loin du pictogramme,
dans une zone sans motif -- et on referme. La frontiere se deplace, rien
d'autre ne change : ni la peinture, ni les dalles, ni le velo peint.

⚠️ LA TRANCHE SE PREND DANS DU UNI, JAMAIS EN TRAVERS D'UN MOTIF. Couper a
   travers le pictogramme le mutilerait, et c'est lui qui dit << piste
   cyclable >>. L'outil REFUSE si la zone coupee n'est pas assez uniforme.

⚠️ ET C'EST LE SEUL PLAN DE L'EPISODE OU RECADRER NE SUFFISAIT PAS. Centrer
   la frontiere dans un cadre 9:16 aurait coupe le pictogramme en deux.
"""
import argparse
import os
import sys

from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")


def frontiere(img, ecart=25):
    """Ou passe la limite rouge / gris, ligne par ligne. Mesuree."""
    L, H = img.size
    px = img.load()
    bords = []
    for y in range(0, H, max(1, H // 40)):
        b = None
        for x in range(L - 1, 0, -1):
            if px[x, y][0] - px[x, y][1] > ecart:
                b = x
                break
        if b:
            bords.append(b)
    if not bords:
        sys.exit("  aucune frontiere rouge/gris trouvee")
    return sum(bords) // len(bords), min(bords), max(bords)


def uniforme(img, x0, x1):
    """L'ecart-type de la zone a couper. Un motif le fait exploser."""
    z = img.crop((x0, 0, x1, img.size[1])).convert("L")
    z = z.resize((max(1, (x1 - x0) // 4), img.size[1] // 4))
    d = list(z.get_flattened_data())
    m = sum(d) / float(len(d))
    return (sum((v - m) ** 2 for v in d) / len(d)) ** 0.5


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dans", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--couper", help="x0,x1 de la tranche a retirer ; sans "
                                    "elle, elle est CALCULEE pour du 50/50")
    p.add_argument("--depuis", type=int, default=None,
                   help="bord gauche de la tranche, quand elle est calculee")
    p.add_argument("--ecart-type-max", type=float, default=14.0)
    a = p.parse_args()

    img = Image.open(a.dans).convert("RGB")
    L, H = img.size
    moy, bas, haut = frontiere(img)
    print("  frontiere mesuree : x %d en moyenne (%d..%d), soit %d %% de rouge"
          % (moy, bas, haut, moy * 100 // L))

    if a.couper:
        x0, x1 = [int(v) for v in a.couper.split(",")]
    else:
        # ⚠️ LE FACTEUR DEUX, ET JE L'AVAIS OUBLIE. Retirer r pixels deplace
        #    la frontiere de r ET retrecit l'image de r : le centre recule
        #    donc de r/2, et il faut retirer DEUX FOIS l'ecart pour l'y
        #    amener. Ecrit d'abord << moy - L//2 >>, ce qui laissait 63 % de
        #    rouge en croyant avoir fait 50 %.
        largeur = 2 * (moy - L // 2)
        if largeur <= 0:
            sys.exit("  le rouge occupe deja la moitie ou moins : rien a faire")
        x1 = a.depuis + largeur if a.depuis else moy - 10
        x0 = x1 - largeur
        print("  tranche calculee : %d px a retirer, de x %d a x %d"
              % (largeur, x0, x1))

    e = uniforme(img, x0, x1)
    print("  ecart-type de la tranche : %.1f  (plafond %.1f)"
          % (e, a.ecart_type_max))
    if e > a.ecart_type_max:
        sys.exit("  la tranche n'est pas assez UNIE : il y a un motif dedans.\n"
                 "  La deplacer vers une zone sans dessin -- couper a travers\n"
                 "  le pictogramme le mutilerait, et c'est lui qui dit\n"
                 "  « piste cyclable ».")

    neuf = Image.new("RGB", (L - (x1 - x0), H))
    neuf.paste(img.crop((0, 0, x0, H)), (0, 0))
    neuf.paste(img.crop((x1, 0, L, H)), (x0, 0))

    # La couture : quelques pixels de flou LOCAL, sinon la jonction se voit
    # comme un trait. On ne touche qu'une bande de 12 px.
    zone = (max(0, x0 - 6), 0, min(neuf.size[0], x0 + 6), H)
    neuf.paste(neuf.crop(zone).filter(ImageFilter.GaussianBlur(1.6)), zone[:2])

    # On rend le cadre a sa proportion : 9:16, en rognant le surplus de haut.
    cible = int(round(neuf.size[0] * 16.0 / 9.0))
    if cible < neuf.size[1]:
        y0 = (neuf.size[1] - cible) // 2
        neuf = neuf.crop((0, y0, neuf.size[0], y0 + cible))
    neuf.save(a.sortie)

    m2, _, _ = frontiere(neuf)
    print("  -> %s  (%dx%d, %d %% de rouge)"
          % (a.sortie, neuf.size[0], neuf.size[1],
             m2 * 100 // neuf.size[0]))


if __name__ == "__main__":
    main()
