# -*- coding: utf-8 -*-
"""L'audio complet d'une scene : une replique par plan, une voix par locuteur.

    python audio/scene_audio.py --scene 01-ankunft-berlin              # a blanc
    python audio/scene_audio.py --scene 01-ankunft-berlin --pour-de-vrai

A BLANC PAR DEFAUT. Une scene coute plusieurs centaines de credits ; le
script dit ce qu'il ferait et s'arrete, tant qu'on ne le lui demande pas
explicitement.

LA SCENE EST EGALISEE D'UN BLOC, PAS PLAN PAR PLAN
    C'est la seule chose vraiment delicate ici, et c'est un piege ou l'on
    tombe naturellement en reutilisant audio/normaliser.py tel quel.

    normaliser.py ramene CHAQUE fichier a -14 LUFS. C'est exactement juste
    pour le cours : « der Bahnhof » et « die Krankenversicherung » doivent
    sonner pareil, l'un ne doit pas obliger a monter le volume pour l'autre.

    Applique replique par replique a un DIALOGUE, il fait l'inverse de ce
    qu'on veut. Mark qui demande timidement son chemin et Anna qui repond
    avec assurance finiraient a l'intensite exacte, au decibel pres. La
    scene sonnerait plate, et personne ne saurait dire pourquoi.

    On mesure donc la scene ENTIERE une fois, on en tire UN gain, et on
    applique ce meme gain a tous les plans. Le niveau general est juste, et
    les ecarts entre les repliques restent ceux que la voix a produits.

CHAQUE LOCUTEUR PARLE AVEC SA VOIX
    Le voice_id est lu dans scene["locuteurs"], pas passe en argument : c'est
    le fichier de scene qui sait qui parle avec quoi. Un locuteur sans voix
    arrete le script avant la moindre depense.
"""
import argparse
import io
import json
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))

import generer                                            # noqa: E402
import normaliser                                         # noqa: E402

CIBLE_LUFS = -14.0


# --------------------------------------------------------------------------
# LE DIALOGUE N'OBEIT PAS AUX MEMES REGLES QUE LE VOCABULAIRE.
#
# generer.REGLAGES resserre volontairement la distribution : stability 0.75,
# style 0.0. C'est juste pour les 25 298 mots isolés du cours -- « der Bahnhof »
# et « die Krankenversicherung » doivent sonner pareil, et personne ne peut
# reecouter 25 000 fichiers pour trier les bonnes prises.
#
# Applique a une SCENE, ce reglage fait exactement ce qu'on ne veut pas : il
# aplatit. Jacques l'a entendu avant qu'on l'explique -- « ca manque un peu
# d'expression ». Ce n'etait pas la voix, c'etait le reglage.
#
# On abaisse donc la stabilite (la voix varie d'une phrase a l'autre) et on
# leve le style (l'intention devient audible). ON NE TOUCHE PAS A generer.py :
# le corpus du cours doit rester homogene avec ce qui a deja ete produit.
# --------------------------------------------------------------------------
DIALOGUE = {"stability": 0.40, "similarity_boost": 0.75,
            "style": 0.45, "use_speaker_boost": True}

def gain_de_la_scene(morceaux, dossier):
    """Le gain unique qui met la scene entiere a la cible."""
    liste = os.path.join(dossier, "_concat.txt")
    io.open(liste, "w", encoding="utf-8", newline="").write(
        "".join("file '%s'\n" % f.replace("'", "'\\''") for f in morceaux))
    ensemble = os.path.join(dossier, "_ensemble.mp3")
    r = subprocess.run(
        [normaliser.FF, "-hide_banner", "-nostats", "-y", "-f", "concat",
         "-safe", "0", "-i", liste, "-c", "copy", ensemble],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not os.path.exists(ensemble):
        sys.exit("  Impossible d'assembler la scene pour la mesurer :\n" + r.stderr[-400:])
    m = normaliser.mesurer(ensemble)
    if not m:
        sys.exit("  Mesure de sonie impossible sur la scene assemblee.")
    mesure = float(m["input_i"])
    crete = float(m["input_tp"])
    return CIBLE_LUFS - mesure, mesure, crete, ensemble


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--modele", default="v2", choices=sorted(generer.MODELES))
    ap.add_argument("--reglages-du-cours", action="store_true",
                    help="utiliser la stabilite haute du corpus au lieu de celle du dialogue")
    ap.add_argument("--pour-de-vrai", action="store_true",
                    help="depenser reellement les credits")
    a = ap.parse_args()

    chemin = os.path.join(RACINE, "scenes", a.scene + ".json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    plans, locuteurs = d["plans"], d["locuteurs"]

    # Un locuteur sans voix arrete tout AVANT la premiere depense : sinon on
    # decouvre le trou au onzieme plan, apres six cents credits.
    manquants = sorted({p["locuteur"] for p in plans
                        if not locuteurs.get(p["locuteur"], {}).get("voice_id")})
    if manquants:
        sys.exit("  Sans voix : %s\n  Renseigner voice_id dans %s."
                 % (", ".join(manquants), os.path.basename(chemin)))

    modele, cout = generer.MODELES[a.modele]
    car = sum(len(p["de"]) for p in plans)
    print("  %s — %d plans, %d s" % (d["situation"], len(plans), d["duree"]))
    for cle, v in locuteurs.items():
        n = sum(1 for p in plans if p["locuteur"] == cle)
        print("    %-10s %-12s %2d replique(s)" % (v["nom"], v.get("voix") or "?", n))
    print("  %d caracteres en %s = environ %d credits" % (car, a.modele, int(car * cout)))

    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai pour depenser.")
        return

    normaliser.FF = normaliser.ffmpeg()
    if not normaliser.FF:
        sys.exit("  ffmpeg est indispensable pour egaliser la scene.")

    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    brut = os.path.join(dossier, "_brut")
    os.makedirs(brut, exist_ok=True)
    cle_api = generer.cle_api()
    if not a.reglages_du_cours:
        generer.REGLAGES = DIALOGUE

    bruts = []
    for p in plans:
        nom = "%02d-%s" % (p["n"], p["locuteur"])
        f = os.path.join(brut, nom + ".mp3")
        print("  %s ..." % nom, end="", flush=True)
        avant = generer.VOIX
        generer.VOIX = locuteurs[p["locuteur"]]["voice_id"]
        try:
            octets = generer.synthetiser(p["de"], modele, cle_api)
        except generer.TexteBloque:
            sys.exit("\n  Texte refuse par ElevenLabs au plan %d. Rien n'est "
                     "utilisable tant que la scene est incomplete." % p["n"])
        finally:
            generer.VOIX = avant
        io.open(f, "wb").write(octets)
        bruts.append(f)
        print(" %.1f s" % normaliser.duree(f))

    gain, mesure, crete, ensemble = gain_de_la_scene(bruts, brut)
    # Le limiteur ne sert qu'aux cretes que le gain ferait depasser ; il ne
    # touche pas aux ecarts entre repliques, qui sont ce qu'on protege.
    filtre = "volume=%.2fdB,alimiter=limit=0.891" % gain
    print("\n  scene mesuree a %.2f LUFS (crete %.2f) -> gain unique de %+.2f dB"
          % (mesure, crete, gain))

    manifeste = []
    for p, f in zip(plans, bruts):
        nom = os.path.basename(f)
        fini = os.path.join(dossier, nom)
        if not normaliser._ff(f, fini, filtre):
            sys.exit("  Egalisation echouee sur %s." % nom)
        manifeste.append({"plan": p["n"], "locuteur": p["locuteur"],
                          "fichier": nom, "de": p["de"],
                          "duree_reelle": round(normaliser.duree(fini), 2),
                          "duree_prevue": p["duree"]})

    io.open(os.path.join(dossier, "manifeste.json"), "w",
            encoding="utf-8", newline="").write(
        json.dumps({"scene": a.scene, "modele": modele,
                    "reglages": generer.REGLAGES, "seed": generer.SEED,
                    "gain_applique_db": round(gain, 2),
                    "sonie_avant_lufs": round(mesure, 2),
                    "plans": manifeste}, ensure_ascii=False, indent=2) + "\n")

    reel = sum(x["duree_reelle"] for x in manifeste)
    print("\n  %d fichiers dans audio/scenes/%s/" % (len(manifeste), a.scene))
    print("  duree reelle %.1f s, prevue %d s" % (reel, d["duree"]))
    ecarts = [x for x in manifeste if abs(x["duree_reelle"] - x["duree_prevue"]) >= 2]
    if ecarts:
        print("\n  Plans dont la duree reelle s'ecarte de 2 s ou plus du plan :")
        for x in ecarts:
            print("    %2d  prevu %2d s, reel %5.1f s  « %s »"
                  % (x["plan"], x["duree_prevue"], x["duree_reelle"], x["de"][:48]))
        print("  Reporter ces durees dans la scene : c'est l'audio qui a raison,")
        print("  et le chiffrage HeyGen se calcule dessus.")


if __name__ == "__main__":
    main()
