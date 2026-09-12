# -*- coding: utf-8 -*-
"""Preparer -- puis juger -- un essai d'avatar pilote par l'audio.

    python video/essai_avatar.py --plan 16
    python video/essai_avatar.py --plan 16 --mesurer chemin/vers/le/retour.mp4

CE QUE CET ESSAI DOIT REPONDRE, ET RIEN D'AUTRE
    Seedance recoit une fenetre de parole ECRITE DANS LE PROMPT et fait ce
    qu'il veut de ces nombres : de +0,11 a +1,96 s d'ecart sur six prises
    mesurees le 10 septembre 2026, toujours du meme cote -- le son arrive
    avant l'image, celui que l'UIT tolere le moins.

    Un modele PILOTE PAR L'AUDIO n'a pas de fenetre demandee a ignorer : le
    son conditionne chaque instant de la generation. Le decalage d'attaque ne
    peut pas exister. La question n'est donc pas « est-ce mieux », elle est :
    LA BOUCHE DIT-ELLE VRAIMENT LES MOTS, sur un gros plan en allemand ?

    Ce qui se mesure, c'est LSE-C -- la confiance de SyncNet. Les LSE-D de
    l'episode actuel sont deja dans la bande de l'etat de l'art (4,9 a 7,6) ;
    c'est la confiance qui pend : 1,0 a 5,8, contre 10,1 sur de vraies images.
    Une bouche plausiblement dans le temps, dont le reseau doute qu'elle dise
    ces mots-la. C'est la signature de levres repeintes sur une machoire qui
    articule autre chose.

POURQUOI HORS D'ARTLIST
    Il reste 460 credits. En mode reference, Seedance coute 120 credits la
    SECONDE : 3,8 secondes, pas meme un plan. Un essai de deux secondes chez
    un fournisseur externe coute vingt-cinq cents.

⚠️ LES DROITS COMMERCIAUX SE VERIFIENT AVANT DE PAYER, PAS APRES
    Wortando est un projet commercial. Tarifs releves le 10 septembre ;
    celui de BytePlus corrige le 12 depuis leur propre console -- la note
    du 10 disait 0,16 $, leur fiche produit dit 0,12 $.

        BytePlus    0,12 $/s   l'API OFFICIELLE de ByteDance -- terrain le
                               plus sur pour un usage commercial
        fal         0,16 $/s   annonce une sortie « commercial-ready »
        ModelsLab   0,14 $/s
        WaveSpeed   0,12 $/s
        PiAPI          --      usage commercial reserve au plan PREMIUM :
                               ce n'est donc PAS la route des credits
                               gratuits d'inscription

    L'officiel est donc AUSSI le moins cher, a egalite avec WaveSpeed. Il n'y
    a plus d'arbitrage a faire : BytePlus.

CE QUE LE SCRIPT FAIT
    1. Il taille une piste audio a la mesure du plan -- amorce, la voix, une
       queue courte -- au lieu des cinq secondes de la piste de tournage, dont
       trois seraient payees a filmer une bouche fermee.
    2. Il mesure la prise ACTUELLE du meme plan avec SyncNet et garde le
       chiffre. Sans cette ligne de base prise AVANT, on comparera le retour a
       un souvenir.
    3. Au retour, --mesurer compare les deux et dit lequel gagne, sur quoi.

⚠️ ET LA LIMITE DE SYNCNET IMPOSE LE PROTOCOLE : il n'est pas invariant a la
    translation, donc il compare deux prises du MEME plan, jamais deux
    cadrages. C'est pour ca que l'essai part de l'image de depart deja
    utilisee, et pas d'une nouvelle.
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
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402
import syncnet as S                                         # noqa: E402

AMORCE = 0.35          # le silence avant le premier mot, comme au montage
QUEUE = 0.60           # de quoi refermer la bouche sans payer du vide
TARIFS = [("WaveSpeed", 0.12), ("ModelsLab", 0.14),
          ("BytePlus (officiel ByteDance)", 0.12), ("fal", 0.16)]


def image_du_plan(ep, n):
    """L'image de depart que la feuille de tournage donne pour ce plan."""
    feuille = os.path.join(ep, "A-REFAIRE-AUDIO.txt")
    if not os.path.exists(feuille):
        return None
    bloc = re.split(r"(?m)^PLAN %02d\b" % n, io.open(feuille, encoding="utf-8").read())
    if len(bloc) < 2:
        return None
    m = re.search(r"@img1 : (\S+)", bloc[1])
    return m.group(1) if m else None


def piste(F, src, dst):
    """Amorce + la voix nue + une queue courte. Renvoie la duree obtenue."""
    tete, queue, _ = M.parole(F, src)
    subprocess.run([F, "-y", "-v", "error", "-ss", "%.3f" % tete,
                    "-to", "%.3f" % queue, "-i", src,
                    "-af", "adelay=%d:all=1,apad" % int(round(AMORCE * 1000)),
                    "-t", "%.3f" % (AMORCE + (queue - tete) + QUEUE),
                    "-ar", "44100", "-ac", "1", "-b:a", "192k", dst], check=True)
    return M.duree(F, dst)


def mesure_json(chemin, clip):
    r = S.mesurer(clip)
    if not r:
        return None
    img, d, c = r
    val = {"clip": os.path.relpath(clip, RACINE), "offset_images": img,
           "offset_ms": round(img / S.IPS_SYNCNET * 1000.0, 1),
           "lse_d": round(d, 3), "lse_c": round(c, 3)}
    io.open(chemin, "w", encoding="utf-8", newline="").write(
        json.dumps(val, ensure_ascii=False, indent=1) + "\n")
    return val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--plan", type=int, default=16)
    ap.add_argument("--mesurer", help="le clip revenu du fournisseur")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    dossier = os.path.join(ep, "_essai-avatar")
    os.makedirs(dossier, exist_ok=True)
    avant_f = os.path.join(dossier, "plan%02d-avant.json" % a.plan)

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    p = next((x for x in d["plans"] if x["n"] == a.plan), None)
    if not p:
        sys.exit("  Le plan %d n'existe pas dans la scene." % a.plan)

    # ---------------------------------------------------- juger le retour
    if a.mesurer:
        if not os.path.exists(a.mesurer):
            sys.exit("  Fichier introuvable : %s" % a.mesurer)
        if not os.path.exists(avant_f):
            sys.exit("  Pas de ligne de base pour le plan %02d.\n"
                     "  Lancer d'abord : python video/essai_avatar.py --plan %d"
                     % (a.plan, a.plan))
        avant = json.load(io.open(avant_f, encoding="utf-8"))
        apres = mesure_json(os.path.join(dossier, "plan%02d-apres.json" % a.plan),
                            a.mesurer)
        if not apres:
            sys.exit("  Aucun visage suivi dans le clip revenu.")
        print("  PLAN %02d  « %s »\n" % (a.plan, p["de"]))
        print("  %-26s %10s %10s %10s" % ("", "offset", "LSE-D", "LSE-C"))
        print("  " + "-" * 60)
        for nom, v in (("Seedance + sync.so", avant), ("l'avatar", apres)):
            print("  %-26s %+8.0f ms %10.3f %10.3f"
                  % (nom, v["offset_ms"], v["lse_d"], v["lse_c"]))
        print()
        # LSE-C EST LE JUGE, ET C'EST DIT AVANT DE REGARDER LE RESULTAT.
        dc = apres["lse_c"] - avant["lse_c"]
        dd = apres["lse_d"] - avant["lse_d"]
        print("  confiance : %+.3f  (%s)"
              % (dc, "l'avatar gagne" if dc > 0 else "l'avatar perd"))
        print("  distance  : %+.3f  (%s ; plus bas vaut mieux)"
              % (dd, "l'avatar gagne" if dd < 0 else "l'avatar perd"))
        print("\n  Rappel de l'echelle : LSE-D de 6 a 8 est l'etat de l'art,")
        print("  et de vraies images filmees donnent une confiance de 10,1.")
        print("  L'oeil tranche ensuite -- le sourire permanent et les dents")
        print("  sont le defaut que les praticiens rapportent le plus souvent.")
        return

    # ------------------------------------------------- preparer l'essai
    src = os.path.join(RACINE, "audio", "scenes", a.scene,
                       "%02d-%s.mp3" % (a.plan, p["locuteur"]))
    if not os.path.exists(src):
        sys.exit("  Voix manquante : %s" % os.path.basename(src))
    dst = os.path.join(dossier, "plan%02d-%s.mp3" % (a.plan, p["locuteur"]))
    duree = piste(F, src, dst)

    img = image_du_plan(ep, a.plan)
    chemin_img = os.path.join(ep, "01-images", img) if img else None

    print("  PLAN %02d   %s   « %s »" % (a.plan, p["locuteur"], p["de"]))
    print()
    print("  A TELEVERSER")
    if chemin_img and os.path.exists(chemin_img):
        print("    image : %s" % os.path.relpath(chemin_img, RACINE))
    else:
        print("    image : INTROUVABLE (%s) -- la feuille de tournage la nomme,"
              % (img or "?"))
        print("            regenerer avec scenes/refaire_audio.py")
    print("    audio : %s   (%.2f s)" % (os.path.relpath(dst, RACINE), duree))
    print()
    print("  CE QUE CA COUTE, LA DUREE DE LA VIDEO ETANT CELLE DE L'AUDIO")
    for nom, prix in TARIFS:
        print("    %-30s %.2f $" % (nom, duree * prix))
    print()
    print("  LA LIGNE DE BASE, prise MAINTENANT sur la prise actuelle du meme plan")
    sync = os.path.join(ep, "04-lipsync", "plan%02d.mp4" % a.plan)
    mont = os.path.join(ep, "_montage", "plan%02d.mp4" % a.plan)
    clip = sync if os.path.exists(sync) else (mont if os.path.exists(mont) else None)
    if not clip:
        print("    aucune prise sonore a comparer : la comparaison sera boiteuse.")
    else:
        avant = mesure_json(avant_f, clip)
        if avant:
            print("    %-24s offset %+.0f ms   LSE-D %.3f   LSE-C %.3f"
                  % (os.path.basename(clip), avant["offset_ms"],
                     avant["lse_d"], avant["lse_c"]))
            print("    gardee dans %s" % os.path.relpath(avant_f, RACINE))
        else:
            print("    aucun visage suivi dans la prise actuelle.")
    print()
    print("  AU RETOUR")
    print("    python video/essai_avatar.py --plan %d --mesurer <le fichier>" % a.plan)


if __name__ == "__main__":
    main()
