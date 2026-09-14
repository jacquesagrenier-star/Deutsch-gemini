# -*- coding: utf-8 -*-
"""Ecrit dans la scene la duree REELLE de chaque replique.

    python audio/reporter_durees.py --scene 02-beim-buergeramt
    python audio/reporter_durees.py --scene 02-beim-buergeramt --simuler

POURQUOI CET OUTIL EXISTE
    scene_audio.py finit en disant << Reporter ces durees dans la scene : c'est
    l'audio qui a raison >>, et il ne le fait pas. refaire_plan.py, lui, ne
    sait que METTRE A JOUR un duree_audio deja present -- sinon il ecrit
    << a reporter a la main >>. Le premier report n'avait donc pas d'outil, et
    une etape manuelle dans une chaine qui en compte douze est une etape
    oubliee.

⚠️ duree_audio N'EST PAS LA DUREE DU PLAN. NE JAMAIS MONTER DESSUS.
    C'est la duree de la VOIX, rien d'autre. Mesure sur l'episode 1, qui est
    monte et qui marche :

        audio d'une replique      1,2 a 2,7 s
        duree ecrite dans la scene  3 a 5 s
        CLIP FINAL                  5,04 s

    La parole n'occupe que la MOITIE du plan. Le reste, c'est le personnage qui
    ecoute, respire et attend -- et c'est ce que le prompt du plan 05 de
    l'episode 1 demande explicitement : << Finally, he stops speaking and
    listens intently without speaking [...] he blinks, he breathes, he shifts
    his weight a little, and he waits. >>

    Un plan coupe a duree_audio donnerait un avatar qui se tait et disparait
    dans la meme image. C'est l'erreur que ce paragraphe existe pour empecher.

⚠️ ET LE CHIFFRAGE DE L'AVATAR NE SE FAIT PAS ICI NON PLUS. OmniHuman
    facture a la seconde de sortie, et la sortie suit LA PISTE QU'ON ENVOIE --
    piste qui doit etre allongee jusqu'a la duree du plan avant l'envoi
    (procedure de l'episode 1 : << ne pas raccourcir la piste pour economiser,
    le silence final est la marge dont la bouche a besoin pour se refermer >>).
    Le total imprime ci-dessous est donc un PLANCHER, pas la facture.

RIEN N'EST APPELE, RIEN N'EST FACTURE : on ne fait que mesurer des fichiers
deja sur le disque.
"""
import argparse
import collections
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                          # noqa: E402

PRIX_AVATAR = 0.16       # $ la seconde chez fal, releve sur la fiche du modele


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", required=True)
    p.add_argument("--simuler", action="store_true",
                   help="afficher le tableau sans ecrire dans la scene")
    a = p.parse_args()

    chemin = os.path.join(RACINE, "scenes", a.scene + ".json")
    if not os.path.exists(chemin):
        sys.exit("  scene introuvable : %s" % chemin)
    d = json.loads(io.open(chemin, encoding="utf-8").read(),
                   object_pairs_hook=collections.OrderedDict)
    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)

    ff = M.ffmpeg()
    total = avatar = 0.0
    manquants = []
    print("  %-5s %-10s %8s %8s %8s" % ("plan", "locuteur", "ecrit", "reel", "ecart"))
    print("  " + "-" * 45)
    for plan in d["plans"]:
        f = os.path.join(dossier, "%02d-%s.mp3" % (plan["n"], plan["locuteur"]))
        if not os.path.exists(f):
            manquants.append(plan["n"])
            continue
        reelle = M.duree(ff, f)
        if reelle is None:
            manquants.append(plan["n"])
            continue
        plan["duree_audio"] = round(reelle, 2)
        total += reelle
        if plan["type"] != "decor":
            avatar += reelle
        ecart = reelle - plan["duree"]
        print("  %-5d %-10s %7.0fs %7.2fs %+7.2fs%s"
              % (plan["n"], plan["locuteur"], plan["duree"], reelle, ecart,
                 "  <--" if abs(ecart) >= 2 else ""))

    if manquants:
        sys.exit("\n  Audio absent pour le(s) plan(s) %s.\n"
                 "  Lancer d'abord : python audio/scene_audio.py --scene %s "
                 "--pour-de-vrai" % (manquants, a.scene))

    d["duree_audio"] = round(total, 2)
    print("\n  scene : %.1f s reelles contre %d s ecrites" % (total, d["duree"]))
    print("  dont %.1f s de PAROLE d'avatar -> %.2f $ au minimum absolu"
          % (avatar, avatar * PRIX_AVATAR))
    print("  (plancher, pas la facture : les pistes s'allongent avant l'envoi)")

    if a.simuler:
        print("\n  SIMULATION -- la scene n'a pas ete modifiee.")
        return
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  ecrit dans scenes/%s.json" % a.scene)


if __name__ == "__main__":
    main()
