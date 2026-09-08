# -*- coding: utf-8 -*-
"""La bouche suit-elle vraiment la voix ? Un chiffre, pas une impression.

    python video/controler_bouche.py --scene 01-ankunft-berlin
    python video/controler_bouche.py --fichier chemin/vers/un/plan.mp4

CE QU'IL MESURE
    Deux courbes, image par image : combien la zone de la bouche BOUGE, et
    combien la voix PORTE. Puis leur correlation. Si le lip-sync a fait son
    travail, les deux montent et descendent ensemble.

POURQUOI IL EXISTE
    Le 8 septembre 2026, Jacques sur l'episode monte : « il y a quand meme un
    petit decalage ». Le montage n'y etait pour rien -- image et son avaient
    la meme duree au centieme pres. La mesure a montre autre chose :

        plan 5, apres lip-sync, correlation 0,53
        la bouche fait son grand mouvement de 0,42 a 0,92 s
        la voix atteint son pic a 1,04 s, quand la bouche est deja retombee
        a 2,92 s la bouche rebouge, la voix est silencieuse depuis 0,4 s

    Le lip-sync REPEINT LA FORME DES LEVRES a l'interieur d'un mouvement de
    machoire qu'il ne retime pas. Si la machoire du clip source suit un
    charabia, le plan restera decale quoi qu'on fasse aux levres.

    Une impression ne se compare pas d'un essai a l'autre. Un chiffre, oui.

CE QU'IL NE SAIT PAS FAIRE -- MESURE LE SOIR MEME, ET C'EST UNE LIMITE
    Trois prises du plan 5, meme voix, meme image de depart, passees au meme
    lip-sync :

        0,53   Seedance parle du debut a la fin (la prise DEFECTUEUSE)
        0,40   trois phases minutees : ferme, parle, ferme
        0,09   bouche fermee des la fin de la replique

    La prise dont Jacques avait vu le defaut obtient la MEILLEURE note. La
    raison est mecanique : une bouche tres agitee pendant que la voix porte
    correle bien avec l'enveloppe sonore, meme si elle articule un charabia.
    Une bouche calme a peu de signal a correler.

    CE SCRIPT NE PEUT DONC PAS ARBITRER LA QUALITE D'UN LIP-SYNC. C'est
    l'oeil qui tranche, sur les clips cote a cote.

    Ce a quoi il sert encore, et ou il a ete decisif :
      - COMPARER une serie a elle-meme. Les douze plans allaient de 0,53 a
        -0,31 ; une correlation negative veut dire que la bouche bouge quand
        la voix se tait, et ca, c'est un fait, pas une echelle.
      - MESURER QUAND la bouche s'ouvre. C'est la courbe, pas la correlation.
        Elle a montre que Seedance OBEIT a un minutage explicite : demande
        << ferme 0-1 s, parle 1-3,5 s, ferme ensuite >>, le pic tombe a
        0,96 s et l'amplitude retombe apres 3,6 s. C'etait la question
        ouverte de la journee, et elle est reglee.

CE QU'IL NE DIT PAS
    Il ne juge pas la beaute d'un plan, ni si la bouche est CREDIBLE. Il dit
    si le mouvement et le son vont ensemble. Une bouche parfaitement immobile
    sur une voix qui parle donnerait une correlation basse elle aussi -- et ce
    serait juste, c'est bien un defaut.

LE CADRE DE MESURE
    On regarde un rectangle centre sur le bas du visage, dans nos cadrages
    verticaux 720x1280. Il vaut pour cette serie ; une autre mise en cadre
    demanderait d'autres coordonnees.
"""
import argparse
import glob
import io
import json
import os
import struct
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CADRE = "crop=340:240:190:320,scale=64:48,format=gray"     # le bas du visage
# LE SEUIL N'EST PAS ETALONNE, ET IL FAUT LE DIRE. 0,80 est un chiffre
# d'intuition : on n'a aucun lip-sync REUSSI a mesurer pour savoir ou tombe
# vraiment un bon plan avec cette methode. Ce qui est solide, c'est l'ORDRE et
# les valeurs proches de zero -- une correlation de -0,31 (plan 16) veut dire
# que la bouche bouge quand la voix se tait. Le premier plan retourne sous la
# regle BOUCHE etalonnera l'echelle : s'il monte franchement, la mesure vaut ;
# s'il reste a 0,5, c'est la mesure qui est trop grossiere, pas le plan.
SEUIL = 0.80


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def courbes(F, clip):
    """Renvoie (mouvement de la bouche, energie de la voix), une valeur par
    image, alignees."""
    n = 64 * 48
    r = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", clip, "-vf", CADRE, "-f", "rawvideo", "-"],
                       capture_output=True)
    img = [r.stdout[i * n:(i + 1) * n] for i in range(len(r.stdout) // n)]
    if len(img) < 8:
        return None, None
    bouche = [sum(abs(a - b) for a, b in zip(img[i], img[i - 1])) / float(n)
              for i in range(1, len(img))]

    a = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", clip, "-map", "0:a", "-ac", "1", "-ar", "24000",
                        "-f", "s16le", "-"], capture_output=True)
    if not a.stdout:
        return bouche, None
    ech = struct.unpack("<%dh" % (len(a.stdout) // 2), a.stdout)
    par = max(1, len(ech) // len(bouche))
    voix = [sum(abs(x) for x in ech[i * par:(i + 1) * par]) / float(par)
            for i in range(len(bouche))]
    return bouche, voix


def correlation(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = sum((a - mx) ** 2 for a in x) ** 0.5
    dy = sum((b - my) ** 2 for b in y) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--fichier", help="un seul clip, au lieu de toute la scene")
    a = ap.parse_args()

    F = ffmpeg()
    if a.fichier:
        clips = [a.fichier]
    else:
        d = os.path.join(RACINE, "video", "episode-" + a.scene, "04-lipsync")
        clips = sorted(glob.glob(os.path.join(d, "plan*.mp4")))
        if not clips:
            sys.exit("  Aucun plan synchronise dans %s." % os.path.relpath(d, RACINE))

    print("  correlation entre le mouvement de la bouche et la voix")
    print("  au-dessus de %.2f : la bouche suit. En dessous : elle vit sa vie.\n"
          % SEUIL)
    faibles = []
    for c in clips:
        bouche, voix = courbes(F, c)
        if not bouche or not voix:
            print("  %-14s pas de piste son" % os.path.basename(c))
            continue
        r = correlation(bouche, voix)
        marque = "" if r >= SEUIL else "   <- la bouche ne suit pas"
        print("  %-14s %.2f%s" % (os.path.basename(c), r, marque))
        if r < SEUIL:
            faibles.append((os.path.basename(c), r))

    if faibles:
        print("\n  %d plan(s) sous le seuil." % len(faibles))
        print("  Le lip-sync ne peut pas les sauver : il repeint les levres, il")
        print("  ne retime pas la machoire. C'est le clip source qu'il faut")
        print("  retourner -- voir le bloc BOUCHE dans scenes/production.py.")
    else:
        print("\n  Tous les plans suivent leur voix.")


if __name__ == "__main__":
    main()
