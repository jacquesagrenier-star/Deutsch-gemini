# -*- coding: utf-8 -*-
"""Construit japonais/datos/prononciation.json : lire et dire le japonais.

    python japonais/datos/prononciation_construire.py

LE MEME FORMAT QUE espanol/datos/prononciation.json, lu par le meme moteur :
la tuile Prononciation (ouvrirPrononciation) et « le son du jour » de la
seance (preparerSonDuJour, insererSonDuJour). Une regle : graphie (les kana en
cause, separes par « · », soulignes dans les exemples), api, court,
explication, exemples (mot, traduction, traduction_en). Groupes : voyelles,
consonnes, fins (ici : la longueur des sons), accent (ici : la hauteur).

Les exemples sont ecrits en KANA : c'est la que le son se voit, et que le
moteur le souligne. La voix du telephone les lit ; l'oral du « son du jour »
accepte aussi la reponse en kanji (scoreOralJaponais).

Ecrit a la main pour des francophones et des anglophones : chaque son est
decrit avec un repere de leur langue. Brouillon, a faire relire par un natif.
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))


def fe(fr, en):
    return {"fr": fr, "en": en}


def m(mot, fr, en):
    return {"mot": mot, "traduction": fr, "traduction_en": en}


GROUPES = [
    {"id": "voyelles", "regles": [
        {"id": "voyelles", "graphie": "あ · い · う · え · お", "api": "[a i ɯ e o]",
         "court": fe("cinq voyelles, courtes et nettes", "five short, clean vowels"),
         "explication": fe(
             "a, i, u, e (« é »), o : toujours la même valeur, jamais nasales, jamais muettes. "
             "Le u se dit lèvres détendues, entre « ou » et « eu » : pas le « ou » arrondi du français.",
             "a, i, u, e (“eh”), o: always the same sound, never reduced to “uh”. "
             "u is said with relaxed, unrounded lips: not the rounded “oo” of “food”."),
         "exemples": [m("いえ", "maison", "house"), m("うえ", "dessus", "above"),
                      m("あおい", "bleu", "blue"), m("おおい", "nombreux", "many")]},
        {"id": "longues", "graphie": "ー · あ · い · う", "api": "[aː iː ɯː eː oː]",
         "court": fe("une voyelle longue change le mot", "a long vowel changes the word"),
         "explication": fe(
             "Une voyelle longue dure deux temps, et c'est un autre mot : おばさん (tante) et おばあさん (grand-mère). "
             "えい se dit « é » long (せんせい = sen-sée), おう se dit « o » long (とうきょう = too-kyoo). "
             "En katakana, la longueur s'écrit avec un trait : コーヒー.",
             "A long vowel lasts two beats, and it's a different word: おばさん (aunt) and おばあさん (grandmother). "
             "えい is a long “eh” (せんせい = sen-sei), おう a long “o” (とうきょう = too-kyoo). "
             "In katakana, length is written with a dash: コーヒー."),
         "exemples": [m("おばさん", "tante (voyelle courte)", "aunt (short vowel)"), m("おばあさん", "grand-mère", "grandmother"),
                      m("せんせい", "professeur", "teacher"), m("コーヒー", "café", "coffee"),
                      m("とうきょう", "Tokyo", "Tokyo")]},
        {"id": "devoisement", "graphie": "す · し · く", "api": "[s̥ ɕ̥ k̥]",
         "court": fe("i et u qui s'effacent", "i and u that fade out"),
         "explication": fe(
             "Entre deux consonnes sourdes, ou en fin de phrase, le i et le u se chuchotent presque : "
             "です = « dess », ～ます = « mass », すき = « ski », した = « shta ». Le mot garde son rythme.",
             "Between two voiceless consonants, or at the end of a sentence, i and u are almost whispered: "
             "です = “dess”, ～ます = “mass”, すき = “ski”, した = “shta”. The word keeps its rhythm."),
         "exemples": [m("です", "c'est", "it is"), m("すき", "aimer", "to like"),
                      m("すこし", "un peu", "a little"), m("つくえ", "bureau (meuble)", "desk")]},
    ]},
    {"id": "consonnes", "regles": [
        {"id": "r", "graphie": "ら · り · る · れ · ろ", "api": "[ɾ]",
         "court": fe("un r battu, presque un l", "a tapped r, close to l"),
         "explication": fe(
             "La langue touche une seule fois, très vite, derrière les dents du haut : entre r, l et d. "
             "Jamais le r de gorge du français. Pense au d rapide de « madame » dit vite.",
             "The tongue taps once, very quickly, behind the upper teeth: between r, l and d. "
             "Like the quick t in American “water” or “better”."),
         "exemples": [m("りんご", "pomme", "apple"), m("くるま", "voiture", "car"),
                      m("これ", "ceci", "this"), m("しろ", "blanc", "white")]},
        {"id": "shi-chi-tsu", "graphie": "し · ち · つ", "api": "[ɕi tɕi tsɯ]",
         "court": fe("shi, tchi, tsou", "shi, chi, tsu"),
         "explication": fe(
             "Dans la ligne de さ, le i donne し (« chi » de « chiffon », écrit shi) ; dans celle de た, "
             "ち (« tchi ») et つ (« tsou », comme dans « tsé-tsé »). Il n'y a pas de « si » ni de « ti » en japonais ancien.",
             "In the さ row, i gives し (“shee”, written shi); in the た row, ち (“chee”) and つ (“tsu”, like “cats”). "
             "Traditional Japanese has no “si” or “ti”."),
         "exemples": [m("すし", "sushi", "sushi"), m("ちず", "carte (plan)", "map"),
                      m("くつ", "chaussures", "shoes"), m("つくえ", "bureau (meuble)", "desk")]},
        {"id": "fu", "graphie": "ふ", "api": "[ɸɯ]",
         "court": fe("un souffle entre f et h", "a breath between f and h"),
         "explication": fe(
             "Les lèvres ne touchent pas les dents : on souffle doucement, comme pour refroidir une soupe. "
             "Ni le f de « fou », ni un h aspiré.",
             "The lips don't touch the teeth: blow gently, as if cooling soup. "
             "Neither the f of “food” nor a plain h."),
         "exemples": [m("ふゆ", "hiver", "winter"), m("ふたつ", "deux (choses)", "two (things)"),
                      m("ふく", "vêtement", "clothes")]},
        {"id": "ji-zu", "graphie": "じ · ず", "api": "[dʑi dzɯ]",
         "court": fe("dji, dzou", "ji, zu"),
         "explication": fe(
             "じ se dit « dji » (comme « jeans » à l'anglaise), ず « dzou » en début de mot, plus doux au milieu. "
             "ぢ et づ, rares, se disent pareil.",
             "じ is “jee” (as in “jeans”), ず is “dzu” at the start of a word, softer in the middle. "
             "The rare ぢ and づ sound the same."),
         "exemples": [m("じかん", "temps (durée)", "time"), m("みず", "eau", "water"),
                      m("ちず", "carte (plan)", "map")]},
        {"id": "yoon", "graphie": "ゃ · ゅ · ょ", "api": "[ʲa ʲɯ ʲo]",
         "court": fe("petit ゃ ゅ ょ : une seule syllabe", "small ゃ ゅ ょ: one single syllable"),
         "explication": fe(
             "Un petit ゃ, ゅ ou ょ se fond dans le kana d'avant : きゃ = « kya », une syllabe. "
             "En grand, ce sont deux syllabes, et un autre mot : びょういん (hôpital) et びよういん (salon de coiffure).",
             "A small ゃ, ゅ or ょ merges with the kana before it: きゃ = “kya”, one syllable. "
             "Written full-size, it's two syllables and another word: びょういん (hospital) and びよういん (hair salon)."),
         "exemples": [m("おちゃ", "thé", "tea"), m("しゃしん", "photo", "photo"),
                      m("りょこう", "voyage", "trip"), m("びょういん", "hôpital", "hospital")]},
        {"id": "particules", "graphie": "は · へ · を", "api": "[wa e o]",
         "court": fe("は, へ, を : wa, é, o quand ce sont des particules", "は, へ, を: wa, e, o as particles"),
         "explication": fe(
             "Trois kana gardent une vieille orthographe : la particule は se dit « wa », へ se dit « é », を se dit « o ». "
             "Dans un mot ordinaire, は reste « ha » : はな (fleur).",
             "Three kana keep an old spelling: the particle は is said “wa”, へ is “e”, を is “o”. "
             "Inside an ordinary word, は stays “ha”: はな (flower)."),
         "exemples": [m("こんにちは", "bonjour", "hello"), m("こんばんは", "bonsoir", "good evening"),
                      m("はな", "fleur", "flower")]},
    ]},
    {"id": "fins", "regles": [
        {"id": "tsu-petit", "graphie": "っ · ッ", "api": "[ː]",
         "court": fe("petit っ : un temps de silence", "small っ: a beat of silence"),
         "explication": fe(
             "Le petit っ ne se prononce pas : il bloque la consonne suivante un temps entier, comme « petit-t-tour ». "
             "きて (viens) et きって (timbre) sont deux mots ; おと (son) et おっと (mari) aussi.",
             "The small っ isn't pronounced: it holds the next consonant for a full beat, like “bookcase” said slowly. "
             "きて (come) and きって (stamp) are two words; so are おと (sound) and おっと (husband)."),
         "exemples": [m("きって", "timbre", "stamp"), m("がっこう", "école", "school"),
                      m("きっぷ", "billet", "ticket"), m("ちょっと", "un peu", "a little")]},
        {"id": "n", "graphie": "ん", "api": "[ɴ m ŋ]",
         "court": fe("ん : un temps à lui seul", "ん: a beat of its own"),
         "explication": fe(
             "ん compte pour une syllabe entière et ne nasalise pas la voyelle d'avant : ほん = « ho-n », pas « hon ». "
             "Devant b, p, m il devient m : しんぶん = « shimboun », さんぽ = « sampo ».",
             "ん counts as a whole beat: ほん = “ho-n”, two beats. "
             "Before b, p, m it becomes m: しんぶん = “shimbun”, さんぽ = “sampo”."),
         "exemples": [m("ほん", "livre", "book"), m("しんぶん", "journal", "newspaper"),
                      m("さんぽ", "promenade", "walk"), m("せんせい", "professeur", "teacher")]},
    ]},
    {"id": "accent", "regles": [
        {"id": "hauteur", "graphie": "", "api": "[ꜛ ꜜ]",
         "court": fe("pas d'accent fort : des notes hautes et basses", "no stress: high and low notes"),
         "explication": fe(
             "Le japonais n'appuie pas sur une syllabe : il monte ou descend d'une note. Chaque syllabe garde la même durée. "
             "La hauteur distingue parfois deux mots : あめ (pluie, haut-bas) et あめ (bonbon, bas-haut). "
             "Imite la voix plutôt qu'une règle : touche les mots et répète la mélodie.",
             "Japanese doesn't stress a syllable: it goes up or down a note. Every syllable keeps the same length. "
             "Pitch sometimes tells two words apart: 雨 (rain, high-low) and 飴 (candy, low-high). "
             "Copy the voice rather than a rule: tap the words and repeat the melody."),
         "exemples": [m("雨", "pluie (a-me : haut-bas)", "rain (a-me: high-low)"),
                      m("飴", "bonbon (a-me : bas-haut)", "candy (a-me: low-high)"),
                      m("箸", "baguettes (ha-shi : haut-bas)", "chopsticks (ha-shi: high-low)"),
                      m("橋", "pont (ha-shi : bas-haut)", "bridge (ha-shi: low-high)")]},
    ]},
]

# Les titres des groupes « fins » et « accent » : dans grammaire_construire.py
# (TEXTES), verses dans I18N avec les textes de grammaire.


def main():
    for g in GROUPES:
        for r in g["regles"]:
            for ex in r["exemples"]:
                morceaux = [x.strip() for x in r["graphie"].split("·") if x.strip()]
                # Un exemple « contraste » (おばさん face a おばあさん) n'a pas le son.
                contraste = "courte" in ex["traduction"]
                assert not morceaux or contraste or any(x in ex["mot"] for x in morceaux), (r["id"], ex["mot"])
    with io.open(os.path.join(ICI, "prononciation.json"), "w", encoding="utf-8", newline="\n") as fo:
        json.dump({"_note": "Derive de japonais/datos/prononciation_construire.py : ne pas modifier a la main. Brouillon.",
                   "groupes": GROUPES}, fo, ensure_ascii=False, indent=1)
        fo.write("\n")
    print("%d regles en %d groupes -> prononciation.json"
          % (sum(len(g["regles"]) for g in GROUPES), len(GROUPES)))


if __name__ == "__main__":
    main()
