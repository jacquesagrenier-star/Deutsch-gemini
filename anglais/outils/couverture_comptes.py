# -*- coding: utf-8 -*-
"""La couverture de l'anglais, niveau par niveau, contre l'espagnol et l'allemand.

    python anglais/outils/couverture_comptes.py

Compte dans les donnees DERIVEES (anglais/datos, espanol/datos, la racine pour
l'allemand) et dans les scenes construites (visuel/prototype/scene-*.js) :
noms, verbes, adjectifs, adverbes, expressions, mots-outils, fiches de grammaire,
questions de leurs series, feuilles de conjugaison, questions de scenes.

L'espagnol n'a ni vocabulaire C1 ni fiches par niveau (ses 17 fiches et 24
series sont communes a tous les niveaux) : le C1 se compare a l'allemand, et la
grammaire au total. Un niveau n'est dit « complet » que lorsque chaque ligne
atteint l'espagnol (l'allemand pour le C1), ou que l'ecart est explique.
"""
import glob, io, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
SCENES_ECARTEES = {"kreuzung", "ubahn", "zug", "stadtplatz", "weihnachtsmarkt", "post"}


def charger(p):
    with io.open(os.path.join(RACINE, p), encoding="utf-8") as f:
        return json.load(f)


def par_niveau(d):
    return {n: len(d.get(n, [])) for n in NIVEAUX}


def noms(fichier):
    c = {n: 0 for n in NIVEAUX}
    for t in charger(fichier)["themes"]:
        n = (t.get("niveau") or "").upper()
        if n in c:
            c[n] += len(t.get("mots", []))
    return c


def fonctionnels(fichier):
    d = charger(fichier)
    c = {n: 0 for n in NIVEAUX}
    if all(k in NIVEAUX for k in d):            # espagnol : par niveau
        return {n: len(d.get(n, [])) for n in NIVEAUX}
    for liste in d.values():                    # allemand, anglais : par categorie
        for e in liste:
            n = (e.get("niveau") or "").upper()
            if n in c:
                c[n] += 1
    return c


def feuilles(fichier):
    d = charger(fichier).get("niveaux", {})
    return {n: len(d.get(n, [])) for n in NIVEAUX}


def scenes(suffixe, exclues=()):
    c = {n: 0 for n in NIVEAUX}
    for f in glob.glob(os.path.join(RACINE, "visuel", "prototype", "scene-*%s.js" % suffixe)):
        nom = os.path.basename(f)[len("scene-"):-len(suffixe + ".js")]
        if "." in nom or nom in exclues:
            continue
        t = io.open(f, encoding="utf-8").read()
        s = json.loads(t[t.index("{"):t.rindex("}") + 1])
        for n, couche in (s.get("couches") or {}).items():
            if n in c:
                c[n] += len(couche.get("qs", []))
    return c


def grammaire_en():
    g = charger("anglais/datos/grammaire.json")["fiches"]
    jeux = charger("anglais/datos/exercices.json")["jeux"]
    f = {n: 0 for n in NIVEAUX}
    q = {n: 0 for n in NIVEAUX}
    for fiche in g:
        n = fiche.get("niveau") or "A1"
        f[n] += 1
        q[n] += len(jeux.get(fiche.get("serie"), []))
    return f, q


def main():
    en = {
        "Noms": noms("anglais/datos/themes.json"),
        "Verbes": par_niveau(charger("anglais/datos/verbes.json")),
        "Adjectifs": par_niveau(charger("anglais/datos/adjectifs.json")),
        "Adverbes": par_niveau(charger("anglais/datos/adverbes.json")),
        "Expressions": par_niveau(charger("anglais/datos/expressions.json")),
        "Mots-outils": fonctionnels("anglais/datos/fonctionnels.json"),
        "Feuilles de conjugaison": feuilles("anglais/datos/conjugaison.json"),
        "Questions de scenes": scenes(".en"),
    }
    es = {
        "Noms": noms("espanol/datos/temas.json"),
        "Verbes": par_niveau(charger("espanol/datos/verbos.json")),
        "Adjectifs": par_niveau(charger("espanol/datos/adjetivos.json")),
        "Adverbes": par_niveau(charger("espanol/datos/adverbios.json")),
        "Expressions": par_niveau(charger("espanol/datos/expresiones.json")),
        "Mots-outils": fonctionnels("espanol/datos/funcionales.json"),
        "Feuilles de conjugaison": feuilles("espanol/datos/conjugaison.json"),
        # Les memes 37 scenes que l'anglais : les six ecartees de Boston ne comptent pas.
        "Questions de scenes": scenes(".es", SCENES_ECARTEES),
    }
    de = {
        "Noms": noms("themes.json"),
        "Verbes": par_niveau(charger("verbe.json")),
        "Adjectifs": par_niveau(charger("adjectif.json")),
        "Adverbes": par_niveau(charger("adverbe.json")),
        "Expressions": par_niveau(charger("redewendung.json")),
        "Mots-outils": fonctionnels("funktionswort.json"),
        "Feuilles de conjugaison": feuilles("conjugaison.json") if os.path.exists(os.path.join(RACINE, "conjugaison.json")) else {n: 0 for n in NIVEAUX},
        "Questions de scenes": scenes("", SCENES_ECARTEES),
    }
    f_en, q_en = grammaire_en()
    en["Fiches de grammaire"], en["Questions de grammaire"] = f_en, q_en

    g_es = charger("espanol/datos/grammaire.json")["fiches"]
    j_es = charger("espanol/datos/ejercicios.json")["jeux"]
    print("Grammaire espagnole (tous niveaux confondus) : %d fiches, %d series, %d questions"
          % (len(g_es), len(j_es), sum(len(v) for v in j_es.values())))
    print("Grammaire anglaise : %d fiches, %d questions\n" % (sum(f_en.values()), sum(q_en.values())))

    for niv in NIVEAUX:
        ref, nom_ref = (de, "allemand") if niv == "C1" else (es, "espagnol")
        print("== %s (reference : %s)" % (niv, nom_ref))
        for cle in en:
            a = en[cle][niv]
            r = ref.get(cle, {}).get(niv)
            if r is None:
                print("   %-26s %6d" % (cle, a))
                continue
            pct = ("%4d %%" % round(100 * a / r)) if r else "   —"
            marque = "" if (r == 0 or a >= r) else "  < " + nom_ref
            print("   %-26s %6d  /%6d  %s%s" % (cle, a, r, pct, marque))
        print()


if __name__ == "__main__":
    main()
