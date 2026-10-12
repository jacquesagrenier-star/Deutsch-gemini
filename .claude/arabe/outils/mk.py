# Brouillon ligne a ligne -> b_<jeu>.json pour exos_convertir.py
#   python mk.py <jeu> <moules.json|-> <lignes.txt>
# ligne : debut|traduction[|explication ou *][|{extras json}]
import io, json, sys, os
jeu, mfile, lfile = sys.argv[1:4]
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
    if len(p) > 3:
        ent.append(json.loads("|".join(p[3:])))
    e.append(ent)
ici = os.path.dirname(os.path.abspath(__file__))
json.dump({"jeu": jeu, "moules": moules, "e": e}, io.open(os.path.join(ici, "b_" + jeu + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
