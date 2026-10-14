"""Construit la page de choix des tableaux espagnols (14 oct. 2026), sur le
modele de la planche allemande : choix-modele.html + les vignettes de
candidats.json, traitees « vif », incrustees en data URI.

  python construire_choix.py <fichier de sortie .html>

La page n'est pas versionnee (plusieurs Mo d'images) : elle se publie comme
artefact et garde le choix de Jacques dans son stockage (document
choix/selection, champ nums).
"""
import base64, io, json, os, sys
from PIL import Image
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

c = json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))
donnees = []
for t in c:
    im = recolter.vif(Image.open(os.path.join(recolter.BRUT, "v-" + t["cle"] + ".jpg")).convert("RGB"))
    if im.width > 300:
        im = im.resize((300, round(300 * im.height / im.width)), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, "JPEG", quality=62, optimize=True)
    titre = t["titre"] or t["titre_en"] or "Sans titre"
    donnees.append({"n": t["num"], "p": t["peintre"], "c": t["pays"], "t": titre[:90],
                    "a": t.get("annee") or "",
                    "i": "data:image/jpeg;base64," + base64.b64encode(tampon.getvalue()).decode("ascii")})

modele = open(os.path.join(ICI, "choix-modele.html"), encoding="utf-8").read()
assert modele.count("/*DONNEES*/[]") == 1
# json.dumps echappe ce qu'il faut ; « </ » est neutralise pour la balise script.
js = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
page = modele.replace("/*DONNEES*/[]", js)
open(sys.argv[1], "w", encoding="utf-8").write(page)
print(len(donnees), "tableaux,", round(len(page.encode("utf-8")) / 1e6, 2), "Mo")
