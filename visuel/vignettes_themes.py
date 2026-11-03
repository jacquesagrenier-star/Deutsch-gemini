# -*- coding: utf-8 -*-
"""Les vignettes des themes illustres, pour le ruban de l'accueil (visuel/prototype/themes/<theme>.webp, 3:4).

    python visuel/vignettes_themes.py

Jacques, 3 nov. 2026 : deux groupes de personnes cote a cote se ressemblaient trop (« On dirait deux groupes de
familles »). Chaque vignette dit son sujet AUTREMENT qu'une rangee de personnes : la famille, un arbre de visages
ronds relies par des branches ; Decrire une personne, la toise et trois tailles tres differentes (Carmen, Mark,
Tomas) sur des graduations en metres. Dessins du chef d'orchestre (couvertures.py, famille_arbre et
decrire_toise), repris ici. Faites des webp DEJA PUBLIES (visuel/prototype/<theme>/) : sans les originaux et sans
rien payer. Un theme futur : une fonction de plus dans VIGNETTES, qui dise le sujet autrement.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ICI, "prototype")
SORTIE = os.path.join(P, "themes")
W, H = 600, 800                       # 3:4, en double pour la nettete
F = lambda t: ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", t)


def rond(img, d, bord=6, couleur=(255, 255, 255)):
    w, h = img.size
    c = min(w, h)
    img = img.crop(((w - c) // 2, 0, (w - c) // 2 + c, c)).resize((d, d), Image.LANCZOS)
    m = Image.new("L", (d, d), 0)
    ImageDraw.Draw(m).ellipse((0, 0, d - 1, d - 1), fill=255)
    o = Image.new("RGBA", (d + 2 * bord, d + 2 * bord), (0, 0, 0, 0))
    ImageDraw.Draw(o).ellipse((0, 0, d + 2 * bord - 1, d + 2 * bord - 1), fill=couleur + (255,))
    o.paste(img, (bord, bord), m)
    return o


def visage(dossier, n):
    return Image.open(os.path.join(P, dossier, n + "-visage.webp")).convert("RGB")


def pied(dossier, n):
    i = Image.open(os.path.join(P, dossier, n + ".webp")).convert("RGBA")
    return i.crop(i.getbbox())


def famille_arbre():
    """L'arbre : des visages ronds relies par des branches."""
    c = Image.new("RGB", (W, H), (240, 228, 210))
    d = ImageDraw.Draw(c)
    vert = (122, 150, 96)
    d.rounded_rectangle((W // 2 - 26, 470, W // 2 + 26, 800), 20, fill=(150, 112, 78))
    noeuds = {"Heinz": (210, 150), "Gisela": (390, 150), "Peter": (150, 360), "Sabine": (450, 360),
              "Anna": (110, 580), "Jan": (300, 600), "Felix": (490, 580)}
    liens = [("Heinz", "Peter"), ("Gisela", "Sabine"), ("Peter", "Anna"), ("Peter", "Jan"), ("Sabine", "Felix")]
    for (x, y, r) in [(300, 330, 290), (150, 260, 170), (450, 260, 170), (300, 120, 170)]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=(206, 222, 176))
    d.line([noeuds["Heinz"], noeuds["Gisela"]], fill=vert, width=10)
    for a, b in liens:
        xa, ya = noeuds[a]
        xb, yb = noeuds[b]
        d.line([(xa, ya), (xa, (ya + yb) // 2), (xb, (ya + yb) // 2), (xb, yb)], fill=vert, width=10, joint="curve")
    for n, (x, y) in noeuds.items():
        r = rond(visage("familia", n), 118 if n in ("Heinz", "Gisela") else 112, 7)
        c.paste(r, (x - r.size[0] // 2, y - r.size[1] // 2), r)
    return c


def decrire_toise():
    """La toise : les graduations en metres et trois tailles tres differentes."""
    c = Image.new("RGB", (W, H), (230, 238, 246))
    d = ImageDraw.Draw(c)
    sol = 770
    px_m = (sol - 60) / 2.0          # 2 m sur la hauteur
    for cm in range(0, 201, 10):
        y = sol - cm / 100 * px_m
        fort = cm % 50 == 0
        d.line([(0, y), (W, y)], fill=(196, 212, 228) if not fort else (150, 176, 204), width=4 if fort else 2)
        if fort and cm:
            d.text((14, y - 34), "%d,%02d" % (cm // 100, cm % 100) if cm % 100 else "%d m" % (cm // 100), font=F(30), fill=(90, 116, 146))
    tailles = json.load(open(os.path.join(P, "descripcion", "personnages.json"), encoding="utf-8"))
    gens = [(n, tailles[n]["metres"]) for n in ("Carmen", "Mark", "Tomas")]
    ims = [pied("descripcion", n) for n, _ in gens]
    ims = [i.resize((int(i.size[0] * m * px_m / i.size[1]), int(m * px_m)), Image.LANCZOS) for i, (_, m) in zip(ims, gens)]
    x = 92
    for i in ims:
        c.paste(i, (int(x), sol - i.size[1]), i)
        x += i.size[0] * 0.74
    return c


VIGNETTES = {"familia": famille_arbre, "descripcion": decrire_toise}

if __name__ == "__main__":
    os.makedirs(SORTIE, exist_ok=True)
    for nom, f in VIGNETTES.items():
        f().resize((450, 600), Image.LANCZOS).save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=84, method=6)
        print("  ->", nom + ".webp")
