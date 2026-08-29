# -*- coding: utf-8 -*-
"""Fabrique les ecrans de lancement iOS.

    python marca/hacer-pantallas.py

Quand iOS lance une app web installee sur l'ecran d'accueil, il affiche
l'image de lancement correspondant EXACTEMENT a la taille de l'ecran. S'il
n'en trouve aucune, il affiche sa photo de la session precedente, ce qui
produit un eclair de l'ecran ou l'on en etait.

Ici les images sont un APLAT CREME, sans logo -- et c'est voulu. L'ecran
d'ouverture de l'app est une animation CSS qui part precisement d'un aplat
creme : le mot « Wortando » monte depuis une opacite nulle. L'image de
lancement reproduit donc exactement la premiere image de l'animation, et le
passage de l'ecran systeme a l'app est invisible.

Relancer si la couleur de fond de #apertura change.
"""
import pathlib
from PIL import Image

CREMA = (242, 238, 226)          # #F2EEE2, fond de #apertura
AQUI = pathlib.Path(__file__).resolve().parent
SALIDA = AQUI / "lanzamiento"

# (largeur CSS, hauteur CSS, densite) -- portrait seulement : l'app se tient a
# la verticale, et iOS ignore simplement une taille qu'il ne reconnait pas
# (auquel cas on retombe sur le comportement d'avant, jamais pire).
APARATOS = [
    (320, 568, 2),   # SE 1re gen, 5/5s
    (375, 667, 2),   # 6/7/8, SE 2e et 3e gen
    (414, 736, 3),   # 6+/7+/8+
    (375, 812, 3),   # X, XS, 11 Pro, 12 mini, 13 mini
    (414, 896, 2),   # XR, 11
    (414, 896, 3),   # XS Max, 11 Pro Max
    (390, 844, 3),   # 12, 12 Pro, 13, 13 Pro, 14
    (428, 926, 3),   # 12 Pro Max, 13 Pro Max, 14 Plus
    (393, 852, 3),   # 14 Pro, 15, 15 Pro, 16
    (430, 932, 3),   # 14 Pro Max, 15 Plus, 15 Pro Max, 16 Plus
    (402, 874, 3),   # 16 Pro
    (440, 956, 3),   # 16 Pro Max
]


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for viejo in SALIDA.glob("*.png"):
        viejo.unlink()
    total = 0
    for l, h, d in APARATOS:
        nombre = "lanzamiento-%dx%d@%dx.png" % (l, h, d)
        # Un aplat se code en une poignee d'octets : palette d'une couleur.
        img = Image.new("P", (l * d, h * d), 0)
        img.putpalette(list(CREMA) + [0] * 765)
        img.save(SALIDA / nombre, optimize=True)
        total += (SALIDA / nombre).stat().st_size
    print("%d ecrans de lancement, %.1f Ko au total" % (len(APARATOS), total / 1024))

    # Les balises a coller dans le <head>, pour ne pas les recopier a la main.
    lineas = []
    for l, h, d in APARATOS:
        lineas.append(
            '<link rel="apple-touch-startup-image" href="marca/lanzamiento/lanzamiento-%dx%d@%dx.png"\n'
            '      media="(device-width: %dpx) and (device-height: %dpx) and '
            '(-webkit-device-pixel-ratio: %d) and (orientation: portrait)">' % (l, h, d, l, h, d))
    (AQUI / "lanzamiento" / "_balises.txt").write_text("\n".join(lineas), encoding="utf-8")
    print("balises ecrites dans marca/lanzamiento/_balises.txt")


if __name__ == "__main__":
    main()
