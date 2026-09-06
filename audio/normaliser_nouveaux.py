# -*- coding: utf-8 -*-
"""Normalise UNIQUEMENT les fichiers qui n'ont pas encore d'original archive.

Un fichier sans archive dans audio/mp3_original/ est, par construction, un
fichier qui sort de generer.py et n'est jamais passe par la normalisation.
C'est le critere le plus sur : il ne depend d'aucune date, d'aucune liste
tenue a la main, et il est idempotent -- relancer ce script ne retraite rien.

L'archivage se fait AVANT le traitement. Sans lui, une seconde passe repartirait
du fichier deja normalise et empilerait une generation d'encodage de plus, et
la degradation ne se remonte pas.
"""
import io, json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
import normaliser as N

N.FF = N.ffmpeg()
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP3 = os.path.join(RACINE, "audio", "mp3")

m = json.load(io.open(os.path.join(RACINE, "audio", "manifest.json"), encoding="utf-8"))
vises = [e for e in m
         if os.path.exists(os.path.join(MP3, e["id"] + ".mp3"))
         and not os.path.exists(os.path.join(N.SOURCE, e["id"] + ".mp3"))]
print("a normaliser :", len(vises), flush=True)

os.makedirs(N.SOURCE, exist_ok=True)
avant, apres, rates = [], [], 0
for i, e in enumerate(vises, 1):
    cible = os.path.join(MP3, e["id"] + ".mp3")
    src = os.path.join(N.SOURCE, e["id"] + ".mp3")
    shutil.copy2(cible, src)
    tmp = cible + ".norm.mp3"
    a = N.normaliser(src, tmp)
    if not a:
        rates += 1
        if os.path.exists(tmp): os.remove(tmp)
        continue
    p = N.mesurer(tmp)
    os.replace(tmp, cible)
    avant.append(float(a["input_i"]))
    if p: apres.append(float(p["input_i"]))
    if i % 100 == 0: print("  %d/%d" % (i, len(vises)), flush=True)

print("normalises : %d, rates : %d" % (len(avant), rates))
if avant: print("avant : moyenne %.1f LUFS (min %.1f, max %.1f)" % (sum(avant)/len(avant), min(avant), max(avant)))
if apres: print("apres : moyenne %.1f LUFS (min %.1f, max %.1f)" % (sum(apres)/len(apres), min(apres), max(apres)))
