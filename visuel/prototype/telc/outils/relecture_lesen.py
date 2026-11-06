"""Refait retours/A-RELIRE-TELC-LESEN.md, la relecture germanophone de Lire (Leseverstehen) du telc, a partir des
donnees.

Usage : python visuel/prototype/telc/outils/relecture_lesen.py

Le fichier est DERIVE : on ne le corrige jamais a la main ; on corrige donnees/lesen.json, puis on relance ce
script. (Un fichier a part de A-RELIRE-TELC.md, pour que les sessions paralleles du bloc telc n'ecrivent pas le
meme script ; la session des examens pourra les reunir.)
"""
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
SORTIE = os.path.join(RACINE, "retours", "A-RELIRE-TELC-LESEN.md")
RF = ["richtig", "falsch"]


def texte(lignes, t):
    lignes.append("> **%s** — %s" % (t["kopf"], t["titel"]))
    lignes.append(">")
    for p in t["absaetze"]:
        lignes.append("> " + p)
        lignes.append(">")
    lignes.pop()
    lignes.append("")
    lignes.append("→ ")
    lignes.append("")


def items(lignes, its):
    for it in its:
        if it.get("rf"):
            choix = " · ".join(("**%s**" if k == it["bon"] else "%s") % o for k, o in enumerate(RF))
        else:
            choix = " · ".join(("**%s) %s**" if k == it["bon"] else "%s) %s") % ("abc"[k], o) for k, o in enumerate(it["optionen"]))
        lignes.append("- %d. %s — %s" % (it["nr"], it["frage"], choix))
        lignes.append("  → ")


def main():
    d = json.load(open(os.path.join(TELC, "donnees", "lesen.json"), encoding="utf-8"))
    L = [
        "# Le telc Deutsch A2·B1, Lire (Leseverstehen) : textes allemands à relire",
        "",
        "Pages : `visuel/prototype/telc/lesen.js`. Fichier DÉRIVÉ des données (ne pas corriger ici : la session corrige "
        "`visuel/prototype/telc/donnees/lesen.json`, puis relance `python visuel/prototype/telc/outils/relecture_lesen.py`).",
        "",
        "Pour le relecteur ou la relectrice : ces textes sont écrits pour Wortando, au format du telc Deutsch A2·B1 "
        "(jamais repris de ses modèles). Mark Garnier, de Montréal, vit à Berlin-Pankow. Écrire la correction sous la "
        "ligne, après « → ». Une ligne laissée vide veut dire « correct ». La bonne réponse est en **gras**. Questions : "
        "les textes sont-ils corrects et naturels ? Le niveau convient-il à l'A2-B1 ? Pour chaque question, **une seule** "
        "réponse est-elle défendable d'après le texte ?",
        "",
        "## Les consignes",
        "",
    ]
    for t, c in d["consignes"].items():
        L.append("- Teil %s : %s" % (t[1:], c["de"]))
        L.append("  → ")
    L.append("")
    for s in d["series"]:
        L.append("## Série %d" % s["id"])
        L.append("")
        L.append("### Teil 1 · Petites annonces")
        L.append("")
        for a in s["T1"]["anzeigen"]:
            L.append("- (%s) **%s** — %s" % (a["b"], a["titel"], a["text"]))
            L.append("  → ")
        L.append("")
        for it in s["T1"]["items"]:
            L.append("- %d. %s — **%s**" % (it["nr"], it["situation"], it["bon"]))
            L.append("  → ")
        L.append("")
        L.append("### Teil 2 · Un texte court")
        L.append("")
        texte(L, s["T2"]["text"])
        items(L, s["T2"]["items"])
        L.append("")
        L.append("### Teil 3 · Des courriels")
        L.append("")
        for p in s["T3"]["saetze"]:
            L.append("- (%s) %s" % (p["b"], p["de"]))
            L.append("  → ")
        L.append("")
        for m in s["T3"]["mails"]:
            L.append("**%d.** Von: %s · An: %s — réponse **%s**" % (m["nr"], m["von"], m["an"], m["bon"]))
            L.append("")
            for p in m["absaetze"]:
                L.append("> " + p)
                L.append(">")
            L.pop()
            L.append("")
            L.append("→ ")
            L.append("")
        L.append("### Teil 4 · Un texte plus long")
        L.append("")
        texte(L, s["T4"]["text"])
        items(L, s["T4"]["items"])
        L.append("")
    open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(L).rstrip() + "\n")
    print("ecrit", os.path.relpath(SORTIE, RACINE))


main()
