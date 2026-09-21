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
# ⚠️ LES CLIPS VIENNENT DU MEME DOSSIER QUE LES CAPTURES, ET PLUS D'AILLEURS.
# Le montage cherchait d'abord dans `clip720` -- une fenetre plus large, essayee
# pour gagner en nettete -- puis retombait sur le dossier normal. Deux sources
# pour une meme scene, et la plus ancienne gagnait : le film a montre pendant
# deux versions un plan refilme le matin meme, avec le mot qu'on venait
# justement de remplacer. Signale par Jacques : << je vois encore euro >>.
# Une preference silencieuse entre deux dossiers est un piege a version
# perimee ; on n'en garde qu'un.

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
PROMO = [
    ("suite:affinage",          4.6, 0.00),  # 1. le tableau se precise -- L'ACCROCHE
    ("clip:choix_niveau",       8.6, 0.00),  # 2. tu choisis, tu commences, la carte est la
    ("clip:retournement",       4.5, 0.00),  # 3. tu reponds -- LE VRAI GESTE
    ("clip:ecoute_suite",       3.8, 0.05),  # 4. les mains libres -- LE VRAI LECTEUR
    ("clip:dictionnaire_frappe", 11.0, 0.00),  # 5. trois lettres, un mot choisi, sa carte
    ("retour-01.png",           2.6, 0.35),  # 6. dis-nous ce qui t'aiderait

# ⚠️ LE PLAN DES EXAMENS EST RETIRE (demande de Jacques). C'etait le seul qui ne
# montrait ni geste ni mouvement : un panneau qu'on lit, dans un film qu'on
# regarde. Ce qu'il portait -- les listes officielles Goethe et DTZ -- se dit
# mieux en une ligne de narration ou sur une carte-titre qu'en trois secondes
# d'ecran fixe.
]

# ============ LE TOUR DU PROPRIETAIRE ============
# ⚠️ CE N'EST PAS LE MEME FILM, ET CE N'EST PAS LA MEME QUESTION. Jacques, le
# 21 septembre : << quand on entre dans l'application, on n'est pas trop
# certain de ce qu'on peut faire avec >>. Une promo retient quelqu'un qui
# pourrait partir ; une explication dresse la carte pour quelqu'un qui est deja
# entre -- son professeur d'allemand, un etudiant a qui on a dit << regarde
# ca >>. Personne ne la regarde par hasard.
#
# ⚠️ D'OU TROIS RENVERSEMENTS PAR RAPPORT A LA PROMO :
#   - on commence par ce qu'on fait TOUS LES JOURS, pas par l'image la plus
#     forte : l'accroche sert a retenir, pas a expliquer ;
#   - le tableau passe a la fin, a sa place reelle -- une recompense se decouvre
#     en chemin, elle ne s'annonce pas ;
#   - la duree cesse d'etre un ennemi. Vingt-sept secondes, c'est une
#     bande-annonce.
#
# ⚠️ ET LE DICTIONNAIRE REVIENT. Dans une promo c'etait l'argument le plus
# copiable ; dans une explication, << tu peux chercher n'importe quel mot et en
# faire une carte >> est exactement ce qu'un usager a besoin de savoir.
TOUR = [
    ("clip:choix_niveau",       5.7, 0.00),  # 1. ouvrir, choisir son niveau, commencer
    ("clip:retournement",       5.2, 0.00),  # 2. repondre, et l'echeance suit
    ("clip:tuiles",             5.5, 0.00),  # 3. LA CARTE DES LIEUX -- la reponse a la question
    ("clip:ecoute_suite",       4.5, 0.05),  # 4. les mains libres
    ("clip:dictionnaire_frappe", 7.5, 0.00),  # 5. un mot qui manque devient une carte
    ("clip:reglages_defile",    8.6, 0.00),  # 6. ce qu'on regle soi-meme, en descendant
    ("suite:affinage",          4.6, 0.00),  # 7. ce qu'on gagne en chemin
    ("clip:langues",            7.1, 0.00),  # 8. l'app dans ta langue -- la preuve
]

FILMS = {"promo": PROMO, "tour": TOUR}

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

# ⚠️ ACCELERER UN PLAN, C'EST MENTIR UN PEU -- alors on le note ici, en clair,
# plutot que de le cacher dans un filtre. Un geste d'interface supporte 1,3x
# sans qu'on le voie : la main va un peu plus vite, rien d'autre ne change. Le
# plan du dictionnaire enchaine quatre gestes (ouvrir, taper, choisir,
# retourner) et durerait quinze secondes dans un film qui en fait trente.
# Au-dela de 1,4x, la frappe devient une saccade : ce n'est plus du rythme,
# c'est du sucre.
VITESSE = {"dictionnaire_frappe": 1.3, "reglages_defile": 1.35}

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


# La couleur de fond de l'app, prise dans manifest.json : la carte-titre n'est
# pas un ecran de plus, c'est le meme papier que tout le reste.
PAPIER = "0xF2EEE2"
LOGO = "branding/wortando-logo-pale.png"


def carte_titre(duree, cible):
    """Le monogramme sur le papier de l'app, en fondu.

    ⚠️ LE LOGO SEUL, AUCUNE PHRASE. Une accroche inventee pour finir un film
    est une promesse que personne n'a relue -- et elle vieillit avant l'app.
    Le nom suffit : c'est la seule chose qu'on demande au spectateur de retenir.
    ⚠️ ET PAS DE VERSION CLAIRE SUR FOND FONCE : `wortando-logo-pale.png` est
    fait pour les sections claires, `-dark` pour les foncees. Poser l'un sur
    l'autre donne un logo qui disparait -- ils ne sont pas interchangeables."""
    logo = RACINE / LOGO
    if not logo.exists():
        return False
    ffmpeg(["-f", "lavfi", "-i", "color=c=%s:s=%dx%d:d=%s:r=%d" % (PAPIER, LARGEUR, HAUTEUR, duree, FPS),
            "-loop", "1", "-i", str(logo),
            "-filter_complex",
            # ⚠️ format=rgba APRES scale : sans lui, le redimensionnement rend un
            # format sans couche alpha et la zone transparente du logo arrive
            # comme un rectangle pale sur le papier -- visible a l'oeil, pas
            # dans le fichier source, qui est bien transparent partout.
            "[1:v]scale=680:-1,format=rgba[l];[0:v][l]overlay=(W-w)/2:(H-h)/2:shortest=1,"
            "fade=t=in:st=0:d=0.45,format=yuv420p[v]",
            "-map", "[v]", "-t", str(duree),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(cible)])
    return True


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


def plan_clip(source, duree, ancre, cible, vitesse=1.0):
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
    presse = ("setpts=%.4f*PTS," % (1.0 / vitesse)) if vitesse and vitesse != 1.0 else ""
    ffmpeg(["-i", str(source), "-t", str(duree * (vitesse or 1.0)),
            "-vf", "%sscale=%d:-2:flags=lanczos,crop=%d:%d:0:'%s',fps=%d,format=yuv420p"
                   % (presse, LARGEUR, LARGEUR, HAUTEUR, y, FPS),
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
    a.add_argument("--recit", default="promo", choices=["promo", "tour"],
                   help="promo : 27 s, l'accroche d'abord. "
                        "tour : le tour du proprietaire, pour montrer ce qu'on peut faire")
    a.add_argument("--langue", default="en")
    a.add_argument("--appareil", default="iphone67")
    a.add_argument("--sortie", default=None)
    a.add_argument("--transition", default="coupe", choices=["coupe", "fondu", "bascule"],
                   help="coupe : rien entre les plans. fondu : un fondu enchaine. "
                        "bascule : l'image s'ecrase et se rouvre, comme une carte qu'on retourne")
    a.add_argument("--titre-debut", action="store_true",
                   help="poser aussi une carte-titre AU DEBUT (a comparer : elle depense "
                        "les trois secondes qui decident si la suite est regardee)")
    a.add_argument("--sans-titre", action="store_true",
                   help="ne pas ajouter la carte-titre de fin")
    a.add_argument("--immobile", action="store_true",
                   help="aucun mouvement : des images fixes, le rythme vient des coupes")
    args = a.parse_args()

    source = RACINE / "video" / "demo" / args.langue / args.appareil
    if not source.exists():
        sys.exit("Aucun plan pour cette langue. Lancer d'abord :\n"
                 "  python video/banc.py --photos --langue %s" % args.langue)

    plans = FILMS[args.recit]
    travail = source / ("_montage" if args.recit == "promo" else "_montage-" + args.recit)
    travail.mkdir(exist_ok=True)
    # ⚠️ ON VIDE LE PLAN DE TRAVAIL. Les morceaux sont nommes par leur RANG :
    # retirer un plan de PLANS, ou monter une fois avec une carte-titre au
    # debut, laisse derriere un fichier qui ne fait plus partie du film. Le
    # montage l'ignore -- mais voix_demo.py, lui, lit ce dossier pour savoir ou
    # commence chaque plan, et un orphelin decale toute la narration d'un plan.
    # Vu : la premiere phrase posee sur la carte-titre d'un ancien essai.
    for vieux in travail.glob("*.mp4"):
        vieux.unlink()
    morceaux = []
    # ⚠️ UNE CARTE-TITRE AU DEBUT SE PAIE SUR L'ACCROCHE. Les trois premieres
    # secondes decident si les vingt-sept suivantes sont regardees, et le nom
    # est deja dans CHAQUE plan -- l'en-tete de l'app le porte. D'ou l'option,
    # et non le defaut : on compare, on ne discute pas.
    if args.titre_debut and not args.sans_titre:
        ouverture = travail / "00-titre.mp4"
        if carte_titre(1.2, ouverture):
            morceaux.append(ouverture)
    glisse = 0 if args.immobile else GLISSE
    effet = EFFETS.get(args.transition)
    retrait = TRANSITION_S if effet else 0
    for i, (nom, duree, ancre) in enumerate(plans):
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
            plan_clip(image, max(1.0, duree - retrait), ancre, cible,
                      VITESSE.get(nom[5:], 1.0))
        else:
            plan(image, max(1.0, duree - retrait), ancre, glisse, cible)
        if effet and morceaux:
            pont = travail / ("%02d-pont.mp4" % i)
            transition(morceaux[-1], cible, effet, pont)
            morceaux.append(pont)
        morceaux.append(cible)

    if not morceaux:
        sys.exit("Aucun plan a monter.")

    # La carte-titre ferme le film. Elle vient APRES la boucle : ce n'est pas un
    # plan de l'app, et la lister parmi les autres inviterait a lui donner une
    # duree, une ancre, un mouvement -- trois occasions de la charger.
    if not args.sans_titre:
        fin = travail / "99-titre.mp4"
        if carte_titre(2.0, fin):
            if effet:
                pont = travail / "99-pont.mp4"
                transition(morceaux[-1], fin, effet, pont)
                morceaux.append(pont)
            morceaux.append(fin)

    liste = travail / "liste.txt"
    liste.write_text("".join("file '%s'\n" % m.as_posix() for m in morceaux), encoding="utf-8")
    nom_defaut = "wortando-%s-%s-%s-%s.mp4" % (
        args.recit, "immobile" if args.immobile else "calme", args.transition, args.langue)
    sortie = Path(args.sortie) if args.sortie else source.parent / nom_defaut
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(liste), "-c", "copy", str(sortie)])
    print("%s  (%d morceaux)" % (sortie, len(morceaux)))


if __name__ == "__main__":
    main()
