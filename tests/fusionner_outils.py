# -*- coding: utf-8 -*-
"""Fusionne des lots de mots-outils dans funktionswort.json.

    python tests/fusionner_outils.py --verifier lot.json
    python tests/fusionner_outils.py            lot.json

POURQUOI CE FICHIER A SON PROPRE OUTIL. ajouter_mots.py connait les cinq JSON
de vocabulaire, qui sont ranges par NIVEAU (A1, A2...). funktionswort.json est
range par CLASSE DE MOT -- konjunktionen, praepositionen, partikeln, zahlen --
et le niveau y est un champ de l'entree. Les deux formes ne se plient pas l'une
a l'autre sans tordre l'une des deux.

MEMES TROIS REFUS QU'AILLEURS, et pour les memes raisons : doublon dans la
meme classe, fichier qui ne se reproduit pas a l'octet pres, champ manquant ou
champ en trop. Ce dernier a deja attrape trois accidents dans la journee, dont
un champ `registre` sur un adjectif que le chargeur aurait jete en silence.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIER = os.path.join(RACINE, "funktionswort.json")


def serialiser(donnees, saut_final):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 1
    verifier = "--verifier" in sys.argv
    lot = json.load(io.open(args[0], encoding="utf-8"))

    brut = io.open(FICHIER, encoding="utf-8", newline="").read()
    donnees = json.loads(brut)
    saut = brut.endswith("\n")
    if serialiser(donnees, saut) != brut:
        print("  ! funktionswort.json ne se reproduit pas a l'identique -- rien ecrit")
        return 1

    # Les champs qu'une entree doit avoir : ceux que TOUTES les entrees
    # existantes portent, toutes classes confondues. Deduits, pas codes en dur.
    toutes = [m for v in donnees.values() for m in v]
    requis = set(toutes[0])
    for m in toutes[1:]:
        requis &= set(m)
    connus = {k for m in toutes for k in m} | {"pruefung"}

    total, refus = 0, 0
    for classe, nouvelles in lot.items():
        if classe.startswith("_"):
            continue
        cible = donnees.setdefault(classe, [])
        deja = {(m.get("mot") or "").strip() for m in cible}
        poses = 0
        for e in nouvelles:
            mot = (e.get("mot") or "").strip()
            if not mot:
                print("  ! %-16s entree sans `mot`" % classe)
                refus += 1
                continue
            if mot in deja:
                print("  ! %-16s %s : deja present" % (classe, mot))
                refus += 1
                continue
            manque = sorted(requis - set(e))
            if manque:
                print("  ! %-16s %s : champ(s) manquant(s) -- %s"
                      % (classe, mot, ", ".join(manque)))
                refus += 1
                continue
            inconnus = sorted(set(e) - connus)
            if inconnus:
                print("  ! %-16s %s : champ(s) inconnu(s) -- %s"
                      % (classe, mot, ", ".join(inconnus)))
                refus += 1
                continue
            cible.append(e)
            deja.add(mot)
            poses += 1
        print("  %-16s %3d mot(s) ajoute(s)" % (classe, poses))
        total += poses

    print()
    print("  %d mot(s) %s, %d refus"
          % (total, "a ajouter" if verifier else "ajoute(s)", refus))
    if not verifier and total:
        with io.open(FICHIER, "w", encoding="utf-8", newline="") as f:
            f.write(serialiser(donnees, saut))
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main())
