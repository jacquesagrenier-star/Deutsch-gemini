# -*- coding: utf-8 -*-
"""Pose les voix et les clips RETENUS de l'oral du DTZ la ou la page les lit. GRATUIT.

    python video/episode-dtz-oral/publier_medias.py

  visuel/prototype/dtz/voix/<id>.mp3    toutes les repliques (audio/scenes/dtz-oral/), mono 64 kbit/s
  visuel/prototype/dtz/video/<id>.mp4   les clips Kling de RETENUS seulement, 480 px de large, H.264 + AAC,
  visuel/prototype/dtz/video/<id>.jpg   leur premiere image (le poster, avant que la video joue)
  visuel/prototype/dtz/voix/manifest.json   {id: {"son": 1, "video": 0|1}} -- la page s'y fie

⚠️ UN CLIP N'ENTRE DANS RETENUS QU'APRES AVOIR ETE REGARDE : texte_incruste.py « propre » ET une planche d'images
   vue (le detecteur se trompe dans les deux sens, verifier_prompt.py « texte-incruste »). Une replique sans clip
   retenu joue sa voix enregistree, avec le portrait : rien ne casse.
"""
import io
import json
import os
import subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
DTZ = os.path.join(RACINE, "visuel", "prototype", "dtz")
ESSAI = os.path.join(ICI, "_essai-avatar")

# Les numeros de plan (scenes/dtz-oral.json) dont la prise Kling a ete regardee et gardee.
RETENUS = set()


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True)


def main():
    sc = json.load(io.open(os.path.join(RACINE, "scenes", "dtz-oral.json"), encoding="utf-8"))
    os.makedirs(os.path.join(DTZ, "voix"), exist_ok=True)
    os.makedirs(os.path.join(DTZ, "video"), exist_ok=True)
    manifeste = {}
    for p in sc["plans"]:
        cle, n = p["id"], p["n"]
        ff("-i", os.path.join(RACINE, "audio", "scenes", "dtz-oral", "%02d-%s.mp3" % (n, p["locuteur"])),
           "-ac", "1", "-b:a", "64k", os.path.join(DTZ, "voix", cle + ".mp3"))
        prise = os.path.join(ESSAI, "plan%02d-kling.mp4" % n)
        video = n in RETENUS and os.path.exists(prise)
        if video:
            mp4 = os.path.join(DTZ, "video", cle + ".mp4")
            ff("-i", prise, "-vf", "scale=480:-2", "-c:v", "libx264", "-preset", "slow", "-crf", "26",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", mp4)
            ff("-i", mp4, "-frames:v", "1", "-q:v", "4", os.path.join(DTZ, "video", cle + ".jpg"))
        manifeste[cle] = {"son": 1, "video": 1 if video else 0}
    io.open(os.path.join(DTZ, "voix", "manifest.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n")
    print("%d voix, %d clips" % (len(manifeste), sum(v["video"] for v in manifeste.values())))


if __name__ == "__main__":
    main()
