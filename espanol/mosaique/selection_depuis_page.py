"""Ecrit selection.json a partir de l'ordre enregistre par la page « Tableaux
espagnols » (document choix/selection, champ ordre).

  python selection_depuis_page.py "[2, 3, 4, ...]"

Le rang est la position dans cet ordre : l'ordre d'apparition pour l'apprenant.
"""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__))

ordre = json.loads(sys.argv[1])
c = {t["num"]: t for t in json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))}
sel = []
for rang, n in enumerate(ordre, 1):
    t = c[n]
    sel.append({"rang": rang, "candidat": n, "peintre": t["peintre"], "pays": t["pays"], "mort": t["mort"],
                "titre": t["titre"] or t["titre_en"], "annee": t.get("annee", ""),
                "fichier_commons": t["fichier"], "page": t.get("page"), "original": t.get("original"),
                "licence": t["licence"], "wikidata": t["cle"], "eclat": t["eclat"]})
json.dump({"_note": "Collection espagnole choisie et ordonnee par Jacques le 14 oct. 2026 (page « Tableaux "
                    "espagnols », champ ordre). rang = ordre d'apparition pour l'apprenant. Le meme jour, "
                    "cinq images trop petites (moins de 450 px) remplacees par des tableaux gardes non "
                    "classes, avec son accord.",
           "tableaux": sel},
          open(os.path.join(ICI, "selection.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(sel), "tableaux,", sum(t["pays"] != "Espagne" for t in sel), "d'Amerique latine")
