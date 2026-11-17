# -*- coding: utf-8 -*-
"""La traduction montree AVANT la reponse donne-t-elle la reponse ?

Pour chaque serie d'exercices a petit nombre de reponses (<= 6 distinctes), et chaque langue :
un mot de la traduction qui predit la bonne reponse a >= 95 % (au moins 4 exercices) est un indice.
taux = part des exercices de la serie ou un tel indice designe la bonne reponse.
On compare au francais, la langue de reference (deja acceptee).
    python tests/traduction_reponse.py . exercices.json fr,en,tr,uk,fa,ar,pt,pl,ru,es
    python tests/traduction_reponse.py . espanol/datos/ejercicios.json fr,en,pt,ar,de

Ne en revue des traductions du 15 nov. 2026 (regle du chef : « la traduction ne donne pas la reponse »).
Une serie signalee pour une langue se protege en marquant ses exercices `traductionApres_es` et en mettant
la langue dans LANGUES_TRADUCTION_APRES (index.html) : la traduction n'apparait qu'apres la reponse.
C'est une MESURE, pas un verdict : un indice peut etre legitime (le cas d'un pronom relatif slave).
"""
import io, json, re, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
R, F = sys.argv[1], sys.argv[2]
d = json.load(io.open(R + "/" + F, encoding="utf-8"))["jeux"]
LANGS = sys.argv[3].split(",")


def mots(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return set(w.lower() for w in re.findall(r"[^\W\d_]+", s))


def champ(e, l):
    if l == "fr":
        return e.get("translation")
    return e.get("translation_" + l)


res = []
for nom, exs in d.items():
    if not isinstance(exs, list) or len(exs) < 8:
        continue
    reps = [str(e.get("correct", "")).strip().lower() for e in exs]
    if len(set(reps)) > 6 or len(set(reps)) < 2:
        continue
    ligne = {}
    exemples = {}
    for l in LANGS:
        items = [(mots(champ(e, l)), r, e) for e, r in zip(exs, reps) if champ(e, l)]
        if len(items) < 8:
            continue
        c = collections.defaultdict(collections.Counter)
        for ws, r, e in items:
            for w in ws:
                c[w][r] += 1
        indices = {}
        for w, cnt in c.items():
            n = sum(cnt.values())
            a, k = cnt.most_common(1)[0]
            if n >= 4 and k / n >= 0.95 and n < len(items):
                indices[w] = a
        trahis = 0
        directs = 0
        for ws, r, e in items:
            if any(indices.get(w) == r for w in ws):
                trahis += 1
            if re.search(r"(?<!\w)" + re.escape(r) + r"(?!\w)", champ(e, l) or "", re.I) and l != "fr":
                directs += 1
        ligne[l] = (trahis / len(items), len(items), directs)
        exemples[l] = sorted(((w, a) for w, a in indices.items()), key=lambda x: x[1])[:12]
    if "fr" in ligne:
        res.append((nom, sorted(set(reps)), ligne, exemples))

for nom, reps, ligne, ex in res:
    fr = ligne["fr"][0]
    pires = [(l, v) for l, v in ligne.items() if l != "fr" and (v[0] - fr >= 0.25 or v[2] > 0)]
    if not pires:
        continue
    print("%s  reponses %s  fr %.0f %%" % (nom, "/".join(reps)[:60], 100 * fr))
    for l, v in sorted(pires, key=lambda x: -x[1][0]):
        print("    %s %3.0f %% de %d%s   indices : %s" % (l, 100 * v[0], v[1], ("  · %d citent la reponse allemande" % v[2]) if v[2] else "",
                                                     ", ".join("%s→%s" % wa for wa in ex[l])[:160]))
