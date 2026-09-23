# -*- coding: utf-8 -*-
"""Effacer les velos peints de TOUS les plans d'un episode, sans repasser par fal.

    python video/effacer_velos.py --scene 03-auf-dem-radweg --essai
    python video/effacer_velos.py --scene 03-auf-dem-radweg

POURQUOI, ET C'EST UN ARGUMENT D'HISTOIRE.

Jacques, 23 septembre 2026 : << peux-tu enlever les velos blancs partout sur
tous les plans [...] ca ne fait pas de sens que Mark n'ait pas compris qu'il ne
pouvait pas marcher sur la piste rouge alors qu'il y a des velos peints en
blanc. >> Puis : << il y a des velos a peu pres sur tous les plans, donc il
faudrait vraiment s'en debarrasser. >>

Un velo peint au sol est un panneau. Tout l'episode repose sur le fait que Mark
ne lit pas la bande ; avec le pictogramme, il n'est plus distrait, il est bete.

CE QUI A MARCHE, APRES CE QUI N'A PAS MARCHE.

⚠️ 1. REGLER DES SEUILS IMAGE PAR IMAGE NE CONVERGEAIT PAS. Le critere
      << clair et cerne de rouge >> attrapait le PANTALON de Mark a trois
      cotes sur quatre (son mollet longe la bande) et ne prenait le velo qu'a
      moitie a quatre cotes. Un glyphe a moitie efface est pire que les deux.
      J'ai perdu plusieurs tours a tourner ces boutons.

⚠️ 2. LA CAMERA EST VERROUILLEE, ET CA CHANGE TOUT. C'est une propriete de la
      serie depuis l'episode 1. Un pixel montre donc le meme point du decor
      pendant tout le plan, sauf quand quelqu'un passe devant. La MEDIANE PAR
      PIXEL sur une quinzaine de trames garde le decor et jette le passant.
      On detecte donc le marquage sur une image ou PERSONNE ne le cache, et le
      probleme des occlusions disparait au lieu de se regler.

⚠️ 3. ET L'OCCLUSION SE GERE A LA POSE, PAS A LA DETECTION. Le masque est
      statique -- le marquage ne bouge pas -- mais on ne rebouche un pixel que
      s'il ressemble ENCORE au fond a cette trame-la. Une jambe, une roue, un
      blouson devant le glyphe s'ecartent du fond : on les laisse tranquilles.
      C'est un test de difference, pas un detourage.

⚠️ 4. LE REBOUCHAGE EST A OPENCV, PAS A MOI. Jacques : << il n'y a pas des
      outils gratuits que tu peux utiliser pour ce genre de travail ? >> Oui,
      et cv2 etait deja installe. Ma mediane de bande ligne par ligne laissait
      un FANTOME parfaitement lisible du velo. cv2.inpaint n'en laisse rien.
      Le travail se coupait en deux et une seule moitie etait a nous :
      DETECTER de la peinture sur une bande cyclable, aucune bibliotheque ne
      le sait ; REBOUCHER un trou dans une photo est resolu depuis vingt ans.
"""
import argparse
import os
import subprocess
import sys

import numpy as np

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import effacer_marquage as EM                              # noqa: E402


def glyphes(fond, sur_clair=10, erosion=18, aire_bande=20000, dilate=3):
    """Le masque du marquage : de la peinture claire DANS l'interieur de la bande.

    ⚠️ CE N'EST PLUS UN TEST DE VOISINAGE, ET C'EST TOUT L'INTERET. Les
       versions precedentes demandaient << du rouge sur 3 ou 4 cotes a 22 px >>.
       Trois tours passes a regler ce chiffre : a 3 le pantalon de Mark entrait,
       a 4 le velo sortait a moitie. Le defaut n'etait dans aucun des deux
       reglages -- il etait dans l'idee. Un voisinage local ne sait pas dire
       << sur la bande >>.

       La bonne formulation vient de Jacques : << le blanc sur la piste
       rouge >>. Donc :
         1. on prend la ou les GRANDES regions rouges -- la bande, pas un
            vetement ni une joue (la peau est deja exclue par g-b < 4) ;
         2. on les ERODE de 18 px, ce qui donne l'INTERIEUR de la bande ;
         3. on n'efface que la peinture claire dans cet interieur.

       L'erosion fait un travail de plus, gratuitement : les pointillets de
       BORD de la piste -- qui sont un vrai marquage de rue, present aussi au
       plan 18 -- tombent hors de l'interieur et sont donc epargnes. Seul ce
       qui est peint AU MILIEU de la bande part, c'est-a-dire le velo.
    """
    from scipy import ndimage
    r = fond[:, :, 0].astype(np.int16)
    g = fond[:, :, 1].astype(np.int16)
    b = fond[:, :, 2].astype(np.int16)
    clarte = 0.299 * r + 0.587 * g + 0.114 * b
    rouge = (r - g > EM.ROUGE_RG) & (r - b > EM.ROUGE_RB) & (g - b < 4)

    # Ne garder que les grandes regions : la bande, pas une tache de couleur.
    lab, n = ndimage.label(rouge)
    if n == 0:
        return np.zeros(rouge.shape, dtype=bool), rouge
    tailles = ndimage.sum(rouge, lab, index=np.arange(1, n + 1))
    grandes = np.zeros(n + 1, dtype=bool)
    grandes[1:] = tailles >= aire_bande
    bande = grandes[lab]
    if not bande.any():
        return np.zeros(rouge.shape, dtype=bool), rouge

    interieur = ndimage.binary_erosion(bande, iterations=erosion)
    if not interieur.any():
        return np.zeros(rouge.shape, dtype=bool), rouge

    # ⚠️ LE SEUIL SE CHOISIT PAR PLAN, IL NE SE FIXE PAS. Mesure du 23 sept.
    #    2026 : a << mediane + 10 >>, la bande du plan 07 entrait en entier
    #    (96 265 px) parce que son revetement varie fort dans une meme ligne ;
    #    a << + 30 >>, les velos LAVES des plans 12, 18 et 19 disparaissaient du
    #    masque. Aucune valeur ne marche partout, parce que le contraste du
    #    pictogramme va du blanc franc au rose pale selon le plan.
    #    Otsu, lui, cherche la coupure NATURELLE entre deux populations dans
    #    l'histogramme de CE plan-la : la bande et ce qui est peint dessus. Le
    #    seuil devient une mesure et non un reglage.
    vals = clarte[interieur]
    if len(vals) < 500:
        return np.zeros(clarte.shape, dtype=bool), bande
    import cv2
    v8 = np.clip(vals, 0, 255).astype(np.uint8)
    seuil_otsu, _ = cv2.threshold(v8, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Un plancher : sans peinture, Otsu coupe quand meme la bande en deux.
    seuil_otsu = max(seuil_otsu, float(np.median(vals)) + 14.0)
    clair = (clarte > seuil_otsu) & interieur

    # ⚠️ ET LA CLASSE CLAIRE DOIT ETRE UNE MINORITE. Un plan sans pictogramme
    #    existe : la moitie de la bande au-dessus du seuil ne veut pas dire
    #    << la moitie est peinte >>, ca veut dire << il n'y a rien a effacer >>.
    part = clair.sum() / float(interieur.sum())
    if part > 0.14:
        return np.zeros(clarte.shape, dtype=bool), bande
    return EM.dilater(clair, dilate), bande


def main():
    p = argparse.ArgumentParser(
        description="Effacer les velos peints de tous les plans d'un episode.")
    p.add_argument("--scene", required=True)
    p.add_argument("--plans", help="8,9,12 -- sinon tous ceux du montage")
    p.add_argument("--erosion", type=int, default=18,
                   help="de combien on rentre dans la bande")
    p.add_argument("--aire-bande", type=int, default=20000,
                   dest="aire_bande",
                   help="taille minimale d une region rouge pour etre prise "
                        "pour la bande")
    p.add_argument("--sur-clair", type=int, dest="sur_clair", default=12)
    p.add_argument("--aire", type=int, default=700)
    p.add_argument("--remplissage", type=float, default=0.30)
    p.add_argument("--dilate", type=int, default=3)
    p.add_argument("--part-rouge", type=float, default=0.60,
                   dest="part_rouge",
                   help="proportion de rouge exigee dans la "
                        "couronne autour de chaque tache")
    p.add_argument("--ecart", type=int, default=26,
                   help="au-dela de cet ecart au fond, on considere que "
                        "quelque chose est devant et on ne touche pas")
    p.add_argument("--essai", action="store_true",
                   help="dit combien de pixels par plan et n'encode rien")
    a = p.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    dossier = os.path.join(ep, "_montage-avatar")
    if not os.path.isdir(dossier):
        sys.exit("  pas de montage : %s" % dossier)

    if a.plans:
        nums = [int(v) for v in a.plans.split(",")]
    else:
        nums = sorted(int(f[4:6]) for f in os.listdir(dossier)
                      if f.startswith("plan") and f.endswith(".mp4"))

    print("  %d plan(s) a examiner" % len(nums))
    total_px = 0
    for n in nums:
        clip = os.path.join(dossier, "plan%02d.mp4" % n)
        if not os.path.exists(clip):
            continue
        L, H, cadence = EM.dimensions(clip)
        fond, n_img = EM.fond_median(clip, L, H)
        m, _bande = glyphes(fond, a.sur_clair, a.erosion,
                            a.aire_bande, a.dilate)
        if m.sum() < 120:
            print("   plan %02d : rien de marque (%d px) -- laisse tel quel"
                  % (n, int(m.sum())))
            continue
        ys, xs = np.where(m)
        print("   plan %02d : %6d px   boite x %d..%d y %d..%d"
              % (n, int(m.sum()), xs.min(), xs.max(), ys.min(), ys.max()))
        total_px += int(m.sum())
        if a.essai:
            continue

        sortie = clip + ".neuf.mp4"
        lecture = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-i", clip, "-f", "rawvideo",
             "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        ecriture = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo",
             "-pix_fmt", "rgb24", "-s", "%dx%d" % (L, H), "-r", cadence,
             "-i", "-", "-i", clip, "-map", "0:v", "-map", "1:a?",
             "-c:v", "libx264", "-profile:v", "high", "-crf", "17",
             "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy",
             "-shortest", sortie], stdin=subprocess.PIPE)
        taille = L * H * 3
        while True:
            brut = lecture.stdout.read(taille)
            if len(brut) < taille:
                break
            img = np.frombuffer(brut, dtype=np.uint8).reshape(H, L, 3)
            # Quelque chose est-il devant ? On compare au fond.
            proche = (np.abs(img.astype(np.int16) - fond).max(axis=2)
                      <= a.ecart)
            cible = m & proche
            if cible.any():
                out, _ = EM.reboucher_cv2(img.astype(np.int16), cible)
                ecriture.stdin.write(out.astype(np.uint8).tobytes())
            else:
                ecriture.stdin.write(brut)
        ecriture.stdin.close()
        lecture.wait()
        ecriture.wait()
        os.replace(sortie, clip)
        print("      -> reecrit (%d images)" % n_img)

    print("\n  %d pixels de marquage au total" % total_px)
    if a.essai:
        print("  (essai -- aucun clip reecrit)")
    else:
        print("  Ensuite : resonoriser et re-sous-titrer -- le montage muet")
        print("  EPISODE-03-avatar.mp4 doit etre refait depuis les clips.")


if __name__ == "__main__":
    main()
