# -*- coding: utf-8 -*-
"""Les images web du theme « Le corps et la sante », a cote de la page (visuel/prototype/cuerpo/) :
    dolor-<endroit>-<qui>.webp    les 36 « j'ai mal », 600 x 800 (3:4)
    sintoma-<mal>-<qui>.webp      les 12 maux, 600 x 800
    medico-<qui>.webp             les deux medecins, 960 x 720 (4:3)
    cuerpo.json, gloses.json      la donnee de la page (ecrite par cuerpo.py --json)
La vignette du ruban de l'accueil (la carte du corps) : python visuel/vignettes_themes.py.

    python visuel/cuerpo/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/cuerpo/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from cuerpo import DOSSIER, images, ecrire_json, ecrire_gloses   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "cuerpo")


def recadrer(im, rw, rh):
    """Au rapport exact (fal rend 3:4 ou 4:3 a quelques pixels pres)."""
    w, h = im.size
    if abs(w * rh - h * rw) <= 8:
        return im
    if w * rh > h * rw:
        cw = round(h * rw / rh)
        return im.crop(((w - cw) // 2, 0, (w + cw) // 2, h))
    ch = round(w * rh / rw)
    return im.crop((0, (h - ch) // 2, w, (h + ch) // 2))


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    ecrire_gloses()
    manque = []
    for nom, (_, _, fmt) in images().items():
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = Image.open(src).convert("RGB")
        taille = (960, 720) if fmt == "4:3" else (600, 800)
        im = recadrer(im, *taille).resize(taille, Image.LANCZOS)
        im.save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=78, method=6)
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
