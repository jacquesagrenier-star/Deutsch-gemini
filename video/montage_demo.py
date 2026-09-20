# -*- coding: utf-8 -*-
"""LE MONTAGE MUET de la demo -- l'histoire avant la voix.

    python video/montage_demo.py --langue en
    python video/montage_demo.py --langue en --immobile

POURQUOI MUET, ET POURQUOI D'ABORD. Une narration posee trop tot FIGE le
montage : deplacer un plan oblige alors a reenregistrer, et a le refaire dans
chaque langue. Muet, deplacer un plan coute dix secondes. On regarde donc
d'abord si l'histoire tient -- si un plan traine, si l'ordre est mauvais, si le
tableau arrive trop tard -- et la voix vient ensuite, une seule fois, sur un
montage fige.

⚠️ LES IMAGES VIENNENT DU BANC, JAMAIS D'UNE CAPTURE A LA MAIN. Relancer
`python video/banc.py --photos --langue en` les refait a l'etat courant de
l'app ; ce script ne fait que les mettre bout a bout. C'est ce qui rend le
montage jetable et refaisable, au lieu d'etre un objet qu'on protege.

⚠️ LE MOUVEMENT EST SYNTHETIQUE, ET IL SE VOIT COMME TEL. Une fenetre qui
glisse sur une image fixe n'est pas la mosaique qui s'affine ni la carte qui se
retourne : c'est un substitut, assez bon pour juger le RYTHME et l'ORDRE, pas
pour la version finale. Les vrais mouvements se tournent avec `--clips`.

⚠️ `--immobile` N'EST PAS UN REPLI, C'EST UNE PROPOSITION. Sur des ecrans
charges de texte, l'oeil lit mieux une image qui ne bouge pas, et les coupes
suffisent a donner le rythme. Les deux versions se rendent en trente secondes :
on les compare, on ne les discute pas.
"""
import argparse
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LARGEUR, HAUTEUR, FPS = 1080, 1920, 30

# Une phrase de narration par plan -- voir video/banc.py.
# Les plans, dans l'ordre du recit. Chaque entree : image, duree, et l'ANCRE --
# quelle part de la capture compte, de 0 (le haut) a 1 (le bas). Une capture
# d'iPhone fait 2796 px de haut pour une image de 1920 : il y a toujours 800 px
# qu'on ne montre pas, et c'est l'ancre qui decide lesquels.
#
# ⚠️ PLUS DE VA-ET-VIENT. Les plans alternaient haut-bas / bas-haut << pour
# donner un cote vivant >> ; Jacques, en spectateur : << ca me derange >>. Il a
# raison, et la raison est mecanique -- l'oeil suit le mouvement, et un
# mouvement qui change de sens a chaque plan le fait repartir a zero neuf fois
# en trente secondes, au lieu de lire. Le mouvement, quand il y en a un, va
# maintenant TOUJOURS dans le meme sens et deux fois moins vite.
PLANS = [
    ("accueil-01.png",          4.0, 0.00),  # 1. une seance t'attend
    ("carte-01-recto.png",      2.5, 0.00),  # 2. tu reponds...
    ("carte-02-verso.png",      4.0, 0.00),  #    ...et l'echeance suit
    ("ecoute-02-en-ecoute.png", 4.0, 0.05),  # 3. quand tu ne peux pas regarder
    ("tableau-02-milieu.png",   2.5, 0.00),  # 4. chaque carte affine...
    ("tableau-04-gagne.png",    4.0, 0.00),  #    ...a la derniere, il est a toi
    ("dictionnaire-01.png",     4.5, 0.10),  # 5. un mot te manque ?
    ("examens-01-panneau.png",  3.5, 0.15),  # 6. les listes officielles
    ("retour-01.png",           3.0, 0.35),  # 7. dis-nous ce qui t'aiderait
]

# De combien la fenetre glisse, en part de ce qui depasse. 0 = image immobile.
GLISSE = 0.35

def ffmpeg(args):
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + args)
    if r.returncode != 0:
        sys.exit("ffmpeg a echoue : " + " ".join(args[:6]))


def plan(image, duree, ancre, glisse, cible):
    """Un plan : l'image montee a 1080 de large, et une fenetre de 1920 posee
    dessus a l'ancre -- qui glisse un peu vers le bas si `glisse` n'est pas nul.

    ⚠️ LE DEPLACEMENT EST BORNE PAR min/max. Sans ca, une image moins haute que
    1920 apres mise a l'echelle donne un decalage negatif, et ffmpeg s'arrete
    sur une erreur de filtre -- sur UNE image du lot, a la fin du rendu."""
    course = "(ih-%d)" % HAUTEUR
    depart = "%s*%s" % (course, ancre)
    if glisse:
        y = "%s+%s*%s*t/%s" % (depart, course, glisse, duree)
    else:
        y = depart
    y = "min(max(%s,0),%s)" % (y, course)
    ffmpeg(["-loop", "1", "-t", str(duree), "-i", str(image),
            "-vf", "scale=%d:-2,crop=%d:%d:0:'%s',fps=%d,format=yuv420p"
                   % (LARGEUR, LARGEUR, HAUTEUR, y, FPS),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(cible)])


def main():
    a = argparse.ArgumentParser(description="Monte la demo muette a partir des plans du banc.")
    a.add_argument("--langue", default="en")
    a.add_argument("--appareil", default="iphone67")
    a.add_argument("--sortie", default=None)
    a.add_argument("--immobile", action="store_true",
                   help="aucun mouvement : des images fixes, le rythme vient des coupes")
    args = a.parse_args()

    source = RACINE / "video" / "demo" / args.langue / args.appareil
    if not source.exists():
        sys.exit("Aucun plan pour cette langue. Lancer d'abord :\n"
                 "  python video/banc.py --photos --langue %s" % args.langue)

    travail = source / "_montage"
    travail.mkdir(exist_ok=True)
    morceaux = []
    glisse = 0 if args.immobile else GLISSE
    for i, (nom, duree, ancre) in enumerate(PLANS):
        image = source / nom
        if not image.exists():
            print("  MANQUE  " + nom + " -- plan saute")
            continue
        cible = travail / ("%02d.mp4" % i)
        plan(image, duree, ancre, glisse, cible)
        morceaux.append(cible)

    if not morceaux:
        sys.exit("Aucun plan a monter.")

    liste = travail / "liste.txt"
    liste.write_text("".join("file '%s'\n" % m.as_posix() for m in morceaux), encoding="utf-8")
    nom_defaut = "wortando-demo-%s-%s.mp4" % ("immobile" if args.immobile else "calme", args.langue)
    sortie = Path(args.sortie) if args.sortie else source.parent / nom_defaut
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(liste), "-c", "copy", str(sortie)])
    duree = sum(d for n, d, a in PLANS if (source / n).exists())
    print("%s  (%d plans, %.1f s)" % (sortie, len(morceaux), duree))


if __name__ == "__main__":
    main()
