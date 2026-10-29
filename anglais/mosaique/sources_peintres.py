"""Le resume Wikipedia (en, et fr quand il existe) de chaque peintre de
selection.json, d'apres lequel les notices de peintres.json sont ecrites --
comme l'espagnol (sources_peintres.json) : rien qui ne soit dans ces resumes.

  python anglais/mosaique/sources_peintres.py  ->  sources_peintres.json
"""
import json, os, sys, urllib.parse
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter


def resume(langue, titre):
    d = recolter.get("https://%s.wikipedia.org/w/api.php" % langue, {"action": "query", "format": "json",
        "prop": "extracts", "exintro": 1, "explaintext": 1, "redirects": 1, "titles": titre})
    p = next(iter(d["query"]["pages"].values()))
    return p.get("extract", "")


def main():
    sel = json.load(open(os.path.join(ICI, "selection.json"), encoding="utf-8"))["tableaux"]
    peintres = []
    for t in sel:
        if t["peintre"] not in peintres:
            peintres.append(t["peintre"])
    sortie = {}
    for nom in peintres:
        q = recolter.QID_CONNUS.get(nom) or recolter.qid(nom)
        d = recolter.get("https://www.wikidata.org/w/api.php", {"action": "wbgetentities", "ids": q,
            "props": "sitelinks", "format": "json"})
        liens = d["entities"][q].get("sitelinks", {})
        sortie[nom] = {"wikidata": q,
                       "en": resume("en", liens["enwiki"]["title"]) if "enwiki" in liens else "",
                       "fr": resume("fr", liens["frwiki"]["title"]) if "frwiki" in liens else ""}
        print(nom, q, len(sortie[nom]["en"]), len(sortie[nom]["fr"]))
    json.dump(sortie, open(os.path.join(ICI, "sources_peintres.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
