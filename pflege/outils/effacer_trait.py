# -*- coding: utf-8 -*-
"""Efface un trait SOMBRE et fin d'une image (un fil, un cordon) le long d'un tracé, sans payer de reprise.

    python pflege/outils/effacer_trait.py <source.png> <sortie.png> pflege/scenes/<nom>-trait.json [--voir masque.png]

POURQUOI (15 nov. 2026, soins-telefon)
    Trois prises de fal ont redonné un combiné à fil en plus de celui posé sur la base du téléphone de
    bureau. Le fil ne reliait rien (il finit sous la main qui écrit) : l'effacer fait du combiné tenu le
    téléphone sans fil du service, et l'image redevient cohérente. visuel/effacer_texte.py efface des
    RECTANGLES ; un fil en diagonale sur un avant-bras demande un masque qui suit le fil.

LE FICHIER DU TRACÉ
    {"traits": [{"points": [[x, y], ...], "largeur": 44, "sombre": 85}]}
    points : le tracé en pixels de l'image ORIGINALE ; largeur : la bande autour du tracé ; sombre : seuls
    les pixels de cette bande plus sombres que ce seuil (0-255) sont effacés, la peau et le tissu restent.
    Le masque est élargi de 3 px puis rempli par cv2.inpaint (Telea).
"""
import io
import json
import sys

import cv2
import numpy as np


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) < 3:
        sys.exit(__doc__)
    src, out, trace = a[:3]
    img = cv2.imdecode(np.fromfile(src, dtype=np.uint8), cv2.IMREAD_COLOR)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    masque = np.zeros(gris.shape, np.uint8)
    for t in json.load(io.open(trace, encoding="utf-8"))["traits"]:
        bande = np.zeros(gris.shape, np.uint8)
        cv2.polylines(bande, [np.array(t["points"], np.int32)], False, 255, int(t.get("largeur", 40)))
        masque |= ((bande > 0) & (gris < int(t.get("sombre", 85)))).astype(np.uint8) * 255
    masque = cv2.dilate(masque, np.ones((7, 7), np.uint8))
    res = cv2.inpaint(img, masque, 7, cv2.INPAINT_TELEA)
    cv2.imencode(".png", res)[1].tofile(out)
    if "--voir" in sys.argv:
        cv2.imencode(".png", masque)[1].tofile(sys.argv[sys.argv.index("--voir") + 1])
    print("%d pixels effacés -> %s" % (int((masque > 0).sum()), out))


if __name__ == "__main__":
    main()
