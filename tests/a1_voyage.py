# -*- coding: utf-8 -*-
"""Contrôle de l'A1 voyage (a1-voyage.json et espanol/datos/a1-voyage.json).
Aucune dépendance.

    python tests/a1_voyage.py                      # contrôle les deux fichiers
    python tests/a1_voyage.py --detail             # et les comptes par escale
    python tests/a1_voyage.py --inventaire de      # les mots A1 de l'allemand, par catégorie
    python tests/a1_voyage.py --inventaire es      # ceux de l'espagnol
    python tests/a1_voyage.py --libres de          # les mots A1 qu'aucune escale ne prend encore

L'A1 voyage (18 oct. 2026) range l'A1 EXISTANT par situations : après Premiers pas,
12 escales (10 utiles à tous, puis 2 seulement touristiques), deux escales de
remplacement pour qui « s'installe » (elles prennent la place des 2 touristiques),
puis la suite de l'A1 en 8 étapes. Les mots ne s'écrivent pas : chaque escale
NOMME des mots qui existent déjà dans l'A1 (themes.json, verbe.json...). Ce qui
s'écrit : le tableau, les phrases toutes faites et le dialogue de chaque escale.

Ce qu'il vérifie :
  - 12 escales dans l'ordre : « pour » = "tous" pour les 10 premières, "voyage" pour
    les 2 dernières ; 2 escales « installe » ; 8 étapes de « suite » ;
  - chaque mot nommé existe dans l'A1 de la langue (même graphie, sans article) ;
    25 à 35 mots par escale ; aucun mot dans deux escales ;
  - chaque objet de sens porte toutes les langues attendues, non vides
    (allemand : fr en tr uk fa ar pt pl ru ; espagnol : fr en pt ar) ;
  - un tableau par escale et par étape (4 à 8 lignes) ;
  - 5 ou 6 phrases toutes faites par escale, chacune avec un « … » à remplir,
    3 variantes, un exemple complet et son sens ;
  - un dialogue de 4 à 6 répliques qui alternent, « eux » d'abord ; les répliques
    « moi » font 10 mots au plus (elles se disent à voix haute et se jugent) ;
  - chaque scène existe (visuel/prototype/scene-<nom>.js, et .es.js pour l'espagnol) ;
  - chaque thème de la suite existe dans l'A1 de la langue.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIERS = {
    "de": {"chemin": "a1-voyage.json", "langues": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]},
    "es": {"chemin": os.path.join("espanol", "datos", "a1-voyage.json"), "langues": ["fr", "en", "pt", "ar"]},
}
NB_ESCALES, NB_TOURISTIQUES, NB_INSTALLE, NB_SUITE = 12, 2, 2, 8
MOTS_MIN, MOTS_MAX = 25, 35
BLOCS_MIN, BLOCS_MAX = 5, 6
TABLEAU_MIN, TABLEAU_MAX = 4, 8
DIALOGUE_MIN, DIALOGUE_MAX = 4, 6
MOI_MAX_MOTS = 10


def lire(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return json.load(f)


def inventaire(code):
    """{catégorie: [(mot, sens fr, thème)]} pour l'A1 de la langue."""
    inv = {}

    def ajouter(cat, mot, fr, theme=""):
        if mot:
            inv.setdefault(cat, []).append((mot, fr or "", theme))

    if code == "de":
        th = lire("themes.json")
        th = th if isinstance(th, list) else th.get("themes", th)
        for t in th:
            if t.get("niveau") == "A1":
                for m in t.get("mots", []):
                    ajouter("noms", m.get("mot"), m.get("traduction"), t.get("id"))
        for e in lire("verbe.json").get("A1", []):
            ajouter("verbes", e.get("infinitif"), e.get("traduction"))
        for f, cat in (("adjectif.json", "adjectifs"), ("adverbe.json", "adverbes"), ("redewendung.json", "expressions")):
            for e in lire(f).get("A1", []):
                ajouter(cat, e.get("mot"), e.get("traduction"))
        for fam, liste in lire("funktionswort.json").items():
            for e in liste:
                if e.get("niveau") == "A1":
                    ajouter("mots-outils (" + fam + ")", e.get("mot"), e.get("traduction"))
    else:
        base = os.path.join("espanol", "datos")
        th = lire(os.path.join(base, "temas.json"))
        th = th if isinstance(th, list) else th.get("themes", th)
        for t in th:
            if t.get("niveau") == "A1":
                for m in t.get("mots", []):
                    ajouter("noms", m.get("mot"), m.get("traduction"), t.get("id"))
        for f, cat in (("verbos.json", "verbes"), ("adjetivos.json", "adjectifs"), ("adverbios.json", "adverbes"),
                       ("expresiones.json", "expressions"), ("funcionales.json", "mots-outils")):
            for e in lire(os.path.join(base, f)).get("A1", []):
                ajouter(cat, e.get("infinitif") or e.get("mot"), e.get("traduction"))
    return inv


def themes_a1(code):
    if code == "de":
        th = lire("themes.json")
    else:
        th = lire(os.path.join("espanol", "datos", "temas.json"))
    th = th if isinstance(th, list) else th.get("themes", th)
    return {t.get("id") for t in th if t.get("niveau") == "A1"}


def scene_existe(code, nom):
    base = os.path.join(RACINE, "visuel", "prototype")
    ok = os.path.exists(os.path.join(base, "scene-%s.js" % nom))
    if code == "es":
        ok = ok and os.path.exists(os.path.join(base, "scene-%s.es.js" % nom))
    return ok


def sens_complet(o, langues):
    return isinstance(o, dict) and all(isinstance(o.get(l), str) and o.get(l).strip() for l in langues)


def nb_mots(texte):
    return len([m for m in re.sub(r"[¿?¡!.,;:«»\"“”„…]", " ", texte).split() if m])


def verifier(code, info, data, detail):
    err = []
    nom = info["chemin"]
    langues = info["langues"]
    inv = inventaire(code)
    connus = {m for liste in inv.values() for (m, _, _) in liste}
    escales = data.get("escales")
    installe = data.get("installe")
    suite = data.get("suite")
    if not isinstance(escales, list) or not isinstance(installe, list) or not isinstance(suite, list):
        return ["%s : il faut trois listes « escales », « installe », « suite »" % nom]
    if len(escales) != NB_ESCALES:
        err.append("%s : %d escales au lieu de %d" % (nom, len(escales), NB_ESCALES))
    if len(installe) != NB_INSTALLE:
        err.append("%s : %d escales « installe » au lieu de %d" % (nom, len(installe), NB_INSTALLE))
    if len(suite) != NB_SUITE:
        err.append("%s : %d étapes de suite au lieu de %d" % (nom, len(suite), NB_SUITE))

    vus = {}
    ids = set()
    for groupe, liste in (("escales", escales), ("installe", installe)):
        for i, e in enumerate(liste):
            ou = "%s %s[%d] %s" % (nom, groupe, i, e.get("id", "?"))
            if not e.get("id") or e.get("id") in ids:
                err.append("%s : id absent ou en double" % ou)
            ids.add(e.get("id"))
            attendu = "installe" if groupe == "installe" else ("voyage" if i >= NB_ESCALES - NB_TOURISTIQUES else "tous")
            if e.get("pour") != attendu:
                err.append("%s : « pour » vaut %r au lieu de %r" % (ou, e.get("pour"), attendu))
            if not e.get("icone"):
                err.append("%s : pas d'icône" % ou)
            if not sens_complet(e.get("s"), langues):
                err.append("%s : titre « s » incomplet" % ou)
            for sc in e.get("scenes", []):
                if not scene_existe(code, sc):
                    err.append("%s : scène inconnue %r" % (ou, sc))
            mots = e.get("mots", [])
            if not (MOTS_MIN <= len(mots) <= MOTS_MAX):
                err.append("%s : %d mots (attendu %d à %d)" % (ou, len(mots), MOTS_MIN, MOTS_MAX))
            for m in mots:
                if m not in connus:
                    err.append("%s : mot absent de l'A1 : %r" % (ou, m))
                elif m in vus:
                    err.append("%s : %r est déjà dans %s" % (ou, m, vus[m]))
                else:
                    vus[m] = e.get("id")
            err += verifier_tableau(ou, e.get("tableau"), langues)
            blocs = e.get("blocs", [])
            if not (BLOCS_MIN <= len(blocs) <= BLOCS_MAX):
                err.append("%s : %d phrases toutes faites (attendu %d à %d)" % (ou, len(blocs), BLOCS_MIN, BLOCS_MAX))
            for j, b in enumerate(blocs):
                ob = "%s bloc %d" % (ou, j + 1)
                if "…" not in (b.get("p") or ""):
                    err.append("%s : le moule « p » n'a pas de « … »" % ob)
                if not sens_complet(b.get("s"), langues):
                    err.append("%s : sens du moule incomplet" % ob)
                v = b.get("v", [])
                if len(v) != 3 or not all(isinstance(x, str) and x.strip() for x in v):
                    err.append("%s : il faut 3 variantes" % ob)
                if not (b.get("ex") or "").strip():
                    err.append("%s : pas d'exemple « ex »" % ob)
                if not sens_complet(b.get("exs"), langues):
                    err.append("%s : sens de l'exemple incomplet" % ob)
            d = e.get("dialogue") or {}
            if not sens_complet(d.get("t"), langues):
                err.append("%s : titre du dialogue incomplet" % ou)
            lignes = d.get("l", [])
            if not (DIALOGUE_MIN <= len(lignes) <= DIALOGUE_MAX):
                err.append("%s : dialogue de %d répliques (attendu %d à %d)" % (ou, len(lignes), DIALOGUE_MIN, DIALOGUE_MAX))
            for j, l in enumerate(lignes):
                attendu = "eux" if j % 2 == 0 else "moi"
                if l.get("q") != attendu:
                    err.append("%s : réplique %d de %r au lieu de %r" % (ou, j + 1, l.get("q"), attendu))
                if not (l.get("p") or "").strip() or not sens_complet(l.get("s"), langues):
                    err.append("%s : réplique %d incomplète" % (ou, j + 1))
                if l.get("q") == "moi" and nb_mots(l.get("p") or "") > MOI_MAX_MOTS:
                    err.append("%s : réplique %d trop longue pour l'oral (%d mots)" % (ou, j + 1, nb_mots(l.get("p"))))
            if detail:
                print("  %-12s %-9s %2d mots  %d phrases  %d répliques  scènes %s" % (
                    e.get("id"), e.get("pour"), len(mots), len(blocs), len(lignes), ", ".join(e.get("scenes", [])) or "-"))

    tha = themes_a1(code)
    for i, e in enumerate(suite):
        ou = "%s suite[%d] %s" % (nom, i, e.get("id", "?"))
        if not e.get("id") or e.get("id") in ids:
            err.append("%s : id absent ou en double" % ou)
        ids.add(e.get("id"))
        if not e.get("icone"):
            err.append("%s : pas d'icône" % ou)
        if not sens_complet(e.get("s"), langues):
            err.append("%s : titre « s » incomplet" % ou)
        if e.get("scene") and not scene_existe(code, e.get("scene")):
            err.append("%s : scène inconnue %r" % (ou, e.get("scene")))
        th = e.get("themes", [])
        if not th:
            err.append("%s : aucun thème" % ou)
        for t in th:
            if t not in tha:
                err.append("%s : thème A1 inconnu %r" % (ou, t))
        err += verifier_tableau(ou, e.get("tableau"), langues)
        if detail:
            print("  suite %-10s thèmes %s" % (e.get("id"), ", ".join(th)))
    if detail:
        print("  %s : %d mots pris par les escales, sur %d mots A1" % (nom, len(vus), len(connus)))
    return err


def verifier_tableau(ou, tab, langues):
    err = []
    if not isinstance(tab, dict):
        return ["%s : pas de tableau" % ou]
    if not sens_complet(tab.get("t"), langues):
        err.append("%s : titre du tableau incomplet" % ou)
    lignes = tab.get("l", [])
    if not (TABLEAU_MIN <= len(lignes) <= TABLEAU_MAX):
        err.append("%s : tableau de %d lignes (attendu %d à %d)" % (ou, len(lignes), TABLEAU_MIN, TABLEAU_MAX))
    for j, l in enumerate(lignes):
        if not (isinstance(l, list) and len(l) == 2 and isinstance(l[0], str) and l[0].strip() and sens_complet(l[1], langues)):
            err.append("%s : ligne %d du tableau mal formée" % (ou, j + 1))
    if tab.get("a") is not None and not sens_complet(tab.get("a"), langues):
        err.append("%s : astuce du tableau incomplète" % ou)
    return err


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--inventaire" in sys.argv or "--libres" in sys.argv:
        code = sys.argv[-1] if sys.argv[-1] in FICHIERS else "de"
        inv = inventaire(code)
        pris = set()
        if "--libres" in sys.argv:
            try:
                data = lire(FICHIERS[code]["chemin"])
                for e in data.get("escales", []) + data.get("installe", []):
                    pris.update(e.get("mots", []))
            except Exception:
                pass
        total = 0
        for cat, liste in inv.items():
            liste = [x for x in liste if x[0] not in pris]
            print("== %s (%d)" % (cat, len(liste)))
            for mot, fr, theme in liste:
                print("  %s  --  %s%s" % (mot, fr, ("  [" + theme + "]") if theme else ""))
            total += len(liste)
        print("\n%d mots." % total)
        return
    detail = "--detail" in sys.argv
    erreurs = []
    for code, info in FICHIERS.items():
        if not os.path.exists(os.path.join(RACINE, info["chemin"])):
            print("%s : pas encore écrit." % info["chemin"])
            continue
        try:
            data = lire(info["chemin"])
        except Exception as e:
            erreurs.append("%s : illisible (%s)" % (info["chemin"], e))
            continue
        erreurs += verifier(code, info, data, detail)
    if erreurs:
        print("\n".join(erreurs))
        print("\n%d problème(s)." % len(erreurs))
        sys.exit(1)
    print("A1 voyage : aucun problème.")


if __name__ == "__main__":
    main()
