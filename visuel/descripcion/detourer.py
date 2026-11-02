# -*- coding: utf-8 -*-
"""Detoure les douze personnages de « Descripcion fisica » (fond transparent), pour les ranger cote a cote a
l'echelle de leur taille devant la toise. Chez fal (BiRefNet), quelques centimes pour le tout.

    python visuel/descripcion/detourer.py          # ceux qui manquent -> visuel/descripcion/img/<Nom>-detoure.png

Jacques, 2 nov. 2026 : « lorsque on a des personnages de differentes tailles, un a cote de l'autre ».
Un seuil maison sur le fond gris laissait des pans de studio (ombres, toile qui se courbe).
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
sys.path.insert(0, ICI)
import omnihuman as O                                        # noqa: E402
from personnages import PERSONNAGES, EXISTANTS               # noqa: E402

MODELE = "fal-ai/birefnet/v2"


def source(nom):
    return os.path.join(RACINE, EXISTANTS[nom]) if nom in EXISTANTS else os.path.join(ICI, "img", nom + ".png")


def main():
    cle = O.cle()
    for nom in PERSONNAGES:
        sortie = os.path.join(ICI, "img", nom + "-detoure.png")
        if os.path.exists(sortie):
            continue
        url = O.deposer(source(nom), "image/png", cle)[0]
        soum = O._json("https://queue.fal.run/" + MODELE, cle, {"image_url": url, "output_format": "png", "refine_foreground": True})
        res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        O.telecharger(res["image"]["url"], sortie)
        print("  ->", os.path.relpath(sortie, RACINE))


if __name__ == "__main__":
    main()
