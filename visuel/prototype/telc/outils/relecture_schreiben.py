"""Les textes allemands de l'epreuve Ecrire du telc (donnees/schreiben.json), pour la relecture germanophone.

Usage :
  depuis relecture.py (le fichier commun retours/A-RELIRE-TELC.md) :  from relecture_schreiben import sections
                                                                     sections(lignes)
  seul, pour voir le resultat :  python visuel/prototype/telc/outils/relecture_schreiben.py

Derive des donnees : on corrige donnees/schreiben.json, jamais la sortie.
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
        m = s["modeles"][niv]
        lignes.append("**%s modèle %s** (montré à l'élève comme exemple de niveau %s ; il doit être correct, et "
                      "typique de ce niveau)" % (nom, niv.upper(), niv.upper()))
        lignes.append("")
        _lettre(lignes, m["lignes"])


def sections(lignes):
    d = json.load(open(os.path.join(TELC, "donnees", "schreiben.json"), encoding="utf-8"))
    lignes.append("## Écrire : le courriel à lire puis à écrire (Lesen und Schreiben, 29-31)")
    lignes.append("")
    lignes.append("Pour chaque sujet : le courriel reçu, les deux questions de compréhension, les points que la "
                  "réponse doit traiter, puis deux réponses modèles (A2 et B1). Questions : le courriel est-il "
                  "naturel et au bon registre ? Les questions 29 et 30 n'ont-elles qu'une réponse possible ? Les "
                  "lettres modèles sont-elles correctes, et la lettre A2 est-elle bien plus simple que la B1, sans "
                  "être fautive ?")
    lignes.append("")
    for s in d["email"]:
        m = s["mail"]
        lignes.append("### Courriel %d · %s (%s)" % (s["id"], s["situation_fr"], s["registre"]))
        lignes.append("")
        lignes.append("Von : %s · An : %s · Betreff : %s" % (m["von"], m["an"], m["betreff"]))
        lignes.append("")
        _lettre(lignes, m["lignes"])
        for f in s["fragen"]:
            if f["typ"] == "rf":
                lignes.append("- %d. %s — **%s**" % (f["n"], f["de"], "Richtig" if f["bon"] == 0 else "Falsch"))
            else:
                choix = " · ".join(("**%s) %s**" if k == f["bon"] else "%s) %s") % ("ab"[k], o) for k, o in enumerate(f["o"]))
                lignes.append("- %d. %s %s" % (f["n"], f["de"], choix))
            lignes.append("  → ")
        lignes.append("- Points à traiter : " + " · ".join(p["de"] for p in s["punkte"]))
        lignes.append("  → ")
        lignes.append("")
        _modeles(lignes, s, "Lettre")
    lignes.append("## Écrire : le message court (Schreiben, 57)")
    lignes.append("")
    for s in d["kurz"]:
        n = s["nachricht"]
        lignes.append("### Message %d · %s (%s, « %s »)" % (s["id"], s["situation_fr"], s["registre"], s["frage"]))
        lignes.append("")
        lignes.append("%s de %s :" % (n["art"], n["von"]))
        lignes.append("")
        _lettre(lignes, n["lignes"])
        _modeles(lignes, s, "Réponse")
    lignes.append("## Écrire : les formules utiles")
    lignes.append("")
    for g in d["redemittel"]:
        lignes.append("- **%s** : %s" % (g["fr"], " · ".join("%s (%s)" % (it["de"], it["reg"]) for it in g["items"])))
        lignes.append("  → ")
    lignes.append("")


if __name__ == "__main__":
    out = []
    sections(out)
    print("\n".join(out))
