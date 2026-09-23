# -*- coding: utf-8 -*-
"""Effacer le velo peint d'UN plan, avec un etalonnage propre a ce plan.

    python video/velo_un_plan.py --scene 03-auf-dem-radweg --plan 12 --grille
    python video/velo_un_plan.py --scene 03-auf-dem-radweg --plan 12 --zone 40,1180,360,1500 --essai
    python video/velo_un_plan.py --scene 03-auf-dem-radweg --plan 12 --zone 40,1180,360,1500

POURQUOI UN PLAN A LA FOIS, ET PAS UNE PASSE AUTOMATIQUE.

Mesure du 23 septembre 2026, au centre de la bande :
    plan 06 : (173, 96, 84)   r-g = 77   g-b = +12   un rouge brique chaud
    plan 17 :                 r-g = 60-70 g-b = -7   un rose presque mauve
**La bande n'a pas la meme couleur d'un plan a l'autre**, parce que chaque clip
a ete rendu separement par Seedance. Et la peau tombe entre les deux. Six
criteres globaux ont echoue avant que je mesure ca -- voir le journal des
retours du 23 septembre.

Un etalonnage global est donc impossible. Un etalonnage PAR PLAN, lui, est
facile : dans une boite posee sur la bande, la peinture est simplement ce qui
est nettement plus clair que le revetement autour, et il n'y a plus ni peau ni
vetement ni facade dans le champ du test.

⚠️ LA BOITE SE LIT SUR UNE GRILLE, ELLE NE SE DEVINE PAS. --grille ecrit le
   fond median avec un quadrillage de 100 px et ses coordonnees. J'ai perdu
   trois essais a placer des boites au jugement, dont un qui recadrait a cote
   de la bande.

⚠️ ET LE FOND MEDIAN EST CE QUI REND TOUT CECI SUR. La camera est verrouillee :
   la mediane par pixel dans le temps garde le decor et jette les passants. On
   etalonne donc sur une image ou personne ne cache la bande, puis on ne
   rebouche, image par image, que les pixels qui ressemblent ENCORE au fond.
"""
import argparse
import os
import subprocess
import sys

import numpy as np

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import effacer_marquage as EM                              # noqa: E402


def grille(img, pas=100):
    from PIL import Image, ImageDraw
    im = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(im)
    L, H = im.size
    for x in range(0, L, pas):
        d.line([(x, 0), (x, H)], fill=(0, 255, 255), width=1)
        d.text((x + 3, 4), str(x), fill=(0, 255, 255))
    for y in range(0, H, pas):
        d.line([(0, y), (L, y)], fill=(0, 255, 255), width=1)
        d.text((4, y + 3), str(y), fill=(0, 255, 255))
    return im


def masque_zone(fond, zone, marge, rg_min=13):
    """Ce qui est nettement plus clair que la bande, DANS la boite ET sur la bande.

    ⚠️ LE RECTANGLE NE SUFFIT PAS : IL FAUT L'INTERSECTER AVEC CE QUI EST
       ROUGEATRE. Mesure du 23 septembre 2026, plans 08 et 10 : mes rectangles
       debordaient de quelques dizaines de pixels au-dessus de la piste, et le
       BETON du trottoir -- clair et gris -- passait le seuil de clarte. Le
       masque s'est pose sur le trottoir et le velo est reste. Deux essais
       perdus a replacer le rectangle plus finement, alors que le defaut
       n'etait pas sa position mais son principe.
       Le beton est gris (r-g de 5 a 10), la peinture blanche sur du rouge
       garde un reste de rouge (r-g de 15 a 45). Une condition r-g > 13 sort
       donc le trottoir sans toucher au glyphe, et la boite peut rester large.

    ⚠️ ET LE NIVEAU DU SOL SE MESURE SUR LA BANDE SEULE, pas sur la boite. Une
       boite qui contient du trottoir a une mediane tiree vers le haut, donc un
       seuil trop severe, donc un velo a moitie efface.
    """
    x0, y0, x1, y1 = zone
    r = fond[:, :, 0].astype(np.int16)
    v = fond[:, :, 1].astype(np.int16)
    b = fond[:, :, 2].astype(np.int16)
    clarte = 0.299 * r + 0.587 * v + 0.114 * b
    rg = r - v

    m = np.zeros(clarte.shape, dtype=bool)
    boite = np.zeros(clarte.shape, dtype=bool)
    boite[y0:y1, x0:x1] = True
    bande = boite & (rg > 20) & (r - b > 15)
    if bande.sum() < 200:
        return m, 0.0
    niveau = float(np.median(clarte[bande]))
    m = boite & (clarte > niveau + marge) & (rg > rg_min)
    return m, niveau


def main():
    p = argparse.ArgumentParser(
        description="Effacer le velo peint d'un plan, etalonne sur ce plan.")
    p.add_argument("--scene", required=True)
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--zone", help="x0,y0,x1,y1 lus sur --grille")
    p.add_argument("--marge", type=float, default=22.0,
                   help="de combien la peinture depasse le sol, en clarte")
    p.add_argument("--dilate", type=int, default=3)
    p.add_argument("--ecart", type=int, default=30,
                   help="au-dela de cet ecart au fond, quelque chose est "
                        "devant : on ne touche pas")
    p.add_argument("--grille", action="store_true",
                   help="ecrire le fond median quadrille, et s'arreter")
    p.add_argument("--essai", action="store_true",
                   help="ecrire avant/masque/apres, n'encoder aucune video")
    a = p.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    clip = os.path.join(ep, "_montage-avatar", "plan%02d.mp4" % a.plan)
    if not os.path.exists(clip):
        sys.exit("  introuvable : %s" % clip)
    L, H, cadence = EM.dimensions(clip)
    fond, n_img = EM.fond_median(clip, L, H)
    base = os.path.join(ep, "_velo-plan%02d" % a.plan)
    print("  plan %02d : %dx%d, %d images" % (a.plan, L, H, n_img))

    if a.grille or not a.zone:
        grille(fond).save(base + "-grille.png")
        print("  -> %s-grille.png" % base)
        if not a.zone:
            print("  (pose --zone x0,y0,x1,y1 lue sur la grille)")
        return

    zone = [int(v) for v in a.zone.split(",")]
    m, niveau = masque_zone(fond, zone, a.marge)
    m = EM.dilater(m, a.dilate)
    print("  sol de la boite : clarte %.1f ; seuil %.1f ; masque %d px"
          % (niveau, niveau + a.marge, int(m.sum())))

    if a.essai:
        from PIL import Image
        out, _ = EM.reboucher_cv2(fond.astype(np.int16), m)
        vue = fond.astype(np.uint8).copy()
        vue[m] = [0, 255, 0]
        x0, y0, x1, y1 = zone
        mx, my = 90, 90
        b = (max(0, x0 - mx), max(0, y0 - my), min(L, x1 + mx), min(H, y1 + my))
        trio = Image.new("RGB", ((b[2] - b[0]) * 3, b[3] - b[1]))
        for i, src in enumerate((fond.astype(np.uint8), vue,
                                 out.astype(np.uint8))):
            trio.paste(Image.fromarray(src).crop(b), ((b[2] - b[0]) * i, 0))
        trio.save(base + "-trio.png")
        print("  -> %s-trio.png   (avant | masque | apres)" % base)
        return

    sortie = clip + ".neuf.mp4"
    lecture = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-i", clip, "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    ecriture = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", "%dx%d" % (L, H), "-r", cadence, "-i", "-", "-i", clip,
         "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-profile:v", "high",
         "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "copy", "-shortest", sortie], stdin=subprocess.PIPE)
    taille = L * H * 3
    n = 0
    while True:
        brut = lecture.stdout.read(taille)
        if len(brut) < taille:
            break
        img = np.frombuffer(brut, dtype=np.uint8).reshape(H, L, 3)
        proche = np.abs(img.astype(np.int16) - fond).max(axis=2) <= a.ecart
        cible = m & proche
        if cible.any():
            out, _ = EM.reboucher_cv2(img.astype(np.int16), cible)
            ecriture.stdin.write(out.astype(np.uint8).tobytes())
        else:
            ecriture.stdin.write(brut)
        n += 1
    ecriture.stdin.close()
    lecture.wait()
    ecriture.wait()
    os.replace(sortie, clip)
    print("  -> clip reecrit (%d images)" % n)


if __name__ == "__main__":
    main()
