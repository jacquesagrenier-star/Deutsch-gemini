# -*- coding: utf-8 -*-
"""L'ESPAGNOL du corpus anglais : interface de l'anglais pour les hispanophones
(2 nov. 2026, anglais/es/AVANCEMENT.md).

    python anglais/outils/espagnol.py          # pose dans anglais/datos et datos-gb
    python anglais/outils/espagnol.py --etat   # compte, n'ecrit rien

anglais/datos est DERIVE (construire.py) : un champ pose a la main y
disparaitrait au prochain construire.py. L'espagnol vit donc dans une MEMOIRE
de traduction, anglais/es/traductions/, que ce module pose :
  - construire.py l'appelle a la fin (poser(us, gb)) ;
  - en ligne de commande, il la pose dans les fichiers deja construits, sans
    rien reconstruire (l'anglais ne bouge pas).

corpus.json      {cle: {"ex": phrase anglaise temoin, "t": traduction_es, "e": exemple_es,
                        ["tE", "eE" : l'Espagne, quand elle dit autrement -> traduction_esp, exemple_esp]}}
categories.json  {categorie francaise: categorie espagnole}

La cle d'une carte : fichier|groupe|mot anglais|traduction francaise. Une phrase
anglaise changee depuis la traduction (le temoin differe) ne recoit pas son
exemple_es : anglais/es/extraire.py la ressort, tests/verifier.py la signale.
Les deux variantes ont les memes cartes dans le meme ordre : la carte
britannique recoit l'espagnol de la carte americaine de meme rang.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
MEMOIRE = os.path.join(RACINE, "anglais", "es", "traductions")
CORPUS = ["themes", "verbes", "adjectifs", "adverbes", "expressions", "fonctionnels"]


def groupes(fichier, d):
    """(groupe, liste de mots) : un theme pour les noms, un niveau ou une categorie ailleurs."""
    if fichier == "themes":
        return [(t["id"], t["mots"]) for t in d["themes"]]
    return list(d.items())


def cle_corpus(fichier, groupe, m):
    return "%s|%s|%s|%s" % (fichier, groupe, m.get("mot") or m.get("infinitif"), m.get("traduction", ""))


def memoire(nom):
    p = os.path.join(MEMOIRE, nom + ".json")
    if not os.path.exists(p):
        return {}
    return json.load(io.open(p, encoding="utf-8"))


def poser(us, gb):
    """Pose traduction_es, exemple_es, kategorie_es. us / gb : {"themes.json": ..., ...}.
    Renvoie {fichier: (cartes, traduites, phrase perimee)}."""
    mem, cats = memoire("corpus"), memoire("categories")
    stats = {}
    for f in CORPUS:
        nom = f + ".json"
        if nom not in us:
            continue
        n = t = perime = 0
        g_us = groupes(f, us[nom])
        g_gb = groupes(f, gb[nom]) if nom in gb else [(g, [None] * len(m)) for g, m in g_us]
        for (groupe, mots), (_, mots_gb) in zip(g_us, g_gb):
            for m, mg in zip(mots, mots_gb):
                n += 1
                cibles = [m] + ([mg] if mg is not None else [])
                e = mem.get(cle_corpus(f, groupe, m))
                if e and e.get("t"):
                    t += 1
                    for c in cibles:
                        c["traduction_es"] = e["t"]
                    if e.get("tE"):
                        for c in cibles:
                            c["traduction_esp"] = e["tE"]
                    if e.get("e") and e.get("ex") == m.get("exemple"):
                        for c in cibles:
                            c["exemple_es"] = e["e"]
                            if e.get("eE"):
                                c["exemple_esp"] = e["eE"]
                    elif e.get("e"):
                        perime += 1
                if m.get("kategorie") and cats.get(m["kategorie"]):
                    for c in cibles:
                        c["kategorie_es"] = cats[m["kategorie"]]
        stats[f] = (n, t, perime)
    # Les textes hors corpus (fiches, exercices, Premiers pas...) : espagnol_textes.py.
    import espagnol_textes
    for nom, (n, t) in espagnol_textes.poser(us, gb).items():
        stats[nom] = (n, t, 0)
    return stats


def charger(dossier, nom):
    return json.load(io.open(os.path.join(RACINE, dossier, nom), encoding="utf-8"))


def ecrire(dossier, nom, donnees):
    # Meme ecriture que construire.py (indent=1, LF) : seul l'espagnol change.
    with io.open(os.path.join(RACINE, dossier, nom), "w", encoding="utf-8", newline="\n") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    import espagnol_textes
    noms = [f + ".json" for f in CORPUS + espagnol_textes.OBJETS] + ["grammaire.json", "exercices.json"]
    us = {n: charger("anglais/datos", n) for n in noms if os.path.exists(os.path.join(RACINE, "anglais/datos", n))}
    gb = {n: charger("anglais/datos-gb", n) for n in noms if os.path.exists(os.path.join(RACINE, "anglais/datos-gb", n))}
    stats = poser(us, gb)
    for f, (n, t, perime) in stats.items():
        print("%-13s %5d textes, %5d en espagnol, %d phrase(s) perimee(s)" % (f, n, t, perime))
    if "--etat" in sys.argv:
        return
    for n in noms:
        if n in us:
            ecrire("anglais/datos", n, us[n])
        if n in gb:
            ecrire("anglais/datos-gb", n, gb[n])
    print("Ecrit : anglais/datos et anglais/datos-gb")


if __name__ == "__main__":
    main()
