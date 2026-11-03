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
    """L'arbre : des visages ronds relies par des branches. Jacques, 3 nov. 2026 : « les images dans les tuiles
    themes [...] sont completes » -- l'arbre ENTIER tient dans le cadre, avec de l'air tout autour : le feuillage,
    le tronc jusqu'a son pied dans l'herbe, et chaque visage entier."""
    c = Image.new("RGB", (W, H), (240, 228, 210))
    d = ImageDraw.Draw(c)
    vert, feuille = (122, 150, 96), (206, 222, 176)
    # le sol, puis le tronc qui s'y plante, puis le feuillage (des ronds, a 18 px au moins des bords)
    d.ellipse((150, 452, 450, 494), fill=(196, 208, 160))
    d.polygon([(278, 330), (322, 330), (334, 472), (266, 472)], fill=(150, 112, 78))
    d.polygon([(266, 472), (240, 482), (300, 476), (360, 482), (334, 472)], fill=(150, 112, 78))
    for (x, y, r) in [(300, 196, 168), (160, 236, 132), (440, 236, 132), (300, 132, 108), (128, 296, 98), (472, 296, 98)]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=feuille)
    noeuds = {"Heinz": (240, 104), "Gisela": (360, 104), "Peter": (170, 210), "Sabine": (430, 210),
              "Anna": (120, 314), "Jan": (300, 318), "Felix": (480, 314)}
    liens = [("Heinz", "Peter"), ("Gisela", "Sabine"), ("Peter", "Anna"), ("Peter", "Jan"), ("Sabine", "Felix")]
    d.line([noeuds["Heinz"], noeuds["Gisela"]], fill=vert, width=9)
    for a, b in liens:
        xa, ya = noeuds[a]
        xb, yb = noeuds[b]
        d.line([(xa, ya), (xa, (ya + yb) // 2), (xb, (ya + yb) // 2), (xb, yb)], fill=vert, width=9, joint="curve")
    for n, (x, y) in noeuds.items():
        r = rond(visage("familia", n), 78, 5)
        c.paste(r, (x - r.size[0] // 2, y - r.size[1] // 2), r)
    return c


def decrire_toise():
    """La toise : les graduations en metres et trois tailles tres differentes."""
    c = Image.new("RGB", (W, H), (230, 238, 246))
    d = ImageDraw.Draw(c)
    # de l'air tout autour du groupe (3 nov. 2026) : le sol remonte, les 2 m descendent sous le haut, et les
    # graduations s'arretent a 16 px des bords au lieu de s'y perdre
    sol = H - 34
    px_m = (sol - 70) / 2.0          # 2 m sur la hauteur, a 70 px du haut
    for cm in range(0, 201, 10):
        y = sol - cm / 100 * px_m
        fort = cm % 50 == 0
        d.line([(16, y), (W - 16, y)], fill=(196, 212, 228) if not fort else (150, 176, 204), width=4 if fort else 2)
        if fort and cm:
            d.text((22, y - 30), "%d,%02d" % (cm // 100, cm % 100) if cm % 100 else "%d m" % (cm // 100), font=F(26), fill=(90, 116, 146))
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
    M = 28                                         # les coins arrondis de la carte ne mordent pas les photos
    pw, ph = (W - 3 * M) // 2, (H - 3 * M) // 2
    c = Image.new("RGB", (W, H), (250, 249, 246))
    d = ImageDraw.Draw(c)
    for k, e in enumerate(["contento", "sorprendido", "enfadado", "triste"]):
        im = Image.open(os.path.join(P, "emociones", "Anna-" + e + ".webp")).convert("RGB")
        w, h = im.size
        # la tete entiere, le menton et les epaules, avec de l'air au-dessus des cheveux (3 nov. 2026 : la coupe
        # serree de la v1078 tranchait mentons et epaules)
        cw = round(w * 0.80)
        ch = round(cw * ph / pw)
        y0 = round(h * 0.04)
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


def chat_quatre_places():
    """« Ou est le chat ? » : le meme chat (Moritz) a quatre places de la meme piece, deux par deux -- sur la table,
    sous le canape, dans le carton, derriere le canape. Chaque case est serree sur le chat et son meuble (la place
    mesuree par visuel/gato/gato.py --mesurer) : sur le ruban, une piece entiere montrerait un chat de deux pixels."""
    M = 14
    pw, ph = (W - 3 * M) // 2, (H - 3 * M) // 2
    c = Image.new("RGB", (W, H), (250, 249, 246))
    d = ImageDraw.Draw(c)
    places = json.load(open(os.path.join(P, "gato", "gato.json"), encoding="utf-8"))["images"]
    for k, id in enumerate(["tisch-auf", "sofa-unter", "karton-in", "sofa-hinter"]):
        im = Image.open(os.path.join(P, "gato", id + ".webp")).convert("RGB")
        w, h = im.size
        cx, cy = places[id]["chat"][0] / 100 * w, places[id]["chat"][1] / 100 * h
        cw = round(w * 0.36); ch = round(cw * ph / pw)
        x0 = min(max(0, round(cx - cw / 2)), w - cw); y0 = min(max(0, round(cy - ch * 0.55)), h - ch)
        im = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((pw, ph), Image.LANCZOS)
        x, y = M + (k % 2) * (pw + M), M + (k // 2) * (ph + M)
        c.paste(im, (x, y))
        d.rectangle((x - 1, y - 1, x + pw, y + ph), outline=(214, 210, 202), width=2)
    return c


def vetements_meteo():
    """Le bulletin meteo : quatre personnes sous quatre pictogrammes dessines (la pluie, la neige, le soleil, les
    alliances du mariage), chacune habillee pour son temps -- Anna au parapluie, Mark en manteau, Ines au chapeau,
    Javier en costume (3 nov. 2026). Tant que leurs tenues de situation ne sont pas faites, leur tenue de tous les jours."""
    c = Image.new("RGB", (W, H), (226, 238, 248))
    d = ImageDraw.Draw(c)
    bleu, ambre = (47, 111, 168), (232, 162, 58)
    d.rectangle((0, 0, W, 112), fill=(205, 225, 243))
    gens = [("Anna", "lluvia"), ("Mark", "frio"), ("Ines", "calor"), ("Javier", "boda")]
    case = W // 4
    for k, (n, sit) in enumerate(gens):
        x0, cx, cy = k * case, k * case + case // 2, 56
        if k:
            d.line((x0, 14, x0, H - 14), fill=(196, 214, 232), width=2)
        if sit == "lluvia":
            for (ex, ey, r) in [(-16, 4, 18), (6, -6, 22), (24, 6, 15)]:
                d.ellipse((cx + ex - r, cy + ey - r, cx + ex + r, cy + ey + r), fill=bleu)
            d.rectangle((cx - 30, cy + 4, cx + 36, cy + 20), fill=bleu)
            for dx in (-18, 2, 22):
                d.line((cx + dx, cy + 28, cx + dx - 6, cy + 42), fill=bleu, width=5)
        elif sit == "frio":
            import math
            for a in range(3):
                t = math.pi / 3 * a
                dx, dy = 34 * math.cos(t), 34 * math.sin(t)
                d.line((cx - dx, cy - dy, cx + dx, cy + dy), fill=bleu, width=6)
        elif sit == "calor":
            d.ellipse((cx - 20, cy - 20, cx + 20, cy + 20), fill=ambre)
            import math
            for a in range(8):
                t = math.pi / 4 * a
                d.line((cx + 27 * math.cos(t), cy + 27 * math.sin(t), cx + 38 * math.cos(t), cy + 38 * math.sin(t)), fill=ambre, width=6)
        else:
            for ex in (-12, 12):
                d.ellipse((cx + ex - 22, cy - 18, cx + ex + 22, cy + 26), outline=ambre, width=7)
        chemin = os.path.join(P, "ropa", n + "-" + sit + ".webp")
        p = Image.open(chemin if os.path.exists(chemin) else os.path.join(P, "descripcion", n + ".webp")).convert("RGBA")
        p = p.crop(p.getbbox())
        h = H - 130
        p = p.resize((round(p.size[0] * h / p.size[1]), h), Image.LANCZOS)
        if p.size[0] > case - 8:
            p = p.resize((case - 8, round(p.size[1] * (case - 8) / p.size[0])), Image.LANCZOS)
        c.paste(p, (cx - p.size[0] // 2, H - 8 - p.size[1]), p)
    return c


VIGNETTES = {"familia": famille_arbre, "descripcion": decrire_toise, "emociones": emotions_photomaton, "contrarios": contraires_verres, "gato": chat_quatre_places, "ropa": vetements_meteo}

if __name__ == "__main__":
    os.makedirs(SORTIE, exist_ok=True)
    # python visuel/vignettes_themes.py gato : une seule vignette (les autres restent telles quelles)
    for nom, f in VIGNETTES.items():
        if sys.argv[1:] and nom not in sys.argv[1:]:
            continue
        f().save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=84, method=6)
        print("  ->", nom + ".webp")
