# -*- coding: utf-8 -*-
"""Choisit la prise retenue de chaque plan et la porte dans 03-final.

    python video/retenir.py --plans 5,6,8,9,10,11,12,13,14,15,16,17
    python video/retenir.py --plan 13 --prise 6
    python video/retenir.py --plans 5,6 --essai      # dit sans rien ecrire

POURQUOI CE SCRIPT EXISTE
    03-final est le dossier ou puisent lipsync.py et montage.py. Jusqu'au
    9 septembre 2026 on y copiait les prises a la main, et RIEN NE DISAIT
    laquelle s'y trouvait : plan13.mp4 pouvait etre la premiere prise comme la
    sixieme. Au moment de juger un lip-sync rate, la question « on a synchro
    quelle prise, deja ? » n'avait pas de reponse.

    Chaque copie ecrit donc sa ligne dans 03-final/_retenues.txt : le plan, la
    prise, son empreinte, la date, et ce qui etait la avant.

CE QU'IL VERIFIE AVANT DE COPIER
    Que la prise part de l'image de depart demandee et dure ce qu'il faut --
    la meme mesure que video/verifier_prises.py. Une prise melangee (l'image
    d'un plan avec le prompt d'un autre) ne doit pas pouvoir entrer dans le
    montage par une faute de frappe.

CE QU'IL NE JUGE PAS
    La bouche, le regard, le jeu. Sans --prise, il prend la DERNIERE prise
    conforme du plan -- ce qui est presque toujours la bonne, puisqu'on refait
    une prise quand la precedente ne va pas. Presque n'est pas toujours :
    quand une prise ancienne etait meilleure, il faut la nommer.
"""
import argparse
import hashlib
import io
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import verifier_prises as V                                 # noqa: E402


def empreinte(f):
    h = hashlib.md5()
    with open(f, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--plans", help="5,6,8...")
    ap.add_argument("--plan", type=int)
    ap.add_argument("--prise", type=int,
                    help="le numero de la prise, sinon la derniere conforme")
    ap.add_argument("--essai", action="store_true",
                    help="dit ce qu'il ferait, n'ecrit rien")
    a = ap.parse_args()

    if a.plan:
        voulus = [a.plan]
    elif a.plans:
        voulus = [int(x) for x in a.plans.replace(" ", "").split(",") if x]
    else:
        sys.exit("  Preciser --plan ou --plans.")
    if a.prise and len(voulus) != 1:
        sys.exit("  --prise ne vaut que pour un seul plan.")

    F = V.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    pr, fin = os.path.join(ep, "02-prises"), os.path.join(ep, "03-final")
    dim = os.path.join(ep, "01-images")
    tmp = os.path.join(ep, "_montage", "_identif")
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(fin, exist_ok=True)
    table = V.attendus(a.scene)
    refs = [f for f in sorted(os.listdir(dim))
            if f.endswith(".png") and "16x9" not in f]

    par_plan = {}
    for f in sorted(os.listdir(pr)):
        m = re.match(r"plan(\d+)-(\d+)\.mp4$", f)
        if m:
            par_plan.setdefault(int(m.group(1)), []).append((int(m.group(2)), f))

    gestes, refus = [], []
    for n in voulus:
        prises = par_plan.get(n, [])
        if not prises:
            refus.append("plan %02d : aucune prise dans 02-prises" % n)
            continue
        if a.prise:
            choix = [f for k, f in prises if k == a.prise]
            if not choix:
                refus.append("plan %02d : pas de prise %02d" % (n, a.prise))
                continue
            candidats = [choix[0]]
        else:
            candidats = [f for _, f in sorted(prises, reverse=True)]

        attendu_img, attendu_duree = table.get(n, (None, None))
        retenu = None
        for f in candidats:
            c = os.path.join(pr, f)
            d = V.duree(F, c)
            img = V.premiere_image(F, c, os.path.join(tmp, "retenir.png"))
            notes = sorted(((V.ecart(F, img, os.path.join(dim, r)), r)
                            for r in refs), reverse=True)
            note, trouvee = notes[0]
            proches = [r for v, r in notes if note - v < 2.0]
            mal = []
            if attendu_img and attendu_img not in proches:
                mal.append("part de %s au lieu de %s" % (trouvee, attendu_img))
            if attendu_duree and abs(d - attendu_duree) > 0.3:
                mal.append("dure %.2f s au lieu de %d s" % (d, attendu_duree))
            if mal:
                if a.prise:
                    refus.append("plan %02d : %s -- %s" % (n, f, " ; ".join(mal)))
                continue
            retenu = (f, d, trouvee, note)
            break
        if not retenu:
            if not a.prise:
                refus.append("plan %02d : aucune prise conforme parmi %d"
                             % (n, len(candidats)))
            continue
        gestes.append((n, retenu))

    if refus:
        print("  REFUS")
        for r in refus:
            print("    " + r)
        print()

    if not gestes:
        return 1

    lignes = []
    print("  plan  prise            duree   image de depart")
    for n, (f, d, trouvee, note) in gestes:
        cible = os.path.join(fin, "plan%02d.mp4" % n)
        avant = empreinte(cible)[:12] if os.path.exists(cible) else "(vide)"
        neuf = empreinte(os.path.join(pr, f))
        remplace = "" if avant == "(vide)" else "  remplace %s" % avant
        if neuf[:12] == avant:
            remplace = "  (deja en place)"
        print("  %02d    %-16s %5.2f s  %-24s%s"
              % (n, f, d, trouvee, remplace))
        if not a.essai and neuf[:12] != avant:
            shutil.copy2(os.path.join(pr, f), cible)
            lignes.append("%s  plan%02d  %s  %s  avant:%s"
                          % (time.strftime("%Y-%m-%d %H:%M"), n, f, neuf, avant))

    print()
    if a.essai:
        print("  --essai : rien n'a ete ecrit.")
        return 0
    if lignes:
        j = os.path.join(fin, "_retenues.txt")
        neuf_fichier = not os.path.exists(j)
        with io.open(j, "a", encoding="utf-8", newline="\n") as fh:
            if neuf_fichier:
                fh.write("PRISES RETENUES -- qui est dans 03-final, et depuis quand\n")
                fh.write("=" * 62 + "\n\n")
            for l in lignes:
                fh.write(l + "\n")
        print("  %d plan(s) porte(s) dans 03-final." % len(lignes))
        print("  Ces plans doivent repasser au lip-sync : 04-lipsync garde")
        print("  encore la synchro de l'ancienne prise.")
    else:
        print("  Rien a changer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
