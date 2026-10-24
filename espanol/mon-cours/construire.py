# -*- coding: utf-8 -*-
"""Verse les pages de « Mon cours » (pages.json) dans espanol/datos/temas.json.

    python espanol/mon-cours/construire.py

« Mon cours » est le pendant espagnol des Chapitres VHS de l'allemand : le
vocabulaire du manuel de Jacques, une rangee par page, tuile reservee a
l'administrateur. Meme mecanique dans index.html : des themes dont l'id
commence par « vhs_kapitel », hors seance et hors pourcentages
(estChapitreVhs). Le niveau B1 n'est qu'une cle interne, comme en allemand.

Le script remplace a chaque fois TOUS les themes vhs_kapitel* de temas.json
par ceux de pages.json : c'est pages.json qu'on complete, jamais temas.json.
"""
import io, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
TEMAS = os.path.join(ICI, "..", "datos", "temas.json")
# L'icone du livre, comme la tuile.
SVG = '<svg viewBox="0 0 24 24"><path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3zM5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/></svg>'

pages = json.load(io.open(os.path.join(ICI, "pages.json"), encoding="utf-8"))["pages"]
temas = json.load(io.open(TEMAS, encoding="utf-8"))
avant = [t for t in temas["themes"] if not t["id"].startswith("vhs_kapitel")]

nouveaux = []
for p in pages:
    nouveaux.append({
        "id": "vhs_kapitel%d_b1" % p["n"],
        "nom_theme": p["nom_theme"],
        "nom_theme_es": p["nom_theme_es"],
        "niveau": "B1",
        "svg": SVG,
        "mots": p.get("mots", []),
        "adjektive": p.get("adjektive", []),
    })

temas["themes"] = avant + nouveaux
with io.open(TEMAS, "w", encoding="utf-8", newline="\n") as f:
    json.dump(temas, f, ensure_ascii=False, indent=1)
    f.write("\n")
for t in nouveaux:
    print("%s  %-20s %2d noms, %2d adjectifs" % (t["id"], t["nom_theme_es"], len(t["mots"]), len(t["adjektive"])))
