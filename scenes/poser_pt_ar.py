# -*- coding: utf-8 -*-
"""Pose les sous-titres pt (Brésil) et ar de la série « Mark en Madrid »
(scenes/traductions-es-pt-ar.json) dans scenes/es-0N-*.json, une clé par plan
après « en ». N'écrase jamais un texte déjà posé.

    python scenes/poser_pt_ar.py

Puis, par épisode et par langue (graveur local, aucune dépense) :
    python video/sous_titres.py --scene es-01-llegada-madrid --langue pt --incruster --sortie <...>-st.pt.mp4
"""
import io, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
lot = json.load(io.open(os.path.join(ICI, "traductions-es-pt-ar.json"), encoding="utf-8"))
for scene, langues in lot.items():
    if scene.startswith("_"):
        continue
    chemin = os.path.join(ICI, scene + ".json")
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    crlf = "\r\n" in brut[:200]
    d = json.loads(brut)
    plans = d["plans"]
    for lg, lignes in langues.items():
        if len(lignes) != len(plans):
            sys.exit("%s %s : %d lignes pour %d plans" % (scene, lg, len(lignes), len(plans)))
    poses = 0
    nouveaux = []
    for i, p in enumerate(plans):
        q = {}
        for k, v in p.items():
            q[k] = v
            if k == "en":
                for lg in ("pt", "ar"):
                    if lg in langues and not p.get(lg):
                        q[lg] = langues[lg][i]
                        poses += 1
        nouveaux.append(q)
    d["plans"] = nouveaux
    texte = json.dumps(d, ensure_ascii=False, indent=1)
    if crlf:
        texte = texte.replace("\n", "\r\n")
    fin = "\r\n" if brut.endswith("\r\n") else ("\n" if brut.endswith("\n") else "")
    io.open(chemin, "w", encoding="utf-8", newline="").write(texte + fin)
    print("%s : %d textes posés" % (scene, poses))
