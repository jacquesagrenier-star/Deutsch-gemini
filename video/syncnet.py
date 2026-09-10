# -*- coding: utf-8 -*-
"""LSE-D et LSE-C : la mesure de lip-sync que le domaine utilise vraiment.

    python video/syncnet.py --plan 16
    python video/syncnet.py --fichier chemin/vers/un/clip.mp4
    python video/syncnet.py --scene 01-ankunft-berlin --tous

POURQUOI CET OUTIL, ET POURQUOI IL REMPLACE LE NOTRE
    video/controler_bouche.py dit lui-meme ce qu'il ne peut pas faire : il
    correle le mouvement de la bouche avec l'enveloppe sonore, et « la prise
    dont Jacques avait vu le defaut obtient la MEILLEURE note ». Une bouche
    tres agitee correle bien, meme si elle articule un charabia. Sa mesure
    s'est trompee quatre fois, et le fichier le dit en toutes lettres.

    SyncNet mesure autre chose : la distance entre ce que la bouche DIT et ce
    que la voix dit, dans l'espace d'un reseau entraine pour ca. C'est la
    mesure sur laquelle se juge toute la litterature des tetes parlantes.

LES DEUX NOMBRES, ET LEUR ECHELLE
    LSE-D (min dist)   la distance. PLUS BAS = MIEUX.
    LSE-C (confidence) la confiance de l'appariement. PLUS HAUT = MIEUX.

    L'echelle est publiee, et c'est tout l'interet : dans les grandes
    evaluations, un LSE-D de 6 a 8 correspond a l'etat de l'art. Notre mesure
    maison n'avait aucun etalon -- on ne savait pas si 0,53 etait bon.

    Le troisieme nombre, AV offset, est le decalage en IMAGES a 25 im/s. Il se
    lit en millisecondes contre les seuils de l'UIT-R BT.1359-1, comme dans
    video/mesurer_decalage.py : detection a +45 ms (son en avance) et -125 ms
    (son en retard).

⚠️ CE QU'IL NE FAUT PAS LUI DEMANDER
    COMPARER DEUX CADRAGES. SyncNet n'est pas invariant a la translation : un
    visage decale dans le cadre change le score, et la litterature le dit.
    Il compare donc deux PRISES DU MEME PLAN -- ce qui est exactement l'usage
    qu'on en veut -- jamais un gros plan contre un plan moyen.

⚠️ OU VIT LE MODELE, ET POURQUOI PAS ICI
    Dans C:/Users/jacqu/.wortando/syncnet, hors du depot. Le depot est public
    et ces poids font 145 Mo : ils n'ont rien a y faire. Le code est de Joon
    Son Chung, sous licence MIT ; les poids viennent de VGG (Oxford).

    L'INSTALLATION SE VERIFIE, et c'est la premiere chose a faire :

        cd C:/Users/jacqu/.wortando/syncnet
        python demo_syncnet.py --videofile data/example.avi --tmp_dir <tmp>

    Le depot annonce AV offset 3, min dist 5.353, confiance 10.021. Mesure ici
    le 10 septembre 2026 : 3, 5.358, 10.081. Un outil de mesure dont on n'a
    pas verifie l'etalonnage ne mesure rien -- c'est la lecon des quatre fois
    ou notre mesure maison s'est trompee.
"""
import argparse
import glob
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNCNET = "C:/Users/jacqu/.wortando/syncnet"
IPS_SYNCNET = 25.0          # run_pipeline.py reechantillonne a 25 im/s

# Les seuils de l'UIT, en millisecondes. Positif = son en avance sur l'image.
ITU_DETECTABLE = (45.0, -125.0)


def verdict_offset(ms):
    haut, bas = ITU_DETECTABLE
    if ms > 0:
        seuil, sens = haut, "son en avance"
    elif ms < 0:
        seuil, sens = -bas, "son en retard"
    else:
        return "cale"
    x = abs(ms)
    if x <= seuil:
        return "%s, sous le seuil de detection" % sens
    return "%s, x%.1f du seuil de detection" % (sens, x / seuil)


def verdict_lse(d, c):
    """L'echelle publiee : 6 a 8 de LSE-D est l'etat de l'art."""
    if d <= 8.0:
        q = "dans la bande de l'etat de l'art (6-8)"
    elif d <= 10.0:
        q = "au-dessus de la bande de l'etat de l'art"
    else:
        q = "loin au-dessus : la bouche ne dit pas la voix"
    return "LSE-D %.3f %s ; LSE-C %.3f" % (d, q, c)


def a_du_son(clip):
    """Un clip muet n'est pas mesurable : autant le dire ici."""
    import imageio_ffmpeg
    r = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-i", clip],
                       capture_output=True, text=True, errors="replace")
    return "Audio:" in r.stderr


def mesurer(clip, garder=None):
    """(offset en images, LSE-D, LSE-C) pour un clip. None si aucun visage."""
    if not os.path.isdir(SYNCNET):
        sys.exit("  SyncNet introuvable dans %s.\n"
                 "  Voir l'en-tete de ce fichier : le modele vit hors du depot."
                 % SYNCNET)
    tmp = garder or tempfile.mkdtemp(prefix="syncnet-")
    ref = "mesure"
    try:
        for etape in ("run_pipeline.py", "run_syncnet.py"):
            r = subprocess.run(
                [sys.executable, etape, "--videofile", os.path.abspath(clip),
                 "--reference", ref, "--data_dir", tmp,
                 # ⚠️ NOS PLANS SONT PLUS COURTS QUE CE QUE SYNCNET ATTEND.
                 # Son defaut exige une piste de visage de 100 images -- quatre
                 # secondes a 25 im/s. Coupes a --queue 0.9, nos plans font 2,6
                 # a 4 s : le suivi les rejetait tous, et l'outil repondait
                 # « aucun visage suivi » sur des plans ou le visage occupe la
                 # moitie du cadre. Une seconde suffit a mesurer.
                 # run_syncnet.py, lui, ne connait pas cette option.
                 ] + (["--min_track", "25"] if etape == "run_pipeline.py" else []),
                cwd=SYNCNET, capture_output=True, text=True, errors="replace")
            if r.returncode != 0:
                print(r.stdout[-1500:]); print(r.stderr[-1500:])
                sys.exit("  echec de %s sur %s" % (etape, os.path.basename(clip)))
            sortie = r.stdout + r.stderr
        # run_syncnet.py imprime une ligne par piste de visage suivie ; on
        # garde la meilleure, c'est-a-dire la plus confiante.
        pistes = []
        for m in re.finditer(r"AV offset:\s*(-?\d+).*?Min dist:\s*([\d.]+)"
                             r".*?Confidence:\s*([\d.]+)", sortie, re.S):
            pistes.append((int(m.group(1)), float(m.group(2)), float(m.group(3))))
        if not pistes:
            return None
        return max(pistes, key=lambda x: x[2])
    finally:
        if not garder:
            shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--plan", type=int, help="mesure le plan synchronise, ou "
                                            "a defaut le clip de 03-final")
    ap.add_argument("--fichier", help="ou bien ce fichier-la")
    ap.add_argument("--tous", action="store_true",
                    help="tous les plans parlants de la scene")
    a = ap.parse_args()

    cibles = []
    if a.fichier:
        cibles = [(os.path.basename(a.fichier), a.fichier)]
    else:
        # ⚠️ LES CLIPS DE 03-final SONT MUETS. rapatrier.py coupe la piste de
        # Seedance a l'archivage : SyncNet n'a alors rien a comparer, et
        # ffmpeg echoue trois ecrans plus bas sur « Output file does not
        # contain any stream ».
        #
        # On mesure donc, dans l'ordre : le SEGMENT DE MONTAGE (l'image du
        # plan avec notre voix posee dessus -- c'est ce que le spectateur voit
        # et entend), sinon le plan synchronise. Un plan sans aucune des deux
        # n'est pas mesurable, et on le dit au lieu de planter.
        import json
        dv = os.path.join(RACINE, "video", "episode-" + a.scene)
        d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                              encoding="utf-8"))
        parlants = [p["n"] for p in d["plans"] if p["type"] == "replique"]
        nums = [a.plan] if a.plan else parlants
        for n in nums:
            # Le plan synchronise d'abord : il est ENTIER, la ou le segment
            # de montage est deja coupe a la queue -- moins d'images pour la
            # meme mesure, et sur les plans les plus courts ca compte.
            for etiquette, c in (("synchro", os.path.join(dv, "04-lipsync", "plan%02d.mp4" % n)),
                                 ("montage", os.path.join(dv, "_montage", "plan%02d.mp4" % n))):
                if os.path.exists(c) and a_du_son(c):
                    cibles.append(("plan%02d (%s)" % (n, etiquette), c))
                    break
            else:
                cibles.append(("plan%02d" % n, None))
        if not a.plan and not a.tous:
            sys.exit("  Preciser --plan N, --fichier F, ou --tous.")

    print("  %-22s %8s %8s %9s   %s"
          % ("clip", "offset", "LSE-D", "LSE-C", "verdict"))
    print("  " + "-" * 96)
    for nom, chemin in cibles:
        if chemin is None:
            print("  %-22s pas de clip sonore (03-final est muet : monter la"
                  " scene, ou synchroniser)" % nom)
            continue
        r = mesurer(chemin)
        if not r:
            print("  %-22s aucun visage suivi" % nom)
            continue
        img, d, c = r
        ms = img / IPS_SYNCNET * 1000.0
        print("  %-22s %+5d im %8.3f %9.3f   %s"
              % (nom, img, d, c, verdict_lse(d, c)))
        print("  %-22s %+8.0f ms %26s%s" % ("", ms, "", verdict_offset(ms)))


if __name__ == "__main__":
    main()
