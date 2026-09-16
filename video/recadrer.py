# -*- coding: utf-8 -*-
"""Resserrer un plan moyen en tete et epaules, sans repasser par le modele.

    python video/recadrer.py <clip.mp4>
    python video/recadrer.py <clip.mp4> --zone 619x1100+230+40

POURQUOI. Le 16 septembre 2026, apres une demi-journee de reprises payantes,
un fait s'est impose en comptant les defauts plan par plan :

    plans SERRES (tete et epaules)  08, 10, 16   aucun objet invente, jamais
    plans MOYENS (comptoir visible) 04 07 09 13 15 17   feuilles, mains,
                                                        silhouettes

Le comptoir et les mains sont exactement l'endroit ou le modele invente. Tant
qu'ils sont dans le cadre, chaque generation est un tirage a 0,70 $. Le prompt
reduit le risque ; LE CADRAGE LE SUPPRIME -- ce qui n'est pas dans l'image ne
peut pas y apparaitre.

Jacques, ce jour-la : << une feuille qui apparait, ce n'est pas realiste ; il
n'y a pas de magie dans le comportement humain >>. Il avait raison, et la
reponse la moins chere n'etait pas un meilleur prompt : c'etait de retirer du
cadre la zone ou la magie se produit.

⚠️ CE QU'IL FAUT VERIFIER AVANT DE RECADRER. Le bas du cadre ne doit rien
   porter d'utile. Le plan 13 garde son comptoir -- la feuille tendue EST le
   plan -- et le 14 aussi, Mark y regarde le formulaire dans sa main. Un
   recadrage qui coupe l'action est pire qu'un objet invente.

⚠️ ET LE PRIX A PAYER : on agrandit 1,76 fois. Sur un visage doux c'est
   invisible ; sur du texte ou une arete franche, ca se verrait. Regarder.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

# Le cadrage tete-et-epaules du fonctionnaire, etabli a l'oeil sur le plan 17
# et valable pour les quatre plans qui partent de beamter-moyen (07, 09, 15,
# 17) : ils ont la meme image de depart, donc la meme position de visage.
ZONE_BEAMTER = "619x1100+230+40"


def ffmpeg(args):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y"] + args,
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit("  ffmpeg a echoue :\n  " + (r.stderr or "")[-600:])


def recadrer(clip, large, haut, x, y):
    base = os.path.splitext(clip)[0]
    garde = base + "-AVANT-recadrage.mp4"
    if not os.path.exists(garde):
        shutil.copy2(clip, garde)
        print("  prise d'origine gardee : %s" % os.path.basename(garde))

    # 9:16 exact en sortie, comme tous les plans de la serie.
    sortie = base + "-serre.mp4"
    ffmpeg(["-i", clip, "-vf",
            "crop=%d:%d:%d:%d,scale=1088:1920:flags=lanczos" % (large, haut, x, y),
            "-c:a", "copy", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
            "-pix_fmt", "yuv420p", sortie])
    os.replace(sortie, clip)
    print("  %s : %dx%d en (%d,%d) -> 1088x1920  (agrandi %.2f fois)"
          % (os.path.basename(clip), large, haut, x, y, 1088.0 / large))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clip")
    p.add_argument("--zone", default=ZONE_BEAMTER,
                   help="LxH+X+Y ; defaut = le cadrage du fonctionnaire")
    a = p.parse_args()
    if not os.path.exists(a.clip):
        sys.exit("  introuvable : %s" % a.clip)
    m = re.match(r"^(\d+)x(\d+)\+(\d+)\+(\d+)$", a.zone)
    if not m:
        sys.exit("  --zone attend LxH+X+Y")
    large, haut, x, y = (int(g) for g in m.groups())
    if abs(large / float(haut) - 9.0 / 16.0) > 0.02:
        print("  ⚠️ la zone n'est pas en 9:16 (%.3f) -- l'image sera deformee"
              % (large / float(haut)))
    recadrer(a.clip, large, haut, x, y)


if __name__ == "__main__":
    main()
