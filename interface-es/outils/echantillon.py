# -*- coding: utf-8 -*-
"""L'echantillon de la relecture croisee : des cartes tirees dans chaque fichier et chaque niveau.

    python interface-es/outils/echantillon.py [graine]   -> interface-es/relecture/lot-NN.json (100 entrees chacun)

Comme pour le polonais (315 cartes, 94,6 % jugees bonnes) et le russe (96,4 %) : un tirage
reparti, relu par un AUTRE modele que celui qui a traduit, avant de decider s'il faut tout relire.
Les exercices et les fiches entrent aussi dans l'echantillon. Tirage fixe (graine), donc refaisable.
"""
import io, json, os, random, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "tests"))
import corpus_langue as C  # noqa: E402
rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 20261115)
entrees = []
# 1. Le corpus : 12 cartes par fichier et par niveau (moins s'il y en a moins).
for nom in C.FICHIERS:
    d, _ = C.charger(nom)
    par_niv = {}
    for i, (niv, ctx, m) in enumerate(C.cases(nom, d)):
        par_niv.setdefault(niv, []).append((i, ctx, m))
    for niv, lst in sorted(par_niv.items()):
        for i, ctx, m in rnd.sample(lst, min(12, len(lst))):
            e = {"id": "corpus|%s|%d" % (nom, i), "type": "carte", "mot": ((m.get("genre") or "") + " " + C.cle(m)).strip(),
                 "niveau": niv, "contexte": ctx, "fr": m.get("traduction", ""), "es": m.get("traduction_es", ""),
                 "phrase_de": m.get("exemple", ""), "phrase_es": m.get("exemple_es", "")}
            for t in ("perfekt", "praeteritum", "konjunktiv2"):
                if m.get(t):
                    e[t + "_de"], e[t + "_es"] = m[t], m.get(t + "_es", "")
            entrees.append(e)
# 2. Les exercices : 2 par jeu.
ex = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))
for jeu, lst in sorted(ex["jeux"].items()):
    for i in rnd.sample(range(len(lst)), min(2, len(lst))):
        e = lst[i]
        entrees.append({"id": "exo|%s|%d" % (jeu, i), "type": "exercice", "question_de": e.get("question", ""),
                        "reponse": e.get("correct", ""), "translation_es": e.get("translation_es", ""),
                        "explanation_fr": e.get("explanation", ""), "explanation_es": e.get("explanation_es", "")})
# 3. Les fiches : 30 textes.
g = json.load(io.open(os.path.join(RACINE, "grammaire.json"), encoding="utf-8"))["textes"]
for k in rnd.sample(sorted(g["es"]), 30):
    entrees.append({"id": "fiche|%s" % k, "type": "fiche", "fr": g["fr"][k], "es": g["es"][k]})
rnd.shuffle(entrees)
dossier = os.path.join(ICI, "relecture")
os.makedirs(dossier, exist_ok=True)
for k, deb in enumerate(range(0, len(entrees), 100), 1):
    io.open(os.path.join(dossier, "lot-%02d.json" % k), "w", encoding="utf-8").write(
        json.dumps(entrees[deb:deb + 100], ensure_ascii=False, indent=1) + "\n")
print("%d entrees en %d lots" % (len(entrees), k))
