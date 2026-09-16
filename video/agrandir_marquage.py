# -*- coding: utf-8 -*-
"""Agrandir un marquage peint au sol, sans repasser par fal.

    python video/agrandir_marquage.py --dans a.png --sortie b.png \\
        --zone 30,1170,500,1550 --fond 60,120 --facteur 2.5 --vers 255,1300

POURQUOI.

Jacques, 16 septembre 2026, sur le plan 12 : << ce qui n'est pas realiste,
c'est la grandeur du velo qu'on voit sur la piste. Il faudrait voir seulement
la roue arriere, peut-etre, en plus gros. C'est jamais comme ca sur une
piste, un petit velo comme on voit sur le tapis rouge. >>

Il a raison, et c'est mesurable : le velo peint fait 460 px de large pour une
bande de 512, soit 90 % -- mais il est ENTIER dans le cadre, et un marquage
entier vu d'en haut lit comme un autocollant. Un vrai marquage de Radweg est
grand, et quand on baisse les yeux sur ses pieds on n'en voit qu'un morceau.

C'EST LE MEME GESTE QUE L'AMPELMAENNCHEN. Un marquage peint est un graphique :
il se deplace, il s'agrandit, il se laisse couper par le bord du cadre. Rien
a racheter. La peinture est celle de l'image -- sa matiere, son usure, ses
ecaillures -- simplement plus grande.

⚠️ ON RELEVE LE FOND LIGNE PAR LIGNE, JAMAIS UNE COULEUR UNIQUE. L'asphalte
   peint n'a pas une valeur : il palit, il s'use, il porte des traces. Une
   couleur moyenne posee en aplat fait un rectangle qu'on voit tout de suite
   -- c'est la lecon de l'effacement du panneau sur mark-marche.

⚠️ ET CE QUI SORT DU CADRE EST COUPE, PAS COMPRIME. C'est tout l'effet
   recherche : le marquage continue au-dela du bord, comme dans la rue.
"""
import argparse
import sys

from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")


def masque_peinture(img, zone, clair=150, ecart=58):
    """Le masque de la peinture dans la zone : clair, et peu colore.

    Le seuil ne se devine pas -- il se lit sur l'image. La peinture blanche
    usee tourne autour de (200,195,190), l'asphalte rouge autour de
    (160,110,110) : c'est l'ECART entre le bleu et le rouge qui separe les
    deux proprement, bien mieux que la luminosite seule."""
    x0, y0, x1, y1 = zone
    m = Image.new("L", (x1 - x0, y1 - y0), 0)
    px = img.load()
    mp = m.load()
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            r, v, b = px[x, y]
            if b > clair and r - b < ecart:
                mp[x - x0, y - y0] = 255
                n += 1
    return m, n


def effacer(img, zone, source, flou=1.6):
    """Efface la zone en TRANSPLANTANT un bloc de sol nu.

    ⚠️ PAS PAR MEDIANE DE COLONNE. Cette methode-la -- celle qui a efface le
       panneau de mark-marche -- suppose qu'il existe, A LA MEME HAUTEUR, une
       colonne de sol propre. Ca valait dans du ciel. Ca ne vaut pas ici : le
       velo peint traverse toute la largeur de la bande rouge, et il n'y a
       aucune colonne propre a sa hauteur. Une mediane prise sur les 10 px
       restants poserait un aplat.

    `source` est le coin haut-gauche d'un bloc de MEME TAILLE pris ailleurs
    sur la meme bande. Ce n'est pas une couleur inventee : c'est le meme
    revetement, la meme lumiere, la meme usure -- un autre metre de piste."""
    x0, y0, x1, y1 = zone
    sx, sy = source
    img.paste(img.crop((sx, sy, sx + (x1 - x0), sy + (y1 - y0))), (x0, y0))
    for bord in ((x0 - 6, y0 - 6, x1 + 6, y0 + 6),
                 (x0 - 6, y1 - 6, x1 + 6, y1 + 6),
                 (x0 - 6, y0 - 6, x0 + 6, y1 + 6),
                 (x1 - 6, y0 - 6, x1 + 6, y1 + 6)):
        b = (max(0, bord[0]), max(0, bord[1]),
             min(img.size[0], bord[2]), min(img.size[1], bord[3]))
        if b[2] > b[0] and b[3] > b[1]:
            img.paste(img.crop(b).filter(ImageFilter.GaussianBlur(flou)),
                      b[:2])
    return img


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dans", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--zone", required=True, help="x0,y0,x1,y1 du marquage")
    p.add_argument("--fond", required=True,
                   help="x,y du coin d'un BLOC de sol nu, meme taille que la "
                        "zone, pris ailleurs sur la meme surface")
    p.add_argument("--facteur", type=float, default=2.5)
    p.add_argument("--tourner", type=float, default=0.0,
                   help="degres, pour aligner le marquage sur la voie")
    p.add_argument("--vers", required=True,
                   help="x,y ou poser le CENTRE du marquage agrandi")
    p.add_argument("--clair", type=int, default=150)
    p.add_argument("--ecart", type=int, default=58)
    a = p.parse_args()

    img = Image.open(a.dans).convert("RGB")
    zone = [int(v) for v in a.zone.split(",")]
    source = tuple(int(v) for v in a.fond.split(","))
    cx, cy = [int(v) for v in a.vers.split(",")]

    m, n = masque_peinture(img, zone, a.clair, a.ecart)
    aire = (zone[2] - zone[0]) * (zone[3] - zone[1])
    print("  peinture reperee : %d px sur %d (%d %% de la zone)"
          % (n, aire, n * 100 // max(1, aire)))
    if n < aire // 40:
        sys.exit("  trop peu de peinture trouvee : le seuil ne convient pas.\n"
                 "  Regarder l'image et ajuster --clair / --ecart.")

    peinture = img.crop(tuple(zone))
    if a.tourner:
        peinture = peinture.rotate(a.tourner, expand=True,
                                   resample=Image.BICUBIC)
        m = m.rotate(a.tourner, expand=True, resample=Image.BICUBIC)

    effacer(img, zone, source)

    L = int(peinture.size[0] * a.facteur)
    H = int(peinture.size[1] * a.facteur)
    peinture = peinture.resize((L, H), Image.LANCZOS)
    m = m.resize((L, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    print("  marquage : %dx%d  ->  %dx%d  (x%.2f)"
          % (zone[2] - zone[0], zone[3] - zone[1], L, H, a.facteur))

    # Ce qui deborde du cadre est COUPE -- c'est l'effet cherche.
    img.paste(peinture, (cx - L // 2, cy - H // 2), m)
    img.save(a.sortie)
    print("  -> %s" % a.sortie)


if __name__ == "__main__":
    main()
