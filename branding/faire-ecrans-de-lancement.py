# -*- coding: utf-8 -*-
"""Fabrique les ecrans de lancement iOS (apple-touch-startup-image) et
l'icone apple-touch-icon de Wortando.

Pourquoi ces images existent : quand iOS lance une app web installee sur
l'ecran d'accueil, il affiche l'image de lancement correspondant EXACTEMENT a
la taille de l'ecran. S'il n'en trouve aucune, il affiche sa photo de la
session precedente -- l'accueil de l'app -- ce qui produisait l'eclair qu'on
voyait avant la video d'ouverture.

Chaque image reproduit donc au pixel pres ce que l'app affiche a la premiere
milliseconde : fond creme #F2EEE2, et la PREMIERE IMAGE de la video
d'ouverture, a la meme taille et au meme endroit que la regle CSS
#splashOuverture video { width: min(76vw, 58vh, 420px) }. La transition entre
l'ecran de lancement du systeme et la video devient invisible.

Source de l'image : branding/ouverture-image0.png -- la premiere image de la
video embarquee dans index.html, extraite une fois pour toutes et conservee
ici, puisque la video n'existe qu'en base64 a l'interieur du HTML.

Relancer apres tout changement de la video d'ouverture ou de sa regle CSS :
    python branding/faire-ecrans-de-lancement.py
"""
import pathlib
from PIL import Image

CREME = (242, 238, 226)          # #F2EEE2, fond de #splashOuverture
RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "branding" / "ouverture-image0.png"
SORTIE = RACINE / "branding" / "lancement"

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

def largeur_css_du_logo(l_css, h_css):
    """La regle CSS : width: min(76vw, 58vh, 420px)."""
    return min(0.76 * l_css, 0.58 * h_css, 420.0)

def main():
    logo = Image.open(SOURCE).convert("RGB")
    SORTIE.mkdir(parents=True, exist_ok=True)
    for ancien in SORTIE.glob("*.png"):
        ancien.unlink()

    rapport = logo.height / logo.width
    lignes = []
    for l_css, h_css, densite in APPAREILS:
        lp, hp = l_css * densite, h_css * densite
        toile = Image.new("RGB", (lp, hp), CREME)
        ll = round(largeur_css_du_logo(l_css, h_css) * densite)
        lh = round(ll * rapport)
        toile.paste(logo.resize((ll, lh), Image.LANCZOS),
                    ((lp - ll) // 2, (hp - lh) // 2))
        # Palette : l'image est un aplat creme plus un logo a deux encres.
        # 64 couleurs suffisent et divisent le poids par dix.
        nom = "lancement-%dx%d@%dx.png" % (l_css, h_css, densite)
        toile.quantize(colors=64, method=Image.MEDIANCUT).save(
            SORTIE / nom, optimize=True)
        lignes.append((nom, l_css, h_css, densite,
                       (SORTIE / nom).stat().st_size))

    # L'icone que iOS pose sur l'ecran d'accueil. Sans elle, iOS fabrique
    # l'icone a partir d'une capture de la page -- une vignette illisible.
    icone = Image.open(RACINE / "branding" / "wortando-app-icon.png").convert("RGB")
    icone.resize((180, 180), Image.LANCZOS).save(
        RACINE / "branding" / "wortando-apple-touch-icon.png", optimize=True)

    total = sum(l[4] for l in lignes)
    for nom, l, h, d, o in lignes:
        print("  %-26s %5dx%-5d @%dx  %6.1f ko" % (nom, l*d, h*d, d, o/1024))
    print("  %d ecrans, %.0f ko au total" % (len(lignes), total/1024))
    print("  apple-touch-icon 180x180 : %.1f ko" % (
        (RACINE/"branding"/"wortando-apple-touch-icon.png").stat().st_size/1024))

if __name__ == "__main__":
    main()
