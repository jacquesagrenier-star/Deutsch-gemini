# -*- coding: utf-8 -*-
"""Rapatrie une prise depuis Telechargements, lui coupe le son, et la classe.

    python video/rapatrier.py --plan 13
    python video/rapatrier.py --plan 13 --fichier "C:/chemin/vers/clip.mp4"

POURQUOI COUPER LE SON
    Seedance fabrique une piste audio et fait articuler au personnage des mots
    inventes. La voix, elle, vient d'ElevenLabs et se pose au montage. Garder
    les deux revient a se demander trois semaines plus tard laquelle on ecoute.

    Ce que le personnage semblait articuler n'a aucune importance : sync.so
    reecrit la zone de la bouche par-dessus. Seule compte la nettete du visage.

ON NE REENCODE PAS
    -c copy recopie le flux video tel quel et jette la piste audio. Aucune
    perte, et c'est instantane. Un reencodage a cette etape abimerait l'image
    avant meme le lip-sync, qui la reencodera de toute facon une fois.

PLUSIEURS PRISES PAR PLAN, ET C'EST VOULU
    Un modele video ne rend jamais deux fois la meme chose. On juge sur une
    serie, pas sur un essai. Le numero s'incremente tout seul : plan13-01,
    plan13-02... On garde les ratees jusqu'a ce que la bonne soit choisie --
    elles coutent 200 credits chacune et ne se refont pas a l'identique.
"""
import argparse
import glob
import io
import json
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = (".mp4", ".mov", ".webm", ".m4v")


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("  ffmpeg introuvable. Il vient avec le paquet imageio-ffmpeg.")


def telechargements():
    """Le dossier de telechargement, quel que soit son nom -- il est en francais
    sur certaines installations et en anglais sur d'autres."""
    base = os.path.expanduser("~")
    for nom in ("Downloads", "Telechargements", u"T\u00e9l\u00e9chargements"):
        d = os.path.join(base, nom)
        if os.path.isdir(d):
            return d
    return None


def plus_recente(dossier):
    fichiers = [f for f in glob.glob(os.path.join(dossier, "*"))
                if f.lower().endswith(VIDEOS)]
    return max(fichiers, key=os.path.getmtime) if fichiers else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int, required=True)
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--fichier", help="a defaut, la video la plus recente des telechargements")
    a = ap.parse_args()

    src = a.fichier
    if not src:
        d = telechargements()
        if not d:
            sys.exit("  Dossier de telechargement introuvable. Passe --fichier.")
        src = plus_recente(d)
        if not src:
            sys.exit("  Aucune video dans %s.\n"
                     "  Clique << Download >> sur la prise dans Artlist, puis relance." % d)
    if not os.path.exists(src):
        sys.exit("  Introuvable : %s" % src)

    # Le plan existe-t-il vraiment dans la scene ? Une faute de frappe sur --plan
    # classerait la prise sous un numero qui n'a pas de replique.
    fs = os.path.join(RACINE, "scenes", a.scene + ".json")
    if os.path.exists(fs):
        d = json.load(io.open(fs, encoding="utf-8"))
        p = next((x for x in d["plans"] if x["n"] == a.plan), None)
        if not p:
            sys.exit("  Le plan %d n'existe pas dans %s." % (a.plan, a.scene))
        print("  plan %02d  %s  (%s s)" % (a.plan, p["locuteur"], p["duree"]))
        if p.get("de"):
            print("  << %s >>" % p["de"])

    dst = os.path.join(RACINE, "video", "episode-" + a.scene, "02-prises")
    if not os.path.isdir(dst):
        os.makedirs(dst)
    n = 1
    while os.path.exists(os.path.join(dst, "plan%02d-%02d.mp4" % (a.plan, n))):
        n += 1
    out = os.path.join(dst, "plan%02d-%02d.mp4" % (a.plan, n))

    r = subprocess.run([ffmpeg(), "-hide_banner", "-nostats", "-loglevel", "error",
                        "-y", "-i", src, "-c", "copy", "-an", out],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("  echec ffmpeg :\n%s" % r.stderr[-600:])

    print("  %s  ->  video/episode-%s/02-prises/%s  (%d Ko, muet)"
          % (os.path.basename(src), a.scene, os.path.basename(out),
             os.path.getsize(out) // 1024))
    print("  L'original reste dans les telechargements : rien n'est efface.")


if __name__ == "__main__":
    main()
