"""Les données japonaises de l'app, au format de l'espagnol (espanol/datos/).

Lit les fiches jugées (japonais/cartes/mots-n*.json, phrases-n*.json, refaites
par japonais/cartes/outils/construire.py) et le catalogue des domaines
(japonais/cartes/domaines.json), et écrit à côté de ce script :

  themes.json       {"themes": [...]}  les noms, rangés par domaine et par niveau
  verbes.json       {"A1": [...], ...} avec leurs formes (moteur de conjugaison)
  adjectifs.json    idem, adjectifs en い et en な
  adverbes.json     avec « kategorie »
  expressions.json  expressions et interjections
  fonctionnels.json particules, conjonctions, pronoms, compteurs, préfixes…

Les mêmes clés que l'espagnol (mot, traduction, traduction_en, exemple,
exemple_fr, exemple_en, theme_source, kategorie), plus ce que le japonais
demande : lecture (kana), romaji, furigana, kanji, jlpt, id (la clé de
progression, « jmdict:<n> », stable pour toujours).

Niveaux : N5 -> A1, N4 -> A2, N3 -> B1, N2 -> B2, N1 -> C1 (approximation
assumée, pour que le moteur garde ses cinq niveaux).

Fichier dérivé : ne jamais corriger ces JSON à la main, corriger la décision
(japonais/cartes/decisions/) et relancer.

Usage : python japonais/datos/construire.py
"""
import importlib.util
import json
import os
import subprocess
import sys
from collections import Counter, OrderedDict, defaultdict

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.dirname(ICI)
CARTES = os.path.join(JAPONAIS, "cartes")
NIVEAUX = OrderedDict([("N5", "A1"), ("N4", "A2"), ("N3", "B1"), ("N2", "B2"), ("N1", "C1")])

VERBES = {"v1", "v1-s", "v5u", "v5k", "v5g", "v5s", "v5t", "v5n", "v5b", "v5m", "v5r", "v5k-s",
          "v5r-i", "v5u-s", "v5aru", "vk", "vs-i", "vs-s", "vz", "v2a-s"}
ADJECTIFS = {"adj-i", "adj-ix", "adj-na", "adj-f", "adj-t", "adj-pn"}
ADVERBES = {"adv", "adv-to"}
EXPRESSIONS = {"exp", "int"}
FONCTIONNELS = OrderedDict([("prt", "particule"), ("conj", "conjonction"), ("pn", "pronom"),
                            ("ctr", "compteur"), ("aux", "auxiliaire"), ("pref", "préfixe"),
                            ("suf", "suffixe")])
# この, その, こんな… sont des « adj-pn » pour JMdict, mais des démonstratifs
# pour un apprenant : ils vont avec les mots-outils, comme este / ese en espagnol.
DEMONSTRATIFS = ("こ", "そ", "あ", "ど")
TAILLE_MIN_THEME = 4      # en dessous, les noms rejoignent « mots_utiles » du niveau
TAILLE_MAX_THEME = 60     # au-dessus, le thème est coupé en parties


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire(nom, donnees):
    with open(os.path.join(ICI, nom), "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)
        f.write("\n")


def nature(f):
    c = f["classe"]["v"] or "n"
    kana = f["ecritures"]["kana"]["v"]
    if c in VERBES:
        return "verbe"
    if c == "adj-pn" and kana.startswith(DEMONSTRATIFS):
        return "fonctionnel"
    if c in ADJECTIFS:
        return "adjectif"
    if c in ADVERBES:
        return "adverbe"
    if c in EXPRESSIONS:
        return "expression"
    if c in FONCTIONNELS:
        return "fonctionnel"
    return "nom"


def conjuguer(fiches):
    """Toutes les formes d'un coup, par le moteur JavaScript (une seule source de vérité)."""
    demandes = [{"kanji": f["ecritures"]["kanji"]["v"], "kana": f["ecritures"]["kana"]["v"],
                 "classe": f["classe"]["v"]} for f in fiches]
    r = subprocess.run(["node", os.path.join(ICI, "conjuguer.js")], input=json.dumps(demandes),
                       capture_output=True, text=True, encoding="utf-8", check=True)
    return json.loads(r.stdout)


def entree(f, phrases, domaines_niv):
    k = f["ecritures"]["kanji"]["v"]
    kana = f["ecritures"]["kana"]["v"]
    e = OrderedDict()
    e["mot"] = k or kana
    e["lecture"] = kana
    e["romaji"] = f["ecritures"]["romaji"]["v"]
    e["furigana"] = f["furigana"]["v"]
    e["traduction"] = f["gloses"]["fr"]["affichee"]["v"]
    e["traduction_en"] = f["gloses"]["en"]["affichee"]["v"]
    autres_fr = [a["v"] for a in f["gloses"]["fr"]["autres"]]
    autres_en = [a["v"] for a in f["gloses"]["en"]["autres"]]
    if autres_fr:
        e["traduction_autres"] = autres_fr
    if autres_en:
        e["traduction_autres_en"] = autres_en
    if f["gloses"]["fr"]["affichee"].get("note"):
        e["note"] = f["gloses"]["fr"]["affichee"]["note"]
    p = phrases.get(f["phrases"][0]) if f["phrases"] else None
    if p:
        e["exemple"] = p["texte"]["ja"]["v"]
        e["exemple_fr"] = p["texte"]["fr"]["v"]
        e["exemple_en"] = p["texte"]["en"]["v"]
        # Tatoeba est sous CC BY : l'auteur de chaque phrase doit pouvoir être cité.
        e["exemple_source"] = OrderedDict([("tatoeba", p["tatoeba"]["ids"]), ("auteurs", p["tatoeba"]["auteurs"])])
    e["theme_source"] = domaines_niv(f)
    e["id"] = f["id"]
    e["jlpt"] = f["niveau"]
    e["classe"] = f["classe"]["v"]
    e["kanji"] = f["kanji"]
    # Rien n'est relu par un natif : tout part en brouillon, avec le verdict de la machine.
    e["statut"] = "brouillon"
    e["verdict_machine"] = f["verdict_machine"]
    return e


def romaji_de():
    """Le romaji des cartes, calculé par la même fonction que les fiches
    (japonais/cartes/outils/construire.py ; chargé sous un autre nom, ce
    fichier-ci s'appelant aussi construire.py)."""
    spec = importlib.util.spec_from_file_location("cartes_construire", os.path.join(CARTES, "outils", "construire.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.romaji


def ajouts(catalogue, cle, decisions, candidates, romaji):
    """Les mots écrits par Wortando hors des listes JLPT (particules,
    expressions), avec la phrase Tatoeba choisie pour chacun."""
    chemin = os.path.join(CARTES, catalogue)
    if not os.path.exists(chemin):
        return []
    choix = {}
    if os.path.exists(os.path.join(CARTES, "decisions", decisions)):
        choix = {d["id"]: d for d in lire(os.path.join(CARTES, "decisions", decisions))}
    cands = {}
    if os.path.exists(os.path.join(CARTES, "sources", candidates)):
        for x in lire(os.path.join(CARTES, "sources", candidates)):
            for p in x["phrases"]:
                cands[(x["id"], p["jpn"])] = p
    out = []
    for a in lire(chemin)[cle]:
        e = OrderedDict()
        e["mot"] = a["mot"]
        e["lecture"] = a["lecture"]
        e["romaji"] = romaji(a["lecture"])
        e["furigana"] = [[a["mot"], None]] if a["mot"] == a["lecture"] else None
        e["traduction"] = a["fr"]
        e["traduction_en"] = a["en"]
        if a.get("note"):
            e["note"] = a["note"]
        d = choix.get(a["id"]) or {}
        p = cands.get((a["id"], d["phrases"][0])) if d.get("phrases") else None
        if p:
            e["exemple"] = p["ja"]
            e["exemple_fr"] = p["fr"]
            if p.get("en"):
                e["exemple_en"] = p["en"]
            e["exemple_source"] = p["tatoeba"]
        e["theme_source"] = "mots_utiles_" + NIVEAUX[a["jlpt"]].lower()
        e["id"] = a["id"]
        e["jlpt"] = a["jlpt"]
        e["kategorie"] = a["kategorie"]
        if a.get("registre"):
            e["registre"] = a["registre"]
        e["statut"] = "brouillon"
        e["source"] = "wortando"
        out.append(e)
    return out


def principal():
    sys.stdout.reconfigure(encoding="utf-8")
    cat = lire(os.path.join(CARTES, "domaines.json"))["domaines"]
    domaines = OrderedDict((d["id"], d) for d in cat)
    svg_es = {t["id"]: t["svg"] for t in lire(os.path.join(JAPONAIS, "..", "espanol", "datos", "temas.json"))["themes"]}

    phrases = {}
    fiches = OrderedDict()
    for jlpt in NIVEAUX:
        fiches[jlpt] = lire(os.path.join(CARTES, "mots-%s.json" % jlpt.lower()))["entrees"]
        for p in lire(os.path.join(CARTES, "phrases-%s.json" % jlpt.lower()))["entrees"]:
            phrases[p["id"]] = p

    en_attente, sans_domaine = Counter(), Counter()
    retenues = OrderedDict()
    for jlpt, l in fiches.items():
        retenues[jlpt] = []
        for f in l:
            if not f["gloses"]["fr"]["affichee"]["v"]:
                en_attente[jlpt] += 1          # pas encore jugé : pas de carte
                continue
            if not f.get("domaine"):
                sans_domaine[jlpt] += 1
            retenues[jlpt].append(f)

    # Les thèmes : un par domaine et par niveau ; les petits rejoignent « mots_utiles ».
    noms_par = defaultdict(list)
    for jlpt, l in retenues.items():
        for f in l:
            if nature(f) == "nom":
                noms_par[(jlpt, f.get("domaine") or "mots_utiles")].append(f)
    for (jlpt, dom), l in list(noms_par.items()):
        if dom != "mots_utiles" and len(l) < TAILLE_MIN_THEME:
            noms_par[(jlpt, "mots_utiles")].extend(l)
            del noms_par[(jlpt, dom)]

    theme_de = {}
    themes = []
    for jlpt, cecr in NIVEAUX.items():
        for dom in domaines:
            l = noms_par.get((jlpt, dom))
            if not l:
                continue
            parts = [l[i:i + TAILLE_MAX_THEME] for i in range(0, len(l), TAILLE_MAX_THEME)]
            # Parts de taille égale plutôt qu'un reste minuscule.
            if len(parts) > 1:
                n = -(-len(l) // len(parts))
                parts = [l[i:i + n] for i in range(0, len(l), n)]
            for i, part in enumerate(parts):
                d = domaines[dom]
                suffixe = "" if len(parts) == 1 else " (%d)" % (i + 1)
                tid = "%s%s_%s" % (dom, "" if len(parts) == 1 else "_%d" % (i + 1), cecr.lower())
                for f in part:
                    theme_de[f["id"]] = tid
                themes.append(OrderedDict([
                    ("id", tid),
                    ("nom_theme", d["en"] + suffixe),
                    ("nom_theme_ja", d["ja"] + suffixe),
                    ("nom_theme_fr", d["fr"] + suffixe),
                    ("niveau", cecr),
                    ("jlpt", jlpt),
                    ("svg", svg_es.get(d["svg"], "")),
                    ("mots", part),   # remplacés par les entrées plus bas
                ]))

    def domaine_theme(f):
        if f["id"] in theme_de:
            return theme_de[f["id"]]
        dom = f.get("domaine") or "mots_utiles"
        return "%s_%s" % (dom, NIVEAUX[f["niveau"]].lower())

    for t in themes:
        t["mots"] = [entree(f, phrases, domaine_theme) for f in t["mots"]]

    par_nature = {n: OrderedDict((c, []) for c in NIVEAUX.values())
                  for n in ("verbe", "adjectif", "adverbe", "expression", "fonctionnel")}
    a_conjuguer = []
    for jlpt, l in retenues.items():
        for f in l:
            n = nature(f)
            if n == "nom":
                continue
            e = entree(f, phrases, domaine_theme)
            if n == "verbe" or (n == "adjectif" and f["classe"]["v"] in ("adj-i", "adj-ix", "adj-na")):
                a_conjuguer.append((e, f))
            if n == "adjectif":
                c = f["classe"]["v"]
                e["type"] = {"adj-i": "i", "adj-ix": "i", "adj-na": "na"}.get(c, c.replace("adj-", ""))
            if n == "fonctionnel":
                c = f["classe"]["v"]
                e["kategorie"] = "démonstratif" if c == "adj-pn" else FONCTIONNELS[c]
            if n == "adverbe":
                e["kategorie"] = "onomatopée" if f["classe"]["v"] == "adv-to" else "adverbe"
            if n == "expression":
                e["kategorie"] = "interjection" if f["classe"]["v"] == "int" else "expression"
            par_nature[n][NIVEAUX[jlpt]].append(e)

    romaji = romaji_de()
    # だけ, など… sont déjà dans les listes JLPT : la carte écrite à la main ne
    # s'ajoute que si la liste n'a pas ce mot à un niveau aussi facile (と n'y est
    # qu'au N1, au sens de « si » : la particule と du N5 garde sa carte).
    rang = {c: i for i, c in enumerate(NIVEAUX.values())}
    deja = {}
    for n in par_nature.values():
        for c, l in n.items():
            for e in l:
                deja[e["mot"]] = min(deja.get(e["mot"], 9), rang[c])
    for nat, args in (("fonctionnel", ("particules.json", "particules", "particules.json", "particules-candidates.json")),
                      ("expression", ("expressions.json", "expressions", "expressions.json", "expressions-candidates.json"))):
        for e in ajouts(*args, romaji):
            if deja.get(e["mot"], 9) > rang[NIVEAUX[e["jlpt"]]]:
                par_nature[nat][NIVEAUX[e["jlpt"]]].append(e)

    non_conjugues = []
    for (e, f), r in zip(a_conjuguer, conjuguer([f for _, f in a_conjuguer])):
        if r["formes"]:
            e["formes"] = r["formes"]
        else:
            non_conjugues.append("%s %s (%s) : %s" % (e["mot"], e["lecture"], e["classe"], r["erreur"]))

    ecrire("themes.json", OrderedDict([("themes", themes)]))
    ecrire("verbes.json", par_nature["verbe"])
    ecrire("adjectifs.json", par_nature["adjectif"])
    ecrire("adverbes.json", par_nature["adverbe"])
    ecrire("expressions.json", par_nature["expression"])
    ecrire("fonctionnels.json", par_nature["fonctionnel"])

    print("Niveau | noms (thèmes) | verbes | adjectifs | adverbes | expressions | mots-outils | en attente")
    for jlpt, cecr in NIVEAUX.items():
        t = [x for x in themes if x["niveau"] == cecr]
        print("%s %s | %d (%d) | %d | %d | %d | %d | %d | %d" % (
            jlpt, cecr, sum(len(x["mots"]) for x in t), len(t),
            *(len(par_nature[n][cecr]) for n in ("verbe", "adjectif", "adverbe", "expression", "fonctionnel")),
            en_attente[jlpt]))
    sans_ex = sum(1 for t in themes for m in t["mots"] if "exemple" not in m) + sum(
        1 for n in par_nature.values() for l in n.values() for m in l if "exemple" not in m)
    print("Sans exemple :", sans_ex, "| sans domaine :", dict(sans_domaine) or 0,
          "| non conjugués :", len(non_conjugues))
    for x in non_conjugues[:15]:
        print("  -", x)


if __name__ == "__main__":
    principal()
