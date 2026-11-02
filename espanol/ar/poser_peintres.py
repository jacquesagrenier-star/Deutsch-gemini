# -*- coding: utf-8 -*-
"""Pose les notices arabes des peintres de la mosaïque espagnole
(espanol/ar/lots/peintres-ar.json -> espanol/mosaique/peintres.json, clé « ar »
après « pt »). Ne remplace jamais une notice déjà posée.

    python espanol/ar/poser_peintres.py"""
import io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CIBLE = os.path.join(RACINE, "espanol", "mosaique", "peintres.json")
LOT = os.path.join(RACINE, "espanol", "ar", "lots", "peintres-ar.json")

texte = io.open(CIBLE, encoding="utf-8").read()
d = json.loads(texte)
lot = json.load(io.open(LOT, encoding="utf-8"))["peintres"]
manquants = sorted(set(d["peintres"]) - set(lot))
if manquants:
    sys.exit("peintres sans notice arabe dans le lot : " + ", ".join(manquants))
poses = 0
for nom, n in d["peintres"].items():
    if not n.get("ar"):
        n["ar"] = lot[nom]
        poses += 1
d["_langues"] = d.get("_langues", "").replace("fr, en, pt (LANGUES_UI_AVEC_ESPAGNOL)", "fr, en, pt, ar (LANGUES_UI_AVEC_ESPAGNOL)")
indent = 1 if texte.startswith("{\n \"") else 2
with io.open(CIBLE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=indent)
    if texte.endswith("\n"):
        f.write("\n")
print("%d notices posées" % poses)
