# -*- coding: utf-8 -*-
"""Les images web de « Descripcion fisica », a cote de la page des exercices (visuel/prototype/descripcion/) :
    <Nom>.webp          le personnage detoure (fond transparent), 900 px de haut, pour les rangees a l'echelle
    <Nom>-visage.webp   le visage, recadre dans l'image haute definition (les yeux se lisent)
    yeux-<couleur>.webp la planche des couleurs d'yeux
    personnages.json    les combinaisons et les tailles (copie de visuel/descripcion/personnages.json)

    python visuel/descripcion/web.py

Fichiers DERIVES des originaux (visuel/descripcion/img/, 94 Mo, hors du depot) : les refaire, pas les corriger.
"""
import io, json, os, shutil, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from personnages import PERSONNAGES, EXISTANTS   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "descripcion")
# Le visage dans l'image en pied (1536 x 2752, cadrage commun) : un rectangle autour de la tete.
VISAGE = (0.30, 0.03, 0.70, 0.20)


def source(nom):
    return os.path.join(RACINE, EXISTANTS[nom]) if nom in EXISTANTS else os.path.join(ICI, "img", nom + ".png")


def main():
    os.makedirs(SORTIE, exist_ok=True)
    total = 0
    for nom in PERSONNAGES:
        d = Image.open(os.path.join(ICI, "img", nom + "-detoure.png")).convert("RGBA")
        d = d.crop(d.getbbox())
        d = d.resize((round(d.size[0] * 900 / d.size[1]), 900), Image.LANCZOS)
        d.save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=82, method=6)
        im = Image.open(source(nom)).convert("RGB")
        W, H = im.size
        v = im.crop((int(W * VISAGE[0]), int(H * VISAGE[1]), int(W * VISAGE[2]), int(H * VISAGE[3])))
        v.thumbnail((480, 480), Image.LANCZOS)
        v.save(os.path.join(SORTIE, nom + "-visage.webp"), "WEBP", quality=84, method=6)
    for f in sorted(os.listdir(os.path.join(ICI, "img"))):
        if f.startswith("yeux-") and f.endswith(".png"):
            y = Image.open(os.path.join(ICI, "img", f)).convert("RGB")
            y.thumbnail((900, 900), Image.LANCZOS)
            y.save(os.path.join(SORTIE, f[:-4] + ".webp"), "WEBP", quality=84, method=6)
    shutil.copyfile(os.path.join(ICI, "personnages.json"), os.path.join(SORTIE, "personnages.json"))
    for f in os.listdir(SORTIE):
        total += os.path.getsize(os.path.join(SORTIE, f))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))


if __name__ == "__main__":
    main()
