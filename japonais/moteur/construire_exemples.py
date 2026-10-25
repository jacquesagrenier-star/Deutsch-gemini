# -*- coding: utf-8 -*-
"""Fabrique les trois exemples du modele de donnees A PARTIR DES BRANCHES.

Rien n'est tape a la main dans exemples/*.json : chaque valeur vient d'un
fichier reel d'une branche japonais-*, lu par `git show`, et chaque champ
porte d'ou il vient. Ce qui manque dans les donnees reste vide et le dit
(statut "manquant") -- c'est le but : montrer ce que le format exige et ce
que les donnees actuelles fournissent vraiment.

    git fetch origin japonais-donnees japonais-kanji-mnemo japonais-conjugaison
    python japonais/moteur/construire_exemples.py

Ecrit japonais/moteur/exemples/{mot-mizu,verbe-taberu,kanji-mizu}.json.
Si node est present, fait aussi conjuguer 食べる par le moteur de la branche
japonais-conjugaison, pour prouver que la classe suffit (les formes ne sont
PAS stockees).
Bibliotheque standard seulement.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "exemples")

B_DONNEES = "origin/japonais-donnees"
B_MNEMO = "origin/japonais-kanji-mnemo"
B_CONJ = "origin/japonais-conjugaison"


def show(branche, chemin):
    return subprocess.run(["git", "show", "%s:%s" % (branche, chemin)],
                          capture_output=True, check=True, cwd=ICI).stdout.decode("utf-8")


def charger(branche, chemin):
    return json.loads(show(branche, chemin))


# Les sources, declarees UNE fois par fichier. Chaque champ n'en porte que la cle.
SOURCES = {
    "tanos": {"nom": "Listes JLPT de Jonathan Waller (tanos.co.uk)", "licence": "CC BY",
              "fichier": "japonais/mots.json @ japonais-donnees"},
    "kanjidic2": {"nom": "KANJIDIC2 (EDRDG) 2025-310", "licence": "CC BY-SA 4.0",
                  "fichier": "japonais/kanji.json @ japonais-donnees"},
    "jmdict": {"nom": "JMdict (EDRDG)", "licence": "CC BY-SA 4.0",
               "fichier": "japonais/conjugaison/oracles/jmdict-courants.json @ japonais-conjugaison (copie 2021)"},
    "kanjivg": {"nom": "KanjiVG (Ulrich Apel)", "licence": "CC BY-SA 3.0",
                "fichier": "japonais/kanji/composants.json @ japonais-kanji-mnemo"},
    "wortando": {"nom": "Texte original Wortando", "licence": "a choisir par le proprietaire",
                 "fichier": "japonais/kanji/mnemoniques_n5.json @ japonais-kanji-mnemo"},
    "calcul": {"nom": "Calcule par un script a partir des champs voisins", "licence": "-",
               "fichier": "japonais/kanji/construire.py @ japonais-kanji-mnemo"},
}


def champ(valeur, source, statut="brouillon"):
    """Un champ = sa valeur + d'ou il vient + ou en est sa relecture."""
    return {"v": valeur, "src": source, "statut": statut}


def manquant(pourquoi):
    return {"v": None, "src": None, "statut": "manquant", "note": pourquoi}


def furigana_simple(kanji, kana):
    """Decoupe K...K + okurigana. Suffit pour les exemples ; le vrai alignement
    est celui de japonais/kanji/construire.py (mots_n5_non_alignes)."""
    i = len(kanji)
    while i > 0 and "぀" <= kanji[i - 1] <= "ヿ":
        i -= 1
    tete, queue = kanji[:i], kanji[i:]
    if queue and not kana.endswith(queue):
        return None
    lecture = kana[:len(kana) - len(queue)] if queue else kana
    segs = [[tete, lecture]]
    if queue:
        segs.append([queue, None])
    return segs


def trouver(mots, kanji, kana):
    for niv, liste in mots["niveaux"].items():
        for m in liste:
            if m["kanji"] == kanji and m["kana"] == kana:
                return m
    raise KeyError(kanji)


def mot(m, classe, mnemo_par_kanji, kanji_json):
    kanji_du_mot = [c for c in m["kanji"] if "一" <= c <= "鿿"]
    romaji = None
    for k in kanji_du_mot:
        for ex in (mnemo_par_kanji.get(k) or {}).get("exemples", []):
            if ex["mot"] == m["kanji"] and ex["kana"] == m["kana"]:
                romaji = ex.get("romaji")
    seq = m["appariement"]["jmdict_seq_tanos"]
    sens_kanji_fr = (kanji_json.get(kanji_du_mot[0]) or {}).get("sens_fr") if len(kanji_du_mot) == 1 else None
    return {
        "id": "jmdict:" + seq,
        "type": "mot",
        "niveau": m["niveau"],
        "ecritures": {
            "kanji": champ(m["kanji"], "tanos"),
            "kana": champ(m["kana"], "tanos"),
            "romaji": champ(romaji, "calcul") if romaji else manquant("calculable, jamais stocke a la main"),
        },
        "furigana": champ(furigana_simple(m["kanji"], m["kana"]), "calcul"),
        "classe": champ(classe, "jmdict") if classe else manquant("JMdict pas encore apparie"),
        "flexion": {"moteur": "conjugaison", "classe_cle": "classe"} if classe and classe.startswith(("v", "adj")) else None,
        "gloses": {
            "fr": {
                "affichee": manquant("mots.json n'a aucune glose francaise (JMdict absent au build)"),
                "autres": [],
                # Une piste, pas une glose : le sens du KANJI n'est pas celui du mot.
                "pistes": [champ(s, "kanjidic2") for s in (sens_kanji_fr or [])],
            },
            "en": {
                "affichee": champ(m["tanos"]["champs"]["waller_definition"], "tanos"),
                "autres": [],
            },
        },
        "kanji": kanji_du_mot,
        "phrases": [],
        "image": None,
        "provenance": {"tanos": "%s:%d" % (m["tanos"]["fichier"], m["tanos"]["ligne"]),
                       "jmdict_seq_non_verifie": seq},
    }


def kanji_entree(k, kj, mn):
    return {
        "id": "kanji:" + k,
        "type": "kanji",
        "niveau": kj["niveau"],
        "caractere": k,
        "traits": champ(kj["traits"][0], "kanjidic2", "source"),
        "trace": {"svg": "kanji/traits/%05x.svg" % ord(k), "src": "kanjivg",
                  "statut": "a_extraire", "note": "pas encore extrait pour les kanji (fait pour les kana)"},
        "lectures": {
            "on": champ(kj["lectures_on"], "kanjidic2", "source"),
            "kun": champ(kj["lectures_kun"], "kanjidic2", "source"),
            "retenue": champ({"type": mn["lecture"]["type"], "kana": mn["lecture"]["kana"],
                              "romaji": mn["lecture"]["romaji"]}, "calcul"),
        },
        "sens": {
            "fr": {"affichee": champ(mn["sens_fr"], "kanjidic2"),
                   "autres": [x for x in kj["sens_fr"] if x != mn["sens_fr"]]},
            "en": {"affichee": champ(mn["sens_en"], "kanjidic2"),
                   "autres": [x for x in kj["sens_en"] if x != mn["sens_en"]]},
        },
        "composants": [c["element"] for c in mn["composants"]] or [k],
        # Les mnemotechniques ne se traduisent pas : une entree par langue
        # d'apprenant, chacune avec sa propre relecture et sa propre note.
        "mnemo": {
            "fr": dict(champ(mn["mnemo_fr"], "wortando"),
                       confiance=mn["confiance"], pourquoi=mn["confiance_pourquoi"],
                       image_mene_au_sens=None),
            "en": dict(champ(mn["mnemo_en"], "wortando"),
                       confiance=None, image_mene_au_sens=None),
        },
        "mots": [],   # rempli par l'index inverse calcule au build, voir CONCEPTION.md 2.4
        "frequence": champ(kj["frequence"], "kanjidic2", "source"),
    }


def conjuguer_par_node(kanji, kana, classe):
    if not shutil.which("node"):
        return None
    d = tempfile.mkdtemp()
    try:
        with open(os.path.join(d, "conjugaison.js"), "w", encoding="utf-8") as f:
            f.write(show(B_CONJ, "japonais/conjugaison/conjugaison.js"))
        code = ("const C=require(%r);const r=C.conjuguer(%r,%r,%r);"
                "const o={};['masu','te','ta','nai','potentiel'].forEach(k=>o[k]=r.formes[k]);"
                "console.log(JSON.stringify(o));") % (os.path.join(d, "conjugaison.js"), kanji, kana, classe)
        out = subprocess.run(["node", "-e", code], capture_output=True, check=True).stdout.decode()
        return json.loads(out)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main():
    mots = charger(B_DONNEES, "japonais/mots.json")
    kanji_json = {e["kanji"]: e for liste in charger(B_DONNEES, "japonais/kanji.json")["niveaux"].values() for e in liste}
    mnemo = {e["kanji"]: e for e in charger(B_MNEMO, "japonais/kanji/mnemoniques_n5.json")["kanji"]}
    classes = {(k, r): c for k, r, c in charger(B_CONJ, "japonais/conjugaison/oracles/jmdict-courants.json")}

    os.makedirs(SORTIE, exist_ok=True)
    m_mizu = trouver(mots, "水", "みず")
    m_tab = trouver(mots, "食べる", "たべる")
    sorties = {
        "mot-mizu.json": {"sources": SOURCES, "entree": mot(m_mizu, classes.get(("水", "みず")), mnemo, kanji_json)},
        "verbe-taberu.json": {"sources": SOURCES, "entree": mot(m_tab, classes.get(("食べる", "たべる")), mnemo, kanji_json)},
        "kanji-mizu.json": {"sources": SOURCES, "entree": kanji_entree("水", kanji_json["水"], mnemo["水"])},
    }
    # L'index inverse kanji -> mots, tel que le build le calculerait.
    sorties["kanji-mizu.json"]["entree"]["mots"] = sorted(
        "jmdict:" + m["appariement"]["jmdict_seq_tanos"]
        for m in mots["niveaux"]["N5"] if m["kanji"] and "水" in m["kanji"])

    formes = conjuguer_par_node("食べる", "たべる", sorties["verbe-taberu.json"]["entree"]["classe"]["v"])
    if formes:
        sorties["verbe-taberu.json"]["_formes_calculees_a_l_execution_non_stockees"] = formes

    for nom, contenu in sorties.items():
        with open(os.path.join(SORTIE, nom), "w", encoding="utf-8", newline="\n") as f:
            json.dump(contenu, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("ecrit", os.path.join("japonais/moteur/exemples", nom))
    if formes:
        print("食べる conjugue par japonais-conjugaison :", json.dumps(formes, ensure_ascii=False))


if __name__ == "__main__":
    main()
