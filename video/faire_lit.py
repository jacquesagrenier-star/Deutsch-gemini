# -*- coding: utf-8 -*-
"""Un lit d'ambiance de hall d'aeroport, fabrique sur place.

    python video/faire_lit.py --duree 40

⚠️ C'EST UN PROVISOIRE, ET IL FAUT LE DIRE. Le vrai lit se genere chez
   ElevenLabs (SFX V2, boucle activee) avec le prompt garde dans
   audio/ambiance/_prompts.txt. Celui-ci existe pour qu'on puisse entendre
   le montage complet -- niveaux, placement de l'annonce, equilibre -- sans
   attendre. Il se remplace par un fichier, pas par une reecriture.

CE QUE C'EST, TECHNIQUEMENT
    Un hall est du bruit filtre plus une longue reverberation. On empile :
      - un souffle grave continu (la ventilation, le lointain de la piste)
      - une bande medium tres attenuee, lentement modulee (la foule)
      - des transitoires rares (roulettes de valise, pas lointains)
    puis une reverberation par echos multiples, et un fondu aux deux bouts.

⚠️ AUCUNE VOIX. Un lit qui contient de la parole intelligible entre en
   concurrence avec la lecon -- c'est la meme regle que pour l'annonce.
"""
import argparse
import math
import os
import random
import struct
import subprocess
import sys
import wave

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

SR = 44100


def passe_bas(x, a):
    y, v = [0.0] * len(x), 0.0
    for i, e in enumerate(x):
        v += a * (e - v)
        y[i] = v
    return y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--duree", type=float, default=40.0)
    ap.add_argument("--sortie")
    a = ap.parse_args()
    random.seed(20260912)

    n = int(SR * a.duree)
    brut = [random.uniform(-1, 1) for _ in range(n)]

    grave = passe_bas(passe_bas(brut, 0.006), 0.006)        # ventilation
    medium = passe_bas(brut, 0.05)                          # la foule, lointaine
    medium = [m - g for m, g in zip(medium, passe_bas(medium, 0.002))]

    x = [0.0] * n
    for i in range(n):
        t = i / float(SR)
        # la foule respire : deux modulations lentes, incommensurables
        souffle = 0.75 + 0.25 * math.sin(2 * math.pi * t / 7.3) \
                       + 0.10 * math.sin(2 * math.pi * t / 3.1)
        x[i] = 6.0 * grave[i] + 0.55 * medium[i] * souffle

    # ⚠️ Des transitoires RARES et lointaines : sans elles le lit sonne comme
    # un ventilateur ; trop nombreuses, il sonne comme une gare.
    for _ in range(int(a.duree * 1.6)):
        d = random.randrange(0, n - SR // 2)
        duree = random.uniform(0.05, 0.22)
        f = random.uniform(900, 2600)
        amp = random.uniform(0.015, 0.05)
        for k in range(int(SR * duree)):
            env = math.exp(-k / (SR * duree * 0.25))
            x[d + k] += amp * env * math.sin(2 * math.pi * f * k / SR) \
                        * random.uniform(0.4, 1.0)

    # reverberation : quatre retards inegaux, sinon on entend un peigne
    y = list(x)
    for retard, gain in ((0.037, 0.32), (0.061, 0.24), (0.089, 0.18), (0.131, 0.12)):
        d = int(SR * retard)
        for i in range(d, n):
            y[i] += gain * y[i - d]

    crete = max(abs(v) for v in y) or 1.0
    f_in, f_out = int(SR * 1.5), int(SR * 2.0)
    ech = []
    for i, v in enumerate(y):
        g = 0.28 / crete
        if i < f_in:
            g *= i / float(f_in)
        if i > n - f_out:
            g *= (n - i) / float(f_out)
        ech.append(max(-32767, min(32767, int(v * g * 32767))))

    dst = a.sortie or os.path.join(RACINE, "audio", "ambiance", "hall-provisoire.mp3")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    tmp = dst + ".wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(struct.pack("<%dh" % len(ech), *ech))
    F = M.ffmpeg()
    subprocess.run([F, "-y", "-v", "error", "-i", tmp, "-b:a", "192k", dst],
                   check=True)
    os.remove(tmp)
    print("  %s  (%.1f s)" % (os.path.relpath(dst, RACINE), a.duree))
    print("  ⚠️ Provisoire. Le vrai lit vient d'ElevenLabs SFX, en boucle.")


if __name__ == "__main__":
    main()
