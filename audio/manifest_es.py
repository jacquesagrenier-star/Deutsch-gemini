# -*- coding: utf-8 -*-
"""Inventorie tout l'ESPAGNOL que l'app prononce, et le chiffre -- pour les
deux voix : Espagne et Amerique latine (decide le 10 oct. 2026).

    python audio/manifest_es.py              # rapport seul, n'ecrit rien

Meme principe que manifest.py (l'allemand) : les textes que l'app peut dire a
voix haute en mode espagnol, dedoublonnes, comptes en caracteres. Les
traductions ne sont pas comptees : elles restent a la synthese du navigateur.

CE QUI DIFFERE DE L'ALLEMAND
  - Le pluriel se dit avec SON article (los / las), pas « die ».
  - La carte de verbe espagnole n'a qu'un haut-parleur : la phrase d'exemple.
    Les tableaux des temps ne se lisent pas a voix haute.
  - Les listes ecrites dans le code (prepositions, connecteurs, marqueurs du
    discours) et les exemples des sept fiches de grammaire.
  - L'AMERIQUE LATINE : le meme corpus, ou les noms de variantes.json prennent
    leur forme d'Amerique latine (mot, article, pluriel, exemple). Une seconde
    voix, donc un second jeu de fichiers, presque entierement identique en
    texte : seuls changent ces noms.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
sys.path.insert(0, os.path.join(RACINE, "fusion-espagnol"))

CREDITS_FLASH = 0.5          # un demi-credit par caractere (modele Flash)
CREATOR_MOIS = 121000         # credits d'un mois de Creator


def charger(nom):
    return json.load(io.open(os.path.join(DATOS, nom), encoding="utf-8"))


def article_pluriel(art):
    return {"el": "los ", "la": "las "}.get((art or "").strip().lower(), "")


def recolter(variante):
    out = []

    def prendre(t, source):
        if t and str(t).strip():
            out.append((str(t).strip(), source))

    variantes = charger("variantes.json").get("noms", {}) if variante == "latam" else {}
    d = charger("temas.json")
    for theme in (d["themes"] if isinstance(d, dict) else d):
        for m in theme.get("mots", []):
            mot, art, pl, ex = m.get("mot"), m.get("genre"), m.get("pluriel"), m.get("exemple")
            v = variantes.get(mot)
            if v:
                mot, art, pl, ex = v["mot"], v["genre"], v["pluriel"], v.get("exemple") or ex
            prendre(mot, "noms")
            if art:
                prendre(art + " " + mot, "noms.article")
            if pl and pl not in ("—", "-"):
                prendre(article_pluriel(art) + pl, "noms.pluriel")
            prendre(ex, "noms")
    for fichier, cle in (("verbos.json", "infinitif"), ("adjetivos.json", "mot"),
                         ("adverbios.json", "mot"), ("expresiones.json", "mot"),
                         ("funcionales.json", "mot")):
        for niv, liste in charger(fichier).items():
            for x in liste:
                prendre(x.get(cle), fichier)
                prendre(x.get("exemple"), fichier)
    # Les exercices : la phrase complete, comme l'app la dit apres la reponse.
    for nom, jeu in charger("ejercicios.json").get("jeux", {}).items():
        for e in jeu:
            q, bon = e.get("question") or "", e.get("correct") or ""
            if "___" in q and bon:
                prendre(q.replace("___", bon, 1), "exercices." + nom)
    # Les fiches de grammaire : leurs exemples ont un haut-parleur.
    for f in charger("grammaire.json").get("fiches", []):
        for e in f.get("exemples", []):
            prendre(e[0] if isinstance(e[0], str) else e[0].get("fr"), "fiches")
    # Les listes ecrites dans le code : la branche espagnole des declarations.
    from extraire import declaration  # noqa
    page = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
    for nom in ("praepTheme", "partikelnTheme", "konjunktionenTheme"):
        txt = declaration(page, nom)[2]
        es = txt[txt.index("? ") + 2: txt.index("\n    : ")]
        for ligne in re.findall(r'^\s*\["([^"]*)",\s*"[^"]*",\s*"[^"]*",\s*"([^"]*)"', es, re.M):
            prendre(ligne[0], "code." + nom)
            prendre(ligne[1], "code." + nom)
    return out


def chiffrer(variante):
    occ = recolter(variante)
    uniques = {}
    for t, s in occ:
        uniques.setdefault(t, s)
    car = sum(len(t) for t in uniques)
    return len(occ), uniques, car


def main():
    res = {}
    for v, nom in (("es", "Espagne"), ("latam", "Amerique latine")):
        n, uniques, car = chiffrer(v)
        res[v] = set(uniques)
        cr = car * CREDITS_FLASH
        print("%-16s %6d textes uniques  %8d caracteres  -> %7d credits Flash  (%.2f mois de Creator)"
              % (nom, len(uniques), car, cr, cr / CREATOR_MOIS))
    seuls = res["latam"] - res["es"]
    car_seuls = sum(len(t) for t in seuls)
    print("\nTextes propres a l'Amerique latine : %d (%d caracteres)" % (len(seuls), car_seuls))
    print("(la voix d'Amerique latine doit pourtant tout relire : c'est une autre voix)")
    par = {}
    _, uniques, _ = chiffrer("es")
    for t, s in uniques.items():
        k = s.split(".")[0]
        par[k] = par.get(k, 0) + len(t)
    print("\nRepartition (Espagne, caracteres) :")
    for k, c in sorted(par.items(), key=lambda x: -x[1]):
        print("  %-22s %8d" % (k, c))


if __name__ == "__main__":
    main()
