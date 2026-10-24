# -*- coding: utf-8 -*-
"""Inventorie tout l'ESPAGNOL que l'app prononce, et le chiffre -- pour les
deux voix : Espagne et Amerique latine (decide le 10 oct. 2026).

    python audio/manifest_es.py              # rapport seul, n'ecrit rien

Meme principe que manifest.py (l'allemand) : les textes que l'app peut dire a
voix haute en mode espagnol, dedoublonnes, comptes en caracteres. Les
traductions ne sont pas comptees : elles restent a la synthese du navigateur.
L'identifiant d'un fichier est sha1(texte)[:16], comme pour l'allemand : c'est
ce que l'app recalcule a l'execution.

CE QUI DIFFERE DE L'ALLEMAND
  - Le pluriel se dit avec SON article (los / las), pas « die ».
  - La carte de verbe espagnole lit sa phrase d'exemple, et depuis le 13 oct.
    2026 la phrase de chacun de ses six autres temps, plus l'imperatif (ses
    formes a la suite). Les tableaux des temps ne se lisent pas a voix haute.
  - Les listes ecrites dans le code (prepositions, connecteurs, marqueurs du
    discours) et les exemples des sept fiches de grammaire, ranges en A1.
  - Les exercices n'ont pas de niveau : ranges a part (« EX »).
  - L'AMERIQUE LATINE : le meme corpus, ou les noms de variantes.json prennent
    leur forme d'Amerique latine (mot, article, pluriel, exemple). Une seconde
    voix, donc un second jeu de fichiers, presque entierement identique en
    texte : seuls changent ces noms.
"""
import hashlib, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
sys.path.insert(0, os.path.join(RACINE, "fusion-espagnol"))

CREDITS_FLASH = 0.5          # un demi-credit par caractere (modele Flash)
CREDITS_V2 = 1.0             # un credit par caractere (multilingual v2)
CREATOR_MOIS = 121000         # credits d'un mois de Creator


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def charger(nom):
    return json.load(io.open(os.path.join(DATOS, nom), encoding="utf-8"))


def article_pluriel(art):
    return {"el": "los ", "la": "las "}.get((art or "").strip().lower(), "")


def recolter(variante):
    """Les occurrences : (texte, source, niveau)."""
    out = []

    def prendre(t, source, niveau):
        if t and str(t).strip():
            out.append((str(t).strip(), source, niveau or "A1"))

    variantes = charger("variantes.json").get("noms", {}) if variante == "latam" else {}
    # v904 : les phrases des AUTRES mots qui contiennent un mot d'Espagne
    # (variantes.json, « phrases ») -- phraseVariante() dans index.html.
    phrases = charger("variantes.json").get("phrases", {}) if variante == "latam" else {}
    d = charger("temas.json")
    for theme in (d["themes"] if isinstance(d, dict) else d):
        niv = (theme.get("niveau") or "A1").upper()
        for m in theme.get("mots", []):
            mot, art, pl, ex = m.get("mot"), m.get("genre"), m.get("pluriel"), m.get("exemple")
            v = variantes.get(mot)
            if v:
                mot, art, pl, ex = v["mot"], v["genre"], v["pluriel"], v.get("exemple") or ex
            prendre(mot, "noms", niv)
            if art:
                prendre(art + " " + mot, "noms.article", niv)
            if pl and pl not in ("—", "-"):
                prendre(article_pluriel(art) + pl, "noms.pluriel", niv)
            prendre(phrases.get(ex, ex), "noms", niv)
    for fichier, cle in (("verbos.json", "infinitif"), ("adjetivos.json", "mot"),
                         ("adverbios.json", "mot"), ("expresiones.json", "mot"),
                         ("funcionales.json", "mot")):
        for niv, liste in charger(fichier).items():
            for x in liste:
                prendre(x.get(cle), fichier, niv)
                ex = x.get("exemple")
                prendre(phrases.get(ex, ex) if fichier in ("verbos.json", "adjetivos.json") else ex, fichier, niv)
                if fichier != "verbos.json":
                    continue
                # LA CARTE DE VERBE DEPUIS LE 13 OCT. 2026 : une phrase par
                # temps, chacune avec son haut-parleur (blocTempsEspagnol), et
                # l'imperatif lu comme l'app l'affiche (texteImperativoEspagnol :
                # tu, usted, vosotros, ustedes separes par des virgules --
                # vosotros absent en Amerique latine).
                for temps in ("preterito", "imperfecto", "perfecto", "futuro", "condicional", "subjuntivo"):
                    prendre(x.get("exemple_" + temps), "verbos.temps", niv)
                imp = x.get("imperativo")
                if imp:
                    cles = ("tu", "usted", "ustedes") if variante == "latam" else ("tu", "usted", "vosotros", "ustedes")
                    prendre(", ".join(imp[k] for k in cles if imp.get(k)), "verbos.imperativo", niv)
    # Les exercices : la phrase complete, comme l'app la dit apres la reponse.
    for nom, jeu in charger("ejercicios.json").get("jeux", {}).items():
        for e in jeu:
            q, bon = e.get("question") or "", e.get("correct") or ""
            if "___" in q and bon:
                # LA MAJUSCULE DE L'APP (24 oct. 2026). phraseAllemandeDeLExercice()
                # met une capitale quand le blanc ouvre une phrase : elle demande
                # « Abre la ventana, por favor. », on avait fait « abre la... » --
                # 48 phrases par voix a la voix du telephone, l'imperatif surtout.
                if q.startswith("___") and re.search(r"[.?!]", q):
                    bon = bon[:1].upper() + bon[1:]
                prendre(q.replace("___", bon, 1), "exercices." + nom, "EX")
    # Les fiches de grammaire : leurs exemples ont un haut-parleur.
    for f in charger("grammaire.json").get("fiches", []):
        for e in f.get("exemples", []):
            prendre(e[0] if isinstance(e[0], str) else e[0].get("fr"), "fiches", "A1")
    # Les listes ecrites dans le code : la branche espagnole des declarations.
    from extraire import declaration  # noqa
    page = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
    for nom in ("praepTheme", "partikelnTheme", "konjunktionenTheme"):
        txt = declaration(page, nom)[2]
        es = txt[txt.index("? ") + 2: txt.index("\n    : ")]
        for ligne in re.findall(r'^\s*\["([^"]*)",\s*"[^"]*",\s*"[^"]*",\s*"([^"]*)"', es, re.M):
            prendre(ligne[0], "code." + nom, "A1")
            prendre(ligne[1], "code." + nom, "A1")
    # LES SCENES (10 oct. 2026). Ce que visuel/prototype/index.html dit :
    # « el reloj » en touchant une zone, « Anna. la participante » pour une
    # personne, et la phrase entiere apres chaque question. Lu dans les
    # scene-*.es.js que construire.py a faits -- en Amerique latine, avec le
    # mot (latam) et la question (latam) d'ici, comme la page les montre.
    import glob
    for chemin in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "scene-*.es.js"))):
        txt = io.open(chemin, encoding="utf-8").read()
        sc = json.loads(txt[txt.index("{"):txt.rindex("}") + 1])
        ici = (lambda m: dict(m, **m["latam"]) if variante == "latam" and m.get("latam") else m)
        for p in sc["points"]:
            for m in [p] + p.get("aussi", []):
                m = ici(m)
                if m.get("genre"):
                    prendre(m["genre"] + " " + m["mot"], "scenes", "SC")
            if p.get("personne") and p.get("genre"):
                m = ici(p)
                prendre(p["personne"] + ". " + m["genre"] + " " + m["mot"], "scenes", "SC")
        for c in sc.get("couches", {}).values():
            for q in c.get("qs", []):
                q = dict(q, **q["latam"]) if variante == "latam" and q.get("latam") else q
                prendre(q["phrase"], "scenes", "SC")
    # PREMIERS PAS (v837, 16 oct. 2026) : espanol/datos/premiers-pas.json, avec
    # la variante d'Amerique latine comme joursPremiersPas() la montre : une
    # entree en tableau peut finir par {"la": [...]} (position par position,
    # null = inchange) ; une phrase porte {"la": {"p": ...}}. Ce que l'app dit :
    # la forme des tableaux, l'expression et l'exemple des cartes, les phrases.
    def varier(e):
        if isinstance(e, list) and e and isinstance(e[-1], dict) and isinstance(e[-1].get("la"), list):
            base = list(e[:-1])
            if variante == "latam":
                for i, v in enumerate(e[-1]["la"]):
                    if v is not None and i < len(base):
                        base[i] = v
            return base
        return e
    for etape in charger("premiers-pas.json")["etapes"]:
        for l in etape["tableau"]["l"]:
            prendre(varier(l)[0], "premiers_pas", "A1")
        for c in etape["cartes"]:
            c = varier(c)
            prendre(c[0], "premiers_pas", "A1")
            if len(c) > 2 and isinstance(c[2], str):
                prendre(c[2], "premiers_pas", "A1")
        for p in etape["phrases"]:
            p = dict(p, **p["la"]) if variante == "latam" and isinstance(p.get("la"), dict) else p
            prendre(p["p"], "premiers_pas", "A1")
    # A1 VOYAGE (v862-v864, 18 oct. 2026) : espanol/datos/a1-voyage.json, la
    # meme regle que manifest.py (a1_voyage_textes), variante comprise.
    import manifest as manifest_de
    for t in manifest_de.a1_voyage_textes(charger("a1-voyage.json"), latam=(variante == "latam"), espagnol=True):
        prendre(t, "a1_voyage", "A1")
    # LES MOTS DES TUILES (v919, 22 oct. 2026). Depuis la v904, « Construire la
    # phrase » dit chaque mot touche ; mais un mot de phrase n'a pas de fichier a
    # lui, et « es », « soy », « Madrid » partaient a la voix du telephone
    # (Jacques, trois fois le 22 oct.). Le chemin des debutants d'abord : les
    # phrases de Premiers pas et d'A1 voyage, mot par mot, comme le decoupe
    # motsPhrase(), sans la ponctuation collee, EN MINUSCULES -- l'app demande la
    # minuscule en espagnol (« Es » en tete de phrase et « es » sont un seul son).
    for t, source, _ in list(out):
        if source in ("premiers_pas", "a1_voyage") and " " in t:
            for m in t.split():
                m = re.sub(r'[.,;:!?»")]+$', "", re.sub(r'^[¿¡«"(]+', "", m)).lower()
                if re.search(r"\w", m):      # « – » ou « · » seuls : rien a dire
                    prendre(m, "tuiles", "A1")
    # FEUILLES DE CONJUGAISON (v867, 18 oct. 2026) : espanol/datos/conjugaison.json,
    # la meme regle que manifest.py (conjugaison_textes) -- la forme sans ses
    # crochets. Les memes textes dans les deux variantes.
    for niveau, t in manifest_de.conjugaison_textes(charger("conjugaison.json")):
        prendre(t, "conjugaison", niveau)
    # LES REPERES (v879, 19 oct. 2026) : espanol/datos/reperes.json, la meme
    # regle que manifest.py (reperes_textes). Les memes textes dans les deux variantes.
    for t in manifest_de.reperes_textes(charger("reperes.json")):
        prendre(t, "reperes", "A1")
    return out


def entrees(variante):
    """Dedoublonnees : un texte n'est enregistre qu'une fois, au niveau le
    plus BAS ou il apparait (c'est la qu'on l'entend en premier)."""
    ordre = {"A1": 0, "A2": 1, "B1": 2, "B2": 3, "C1": 4, "EX": 5, "SC": 6}
    vus = {}
    for t, s, n in recolter(variante):
        if t not in vus or ordre.get(n, 9) < ordre.get(vus[t]["niveau"], 9):
            vus[t] = {"id": identifiant(t), "texte": t, "source": s, "niveau": n}
    return list(vus.values())


def main():
    for v, nom in (("es", "Espagne"), ("latam", "Amerique latine")):
        es = entrees(v)
        car = sum(len(e["texte"]) for e in es)
        print("%-16s %6d textes  %8d caracteres  -> v2 %7d credits | Flash %7d"
              % (nom, len(es), car, car * CREDITS_V2, car * CREDITS_FLASH))
        par = {}
        for e in es:
            par.setdefault(e["niveau"], [0, 0])
            par[e["niveau"]][0] += 1
            par[e["niveau"]][1] += len(e["texte"])
        for n in ("A1", "A2", "B1", "B2", "C1", "EX"):
            if n in par:
                print("    %-3s %6d textes  %8d caracteres" % (n, par[n][0], par[n][1]))


if __name__ == "__main__":
    main()
