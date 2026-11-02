# -*- coding: utf-8 -*-
"""L'ESPAGNOL des textes hors corpus et des exercices : des lots a la memoire (2 nov. 2026).

    python anglais/es/poser_textes.py controle [textes|exercices]
    python anglais/es/poser_textes.py pose [textes|exercices]

Sources (extraire.py) : sources/<palier>-textes.json, sources/<palier>-exercices.json
(a1-textes, a1-exercices...). Lots :
  lots/textes-NN.es.json     {cle: texte espagnol}
  lots/exercices-NN.es.json  {cle: [traduction espagnole, explication espagnole]}
Memoire : traductions/textes.json {cle: {"fr", "es"}}, traductions/exercices.json
{cle: {"tr_fr", "ex_fr", "tr", "ex"}}. Puis `python anglais/outils/espagnol.py` pose.

Garde-fous : cle connue d'une source ; texte non vide ; ni francais ni anglais
restes (doute_espagnol) ; marques {x} et balises <b> du francais conservees.
"""
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
LOTS = os.environ.get("ESSAI_LOTS") or os.path.join(ICI, "lots")
sys.path.insert(0, ICI)
from poser_autres import doute_espagnol, balises, MARQUE   # noqa: E402


def sources(genre):
    out = {}
    for c in sorted(glob.glob(os.path.join(ICI, "sources", "*-%s.json" % genre))):
        for e in json.load(io.open(c, encoding="utf-8")):
            out[e["id"]] = e
    return out


def lots(genre):
    out = {}
    for c in sorted(glob.glob(os.path.join(LOTS, "%s-*.es.json" % genre))):
        for k, v in json.load(io.open(c, encoding="utf-8")).items():
            if k in out and out[k] != v:
                raise SystemExit("%s : %s traduit deux fois, differemment" % (genre, k))
            out[k] = v
    return out


def verifier(id_, fr, es, fautes, avis, en=""):
    if not isinstance(es, str) or not es.strip():
        if (fr or "").strip():
            fautes.append("%s : vide" % id_)
        return
    d = doute_espagnol(es, fr, en)
    if d:
        (fautes if d.startswith("identique") else avis).append("%s : %s : %s" % (id_, d, es[:70]))
    if sorted(MARQUE.findall(es)) != sorted(MARQUE.findall(fr)):
        fautes.append("%s : marques %s au lieu de %s" % (id_, MARQUE.findall(es), MARQUE.findall(fr)))
    if balises(es) != balises(fr):
        avis.append("%s : balises %s (fr %s)" % (id_, balises(es), balises(fr)))


def controler(genre):
    src, trad = sources(genre), lots(genre)
    fautes, avis = [], []
    for k in sorted(set(trad) - set(src)):
        fautes.append("cle inconnue : " + k)
    for k, v in trad.items():
        e = src.get(k)
        if not e:
            continue
        if genre == "textes":
            verifier(k, e["fr"], v, fautes, avis)
        else:
            if not isinstance(v, list) or len(v) != 2:
                fautes.append("%s : [traduction, explication] attendus" % k)
                continue
            verifier(k + " (traduction)", e["translation"], v[0], fautes, avis, e["question"])
            verifier(k + " (explication)", e["explanation"], v[1], fautes, avis)
    return src, trad, fautes, avis


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("controle", "pose"):
        raise SystemExit(__doc__)
    genres = sys.argv[2:] or ["textes", "exercices"]
    total, res = 0, {}
    for g in genres:
        src, trad, fautes, avis = controler(g)
        res[g] = (src, trad)
        total += len(fautes)
        print("%-10s %5d traduits sur %5d, %d faute(s), %d avis" % (g, len(trad), len(src), len(fautes), len(avis)))
        for x in fautes[:40]:
            print("  FAUTE", x)
        for x in avis[:25]:
            print("  avis ", x)
    if sys.argv[1] == "controle":
        return
    if total:
        raise SystemExit("Des fautes : rien n'est ecrit.")
    os.makedirs(os.path.join(ICI, "traductions"), exist_ok=True)
    for g, (src, trad) in res.items():
        chemin = os.path.join(ICI, "traductions", g + ".json")
        mem = json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else {}
        for k, v in trad.items():
            if g == "textes":
                mem[k] = {"fr": src[k]["fr"], "es": v.strip()}
            else:
                mem[k] = {"tr_fr": src[k]["translation"], "ex_fr": src[k]["explanation"], "tr": v[0].strip(), "ex": v[1].strip()}
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(dict(sorted(mem.items())), fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print("Ecrit :", chemin, "(%d)" % len(mem))
    print("Puis : python anglais/outils/espagnol.py")


if __name__ == "__main__":
    main()
