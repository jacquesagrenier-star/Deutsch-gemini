# -*- coding: utf-8 -*-
# TRADUCTIONS JAMAIS ALIGNEES : un indice mecanique. Une traduction ecrite sans voir la phrase allemande
# perd ce que la phrase contient de non traduisible : ses chiffres et ses noms propres (Hamburg, Anna).
# On liste les traductions ou un chiffre ou un nom de l'allemand n'apparait pas.
#   python entites.py noms     -> les noms propres les plus frequents des exemples (pour la table)
#   python entites.py <sortie.json>
import json, sys, re, os, unicodedata
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")
LANGS = ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "fr"]
CHAMPS = ("exemple", "perfekt", "praeteritum", "konjunktiv2")
CORPUS = ["themes.json", "verbe.json", "adjectif.json", "adverbe.json", "redewendung.json", "funktionswort.json"]

def enregistrements(o, chemin=""):
    if isinstance(o, dict):
        if isinstance(o.get("exemple"), str):
            yield chemin, o
        for k, v in o.items():
            yield from enregistrements(v, chemin + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from enregistrements(v, chemin + "/" + (v.get("id") if isinstance(v, dict) and isinstance(v.get("id"), str) else str(i)))

mots = set()
recs = []
for f in CORPUS:
    for ch, o in enregistrements(json.load(open(f, encoding="utf-8"))):
        recs.append((f, ch, o))
        for k in ("mot", "infinitif"):
            if isinstance(o.get(k), str):
                for w in re.findall(r"\w+", o[k]):
                    mots.add(w.lower())

# Noms propres : un mot a majuscule qui n'est ni un mot du corpus ni en tete de phrase
def noms(phrase):
    out = []
    toks = re.findall(r"\w+", phrase)
    for i, w in enumerate(toks):
        if w[:1].isupper() and w.lower() not in mots and not w.isupper() and len(w) > 2:
            out.append(w)
    return out

if sys.argv[1] == "noms":
    c = Counter()
    for f, ch, o in recs:
        for k in CHAMPS:
            if isinstance(o.get(k), str):
                c.update(noms(o[k]))
    print(c.most_common(150))
    sys.exit()

TABLE = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "noms_table.json"), encoding="utf-8"))
CHIFFRES = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")

def present(nom, l, t):
    formes = TABLE.get(nom, {}).get(l) or TABLE.get(nom, {}).get("*")
    if formes is None:
        if l in ("en", "tr", "pt", "pl", "fr"):
            formes = [nom[:max(3, len(nom) - 2)]]
        else:
            return None   # pas de forme connue dans cet alphabet : on ne juge pas
    tl = t.lower()
    return any(x.lower() in tl for x in formes)

sortie = []
compte = Counter()
for f, ch, o in recs:
    for k in CHAMPS:
        de = o.get(k)
        if not isinstance(de, str):
            continue
        chif = re.findall(r"\d+", de)
        ns = [n for n in re.findall(r"\w+", de) if n in TABLE]
        for l in LANGS:
            t = o.get(k + "_" + l)
            if not isinstance(t, str) or not t:
                continue
            tt = t.translate(CHIFFRES)
            manque = [c for c in chif if c not in tt]
            for n in ns:
                p = present(n, l, t)
                if p is False:
                    manque.append(n)
            if manque:
                compte[(f, l)] += 1
                sortie.append(dict(f=f, ch=ch, mot=o.get("mot") or o.get("infinitif"), champ=k, l=l, de=de, t=t, manque=manque))
for k, n in sorted(compte.items()):
    print(k, n)
print(len(sortie), "en tout")
json.dump(sortie, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
