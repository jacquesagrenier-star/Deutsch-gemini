# -*- coding: utf-8 -*-
"""De quel COTE la bouche est-elle decalee ? Le signe, pas seulement l'ecart.

    python video/mesurer_decalage.py --scene 01-ankunft-berlin

CE QU'IL MESURE, ET POURQUOI LE SIGNE CHANGE TOUT
    On savait depuis le 9 septembre 2026 que Seedance ne place pas la voix ou
    on la lui donne : « decalage d'attaque de 0,35 s tres regulier ». On avait
    note l'AMPLITUDE et jamais la DIRECTION, faute de savoir qu'elle comptait.

    Elle compte. La recommandation UIT-R BT.1359-1, mesuree sur des sujets
    parlants, donne deux seuils qui ne sont pas symetriques :

        son en AVANCE sur l'image   detectable a  +45 ms   acceptable a  +90 ms
        son en RETARD  sur l'image  detectable a -125 ms   acceptable a -185 ms

    L'oeil pardonne pres de TROIS FOIS plus un son en retard qu'un son en
    avance. Le meme ecart de 0,35 s est donc un defaut moyen d'un cote et une
    faute grossiere de l'autre. Sans le signe, le chiffre ne se juge pas.

COMMENT ON L'OBTIENT
    La piste que Seedance GENERE est le seul temoin exact de sa machoire : les
    deux naissent dans la meme passe. On compare donc, sur chaque prise :

        la voix qu'on lui a DONNEE   (le mp3 ElevenLabs de 01-images)
        la voix qu'il a RENDUE       (sa piste generee)

    ⚠️ LA PISTE RENDUE N'EXISTE PLUS DANS LES CLIPS. rapatrier.py la coupe a
    l'archivage -- les prises de 02-prises sont muettes. C'est precisement
    pourquoi il la MESURE avant de la jeter et ecrit le resultat dans
    02-prises/_parole.json. Ce fichier est donc la seule trace de la machoire,
    et ce script le lit plutot que de rouvrir les clips. Une prise absente de
    ce fichier est une prise d'avant la mesure : elle ne peut plus etre jugee.

    ecart d'attaque = debut rendu - debut donne

        POSITIF  la machoire demarre APRES la voix qu'on posera au montage.
                 Au montage, le son arrive donc AVANT l'image : « son en
                 avance », le cote intolerant.
        NEGATIF  la machoire demarre avant : « son en retard », le cote
                 clement.

CE QU'IL NE MESURE PAS
    La qualite de l'articulation. Une machoire peut demarrer a l'heure et dire
    n'importe quoi -- c'est controler_bouche.py qui regarde le mouvement, et
    lui-meme ne juge pas la ressemblance. Ici on ne mesure que le CALAGE.

    Et il ne vaut que pour les prises tournees AVEC la voix en reference (a
    partir du 9 septembre 2026, 15 h 19). Avant, Seedance inventait les mots :
    comparer sa piste a la notre n'aurait aucun sens. Le script le signale.
"""
import argparse
import glob
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

# Les seuils de l'UIT-R BT.1359-1, en secondes. Positif = son en avance.
ITU_DETECTABLE = (0.045, -0.125)
ITU_ACCEPTABLE = (0.090, -0.185)

# La voix en reference n'existe qu'a partir de la (commit c7d906c).
DEPUIS = "2026-09-09 15:19"


def verdict(ecart):
    """Le mot que l'UIT met sur ce chiffre-la, dans ce sens-la."""
    haut, bas = (ITU_DETECTABLE if ecart >= 0 else (ITU_DETECTABLE[1], 0))
    d = ITU_DETECTABLE[0] if ecart >= 0 else -ITU_DETECTABLE[1]
    a = ITU_ACCEPTABLE[0] if ecart >= 0 else -ITU_ACCEPTABLE[1]
    x = abs(ecart)
    sens = "son en avance" if ecart > 0 else ("son en retard" if ecart < 0 else "cale")
    if x <= d:
        return "%-14s invisible" % sens
    if x <= a:
        return "%-14s visible, tolere (x%.1f du seuil)" % (sens, x / d)
    return "%-14s HORS NORME (x%.1f du seuil)" % (sens, x / d)


def numero(nom):
    base = os.path.basename(nom)
    return int(base[4:6]) if base.startswith("plan") else None


def reference(dossier_images, plan, duree_clip):
    """Le mp3 donne a Seedance pour ce plan : la variante la plus proche."""
    cands = sorted(glob.glob(os.path.join(dossier_images, "%02d-*.mp3" % plan)))
    if not cands:
        return None
    ff = M.ffmpeg()
    return min(cands, key=lambda c: abs((M.duree(ff, c) or 0) - duree_clip))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--json", help="ecrire le detail dans ce fichier")
    a = ap.parse_args()

    base = os.path.join(RACINE, "video", "episode-" + a.scene)
    prises = sorted(glob.glob(os.path.join(base, "02-prises", "plan*.mp4")))
    if not prises:
        sys.exit("aucune prise dans %s/02-prises" % base)
    images = os.path.join(base, "01-images")
    ff = M.ffmpeg()

    # Les prises tournees avec la voix en reference. rapatrier.py note leur
    # fenetre de bouche depuis le 9 septembre : c'est la liste sure.
    connues = {}
    pj = os.path.join(base, "02-prises", "_parole.json")
    if os.path.exists(pj):
        connues = json.load(io.open(pj, encoding="utf-8"))

    print("MESURE DU DECALAGE, AVEC LE SIGNE -- scene %s" % a.scene)
    print("positif = machoire APRES la voix = son en avance au montage")
    print("seuils UIT-R BT.1359-1 : avance +45 ms / retard -125 ms (detection)")
    print()
    print("%-16s %-17s %-17s %8s %8s   %s"
          % ("prise", "voix donnee", "voix rendue", "attaque", "duree", "verdict UIT"))
    print("-" * 108)

    lignes, detail = [], {}
    for p in prises:
        n = numero(p)
        if n is None:
            continue
        nom = os.path.basename(p)
        avec_reference = nom in connues
        dclip = M.duree(ff, p) or 0.0
        ref = reference(images, n, dclip)
        if not ref:
            continue
        if not avec_reference:
            continue
        s0, s1 = connues[nom]["bouche"]
        r0, r1, _ = M.parole_nette(ff, ref, seuil=0.04)
        if s1 <= s0 or r1 <= r0:
            continue
        attaque = s0 - r0
        etirement = (s1 - s0) - (r1 - r0)
        marque = " " if avec_reference else "~"
        lignes.append((marque, nom, r0, r1, s0, s1, attaque, etirement))
        detail[nom] = {"reference": os.path.basename(ref),
                       "donnee": [round(r0, 2), round(r1, 2)],
                       "rendue": [round(s0, 2), round(s1, 2)],
                       "attaque": round(attaque, 3),
                       "etirement": round(etirement, 3),
                       "voix_en_reference": avec_reference}
        print("%s%-15s %6.2f - %-8.2f %6.2f - %-8.2f %+8.3f %+8.3f   %s"
              % (marque, nom, r0, r1, s0, s1, attaque, etirement,
                 verdict(attaque) if avec_reference else "(sans reference)"))

    sures = [l for l in lignes if l[0] == " "]
    print()
    if not sures:
        print("Aucune prise tournee avec la voix en reference (depuis %s)." % DEPUIS)
        return
    ecarts = [l[6] for l in sures]
    moy = sum(ecarts) / len(ecarts)
    print("LES %d PRISES TOURNEES AVEC LA VOIX EN REFERENCE (depuis %s)"
          % (len(sures), DEPUIS))
    print("  attaque : de %+0.3f a %+0.3f s, moyenne %+0.3f s" %
          (min(ecarts), max(ecarts), moy))
    print("  %s" % verdict(moy))
    print()
    ecarte = max(ecarts) - min(ecarts)
    print()
    print("  ETENDUE : %0.3f s entre la plus petite et la plus grande." % ecarte)
    if ecarte > 0.2:
        print("  ⚠️ L'ecart n'est donc PAS une constante. Une compensation fixe")
        print("     de 0,35 s le corrigerait sur une prise et l'aggraverait sur")
        print("     une autre : il faut poser la voix sur la fenetre MESUREE de")
        print("     chaque prise, celle que rapatrier.py ecrit dans _parole.json.")

    if a.json:
        io.open(a.json, "w", encoding="utf-8").write(
            json.dumps(detail, ensure_ascii=False, indent=1))
        print("\n  detail ecrit dans %s" % a.json)


if __name__ == "__main__":
    main()
