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

SONIE, PAS CRETE
    On vise l'EBU R128 (`loudnorm`), qui mesure la sonie percue en excluant les
    silences, et non le simple maximum. Une normalisation par la crete rendrait
    plus faible un mot ou la voix marque une consonne forte, et plus fort un
    mot murmure -- l'inverse de ce qu'on cherche. `linear=true` demande un gain
    constant plutot qu'une compression : on remonte le niveau, on n'ecrase pas
    la dynamique de la voix.

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

CIBLE_LUFS = -16.0      # standard parole mono
CRETE_MAX = -1.5        # dBTP, marge contre la saturation au decodage
DEBIT = "96k"


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


def normaliser(chemin, sortie):
    """Deuxieme passe, gain lineaire calcule sur la mesure."""
    d = mesurer(chemin)
    if not d:
        return None
    filtre = ("loudnorm=I=%s:TP=%s:linear=true"
              ":measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s"
              % (CIBLE_LUFS, CRETE_MAX, d["input_i"], d["input_tp"],
                 d["input_lra"], d["input_thresh"]))
    # -f mp3 explicite : le fichier de sortie du lot s'appelle « ....mp3.norm »
    # le temps d'etre ecrit, et ffmpeg deduit sinon le format de l'extension.
    # Sans ce drapeau il refuse les 5 260, un par un, en silence.
    r = subprocess.run(
        [FF, "-hide_banner", "-nostats", "-y", "-i", chemin, "-af", filtre,
         "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", DEBIT,
         "-f", "mp3", sortie],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not os.path.exists(sortie):
        _noter_echec(r.stderr)
        return None
    return d


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
        src = os.path.join(DOSSIER, e["id"] + ".mp3")
        tmp = src + ".norm.mp3"
        if normaliser(src, tmp):
            os.replace(tmp, src)
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
