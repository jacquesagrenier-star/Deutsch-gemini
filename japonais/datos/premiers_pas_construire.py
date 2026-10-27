# -*- coding: utf-8 -*-
"""Construit japonais/datos/premiers-pas.json : les Premiers pas du japonais.

    python japonais/datos/premiers_pas_construire.py

LE MEME FORMAT QUE espanol/datos/premiers-pas.json, lu par le meme moteur
(chargerPremiersPas, sequencePremiersPas, ouvrirPremiersPas) : des etapes de
voyage, chacune { s, scene, tableau {t, l, a}, cartes, phrases }.

Ce qui change pour le japonais :
  - une carte porte en 5e position { "ja": { lecture, romaji } } : la carte
    japonaise ecrit la lecture et le romaji sous l'expression ;
  - une ligne de tableau porte en 3e position la prononciation (kana · romaji),
    comme les reperes ;
  - les phrases sont ecrites en kana, AVEC DES ESPACES entre les groupes de
    mots (comme les livres pour enfants et les manuels de debutants) : c'est
    ce qui permet l'exercice « remettre en ordre » ; la voix les lit sans les
    entendre, l'oral les ignore ;
  - `scene` est nul tant que les scenes japonaises (konbini, eki, genkan) ne
    sont pas jouables dans l'app : l'etape se ferme sans scene.

Tout est en kana (le debutant apprend les kana en parallele, dans la seance),
avec le romaji Hepburn ecrit a la main (は particule = wa, を = o).
Brouillon : a faire relire par un natif.
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))


def fe(fr, en):
    return {"fr": fr, "en": en}


def carte(expr, romaji, fr, en, ex=None, ex_romaji=None, ex_fr=None, ex_en=None):
    c = [expr, fe(fr, en), ex or "", fe(ex_fr, ex_en) if ex else {}]
    c.append({"ja": {"lecture": expr, "romaji": romaji}})
    return c


def ligne(forme, romaji, fr, en):
    return [forme, fe(fr, en), {"fr": forme.replace(" ", "") + " · " + romaji, "en": forme.replace(" ", "") + " · " + romaji}]


def phrase(p, fr, en, l1, l2):
    return {"p": p, "s": fe(fr[0], en[0]) if isinstance(fr, tuple) else fe(fr, en),
            "l": [fe(*l1), fe(*l2)]}


ETAPES = [
    {
        "s": fe("L'arrivée : saluer et se présenter", "Arriving: greetings and introductions"),
        "scene": None,
        "tableau": {
            "t": fe("Se présenter : ～です", "Introducing yourself: ～です"),
            "l": [ligne("わたしは マルクです", "watashi wa Maruku desu", "je suis Mark", "I'm Mark"),
                  ligne("カナダじんです", "Kanada-jin desu", "je suis Canadien", "I'm Canadian"),
                  ligne("がくせいです", "gakusei desu", "je suis étudiant", "I'm a student"),
                  ligne("はじめまして", "hajimemashite", "enchanté (première rencontre)", "nice to meet you"),
                  ligne("どうぞ よろしく", "dōzo yoroshiku", "ravi de vous connaître", "pleased to meet you")],
            "a": fe("～です termine poliment la phrase : « c'est, je suis ». On ne répète pas わたしは une fois qu'on s'est présenté. "
                    "Le nom d'un pays + じん = la nationalité : フランスじん, カナダじん.",
                    "～です politely closes the sentence: “it is, I am”. Don't repeat わたしは once you've introduced yourself. "
                    "A country + じん = the nationality: フランスじん, カナダじん."),
        },
        "cartes": [
            carte("こんにちは", "konnichiwa", "bonjour", "hello", "こんにちは、マルクです。", "", "Bonjour, je suis Mark.", "Hello, I'm Mark."),
            carte("おはようございます", "ohayō gozaimasu", "bonjour (le matin)", "good morning"),
            carte("こんばんは", "konbanwa", "bonsoir", "good evening"),
            carte("はじめまして", "hajimemashite", "enchanté", "nice to meet you", "はじめまして、アンナです。", "", "Enchantée, je suis Anna.", "Nice to meet you, I'm Anna."),
            carte("どうぞ よろしく", "dōzo yoroshiku", "ravi de vous connaître", "pleased to meet you"),
            carte("ありがとうございます", "arigatō gozaimasu", "merci", "thank you"),
            carte("すみません", "sumimasen", "excusez-moi, pardon", "excuse me, sorry", "すみません、トイレは どこですか。", "", "Excusez-moi, où sont les toilettes ?", "Excuse me, where's the toilet?"),
            carte("はい", "hai", "oui", "yes"),
            carte("いいえ", "iie", "non", "no"),
            carte("さようなら", "sayōnara", "au revoir (pour longtemps)", "goodbye (for a long time)"),
            carte("おなまえは", "onamae wa", "votre nom ?", "your name?", "おなまえは？ — マルクです。", "", "Votre nom ? — Mark.", "Your name? — Mark."),
            carte("～から きました", "～kara kimashita", "je viens de…", "I'm from…", "カナダから きました。", "", "Je viens du Canada.", "I'm from Canada."),
        ],
        "phrases": [
            phrase("はじめまして、 マルクです。", "Enchanté, je suis Mark.", "Nice to meet you, I'm Mark.",
                   ("Au revoir, je suis Mark.", "Goodbye, I'm Mark."), ("Merci, Mark.", "Thank you, Mark.")),
            phrase("わたしは カナダじんです。", "Je suis Canadien.", "I'm Canadian.",
                   ("Je suis Japonais.", "I'm Japanese."), ("Il est Canadien.", "He's Canadian.")),
            phrase("カナダから きました。", "Je viens du Canada.", "I'm from Canada.",
                   ("Je vais au Canada.", "I'm going to Canada."), ("J'aime le Canada.", "I like Canada.")),
            phrase("おはようございます。", "Bonjour (le matin).", "Good morning.",
                   ("Bonsoir.", "Good evening."), ("Merci beaucoup.", "Thank you very much.")),
            phrase("どうぞ よろしく。", "Ravi de vous connaître.", "Pleased to meet you.",
                   ("Excusez-moi.", "Excuse me."), ("À bientôt.", "See you soon.")),
            phrase("アンナさんは がくせいですか。", "Anna, tu es étudiante ?", "Anna, are you a student?",
                   ("Anna est professeur.", "Anna is a teacher."), ("Anna, tu es Canadienne ?", "Anna, are you Canadian?")),
        ],
    },
    {
        "s": fe("Au konbini : acheter", "At the konbini: buying"),
        "scene": None,
        "tableau": {
            "t": fe("Demander : ～を ください", "Asking for: ～を ください"),
            "l": [ligne("これを ください", "kore o kudasai", "je voudrais ceci", "this, please"),
                  ligne("みずを ください", "mizu o kudasai", "de l'eau, s'il vous plaît", "water, please"),
                  ligne("おにぎりを ふたつ ください", "onigiri o futatsu kudasai", "deux onigiri, s'il vous plaît", "two onigiri, please"),
                  ligne("いくらですか", "ikura desu ka", "combien ça coûte ?", "how much is it?"),
                  ligne("ふくろは いりません", "fukuro wa irimasen", "je n'ai pas besoin de sac", "I don't need a bag")],
            "a": fe("La chose demandée + を + ください. Pour le nombre, ひとつ, ふたつ, みっつ se placent juste avant ください. "
                    "を se lit « o ». Au konbini, on te demandera souvent : ふくろは いりますか (un sac ?).",
                    "The thing + を + ください. For the number, ひとつ, ふたつ, みっつ go right before ください. "
                    "を is read “o”. At a konbini you'll often hear: ふくろは いりますか (a bag?)."),
        },
        "cartes": [
            carte("これ", "kore", "ceci (près de moi)", "this (near me)", "これを ください。", "", "Je voudrais ceci.", "This, please."),
            carte("それ", "sore", "cela (près de toi)", "that (near you)"),
            carte("ください", "kudasai", "s'il vous plaît (donnez-moi)", "please (give me)"),
            carte("いくらですか", "ikura desu ka", "combien ça coûte ?", "how much is it?", "これは いくらですか。", "", "Combien coûte ceci ?", "How much is this?"),
            carte("～えん", "～en", "… yens", "… yen", "ひゃくえんです。", "", "C'est 100 yens.", "It's 100 yen."),
            carte("おにぎり", "onigiri", "boulette de riz", "rice ball"),
            carte("みず", "mizu", "eau", "water"),
            carte("おちゃ", "ocha", "thé (vert)", "(green) tea"),
            carte("ふくろ", "fukuro", "sac (de course)", "(shopping) bag"),
            carte("あたためますか", "atatamemasu ka", "je vous le réchauffe ?", "shall I heat it up?"),
            carte("カードで", "kādo de", "par carte", "by card", "カードで いいですか。", "", "Je peux payer par carte ?", "Can I pay by card?"),
            carte("ひとつ", "hitotsu", "un (objet)", "one (thing)"),
        ],
        "phrases": [
            phrase("これを ください。", "Je voudrais ceci.", "This, please.",
                   ("C'est combien ?", "How much is it?"), ("Je n'en veux pas.", "I don't want it.")),
            phrase("これは いくらですか。", "Combien coûte ceci ?", "How much is this?",
                   ("Où est-ce ?", "Where is it?"), ("Qu'est-ce que c'est ?", "What is this?")),
            phrase("おちゃを ふたつ ください。", "Deux thés, s'il vous plaît.", "Two teas, please.",
                   ("Un thé, s'il vous plaît.", "One tea, please."), ("Deux cafés, s'il vous plaît.", "Two coffees, please.")),
            phrase("ふくろは いりません。", "Je n'ai pas besoin de sac.", "I don't need a bag.",
                   ("Un sac, s'il vous plaît.", "A bag, please."), ("Où est le sac ?", "Where's the bag?")),
            phrase("カードで いいですか。", "Je peux payer par carte ?", "Can I pay by card?",
                   ("Vous avez une carte ?", "Do you have a card?"), ("C'est combien en espèces ?", "How much in cash?")),
            phrase("すみません、 みずは どこですか。", "Excusez-moi, où est l'eau ?", "Excuse me, where's the water?",
                   ("Excusez-moi, de l'eau s'il vous plaît.", "Excuse me, water please."), ("Merci pour l'eau.", "Thanks for the water.")),
        ],
    },
    {
        "s": fe("À la gare : trouver son chemin", "At the station: finding your way"),
        "scene": None,
        "tableau": {
            "t": fe("Où est… ? ～は どこですか", "Where is…? ～は どこですか"),
            "l": [ligne("えきは どこですか", "eki wa doko desu ka", "où est la gare ?", "where's the station?"),
                  ligne("トイレは どこですか", "toire wa doko desu ka", "où sont les toilettes ?", "where's the toilet?"),
                  ligne("ここです", "koko desu", "c'est ici", "it's here"),
                  ligne("あそこです", "asoko desu", "c'est là-bas", "it's over there"),
                  ligne("みぎ ・ ひだり ・ まっすぐ", "migi · hidari · massugu", "droite · gauche · tout droit", "right · left · straight ahead")],
            "a": fe("Ce qu'on cherche + は どこですか. Pour répondre : ここ (ici, près de moi), そこ (là, près de toi), "
                    "あそこ (là-bas). Commence par すみません pour attirer l'attention.",
                    "What you're looking for + は どこですか. Answers: ここ (here, near me), そこ (there, near you), "
                    "あそこ (over there). Start with すみません to get someone's attention."),
        },
        "cartes": [
            carte("えき", "eki", "gare", "station", "えきは どこですか。", "", "Où est la gare ?", "Where's the station?"),
            carte("でんしゃ", "densha", "train", "train"),
            carte("きっぷ", "kippu", "billet", "ticket", "きっぷを ください。", "", "Un billet, s'il vous plaît.", "A ticket, please."),
            carte("～ばんせん", "～bansen", "voie n°…", "platform no. …", "さんばんせんです。", "", "C'est la voie 3.", "It's platform 3."),
            carte("トイレ", "toire", "toilettes", "toilet"),
            carte("でぐち", "deguchi", "sortie", "exit"),
            carte("いりぐち", "iriguchi", "entrée", "entrance"),
            carte("みぎ", "migi", "droite", "right"),
            carte("ひだり", "hidari", "gauche", "left"),
            carte("まっすぐ", "massugu", "tout droit", "straight ahead"),
            carte("ちかい", "chikai", "proche", "near"),
            carte("とおい", "tōi", "loin", "far"),
        ],
        "phrases": [
            phrase("すみません、 えきは どこですか。", "Excusez-moi, où est la gare ?", "Excuse me, where's the station?",
                   ("Excusez-moi, c'est la gare ?", "Excuse me, is this the station?"), ("Excusez-moi, la gare est loin.", "Excuse me, the station is far.")),
            phrase("トイレは あそこです。", "Les toilettes sont là-bas.", "The toilet is over there.",
                   ("Les toilettes sont ici.", "The toilet is here."), ("Où sont les toilettes ?", "Where's the toilet?")),
            phrase("まっすぐ いって、 みぎです。", "Tout droit, puis à droite.", "Go straight, then right.",
                   ("Tout droit, puis à gauche.", "Go straight, then left."), ("À droite, puis tout droit.", "Right, then straight on.")),
            phrase("きっぷを いちまい ください。", "Un billet, s'il vous plaît.", "One ticket, please.",
                   ("Deux billets, s'il vous plaît.", "Two tickets, please."), ("Où sont les billets ?", "Where are the tickets?")),
            phrase("でぐちは ひだりです。", "La sortie est à gauche.", "The exit is on the left.",
                   ("L'entrée est à gauche.", "The entrance is on the left."), ("La sortie est à droite.", "The exit is on the right.")),
            phrase("これを ください。", "Je voudrais ceci.", "This, please.",
                   ("C'est combien ?", "How much is it?"), ("Qu'est-ce que c'est ?", "What is this?")),
        ],
    },
    {
        "s": fe("Chez quelqu'un : les formules de la maison", "At someone's home: household phrases"),
        "scene": None,
        "tableau": {
            "t": fe("Les mots de tous les jours, à la maison", "Everyday words at home"),
            "l": [ligne("おじゃまします", "ojama shimasu", "en entrant chez quelqu'un", "when entering someone's home"),
                  ligne("いただきます", "itadakimasu", "avant de manger", "before eating"),
                  ligne("ごちそうさまでした", "gochisōsama deshita", "après le repas : merci", "after the meal: thank you"),
                  ligne("いってきます ・ いってらっしゃい", "ittekimasu · itterasshai", "j'y vais · vas-y, à tout à l'heure", "I'm off · see you later"),
                  ligne("ただいま ・ おかえりなさい", "tadaima · okaerinasai", "je suis rentré · bon retour", "I'm home · welcome back")],
            "a": fe("Ces formules se disent à chaque fois, sans exception, et elles vont par paires : celui qui part dit いってきます, "
                    "celui qui reste répond いってらっしゃい. Au 玄関 (l'entrée), on enlève ses chaussures.",
                    "These phrases are said every time, without exception, and come in pairs: the one leaving says いってきます, "
                    "the one staying answers いってらっしゃい. In the 玄関 (entryway), you take your shoes off."),
        },
        "cartes": [
            carte("おじゃまします", "ojama shimasu", "pardon de vous déranger (en entrant)", "sorry to intrude (when entering)"),
            carte("どうぞ", "dōzo", "je vous en prie, entrez", "please, go ahead", "どうぞ、 あがって ください。", "", "Je vous en prie, entrez.", "Please, come in."),
            carte("くつ", "kutsu", "chaussures", "shoes"),
            carte("スリッパ", "surippa", "chaussons", "slippers"),
            carte("いただきます", "itadakimasu", "bon appétit (avant de manger)", "said before eating"),
            carte("ごちそうさまでした", "gochisōsama deshita", "merci pour le repas", "thank you for the meal"),
            carte("おいしい", "oishii", "bon, délicieux", "delicious", "とても おいしいです。", "", "C'est très bon.", "It's very good."),
            carte("ただいま", "tadaima", "je suis rentré", "I'm home"),
            carte("おかえりなさい", "okaerinasai", "bon retour", "welcome back"),
            carte("いってきます", "ittekimasu", "j'y vais (et je reviens)", "I'm off (and will be back)"),
            carte("いってらっしゃい", "itterasshai", "vas-y, à tout à l'heure", "see you later"),
            carte("おやすみなさい", "oyasuminasai", "bonne nuit", "good night"),
        ],
        "phrases": [
            phrase("おじゃまします。", "Pardon de vous déranger (en entrant).", "Sorry to intrude (when entering).",
                   ("Merci pour le repas.", "Thank you for the meal."), ("Je suis rentré.", "I'm home.")),
            phrase("いただきます。", "Bon appétit (avant de manger).", "(Said before eating.)",
                   ("Merci pour le repas (après).", "Thank you for the meal (after)."), ("Bonne nuit.", "Good night.")),
            phrase("とても おいしいです。", "C'est très bon.", "It's very good.",
                   ("Ce n'est pas bon.", "It's not good."), ("C'est très cher.", "It's very expensive.")),
            phrase("くつは ここです。", "Les chaussures, c'est ici.", "Shoes go here.",
                   ("Où sont les chaussures ?", "Where are the shoes?"), ("Les chaussons sont là-bas.", "The slippers are over there.")),
            phrase("ただいま。 — おかえりなさい。", "Je suis rentré. — Bon retour.", "I'm home. — Welcome back.",
                   ("J'y vais. — À tout à l'heure.", "I'm off. — See you later."), ("Bonjour. — Bonsoir.", "Hello. — Good evening.")),
            phrase("みずを ください。", "De l'eau, s'il vous plaît.", "Water, please.",
                   ("Du thé, s'il vous plaît.", "Tea, please."), ("Où est l'eau ?", "Where's the water?")),
        ],
    },
    {
        "s": fe("Au restaurant : commander", "At the restaurant: ordering"),
        "scene": None,
        "tableau": {
            "t": fe("Commander : ～を おねがいします", "Ordering: ～を おねがいします"),
            "l": [ligne("なんめいさまですか", "nanmei-sama desu ka", "combien êtes-vous ?", "how many people?"),
                  ligne("ふたりです", "futari desu", "nous sommes deux", "two of us"),
                  ligne("メニューを おねがいします", "menyū o onegai shimasu", "la carte, s'il vous plaît", "the menu, please"),
                  ligne("これに します", "kore ni shimasu", "je prends ceci", "I'll have this"),
                  ligne("おかいけい おねがいします", "okaikei onegai shimasu", "l'addition, s'il vous plaît", "the bill, please")],
            "a": fe("おねがいします est la demande polie passe-partout, plus douce que ください. "
                    "Pour choisir, on montre et on dit これに します. On paie souvent à la caisse, en sortant, et sans pourboire.",
                    "おねがいします is the all-purpose polite request, softer than ください. "
                    "To choose, point and say これに します. You often pay at the till on the way out, with no tip."),
        },
        "cartes": [
            carte("おねがいします", "onegai shimasu", "s'il vous plaît (demande polie)", "please (polite request)"),
            carte("メニュー", "menyū", "carte, menu", "menu"),
            carte("これに します", "kore ni shimasu", "je prends ceci", "I'll have this"),
            carte("ラーメン", "rāmen", "ramen (nouilles)", "ramen (noodles)"),
            carte("すし", "sushi", "sushi", "sushi"),
            carte("ビール", "bīru", "bière", "beer"),
            carte("おかいけい", "okaikei", "l'addition", "the bill"),
            carte("べつべつに", "betsubetsu ni", "séparément", "separately", "べつべつに おねがいします。", "", "Séparément, s'il vous plaît.", "Separately, please."),
            carte("いっしょに", "issho ni", "ensemble", "together"),
            carte("ふたり", "futari", "deux personnes", "two people"),
            carte("おいしかったです", "oishikatta desu", "c'était délicieux", "it was delicious"),
            carte("おすすめは", "osusume wa", "que me conseillez-vous ?", "what do you recommend?", "おすすめは なんですか。", "", "Que me conseillez-vous ?", "What do you recommend?"),
        ],
        "phrases": [
            phrase("メニューを おねがいします。", "La carte, s'il vous plaît.", "The menu, please.",
                   ("L'addition, s'il vous plaît.", "The bill, please."), ("De l'eau, s'il vous plaît.", "Water, please.")),
            phrase("ラーメンに します。", "Je prends les ramen.", "I'll have the ramen.",
                   ("Je n'aime pas les ramen.", "I don't like ramen."), ("Où sont les ramen ?", "Where's the ramen?")),
            phrase("ビールを ふたつ ください。", "Deux bières, s'il vous plaît.", "Two beers, please.",
                   ("Une bière, s'il vous plaît.", "One beer, please."), ("Deux thés, s'il vous plaît.", "Two teas, please.")),
            phrase("おかいけい おねがいします。", "L'addition, s'il vous plaît.", "The bill, please.",
                   ("La carte, s'il vous plaît.", "The menu, please."), ("C'était délicieux.", "It was delicious.")),
            phrase("べつべつに おねがいします。", "Séparément, s'il vous plaît.", "Separately, please.",
                   ("Ensemble, s'il vous plaît.", "Together, please."), ("Par carte, s'il vous plaît.", "By card, please.")),
            phrase("ふたりです。", "Nous sommes deux.", "There are two of us.",
                   ("Nous sommes trois.", "There are three of us."), ("Je suis seul.", "I'm alone.")),
        ],
    },
    {
        "s": fe("Se débrouiller : quand on ne comprend pas", "Getting by: when you don't understand"),
        "scene": None,
        "tableau": {
            "t": fe("Comprendre, ne pas comprendre", "Understanding, not understanding"),
            "l": [ligne("わかりません", "wakarimasen", "je ne comprends pas", "I don't understand"),
                  ligne("もう いちど おねがいします", "mō ichido onegai shimasu", "encore une fois, s'il vous plaît", "once more, please"),
                  ligne("ゆっくり おねがいします", "yukkuri onegai shimasu", "plus lentement, s'il vous plaît", "more slowly, please"),
                  ligne("えいごで いいですか", "eigo de ii desu ka", "en anglais, ça va ?", "is English OK?"),
                  ligne("にほんごは すこしだけ です", "nihongo wa sukoshi dake desu", "je parle juste un peu japonais", "I only speak a little Japanese")],
            "a": fe("Ces cinq phrases te sortent de presque tout. わかります = je comprends ; ません le met au négatif. "
                    "だいじょうぶです = ça va, pas de problème (et aussi « non merci »).",
                    "These five sentences get you out of almost anything. わかります = I understand; ません makes it negative. "
                    "だいじょうぶです = it's fine, no problem (and also “no thanks”)."),
        },
        "cartes": [
            carte("わかります", "wakarimasu", "je comprends", "I understand"),
            carte("わかりません", "wakarimasen", "je ne comprends pas", "I don't understand"),
            carte("もう いちど", "mō ichido", "encore une fois", "once more"),
            carte("ゆっくり", "yukkuri", "lentement", "slowly"),
            carte("すこし", "sukoshi", "un peu", "a little"),
            carte("にほんご", "nihongo", "le japonais (langue)", "Japanese (language)"),
            carte("えいご", "eigo", "l'anglais", "English"),
            carte("フランスご", "furansugo", "le français", "French"),
            carte("だいじょうぶです", "daijōbu desu", "ça va, pas de problème", "it's fine, no problem"),
            carte("たすけて", "tasukete", "au secours !", "help!"),
            carte("びょういん", "byōin", "hôpital", "hospital"),
            carte("いいですか", "ii desu ka", "c'est possible ? je peux ?", "is it OK? may I?", "しゃしんを とっても いいですか。", "", "Je peux prendre une photo ?", "May I take a photo?"),
        ],
        "phrases": [
            phrase("すみません、 わかりません。", "Désolé, je ne comprends pas.", "Sorry, I don't understand.",
                   ("Désolé, je comprends.", "Sorry, I understand."), ("Merci, je sais.", "Thanks, I know.")),
            phrase("もう いちど おねがいします。", "Encore une fois, s'il vous plaît.", "Once more, please.",
                   ("Plus lentement, s'il vous plaît.", "More slowly, please."), ("Merci beaucoup.", "Thank you very much.")),
            phrase("ゆっくり おねがいします。", "Plus lentement, s'il vous plaît.", "More slowly, please.",
                   ("Plus vite, s'il vous plaît.", "Faster, please."), ("Encore une fois, s'il vous plaît.", "Once more, please.")),
            phrase("にほんごは すこしだけ です。", "Je parle juste un peu japonais.", "I only speak a little Japanese.",
                   ("Je parle bien japonais.", "I speak Japanese well."), ("Je ne parle pas anglais.", "I don't speak English.")),
            phrase("えいごで いいですか。", "En anglais, ça va ?", "Is English OK?",
                   ("Vous parlez français ?", "Do you speak French?"), ("C'est en japonais ?", "Is it in Japanese?")),
            phrase("トイレは どこですか。", "Où sont les toilettes ?", "Where's the toilet?",
                   ("Les toilettes sont ici.", "The toilet is here."), ("C'est la sortie ?", "Is this the exit?")),
        ],
    },
]


def main():
    for e in ETAPES:
        assert e["tableau"]["l"] and len(e["cartes"]) >= 8 and len(e["phrases"]) >= 4
        for p in e["phrases"]:
            assert len(p["l"]) == 2 and p["s"]["fr"] and p["s"]["en"]
    with io.open(os.path.join(ICI, "premiers-pas.json"), "w", encoding="utf-8", newline="\n") as fo:
        json.dump({"_lisez_moi": ["Derive de japonais/datos/premiers_pas_construire.py : ne pas modifier a la main.",
                                  "Brouillon, a faire relire par un natif."],
                   "etapes": ETAPES}, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    print("%d etapes, %d cartes, %d phrases -> premiers-pas.json"
          % (len(ETAPES), sum(len(e["cartes"]) for e in ETAPES), sum(len(e["phrases"]) for e in ETAPES)))


if __name__ == "__main__":
    main()
