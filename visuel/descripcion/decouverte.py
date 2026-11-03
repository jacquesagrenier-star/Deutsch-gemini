# -*- coding: utf-8 -*-
"""Les images de la DECOUVERTE de « Decrire une personne » (3 nov. 2026) : la tete et les epaules de quelques
personnes, pour montrer une couleur, une longueur ou une forme de cheveux, une barbe, des lunettes.

    python visuel/descripcion/decouverte.py       -> visuel/prototype/descripcion/tete-<Nom>.webp

Jacques : « on pourrait avoir toutes les couleurs des yeux qu'on peut cliquer sur chaque couleur pour voir la
couleur. Pour l'entendre, et le voir. La meme chose probablement pour les cheveux ». Rien de neuf a fabriquer : les
tetes viennent des personnes deja detourees (visuel/prototype/descripcion/<Nom>.webp), et les cheveux gris de
Peter, de la famille d'Anna (visuel/prototype/familia/). Le recadrage descend jusqu'aux epaules, sans quoi des
cheveux longs ne se verraient pas longs.
"""
import os, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.join(os.path.dirname(ICI), "prototype")
SORTIE = os.path.join(PROTO, "descripcion")
# nom : dossier ou se trouve la personne detouree
TETES = {"Elena": "descripcion", "Marta": "descripcion", "Anna": "descripcion", "Ines": "descripcion", "Rosa": "descripcion",
         "Javier": "descripcion", "Carmen": "descripcion", "Diego": "descripcion", "Pablo": "descripcion", "Peter": "familia"}
FOND = (236, 241, 246)


def tete(nom, dossier):
    d = Image.open(os.path.join(PROTO, dossier, nom + ".webp")).convert("RGBA")
    x0, y0, x1, y1 = d.getbbox()
    h = y1 - y0
    haut = int(h * 0.36)                          # du sommet du crane aux epaules, cheveux longs compris
    a = d.getchannel("A").crop((x0, y0, x1, y0 + int(h * 0.13))).point(lambda v: 255 if v > 128 else 0)
    bx0, _, bx1, _ = a.getbbox()
    cx = x0 + (bx0 + bx1) // 2                    # centre sur la tete, pas sur le corps
    large = int(haut * 0.8)
    boite = (cx - large // 2, y0 - int(h * 0.015), cx + large // 2, y0 + haut)
    f = Image.new("RGBA", (boite[2] - boite[0], boite[3] - boite[1]), FOND + (255,))
    f.alpha_composite(d.crop(boite))
    f = f.convert("RGB").resize((300, round(300 * f.size[1] / f.size[0])), Image.LANCZOS)
    f.save(os.path.join(SORTIE, "tete-" + nom + ".webp"), "WEBP", quality=84, method=6)
    print("  -> tete-%s.webp" % nom)


if __name__ == "__main__":
    for n, dos in TETES.items():
        tete(n, dos)
