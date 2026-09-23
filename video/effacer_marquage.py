# -*- coding: utf-8 -*-
"""Effacer la peinture BLANCHE posee sur la bande rouge, sans repasser par fal.

    python video/effacer_marquage.py --dans a.mp4 --sortie b.mp4 --essai
    python video/effacer_marquage.py --dans a.mp4 --sortie b.mp4

POURQUOI CET OUTIL EXISTE, ET C'EST UN ARGUMENT D'HISTOIRE.

Jacques, 23 septembre 2026 : << peux-tu enlever les velos blancs partout sur
tous les plans [...] ca ne fait pas de sens que Mark n'ait pas compris qu'il ne
pouvait pas marcher sur la piste rouge alors qu'il y a des velos peints en
blanc. >>

Il a raison, et ca renverse ce qu'on venait de faire le meme jour -- j'avais
REPOSE un pictogramme sur il-attend.png a sa demande. Le pictogramme rend la
bande lisible ; or tout l'episode repose sur le fait que Mark ne la lit PAS. Un
velo peint au sol est un panneau : avec lui, le personnage n'est plus distrait,
il est bete. L'argument d'histoire passe avant la fidelite documentaire.

⚠️ ON TRAVAILLE PAR LA COULEUR *ET* PAR LE VOISINAGE, JAMAIS PAR LA GEOMETRIE.
   C'est la lecon de degriser_bande.py : il y a du MONDE devant la bande -- les
   jambes de Mark, ses espadrilles BLANCHES, un cycliste, un blouson jaune. Un
   rectangle passerait dessus.
   Mais la couleur seule ne suffit pas non plus : les barres de la traverse,
   les espadrilles et la facade creme sont blanches elles aussi. Le critere est
   donc << blanc ET CERNE DE ROUGE >> : on ne touche un pixel clair que si,
   dans plusieurs directions, on rencontre la bande rouge a quelques dizaines
   de pixels. Une espadrille est posee sur du gris et du pave ; une barre de
   traverse a du rouge d'UN cote. Un marquage sur la bande en a de partout.

⚠️ ET ON REBOUCHE LIGNE PAR LIGNE, JAMAIS AVEC UNE COULEUR UNIQUE. C'est la
   lecon d'agrandir_marquage.py : la bande palit, s'use, porte des traces et
   change de clarte avec la distance. Une couleur moyenne posee en aplat fait
   une tache qu'on voit tout de suite. On prend donc, POUR CHAQUE LIGNE, la
   mediane des pixels de bande de cette ligne-la.

⚠️ LE MASQUE SE RECALCULE A CHAQUE IMAGE. La camera est verrouillee, donc on
   serait tente de le calculer une fois. Mais quelqu'un PASSE devant la bande :
   un masque fige repeindrait du rouge sur une roue ou sur une jambe. Le test
   de couleur, lui, cesse tout seul d'etre vrai des qu'autre chose occupe le
   pixel -- c'est le contraire d'un detourage, c'est la matiere qui se designe
   elle-meme.
"""
import argparse
import os
import subprocess
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("  Il faut numpy : python -m pip install numpy")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mesures du 23 septembre 2026, sur les clips de l'episode 03.
ROUGE_RG = 30          # r-g : la bande est a 60-75, l'asphalte a 9-17
ROUGE_RB = 20
BLANC_L = 165          # clarte : la peinture blanche est a 190-250
BLANC_RG = 26          # et elle est desaturee


def dimensions(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries",
                        "stream=width,height,r_frame_rate,nb_frames",
                        "-of", "default=nw=1", clip],
                       capture_output=True, text=True)
    d = {}
    for ligne in r.stdout.splitlines():
        if "=" in ligne:
            k, v = ligne.split("=", 1)
            d[k.strip()] = v.strip()
    if "width" not in d:
        sys.exit("  impossible de lire %s" % clip)
    return int(d["width"]), int(d["height"]), d["r_frame_rate"]


def decale(m, n, axe):
    """Decale un masque de n pixels et remplit le bord de False.

    ⚠️ PAS np.roll : IL EST CIRCULAIRE, et ca s'est vu tout de suite. Premier
       essai du 23 sept. 2026 : un pixel clair du bord GAUCHE de l'image
       << voyait >> la bande rouge du bord DROIT, et la main de Mark s'est
       retrouvee dans le masque puis repeinte en rose. Un voisinage qui fait
       le tour de l'image n'est pas un voisinage.
    """
    out = np.zeros_like(m)
    if n == 0:
        return m.copy()
    if axe == 1:
        if n > 0:
            out[:, n:] = m[:, :-n]
        else:
            out[:, :n] = m[:, -n:]
    else:
        if n > 0:
            out[n:, :] = m[:-n, :]
        else:
            out[:n, :] = m[-n:, :]
    return out


def masque(img, rayon, cotes_min, sur_clair=16):
    """Les pixels de peinture cernes de bande rouge.

    ⚠️ LE CRITERE EST RELATIF A LA BANDE, PAS ABSOLU. Premiere version :
       << clair (L>165) et desature (r-g<26) >>. Elle attrapait les deux
       pointillets blancs francs et LAISSAIT LE VELO. Mesure du 23 sept. :
       le pictogramme de il-attend a ete COMPOSITE sur du rouge -- c'est un
       blanc ROSE, a r-g de l'ordre de 40, donc rejete par le seuil de
       desaturation. Un seuil absolu ne peut pas decrire << de la peinture sur
       du rouge >> : selon l'epaisseur, la peinture va du blanc franc au rose.
       On compare donc chaque pixel a la MEDIANE DE SA LIGNE dans la bande :
       est-il plus clair qu'elle, sans etre plus sature qu'elle ? C'est ce que
       << de la peinture posee dessus >> veut dire.
    """
    r = img[:, :, 0].astype(np.int16)
    g = img[:, :, 1].astype(np.int16)
    b = img[:, :, 2].astype(np.int16)
    clarte = 0.299 * r + 0.587 * g + 0.114 * b
    rg = r - g

    # ⚠️ ET LA PEAU EST ROUGE, ELLE AUSSI. C'est la cause racine de tous les
    #    faux positifs du 23 septembre 2026 -- la main, le pantalon, puis
    #    126 849 px de masque sur un GROS PLAN DE VISAGE. Un teint a
    #    (210,165,150) donne r-g = 45 : il passait le test de << bande rouge >>,
    #    donc les criteres de voisinage batis dessus n'avaient aucun sens.
    #    Ce qui les separe est le BLEU. Mesure sur la bande : (205,143,149),
    #    (211,144,153), (183,125,131) -- le bleu est toujours un peu AU-DESSUS
    #    du vert, g-b de -6 a -9 : c'est un rouge brique desature, presque
    #    mauve. Sur un teint, le bleu tombe sous le vert. Une seule condition
    #    de plus, g-b < 4, et la peau sort.
    rouge = (rg > ROUGE_RG) & (r - b > ROUGE_RB) & (g - b < 4)

    # Mediane de clarte et de rougeur, ligne par ligne, sur la bande seule.
    H = img.shape[0]
    med_l = np.zeros(H)
    med_rg = np.full(H, 60.0)
    for y in range(H):
        m = rouge[y]
        if m.sum() >= 24:
            med_l[y] = np.median(clarte[y][m])
            med_rg[y] = np.median(rg[y][m])
        else:
            med_l[y] = 1e9          # pas de bande sur cette ligne
    blanc = (clarte > med_l[:, None] + sur_clair) & (rg < med_rg[:, None] + 8)

    # Combien des quatre directions rencontrent la bande a `rayon` pixels ?
    cotes = np.zeros(rouge.shape, dtype=np.int8)
    cotes += decale(rouge, rayon, 1)       # du rouge a gauche
    cotes += decale(rouge, -rayon, 1)      # a droite
    cotes += decale(rouge, rayon, 0)       # au-dessus
    cotes += decale(rouge, -rayon, 0)      # au-dessous
    return blanc & (cotes >= cotes_min), rouge


def borner(cible, zone):
    """Restreint le masque a un rectangle, quand on en a un."""
    if not zone:
        return cible
    x0, y0, x1, y1 = [int(v) for v in zone.split(",")]
    m = np.zeros_like(cible)
    m[y0:y1, x0:x1] = cible[y0:y1, x0:x1]
    return m


def par_la_forme(cible, aire_max, remplissage_max):
    """Ne garde que les taches qui ONT LA FORME d'un marquage.

    ⚠️ NI TROIS NI QUATRE COTES NE SUFFISAIENT, et c'est ce qui a mene ici.
       Mesure du 23 sept. 2026 sur le plan 17 :
         - a 3 cotes sur 4, le PANTALON de Mark entrait dans le masque : son
           mollet longe la bande, donc trois directions rencontrent du rouge.
           Resultat : une trainee rose sur sa jambe et son polo.
         - a 4 cotes, le pantalon sortait mais le velo n'etait efface qu'a
           MOITIE -- et un glyphe a moitie efface est pire que les deux
           autres etats.
       Le nombre de cotes mesure le voisinage ; il ne dit rien de l'objet. Or
       ce qui distingue un marquage d'une jambe est sa FORME : un trait peint
       est fin (il remplit mal sa boite englobante) ou petit (une barre de
       pointille). Une jambe est une grande surface pleine. On etiquette donc
       les taches et on ne garde que celles qui sont petites OU creuses.
    """
    try:
        from scipy import ndimage
    except ImportError:
        return cible          # sans scipy, on garde tout : mieux vaut le dire
    lab, n = ndimage.label(cible)
    if n == 0:
        return cible
    garde = np.zeros(n + 1, dtype=bool)
    for i, tranche in enumerate(ndimage.find_objects(lab), start=1):
        aire = int((lab[tranche] == i).sum())
        boite = ((tranche[0].stop - tranche[0].start)
                 * (tranche[1].stop - tranche[1].start))
        if aire <= aire_max or aire / float(max(1, boite)) <= remplissage_max:
            garde[i] = True
    return garde[lab]


def dilater(m, n):
    """Elargit le masque de n pixels : la frange anti-crenelee doit partir."""
    for _ in range(n):
        m = (m | decale(m, 1, 0) | decale(m, -1, 0)
             | decale(m, 1, 1) | decale(m, -1, 1))
    return m


def reboucher_cv2(img, cible, rayon=4):
    """Rebouche par inpainting OpenCV. Meilleur que la mediane par ligne.

    ⚠️ ET C'EST JACQUES QUI A POSE LA QUESTION : << il n'y a pas des outils
       gratuits que tu peux utiliser pour faire ce genre de travail ? >>
       Oui, et il etait deja installe : cv2 5.0. J'avais ecrit un rebouchage a
       la main -- la mediane de bande, ligne par ligne -- qui laissait un
       FANTOME du glyphe, parce qu'une mediane ne reconstruit pas la texture,
       elle l'aplatit.
       La lecon est generale : le travail se coupait en deux, et une seule
       moitie etait a nous. DETECTER quels pixels sont de la peinture sur une
       bande cyclable, aucune bibliotheque ne le sait -- c'est la logique de
       couleur du fichier. REBOUCHER un trou dans une photo, c'est un probleme
       resolu depuis vingt ans, et le reecrire etait du temps perdu et un
       resultat moins bon. Avant d'ecrire un traitement d'image, regarder ce
       qui est deja installe.
    """
    import cv2
    bgr = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2BGR)
    m = (cible.astype(np.uint8)) * 255
    out = cv2.inpaint(bgr, m, rayon, cv2.INPAINT_TELEA)
    return cv2.cvtColor(out, cv2.COLOR_BGR2RGB).astype(np.int16), int(cible.sum())


def reboucher(img, cible, rouge):
    """Remplace les pixels cibles par la mediane de bande DE LEUR LIGNE."""
    out = img.copy()
    fond = rouge & ~cible
    lignes = np.where(cible.any(axis=1))[0]
    if not len(lignes):
        return out, 0
    # Mediane globale de secours, pour une ligne sans assez de bande.
    if fond.any():
        secours = np.median(img[fond], axis=0)
    else:
        return out, 0
    for y in lignes:
        pix = img[y][fond[y]]
        couleur = np.median(pix, axis=0) if len(pix) >= 12 else secours
        out[y][cible[y]] = couleur
    return out, int(cible.sum())


def fond_median(clip, L, H, n=13):
    """Le decor du plan, SANS personne : la mediane par pixel dans le temps.

    ⚠️ C'EST LA CLE DE TOUT, ET ELLE VIENT D'UNE PROPRIETE DE LA SERIE : la
       camera est VERROUILLEE dans tous les plans depuis l'episode 1. Un pixel
       donne montre donc le meme point du decor pendant toute la duree -- sauf
       quand quelqu'un passe devant. Sur une quinzaine de trames, la mediane
       par pixel garde le decor et jette le passant : une jambe, une roue, un
       blouson jaune n'occupent ce pixel que sur une minorite des trames.
       On detecte donc le marquage sur une image OU PERSONNE NE LE CACHE, au
       lieu de se battre image par image avec des occlusions. Deux heures de
       reglages de seuils evitees par une propriete du tournage.
    """
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", clip, "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    total = len(brut) // (L * H * 3)
    if total == 0:
        sys.exit("  clip vide : %s" % clip)
    pas = max(1, total // n)
    idx = list(range(0, total, pas))[:n]
    pile = np.stack([
        np.frombuffer(brut[i * L * H * 3:(i + 1) * L * H * 3],
                      dtype=np.uint8).reshape(H, L, 3) for i in idx])
    return np.median(pile, axis=0).astype(np.int16), total


def main():
    p = argparse.ArgumentParser(
        description="Effacer la peinture blanche posee sur une bande rouge.")
    p.add_argument("--dans", required=True)
    p.add_argument("--sortie")
    p.add_argument("--rayon", type=int, default=40,
                   help="a quelle distance on cherche la bande, en px")
    p.add_argument("--cotes", type=int, default=3,
                   help="combien des 4 directions doivent trouver du rouge")
    p.add_argument("--dilate", type=int, default=2)
    p.add_argument("--mediane", action="store_true",
                   help="reboucher a la mediane par ligne au "
                        "lieu de l inpainting OpenCV (moins bon, "
                        "garde pour comparer)")
    p.add_argument("--zone",
                   help="x0,y0,x1,y1 -- n'effacer QUE dans ce rectangle. Sur "
                        "un plan FIXE la bande ne bouge pas : borner la zone "
                        "met tout le reste du cadre hors d'atteinte, ce qu'un "
                        "seuil de couleur ne garantira jamais.")
    p.add_argument("--aire", type=int, default=900,
                   help="une tache plus petite que ca est gardee "
                        "quelle que soit sa forme")
    p.add_argument("--remplissage", type=float, default=0.32,
                   help="au-dela de ce taux de remplissage de sa "
                        "boite, une grande tache est rejetee")
    p.add_argument("--sur-clair", type=int, default=16,
                   dest="sur_clair",
                   help="de combien un pixel doit depasser la "
                        "clarte mediane de la bande sur sa ligne")
    p.add_argument("--essai", action="store_true",
                   help="ecrit trois images -- avant, masque, apres -- et "
                        "n'encode aucune video. A REGARDER AVANT DE LANCER.")
    p.add_argument("--a", type=float, default=1.0,
                   help="l'instant de la trame d'essai, en secondes")
    a = p.parse_args()

    dans = a.dans if os.path.isabs(a.dans) else os.path.join(RACINE, a.dans)
    if not os.path.exists(dans):
        sys.exit("  introuvable : %s" % dans)
    L, H, cadence = dimensions(dans)
    print("  %s  %dx%d  %s im/s" % (os.path.basename(dans), L, H,
                                    cadence.split("/")[0]))
    print("  rayon %d px, %d cotes sur 4, dilatation %d px"
          % (a.rayon, a.cotes, a.dilate))

    if a.essai:
        from PIL import Image
        brut = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", "%.3f" % a.a, "-i", dans,
             "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
            capture_output=True).stdout
        img = np.frombuffer(brut, dtype=np.uint8)[:L * H * 3].reshape(H, L, 3)
        cible, rouge = masque(img, a.rayon, a.cotes, a.sur_clair)
        cible = borner(cible, a.zone)
        cible = par_la_forme(cible, a.aire, a.remplissage)
        cible = dilater(cible, a.dilate)
        f_rebouche = reboucher if a.mediane else (
            lambda i, c, r: reboucher_cv2(i, c))
        out, n = f_rebouche(img.astype(np.int16), cible, rouge)
        vue = img.copy()
        vue[cible] = [0, 255, 0]
        base = os.path.join(os.path.dirname(dans) or ".", "_essai-effacer")
        Image.fromarray(img).save(base + "-avant.png")
        Image.fromarray(vue).save(base + "-masque.png")
        Image.fromarray(out.astype(np.uint8)).save(base + "-apres.png")
        print("\n  %d pixels dans le masque" % n)
        print("  ecrit : %s-avant.png, -masque.png, -apres.png" % base)
        print("  (essai -- aucune video encodee)")
        return

    if not a.sortie:
        sys.exit("  --sortie manque (ou passe --essai).")
    sortie = a.sortie if os.path.isabs(a.sortie) else os.path.join(RACINE, a.sortie)

    lecture = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-i", dans, "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    # ⚠️ L'AUDIO SE RECOPIE DEPUIS LA SOURCE, IL NE SE REENCODE PAS. Le
    #    montage porte la narration : la reencoder a chaque passe la degraderait
    #    en cascade, et personne ne saurait d'ou vient la perte.
    ecriture = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (L, H),
         "-r", cadence, "-i", "-",
         "-i", dans,
         "-map", "0:v", "-map", "1:a?",
         "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
         "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "copy", "-shortest", sortie], stdin=subprocess.PIPE)

    taille = L * H * 3
    n_img, n_px = 0, 0
    while True:
        brut = lecture.stdout.read(taille)
        if len(brut) < taille:
            break
        img = np.frombuffer(brut, dtype=np.uint8).reshape(H, L, 3)
        cible, rouge = masque(img, a.rayon, a.cotes, a.sur_clair)
        cible = borner(cible, a.zone)
        if cible.any():
            cible = par_la_forme(cible, a.aire, a.remplissage)
            cible = dilater(cible, a.dilate)
            f_rebouche = reboucher if a.mediane else (
                lambda i, c, r: reboucher_cv2(i, c))
            out, n = f_rebouche(img.astype(np.int16), cible, rouge)
            n_px += n
            ecriture.stdin.write(out.astype(np.uint8).tobytes())
        else:
            ecriture.stdin.write(brut)
        n_img += 1
        if n_img % 200 == 0:
            print("    %d images" % n_img)
    ecriture.stdin.close()
    lecture.wait()
    ecriture.wait()
    print("\n  %d images, %d pixels repeints (%.0f par image)"
          % (n_img, n_px, n_px / max(1, n_img)))
    print("  -> %s" % sortie)


if __name__ == "__main__":
    main()
