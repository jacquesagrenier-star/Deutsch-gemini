# -*- coding: utf-8 -*-
"""Prepare les fichiers de traduction d'une scene des Soins, SANS passer par le corpus.

    python pflege/outils/squelette_traductions.py soins-zimmer soins-aufnahme
    python pflege/outils/squelette_traductions.py --toutes
    python pflege/outils/squelette_traductions.py --manquantes        # compte ce qui reste a traduire

POURQUOI
    `construire.py --squelette` ferait la meme chose, mais il s'arrete d'abord
    sur un mot absent du corpus : les scenes des Soins attendent les mots de
    la session vocabulaire, et leurs textes (alt, consigne, couches,
    explications, sens) peuvent se traduire avant. Le format est EXACTEMENT
    celui de construire.py (visuel/prototype/traductions/<nom>.<langue>.json,
    {"fr": source, "trad": traduction}) : c'est lui qui les lira ensuite, et
    une traduction dont le francais a change y est declaree perimee.
    Une traduction existante n'est jamais ecrasee ; une entree dont le
    francais a change garde sa traduction et recoit le nouveau francais
    dans « fr_nouveau », pour qu'on la revoie.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
sys.path.insert(0, PROTO)
import construire as C                                       # noqa: E402

LIRE = ("Traduction du contenu francais d'une scene des Soins (alt, consigne, nom de la vue, titres des "
        "couches, explication « n » et sens de chaque question). L'allemand ne se traduit jamais : les "
        "balises <b> et les mots allemands restent tels quels. Fait par pflege/outils/squelette_traductions.py.")


def squelette(nom):
    pts = json.load(io.open(os.path.join(PROTO, nom + ".points.json"), encoding="utf-8"))
    src = C.sources(pts)
    reste = 0
    for l in C.LANGUES:
        chemin = os.path.join(PROTO, "traductions", "%s.%s.json" % (nom, l))
        fic = (json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin)
               else {"_lisez_moi": LIRE, "langue": l, "scene": nom})
        for groupe, textes in src.items():
            entrees = fic.setdefault(groupe, {})
            for cle, fr in textes.items():
                e = entrees.get(cle)
                if not e:
                    entrees[cle] = {"fr": fr, "trad": ""}
                elif e.get("fr") != fr and e.get("trad"):
                    e["fr_nouveau"] = fr
                elif e.get("fr") != fr:
                    e["fr"] = fr
            for cle in list(entrees):
                if cle not in textes:
                    print("  %s %s : entree sans source, retiree -- %s" % (nom, l, cle))
                    del entrees[cle]
            reste += sum(1 for e in entrees.values() if not e.get("trad") or e.get("fr_nouveau"))
        if "--manquantes" not in sys.argv:
            io.open(chemin, "w", encoding="utf-8").write(json.dumps(fic, ensure_ascii=False, indent=1) + "\n")
    print("  %-28s %d texte(s) a traduire ou a revoir (8 langues)" % (nom, reste))
    return reste


def main():
    noms = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--toutes" in sys.argv or "--manquantes" in sys.argv and not noms:
        noms = sorted(f[:-len(".points.json")] for f in os.listdir(PROTO)
                      if f.startswith("soins-") and f.endswith(".points.json"))
    for n in noms:
        squelette(n)


if __name__ == "__main__":
    main()
