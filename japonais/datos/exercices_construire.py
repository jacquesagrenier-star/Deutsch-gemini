# -*- coding: utf-8 -*-
"""Construit japonais/datos/exercices.json : les series d'exercices du japonais (N5).

    python japonais/datos/exercices_construire.py

LE MEME FORMAT QUE espanol/datos/ejercicios.json (« jeux » : nom -> liste
d'items), lu par le meme moteur (jeu(), startExerciseSet). Un item : une
phrase a trou (question, « ___ »), sa traduction, un indice, les options, la
bonne reponse et l'explication -- en francais et en anglais (le japonais ne
s'apprend qu'en fr et en, decision du 4 oct. 2026).

Deux sortes de series :
  - ECRITES A LA MAIN (particules, ます, こそあど, questions, あります/います) :
    phrases N5 courtes, une seule bonne reponse possible ;
  - CALCULEES (forme en て, adjectifs) a partir des formes de
    japonais/datos/verbes.json et adjectifs.json, elles-memes calculees par
    japonais/conjugaison : les leurres sont les fautes qu'on fait vraiment
    (んで pour って, 静かくない pour 静かじゃない).

Brouillon : a faire relire par un natif.
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))


def lire(nom):
    with io.open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def item(topic, question, fr, en, options, correct, hint_fr, hint_en, expl_fr, expl_en):
    assert correct in options, (question, correct, options)
    assert len(set(options)) == len(options), options
    assert "___" in question, question
    return {
        "topic": topic, "question": question, "question_en": question,
        "translation": fr, "translation_en": en,
        "hint": hint_fr, "hint_en": hint_en,
        "answers": [correct], "correct": correct, "correctEn": correct,
        "explanation": expl_fr, "explanation_en": expl_en,
        "options": options, "optionsEn": options,
    }


# --- Les particules --------------------------------------------------------
H_PART = ("(は thème · が sujet · を objet · に arrivée, heure · で lieu de l'action, moyen · へ direction · と avec, et · の de · も aussi · か question)",
          "(は topic · が subject · を object · に destination, time · で place of action, means · へ direction · と with, and · の of · も also · か question)")
PARTICULES = [
    ("わたし___学生です。", "Je suis étudiant.", "I'm a student.", "は", ["は", "を", "に"],
     "Le thème de la phrase : « moi, je… ».", "The topic of the sentence: “as for me…”."),
    ("パン___食べます。", "Je mange du pain.", "I eat bread.", "を", ["を", "に", "で"],
     "Ce qu'on mange : l'objet, を.", "What you eat: the object, を."),
    ("学校___行きます。", "Je vais à l'école.", "I go to school.", "に", ["に", "を", "で"],
     "Où l'on arrive : に (へ irait aussi).", "Where you arrive: に (へ would also work)."),
    ("としょかん___本を読みます。", "Je lis un livre à la bibliothèque.", "I read a book at the library.", "で", ["で", "に", "を"],
     "Le lieu où l'on FAIT quelque chose : で.", "The place where you DO something: で."),
    ("バス___行きます。", "J'y vais en bus.", "I go by bus.", "で", ["で", "を", "が"],
     "Le moyen : で.", "The means: で."),
    ("七時___起きます。", "Je me lève à 7 h.", "I get up at 7.", "に", ["に", "で", "を"],
     "Une heure précise : に.", "A precise time: に."),
    ("友だち___えいがを見ました。", "J'ai vu un film avec un ami.", "I saw a film with a friend.", "と", ["と", "を", "の"],
     "Avec qui : と.", "With whom: と."),
    ("これはわたし___かばんです。", "C'est mon sac.", "This is my bag.", "の", ["の", "は", "と"],
     "Relier deux noms, « le sac de moi » : の.", "Linking two nouns, “the bag of me”: の."),
    ("マルクさんはカナダ人です。わたし___カナダ人です。", "Mark est Canadien. Moi aussi, je suis Canadien.", "Mark is Canadian. I'm Canadian too.", "も", ["も", "は", "が"],
     "« Aussi » : も, à la place de は.", "“Also”: も, in place of は."),
    ("アンナさんは先生です___。", "Anna est-elle professeur ?", "Is Anna a teacher?", "か", ["か", "の", "ね"],
     "La question : か à la fin.", "The question: か at the end."),
    ("だれ___来ましたか。", "Qui est venu ?", "Who came?", "が", ["が", "は", "を"],
     "Après un mot interrogatif, toujours が.", "After a question word, always が."),
    ("ねこ___すきです。", "J'aime les chats.", "I like cats.", "が", ["が", "を", "に"],
     "すき : ce qu'on aime prend が.", "すき: the liked thing takes が."),
    ("へや___ねこがいます。", "Il y a un chat dans la chambre.", "There's a cat in the room.", "に", ["に", "で", "を"],
     "Où se trouve quelque chose (いる, ある) : に.", "Where something is (いる, ある): に."),
    ("日本語___わかります。", "Je comprends le japonais.", "I understand Japanese.", "が", ["が", "を", "で"],
     "わかる : ce qu'on comprend prend が.", "わかる: what you understand takes が."),
    ("コーヒー___飲みますか。", "Tu bois du café ?", "Do you drink coffee?", "を", ["を", "が", "で"],
     "Ce qu'on boit : l'objet, を.", "What you drink: the object, を."),
    ("えき___バスにのります。", "Je prends le bus à la gare.", "I take the bus at the station.", "で", ["で", "を", "が"],
     "Le lieu où l'on fait l'action : で.", "The place where the action happens: で."),
    ("九時___五時まではたらきます。", "Je travaille de 9 h à 17 h.", "I work from 9 to 5.", "から", ["から", "まで", "に"],
     "« Depuis » : から ; « jusqu'à » : まで.", "“From”: から; “until”: まで."),
    ("にく___さかなも食べません。", "Je ne mange ni viande ni poisson.", "I eat neither meat nor fish.", "も", ["も", "と", "を"],
     "A も B も + négatif = ni A ni B.", "A も B も + negative = neither A nor B."),
    ("りんご___バナナを買いました。", "J'ai acheté des pommes et des bananes.", "I bought apples and bananas.", "と", ["と", "の", "で"],
     "« Et » entre deux noms : と.", "“And” between two nouns: と."),
    ("日本___行きたいです。", "Je veux aller au Japon.", "I want to go to Japan.", "に", ["に", "で", "を"],
     "La destination : に.", "The destination: に."),
    ("きょう___いい天気ですね。", "Il fait beau aujourd'hui.", "Nice weather today, isn't it?", "は", ["は", "に", "を"],
     "Le moment dont on parle, en thème : きょうは (jamais きょうに).", "The time we're talking about, as topic: きょうは (never きょうに)."),
    ("先生___本をもらいました。", "J'ai reçu un livre du professeur.", "I got a book from the teacher.", "に", ["に", "で", "が"],
     "De qui l'on reçoit : に (ou から).", "Who you receive from: に (or から)."),
    ("はし___食べます。", "Je mange avec des baguettes.", "I eat with chopsticks.", "で", ["で", "と", "を"],
     "L'outil : で. と voudrait dire « en compagnie de ».", "The tool: で. と would mean “together with”."),
    ("それはなんです___。", "Qu'est-ce que c'est ?", "What's that?", "か", ["か", "は", "の"],
     "La question : か.", "The question: か."),
]

# --- Les formes en ます ----------------------------------------------------
H_MASU = ("(～ます présent, futur · ～ません négatif · ～ました passé · ～ませんでした passé négatif · ～ませんか invitation · ～ましょう « faisons »)",
          "(～ます present, future · ～ません negative · ～ました past · ～ませんでした past negative · ～ませんか invitation · ～ましょう “let's”)")
MASU = [
    ("まいにち、コーヒーを___。", "Je bois du café tous les jours.", "I drink coffee every day.", "飲みます", ["飲みます", "飲みました", "飲みません"],
     "Une habitude : le présent.", "A habit: the present."),
    ("きのう、テレビを___。", "Hier, je n'ai pas regardé la télé.", "Yesterday I didn't watch TV.", "見ませんでした", ["見ませんでした", "見ません", "見ました"],
     "Hier + négatif : passé négatif.", "Yesterday + negative: past negative."),
    ("あした、東京に___。", "Demain, j'irai à Tokyo.", "Tomorrow I'll go to Tokyo.", "行きます", ["行きます", "行きました", "行きませんでした"],
     "Le futur se dit au présent.", "The future uses the present."),
    ("けさ、六時に___。", "Ce matin, je me suis levé à 6 h.", "This morning I got up at 6.", "起きました", ["起きました", "起きます", "起きません"],
     "けさ (ce matin) : passé.", "けさ (this morning): past."),
    ("わたしはおさけを___。", "Je ne bois pas d'alcool.", "I don't drink alcohol.", "飲みません", ["飲みません", "飲みませんでした", "飲みます"],
     "Une habitude au négatif.", "A habit, negative."),
    ("いっしょにひるごはんを___。", "Tu ne veux pas déjeuner avec moi ?", "Won't you have lunch with me?", "食べませんか", ["食べませんか", "食べましたか", "食べません"],
     "Une invitation : ～ませんか.", "An invitation: ～ませんか."),
    ("じゃあ、___。", "Bon, allons-y.", "Well, let's go.", "行きましょう", ["行きましょう", "行きました", "行きません"],
     "« Faisons » : ～ましょう.", "“Let's”: ～ましょう."),
    ("せんしゅう、友だちに___。", "La semaine dernière, j'ai vu un ami.", "Last week I met a friend.", "会いました", ["会いました", "会います", "会いません"],
     "せんしゅう : passé.", "せんしゅう: past."),
    ("きょうは、べんきょう___。", "Aujourd'hui, je n'étudie pas.", "I'm not studying today.", "しません", ["しません", "しました", "します"],
     "する → します, しません.", "する → します, しません."),
    ("きのう、ともだちがうちに___。", "Hier, un ami est venu chez moi.", "Yesterday a friend came to my place.", "来ました", ["来ました", "来ます", "来ませんでした"],
     "来る → 来ます (きます), 来ました.", "来る → 来ます (kimasu), 来ました."),
    ("ゆうべ、よく___。", "Je n'ai pas bien dormi cette nuit.", "I didn't sleep well last night.", "ねませんでした", ["ねませんでした", "ねません", "ねました"],
     "ゆうべ (hier soir) + négatif.", "ゆうべ (last night) + negative."),
    ("まいばん、日本語を___。", "J'étudie le japonais tous les soirs.", "I study Japanese every evening.", "べんきょうします", ["べんきょうします", "べんきょうしました", "べんきょうしません"],
     "Une habitude : présent.", "A habit: present."),
    ("らいねん、日本に___。", "L'année prochaine, j'irai au Japon.", "Next year I'll go to Japan.", "行きます", ["行きます", "行きました", "行きませんでした"],
     "らいねん : futur, donc présent.", "らいねん: future, so present."),
    ("さっき、メールを___。", "Je viens d'écrire un courriel.", "I wrote an email a moment ago.", "書きました", ["書きました", "書きます", "書きません"],
     "さっき (tout à l'heure) : passé.", "さっき (a moment ago): past."),
]

# --- こそあど --------------------------------------------------------------
H_KO = ("(こ près de moi · そ près de toi · あ loin des deux · ど question ; これ seul, この + nom, ここ lieu)",
        "(こ near me · そ near you · あ far from both · ど question; これ alone, この + noun, ここ place)")
KOSOADO = [
    ("___はなんですか。(l'objet est dans ta main)", "Qu'est-ce que c'est, ça ? (dans ta main)", "What's that? (in your hand)", "それ", ["それ", "これ", "あれ"],
     "Près de la personne à qui l'on parle : そ.", "Near the listener: そ."),
    ("___本はわたしのです。(je le tiens)", "Ce livre-ci est à moi.", "This book is mine.", "この", ["この", "これ", "ここ"],
     "Devant un nom : この, pas これ.", "Before a noun: この, not これ."),
    ("トイレは___ですか。", "Où sont les toilettes ?", "Where's the toilet?", "どこ", ["どこ", "どれ", "どの"],
     "Un lieu, en question : どこ.", "A place, as a question: どこ."),
    ("___はえきです。(le bâtiment, loin de nous deux)", "Là-bas, c'est la gare.", "That over there is the station.", "あれ", ["あれ", "それ", "これ"],
     "Loin de nous deux : あ.", "Far from both of us: あ."),
    ("___人はだれですか。(la personne là-bas)", "Qui est cette personne là-bas ?", "Who's that person over there?", "あの", ["あの", "あれ", "あそこ"],
     "Devant un nom : あの.", "Before a noun: あの."),
    ("___に座ってください。(à côté de moi)", "Asseyez-vous ici.", "Please sit here.", "ここ", ["ここ", "これ", "この"],
     "Un lieu près de moi : ここ.", "A place near me: ここ."),
    ("___かさがあなたのですか。", "Quel parapluie est le tien ?", "Which umbrella is yours?", "どの", ["どの", "どれ", "どこ"],
     "« Quel » + nom : どの.", "“Which” + noun: どの."),
    ("あなたのかばんは___ですか。", "Lequel est ton sac ?", "Which one is your bag?", "どれ", ["どれ", "どの", "どこ"],
     "« Lequel » seul : どれ.", "“Which one” alone: どれ."),
    ("___は 1000円です。(tu tiens l'objet)", "Ça, c'est 1 000 yens.", "That one is 1,000 yen.", "それ", ["それ", "その", "そこ"],
     "Seul, près de toi : それ.", "Alone, near you: それ."),
    ("コンビニは___です。(loin, on montre du doigt)", "La supérette, c'est là-bas.", "The convenience store is over there.", "あそこ", ["あそこ", "あれ", "あの"],
     "Un lieu loin : あそこ.", "A far place: あそこ."),
]

# --- Les questions ---------------------------------------------------------
H_Q = ("(なに / なん quoi · だれ qui · どこ où · いつ quand · いくら combien · どうして pourquoi · どう comment)",
       "(なに / なん what · だれ who · どこ where · いつ when · いくら how much · どうして why · どう how)")
QUESTIONS = [
    ("これは___ですか。— ペンです。", "Qu'est-ce que c'est ? — Un stylo.", "What's this? — A pen.", "なん", ["なん", "だれ", "どこ"],
     "Une chose : なん (なに devient なん devant です).", "A thing: なん (なに becomes なん before です)."),
    ("あの人は___ですか。— 先生です。", "Qui est-ce ? — C'est le professeur.", "Who's that? — The teacher.", "だれ", ["だれ", "なん", "いつ"],
     "Une personne : だれ.", "A person: だれ."),
    ("___に住んでいますか。— 東京です。", "Où habites-tu ? — À Tokyo.", "Where do you live? — In Tokyo.", "どこ", ["どこ", "いつ", "だれ"],
     "Un lieu : どこ.", "A place: どこ."),
    ("___日本に来ましたか。— 先月です。", "Quand es-tu venu au Japon ? — Le mois dernier.", "When did you come to Japan? — Last month.", "いつ", ["いつ", "どこ", "いくら"],
     "Un moment : いつ.", "A time: いつ."),
    ("このシャツは___ですか。— 3000円です。", "Combien coûte cette chemise ? — 3 000 yens.", "How much is this shirt? — 3,000 yen.", "いくら", ["いくら", "いつ", "なん"],
     "Un prix : いくら.", "A price: いくら."),
    ("___行きませんか。— いそがしいからです。", "Pourquoi tu n'y vas pas ? — Parce que je suis occupé.", "Why aren't you going? — Because I'm busy.", "どうして", ["どうして", "どう", "どこ"],
     "Une raison : どうして.", "A reason: どうして."),
    ("日本の生活は___ですか。— たのしいです。", "Comment est la vie au Japon ? — Agréable.", "How's life in Japan? — Fun.", "どう", ["どう", "どうして", "なん"],
     "« Comment c'est ? » : どう.", "“How is it?”: どう."),
    ("いま___時ですか。— 三時です。", "Quelle heure est-il ? — 3 h.", "What time is it? — 3 o'clock.", "なん", ["なん", "いつ", "いくら"],
     "なん + compteur : なん時, なん人, なん月.", "なん + counter: なん時, なん人, なん月."),
    ("きょうは___曜日ですか。— 水曜日です。", "Quel jour sommes-nous ? — Mercredi.", "What day is it? — Wednesday.", "なん", ["なん", "いつ", "どこ"],
     "Le jour de la semaine : なん曜日.", "The day of the week: なん曜日."),
    ("ごかぞくは___人ですか。— 四人です。", "Vous êtes combien dans votre famille ? — Quatre.", "How many in your family? — Four.", "なん", ["なん", "いくら", "だれ"],
     "Combien de personnes : なん人.", "How many people: なん人."),
]

# --- あります / います -----------------------------------------------------
H_AI = ("(あります pour les choses et les plantes · います pour les personnes et les animaux ; le lieu prend に)",
        "(あります for things and plants · います for people and animals; the place takes に)")
ARU_IRU = [
    ("つくえの上に本が___。", "Il y a un livre sur le bureau.", "There's a book on the desk.", "あります", ["あります", "います"],
     "Un livre est une chose : あります.", "A book is a thing: あります."),
    ("こうえんに子どもが___。", "Il y a des enfants dans le parc.", "There are children in the park.", "います", ["います", "あります"],
     "Des personnes : います.", "People: います."),
    ("いえにねこが___。", "Il y a un chat à la maison.", "There's a cat at home.", "います", ["います", "あります"],
     "Un animal : います.", "An animal: います."),
    ("えきの前にコンビニが___。", "Il y a une supérette devant la gare.", "There's a convenience store in front of the station.", "あります", ["あります", "います"],
     "Un magasin : あります.", "A shop: あります."),
    ("きょうだいが___か。", "Tu as des frères et sœurs ?", "Do you have siblings?", "います", ["います", "あります"],
     "Des personnes : います (« avoir » des frères = il y a).", "People: います (“to have” siblings = there are)."),
    ("あしたじかんが___か。", "Tu as du temps demain ?", "Do you have time tomorrow?", "あります", ["あります", "います"],
     "Le temps est une chose : あります.", "Time is a thing: あります."),
    ("にわに木が___。", "Il y a un arbre dans le jardin.", "There's a tree in the garden.", "あります", ["あります", "います"],
     "Une plante ne bouge pas seule : あります.", "A plant doesn't move by itself: あります."),
    ("先生はきょうしつに___。", "Le professeur est dans la salle de classe.", "The teacher is in the classroom.", "います", ["います", "あります"],
     "Une personne : います.", "A person: います."),
    ("れいぞうこにたまごが___。", "Il n'y a pas d'œufs dans le frigo.", "There are no eggs in the fridge.", "ありません", ["ありません", "いません", "あります"],
     "Une chose, au négatif : ありません.", "A thing, negative: ありません."),
    ("へやにだれも___。", "Il n'y a personne dans la pièce.", "There's nobody in the room.", "いません", ["いません", "ありません", "います"],
     "Personne (だれも) : います au négatif.", "Nobody (だれも): います in the negative."),
]

# --- La forme en て, calculee -----------------------------------------------
H_TE = ("(う・つ・る → って · む・ぶ・ぬ → んで · く → いて · ぐ → いで · す → して · groupe 2 : る → て · 行く → 行って)",
        "(う・つ・る → って · む・ぶ・ぬ → んで · く → いて · ぐ → いで · す → して · group 2: る → て · 行く → 行って)")
FINS_TE = ["って", "んで", "いて", "いで", "して", "て"]


def te_items(verbes):
    out = []
    for v in verbes:
        cl, f = v.get("classe", ""), v.get("formes") or {}
        if cl in ("vk", "vs-i") or not f.get("te") or not f.get("dictionnaire"):
            continue
        dico, te = f["dictionnaire"]["kanji"], f["te"]["kanji"]
        radical = dico[:-1]
        if not te.startswith(radical):
            continue
        faux = []
        for fin in FINS_TE:
            x = radical + fin
            if x != te and x not in faux:
                faux.append(x)
        # Les leurres les plus vraisemblables d'abord : groupe 2 contre groupe 1.
        if cl == "v1":
            faux = [radical + "って", radical + "んで"]
        elif cl == "v5r":
            faux = [radical + "て", radical + "んで"]
        elif cl in ("v5k", "v5k-s"):
            faux = [x for x in (radical + "いて", radical + "って", radical + "んで") if x != te][:2]
        else:
            faux = faux[:2]
        opts = [te] + faux[:2]
        groupe = "groupe 2" if cl == "v1" else "groupe 1"
        out.append(item("forme en て", dico + " → ___",
                        "%s : la forme en て (%s)" % (v["traduction"], groupe),
                        "%s: the て-form (%s)" % (v["traduction_en"], groupe.replace("groupe", "group")),
                        sorted(opts, key=lambda s: (sum(map(ord, s + dico)) % 7, s)), te, H_TE[0], H_TE[1],
                        "%s → %s (%s)" % (dico, te, f["te"]["kana"]), "%s → %s (%s)" % (dico, te, f["te"]["kana"])))
    return out


# --- Les adjectifs, calcules ------------------------------------------------
H_ADJ = ("(い : 高い → 高くない, 高かった, 高くなかった · な : 静か → 静かじゃない, 静かだった, 静かじゃなかった · いい → よくない)",
         "(い: 高い → 高くない, 高かった, 高くなかった · な: 静か → 静かじゃない, 静かだった, 静かじゃなかった · いい → よくない)")
FORMES_ADJ = [("negatif", "négatif", "negative"), ("passe", "passé", "past"), ("passe_negatif", "passé négatif", "past negative")]


def adj_items(adjectifs):
    out = []
    for k, a in enumerate(adjectifs):
        t, f = a.get("type"), a.get("formes") or {}
        if t not in ("i", "na") or not f.get("present"):
            continue
        cle, fr, en = FORMES_ADJ[k % 3]
        bon = f.get(cle, {}).get("kanji")
        if not bon:
            continue
        base = a["mot"]
        if t == "i":
            r = base[:-1]
            if base == "いい":
                r = "よ"
            fautes = {"negatif": [base + "じゃない", r + "かった"],
                      "passe": [base + "だった", r + "くない"],
                      "passe_negatif": [base + "じゃなかった", r + "くない"]}[cle]
        else:
            # Les formes calculees ecrivent では ; l'oral dit じゃ. La bonne
            # reponse prend la forme parlee, comme la fiche.
            bon = bon.replace("ではな", "じゃな")
            fautes = {"negatif": [base + "くない", base + "だった"],
                      "passe": [base + "かった", base + "じゃない"],
                      "passe_negatif": [base + "くなかった", base + "じゃない"]}[cle]
        opts = [bon] + [x for x in fautes if x != bon][:2]
        if len(set(opts)) < 3:
            continue
        famille = "adjectif en い" if t == "i" else "adjectif en な"
        out.append(item("adjectifs", "%s → %s : ___" % (base, fr),
                        "%s (%s) : %s" % (a["traduction"], famille, fr),
                        "%s (%s): %s" % (a["traduction_en"], famille.replace("adjectif en", "").strip() + "-adjective", en),
                        sorted(opts, key=lambda s: (sum(map(ord, s + base)) % 5, s)), bon, H_ADJ[0], H_ADJ[1],
                        "%s → %s" % (base, bon), "%s → %s" % (base, bon)))
    return out


def serie(liste, topic, h):
    return [item(topic, q, fr, en, opts, c, h[0], h[1], ef, ee) for q, fr, en, c, opts, ef, ee in liste]


def main():
    verbes = lire("verbes.json")["A1"]
    adjectifs = lire("adjectifs.json")["A1"]
    jeux = {
        "particulesJaExercises": serie(PARTICULES, "particules", H_PART),
        "masuJaExercises": serie(MASU, "formes en ます", H_MASU),
        "kosoadoJaExercises": serie(KOSOADO, "こそあど", H_KO),
        "questionsJaExercises": serie(QUESTIONS, "questions", H_Q),
        "aruIruJaExercises": serie(ARU_IRU, "あります / います", H_AI),
        "teJaExercises": te_items(verbes),
        "adjectifsJaExercises": adj_items(adjectifs),
    }
    chemin = os.path.join(ICI, "exercices.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as fo:
        json.dump({"_note": "Derive de japonais/datos/exercices_construire.py : ne pas modifier a la main. Brouillon.",
                   "jeux": jeux}, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    print(", ".join("%s %d" % (k, len(v)) for k, v in jeux.items()), "->", os.path.relpath(chemin))


if __name__ == "__main__":
    main()
