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
import json, math, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, ICI)
from figures import DESIGNATIONS, V_USUELLE, FIGURES, GROUPES, TEXTES_DISTANCE, noms_sans_nom
from voyage import (VOYAGE, ORDRE_EXISTANT, NOMS_EXISTANTES, GENITIFS_VOYAGE, LETTRES_VOYAGE, USAGE_VOYAGE,
                    PARALLAXE_DU_SYSTEME, V_DU_BSC, ENVIRON_SI_ECART)

AL_PAR_PC = 3.261563777
BOITE = (375, 372)
MARGE = 46
CATALOGUES = {
    "2007A&A...474..653V": "Hipparcos, nouvelle réduction (van Leeuwen 2007, A&A 474, 653)",
    "2020yCat.1350....0G": "Gaia EDR3 (Gaia Collaboration 2020, VizieR I/350)",
    "2018yCat.1345....0G": "Gaia DR2 (Gaia Collaboration 2018, VizieR I/345)",
    "1997A&A...323L..49P": "Hipparcos (Perryman et al. 1997, A&A 323, L49)",
}
HIPPARCOS_2007 = "2007A&A...474..653V"
GAIA = ("2020yCat.1350....0G", "2018yCat.1345....0G")


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


# ------------------------------------------------------------------------------------------------------------------
# LE VOYAGE JUSQU'AU C1 (voyage.py, 11 nov. 2026) : les 42 figures qui suivent les 15 premieres. Memes calculs
# (projection, rayon, eclat, teinte, distance) ; trois ajouts, propres a ces figures :
# - le nom propre vient de la liste officielle de l'UAI (sources/IAU-CSN.txt), par numero Hipparcos, a defaut par
#   la lettre et la constellation ; sinon la lettre grecque et la constellation dans chaque langue d'interface ;
# - une magnitude V absente de SIMBAD vient du Yale Bright Star Catalogue (sources/bsc5_extrait.txt) ;
# - la distance passe en « environ » (a la dizaine) quand Hipparcos 2007 et Gaia, tous deux connus de SIMBAD
#   (sources/simbad_voyage_parallaxes.tsv), donnent des distances qui different de plus de 10 % : pour les etoiles
#   brillantes, les deux catalogues se contredisent souvent au-dela de leurs erreurs annoncees.
LETTRES_COURTES = {"alf": "alf", "bet": "bet", "gam": "gam", "del": "del_", "eps": "eps", "zet": "zet", "eta": "eta",
                   "tet": "tet", "iot": "iot", "kap": "kap", "lam": "lam", "mu.": "mu", "nu.": "nu", "ksi": "ksi",
                   "omi": "omi", "pi.": "pi", "rho": "rho", "sig": "sig", "tau": "tau", "ups": "ups", "phi": "phi",
                   "chi": "chi", "psi": "psi", "ome": "ome"}
EXPOSANTS = {"1": "¹", "2": "²", "3": "³", "4": "⁴"}


def lettre_de(designation):
    """« gam01 Leo » -> ("gam", "1", "Leo") ; None pour une etoile sans lettre grecque (« 41 Ari »)."""
    t = designation.split()
    tete = t[0]
    for court in LETTRES_COURTES:
        if tete.startswith(court):
            reste = tete[len(court):]
            if reste == "" or reste.isdigit():
                return court, str(int(reste)) if reste else "", t[1]
    return None


def lire_csn():
    """La liste de l'UAI : par numero Hipparcos et par (lettre, constellation)."""
    par_hip, par_lettre = {}, {}
    for l in open(os.path.join(RACINE, "sources", "IAU-CSN.txt"), encoding="utf-8"):
        if l.startswith(("#", "$")) or len(l) < 80:
            continue
        nom = l[18:36].strip()
        ident, con = l[49:55].strip(), l[61:65].strip()
        reste = l[70:].split()
        hip = reste[3] if len(reste) > 3 else "_"
        if hip.isdigit():
            par_hip.setdefault(int(hip), nom)
        if ident != "_":
            par_lettre.setdefault((ident, con), nom)
    return par_hip, par_lettre


def lire_bsc():
    out = {}
    for l in open(os.path.join(RACINE, "sources", "bsc5_extrait.txt"), encoding="utf-8"):
        if l.startswith("#"):
            continue
        bv = l[109:114].strip()
        out[int(l[:4])] = (float(l[102:107]), float(bv) if bv else None)
    return out


def lire_mesures():
    out = {}
    for l in open(os.path.join(RACINE, "sources", "simbad_voyage_parallaxes.tsv"), encoding="utf-8"):
        if l.startswith(("#", "id\t")):
            continue
        i, p, e, b = l.rstrip("\n").split("\t")
        if p and e:
            out.setdefault(" ".join(i.strip('"')[1:].split()), {})[b.strip('"')] = (float(p), float(e))
    return out


def lire_voyage():
    txt = open(os.path.join(RACINE, "sources", "simbad_voyage.txt"), encoding="utf-8").read()
    ids = txt.split("# Identifiants demandes : ")[1].split("\n")[0].split(" ; ")
    lig = [[" ".join(c.split()) for c in l[1:].strip().split("|")] for l in txt.splitlines() if l.startswith("*")]
    assert len(ids) == len(lig), (len(ids), len(lig))
    brut = dict(zip(ids, lig))
    bsc, mes = lire_bsc(), lire_mesures()
    par_hip, par_lettre = lire_csn()
    E = {}
    for d, (main, coo, b, v, plx, hip, hr) in brut.items():
        if d in PARALLAXE_DU_SYSTEME.values() and d not in [x for f in VOYAGE for x in f["et"]]:
            continue
        ra, de = (float(x) for x in coo.split())
        B = float(b) if b else None
        V = float(v) if v else None
        bv, v_bsc = (B - V) if (B is not None and V is not None) else None, None
        if V is None:
            hrs = V_DU_BSC[d]
            V = -2.5 * math.log10(sum(10 ** (-0.4 * bsc[h][0]) for h in hrs))
            bv = bsc[min(hrs, key=lambda h: bsc[h][0])][1]
            v_bsc = ["HR %d" % h for h in hrs]
        source_plx = d
        if plx.startswith("~"):
            source_plx = PARALLAXE_DU_SYSTEME[d]
            plx = brut[source_plx][4]
            hip = hip or brut[source_plx][5]
        val, err, qual, bib = plx.split()[:4]
        hipn = int(re.match(r"HIP (\d+)", hip).group(1)) if hip else None
        lt = lettre_de(d)
        csn = par_hip.get(hipn) if hipn else None
        if not csn and lt:
            csn = par_lettre.get(((lt[0] if lt[0][-1] != "." else lt[0][:-1]) + (lt[1].zfill(2) if lt[1] else ""), lt[2]))
        if not csn and d.split()[0].isdigit():
            csn = par_lettre.get((d.split()[0], d.split()[1]))
        m = mes.get(" ".join(source_plx.split()), {})
        cg = next((x for x in GAIA if x in m), None)
        h, g = m.get(HIPPARCOS_2007), m.get(cg) if cg else None
        ecart = abs(h[0] - g[0]) / max(h[0], g[0]) if (h and g) else None
        val, err, choix = float(val), float(err), None
        if ecart is not None and ecart > ENVIRON_SI_ECART:
            # les deux catalogues se contredisent : la mesure la plus precise des deux (erreur relative la plus faible)
            (val, err), bib = min(((h, HIPPARCOS_2007), (g, cg)), key=lambda x: x[0][1] / x[0][0])
            choix = "la plus précise de Hipparcos 2007 et de Gaia, qui diffèrent de %d %%" % round(ecart * 100)
        E[d] = dict(simbad=main, ra=ra, de=de, B=B, V=round(V, 2), bv=bv, v_bsc=v_bsc, plx=val, err=err,
                    ref=bib, hip=hipn, nom_uai=csn, lettre=lt, systeme=source_plx if source_plx != d else None,
                    hipparcos=h, gaia=g, ecart=ecart, choix=choix)
    return E


def noms_voyage(lt):
    """Une etoile sans nom propre : la lettre grecque (et son exposant) et la constellation, par langue d'interface."""
    court, exp, con = lt
    gen = GENITIFS_VOYAGE[con]
    return {lg: LETTRES_VOYAGE[l][LETTRES_COURTES[court]] + "".join(EXPOSANTS[c] for c in exp) + " " + gen[g]
            for lg, (l, g) in USAGE_VOYAGE.items()}


def nom_court(d, lt):
    """Le nom de secours d'une etoile sans nom propre, a la maniere de figures.py (« eta Leo », « delta1 Gru »)."""
    return LETTRES_VOYAGE["latin"][LETTRES_COURTES[lt[0]]].lower() + lt[1] + " " + lt[2]


def distance_voyage(e):
    al, aff, env = distance(e)
    if not env and e["ecart"] is not None and e["ecart"] > ENVIRON_SI_ECART:
        return al, int(round(al / 10.0)) * 10, True
    return al, aff, env


def construire_voyage():
    E = lire_voyage()
    cons = {}
    for f in VOYAGE:
        P = projeter(E, f["et"])
        mmin = min(E[n]["V"] for n in f["et"])
        et = []
        for n, (x, y) in zip(f["et"], P):
            e = E[n]
            al, aff, env = distance_voyage(e)
            if e["nom_uai"]:
                nom, extra = e["nom_uai"], {}
            else:
                assert e["lettre"], "etoile sans nom propre ni lettre grecque : " + n
                nom, extra = nom_court(n, e["lettre"]), dict(noms=noms_voyage(e["lettre"]))
            src = dict(simbad=e["simbad"], ra=e["ra"], de=e["de"], V=e["V"], B=e["B"], parallaxe_mas=e["plx"],
                       erreur_mas=e["err"], reference=e["ref"], catalogue=CATALOGUES[e["ref"]], v_usuelle=False)
            if e["hip"]:
                src["hip"] = e["hip"]
            if e["v_bsc"]:
                src["v_bsc"] = e["v_bsc"]
            if e["systeme"]:
                src["parallaxe_du_systeme"] = e["systeme"]
            if e["hipparcos"] and e["gaia"]:
                src["hipparcos_2007_mas"] = e["hipparcos"][0]
                src["gaia_mas"] = e["gaia"][0]
            if e["choix"]:
                src["parallaxe_retenue"] = e["choix"]
            if e["nom_uai"]:
                src["nom"] = "UAI, IAU Catalog of Star Names (WGSN)"
            et.append(dict(nom=nom, **extra, x=x, y=y, r=round(rayon(e["V"], mmin), 2),
                           lum=round(luminosite(e["V"], mmin), 2), couleur=teinte(e["bv"]), al=round(al, 1),
                           affiche=aff, environ=env, source=src))
        cons[f["cle"]] = dict(noms=f["noms"], traits=[list(t) for t in f["tr"]], etoiles=et)
    return cons


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
            ns = noms_sans_nom(n)
            if ns:
                extra = dict(noms=ns)
            else:
                extra = {}
            et.append(dict(nom=n, **extra, x=x, y=y, r=round(rayon(e["V"], mmin), 2), lum=round(luminosite(e["V"], mmin), 2),
                           couleur=teinte(bv), al=round(al, 1), affiche=aff, environ=env,
                           source=dict(simbad=e["simbad"], ra=e["ra"], de=e["de"], V=e["V"], B=e["B"],
                                       parallaxe_mas=e["plx"], erreur_mas=e["err"], reference=e["ref"],
                                       catalogue=CATALOGUES[e["ref"]], v_usuelle=e["v_usuelle"])))
        noms = dict(f["noms"])
        for lg, v in NOMS_EXISTANTES.get(cle, {}).items():
            noms.setdefault(lg, v)
        cons[cle] = dict(noms=noms, traits=[list(t) for t in f["tr"]], etoiles=et)
    assert list(cons) == ORDRE_EXISTANT, list(cons)
    nouvelles = construire_voyage()
    assert not set(nouvelles) & set(cons)
    cons.update(nouvelles)
    data = {
        "_lisez_moi": [
            "Les constellations de la séance légère : une étoile par étape, dans l'ordre des étapes (essai admin seance_legere).",
            "Fichier DÉRIVÉ : python etoiles/outils/construire.py. Les figures et les textes sont dans etoiles/outils/figures.py, "
            "les mesures dans etoiles/sources/ (SIMBAD, CDS Strasbourg, relevé du 7 nov. 2026).",
            "x, y : la position dans une boîte de 375 x 372 px ; r : le rayon du cœur de l'étoile ; lum : son éclat (0,55 à 1) ; "
            "couleur : sa teinte selon B-V. al : la distance en années-lumière ; affiche : ce qu'on écrit ; environ : arrondie.",
            "noms : le nom affiché d'une étoile sans nom propre, par langue d'interface (« Tau des Gémeaux », « Tau Geminorum »).",
            "La source de chaque étoile (désignation SIMBAD, parallaxe, erreur, référence) est dans etoiles/sources-etoiles.json, "
            "que seuls les outils lisent (même ordre que les étoiles de chaque constellation) : ciel.json reste léger.",
            "ordre : le voyage jusqu'au C1 (décision du 11 nov. 2026), une étoile par séance terminée, constellation après "
            "constellation : les 15 premières (etoiles/outils/figures.py), puis les 42 de etoiles/outils/voyage.py. "
            "Leurs mesures : etoiles/sources/simbad_voyage*.txt ; leurs noms propres : la liste de l'UAI (IAU-CSN.txt).",
            "Les noms des figures : fr, de, es, en, pt, ja, tr, pl, ru, uk, ar, fa. Crédits : etoiles/CREDITS.md.",
        ],
        "boite": list(BOITE),
        "ordre": list(cons),
        "groupes": GROUPES,
        "textes_distance": TEXTES_DISTANCE,
        "constellations": cons,
    }
    # Les sources a part (chef, 11 nov. 2026) : l'app charge ciel.json, elle ne lit jamais « source ».
    sources = {"_lisez_moi": "La source de chaque étoile de ciel.json, constellation par constellation, dans l'ordre de ses "
                             "étoiles. Fichier DÉRIVÉ : python etoiles/outils/construire.py. Lu par les outils, jamais par l'app.",
               "constellations": {k: [e.pop("source") for e in c["etoiles"]] for k, c in cons.items()}}
    open(os.path.join(RACINE, "sources-etoiles.json"), "w", encoding="utf-8").write(
        json.dumps(sources, ensure_ascii=False, separators=(",", ":")))
    sortie = os.path.join(RACINE, "ciel.json")
    open(sortie, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print("ecrit", sortie, os.path.getsize(sortie), "octets,", sum(len(c["etoiles"]) for c in cons.values()), "etoiles")
    for k, c in cons.items():
        for e, src in zip(c["etoiles"], sources["constellations"][k]):
            e["source"] = src
    return data


if __name__ == "__main__":
    d = construire()
    for c in ("gemeaux", "orion", "ourse"):
        print(c, [(e["nom"], e["affiche"], e["environ"]) for e in d["constellations"][c]["etoiles"]])
