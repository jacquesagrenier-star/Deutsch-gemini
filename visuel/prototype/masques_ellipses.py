# -*- coding: utf-8 -*-
"""Ajoute a masques-<nom>.js les zones en ELLIPSES (ou « plein ») qui y manquent.

    python visuel/prototype/masques_ellipses.py untersuchung

POURQUOI
    detourer.py refait TOUS les masques et a besoin de SAM 2 (le modele vit sur
    le PC, dans ~/.wortando/modeles). Or une zone en ellipses -- une partie du
    corps, un petit objet -- ne passe pas par SAM : son masque est l'ellipse
    elle-meme. Ce script fait exactement le meme calcul que detourer.py pour
    ces zones-la, et SEULEMENT pour celles qui manquent au fichier : les
    masques SAM des autres zones ne bougent pas d'un pixel. Ne demande que
    Pillow, numpy et opencv -- il tourne donc dans une session cloud.

    Le jour ou detourer.py est relance sur le PC, il refait ces zones a
    l'identique (meme code, memes constantes) : rien a defaire.
"""
import io
import json
import os
import sys

import detourer as D

sys.stdout.reconfigure(encoding="utf-8")


def main():
    import cv2
    import numpy as np
    from PIL import Image

    nom = sys.argv[1]
    scene = json.load(io.open(os.path.join(D.ICI, nom + ".points.json"), encoding="utf-8"))
    chemin = os.path.join(D.ICI, "masques-%s.js" % nom)
    texte = io.open(chemin, encoding="utf-8").read()
    M = json.loads(texte[texte.index("{"):texte.rindex("}") + 1])
    W, H = Image.open(os.path.join(D.ICI, scene["image"])).size
    if (W, H) != (M["W"], M["H"]):
        sys.exit("  l'image (%dx%d) n'est plus celle des masques (%dx%d) : relancer detourer.py"
                 % (W, H, M["W"], M["H"]))
    w, h = W // D.REDUCTION, H // D.REDUCTION
    noyau = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (D.NETTOYAGE, D.NETTOYAGE))
    ajoutes = 0
    for z in scene["points"]:
        if z["id"] in M["zones"]:
            continue
        if not (z.get("ellipses") or z.get("plein")):
            sys.exit("  %s n'a pas de masque et demande SAM : detourer.py, sur le PC" % z["id"])
        m = np.zeros((H, W), np.uint8)
        if z.get("plein"):
            for x, y, bw, bh in D.boites_de(z):
                cv2.rectangle(m, (round(W * x / 100), round(H * y / 100)),
                              (round(W * (x + bw) / 100), round(H * (y + bh) / 100)), 1, -1)
        else:
            for cx, cy, rx, ry in z["ellipses"]:
                cv2.ellipse(m, (round(W * cx / 100), round(H * cy / 100)),
                            (round(W * rx / 100), round(H * ry / 100)), 0, 0, 360, 1, -1)
        # La suite est celle de detourer.py, zone par zone.
        m8 = cv2.morphologyEx(m * 255, cv2.MORPH_CLOSE, noyau)
        m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, noyau)
        contours, _ = cv2.findContours(m8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        polys = []
        for c in contours:
            if cv2.contourArea(c) < D.MIETTE:
                continue
            a = cv2.approxPolyDP(c, D.SIMPLIFICATION, True).reshape(-1, 2)
            polys.append([int(v) for v in a.ravel()])
        if not polys:
            sys.exit("  %s : trop petite pour etre tracee (< %d px2) -- agrandir l'ellipse"
                     % (z["id"], D.MIETTE))
        petit = np.array(Image.fromarray(m8).resize((w, h), Image.BILINEAR)) > 127
        M["zones"][z["id"]] = D.rle(petit.ravel().tolist())
        M["traces"][z["id"]] = polys
        ajoutes += 1
        print("  + %-13s %5.2f %% de l'image" % (z["id"], petit.mean() * 100))
    if not ajoutes:
        print("  rien a ajouter")
        return
    js = ("// GENERE par detourer.py (SAM 2) -- ne pas modifier a la main.\n"
          "window.MASQUES = " + json.dumps({"w": M["w"], "h": M["h"], "zones": M["zones"],
                                            "W": M["W"], "H": M["H"], "traces": M["traces"]},
                                           separators=(",", ":")) + ";\n")
    io.open(chemin, "w", encoding="utf-8").write(js)
    print("  -> masques-%s.js (%d zones ajoutees)" % (nom, ajoutes))


if __name__ == "__main__":
    main()
