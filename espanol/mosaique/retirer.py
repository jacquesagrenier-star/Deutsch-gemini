"""Retire des planches ce que l'oeil a ecarte, renumerote, et refait les
planches -- sans relancer la recolte.

Les numeros ci-dessous sont ceux de la recolte « eclat » du 14 oct. 2026
(236 candidats). Leurs identifiants Wikidata vont ensuite dans EXCLUS_ID de
recolter.py, pour qu'une nouvelle recolte ne les ramene pas. (Le tour
precedent, sur 270 candidats, y est deja.)
"""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

TOTAL_ATTENDU = 342
# Recolte avec les peintres plus modernes (14 oct. 2026) : doublons sous deux
# noms de fichier, affiches pleines de texte, gravures en noir et blanc.
RETIRES = {
    10: "doublon du 6 (Silva)", 64: "doublon du 63 (Silva)", 45: "doublon du 27 (Navazio)",
    168: "doublon du 27 (Navazio)", 273: "doublon du 171 (Boggio)",
    59: "affiche (Riquer)", 69: "affiche (Riquer)", 152: "affiche (Riquer)",
    238: "noir et blanc", 341: "noir et blanc", 342: "noir et blanc",
}

c = json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))
assert len(c) == TOTAL_ATTENDU, len(c)
ids = sorted({t["cle"] for t in c if t["num"] in RETIRES})
gardes = [t for t in c if t["num"] not in RETIRES]
for n, t in enumerate(gardes, 1):
    t["num"] = n
json.dump(gardes, open(os.path.join(ICI, "candidats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for f in os.listdir(ICI):
    if f.startswith("planche-"):
        os.remove(os.path.join(ICI, f))
recolter.planches(gardes)
print(len(c), "->", len(gardes))
print("A AJOUTER A EXCLUS_ID :", ids)
