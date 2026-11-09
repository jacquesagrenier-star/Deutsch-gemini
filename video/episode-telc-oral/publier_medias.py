# -*- coding: utf-8 -*-
"""Pose les voix et les clips RETENUS de l'oral du telc la ou la page les lit. GRATUIT.

    python video/episode-telc-oral/publier_medias.py

Memes dossiers que l'oral du DTZ, dont la page du telc lit deja le manifeste (visuel/prototype/dtz/voix/manifest.json) :
aucun code a changer, une replique passe du portrait a la video des que son entree dit video:1. Le manifeste est
COMPLETE, jamais recree : il porte aussi les repliques du DTZ.

Chaque clip est coupe a la fin de la voix (video/bouche_apres_voix.py). RETOUCHES efface un intrus sur le mur en y
recollant le mur d'un autre instant de la meme prise, et seulement pendant ces images : le mur est fixe, rien ne se voit.

⚠️ UN CLIP N'ENTRE DANS RETENUS QU'APRES AVOIR ETE REGARDE : texte_incruste.py, intrus_au_bord.py, apparition_sur_mur.py, et une planche.
"""
import io
import json
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
from bouche_apres_voix import point_de_coupe  # noqa: E402
DTZ = os.path.join(RACINE, "visuel", "prototype", "dtz")
ESSAI = os.path.join(ICI, "_essai-avatar")

RETENUS = set(range(1, 36))
# plan : (x, y, largeur, hauteur, debut, fin, instant d'ou vient le mur), en pixels de la prise (720 x 1280) et en secondes
RETOUCHES = {
    12: (30, 270, 175, 240, 5.5, 6.5, 5.0),     # un faux caractere noir sur le mur, de 5,67 a 6,40 s
    34: (0, 0, 72, 1060, 12.7, 14.4, 12.0),     # une tete et une main fantomes au bord gauche, des 12,80 s
}
# Au-dessus de faux sous-titres : le cadre 4:5 que la page montre, remonte de 50 px, comme les verdicts du DTZ.
RECADRES = {20: "720:900:0:50", 29: "720:900:0:50"}


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True)


def main():
    sc = json.load(io.open(os.path.join(RACINE, "scenes", "telc-oral.json"), encoding="utf-8"))
    chemin_m = os.path.join(DTZ, "voix", "manifest.json")
    manifeste = json.load(io.open(chemin_m, encoding="utf-8"))
    for p in sc["plans"]:
        cle, n = p["id"], p["n"]
        ff("-i", os.path.join(RACINE, "audio", "scenes", "telc-oral", "%02d-%s.mp3" % (n, p["locuteur"])),
           "-ac", "1", "-b:a", "64k", os.path.join(DTZ, "voix", cle + ".mp3"))
        prise = os.path.join(ESSAI, "plan%02d-kling.mp4" % n)
        video = n in RETENUS and os.path.exists(prise)
        if video:
            coupe, fin, retard = point_de_coupe(prise)
            print("  %-16s voix -> %5.2f s, coupe a %5.2f s" % (cle, fin, coupe))
            mp4 = os.path.join(DTZ, "video", cle + ".mp4")
            if n in RETOUCHES:
                x, y, l, h, t0, t1, source = RETOUCHES[n]
                filtre = ("[1:v]crop=%d:%d:%d:%d[mur];[0:v][mur]overlay=%d:%d:enable='between(t,%g,%g)',scale=480:-2[v]"
                          % (l, h, x, y, x, y, t0, t1))
                mur = os.path.join(ESSAI, "mur-plan%02d.png" % n)
                ff("-ss", "%.3f" % source, "-i", prise, "-frames:v", "1", mur)
                ff("-i", prise, "-loop", "1", "-i", mur, "-t", "%.3f" % coupe, "-filter_complex", filtre,
                   "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-pix_fmt", "yuv420p",
                   "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", mp4)
                os.remove(mur)
            else:
                vf = "crop=%s,scale=480:-2" % RECADRES[n] if n in RECADRES else "scale=480:-2"
                ff("-i", prise, "-t", "%.3f" % coupe, "-vf", vf, "-c:v", "libx264", "-preset", "slow", "-crf", "26",
                   "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", mp4)
            ff("-i", mp4, "-frames:v", "1", "-q:v", "4", os.path.join(DTZ, "video", cle + ".jpg"))
        manifeste[cle] = {"son": 1, "video": 1 if video else 0}
    io.open(chemin_m, "w", encoding="utf-8", newline="\n").write(json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n")
    print("%d entrees au manifeste, dont %d clips" % (len(manifeste), sum(v["video"] for v in manifeste.values())))


if __name__ == "__main__":
    main()
