# -*- coding: utf-8 -*-
"""Repere les fichiers audio probablement rates, sans les ecouter.

    python audio/controler.py
    python audio/controler.py --niveaux A1,A2 --ecarts 20

POURQUOI CE SCRIPT EXISTE
    Personne ne reecoutera 5 260 fichiers. Mais un rate de synthese n'est pas
    « un peu moins bon » : c'est un mot avale, une phrase coupee, un silence.
    Or tout cela se voit dans la DUREE. A 64 kbit/s, le poids d'un MP3 est
    proportionnel a sa duree, et la duree d'une phrase allemande lue est, elle,
    tres regulierement proportionnelle a sa longueur en caracteres.

    ATTENTION AU RAPPORT OCTETS/CARACTERE : il ne marche pas.
    Chaque MP3 porte un cout fixe -- en-tete, silence de tete et de queue --
    d'environ 8 ko. Sur « weg », trois lettres, ce cout fixe EST le fichier :
    2 940 octets par caractere, contre 419 pour une phrase de quarante lettres.
    Classer par ce rapport ne trie donc pas les rates, il trie les textes du
    plus court au plus long. C'est exactement ce qu'il faisait avant cette
    correction, et il n'aurait jamais rien trouve.

    On ajuste donc une droite taille = fixe + pente x longueur sur l'ensemble
    du lot, et on regarde les ECARTS a cette droite. Un fichier tres au-dessous
    de sa prevision a perdu du texte ; tres au-dessus, il a ajoute un silence
    ou repete.

    Ce n'est PAS une mesure de qualite : une voix qui prononce mal un mot
    produit un fichier de taille parfaitement normale. C'est un filtre a
    accidents grossiers, a ecouter ensuite a la main -- une trentaine de
    fichiers, pas cinq mille.
"""
import argparse
import io
import json
import os
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "audio", "mp3")
MANIFESTE = os.path.join(RACINE, "audio", "manifest.json")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--niveaux", default="")
    p.add_argument("--ecarts", type=int, default=25,
                   help="combien de suspects afficher de chaque cote")
    a = p.parse_args()

    with io.open(MANIFESTE, encoding="utf-8") as f:
        entrees = json.load(f)
    if a.niveaux:
        niveaux = a.niveaux.split(",")
        entrees = [e for e in entrees if e["niveau"] in niveaux]

    mesures = []
    absents = 0
    for e in entrees:
        chemin = os.path.join(DOSSIER, e["id"] + ".mp3")
        if not os.path.exists(chemin):
            absents += 1
            continue
        n = len(e["texte"])
        mesures.append((n, os.path.getsize(chemin), e))

    if len(mesures) < 30:
        print("  trop peu de fichiers pour ajuster une droite.")
        return

    # Moindres carres, taille = fixe + pente x longueur.
    xs = [m[0] for m in mesures]
    ys = [m[1] for m in mesures]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    var = sum((x - mx) ** 2 for x in xs)
    pente = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / var
    fixe = my - pente * mx

    ecarts = []
    for n, taille, e in mesures:
        prevu = fixe + pente * n
        ecarts.append(((taille - prevu) / prevu, n, taille, prevu, e))

    print("  %d fichiers mesures (%d absents)" % (len(mesures), absents))
    print("  droite ajustee : %.0f octets fixes + %.0f par caractere\n"
          % (fixe, pente))

    ecarts.sort(key=lambda x: x[0])   # le dict final n'est pas comparable

    def montrer(liste):
        for r, n, taille, prevu, e in liste:
            print("    %+5.0f%%  %6d o (prevu %6d)  %-4s %s"
                  % (r * 100, taille, prevu, e["niveau"], e["texte"][:52]))

    print("  LES PLUS COURTS pour leur texte — un mot avale, une phrase coupee")
    montrer(ecarts[:a.ecarts])
    print("\n  LES PLUS LONGS — un silence ajoute, une repetition")
    montrer(ecarts[-a.ecarts:][::-1])

    # Perdre 40 % de la duree prevue, ce n'est plus une variation de debit :
    # c'est du texte qui n'a pas ete dit.
    graves = [x for x in ecarts if x[0] < -0.40]
    print("\n  a plus de 40 %% sous la prevision : %d fichier(s)" % len(graves))
    for r, n, taille, prevu, e in graves[:20]:
        print("    %s  %+.0f%%  %s" % (e["id"], r * 100, e["texte"][:56]))
    if graves:
        print("\n  Pour les refaire : supprime ces .mp3 de audio/mp3/ et relance")
        print("  la generation, elle ne refait que ce qui manque.")


if __name__ == "__main__":
    main()
