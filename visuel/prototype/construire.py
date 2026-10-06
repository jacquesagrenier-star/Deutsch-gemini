# -*- coding: utf-8 -*-
"""Refait scene-klassenzimmer.js a partir des zones et du corpus.

    python visuel/prototype/construire.py            # ecrit le .js
    python visuel/prototype/construire.py --grille   # + une image de controle

POURQUOI UN .js ET PAS UN .json
    Le prototype doit s'ouvrir en double-cliquant le fichier. Or un navigateur
    refuse fetch() sur file:// ; un <script src> passe. Dans l'app, ce sera un
    JSON charge par urlDonnees(), comme les autres donnees.

LE GENRE ET LA TRADUCTION VIENNENT DU CORPUS, JAMAIS DES ZONES
    C'est toute l'idee : une scene ne fait que POINTER des mots qui existent
    deja. Un mot absent de themes.json arrete la construction -- sinon la scene
    enseignerait un mot que la repetition espacee ne connait pas.

--grille dessine les boites sur l'image : la seule facon de verifier qu'une
zone ecrite a la main tombe sur son objet.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))


def corpus():
    themes = json.load(io.open(os.path.join(RACINE, "themes.json"),
                               encoding="utf-8"))["themes"]
    idx = {}
    for t in themes:
        for m in t["mots"]:
            # Premiere occurrence = le niveau le plus bas ou le mot apparait.
            idx.setdefault(m["mot"], dict(m, theme=t["id"],
                                          niveau=t.get("niveau")))
    return idx


def main():
    pts = json.load(io.open(os.path.join(ICI, "klassenzimmer.points.json"),
                            encoding="utf-8"))
    idx = corpus()
    sortie, manquants = [], []
    for p in pts["points"]:
        m = idx.get(p["mot"])
        if not m:
            manquants.append(p["mot"])
            continue
        absents = [a for a in p.get("aussi", []) if a not in idx]
        if absents:
            manquants.extend(absents)
            continue
        boites = p.get("boites") or [p["boite"]]
        for (x, y, w, h) in boites:
            if x < 0 or y < 0 or x + w > 100.01 or y + h > 100.01:
                sys.exit("  %s : boite hors de l'image %r" % (p["id"], [x, y, w, h]))
        sortie.append({
            "id": p["id"], "mot": m["mot"], "genre": m.get("genre"),
            "pluriel": m.get("pluriel"), "fr": m.get("traduction"),
            "en": m.get("traduction_en"), "niveau": m["niveau"],
            "theme": m["theme"], "personne": p.get("personne"),
            "aussi": [{"mot": a, "genre": idx[a].get("genre"),
                       "fr": idx[a].get("traduction")}
                      for a in p.get("aussi", [])],
            "sur": p.get("sur"), "devant": p.get("devant", 0),
            "boites": boites})
    connus = {p["id"] for p in sortie}
    for p in sortie:
        if p["sur"] and p["sur"] not in connus:
            sys.exit("  %s : sur=%r ne designe aucune zone" % (p["id"], p["sur"]))
    if manquants:
        sys.exit("  absents du corpus : %s" % ", ".join(manquants))

    js = ("// GENERE par construire.py -- ne pas modifier a la main.\n"
          "window.SCENE = " + json.dumps(
              {"image": pts["image"], "points": sortie},
              ensure_ascii=False, indent=1) + ";\n")
    io.open(os.path.join(ICI, "scene-klassenzimmer.js"), "w",
            encoding="utf-8").write(js)
    print("  %d zones -> scene-klassenzimmer.js" % len(sortie))

    if "--grille" in sys.argv:
        from PIL import Image, ImageDraw
        im = Image.open(os.path.join(ICI, pts["image"])).convert("RGB")
        W, H = im.size
        d = ImageDraw.Draw(im)
        for p in sortie:
            for (x, y, w, h) in p["boites"]:
                r = [W * x / 100, H * y / 100, W * (x + w) / 100, H * (y + h) / 100]
                d.rectangle(r, outline=(255, 210, 0), width=3)
                d.text((r[0] + 4, r[1] + 3), p["mot"], fill=(255, 255, 0))
        chemin = os.path.join(os.environ.get("TMP", ICI), "zones.png")
        im.save(chemin)
        print("  controle : %s" % chemin)


if __name__ == "__main__":
    main()
