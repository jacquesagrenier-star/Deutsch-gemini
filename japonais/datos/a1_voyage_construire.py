# -*- coding: utf-8 -*-
"""Construit japonais/datos/a1-voyage.json : l'A1 voyage du japonais.

    python japonais/datos/a1_voyage_construire.py      (apres construire.py : il lit themes.json & co)

LE MEME FORMAT QUE espanol/datos/a1-voyage.json et portugais/datos/a1-voyage.json,
lu par le meme moteur (chargerA1Voyage, preparerA1Voyage) : 12 escales (10 « tous »,
2 « voyage »), 2 etapes « installe », la suite en 8 etapes. Demande de Jacques,
11 nov. 2026 (lot J3 de audit/ALIGNEMENT-LANGUES-2026-11-11.md) : le japonais au
meme niveau que l'espagnol et l'allemand.

Ce qui change pour le japonais (memes conventions que premiers_pas_construire.py) :
  - les phrases sont en kana, AVEC DES ESPACES entre les groupes de mots (le
    debutant lit les kana ; l'exercice des repliques decoupe sur les espaces) ;
  - une ligne de tableau porte en 3e position la prononciation (kana · romaji),
    comme les Premiers pas et les reperes, et le romaji est ecrit a la main
    (は particule = wa, を = o, へ = e) ;
  - chaque sens a le francais et l'anglais (les deux langues d'interface) ;
  - « mots » NOMME des mots du corpus A1 japonais tels que les cartes les ecrivent
    (champ « mot » : kanji quand la carte en a) ; un mot absent arrete le script ;
  - « scenes » : les scenes de Camille (scene-<nom>.ja.js), dans l'ordre de l'annee.
    Tant que la seance japonaise ne montre pas de scene (garde du lot J1), elles
    attendent ; le moteur les trouvera dans SCENES_JA.

Formats des textes :
  - tableau « l » : « japonais | romaji | sens fr | sens en » ;
  - blocs : « phrase avec … | sens fr avec … | sens en avec … | 3 variantes / | 3 fr / | 3 en / »,
    l'exemple prend la 3e variante ;
  - dialogue : « eux|moi | replique | sens fr | sens en ».
Brouillon : a faire relire par un natif.
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))

ESCALES = [
{"id": "arriver", "pour": "tous", "icone": "🛬",
 "s": ("Arriver au Japon : l'aéroport, l'auberge", "Arriving in Japan: the airport, the inn"),
 "scenes": ["kuukou", "ryokan"],
 "mots": "飛行機, 荷物, ホテル, 旅行, 外国, 外国人, 大使館, 地図, エレベーター, 着く, 来る, 降りる, 帰る, 寝る, ようこそ, …と申します, お名前は",
 "tableau": {"t": ("Venir, arriver : ～に きました", "Coming, arriving: ～に きました"),
  "l": """にほんに きました | nihon ni kimashita | je suis venu(e) au Japon | I came to Japan
カナダから きました | kanada kara kimashita | je viens du Canada | I'm from Canada
くうこうに つきました | kūkō ni tsukimashita | je suis arrivé(e) à l'aéroport | I arrived at the airport
ホテルに いきます | hoteru ni ikimasu | je vais à l'hôtel | I'm going to the hotel
なんじに つきますか | nanji ni tsukimasu ka | à quelle heure arrivez-vous ? | what time do you arrive?
あした かえります | ashita kaerimasu | je rentre demain | I'm going home tomorrow""",
  "a": ("Le lieu où l'on va ou arrive prend に : ホテルに いきます. Le lieu d'où l'on vient prend から : カナダから きました. ～ました, c'est le passé poli de ～ます.",
        "The place you go to or arrive at takes に: ホテルに いきます. The place you come from takes から: カナダから きました. ～ました is the polite past of ～ます.")},
 "blocs": """…と もうします。 | Je m'appelle …. | My name is …. | マルタン / ポール / トランブレ | Martin / Paul / Tremblay | Martin / Paul / Tremblay
…から きました。 | Je viens …. | I'm from …. | フランス / ベルギー / カナダ | de France / de Belgique / du Canada | France / Belgium / Canada
…は どこですか。 | Où est … ? | Where is …? | でぐち / エレベーター / タクシーのりば | la sortie / l'ascenseur / la station de taxis | the exit / the lift / the taxi rank
…を おねがいします。 | …, s'il vous plaît. | …, please. | かぎ / タオル / ちず | La clé / Une serviette / Un plan | The key / A towel / A map""",
 "dialogue": {"t": ("À la réception de l'auberge", "At the inn's front desk"), "l": """eux | いらっしゃいませ。ごよやくですか。 | Bienvenue. Vous avez réservé ? | Welcome. Do you have a reservation?
moi | はい、トランブレと もうします。 | Oui, je m'appelle Tremblay. | Yes, my name is Tremblay.
eux | トランブレさまですね。パスポートを おねがいします。 | Madame Tremblay, très bien. Votre passeport, s'il vous plaît. | Ms Tremblay, yes. Your passport, please.
moi | はい、どうぞ。 | Voici. | Here you are.
eux | こちらが へやの かぎです。ごゆっくり どうぞ。 | Voici la clé de la chambre. Reposez-vous bien. | Here's your room key. Enjoy your stay.
moi | ありがとうございます。 | Merci beaucoup. | Thank you very much."""}},

{"id": "manger", "pour": "tous", "icone": "🍜",
 "s": ("Manger : le ramen, le café", "Eating: ramen, the café"),
 "scenes": ["raamen", "kissaten"],
 "mots": "朝ごはん, 昼ご飯, 晩御飯, 御飯, 水, お茶, コーヒー, 紅茶, 牛乳, 飲み物, 食べ物, 料理, 卵, 肉, 箸, スプーン, コップ, カップ, お皿, レストラン, 喫茶店, 食堂, 食べる, 飲む, 頼む, おいしい, 辛い, 甘い, お会計お願いします, 英語のメニューはありますか",
 "tableau": {"t": ("Manger, boire : ～を たべます", "Eating, drinking: ～を たべます"),
  "l": """ラーメンを たべます | rāmen o tabemasu | je mange des ramen | I eat ramen
コーヒーを のみます | kōhī o nomimasu | je bois du café | I drink coffee
なにを たべますか | nani o tabemasu ka | qu'est-ce que vous mangez ? | what will you eat?
おちゃを のみませんか | ocha o nomimasen ka | vous prenez un thé ? | would you like some tea?
にくは たべません | niku wa tabemasen | je ne mange pas de viande | I don't eat meat
とても おいしいです | totemo oishii desu | c'est très bon | it's delicious""",
  "a": ("Ce qu'on mange ou boit prend を (lu « o »). La négation polie : ～ません. ～ませんか invite poliment : « vous ne voulez pas… ? ». Au restaurant de ramen, on paie d'abord au distributeur, puis on donne le ticket.",
        "What you eat or drink takes を (read “o”). The polite negative is ～ません. ～ませんか is a polite invitation: “won't you…?”. In a ramen shop you pay first at the ticket machine, then hand over the ticket.")},
 "blocs": """…を ください。 | …, s'il vous plaît. | …, please. | ラーメン / ぎょうざ / おみず | Un ramen / Des gyoza / De l'eau | A ramen / Some gyoza / Some water
…を ひとつ おねがいします。 | Un …, s'il vous plaît. | One …, please. | コーヒー / こうちゃ / ケーキ | café / thé / gâteau | coffee / tea / cake
…は ありますか。 | Vous avez … ? | Do you have …? | えいごの メニュー / スプーン / フォーク | un menu en anglais / une cuillère / une fourchette | an English menu / a spoon / a fork
…が すきです。 | J'aime …. | I like …. | すし / てんぷら / ラーメン | les sushis / les tempuras / les ramen | sushi / tempura / ramen""",
 "dialogue": {"t": ("Au café", "At the café"), "l": """eux | いらっしゃいませ。なんめいさまですか。 | Bienvenue. Vous êtes combien ? | Welcome. How many of you?
moi | ひとりです。 | Je suis seul(e). | Just one.
eux | ごちゅうもんは。 | Qu'est-ce que vous prenez ? | What would you like?
moi | コーヒーを ひとつ おねがいします。 | Un café, s'il vous plaît. | One coffee, please.
eux | はい、しょうしょう おまちください。 | Très bien, un instant. | Certainly, just a moment.
moi | おかいけい おねがいします。 | L'addition, s'il vous plaît. | The bill, please."""}},

{"id": "marche", "pour": "tous", "icone": "🛒",
 "s": ("Faire les courses : le supermarché, le konbini", "Buying food: the supermarket, the konbini"),
 "scenes": ["suupaa", "konbini"],
 "mots": "野菜, 果物, 魚, 牛肉, 豚肉, 鶏肉, パン, バター, 砂糖, 塩, 醤油, お菓子, 飴, お弁当, 八百屋, 店, 買い物, いくら, 買う, 売る, 安い, 高い, 一つ, 二つ, 三つ, いくらですか, これをください, いらっしゃいませ",
 "tableau": {"t": ("Compter les choses : ひとつ, ふたつ", "Counting things: ひとつ, ふたつ"),
  "l": """りんごを ひとつ ください | ringo o hitotsu kudasai | une pomme, s'il vous plaît | one apple, please
たまごを ふたつ かいます | tamago o futatsu kaimasu | j'achète deux œufs | I'm buying two eggs
パンを みっつ ください | pan o mittsu kudasai | trois petits pains, s'il vous plaît | three rolls, please
これは いくらですか | kore wa ikura desu ka | combien coûte ceci ? | how much is this?
ひゃくえんです | hyaku en desu | c'est cent yens | it's a hundred yen
ぜんぶで せんえんです | zenbu de sen en desu | en tout, mille yens | that's a thousand yen altogether""",
  "a": ("ひとつ, ふたつ, みっつ comptent les objets sans compteur propre ; le nombre se place après la chose et を : りんごを ふたつ. Les prix se disent en えん (yens).",
        "ひとつ, ふたつ, みっつ count things that have no counter of their own; the number comes after the thing and を: りんごを ふたつ. Prices are in えん (yen).")},
 "blocs": """…を ふたつ ください。 | Deux …, s'il vous plaît. | Two …, please. | りんご / トマト / おにぎり | pommes / tomates / onigiri | apples / tomatoes / onigiri
…は どこですか。 | Où est … ? | Where is …? | しょうゆ / さとう / パン | la sauce soja / le sucre / le pain | the soy sauce / the sugar / the bread
…で おねがいします。 | Par …, s'il vous plaît. | By …, please. | カード / げんきん / スマホ | carte / espèces / téléphone | card / cash / phone""",
 "dialogue": {"t": ("À la caisse du konbini", "At the konbini till"), "l": """eux | いらっしゃいませ。ふくろは いりますか。 | Bonjour. Vous voulez un sac ? | Hello. Do you need a bag?
moi | いいえ、だいじょうぶです。 | Non, ça ira. | No, I'm fine.
eux | おべんとうは あたためますか。 | Je vous réchauffe le bento ? | Shall I heat up your bento?
moi | はい、おねがいします。 | Oui, s'il vous plaît. | Yes, please.
eux | ぜんぶで ごひゃくえんです。 | Ça fait cinq cents yens en tout. | That's five hundred yen altogether.
moi | カードで おねがいします。 | Par carte, s'il vous plaît. | By card, please."""}},

{"id": "ville", "pour": "tous", "icone": "🏙️",
 "s": ("La ville : se repérer, se promener", "The city: finding your way, going for a walk"),
 "scenes": ["hanami", "furusato"],
 "mots": "町, 公園, 建物, 図書館, 橋, 道, 角, 交差点, 右, 左, 前, 後ろ, 隣, 近く, 向こう, 入口, 出口, 散歩, 歩く, 曲がる, 渡る, まっすぐ, 近い, 遠い",
 "tableau": {"t": ("Où se trouve : ～は どこですか", "Where is it: ～は どこですか"),
  "l": """こうえんは どこですか | kōen wa doko desu ka | où est le parc ? | where is the park?
まっすぐ いって ください | massugu itte kudasai | allez tout droit | go straight ahead
つぎの かどを みぎに まがって ください | tsugi no kado o migi ni magatte kudasai | tournez à droite au prochain coin | turn right at the next corner
はしを わたって ください | hashi o watatte kudasai | traversez le pont | cross the bridge
えきの まえに あります | eki no mae ni arimasu | c'est devant la gare | it's in front of the station
ここから ちかいです | koko kara chikai desu | c'est près d'ici | it's close to here""",
  "a": ("～て ください demande poliment : いって ください (allez), まがって ください (tournez). Le lieu se situe avec の : えきの まえ (devant la gare), ぎんこうの となり (à côté de la banque).",
        "～て ください is a polite request: いって ください (go), まがって ください (turn). Places are located with の: えきの まえ (in front of the station), ぎんこうの となり (next to the bank).")},
 "blocs": """…は どこですか。 | Où est … ? | Where is …? | こうえん / としょかん / こうばん | le parc / la bibliothèque / le poste de police | the park / the library / the police box
…を まがって ください。 | Tournez …. | Please turn …. | つぎの かど / その かど / こうさてん | au prochain coin / à ce coin-là / au carrefour | at the next corner / at that corner / at the crossroads
…の まえで まちます。 | J'attends devant …. | I'll wait in front of …. | えき / ぎんこう / としょかん | la gare / la banque / la bibliothèque | the station / the bank / the library""",
 "dialogue": {"t": ("Demander son chemin", "Asking the way"), "l": """eux | どう しましたか。 | Je peux vous aider ? | Can I help you?
moi | こうえんは どこですか。 | Où est le parc ? | Where is the park?
eux | まっすぐ いって、はしを わたって ください。 | Allez tout droit et traversez le pont. | Go straight on and cross the bridge.
moi | とおいですか。 | C'est loin ? | Is it far?
eux | いいえ、あるいて ごふんです。 | Non, cinq minutes à pied. | No, five minutes on foot.
moi | ありがとうございます。 | Merci beaucoup. | Thank you very much."""}},

{"id": "transports", "pour": "tous", "icone": "🚃",
 "s": ("Les transports : la gare, le shinkansen", "Getting around: the station, the shinkansen"),
 "scenes": ["eki", "shinkansen"],
 "mots": "駅, 電車, 地下鉄, バス, タクシー, 車, 自動車, 自転車, 切符, 番号, 時間, 乗る, 待つ, 出る, 止まる, かかる, 早い, 遅い, 次, 東, 西, 北, 南, ドアが閉まります",
 "tableau": {"t": ("Prendre un transport : ～に のります", "Taking transport: ～に のります"),
  "l": """でんしゃに のります | densha ni norimasu | je prends le train | I take the train
バスで いきます | basu de ikimasu | j'y vais en bus | I go by bus
つぎの えきで おります | tsugi no eki de orimasu | je descends à la prochaine gare | I get off at the next station
なんじに でますか | nanji ni demasu ka | à quelle heure part-il ? | what time does it leave?
じかんが かかります | jikan ga kakarimasu | ça prend du temps | it takes a while
しんじゅくまで いくらですか | shinjuku made ikura desu ka | combien jusqu'à Shinjuku ? | how much to Shinjuku?""",
  "a": ("On monte DANS un véhicule avec に : でんしゃに のります ; le moyen se dit avec で : バスで いきます. まで : jusqu'à. Dans le train, on entend souvent : ドアが しまります (les portes se ferment).",
        "You get ON a vehicle with に: でんしゃに のります; the means takes で: バスで いきます. まで: as far as. On the train you'll often hear: ドアが しまります (the doors are closing).")},
 "blocs": """…まで いくらですか。 | Combien jusqu'à … ? | How much to …? | しんじゅく / きょうと / かなざわ | Shinjuku / Kyoto / Kanazawa | Shinjuku / Kyoto / Kanazawa
…で いきます。 | J'y vais en …. | I go by …. | でんしゃ / バス / タクシー | train / bus / taxi | train / bus / taxi
…は なんばんせんですか。 | … part de quel quai ? | Which platform does … leave from? | しんかんせん / つぎの でんしゃ / ちかてつ | Le shinkansen / Le prochain train / Le métro | the shinkansen / the next train / the subway
…に のりかえます。 | Je change pour …. | I change to …. | ちかてつ / バス / やまのてせん | le métro / le bus / la ligne Yamanote | the subway / the bus / the Yamanote line""",
 "dialogue": {"t": ("Au guichet de la gare", "At the ticket office"), "l": """eux | いらっしゃいませ。 | Bonjour. | Hello.
moi | かなざわまで おとな いちまい おねがいします。 | Un billet adulte pour Kanazawa, s'il vous plaît. | One adult ticket to Kanazawa, please.
eux | じゆうせきと していせき、どちらに しますか。 | Place libre ou place réservée ? | Unreserved or reserved seat?
moi | していせきで おねがいします。 | Une place réservée, s'il vous plaît. | A reserved seat, please.
eux | じゅうじの しんかんせんです。じゅうよんばんせんです。 | C'est le shinkansen de dix heures, quai quatorze. | It's the ten o'clock shinkansen, platform fourteen.
moi | わかりました。ありがとうございます。 | D'accord, merci beaucoup. | Got it, thank you very much."""}},

{"id": "achats", "pour": "tous", "icone": "🛍️",
 "s": ("Les achats : le grand magasin, les vêtements", "Shopping: the department store, clothes"),
 "scenes": ["depaato"],
 "mots": "デパート, 服, 洋服, シャツ, ワイシャツ, ズボン, スカート, セーター, コート, 上着, 靴, 靴下, 帽子, ネクタイ, ハンカチ, かばん, 財布, お金, 大きい, 小さい, 長い, 短い, 色, 赤い, 青い, 白い, 黒い, 欲しい, 着る, 見せる",
 "tableau": {"t": ("Décrire et choisir : les adjectifs en い", "Describing and choosing: い-adjectives"),
  "l": """この シャツは おおきいです | kono shatsu wa ōkii desu | cette chemise est grande | this shirt is big
もっと ちいさいのは ありますか | motto chiisai no wa arimasu ka | vous en avez une plus petite ? | do you have a smaller one?
あかい セーターが ほしいです | akai sētā ga hoshii desu | je voudrais un pull rouge | I'd like a red sweater
くつは たかくないです | kutsu wa takakunai desu | les chaussures ne sont pas chères | the shoes aren't expensive
きて みても いいですか | kite mite mo ii desu ka | je peux l'essayer ? | can I try it on?
これに します | kore ni shimasu | je prends celui-ci | I'll take this one""",
  "a": ("L'adjectif en い se place devant le nom (あかい セーター) ou finit la phrase (おおきいです). Négation : い devient くない : たかい → たかくない. ～が ほしいです : je voudrais.",
        "An い-adjective comes before the noun (あかい セーター) or ends the sentence (おおきいです). Negative: い becomes くない: たかい → たかくない. ～が ほしいです: I'd like.")},
 "blocs": """…を みせて ください。 | Montrez-moi …, s'il vous plaît. | Please show me …. | あの かばん / その さいふ / あの くつ | ce sac-là / ce portefeuille / ces chaussures-là | that bag / that wallet / those shoes
…は ありますか。 | Vous avez … ? | Do you have …? | もっと おおきいの / もっと ちいさいの / ほかの いろ | plus grand / plus petit / une autre couleur | a bigger one / a smaller one / another colour
…が ほしいです。 | Je voudrais …. | I'd like …. | あたらしい くつ / あかい セーター / くろい コート | des chaussures neuves / un pull rouge / un manteau noir | new shoes / a red sweater / a black coat""",
 "dialogue": {"t": ("Au rayon des vêtements", "In the clothes department"), "l": """eux | いらっしゃいませ。なにを おさがしですか。 | Bonjour. Vous cherchez quelque chose ? | Hello. Are you looking for something?
moi | セーターが ほしいです。 | Je voudrais un pull. | I'd like a sweater.
eux | こちらは いかがですか。 | Que pensez-vous de celui-ci ? | How about this one?
moi | きて みても いいですか。 | Je peux l'essayer ? | Can I try it on?
eux | はい、どうぞ。 | Oui, je vous en prie. | Yes, go ahead.
moi | これに します。 | Je prends celui-ci. | I'll take this one."""}},

{"id": "sante", "pour": "tous", "icone": "💊",
 "s": ("La santé : la pharmacie, le médecin", "Health: the pharmacy, the doctor"),
 "scenes": ["kusuriya"],
 "mots": "医者, 風邪, 薬, 病院, 病気, 頭, お腹, 歯, 目, 耳, 鼻, 口, 手, 足, 体, 声, 痛い, 疲れる, 休む, 元気, 大丈夫, 大丈夫ですか, 気をつけて",
 "tableau": {"t": ("Avoir mal : ～が いたいです", "Being in pain: ～が いたいです"),
  "l": """あたまが いたいです | atama ga itai desu | j'ai mal à la tête | I have a headache
おなかが いたいです | onaka ga itai desu | j'ai mal au ventre | I have a stomach ache
ねつが あります | netsu ga arimasu | j'ai de la fièvre | I have a fever
かぜを ひきました | kaze o hikimashita | j'ai attrapé un rhume | I've caught a cold
くすりを のみます | kusuri o nomimasu | je prends un médicament | I take some medicine
ゆっくり やすんで ください | yukkuri yasunde kudasai | reposez-vous bien | get plenty of rest""",
  "a": ("La partie du corps + が + いたいです : あたまが いたいです. Un médicament « se boit » : くすりを のみます, même en comprimés.",
        "Body part + が + いたいです: あたまが いたいです. In Japanese you “drink” medicine: くすりを のみます, even tablets.")},
 "blocs": """…が いたいです。 | J'ai mal …. | My … hurts. | あたま / のど / おなか | à la tête / à la gorge / au ventre | head / throat / stomach
…の くすりは ありますか。 | Vous avez quelque chose contre … ? | Do you have something for …? | かぜ / ずつう / ねつ | le rhume / le mal de tête / la fièvre | a cold / a headache / a fever
…から いたいです。 | J'ai mal depuis …. | It started hurting …. | きのう / けさ / みっか まえ | hier / ce matin / trois jours | yesterday / this morning / three days ago""",
 "dialogue": {"t": ("À la pharmacie", "At the pharmacy"), "l": """eux | どう しましたか。 | Qu'est-ce qui ne va pas ? | What seems to be the problem?
moi | かぜを ひきました。 | J'ai attrapé un rhume. | I've caught a cold.
eux | ねつは ありますか。 | Vous avez de la fièvre ? | Do you have a fever?
moi | すこし あります。のども いたいです。 | Un peu. J'ai mal à la gorge aussi. | A little. My throat hurts too.
eux | この くすりを いちにち さんかい のんで ください。 | Prenez ce médicament trois fois par jour. | Take this medicine three times a day.
moi | わかりました。ありがとうございます。 | D'accord. Merci beaucoup. | All right. Thank you very much."""}},

{"id": "imprevus", "pour": "tous", "icone": "☔",
 "s": ("Les imprévus : se perdre, perdre ses affaires", "Mishaps: getting lost, losing things"),
 "scenes": ["tsuyu"],
 "mots": "交番, おまわりさん, 警官, 傘, 雨, 風, 天気, 電話, 問題, 困る, なくす, 忘れる, 呼ぶ, わかる, ちょっと待ってください, わかりません, もう一度お願いします, ゆっくりお願いします, 失礼しました, 違います",
 "tableau": {"t": ("Perdre, oublier : ～を なくしました", "Losing, forgetting: ～を なくしました"),
  "l": """さいふを なくしました | saifu o nakushimashita | j'ai perdu mon portefeuille | I've lost my wallet
かさを わすれました | kasa o wasuremashita | j'ai oublié mon parapluie | I left my umbrella behind
みちが わかりません | michi ga wakarimasen | je ne connais pas le chemin | I don't know the way
こまって います | komatte imasu | j'ai un problème | I'm in trouble
もう いちど おねがいします | mō ichido onegai shimasu | encore une fois, s'il vous plaît | once more, please
ゆっくり はなして ください | yukkuri hanashite kudasai | parlez lentement, s'il vous plaît | please speak slowly""",
  "a": ("～を なくしました : j'ai perdu ; ～を わすれました : j'ai oublié (laissé quelque part). Un objet perdu au Japon revient très souvent : on le signale au こうばん, le petit poste de police du quartier.",
        "～を なくしました: I've lost; ～を わすれました: I left (something) behind. Lost things very often come back in Japan: you report them at the こうばん, the little neighbourhood police box.")},
 "blocs": """…を なくしました。 | J'ai perdu …. | I've lost …. | パスポート / かぎ / けいたい | mon passeport / ma clé / mon portable | my passport / my key / my phone
…を わすれました。 | J'ai oublié …. | I left … behind. | かさ / かばん / ノート | mon parapluie / mon sac / mon carnet | my umbrella / my bag / my notebook
…を よんで ください。 | Appelez …, s'il vous plaît. | Please call …. | タクシー / いしゃ / けいさつ | un taxi / un médecin / la police | a taxi / a doctor / the police""",
 "dialogue": {"t": ("Au poste de police", "At the police box"), "l": """eux | どう しましたか。 | Qu'est-ce qui se passe ? | What's the matter?
moi | さいふを なくしました。 | J'ai perdu mon portefeuille. | I've lost my wallet.
eux | どこで なくしましたか。 | Où l'avez-vous perdu ? | Where did you lose it?
moi | わかりません。えきの ちかくだと おもいます。 | Je ne sais pas. Près de la gare, je crois. | I don't know. Near the station, I think.
eux | なまえと でんわばんごうを かいて ください。 | Écrivez votre nom et votre numéro de téléphone. | Please write your name and phone number.
moi | はい。よろしく おねがいします。 | D'accord. Merci de votre aide. | All right. Thank you for your help."""}},

{"id": "services", "pour": "tous", "icone": "📮",
 "s": ("Les services : la poste, le bain public", "Services: the post office, the public bath"),
 "scenes": ["yuubinkyoku", "sentou"],
 "mots": "郵便局, 切手, 手紙, はがき, 封筒, ポスト, 銀行, 風呂, お風呂, 石鹸, 洗濯, 出す, 貼る, 洗う, 浴びる, 入る",
 "tableau": {"t": ("Envoyer : ～を だします", "Sending: ～を だします"),
  "l": """てがみを だします | tegami o dashimasu | je poste une lettre | I'm posting a letter
きってを はります | kitte o harimasu | je colle un timbre | I put on a stamp
カナダまで いくらですか | kanada made ikura desu ka | combien pour le Canada ? | how much to Canada?
こうくうびんで おねがいします | kōkūbin de onegai shimasu | par avion, s'il vous plaît | airmail, please
おふろに はいります | ofuro ni hairimasu | je prends un bain | I take a bath
からだを あらって から はいります | karada o aratte kara hairimasu | on se lave avant d'entrer dans le bain | you wash before getting into the bath""",
  "a": ("だします : envoyer, poster (litt. « sortir »). Au bain public, on se lave assis sur un tabouret AVANT d'entrer dans l'eau, et la petite serviette ne va jamais dans le bain.",
        "だします: to send, to post (literally “to put out”). At a public bath you wash sitting on a stool BEFORE getting into the water, and the small towel never goes in the bath.")},
 "blocs": """これを …まで おねがいします。 | Ceci pour …, s'il vous plaît. | This to …, please. | フランス / カナダ / かなざわ | la France / le Canada / Kanazawa | France / Canada / Kanazawa
…を ください。 | …, s'il vous plaît. | …, please. | きって ごまい / ふうとう / はがき | Cinq timbres / Une enveloppe / Une carte postale | Five stamps / An envelope / A postcard
…で おくって ください。 | Envoyez-le par …, s'il vous plaît. | Please send it by …. | こうくうびん / ふなびん / そくたつ | avion / bateau / exprès | airmail / sea mail / express""",
 "dialogue": {"t": ("Au guichet de la poste", "At the post office counter"), "l": """eux | いらっしゃいませ。 | Bonjour. | Hello.
moi | この こづつみを カナダまで おねがいします。 | Ce colis pour le Canada, s'il vous plaît. | This parcel to Canada, please.
eux | こうくうびんですか、ふなびんですか。 | Par avion ou par bateau ? | Airmail or sea mail?
moi | こうくうびんで おねがいします。 | Par avion, s'il vous plaît. | Airmail, please.
eux | にせんえんです。ここに じゅうしょを かいて ください。 | Deux mille yens. Écrivez l'adresse ici. | Two thousand yen. Please write the address here.
moi | はい、わかりました。 | Oui, d'accord. | Yes, all right."""}},

{"id": "rencontrer", "pour": "tous", "icone": "🍶",
 "s": ("Rencontrer : la famille, les collègues", "Meeting people: family, colleagues"),
 "scenes": ["sofu-no-ie", "izakaya"],
 "mots": "友達, 皆さん, みんな, 人, 方, 大人, 誕生日, パーティー, 一緒, 会う, 話す, 言う, 知る, 好き, 嫌い, 楽しい, 面白い, 初めて, お元気ですか, よろしくお願いします, おめでとうございます, お誕生日おめでとう, そうですか, 本当ですか, いいですね",
 "tableau": {"t": ("Se présenter : ～です", "Introducing yourself: ～です"),
  "l": """はじめまして | hajimemashite | enchanté(e) | nice to meet you
カミーユです | kamīyu desu | je suis Camille | I'm Camille
モントリオールから きました | montoriōru kara kimashita | je viens de Montréal | I'm from Montreal
バリスタです | barisuta desu | je suis barista | I'm a barista
にほんごを べんきょうして います | nihongo o benkyō shite imasu | j'étudie le japonais | I'm studying Japanese
どうぞ よろしく おねがいします | dōzo yoroshiku onegai shimasu | ravi(e) de vous connaître | pleased to meet you""",
  "a": ("Le premier mot d'une rencontre : はじめまして. Puis son nom + です, d'où l'on vient, et pour finir どうぞ よろしく おねがいします, avec une petite révérence. ～て います : ce qu'on est en train de faire.",
        "The first word when you meet someone: はじめまして. Then your name + です, where you're from, and finally どうぞ よろしく おねがいします, with a small bow. ～て います: what you're doing right now.")},
 "blocs": """しゅみは …です。 | Mon passe-temps, c'est …. | My hobby is …. | しゃしん / りょうり / さんぽ | la photo / la cuisine / la promenade | photography / cooking / walking
…で はたらいて います。 | Je travaille …. | I work …. | きっさてん / かいしゃ / がっこう | dans un café / dans une entreprise / dans une école | in a café / at a company / at a school
…を べんきょうして います。 | J'étudie …. | I'm studying …. | にほんご / かんじ / えいご | le japonais / les kanji / l'anglais | Japanese / kanji / English
…に かんぱい！ | À … ! | To …! | みなさん / ともだち / あたらしい しごと | tout le monde / nos amis / ton nouveau travail | everyone / our friends / your new job""",
 "dialogue": {"t": ("À l'izakaya avec les collègues", "At the izakaya with colleagues"), "l": """eux | はじめまして。さかもとさんの ともだちの たなかです。 | Enchanté. Je suis Tanaka, un ami de M. Sakamoto. | Nice to meet you. I'm Tanaka, a friend of Mr Sakamoto's.
moi | はじめまして。カミーユです。 | Enchantée. Je suis Camille. | Nice to meet you. I'm Camille.
eux | にほんごが じょうずですね。 | Votre japonais est très bon ! | Your Japanese is very good!
moi | いえいえ、まだまだです。 | Oh non, j'ai encore beaucoup à apprendre. | Oh no, I still have a long way to go.
eux | じゃあ、みなさん、かんぱい！ | Allez, tout le monde, santé ! | Right, everyone, cheers!
moi | かんぱい！ | Santé ! | Cheers!"""}},

{"id": "plage", "pour": "voyage", "icone": "🏖️",
 "s": ("La plage et les fêtes d'été", "The beach and summer festivals"),
 "scenes": ["kamakura", "natsumatsuri"],
 "mots": "海, 夏, 夏休み, 暑い, 涼しい, 冷たい, 泳ぐ, 遊ぶ, 空, 晴れ, 晴れる, 鳥, 写真, カメラ, 撮る, 歌, 歌う, 写真を撮ってもいいですか, はい、チーズ, すごい",
 "tableau": {"t": ("Proposer : ～ましょう", "Suggesting: ～ましょう"),
  "l": """うみに いきましょう | umi ni ikimashō | allons à la mer ! | let's go to the sea!
いっしょに およぎませんか | issho ni oyogimasen ka | on nage ensemble ? | shall we swim together?
きょうは あついですね | kyō wa atsui desu ne | il fait chaud aujourd'hui, hein | it's hot today, isn't it?
しゃしんを とりましょう | shashin o torimashō | prenons une photo | let's take a photo
はなびを みに いきます | hanabi o mi ni ikimasu | je vais voir les feux d'artifice | I'm going to see the fireworks
かきごおりを たべたいです | kakigōri o tabetai desu | j'ai envie d'une glace pilée | I want some shaved ice""",
  "a": ("～ましょう propose de faire ensemble (allons-y !), ～ませんか invite plus doucement. ね en fin de phrase cherche l'accord : あついですね (chaud, hein ?). ～たいです : avoir envie de.",
        "～ましょう suggests doing something together (let's!), ～ませんか is a gentler invitation. ね at the end looks for agreement: あついですね (hot, isn't it?). ～たいです: to want to.")},
 "blocs": """…に いきましょう。 | Allons …! | Let's go to …! | うみ / まつり / かまくら | à la mer / à la fête / à Kamakura | the sea / the festival / Kamakura
…を たべたいです。 | J'ai envie de …. | I want to eat …. | かきごおり / やきそば / アイス | glace pilée / nouilles sautées / glace | shaved ice / fried noodles / ice cream""",
 "dialogue": {"t": ("Une photo sur la plage", "A photo on the beach"), "l": """eux | すみません、しゃしんを とって もらえますか。 | Excusez-moi, vous pourriez nous prendre en photo ? | Excuse me, could you take our photo?
moi | いいですよ。はい、チーズ！ | Bien sûr. Souriez ! | Sure. Say cheese!
eux | ありがとうございます。どこから きましたか。 | Merci beaucoup. Vous venez d'où ? | Thank you very much. Where are you from?
moi | カナダから きました。 | Je viens du Canada. | I'm from Canada.
eux | そうですか。いい なつやすみを！ | Ah bon. Bonnes vacances d'été ! | Oh really. Have a good summer holiday!"""}},

{"id": "visiter", "pour": "voyage", "icone": "⛩️",
 "s": ("Visiter : sanctuaires et jardins", "Sightseeing: shrines and gardens"),
 "scenes": ["fushimi", "kenrokuen"],
 "mots": "山, 川, 木, 花, 池, 庭, 雪, 冬, 秋, 有名, 綺麗, 古い, 静か, 立派, 見る, 登る, 何時ですか, いい天気ですね",
 "tableau": {"t": ("Le passé poli : ～ました", "The polite past: ～ました"),
  "l": """きょうとに いきました | kyōto ni ikimashita | je suis allé(e) à Kyoto | I went to Kyoto
じんじゃを みました | jinja o mimashita | j'ai vu un sanctuaire | I saw a shrine
やまに のぼりました | yama ni noborimashita | je suis monté(e) sur la montagne | I climbed the mountain
とても きれいでした | totemo kirei deshita | c'était très beau | it was very beautiful
たのしかったです | tanoshikatta desu | c'était amusant | it was fun
しずかな にわでした | shizuka na niwa deshita | c'était un jardin paisible | it was a quiet garden""",
  "a": ("Le passé des verbes : ～ます → ～ました. Les adjectifs en な prennent でした (きれいでした) ; ceux en い changent eux-mêmes : たのしい → たのしかったです.",
        "The past of verbs: ～ます → ～ました. な-adjectives take でした (きれいでした); い-adjectives change themselves: たのしい → たのしかったです.")},
 "blocs": """…に いきたいです。 | Je voudrais aller …. | I'd like to go to …. | きょうと / ふじさん / かなざわ | à Kyoto / au mont Fuji / à Kanazawa | Kyoto / Mount Fuji / Kanazawa
…は なんじまでですか。 | … ferme à quelle heure ? | What time does … close? | にわ / びじゅつかん / おてら | Le jardin / Le musée / Le temple | the garden / the museum / the temple""",
 "dialogue": {"t": ("À l'entrée du jardin", "At the garden entrance"), "l": """eux | いらっしゃいませ。おとな なんまいですか。 | Bonjour. Combien de billets adulte ? | Hello. How many adult tickets?
moi | おとな にまい おねがいします。 | Deux adultes, s'il vous plaît. | Two adults, please.
eux | せんにひゃくえんです。 | Mille deux cents yens. | One thousand two hundred yen.
moi | なんじまで あいて いますか。 | C'est ouvert jusqu'à quelle heure ? | What time are you open until?
eux | ごご ごじまでです。ゆきに きを つけて ください。 | Jusqu'à cinq heures. Faites attention à la neige. | Until five o'clock. Watch out for the snow.
moi | はい、ありがとうございます。 | Oui, merci beaucoup. | Yes, thank you very much."""}},
]

INSTALLE = [
{"id": "logement", "pour": "installe", "icone": "🏠",
 "s": ("Le logement : la chambre, la propriétaire", "Housing: the room, the landlady"),
 "scenes": ["heya", "genkan"],
 "mots": "アパート, 家, 部屋, 鍵, ベッド, シャワー, 台所, トイレ, 階段, 玄関, 窓, 冷蔵庫, 住む, 掃除",
 "tableau": {"t": ("Il y a : あります, います", "There is: あります, います"),
  "l": """へやに ベッドが あります | heya ni beddo ga arimasu | il y a un lit dans la chambre | there's a bed in the room
だいどころは ありますか | daidokoro wa arimasu ka | il y a une cuisine ? | is there a kitchen?
エレベーターは ありません | erebētā wa arimasen | il n'y a pas d'ascenseur | there's no lift
いえに ねこが います | ie ni neko ga imasu | il y a un chat à la maison | there's a cat in the house
どこに すんで いますか | doko ni sunde imasu ka | où habitez-vous ? | where do you live?
げんかんで くつを ぬぎます | genkan de kutsu o nugimasu | on enlève ses chaussures dans l'entrée | you take your shoes off in the entryway""",
  "a": ("あります pour les choses, います pour ce qui vit (personnes, animaux). Le lieu prend に : へやに. Dans une maison japonaise, on laisse ses chaussures au げんかん, l'entrée, avant la marche.",
        "あります is for things, います for living beings (people, animals). The place takes に: へやに. In a Japanese home you leave your shoes in the げんかん, the entryway, below the step.")},
 "blocs": """…は ありますか。 | Il y a … ? | Is there …? | だいどころ / せんたくき / エレベーター | une cuisine / une machine à laver / un ascenseur | a kitchen / a washing machine / a lift
…に すんで います。 | J'habite …. | I live …. | とうきょう / やなか / アパート | à Tokyo / à Yanaka / dans un appartement | in Tokyo / in Yanaka / in a flat""",
 "dialogue": {"t": ("Chez la propriétaire", "At the landlady's"), "l": """eux | はじめまして。おおたです。 | Enchantée. Je suis Mme Ōta. | Nice to meet you. I'm Mrs Ōta.
moi | はじめまして。きょうから おせわに なります。 | Enchantée. Merci de m'accueillir à partir d'aujourd'hui. | Nice to meet you. Thank you for having me from today.
eux | これが へやの かぎです。ゴミは かようびと きんようびです。 | Voici la clé de la chambre. Les poubelles, c'est le mardi et le vendredi. | Here's your room key. Rubbish day is Tuesday and Friday.
moi | わかりました。よろしく おねがいします。 | D'accord. Merci beaucoup. | All right. Thank you very much."""}},

{"id": "demarches", "pour": "installe", "icone": "🏛️",
 "s": ("Les démarches : la mairie, l'entretien", "Paperwork: the ward office, the interview"),
 "scenes": ["kuyakusho", "mensetsu"],
 "mots": "名前, 国, 紙, 仕事, 会社, 質問, 書く, 答える, 教える, 失礼します, わかりました, 少々お待ちください",
 "tableau": {"t": ("Les questions du guichet", "Questions at the counter"),
  "l": """おなまえは なんですか | onamae wa nan desu ka | quel est votre nom ? | what's your name?
おくには どちらですか | okuni wa dochira desu ka | de quel pays êtes-vous ? | what country are you from?
じゅうしょを かいて ください | jūsho o kaite kudasai | écrivez votre adresse | please write your address
ここに サインして ください | koko ni sain shite kudasai | signez ici | please sign here
しょうしょう おまちください | shōshō omachi kudasai | un instant, s'il vous plaît | one moment, please
どうぞ おかけください | dōzo okake kudasai | asseyez-vous, je vous en prie | please take a seat""",
  "a": ("Au guichet, on vous parle très poliment : おなまえ, おくに (le お de respect), おまちください. On répond simplement, avec です et ます. Un employeur attend aussi ce japonais poli, même dans un petit café.",
        "At the counter, people speak to you very politely: おなまえ, おくに (the respectful お), おまちください. You answer simply, with です and ます. An employer expects this polite Japanese too, even in a small café.")},
 "blocs": """じゅうしょは …です。 | Mon adresse, c'est …. | My address is …. | やなか / たいとうく / とうきょう | Yanaka / l'arrondissement de Taitō / Tokyo | Yanaka / Taitō ward / Tokyo
…で はたらきたいです。 | Je voudrais travailler …. | I'd like to work …. | きっさてん / レストラン / ここ | dans un café / dans un restaurant / ici | in a café / in a restaurant / here""",
 "dialogue": {"t": ("Au guichet de la mairie", "At the ward office counter"), "l": """eux | つぎの かた、どうぞ。 | Personne suivante, je vous en prie. | Next, please.
moi | ざいりゅうカードの てつづきを おねがいします。 | Je viens pour la carte de résident. | I'm here about my residence card.
eux | この かみに なまえと じゅうしょを かいて ください。 | Écrivez votre nom et votre adresse sur cette feuille. | Please write your name and address on this form.
moi | すみません、じゅうしょは どこに かきますか。 | Pardon, où est-ce que j'écris l'adresse ? | Sorry, where do I write the address?
eux | ここです。しょうしょう おまちください。 | Ici. Un instant, s'il vous plaît. | Here. One moment, please."""}},
]

SUITE = [
 {"id": "famille", "icone": "👨‍👩‍👧", "s": ("La famille", "Family"), "scene": "oomisoka",
  "themes": ["famille_a1", "personnes_a1"],
  "tableau": {"t": ("Ma famille, ta famille", "My family, your family"),
   "l": """ちちは りょうりにんです | chichi wa ryōrinin desu | mon père est cuisinier | my father is a cook
おとうさんは おげんきですか | otōsan wa ogenki desu ka | votre père va bien ? | how is your father?
そぼは かなざわに すんで います | sobo wa kanazawa ni sunde imasu | ma grand-mère habite à Kanazawa | my grandmother lives in Kanazawa
きょうだいは いますか | kyōdai wa imasu ka | vous avez des frères et sœurs ? | do you have brothers or sisters?
ひとりっこです | hitorikko desu | je suis enfant unique | I'm an only child
かぞくは よにんです | kazoku wa yonin desu | nous sommes quatre dans la famille | there are four of us in my family""",
   "a": ("Deux mots par parent : un pour SA famille (ちち, はは, そぼ), un pour celle des autres (おとうさん, おかあさん, おばあさん). On parle humblement des siens.",
         "Two words for each relative: one for YOUR family (ちち, はは, そぼ), one for other people's (おとうさん, おかあさん, おばあさん). You speak humbly about your own.")}},
 {"id": "maison", "icone": "🏡", "s": ("La maison", "The home"), "scene": "kotatsu",
  "themes": ["maison_a1", "vie_quotidienne_a1"],
  "tableau": {"t": ("Où sont les choses : うえ, した, なか", "Where things are: うえ, した, なか"),
   "l": """つくえの うえに ほんが あります | tsukue no ue ni hon ga arimasu | il y a un livre sur le bureau | there's a book on the desk
ねこは こたつの なかに います | neko wa kotatsu no naka ni imasu | le chat est sous la table chauffante | the cat is inside the kotatsu
かぎは かばんの なかです | kagi wa kaban no naka desu | la clé est dans le sac | the key is in the bag
いすの したに くつが あります | isu no shita ni kutsu ga arimasu | il y a des chaussures sous la chaise | there are shoes under the chair
まどの そばに テレビが あります | mado no soba ni terebi ga arimasu | la télé est près de la fenêtre | the TV is by the window
へやを そうじします | heya o sōji shimasu | je fais le ménage de la chambre | I clean the room""",
   "a": ("Chose + の + うえ (sur), した (sous), なか (dans), そば (près de) + に : つくえの うえに. Puis あります ou います.",
         "Thing + の + うえ (on), した (under), なか (in), そば (near) + に: つくえの うえに. Then あります or います.")}},
 {"id": "cuisine", "icone": "🍳", "s": ("Manger et cuisiner", "Eating and cooking"), "scene": "daidokoro",
  "themes": ["nourriture_a1", "cuisine_a1"],
  "tableau": {"t": ("Faire, puis faire : la forme en て", "One thing then another: the て-form"),
   "l": """やさいを きって ください | yasai o kitte kudasai | coupez les légumes, s'il vous plaît | please cut the vegetables
おゆを わかして います | oyu o wakashite imasu | je fais bouillir de l'eau | I'm boiling some water
たまごを いれて まぜます | tamago o irete mazemasu | j'ajoute l'œuf et je mélange | I add the egg and mix
あじを みて ください | aji o mite kudasai | goûtez, s'il vous plaît | please taste it
ちょっと しおからいです | chotto shiokarai desu | c'est un peu salé | it's a bit salty
いただきます | itadakimasu | bon appétit (avant de manger) | let's eat (before eating)""",
   "a": ("La forme en て relie deux actions (いれて まぜます : j'ajoute et je mélange) et sert à demander (きって ください). いただきます avant le repas, ごちそうさまでした après.",
         "The て-form links two actions (いれて まぜます: I add and mix) and makes requests (きって ください). いただきます before a meal, ごちそうさまでした after.")}},
 {"id": "travail", "icone": "💼", "s": ("Le travail", "Work"), "scene": "kissaten",
  "themes": ["travail_a1", "mots_utiles_a1"],
  "tableau": {"t": ("Le japonais du travail", "Japanese at work"),
   "l": """いらっしゃいませ | irasshaimase | bienvenue (au client) | welcome (to a customer)
かしこまりました | kashikomarimashita | bien, c'est noté | certainly
しょうしょう おまちください | shōshō omachi kudasai | un instant, je vous prie | one moment, please
おさきに しつれいします | osaki ni shitsurei shimasu | je m'en vais avant vous | I'll be leaving before you
おつかれさまです | otsukaresama desu | bon travail, merci | thanks for your hard work
なんじから はたらきますか | nanji kara hatarakimasu ka | vous commencez à quelle heure ? | what time do you start work?""",
   "a": ("Au travail, des formules toutes faites : かしこまりました (bien compris, envers un client), おつかれさまです (pour saluer un collègue), おさきに しつれいします (en partant avant les autres).",
         "At work, set phrases: かしこまりました (certainly, to a customer), おつかれさまです (to greet a colleague), おさきに しつれいします (when leaving before the others).")}},
 {"id": "ecole", "icone": "📚", "s": ("L'école et les études", "School and studying"), "scene": "kyoushitsu",
  "themes": ["ecole_a1", "communication_a1"],
  "tableau": {"t": ("Comprendre, demander : わかります", "Understanding, asking: わかります"),
   "l": """わかりました | wakarimashita | j'ai compris | I understand
わかりません | wakarimasen | je ne comprends pas | I don't understand
これは なんと よみますか | kore wa nan to yomimasu ka | comment se lit ceci ? | how do you read this?
もう いちど いって ください | mō ichido itte kudasai | redites-le, s'il vous plaît | please say it again
しゅくだいを わすれました | shukudai o wasuremashita | j'ai oublié mes devoirs | I forgot my homework
まいにち かんじを れんしゅうします | mainichi kanji o renshū shimasu | je m'exerce aux kanji tous les jours | I practise kanji every day""",
   "a": ("わかります se construit avec が : にほんごが わかります. Pour un kanji inconnu : なんと よみますか (comment se lit-il ?). L'élève appelle le professeur せんせい, jamais par son prénom.",
         "わかります takes が: にほんごが わかります. For an unknown kanji: なんと よみますか (how is it read?). Students call the teacher せんせい, never by first name.")}},
 {"id": "loisirs", "icone": "🎆", "s": ("Les loisirs", "Free time"), "scene": "hanabi",
  "themes": ["loisirs_a1", "culture_a1", "animaux_a1", "medias_a1"],
  "tableau": {"t": ("Aimer : ～が すきです", "Liking: ～が すきです"),
   "l": """えいがが すきです | eiga ga suki desu | j'aime le cinéma | I like films
おんがくを ききます | ongaku o kikimasu | j'écoute de la musique | I listen to music
ギターを ひきます | gitā o hikimasu | je joue de la guitare | I play the guitar
いぬが だいすきです | inu ga daisuki desu | j'adore les chiens | I love dogs
しゅうまつは さんぽします | shūmatsu wa sanpo shimasu | le week-end, je me promène | at weekends I go for walks
スポーツは あまり すきじゃ ありません | supōtsu wa amari suki ja arimasen | je n'aime pas trop le sport | I don't really like sport""",
   "a": ("すき (aimer) est un adjectif, et ce qu'on aime prend が : えいがが すきです. Négation : すきじゃ ありません ; あまり adoucit (pas trop).",
         "すき (liking) is an adjective, and the thing you like takes が: えいがが すきです. Negative: すきじゃ ありません; あまり softens it (not really).")}},
 {"id": "corps", "icone": "🩺", "s": ("Le corps et les vêtements", "The body and clothes"), "scene": "sentou",
  "themes": ["corps_a1", "sante_a1", "vetements_a1"],
  "tableau": {"t": ("Porter : きます, はきます, かぶります", "Wearing: きます, はきます, かぶります"),
   "l": """シャツを きます | shatsu o kimasu | je mets une chemise | I put on a shirt
ズボンを はきます | zubon o hakimasu | je mets un pantalon | I put on some trousers
くつを はきます | kutsu o hakimasu | je mets mes chaussures | I put on my shoes
ぼうしを かぶります | bōshi o kaburimasu | je mets un chapeau | I put on a hat
めがねを かけます | megane o kakemasu | je mets mes lunettes | I put on my glasses
くつを ぬぎます | kutsu o nugimasu | j'enlève mes chaussures | I take off my shoes""",
   "a": ("Le japonais a un verbe par partie du corps : きます pour le haut, はきます pour les jambes et les pieds, かぶります pour la tête, かけます pour les lunettes. Pour tout enlever : ぬぎます.",
         "Japanese has a verb for each part of the body: きます for the top, はきます for legs and feet, かぶります for the head, かけます for glasses. To take anything off: ぬぎます.")}},
 {"id": "societe", "icone": "🗓️", "s": ("Le temps, la ville, le quotidien", "Weather, the city, everyday life"), "scene": "hatsumoude",
  "themes": ["ville_a1", "temps_a1", "meteo_a1", "achats_a1", "transports_a1", "nombres_a1", "couleurs_formes_a1",
             "nature_a1", "directions_a1", "objets_a1", "voyage_a1"],
  "tableau": {"t": ("Le temps qu'il fait, le temps qui passe", "The weather, the time"),
   "l": """きょうは いい てんきですね | kyō wa ii tenki desu ne | il fait beau aujourd'hui | it's lovely weather today
あしたは あめが ふります | ashita wa ame ga furimasu | demain, il va pleuvoir | it'll rain tomorrow
いま なんじですか | ima nanji desu ka | quelle heure est-il ? | what time is it?
ごご さんじはんです | gogo sanji han desu | il est trois heures et demie de l'après-midi | it's half past three in the afternoon
まいあさ ろくじに おきます | maiasa rokuji ni okimasu | je me lève à six heures tous les matins | I get up at six every morning
らいしゅう かなざわへ いきます | raishū kanazawa e ikimasu | j'irai à Kanazawa la semaine prochaine | I'm going to Kanazawa next week""",
   "a": ("Le présent en ～ます sert aussi au futur : あした いきます (j'irai demain). L'heure précise prend に (ろくじに), mais pas あした, まいあさ ou らいしゅう. へ (lu « e ») marque la direction.",
         "The ～ます present also covers the future: あした いきます (I'll go tomorrow). An exact time takes に (ろくじに), but not あした, まいあさ or らいしゅう. へ (read “e”) marks direction.")}},
]


def fe(paire):
    return {"fr": paire[0], "en": paire[1]}


def lignes(texte):
    return [[c.strip() for c in l.split("|")] for l in texte.strip().split("\n") if l.strip()]


def lire(f):
    return json.load(io.open(os.path.join(ICI, f), encoding="utf-8"))


def corpus_a1():
    mots = set()
    themes = set()
    for t in lire("themes.json")["themes"]:
        if t.get("niveau") == "A1":
            themes.add(t["id"])
            mots.update(m["mot"] for m in t["mots"])
    for f in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        mots.update(e["mot"] for e in lire(f).get("A1", []))
    return mots, themes


def construire():
    erreurs = []
    corpus, themes = corpus_a1()
    scenes = {f[len("scene-"):-len(".ja.js")] for f in os.listdir(os.path.join(RACINE, "visuel", "prototype"))
              if f.startswith("scene-") and f.endswith(".ja.js")}
    vus = {}

    def mots(lieu):
        sortie = []
        for m in [x.strip() for x in lieu["mots"].split(",") if x.strip()]:
            if m not in corpus:
                erreurs.append("%s : « %s » n'est pas dans l'A1 japonais" % (lieu["id"], m))
            elif m in vus:
                erreurs.append("%s : « %s » deja pris par %s" % (lieu["id"], m, vus[m]))
            else:
                vus[m] = lieu["id"]
                sortie.append(m)
        return sortie

    def tableau(t, lieu):
        l = []
        for c in lignes(t["l"]):
            if len(c) != 4:
                erreurs.append("%s : ligne de tableau mal formee %r" % (lieu, c))
                continue
            ja, rom, fr, en = c
            pr = ja.replace(" ", "") + " · " + rom
            l.append([ja, {"fr": fr, "en": en}, {"fr": pr, "en": pr}])
        return {"t": fe(t["t"]), "l": l, "a": fe(t["a"])}

    def blocs(texte, lieu):
        out = []
        for c in lignes(texte):
            if len(c) != 6:
                erreurs.append("%s : phrase mal formee %r" % (lieu, c))
                continue
            p, sfr, sen, vja, vfr, ven = c
            vja, vfr, ven = ([x.strip() for x in v.split("/")] for v in (vja, vfr, ven))
            if not (len(vja) == len(vfr) == len(ven) == 3) or p.count("…") != 1:
                erreurs.append("%s : « %s » veut un seul … et 3 variantes partout" % (lieu, p))
                continue
            out.append({"p": p, "s": {"fr": sfr, "en": sen}, "v": vja,
                        "ex": p.replace("…", vja[-1]),
                        "exs": {"fr": sfr.replace("…", vfr[-1]), "en": sen.replace("…", ven[-1])},
                        "vs": [{"fr": sfr.replace("…", a), "en": sen.replace("…", b)} for a, b in zip(vfr, ven)]})
        return out

    def dialogue(d, lieu):
        l = []
        for c in lignes(d["l"]):
            if len(c) != 4 or c[0] not in ("eux", "moi"):
                erreurs.append("%s : replique mal formee %r" % (lieu, c))
                continue
            if c[0] == "moi" and len(c[1].split(" ")) > 10:
                erreurs.append("%s : replique « moi » trop longue (10 groupes au plus) : %s" % (lieu, c[1]))
            l.append({"q": c[0], "p": c[1], "s": {"fr": c[2], "en": c[3]}})
        return {"t": fe(d["t"]), "l": l}

    def scenes_de(liste, lieu):
        for s in liste:
            if s not in scenes:
                erreurs.append("%s : pas de scene-%s.ja.js" % (lieu, s))
        return [s for s in liste if s in scenes]

    def lieu(e):
        return {"id": e["id"], "pour": e["pour"], "icone": e["icone"], "s": fe(e["s"]),
                "scenes": scenes_de(e["scenes"], e["id"]), "mots": mots(e),
                "tableau": tableau(e["tableau"], e["id"]), "blocs": blocs(e["blocs"], e["id"]),
                "dialogue": dialogue(e["dialogue"], e["id"])}

    suite = []
    for e in SUITE:
        for t in e["themes"]:
            if t not in themes:
                erreurs.append("%s : pas de theme A1 « %s »" % (e["id"], t))
        suite.append({"id": e["id"], "icone": e["icone"], "s": fe(e["s"]),
                      "scene": (scenes_de([e["scene"]], e["id"]) or [None])[0],
                      "themes": e["themes"], "tableau": tableau(e["tableau"], e["id"])})
    d = {"_lisez_moi": ["Derive de japonais/datos/a1_voyage_construire.py (branche japonais) : ne pas modifier a la main.",
                        "L'A1 voyage du japonais, l'annee de Camille a Tokyo : 12 escales, 2 etapes « installe », "
                        "la suite en 8 etapes. Phrases en kana avec des espaces. Brouillon, a faire relire par un natif."],
         "escales": [lieu(e) for e in ESCALES],
         "installe": [lieu(e) for e in INSTALLE],
         "suite": suite}
    if len(d["escales"]) != 12 or [e["pour"] for e in d["escales"]].count("voyage") != 2:
        erreurs.append("12 escales, dont 2 « voyage », attendues")
    if erreurs:
        sys.exit("\n".join(erreurs))
    with io.open(os.path.join(ICI, "a1-voyage.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    nb_blocs = sum(len(e["blocs"]) for e in d["escales"] + d["installe"])
    nb_rep = sum(len(e["dialogue"]["l"]) for e in d["escales"] + d["installe"])
    print("a1-voyage.json : %d escales, %d installe, %d etapes de suite ; %d mots, %d phrases toutes faites, "
          "%d repliques, %d lignes de tableau"
          % (len(d["escales"]), len(d["installe"]), len(d["suite"]), len(vus), nb_blocs, nb_rep,
             sum(len(e["tableau"]["l"]) for e in d["escales"] + d["installe"] + d["suite"])))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    construire()
