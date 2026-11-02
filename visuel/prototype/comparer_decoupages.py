# -*- coding: utf-8 -*-
"""Captures AVANT / APRES des contours : l'ancien trace a gauche (ambre), le
nouveau a droite (cyan), sur l'image de la scene.

    python visuel/prototype/comparer_decoupages.py museum jacke,krawatte sortie.jpg
    python visuel/prototype/comparer_decoupages.py museum auto sortie.jpg   # ce qui a change
    python visuel/prototype/comparer_decoupages.py museum jacke sortie.jpg --avant b4c2f27
    python visuel/prototype/comparer_decoupages.py museum jacke sortie.jpg --x4  # comme a x4

L'AVANT est lu dans git (--avant, par defaut HEAD : les masques publies), l'APRES
dans le dossier. --x4 montre la zone comme sur un telephone de 390 px agrandi
quatre fois (1 px de l'image ~ 1 px d'ecran), pour juger les facettes.
Ne demande que Pillow, numpy et opencv.
"""
import io
import json
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image

import detourer as D

sys.stdout.reconfigure(encoding="utf-8")


def lire_js(texte):
    return json.loads(texte[texte.index("{"):texte.rindex("}") + 1])


def avant(nom, ref):
    chemin = "visuel/prototype/masques-%s.js" % nom
    racine = os.path.dirname(os.path.dirname(D.ICI))
    return lire_js(subprocess.run(["git", "show", "%s:%s" % (ref, chemin)], cwd=racine,
                                  capture_output=True, check=True).stdout.decode("utf-8"))


def cellule(img, M, i, cadre, k, couleur):
    x0, y0, x1, y1 = cadre
    c = cv2.resize(img[y0:y1, x0:x1], None, fx=k, fy=k, interpolation=cv2.INTER_CUBIC)
    c = (c * 0.85).astype(np.uint8)
    for p in M["traces"].get(i, []):
        q = ((D.points_du_trace(p, np) - [x0, y0]) * k * 16).round().astype(np.int32)
        cv2.polylines(c, [q], True, (255, 255, 255), 4, cv2.LINE_AA, shift=4)
        cv2.polylines(c, [q], True, couleur, 2, cv2.LINE_AA, shift=4)
    cv2.putText(c, i, (5, 17), 0, 0.5, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(c, i, (5, 17), 0, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    return c


def main():
    args = sys.argv[1:]
    ref = "HEAD"
    if "--avant" in args:
        k = args.index("--avant")
        ref = args[k + 1]
        del args[k:k + 2]
    x4 = "--x4" in args
    args = [a for a in args if a != "--x4"]
    nom, choix, sortie = args[:3]
    A = avant(nom, ref)
    N = lire_js(io.open(os.path.join(D.ICI, "masques-%s.js" % nom), encoding="utf-8").read())
    S = json.load(io.open(os.path.join(D.ICI, nom + ".points.json"), encoding="utf-8"))
    img = np.array(Image.open(os.path.join(D.ICI, S["image"])).convert("RGB"))
    if choix == "auto":
        ids = []
        for i in N["zones"]:
            if i not in A["zones"]:
                continue
            o, n = D.derle(A["zones"][i], A["w"], A["h"]), D.derle(N["zones"][i], N["w"], N["h"])
            if (o & n).sum() / max((o | n).sum(), 1) < 0.95:
                ids.append(i)
    else:
        ids = choix.split(",")
    lignes = []
    for i in ids:
        pts = np.vstack([D.points_du_trace(p, np) for M in (A, N) for p in M["traces"].get(i, [])])
        x0, y0 = np.maximum(pts.min(0) - 25, 0).astype(int)
        x1, y1 = np.minimum(pts.max(0) + 25, [img.shape[1], img.shape[0]]).astype(int)
        if x4:
            k = 390 / img.shape[1] * 4
            cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
            t = int(360 / k)
            x0, y0 = max(0, cx - t // 2), max(0, cy - t // 2)
            x1, y1 = min(img.shape[1], x0 + t), min(img.shape[0], y0 + t)
        else:
            k = min(3.0, 300 / max(x1 - x0, y1 - y0))
        a = cellule(img, A, i, (x0, y0, x1, y1), k, (232, 162, 58))
        b = cellule(img, N, i, (x0, y0, x1, y1), k, (0, 210, 255))
        lignes.append(np.hstack([a, np.full((a.shape[0], 6, 3), 255, np.uint8), b]))
    if not lignes:
        print("  rien n'a change")
        return
    cols = 2 if x4 else 3
    larg = max(l.shape[1] for l in lignes)
    lignes = [np.pad(l, ((0, 8), (0, larg - l.shape[1] + 12), (0, 0)), constant_values=255) for l in lignes]
    rangs = []
    for j in range(0, len(lignes), cols):
        g = lignes[j:j + cols]
        h = max(l.shape[0] for l in g)
        g = [np.pad(l, ((0, h - l.shape[0]), (0, 0), (0, 0)), constant_values=255) for l in g]
        g += [np.full((h, lignes[0].shape[1], 3), 255, np.uint8)] * (cols - len(g))
        rangs.append(np.hstack(g))
    Image.fromarray(np.vstack(rangs)).save(sortie, quality=82)
    print("  %s : %d zone(s) -- %s" % (sortie, len(ids), ", ".join(ids)))


if __name__ == "__main__":
    main()
