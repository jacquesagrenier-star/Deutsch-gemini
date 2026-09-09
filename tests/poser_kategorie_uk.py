# -*- coding: utf-8 -*-
"""Pose kategorie_uk (et l'anglais reste vide) sur funktionswort.json.

POURQUOI UN SCRIPT DEDIE, ET PAS PATCH_LANGUE. Ce champ-ci n'est pas une
traduction de carte mais un LIBELLE DE CATEGORIE : 161 entrees ne portent que
25 valeurs distinctes. Les poser une par une invite a la faute de frappe et
ferait dire la meme regle avec des mots differents selon l'entree. On traduit
donc la table, une fois, et on l'applique.

LE GARDE-FOU D'ALLER-RETOUR est le meme que partout ici : le fichier est relu
apres ecriture et compare a ce qu'on croyait ecrire. Le turc a perdu 673
entrees parce qu'une ecriture non relue avait pose un caractere par entree,
sans que rien echoue -- le champ existait et n'etait pas vide.

    python tests/poser_kategorie_uk.py --etat
    python tests/poser_kategorie_uk.py --poser
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIER = os.path.join(RACINE, "funktionswort.json")

# Les valeurs allemandes (Dativ, Akkusativ, Genitiv, Wechselpraeposition, les
# noms de series de nombres) sont GARDEES TELLES QUELLES, comme le turc et le
# persan le font : ce sont les etiquettes que l'apprenant verra dans sa
# grammaire allemande. Les traduire lui donnerait un mot qu'il ne retrouvera
# nulle part.
UK = {
    "Grundzahlen — compter":                          "Grundzahlen — рахувати",
    "Zehner — les dizaines":                          "Zehner — десятки",
    "Nombres composés — l'ordre s'inverse":           "Складені числівники — порядок міняється",
    "Grands nombres":                                 "Великі числа",
    "Millésimes":                                     "Роки",
    "Ordinaux — premier, deuxième…":                  "Порядкові числівники — перший, другий…",
    "toujours Dativ":                                 "завжди Dativ",
    "toujours Akkusativ":                             "завжди Akkusativ",
    "toujours Genitiv":                               "завжди Genitiv",
    "Wechselpräposition (Wo=Dativ, Wohin=Akkusativ)": "Wechselpräposition (Wo=Dativ, Wohin=Akkusativ)",
    "conjonction de subordination":                   "підрядний сполучник",
    "conjonction de coordination":                    "сурядний сполучник",
    "particule modale":                               "модальна частка",
    "article défini":                                 "означений артикль",
    "article indéfini":                               "неозначений артикль",
    "déterminant indéfini":                           "неозначений визначник",
    "déterminant négatif":                            "заперечний визначник",
    "déterminant démonstratif":                       "вказівний визначник",
    "pronom personnel":                               "особовий займенник",
    "pronom réfléchi":                                "зворотний займенник",
    "pronom réciproque":                              "взаємний займенник",
    "pronom démonstratif":                            "вказівний займенник",
    "pronom indéfini":                                "неозначений займенник",
    "pronom interrogatif":                            "питальний займенник",
    "pronom d'insistance":                            "підсилювальний займенник",
}

# Trois categories n'avaient AUCUN libelle anglais -- champ present, valeur
# vide, ce qu'aucun compteur d'entrees ne signale.
EN_MANQUANTS = {
    "conjonction de subordination": "subordinating conjunction",
    "conjonction de coordination":  "coordinating conjunction",
    "particule modale":             "modal particle",
}


def entrees(x, out):
    if isinstance(x, dict):
        if "kategorie" in x:
            out.append(x)
        else:
            for v in x.values():
                entrees(v, out)
    elif isinstance(x, list):
        for v in x:
            entrees(v, out)
    return out


def charger():
    return json.load(io.open(FICHIER, encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--poser", action="store_true")
    a = ap.parse_args()

    d = charger()
    ents = entrees(d, [])
    cats = sorted({e["kategorie"] for e in ents})

    inconnues = [c for c in cats if c not in UK]
    if inconnues:
        print("ARRET : %d categorie(s) sans traduction ukrainienne." % len(inconnues))
        for c in inconnues:
            print("   " + c)
        print("Les ajouter a UK plutot que de poser un champ vide.")
        return 2

    manque_uk = sum(1 for e in ents if not e.get("kategorie_uk"))
    manque_en = sum(1 for e in ents if not e.get("kategorie_en"))
    print("%d entrees, %d categories distinctes" % (len(ents), len(cats)))
    print("   sans kategorie_uk : %d" % manque_uk)
    print("   sans kategorie_en : %d" % manque_en)

    if a.etat or not a.poser:
        return 0

    poses_uk = poses_en = 0
    for e in ents:
        k = e["kategorie"]
        if not e.get("kategorie_uk"):
            e["kategorie_uk"] = UK[k]
            poses_uk += 1
        if not e.get("kategorie_en") and k in EN_MANQUANTS:
            e["kategorie_en"] = EN_MANQUANTS[k]
            poses_en += 1

    io.open(FICHIER, "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    # --- GARDE-FOU : on relit ce qu'on vient d'ecrire ---
    relu = entrees(charger(), [])
    if len(relu) != len(ents):
        print("ECHEC : %d entrees relues pour %d ecrites." % (len(relu), len(ents)))
        return 1
    fautes = []
    for e in relu:
        k = e["kategorie"]
        if e.get("kategorie_uk") != UK[k]:
            fautes.append("%s -> %r" % (k, e.get("kategorie_uk")))
        if k in EN_MANQUANTS and not e.get("kategorie_en"):
            fautes.append("%s : anglais toujours vide" % k)
    if fautes:
        print("ECHEC a la relecture : %d ecart(s)." % len(fautes))
        for f in fautes[:10]:
            print("   " + f)
        return 1

    print("Pose et RELU : %d kategorie_uk, %d kategorie_en." % (poses_uk, poses_en))
    print("Toutes les entrees relues portent la valeur attendue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
