# -*- coding: utf-8 -*-
"""Construit les etapes de l'A2 au C1 et les lignes « Tu sais... ».

    python tests/etapes_construire.py                # ecrit les quatre fichiers
    python tests/etapes_construire.py --a-traduire   # ecrit etapes/traductions/a-traduire-<langue>.json

Source : etapes/structure.py (structure et francais) et
etapes/traductions/<langue>.json ({texte francais: traduction}). Une traduction
se retrouve par son TEXTE francais : la meme ligne en allemand et en espagnol
(« te presenter ») ne se traduit qu'une fois.

Ecrit (fichiers DERIVES, jamais a la main) :
  etapes.json, je-sais.json                              (allemand)
  espanol/datos/etapes.json, espanol/datos/je-sais.json  (espagnol)
Controle : python tests/etapes.py
"""
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "etapes"))
import structure as S  # noqa: E402

TRAD = os.path.join(RACINE, "etapes", "traductions")
SORTIES = {
    "de": ("etapes.json", "je-sais.json"),
    "es": (os.path.join("espanol", "datos", "etapes.json"), os.path.join("espanol", "datos", "je-sais.json")),
}
# Les deux amorces de l'app, a traduire avec le reste : la ligne doit s'y lire.
AMORCES = ["Tu sais maintenant…", "Cette semaine, tu as appris à…"]


def textes_francais(appr):
    """[(texte, contexte)] : tout ce qui se traduit pour cette langue apprise."""
    nom_langue = "l'allemand" if appr == "de" else "l'espagnol"
    out = [(a, "amorce de la liste du bilan") for a in AMORCES]
    for niv, groupes in S.GROUPES[appr].items():
        for g in groupes:
            out.append((g["nom"], "nom d'un groupe d'étapes (%s, %s), à la première personne" % (nom_langue, niv)))
            for e in g["etapes"]:
                out.append((e["t"], "titre d'une étape (%s, %s)" % (nom_langue, niv)))
                out.append((e["sais"], "ligne « Tu sais… » (%s, %s)" % (nom_langue, niv)))
    for s in S.PREMIERS_PAS[appr]:
        out.append((s, "ligne « Tu sais… » (Premiers pas)"))
    for s in S.A1[appr].values():
        out.append((s, "ligne « Tu sais… » (A1)"))
    for s in S.REPERES[appr].values():
        out.append((s, "ligne « Tu sais… » (repère : nombres, jours, genre…)"))
    return out


def a_traduire():
    par_langue = {}
    for appr, langues in S.LANGUES.items():
        for lg in langues:
            if lg == "fr":
                continue
            d = par_langue.setdefault(lg, {})
            for texte, ctx in textes_francais(appr):
                d.setdefault(texte, ctx)
    os.makedirs(TRAD, exist_ok=True)
    for lg, d in sorted(par_langue.items()):
        chemin = os.path.join(TRAD, "a-traduire-%s.json" % lg)
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump([{"fr": t, "contexte": c} for t, c in d.items()], f, ensure_ascii=False, indent=1)
        print("%s : %d textes -> %s" % (lg, len(d), os.path.relpath(chemin, RACINE)))


def lire_trad():
    t = {}
    for nom in os.listdir(TRAD):
        if nom.endswith(".json") and not nom.startswith("a-traduire"):
            with open(os.path.join(TRAD, nom), encoding="utf-8") as f:
                t[nom[:-5]] = json.load(f)
    return t


def construire():
    trad = lire_trad()
    manque = []

    def sens(texte, langues):
        o = {}
        for lg in langues:
            if lg == "fr":
                o[lg] = texte
                continue
            v = trad.get(lg, {}).get(texte)
            if not v:
                manque.append((lg, texte))
                continue
            o[lg] = v
        return o

    for appr, (f_etapes, f_sais) in SORTIES.items():
        L = S.LANGUES[appr]
        niveaux = {}
        for niv, groupes in S.GROUPES[appr].items():
            gs = []
            for g in groupes:
                og = {"id": g["id"], "nom": sens(g["nom"], L)}
                if g.get("examen"):
                    og["examen"] = g["examen"]
                og["etapes"] = []
                for e in g["etapes"]:
                    oe = {"id": e["id"], "icone": e["icone"], "t": sens(e["t"], L), "sais": sens(e["sais"], L)}
                    for cle in ("themes", "feuilles", "scenes", "illustres", "series", "tuiles", "fiches", "pruefung"):
                        if e.get(cle):
                            oe[cle] = e[cle]
                    og["etapes"].append(oe)
                gs.append(og)
            niveaux[niv] = gs
        etapes = {
            "_lisez_moi": [
                "Les étapes de l'A2 au C1 (6 nov. 2026), sur le modèle de l'A1 voyage : par niveau, des groupes d'étapes nommés, puis un groupe « examen » là où l'app a le contenu de l'épreuve.",
                "Fichier DÉRIVÉ : le refaire avec python tests/etapes_construire.py (source : etapes/structure.py et etapes/traductions/), jamais à la main. Contrôle : python tests/etapes.py.",
                "Une étape ne crée aucun contenu : elle NOMME ce qui existe (themes, feuilles de conjugaison, scenes, illustres = THEMES_ILLUSTRES, series d'exercices, tuiles ou fiches de grammaire, pruefung = une partie de pruefung.json).",
                "sais : la ligne « Tu sais… » de l'étape, à l'infinitif, qui se lit après « Tu sais maintenant… » et « Cette semaine, tu as appris à… » (amorces dans je-sais.json).",
            ],
            "niveaux": niveaux,
        }
        sais = {
            "_lisez_moi": [
                "Les lignes « Tu sais… » de ce qui existait avant les étapes A2-C1 : Premiers pas (par rang d'étape), l'A1 (par id d'escale ou d'étape de a1-voyage.json), les repères (par id de reperes.json).",
                "Elles servent au bilan « je sais faire » (le lundi, et à la fin d'un groupe d'étapes). Fichier DÉRIVÉ : python tests/etapes_construire.py.",
            ],
            "amorces": {"maintenant": sens(AMORCES[0], L), "semaine": sens(AMORCES[1], L)},
            "premiers_pas": [sens(s, L) for s in S.PREMIERS_PAS[appr]],
            "a1": {k: sens(v, L) for k, v in S.A1[appr].items()},
            "reperes": {k: sens(v, L) for k, v in S.REPERES[appr].items()},
        }
        for chemin, contenu in ((f_etapes, etapes), (f_sais, sais)):
            with open(os.path.join(RACINE, chemin), "w", encoding="utf-8", newline="\n") as f:
                json.dump(contenu, f, ensure_ascii=False, indent=1)
                f.write("\n")
    if manque:
        vus = sorted(set(manque))
        print("%d traductions manquantes, par exemple :" % len(vus))
        for lg, t in vus[:12]:
            print("  %s : %s" % (lg, t))
        return 1
    print("ok : etapes.json, je-sais.json et leurs pendants espagnols")
    return 0


if __name__ == "__main__":
    if "--a-traduire" in sys.argv:
        a_traduire()
    else:
        sys.exit(construire())
