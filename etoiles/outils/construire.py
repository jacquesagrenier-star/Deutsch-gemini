# -*- coding: utf-8 -*-
"""Construit etoiles/ciel.json, le fichier que lit la fete de la nouvelle etoile (seance legere, essai admin).

    python etoiles/outils/construire.py

Fichier DERIVE : on corrige figures.py (les figures, les noms, la phrase de la distance) ou on refait les
releves de sources/ ; jamais ciel.json a la main.

Sources (sources/, reproduits tels que SIMBAD les a rendus le 7 nov. 2026, miroir de Harvard) :
- simbad_positions.txt : ascension droite et declinaison (ICRS, J2000), magnitudes B et V ;
- simbad_parallaxes.txt : la parallaxe, son erreur et sa reference (Hipparcos, van Leeuwen 2007 ; Gaia EDR3 ;
  Gaia DR2). alf01 Cru n'en a pas : la ligne suivante est celle du systeme alf Cru.

Ce qu'on en tire :
- la figure en projection gnomonique, l'est a gauche comme sur une carte du ciel, posee dans une boite de
  375 x 372 px (l'ecran de la fete, mis a l'echelle par l'app) ;
- le rayon d'une etoile selon sa magnitude (aire proportionnelle au flux, avec un plancher), son eclat, une
  teinte a peine perceptible selon B-V ;
- la distance en annees-lumiere = 1000 / parallaxe (mas) x 3,2616 ; affichee a l'entier, a la centaine
  au-dela de 1 000 (« environ »), a la dizaine quand l'erreur de la parallaxe depasse 10 % (« environ »)."""
import json, math, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, ICI)
from figures import DESIGNATIONS, V_USUELLE, FIGURES, GROUPES, TEXTES_DISTANCE

AL_PAR_PC = 3.261563777
BOITE = (375, 372)
MARGE = 46
CATALOGUES = {
    "2007A&A...474..653V": "Hipparcos, nouvelle réduction (van Leeuwen 2007, A&A 474, 653)",
    "2020yCat.1350....0G": "Gaia EDR3 (Gaia Collaboration 2020, VizieR I/350)",
    "2018yCat.1345....0G": "Gaia DR2 (Gaia Collaboration 2018, VizieR I/345)",
}


def lignes(nom):
    out = []
    for l in open(os.path.join(RACINE, "sources", nom), encoding="utf-8"):
        if l.startswith("*"):
            out.append([" ".join(c.split()) for c in l[1:].strip().split("|")])
    return out


def lire():
    pos = lignes("simbad_positions.txt")
    plx = lignes("simbad_parallaxes.txt")
    # alf01 Cru, sans parallaxe : on prend la ligne du systeme qui la suit
    p2, i = [], 0
    while i < len(plx):
        if plx[i][0] == "alf01 Cru":
            p2.append(["alf01 Cru", plx[i + 1][1]]); i += 2; continue
        p2.append(plx[i]); i += 1
    assert len(pos) == len(p2) == len(DESIGNATIONS), (len(pos), len(p2), len(DESIGNATIONS))
    etoiles = {}
    for (nom, des), lp, lx in zip(DESIGNATIONS, pos, p2):
        ra, de = (float(v) for v in lp[1].split())
        b = float(lp[2]) if lp[2] else None
        v = float(lp[3]) if lp[3] else None
        val, err, qual, bib = lx[1].split()[:4]
        etoiles[nom] = dict(designation=des, simbad=lp[0], ra=ra, de=de, B=b, V=v if v is not None else V_USUELLE[nom],
                            v_usuelle=v is None, plx=float(val), err=float(err), ref=bib)
    return etoiles


def projeter(E, noms):
    vx = vy = vz = 0
    for n in noms:
        a, d = math.radians(E[n]["ra"]), math.radians(E[n]["de"])
        vx += math.cos(d) * math.cos(a); vy += math.cos(d) * math.sin(a); vz += math.sin(d)
    a0 = math.atan2(vy, vx); d0 = math.atan2(vz, math.hypot(vx, vy))
    pts = []
    for n in noms:
        a, d = math.radians(E[n]["ra"]), math.radians(E[n]["de"])
        da = a - a0
        cc = math.sin(d0) * math.sin(d) + math.cos(d0) * math.cos(d) * math.cos(da)
        x = math.cos(d) * math.sin(da) / cc
        y = (math.cos(d0) * math.sin(d) - math.sin(d0) * math.cos(d) * math.cos(da)) / cc
        pts.append((-x, -y))
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    s = min((BOITE[0] - 2 * MARGE) / (max(xs) - min(xs)), (BOITE[1] - 2 * MARGE) / (max(ys) - min(ys)))
    ox = BOITE[0] / 2 - (max(xs) + min(xs)) / 2 * s
    oy = BOITE[1] / 2 - (max(ys) + min(ys)) / 2 * s
    return [(round(ox + x * s, 1), round(oy + y * s, 1)) for x, y in pts]


def rayon(mag, mmin, r_max=6.6, r_min=2.3):
    return max(r_min, r_max * 10 ** (-0.2 * (mag - mmin)))


def luminosite(mag, mmin):
    return max(.55, 10 ** (-0.12 * (mag - mmin)))


def _mix(a, b, t):
    a = [int(a[i:i + 2], 16) for i in (1, 3, 5)]; b = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join("%02X" % round(x * (1 - t) + y * t) for x, y in zip(a, b))


def teinte(bv, base="#FFF6E2", force=.38):
    if bv is None:
        return base
    if bv < 0.3:
        return _mix(base, "#BFD3FF", force * min(1, (0.3 - bv) / 0.5))
    if bv > 0.7:
        return _mix(base, "#FFB774", force * min(1, (bv - 0.7) / 1.1))
    return base


def distance(e):
    al = 1000.0 / e["plx"] * AL_PAR_PC
    rel = e["err"] / e["plx"]
    if al >= 1000:
        return al, int(round(al / 100.0)) * 100, True
    if rel > 0.10:
        return al, int(round(al / 10.0)) * 10, True
    return al, int(round(al)), False


def construire():
    E = lire()
    cons = {}
    for cle, f in FIGURES.items():
        P = projeter(E, f["et"])
        mmin = min(E[n]["V"] for n in f["et"])
        et = []
        for n, (x, y) in zip(f["et"], P):
            e = E[n]
            bv = (e["B"] - e["V"]) if (e["B"] is not None and not e["v_usuelle"]) else None
            al, aff, env = distance(e)
            et.append(dict(nom=n, x=x, y=y, r=round(rayon(e["V"], mmin), 2), lum=round(luminosite(e["V"], mmin), 2),
                           couleur=teinte(bv), al=round(al, 1), affiche=aff, environ=env,
                           source=dict(simbad=e["simbad"], ra=e["ra"], de=e["de"], V=e["V"], B=e["B"],
                                       parallaxe_mas=e["plx"], erreur_mas=e["err"], reference=e["ref"],
                                       catalogue=CATALOGUES[e["ref"]], v_usuelle=e["v_usuelle"])))
        cons[cle] = dict(noms=f["noms"], traits=[list(t) for t in f["tr"]], etoiles=et)
    data = {
        "_lisez_moi": [
            "Les constellations de la séance légère : une étoile par étape, dans l'ordre des étapes (essai admin seance_legere).",
            "Fichier DÉRIVÉ : python etoiles/outils/construire.py. Les figures et les textes sont dans etoiles/outils/figures.py, "
            "les mesures dans etoiles/sources/ (SIMBAD, CDS Strasbourg, relevé du 7 nov. 2026).",
            "x, y : la position dans une boîte de 375 x 372 px ; r : le rayon du cœur de l'étoile ; lum : son éclat (0,55 à 1) ; "
            "couleur : sa teinte selon B-V. al : la distance en années-lumière ; affiche : ce qu'on écrit ; environ : arrondie.",
            "Chaque étoile garde sa source : la désignation SIMBAD, la parallaxe, son erreur et sa référence.",
        ],
        "boite": list(BOITE),
        "groupes": GROUPES,
        "textes_distance": TEXTES_DISTANCE,
        "constellations": cons,
    }
    sortie = os.path.join(RACINE, "ciel.json")
    open(sortie, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print("ecrit", sortie, os.path.getsize(sortie), "octets,", sum(len(c["etoiles"]) for c in cons.values()), "etoiles")
    return data


if __name__ == "__main__":
    d = construire()
    for c in ("gemeaux", "orion", "ourse"):
        print(c, [(e["nom"], e["affiche"], e["environ"]) for e in d["constellations"][c]["etoiles"]])
