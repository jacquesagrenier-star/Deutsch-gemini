# -*- coding: utf-8 -*-
"""Les mots prevus de chaque scene japonaise sont-ils dans le corpus N5-N3 ?

    python japonais/scenes/verifier_mots.py            # toutes les scenes
    python japonais/scenes/verifier_mots.py kuukou     # une scene

Entree : japonais/scenes/mots-prevus.json -- pour chaque scene, les mots que
         le prompt fait apparaitre (forme du corpus : kanji quand le corpus
         l'ecrit en kanji, sinon kana) ; `hors_corpus` liste ceux qu'on sait
         absents, avec leur lecture et leur traduction, a ajouter au corpus
         avant que la scene soit jouable.
Corpus : origin/japonais-cartes:japonais/cartes/mots-n5|n4|n3.json, lu par
         git (rien a copier).

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
    index = {}
    for n in ("5", "4", "3"):
        brut = subprocess.run(
            ["git", "show", "origin/japonais-cartes:japonais/cartes/mots-n%s.json" % n],
            cwd=RACINE, capture_output=True, check=True).stdout.decode("utf-8")
        for e in json.loads(brut)["entrees"]:
            for k in ("kanji", "kana"):
                v = (e["ecritures"].get(k) or {}).get("v")
                if v:
                    index.setdefault(v, e)
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
