# -*- coding: utf-8 -*-
"""Refait la voix d'UN SEUL plan, au reglage et au gain deja mesures.

    python audio/refaire_plan.py --plan 2
    python audio/refaire_plan.py --plan 2 --pour-de-vrai

POURQUOI CET OUTIL EXISTE
    scene_audio.py refait la scene entiere : il mesure la sonie sur l'ensemble
    des fichiers et applique un gain unique. C'est ce qu'il faut la premiere
    fois. Mais quand une seule replique change -- une phrase reecrite, une
    faute entendue a l'ecoute -- tout regenerer jetterait dix-huit prises
    approuvees, que v3 ne rendra jamais deux fois pareil.

LE GAIN NE SE RECALCULE PAS
    Il est lu dans manifeste.json, ou scene_audio.py l'a ecrit. Meme voix,
    memes reglages, meme modele : le nouveau fichier arrive a la meme sonie
    brute que celui qu'il remplace, a une fraction de decibel pres. Recalculer
    un gain sur un seul fichier, en revanche, le poserait au niveau moyen de
    la scene et ecraserait justement l'ecart voulu entre les repliques.

CE QU'IL MET A JOUR
    Le mp3 final, sa copie brute, la ligne du plan dans manifeste.json, et
    duree_audio dans la scene -- c'est cette derniere que montage.py lit.
"""
import argparse
import io
import json
import os
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                             # noqa: E402
import normaliser                                          # noqa: E402
from scene_audio import DIALOGUE, DIALOGUE_V3              # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int, required=True)
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()

    fs = os.path.join(RACINE, "scenes", a.scene + ".json")
    d = json.load(io.open(fs, encoding="utf-8"))
    p = next((x for x in d["plans"] if x["n"] == a.plan), None)
    if not p:
        sys.exit("  Le plan %d n'existe pas dans %s." % (a.plan, a.scene))

    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    fm = os.path.join(dossier, "manifeste.json")
    if not os.path.exists(fm):
        sys.exit("  Pas de manifeste : la scene n'a jamais ete generee en entier.\n"
                 "  Lancer d'abord audio/scene_audio.py.")
    m = json.load(io.open(fm, encoding="utf-8"))

    modele = m["modele"]
    court = next((k for k, v in generer.MODELES.items() if v[0] == modele), None)
    gain = m["gain_applique_db"]
    voix = d["locuteurs"][p["locuteur"]]["voice_id"]

    texte = p["de"]
    if court == "v3" and p.get("balise"):
        texte = p["balise"] + " " + texte

    ancien = next((x for x in m["plans"] if x["plan"] == a.plan), None)
    print("  plan %02d  %s  %s" % (a.plan, p["locuteur"], modele))
    if ancien:
        print("  avant  << %s >>  (%.2f s)" % (ancien["de"], ancien["duree_reelle"]))
    print("  apres  << %s >>" % p["de"])
    if texte != p["de"]:
        print("  balise %s" % p["balise"])
    print("  %d caracteres, gain de scene %+.2f dB (non recalcule)"
          % (len(texte), gain))

    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai pour depenser.")
        return

    normaliser.FF = normaliser.ffmpeg()
    if not normaliser.FF:
        sys.exit("  ffmpeg est indispensable.")

    generer.VOIX = voix
    generer.REGLAGES = DIALOGUE_V3 if court == "v3" else DIALOGUE
    octets = generer.synthetiser(texte, modele, generer.cle_api())

    nom = "%02d-%s.mp3" % (a.plan, p["locuteur"])
    brut = os.path.join(dossier, "_brut", nom)
    fini = os.path.join(dossier, nom)

    # La prise remplacee part dans _ancienne-numerotation, ou dorment deja les
    # fichiers d'avant : une prise v3 ne se refait pas a l'identique.
    vieux = os.path.join(dossier, "_ancienne-numerotation")
    os.makedirs(vieux, exist_ok=True)
    if os.path.exists(fini):
        garde = os.path.join(vieux, "remplace-%s" % nom)
        shutil.copy2(fini, garde)
        print("  ancienne prise gardee : _ancienne-numerotation/%s"
              % os.path.basename(garde))

    io.open(brut, "wb").write(octets)
    filtre = "volume=%.2fdB,alimiter=limit=0.891" % gain
    if not normaliser._ff(brut, fini, filtre):
        sys.exit("  Egalisation echouee.")
    duree = round(normaliser.duree(fini), 2)
    print("  %s  %.2f s" % (nom, duree))

    for x in m["plans"]:
        if x["plan"] == a.plan:
            x["de"], x["duree_reelle"] = p["de"], duree
    io.open(fm, "w", encoding="utf-8", newline="").write(
        json.dumps(m, ensure_ascii=False, indent=2) + chr(10))

    # duree_audio dans la scene : c'est elle que montage.py croit.
    t = io.open(fs, encoding="utf-8").read()
    if p.get("duree_audio") is not None:
        vieille = '"duree_audio": %s' % json.dumps(p["duree_audio"])
        bloc = t.split('"n": %d,' % a.plan, 1)[1].split('"n":', 1)[0]
        if bloc.count(vieille) == 1:
            t = t.replace('"n": %d,' % a.plan,
                          '"n": %d,' % a.plan, 1)
            avant, apres = t.split('"n": %d,' % a.plan, 1)
            apres = apres.replace(vieille, '"duree_audio": %s' % duree, 1)
            t = avant + '"n": %d,' % a.plan + apres
            io.open(fs, "w", encoding="utf-8", newline=chr(10)).write(t)
            print("  duree_audio du plan %02d : %.2f -> %.2f"
                  % (a.plan, p["duree_audio"], duree))
        else:
            print("  duree_audio a reporter a la main : %.2f" % duree)

    if duree + 1 > p["duree"]:
        print("  ATTENTION : le clip dure %d s, la voix %.2f s -- la replique"
              " sera au ras." % (p["duree"], duree))
    print("\n  Relancer : python video/montage.py --scene %s" % a.scene)


if __name__ == "__main__":
    main()
