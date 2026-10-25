"""Extrait allégé des sources japonaises N5-N3, pour une session cloud.

Le cloud ne peut pas télécharger JMdict (réseau bloqué, voir japonais/RAPPORT.md
sur la branche japonais-donnees). Ce script lit les résultats calculés sur le PC
et n'en garde que ce qu'il faut pour fabriquer les cartes :

  ~/.wortando/japonais-donnees/japonais/mots.json         (Tanos + JMdict, 50 Mo)
  ~/.wortando/japonais-phrases/japonais/phrases/phrases.json (Tatoeba, 6 Mo)

  -> japonais/cartes/sources/mots-n5-n3.json

Usage : python japonais/cartes/outils/extraire_sources.py
"""
import json
import sys
from pathlib import Path

NIVEAUX = ["N5", "N4", "N3"]
ACCUEIL = Path.home() / ".wortando"
MOTS = ACCUEIL / "japonais-donnees/japonais/mots.json"
PHRASES = ACCUEIL / "japonais-phrases/japonais/phrases/phrases.json"
SORTIE = Path(__file__).resolve().parents[1] / "sources/mots-n5-n3.json"

CHAMPS_PHRASE = ["japonais", "francais", "anglais", "francais_direct", "ids_tatoeba",
                 "auteurs", "longueur", "niveau_mot_le_plus_difficile",
                 "mots_hors_liste", "niveau_respecte", "longueur_dans_la_cible",
                 "appariement"]


def sens_compacts(jm):
    """Les sens anglais gardent leur ordre JMdict (du plus courant au plus rare).
    Les gloses françaises, elles, ne sont PAS alignées sur ces sens : JMdict les
    livre comme des sens à part, en vrac. On les rassemble donc à part."""
    en, fr = [], []
    for s in jm.get("sens") or []:
        if s.get("en"):
            d = {"en": s["en"], "pos": s.get("partOfSpeech") or []}
            for k in ("misc", "info", "field"):
                if s.get(k):
                    d[k] = s[k]
            en.append(d)
        if s.get("fr"):
            fr.append(s["fr"])
    return en, fr


def main():
    mots = json.loads(MOTS.read_text(encoding="utf-8"))
    phrases = json.loads(PHRASES.read_text(encoding="utf-8"))

    par_cle = {}
    for p in phrases["mots"]:
        par_cle.setdefault((p["niveau"], p["mot"], p["lecture"]), p)

    entrees, sans_jmdict, sans_fr, sans_phrase = [], 0, 0, 0
    for niv in NIVEAUX:
        for m in mots["niveaux"][niv]:
            jm = m.get("jmdict") or {}
            en, fr = sens_compacts(jm) if jm else ([], [])
            p = par_cle.get((niv, m["kanji"] or m["kana"], m["kana"])) \
                or par_cle.get((niv, m["kanji"], m["kana"])) \
                or par_cle.get((niv, m["kana"], m["kana"]))
            cands = [{k: c.get(k) for k in CHAMPS_PHRASE} for c in (p or {}).get("candidates", [])]
            e = {
                "niveau": niv,
                "kanji": m["kanji"] or None,
                "kana": m["kana"],
                "waller_en": m["tanos"]["champs"].get("waller_definition"),
                "jmdict_id": jm.get("id") or m["tanos"]["champs"].get("jmdict_seq") or None,
                "jmdict_formes_kanji": [f["text"] + ("" if f.get("common") else " (rare)")
                                        for f in jm.get("formes_kanji") or []],
                "jmdict_formes_kana": [f["text"] for f in jm.get("formes_kana") or []],
                "sens_en": en,
                "gloses_fr_en_vrac": fr,
                "phrases_candidates": cands,
                "phrases_trouvees": (p or {}).get("phrases_trouvees"),
            }
            sans_jmdict += not jm
            sans_fr += not fr
            sans_phrase += not cands
            entrees.append(e)

    sortie = {
        "meta": {
            "extrait_par": "japonais/cartes/outils/extraire_sources.py",
            "niveaux": NIVEAUX,
            "sources": {
                "tanos": "Listes JLPT de Jonathan Waller (CC BY), copie stephenmk/yomitan-jlpt-vocab",
                "jmdict": "JMdict (EDRDG, CC BY-SA 4.0), jmdict-simplified 3.6.2+20260928191014",
                "tatoeba": "Tatoeba (CC BY 2.0 FR) : citer l'auteur de chaque phrase",
            },
            "avertissements": [
                "gloses_fr_en_vrac : NON alignées sur les sens anglais, souvent par ordre alphabétique ; la traduction à afficher est à CHOISIR.",
                "phrases : corpus Tanaka (étudiants), ~80 % justes ; appariement 'sous-chaîne' = à rejeter.",
                "Tanos ne garde parfois qu'une graphie rare (ex. 明い) : la forme courante est dans jmdict_formes_kanji.",
            ],
            "comptes": {"entrees": len(entrees), "sans_jmdict": sans_jmdict,
                        "sans_glose_fr": sans_fr, "sans_phrase": sans_phrase},
        },
        "entrees": entrees,
    }
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(json.dumps(sortie, ensure_ascii=False, indent=0), encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print(SORTIE, f"{SORTIE.stat().st_size / 1e6:.1f} Mo")
    print(json.dumps(sortie["meta"]["comptes"], ensure_ascii=False))


if __name__ == "__main__":
    main()
