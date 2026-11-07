# -*- coding: utf-8 -*-
"""Controle des etapes A2-C1 et des lignes « Tu sais... ». Aucune dependance.

    python tests/etapes.py            # controle les quatre fichiers derives
    python tests/etapes.py --detail   # et les comptes par groupe

Ce qu'il verifie, pour l'allemand (etapes.json, je-sais.json) et l'espagnol
(espanol/datos/etapes.json, je-sais.json) :
  - les fichiers derives sont a jour avec etapes/structure.py ;
  - chaque texte porte toutes les langues d'interface, non vide ; aucune autre ;
  - chaque identifiant existe : themes (au niveau de l'etape, sauf exceptions
    nommees), feuilles de conjugaison (au niveau de l'etape), scenes
    (scene-<nom>.js, et .es.js pour l'espagnol), themes illustres
    (THEMES_ILLUSTRES d'index.html), series d'exercices, tuiles (data-orbid),
    fiches espagnoles, parties d'examen non vides ;
  - chaque feuille de conjugaison A2-C1 sert une fois, et toutes servent ;
  - chaque theme A2-C1 sert au plus une fois (ceux qui ne servent pas sont listes) ;
  - les lignes « Tu sais... » de Premiers pas, de l'A1 et des reperes couvrent
    exactement les etapes, escales et reperes des fichiers existants ;
  - le francais d'une ligne « Tu sais... » : une minuscule au debut, pas de point
    a la fin, 60 signes au plus ; ids uniques.
"""
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "etapes"))
import structure as S  # noqa: E402

FICHIERS = {
    "de": {"etapes": "etapes.json", "sais": "je-sais.json", "themes": "themes.json", "conj": "conjugaison.json",
           "exos": "exercices.json", "pp": "premiers-pas.json", "a1": "a1-voyage.json", "reperes": "reperes.json"},
    "es": {"etapes": "espanol/datos/etapes.json", "sais": "espanol/datos/je-sais.json", "themes": "espanol/datos/temas.json",
           "conj": "espanol/datos/conjugaison.json", "exos": "espanol/datos/ejercicios.json",
           "pp": "espanol/datos/premiers-pas.json", "a1": "espanol/datos/a1-voyage.json", "reperes": "espanol/datos/reperes.json",
           "fiches": "espanol/datos/grammaire.json"},
}
# Themes pris hors de leur niveau, chacun avec sa raison.
HORS_NIVEAU = {
    ("es", "vhs_kapitel1_b1"): "Descripción física du cours de Jacques : marqué B1, ses mots sont ceux du thème illustré Décrire (A2)",
}
SAIS_MAX = 60


def lire(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return json.load(f)


def main():
    detail = "--detail" in sys.argv
    err = []
    # Les fichiers derives sont-ils a jour ? On reconstruit a cote et on compare.
    avant = {}
    for appr, F in FICHIERS.items():
        for k in ("etapes", "sais"):
            p = os.path.join(RACINE, F[k])
            avant[p] = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    r = subprocess.run([sys.executable, os.path.join(RACINE, "tests", "etapes_construire.py")], capture_output=True, text=True, encoding="utf-8")
    for p, txt in avant.items():
        apres = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if txt != apres:
            err.append("%s n'était pas à jour (refait par etapes_construire.py : relancer le contrôle)" % os.path.relpath(p, RACINE))
    if r.returncode != 0:
        err.append("etapes_construire.py : " + r.stdout.strip().splitlines()[0] if r.stdout.strip() else "etapes_construire.py a échoué")

    index = open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
    m = re.search(r"const THEMES_ILLUSTRES = \{(.*?)\};", index, re.S)
    illustres = set(re.findall(r"(\w+): \{page:", m.group(1))) if m else set()
    orbids = set(re.findall(r'data-orbid="([a-zA-Z_]+)"', index))

    for appr, F in FICHIERS.items():
        L = S.LANGUES[appr]
        try:
            et, sa = lire(F["etapes"]), lire(F["sais"])
        except FileNotFoundError as e:
            err.append(str(e)); continue
        th = {t["id"]: t for t in lire(F["themes"])["themes"]}
        conj = {niv: {f["id"] for f in fs} for niv, fs in lire(F["conj"])["niveaux"].items()}
        exos = set(lire(F["exos"])["jeux"].keys())
        fiches = {f["id"] for f in lire(F["fiches"])["fiches"]} if "fiches" in F else set()
        pr = lire("pruefung.json") if appr == "de" else None

        def langues(obj, ou):
            if not isinstance(obj, dict):
                err.append("%s : %s : objet par langue attendu" % (appr, ou)); return
            for lg in L:
                if not (obj.get(lg) or "").strip():
                    err.append("%s : %s : « %s » absent ou vide" % (appr, ou, lg))
            for lg in obj:
                if lg not in L:
                    err.append("%s : %s : langue inattendue « %s »" % (appr, ou, lg))

        def ligne_sais(obj, ou):
            langues(obj, ou)
            fr = (obj or {}).get("fr", "")
            if fr and (fr[0] != fr[0].lower() or fr.endswith((".", "!", "?")) or len(fr) > SAIS_MAX):
                err.append("%s : %s : « %s » (minuscule au début, pas de point final, %d signes au plus)" % (appr, ou, fr, SAIS_MAX))

        ids, feuilles_vues, themes_vus = set(), [], []
        for niv, groupes in et["niveaux"].items():
            for g in groupes:
                langues(g["nom"], g["id"])
                if g["id"] in ids: err.append("%s : id en double %s" % (appr, g["id"]))
                ids.add(g["id"])
                if not g["etapes"]: err.append("%s : %s : aucune étape" % (appr, g["id"]))
                noms = 0
                for e in g["etapes"]:
                    ou = "%s > %s" % (g["id"], e["id"])
                    if e["id"] in ids: err.append("%s : id en double %s" % (appr, e["id"]))
                    ids.add(e["id"])
                    langues(e["t"], ou + " (titre)")
                    ligne_sais(e["sais"], ou + " (sais)")
                    if not (e.get("themes") or e.get("pruefung")):
                        err.append("%s : %s : ni thème ni partie d'examen" % (appr, ou))
                    if g.get("examen") and not e.get("pruefung"):
                        err.append("%s : %s : étape d'un groupe examen sans partie d'examen" % (appr, ou))
                    for t in e.get("themes", []):
                        themes_vus.append(t)
                        if t not in th:
                            err.append("%s : %s : thème inconnu %s" % (appr, ou, t)); continue
                        noms += len(th[t]["mots"])
                        if th[t].get("niveau") != niv and (appr, t) not in HORS_NIVEAU:
                            err.append("%s : %s : thème %s de niveau %s" % (appr, ou, t, th[t].get("niveau")))
                    for f in e.get("feuilles", []):
                        feuilles_vues.append(f)
                        if f not in conj.get(niv, set()):
                            err.append("%s : %s : feuille %s absente du %s" % (appr, ou, f, niv))
                    for s in e.get("scenes", []):
                        for suffixe in ([".js"] + ([".es.js"] if appr == "es" else [])):
                            if not os.path.exists(os.path.join(RACINE, "visuel", "prototype", "scene-%s%s" % (s, suffixe))):
                                err.append("%s : %s : scène absente scene-%s%s" % (appr, ou, s, suffixe))
                    for i in e.get("illustres", []):
                        if i not in illustres: err.append("%s : %s : thème illustré inconnu %s" % (appr, ou, i))
                    for x in e.get("series", []):
                        if x not in exos: err.append("%s : %s : série inconnue %s" % (appr, ou, x))
                    for x in e.get("tuiles", []):
                        if x not in orbids: err.append("%s : %s : tuile inconnue %s" % (appr, ou, x))
                    for x in e.get("fiches", []):
                        if x not in fiches: err.append("%s : %s : fiche inconnue %s" % (appr, ou, x))
                    p = e.get("pruefung")
                    if p:
                        if pr is None:
                            err.append("%s : %s : pas d'examen dans cette langue" % (appr, ou))
                        else:
                            items = [x for x in pr.get(p["partie"], []) if x.get("niveau") == p["niveau"]]
                            if p.get("teil"):
                                items = [x for x in items if (x.get("teil") or x.get("typ")) in p["teil"]]
                                for t in p["teil"]:
                                    if not any((x.get("teil") or x.get("typ")) == t for x in items):
                                        err.append("%s : %s : partie « %s » introuvable" % (appr, ou, t))
                            if not items:
                                err.append("%s : %s : examen vide (%s, %s)" % (appr, ou, p["partie"], p["niveau"]))
                            elif detail:
                                print("    %s : %d sujets d'examen" % (e["id"], len(items)))
                if detail:
                    print("%s %s %-14s %2d étapes, %4d noms  %s" % (appr, niv, g["id"], len(g["etapes"]), noms, g["nom"]["fr"]))

        dbl = sorted({f for f in feuilles_vues if feuilles_vues.count(f) > 1})
        if dbl: err.append("%s : feuilles en double %s" % (appr, dbl))
        toutes = {f for n, fs in conj.items() if n in ("A2", "B1", "B2", "C1") for f in fs}
        reste = sorted(toutes - set(feuilles_vues))
        if reste: err.append("%s : feuilles qui ne servent pas %s" % (appr, reste))
        dbl = sorted({t for t in themes_vus if themes_vus.count(t) > 1})
        if dbl: err.append("%s : thèmes en double %s" % (appr, dbl))
        libres = sorted(t for t, v in th.items() if v.get("niveau") in ("A2", "B1", "B2", "C1") and v["mots"] and t not in themes_vus)
        if libres: print("[info] %s : thèmes A2-C1 qu'aucune étape ne prend : %s" % (appr, libres))

        # Les lignes de ce qui existe deja.
        langues(sa["amorces"]["maintenant"], "amorce maintenant")
        langues(sa["amorces"]["semaine"], "amorce semaine")
        pp = lire(F["pp"])["etapes"]
        if len(sa["premiers_pas"]) != len(pp):
            err.append("%s : %d lignes Premiers pas pour %d étapes" % (appr, len(sa["premiers_pas"]), len(pp)))
        for i, o in enumerate(sa["premiers_pas"]):
            ligne_sais(o, "Premiers pas %d" % (i + 1))
        a1 = lire(F["a1"])
        a1ids = [e["id"] for k in ("escales", "installe", "suite") for e in a1.get(k, [])]
        if sorted(a1ids) != sorted(sa["a1"].keys()):
            err.append("%s : A1 : ids différents (manque %s, en trop %s)" % (appr, sorted(set(a1ids) - set(sa["a1"])), sorted(set(sa["a1"]) - set(a1ids))))
        for k, o in sa["a1"].items():
            ligne_sais(o, "A1 " + k)
        rids = [x["id"] for x in lire(F["reperes"])["reperes"]]
        if sorted(rids) != sorted(sa["reperes"].keys()):
            err.append("%s : repères : ids différents (manque %s, en trop %s)" % (appr, sorted(set(rids) - set(sa["reperes"])), sorted(set(sa["reperes"]) - set(rids))))
        for k, o in sa["reperes"].items():
            ligne_sais(o, "repère " + k)

    if err:
        print("%d problème(s) :" % len(err))
        for e in err:
            print("  - " + e)
        return 1
    print("etapes : aucun problème (allemand et espagnol)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
