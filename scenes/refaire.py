# -*- coding: utf-8 -*-
"""La feuille de re-tournage : les plans a refaire, prompt pret a coller.

    python scenes/refaire.py --scene 01-ankunft-berlin --muets

POURQUOI UNE FEUILLE A PART
    production-01.html porte les DEUX prompts de chaque plan -- l'image et
    l'animation -- pour dix-neuf plans. C'est ce qu'il faut pour tourner un
    episode. Pour en refaire douze, c'est douze fois trop de texte a l'ecran,
    et le risque de coller le mauvais bloc.

    Ici : que les plans a refaire, que le prompt d'animation, dans l'ordre, et
    le nom du fichier a mettre en Start Frame. Rien d'autre.

    Les images de depart ne se refont pas. Elles portent l'identite, elles
    sont validees, et elles coutent 130 credits les quatre. Seule l'animation
    est a relancer -- 200 credits par plan.

LES SECONDES VIENNENT DU FICHIER, PAS DU SCENARIO
    La fenetre de parole demandee a Seedance est celle de la voix : elle
    commence a l'amorce du montage et dure ce que dure le mp3. Le script lit
    donc duree_audio -- et le 8 septembre au soir, QUINZE des dix-neuf valeurs
    etaient fausses, le plan 13 de 1,60 s. La feuille aurait demande une
    fenetre trop courte d'une seconde et demie, sur douze plans, sans que rien
    ne s'en plaigne.

    Le script mesure donc les mp3 et refuse de travailler sur une valeur
    perimee. Une duree inventee coute deux cents credits et une prise a
    refaire.

LE PIEGE DE LA REPETITION
    Deux plans de la meme taille qui partent de la MEME image au pixel pres
    ramenent le personnage a la position identique, et ca se voit. Le script
    distribue les variantes (-b, -c) et dit lesquelles manquent, au lieu de
    laisser la decouverte au montage.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "scenes"))
import production as P                                     # noqa: E402


def images(dossier, pose, taille):
    """Les variantes disponibles pour un personnage a une taille, dans l'ordre
    ou on veut les servir : la nue d'abord, puis -b, -c..."""
    base = "%s-%s" % (pose, taille.replace(" ", "-"))
    trouvees = []
    for suffixe in ("", "-b", "-c", "-d"):
        f = base + suffixe + ".png"
        if os.path.exists(os.path.join(dossier, f)):
            trouvees.append(f)
    return trouvees


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--muets", action="store_true",
                    help="tous les plans qui ont un visage -- ceux que la regle "
                         "MUET oblige a refaire")
    ap.add_argument("--plans", help="ou bien ceux-la : 5,8,10")
    a = ap.parse_args()

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    dim = os.path.join(RACINE, "video", "episode-" + a.scene, "01-images")

    if a.plans:
        voulus = {int(x) for x in a.plans.replace(" ", "").split(",") if x}
    elif a.muets:
        voulus = {n for n, m in P.MISE_EN_SCENE.items() if "pose" in m}
    else:
        sys.exit("  Preciser --muets ou --plans.")

    plans = [p for p in d["plans"] if p["n"] in voulus]
    if not plans:
        sys.exit("  Aucun plan a refaire.")

    # LES DUREES DOIVENT ETRE CELLES DES FICHIERS. Voir l'en-tete.
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import montage as M                                    # noqa: E402
    F = M.ffmpeg()
    perimes = []
    for p in plans:
        f = os.path.join(RACINE, "audio", "scenes", a.scene,
                         "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(f):
            sys.exit("  Plan %02d : voix manquante (%s)"
                     % (p["n"], os.path.basename(f)))
        vrai = round(M.duree(F, f), 2)
        if abs(vrai - (p.get("duree_audio") or 0)) > 0.05:
            perimes.append((p["n"], p.get("duree_audio"), vrai))
        p["duree_audio"] = vrai
    if perimes:
        print("  duree_audio perimee dans la scene, corrigee ici :")
        for n, vieux, vrai in perimes:
            print("    plan %02d  %s -> %.2f s" % (n, vieux, vrai))
        print("  Reporter ces valeurs dans scenes/%s.json." % a.scene)

    # Distribuer les variantes d'image : une par plan de la meme taille.
    servi, manque = {}, []
    for p in plans:
        m = P.MISE_EN_SCENE[p["n"]]
        cle = (m["pose"], m["taille"])
        dispo = images(dim, *cle)
        rang = servi.setdefault(cle, 0)
        if rang < len(dispo):
            p["_image"] = dispo[rang]
        else:
            p["_image"] = dispo[0] if dispo else "(aucune)"
            manque.append((p["n"], cle))
        servi[cle] = rang + 1

    out = os.path.join(RACINE, "video", "episode-" + a.scene, "A-REFAIRE.txt")
    o = []
    nl = chr(10)
    o.append("RE-TOURNAGE -- %s" % d["situation"])
    o.append("=" * 62)
    o.append("")
    o.append("%d plans, 200 credits piece = %d credits."
             % (len(plans), 200 * len(plans)))
    o.append("")
    o.append("POUR CHAQUE PLAN, DANS ARTLIST")
    o.append("  1. Video, modele Seedance 2.0 Mini, 9:16, la duree indiquee.")
    o.append("  2. Start Frame = l'image nommee ci-dessous, prise dans")
    o.append("     video/episode-%s/01-images/." % a.scene)
    o.append("  3. Coller le prompt tel quel. Lancer. Telecharger.")
    o.append("  4. python video/rapatrier.py --plan N")
    o.append("")
    o.append("REGARDEZ LE PREMIER AVANT DE FAIRE LES ONZE AUTRES. C'est lui qui")
    o.append("dit si la bouche fermee tient. Deux cents credits pour le savoir.")
    o.append("")
    if manque:
        o.append("VARIANTES D'IMAGE MANQUANTES")
        for n, (pose, taille) in manque:
            o.append("  plan %02d  %s %s -- repart d'une image deja servie."
                     % (n, pose, taille))
        o.append("  Le personnage reviendra a la position identique, et ca se")
        o.append("  voit. Generer 4 images (130 credits) evite le defaut.")
        o.append("")
    o.append("")

    for p in plans:
        m = P.MISE_EN_SCENE[p["n"]]
        o.append("-" * 62)
        o.append("PLAN %02d   %s   %s   GENERER A %d SECONDES%s"
                 % (p["n"], p["locuteur"], m["taille"],
                    P.duree_a_generer(p),
                    "   (zoom)" if m.get("zoom") else ""))
        o.append("  replique de %.2f s, parole demandee de 0,5 a %.1f s"
                 % (p.get("duree_audio") or p["duree"],
                    0.5 + (p.get("duree_audio") or p["duree"])))
        o.append("  << %s >>" % p["de"])
        o.append("  Start Frame : %s" % p["_image"])
        o.append("")
        o.append(P.video_prompt(m, p))
        o.append("")

    io.open(out, "w", encoding="utf-8", newline=nl).write(nl.join(o) + nl)
    print("  %d plans  ->  %s" % (len(plans), os.path.relpath(out, RACINE)))
    print("  %d credits d'animation, aucune image a refaire." % (200 * len(plans)))
    if manque:
        print("  %d plan(s) sans variante d'image propre : %s"
              % (len(manque), ", ".join(str(n) for n, _ in manque)))


if __name__ == "__main__":
    main()
