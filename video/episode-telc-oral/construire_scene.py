# -*- coding: utf-8 -*-
"""Fabrique scenes/telc-oral.json depuis la page de l'oral du telc (visuel/prototype/telc/oral.html), SOURCE UNIQUE.

    python video/episode-telc-oral/construire_scene.py

Seules les repliques ecrites pour le telc (id « t_... ») : les autres sont celles du DTZ, deja filmees. Le numero de
plan suit l'ordre de L. Memes voix que l'oral du DTZ (personnages.json), en multilingual v2.
Accord de Jacques dans la session de l'oral, 8 nov. 2026 : « Oui, fabrique » (35 clips, plafond 30 $ et 7 400 credits).
"""
import io
import json
import os
import re
import subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PAGE = os.path.join(RACINE, "visuel", "prototype", "telc", "oral.html")


def lire_L():
    s = io.open(PAGE, encoding="utf-8").read()
    bloc = re.search(r"const L = (\{[\s\S]*?\n\});", s).group(1)
    js = "process.stdout.write(JSON.stringify(" + bloc + "))"
    sortie = subprocess.run(["node", "-e", js], capture_output=True, check=True)
    return json.loads(sortie.stdout.decode("utf-8"))


def main():
    L = lire_L()
    plans = []
    for cle, ligne in L.items():
        if cle.startswith("t_"):
            plans.append({"n": len(plans) + 1, "id": cle, "locuteur": ligne[0], "de": ligne[1], "fr": ligne[2], "video": True})
    scene = {
        "_format": "Fabrique par video/episode-telc-oral/construire_scene.py depuis visuel/prototype/telc/oral.html : ne pas corriger ici.",
        "id": "telc-oral",
        "situation": "telc A2-B1, l'oral en repetition : Anna joue l'examinatrice, Mark l'autre candidat",
        "duree": 0,
        "locuteurs": {
            "anna": {"nom": "Anna", "voix": "anna-vd-01", "voice_id": "92qyovlOYJE0EVmWB0fA", "modele": "v2"},
            "mark": {"nom": "Mark", "voix": "mark-vd-03", "voice_id": "J8ovlSvQ5WTDCCxIM8U0", "modele": "v2"},
        },
        "plans": plans,
    }
    io.open(os.path.join(RACINE, "scenes", "telc-oral.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(scene, ensure_ascii=False, indent=1) + "\n")
    print("%d repliques (%d caracteres)" % (len(plans), sum(len(p["de"]) for p in plans)))


if __name__ == "__main__":
    main()
