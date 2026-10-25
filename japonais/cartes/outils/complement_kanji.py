#!/usr/bin/env python3
"""Lectures KANJIDIC2 des kanji de nos mots qui manquent à japonais/kanji.json.

kanji.json (branche japonais-donnees) ne garde que les kanji classés JLPT par
kanji-data : 分, 丈, 誰… n'y sont pas, et leurs mots n'avaient pas de furigana
découpés. Ce script les reprend dans KANJIDIC2 complet, à la même version 2025-310 :

    curl -O http://archive.ubuntu.com/ubuntu/pool/universe/k/kanjidic/kanjidic_2025.11.06.tar.xz
    tar -xJf kanjidic_2025.11.06.tar.xz --wildcards '*kanjidic2.xml.gz'
    python japonais/cartes/outils/complement_kanji.py kanjidic-2025.11.06/kanjidic2.xml.gz

Sortie : sources/kanji-complement.json (KANJIDIC2, EDRDG, CC BY-SA 4.0).
"""
import gzip
import json
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from construire import CARTES, charger_kanji, est_kana  # noqa: E402


def main(chemin):
    connus = charger_kanji(None)
    src = json.load(open(os.path.join(CARTES, "sources", "mots-n5-n3.json"), encoding="utf-8"))
    voulus = set()
    for e in src["entrees"]:
        for f in [e["kanji"] or ""] + [f.split(" (")[0] for f in e["jmdict_formes_kanji"]]:
            voulus.update(c for c in f if not est_kana(c) and c != "々" and c not in connus)
    out = {}
    with gzip.open(chemin) as fh:
        for _, el in ET.iterparse(fh):
            if el.tag != "character":
                continue
            c = el.findtext("literal")
            if c in voulus:
                rm = el.find("reading_meaning")
                on, kun, fr = [], [], []
                if rm is not None:
                    for r in rm.iter("reading"):
                        if r.get("r_type") == "ja_on":
                            on.append(r.text)
                        elif r.get("r_type") == "ja_kun":
                            kun.append(r.text)
                    fr = [m.text for m in rm.iter("meaning") if m.get("m_lang") == "fr"]
                out[c] = {"kanji": c, "lectures_on": on, "lectures_kun": kun, "sens_fr": fr}
            el.clear()
    sortie = {"meta": {"source": "KANJIDIC2 (EDRDG) 2025-310, CC BY-SA 4.0",
                       "role": "lectures des kanji de nos mots absents de japonais/kanji.json",
                       "absents_de_kanjidic": sorted(voulus - set(out))},
              "kanji": dict(sorted(out.items()))}
    with open(os.path.join(CARTES, "sources", "kanji-complement.json"), "w", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print(len(out), "kanji ajoutés ;", "absents :", "".join(sorted(voulus - set(out))) or "aucun")


if __name__ == "__main__":
    main(sys.argv[1])
