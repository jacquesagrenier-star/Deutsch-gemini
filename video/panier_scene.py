# -*- coding: utf-8 -*-
"""Les paniers des repliques d'une scene (image + piste), lus dans la scene elle-meme.

    python video/panier_scene.py --scene es-02-el-carro

Ecrit, pour chaque replique qui porte un champ « image » :
    video/episode-<scene>/_a-televerser/planNN-<image>.jpg
    video/episode-<scene>/_a-televerser/planNN-pleine.mp3
Ce sont les noms qu'attend video/omnihuman.py (panier()).

POURQUOI UN NOUVEL OUTIL (21 oct. 2026). preparer_avatar.py lit A-REFAIRE.txt
et tire la piste du montage allemand : une serie neuve n'a ni l'un ni l'autre.
Ici la correspondance plan -> image vit dans la scene (champ « image »), et la
piste vient de audio/scenes/<scene>/, deja egalisee par audio/egaliser_voix.py.

LES DEUX REGLES DE LA PROCEDURE (etape 1), APPLIQUEES ICI :
  - l'image a sa RESOLUTION D'ORIGINE (JPEG qualite 95) : << the clearer the
    input image, the better >> ; le 12 sept. tout avait ete reduit a tort ;
  - la piste n'est PAS raccourcie : 0,35 s de silence devant (l'amorce du
    montage) et 0,90 s derriere (sa queue) -- la bouche met ~1,4 s a se
    refermer apres le dernier mot, et ce silence est sa marge.
"""
import argparse
import io
import json
import os
import subprocess
import sys

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMORCE, QUEUE = 0.35, 0.90


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    a = ap.parse_args()
    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    tel = os.path.join(RACINE, "video", "episode-" + a.scene, "_a-televerser")
    os.makedirs(tel, exist_ok=True)
    for p in d["plans"]:
        if p.get("type") != "replique":
            continue
        if not p.get("image"):
            sys.exit("  plan %d : replique sans champ « image » dans la scene." % p["n"])
        n = p["n"]
        src_img = os.path.join(RACINE, p["image"])
        nom = os.path.splitext(os.path.basename(src_img))[0]
        for vieux in [f for f in os.listdir(tel) if f.startswith("plan%02d-" % n) and f.endswith(".jpg")]:
            if vieux != "plan%02d-%s.jpg" % (n, nom):
                os.remove(os.path.join(tel, vieux))       # un seul candidat par plan (voir panier())
        Image.open(src_img).convert("RGB").save(os.path.join(tel, "plan%02d-%s.jpg" % (n, nom)), quality=95)
        piste = os.path.join(RACINE, "audio", "scenes", a.scene, "%02d-%s.mp3" % (n, p["locuteur"]))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", piste, "-af",
                        "adelay=%d:all=1,apad=pad_dur=%.2f" % (AMORCE * 1000, QUEUE),
                        "-ar", "44100", "-ac", "1", "-b:a", "192k",
                        os.path.join(tel, "plan%02d-pleine.mp3" % n)], check=True)
        print("  plan %02d  %-8s %s" % (n, p["locuteur"], os.path.basename(src_img)))


if __name__ == "__main__":
    main()
