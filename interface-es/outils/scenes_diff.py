# -*- coding: utf-8 -*-
"""Les scenes reconstruites ne different-elles de HEAD que par l'espagnol ?

    python interface-es/outils/scenes_diff.py

Pour chaque visuel/prototype/scene-*.js modifie : on retire de la version neuve les
cles « es » (le mot d'une zone, le bloc traductions.es) et on compare a HEAD. Un
ecart restant est une derive anterieure (une source changee sans reconstruction) :
il ne doit pas partir avec l'espagnol.
"""
import json, os, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def charger(texte):
    a = texte.index("window.SCENE = ") + len("window.SCENE = ")
    return json.loads(texte[a:texte.rindex(";")])


def sans_es(o):
    if isinstance(o, dict):
        return {k: sans_es(v) for k, v in o.items() if k != "es"}
    if isinstance(o, list):
        return [sans_es(x) for x in o]
    return o


mod = subprocess.run(["git", "diff", "--name-only", "--", sys.argv[1] if len(sys.argv) > 1 else "visuel/prototype/scene-*.js"], cwd=RACINE,
                     capture_output=True, text=True).stdout.split()
propres, derives = [], []
for f in mod:
    avant = subprocess.run(["git", "show", "HEAD:" + f], cwd=RACINE, capture_output=True).stdout.decode("utf-8")
    apres = open(os.path.join(RACINE, f), encoding="utf-8").read()
    if sans_es(charger(apres)) == sans_es(charger(avant)):
        propres.append(f)
    else:
        derives.append(f)
print("%d scenes ne changent que par l'espagnol" % len(propres))
for f in derives:
    print("DERIVE (autre chose que l'espagnol) :", f)
