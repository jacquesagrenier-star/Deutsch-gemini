# -*- coding: utf-8 -*-
"""Pose le champ `registre` sur des mots nommes, dans n'importe lequel des JSON.

    python tests/poser_registre.py --verifier
    python tests/poser_registre.py

POURQUOI UNE TABLE EN DUR ET PAS UN LOT. Ces marques sont rares -- une
quarantaine de mots sur dix mille -- et elles se decident un par un, a la
lecture. Un fichier de lot pour six entrees couterait plus a maintenir qu'il
ne rapporte, et la table ci-dessous se relit d'un coup d'oeil.

LES QUATRE VALEURS RECONNUES, et rien d'autre :
    schriftlich        surtout a l'ecrit
    umgangssprachlich  familier
    oesterreichisch    surtout en Autriche
    schweizerisch      surtout en Suisse

Une cinquieme valeur ne serait affichee nulle part : usageMarkText() les
enumere, elle ne les devine pas. Le controle ci-dessous refuse donc ce qui
n'est pas dans la liste, plutot que d'ecrire une marque muette.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VALEURS = {"schriftlich", "umgangssprachlich", "oesterreichisch", "schweizerisch"}

# fichier -> { mot : registre }
MARQUES = {
    "verbe.json": {
        "grillieren": "schweizerisch",
        "parkieren": "schweizerisch",
    },
    "adjectif.json": {
        "cool": "umgangssprachlich",
        "okay": "umgangssprachlich",
        "chic": "umgangssprachlich",
    },
    "adverbe.json": {
        "naja": "umgangssprachlich",
        "rauf": "umgangssprachlich",
        "raus": "umgangssprachlich",
    },
    "funktionswort.json": {
        "bloß / nur": "umgangssprachlich",
    },
}

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]


def serialiser(donnees, saut_final):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def entrees(fichier, donnees):
    """Les entrees d'un fichier, quelle que soit sa forme."""
    if fichier == "themes.json":
        return [m for t in donnees.get("themes", donnees) for m in t.get("mots", [])]
    if fichier == "funktionswort.json":
        return [m for v in donnees.values() for m in v]
    return [m for n in NIVEAUX for m in donnees.get(n, [])]


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    verifier = "--verifier" in sys.argv
    total, absents = 0, []

    for fichier, table in MARQUES.items():
        mauvaises = {v for v in table.values()} - VALEURS
        if mauvaises:
            print("  ! %s : valeur inconnue -- %s" % (fichier, ", ".join(sorted(mauvaises))))
            return 1

        chemin = os.path.join(RACINE, fichier)
        brut = io.open(chemin, encoding="utf-8", newline="").read()
        donnees = json.loads(brut)
        saut = brut.endswith("\n")
        if serialiser(donnees, saut) != brut:
            print("  ! %s ne se reproduit pas a l'identique -- ignore" % fichier)
            continue

        cle = "infinitif" if fichier == "verbe.json" else "mot"
        poses, vus = 0, set()
        for m in entrees(fichier, donnees):
            mot = (m.get(cle) or "").strip()
            if mot in table:
                vus.add(mot)
                if m.get("registre") != table[mot]:
                    m["registre"] = table[mot]
                    poses += 1
        absents += ["%s / %s" % (fichier, m) for m in table if m not in vus]

        print("  %-20s %2d marque(s) %s" % (fichier, poses,
                                            "a poser" if verifier else "posee(s)"))
        total += poses
        if not verifier and poses:
            with io.open(chemin, "w", encoding="utf-8", newline="") as f:
                f.write(serialiser(donnees, saut))

    print()
    if absents:
        # Un mot de la table qui n'existe plus au cours est un signal, pas un
        # detail : la table a ete ecrite pour un corpus qui a change depuis.
        print("  ! %d mot(s) de la table introuvable(s) : %s"
              % (len(absents), ", ".join(absents)))
    print("  %d marque(s) au total" % total)
    return 1 if absents else 0


if __name__ == "__main__":
    sys.exit(main())
