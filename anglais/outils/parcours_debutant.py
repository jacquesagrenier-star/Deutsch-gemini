# -*- coding: utf-8 -*-
"""Les fichiers du parcours debutant de l'anglais : reperes, prononciation,
feuilles de conjugaison, Premiers pas. Appele par construire.py, qui passe sa
fonction vers_gb (la phrase americaine -> la phrase britannique).

Chaque fichier sort en deux versions, americaine et britannique : le moteur
les trouve par la table `fichiers` de LANGUE_ANGLAIS (datos/ ou datos-gb/).
"""
import os
import reperes_a1, prononciation_a1, conjugaison_a1, premiers_pas_a1

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _sens(fr):
    return {"fr": fr}


def _lignes(bloc):
    for l in (bloc or "").strip().splitlines():
        if l.strip():
            yield [c.strip() for c in l.split("|")]


def reperes(gb, vers_gb):
    out = []
    for r in reperes_a1.REPERES:
        r = {k: (list(v) if isinstance(v, list) else v) for k, v in r.items()}
        if gb:
            def conv(x):
                return vers_gb(x) if isinstance(x, str) else x
            r["l"] = [[conv(c) for c in ligne] if isinstance(ligne, list) else ligne for ligne in r["l"]]
            if r["id"] == "n100-1000":
                # Le britannique dit « one hundred AND twenty ».
                r["x"] = [[m.replace("hundred ", "hundred and ", 1) if m.split("hundred", 1)[-1].strip() else m, n]
                          for m, n in r["x"]]
        out.append(r)
    return {"_lisez_moi": "Derive de anglais/outils/reperes_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "reperes": out}


def prononciation(gb):
    groupes = []
    for gid, regles in prononciation_a1.GROUPES:
        rs = []
        for r in regles:
            v = r.get("gb") if gb else None
            rs.append({"id": r["id"], "graphie": r["graphie"], "api": r["api"],
                       "court": _sens((v or r)["court"]), "explication": _sens((v or r)["explication"]),
                       "exemples": [{"mot": m, "traduction": t} for m, t in _lignes(r["exemples"])]})
        groupes.append({"id": gid, "regles": rs})
    return {"_note": "Derive de anglais/outils/prononciation_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "groupes": groupes}


def conjugaison(gb, vers_gb):
    conv = (lambda s: vers_gb(s)) if gb else (lambda s: s)
    feuilles = []
    for f in conjugaison_a1.FEUILLES_A1:
        feuilles.append({"id": f["id"], "serie": f["serie"], "temps": None, "t": _sens(f["t"]),
                         "l": [[conv(a), _sens(b)] for a, b in f["l"]], "a": _sens(f["a"])})
    return {"_lisez_moi": "Derive de anglais/outils/conjugaison_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "niveaux": {"A1": feuilles}}


def premiers_pas(gb, vers_gb, scenes_anglaises):
    conv = (lambda s: vers_gb(s)) if gb else (lambda s: s)
    etapes = []
    for e in premiers_pas_a1.ETAPES:
        tab = e["tableau"]
        cartes = []
        for c in _lignes(e["cartes"]):
            c = (c + ["", ""])[:4]
            cartes.append([conv(c[0]), _sens(c[1]), conv(c[2]), _sens(c[3]) if c[3] else {}])
        phrases = []
        for p in _lignes(e["phrases"]):
            phrases.append({"p": conv(p[0]), "s": _sens(p[1]), "l": [_sens(p[2]), _sens(p[3])]})
        # La scene seulement si sa version anglaise existe (construire.py des
        # scenes) : sinon l'etape s'ouvre sans scene, comme le japonais.
        scene = e["scene"] if e["scene"] in scenes_anglaises else None
        etapes.append({"s": _sens(e["s"]), "scene": scene,
                       "tableau": {"t": _sens(tab["t"]), "l": [[conv(a), _sens(b)] for a, b in _lignes(tab["l"])],
                                   "a": _sens(tab["a"])},
                       "cartes": cartes, "phrases": phrases})
    return {"_lisez_moi": ["Derive de anglais/outils/premiers_pas_a1.py (construire.py) : ne pas modifier a la main.",
                           "« Premiers pas » en anglais, a Boston. Brouillon, a faire relire par un anglophone."],
            "etapes": etapes}


def scenes_anglaises():
    dossier = os.path.join(RACINE, "visuel", "prototype")
    return {n[len("scene-"):-len(".en.js")] for n in os.listdir(dossier)
            if n.startswith("scene-") and n.endswith(".en.js")}


def construire(us, gb, vers_gb):
    sc = scenes_anglaises()
    for jeu, est_gb in ((us, False), (gb, True)):
        jeu["reperes.json"] = reperes(est_gb, vers_gb)
        jeu["prononciation.json"] = prononciation(est_gb)
        jeu["conjugaison.json"] = conjugaison(est_gb, vers_gb)
        jeu["premiers-pas.json"] = premiers_pas(est_gb, vers_gb, sc)
    n = sum(len(e["cartes"]) for e in us["premiers-pas.json"]["etapes"])
    print("Parcours : %d reperes, %d regles de prononciation, %d feuilles, %d etapes de Premiers pas (%d cartes)" % (
        len(us["reperes.json"]["reperes"]),
        sum(len(g["regles"]) for g in us["prononciation.json"]["groupes"]),
        len(us["conjugaison.json"]["niveaux"]["A1"]), len(us["premiers-pas.json"]["etapes"]), n))
