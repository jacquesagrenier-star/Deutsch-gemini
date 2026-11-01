# -*- coding: utf-8 -*-
"""Un ressort comique VISIBLE dans chacune des 28 scenes encore a generer.

    python japonais/scenes/ajouter_humour.py          # applique (une seule fois)
    python japonais/scenes/ajouter_humour.py --voir   # montre sans ecrire

Decide par Jacques le 31 oct. 2026 (« Oui, ajoute-les ») : chaque scene a son
gag, montre dans l'image et pas seulement raconte par les questions ; quelques
gags reviennent au long de l'annee (bible, section 3 bis). Les quatre scenes du
pilote (kuukou, heya, kuyakusho, hanami) sont deja payees et restent telles
quelles. Chaque remplacement doit trouver son texte exactement une fois, sinon
rien n'est ecrit. Ensuite : video/verifier_prompt.py sur chaque prompt.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
SCENES = os.path.normpath(os.path.join(ICI, "..", "..", "visuel", "scenes"))

R = {
    "suupaa": [(
        "behind her, an old man in a grey cap waits his turn with a basket holding a fish wrapped in clear film and a bottle of soy sauce.",
        "behind her, an old man in a grey cap waits his turn with a basket holding a fish wrapped in clear film and a bottle of soy sauce; he holds up his own small pale-blue card beside her shoulder between two fingers to show her, with a kind, amused wink.",
    )],
    "raamen": [(
        "on the right, a clear plastic umbrella stands in a steel umbrella stand by the door.",
        "on the right, a clear plastic umbrella stands in a steel umbrella stand by the door, and beside it an office worker of about thirty in a white shirt and a dark tie waits his turn, standing upright behind her, and only his arm reaches past her shoulder to point at the right yellow button, with a friendly, patient grin.",
    )],
    "sentou": [(
        "leaning her forearms on the counter, smiling and explaining something with one raised forefinger;",
        "leaning her forearms on the counter and holding up a small, thin white towel in one hand to show the right size, smiling as she explains;",
    ), (
        "she holds a folded white towel against her chest with both hands and listens with wide eyes and a nervous smile;",
        "she hugs an enormous, thick, fluffy plain orange bath towel against her chest with both arms, bundled up to her chin, and listens with wide eyes and a sheepish smile;",
    )],
    "tsuyu": [(
        "she holds a small clear plastic umbrella over her head with one hand, tilted against the rain, and with the other hand she hugs a big plain white cloth bag full of laundry against her side;",
        "she holds a tiny clear plastic umbrella over her head with one hand; it covers her head alone, and her shoulders, her jacket sleeves and the big plain white cloth bag full of laundry that she hugs against her side with the other hand are soaked dark with rain;",
    ), (
        "a small boy in a yellow rain hat and yellow boots walks holding the hand of his mother, who holds a plain dark-blue umbrella over them both;",
        "a small boy in a yellow rain hat and yellow boots walks holding the hand of his mother, who holds a huge plain dark-blue umbrella over them both; the boy has turned round to stare at the young woman's tiny umbrella with round eyes;",
    )],
    "yuubinkyoku": [(
        "she pushes a square parcel in brown paper across the counter with both hands, her chin lifted, proud of her parcel;",
        "she pushes an enormous square parcel in brown paper across the counter with both hands, so big that its top reaches her chin, wound round and round with far too much brown tape; her chin lifted above it, she is very proud of her parcel;",
    ), (
        "holds a blank white label in his hand, pointing with a pen at the blank address lines on the label, smiling helpfully;",
        "leans to one side to see her past the huge parcel, holding a blank white label in his hand and pointing with a pen at the blank address lines on the label, smiling helpfully;",
    )],
    "kissaten": [(
        "at the next table on the left, an old man in a grey summer shirt reads a folded newspaper, his cup of tea in front of him;",
        "at the next table on the left, an old man in a grey summer shirt has lowered his folded newspaper and watches the young woman over the top of it with an amused smile, his cup of tea in front of him;",
    ), (
        "holding it level with both hands, a concentrated smile on her face, her eyes on the cups;",
        "holding it with both hands and making a polite little bow over it as she walks, her eyes fixed on the cups, the coffee trembling right up to their rims, a concentrated smile on her face;",
    )],
    "shinkansen": [(
        "moves her lips as if repeating something to herself, frowning in concentration;",
        "moves her lips as if repeating something to herself, frowning in concentration, her eyes darting sideways towards her neighbour;",
    ), (
        "an old man in a pale grey summer shirt sleeps with his arms folded and his chin on his chest, a folded newspaper on his knee.",
        "an old man in a pale grey summer shirt, a folded newspaper on his knee, sits upright and turns his head towards her notebook with one forefinger raised, whispering the next words to her, with a mischievous, delighted smile.",
    )],
    "daidokoro": [(
        "holding a wooden ladle with a little soup in a small bowl out towards her granddaughter, watching her face with a mischievous smile;",
        "holding a wooden ladle in one hand, watching her granddaughter's face with a mischievous smile; her other hand, held behind her back where the camera sees it, hides a small plain orange paper packet of soup stock;",
    )],
    "obon": [(
        "an offering of two peaches, a small bunch of grapes and a little cup of sake;",
        "an offering of two peaches, a small bunch of grapes, a little cup of sake and a plain silver can of beer, the grandfather's favourite;",
    )],
    "natsumatsuri": [(
        "laughing with her mouth full; Yui, beside her, holds a round paper fan and points with it at something further down the lane, smiling.",
        "laughing with her mouth open and her tongue bright red from the syrup; Yui, beside her, points at the red tongue with her round paper fan, laughing too.",
    )],
    "hanabi": [(
        "the young woman points up at the sky with one arm, her mouth open in delight; Yui leans her head towards her, holding a round paper fan against her chest;",
        "the young woman holds her old black film camera up towards the sky with both hands, and its flash has just gone off, a burst of white light; Yui leans her head towards her, holding a round paper fan against her chest, laughing;",
    ), (
        "a couple sharing a fan, an old man on a folding stool.",
        "a couple sharing a fan; and just in front of the two friends, an old man on a folding stool, his bald head lit up bright white by the flash, has turned his head halfway round, blinking and amused.",
    )],
    "kamakura": [(
        "the young woman holds an ice-cream cone of white soft-serve that is dripping down her fingers, laughing and licking it; Yui holds out a white paper napkin to her, laughing too;",
        "the young woman holds an ice-cream cone of white soft-serve, dripping down her fingers, high above her head at arm's length, laughing, while a large brown bird of prey swoops low over the towel towards it with its wings spread wide; Yui holds out a white paper napkin to her, laughing too;",
    )],
    "fushimi": [(
        "in the middle of the steps, the young woman of the reference pictures stands seen whole from her head to her white sneakers, which stand on a stone step with their shadow beside them; she is turned in three-quarter view towards the camera, holding her old black film camera up to her eye with both hands, photographing the gates above and behind the camera, one eye closed, her mouth a little open in concentration;",
        "at the bottom left, the young woman of the reference pictures crouches face to face with the stone fox, seen whole from her head to her white sneakers, which stand on a stone step with their shadow beside them, in three-quarter view; she photographs the fox from very close with her old black film camera held in both hands at chest height, and she has tilted her head to exactly the same angle as the fox, with the same solemn face;",
    ), (
        "a few steps above her, two other visitors walk up the path: an old couple in beige jackets, the man with a walking stick, the woman with a small cloth bag;",
        "a few steps above her, two other visitors have stopped on the path to smile at the young woman and the fox: an old couple in beige jackets, the man with a walking stick, the woman with a small cloth bag;",
    )],
    "ryokan": [(
        "grinning; a small white towel is folded over her shoulder.",
        "grinning; a small white towel is folded neatly on top of her curly head, like an old man at the hot spring.",
    )],
    "momiji": [(
        "points with the other hand up at the trees, her face lifted, amazed; Yui, beside her, holds a single red maple leaf up by its stem, turning it in the light, smiling;",
        "points with the other hand up at the trees, her face lifted, amazed; a single red maple leaf sits on top of her curly hair like a little hat; Yui, beside her, holds up a second red maple leaf by its stem next to it, comparing the two, laughing;",
    )],
    "izakaya": [(
        "holding up his glass with both hands, a big rare smile on his face;",
        "holding up his glass with both hands, white beer foam running over the rim and down his fingers, a big rare smile on his face;",
    ), (
        "and carefully pouring beer into Mr Sakamoto's glass, concentrating, a proud little smile on her lips;",
        "and pouring beer into Mr Sakamoto's glass so carefully and for so long that the foam has risen over the rim, concentrating, the tip of her tongue between her teeth, a proud little smile on her lips;",
    )],
    "kusuriya": [(
        "showing it to the young woman, explaining kindly, the other hand resting on the counter;",
        "showing it to the young woman, explaining kindly, her lips pressed together on a smile, the other hand resting on the counter;",
    ), (
        "and she holds one hand on her forehead to show that she has a fever, the other hand holding a crumpled tissue;",
        "and she acts out her illness for the pharmacist like a game of charades: one hand on her forehead, the other on her stomach with a crumpled tissue in it, her eyes rolled up and her mouth pulled into a big dramatic grimace;",
    ), (
        "looking at the pharmacist and nodding.",
        "looking at the pharmacist and nodding, trying hard to keep a straight face.",
    )],
    "depaato": [(
        "and a second plain white shopping bag hangs from her wrist.",
        "and from her wrist hangs her first purchase of the day: a big plain white shopping bag, with a smaller plain white bag peeping out of its top, and an even smaller white bag peeping out of that one, holding one tiny wrapped box the size of a matchbox.",
    )],
    "furusato": [(
        "holding a large old photo album open in both arms; she looks from the black-and-white photograph to the real gate and back, her mouth open in wonder;",
        "holding a large old photo album open against her side with one arm; she stands exactly like the little boy in the black-and-white photograph, chin up, chest out, her other fist on her hip, with a very solemn face;",
    ), (
        "one gloved forefinger pointing at one small boy in the old photograph, smiling with her eyes half closed, remembering;",
        "one gloved forefinger pointing at one small boy in the old photograph, laughing with her eyes half closed;",
    )],
    "kotatsu": [(
        "the young woman of the reference pictures on the left, seen from her side, laughing with her head thrown back, holding a peeled mandarin orange;",
        "the young woman of the reference pictures on the left, so cosy that she has slid down under the quilt until only her head and shoulders are out, lying on her back on the tatami, laughing, a peeled mandarin orange held up above her face;",
    ), (
        "serving meat from the pot with long chopsticks into a bowl;",
        "sitting upright, only her arm reaching across the table to hold a piece of meat out with long chopsticks towards her friend's mouth, laughing;",
    )],
    "chichi-tochaku": [(
        "and opens his arms wide, his gloved hands spread, his face breaking into a broad, moved smile;",
        "and opens his arms wide for a big hug, his gloved hands spread, his face breaking into a broad laugh of surprise;",
    ), (
        "is caught mid-step, seen whole from her head to her white sneakers, one foot lifted from the floor, her scarf flying out behind her, about to throw her arms around him; in one hand she holds a small bunch of yellow flowers wrapped in white paper; her face, in three-quarter view, is laughing with tears in her eyes;",
        "stands just in front of him, seen whole from her head to her white sneakers, and makes him a perfect, formal Japanese bow from the waist, holding out a small bunch of yellow flowers wrapped in white paper in both hands; her face, in three-quarter view, has a mischievous smile, with tears of joy in her eyes;",
    )],
    "oomisoka": [(
        "Fumiko lifts noodles with her chopsticks and looks up at her son with a happy smile; Hiroshi, his bowl in his hands, looks back at his mother, his eyes moist and smiling;",
        "Hiroshi, worn out by his long journey, has dozed off sitting up, his head resting on his mother's shoulder and his bowl still held in his hands; Fumiko goes on lifting noodles with her chopsticks, a tender, amused smile on her face;",
    ), (
        "watching her father and grandmother with delight;",
        "her eyes going from her sleeping father to her grandmother, laughing;",
    )],
    "hatsumoude": [(
        "she holds an unfolded slip of white paper open in both gloved hands, reading it, her face bursting into a delighted grin;",
        "she holds an unfolded slip of white paper open in both gloved hands, turned towards her father to show it to him, her face bursting into a delighted grin;",
    ), (
        "beside her, Hiroshi of the fourth reference picture stands close behind her shoulder, reading the slip too, his eyebrows raised, laughing; Fumiko of the third reference picture, on her other side, claps her gloved hands together once, beaming.",
        "beside her, Hiroshi of the fourth reference picture holds his own unfolded slip of white paper, his face fallen in comic dismay, his shoulders slumped; Fumiko of the third reference picture, on her other side, laughs with one gloved hand in front of her mouth.",
    )],
    "kenrokuen": [(
        "the young woman holds her old black film camera up to her eye with both hands, photographing the garden; Hiroshi stands close beside her, pointing with one gloved hand at the great pine tree on the right, saying something with a warm smile;",
        "the young woman holds her old black film camera up to her eye with both hands, photographing her father, laughing behind the camera; Hiroshi stands close beside her, pointing with one gloved hand at the great pine tree on the right and explaining with a warm smile, while a clump of snow that has just fallen from an overhanging pine branch sits on top of his head and on his shoulders, white on his dark hair;",
    )],
    "ichinengo": [(
        "he holds an unfolded paper map in one hand and a phone in the other, looking a little lost and tired, and he smiles shyly;",
        "he bows to her from the waist, far too deep and stiff, an unfolded paper map in one hand and a phone in the other, and his big backpack has tipped forward onto the back of his head;",
    ), (
        "she bows politely to him from the waist, one hand held out towards him with the palm up, inviting him to join them, with a confident, welcoming smile;",
        "she answers with a small, perfect bow, one hand held out towards him with the palm up, inviting him to join them, holding back a laugh with a warm, welcoming smile;",
    )],
}


def main():
    voir = "--voir" in sys.argv
    nouveaux = {}
    for nom, paires in R.items():
        chemin = os.path.join(SCENES, nom + ".prompt.txt")
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        for ancien, neuf in paires:
            n = texte.count(ancien)
            if n != 1:
                sys.exit("%s : texte trouve %d fois, rien n'est ecrit :\n  %s" % (nom, n, ancien[:90]))
            texte = texte.replace(ancien, neuf)
        nouveaux[chemin] = texte
    for chemin, texte in nouveaux.items():
        if not voir:
            with open(chemin, "w", encoding="utf-8", newline="\n") as f:
                f.write(texte)
        print(("vu      " if voir else "ecrit   ") + os.path.basename(chemin))
    print("%d prompts." % len(nouveaux))


if __name__ == "__main__":
    main()
