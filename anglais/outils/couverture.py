# -*- coding: utf-8 -*-
"""L'A1 anglais couvre-t-il l'A1 allemand ? (consigne de Jacques, 27 oct. 2026 :
« tous les mots » ; l'anglais au moins aussi large que l'allemand a chaque niveau.)

    python anglais/outils/couverture.py [NIVEAU]

Pour chaque categorie, chaque entree allemande du niveau est cherchee dans
l'anglais par sa traduction anglaise (toutes les variantes : « wife, woman »),
apres avoir retire l'article et « to ». Ce qui manque est liste avec son sens
francais : c'est la liste de travail, a juger mot par mot (un mot propre a
l'Allemagne -- Pfand, Bürgeramt -- n'a pas a etre copie).
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def lire(p):
    with io.open(os.path.join(RACINE, p), encoding="utf-8") as f:
        return json.load(f)


def tetes(en):
    en = re.sub(r"\(.*?\)", "", en or "")
    out = []
    for p in re.split(r"[,;/]", en):
        p = re.sub(r"^\s*(the|a|an|to)\s+", "", p.strip(), flags=re.I).strip().lower()
        p = re.sub(r"[.!?]+$", "", p)
        if p:
            out.append(p)
    return out


def anglais(niveau):
    d = {}
    th = lire("anglais/datos/themes.json")["themes"]
    d["noms"] = {m["mot"].lower() for t in th if t["niveau"] == niveau for m in t["mots"]}
    for cat, f in (("verbes", "verbes"), ("adjectifs", "adjectifs"), ("adverbes", "adverbes"), ("expressions", "expressions")):
        d[cat] = {re.sub(r"[.!?]+$", "", e["mot"].lower()) for e in lire("anglais/datos/%s.json" % f).get(niveau, [])}
    tous = set().union(*d.values())
    fw = lire("anglais/datos/fonctionnels.json")
    tous |= {e["mot"].lower() for v in fw.values() for e in v if e.get("niveau", "A1") == niveau}
    return d, tous


def allemand(niveau):
    d = {}
    th = lire("themes.json")["themes"]
    d["noms"] = [m for t in th if t["niveau"].upper() == niveau for m in t["mots"]]
    for cat, f in (("verbes", "verbe.json"), ("adjectifs", "adjectif.json"), ("adverbes", "adverbe.json"),
                   ("expressions", "redewendung.json")):
        d[cat] = lire(f).get(niveau, [])
    return d


def main():
    niveau = (sys.argv[1] if len(sys.argv) > 1 else "A1").upper()
    en, tous = anglais(niveau)
    de = allemand(niveau)
    print("Niveau %s : anglais / allemand" % niveau)
    for cat in ("noms", "verbes", "adjectifs", "adverbes", "expressions"):
        manque = []
        for e in de[cat]:
            t = tetes(e.get("traduction_en"))
            if not t or any(x in en[cat] or x in tous for x in t):
                continue
            manque.append("%s (%s = %s)" % (t[0], e.get("mot") or e.get("infinitif"), e.get("traduction")))
        print("== %-11s %4d / %4d   non couverts : %d" % (cat, len(en[cat]), len(de[cat]), len(manque)))
        for m in manque:
            print("     " + m)


if __name__ == "__main__":
    main()
