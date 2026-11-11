# -*- coding: utf-8 -*-
"""Les tuiles de grammaire et « S'entrainer par temps » du japonais (lot J4, 11 nov. 2026).

    python japonais/datos/exercices_construire.py
    python japonais/datos/conjugaison_construire.py
    python japonais/datos/grammaire_construire.py
    python japonais/datos/tuiles_construire.py        # EN DERNIER : il complete les deux fichiers

LE MEME MECANISME QUE L'ANGLAIS (anglais/outils/tuiles_niveaux.py,
temps_<niv>.py) : dans grammaire.json, une cle « tuiles » (panneau de chaque
tuile : fiches, series, vocabulaire) et une cle « temps » (une carte par forme
verbale, avec sa serie). Le moteur les lit avec panneauTuileAnglaise() et
ouvrirTempsAnglais(), elargis au japonais.

Les tuiles du japonais :
  - praep          « Particules » (la tuile des prepositions : le japonais
                   met ses particules APRES le mot, ce sont ses prepositions) ;
  - pronomen       pronoms et こそあど ;
  - zahlen         « Nombres et compteurs » ;
  - konjunktionen  connecteurs ;
  - wortstellung   l'ordre des mots (le verbe a la fin).

Ce script ajoute aussi a exercices.json les series qui manquaient : compteurs,
connecteurs, ordre des mots (en morceaux, depuis morceaux.json), et cinq
formes verbales calculees (～ている, ～たい, potentiel, volitif, ば). Et deux
fiches a grammaire.json : les compteurs, l'ordre des mots.

Ecrit a la main pour les series et les fiches ; les formes viennent du moteur
de conjugaison (verbes.json). Brouillon, a faire relire par un natif.
"""
import io
import json
import os
import random

ICI = os.path.dirname(os.path.abspath(__file__))


def lire(nom):
    with io.open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def ecrire(nom, d):
    with io.open(os.path.join(ICI, nom), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")


def fe(fr, en):
    return {"fr": fr, "en": en}


def item(topic, question, fr, en, options, correct, hint, expl_fr, expl_en):
    assert correct in options and len(set(options)) == len(options), (question, options)
    return {"topic": topic, "question": question, "question_en": question,
            "translation": fr, "translation_en": en, "hint": hint[0], "hint_en": hint[1],
            "answers": [correct], "correct": correct, "correctEn": correct,
            "explanation": expl_fr, "explanation_en": expl_en, "options": options, "optionsEn": options}


def melange(opts, graine):
    return sorted(opts, key=lambda s: (sum(map(ord, s + graine)) % 7, s))


# --- Les compteurs ------------------------------------------------------------
H_CPT = ("(～つ choses · ～人 personnes · ～枚 plat · ～本 long · ～冊 livres · ～台 machines · ～匹 petits animaux · ～杯 verres · ～回 fois · ～階 étages)",
         "(～つ things · ～人 people · ～枚 flat · ～本 long · ～冊 books · ～台 machines · ～匹 small animals · ～杯 cups · ～回 times · ～階 floors)")
COMPTEURS = [
    ("りんごを___ください。", "Trois pommes, s'il vous plaît.", "Three apples, please.", "三つ", ["三つ", "三人", "三枚"],
     "Des choses sans compteur propre : ～つ.", "Things with no counter of their own: ～つ."),
    ("家族は___です。", "Nous sommes quatre dans la famille.", "There are four of us in my family.", "四人", ["四人", "四つ", "四匹"],
     "Des personnes : ～人 (よにん).", "People: ～人 (yonin)."),
    ("猫が___います。", "Il y a deux chats.", "There are two cats.", "二匹", ["二匹", "二人", "二本"],
     "Un petit animal : ～匹.", "A small animal: ～匹."),
    ("ビールを___ください。", "Une bouteille de bière, s'il vous plaît.", "One bottle of beer, please.", "一本", ["一本", "一枚", "一冊"],
     "Une bouteille est longue : ～本.", "A bottle is long: ～本."),
    ("切手を___ください。", "Deux timbres, s'il vous plaît.", "Two stamps, please.", "二枚", ["二枚", "二本", "二台"],
     "Un timbre est plat : ～枚.", "A stamp is flat: ～枚."),
    ("本を___買いました。", "J'ai acheté trois livres.", "I bought three books.", "三冊", ["三冊", "三枚", "三本"],
     "Les livres et les cahiers : ～冊.", "Books and notebooks: ～冊."),
    ("車が___あります。", "Il y a deux voitures.", "There are two cars.", "二台", ["二台", "二人", "二つ"],
     "Les machines et les véhicules : ～台.", "Machines and vehicles: ～台."),
    ("コーヒーを___飲みました。", "J'ai bu une tasse de café.", "I drank a cup of coffee.", "一杯", ["一杯", "一本", "一枚"],
     "Une tasse, un verre, un bol : ～杯.", "A cup, a glass, a bowl: ～杯."),
    ("日本に___行きました。", "Je suis allé deux fois au Japon.", "I've been to Japan twice.", "二回", ["二回", "二台", "二人"],
     "Le nombre de fois : ～回.", "How many times: ～回."),
    ("トイレは___です。", "Les toilettes sont au premier étage.", "The toilet is on the second floor.", "二階", ["二階", "二回", "二台"],
     "L'étage : ～階 (au Japon, le rez-de-chaussée est 一階).", "The floor: ～階 (in Japan the ground floor is 一階)."),
    ("___で旅行します。", "Je voyage seul.", "I travel alone.", "一人", ["一人", "一つ", "一回"],
     "« Seul » : 一人で (ひとりで).", "“Alone”: 一人で (hitori de)."),
    ("シャツを___買いました。", "J'ai acheté deux chemises.", "I bought two shirts.", "二枚", ["二枚", "二本", "二冊"],
     "Un vêtement plat : ～枚.", "A flat piece of clothing: ～枚."),
    ("鉛筆が___あります。", "Il y a cinq crayons.", "There are five pencils.", "五本", ["五本", "五枚", "五匹"],
     "Un crayon est long : ～本.", "A pencil is long: ～本."),
    ("三本 se lit ___", "Trois (bouteilles) : la lecture", "Three (bottles): the reading", "さんぼん", ["さんぼん", "さんほん", "さんぽん"],
     "Après 三, ほん devient ぼん.", "After 三, hon becomes bon."),
    ("一本 se lit ___", "Une (bouteille) : la lecture", "One (bottle): the reading", "いっぽん", ["いっぽん", "いちほん", "いっほん"],
     "一 + ほん = いっぽん (le son se double).", "一 + hon = ippon (the sound doubles)."),
    ("六本 se lit ___", "Six (bouteilles) : la lecture", "Six (bottles): the reading", "ろっぽん", ["ろっぽん", "ろくほん", "ろくぼん"],
     "六 + ほん = ろっぽん.", "六 + hon = roppon."),
    ("一匹 se lit ___", "Un (petit animal) : la lecture", "One (small animal): the reading", "いっぴき", ["いっぴき", "いちひき", "いちびき"],
     "一 + ひき = いっぴき.", "一 + hiki = ippiki."),
    ("三匹 se lit ___", "Trois (petits animaux) : la lecture", "Three (small animals): the reading", "さんびき", ["さんびき", "さんひき", "さんぴき"],
     "三 + ひき = さんびき.", "三 + hiki = sanbiki."),
    ("二人 se lit ___", "Deux personnes : la lecture", "Two people: the reading", "ふたり", ["ふたり", "ににん", "ふたにん"],
     "一人 ひとり et 二人 ふたり sont à part ; ensuite さんにん, よにん…", "一人 hitori and 二人 futari are special; then sannin, yonin…"),
    ("一杯 se lit ___", "Une tasse : la lecture", "One cup: the reading", "いっぱい", ["いっぱい", "いちはい", "いっはい"],
     "一 + はい = いっぱい.", "一 + hai = ippai."),
]

# --- Les connecteurs ----------------------------------------------------------
H_CON = ("(だから / から donc, parce que · でも / けど mais · それから et puis · それに / し en plus · のに alors que · ので comme · それとも ou bien · ながら tout en)",
         "(だから / から so, because · でも / けど but · それから and then · それに / し besides · のに even though · ので since · それとも or · ながら while)")
CONNECTEURS = [
    ("雨が降っています。___、傘を持って行きます。", "Il pleut. Donc je prends un parapluie.", "It's raining, so I'll take an umbrella.", "だから", ["だから", "でも", "それとも"],
     "La conséquence : だから.", "The consequence: だから."),
    ("日本語は難しいです。___、面白いです。", "Le japonais est difficile. Mais c'est intéressant.", "Japanese is hard, but it's interesting.", "でも", ["でも", "だから", "それから"],
     "L'opposition, en début de phrase : でも.", "Contrast, at the start of a sentence: でも."),
    ("朝ご飯を食べました。___、学校へ行きました。", "J'ai pris mon petit-déjeuner. Puis je suis allé à l'école.", "I had breakfast. Then I went to school.", "それから", ["それから", "でも", "だから"],
     "La suite des actions : それから.", "What happens next: それから."),
    ("疲れた___、早く寝ます。", "Comme je suis fatigué, je me couche tôt.", "I'm tired, so I'll go to bed early.", "から", ["から", "けど", "のに"],
     "La raison avant, puis から.", "The reason first, then から."),
    ("高い___、買いました。", "C'était cher, mais je l'ai acheté.", "It was expensive, but I bought it.", "けど", ["けど", "から", "ので"],
     "« Mais », à l'oral : けど.", "“But”, in speech: けど."),
    ("コーヒーにしますか、___紅茶にしますか。", "Vous prenez un café, ou bien un thé ?", "Will you have coffee, or tea?", "それとも", ["それとも", "そして", "だから"],
     "« Ou bien », entre deux questions : それとも.", "“Or”, between two questions: それとも."),
    ("この店は安い___、おいしいです。", "Ce restaurant est bon marché, et en plus il est bon.", "This place is cheap, and the food is good too.", "し", ["し", "のに", "から"],
     "Une raison de plus : し.", "One more reason: し."),
    ("たくさん勉強した___、試験に落ちました。", "J'ai beaucoup étudié, et pourtant j'ai raté l'examen.", "I studied a lot, yet I failed the exam.", "のに", ["のに", "ので", "から"],
     "« Alors que », avec un regret : のに.", "“Even though”, with regret: のに."),
    ("雨が降った___、試合は中止になりました。", "Comme il a plu, le match a été annulé.", "Since it rained, the match was cancelled.", "ので", ["ので", "のに", "けど"],
     "« Comme », plus doux et plus poli que から : ので.", "“Since”, softer and more polite than から: ので."),
    ("音楽を聞き___、勉強します。", "J'étudie en écoutant de la musique.", "I study while listening to music.", "ながら", ["ながら", "たり", "ので"],
     "Deux actions en même temps : radical en ます + ながら.", "Two actions at once: masu-stem + ながら."),
    ("この部屋は広いです。___、明るいです。", "Cette pièce est grande. En plus, elle est claire.", "This room is big. Besides, it's bright.", "それに", ["それに", "でも", "それとも"],
     "« En plus » : それに.", "“Besides”: それに."),
    ("暑いです___、窓を開けてください。", "Il fait chaud, alors ouvrez la fenêtre, s'il vous plaît.", "It's hot, so please open the window.", "から", ["から", "のに", "けど"],
     "La raison d'une demande : から.", "The reason for a request: から."),
    ("天気がいいです。___、散歩しましょう。", "Il fait beau. Alors, allons nous promener.", "The weather's nice. So let's go for a walk.", "じゃあ", ["じゃあ", "でも", "それとも"],
     "« Alors », pour proposer : じゃあ (では, plus soutenu).", "“Well then”, to suggest: じゃあ (では, more formal)."),
    ("駅に着きました。___、電話します。", "Je suis arrivé à la gare. Je t'appelle donc.", "I've arrived at the station, so I'll call you.", "だから", ["だから", "それとも", "でも"],
     "La conséquence : だから.", "The consequence: だから."),
]


def ordre_items(morceaux, traductions):
    """Remettre les morceaux (bunsetsu) dans l'ordre : le verbe a la fin."""
    out = []
    for phrase, d in morceaux.items():
        b = d.get("b") or []
        tr = traductions.get(phrase)
        # 3 ou 4 morceaux : au-dela, plusieurs ordres sont justes (le moment avant
        # ou apres le theme) et l'exercice, qui attend UN ordre, compterait faux.
        if not tr or not (3 <= len(b) <= 4) or len(phrase) > 22:
            continue
        niv, fr, en = tr
        if niv not in ("A1", "A2"):
            continue
        out.append({"topic": "ordre des mots", "question": fr, "question_en": en,
                    "translation": "", "translation_en": "",
                    "hint": "Remets les morceaux dans l'ordre : le verbe (ou です) vient à la fin.",
                    "hint_en": "Put the pieces in order: the verb (or です) comes last.",
                    "chunks": b, "leurres": [], "correct": phrase, "correctEn": phrase,
                    "explanation": phrase, "explanation_en": phrase, "niveauPhrase": niv})
    random.Random(11).shuffle(out)
    out.sort(key=lambda x: x["niveauPhrase"])
    return out[:60]


def traductions_corpus():
    t = {}
    d = lire("themes.json")
    for th in d["themes"]:
        for m in th.get("mots", []):
            if m.get("exemple") and m.get("exemple_fr"):
                t.setdefault(m["exemple"], (th.get("niveau"), m["exemple_fr"], m.get("exemple_en") or m["exemple_fr"]))
    for nom in ("verbes.json", "adjectifs.json", "adverbes.json"):
        d = lire(nom)
        for niv, l in d.items():
            if isinstance(l, list):
                for m in l:
                    if m.get("exemple") and m.get("exemple_fr"):
                        t.setdefault(m["exemple"], (niv, m["exemple_fr"], m.get("exemple_en") or m["exemple_fr"]))
    return t


# --- Cinq formes verbales calculees ---------------------------------------
H_FORMES = {
    "te_iru": ("(forme en て + いる : 食べている, 待っている, している)", "(te-form + いる: 食べている, 待っている, している)"),
    "tai": ("(radical en ます + たい : 食べます → 食べたい, 行きます → 行きたい)", "(masu-stem + たい: 食べます → 食べたい, 行きます → 行きたい)"),
    "potentiel": ("(groupe 1 : u → e + る, 書ける · groupe 2 : る → られる · する → できる · 来る → こられる)", "(group 1: u → e + る, 書ける · group 2: る → られる · する → できる · 来る → こられる)"),
    "volitif": ("(groupe 1 : u → o + う, 行こう · groupe 2 : る → よう · する → しよう · 来る → こよう)", "(group 1: u → o + う, 行こう · group 2: る → よう · する → しよう · 来る → こよう)"),
    "ba": ("(u → e + ば : 行けば, 食べれば · する → すれば · 来る → くれば)", "(u → e + ば: 行けば, 食べれば · する → すれば · 来る → くれば)"),
}
SENS = {"te_iru": ("en train de…", "…-ing"), "tai": ("vouloir…", "want to…"), "potentiel": ("pouvoir…", "can…"),
        "volitif": ("« faisons… »", "“let's…”"), "ba": ("si…", "if…")}


def series_formes(verbes):
    out = {k: [] for k in H_FORMES}
    for v in verbes:
        f, cl = v.get("formes") or {}, v.get("classe", "")
        if cl in ("vs-i", "vk") or not f.get("dictionnaire"):
            continue
        dico = f["dictionnaire"]["kanji"]
        rad = dico[:-1]
        masu = (f.get("masu") or {}).get("kanji", "")
        radm = masu[:-2] if masu.endswith("ます") else ""
        te = (f.get("te") or {}).get("kanji", "")
        cand = {
            "te_iru": (te + "いる" if te else "", [dico + "いる", (f.get("ta") or {}).get("kanji", "") + "いる"]),
            "tai": (radm + "たい" if radm else "", [dico + "たい", te + "たい" if te else ""]),
            "potentiel": ((f.get("potentiel") or {}).get("kanji", ""), [(f.get("passif") or {}).get("kanji", ""), dico + "られる" if cl != "v1" else rad + "れる"]),
            "volitif": ((f.get("volitif") or {}).get("kanji", ""), [rad + "よう" if cl != "v1" else rad + "ろう", (f.get("mashou") or {}).get("kanji", "")]),
            "ba": ((f.get("ba") or {}).get("kanji", ""), [dico + "ば", (f.get("tara") or {}).get("kanji", "")]),
        }
        # La forme ていて, calculee, n'est pas « te_iru » du moteur (いる simple) : on garde la sienne.
        if f.get("te_iru"):
            cand["te_iru"] = ((f["te_iru"] or {}).get("kanji", ""), cand["te_iru"][1])
        for k, (bon, faux) in cand.items():
            faux = [x for x in faux if x and x != bon]
            if not bon or len(set(faux)) < 2 or len(out[k]) >= 40:
                continue
            fr, en = SENS[k]
            out[k].append(item(k, dico + " → ___", "%s : %s" % (v["traduction"], fr), "%s: %s" % (v["traduction_en"], en),
                               melange([bon] + faux[:2], dico + k), bon, H_FORMES[k],
                               "%s → %s" % (dico, bon), "%s → %s" % (dico, bon)))
    return out


# --- Les fiches nouvelles -----------------------------------------------------
def ex(ja, romaji, fr, en):
    return [ja, fe(romaji + " — " + fr, romaji + " — " + en)]


FICHES = [
    {
        "id": "compteurs",
        "exercice": "exercicesCompteursJa",
        "titre": fe("Compter : nombres et compteurs", "Counting: numbers and counters"),
        "resume": fe("Un compteur pour chaque sorte de chose", "A counter for each kind of thing"),
        "regle": fe(
            "En japonais, on ne dit pas « trois pommes » mais « pommes, trois-<b>choses</b> » : le nombre prend un "
            "<b>compteur</b> qui dit quelle sorte de chose on compte. <b>りんごを三つください</b>. "
            "Le groupe nombre + compteur se place en général <b>juste avant le verbe</b>.",
            "Japanese doesn't say “three apples” but “apples, three-<b>things</b>”: the number takes a "
            "<b>counter</b> that tells what kind of thing is counted. <b>りんごを三つください</b>. "
            "The number + counter usually goes <b>right before the verb</b>."),
        "tableau": [
            ["～つ", fe("les choses en général (jusqu'à 10 : ひとつ… とお)", "things in general (up to 10: hitotsu… tō)"), "りんごを三つください。"],
            ["～人（にん）", fe("les personnes (mais 一人 ひとり, 二人 ふたり)", "people (but 一人 hitori, 二人 futari)"), "学生が五人います。"],
            ["～枚（まい）", fe("les choses plates : papier, billets, chemises", "flat things: paper, tickets, shirts"), "切手を二枚ください。"],
            ["～本（ほん）", fe("les choses longues : bouteilles, crayons (ぽん, ぼん)", "long things: bottles, pencils (pon, bon)"), "ビールを一本ください。"],
            ["～冊（さつ）", fe("les livres, les cahiers", "books, notebooks"), "本を三冊買いました。"],
            ["～匹（ひき）", fe("les petits animaux (ぴき, びき)", "small animals (piki, biki)"), "猫が二匹います。"],
            ["～台（だい）", fe("les machines, les véhicules", "machines, vehicles"), "車が一台あります。"],
            ["～回（かい） · ～階（かい）", fe("… fois · … étage", "… times · … floor"), "二回行きました。"],
        ],
        "exemples": [
            ex("りんごを三つください。", "ringo o mittsu kudasai", "Trois pommes, s'il vous plaît.", "Three apples, please."),
            ex("家族は四人です。", "kazoku wa yonin desu", "Nous sommes quatre dans la famille.", "There are four of us in my family."),
            ex("ビールを二本ください。", "bīru o nihon kudasai", "Deux bières, s'il vous plaît.", "Two beers, please."),
        ],
        "attention": fe(
            "Les sons changent avec certains nombres : 一本 いっぽん, 三本 さんぼん, 六本 ろっぽん ; "
            "一匹 いっぴき, 三匹 さんびき. Ne cherche pas la règle complète d'abord : ces formes reviennent si souvent qu'elles se retiennent.",
            "Sounds change with some numbers: 一本 ippon, 三本 sanbon, 六本 roppon; "
            "一匹 ippiki, 三匹 sanbiki. Don't look for the full rule first: these forms come up so often that they stick."),
    },
    {
        "id": "ordre-des-mots",
        "titre": fe("L'ordre des mots : le verbe à la fin", "Word order: the verb comes last"),
        "resume": fe("Sujet, compléments, verbe", "Subject, complements, verb"),
        "regle": fe(
            "La phrase japonaise finit <b>toujours</b> par le verbe (ou です) : <b>わたしは パンを 食べます</b> = moi, du pain, je mange. "
            "Avant lui, les morceaux peuvent bouger : ce sont les <b>particules</b> qui disent qui fait quoi, pas la place. "
            "L'habitude : <b>quand → qui → où → quoi → verbe</b>.",
            "A Japanese sentence <b>always</b> ends with the verb (or です): <b>わたしは パンを 食べます</b> = I, bread, eat. "
            "Before it, the pieces can move: the <b>particles</b> say who does what, not the position. "
            "The usual order: <b>when → who → where → what → verb</b>."),
        "tableau": [
            ["きのう / わたしは / 駅で / 友だちに / 会いました", fe("hier / moi / à la gare / un ami / j'ai rencontré", "yesterday / I / at the station / a friend / met")],
            ["わたしは / きのう / 駅で…", fe("le thème peut passer devant le moment : même sens", "the topic can go before the time: same meaning")],
            ["新しい / 本", fe("l'adjectif AVANT le nom", "the adjective BEFORE the noun")],
            ["駅の / 前", fe("« devant la gare » : ce qui précise vient avant", "“in front of the station”: what specifies comes first")],
        ],
        "exemples": [
            ex("わたしは 毎朝 コーヒーを 飲みます。", "watashi wa maiasa kōhī o nomimasu", "Je bois du café tous les matins.", "I drink coffee every morning."),
            ex("きのう 駅で 先生に 会いました。", "kinō eki de sensei ni aimashita", "Hier, j'ai rencontré le professeur à la gare.", "Yesterday I met the teacher at the station."),
        ],
        "attention": fe(
            "Ce qui précise vient toujours <b>avant</b> ce qu'il précise : 日本の車 (une voiture du Japon), "
            "赤い車 (une voiture rouge), 昨日買った車 (la voiture achetée hier).",
            "What specifies always comes <b>before</b> what it specifies: 日本の車 (a car from Japan), "
            "赤い車 (a red car), 昨日買った車 (the car bought yesterday)."),
        "exercice": "exercicesOrdreJa",
    },
]

TUILES = {
    "praep": {"sous_titre": "は · が · を · に · で · へ", "options": [
        {"type": "fiche", "cible": "wa-ga", "titre": fe("は et が : thème et sujet", "は and が: topic and subject"), "desc": fe("Deux particules pour qui et quoi", "Two particles for who and what")},
        {"type": "fiche", "cible": "particules", "titre": fe("を, に, へ, で : où va l'action", "を, に, へ, で: where the action goes"), "desc": fe("L'objet, le but, le lieu, le moyen", "Object, destination, place, means")},
        {"type": "fiche", "cible": "no-mo-to", "titre": fe("の, も, と, や", "の, も, と, や"), "desc": fe("De, aussi, et", "Of, also, and")},
        {"type": "serie", "cible": "particulesJaExercises", "titre": fe("Quelle particule ?", "Which particle?"), "desc": fe("24 phrases à compléter", "24 sentences to complete")},
        {"type": "vocab", "cible": "startPartikelnVokabular", "titre": fe("Vocabulaire · particules et petits mots", "Vocabulary · particles and little words"), "desc": fe("は, が, から, まで, です, ます…", "は, が, から, まで, です, ます…")},
    ]},
    "pronomen": {"sous_titre": "わたし · これ · この · ここ", "options": [
        {"type": "fiche", "cible": "kosoado", "titre": fe("これ, それ, あれ, どれ", "これ, それ, あれ, どれ"), "desc": fe("Ici, là, là-bas : la série こそあど", "Here, there, over there: the こそあど series")},
        {"type": "serie", "cible": "kosoadoJaExercises", "titre": fe("こ, そ, あ ou ど ?", "こ, そ, あ or ど?"), "desc": fe("Choisir le bon démonstratif", "Choose the right demonstrative")},
        {"type": "vocab", "cible": "startPronomenVokabular", "titre": fe("Vocabulaire · pronoms et démonstratifs", "Vocabulary · pronouns and demonstratives"), "desc": fe("わたし, あなた, かれ, この, どこ…", "わたし, あなた, かれ, この, どこ…")},
    ]},
    "zahlen": {"sous_titre": "一 · 二 · 三 · ～つ · ～人 · ～本", "options": [
        {"type": "fiche", "cible": "compteurs", "titre": fe("Comprendre les compteurs", "Understanding counters"), "desc": fe("つ, 人, 枚, 本, 冊, 匹, 台…", "つ, 人, 枚, 本, 冊, 匹, 台…")},
        {"type": "serie", "cible": "compteursJaExercises", "titre": fe("Quel compteur ?", "Which counter?"), "desc": fe("Le compteur et sa lecture (いっぽん, さんびき…)", "The counter and its reading (ippon, sanbiki…)")},
        {"type": "vocab", "cible": "startZahlenVokabular", "titre": fe("Vocabulaire · nombres et compteurs", "Vocabulary · numbers and counters"), "desc": fe("一, 十, 百, 千, 万, ～つ, ～人…", "一, 十, 百, 千, 万, ～つ, ～人…")},
    ]},
    "konjunktionen": {"sous_titre": "そして · でも · だから · から · けど", "options": [
        {"type": "fiche", "cible": "liaisons", "titre": fe("Relier deux phrases : から, が, けど", "Linking two sentences: から, が, けど"), "desc": fe("Parce que, mais", "Because, but")},
        {"type": "serie", "cible": "connecteursJaExercises", "titre": fe("Quel connecteur ?", "Which connector?"), "desc": fe("だから, でも, それから, のに, ので, ながら…", "だから, でも, それから, のに, ので, ながら…")},
        {"type": "vocab", "cible": "startKonjunktionenVokabular", "titre": fe("Vocabulaire · connecteurs", "Vocabulary · connectors"), "desc": fe("そして, しかし, それに, ところで…", "そして, しかし, それに, ところで…")},
    ]},
    "wortstellung": {"sous_titre": "qui · où · quoi · verbe", "options": [
        {"type": "fiche", "cible": "ordre-des-mots", "titre": fe("Comprendre l'ordre des mots", "Understanding word order"), "desc": fe("Le verbe à la fin", "The verb comes last")},
        {"type": "serie", "cible": "ordreJaExercises", "titre": fe("Remettre les morceaux dans l'ordre", "Put the pieces in order"), "desc": fe("Des phrases A1-A2, en morceaux", "A1-A2 sentences, in pieces")},
        {"type": "fiche", "cible": "questions", "titre": fe("Poser une question", "Asking questions"), "desc": fe("か, なに, だれ, どこ, いつ…", "か, なに, だれ, どこ, いつ…")},
        {"type": "serie", "cible": "questionsJaExercises", "titre": fe("Quel mot interrogatif ?", "Which question word?"), "desc": fe("10 questions et leurs réponses", "10 questions and their answers")},
    ]},
}

TEMPS = [
    ("temps-masu", "A1", fe("～ます — la forme polie", "～ます — the polite form"),
     fe("Présent et futur, négatif, passé : <b>食べます, 食べません, 食べました, 食べませんでした</b>. La forme qu'on parle avec un inconnu.",
        "Present and future, negative, past: <b>食べます, 食べません, 食べました, 食べませんでした</b>. The form you use with a stranger."), "masuJaExercises"),
    ("temps-te", "A1", fe("La forme en て", "The て-form"),
     fe("Relier deux actions, demander poliment (<b>～てください</b>). <b>書く → 書いて, 飲む → 飲んで, 食べる → 食べて</b>.",
        "Linking two actions, polite requests (<b>～てください</b>). <b>書く → 書いて, 飲む → 飲んで, 食べる → 食べて</b>."), "teJaExercises"),
    ("temps-te-iru", "A1", fe("～ている — en train de, un état", "～ている — ongoing action, state"),
     fe("Forme en て + いる : ce qui se passe maintenant (<b>食べている</b>) ou un état qui dure (<b>結婚している</b>).",
        "te-form + いる: what's happening now (<b>食べている</b>) or a lasting state (<b>結婚している</b>)."), "te_iruJaExercises"),
    ("temps-tai", "A1", fe("～たい — vouloir faire", "～たい — wanting to do"),
     fe("Le radical en ます + <b>たい</b> : <b>行きます → 行きたい</b>. Se conjugue comme un adjectif en い (行きたくない).",
        "The masu-stem + <b>たい</b>: <b>行きます → 行きたい</b>. Conjugates like an い-adjective (行きたくない)."), "taiJaExercises"),
    ("temps-adjectifs", "A1", fe("Les adjectifs : présent, négatif, passé", "Adjectives: present, negative, past"),
     fe("<b>高い → 高くない, 高かった</b> ; <b>静か → 静かじゃない, 静かだった</b>.", "<b>高い → 高くない, 高かった</b>; <b>静か → 静かじゃない, 静かだった</b>."), "adjectifsJaExercises"),
    ("temps-nai", "A2", fe("～ない — le négatif simple", "～ない — the plain negative"),
     fe("Groupe 1 : u → a + ない (<b>書かない</b>, う → わ : <b>買わない</b>) ; groupe 2 : <b>食べない</b> ; <b>しない, こない</b>.",
        "Group 1: u → a + ない (<b>書かない</b>, う → わ: <b>買わない</b>); group 2: <b>食べない</b>; <b>しない, こない</b>."), "naiJaExercises"),
    ("temps-ta", "A2", fe("～た — le passé simple", "～た — the plain past"),
     fe("La forme en て, avec a : <b>書いた, 飲んだ, 食べた, した, 来た</b>.", "The て-form with a: <b>書いた, 飲んだ, 食べた, した, 来た</b>."), "taJaExercises"),
    ("temps-potentiel", "A2", fe("Le potentiel — pouvoir", "The potential — can"),
     fe("<b>書ける, 話せる, 食べられる, できる</b>. Ce qu'on peut faire prend が : <b>日本語が話せます</b>.",
        "<b>書ける, 話せる, 食べられる, できる</b>. What you can do takes が: <b>日本語が話せます</b>."), "potentielJaExercises"),
    ("temps-volitif", "A2", fe("Le volitif — « faisons »", "The volitional — “let's”"),
     fe("La forme familière de ましょう : <b>行こう, 食べよう, しよう</b>. Avec と思う : <b>行こうと思う</b> (je pense y aller).",
        "The casual form of ましょう: <b>行こう, 食べよう, しよう</b>. With と思う: <b>行こうと思う</b> (I'm thinking of going)."), "volitifJaExercises"),
    ("temps-ba", "A2", fe("～ば — si…", "～ば — if…"),
     fe("u → e + ば : <b>行けば, 食べれば, すれば</b>. Adjectifs : <b>高ければ</b>.", "u → e + ば: <b>行けば, 食べれば, すれば</b>. Adjectives: <b>高ければ</b>."), "baJaExercises"),
    ("temps-formes", "A2", fe("Reconnaître une forme", "Recognising a form"),
     fe("Pouvoir, faisons, si, ne pas, passé : quelle forme est-ce ?", "Can, let's, if, not, past: which form is it?"), "formesJaExercises"),
]

KICKERS = {
    "praep": ("Particules", "Particles"),
    "zahlen": ("Nombres et compteurs", "Numbers and counters"),
}
NOMS_SERIES = {
    "particulesJaExercises": ("Les particules", "Particles"),
    "kosoadoJaExercises": ("これ, それ, あれ, どれ", "これ, それ, あれ, どれ"),
    "compteursJaExercises": ("Les compteurs", "Counters"),
    "connecteursJaExercises": ("Les connecteurs", "Connectors"),
    "ordreJaExercises": ("L'ordre des mots", "Word order"),
    "questionsJaExercises": ("Les questions", "Questions"),
    "masuJaExercises": ("Les verbes en ます", "Verbs in ます"),
    "teJaExercises": ("La forme en て", "The て-form"),
    "te_iruJaExercises": ("～ている", "～ている"),
    "taiJaExercises": ("～たい", "～たい"),
    "adjectifsJaExercises": ("Les adjectifs", "Adjectives"),
    "naiJaExercises": ("La forme en ない", "The ない-form"),
    "taJaExercises": ("La forme en た", "The た-form"),
    "potentielJaExercises": ("Le potentiel", "The potential"),
    "volitifJaExercises": ("Le volitif", "The volitional"),
    "baJaExercises": ("～ば", "～ば"),
    "formesJaExercises": ("Reconnaître une forme", "Recognising a form"),
}


def serie(liste, topic, h):
    return [item(topic, q, fr, en, opts, c, h, ef, ee) for q, fr, en, c, opts, ef, ee in liste]


def main():
    exos = lire("exercices.json")
    jeux = exos["jeux"]
    jeux["compteursJaExercises"] = serie(COMPTEURS, "compteurs", H_CPT)
    jeux["connecteursJaExercises"] = serie(CONNECTEURS, "connecteurs", H_CON)
    morceaux = lire("morceaux.json")["phrases"]
    jeux["ordreJaExercises"] = ordre_items(morceaux, traductions_corpus())
    verbes = [v for niv in ("A1", "A2") for v in lire("verbes.json").get(niv, [])]
    for k, l in series_formes(verbes).items():
        jeux[k + "JaExercises"] = l
    ecrire("exercices.json", exos)

    g = lire("grammaire.json")
    ids = {f["id"] for f in g["fiches"]}
    for f in FICHES:
        f = dict(f, statut="brouillon")
        if f["id"] in ids:
            g["fiches"] = [f if x["id"] == f["id"] else x for x in g["fiches"]]
        else:
            g["fiches"].append(f)
    g["tuiles"] = TUILES
    g["temps"] = [{"id": i, "niveau": n, "titre": t, "texte": x, "serie": s} for i, n, t, x, s in TEMPS]
    for code, idx in (("fr", 0), ("en", 1)):
        tx = g["textes"].setdefault(code, {})
        for tuile, noms in KICKERS.items():
            tx["orb_%s_title" % tuile] = noms[idx]
        for s, noms in NOMS_SERIES.items():
            tx["kicker_" + s] = noms[idx]
        tx["kicker_ordre_ja"] = NOMS_SERIES["ordreJaExercises"][idx]
    ecrire("grammaire.json", g)

    manque = [o["cible"] for t in TUILES.values() for o in t["options"] if o["type"] == "serie" and not jeux.get(o["cible"])]
    manque += [s for *_, s in TEMPS if not jeux.get(s)]
    manque += [o["cible"] for t in TUILES.values() for o in t["options"] if o["type"] == "fiche" and o["cible"] not in {f["id"] for f in g["fiches"]}]
    assert not manque, manque
    print("series :", ", ".join("%s %d" % (k, len(jeux[k])) for k in ("compteursJaExercises", "connecteursJaExercises", "ordreJaExercises",
                                                                     "te_iruJaExercises", "taiJaExercises", "potentielJaExercises", "volitifJaExercises", "baJaExercises")))
    print("tuiles :", ", ".join(TUILES), "| temps :", len(TEMPS), "| fiches :", len(g["fiches"]))


if __name__ == "__main__":
    main()
