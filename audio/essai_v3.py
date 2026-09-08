# -*- coding: utf-8 -*-
"""Essaie une replique avec Eleven v3 et ses balises, pour quelques centimes.

    python audio/essai_v3.py

POURQUOI CE SCRIPT EXISTE
    Le 8 septembre 2026, apres avoir baisse la stabilite a 0.40 et leve le
    style a 0.45, Jacques a ecoute la scene et a dit : << je ne peux pas dire
    que je sens vraiment une emotion dans la voix >>. Les reglages ne
    suffisent pas.

    Eleven v3 accepte des BALISES dans le texte -- [warmly], [laughs],
    [sighs] -- que le modele lit comme une direction de jeu et non comme des
    mots. eleven_multilingual_v2, celui du corpus, les prononcerait.

    Avant de regenerer dix-neuf repliques et de changer la chaine, on essaie
    UNE phrase. Six versions, moins de 400 caracteres en tout.

CE QU'ON COMPARE
    La meme replique d'Anna, six fois : sans balise en v2, sans balise en v3,
    puis quatre balises differentes en v3. Le fichier dit dans son nom ce
    qu'il contient, mais ECOUTEZ AVANT DE REGARDER LES NOMS -- c'est la seule
    facon de savoir si la balise s'entend vraiment ou si on l'imagine.

CE QUE CE SCRIPT NE FAIT PAS
    Il ne touche a rien. Ni au corpus, ni a la scene, ni a generer.py. Il
    ecrit six fichiers dans audio/a_ecouter_voix/essai-v3/ et s'arrete.
"""
import io
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                            # noqa: E402

SORTIE = os.path.join(RACINE, "audio", "a_ecouter_voix", "essai-v3")

# La replique la plus chaleureuse d'Anna : si une balise ne s'entend pas
# ici, elle ne s'entendra nulle part.
PHRASE = "Gern geschehen. Viel Glück in Berlin!"

# nom du fichier, modele, texte
ESSAIS = [
    ("1-v2-sans-balise",   "eleven_multilingual_v2", PHRASE),
    ("2-v3-sans-balise",   "eleven_v3",              PHRASE),
    ("3-v3-warmly",        "eleven_v3",              "[warmly] " + PHRASE),
    ("4-v3-smiling",       "eleven_v3",              "[smiling] " + PHRASE),
    ("5-v3-cheerful",      "eleven_v3",              "[cheerful] " + PHRASE),
    ("6-v3-laughs",        "eleven_v3",              "Gern geschehen. [laughs] Viel Glück in Berlin!"),
]

ANNA = "92qyovlOYJE0EVmWB0fA"


def main():
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    cle = generer.cle_api()

    # On force la voix d'Anna et des reglages expressifs, sans rien modifier
    # de facon durable : ce script s'execute et disparait.
    generer.VOIX = ANNA
    generer.REGLAGES = {"stability": 0.40, "similarity_boost": 0.75,
                        "style": 0.45, "use_speaker_boost": True}

    total = sum(len(t) for _, _, t in ESSAIS)
    print("  %d essais, %d caracteres au total\n" % (len(ESSAIS), total))

    for nom, modele, texte in ESSAIS:
        chemin = os.path.join(SORTIE, nom + ".mp3")
        try:
            octets = generer.synthetiser(texte, modele, cle)
        except Exception as e:
            # Un modele indisponible sur le forfait echoue ici, et c'est
            # precisement ce qu'on veut apprendre a moindre frais.
            print("  %-20s ECHEC : %s" % (nom, str(e)[:110]))
            continue
        open(chemin, "wb").write(octets)
        print("  %-20s %6d octets   %s" % (nom, len(octets), texte[:46]))

    print("\n  Ecoute : audio/a_ecouter_voix/essai-v3/")
    print("  Compare le 1 et le 2 d'abord : c'est l'ecart entre les deux modeles.")
    print("  Puis 3 a 6 : c'est ce que les balises ajoutent.")


if __name__ == "__main__":
    main()
