# -*- coding: utf-8 -*-
"""Les fautes de prompt qu'on a deja payees -- et qu'on ne repaiera plus.

    python video/verifier_prompt.py --scene 02-beim-buergeramt
    python video/verifier_prompt.py <un fichier de prompt>

POURQUOI CE FICHIER EXISTE, ET POURQUOI IL EST UN PROGRAMME ET PAS UNE NOTE.

Le 16 septembre 2026, Jacques : << j'ai l'impression qu'on n'apprend pas de nos
erreurs suffisamment >>. Il avait raison, et la preuve etait dans le depot :
chaque faute ci-dessous etait DEJA ecrite quelque part -- dans A-TOURNER.txt,
dans OU-ON-EN-EST.txt, dans le journal des retours -- et chacune a ete refaite
malgre tout.

Une lecon rangee dans un document se relit quand on y pense. Celle-ci s'execute
avant chaque depense : `omnihuman.py` appelle ce controle avant de televerser
quoi que ce soit, et refuse de payer sur une faute connue. C'est la seule forme
de memoire qui ait tenu jusqu'ici dans ce projet -- la meme idee que
`tests/verifier.py` pour l'application.

⚠️ CE QU'IL NE SAIT PAS FAIRE. Il lit du texte, pas une intention : il
   n'attrapera jamais une direction de jeu fausse, un contresens, une phrase
   allemande maladroite. Il attrape ce qui est ATTRAPABLE, c'est-a-dire ce
   qu'on a deja paye deux fois. Passer le controle ne veut pas dire que le
   prompt est bon.

⚠️ ET CHAQUE REGLE PORTE SA DATE ET SON COUT. Sans ca, la liste devient un
   reglement qu'on ne discute plus. Une regle dont la cause a disparu doit
   pouvoir etre retiree -- il suffit de savoir d'ou elle venait.
"""
import argparse
import glob
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Les fautes. (code, gravite, motif, titre, ce qu'elle a coute, comment faire)
# --------------------------------------------------------------------------
#   "faute"  -> on ne depense pas. Elle nous a deja coute une prise.
#   "doute"  -> on previent et on continue. Elle demande un coup d'oeil.
REGLES = [
    ("garde-negative", "faute",
     # ⚠️ ELARGIE LE 16 SEPT. 2026, APRES UNE RELECTURE CROISEE.
     #    La premiere version n'enumerait que les formulations exactes de
     #    l'episode 2 : elle ne voyait donc QUE le passe. Un relecteur
     #    exterieur a propose << No feet or shoes touch the red lane >> en
     #    le presentant comme une garde POSITIVE -- et le controle l'a
     #    laisse passer sans broncher.
     #
     #    La forme dangereuse n'est pas un vocabulaire, c'est une
     #    STRUCTURE : une negation qui nomme un ACTEUR et une ACTION. Pour
     #    la refuser, le modele doit d'abord se representer l'acteur en
     #    train d'agir -- et c'est precisement ce qu'il fabrique.
     r"(?i)(\b(no head|no hair|no face|no shoulder|no blurred figure|"
     r"no part of anyone|is NEVER seen|nobody walks in|nobody passes)\b"
     r"|\bno\s+\w+(?:\s+(?:or|and)\s+\w+)?\s+"
     r"(?:touch|touches|enter|enters|appear|appears|walk|walks|pass|"
     r"passes|cross|crosses|stand|stands|move|moves|is seen|are seen)\b)",
     u"La garde qui enumere ce qu'il ne faut pas montrer",
     u"16 sept. 2026 : QUATRE prises sur six (09, 13, 15, 17). On a obtenu une "
     u"nuque, des cheveux, une epaule, un bras, une silhouette floue -- "
     u"exactement les mots de l'interdiction, du cote precis ou elle "
     u"s'appliquait. ~2,80 $ et une demi-journee.",
     u"Ces modeles n'ont aucun canal pour les negations : le schema de l'API "
     u"n'a ni negative_prompt ni seed, donc tout ce qu'on ecrit decrit ce "
     u"qu'il faut MONTRER. Remplir la place plutot que l'interdire : << To his "
     u"left the counter runs on, bare except for the sign and the stamp, and "
     u"behind it a plain pale-green wall. >>"),

    ("absent-qui-agit", "faute",
     r"(?i)(until it is taken|when he takes it|once he takes it|"
     r"hands? it to (him|her)|as (he|she) takes)",
     u"Une consigne que seule la personne hors champ pourrait accomplir",
     u"16 sept. 2026, plan 13 : << the hand stays out until it is taken >>, "
     u"alors qu'un autre paragraphe interdit qu'on voie Mark. Personne ne peut "
     u"prendre la feuille. Le modele a tranche : il l'a ramenee vers lui, puis "
     u"elle a disparu. 0,73 $.",
     u"Une action ne peut dependre que de ce qui est DANS le cadre. Ecrire "
     u"l'etat final voulu : << it simply stays offered >>."),

    ("geste-qui-revient", "faute",
     r"(?i)(comes? back down|come back to the counter|lets the arm come back|"
     r"lowers the (arm|hand)|brings? it back|returns? (it )?to the counter)",
     u"Un geste qu'on demande d'annuler avant la fin du plan",
     u"16 sept. 2026, plan 13 : << lets the arm come back down to the counter >>. "
     u"Le modele a obei, et le geste central du plan -- tendre le formulaire -- "
     u"etait detruit. Signale par Jacques avant moi. 0,73 $.",
     u"Un plan de quatre secondes montre UN etat, et il le tient jusqu'a la "
     u"derniere image. Ce qui est tendu reste tendu."),

    ("trop-de-temps", "doute",
     None,   # compte les marqueurs, voir plus bas
     u"Plus de trois temps dans un plan de quatre secondes",
     u"16 sept. 2026, plan 13 : taper la feuille, la tendre, parler, attendre. "
     u"Le geste ajoute n'a jamais ete visible, et il a probablement brouille "
     u"l'ordre du reste.",
     u"OmniHuman est pilote par l'audio : il fait la bouche et des "
     u"micro-mouvements. Ce n'est pas un metteur en scene. Decrire un ETAT, pas "
     u"un enchainement."),

    ("geste-deja-dans-l-image", "doute",
     r"(?i)(First he (holds|picks|lifts|takes|reaches)|then holds it out|"
     r"picks up the)",
     u"Un geste qu'on demande de COMMENCER, alors que l'image le montre fini",
     u"16 sept. 2026, plan 13 : l'image maitresse montre la feuille DEJA "
     u"tendue, et le prompt demandait de la tendre. Le modele a du inventer un "
     u"avant et un apres -- d'ou le bras qui revient.",
     u"Ouvrir l'image avant d'ecrire. Si le geste y est deja fait, dire << "
     u"exactly as in the image >> et ne rien demander d'autre."),

    ("camera-qui-bouge", "doute",
     r"(?i)(zoom in|push[- ]in|dolly|pan (left|right)|tracking shot)",
     u"Un mouvement de camera dans une serie a camera verrouillee",
     u"Regle de la serie depuis l'episode 1 : tous les plans sont fixes, sinon "
     u"les raccords ne tiennent pas entre deux plans generes separement.",
     u"Garder la phrase << Locked-off camera: no zoom, no push-in, no camera "
     u"movement of any kind. >>"),

    # ----------------------------------------------------------------------
    # CE QUE L'EPISODE 1 A DEJA PAYE (video/PROCEDURE-episode.md, section
    # << Les cinq pieges, chacun paye d'une prise >>).
    #
    # ⚠️ TOUS ETAIENT DEJA ECRITS quand on a tourne l'episode 2, et l'un d'eux
    # -- << minimal negation >> -- a quand meme coute quatre prises. C'est
    # exactement la remarque de Jacques le 16 septembre : une lecon rangee dans
    # un document se relit quand on y pense. Elles s'executent maintenant.
    # ----------------------------------------------------------------------
    ("pas-de-verbe-de-parole", "faute",
     None,   # cherche une liste de verbes, voir controler()
     u"Aucun vrai verbe de parole dans le prompt",
     u"Episode 1 : c'est le remede que donne le guide d'OmniHuman pour les "
     u"bouches qui bougent mal -- << Unnatural lip movements: add explicit "
     u"speaking verbs >>. Nos premiers prompts le mettaient en derniere ligne "
     u"comme une contrainte technique, et les levres etaient fausses.",
     u"Ecrire ce qu'il DIT, avec un verbe : he says, he asks, he answers, he "
     u"greets, he explains, he names, he lists, he repeats."),

    ("fin-sans-intention", "faute",
     None,   # cherche le bloc d'apres-parole, voir controler()
     u"Rien apres la parole : l'avatar retombe en poker-face",
     u"Episode 1, documente : sans bloc d'apres-parole, le visage se fige des "
     u"que le son s'arrete. Et la moitie d'un plan de quatre secondes est du "
     u"silence -- duree_audio n'est PAS la duree du plan.",
     u"Finir par ce qu'il veut pendant qu'il se tait : << he listens without "
     u"speaking >>, et ce qui vit -- il cligne, il respire, il attend. Une "
     u"queue de plan a besoin d'une INTENTION, pas seulement de gestes."),

    ("verbe-sans-plafond", "doute",
     r"(?i)\b(lifts?|raises?) (his|her|one) (hand|arm|eyebrows?)\b",
     u"Un verbe fort sans amplitude : il sera sur-joue",
     u"Episode 1, une prise : << she lifts one hand >> -- la main est partie en "
     u"l'air. Le modele obeit au verbe s'il n'a rien d'autre.",
     u"Nommer l'amplitude AVEC le geste : << lifts one hand a few centimetres "
     u"from the counter and settles it back >>."),

    ("qualificatifs-empiles", "doute",
     None,   # compte les attenuateurs, voir controler()
     u"Des attenuations empilees : ce sera sous-joue jusqu'a l'invisible",
     u"Episode 1, une prise : << a small, gentle, closed-lipped smile... "
     u"nothing broad >> a donne presque rien. LE MODELE OBEIT AUX "
     u"MODIFICATEURS PLUS QU'AU VERBE.",
     u"Decrire l'etat d'arrivee plutot que des limites : << a half-smile that "
     u"reaches his eyes >>, et s'arreter la."),

    ("decrit-ce-que-l-image-porte", "doute",
     r"(?i)(depth of field|\b\d{2}mm\b|bokeh|soft overhead|"
     u"he wears|she wears|his hair is|her hair is|the lighting is)",
     u"Le prompt decrit ce que l'image montre deja",
     u"Episode 1 : << soft overhead terminal lighting, shallow depth of field, "
     u"50mm >> ajoutes sur la foi d'un guide TEXTE-vers-video, ou rien "
     u"n'existe avant le prompt. Ici l'image existe, et leur fiche le dit : "
     u"<< Do not describe static visual details already visible in the input "
     u"image. >>",
     u"Ne decrire que ce qui BOUGE : le visage, le regard, le geste, la "
     u"respiration."),

    ("minutage-en-secondes", "faute",
     r"(?i)\b(at|after|for|during)\s+\d+([.,]\d+)?\s*(s\b|sec|second)",
     u"Une fenetre de parole donnee en secondes",
     u"Episode 1 : c'etait la panne de Seedance -- il recevait des chiffres et "
     u"faisait ce qu'il voulait, de +0,11 a +1,96 s d'ecart. Chez un modele "
     u"pilote par l'audio, les reintroduire referait le defaut.",
     u"Le son porte deja le minutage : << let his face follow the voice >>."),

    ("objet-qui-se-materialise", "doute",
     None,   # objet nomme + plan large sans dire ce que tiennent les mains
     u"Un objet nomme, des mains dont on ne dit rien : il apparaitra dedans",
     u"16 sept. 2026, plan 15 : la replique enumere deux documents, le prompt "
     u"disait seulement << one hand may rise slightly >>, et une page A4 "
     u"couverte de texte s'est MATERIALISEE dans sa main en cours de plan -- "
     u"elle n'est pas dans l'image de depart. Signale par Jacques : << elle "
     u"apparait d'un seul coup, ce n'est pas du tout realiste >>. 0,70 $.",
     u"MEME CAUSE QUE LA GARDE NEGATIVE, et c'est le principe general : ce que "
     u"le prompt NOMME, le modele le fabrique -- meme quand la phrase parle de "
     u"ce que le personnage DIT et non de ce qu'on voit. Dans un plan ou les "
     u"mains sont visibles, dire ce qu'elles tiennent, y compris rien : << his "
     u"hands rest on the counter, open and empty, and they stay there >>."),

    ("icone-nommee-par-son-nom", "faute",
     r"(?i)\b(ampelm(ae|ä)nnchen|ampelmann|berlin man|"
     r"east berlin (man|figure|signal))\b",
     u"Une icone appelee par son nom : c'est l'enseigne qui vient, pas l'objet",
     u"16 sept. 2026, DEUX images de mark-marche perdues (0,30 $). Le prompt "
     u"decrivait pourtant le chapeau et les deux bras tendus. Le modele a "
     u"boulonne un PANNEAU CARRE ROUGE sur le mat -- avec la pose du VERT "
     u"coloriee en rouge -- et laisse dans le boitier une silhouette "
     u"quelconque. Jacques : << il l'a mis sur le poteau et non dans le feu "
     u"lui-meme >>.",
     u"Le nom propre d'une icone convoque l'imagerie qui l'entoure -- "
     u"panneaux, autocollants, vitrines a souvenirs -- et aucun luxe de "
     u"detail ne dit assez fermement OU elle est posee. Deux remedes, dans "
     u"cet ordre : (1) NE PAS LA NOMMER, decrire la lampe seule, << the upper "
     u"round lens is lit and glows an even plain red >> ; (2) la DESSINER et "
     u"l'incruster -- video/ampelmann.py. Un dessin ne derive pas, il est "
     u"gratuit, et les huit plans recoivent la meme icone au pixel pres."),

    ("negations-en-nombre", "doute",
     None,   # compte, voir controler()
     u"Trop de negations -- le guide du modele demande le contraire",
     u"Le guide d'OmniHuman met << clarity, non-contradiction, and minimal "
     u"negation >> en tete de ses principes. Nos prompts d'episode 1 en "
     u"alignaient QUATORZE, dont cinq d'affilee sur l'arriere-plan -- "
     u"precisement le passage qui echouait.",
     u"Un modele qui doit se representer << personne ne s'avance >> doit "
     u"d'abord se representer quelqu'un qui s'avance. Leurs propres exemples "
     u"sont positifs : << The leaves in the background sway. >>"),
]

# Les verbes qui font parler. Un prompt sans aucun d'eux decrit une pose, pas
# une replique -- et c'est la cause documentee des bouches qui bougent mal.
#
# ⚠️ SANS << he >> DEVANT. La premiere version exigeait << he asks >> et ratait
# << and asks again >> du plan 16 : le verbe etait la, la phrase coordonnee
# avait laisse tomber le sujet. Un controle qui accuse un prompt correct se
# fait desarmer au bout de deux fois.
VERBES_PAROLE = re.compile(
    r"(?i)\b(says|asks|answers|replies|greets|explains|tells|names|lists|"
    r"repeats|states|adds|offers|confirms|agrees|reads|speaking)\b")

# Le bloc d'apres-parole : ce qu'il fait pendant qu'il se tait. On le cherche
# dans SON paragraphe -- celui qui commence par << Finally >>.
APRES_PAROLE = re.compile(r"(?i)(blinks?|breathes?|listens?|waits?)")
PARA_FINAL = re.compile(r"(?ms)^Finally\b.*?(?=\n\s*\n|\Z)")
# Le paragraphe de decor de la garde positive : ce qu'il nomme EST dans l'image.
PARA_DECOR = re.compile(r"(?ms)^He is alone in the room\b.*?(?=\n\s*\n|\Z)")

# Les attenuateurs. Au-dela de six dans un prompt, le geste disparait.
ATTENUATEURS = re.compile(
    r"(?i)\b(small|slight(ly)?|gentl[ey]|subtle|barely|hardly|faint(ly)?|"
    r"a little|not broad|nothing broad|minimal|tiny)\b")

# Les negations, au sens du guide : ce que le modele doit se representer pour
# le refuser.
NEGATIONS = re.compile(r"(?i)\b(no|not|never|nobody|nothing|neither|without)\b")

# Les objets que le modele sait fabriquer si on les nomme sans dire ou ils sont.
#
# ⚠️ LE PLURIEL. La premiere version ecrivait \bdocument\b et ratait
# << two documents >> -- c'est-a-dire exactement le prompt qui a fait apparaitre
# la feuille. Un controle qui rate le cas qui l'a fait naitre ne sert a rien.
OBJETS = re.compile(r"(?i)\b(forms?|sheets?|papers?|documents?|leaflets?|"
                    r"cards?|passports?|stamps?|pens?|phones?|folders?)\b")
# Ce qui compte comme << j'ai dit ce que font les mains >>.
#
# ⚠️ << empty >> TOUT SEUL NE VEUT RIEN DIRE. La premiere version l'acceptait
# comme preuve qu'on avait decrit les mains -- et la garde positive contient
# << the room is quiet and empty >> et << an empty noticeboard >>. Le controle
# se declarait donc satisfait par une phrase qui parle du MUR. Le mot doit
# etre attache aux mains.
MAINS_DITES = re.compile(
    r"(?i)(hands?[^.]{0,60}(rest|stay|lie|remain|empty|open)"
    r"|(empty|open)[^.]{0,30}hands?"
    r"|holds? (it|the sheet|the form|it out)"
    r"|in his hands?|between finger)")

MARQUEURS = re.compile(r"(?im)^(first|then|next|after that|finally)\b")


# La phrase de camera verrouillee contient elle-meme les mots << zoom >> et
# << push-in >>, precedes de << no >>. Une regle qui cherche ces mots se declenche
# donc sur la consigne qu'elle est censee proteger : premier faux positif du
# controle, trouve en le lancant. On retire la phrase avant de chercher.
PHRASE_VERROU = re.compile(r"(?i)Locked-off camera:[^.]*\.")


# Les seules regles qui ont un sens sur un prompt d'IMAGE FIXE.
#
# ⚠️ NE PAS LEUR APPLIQUER TOUT LE JEU. Une image ne parle pas, ne dure pas et
#    n'a pas de queue de plan : << pas-de-verbe-de-parole >> et
#    << fin-sans-intention >> accuseraient CHAQUE prompt d'image, tous corrects.
#    Un controle qui accuse le juste se fait desarmer au bout de deux fois --
#    c'est deja ecrit plus haut a propos de << he asks >>, et ca vaut ici.
#
#    Ce qui reste est ce qui a reellement coute des images : la garde
#    negative, l'icone appelee par son nom, et l'empilement de negations.
POUR_IMAGE = ("garde-negative", "icone-nommee-par-son-nom",
              "negations-en-nombre", "qualificatifs-empiles")


def controler(texte, image=False):
    """Rend la liste des (code, gravite, titre, cout, remede, extrait).

    `image=True` restreint le jeu a POUR_IMAGE -- voir la note ci-dessus."""
    trouves = []
    sans_verrou = PHRASE_VERROU.sub(" ", texte)
    for code, gravite, motif, titre, cout, remede in REGLES:
        if image and code not in POUR_IMAGE:
            continue
        if code == "trop-de-temps":
            n = len(MARQUEURS.findall(texte))
            if n > 3:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d temps marques" % n))
            continue
        if code == "pas-de-verbe-de-parole":
            if not VERBES_PAROLE.search(texte):
                trouves.append((code, gravite, titre, cout, remede,
                                u"aucun de : says, asks, answers, greets..."))
            continue
        if code == "fin-sans-intention":
            # ⚠️ PREMIERE VERSION FAUSSE, ET INSTRUCTIVE : elle regardait le
            # dernier tiers du FICHIER. Or deux paragraphes de forme suivent la
            # queue du plan -- le decor et le cadrage -- donc le bloc
            # d'apres-parole n'y est jamais, et huit prompts corrects etaient
            # declares fautifs. On cherche le paragraphe lui-meme.
            para = PARA_FINAL.search(texte)
            if not para:
                trouves.append((code, gravite, titre, cout, remede,
                                u"aucun paragraphe de queue de plan"))
            elif len(APRES_PAROLE.findall(para.group(0))) < 2:
                trouves.append((code, gravite, titre, cout, remede,
                                u"la queue du plan ne dit pas ce qu'il fait"))
            continue
        if code == "qualificatifs-empiles":
            n = len(ATTENUATEURS.findall(texte))
            if n > 6:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d attenuateurs" % n))
            continue
        if code == "objet-qui-se-materialise":
            # Seulement quand les mains sont dans le cadre : un plan tete et
            # epaules n'a pas de mains a decrire.
            # ⚠️ ET ON NE COMPTE PAS LES OBJETS DU DECOR. La garde positive que
            # j'ai ecrite nomme << the date stamp >> -- un objet qui est DANS
            # l'image, donc sans danger. Sans cette exception, la regle se
            # declenchait sur sept prompts dont quatre deja tournes et bons :
            # un controle qui crie tout le temps ne se lit plus.
            utile = PARA_DECOR.sub(" ", texte)
            large = re.search(r"(?i)(medium shot|waist up)", texte)
            objet = OBJETS.search(utile)
            dit_les_mains = MAINS_DITES.search(texte)
            if large and objet and not dit_les_mains:
                trouves.append((code, gravite, titre, cout, remede,
                                u"<< %s >> nomme, et rien sur ce que tiennent "
                                u"les mains" % objet.group(0)))
            continue
        if code == "negations-en-nombre":
            n = len(NEGATIONS.findall(sans_verrou))
            if n > 10:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d negations (le guide en demande le moins "
                                u"possible)" % n))
            continue
        ou = sans_verrou if code == "camera-qui-bouge" else texte
        m = re.search(motif, ou)
        if m:
            extrait = ou[max(0, m.start() - 40):m.end() + 40]
            extrait = " ".join(extrait.split())
            trouves.append((code, gravite, titre, cout, remede, extrait))
    return trouves


def dire(chemin, trouves, bavard=True):
    if not trouves:
        if bavard:
            print("  %-14s ok" % os.path.basename(chemin))
        return 0
    fautes = 0
    print("  %s" % os.path.basename(chemin))
    for code, gravite, titre, cout, remede, extrait in trouves:
        marque = "FAUTE" if gravite == "faute" else "doute"
        if gravite == "faute":
            fautes += 1
        print("    [%s] %s -- %s" % (marque, code, titre))
        print("           ... %s ..." % extrait[:110])
        print("           deja paye : %s" % cout)
        print("           a la place : %s" % remede)
    return fautes


def verifier_fichier(chemin, bavard=True):
    texte = io.open(chemin, encoding="utf-8").read()
    return dire(chemin, controler(texte), bavard)


def verifier_scene(scene, bavard=True):
    d = os.path.join(RACINE, "video", "episode-%s" % scene,
                     "_essai-avatar", "prompts")
    fichiers = sorted(glob.glob(os.path.join(d, "plan*.txt")))
    if not fichiers:
        sys.exit("  aucun prompt dans %s" % d)
    return sum(verifier_fichier(f, bavard) for f in fichiers)


def lecons():
    """Tout ce qu'on a appris, a relire AVANT d'ecrire un prompt.

    Demande de Jacques le 16 septembre 2026 : << j'aimerais qu'on passe a
    travers tout, tout ce qu'on a appris avant meme de decrire un nouveau
    prompt >>, et << je veux que cette experience-la continue a se construire >>.

    ⚠️ CE QUI FAIT VIVRE CETTE LISTE. Chaque prise refusee doit produire soit
    une regle de plus ici, soit une phrase qui dit pourquoi elle n'est pas
    mecanisable. Une prise refusee qui ne laisse rien derriere elle sera
    repayee -- c'est deja arrive quatre fois le 16 septembre, sur des lecons
    qui etaient ecrites ailleurs et que personne ne relisait.
    """
    print()
    print("  CE QU'ON A DEJA PAYE -- a relire avant d'ecrire un prompt")
    print("  " + "-" * 66)
    for code, gravite, _motif, titre, cout, remede in REGLES:
        print()
        print("  [%s] %s" % ("refus " if gravite == "faute" else "doute ", code))
        print("     %s" % titre)
        print("     deja paye  : %s" % cout)
        print("     a la place : %s" % remede)
    print()
    print("  %d regles. Une prise refusee doit en laisser une de plus." % len(REGLES))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("fichier", nargs="?")
    p.add_argument("--scene")
    p.add_argument("--lecons", action="store_true",
                   help="tout ce qu'on a appris, a relire avant d'ecrire")
    a = p.parse_args()
    if a.lecons:
        lecons()
        return
    if a.scene:
        fautes = verifier_scene(a.scene)
    elif a.fichier:
        fautes = verifier_fichier(a.fichier)
    else:
        sys.exit("  Preciser un fichier ou --scene NOM.")
    print()
    if fautes:
        print("  %d faute(s) connue(s). Elles ont deja coute une prise chacune." % fautes)
        sys.exit(1)
    print("  aucune faute connue. (Ce qui ne veut pas dire que le prompt est bon.)")


if __name__ == "__main__":
    main()
