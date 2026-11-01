# -*- coding: utf-8 -*-
# Trie les candidates de rejouer.py : ecarte les changements cosmetiques de la source (ponctuation,
# casse, espaces, guillemets, points de suspension) et regroupe le reste par (fichier, ident) pour
# la relecture : l'allemand d'alors, l'allemand d'aujourd'hui, et chaque traduction restee.
#   python trier.py c/*.json > a_relire.txt
import json, sys, re, unicodedata
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding="utf-8")

def norm(x):
    x = unicodedata.normalize("NFC", x or "").lower()
    x = re.sub(r"<[^>]+>", "", x)
    x = re.sub(r"[\s\.\,\;\:\!\?\…«»\"“”„'’‘\-–—\(\)\[\]‌‎‏  ]+", "", x)
    return x

groupes = defaultdict(list)
stats = Counter(); cosm = Counter()
for f in sys.argv[1:]:
    for c in json.load(open(f, encoding="utf-8")):
        if norm(c["de"]) == norm(c["de0"]) and norm(c["fr"]) == norm(c["fr0"]):
            cosm[(c["f"], c["l"])] += 1
            continue
        # le temps d'un verbe n'etait qu'une forme (« hat ausgehandelt ») quand la traduction de la
        # phrase est nee : elle a ete ecrite pour la phrase venue ensuite, rien de perime
        if c["champ"] in ("perfekt", "praeteritum", "konjunktiv2") \
                and len(c["de0"].split()) <= 3 and not re.search(r"[.!?]$", c["de0"].strip()):
            cosm[(c["f"], c["l"], "forme")] += 1
            continue
        # indice ou explication dont le francais n'a pas bouge : la traduction traduit ce francais,
        # commun a plusieurs exercices (« Dans une relative, le verbe part a la FIN »)
        if c["champ"] in ("hint", "explanation") and norm(c["fr"]) == norm(c["fr0"]):
            cosm[(c["f"], c["l"], "fr commun")] += 1
            continue
        stats[(c["f"], c["l"])] += 1
        groupes[(c["f"], c["ident"], c["champ"], c["de0"], c["de"], c["fr0"], c["fr"])].append(c)
print("# cosmetiques ecartees :", sum(cosm.values()), dict(cosm))
print("# a relire :", sum(stats.values()), dict(stats))
print("# groupes :", len(groupes))
for (f, ident, champ, de0, de, fr0, fr), cs in sorted(groupes.items()):
    print()
    print("==", f, ident, champ, "| ne", cs[0]["ne"], cs[0]["sorte"])
    if norm(de0) != norm(de):
        print("  DE alors :", de0)
        print("  DE  now  :", de)
    else:
        print("  DE       :", de)
    if norm(fr0) != norm(fr):
        print("  FR alors :", fr0)
        print("  FR  now  :", fr)
    else:
        print("  FR       :", fr)
    for c in cs:
        print("   ", c["l"], ":", c["t"])
