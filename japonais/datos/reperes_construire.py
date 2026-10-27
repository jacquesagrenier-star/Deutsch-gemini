# -*- coding: utf-8 -*-
"""Construit japonais/datos/reperes.json : les reperes du japonais.

    python japonais/datos/reperes_construire.py

LES MEMES BLOCS QUE L'ALLEMAND ET L'ESPAGNOL (tests/reperes_construire.py), lus
par le meme moteur (preparerReperes / exercicesRepere dans index.html) : un
tableau a decouvrir d'un coup, puis des exercices, puis des revisions a J+1,
J+3, J+7. Ce que le japonais n'a pas (alphabet a epeler, genre, pluriel) n'est
pas la ; ce qu'il a en propre y entre : les COMPTEURS (ひとつ, ひとり), et
l'heure, qui change de son comme eux.

Une ligne : [forme ecrite, sens, prononciation]. La forme est ecrite comme un
Japonais l'ecrit (kanji : 二十一, 月曜日) ; c'est elle que la voix lit et que
la reconnaissance vocale rend. La « prononciation », sous la forme, donne la
lecture en kana et le romaji : un debutant ne lit pas encore les kanji.

Ecrit a la main, brouillon : a faire relire par un natif comme le reste.
"""
import importlib.util
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.normpath(os.path.join(ICI, ".."))

spec = importlib.util.spec_from_file_location(
    "cartes_construire", os.path.join(JAPONAIS, "cartes", "outils", "construire.py"))
_m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_m)


def romaji(kana):
    return _m.romaji("".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in kana))


def pr(kana):
    """La prononciation sous la forme : la lecture en kana, puis le romaji."""
    r = romaji(kana)
    return {"fr": kana + " · " + r, "en": kana + " · " + r}


def fe(fr, en):
    return {"fr": fr, "en": en}


def ligne(forme, sens, kana):
    return [forme, sens, pr(kana)]


# --- Les nombres ----------------------------------------------------------
UNITES = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
UNITES_KANA = ["", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう"]
CENTAINES_KANA = ["", "ひゃく", "にひゃく", "さんびゃく", "よんひゃく", "ごひゃく",
                  "ろっぴゃく", "ななひゃく", "はっぴゃく", "きゅうひゃく"]


def nombre(n):
    """(kanji, kana) de 0 a 1000, comme on le dit : 十四 じゅうよん, 三百 さんびゃく."""
    if n == 0:
        return "ゼロ", "ゼロ"
    if n == 1000:
        return "千", "せん"
    c, d, u = n // 100, (n // 10) % 10, n % 10
    kj, kn = "", ""
    if c:
        kj += ("" if c == 1 else UNITES[c]) + "百"
        kn += CENTAINES_KANA[c]
    if d:
        kj += ("" if d == 1 else UNITES[d]) + "十"
        kn += ("" if d == 1 else UNITES_KANA[d]) + "じゅう"
    if u:
        kj += UNITES[u]
        kn += UNITES_KANA[u]
    return kj, kn


def ligne_nombre(n):
    kj, kn = nombre(n)
    return [kj, str(n), pr(kn)]


def extra_nombre(n):
    kj, kn = nombre(n)
    return [kj, str(n), pr(kn)]


REPERES = []

REPERES.append({
    "id": "n0-20", "type": "nombre",
    "t": fe("Les nombres de 0 à 20", "Numbers from 0 to 20"),
    "a": fe("Après 10, on assemble : 十一 (10 + 1) = じゅういち, 二十 (2 × 10) = にじゅう. "
            "4 et 7 ont deux lectures : よん ou し, なな ou しち ; on dit よん et なな pour compter. "
            "9 se dit きゅう (く existe aussi).",
            "After 10, you build: 十一 (10 + 1) = jūichi, 二十 (2 × 10) = nijū. "
            "4 and 7 have two readings: yon or shi, nana or shichi; yon and nana are used for counting. "
            "9 is kyū (ku also exists)."),
    "l": [ligne_nombre(n) for n in range(0, 21)],
    "x": [],
})
REPERES.append({
    "id": "n20-100", "type": "nombre",
    "t": fe("Les dizaines, jusqu'à 100", "Tens, up to 100"),
    "a": fe("Une dizaine = le chiffre + 十 : 三十 さんじゅう (3 × 10). On ajoute l'unité derrière : "
            "三十五 さんじゅうご (35). 100 se dit 百 ひゃく, sans « un » devant.",
            "A ten = the digit + 十: 三十 sanjū (3 × 10). The unit goes after: "
            "三十五 sanjūgo (35). 100 is 百 hyaku, with no “one” in front."),
    "l": [ligne_nombre(n) for n in (20, 21, 30, 40, 50, 60, 70, 80, 90, 100)],
    "x": [extra_nombre(n) for n in (23, 26, 35, 43, 47, 58, 64, 76, 89, 92)],
})
REPERES.append({
    "id": "n100-1000", "type": "nombre",
    "t": fe("Les centaines, jusqu'à 1000", "Hundreds, up to 1,000"),
    "a": fe("Le son change trois fois : 300 さんびゃく, 600 ろっぴゃく, 800 はっぴゃく. "
            "1000 = 千 せん (3000 さんぜん, 8000 はっせん). Et le japonais compte par 10 000 : "
            "一万 いちまん, pas « dix mille ».",
            "The sound changes three times: 300 sanbyaku, 600 roppyaku, 800 happyaku. "
            "1,000 = 千 sen (3,000 sanzen, 8,000 hassen). And Japanese counts in 10,000s: "
            "一万 ichiman, not “ten thousand”."),
    "l": [ligne_nombre(n) for n in (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)],
    "x": [extra_nombre(n) for n in (101, 120, 250, 345, 505, 680, 712, 999)],
})

JOURS = [
    ("月曜日", "げつようび", "lundi", "Monday"),
    ("火曜日", "かようび", "mardi", "Tuesday"),
    ("水曜日", "すいようび", "mercredi", "Wednesday"),
    ("木曜日", "もくようび", "jeudi", "Thursday"),
    ("金曜日", "きんようび", "vendredi", "Friday"),
    ("土曜日", "どようび", "samedi", "Saturday"),
    ("日曜日", "にちようび", "dimanche", "Sunday"),
]
REPERES.append({
    "id": "jours", "type": "suite",
    "t": fe("Les jours de la semaine", "The days of the week"),
    "a": fe("Chaque jour porte un astre : 月 la lune (lundi), 火 le feu, 水 l'eau, 木 le bois, "
            "金 le métal, 土 la terre, 日 le soleil (dimanche). 曜日 (ようび) veut dire « jour de la semaine ». "
            "« Quel jour ? » : 何曜日 (なんようび).",
            "Each day carries an element: 月 the moon (Monday), 火 fire, 水 water, 木 wood, "
            "金 metal, 土 earth, 日 the sun (Sunday). 曜日 (yōbi) means “day of the week”. "
            "“Which day?”: 何曜日 (nan'yōbi)."),
    "l": [ligne(k, fe(fr, en), kn) for k, kn, fr, en in JOURS],
    "p": [
        ["月曜日、火曜日、水曜日", fe("lundi, mardi, mercredi", "Monday, Tuesday, Wednesday")],
        ["木曜日、金曜日、土曜日、日曜日", fe("jeudi, vendredi, samedi, dimanche", "Thursday, Friday, Saturday, Sunday")],
        ["今日は月曜日です", fe("Aujourd'hui, c'est lundi.", "Today is Monday.")],
        ["土曜日と日曜日", fe("samedi et dimanche", "Saturday and Sunday")],
    ],
})

COULEURS = [
    ("赤", "あか", "rouge", "red", "#d93a32"),
    ("青", "あお", "bleu", "blue", "#2f6fd6"),
    ("緑", "みどり", "vert", "green", "#2e9e4f"),
    ("黄色", "きいろ", "jaune", "yellow", "#f2c500"),
    ("黒", "くろ", "noir", "black", "#1c1c1c"),
    ("白", "しろ", "blanc", "white", "#ffffff"),
    ("灰色", "はいいろ", "gris", "gray", "#8c8c8c"),
    ("茶色", "ちゃいろ", "marron", "brown", "#7a4a24"),
    ("オレンジ", "オレンジ", "orange", "orange", "#f28a1a"),
    ("ピンク", "ピンク", "rose", "pink", "#f2a0c0"),
    ("紫", "むらさき", "violet", "purple", "#7d3fb5"),
]
REPERES.append({
    "id": "couleurs", "type": "couleur",
    "t": fe("Les couleurs", "Colors"),
    "a": fe("赤 青 黒 白 deviennent des adjectifs en い : 赤い車 (une voiture rouge). 黄色 et 茶色 aussi : "
            "黄色い. Les autres prennent の : 緑の車. Et le feu vert se dit 青信号 : le « bleu » "
            "couvre une part de notre vert.",
            "赤 青 黒 白 become い-adjectives: 赤い車 (a red car). 黄色 and 茶色 too: 黄色い. "
            "The others take の: 緑の車. And a green traffic light is 青信号: “blue” covers part of our green."),
    # La teinte en l[2] (le moteur la montre), la prononciation en l[3] :
    # construireTableau la cherche la quand l[2] est une teinte.
    "l": [[k, fe(fr, en), h, pr(kn)] for k, kn, fr, en, h in COULEURS],
})

MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
           "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"]
MOIS_KANA = ["いち", "に", "さん", "し", "ご", "ろく", "しち", "はち", "く", "じゅう", "じゅういち", "じゅうに"]
MOIS_KJ = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
REPERES.append({
    "id": "mois", "type": "suite",
    "t": fe("Les mois de l'année", "The months of the year"),
    "a": fe("Pas de noms : le numéro du mois + 月 (がつ). Trois pièges : avril 四月 しがつ, "
            "juillet 七月 しちがつ, septembre 九月 くがつ (jamais よん, なな, きゅう ici). "
            "« Quel mois ? » : 何月 (なんがつ).",
            "No names: the month's number + 月 (gatsu). Three traps: April 四月 shigatsu, "
            "July 七月 shichigatsu, September 九月 kugatsu (never yon, nana, kyū here). "
            "“Which month?”: 何月 (nangatsu)."),
    "l": [ligne(MOIS_KJ[i] + "月", fe(MOIS_FR[i], MOIS_EN[i]), MOIS_KANA[i] + "がつ") for i in range(12)],
    "p": [
        ["一月、二月、三月", fe("janvier, février, mars", "January, February, March")],
        ["四月、五月、六月", fe("avril, mai, juin", "April, May, June")],
        ["七月、八月、九月", fe("juillet, août, septembre", "July, August, September")],
        ["十月、十一月、十二月", fe("octobre, novembre, décembre", "October, November, December")],
    ],
})

HEURES_KANA = ["いち", "に", "さん", "よ", "ご", "ろく", "しち", "はち", "く", "じゅう", "じゅういち", "じゅうに"]
REPERES.append({
    "id": "heures", "type": "suite",
    "t": fe("L'heure", "Telling the time"),
    "a": fe("L'heure = le nombre + 時 (じ). Trois sons changent : 4 h 四時 よじ, 7 h 七時 しちじ, "
            "9 h 九時 くじ. La demie : 半 (はん), 三時半 = 3 h 30. « Quelle heure est-il ? » : 何時ですか (なんじですか).",
            "The hour = the number + 時 (ji). Three sounds change: 4 o'clock 四時 yoji, 7 o'clock 七時 shichiji, "
            "9 o'clock 九時 kuji. Half past: 半 (han), 三時半 = 3:30. “What time is it?”: 何時ですか (nanji desu ka)."),
    "l": [ligne(MOIS_KJ[i] + "時", fe("%d h" % (i + 1), "%d o'clock" % (i + 1)), HEURES_KANA[i] + "じ") for i in range(12)],
    "p": [
        ["一時、二時、三時", fe("1 h, 2 h, 3 h", "1, 2, 3 o'clock")],
        ["四時、七時、九時", fe("4 h, 7 h, 9 h", "4, 7, 9 o'clock")],
        ["今、三時半です", fe("Il est 3 h 30.", "It's half past three.")],
        ["何時ですか", fe("Quelle heure est-il ?", "What time is it?")],
    ],
})

TSU = [("一つ", "ひとつ"), ("二つ", "ふたつ"), ("三つ", "みっつ"), ("四つ", "よっつ"), ("五つ", "いつつ"),
       ("六つ", "むっつ"), ("七つ", "ななつ"), ("八つ", "やっつ"), ("九つ", "ここのつ"), ("とお", "とお")]
REPERES.append({
    "id": "compteurs-tsu", "type": "suite",
    "t": fe("Compter les choses : ひとつ, ふたつ…", "Counting things: hitotsu, futatsu…"),
    "a": fe("Le japonais ne dit pas « trois pommes » mais « pommes, trois-choses » : りんごを三つください. "
            "Ces nombres-là sont japonais d'origine, d'où leurs sons à part. Ils s'arrêtent à 10 (とお) ; "
            "au-delà, on reprend じゅういち.",
            "Japanese doesn't say “three apples” but “apples, three-things”: りんごを三つください. "
            "These numbers are native Japanese, hence their own sounds. They stop at 10 (tō); "
            "beyond that, back to jūichi."),
    "l": [ligne(k, fe("%d (chose%s)" % (i + 1, "s" if i else ""), "%d (thing%s)" % (i + 1, "s" if i else "")), kn)
          for i, (k, kn) in enumerate(TSU)],
    "p": [
        ["一つ、二つ、三つ", fe("une, deux, trois (choses)", "one, two, three (things)")],
        ["りんごを三つください", fe("Trois pommes, s'il vous plaît.", "Three apples, please.")],
        ["四つ、五つ、六つ", fe("quatre, cinq, six (choses)", "four, five, six (things)")],
        ["コーヒーを二つください", fe("Deux cafés, s'il vous plaît.", "Two coffees, please.")],
    ],
})

NIN = [("一人", "ひとり"), ("二人", "ふたり"), ("三人", "さんにん"), ("四人", "よにん"), ("五人", "ごにん"),
       ("六人", "ろくにん"), ("七人", "ななにん"), ("八人", "はちにん"), ("九人", "きゅうにん"), ("十人", "じゅうにん")]
REPERES.append({
    "id": "compteurs-nin", "type": "suite",
    "t": fe("Compter les personnes : ひとり, ふたり…", "Counting people: hitori, futari…"),
    "a": fe("Les personnes se comptent avec 人 (にん) : 三人 さんにん. Sauf les deux premiers, à retenir tels quels : "
            "一人 ひとり (seul), 二人 ふたり (à deux). Et 4 = よにん. Au restaurant : 何名様ですか ? — 二人です.",
            "People are counted with 人 (nin): 三人 sannin. Except the first two, to learn as they are: "
            "一人 hitori (alone), 二人 futari (two people). And 4 = yonin. At a restaurant: 何名様ですか? — 二人です."),
    "l": [ligne(k, fe("%d personne%s" % (i + 1, "s" if i else ""), "%d %s" % (i + 1, "people" if i else "person")), kn)
          for i, (k, kn) in enumerate(NIN)],
    "p": [
        ["一人、二人、三人", fe("une, deux, trois personnes", "one, two, three people")],
        ["二人です", fe("Nous sommes deux.", "There are two of us.")],
        ["家族は四人です", fe("Nous sommes quatre dans la famille.", "There are four people in my family.")],
        ["一人で行きます", fe("J'y vais seul.", "I'm going alone.")],
    ],
})


# La lecture des suites a dire a voix haute (p), ecrite sous la phrase.
LECTURES_P = {
    "月曜日、火曜日、水曜日": ("げつようび、かようび、すいようび", "getsuyōbi, kayōbi, suiyōbi"),
    "木曜日、金曜日、土曜日、日曜日": ("もくようび、きんようび、どようび、にちようび", "mokuyōbi, kin'yōbi, doyōbi, nichiyōbi"),
    "今日は月曜日です": ("きょうはげつようびです", "kyō wa getsuyōbi desu"),
    "土曜日と日曜日": ("どようびとにちようび", "doyōbi to nichiyōbi"),
    "一月、二月、三月": ("いちがつ、にがつ、さんがつ", "ichigatsu, nigatsu, sangatsu"),
    "四月、五月、六月": ("しがつ、ごがつ、ろくがつ", "shigatsu, gogatsu, rokugatsu"),
    "七月、八月、九月": ("しちがつ、はちがつ、くがつ", "shichigatsu, hachigatsu, kugatsu"),
    "十月、十一月、十二月": ("じゅうがつ、じゅういちがつ、じゅうにがつ", "jūgatsu, jūichigatsu, jūnigatsu"),
    "一時、二時、三時": ("いちじ、にじ、さんじ", "ichiji, niji, sanji"),
    "四時、七時、九時": ("よじ、しちじ、くじ", "yoji, shichiji, kuji"),
    "今、三時半です": ("いま、さんじはんです", "ima, sanji han desu"),
    "何時ですか": ("なんじですか", "nanji desu ka"),
    "一つ、二つ、三つ": ("ひとつ、ふたつ、みっつ", "hitotsu, futatsu, mittsu"),
    "りんごを三つください": ("りんごをみっつください", "ringo o mittsu kudasai"),
    "四つ、五つ、六つ": ("よっつ、いつつ、むっつ", "yottsu, itsutsu, muttsu"),
    "コーヒーを二つください": ("コーヒーをふたつください", "kōhī o futatsu kudasai"),
    "一人、二人、三人": ("ひとり、ふたり、さんにん", "hitori, futari, sannin"),
    "二人です": ("ふたりです", "futari desu"),
    "家族は四人です": ("かぞくはよにんです", "kazoku wa yonin desu"),
    "一人で行きます": ("ひとりでいきます", "hitori de ikimasu"),
}


def main():
    for r in REPERES:
        for row in r.get("p", []):
            if len(row) == 2:
                kana, rom = LECTURES_P[row[0]]
                row.append({"fr": kana + " · " + rom, "en": kana + " · " + rom})
    ids = [r["id"] for r in REPERES]
    assert len(ids) == len(set(ids)), ids
    for r in REPERES:
        assert r["l"], r["id"]
        if r["type"] == "suite":
            assert len(r["l"]) > 3 and r.get("p"), r["id"]
    chemin = os.path.join(ICI, "reperes.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_lisez_moi": "Derive de japonais/datos/reperes_construire.py : ne pas modifier a la main. "
                                 "Brouillon, a faire relire par un natif.",
                   "reperes": REPERES}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("%d blocs : %s -> %s" % (len(REPERES), ", ".join(ids), os.path.relpath(chemin)))


if __name__ == "__main__":
    main()
