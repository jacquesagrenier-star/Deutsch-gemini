# -*- coding: utf-8 -*-
"""Trouver le velo peint par CORRESPONDANCE DE MOTIF, plan par plan.

    python video/trouver_velo.py --scene 03-auf-dem-radweg

POURQUOI, APRES TOUT LE RESTE.

Le 23 septembre 2026 j'ai essaye, dans l'ordre : un seuil de couleur absolu,
un test de voisinage a 3 puis 4 cotes, une garde par la forme, une garde
<< entoure de rouge >>, et un seuil d'Otsu par plan. Aucun n'a converge : le
contraste du pictogramme va du blanc franc au rose pale selon le plan, donc
tout critere de CLARTE se trompe quelque part.

⚠️ ET J'AI MIS DES HEURES A VOIR L'EVIDENCE : C'EST LE MEME DESSIN PARTOUT.
   Tous les plans viennent du meme jeu d'images, et le pictogramme de Radweg
   est un glyphe normalise. On ne cherche donc pas << quelque chose de clair
   sur du rouge >> -- on cherche UN DESSIN CONNU. C'est le probleme que
   matchTemplate resout, et cv2 etait installe depuis le debut.
   La lecon, pour la prochaine fois : quand cinq criteres d'apparence echouent
   l'un apres l'autre, c'est qu'on decrit la mauvaise chose. Un objet
   identique d'un plan a l'autre se cherche par sa FORME, pas par sa teinte.

⚠️ LA PERSPECTIVE CHANGE, PAS LE DESSIN. Selon le plan, le velo est vu de
   presque face ou tres rasant : sa largeur et sa hauteur ne varient pas dans
   le meme rapport. On balaie donc les deux INDEPENDAMMENT, ce qu'un
   redimensionnement uniforme ne ferait pas.
"""
import argparse
import os
import sys

import numpy as np

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import effacer_marquage as EM                              # noqa: E402


def gabarit():
    """Le glyphe seul, en niveaux de gris, depuis carrefour-rouge-v7.png.

    ⚠️ PAS carrefour-rouge.png : c'est desormais l'image de Jimmy, qui n'a PAS
       de pictogramme. La v7 est ma version, celle qui en portait un -- rangee
       justement parce qu'une prise ne s'ecrase pas.
    """
    from PIL import Image
    f = os.path.join(RACINE, "video", "episode-03-auf-dem-radweg",
                     "01-images", "carrefour-rouge-v7.png")
    if not os.path.exists(f):
        sys.exit("  gabarit introuvable : %s" % f)
    im = np.array(Image.open(f).convert("RGB")).astype(np.int16)
    # La boite du glyphe, mesuree le 23 sept. : x 605..1100, y 2090..2220.
    g = im[2090:2220, 605:1100]
    r, v, b = g[:, :, 0], g[:, :, 1], g[:, :, 2]
    clarte = 0.299 * r + 0.587 * v + 0.114 * b
    # Normalise : on garde la FORME, pas les niveaux.
    c = clarte - clarte.min()
    c = c / max(1.0, c.max())
    return (c * 255).astype(np.uint8)


def chercher(fond, gab, bande, echelles_l, echelles_h, seuil):
    """Le meilleur emplacement du glyphe dans la bande, et son score."""
    import cv2
    r = fond[:, :, 0].astype(np.int16)
    v = fond[:, :, 1].astype(np.int16)
    b = fond[:, :, 2].astype(np.int16)
    clarte = 0.299 * r + 0.587 * v + 0.114 * b
    img = np.clip(clarte, 0, 255).astype(np.uint8)
    H, L = img.shape
    meilleur = (None, -1.0, None)
    for fl in echelles_l:
        for fh in echelles_h:
            w = int(gab.shape[1] * fl)
            h = int(gab.shape[0] * fh)
            if w < 24 or h < 10 or w > L or h > H:
                continue
            t = cv2.resize(gab, (w, h), interpolation=cv2.INTER_AREA)
            res = cv2.matchTemplate(img, t, cv2.TM_CCOEFF_NORMED)
            _, mx, _, loc = cv2.minMaxLoc(res)
            if mx > meilleur[1]:
                meilleur = ((loc[0], loc[1], w, h), mx, t)
    if meilleur[1] < seuil:
        return None, meilleur[1]
    x, y, w, h = meilleur[0]
    # Le glyphe doit tomber SUR la bande, sinon c'est une ressemblance fortuite.
    part = bande[y:y + h, x:x + w].mean() if h and w else 0.0
    if part < 0.45:
        return None, meilleur[1]
    return meilleur[0], meilleur[1]


def main():
    p = argparse.ArgumentParser(
        description="Trouver le velo peint par correspondance de motif.")
    p.add_argument("--scene", required=True)
    p.add_argument("--plans")
    p.add_argument("--seuil", type=float, default=0.42)
    a = p.parse_args()

    from scipy import ndimage
    gab = gabarit()
    print("  gabarit : %dx%d" % (gab.shape[1], gab.shape[0]))

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    dossier = os.path.join(ep, "_montage-avatar")
    nums = ([int(v) for v in a.plans.split(",")] if a.plans else
            sorted(int(f[4:6]) for f in os.listdir(dossier)
                   if f.startswith("plan") and f.endswith(".mp4")))

    el = [0.20, 0.30, 0.42, 0.55, 0.70, 0.85, 1.00, 1.20]
    eh = [0.20, 0.30, 0.42, 0.55, 0.70, 0.85, 1.00, 1.30, 1.70]
    for n in nums:
        clip = os.path.join(dossier, "plan%02d.mp4" % n)
        if not os.path.exists(clip):
            continue
        L, H, _ = EM.dimensions(clip)
        fond, _ = EM.fond_median(clip, L, H)
        r = fond[:, :, 0].astype(np.int16)
        v = fond[:, :, 1].astype(np.int16)
        b = fond[:, :, 2].astype(np.int16)
        rouge = ((r - v > EM.ROUGE_RG) & (r - b > EM.ROUGE_RB) & (v - b < 4))
        lab, nn = ndimage.label(rouge)
        bande = np.zeros(rouge.shape, dtype=bool)
        if nn:
            tailles = ndimage.sum(rouge, lab, index=np.arange(1, nn + 1))
            grandes = np.zeros(nn + 1, dtype=bool)
            grandes[1:] = tailles >= 20000
            bande = grandes[lab]
        if not bande.any():
            print("   plan %02d : pas de bande -- ignore" % n)
            continue
        boite, score = chercher(fond, gab, bande, el, eh, a.seuil)
        if boite is None:
            print("   plan %02d : rien trouve (meilleur score %.2f)" % (n, score))
        else:
            x, y, w, h = boite
            print("   plan %02d : velo a x %d..%d  y %d..%d   score %.2f"
                  % (n, x, x + w, y, y + h, score))


if __name__ == "__main__":
    main()
