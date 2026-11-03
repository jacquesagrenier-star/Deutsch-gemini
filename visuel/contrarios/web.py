# -*- coding: utf-8 -*-
"""Les images web du theme « Les contraires », a cote de la page (visuel/prototype/contrarios/) :
    <image>.webp        les 18 images, 960 x 720
    contrarios.json     la donnee de la page (ecrite par contrarios.py --json)
La vignette du ruban de l'accueil (le verre plein et le verre vide) se fait avec les autres, a partir de ces webp :
python visuel/vignettes_themes.py.

    python visuel/contrarios/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/contrarios/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from contrarios import DOSSIER, IMAGES, ecrire_json   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "contrarios")


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
