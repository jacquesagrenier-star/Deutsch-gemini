# -*- coding: utf-8 -*-
"""Taille les douze segments de l'episode dans deux clips de cinq secondes.

    python video/decouper.py --scene 01-ankunft-berlin

POURQUOI DEUX CLIPS SUFFISENT
    Il faut 21 secondes de Mark et 28 d'Anna, et on n'a que cinq secondes de
    chacun. On les rallonge par ALLER-RETOUR : le clip a l'endroit, puis a
    l'envers, puis a l'endroit. La boucle est invisible parce que la derniere
    image de l'aller EST la premiere du retour -- aucun saut, aucun raccord a
    masquer. Sur des mouvements discrets, personne ne le voit.

    Et surtout : le lip-sync reecrit la bouche par-dessus. Le clip d'origine
    est muet et ne « dit » rien ; il doit seulement montrer quelqu'un de
    credible au comptoir. C'est ce qui rend la boucle acceptable ici alors
    qu'elle ne le serait pas dans un film ordinaire.

CHAQUE SEGMENT PART D'UN ENDROIT DIFFERENT
    Les six repliques d'un personnage se suivent dans la boucle au lieu de
    repartir toutes de zero. Sans ca, les six plans montreraient exactement le
    meme geste au meme moment, et la repetition sauterait aux yeux.
"""
import argparse
import io
import json
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import normaliser                                          # noqa: E402


def ff(args, quoi):
    r = subprocess.run([normaliser.FF, "-hide_banner", "-nostats", "-y"] + args,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("  echec sur %s :\n%s" % (quoi, r.stderr[-600:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    a = ap.parse_args()

    normaliser.FF = normaliser.ffmpeg()
    if not normaliser.FF:
        sys.exit("  ffmpeg introuvable.")

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    rep = [p for p in d["plans"] if p["type"] == "replique"]

    dossier = os.path.join(RACINE, "video", a.scene)
    travail = os.path.join(dossier, "_travail")
    os.makedirs(travail, exist_ok=True)

    for qui in sorted({p["locuteur"] for p in rep}):
        base = os.path.join(RACINE, "video", "%s-base.mp4" % qui)
        if not os.path.exists(base):
            sys.exit("  %s manquant." % os.path.basename(base))

        plans = [p for p in rep if p["locuteur"] == qui]
        besoin = sum(p["duree"] for p in plans)
        duree = normaliser.duree(base)

        # aller-retour, puis autant de tours qu'il en faut pour couvrir le besoin
        env = os.path.join(travail, "%s-envers.mp4" % qui)
        ff(["-i", base, "-vf", "reverse", "-an", env], "inversion de " + qui)
        liste = os.path.join(travail, "%s-ar.txt" % qui)
        io.open(liste, "w", encoding="utf-8", newline="").write(
            "file '%s'\nfile '%s'\n" % (base.replace("\\", "/"), env.replace("\\", "/")))
        ar = os.path.join(travail, "%s-ar.mp4" % qui)
        ff(["-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", ar], "aller-retour " + qui)

        tours = int(besoin // (duree * 2)) + 1
        long = os.path.join(travail, "%s-long.mp4" % qui)
        ff(["-stream_loop", str(tours), "-i", ar, "-c", "copy", long], "boucle " + qui)

        print("  %-6s %d plans, %d s a tailler dans %.0f s bouclees %d fois"
              % (qui, len(plans), besoin, duree * 2, tours + 1))

        # Les segments se suivent dans la boucle : six gestes differents plutot
        # que six fois le meme depart.
        t = 0.0
        for p in plans:
            sortie = os.path.join(dossier, "plan%02d-%s.mp4" % (p["n"], qui))
            # Reencodage plutot que -c copy : une coupe au keyframe le plus
            # proche decalerait le segment de plusieurs dixiemes, et la
            # replique ne tomberait plus au bon endroit.
            ff(["-ss", "%.3f" % t, "-i", long, "-t", "%.3f" % p["duree"],
                "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-pix_fmt", "yuv420p", sortie], "plan %d" % p["n"])
            print("     plan%02d  %d s  a %5.1f s dans la boucle" % (p["n"], p["duree"], t))
            t += p["duree"]

    faits = sorted(f for f in os.listdir(dossier) if f.startswith("plan"))
    total = sum(normaliser.duree(os.path.join(dossier, f)) for f in faits)
    print("\n  %d segments dans video/%s/ — %.1f s au total" % (len(faits), a.scene, total))


if __name__ == "__main__":
    main()
