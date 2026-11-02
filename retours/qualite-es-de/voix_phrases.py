# -*- coding: utf-8 -*-
"""Les voix des six phrases de verbes corrigees (phrases_verbes.py), et rien
d'autre : Aurora, eleven_multilingual_v2 (jamais Flash), par les fonctions de
audio/generer.py (memes reglages, meme graine, lectures des nombres).

    python retours/qualite-es-de/voix_phrases.py --a-blanc
    python retours/qualite-es-de/voix_phrases.py
"""
import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "audio"))
sys.path.insert(0, ICI)
import generer      # noqa: E402
import lectures     # noqa: E402
from phrases_verbes import PHRASES  # noqa: E402


def main():
    modele = generer.MODELES["v2"][0]
    assert modele == "eleven_multilingual_v2"
    textes = [p[4] for p in PHRASES]
    a_faire = []
    for t in textes:
        ident = hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]
        chemin = os.path.join(generer.SORTIE, ident + ".mp3")
        print("%s %s %s" % (ident, "deja la" if os.path.exists(chemin) else "a faire", t))
        if not os.path.exists(chemin):
            a_faire.append((t, chemin))
    credits = sum(len(lectures.lecture("de", t)) for t, _ in a_faire)
    print("%d fichiers, environ %d credits" % (len(a_faire), credits))
    if "--a-blanc" in sys.argv or not a_faire:
        return
    cle = generer.cle_api()
    for t, chemin in a_faire:
        octets = generer.synthetiser(lectures.lecture("de", t), modele, cle)
        with open(chemin, "wb") as f:
            f.write(octets)
        print("  + %s (%d o)" % (os.path.basename(chemin), len(octets)))
    print("depense : %d credits" % credits)


if __name__ == "__main__":
    main()
