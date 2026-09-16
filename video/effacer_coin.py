# -*- coding: utf-8 -*-
"""Effacer un intrus au bord du cadre, sans repasser par le modele.

    python video/effacer_coin.py <clip.mp4>
    python video/effacer_coin.py <clip.mp4> --zone 90x450+0+0 --fondu 30
    python video/effacer_coin.py <clip.mp4> --mesurer      (ne modifie rien)

POURQUOI CET OUTIL EXISTE.

OmniHuman fait entrer, de temps en temps, quelqu'un qui ne devrait pas etre
la : une nuque, des cheveux, une epaule floue au bord du cadre. Le prompt
l'interdit sur dix lignes -- et c'est peut-etre ce qui l'appelle, ces modeles
n'ayant aucun canal pour les negations (le schema de l'API n'a ni
`negative_prompt` ni `seed`). Regenerer coute 0,70 $ et ne garantit rien : le
tirage suivant peut refaire la meme chose.

Or la camera de ces plans est VERROUILLEE et le fond y est un mur uni. Ce que
l'intrus recouvre ne bouge donc jamais : il suffit de recopier ce coin depuis
une image ou il est absent, sur toute la duree. Recopier un mur immobile sur
un mur immobile ne se voit pas.

⚠️ CE QUE CET OUTIL NE SAIT PAS FAIRE, ET QU'IL NE FAUT PAS LUI DEMANDER.
   Il ne repare qu'un fond FIXE. Si l'intrus passe devant le personnage, s'il
   traverse une zone ou quelque chose bouge (la main, la feuille, un reflet),
   le rustine gelerait ce mouvement. Dans ce cas-la, il faut regenerer.
   `--mesurer` sert justement a verifier d'abord OU et QUAND ca bouge.

⚠️ ET L'IMAGE DE REFERENCE N'EST PAS TOUJOURS LA PREMIERE. L'intrus arrive
   souvent apres une demi-seconde, mais pas toujours : `--mesurer` compare
   chaque image a la premiere, et si la premiere est deja sale, tout l'ecart
   se lit a l'envers. Regarder la sortie avant de faire confiance.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ffmpeg(args, muet=True):
    c = ["ffmpeg", "-v", "error" if muet else "info", "-y"] + args
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.exit("  ffmpeg a echoue :\n  " + (r.stderr or "")[-600:])
    return r


def dimensions(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=width,height,nb_frames",
                        "-of", "csv=p=0", clip], capture_output=True, text=True)
    p = (r.stdout or "").strip().split(",")
    return int(p[0]), int(p[1])


def mesurer(clip, large, haut):
    """Ou et quand le bord change-t-il ? Gratuit, et a lire AVANT de rustiner."""
    import io
    W, H = 80, 120
    brut = os.path.join(os.environ.get("TEMP", "."), "_coin.raw")
    ffmpeg(["-i", clip, "-vf",
            "crop=%d:%d:0:0,format=gray,scale=%d:%d" % (large, haut, W, H),
            "-f", "rawvideo", brut])
    d = io.open(brut, "rb").read()
    n = len(d) // (W * H)
    ref = d[:W * H]
    print("  %d images, zone %dx%d en haut a gauche" % (n, large, haut))
    vu = False
    for i in range(n):
        f = d[i * W * H:(i + 1) * W * H]
        forts = [k for k in range(W * H) if abs(f[k] - ref[k]) > 28]
        if not forts:
            continue
        vu = True
        xs = [k % W for k in forts]
        ys = [k // W for k in forts]
        if i % 5 == 0:
            print("    %5.2f s  %4d px   x 0-%3d px   y 0-%3d px"
                  % (i / 25.0, len(forts),
                     max(xs) * large // W, max(ys) * haut // H))
    if not vu:
        print("    rien ne change dans cette zone.")
    os.remove(brut)


def effacer(clip, x, y, large, haut, fondu, image_ref):
    W, H = dimensions(clip)
    if x + large > W or y + haut > H:
        sys.exit("  la zone deborde du cadre (%dx%d)." % (W, H))

    base = os.path.splitext(clip)[0]
    garde = base + "-AVANT-coin.mp4"
    if not os.path.exists(garde):
        shutil.copy2(clip, garde)
        print("  prise d'origine gardee : %s" % os.path.basename(garde))

    tmp = os.path.join(os.environ.get("TEMP", "."), "_ref.png")
    rustine = os.path.join(os.environ.get("TEMP", "."), "_rustine.png")
    ffmpeg(["-ss", str(image_ref), "-i", clip, "-vframes", "1", tmp])

    # Le fondu vit dans l'alpha : plein au coin, nul aux deux bords interieurs.
    # Sans lui, la rustine laisse une arete visible sur un mur en degrade.
    alpha = ("255*min(1,min((%d-X)/%d,(%d-Y)/%d))" % (large, fondu, haut, fondu))
    ffmpeg(["-i", tmp, "-vf",
            "crop=%d:%d:%d:%d,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='%s'"
            % (large, haut, x, y, alpha), rustine])

    sortie = base + "-propre.mp4"
    ffmpeg(["-i", clip, "-i", rustine, "-filter_complex",
            "[0:v][1:v]overlay=%d:%d" % (x, y),
            "-c:a", "copy", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
            "-pix_fmt", "yuv420p", sortie])
    os.replace(sortie, clip)
    for f in (tmp, rustine):
        try:
            os.remove(f)
        except OSError:
            pass
    print("  zone %dx%d en (%d,%d) recouverte depuis l'image de %.2f s, fondu %d px"
          % (large, haut, x, y, image_ref, fondu))
    print("  ecrit : %s" % os.path.basename(clip))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clip")
    p.add_argument("--zone", default="90x450+0+0",
                   help="LxH+X+Y en pixels (defaut 90x450+0+0)")
    p.add_argument("--fondu", type=int, default=30,
                   help="largeur du fondu des bords interieurs, en pixels")
    p.add_argument("--ref", type=float, default=0.0,
                   help="seconde de l'image PROPRE a recopier (defaut 0)")
    p.add_argument("--mesurer", action="store_true",
                   help="dire ou et quand le bord change, sans rien modifier")
    a = p.parse_args()

    if not os.path.exists(a.clip):
        sys.exit("  introuvable : %s" % a.clip)

    m = re.match(r"^(\d+)x(\d+)\+(\d+)\+(\d+)$", a.zone)
    if not m:
        sys.exit("  --zone attend la forme LxH+X+Y, par exemple 90x450+0+0")
    large, haut, x, y = (int(g) for g in m.groups())

    if a.mesurer:
        mesurer(a.clip, max(large, 400), max(haut, 600))
        return
    effacer(a.clip, x, y, large, haut, a.fondu, a.ref)


if __name__ == "__main__":
    main()
