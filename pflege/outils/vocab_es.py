# -*- coding: utf-8 -*-
"""L'espagnol (10e langue d'interface, décision de Jacques du 16 nov. 2026) dans le vocabulaire des Soins.

    python pflege/outils/vocab_es.py exporter      # écrit pflege/sources/vocabulaire/es/lot_NN.json : ce qui manque
    python pflege/outils/vocab_es.py importer      # recopie les champs « es_* » remplis dans les sources compactes
    python pflege/outils/vocab_es.py compter       # ce qui reste à traduire
    python pflege/outils/vocab_es.py verifier lot_01   # contraste mécanique d'un lot rempli

Pourquoi un outil à part : les mots, les paires et les abréviations ne passent pas par
pflege/sources/traductions/ (la chaîne des dialogues, des scènes et de l'écrit) ; leurs langues vivent DANS leurs
sources (pflege/sources/vocabulaire/tNN_*.py, « | » entre les langues, l'espagnol en dernier). Ce script les en
sort pour la traduction, puis les y remet, au caractère près, sans réécrire le reste du fichier.

Les lots : d'abord les 4 premiers chapitres (la douleur, la relève, l'admission, le téléphone), puis le reste par
thème. Un champ à remplir vaut "" ; l'importation ne prend que ce qui est rempli et l'efface du lot. Consignes de
traduction : pflege/sources/vocabulaire/es/CONSIGNES.md.
"""
import ast
import glob
import importlib.util
import io
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VOC = os.path.join(RACINE, "pflege", "sources", "vocabulaire")
ES = os.path.join(VOC, "es")
VITAL = os.path.join(RACINE, "pflege", "sources", "vitalzeichen.py")
sys.path.insert(0, VOC)
import adaptateur  # noqa: E402

PRIORITE = ["ch07_schmerz", "ch08_uebergabe", "ch01_aufnahme", "ch10_telefon"]
TAILLE_LOT = 110
ORDRE = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]   # ordre des sources compactes


def _chapitres():
    spec = importlib.util.spec_from_file_location("chapitres_src", os.path.join(RACINE, "pflege", "sources", "chapitres.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def modules():
    return sorted(os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(VOC, "t[0-9][0-9]_*.py")))


def champs(texte):
    return [p.strip() for p in texte.split("|")]


def items_module(mod, CH):
    """Les entrées sans espagnol d'un module compact, avec ce qu'il faut traduire."""
    m = adaptateur.charger(mod)
    base = "soins_" + m.THEME["cle"]
    out = []
    t = champs(m.THEME["titre"])
    if len(t) == 9:
        out.append({"id": mod + "#titre", "chapitre": "", "sorte": "titre du thème", "mot": m.THEME["nom_theme"],
                    "fr": t[0], "en": t[1], "pt": t[6], "es_trad": ""})
    caches = set()
    if mod == "t03_vitalzeichen":   # ses entrées déjà parmi les 31 noms de l'architecture ne sont pas affichées
        caches = {adaptateur.corpus.cle(x[2], garder_sich=True) for x in _vital().MOTS if isinstance(x, tuple)}
    for i, e in enumerate(m.MOTS):
        if adaptateur.corpus.cle(e["mot"], garder_sich=True) in caches:
            continue
        d = adaptateur._chapitre(adaptateur.convertir(e, {}), mod)
        ch = d.get("chapitre") or CH.THEME_DEFAUT.get(base) or ""
        if "(=" in d["mot"] and not e.get("chapitre"):
            ch = CH.ABREVIATIONS_DEFAUT
        it = {"id": "%s#%d" % (mod, i), "chapitre": ch, "sorte": e["type"], "niveau": e["niveau"]}
        if e["type"] == "nom":
            it["mot"] = "%s %s" % ("die" if e["genre"] == "die (Pl.)" else e["genre"], e["mot"])
        else:
            it["mot"] = e["mot"]
        ex = e["ex"]
        besoin = []
        if e["type"] == "reprise":
            it["fr"], it["en"], it["pt"] = d["trad"]["fr"][0], d["trad"]["en"][0], d["trad"]["pt"][0]
            if e.get("precision"):
                if len(e["precision"]) == 9:
                    besoin.append("es_trad")
            elif not e.get("es_trad") and not (adaptateur.source_reprise(e)["fiche"] or {}).get("traduction_es"):
                besoin.append("es_trad")
        else:
            tr = e["trad"]
            it["fr"], it["en"], it["pt"] = tr[0], tr[1], tr[6]
            if len(tr) == 9:
                besoin.append("es_trad")
        if len(ex) == 10:
            besoin.append("es_ex")
        it["de_ex"], it["fr_ex"], it["en_ex"] = ex[0], ex[1], ex[2]
        if e["type"] == "paire":
            it["patient"] = e["patient"]
            tp, xp = e["trad_patient"], e["ex_patient"]
            it["fr_patient"], it["en_patient"] = tp[0], tp[1]
            it["de_ex_patient"], it["fr_ex_patient"] = xp[0], xp[1]
            if len(tp) == 9:
                besoin.append("es_trad_patient")
            if len(xp) == 10:
                besoin.append("es_ex_patient")
        if e.get("note"):
            it["note"] = e["note"]
        if not besoin:
            continue
        for b in besoin:
            it[b] = ""
        out.append(it)
    return out


def _vital():
    spec = importlib.util.spec_from_file_location("vital", VITAL)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def items_vital(CH):
    """Les 31 noms de l'architecture (tuples) : le dictionnaire {langue: (traduction, exemple)}."""
    m = _vital()
    out = []
    for i, x in enumerate(m.MOTS):
        if not isinstance(x, tuple) or "es" in x[5]:
            continue
        niveau, genre, mot, _, _, tr, ex_de, _ = x
        out.append({"id": "vitalzeichen#%d" % i, "chapitre": CH.THEME_DEFAUT.get("soins_vitalzeichen", ""),
                    "sorte": "nom", "niveau": niveau, "mot": "%s %s" % (genre, mot), "fr": tr["fr"][0],
                    "en": tr["en"][0], "pt": tr["pt"][0], "de_ex": ex_de, "fr_ex": tr["fr"][1], "en_ex": tr["en"][1],
                    "es_trad": "", "es_ex": ""})
    return out


def tous_les_items():
    CH = _chapitres()
    items = []
    for mod in modules():
        items += items_module(mod, CH)
    items += items_vital(CH)
    return items


def exporter():
    os.makedirs(ES, exist_ok=True)
    deja = {}
    for f in glob.glob(os.path.join(ES, "lot_*.json")):
        for it in json.load(io.open(f, encoding="utf-8"))["items"]:
            deja[it["id"]] = f
    items = [it for it in tous_les_items() if it["id"] not in deja]
    rang = {c: i for i, c in enumerate(PRIORITE)}
    items.sort(key=lambda it: (rang.get(it["chapitre"], len(PRIORITE)), it["id"].split("#")[0]))
    n = len(glob.glob(os.path.join(ES, "lot_*.json")))
    for k in range(0, len(items), TAILLE_LOT):
        n += 1
        lot = items[k:k + TAILLE_LOT]
        chemin = os.path.join(ES, "lot_%02d.json" % n)
        json.dump({"_lisez_moi": "Remplir les champs es_* vides (pflege/sources/vocabulaire/es/CONSIGNES.md), "
                                 "puis python pflege/outils/vocab_es.py importer.", "items": lot},
                  io.open(chemin, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        print("ecrit", os.path.relpath(chemin, RACINE), ":", len(lot), "entrees,",
              ", ".join(sorted({it["chapitre"] for it in lot})))
    if not items:
        print("rien a exporter")


# ── importation : insertion au caractère près ──────────────────────────────────────────────────────────

def _octet(lignes, ligne, col):
    """Position (index dans le texte complet) d'un (lineno, col_offset UTF-8) de l'AST."""
    debut = sum(len(l) for l in lignes[:ligne - 1])
    return debut + len(lignes[ligne - 1].encode("utf-8")[:col].decode("utf-8"))


def _avant_guillemet(lignes, node):
    """Position juste avant le guillemet fermant d'une chaîne littérale."""
    return _octet(lignes, node.end_lineno, node.end_col_offset) - 1


def _verifie(txt, quoi):
    if not txt or '"' in txt or "\\" in txt or "\n" in txt or "|" in txt:
        raise ValueError("%s : texte espagnol refuse (vide, guillemet droit, antislash, saut de ligne ou |) : %r" % (quoi, txt))
    return txt


def _liste_mots(arbre):
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "MOTS" for t in n.targets):
            return n.value.elts
    raise ValueError("MOTS introuvable")


def _theme_titre(arbre):
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "THEME" for t in n.targets):
            for k, v in zip(n.value.keys, n.value.values):
                if isinstance(k, ast.Constant) and k.value == "titre":
                    return v
    raise ValueError("THEME['titre'] introuvable")


INDICES = {"N": (3, 4), "V": (2, 3), "A": (2, 3), "X": (2, 3), "R": (None, 2)}


def inserer_module(chemin, items):
    texte = io.open(chemin, encoding="utf-8").read()
    lignes = texte.splitlines(keepends=True)
    arbre = ast.parse(texte)
    elts = _liste_mots(arbre)
    ajouts = []   # (position, texte)
    for it in items:
        idx = it["id"].split("#")[1]
        if idx == "titre":
            if it.get("es_trad"):
                ajouts.append((_avant_guillemet(lignes, _theme_titre(arbre)), " | " + _verifie(it["es_trad"], it["id"])))
            continue
        call = elts[int(idx)]
        f = call.func.id
        kw = {k.arg: k.value for k in call.keywords}
        if f == "P":
            cibles = {"es_trad_patient": call.args[3], "es_trad": call.args[4], "es_ex_patient": call.args[5],
                      "es_ex": call.args[6]}
        else:
            i_tr, i_ex = INDICES[f]
            cibles = {"es_ex": call.args[i_ex]}
            if i_tr is not None:
                cibles["es_trad"] = call.args[i_tr]
            elif "precision" in kw:
                cibles["es_trad"] = kw["precision"]
        for champ, node in cibles.items():
            if it.get(champ):
                ajouts.append((_avant_guillemet(lignes, node), " | " + _verifie(it[champ], it["id"] + " " + champ)))
        if f == "R" and "precision" not in kw and it.get("es_trad"):
            fin = _octet(lignes, call.end_lineno, call.end_col_offset) - 1      # la parenthèse fermante
            ajouts.append((fin, ', es_trad="%s"' % _verifie(it["es_trad"], it["id"] + " es_trad")))
    for pos, ajout in sorted(ajouts, key=lambda a: -a[0]):
        texte = texte[:pos] + ajout + texte[pos:]
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    return len(ajouts)


def inserer_vital(items):
    texte = io.open(VITAL, encoding="utf-8").read()
    lignes = texte.splitlines(keepends=True)
    elts = _liste_mots(ast.parse(texte))
    ajouts = []
    for it in items:
        if not (it.get("es_trad") and it.get("es_ex")):
            continue
        dico = elts[int(it["id"].split("#")[1])].elts[5]
        fin = _octet(lignes, dico.values[-1].end_lineno, dico.values[-1].end_col_offset)
        ajouts.append((fin, ',\n        "es": ("%s", "%s")' % (_verifie(it["es_trad"], it["id"]), _verifie(it["es_ex"], it["id"]))))
    for pos, ajout in sorted(ajouts, key=lambda a: -a[0]):
        texte = texte[:pos] + ajout + texte[pos:]
    io.open(VITAL, "w", encoding="utf-8", newline="\n").write(texte)
    return len(ajouts)


def importer():
    lots = sorted(glob.glob(os.path.join(ES, "lot_*.json")))
    par_module = {}
    for f in lots:
        for it in json.load(io.open(f, encoding="utf-8"))["items"]:
            if any(it.get(k) for k in ("es_trad", "es_ex", "es_trad_patient", "es_ex_patient")):
                par_module.setdefault(it["id"].split("#")[0], []).append(it)
    total = 0
    for mod, items in sorted(par_module.items()):
        n = inserer_vital(items) if mod == "vitalzeichen" else inserer_module(os.path.join(VOC, mod + ".py"), items)
        print("%-20s %d champs" % (mod, n))
        total += n
    # ce qui est importé quitte les lots (un lot vide disparaît)
    for f in lots:
        donnees = json.load(io.open(f, encoding="utf-8"))
        reste = []
        for it in donnees["items"]:
            vides = [k for k in ("es_trad", "es_ex", "es_trad_patient", "es_ex_patient") if k in it and not it[k]]
            if vides:
                for k in ("es_trad", "es_ex", "es_trad_patient", "es_ex_patient"):
                    if k in it and it[k]:
                        del it[k]
                reste.append(it)
        if reste:
            donnees["items"] = reste
            json.dump(donnees, io.open(f, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        else:
            os.remove(f)
    print("importe :", total, "champs")


PORTUGAIS = ("ã", "õ", "ç", " você", " não ", " é ", " uma ", " com ", " muito ", " também ")  # pas « está » : de l espagnol aussi


def verifier(nom):
    """Le contraste mécanique d'un lot : ce qu'une machine peut voir, avant tout avis de modèle."""
    import re
    chemin = os.path.join(ES, nom if nom.endswith(".json") else nom + ".json")
    items = json.load(io.open(chemin, encoding="utf-8"))["items"]
    pb = []
    for it in items:
        for k in ("es_trad", "es_ex", "es_trad_patient", "es_ex_patient"):
            if k not in it:
                continue
            v = it[k]
            ou = "%s %s" % (it["id"], k)
            if not v:
                pb.append(ou + " : vide")
                continue
            if any(c in v for c in '"\\|\n'):
                pb.append(ou + " : guillemet droit, antislash, | ou saut de ligne")
            if re.search(r"[Ѐ-ӿ؀-ۿ]", v):
                pb.append(ou + " : pas en alphabet latin")
            if "?" in v and "¿" not in v:
                pb.append(ou + " : « ¿ » manquant")
            if "!" in v and "¡" not in v:
                pb.append(ou + " : « ¡ » manquant")
            if any(p in (" " + v.lower() + " ") for p in PORTUGAIS):
                pb.append(ou + " : du portugais ? %r" % v)
            src = {"es_ex": "de_ex", "es_ex_patient": "de_ex_patient"}.get(k)
            if src:
                if re.search(r"\d", v):
                    pb.append(ou + " : chiffre")
                noms_de = sorted(re.findall(r"\{[^{}]+\}", it.get(src, "")))
                noms_es = sorted(re.findall(r"\{[^{}]+\}", v))
                if noms_de != noms_es:
                    pb.append(ou + " : noms %s au lieu de %s" % (noms_es, noms_de))
                if re.search(r"\b(el|la|los|las|del|al)\s+\{(Herr|Frau|Dr)", v, re.I):
                    pb.append(ou + " : article devant un gabarit qui le porte déjà")
                fr = it.get({"es_ex": "fr_ex", "es_ex_patient": "fr_ex_patient"}[k], "")
                if fr and not (0.5 <= len(v) / max(len(fr), 1) <= 1.9):
                    pb.append(ou + " : longueur douteuse (%d contre %d en français)" % (len(v), len(fr)))
            if v.strip() == str(it.get("pt", "")).strip() and len(v) > 4:
                pb.append(ou + " : identique au portugais")
    print("%s : %d entrees" % (nom, len(items)))
    for p in pb:
        print("  " + p)
    print("aucun probleme" if not pb else "%d point(s)" % len(pb))
    return 1 if pb else 0


def compter():
    items = tous_les_items()
    par = {}
    for it in items:
        par[it["chapitre"]] = par.get(it["chapitre"], 0) + 1
    print("sans espagnol :", len(items), "entrees")
    for ch, n in sorted(par.items()):
        print("  %-20s %d" % (ch or "(titres)", n))


def remplir(nom, reponses):
    """Recopie dans un lot un fichier de réponses {id: {champ: texte}} (champs es_* seulement)."""
    chemin = os.path.join(ES, nom if nom.endswith(".json") else nom + ".json")
    donnees = json.load(io.open(chemin, encoding="utf-8"))
    rep = json.load(io.open(reponses, encoding="utf-8"))
    n = 0
    for it in donnees["items"]:
        for k, v in rep.get(it["id"], {}).items():
            if k in it and k.startswith("es_"):
                it[k] = v
                n += 1
            else:
                print("  ignore :", it["id"], k)
    inconnus = set(rep) - {it["id"] for it in donnees["items"]}
    for i in sorted(inconnus):
        print("  id inconnu :", i)
    json.dump(donnees, io.open(chemin, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print("%s : %d champs recopies" % (nom, n))


if __name__ == "__main__":
    if sys.argv[1] == "verifier":
        sys.exit(verifier(sys.argv[2]))
    if sys.argv[1] == "remplir":
        sys.exit(remplir(sys.argv[2], sys.argv[3]))
    {"exporter": exporter, "importer": importer, "compter": compter}[sys.argv[1]]()
