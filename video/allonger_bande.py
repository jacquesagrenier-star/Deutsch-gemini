# -*- coding: utf-8 -*-
"""Prolonger une bande cyclable peinte, sans repasser par fal.

    python video/allonger_bande.py --dans il-attend.png --sortie il-attend.png
    python video/allonger_bande.py --dans il-attend.png --essai

POURQUOI CET OUTIL EXISTE.

Jacques, 23 septembre 2026, sur le plan ou Mark attend au feu : << peux-tu
toi-meme allonger la piste, car lorsque le cycliste apparait elle est plus
longue >>.

Il a raison, et c'est mesurable. Dans il-attend.png la peinture rouge
s'arrete net a y=2170 et laisse 580 px d'asphalte nu jusqu'au bas du cadre :
une courte plaque qui finit au milieu de la chaussee. Dans
les-deux-hommes.png -- le plan du cycliste, la meme rue -- la piste court sur
toute la profondeur de l'image. Les deux plans se suivent a l'ecran, donc la
piste raccourcit puis rallonge sous les yeux du spectateur.

C'EST LE MEME GESTE QUE degriser_bande.py, A L'ENVERS. Celui-la retirait le
rouge en gardant la clarte de chaque pixel ; celui-ci le POSE de la meme
maniere. On ne peint pas un aplat : on prend l'asphalte qui est deja la, avec
son grain, ses reprises, ses taches, et on lui donne la teinte de la bande en
lui laissant sa luminosite. Rien a racheter, et la peinture neuve a la meme
usure que l'ancienne parce que c'est le meme revetement.

⚠️ LA TEINTE SE RELEVE DANS L'IMAGE, ELLE NE S'ECRIT PAS EN DUR. On moyenne
   les pixels franchement rouges de la bande existante et on en tire le
   rapport de chaque canal a la luminosite. Une couleur choisie a la main
   ferait une bande qui ne raccorde pas avec celle du haut -- et le raccord
   est tout le propos.

⚠️ LE BORD GAUCHE SE REGLE PAR MOINDRES CARRES, SUR LA BANDE ELLE-MEME. Il
   est droit en perspective ; 27 lignes suffisent a le fixer. Le prolonger a
   la main donnerait un coude, et un coude dans un marquage se voit
   immediatement.

⚠️ ET LA BORDURE DE GRANIT NE SE DISTINGUE PAS DE L'ASPHALTE PAR LA COULEUR.
   Mesure du 23 sept. : granit L=112 a 149, asphalte L=139 a 155, r-g de 13 a
   20 des deux cotes. Aucun seuil ne les separe. C'est donc la GEOMETRIE qui
   tient la bande a distance du trottoir -- le bord gauche extrapole laisse
   100 a 190 px d'asphalte gris entre la peinture et le granit, ce qui est
   aussi ce qu'on voit dans le plan du cycliste. La couleur ne sert qu'a
   proteger les traits blancs, eux qui sont franchement plus clairs (L>180).
"""
import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("  Il faut Pillow : python -m pip install Pillow")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Franchement rouge : mesure du 23 sept. -- la bande est a r-g de 59 a 66,
# l'asphalte a 9 a 17, le pantalon beige de Mark a 28. 35 passe au milieu.
ROUGE_MIN = 35
ROUGE_MIN_B = 25

# Un trait blanc peint. Mesure : traits a L=187 a 205, asphalte a 139 a 155.
BLANC_MIN = 180


def clarte(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def est_rouge(c):
    return c[0] - c[1] > ROUGE_MIN and c[0] - c[2] > ROUGE_MIN_B


def relever_bande(px, larg, haut, depuis_x):
    """Le bord gauche de la bande (droite des moindres carres), son bas, sa teinte.

    On ne regarde qu'a droite de depuis_x : ailleurs dans l'image il y a des
    matieres chaudes -- la facade creme, la peau, le pantalon beige -- et ce
    n'est pas a un seuil de couleur de les ecarter.
    """
    bords, teinte, n_teinte = [], [0.0, 0.0, 0.0], 0
    bas = 0
    for y in range(haut):
        xs = [x for x in range(depuis_x, larg) if est_rouge(px[x, y])]
        if len(xs) <= 40:
            continue
        bords.append((y, min(xs)))
        bas = y
        for x in xs[::7]:
            c = px[x, y]
            teinte[0] += c[0]; teinte[1] += c[1]; teinte[2] += c[2]
            n_teinte += 1
    if len(bords) < 10:
        sys.exit("  moins de 10 lignes de bande trouvees : rien a prolonger.")

    n = len(bords)
    sy = sum(b[0] for b in bords); sx = sum(b[1] for b in bords)
    syy = sum(b[0] * b[0] for b in bords); sxy = sum(b[0] * b[1] for b in bords)
    pente = (n * sxy - sy * sx) / float(n * syy - sy * sy)
    ord0 = (sx - pente * sy) / float(n)

    moy = [v / n_teinte for v in teinte]
    lc = clarte(moy)
    ratio = [moy[0] / lc, moy[1] / lc, moy[2] / lc]
    return pente, ord0, bas, ratio, n


def main():
    p = argparse.ArgumentParser(
        description="Prolonger une bande cyclable peinte jusqu'au bas du cadre.")
    p.add_argument("--dans", required=True,
                   help="l'image, chemin depuis la racine du depot")
    p.add_argument("--sortie", help="ou ecrire ; sans elle, --essai est impose")
    p.add_argument("--depuis-x", type=int, default=900,
                   help="on ne cherche le rouge qu'a droite de cette colonne")
    p.add_argument("--marge", type=int, default=0,
                   help="decaler le bord gauche vers la droite, en px")
    p.add_argument("--fondu", type=int, default=4,
                   help="largeur de la lisiere du bord gauche, en px")
    p.add_argument("--essai", action="store_true",
                   help="dire la mesure et n'ecrire aucune image")
    a = p.parse_args()

    dans = a.dans if os.path.isabs(a.dans) else os.path.join(RACINE, a.dans)
    if not os.path.exists(dans):
        sys.exit("  introuvable : %s" % dans)

    im = Image.open(dans).convert("RGB")
    larg, haut = im.size
    px = im.load()

    pente, ord0, bas, ratio, n = relever_bande(px, larg, haut, a.depuis_x)
    print("  %s  %dx%d" % (os.path.basename(dans), larg, haut))
    print("  bord gauche : x = %.4f * y + %.1f   (%d lignes)" % (pente, ord0, n))
    print("  la bande s'arrete a y=%d, il reste %d px jusqu'au bas" % (bas, haut - bas))
    print("  teinte relevee : r/L=%.3f  g/L=%.3f  b/L=%.3f" % tuple(ratio))
    for y in (bas, (bas + haut) // 2, haut - 1):
        print("     bord gauche a y=%d -> x=%d" % (y, int(pente * y + ord0) + a.marge))

    if a.essai or not a.sortie:
        print("\n  (essai -- aucune image ecrite)")
        return

    touches = 0
    for y in range(bas, haut):
        xf = pente * y + ord0 + a.marge
        x0 = int(xf) - a.fondu
        if x0 < 0:
            x0 = 0
        for x in range(x0, larg):
            c = px[x, y]
            if est_rouge(c):
                continue          # deja de la peinture rouge
            lc = clarte(c)
            if lc > BLANC_MIN:
                continue          # un trait blanc peint
            # Le bord gauche se fond sur --fondu pixels. Un masque coupe au
            # pixel se lit comme un masque : la peinture, elle, a une lisiere.
            k = 1.0
            if a.fondu:
                k = (x - (xf - a.fondu)) / float(a.fondu)
                if k <= 0.0:
                    continue
                if k > 1.0:
                    k = 1.0
            # On interpole depuis LE PIXEL LUI-MEME, pas depuis un gris neutre :
            # a k=0 il doit etre intact, sinon la lisiere decolore l'asphalte.
            px[x, y] = tuple(
                min(255, max(0, int(c[i] + (ratio[i] * lc - c[i]) * k + 0.5)))
                for i in (0, 1, 2))
            touches += 1

    sortie = a.sortie if os.path.isabs(a.sortie) else os.path.join(RACINE, a.sortie)
    im.save(sortie)
    print("\n  -> %s  (%d pixels repeints)" % (sortie, touches))


if __name__ == "__main__":
    main()
