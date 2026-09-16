# -*- coding: utf-8 -*-
"""Poser l'Ampelmaennchen IMAGE PAR IMAGE, en suivant le feu.

    python video/ampelmann_suivi.py --clip plan17.mp4 --fenetre 362,262,422,328 \\
        --sortie plan17-ampel.mp4

POURQUOI PAS UN CALQUE FIXE.

ampelmann_clip.py pose un rectangle unique sur toute la duree, et il REFUSE si
la zone bouge. Sur les quatre plans de l'episode 3, il a refuse les quatre :
le feu se deplace de 6 a 37 points entre la premiere et la derniere image.

Le refus etait juste -- verifie a l'oeil, tout le boitier glisse. Seedance
refabrique chaque image et la geometrie flotte de quelques pixels. Un calque
fixe se detacherait, exactement comme la rustine du plan 17 de l'episode 2 :
<< c'est comme une image par-dessus l'autre >>.

CE QUE FAIT CELUI-CI : il cherche la lampe rouge dans CHAQUE image, a partir
de la position trouvee dans la precedente, et redessine le bonhomme la ou elle
est. Le calque ne peut plus se detacher, puisqu'il n'y a plus de calque.

⚠️ ET LA FENETRE SUIT, ELLE N'EST PAS FIXE NON PLUS. On repart du centre
   precedent avec une marge : si le feu derive de deux pixels par image, une
   fenetre fixe finirait a cote au bout de cent images.

⚠️ SI UNE IMAGE PERD LA LAMPE, ON GARDE LA DERNIERE POSITION CONNUE plutot
   que de sauter. Une image sans bonhomme au milieu d'un plan se voit
   beaucoup plus qu'un bonhomme a deux pixels pres.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import ampelmann as A                                      # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def ips(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=r_frame_rate", "-of",
                        "csv=p=0", clip], capture_output=True, text=True)
    a, _, b = r.stdout.strip().partition("/")
    return float(a) / float(b or 1)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--clip", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--fenetre", required=True, help="x0,y0,x1,y1 sur la 1re image")
    p.add_argument("--flou", type=float, default=1.1)
    p.add_argument("--part", type=float, default=0.84)
    p.add_argument("--marge", type=int, default=18,
                   help="de combien la fenetre suit autour du centre precedent")
    a = p.parse_args()

    tmp = tempfile.mkdtemp()
    brut = os.path.join(tmp, "b")
    os.makedirs(brut)
    subprocess.run(["ffmpeg", "-v", "error", "-i", a.clip,
                    os.path.join(brut, "%05d.png")], check=True)
    images = sorted(os.listdir(brut))
    print("  %d images a traiter" % len(images))

    fen = [int(v) for v in a.fenetre.split(",")]
    dernier = None
    perdues = 0
    for k, nom in enumerate(images):
        f = os.path.join(brut, nom)
        im = Image.open(f).convert("RGB")
        try:
            cx, cy, r = A.trouver_lentille(im, tuple(fen))
            dernier = (cx, cy, r)
        except SystemExit:
            # ⚠️ ON GARDE LA DERNIERE POSITION plutot que de sauter l'image :
            #    un trou au milieu d'un plan se voit bien plus qu'un bonhomme
            #    a deux pixels pres.
            if dernier is None:
                sys.exit("  la lampe est introuvable des la premiere image.\n"
                         "  Verifier --fenetre.")
            cx, cy, r = dernier
            perdues += 1
        m = a.marge
        fen = [max(0, cx - r - m), max(0, cy - r - m),
               min(im.size[0], cx + r + m), min(im.size[1], cy + r + m)]
        A.sa_lumiere(im, "rouge", (cx, cy), r, None,
                     flou=a.flou, part=a.part)
        im.save(f)
        if k % 25 == 0:
            print("    image %4d   lampe a %d,%d  rayon %d" % (k, cx, cy, r))

    print("  %d image(s) ou la lampe n'a pas ete retrouvee" % perdues)
    subprocess.run(["ffmpeg", "-v", "error", "-framerate", "%.6f" % ips(a.clip),
                    "-i", os.path.join(brut, "%05d.png"), "-i", a.clip,
                    "-map", "0:v", "-map", "1:a?", "-c:v", "libx264",
                    "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    a.sortie, "-y"], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print("  -> %s" % a.sortie)


if __name__ == "__main__":
    main()
