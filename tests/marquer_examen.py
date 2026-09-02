# -*- coding: utf-8 -*-
"""Pose le champ `pruefung` sur les mots du cours qui figurent aux listes officielles.

    python tests/marquer_examen.py --verifier    # ce qui serait marque
    python tests/marquer_examen.py               # ecrit

POURQUOI UN CHAMP ET PAS UN THEME. Le premier reflexe serait de creer un theme
« Preparation B1 » et d'y ranger les mots. Ce serait une erreur : « Anruf »
appartient a la communication, « Brille » au corps, « Baeckerei » a la ville.
Les sortir de leur theme pour les mettre dans un theme d'examen appauvrit le
cours, et personne ne revise « le vocabulaire de l'examen » comme on revise un
champ de sens.

Un CHAMP, lui, se pose sur le mot la ou il est deja. La tuile filtre dessus a
travers tous les themes et toutes les categories, exactement comme le mode
Ecoute construit sa sequence -- et les cartes gardent leur place.

CE QUE CA CHANGE IMMEDIATEMENT. 1 728 mots du cours figurent deja aux listes.
Les marquer donne a la tuile un contenu des aujourd'hui, au lieu d'attendre que
les 1 332 manquants soient ecrits. La tuile part a la moitie et grossit a
chaque lot ajoute.

LA VALEUR EST UNE LISTE, PAS UN BOOLEEN : ["dtz", "b1", "a2"]. Un mot present
aux trois est du noyau ; un mot present a une seule est peut-etre specifique a
cet examen. La tuile pourra proposer « le noyau » ou « tout », et l'arbitrage
des cas douteux reste possible plus tard sans revenir sur les donnees.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMENS = os.path.join(RACINE, "examens")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langue as L                                          # noqa: E402

# nom du fichier de liste -> etiquette portee par le champ
ETIQUETTES = {"dtz": "dtz", "goethe_b1": "b1", "goethe_a2": "a2"}

CHAMP = "pruefung"


def listes():
    out = {}
    for nom, etiquette in ETIQUETTES.items():
        chemin = os.path.join(EXAMENS, nom + ".json")
        if os.path.isfile(chemin):
            out[etiquette] = set(json.load(io.open(chemin, encoding="utf-8"))["mots"])
    return out


def serialiser(donnees, saut_final):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def marquer(verifier_seulement):
    """Meme garde-fou d'aller-retour que patch_langue.py : si le fichier ne se
    reproduit pas a l'octet pres, on n'ecrit rien. Un reformatage silencieux de
    2 Mo de JSON rendrait le diff illisible et la modification introuvable."""
    ls = listes()
    if not ls:
        print("Aucune liste extraite. Lancer tests/listes_examen.py --extraire.")
        return 1

    total = 0
    for categorie, (fichier, cle) in L.FICHIERS.items():
        chemin = os.path.join(RACINE, fichier)
        brut = io.open(chemin, encoding="utf-8", newline="").read()
        donnees = json.loads(brut)
        saut = brut.endswith("\n")
        if serialiser(donnees, saut) != brut:
            print("  ! %s ne se reproduit pas a l'identique -- ignore" % fichier)
            continue

        # Les mots, quelle que soit la forme du fichier.
        if fichier == "themes.json":
            entrees = [m for t in donnees.get("themes", donnees)
                       for m in t.get("mots", [])]
        else:
            entrees = [m for n in L.NIVEAUX for m in donnees.get(n, [])]

        poses = 0
        for m in entrees:
            mot = (m.get(cle) or "").strip()
            if not mot:
                continue
            etiquettes = sorted(e for e, s in ls.items() if mot in s)
            if not etiquettes:
                # Un mot qui n'y est plus perd sa marque : les listes peuvent
                # etre reextraites, et une marque perimee est pire qu'absente.
                if m.pop(CHAMP, None) is not None:
                    poses += 1
                continue
            if m.get(CHAMP) != etiquettes:
                m[CHAMP] = etiquettes
                poses += 1

        print("  %-18s %4d mot(s) marque(s) sur %d" % (fichier, poses, len(entrees)))
        total += poses
        if not verifier_seulement and poses:
            with io.open(chemin, "w", encoding="utf-8", newline="") as f:
                f.write(serialiser(donnees, saut))

    print()
    print("  %d champ(s) `%s` %s" % (total, CHAMP,
                                     "a poser" if verifier_seulement else "poses"))
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return marquer("--verifier" in sys.argv)


if __name__ == "__main__":
    sys.exit(main())
