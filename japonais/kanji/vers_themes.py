# -*- coding: utf-8 -*-
"""Fait des kanji N5 des THEMES DE CARTES, au format de japonais/datos/themes.json.

    python japonais/kanji/vers_themes.py

Entree : japonais/kanji/mnemoniques_n5.json (genere par construire.py),
         japonais/kanji/traits/*.svg (KanjiVG, CC BY-SA 3.0),
         japonais/datos/*.json (pour traduire les mots d'exemple en francais).
Sortie : japonais/datos/kanji.json -- FICHIER DERIVE, ne pas le corriger a la
         main : on corrige textes/textes_n5.json, on relance construire.py,
         puis ce script.

CE QUE LA CARTE MONTRE. Le kanji en grand au recto (on le RECONNAIT avant de
l'ecrire, comme un kana) ; au verso son sens, la lecture enseignee et son
romaji, l'ordre des traits, les autres lectures, deux mots N5 qui le portent.

LE MNEMONIQUE N'APPARAIT QUE VALIDE (etat « validee » : Jacques a dit oui au
texte actuel et il respecte la charte des sons). Les autres restent dans
mnemoniques_n5.json, a juger : une image fausse s'apprend aussi bien qu'une
juste, et on ne la desapprend pas. Toutes les cartes restent « brouillon » tant
qu'un natif n'a pas relu les lectures.
"""
import importlib.util
import io
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.normpath(os.path.join(ICI, ".."))
DATOS = os.path.join(JAPONAIS, "datos")

# Six themes, par le sens : on apprend ensemble ce qui se dit ensemble.
THEMES = [
    ("kanji_nombres", "数", "Kanji — numbers and money", "Kanji — les nombres et l'argent",
     "一二三四五六七八九十百千万円"),
    ("kanji_temps", "時", "Kanji — days and time", "Kanji — les jours et le temps",
     "日月火水木金土年時間午前後半今毎週"),
    ("kanji_personnes", "人", "Kanji — people", "Kanji — les personnes",
     "人男女子父母友名先生学校"),
    ("kanji_lieux", "山", "Kanji — places and directions", "Kanji — les lieux et les directions",
     "上下中左右外東西南北国山川天気雨電車本"),
    ("kanji_actions", "行", "Kanji — actions", "Kanji — les actions",
     "行来出入見聞話読書食休言"),
    ("kanji_qualites", "大", "Kanji — size and qualities", "Kanji — la taille et les qualités",
     "大小高長白多少新古安何語"),
]

NOM_JA = {"kanji_nombres": "数字", "kanji_temps": "時間", "kanji_personnes": "人",
          "kanji_lieux": "場所", "kanji_actions": "動作", "kanji_qualites": "様子"}

SVG_ICONE = ('<svg viewBox="0 0 24 24"><text x="12" y="18" text-anchor="middle" '
             'font-size="16" font-family="sans-serif">{}</text></svg>')

# LA LECTURE DE LA CARTE (celle qu'on dit et qu'on retient d'abord). Le pilote
# des mnemoniques CALCULE une lecture (la plus frequente dans les mots N5) ;
# c'est un outil pour juger la methode, pas une lecture de manuel : il donne
# 日 → び, 三 → み, 人 → り. La carte prend donc la lecture qu'un manuel donne
# en premier : le kanji dit seul quand il est un mot (山 やま, 人 ひと, 見る),
# la lecture on sinon (学 ガク, 気 キ) et pour les nombres. Une mnemonique
# VALIDEE garde SA lecture : c'est le son qu'elle fait retenir.
# Ecrite a la main, a faire relire par un natif comme le reste.
LECTURE_CARTE = {
    "一": "イチ", "二": "ニ", "三": "サン", "四": "よん", "五": "ゴ", "六": "ロク",
    "七": "なな", "八": "ハチ", "九": "キュウ", "十": "ジュウ", "百": "ヒャク",
    "千": "セン", "万": "マン", "円": "エン",
    "日": "ひ", "月": "つき", "水": "みず", "木": "き", "金": "かね", "土": "つち",
    "年": "とし", "時": "とき", "午": "ゴ", "前": "まえ", "後": "あと", "半": "ハン",
    "毎": "マイ",
    "人": "ひと", "男": "おとこ", "女": "おんな", "子": "こ", "父": "ちち", "母": "はは",
    "友": "とも", "名": "な", "先": "さき", "生": "セイ", "学": "ガク", "校": "コウ",
    "上": "うえ", "下": "した", "左": "ひだり", "右": "みぎ", "外": "そと",
    "東": "ひがし", "西": "にし", "南": "みなみ", "国": "くに", "川": "かわ",
    "気": "キ", "雨": "あめ", "車": "くるま", "本": "ホン",
    "行": "いく", "来": "くる", "入": "はいる", "見": "みる", "聞": "きく",
    "話": "はなす", "読": "よむ", "書": "かく", "食": "たべる",
    "小": "ちいさい", "長": "ながい", "白": "しろ", "何": "なに", "語": "ゴ",
}

ROMAJI = None


def romaji(kana):
    global ROMAJI
    if ROMAJI is None:
        spec = importlib.util.spec_from_file_location(
            "cartes_construire", os.path.join(JAPONAIS, "cartes", "outils", "construire.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        ROMAJI = m.romaji
    # Le romaji des cartes attend des hiragana : la lecture on est en katakana.
    return ROMAJI("".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in kana))


def lectures_kanjidic():
    """kanji -> (on, kun) de KANJIDIC2, trois au plus de chaque, sous une forme
    lisible : ひと.つ devient ひと(つ), les tirets des prefixes tombent."""
    d = lire(os.path.join(JAPONAIS, "kanji.json"))["niveaux"]["N5"]
    net = lambda r: re.sub(r"\.(.+)$", r"(\1)", r.replace("-", ""))
    sortie = {}
    for k in d:
        on, kun = [], []
        for r in k.get("lectures_on", []):
            if net(r) not in on:
                on.append(net(r))
        for r in k.get("lectures_kun", []):
            if net(r) not in kun:
                kun.append(net(r))
        sortie[k["kanji"]] = (on[:3], kun[:3])
    return sortie


def lire(chemin):
    with io.open(chemin, encoding="utf-8") as f:
        return json.load(f)


def sans_gras(texte):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", texte or "")


def traductions():
    """mot japonais -> (fr, en), pris dans les fichiers de mots de l'app."""
    t = {}
    for nom in ("themes.json", "verbes.json", "adjectifs.json", "adverbes.json",
                "expressions.json", "fonctionnels.json"):
        d = lire(os.path.join(DATOS, nom))
        listes = []
        if "themes" in d:
            listes = [m for th in d["themes"] for m in th.get("mots", [])]
        else:
            for v in d.values():
                if isinstance(v, list):
                    listes.extend(v)
        for m in listes:
            if not isinstance(m, dict):
                continue
            mot = m.get("mot") or m.get("infinitif")
            if mot and mot not in t and m.get("traduction"):
                t[mot] = (m["traduction"], m.get("traduction_en", ""))
    return t


def note(k, lectures, fr):
    on, kun = lectures
    morceaux = []
    if k.get("etat") == "validée":
        morceaux.append(sans_gras(k["mnemo_fr"] if fr else k.get("mnemo_en", "")))
    l = []
    if on:
        l.append("On : " + ", ".join(on))
    if kun:
        l.append("Kun : " + ", ".join(kun))
    if l:
        morceaux.append(" · ".join(l))
    return "\n".join(morceaux)


def main():
    kanji = {k["kanji"]: k for k in lire(os.path.join(ICI, "mnemoniques_n5.json"))["kanji"]}
    trad = traductions()
    kd = lectures_kanjidic()
    places = "".join(t[4] for t in THEMES)
    manquants = [c for c in kanji if c not in places]
    if manquants:
        raise SystemExit("Kanji N5 sans theme : " + "".join(manquants))
    doubles = [c for c in set(places) if places.count(c) > 1]
    if doubles:
        raise SystemExit("Kanji dans deux themes : " + "".join(doubles))

    sortie = []
    for tid, icone, nom_en, nom_fr, signes in THEMES:
        cartes = []
        for c in signes:
            if c not in kanji:
                continue  # un kanji de la liste longue (103) qui n'est pas dans nos 79
            k = kanji[c]
            ex = (k.get("exemples") or [])[:2]
            fr = [trad.get(e["mot"], ("", ""))[0] for e in ex]
            en = [trad.get(e["mot"], ("", e.get("sens_en", "")))[1] or e.get("sens_en", "") for e in ex]
            svg = "kanji/traits/%05x.svg" % ord(c)
            if not os.path.exists(os.path.join(JAPONAIS, svg)):
                raise SystemExit("Trace absent : " + svg)
            lecture = k["lecture_enseignee"]["kana"] if k.get("etat") == "validée" else LECTURE_CARTE.get(c)
            if not lecture:
                raise SystemExit("Pas de lecture de carte pour " + c)
            cartes.append({
                "mot": c,
                "lecture": lecture,
                "romaji": romaji(lecture),
                "furigana": None,
                "traduction": k["sens_fr"],
                "traduction_en": k["sens_en"],
                "note": note(k, kd[c], True),
                "note_en": note(k, kd[c], False),
                "exemple": " · ".join("%s（%s）" % (e["mot"], e["kana"]) for e in ex),
                "exemple_fr": " · ".join(x for x in fr if x),
                "exemple_en": " · ".join(x for x in en if x),
                "traits": k["traits"],
                "svg": svg,
                "id": "ja:kanji:" + c,
                "classe": "kanji",
                "mnemonique": "validée" if k.get("etat") == "validée" else "à juger",
                "statut": "brouillon",
            })
        sortie.append({
            "id": tid + "_a1",
            "nom_theme": nom_en,
            "nom_theme_ja": "漢字・" + NOM_JA[tid],
            "nom_theme_fr": nom_fr,
            "niveau": "A1",
            "jlpt": "N5",
            "kanji": True,
            "svg": SVG_ICONE.format(icone),
            "mots": cartes,
        })

    chemin = os.path.join(DATOS, "kanji.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_lisez_moi": "Derive de japonais/kanji/ par japonais/kanji/vers_themes.py : ne pas modifier a la main.",
                   "themes": sortie}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    total = sum(len(t["mots"]) for t in sortie)
    valides = sum(1 for t in sortie for c in t["mots"] if c["mnemonique"] == "validée")
    sans_fr = sum(1 for t in sortie for c in t["mots"] if c["exemple"] and not c["exemple_fr"])
    print(f"{len(sortie)} themes, {total} kanji, {valides} mnemoniques validees montrees -> {os.path.relpath(chemin)}")
    print(f"exemples sans traduction francaise : {sans_fr}")


if __name__ == "__main__":
    main()
