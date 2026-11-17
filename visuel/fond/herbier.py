# -*- coding: utf-8 -*-
"""L'herbier, le fond de l'accueil Soins (Wortando Pflege, 16 nov. 2026 ; Jacques : « le herbier est plus positif »).

Quatre plantes de soin gravees au trait fin, chacune avec son nom latin en italique, comme une planche d'herbier :
la camomille (Matricaria chamomilla), la lavande (Lavandula angustifolia), la sauge (Salvia officinalis) et
l'arnica (Arnica montana), plus des fleurs, des feuilles et des epis poses a cote, pour remplir le ciel comme les
continents. La tuile a la taille de la carte du monde (960 x 378, repetee en largeur et defilant comme elle) :
le moteur ne change que l'image de .fm-piste et de .spf-piste (le filigrane de la carte de la seance).

    python visuel/fond/herbier.py                    # herbier-jour.svg, herbier-nuit.svg, herbier-filigrane.svg
    python visuel/fond/herbier.py --apercu <dossier> # et trois PNG d'apercu (Pillow), sans navigateur

Fichiers DERIVES : corriger ce script, pas les SVG. Tout est tire d'un hasard a graine fixe : meme dessin a chaque fois.
"""
import math
import os
import random
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
L_TUILE, H_TUILE = 960, 378
R = random.Random(16112026)
ELEMENTS = []   # (sorte, points, ferme)
TEXTES = []     # (x, y, texte)


# ---------- geometrie ----------
def bez(p0, p1, p2, p3, n=24):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        out.append((u * u * u * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t * t * t * p3[0],
                    u * u * u * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t * t * t * p3[1]))
    return out


def tr(pts, ox, oy, ang=0.0, s=1.0, sy=1.0):
    a = math.radians(ang)
    c, sn = math.cos(a), math.sin(a)
    return [(ox + s * (x * c - y * sy * sn), oy + s * (x * sn + y * sy * c)) for x, y in pts]


def ajouter(sorte, pts, ferme=False):
    ELEMENTS.append((sorte, pts, ferme))


def le_long(pts, t):
    """Le point et la direction (degres) a la fraction t d'une polyligne."""
    longs = [0.0]
    for a, b in zip(pts, pts[1:]):
        longs.append(longs[-1] + math.dist(a, b))
    cible = t * longs[-1]
    for i in range(1, len(pts)):
        if longs[i] >= cible or i == len(pts) - 1:
            a, b = pts[i - 1], pts[i]
            seg = (longs[i] - longs[i - 1]) or 1
            f = min(max((cible - longs[i - 1]) / seg, 0), 1)
            return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    return pts[-1], 0.0


def tige(p0, p1, p2, p3, sorte="tige"):
    pts = bez(p0, p1, p2, p3, 30)
    ajouter(sorte, pts)
    return pts


# ---------- feuilles ----------
FORMES = {  # a, b, c, d : les points de controle du bord, en fractions de la longueur et de la demi-largeur
    "ovale": (0.05, 1.25, 0.55, 1.0),
    "oblong": (0.10, 1.10, 0.78, 1.05),
    "lance": (0.20, 1.00, 0.70, 0.90),
    "arnica": (0.15, 1.15, 0.70, 0.85),
}


def feuille(ox, oy, ang, L, W, forme="ovale", creneaux=0.0, nb_cren=12, courbe=0.0, nerv="penne", nv=5,
            hachures=True, petiole=0.0):
    a, b, c, d = FORMES[forme]
    haut = bez((0, 0), (L * a, -W * b), (L * c, -W * d), (L, 0), 22 if not creneaux else 34)
    bas = [(x, -y) for x, y in reversed(haut)]

    def demi_largeur(x):
        for (x1, y1), (x2, y2) in zip(haut, haut[1:]):
            if x1 <= x <= x2:
                return -(y1 + (y2 - y1) * ((x - x1) / ((x2 - x1) or 1)))
        return 0.0

    def cren(pts):
        if not creneaux:
            return pts
        return [(x, y * (1 - creneaux * (1 - abs(math.sin(nb_cren * math.pi * x / L))))) for x, y in pts]

    def plier(pts):
        return [(x + petiole, y + courbe * L * (x / L) ** 2) for x, y in pts]

    bord = plier(cren(haut) + cren(bas)[1:])
    ajouter("masse", tr(bord, ox, oy, ang), True)
    if petiole:
        ajouter("trait", tr([(0, 0), (petiole + 1, 0)], ox, oy, ang))
    ajouter("trait", tr(plier([(x, 0) for x in (0, L * 0.3, L * 0.6, L * 0.93)]), ox, oy, ang))
    if nerv == "penne":
        pas = 0.72 / nv
        for i in range(nv):
            t0 = 0.10 + i * pas
            xe = min(t0 + 0.24, 0.94) * L
            for cote in (-1, 1):
                v = bez((t0 * L, 0), (t0 * L + 0.06 * L, cote * 0.25 * demi_largeur(t0 * L)),
                        (xe - 0.05 * L, cote * 0.7 * demi_largeur(xe)), (xe, cote * 0.84 * demi_largeur(xe)), 8)
                ajouter("trait", tr(plier(v), ox, oy, ang))
            if hachures:   # l'ombre de la gravure : de fines hachures sur la moitie du dessous
                for k in (0.33, 0.66):
                    tm = t0 + k * pas
                    xe2 = min(tm + 0.16, 0.92) * L
                    h = [(tm * L + 0.02 * L, 0.12 * demi_largeur(tm * L)), (xe2, 0.62 * demi_largeur(xe2))]
                    ajouter("fin", tr(plier(h), ox, oy, ang))
    elif nerv == "paralleles":
        for f in (-0.72, -0.38, 0.38, 0.72):
            v = bez((0.04 * L, 0), (0.3 * L, f * demi_largeur(0.3 * L) * 1.1), (0.75 * L, f * demi_largeur(0.75 * L)),
                    (0.93 * L, f * 0.15 * W), 16)
            ajouter("trait", tr(plier(v), ox, oy, ang))
        if hachures:
            for f in (0.15, 0.55, 0.88):
                v = bez((0.12 * L, f * 0.5 * W), (0.35 * L, f * demi_largeur(0.35 * L) * 0.95),
                        (0.65 * L, f * demi_largeur(0.65 * L) * 0.9), (0.85 * L, f * 0.2 * W), 12)
                ajouter("fin", tr(plier(v), ox, oy, ang))


def feuille_fine(ox, oy, ang, L, cote=1):
    """Feuille de camomille : decoupee en lanieres fines (bipennee), au trait seul."""
    rachis = bez((0, 0), (L * 0.3, -cote * L * 0.05), (L * 0.7, -cote * L * 0.09), (L, -cote * L * 0.02), 18)
    ajouter("fil", tr(rachis, ox, oy, ang))
    n = 7
    for i in range(1, n + 1):
        p, d = le_long(rachis, i / (n + 0.6))
        seg = L * 0.30 * (1 - 0.65 * i / n)
        for s in (-1, 1):
            a = math.radians(d + s * 48)
            q = (p[0] + seg * math.cos(a), p[1] + seg * math.sin(a))
            m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2 + 0.6)
            ajouter("fil", tr([p, m, q], ox, oy, ang))
            a2 = math.radians(d + s * 48 + s * 34)
            mm = (p[0] + 0.55 * (q[0] - p[0]), p[1] + 0.55 * (q[1] - p[1]))
            ajouter("fil", tr([mm, (mm[0] + 0.42 * seg * math.cos(a2), mm[1] + 0.42 * seg * math.sin(a2))], ox, oy, ang))


def racines(x, y, n=5):
    for _ in range(n):
        dx = R.uniform(-9, 9)
        ajouter("fil", bez((x, y), (x + dx * 0.3, y + 4), (x + dx * 0.8, y + 7), (x + dx, y + R.uniform(9, 13)), 8))


# ---------- fleurs ----------
def capitule(cx, cy, r0, r1, n, larg, sy=0.55, ang=0.0, retombe=0.0, dents=False, desordre=0.0, dome=0.9):
    for k in range(n):
        th = 2 * math.pi * k / n + R.uniform(-desordre, desordre)
        long_ = r1 - r0 + R.uniform(-desordre, desordre) * 10
        cote = []
        for i in range(9):
            s = i / 8
            w = larg * (0.35 + 0.65 * math.sin(min(s / 0.8, 1) * math.pi / 2)) / 2
            cote.append((r0 + s * long_, -w))
        bout = r0 + long_
        if dents:
            pointe = [(bout + 1.0, -larg / 3), (bout - 0.6, -larg / 6), (bout + 1.4, 0), (bout - 0.6, larg / 6), (bout + 1.0, larg / 3)]
        else:
            pointe = [(bout + larg * 0.25 * math.cos(u), larg * 0.5 * math.sin(u)) for u in (-1.2, -0.6, 0, 0.6, 1.2)]
        petale = cote + pointe + [(x, -y) for x, y in reversed(cote)]
        c, s_ = math.cos(th), math.sin(th)
        pts = []
        for x, y in petale:
            px, py = x * c - y * s_, (x * s_ + y * c) * sy
            py += retombe * max(0.0, (math.hypot(x, y) - r0) / (r1 - r0))
            pts.append((px, py))
        ajouter("petale", tr(pts, cx, cy, ang), True)
        nerv = [(r0 + 0.25 * long_) * c, (r0 + 0.25 * long_) * s_ * sy], [(r0 + 0.8 * long_) * c, (r0 + 0.8 * long_) * s_ * sy + retombe * 0.8]
        ajouter("fin", tr(nerv, cx, cy, ang))
    # le coeur : un dome (camomille) ou un disque plus plat (arnica), pointille
    h = r0 * dome
    disque = [(r0 * math.cos(u), r0 * sy * math.sin(u)) for u in [i * math.pi / 16 for i in range(17)]]
    disque += [(r0 * math.cos(u), -h * math.sin(u)) for u in [math.pi - i * math.pi / 16 for i in range(1, 16)]]
    ajouter("disque", tr(disque, cx, cy, ang), True)
    for i in range(int(r0 * r0 * 0.9)):
        u = R.uniform(0, 2 * math.pi)
        rr = math.sqrt(R.random()) * 0.85
        x = r0 * rr * math.cos(u)
        y = (h if math.sin(u) < 0 else r0 * sy) * rr * math.sin(u)
        ajouter("point", tr([(x, y)], cx, cy, ang))


def bouton(cx, cy, r, ang=0.0):
    ajouter("disque", tr([(r * math.cos(u), r * 0.85 * math.sin(u)) for u in [i * math.pi / 10 for i in range(21)]], cx, cy, ang), True)
    for u in (-0.9, 0, 0.9):
        ajouter("fin", tr([(r * 0.9 * math.cos(math.pi / 2 + u), r * 0.8), (0, -r * 0.6)], cx, cy, ang))


def epi_lavande(base, dirdeg, longueur, f0=1.0):
    """Un epi de lavande : des verticilles de calices, espaces en bas, serres en haut, quelques corolles."""
    s, n = 0.0, 0
    a = math.radians(dirdeg)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    ajouter("trait", [base, (base[0] + ux * longueur, base[1] + uy * longueur)])
    while s < longueur:
        f = f0 * (1 - 0.55 * s / longueur)
        cx, cy = base[0] + ux * s, base[1] + uy * s
        for cote, decal in ((-1, 2.4), (1, 2.4), (0, 0)):
            ox, oy = cx + px * cote * decal * f, cy + py * cote * decal * f
            ang = dirdeg + cote * 28
            cal = [(4.6 * f * math.cos(u) / 2 + 2.3 * f, 1.35 * f * math.sin(u)) for u in [i * math.pi / 8 for i in range(17)]]
            ajouter("masse", tr(cal, ox, oy, ang), True)
            ajouter("fin", tr([(0.6 * f, 0), (3.8 * f, 0)], ox, oy, ang))
            if cote and n % 2 == 0 and s > longueur * 0.35:
                cor = [(4.6 * f + 1.6 * f * math.cos(u), 1.1 * f * math.sin(u)) for u in [i * math.pi / 6 for i in range(13)]]
                ajouter("petale", tr(cor, ox, oy, ang + cote * 30), True)
        s += 7.5 if s < longueur * 0.3 else 4.6
        n += 1
    bout = (base[0] + ux * (longueur + 3), base[1] + uy * (longueur + 3))
    ajouter("masse", tr([(3.2 * math.cos(u), 1.2 * math.sin(u)) for u in [i * math.pi / 8 for i in range(17)]], bout[0], bout[1], dirdeg), True)


def fleur_sauge(ox, oy, ang, f=1.0):
    """Une fleur de sauge a deux levres, vue de profil, dirigee vers +x."""
    calice = [(0, -1.4 * f), (4 * f, -2 * f), (5.2 * f, -0.4 * f), (4 * f, 1.4 * f), (0, 1.2 * f)]
    ajouter("masse", tr(calice, ox, oy, ang), True)
    casque = bez((4.5 * f, -1.4 * f), (6 * f, -6.5 * f), (11 * f, -6 * f), (12.5 * f, -2.2 * f), 12)
    casque += bez((12.5 * f, -2.2 * f), (10.5 * f, -2.6 * f), (7.5 * f, -1.6 * f), (5.2 * f, -0.2 * f), 8)[1:]
    ajouter("petale", tr(casque, ox, oy, ang), True)
    levre = bez((5.2 * f, 0.2 * f), (7.5 * f, 1.0 * f), (10 * f, 3.8 * f), (12.5 * f, 3.0 * f), 10)
    levre += bez((12.5 * f, 3.0 * f), (11 * f, 1.0 * f), (8.5 * f, 0.4 * f), (5.2 * f, 0.2 * f), 8)[1:]
    ajouter("petale", tr(levre, ox, oy, ang), True)


def epi_sauge(base, dirdeg, longueur):
    a = math.radians(dirdeg)
    ux, uy = math.cos(a), math.sin(a)
    ajouter("trait", [base, (base[0] + ux * longueur, base[1] + uy * longueur)])
    s = 0.0
    while s < longueur - 4:
        f = 1 - 0.45 * s / longueur
        cx, cy = base[0] + ux * s, base[1] + uy * s
        for cote in (-1, 1):
            fleur_sauge(cx, cy, dirdeg + cote * 62, f)
        s += 13 * f
    bouton(base[0] + ux * longueur, base[1] + uy * longueur, 2.4, dirdeg)


def nom(x, y, texte):
    TEXTES.append((x, y, texte))


# ---------- la planche ----------
SOL = 350


def camomille(x0, s=1.0):
    principale = tige((x0, SOL), (x0 + 3 * s, SOL - 60 * s), (x0 - 10 * s, SOL - 140 * s), (x0 - 6 * s, SOL - 205 * s))
    racines(x0, SOL)
    tetes = [principale[-1]]
    for t, dx, dy in ((0.40, -48, -232), (0.58, 44, -258), (0.30, 70, -195)):
        p, _ = le_long(principale, t)
        bout = (x0 + dx * s, SOL + dy * s)
        tige(p, (p[0] + (bout[0] - p[0]) * 0.2, p[1] - 20 * s), (bout[0] - (bout[0] - p[0]) * 0.15, bout[1] + 25 * s), bout, "branche")
        tetes.append(bout)
    for t, cote in ((0.12, -1), (0.2, 1), (0.33, -1), (0.47, 1), (0.6, -1), (0.75, 1)):
        p, d = le_long(principale, t)
        feuille_fine(p[0], p[1], d + cote * 52, (40 - 18 * t) * s, cote)
    feuille_fine(x0, SOL - 4, -150, 44 * s, 1)
    feuille_fine(x0, SOL - 4, -30, 42 * s, -1)
    for i, (hx, hy) in enumerate(tetes):
        f = (1.0, 0.92, 1.05, 0.78)[i] * s
        capitule(hx, hy - 5 * f, 6.2 * f, 17 * f, 16, 3.8 * f, sy=0.5, ang=R.uniform(-8, 8), retombe=3.2 * f, dome=1.0)
    p, _ = le_long(principale, 0.52)
    b = (x0 - 30 * s, SOL - 162 * s)
    tige(p, (p[0] - 8 * s, p[1] - 8 * s), (b[0] + 6 * s, b[1] + 10 * s), b, "branche")
    bouton(b[0], b[1] - 2, 3.4 * s, -100)
    nom(x0, 372, "Matricaria chamomilla")


def lavande(x0):
    racines(x0, SOL, 6)
    for ang, L in ((-150, 46), (-138, 40), (-125, 50), (-112, 36), (-68, 38), (-55, 50), (-42, 42), (-30, 46), (-95, 30), (-82, 34)):
        feuille(x0, SOL - 2, ang, L, 2.4, "lance", courbe=R.uniform(-0.12, 0.12), nerv=None)
    for dx, haut, pli in ((-62, 222, -10), (-34, 250, -6), (-8, 268, 2), (18, 258, 8), (44, 236, 10), (68, 205, 14)):
        bout = (x0 + dx, SOL - haut)
        pts = tige((x0 + dx * 0.05, SOL - 4), (x0 + dx * 0.2, SOL - haut * 0.4), (bout[0] - pli, bout[1] + haut * 0.3), bout)
        if abs(dx) > 30:   # une paire de petites feuilles, la ou les tiges se sont ecartees
            p, d = le_long(pts, 0.55)
            for cote in (-1, 1):
                feuille(p[0], p[1], d + cote * 34, 15, 1.7, "lance", courbe=cote * 0.05, nerv=None)
        _, d = le_long(pts, 0.99)
        epi_lavande(bout, d, 50 + (haut - 200) * 0.25, 1.0)
    nom(x0, 372, "Lavandula angustifolia")


def sauge(x0):
    racines(x0, SOL, 6)
    ajouter("tige", [(x0 - 2, SOL), (x0 - 1, SOL - 22)])
    ajouter("tige", [(x0 + 2, SOL), (x0 + 1, SOL - 22)])
    centre = tige((x0, SOL - 22), (x0 + 4, SOL - 110), (x0 - 2, SOL - 190), (x0 + 4, SOL - 238))
    gauche = tige((x0, SOL - 26), (x0 - 20, SOL - 70), (x0 - 52, SOL - 120), (x0 - 64, SOL - 168))
    droite = tige((x0, SOL - 30), (x0 + 24, SOL - 72), (x0 + 50, SOL - 112), (x0 + 66, SOL - 156))
    for pts, noeuds, L0 in ((centre, (0.3, 0.5, 0.7), 50), (gauche, (0.5, 0.88), 44), (droite, (0.46, 0.86), 46)):
        for i, t in enumerate(noeuds):
            p, d = le_long(pts, t)
            for cote in (-1, 1):
                L = L0 - i * 6 + R.uniform(-3, 3)
                feuille(p[0], p[1], d + cote * 64, L, L * 0.25, "oblong", creneaux=0.07, nb_cren=14,
                        courbe=cote * 0.07, nv=6, petiole=5)
    for pts in (gauche, droite):
        p, d = le_long(pts, 0.99)
        feuille(p[0], p[1], d - 12, 24, 6, "oblong", creneaux=0.07, nv=4, hachures=False)
        feuille(p[0], p[1], d + 14, 22, 5.6, "oblong", creneaux=0.07, nv=4, hachures=False)
    _, d = le_long(centre, 0.99)
    epi_sauge(centre[-1], d, 70)
    nom(x0, 372, "Salvia officinalis")


def arnica(x0):
    racines(x0, SOL, 6)
    for ang, L, cb in ((200, 60, -0.1), (162, 50, 0.12), (-20, 58, 0.1), (18, 48, -0.12), (232, 38, -0.06), (-52, 40, 0.06)):
        feuille(x0, SOL - 4, ang, L, L * 0.26, "arnica", courbe=cb, nerv="paralleles")
    principale = tige((x0, SOL - 6), (x0 + 6, SOL - 90), (x0 - 4, SOL - 170), (x0 + 8, SOL - 240))
    p, d = le_long(principale, 0.42)
    for cote in (-1, 1):
        feuille(p[0], p[1], d + cote * 58, 30, 8, "arnica", courbe=cote * 0.1, nerv="paralleles", hachures=False)
    capitule(x0 + 9, SOL - 252, 8.2, 31, 13, 6, sy=0.8, ang=-8, retombe=2.5, dents=True, desordre=0.13, dome=0.45)
    p, _ = le_long(principale, 0.62)
    b = (x0 + 52, SOL - 202)
    tige(p, (p[0] + 12, p[1] - 4), (b[0] - 12, b[1] + 16), b, "branche")
    capitule(b[0], b[1] - 4, 5, 17, 12, 4, sy=0.55, ang=14, retombe=3, dents=True, desordre=0.15, dome=0.5)
    p, _ = le_long(principale, 0.5)
    b = (x0 - 34, SOL - 172)
    tige(p, (p[0] - 8, p[1] - 6), (b[0] + 8, b[1] + 12), b, "branche")
    bouton(b[0], b[1] - 2, 4.2, -110)
    nom(x0, 372, "Arnica montana")


def planche():
    camomille(112)
    lavande(345)
    sauge(585)
    arnica(820)
    # ce qui est pose a cote, comme sur une planche : de quoi remplir le ciel
    capitule(232, 58, 6.4, 16, 17, 3.6, sy=1.0, dome=0.0)               # une camomille vue de dessus
    capitule(268, 112, 4.2, 10.5, 14, 2.6, sy=0.62, ang=-18, retombe=2.2)
    feuille_fine(212, 196, -62, 46, 1)
    feuille(452, 92, 28, 50, 13, "oblong", creneaux=0.07, nb_cren=14, nv=6, petiole=6)   # une feuille de sauge
    feuille(492, 196, -118, 42, 11, "oblong", creneaux=0.07, nb_cren=12, nv=5, petiole=5)
    epi_lavande((468, 300), -72, 44)                                      # un epi de lavande seul
    capitule(706, 62, 6.6, 22, 13, 5, sy=0.95, ang=10, dents=True, desordre=0.12, dome=0.2)   # une arnica de dessus
    feuille(690, 160, -96, 52, 14, "arnica", courbe=0.08, nerv="paralleles")
    epi_lavande((930, 196), -96, 56)
    feuille(16, 132, -74, 46, 12, "oblong", creneaux=0.07, nb_cren=13, nv=5, petiole=5)
    capitule(40, 52, 5, 12.5, 15, 3, sy=0.7, ang=12, retombe=1.5)
    capitule(872, 46, 4.6, 11.5, 14, 2.8, sy=0.9, ang=-6, dome=0.2)
    feuille_fine(896, 120, -118, 40, -1)


# ---------- sortie ----------
STYLES = {
    # sorte : (fond, opacite du fond, trait, epaisseur, opacite du trait)
    "jour": {"tige": (None, 0, "#FFFFFF", 1.15, 0.92), "branche": (None, 0, "#FFFFFF", 0.85, 0.92),
             "masse": ("#CCD7E0", 0.62, "#FFFFFF", 0.7, 0.95), "fil": (None, 0, "#FFFFFF", 0.62, 0.92),
             "trait": (None, 0, "#FFFFFF", 0.5, 0.9), "fin": (None, 0, "#FFFFFF", 0.38, 0.75),
             "petale": ("#FFFFFF", 0.78, "#FFFFFF", 0.6, 1.0), "disque": ("#E3EAF0", 0.9, "#FFFFFF", 0.6, 1.0),
             "point": ("#9FB3C2", 1.0, None, 0, 0), "texte": ("#FFFFFF", 0.92, None, 0, 0)},
    "nuit": {"tige": (None, 0, "#56708A", 1.15, 0.9), "branche": (None, 0, "#56708A", 0.85, 0.9),
             "masse": ("#29404F", 0.95, "#4F6A80", 0.7, 0.95), "fil": (None, 0, "#56708A", 0.62, 0.9),
             "trait": (None, 0, "#4A6378", 0.5, 0.9), "fin": (None, 0, "#41586B", 0.38, 0.85),
             "petale": ("#38505F", 0.95, "#5E7990", 0.6, 1.0), "disque": ("#34495B", 1.0, "#5E7990", 0.6, 1.0),
             "point": ("#5E7990", 1.0, None, 0, 0), "texte": ("#5E7990", 0.95, None, 0, 0)},
    "filigrane": {"tige": (None, 0, "#FFFFFF", 1.15, 0.6), "branche": (None, 0, "#FFFFFF", 0.85, 0.6),
                  "masse": ("#FFF39A", 0.4, "#FFFFFF", 0.75, 0.6), "fil": (None, 0, "#FFFFFF", 0.62, 0.6),
                  "trait": (None, 0, "#FFFFFF", 0.5, 0.55), "fin": (None, 0, "#FFFFFF", 0.38, 0.45),
                  "petale": ("#FFFCD4", 0.5, "#FFFFFF", 0.6, 0.65), "disque": ("#FFEE78", 0.45, "#FFFFFF", 0.6, 0.6),
                  "point": ("#FFFFFF", 0.5, None, 0, 0), "texte": ("#FFFFFF", 0.6, None, 0, 0)},
}
ORDRE = ("tige", "branche", "masse", "fil", "fin", "trait", "petale", "disque", "point")
POLICE = "Georgia, 'Noto Serif', 'Times New Roman', serif"


def chemin(pts, ferme):
    """M absolu puis l relatifs, au dixieme : le fichier de la carte du monde pese 151 ko, celui-ci doit rester pres."""
    x0, y0 = round(pts[0][0], 1), round(pts[0][1], 1)
    d, morceaux = "M%g,%g" % (x0, y0), []
    for x, y in pts[1:]:
        x, y = round(x, 1), round(y, 1)
        dx, dy = round(x - x0, 1), round(y - y0, 1)
        if dx or dy:
            morceaux.append(("%g" % dx) + ("," if dy >= 0 else "") + ("%g" % dy))
        x0, y0 = x, y
    return d + ("l" + " ".join(morceaux) if morceaux else "") + ("z" if ferme else "")


def svg(style):
    st = STYLES[style]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">' % (L_TUILE, H_TUILE)]
    for sorte in ORDRE:
        els = [x for x in ELEMENTS if x[0] == sorte]
        if not els:
            continue
        fond, of, trait, ep, ot = st[sorte]
        if sorte == "point":
            d = "".join("M%.1f,%.1fa.55,.55 0 1,0 1.1,0a.55,.55 0 1,0 -1.1,0" % (p[0][0] - 0.55, p[0][1]) for _, p, _ in els)
            parts.append('<path d="%s" fill="%s" fill-opacity="%s"/>' % (d, fond, of))
            continue
        d = "".join(chemin(p, f) for _, p, f in els)
        attrs = 'fill="%s"' % fond if fond else 'fill="none"'
        if fond:
            attrs += ' fill-opacity="%s"' % of
        attrs += ' stroke="%s" stroke-width="%s" stroke-opacity="%s" stroke-linejoin="round" stroke-linecap="round"' % (trait, ep, ot)
        parts.append('<path d="%s" %s/>' % (d, attrs))
    fond, of = st["texte"][:2]
    for x, y, t in TEXTES:
        parts.append('<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-style="italic" font-size="11" '
                     'letter-spacing=".4" fill="%s" fill-opacity="%s">%s</text>' % (x, y, POLICE, fond, of, t))
    parts.append("</svg>")
    return "".join(parts)


def apercu(style, chemin_png):
    """Le meme dessin rendu par Pillow (trois fois plus grand puis reduit), sur le ciel de l'app : pour juger sans navigateur."""
    from PIL import Image, ImageDraw, ImageFont
    k = 3
    W, H = L_TUILE * k, H_TUILE * k
    if style == "jour":
        ciel = Image.new("RGBA", (W, H))
        dc = ImageDraw.Draw(ciel)
        for y in range(H):
            f = y / H
            c = [int(a + (b - a) * f) for a, b in zip((0x6C, 0x9B, 0xD0), (0x8D, 0xB4, 0xDF))]
            dc.line([(0, y), (W, y)], fill=tuple(c) + (255,))
    elif style == "nuit":
        ciel = Image.new("RGBA", (W, H), (0x0E, 0x1C, 0x26, 255))
    else:
        ciel = Image.new("RGBA", (W, H), (0xF4, 0xA0, 0x4C, 255))
    st = STYLES[style]

    def rgba(h, o):
        return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (int(255 * o),)

    for sorte in ORDRE:
        fond, of, trait, ep, ot = st[sorte]
        calque = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dc = ImageDraw.Draw(calque)
        for _, pts, ferme in (x for x in ELEMENTS if x[0] == sorte):
            P = [(x * k, y * k) for x, y in pts]
            if sorte == "point":
                x, y = P[0]
                dc.ellipse([x - 0.55 * k, y - 0.55 * k, x + 0.55 * k, y + 0.55 * k], fill=rgba(fond, 1))
                continue
            if fond and len(P) > 2:
                dc.polygon(P, fill=rgba(fond, 1))
        if fond:
            a = calque.getchannel("A").point(lambda v: int(v * of))
            calque.putalpha(a)
            ciel = Image.alpha_composite(ciel, calque)
        if trait:
            calque = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            dc = ImageDraw.Draw(calque)
            for _, pts, ferme in (x for x in ELEMENTS if x[0] == sorte):
                P = [(x * k, y * k) for x, y in pts] + ([(pts[0][0] * k, pts[0][1] * k)] if ferme else [])
                if len(P) > 1:
                    dc.line(P, fill=rgba(trait, 1), width=max(1, round(ep * k)), joint="curve")
            a = calque.getchannel("A").point(lambda v: int(v * ot))
            calque.putalpha(a)
            ciel = Image.alpha_composite(ciel, calque)
    police = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 11 * k)
    dc = ImageDraw.Draw(ciel)
    fond, of = st["texte"][:2]
    for x, y, t in TEXTES:
        dc.text((x * k, y * k), t, font=police, fill=rgba(fond, of), anchor="ms")
    ciel.resize((L_TUILE * 2, H_TUILE * 2), Image.LANCZOS).save(chemin_png)


def main():
    planche()
    for style in ("jour", "nuit", "filigrane"):
        s = svg(style)
        with open(os.path.join(ICI, "herbier-%s.svg" % style), "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
        print("herbier-%s.svg : %d octets, %d elements" % (style, len(s), len(ELEMENTS)))
    if "--apercu" in sys.argv:
        dossier = sys.argv[sys.argv.index("--apercu") + 1]
        os.makedirs(dossier, exist_ok=True)
        for style in ("jour", "nuit", "filigrane"):
            apercu(style, os.path.join(dossier, "herbier-%s.png" % style))
        print("apercus dans", dossier)


if __name__ == "__main__":
    main()
