# Brouillon ligne a ligne -> b_<jeu>.json pour exos_convertir.py
#   python mk.py <jeu> <moules.json|-> <lignes.txt> [options.json]
# ligne : debut|traduction[|explication ou *][|{extras json}]
# options.json : {"francais": "arabe"} -- correct/options du releve traduits par table.
import io, json, sys, os
jeu, mfile, lfile = sys.argv[1:4]
O = json.load(io.open(sys.argv[4], encoding="utf-8")) if len(sys.argv) > 4 else None
ici = os.path.dirname(os.path.abspath(__file__))
rel = [json.loads(l) for l in io.open(os.path.join(ici, jeu + ".txt"), encoding="utf-8") if l.strip()]
moules = json.load(io.open(mfile, encoding="utf-8")) if mfile != "-" else []
e = []
for n, l in enumerate(io.open(lfile, encoding="utf-8"), 1):
    l = l.rstrip("\n")
    if not l.strip() or l.startswith("#"):
        continue
    p = l.split("|")
    debut, trad = p[0], p[1]
    expl = p[2] if len(p) > 2 and p[2] else "*"
    ent = [debut, trad, expl]
    ex = json.loads("|".join(p[3:])) if len(p) > 3 else {}
    if O is not None and len(e) < len(rel):
        r = rel[len(e)]
        if "correct" in r and "correct" not in ex:
            ex["correct"] = O[r["correct"]["fr"]]
        if "options" in r and "options" not in ex:
            ex["options"] = [O[o] for o in r["options"]["fr"]]
    if ex:
        ent.append(ex)
    e.append(ent)
json.dump({"jeu": jeu, "moules": moules, "e": e}, io.open(os.path.join(ici, "b_" + jeu + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
