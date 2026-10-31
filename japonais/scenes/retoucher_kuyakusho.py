# -*- coding: utf-8 -*-
"""Retouche locale (gratuite) de la scene kuyakusho : le passeport.

    python japonais/scenes/retoucher_kuyakusho.py

La prise du 31 oct. 2026 a pose sur le comptoir un passeport JAPONAIS
(chrysantheme dore, « 日本国 JAPAN ») : du texte dans l'image, et un contresens,
Camille est canadienne. Mon prompt disait « dark-red passport » ; un passeport
canadien est bleu marine. On repeint la couverture en bleu marine uni, en
gardant la lumiere de la photo : le motif dore est d'abord efface par un
grand filtre median, puis chaque pixel prend le bleu marine module par la
luminance d'origine. Bord adouci.

Entree  visuel/scenes/kuyakusho.png (source hors depot)
Sortie  visuel/scenes/kuyakusho-propre.png
"""
import os

import cv2
import numpy as np

RACINE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = os.path.join(RACINE, "visuel", "scenes", "kuyakusho.png")
SORTIE = os.path.join(RACINE, "visuel", "scenes", "kuyakusho-propre.png")

# Couverture, en pixels de la source 1536 x 2752 (mesuree sur une grille de 20 px),
# jusqu'au bord de la couverture (la tranche et les pages blanches restent).
COUVERTURE = [(967, 1820), (1061, 1869), (946, 1936), (848, 1886)]
MARINE = np.array([72, 38, 22], np.float32)       # BGR, bleu marine


def main():
    img = cv2.imread(SRC)
    m = np.zeros(img.shape[:2], np.uint8)
    cv2.fillPoly(m, [np.array(COUVERTURE, np.int32)], 255)
    lisse = cv2.medianBlur(img, 51)
    lum = cv2.cvtColor(lisse, cv2.COLOR_BGR2GRAY).astype(np.float32)
    ref = float(np.median(lum[m > 0]))
    marine = np.clip(MARINE[None, None, :] * np.clip(lum / ref, 0.85, 1.15)[:, :, None], 0, 255)
    alpha = cv2.GaussianBlur(m.astype(np.float32) / 255.0, (3, 3), 0)[:, :, None]
    res = (img.astype(np.float32) * (1 - alpha) + marine * alpha).astype(np.uint8)
    cv2.imwrite(SORTIE, res)
    print("  %s : %d px repeints" % (os.path.basename(SORTIE), int((m > 0).sum())))


if __name__ == "__main__":
    main()
