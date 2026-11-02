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


def main():
    lignes = lire(INDEX).split("\n")
    travaux = {"i18n": i18n, "surcharge-en": lambda: surcharge_en(lignes), "categories": categories}
    for f in CORPUS:
        travaux["corpus-" + f] = (lambda f=f: corpus(f))
    veut = sys.argv[1:] or list(travaux)
    os.makedirs(SOURCES, exist_ok=True)
    for nom in veut:
        entrees = travaux[nom]()
        with io.open(os.path.join(SOURCES, nom + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(entrees, f, ensure_ascii=False, indent=1)
            f.write("\n")
        mots = sum(len(re.sub(r"<[^>]+>", " ", e["fr"]).split()) for e in entrees)
        print("%-14s %5d textes, %6d mots francais" % (nom, len(entrees), mots))


if __name__ == "__main__":
    main()
