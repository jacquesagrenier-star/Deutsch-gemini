# -*- coding: utf-8 -*-
"""Construit kana.json à partir d'un tableau gojūon écrit à la main,
puis le recoupe contre deux sources indépendantes :
  - les noms Unicode des caractères (module unicodedata de Python),
    qui donnent consonne et voyelle de chaque signe ;
  - les SVG KanjiVG de traits/, qui donnent le nombre de traits.
Toute divergence fait échouer le script.

Usage : python japonais/kana/outils/construire.py
"""
import json
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
KANA = os.path.dirname(ICI)
TRAITS = os.path.join(KANA, "traits")

VOYELLES = ["a", "i", "u", "e", "o"]
DAN = {"a": "あ段", "i": "い段", "u": "う段", "e": "え段", "o": "お段"}

# Tableau gojūon, saisi à la main : (consonne, hiragana, katakana, romaji Hepburn).
# None = case vide du tableau moderne.
BASE = [
    ("", "あいうえお", "アイウエオ", ["a", "i", "u", "e", "o"]),
    ("k", "かきくけこ", "カキクケコ", ["ka", "ki", "ku", "ke", "ko"]),
    ("s", "さしすせそ", "サシスセソ", ["sa", "shi", "su", "se", "so"]),
    ("t", "たちつてと", "タチツテト", ["ta", "chi", "tsu", "te", "to"]),
    ("n", "なにぬねの", "ナニヌネノ", ["na", "ni", "nu", "ne", "no"]),
    ("h", "はひふへほ", "ハヒフヘホ", ["ha", "hi", "fu", "he", "ho"]),
    ("m", "まみむめも", "マミムメモ", ["ma", "mi", "mu", "me", "mo"]),
    ("y", "や_ゆ_よ", "ヤ_ユ_ヨ", ["ya", None, "yu", None, "yo"]),
    ("r", "らりるれろ", "ラリルレロ", ["ra", "ri", "ru", "re", "ro"]),
    ("w", "わ___を", "ワ___ヲ", ["wa", None, None, None, "o"]),
]
DAKU = [
    ("g", "がぎぐげご", "ガギグゲゴ", ["ga", "gi", "gu", "ge", "go"], "dakuten"),
    ("z", "ざじずぜぞ", "ザジズゼゾ", ["za", "ji", "zu", "ze", "zo"], "dakuten"),
    ("d", "だぢづでど", "ダヂヅデド", ["da", "ji", "zu", "de", "do"], "dakuten"),
    ("b", "ばびぶべぼ", "バビブベボ", ["ba", "bi", "bu", "be", "bo"], "dakuten"),
    ("p", "ぱぴぷぺぽ", "パピプペポ", ["pa", "pi", "pu", "pe", "po"], "handakuten"),
]
GYO = {"": "あ行", "k": "か行", "s": "さ行", "t": "た行", "n": "な行", "h": "は行",
       "m": "ま行", "y": "や行", "r": "ら行", "w": "わ行", "g": "が行", "z": "ざ行",
       "d": "だ行", "b": "ば行", "p": "ぱ行"}

# Yōon : (hiragana, katakana, romaji Hepburn) — 33 combinaisons.
YOON = [
    ("きゃ", "キャ", "kya"), ("きゅ", "キュ", "kyu"), ("きょ", "キョ", "kyo"),
    ("しゃ", "シャ", "sha"), ("しゅ", "シュ", "shu"), ("しょ", "ショ", "sho"),
    ("ちゃ", "チャ", "cha"), ("ちゅ", "チュ", "chu"), ("ちょ", "チョ", "cho"),
    ("にゃ", "ニャ", "nya"), ("にゅ", "ニュ", "nyu"), ("にょ", "ニョ", "nyo"),
    ("ひゃ", "ヒャ", "hya"), ("ひゅ", "ヒュ", "hyu"), ("ひょ", "ヒョ", "hyo"),
    ("みゃ", "ミャ", "mya"), ("みゅ", "ミュ", "myu"), ("みょ", "ミョ", "myo"),
    ("りゃ", "リャ", "rya"), ("りゅ", "リュ", "ryu"), ("りょ", "リョ", "ryo"),
    ("ぎゃ", "ギャ", "gya"), ("ぎゅ", "ギュ", "gyu"), ("ぎょ", "ギョ", "gyo"),
    ("じゃ", "ジャ", "ja"), ("じゅ", "ジュ", "ju"), ("じょ", "ジョ", "jo"),
    ("びゃ", "ビャ", "bya"), ("びゅ", "ビュ", "byu"), ("びょ", "ビョ", "byo"),
    ("ぴゃ", "ピャ", "pya"), ("ぴゅ", "ピュ", "pyu"), ("ぴょ", "ピョ", "pyo"),
]

# Katakana étendus pour les mots étrangers, d'après les deux tableaux de la
# notice gouvernementale de 1991 « 外来語の表記 » (第1表 : usage général,
# 第2表 : pour rester proche de la prononciation d'origine).
ETENDU = [
    ("シェ", "she", 1, "シェフ (chef)"), ("チェ", "che", 1, "チェス (échecs)"),
    ("ツァ", "tsa", 1, "モーツァルト (Mozart)"), ("ツェ", "tse", 1, "コンツェルン (Konzern)"),
    ("ツォ", "tso", 1, "カンツォーネ (canzone)"), ("ティ", "ti", 1, "パーティー (fête)"),
    ("ファ", "fa", 1, "ファン (fan)"), ("フィ", "fi", 1, "フィルム (film)"),
    ("フェ", "fe", 1, "カフェ (café)"), ("フォ", "fo", 1, "フォーク (fourchette)"),
    ("ジェ", "je", 1, "ジェット (jet)"), ("ディ", "di", 1, "ディスク (disque)"),
    ("デュ", "dyu", 1, "デュエット (duo)"),
    ("イェ", "ye", 2, "イェール (Yale)"), ("ウィ", "wi", 2, "ウィスキー (whisky)"),
    ("ウェ", "we", 2, "ウェディング (mariage)"), ("ウォ", "wo", 2, "ウォッカ (vodka)"),
    ("クァ", "kwa", 2, "クァルテット (quartette)"), ("クィ", "kwi", 2, "クィーン (queen)"),
    ("クェ", "kwe", 2, "クェスチョン (question)"), ("クォ", "kwo", 2, "クォーツ (quartz)"),
    ("ツィ", "tsi", 2, "ツィゴイネルワイゼン (Zigeunerweisen)"),
    ("トゥ", "tu", 2, "トゥデー (today)"), ("グァ", "gwa", 2, "グァテマラ (Guatemala)"),
    ("ドゥ", "du", 2, "ドゥ (do, it yourself)"), ("ヴァ", "va", 2, "ヴァイオリン (violon)"),
    ("ヴィ", "vi", 2, "ヴィーナス (Vénus)"), ("ヴ", "vu", 2, "ヴ (v)"),
    ("ヴェ", "ve", 2, "ヴェール (voile)"), ("ヴォ", "vo", 2, "ヴォルガ (Volga)"),
    ("テュ", "tyu", 2, "テューバ (tuba)"), ("フュ", "fyu", 2, "フュージョン (fusion)"),
    ("ヴュ", "vyu", 2, "インタヴュー (interview)"),
]

# Nombre de traits attendu pour les signes de base, saisi de mémoire d'après les
# tableaux d'écriture usuels (manuels scolaires japonais), pour recouper
# KanjiVG. Les variantes connues sont signalées dans VARIANTES.
ATTENDU = dict(zip(
    "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん",
    [3, 2, 2, 2, 3, 3, 4, 1, 3, 2, 3, 1, 2, 3, 1, 4, 2, 1, 1, 2, 4, 3, 2, 2, 1, 3, 1, 4, 1, 4,
     3, 2, 3, 2, 3, 3, 2, 2, 2, 2, 1, 2, 1, 2, 3, 1]))
ATTENDU.update(zip(
    "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン",
    [2, 2, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 4, 1, 2, 2, 1, 1, 4,
     2, 3, 2, 2, 3, 2, 2, 3, 2, 2, 2, 1, 3, 2, 3, 2]))
VARIANTES = {
    "き": "Souvent écrit en 3 traits dans les polices manuscrites (le bas attaché) ; KanjiVG et les manuels : 4.",
    "さ": "En police manuscrite le bas est parfois attaché (2 traits) ; KanjiVG et les manuels : 3.",
    "そ": "Certains manuels l'écrivent en 2 traits (le haut détaché) ; KanjiVG : 1.",
    "り": "Peut s'écrire en 1 trait en écriture rapide ; KanjiVG et les manuels : 2.",
    "ふ": "L'ordre du premier et du deuxième trait varie selon les manuels.",
}


def svg_de(car):
    return "traits/%05x.svg" % ord(car)


def traits_kanjivg(car):
    chemin = os.path.join(KANA, svg_de(car))
    if not os.path.exists(chemin):
        raise SystemExit("SVG KanjiVG absent pour %s (%s)" % (car, chemin))
    texte = open(chemin, encoding="utf-8").read()
    return len(re.findall(r'<path id="kvg:%05x-s\d+"' % ord(car), texte))


# --- Recoupement avec les noms Unicode -------------------------------------
KUNREI_VERS_HEPBURN = {"si": "shi", "ti": "chi", "tu": "tsu", "hu": "fu", "zi": "ji",
                       "di": "ji", "du": "zu", "wo": "o", "wi": "i", "we": "e"}


def romaji_unicode(car):
    """Romaji déduit du nom Unicode (ex. 'HIRAGANA LETTER SMALL TU' -> 'tsu')."""
    nom = unicodedata.name(car)
    m = re.match(r"(HIRAGANA|KATAKANA) LETTER (SMALL )?([A-Z]+)$", nom)
    if not m:
        raise SystemExit("Nom Unicode inattendu pour %s : %s" % (car, nom))
    r = m.group(3).lower()
    return KUNREI_VERS_HEPBURN.get(r, r), bool(m.group(2))


def romaji_compose(seq):
    """Romaji Hepburn d'une suite de kana, recalculé depuis les noms Unicode."""
    if len(seq) == 1:
        return romaji_unicode(seq)[0]
    tete, (petit, est_petit) = romaji_unicode(seq[0])[0], romaji_unicode(seq[1])
    assert est_petit, seq
    if petit in ("ya", "yu", "yo"):
        if tete in ("shi", "chi", "ji"):
            return tete[:-1] + petit[1]
        return tete[:-1] + petit
    # Katakana étendus : consonne de la tête + voyelle du petit signe.
    consonne = {"tsu": "ts", "fu": "f", "shi": "sh", "chi": "ch", "ji": "j", "te": "t",
                "de": "d", "to": "t", "do": "d", "u": "w", "i": "y", "vu": "v",
                "ku": "kw", "gu": "gw"}[tete]
    if petit == "yu":
        consonne = {"t": "ty", "d": "dy", "f": "fy", "v": "vy"}[consonne]
        petit = "u"
    return consonne + petit


ERREURS = []


def verifier(cond, message):
    if not cond:
        ERREURS.append(message)


def entree(signe, ecriture, romaji, categorie, groupe, gojuon=None, statut="courant", **extra):
    composants = list(signe)
    traits_par = [traits_kanjivg(c) for c in composants]
    e = {
        "id": "%s-%s" % (ecriture[0], extra.pop("id_romaji", None)
                          or (romaji if not romaji.startswith("(") else categorie)),
        "signe": signe,
        "ecriture": ecriture,
        "romaji": romaji,
        "categorie": categorie,
        "gojuon": gojuon,
        "traits": sum(traits_par),
        "composants": [{"signe": c, "unicode": "U+%04X" % ord(c), "traits": t, "svg": svg_de(c)}
                       for c, t in zip(composants, traits_par)],
        "groupe": groupe,
        "statut": statut,
    }
    e.update(extra)
    return e


def gojuon(consonne, voyelle):
    return {"gyo": GYO[consonne], "consonne": consonne or None,
            "dan": DAN[voyelle], "voyelle": voyelle}


def construire():
    signes = []
    # Groupes d'apprentissage : une rangée gojūon par groupe, de 3 à 5 signes.
    groupes_base = {"": 1, "k": 2, "s": 3, "t": 4, "n": 5, "h": 6, "m": 7, "y": 8, "r": 9, "w": 10}
    for ecriture, idx, pfx in (("hiragana", 1, "H"), ("katakana", 2, "K")):
        for ligne in BASE:
            consonne, rom = ligne[0], ligne[3]
            for i, car in enumerate(ligne[idx]):
                if car == "_":
                    continue
                v = VOYELLES[i]
                extra = {}
                statut = "courant"
                if car in "をヲ":
                    statut = "particule seulement"
                    extra["romaji_variante"] = "wo"
                    extra["id_romaji"] = "wo"
                    extra["note"] = ("Se prononce « o » aujourd'hui. を ne s'emploie plus que comme "
                                     "particule de l'objet direct ; ヲ est très rare en dehors de ce rôle."
                                     if car == "を" else
                                     "Quasi absent de l'usage moderne : on écrit オ. Enseigné pour "
                                     "compléter le tableau.")
                if car in "はへ":
                    extra["note"] = ("Employé comme particule, se lit « %s » (%s)."
                                     % (("wa", "わたしは") if car == "は" else ("e", "がっこうへ")))
                if car in VARIANTES:
                    extra["note_traits"] = VARIANTES[car]
                signes.append(entree(car, ecriture, rom[i], "base",
                                     "%s%02d" % (pfx, groupes_base[consonne]),
                                     gojuon(consonne, v), statut, **extra))
        n = "ん" if ecriture == "hiragana" else "ン"
        signes.append(entree(n, ecriture, "n", "base", "%s10" % pfx,
                             {"gyo": None, "consonne": "n", "dan": None, "voyelle": None},
                             note="Hors grille : seule consonne isolée du système. Devant b, p, m "
                                  "elle se prononce m (しんぶん shinbun ≈ shimbun)."))
        for consonne, hira, kata, rom, cat in DAKU:
            grp = "%s%d" % (pfx, {"g": 11, "z": 11, "d": 12, "b": 12, "p": 13}[consonne])
            for i, car in enumerate(hira if ecriture == "hiragana" else kata):
                extra = {}
                if car in "ぢづヂヅ":
                    extra["id_romaji"] = "di" if car in "ぢヂ" else "du"
                    extra["note"] = ("Se prononce comme %s. Rare : ne s'emploie que dans quelques "
                                     "mots (ex. はなぢ, つづく), où le son vient de ち/つ."
                                     % ("じ/ジ" if car in "ぢヂ" else "ず/ズ"))
                signes.append(entree(car, ecriture, rom[i], cat, grp,
                                     gojuon(consonne, VOYELLES[i]), **extra))
        for h, k, rom in YOON:
            signe = h if ecriture == "hiragana" else k
            tete = romaji_unicode(signe[0])[0]
            grp = 14 if tete in ("ki", "shi", "chi", "ni") else 15 if tete in ("hi", "mi", "ri") else 16
            signes.append(entree(signe, ecriture, rom, "yoon", "%s%d" % (pfx, grp),
                                 {"gyo": GYO[{"shi": "s", "chi": "t", "ji": "z"}.get(tete, tete[0])],
                                  "consonne": None, "dan": None, "voyelle": rom[-1],
                                  "note": "Yōon : pas de case propre, rattaché à la rangée de son "
                                          "premier signe."}))
    # Petit tsu et allongement.
    signes.append(entree("っ", "hiragana", "(consonne doublée)", "petit-tsu", "H17",
                         note="Petit つ : double la consonne qui suit (きって kitte). Pas de son propre ; "
                              "en Hepburn, devant ch on écrit tch (まっちゃ matcha)."))
    signes.append(entree("ッ", "katakana", "(consonne doublée)", "petit-tsu", "K17",
                         note="Petit ツ : même rôle que っ (ベッド beddo)."))
    signes.append(entree("ー", "katakana", "(voyelle longue)", "allongement", "K17",
                         note="Chōonpu : allonge la voyelle précédente (コーヒー kōhī). En Hepburn, macron "
                              "(ō). En hiragana on allonge en écrivant la voyelle (おかあさん) ; ー n'y "
                              "apparaît que dans l'écriture familière. À l'écrit vertical, le trait est "
                              "vertical."))
    for signe, rom, table, exemple in ETENDU:
        signes.append(entree(signe, "katakana", rom, "etendu", "K18" if table == 1 else "K19" if "ウ" in signe or "ヴ" in signe or "イ" in signe else "K20",
                             tableau_1991=table, exemple=exemple, id_romaji="ext-" + rom))
    for car, rom, var, ecr in (("ゐ", "i", "wi", "hiragana"), ("ゑ", "e", "we", "hiragana"),
                               ("ヰ", "i", "wi", "katakana"), ("ヱ", "e", "we", "katakana")):
        signes.append(entree(car, ecr, rom, "rare", "R", gojuon("w", "i" if rom == "i" else "e"),
                             "obsolète", romaji_variante=var, id_romaji=var,
                             note="Retiré de l'orthographe officielle en 1946 ; se prononce comme "
                                  "%s. Se voit encore dans des noms propres et des enseignes "
                                  "(ヱビス Yebisu, ニッカウヰスキー)." % ("い" if rom == "i" else "え")))
    return signes


def recouper(signes):
    for s in signes:
        sig = s["signe"]
        # 1. Traits : KanjiVG == tableau usuel (signes de base).
        if s["categorie"] == "base":
            verifier(ATTENDU.get(sig) == s["traits"],
                     "%s : %s traits dans KanjiVG, %s attendus" % (sig, s["traits"], ATTENDU.get(sig)))
        # 2. Dakuten = base + 2, handakuten = base + 1.
        if s["categorie"] in ("dakuten", "handakuten"):
            base = unicodedata.normalize("NFD", sig)[0]
            delta = 2 if s["categorie"] == "dakuten" else 1
            verifier(s["traits"] == traits_kanjivg(base) + delta,
                     "%s : %s traits, base %s + %s attendu" % (sig, s["traits"], base, delta))
        # 3. Romaji contre les noms Unicode.
        if not s["romaji"].startswith("("):
            r = romaji_compose(sig)
            verifier(r == s["romaji"], "%s : romaji %s, Unicode donne %s" % (sig, s["romaji"], r))
        # 4. Grille gojūon contre les noms Unicode.
        g = s["gojuon"]
        if g and g["voyelle"] and len(sig) == 1:
            nom = unicodedata.name(sig).split()[-1].lower()
            nom_c = nom[:-1]
            verifier(nom[-1] == g["voyelle"], "%s : voyelle %s, Unicode %s" % (sig, g["voyelle"], nom))
            verifier((g["consonne"] or "") == nom_c,
                     "%s : consonne %s, Unicode %s" % (sig, g["consonne"], nom))
    # 5. Comptes.
    def compte(cat, ecr=None):
        return sum(1 for s in signes if s["categorie"] in cat and (ecr is None or s["ecriture"] == ecr))
    for ecr in ("hiragana", "katakana"):
        verifier(compte(("base",), ecr) == 46, "%s : %d signes de base" % (ecr, compte(("base",), ecr)))
        verifier(compte(("dakuten", "handakuten"), ecr) == 25, "%s : dakuten" % ecr)
        verifier(compte(("yoon",), ecr) == 33, "%s : yōon" % ecr)
    verifier(compte(("etendu",)) == 33, "étendus : %d" % compte(("etendu",)))
    ids = [s["id"] for s in signes]
    verifier(len(ids) == len(set(ids)), "identifiants en double")
    verifier(len({(s["signe"]) for s in signes}) == len(signes), "signes en double")
    # Ordre Unicode == ordre gojūon à l'intérieur de chaque rangée de base.
    for ecr in ("hiragana", "katakana"):
        base = [s["signe"] for s in signes if s["ecriture"] == ecr and s["categorie"] == "base"
                and s["signe"] not in "んン"]
        for a, b in zip(base, base[1:]):
            verifier(ord(a) < ord(b), "ordre gojūon/Unicode rompu entre %s et %s" % (a, b))


GROUPES = [
    ("H01", "Hiragana — voyelles", "あ い う え お : les cinq sons sur lesquels tout le reste est bâti."),
    ("H02", "Hiragana — rangée K", "か き く け こ"),
    ("H03", "Hiragana — rangée S", "さ し す せ そ (し = shi : première irrégularité)."),
    ("H04", "Hiragana — rangée T", "た ち つ て と (ち = chi, つ = tsu)."),
    ("H05", "Hiragana — rangée N", "な に ぬ ね の"),
    ("H06", "Hiragana — rangée H", "は ひ ふ へ ほ (ふ = fu)."),
    ("H07", "Hiragana — rangée M", "ま み む め も"),
    ("H08", "Hiragana — rangée Y", "や ゆ よ : trois signes seulement."),
    ("H09", "Hiragana — rangée R", "ら り る れ ろ"),
    ("H10", "Hiragana — W et N", "わ を ん"),
    ("H11", "Hiragana — dakuten (1)", "が行, ざ行 : rien de nouveau à dessiner, deux petits traits rendent la consonne sonore (k → g, s → z)."),
    ("H12", "Hiragana — dakuten (2)", "だ行, ば行 (t → d, h → b). ぢ et づ : rares, se lisent ji et zu."),
    ("H13", "Hiragana — handakuten", "ぱ行 : le petit rond change h en p."),
    ("H14", "Hiragana — yōon (1)", "きゃ しゃ ちゃ にゃ et leurs ゅ ょ : un signe en -i + petit ゃ ゅ ょ."),
    ("H15", "Hiragana — yōon (2)", "ひゃ みゃ りゃ et leurs ゅ ょ."),
    ("H16", "Hiragana — yōon (3)", "ぎゃ じゃ びゃ ぴゃ et leurs ゅ ょ : combinaison de deux règles déjà vues."),
    ("H17", "Hiragana — petit っ", "La consonne doublée."),
    ("K01", "Katakana — voyelles", "ア イ ウ エ オ"),
    ("K02", "Katakana — rangée K", "カ キ ク ケ コ"),
    ("K03", "Katakana — rangée S", "サ シ ス セ ソ"),
    ("K04", "Katakana — rangée T", "タ チ ツ テ ト"),
    ("K05", "Katakana — rangée N", "ナ ニ ヌ ネ ノ"),
    ("K06", "Katakana — rangée H", "ハ ヒ フ ヘ ホ"),
    ("K07", "Katakana — rangée M", "マ ミ ム メ モ"),
    ("K08", "Katakana — rangée Y", "ヤ ユ ヨ"),
    ("K09", "Katakana — rangée R", "ラ リ ル レ ロ"),
    ("K10", "Katakana — W et N", "ワ ヲ ン"),
    ("K11", "Katakana — dakuten (1)", "ガ行, ザ行"),
    ("K12", "Katakana — dakuten (2)", "ダ行, バ行"),
    ("K13", "Katakana — handakuten", "パ行"),
    ("K14", "Katakana — yōon (1)", "キャ シャ チャ ニャ…"),
    ("K15", "Katakana — yōon (2)", "ヒャ ミャ リャ…"),
    ("K16", "Katakana — yōon (3)", "ギャ ジャ ビャ ピャ…"),
    ("K17", "Katakana — ッ et ー", "Consonne doublée et voyelle longue, omniprésentes dans les mots empruntés."),
    ("K18", "Katakana étendus — usage courant", "Tableau 1 de 1991 : ティ, ファ, シェ, ジェ…"),
    ("K19", "Katakana étendus — W, V, Y", "Tableau 2 de 1991 : ウィ ウェ ウォ, ヴァ ヴィ ヴ…, イェ."),
    ("K20", "Katakana étendus — autres sons étrangers", "Tableau 2 de 1991 : クァ, トゥ, ツィ, フュ… À voir quand on les rencontre."),
    ("R", "Signes rares (facultatif)", "ゐ ゑ ヰ ヱ : obsolètes, pour la culture."),
]


def main():
    signes = construire()
    recouper(signes)
    if ERREURS:
        print("ÉCHEC du recoupement :")
        for e in ERREURS:
            print("  -", e)
        sys.exit(1)
    doc = {
        "description": "Hiragana et katakana : romaji Hepburn, place dans le tableau gojūon, nombre "
                       "de traits (KanjiVG) et groupe d'apprentissage. Fichier généré par "
                       "outils/construire.py — ne pas modifier à la main.",
        "romanisation": "Hepburn modifié (を = o, ん = n, voyelles longues avec macron).",
        "sources": {
            "traits": "KanjiVG (https://kanjivg.tagaini.net/), CC BY-SA 3.0 — voir LICENCES.md",
            "recoupement": "Noms de caractères Unicode %s (module unicodedata de Python)"
                           % unicodedata.unidata_version,
        },
        "groupes": [{"id": g, "titre": t, "contenu": c,
                     "signes": [s["signe"] for s in signes if s["groupe"] == g]}
                    for g, t, c in GROUPES],
        "signes": signes,
    }
    with open(os.path.join(KANA, "kana.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    cats = {}
    for s in signes:
        cats[s["categorie"]] = cats.get(s["categorie"], 0) + 1
    print("kana.json : %d signes %s — recoupement OK" % (len(signes), cats))


if __name__ == "__main__":
    main()
