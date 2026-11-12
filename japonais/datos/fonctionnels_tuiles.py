# -*- coding: utf-8 -*-
"""Range les mots-outils japonais par TUILE, comme l'allemand et l'anglais.

    python japonais/datos/fonctionnels_tuiles.py      # refait fonctionnels.json en place

POURQUOI (lot J4, 11 nov. 2026). Le moteur lit funktionswort.json par cles --
`partikeln`, `pronomen`, `zahlen`, `konjunktionen`, `praepositionen`,
`artikelwoerter` (FUNKTIONSWORT_THEMES dans index.html). Le japonais rangeait
ses mots-outils par NIVEAU (A1, A2...) : le moteur n'y trouvait aucune de ses
cles, gardait les listes ALLEMANDES de prepositions, de conjonctions et de
particules, et la recherche japonaise les servait.

Les cles du japonais :
  - partikeln     : les particules (は, が, を...), la copule et ます, les
                    auxiliaires, prefixes et suffixes -- les « petits mots » ;
  - pronomen      : pronoms, こそあど (これ, この, ここ...), interrogatifs ;
  - zahlen        : les nombres et les compteurs (ecrits ici, a la main) ;
  - konjunktionen : les connecteurs (そして, でも, だから...) ;
  - praepositionen et artikelwoerter : VIDES, expres. Le japonais n'en a pas ;
    une liste vide dit au moteur de ne rien garder (pas de repli allemand).

Chaque entree garde les champs japonais (lecture, romaji, furigana, note) et
recoit ceux qu'attend le chargeur : kategorie / kategorie_en, niveau.

Appele par construire.py au moment d'ecrire fonctionnels.json ; lance seul,
il refait le fichier en place a partir de sa forme par niveau.
Brouillon : les nombres et compteurs ecrits ici sont a faire relire par un natif.
"""
import importlib.util
import io
import json
import os
from collections import OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.normpath(os.path.join(ICI, ".."))

KATEGORIE_EN = {
    "particule": "particle", "particule de fin": "sentence-final particle", "copule": "copula",
    "terminaison": "verb ending", "conjonction": "conjunction", "pronom": "pronoun",
    "démonstratif": "demonstrative", "compteur": "counter", "auxiliaire": "auxiliary",
    "préfixe": "prefix", "suffixe": "suffix", "nombre": "number", "connecteur": "connector",
}

# Les nombres et les compteurs : les mots que le tableau des reperes enseigne,
# en cartes. Le N5 (A1) d'abord, puis les compteurs courants du N4.
NOMBRES = [
    # mot, lecture, fr, en, kategorie, niveau, exemple, ex_lecture?, ex_fr, ex_en
    ("一", "いち", "un", "one", "nombre", "A1", "一から十まで数えます。", "Je compte de un à dix.", "I count from one to ten."),
    ("二", "に", "deux", "two", "nombre", "A1", "二かける三は六です。", "Deux fois trois font six.", "Two times three is six."),
    ("三", "さん", "trois", "three", "nombre", "A1", "三時に会いましょう。", "Retrouvons-nous à 3 h.", "Let's meet at three."),
    ("四", "よん", "quatre (aussi し)", "four (also shi)", "nombre", "A1", "四月に日本へ行きます。", "En avril, je vais au Japon.", "I'm going to Japan in April."),
    ("五", "ご", "cinq", "five", "nombre", "A1", "五分待ってください。", "Attendez cinq minutes, s'il vous plaît.", "Please wait five minutes."),
    ("六", "ろく", "six", "six", "nombre", "A1", "六時に起きます。", "Je me lève à 6 h.", "I get up at six."),
    ("七", "なな", "sept (aussi しち)", "seven (also shichi)", "nombre", "A1", "七時に晩ご飯を食べます。", "Je dîne à 7 h.", "I have dinner at seven."),
    ("八", "はち", "huit", "eight", "nombre", "A1", "八百円です。", "C'est 800 yens.", "It's 800 yen."),
    ("九", "きゅう", "neuf (aussi く)", "nine (also ku)", "nombre", "A1", "九時に寝ます。", "Je me couche à 9 h.", "I go to bed at nine."),
    ("十", "じゅう", "dix", "ten", "nombre", "A1", "十人来ました。", "Dix personnes sont venues.", "Ten people came."),
    ("百", "ひゃく", "cent", "hundred", "nombre", "A1", "このペンは百円です。", "Ce stylo coûte 100 yens.", "This pen is 100 yen."),
    ("千", "せん", "mille", "thousand", "nombre", "A1", "千円札を持っています。", "J'ai un billet de mille yens.", "I have a thousand-yen note."),
    ("万", "まん", "dix mille", "ten thousand", "nombre", "A1", "一万円は高いです。", "Dix mille yens, c'est cher.", "Ten thousand yen is expensive."),
    ("ゼロ", "ゼロ", "zéro", "zero", "nombre", "A1", "ゼロから始めます。", "Je commence de zéro.", "I'm starting from zero."),
    ("～つ", "～つ", "(compteur des choses : ひとつ, ふたつ…)", "(counter for things: hitotsu, futatsu…)", "compteur", "A1", "りんごを三つください。", "Trois pommes, s'il vous plaît.", "Three apples, please."),
    ("～人", "～にん", "(compteur des personnes : 三人 ; mais ひとり, ふたり)", "(counter for people: sannin; but hitori, futari)", "compteur", "A1", "家族は四人です。", "Nous sommes quatre dans la famille.", "There are four of us in my family."),
    ("～円", "～えん", "… yens (la monnaie)", "… yen (currency)", "compteur", "A1", "全部で五百円です。", "Ça fait 500 yens en tout.", "That's 500 yen altogether."),
    ("～時", "～じ", "… heure(s)", "… o'clock", "compteur", "A1", "今、三時です。", "Il est 3 h.", "It's three o'clock now."),
    ("～分", "～ふん / ～ぷん", "… minute(s)", "… minute(s)", "compteur", "A1", "駅まで十分かかります。", "Il faut dix minutes jusqu'à la gare.", "It takes ten minutes to the station."),
    ("～歳", "～さい", "… an(s) (l'âge)", "… years old", "compteur", "A1", "私は二十歳です。", "J'ai vingt ans.", "I'm twenty."),
    ("～枚", "～まい", "(compteur des choses plates : feuilles, billets, chemises)", "(counter for flat things: sheets, tickets, shirts)", "compteur", "A1", "切手を二枚ください。", "Deux timbres, s'il vous plaît.", "Two stamps, please."),
    ("～本", "～ほん", "(compteur des choses longues : bouteilles, crayons)", "(counter for long things: bottles, pencils)", "compteur", "A1", "ビールを一本ください。", "Une bière (bouteille), s'il vous plaît.", "One bottle of beer, please."),
    ("～冊", "～さつ", "(compteur des livres et cahiers)", "(counter for books and notebooks)", "compteur", "A2", "本を三冊買いました。", "J'ai acheté trois livres.", "I bought three books."),
    ("～台", "～だい", "(compteur des machines et véhicules)", "(counter for machines and vehicles)", "compteur", "A2", "車が二台あります。", "Il y a deux voitures.", "There are two cars."),
    ("～匹", "～ひき", "(compteur des petits animaux)", "(counter for small animals)", "compteur", "A2", "猫が三匹います。", "Il y a trois chats.", "There are three cats."),
    ("～回", "～かい", "… fois", "… times", "compteur", "A2", "一日に三回歯を磨きます。", "Je me brosse les dents trois fois par jour.", "I brush my teeth three times a day."),
    ("～階", "～かい / ～がい", "… étage", "… floor", "compteur", "A2", "トイレは二階です。", "Les toilettes sont au premier étage.", "The toilet is on the second floor."),
    ("～杯", "～はい", "(compteur des verres, tasses, bols)", "(counter for cups, glasses, bowls)", "compteur", "A2", "コーヒーを一杯飲みました。", "J'ai bu une tasse de café.", "I drank a cup of coffee."),
    ("～番", "～ばん", "numéro …", "number …", "compteur", "A2", "三番のバスに乗ります。", "Je prends le bus numéro 3.", "I take bus number three."),
]


def _romaji():
    spec = importlib.util.spec_from_file_location(
        "cartes_construire", os.path.join(JAPONAIS, "cartes", "outils", "construire.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    def r(kana):
        k = kana.replace("～", "").split("/")[0].strip()
        try:
            return m.romaji("".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in k))
        except Exception:
            return ""
    return r


def entrees_nombres():
    r = _romaji()
    out = []
    for mot, lect, fr, en, kat, niv, ex, ex_fr, ex_en in NOMBRES:
        out.append(OrderedDict([
            ("mot", mot), ("lecture", lect), ("romaji", r(lect)), ("furigana", None),
            ("traduction", fr), ("traduction_en", en), ("note", ""),
            ("exemple", ex), ("exemple_fr", ex_fr), ("exemple_en", ex_en),
            ("kategorie", kat), ("kategorie_en", KATEGORIE_EN[kat]), ("niveau", niv),
            ("id", "ja:nombre:" + mot), ("statut", "brouillon"),
        ]))
    return out


def cle_de(e):
    c = e.get("classe")
    k = e.get("kategorie", "")
    if c == "conj" or k == "conjonction":
        # ので, のに, けど, し : écrits comme particules de liaison, rangés
        # avec les connecteurs, ou un apprenant les cherche.
        return "konjunktionen"
    if c in ("pn", "adj-pn") or k in ("pronom", "démonstratif"):
        return "pronomen"
    if c == "ctr" or k == "compteur":
        return "zahlen"
    # Une unite (キロ) ou un suffixe de comptage (軒) : avec les nombres.
    t = (e.get("traduction") or "").lower()
    if t.startswith("(compteur") or t.startswith("kilo"):
        return "zahlen"
    return "partikeln"


def regrouper(par_niveau):
    """{A1: [...], A2: [...]} -> {partikeln: [...], pronomen: [...], ...}."""
    if not any(k in par_niveau for k in ("A1", "A2", "B1", "B2", "C1")):
        return par_niveau  # deja range par tuile
    sortie = OrderedDict((k, []) for k in ("partikeln", "pronomen", "zahlen", "konjunktionen",
                                           "praepositionen", "artikelwoerter"))
    deja_nombres = set()
    for niv, liste in par_niveau.items():
        for e in liste:
            e = OrderedDict(e)
            e["niveau"] = niv
            k = e.get("kategorie") or ""
            e["kategorie_en"] = KATEGORIE_EN.get(k, k)
            cle = cle_de(e)
            sortie[cle].append(e)
            if cle == "zahlen":
                deja_nombres.add(e["mot"].lstrip("～"))
    for e in entrees_nombres():
        if e["mot"].lstrip("～") not in deja_nombres:
            sortie["zahlen"].append(e)
    rang = {"A1": 0, "A2": 1, "B1": 2, "B2": 3, "C1": 4}
    # Dans un niveau, les particules d'abord, puis la copule et les terminaisons,
    # puis les auxiliaires, suffixes et prefixes (tri stable).
    nature = {"particule": 0, "particule de fin": 1, "copule": 2, "terminaison": 3,
              "auxiliaire": 4, "suffixe": 5, "préfixe": 6}
    for k in sortie:
        sortie[k].sort(key=lambda e: (rang.get(e.get("niveau"), 9),
                                      nature.get(e.get("kategorie"), 3) if k == "partikeln" else 0))
    return sortie


def main():
    chemin = os.path.join(ICI, "fonctionnels.json")
    with io.open(chemin, encoding="utf-8") as f:
        d = json.load(f, object_pairs_hook=OrderedDict)
    r = regrouper(d)
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(", ".join("%s %d" % (k, len(v)) for k, v in r.items()), "->", os.path.relpath(chemin))


if __name__ == "__main__":
    main()
