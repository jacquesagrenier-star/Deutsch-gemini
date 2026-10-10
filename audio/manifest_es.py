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
  - La carte de verbe espagnole n'a qu'un haut-parleur : la phrase d'exemple.
    Les tableaux des temps ne se lisent pas a voix haute.
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
            prendre(ex, "noms", niv)
    for fichier, cle in (("verbos.json", "infinitif"), ("adjetivos.json", "mot"),
                         ("adverbios.json", "mot"), ("expresiones.json", "mot"),
                         ("funcionales.json", "mot")):
        for niv, liste in charger(fichier).items():
            for x in liste:
                prendre(x.get(cle), fichier, niv)
                prendre(x.get("exemple"), fichier, niv)
    # Les exercices : la phrase complete, comme l'app la dit apres la reponse.
    for nom, jeu in charger("ejercicios.json").get("jeux", {}).items():
        for e in jeu:
            q, bon = e.get("question") or "", e.get("correct") or ""
            if "___" in q and bon:
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
    return out


def entrees(variante):
    """Dedoublonnees : un texte n'est enregistre qu'une fois, au niveau le
    plus BAS ou il apparait (c'est la qu'on l'entend en premier)."""
    ordre = {"A1": 0, "A2": 1, "B1": 2, "B2": 3, "C1": 4, "EX": 5}
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
