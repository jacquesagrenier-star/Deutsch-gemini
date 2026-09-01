# -*- coding: utf-8 -*-
"""Remonte tous les fichiers audio a la meme sonie.

    python audio/normaliser.py --essai 6      # six fichiers, mesure avant/apres
    python audio/normaliser.py --niveaux A1,A2

POURQUOI
    Les fichiers sortis d'ElevenLabs plafonnent entre -7 et -15 dBFS, avec une
    sonie integree autour de -24 LUFS. La synthese vocale du telephone, elle,
    sort proche du maximum. Resultat a l'usage : la voix de Nadja est deux a
    cinq fois plus faible que tout le reste de l'application, et l'utilisateur
    monte le volume pour elle puis le redescend pour le reste.

    On ne peut pas corriger ca dans l'application : `volume` d'un element audio
    plafonne a 1, il ne sait qu'attenuer. Passer par Web Audio pour amplifier
    imposerait d'ouvrir CORS, de reveiller un AudioContext dans le geste de
    l'utilisateur et de rerouter le son -- trois mecanismes de plus, sur la
    plateforme meme qui vient de nous couter une version. Le defaut est dans
    les fichiers : c'est la qu'on le corrige, une fois pour toutes.

EGALISER, PAS SEULEMENT REMONTER
    La premiere version visait la sonie avec `loudnorm linear=true`, un gain
    constant. Elle remontait bien le niveau moyen, mais elle RENONCAIT des que
    la crete plafonnait -- et comme le rapport crete/sonie varie enormement d'un
    mot a l'autre, il restait 6 dB d'ecart entre fichiers. Mesure sur le corpus
    deposé : « der Traum » a -11,6 LUFS contre « August » a -18,5. Un mot pouvait
    donc sonner nettement plus faible que la phrase suivante, sans regularite --
    exactement ce qui etait signale a l'usage, et ce que la moyenne cachait.

    La chaine actuelle procede en deux temps :
      1. on pousse le gain qui MANQUE pour atteindre la cible, un limiteur
         absorbant les cretes. C'est lui qui egalise : les fichiers a forte
         crete cessent d'etre penalises.
      2. on rend par un gain simple ce que le limiteur a mange, borne par la
         crete pour ne rien saturer.

    Resultat mesure sur 24 fichiers, moitie mots moitie phrases :
      en ligne avant   moyenne -13,8   ecart-type 1,3   etendue 6,0 dB
      apres            moyenne -14,1   ecart-type 0,7   etendue 3,8 dB
    Meme niveau moyen, variation divisee par deux. C'est l'egalite qui manquait,
    pas le volume.

LES FICHIERS COURTS RECOIVENT PLUS, DELIBEREMENT
    Mesure faite sur le corpus deja egalise : mots -14,6 LUFS et -15,0 dB RMS,
    phrases -14,3 et -14,4. Un tiers de decibel d'ecart, inaudible. Et pourtant
    le mot s'entend plus faible que la phrase qui le suit, de facon constante.

    Ce n'est pas un defaut des fichiers, c'est l'oreille : elle integre la sonie
    sur environ deux secondes. Un mot d'une seconde ne remplit pas cette
    fenetre, une phrase de deux si -- a niveau mesure identique, le mot EST
    percu plus faible. C'est la raison pour laquelle les diffuseurs donnent 2 a
    3 dB de plus aux elements courts qu'au reste du programme : les mesurer
    egaux les rendrait inegaux a l'ecoute.

    On vise donc une cible qui depend de la DUREE. Mais l'avantage se donne en
    BAISSANT LES LONGS, pas en montant les courts : les courts sont deja jammes
    contre le plafond du limiteur, et pousser davantage ne monte plus rien --
    mesure faite, +0,4 dB obtenus sur les +2,5 vises. Une attenuation, elle,
    reussit toujours et ne coute aucune compression. Le corpus sort donc un peu
    plus bas dans l'ensemble, et equilibre a l'oreille.

LE PRIX A PAYER
    Il faut reencoder, donc perdre une generation. Les sources ElevenLabs ne
    sont plus disponibles -- les regenerer couterait 110 000 credits. On
    reencode donc a 96 kbit/s au lieu des 64 d'origine : le debit superieur
    absorbe la perte de la deuxieme generation, pour environ 50 % de poids en
    plus. Sur de la parole mono, l'echange est franchement favorable.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import concurrent.futures

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "audio", "mp3")
MANIFESTE = os.path.join(RACINE, "audio", "manifest.json")
# Les mp3 tels que sortis d ElevenLabs. Toute normalisation part de la, jamais
# du resultat d une normalisation precedente.
SOURCE = os.path.join(RACINE, "audio", "mp3_original")

CIBLE_LUFS = -12.0      # visee du limiteur ; la sortie retombe vers -14
CRETE_MAX = -1.5        # dBTP, marge contre la saturation au decodage
DEBIT = "96k"
PLAFOND_LIMITEUR = 0.95   # -0,45 dBFS, seuil du limiteur du premier temps
BONUS_COURT = 2.5       # dB accordes aux fichiers d une seconde ou moins
SEUIL_LONG = 2.5        # secondes ; au-dela, plus aucun supplement


def ffmpeg():
    for c in ("ffmpeg", os.path.join(
            os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WinGet", "Packages",
            "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe",
            "ffmpeg-9.0.1-full_build", "bin", "ffmpeg.exe")):
        try:
            subprocess.run([c, "-version"], capture_output=True, timeout=30)
            return c
        except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
            continue
    print("  ffmpeg introuvable.")
    sys.exit(1)


FF = None


def mesurer(chemin):
    """Sonie integree, crete et plage, par la premiere passe de loudnorm."""
    r = subprocess.run(
        [FF, "-hide_banner", "-nostats", "-i", chemin,
         "-af", "loudnorm=I=%s:TP=%s:print_format=json" % (CIBLE_LUFS, CRETE_MAX),
         "-f", "null", "-"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S)
    return json.loads(m.group(0)) if m else None


def _ff(src, dst, filtre):
    r = subprocess.run(
        [FF, "-hide_banner", "-nostats", "-y", "-i", src, "-af", filtre,
         "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", DEBIT,
         # -f mp3 explicite : le fichier intermediaire ne porte pas toujours
         # l'extension .mp3, et ffmpeg deduit sinon le format du nom.
         "-f", "mp3", dst],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not os.path.exists(dst):
        _noter_echec(r.stderr)
        return False
    return True


def duree(chemin):
    """Duree en secondes, lue dans l'en-tete par ffmpeg."""
    r = subprocess.run([FF, "-hide_banner", "-nostats", "-i", chemin,
                        "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", r.stderr)
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def bonus_court(d):
    """Le supplement, en dB, qu'un fichier court doit avoir SUR un long pour
    etre percu au meme niveau. Il se realise en attenuant les longs -- voir
    l'en-tete. Lineaire entre les deux bornes : rien ne justifie une courbe
    plus savante, et une marche brusque s'entendrait d'une carte a l'autre."""
    if d <= 1.0:
        return BONUS_COURT
    if d >= SEUIL_LONG:
        return 0.0
    return BONUS_COURT * (SEUIL_LONG - d) / (SEUIL_LONG - 1.0)


def normaliser(chemin, sortie, intermediaire=None):
    """Les deux temps decrits en tete de fichier. Renvoie la mesure d'entree."""
    d = mesurer(chemin)
    if not d:
        return None
    inter = intermediaire or (sortie + ".t1.mp3")
    # L'avantage est relatif : les courts gardent la cible pleine, les longs
    # sont attenues d'autant. Monter etant impossible, on descend.
    cible = CIBLE_LUFS - (BONUS_COURT - bonus_court(duree(chemin)))

    # Temps 1 : viser la cible, le limiteur absorbant ce qui depasse.
    manque = cible - float(d["input_i"])
    f1 = ("volume=%.2fdB,alimiter=level_in=1:level_out=1:limit=%.2f"
          ":attack=5:release=60:level=disabled" % (manque, PLAFOND_LIMITEUR))
    if not _ff(chemin, inter, f1):
        return None

    # Temps 2 : reprendre ce que le limiteur a mange, sans depasser la crete.
    m = mesurer(inter)
    if not m:
        return None
    # Pas de plancher a zero : un gain NEGATIF est exactement ce qu'on veut
    # pour les fichiers longs. La borne de crete ne s'applique qu'a la hausse.
    vise = cible - float(m["input_i"])
    marge = CRETE_MAX - float(m["input_tp"])
    gain = vise if vise < 0 else max(0.0, min(vise, marge))
    ok = _ff(inter, sortie, "volume=%.2fdB" % gain)
    try:
        os.remove(inter)
    except OSError:
        pass
    return d if ok else None


# La premiere erreur rencontree, gardee pour l'afficher a la fin. Un lot qui
# echoue 5 260 fois sans jamais dire pourquoi coute une execution entiere avant
# qu'on sache ce qui cloche.
_PREMIER_ECHEC = []


def _noter_echec(stderr):
    if not _PREMIER_ECHEC and stderr:
        lignes = [l for l in stderr.strip().splitlines() if l.strip()]
        _PREMIER_ECHEC.append("\n".join(lignes[-3:]))


def main():
    global FF
    p = argparse.ArgumentParser()
    p.add_argument("--niveaux", default="")
    p.add_argument("--essai", type=int, default=0,
                   help="ne traiter que N fichiers, dans audio/essai_norm/")
    a = p.parse_args()
    FF = ffmpeg()

    with open(MANIFESTE, encoding="utf-8") as f:
        entrees = json.load(f)
    if a.niveaux:
        niveaux = a.niveaux.split(",")
        entrees = [e for e in entrees if e["niveau"] in niveaux]
    entrees = [e for e in entrees
               if os.path.exists(os.path.join(DOSSIER, e["id"] + ".mp3"))]

    if a.essai:
        dossier = os.path.join(RACINE, "audio", "essai_norm")
        os.makedirs(dossier, exist_ok=True)
        pas = max(1, len(entrees) // a.essai)
        for e in entrees[::pas][:a.essai]:
            src = os.path.join(SOURCE, e["id"] + ".mp3")
            if not os.path.exists(src):
                src = os.path.join(DOSSIER, e["id"] + ".mp3")
            dst = os.path.join(dossier, e["id"] + ".mp3")
            avant = normaliser(src, dst)
            apres = mesurer(dst)
            if not avant or not apres:
                print("  ECHEC  %s" % e["texte"][:40])
                continue
            print("  %-42s %6.1f -> %6.1f LUFS | crete %6.1f -> %6.1f | "
                  "%5d -> %5d o"
                  % (e["texte"][:42], float(avant["input_i"]),
                     float(apres["input_i"]), float(avant["input_tp"]),
                     float(apres["input_tp"]),
                     os.path.getsize(src), os.path.getsize(dst)))
        print("\n  Fichiers dans audio/essai_norm/ — ecoute avant de lancer le lot.")
        return

    # Le lot : on ecrit a cote, puis on remplace. Ecraser en place perdrait
    # l'original si ffmpeg echoue au milieu, et il n'est pas regenerable
    # gratuitement.
    faits = rates = 0
    def traiter(e):
        # TOUJOURS repartir de l'original quand il existe. Relire audio/mp3/,
        # qui contient deja une version normalisee, empilerait une generation
        # d'encodage a chaque essai de reglage -- et la degradation, elle, ne se
        # remonte pas.
        src = os.path.join(SOURCE, e["id"] + ".mp3")
        if not os.path.exists(src):
            src = os.path.join(DOSSIER, e["id"] + ".mp3")
        tmp = os.path.join(DOSSIER, e["id"] + ".mp3.norm.mp3")
        cible = os.path.join(DOSSIER, e["id"] + ".mp3")
        if normaliser(src, tmp):
            os.replace(tmp, cible)
            return True
        if os.path.exists(tmp):
            os.remove(tmp)
        return False

    print("  %d fichiers a normaliser vers %s LUFS, crete %s dBTP, %s\n"
          % (len(entrees), CIBLE_LUFS, CRETE_MAX, DEBIT))
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        for i, ok in enumerate(ex.map(traiter, entrees), 1):
            faits += 1 if ok else 0
            rates += 0 if ok else 1
            if i % 200 == 0 or i == len(entrees):
                print("    %d/%d  (%d rates)" % (i, len(entrees), rates))
    print("\n  %d normalises, %d rates." % (faits, rates))
    if _PREMIER_ECHEC:
        print("\n  Premiere erreur rencontree :\n    %s"
              % _PREMIER_ECHEC[0].replace("\n", "\n    "))
    # Un fichier temporaire abandonne par une interruption serait depose comme
    # les autres : deposer.py le signalerait comme orphelin, mais autant ne pas
    # le laisser.
    restes = [f for f in os.listdir(DOSSIER) if f.endswith(".norm.mp3")]
    if restes:
        print("\n  %d fichiers temporaires nettoyes." % len(restes))
        for f in restes:
            os.remove(os.path.join(DOSSIER, f))
    if faits:
        print("  Redepose ensuite : python audio/deposer.py")


if __name__ == "__main__":
    main()
