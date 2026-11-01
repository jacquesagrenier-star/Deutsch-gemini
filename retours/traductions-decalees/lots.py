# -*- coding: utf-8 -*-
# LES LOTS INDEXES PAR LE MOT (corrections_uk/, corrections_fa/, corrections_tr/, corrections_vhs/,
# corrections_collisions/). Chaque entree dit {mot, exemple_<l>, ...} : rien n'y dit A QUELLE PHRASE
# allemande la traduction repond. Un mot present dans deux themes (Chef : berufe_a1 et arbeit_buero_a1)
# a donc pu recevoir la meme phrase deux fois -- c'est le defaut trouve par Daria (1er nov. 2026).
#
# Pour chaque champ traduit d'un lot, on cherche TOUS les enregistrements actuels de ce mot qui portent
# encore la traduction du lot (« intacts »). Deux intacts en face de deux phrases allemandes differentes :
# l'un des deux est faux (COPIE). Un seul intact : a relire (la traduction a-t-elle vu la phrase ?).
#   python lots.py <sortie.json>
import json, sys, os, re, glob, unicodedata
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
LANGS = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
CHAMPS = ("exemple", "perfekt", "praeteritum", "konjunktiv2")

def norm(x):
    x = unicodedata.normalize("NFC", x or "").lower()
    return re.sub(r"[\W_]+", "", x)

def enregistrements(o, chemin=""):
    if isinstance(o, dict):
        a = o.get("mot") or o.get("infinitif")
        if isinstance(a, str) and isinstance(o.get("exemple"), str):
            yield chemin, a, o
        for k, v in o.items():
            yield from enregistrements(v, chemin + "/" + (o.get("id") if k == "mots" and False else k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from enregistrements(v, chemin + "/" + (v.get("id", str(i)) if isinstance(v, dict) and "id" in v else str(i)))

CORPUS = ["themes.json", "verbe.json", "adjectif.json", "adverbe.json", "redewendung.json", "funktionswort.json"]
index = defaultdict(list)     # mot -> [(fichier, chemin, objet)]
for f in CORPUS:
    for ch, a, o in enregistrements(json.load(open(f, encoding="utf-8"))):
        index[a].append((f, ch, o))

resultats = []
stats = defaultdict(lambda: defaultdict(int))
for lot in sorted(glob.glob("corrections_*/*.json")):
    try:
        d = json.load(open(lot, encoding="utf-8"))
    except Exception:
        continue
    entrees = d.get("entrees") if isinstance(d, dict) else None
    if not isinstance(entrees, list):
        continue
    for e in entrees:
        if not isinstance(e, dict) or not isinstance(e.get("mot") or e.get("infinitif"), str):
            continue
        mot = e.get("mot") or e.get("infinitif")
        for k, t in e.items():
            m = re.match(r"^(%s)_(%s)$" % ("|".join(CHAMPS), "|".join(LANGS)), k)
            if not m or not isinstance(t, str) or not t:
                continue
            c, l = m.group(1), m.group(2)
            recs = [(f, ch, o) for f, ch, o in index.get(mot, []) if isinstance(o.get(c), str)]
            intacts = [(f, ch, o) for f, ch, o in recs if norm(o.get(k)) == norm(t)]
            des = set(norm(o[c]) for f, ch, o in intacts)
            sorte = "absent" if not intacts else ("COPIE" if len(des) > 1 else "intact")
            stats[(lot.split(os.sep)[0].split("/")[0], l)][sorte] += 1
            resultats.append(dict(lot=lot.replace("\\", "/"), mot=mot, champ=c, l=l, t=t, sorte=sorte,
                                  recs=[dict(f=f, ch=ch, de=o[c], fr=o.get(c + "_fr", ""), en=o.get(c + "_en", ""),
                                             t=o.get(k), intact=norm(o.get(k)) == norm(t)) for f, ch, o in recs]))
for k in sorted(stats):
    print(k, dict(stats[k]))
json.dump(resultats, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
