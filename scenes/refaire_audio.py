# -*- coding: utf-8 -*-
"""La feuille de re-tournage AVEC LA VOIX EN REFERENCE.

    python scenes/refaire_audio.py --scene 01-ankunft-berlin

CE QUI CHANGE PAR RAPPORT A refaire.py
    L'ancienne feuille demandait a Seedance d'inventer une articulation, qu'on
    payait ensuite sync.so pour repeindre. Le 9 septembre 2026 la mesure a
    montre que ca ne pouvait pas marcher : le lip-sync repeint les levres mais
    ne retime pas la machoire, et la machoire battait sa propre mesure --
    correlation nulle ou negative sur la moitie des plans, dans le clip brut
    comme dans le synchronise.

    Seedance 2.0 accepte une PISTE AUDIO EN REFERENCE et fabrique la bouche a
    partir d'elle, dans la meme passe que l'image. C'etait ecrit dans sa fiche
    Artlist depuis le debut. Il n'y a plus d'etape de lip-sync.

DEUX FICHIERS A TELEVERSER, PAS UN
    @img1  l'image de depart, comme avant
    @aud1  la piste de voix, construite par ce script

    Attention : en mode reference, l'image N'EST PLUS la premiere image du
    clip. Elle decrit ce qu'on veut voir, elle ne l'impose pas.

LA LECON QUI A COUTE UNE GENERATION -- NE PAS DECRIRE LE CADRAGE EN MOTS
    Premier essai, le prompt disait « close shot, head and shoulders, face
    filling the upper half of the frame » ET « frame him exactly as in @img1 ».
    Les deux consignes se sont disputees, le modele a suivi les mots, et le
    plan est revenu bien plus serre que la photo : 15,9 dB de ressemblance.

    Jacques : « n'aurait-on pas pu lui dire de faire le cadrage a meme
    l'image ? ». On a retire toute description de taille de plan et laisse
    @img1 parler seule : 29,5 dB -- mieux que le mode image de depart
    lui-meme, qui donnait 27,1.

    Aucune phrase de ce fichier ne decrit donc une taille de plan.

CE QUI RESTE OUVERT
    La qualite du calage. La mesure de video/controler_bouche.py donne au
    premier essai 0,26 contre 0,44 pour sync.so -- moins bon. Mais cette
    mesure s'est trompee trois fois dans la journee la ou l'oeil de Jacques
    avait raison, et elle porte sur une replique de 1,1 s, soit 27 images.
    Elle ne tranche pas. C'est l'oeil qui tranche, sur les clips cote a cote.
"""
import argparse
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "scenes"))
sys.path.insert(0, os.path.join(RACINE, "video"))
import production as P                                      # noqa: E402
import montage as M                                         # noqa: E402

FENETRE = 0.5          # le silence d'amorce, en tete de la piste de reference

# CE QUI DOIT RESTER DANS LE CADRE, PAR TAILLE DE PLAN.
#
# 9 septembre 2026, plan 05 : sans un mot sur le cadrage, Seedance est revenu
# en gros plan sur un plan MOYEN -- 18 dB, sous le seuil. Le reflexe du modele
# pour une tete parlante est le gros plan, et rien ne l'en empechait.
#
# Ca n'avait pas gene au plan 16 parce que le plan 16 EST un gros plan : la
# derive etait invisible. Un seul plan valide ne valide pas une recette.
#
# On ne redecrit pas la TAILLE -- c'est ce qui avait tout casse au premier
# essai, les mots l'emportant sur l'image. On nomme ce qui doit rester VISIBLE,
# ce qui se verifie dans @img1 au lieu de le concurrencer.
VISIBLE = {
    "moyen": ("The person is seen from the waist up, and the front edge of "
              "the information desk crosses the lower part of the frame. Both "
              "stay visible for the whole clip."),
    "moyen serre": ("The person is seen from the chest up, with the top of "
                    "the information desk still in the lower part of the "
                    "frame."),
    "serre": "The person is seen head and shoulders.",
}
PAS_DE_ZOOM = ("Do not push in at any point. The shot stays exactly as wide "
               "as @img1 from the first frame to the last.")

# LA DIRECTION DU REGARD, ET POURQUOI ELLE DOIT ETRE ECRITE.
#
# En retirant toute description du cadrage -- ce qui a repare la derive -- on a
# retire le regard avec. Le 9 septembre 2026, Jacques : « meme la derniere,
# Mark ne regarde plus dans la bonne direction ».
#
# Ce n'est pas un detail de rendu : c'est le champ-contrechamp. Mark regarde
# vers la GAUCHE du cadre, Anna vers la DROITE ; s'ils regardent du meme cote,
# ils ne se parlent plus, ils parlent chacun dans le vide, et la scene ne tient
# plus. Deux personnages qui dialoguent doivent se regarder A TRAVERS l'axe.
#
# Une direction n'est pas une taille de plan : elle decrit ce qui se passe dans
# l'image, pas comment la cadrer. Elle ne concurrence donc pas @img1.
REGARD = {
    "mark": ("He is placed right of centre and looks toward the LEFT of the "
             "frame, at the person he is talking to, off screen. He keeps "
             "looking that way for the whole clip - he never turns to face the "
             "camera."),
    "anna": ("She is placed left of centre and looks toward the RIGHT of the "
             "frame, at the person she is talking to, off screen. She keeps "
             "looking that way for the whole clip - she never turns to face "
             "the camera."),
}


def piste(F, scene, p, duree, dossiers):
    """Construit la piste de reference : silence, la voix nue, silence.

    Le silence d'origine du mp3 est retire aux deux bouts -- c'est le defaut
    du 9 septembre, ou la duree du FICHIER servait de fenetre de parole alors
    qu'un mp3 porte 0,29 s de silence en moyenne (2,33 s sur le plan 13).
    """
    src = os.path.join(RACINE, "audio", "scenes", scene,
                       "%02d-%s.mp3" % (p["n"], p["locuteur"]))
    tete, queue, _ = M.parole(F, src)
    nom = "%02d-%s-%gs.mp3" % (p["n"], p["locuteur"], duree)
    for d in dossiers:
        os.makedirs(d, exist_ok=True)
        subprocess.run([F, "-y", "-v", "error", "-ss", "%.3f" % tete,
                        "-to", "%.3f" % queue, "-i", src,
                        "-af", "adelay=%d:all=1,apad" % int(round(FENETRE * 1000)),
                        "-t", "%.3f" % duree, "-ar", "44100", "-ac", "1",
                        "-b:a", "128k", os.path.join(d, nom)], check=True)
    return nom, FENETRE, FENETRE + (queue - tete)


def prompt(m, p, debut, fin, duree, jeu=True):
    """Le prompt du mode reference. Le mouvement de camera, l'action, le
    minutage -- et PAS UN MOT sur la taille du plan.

    `jeu` porte la DERNIERE ligne, celle qui dirige l'interpretation (« a
    slight forward lean, eyebrows raised in question »). Voir --sans-jeu.
    """
    bloc = []
    bloc.append(
        "Use @img1 as the exact framing for this shot: match its composition, "
        "the position of the person in the frame and their distance from the "
        "camera, precisely as they are in @img1. Do not reframe, do not crop "
        "in, do not move closer.")
    bloc.append(
        "The person is the one in @img1 - same face, same clothes, same "
        "airport setting behind them.")
    bloc.append(REGARD[m["pose"]])
    bloc.append(VISIBLE[m["taille"]] + ("" if m.get("zoom") else " " + PAS_DE_ZOOM))
    bloc.append(P.ZOOM if m.get("zoom") else P.FIXE)
    # ⚠️ LE TEXTE EST OBLIGATOIRE. On l'avait retire le 9 septembre parce que
    # le modele bafouillait sur un mot -- « ihrere Hilfe » au lieu de « Ihre
    # Hilfe » -- en croyant que le texte ecrit et @aud1 se disputaient.
    #
    # Sans le texte, c'est bien pire : Seedance doit deviner les mots au son
    # seul. Au plan 14 il attrape « Wie lange dauert... » puis decroche et
    # invente -- Jacques : « il dit quelque chose comme eine findungdung ». Et
    # les levres suivent le charabia, puisque voix et bouche naissent ensemble.
    #
    # La mesure de l'etirement ne voyait rien : elle compte la DUREE de
    # l'articulation, pas les mots. 1,42 s contre 1,47 -- juste, et faux.
    #
    # Le texte donne les MOTS, @aud1 donne le RYTHME. Les deux, chacun son
    # role nomme.
    bloc.append("They say, in German: \"%s\"" % p["de"])
    bloc.append(
        "@aud1 is a recording of exactly that sentence. Take the timing of "
        "every syllable from @aud1. Do not add, repeat, stretch or hesitate "
        "on any syllable, and do not say anything that is not in that "
        "sentence. Their mouth follows @aud1.")
    bloc.append(
        "Total clip duration: %d seconds. Their mouth is closed from 0 to "
        "%.1f seconds. They speak from %.1f to %.1f seconds. From %.1f "
        "seconds to the end of the clip the mouth closes and stays closed - "
        "it does not open again."
        % (duree, debut, debut, fin, fin))
    # ⚠️ LA SEULE LIGNE DE CE PROMPT QU'ON PUISSE VRAIMENT DISCUTER (v. --sans-jeu).
    #
    # Les praticiens designent la sur-direction comme la premiere cause de
    # mauvais lip-sync : « most bad lip sync comes from giving it too many
    # performance notes, not too few ». Toutes les autres lignes d'ici ont ete
    # gagnees par une mesure -- le cadrage a 29,5 dB contre 15,9, le regard
    # rendu apres l'avoir perdu, le texte remis apres le charabia du plan 14,
    # ce qui doit rester VISIBLE apres la derive du plan 05. Celle-ci, non :
    # elle dirige le JEU, et c'est exactement ce que le reproche vise.
    #
    # On ne la retire donc pas d'office -- on la rend commutable, pour la
    # juger sur un plan a la fois. Changer trois choses ensemble est ce qu'on
    # a fait toute la journee du 9 septembre, et c'est ce que toutes les
    # sources deconseillent.
    if jeu:
        bloc.append(m["action"])
    return "\n\n".join(bloc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--plans", help="5,6,8... par defaut tous les parlants")
    ap.add_argument("--sans-jeu", action="store_true",
                    help="retirer la ligne de direction d'acteur, celle que "
                         "les praticiens designent comme la premiere cause de "
                         "mauvais lip-sync. A essayer sur UN plan.")
    a = ap.parse_args()

    F = M.ffmpeg()
    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    dim = os.path.join(ep, "01-images")
    dossiers = [os.path.join(RACINE, "audio", "scenes", a.scene,
                             "reference-seedance"), dim]

    voulus = ({int(x) for x in a.plans.replace(" ", "").split(",") if x}
              if a.plans else
              {n for n, m in P.MISE_EN_SCENE.items() if "pose" in m})
    plans = [p for p in d["plans"] if p["n"] in voulus]

    # Les images de depart : la meme distribution des variantes que refaire.py.
    import refaire as R
    servi = {}
    for p in plans:
        m = P.MISE_EN_SCENE[p["n"]]
        cle = (m["pose"], m["taille"])
        dispo = R.images(dim, *cle)
        rang = servi.setdefault(cle, 0)
        p["_image"] = dispo[rang] if rang < len(dispo) else (dispo[0] if dispo else "(aucune)")
        servi[cle] = rang + 1

    nl = chr(10)
    o = ["RE-TOURNAGE AVEC LA VOIX EN REFERENCE -- %s" % d["situation"],
         "=" * 66, "",
         "%d plans. Plus de lip-sync : la bouche naît de la voix, dans la"
         " meme passe" % len(plans),
         "que l'image.", "",
         "DANS ARTLIST, POUR CHAQUE PLAN",
         "  1. Video, modele Seedance 2.0 Mini, 9:16, 720p, la duree indiquee.",
         "  2. Audio : On.  Unlimited : eteint (le mode reference se paie).",
         "  3. + -> Image Reference : l'image nommee ci-dessous.",
         "  4. + -> Audio File      : la piste nommee ci-dessous.",
         "     Les deux vivent dans video/episode-%s/01-images/." % a.scene,
         "  5. Verifier que les etiquettes sont bien @img1 et @aud1.",
         "  6. Coller le prompt tel quel. Generer. Telecharger.",
         "  7. python video/rapatrier.py --plan N", "",
         "⚠️ L'IMAGE N'EST PLUS LA PREMIERE IMAGE DU CLIP. En mode reference",
         "elle decrit le cadrage, elle ne l'impose pas. verifier_prises.py le",
         "verra : viser au-dessus de 25 dB, sous 21 le plan est a refaire.", "",
         "⚠️ NE RIEN AJOUTER SUR LA TAILLE DU PLAN. Une description ecrite",
         "entre en concurrence avec @img1 et le modele suit les mots -- 15,9 dB",
         "au premier essai, 29,5 dB une fois les mots retires.", ""]

    # ⚠️ LA VOIX DOIT DIRE CE QUE LA FEUILLE ANNONCE (10 septembre 2026).
    #
    # Le plan 13 a ete coupe en deux. La feuille annoncait donc « Nehmen Sie
    # die S-Bahn. » -- une seconde et demie -- au-dessus d'une piste @aud1 qui
    # portait encore les DEUX phrases et 4,6 s de parole, et d'une fenetre de
    # bouche calculee dessus. Rien ne s'en plaignait : le mp3 existe, il se
    # mesure, tout est coherent sauf le sens.
    #
    # Deux cents credits pour un plan qui articule une phrase qu'on n'a plus.
    # manifeste.json garde le texte AVEC lequel chaque mp3 a ete fabrique :
    # on compare, et on refuse.
    fm = os.path.join(RACINE, "audio", "scenes", a.scene, "manifeste.json")
    dit = {}
    if os.path.exists(fm):
        dit = {x["plan"]: x.get("de", "") for x in
               json.load(io.open(fm, encoding="utf-8")).get("plans", [])}
    # Un plan neuf n'a pas encore de voix du tout : c'est le meme probleme --
    # une feuille qui nomme un @aud1 introuvable -- et il vaut mieux le dire
    # ici que laisser ffmpeg echouer trois ecrans plus bas.
    def voix_de(p):
        f = os.path.join(RACINE, "audio", "scenes", a.scene,
                         "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(f):
            return None
        return dit.get(p["n"], p["de"])

    perimes = [p for p in plans if voix_de(p) != p["de"]]
    if perimes:
        print("  LA VOIX NE DIT PLUS LE TEXTE DE LA SCENE :")
        for p in perimes:
            print("    plan %02d" % p["n"])
            print("      scene : %s" % p["de"])
            print("      voix  : %s" % (voix_de(p) or "(aucune)"))
        print("  Refaire ces voix avant de tourner :")
        for p in perimes:
            print("    python audio/refaire_plan.py --plan %d --pour-de-vrai" % p["n"])
        sys.exit("  Aucune feuille ecrite.")

    # ⚠️ LE SEUIL DE 2,2 s, ET POURQUOI IL DOIT SE VOIR SUR LA FEUILLE.
    #
    # production.duree_a_generer le dit dans son propre docstring : « ce
    # qu'aucune duree ne sauve, c'est une replique de plus de 2,2 s environ.
    # Les deux seules qui depassent ce seuil se sont etirees, a des rapports
    # pourtant differents. »
    #
    # La regle x3,5 continue pourtant de rendre une duree, sans un mot. Le 10
    # septembre, apres avoir coupe le plan 13 en deux, la seconde moitie
    # faisait encore 3,13 s de parole : la feuille annoncait ONZE secondes a
    # generer -- a 120 credits la seconde en mode reference, 1 320 credits sur
    # un plan que notre propre mesure dit a risque.
    #
    # Une feuille qui coute ca doit le dire avant, pas apres.
    longues = [(p, P.duree_voix(p, a.scene)) for p in plans
               if P.duree_voix(p, a.scene) > 2.2]
    if longues:
        print("  ⚠️ AU-DESSUS DU SEUIL DE 2,2 s -- nos deux seules repliques plus")
        print("     longues se sont ETIREES, a des rapports differents :")
        for p, v in longues:
            print("       plan %02d  %.2f s de parole  ->  %d s a generer"
                  % (p["n"], v, P.duree_a_generer(p, a.scene)))
        print("     Couper la replique, ou la passer en voix off sur un plan")
        print("     sans visage : aucune duree de clip ne les sauve.")
        print("")

    for p in plans:
        m = P.MISE_EN_SCENE[p["n"]]
        duree = P.duree_a_generer(p, a.scene)
        nom, deb, fin = piste(F, a.scene, p, float(duree), dossiers)
        o.append("-" * 66)
        o.append("PLAN %02d   %s   GENERER A %d SECONDES%s"
                 % (p["n"], p["locuteur"], duree,
                    "   (zoom)" if m.get("zoom") else ""))
        o.append("  << %s >>" % p["de"])
        o.append("  @img1 : %s" % p["_image"])
        o.append("  @aud1 : %s   (parole de %.1f a %.1f s)" % (nom, deb, fin))
        o.append("")
        o.append(prompt(m, p, deb, fin, duree, jeu=not a.sans_jeu))
        o.append("")

    out = os.path.join(ep, "A-REFAIRE-AUDIO.txt")
    io.open(out, "w", encoding="utf-8", newline=nl).write(nl.join(o) + nl)
    print("  %d plans  ->  %s" % (len(plans), os.path.relpath(out, RACINE)))
    print("  Les pistes de reference sont ecrites dans les deux dossiers.")


if __name__ == "__main__":
    main()
