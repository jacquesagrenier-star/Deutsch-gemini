# -*- coding: utf-8 -*-
"""Les collisions, mais avec de quoi les corriger.

    python tests/lot_collisions.py --langue tr --categorie adjectifs
    python tests/lot_collisions.py --langue tr --categorie noms --debut 40 --taille 20

`relecture_langue.py --collisions` DIT quelles cartes se marchent dessus. Il ne
dit pas dans quel FICHIER ni a quel NIVEAU chacune se trouve -- or c'est
exactement ce que `patch_langue.py` reclame pour ecrire la correction. Sans ces
deux informations, chaque ligne du rapport demande une fouille a la main.

Ce script les joint. Une ligne par mot allemand :

    adjectif.json B1 | korrekt | correct, exact | dogru

Les adjectifs et les verbes des chapitres VHS vivent dans themes.json, pas dans
adjectif.json ni verbe.json : le script le dit, au lieu de le laisser deviner.
"""
import argparse
import collections
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ou vit chaque categorie du rapport de collisions, et sous quelle cle.
CATEGORIES = {
    "adjectifs": ("adjectif.json", "adjektive", "mot"),
    "adverbes": ("adverbe.json", None, "mot"),
    "noms": ("themes.json", "mots", "mot"),
    "verbes": ("verbe.json", "verben", "infinitif"),
    "expressions": ("redewendung.json", None, "mot"),
}


def charger(nom):
    return json.load(io.open(os.path.join(RACINE, nom), encoding="utf-8"))


def entrees(categorie):
    """[(fichier, niveau, entree)] pour une categorie, THEMES COMPRIS."""
    fichier, cle_theme, _ = CATEGORIES[categorie]
    out = []
    if fichier == "themes.json":
        for t in charger("themes.json").get("themes", []):
            for m in t.get(cle_theme or "mots", []):
                out.append(("themes.json", t.get("niveau"), m))
        return out
    for niveau, liste in charger(fichier).items():
        if isinstance(liste, list):
            for m in liste:
                out.append((fichier, niveau, m))
    # Les adjectifs et les verbes des chapitres VHS sont dans themes.json :
    # sans cette seconde passe, une collision qui les touche resterait
    # introuvable et la correction viserait le mauvais fichier.
    if cle_theme:
        for t in charger("themes.json").get("themes", []):
            for m in t.get(cle_theme, []):
                out.append(("themes.json", t.get("niveau"), m))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--categorie", required=True, choices=sorted(CATEGORIES))
    ap.add_argument("--debut", type=int, default=0)
    ap.add_argument("--taille", type=int, default=25)
    a = ap.parse_args()

    _, _, champ = CATEGORIES[a.categorie]
    cle_trad = "traduction_" + a.langue

    # LES DECISIONS DEJA PRISES NE SE REPOSENT PAS. collisions-acceptees.txt
    # porte les cas ou la langue cible n'a REELLEMENT qu'un mot, valides devant
    # une locutrice native. Les remonter ici ferait re-trancher, et mal, ce qui
    # a deja ete tranche.
    acceptees = set()
    chemin = os.path.join(RACINE, "relecture_" + a.langue, "collisions-acceptees.txt")
    if os.path.isfile(chemin):
        for ligne in io.open(chemin, encoding="utf-8"):
            bouts = [b.strip() for b in ligne.strip().split("|", 2)]
            if len(bouts) == 3 and not ligne.startswith("#"):
                acceptees.add((bouts[0], bouts[1].lower()))

    par_reponse = collections.defaultdict(list)
    for fichier, niveau, m in entrees(a.categorie):
        rep = (m.get(cle_trad) or "").strip()
        if rep:
            par_reponse[rep.lower()].append((fichier, niveau, m))

    # Une collision = une reponse partagee par plusieurs mots allemands
    # DISTINCTS. Le meme mot present dans deux themes n'en est pas une.
    groupes = []
    for rep, liste in par_reponse.items():
        mots = {m.get(champ) for _, _, m in liste}
        if len(mots) > 1 and (a.categorie, rep) not in acceptees:
            groupes.append((rep, liste))
    groupes.sort(key=lambda g: (-len(g[1]), g[0]))

    print("# %s / %s : %d collisions" % (a.langue, a.categorie, len(groupes)))
    for rep, liste in groupes[a.debut:a.debut + a.taille]:
        print("\n## %s" % rep)
        vus = set()
        for fichier, niveau, m in liste:
            nom = m.get(champ)
            if nom in vus:
                continue
            vus.add(nom)
            print("   %-14s %-3s | %-22s | %s"
                  % (fichier, niveau or "", nom, m.get("traduction", "")))


if __name__ == "__main__":
    main()
