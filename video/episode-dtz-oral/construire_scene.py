# -*- coding: utf-8 -*-
"""Fabrique scenes/dtz-oral.json depuis la page de l'oral (visuel/prototype/dtz-oral.html), SOURCE UNIQUE.

    python video/episode-dtz-oral/construire_scene.py

Les repliques vivent dans la page (objet L : id -> [locuteur, allemand, francais]). Les recopier ici les ferait
diverger le jour ou la relecture germanophone en corrige une : on les lit donc dans la page, et on fabrique la scene
que lisent audio/scene_audio.py (les voix) et video/omnihuman.py (les clips). Le numero de plan suit l'ordre de L ;
la table PLANS (dtz/plans.json) relie chaque id a son numero, pour la page.

Voix : celles de la serie (personnages.json), en multilingual v2 pour les deux (decision du 3 nov. 2026 : « B :
video », chiffree en v2). Mark parlait en v3 dans les episodes 03-05 pour les balises de jeu ; ici aucune balise.
"""
import io
import json
import os
import re
import subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PAGE = os.path.join(RACINE, "visuel", "prototype", "dtz-oral.html")

# Les repliques qui deviennent des CLIPS (variante B) : Anna partout, Mark pour la planification seulement. Ses deux
# reponses-modeles (presentation, photo) restent en photo et voix.
SANS_VIDEO = {"m_vorstellung", "m_foto"}


def lire_L():
    s = io.open(PAGE, encoding="utf-8").read()
    bloc = re.search(r"const L = (\{[\s\S]*?\n\});", s).group(1)
    js = "process.stdout.write(JSON.stringify(" + bloc + "))"
    sortie = subprocess.run(["node", "-e", js], capture_output=True, check=True)
    return json.loads(sortie.stdout.decode("utf-8"))


def main():
    L = lire_L()
    plans, table = [], {}
    for n, (cle, (qui, de, fr)) in enumerate(L.items(), 1):
        plans.append({"n": n, "id": cle, "locuteur": qui, "de": de, "fr": fr, "video": cle not in SANS_VIDEO})
        table[cle] = n
    scene = {
        "_format": "Fabrique par video/episode-dtz-oral/construire_scene.py depuis visuel/prototype/dtz-oral.html : ne pas corriger ici.",
        "id": "dtz-oral",
        "situation": "DTZ, l'oral en repetition : Anna joue l'examinatrice, Mark l'autre candidat",
        "duree": 0,
        "locuteurs": {
            "anna": {"nom": "Anna", "voix": "anna-vd-01", "voice_id": "92qyovlOYJE0EVmWB0fA", "modele": "v2"},
            "mark": {"nom": "Mark", "voix": "mark-vd-03", "voice_id": "J8ovlSvQ5WTDCCxIM8U0", "modele": "v2"},
        },
        "plans": plans,
    }
    io.open(os.path.join(RACINE, "scenes", "dtz-oral.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(scene, ensure_ascii=False, indent=1) + "\n")
    os.makedirs(os.path.join(RACINE, "visuel", "prototype", "dtz"), exist_ok=True)
    io.open(os.path.join(RACINE, "visuel", "prototype", "dtz", "plans.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    print("%d repliques, dont %d en video (%d caracteres)" % (
        len(plans), sum(p["video"] for p in plans), sum(len(p["de"]) for p in plans)))


if __name__ == "__main__":
    main()
