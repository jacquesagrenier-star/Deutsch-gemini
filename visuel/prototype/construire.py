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

LES TRADUCTIONS (10 oct. 2026) : traductions/<nom>.<langue>.json
    Le contenu ecrit en francais (alt, consigne, nom de la vue, bouton de
    l'autre vue, titres des couches, explication « n » de chaque question) a
    sa traduction en en / tr / uk / fa / ar dans un fichier A PART, pas dans
    le points.json : les questions sont relues sur main, et deux mains dans
    le meme fichier font des conflits. L'allemand ne se traduit jamais.
    Chaque entree garde le FRANCAIS SOURCE a cote de sa traduction. Si le
    francais du points.json a change depuis, la traduction est PERIMEE : elle
    n'est pas reprise (la page montre le francais, plutot qu'une explication
    qui ne correspond plus a la question) et la construction l'annonce.
    Une question se reconnait a sa couche et a sa phrase allemande :
    « A2 | Der Rucksack ist unter dem Tisch. ».

    --squelette ajoute aux fichiers de traduction les entrees qui manquent
    (traduction vide) : le point de depart pour traduire une question neuve.
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


LANGUES = ["en", "tr", "uk", "fa", "ar"]
# Les traductions d'un mot dans le corpus : traduction (fr), traduction_en...
# Pas encore d'arabe dans le corpus : la page retombe sur l'anglais.
CHAMPS_MOT = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr",
              "uk": "traduction_uk", "fa": "traduction_fa"}


def sens(m):
    return {l: m.get(c) for l, c in CHAMPS_MOT.items() if m.get(c)}


def cle_question(niv, q):
    return "%s | %s" % (niv, q["phrase"])


def sources(pts):
    """Tout le francais a traduire d'une scene : {groupe: {cle: texte}}."""
    champs = {k: pts[k] for k in ("alt", "consigne", "nom_vue") if pts.get(k)}
    if pts.get("autre_vue", {}).get("libelle"):
        champs["autre_vue"] = pts["autre_vue"]["libelle"]
    couches, questions = {}, {}
    for niv, c in pts.get("couches", {}).items():
        if c.get("titre"):
            couches[niv] = c["titre"]
        for q in c.get("qs", []):
            questions[cle_question(niv, q)] = q["n"]
    return {"champs": champs, "couches": couches, "questions": questions}


def traductions(pts, nom, squelette):
    """{langue: {champs, couches, questions}} -- seulement ce qui est a jour."""
    src = sources(pts)
    sortie = {}
    for lang in LANGUES:
        chemin = os.path.join(ICI, "traductions", "%s.%s.json" % (nom, lang))
        if not os.path.exists(chemin):
            if not squelette:
                continue
            fic = {"langue": lang, "scene": nom}
        else:
            fic = json.load(io.open(chemin, encoding="utf-8"))
        bon = {"champs": {}, "couches": {}, "questions": {}}
        perimes, orphelins, manquants = [], [], 0
        for groupe, textes in src.items():
            entrees = fic.setdefault(groupe, {})
            for cle in list(entrees):
                if cle not in textes:
                    orphelins.append(cle)
            for cle, fr in textes.items():
                e = entrees.get(cle)
                if not e or not e.get("trad"):
                    manquants += 1
                    if squelette and not e:
                        entrees[cle] = {"fr": fr, "trad": ""}
                elif e.get("fr") != fr:
                    perimes.append(cle)
                else:
                    bon[groupe][cle] = e["trad"]
        if squelette:
            io.open(chemin, "w", encoding="utf-8").write(
                json.dumps(fic, ensure_ascii=False, indent=1) + "\n")
        for cle in perimes:
            print("  ⚠ %s : traduction PERIMEE (le francais a change) -- %s" % (lang, cle))
        for cle in orphelins:
            print("  ⚠ %s : traduction sans question (phrase changee ?) -- %s" % (lang, cle))
        if manquants:
            print("  %s : %d texte(s) sans traduction, montres en francais" % (lang, manquants))
        sortie[lang] = bon
    return sortie


def decouper(pts, nom, g):
    """L'image NETTE d'un gros plan : le cadre decoupe dans la source a sa
    pleine resolution, au lieu de la scene web (1080 px) etiree.

    Le visage de Mark fait ~150 px dans la scene web et ~210 dans la source :
    pas de miracle, mais 40 % de pixels en plus pour le meme ecran. Le vrai
    remede reste une image du visage generee pour le gros plan."""
    fichier = "%s-%s.webp" % (nom, g["id"])
    chemin = os.path.normpath(os.path.join(ICI, pts["source"]))
    if os.path.exists(chemin):
        # PIL seulement ici : une session cloud n'a ni la source ni PIL.
        from PIL import Image
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
        sortie.append(dict({
            "id": p["id"], "mot": m["mot"], "genre": m.get("genre"),
            "pluriel": m.get("pluriel"), "niveau": m["niveau"],
            "theme": m["theme"], "personne": p.get("personne"),
            "aussi": [dict({"mot": a, "genre": idx[a].get("genre"),
                            "niveau": idx[a]["niveau"]}, **sens(idx[a]))
                      for a in p.get("aussi", [])],
            "sur": p.get("sur"), "devant": p.get("devant", 0),
            "boites": boites}, **sens(m)))
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
            sortie.append(dict({
                "id": q["id"], "mot": m["mot"], "genre": m.get("genre"),
                "pluriel": m.get("pluriel"), "niveau": m["niveau"],
                "theme": m["theme"], "personne": None, "aussi": [],
                "sur": g["personne"], "devant": 0, "detail": g["id"],
                "boites": [[cx - rx, cy - ry, 2 * rx, 2 * ry]]}, **sens(m)))
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

    scene = {"image": pts["image"], "points": sortie, "grosPlans": gros}
    for cle in ("titre", "alt", "consigne", "exclus", "couches", "corps", "autre_vue",
                "vues", "nom_vue"):
        if cle in pts:
            scene[cle] = pts[cle]
    trad = traductions(pts, nom, "--squelette" in sys.argv)
    if trad:
        scene["traductions"] = trad
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
