# -*- coding: utf-8 -*-
"""Les images web du theme « Manger et gouter », a cote de la page (visuel/prototype/manger/) :
    gout-<Personne>.webp          les 16 degustations, 480 x 480
    qte-<contenant>-<contenu>.webp  les 10 quantites, 960 x 720
    cafe-<moment>.webp            les 6 moments au cafe, 960 x 720
    manger.json, gloses.json      la donnee de la page (ecrite par manger.py --json)
La vignette du ruban de l'accueil se fait avec les autres, a partir de ces webp : python visuel/vignettes_themes.py.

    python visuel/manger/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/manger/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from manger import DOSSIER, SORTIE, RACINE, images, ecrire_json, ecrire_gloses   # noqa: E402


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    ecrire_gloses()
    manque = []
    for nom, (_, _, fmt, _) in images().items():
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = Image.open(src).convert("RGB")
        if fmt == "1:1":
            im.resize((480, 480), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
            continue
        w, h = im.size
        # 4:3 exact (fal rend 4:3 a quelques pixels pres)
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=78, method=6)
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
