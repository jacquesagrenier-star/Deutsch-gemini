# -*- coding: utf-8 -*-
"""Les vignettes des themes illustres des Soins (visuel/prototype/themes/soins-theme-<cle>.webp, 600 x 510).

    python pflege/outils/themes_soins/vignettes.py

Le format des vignettes des themes (visuel/vignettes_themes.py) : 4:3,4, montre a l'accueil et sur l'ecran de fin
(themes/fin.js). Chaque vignette dit son sujet autrement qu'une rangee de personnes, et se fait d'images DEJA la
(les visages decoupes, les recadrages des scenes) : rien a payer.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
P = os.path.join(RACINE, "visuel", "prototype")
W, H = 600, 510
F = lambda t: ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", t)
FOND = (232, 240, 247)
ENCRE = (28, 36, 48)
AMBRE = (232, 162, 58)


def rond(img, chemin, cx, cy, d):
    im = Image.open(chemin).convert("RGB").resize((d, d), Image.LANCZOS)
    m = Image.new("L", (d, d), 0)
    ImageDraw.Draw(m).ellipse([0, 0, d - 1, d - 1], fill=255)
    bord = Image.new("RGB", (d + 12, d + 12), (255, 255, 255))
    mb = Image.new("L", (d + 12, d + 12), 0)
    ImageDraw.Draw(mb).ellipse([0, 0, d + 11, d + 11], fill=255)
    img.paste(bord, (cx - d // 2 - 6, cy - d // 2 - 6), mb)
    img.paste(im, (cx - d // 2, cy - d // 2), m)


def papier(d, x0, y0, x1, y1, titre, lignes):
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(255, 253, 246), outline=(201, 207, 216), width=2)
    d.text((x0 + 18, y0 + 14), titre, font=F(22), fill=ENCRE)
    y = y0 + 52
    for a, b in lignes:
        d.text((x0 + 18, y), a, font=F(16), fill=(76, 86, 107))
        d.text((x0 + 150, y), b, font=F(18), fill=ENCRE)
        d.line([x0 + 14, y + 30, x1 - 14, y + 30], fill=(201, 207, 216), width=1)
        y += 38


def schmerz():
    img = Image.new("RGB", (W, H), FOND)
    d = ImageDraw.Draw(img)
    x0, y0, c = 30, 330, 46
    for i in range(11):
        t = (127, 200, 160) if i <= 3 else (242, 193, 78) if i <= 6 else (224, 122, 95)
        x = x0 + i * (c + 4)
        d.rounded_rectangle([x, y0, x + c, y0 + 62], radius=8, fill=t)
        d.text((x + c / 2, y0 + 31), str(i), font=F(24), fill=ENCRE, anchor="mm")
        if i == 7:
            d.rounded_rectangle([x - 5, y0 - 5, x + c + 5, y0 + 67], radius=10, outline=ENCRE, width=5)
    rond(img, os.path.join(P, "soins-theme-uebergabe", "visage-brandt.webp"), 300, 170, 230)
    return img


def uebergabe():
    img = Image.new("RGB", (W, H), FOND)
    d = ImageDraw.Draw(img)
    papier(d, 40, 60, 420, 460, "Übergabe · 4B", [("Zimmer", "14"), ("BZ 7:00", "180"), ("VW", "reizlos"), ("NRS", "7 → 3"), ("Offen", "BZ 14:00")])
    rond(img, os.path.join(P, "soins-theme-uebergabe", "visage-lehmann.webp"), 470, 160, 170)
    rond(img, os.path.join(P, "soins-theme-uebergabe", "visage-brandt.webp"), 470, 360, 170)
    return img


def aufnahme():
    img = Image.new("RGB", (W, H), FOND)
    d = ImageDraw.Draw(img)
    papier(d, 40, 50, 400, 470, "Aufnahme", [("Name", "Lehmann"), ("Geb.", "21.08.1952"), ("Allergien", "keine"), ("Hilfsmittel", "Brille"),
                                             ("Angehörige", "Tochter")])
    for i, nom in enumerate(("brille", "hoergeraet")):
        im = Image.open(os.path.join(P, "soins-theme-aufnahme", "objet-%s.webp" % nom)).convert("RGB").resize((200, 150), Image.LANCZOS)
        img.paste(im, (380, 90 + i * 190))
        d.rounded_rectangle([380, 90 + i * 190, 580, 240 + i * 190], radius=12, outline=(255, 255, 255), width=5)
    return img


def telefon():
    img = Image.new("RGB", (W, H), FOND)
    src = Image.open(os.path.expanduser("~/.wortando/pflege/scenes/soins-telefon.png")).convert("RGB")
    sw, sh = src.size
    # Yusuf au combine : le haut du corps, recadre en 600 x 510
    x0, y0, w = int(sw * 0.25), int(sh * 0.42), int(sw * 0.55)
    c = src.crop((x0, y0, x0 + w, y0 + int(w * H / W))).resize((W, H), Image.LANCZOS)
    img.paste(c, (0, 0))
    return img


VIGNETTES = {"schmerz": schmerz, "uebergabe": uebergabe, "aufnahme": aufnahme, "telefon": telefon}

if __name__ == "__main__":
    for cle, f in VIGNETTES.items():
        f().save(os.path.join(P, "themes", "soins-theme-%s.webp" % cle), quality=86, method=6)
        print("themes/soins-theme-%s.webp" % cle)
