# -*- coding: utf-8 -*-
"""Les images web du theme « Les demarches », a cote de la page (visuel/prototype/demarches/) :
    <image>.webp     les documents et les actions de Mark, 960 x 720 (4:3)
    demarches.json   la donnee de la page (ecrite par demarches.py --json)
La vignette du ruban de l'accueil est dessinee par python visuel/vignettes_themes.py (aucune photo).

    python visuel/demarches/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/demarches/img/, hors du depot) : les refaire, pas les
corriger. Une image pas encore generee est signalee et sautee : la page tient alors ses questions hors jeu.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from demarches import DOSSIER, IMAGES, ecrire_json   # noqa: E402

SORTIE = os.path.join(ICI, "..", "prototype", "demarches")


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    faites, manque = [], []
    for nom in IMAGES:
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        if abs(w * 3 - h * 4) > 8:                   # 4:3 exact (fal rend 4:3 a quelques pixels pres)
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
        faites.append(nom)
    print("  %d webp : %s" % (len(faites), ", ".join(faites)))
    if manque:
        print("  pas encore generees (%d) : %s" % (len(manque), ", ".join(manque)))


if __name__ == "__main__":
    main()
