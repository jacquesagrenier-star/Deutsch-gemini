# -*- coding: utf-8 -*-
"""La planche des figures du voyage, telles que l'app les dessine (boite de 375 x 372, ciel du soir), pour les
montrer avant de les mettre en service.

    python etoiles/outils/planche.py [sortie.png] [--toutes]

Par defaut les 42 nouvelles figures (voyage.py) ; --toutes ajoute les 15 premieres. Sous chaque figure : son rang dans
le voyage, son nom en francais, son nombre d'etoiles et les seances qui l'allument (une etoile par seance terminee).
Pres de chaque etoile, son rang d'allumage dans la figure et son nom court (la lettre grecque pour une etoile sans nom
propre, comme dans « Ton ciel »)."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
W, H, BAS = 375, 372, 64
COLS = 6
FOND, TRAIT, TEXTE, PALE = (16, 24, 40), (255, 233, 191), (238, 228, 210), (150, 170, 200)


def police(t, gras=False):
    for nom in (("segoeuib.ttf", "arialbd.ttf") if gras else ("segoeui.ttf", "arial.ttf")):
        try:
            return ImageFont.truetype(nom, t)
        except OSError:
            pass
    return ImageFont.load_default()


def nom_court(e):
    n = (e.get("noms") or {}).get("fr") or e["nom"]
    return n.split()[0]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sortie = args[0] if args else os.path.join(RACINE, "planche-voyage.png")
    d = json.load(open(os.path.join(RACINE, "ciel.json"), encoding="utf-8"))
    ordre = d["ordre"]
    debut = 0 if "--toutes" in sys.argv else 15
    cles = ordre[debut:]
    cumul, avant = {}, 0
    for k in ordre:
        n = len(d["constellations"][k]["etoiles"])
        cumul[k] = (avant + 1, avant + n)
        avant += n
    lignes = -(-len(cles) // COLS)
    img = Image.new("RGB", (COLS * W, lignes * (H + BAS) + 70), (10, 15, 28))
    dr = ImageDraw.Draw(img)
    f_titre, f_sous, f_nom, f_num = police(22, True), police(15), police(13), police(11, True)
    dr.text((16, 18), "Le ciel jusqu'au C1 : %d nouvelles constellations, %d étoiles (séances %d à %d du voyage)" % (
        len(cles), sum(len(d["constellations"][k]["etoiles"]) for k in cles), cumul[cles[0]][0], cumul[cles[-1]][1]),
        fill=TEXTE, font=f_titre)
    for i, k in enumerate(cles):
        c = d["constellations"][k]
        ox, oy = (i % COLS) * W, 70 + (i // COLS) * (H + BAS)
        dr.rectangle([ox + 3, oy + 3, ox + W - 3, oy + H + BAS - 3], fill=FOND)
        E = c["etoiles"]
        for a, b in c["traits"]:
            dr.line([ox + E[a]["x"], oy + E[a]["y"], ox + E[b]["x"], oy + E[b]["y"]], fill=TRAIT, width=2)
        for j, e in enumerate(E):
            x, y, r = ox + e["x"], oy + e["y"], e["r"] * 1.15
            col = tuple(int(e["couleur"][p:p + 2], 16) for p in (1, 3, 5))
            dr.ellipse([x - r * 2.2, y - r * 2.2, x + r * 2.2, y + r * 2.2], fill=tuple(int(v * .25 + f * .75) for v, f in zip(col, FOND)))
            dr.ellipse([x - r, y - r, x + r, y + r], fill=col)
            dr.text((x + r + 3, y - 15), str(j + 1), fill=(246, 206, 132), font=f_num)
            dr.text((x + r + 3, y - 2), nom_court(e), fill=PALE, font=f_nom)
        a, b = cumul[k]
        dr.text((ox + 14, oy + H - 4), "%d. %s" % (ordre.index(k) + 1, c["noms"]["fr"]), fill=TEXTE, font=police(18, True))
        dr.text((ox + 14, oy + H + 20), "%d étoiles · séances %d à %d" % (len(E), a, b), fill=PALE, font=f_sous)
    img.save(sortie)
    print("ecrit", sortie, img.size)


if __name__ == "__main__":
    main()
