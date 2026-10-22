# -*- coding: utf-8 -*-
"""Les prompts des repliques des episodes allemands 04 et 05, ecrits d'un seul gabarit.

    python -X utf8 video/prompts_repliques_de.py     -> _essai-avatar/prompts/planNN.txt

C'EST LE GABARIT DE video/prompts_repliques_es.py (22 oct. 2026), repris pour
l'allemand -- les episodes 1 a 3 ont leurs prompts ecrits a la main, et ils
restent tels quels. Ce fichier ne couvre que 04-schrippe et 05-pfand.

Ce que le gabarit impose, et pourquoi (chaque point est une prise payee, voir
video/verifier_prompt.py) :
  - la camera decrite comme un ETAT (camera-qui-bouge) ;
  - l'emotion situee dans la COURBE du personnage ;
  - un vrai VERBE DE PAROLE, et le regard donne par un POINT a hauteur des yeux
    (interlocuteur-fantome : l'autre n'est JAMAIS nomme) ;
  - UN GESTE DIFFERENT PAR REPLIQUE : la main immobile dite D'ABORD, puis le
    trajet de celle qui bouge, le cote dit par le BORD DE L'IMAGE (cote-du-corps),
    tenu jusqu'a la fin (geste-qui-revient) ;
  - la poitrine decrite du debut a la fin (texte-incruste) ;
  - l'espace entre le personnage et le bord ou est l'autre, rempli (BORD) ;
  - une INTENTION apres la parole (fin-sans-intention) ;
  - le fond en positif (garde-negative), le cadre qui tient jusqu'au bout.

LES COTES SUIVENT LA GEOGRAPHIE DES FEUILLES (A-TOURNER.txt), et elles gardent la
convention de la serie (personnages.json, _mise_en_scene) pour les DEUX recurrents :
Mark regarde vers la GAUCHE de l'image quand il parle a Anna, Anna vers la DROITE.
  04-schrippe  comptoir a DROITE : Mark -> la boulangere : DROITE ; la boulangere : GAUCHE ;
               Anna (dans la file, a gauche) : DROITE ; Mark tourne vers Anna : GAUCHE.
  05-pfand     le voisin sur son banc a GAUCHE : Mark : GAUCHE ; le voisin : DROITE ;
               a l'automate (a gauche de l'image) : Mark : GAUCHE.
Ce fichier est la source ; les planNN.txt se regenerent, ils ne s'editent pas.
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMERA = ("A static {plan} holds on {him}, {cadrage}. The camera is locked on a tripod and stays there for the whole "
          "shot: the same lens, the same height, the same distance. Keep {his} position and {his} distance from "
          "the camera exactly as in the image.")
FIN = ("The framing holds to the very end: in the last frame {he} is the same size and in the same place in "
       "the picture as in the first.")
MOYEN = ("medium shot", "seen from the hips up")

# Les fonds, en positif : ce qui est DANS l'image et y reste.
BAECKEREI = ("Behind {him} the bakery stays warm and soft and out of focus: the pale wall, the shelves of loaves, "
             "the warm lamps over the counter. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
             "frame and stay there for the whole shot.")
SPAETI = ("Behind {him} the evening street stays quiet, soft and out of focus, the warm light from the shop "
          "window steady on the pavement. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
          "frame and stay there for the whole shot.")
AUTOMAT = ("Behind {him} the pale wall of the shop entrance and the stack of blue plastic crates stay soft and "
           "out of focus. {His} eyes rest on the round dark opening of the machine at the {cote} edge of the "
           "frame and stay there for the whole shot.")

# Ce qu'on voit sur le haut du corps, du premier au dernier image (texte-incruste).
TENUE = {
    ("04-schrippe", "mark"): "Across his chest we see only his plain dark green sweater and the white collar of "
                             "his T-shirt, from the first frame to the last.",
    ("04-schrippe", "anna"): "Across her chest we see only her open rust-red wool coat and the plain cream knit "
                             "of her sweater, from the first frame to the last.",
    ("04-schrippe", "baeckerin"): "Across her chest we see only her plain dark blue apron and the white sleeves "
                                  "of her shirt, from the first frame to the last.",
    ("05-pfand", "mark"): "Across his chest we see only his plain dark burgundy sweater, from the first frame to "
                          "the last.",
    ("05-pfand", "nachbar"): "Across his chest we see only his plain bright yellow jacket, zipped to the collar, "
                             "from the first frame to the last.",
}
# La tenue d'un plan qui pose une main sur la poitrine (voir GESTES).
TENUE_PLAN = {
    ("04-schrippe", 16): "Across her chest we see only her open rust-red wool coat, the plain cream knit of her "
                         "sweater and her hand resting flat on it, from the first frame to the last.",
    ("05-pfand", 15): "Across his chest we see only his plain dark burgundy sweater and his hand resting flat "
                      "on it, from the first frame to the last.",
}

# L'espace entre le personnage et le bord ou est l'autre, rempli du debut a la fin
# (interlocuteur-fantome, 21 oct. 2026). Cle : (scene, locuteur, cote du regard).
BORD = {
    ("04-schrippe", "mark", "right"):
        "On the right of the picture, between him and the edge of the frame, the glass top of the counter and "
        "the warm lamps above it run on, open and quiet, from the first frame to the last.",
    ("04-schrippe", "mark", "left"):
        "On the left of the picture, between him and the edge of the frame, the shop runs on, open and soft: the "
        "pale wall and the daylight from the window, from the first frame to the last.",
    ("04-schrippe", "baeckerin", "left"):
        "On the left of the picture, between her and the edge of the frame, the glass counter with its baskets "
        "of rolls runs on, open and quiet, from the first frame to the last.",
    ("04-schrippe", "anna", "right"):
        "On the right of the picture, between her and the edge of the frame, the blurred dark green shoulder in "
        "the foreground stays exactly as it is in the image, just as blurred, from the first frame to the last.",
    ("05-pfand", "nachbar", "right"):
        "On the right of the picture, between him and the edge of the frame, the lit shop door and the pavement "
        "run on, open and quiet, from the first frame to the last.",
    ("05-pfand", "mark", "left"):
        "On the left of the picture, between him and the edge of the frame, the orange litter bin on its grey "
        "post stays exactly as it is in the image, and past it the pavement runs on, open and quiet, from the "
        "first frame to the last.",
    ("05-pfand", "mark-automat", "left"):
        "On the left of the picture, between him and the edge of the frame, the pale housing of the machine with "
        "its round dark opening stays exactly as it is in the image, from the first frame to the last.",
}

IL = {"he": "he", "him": "him", "his": "his", "He": "He", "His": "His"}
ELLE = {"he": "she", "him": "her", "his": "her", "He": "She", "His": "Her"}

# UN GESTE PAR REPLIQUE, ecrit pour CE que dit la replique. La main immobile
# D'ABORD, puis le trajet de celle qui bouge ; le cote par le bord de l'image.
# ⚠️ Pas de « his right hand », pas de « waist », « knee », « shoes » (reperes
#    hors champ), pas de nom de geste (shrug, thumbs up), pas de « lifts/raises
#    his hand » sans amplitude. Et pas de doigts entrelaces : ils fondent.
GESTES = {
    # --- 04 Schrippe -- Mark au comptoir (regard a DROITE, la boulangere) ---
    # « Guten Morgen! Ein Brötchen, bitte. » : il compte UN.
    ("04-schrippe", 3):
        "His hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « ein » it comes up in "
        "front of his chest with the index finger raised, one, and it stays there while he finishes.",
    # « Eine Schrippe. Gut. Und einen Pfannkuchen, bitte. » : il montre la vitrine.
    ("04-schrippe", 5):
        "His hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only his other hand moves: as he names the second thing it "
        "rises to the height of his chest and its index finger points loosely towards the right edge of the "
        "picture and a little downwards, into the display, and it stays pointing there.",
    # « Das ist kein Pfannkuchen! Das ist ein Berliner. » : la paume qui pese la chose.
    ("04-schrippe", 7):
        "His hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on his first words it comes up "
        "level with his chest, palm open and turned up, fingers together, held out towards the right edge of the "
        "picture as if weighing the thing on it, and it stays there, open.",
    # --- 04 Schrippe -- Mark tourne vers la file (regard a GAUCHE, Anna) ---
    # « Ja! Sie haben mir am Flughafen geholfen! » : la main ouverte du salut.
    ("04-schrippe", 11):
        "His hand nearer the right edge of the picture stays resting on the edge of the counter behind him, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « Ja! » it comes up level "
        "with his shoulder, palm open towards the left edge of the picture, fingers together, a glad greeting, "
        "and it stays raised there while he speaks.",
    # « Berlinerisch? Ich wollte nur ein Brötchen! » : la paume impuissante, bas.
    ("04-schrippe", 13):
        "His hand nearer the right edge of the picture stays resting on the edge of the counter behind him, "
        "exactly as in the image, for the whole shot. Only his other hand moves: on « nur » it turns palm up at "
        "the height of his belt, fingers loosely open, the helpless hand of all I wanted, and it stays there, "
        "palm up.",
    # « Und warum sagt hier niemand Berliner? » : le beignet invisible entre pouce et index.
    ("04-schrippe", 15):
        "His hand nearer the right edge of the picture stays resting on the edge of the counter behind him, "
        "exactly as in the image, for the whole shot. Only his other hand moves: as he asks it rises in front of "
        "his chest, the thumb and the index finger a few centimetres apart as if holding a small round thing, "
        "the pastry in question, and it stays there holding the air.",
    # --- 04 Schrippe -- la boulangere derriere le comptoir (regard a GAUCHE) ---
    # « Ein was? Hier heißt das Schrippe, junger Mann! » : la main « quoi ? ».
    ("04-schrippe", 4):
        "Her hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « Ein was? » it comes up to "
        "the height of her chest, palm up and open, fingers spread, the hand of what did you say, and it stays "
        "there, open, while she corrects him.",
    # « Ein Berliner? In Berlin? Nee. Das ist ein Pfannkuchen. » : le balayage du « nee ».
    ("04-schrippe", 8):
        "Her hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « Nee » it rises to chest "
        "height, palm down and flat, and makes one short sweep a few centimetres towards the left edge of the "
        "picture, the dismissal, then stays there, palm down.",
    # « Zwei Euro zehn. Und die Schlange wartet! » : la paume ouverte pour l'argent.
    ("04-schrippe", 17):
        "Her hand nearer the right edge of the picture stays resting flat on the glass top of the counter, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on the price it comes forward "
        "over the counter towards the left edge of the picture, palm up and open, cupped for the coins, and it "
        "stays held out there.",
    # --- 04 Schrippe -- Anna dans la file (regard a DROITE, Mark) ---
    # « Entschuldigung… Sind Sie nicht der Mann vom Flughafen? » : l'hesitation.
    ("04-schrippe", 10):
        "Her hand nearer the left edge of the picture stays on the strap of her canvas bag at her shoulder, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « Entschuldigung » it rises "
        "to her collarbone and rests there, fingers together, the hesitation before a question, and it stays "
        "there while she asks.",
    # « Und jetzt lernen Sie Berlinerisch. » : l'index qui dessine un cercle, « tout ca ».
    ("04-schrippe", 12):
        "Her hand nearer the left edge of the picture stays on the strap of her canvas bag at her shoulder, "
        "exactly as in the image, for the whole shot. Only her other hand moves: as she speaks it rises to chest "
        "height and its index finger draws one slow circle in the air, taking in the whole shop, then the hand "
        "stays there, the finger still up.",
    # « Schrippe, Brötchen, Semmel. Drei Wörter, ein Brot. » : elle compte trois.
    ("04-schrippe", 14):
        "Her hand nearer the left edge of the picture stays on the strap of her canvas bag at her shoulder, "
        "exactly as in the image, for the whole shot. Only her other hand moves: it rises in front of her chest "
        "and counts the three words, the thumb, then the index finger, then the middle finger coming up one "
        "after the other, and the three fingers stay up while she finishes.",
    # « Weil Berliner Menschen sind. Zum Beispiel ich. » : la main sur le coeur.
    ("04-schrippe", 16):
        "Her hand nearer the left edge of the picture stays on the strap of her canvas bag at her shoulder, "
        "exactly as in the image, for the whole shot. Only her other hand moves: on « ich » it rises to her "
        "chest and lays itself flat over her heart, on the cream knit of her sweater, and it stays there, warm "
        "and still.",
    # --- 05 Pfand -- le voisin sur son banc (regard a DROITE, Mark) ---
    # « Halt! Das ist doch Pfand! » : la main plate du « stop ».
    ("05-pfand", 4):
        "His hand nearer the left edge of the picture stays closed round the neck of his brown bottle, resting "
        "low in his lap, exactly as in the image, for the whole shot. Only his other hand moves: on « Halt! » it "
        "comes up fast to the height of his shoulder, flat, palm out towards the right edge of the picture, the "
        "stop, and it stays there while he speaks.",
    # « Fünfundzwanzig Cent. Für die Flasche. Die bringen Sie zurück. » : la piece.
    ("05-pfand", 6):
        "His hand nearer the left edge of the picture stays closed round the neck of his brown bottle, resting "
        "low in his lap, exactly as in the image, for the whole shot. Only his other hand moves: on the number it "
        "comes up to chest height with the thumb and the index finger pressed together, the sign of a coin, and "
        "it stays there while he explains.",
    # « Flaschen, Dosen – fast alle haben Pfand. » : l'index sur l'etiquette.
    ("05-pfand", 8):
        "His hand nearer the left edge of the picture stays closed round the neck of his brown bottle, resting "
        "low in his lap, exactly as in the image, for the whole shot. Only his other hand moves: as he speaks it "
        "comes across and lays its index finger on the plain label of that bottle, and it stays there, pointing "
        "at the label.",
    # « Richtig so. Die holt jemand. Jetzt sind Sie ein Berliner. » : la tape sur l'air.
    ("05-pfand", 18):
        "His hand nearer the left edge of the picture stays closed round the neck of his brown bottle, resting "
        "low in his lap, exactly as in the image, for the whole shot. Only his other hand moves: on « Richtig so » "
        "it rises, palm down, to the height of his chest and gives one slow pat on the air, approval, then stays "
        "there, palm down and calm.",
    # --- 05 Pfand -- Mark au bac (regard a GAUCHE, le voisin) ---
    # « Pfand? Was ist Pfand? » : la main ouverte de la question, haut.
    ("05-pfand", 5):
        "His hand nearer the left edge of the picture stays where it is, holding the empty bottle above the "
        "mouth of the orange bin, exactly as in the image, for the whole shot. Only his other hand moves: on "
        "« Pfand? » it rises to the height of his shoulder, palm up and open, the open hand of a question, and it "
        "stays there.",
    # « Fünfundzwanzig Cent? Für eine leere Flasche? » : l'index sur la bouteille.
    ("05-pfand", 7):
        "His hand nearer the left edge of the picture stays where it is, holding the empty bottle above the "
        "mouth of the orange bin, exactly as in the image, for the whole shot. Only his other hand moves: on "
        "« Flasche » it comes up and its index finger points at the empty bottle in his other hand, from a hand's "
        "width away, and it stays pointing at it.",
    # --- 05 Pfand -- Mark a l'automate (regard a GAUCHE, la machine) ---
    # « Nein? Warum nicht? » : les deux mains encadrent la bouteille refusee.
    ("05-pfand", 13):
        "His hand nearer the left edge of the picture stays closed round the refused bottle at the height of his "
        "chest, exactly as in the image, for the whole shot. Only his other hand moves: on « Warum » it comes up "
        "beside the bottle, palm up, open, fingers spread, so that the two hands frame the bottle, and it stays "
        "there.",
    # « Zwei Euro vierzig. Für Müll! » : la main a plat sur le coeur, ravi.
    ("05-pfand", 15):
        "His hand nearer the left edge of the picture stays closed round the small white slip at the height of "
        "his chest, exactly as in the image, for the whole shot. Only his other hand moves: on « Müll » it comes "
        "up and lays itself flat on his chest, over his heart, the delight, and it stays there.",
    # --- 05 Pfand -- Mark au bac, le soir, mains libres (regard a GAUCHE) ---
    # « Ein Berliner? Oder ein Pfannkuchen? » : le beignet invisible, en riant.
    ("05-pfand", 19):
        "His hand nearer the left edge of the picture stays resting on the grey post of the street lamp, exactly "
        "as in the image, for the whole shot. Only his other hand moves: with the laugh it comes up in front of "
        "his chest, the thumb and the index finger a few centimetres apart, the size of a pastry, and it stays "
        "there holding the air.",
}

# (scene, plan, locuteur, pronoms, cote, fond, cle BORD, emotion, parole, apres)
PLANS = [
    # ================= 04 SCHRIPPE =================
    ("04-schrippe", 3, "mark", IL, "right", BAECKEREI, "mark",
     "It is Saturday morning in his own neighbourhood and he is hungry and in a good mood: he knows this word, "
     "this is going to be easy.",
     "He says good morning and orders in one short, cheerful sentence."),
    ("04-schrippe", 4, "baeckerin", ELLE, "left", BAECKEREI, "baeckerin",
     "Berlin to the bone: brisk, loud, and fond of correcting newcomers. This is her first line and she sets the "
     "tone of the shop with it.",
     "She repeats his word as a question, then corrects him in one firm sentence, her eyebrows rising on the "
     "word she insists on."),
    ("04-schrippe", 5, "mark", IL, "right", BAECKEREI, "mark",
     "He takes the correction with good humour and tries the new word out loud, pleased with himself, then "
     "orders the second thing with complete confidence.",
     "He repeats the new word carefully, agrees, and adds one more order."),
    ("04-schrippe", 7, "mark", IL, "right", BAECKEREI, "mark",
     "He has just been handed something round and sugared instead of the flat thing he expected, and he is "
     "delighted to recognise it: he knows this one.",
     "He protests in two short sentences, half laughing, naming what he sees."),
    ("04-schrippe", 8, "baeckerin", ELLE, "left", BAECKEREI, "baeckerin",
     "Deadpan, and this is as dry as she gets: in her shop that word is simply wrong, and she says so without "
     "raising her voice.",
     "She repeats his word as a question twice, says a flat Berlin no, then states the right word, matter of "
     "fact."),
    ("04-schrippe", 10, "anna", ELLE, "right", BAECKEREI, "anna",
     "She has been looking at the back of his head for a minute and she is almost sure. Warm, unhurried, and a "
     "touch hesitant: she is about to speak to a stranger who may not be one.",
     "She says excuse me, then asks one careful question, her eyebrows rising at the end of it."),
    ("04-schrippe", 11, "mark", IL, "left", BAECKEREI, "mark",
     "He has turned round and he recognises her at once, out of uniform, in the middle of his bakery: a real, "
     "glad surprise.",
     "He says yes with a laugh and answers in one short glad sentence."),
    ("04-schrippe", 12, "anna", ELLE, "right", BAECKEREI, "anna",
     "Her dry humour, gone almost before it appears: she has heard the whole exchange at the counter and she is "
     "amused, on his side, never mocking.",
     "She says one short dry sentence, a half-smile arriving on the last word."),
    ("04-schrippe", 13, "mark", IL, "left", BAECKEREI, "mark",
     "He laughs at himself: all he wanted was a roll, and it has become a language lesson.",
     "He repeats her word as a question, then says one short sentence through a laugh."),
    ("04-schrippe", 14, "anna", ELLE, "right", BAECKEREI, "anna",
     "She explains rather than instructs: calmly, with pleasure, the way she once explained the S-Bahn.",
     "She names three words one after the other, then adds one short sentence."),
    ("04-schrippe", 15, "mark", IL, "left", BAECKEREI, "mark",
     "Curious and willing, as always: he asks rather than guesses, and he wants to understand the pastry.",
     "He asks one short question, his eyebrows rising on it."),
    ("04-schrippe", 16, "anna", ELLE, "right", BAECKEREI, "anna",
     "The warmest moment of the episode, and it stays sober: a plain fact about herself, said with a quiet "
     "smile, nothing more.",
     "She answers in one sentence, then adds two words about herself."),
    ("04-schrippe", 17, "baeckerin", ELLE, "left", BAECKEREI, "baeckerin",
     "She has had enough of the chatting at her counter: brisk, loud, and still fond underneath. She brings the "
     "shop back to business.",
     "She states the price, then tells him to hurry in one short sentence, her chin coming up on it."),
    # ================= 05 PFAND =================
    ("05-pfand", 4, "nachbar", IL, "right", SPAETI, "nachbar",
     "He has just seen a perfectly good bottle about to go into a litter bin, and he cannot let it happen. Sharp "
     "at first, the voice of a neighbour who stops you because somebody has to.",
     "He calls one sharp word, then says one short sentence, firm and a little indignant."),
    ("05-pfand", 5, "mark", IL, "left", SPAETI, "mark",
     "Caught mid-gesture with the bottle over the bin, and completely puzzled: the word is brand new to him.",
     "He repeats the word as a question, then asks what it means, his eyebrows up."),
    ("05-pfand", 6, "nachbar", IL, "right", SPAETI, "nachbar",
     "The sharpness has gone out of him already, and it shows before he speaks: he explains, plainly, like a "
     "neighbour who has done this a thousand times.",
     "He names the amount, says what it is for, and tells him what to do, in three short pieces."),
    ("05-pfand", 7, "mark", IL, "left", SPAETI, "mark",
     "Open disbelief, and he finds it funny: money for an empty bottle.",
     "He repeats the amount as a question, then asks a second disbelieving question, half laughing."),
    ("05-pfand", 8, "nachbar", IL, "right", SPAETI, "nachbar",
     "Patient now, almost pleased to be asked: this is the city he knows, and he is handing it over.",
     "He lists two things, then states the rule in one plain sentence."),
    ("05-pfand", 13, "mark", IL, "left", AUTOMAT, "mark-automat",
     "Alone at the deposit machine, one bottle has just rolled back out to him, and he takes it personally, "
     "amused: he is talking to a machine and he knows it.",
     "He says a short no as a question to the machine, then asks it why."),
    ("05-pfand", 15, "mark", IL, "left", AUTOMAT, "mark-automat",
     "Pure delight: the slip in his hand says real money, and a week ago all of this was rubbish to him.",
     "He reads the amount aloud, then says two words with a laugh."),
    ("05-pfand", 18, "nachbar", IL, "right", SPAETI, "nachbar",
     "By now he likes this young newcomer, and it is plain on his face: approval, dry and warm at once. He has "
     "watched him set the bottle down beside the bin instead of in it.",
     "He says two words of approval, explains in one short sentence, then states the verdict, deadpan."),
    ("05-pfand", 19, "mark", IL, "left", SPAETI, "mark",
     "He has been called a Berliner and the word makes him laugh: last week it was a pastry.",
     "He repeats the word as a question, then asks a second one through a laugh."),
]

# Ce que le visage fait une fois la replique finie : l'INTENTION de la queue.
APRES = {
    ("04-schrippe", 3): "waits for his roll, cheerful, his mouth closed",
    ("04-schrippe", 4): "waits to see if the lesson has landed, her chin up, her mouth closed",
    ("04-schrippe", 5): "waits, pleased with himself, his mouth closed",
    ("04-schrippe", 7): "keeps the amused grin and waits for her answer, his mouth closed",
    ("04-schrippe", 8): "holds a flat, satisfied look, her mouth closed, the matter settled",
    ("04-schrippe", 10): "waits for his answer, hopeful and a touch embarrassed, her mouth closed",
    ("04-schrippe", 11): "keeps a wide glad smile that reaches his eyes, his mouth closed",
    ("04-schrippe", 12): "keeps the half-smile and waits, amused, her mouth closed",
    ("04-schrippe", 13): "keeps laughing quietly, his mouth closed, his eyes on her",
    ("04-schrippe", 14): "waits to see if he has followed, calm and friendly, her mouth closed",
    ("04-schrippe", 15): "waits for the answer, curious, his mouth closed",
    ("04-schrippe", 16): "keeps a quiet warm smile, her mouth closed, her eyes steady",
    ("04-schrippe", 17): "waits for the money with one eyebrow up, her mouth closed",
    ("05-pfand", 4): "keeps a stern, expectant look, his mouth closed, waiting to see what he does",
    ("05-pfand", 5): "waits for the answer, puzzled and friendly, his mouth closed",
    ("05-pfand", 6): "waits to see if it has been understood, patient, his mouth closed",
    ("05-pfand", 7): "keeps the disbelieving grin and waits, his mouth closed",
    ("05-pfand", 8): "settles into a calm look, his mouth closed, the lesson given",
    ("05-pfand", 13): "frowns at the machine, amused, his mouth closed, waiting as if it might answer",
    ("05-pfand", 15): "keeps a wide delighted smile that reaches his eyes, his mouth closed",
    ("05-pfand", 18): "keeps a slow, approving half-smile, his mouth closed, his eyes steady on him",
    ("05-pfand", 19): "keeps laughing, his mouth closed, the whole week in that laugh",
}


def ecrire(sc, n, loc, P, cote, fond, bord, emotion, parole):
    f = lambda s: s.format(plan=MOYEN[0], cadrage=MOYEN[1], cote=cote, **P)
    if fond is AUTOMAT:
        # La machine est DANS l'image, a son bord : on la regarde, elle, pas un point.
        regard = (" %s speaks towards the round dark opening of the machine at the %s edge of the picture."
                  % (P["He"], cote))
    else:
        regard = (" %s speaks towards a point just beyond the %s edge of the picture, level with %s own eyes."
                  % (P["He"], cote, P["his"]))
    blocs = [f(CAMERA), emotion, parole + regard + " Let %s face follow the voice." % P["his"]]
    blocs.append(GESTES[(sc, n)])
    blocs.append(TENUE_PLAN.get((sc, n)) or TENUE[(sc, loc)])
    blocs.append(BORD[(sc, bord, cote)])
    blocs.append("Finally %s stops speaking and %s. %s blinks, %s breathes, and %s holds that expression "
                 "the whole time %s waits." % (P["he"], APRES[(sc, n)], P["He"], P["he"], P["he"], P["he"]))
    blocs += [f(fond), f(FIN)]
    d = os.path.join(RACINE, "video", "episode-" + sc, "_essai-avatar", "prompts")
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "plan%02d.txt" % n), "w", encoding="utf-8").write("\n\n".join(blocs) + "\n")


if __name__ == "__main__":
    for x in PLANS:
        ecrire(*x)
    print("%d prompts ecrits" % len(PLANS))
