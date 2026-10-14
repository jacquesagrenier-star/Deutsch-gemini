"""Le resume Wikipedia de chaque peintre de la mosaique espagnole, pour ecrire
les notices d'apres une source et non de memoire (meme methode que le
japonais). Ecrit sources_peintres.json : fr, es et en quand ils existent.
"""
import json, os, sys, urllib.parse
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

peintres = sorted({x["peintre"] for x in json.load(open(os.path.join(ICI, "mosaiques.json"), encoding="utf-8"))["images"]})
sortie = {}
for nom in peintres:
    q = recolter.qid(nom)
    d = recolter.get("https://www.wikidata.org/w/api.php", {"action": "wbgetentities", "ids": q, "props": "sitelinks", "format": "json"})
    liens = d["entities"][q].get("sitelinks", {})
    textes = {}
    for lang in ("fr", "es", "en"):
        s = liens.get(lang + "wiki")
        if not s:
            continue
        titre = urllib.parse.quote(s["title"].replace(" ", "_"))
        try:
            r = recolter.get("https://%s.wikipedia.org/api/rest_v1/page/summary/%s" % (lang, titre))
            textes[lang] = r.get("extract", "")
        except Exception as e:
            textes[lang] = ""
    sortie[nom] = {"wikidata": q, "textes": textes}
    print(nom, q, {k: len(v) for k, v in textes.items()})
json.dump(sortie, open(os.path.join(ICI, "sources_peintres.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
