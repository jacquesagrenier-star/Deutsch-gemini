# -*- coding: utf-8 -*-
"""Ou manque-t-il une traduction, dans TOUS les fichiers de donnees ?

    python tests/trous_langue.py
    python tests/trous_langue.py --detail

lot_langue.py ne connait que les cinq fichiers de cartes, et lot_exos.py que
exercices.json. Restent des poches entieres que personne ne compte : les verbes
et les adjectifs des chapitres VHS, les listes d'examen, la grammaire. C'est
Hatice qui les a trouvees a l'usage, pas un controle -- d'ou ce script.

LA REGLE : un champ est « du a la traduction » quand sa version FRANCAISE
existe et n'est pas vide. On ne reclame donc jamais une traduction pour un
champ que le francais lui-meme n'a pas -- ce serait inventer du contenu.
"""
import argparse
import collections
import io
import json
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = ["tr", "uk", "fa"]

# Les bases traduisibles, quel que soit le fichier. « traduction » et
# « exemple » couvrent le vocabulaire ; les autres viennent des verbes, des
# exercices et des epreuves d'examen.
BASES = ["traduction", "exemple", "perfekt", "praeteritum", "konjunktiv2",
         "kategorie", "question", "translation", "hint", "explanation",
         "frage", "aufgabe", "consigne", "trad", "erkl", "options", "correct"]

# DEUX CONVENTIONS DE SUFFIXE COEXISTENT, parfois dans le meme objet :
# « translation_tr » avec un souligne, mais « optionsTr » en casse chameau.
# Chercher options_tr ne trouve donc jamais rien et fait crier le script sur
# 965 champs qui sont la.
CHAMEAU = {"options": {"tr": "optionsTr", "uk": "optionsUk", "fa": "optionsFa",
                       "en": "optionsEn"},
           "correct": {"tr": "correctTr", "uk": "correctUk", "fa": "correctFa",
                       "en": "correctEn"}}

# Le francais de ces bases-la n'a PAS de suffixe : « traduction » est deja le
# francais, « exemple » est l'ALLEMAND et son francais est « exemple_fr ».
FR_SUFFIXE = {"exemple", "perfekt", "praeteritum", "konjunktiv2", "frage",
              "aufgabe", "consigne", "trad", "erkl"}


def cle_fr(base):
    return base + "_fr" if base in FR_SUFFIXE else base


def cle_langue(base, langue):
    if base in CHAMEAU:
        return CHAMEAU[base][langue]
    return base + "_" + langue


def parcourir(objet, visiteur):
    """Descend dans n'importe quelle forme de JSON et livre chaque dict."""
    if isinstance(objet, dict):
        visiteur(objet)
        for v in objet.values():
            parcourir(v, visiteur)
    elif isinstance(objet, list):
        for v in objet:
            parcourir(v, visiteur)


def analyser(chemin):
    """{(base, langue): (manquants, dus)} pour un fichier."""
    with io.open(chemin, encoding="utf-8") as f:
        donnees = json.load(f)
    compte = collections.Counter()
    dus = collections.Counter()
    exemples = {}

    def visiter(d):
        for base in BASES:
            fr = d.get(cle_fr(base))
            if not fr:
                continue
            # L'ANGLAIS SERT DE PREUVE que le champ est traduisible. Sans ce
            # garde-fou, « kategorie » d'adverbe.json est reclame 470 fois --
            # or sa valeur est « Zeit », un identifiant allemand dont le
            # libelle affiche vit dans ADVERB_CATEGORIES, pas dans la donnee.
            if not d.get(cle_langue(base, "en")):
                continue
            for lg in LANGUES:
                dus[(base, lg)] += 1
                if not d.get(cle_langue(base, lg)):
                    compte[(base, lg)] += 1
                    exemples.setdefault((base, lg), d)

    parcourir(donnees, visiter)
    return compte, dus, exemples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detail", action="store_true",
                    help="montre une entree incomplete par trou trouve")
    a = ap.parse_args()

    fichiers = ["themes.json", "verbe.json", "adjectif.json", "adverbe.json",
                "redewendung.json", "funktionswort.json", "exercices.json",
                "pruefung.json", "grammaire.json", "synonymes.json"]

    total_manque = 0
    for nom in fichiers:
        chemin = os.path.join(RACINE, nom)
        if not os.path.exists(chemin):
            continue
        compte, dus, exemples = analyser(chemin)
        trous = {k: v for k, v in compte.items() if v}
        if not trous:
            print("  %-20s complet" % nom)
            continue
        print("  %-20s" % nom)
        for (base, lg), n in sorted(trous.items(), key=lambda kv: -kv[1]):
            total_manque += n
            print("      %-14s %-3s %5d manquants sur %d"
                  % (base, lg, n, dus[(base, lg)]))
            if a.detail:
                d = exemples[(base, lg)]
                nom_entree = d.get("mot") or d.get("infinitif") or d.get("question") or ""
                print("          ex. %s" % str(nom_entree)[:70])
    print("  ---")
    print("  %d champ(s) de traduction manquant(s) au total" % total_manque)


if __name__ == "__main__":
    main()
