# -*- coding: utf-8 -*-
"""Retirer la peinture rouge d'une bande cyclable, sans repasser par fal.

    python video/degriser_bande.py --clip plan18.mp4 --sortie plan18-gris.mp4 \\
        --depuis 0.52 --essai

Jacques, 16 septembre 2026, sur le dernier plan : << est-ce que tu peux enlever
le rouge de la piste cyclable ? C'est une traverse de pietons. Est-ce que tu
peux le faire sans repasser a FAL ? >>

⚠️ ON NE PEINT PAS UNE FORME PAR-DESSUS. Ce serait une rustine, et il y a du
   MONDE devant la bande : les jambes de Mark, le cycliste, son velo. Un
   rectangle gris passerait sur eux.

   On travaille donc PAR LA COULEUR, pas par la geometrie : on ne touche que
   les pixels franchement rouges. Tout ce qui ne l'est pas -- un pantalon
   beige, un polo bleu, un blouson jaune, un pneu noir -- est protege sans
   qu'on ait a le detourer. C'est le contraire d'un masque : c'est la matiere
   qui se designe elle-meme.

⚠️ ET ON GARDE LA LUMINOSITE DE CHAQUE PIXEL. Un aplat gris effacerait les
   joints, l'usure, les ombres, et se verrait comme une tache. On remplace
   donc la TEINTE en conservant la clarte : ce qui etait un rouge sombre
   devient un gris sombre, ce qui etait un rouge clair devient un gris clair.
   Le revetement garde sa vie.

⚠️ ET LE FEU EST ROUGE, LUI AUSSI. D'ou --depuis : on ne travaille qu'en
   dessous d'une certaine hauteur. Sans ca on eteindrait la lampe, qui est
   precisement ce que le plan raconte.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")


def ips(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=r_frame_rate", "-of",
                        "csv=p=0", clip], capture_output=True, text=True)
    a, _, b = r.stdout.strip().partition("/")
    return float(a) / float(b or 1)


def degriser(im, y0, ecart, teinte, force, zones=()):
    """Remplace le rouge par un gris DE MEME CLARTE, sous la ligne y0."""
    px = im.load()
    L, H = im.size
    n = 0
    for y in range(y0, H):
        for x in range(L):
            r, v, b = px[x, y]
            if any(zx0 <= x < zx1 and zy0 <= y < zy1
                   for zx0, zy0, zx1, zy1 in zones):
                continue
            if r - v > ecart and r - b > ecart:
                # La clarte du pixel, pesee comme l'oeil la percoit.
                c = 0.299 * r + 0.587 * v + 0.114 * b
                # Un asphalte n'est pas neutre : il tire legerement au bleu.
                g = (int(min(255, c * teinte[0])),
                     int(min(255, c * teinte[1])),
                     int(min(255, c * teinte[2])))
                if force < 1.0:
                    g = tuple(int(o + (n2 - o) * force)
                              for o, n2 in zip((r, v, b), g))
                px[x, y] = g
                n += 1
    return n


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--clip", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--depuis", type=float, default=0.5,
                   help="fraction de la hauteur sous laquelle on travaille ; "
                        "au-dessus, on ne touche a rien -- le feu est rouge")
    p.add_argument("--ecart", type=int, default=26,
                   help="de combien le rouge doit depasser les deux autres "
                        "canaux pour etre pris pour de la peinture")
    # ⚠️ LE GRIS SE MESURE DANS L IMAGE, IL NE SE DEVINE PAS. La premiere
    #    valeur -- 1.02,1.04,1.06 -- mettait le vert et le bleu AU-DESSUS du
    #    rouge : elle fabriquait un gris verdatre, et Jacques l a vu tout de
    #    suite. L asphalte reel du plan 18 est (164,152,159), dont la clarte
    #    vaut 156 : les facteurs justes sont donc 1.05, 0.97, 1.02 -- le rouge
    #    LEGEREMENT au-dessus, le vert en dessous.
    p.add_argument("--teinte", default="1.05,0.97,1.02",
                   help="le gris vise, en facteurs de clarte (r,v,b)")
    p.add_argument("--protege", action="append", default=[],
                   metavar="X0,Y0,X1,Y1",
                   help="une zone a ne JAMAIS toucher. Repetable. La peau a "
                        "le meme ecart rouge/vert que la peinture -- 50 contre "
                        "51, mesure -- donc aucun seuil ne les separe : il "
                        "faut proteger la personne par sa position.")
    p.add_argument("--force", type=float, default=1.0)
    p.add_argument("--essai", action="store_true",
                   help="ne traiter que trois images, pour juger avant de "
                        "lancer tout le clip")
    a = p.parse_args()

    teinte = [float(v) for v in a.teinte.split(",")]
    zones = [tuple(int(v) for v in z.split(",")) for z in a.protege]
    tmp = tempfile.mkdtemp()
    brut = os.path.join(tmp, "b")
    os.makedirs(brut)

    if a.essai:
        for i, t in enumerate((0.2, 2.0, 3.9)):
            d = os.path.join(brut, "%05d.png" % (i + 1))
            subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i",
                            a.clip, "-frames:v", "1", d, "-y"], check=True)
    else:
        subprocess.run(["ffmpeg", "-v", "error", "-i", a.clip,
                        os.path.join(brut, "%05d.png")], check=True)

    images = sorted(os.listdir(brut))
    total = 0
    for k, nom in enumerate(images):
        f = os.path.join(brut, nom)
        im = Image.open(f).convert("RGB")
        y0 = int(im.size[1] * a.depuis)
        total += degriser(im, y0, a.ecart, teinte, a.force, zones)
        im.save(f)
        if not a.essai and k % 25 == 0:
            print("    image %4d" % k)
    print("  %d px repeints sur %d image(s) (%.0f par image)"
          % (total, len(images), total / float(len(images))))

    if a.essai:
        planche = Image.new("RGB", (240 * len(images), 427))
        for i, nom in enumerate(images):
            planche.paste(Image.open(os.path.join(brut, nom))
                          .resize((240, 427), Image.LANCZOS), (240 * i, 0))
        planche.save(a.sortie)
        print("  planche d'essai : %s" % a.sortie)
    else:
        subprocess.run(["ffmpeg", "-v", "error", "-framerate",
                        "%.6f" % ips(a.clip), "-i",
                        os.path.join(brut, "%05d.png"), "-i", a.clip,
                        "-map", "0:v", "-map", "1:a?", "-c:v", "libx264",
                        "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy",
                        a.sortie, "-y"], check=True)
        print("  -> %s" % a.sortie)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
