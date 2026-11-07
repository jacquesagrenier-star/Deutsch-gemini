# -*- coding: utf-8 -*-
"""Applique les corrections retenues apres relecture : python etapes/traductions/appliquer.py <langue> <fichier>.

<fichier> : un JSON {texte francais: nouvelle traduction}. Refuse une cle absente
de <langue>.json (une faute de recopie ne doit pas passer inapercue)."""
import json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
lg, src = sys.argv[1], sys.argv[2]
chemin = os.path.join(ICI, lg + ".json")
d = json.load(open(chemin, encoding="utf-8"))
corr = json.load(open(src, encoding="utf-8"))
absentes = [k for k in corr if k not in d]
if absentes:
    sys.exit("cles absentes de %s.json : %s" % (lg, absentes))
for k, v in corr.items():
    print("%s : %s -> %s" % (k, d[k], v))
    d[k] = v
with open(chemin, "w", encoding="utf-8", newline="\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("%d corrections appliquees a %s.json" % (len(corr), lg))
