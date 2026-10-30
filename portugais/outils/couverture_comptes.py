# -*- coding: utf-8 -*-
"""La couverture du portugais A2-C1, niveau par niveau, contre l'espagnol,
l'anglais et l'allemand (sur le modele de anglais/outils/couverture_comptes.py).

    python portugais/outils/couverture_comptes.py

Le portugais est compte en construisant les niveaux en memoire (niveaux.py,
sans rien ecrire) ; les autres dans leurs donnees derivees. Les questions de
scenes portugaises viennent de portugais/scenes/*.json (les couches A2-C1
ecrites pour le portugais) ; celles des autres langues, des scenes construites.

L'espagnol n'a pas de C1 : le C1 se compare a l'allemand et a l'anglais.
"""
import contextlib, glob, io, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NIVEAUX = ["A2", "B1", "B2", "C1"]


def charger(p):
    p = os.path.join(RACINE, p)
    if not os.path.exists(p):
        return None
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def par_niveau(d):
    return {n: len((d or {}).get(n, [])) for n in NIVEAUX} if d else None


def noms(d):
    if not d:
        return None
    c = {n: 0 for n in NIVEAUX}
    for t in d["themes"]:
        n = (t.get("niveau") or "").upper()
        if n in c:
            c[n] += len(t.get("mots", []))
    return c


def fonctionnels(d):
    if not d:
        return None
    if all(k in ("A1",) + tuple(NIVEAUX) for k in d):
        return {n: len(d.get(n, [])) for n in NIVEAUX}
    c = {n: 0 for n in NIVEAUX}
    for liste in d.values():
        for e in liste:
            n = (e.get("niveau") or "").upper()
            if n in c:
                c[n] += 1
    return c


def feuilles(d):
    if not d:
        return None
    return {n: len(d.get("niveaux", {}).get(n, [])) for n in NIVEAUX}


def grammaire(g, ex):
    if not g or not ex:
        return None, None
    f, q = {n: 0 for n in NIVEAUX}, {n: 0 for n in NIVEAUX}
    for fiche in g["fiches"]:
        n = fiche.get("niveau")
        if n in f:
            f[n] += 1
            q[n] += len(ex["jeux"].get(fiche.get("serie"), []))
    for t in g.get("temps", []):
        n = t.get("niveau")
        if n in q:
            q[n] += len(ex["jeux"].get(t.get("serie"), []))
    return f, q


def scenes_construites(suffixe):
    c = {n: 0 for n in NIVEAUX}
    vu = False
    for f in glob.glob(os.path.join(RACINE, "visuel", "prototype", "scene-*%s.js" % suffixe)):
        nom = os.path.basename(f)[len("scene-"):-len(suffixe + ".js")]
        if "." in nom:
            continue
        vu = True
        t = io.open(f, encoding="utf-8").read()
        s = json.loads(t[t.index("{"):t.rindex("}") + 1])
        for n, couche in (s.get("couches") or {}).items():
            if n in c:
                c[n] += len(couche.get("qs", []))
    return c if vu else None


def scenes_pt():
    c = {n: 0 for n in NIVEAUX}
    nb = {n: 0 for n in NIVEAUX}
    for f in glob.glob(os.path.join(RACINE, "portugais", "scenes", "*.json")):
        d = json.load(io.open(f, encoding="utf-8"))
        for n, couche in d.get("couches", {}).items():
            if n in c:
                c[n] += len(couche.get("qs", []))
                nb[n] += 1
    return c, nb


def main():
    import niveaux
    with contextlib.redirect_stdout(io.StringIO()):
        jeu = niveaux.construire(niveaux.charger_a1())
    fp, qp = grammaire(jeu["grammaire.json"], jeu["exercices.json"])
    sc, nb_sc = scenes_pt()
    pt = {
        "Noms": noms(jeu["themes.json"]), "Verbes": par_niveau(jeu["verbes.json"]),
        "Adjectifs": par_niveau(jeu["adjectifs.json"]), "Adverbes": par_niveau(jeu["adverbes.json"]),
        "Expressions": par_niveau(jeu["expressions.json"]), "Mots-outils": fonctionnels(jeu.get("fonctionnels.json")),
        "Fiches de grammaire": fp, "Questions de grammaire (fiches + temps)": qp,
        "Feuilles de conjugaison": feuilles(jeu.get("conjugaison.json")), "Questions de scenes": sc,
    }
    fe, qe = grammaire(charger("anglais/datos/grammaire.json"), charger("anglais/datos/exercices.json"))
    en = {
        "Noms": noms(charger("anglais/datos/themes.json")), "Verbes": par_niveau(charger("anglais/datos/verbes.json")),
        "Adjectifs": par_niveau(charger("anglais/datos/adjectifs.json")), "Adverbes": par_niveau(charger("anglais/datos/adverbes.json")),
        "Expressions": par_niveau(charger("anglais/datos/expressions.json")),
        "Mots-outils": fonctionnels(charger("anglais/datos/fonctionnels.json")),
        "Fiches de grammaire": fe, "Questions de grammaire (fiches + temps)": qe,
        "Feuilles de conjugaison": feuilles(charger("anglais/datos/conjugaison.json")),
        "Questions de scenes": scenes_construites(".en"),
    }
    es = {
        "Noms": noms(charger("espanol/datos/temas.json")), "Verbes": par_niveau(charger("espanol/datos/verbos.json")),
        "Adjectifs": par_niveau(charger("espanol/datos/adjetivos.json")), "Adverbes": par_niveau(charger("espanol/datos/adverbios.json")),
        "Expressions": par_niveau(charger("espanol/datos/expresiones.json")),
        "Mots-outils": fonctionnels(charger("espanol/datos/funcionales.json")),
        "Fiches de grammaire": None, "Questions de grammaire (fiches + temps)": None,
        "Feuilles de conjugaison": feuilles(charger("espanol/datos/conjugaison.json")),
        "Questions de scenes": scenes_construites(".es"),
    }
    de = {
        "Noms": noms(charger("themes.json")), "Verbes": par_niveau(charger("verbe.json")),
        "Adjectifs": par_niveau(charger("adjectif.json")), "Adverbes": par_niveau(charger("adverbe.json")),
        "Expressions": par_niveau(charger("redewendung.json")), "Mots-outils": fonctionnels(charger("funktionswort.json")),
        "Fiches de grammaire": None, "Questions de grammaire (fiches + temps)": None,
        "Feuilles de conjugaison": feuilles(charger("conjugaison.json")),
        "Questions de scenes": scenes_construites(""),
    }

    def v(d, n):
        return "—" if not d or d.get(n) is None else str(d[n])

    print("| | A2 | B1 | B2 | C1 |")
    print("|---|---|---|---|---|")
    for ligne in pt:
        cases = []
        for n in NIVEAUX:
            ref = "es %s · en %s" % (v(es[ligne], n), v(en[ligne], n)) if n != "C1" else "de %s · en %s" % (v(de[ligne], n), v(en[ligne], n))
            cases.append("**%s** (%s)" % (v(pt[ligne], n), ref))
        print("| %s | %s |" % (ligne, " | ".join(cases)))
    print()
    print("Scenes portugaises ayant leur couche : " + ", ".join("%s %d" % (n, nb_sc[n]) for n in NIVEAUX))


if __name__ == "__main__":
    main()
