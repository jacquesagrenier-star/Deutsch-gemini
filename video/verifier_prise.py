# -*- coding: utf-8 -*-
"""Ce qui APPARAIT dans une prise et qui n'y etait pas au depart.

    python video/verifier_prise.py <clip.mp4>
    python video/verifier_prise.py --scene 02-beim-buergeramt

POURQUOI CET OUTIL EXISTE.

Le 16 septembre 2026, trois defauts de suite, tous de la meme famille : une
femme entre par le bord gauche ; une masse sombre s'installe dans un coin ;
une feuille se materialise dans les mains d'un homme qui ne l'a prise nulle
part. Chacun a ete trouve par L'OEIL DE JACQUES, jamais par une mesure.

⚠️ ET MES MESURES A LA MAIN ONT MANQUE LE DERNIER. J'avais mesure le plan 15
   dans une boite choisie a vue, annonce << plus rien qui apparait >>, et la
   feuille etait juste au-dessus de ma boite. Une mesure dont on choisit
   l'endroit ne prouve rien : elle prouve seulement qu'on a bien regarde la ou
   on regardait deja.

Ce script ne choisit rien. Il decoupe l'image en cases, compare chaque case a
la PREMIERE image, et dit lesquelles changent, quand, et si le changement
reste. Un personnage qui parle fait bouger sa tete et ses mains -- c'est
normal et ca revient. Un objet qui apparait, lui, ne revient pas : la case
change et RESTE changee jusqu'a la fin. C'est ce qu'on cherche.

⚠️ CE QU'IL NE SAIT PAS FAIRE : dire ce qui est apparu. Il dit ou et quand.
   L'oeil fait le reste -- mais il regarde alors au bon endroit.
"""
import argparse
import glob
import io
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COLS, LIGNES = 8, 14          # la grille sur l'image
LARGE, HAUT = 96, 168         # la taille a laquelle on reduit (multiple des cases)
SEUIL_PIXEL = 30              # ecart de gris qui compte comme un changement
SEUIL_CASE = 0.25             # part de la case qui doit changer
TENUE = 0.6                   # part du RESTE du plan ou le changement persiste


def gris(clip):
    """Toutes les images en niveaux de gris, reduites."""
    cmd = ["ffmpeg", "-v", "error", "-i", clip, "-vf",
           "format=gray,scale=%d:%d" % (LARGE, HAUT), "-f", "rawvideo", "-"]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        sys.exit("  ffmpeg a echoue sur %s" % clip)
    d = r.stdout
    n = len(d) // (LARGE * HAUT)
    return [d[i * LARGE * HAUT:(i + 1) * LARGE * HAUT] for i in range(n)], n


def cases_changees(a, b):
    """Les cases ou l'ecart depasse le seuil, entre deux images."""
    cw, ch = LARGE // COLS, HAUT // LIGNES
    out = set()
    for cy in range(LIGNES):
        for cx in range(COLS):
            n = 0
            for y in range(cy * ch, (cy + 1) * ch):
                base = y * LARGE
                for x in range(cx * cw, (cx + 1) * cw):
                    if abs(a[base + x] - b[base + x]) > SEUIL_PIXEL:
                        n += 1
            if n > SEUIL_CASE * cw * ch:
                out.add((cx, cy))
    return out


def verifier(clip, bavard=True):
    images, n = gris(clip)
    if n < 10:
        print("  %s : trop court" % os.path.basename(clip))
        return 0
    ref = images[0]
    changes = [cases_changees(ref, f) for f in images]

    # Une case qui change et RESTE changee jusqu'a la fin : quelque chose est
    # arrive et n'est pas reparti.
    suspects = []
    for cy in range(LIGNES):
        for cx in range(COLS):
            premiere = None
            for i, c in enumerate(changes):
                if (cx, cy) in c:
                    premiere = i
                    break
            if premiere is None or premiere < 3:
                continue          # jamais change, ou change des le debut
            reste = changes[premiere:]
            tenu = sum(1 for c in reste if (cx, cy) in c) / float(len(reste))
            if tenu >= TENUE:
                suspects.append((cx, cy, premiere / 25.0, tenu))

    if not suspects:
        if bavard:
            print("  %-26s rien n'apparait." % os.path.basename(clip))
        return 0

    print("  %s" % os.path.basename(clip))
    # On regroupe par instant d'apparition : un objet, c'est plusieurs cases
    # voisines qui s'allument ensemble.
    par_temps = {}
    for cx, cy, t, tenu in suspects:
        par_temps.setdefault(round(t, 1), []).append((cx, cy, tenu))
    for t in sorted(par_temps):
        g = par_temps[t]
        xs = [c[0] for c in g]
        ys = [c[1] for c in g]
        print("    a %4.1f s : %d case(s) s'allument et restent  "
              "-- colonnes %d-%d sur %d, lignes %d-%d sur %d"
              % (t, len(g), min(xs) + 1, max(xs) + 1, COLS,
                 min(ys) + 1, max(ys) + 1, LIGNES))
    print("    (colonne 1 = bord gauche, ligne 1 = haut de l'image)")
    return len(suspects)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clip", nargs="?")
    p.add_argument("--scene")
    a = p.parse_args()
    if a.scene:
        d = os.path.join(RACINE, "video", "episode-%s" % a.scene,
                         "_essai-avatar")
        clips = sorted(glob.glob(os.path.join(d, "plan*-omnihuman.mp4")))
        clips = [c for c in clips if "AVANT" not in c]
        total = sum(verifier(c) for c in clips)
    elif a.clip:
        total = verifier(a.clip)
    else:
        sys.exit("  Preciser un clip ou --scene NOM.")
    print()
    print("  %d case(s) suspecte(s). Une case qui s'allume tard et ne "
          "s'eteint plus\n  est un objet qui est apparu." % total)


if __name__ == "__main__":
    main()
