# -*- coding: utf-8 -*-
"""Les images web du theme « Faire les courses », a cote de la page (visuel/prototype/courses/) :
    <magasin>.webp                 les 4 magasins neufs (Metzgerei, Kiosk, Drogerie, Buchhandlung), 9:16, 768 x 1376
    <emballage>-<produit>.webp     les 4 natures mortes du prospectus, 960 x 720
    <moment>.webp                  les 8 moments au comptoir et a la caisse, 960 x 720
    courses.json, gloses.json      la donnee de la page (ecrite aussi par courses.py --json)
Les autres magasins sont les scenes de l'app (baeckerei.webp, supermarkt.webp...), deja en ligne.

    python visuel/courses/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/courses/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from courses import DOSSIER, SORTIE, RACINE, images, ecrire_json, ecrire_gloses   # noqa: E402


def recadrer(im, rw, rh):
    """Recadre au centre au rapport rw:rh exact (fal rend a quelques pixels pres)."""
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
    manque = []
    for nom in images():
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = Image.open(src).convert("RGB")
        if im.size[1] > im.size[0]:
            im = recadrer(im, 9, 16).resize((768, 1376), Image.LANCZOS)
        else:
            im = recadrer(im, 4, 3).resize((960, 720), Image.LANCZOS)
        im.save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=78, method=6)
    # la donnee APRES les images : les drapeaux « pret » suivent les webp presents
    ecrire_json()
    ecrire_gloses()
    fichiers = [f for f in os.listdir(SORTIE) if f.endswith(".webp")]
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in fichiers)
    print("  %d images, %.0f ko dans %s" % (len(fichiers), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
