# -*- coding: utf-8 -*-
"""Inventaire des cles localStorage d'index.html, pour le demenagement.

Une nouvelle adresse est un nouveau site pour le navigateur : le localStorage
de l'ancienne adresse ne suit pas. Ce script dit, pour chaque cle, si elle
part dans la sauvegarde Firestore (syncProgressToCloud) et si elle en revient
(restoreProgressFromCloud). Celles qui ne font ni l'un ni l'autre ne vivent
que sur l'appareil.

    python demenagement/inventaire_cles.py

Lecture seule. Mesure par le texte : une cle est « sauvee » si son nom (ou la
constante qui le porte) apparait dans le corps de la fonction de sauvegarde.
C'est un indice solide, pas une preuve -- relire les cas limites a la main.
"""
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(ICI, "..", "index.html")


def corps_fonction(src, entete):
    """Le texte d'une fonction de premier niveau, de son entete a la suivante."""
    i = src.index(entete)
    m = re.compile(r"\n(?:async )?function |\nconst ").search(src, i + len(entete))
    return src[i:m.start() if m else len(src)]


def main():
    with open(HTML, encoding="utf-8") as f:
        src = f.read()

    # Constante -> nom de cle ("deutschAI_...").
    consts = dict(re.findall(r'const ([A-Z_]+)\s*=\s*"(deutschAI_[^"]*)"', src))
    # Cles ecrites en toutes lettres dans un appel localStorage.
    litterales = set(re.findall(r'localStorage\.(?:get|set|remove)Item\(\s*"(deutschAI_[^"]+)"', src))
    toutes = {}
    for c, nom in consts.items():
        toutes.setdefault(nom, set()).add(c)
    for nom in litterales:
        toutes.setdefault(nom, set())

    # Ne garder que les cles vraiment utilisees avec localStorage (une
    # constante peut nommer une cle de sessionStorage).
    def en_localstorage(nom, noms_const):
        if nom in litterales:
            return True
        for c in noms_const:
            if re.search(r"localStorage\.\w+Item\(\s*(?:directionScopedKey\()?" + c + r"\b", src):
                return True
        return False

    sauve = corps_fonction(src, "async function syncProgressToCloud(")
    restaure = corps_fonction(src, "async function restoreProgressFromCloud(")
    # La langue imposee, lue a la connexion par loadVhsKapitelAccessFlag.
    restaure += corps_fonction(src, "async function loadVhsKapitelAccessFlag(")

    # Cles sauvegardees par une fonction d'acces (getXp(), getStreakCount()...)
    # plutot que par leur nom : on les relie a la main, c'est court et lisible.
    via_fonction = {
        "XP_KEY": "getXp",
        "STREAK_KEY": "getStreakCount",
        "STREAK_FREEZE_KEY": "getStreakFreezes",
        "DAILY_GOAL_STORAGE_KEY": "getDailyGoalTarget",
        "DAILY_ACTIVITY_KEY": "getDailyActivityCount",
        "MY_REQUESTS_KEY": "loadMyRequests",
        "MY_VOCAB_KEY": "loadMyVocab",
        "UI_LANG_KEY": "getUiLang",
        "STORAGE_KEY": "progressionUtile(progress)",
    }
    via_restaure = {
        "STORAGE_KEY": "progressJson",
        "STREAK_FREEZE_KEY": "setStreakFreezes",
        "MOSAIQUE_CLE": "data.mosaique",
        "BADGES_KEY": "saveUnlockedBadges",
        "MY_VOCAB_KEY": "saveMyVocab",
    }

    def present(texte, nom, noms_const, table):
        if nom in texte:
            return True
        for c in noms_const:
            if re.search(r"\b" + c + r"\b", texte):
                return True
            if c in table and table[c] in texte:
                return True
        return False

    lignes = []
    for nom in sorted(toutes):
        noms_const = toutes[nom]
        if not en_localstorage(nom, noms_const):
            continue
        s = present(sauve, nom, noms_const, via_fonction)
        r = present(restaure, nom, noms_const, via_restaure)
        lignes.append((nom, "/".join(sorted(noms_const)) or "-", s, r))

    larg = max(len(l[0]) for l in lignes)
    print("cle".ljust(larg), " sauvee  restauree  constante")
    for nom, c, s, r in lignes:
        print(nom.ljust(larg), " ", "oui " if s else "NON ", "   ", "oui " if r else "NON ", "    ", c)
    seules = [l for l in lignes if not l[3]]
    print()
    print(len(lignes), "cles localStorage ;", len(seules), "ne reviennent pas du nuage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
