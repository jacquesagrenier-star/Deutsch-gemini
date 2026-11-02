# -*- coding: utf-8 -*-
"""Scenes espagnoles : langue x contenu des couches A2-C1 (titres, phrases,
sens) et articles de mots.json contre le corpus espagnol.

    python retours/qualite-es-de/scenes_es.py
"""
import collections
import glob
import os
import re

import commun
from langues import juger


def main():
    racine = commun.RACINE
    fichiers = sorted(glob.glob(os.path.join(racine, "visuel", "prototype", "espanol", "*.json")))
    tot = collections.Counter()
    out = []
    for f in fichiers:
        if f.endswith("mots.json"):
            continue
        rel = os.path.relpath(f, racine).replace(os.sep, "/")
        d = commun.charger(rel)
        for ch, cle, fr, tr, src, obj in commun.groupes(d, commun.LANGUES["es"]):
            for l, t in tr.items():
                tot[l] += 1
                for c in juger("es", cle, fr, l, t, tr, src):
                    out.append((c, l, os.path.basename(f), ch, cle, fr[:70], (t or "")[:70]))
    print(sum(tot.values()), "textes de scenes espagnoles", dict(tot))
    print(collections.Counter((o[0], o[1]) for o in out))
    for o in out:
        print(o)

    mots = commun.charger("visuel/prototype/espanol/mots.json")
    corpus = collections.defaultdict(set)
    for t in commun.charger("espanol/datos/temas.json")["themes"]:
        for x in t["mots"]:
            corpus[x["mot"]].add(x.get("genre"))
    for k, v in mots.items():
        if k.startswith("_"):
            continue
        m = re.match(r"^(el|la|los|las) (.+)$", v.split("#")[0].strip())
        if not m:
            print("sans article", k, v)
        elif m.group(2) not in corpus:
            print("absent du corpus", k, v)


if __name__ == "__main__":
    main()
