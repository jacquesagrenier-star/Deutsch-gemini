"""La relecture germanophone de l'oral du telc (visuel/prototype/telc/oral.html), pour retours/A-RELIRE-TELC.md.

Ramasse par outils/relecture.py (section(lignes)). Les textes viennent de la page elle-meme, par
`node tests/telc_oral.js --json` : on ne les recopie pas ici, on corrige oral.html puis on relance relecture.py.
Les repliques reprises de l'oral du DTZ (sans prefixe « t_ ») sont deja relues avec lui : elles ne sont pas listees.
"""
import json
import os
import subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))


def _donnees():
    sortie = subprocess.run(["node", os.path.join(RACINE, "tests", "telc_oral.js"), "--json"],
                            capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return json.loads(sortie)


def _replique(lignes, d, ident):
    qui, de, fr = d["L"][ident][0], d["L"][ident][1], d["L"][ident][2]
    lignes.append("- %s : %s" % ("Anna (examinatrice)" if qui == "anna" else "Mark (l'autre candidat)", de))
    lignes.append("  _(%s)_" % fr)
    lignes.append("  → ")


def _modeles(lignes, liste, d):
    for m in liste:
        if m.get("id"):
            continue   # une replique du DTZ, deja relue
        lignes.append("- Modèle %s : %s" % (m["niv"], m["de"][0]))
        lignes.append("  _(%s)_" % m["de"][1])
        lignes.append("  → ")


def section(lignes):
    d = _donnees()
    lignes.append("## L'oral (Mündliche Prüfung) : répliques et réponses modèles")
    lignes.append("")
    lignes.append("Anna mène l'entretien, Mark joue l'autre candidat, l'élève parle pour lui-même. Chaque réponse "
                  "modèle existe au niveau A2 et au niveau B1, **jamais au-dessus**. Questions : l'allemand est-il "
                  "correct et naturel à l'oral ? Le modèle A2 est-il vraiment A2, le modèle B1 vraiment B1 (pas plus "
                  "difficile) ? Les tours de Mark sont-ils ceux d'un candidat B1 ?")
    lignes.append("")
    lignes.append("### Partie 1 · se présenter et répondre")
    lignes.append("")
    lignes.append("Mots-clés de la feuille : " + " · ".join(d["STICHWORTE"]))
    lignes.append("")
    _modeles(lignes, d["MODELES_1A"], d)
    for question, liste in d["MODELES_1B"].items():
        lignes.append("- Question d'Anna : %s" % d["L"][question][1])
        _modeles(lignes, liste, d)
    lignes.append("")
    lignes.append("### Partie 2 · planifier ensemble")
    lignes.append("")
    for cle, s in d["PLAN"].items():
        lignes.append("#### %s" % s["titre"]["fr"])
        lignes.append("")
        lignes.append("Feuille : %s — %s" % (s["blatt"], " · ".join(s["punkte"])))
        lignes.append("")
        _replique(lignes, d, s["intro"])
        for k, t in enumerate(s["tours"]):
            _replique(lignes, d, t["m"])
            _modeles(lignes, [{"niv": "A2", "de": t["a2"]}, {"niv": "B1", "de": t["b1"]}], d)
        lignes.append("")
    lignes.append("### Partie 3 · donner et justifier son avis")
    lignes.append("")
    for cle, s in d["AVIS"].items():
        lignes.append("#### %s" % s["titre"]["fr"])
        lignes.append("")
        lignes.append("Feuille : %s" % s["blatt"])
        lignes.append("")
        _replique(lignes, d, s["frage"])
        _modeles(lignes, s["avis"], d)
        for cote, gegen in (("A", "gegenA"), ("B", "gegenB")):
            _replique(lignes, d, s[gegen])
            _modeles(lignes, s["reaction"][cote], d)
        lignes.append("")
    lignes.append("### Les autres répliques")
    lignes.append("")
    _replique(lignes, d, "t_a_los")
    _replique(lignes, d, "t_m_schluss")
    lignes.append("")
