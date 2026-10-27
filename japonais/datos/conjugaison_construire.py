# -*- coding: utf-8 -*-
"""Construit japonais/datos/conjugaison.json : les feuilles de conjugaison du japonais.

    python japonais/datos/conjugaison_construire.py

LE MEME FORMAT QUE espanol/datos/conjugaison.json, lu par le meme moteur
(chargerFeuilles, preparerFeuille, insererFeuille, ouvrirMesFeuilles) : par
niveau, une liste ORDONNEE de feuilles { id, serie, temps, t, l, a }. Dans
la forme, [crochets] = la partie qui change, surlignee, et que la voix lit
sans les crochets ; l[2] = la lecture (kana · romaji), ecrite sous la forme.

`temps` reste nul : en allemand et en espagnol, il nomme le champ de la carte
de verbe d'ou vient une phrase « a remettre en ordre » -- un exercice qui
coupe la phrase a ses espaces, et le japonais n'en a pas.

LES FORMES NE SONT PAS ECRITES A LA MAIN : elles viennent de
japonais/datos/verbes.json et adjectifs.json, calculees par
japonais/conjugaison (le moteur teste contre ses oracles). Le crochet se pose
tout seul : la partie commune a la forme du dictionnaire reste en clair.

Ce script ajoute aussi a japonais/datos/exercices.json les series des
feuilles qui n'en avaient pas (forme en ない, en た, reconnaitre une forme),
calculees de la meme facon. Lancer exercices_construire.py AVANT ce script.

Brouillon : a faire relire par un natif.
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


def lire(nom):
    with io.open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def fe(fr, en):
    return {"fr": fr, "en": en}


VERBES = {}
for niv, liste in lire("verbes.json").items():
    if isinstance(liste, list):
        for v in liste:
            VERBES.setdefault(v["mot"], v)
ADJ = {}
for niv, liste in lire("adjectifs.json").items():
    if isinstance(liste, list):
        for a in liste:
            ADJ.setdefault(a["mot"], a)


def crochet(base, forme):
    """« 食べ[ます] » : la partie commune avec la forme de base reste en clair."""
    i = 0
    while i < min(len(base), len(forme)) and base[i] == forme[i]:
        i += 1
    if i == len(forme):
        return forme
    return forme[:i] + "[" + forme[i:] + "]"


def ligne_v(mot, cle, fr, en):
    v = VERBES[mot]
    f = v["formes"][cle]
    base = v["formes"]["dictionnaire"]["kanji"]
    kana = f["kana"]
    return [crochet(base, f["kanji"]), fe(fr, en), {"fr": kana + " · " + romaji(kana), "en": kana + " · " + romaji(kana)}]


def ligne_a(mot, cle, fr, en, oral=True):
    a = ADJ[mot]
    f = a["formes"][cle]
    k, kn = f["kanji"], f["kana"]
    if oral:
        k, kn = k.replace("ではな", "じゃな"), kn.replace("ではな", "じゃな")
    return [crochet(a["mot"], k), fe(fr, en), {"fr": kn + " · " + romaji(kn), "en": kn + " · " + romaji(kn)}]


def feuille(id_, serie, t, l, a):
    # Les crochets surlignent dans les lignes, pas dans le titre.
    t = {k: v.replace("[", "").replace("]", "") for k, v in t.items()}
    return {"id": id_, "serie": serie, "temps": None, "t": t, "l": l, "a": a}


A1 = [
    feuille("masu_groupe2", "masuJaExercises",
            fe("ます, groupe 2 : 食べ[ます]", "ます, group 2: 食べ[ます]"),
            [ligne_v("食べる", "masu", "je mange", "I eat"),
             ligne_v("食べる", "masen", "je ne mange pas", "I don't eat"),
             ligne_v("食べる", "mashita", "j'ai mangé", "I ate"),
             ligne_v("食べる", "masen_deshita", "je n'ai pas mangé", "I didn't eat"),
             ligne_v("見る", "masu", "je regarde", "I watch"),
             ligne_v("起きる", "mashita", "je me suis levé", "I got up")],
            fe("Les verbes en る après e ou i (groupe 2) : on enlève る, on ajoute ます. "
               "Les quatre fins valent pour tous les verbes : ます, ません, ました, ませんでした. "
               "Pas de personne : 食べます = je, tu, il, nous mangeons.",
               "ru-verbs after e or i (group 2): drop る, add ます. "
               "The four endings work for every verb: ます, ません, ました, ませんでした. "
               "No person: 食べます = I, you, he, we eat.")),
    feuille("masu_groupe1", "masuJaExercises",
            fe("ます, groupe 1 : 書[きます]", "ます, group 1: 書[きます]"),
            [ligne_v("書く", "masu", "j'écris", "I write"),
             ligne_v("飲む", "masu", "je bois", "I drink"),
             ligne_v("話す", "masu", "je parle", "I speak"),
             ligne_v("待つ", "masu", "j'attends", "I wait"),
             ligne_v("買う", "mashita", "j'ai acheté", "I bought"),
             ligne_v("帰る", "masen", "je ne rentre pas", "I'm not going home")],
            fe("Les autres verbes (groupe 1) : le dernier son passe de u à i, puis ます — "
               "く → き, む → み, す → し, つ → ち, う → い, る → り. "
               "Piège : 帰る, 入る, 知る finissent par る mais sont du groupe 1 (帰ります).",
               "The other verbs (group 1): the last sound moves from u to i, then ます — "
               "く → き, む → み, す → し, つ → ち, う → い, る → り. "
               "Trap: 帰る, 入る, 知る end in る but are group 1 (帰ります).")),
    feuille("masu_irreguliers", "masuJaExercises",
            fe("Les deux irréguliers : する et 来る", "The two irregulars: する and 来る"),
            [ligne_v("する", "masu", "je fais", "I do"),
             ligne_v("する", "mashita", "j'ai fait", "I did"),
             ligne_v("来る", "masu", "je viens", "I come"),
             ligne_v("来る", "masen", "je ne viens pas", "I don't come"),
             ligne_v("行く", "masu", "je vais", "I go"),
             ligne_v("行く", "mashita", "je suis allé", "I went")],
            fe("Seulement deux verbes irréguliers, et する en fabrique des centaines : "
               "勉強する (étudier) → 勉強します, 料理する (cuisiner) → 料理します. "
               "来る se lit く au dictionnaire mais き devant ます : 来ます (きます).",
               "Only two irregular verbs, and する builds hundreds more: "
               "勉強する (to study) → 勉強します, 料理する (to cook) → 料理します. "
               "来る reads く in the dictionary but き before ます: 来ます (kimasu).")),
    feuille("adjectifs_i", "adjectifsJaExercises",
            fe("Les adjectifs en い : 高[くない]", "い-adjectives: 高[くない]"),
            [ligne_a("高い", "present", "c'est cher", "it's expensive"),
             ligne_a("高い", "negatif", "ce n'est pas cher", "it's not expensive"),
             ligne_a("高い", "passe", "c'était cher", "it was expensive"),
             ligne_a("高い", "passe_negatif", "ce n'était pas cher", "it wasn't expensive"),
             ligne_a("いい", "negatif", "ce n'est pas bien", "it's not good"),
             ligne_a("いい", "passe", "c'était bien", "it was good")],
            fe("L'adjectif en い se conjugue lui-même : い → くない, かった, くなかった. "
               "Pour être poli, on ajoute です à la fin (高くないです). "
               "いい est irrégulier : il passe par よ (よくない, よかった).",
               "An い-adjective conjugates itself: い → くない, かった, くなかった. "
               "To be polite, add です at the end (高くないです). "
               "いい is irregular: it goes through よ (よくない, よかった).")),
    feuille("adjectifs_na", "adjectifsJaExercises",
            fe("Les adjectifs en な : 静か[じゃない]", "な-adjectives: 静か[じゃない]"),
            [ligne_a("静か", "present", "c'est calme", "it's quiet"),
             ligne_a("静か", "negatif", "ce n'est pas calme", "it's not quiet"),
             ligne_a("静か", "passe", "c'était calme", "it was quiet"),
             ligne_a("静か", "passe_negatif", "ce n'était pas calme", "it wasn't quiet"),
             ligne_a("元気", "present", "je vais bien", "I'm fine"),
             ligne_a("好き", "negatif", "je n'aime pas", "I don't like it")],
            fe("L'adjectif en な ne bouge pas : c'est だ (ou です) qui se conjugue, exactement comme après un nom. "
               "À l'écrit, じゃ devient では : 静かではない. Devant un nom : 静かな町.",
               "A な-adjective doesn't change: だ (or です) conjugates, exactly as after a noun. "
               "In writing, じゃ becomes では: 静かではない. Before a noun: 静かな町.")),
    feuille("te_1", "teJaExercises",
            fe("La forme en て (1) : 買[って], 飲[んで]", "The て-form (1): 買[って], 飲[んで]"),
            [ligne_v("買う", "te", "acheter", "buy"),
             ligne_v("待つ", "te", "attendre", "wait"),
             ligne_v("帰る", "te", "rentrer", "go home"),
             ligne_v("飲む", "te", "boire", "drink"),
             ligne_v("遊ぶ", "te", "jouer", "play"),
             ligne_v("死ぬ", "te", "mourir", "die")],
            fe("Groupe 1 : う, つ, る → って ; む, ぶ, ぬ → んで. "
               "La forme en て relie deux actions (買って、帰ります : j'achète puis je rentre) "
               "et sert à demander : 待ってください (attendez, s'il vous plaît).",
               "Group 1: う, つ, る → って; む, ぶ, ぬ → んで. "
               "The て-form links two actions (買って、帰ります: I buy and then go home) "
               "and makes requests: 待ってください (please wait).")),
    feuille("te_2", "teJaExercises",
            fe("La forme en て (2) : 書[いて], 話[して], 食べ[て]", "The て-form (2): 書[いて], 話[して], 食べ[て]"),
            [ligne_v("書く", "te", "écrire", "write"),
             ligne_v("泳ぐ", "te", "nager", "swim"),
             ligne_v("話す", "te", "parler", "speak"),
             ligne_v("行く", "te", "aller (l'exception)", "go (the exception)"),
             ligne_v("食べる", "te", "manger (groupe 2)", "eat (group 2)"),
             ligne_v("する", "te", "faire", "do"),
             ligne_v("来る", "te", "venir", "come")],
            fe("く → いて, ぐ → いで, す → して. Une seule exception : 行く → 行って. "
               "Groupe 2 : on remplace る par て (食べて, 見て). Et する → して, 来る → 来て (きて).",
               "く → いて, ぐ → いで, す → して. One single exception: 行く → 行って. "
               "Group 2: replace る with て (食べて, 見て). And する → して, 来る → 来て (kite).")),
    feuille("te_iru", "teJaExercises",
            fe("～ています et ～てください", "～ています and ～てください"),
            [ligne_v("食べる", "te_iru", "je suis en train de manger", "I'm eating"),
             ligne_v("待つ", "te_iru", "j'attends (en ce moment)", "I'm waiting"),
             ["待って[ください]", fe("attendez, s'il vous plaît", "please wait"), fe("まってください · matte kudasai", "まってください · matte kudasai")],
             ["見て[ください]", fe("regardez, s'il vous plaît", "please look"), fe("みてください · mite kudasai", "みてください · mite kudasai")],
             ["書いて[ください]", fe("écrivez, s'il vous plaît", "please write"), fe("かいてください · kaite kudasai", "かいてください · kaite kudasai")]],
            fe("Forme en て + います = une action en cours (今、食べています) ou un état (結婚しています : je suis marié). "
               "Forme en て + ください = une demande polie. À l'oral, ている devient souvent てる.",
               "て-form + います = an ongoing action (今、食べています) or a state (結婚しています: I'm married). "
               "て-form + ください = a polite request. In speech, ている often becomes てる.")),
]

A2 = [
    feuille("nai", "naiJaExercises",
            fe("La forme en ない : 書[かない]", "The ない-form: 書[かない]"),
            [ligne_v("書く", "nai", "ne pas écrire", "not write"),
             ligne_v("飲む", "nai", "ne pas boire", "not drink"),
             ligne_v("買う", "nai", "ne pas acheter", "not buy"),
             ligne_v("食べる", "nai", "ne pas manger", "not eat"),
             ligne_v("する", "nai", "ne pas faire", "not do"),
             ligne_v("来る", "nai", "ne pas venir", "not come")],
            fe("Le négatif familier. Groupe 1 : u → a, puis ない (書く → 書かない) ; う devient わ (買わない). "
               "Groupe 2 : る → ない. する → しない, 来る → 来ない (こない). Et ある → ない tout court.",
               "The casual negative. Group 1: u → a, then ない (書く → 書かない); う becomes わ (買わない). "
               "Group 2: る → ない. する → しない, 来る → 来ない (konai). And ある → just ない.")),
    feuille("ta", "taJaExercises",
            fe("La forme en た : le passé familier", "The た-form: the casual past"),
            [ligne_v("書く", "ta", "j'ai écrit", "I wrote"),
             ligne_v("飲む", "ta", "j'ai bu", "I drank"),
             ligne_v("買う", "ta", "j'ai acheté", "I bought"),
             ligne_v("食べる", "ta", "j'ai mangé", "I ate"),
             ligne_v("する", "ta", "j'ai fait", "I did"),
             ligne_v("行く", "ta", "je suis allé", "I went")],
            fe("Rien de neuf : c'est la forme en て, avec a. て → た, で → だ (飲んで → 飲んだ). "
               "Le négatif passé : ない → なかった (書かなかった).",
               "Nothing new: it's the て-form with a. て → た, で → だ (飲んで → 飲んだ). "
               "The past negative: ない → なかった (書かなかった).")),
    feuille("potentiel", "formesJaExercises",
            fe("Pouvoir : 書[ける], 食べ[られる]", "Can: 書[ける], 食べ[られる]"),
            [ligne_v("書く", "potentiel", "pouvoir écrire", "can write"),
             ligne_v("話す", "potentiel", "pouvoir parler", "can speak"),
             ligne_v("食べる", "potentiel", "pouvoir manger", "can eat"),
             ligne_v("来る", "potentiel", "pouvoir venir", "can come"),
             ["[できる]", fe("pouvoir faire (する)", "can do (する)"), fe("できる · dekiru", "できる · dekiru")]],
            fe("Groupe 1 : u → e, puis る (書ける). Groupe 2 : る → られる (食べられる ; à l'oral, souvent 食べれる). "
               "する devient できる, 来る → 来られる. Ce qu'on peut faire prend が : 日本語が話せます.",
               "Group 1: u → e, then る (書ける). Group 2: る → られる (食べられる; in speech often 食べれる). "
               "する becomes できる, 来る → 来られる. What you can do takes が: 日本語が話せます.")),
    feuille("volitif", "formesJaExercises",
            fe("Faisons ! : 書[こう], 食べ[よう]", "Let's!: 書[こう], 食べ[よう]"),
            [ligne_v("行く", "volitif", "allons-y", "let's go"),
             ligne_v("飲む", "volitif", "buvons", "let's drink"),
             ligne_v("食べる", "volitif", "mangeons", "let's eat"),
             ligne_v("する", "volitif", "faisons", "let's do it"),
             ligne_v("来る", "volitif", "venons", "let's come")],
            fe("La forme familière de ましょう. Groupe 1 : u → o + う (行こう). Groupe 2 : る → よう. "
               "する → しよう, 来る → 来よう (こよう). Avec と思う : 行こうと思う = je pense y aller.",
               "The casual form of ましょう. Group 1: u → o + う (行こう). Group 2: る → よう. "
               "する → しよう, 来る → 来よう (koyō). With と思う: 行こうと思う = I'm thinking of going.")),
    feuille("ba", "formesJaExercises",
            fe("Si… : 書[けば], 食べ[れば]", "If…: 書[けば], 食べ[れば]"),
            [ligne_v("行く", "ba", "si j'y vais", "if I go"),
             ligne_v("読む", "ba", "si je lis", "if I read"),
             ligne_v("食べる", "ba", "si je mange", "if I eat"),
             ligne_v("する", "ba", "si je fais", "if I do"),
             ligne_a("高い", "ba", "si c'est cher", "if it's expensive", oral=False)],
            fe("Le conditionnel en ば. Verbes : u → e, puis ば (行けば, 食べれば). Adjectifs en い : い → ければ (高ければ). "
               "Une autre façon, plus courante à l'oral : la forme en た + ら (行ったら).",
               "The ば-conditional. Verbs: u → e, then ば (行けば, 食べれば). い-adjectives: い → ければ (高ければ). "
               "Another way, more common in speech: the た-form + ら (行ったら).")),
]


# --- Les series des feuilles -------------------------------------------------
LIGNE_A = {"う": "わ", "く": "か", "ぐ": "が", "す": "さ", "つ": "た", "ぬ": "な", "ぶ": "ば", "む": "ま", "る": "ら"}
LIGNE_I = {"う": "い", "く": "き", "ぐ": "ぎ", "す": "し", "つ": "ち", "ぬ": "に", "ぶ": "び", "む": "み", "る": "り"}


def item(topic, question, fr, en, options, correct, hint, expl):
    assert correct in options and len(set(options)) == len(options), (question, options)
    return {"topic": topic, "question": question, "question_en": question,
            "translation": fr, "translation_en": en, "hint": hint[0], "hint_en": hint[1],
            "answers": [correct], "correct": correct, "correctEn": correct,
            "explanation": expl, "explanation_en": expl, "options": options, "optionsEn": options}


def melange(opts, graine):
    return sorted(opts, key=lambda s: (sum(map(ord, s + graine)) % 7, s))


H_NAI = ("(groupe 1 : u → a + ない, う → わない · groupe 2 : る → ない · する → しない · 来る → こない · ある → ない)",
         "(group 1: u → a + ない, う → わない · group 2: る → ない · する → しない · 来る → こない · ある → ない)")
H_TA = ("(comme la forme en て : って → った, んで → んだ, いて → いた, いで → いだ, して → した ; 行く → 行った)",
        "(like the て-form: って → った, んで → んだ, いて → いた, いで → いだ, して → した; 行く → 行った)")
H_FORMES = ("(～ける / ～られる pouvoir · ～こう / ～よう faisons · ～けば / ～れば si · ～かない ne pas · ～いた / ～った passé)",
            "(～ける / ～られる can · ～こう / ～よう let's · ～けば / ～れば if · ～かない not · ～いた / ～った past)")


def verbes_series():
    nai, ta, formes = [], [], []
    noms = [v for v in VERBES.values() if v.get("jlpt") in ("N5", "N4") and v.get("formes")]
    for k, v in enumerate(noms):
        cl, f = v["classe"], v["formes"]
        dico = f["dictionnaire"]["kanji"]
        rad, fin = dico[:-1], dico[-1:]
        # ない
        if f.get("nai") and cl not in ("vs-i", "vk", "vs-s", "vz") and not dico.endswith("する"):
            bon = f["nai"]["kanji"]
            if cl == "v1":
                faux = [rad + "らない", dico + "ない"]
            elif cl == "v5r-i":
                faux = [rad + "らない", dico + "ない"]
            elif fin in LIGNE_I:
                faux = [rad + LIGNE_I[fin] + "ない", dico + "ない"]
                if fin == "う":
                    faux[1] = rad + "あない"
            else:
                faux = []
            faux = [x for x in faux if x != bon]
            if len(faux) == 2 and len(nai) < 60:
                nai.append(item("forme en ない", dico + " → ___", "%s : ne pas…" % v["traduction"],
                                "%s: not…" % v["traduction_en"], melange([bon] + faux, dico), bon, H_NAI,
                                "%s → %s (%s)" % (dico, bon, f["nai"]["kana"])))
        # た
        if f.get("ta") and f.get("te") and cl not in ("vs-i", "vk"):
            bon = f["ta"]["kanji"]
            fins = ["った", "んだ", "いた", "いだ", "した", "た"]
            faux = [rad + x for x in fins if rad + x != bon]
            if cl == "v1":
                faux = [rad + "った", rad + "んだ"]
            elif cl == "v5r":
                faux = [rad + "た", rad + "んだ"]
            faux = [x for x in faux if x != bon][:2]
            if len(faux) == 2 and len(ta) < 60:
                ta.append(item("forme en た", dico + " → ___", "%s : le passé familier" % v["traduction"],
                               "%s: casual past" % v["traduction_en"], melange([bon] + faux, dico), bon, H_TA,
                               "%s → %s (%s)" % (dico, bon, f["ta"]["kana"])))
        # Reconnaitre la forme
        cles = [("potentiel", "pouvoir", "can"), ("volitif", "« faisons »", "“let's”"),
                ("ba", "si…", "if…"), ("nai", "ne pas…", "not…"), ("ta", "passé", "past")]
        cle, fr, en = cles[k % len(cles)]
        if f.get(cle) and cl not in ("vs-i", "vk") and len(formes) < 60:
            autres = [c for c in cles if c[0] != cle][:2] if k % 2 else [c for c in cles if c[0] != cle][2:4]
            forme = f[cle]["kanji"]
            formes.append({"topic": "formes", "question": forme + " : ___", "question_en": forme + " : ___",
                           "translation": "%s (%s) — quelle forme ?" % (dico, v["traduction"]),
                           "translation_en": "%s (%s) — which form?" % (dico, v["traduction_en"]),
                           "hint": H_FORMES[0], "hint_en": H_FORMES[1],
                           "answers": [fr], "correct": fr, "correctEn": en,
                           "explanation": "%s → %s (%s)" % (dico, forme, f[cle]["kana"]),
                           "explanation_en": "%s → %s (%s)" % (dico, forme, f[cle]["kana"]),
                           "options": melange([fr] + [c[1] for c in autres], dico),
                           "optionsEn": melange([en] + [c[2] for c in autres], dico)})
    return nai, ta, formes


def main():
    sortie = {"_lisez_moi": "Derive de japonais/datos/conjugaison_construire.py : ne pas modifier a la main. "
                            "Formes calculees par japonais/conjugaison ; brouillon a faire relire par un natif.",
              "niveaux": {"A1": A1, "A2": A2}}
    with io.open(os.path.join(ICI, "conjugaison.json"), "w", encoding="utf-8", newline="\n") as fo:
        json.dump(sortie, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    exos = lire("exercices.json")
    nai, ta, formes = verbes_series()
    exos["jeux"]["naiJaExercises"] = nai
    exos["jeux"]["taJaExercises"] = ta
    exos["jeux"]["formesJaExercises"] = formes
    with io.open(os.path.join(ICI, "exercices.json"), "w", encoding="utf-8", newline="\n") as fo:
        json.dump(exos, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    series = {f["serie"] for n in sortie["niveaux"].values() for f in n}
    manque = [s for s in series if not exos["jeux"].get(s)]
    assert not manque, manque
    print("feuilles A1 %d, A2 %d ; series ない %d, た %d, formes %d" % (len(A1), len(A2), len(nai), len(ta), len(formes)))


if __name__ == "__main__":
    main()
