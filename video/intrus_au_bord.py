# -*- coding: utf-8 -*-
"""Quelqu'un est-il entre par le bord du cadre pendant la prise ?

    python video/intrus_au_bord.py video/episode-03-*/_essai-avatar/*.mp4

POURQUOI UNE MESURE DE PLUS, alors que verifier_prise.py existe.

verifier_prise.py decoupe l'image en 8 x 14 et signale toute case qui
s'allume tard. Il SUR-SIGNALE volontairement -- c'est ecrit dans sa fiche :
il localise, il ne juge pas. Passe sur les onze prises de l'episode 3, il
rend entre 24 et 80 cases suspectes POUR CHACUNE. Un classement ou tout le
monde est premier ne classe rien.

Ce qu'on cherche est plus etroit et se mesure : une silhouette qui ENTRE PAR
UN BORD. Le personnage, lui, vit au centre -- il bouge la tete, il gesticule,
et c'est normal. On compare donc la premiere et la derniere image UNIQUEMENT
sur les bandes de bord, la ou rien ne devrait changer.

⚠️ CE QUE CA NE VOIT PAS. Un intrus qui entre et ressort avant la fin, ou qui
   apparait au centre derriere le personnage. La mesure est faite pour le cas
   observe le 16 septembre 2026 -- une silhouette sombre entree par la droite
   au plan 16, invisible sur l'image maitresse et sur la premiere image.
"""
import argparse
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageChops, ImageStat

sys.stdout.reconfigure(encoding="utf-8")

PART = 0.16          # largeur de chaque bande de bord, en fraction du cadre


def image_a(clip, t, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", clip,
                    "-frames:v", "1", dst, "-y"], check=True)
    return Image.open(dst).convert("L")


def duree(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", clip],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def bande(img, cote):
    L, H = img.size
    w = int(L * PART)
    return img.crop((0, 0, w, H)) if cote == "g" else img.crop((L - w, 0, L, H))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clips", nargs="+")
    p.add_argument("--seuil", type=float, default=9.0,
                   help="ecart moyen au-dela duquel on signale")
    a = p.parse_args()

    tmp = tempfile.mkdtemp()
    print("  plan                     bord gauche   bord droit")
    print("  " + "-" * 56)
    suspects = []
    for c in a.clips:
        d = duree(c)
        d0 = image_a(c, 0.05, os.path.join(tmp, "a.png"))
        d1 = image_a(c, max(0.05, d - 0.12), os.path.join(tmp, "b.png"))
        vals = {}
        for cote in ("g", "d"):
            # ⚠️ ON NE MESURE PAS LE CHANGEMENT, ON MESURE L ASSOMBRISSEMENT.
            #    Premiere version : la difference absolue entre la premiere et
            #    la derniere image. Etalonnee sur les onze prises du 16 sept.
            #    2026, elle signalait TOUT -- et sur les quatre plus forts
            #    ecarts, UN SEUL etait un intrus. Les trois autres etaient
            #    Mark lui-meme, qui bouge dans la bande de bord parce que le
            #    plan est serre. Une metrique qui classe le personnage avec
            #    l intrus n arbitre rien.
            #
            #    Un intrus arrive presque toujours SOMBRE sur un fond clair --
            #    une silhouette, un manteau, une nuque contre du trottoir. Le
            #    personnage, lui, occupe deja sa place : il la quitte aussi
            #    souvent qu il l envahit. On ne compte donc que ce qui
            #    S ASSOMBRIT, et la dissymetrie fait le tri.
            av, ap = bande(d0, cote), bande(d1, cote)
            noirci = ImageChops.subtract(av, ap)
            vals[cote] = ImageStat.Stat(noirci).mean[0]
        marque = ""
        if max(vals.values()) >= a.seuil:
            marque = "  <-- quelque chose est entre"
            suspects.append((os.path.basename(c), vals))
        print("  %-24s %8.1f     %8.1f%s"
              % (os.path.basename(c)[:24], vals["g"], vals["d"], marque))

    print("  " + "-" * 56)
    if suspects:
        print("  %d prise(s) a regarder : le bord a change entre la premiere\n"
              "  et la derniere image, la ou le personnage ne va pas."
              % len(suspects))
    else:
        print("  aucun bord n'a bouge au-dela de %.1f." % a.seuil)


if __name__ == "__main__":
    main()
