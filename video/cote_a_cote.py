# -*- coding: utf-8 -*-
"""Deux ou trois prises du meme plan, cote a cote, avec leur nom dessus.

    python video/cote_a_cote.py --plan 10
    python video/cote_a_cote.py --plan 10 --sortie ailleurs.mp4

POURQUOI CE SCRIPT EXISTE
    Le 12 septembre 2026, Jacques compare une prise OmniHuman a la version
    Seedance qu'il a vue la veille : « ce n'est pas aussi interessant qu'on
    avait avant ». Une prise se juge contre une autre, pas contre un
    souvenir -- et un souvenir d'un jour flatte ou punit sans qu'on sache
    lequel.

    Les fichiers plan05-avant-apres.mp4, plan16-syncso-vs-seedance.mp4 et les
    autres avaient ete bricoles a la main, un a un. Celui-ci les remplace.

⚠️ ON RAMENE TOUT AU MEME FORMAT ET A LA MEME CADENCE. Une prise en
   1088x1920 a 30 im/s a cote d'une en 720x1280 a 24 donne un ecart qui ne
   parle que de l'encodage, et l'oeil le lit comme une difference de qualite.

⚠️ LE SON VIENT D'UNE SEULE PRISE, la premiere trouvee. Trois pistes
   identiques melangees se peignent en un ecart de phase audible qui
   n'existe dans aucune des trois.
"""
import argparse
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

L, H = 540, 960          # chaque vignette


# ⚠️ LES ETIQUETTES DISENT CE QU'ON SAIT, PAS CE QU'ON CROYAIT.
# Le 12 septembre 2026, le selecteur de modele du Studio BytePlus revenait
# tout seul au 1.5 a chaque ouverture -- constate apres coup. Les deux
# premieres prises ont donc PEUT-ETRE ete faites par le meme modele, et
# l'ecart de 13 % qu'on avait mesure entre elles mesurait alors la variation
# d'un tirage a l'autre, pas une difference de modele. Rien dans les fichiers
# ne permet de trancher : memes dimensions, meme cadence, memes balises.
#
# On nomme donc les prises par ce qui est CERTAIN -- leur ordre et le prompt
# utilise -- et jamais par un modele qu'on n'a pas verifie. Une etiquette plus
# precise que ce qu'on sait finit par etre citee comme un fait.
def sources(ep, n):
    """Les prises connues de ce plan, dans l'ordre chronologique."""
    lip = os.path.join(ep, "04-lipsync", "plan%02d.mp4" % n)
    dos = os.path.join(ep, "_essai-avatar", "retours")
    cand = [
        ("Seedance + sync.so", lip),
        ("avatar - prompt A", os.path.join(dos, "plan%02d-omnihuman1.mp4" % n)),
        ("avatar - prompt A (2)", os.path.join(dos, "plan%02d-omnihuman15.mp4" % n)),
        ("avatar - prompt B", os.path.join(dos, "plan%02d-omnihuman1-B.mp4" % n)),
        ("avatar", os.path.join(dos, "plan%02d-omnihuman.mp4" % n)),
    ]
    return [(nom, c) for nom, c in cand if os.path.exists(c)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int, required=True)
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--sortie")
    a = ap.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    prises = sources(ep, a.plan)
    if len(prises) < 2:
        sys.exit("  Il faut au moins deux prises du plan %02d. Trouve : %d."
                 % (a.plan, len(prises)))

    F = M.ffmpeg()
    dst = a.sortie or os.path.join(ep, "plan%02d-cote-a-cote.mp4" % a.plan)

    cmd = [F, "-y", "-v", "error"]
    for _, c in prises:
        cmd += ["-i", c]

    # ⚠️ La police doit exister sur la machine : sans fontfile, drawtext
    # echoue avec un message que ffmpeg n'explique pas.
    police = "C\\:/Windows/Fonts/arial.ttf"
    filtres = []
    for i, (nom, _) in enumerate(prises):
        filtres.append(
            "[%d:v]scale=%d:%d:force_original_aspect_ratio=decrease,"
            "pad=%d:%d:-1:-1:color=0x14181C,fps=25,"
            "drawtext=fontfile='%s':text='%s':fontcolor=white:fontsize=26:"
            "box=1:boxcolor=0x14181C@0.75:boxborderw=10:x=(w-text_w)/2:y=h-56"
            "[v%d]" % (i, L, H, L, H, police, nom, i))
    filtres.append("".join("[v%d]" % i for i in range(len(prises)))
                   + "hstack=inputs=%d[out]" % len(prises))

    cmd += ["-filter_complex", ";".join(filtres), "-map", "[out]",
            "-map", "0:a?", "-c:v", "libx264", "-crf", "18",
            "-preset", "medium", "-c:a", "aac", "-b:a", "160k", dst]
    subprocess.run(cmd, check=True)

    print("  %s" % os.path.relpath(dst, RACINE))
    print("  %d prises, %.2f s : %s"
          % (len(prises), M.duree(F, dst), ", ".join(n for n, _ in prises)))
    print("  le son vient de : %s" % prises[0][0])


if __name__ == "__main__":
    main()
