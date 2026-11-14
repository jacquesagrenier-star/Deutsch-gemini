# -*- coding: utf-8 -*-
"""Fait pflege/datos/themes.json (et lectures-de.json) a partir de pflege/sources/vocabulaire/.

    python pflege/outils/construire_vocabulaire.py           # ecrit
    python pflege/outils/construire_vocabulaire.py --verifier # dit seulement si datos/ est a jour

Les donnees de pflege/datos/ sont DERIVEES : on corrige les sources, jamais le JSON.

LE FORMAT PRODUIT (celui de themes.json, mots par mots) :

  {"_lisez_moi": ..., "themes": [ un theme par (sujet, niveau) ], ...}
  theme : id "pflege_<cle>_<niveau>" (pflege_koerper_a2), nom_theme (allemand), niveau,
          domaine "pflege", sujet (cle), numero (1-10), titre {fr, en, ..., ru},
          et cinq listes :
    mots        les NOMS, cles de themes.json : mot, genre, pluriel, article_fr,
                traduction (fr), traduction_en ... traduction_ru, exemple, exemple_fr ...
                exemple_ru ; feminin / masculin comme au corpus
    verben      les verbes : infinitif, traductions, exemples ; auxiliaire + partizip2
                (pas de tables de conjugaison : les Soins n'ouvrent pas cet ecran)
    adjektive   les adjectifs : mot, traductions, exemples
    ausdruecke  les expressions et phrases du metier : mot, traductions, exemples
    reprises    les mots DEJA au corpus general : mot, type, source {fichier, theme},
                exemple_* (la phrase de soins en plus) ; precision_* quand le corpus ne
                donne pas le sens du metier. La traduction est celle de la fiche du corpus.
  Sur chaque entree : domaine "pflege" ; relire true si une infirmiere doit valider ;
  note_relecture (fr) pour elle ; sens_distinct quand le mot existe au corpus dans un
  autre sens.

  lectures-de.json : { texte allemand ecrit : texte dit en lettres } pour chaque texte
  prononce qui contient un chiffre (regle de CLAUDE.md, audio/lectures/). A verser dans
  audio/lectures/de.json le jour ou l'on fera les voix.
"""
import glob
import importlib.util
import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCES = os.path.join(RACINE, "pflege", "sources", "vocabulaire")
DATOS = os.path.join(RACINE, "pflege", "datos")
SORTIE = os.path.join(DATOS, "themes.json")
SORTIE_LECTURES = os.path.join(DATOS, "lectures-de.json")

sys.path.insert(0, ICI)
sys.path.insert(0, SOURCES)
import corpus  # noqa: E402
from commun import LANGUES, NIVEAUX  # noqa: E402
from personnages import PERSONNAGES, LANGUES_EX  # noqa: E402

ARTICLES_FR = ("le ", "la ", "les ", "l'", "l’")


def modules():
    """Les fichiers de theme, dans l'ordre (t01_..., t02_...)."""
    out = []
    for chemin in sorted(glob.glob(os.path.join(SOURCES, "t[0-9][0-9]_*.py"))):
        nom = os.path.splitext(os.path.basename(chemin))[0]
        spec = importlib.util.spec_from_file_location(nom, chemin)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        out.append((nom, m))
    return out


def noms(texte, langue):
    """Remplace {Elif}, {Frau Hoffmann}... par la forme de la langue."""
    def rep(mo):
        n = mo.group(1)
        if n not in PERSONNAGES:
            raise ValueError("personnage inconnu {%s} dans : %s" % (n, texte))
        return PERSONNAGES[n][langue]
    return re.sub(r"\{([^{}]+)\}", rep, texte)


def article_fr(trad):
    for a in ARTICLES_FR:
        if trad.startswith(a):
            return ("l'" if a in ("l'", "l’") else a), trad[len(a):]
    return "", trad


def champs_exemple(e):
    out = {}
    for lang, txt in zip(LANGUES_EX, e["ex"]):
        out["exemple" if lang == "de" else "exemple_" + lang] = noms(txt, lang)
    return out


def champs_trad(prefixe, trad, nom=False):
    out = {}
    for lang, txt in zip(LANGUES, trad):
        if lang == "fr":
            if nom:
                art, reste = article_fr(txt)
                out["article_fr"] = art
                out[prefixe] = reste
            else:
                out[prefixe] = txt
        else:
            out[prefixe + "_" + lang] = txt
    return out


def options(e, d):
    d["domaine"] = "pflege"
    if e.get("relire"):
        d["relire"] = True
    if e.get("note"):
        d["note_relecture"] = e["note"]
    if e.get("sens_distinct"):
        d["sens_distinct"] = e["sens_distinct"]
    return d


def source_reprise(e):
    """La fiche du corpus que reprend une entree R() : celle donnee, sinon la premiere
    hors chapitres VHS du bon type."""
    hits = corpus.chercher(e["mot"], e.get("type_corpus"))
    if e.get("source"):
        hits = [h for h in hits if h["ou"] == e["source"]]
    if not hits:
        raise ValueError("reprise %r : absent du corpus%s" % (e["mot"], " (source %s)" % e["source"] if e.get("source") else ""))
    hors_vhs = [h for h in hits if not str(h["ou"]).startswith("vhs_")]
    h = (hors_vhs or hits)[0]
    return h


def convertir(e):
    typ = e["type"]
    if typ == "nom":
        d = {"mot": e["mot"], "genre": e["genre"], "pluriel": e["pluriel"]}
        d.update(champs_trad("traduction", e["trad"], nom=True))
        if e.get("feminin"):
            d["feminin"] = e["feminin"]
        if e.get("masculin"):
            d["masculin"] = e["masculin"]
    elif typ == "verbe":
        d = {"infinitif": e["mot"]}
        d.update(champs_trad("traduction", e["trad"]))
        if e.get("aux"):
            d["auxiliaire"] = e["aux"]
        if e.get("p2"):
            d["partizip2"] = e["p2"]
    elif typ in ("adjectif", "expression"):
        d = {"mot": e["mot"]}
        d.update(champs_trad("traduction", e["trad"]))
    elif typ == "reprise":
        h = source_reprise(e)
        d = {"mot": h["mot"], "type": h["type"], "source": {"fichier": h["fichier"], "theme": h["ou"]}}
        if e.get("precision"):
            d.update(champs_trad("precision", e["precision"]))
    else:
        raise ValueError(typ)
    d.update(champs_exemple(e))
    return options(e, d)


LISTE = {"nom": "mots", "verbe": "verben", "adjectif": "adjektive", "expression": "ausdruecke", "reprise": "reprises"}


def construire():
    themes, lectures = [], {}
    for nom_module, m in modules():
        T = m.THEME
        titre = [x.strip() for x in T["titre"].split("|")]
        assert len(titre) == 9, nom_module
        for niv in NIVEAUX:
            entrees = [e for e in m.MOTS if e["niveau"] == niv]
            if not entrees:
                continue
            th = {
                "id": "pflege_%s_%s" % (T["cle"], niv.lower()),
                "nom_theme": T["nom_theme"],
                "niveau": niv,
                "domaine": "pflege",
                "sujet": T["cle"],
                "numero": T["numero"],
                "titre": dict(zip(LANGUES, titre)),
            }
            for liste in LISTE.values():
                th[liste] = []
            for e in entrees:
                th[LISTE[e["type"]]].append(convertir(e))
            themes.append(th)
        for ecrit, dit in getattr(m, "LECTURES", {}).items():
            lectures[noms(ecrit, "de")] = noms(dit, "de")
    doc = {
        "_lisez_moi": "Vocabulaire de la section Soins (Wortando Pflege). Fichier DERIVE : "
                      "le refaire avec python pflege/outils/construire_vocabulaire.py, jamais a la main. "
                      "Sources : pflege/sources/vocabulaire/. Controle : python tests/pflege_vocabulaire.py.",
        "themes": themes,
    }
    return doc, dict(sorted(lectures.items()))


def texte_json(x):
    return json.dumps(x, ensure_ascii=False, indent=1) + "\n"


def main():
    doc, lectures = construire()
    a_ecrire = {SORTIE: texte_json(doc), SORTIE_LECTURES: texte_json(lectures)}
    if "--verifier" in sys.argv:
        retard = []
        for chemin, contenu in a_ecrire.items():
            ancien = io.open(chemin, encoding="utf-8", newline="").read() if os.path.exists(chemin) else None
            if ancien is None or ancien.replace("\r\n", "\n") != contenu:  # git peut rendre du CRLF
                retard.append(os.path.relpath(chemin, RACINE))
        if retard:
            print("en retard sur les sources : " + ", ".join(retard))
            return 1
        print("pflege/datos/ a jour")
        return 0
    os.makedirs(DATOS, exist_ok=True)
    for chemin, contenu in a_ecrire.items():
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
            f.write(contenu)
    n = sum(len(t[l]) for t in doc["themes"] for l in LISTE.values())
    print("pflege/datos/themes.json : %d themes-niveaux, %d entrees ; lectures-de.json : %d" % (len(doc["themes"]), n, len(lectures)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
