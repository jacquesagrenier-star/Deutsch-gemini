# -*- coding: utf-8 -*-
# TRADUCTIONS RECOPIEES D'UN HOMONYME. Le cas de Daria (1er nov. 2026) n'est pas une phrase restee en
# place apres reecriture : « Der Chef ist heute nicht im Büro » a recu, en persan et en ukrainien, la
# traduction du MEME MOT dans un autre theme (« Mein Chef ist sehr streng »). Une traduction choisie
# par le mot, pas par la phrase.
#
# Detecteur sans historique : une meme traduction T (dans une langue) en face de deux phrases sources
# DIFFERENTES, alors que le francais de ces deux phrases differe aussi. Une des deux est fausse.
#   python doublons.py <sortie.json> <langues> <fichier.json>...
import json, sys, re, os, unicodedata
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
sys.argv, ARGS = sys.argv[:1] + ["x", "y"], sys.argv
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, "rejouer.py"), encoding="utf-8").read()
# on reprend la lecture des champs de rejouer.py, sans son rejeu git
exec(src[:src.index("commits = subprocess.run")])
fn = open(os.path.join(ICI, "trier.py"), encoding="utf-8").read()
exec(fn[fn.index("def norm"):fn.index("groupes =")])

SORTIE, LANGS, FICHIERS = ARGS[1], ARGS[2].split(","), ARGS[3:]
LANGUES[:] = LANGS
RL = re.compile(r"^(.+?)_(%s)$" % "|".join(LANGUES))
toutes = defaultdict(dict)  # (fichier, ident, champ) -> {langue: T normalise}
par = defaultdict(list)     # (langue, T normalise) -> [(fichier, ident, champ, T, allemand, francais)]
for f in FICHIERS:
    d = json.load(open(f, encoding="utf-8"))
    for ident, b, l, t, de, fr in tout(d):
        if l == "fr" or b in ("hint", "explanation", "textes", "{}") and not de:
            continue
        if b in ("traduction", "traduccion"):
            continue       # un mot : deux mots voisins partagent souvent leur traduction
        if len(norm(t)) < 6 or not de:
            continue
        par[(l, norm(t))].append((f, ident, b, t, de, fr))
        toutes[(f, ident, b)][l] = norm(t)
def arbitres(e, e2, l):
    """combien d'AUTRES langues traduisent aussi les deux phrases a l'identique"""
    a, b = toutes[(e[0], e[1], e[2])], toutes[(e2[0], e2[1], e2[2])]
    return sum(1 for k in a if k != l and k in b and a[k] == b[k])
def mots(x):
    return set(w for w in re.findall(r"\w+", (x or "").lower()) if len(w) > 2)

def proches(a, b):
    # deux phrases qui partagent la moitie de leurs mots : variantes d'une meme phrase (temps,
    # ordre des mots), leur traduction commune n'a rien de suspect
    A, B = mots(a), mots(b)
    return not A or not B or len(A & B) / len(A | B) >= float(os.environ.get("SEUIL", "0.4"))

groupes = []
for (l, nt), es in par.items():
    # un enregistrement = son ident sans le champ : perfekt et praeteritum d'un meme verbe ne comptent qu'une fois
    paires = []
    for i, e in enumerate(es):
        for e2 in es[i + 1:]:
            if e[1] == e2[1] and e[0] == e2[0]:
                continue
            a1, a2 = e[1].split("/")[-1], e2[1].split("/")[-1]
            if "=" in a1 and a1 == a2:
                continue    # le meme verbe dans themes.json et verbe.json
            if proches(e[4], e2[4]) or proches(e[5], e2[5]):
                continue
            if arbitres(e, e2, l) > int(os.environ.get("ARBITRES", "99")):
                continue
            paires.append((e, e2))
    if paires:
        vus = []
        for e, e2 in paires:
            for x in (e, e2):
                if x not in vus: vus.append(x)
        groupes.append(dict(l=l, t=es[0][3], entrees=[dict(f=e[0], ident=e[1], champ=e[2], de=e[4], fr=e[5], t=e[3]) for e in vus]))
groupes.sort(key=lambda g: (g["l"], g["t"]))
from collections import Counter
print(len(groupes), "groupes :", dict(Counter(g["l"] for g in groupes)))
json.dump(groupes, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
