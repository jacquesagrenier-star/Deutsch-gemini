# -*- coding: utf-8 -*-
"""La relecture COMPLETE (decision de Jacques, 2 nov. 2026 : « vraiment y aller
passer a travers tout au complet ») : tout le contenu allemand et espagnol
decoupe en lots numerotes, chacun relu par un autre modele.

    python retours/qualite-es-de/lots_complets.py <dossier>          # ecrit les lots et l'index
    python retours/qualite-es-de/lots_complets.py <dossier> --etat   # lots faits / restants

Un lot = un fichier lot-NNN.json (au plus TAILLE textes). Son verdict, quand il
est relu, est verdict-NNN.json dans le meme dossier : c'est ce qui dit qu'un
lot est fait. Le decoupage est DETERMINISTE (meme ordre, meme taille) : on
peut le refaire apres une interruption et reprendre au premier lot sans verdict.
Chaque entree porte son adresse (fichier, chemin) pour qu'un signalement se
verifie dans le fichier, jamais sur la citation du relecteur.
"""
import json
import os
import re
import sys

from commun import LANGUES, charger

TAILLE = 700          # textes par lot (≈ 60 mots avec phrase en 9 langues)


def compter(o):
    if isinstance(o, str):
        return 1
    if isinstance(o, list):
        return sum(compter(x) for x in o)
    if isinstance(o, dict):
        return sum(compter(v) for v in o.values())
    return 0


def garder(e, cles_exclues=("svg", "pruefung", "audio", "audioDe", "theme_source", "registre",
                            "exempleHighlight", "perfektHighlight", "praeteritumHighlight",
                            "konjunktiv2Highlight", "icon", "image", "id")):
    if isinstance(e, dict):
        return {k: garder(v) for k, v in e.items() if k not in cles_exclues and not k.startswith("_")}
    if isinstance(e, list):
        return [garder(x) for x in e]
    return e


def sources():
    """(langue apprise, famille, fichier, chemin, entree) dans l'ordre de relecture."""
    out = []
    # ---------- allemand
    for t in charger("themes.json")["themes"]:
        for i, m in enumerate(t["mots"]):
            out.append(("de", "noms " + t["niveau"], "themes.json", "%s.mots[%d]" % (t["id"], i), m))
        for cle in ("verben", "adjektive"):
            for i, m in enumerate(t.get(cle, [])):
                out.append(("de", cle + " des chapitres", "themes.json", "%s.%s[%d]" % (t["id"], cle, i), m))
    for f, fam in (("verbe.json", "verbes"), ("adjectif.json", "adjectifs"), ("adverbe.json", "adverbes"),
                   ("redewendung.json", "expressions")):
        for niv, lst in charger(f).items():
            for i, e in enumerate(lst):
                out.append(("de", fam + " " + niv, f, "%s[%d]" % (niv, i), e))
    for cat, lst in charger("funktionswort.json").items():
        if isinstance(lst, list):
            for i, e in enumerate(lst):
                out.append(("de", "mots-outils", "funktionswort.json", "%s[%d]" % (cat, i), e))
    for jeu, lst in charger("exercices.json")["jeux"].items():
        for i, e in enumerate(lst):
            out.append(("de", "exercices " + jeu, "exercices.json", "jeux.%s[%d]" % (jeu, i), e))
    pr = charger("pruefung.json")
    for part in ("sprechen", "schreiben", "lesen", "hoeren"):
        for i, e in enumerate(pr.get(part, [])):
            out.append(("de", "examen " + part, "pruefung.json", "%s[%d]" % (part, i), e))
    g = charger("grammaire.json")["textes"]
    for k in sorted(g["fr"]):
        out.append(("de", "fiches de grammaire", "grammaire.json", "textes.*.%s" % k,
                    {l: g[l].get(k) for l in g}))
    for f in ("conjugaison.json", "premiers-pas.json", "a1-voyage.json", "reperes.json", "prononciation.json"):
        d = charger(f)
        for k, v in d.items():
            if k.startswith("_"):
                continue
            if isinstance(v, dict):
                for kk, vv in v.items():
                    for i, e in enumerate(vv if isinstance(vv, list) else [vv]):
                        out.append(("de", f[:-5], f, "%s.%s[%d]" % (k, kk, i), e))
            else:
                for i, e in enumerate(v if isinstance(v, list) else [v]):
                    out.append(("de", f[:-5], f, "%s[%d]" % (k, i), e))
    for f in sorted(os.listdir(os.path.join(_racine(), "visuel", "prototype", "traductions"))):
        if f.endswith(".json"):
            out.append(("de", "scenes (traductions)", "visuel/prototype/traductions/" + f, "",
                        charger("visuel/prototype/traductions/" + f)))
    # ---------- espagnol
    E = "espanol/datos/"
    for t in charger(E + "temas.json")["themes"]:
        for cle in ("mots", "adjektive"):
            for i, m in enumerate(t.get(cle, [])):
                out.append(("es", "noms " + t["niveau"], E + "temas.json", "%s.%s[%d]" % (t["id"], cle, i), m))
    for f, fam in (("verbos.json", "verbes"), ("adjetivos.json", "adjectifs"), ("adverbios.json", "adverbes"),
                   ("expresiones.json", "expressions"), ("funcionales.json", "mots-outils")):
        for niv, lst in charger(E + f).items():
            for i, e in enumerate(lst):
                out.append(("es", fam + " " + niv, E + f, "%s[%d]" % (niv, i), e))
    for jeu, lst in charger(E + "ejercicios.json")["jeux"].items():
        for i, e in enumerate(lst):
            out.append(("es", "exercices " + jeu, E + "ejercicios.json", "jeux.%s[%d]" % (jeu, i), e))
    g = charger(E + "grammaire.json")
    for i, fi in enumerate(g["fiches"]):
        out.append(("es", "fiches", E + "grammaire.json", "fiches[%d]" % i, fi))
    for k in sorted(g["textes"]["fr"]):
        out.append(("es", "textes de grammaire", E + "grammaire.json", "textes.*.%s" % k,
                    {l: g["textes"][l].get(k) for l in g["textes"]}))
    for f in ("conjugaison.json", "premiers-pas.json", "a1-voyage.json", "reperes.json", "prononciation.json",
              "variantes.json"):
        d = charger(E + f)
        for k, v in d.items():
            if k.startswith("_"):
                continue
            items = v.items() if isinstance(v, dict) else enumerate(v if isinstance(v, list) else [v])
            for kk, e in items:
                out.append(("es", f[:-5], E + f, "%s[%s]" % (k, kk), e))
    d = os.path.join(_racine(), "visuel", "prototype", "espanol")
    for f in sorted(os.listdir(d)):
        if f.endswith(".json") and f != "mots.json":
            out.append(("es", "scenes", "visuel/prototype/espanol/" + f, "", charger("visuel/prototype/espanol/" + f)))
    out.append(("es", "scenes (mots)", "visuel/prototype/espanol/mots.json", "",
                charger("visuel/prototype/espanol/mots.json")))
    return out


def _racine():
    from commun import RACINE
    return RACINE


def decouper():
    lots, cour, n = [], [], 0
    cle_cour = None
    for app, fam, f, ch, e in sources():
        e = garder(e)
        t = compter(e)
        cle = (app, fam.split(" ")[0], f)
        if cour and (n + t > TAILLE or cle != cle_cour):
            lots.append(cour)
            cour, n = [], 0
        cle_cour = cle
        cour.append({"app": app, "famille": fam, "fichier": f, "chemin": ch, "entree": e})
        n += t
    if cour:
        lots.append(cour)
    return lots


def main():
    dossier = sys.argv[1]
    os.makedirs(dossier, exist_ok=True)
    lots = decouper()
    if "--etat" not in sys.argv:
        index = []
        for k, lot in enumerate(lots, 1):
            nom = "lot-%03d.json" % k
            json.dump(lot, open(os.path.join(dossier, nom), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            index.append({"lot": k, "app": lot[0]["app"], "famille": lot[0]["famille"], "fichier": lot[0]["fichier"],
                          "entrees": len(lot), "textes": sum(compter(x["entree"]) for x in lot)})
        json.dump(index, open(os.path.join(dossier, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    faits = sorted(int(m.group(1)) for m in (re.match(r"verdict-(\d+)\.json$", f) for f in os.listdir(dossier)) if m)
    print("%d lots, %d textes ; faits : %d ; restants : %d" % (
        len(lots), sum(compter(x["entree"]) for l in lots for x in l), len(faits), len(lots) - len(faits)))
    par = {}
    for k, lot in enumerate(lots, 1):
        cle = "%s %s" % (lot[0]["app"], lot[0]["fichier"])
        a = par.setdefault(cle, [0, 0])
        a[0] += 1
        a[1] += k in faits
    for cle, (n, f) in par.items():
        print("  %-48s %3d lots, %3d faits" % (cle, n, f))


if __name__ == "__main__":
    main()
