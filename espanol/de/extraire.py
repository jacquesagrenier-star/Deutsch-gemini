# -*- coding: utf-8 -*-
"""Les textes de l'espagnol a traduire en ALLEMAND (1er nov. 2026).

    python espanol/de/extraire.py

Decide par Jacques le 1er nov. 2026 : ouvrir l'espagnol aux germanophones,
donc une interface en allemand (« de ») quand la langue apprise est
l'espagnol. Copie de espanol/ar/extraire.py (l'arabe, 15 oct.), plus ce qui
est venu apres lui : l'interface entiere (I18N, l'arabe l'avait deja pour
l'allemand appris), les Premiers pas, l'A1 voyage, les reperes, les feuilles
de conjugaison, les notices des peintres, la page des scenes.

Ecrit espanol/de/sources/<nom>.json : une liste d'entrees
{"id": ..., "fr": ..., "en": ..., [...]} ; le traducteur rend
espanol/de/lots/<nom>.de.json : {id: texte allemand}. poser_autres.py pose
ces lots ; ce script-ci n'ecrit rien hors de espanol/de/sources/.

Le corpus (temas, verbos...) et les exercices passent, eux, par poser.py.
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
DATOS = os.path.join(RACINE, "espanol", "datos")
SCENES = os.path.join(RACINE, "visuel", "prototype", "espanol")
PAGE_SCENES = os.path.join(RACINE, "visuel", "prototype", "index.html")

# Les fichiers de donnees ou chaque texte est un objet {fr, en, pt, ar}.
# grammaire.json est a part (textes.<langue> + les fiches).
OBJETS = ["premiers-pas", "a1-voyage", "reperes", "conjugaison"]


def lire(chemin):
    return io.open(chemin, encoding="utf-8").read()


def evaluer(js):
    """Evalue une expression JavaScript (un objet litteral) par node."""
    r = subprocess.run(["node", "-e", "process.stdout.write(JSON.stringify(" + js + "))"],
                       capture_output=True)
    if r.returncode:
        raise SystemExit("node : " + r.stderr.decode("utf-8", "replace")[:500])
    return json.loads(r.stdout.decode("utf-8"))


def i18n():
    """Le dictionnaire d'interface entier (I18N.fr), avec l'anglais en regard."""
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js"), "fr", "en"],
                       capture_output=True, cwd=RACINE)
    if r.returncode:
        raise SystemExit("i18n_dump.js : " + r.stderr.decode("utf-8", "replace")[:500])
    d = json.loads(r.stdout.decode("utf-8"))
    return [{"id": k, "fr": v, "en": d["en"].get(k, "")} for k, v in d["fr"].items()]


def bloc_espagnol(lignes, langue):
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


def i18n_es(lignes):
    """I18N_ESPAGNOL : ce qui change dans l'interface quand on apprend l'espagnol."""
    en = dict(bloc_espagnol(lignes, "en"))
    return [{"id": k, "fr": v, "en": en.get(k, "")} for k, v in bloc_espagnol(lignes, "fr")]


def categories(lignes):
    """ADVERB_CATEGORIES et REDEWENDUNG_CATEGORIES, branche espagnole."""
    out = []
    for nom in ("ADVERB_CATEGORIES", "REDEWENDUNG_CATEGORIES"):
        debut = next(i for i, l in enumerate(lignes) if l.startswith("const %s = LANGUE_APPRISE" % nom))
        for l in lignes[debut + 2:]:
            if l.startswith("}") or l.startswith("    :"):
                break
            m = re.match(r'^    "([^"]+)":\s*\{ fr: (".*?"), en: (".*?"), pt: (".*?"), ar: (".*?") \},?\s*$', l)
            if not m:
                raise SystemExit("%s : ligne illisible : %s" % (nom, l))
            out.append({"id": nom + "|" + m.group(1), "fr": json.loads(m.group(2)),
                        "en": json.loads(m.group(3))})
    return out


def mots_outils(lignes):
    """Les trois listes espagnoles codees en dur (prepositions, conjonctions,
    particules) : [traduction, exemple traduit, categorie]."""
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
        for es in pt[cle]:
            w = mots[es]
            out.append({"id": cle + "|" + es, "es": es, "exemple_es": w[3],
                        "fr": [w[1], w[4], w[2]], "en": [w[5], w[6], w[7] if len(w) > 7 else ""]})
    return out


def scenes_courts(lignes):
    """SCENES_COURTS : les titres courts des vignettes des scenes."""
    texte = "\n".join(lignes)
    m = re.search(r"^const SCENES_COURTS = \{\n(.*?)\n\};", texte, re.S | re.M)
    d = {}
    for l in m.group(1).split("\n"):
        mm = re.match(r'^    ([a-z]{2}): (\[.*\]),?\s*$', l)
        if mm:
            d[mm.group(1)] = json.loads(mm.group(2))
    ordre = re.search(r"^const SCENES_ORDRE_COURT = (\[.*?\]);", texte, re.S | re.M).group(1)
    ordre = json.loads(ordre)
    return [{"id": nom, "fr": d["fr"][i], "en": d["en"][i]} for i, nom in enumerate(ordre)]


def page_scenes():
    """TEXTES de visuel/prototype/index.html (la page des scenes)."""
    s = lire(PAGE_SCENES)
    d = s.index("const TEXTES = {")
    f = s.index("\n};", d)
    textes = evaluer(s[d + len("const TEXTES = "):f + 2])
    return [{"id": k, "fr": v["fr"], "en": v.get("en", "")} for k, v in textes.items()]


def objets(nom):
    """Chaque objet {fr, en, pt, ar} du fichier, repere par son chemin."""
    d = json.load(io.open(os.path.join(DATOS, nom + ".json"), encoding="utf-8"))
    out = []

    def marcher(o, chemin):
        if isinstance(o, dict):
            if isinstance(o.get("fr"), str) and "ar" in o:
                out.append({"id": chemin, "fr": o["fr"], "en": o.get("en", "")})
                return
            for k, v in o.items():
                if not k.startswith("_"):
                    marcher(v, chemin + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                marcher(v, chemin + "/" + str(i))
    marcher(d, "")
    return out


def grammaire():
    d = json.load(io.open(os.path.join(DATOS, "grammaire.json"), encoding="utf-8"))
    out = [{"id": "textes|" + k, "fr": v, "en": d["textes"]["en"].get(k, "")}
           for k, v in d["textes"]["fr"].items()]

    def marcher(o, chemin):
        if isinstance(o, dict):
            if "ar" in o and "fr" in o:
                out.append({"id": chemin, "fr": o["fr"], "en": o.get("en", "")})
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
    d = json.load(io.open(os.path.join(DATOS, "prononciation.json"), encoding="utf-8"))
    out = []

    def regle(rid, r, graphie):
        out.append({"id": rid, "graphie": graphie,
                    "fr": [r["court"]["fr"], r["explication"]["fr"]],
                    "en": [r["court"]["en"], r["explication"]["en"]],
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
    d = json.load(io.open(os.path.join(DATOS, "variantes.json"), encoding="utf-8"))
    out = []
    for cle in ("noms", "verbes"):
        for mot, v in d[cle].items():
            r = v.get("remarque") if isinstance(v, dict) else None
            if isinstance(r, dict) and r.get("ar"):
                out.append({"id": cle + "|" + mot, "es": mot, "latam": v.get("mot"),
                            "fr": r["fr"], "en": r["en"]})
    return out


def peintres():
    d = json.load(io.open(os.path.join(RACINE, "espanol", "mosaique", "peintres.json"), encoding="utf-8"))
    return [{"id": nom, "fr": p["fr"], "en": p.get("en", "")} for nom, p in d["peintres"].items()]


def scenes():
    """Les notes des questions (n), les titres des couches, et le texte de
    l'image (alt) et la consigne : ces deux-la viennent de la scene allemande
    pour les autres langues ; en allemand ils s'ecrivent dans
    espanol/<scene>.json (alt_de, consigne_de) pour ne pas toucher aux
    scenes allemandes."""
    out = []
    for f in sorted(os.listdir(SCENES)):
        if not f.endswith(".json") or f == "mots.json":
            continue
        d = json.load(io.open(os.path.join(SCENES, f), encoding="utf-8"))
        nom = f[:-5]
        js = os.path.join(RACINE, "visuel", "prototype", "scene-%s.es.js" % nom)
        if os.path.exists(js):
            s = lire(js)
            sc = json.loads(s[s.index("=") + 1:s.rindex(";")])
            en = ((sc.get("traductions") or {}).get("en") or {}).get("champs", {})
            for champ in ("alt", "consigne"):
                if sc.get(champ):
                    out.append({"id": "%s|%s" % (nom, champ), "fr": sc[champ], "en": en.get(champ, "")})
        for niv, c in d.get("couches", {}).items():
            if c.get("titre_ar"):
                out.append({"id": "%s|%s|titre" % (nom, niv), "fr": c["titre"],
                            "en": c.get("titre_en", "")})
            for i, q in enumerate(c.get("qs", [])):
                # « sens » : le sens de la phrase espagnole, montre apres la reponse.
                if q.get("sens_ar"):
                    out.append({"id": "%s|%s|%d|sens" % (nom, niv, i), "phrase": q["phrase"],
                                "fr": q["sens"], "en": q.get("sens_en", "")})
                if q.get("n_ar"):
                    out.append({"id": "%s|%s|%d" % (nom, niv, i), "question": q["q"],
                                "phrase": q["phrase"], "fr": q["n"], "en": q.get("n_en", "")})
                lat = q.get("latam") or {}
                if lat.get("n_ar"):
                    out.append({"id": "%s|%s|%d|latam" % (nom, niv, i),
                                "question": lat.get("q", q["q"]), "phrase": lat.get("phrase", q["phrase"]),
                                "fr": lat.get("n", q["n"]), "en": lat.get("n_en", "")})
    return out


def main():
    os.makedirs(SOURCES, exist_ok=True)
    lignes = lire(INDEX).replace("\r\n", "\n").split("\n")
    travaux = [("i18n", i18n()), ("surcharge-es", i18n_es(lignes)), ("categories", categories(lignes)),
               ("mots-outils", mots_outils(lignes)), ("vignettes", scenes_courts(lignes)),
               ("page-scenes", page_scenes()), ("grammaire", grammaire()),
               ("prononciation", prononciation()), ("variantes", variantes()),
               ("peintres", peintres()), ("scenes", scenes())]
    travaux += [(nom, objets(nom)) for nom in OBJETS]
    for nom, entrees in travaux:
        chemin = os.path.join(SOURCES, nom + ".json")
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(
            json.dumps(entrees, ensure_ascii=False, indent=1) + "\n")
        signes = sum(len(json.dumps(e.get("fr"), ensure_ascii=False)) for e in entrees)
        print("  %-14s %5d textes  %7d signes (fr)" % (nom, len(entrees), signes))


if __name__ == "__main__":
    main()
