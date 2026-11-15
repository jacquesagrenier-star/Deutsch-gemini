# -*- coding: utf-8 -*-
"""Corrections ponctuelles de l'espagnol du corpus, et la liste des collisions a trancher.

    python interface-es/outils/corriger.py collisions          -> interface-es/sources/collisions.json
    python interface-es/outils/corriger.py controle <lot.json>
    python interface-es/outils/corriger.py pose <lot.json>

Un lot de corrections :
    {"corrections": [{"fichier": "themes.json", "n": 12, "mot": "Schlaf",
                      "champ": "traduction", "avant": "el sueño", "apres": "el sueño (dormir)"}]}
La pose refuse tout ce qui ne correspond plus : le mot allemand au numero n, la
valeur « avant » encore dans le fichier. Meme numerotation et memes garde-fous
d'ecriture que tests/corpus_langue.py (aller-retour a l'octet, relecture).
"""
import collections, io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "tests"))
import corpus_langue as C  # noqa: E402
CATEGORIES = {"noms": ["themes.json"], "verbes": ["verbe.json", "themes.json"], "adjectifs": ["adjectif.json", "themes.json"]}


def collisions():
    """Les groupes de cartes dont la traduction espagnole est identique, par categorie
    (comme tests/relecture_langue.py --collisions), avec leur numero de carte."""
    groupes = collections.defaultdict(list)
    for nom in C.FICHIERS:
        d, _ = C.charger(nom)
        for i, (niv, ctx, m) in enumerate(C.cases(nom, d)):
            t = (m.get("traduction_es") or "").strip().lower()
            if not t:
                continue
            cat = "verbes" if "infinitif" in m else ("noms" if m.get("genre") else nom)
            groupes[(cat, t)].append({"fichier": nom, "n": i, "mot": C.cle(m), "genre": m.get("genre", ""),
                                      "niveau": niv, "contexte": ctx, "fr": m.get("traduction", ""),
                                      "en": m.get("traduction_en", ""), "es": m.get("traduction_es", ""),
                                      "exemple": m.get("exemple", ""), "exemple_es": m.get("exemple_es", "")})
    out = []
    for (cat, t), cartes in sorted(groupes.items()):
        mots = {c["mot"] for c in cartes}
        if len(mots) > 1:
            out.append({"categorie": cat, "es": t, "cartes": cartes})
    io.open(os.path.join(ICI, "sources", "collisions.json"), "w", encoding="utf-8").write(
        json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("%d groupes, %d cartes -> interface-es/sources/collisions.json" % (len(out), sum(len(g["cartes"]) for g in out)))


def verifier(lot):
    fautes, par_fichier = [], collections.defaultdict(list)
    for c in lot["corrections"]:
        par_fichier[c["fichier"]].append(c)
    charges = {}
    for nom, cs in par_fichier.items():
        d, brut = C.charger(nom)
        toutes = C.cases(nom, d)
        charges[nom] = (d, brut, toutes)
        for c in cs:
            if c["n"] >= len(toutes):
                fautes.append("%s #%d hors du fichier" % (nom, c["n"]))
                continue
            m = toutes[c["n"]][2]
            if C.cle(m) != c["mot"]:
                fautes.append("%s #%d : le lot dit %r, le fichier %r" % (nom, c["n"], c["mot"], C.cle(m)))
            k = c["champ"] + "_es"
            if (m.get(k) or "") != c["avant"]:
                fautes.append("%s #%d %s : « avant » ne correspond plus (%r)" % (nom, c["n"], k, m.get(k)))
            if not (c.get("apres") or "").strip():
                fautes.append("%s #%d : « apres » vide" % (nom, c["n"]))
    return fautes, par_fichier, charges


def controle(chemin):
    fautes, _, _ = verifier(json.load(io.open(chemin, encoding="utf-8")))
    for f in fautes:
        print("FAUTE", f)
    print("%d faute(s)" % len(fautes))
    return fautes


def pose(chemin):
    lot = json.load(io.open(chemin, encoding="utf-8"))
    fautes, par_fichier, charges = verifier(lot)
    if fautes:
        sys.exit("ARRET : %d fautes, rien n'est ecrit" % len(fautes))
    for nom, cs in par_fichier.items():
        d, brut, toutes = charges[nom]
        saut, crlf = brut.endswith("\n"), "\r\n" in brut
        if C.serialiser(d, saut, crlf) != brut:
            sys.exit("%s ne se reproduit pas a l'octet pres" % nom)
        for c in cs:
            toutes[c["n"]][2][c["champ"] + "_es"] = c["apres"]
        io.open(os.path.join(RACINE, nom), "w", encoding="utf-8", newline="").write(C.serialiser(d, saut, crlf))
        relu, _ = C.charger(nom)
        rt = C.cases(nom, relu)
        if any(rt[c["n"]][2].get(c["champ"] + "_es") != c["apres"] for c in cs):
            sys.exit("RELECTURE : %s differe" % nom)
        print("%s : %d corrections posees, relues" % (nom, len(cs)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    {"collisions": lambda: collisions(), "controle": lambda: sys.exit(1 if controle(a[1]) else 0),
     "pose": lambda: pose(a[1])}[a[0]]()
