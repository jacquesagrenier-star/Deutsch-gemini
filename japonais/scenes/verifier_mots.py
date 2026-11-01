# -*- coding: utf-8 -*-
"""Les mots prevus de chaque scene japonaise sont-ils dans le corpus (N5-N1) ?

    python japonais/scenes/verifier_mots.py            # toutes les scenes
    python japonais/scenes/verifier_mots.py kuukou     # une scene

Entree : japonais/scenes/mots-prevus.json -- pour chaque scene, les mots que
         le prompt fait apparaitre (forme du corpus : kanji quand le corpus
         l'ecrit en kanji, sinon kana) ; `hors_corpus` liste ceux qu'on sait
         absents, avec leur lecture et leur traduction, a ajouter au corpus
         avant que la scene soit jouable.
Corpus : japonais/cartes/mots-n5..n1.json de cette branche (N2 et N1 depuis
         le 1er nov. 2026 : 43 mots qu'on croyait absents y etaient).

Un mot de `mots` absent du corpus est une FAUTE : soit on le retire du
prompt, soit on le deplace dans `hors_corpus` en connaissance de cause.
Brouillon : le japonais attend un natif.
"""
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))


def corpus():
    """Le corpus N5-N1 de cette branche (japonais/cartes/mots-n*.json), par
    forme ECRITE : le kanji quand la fiche en a un, sinon le kana. Jusqu'au
    1er nov. 2026 on lisait le seul N5-N3 de origin/japonais-cartes, et un mot
    se trouvait aussi par sa lecture : 銭湯 tombait sur 戦闘 (« combat »), 線香
    sur 専攻, 炭 sur 隅. Une lecture ne dit pas quel mot c'est."""
    index = {}
    for n in ("5", "4", "3", "2", "1"):
        chemin = os.path.join(RACINE, "japonais", "cartes", "mots-n%s.json" % n)
        for e in json.load(open(chemin, encoding="utf-8"))["entrees"]:
            ec = e["ecritures"]
            v = (ec.get("kanji") or {}).get("v") or ec["kana"]["v"]
            index.setdefault(v, e)
    # Les mots des scenes hors listes JLPT (japonais/cartes/scenes.json, 1er nov.
    # 2026), au format d'une fiche pour ce qu'on en lit ici.
    chemin = os.path.join(RACINE, "japonais", "cartes", "scenes.json")
    for a in json.load(open(chemin, encoding="utf-8"))["mots"]:
        index.setdefault(a["mot"], {
            "id": a["id"], "niveau": "hors JLPT", "jlpt_estime": a["jlpt"],
            "ecritures": {"kana": {"v": a["lecture"]}},
            "gloses": {"fr": {"affichee": {"v": a["fr"]}}}})
    return index


def main():
    prevus = json.load(open(os.path.join(ICI, "mots-prevus.json"), encoding="utf-8"))
    voulues = sys.argv[1:] or [k for k in prevus if not k.startswith("_")]
    idx = corpus()
    fautes = 0
    total_hors = {}
    for nom in voulues:
        s = prevus[nom]
        manquants = [m for m in s["mots"] if m not in idx]
        niv = {}
        for m in s["mots"]:
            if m in idx:
                niv[idx[m]["niveau"]] = niv.get(idx[m]["niveau"], 0) + 1
        hors = s.get("hors_corpus", {})
        deja = [m for m in hors if m in idx]
        print("%-16s %2d mots (%s)  + %d hors corpus%s" % (
            nom, len(s["mots"]),
            " ".join("%s %d" % (k, niv[k]) for k in sorted(niv, reverse=True)),
            len(hors), "" if not manquants else "   FAUTE : " + " ".join(manquants)))
        if deja:
            print("   (dans le corpus, a remonter dans mots : %s)" % " ".join(deja))
        fautes += len(manquants)
        for m, v in hors.items():
            total_hors.setdefault(m, (v, []))[1].append(nom)
    if len(voulues) > 1:
        print("\n%d mots hors corpus a ajouter :" % len(total_hors))
        for m, (v, ou) in sorted(total_hors.items(), key=lambda x: -len(x[1][1])):
            print("   %s (%s) %s -- %s" % (m, v[0], v[1], ", ".join(ou)))
    print("\n%d faute(s)." % fautes)
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
