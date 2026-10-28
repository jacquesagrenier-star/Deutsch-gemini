# -*- coding: utf-8 -*-
"""Le comparatif A L'AVEUGLE des voix anglaises, PRET mais pas produit.

    python anglais/outils/echantillons_voix.py --variante us              # dit ce que ca couterait, ne depense rien
    python anglais/outils/echantillons_voix.py --variante gb --generer    # SEULEMENT avec l'accord de Jacques

Meme methode que le choix d'Aurora par Barbara (3 sept. 2026) : les memes
textes dits par chaque candidate, sonie egalisee, noms neutres VOIX-A, VOIX-B...,
une voix presentee deux fois (le doublon dit si le verdict tient), la cle
rangee a part. Tout le travail est celui d'audio/comparatif_voix.py, appele tel
quel : on ne lui donne que nos textes a la place des repliques d'une scene.

Les candidates : audio/candidats_anglais_<us|gb>.json.

LES TEXTES sont ceux qu'un cours fait entendre : un mot seul dans sa porteuse
(comme la production le fera), une phrase d'exemple, une question polie, une
heure et un prix -- deja en toutes lettres (audio/lectures : la voix ne doit
jamais recevoir de chiffres), et une phrase longue.
"""
import argparse, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "audio"))

TEXTES = {
    "us": ["Word: neighborhood.",
           "My family is very big.",
           "Excuse me, can we have the check, please?",
           "The train leaves at a quarter past nine, from platform two.",
           "This T-shirt costs twelve dollars and fifty cents.",
           "I'm sorry, I didn't understand. Could you say that again, a little more slowly?"],
    "gb": ["Word: neighbourhood.",
           "My family is very big.",
           "Excuse me, can we have the bill, please?",
           "The train leaves at a quarter past nine, from platform two.",
           "This T-shirt costs twelve pounds fifty.",
           "I'm sorry, I didn't understand. Could you say that again, a little more slowly?"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variante", choices=("us", "gb"), required=True)
    ap.add_argument("--generer", action="store_true",
                    help="produit vraiment les echantillons (DEPENSE des credits ElevenLabs)")
    a = ap.parse_args()
    import json, io
    cands = json.load(io.open(os.path.join(RACINE, "audio", "candidats_anglais_%s.json" % a.variante),
                              encoding="utf-8"))["voix"]
    textes = TEXTES[a.variante]
    car = sum(len(t) for t in textes) * (len(cands) + 1)      # + le doublon
    print("%d voix + 1 doublon x %d textes = %d caracteres, soit environ %d credits (multilingual v2)"
          % (len(cands), len(textes), car, car))
    for v in cands:
        print("   %s  %s" % (v["voice_id"], v["nom"]))
    if not a.generer:
        print("Rien n'est produit sans --generer (et sans l'accord de Jacques).")
        return
    import comparatif_voix as C
    C.repliques = lambda personnage, scene: list(textes)
    sys.argv = [sys.argv[0], "--personnage", "anglais_" + a.variante, "--modele", "v2"]
    C.main()


if __name__ == "__main__":
    main()
