# -*- coding: utf-8 -*-
"""Assemble l'episode : les 19 plans dans l'ordre, chacun avec sa replique.

    python video/montage.py --scene 01-ankunft-berlin

CE QU'IL FAIT, ET CE QU'IL NE FAIT PAS
    Il colle bout a bout les clips de 03-final/ dans l'ordre du scenario et
    pose sur chacun sa piste ElevenLabs. Il ne fait NI lip-sync NI
    sous-titres : le lip-sync se fait avant, plan par plan, chez sync.so, et
    les sous-titres sont affiches par l'application, pas incrustes.

    C'est donc un montage de travail -- celui qui permet de voir l'episode
    pour la premiere fois et de juger le rythme.

LE SILENCE AVANT ET APRES CHAQUE REPLIQUE
    Les clips durent 4 a 7 secondes, les repliques 1,5 a 7. L'ecart n'est pas
    du gaspillage : un plan ne peut pas commencer sur la premiere syllabe ni
    finir sur la derniere. On pose donc la voix avec un retard (AMORCE), et
    ce qui reste apres elle est la respiration du plan.

    Si la replique est plus longue que le clip -- ca arrive, plan 13 -- on
    part a zero et on laisse deborder : mieux vaut une fin serree qu'une
    phrase coupee.

ON NE REENCODE LA VIDEO QU'UNE FOIS
    Chaque plan est mux avec son audio sans toucher au flux video (-c:v copy).
    Le seul reencodage a lieu au collage final, et il est inevitable : les
    clips viennent tous du meme modele avec les memes reglages, mais concat
    exige un flux continu.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Le retard de la voix sur le debut du plan. Assez pour qu'on voie le
# personnage avant qu'il parle, assez peu pour que le plan ne traine pas.
AMORCE = 0.35


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def duree(ff, chemin):
    r = subprocess.run([ff, "-hide_banner", "-i", chemin],
                       capture_output=True, text=True, errors="replace")
    m = re.search(r"Duration: \d+:(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 60 + float(m.group(2)) if m else None


def ff(cmd, quoi):
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  echec sur %s :\n%s" % (quoi, r.stderr[-700:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    a = ap.parse_args()

    F = ffmpeg()
    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    dv = os.path.join(RACINE, "video", "episode-" + a.scene)
    da = os.path.join(RACINE, "audio", "scenes", a.scene)
    tmp = os.path.join(dv, "_montage")
    os.makedirs(tmp, exist_ok=True)

    morceaux = []
    print("  plan   clip    voix   %s" % "assemblage")
    for p in d["plans"]:
        v = os.path.join(dv, "03-final", "plan%02d.mp4" % p["n"])
        s = os.path.join(da, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  Plan %02d : clip manquant (%s)" % (p["n"], os.path.basename(v)))
        if not os.path.exists(s):
            sys.exit("  Plan %02d : replique manquante (%s)" % (p["n"], os.path.basename(s)))

        dv_, da_ = duree(F, v), duree(F, s)
        # La voix tient-elle avec l'amorce ? Sinon on la colle au debut.
        amorce = AMORCE if (da_ + AMORCE) <= dv_ else 0.0
        note = "" if amorce else "  <- voix au ras, la replique remplit le plan"

        out = os.path.join(tmp, "plan%02d.mp4" % p["n"])
        # La replique deborde-t-elle du clip ? Alors on garde toute la voix et
        # l'image tient jusqu'a sa fin ; sinon on coupe a la duree du clip.
        borne = ["-shortest"] if (da_ + amorce) > dv_ else ["-t", "%.3f" % dv_]
        ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
            "-i", v, "-itsoffset", "%.3f" % amorce, "-i", s,
            "-map", "0:v", "-map", "1:a", "-c:v", "copy",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100"]
           + borne + [out], "plan %02d" % p["n"])
        morceaux.append(out)
        print("  %02d    %5.2f  %5.2f   +%.2f%s" % (p["n"], dv_, da_, amorce, note))

    liste = os.path.join(tmp, "_liste.txt")
    io.open(liste, "w", encoding="utf-8", newline="").write(
        "".join("file '%s'\n" % os.path.basename(m) for m in morceaux))

    final = os.path.join(dv, "EPISODE-%s.mp4" % a.scene.split("-")[0])
    ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", liste,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
        final], "collage final")

    print("\n  %s" % os.path.relpath(final, RACINE))
    print("  %.1f secondes, %d plans" % (duree(F, final), len(morceaux)))


if __name__ == "__main__":
    main()
