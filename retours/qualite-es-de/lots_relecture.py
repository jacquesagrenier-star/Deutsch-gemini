# -*- coding: utf-8 -*-
"""Lots pour la relecture par un autre modele : un echantillon TIRE AU HASARD
(graine fixe, pour pouvoir le refaire) et les cas que les controles
mecaniques ont signales sans pouvoir trancher.

    python retours/qualite-es-de/lots_relecture.py <dossier> [suspects_verbes.json]

Chaque entree porte son adresse exacte (fichier, chemin) : un signalement du
relecteur se verifie dans le fichier, jamais sur sa citation.
"""
import json
import os
import random
import sys

from commun import charger

GRAINE = 20261102
LDE = ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
LES = ["en", "pt", "ar", "de"]


def carte(e, langues, champs):
    out = {}
    for c in champs:
        if c in e:
            out[c] = e[c]
    for base in ("traduction", "exemple"):
        fr = e.get(base + "_fr") if base == "exemple" else e.get("traduction")
        if fr is not None:
            out[base + "_fr"] = fr
        for l in langues:
            if e.get(base + "_" + l):
                out[base + "_" + l] = e[base + "_" + l]
    return out


def main():
    dossier = sys.argv[1]
    os.makedirs(dossier, exist_ok=True)
    rnd = random.Random(GRAINE)

    # allemand : noms, verbes, adjectifs, adverbes, expressions
    pool = []
    for t in charger("themes.json")["themes"]:
        for i, m in enumerate(t["mots"]):
            pool.append(("themes.json", "%s[%d]" % (t["id"], i), m, ["mot", "genre", "pluriel", "exemple"]))
    for f, cle in (("verbe.json", "infinitif"), ("adjectif.json", "mot"), ("adverbe.json", "mot"),
                   ("redewendung.json", "mot")):
        for niv, lst in charger(f).items():
            for i, e in enumerate(lst):
                pool.append((f, "%s[%d]" % (niv, i), e, [cle, "exemple"]))
    lot = rnd.sample(pool, 90)
    json.dump([{"fichier": f, "chemin": c, **carte(e, LDE, ch)} for f, c, e, ch in lot],
              open(os.path.join(dossier, "lot-de-mots.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # espagnol : temas, verbos, adjetivos, adverbios, expresiones, funcionales
    pool = []
    for t in charger("espanol/datos/temas.json")["themes"]:
        for i, m in enumerate(t["mots"]):
            pool.append(("espanol/datos/temas.json", "%s[%d]" % (t["id"], i), m,
                         ["mot", "genre", "pluriel", "exemple"]))
    for f in ("verbos.json", "adjetivos.json", "adverbios.json", "expresiones.json", "funcionales.json"):
        for niv, lst in charger("espanol/datos/" + f).items():
            for i, e in enumerate(lst):
                pool.append(("espanol/datos/" + f, "%s[%d]" % (niv, i), e, ["mot", "feminin", "exemple"]))
    lot = rnd.sample(pool, 110)
    json.dump([{"fichier": f, "chemin": c, **carte(e, LES, ch)} for f, c, e, ch in lot],
              open(os.path.join(dossier, "lot-es-mots.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # exercices des deux langues : question, options, reponse, traductions fr/en
    pool = []
    for app, f in (("de", "exercices.json"), ("es", "espanol/datos/ejercicios.json")):
        for jeu, lst in charger(f)["jeux"].items():
            for i, e in enumerate(lst):
                d = {k: e[k] for k in ("question", "options", "correct", "answers", "chunks", "hint",
                                       "translation", "translation_en", "explanation", "explanation_en")
                     if k in e}
                pool.append({"fichier": f, "chemin": "%s[%d]" % (jeu, i), **d})
    lot = rnd.sample(pool, 90)
    if len(sys.argv) > 2:
        sus = json.load(open(sys.argv[2], encoding="utf-8"))
        vb = charger("verbe.json")
        for s in sus:
            if s.get("code") != "phrase_sans_verbe":
                continue
            niv_i, champ = s["ou"].split(".", 1)[1].rsplit(".", 1)
            niv, i = niv_i.split("[")
            v = vb[niv][int(i[:-1])]
            lot.append({"fichier": "verbe.json", "chemin": s["ou"], "verbe_enseigne": v["infinitif"],
                        "traduction_fr": v["traduction"], "temps": champ, "phrase": v[champ],
                        "phrase_fr": v.get(champ + "_fr"), "phrase_en": v.get(champ + "_en"),
                        "question": "Cette phrase illustre-t-elle bien le verbe enseigne, a ce temps ?"})
    json.dump(lot, open(os.path.join(dossier, "lot-exercices.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("lots ecrits dans", dossier)


if __name__ == "__main__":
    main()
