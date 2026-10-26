# -*- coding: utf-8 -*-
"""Fait des kana des THEMES DE CARTES, au format de japonais/datos/themes.json.

    python japonais/kana/outils/vers_themes.py

Entree : japonais/kana/kana.json (les 248 signes et leurs groupes),
         japonais/kana/mnemoniques.json (brouillon a relire),
         japonais/datos/themes.json (pour donner a chaque signe un mot N5).
Sortie : japonais/datos/kana.json -- FICHIER DERIVE, ne pas le corriger a la
         main : on corrige kana.json ou mnemoniques.json, puis on relance.

POURQUOI DES THEMES. Le moteur sait deja tout faire d'un theme : la seance du
jour, la repetition espacee, « Parcourir par theme », la progression. Un kana
y devient une carte comme une autre : le signe, son romaji, son trace
(KanjiVG), son mnemonique, et un premier mot qui commence par lui.

Six themes, dans l'ordre ou on les apprend : hiragana de base (46), puis
dakuten / handakuten et le petit っ, puis les sons contractes (yoon) ; la
meme chose en katakana, plus les katakana etendus des mots etrangers. Les
quatre signes rares (ゐ ゑ ヰ ヱ) restent hors des cartes.
"""
import io
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
KANA = os.path.normpath(os.path.join(ICI, ".."))
JAPONAIS = os.path.normpath(os.path.join(KANA, ".."))
DATOS = os.path.join(JAPONAIS, "datos")

THEMES = [
    ("kana_hiragana", "ひらがな", "Hiragana", "Hiragana — the 46 basic signs",
     "Hiragana — les 46 signes de base", ["H01", "H02", "H03", "H04", "H05", "H06", "H07", "H08", "H09", "H10"]),
    ("kana_hiragana_dakuten", "ひらがな ゛゜", "Hiragana ゛゜", "Hiragana — voiced sounds and small っ",
     "Hiragana — sons sonores (゛ ゜) et petit っ", ["H11", "H12", "H13", "H17"]),
    ("kana_hiragana_yoon", "ひらがな きゃ", "Hiragana きゃ", "Hiragana — combined sounds (kya, sho…)",
     "Hiragana — sons combinés (kya, sho…)", ["H14", "H15", "H16"]),
    ("kana_katakana", "カタカナ", "Katakana", "Katakana — the 46 basic signs",
     "Katakana — les 46 signes de base", ["K01", "K02", "K03", "K04", "K05", "K06", "K07", "K08", "K09", "K10"]),
    ("kana_katakana_dakuten", "カタカナ ゛゜", "Katakana ゛゜", "Katakana — voiced sounds, ッ and ー",
     "Katakana — sons sonores (゛ ゜), ッ et ー", ["K11", "K12", "K13", "K17"]),
    ("kana_katakana_yoon", "カタカナ キャ", "Katakana キャ", "Katakana — combined and foreign sounds",
     "Katakana — sons combinés et sons étrangers", ["K14", "K15", "K16", "K18", "K19", "K20"]),
]

SVG_ICONE = ('<svg viewBox="0 0 24 24"><text x="12" y="18" text-anchor="middle" '
             'font-size="16" font-family="sans-serif">{}</text></svg>')


def lire(chemin):
    with io.open(chemin, encoding="utf-8") as f:
        return json.load(f)


def sans_gras(texte):
    # Les mnemoniques marquent le son en **gras** : la carte n'a pas de
    # Markdown, on garde le texte.
    return re.sub(r"\*\*(.+?)\*\*", r"\1", texte or "")


def premiers_mots(themes):
    """Les noms de tous les niveaux, le N5 d'abord : un signe rare (ぬ, ぽ) trouve
    plus souvent son mot au N4 ou au N3 qu'au N5."""
    rang = {"N5": 0, "N4": 1, "N3": 2, "N2": 3, "N1": 4}
    mots = []
    for t in themes.get("themes", []):
        r = rang.get(t.get("jlpt"), 9)
        for m in t.get("mots", []):
            if m.get("lecture") and m.get("mot"):
                mots.append((r, m))
    return mots


def katakana_vers_hiragana(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def mot_pour(signe, ecriture, mots):
    """Le mot le plus simple dont la lecture commence par ce signe (le N5 d'abord,
    puis le plus court). En katakana, seulement un mot ECRIT en katakana
    (コーヒー) : un mot en hiragana sous une carte de katakana tromperait."""
    if signe in ("ー", "っ", "ッ", "ん", "ン"):
        cands = [(r, m) for r, m in mots if signe in m["mot"] or signe in m["lecture"]]
        if ecriture == "katakana":
            cands = [(r, m) for r, m in cands if signe in m["mot"]]
    elif ecriture == "katakana":
        cands = [(r, m) for r, m in mots if m["mot"].startswith(signe)]
    else:
        cands = [(r, m) for r, m in mots if m["lecture"].startswith(signe)]
    if not cands:
        return None
    cands.sort(key=lambda rm: (rm[0], len(rm[1]["lecture"]), len(rm[1]["mot"])))
    return cands[0][1]


def exemple_de(m):
    if not m:
        return ""
    return m["mot"] if m["mot"] == m["lecture"] else m["mot"] + "（" + m["lecture"] + "）"


def main():
    kana = lire(os.path.join(KANA, "kana.json"))
    mnemo = {(m["signe"]): m for m in lire(os.path.join(KANA, "mnemoniques.json"))["mnemoniques"]}
    mots = premiers_mots(lire(os.path.join(DATOS, "themes.json")))
    groupes = {g["id"]: g for g in kana["groupes"]}
    signes = {s["signe"]: s for s in kana["signes"]}

    sortie = []
    sans_mot = []
    for tid, nom_ja, nom_en_court, nom_en, nom_fr, ids in THEMES:
        cartes = []
        for gid in ids:
            for sg in groupes[gid]["signes"]:
                s = signes[sg]
                mn = mnemo.get(sg, {})
                m = mot_pour(sg, s["ecriture"], mots)
                if m is None:
                    sans_mot.append(sg)
                comp = s.get("composants") or []
                carte = {
                    "mot": sg,
                    "lecture": sg,
                    "romaji": s["romaji"],
                    "furigana": None,
                    "traduction": s["romaji"],
                    "traduction_en": s["romaji"],
                    "note": sans_gras(mn.get("fr", "")),
                    "note_en": sans_gras(mn.get("en", "")),
                    "exemple": exemple_de(m),
                    "exemple_fr": m.get("traduction", "") if m else "",
                    "exemple_en": m.get("traduction_en", "") if m else "",
                    "traits": s.get("traits"),
                    "svg": ("kana/" + comp[0]["svg"]) if len(comp) == 1 and comp[0].get("svg") else "",
                    "id": "ja:kana:" + s["id"],
                    "classe": "kana",
                    "ecriture": s["ecriture"],
                    "groupe": gid,
                    "statut": "brouillon" if mn else "sans_mnemonique",
                }
                cartes.append(carte)
        sortie.append({
            "id": tid + "_a1",
            "nom_theme": nom_en,
            "nom_theme_ja": nom_ja,
            "nom_theme_fr": nom_fr,
            "niveau": "A1",
            "jlpt": "N5",
            "kana": True,
            "svg": SVG_ICONE.format(nom_ja[0]),
            "mots": cartes,
        })

    chemin = os.path.join(DATOS, "kana.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_lisez_moi": "Derive de japonais/kana/ par japonais/kana/outils/vers_themes.py : ne pas modifier a la main.",
                   "themes": sortie}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    total = sum(len(t["mots"]) for t in sortie)
    avec_mn = sum(1 for t in sortie for c in t["mots"] if c["note"])
    print(f"{len(sortie)} themes, {total} kana, {avec_mn} avec mnemonique -> {os.path.relpath(chemin)}")
    if sans_mot:
        print(f"sans mot d'exemple ({len(sans_mot)}) : {' '.join(sans_mot)}")


if __name__ == "__main__":
    main()
