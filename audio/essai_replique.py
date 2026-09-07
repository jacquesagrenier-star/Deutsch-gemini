# -*- coding: utf-8 -*-
"""Fabrique l'audio d'UNE replique, pret a televerser chez HeyGen.

    python audio/essai_replique.py --voix <voice_id> --plan 3
    python audio/essai_replique.py --voix <voice_id> --texte "Guten Tag."

POURQUOI CE SCRIPT PLUTOT QUE L'INTERFACE ELEVENLABS
    Le fichier telecharge depuis le site sort au niveau brut d'ElevenLabs,
    quelque part entre -7 et -15 dBFS selon la voix. Or tout le corpus de
    Wortando est egalise a -14 LUFS par audio/normaliser.py. Une scene video
    montee sur un fichier brut sonnerait plus fort ou plus faible que le reste
    de l'application, et personne ne saurait pourquoi -- on accuserait la
    video, alors que ce serait le niveau.

    Ce script fait donc les deux d'un coup : meme modele, memes reglages et
    meme graine que la production, puis la meme egalisation.

CE QU'IL FAUT SAVOIR SUR LE TEST HEYGEN
    Le plan 3 dit « Entschuldigung, wo ist die Gepaeckausgabe? ». Ce n'est pas
    une replique au hasard : « Gepaeckausgabe » est un compose long avec un
    umlaut et un groupe ck, exactement la ou une synchronisation labiale casse.
    Un essai sur « Guten Tag » ne prouverait rien.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))

import generer                                            # noqa: E402
import normaliser                                         # noqa: E402

SORTIE = os.path.join(RACINE, "audio", "essai_heygen")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voix", required=True, help="voice_id ElevenLabs")
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--plan", type=int, help="numero du plan dans la scene")
    ap.add_argument("--texte", help="texte libre, au lieu d'un plan")
    ap.add_argument("--modele", default="v2", choices=sorted(generer.MODELES))
    ap.add_argument("--nom", default=None, help="nom du fichier de sortie")
    a = ap.parse_args()

    if not a.texte and not a.plan:
        sys.exit("  Donne --plan ou --texte.")

    if a.texte:
        texte, etiquette = a.texte, "libre"
    else:
        d = json.load(io.open(
            os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
        plans = [p for p in d["plans"] if p["n"] == a.plan]
        if not plans:
            sys.exit("  Le plan %d n'existe pas dans %s." % (a.plan, a.scene))
        texte = plans[0]["de"]
        etiquette = "%s-plan%02d" % (a.scene, a.plan)

    # Sans egalisation le fichier ne sonne pas comme le reste de l'app. On
    # s'arrete plutot que de livrer un audio au mauvais niveau : il finirait
    # dans une video, et une video ne se recorrige pas d'un coup de filtre.
    normaliser.FF = normaliser.ffmpeg()
    if not normaliser.FF:
        sys.exit("  ffmpeg est indispensable : le corpus est a -14 LUFS et ce\n"
                 "  fichier doit l'etre aussi, sinon la scene sonnera a cote\n"
                 "  du reste de l'application. Rien n'a ete produit.")

    cle = generer.cle_api()
    modele, cout = generer.MODELES[a.modele]
    print("  « %s »" % texte)
    print("  %d caracteres, environ %d credits" % (len(texte), int(len(texte) * cout)))

    avant = generer.VOIX
    generer.VOIX = a.voix
    try:
        octets = generer.synthetiser(texte, modele, cle)
    finally:
        generer.VOIX = avant

    os.makedirs(SORTIE, exist_ok=True)
    nom = (a.nom or etiquette) + ".mp3"
    brut = os.path.join(SORTIE, "_brut-" + nom)
    fini = os.path.join(SORTIE, nom)
    io.open(brut, "wb").write(octets)
    normaliser.normaliser(brut, fini)

    print("\n  %s" % fini)
    print("  sonie : %s" % normaliser.mesurer(fini))
    print("\n  A televerser chez HeyGen : dans le reglage de voix de la video,")
    print("  choisir « Audio » plutot qu'un texte a lire, et deposer ce fichier.")
    print("  C'est l'equivalent, dans l'editeur, du audio_url de l'API.")


if __name__ == "__main__":
    main()
