# -*- coding: utf-8 -*-
# Le mecanisme du defaut de Daria, sans aucun filtre : un meme mot (mot / infinitif) present dans
# plusieurs enregistrements (themes differents, ou themes.json et verbe.json) dont une langue porte la
# MEME traduction d'exemple en face de deux phrases allemandes differentes.
#   python homonymes.py <langues> <fichier>...
import json, sys, re, unicodedata
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
LANGS = sys.argv[1].split(",")
CHAMPS = ("exemple", "perfekt", "praeteritum", "konjunktiv2", "exemple_imperfecto", "exemple_perfecto",
          "exemple_subjuntivo", "exemple_preterito", "exemple_futuro", "exemple_condicional")

def norm(x):
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", x or "").lower())

def recs(o, p=""):
    if isinstance(o, dict):
        a = o.get("mot") or o.get("infinitif") or o.get("palabra") or o.get("infinitivo")
        if isinstance(a, str) and isinstance(o.get("exemple"), str):
            yield p, a, o
        for k, v in o.items():
            yield from recs(v, p + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from recs(v, p + "/" + (v["id"] if isinstance(v, dict) and isinstance(v.get("id"), str) else str(i)))

par = defaultdict(list)
for f in sys.argv[2:]:
    for p, a, o in recs(json.load(open(f, encoding="utf-8"))):
        par[a].append((f, p, o))
n = 0
for a, rs in sorted(par.items()):
    if len(rs) < 2:
        continue
    for c in CHAMPS:
        for l in LANGS:
            vus = defaultdict(set)
            for f, p, o in rs:
                t, de = o.get(c + "_" + l), o.get(c)
                if isinstance(t, str) and t and isinstance(de, str):
                    vus[norm(t)].add((de, f, p, t))
            for nt, s in vus.items():
                if len(set(norm(x[0]) for x in s)) > 1:
                    n += 1
                    print("##", a, c, l, ":", next(iter(s))[3])
                    for de, f, p, t in sorted(s):
                        print("     ", f, p, "|", de)
print(n, "cas")
