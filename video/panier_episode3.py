# -*- coding: utf-8 -*-
"""Preparer les paniers d'avatar de l'episode 3 : image + piste.

    python video/panier_episode3.py            # a blanc
    python video/panier_episode3.py --ecrire

POURQUOI UN SCRIPT A PART, ET PAS preparer_avatar.py.

preparer_avatar.py tire la piste d'un clip `04-lipsync/planNN.mp4` DEJA MONTE.
C'etait la chaine des episodes 1 et 2, ou un lipsync existait avant OmniHuman
et servait aussi de ligne de base pour mesurer la synchro.

L'episode 3 n'a pas de lipsync : son audio sort directement d'ElevenLabs,
dans audio/scenes/03-auf-dem-radweg/. Il n'y a donc ni clip a vider, ni base a
mesurer -- et forcer l'ancien outil demanderait de fabriquer un faux clip.

⚠️ LA CONSEQUENCE, ET IL FAUT L'ECRIRE : on perd la LIGNE DE BASE. Aux
   episodes 1 et 2, syncnet.py comparait la prise revenue au lipsync de
   depart. Ici il n'y a rien a comparer : la synchro se juge a l'oeil et a
   l'oreille. C'est une perte reelle, pas un detail d'outillage.

⚠️ LE SILENCE FINAL N'EST PAS DU GASPILLAGE. Mesure sur le plan 16 de
   l'episode 2 : la bouche met environ 1,4 s a redescendre apres le dernier
   mot. Une piste coupee au dernier phoneme fige un visage la bouche ouverte.
   Quelques cents contre une prise a refaire.
"""
import argparse
import json
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

EP = os.path.join(RACINE, "video", "episode-03-auf-dem-radweg")
SCENE = os.path.join(RACINE, "audio", "scenes", "03-auf-dem-radweg")
PRIX = 0.16          # $ la seconde chez OmniHuman 1.5
QUEUE = 1.4          # s de silence final

# ⚠️ LA CORRESPONDANCE SE RELIT, ELLE NE SE SUPPOSE PAS. Un plan servi par la
#    mauvaise image ne rate pas a moitie : il change de cadrage au milieu
#    d'un champ/contrechamp, et ca ne se voit qu'au montage.
#
#    Les cadrages SERRES (05, 13, 14, 15) sont des recadrages des maitresses,
#    faits le 16 sept. 2026. Mes prompts demandaient un gros plan tout en
#    disant << garde la distance exactement comme dans l'image >>, et l'image
#    etait a mi-corps : la consigne se contredisait elle-meme.
PLANS = {
    2:  ("mark-marche",    "mark"),
    # ⚠️ 22 sept. 2026 : dame-feu -> dame-trottoir. dame-feu.png la posait au
    #    bord de la chaussee, une barre de passage pieton sous elle -- une
    #    dame qui sermonne sur le feu rouge depuis la rue detruit sa replique.
    4:  ("dame-trottoir",  "dame"),
    5:  ("mark-serre",     "mark"),
    8:  ("mark-retourne",  "mark"),
    9:  ("cycliste-jaune", "radfahrer"),
    10: ("mark-marche",    "mark"),
    11: ("cycliste-jaune", "radfahrer"),
    13: ("cycliste-serre", "radfahrer"),
    14: ("mark-serre",     "mark"),
    15: ("cycliste-serre", "radfahrer"),
    16: ("mark-marche",    "mark"),
}


def duree(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", f],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--ecrire", action="store_true")
    p.add_argument("--plan", type=int, nargs="+",
                   help="ne refaire que ces paniers ; par defaut, tous")
    a = p.parse_args()
    if a.plan:
        inconnus = [n for n in a.plan if n not in PLANS]
        if inconnus:
            sys.exit("  plan(s) sans replique : %s"
                     % ", ".join(str(n) for n in inconnus))

    tel = os.path.join(EP, "_a-televerser")
    if a.ecrire and not os.path.isdir(tel):
        os.makedirs(tel)

    total = 0.0
    print("  plan  image              piste        parole  +silence   cout")
    print("  " + "-" * 68)
    choisis = sorted(n for n in PLANS if not a.plan or n in a.plan)
    for n in choisis:
        nom_img, loc = PLANS[n]
        src_img = os.path.join(EP, "01-images", nom_img + ".png")
        src_mp3 = os.path.join(SCENE, "%02d-%s.mp3" % (n, loc))
        if not os.path.exists(src_img):
            sys.exit("  plan %02d : image introuvable -- %s" % (n, src_img))
        if not os.path.exists(src_mp3):
            sys.exit("  plan %02d : piste introuvable -- %s" % (n, src_mp3))

        d = duree(src_mp3)
        dt = d + QUEUE
        total += dt
        print("  %02d    %-18s %-12s %5.2f s  %5.2f s  %5.2f $"
              % (n, nom_img, os.path.basename(src_mp3), d, dt, dt * PRIX))

        if not a.ecrire:
            continue
        dst_img = os.path.join(tel, "plan%02d-%s.jpg" % (n, nom_img))
        dst_mp3 = os.path.join(tel, "plan%02d-pleine.mp3" % n)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src_img,
                        "-q:v", "2", dst_img], check=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src_mp3,
                        "-af", "apad=pad_dur=%.2f" % QUEUE,
                        "-ar", "44100", "-ac", "1", "-b:a", "192k",
                        dst_mp3], check=True)

    print("  " + "-" * 68)
    print("  %d plans, %.1f s au total  ->  %.2f $" % (len(choisis), total,
                                                       total * PRIX))
    if not a.ecrire:
        print("\n  Essai a blanc. Relancer avec --ecrire pour fabriquer les "
              "paniers.\n  (Fabriquer un panier ne coute rien ; c'est "
              "omnihuman.py qui facture.)")
    else:
        print("  paniers dans %s" % os.path.relpath(tel, RACINE))


if __name__ == "__main__":
    main()
