# -*- coding: utf-8 -*-
"""Le gros plan des yeux de chaque personnage de « Descripcion fisica » (3 nov. 2026) :
    <Nom>-yeux.webp   une bande autour des deux yeux, 720 x 300, prise dans l'image haute definition

Jacques : « c'est un peu loin pour voir la couleur des yeux ». Dans « Complète la phrase » (« Tiene los ojos ___. »),
le visage tient dans une colonne de 130 px a 375 px de large : les yeux y font une vingtaine de pixels. La bande les
montre a toute la largeur de l'ecran.

La place des yeux est RELEVEE A L'OEIL sur les visages (<Nom>-visage.webp), en fractions du visage : milieu des deux
yeux (x, y) et ecart entre eux (en largeur du visage). OpenCV 5 n'a plus les cascades de Haar, et un modele a
telecharger pour douze visages ne vaut pas la peine. Une image refaite = une ligne a revoir ici. La planche de
controle (img/yeux-planche.png, hors du depot) se regarde avant de publier. Pas de bande pour qui n'a pas de couleur
d'yeux dans personnages.py (Anna, Lucas et ses lunettes de soleil) : aucune question ne la demande.

    python visuel/descripcion/yeux_personnes.py

Fichiers DERIVES des originaux (visuel/descripcion/img/ du dossier principal, hors du depot).
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from personnages import PERSONNAGES   # noqa: E402
from web import VISAGE, source        # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "descripcion")
W_SORTIE, H_SORTIE = 720, 300
# nom : (x, y) du milieu des yeux et ecart des yeux, en fractions du visage
YEUX = {
    "Mark":   (0.49, 0.61, 0.18), "Anna":   (0.53, 0.57, 0.21), "Diego":  (0.50, 0.495, 0.19),
    "Elena":  (0.51, 0.70, 0.16), "Pablo":  (0.50, 0.555, 0.17), "Marta":  (0.53, 0.71, 0.19),
    "Javier": (0.50, 0.485, 0.19), "Ines":   (0.52, 0.825, 0.16), "Tomas":  (0.51, 0.43, 0.17),
    "Carmen": (0.52, 0.70, 0.19), "Lucas":  (0.50, 0.70, 0.19), "Rosa":   (0.52, 0.43, 0.19),
}


def main():
    planche = []
    for nom in PERSONNAGES:
        if PERSONNAGES[nom][6] is None:
            continue
        im = Image.open(source(nom)).convert("RGB")
        W, H = im.size
        v = im.crop((int(W * VISAGE[0]), int(H * VISAGE[1]), int(W * VISAGE[2]), int(H * VISAGE[3])))
        vw, vh = v.size
        fx, fy, fe = YEUX[nom]
        # la bande : 2,6 fois l'ecart des yeux en largeur, au rapport 720 x 300
        bw = fe * vw * 2.6; bh = bw * H_SORTIE / W_SORTIE
        cx, cy = fx * vw, fy * vh
        b = v.crop((int(cx - bw / 2), int(cy - bh / 2), int(cx + bw / 2), int(cy + bh / 2))).resize((W_SORTIE, H_SORTIE), Image.LANCZOS)
        b.save(os.path.join(SORTIE, nom + "-yeux.webp"), "WEBP", quality=86, method=6)
        print("  %-8s bande de %d x %d px de l'original" % (nom, bw, bh))
        planche.append(b)
    p = Image.new("RGB", (W_SORTIE // 2 * 3, H_SORTIE // 2 * ((len(planche) + 2) // 3)), "white")
    for i, b in enumerate(planche):
        p.paste(b.resize((W_SORTIE // 2, H_SORTIE // 2)), ((i % 3) * W_SORTIE // 2, (i // 3) * H_SORTIE // 2))
    p.save(os.path.join(ICI, "img", "yeux-planche.png"))


if __name__ == "__main__":
    main()
