# -*- coding: utf-8 -*-
"""La tenue raccorde-t-elle d'un plan a l'autre ? Mesure, puis accord.

    python video/accorder_tenue.py --mesurer a.png b.png
    python video/accorder_tenue.py --dans b.png --modele a.png --sortie c.png

POURQUOI, ET CE QUE CA REMPLACE.

Jacques, 16 septembre 2026, a propos du plan 12 fabrique SANS image de
reference : << comment on s'assure que la couleur des pantalons et des
souliers, c'est la meme chose ? >>

Reponse honnete : le prompt ne l'assure pas. Il verrouille les mots -- beige
cotton chino trousers, white leather low-top sneakers -- ce qui reduit la
derive sans la supprimer. Ce qui l'assure, c'est de MESURER les deux images
et d'accorder la seconde sur la premiere.

C'est la meme discipline que le jaune du blouson : on n'a pas dit << ca a
l'air pareil >>, on a releve RGB (210,212,52) contre (210,209,81) et conclu
que le gag tenait. Une impression ne raccorde rien ; un chiffre, oui.

⚠️ ON N'ACCORDE QUE CE QUI EST DEJA PRESQUE JUSTE. Cet outil deplace des
   niveaux, il ne repeint pas. Si le modele a rendu un pantalon gris au lieu
   de beige, il faut refaire l'image -- et l'outil le dit au lieu de maquiller
   l'ecart.

⚠️ ET ON N'ACCORDE PAS TOUTE L'IMAGE. Le rouge de la bande et le gris des
   dalles ont leurs propres valeurs, mesurees ailleurs. Corriger globalement
   pour rattraper un pantalon casserait le decor. On travaille par MASQUE.
"""
import argparse
import os
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

# Les deux pieces a surveiller, definies par ce qu'elles SONT en couleur, pas
# par une position : d'un plan a l'autre elles ne sont jamais au meme endroit.
PIECES = {
    "souliers": lambda r, v, b: (min(r, v, b) > 150
                                 and max(r, v, b) - min(r, v, b) < 34),
    "pantalon": lambda r, v, b: (110 < r < 235 and r > v > b
                                 and 12 < r - b < 85 and r - v < 40),
    # Le gris des dalles n'est pas une piece de tenue : c'est le BLANC DE
    # REFERENCE. Il est neutre par nature et present dans les deux plans.
    "_gris": lambda r, v, b: (95 < r < 205
                              and max(r, v, b) - min(r, v, b) < 16),
}


def mesurer(chemin, pas=6):
    img = Image.open(chemin).convert("RGB")
    L, H = img.size
    px = img.load()
    out = {}
    for nom, test in PIECES.items():
        pts = [px[x, y] for y in range(0, H, pas) for x in range(0, L, pas)
               if test(*px[x, y])]
        if len(pts) < 150:
            out[nom] = None
            continue
        n = len(pts)
        out[nom] = (tuple(sum(p[i] for p in pts) // n for i in range(3)), n)
    return img, out


def dire(chemin, m):
    print("  %s" % os.path.basename(chemin))
    for nom in sorted(PIECES):
        v = m.get(nom)
        if v is None:
            print("    %-9s introuvable dans l'image" % nom)
        else:
            print("    %-9s RGB %-16s sur %d px" % (nom, str(v[0]), v[1]))


def ecart(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def relatif(m):
    """La tenue RAPPORTEE au gris des dalles de la meme image.

    ⚠️ LA PREMIERE VERSION COMPARAIT DES RGB ABSOLUS, ET ELLE MESURAIT
       L'EXPOSITION. Entre bande-rouge-pieds (gros plan, a l'ombre du corps)
       et les-deux-hommes (plan large, plein jour), elle annoncait 41 points
       d'ecart sur le pantalon et concluait << ce n'est plus la meme tenue >>,
       alors que les deux images sont bonnes et deja validees.

       Une metrique non etalonnee n'arbitre rien -- c'est deja arrive dans ce
       projet, le 16 septembre, quand une mesure avait prefere la prise que
       Jacques avait rejetee. Le gris des dalles est neutre par nature et
       present partout : il sert de blanc de reference, et le RAPPORT au gris
       ne depend plus de la lumiere."""
    g = m.get("_gris")
    if not g:
        return None
    gris = g[0]
    out = {}
    for nom, v in m.items():
        if nom.startswith("_") or not v:
            continue
        out[nom] = tuple(round(100.0 * v[0][i] / max(1, gris[i]))
                         for i in range(3))
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--mesurer", nargs="+")
    p.add_argument("--dans")
    p.add_argument("--modele", help="l'image qui fait foi (le plan precedent)")
    p.add_argument("--sortie")
    p.add_argument("--ecart-max", type=int, default=40,
                   help="au-dela, on refuse d'accorder : ce n'est plus une "
                        "derive, c'est une autre tenue")
    a = p.parse_args()

    if a.mesurer:
        for c in a.mesurer:
            dire(c, mesurer(c)[1])
        if len(a.mesurer) == 2:
            _, m1 = mesurer(a.mesurer[0])
            _, m2 = mesurer(a.mesurer[1])
            r1, r2 = relatif(m1), relatif(m2)
            if not (r1 and r2):
                print("\n  pas de gris de reference dans une des deux images :"
                      "\n  la comparaison resterait une mesure d'exposition.")
                return
            print("\n  rapportes au gris des dalles (100 = la valeur du gris) :")
            for nom in sorted(r1):
                if nom in r2:
                    e = ecart(r1[nom], r2[nom])
                    print("    %-9s %-16s contre %-16s  %2d points  %s"
                          % (nom, str(r1[nom]), str(r2[nom]), e,
                             "ok" if e <= 8 else
                             "a accorder" if e <= 25 else
                             "TROP LOIN -- ce n'est plus la meme tenue"))
        return

    if not (a.dans and a.modele and a.sortie):
        sys.exit("  Preciser --mesurer, ou --dans, --modele et --sortie.")

    img, m2 = mesurer(a.dans)
    _, m1 = mesurer(a.modele)
    px = img.load()
    L, H = img.size
    corriges = 0

    for nom, test in PIECES.items():
        if not (m1.get(nom) and m2.get(nom)):
            print("    %-9s absent d'une des deux images -- laisse tel quel"
                  % nom)
            continue
        cible, actuel = m1[nom][0], m2[nom][0]
        e = ecart(cible, actuel)
        if e <= 12:
            print("    %-9s deja d'accord (%d points)" % (nom, e))
            continue
        if e > a.ecart_max:
            sys.exit("  %s : %d points d'ecart. Ce n'est pas une derive de\n"
                     "  niveaux, c'est une autre tenue -- il faut refaire\n"
                     "  l'image, pas la maquiller." % (nom, e))
        d = [cible[i] - actuel[i] for i in range(3)]
        for y in range(H):
            for x in range(L):
                c = px[x, y]
                if test(*c):
                    px[x, y] = tuple(min(255, max(0, c[i] + d[i]))
                                     for i in range(3))
                    corriges += 1
        print("    %-9s decale de %s (%d points d'ecart)" % (nom, d, e))

    img.save(a.sortie)
    print("  %d px corriges  ->  %s" % (corriges, a.sortie))


if __name__ == "__main__":
    main()
