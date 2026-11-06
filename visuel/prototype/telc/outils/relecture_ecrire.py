"""Les textes allemands de l'ecrit du telc (le courriel LS et la reponse courte S), pour la relecture germanophone.

Ramasse par relecture.py (retours/A-RELIRE-TELC.md), qui appelle section(lignes). Pour voir le resultat seul :
  python visuel/prototype/telc/outils/relecture_ecrire.py

Derive des donnees : on corrige donnees/lesen-schreiben.json et donnees/schreiben.json, jamais la sortie.
"""
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)


def _lettre(lignes, l):
    for p in l:
        lignes.append("> " + p)
        lignes.append(">")
    lignes.pop()
    lignes.append("")
    lignes.append("→ ")
    lignes.append("")


def _modeles(lignes, s, nom):
    for niv in ("a2", "b1"):
        lignes.append("**%s modèle %s** (montrée à l'élève comme exemple du niveau %s : correcte, et typique de ce "
                      "niveau)" % (nom, niv.upper(), niv.upper()))
        lignes.append("")
        _lettre(lignes, s["modeles"][niv]["lignes"])


def section(lignes):
    ls = json.load(open(os.path.join(TELC, "donnees", "lesen-schreiben.json"), encoding="utf-8"))
    s = json.load(open(os.path.join(TELC, "donnees", "schreiben.json"), encoding="utf-8"))
    lignes.append("## Lire et écrire : le courriel à lire puis à écrire (Lesen und Schreiben, 29-31)")
    lignes.append("")
    lignes.append("Pour chaque sujet : le courriel reçu, les deux questions de compréhension, les points que la "
                  "réponse doit traiter, puis deux lettres modèles (A2 et B1). Questions : le courriel est-il "
                  "naturel et au bon registre ? Les questions 29 et 30 n'ont-elles qu'une réponse possible ? Les "
                  "lettres modèles sont-elles correctes, et la lettre A2 est-elle bien plus simple que la B1, sans "
                  "être fautive ?")
    lignes.append("")
    for x in ls["series"]:
        m = x["mail"]
        lignes.append("### Courriel %d · %s (%s)" % (x["id"], x["situation_fr"], x["registre"]))
        lignes.append("")
        lignes.append("Von : %s · An : %s · Betreff : %s" % (m["von"], m["an"], m["betreff"]))
        lignes.append("")
        _lettre(lignes, m["lignes"])
        for f in x["fragen"]:
            if f["typ"] == "rf":
                lignes.append("- %d. %s — **%s**" % (f["n"], f["de"], "Richtig" if f["bon"] == 0 else "Falsch"))
            else:
                choix = " · ".join(("**%s) %s**" if k == f["bon"] else "%s) %s") % ("ab"[k], o) for k, o in enumerate(f["o"]))
                lignes.append("- %d. %s %s" % (f["n"], f["de"], choix))
            lignes.append("  → ")
        lignes.append("- Points à traiter : " + " · ".join(p["de"] for p in x["punkte"]))
        lignes.append("  → ")
        lignes.append("")
        _modeles(lignes, x, "Lettre")
    lignes.append("## Écrire : la réponse courte (Schreiben, 57)")
    lignes.append("")
    for x in s["series"]:
        n = x["nachricht"]
        lignes.append("### Message %d · %s (%s, « %s »)" % (x["id"], x["situation_fr"], x["registre"], x["frage"]))
        lignes.append("")
        lignes.append("%s de %s :" % (n["art"], n["von"]))
        lignes.append("")
        _lettre(lignes, n["lignes"])
        _modeles(lignes, x, "Réponse")
    lignes.append("## Écrire : les formules utiles")
    lignes.append("")
    for g in s["redemittel"]:
        lignes.append("- **%s** : %s" % (g["titre_fr"], " · ".join("%s (%s)" % (it["de"], it["reg"]) for it in g["items"])))
        lignes.append("  → ")
    lignes.append("")


if __name__ == "__main__":
    out = []
    section(out)
    print("\n".join(out))
