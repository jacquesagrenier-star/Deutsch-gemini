# -*- coding: utf-8 -*-
"""Verse une couche de scenes ecrite en texte compact dans anglais/scenes/<scene>.json.

    python anglais/outils/couches_texte.py B1 chemin/vers/b1_scenes.txt

Le texte est un BROUILLON de redaction : une fois verse, la source est le JSON
de chaque scene (anglais/scenes/), qu'on corrige directement. Relancer ce
script ecrase la couche de ce niveau dans chaque scene citee.

Format du texte :
    ## <scene> | <titre de la couche>
    question avec ___ | bonne | fausse 1 / fausse 2 | f | r | phrase | sens | note

f est la zone visee, r le repere (vide si aucun) : ils doivent exister dans la
scene, sinon le script le dit et n'ecrit rien.
"""
import io, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import scenes as S


def lire(chemin):
    blocs, courant = {}, None
    for l in io.open(chemin, encoding="utf-8").read().splitlines():
        l = l.strip()
        if not l or l.startswith("# "):
            continue
        if l.startswith("## "):
            nom, _, titre = l[3:].partition("|")
            courant = nom.strip()
            blocs[courant] = {"titre": titre.strip(), "qs": []}
            continue
        cols = [c.strip() for c in l.split("|")]
        while len(cols) > 8 and "" in cols[5:]:
            cols.pop(cols.index("", 5))
        if len(cols) != 8:
            raise SystemExit("ligne mal formee (%d colonnes) : %s" % (len(cols), l))
        q, bonne, fausses, f, r, phrase, sens, note = cols
        e = {"q": q, "c": [bonne] + [x.strip() for x in fausses.split("/")], "f": f}
        if r:
            e["r"] = r
        e.update({"phrase": phrase, "sens": sens, "n": note})
        blocs[courant]["qs"].append(e)
    return blocs


def main():
    niv, chemin = sys.argv[1].upper(), sys.argv[2]
    blocs = lire(chemin)
    fautes = 0
    for nom, couche in blocs.items():
        ids = {p.get("id") for p in S.charger_scene(nom)["points"]}
        for q in couche["qs"]:
            for cle in ("f", "r"):
                if q.get(cle) and q[cle] not in ids:
                    print("  %s : zone inconnue %s=%s (%s)" % (nom, cle, q[cle], q["q"]))
                    fautes += 1
            if len(set(q["c"])) != len(q["c"]):
                print("  %s : choix en double (%s)" % (nom, q["q"]))
                fautes += 1
    if fautes:
        raise SystemExit("%d faute(s) : rien n'est ecrit." % fautes)
    n = 0
    for nom, couche in blocs.items():
        p = os.path.join(RACINE, "anglais", "scenes", nom + ".json")
        d = json.load(io.open(p, encoding="utf-8"))
        d["couches"][niv] = couche
        io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        n += len(couche["qs"])
    print("%s : %d questions dans %d scenes." % (niv, n, len(blocs)))


if __name__ == "__main__":
    main()
