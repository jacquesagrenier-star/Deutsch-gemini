# -*- coding: utf-8 -*-
"""Remplace des explications turques de pruefung.json, en refusant les regressions.

    python tests/completer_tr_pruefung.py lot.json

Le lot est un objet { "section|index": "nouveau turc", ... } ou la cle designe
une entree : « sprechen|5 », « hoeren|12 », ou « lesen|3|1 » pour la deuxieme
question du quatrieme texte. Les index sont ceux du fichier, pas ceux d'un
niveau filtre.

POURQUOI UN OUTIL. Le turc de ce fichier avait ete ecrit plus court que le
francais : les explications gardaient la premiere phrase et perdaient la
seconde -- celle qui dit ce que l'erreur coute. Ni tests/verifier.py ni
tests/ajouter_pruefung.py ne voient cela : le champ existe et n'est pas vide.

Le seul controle qui l'attrape compare les LONGUEURS et le NOMBRE DE PHRASES
avec le francais, et c'est ce que fait --auditer. Le meme controle sert ici de
garde-fou : on refuse un remplacement qui raccourcirait le turc, sans quoi une
passe de correction pourrait defaire la precedente sans rien signaler.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIBLE = os.path.join(RACINE, "pruefung.json")


def phrases(t):
    """Compte les phrases utiles -- les fragments de moins de 12 signes sont
    des abreviations (« max. », « ca. ») ou des restes de coupe, pas des
    phrases."""
    return len([x for x in re.split(r"(?<=[.!?])\s+", t.strip()) if len(x) > 12])


def entree(d, cle):
    p = cle.split("|")
    if p[0] == "lesen":
        return d["lesen"][int(p[1])]["fragen"][int(p[2])]
    return d[p[0]][int(p[1])]


def incomplet(o):
    """Le turc a-t-il perdu quelque chose en route ?"""
    fr, tr = o["erkl_fr"], o["erkl_tr"]
    return phrases(tr) < phrases(fr) or len(tr) < 0.55 * len(fr)


def toutes_les_cles(d):
    for s in ("sprechen", "schreiben", "hoeren"):
        for i in range(len(d[s])):
            yield "%s|%d" % (s, i)
    for i, o in enumerate(d["lesen"]):
        for j in range(len(o["fragen"])):
            yield "lesen|%d|%d" % (i, j)


def auditer(d):
    restants = [c for c in toutes_les_cles(d) if incomplet(entree(d, c))]
    total = sum(1 for _ in toutes_les_cles(d))
    print("  %d explications turques incompletes sur %d" % (len(restants), total))
    for c in restants[:40]:
        o = entree(d, c)
        print("     %-16s %3d signes contre %3d en francais"
              % (c, len(o["erkl_tr"]), len(o["erkl_fr"])))
    if len(restants) > 40:
        print("     ... et %d autres" % (len(restants) - 40))
    return restants


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    with io.open(CIBLE, encoding="utf-8") as f:
        d = json.load(f)

    if sys.argv[1] == "--auditer":
        return 1 if auditer(d) else 0

    with io.open(sys.argv[1], encoding="utf-8") as f:
        lot = json.load(f)

    poses = refus = 0
    for cle, neuf in lot.items():
        try:
            o = entree(d, cle)
        except (KeyError, IndexError, ValueError):
            print("  ! %s : cle introuvable dans le fichier" % cle)
            refus += 1
            continue
        ancien = o["erkl_tr"]
        if len(neuf) < len(ancien):
            print("  ! %s : le nouveau turc est PLUS COURT (%d contre %d) -- "
                  "refuse, c'est le defaut qu'on repare" % (cle, len(neuf), len(ancien)))
            refus += 1
            continue
        if phrases(neuf) < phrases(o["erkl_fr"]):
            print("  ! %s : %d phrase(s) contre %d en francais -- il en manque "
                  "encore" % (cle, phrases(neuf), phrases(o["erkl_fr"])))
            refus += 1
            continue
        o["erkl_tr"] = neuf
        poses += 1

    if poses:
        with io.open(CIBLE, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
            f.write(u"\n")

    print("  %d posees, %d refusees" % (poses, refus))
    auditer(d)
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main())
