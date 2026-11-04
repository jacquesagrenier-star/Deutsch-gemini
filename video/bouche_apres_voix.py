# -*- coding: utf-8 -*-
"""La bouche s'arrete-t-elle avec la voix ? Le controle a passer sur CHAQUE clip parle, avant publication. GRATUIT.

    python video/bouche_apres_voix.py video/episode-dtz-oral/_essai-avatar/plan??-kling.mp4
    python video/bouche_apres_voix.py --planche bouches.jpg <clips...>      (+ une planche des bouches, a REGARDER)
    python video/bouche_apres_voix.py --couper <dossier> <clips...>          (+ les clips coupes au repos de la bouche)

POURQUOI IL EXISTE
    4 nov. 2026, Jacques sur l'essai de l'oral du DTZ (Kling Avatar v2) : dans la premiere video, << Guten Tag und
    herzlich willkommen... >>, la bouche d'Anna continue de bouger apres la fin de sa replique. Les paniers de Kling
    portent 1,3 s de silence apres la voix (preparer_clips.py : la marge dont la bouche a besoin pour se refermer) ;
    Kling la remplit parfois d'une articulation muette. texte_incruste.py et la planche de 8 images ne le voient pas :
    une image fixe ne montre pas qu'une bouche bouge.

CE QU'IL MESURE
    1. La FIN DE LA VOIX, lue sur la piste du clip : la derniere tranche de 20 ms a moins de 30 dB sous le pic.
    2. La BOUCHE, image par image. Le visage hoche et glisse : on suit le NEZ (qui ne se deforme pas) par
       correspondance d'image, et la case de la bouche suit le nez. Le mouvement d'une image a l'autre dans cette
       case, ramene a celui du nez, ne garde que ce que fait la bouche.
    3. Le verdict : la bouche est << au repos >> quand son mouvement retombe sous le tiers de sa mediane pendant la
       parole. Elle doit l'etre au plus tard MARGE secondes apres la voix. Sinon : BOUGE, avec l'instant ou elle
       s'arrete vraiment (ou << jusqu'a la fin >>).

LA CORRECTION GRATUITE (--couper)
    La page s'arrete sur la derniere image du clip (onended) : couper le clip suffit. On coupe a la premiere image
    apres la voix ou la bouche est la plus proche de son image de depart (bouche fermee de l'image maitresse), dans
    les 0,4 s qui suivent la voix -- jamais avant la fin de la voix. Le son est coupe au meme instant.
    Pour l'oral du DTZ, publier_medias.py fait cette coupe lui-meme a chaque publication (point_de_coupe()) : la
    queue muette de 1,3 s ne sert qu'a Kling, jamais a l'eleve.

    MESURE LE 4 NOV. 2026 sur les 23 clips de l'oral : 19 bougeaient apres la voix (de 0,4 a 3,5 s : levres qui
    s'entrouvrent, articulation muette, grand sourire), parfois jusqu'a la derniere image. Le prompt avait pourtant
    sa queue << Finally, ... listens without speaking >> (verifier_prompt.py fin-sans-intention) : elle garde le
    visage vivant, elle ne ferme pas la bouche. D'ou la coupe, systematique.

CE QU'IL NE SAIT PAS
    Il ne juge pas si la bouche ARTICULE juste pendant la parole (voir controler_bouche.py et syncnet.py) : il dit
    seulement si elle bouge quand la voix s'est tue. Les positions de la bouche sont celles de NOS cadrages
    (BOUCHES) : un cadrage neuf demande d'y ajouter la sienne, ou --bouche x,y. Il regarde aussi les YEUX pour choisir la coupe (CASE_YEUX), pas pour le verdict. ET LA PLANCHE SE REGARDE : le chiffre
    trie, l'oeil tranche (le detecteur de texte s'est trompe dans les deux sens, verifier_prompt.py texte-incruste).
"""
import argparse
import os
import re
import struct
import subprocess
import sys

import cv2
import numpy as np

# La bouche a le droit de finir de se refermer pendant ce temps apres la voix. 0,4 s, MESURE le 4 nov. 2026 sur les
# 23 clips coupes de l'oral du DTZ, regardes image par image : les levres se referment en 2 a 5 images (Mark, plan 13 :
# 0,17 s) puis le sourire se pose (plan 22 : 0,32 s sans articuler). Le defaut que Jacques a vu durait 2 s.
MARGE = 0.4
CASE_BOUCHE = (150, 80)   # largeur, hauteur de la case de la bouche, en pixels du clip 720 x 1280
CASE_NEZ = (110, 70)
ECART_NEZ = 85        # le nez est a ~85 px au-dessus de la bouche dans nos cadrages
CHERCHE = 40          # de combien le nez peut glisser d'une image a l'autre

CASE_YEUX = (240, 60)
# Ou est la bouche (x, y), en pixels du clip 720 x 1280, selon l'image de depart, et de combien les yeux sont
# au-dessus d'elle.
BOUCHES = {
    "anna-dtz": (366, 620, 115),
    "anna-dtz-recadre": (356, 824, 155),   # oral du DTZ, plans 23-25, recadres au-dessus de faux sous-titres
    "mark-dtz": (390, 530, 140),
}
RECADRES = {("dtz-oral", 23), ("dtz-oral", 24), ("dtz-oral", 25)}


def ffmpeg(*args, **kw):
    return subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True, **kw)


def fin_de_voix(clip):
    """L'instant (s) ou la voix se tait : la derniere tranche de 20 ms a moins de 30 dB sous le pic."""
    r = ffmpeg("-i", clip, "-map", "0:a", "-ac", "1", "-ar", "16000", "-f", "s16le", "-", capture_output=True)
    ech = np.frombuffer(r.stdout, dtype="<i2").astype(np.float32)
    t = 320
    rms = np.sqrt(np.array([np.mean(ech[i:i + t] ** 2) for i in range(0, len(ech) - t, t)]) + 1e-9)
    seuil = rms.max() * 10 ** (-30 / 20.0)
    fortes = np.nonzero(rms > seuil)[0]
    return (fortes[-1] + 1) * t / 16000.0, (fortes[0]) * t / 16000.0


def image_de_depart(clip):
    """Le nom de l'image maitresse (anna-dtz, mark-dtz...), lu dans le panier _a-televerser du plan."""
    d = os.path.dirname(os.path.abspath(clip))
    m = re.match(r"plan(\d+)", os.path.basename(clip))
    scene = os.path.basename(os.path.dirname(d)).replace("episode-", "")
    tel = os.path.join(os.path.dirname(d), "_a-televerser")
    nom = None
    if m and os.path.isdir(tel):
        for f in os.listdir(tel):
            mm = re.match(r"plan%s-(.+)\.jpg$" % m.group(1), f)
            if mm:
                nom = mm.group(1)
    if m and (scene, int(m.group(1))) in RECADRES:
        nom = (nom or "") + "-recadre"
    return nom


def case(img, cx, cy, l, h):
    x0, y0 = int(cx - l / 2), int(cy - h / 2)
    return img[max(0, y0):y0 + h, max(0, x0):x0 + l]


def mesurer(clip, bouche):
    cap = cv2.VideoCapture(clip)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    imgs = []
    while True:
        ok, im = cap.read()
        if not ok:
            break
        imgs.append(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32))
    cap.release()
    bx, by, dy_yeux = bouche
    nx, ny = bx, by - ECART_NEZ
    modele = case(imgs[0], nx, ny, *CASE_NEZ)
    ref_bouche = case(imgs[0], bx, by, *CASE_BOUCHE)
    ref_yeux = case(imgs[0], bx, by - dy_yeux, *CASE_YEUX)
    pos, mouv, ecart_depart, nez = [], [0.0], [], [0.0]
    for i, im in enumerate(imgs):
        if i:
            zone = case(im, nx, ny, CASE_NEZ[0] + 2 * CHERCHE, CASE_NEZ[1] + 2 * CHERCHE)
            res = cv2.matchTemplate(zone, modele, cv2.TM_SQDIFF)
            _, _, mn, _ = cv2.minMaxLoc(res)
            x0 = int(nx - (CASE_NEZ[0] + 2 * CHERCHE) / 2)
            y0 = int(ny - (CASE_NEZ[1] + 2 * CHERCHE) / 2)
            nx2 = max(0, x0) + mn[0] + CASE_NEZ[0] / 2.0
            ny2 = max(0, y0) + mn[1] + CASE_NEZ[1] / 2.0
            bx, by = bx + nx2 - nx, by + ny2 - ny
            nx, ny = nx2, ny2
        pos.append((bx, by))
        b = case(im, bx, by, *CASE_BOUCHE)
        y = case(im, bx, by - dy_yeux, *CASE_YEUX)
        # L'image ou s'arreter ressemble a l'image de depart : bouche fermee ET yeux ouverts (une coupe sur un
        # clignement fige la page sur des yeux clos -- vu le 4 nov. sur a_ihr_foto et m_ende).
        if b.shape == ref_bouche.shape and y.shape == ref_yeux.shape:
            ecart_depart.append(float(np.mean(np.abs(b - ref_bouche)) + 2 * np.mean(np.abs(y - ref_yeux))))
        else:
            ecart_depart.append(float("inf"))
        if i:
            pb = case(imgs[i - 1], pos[i - 1][0], pos[i - 1][1], *CASE_BOUCHE)
            if pb.shape == b.shape:
                mouv.append(float(np.mean(np.abs(b - pb))))
            else:
                mouv.append(mouv[-1])
            pn = case(imgs[i - 1], pos[i - 1][0], pos[i - 1][1] - ECART_NEZ, *CASE_NEZ)
            cn = case(im, bx, by - ECART_NEZ, *CASE_NEZ)
            nez.append(float(np.mean(np.abs(cn - pn))) if pn.shape == cn.shape else nez[-1])
    # Ce que fait la bouche seule : son mouvement moins celui du nez (le grain, la lumiere, le glissement residuel).
    propre = [max(0.0, m - n) for m, n in zip(mouv, nez)]
    return fps, imgs, pos, propre, ecart_depart


def lisse(x, k=3):
    return [float(np.mean(x[max(0, i - k // 2):i + k // 2 + 1])) for i in range(len(x))]


def juger(clip, bouche):
    fin, debut = fin_de_voix(clip)
    fps, imgs, pos, propre, ecart = mesurer(clip, bouche)
    m = lisse(propre)
    i_deb, i_fin = int(debut * fps), int(fin * fps)
    parole = sorted(m[i_deb:i_fin]) or [1.0]
    med = parole[len(parole) // 2]
    repos = med / 3.0
    # Le dernier instant ou la bouche bouge encore franchement apres la voix.
    apres = [i for i in range(i_fin, len(m)) if m[i] > repos]
    dernier = (apres[-1] + 1) / fps if apres else fin
    duree = len(imgs) / fps
    retard = max(0.0, dernier - fin)
    bouge = retard > MARGE
    # La coupe : l'image, entre 0,08 et 0,4 s apres la voix, ou la bouche ressemble le plus a son image de depart
    # (les 0,08 s gardent la fin de la derniere syllabe, que le seuil de -30 dB rogne).
    fen = range(i_fin + int(0.08 * fps), min(len(imgs), i_fin + int(0.4 * fps) + 1))
    i_coupe = min(fen, key=lambda i: ecart[i]) if len(fen) else len(imgs) - 1
    return {"clip": clip, "fps": fps, "fin": fin, "debut": debut, "duree": duree, "retard": retard,
            "bouge": bouge, "jusqu_a_la_fin": bool(apres) and apres[-1] >= len(m) - 2, "med": med,
            "coupe": (i_coupe + 1) / fps, "imgs": imgs, "pos": pos, "m": m}


def planche(resultats, sortie):
    """Une ligne par clip : la bouche toutes les 2 images, de 0,3 s avant la fin de la voix a la fin du clip."""
    lignes = []
    for r in resultats:
        fps, i0 = r["fps"], max(0, int((r["fin"] - 0.3) * r["fps"]))
        vignettes = []
        for i in range(i0, len(r["imgs"]), 2):
            b = case(r["imgs"][i], r["pos"][i][0], r["pos"][i][1], *CASE_BOUCHE).astype(np.uint8)
            if b.shape != (CASE_BOUCHE[1], CASE_BOUCHE[0]):
                b = cv2.resize(b, CASE_BOUCHE)
            b = cv2.cvtColor(b, cv2.COLOR_GRAY2BGR)
            t = i / fps
            # Un trait rouge sous les images d'apres la voix, vert sous celles ou elle parle encore.
            cv2.rectangle(b, (0, CASE_BOUCHE[1] - 5), (CASE_BOUCHE[0], CASE_BOUCHE[1]),
                          (0, 0, 220) if t > r["fin"] else (0, 170, 0), -1)
            vignettes.append(b)
        rang = np.hstack(vignettes[:22])
        tete = np.full((22, rang.shape[1], 3), 255, np.uint8)
        etat = "BOUGE %.2f s apres la voix" % r["retard"] if r["bouge"] else "au repos"
        cv2.putText(tete, "%s  voix -> %.2f s  %s" % (os.path.basename(r["clip"]), r["fin"], etat), (4, 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        lignes.append(np.vstack([tete, rang]))
    l = max(x.shape[1] for x in lignes)
    lignes = [np.hstack([x, np.full((x.shape[0], l - x.shape[1], 3), 255, np.uint8)]) for x in lignes]
    cv2.imwrite(sortie, np.vstack(lignes))


def point_de_coupe(clip):
    """(instant de coupe, fin de la voix, retard de la bouche) pour un clip de nos cadrages : ce que publie la page."""
    nom = image_de_depart(clip)
    if nom not in BOUCHES:
        raise SystemExit("  %s : cadrage inconnu (%s), ajouter sa bouche a BOUCHES" % (clip, nom))
    r = juger(clip, BOUCHES[nom])
    return r["coupe"], r["fin"], r["retard"]


def couper(r, dossier):
    os.makedirs(dossier, exist_ok=True)
    sortie = os.path.join(dossier, os.path.basename(r["clip"]))
    ffmpeg("-i", r["clip"], "-t", "%.3f" % r["coupe"], "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", sortie)
    return sortie


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clips", nargs="+")
    ap.add_argument("--planche")
    ap.add_argument("--couper", metavar="DOSSIER")
    ap.add_argument("--bouche", help="x,y de la bouche, pour un cadrage absent de BOUCHES")
    a = ap.parse_args()
    resultats, mauvais = [], 0
    for c in a.clips:
        if a.bouche:
            b = tuple(int(v) for v in a.bouche.split(",")) + (120,)
        else:
            nom = image_de_depart(c)
            if nom not in BOUCHES:
                sys.exit("  %s : cadrage inconnu (%s), ajouter sa bouche a BOUCHES ou passer --bouche x,y" % (c, nom))
            b = BOUCHES[nom]
        r = juger(c, b)
        resultats.append(r)
        mauvais += r["bouge"]
        etat = ("BOUGE  %.2f s apres la voix%s" % (r["retard"], ", jusqu'a la fin" if r["jusqu_a_la_fin"] else "")
                if r["bouge"] else "au repos")
        print("  %-24s voix %.2f-%.2f s / clip %.2f s   %-40s coupe a %.2f s"
              % (os.path.basename(c), r["debut"], r["fin"], r["duree"], etat, r["coupe"]))
        if a.couper:
            couper(r, a.couper)
    if a.planche:
        planche(resultats, a.planche)
        print("  planche : %s  -- A REGARDER : le chiffre trie, l'oeil tranche" % a.planche)
    print("  %d clip(s) sur %d ou la bouche bouge apres la voix" % (mauvais, len(resultats)))


if __name__ == "__main__":
    main()
