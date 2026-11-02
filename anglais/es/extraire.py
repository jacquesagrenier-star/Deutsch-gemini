# -*- coding: utf-8 -*-
"""Les textes de l'anglais appris a traduire en ESPAGNOL (2 nov. 2026).

    python anglais/es/extraire.py [nom ...]

Demande de Jacques le 2 nov. 2026 : l'anglais pour les hispanophones, donc une
interface espagnole (« es ») quand la langue apprise est l'anglais. Copie de
espanol/de/extraire.py (l'allemand, interface de l'espagnol, 1er nov.).

Ecrit anglais/es/sources/<nom>.json : une liste d'entrees
{"id": ..., "fr": ..., "en": ...} ; le traducteur rend
anglais/es/lots/<nom>.es.json (ou <nom>-NN.es.json) : {id: texte espagnol}.
poser_autres.py pose ces lots ; ce script-ci n'ecrit rien hors de
anglais/es/sources/.

  i18n          I18N.fr d'index.html entier (1 607 cles), l'anglais en regard
  surcharge-en  I18N_ANGLAIS.fr : ce qui change quand on apprend l'anglais
                (pas d'anglais en regard : l'interface anglaise n'existe pas
                pour l'anglais appris)
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCES = os.path.join(ICI, "sources")
INDEX = os.path.join(RACINE, "index.html")


def lire(chemin):
    return io.open(chemin, encoding="utf-8").read()


def i18n():
    """Le dictionnaire d'interface entier (I18N.fr), avec l'anglais en regard."""
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js"), "fr", "en"],
                       capture_output=True, cwd=RACINE)
    if r.returncode:
        raise SystemExit("i18n_dump.js : " + r.stderr.decode("utf-8", "replace")[:500])
    d = json.loads(r.stdout.decode("utf-8"))
    return [{"id": k, "fr": v, "en": d["en"].get(k, "")} for k, v in d["fr"].items()]


def bloc_anglais(lignes, langue):
    """Le bloc « "fr" » de I18N_ANGLAIS, cle par cle (une cle par ligne)."""
    debut = next(i for i, l in enumerate(lignes) if l.startswith("const I18N_ANGLAIS = {"))
    ouvre = next(i for i in range(debut, len(lignes)) if lignes[i] == '    "%s": {' % langue)
    out = []
    for l in lignes[ouvre + 1:]:
        if l.startswith("    }"):
            return out
        if l.strip().startswith("//"):
            continue
        m = re.match(r'^        "([^"]+)": (".*"),?\s*$', l)
        if not m:
            raise SystemExit("I18N_ANGLAIS.%s : ligne illisible : %s" % (langue, l))
        out.append((m.group(1), json.loads(m.group(2))))
    raise SystemExit("I18N_ANGLAIS.%s : fin de bloc introuvable" % langue)


def surcharge_en(lignes):
    """I18N_ANGLAIS : ce qui change dans l'interface quand on apprend l'anglais."""
    return [{"id": k, "fr": v, "en": ""} for k, v in bloc_anglais(lignes, "fr")]


# La cle et les groupes d'une carte : les memes que ceux qui posent l'espagnol.
sys.path.insert(0, os.path.join(RACINE, "anglais", "outils"))
from espagnol import CORPUS, groupes, cle_corpus   # noqa: E402


def phrases_espagnoles():
    """Notre corpus espagnol : phrase anglaise -> phrase espagnole d'origine.
    Une phrase anglaise du corpus anglais qui vient de la (construire.py puise
    dans les deux cours) a deja son espagnol, ecrit par Wortando."""
    out = {}
    for f in sorted(os.listdir(os.path.join(RACINE, "espanol", "datos"))):
        if not f.endswith(".json"):
            continue
        try:
            d = json.load(io.open(os.path.join(RACINE, "espanol", "datos", f), encoding="utf-8"))
        except ValueError:
            continue

        def marcher(o):
            if isinstance(o, dict):
                if o.get("exemple_en") and o.get("exemple") and ("mot" in o or "infinitif" in o):
                    out.setdefault(o["exemple_en"].strip(), o["exemple"].strip())
                for v in o.values():
                    marcher(v)
            elif isinstance(o, list):
                for v in o:
                    marcher(v)
        marcher(d)
    return out


def corpus(fichier):
    """Les cartes d'un fichier du corpus americain : mot, sens francais, phrase
    anglaise et sa traduction francaise ; « es_existant » quand notre corpus
    espagnol a deja cette phrase (a relire, pas a recopier aveuglement)."""
    d = json.load(io.open(os.path.join(RACINE, "anglais", "datos", fichier + ".json"), encoding="utf-8"))
    connues = phrases_espagnoles()
    out = []
    for groupe, mots in groupes(fichier, d):
        for m in mots:
            e = {"id": cle_corpus(fichier, groupe, m), "mot": m.get("mot") or m.get("infinitif"),
                 "fr": m.get("traduction", ""), "ex": m.get("exemple", ""), "ex_fr": m.get("exemple_fr", "")}
            if m.get("kategorie"):
                e["categorie"] = m["kategorie"]
            if connues.get(e["ex"].strip()):
                e["es_existant"] = connues[e["ex"].strip()]
            out.append(e)
    return out


def categories():
    """Les categories (francaises) des adverbes, expressions et mots-outils."""
    vues = {}
    for f in ("adverbes", "expressions", "fonctionnels"):
        d = json.load(io.open(os.path.join(RACINE, "anglais", "datos", f + ".json"), encoding="utf-8"))
        for _, mots in groupes(f, d):
            for m in mots:
                if m.get("kategorie"):
                    vues.setdefault(m["kategorie"], f)
    return [{"id": k, "fr": k, "en": ""} for k in vues]


def textes_palier():
    """Les textes hors corpus du palier (espagnol_textes.NIVEAUX) : fiches, tuiles,
    temps, Premiers pas, A1 voyage, reperes, prononciation, conjugaison.
    Une entree par cle (un meme francais a deux endroits ne se traduit qu'une fois)."""
    import espagnol_textes as T
    d = os.path.join(RACINE, "anglais", "datos")
    vus, out = set(), []
    entrees = []
    # Le britannique aussi : quelques regles de prononciation n'existent que la.
    for dossier in (d, os.path.join(RACINE, "anglais", "datos-gb")):
        for nom in T.OBJETS:
            entrees += T.entrees_objets(nom, json.load(io.open(os.path.join(dossier, nom + ".json"), encoding="utf-8")))
    entrees += T.entrees_grammaire(json.load(io.open(os.path.join(d, "grammaire.json"), encoding="utf-8")))
    for cle, fr, contexte, _ in entrees:
        if cle not in vus and fr.strip():
            vus.add(cle)
            out.append({"id": cle, "fr": fr, "en": "", "contexte": contexte})
    return out


def exercices_palier():
    """Les questions des series du palier : la question (anglaise), les options, la
    bonne reponse, et la traduction et l'explication francaises a rendre en espagnol."""
    import espagnol_textes as T
    d = os.path.join(RACINE, "anglais", "datos")
    g = json.load(io.open(os.path.join(d, "grammaire.json"), encoding="utf-8"))
    jeux = json.load(io.open(os.path.join(d, "exercices.json"), encoding="utf-8"))["jeux"]
    out = []
    for jeu in sorted(T.series_du_palier(g)):
        for q in jeux.get(jeu, []):
            out.append({"id": T.cle_exercice(jeu, q), "question": q.get("question", ""), "options": q.get("options", []),
                        "correct": q.get("correct", ""), "translation": q.get("translation", ""),
                        "explanation": q.get("explanation", "")})
    return out


def scenes_palier():
    """Les textes des scenes anglaises (Boston) : description de l'image (alt), consigne,
    et le titre de la couche A1. Poses par anglais/outils/scenes.py (traductions.es)."""
    out, vus = [], set()
    for f in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "scene-*.en.js"))):
        nom = os.path.basename(f)[len("scene-"):-len(".en.js")]
        t = io.open(f, encoding="utf-8").read()
        d = json.loads(t[t.index("{"):t.rindex("}") + 1])
        for k, quoi in (("alt", "description de l'image (lecteurs d'ecran)"), ("consigne", "consigne affichee")):
            if d.get(k):
                out.append({"id": "scenes|%s|%s" % (nom, k), "fr": d[k], "en": "", "contexte": "scene %s : %s" % (nom, quoi)})
        a1 = (d.get("couches") or {}).get("A1", {}).get("titre")
        if a1 and a1 not in vus:
            vus.add(a1)
            out.append({"id": "scenes|*|A1|" + a1, "fr": a1, "en": "", "contexte": "titre de la couche A1 des scenes"})
    return out


def corpus_palier(fichier):
    """Les cartes du palier seulement (corpus-<fichier> complet reste disponible)."""
    import espagnol_textes as T
    d = json.load(io.open(os.path.join(RACINE, "anglais", "datos", fichier + ".json"), encoding="utf-8"))
    garder = set()
    for groupe, mots in groupes(fichier, d):
        for m in mots:
            if fichier == "themes":
                niv = next(t.get("niveau") for t in d["themes"] if t["id"] == groupe)
            elif fichier == "fonctionnels":
                niv = m.get("niveau")
            else:
                niv = groupe
            if niv in T.NIVEAUX:
                garder.add(cle_corpus(fichier, groupe, m))
    return [e for e in corpus(fichier) if e["id"] in garder]


def main():
    lignes = lire(INDEX).split("\n")
    travaux = {"i18n": i18n, "surcharge-en": lambda: surcharge_en(lignes), "categories": categories}
    for f in CORPUS:
        travaux["corpus-" + f] = (lambda f=f: corpus(f))
        travaux["a1-corpus-" + f] = (lambda f=f: corpus_palier(f))
    travaux["a1-textes"] = textes_palier
    travaux["a1-exercices"] = exercices_palier
    travaux["a1-scenes-textes"] = scenes_palier
    veut = sys.argv[1:] or list(travaux)
    os.makedirs(SOURCES, exist_ok=True)
    for nom in veut:
        entrees = travaux[nom]()
        with io.open(os.path.join(SOURCES, nom + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(entrees, f, ensure_ascii=False, indent=1)
            f.write("\n")
        mots = sum(len(re.sub(r"<[^>]+>", " ", e.get("fr") or e.get("explanation", "") + " " + e.get("translation", "")).split()) for e in entrees)
        print("%-14s %5d textes, %6d mots francais" % (nom, len(entrees), mots))


if __name__ == "__main__":
    main()
