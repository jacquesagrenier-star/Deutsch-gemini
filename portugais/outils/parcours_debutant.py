# -*- coding: utf-8 -*-
"""Les fichiers du parcours debutant du portugais : reperes, prononciation,
feuilles de conjugaison, Premiers pas, A1 voyage. Appele par construire.py.

Repris de anglais/outils/parcours_debutant.py, sans la variante britannique :
le portugais n'a qu'un jeu de donnees (le Portugal) pour l'instant.
"""
import os, re
import reperes_a1, prononciation_a1, conjugaison_a1, premiers_pas_a1, a1_voyage_a1

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _sens(fr):
    return {"fr": fr}


def _lignes(bloc):
    for l in (bloc or "").strip().splitlines():
        if l.strip():
            yield [c.strip() for c in l.split("|")]


def reperes():
    return {"_lisez_moi": "Derive de portugais/outils/reperes_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "reperes": reperes_a1.REPERES}


def prononciation():
    groupes = []
    for gid, regles in prononciation_a1.GROUPES:
        rs = []
        for r in regles:
            rs.append({"id": r["id"], "graphie": r["graphie"], "api": r["api"],
                       "court": _sens(r["court"]), "explication": _sens(r["explication"]),
                       "exemples": [{"mot": m, "traduction": t} for m, t in _lignes(r["exemples"])]})
        groupes.append({"id": gid, "regles": rs})
    return {"_note": "Derive de portugais/outils/prononciation_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "groupes": groupes}


def conjugaison():
    feuilles = []
    for f in conjugaison_a1.FEUILLES_A1:
        feuilles.append({"id": f["id"], "serie": f["serie"], "temps": None, "t": _sens(f["t"]),
                         "l": [[a, _sens(b)] for a, b in f["l"]], "a": _sens(f["a"])})
    return {"_lisez_moi": "Derive de portugais/outils/conjugaison_a1.py (construire.py) : ne pas modifier a la main. Brouillon.",
            "niveaux": {"A1": feuilles}}


def scenes_portugaises():
    dossier = os.path.join(RACINE, "visuel", "prototype")
    return {n[len("scene-"):-len(".pt.js")] for n in os.listdir(dossier)
            if n.startswith("scene-") and n.endswith(".pt.js")}


def premiers_pas(scenes):
    etapes = []
    for e in premiers_pas_a1.ETAPES:
        tab = e["tableau"]
        cartes = []
        for c in _lignes(e["cartes"]):
            c = (c + ["", ""])[:4]
            cartes.append([c[0], _sens(c[1]), c[2], _sens(c[3]) if c[3] else {}])
        phrases = []
        for p in _lignes(e["phrases"]):
            phrases.append({"p": p[0], "s": _sens(p[1]), "l": [_sens(p[2]), _sens(p[3])]})
        scene = e["scene"] if e["scene"] in scenes else None
        etapes.append({"s": _sens(e["s"]), "scene": scene,
                       "tableau": {"t": _sens(tab["t"]), "l": [[a, _sens(b)] for a, b in _lignes(tab["l"])],
                                   "a": _sens(tab["a"])},
                       "cartes": cartes, "phrases": phrases})
    return {"_lisez_moi": ["Derive de portugais/outils/premiers_pas_a1.py (construire.py) : ne pas modifier a la main.",
                           "« Premiers pas » en portugais du Portugal, a Lisbonne. Brouillon, a faire relire par un lusophone."],
            "etapes": etapes}


def mots_du_corpus(jeu):
    mots = set()
    for t in jeu["themes.json"]["themes"]:
        mots.update(m["mot"] for m in t["mots"])
    for f in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        for e in jeu[f].get("A1", []):
            mots.add(e["mot"])
    return mots


def a1_voyage(jeu, scenes):
    corpus = mots_du_corpus(jeu)
    absents = []

    def mots(liste):
        sortie = []
        for m in [x.strip() for x in liste.split(",") if x.strip()]:
            if m in corpus:
                if m not in sortie:
                    sortie.append(m)
            else:
                absents.append(m)
        return sortie

    def tableau(t):
        return {"t": _sens(t["t"]), "l": [[a, _sens(b)] for a, b in _lignes(t["l"])], "a": _sens(t["a"])}

    def blocs(bloc):
        out = []
        for p, s, pt, fr in _lignes(bloc):
            vpt = [x.strip() for x in pt.split("/")]
            vfr = [x.strip() for x in fr.split("/")]
            p = re.sub(r" ([.,?!])", r"\1", p)
            s = re.sub(r" ([.,])", r"\1", s)
            out.append({"p": p, "s": _sens(s), "v": vpt,
                        "ex": p.replace("…", vpt[-1]).replace(" .", ".").replace(" ,", ",").replace(" ?", "?"),
                        "exs": _sens(s.replace("…", vfr[-1]).replace(" .", ".").replace(" ,", ",")),
                        "vs": [_sens(s.replace("…", v).replace(" .", ".").replace(" ,", ",")) for v in vfr]})
        return out

    def dialogue(d):
        return {"t": _sens(d["t"]), "l": [{"q": q, "p": p, "s": _sens(s)} for q, p, s in _lignes(d["l"])]}

    def lieu(e):
        return {"id": e["id"], "pour": e["pour"], "icone": e["icone"], "s": _sens(e["s"]),
                "scenes": [x for x in e["scenes"] if x in scenes], "mots": mots(e["mots"]),
                "tableau": tableau(e["tableau"]), "blocs": blocs(e["blocs"]), "dialogue": dialogue(e["dialogue"])}

    d = {"_lisez_moi": ["Derive de portugais/outils/a1_voyage_a1.py (construire.py) : ne pas modifier a la main.",
                        "L'A1 voyage du portugais, a Lisbonne : 12 escales, 2 etapes « installe », la suite en 8 etapes. Brouillon."],
         "escales": [lieu(e) for e in a1_voyage_a1.ESCALES],
         "installe": [lieu(e) for e in a1_voyage_a1.INSTALLE],
         "suite": [{"id": e["id"], "icone": e["icone"], "s": _sens(e["s"]),
                    "scene": e["scene"] if e["scene"] in scenes else None,
                    "themes": e["themes"], "tableau": tableau(e["tableau"])} for e in a1_voyage_a1.SUITE]}
    return d, sorted(set(absents))


def construire(jeu):
    sc = scenes_portugaises()
    jeu["reperes.json"] = reperes()
    jeu["prononciation.json"] = prononciation()
    jeu["conjugaison.json"] = conjugaison()
    jeu["premiers-pas.json"] = premiers_pas(sc)
    jeu["a1-voyage.json"], absents = a1_voyage(jeu, sc)
    if absents:
        print("A1 voyage : %d mot(s) absent(s) du corpus, ecartes : %s" % (len(absents), ", ".join(absents)))
    themes = {t["id"] for t in jeu["themes.json"]["themes"]}
    for e in a1_voyage_a1.SUITE:
        for t in e["themes"]:
            if t not in themes:
                print("A1 voyage : theme inconnu dans la suite :", t)
    av = jeu["a1-voyage.json"]
    print("A1 voyage : %d escales (%d mots), %d installe, %d etapes de suite, %d phrases toutes faites" % (
        len(av["escales"]), sum(len(e["mots"]) for e in av["escales"]), len(av["installe"]), len(av["suite"]),
        sum(len(e["blocs"]) for e in av["escales"] + av["installe"])))
    n = sum(len(e["cartes"]) for e in jeu["premiers-pas.json"]["etapes"])
    print("Parcours : %d reperes, %d regles de prononciation, %d feuilles, %d etapes de Premiers pas (%d cartes) ; %d scenes .pt.js" % (
        len(jeu["reperes.json"]["reperes"]),
        sum(len(g["regles"]) for g in jeu["prononciation.json"]["groupes"]),
        len(jeu["conjugaison.json"]["niveaux"]["A1"]), len(jeu["premiers-pas.json"]["etapes"]), n, len(sc)))
