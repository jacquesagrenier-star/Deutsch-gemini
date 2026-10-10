# -*- coding: utf-8 -*-
"""Refait scene-<nom>.js a partir des zones et du corpus.

    python visuel/prototype/construire.py                       # la classe
    python visuel/prototype/construire.py arztpraxis            # une autre scene
    python visuel/prototype/construire.py arztpraxis --grille   # + une image de controle

UNE SCENE = UN FICHIER <nom>.points.json
    Les zones, mais aussi tout ce qui est propre a la scene : son titre, son
    texte alternatif, la consigne A1, les mots exclus de « Trouve ! » et les
    questions A2-C1. index.html ne connait aucune scene ; il charge celle
    qu'on lui nomme (?scene=arztpraxis). Ajouter une scene = ajouter un
    fichier, jamais recopier la page.

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


def corpus_cat(fichier, cle):
    """Les mots d'un fichier rangé par niveau (verbe.json, adjectif.json)."""
    d = json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8"))
    return {e[cle] for niv in d.values() for e in niv if e.get(cle)}


def decouper(pts, nom, g):
    """L'image NETTE d'un gros plan : le cadre decoupe dans la source a sa
    pleine resolution, au lieu de la scene web (1080 px) etiree.

    Le visage de Mark fait ~150 px dans la scene web et ~210 dans la source :
    pas de miracle, mais 40 % de pixels en plus pour le meme ecran. Le vrai
    remede reste une image du visage generee pour le gros plan."""
    from PIL import Image
    fichier = "%s-%s.webp" % (nom, g["id"])
    chemin = os.path.normpath(os.path.join(ICI, pts["source"]))
    if os.path.exists(chemin):
        src = Image.open(chemin).convert("RGB")
        W, H = src.size
        x, y, w, h = g["cadre"]
        boite = (round(W * x / 100), round(H * y / 100),
                 round(W * (x + w) / 100), round(H * (y + h) / 100))
        src.crop(boite).save(os.path.join(ICI, fichier), quality=88)
    elif os.path.exists(os.path.join(ICI, fichier)):
        # Une session cloud n'a pas la source (hors du depot) : on garde
        # l'image deja decoupee. Juste tant que le CADRE n'a pas change --
        # sinon, refaire la construction en local.
        print("  source absente : %s garde telle quelle (cadre inchange ?)" % fichier)
    else:
        sys.exit("  source absente (%s) et pas de %s" % (chemin, fichier))
    # ⚠️ L'ADRESSE CHANGE AVEC LE CADRE. Le 6 oct. 2026, le telephone de
    #    Jacques a garde en cache l'ANCIENNE image du visage et recu le
    #    NOUVEAU cadre : les cercles des yeux tombaient a cote des yeux. Avec
    #    le cadre dans l'adresse, une image ne peut plus servir un autre
    #    cadre que le sien.
    import hashlib
    empreinte = hashlib.md5(json.dumps([g["cadre"], pts["source"]]).encode()).hexdigest()[:8]
    return "%s?c=%s" % (fichier, empreinte)


def main():
    noms = [a for a in sys.argv[1:] if not a.startswith("--")]
    nom = noms[0] if noms else "klassenzimmer"
    pts = json.load(io.open(os.path.join(ICI, nom + ".points.json"),
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
        # Une zone en ellipses (une partie du corps) a les rectangles de ses
        # ellipses ; c'est d'eux que l'app tire la place de l'etiquette.
        boites = p.get("boites") or ([p["boite"]] if "boite" in p else
                                     [[cx - rx, cy - ry, 2 * rx, 2 * ry]
                                      for cx, cy, rx, ry in p["ellipses"]])
        for (x, y, w, h) in boites:
            if x < 0 or y < 0 or x + w > 100.01 or y + h > 100.01:
                sys.exit("  %s : boite hors de l'image %r" % (p["id"], [x, y, w, h]))
        sortie.append({
            "id": p["id"], "mot": m["mot"], "genre": m.get("genre"),
            "pluriel": m.get("pluriel"), "fr": m.get("traduction"),
            "en": m.get("traduction_en"), "niveau": m["niveau"],
            "theme": m["theme"], "personne": p.get("personne"),
            "aussi": [{"mot": a, "genre": idx[a].get("genre"),
                       "fr": idx[a].get("traduction"), "niveau": idx[a]["niveau"],
                       "theme": idx[a]["theme"]}
                      for a in p.get("aussi", [])],
            "sur": p.get("sur"), "devant": p.get("devant", 0),
            "boites": boites})
    # LES GROS PLANS (Jacques, 6 oct.) : toucher le visage du prof l'agrandit,
    # et ses parties -- l'oeil, le nez, la bouche -- deviennent des cibles a
    # la taille du doigt. Une partie est une ellipse [cx, cy, rx, ry] en % de
    # l'image, pas un masque : SAM detoure une personne, pas son oreille. Elle
    # est soit un mot NOUVEAU (« mot »), soit une zone existante vue de pres
    # (« ref » : les lunettes, la barbe).
    gros = []
    for g in pts.get("gros_plans", []):
        formes = {}
        for q in g["parties"]:
            cx, cy, rx, ry = q["forme"]
            if "ref" in q:
                formes[q["ref"]] = q["forme"]
                continue
            m = idx.get(q["mot"])
            if not m:
                manquants.append(q["mot"])
                continue
            formes[q["id"]] = q["forme"]
            sortie.append({
                "id": q["id"], "mot": m["mot"], "genre": m.get("genre"),
                "pluriel": m.get("pluriel"), "fr": m.get("traduction"),
                "en": m.get("traduction_en"), "niveau": m["niveau"],
                "theme": m["theme"], "personne": None, "aussi": [],
                "sur": g["personne"], "devant": 0, "detail": g["id"],
                "boites": [[cx - rx, cy - ry, 2 * rx, 2 * ry]]})
        entree = {"id": g["id"], "declencheur": g["declencheur"],
                  "cadre": g["cadre"], "formes": formes}
        if g.get("net"):
            entree["image"] = decouper(pts, nom, g)
        gros.append(entree)

    connus = {p["id"] for p in sortie}
    for p in sortie:
        if p["sur"] and p["sur"] not in connus:
            sys.exit("  %s : sur=%r ne designe aucune zone" % (p["id"], p["sur"]))
    for g in gros:
        for z in g["formes"]:
            if z not in connus:
                sys.exit("  %s : la partie %r ne designe aucune zone" % (g["id"], z))
    if manquants:
        sys.exit("  absents du corpus : %s" % ", ".join(manquants))

    # Les questions A2-C1 visent des zones par leur id (f = l'objet de la
    # question, r = sa reference) : une faute de frappe ne doit pas attendre
    # qu'on tombe sur la question pour se voir.
    for niv, c in pts.get("couches", {}).items():
        for q in c.get("qs", []):
            for cle in ("f", "r"):
                if q.get(cle) and q[cle] not in connus:
                    sys.exit("  %s, << %s >> : %s=%r ne designe aucune zone"
                             % (niv, q["q"], cle, q[cle]))

    # LE MOT QU'UNE QUESTION FAIT TRAVAILLER (« revise »). Dans la seance, la
    # reponse compte comme une revision de ce mot (repetition espacee). La cle
    # est posee A LA MAIN, et seulement quand un mot est clairement en jeu :
    # « Der Rucksack ___ unter dem Tisch » travaille stehen, un pronom
    # relatif ne travaille aucun mot du corpus -- et mieux vaut ne rien noter
    # qu'enregistrer une revision fausse. Le mot doit exister dans le corpus
    # (nom de themes.json, verbe de verbe.json, adjectif d'adjectif.json) :
    # on le resout ici, l'app n'a plus qu'a le retrouver.
    verbes, adjectifs = corpus_cat("verbe.json", "infinitif"), corpus_cat("adjectif.json", "mot")
    couches = json.loads(json.dumps(pts.get("couches", {})))
    for niv, c in couches.items():
        for q in c.get("qs", []):
            mot = q.get("revise")
            if not mot:
                continue
            if mot in idx:
                q["revise"] = {"mot": mot, "genre": idx[mot].get("genre"),
                               "theme": idx[mot]["theme"]}
            elif mot in verbes:
                q["revise"] = {"mot": mot, "cat": "verbe"}
            elif mot in adjectifs:
                q["revise"] = {"mot": mot, "cat": "adjectif"}
            else:
                sys.exit("  %s, << %s >> : revise=%r absent du corpus"
                         % (niv, q["q"], mot))

    scene = {"image": pts["image"], "points": sortie, "grosPlans": gros}
    for cle in ("titre", "alt", "consigne", "exclus", "couches", "corps", "autre_vue",
                "vues", "nom_vue"):
        if cle in pts:
            scene[cle] = pts[cle]
    if "couches" in pts:
        scene["couches"] = couches
    js = ("// GENERE par construire.py -- ne pas modifier a la main.\n"
          "window.SCENE = " + json.dumps(scene, ensure_ascii=False, indent=1)
          + ";\n")
    io.open(os.path.join(ICI, "scene-%s.js" % nom), "w",
            encoding="utf-8").write(js)
    print("  %d zones -> scene-%s.js" % (len(sortie), nom))

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
        chemin = os.path.join(os.environ.get("TMP", ICI), "zones-%s.png" % nom)
        im.save(chemin)
        print("  controle : %s" % chemin)


if __name__ == "__main__":
    main()
