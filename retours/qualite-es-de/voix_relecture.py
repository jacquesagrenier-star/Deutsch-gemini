# -*- coding: utf-8 -*-
"""Les voix des textes allemands que la relecture complete a changes : ceux
du manifeste APRES correction qui n'etaient pas dans le manifeste AVANT et
n'ont pas encore de fichier. Aurora, eleven_multilingual_v2 (jamais Flash),
par les fonctions de audio/generer.py (memes reglages, lectures des nombres).
Accord de Jacques du 2 nov. 2026 : plafond 5 000 credits pour toute la
relecture (decisions/DECISIONS.md).

    python audio/manifest.py --ecrire      (apres les corrections)
    python retours/qualite-es-de/voix_relecture.py <manifeste-avant.json> --a-blanc
    python retours/qualite-es-de/voix_relecture.py <manifeste-avant.json> --plafond 5000
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer      # noqa: E402
import lectures     # noqa: E402


def main():
    avant = {e["id"] for e in json.load(io.open(sys.argv[1], encoding="utf-8"))}
    apres = generer.charger_manifeste()
    a_faire = [e for e in apres if e["id"] not in avant
               and not os.path.exists(os.path.join(generer.SORTIE, e["id"] + ".mp3"))]
    modele, taux = generer.MODELES["v2"]
    assert modele == "eleven_multilingual_v2"
    prix = lambda e: int(round(len(lectures.lecture("de", e["texte"])) * taux))
    for e in a_faire:
        print("%s %4d  %s" % (e["id"], prix(e), e["texte"]))
    total = sum(prix(e) for e in a_faire)
    print("\n%d fichiers, environ %d credits" % (len(a_faire), total))
    plafond = int(sys.argv[sys.argv.index("--plafond") + 1]) if "--plafond" in sys.argv else 0
    if "--a-blanc" in sys.argv or not a_faire:
        return
    if total > plafond:
        print("depasse le plafond de %d : rien n'est lance" % plafond)
        return
    cle = generer.cle_api()
    depense = 0
    for e in a_faire:
        octets = generer.synthetiser(lectures.lecture("de", e["texte"]), modele, cle)
        with open(os.path.join(generer.SORTIE, e["id"] + ".mp3"), "wb") as f:
            f.write(octets)
        depense += prix(e)
        print("  + %s.mp3 (%d o)" % (e["id"], len(octets)))
    print("depense : %d credits" % depense)


if __name__ == "__main__":
    main()
