# -*- coding: utf-8 -*-
"""Prepare la relecture croisee du vocabulaire allemand, puis la depouille.

    python tests/relecture.py --lots 6     # decoupe
    python tests/relecture.py --rapport    # depouille les verdicts

CE QU'ELLE FAIT, ET CE QU'ELLE NE REFAIT PAS.

`tests/contraste.py` a deja confronte les 1 840 noms a WikDict sur le genre
et le pluriel, et n'a trouve que deux erreurs reelles. Inutile de faire
relire ce qu'une table a deja tranche.

Restent les trois choses qu'aucune table ne juge :

    - le NATUREL d'une phrase d'exemple ;
    - le REGISTRE, et son accord avec le niveau annonce ;
    - les FAUX AMIS propres a un francophone -- Gift, Rat, bekommen, sensibel,
      qui sont exactement les mots qu'on croit connaitre.

UNE LIMITE A NE PAS OUBLIER. Le relecteur est un autre modele, pas un autre
esprit : il partage une partie de nos donnees d'entrainement, donc une partie
de nos angles morts. Son accord n'est pas une preuve. C'est pourquoi le
depouillement ne corrige RIEN -- il produit une liste a examiner.

ET UNE PRUDENCE SUPPLEMENTAIRE ICI. Cette application-ci est EN SERVICE, avec
des testeurs. Cote espagnol, 98 signalements sur 202 ont ete appliques ; sur
du contenu que des gens utilisent deja, la proportion doit pencher davantage
vers l'arbitrage.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(RACINE, "relecture")

# Ce qu'on soumet. Le genre et le pluriel sont inclus pour le CONTEXTE, mais
# la consigne dit au relecteur de ne pas les juger : contraste.py l'a fait.
CHAMPS = ["mot", "genre", "pluriel", "traduction", "traduction_en",
          "exemple", "exemple_fr", "exemple_en"]


def charger():
    chemin = os.path.join(RACINE, "themes.json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    return d.get("themes", d)


def carte(m):
    return {k: m[k] for k in CHAMPS if m.get(k) not in (None, "", [], {})}


def faire_lots(combien):
    themes = charger()
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)

    # Repartition par nombre de CARTES, pas de themes : ils vont de 5 a 60
    # mots, et un lot deux fois plus gros serait relu deux fois moins bien.
    # (Lecon de la relecture espagnole : a 330 cartes, le relecteur cale.)
    tries = sorted(themes, key=lambda t: -len(t.get("mots", [])))
    lots = [[] for _ in range(combien)]
    poids = [0] * combien
    for t in tries:
        i = poids.index(min(poids))
        lots[i].append(t)
        poids[i] += len(t.get("mots", []))

    for i, lot in enumerate(lots, 1):
        donnees = {
            "lot": i,
            "themes": [{
                "id": t["id"],
                "nom": t.get("nom_theme"),
                "niveau": t.get("niveau"),
                "mots": [carte(m) for m in t.get("mots", [])],
            } for t in lot],
        }
        chemin = os.path.join(SORTIE, "lot_%02d.json" % i)
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("  lot_%02d.json : %2d themes, %3d cartes"
              % (i, len(lot), poids[i - 1]))
    print()
    print("%d lots, %d cartes" % (combien, sum(poids)))


def rapport():
    themes = charger()
    connus = {m.get("mot") for t in themes for m in t.get("mots", [])}

    trouvailles, lus = [], 0
    for nom in sorted(os.listdir(SORTIE)) if os.path.isdir(SORTIE) else []:
        if not nom.startswith("verdict_"):
            continue
        try:
            d = json.load(io.open(os.path.join(SORTIE, nom), encoding="utf-8"))
        except ValueError as e:
            print("  ! %s illisible : %s" % (nom, e))
            continue
        lus += 1
        for h in d:
            h["_source"] = nom
            trouvailles.append(h)

    if not lus:
        print("Aucun verdict_*.json dans %s." % SORTIE)
        return 1

    fantomes = [h for h in trouvailles if h.get("mot") not in connus]
    reels = [h for h in trouvailles if h.get("mot") in connus]
    par_type = {}
    for h in reels:
        par_type.setdefault(h.get("verdict", "?"), []).append(h)

    print()
    print("RELECTURE CROISEE — ALLEMAND")
    print("  %d fichier(s), %d signalement(s)" % (lus, len(trouvailles)))
    if fantomes:
        print("  %d portent sur un mot absent du corpus (ignores)" % len(fantomes))
    print()
    for t in sorted(par_type, key=lambda k: -len(par_type[k])):
        print("  %-28s %3d" % (t, len(par_type[t])))

    chemin = os.path.join(SORTIE, "divergences.md")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Divergences de la relecture croisee (allemand)\n\n")
        f.write("Produit par `python tests/relecture.py --rapport`. ")
        f.write("**Aucune correction appliquee.** Cette application est en ")
        f.write("service, avec des testeurs : ce qui remonte ici s'examine, ")
        f.write("ne s'applique pas en bloc.\n\n")
        f.write("Le genre et le pluriel ne figurent pas : `tests/contraste.py` ")
        f.write("les a deja tranches contre WikDict.\n")
        for t in sorted(par_type, key=lambda k: -len(par_type[k])):
            f.write("\n## %s (%d)\n\n" % (t, len(par_type[t])))
            for h in sorted(par_type[t], key=lambda x: x.get("mot", "")):
                f.write("- **%s** — champ `%s`" % (h.get("mot", "?"),
                                                   h.get("champ", "?")))
                if h.get("suggestion"):
                    f.write("\n  - suggestion : %s" % h["suggestion"])
                f.write("\n")
    print()
    print("  ecrit : relecture/divergences.md")
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    if "--rapport" in sys.argv:
        return rapport()
    combien = 6
    for i, a in enumerate(sys.argv):
        if a == "--lots" and i + 1 < len(sys.argv):
            combien = int(sys.argv[i + 1])
    faire_lots(combien)
    return 0


if __name__ == "__main__":
    sys.exit(main())
