# -*- coding: utf-8 -*-
"""Les images web des tenues de situation (visuel/prototype/ropa/<Nom>-<situation>.webp), puis ropa.json.

    python visuel/ropa/web.py            # detoure ce qui manque (fal, BiRefNet, quelques centimes) et fait les webp

Comme Descripcion (visuel/descripcion/detourer.py et web.py) : la personne detouree, fond transparent, recadree sur
elle et ramenee a 900 px de haut, pour se ranger a l'echelle de sa taille a cote des autres. Les originaux et les
detourages restent hors du depot (C:/Users/jacqu/.wortando/ropa/img/). Fichiers DERIVES : les refaire.
"""
import io, os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(RACINE, "video"))
import ropa                                                  # noqa: E402
MODELE = "fal-ai/birefnet/v2"


def main():
    os.makedirs(ropa.SORTIE, exist_ok=True)
    faites = [n for n in ropa.TENUES if os.path.exists(os.path.join(ropa.DOSSIER, n + ".png"))]
    a_detourer = [n for n in faites if not os.path.exists(os.path.join(ropa.DOSSIER, n + "-detoure.png"))]
    if a_detourer:
        import omnihuman as O                                # noqa: E402
        if not os.environ.get("FAL_KEY") and os.path.exists(ropa.PRINCIPAL + "/fal.secret"):
            os.environ["FAL_KEY"] = io.open(ropa.PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
        cle = O.cle()
        for n in a_detourer:
            url = O.deposer(os.path.join(ropa.DOSSIER, n + ".png"), "image/png", cle)[0]
            soum = O._json("https://queue.fal.run/" + MODELE, cle, {"image_url": url, "output_format": "png", "refine_foreground": True})
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
            O.telecharger(res["image"]["url"], os.path.join(ropa.DOSSIER, n + "-detoure.png"))
            print("  detoure", n)
    for n in faites:
        d = Image.open(os.path.join(ropa.DOSSIER, n + "-detoure.png")).convert("RGBA")
        d = d.crop(d.getbbox())
        d = d.resize((round(d.size[0] * 900 / d.size[1]), 900), Image.LANCZOS)
        d.save(os.path.join(ropa.SORTIE, n + ".webp"), "WEBP", quality=82, method=6)
    ropa.ecrire_json()
    total = sum(os.path.getsize(os.path.join(ropa.SORTIE, f)) for f in os.listdir(ropa.SORTIE))
    print("  %d tenues de situation en webp, %.0f ko dans %s" % (len(faites), total / 1024, os.path.relpath(ropa.SORTIE, RACINE)))


if __name__ == "__main__":
    main()
