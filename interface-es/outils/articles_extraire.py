# -*- coding: utf-8 -*-
"""Les exercices d'articles codes en dur dans index.html : sources a traduire et dump pour la pose.

    python interface-es/outils/articles_extraire.py

Ecrit :
  interface-es/sources/articles.json      [{cle, de, fr, en}] a traduire (219 textes)
  interface-es/sources/articles_dump.jsonl [cle, "", "", allemand] par ligne de tableau,
                                           le garde-fou de russe/outils/patch_articles.py
Les cles sont celles de patch_articles.py : « E|def.nom.m » (explications),
« D|sujet » (declencheurs), « R|<TABLEAU>|<rang> » et « M|<rang> » (phrases).
La pose : python russe/outils/patch_articles.py index.html es ru <t_es.json> <dump> --ecrire,
avec GENRES["es"] (interface-es/outils/patch_articles_es.py en est la copie).
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
src = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()


def bloc(debut):
    a = src.index(debut)
    return src[a:src.index("};" if debut.endswith("{") else "];", a)]


out, dump = [], []
# 1. Explications : "def.nom.m": ["fr", "en", ...]
for m in re.finditer(r'"((?:def|indef|neg)\.(?:nom|akk|dat|gen)\.(?:m|f|n|pl))":\s*\[(.*?)\]', bloc("const ARTICLE_EXPLICATIONS = {"), re.S):
    vals = json.loads("[" + m.group(2) + "]")
    out.append({"cle": "E|" + m.group(1), "de": m.group(1), "fr": vals[0], "en": vals[1]})
# 2. Declencheurs : sujet: ["fr", "en", ...]
for m in re.finditer(r'\n    (sujet|objet|verbe|preposition|possession):\s*\[(.*?)\]', bloc("const ARTICLE_DECLENCHEURS = {"), re.S):
    vals = json.loads("[" + m.group(2) + "]")
    out.append({"cle": "D|" + m.group(1), "de": m.group(1), "fr": vals[0], "en": vals[1]})
# 3. Les tableaux de phrases : [phrase, genre, fr, en, dico, tr, ...] et ARTICLES_MIX
#    [phrase, cas, famille, genre, decl, fr, en, dico, ...]
noms = sorted(set(re.findall(r"const (ARTICLES_[A-Z]+_(?:DEF|INDEF|NEG)) = \[", src)))
for nom in noms + ["ARTICLES_MIX"]:
    i = 0
    for ligne in bloc("const " + nom + " = [").split("\n"):
        l = ligne.strip()
        if not l.startswith('["'):
            continue
        row = json.loads(l.rstrip(","))
        if nom == "ARTICLES_MIX":
            cle, fr, en = "M|%d" % i, row[5], row[6]
        else:
            cle, fr, en = "R|%s|%d" % (nom, i), row[2], row[3]
        out.append({"cle": cle, "de": row[0], "fr": fr, "en": en})
        dump.append([cle, "", "", row[0]])
        i += 1
io.open(os.path.join(ICI, "sources", "articles.json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
with io.open(os.path.join(ICI, "sources", "articles_dump.jsonl"), "w", encoding="utf-8") as f:
    for d in dump:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
print("%d textes (%d explications, %d declencheurs, %d phrases)" % (
    len(out), sum(1 for x in out if x["cle"][0] == "E"), sum(1 for x in out if x["cle"][0] == "D"), len(dump)))
