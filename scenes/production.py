# -*- coding: utf-8 -*-
"""Fabrique la feuille de production d'une scene : les 19 plans, deux prompts
chacun, prets a coller dans Artlist.

    python scenes/production.py --scene 01-ankunft-berlin

POURQUOI UN SCRIPT ET PAS UN DOCUMENT ECRIT A LA MAIN
    Les repliques allemandes viennent de scenes/<scene>.json. Si une phrase
    change -- et elles changeront, c'est un cours de langue -- la feuille se
    refait en une commande au lieu d'etre recopiee, avec le risque de recopier
    de travers. Le texte allemand ne doit exister qu'a un seul endroit.

CE QUE LE SCRIPT APPORTE, LUI
    La mise en scene : le cadrage de chaque plan et l'action de chaque
    replique. C'est du travail d'auteur, il vit ici, dans MISE_EN_SCENE.

LES DEUX PROMPTS, ET POURQUOI ILS SONT SEPARES
    Framing  -- l'image fixe. Elle porte le cadrage, le decor, la lumiere, la
                place du personnage. C'est elle qui tient l'identite.
    Directing -- l'animation. Elle ne decrit QUE le mouvement.

    Redecrire la composition dans le prompt d'animation lui laisse moins de
    place pour l'action, et le modele finit par n'avoir rien a animer. Verifie
    le 8 septembre 2026 : le prompt d'image utilise pour la video a produit un
    plan sans geste, ou le modele a invente un zoom faute d'instruction.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Ce qui ne change pas d'un plan a l'autre.
# --------------------------------------------------------------------------
ANNA_POSE = ("She is placed LEFT of centre and looks toward the RIGHT of frame "
             "and slightly upward, with open space in front of her gaze. She "
             "stands at an OPEN information desk in an airport arrivals hall - "
             "no glass partition, no booth, no screen. The pale desk crosses "
             "the lower third of the frame, close to the camera, with a dark "
             "tablet and a few leaflets on it. One of her hands rests on the "
             "desk beside them.")

MARK_POSE = ("He is placed RIGHT of centre and looks toward the LEFT of frame "
             "and slightly downward, with open space in front of his gaze. He "
             "stands in front of an information desk in an airport arrivals "
             "hall, the pale edge of the desk crossing the lower left corner. "
             "He wears a dark technical shell jacket over a plain dark t-shirt, "
             "slightly rumpled from travelling. The handle of a suitcase is "
             "visible at the very bottom of the frame.")

FOND = ("Soft, even light on the face. Behind, the open depth of the hall - "
        "warm interior lighting, distant travellers - thrown STRONGLY out of "
        "focus, heavy bokeh. No bright window behind the head, no vertical "
        "pillar close to the head.")

EPAULE = ("In the lower {coin} corner, only a soft dark blurred shape suggests "
          "the other person's shoulder. No second face.")

FIN_IMAGE = "Natural skin texture, realistic lighting, photorealistic, no stylization."

FIXE = "Locked-off camera. No zoom, no push-in, no camera movement of any kind."
ZOOM = "A very slow, subtle push-in throughout the shot, ending on the face."

# --------------------------------------------------------------------------
# LES TROIS TAILLES DE PLAN, ET POURQUOI ELLES CHANGENT EN COURS DE SCENE.
#
# Douze repliques au meme cadrage donnent un diaporama de tetes parlantes. Le
# cinema fait varier la taille des plans -- c'est ce qui evite la monotonie
# d'un dialogue, bien plus que des mouvements de camera ajoutes au hasard.
#
# Ici la progression raconte quelque chose : ils commencent a distance,
# etrangers et vouvoyes, et finissent proches. LE CADRAGE SUIT LA RELATION.
#
#   plans 5-6    moyen        deux inconnus, la distance polie
#   plans 8-11   moyen serre  la conversation s'installe
#   plans 12-13  serre        le coeur pratique de la scene
#   plans 14-15  moyen serre  on respire, echange bref
#   plans 16-17  serre        l'adieu, le moment le plus chaleureux
# --------------------------------------------------------------------------
TAILLES = {
    "moyen": ("Medium shot of {qui}, from the waist up, the figure occupying "
              "about half the frame height."),
    "moyen serre": ("Medium close shot of {qui}, chest up, the face filling the "
                    "upper third of the frame."),
    "serre": ("Close shot of {qui}, head and shoulders, the face filling the "
              "upper half of the frame."),
}

# --------------------------------------------------------------------------
# LA MISE EN SCENE, plan par plan. C'est le coeur du fichier.
#   cadre  -- ce qui s'ajoute a la pose type, pour l'image fixe
#   action -- le prompt d'animation. QUE du mouvement.
#   zoom   -- True seulement la ou le moment le merite (voir _lisez_moi)
# --------------------------------------------------------------------------
MISE_EN_SCENE = {
    1: dict(cadre="Vertical 9:16. Seen from inside the terminal, through a tall "
                  "glass wall: an aircraft on the apron at dusk, ground vehicles "
                  "around it, warm low sun. No people in the foreground. The "
                  "glass reflects the interior faintly.",
            action="Almost still. The faintest drift of the camera. Ground "
                   "vehicles move slowly in the distance, light shifts on the "
                   "glass. Nothing dramatic."),

    2: dict(cadre="Vertical 9:16. Wide shot of a busy airport arrivals hall, "
                  "warm evening light. Small in the frame and seen FROM BEHIND, "
                  "a young man in a dark technical shell jacket walks in pulling "
                  "ONE small cabin case on wheels, grey handle extended. No large "
                  "suitcase - he has not collected them yet. His face is not "
                  "visible. Travellers pass in "
                  "soft focus.",
            action="He walks slowly away from the camera into the hall, pulling "
                   "the cabin case. Travellers cross the frame around him. "
                   "The camera stays still."),

    3: dict(cadre="Vertical 9:16. A baggage carousel turning, suitcases going "
                  "round, seen close and slightly from above. Warm terminal "
                  "light, the hall behind thrown out of focus. No faces.",
            action="The carousel turns steadily, suitcases sliding past the "
                   "camera. A hand reaches in at the edge of frame and lifts one "
                   "away. The camera stays still."),

    4: dict(cadre="Vertical 9:16. A young man in a dark technical shell jacket, "
                  "seen from BEHIND and slightly to the side, standing still in "
                  "the hall and looking up at the overhead signs. His face is "
                  "not visible. ONE small cabin case beside him, nothing else - "
                  "he is looking for the baggage claim. Signs and travellers "
                  "softly out of focus.",
            action="He turns his head slowly, scanning the overhead signs, then "
                   "settles on one direction. His shoulders shift as he decides. "
                   "The camera stays still."),

    5: dict(pose="mark", coin="left", taille="moyen",
            action="He leans in very slightly, polite and a little tired from "
                   "the flight. His eyebrows lift as if putting a question, and "
                   "stay up as he waits for an answer. One small open-hand "
                   "gesture of enquiry, close to his body."),

    6: dict(pose="anna", coin="right", taille="moyen",
            action="She reacts immediately, without hesitating. A small open "
                   "hand indicates a direction just past him, low and close to "
                   "her body, then returns to the desk. Her head tilts slightly "
                   "at the end, eyebrows lifting as if putting a question back "
                   "to him."),

    7: dict(cadre="Vertical 9:16. Close on a baggage carousel, the number FOUR "
                  "on a sign above it out of focus in the upper frame. Suitcases "
                  "turn past the camera. Warm terminal light. No faces.",
            action="The suitcases turn steadily past the camera, one after "
                   "another. The camera stays still."),

    8: dict(pose="mark", coin="left", taille="moyen serre",
            action="A small settling of the shoulders. On the second half a "
                   "quiet pride comes into his face, and the beginning of a "
                   "smile. He holds her eye throughout."),

    9: dict(pose="anna", coin="right", taille="moyen serre",
            action="Her face opens with genuine warmth and she gives a small "
                   "welcoming nod. Then curiosity: her eyebrows lift and her "
                   "head tilts a little, as if asking."),

    10: dict(pose="mark", coin="left", taille="moyen serre",
             action="He nods once, the smile widening. A small lift "
                    "of the chin - confidence with a trace of nervousness under "
                    "it. He holds her eye."),

    # Le seul trait d'humour de l'episode, et il tient en un quart de seconde.
    # Anna porte << a dry sense of humour >> dans sa fiche et aucun plan ne s'en
    # servait. Il joue sur le Buergeramt parce que tout etranger en Allemagne a
    # une histoire de Buergeramt -- le rendez-vous dans trois mois, le guichet
    # qui ferme a midi et demi.
    #
    # IL DOIT RESTER MINUSCULE. L'humour verbal est le dernier acquis d'une
    # langue : une blague qu'on ne comprend pas a A2 est PIRE que pas de blague,
    # elle produit le sentiment d'exclusion que le debutant redoute deja. Celui
    # qui ne connait pas encore le Buergeramt voit seulement quelqu'un de
    # gentil ; celui qui y est deja alle rit. Les deux comprennent la phrase.
    #
    # Rien n'est change au dialogue ni a l'audio : ca se joue dans le prompt.
    11: dict(pose="anna", coin="right", taille="moyen serre",
             action="She becomes practical and matter-of-fact. A third of the "
                    "way in, the smallest flicker crosses her "
                    "face - a quarter-second wince of sympathy, one eyebrow "
                    "lifting, gone almost before it appears, as if she knows "
                    "exactly what he is in for. Then she is helpful again "
                    "immediately. A small precise gesture of one hand, kept "
                    "close to her body. Her eyebrows lift at the end to check "
                    "he has followed."),

    12: dict(pose="mark", coin="left", taille="serre",
             action="He glances briefly away, orienting himself in the hall, "
                    "then back to her. A slight forward lean, eyebrows raised "
                    "in question."),

    13: dict(pose="anna", coin="right", taille="serre", zoom=True,
             action="EARLY in the shot, while the framing is still wide, she "
                    "lifts one hand and indicates DOWN and to her LEFT - away "
                    "from him, into the depth of the hall behind her - a small "
                    "precise gesture, not a broad sweep. Her eyes follow her "
                    "hand briefly, then return to him and stay there as the "
                    "camera closes in. A small nod at the end."),

    18: dict(cadre="Vertical 9:16. A ticket machine standing in a lower "
                   "concourse of an airport, screen lit, seen straight on from a "
                   "few steps away. The hall around it warm and softly out of "
                   "focus, a few travellers passing.",
             action="A traveller crosses the frame in front of the machine and "
                    "walks on. The lit screen flickers gently. The camera stays "
                    "still."),

    # « Nothing else moves » a ete pris au mot : la prise du 9 septembre est
    # d'une neutralite de guichet. Jacques : « je trouve qu'il manque de
    # sourire ». On garde la question dans le visage -- c'en est une, pratique,
    # pas un moment chaleureux -- mais on lui rend l'aisance de quelqu'un qui
    # se sent bien accueilli. Un consigne d'immobilite est prise au pied de la
    # lettre par le modele ; ne l'ecrire que quand on la veut vraiment.
    14: dict(pose="mark", coin="left", taille="moyen serre",
             action="He asks lightly, easy and friendly - a warm half-smile "
                    "already on his face as he speaks, and it stays there "
                    "while he waits for the answer. His head tilts slightly, "
                    "eyebrows raised. He is enjoying the exchange."),

    15: dict(pose="anna", coin="right", taille="moyen serre",
             action="Precise and factual. A tiny nod partway through, as if "
                    "landing on a number. Her hand stays on the desk."),

    16: dict(pose="mark", coin="left", taille="serre",
             action="Warm and genuine. A small nod of thanks, his shoulders "
                    "loosening now that he knows where to go. A real smile at "
                    "the end."),

    17: dict(pose="anna", coin="right", taille="serre", zoom=True,
             action="The warmest moment of the scene. As the camera closes in a "
                    "real smile reaches her eyes. A small nod of farewell at "
                    "the end. She keeps looking at him, easy and unhurried."),

    19: dict(cadre="Vertical 9:16. The terminal exit at night, seen from inside: "
                   "dark glass doors, city lights and headlights beyond, wet "
                   "tarmac reflecting them. A figure in silhouette walks out, "
                   "small in the frame, face not visible.",
             action="The figure walks out through the doors and away into the "
                    "night. Headlights pass beyond the glass. The camera stays "
                    "still."),
}


def image_prompt(p, m):
    """Le prompt de Framing. Pour un plan de decor, le cadre est ecrit en
    entier ; pour une replique, on assemble la pose type et le fond."""
    if "cadre" in m:
        return m["cadre"] + "\n\n" + FIN_IMAGE
    qui = "@Anna" if m["pose"] == "anna" else "@Mark"
    tete = "Vertical 9:16. " + TAILLES[m["taille"]].format(qui=qui)
    pose = ANNA_POSE if m["pose"] == "anna" else MARK_POSE
    return "\n\n".join([tete, pose, FOND, EPAULE.format(coin=m["coin"]), FIN_IMAGE])


# LA REGLE LA PLUS CHERE DE LA JOURNEE : ON TOURNE LES PERSONNAGES MUETS.
#
# Le 8 septembre 2026, plan 5 passe au lip-sync. Jacques : << la bouche
# s'ouvre une derniere fois apres avoir termine de parler >>. L'audio a cet
# instant est a -91 dB -- du silence numerique. Ce n'etait donc ni la voix ni
# le calage.
#
# Ce n'etait pas sync non plus : lipsync-2-pro, essaye sur le meme plan, ouvre
# la bouche aux memes images. Et le clip D'ORIGINE, mesure image par image,
# les ouvre aussi -- a 3,10 s, 3,20 s, 3,70 s, exactement la ou on les voit.
#
# Le lip-sync REPEINT LES LEVRES. La machoire, le menton et les joues restent
# ceux du clip source. Si Seedance a fait parler le personnage pendant quatre
# secondes, il continue de mastiquer sous des levres refaites, et aucun modele
# de lip-sync ne peut defaire ca : ce n'est pas dans les levres.
#
# PREMIERE VERSION DE LA REGLE, ET POURQUOI ELLE ALLAIT TROP LOIN
#     On a d'abord ecrit : le personnage ne parle JAMAIS, bouche fermee d'un
#     bout a l'autre. Un autre modele, consulte le meme jour, a fait remarquer
#     qu'un lip-sync travaille mieux sur un visage qui porte deja un mouvement
#     de parole -- une bouche figee risque l'effet colle. C'est juste.
#
#     Ce qu'il faut retirer n'est pas la parole : c'est la parole PENDANT LE
#     SILENCE. Le personnage parle donc au debut du plan, le temps de la
#     replique, puis termine, ferme la bouche et reste la. La machoire bouge
#     ou l'oreille entend une voix, et se tait ou la voix se tait.
#
# ET POURQUOI ON NE PEUT PAS SIMPLEMENT RACCOURCIR LE CLIP
#     Ce serait plus simple : un plan de la longueur de la replique, sans
#     surplus. Mais Seedance 2.0 Mini NE DESCEND PAS SOUS 4 SECONDES, et nos
#     repliques font 1,5 a 2,7 s. Pour onze plans sur douze il n'existe aucune
#     duree de clip qui colle a l'audio -- le surplus est structurel.
#
# CE QU'ON NE FERA PAS, ET C'EST UNE REGLE DE FOND
#     Copilot, consulte le 8 septembre : << ajoute 1-2 mots neutres a la fin
#     du texte >> pour que la voix remplisse le plan. Non.
#
#     Le dialogue de cette serie N'EST PAS de la bande-son : c'est la matiere
#     du cours. Chaque mot allemand arrive dans les sous-titres, dans le
#     lexique, dans les six traductions, et sera relu par quelqu'un qui
#     apprend. Ajouter << das ist alles >> parce qu'un clip fait deux secondes
#     de trop, c'est faire apprendre du remplissage a un debutant pour arranger
#     un rendu.
#
#     La contrainte technique s'incline devant la lecon, jamais l'inverse. Si
#     un plan est trop long pour sa replique, on coupe le plan (montage.py
#     --queue) -- on n'allonge pas la replique.
#
# CE QUE CETTE REGLE N'A PAS ENCORE PROUVE
#     Elle n'a pas ete tournee. C'est une hypothese mieux argumentee que la
#     precedente, pas un resultat. Un plan suffit a la juger : 200 credits et
#     19 cents de lip-sync.
# CE QUE LES ESSAIS DU 8 SEPTEMBRE AU SOIR ONT APPRIS
#     Quatre prises du plan 5, la meme, avec des consignes de bouche
#     differentes. Mesurees image par image (video/controler_bouche.py).
#
#     << la premiere moitie du plan >>  -- MAUVAISE FORMULE. Elle suit la duree
#         du clip : 2 s de parole a 4 s, 3 s a 6 s. Mais la replique fait
#         2,27 s quoi qu'il arrive. L'instruction derivait avec un chiffre qui
#         n'a rien a voir avec elle.
#
#     DES SECONDES ABSOLUES -- ca marche. Demande << ferme 0-1 s, parle
#         1-3,5 s, ferme ensuite >> sur un clip de 4 s : le pic tombe a 0,96 s
#         et l'amplitude retombe apres 3,6 s. Seedance OBEIT a un minutage.
#         C'etait la question ouverte de la journee.
#
#     LA DUREE DU CLIP CHANGE L'OBEISSANCE. Meme consigne a 6 s : il ne
#         commence qu'a 1,9 s au lieu de 1,0. Jacques : << le mouvement
#         d'ouverture de bouche dure un petit peu trop longtemps >>. A 4 s il
#         demarre a l'heure mais la fenetre est etroite. CINQ SECONDES est
#         l'entre-deux, choisi a l'oeil.
#
#     LA FIN EST BONNE DANS TOUS LES CAS. C'est le debut qui se regle.
#
# L'idee du silence AU DEBUT vient de Jacques, et elle valait mieux que la
# mienne : un silence initial se verifie d'un coup d'oeil, une fermeture
# finale demande de comparer des courbes.
BOUCHE = ("Total clip duration: {total} seconds.\n"
          "TIMING OF THE MOUTH - this matters more than anything else here, "
          "and the numbers are exact:\n"
          "1. From 0 to {debut} seconds his or her mouth is CLOSED. Not "
          "speaking yet, just settling and looking at the other person. Do "
          "not begin a slow mouth-opening during this time - the mouth simply "
          "rests closed, then opens to speak.\n"
          "2. From {debut} to {fin} seconds: speaking. Natural, unhurried.\n"
          "3. From {fin} seconds to the end of the clip: finished. The mouth "
          "CLOSES and stays closed - it does not open again, not once, not "
          "slightly.\n"
          "Through all three phases the rest of the face lives: the eyes, a "
          "blink, a small natural head movement, the breathing. Present and "
          "engaged at every moment, whether speaking or not.")


def duree_voix(p, scene=None):
    """La duree pendant laquelle la VOIX PORTE, mesuree sur le mp3.

    LE CHAMP duree_audio NE FAIT PAS FOI. Le 8 septembre 2026 au soir, quinze
    des dix-neuf valeurs de l'episode 1 etaient fausses -- le plan 13 de
    1,60 s. Elles avaient ete ecrites une fois puis n'avaient plus suivi les
    fichiers, et rien dans la chaine ne s'en plaignait.

    Une fenetre de parole calculee sur une valeur perimee produit un clip a
    refaire : deux cents credits, et le defaut ne se voit qu'a la prise.
    On lit donc le fichier ; le champ ne sert que de dernier recours, et on
    le dit alors a l'ecran.

    ⚠️ ET LA DUREE DU FICHIER NE FAIT PAS FOI NON PLUS (9 septembre 2026)
        On mesurait le fichier. Un mp3 ne parle pas tout du long : nos
        dix-neuf repliques portent 0,10 s de silence en tete et 0,19 s en
        queue. On demandait donc a Seedance de faire articuler la machoire
        0,29 s de plus que la voix, en moyenne, et l'ecart grandissait
        jusqu'au dernier mot -- 208 ms de retard mesures sur le plan 05
        synchronise, plus 0,62 s de machoire apres le silence.

        Jacques l'a vu avant toute mesure : « la bouche continue un petit
        peu, elle n'est pas synchro ».

        Le plan 13 est le cas extreme : fichier de 7,04 s, voix qui s'arrete
        a 4,71 s, 2,33 s de silence numerique ensuite. duree_a_generer
        demandait NEUF secondes de clip pour une replique de 4,6 s.

        On mesure donc la parole, pas le fichier. Le montage, lui, garde le
        fichier entier : c'est la fenetre demandee au modele qui change.
    """
    if scene:
        f = os.path.join(RACINE, "audio", "scenes", scene,
                         "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if os.path.exists(f):
            sys.path.insert(0, os.path.join(RACINE, "video"))
            import montage as M                             # noqa: E402
            debut, fin, _ = M.parole(M.ffmpeg(), f)
            if fin > debut:
                return round(fin - debut, 2)
    return p.get("duree_audio") or p["duree"]


def bouche(p, scene=None):
    """Le bloc de minutage de la bouche pour CE plan, en secondes reelles.

    La fenetre de parole est celle de la voix : elle commence a l'amorce du
    montage et dure exactement ce que dure le fichier ElevenLabs. Demander
    autre chose ferait articuler la machoire a cote de la voix -- le defaut
    qu'on passe la journee a chasser.
    """
    debut = 0.5                        # l'amorce du montage, arrondie
    fin = debut + duree_voix(p, scene)
    # La duree totale est annoncee en tete : les trois bornes n'ont de sens
    # que dans un cadre, et le modele ne connait pas celui qu'on choisit dans
    # l'interface d'Artlist.
    return BOUCHE.format(debut="%.1f" % debut, fin="%.1f" % fin,
                         total=duree_a_generer(p, scene))


def duree_a_generer(p, scene=None):
    """Combien de secondes demander a Seedance pour ce plan.

    CINQ SECONDES par defaut, et le chiffre est mesure, pas choisi. Quatre
    prises du plan 5 le 8 septembre au soir, meme consigne de minutage :
        a 4 s  il demarre a l'heure, mais la fenetre de parole est etroite
        a 6 s  il ne commence qu'a 1,9 s au lieu de 1,0 -- Jacques : << le
               mouvement d'ouverture de bouche dure un peu trop longtemps >>
    Cinq est l'entre-deux, retenu a l'oeil.

    Plus long seulement quand la replique ne rentre pas : il faut la fenetre
    de parole, l'amorce avant, et une seconde de silence apres pour que la
    bouche ait le temps de se refermer a l'image.
    """
    return max(5, int(round(0.5 + duree_voix(p, scene) + 1.5)))


def video_prompt(m, p=None, scene=None):
    """Le prompt de Directing. Le mouvement de camera d'abord, l'action
    ensuite, et le minutage de la bouche en dernier.

    `p` est le plan de la scene. Sans lui on ne connait pas la duree de la
    replique, donc pas la fenetre de parole : le bloc de minutage est alors
    omis plutot qu'invente avec des chiffres au hasard."""
    bloc = [ZOOM if m.get("zoom") else FIXE, m["action"]]
    if "pose" in m and p:               # un decor n'a pas de visage
        bloc.append(bouche(p, scene))
    return "\n\n".join(bloc)


def html(d, scene):
    e = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    o = []
    o.append("""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Production &mdash; %s</title><style>
:root{color-scheme:light}
body{margin:0;background:#F2EEE2;color:#1C2430;
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:56rem;margin:0 auto;padding:2rem 1.25rem 5rem}
h1{font-size:1.6rem;margin:0 0 .25rem}
.sous{color:#6b6558;margin:0 0 2rem}
.regles{background:#fff;border:1px solid #e2dcc9;border-radius:10px;
 padding:1rem 1.25rem;margin-bottom:2.5rem}
.regles h2{font-size:1rem;margin:0 0 .6rem;text-transform:uppercase;
 letter-spacing:.05em;color:#6b6558}
.regles ul{margin:0;padding-left:1.1rem}.regles li{margin:.25rem 0}
article{background:#fff;border:1px solid #e2dcc9;border-radius:10px;
 padding:1.1rem 1.25rem;margin-bottom:1.5rem}
article.fait{border-color:#7a9a5b;background:#f6faf2}
h2.plan{font-size:1.15rem;margin:0 0 .1rem}
.meta{color:#6b6558;font-size:.85rem;margin:0 0 .8rem}
.de{font-size:1.05rem;margin:.2rem 0}
.fr{color:#6b6558;margin:0 0 1rem}
h3{font-size:.75rem;text-transform:uppercase;letter-spacing:.07em;
 color:#6b6558;margin:1.1rem 0 .35rem}
pre{background:#1C2430;color:#e8e4d8;border-radius:8px;padding:.85rem 1rem;
 overflow-x:auto;white-space:pre-wrap;font:13px/1.5 ui-monospace,Menlo,Consolas,monospace;margin:0}
.reglage{font:13px ui-monospace,Menlo,Consolas,monospace;color:#6b6558;margin:.4rem 0 0}
.badge{display:inline-block;background:#E8A23A;color:#1C2430;border-radius:4px;
 padding:.05rem .4rem;font-size:.72rem;font-weight:600;vertical-align:.1em}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) body{background:#15181d;color:#e8e4d8}
:root:not([data-theme="light"]) article,:root:not([data-theme="light"]) .regles{background:#1e232a;border-color:#2e353f}
:root:not([data-theme="light"]) .fr,:root:not([data-theme="light"]) .meta,
:root:not([data-theme="light"]) .sous,:root:not([data-theme="light"]) h3,
:root:not([data-theme="light"]) .reglage,:root:not([data-theme="light"]) .regles h2{color:#9aa3ae}
:root:not([data-theme="light"]) article.fait{background:#1b2620;border-color:#4a6b3a}}
</style></head><body><main>""" % e(scene))

    o.append("<h1>Feuille de production &mdash; %s</h1>" % e(scene))
    o.append('<p class="sous">%d plans &middot; %d s de video &middot; '
             'genere par <code>scenes/production.py</code></p>'
             % (len(d["plans"]), sum(p["duree"] for p in d["plans"])))

    o.append("""<div class="regles"><h2>La marche a suivre</h2><ul>
<li><b>Deux etapes par plan.</b> D'abord <b>Framing</b> (l'image fixe), puis
<b>Directing</b> (l'animation), avec l'image en <b>Start Frame</b>.</li>
<li><b>Images :</b> 9:16 &middot; 1K &middot; 4 images &mdash; 130 credits les quatre.
Le 2K est inutile : la video plafonne a 720p.</li>
<li><b>Video :</b> Seedance 2.0 Mini &middot; 9:16 &middot; 720p &middot; audio
<b>coupe</b> &middot; duree du plan, avec un <b>minimum de 4 secondes</b> : le modele
ne descend pas plus bas. Les plans de 3 s se generent donc en 4 s et se coupent au
montage &mdash; la seconde en trop est une marge, pas une perte.</li>
<li><b>N'attachez que les visages qui doivent etre reconnaissables.</b>
<code>@Anna</code>, <code>@Mark</code>. Une personne vue de dos ne s'attache pas :
l'attacher inviterait le modele a lui montrer le visage.</li>
<li><b>En Directing, aucun personnage attache.</b> Ils sont deja dans l'image.</li>
<li><b>Regard :</b> Mark vers la GAUCHE, Anna vers la DROITE. C'est ce qui donne
l'impression qu'ils se regardent.</li>
<li><b>Un seul visage ancre par plan.</b> L'autre n'est qu'une epaule floue.</li>
<li><b>Telechargez chaque prise gardee tout de suite</b> &mdash; Artlist peut
effacer sans preavis (voir <code>video/PROVENANCE.txt</code>).</li>
<li>Puis <code>python video/rapatrier.py --plan N</code> : son coupe, prise classee.</li>
</ul></div>""")

    for p in d["plans"]:
        m = MISE_EN_SCENE.get(p["n"])
        if not m:
            continue
        fait = ' class="fait"' if p["n"] == 13 else ""
        o.append("<article%s>" % fait)
        badge = ' <span class="badge">FAIT</span>' if p["n"] == 13 else ""
        o.append('<h2 class="plan">Plan %02d &mdash; %s%s</h2>' % (p["n"], e(p["locuteur"]), badge))
        o.append('<p class="meta">%s &middot; %s s &middot; audio %s s%s</p>'
                 % (e(p["type"]), p["duree"], p.get("duree_audio", "?"),
                    (" &middot; " + m["taille"] if "taille" in m else "")
                    + (" &middot; rapprochement" if m.get("zoom") else "")))
        if p.get("de"):
            o.append('<p class="de">%s</p><p class="fr">%s</p>' % (e(p["de"]), e(p.get("fr", ""))))
        o.append("<h3>1. Framing &mdash; l'image de depart</h3>")
        o.append("<pre>%s</pre>" % e(image_prompt(p, m)))
        o.append("<h3>2. Directing &mdash; l'animation</h3>")
        o.append("<pre>%s</pre>" % e(video_prompt(m, p, scene)))
        gen = max(4, p["duree"])   # Seedance 2.0 Mini ne descend pas sous 4 s
        sup = ('' if gen == p["duree"] else
               ' <b>(le plan fait %s s : la seconde en trop se coupe au montage)</b>' % p["duree"])
        o.append('<p class="reglage">Seedance 2.0 Mini &middot; 9:16 &middot; 720p &middot; '
                 '<b>%s sec</b> &middot; audio coupe%s</p>' % (gen, sup))
        o.append("</article>")

    o.append("</main></body></html>")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    a = ap.parse_args()
    src = os.path.join(RACINE, "scenes", a.scene + ".json")
    if not os.path.exists(src):
        sys.exit("  Introuvable : %s" % src)
    d = json.load(io.open(src, encoding="utf-8"))
    manquants = [p["n"] for p in d["plans"] if p["n"] not in MISE_EN_SCENE]
    if manquants:
        print("  ATTENTION, plans sans mise en scene : %s" % manquants)
    out = os.path.join(RACINE, "scenes", "production-%s.html" % a.scene.split("-")[0])
    io.open(out, "w", encoding="utf-8", newline="").write(html(d, a.scene))
    print("  %d plans  ->  scenes/%s" % (len(d["plans"]), os.path.basename(out)))


if __name__ == "__main__":
    main()
