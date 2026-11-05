# -*- coding: utf-8 -*-
"""Les images web du theme « L'ecole et la garderie », a cote de la page (visuel/prototype/ecole/) :
    <image>.webp     les actions, 960 x 720 (4:3)
    <objet>.webp     les fournitures, decoupees dans la photo « material » (DECOUPES d'ecole.py), 4:3
    ecole.json       la donnee de la page (ecrite par ecole.py --json)

    python visuel/ecole/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/ecole/img/, hors du depot) : les refaire, pas les corriger.
Une image pas encore generee est signalee et sautee.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from ecole import DOSSIER, IMAGES, DECOUPES, ecrire_json   # noqa: E402

SORTIE = os.path.join(ICI, "..", "prototype", "ecole")


# Les mots que fal a ecrits malgre la consigne, floutes ici plutot que de racheter l'image (boites en pixels de
# l'original 2400 x 1792), 5 nov. : « Registration Form » sur le formulaire d'inscription, « Tempera » sur les pots de
# peinture et un mot sur une feuille du mur de la Kita.
FLOUS = {"anmelden": [(800, 1365, 1245, 1528)], "malen": [(1200, 1215, 1525, 1320), (425, 115, 510, 190)]}


def flouter(im, boites):
    from PIL import ImageFilter
    for b in boites:
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(9)), b[:2])
    return im


def quatre_tiers(im):
    w, h = im.size
    if abs(w * 3 - h * 4) > 8:
        ch = round(w * 3 / 4) if w * 3 < h * 4 else h
        cw = round(ch * 4 / 3)
        im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
    return im


def complet(im):
    """Complete en 4:3 sans rien couper : le bureau autour de l'objet, prolonge par sa couleur (mediane des bords)."""
    w, h = im.size
    W, H = (w, round(w * 3 / 4)) if w * 3 >= h * 4 else (round(h * 4 / 3), h)
    W, H = round(max(W, w) * 1.08), round(max(H, h) * 1.08)
    bords = [im.getpixel((x, y)) for x in range(0, w, 4) for y in (0, h - 1)] + [im.getpixel((x, y)) for y in range(0, h, 4) for x in (0, w - 1)]
    fond = tuple(sorted(c[i] for c in bords)[len(bords) // 2] for i in range(3))
    toile = Image.new("RGB", (W, H), fond)
    # un fondu sur les bords du decoupage, pour que la jointure avec le fond ne se voie pas
    from PIL import ImageDraw, ImageFilter
    r = max(6, min(w, h) // 32)
    masque = Image.new("L", (w, h), 0)
    ImageDraw.Draw(masque).rectangle((r, r, w - 1 - r, h - 1 - r), fill=255)
    toile.paste(im, ((W - w) // 2, (H - h) // 2), masque.filter(ImageFilter.GaussianBlur(r / 2)))
    return toile


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    faites, manque = [], []
    for nom, im in IMAGES.items():
        if im.get("existe"):
            continue
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        image = flouter(Image.open(src).convert("RGB"), FLOUS.get(nom, []))
        if nom == "material":
            # les fournitures : une boite 4:3 par objet, en fractions de l'image (relevees a l'oeil)
            w, h = image.size
            for obj, (x0, y0, x1, y1) in DECOUPES.items():
                complet(image.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)))).resize((640, 480), Image.LANCZOS).save(
                    os.path.join(SORTIE, obj + ".webp"), "WEBP", quality=82, method=6)
                faites.append(obj)
            continue
        quatre_tiers(image).resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
        faites.append(nom)
    print("  %d webp : %s" % (len(faites), ", ".join(faites)))
    if manque:
        print("  pas encore generees (%d) : %s" % (len(manque), ", ".join(manque)))


if __name__ == "__main__":
    main()
