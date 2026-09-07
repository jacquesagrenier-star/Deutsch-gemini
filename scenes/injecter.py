# -*- coding: utf-8 -*-
"""Recopie une scene dans le lecteur de prototype.

    python scenes/injecter.py 01-ankunft-berlin

Le lecteur porte la scene EN DUR, parce qu'un artefact publie ne peut pas
aller chercher un fichier : la politique de securite de la page bloque
fetch et XHR. La donnee doit donc etre dans la page.

D'ou ce script. Sans lui, il y aurait deux exemplaires de la scene qui
divergeraient au premier changement -- et c'est le JSON qui fait foi, pas
la copie collee dans le HTML.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LECTEUR = os.path.join(RACINE, "scenes", "lecteur-prototype.html")

nom = sys.argv[1] if len(sys.argv) > 1 else "01-ankunft-berlin"
chemin = os.path.join(RACINE, "scenes", nom + ".json")
d = json.load(io.open(chemin, encoding="utf-8"))

# Ce qui sert a la machine seulement n'a rien a faire dans la page.
d.pop("_format", None)
for loc in d.get("locuteurs", {}).values():
    loc.pop("_voix", None)

html = io.open(LECTEUR, encoding="utf-8").read()
bloc = "const SCENE = " + json.dumps(d, ensure_ascii=False, indent=1) + ";"

motif = re.compile(r"const SCENE = \{.*?\n\};", re.S)
if not motif.search(html):
    sys.exit("  Bloc « const SCENE = {...}; » introuvable dans le lecteur.")
html = motif.sub(lambda _: bloc, html, count=1)

io.open(LECTEUR, "w", encoding="utf-8", newline="").write(html)

facturable = sum(p["duree"] for p in d["plans"] if p["type"] == "replique")
total = sum(p["duree"] for p in d["plans"])
print("  %s -> lecteur-prototype.html" % os.path.basename(chemin))
print("  %d plans, %d s, dont %d s facturables" % (len(d["plans"]), total, facturable))
print("  locuteurs : %s" % ", ".join(
    "%s (%s)" % (v["nom"], v.get("voix") or "voix a choisir")
    for v in d["locuteurs"].values()))
