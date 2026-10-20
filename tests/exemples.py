# -*- coding: utf-8 -*-
"""Les cartes sans phrase d'exemple, ou dont l'exemple n'est pas traduit.

Ne le 19 oct. 2026 : Jacques retourne « ¿A qué hora es la salida? » et ne trouve
pas de phrase d'exemple ; « fais une verification complete de l'application ».

Pour chaque carte de vocabulaire (allemand et espagnol) : l'exemple dans la
langue apprise, et sa traduction dans chaque langue d'interface de cette langue
(allemand : fr en tr uk fa ar pt pl ru ; espagnol : fr en pt ar). Les verbes ont
un exemple par temps ; on controle le temps de base (exemple) et chaque autre
temps qui porte une phrase.

    python tests/exemples.py            le bilan
    python tests/exemples.py --liste    et chaque carte en defaut
Code de sortie 1 s'il manque un exemple ou une traduction.
"""
import io, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = {"de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"], "es": ["fr", "en", "pt", "ar"]}
LISTE = "--liste" in sys.argv

def charger(f):
    return json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))

def cle_trad(champ, lg):
    # « exemple » se traduit dans exemple_fr, exemple_en... ; « perfekt » dans perfekt_fr...
    return champ + "_" + lg

bilan = []      # (source, cartes, sans exemple, traductions manquantes, exemples)

def controler(source, entrees, langue, champs=("exemple",), nom=lambda e: e.get("mot") or e.get("infinitif")):
    cartes = sans = trad = 0
    defauts = []
    for e in entrees:
        cartes += 1
        for champ in champs:
            if champ != "exemple" and not (e.get(champ) or "").strip():
                continue    # un temps sans phrase n'est pas montre
            if not (e.get(champ) or "").strip():
                sans += 1; defauts.append("%s : pas d'exemple" % nom(e)); continue
            manque = [lg for lg in LANGUES[langue] if not (e.get(cle_trad(champ, lg)) or "").strip()]
            if manque:
                trad += 1; defauts.append("%s [%s] : traduction manquante %s" % (nom(e), champ, ",".join(manque)))
    bilan.append((source, cartes, sans, trad, defauts))

def niveaux(d):
    out = []
    for k, v in d.items():
        if isinstance(v, list): out.extend(x for x in v if isinstance(x, dict))
    return out

# --- allemand
mots = [m for th in charger("themes.json")["themes"] for m in th.get("mots", [])]
controler("de themes (noms)", mots, "de")
controler("de verbes", niveaux(charger("verbe.json")), "de", ("exemple", "perfekt", "praeteritum", "konjunktiv2"))
controler("de adjectifs", niveaux(charger("adjectif.json")), "de")
controler("de adverbes", niveaux(charger("adverbe.json")), "de")
controler("de expressions", niveaux(charger("redewendung.json")), "de")
controler("de mots-outils", niveaux(charger("funktionswort.json")), "de")
# --- espagnol
mots = [m for th in charger("espanol/datos/temas.json")["themes"] for m in th.get("mots", [])]
controler("es temas (noms)", mots, "es")
controler("es verbos", niveaux(charger("espanol/datos/verbos.json")), "es",
          ("exemple", "exemple_preterito", "exemple_imperfecto", "exemple_perfecto", "exemple_futuro", "exemple_condicional", "exemple_subjuntivo"))
controler("es adjetivos", niveaux(charger("espanol/datos/adjetivos.json")), "es")
controler("es adverbios", niveaux(charger("espanol/datos/adverbios.json")), "es")
controler("es expresiones", niveaux(charger("espanol/datos/expresiones.json")), "es")
controler("es funcionales", niveaux(charger("espanol/datos/funcionales.json")), "es")
# --- Premiers pas : [expression, sens, exemple, sens de l'exemple]
for f, langue in (("premiers-pas.json", "de"), ("espanol/datos/premiers-pas.json", "es")):
    cartes = sans = trad = 0; defauts = []
    for i, et in enumerate(charger(f)["etapes"]):
        for c in et["cartes"]:
            c = c[:-1] if c and isinstance(c[-1], dict) and "la" in c[-1] else c
            cartes += 1
            if not (len(c) > 2 and isinstance(c[2], str) and c[2].strip()):
                sans += 1; defauts.append("etape %d · %s : pas d'exemple" % (i + 1, c[0])); continue
            sens = c[3] if len(c) > 3 and isinstance(c[3], dict) else {}
            manque = [lg for lg in LANGUES[langue] if not (sens.get(lg) or "").strip()]
            if manque:
                trad += 1; defauts.append("etape %d · %s : traduction manquante %s" % (i + 1, c[0], ",".join(manque)))
    bilan.append(("%s premiers pas" % langue, cartes, sans, trad, defauts))

total = 0
for source, cartes, sans, trad, defauts in bilan:
    total += sans + trad
    print("%-22s %5d cartes  %4d sans exemple  %4d exemples non traduits" % (source, cartes, sans, trad))
    if LISTE:
        for d in defauts: print("      " + d)
print("\n%s" % ("OK : chaque carte a son exemple, traduit." if not total else "%d defaut(s)." % total))
sys.exit(1 if total else 0)
