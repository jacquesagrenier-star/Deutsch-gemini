# -*- coding: utf-8 -*-
"""Un plan de decor SANS MOUVEMENT, fabrique depuis son image. Gratuit.

    python video/plan_fixe.py --scene 03-auf-dem-radweg --plan 1 --duree 7.5

POURQUOI CET OUTIL EXISTE.

Jacques, 23 septembre 2026, alors que le solde fal etait a 1,31 $ et qu'une
reprise du plan 01 coutait 1,69 $ : << mais tu peux pas te servir seulement de
l'image ? Il n'y a pas de mouvement dans cette image-la. Donc pourquoi tu ne
prends pas juste l'image en premier plan ? >>

Il a raison, et c'etait mesurable dans notre propre feuille. Le PROMPT DE
MOUVEMENT du plan 01 dit en entier : << The red lens glows steadily. A few
leaves move on the pavement and a tram passes far away in the distance, small
and soft. The road stays empty. Hold on the stillness. >> Des feuilles et un
tram lointain -- rien qu'un spectateur remarque, sur un plan de six secondes
qui porte une narration. On payait 1,69 $ pour une immobilite.

⚠️ ET LA SERIE EST DEJA A CAMERA VERROUILLEE. Tous les plans sont fixes depuis
   l'episode 1, sinon les raccords ne tiennent pas entre deux plans generes
   separement. Une image tenue n'introduit donc aucune rupture de langage :
   elle est le cas limite de la regle, pas une exception.

⚠️ QUAND *NE PAS* S'EN SERVIR : QUAND UN VISAGE EST VISIBLE, ou quand un geste
   est le sujet du plan. Un visage parfaitement immobile pendant six secondes
   se lit comme un arret sur image, pas comme du calme -- il ne cligne pas, il
   ne respire pas.

   ⚠️ LA PREMIERE VERSION DE CETTE REGLE DISAIT << des qu'une personne est
      dans le cadre >>, ET C'ETAIT TROP LARGE. Jacques, 23 sept. 2026, sur le
      plan 17 : << l'avant-dernier plan n'a egalement que tres peu de
      mouvement, on pourrait tout simplement prendre cette image. >> Mark y
      est DE DOS, debout, immobile, a plusieurs metres. Aucun visage, aucun
      geste : la raison que ma propre regle donnait ne s'appliquait pas a
      elle. J'ai failli refuser en citant la lettre de la regle contre son
      motif.
      Le critere est donc : y a-t-il un VISAGE, ou un GESTE qui porte le plan ?
      Une nuque immobile est une nuque immobile, a l'image comme dans la rue.

⚠️ LES CARACTERISTIQUES SE RELEVENT SUR UN CLIP VOISIN, ELLES NE S'INVENTENT
   PAS. 720x1280, 24 im/s, yuv420p, h264 High : mesure le 23 sept. sur
   03-final/plan17.mp4. Un plan a 25 im/s ou en yuv444p se recoderait au
   montage, et le recodage d'un seul plan se voit comme une chute de qualite
   au milieu de l'episode.
"""
import argparse
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def caracteristiques(voisin):
    """Releve largeur, hauteur, cadence et format de pixel sur un clip voisin."""
    champs = "stream=width,height,r_frame_rate,pix_fmt"
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", champs, "-of", "default=nw=1", voisin],
                       capture_output=True, text=True)
    d = {}
    for ligne in r.stdout.splitlines():
        if "=" in ligne:
            k, v = ligne.split("=", 1)
            d[k.strip()] = v.strip()
    if "width" not in d:
        sys.exit("  impossible de relever %s" % voisin)
    return d


def main():
    p = argparse.ArgumentParser(
        description="Un plan de decor fixe, fabrique depuis son image.")
    p.add_argument("--scene", required=True)
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--duree", type=float, default=7.5,
                   help="un peu plus long que le besoin : le montage taille")
    p.add_argument("--image", help="l'image ; sinon celle nommee dans A-TOURNER")
    p.add_argument("--essai", action="store_true")
    a = p.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    if not os.path.isdir(ep):
        sys.exit("  scene introuvable : %s" % ep)

    image = a.image
    if not image:
        # Le nom vit dans A-TOURNER.txt, comme pour image_plan.py : le fichier
        # reste la source unique, on ne recopie pas un nom d'image ici.
        import re
        feuille = os.path.join(ep, "A-TOURNER.txt")
        with open(feuille, encoding="utf-8") as f:
            t = f.read()
        m = re.search(r"PLAN %02d\b.*?Image a nommer\s*:\s*(\S+)" % a.plan, t,
                      re.S)
        if not m:
            sys.exit("  A-TOURNER.txt ne nomme pas d'image pour le plan %02d"
                     % a.plan)
        image = os.path.join(ep, "01-images", m.group(1) + ".png")
    elif not os.path.isabs(image):
        image = os.path.join(RACINE, image)
    if not os.path.exists(image):
        sys.exit("  image introuvable : %s" % image)

    # Le voisin de reference : le plan final le plus proche qui existe.
    voisin = None
    for n in range(1, 21):
        c = os.path.join(ep, "03-final", "plan%02d.mp4" % n)
        if n != a.plan and os.path.exists(c):
            voisin = c
            break
    if not voisin:
        sys.exit("  aucun clip voisin dans 03-final pour relever les "
                 "caracteristiques.")
    d = caracteristiques(voisin)
    print("  image   : %s" % os.path.basename(image))
    print("  voisin  : %s -> %sx%s, %s im/s, %s"
          % (os.path.basename(voisin), d["width"], d["height"],
             d["r_frame_rate"].split("/")[0], d["pix_fmt"]))

    # ⚠️ UNE PRISE PAYEE NE S'ECRASE PAS -- et une prise gratuite non plus :
    #    elle porte le meme numero dans la suite, et retenir.py s'en sert.
    prises = os.path.join(ep, "02-prises")
    os.makedirs(prises, exist_ok=True)
    n = 1
    while os.path.exists(os.path.join(prises, "plan%02d-%02d.mp4" % (a.plan, n))):
        n += 1
    sortie = os.path.join(prises, "plan%02d-%02d.mp4" % (a.plan, n))
    print("  sortie  : %s  (%.2f s)" % (os.path.basename(sortie), a.duree))

    if a.essai:
        print("\n  (essai -- rien n'a ete ecrit)")
        return

    cadence = d["r_frame_rate"].split("/")[0]
    subprocess.run([
        "ffmpeg", "-loglevel", "error", "-y",
        "-loop", "1", "-i", image, "-t", "%.3f" % a.duree,
        "-r", cadence,
        "-vf", "scale=%s:%s:flags=lanczos" % (d["width"], d["height"]),
        "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
        "-preset", "medium", "-pix_fmt", d["pix_fmt"], "-an", sortie],
        check=True)
    ko = os.path.getsize(sortie) / 1024.0
    print("\n  -> %s  (%.0f ko, 0 $)" % (sortie, ko))
    print("  Ensuite : python video/retenir.py --scene %s --plan %d --prise %d"
          % (a.scene, a.plan, n))


if __name__ == "__main__":
    main()
