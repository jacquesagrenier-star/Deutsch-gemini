# -*- coding: utf-8 -*-
"""Le corpus allemand en espagnol : decouper en lots, controler, poser.

    python interface-es/outils/corpus_lots.py decouper <fichier.json> <niveau> [taille]
    python interface-es/outils/corpus_lots.py controle <lot.es.json> [...]
    python interface-es/outils/corpus_lots.py pose <lot.es.json> [...]
    python interface-es/outils/corpus_lots.py etat

La numerotation et la pose sont celles de tests/corpus_langue.py (un numero par
carte, le mot allemand en tete de chaque ligne, aller-retour a l'octet pres,
relecture apres ecriture). Ce module n'ajoute que :
  - des SOURCES lisibles pour les traducteurs (interface-es/sources/corpus-*.json),
    avec le theme, le francais, l'anglais, les phrases allemandes et leurs
    traductions, et des PISTES tirees de notre corpus d'espagnol APPRIS
    (espanol/datos/ : 4 068 entrees portent leur traduction allemande) ;
  - un CONTROLE sans ecriture, plus severe que la pose : vosotros, francais
    oublie, anglais recopie, nom sans article, doublons dans un meme theme.

⚠️ verbe.json et themes.json ont des cles `praesens.er_sie_es` (le pronom
allemand) : on ne cherche jamais les champs espagnols par le suffixe `_es`
seul ; on ne lit que les champs nommes par corpus_langue.champs().
"""
import collections
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "tests"))
import corpus_langue as C  # noqa: E402

LANG = "es"
SOURCES = os.path.join(ICI, "sources")
ARTICLES = ("el ", "la ", "los ", "las ", "el/la ", "un ", "una ")
VOSOTROS = re.compile(r"(?<![\w])(vosotros|vosotras|vuestro|vuestra|vuestros|vuestras|os|sois|estáis|habéis|tenéis|"
                      r"\w+áis|\w+éis|\w+ísteis|\w+asteis)(?![\w])", re.I)
# Des mots justes qui finissent comme une forme de vosotros (-éis, -áis).
PAS_VOSOTROS = {"dieciséis", "veintiséis"}


def vosotros(texte):
    """La premiere forme de vosotros du texte, ou None."""
    for m in VOSOTROS.finditer(texte):
        if m.group(0).lower() not in PAS_VOSOTROS:
            return m.group(0)
    return None


FRANCAIS = re.compile(r"(?<![\w'’])(je|tu es|nous|vous|avec|pour|dans|est|sont|chez|très|aussi|mais|déjà|leur|cette|ces)(?![\w'’])", re.I)
LETTRES_FR = re.compile(r"[çèêëàâîïôûùœ]")


def norm_de(s):
    s = (s or "").strip()
    s = re.sub(r"^(der|die|das|sich)\s+", "", s, flags=re.I)
    s = re.sub(r"\s*\(.*?\)\s*", " ", s)
    return s.strip().lower()


def pistes_espagnol():
    """{allemand normalise: [« la casa », ...]} depuis l'espagnol appris."""
    out = collections.defaultdict(list)
    for chemin in glob.glob(os.path.join(RACINE, "espanol", "datos", "*.json")):
        try:
            d = json.load(io.open(chemin, encoding="utf-8"))
        except Exception:
            continue
        def visiter(o):
            if isinstance(o, dict):
                de = o.get("traduction_de")
                mot = o.get("mot") or o.get("infinitif")
                if isinstance(de, str) and isinstance(mot, str) and de.strip():
                    es = ((o.get("genre") + " ") if isinstance(o.get("genre"), str) and o.get("genre") else "") + mot
                    for morceau in re.split(r"[,;/]", de):
                        k = norm_de(morceau)
                        if k and es not in out[k]:
                            out[k].append(es)
                for v in o.values():
                    visiter(v)
            elif isinstance(o, list):
                for v in o:
                    visiter(v)
        visiter(d)
    return out


def decouper(nom, niveau, taille=250):
    d, _ = C.charger(nom)
    pistes = pistes_espagnol()
    entrees = []
    for i, (niv, ctx, m) in enumerate(C.cases(nom, d)):
        if niveau != "*" and niv != niveau:
            continue
        if not C.manque(m, LANG):
            continue
        e = {"n": i, "mot": C.cle(m), "niveau": niv}
        if m.get("genre"):
            e["genre"] = m["genre"]
        if m.get("pluriel"):
            e["pluriel"] = m["pluriel"]
        if ctx:
            e["contexte"] = ctx
        e["fr"] = m.get("traduction", "")
        e["en"] = m.get("traduction_en", "")
        e["champs"] = C.champs(m)
        for c in e["champs"][1:]:
            if c == "kategorie":
                e["kategorie"] = [m.get("kategorie", ""), m.get("kategorie_fr", "") or m.get("kategorie_en", "")]
            else:
                e[c] = [m.get(c, ""), m.get(c + "_fr", ""), m.get(c + "_en", "")]
        p = pistes.get(norm_de(C.cle(m)))
        if p:
            e["pistes"] = p[:4]
        entrees.append(e)
    os.makedirs(SOURCES, exist_ok=True)
    base = os.path.splitext(nom)[0]
    k = 0
    for k, deb in enumerate(range(0, len(entrees), taille), 1):
        chemin = os.path.join(SOURCES, "corpus-%s-%s-%02d.json" % (base, niveau, k))
        io.open(chemin, "w", encoding="utf-8").write(
            json.dumps({"fichier": nom, "entrees": entrees[deb:deb + taille]}, ensure_ascii=False, indent=1) + "\n")
        print("%s : %d cartes" % (os.path.relpath(chemin, RACINE), len(entrees[deb:deb + taille])))
    if not entrees:
        print("%s %s : rien a traduire" % (nom, niveau))


def controle(chemin, silencieux=False):
    lot = json.load(io.open(chemin, encoding="utf-8"))
    nom = lot["fichier"]
    d, _ = C.charger(nom)
    toutes = C.cases(nom, d)
    fautes, avis = [], []
    par_ctx = collections.defaultdict(list)
    for num, vals in lot["e"].items():
        i = int(num)
        if i >= len(toutes):
            fautes.append("#%s hors du fichier" % num)
            continue
        niv, ctx, m = toutes[i]
        if vals[0] != C.cle(m):
            fautes.append("#%s : le lot dit %r, le fichier %r" % (num, vals[0], C.cle(m)))
            continue
        cs = C.champs(m)
        if len(vals) - 1 != len(cs):
            fautes.append("#%s %s : %d valeurs pour %s" % (num, vals[0], len(vals) - 1, cs))
            continue
        for c, v in zip(cs, vals[1:]):
            v = (v or "").strip()
            if not v:
                if c == "exemple" and not (m.get("exemple") or "").strip():
                    continue
                fautes.append("#%s %s : %s vide" % (num, vals[0], c))
                continue
            vo = vosotros(v)
            if vo:
                fautes.append("#%s %s : %s -- vosotros ou forme d'Espagne (%r)" % (num, vals[0], c, vo))
            if LETTRES_FR.search(v) or FRANCAIS.search(v):
                avis.append("#%s %s : %s -- du francais ? %r" % (num, vals[0], c, v[:70]))
            src_en = m.get(c + "_en", "") if c != "traduction" else m.get("traduction_en", "")
            if src_en and v == src_en and len(v) > 4:
                avis.append("#%s %s : %s -- identique a l'anglais %r" % (num, vals[0], c, v[:60]))
            src_fr = m.get("traduction", "") if c == "traduction" else m.get(c + "_fr", "")
            if src_fr and v == src_fr and len(v) > 4:
                avis.append("#%s %s : %s -- identique au francais %r" % (num, vals[0], c, v[:60]))
        trad = (vals[1] or "").strip()
        if m.get("genre") and "infinitif" not in m and not trad.lower().startswith(ARTICLES):
            avis.append("#%s %s : nom sans article espagnol (%r)" % (num, vals[0], trad))
        par_ctx[(niv, ctx, nom)].append((trad.lower(), vals[0]))
    for k, lst in par_ctx.items():
        vus = collections.defaultdict(list)
        for t, mot in lst:
            vus[t].append(mot)
        for t, mots in vus.items():
            if len(set(mots)) > 1:
                avis.append("meme traduction %r pour %s (%s %s)" % (t, ", ".join(sorted(set(mots))), k[0], k[1]))
    if not silencieux:
        print("%s : %d cartes, %d fautes, %d avis" % (os.path.relpath(chemin, RACINE), len(lot["e"]), len(fautes), len(avis)))
        for f in fautes:
            print("  FAUTE " + f)
        for a in avis:
            print("  avis  " + a)
    return fautes, avis


def pose(chemin):
    fautes, _ = controle(chemin, silencieux=True)
    if fautes:
        sys.exit("ARRET, %s a %d fautes : lancer « controle »" % (chemin, len(fautes)))
    C.pose(LANG, chemin)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "etat":
        C.etat(LANG)
    elif a[0] == "decouper":
        decouper(a[1], a[2], int(a[3]) if len(a) > 3 else 250)
    elif a[0] == "controle":
        total = 0
        for c in a[1:]:
            total += len(controle(c)[0])
        sys.exit(1 if total else 0)
    elif a[0] == "pose":
        for c in a[1:]:
            pose(c)
    else:
        sys.exit(__doc__)
