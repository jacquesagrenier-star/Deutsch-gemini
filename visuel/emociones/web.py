# -*- coding: utf-8 -*-
"""Les images web du theme « Les emotions et le caractere », a cote de la page (visuel/prototype/emociones/) :
    <Personne>-<emotion>.webp   les 36 portraits, 480 x 480
    trait-<trait>.webp          les 12 situations, 960 x 720
    emociones.json              la donnee de la page (ecrite par emociones.py --json)
et la vignette du ruban de l'accueil, visuel/prototype/themes/emociones.webp (450 x 600, comme l'arbre et la
toise) : une PLANCHE DE PHOTOMATON, Anna quatre fois -- contente, surprise, fachee, triste. Une seule personne et
quatre visages : elle dit le sujet autrement qu'une rangee de personnes (regle de Jacques, 3 nov. 2026).

    python visuel/emociones/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/emociones/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image, ImageDraw
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from emociones import DOSSIER, PORTRAITS, TRAITS, ecrire_json   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "emociones")
VIGNETTE = os.path.join(RACINE, "visuel", "prototype", "themes", "emociones.webp")
PHOTOMATON = ["contento", "sorprendido", "enfadado", "triste"]


def photomaton():
    """Quatre photos d'identite sur leur bande blanche, deux par deux, separees d'un liseré gris clair."""
    W, H, M = 450, 600, 13
    pw, ph = (W - 3 * M) // 2, (H - 3 * M) // 2
    P = Image.new("RGB", (W, H), (250, 249, 246))
    d = ImageDraw.Draw(P)
    for k, e in enumerate(PHOTOMATON):
        im = Image.open(os.path.join(DOSSIER, "Anna-" + e + ".png")).convert("RGB")
        w, h = im.size
        # serre sur la tete et les epaules : le ruban montre la vignette a 66 px de large, le pull n'y dit rien
        ch = round(h * 0.62)
        cw = round(ch * pw / ph)
        y0 = round(h * 0.03)
        im = im.crop(((w - cw) // 2, y0, (w + cw) // 2, y0 + ch)).resize((pw, ph), Image.LANCZOS)
        x, y = M + (k % 2) * (pw + M), M + (k // 2) * (ph + M)
        P.paste(im, (x, y))
        d.rectangle((x - 1, y - 1, x + pw, y + ph), outline=(214, 210, 202))
    os.makedirs(os.path.dirname(VIGNETTE), exist_ok=True)
    P.save(VIGNETTE, "WEBP", quality=84, method=6)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecrire_json()
    manque = []
    for p, emos in PORTRAITS.items():
        for e in emos:
            src = os.path.join(DOSSIER, p + "-" + e + ".png")
            if not os.path.exists(src):
                manque.append(p + "-" + e)
                continue
            im = Image.open(src).convert("RGB").resize((480, 480), Image.LANCZOS)
            im.save(os.path.join(SORTIE, p + "-" + e + ".webp"), "WEBP", quality=80, method=6)
    for t in TRAITS:
        src = os.path.join(DOSSIER, "trait-" + t + ".png")
        if not os.path.exists(src):
            manque.append("trait-" + t)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        # 4:3 exact (fal rend 4:3 a quelques pixels pres)
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, "trait-" + t + ".webp"), "WEBP", quality=78, method=6)
    photomaton()
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
