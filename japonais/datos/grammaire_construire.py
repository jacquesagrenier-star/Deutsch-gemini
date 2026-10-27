# -*- coding: utf-8 -*-
"""Construit japonais/datos/grammaire.json : les fiches de grammaire du japonais (N5).

    python japonais/datos/grammaire_construire.py

LE MEME FORMAT QUE espanol/datos/grammaire.json, lu par le meme moteur
(chargerCours, abrirGramatica, abrirIndiceGramatica dans index.html) :

  - `textes` : verse dans I18N au chargement -- vide ici, le japonais n'a pas
    les ecrans de grammaire allemands ;
  - `fiches` : une fiche = titre, resume, regle (HTML : <b> seulement),
    tableau (lignes [forme, sens, exemple facultatif]), exemples ([phrase
    japonaise, traduction]), attention, et `exercice` (nom d'une fonction de
    index.html qui lance la serie d'exercices de la fiche).

Le niveau : le N5 (JLPT), soit le A1 du CECR. L'ordre est celui d'un manuel
de debutant : la phrase en です d'abord, les particules, les verbes en ます,
puis le reste. Chaque phrase japonaise porte sa lecture en romaji dans la
traduction : la fiche se lit avant de connaitre les kanji.

Ecrit a la main par Claude, BROUILLON : a faire relire par un natif avant
d'ouvrir le japonais a d'autres que l'admin.
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))


def fe(fr, en):
    return {"fr": fr, "en": en}


def ex(ja, romaji, fr, en):
    """Une phrase d'exemple : le japonais, puis « romaji — traduction »."""
    return [ja, fe(romaji + " — " + fr, romaji + " — " + en)]


FICHES = [
    {
        "id": "desu",
        "titre": fe("A は B です : la phrase de base", "A は B です: the basic sentence"),
        "resume": fe("Dire ce qu'est une chose, au présent et au passé", "Saying what something is, present and past"),
        "regle": fe(
            "<b>A は B です</b> = « A, c'est B ». は (lu <b>wa</b>) pose le sujet dont on parle ; です termine poliment la phrase. "
            "Pas d'article, pas de pluriel, pas de « je, tu, il » obligatoire : <b>学生です</b> suffit à dire « je suis étudiant ». "
            "Pour poser une question, on ajoute <b>か</b> à la fin, sans changer l'ordre des mots.",
            "<b>A は B です</b> = “A is B”. は (read <b>wa</b>) sets the topic; です politely closes the sentence. "
            "No articles, no plural, no compulsory “I, you, he”: <b>学生です</b> is enough to say “I'm a student”. "
            "To ask a question, add <b>か</b> at the end, without changing the word order."),
        "tableau": [
            ["です", fe("présent : c'est, je suis…", "present: it is, I am…"), "学生です。"],
            ["じゃありません", fe("négatif : ce n'est pas (じゃないです, plus parlé)", "negative: it isn't (じゃないです, more spoken)"), "学生じゃありません。"],
            ["でした", fe("passé : c'était", "past: it was"), "雨でした。"],
            ["じゃありませんでした", fe("passé négatif : ce n'était pas", "past negative: it wasn't"), "休みじゃありませんでした。"],
            ["～ですか", fe("question : est-ce que c'est… ?", "question: is it…?"), "学生ですか。"],
        ],
        "exemples": [
            ex("わたしはマルクです。", "watashi wa Maruku desu", "Je suis Mark.", "I'm Mark."),
            ex("カナダ人です。", "Kanada-jin desu", "Je suis Canadien.", "I'm Canadian."),
            ex("アンナさんは学生ですか。", "Anna-san wa gakusei desu ka", "Anna, tu es étudiante ?", "Anna, are you a student?"),
            ex("いいえ、学生じゃありません。", "iie, gakusei ja arimasen", "Non, je ne suis pas étudiante.", "No, I'm not a student."),
        ],
        "attention": fe(
            "は s'écrit avec le kana は (ha) mais se dit <b>wa</b> quand c'est la particule. "
            "Et on ne dit jamais « わたしは » à chaque phrase : une fois le sujet connu, on le laisse tomber. "
            "さん suit le nom des autres, jamais le sien.",
            "は is written with the kana は (ha) but said <b>wa</b> when it's the particle. "
            "And you never say “わたしは” in every sentence: once the topic is known, it's dropped. "
            "さん follows other people's names, never your own."),
        "exercice": "exercicesParticulesJa",
    },
    {
        "id": "wa-ga",
        "titre": fe("は et が : le thème et le sujet", "は and が: topic and subject"),
        "resume": fe("Deux particules pour « qui » ou « quoi » dans la phrase", "Two particles for “who” or “what” in the sentence"),
        "regle": fe(
            "<b>は</b> annonce le <b>thème</b> : « quant à… ». Il porte ce qu'on sait déjà, ou ce qu'on oppose. "
            "<b>が</b> désigne le <b>sujet</b> qui fait l'action ou qui existe, surtout quand c'est l'information nouvelle. "
            "Après un mot interrogatif (だれ, なに, どこ) on met toujours <b>が</b>, et la réponse le reprend.",
            "<b>は</b> announces the <b>topic</b>: “as for…”. It carries what is already known, or a contrast. "
            "<b>が</b> marks the <b>subject</b> that acts or exists, especially when it's the new information. "
            "After a question word (だれ, なに, どこ) it's always <b>が</b>, and the answer keeps it."),
        "tableau": [
            ["は (wa)", fe("le thème : « quant à », ce dont on parle", "topic: “as for”, what we're talking about"), "わたしは日本語がすきです。"],
            ["が (ga)", fe("le sujet : qui fait, qui existe, l'info nouvelle", "subject: who acts, what exists, the new info"), "だれが来ましたか。"],
            ["～がすき", fe("aimer quelque chose (l'objet aimé prend が)", "to like something (the liked thing takes が)"), "ねこがすきです。"],
            ["～がわかります", fe("comprendre quelque chose", "to understand something"), "日本語がわかります。"],
        ],
        "exemples": [
            ex("わたしはコーヒーがすきです。", "watashi wa kōhī ga suki desu", "Moi, j'aime le café.", "I like coffee."),
            ex("だれが来ましたか。— アンナさんが来ました。", "dare ga kimashita ka — Anna-san ga kimashita",
               "Qui est venu ? — C'est Anna qui est venue.", "Who came? — Anna came."),
            ex("雨がふっています。", "ame ga futte imasu", "Il pleut (la pluie tombe).", "It's raining."),
        ],
        "attention": fe(
            "Le contraste : <b>肉は食べません</b> = « la viande, je n'en mange pas » (sous-entendu : le reste, oui). "
            "Ne cherche pas une règle parfaite au début : retiens les tournures (～がすき, ～がわかります, ～があります) et le reste viendra.",
            "Contrast: <b>肉は食べません</b> = “meat, I don't eat” (implying: other things, yes). "
            "Don't look for a perfect rule at first: learn the set phrases (～がすき, ～がわかります, ～があります) and the rest will follow."),
        "exercice": "exercicesParticulesJa",
    },
    {
        "id": "particules",
        "titre": fe("を, に, へ, で : où va l'action", "を, に, へ, で: where the action goes"),
        "resume": fe("L'objet, le but, le lieu, le moyen", "Object, destination, place, means"),
        "regle": fe(
            "Les particules se placent <b>après</b> le mot qu'elles marquent, comme des prépositions à l'envers. "
            "<b>を</b> (lu <b>o</b>) marque l'objet direct ; <b>に</b> le point d'arrivée, l'heure, la personne à qui l'on donne ; "
            "<b>へ</b> (lu <b>e</b>) la direction ; <b>で</b> le lieu où l'on agit et le moyen.",
            "Particles go <b>after</b> the word they mark, like prepositions in reverse. "
            "<b>を</b> (read <b>o</b>) marks the direct object; <b>に</b> the destination, the time, the person you give to; "
            "<b>へ</b> (read <b>e</b>) the direction; <b>で</b> the place where you act, and the means."),
        "tableau": [
            ["を (o)", fe("l'objet : ce qu'on mange, lit, achète", "object: what you eat, read, buy"), "パンを食べます。"],
            ["に (ni)", fe("où l'on arrive, l'heure, à qui", "where you arrive, the time, to whom"), "七時に起きます。"],
            ["へ (e)", fe("vers où l'on va (≈ に)", "towards where you go (≈ に)"), "日本へ行きます。"],
            ["で (de)", fe("où l'on agit ; avec quoi, en quoi", "where you act; with what, by what"), "電車で行きます。"],
            ["と (to)", fe("avec qui ; et (entre deux noms)", "with whom; and (between two nouns)"), "友だちと行きます。"],
            ["から / まで", fe("depuis / jusqu'à", "from / until"), "九時から五時までです。"],
        ],
        "exemples": [
            ex("きのう、えきでパンを買いました。", "kinō, eki de pan o kaimashita", "Hier, j'ai acheté du pain à la gare.", "Yesterday I bought bread at the station."),
            ex("あした、バスで東京に行きます。", "ashita, basu de Tōkyō ni ikimasu", "Demain, je vais à Tokyo en bus.", "Tomorrow I'm going to Tokyo by bus."),
            ex("アンナさんに本をあげました。", "Anna-san ni hon o agemashita", "J'ai donné un livre à Anna.", "I gave Anna a book."),
        ],
        "attention": fe(
            "<b>に</b> ou <b>で</b> pour un lieu ? に si on y <b>est</b> ou on y <b>arrive</b> (へやにいます, 学校に行きます) ; "
            "で si on y <b>fait</b> quelque chose (へやで勉強します). L'heure précise prend に (三時に), "
            "mais pas きょう, あした, まいにち.",
            "<b>に</b> or <b>で</b> for a place? に if you <b>are</b> there or <b>arrive</b> there (へやにいます, 学校に行きます); "
            "で if you <b>do</b> something there (へやで勉強します). A precise time takes に (三時に), "
            "but not きょう, あした, まいにち."),
        "exercice": "exercicesParticulesJa",
    },
    {
        "id": "no-mo-to",
        "titre": fe("の, も, と, や : relier les noms", "の, も, と, や: linking nouns"),
        "resume": fe("De, aussi, et", "Of, also, and"),
        "regle": fe(
            "<b>の</b> relie deux noms, le premier précise le second : <b>わたしの本</b> = mon livre, <b>日本の車</b> = une voiture japonaise. "
            "<b>も</b> = « aussi » ; il remplace は, が ou を. "
            "<b>と</b> relie une liste complète (« A et B »), <b>や</b> une liste ouverte (« A, B, entre autres »).",
            "<b>の</b> links two nouns, the first one specifies the second: <b>わたしの本</b> = my book, <b>日本の車</b> = a Japanese car. "
            "<b>も</b> = “also”; it replaces は, が or を. "
            "<b>と</b> joins a complete list (“A and B”), <b>や</b> an open one (“A, B, among others”)."),
        "tableau": [
            ["A の B", fe("le B de A ; mon, ton (わたしの, あなたの)", "A's B; my, your (わたしの, あなたの)"), "これはわたしのかさです。"],
            ["も", fe("aussi, non plus (à la négation)", "also, not… either (in the negative)"), "わたしも学生です。"],
            ["A と B", fe("A et B (liste complète)", "A and B (complete list)"), "パンとたまごを食べました。"],
            ["A や B", fe("A, B, etc. (liste ouverte)", "A, B and so on (open list)"), "りんごやバナナを買いました。"],
        ],
        "exemples": [
            ex("マルクさんはカナダ人です。わたしもカナダ人です。", "Maruku-san wa Kanada-jin desu. watashi mo Kanada-jin desu",
               "Mark est Canadien. Moi aussi.", "Mark is Canadian. So am I."),
            ex("それはだれのかばんですか。", "sore wa dare no kaban desu ka", "À qui est ce sac ?", "Whose bag is that?"),
            ex("肉も魚も食べません。", "niku mo sakana mo tabemasen", "Je ne mange ni viande ni poisson.", "I eat neither meat nor fish."),
        ],
        "attention": fe(
            "と ne relie que des <b>noms</b>, jamais deux phrases : « je mange et je bois » passe par la forme en て (食べて、飲みます).",
            "と only joins <b>nouns</b>, never two sentences: “I eat and drink” uses the て-form (食べて、飲みます)."),
        "exercice": "exercicesParticulesJa",
    },
    {
        "id": "masu",
        "titre": fe("Les verbes en ます", "Verbs in ます"),
        "resume": fe("Présent, négatif, passé : la forme polie", "Present, negative, past: the polite form"),
        "regle": fe(
            "Le verbe se place <b>à la fin</b> de la phrase et ne change pas selon la personne : <b>行きます</b> = je vais, tu vas, ils vont… "
            "Le même présent vaut pour le futur : <b>あした行きます</b> = j'irai demain. "
            "Quatre terminaisons suffisent pour parler poliment.",
            "The verb goes <b>at the end</b> of the sentence and doesn't change with the person: <b>行きます</b> = I go, you go, they go… "
            "The same present covers the future: <b>あした行きます</b> = I'll go tomorrow. "
            "Four endings are enough to speak politely."),
        "tableau": [
            ["～ます", fe("présent et futur : je mange, je mangerai", "present and future: I eat, I'll eat"), "食べます"],
            ["～ません", fe("négatif : je ne mange pas", "negative: I don't eat"), "食べません"],
            ["～ました", fe("passé : j'ai mangé", "past: I ate"), "食べました"],
            ["～ませんでした", fe("passé négatif : je n'ai pas mangé", "past negative: I didn't eat"), "食べませんでした"],
            ["～ませんか", fe("invitation : tu ne veux pas… ?", "invitation: won't you…?"), "いっしょに行きませんか。"],
            ["～ましょう", fe("proposition : faisons…", "suggestion: let's…"), "行きましょう。"],
        ],
        "exemples": [
            ex("まいあさ、コーヒーを飲みます。", "maiasa, kōhī o nomimasu", "Tous les matins, je bois un café.", "Every morning I drink coffee."),
            ex("きのう、テレビを見ませんでした。", "kinō, terebi o mimasen deshita", "Hier, je n'ai pas regardé la télé.", "Yesterday I didn't watch TV."),
            ex("土曜日にえいがを見ませんか。", "doyōbi ni eiga o mimasen ka", "Tu ne veux pas voir un film samedi ?", "Would you like to see a film on Saturday?"),
        ],
        "attention": fe(
            "Chaque verbe de l'app montre ces quatre formes sur sa carte, calculées par le moteur de conjugaison : "
            "pas besoin de les apprendre une par une, la règle est la même pour tous.",
            "Every verb in the app shows these four forms on its card, computed by the conjugation engine: "
            "no need to learn them one by one, the rule is the same for all."),
        "exercice": "exercicesMasuJa",
    },
    {
        "id": "groupes-te",
        "titre": fe("Les trois groupes et la forme en て", "The three groups and the て-form"),
        "resume": fe("D'où vient ます, et la forme qui porte la moitié de la grammaire", "Where ます comes from, and the form that carries half the grammar"),
        "regle": fe(
            "Le dictionnaire donne la forme simple (<b>食べる</b>, <b>行く</b>). Trois groupes : "
            "<b>1</b>, les verbes en う (書く → 書きます) ; <b>2</b>, les verbes en る après e ou i (食べる → 食べます) ; "
            "<b>3</b>, les deux irréguliers する et 来る. "
            "La <b>forme en て</b> relie les actions, demande poliment (<b>～てください</b>) et dit ce qui est en cours (<b>～ています</b>).",
            "The dictionary gives the plain form (<b>食べる</b>, <b>行く</b>). Three groups: "
            "<b>1</b>, verbs in u (書く → 書きます); <b>2</b>, verbs in ru after e or i (食べる → 食べます); "
            "<b>3</b>, the two irregulars する and 来る. "
            "The <b>て-form</b> links actions, makes polite requests (<b>～てください</b>) and says what's ongoing (<b>～ています</b>)."),
        "tableau": [
            ["う・つ・る → って", fe("買う → 買って, 待つ → 待って, 帰る → 帰って", "買う → 買って, 待つ → 待って, 帰る → 帰って")],
            ["む・ぶ・ぬ → んで", fe("飲む → 飲んで, 遊ぶ → 遊んで, 死ぬ → 死んで", "飲む → 飲んで, 遊ぶ → 遊んで, 死ぬ → 死んで")],
            ["く → いて, ぐ → いで", fe("書く → 書いて, 泳ぐ → 泳いで (mais 行く → 行って)", "書く → 書いて, 泳ぐ → 泳いで (but 行く → 行って)")],
            ["す → して", fe("話す → 話して", "話す → 話して")],
            ["groupe 2 : る → て", fe("食べる → 食べて, 見る → 見て", "食べる → 食べて, 見る → 見て")],
            ["する → して, 来る → 来て", fe("les deux irréguliers", "the two irregulars")],
        ],
        "exemples": [
            ex("ちょっと待ってください。", "chotto matte kudasai", "Attendez un instant, s'il vous plaît.", "Please wait a moment."),
            ex("いま、ごはんを食べています。", "ima, gohan o tabete imasu", "Je suis en train de manger.", "I'm eating right now."),
            ex("うちに帰って、ねました。", "uchi ni kaette, nemashita", "Je suis rentré et je me suis couché.", "I went home and went to bed."),
        ],
        "attention": fe(
            "Piège : quelques verbes en る sont du groupe 1 (帰る, 入る, 走る, 知る) : 帰ります, 帰って. "
            "Les cartes de verbes donnent le groupe et toutes ces formes, calculées.",
            "Trap: a few ru-verbs belong to group 1 (帰る, 入る, 走る, 知る): 帰ります, 帰って. "
            "The verb cards give the group and all these forms, computed."),
        "exercice": "exercicesTeJa",
    },
    {
        "id": "adjectifs",
        "titre": fe("Les adjectifs en い et en な", "い- and な-adjectives"),
        "resume": fe("Deux familles, deux façons de se conjuguer", "Two families, two ways to conjugate"),
        "regle": fe(
            "Un adjectif japonais se place <b>avant</b> le nom et se <b>conjugue</b>. "
            "Les adjectifs en <b>い</b> (高い, 大きい) changent leur fin : 高くない, 高かった. "
            "Les adjectifs en <b>な</b> (静か, 元気) ne bougent pas ; c'est です qui se conjugue, et devant un nom ils prennent な : 静かな町.",
            "A Japanese adjective goes <b>before</b> the noun and <b>conjugates</b>. "
            "<b>い</b>-adjectives (高い, 大きい) change their ending: 高くない, 高かった. "
            "<b>な</b>-adjectives (静か, 元気) don't move; です conjugates instead, and before a noun they take な: 静かな町."),
        "tableau": [
            ["高いです / 静かです", fe("présent : c'est cher / c'est calme", "present: it's expensive / it's quiet")],
            ["高くないです / 静かじゃないです", fe("négatif (à l'écrit : 静かではない)", "negative (in writing: 静かではない)")],
            ["高かったです / 静かでした", fe("passé", "past")],
            ["高くなかったです / 静かじゃなかったです", fe("passé négatif", "past negative")],
            ["高い本 / 静かな町", fe("devant un nom : い reste, な apparaît", "before a noun: い stays, な appears")],
        ],
        "exemples": [
            ex("この本はおもしろいです。", "kono hon wa omoshiroi desu", "Ce livre est intéressant.", "This book is interesting."),
            ex("きのうはさむかったです。", "kinō wa samukatta desu", "Hier, il faisait froid.", "It was cold yesterday."),
            ex("きれいな花ですね。", "kirei na hana desu ne", "Quelle jolie fleur !", "What a pretty flower!"),
        ],
        "attention": fe(
            "<b>いい</b> (bien) est irrégulier : よくない, よかった. Et <b>きれい</b>, <b>きらい</b> finissent par い mais sont des adjectifs en な : きれいな花. "
            "Chaque carte d'adjectif dit sa famille et donne ses quatre formes.",
            "<b>いい</b> (good) is irregular: よくない, よかった. And <b>きれい</b>, <b>きらい</b> end in い but are な-adjectives: きれいな花. "
            "Each adjective card states its family and gives its four forms."),
        "exercice": "exercicesAdjectifsJa",
    },
    {
        "id": "kosoado",
        "titre": fe("これ, それ, あれ, どれ", "これ, それ, あれ, どれ"),
        "resume": fe("Ceci, cela, là-bas, lequel : la série こそあど", "This, that, over there, which: the こそあど series"),
        "regle": fe(
            "Quatre préfixes, toujours dans le même ordre : <b>こ</b> près de moi, <b>そ</b> près de toi, <b>あ</b> loin de nous deux, "
            "<b>ど</b> la question. On les combine : これ (ceci), ここ (ici), この本 (ce livre-ci).",
            "Four prefixes, always in the same order: <b>こ</b> near me, <b>そ</b> near you, <b>あ</b> far from both of us, "
            "<b>ど</b> the question. They combine: これ (this), ここ (here), この本 (this book)."),
        "tableau": [
            ["これ・それ・あれ・どれ", fe("ceci, cela, ça là-bas, lequel (seul)", "this, that, that over there, which (on its own)")],
            ["この・その・あの・どの + nom", fe("ce… -ci, ce… -là, quel…", "this…, that…, which…"), "この本"],
            ["ここ・そこ・あそこ・どこ", fe("ici, là, là-bas, où", "here, there, over there, where")],
            ["こちら・そちら・あちら・どちら", fe("par ici… (poli) ; aussi « cette personne »", "this way… (polite); also “this person”")],
        ],
        "exemples": [
            ex("これはなんですか。— それはおちゃです。", "kore wa nan desu ka — sore wa ocha desu", "Qu'est-ce que c'est ? — C'est du thé.", "What's this? — That's tea."),
            ex("トイレはどこですか。— あそこです。", "toire wa doko desu ka — asoko desu", "Où sont les toilettes ? — Là-bas.", "Where's the toilet? — Over there."),
            ex("あの人はだれですか。", "ano hito wa dare desu ka", "Qui est cette personne là-bas ?", "Who's that person over there?"),
        ],
        "attention": fe(
            "これ ne se met jamais devant un nom : <b>この本</b>, pas « これ本 ».",
            "これ never goes before a noun: <b>この本</b>, not “これ本”."),
        "exercice": "exercicesKosoadoJa",
    },
    {
        "id": "questions",
        "titre": fe("Poser une question", "Asking questions"),
        "resume": fe("か, et les mots interrogatifs", "か, and the question words"),
        "regle": fe(
            "Une question se fait en ajoutant <b>か</b> à la fin d'une phrase polie. "
            "Le mot interrogatif prend la place de la réponse, sans bouger le reste : "
            "<b>えきはどこですか</b> (où est la gare ?) → <b>えきはあそこです</b>.",
            "A question is made by adding <b>か</b> at the end of a polite sentence. "
            "The question word takes the place of the answer, without moving the rest: "
            "<b>えきはどこですか</b> (where's the station?) → <b>えきはあそこです</b>."),
        "tableau": [
            ["なに / なん", fe("quoi (なん devant です, の et les compteurs)", "what (なん before です, の and counters)"), "なんですか。"],
            ["だれ", fe("qui (どなた, plus poli)", "who (どなた, more polite)"), "だれですか。"],
            ["どこ", fe("où", "where"), "どこに行きますか。"],
            ["いつ", fe("quand", "when"), "いつ来ますか。"],
            ["いくら", fe("combien (le prix)", "how much (price)"), "これはいくらですか。"],
            ["どうして / なぜ", fe("pourquoi", "why"), "どうしてですか。"],
            ["どう", fe("comment ; comment c'était", "how; how was it"), "日本はどうですか。"],
        ],
        "exemples": [
            ex("おなまえはなんですか。", "onamae wa nan desu ka", "Comment vous appelez-vous ?", "What's your name?"),
            ex("いつ日本に来ましたか。", "itsu Nihon ni kimashita ka", "Quand es-tu arrivé au Japon ?", "When did you come to Japan?"),
            ex("このりんごはいくらですか。", "kono ringo wa ikura desu ka", "Combien coûte cette pomme ?", "How much is this apple?"),
        ],
        "attention": fe(
            "Pas de point d'interrogation en japonais soigné : か suffit (on écrit 。). "
            "À l'oral entre amis, on laisse tomber か et on monte la voix.",
            "No question mark in careful Japanese: か is enough (you write 。). "
            "In casual speech, か is dropped and the voice rises."),
        "exercice": "exercicesQuestionsJa",
    },
    {
        "id": "aru-iru",
        "titre": fe("あります et います : il y a", "あります and います: there is"),
        "resume": fe("Exister, se trouver, avoir", "To exist, to be somewhere, to have"),
        "regle": fe(
            "Deux verbes pour « il y a » : <b>あります</b> pour les choses et les plantes, <b>います</b> pour ce qui bouge tout seul "
            "(personnes, animaux). Le lieu prend <b>に</b>, la chose <b>が</b> : <b>へやにねこがいます</b> = il y a un chat dans la chambre.",
            "Two verbs for “there is”: <b>あります</b> for things and plants, <b>います</b> for what moves by itself "
            "(people, animals). The place takes <b>に</b>, the thing <b>が</b>: <b>へやにねこがいます</b> = there's a cat in the room."),
        "tableau": [
            ["あります / ありません", fe("il y a (choses) / il n'y a pas", "there is (things) / there isn't"), "つくえの上に本があります。"],
            ["います / いません", fe("il y a (êtres vivants) / il n'y a pas", "there is (living beings) / there isn't"), "こうえんに子どもがいます。"],
            ["～があります", fe("avoir : 時間があります = j'ai le temps", "to have: 時間があります = I have time")],
            ["上・下・中・前・うしろ・となり", fe("sur, sous, dans, devant, derrière, à côté (+ の)", "on, under, in, in front, behind, next to (+ の)"), "えきの前"],
        ],
        "exemples": [
            ex("れいぞうこにぎゅうにゅうがありますか。", "reizōko ni gyūnyū ga arimasu ka", "Il y a du lait dans le frigo ?", "Is there milk in the fridge?"),
            ex("きょうだいがいますか。— 兄が一人います。", "kyōdai ga imasu ka — ani ga hitori imasu", "Tu as des frères et sœurs ? — J'ai un grand frère.", "Do you have siblings? — I have one older brother."),
            ex("コンビニはえきの前にあります。", "konbini wa eki no mae ni arimasu", "La supérette est devant la gare.", "The convenience store is in front of the station."),
        ],
        "attention": fe(
            "« Où est X ? » met X en thème : <b>トイレはどこにありますか</b> (ou simplement <b>どこですか</b>).",
            "“Where is X?” makes X the topic: <b>トイレはどこにありますか</b> (or simply <b>どこですか</b>)."),
        "exercice": "exercicesAruIruJa",
    },
    {
        "id": "tai-suki",
        "titre": fe("Vouloir et aimer : ～たい, ほしい, すき", "Wanting and liking: ～たい, ほしい, すき"),
        "resume": fe("Dire ce qu'on veut faire, ce qu'on veut avoir, ce qu'on aime", "Saying what you want to do, to have, and what you like"),
        "regle": fe(
            "<b>～たい</b> remplace ます : <b>行きます → 行きたいです</b> (je veux y aller). Il se conjugue comme un adjectif en い. "
            "<b>ほしい</b> = vouloir une chose : <b>水がほしいです</b>. "
            "<b>すき</b> (aimer) et <b>きらい</b> (ne pas aimer) sont des adjectifs en な : l'objet prend <b>が</b>.",
            "<b>～たい</b> replaces ます: <b>行きます → 行きたいです</b> (I want to go). It conjugates like an い-adjective. "
            "<b>ほしい</b> = to want a thing: <b>水がほしいです</b>. "
            "<b>すき</b> (to like) and <b>きらい</b> (to dislike) are な-adjectives: the object takes <b>が</b>."),
        "tableau": [
            ["～たいです", fe("je veux (faire)", "I want to (do)"), "日本に行きたいです。"],
            ["～たくないです", fe("je ne veux pas (faire)", "I don't want to (do)"), "あした、はたらきたくないです。"],
            ["～がほしいです", fe("je veux (une chose)", "I want (a thing)"), "あたらしいくつがほしいです。"],
            ["～がすきです / きらいです", fe("j'aime / je n'aime pas", "I like / I dislike"), "すしがすきです。"],
            ["じょうず / へた", fe("être doué / pas doué (pour…が)", "good / bad (at…が)"), "りょうりがじょうずですね。"],
        ],
        "exemples": [
            ex("なにが食べたいですか。", "nani ga tabetai desu ka", "Qu'est-ce que tu veux manger ?", "What do you want to eat?"),
            ex("わたしはねこがだいすきです。", "watashi wa neko ga daisuki desu", "J'adore les chats.", "I love cats."),
        ],
        "attention": fe(
            "～たい et ほしい parlent de <b>soi</b> (et, en question, de l'autre) ; pour une tierce personne, on dit autrement (～たがっています), plus tard.",
            "～たい and ほしい talk about <b>yourself</b> (and, in a question, the listener); for a third person it's said differently (～たがっています), later."),
    },
    {
        "id": "politesse",
        "titre": fe("Poli ou familier : です・ます et la forme simple", "Polite or casual: です・ます and the plain form"),
        "resume": fe("Deux registres, un même sens", "Two registers, one meaning"),
        "regle": fe(
            "Avec un inconnu, un collègue, un commerçant : <b>です・ます</b>. Avec un ami, la famille : la <b>forme simple</b> "
            "(行く, 行かない, 行った ; だ au lieu de です). Le sens ne change pas, seule la distance. "
            "Commence par la forme polie : elle n'est jamais une faute.",
            "With a stranger, a colleague, a shopkeeper: <b>です・ます</b>. With a friend, family: the <b>plain form</b> "
            "(行く, 行かない, 行った; だ instead of です). The meaning is the same, only the distance changes. "
            "Start with the polite form: it's never a mistake."),
        "tableau": [
            ["行きます ↔ 行く", fe("je vais", "I go")],
            ["行きません ↔ 行かない", fe("je ne vais pas", "I don't go")],
            ["行きました ↔ 行った", fe("je suis allé", "I went")],
            ["学生です ↔ 学生だ", fe("je suis étudiant", "I'm a student")],
            ["高いです ↔ 高い", fe("c'est cher", "it's expensive")],
        ],
        "exemples": [
            ex("あした、来ますか。/ あした、来る？", "ashita, kimasu ka / ashita, kuru?", "Tu viens demain ? (poli / familier)", "Are you coming tomorrow? (polite / casual)"),
            ex("ありがとうございます。/ ありがとう。", "arigatō gozaimasu / arigatō", "Merci. (poli / familier)", "Thank you. (polite / casual)"),
        ],
        "attention": fe(
            "Les cartes de verbes montrent la forme polie d'abord, puis les formes simples en dépliant.",
            "Verb cards show the polite form first, then the plain forms when unfolded."),
    },
    {
        "id": "liaisons",
        "titre": fe("Relier deux phrases : から, が, けど", "Linking two sentences: から, が, けど"),
        "resume": fe("Parce que, mais", "Because, but"),
        "regle": fe(
            "La raison vient <b>avant</b>, suivie de <b>から</b> : <b>雨ですから、行きません</b> = il pleut, donc je n'y vais pas. "
            "<b>が</b> (soutenu) et <b>けど</b> (parlé) = « mais », à la fin de la première partie.",
            "The reason comes <b>first</b>, followed by <b>から</b>: <b>雨ですから、行きません</b> = it's raining, so I'm not going. "
            "<b>が</b> (formal) and <b>けど</b> (spoken) = “but”, at the end of the first part."),
        "tableau": [
            ["A から、B", fe("parce que A, B ; A, donc B", "because A, B; A, so B"), "つかれましたから、ねます。"],
            ["A が、B", fe("A, mais B (soutenu)", "A, but B (formal)"), "高いですが、おいしいです。"],
            ["A けど、B", fe("A, mais B (parlé)", "A, but B (spoken)"), "むずかしいけど、おもしろい。"],
            ["それから / でも", fe("et puis / mais (en début de phrase)", "and then / but (at the start of a sentence)")],
        ],
        "exemples": [
            ex("じかんがありませんから、タクシーで行きます。", "jikan ga arimasen kara, takushī de ikimasu", "Je n'ai pas le temps, alors je prends un taxi.", "I don't have time, so I'll take a taxi."),
            ex("日本語はむずかしいですが、たのしいです。", "Nihongo wa muzukashii desu ga, tanoshii desu", "Le japonais est difficile, mais amusant.", "Japanese is hard, but fun."),
        ],
        "attention": fe(
            "Ne confonds pas ce が (« mais », entre deux phrases) avec la particule が du sujet.",
            "Don't confuse this が (“but”, between two sentences) with the subject particle が."),
    },
]


# Les titres des series d'exercices (kicker), verses dans I18N au chargement.
TEXTES = {
    "fr": {
        "fiche_entrainer": "M'ENTRAÎNER →",
        "fiche_entrainer_x": "M'ENTRAÎNER : {x} →",
        "gram_attention": "Attention",
        "orb_es_indice": "Grammaire",
        "gram_indice_kicker": "Grammaire · N5",
        "gram_indice_titre": "Toutes les fiches",
        "kicker_particules_ja": "Les particules",
        "kicker_masu_ja": "Les verbes en ます",
        "kicker_te_ja": "La forme en て",
        "kicker_adjectifs_ja": "Les adjectifs en い et en な",
        "kicker_kosoado_ja": "これ, それ, あれ, どれ",
        "kicker_questions_ja": "Les questions",
        "kicker_aru_iru_ja": "あります et います",
    },
    "en": {
        "fiche_entrainer": "PRACTICE →",
        "fiche_entrainer_x": "PRACTICE: {x} →",
        "gram_attention": "Watch out",
        "orb_es_indice": "Grammar",
        "gram_indice_kicker": "Grammar · N5",
        "gram_indice_titre": "All grammar notes",
        "kicker_particules_ja": "Particles",
        "kicker_masu_ja": "Verbs in ます",
        "kicker_te_ja": "The て-form",
        "kicker_adjectifs_ja": "い- and な-adjectives",
        "kicker_kosoado_ja": "これ, それ, あれ, どれ",
        "kicker_questions_ja": "Questions",
        "kicker_aru_iru_ja": "あります and います",
    },
}


def main():
    ids = [f["id"] for f in FICHES]
    assert len(ids) == len(set(ids)), ids
    for f in FICHES:
        for k in ("titre", "resume", "regle"):
            assert f[k]["fr"] and f[k]["en"], (f["id"], k)
        f["statut"] = "brouillon"
    chemin = os.path.join(ICI, "grammaire.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as fo:
        json.dump({"_note": "Derive de japonais/datos/grammaire_construire.py : ne pas modifier a la main. "
                            "Fiches N5, brouillon a faire relire par un natif.",
                   "textes": TEXTES, "fiches": FICHES}, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    print("%d fiches : %s -> %s" % (len(FICHES), ", ".join(ids), os.path.relpath(chemin)))


if __name__ == "__main__":
    main()
