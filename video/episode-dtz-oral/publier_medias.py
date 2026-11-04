# -*- coding: utf-8 -*-
"""Pose les voix et les clips RETENUS de l'oral du DTZ la ou la page les lit. GRATUIT.

    python video/episode-dtz-oral/publier_medias.py

  visuel/prototype/dtz/voix/<id>.mp3    toutes les repliques (audio/scenes/dtz-oral/), mono 64 kbit/s
  visuel/prototype/dtz/video/<id>.mp4   les clips Kling de RETENUS seulement, 480 px de large, H.264 + AAC,
                                        COUPES a la fin de la voix (video/bouche_apres_voix.py, point_de_coupe),
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
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
from bouche_apres_voix import point_de_coupe  # noqa: E402
DTZ = os.path.join(RACINE, "visuel", "prototype", "dtz")
ESSAI = os.path.join(ICI, "_essai-avatar")

# Les numeros de plan (scenes/dtz-oral.json) dont la prise Kling a ete regardee et gardee.
# 3 nov. 2026 : les 23 prises, chacune passee a texte_incruste.py et vue sur une planche de 8 images. 22 et 25 sont
# des reprises (le buste qui bougeait faisait bouger la camera) ; 23, 24 et 25 sont recadrees au-dessus de faux
# sous-titres (crop=720:900:0:50 depuis le 4 nov. : le cadre 4:5 que la page montre des autres clips, remonte de
# 50 px ; l'original en planNN-kling-avant-recadrage.mp4). Le premier recadrage (crop=536:952:92:0, 9:16 depuis le
# haut) laissait un mur au-dessus d'Anna et sa tete en bas du cadre (Jacques, 4 nov. : << mal cadree >>).
RETENUS = {1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}


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
            # COUPE A LA FIN DE LA VOIX (4 nov. 2026, Jacques : la bouche d'Anna bougeait apres sa replique). La queue
            # muette de 1,3 s du panier sert a Kling ; dans 19 prises sur 23 il y a fait articuler la bouche. La page
            # s'arrete sur la derniere image : on coupe la ou la bouche est la plus fermee, 0,08 a 0,4 s apres la voix.
            coupe, fin, retard = point_de_coupe(prise)
            print("  %-16s voix -> %5.2f s, coupe a %5.2f s%s" % (cle, fin, coupe,
                  "  (la bouche bougeait %.2f s de plus)" % retard if retard > 0.25 else ""))
            mp4 = os.path.join(DTZ, "video", cle + ".mp4")
            ff("-i", prise, "-t", "%.3f" % coupe, "-vf", "scale=480:-2", "-c:v", "libx264", "-preset", "slow", "-crf", "26",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", mp4)
            ff("-i", mp4, "-frames:v", "1", "-q:v", "4", os.path.join(DTZ, "video", cle + ".jpg"))
        manifeste[cle] = {"son": 1, "video": 1 if video else 0}
    io.open(os.path.join(DTZ, "voix", "manifest.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n")
    print("%d voix, %d clips" % (len(manifeste), sum(v["video"] for v in manifeste.values())))


if __name__ == "__main__":
    main()
