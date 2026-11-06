"""La relecture germanophone de Lire (Leseverstehen) du telc : section(lignes) ajoute les textes de donnees/lesen.json
a retours/A-RELIRE-TELC.md.

Usage : python visuel/prototype/telc/outils/relecture.py (qui ramasse tous les relecture_<partie>.py).

Le fichier est DERIVE : on ne le corrige jamais a la main ; on corrige donnees/lesen.json, puis on relance
relecture.py.
"""
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
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


def section(L):
    d = json.load(open(os.path.join(TELC, "donnees", "lesen.json"), encoding="utf-8"))
    L.append("## Lire (Leseverstehen), Teile 1-4")
    L.append("")
    L.append("Trois séries de 18 questions. La bonne réponse est en **gras**. Questions : les textes sont-ils corrects et "
             "naturels ? Le niveau convient-il à l'A2-B1 ? Pour chaque question, **une seule** réponse est-elle "
             "défendable d'après le texte ?")
    L.append("")
    L.append("### Les consignes")
    L.append("")
    for t, c in d["consignes"].items():
        L.append("- Teil %s : %s" % (t[1:], c["de"]))
        L.append("  → ")
    L.append("")
    for s in d["series"]:
        L.append("### Lire, série %d · Teil 1 · Petites annonces" % s["id"])
        L.append("")
        for a in s["T1"]["anzeigen"]:
            L.append("- (%s) **%s** — %s" % (a["b"], a["titel"], a["text"]))
            L.append("  → ")
        L.append("")
        for it in s["T1"]["items"]:
            L.append("- %d. %s — **%s**" % (it["nr"], it["situation"], it["bon"]))
            L.append("  → ")
        L.append("")
        L.append("### Lire, série %d · Teil 2 · Un texte court" % s["id"])
        L.append("")
        texte(L, s["T2"]["text"])
        items(L, s["T2"]["items"])
        L.append("")
        L.append("### Lire, série %d · Teil 3 · Des courriels" % s["id"])
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
        L.append("### Lire, série %d · Teil 4 · Un texte plus long" % s["id"])
        L.append("")
        texte(L, s["T4"]["text"])
        items(L, s["T4"]["items"])
        L.append("")
