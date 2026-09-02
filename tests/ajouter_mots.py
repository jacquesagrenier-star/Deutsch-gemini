# -*- coding: utf-8 -*-
"""Insere de nouveaux mots dans les cinq JSON du cours, depuis un fichier de lot.

    python tests/ajouter_mots.py --verifier ajouts/noyau-noms.json
    python tests/ajouter_mots.py            ajouts/noyau-noms.json

FORME D'UN LOT. Un objet par categorie, chacune une liste d'entrees completes
telles qu'elles apparaitront dans le JSON, plus une cle de placement :

    {
      "noms":      [ { "_theme": "stadt_gebaeude_a2", "mot": "Kiosk", ... } ],
      "verbes":    [ { "_niveau": "A2", "infinitif": "danken", ... } ],
      "adjectifs": [ { "_niveau": "A2", "mot": "froh", ... } ],
      "adverbes":  [ { "_niveau": "A2", "mot": "sogar", ... } ]
    }

Les cles `_theme` et `_niveau` sont retirees avant l'ecriture : elles disent OU
poser l'entree, elles ne font pas partie d'elle.

TROIS REFUS, ET AUCUN N'EST NEGOCIABLE.

1. Un mot deja present ailleurs dans le meme fichier est refuse. Un doublon ne
   se voit pas dans un fichier de 3 400 entrees, et il produit deux cartes
   identiques avec deux progressions separees.

2. Un fichier qui ne se reproduit pas a l'octet pres apres relecture n'est pas
   touche. Meme garde-fou que patch_langue.py et marquer_examen.py : un
   reformatage silencieux de 2 Mo de JSON rend le diff illisible.

3. Une entree a qui il manque un champ que ses voisines ont TOUTES est refusee.
   C'est le seul controle qui attrape l'oubli reel -- une traduction turque
   absente, une phrase d'exemple anglaise oubliee en cours de lot. Le
   vocabulaire s'ecrit a la main, par centaines ; l'oubli est la regle, pas
   l'exception, et il ne se voit qu'a l'usage, des mois plus tard, sur le
   telephone d'un testeur.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langue as L                                          # noqa: E402

PLACEMENT = ("_theme", "_niveau")


def serialiser(donnees, saut_final):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def champs_obligatoires(entrees, cle):
    """Les champs que TOUTES les entrees existantes portent.

    On ne code pas la liste en dur : elle differe d'un fichier a l'autre
    (`genre` et `pluriel` pour un nom, `praesens` pour un verbe, `kategorie`
    pour un adverbe) et elle grandira quand une langue s'ajoutera. La deduire
    du fichier, c'est un controle qui reste juste sans qu'on y pense.
    """
    if not entrees:
        return set()
    communs = set(entrees[0])
    for e in entrees[1:]:
        communs &= set(e)
    # `pruefung` est pose apres coup par marquer_examen.py, pas par l'auteur.
    return communs - {"pruefung"} | {cle}


def lire(fichier):
    chemin = os.path.join(RACINE, fichier)
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    return chemin, json.loads(brut), brut, brut.endswith("\n")


def ajouter(lot, verifier_seulement):
    total, refus = 0, 0

    for categorie, nouvelles in lot.items():
        if categorie not in L.FICHIERS or not nouvelles:
            continue
        fichier, cle = L.FICHIERS[categorie]
        chemin, donnees, brut, saut = lire(fichier)
        if serialiser(donnees, saut) != brut:
            print("  ! %s ne se reproduit pas a l'identique -- ignore" % fichier)
            refus += len(nouvelles)
            continue

        est_theme = fichier == "themes.json"
        if est_theme:
            themes = {t["id"]: t for t in donnees.get("themes", donnees)}
            existantes = [m for t in themes.values() for m in t.get("mots", [])]
        else:
            themes = None
            existantes = [m for n in L.NIVEAUX for m in donnees.get(n, [])]

        deja = {(m.get(cle) or "").strip() for m in existantes}
        requis = champs_obligatoires(existantes, cle)
        # Tout champ qu'au moins une entree du fichier porte deja. Deduit comme
        # `requis`, et pour la meme raison : la liste evoluera, la deduction
        # suivra. `pruefung` est pose apres coup et compte donc comme connu.
        connus = {k for m in existantes for k in m} | {"pruefung"}

        poses = 0
        for e in nouvelles:
            e = dict(e)
            ou = {k: e.pop(k, None) for k in PLACEMENT}
            mot = (e.get(cle) or "").strip()

            if not mot:
                print("  ! %-14s entree sans `%s`" % (fichier, cle))
                refus += 1
                continue
            if mot in deja:
                print("  ! %-14s %s : deja present" % (fichier, mot))
                refus += 1
                continue
            manque = sorted(requis - set(e))
            if manque:
                print("  ! %-14s %s : champ(s) manquant(s) -- %s"
                      % (fichier, mot, ", ".join(manque)))
                refus += 1
                continue
            # ET LE CHAMP EN TROP, symetrique du champ manquant. Un lot ecrit a
            # la main finit par contenir une cle inventee -- une faute de
            # frappe, un reste de copier-coller. Elle ne fait rien planter :
            # elle s'installe dans le JSON et n'est jamais lue par personne.
            # Attrape pour la premiere fois sur un « exemple_tr_unused » reste
            # dans un lot de verbes.
            inconnus = sorted(set(e) - connus)
            if inconnus:
                print("  ! %-14s %s : champ(s) inconnu(s) -- %s"
                      % (fichier, mot, ", ".join(inconnus)))
                refus += 1
                continue

            if est_theme:
                cible = themes.get(ou["_theme"])
                if cible is None:
                    print("  ! %-14s %s : theme inconnu `%s`"
                          % (fichier, mot, ou["_theme"]))
                    refus += 1
                    continue
                cible.setdefault("mots", []).append(e)
            else:
                niveau = ou["_niveau"]
                if niveau not in L.NIVEAUX:
                    print("  ! %-14s %s : niveau inconnu `%s`"
                          % (fichier, mot, niveau))
                    refus += 1
                    continue
                donnees.setdefault(niveau, []).append(e)

            deja.add(mot)
            poses += 1

        print("  %-18s %3d mot(s) ajoute(s)" % (fichier, poses))
        total += poses
        if not verifier_seulement and poses:
            with io.open(chemin, "w", encoding="utf-8", newline="") as f:
                f.write(serialiser(donnees, saut))

    print()
    print("  %d mot(s) %s, %d refus"
          % (total, "a ajouter" if verifier_seulement else "ajoute(s)", refus))
    return 1 if refus else 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 1
    lot = json.load(io.open(args[0], encoding="utf-8"))
    return ajouter(lot, "--verifier" in sys.argv)


if __name__ == "__main__":
    sys.exit(main())
