# -*- coding: utf-8 -*-
"""Poser l'Ampelmaennchen sur un CLIP FINI, pas sur l'image de depart.

    python video/ampelmann_clip.py --clip plan01.mp4 --fenetre 940,530,1110,700 \\
        --verre 1014,750 --sortie plan01-ampel.mp4

POURQUOI SUR LE CLIP ET PAS SUR L'IMAGE.

mouvement.py REFABRIQUE chaque image du clip a partir de l'image de depart.
Un bonhomme incruste en amont serait redessine a chaque image -- donc
deforme, donc pire que pas de bonhomme du tout. C'etait ecrit dans
A-TOURNER.txt des le 16 septembre : << l'incrustation se fait en dernier, sur
ce qui est deja anime >>.

CE QUI REND LA CHOSE POSSIBLE : la camera est verrouillee sur ces plans. Le
feu ne bouge pas d'un pixel du debut a la fin. On peut donc calculer la
lentille UNE FOIS sur la premiere image et poser le meme rectangle sur toutes
les autres.

⚠️ ET L'OUTIL REFUSE SI LE FEU BOUGE. C'est la lecon de la rustine du plan 17
   de l'episode 2 -- Jacques : << c'est comme une image par-dessus l'autre, on
   voit une main qui apparait en dessous >>. Un rectangle colle sur une zone
   qui bouge se voit immediatement. On mesure donc l'ecart entre la premiere
   et la derniere image DANS LA ZONE VISEE, et au-dela d'un seuil on s'arrete
   au lieu de livrer une rustine.
"""
import argparse
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageChops, ImageStat

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import ampelmann as A                                      # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def duree(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", clip],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def image_a(clip, t, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", clip,
                    "-frames:v", "1", dst, "-y"], check=True)
    return Image.open(dst).convert("RGB")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--clip", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--fenetre", required=True,
                   help="x0,y0,x1,y1 ou CHERCHER la lampe rouge")
    p.add_argument("--verre", help="x,y sur la lentille eteinte du meme boitier")
    p.add_argument("--flou", type=float, default=1.3)
    p.add_argument("--part", type=float, default=0.84)
    p.add_argument("--bouge-max", type=float, default=6.0,
                   help="ecart tolere dans la zone entre la premiere et la "
                        "derniere image")
    a = p.parse_args()

    n = lambda s: [int(v) for v in s.split(",")]                  # noqa: E731
    tmp = tempfile.mkdtemp()
    d = duree(a.clip)
    im0 = image_a(a.clip, 0.04, os.path.join(tmp, "a.png"))
    im1 = image_a(a.clip, max(0.04, d - 0.10), os.path.join(tmp, "b.png"))

    cx, cy, r = A.trouver_lentille(im0, n(a.fenetre))
    print("  lentille mesuree : centre %d,%d  rayon %d" % (cx, cy, r))

    # ⚠️ LA ZONE DOIT ETRE IMMOBILE, sinon la rustine se voit.
    d2 = int(r * 1.6)
    boite = (max(0, cx - d2), max(0, cy - d2),
             min(im0.size[0], cx + d2), min(im0.size[1], cy + d2))
    ecart = ImageStat.Stat(ImageChops.difference(
        im0.crop(boite).convert("L"), im1.crop(boite).convert("L"))).mean[0]
    print("  le feu bouge de %.2f entre la premiere et la derniere image "
          "(plafond %.1f)" % (ecart, a.bouge_max))
    if ecart > a.bouge_max:
        sys.exit("  LE FEU BOUGE DANS CE PLAN : une incrustation fixe se "
                 "verrait\n  comme une image posee par-dessus l'autre. On ne "
                 "pose rien.")

    fond = im0.getpixel(tuple(n(a.verre))) if a.verre else None
    corrige = im0.copy()
    A.sa_lumiere(corrige, "rouge", (cx, cy), r, fond, flou=a.flou, part=a.part)

    # Le calque est exactement ce qui a change, plus une marge de fondu.
    bb = ImageChops.difference(im0, corrige).convert("L").getbbox()
    if not bb:
        sys.exit("  rien n'a change : le bonhomme n'a pas ete pose.")
    m = 4
    bb = (max(0, bb[0] - m), max(0, bb[1] - m),
          min(im0.size[0], bb[2] + m), min(im0.size[1], bb[3] + m))
    calque = os.path.join(tmp, "calque.png")
    corrige.crop(bb).save(calque)
    print("  calque %dx%d pose en %d,%d"
          % (bb[2] - bb[0], bb[3] - bb[1], bb[0], bb[1]))

    subprocess.run(["ffmpeg", "-v", "error", "-i", a.clip, "-i", calque,
                    "-filter_complex", "[0:v][1:v]overlay=%d:%d" % (bb[0], bb[1]),
                    "-c:a", "copy", "-c:v", "libx264", "-crf", "18",
                    "-pix_fmt", "yuv420p", a.sortie, "-y"], check=True)
    print("  -> %s" % a.sortie)


if __name__ == "__main__":
    main()
