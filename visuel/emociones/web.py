# -*- coding: utf-8 -*-
"""Les images web du theme « Les emotions et le caractere », a cote de la page (visuel/prototype/emociones/) :
    <Personne>-<emotion>.webp   les 36 portraits, 480 x 480
    trait-<trait>-<qui>.webp    les 36 situations (trois par trait), 960 x 720
    emociones.json              la donnee de la page (ecrite par emociones.py --json)
La vignette du ruban de l'accueil (la planche de photomaton d'Anna) se fait avec les autres, a partir de ces webp :
python visuel/vignettes_themes.py.

    python visuel/emociones/web.py

Fichiers DERIVES des originaux (C:/Users/jacqu/.wortando/emociones/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from emociones import DOSSIER, PORTRAITS, TRAITS, PERS, ecrire_json   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "emociones")


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
    # v1078 : une scene par trait, trait-<trait>.webp ; depuis, trois, trait-<trait>-<personne>.webp
    for f in os.listdir(SORTIE):
        if f.startswith("trait-") and f.count("-") == 1:
            os.remove(os.path.join(SORTIE, f))
    # un prenom reserve (Hugo, Nuria... : visuel/personnes.json) garde l'image de son visage : trait-<trait>-<visage>
    for t, qui in ((t, PERS.visage(p)) for t, scenes in TRAITS.items() for p, *_ in scenes):
        src = os.path.join(DOSSIER, "trait-" + t + "-" + qui + ".png")
        if not os.path.exists(src):
            manque.append("trait-" + t + "-" + qui)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        # 4:3 exact (fal rend 4:3 a quelques pixels pres)
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, "trait-" + t + "-" + qui + ".webp"), "WEBP", quality=78, method=6)
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))
    if manque:
        print("  MANQUENT :", ", ".join(manque))


if __name__ == "__main__":
    main()
