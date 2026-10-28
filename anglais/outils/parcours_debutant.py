# -*- coding: utf-8 -*-
"""Les fichiers du parcours debutant de l'anglais : reperes, prononciation,
feuilles de conjugaison, Premiers pas. Appele par construire.py, qui passe sa
fonction vers_gb (la phrase americaine -> la phrase britannique).

Chaque fichier sort en deux versions, americaine et britannique : le moteur
les trouve par la table `fichiers` de LANGUE_ANGLAIS (datos/ ou datos-gb/).
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


def mots_du_corpus(jeu):
    """Le texte de chaque carte A1, tel que le moteur le lit (texteDeCarte) :
    le nom, l'infinitif, l'adjectif, l'adverbe, l'expression."""
    mots = set()
    for t in jeu["themes.json"]["themes"]:
        mots.update(m["mot"] for m in t["mots"])
    for f in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        for e in jeu[f].get("A1", []):
            mots.add(e["mot"])
    return mots


def a1_voyage(est_gb, vers_gb, jeu, us_vers_gb, scenes):
    """L'A1 voyage (anglais/outils/a1_voyage_a1.py). Les mots doivent etre ceux
    des cartes de CE jeu : en britannique, apartment devient flat."""
    conv = (lambda s: vers_gb(s)) if est_gb else (lambda s: s)
    corpus = mots_du_corpus(jeu)
    absents = []

    def mots(liste):
        sortie = []
        # Une expression peut porter une virgule (« The check, please. ») :
        # deux morceaux voisins dont la reunion est une carte n'en font qu'un.
        brut = [x.strip() for x in liste.split(",") if x.strip()]
        morceaux, i = [], 0
        while i < len(brut):
            joint = (brut[i] + ", " + brut[i + 1]) if i + 1 < len(brut) else None
            if joint and (us_vers_gb.get(joint, joint) if est_gb else joint) in corpus:
                morceaux.append(joint)
                i += 2
            else:
                morceaux.append(brut[i])
                i += 1
        for m in morceaux:
            m = us_vers_gb.get(m, m) if est_gb else m
            if m in corpus:
                if m not in sortie:
                    sortie.append(m)
            else:
                absents.append(m)
        return sortie

    def tableau(t):
        return {"t": _sens(t["t"]), "l": [[conv(a), _sens(b)] for a, b in _lignes(t["l"])], "a": _sens(t["a"])}

    def blocs(bloc):
        out = []
        for p, s, en, fr in _lignes(bloc):
            ven = [x.strip() for x in en.split("/")]
            vfr = [x.strip() for x in fr.split("/")]
            # « … . » s'ecrit « …. », comme l'espagnol : pas d'espace avant la ponctuation.
            p = re.sub(r" ([.,?!])", r"\1", p)
            # Le francais garde son espace devant ? et ! : seulement . et ,
            s = re.sub(r" ([.,])", r"\1", s)
            pp = conv(p)
            out.append({"p": pp, "s": _sens(s), "v": [conv(v) for v in ven],
                        "ex": pp.replace("…", conv(ven[-1])).replace(" .", ".").replace(" ,", ",").replace(" ?", "?"),
                        "exs": _sens(s.replace("…", vfr[-1]).replace(" .", ".").replace(" ,", ",")),
                        "vs": [_sens(s.replace("…", v).replace(" .", ".").replace(" ,", ",")) for v in vfr]})
        return out

    def dialogue(d):
        return {"t": _sens(d["t"]), "l": [{"q": q, "p": conv(p), "s": _sens(s)} for q, p, s in _lignes(d["l"])]}

    def lieu(e):
        return {"id": e["id"], "pour": e["pour"], "icone": e["icone"], "s": _sens(e["s"]),
                "scenes": [x for x in e["scenes"] if x in scenes], "mots": mots(e["mots"]),
                "tableau": tableau(e["tableau"]), "blocs": blocs(e["blocs"]), "dialogue": dialogue(e["dialogue"])}

    d = {"_lisez_moi": ["Derive de anglais/outils/a1_voyage_a1.py (construire.py) : ne pas modifier a la main.",
                        "L'A1 voyage de l'anglais, a Boston : 12 escales, 2 etapes « installe », la suite en 8 etapes. Brouillon."],
         "escales": [lieu(e) for e in a1_voyage_a1.ESCALES],
         "installe": [lieu(e) for e in a1_voyage_a1.INSTALLE],
         "suite": [{"id": e["id"], "icone": e["icone"], "s": _sens(e["s"]),
                    "scene": e["scene"] if e["scene"] in scenes else None,
                    "themes": e["themes"], "tableau": tableau(e["tableau"])} for e in a1_voyage_a1.SUITE]}
    return d, sorted(set(absents))


def construire(us, gb, vers_gb):
    sc = scenes_anglaises()
    # Le mot britannique de chaque carte americaine (memes themes, meme ordre).
    us_vers_gb = {}
    for tu, tg in zip(us["themes.json"]["themes"], gb["themes.json"]["themes"]):
        for mu, mg in zip(tu["mots"], tg["mots"]):
            if mu["mot"] != mg["mot"]:
                us_vers_gb[mu["mot"]] = mg["mot"]
    for f in ("adjectifs.json", "expressions.json"):
        for eu, eg in zip(us[f]["A1"], gb[f]["A1"]):
            if eu["mot"] != eg["mot"]:
                us_vers_gb[eu["mot"]] = eg["mot"]
    for jeu, est_gb in ((us, False), (gb, True)):
        jeu["reperes.json"] = reperes(est_gb, vers_gb)
        jeu["prononciation.json"] = prononciation(est_gb)
        jeu["conjugaison.json"] = conjugaison(est_gb, vers_gb)
        jeu["premiers-pas.json"] = premiers_pas(est_gb, vers_gb, sc)
        jeu["a1-voyage.json"], absents = a1_voyage(est_gb, vers_gb, jeu, us_vers_gb, sc)
        if absents:
            print("A1 voyage (%s) : %d mot(s) absent(s) du corpus, ecartes : %s"
                  % ("gb" if est_gb else "us", len(absents), ", ".join(absents)))
    av = us["a1-voyage.json"]
    print("A1 voyage : %d escales (%d mots), %d installe, %d etapes de suite, %d phrases toutes faites" % (
        len(av["escales"]), sum(len(e["mots"]) for e in av["escales"]), len(av["installe"]), len(av["suite"]),
        sum(len(e["blocs"]) for e in av["escales"] + av["installe"])))
    n = sum(len(e["cartes"]) for e in us["premiers-pas.json"]["etapes"])
    print("Parcours : %d reperes, %d regles de prononciation, %d feuilles, %d etapes de Premiers pas (%d cartes)" % (
        len(us["reperes.json"]["reperes"]),
        sum(len(g["regles"]) for g in us["prononciation.json"]["groupes"]),
        len(us["conjugaison.json"]["niveaux"]["A1"]), len(us["premiers-pas.json"]["etapes"]), n))
