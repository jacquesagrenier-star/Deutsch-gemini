# -*- coding: utf-8 -*-
"""Controle des themes illustres des Soins, SANS navigateur (quelques secondes).

    python tests/themes_soins.py              # tous les themes soins-theme-*
    python tests/themes_soins.py schmerz      # un seul

Il relit visuel/prototype/soins-theme-<cle>/donnees.json (fait par pflege/outils/themes_soins/<cle>.py) :
  - au moins 100 questions (la reserve des themes, visuel/THEMES-ILLUSTRES.md) ;
  - chaque mot vise par au moins deux sortes (sinon une partie enchaine deux fois la meme sorte) ;
  - aucun chiffre dans l'allemand DIT (la phrase, la reponse, l'ecoute, « dit ») : regle 4 du contrat Pflege ;
  - chaque phrase, chaque mot et chaque texte de l'interface traduits dans les dix langues d'interface ;
  - chaque choix bien forme (la bonne reponse parmi les choix, pas de doublon) ;
  - les images : celles qui existent, et celles qui manquent encore (etape 2), comptees a part (avertissement).
"""
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = ["fr", "en", "es", "pt", "tr", "uk", "pl", "ru", "ar", "fa"]
CHIFFRE = re.compile(r"\d")


def controler(cle):
    dossier = os.path.join(RACINE, "visuel", "prototype", "soins-theme-" + cle)
    d = json.load(io.open(os.path.join(dossier, "donnees.json"), encoding="utf-8"))
    fautes, avert = [], []
    qs = d["questions"]
    if len(qs) < 100:
        fautes.append("%d questions (moins de 100)" % len(qs))
    sortes = {}
    for q in qs:
        sortes.setdefault(q["mot"], set()).add(q["sorte"])
        for k in ("phrase", "ecoute", "dit"):
            if q.get(k) and CHIFFRE.search(q[k]):
                fautes.append("chiffre dans l'allemand dit (%s) : %s" % (k, q[k]))
        if q.get("choix") is not None:
            if q["bonne"] not in q["choix"] or len(set(q["choix"])) != len(q["choix"]):
                fautes.append("choix mal formes : %s" % q["id"])
            if CHIFFRE.search(q["bonne"]):
                fautes.append("chiffre dans la reponse dite : %s" % q["bonne"])
        if q.get("images") is not None and q["bonne"] not in q["images"]:
            fautes.append("image juste absente des images : %s" % q["id"])
        p = d["phrases"].get(q["phrase"])
        if not p:
            fautes.append("phrase sans traduction : %s" % q["phrase"])
    for i, m in enumerate(d["mots"]):
        if len(sortes.get(i, ())) < 2:
            fautes.append("mot a moins de deux sortes : %s" % m["affiche"])
        manque = [l for l in LANGUES if not m["glose"].get(l)]
        if manque:
            fautes.append("mot sans traduction (%s) : %s" % (",".join(manque), m["affiche"]))
    for ph, t in d["phrases"].items():
        manque = [l for l in LANGUES if not t.get(l)]
        if manque:
            fautes.append("phrase sans traduction (%s) : %s" % (",".join(manque), ph[:60]))
    for k, t in d["textes"].items():
        manque = [l for l in LANGUES if not t.get(l)]
        if manque:
            fautes.append("texte sans traduction (%s) : %s" % (",".join(manque), k))
    for nom in d["images"]:
        if not os.path.exists(os.path.join(dossier, nom + ".webp")):
            avert.append(nom)
    print("soins-theme-%s : %d questions, %d mots, %d phrases ; %d image(s) manquante(s)%s"
          % (cle, len(qs), len(d["mots"]), len(d["phrases"]), len(avert), (" : " + ", ".join(avert)) if avert else ""))
    for f in fautes[:30]:
        print("  ✗ " + f)
    if len(fautes) > 30:
        print("  ... et %d autres" % (len(fautes) - 30))
    return not fautes


def main():
    cles = [a for a in sys.argv[1:] if not a.startswith("--")] or sorted(
        os.path.basename(x)[len("soins-theme-"):] for x in glob.glob(os.path.join(RACINE, "visuel", "prototype", "soins-theme-*")) if os.path.isdir(x))
    ok = all([controler(c) for c in cles])
    print("OK" if ok else "ECHEC")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
