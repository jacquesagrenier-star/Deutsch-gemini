# -*- coding: utf-8 -*-
"""Egalise une scene PAR VOIX, et releve les fins de phrase qui retombent.

    python audio/egaliser_voix.py --scene es-02-el-carro            (mesure seule)
    python audio/egaliser_voix.py --scene es-02-el-carro --appliquer

POURQUOI (21 oct. 2026). Jacques, sur la serie espagnole : « la voix est plus
elevee, puis ensuite ca baisse trop ». Mesure : le narrateur de l'episode 1
tournait a -18 LUFS contre -11 a -12 pour Ana et Mark (6 dB), et la voisine de
l'episode 2 perdait jusqu'a 6,6 dB entre la premiere et la seconde moitie d'une
replique.

scene_audio.py applique UN gain a toute la scene, expres : il garde les ecarts
entre les repliques (voir son en-tete). C'est juste entre deux repliques d'une
MEME voix ; c'est faux entre deux VOIX, quand l'une sort de son generateur six
decibels sous l'autre -- ce n'est pas du jeu, c'est un ecart de fabrication.

Donc, en partant des pistes BRUTES (_brut/, jamais des pistes deja egalisees) :
  1. une compression douce (2:1 au-dessus de -26 dBFS) qui releve les fins de
     phrase sans aplatir l'attaque ;
  2. un gain PAR VOIX, qui met chaque locuteur a -14 LUFS sur l'ensemble de ses
     repliques -- les ecarts entre ses repliques restent les siens ;
  3. le meme limiteur que scene_audio.py.
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
CIBLE = -14.0
COMPRESSION = "acompressor=threshold=-26dB:ratio=2:attack=15:release=250:makeup=1"


def sonie(fichiers):
    """Sonie integree de plusieurs fichiers mis bout a bout."""
    entrees = []
    for f in fichiers:
        entrees += ["-i", f]
    filtre = "".join("[%d:a]" % i for i in range(len(fichiers))) + \
        "concat=n=%d:v=0:a=1,ebur128" % len(fichiers)
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats"] + entrees +
                       ["-filter_complex", filtre, "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--appliquer", action="store_true")
    a = ap.parse_args()
    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    m = json.load(io.open(os.path.join(dossier, "manifeste.json"), encoding="utf-8"))
    brut = os.path.join(dossier, "_brut")
    comp = os.path.join(brut, "_comprime")
    os.makedirs(comp, exist_ok=True)

    # 1. compression, replique par replique
    for x in m["plans"]:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(brut, x["fichier"]),
                        "-af", COMPRESSION, "-ar", "44100", "-b:a", "192k",
                        os.path.join(comp, x["fichier"])], check=True)

    # 2. un gain par voix
    voix = sorted({x["locuteur"] for x in m["plans"]})
    gains = {}
    for v in voix:
        fs = [os.path.join(comp, x["fichier"]) for x in m["plans"] if x["locuteur"] == v]
        mesure = sonie(fs)
        gains[v] = CIBLE - mesure
        print("  %-10s %d replique(s)  %.1f LUFS apres compression -> gain %+.1f dB"
              % (v, len(fs), mesure, gains[v]))
    if not a.appliquer:
        print("\n  Mesure seule. Relancer avec --appliquer.")
        return

    # 3. gain + limiteur, vers les pistes finales
    for x in m["plans"]:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(comp, x["fichier"]),
                        "-af", "volume=%.2fdB,alimiter=limit=0.891" % gains[x["locuteur"]],
                        "-ar", "44100", "-b:a", "192k", os.path.join(dossier, x["fichier"])], check=True)
    m["egalisation"] = {"methode": "par voix, audio/egaliser_voix.py", "compression": COMPRESSION,
                        "cible_lufs": CIBLE, "gains_db": {k: round(g, 2) for k, g in gains.items()}}
    io.open(os.path.join(dossier, "manifeste.json"), "w", encoding="utf-8", newline="").write(
        json.dumps(m, ensure_ascii=False, indent=2) + "\n")
    print("\n  %d pistes egalisees dans audio/scenes/%s/" % (len(m["plans"]), a.scene))


if __name__ == "__main__":
    main()
