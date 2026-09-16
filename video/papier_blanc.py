# -*- coding: utf-8 -*-
"""Rendre blanc le formulaire jaune, pour que le raccord tienne.

    python video/papier_blanc.py <clip.mp4>
    python video/papier_blanc.py <clip.mp4> --essai 3.8   (une image, sans rien ecrire)

POURQUOI.

Jacques, 16 septembre 2026 : << il lui donne un papier jaune ; dans la rue, on
voit qu'il a un papier blanc. Dependant des sequences, le papier est blanc ou
jaune. C'est grandement bizarre. >>

Il a raison, et c'est un vrai raccord, pas un detail : un objet qui change de
couleur d'un plan a l'autre casse la croyance plus surement qu'un defaut
technique. Le spectateur ne se dit pas << tiens, une incoherence >> : il se dit
que ce n'est pas le meme papier, donc que l'histoire lui echappe.

⚠️ C'EST LE JAUNE QUI CEDE, ET LE CHOIX EST DICTE PAR LE COUT. Le papier est
   jaune dans deux plans d'avatar (13 et 17, ou il est tendu et pris) et blanc
   dans les plans de DECOR du couloir et de la rue (18, 19). Les decors sont
   des clips generes a partir d'images : les refaire en jaune coute une
   generation par plan, plus l'image. Repeindre le jaune en blanc, ici, ne
   coute rien -- et un formulaire d'Anmeldung est blanc dans la vraie vie.

COMMENT.

Le jaune de ce papier a une signature simple : rouge et vert eleves, bleu
nettement plus bas. On releve le bleu a la moyenne des deux autres, ce qui
ramene le pixel vers le blanc, et SEULEMENT la.

⚠️ LE SEUIL EPARGNE LE BOIS DU COMPTOIR, et c'est tout l'enjeu du reglage. Le
   comptoir est jaune-brun : rouge haut, vert moyen, bleu bas. Sans la
   condition sur le VERT (g > 165), il blanchissait avec le papier -- et un
   comptoir gris au milieu d'un bureau vert se voit bien plus qu'une feuille
   jaune.
"""
import argparse
import os
import shutil
import subprocess
import sys

# r et g hauts, et un ecart net entre le vert et le bleu : c'est du jaune vif,
# pas du bois.
FILTRE = ("format=rgb24,geq=r='r(X,Y)':g='g(X,Y)':"
          "b='if(gt(r(X,Y),175)*gt(g(X,Y),165)*gt(g(X,Y)-b(X,Y),55),"
          "(r(X,Y)+g(X,Y))/2, b(X,Y))'")


def ffmpeg(args):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y"] + args,
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit("  ffmpeg a echoue :\n  " + (r.stderr or "")[-500:])


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clip")
    p.add_argument("--essai", type=float,
                   help="n'ecrire qu'une image PNG a cette seconde, pour voir")
    a = p.parse_args()
    if not os.path.exists(a.clip):
        sys.exit("  introuvable : %s" % a.clip)

    base = os.path.splitext(a.clip)[0]
    if a.essai is not None:
        png = base + "-essai-blanc.png"
        ffmpeg(["-ss", "%.2f" % a.essai, "-i", a.clip, "-vframes", "1",
                "-vf", FILTRE, png])
        print("  image d'essai : %s" % os.path.basename(png))
        return

    garde = base + "-AVANT-blanc.mp4"
    if not os.path.exists(garde):
        shutil.copy2(a.clip, garde)
        print("  prise d'origine gardee : %s" % os.path.basename(garde))
    sortie = base + "-blanc.mp4"
    ffmpeg(["-i", a.clip, "-vf", FILTRE, "-c:a", "copy",
            "-c:v", "libx264", "-crf", "16", "-preset", "slow",
            "-pix_fmt", "yuv420p", sortie])
    os.replace(sortie, a.clip)
    print("  %s : le jaune est devenu blanc" % os.path.basename(a.clip))


if __name__ == "__main__":
    main()
