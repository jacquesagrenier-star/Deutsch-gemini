# -*- coding: utf-8 -*-
"""Contrôle des feuilles de conjugaison A2-B1 (conjugaison.json et
espanol/datos/conjugaison.json). Aucune dépendance.

    python tests/conjugaison.py            # contrôle les fichiers présents
    python tests/conjugaison.py --detail   # et la liste des feuilles

Les feuilles de conjugaison (18 oct. 2026, essai « feuilles_conj ») prolongent
au-delà de l'A1 les tableaux de Premiers pas et de l'A1 voyage : une feuille
enseigne un TEMPS ou une CONSTRUCTION, avec des verbes modèles fixes. Même
forme que le tableau (pp_tableau) : t, l: [[forme, sens]], a. Maquette validée :
.claude/maquette-conjugaison-niveaux.html.

Ce qu'il vérifie :
  - « niveaux » : A2 et B1, le nombre de feuilles attendu pour chacun ;
  - chaque feuille : un id unique, un titre « t » et une astuce « a » dans toutes
    les langues d'interface de la langue apprise, non vides ;
  - exactement 6 lignes, chacune [forme, sens complet] ;
  - la forme a au moins une partie [entre crochets] (ce qui change, surligné),
    des crochets bien appariés et non imbriqués, rien de vide entre eux ;
  - « serie » : null ou une série qui existe dans les exercices de la langue ;
  - « temps » : null ou un temps dont verbe.json (verbos.json) a la phrase ;
  - aucune forme en double dans tout le fichier (une voix par texte).
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIERS = {
    "de": {"chemin": "conjugaison.json",
           "langues": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"],
           "exercices": "exercices.json",
           "verbes": "verbe.json",
           "temps": {"perfekt": "perfekt", "praeteritum": "praeteritum", "konjunktiv2": "konjunktiv2"},
           "niveaux": {"A2": 12, "B1": 12}},
    "es": {"chemin": os.path.join("espanol", "datos", "conjugaison.json"),
           "langues": ["fr", "en", "pt", "ar"],
           "exercices": os.path.join("espanol", "datos", "ejercicios.json"),
           "verbes": os.path.join("espanol", "datos", "verbos.json"),
           "temps": {t: "exemple_" + t for t in ("preterito", "imperfecto", "perfecto", "futuro", "condicional", "subjuntivo")},
           "niveaux": {"A2": 10, "B1": 10}},
}
NB_LIGNES = 6


def lire(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return json.load(f)


def sens_complet(o, langues):
    return isinstance(o, dict) and all(isinstance(o.get(l), str) and o.get(l).strip() for l in langues)


def texte_dit(forme):
    """Ce que la voix lit : la forme sans ses crochets (miroir de index.html)."""
    return forme.replace("[", "").replace("]", "")


def crochets_ok(forme):
    prof = 0
    for c in forme:
        if c == "[":
            prof += 1
            if prof > 1:
                return False
        elif c == "]":
            prof -= 1
            if prof < 0:
                return False
    return prof == 0 and "[" in forme and not re.search(r"\[\s*\]", forme)


def verifier(code, info, detail):
    err = []
    nom = info["chemin"]
    if not os.path.exists(os.path.join(RACINE, nom)):
        return None
    data = lire(nom)
    langues = info["langues"]
    jeux = lire(info["exercices"])
    jeux = jeux.get("jeux", jeux)
    verbes = lire(info["verbes"])
    niveaux = data.get("niveaux")
    if not isinstance(niveaux, dict):
        return ["%s : il faut un objet « niveaux »" % nom]
    ids, formes = set(), {}
    for niv, attendu in info["niveaux"].items():
        liste = niveaux.get(niv)
        if not isinstance(liste, list):
            err.append("%s : pas de liste pour %s" % (nom, niv))
            continue
        if len(liste) != attendu:
            err.append("%s : %s a %d feuilles au lieu de %d" % (nom, niv, len(liste), attendu))
        for i, f in enumerate(liste):
            ou = "%s %s[%d] %s" % (nom, niv, i, f.get("id", "?"))
            if not f.get("id") or f["id"] in ids:
                err.append("%s : id absent ou en double" % ou)
            ids.add(f.get("id"))
            if not sens_complet(f.get("t"), langues):
                err.append("%s : titre « t » incomplet" % ou)
            if not sens_complet(f.get("a"), langues):
                err.append("%s : astuce « a » incomplète" % ou)
            serie = f.get("serie")
            if serie is not None and not (isinstance(jeux.get(serie), list) and jeux[serie]):
                err.append("%s : série inconnue %r" % (ou, serie))
            temps = f.get("temps")
            if temps is not None:
                champ = info["temps"].get(temps)
                if not champ:
                    err.append("%s : temps inconnu %r" % (ou, temps))
                else:
                    n = sum(1 for v in verbes.get(niv, []) if (v.get(champ) or "").strip())
                    if not n:
                        err.append("%s : aucun verbe %s n'a le champ %r" % (ou, niv, champ))
            lignes = f.get("l", [])
            if len(lignes) != NB_LIGNES:
                err.append("%s : %d lignes au lieu de %d" % (ou, len(lignes), NB_LIGNES))
            for j, l in enumerate(lignes):
                ol = "%s ligne %d" % (ou, j + 1)
                if not (isinstance(l, list) and len(l) == 2 and isinstance(l[0], str) and l[0].strip()):
                    err.append("%s : il faut [forme, sens]" % ol)
                    continue
                if not crochets_ok(l[0]):
                    err.append("%s : crochets absents ou mal formés : %r" % (ol, l[0]))
                if not sens_complet(l[1], langues):
                    err.append("%s : sens incomplet" % ol)
                dit = texte_dit(l[0])
                if dit in formes:
                    err.append("%s : forme déjà dans %s : %r" % (ol, formes[dit], dit))
                formes[dit] = f.get("id")
            if detail:
                print("  %s %-22s %-24s %s" % (niv, f.get("id"), serie or "-", f["t"].get("fr")))
    return err


def main():
    detail = "--detail" in sys.argv
    total = 0
    vus = 0
    for code, info in FICHIERS.items():
        e = verifier(code, info, detail)
        if e is None:
            print("%s : absent, pas contrôlé" % info["chemin"])
            continue
        vus += 1
        for x in e:
            print("✗ " + x)
        total += len(e)
        if not e:
            print("✓ %s : aucun problème" % info["chemin"])
    if not vus:
        print("Aucun fichier de feuilles.")
        sys.exit(1)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
