# -*- coding: utf-8 -*-
"""Le bonhomme du feu berlinois, DESSINE puis incruste. Aucun appel paye.

    python video/ampelmann.py --planche            # voir les deux poses
    python video/ampelmann.py --dans image.png --lentille 1046,415,34 \\
        --flou 3.4 --sortie image-corrigee.png

POURQUOI ON LE DESSINE AU LIEU DE LE DEMANDER.

Deux essais rates chez nano-banana le 16 septembre 2026. Le prompt decrivait
pourtant le chapeau et les deux bras tendus : le modele a boulonne un PANNEAU
CARRE ROUGE sur le mat -- avec en prime la pose du VERT coloriee en rouge --
et laisse dans le boitier une silhouette quelconque. Jacques : << il l'a mis
sur le poteau et non dans le feu lui-meme >>.

Ce n'etait pas un manque de detail. Le mot << Ampelmaennchen >> tire vers
l'imagerie de souvenir -- panneaux, autocollants, vitrines -- dont les corpus
debordent, et un prompt ne dit jamais assez fermement OU une icone est posee.

Un graphique fixe, lui, ne derive pas. C'est le meme avantage que le recadrage
d'une prise deja payee : on arrete de racheter une chance, on fabrique une
certitude. Et le decor ne se remeuble plus d'un plan a l'autre, puisque les
huit plans recoivent le MEME bonhomme au pixel pres.

⚠️ LES DEUX POSES NE SONT PAS SYMETRIQUES, ET JE LES AVAIS ECRITES A L'ENVERS.
   ROUGE : de face, immobile, LES DEUX BRAS A L'HORIZONTALE.
   VERT  : de profil, EN MARCHE vers la droite, bras balances, jambes
           ecartees.
   Verifie sur les photos de Jacques, 16 septembre 2026.

⚠️ ET ON NE COLLE PAS UN DESSIN NET DANS UNE IMAGE FLOUE. Le feu est au fond
   du cadre, donc dans le flou d'arriere-plan. Une incrustation nette se voit
   immediatement -- c'est le defaut exact de la rustine du plan 17 de
   l'episode 2, << on voit une image par-dessus l'autre >>. D'ou --flou, et
   d'ou `flou_local()`, qui MESURE le flou autour de la lentille au lieu de
   le deviner.
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")

# Le dessin vit dans une boite de 200 x 240, origine en haut a gauche. Tout
# le reste est mis a l'echelle depuis la, pour que les proportions ne
# dependent jamais de la taille de la lentille visee.
BOITE = (200, 240)


class Echelle(object):
    """Un ImageDraw qui multiplie tout ce qu'on lui donne.

    Le dessin est ecrit une fois dans la boite de 200 x 240 et rendu k fois
    plus grand, puis reduit : c'est la seule facon d'avoir des obliques
    propres. La version precedente dessinait a la taille finale puis
    agrandissait au plus proche voisin -- un surechantillonnage pour rien,
    et des escaliers sur les jambes du vert."""

    def __init__(self, d, k):
        self.d, self.k = d, k

    def _b(self, xy):
        return [v * self.k for v in xy]

    def rounded_rectangle(self, xy, radius=0, fill=None):
        self.d.rounded_rectangle(self._b(xy), radius=radius * self.k, fill=fill)

    def ellipse(self, xy, fill=None):
        self.d.ellipse(self._b(xy), fill=fill)

    def polygon(self, pts, fill=None):
        self.d.polygon([(x * self.k, y * self.k) for x, y in pts], fill=fill)

    def line(self, pts, fill=None, width=1):
        self.d.line([(x * self.k, y * self.k) for x, y in pts],
                    fill=fill, width=int(round(width * self.k)))


def _rond(d, x0, y0, x1, y1, r):
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=255)


def _barre(d, a, b, ep):
    """Un membre : un segment epais a bouts ARRONDIS.

    PIL coupe les lignes a l'equerre ; le bonhomme berlinois n'a pas un seul
    angle vif. On repose donc un disque a chaque extremite."""
    d.line([a, b], fill=255, width=ep)
    r = ep / 2.0
    for x, y in (a, b):
        d.ellipse([x - r, y - r, x + r, y + r], fill=255)


def rouge(d):
    """De face, immobile, les deux bras a l'horizontale.

    Trapu : c'est ce qui le distingue d'un pictogramme de sortie de secours.
    Les jambes tiennent dans le tiers bas, les bras sont epais, et
    l'envergure depasse largement le chapeau."""
    _rond(d, 78, 10, 122, 36, 12)             # calotte du chapeau
    _rond(d, 40, 33, 160, 50, 8)              # bord, tres large
    d.ellipse([74, 44, 126, 94], fill=255)    # tete
    _rond(d, 60, 96, 140, 168, 16)            # torse, large et court
    _rond(d, 2, 104, 68, 134, 15)             # bras gauche, epais
    _rond(d, 132, 104, 198, 134, 15)          # bras droit
    _rond(d, 66, 160, 94, 228, 13)            # jambe gauche, courte
    _rond(d, 106, 160, 134, 228, 13)          # jambe droite


def vert(d):
    """De profil, EN MARCHE vers la droite, bras balances, grand pas."""
    _rond(d, 66, 10, 116, 34, 11)             # calotte
    _rond(d, 34, 31, 152, 46, 7)              # bord, deborde vers l'avant
    d.ellipse([68, 40, 116, 88], fill=255)    # tete
    d.polygon([(64, 92), (122, 92), (130, 150), (72, 154)], fill=255)
    _barre(d, (120, 102), (176, 124), 21)     # bras avant, lance en avant
    _barre(d, (70, 106), (26, 132), 20)       # bras arriere, ramene en bas
    _barre(d, (88, 150), (54, 212), 24)       # cuisse arriere
    _barre(d, (54, 212), (40, 222), 20)       # pied arriere, au sol
    _barre(d, (108, 150), (150, 200), 24)     # cuisse avant
    _barre(d, (150, 200), (168, 222), 20)     # pied avant, qui se pose


POSES = {"rouge": (rouge, (252, 58, 34)), "vert": (vert, (74, 214, 86))}


def silhouette(pose, hauteur):
    """Le masque du bonhomme, en niveaux de gris, a la hauteur demandee.

    Dessine huit fois trop grand puis reduit : les bords obliques du vert
    seraient crenelees autrement, et un crenelage se voit encore mieux une
    fois pose dans du flou."""
    k = 8
    m = Image.new("L", (BOITE[0] * k, BOITE[1] * k), 0)
    POSES[pose][0](Echelle(ImageDraw.Draw(m), k))
    large = int(round(hauteur * BOITE[0] / float(BOITE[1])))
    return m.resize((large, int(hauteur)), Image.LANCZOS)


def planche(dst):
    """Les deux poses, sur leur lentille, pour juger le dessin avant tout."""
    img = Image.new("RGB", (520, 340), (26, 26, 28))
    d = ImageDraw.Draw(img)
    for i, pose in enumerate(("rouge", "vert")):
        cx = 140 + i * 240
        d.rounded_rectangle([cx - 105, 20, cx + 105, 320], radius=26,
                            fill=(18, 18, 20), outline=(70, 70, 74), width=3)
        d.ellipse([cx - 88, 82, cx + 88, 258], fill=(8, 8, 9))
        poser(img, pose, (cx, 170), 176, flou=0.0)
        d.text((cx - 18, 292), pose, fill=(150, 150, 154))
    img.save(dst)
    print("  planche : %s" % dst)


def eteindre(img, centre, rayon, fond=None):
    """Eteint la lentille : la figure deja presente s'en va.

    Sans ca on empile deux bonshommes, et le premier deborde du second --
    exactement le defaut de la rustine du plan 17 de l'episode 2, ou l'on
    voyait une main apparaitre sous l'autre.

    La couleur du verre eteint n'est pas inventee : elle est PRELEVEE sur la
    lentille voisine du meme boitier, celle qui n'est pas allumee.

    ⚠️ ET LE DISQUE NE DOIT PAS DEBORDER DE LA LENTILLE. La premiere version
       l'etendait a 1,25 fois le rayon et le fondait sur 0,18 rayon : la
       couleur du verre bavait donc sur 15 px de BOITIER tout autour, et ca
       se voyait comme un voile carre -- mesure a la difference de pixels,
       156 x 156 exactement, la taille du tampon. Le fondu doit rester a
       l'interieur du verre ; c'est le bord du verre lui-meme qui cache la
       couture."""
    cx, cy = centre
    if fond is None:
        fond = (14, 16, 15)
    d = int(rayon * 1.02)
    tampon = Image.new("RGB", (d * 2, d * 2), fond)
    masque = Image.new("L", (d * 2, d * 2), 0)
    marge = max(2, int(rayon * 0.10))
    ImageDraw.Draw(masque).ellipse(
        [marge, marge, d * 2 - 1 - marge, d * 2 - 1 - marge], fill=255)
    masque = masque.filter(ImageFilter.GaussianBlur(max(1.0, rayon * 0.05)))
    img.paste(tampon, (cx - d, cy - d), masque)
    return img


def sa_lumiere(img, pose, centre, rayon, fond, flou=1.2, part=0.95,
               halo=0.55):
    """Decoupe le bonhomme DANS la lampe deja allumee, sans rien repeindre.

    Le meilleur rouge disponible est celui que l'image porte deja. Une lampe
    de feu n'est pas un aplat : elle a sa granulation de LED, son coeur
    surexpose, sa dominante propre et le reflet de sa vitre. Tout ca se perd
    des qu'on peint par-dessus avec une couleur choisie -- et ce qui se perd
    est exactement ce qui faisait croire a une lampe.

    On procede donc a l'envers : on MET DE COTE la lentille telle qu'elle
    est, on eteint, puis on redepose la lumiere d'origine a travers la
    decoupe du bonhomme. Le resultat n'est pas une incrustation par-dessus
    une image, c'est la meme image avec moins de lumiere allumee.

    ⚠️ Ne vaut que si la lampe est DEJA allumee et unie. Pour une lentille
       eteinte, ou pour un feu noye dans le flou d'arriere-plan, `poser()`
       et sa couleur dessinee restent la bonne route."""
    cx, cy = centre
    d = int(rayon * 1.35)
    boite = (cx - d, cy - d, cx + d, cy + d)
    lampe = img.crop(boite)

    eteindre(img, centre, rayon, fond=fond)

    base = silhouette(pose, rayon * 2 * part)
    masque = Image.new("L", (d * 2, d * 2), 0)
    coin = (d - base.size[0] // 2, d - base.size[1] // 2)

    if halo > 0:
        large = base.filter(ImageFilter.GaussianBlur(max(flou, 1.0) * 2.8))
        large = large.point(lambda v: int(v * halo))
        voile = Image.new("L", (d * 2, d * 2), 0)
        voile.paste(large, coin)
        img.paste(lampe, boite[:2], voile)

    masque.paste(base.filter(ImageFilter.GaussianBlur(flou)), coin)
    img.paste(lampe, boite[:2], masque)
    return img


def poser(img, pose, centre, diametre, flou=0.0, force=1.0, halo=0.55,
          part=0.95, noyau=(255, 194, 158)):
    """Incruste le bonhomme dans une lentille de `diametre` px, centree.

    Le bonhomme occupe 0,80 du diametre en hauteur : proportion relevee sur
    les photos de Jacques -- la lumiere ne touche pas le bord de la lentille,
    il reste un anneau sombre tout autour.

    ⚠️ ET UNE LAMPE ALLUMEE DEBORDE D'ELLE-MEME. Une silhouette posee a plat,
       meme floue, reste un autocollant : il lui manque le halo, et il lui
       manque le coeur surexpose. Trois couches, donc : un voile large et
       faible, la figure, puis un noyau plus clair que le rouge. C'est le
       premier essai sur mark-marche qui l'a montre -- la figure y lisait
       comme une croix terne alors que la lampe d'origine etait un bloc vif.

    `part` est la hauteur du bonhomme en fraction du diametre. La premiere
    valeur, 0,80, venait des photos ; elle est juste pour un feu VU DE PRES.
    Dans un arriere-plan flou la figure retrecit encore une fois floutee, et
    il faut la monter."""
    haut = diametre * part
    base = silhouette(pose, haut)
    couleur = POSES[pose][1]
    x = int(round(centre[0] - base.size[0] / 2.0))
    y = int(round(centre[1] - base.size[1] / 2.0))
    tache = Image.new("RGB", base.size, couleur)

    if halo > 0:
        large = base.filter(ImageFilter.GaussianBlur(max(flou, 1.0) * 2.6))
        large = large.point(lambda v: int(v * halo))
        img.paste(tache, (x, y), large)

    m = base.filter(ImageFilter.GaussianBlur(flou)) if flou > 0 else base
    if force < 1.0:
        m = m.point(lambda v: int(v * force))
    img.paste(tache, (x, y), m)

    if noyau:
        # Le coeur : la meme forme RETRECIE, donc seulement la ou la figure
        # est epaisse. Un MinFilter erode ; les bras minces disparaissent et
        # le torse reste, ce qui est exactement ce que fait une vraie lampe.
        c = base.filter(ImageFilter.MinFilter(3))
        c = c.filter(ImageFilter.GaussianBlur(max(flou * 0.7, 0.6)))
        c = c.point(lambda v: int(v * 0.90))
        img.paste(Image.new("RGB", base.size, noyau), (x, y), c)
    return img


def effacer_panneau(img, boite, ciel):
    """Efface le panneau parasite en recopiant le ciel, LIGNE PAR LIGNE.

    Le ciel berlinois d'un matin couvert n'est pas d'une seule valeur : il
    palit vers le haut. Une couleur unique se verrait comme un rectangle. On
    prend donc, pour chaque ligne, la valeur MEDIANE d'une bande de ciel
    propre a la meme hauteur -- l'image dit elle-meme ce qu'il faut ecrire,
    et rien n'est choisi a la main."""
    px = img.load()
    for y in range(boite[1], boite[3]):
        ech = sorted(px[x, y] for x in range(ciel[0], ciel[2]))
        c = ech[len(ech) // 2]
        for x in range(boite[0], boite[2]):
            px[x, y] = c
    return img


def prolonger_mat(img, mat, jusqu_a=0):
    """Prolonge le mat vers le haut, prive du panneau qui le coiffait.

    ⚠️ PAS EN REPETANT UNE TRANCHE. Le premier essai empilait une tranche de
       44 px : la moindre variation de lumiere dedans revenait tous les
       44 px et donnait un mat ANNELE, comme une colonne vertebrale. Un mat
       est uniforme dans le sens de sa hauteur, donc on etire UNE SEULE
       LIGNE et plus rien ne peut se repeter."""
    x0, y0, x1, y1 = mat
    ligne = img.crop((x0, y0 + 8, x1, y0 + 9))
    haut = y0 + 8 - jusqu_a
    if haut > 0:
        img.paste(ligne.resize((x1 - x0, haut), Image.BILINEAR), (x0, jusqu_a))
    return img


def trouver_lentille(img, fenetre):
    """Trouve la lampe ROUGE ALLUMEE dans une fenetre, et la rend mesuree.

    ⚠️ PARCE QUE L'ESTIMER A L'OEIL RATE. Sur carrefour-rouge j'avais lu le
       centre a 10 px pres, et l'extinction a laisse un croissant rouge en
       haut a gauche de la lentille -- visible tout de suite. A l'oeil on
       vise le coeur brillant ; or le verre s'etend plus loin que lui, et
       c'est le verre qu'il faut couvrir.

    Le seuil regarde l'ECART entre le rouge et les deux autres canaux, pas
    la valeur du rouge : une facade creme a un rouge eleve et un ecart nul,
    une lampe a un ecart franc, meme sur son bord sombre."""
    x0, y0, x1, y1 = fenetre
    px = img.load()
    pts = [(x, y) for y in range(y0, y1) for x in range(x0, x1)
           if px[x, y][0] > px[x, y][1] + 22 and px[x, y][0] > px[x, y][2] + 22]
    if len(pts) < 200:
        sys.exit("  aucune lampe rouge dans la fenetre %s (%d px)"
                 % (fenetre, len(pts)))
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    cx, cy = (min(xs) + max(xs)) // 2, (min(ys) + max(ys)) // 2
    r = max(max(xs) - min(xs), max(ys) - min(ys)) / 2.0
    return cx, cy, int(round(r * 1.04))


def flou_local(img, centre, rayon):
    """Mesure le flou AUTOUR de la lentille, pour ne pas le deviner.

    On prend la couronne juste en dehors de la lentille -- le boitier et ce
    qui le borde -- et on regarde combien un leger flou supplementaire change
    l'image. Dans une zone deja floue il ne change presque rien ; dans une
    zone nette il change beaucoup. Le rapport donne un rayon utilisable."""
    c = int(rayon * 2.4)
    b = img.crop((centre[0] - c, centre[1] - c, centre[0] + c, centre[1] + c))
    b = b.convert("L")
    n = b.filter(ImageFilter.GaussianBlur(1.0))
    ecart = sum(abs(a - z) for a, z in zip(b.getdata(), n.getdata()))
    ecart /= float(b.size[0] * b.size[1])
    # Etalonne sur mark-marche : 0,9 sur une zone nette, 0,12 dans le bokeh.
    if ecart <= 0.05:
        return 6.0
    return max(0.0, min(8.0, 0.55 / ecart))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--planche", action="store_true")
    p.add_argument("--dans", help="l'image ou incruster")
    p.add_argument("--sortie")
    p.add_argument("--pose", default="rouge", choices=sorted(POSES))
    p.add_argument("--lentille", help="cx,cy,rayon en pixels")
    p.add_argument("--fenetre", help="x0,y0,x1,y1 ou CHERCHER la lampe rouge "
                                     "-- elle est alors mesuree, pas estimee")
    p.add_argument("--flou", type=float, default=None,
                   help="rayon du flou ; sans lui, il est MESURE sur place")
    p.add_argument("--force", type=float, default=1.0)
    p.add_argument("--part", type=float, default=1.02,
                   help="hauteur du bonhomme, en fraction du diametre")
    p.add_argument("--verre", help="x,y sur la lentille ETEINTE du meme "
                                   "boitier : sa couleur sert de fond")
    p.add_argument("--panneau", help="x0,y0,x1,y1 du panneau a effacer")
    p.add_argument("--ciel", help="x0,y0,x1,y1 de ciel propre, meme hauteur")
    p.add_argument("--mat", help="x0,y0,x1,y1 d'une tranche saine du mat")
    p.add_argument("--sa-lumiere", action="store_true", dest="sa_lumiere",
                   help="decouper le bonhomme DANS la lampe deja allumee, "
                        "au lieu de le repeindre")
    a = p.parse_args()

    if a.planche:
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "ampelmann-planche.png")
        planche(d)
        return
    if not (a.dans and a.sortie and (a.lentille or a.fenetre)):
        sys.exit("  Preciser --dans, --sortie, et --lentille cx,cy,r "
                 "ou --fenetre x0,y0,x1,y1.")
    n = lambda s: [int(v) for v in s.split(",")]                  # noqa: E731
    img = Image.open(a.dans).convert("RGB")
    if a.fenetre:
        cx, cy, r = trouver_lentille(img, n(a.fenetre))
        print("  lentille mesuree : centre %d,%d  rayon %d" % (cx, cy, r))
    else:
        cx, cy, r = n(a.lentille)
    flou = a.flou if a.flou is not None else flou_local(img, (cx, cy), r)
    print("  flou %.2f px  (%s)"
          % (flou, "impose" if a.flou is not None else "mesure sur place"))

    if a.panneau and a.ciel:
        effacer_panneau(img, n(a.panneau), n(a.ciel))
        print("  panneau efface")
    if a.mat:
        prolonger_mat(img, n(a.mat))
        print("  mat prolonge")
    if a.panneau:
        # La couture se voit tant qu'elle reste nette au milieu du flou.
        b = n(a.panneau)
        zone = (b[0] - 10, 0, b[2] + 10, b[3] + 14)
        img.paste(img.crop(zone).filter(ImageFilter.GaussianBlur(flou * 0.8)),
                  zone[:2])

    fond = img.getpixel(tuple(n(a.verre))) if a.verre else None
    if a.sa_lumiere:
        sa_lumiere(img, a.pose, (cx, cy), r, fond, flou=flou, part=a.part)
    else:
        eteindre(img, (cx, cy), r, fond=fond)
        poser(img, a.pose, (cx, cy), r * 2, flou=flou, force=a.force,
              part=a.part)
    img.save(a.sortie)
    print("  %s" % a.sortie)


if __name__ == "__main__":
    main()
