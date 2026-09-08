# -*- coding: utf-8 -*-
"""Deuxieme tour : ce que la STABILITE change sous v3.

    python audio/essai_v3b.py

CE QU'ON A APPRIS AU PREMIER TOUR
    eleven_v3 fonctionne sur le compte, et il sonne mieux que
    eleven_multilingual_v2. Mais Jacques a trouve les balises << pas tres
    accentuees >>.

L'HYPOTHESE QU'ON TESTE ICI
    v3 ne lit pas stability comme une glissiere continue mais comme trois
    regimes : 0.0 Creative, 0.5 Natural, 1.0 Robust. Creative est le plus
    expressif ET le plus sensible aux balises. Le premier tour tournait a
    0.40 -- presque Natural. C'est peut-etre lui qui bridait tout.

    On refait donc la meme phrase, la meme balise, en ne changant QUE la
    stabilite. Si l'ecart est net, le reglage tenait la bride ; s'il est nul,
    l'hypothese est fausse et il faudra chercher ailleurs.

UNE SEULE VARIABLE A LA FOIS
    C'est la regle qu'on s'est donnee toute la journee sur les images, et
    elle vaut ici : meme voix, meme phrase, meme modele, meme balise. Seule
    la stabilite bouge.
"""
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                            # noqa: E402

SORTIE = os.path.join(RACINE, "audio", "a_ecouter_voix", "essai-v3")
ANNA = "92qyovlOYJE0EVmWB0fA"
PHRASE = "Gern geschehen. Viel Glück in Berlin!"

# nom, stability, style, texte
ESSAIS = [
    ("7-creative-sans-balise", 0.0, 0.45, PHRASE),
    ("8-creative-warmly",      0.0, 0.45, "[warmly] " + PHRASE),
    ("9-creative-style-haut",  0.0, 0.80, "[warmly] " + PHRASE),
    ("10-natural-warmly",      0.5, 0.45, "[warmly] " + PHRASE),
    # Une balise plus explicite : [warmly] est doux, celle-ci demande le geste.
    ("11-creative-smile-fort", 0.0, 0.80,
     "[warm, smiling, genuinely pleased] " + PHRASE),
]


def main():
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    cle = generer.cle_api()
    generer.VOIX = ANNA
    print("  %d essais, %d caracteres\n" % (len(ESSAIS), sum(len(t) for _, _, _, t in ESSAIS)))
    for nom, stab, style, texte in ESSAIS:
        generer.REGLAGES = {"stability": stab, "similarity_boost": 0.75,
                            "style": style, "use_speaker_boost": True}
        try:
            octets = generer.synthetiser(texte, "eleven_v3", cle)
        except Exception as e:
            print("  %-24s ECHEC : %s" % (nom, str(e)[:100]))
            continue
        open(os.path.join(SORTIE, nom + ".mp3"), "wb").write(octets)
        print("  %-24s stab %.1f  style %.2f  %6d octets" % (nom, stab, style, len(octets)))
    print("\n  Ecoute 8 contre 10 : c'est la stabilite seule.")
    print("  Puis 9 contre 8 : c'est le style seul.")
    print("  Puis 11 : la balise la plus explicite, tous curseurs ouverts.")


if __name__ == "__main__":
    main()
