# -*- coding: utf-8 -*-
"""Efface le texte et les logos d'une image de scene, sur place, gratuitement.

    python visuel/effacer_texte.py <source.png> <sortie.png> <zones.json> [--voir controle.png]

POURQUOI. Une scene ne porte JAMAIS de mots : l'app pose les etiquettes dans
la langue de l'usager. Le generateur en met quand meme (le « TAXI » sur le
toit, le numero du tram, le cor de la Deutsche Post), et repayer une image
pour trois details risque de deplacer ce qui est reussi (voir
video/verifier_prompt.py, acquis « retirer par retouche »). Ces details sont
presque toujours des traits FONCES sur un aplat de couleur : on les repeint.

COMMENT. Chaque zone est un rectangle [x, y, largeur, hauteur] en PIXELS de la
source. Dedans, le masque prend les pixels nettement plus sombres que la
mediane du rectangle (les lettres), un peu elargi, et OpenCV les remplit
depuis les bords (inpaint Telea) : le degrade et l'ombre de l'aplat restent.
Une zone peut forcer tout le rectangle (« tout » : true) quand le motif
n'est pas plus sombre que son fond.
"""
import json
import sys

import cv2
import numpy as np


def main():
    src, sortie, zones_f = sys.argv[1:4]
    img = cv2.imread(src)
    zones = json.load(open(zones_f, encoding="utf-8"))
    masque = np.zeros(img.shape[:2], np.uint8)
    # « poly » + « echantillon » : un motif qui remplit une face inclinee (les
    # lettres TAXI sur leur boitier). Un rectangle debordait sur la route,
    # que le seuil prenait pour des lettres. On peint tout le polygone avec
    # la couleur de l'echantillon [x, y, l, h], puis on adoucit le bord.
    peints = []
    for z in zones:
        if "poly" not in z:
            continue
        m = np.zeros(img.shape[:2], np.uint8)
        cv2.fillPoly(m, [np.array(z["poly"], np.int32)], 255)
        ex, ey, ew, eh = z["echantillon"]
        couleur = np.median(img[ey:ey + eh, ex:ex + ew].reshape(-1, 3), axis=0)
        peints.append((m, couleur))
        print("  %-18s %5d px peints" % (z["nom"], int((m > 0).sum())))
    for z in zones:
        if "poly" in z:
            continue
        x, y, w, h = z["boite"]
        bloc = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY).astype(int)
        if z.get("tout"):
            m = np.full(bloc.shape, 255, np.uint8)
        else:
            seuil = np.median(bloc) - z.get("ecart", 45)
            m = (bloc < seuil).astype(np.uint8) * 255
        m = cv2.dilate(m, np.ones((5, 5), np.uint8), iterations=1)
        masque[y:y + h, x:x + w] = np.maximum(masque[y:y + h, x:x + w], m)
        print("  %-18s %5d px effaces" % (z["nom"], int((m > 0).sum())))
    res = cv2.inpaint(img, masque, 6, cv2.INPAINT_TELEA) if masque.any() else img.copy()
    for m, couleur in peints:
        res[m > 0] = couleur.astype(np.uint8)
        bord = cv2.dilate(m, np.ones((3, 3), np.uint8)) - cv2.erode(m, np.ones((3, 3), np.uint8))
        douce = cv2.GaussianBlur(res, (5, 5), 0)
        res[bord > 0] = douce[bord > 0]
    # « remplir » : quand le motif couvre presque tout son support (les lettres
    # du boitier TAXI), l'inpaint va chercher la couleur AUTOUR du support (le
    # toit blanc, la route) et fait une tache. On peint alors avec la couleur
    # du support lui-meme : la mediane de ses pixels vifs hors du masque.
    for z in zones:
        if not z.get("remplir"):
            continue
        x, y, w, h = z["boite"]
        bloc = img[y:y + h, x:x + w].astype(int)
        m = masque[y:y + h, x:x + w] > 0
        vif = (bloc.max(axis=2) - bloc.min(axis=2)) > 70
        couleur = np.median(bloc[vif & ~m], axis=0) if (vif & ~m).any() else np.median(bloc[~m], axis=0)
        zone = res[y:y + h, x:x + w].copy()
        zone[m] = couleur.astype(np.uint8)
        douce = cv2.GaussianBlur(zone, (3, 3), 0)
        zone[m] = douce[m]
        res[y:y + h, x:x + w] = zone
    cv2.imwrite(sortie, res)
    if "--voir" in sys.argv:
        ctl = sys.argv[sys.argv.index("--voir") + 1]
        bandes = []
        for z in zones:
            x, y, w, h = z["boite"]
            m = 20
            a = img[max(0, y - m):y + h + m, max(0, x - m):x + w + m]
            b = res[max(0, y - m):y + h + m, max(0, x - m):x + w + m]
            paire = np.hstack([a, np.full((a.shape[0], 8, 3), 255, np.uint8), b])
            paire = cv2.resize(paire, (int(paire.shape[1] * 220 / paire.shape[0]), 220))
            bandes.append(paire)
        largeur = max(b.shape[1] for b in bandes)
        bandes = [np.hstack([b, np.full((b.shape[0], largeur - b.shape[1], 3), 255, np.uint8)]) for b in bandes]
        cv2.imwrite(ctl, np.vstack(bandes))
    print("  ->", sortie)


if __name__ == "__main__":
    main()
