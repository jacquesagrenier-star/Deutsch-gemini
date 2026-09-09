# -*- coding: utf-8 -*-
"""Chaque prise part-elle de la bonne image, et dure-t-elle le bon temps ?

    python video/verifier_prises.py                    # les prises rangees
    python video/verifier_prises.py --telechargements  # avant de ranger

POURQUOI CE CONTROLE EXISTE
    Le 9 septembre 2026, un re-tournage de douze plans s'est fait dans un seul
    panneau Artlist : on change le prompt, on change la Start Frame, on relance.
    Deux fois, un des deux champs n'a pas suivi -- une image de plan 15 animee
    avec le prompt de neuf secondes du plan 13. Le clip existe, il est beau, il
    ne va nulle part.

    Rien ne signale ce defaut. Le nom du fichier telecharge vient du prompt, pas
    du plan ; la duree seule ne suffit pas (huit plans durent 5 s) ; et l'oeil
    confond deux cadrages voisins d'Anna a trois heures d'intervalle.

CE QUI IDENTIFIE UNE PRISE
    Sa PREMIERE IMAGE. Seedance part de la Start Frame et la rend presque telle
    quelle : la comparer aux images de depart donne un ecart franc -- 25 a 28 dB
    pour la bonne, 13 a 16 dB pour toutes les autres. Il n'y a pas de zone
    grise, donc pas de jugement a rendre.

    La duree confirme, elle n'arbitre pas.

CE QU'IL NE JUGE PAS
    La bouche fermee a la fin, le regard, le naturel du geste. Ce controle dit
    que la prise est CELLE QU'ON A DEMANDEE, pas qu'elle est bonne.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = (".mp4", ".mov", ".webm", ".m4v")
# En dessous, l'image de depart n'est pas reconnaissable ; au-dessus, elle est
# franche. Les mesures du 9 septembre : bonne image 25,0 a 28,1 dB, mauvaise
# 13,1 a 17,0 dB. Le seuil est pose au milieu du vide.
SEUIL = 21.0


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("  ffmpeg introuvable. Il vient avec le paquet imageio-ffmpeg.")


def duree(F, f):
    r = subprocess.run([F, "-i", f], capture_output=True, text=True,
                       errors="ignore")
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", r.stderr or "")
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def premiere_image(F, video, sortie):
    subprocess.run([F, "-y", "-v", "error", "-i", video, "-vframes", "1",
                    sortie], capture_output=True)
    return sortie


def ecart(F, a, b):
    """PSNR moyen entre deux images ramenees a la meme taille, en dB."""
    r = subprocess.run(
        [F, "-i", a, "-i", b, "-lavfi",
         "[1:v]scale=1080:1920,format=yuv420p[y];"
         "[0:v]scale=1080:1920,format=yuv420p[x];[x][y]psnr",
         "-f", "null", "-"],
        capture_output=True, text=True, errors="ignore")
    m = re.search(r"average:([\d.]+)", r.stderr or "")
    return float(m.group(1)) if m else 0.0


def attendus(scene):
    """Ce que la feuille de re-tournage demande : image de depart et duree.

    La feuille est la source, pas une table recopiee ici -- c'est elle que
    Jacques a sous les yeux quand il lance les generations.
    """
    f = os.path.join(RACINE, "video", "episode-" + scene, "A-REFAIRE.txt")
    if not os.path.exists(f):
        sys.exit("  Pas de feuille de re-tournage : %s" % os.path.relpath(f, RACINE))
    texte = io.open(f, encoding="utf-8").read()
    table = {}
    for bloc in texte.split("\nPLAN ")[1:]:
        n = int(bloc[:2])
        d = re.search(r"GENERER A (\d+) SECONDES", bloc)
        i = re.search(r"Start Frame : (\S+)", bloc)
        table[n] = (i.group(1) if i else None, int(d.group(1)) if d else None)
    return table


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scene", default="01-ankunft-berlin")
    p.add_argument("--telechargements", action="store_true",
                   help="regarde les fichiers pas encore ranges")
    p.add_argument("--depuis", default="2026-09-09",
                   help="ne juger que les prises rangees a partir de ce jour")
    a = p.parse_args()

    F = ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    dim = os.path.join(ep, "01-images")
    tmp = os.path.join(ep, "_montage", "_identif")
    os.makedirs(tmp, exist_ok=True)
    table = attendus(a.scene)

    refs = [f for f in sorted(os.listdir(dim))
            if f.endswith(".png") and "16x9" not in f]

    if a.telechargements:
        base = os.path.expanduser("~")
        dl = None
        for nom in ("Downloads", "Telechargements", u"Téléchargements"):
            if os.path.isdir(os.path.join(base, nom)):
                dl = os.path.join(base, nom)
                break
        if not dl:
            sys.exit("  Dossier de telechargement introuvable.")
        clips = [(None, os.path.join(dl, f)) for f in sorted(
            os.listdir(dl), key=lambda x: os.path.getmtime(os.path.join(dl, x)))
            if f.lower().endswith(VIDEOS)]
        # Que ceux du jour : le dossier en garde des dizaines.
        import time
        limite = time.mktime(time.strptime(a.depuis, "%Y-%m-%d"))
        clips = [c for c in clips if os.path.getmtime(c[1]) >= limite]
    else:
        pr = os.path.join(ep, "02-prises")
        clips = []
        import time
        limite = time.mktime(time.strptime(a.depuis, "%Y-%m-%d"))
        for f in sorted(os.listdir(pr)):
            if not f.lower().endswith(VIDEOS):
                continue
            c = os.path.join(pr, f)
            if os.path.getmtime(c) < limite:
                continue
            m = re.match(r"plan(\d+)-", f)
            clips.append((int(m.group(1)) if m else None, c))

    if not clips:
        print("  Rien a verifier.")
        return 0

    defauts = 0
    for n, chemin in clips:
        nom = os.path.basename(chemin)
        d = duree(F, chemin)
        img = premiere_image(F, chemin, os.path.join(tmp, "courante.png"))
        notes = sorted(((ecart(F, img, os.path.join(dim, r)), r) for r in refs),
                       reverse=True)
        note, trouvee = notes[0]
        # ⚠️ DEUX IMAGES DE DEPART PEUVENT ETRE LA MEME PHOTO. mark-moyen et
        # mark-moyen-serre-b sont a 39,7 dB l'une de l'autre : deux tirages du
        # meme cadrage. Le PSNR les note a 23,8 et 23,7 -- il ne tranche pas, et
        # un script qui tranche quand meme accuse une prise correcte. On dit
        # « indiscernable », et c'est la feuille qui decide.
        proches = [r for v, r in notes if note - v < 2.0]

        if note < SEUIL:
            print("  %-34s  aucune image de depart reconnue (%.1f dB au mieux,"
                  " %s)" % (nom, note, trouvee))
            defauts += 1
            continue

        # De quel plan cette image de depart est-elle celle ? Une image
        # indiscernable d'une autre ouvre la porte aux deux plans.
        candidats = [k for k, (i, _) in table.items() if i in proches]

        if n is None:
            # ⚠️ LA DUREE SE VERIFIE MEME QUAND L'IMAGE DESIGNE UN SEUL PLAN.
            # Le 9 septembre, un clip parti de anna-moyen-serre-c (plan 15,
            # 5 s) durait 9 s : le panneau Artlist avait garde le prompt du
            # plan 13. Une premiere version de ce script disait « plan 15 » et
            # passait a la suite -- la prise aurait ete rangee.
            duree_ok = [k for k in candidats
                        if abs(d - (table[k][1] or 0)) < 0.3]
            if duree_ok:
                verdict = "plan %s" % " ou ".join("%02d" % k for k in duree_ok)
            elif candidats:
                verdict = ("MELANGE : image du plan %s, mais %.2f s au lieu"
                           " de %s s -- a jeter"
                           % (" ou ".join("%02d" % k for k in candidats), d,
                              " ou ".join(str(table[k][1]) for k in candidats)))
                defauts += 1
            else:
                verdict = "%s : aucun plan ne demande cette image" % trouvee
                defauts += 1
            print("  %-34s  %.2f s  %-24s  %s" % (nom, d, trouvee, verdict))
            continue

        attendu_img, attendu_duree = table.get(n, (None, None))
        ecarts = []
        if attendu_img and attendu_img not in proches:
            ecarts.append("IMAGE : %s au lieu de %s" % (trouvee, attendu_img))
        if attendu_duree and abs(d - attendu_duree) > 0.3:
            ecarts.append("DUREE : %.2f s au lieu de %d s" % (d, attendu_duree))
        if ecarts:
            defauts += 1
            print("  %-16s  %s" % (nom, " ; ".join(ecarts)))
        else:
            confusion = ""
            if len(proches) > 1:
                confusion = "   (indiscernable de %s)" % ", ".join(
                    r for r in proches if r != attendu_img)
            print("  %-16s  ok   %s   %.2f s   (%.1f dB)%s"
                  % (nom, attendu_img or trouvee, d, note, confusion))

    print()
    if defauts:
        print("  %d prise(s) a refaire ou a jeter." % defauts)
        return 1
    print("  Les %d prises partent de l'image demandee et durent ce qu'il faut."
          % len(clips))
    print("  (ce controle ne dit rien de la bouche ni du jeu)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
