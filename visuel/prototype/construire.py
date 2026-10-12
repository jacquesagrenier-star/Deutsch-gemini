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
import re
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


LANGUES = ["en", "tr", "uk", "fa", "ar", "pt"]
# Les traductions d'un mot dans le corpus : traduction (fr), traduction_en...
CHAMPS_MOT = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr",
              "uk": "traduction_uk", "fa": "traduction_fa",
              "pt": "traduction_pt", "ar": "traduction_ar"}


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
                            "niveau": idx[a]["niveau"], "theme": idx[a]["theme"]},
                           **sens(idx[a]))
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
    trad = traductions(pts, nom, "--squelette" in sys.argv)
    if trad:
        scene["traductions"] = trad
    js = ("// GENERE par construire.py -- ne pas modifier a la main.\n"
          "window.SCENE = " + json.dumps(scene, ensure_ascii=False, indent=1)
          + ";\n")
    io.open(os.path.join(ICI, "scene-%s.js" % nom), "w",
            encoding="utf-8").write(js)
    print("  %d zones -> scene-%s.js" % (len(sortie), nom))
    construire_espagnol(nom, scene)

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


# ============ L'ESPAGNOL (10 oct. 2026) ============
#
# UNE SCENE, DEUX LANGUES, UNE SEULE GEOMETRIE. Jacques : « il va falloir
# faire evoluer tout ca en meme temps ». L'image, les zones, les masques et
# les gros plans restent ceux de l'allemand ; espanol/<nom>.json ne donne que
# ce qui change avec la langue :
#   - « mots » : pour CHAQUE mot allemand de la scene (zone, « aussi », partie
#     de gros plan), son mot espagnol, ecrit avec son article : « el reloj ».
#     L'article peut differer du corpus quand le mot a deux genres (« la
#     estudiante ») ; « #theme » choisit l'entree quand le corpus a deux fois
#     le meme mot (planta : l'etage de l'hotel, ou la plante).
#   - « titre », et plus tard les « couches » A2-C1, ecrites POUR l'espagnol :
#     les questions allemandes enseignent l'allemand (le datif de « Wo? »),
#     elles ne se traduisent pas.
# Une zone allemande ajoutee sans son mot espagnol arrete la construction de
# l'espagnol, et le dit : c'est ce qui garde les deux langues ensemble.
# Genre, pluriel, niveau, theme et sens viennent du corpus espagnol
# (espanol/datos/temas.json), jamais d'ici -- meme regle que l'allemand.
# La variante d'Amerique latine (variantes.json) part avec chaque mot : la
# page la prend quand l'app lui passe variante=latam.
ART_PLURIEL = {"el": "los", "la": "las"}
# Les noms feminins qui prennent « el » au singulier (le a tonique) : leur
# pluriel reprend « las ». « los aguas » serait faux.
FEMININS_EN_EL = {"agua", "hacha", "águila", "aula", "alma", "hambre", "arma", "área"}


def article_pluriel(mot, genre):
    if mot in FEMININS_EN_EL:
        return "las"
    return ART_PLURIEL.get(genre, "")


def pluriel_avec_article(mot, genre, pl):
    # las gafas, los calzoncillos : deja au pluriel, rien a ajouter.
    if not pl or genre in ("los", "las"):
        return None
    return (article_pluriel(mot, genre) + " " + pl).strip()


def corpus_espagnol():
    d = os.path.join(RACINE, "espanol", "datos")
    themes = json.load(io.open(os.path.join(d, "temas.json"), encoding="utf-8"))["themes"]
    idx = {}
    for t in themes:
        for m in t["mots"]:
            idx.setdefault(m["mot"], []).append(dict(m, theme=t["id"], niveau=t.get("niveau")))
    variantes = json.load(io.open(os.path.join(d, "variantes.json"), encoding="utf-8")).get("noms", {})
    return idx, variantes


def mot_espagnol(valeur, idx, variantes):
    """« el reloj » / « la planta#la_naturaleza » -> le mot de la page, ou None."""
    texte, _, theme = valeur.partition("#")
    morceaux = texte.split(" ", 1)
    art, mot = (morceaux if len(morceaux) == 2 and morceaux[0] in ("el", "la", "los", "las")
                else (None, texte))
    entrees = idx.get(mot) or []
    if theme:
        entrees = [e for e in entrees if e["theme"] == theme]
    if not entrees:
        return None
    m = entrees[0]
    genre = art or m.get("genre")
    pl = m.get("pluriel")
    sortie = {"mot": mot, "genre": genre, "niveau": m["niveau"], "theme": m["theme"],
              "pluriel": pluriel_avec_article(mot, genre, pl),
              "fr": m.get("traduction"), "en": m.get("traduction_en")}
    v = variantes.get(mot)
    if v and (not art or art == m.get("genre")):
        sortie["latam"] = {"mot": v["mot"], "genre": v["genre"],
                           "pluriel": pluriel_avec_article(v["mot"], v["genre"], v.get("pluriel"))}
    return sortie


def construire_espagnol(nom, scene_de):
    chemin = os.path.join(ICI, "espanol", nom + ".json")
    if not os.path.exists(chemin):
        return
    es = json.load(io.open(chemin, encoding="utf-8"))
    idx, variantes = corpus_espagnol()
    # La table COMMUNE (espanol/mots.json) : un mot n'a qu'une traduction
    # d'une scene a l'autre. Une scene peut la preciser (« mots » de son
    # fichier) quand le contexte l'exige.
    table = json.load(io.open(os.path.join(ICI, "espanol", "mots.json"), encoding="utf-8"))
    table.update(es.get("mots", {}))
    manque, inconnus = [], []

    def traduire(m):
        v = table.get(m["mot"])
        if v is None:
            manque.append(m["mot"])
            return None
        r = mot_espagnol(v, idx, variantes)
        if r is None:
            inconnus.append(v)
        return r

    points = []
    for p in scene_de["points"]:
        r = traduire(p)
        aussi, vus = [], set()
        for a in p["aussi"]:
            ra = traduire(a)
            if ra and r and ra["mot"] != r["mot"] and ra["mot"] not in vus:
                vus.add(ra["mot"])
                aussi.append({k: v for k, v in ra.items() if k != "pluriel"})
        if r:
            points.append(dict(p, aussi=aussi, **{k: r.get(k) for k in
                          ("mot", "genre", "pluriel", "niveau", "theme", "fr", "en", "latam")}))
    for cle in ("tr", "uk", "fa", "pt"):     # le corpus espagnol n'a que fr et en
        for p in points:
            p.pop(cle, None)
            for a in p["aussi"]:
                a.pop(cle, None)
    if manque or inconnus:
        if manque:
            print("  ⚠ espagnol : %s -- mot(s) allemand(s) sans mot espagnol dans espanol/%s.json : %s"
                  % (nom, nom, ", ".join(sorted(set(manque)))))
        if inconnus:
            print("  ⚠ espagnol : %s -- absent(s) du corpus espagnol : %s"
                  % (nom, ", ".join(sorted(set(inconnus)))))
        print("  scene-%s.es.js NON refaite" % nom)
        return
    scene = dict(scene_de, points=points)
    scene["titre"] = es.get("titre", scene_de.get("titre"))
    exclus = [mot_espagnol(table[m], idx, variantes) for m in scene_de.get("exclus", []) if m in table]
    scene["exclus"] = sorted({e["mot"] for e in exclus if e})
    # Les couches allemandes enseignent l'allemand : l'espagnol n'a que les
    # siennes. A1 (les noms) vient de l'allemand -- elle ne pose aucune
    # question, seul son titre compte.
    a1 = scene_de.get("couches", {}).get("A1", {"titre": "Noms et articles"})
    couches = {"A1": a1}
    trad_en = {"couches": {}, "questions": {}}
    connus = {p["id"] for p in points}
    verbes = {e["infinitif"] for n in json.load(io.open(os.path.join(RACINE, "espanol", "datos", "verbos.json"),
                                                        encoding="utf-8")).values() for e in n}
    adjectifs = {e["mot"] for n in json.load(io.open(os.path.join(RACINE, "espanol", "datos", "adjetivos.json"),
                                                     encoding="utf-8")).values() for e in n}
    erreurs = []
    for niv, c in es.get("couches", {}).items():
        sortie_c = {"titre": c["titre"], "qs": []}
        if c.get("titre_en"):
            trad_en["couches"][niv] = c["titre_en"]
        for q in c.get("qs", []):
            q = dict(q)
            n_en = q.pop("n_en", None)
            if "___" in q["q"] and not q["q"].replace("___", q["c"][0]).lower().endswith(q["phrase"].lower()):
                # La phrase dite et gardee doit etre la question remplie par la
                # bonne reponse (une amorce « Seguro: » peut la preceder) :
                # sinon la voix dit autre chose que l'ecran.
                erreurs.append("%s : la phrase ne remplit pas le trou -- %s" % (niv, q["q"]))
            if len(set(q["c"])) != len(q["c"]):
                erreurs.append("%s : choix en double -- %s" % (niv, q["q"]))
            for cle in ("f", "r"):
                if q.get(cle) and q[cle] not in connus:
                    erreurs.append("%s : %s=%r ne designe aucune zone -- %s" % (niv, cle, q[cle], q["q"]))
            mot = q.get("revise")
            if mot:
                r = mot_espagnol(mot, idx, variantes) if mot in idx else None
                if r:
                    q["revise"] = {"mot": r["mot"], "genre": r["genre"], "theme": r["theme"]}
                elif mot in verbes:
                    q["revise"] = {"mot": mot, "cat": "verbe"}
                elif mot in adjectifs:
                    q["revise"] = {"mot": mot, "cat": "adjectif"}
                else:
                    erreurs.append("%s : revise=%r absent du corpus espagnol" % (niv, mot))
            # LES MOTS QUI CHANGENT EN AMERIQUE LATINE. La zone y dit « el
            # pizarron » : une question qui dirait « la pizarra » contredirait
            # l'image. Une question qui contient un mot de variantes.json porte
            # donc sa version d'ici (« latam » : q, c, phrase, n, n_en), ecrite
            # a la main -- l'article change avec le mot (de la pizarra / del
            # pizarron), une substitution automatique se tromperait.
            texte = " ".join([q["q"], q["phrase"]] + q["c"]).lower()
            cites = [m for m in variantes if re.search(r"(?<!\w)%s(?!\w)" % re.escape(m.lower()), texte)]
            lat = q.get("latam")
            if cites and not lat:
                erreurs.append("%s : %s change en Amerique latine, la question n'a pas de « latam » -- %s"
                               % (niv, ", ".join(cites), q["q"]))
            if lat:
                lq = dict(q, **{k: v for k, v in lat.items() if k != "n_en"})
                if "___" in lq["q"] and not lq["q"].replace("___", lq["c"][0]).lower().endswith(lq["phrase"].lower()):
                    erreurs.append("%s : (latam) la phrase ne remplit pas le trou -- %s" % (niv, lq["q"]))
                lat_en = lat.get("n_en", n_en)
                if lat_en:
                    trad_en["questions"][niv + " | " + lq["phrase"]] = lat_en
                q["latam"] = {k: v for k, v in lat.items() if k != "n_en"}
            if n_en:
                trad_en["questions"][niv + " | " + q["phrase"]] = n_en
            sortie_c["qs"].append(q)
        couches[niv] = sortie_c
    if erreurs:
        for e in erreurs:
            print("  ⚠ espagnol : %s -- %s" % (nom, e))
        print("  scene-%s.es.js NON refaite" % nom)
        return
    scene["couches"] = couches
    traductions = {}
    for l, t in (scene_de.get("traductions") or {}).items():
        traductions[l] = {"champs": t.get("champs", {}),
                          "couches": {k: v for k, v in t.get("couches", {}).items() if k == "A1"},
                          "questions": {}}
    # L'espagnol a deux langues d'interface : le francais (le texte des
    # couches) et l'anglais (titre_en, n_en). Les autres ne s'y affichent pas.
    en = traductions.setdefault("en", {"champs": {}, "couches": {}, "questions": {}})
    en["couches"].update(trad_en["couches"])
    en["questions"].update(trad_en["questions"])
    scene["traductions"] = traductions
    js = ("// GENERE par construire.py (espanol/%s.json) -- ne pas modifier a la main.\n" % nom
          + "window.SCENE = " + json.dumps(scene, ensure_ascii=False, indent=1) + ";\n")
    io.open(os.path.join(ICI, "scene-%s.es.js" % nom), "w", encoding="utf-8").write(js)
    print("  %d zones -> scene-%s.es.js" % (len(points), nom))


if __name__ == "__main__":
    main()
