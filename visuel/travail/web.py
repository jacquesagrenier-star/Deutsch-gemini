# -*- coding: utf-8 -*-
"""Les images web du theme « Le travail et l'emploi », a cote de la page (visuel/prototype/travail/) :
    <image>.webp     les etapes de Mark et les papiers, 960 x 720 (4:3)
    travail.json     la donnee de la page (ecrite par travail.py --json, refaite ici : elle sait quelles images existent)
Deux images viennent des demarches, telles quelles (unterschreiben, arbeitsvertrag) : rien a faire ici.
La vignette du ruban de l'accueil est dessinee par python visuel/vignettes_themes.py travail.

    python visuel/travail/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/travail/img/, hors du depot) : les refaire, pas les
corriger. Une image pas encore generee est signalee et sautee : la page tient alors ses questions hors jeu.
"""
import os, sys
from PIL import Image, ImageFilter
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from travail import DOSSIER, IMAGES, ecrire_json   # noqa: E402

SORTIE = os.path.join(ICI, "..", "prototype", "travail")

# Les mots que fal aurait ecrits malgre la consigne, floutes ici plutot que de racheter l'image (boites en pixels de
# l'original 2400 x 1792). bewerbung : « CV » en tete du CV que tient Mark ; gespraech : « Curriculum CV », a l'envers,
# sur la feuille que tient la cheffe (5 nov.). On floute tout le texte, jamais la photo du CV.
# zeitung : des titres d'annonces en faux anglais lisibles (« Food Wooed Salary ») -- toute la page du journal floutee,
# le cercle rouge reste visible ; anschreiben : le bloc d'adresse et la formule d'appel, par prudence.
FLOUS = {"bewerbung": [(1150, 830, 1480, 960), (1150, 960, 1640, 1300)],
         "gespraech": [(1600, 1010, 2010, 1320)],
         "zeitung": [(0, 0, 2400, 1792)],
         "anschreiben": [(540, 330, 1740, 950), (540, 950, 1500, 1180)]}


def flouter(im, boites):
    for b in boites:
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(9)), b[:2])
    return im


def main():
    os.makedirs(SORTIE, exist_ok=True)
    faites, manque = [], []
    for nom, im_ in IMAGES.items():
        if im_.get("src"):
            continue
        src = os.path.join(DOSSIER, nom + ".png")
        if not os.path.exists(src):
            manque.append(nom)
            continue
        im = flouter(Image.open(src).convert("RGB"), FLOUS.get(nom, []))
        w, h = im.size
        if abs(w * 3 - h * 4) > 8:                   # 4:3 exact (fal rend 4:3 a quelques pixels pres)
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=80, method=6)
        faites.append(nom)
    ecrire_json()                                     # apres les webp : travail.json sait lesquelles existent
    print("  %d webp : %s" % (len(faites), ", ".join(faites)))
    if manque:
        print("  pas encore generees (%d) : %s" % (len(manque), ", ".join(manque)))


if __name__ == "__main__":
    main()
