# -*- coding: utf-8 -*-
# Scenes : chaque traduction garde le francais source a cote d'elle (traductions/<scene>.<langue>.json) ;
# construire.py n'en reprend une que si ce francais est encore celui du points.json. On compte, sans rien
# ecrire, les traductions perimees (francais change) et orphelines (phrase allemande changee).
import sys, os, json, glob, io
sys.stdout.reconfigure(encoding="utf-8")
RACINE = sys.argv[1]
sys.path.insert(0, os.path.join(RACINE, "visuel", "prototype"))
import construire as C
from collections import Counter
per, orph, total = Counter(), Counter(), Counter()
exemples = []
for pts_f in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "*.points.json"))):
    nom = os.path.basename(pts_f)[:-len(".points.json")]
    pts = json.load(io.open(pts_f, encoding="utf-8"))
    src = C.sources(pts)
    for lang in C.LANGUES:
        ch = os.path.join(RACINE, "visuel", "prototype", "traductions", "%s.%s.json" % (nom, lang))
        if not os.path.exists(ch):
            continue
        fic = json.load(io.open(ch, encoding="utf-8"))
        for groupe, textes in src.items():
            entrees = fic.get(groupe, {})
            for cle, fr in textes.items():
                e = entrees.get(cle)
                if e and e.get("trad"):
                    total[lang] += 1
                    if e.get("fr") != fr:
                        per[lang] += 1
                        exemples.append((nom, lang, cle, e.get("fr"), fr))
            for cle in entrees:
                if cle not in textes and isinstance(entrees[cle], dict) and entrees[cle].get("trad"):
                    orph[lang] += 1
print("traductions a jour ou non :", dict(total))
print("perimees (francais change) :", dict(per))
print("orphelines (phrase disparue) :", dict(orph))
for x in exemples[:20]:
    print("  ", x)
