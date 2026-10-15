# -*- coding: utf-8 -*-
"""Les textes de l'espagnol HORS corpus a traduire en arabe (15 oct. 2026).

    python espanol/ar/extraire.py

Ecrit espanol/ar/sources/<nom>.json : une liste d'entrees
{"id": ..., "fr": ..., "en": ..., "pt": ..., ["es": ...]} pour chaque texte que
le portugais a recu en v784 et que l'arabe n'a pas encore. Le traducteur rend
espanol/ar/lots/<nom>.ar.json : {id: texte arabe} (une liste de trois textes
pour les mots-outils, deux pour la prononciation). espanol/ar/poser_autres.py
pose ces lots ; ce script-ci n'ecrit rien hors de espanol/ar/sources/.

Le corpus (temas, verbos...) et les exercices passent, eux, par poser.py.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCES = os.path.join(RACINE, "espanol", "ar", "sources")
INDEX = os.path.join(RACINE, "index.html")
SCENES = os.path.join(RACINE, "visuel", "prototype", "espanol")


def lignes_index():
    return io.open(INDEX, encoding="utf-8").read().split("\n")


def bloc_i18n(lignes, langue):
    """Les cles d'un bloc de I18N_ESPAGNOL, dans l'ordre du fichier."""
    debut = next(i for i, l in enumerate(lignes) if l.startswith("const I18N_ESPAGNOL = {"))
    ouvre = next(i for i in range(debut, len(lignes)) if lignes[i] == '    "%s": {' % langue)
    out = []
    for l in lignes[ouvre + 1:]:
        if l.startswith("    }"):
            return out
        m = re.match(r'^        "([^"]+)": (".*"),?\s*$', l)
        if not m:
            raise SystemExit("I18N_ESPAGNOL.%s : ligne illisible : %s" % (langue, l))
        out.append((m.group(1), json.loads(m.group(2))))
    raise SystemExit("I18N_ESPAGNOL.%s : fin de bloc introuvable" % langue)


def i18n(lignes):
    fr, en, pt = (dict(bloc_i18n(lignes, l)) for l in ("fr", "en", "pt"))
    return [{"id": k, "fr": fr[k], "en": en[k], "pt": v} for k, v in bloc_i18n(lignes, "pt")]


def categories(lignes):
    """ADVERB_CATEGORIES et REDEWENDUNG_CATEGORIES, branche espagnole."""
    out = []
    for nom in ("ADVERB_CATEGORIES", "REDEWENDUNG_CATEGORIES"):
        debut = next(i for i, l in enumerate(lignes) if l.startswith("const %s = LANGUE_APPRISE" % nom))
        for l in lignes[debut + 2:]:
            if l.startswith("}") or l.startswith("    :"):
                break
            m = re.match(r'^    "([^"]+)":\s*\{ fr: (".*?"), en: (".*?"), pt: (".*?") \},?\s*$', l)
            if not m:
                raise SystemExit("%s : ligne illisible : %s" % (nom, l))
            out.append({"id": nom + "|" + m.group(1), "fr": json.loads(m.group(2)),
                        "en": json.loads(m.group(3)), "pt": json.loads(m.group(4))})
    return out


def mots_outils(lignes):
    """Les trois listes espagnoles codees en dur et leur portugais (rangs 20-22)."""
    texte = "\n".join(lignes)
    m = re.search(r"^const MOTS_OUTILS_ES_PT = (\{.*?\n\});", texte, re.S | re.M)
    pt = json.loads(m.group(1))
    out = []
    for theme, cle in (("praepTheme", "praep"), ("konjunktionenTheme", "konjunktionen"),
                       ("partikelnTheme", "partikeln")):
        debut = next(i for i, l in enumerate(lignes) if l.startswith("const %s = LANGUE_APPRISE" % theme))
        mots = {}
        for l in lignes[debut:]:
            if l.startswith("    :"):
                break
            s = l.strip().rstrip(",")
            if s.startswith('["'):
                w = json.loads(s)
                mots.setdefault(w[0], w)
        for es, p in pt[cle].items():
            w = mots[es]
            out.append({"id": cle + "|" + es, "es": es, "exemple_es": w[3],
                        "fr": [w[1], w[4], w[2]], "en": [w[5], w[6], w[7] if len(w) > 7 else ""], "pt": p})
    return out


def grammaire():
    d = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "grammaire.json"), encoding="utf-8"))
    out = [{"id": "textes|" + k, "fr": d["textes"]["fr"][k], "en": d["textes"]["en"][k], "pt": v}
           for k, v in d["textes"]["pt"].items()]

    def marcher(o, chemin):
        if isinstance(o, dict):
            if "pt" in o and "fr" in o:
                out.append({"id": chemin, "fr": o["fr"], "en": o.get("en", ""), "pt": o["pt"]})
                return
            for k, v in o.items():
                marcher(v, chemin + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                marcher(v, chemin + "/" + str(i))

    for f in d["fiches"]:
        marcher(f, "fiches/" + f["id"])
    return out


def prononciation():
    d = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "prononciation.json"), encoding="utf-8"))
    out = []

    def regle(rid, r, graphie):
        out.append({"id": rid, "graphie": graphie,
                    "fr": [r["court"]["fr"], r["explication"]["fr"]],
                    "en": [r["court"]["en"], r["explication"]["en"]],
                    "pt": [r["court"]["pt"], r["explication"]["pt"]],
                    "exemples": [e["mot"] for e in r.get("exemples", [])]})

    def marcher(o):
        if isinstance(o, dict):
            if "id" in o and "court" in o and "explication" in o:
                regle(o["id"], o, o.get("graphie", ""))
                for v, t in (o.get("variantes") or {}).items():
                    regle(o["id"] + "." + v, t, o.get("graphie", ""))
                return
            for v in o.values():
                marcher(v)
        elif isinstance(o, list):
            for v in o:
                marcher(v)

    marcher(d)
    return out


def variantes():
    d = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "variantes.json"), encoding="utf-8"))
    out = []
    for cle in ("noms", "verbes"):
        for mot, v in d[cle].items():
            r = v.get("remarque") if isinstance(v, dict) else None
            if isinstance(r, dict) and r.get("pt"):
                out.append({"id": cle + "|" + mot, "es": mot, "latam": v.get("mot"),
                            "fr": r["fr"], "en": r["en"], "pt": r["pt"]})
    return out


def scenes():
    out = []
    for f in sorted(os.listdir(SCENES)):
        if not f.endswith(".json") or f == "mots.json":
            continue
        d = json.load(io.open(os.path.join(SCENES, f), encoding="utf-8"))
        nom = f[:-5]
        for niv, c in d.get("couches", {}).items():
            if c.get("titre_pt"):
                out.append({"id": "%s|%s|titre" % (nom, niv), "fr": c["titre"],
                            "en": c.get("titre_en", ""), "pt": c["titre_pt"]})
            for i, q in enumerate(c.get("qs", [])):
                if q.get("n_pt"):
                    out.append({"id": "%s|%s|%d" % (nom, niv, i), "question": q["q"],
                                "phrase": q["phrase"], "fr": q["n"], "en": q.get("n_en", ""),
                                "pt": q["n_pt"]})
                lat = q.get("latam") or {}
                if lat.get("n_pt"):
                    out.append({"id": "%s|%s|%d|latam" % (nom, niv, i),
                                "question": lat.get("q", q["q"]), "phrase": lat.get("phrase", q["phrase"]),
                                "fr": lat.get("n", q["n"]), "en": lat.get("n_en", ""), "pt": lat["n_pt"]})
    return out


def main():
    os.makedirs(SOURCES, exist_ok=True)
    lignes = lignes_index()
    for nom, entrees in (("i18n", i18n(lignes)), ("categories", categories(lignes)),
                         ("mots-outils", mots_outils(lignes)), ("grammaire", grammaire()),
                         ("prononciation", prononciation()), ("variantes", variantes()),
                         ("scenes", scenes())):
        chemin = os.path.join(SOURCES, nom + ".json")
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(
            json.dumps(entrees, ensure_ascii=False, indent=1) + "\n")
        print("  %-14s %4d textes" % (nom, len(entrees)))


if __name__ == "__main__":
    main()
