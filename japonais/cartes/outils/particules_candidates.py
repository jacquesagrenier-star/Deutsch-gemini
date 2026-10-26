"""Phrases Tatoeba candidates pour les particules de particules.json.

Une phrase est candidate quand la particule y est un mot à elle seule (lignes B de
jpn_indices, le découpage du corpus Tanaka), qu'elle a une traduction française
liée directement, et qu'elle est courte (6 à 16 caractères). Les plus faciles
d'abord : celles dont tous les mots sont du N5 (ou du N4), d'après les fiches.

Usage : python japonais/cartes/outils/particules_candidates.py [--brut DOSSIER]
  -> japonais/cartes/lots/particules.json (à juger) et sources/particules-candidates.json
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict

ICI = os.path.dirname(os.path.abspath(__file__))
CARTES = os.path.dirname(ICI)
BRUT = os.path.join(os.path.expanduser("~"), ".wortando", "japonais-phrases", "japonais", "phrases", "brut")
RANG = {"N5": 5, "N4": 4, "N3": 3, "N2": 2, "N1": 1}
csv.field_size_limit(10 ** 8)


def formes(tok):
    """« 迄(まで){まで} » -> {"迄", "まで"} : le lemme, sa lecture et la forme écrite.
    Le corpus écrit en kanji des particules qu'on écrit en kana (迄, 丈, 頃, 程)."""
    lem = re.split(r"[\(\{\[~]", tok, maxsplit=1)[0]
    return {lem} | set(re.findall(r"\(([^)]*)\)", tok)) | set(re.findall(r"\{([^}]*)\}", tok))


def main():
    brut = sys.argv[sys.argv.index("--brut") + 1] if "--brut" in sys.argv else BRUT
    sys.stdout.reconfigure(encoding="utf-8")
    parts = json.load(open(os.path.join(CARTES, "particules.json"), encoding="utf-8"))["particules"]

    niveau_mot = {}
    for jlpt in ("n1", "n2", "n3", "n4", "n5"):     # le plus facile écrase
        for f in json.load(open(os.path.join(CARTES, "mots-%s.json" % jlpt), encoding="utf-8"))["entrees"]:
            for forme in (f["ecritures"]["kanji"]["v"], f["ecritures"]["kana"]["v"]):
                if forme:
                    niveau_mot[forme] = RANG[f["niveau"]]
    for p in parts:
        niveau_mot[p["mot"]] = 5

    def lire_tsv(nom):
        with open(os.path.join(brut, nom), encoding="utf-8", newline="") as f:
            for l in csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                yield l

    ja, fr, auteur = {}, {}, {}
    for l in lire_tsv("jpn_sentences_detailed.tsv"):
        ja[int(l[0])] = l[2]
        auteur[int(l[0])] = l[3]
    for l in lire_tsv("fra_sentences_detailed.tsv"):
        fr[int(l[0])] = l[2]
        auteur[int(l[0])] = l[3]
    en = {int(l[0]): l[2] for l in lire_tsv("eng_sentences_detailed.tsv")}
    vers_fr, vers_en = defaultdict(list), defaultdict(list)
    with open(os.path.join(brut, "links.csv"), encoding="utf-8") as f:
        for l in csv.reader(f, delimiter="\t"):
            a, b = int(l[0]), int(l[1])
            if a in ja:
                if b in fr:
                    vers_fr[a].append(b)
                elif b in en:
                    vers_en[a].append(b)
    lemmes = {}
    for l in lire_tsv("jpn_indices.csv"):
        lemmes[int(l[0])] = [formes(t) for t in l[2].split()]

    par_particule = defaultdict(list)
    for sid, toks in lemmes.items():
        if sid not in ja or not vers_fr.get(sid):
            continue
        texte = ja[sid]
        if not 6 <= len(texte) <= 16:
            continue
        rangs = [max(niveau_mot.get(f, 0) for f in t) for t in toks
                 if not all(re.fullmatch(r"[\W\d０-９]+", f) for f in t)]
        facile = min(rangs) if rangs else 0
        for p in parts:
            present = any(p["mot"] in t for t in toks) if p["mot"] != "ます" else "ます" in texte
            if present:
                par_particule[p["id"]].append((facile, len(texte), sid))

    lot = []
    for p in parts:
        cands = sorted(par_particule[p["id"]], key=lambda c: (-c[0], abs(c[1] - 11)))[:8]
        lot.append({"id": p["id"], "mot": p["mot"], "fr": p["fr"], "note": p["note"], "phrases": [
            {"jpn": sid, "ja": ja[sid], "fr": fr[vers_fr[sid][0]],
             "en": en[vers_en[sid][0]] if vers_en.get(sid) else None,
             # Tatoeba est sous CC BY : on garde de quoi citer les auteurs.
             "tatoeba": {"ids": {"jpn": sid, "fra": vers_fr[sid][0], "eng": vers_en[sid][0] if vers_en.get(sid) else None},
                         "auteurs": {"jpn": auteur.get(sid), "fra": auteur.get(vers_fr[sid][0])}},
             "niveau_le_plus_difficile": {5: "N5", 4: "N4", 3: "N3", 2: "N2", 1: "N1"}.get(f, "hors liste")}
            for f, _, sid in cands]})
    # Le lot à juger (lots/, non versionné) et sa copie versionnée, d'où
    # japonais/datos/construire.py tire les phrases retenues.
    for dossier, nom in (("lots", "particules.json"), ("sources", "particules-candidates.json")):
        os.makedirs(os.path.join(CARTES, dossier), exist_ok=True)
        with open(os.path.join(CARTES, dossier, nom), "w", encoding="utf-8") as f:
            json.dump(lot, f, ensure_ascii=False, indent=1)
    print(len(lot), "particules ;", sum(1 for x in lot if not x["phrases"]), "sans candidate")


if __name__ == "__main__":
    main()
