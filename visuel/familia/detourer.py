# -*- coding: utf-8 -*-
"""Detoure la famille d'Anna (fond transparent), pour les ranger a l'echelle et cadrer les visages de l'arbre.
Chez fal (BiRefNet), quelques centimes pour le tout. Meme geste que visuel/descripcion/detourer.py.

    python visuel/familia/detourer.py          # celles qui manquent -> visuel/familia/img/<Nom>-detoure.png
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
sys.path.insert(0, ICI)
import omnihuman as O                                        # noqa: E402
from familia import FAMILLE                                  # noqa: E402

MODELE = "fal-ai/birefnet/v2"


def source(nom):
    return os.path.join(ICI, "img", ("Anna-quotidien" if nom == "Anna" else nom) + ".png")


def main():
    cle = O.cle()
    for nom in FAMILLE:
        sortie = os.path.join(ICI, "img", nom + "-detoure.png")
        if os.path.exists(sortie) or not os.path.exists(source(nom)):
            continue
        url = O.deposer(source(nom), "image/png", cle)[0]
        soum = O._json("https://queue.fal.run/" + MODELE, cle, {"image_url": url, "output_format": "png", "refine_foreground": True})
        res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        O.telecharger(res["image"]["url"], sortie)
        print("  ->", os.path.relpath(sortie, RACINE), flush=True)


if __name__ == "__main__":
    main()
