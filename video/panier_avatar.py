# -*- coding: utf-8 -*-
"""Le panier d'un episode NEUF : l'image en JPEG, la piste allongee au plan.

    python video/panier_avatar.py --scene 02-beim-buergeramt
    python video/panier_avatar.py --scene 02-beim-buergeramt --plan 3 8

POURQUOI CE SCRIPT EXISTE A COTE DE preparer_avatar.py
    preparer_avatar.py tire la piste du CLIP DEJA MONTE (04-lipsync/planNN.mp4).
    C'est juste pour l'episode 1, ou Seedance avait produit les clips d'abord
    et ou l'avatar est venu apres : la piste faisait deja la longueur du plan.

    Un episode neuf va DIRECTEMENT a l'avatar. Ces clips n'existent pas, et il
    n'y a que les mp3 de audio/scenes/. Il faut donc fabriquer la piste : le
    silence d'amorce, la replique, puis du silence jusqu'a la duree du plan.

⚠️ ON ALLONGE, ON NE RACCOURCIT JAMAIS -- et on paie ce silence.
    OmniHuman facture a la seconde de sortie et la sortie fait la longueur de
    la piste. Le reflexe est donc d'envoyer la voix nue. C'est l'erreur que la
    procedure de l'episode 1 interdit : << le silence final est la marge dont
    la bouche a besoin pour se refermer >> -- environ 1,4 s, mesure sur son
    plan 16. Une piste au ras donne un avatar dont la machoire est coupee net.

    Et la parole n'occupe que la moitie d'un plan : sur l'episode 1, 1,2 a
    2,7 s de voix dans des clips de 5,04 s. Le reste, c'est le personnage qui
    ECOUTE -- ce que les prompts d'avatar demandent explicitement.

CE QU'IL LIT, ET OU
    scenes/<scene>.json     image et duree_plan de chaque replique
    audio/scenes/<scene>/   la voix, deja egalisee par scene_audio.py
    01-images/              l'image, en PNG
CE QU'IL ECRIT
    _a-televerser/planNN-<image>.jpg   et   planNN-pleine.mp3

⚠️ L'IMAGE PASSE EN JPEG A SA RESOLUTION D'ORIGINE. Nos PNG montent a 8 Mo ;
   un JPEG de qualite 2 tombe vers 1 Mo sans perte visible a l'oeil. On ne
   reduit JAMAIS la taille en pixels : un generateur suit ce qu'il peut voir,
   et c'est la lecon du recadrage des planches de Mark le 13 septembre.
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
import montage as M                                          # noqa: E402

AMORCE = M.AMORCE        # 0,35 s -- on voit le personnage avant qu'il parle
PRIX = 0.16


def lancer(args):
    r = subprocess.run(args, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  ffmpeg a echoue :\n%s" % r.stderr[-600:])


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", required=True)
    p.add_argument("--plan", type=int, nargs="+",
                   help="par defaut, toutes les repliques")
    a = p.parse_args()

    d = json.loads(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                           encoding="utf-8").read())
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    images = os.path.join(ep, "01-images")
    voix = os.path.join(RACINE, "audio", "scenes", a.scene)
    tel = os.path.join(ep, "_a-televerser")
    os.makedirs(tel, exist_ok=True)

    ff = M.ffmpeg()
    plans = [x for x in d["plans"] if x["type"] != "decor"
             and (not a.plan or x["n"] in a.plan)]
    if not plans:
        sys.exit("  aucune replique a preparer.")

    total = 0.0
    for x in plans:
        n = x["n"]
        for champ in ("image", "duree_plan", "duree_audio"):
            if not x.get(champ):
                sys.exit("  plan %d : champ %s absent de la scene." % (n, champ))
        cible = float(x["duree_plan"])

        # --- l'image -------------------------------------------------------
        src_png = os.path.join(images, os.path.splitext(x["image"])[0] + ".png")
        if not os.path.exists(src_png):
            sys.exit("  plan %d : image absente -> %s" % (n, src_png))
        dst_jpg = os.path.join(tel, "plan%02d-%s.jpg"
                               % (n, os.path.splitext(x["image"])[0]))
        lancer([ff, "-y", "-v", "error", "-i", src_png, "-q:v", "2", dst_jpg])

        # --- la piste ------------------------------------------------------
        src_mp3 = os.path.join(voix, "%02d-%s.mp3" % (n, x["locuteur"]))
        if not os.path.exists(src_mp3):
            sys.exit("  plan %d : voix absente -> %s" % (n, src_mp3))
        dst_mp3 = os.path.join(tel, "plan%02d-pleine.mp3" % n)
        # adelay pose l'amorce, apad allonge, -t coupe a la cible. Dans cet
        # ordre : apad sans -t serait infini.
        lancer([ff, "-y", "-v", "error", "-i", src_mp3,
                "-af", "adelay=%d:all=1,apad" % int(AMORCE * 1000),
                "-t", "%.3f" % cible, "-c:a", "libmp3lame", "-q:a", "2",
                dst_mp3])

        reel = M.duree(ff, dst_mp3) or cible
        apres = cible - AMORCE - float(x["duree_audio"])
        print("  plan %-3d %-22s voix %.2fs  plan %.2fs  (%.2fs d'ecoute apres)"
              % (n, os.path.basename(dst_jpg), x["duree_audio"], reel, apres))
        if apres < 1.0:
            print("           ⚠️ moins d'1 s apres le dernier mot : la bouche "
                  "met ~1,4 s a se refermer.")
        total += reel

    print("\n  %d plan(s), %.1f s -> %.2f $ chez fal" % (len(plans), total,
                                                         total * PRIX))
    print("  Ensuite : python video/omnihuman.py --scene %s --reste --simuler"
          % a.scene)


if __name__ == "__main__":
    main()
