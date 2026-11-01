# -*- coding: utf-8 -*-
"""Les mots prevus de chaque scene de Lisbonne sont-ils dans le corpus portugais ?

    python portugais/lisbonne/verifier_mots.py              # toutes les scenes
    python portugais/lisbonne/verifier_mots.py pastelaria   # une scene
    python portugais/lisbonne/verifier_mots.py --chercher bica mola   # ces mots sont-ils au corpus ?

Entree : portugais/lisbonne/mots-prevus.json -- pour chaque scene, les objets que
         le prompt fait apparaitre (le nom tel que le corpus l'ecrit, sans article) ;
         `hors_corpus` liste ceux qu'on sait absents, avec genre et traduction, a
         ajouter au corpus avant que la scene soit jouable.
Corpus : portugais/datos/themes.json (les noms, A1-C1).

Un mot de `mots` absent du corpus est une FAUTE : on le retire du prompt, ou on
le deplace dans `hors_corpus` en connaissance de cause. Meme regle que le
japonais (japonais/scenes/verifier_mots.py) : tout objet bien visible a sa zone,
donc son mot.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))


def corpus():
    d = json.load(io.open(os.path.join(RACINE, "portugais", "datos", "themes.json"), encoding="utf-8"))
    index = {}
    for t in d["themes"]:
        for m in t["mots"]:
            index.setdefault(m["mot"], dict(m, niveau=t.get("niveau"), theme=t.get("id")))
    return index


def main():
    args = sys.argv[1:]
    idx = corpus()
    if args[:1] == ["--chercher"]:
        for w in args[1:]:
            m = idx.get(w)
            print("  %-22s %s" % (w, "%s %s, %s (%s)" % (m["genre"], w, m["traduction"], m["niveau"]) if m else "ABSENT"))
        return
    prevus = json.load(io.open(os.path.join(ICI, "mots-prevus.json"), encoding="utf-8"))
    fautes = 0
    for nom, s in prevus.items():
        if nom.startswith("_") or (args and nom not in args):
            continue
        absents = [w for w in s["mots"] if w not in idx]
        hors = s.get("hors_corpus", {})
        deja = [w for w in hors if w in idx]
        print("%-20s %2d mots, %d hors corpus%s" % (nom, len(s["mots"]), len(hors),
              "" if not absents else "  FAUTE absents : " + ", ".join(absents)))
        if deja:
            print("%20s deja au corpus, a remonter dans « mots » : %s" % ("", ", ".join(deja)))
        fautes += len(absents)
    print("\n%d faute(s)." % fautes)
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
