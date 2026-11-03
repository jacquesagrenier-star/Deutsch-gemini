# -*- coding: utf-8 -*-
"""Les vignettes des themes illustres, pour le ruban de l'accueil (visuel/prototype/themes/<theme>.webp, 3:4).

    python visuel/vignettes_themes.py

Jacques, 3 nov. 2026 : deux groupes de personnes cote a cote se ressemblaient trop (« On dirait deux groupes de
familles »). Chaque vignette dit son sujet AUTREMENT qu'une rangee de personnes : la famille, un arbre de visages
ronds relies par des branches ; Decrire une personne, la toise et trois tailles tres differentes (Carmen, Mark,
Tomas) sur des graduations en metres. Dessins du chef d'orchestre (couvertures.py, famille_arbre et
decrire_toise), repris ici. Faites des webp DEJA PUBLIES (visuel/prototype/<theme>/) : sans les originaux et sans
rien payer. Les emotions et le caractere : une planche de photomaton d'Anna, quatre visages (3 nov.).
Les contraires : le verre plein et le verre vide, coupes par le milieu (3 nov.).
Un theme futur : une fonction de plus dans VIGNETTES, qui dise le sujet autrement.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ICI, "prototype")
SORTIE = os.path.join(P, "themes")
# 4:3,4, le format ou l'accueil montre les vignettes des scenes (Jacques, 3 nov. 2026 : « la meme hauteur que ce
# qu'on a pour les scenes. Pour que ca soit harmonieux, donc trois a la fois ») : chaque dessin y est compose, rien
# n'est coupe par le recadrage de l'accueil.
W, H = 600, 510
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
    d.rounded_rectangle((W // 2 - 24, 330, W // 2 + 24, H), 18, fill=(150, 112, 78))
    noeuds = {"Heinz": (225, 88), "Gisela": (375, 88), "Peter": (140, 245), "Sabine": (460, 245),
              "Anna": (80, 410), "Jan": (300, 420), "Felix": (520, 410)}
    liens = [("Heinz", "Peter"), ("Gisela", "Sabine"), ("Peter", "Anna"), ("Peter", "Jan"), ("Sabine", "Felix")]
    for (x, y, r) in [(300, 230, 250), (130, 200, 150), (470, 200, 150), (300, 90, 140), (90, 370, 110), (510, 370, 110)]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=(206, 222, 176))
    d.line([noeuds["Heinz"], noeuds["Gisela"]], fill=vert, width=10)
    for a, b in liens:
        xa, ya = noeuds[a]
        xb, yb = noeuds[b]
        d.line([(xa, ya), (xa, (ya + yb) // 2), (xb, (ya + yb) // 2), (xb, yb)], fill=vert, width=10, joint="curve")
    for n, (x, y) in noeuds.items():
        r = rond(visage("familia", n), 102 if n in ("Heinz", "Gisela") else 96, 6)
        c.paste(r, (x - r.size[0] // 2, y - r.size[1] // 2), r)
    return c


def decrire_toise():
    """La toise : les graduations en metres et trois tailles tres differentes."""
    c = Image.new("RGB", (W, H), (230, 238, 246))
    d = ImageDraw.Draw(c)
    sol = H - 18
    px_m = (sol - 26) / 2.0          # 2 m sur la hauteur
    for cm in range(0, 201, 10):
        y = sol - cm / 100 * px_m
        fort = cm % 50 == 0
        d.line([(0, y), (W, y)], fill=(196, 212, 228) if not fort else (150, 176, 204), width=4 if fort else 2)
        if fort and cm:
            d.text((14, y - 30), "%d,%02d" % (cm // 100, cm % 100) if cm % 100 else "%d m" % (cm // 100), font=F(26), fill=(90, 116, 146))
    tailles = json.load(open(os.path.join(P, "descripcion", "personnages.json"), encoding="utf-8"))
    gens = [(n, tailles[n]["metres"]) for n in ("Carmen", "Mark", "Tomas")]
    ims = [pied("descripcion", n) for n, _ in gens]
    ims = [i.resize((int(i.size[0] * m * px_m / i.size[1]), int(m * px_m)), Image.LANCZOS) for i, (_, m) in zip(ims, gens)]
    largeur = sum(i.size[0] * 0.8 for i in ims[:-1]) + ims[-1].size[0]
    x = 92 + (W - 92 - largeur) / 2
    for i in ims:
        c.paste(i, (int(x), sol - i.size[1]), i)
        x += i.size[0] * 0.8
    return c


def emotions_photomaton():
    """La planche de photomaton : Anna quatre fois, contente, surprise, fachee, triste. Une seule personne et quatre
    visages, deux par deux, comme les photos d'identite d'une cabine ; serre sur la tete (le ruban montre 66 px)."""
    M = 14
    pw, ph = (W - 3 * M) // 2, (H - 3 * M) // 2
    c = Image.new("RGB", (W, H), (250, 249, 246))
    d = ImageDraw.Draw(c)
    for k, e in enumerate(["contento", "sorprendido", "enfadado", "triste"]):
        im = Image.open(os.path.join(P, "emociones", "Anna-" + e + ".webp")).convert("RGB")
        w, h = im.size
        cw = round(w * 0.58)                       # serre sur la tete et le haut des epaules (session des emotions)
        ch = round(cw * ph / pw)
        y0 = round(h * 0.07)
        im = im.crop(((w - cw) // 2, y0, (w + cw) // 2, y0 + ch)).resize((pw, ph), Image.LANCZOS)
        x, y = M + (k % 2) * (pw + M), M + (k // 2) * (ph + M)
        c.paste(im, (x, y))
        d.rectangle((x - 1, y - 1, x + pw, y + ph), outline=(214, 210, 202), width=2)
    return c


def contraires_verres():
    """Les contraires : le verre plein et le verre vide, coupes par le milieu, un rond ambre « ↔ » sur la ligne.
    Le meme verre, la meme table : seul le contraire change (le ruban montre 66 px, il faut le voir d'un coup)."""
    c = Image.new("RGB", (W, H), (250, 249, 246))
    demi = W // 2
    for k, nom in enumerate(["vaso-lleno", "vaso-vacio"]):
        im = Image.open(os.path.join(P, "contrarios", nom + ".webp")).convert("RGB")
        w, h = im.size
        ch = round(h * 0.74)                        # serre sur le verre (au tiers gauche de l'image, sur la table)
        cw = round(ch * demi / H)
        cx, y0 = round(w * 0.33), round(h * 0.2)
        im = im.crop((cx - cw // 2, y0, cx - cw // 2 + cw, y0 + ch)).resize((demi, H), Image.LANCZOS)
        c.paste(im, (k * demi, 0))
    d = ImageDraw.Draw(c)
    d.line([(demi, 0), (demi, H)], fill=(255, 255, 255), width=6)
    r = 40
    d.ellipse((demi - r, H // 2 - r, demi + r, H // 2 + r), fill=(232, 162, 58), outline=(255, 255, 255), width=5)
    d.text((demi, H // 2 + 2), "↔", font=ImageFont.truetype("C:/Windows/Fonts/seguisym.ttf", 60), fill=(28, 36, 48), anchor="mm")
    return c


VIGNETTES = {"familia": famille_arbre, "descripcion": decrire_toise, "emociones": emotions_photomaton, "contrarios": contraires_verres}

if __name__ == "__main__":
    os.makedirs(SORTIE, exist_ok=True)
    for nom, f in VIGNETTES.items():
        f().save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=84, method=6)
        print("  ->", nom + ".webp")
