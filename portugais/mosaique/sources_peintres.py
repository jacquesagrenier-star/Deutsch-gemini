"""Le resume Wikipedia (fr, pt et en) de chaque peintre de selection.json,
d'apres lequel les notices de app/peintres.json sont ecrites -- comme
l'espagnol et l'anglais : rien qui ne soit dans ces resumes.

  python portugais/mosaique/sources_peintres.py  ->  sources_peintres.json
"""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter


def resume(langue, titre):
    d = recolter.get("https://%s.wikipedia.org/w/api.php" % langue, {"action": "query", "format": "json",
        "prop": "extracts", "exintro": 1, "explaintext": 1, "redirects": 1, "titles": titre})
    p = next(iter(d["query"]["pages"].values()))
    return p.get("extract", "")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sel = json.load(open(os.path.join(ICI, "selection.json"), encoding="utf-8"))["tableaux"]
    peintres = {}
    for t in sel:
        peintres.setdefault(t["peintre"], t["wikidata_peintre"])
    sortie = {}
    for nom, q in peintres.items():
        d = recolter.get("https://www.wikidata.org/w/api.php", {"action": "wbgetentities", "ids": q,
            "props": "sitelinks", "format": "json"})
        liens = d["entities"][q].get("sitelinks", {})
        sortie[nom] = {"wikidata": q}
        for l in ("fr", "pt", "en"):
            sortie[nom][l] = resume(l, liens[l + "wiki"]["title"]) if l + "wiki" in liens else ""
        print(nom, q, {l: len(sortie[nom][l]) for l in ("fr", "pt", "en")})
    json.dump(sortie, open(os.path.join(ICI, "sources_peintres.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
