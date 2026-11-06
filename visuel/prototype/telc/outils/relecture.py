"""Refait retours/A-RELIRE-TELC.md, le fichier de relecture germanophone du bloc telc, a partir des donnees.

Usage : python visuel/prototype/telc/outils/relecture.py

Le fichier est DERIVE : on ne le corrige jamais a la main ; on corrige donnees/*.json, puis on relance ce script.
"""
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
SORTIE = os.path.join(RACINE, "retours", "A-RELIRE-TELC.md")


def sprachbausteine(lignes):
    d = json.load(open(os.path.join(TELC, "donnees", "sprachbausteine.json"), encoding="utf-8"))
    lignes.append("## Les Sprachbausteine (lettres à trous)")
    lignes.append("")
    lignes.append("Chaque lettre est donnée deux fois : d'abord complète, avec la bonne réponse de chaque trou en "
                  "**gras**, puis trou par trou, avec les trois choix proposés à l'élève. Questions : la lettre "
                  "est-elle correcte et naturelle ? Le registre est-il juste (Sie ou du, formules d'appel et de "
                  "fin) ? Pour chaque trou, **une seule** réponse est-elle possible, les deux autres étant "
                  "vraiment fausses dans ce contexte ? Le niveau convient-il à l'A2-B1 ?")
    lignes.append("")
    for s in d["series"]:
        bons = {l["n"]: l["o"][l["bon"]] for l in s["luecken"]}
        lignes.append("### Lettre %d · %s" % (s["id"], s["situation_fr"]))
        lignes.append("")
        lignes.append("Von : %s · An : %s · Betreff : %s" % (s["von"], s["an"], s["betreff"]))
        lignes.append("")
        for p in s["absaetze"]:
            lignes.append("> " + re.sub(r"\{(\d+)\}", lambda m: "**%s**" % bons[int(m.group(1))], p))
            lignes.append(">")
        lignes.pop()
        lignes.append("")
        lignes.append("→ ")
        lignes.append("")
        for l in s["luecken"]:
            choix = " · ".join(("**%s) %s**" if k == l["bon"] else "%s) %s") % ("abc"[k], o) for k, o in enumerate(l["o"]))
            lignes.append("- Trou %d : %s" % (l["n"], choix))
            lignes.append("  _(explication montrée à l'élève : %s)_" % l["erkl_fr"])
            lignes.append("  → ")
        lignes.append("")


def main():
    lignes = [
        "# Le telc Deutsch A2·B1 : textes allemands à relire",
        "",
        "Pages : `visuel/prototype/telc/`. Fichier DÉRIVÉ des données (ne pas corriger ici : la session corrige "
        "`visuel/prototype/telc/donnees/*.json`, puis relance `python visuel/prototype/telc/outils/relecture.py`).",
        "",
        "Pour le relecteur ou la relectrice : ces textes sont écrits pour Wortando, au format du telc Deutsch "
        "A2·B1 (jamais repris de ses modèles). Mark Garnier, de Montréal, vit à Berlin ; Anna est une amie "
        "allemande. Écrire la correction sous la ligne, après « → ». Une ligne laissée vide veut dire « correct ».",
        "",
    ]
    sprachbausteine(lignes)
    # LES AUTRES PARTIES : chaque session ajoute outils/relecture_<partie>.py, qui expose section(lignes) et y
    # ajoute ses textes allemands au meme format (texte, puis « → »). Ce fichier-ci n'a pas a changer.
    import glob
    import importlib.util
    for chemin in sorted(glob.glob(os.path.join(ICI, "relecture_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(chemin)[:-3], chemin)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        (getattr(module, "section", None) or getattr(module, "sections"))(lignes)
    open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(lignes).rstrip() + "\n")
    print("ecrit", os.path.relpath(SORTIE, RACINE))


main()
