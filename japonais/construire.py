#!/usr/bin/env python3
"""Assemble les données brutes du vocabulaire JLPT (N5 à N1) et des kanji JLPT.

Bibliothèque standard seulement. Relançable de bout en bout :

    python japonais/construire.py                 # télécharge ce qui manque, puis construit
    python japonais/construire.py --jmdict CHEMIN # utilise un JMdict déjà téléchargé
    python japonais/construire.py --rafraichir    # retélécharge toutes les sources

Produit, à côté de ce script : mots.json, kanji.json, et imprime les chiffres
repris dans RAPPORT.md. Les archives brutes vont dans japonais/sources/ (ignoré par git).

Sources (versions constatées le 4 octobre 2026, lors de la première construction)
--------------------------------------------------------------------------------
1. Listes de vocabulaire JLPT de Jonathan Waller (« Tanos »), CC BY.
   Le site d'origine (https://www.tanos.co.uk/jlpt/) était injoignable depuis
   l'environnement de construction. On lit donc la copie versionnée dans git des
   listes d'origine, faite par stephenmk, qui garde l'orthographe de Waller et
   ajoute un identifiant JMdict :
   https://github.com/stephenmk/yomitan-jlpt-vocab , dossier original_data/,
   commit b062d4e38c4bdd0950ae1d4ec55f04b176182e03 (26 août 2025).
2. Niveaux JLPT des kanji, liste de Waller (Tanos), CC BY, relevés sur le site
   Tanos par le script tools/jlpt.py de https://github.com/davidluzgouveia/kanji-data
   (champ « jlpt_new » de kanji.json), commit 00fd7079c3890f430759536f91aa5e854ec0ca4f
   (27 février 2026). Seul le niveau est repris de ce fichier.
3. KANJIDIC2 (EDRDG, CC BY-SA 4.0), https://www.edrdg.org/kanjidic/kanjidic2.xml.gz .
   edrdg.org était injoignable : on retombe sur le même fichier, non modifié, livré
   dans les sources du paquet Ubuntu « kanjidic » 2025.11.06 (le script Debian
   debian/download le télécharge tel quel depuis edrdg.org).
   Version obtenue : database_version 2025-310, date_of_creation 2025-11-06.
4. JMdict multilingue (EDRDG, CC BY-SA 4.0). Ordre d'essai :
   a) jmdict-simplified, fichier « jmdict-all » de la dernière release
      (https://github.com/scriptin/jmdict-simplified/releases) ;
   b) XML d'origine http://ftp.edrdg.org/pub/Nihongo/JMdict.gz ;
   c) un fichier local passé par --jmdict (JSON, .json.zip, .json.tgz, XML ou XML.gz).
   Le 4 octobre 2026, a) et b) étaient bloqués par le réseau de l'environnement de
   construction : JMdict n'a PAS pu être lu. La dernière release constatée de
   jmdict-simplified était 3.6.2+20260928191014.
"""

import argparse
import csv
import gzip
import io
import json
import lzma
import random
import re
import sys
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ICI = Path(__file__).resolve().parent
SOURCES = ICI / "sources"
NIVEAUX = ["N5", "N4", "N3", "N2", "N1"]

TANOS_MOTS_COMMIT = "b062d4e38c4bdd0950ae1d4ec55f04b176182e03"
TANOS_MOTS_URL = ("https://raw.githubusercontent.com/stephenmk/yomitan-jlpt-vocab/"
                  + TANOS_MOTS_COMMIT + "/original_data/n{n}.csv")
TANOS_KANJI_COMMIT = "00fd7079c3890f430759536f91aa5e854ec0ca4f"
TANOS_KANJI_URL = ("https://raw.githubusercontent.com/davidluzgouveia/kanji-data/"
                   + TANOS_KANJI_COMMIT + "/kanji.json")
KANJIDIC_URL = "https://www.edrdg.org/kanjidic/kanjidic2.xml.gz"
KANJIDIC_UBUNTU_URL = ("http://archive.ubuntu.com/ubuntu/pool/universe/k/kanjidic/"
                       "kanjidic_2025.11.06.tar.xz")
KANJIDIC_UBUNTU_MEMBRE = "kanjidic-2025.11.06/kanjidic2.xml.gz"
JMDICT_SIMPLIFIED_API = "https://api.github.com/repos/scriptin/jmdict-simplified/releases/latest"
JMDICT_XML_URL = "http://ftp.edrdg.org/pub/Nihongo/JMdict.gz"

# Ordres de grandeur annoncés dans la commande de cette tâche, pour signaler les écarts.
ATTENDU_MOTS = {"N5": 743, "N4": 684, "N3": 1621, "N2": 1910, "N1": 3087}
ATTENDU_KANJI = {"N5": 103, "N4": 181, "N3": 341, "N2": 400, "N1": 1187}

journal = []  # ce qui s'est passé pour chaque source, repris dans meta


def note(msg):
    journal.append(msg)
    print("  " + msg)


def telecharger(url, dest, rafraichir):
    if dest.exists() and not rafraichir:
        note(f"déjà présent : {dest.name}")
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": "wortando-japonais/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        donnees = r.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(donnees)
    note(f"téléchargé : {url} ({len(donnees)} octets)")
    return dest


def essayer(url, dest, rafraichir):
    try:
        return telecharger(url, dest, rafraichir)
    except Exception as e:  # réseau, HTTP, proxy : on le dit, on ne remplace pas
        note(f"ÉCHEC : {url} — {type(e).__name__}: {e}")
        return None


# ---------------------------------------------------------------- Tanos

def lire_tanos_mots(rafraichir):
    mots = []
    for niv in NIVEAUX:
        n = niv[1]
        f = essayer(TANOS_MOTS_URL.format(n=n), SOURCES / f"tanos_n{n}.csv", rafraichir)
        if f is None:
            sys.exit("Liste Tanos injoignable : impossible de continuer.")
        texte = f.read_text(encoding="utf-8")
        lignes = texte.splitlines()
        lecteur = csv.reader(io.StringIO(texte))
        entete = next(lecteur)
        # On garde la ligne brute du fichier : on relit ligne par ligne via csv
        # pour retrouver le texte source de chaque enregistrement.
        for numero, champs in enumerate(lecteur, start=2):
            brut = dict(zip(entete, champs))
            mots.append({
                "niveau": niv,
                "kanji": brut["kanji"] or None,
                "kana": brut["kana"],
                "tanos": {"fichier": f"original_data/n{n}.csv", "ligne": numero,
                          "texte": lignes[numero - 1], "champs": brut},
            })
    return mots


def lire_tanos_kanji(rafraichir):
    f = essayer(TANOS_KANJI_URL, SOURCES / "kanji-data.json", rafraichir)
    if f is None:
        sys.exit("Niveaux JLPT des kanji injoignables : impossible de continuer.")
    d = json.loads(f.read_text(encoding="utf-8"))
    return {k: f"N{v['jlpt_new']}" for k, v in d.items() if v.get("jlpt_new")}


# ---------------------------------------------------------------- KANJIDIC2

def obtenir_kanjidic(rafraichir):
    dest = SOURCES / "kanjidic2.xml.gz"
    origine = SOURCES / "kanjidic2.origine.txt"  # d'où vient la copie en cache
    if dest.exists() and origine.exists() and not rafraichir:
        note(f"déjà présent : {dest.name} (origine : {origine.read_text(encoding='utf-8')})")
        return dest, origine.read_text(encoding="utf-8")
    f = essayer(KANJIDIC_URL, dest, True)
    if f:
        origine.write_text(KANJIDIC_URL, encoding="utf-8")
        return f, KANJIDIC_URL
    note("repli : copie non modifiée du paquet source Ubuntu kanjidic 2025.11.06")
    t = essayer(KANJIDIC_UBUNTU_URL, SOURCES / "kanjidic_2025.11.06.tar.xz", rafraichir)
    if t is None:
        return None, None
    with tarfile.open(t, "r:xz") as tar:
        dest.write_bytes(tar.extractfile(KANJIDIC_UBUNTU_MEMBRE).read())
    origine.write_text(KANJIDIC_UBUNTU_URL + " → " + KANJIDIC_UBUNTU_MEMBRE, encoding="utf-8")
    return dest, origine.read_text(encoding="utf-8")


def lire_kanjidic(chemin):
    with gzip.open(chemin, "rb") as g:
        racine = ET.parse(g).getroot()
    entete = racine.find("header")
    version = {e.tag: e.text for e in entete}
    kanji = {}
    for c in racine.iter("character"):
        lit = c.findtext("literal")
        misc = c.find("misc")
        rm = c.find("reading_meaning")
        sens_fr, sens_en, on, kun, nanori = [], [], [], [], []
        if rm is not None:
            for g in rm.iter("rmgroup"):
                for m in g.findall("meaning"):
                    lang = m.get("m_lang", "en")
                    if lang == "fr":
                        sens_fr.append(m.text)
                    elif lang == "en":
                        sens_en.append(m.text)
                for r in g.findall("reading"):
                    if r.get("r_type") == "ja_on":
                        on.append(r.text)
                    elif r.get("r_type") == "ja_kun":
                        kun.append(r.text)
            nanori = [n.text for n in rm.findall("nanori")]
        freq = misc.findtext("freq")
        grade = misc.findtext("grade")
        jlpt = misc.findtext("jlpt")
        kanji[lit] = {
            "sens_fr": sens_fr or None,
            "sens_en": sens_en or None,
            "lectures_on": on,
            "lectures_kun": kun,
            "nanori": nanori,
            # Le premier nombre est le bon ; les suivants sont des erreurs de compte courantes.
            "traits": [int(s.text) for s in misc.findall("stroke_count")],
            "frequence": int(freq) if freq else None,
            "grade": int(grade) if grade else None,
            "jlpt_ancien_kanjidic": int(jlpt) if jlpt else None,
        }
    return version, kanji


# ---------------------------------------------------------------- JMdict

def obtenir_jmdict(local, rafraichir):
    if local:
        p = Path(local)
        note(f"JMdict local : {p}")
        return p, f"fichier local {p.name}"
    try:
        req = urllib.request.Request(JMDICT_SIMPLIFIED_API,
                                     headers={"User-Agent": "wortando-japonais/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            rel = json.load(r)
        actifs = [a for a in rel["assets"]
                  if re.match(r"jmdict-all-[\d.]+.*\.json\.zip$", a["name"])]
        if actifs:
            a = actifs[0]
            f = essayer(a["browser_download_url"], SOURCES / a["name"], rafraichir)
            if f:
                return f, f"jmdict-simplified {rel['tag_name']} ({a['name']})"
        else:
            note("ÉCHEC : aucun fichier jmdict-all dans la dernière release jmdict-simplified")
    except Exception as e:
        note(f"ÉCHEC : {JMDICT_SIMPLIFIED_API} — {type(e).__name__}: {e}")
    f = essayer(JMDICT_XML_URL, SOURCES / "JMdict.gz", rafraichir)
    if f:
        return f, JMDICT_XML_URL
    return None, None


def _ouvrir_json(p):
    nom = p.name.lower()
    if nom.endswith(".zip"):
        with zipfile.ZipFile(p) as z:
            membre = next(n for n in z.namelist() if n.endswith(".json"))
            return json.loads(z.read(membre).decode("utf-8"))
    if nom.endswith((".tgz", ".tar.gz")):
        with tarfile.open(p, "r:gz") as t:
            membre = next(m for m in t.getmembers() if m.name.endswith(".json"))
            return json.loads(t.extractfile(membre).read().decode("utf-8"))
    return json.loads(p.read_text(encoding="utf-8"))


def lire_jmdict(p):
    """Rend (version, entrées) au format commun de mots.json, quelle que soit la source."""
    nom = p.name.lower()
    if ".json" in nom:
        d = _ouvrir_json(p)
        version = {k: d.get(k) for k in ("version", "languages", "dictDate", "dictRevisions")}
        entrees = []
        for w in d["words"]:
            entrees.append({
                "id": w["id"],
                "formes_kanji": w["kanji"],
                "formes_kana": w["kana"],
                "sens": [_sens_simplifie(s) for s in w["sense"]],
            })
        return version, entrees
    return _lire_jmdict_xml(p)


def _sens_simplifie(s):
    fr = [g["text"] for g in s["gloss"] if g["lang"] == "fre"]
    en = [g["text"] for g in s["gloss"] if g["lang"] == "eng"]
    autres = {k: v for k, v in s.items() if k != "gloss"}
    autres["fr"] = fr or None
    autres["en"] = en or None
    autres["types_glose"] = sorted({g["type"] for g in s["gloss"] if g.get("type")})
    return autres


def _lire_jmdict_xml(p):
    ouvrir = gzip.open if p.name.lower().endswith(".gz") else open
    XL = "{http://www.w3.org/XML/1998/namespace}lang"
    entrees = []
    with ouvrir(p, "rb") as f:
        # Les entités (&n; &v5k; …) sont déclarées dans le DTD interne : expat les développe.
        for _, e in ET.iterparse(f, events=("end",)):
            if e.tag != "entry":
                continue
            fk = [{"text": k.findtext("keb"),
                   "common": any(x.text and x.text.startswith(("news1", "ichi1", "spec1", "spec2", "gai1"))
                                 for x in k.findall("ke_pri")),
                   "tags": [x.text for x in k.findall("ke_inf")],
                   "priorite": [x.text for x in k.findall("ke_pri")]} for k in e.findall("k_ele")]
            fr_ = []
            for r in e.findall("r_ele"):
                restr = [x.text for x in r.findall("re_restr")]
                if r.find("re_nokanji") is not None:
                    restr = []
                elif not restr:
                    restr = ["*"]
                fr_.append({"text": r.findtext("reb"),
                            "common": any(x.text and x.text.startswith(("news1", "ichi1", "spec1", "spec2", "gai1"))
                                          for x in r.findall("re_pri")),
                            "tags": [x.text for x in r.findall("re_inf")],
                            "priorite": [x.text for x in r.findall("re_pri")],
                            "appliesToKanji": restr})
            sens = []
            pos_prec = []
            for s in e.findall("sense"):
                pos = [x.text for x in s.findall("pos")] or pos_prec  # le DTD : pos hérité
                pos_prec = pos
                gl = s.findall("gloss")
                fr = [g.text for g in gl if g.get(XL) == "fre"]
                en = [g.text for g in gl if g.get(XL, "eng") == "eng"]
                sens.append({
                    "partOfSpeech": pos,
                    "appliesToKanji": [x.text for x in s.findall("stagk")] or ["*"],
                    "appliesToKana": [x.text for x in s.findall("stagr")] or ["*"],
                    "related": [x.text for x in s.findall("xref")],
                    "antonym": [x.text for x in s.findall("ant")],
                    "field": [x.text for x in s.findall("field")],
                    "dialect": [x.text for x in s.findall("dial")],
                    "misc": [x.text for x in s.findall("misc")],
                    "info": [x.text for x in s.findall("s_inf")],
                    "fr": fr or None,
                    "en": en or None,
                    "types_glose": sorted({g.get("g_type") for g in gl if g.get("g_type")}),
                })
            entrees.append({"id": e.findtext("ent_seq"), "formes_kanji": fk,
                            "formes_kana": fr_, "sens": sens})
            e.clear()
    return {"source": "XML JMdict"}, entrees


# ---------------------------------------------------------------- appariement

def indexer(entrees):
    paires = defaultdict(list)     # (kanji, kana) → entrées
    kana_seul = defaultdict(list)  # kana → entrées
    for e in entrees:
        ks = [k["text"] for k in e["formes_kanji"]]
        for r in e["formes_kana"]:
            kana_seul[r["text"]].append(e)
            cibles = ks if "*" in r.get("appliesToKanji", ["*"]) else r["appliesToKanji"]
            for k in cibles:
                paires[(k, r["text"])].append(e)
    return paires, kana_seul


def _dedoublonner(liste):
    vu, res = set(), []
    for e in liste:
        if e["id"] not in vu:
            vu.add(e["id"])
            res.append(e)
    return res


def apparier(mot, paires, kana_seul):
    """Apparie sur la paire kanji + kana. Pour un mot Tanos sans kanji, sur le kana seul."""
    seq_tanos = mot["tanos"]["champs"].get("jmdict_seq") or None
    if mot["kanji"]:
        cands = _dedoublonner(paires.get((mot["kanji"], mot["kana"]), []))
    else:
        cands = _dedoublonner(kana_seul.get(mot["kana"], []))
    ids = [e["id"] for e in cands]
    if not cands:
        return None, {"statut": "introuvable", "candidats": [], "jmdict_seq_tanos": seq_tanos}
    if len(cands) == 1:
        return cands[0], {"statut": "unique", "candidats": ids, "jmdict_seq_tanos": seq_tanos}
    # Plusieurs entrées possibles : règles dans cet ordre, la première qui tranche gagne.
    raison = None
    choisi = None
    if seq_tanos and seq_tanos in ids:
        choisi = cands[ids.index(seq_tanos)]
        raison = "identifiant JMdict donné par la copie des listes Tanos (stephenmk)"
    elif not mot["kanji"]:
        sans_kanji = [e for e in cands if not e["formes_kanji"]]
        uk = [e for e in cands if any("uk" in s.get("misc", []) for s in e["sens"])]
        if len(sans_kanji) == 1:
            choisi, raison = sans_kanji[0], "seule entrée sans forme kanji"
        elif len(uk) == 1:
            choisi, raison = uk[0], "seule entrée marquée « s'écrit d'ordinaire en kana » (uk)"
    if choisi is None:
        communs = [e for e in cands if any(f.get("common") for f in e["formes_kanji"] + e["formes_kana"])]
        if len(communs) == 1:
            choisi, raison = communs[0], "seule entrée marquée courante (common)"
        else:
            choisi = min(cands, key=lambda e: int(e["id"]))
            raison = "aucun critère ne tranche : plus petit identifiant JMdict"
    return choisi, {"statut": "ambigu", "candidats": ids, "retenu": choisi["id"],
                    "raison": raison, "jmdict_seq_tanos": seq_tanos}


# ---------------------------------------------------------------- principal

def pct(a, b):
    return f"{100 * a / b:.1f} %" if b else "—"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--jmdict", help="fichier JMdict déjà téléchargé (JSON jmdict-simplified ou XML)")
    ap.add_argument("--rafraichir", action="store_true", help="retélécharger toutes les sources")
    ap.add_argument("--graine", type=int, default=20261004, help="graine des exemples au hasard")
    args = ap.parse_args()
    SOURCES.mkdir(exist_ok=True)

    print("Tanos — vocabulaire")
    mots = lire_tanos_mots(args.rafraichir)
    print("Tanos — niveaux des kanji")
    niveaux_kanji = lire_tanos_kanji(args.rafraichir)
    print("KANJIDIC2")
    kd_chemin, kd_origine = obtenir_kanjidic(args.rafraichir)
    kd_version, kd = lire_kanjidic(kd_chemin) if kd_chemin else ({}, {})
    print("JMdict")
    jm_chemin, jm_origine = obtenir_jmdict(args.jmdict, args.rafraichir)
    jm_version, entrees = lire_jmdict(jm_chemin) if jm_chemin else (None, None)

    # --- mots
    stats_app = Counter()
    ambigus, introuvables = [], []
    if entrees is not None:
        paires, kana_seul = indexer(entrees)
        for m in mots:
            e, app = apparier(m, paires, kana_seul)
            m["jmdict"] = e
            m["appariement"] = app
            stats_app[app["statut"]] += 1
            if app["statut"] == "ambigu":
                ambigus.append(m)
            elif app["statut"] == "introuvable":
                introuvables.append(m)
    else:
        for m in mots:
            m["jmdict"] = None
            m["appariement"] = {"statut": "jmdict_indisponible", "candidats": [],
                                "jmdict_seq_tanos": m["tanos"]["champs"].get("jmdict_seq") or None}
        stats_app["jmdict_indisponible"] = len(mots)

    # --- kanji
    kanji = []
    absents_kd = []
    for k, niv in sorted(niveaux_kanji.items(), key=lambda kv: (NIVEAUX.index(kv[1]), kv[0])):
        info = kd.get(k)
        if info is None:
            absents_kd.append(k)
        kanji.append({"kanji": k, "niveau": niv, **(info or {
            "sens_fr": None, "sens_en": None, "lectures_on": None, "lectures_kun": None,
            "nanori": None, "traits": None, "frequence": None, "grade": None,
            "jlpt_ancien_kanjidic": None})})

    meta = {
        "construit_le": date.today().isoformat(),
        "sources": {
            "tanos_mots": TANOS_MOTS_URL.format(n="*"),
            "tanos_kanji": TANOS_KANJI_URL + " (champ jlpt_new)",
            "kanjidic2": kd_origine, "kanjidic2_version": kd_version,
            "jmdict": jm_origine, "jmdict_version": jm_version,
        },
        "journal": journal,
        "licences": "Tanos : CC BY (Jonathan Waller). JMdict et KANJIDIC2 : CC BY-SA 4.0 (EDRDG). Voir LICENCES.md.",
    }
    sortie_mots = {"meta": meta, "niveaux": {n: [m for m in mots if m["niveau"] == n] for n in NIVEAUX}}
    sortie_kanji = {"meta": meta, "niveaux": {n: [k for k in kanji if k["niveau"] == n] for n in NIVEAUX}}
    (ICI / "mots.json").write_text(json.dumps(sortie_mots, ensure_ascii=False, indent=1), encoding="utf-8")
    (ICI / "kanji.json").write_text(json.dumps(sortie_kanji, ensure_ascii=False, indent=1), encoding="utf-8")

    # --- chiffres
    print("\n== Comptes par niveau (lignes Tanos) ==")
    print("niveau | mots | attendu | écart | kanji | attendu | écart")
    for n in NIVEAUX:
        nm = sum(1 for m in mots if m["niveau"] == n)
        nk = sum(1 for k in kanji if k["niveau"] == n)
        print(f"{n} | {nm} | {ATTENDU_MOTS[n]} | {nm - ATTENDU_MOTS[n]:+d} | {nk} | {ATTENDU_KANJI[n]} | {nk - ATTENDU_KANJI[n]:+d}")
    print(f"total | {len(mots)} | {sum(ATTENDU_MOTS.values())} | | {len(kanji)} | {sum(ATTENDU_KANJI.values())} |")
    paires_tot = Counter((m["kanji"], m["kana"]) for m in mots)
    multi = sorted(((p, [m["niveau"] for m in mots if (m["kanji"], m["kana"]) == p])
                   for p, c in paires_tot.items() if c > 1), key=lambda x: (x[0][0] or "", x[0][1]))
    print(f"paires (kanji, kana) distinctes : {len(paires_tot)} ; présentes à plusieurs niveaux : {len(multi)}")
    for p, nivs in multi:
        print(f"  {p[0] or '—'} / {p[1]} : {', '.join(nivs)}")
    print(f"mots sans forme kanji dans Tanos : {sum(1 for m in mots if not m['kanji'])}")
    print(f"lignes Tanos sans identifiant JMdict (colonne stephenmk) : "
          f"{sum(1 for m in mots if not m['tanos']['champs'].get('jmdict_seq'))}")

    print("\n== Appariement Tanos → JMdict ==")
    for s, c in sorted(stats_app.items()):
        print(f"{s} : {c}")
    if entrees is not None:
        print("-- ambigus")
        for m in ambigus:
            a = m["appariement"]
            print(f"  {m['niveau']} {m['kanji'] or '—'} / {m['kana']} : {a['candidats']} → {a['retenu']} ({a['raison']})")
        print("-- introuvables")
        for m in introuvables:
            print(f"  {m['niveau']} {m['kanji'] or '—'} / {m['kana']} (id Tanos {m['appariement']['jmdict_seq_tanos']})")
        desaccord = [m for m in mots if m["jmdict"] and m["appariement"]["jmdict_seq_tanos"]
                     and m["jmdict"]["id"] != m["appariement"]["jmdict_seq_tanos"]]
        print(f"-- retenus différents de l'identifiant donné par stephenmk : {len(desaccord)}")
        for m in desaccord:
            print(f"  {m['niveau']} {m['kanji'] or '—'} / {m['kana']} : {m['jmdict']['id']} ≠ {m['appariement']['jmdict_seq_tanos']}")

    print("\n== Couverture française ==")
    print("niveau | mots | ≥1 glose fr | tous les sens avec fr | sens fr ≥ sens en | kanji | kanji avec sens fr")
    for n in NIVEAUX:
        mn = [m for m in mots if m["niveau"] == n]
        kn = [k for k in kanji if k["niveau"] == n]
        kfr = sum(1 for k in kn if k["sens_fr"])
        if entrees is not None:
            un = sum(1 for m in mn if m["jmdict"] and any(s["fr"] for s in m["jmdict"]["sens"]))
            tous = sum(1 for m in mn if m["jmdict"] and all(s["fr"] for s in m["jmdict"]["sens"]))
            # Dans le JMdict complet, les gloses d'une autre langue forment souvent des sens à part,
            # non alignés sur les sens anglais : « tous les sens » est alors trop strict. On donne
            # aussi cette approximation : au moins autant de sens français que de sens anglais.
            autant = sum(1 for m in mn if m["jmdict"] and
                         sum(1 for s in m["jmdict"]["sens"] if s["fr"]) >= sum(1 for s in m["jmdict"]["sens"] if s["en"]))
            print(f"{n} | {len(mn)} | {un} ({pct(un, len(mn))}) | {tous} ({pct(tous, len(mn))}) | "
                  f"{autant} ({pct(autant, len(mn))}) | {len(kn)} | {kfr} ({pct(kfr, len(kn))})")
        else:
            print(f"{n} | {len(mn)} | non mesuré | non mesuré | non mesuré | {len(kn)} | {kfr} ({pct(kfr, len(kn))})")
    kfr = sum(1 for k in kanji if k["sens_fr"])
    print(f"kanji, total : {kfr} / {len(kanji)} ({pct(kfr, len(kanji))}) ont un sens français")
    if absents_kd:
        print(f"kanji Tanos absents de KANJIDIC2 : {''.join(absents_kd)}")

    rnd = random.Random(args.graine)
    if entrees is not None:
        avec_fr = [m for m in mots if m["jmdict"] and any(s["fr"] for s in m["jmdict"]["sens"])]
        print("\n== Dix gloses françaises de mots, au hasard ==")
        for m in rnd.sample(avec_fr, min(10, len(avec_fr))):
            fr = [g for s in m["jmdict"]["sens"] for g in (s["fr"] or [])]
            en = [g for s in m["jmdict"]["sens"] for g in (s["en"] or [])]
            print(f"  {m['niveau']} {m['kanji'] or ''} 【{m['kana']}】 fr: {' ; '.join(fr)} | en: {' ; '.join(en[:4])}")
    kfr_l = [k for k in kanji if k["sens_fr"]]
    print("\n== Dix sens français de kanji, au hasard ==")
    for k in rnd.sample(kfr_l, min(10, len(kfr_l))):
        print(f"  {k['niveau']} {k['kanji']} fr: {', '.join(k['sens_fr'])} | en: {', '.join(k['sens_en'] or [])}")


if __name__ == "__main__":
    main()
