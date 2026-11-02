# -*- coding: utf-8 -*-
"""Pose les traductions pt et ar du thème « Description physique »
et « Adjectifs »
(vhs_kapitel1_b1 et vhs_kapitel2_b1, cours de Jacques) depuis espanol/ajouts/cours-jacques-pt-ar.json.

    python espanol/pt/poser_cours.py

Garde-fous : les entrées sont prises dans l'ordre du thème, le mot espagnol doit
concorder ; un champ déjà rempli n'est jamais écrasé. Écrit temas.json dans le
format du fichier (ensure_ascii=False, indent=1)."""
import io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMAS = os.path.join(RACINE, "espanol", "datos", "temas.json")
LOT = os.path.join(RACINE, "espanol", "ajouts", "cours-jacques-pt-ar.json")

texte = io.open(TEMAS, encoding="utf-8").read()
d = json.loads(texte)
lot = json.load(io.open(LOT, encoding="utf-8"))["entrees"]
entrees = []
for tid in ("vhs_kapitel1_b1", "vhs_kapitel2_b1"):
    theme = next(t for t in d["themes"] if t["id"] == tid)
    entrees += list(theme.get("mots", []) or []) + list(theme.get("adjektive", []) or [])
if len(entrees) != len(lot):
    sys.exit("compte différent : thème %d, lot %d" % (len(entrees), len(lot)))
poses = 0
for e, (mot, tpt, ept, tar, ear) in zip(entrees, lot):
    if e["mot"] != mot:
        sys.exit("ordre rompu : %s != %s" % (e["mot"], mot))
    for cle, val in (("traduction_pt", tpt), ("exemple_pt", ept), ("traduction_ar", tar), ("exemple_ar", ear)):
        if not e.get(cle):
            e[cle] = val
            poses += 1
# Même mise en forme que le fichier d'origine (indentation détectée).
indent = 1 if texte.startswith("{\n \"") else (2 if texte.startswith("{\n  \"") else None)
with io.open(TEMAS, "w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=indent)
    if texte.endswith("\n"):
        f.write("\n")
print("%d champs posés" % poses)
