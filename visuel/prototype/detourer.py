# -*- coding: utf-8 -*-
"""Le contour exact de chaque objet de la scene, par SAM 2. Gratuit, local.

    python visuel/prototype/detourer.py            # ecrit masques-klassenzimmer.js
    python visuel/prototype/detourer.py --voir     # + une image de controle

POURQUOI
    Jacques, 6 oct. 2026 : « comme sur Apple, l'objet au complet selectionne,
    meme avec les pattes de la table ». Les rectangles de
    klassenzimmer.points.json attrapaient le mur autour de l'horloge et
    manquaient les pattes de la table. On touche maintenant les PIXELS de
    l'objet, et le surlignage suit son contour.

COMMENT
    Les rectangles ne servent plus a toucher : ils servent a DIRE a SAM 2 ou
    chercher (un rectangle par zone, celui qui englobe toutes ses boites). SAM
    rend un masque par zone. On le reduit a 1/3 de la resolution et on l'ecrit
    en longueurs de plages (RLE), ce qui tient en quelques dizaines de Ko.

    Le modele (sam2.1_b.pt, ~80 Mo, Meta, Apache 2.0) vit dans
    ~/.wortando/modeles : hors du depot, hors de OneDrive.

CE QU'IL NE FAIT PAS
    Decider qui est devant qui. Les masques se recouvrent (le manteau passe
    derriere l'epaule de Mark) ; c'est le PLAN (champ devant, herite par sur)
    qui tranche dans l'app, comme avec les rectangles.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
MODELES = os.path.join(os.path.expanduser("~"), ".wortando", "modeles")
REDUCTION = 3            # le masque garde 1 pixel sur 3 : 360 x 645


def englobe(boites):
    x = min(b[0] for b in boites)
    y = min(b[1] for b in boites)
    return [x, y, max(b[0] + b[2] for b in boites) - x,
            max(b[1] + b[3] for b in boites) - y]


def rle(bits):
    """Longueurs alternees, en commencant par une plage de 0."""
    plages, courant, n = [], 0, 0
    for b in bits:
        if b == courant:
            n += 1
        else:
            plages.append(n)
            courant, n = b, 1
    plages.append(n)
    return plages


def main():
    import numpy as np
    from PIL import Image
    from ultralytics import SAM

    scene = json.load(io.open(os.path.join(ICI, "klassenzimmer.points.json"),
                              encoding="utf-8"))
    image = os.path.join(ICI, scene["image"])
    W, H = Image.open(image).size

    os.makedirs(MODELES, exist_ok=True)
    avant = os.getcwd()
    os.chdir(MODELES)              # ultralytics telecharge dans le dossier courant
    try:
        modele = SAM("sam2.1_b.pt")
    finally:
        os.chdir(avant)

    zones = scene["points"]
    boites = []
    for z in zones:
        x, y, w, h = z.get("sam") or englobe(z.get("boites") or [z["boite"]])
        boites.append([W * x / 100, H * y / 100, W * (x + w) / 100, H * (y + h) / 100])
    print("  %d zones, image %dx%d, SAM 2 sur processeur..." % (len(zones), W, H))
    res = modele(image, bboxes=boites, verbose=False)[0]
    masques = res.masks.data.cpu().numpy().astype(bool)     # (N, H, W)
    if len(masques) != len(zones):
        sys.exit("  SAM a rendu %d masques pour %d zones" % (len(masques), len(zones)))

    w, h = W // REDUCTION, H // REDUCTION
    sortie = {}
    for z, m in zip(zones, masques):
        petit = np.array(Image.fromarray(m.astype(np.uint8) * 255)
                         .resize((w, h), Image.BILINEAR)) > 127
        couverture = petit.mean() * 100
        boite = z.get("sam") or englobe(z.get("boites") or [z["boite"]])
        part = couverture / (boite[2] * boite[3] / 100) * 100 if boite[2] * boite[3] else 0
        print("  %-13s %5.2f %% de l'image, %3.0f %% de sa boite" % (z["id"], couverture, part))
        sortie[z["id"]] = rle(petit.ravel().tolist())

    js = ("// GENERE par detourer.py (SAM 2) -- ne pas modifier a la main.\n"
          "window.MASQUES = " + json.dumps({"w": w, "h": h, "zones": sortie},
                                           separators=(",", ":")) + ";\n")
    chemin = os.path.join(ICI, "masques-klassenzimmer.js")
    io.open(chemin, "w", encoding="utf-8").write(js)
    print("  -> masques-klassenzimmer.js (%d Ko)" % (os.path.getsize(chemin) // 1024))

    if "--voir" in sys.argv:
        rng = np.random.default_rng(3)
        fond = np.array(Image.open(image).convert("RGB").resize((w, h))).astype(float)
        for z, m in zip(zones, masques):
            petit = np.array(Image.fromarray(m.astype(np.uint8) * 255).resize((w, h))) > 127
            fond[petit] = fond[petit] * 0.45 + rng.integers(60, 255, 3) * 0.55
        controle = os.path.join(os.environ.get("TMP", ICI), "masques.png")
        Image.fromarray(fond.astype(np.uint8)).save(controle)
        print("  controle : %s" % controle)


if __name__ == "__main__":
    main()
