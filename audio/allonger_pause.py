# -*- coding: utf-8 -*-
"""Allonge en SILENCE une pause deja presente dans une replique.

    python audio/allonger_pause.py --scene 02-beim-buergeramt --plan 8 --ajout 0.45

POURQUOI CET OUTIL EXISTE
    Le 14 septembre, le plan 08 -- « Sechs Wochen? Ich wohne doch schon
    hier. » -- est sorti avec un « ahhhh » invente de trois secondes et demie.
    Jacques : « le ahhhh est un peu long ». Le contexte (previous_text) l'a
    supprime, mais avec lui LE TEMPS qu'il prenait -- or ce temps etait juste :
    c'est le plan de l'incredulite, le seul qui doive se comprendre sans
    sous-titres, et l'avatar a besoin d'un battement entre les deux phrases.

⚠️ ON LE REND EN SILENCE, PAS EN SON. Un son invente n'est pas dans les
   sous-titres : l'apprenant entendrait quelque chose qui n'est pas ecrit.
   C'est un defaut pour une video d'apprentissage, pas une couleur. Le silence,
   lui, ne ment pas -- et l'avatar a exactement le meme temps pour jouer.

⚠️ ET ON N'ALLONGE QU'UNE PAUSE QUI EXISTE. Le script cherche le plus grand
   trou interne et coupe EN SON MILIEU. Couper au hasard dans une syllabe
   s'entendrait. S'il n'y a pas de trou, il refuse : une pause a fabriquer de
   toutes pieces se demande au modele, pas au montage.

La prise d'origine part dans _ancienne-numerotation/, comme partout ailleurs.
"""
import argparse
import io
import json
import os
import shutil
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import montage as M                                          # noqa: E402
import distance_voix as D                                    # noqa: E402

MINI = 0.08          # un trou plus court qu'un dixieme n'est pas une pause


def plus_grand_trou(x):
    """(debut, duree) du plus grand silence interne, en secondes."""
    w = int(0.020 * D.SR)
    env = np.array([np.sqrt(np.mean(x[i:i + w] ** 2))
                    for i in range(0, len(x) - w, w)])
    seuil = 0.12 * env.max()
    trous, debut = [], None
    for i, v in enumerate(env):
        if v < seuil:
            if debut is None:
                debut = i
        else:
            if debut is not None:
                trous.append((debut * 0.020, (i - debut) * 0.020))
            debut = None
    # On ecarte le silence de tete et de queue : seuls les trous INTERNES
    # comptent, et ils sont les seuls a avoir de la voix des deux cotes.
    internes = [t for t in trous if t[0] > 0.05 and t[1] >= MINI]
    return max(internes, key=lambda t: t[1]) if internes else None


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", required=True)
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--ajout", type=float, default=0.45,
                   help="secondes de silence a inserer (defaut 0,45)")
    a = p.parse_args()

    chemin = os.path.join(RACINE, "scenes", a.scene + ".json")
    d = json.loads(io.open(chemin, encoding="utf-8").read())
    plan = next((x for x in d["plans"] if x["n"] == a.plan), None)
    if plan is None:
        sys.exit("  plan %d absent de la scene." % a.plan)

    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    src = os.path.join(dossier, "%02d-%s.mp3" % (a.plan, plan["locuteur"]))
    if not os.path.exists(src):
        sys.exit("  voix absente : %s" % src)

    ff = M.ffmpeg()
    trou = plus_grand_trou(D.pcm(ff, src))
    if trou is None:
        sys.exit("  aucune pause interne dans cette prise. Une pause a\n"
                 "  fabriquer de toutes pieces se demande au modele, pas ici.")
    debut, duree = trou
    coupe = debut + duree / 2.0
    print("  « %s »" % plan["de"])
    print("  pause trouvee a %.2f s, longue de %.0f ms -> coupe a %.2f s"
          % (debut, duree * 1000, coupe))

    tmp = os.environ.get("TEMP") or "."
    av = os.path.join(tmp, "_ap_a.wav")
    ap = os.path.join(tmp, "_ap_b.wav")
    si = os.path.join(tmp, "_ap_s.wav")
    li = os.path.join(tmp, "_ap.txt")
    subprocess.run([ff, "-y", "-v", "error", "-i", src,
                    "-t", "%.3f" % coupe, av], check=True)
    subprocess.run([ff, "-y", "-v", "error", "-ss", "%.3f" % coupe,
                    "-i", src, ap], check=True)
    subprocess.run([ff, "-y", "-v", "error", "-f", "lavfi", "-i",
                    "anullsrc=r=44100:cl=mono", "-t", "%.3f" % a.ajout, si],
                   check=True)
    with io.open(li, "w", encoding="utf-8", newline="\n") as f:
        for c in (av, si, ap):
            f.write("file '" + c.replace(os.sep, "/") + "'\n")

    garde = os.path.join(dossier, "_ancienne-numerotation")
    os.makedirs(garde, exist_ok=True)
    shutil.copy2(src, os.path.join(garde, "sans-pause-%02d-%s.mp3"
                                   % (a.plan, plan["locuteur"])))
    avant = M.duree(ff, src)
    subprocess.run([ff, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", li, "-c:a", "libmp3lame", "-q:a", "2", src],
                   check=True)
    apres = M.duree(ff, src)
    print("  %.2f s -> %.2f s   (prise d'origine dans _ancienne-numerotation/)"
          % (avant, apres))
    print("\n  Ensuite : python audio/reporter_durees.py --scene %s" % a.scene)


if __name__ == "__main__":
    main()
