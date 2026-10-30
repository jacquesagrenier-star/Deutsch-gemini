# -*- coding: utf-8 -*-
"""Construit les donnees portugaises de l'app (portugais du Portugal) :
portugais/datos, a partir des listes de ce dossier.

    python portugais/outils/construire.py

LES FICHIERS PRODUITS SONT DERIVES : on corrige noms_a1.py, mots_a1.py,
phrases_a1.py, grammaire_a1.py, conjugaison.py (ou les listes du parcours
debutant), puis on relance. Rien ne se corrige dans portugais/datos/.

Sur le modele de anglais/outils/construire.py, mais le portugais a la grammaire
de l'espagnol : genre o / a, pluriel calcule (regle + exceptions), six
personnes en listes ordonnees (eu ... eles), vos cache par le moteur.

Les phrases d'exemple sont ecrites a la main dans les listes (brouillon tire
des champs pt, bresiliens, du corpus espagnol, puis recrit en portugais
d'Europe) : pas de banque de phrases a choisir, comme l'anglais en avait une.

Le mot bresilien (drapeau br=) va dans datos/variantes-br.json, pour la future
variante ; il n'est montre nulle part aujourd'hui.
"""
import json, os, random, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import noms_a1, mots_a1, phrases_a1, grammaire_a1, conjugaison, parcours_debutant

DOSSIER = "portugais/datos"
ALERTES = []


def charger(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return json.load(f)


def ecrire(chemin, donnees):
    p = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)
        f.write("\n")


def lignes(bloc):
    for l in (bloc or "").strip("\n").splitlines():
        if l.strip() and not l.strip().startswith("#"):
            yield [c.strip() for c in l.split("|")]


def drapeaux(cols):
    d = {}
    for c in cols:
        if "=" in c:
            k, v = c.split("=", 1)
            d[k.strip()] = v.strip()
        elif c:
            d[c] = True
    return d


# ---------------------------------------------------------------- le pluriel
ACCENTS = "áéíóúâêôãõ"


def a_un_accent(mot):
    return any(c in ACCENTS for c in mot)


def pluriel_mot(m):
    """Le pluriel d'un mot seul, par la regle. Les noms en -ao ont trois
    pluriels (-oes, -aes, -aos) : on prend -oes, le plus courant, et les deux
    autres sont donnes par pl= dans les listes."""
    if m.endswith("ão"):
        return m[:-2] + "ões"
    if re.search(r"[aeiouáéíóúâêô]$", m):
        return m + "s"
    if m.endswith("m"):
        return m[:-1] + "ns"
    if re.search(r"[rz]$", m):
        return m + "es"
    if m.endswith("s"):
        # -s accentue : +es (mes -> meses, pais -> paises) ; -s atone (lapis,
        # tenis) : invariable.
        if m.endswith(("ês", "és")):
            return m[:-2] + "eses"
        if m.endswith(("ás", "ís", "ós", "ús")):
            return m + "es"
        return m
    if m.endswith("al"):
        return m[:-1] + "is"
    if m.endswith("el"):
        # papel -> papeis (accent), movel -> moveis (deja un accent plus tot).
        return m[:-2] + ("eis" if a_un_accent(m) else "éis")
    if m.endswith("ol"):
        return m[:-2] + "óis"
    if m.endswith("ul"):
        return m[:-1] + "is"
    if m.endswith("il"):
        return m[:-2] + ("eis" if a_un_accent(m) else "is")
    if m.endswith("x"):
        return m
    return m + "s"


def pluriel(mot):
    """Un groupe de mots : le premier porte le pluriel (o bilhete de comboio ->
    os bilhetes de comboio) ; les composes a trait d'union sont donnes par pl=."""
    if " de " in mot or " da " in mot or " do " in mot:
        tete, _, reste = mot.partition(" ")
        return pluriel_mot(tete) + " " + reste
    if " " in mot:
        return " ".join(pluriel_mot(x) for x in mot.split(" "))
    return pluriel_mot(mot)


# ---------------------------------------------------------------- les adjectifs
def comparatif(adj):
    if adj in mots_a1.COMPARATIFS:
        c = mots_a1.COMPARATIFS[adj]
        return c, "o " + c
    return "mais " + adj, "o mais " + adj


# ---------------------------------------------------------------- construction
def themes(variantes):
    icones = {t["id"]: t.get("svg", "") for t in charger("espanol/datos/temas.json")["themes"]}
    sortie, vus = [], {}
    for tid, nom, source in noms_a1.THEMES:
        mots = []
        for cols in lignes(noms_a1.NOMS[tid]):
            tete, fr, ex, exfr, d = cols[0], cols[1], cols[2], cols[3], drapeaux(cols[4:])
            art, _, mot = tete.partition(" ") if tete.split(" ", 1)[0] in ("o", "a", "os", "as") else ("", "", tete)
            mot = mot.strip()
            if mot in vus:
                ALERTES.append("nom en double : %s (%s et %s)" % (mot, vus[mot], tid))
            vus[mot] = tid
            if not ex or not exfr:
                ALERTES.append("nom sans phrase : " + mot)
            sans = d.get("u") or art in ("os", "as")
            pl = "—" if sans else d.get("pl", pluriel(mot))
            e = {"mot": mot, "genre": art, "pluriel": pl, "traduction": fr, "exemple": ex, "exemple_fr": exfr}
            if "br" in d:
                variantes["noms"][mot] = d["br"]
            mots.append(e)
        sortie.append({"id": tid, "niveau": "A1", "svg": icones.get(source, ""), "nom_theme": nom, "mots": mots})
    return {"themes": sortie}


def verbes(variantes):
    out = []
    for cols in lignes(mots_a1.VERBES):
        inf, fr, ex, exfr, d = cols[0], cols[1], cols[2], cols[3], drapeaux(cols[4:])
        c = conjugaison.conjuguer(inf)
        e = {"mot": inf, "infinitif": inf, "traduction": fr, "exemple": ex, "exemple_fr": exfr,
             "praesens": conjugaison.praesens(c),
             "perfeito": c["perfeito"], "imperfeito": c["imperfeito"],
             "futuro": c["futuro"], "condicional": c["condicional"], "conjuntivo": c["conjuntivo"],
             "imperativo": c["imperativo"],
             "irregulier": conjugaison.irregulier(inf), "pronominal": inf.endswith("-se")}
        # Le verbe doit se lire dans sa phrase (une forme conjuguee au moins).
        formes = set(c["presente"]) | set(c["conjuntivo"] or []) | {inf}
        if inf.endswith("-se"):
            base = inf[:-3]
            formes |= {f.split("-")[0] for f in c["presente"]} | {base}
        if not any(re.search(r"(?<!\w)" + re.escape(f.split("-")[0]) + r"(?!\w)", ex, re.I) for f in formes if f != "—"):
            ALERTES.append("verbe absent de sa phrase : %s -> %s" % (inf, ex))
        if "br" in d:
            variantes["verbes"][inf] = d["br"]
        out.append({k: v for k, v in e.items() if v is not None})
    return {"A1": out}


def adjectifs(variantes):
    out = []
    for cols in lignes(mots_a1.ADJECTIFS):
        m, f, fr, ex, exfr, d = cols[0], cols[1], cols[2], cols[3], cols[4], drapeaux(cols[5:])
        pl = d.get("pl", pluriel(m))
        fpl = pl if f == m else pluriel(f)
        formes = {"feminin": f, "pluriel": pl, "feminin_pluriel": fpl}
        if m not in mots_a1.SANS_COMPARATIF:
            formes["comparatif"], formes["superlatif"] = comparatif(m)
        if not re.search(r"(?<!\w)(" + "|".join(re.escape(x) for x in {m, f, pl, fpl}) + r")(?!\w)", ex, re.I):
            ALERTES.append("adjectif absent de sa phrase : %s -> %s" % (m, ex))
        if "br" in d:
            variantes["adjectifs"][m] = d["br"]
        out.append({"mot": m, "traduction": fr, "exemple": ex, "exemple_fr": exfr, "formes": formes})
    return {"A1": out}


def simples(bloc, cat_en_colonne=True):
    out = []
    for cols in lignes(bloc):
        if cat_en_colonne:
            m, fr, cat, ex, exfr = cols[:5]
        out.append({"mot": m, "traduction": fr, "kategorie": cat, "exemple": ex, "exemple_fr": exfr})
    return out


def grammaire():
    fiches, jeux = [], {}
    for f in grammaire_a1.FICHES:
        fiche = {k: f[k] for k in ("id", "titre", "resume", "regle", "tableau", "exemples", "attention")}
        # La serie de la fiche : index.html cree la fonction « exercice » a
        # partir de « serie » (brancherSeriesAnglaises sert aussi le portugais).
        fiche["exercice"] = "exercicesFicheEn_" + f["id"].replace("-", "_")
        fiche["serie"] = f["serie"]
        fiche["statut"] = "brouillon"
        fiches.append(fiche)
        qs = []
        for cols in lignes(f["questions"]):
            question, bonne, fausses, trad, expl = cols[:5]
            options = [bonne] + [x.strip() for x in fausses.split("/")]
            random.Random(question).shuffle(options)
            qs.append({"topic": f["id"], "question": question, "question_en": question,
                       "translation": trad, "translation_en": trad,
                       "answers": [bonne], "correct": bonne, "correctEn": bonne,
                       "explanation": expl, "explanation_en": expl,
                       "options": options, "optionsEn": options})
        jeux[f["serie"]] = qs
    textes = dict(grammaire_a1.TEXTES)
    for f in grammaire_a1.FICHES:
        textes["kicker_" + f["serie"]] = f["kicker"]
    textes.update(parcours_debutant.prononciation_a1.TITRES)
    return {"textes": {"fr": textes}, "fiches": fiches}, {"jeux": jeux}


def construire():
    variantes = {"_lisez_moi": ["Le mot du Bresil quand il differe du Portugal (drapeau br= des listes de portugais/outils).",
                                "Prepare pour une future variante bresilienne ; le moteur ne le lit pas encore."],
                 "noms": {}, "verbes": {}, "adjectifs": {}}
    jeu = {}
    jeu["themes.json"] = themes(variantes)
    jeu["verbes.json"] = verbes(variantes)
    jeu["adjectifs.json"] = adjectifs(variantes)
    jeu["adverbes.json"] = {"A1": simples(mots_a1.ADVERBES)}
    jeu["expressions.json"] = {"A1": simples(phrases_a1.EXPRESSIONS)}
    f = {}
    for cle, bloc in phrases_a1.FONCTIONNELS.items():
        f[cle] = [dict(e, niveau="A1") for e in simples(bloc)]
    jeu["fonctionnels.json"] = f
    jeu["grammaire.json"], jeu["exercices.json"] = grammaire()
    # Les scenes lisent le corpus (themes.json) et Premiers pas lit les scenes :
    # les noms d'abord, puis les scenes, puis le parcours debutant.
    ecrire(DOSSIER + "/themes.json", jeu["themes.json"])
    import scenes
    scenes.main()
    parcours_debutant.construire(jeu)
    # Les niveaux A2-C1 (portugais/outils/niveaux.py, session « Portugais A2-C1 »),
    # apres l'A1, qu'ils ne touchent pas : ils ajoutent leurs cles (« A2 »...) aux
    # fichiers de `jeu` et leurs mots bresiliens a `variantes`. Absent : rien.
    import importlib.util
    if importlib.util.find_spec("niveaux"):
        import niveaux
        niveaux.construire(jeu, variantes)
    jeu["variantes-br.json"] = variantes
    # Pas encore de mots voisins (l'anglais a les siens, WordNet) : un fichier
    # vide plutot qu'une adresse qui repond 404 a chaque carte.
    jeu["synonymes.json"] = {"_note": "Mots voisins du portugais : pas encore faits. Fichier derive (construire.py).",
                             "voisins": {}}
    for nom, donnees in jeu.items():
        ecrire(DOSSIER + "/" + nom, donnees)
    n = {k: (sum(len(t["mots"]) for t in v["themes"]) if k == "themes.json"
             else sum(len(x) for x in v.values() if isinstance(x, list))) for k, v in jeu.items()
         if k in ("themes.json", "verbes.json", "adjectifs.json", "adverbes.json", "expressions.json", "fonctionnels.json")}
    print("Construit :", n)
    print("Grammaire : %d fiches, %d questions." % (len(jeu["grammaire.json"]["fiches"]),
                                                     sum(len(q) for q in jeu["exercices.json"]["jeux"].values())))
    for a in ALERTES:
        print("  ⚠", a)
    return jeu


if __name__ == "__main__":
    construire()
