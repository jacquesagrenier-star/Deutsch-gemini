# -*- coding: utf-8 -*-
"""Quelle candidate ressemble le MOINS a la voix retenue -- mesure, pas oreille.

    python audio/distance_voix.py <ffmpeg> audio/a_ecouter_voix/mark

RESULTAT DU 13 SEPTEMBRE 2026, sur les trois candidates de Mark :

    VOIX-A  Mark-VD-01   132,2 Hz   1566 Hz   7,66 /s
    VOIX-B  Mark-VD-02   100,9 Hz   1404 Hz   8,70 /s
    VOIX-C  Mark-VD-03   103,9 Hz   1639 Hz   7,03 /s   <- retenue

    Jacques cherchait, parmi les ecartees, celle qui ressemble le moins a la
    voix de Mark, pour servir de voix de service masculine. C'est VOIX-A :
    28 Hz au-dessus, pres d'une quarte, ce qui s'entend comme une autre
    personne. VOIX-B est a 3 Hz de la retenue -- meme hauteur, donc elle
    s'entendrait comme Mark d'une autre couleur.

    ⚠️ ET LA MESURE NE REPOND PAS A LA BONNE QUESTION EN ENTIER. Elle dit
    laquelle ressemble le moins a Mark, pas laquelle fait un bon
    fonctionnaire : VD-01 est plus HAUTE, donc plus jeune a l'oreille,
    alors que le role demande la cinquantaine. On gagne la distinction et
    on perd l'age.

⚠️ CE QUE CA MESURE, ET CE QUE CA NE MESURE PAS.
    La distance acoustique n'est pas l'identite percue. Deux voix peuvent
    differer en hauteur et s'entendre comme la meme personne ; deux autres
    peuvent partager une hauteur et s'entendre comme deux. C'est un PREMIER
    FILTRE, pas un verdict -- le verdict reste l'oreille, a l'aveugle, comme
    le projet le fait depuis le 3 septembre.

TROIS GRANDEURS, ET POURQUOI CELLES-LA
    F0 median      la hauteur de la voix. Le discriminateur le plus robuste,
                   et celui qui s'entend le plus vite : un ecart de 20 Hz sur
                   une voix d'homme s'entend comme un autre age.
    Centroide      la brillance du timbre. Deux voix a la meme hauteur mais
                   de brillance differente ne se confondent pas.
    Debit          syllabes par seconde, approxime par les pics d'energie.
                   Une voix lente ne se prend pas pour une rapide.
"""
import os
import subprocess
import sys

import numpy as np

SR = 16000


def pcm(ffmpeg, chemin):
    out = subprocess.run([ffmpeg, "-v", "error", "-i", chemin, "-ac", "1",
                          "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(out, dtype="<i2").astype(np.float64) / 32768.0
    return x


def f0_median(x):
    """Autocorrelation par fenetre. On ne garde que les fenetres VOISEES :
    inclure le silence et les consonnes sourdes tirerait la mediane n'importe
    ou."""
    w = int(0.040 * SR)
    saut = int(0.010 * SR)
    lo, hi = int(SR / 300.0), int(SR / 60.0)   # 60 a 300 Hz
    vals = []
    seuil = 0.06 * np.sqrt(np.mean(x ** 2))
    for i in range(0, len(x) - w, saut):
        t = x[i:i + w]
        if np.sqrt(np.mean(t ** 2)) < seuil:
            continue
        t = t - t.mean()
        r = np.correlate(t, t, mode="full")[w - 1:]
        if r[0] <= 0:
            continue
        seg = r[lo:hi]
        if len(seg) == 0:
            continue
        k = int(np.argmax(seg)) + lo
        # Une periode franche : sinon c'est du bruit, pas une voyelle.
        if r[k] / r[0] < 0.35:
            continue
        vals.append(SR / float(k))
    return (float(np.median(vals)), len(vals)) if vals else (float("nan"), 0)


def centroide(x):
    w = 1024
    sp, tot = 0.0, 0.0
    freqs = np.fft.rfftfreq(w, 1.0 / SR)
    seuil = 0.06 * np.sqrt(np.mean(x ** 2))
    for i in range(0, len(x) - w, w // 2):
        t = x[i:i + w]
        if np.sqrt(np.mean(t ** 2)) < seuil:
            continue
        m = np.abs(np.fft.rfft(t * np.hanning(w)))
        s = m.sum()
        if s > 0:
            sp += float((freqs * m).sum() / s)
            tot += 1
    return sp / tot if tot else float("nan")


def debit(x):
    """Pics d'enveloppe par seconde -- une approximation du debit syllabique."""
    w = int(0.020 * SR)
    env = np.array([np.sqrt(np.mean(x[i:i + w] ** 2))
                    for i in range(0, len(x) - w, w)])
    if len(env) < 3:
        return float("nan")
    env = env / (env.max() or 1.0)
    pics = sum(1 for i in range(1, len(env) - 1)
               if env[i] > env[i - 1] and env[i] >= env[i + 1] and env[i] > 0.25)
    return pics / (len(x) / SR)


def main():
    ffmpeg, dossier = sys.argv[1], sys.argv[2]
    fichiers = sorted(f for f in os.listdir(dossier) if f.lower().endswith(".mp3"))
    mes = {}
    for f in fichiers:
        x = pcm(ffmpeg, os.path.join(dossier, f))
        f0, n = f0_median(x)
        mes[f] = (f0, centroide(x), debit(x), len(x) / SR, n)

    print("  %-14s %9s %11s %9s %8s" % ("echantillon", "F0 (Hz)", "timbre(Hz)",
                                        "debit/s", "duree"))
    print("  " + "-" * 56)
    for f in fichiers:
        f0, c, d, dur, n = mes[f]
        print("  %-14s %9.1f %11.0f %9.2f %7.2fs" % (f, f0, c, d, dur))
    return mes


if __name__ == "__main__":
    main()
