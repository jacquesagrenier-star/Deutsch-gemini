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
# Les clips se tournent dans une fenetre plus large que les captures -- voir
# APPAREILS["clip720"] dans banc.py. On les y cherche d'abord, et on retombe
# sur le dossier des captures s'ils n'y sont pas encore.
CLIPS_APPAREIL = "clip720"

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
# ⚠️ LE TABLEAU OUVRE, ET C'EST UNE DECISION DE JACQUES : << visuellement,
# c'est plus fort >>. Dans une video de trente secondes, les trois premieres
# decident si les vingt-sept suivantes sont regardees -- et l'image la plus
# forte qu'on ait est une toile qui se precise. Elle ne demande a personne de
# comprendre avant de regarder.
#
# ⚠️ ET L'ACCUEIL NE LE SUIT PAS IMMEDIATEMENT, meme si c'est l'ordre qui vient
# naturellement : ce sont DEUX PLANS DU MEME ECRAN. Enchaines, le second se lit
# comme une repetition moins interessante que la premiere. La carte s'intercale
# -- un autre ecran, un autre geste -- et l'accueil revient plus tard, quand il
# joue son vrai role : montrer que tout part de la.
PLANS = [
    ("suite:affinage",          4.6, 0.00),  # 1. le tableau se precise -- L'ACCROCHE
    ("clip:choix_niveau",       7.2, 0.00),  # 2. tu choisis, tu commences, la carte est la
    ("clip:retournement",       3.3, 0.00),  # 3. tu reponds -- LE VRAI GESTE
    ("clip:ecoute_suite",       4.5, 0.05),  # 4. les mains libres -- LE VRAI LECTEUR
    ("dictionnaire-01.png",     4.5, 0.10),  # 5. un mot te manque ?
    ("examens-01-panneau.png",  3.5, 0.15),  # 6. les listes officielles
    ("retour-01.png",           3.0, 0.35),  # 7. dis-nous ce qui t'aiderait
]

# ⚠️ LE PLAN FIXE DE L'ACCUEIL A DISPARU, ET C'EST UN GAIN. Demande de Jacques :
# montrer qu'on CHOISIT son niveau, puis qu'on touche << Commencer >> et que la
# carte arrive. L'accueil n'est plus montre, il est UTILISE -- et c'est le seul
# plan du film ou l'on voit quelqu'un se servir de l'app. Une capture fixe de
# l'accueil, a cote de ca, ne disait rien que ce plan ne dise mieux.

# ⚠️ TROIS PLANS SONT DES CLIPS, ET C'EST LE PARTAGE QUI COMPTE. Un ecran qui
# ne bouge pas dans l'app -- le dictionnaire, les examens, le formulaire -- est
# plus honnete en image fixe : lui inventer un mouvement, c'est promettre une
# vivacite qu'il n'a pas. Les trois qui bougent VRAIMENT sont filmes, parce
# qu'aucun montage ne raconte ce qu'ils font :
#   la carte qui tourne      -- deux images ne montrent pas une rotation ;
#   le lecteur qui avance    -- deux images ne montrent pas << tout seul >> ;
#   la mosaique qui s'affine -- deux images se lisent comme DEUX tableaux,
#                               et l'information etait justement que c'est
#                               le meme.
# Les clips se tournent avec : python video/banc.py --clips --scene affinage

# De combien la fenetre glisse, en part de ce qui depasse. 0 = image immobile.
GLISSE = 0.35

# ⚠️ UNE TRANSITION SE PAIE SUR LE TEMPS DE LECTURE, pas en plus. Chaque plan
# est raccourci de la duree de la transition qui le suit : sans ca, huit
# transitions ajoutent trois secondes au film et chaque essai dure plus
# longtemps que le precedent -- on finirait par comparer des durees, pas des
# transitions.
TRANSITION_S = 0.45
# Ce que ffmpeg appelle ces effets. << fade >> est le fondu ; << squeezeh >>
# ecrase l'image horizontalement puis la rouvre : c'est l'approximation la plus
# proche d'une carte qu'on retourne, avec les outils qu'on a.
EFFETS = {"fondu": "fade", "bascule": "squeezeh"}

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


def plan_suite(dossier, duree, ancre, cible, fps_prise=15):
    """Un plan PHOTOGRAPHIE : une suite d'images pleine resolution, jouee a
    `fps_prise` et redescendue a 1080. Aucune perte de nettete -- on descend,
    on ne monte pas.

    ⚠️ LA DUREE DEMANDEE NE COMMANDE PAS LE NOMBRE D'IMAGES : elle est donnee
    par la prise. On l'ajuste par la cadence de lecture, ce qui change le rythme
    du mouvement -- pas sa fluidite."""
    images = sorted(dossier.glob("*.png"))
    if not images:
        return False
    cadence = max(4.0, len(images) / duree)
    course = "(ih-%d)" % HAUTEUR
    y = "min(max(%s*%s,0),%s)" % (course, ancre, course)
    ffmpeg(["-framerate", "%.3f" % cadence, "-i", str(dossier / "%03d.png"),
            "-vf", "scale=%d:-2:flags=lanczos,crop=%d:%d:0:'%s',fps=%d,format=yuv420p"
                   % (LARGEUR, LARGEUR, HAUTEUR, y, FPS),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(cible)])
    return True


def plan_clip(source, duree, ancre, cible):
    """Un plan filme : meme cadrage que les images fixes, coupe a la duree
    voulue.

    ⚠️ LE CLIP EST ENREGISTRE A LA TAILLE CSS DE LA FENETRE (430 x 932), pas a
    la resolution des captures (1290 x 2796) : Playwright filme la page, il ne
    la re-rend pas en triple densite. On agrandit donc en lanczos, et le texte
    est un peu plus mou que sur les plans fixes. Pour la version finale, on
    filmera dans une fenetre plus grande -- c'est un parametre, pas un
    chantier."""
    course = "(ih-%d)" % HAUTEUR
    y = "min(max(%s*%s,0),%s)" % (course, ancre, course)
    ffmpeg(["-i", str(source), "-t", str(duree),
            "-vf", "scale=%d:-2:flags=lanczos,crop=%d:%d:0:'%s',fps=%d,format=yuv420p"
                   % (LARGEUR, LARGEUR, HAUTEUR, y, FPS),
            "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(cible)])


def transition(avant, apres, effet, cible):
    """Fabrique le petit clip qui relie deux plans.

    ⚠️ ON RELIE DEUX IMAGES FIXES, PAS DEUX CLIPS. On extrait la DERNIERE image
    du plan qui finit et la PREMIERE du plan qui commence, et on fond ces
    deux-la. Un xfade pose sur les clips entiers obligerait a re-encoder tout
    le film d'un seul filtre : la moindre correction sur un plan rendrait les
    huit autres a nouveau. Ici, chaque morceau reste independant et le montage
    se recolle par simple concatenation."""
    fin = cible.with_name(cible.stem + "-a.png")
    debut = cible.with_name(cible.stem + "-b.png")
    ffmpeg(["-sseof", "-0.1", "-i", str(avant), "-frames:v", "1", str(fin)])
    ffmpeg(["-i", str(apres), "-frames:v", "1", str(debut)])
    ffmpeg(["-loop", "1", "-t", str(TRANSITION_S), "-i", str(fin),
            "-loop", "1", "-t", str(TRANSITION_S), "-i", str(debut),
            "-filter_complex",
            "[0][1]xfade=transition=%s:duration=%s:offset=0,fps=%d,format=yuv420p"
            % (effet, TRANSITION_S, FPS),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(cible)])


def main():
    a = argparse.ArgumentParser(description="Monte la demo muette a partir des plans du banc.")
    a.add_argument("--langue", default="en")
    a.add_argument("--appareil", default="iphone67")
    a.add_argument("--sortie", default=None)
    a.add_argument("--transition", default="coupe", choices=["coupe", "fondu", "bascule"],
                   help="coupe : rien entre les plans. fondu : un fondu enchaine. "
                        "bascule : l'image s'ecrase et se rouvre, comme une carte qu'on retourne")
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
    effet = EFFETS.get(args.transition)
    retrait = TRANSITION_S if effet else 0
    for i, (nom, duree, ancre) in enumerate(PLANS):
        photographie = nom.startswith("suite:")
        if photographie:
            dossier_suite = source / "sequences" / nom[6:]
            cible = travail / ("%02d.mp4" % i)
            if not plan_suite(dossier_suite, max(1.0, duree - retrait), ancre, cible):
                print("  MANQUE  " + nom + " -- plan saute")
                continue
            if effet and morceaux:
                pont = travail / ("%02d-pont.mp4" % i)
                transition(morceaux[-1], cible, effet, pont)
                morceaux.append(pont)
            morceaux.append(cible)
            continue
        filme = nom.startswith("clip:")
        if filme:
            image = source.parent / CLIPS_APPAREIL / "clips" / (nom[5:] + ".mp4")
            if not image.exists():
                image = source / "clips" / (nom[5:] + ".mp4")
        else:
            image = source / nom
        if not image.exists():
            print("  MANQUE  " + nom + " -- plan saute")
            continue
        cible = travail / ("%02d.mp4" % i)
        if filme:
            # ⚠️ UN PLAN FILME NE GLISSE PAS : il bouge deja, et lui ajouter un
            # panoramique ferait deux mouvements concurrents dans le meme plan.
            plan_clip(image, max(1.0, duree - retrait), ancre, cible)
        else:
            plan(image, max(1.0, duree - retrait), ancre, glisse, cible)
        if effet and morceaux:
            pont = travail / ("%02d-pont.mp4" % i)
            transition(morceaux[-1], cible, effet, pont)
            morceaux.append(pont)
        morceaux.append(cible)

    if not morceaux:
        sys.exit("Aucun plan a monter.")

    liste = travail / "liste.txt"
    liste.write_text("".join("file '%s'\n" % m.as_posix() for m in morceaux), encoding="utf-8")
    nom_defaut = "wortando-demo-%s-%s-%s.mp4" % (
        "immobile" if args.immobile else "calme", args.transition, args.langue)
    sortie = Path(args.sortie) if args.sortie else source.parent / nom_defaut
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(liste), "-c", "copy", str(sortie)])
    print("%s  (%d morceaux)" % (sortie, len(morceaux)))


if __name__ == "__main__":
    main()
