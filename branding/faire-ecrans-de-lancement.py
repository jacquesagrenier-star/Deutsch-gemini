# -*- coding: utf-8 -*-
"""Fabrique les ecrans de lancement iOS (apple-touch-startup-image) et
l'icone apple-touch-icon de Wortando.

Pourquoi ces images existent : quand iOS lance une app web installee sur
l'ecran d'accueil, il affiche l'image de lancement correspondant EXACTEMENT a
la taille de l'ecran. S'il n'en trouve aucune, il affiche sa photo de la
session precedente -- l'accueil de l'app -- ce qui produisait l'eclair qu'on
voyait avant la video d'ouverture.

Chaque image doit donc reproduire au pixel pres ce que le navigateur peint a
la premiere milliseconde.

TOUT EST LU DANS index.html, RIEN N'EST RECOPIE ICI (v443). La version
precedente gardait sa propre copie de la premiere image (ouverture-image0.png)
et sa propre couleur de fond en dur. Les deux ont derive sans que rien ne le
signale : la video a ete remplacee en v372-v373 (le W de verre devenu W
d'encre) sans que ces images soient refaites, et le fond y valait #F2EEE2
quand la feuille de style disait #EFEEE1. Resultat sur l'iPhone : iOS montrait
l'ancien logo plat, puis la page peignait le nouveau logo de verre sur un
creme legerement different. Deux eclairs, a chaque lancement.

Ce script extrait donc lui-meme :
  - la video, depuis le base64 embarque dans index.html, et sa premiere image ;
  - la couleur de fond, depuis la regle #splashOuverture ;
  - la taille du logo, depuis width:min(..vw, ..vh, ..px) ;
  - le fondu des bords, depuis le mask-image radial.
Si l'une de ces regles change de forme, le script s'arrete au lieu de produire
une image fausse en silence.

Relancer apres tout changement de la video d'ouverture ou de sa regle CSS :
    python branding/faire-ecrans-de-lancement.py
"""
import io
import base64
import pathlib
import re
import subprocess
import tempfile

import numpy as np
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parent.parent
INDEX = RACINE / "index.html"
SORTIE = RACINE / "branding" / "lancement"
# Conservee pour l'oeil : c'est ce que le script vient de composer, pas sa
# source. La source est index.html.
IMAGE0 = RACINE / "branding" / "ouverture-image0.png"

# (largeur CSS, hauteur CSS, densite) -- portrait uniquement : l'app se tient
# a la verticale, et iOS ignore simplement une taille qu'il ne reconnait pas
# (auquel cas on retombe sur le comportement d'avant, jamais pire).
APPAREILS = [
    (320, 568, 2),   # SE 1re gen, 5/5s
    (375, 667, 2),   # 6/7/8, SE 2e et 3e gen
    (414, 736, 3),   # 6+/7+/8+
    (375, 812, 3),   # X, XS, 11 Pro, 12 mini, 13 mini
    (414, 896, 2),   # XR, 11
    (414, 896, 3),   # XS Max, 11 Pro Max
    (390, 844, 3),   # 12, 12 Pro, 13, 13 Pro, 14
    (428, 926, 3),   # 12 Pro Max, 13 Pro Max, 14 Plus
    (393, 852, 3),   # 14 Pro, 15, 15 Pro, 16
    (430, 932, 3),   # 14 Pro Max, 15 Plus, 15 Pro Max, 16 Plus
    (402, 874, 3),   # 16 Pro
    (440, 956, 3),   # 16 Pro Max
]


def lire_index():
    return io.open(INDEX, encoding="utf-8", newline="").read()


def premiere_image(html):
    """La premiere image de la video embarquee, decodee par ffmpeg."""
    m = re.search(r'src="data:video/mp4;base64,([A-Za-z0-9+/=]+)"', html)
    assert m, "video d'ouverture introuvable dans index.html"
    octets = base64.b64decode(m.group(1))
    with tempfile.TemporaryDirectory() as tmp:
        mp4 = pathlib.Path(tmp) / "ouverture.mp4"
        png = pathlib.Path(tmp) / "image0.png"
        mp4.write_bytes(octets)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4),
                        "-frames:v", "1", str(png)], check=True)
        img = Image.open(png).convert("RGB")
        img.load()
    print("  video embarquee : %.1f ko, premiere image %dx%d"
          % (len(octets) / 1024, img.width, img.height))
    return img


def couleur_de_fond(html):
    """La couleur de #splashOuverture, lue dans la feuille de style."""
    bloc = re.search(r"#splashOuverture\{(.*?)\}", html, re.S)
    assert bloc, "regle #splashOuverture introuvable"
    m = re.search(r"background:#([0-9A-Fa-f]{6})", bloc.group(1))
    assert m, "couleur de fond de #splashOuverture introuvable"
    h = m.group(1)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)), "#" + h.upper()


def regle_de_taille(html):
    """width:min(Xvw, Yvh, Zpx) -- la largeur du logo a l'ecran."""
    bloc = re.search(r"#splashOuverture video\{(.*?)\}", html, re.S)
    assert bloc, "regle #splashOuverture video introuvable"
    m = re.search(r"width:min\(\s*([\d.]+)vw\s*,\s*([\d.]+)vh\s*,\s*([\d.]+)px\s*\)",
                  bloc.group(1))
    assert m, "width:min(..vw, ..vh, ..px) introuvable ou de forme inattendue"
    return float(m.group(1)) / 100, float(m.group(2)) / 100, float(m.group(3))


def bornes_du_fondu(html):
    """Le mask radial : opaque jusqu'a A % du rayon, transparent a B %.

    Le CSS dit `radial-gradient(ellipse closest-side at 50% 50%,
    #000 0, #000 50%, rgba(0,0,0,0) 100%)`. `closest-side` veut dire que les
    rayons de l'ellipse valent la demi-largeur et la demi-hauteur de la video.
    """
    bloc = re.search(r"#splashOuverture video\{(.*?)\}", html, re.S)
    m = re.search(r"mask-image:\s*radial-gradient\(ellipse closest-side at 50% 50%,"
                  r"\s*#000 0,\s*#000 ([\d.]+)%,\s*rgba\(0,0,0,0\) ([\d.]+)%\)",
                  bloc.group(1))
    assert m, "mask-image radial de forme inattendue : le fondu n'est plus reproductible"
    return float(m.group(1)) / 100, float(m.group(2)) / 100


def appliquer_le_fondu(img, opaque, bord):
    """Le meme fondu que le CSS, en alpha."""
    l, h = img.size
    ys, xs = np.mgrid[0:h, 0:l]
    # Rayon normalise de l'ellipse : 0 au centre, 1 au milieu d'un bord,
    # racine de 2 dans les coins. C'est l'echelle du degrade CSS, ou 100 %
    # tombe sur le bord le plus proche (`closest-side`) -- pas sur le coin.
    dx = (xs - (l - 1) / 2) / ((l - 1) / 2)
    dy = (ys - (h - 1) / 2) / ((h - 1) / 2)
    r = np.sqrt(dx * dx + dy * dy)
    a = np.clip((bord - r) / (bord - opaque), 0.0, 1.0)
    sortie = img.convert("RGBA")
    sortie.putalpha(Image.fromarray((a * 255).round().astype(np.uint8), "L"))
    return sortie


def largeur_css_du_logo(l_css, h_css, part_l, part_h, plafond):
    return min(part_l * l_css, part_h * h_css, plafond)


# Part de la largeur de l'icone qu'occupe le monogramme. Dans le fichier
# d'origine il n'en prenait que 55 %, ce qui le rendait minuscule une fois
# pose sur l'ecran d'accueil parmi les autres apps. iOS decoupe ensuite
# l'icone en carre arrondi : a 76 %, le logo respire encore sans jamais
# s'approcher des coins ronges par ce masque.
PART_DU_LOGO = 0.76


def faire_icone():
    """Recadre le monogramme au plus pres, puis le recentre plus gros.

    Sans icone declaree, iOS fabrique la sienne a partir d'une capture de la
    page -- une vignette illisible. Le fichier d'origine
    (wortando-app-icon.png) n'est PAS modifie : il sert encore de favicon et
    d'icone de notification, ou le cadrage large convient.
    """
    src = Image.open(RACINE / "branding" / "wortando-app-icon.png").convert("RGB")
    papier = src.getpixel((5, 5))
    px = src.load()
    x0, y0, x1, y1 = src.width, src.height, 0, 0
    for y in range(src.height):
        for x in range(src.width):
            r, g, b = px[x, y]
            if abs(r-papier[0]) + abs(g-papier[1]) + abs(b-papier[2]) > 40:
                x0, x1 = min(x0, x), max(x1, x)
                y0, y1 = min(y0, y), max(y1, y)
    logo = src.crop((x0, y0, x1 + 1, y1 + 1))

    cote = 1024
    ll = round(cote * PART_DU_LOGO)
    lh = round(ll * logo.height / logo.width)
    toile = Image.new("RGB", (cote, cote), papier)
    toile.paste(logo.resize((ll, lh), Image.LANCZOS),
                ((cote - ll) // 2, (cote - lh) // 2))
    toile.save(RACINE / "branding" / "wortando-icone-ecran-accueil.png", optimize=True)
    toile.resize((180, 180), Image.LANCZOS).save(
        RACINE / "branding" / "wortando-apple-touch-icon.png", optimize=True)
    print("  logo recadre : %dx%d -> %d%% de l'icone (etait %d%%)" % (
        logo.width, logo.height, round(100 * PART_DU_LOGO),
        round(100 * logo.width / src.width)))


def main():
    html = lire_index()
    fond, fond_hex = couleur_de_fond(html)
    part_l, part_h, plafond = regle_de_taille(html)
    opaque, bord = bornes_du_fondu(html)
    logo = appliquer_le_fondu(premiere_image(html), opaque, bord)

    print("  lu dans index.html : fond %s | width:min(%d%%vw, %d%%vh, %dpx) | "
          "fondu %d%% -> %d%%"
          % (fond_hex, round(part_l * 100), round(part_h * 100), plafond,
             round(opaque * 100), round(bord * 100)))

    IMAGE0.write_bytes(b"")
    apercu = Image.new("RGB", logo.size, fond)
    apercu.paste(logo, (0, 0), logo)
    apercu.save(IMAGE0, optimize=True)

    SORTIE.mkdir(parents=True, exist_ok=True)
    for ancien in SORTIE.glob("*.png"):
        ancien.unlink()

    rapport = logo.height / logo.width
    lignes = []
    for l_css, h_css, densite in APPAREILS:
        lp, hp = l_css * densite, h_css * densite
        toile = Image.new("RGB", (lp, hp), fond)
        ll = round(largeur_css_du_logo(l_css, h_css, part_l, part_h, plafond) * densite)
        lh = round(ll * rapport)
        vignette = logo.resize((ll, lh), Image.LANCZOS)
        toile.paste(vignette, ((lp - ll) // 2, (hp - lh) // 2), vignette)
        # Palette : un aplat creme, un logo, et le degrade du fondu entre les
        # deux. 128 couleurs -- 64 laissaient des cercles dans le fondu.
        nom = "lancement-%dx%d@%dx.png" % (l_css, h_css, densite)
        toile.quantize(colors=128, method=Image.MEDIANCUT).save(
            SORTIE / nom, optimize=True)
        lignes.append((nom, l_css, h_css, densite,
                       (SORTIE / nom).stat().st_size))

    faire_icone()

    total = sum(l[4] for l in lignes)
    for nom, l, h, d, o in lignes:
        print("  %-26s %5dx%-5d @%dx  %6.1f ko" % (nom, l*d, h*d, d, o/1024))
    print("  %d ecrans, %.0f ko au total" % (len(lignes), total/1024))
    print("  apple-touch-icon 180x180 : %.1f ko" % (
        (RACINE/"branding"/"wortando-apple-touch-icon.png").stat().st_size/1024))


if __name__ == "__main__":
    main()
