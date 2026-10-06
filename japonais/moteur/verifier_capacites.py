# -*- coding: utf-8 -*-
"""Prototype du controle « aucune tuile sans capacite declaree ».

Ce que ferait tests/verifier.py une fois l'etape 2 du plan livree (voir
CONCEPTION.md, section 6). Ici il tourne en LECTURE SEULE sur l'index.html
actuel, pour mesurer le chantier : il liste chaque porte d'entree (tuile
d'accueil, option de panneau) et dit si elle declare une capacite.

Regles proposees :
  1. Toute tuile .orb (sauf les tuiles « moteur » listees dans PORTES_MOTEUR)
     porte data-capacite="...".
  2. Toute option de orbPanelData() porte cap:"..." OU herite de sa tuile.
  3. Chaque capacite citee existe dans capacites.json (le registre).
  4. Une capacite non declaree par la langue enseignee => la porte est
     retiree du DOM au demarrage (pas seulement cachee par CSS).

Aujourd'hui aucune porte ne declare rien : le script sort donc la liste a
annoter, c'est-a-dire la taille reelle de l'etape 2.

    python japonais/moteur/verifier_capacites.py [--registre capacites.json]
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))

# Portes qui appartiennent au moteur et valent pour toute langue.
PORTES_MOTEUR = {"seance", "monvocab"}


def main():
    registre_chemin = os.path.join(ICI, "capacites.json")
    if "--registre" in sys.argv:
        registre_chemin = sys.argv[sys.argv.index("--registre") + 1]
    registre = json.load(open(registre_chemin, encoding="utf-8"))
    connues = set(registre["capacites"])
    src = open(os.path.join(RACINE, "index.html"), encoding="utf-8").read().replace("\r\n", "\n")

    tuiles = re.findall(r'<div class="(orb[^"]*)" data-orbid="([^"]+)"([^>]*)>', src)
    sans = []
    for classes, ident, reste in tuiles:
        if ident in PORTES_MOTEUR:
            continue
        m = re.search(r'data-capacite="([^"]+)"', reste)
        if not m:
            sans.append((ident, classes))
        elif m.group(1) not in connues:
            print("ECHEC capacite inconnue %r sur la tuile %s" % (m.group(1), ident))

    debut = src.find("function orbPanelData(id){")
    corps = src[debut:src.index("\n}\n", debut)]
    options = re.findall(r'action:\s*"([A-Za-z0-9_]+)"', corps)
    options_cap = re.findall(r'cap:\s*"([a-z_]+)"', corps)

    # Proposition d'annotation : ce que la table de capacites.json attribue.
    attribution = registre.get("attribution_tuiles", {})
    print("Tuiles d'accueil      : %d (dont %d portes moteur)" % (len(tuiles), len(PORTES_MOTEUR)))
    print("Tuiles sans capacite  : %d" % len(sans))
    for ident, classes in sans:
        cap = attribution.get(ident, "?")
        print("   %-16s %-14s -> capacite proposee : %s" % (ident, classes.replace("orb ", ""), cap))
    print("Options de panneau    : %d actions, %d avec cap:" % (len(options), len(options_cap)))
    non_attribuees = [i for i, _ in sans if i not in attribution]
    print("Tuiles sans capacite proposee dans le registre : %d %s"
          % (len(non_attribuees), non_attribuees or ""))
    for lang, caps in registre["langues"].items():
        inconnues = [c for c in caps if c not in connues]
        if inconnues:
            print("ECHEC %s declare des capacites inconnues : %s" % (lang, inconnues))
        visibles = [i for i, _ in sans if attribution.get(i) in caps]
        print("Langue %-3s : %2d capacites, %2d tuiles de l'accueil actuel visibles"
              % (lang, len(caps), len(visibles)))
    # Etat attendu apres l'etape 2 : sans == [] ; aujourd'hui c'est la liste a faire.
    return 0


if __name__ == "__main__":
    sys.exit(main())
