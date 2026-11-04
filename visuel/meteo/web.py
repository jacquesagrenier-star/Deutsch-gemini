# -*- coding: utf-8 -*-
"""Les images web du theme « La meteo et les saisons », a cote de la page (visuel/prototype/meteo/) :
    <image>.webp        les 14 images, 960 x 720
    meteo.json          la donnee de la page (ecrite par meteo.py --json)
La vignette du ruban de l'accueil (la meme place aux quatre saisons) se fait avec les autres, a partir de ces webp :
python visuel/vignettes_themes.py.

    python visuel/meteo/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/meteo/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from meteo import DOSSIER, IMAGES, ecrire_json   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "meteo")


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    manque = []
    for i in IMAGES:
        src = os.path.join(DOSSIER, i + ".png")
        if not os.path.exists(src):
            manque.append(i)
            continue
        im = Image.open(src).convert("RGB")
        if IMAGES[i].get("cadre"):       # le recadrage voulu (meteo.py, cadre)
            x0, y0, x1, y1 = IMAGES[i]["cadre"]
            W, H = im.size
            im = im.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H)))
        w, h = im.size
        # 4:3 exact (fal rend 4:3 a quelques pixels pres)
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, i + ".webp"), "WEBP", quality=78, method=6)
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
