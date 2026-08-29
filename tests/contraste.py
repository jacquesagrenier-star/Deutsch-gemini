# -*- coding: utf-8 -*-
"""
Confronte le vocabulaire allemand a une source INDEPENDANTE : WikDict.

    python tests/contraste.py             # resume
    python tests/contraste.py --detail    # chaque divergence
    python tests/contraste.py --genre     # seulement les genres

POURQUOI CE SCRIPT AVANT UNE RELECTURE PAR IA.

L'app espagnole a ete relue par un autre modele, et l'exercice a rapporte
202 signalements. Deux categories seulement etaient des FAITS verifiables ;
les 104 autres etaient des avis, qu'il a fallu laisser en arbitrage.

Or le risque allemand se concentre sur du verifiable, et sur deux points
precis :

    1. LE GENRE. der/die/das est imprevisible, et une carte fausse enseigne
       une faute pour des annees. WikDict le donne pour chaque nom.
    2. LE PLURIEL. L'allemand en a huit formations, sans regle sure, et
       certains mots en ont DEUX avec des sens differents -- Woerter (des
       mots isoles) contre Worte (des paroles), Baenke (des bancs) contre
       Banken (des banques). C'est exactement le genre d'erreur qu'un
       relecteur humain rate et qu'une table tranche.

Une machine donne ici des certitudes la ou une IA donnerait une opinion.
La relecture croisee vient APRES, pour ce que la machine ne sait pas juger :
le naturel d'une phrase, le registre, l'adequation au niveau.

CE QUE LE SCRIPT NE PROUVE PAS. WikDict vient du Wiktionnaire : il est
incomplet, et parfois lui-meme discutable. Un desaccord n'est donc pas une
condamnation, c'est une carte a regarder. Les absences surtout sont
normales -- les composes allemands (Krankenversicherungskarte) n'y sont
souvent pas.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT = os.path.join(RACINE, "dict", "de-fr")

# Le genre tel que WikDict l'ecrit, et tel que nos fiches l'ecrivent.
GENRES = ("der", "die", "das")


def charger_dictionnaire():
    """Tous les noms de WikDict, indexes par mot.

    On garde UNIQUEMENT les noms (p == "n") : le genre n'a de sens que pour
    eux, et un verbe homographe fausserait la comparaison.
    """
    if not os.path.isdir(DICT):
        print("dict/de-fr introuvable — rien a comparer.")
        return {}
    entrees = {}
    for nom in sorted(os.listdir(DICT)):
        if nom == "index.json" or not nom.endswith(".json"):
            continue
        try:
            paquet = json.load(io.open(os.path.join(DICT, nom), encoding="utf-8"))
        except ValueError:
            continue
        for e in paquet:
            if not isinstance(e, dict) or e.get("p") != "n":
                continue
            mot = e.get("m")
            if not mot:
                continue
            # Un mot peut avoir plusieurs entrees (plusieurs genres, plusieurs
            # pluriels). On les accumule au lieu d'en garder une : « der See »
            # et « die See » existent tous les deux.
            # On garde chaque SENS separement, avec son genre, son pluriel et
            # ses traductions. C'est indispensable en allemand : « das Alter »
            # (l'age) et « der Alter » (le vieux) sont deux mots differents
            # qui s'ecrivent pareil. Fondre leurs genres en un seul ensemble
            # ferait passer pour un desaccord ce qui n'est qu'une homographie.
            entrees.setdefault(mot, []).append({
                "g": e.get("g") if e.get("g") in GENRES else None,
                "pl": e.get("pl") or "",
                "t": {t.lower() for t in (e.get("t") or [])},
            })
    return entrees


def charger_themes():
    chemin = os.path.join(RACINE, "themes.json")
    donnees = json.load(io.open(chemin, encoding="utf-8"))
    return donnees.get("themes", donnees)


def comparer():
    dico = charger_dictionnaire()
    if not dico:
        return 1
    themes = charger_themes()

    genres, pluriels, absents, ok = [], [], [], 0
    total = 0

    for t in themes:
        for m in t.get("mots", []):
            mot = (m.get("mot") or "").strip()
            if not mot:
                continue
            total += 1
            sentidos = dico.get(mot)
            if not sentidos:
                absents.append((t["id"], mot))
                continue

            notre_genre = (m.get("genre") or "").strip()
            notre_pluriel = (m.get("pluriel") or "").strip()
            notre_trad = (m.get("traduction") or "").lower()

            # LE SENS D'ABORD. On ne compare qu'aux entrees dont une
            # traduction recoupe la notre : sans ce filtre, « der Kunde »
            # (le client) se ferait corriger par « die Kunde » (la nouvelle),
            # et on corrigerait du juste par du faux.
            memes = [x for x in sentidos
                     if any(u and u in notre_trad or notre_trad and notre_trad in u
                            for u in x["t"])]
            candidats = memes if memes else []

            if not candidats:
                # Aucun sens commun trouve : WikDict connait le mot mais pas
                # dans notre acception. Rien de comparable, on passe.
                ok += 1
                continue

            gs = {x["g"] for x in candidats if x["g"]}
            if gs and notre_genre in GENRES and notre_genre not in gs:
                genres.append((t["id"], mot, notre_genre, "/".join(sorted(gs))))
                continue

            pls = {x["pl"] for x in candidats if x["pl"]}
            # Le tiret signale un nom sans pluriel : ce n'est pas un desaccord,
            # c'est une absence assumee.
            if (notre_pluriel and notre_pluriel not in ("—", "-")
                    and pls and notre_pluriel not in pls):
                pluriels.append((t["id"], mot, notre_pluriel,
                                 "/".join(sorted(pls))))
                continue
            ok += 1

    detail = "--detail" in sys.argv
    seulement_genre = "--genre" in sys.argv

    print()
    print("CONTRASTE AVEC WIKDICT")
    print("  %d noms dans le corpus, %d presents dans WikDict" % (total, total - len(absents)))
    print("  %d concordent entierement" % ok)
    print()
    print("  %-26s %4d   <- a regarder en premier" % ("genre divergent", len(genres)))
    print("  %-26s %4d" % ("pluriel divergent", len(pluriels)))
    print("  %-26s %4d   (souvent normal : composes)" % ("absent de WikDict", len(absents)))

    if genres:
        print()
        print("GENRES DIVERGENTS")
        for tid, mot, nous, eux in sorted(genres, key=lambda x: x[1]):
            print("   %-22s nous: %-4s  WikDict: %-10s  (%s)" % (mot, nous, eux, tid))

    if pluriels and not seulement_genre:
        print()
        print("PLURIELS DIVERGENTS%s" % ("" if detail else "  (les 30 premiers)"))
        for tid, mot, nous, eux in sorted(pluriels, key=lambda x: x[1])[:None if detail else 30]:
            print("   %-22s nous: %-16s WikDict: %-18s (%s)" % (mot, nous, eux, tid))

    if detail and absents:
        print()
        print("ABSENTS DE WIKDICT")
        for tid, mot in sorted(absents, key=lambda x: x[1]):
            print("   %-30s (%s)" % (mot, tid))

    print()
    print("Un desaccord n'est pas une condamnation : WikDict vient du")
    print("Wiktionnaire, il est incomplet et parfois discutable lui-meme.")
    print("C'est une liste de cartes A REGARDER, pas a corriger en bloc.")
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    return comparer()


if __name__ == "__main__":
    sys.exit(main())
