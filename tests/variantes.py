# -*- coding: utf-8 -*-
"""Controle de espanol/datos/variantes.json, section « phrases » (v904).

- chaque phrase remplacee existe bien comme exemple dans temas.json,
  adjetivos.json ou verbos.json (sinon le remplacement ne se fait jamais) ;
- la phrase d'Amerique latine differe de celle du cours ;
- elle ne contient plus de mot d'Espagne de la liste « noms » (sauf « piso »,
  qui est aussi le mot d'Amerique latine pour le sol et l'etage).

    python tests/variantes.py
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")

def charger(nom):
    return json.load(io.open(os.path.join(DATOS, nom), encoding="utf-8"))

v = charger("variantes.json")
noms, phrases = v.get("noms", {}), v.get("phrases", {})
temas = charger("temas.json")["themes"]

exemples = set()
formes = set()
for th in temas:
    for m in th["mots"]:
        if not isinstance(m, dict):
            continue
        exemples.add(m.get("exemple", ""))
        if m.get("mot") in noms:
            formes.add(m["mot"])
            if m.get("pluriel"):
                formes.add(m["pluriel"])
for nom in ("adjetivos.json", "verbos.json"):
    for liste in charger(nom).values():
        if isinstance(liste, list):
            exemples.update(x.get("exemple", "") for x in liste if isinstance(x, dict))
formes.discard("piso")
formes.discard("pisos")
motif = re.compile(r"(?<![\wáéíóúñü])(" + "|".join(sorted(map(re.escape, formes), key=len, reverse=True)) + r")(?![\wáéíóúñü])", re.I)

erreurs = []
for avant, apres in phrases.items():
    if avant not in exemples:
        erreurs.append("introuvable dans le corpus : %r" % avant)
    if avant == apres:
        erreurs.append("phrase identique : %r" % avant)
    reste = motif.findall(apres)
    if reste:
        erreurs.append("%r garde un mot d'Espagne : %s" % (apres, ", ".join(reste)))
if erreurs:
    print("\n".join(erreurs))
    sys.exit(1)
print("OK : %d phrases d'Amerique latine." % len(phrases))
