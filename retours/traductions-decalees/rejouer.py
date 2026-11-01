# -*- coding: utf-8 -*-
# TRADUCTIONS PERIMEES, version generale (tous les fichiers, tous les champs traduits).
# Generalise traductions_perimees.py du chef d'orchestre (1er nov. 2026).
#
# Pour chaque traduction T (champ <base>_<langue>, ou valeur d'un dict {fr, en, uk...}), on calcule
# sa SOURCE = (texte allemand qu'elle traduit, texte francais de reference). On rejoue l'historique
# git du fichier : la source en face de laquelle T est apparue pour la premiere fois est sa source
# « de naissance ». Si la source actuelle differe, T est candidate (a trier : une virgule ne compte pas).
#
#   python rejouer.py <fichier.json> <sortie.json> [langues]
import json, subprocess, sys, re
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
FICHIER, SORTIE = sys.argv[1], sys.argv[2]
LANGUES = (sys.argv[3] if len(sys.argv) > 3 else "fr,en,tr,uk,fa,ar,pt,pl,ru").split(",")
RL = re.compile(r"^(.+?)_(%s)$" % "|".join(LANGUES))
IGNORE = {"article", "kategorie", "er_sie", "sie", "options_correct"}
ANCRES = ("id", "mot", "infinitif", "palabra", "infinitivo", "cle", "nom", "serie", "key")
CONTEXTE = ("exemple", "ejemplo", "question", "pregunta", "audio", "texte", "text", "frage", "chunks",
            "aufgabe", "satz", "phrase", "p", "mot", "infinitif", "palabra", "infinitivo", "de", "es")

def s(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, sort_keys=True)

def contexte(d, parent):
    for o in (d, parent):
        if isinstance(o, dict):
            for k in CONTEXTE:
                if k in o and isinstance(o[k], (str, list)):
                    v = s(o[k])
                    if k in ("question", "pregunta") and "correct" in o:
                        v += " | " + s(o["correct"])
                    return v
    return ""

def traductions(o, ident="", parent=None):
    """produit (ident, champ, langue, T, allemand, francais)"""
    if isinstance(o, dict):
        ks = o.keys()
        # 1. champs <base>_<langue>
        for k, v in o.items():
            m = RL.match(k)
            if not m or not isinstance(v, (str, list)) or not v:
                continue
            b, l = m.group(1), m.group(2)
            if b in IGNORE or k.endswith("Highlight"):
                continue
            if b in ks and (b + "_fr") in ks or (b in ks and isinstance(o[b], str) and l == "fr"):
                de = s(o[b]); fr = s(o.get(b + "_fr", "")) if l != "fr" else ""   # base allemande
            elif b in ks:
                # base francaise (traduction, translation, hint, explanation)
                de = contexte(o, parent) if b not in ("traduction", "traduccion") else s(o.get("mot") or o.get("infinitif") or o.get("palabra") or o.get("infinitivo") or "")
                fr = s(o[b])
            else:
                de = contexte(o, parent)
                fr = s(o.get(b + "_fr", "")) if l != "fr" else ""
            yield ident, b, l, s(v), de, fr
        # 2. dicts de langues
        for k, v in o.items():
            if isinstance(v, dict) and sum(1 for l in LANGUES if l in v) >= 3:
                de = ""
                if k == "s" and isinstance(o.get("p"), str): de = o["p"]
                elif k.endswith("s") and isinstance(o.get(k[:-1]), str): de = o[k[:-1]]
                elif k == "n" or k == "sens":
                    de = contexte(o, parent)
                for l in LANGUES:
                    if isinstance(v.get(l), (str, list)) and v.get(l):
                        yield ident + "/" + k, "{}", l, s(v[l]), de, (s(v.get("fr", "")) if l != "fr" else "")
            elif isinstance(v, list) and k.endswith("s") and isinstance(o.get(k[:-1]), list):
                # vs[i] traduit v[i]
                for i, e in enumerate(v):
                    if isinstance(e, dict) and sum(1 for l in LANGUES if l in e) >= 3:
                        src = o[k[:-1]][i] if i < len(o[k[:-1]]) else ""
                        de = s(o.get("p", "")) + " + " + s(src)
                        for l in LANGUES:
                            if isinstance(e.get(l), (str, list)) and e.get(l):
                                yield ident + "/" + k + "/" + str(i), "{}", l, s(e[l]), de, (s(e.get("fr", "")) if l != "fr" else "")
        for k, v in o.items():
            if isinstance(v, list) and k.endswith("s") and isinstance(o.get(k[:-1]), list):
                continue   # vs : deja traite ci-dessus
            if isinstance(v, (dict, list)) and not (isinstance(v, dict) and sum(1 for l in LANGUES if l in v) >= 3):
                if k in LANGUES and isinstance(v, dict):
                    continue   # grammaire.json textes : traite a part
                yield from traductions(v, ident + "/" + k, o)
    elif isinstance(o, list):
        vus = defaultdict(int)
        for i, e in enumerate(o):
            if isinstance(e, dict) and sum(1 for l in LANGUES if l in e) >= 3:
                # dict de langues dans une liste : l'allemand est l'element precedent
                de = o[i - 1] if i > 0 and isinstance(o[i - 1], str) else ""
                if de or not isinstance(parent, dict) or True:
                    for l in LANGUES:
                        if isinstance(e.get(l), (str, list)) and e.get(l):
                            yield ident + "/" + str(i), "{}", l, s(e[l]), s(de), (s(e.get("fr", "")) if l != "fr" else "")
                continue
            a = ""
            if isinstance(e, dict):
                for k in ANCRES:
                    if isinstance(e.get(k), str):
                        a = k + "=" + e[k]; break
            if a:
                vus[a] += 1
                a = a + ("#" + str(vus[a]) if vus[a] > 1 else "")
            else:
                a = str(i)
            yield from traductions(e, ident + "/" + a, parent if not isinstance(e, dict) else o)

def textes_grammaire(d):
    t = d.get("textes") if isinstance(d, dict) else None
    if not isinstance(t, dict) or "fr" not in t:
        return
    for l, dl in t.items():
        if l == "fr" or l not in LANGUES or not isinstance(dl, dict):
            continue
        for k, v in dl.items():
            if isinstance(v, str) and v:
                yield "/textes/" + k, "textes", l, v, "", s(t["fr"].get(k, ""))

def tout(d):
    yield from traductions(d)
    yield from textes_grammaire(d)

commits = subprocess.run(["git", "log", "--reverse", "--format=%H", "--", FICHIER],
                         capture_output=True, text=True, encoding="utf-8").stdout.split()
ne1 = {}            # (ident, champ, langue, T) -> (de, fr, commit) a la naissance
ne2 = {}            # (champ, langue, T) -> (de, fr, commit)  (repere sans chemin)
ne3 = {}            # (mot, champ, langue, T) -> (de, fr, commit)  (la methode du chef : le mot, pas le chemin)
def ancre(ident):
    for p in reversed(ident.split("/")):
        if "=" in p:
            return p.split("#")[0]
    return ""
proc = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
for h in commits:
    proc.stdin.write((h + ":" + FICHIER + "\n").encode()); proc.stdin.flush()
    tete = proc.stdout.readline().split()
    if len(tete) < 3 or tete[1] != b"blob":
        continue
    brut = proc.stdout.read(int(tete[2])); proc.stdout.read(1)
    try:
        d = json.loads(brut.decode("utf-8"))
    except Exception:
        continue
    for ident, b, l, t, de, fr in tout(d):
        ne1.setdefault((ident, b, l, t), (de, fr, h[:9]))
        ne2.setdefault((b, l, t), (de, fr, h[:9]))
        ne3.setdefault((ancre(ident), b, l, t), (de, fr, h[:9]))
proc.stdin.close()

import os
d = json.load(open(os.environ.get("ACTUEL", FICHIER), encoding="utf-8"))
actuels = set((b, l, t, de, fr) for ident, b, l, t, de, fr in tout(d))
cands = []
n = 0
for ident, b, l, t, de, fr in tout(d):
    n += 1
    x = ne1.get((ident, b, l, t))
    sorte = ""
    if x and (x[0], x[1]) != (de, fr):
        sorte = "chemin"
    else:
        y = ne2.get((b, l, t))
        if y and (y[0], y[1]) != (de, fr) and (b, l, t, y[0], y[1]) not in actuels:
            x = y; sorte = "texte"
        else:
            z = ne3.get((ancre(ident), b, l, t))
            if z and z[0] != de:
                x = z; sorte = "mot"
    if sorte:
        cands.append(dict(f=FICHIER, ident=ident, champ=b, l=l, t=t, de=de, fr=fr,
                          de0=x[0], fr0=x[1], ne=x[2], sorte=sorte))
par = defaultdict(int)
for c in cands:
    par[c["l"]] += 1
print(FICHIER, len(commits), "versions,", n, "traductions,", len(cands), "candidates :", dict(par))
json.dump(cands, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
