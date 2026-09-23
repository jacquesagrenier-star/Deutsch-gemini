# -*- coding: utf-8 -*-
"""Reposer un marquage peint preleve dans une AUTRE image du meme decor.

    python video/poser_pictogramme.py --source .../carrefour-rouge.png --boite 562,2020,1179,2203 --cible .../il-attend.png --quad 995,2380,1436,2330,1436,2600,995,2660 --essai

POURQUOI CET OUTIL EXISTE.

Jacques, 23 septembre 2026, sur le plan de la chute : << c'est a cela que la
piste devrait ressembler, avec le velo en blanc. >>

L'HISTOIRE, PARCE QU'ELLE EXPLIQUE L'ECART. il-attend-v1.png (16 sept.) avait
une bande longue AVEC son pictogramme. La retouche du 22 sept. -- celle qui
ajoutait la traverse pour pietons devant Mark -- a repeint la chaussee, et au
passage elle a raccourci la bande et efface le velo. Personne ne l'a vu : on
regardait la traverse. Puis Seedance, en fabriquant le clip du plan 18 depuis
cette image, a RECOMPOSE une bande longue avec un pictogramme -- un modele
image-vers-video re-rend la scene et corrige ce qui lui parait invraisemblable.
Resultat : le clip monte etait juste et l'image fixe dont il vient etait
fausse. C'est l'ecart que Jacques a vu.

⚠️ LA LECON GENERALE : UNE RETOUCHE QUI REPEINT UNE SURFACE EMPORTE CE QUI
   ETAIT DESSUS. On demande une traverse, on perd un pictogramme. Apres toute
   retouche de chaussee, comparer la surface repeinte a la version d'avant --
   pas seulement regarder ce qu'on avait demande.

ET POURQUOI ON PRELEVE PLUTOT QUE DE DESSINER. Le pictogramme de
carrefour-rouge.png est le meme marquage, dans le meme carrefour, sous la meme
lumiere, a pleine resolution : 617 x 183 px de peinture reelle, avec son usure.
Un dessin vectoriel serait propre et n'aurait ni usure ni grain. Celui du clip
serait le bon cadrage mais vient d'une video, donc mou des qu'on l'agrandit.

⚠️ L'ALPHA SE TIRE DE LA COULEUR, PAS D'UN DETOURAGE. La peinture blanche est
   DESATUREE, la bande est franchement rouge : alpha = (rouge du fond - rouge
   du pixel) / (rouge du fond - rouge de la peinture). Les bords crenele s'en
   trouvent doux tout seuls, et aucun contour n'est trace a la main.

⚠️ ET LA PEINTURE SE POSE DANS LA LUMIERE DE L'IMAGE D'ARRIVEE. On mesure la
   clarte de la bande autour du glyphe a la source et a la cible, et on
   applique le rapport. Sans ca le velo arrive avec l'eclairage de l'autre
   plan et flotte au-dessus de la bande.
"""
import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("  Il faut Pillow : python -m pip install Pillow")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# r-g de la peinture blanche. Mesure du 23 sept. sur les 9 668 px du glyphe de
# carrefour-rouge : median 21, 90e centile 25. Une valeur trop basse -- 10 au
# premier essai -- donne un alpha de 0,80 sur la peinture pleine, et le velo
# arrive fantome. Il se mesure, il ne se suppose pas.
ROUGE_PEINTURE = 22.0


def clarte(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def resoudre(a, b):
    """Gauss avec pivot partiel. Pas de numpy : le depot n'en depend pas."""
    n = len(b)
    m = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[piv][col]) < 1e-12:
            sys.exit("  quadrilatere degenere : deux coins confondus ?")
        m[col], m[piv] = m[piv], m[col]
        d = m[col][col]
        m[col] = [v / d for v in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                f = m[r][col]
                m[r] = [m[r][k] - f * m[col][k] for k in range(n + 1)]
    return [m[i][n] for i in range(n)]


def coefficients(quad_cible, quad_source):
    """Les 8 coefficients de Image.PERSPECTIVE : cible -> source.

    PIL echantillonne la SOURCE en chaque point de la CIBLE, donc c'est bien
    ce sens-la qu'il faut resoudre -- l'inverse donne un glyphe retourne.
    """
    A, b = [], []
    for (x, y), (u, v) in zip(quad_cible, quad_source):
        A.append([x, y, 1, 0, 0, 0, -x * u, -y * u]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -x * v, -y * v]); b.append(v)
    return resoudre(A, b)


def rouge_du_fond(px, x0, y0, x1, y1):
    """Le r-g de la bande, releve sur le pourtour de la boite du glyphe."""
    vals = []
    for x in range(x0, x1, 3):
        for y in (y0, y0 + 1, y1 - 2, y1 - 1):
            c = px[x, y]; vals.append(c[0] - c[1])
    for y in range(y0, y1, 3):
        for x in (x0, x0 + 1, x1 - 2, x1 - 1):
            c = px[x, y]; vals.append(c[0] - c[1])
    vals.sort()
    return vals[len(vals) // 2]


def clarte_bande(px, x0, y0, x1, y1, seuil_rouge):
    """La clarte moyenne de la bande (pixels rouges) dans une boite."""
    s, n = 0.0, 0
    for y in range(y0, y1, 4):
        for x in range(x0, x1, 4):
            c = px[x, y]
            if c[0] - c[1] > seuil_rouge * 0.7:
                s += clarte(c); n += 1
    return s / n if n else 1.0


def main():
    p = argparse.ArgumentParser(
        description="Reposer un marquage peint preleve dans une autre image.")
    p.add_argument("--source", required=True, help="l'image ou se trouve le marquage")
    p.add_argument("--boite", required=True, help="x0,y0,x1,y1 du glyphe dans la source")
    p.add_argument("--cible", required=True, help="l'image ou le poser")
    p.add_argument("--quad", required=True,
                   help="8 nombres : les 4 coins dans la cible, en partant du "
                        "coin qui recoit le HAUT-GAUCHE du glyphe, sens horaire")
    p.add_argument("--sortie", help="ou ecrire ; sans elle, --essai est impose")
    p.add_argument("--essai", action="store_true", help="dire la mesure, ne rien ecrire")
    a = p.parse_args()

    def chemin(c):
        return c if os.path.isabs(c) else os.path.join(RACINE, c)

    src = Image.open(chemin(a.source)).convert("RGB")
    cib = Image.open(chemin(a.cible)).convert("RGB")
    x0, y0, x1, y1 = [int(v) for v in a.boite.split(",")]
    q = [float(v) for v in a.quad.split(",")]
    if len(q) != 8:
        sys.exit("  --quad veut 8 nombres.")
    quad = [(q[0], q[1]), (q[2], q[3]), (q[4], q[5]), (q[6], q[7])]

    ps = src.load()
    rouge_fond = rouge_du_fond(ps, x0, y0, x1, y1)
    lc_src = clarte_bande(ps, x0, y0, x1, y1, rouge_fond)

    # ⚠️ LA BOITE DOIT ETRE ENTIEREMENT DANS LA BANDE. L'alpha prend pour de la
    #    peinture tout ce qui est peu rouge -- donc aussi l'asphalte gris. Au
    #    premier essai la boite depassait en haut de la bande et une BARRE
    #    GRISE est arrivee en travers du velo. Ce controle-la a coute un rendu.
    gris = 0
    for y in range(y0, y1, 2):
        for x in range(x0, x1, 2):
            c = ps[x, y]
            if c[0] - c[1] < 28 and clarte(c) < 180:
                gris += 1
    total = len(range(y0, y1, 2)) * len(range(x0, x1, 2))
    if gris > total * 0.01:
        sys.exit("  %.1f %% de la boite n'est ni peinture ni bande rouge : elle\n"
                 "  depasse du marquage. Resserre --boite -- sinon l'asphalte\n"
                 "  gris sera pose comme de la peinture." % (100.0 * gris / total))

    # La boite de la cible qui contient le quadrilatere.
    bx0 = int(min(c[0] for c in quad)); bx1 = int(max(c[0] for c in quad)) + 1
    by0 = int(min(c[1] for c in quad)); by1 = int(max(c[1] for c in quad)) + 1
    pc = cib.load()
    lc_cib = clarte_bande(pc, max(0, bx0), max(0, by0),
                          min(cib.size[0], bx1), min(cib.size[1], by1), rouge_fond)
    facteur = lc_cib / lc_src

    print("  source : %s, glyphe %dx%d" % (os.path.basename(a.source), x1 - x0, y1 - y0))
    print("  rouge du fond a la source : r-g = %d" % rouge_fond)
    print("  clarte de la bande  source %.1f   cible %.1f   -> facteur %.3f"
          % (lc_src, lc_cib, facteur))
    print("  quadrilatere dans la cible : %s" % (quad,))
    print("  boite : x %d..%d  y %d..%d  (%dx%d)"
          % (bx0, bx1, by0, by1, bx1 - bx0, by1 - by0))

    if a.essai or not a.sortie:
        print("\n  (essai -- aucune image ecrite)")
        return

    # cible -> source, dans le repere de la boite
    quad_local = [(c[0] - bx0, c[1] - by0) for c in quad]
    src_quad = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    co = coefficients(quad_local, src_quad)

    gab = src.transform((bx1 - bx0, by1 - by0), Image.PERSPECTIVE, co,
                        Image.BICUBIC)
    pg = gab.load()
    ecart = float(rouge_fond) - ROUGE_PEINTURE
    poses = 0
    for yy in range(by1 - by0):
        y = by0 + yy
        if y < 0 or y >= cib.size[1]:
            continue
        for xx in range(bx1 - bx0):
            x = bx0 + xx
            if x < 0 or x >= cib.size[0]:
                continue
            g = pg[xx, yy]
            alpha = (rouge_fond - (g[0] - g[1])) / ecart
            if alpha <= 0.02:
                continue
            if alpha > 1.0:
                alpha = 1.0
            c = pc[x, y]
            pc[x, y] = tuple(
                min(255, max(0, int(c[i] + (g[i] * facteur - c[i]) * alpha + 0.5)))
                for i in (0, 1, 2))
            poses += 1

    sortie = chemin(a.sortie)
    cib.save(sortie)
    print("\n  -> %s  (%d pixels de peinture posee)" % (sortie, poses))


if __name__ == "__main__":
    main()
