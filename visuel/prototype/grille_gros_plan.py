# -*- coding: utf-8 -*-
"""Controle des ellipses d'un gros plan : une zone de l'image source, agrandie,
sous une grille fine, avec les ellipses actuelles dessinees dessus.

    python visuel/prototype/grille_gros_plan.py X0 Y0 X1 Y1 PAS K SORTIE.png [GROS_PLAN]
    python visuel/prototype/grille_gros_plan.py 43.5 29 56.5 40.5 0.25 4 visage.png visage-mark

Coordonnees en % de l'image (celles de arztpraxis.points.json). PAS = l'ecart
de la grille (0,25 % pour un visage), K = l'agrandissement. Ne a la demande
de Jacques (6 oct. 2026) : des cercles places a l'oeil sur une grille de 1 %
tombaient a cote de l'oeil droit et de l'oreille. Mesurer, puis corriger.
"""
import io
import json
import os
import sys

from PIL import Image, ImageDraw

ICI = os.path.dirname(os.path.abspath(__file__))
x0, y0, x1, y1, pas, K = [float(v) for v in sys.argv[1:7]]
sortie = sys.argv[7]
gid = sys.argv[8] if len(sys.argv) > 8 else None
pts = json.load(io.open(os.path.join(ICI, "arztpraxis.points.json"), encoding="utf-8"))
src = Image.open(os.path.normpath(os.path.join(ICI, pts["source"]))).convert("RGB")
W, H = src.size
K = int(K)
X = lambda v: (W * v / 100 - round(W * x0 / 100)) * K
Y = lambda v: (H * v / 100 - round(H * y0 / 100)) * K
im = src.crop((round(W * x0 / 100), round(H * y0 / 100), round(W * x1 / 100), round(H * y1 / 100)))
im = im.resize((im.width * K, im.height * K), Image.LANCZOS)
d = ImageDraw.Draw(im)
v = x0
while v <= x1 + 1e-9:
    fort = abs(v - round(v)) < 1e-6
    d.line([(X(v), 0), (X(v), im.height)], fill=(255, 0, 0) if fort else (255, 190, 190), width=1)
    if abs(v * 2 - round(v * 2)) < 1e-6:
        d.text((X(v) + 2, 2), "%g" % v, fill=(200, 0, 0))
    v = round(v + pas, 4)
v = y0
while v <= y1 + 1e-9:
    fort = abs(v - round(v)) < 1e-6
    d.line([(0, Y(v)), (im.width, Y(v))], fill=(0, 0, 255) if fort else (190, 190, 255), width=1)
    if abs(v * 2 - round(v * 2)) < 1e-6:
        d.text((2, Y(v) + 2), "%g" % v, fill=(0, 0, 200))
    v = round(v + pas, 4)
if gid:
    g = next(x for x in pts["gros_plans"] if x["id"] == gid)
    for q in g["parties"]:
        cx, cy, rx, ry = q["forme"]
        d.ellipse([X(cx - rx), Y(cy - ry), X(cx + rx), Y(cy + ry)], outline=(255, 150, 0), width=2)
        d.text((X(cx) - 12, Y(cy) - 6), q.get("id") or q.get("ref"), fill=(255, 255, 0))
im.save(sortie)
print("  %s  (%d x %d)" % (sortie, im.width, im.height))
