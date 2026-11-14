# -*- coding: utf-8 -*-
"""L'index du corpus GENERAL de l'allemand, pour savoir si un mot des Soins y est deja.

Regle du plan (pflege/PLAN.md, § 3) : un mot deja au corpus n'est PAS duplique ;
le theme des Soins le REPREND (meme carte, meme progression) avec une phrase
d'exemple de soins en plus. Cet index sert au constructeur (resoudre une reprise)
et au controle (refuser un doublon).

Lu, jamais ecrit : themes.json (noms, et les verbes / adjectifs des chapitres VHS),
verbe.json, adjectif.json, adverbe.json, redewendung.json, funktionswort.json.
"""
import io
import json
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ARTICLES = ("der ", "die ", "das ", "den ", "dem ", "des ")


def cle(texte, garder_sich=False):
    """La forme comparable d'une entree : minuscules, sans article, sans « sich »
    (sauf garder_sich : « sich übergeben » n'est pas « übergeben »), sans (Pl.),
    sans ponctuation finale, espaces reduites."""
    t = (texte or "").strip().lower()
    t = t.replace("’", "'").replace("„", "").replace("“", "").replace('"', "")
    t = re.sub(r"\(pl\.\)", "", t)
    t = re.sub(r"[.!?…,;:]+$", "", t.strip())
    for a in ARTICLES:
        if t.startswith(a):
            t = t[len(a):]
            break
    if t.startswith("sich ") and not garder_sich:
        t = t[5:]
    return re.sub(r"\s+", " ", t).strip()


def _lire(nom):
    with io.open(os.path.join(RACINE, nom), encoding="utf-8") as f:
        return json.load(f)


_INDEX = None


def index():
    """{cle: [ {fichier, ou, mot, type, niveau, traduction} ]} sur tout le corpus general."""
    global _INDEX
    if _INDEX is not None:
        return _INDEX
    ix = {}

    def ajouter(texte, fichier, ou, typ, niveau, trad):
        ix.setdefault(cle(texte), []).append(
            {"fichier": fichier, "ou": ou, "mot": texte, "type": typ, "niveau": niveau, "traduction": trad})

    for th in _lire("themes.json")["themes"]:
        for m in th.get("mots", []):
            ajouter(m["mot"], "themes.json", th["id"], "nom", th.get("niveau"), m.get("traduction"))
        for v in th.get("verben", []):
            ajouter(v["infinitif"], "themes.json", th["id"], "verbe", th.get("niveau"), v.get("traduction"))
        for a in th.get("adjektive", []):
            ajouter(a["mot"], "themes.json", th["id"], "adjectif", th.get("niveau"), a.get("traduction"))
    for niv, liste in _lire("verbe.json").items():
        if isinstance(liste, list):
            for v in liste:
                ajouter(v["infinitif"], "verbe.json", niv, "verbe", niv, v.get("traduction"))
    for nom, typ in (("adjectif.json", "adjectif"), ("adverbe.json", "adverbe"), ("redewendung.json", "expression")):
        for niv, liste in _lire(nom).items():
            if isinstance(liste, list):
                for x in liste:
                    ajouter(x["mot"], nom, niv, typ, niv, x.get("traduction"))
    for cat, liste in _lire("funktionswort.json").items():
        if isinstance(liste, list):
            for x in liste:
                if isinstance(x, dict) and x.get("mot"):
                    ajouter(x["mot"], "funktionswort.json", cat, "mot-outil", x.get("niveau"), x.get("traduction"))
    _INDEX = ix
    return ix


def chercher(texte, typ=None):
    """Les fiches du corpus pour ce texte (filtrees par type si donne)."""
    r = index().get(cle(texte), [])
    if typ:
        r = [x for x in r if x["type"] == typ]
    return r


if __name__ == "__main__":
    import sys
    for mot in sys.argv[1:]:
        print(mot, "->", chercher(mot) or "absent")
