"""Construit la page de choix des tableaux portugais (29 oct. 2026), sur le
modele de la page des tableaux americains : choix-modele.html + les vignettes
de candidats.json, traitees « vif » (comme dans l'app), en fichiers a cote.

  python portugais/mosaique/construire_choix.py <dossier de sortie>
      ->  <dossier>/index.html + <dossier>/img/<num>.jpg

La page n'est pas versionnee (plusieurs Mo d'images) : elle se publie comme
artefact. Jacques touche les tableaux dans l'ordre voulu et colle son choix
(« n° 3, 12, E4... ») dans la conversation.
"""
import json, os, sys
from PIL import Image
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

GROUPES = [
    {"id": "libre", "titre": "Libres partout",
     "sous": "N° 1 à {n} · peintres morts avant 1926, la règle de l'espagnol (le Mexique protège "
             "100 ans) : rien à vérifier, où que l'app soit vue. {peintres}.",
     "bouton": "Prendre tous les libres partout (1 à {n})"},
    {"id": "europe", "titre": "À décider : libres en Europe",
     "sous": "N° E1 à E{n} · peintres morts <b>entre 1926 et 1955</b> (Malhoa, Columbano, Sousa Pinto…), "
             "œuvres d'avant 1931. Libres au Portugal, en Europe et aux États-Unis, mais pas encore au "
             "Mexique ni dans les pays qui protègent plus de 70 ans. C'est toi qui décides. {peintres}.",
     "bouton": "Prendre tous les libres en Europe (E1 à E{n})"},
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sortie = sys.argv[1]
    os.makedirs(os.path.join(sortie, "img"), exist_ok=True)
    c = json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))
    donnees = []
    for t in c:
        im = recolter.vif(Image.open(os.path.join(recolter.BRUT, "v-" + t["cle"] + ".jpg")).convert("RGB"))
        if im.width > 400:
            im = im.resize((400, round(400 * im.height / im.width)), Image.LANCZOS)
        nom = "img/%s.jpg" % t["num"].lower()
        im.save(os.path.join(sortie, nom), "JPEG", quality=70, optimize=True)
        titre = t["titre"] or t["titre_en"] or t["titre_fr"] or "Sans titre"
        fr = t["titre_fr"] if t["titre_fr"] and t["titre_fr"].lower() != titre.lower() else ""
        donnees.append({"n": t["num"], "g": t["groupe"], "p": t["peintre"], "m": t["mort"],
                        "t": titre[:90], "f": fr[:90], "a": t.get("annee") or "",
                        "c": (t["collection"] or [""])[0][:60], "i": nom,
                        "s": t["l"] if t.get("petite") else 0})
    groupes = []
    for g in GROUPES:
        lot = [d for d in donnees if d["g"] == g["id"]]
        par = {}
        for d in lot:
            par[d["p"]] = par.get(d["p"], 0) + 1
        peintres = ", ".join("%s %d" % kv for kv in sorted(par.items(), key=lambda x: -x[1]))
        groupes.append({k: (v.format(n=len(lot), peintres=peintres) if isinstance(v, str) else v)
                        for k, v in g.items()})
    modele = open(os.path.join(ICI, "choix-modele.html"), encoding="utf-8").read()
    assert modele.count("/*DONNEES*/[]") == 1 and modele.count("/*GROUPES*/[]") == 1
    # json.dumps echappe ce qu'il faut ; « </ » est neutralise pour la balise script.
    js = lambda x: json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
    page = modele.replace("/*DONNEES*/[]", js(donnees)).replace("/*GROUPES*/[]", js(groupes))
    open(os.path.join(sortie, "index.html"), "w", encoding="utf-8").write(page)
    print(len(donnees), "tableaux :", ", ".join("%s %d" % (g["id"], sum(d["g"] == g["id"] for d in donnees))
                                                 for g in GROUPES))


if __name__ == "__main__":
    main()
