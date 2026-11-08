# -*- coding: utf-8 -*-
"""verbos.json B1 : l'entree « oponer » enseignait le verbe sans pronom alors
que ses sept exemples emploient tous « oponerse » (Se opone a cualquier
cambio, Me opondré a…). Recommandation de la relecture appliquee le 4 nov.
2026 (« le controle de la qualite, tu peux continuer ») : l'entree devient
oponerse, tableaux avec pronoms, sur le modele des autres pronominaux
(integrarse, alojarse). Les exemples ne changent pas.

Les VOIX du mot et des formes nouvelles ne sont pas produites (rien de payant
sans accord) : la liste est dans A-JACQUES-VOIX.md.

    python retours/qualite-es-de/oponerse.py            # montre
    python retours/qualite-es-de/oponerse.py --ecrire   # applique
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
F = os.path.join(RACINE, "espanol", "datos", "verbos.json")
PR = ["me", "te", "se", "nos", "os", "se"]

raw = io.open(F, encoding="utf-8", newline="").read()
d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + "\n" == raw, "mise en forme inattendue"
v = [x for x in d["B1"] if x.get("mot") == "oponer"]
assert len(v) == 1
v = v[0]
assert v["exemple"] == "Se opone a cualquier cambio."
avant = json.loads(json.dumps(v))

v["mot"] = v["infinitif"] = "oponerse"
v["reflexiv"] = True
v["traduction"] = "s'opposer"
v["traduction_pt"] = "opor-se"
v["traduction_de"] = "sich widersetzen, sich entgegenstellen"
personnes = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]
assert list(v["praesens"]) == personnes and not v["praesens"]["ich"].startswith("me ")
v["praesens"] = {p: "%s %s" % (pr, v["praesens"][p]) for p, pr in zip(personnes, PR)}
for t in ("preterito", "imperfecto", "subjuntivo", "perfecto", "futuro", "condicional"):
    assert len(v[t]) == 6 and not v[t][0].startswith("me ")
    v[t] = ["%s %s" % (pr, f) for pr, f in zip(PR, v[t])]
v["imperativo"] = {"tu": "oponte", "usted": "opóngase", "vosotros": "oponeos", "ustedes": "opónganse"}

for k in v:
    if v[k] != avant.get(k):
        print("%-12s %s\n%-12s %s" % (k, avant.get(k), "", v[k]))
if "--ecrire" in sys.argv:
    io.open(F, "w", encoding="utf-8", newline="").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("ecrit")
