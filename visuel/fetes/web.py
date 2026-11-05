# -*- coding: utf-8 -*-
"""Les images web du theme « Les fetes et les invitations », a cote de la page (visuel/prototype/fetes/) :
    <image>.webp   les fetes et les moments de Mark, 960 x 720 (4:3)
    fetes.json     la donnee de la page (ecrite par fetes.py --json)

    python visuel/fetes/web.py

Fichiers DERIVES : des originaux (C:/Users/jacqu/.wortando/fetes/img/, hors du depot) et de deux scenes de l'app
reprises telles quelles, recadrees en 4:3 (REPRISES : « Marks Geburtstag », le Weihnachtsmarkt). Les refaire, pas les
corriger. Une image pas encore generee est signalee et sautee : la page tient alors ses questions hors jeu.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from fetes import DOSSIER, IMAGES, REPRISES, ecrire_json   # noqa: E402

SORTIE = os.path.join(ICI, "..", "prototype", "fetes")


def quatre_tiers(im, haut=None):
    """Un 4:3 exact : une image en hauteur (une scene, 9:16) garde toute sa largeur, coupee a partir de « haut »
    (fraction de la hauteur) ; une image a peu pres 4:3 est centree."""
    w, h = im.size
    if abs(w * 3 - h * 4) <= 8:
        return im
    if w * 3 < h * 4:
        ch = round(w * 3 / 4)
        y = round(h * haut) if haut is not None else (h - ch) // 2
        y = max(0, min(y, h - ch))
        return im.crop((0, y, w, y + ch))
    cw = round(h * 4 / 3)
    return im.crop(((w - cw) // 2, 0, (w + cw) // 2, h))


def main():
    os.makedirs(SORTIE, exist_ok=True)
    faites, manque = [], []
    for nom, r in REPRISES.items():
        im = quatre_tiers(Image.open(r["src"]).convert("RGB"), r["haut"])
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
        faites.append(nom)
    for nom in IMAGES:
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = quatre_tiers(Image.open(src).convert("RGB"))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
        faites.append(nom)
    ecrire_json()
    print("  %d webp : %s" % (len(faites), ", ".join(faites)))
    if manque:
        print("  pas encore generees (%d) : %s" % (len(manque), ", ".join(manque)))


if __name__ == "__main__":
    main()
