# -*- coding: utf-8 -*-
"""L'ESPAGNOL du corpus anglais : des lots traduits a la memoire (2 nov. 2026).

    python anglais/es/poser.py etat                       # ce qui est traduit, par fichier
    python anglais/es/poser.py controle [fichier ...]     # lit les lots, n'ecrit rien
    python anglais/es/poser.py pose [fichier ...]         # ecrit anglais/es/traductions/

Sources : anglais/es/sources/corpus-<fichier>.json (extraire.py). Lots :
anglais/es/lots/corpus-<fichier>-NN.es.json = {cle: [traduction_es, exemple_es]} ; quand
l'Espagne dit autrement (coche / carro), deux colonnes de plus : [.., .., traduction
d'Espagne, phrase d'Espagne] (vide = comme l'Amerique latine).
Memoire : anglais/es/traductions/corpus.json = {cle: {"ex", "t", "e"}} (ex = la
phrase anglaise traduite, temoin). Puis `python anglais/outils/espagnol.py`
pose la memoire dans anglais/datos et datos-gb (construire.py le fait aussi).

Garde-fous (une faute arrete tout, rien n'est ecrit) :
  - chaque cle d'un lot existe dans la source ; aucune traduite deux fois differemment ;
  - traduction et phrase non vides (la phrase seulement si l'anglais en a une) ;
  - ni francais ni anglais restes (doute_espagnol de poser_autres.py) ;
  - deux cartes d'un meme groupe (theme, niveau) ne recoivent pas la meme
    traduction quand leurs mots anglais different : la carte serait indecidable.
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
MEMOIRE = os.path.join(ICI, "traductions", "corpus.json")
FICHIERS = ["themes", "verbes", "adjectifs", "adverbes", "expressions", "fonctionnels"]
sys.path.insert(0, ICI)
from poser_autres import doute_espagnol   # noqa: E402


def source(f):
    return json.load(io.open(os.path.join(ICI, "sources", "corpus-%s.json" % f), encoding="utf-8"))


def lots(f):
    out = {}
    for c in sorted(glob.glob(os.path.join(LOTS, "corpus-%s-*.es.json" % f))):
        for k, v in json.load(io.open(c, encoding="utf-8")).items():
            if k in out and out[k] != v:
                raise SystemExit("%s : %s traduit deux fois, differemment" % (f, k))
            out[k] = v
    return out


def memoire():
    if not os.path.exists(MEMOIRE):
        return {}
    return json.load(io.open(MEMOIRE, encoding="utf-8"))


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", "", s or "")).strip().lower()


def controler(f):
    src = {e["id"]: e for e in source(f)}
    trad = lots(f)
    fautes, avis = [], []
    for k in sorted(set(trad) - set(src)):
        fautes.append("%s : cle inconnue %s" % (f, k))
    for k, v in trad.items():
        e = src.get(k)
        if not e:
            continue
        if not isinstance(v, list) or len(v) not in (2, 4):
            fautes.append("%s %s : [traduction, phrase] ou [.., .., Espagne, Espagne] attendus" % (f, k))
            continue
        t, ex = v[0], v[1]
        if len(v) == 4 and not (v[2] or v[3]):
            avis.append("%s %s : colonnes d'Espagne vides" % (f, k))
        if not (t or "").strip():
            fautes.append("%s %s : traduction vide" % (f, k))
        if e["ex"] and not (ex or "").strip():
            fautes.append("%s %s : phrase vide" % (f, k))
        for quoi, es, fr, en in (("traduction", t, e["fr"], e["mot"]), ("phrase", ex, e["ex_fr"], e["ex"])):
            d = doute_espagnol(es or "", fr or "", en or "")
            if d:
                (fautes if d.startswith("identique") else avis).append("%s %s : %s : %s : %s" % (f, k, quoi, d, (es or "")[:60]))
        if ex and ex.strip() == e["ex"].strip():
            fautes.append("%s %s : phrase restee en anglais" % (f, k))
    # Cartes indecidables : meme groupe, mots anglais differents, meme reponse.
    par_groupe = {}
    for k, v in trad.items():
        if k in src and isinstance(v, list) and v[0]:
            groupe = k.split("|")[1]
            par_groupe.setdefault((groupe, norm(v[0])), []).append((src[k]["mot"].lower(), norm(src[k]["fr"])))
    for (groupe, t), cartes in par_groupe.items():
        mots = {m for m, _ in cartes}
        if len(mots) > 1:
            # Le francais les departageait-il ? Sinon le defaut est deja dans la source.
            qui = fautes if len({fr for _, fr in cartes}) > 1 else avis
            qui.append("%s %s : « %s » pour %s (carte indecidable)" % (f, groupe, t, " / ".join(sorted(mots))))
    return src, trad, fautes, avis


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("etat", "controle", "pose"):
        raise SystemExit(__doc__)
    mode, veut = sys.argv[1], sys.argv[2:] or FICHIERS
    mem = memoire()
    if mode == "etat":
        for f in FICHIERS:
            src = source(f)
            n = sum(1 for e in src if e["id"] in mem and mem[e["id"]].get("ex") == e["ex"])
            print("%-13s %5d / %5d" % (f, n, len(src)))
        return
    total = 0
    resultats = {}
    for f in veut:
        src, trad, fautes, avis = controler(f)
        resultats[f] = (src, trad)
        total += len(fautes)
        print("%-13s %5d traduites sur %5d, %d faute(s), %d avis" % (f, len(trad), len(src), len(fautes), len(avis)))
        for x in fautes[:40]:
            print("  FAUTE", x)
        for x in avis[:25]:
            print("  avis ", x)
    if mode == "controle":
        return
    if total:
        raise SystemExit("Des fautes : rien n'est ecrit.")
    for f, (src, trad) in resultats.items():
        for k, v in trad.items():
            mem[k] = {"ex": src[k]["ex"], "t": v[0].strip(), "e": (v[1] or "").strip()}
            if len(v) == 4 and (v[2] or v[3]):
                mem[k]["tE"], mem[k]["eE"] = (v[2] or v[0]).strip(), (v[3] or v[1] or "").strip()
    os.makedirs(os.path.dirname(MEMOIRE), exist_ok=True)
    with io.open(MEMOIRE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(dict(sorted(mem.items())), fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("Ecrit :", MEMOIRE, "(%d cartes) -- puis : python anglais/outils/espagnol.py" % len(mem))


if __name__ == "__main__":
    main()
