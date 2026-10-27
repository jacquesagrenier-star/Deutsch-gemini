# -*- coding: utf-8 -*-
"""Les prompts des repliques de 05-vhs et d'es-05-la-tienda, du meme gabarit que 04 et es-04.

    python -X utf8 video/prompts_repliques_suite.py   -> _essai-avatar/prompts/planNN.txt
    python video/verifier_prompt.py --scene 05-vhs
    python video/verifier_prompt.py --scene es-05-la-tienda

Ecrit le 26 oct. 2026 (nuit). Un fichier a part plutot qu'une section de plus dans
prompts_repliques_de.py / _es.py : ces deux-la reecrivent, a chaque lancement, les prompts
d'episodes DEJA TOURNES ; celui-ci ne touche que les deux episodes a venir. Le gabarit
(CAMERA, FIN, les pronoms) est importe de prompts_repliques_de.py : une seule source.

Ce que le gabarit impose est explique en tete de prompts_repliques_de.py (camera-qui-bouge,
interlocuteur-fantome, geste-repete, texte-incruste, fin-sans-intention, garde-negative).

LES COTES SUIVENT LA GEOGRAPHIE DES FEUILLES (A-TOURNER.txt) :
  05-vhs        le couloir : Mark -> le Hausmeister : DROITE ; le Hausmeister : GAUCHE.
                la classe : Carmen (au tableau) -> la porte et la chaise libre : DROITE ;
                Anna (assise a gauche de Mark) : DROITE ; Mark : GAUCHE.
                le bas de l'escalier : Mark : GAUCHE ; Anna : DROITE.
  es-05         la boutique : Mark (devant la cabine, a gauche) : DROITE ;
                Ana (derriere son comptoir, a droite) : GAUCHE -- comme es-03 et es-04.
Ce fichier est la source ; les planNN.txt se regenerent, ils ne s'editent pas.
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
from prompts_repliques_de import CAMERA, FIN, MOYEN, IL, ELLE   # noqa: E402

ASSIS = ("medium shot", "seen from the waist up, seated at the table")

# Les fonds, en positif.
FLUR = ("Behind {him} the corridor stays quiet, soft and out of focus: the pale green wall, the row of closed "
        "wooden doors, the ceiling lights steady. {His} eyes rest on a fixed point just beyond the {cote} edge "
        "of the frame and stay there for the whole shot.")
KURS = ("Behind {him} the classroom stays warm and soft and out of focus: the pale walls, the dark evening "
        "windows, the other learners still at their tables. {His} eyes rest on a fixed point just beyond the "
        "{cote} edge of the frame and stay there for the whole shot.")
TAFEL = ("Behind {him} the blank white board and the pale wall of the classroom stay soft and out of focus, "
         "still, in the even ceiling light. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
         "frame and stay there for the whole shot.")
TREPPE = ("Behind {him} the stairwell stays quiet, soft and out of focus: the worn stone steps going up, the "
          "wooden handrail, the glass entrance door dark with the evening. {His} eyes rest on a fixed point just "
          "beyond the {cote} edge of the frame and stay there for the whole shot.")
TIENDA = ("Behind {him} the little shop stays warm and soft and out of focus: the rails of clothes, the wooden "
          "shelves of folded sweaters, the morning light from the street window. {His} eyes rest on a fixed "
          "point just beyond the {cote} edge of the frame and stay there for the whole shot.")
MOSTRADOR = ("Behind {him} the wooden shelves of folded sweaters in soft colours stay warm and out of focus, "
             "still, in the morning light. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
             "frame and stay there for the whole shot.")

# Ce qu'on voit sur le haut du corps, du premier au dernier image (texte-incruste).
TENUE = {
    ("05-vhs", "mark"): "Across his chest we see only his open plain navy-blue padded jacket, the plain light-grey "
                        "knit of his sweater and the dark grey strap of his backpack, from the first frame to the "
                        "last.",
    ("05-vhs", "mark-assis"): "Across his chest we see only his open plain navy-blue padded jacket and the plain "
                              "light-grey knit of his sweater, from the first frame to the last.",
    ("05-vhs", "anna"): "Across her chest we see only her open rust-red wool coat and the plain cream knit of her "
                        "sweater, from the first frame to the last.",
    ("05-vhs", "hausmeister"): "Across his chest we see only his plain grey cotton work coat, buttoned to the top, "
                               "from the first frame to the last.",
    ("05-vhs", "carmen"): "Across her chest we see only her plain dark teal cardigan and her plain white blouse, "
                          "from the first frame to the last.",
    ("es-05-la-tienda", "mark"): "Across his chest we see only his plain white long-sleeved cotton shirt, from the "
                                 "first frame to the last.",
    ("es-05-la-tienda", "mark-mediana"): "Across his chest we see only his new plain mustard-yellow padded jacket, "
                                         "open over his plain white shirt, from the first frame to the last.",
    ("es-05-la-tienda", "ana"): "Across her chest we see only her plain dark green knit cardigan over her plain "
                                "white T-shirt, from the first frame to the last.",
}
# Les plans ou une main se pose sur la poitrine.
TENUE_PLAN = {
    ("05-vhs", 12): "Across her chest we see only her open rust-red wool coat, the plain cream knit of her sweater "
                    "and her hand resting flat on it, from the first frame to the last.",
    ("05-vhs", 13): "Across his chest we see only his open plain navy-blue padded jacket, the plain light-grey knit "
                    "of his sweater and his fingertips resting on it, from the first frame to the last.",
    ("es-05-la-tienda", 8): "Across his chest we see only his plain white long-sleeved cotton shirt and his own "
                            "crossed forearms, from the first frame to the last.",
    ("es-05-la-tienda", 17): "Across her chest we see only her plain dark green knit cardigan, her plain white "
                             "T-shirt and her hand resting flat on it, from the first frame to the last.",
    ("es-05-la-tienda", 18): "Across his chest we see only his new plain mustard-yellow padded jacket, his plain "
                             "white shirt and his hand resting flat on it, from the first frame to the last.",
}

# L'espace entre le personnage et le bord ou est l'autre, rempli du debut a la fin.
BORD = {
    ("05-vhs", "mark", "right"):
        "On the right of the picture, between him and the edge of the frame, the corridor runs on, open and "
        "quiet: the pale green wall and a closed wooden door, from the first frame to the last.",
    ("05-vhs", "hausmeister", "left"):
        "On the left of the picture, between him and the edge of the frame, the corridor runs on towards the "
        "open door of the stairwell, open and quiet, from the first frame to the last.",
    ("05-vhs", "carmen", "right"):
        "On the right of the picture, between her and the edge of the frame, the end of the blank white board "
        "and the pale wall run on, open and quiet, from the first frame to the last.",
    ("05-vhs", "anna-assise", "right"):
        "On the right of the picture, between her and the edge of the frame, the pale wooden table runs on with "
        "an open exercise book on it, open and quiet, from the first frame to the last.",
    ("05-vhs", "mark-assis", "left"):
        "On the left of the picture, between him and the edge of the frame, the pale wooden table runs on, its "
        "surface bare, open and quiet, from the first frame to the last.",
    ("05-vhs", "mark-eg", "left"):
        "On the left of the picture, between him and the edge of the frame, the ground-floor hall runs on, open "
        "and quiet: the pale wall and the dark glass of the entrance door, from the first frame to the last.",
    ("05-vhs", "anna-eg", "right"):
        "On the right of the picture, between her and the edge of the frame, the foot of the staircase and its "
        "wooden handrail run on, open and quiet, from the first frame to the last.",
    ("es-05-la-tienda", "mark", "right"):
        "On the right of the picture, between him and the edge of the frame, the open wooden floor of the shop "
        "and the warm shelves of folded sweaters far behind run on, open and still, from the first frame to the "
        "last.",
    ("es-05-la-tienda", "ana", "left"):
        "On the left of the picture, between her and the edge of the frame, the wooden top of her counter runs "
        "on, bare and quiet, from the first frame to the last.",
}

# UN GESTE PAR REPLIQUE, ecrit pour CE que dit la replique. La main immobile D'ABORD.
GESTES = {
    # ---------------- 05 VHS -- le couloir ----------------
    # Mark : « Entschuldigung, wo ist Raum zweihundertvierzehn? » : la paume du « ou ? »
    ("05-vhs", 3):
        "His hand nearer the left edge of the picture stays holding the strap of his backpack at his shoulder, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « wo » it comes up to the "
        "height of his chest, palm open and turned up, fingers loosely apart, and it stays there while he asks.",
    # Mark : « Im ersten? Aber ich bin doch im zweiten! » : deux doigts, DEUX
    ("05-vhs", 5):
        "His hand nearer the left edge of the picture stays holding the strap of his backpack at his shoulder, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « zweiten » it rises in front "
        "of his chest with the index and the middle finger up, two, and it stays there holding them up.",
    # Le Hausmeister : « Das ist im zweiten Stock » : l'index vers le plafond
    ("05-vhs", 4):
        "His hand nearer the right edge of the picture stays hanging at his side, closed round a ring of keys, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « zweiten Stock » it rises to "
        "the height of his shoulder with the index finger pointing straight up at the ceiling, the floor above, "
        "and it stays pointing there.",
    # Le Hausmeister : « Erdgeschoss, erster Stock, zweiter Stock » : trois marches dans l'air
    ("05-vhs", 6):
        "His hand nearer the right edge of the picture stays hanging at his side, closed round a ring of keys, "
        "exactly as in the image, for the whole shot. Only his other hand moves: it comes up flat, palm down, at "
        "the height of his belt, and as he names the three floors it rises in three small even steps, a few "
        "centimetres each, and it stays at the third step, palm down.",
    # ---------------- 05 VHS -- la classe ----------------
    # Carmen : « Siéntate allí » : le bras vers la chaise libre
    ("05-vhs", 8):
        "Her hand nearer the left edge of the picture stays holding a closed board marker low in front of her, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « siéntate » it comes "
        "out towards the right edge of the picture at the height of her chest, palm open and turned up, showing "
        "the way to a seat, and it stays there.",
    # Carmen : « en parejas » : deux doigts cote a cote
    ("05-vhs", 11):
        "Her hand nearer the left edge of the picture stays holding a closed board marker low in front of her, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « parejas » it rises "
        "beside her face with the index and the middle finger up and pressed together, side by side, a pair, and "
        "it stays there.",
    # Anna : « Der Mann aus der Bäckerei! » : la main pres de la bouche, elle chuchote
    ("05-vhs", 9):
        "Her hand nearer the left edge of the picture stays resting flat on her open exercise book on the table, "
        "exactly as in the image, for the whole shot. Only her other hand moves: as she whispers it rises beside "
        "her mouth, fingers together, a little apart from her cheek, the hand of someone whispering in class, "
        "and it stays there.",
    # Anna : « Me llamo Anna » : la main a plat sur la poitrine
    ("05-vhs", 12):
        "Her hand nearer the left edge of the picture stays resting flat on her open exercise book on the table, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « me llamo » it rises and "
        "lays itself flat on her chest, on the cream knit of her sweater, and it stays there.",
    # Mark : « Anna… So heißen Sie also! » : la paume qui lui rend son prenom
    ("05-vhs", 10):
        "His hand nearer the right edge of the picture stays resting flat on the bare table, exactly as in the "
        "image, for the whole shot. Only his other hand moves: on « Anna » it comes up a few centimetres from the "
        "table, palm open and turned up towards the left edge of the picture, as if handing her back her own "
        "name, and it stays there.",
    # Mark : « ¡Yo también! » : le bout des doigts tape deux fois sa poitrine
    ("05-vhs", 13):
        "His hand nearer the right edge of the picture stays resting flat on the bare table, exactly as in the "
        "image, for the whole shot. Only his other hand moves: on « yo » it comes to his chest and its fingertips "
        "tap it twice, me, and then they stay resting there.",
    # ---------------- 05 VHS -- le bas de l'escalier ----------------
    # Mark : « Auf Spanisch duzen wir uns schon… » : le pouce vers la classe, la-haut
    ("05-vhs", 15):
        "His hand nearer the right edge of the picture stays resting on the wooden handrail, exactly as in the "
        "image, for the whole shot. Only his other hand moves: on « Spanisch » it comes up beside his shoulder, "
        "loosely closed, the thumb pointing up and back over that shoulder, towards the classroom upstairs, and "
        "it stays there.",
    # Anna : « Auf Deutsch noch nicht. » : l'index leve, « pas encore »
    ("05-vhs", 16):
        "Her hand nearer the left edge of the picture stays on the strap of her canvas bag at her shoulder, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « noch nicht » it rises in "
        "front of her chest with the index finger up and tilts once from side to side, a few centimetres, not "
        "yet, and then it stays up, still.",
    # ---------------- es-05 -- Ana derriere son comptoir ----------------
    # « ¡Anda! ¡El chico del café! » : le bout des doigts a la joue, surprise ravie
    ("es-05-la-tienda", 3):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « ¡Anda! » it rises to her cheek and its "
        "fingertips rest lightly against it, delighted surprise, and it stays there.",
    # « Es mi tienda. » : la paume qui fait le tour de la boutique
    ("es-05-la-tienda", 5):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « mi tienda » it rises to the height of "
        "her chest, palm up, and opens in one slow arc towards the left edge of the picture, taking in the whole "
        "shop, and it stays at the end of the arc, palm up.",
    # « ¿Una qué? » : la paume « quoi ? », doigts ecartes
    ("es-05-la-tienda", 7):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « qué » it rises to the height of her "
        "shoulder, palm up and open, fingers spread, and it stays there while her head tilts a little.",
    # « ¡Ah, una chaqueta! » : l'index pres de la tempe, compris
    ("es-05-la-tienda", 10):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « ¡Ah! » it rises beside her temple with "
        "the index finger up, the idea arriving, and it stays there.",
    # « ¿Chica? ¡Usted es un chico! » : le dos des doigts devant la bouche, le rire
    ("es-05-la-tienda", 12):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « ¿Chica? » it rises and the backs of its "
        "fingers touch her chin as she laughs, and it stays resting there under her chin.",
    # « Pruebe la mediana. » : l'index vers le portant
    ("es-05-la-tienda", 15):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « mediana » it comes up and its index "
        "finger points towards the left edge of the picture and a little downwards, towards the rail of jackets, "
        "and it stays pointing there.",
    # « me llamo Ana » : la main a plat sur la poitrine
    ("es-05-la-tienda", 17):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « me llamo » it rises and lays itself flat "
        "on her chest, on the green knit of her cardigan, and it stays there.",
    # « ¡Dos, Mark! » : deux doigts leves
    ("es-05-la-tienda", 20):
        "Her hand nearer the right edge of the picture stays resting flat on the wooden counter, exactly as in "
        "the image, for the whole shot. Only her other hand moves: on « dos » it rises to the height of her "
        "shoulder with the index and the middle finger up, two, and it stays there holding them up while she "
        "laughs.",
    # ---------------- es-05 -- Mark devant la cabine ----------------
    # « ¡Usted otra vez! ¿Trabaja aquí? » : l'index vers le sol, ICI
    ("es-05-la-tienda", 4):
        "His hand nearer the left edge of the picture stays hanging at his side, open and empty, exactly as in "
        "the image, for the whole shot. Only his other hand moves: on « aquí » it comes down in front of him "
        "with the index finger pointing down at the floor in front of him, here, and it stays pointing "
        "there.",
    # « Busco una chamarra. » : la paume qui presente le mot
    ("es-05-la-tienda", 6):
        "His hand nearer the left edge of the picture stays hanging at his side, open and empty, exactly as in "
        "the image, for the whole shot. Only his other hand moves: on « chamarra » it comes up to the height of "
        "his chest, palm open and turned up towards the right edge of the picture, offering the word, and it "
        "stays there.",
    # « ¡para el frío! » : les bras croises qui se frottent
    ("es-05-la-tienda", 8):
        "On « frío » both his arms come up and cross over his chest, each hand holding the opposite upper arm, "
        "and his hands rub his sleeves twice, quickly, the shiver of someone cold, and then they stay there, "
        "crossed, while he laughs.",
    # « Chica, por favor. » : le pouce et l'index, petit
    ("es-05-la-tienda", 11):
        "His hand nearer the left edge of the picture stays hanging at his side, open and empty, exactly as in "
        "the image, for the whole shot. Only his other hand moves: on « chica » it rises in front of his chest "
        "with the thumb and the index finger a few centimetres apart, small, and it stays there.",
    # « ¡Perfecta! Me la llevo. » : il tient le bord de la veste
    ("es-05-la-tienda", 16):
        "His hand nearer the left edge of the picture stays hanging at his side, open and empty, exactly as in "
        "the image, for the whole shot. Only his other hand moves: on « ¡Perfecta! » it takes hold of the open "
        "front edge of the mustard-yellow jacket at the height of his chest and draws it a few centimetres "
        "forward, showing it off, and it stays holding it.",
    # « ¡Yo soy Mark! » : la main a plat sur la poitrine
    ("es-05-la-tienda", 18):
        "His hand nearer the left edge of the picture stays hanging at his side, open and empty, exactly as in "
        "the image, for the whole shot. Only his other hand moves: on « Mark » it rises and lays itself flat on "
        "his chest, on the white shirt inside the open jacket, and it stays there.",
}

# (scene, plan, locuteur-tenue, pronoms, cadre, cote, fond, cle BORD, emotion, parole, apres)
PLANS = [
    # ================= 05 VHS =================
    ("05-vhs", 3, "mark", IL, MOYEN, "right", FLUR, "mark",
     "He has just come up the stairs at a brisk pace, a little out of breath, quite sure he is on the right "
     "floor. Polite and easy, he asks rather than guesses.",
     "He says excuse me and asks one short question, his eyebrows rising on it.",
     "waits for the answer, friendly and still a little out of breath, his mouth closed"),
    ("05-vhs", 4, "hausmeister", IL, MOYEN, "left", FLUR, "hausmeister",
     "Matter of fact, neither brusque nor funny on purpose: he has given this answer many times, and he simply "
     "states where things are.",
     "He repeats the number as a question, then states two plain facts.",
     "waits with a calm, level look, his mouth closed, the matter stated"),
    ("05-vhs", 5, "mark", IL, MOYEN, "right", FLUR, "mark",
     "Genuinely lost, and already finding it funny: he counted the floors himself, he is sure of it.",
     "He repeats the word as a question, then protests in two short sentences, half laughing.",
     "keeps an amused, puzzled grin and waits, his mouth closed"),
    ("05-vhs", 6, "hausmeister", IL, MOYEN, "left", FLUR, "hausmeister",
     "Deadpan, the funniest thing in the episode said with no expression at all: to him this is the most "
     "obvious rule in the world.",
     "He names the ground floor, lists three floors one after the other, and ends with one plain sentence.",
     "holds a flat, patient look, his mouth closed, as if nothing could be simpler"),
    ("05-vhs", 8, "carmen", ELLE, MOYEN, "right", TAFEL, "carmen",
     "A teacher who runs her class with a smile and a firm hand: the latecomer is welcome, and he will sit "
     "where she says.",
     "She calls out one short sentence in Spanish, then gives one short instruction, warm and firm.",
     "keeps a warm, expectant smile, her mouth closed, waiting for him to sit down"),
    ("05-vhs", 11, "carmen", ELLE, MOYEN, "right", TAFEL, "carmen",
     "She launches the exercise with energy: this is her favourite part of the lesson.",
     "She announces the exercise in Spanish, then asks two short model questions, clearly, for the whole class.",
     "keeps a bright encouraging smile, her mouth closed, waiting for the pairs to start"),
    ("05-vhs", 9, "anna", ELLE, ASSIS, "right", KURS, "anna-assise",
     "The man from the bakery has just sat down beside her, in her own Spanish class. Surprised and delighted, "
     "and she keeps her voice down because the lesson is going on.",
     "She whispers one short sentence, her eyebrows rising on it.",
     "keeps a surprised, delighted half-smile, her mouth closed"),
    ("05-vhs", 12, "anna", ELLE, ASSIS, "right", KURS, "anna-assise",
     "She does the exercise like a good student, carefully, in her new Spanish, with a small smile at playing "
     "the game.",
     "She says her name in Spanish, then says where she lives, slowly and clearly.",
     "waits for his answer with an amused, attentive look, her mouth closed"),
    ("05-vhs", 10, "mark-assis", IL, ASSIS, "left", KURS, "mark-assis",
     "He has just learned her name from the teacher, and it delights him; he whispers, as she did.",
     "He whispers her name, then one short glad sentence.",
     "keeps a wide glad smile that reaches his eyes, his mouth closed"),
    ("05-vhs", 13, "mark-assis", IL, ASSIS, "left", KURS, "mark-assis",
     "A real surprise: the same street. He forgets to whisper for a moment.",
     "He asks one short question in Spanish, then answers in two short pieces, delighted.",
     "keeps laughing quietly at the coincidence, his mouth closed"),
    ("05-vhs", 15, "mark", IL, MOYEN, "left", TREPPE, "mark-eg",
     "After class, at the foot of the stairs, he dares a little joke, half serious: a playful, slightly shy "
     "smile.",
     "He says one short sentence and lets it trail off, waiting to see how she takes it.",
     "waits for her answer with a hopeful, playful half-smile, his mouth closed"),
    ("05-vhs", 16, "anna", ELLE, MOYEN, "right", TREPPE, "anna-eg",
     "Her dry humour: two words, said kindly, a smile arriving on the last one. A rule of politeness, said with "
     "warmth, nothing more.",
     "She answers in one very short sentence, the smile arriving on the last word.",
     "keeps the quiet amused smile, her mouth closed, her eyes steady"),
    # ================= es-05 LA TIENDA =================
    ("es-05-la-tienda", 3, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "A customer has just walked into her shop and she knows his face: the young man from the café. Glad and "
     "amused.",
     "She calls out one short word of surprise, then names him in one short sentence.",
     "keeps a delighted smile, her mouth closed"),
    ("es-05-la-tienda", 5, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "Her moment: the quiet pride of someone in her own shop.",
     "She says one short sentence about the shop, then asks one short question.",
     "waits for his answer, proud and friendly, her mouth closed"),
    ("es-05-la-tienda", 7, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "She has no idea what the word means, and she is not afraid to say so.",
     "She asks one very short question, her eyebrows rising high on it.",
     "keeps a puzzled, amused frown, her mouth closed"),
    ("es-05-la-tienda", 10, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "She has understood, and the misunderstanding amuses her.",
     "She says the right word with a little laugh, then asks one short question.",
     "waits for his answer, amused, her mouth closed"),
    ("es-05-la-tienda", 12, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "She bursts out laughing: in Madrid that word means a girl. Then she gives him the right word, kindly, "
     "never from above.",
     "She repeats his word as a question through a laugh, then says two short sentences.",
     "keeps laughing quietly, her mouth closed, her eyes on him"),
    ("es-05-la-tienda", 15, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "Deadpan, holding back a laugh at the sight of him in the tiny jacket.",
     "She makes one thoughtful sound, then says one short suggestion.",
     "holds a straight face with difficulty, her mouth closed, the laugh in her eyes"),
    ("es-05-la-tienda", 17, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "Simple and warm: the price, a little pause, and at last her name. Nothing more than friendliness.",
     "She states the price, pauses, then says her name in one short sentence.",
     "keeps a warm, open smile, her mouth closed"),
    ("es-05-la-tienda", 20, "ana", ELLE, MOYEN, "left", MOSTRADOR, "ana",
     "The greeting went wrong and she laughs openly; nobody is to blame.",
     "She laughs and says two short sentences, repeating the number.",
     "keeps laughing, her mouth closed, her eyes bright"),
    ("es-05-la-tienda", 4, "mark", IL, MOYEN, "right", TIENDA, "mark",
     "A glad surprise: the woman from the café is behind the counter. He is still formal with her.",
     "He says one short glad sentence, then asks one short question.",
     "waits for her answer, smiling, his mouth closed"),
    ("es-05-la-tienda", 6, "mark", IL, MOYEN, "right", TIENDA, "mark",
     "Sure of himself: he knows exactly what he wants, and the word he uses at home.",
     "He says one short sentence, plainly.",
     "waits, pleased and confident, his mouth closed"),
    ("es-05-la-tienda", 8, "mark", IL, MOYEN, "right", TIENDA, "mark",
     "He acts out the cold to be understood, and laughs at himself doing it.",
     "He repeats his word, then adds a few words with a laugh.",
     "keeps a sheepish laughing smile, his mouth closed"),
    ("es-05-la-tienda", 11, "mark", IL, MOYEN, "right", TIENDA, "mark",
     "Calm and polite: he orders his size the way he always has.",
     "He says one word and adds please.",
     "waits politely, his mouth closed"),
    ("es-05-la-tienda", 16, "mark-mediana", IL, MOYEN, "right", TIENDA, "mark",
     "Delighted: at last a jacket that fits, and he is warm.",
     "He exclaims one word, then says two short sentences.",
     "keeps a wide pleased smile that reaches his eyes, his mouth closed"),
    ("es-05-la-tienda", 18, "mark-mediana", IL, MOYEN, "right", TIENDA, "mark",
     "At last the names, three meetings after the airport: plain gladness.",
     "He says his name in one short sentence, then one word of greeting.",
     "keeps a warm, open smile, his mouth closed"),
]


def ecrire(sc, n, tenue, P, cadre, cote, fond, bord, emotion, parole, apres):
    f = lambda s: s.format(plan=cadre[0], cadrage=cadre[1], cote=cote, **P)
    regard = (" %s speaks towards a point just beyond the %s edge of the picture, level with %s own eyes."
              % (P["He"], cote, P["his"]))
    blocs = [f(CAMERA), emotion, parole + regard + " Let %s face follow the voice." % P["his"]]
    blocs.append(GESTES[(sc, n)])
    blocs.append(TENUE_PLAN.get((sc, n)) or TENUE[(sc, tenue)])
    blocs.append(BORD[(sc, bord, cote)])
    blocs.append("Finally %s stops speaking and %s. %s blinks, %s breathes, and %s holds that expression "
                 "the whole time %s waits." % (P["he"], apres, P["He"], P["he"], P["he"], P["he"]))
    blocs += [f(fond), f(FIN)]
    d = os.path.join(RACINE, "video", "episode-" + sc, "_essai-avatar", "prompts")
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "plan%02d.txt" % n), "w", encoding="utf-8").write("\n\n".join(blocs) + "\n")


if __name__ == "__main__":
    for x in PLANS:
        ecrire(*x)
    print("%d prompts ecrits" % len(PLANS))
