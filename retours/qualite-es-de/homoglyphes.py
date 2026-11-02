# -*- coding: utf-8 -*-
"""Mots qui melangent deux alphabets (un « a » latin dans un mot cyrillique) :
invisibles a l'oeil, ils cassent la recherche et la voix.

    python retours/qualite-es-de/homoglyphes.py
"""
import re
import sys

from commun import FICHIERS, charger

CYR = re.compile(r"[Ѐ-ӿ]")
LAT = re.compile(r"[A-Za-z]")
ARA = re.compile(r"[؀-ۿ]")


def textes(o, ch=""):
    if isinstance(o, str):
        yield ch, o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from textes(v, ch + "." + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from textes(v, "%s[%d]" % (ch, i))


def main():
    n = 0
    for app in ("de", "es"):
        for f in FICHIERS[app]:
            for ch, t in textes(charger(f)):
                for mot in re.findall(r"[^\W\d_]+", t):
                    if CYR.search(mot) and LAT.search(mot):   # l arabe colle و ou بـ a un mot latin : normal
                        n += 1
                        print("%s %s : %r dans %r" % (f, ch, mot, t[:80]))
    print(n, "mot(s) a deux alphabets")


if __name__ == "__main__":
    main()
