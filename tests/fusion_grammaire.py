# -*- coding: utf-8 -*-
"""Verse un lot de traductions dans grammaire.json, langue par langue.

    python tests/fusion_grammaire.py --langue fa --lot lot1.json
    python tests/fusion_grammaire.py --langue fa --manque      # ce qui reste

Le fichier de lot est un objet JSON {cle: texte}.

⚠️ GARDE-FOU D'ALLER-RETOUR. grammaire.json est ecrit en JSON COMPACT --
`separators=(",", ":")`, sans indentation, sans saut de ligne final. Le
reserialiser avec les reglages par defaut de json.dump gonflerait le fichier de
177 ko a 185 ko et rendrait le diff illisible : la vraie modification s'y
perdrait. Avant d'ecrire, on verifie donc que relire puis reserialiser le
fichier ACTUEL le reproduit au signe pres. Si ce n'est pas le cas, on s'arrete
plutot que de reformater 235 cles par accident.

⚠️ ET ON RELIT CE QU'ON A ECRIT, comme fusion_langue.py. Un fichier de donnees
se recharge a l'execution depuis GitHub : une chaine abimee ne se verrait
qu'en production, chez un usager, dans une langue que personne autour ne lit.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIER = os.path.join(RACINE, "grammaire.json")


def serialiser(d):
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))


def charger():
    brut = io.open(FICHIER, encoding="utf-8").read()
    d = json.loads(brut)
    if serialiser(d) != brut:
        sys.exit("grammaire.json n'est plus en JSON compact : ecrire maintenant "
                 "reformaterait tout le fichier. Verifier avant de continuer.")
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--lot")
    ap.add_argument("--manque", action="store_true")
    ap.add_argument("--nombre", type=int, default=60)
    a = ap.parse_args()

    d = charger()
    textes = d["textes"]
    fr = textes["fr"]
    cible = textes.setdefault(a.langue, {})

    if a.manque:
        reste = [k for k in fr if k not in cible]
        print("%s : %d cles sur %d ; il en manque %d\n"
              % (a.langue, len(cible), len(fr), len(reste)))
        for k in reste[:a.nombre]:
            print("%-30s | %s" % (k, fr[k]))
        return

    if not a.lot:
        sys.exit("--lot ou --manque")
    lot = json.load(io.open(a.lot, encoding="utf-8"))
    inconnues = [k for k in lot if k not in fr]
    if inconnues:
        sys.exit("cles absentes du francais : " + ", ".join(inconnues[:5]))

    cible.update(lot)
    # Les langues gardent l'ordre du francais : un diff de ce fichier doit se
    # lire, et une cle ajoutee en fin de bloc casserait l'alignement.
    textes[a.langue] = {k: cible[k] for k in fr if k in cible}
    io.open(FICHIER, "w", encoding="utf-8", newline="").write(serialiser(d))

    # --- la relecture ---------------------------------------------------
    relu = json.loads(io.open(FICHIER, encoding="utf-8").read())["textes"][a.langue]
    ecarts = [k for k, v in lot.items() if relu.get(k) != v]
    print("%d cles versees en %s ; le bloc en compte %d sur %d"
          % (len(lot), a.langue, len(relu), len(fr)))
    if ecarts:
        print("⚠️ %d ECARTS entre ce qui etait demande et ce qui est ecrit :" % len(ecarts))
        for k in ecarts[:8]:
            print("   %s\n     demande : %r\n     relu    : %r" % (k, lot[k], relu.get(k)))
        sys.exit(1)
    print("relecture : les %d chaines sont identiques a ce qui etait demande." % len(lot))


if __name__ == "__main__":
    main()
