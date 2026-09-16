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
     r"(?i)\b(no head|no hair|no face|no shoulder|no blurred figure|"
     r"no part of anyone|is NEVER seen|nobody walks in|nobody passes)\b",
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
]

MARQUEURS = re.compile(r"(?im)^(first|then|next|after that|finally)\b")


# La phrase de camera verrouillee contient elle-meme les mots << zoom >> et
# << push-in >>, precedes de << no >>. Une regle qui cherche ces mots se declenche
# donc sur la consigne qu'elle est censee proteger : premier faux positif du
# controle, trouve en le lancant. On retire la phrase avant de chercher.
PHRASE_VERROU = re.compile(r"(?i)Locked-off camera:[^.]*\.")


def controler(texte):
    """Rend la liste des (code, gravite, titre, cout, remede, extrait)."""
    trouves = []
    sans_verrou = PHRASE_VERROU.sub(" ", texte)
    for code, gravite, motif, titre, cout, remede in REGLES:
        if code == "trop-de-temps":
            n = len(MARQUEURS.findall(texte))
            if n > 3:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d temps marques" % n))
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


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("fichier", nargs="?")
    p.add_argument("--scene")
    a = p.parse_args()
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
