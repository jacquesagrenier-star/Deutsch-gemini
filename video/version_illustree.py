# -*- coding: utf-8 -*-
"""Une version ILLUSTREE d'un episode : les images fixes des plans, un lent
mouvement de camera, la bande-son et les sous-titres de l'episode monte.

    python video/version_illustree.py --scene 02-beim-buergeramt --clip EPISODE-02-sonorise.mp4

POURQUOI (21 oct. 2026). Jacques : « tu n'es pas en mesure de faire des videos
toi-meme ? ». Ce format ne paie aucun clip : il reprend les images deja faites
(01-images), le son de l'episode et son .ass. Il sert a COMPARER, cote a cote,
avec la version tournee : la difference vaut-elle les ~18 $ d'un episode ?

Rien n'est genere ni paye ici. La ligne de temps est celle du montage
(_montage-avatar/_plans.json), comme pour sous_titres.py : les sous-titres et
le son tombent donc aux memes instants que dans la version tournee.
"""
import argparse
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

L, H, FPS = 720, 1280, 30


def image_du_plan(ep, nom):
    base = os.path.splitext(nom)[0]
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = os.path.join(ep, "01-images", base + ext)
        if os.path.exists(p):
            return p
    sys.exit("  Image introuvable pour " + nom)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--clip", required=True, help="la video montee dont on prend le son")
    ap.add_argument("--langue", default="fr")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    plans = json.load(io.open(os.path.join(ep, "_montage-avatar", "_plans.json"), encoding="utf-8"))
    scene = {p["n"]: p for p in json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                                                 encoding="utf-8"))["plans"]}
    travail = os.path.join(ep, "_illustree")
    os.makedirs(travail, exist_ok=True)

    morceaux = []
    for k, p in enumerate(plans):
        img = image_du_plan(ep, scene[p["n"]]["image"])
        n_im = max(1, int(round(p["duree"] * FPS)))
        # Un lent zoom, avant un plan sur deux, arriere l'autre : de 100 a 108 %.
        if k % 2 == 0:
            z = "1+0.08*on/%d" % n_im
        else:
            z = "1.08-0.08*on/%d" % n_im
        sortie = os.path.join(travail, "plan%02d.mp4" % p["n"])
        vf = ("scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,"
              "scale=%d:%d,zoompan=z='%s':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              ":d=%d:s=%dx%d:fps=%d,format=yuv420p") % (L * 2, H * 2, L * 2, H * 2, L * 2, H * 2,
                                                         z, n_im, L, H, FPS)
        subprocess.run([F, "-loglevel", "error", "-y", "-loop", "1", "-i", img, "-vf", vf,
                        "-frames:v", str(n_im), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast",
                        "-crf", "20", sortie], check=True)
        morceaux.append(sortie)
        print("  plan %02d  %.2f s  %s" % (p["n"], p["duree"], os.path.basename(img)))

    liste = os.path.join(travail, "_liste.txt")
    with io.open(liste, "w", encoding="utf-8") as f:
        for m in morceaux:
            f.write("file '%s'\n" % m.replace("\\", "/"))
    muet = os.path.join(travail, "_muet.mp4")
    subprocess.run([F, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", liste,
                    "-c", "copy", muet], check=True)

    clip = os.path.join(ep, a.clip)
    base = os.path.splitext(a.clip)[0]
    ass = os.path.join(ep, base + "." + a.langue + ".ass")
    if not os.path.exists(ass):
        sys.exit("  Pas de sous-titres " + ass + " : lancer sous_titres.py d'abord.")
    final = os.path.join(ep, base + "-illustree-st." + a.langue + ".mp4")
    # Le filtre ass veut un chemin ou les deux-points et les antislashs sont echappes.
    ass_f = ass.replace("\\", "/").replace(":", "\\:")
    subprocess.run([F, "-loglevel", "error", "-y", "-i", muet, "-i", clip,
                    "-map", "0:v", "-map", "1:a", "-vf", "ass='%s'" % ass_f,
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", final], check=True)
    print("  " + os.path.relpath(final, RACINE))


if __name__ == "__main__":
    main()
