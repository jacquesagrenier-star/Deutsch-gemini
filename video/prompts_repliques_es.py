# -*- coding: utf-8 -*-
"""Les prompts des repliques de la serie espagnole (es-01 a es-04), ecrits d'un seul gabarit.

    python video/prompts_repliques_es.py          -> _essai-avatar/prompts/planNN.txt

LE GABARIT EST CELUI DE L'EPISODE 3 (plan 15, apres les lecons du 16 sept.) :
camera decrite comme un ETAT (camera-qui-bouge), emotion situee dans la COURBE
du personnage, un vrai VERBE DE PAROLE et le cote ou se trouve l'autre,
« Let ... face follow the voice » (pas de secondes), l'etat des MAINS quand elles
sont dans le cadre (objet-qui-se-materialise) -- et rien sur elles quand elles
n'y sont pas --, une INTENTION apres la parole (fin-sans-intention), le fond
decrit en positif (garde-negative), et le cadre qui tient jusqu'au bout.

LES COTES SUIVENT LA GEOGRAPHIE DES FEUILLES (A-TOURNER.txt) :
  es-01  Mark regarde vers la GAUCHE (Ana), Ana vers la DROITE (Mark)
  es-02  Mark regarde vers la DROITE (la voisine), la voisine vers la GAUCHE
  es-03  Mark vers la DROITE (le serveur derriere le comptoir, Ana a sa droite) ;
         le serveur et Ana vers la GAUCHE
  es-04  Mark vers la DROITE (Lucia, puis le directeur dans l'ascenseur) ;
         Lucia et le directeur vers la GAUCHE
Ce fichier est la source ; les planNN.txt se regenerent, ils ne s'editent pas.

⚠️ es-03 et es-04 ont DEUX hommes chacun (Mark et le serveur ; Mark et le
   directeur), et Mark change de tenue au plan 17 d'es-03 : la tenue et le bord
   ne peuvent plus se lire sur (scene, il/elle) seul. D'ou TENUE_PLAN et
   BORD_PLAN, par (scene, plan), lus AVANT les tables generales. Les scenes
   es-01 et es-02 n'y ont aucune entree de bord : leurs prompts ne changent pas.
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAMERA = ("A static {plan} holds on {him}, {cadrage}. The camera is locked on a tripod and stays there for the whole "
          "shot: the same lens, the same height, the same distance. Keep {his} position and {his} distance from "
          "the camera exactly as in the image.")
FIN = ("The framing holds to the very end: in the last frame {he} is the same size and in the same place in "
       "the picture as in the first.")
MOYEN = ("medium shot", "seen from the hips up")
SERRE = ("close shot", "head and shoulders")

HALL = ("Behind {him} the arrivals hall goes on, warm and soft and out of focus, its travellers small and far "
        "away, each continuing on their way. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
        "frame and stay there for the whole shot.")
RUE = ("Behind {him} the sunny street stays quiet, soft and out of focus. {His} eyes rest on a fixed point just "
       "beyond the {cote} edge of the frame and stay there for the whole shot.")
# es-03 : le bar. Le fond est le mur carrele et les tasses, flous ; rien n'y bouge.
BAR = ("Behind {him} the white tiled wall of the bar and its shelves of white cups stay soft and out of focus, "
       "still, in the warm morning light. {His} eyes rest on a fixed point just beyond the {cote} edge of the "
       "frame and stay there for the whole shot.")
# es-04 : le bureau. Les fenetres et les bureaux blancs, flous ; les ecrans restent eteints.
OFICINA = ("Behind {him} the bright open-plan office goes on, soft and out of focus, its white desks and tall "
           "windows still in the morning light, its monitors dark. {His} eyes rest on a fixed point just beyond "
           "the {cote} edge of the frame and stay there for the whole shot.")
# es-04 : l'ascenseur. Une paroi d'acier brosse, et rien d'autre.
ASCENSOR = ("Behind {him} the back wall of the lift stays plain and still, brushed steel evenly lit from the "
            "ceiling. {His} eyes rest on a fixed point just beyond the {cote} edge of the frame and stay there "
            "for the whole shot.")

# Ce qu'on voit sur le haut du corps, du premier au dernier image (voir ecrire()).
TENUE = {
    ("es-01-llegada-madrid", "he"): "Across his chest we see only his grey jacket and his black T-shirt, plain "
                                    "and unmarked, from the first frame to the last.",
    ("es-01-llegada-madrid", "she"): "Across her chest we see only the beige trench coat, the plain grey knit of "
                                     "her sweater and the brown leather strap, from the first frame to the last.",
    ("es-02-el-carro", "he"): "Across his chest we see only his plain white T-shirt, from the first frame to the "
                              "last.",
    ("es-02-el-carro", "she"): "Across her chest we see only her navy coat and her plain white blouse, from the "
                               "first frame to the last.",
    # es-03 : Mark en pull gris (plans 3 a 14) ; le lundi (17) et le serveur passent par TENUE_PLAN.
    ("es-03-el-cafe", "he"): "Across his chest we see only his plain mid-grey knit sweater and the white collar "
                             "of his T-shirt, from the first frame to the last.",
    ("es-03-el-cafe", "she"): "Across her chest we see only her plain rust-coloured sweater and the brown leather "
                              "strap of her bag, from the first frame to the last.",
    # es-04 : Mark en chemise bleu clair et veste sombre (meme tenue qu'es-03 plan 17) ; le
    # directeur passe par TENUE_PLAN.
    ("es-04-tu-o-usted", "he"): "Across his chest we see only his plain light-blue shirt and his dark jacket, "
                                "open and unmarked, from the first frame to the last.",
    ("es-04-tu-o-usted", "she"): "Across her chest we see only her plain dark green blouse, from the first frame "
                                 "to the last.",
}

# ⚠️ L'ESPACE ENTRE LE PERSONNAGE ET LE BORD OU EST L'AUTRE (21 oct. 2026). es-02
#    plan 02 : « speaking to someone just off screen beyond the RIGHT edge » -- et
#    Kling a DESSINE ce quelqu'un, une silhouette fantome au bord droit au milieu
#    du plan. Remede de la garde negative : ne pas dire « personne n'entre », dire
#    ce qui occupe cet espace du debut a la fin. Cle : (scene, il/elle, cadre).
BORD = {
    ("es-01-llegada-madrid", "he", "medium shot"):
        "On the left of the picture, between him and the edge of the frame, the blurred beige shoulder in the "
        "foreground stays exactly as it is in the image, just as blurred, from the first frame to the last.",
    ("es-01-llegada-madrid", "he", "close shot"):
        "On the left of the picture, between him and the edge of the frame, the warm hall runs on, open and "
        "soft, from the first frame to the last.",
    ("es-01-llegada-madrid", "she", "medium shot"):
        "On the right of the picture, between her and the edge of the frame, the dark blurred shoulder in the "
        "foreground stays exactly as it is in the image, just as blurred, from the first frame to the last.",
    ("es-01-llegada-madrid", "she", "close shot"):
        "On the right of the picture, between her and the edge of the frame, the warm hall runs on, open and "
        "soft, from the first frame to the last.",
    ("es-02-el-carro", "he", "medium shot"):
        "On the right of the picture, between him and the edge of the frame, the sunny pavement and the ochre "
        "facade run on, open and quiet, from the first frame to the last.",
    ("es-02-el-carro", "she", "medium shot"):
        "On the left of the picture, between her and the edge of the frame, the top of her trolley and the sunny "
        "street run on, open and quiet, from the first frame to the last.",
    # es-03 : Mark a gauche du cadre, le comptoir file vers la droite (la vitrine des tostadas) ;
    # Ana a droite, le comptoir file vers la gauche (la machine a cafe, loin).
    ("es-03-el-cafe", "he", "medium shot"):
        "On the right of the picture, between him and the edge of the frame, the zinc counter and the glass case "
        "of toast run on, bright and empty, from the first frame to the last.",
    ("es-03-el-cafe", "she", "medium shot"):
        "On the left of the picture, between her and the edge of the frame, the zinc counter runs on towards the "
        "chrome coffee machine far behind it, bright and empty, from the first frame to the last.",
    # es-04 : Mark a gauche (les bureaux blancs et les fenetres a sa droite) ; Lucia a droite (la
    # cuisine et les bureaux a sa gauche).
    ("es-04-tu-o-usted", "he", "medium shot"):
        "On the right of the picture, between him and the edge of the frame, the white desks and the tall sunny "
        "windows run on, bright and open, from the first frame to the last.",
    ("es-04-tu-o-usted", "she", "medium shot"):
        "On the left of the picture, between her and the edge of the frame, the white desks and the small "
        "kitchenette run on, bright and open, from the first frame to the last.",
}
# Le bord d'UN plan, quand il ne suit pas le personnage principal de son sexe : le serveur
# (es-03) et le directeur (es-04) regardent vers la GAUCHE comme Ana et Lucia, pas comme Mark ;
# et l'ascenseur d'es-04 n'a pas le bord du bureau.
BORD_PLAN = {
    ("es-03-el-cafe", 4):
        "On the left of the picture, between him and the edge of the frame, the zinc counter and the chrome "
        "coffee machine run on, bright and still, from the first frame to the last.",
    ("es-03-el-cafe", 10):
        "On the left of the picture, between him and the edge of the frame, the zinc counter and the chrome "
        "coffee machine run on, bright and still, from the first frame to the last.",
    ("es-03-el-cafe", 18):
        "On the left of the picture, between him and the edge of the frame, the zinc counter and the chrome "
        "coffee machine run on, bright and still, from the first frame to the last.",
    ("es-04-tu-o-usted", 15):
        "On the right of the picture, between him and the edge of the frame, the brushed-steel wall of the lift "
        "runs on, plain and evenly lit, from the first frame to the last.",
    ("es-04-tu-o-usted", 17):
        "On the right of the picture, between him and the edge of the frame, the brushed-steel wall of the lift "
        "runs on, plain and evenly lit, from the first frame to the last.",
    ("es-04-tu-o-usted", 16):
        "On the left of the picture, between him and the edge of the frame, the brushed-steel wall of the lift "
        "runs on, plain and evenly lit, from the first frame to the last.",
    ("es-04-tu-o-usted", 18):
        "On the left of the picture, between him and the edge of the frame, the brushed-steel wall of the lift "
        "runs on, plain and evenly lit, from the first frame to the last.",
}

IL = {"he": "he", "him": "him", "his": "his", "He": "He", "His": "His"}
ELLE = {"he": "she", "him": "her", "his": "her", "He": "She", "His": "Her"}

# (scene, plan, pronoms, cadre, cote, fond, emotion, parole, mains (ou None), apres)
M1 = "His visible hand hangs low at his side, open and empty, exactly as in the image."
A1 = "Her hands stay at her sides, open and empty, exactly as in the image."
M2 = "His hand nearer the car stays resting on the box in the open boot, exactly as in the image."
M2B = ("His hand nearer the car stays resting on the box in the open boot, and his other arm stays "
       "relaxed, exactly as in the image.")
V2 = "Her hand stays on the black handle of her shopping trolley, exactly as in the image."

PLANS = [
    # ⚠️ L'AUTRE N'EST JAMAIS NOMME (21 oct. 2026). Les premiers prompts disaient
    #    « he greets an older lady », « asks her », « waiting for her answer » : Kling
    #    a dessine une tete au bas du cadre et Mark l'a regardee en baissant les yeux,
    #    MEME avec le bord rempli (BORD). Meme mecanisme qu'objet-qui-se-materialise :
    #    ce que le prompt nomme, le modele le fabrique. Le regard se donne par un POINT
    #    a hauteur des yeux (voir ecrire()).
    ('es-01-llegada-madrid', 5, IL, MOYEN, 'left', HALL,
     'He has just come off a long flight from Mexico: polite, a little tired, and unsure of himself in a place that is still new to him.',
     'He asks one short, polite question, his eyebrows rising with it.',
     M1,
     'listens without speaking, his mouth closed, waiting for the answer'),
    ('es-01-llegada-madrid', 6, ELLE, MOYEN, 'right', HALL,
     'She is a traveller herself, waiting for her own suitcase, and she is glad to help: open, friendly, curious.',
     'She answers, then asks one friendly question.',
     A1,
     'keeps her friendly half-smile and waits for the answer, interested'),
    ('es-01-llegada-madrid', 8, IL, SERRE, 'left', HALL,
     'The tiredness lifts a little: he is pleased to be asked, and a first smile comes into his eyes.',
     'He answers in two short sentences.',
     None,
     'keeps the small smile and listens, his mouth closed'),
    ('es-01-llegada-madrid', 9, ELLE, MOYEN, 'right', HALL,
     'She is genuinely delighted: a newcomer to her city.',
     'She says a warm welcome, then asks one short question.',
     A1,
     'smiles and waits for the answer'),
    ('es-01-llegada-madrid', 10, IL, MOYEN, 'left', HALL,
     'He is proud of this new job and a little nervous about it, and both show.',
     'He answers in two short sentences.',
     M1,
     'keeps a half-smile that reaches his eyes and listens'),
    ('es-01-llegada-madrid', 11, ELLE, MOYEN, 'right', HALL,
     'She is pleased by the news, and curious.',
     'She says how nice that is, then asks one short question.',
     A1,
     'waits for the answer, her eyebrows still slightly raised'),
    ('es-01-llegada-madrid', 12, IL, SERRE, 'left', HALL,
     "The small smile of the picture fades as a worry crosses his face: for him, nine o'clock at night is already late.",
     'He answers, then asks a short worried question; his eyebrows rise on the last word.',
     None,
     'waits for the answer, his eyebrows still raised, his mouth closed'),
    ('es-01-llegada-madrid', 13, ELLE, SERRE, 'right', HALL,
     "This is the funny moment of the episode: she cannot believe anyone thinks nine o'clock is late, and she is amused, never mocking.",
     'She repeats the word « late » in amused disbelief, then explains with a grin.',
     None,
     'keeps a broad, amused smile, her mouth closed'),
    ('es-01-llegada-madrid', 14, IL, MOYEN, 'left', HALL,
     'He is reassured and hopeful again.',
     'He asks one short question.',
     M1,
     'listens without speaking, his mouth closed'),
    ('es-01-llegada-madrid', 15, ELLE, MOYEN, 'right', HALL,
     'She is easy and reassuring: of course there is a metro.',
     'She answers in two short sentences.',
     A1,
     'smiles and waits'),
    ('es-01-llegada-madrid', 16, IL, SERRE, 'left', HALL,
     'He is warmly grateful: his first evening in Madrid has just become easier.',
     'He says a warm thank-you in one short sentence.',
     None,
     'keeps a warm smile that reaches his eyes, his mouth closed'),
    ('es-01-llegada-madrid', 17, ELLE, SERRE, 'right', HALL,
     'She is warm: she wishes a newcomer well and means it.',
     'She answers, then says « good luck » in two short sentences.',
     None,
     'keeps a warm, open smile, her mouth closed, the goodbye already in her eyes'),
    ('es-02-el-carro', 2, IL, MOYEN, 'right', RUE,
     'It is moving day and he is in a good mood: polite, cheerful, sure of his Spanish.',
     'He says good morning and asks one short question.',
     M2B,
     'listens without speaking, his mouth closed, friendly, waiting for the answer'),
    ('es-02-el-carro', 3, ELLE, MOYEN, 'left', RUE,
     'She recognises a Mexican accent from a single word, and she is delighted: it is someone from home.',
     'She repeats one word, then says warmly where she is from.',
     V2,
     'keeps a delighted smile, her mouth closed, her eyes full of affection'),
    ('es-02-el-carro', 5, IL, MOYEN, 'right', RUE,
     'He is surprised and happy to meet a fellow Mexican here, and curious.',
     'He asks two short questions, his eyebrows rising.',
     M2,
     'waits for the answer, smiling, his mouth closed'),
    ('es-02-el-carro', 6, ELLE, MOYEN, 'left', RUE,
     'She teaches the Madrid words the way someone once taught her: kindly, a little amused.',
     'She explains in two short sentences.',
     V2,
     'keeps a small encouraging smile, her mouth closed, waiting to see if it is understood'),
    ('es-02-el-carro', 7, IL, MOYEN, 'right', RUE,
     'He concentrates hard on the new words, like a student repeating after the teacher.',
     'He repeats the new words carefully, then adds one short word of agreement.',
     M2,
     'looks pleased with himself, his mouth closed'),
    ('es-02-el-carro', 8, ELLE, MOYEN, 'left', RUE,
     'She is proud of her pupil, and she laughs at herself: it took her a year to say that word.',
     'She says « very good », then says one short thing about herself with a small laugh.',
     V2,
     'her mouth closes into a warm smile that stays'),
    ('es-02-el-carro', 10, ELLE, MOYEN, 'left', RUE,
     'Now she is practical, a neighbour who knows the street: the car cannot stay where it is.',
     'She asks one short question and adds one short sentence.',
     V2,
     'waits for the answer, one eyebrow slightly raised, her mouth closed'),
    ('es-02-el-carro', 11, IL, MOYEN, 'right', RUE,
     'He is completely sure of himself, and the audience knows better.',
     'He answers in one short, confident sentence.',
     M2,
     'keeps a confident smile, his mouth closed'),
    ('es-02-el-carro', 12, ELLE, MOYEN, 'left', RUE,
     'She knows exactly what « ahorita » means, because she is Mexican too: knowing, teasing, fond.',
     'She repeats one word as a question, then says she knows better; one eyebrow rises as she speaks.',
     V2,
     'keeps a knowing half-smile, her mouth closed, her eyes steady'),
    ('es-02-el-carro', 13, IL, MOYEN, 'right', RUE,
     'Caught out, he hesitates, and a guilty smile spreads across his face.',
     'He answers slowly, hesitating in the middle.',
     M2,
     'keeps the guilty smile, his mouth closed'),
    ('es-02-el-carro', 14, ELLE, MOYEN, 'left', RUE,
     'She bursts out laughing: she knew it.',
     'She laughs on the first words, then says one short sentence through her laughter.',
     V2,
     'her mouth closes into a broad smile that stays, her eyes still laughing'),
    ('es-02-el-carro', 15, IL, MOYEN, 'right', RUE,
     'He laughs too: two Mexicans in Madrid sharing the same joke.',
     'He agrees in one word, with a short laugh.',
     M2,
     'his mouth closes into a wide smile that stays'),
    # ------------------------------------------------------------------
    # es-03 EL CAFE (22 oct. 2026). Mark au comptoir, en pull gris, regarde vers la
    # DROITE (le serveur derriere le comptoir, Ana a cote de lui). Le serveur et Ana
    # regardent vers la GAUCHE. Les mains : toutes dans GESTES, une par replique.
    # ------------------------------------------------------------------
    ('es-03-el-cafe', 3, IL, MOYEN, 'right', BAR,
     'It is his first order in a Madrid bar and he is sure of his Spanish: polite, cheerful, hungry.',
     'He says good morning and asks for a coffee in one polite question.',
     None,
     'listens without speaking, his mouth closed, friendly, waiting for the coffee'),
    ('es-03-el-cafe', 4, IL, MOYEN, 'left', BAR,
     'A Madrid waiter who has heard everything: the word « regalar » makes him laugh out loud, and the laugh is kind.',
     'He repeats one word in disbelief, laughs, then says one short sentence through the laugh.',
     None,
     'his mouth closes into a broad amused grin that stays, his eyes still laughing'),
    ('es-03-el-cafe', 6, ELLE, MOYEN, 'left', BAR,
     'She has just recognised the young man from the airport, and she is genuinely delighted by the coincidence: warm, open, surprised.',
     'She exclaims in surprise, names where she knows him from, then asks one friendly question.',
     None,
     'keeps a warm, surprised smile, her mouth closed, waiting for the answer'),
    ('es-03-el-cafe', 7, IL, MOYEN, 'right', BAR,
     'The embarrassment of the waiter has gone in an instant: here is the one person he knows in Madrid, and his face lights up.',
     'He greets her, says what a surprise it is, then asks one short question.',
     None,
     'keeps a bright smile that reaches his eyes and waits for the answer, his mouth closed'),
    ('es-03-el-cafe', 8, ELLE, MOYEN, 'left', BAR,
     'She explains the Madrid way of ordering the way she once explained the airport: kindly, clearly, with a touch of amusement.',
     'She answers, then says the Madrid formula slowly and clearly.',
     None,
     'keeps an encouraging half-smile, her mouth closed, waiting to see if he tries it'),
    ('es-03-el-cafe', 9, IL, MOYEN, 'right', BAR,
     'He repeats the formula like a pupil, carefully, a little solemn, and pleased with himself before he has finished.',
     'He asks the question again in the new words, slowly and carefully.',
     None,
     'looks pleased with himself and waits, his mouth closed'),
    ('es-03-el-cafe', 10, IL, MOYEN, 'left', BAR,
     'Now the waiter approves: the newcomer has learned. Then comes the question of the trade, three coffees.',
     'He says « that is it » with a nod, then asks the three-choice question briskly.',
     None,
     'waits for the answer with one eyebrow up, his mouth closed'),
    ('es-03-el-cafe', 11, IL, MOYEN, 'right', BAR,
     'A word that is new to him: he is lost for a second, and instead of guessing he asks -- that is who he is.',
     'He repeats the unknown word as a question, then asks what it is.',
     None,
     'waits for the answer, his eyebrows still raised, his mouth closed'),
    ('es-03-el-cafe', 13, ELLE, MOYEN, 'left', BAR,
     'She orders for herself the way she does every Sunday: simple, sure, unhurried.',
     'She states her order in one clear sentence.',
     None,
     'keeps an easy smile and waits, her mouth closed'),
    ('es-03-el-cafe', 14, IL, MOYEN, 'right', BAR,
     'Relieved: he can simply copy her, and he knows it is a little funny.',
     'He answers with a short hesitation in the middle, then asks for the same.',
     None,
     'keeps a sheepish half-smile that reaches his eyes, his mouth closed'),
    ('es-03-el-cafe', 17, IL, MOYEN, 'right', BAR,
     'Monday morning, in his work shirt and jacket: he walks in knowing the formula, and the confidence shows before he speaks.',
     'He says good morning and asks for his coffee in the Madrid formula, sure of every word.',
     None,
     'keeps a quiet, confident smile and waits, his mouth closed'),
    ('es-03-el-cafe', 18, IL, MOYEN, 'left', BAR,
     'The waiter is proud of his customer, the way a coach is proud: warm, loud, pleased.',
     'He says « very good » with a grin, then calls the order out towards the machine in one short sentence.',
     None,
     'his mouth closes into a wide satisfied grin that stays'),
    # ------------------------------------------------------------------
    # es-04 TU O USTED (22 oct. 2026). Mark au bureau, chemise bleu clair et veste
    # sombre, regarde vers la DROITE (Lucia) ; Lucia vers la GAUCHE. Dans l'ascenseur
    # (15 a 18) : Mark a gauche regarde vers la DROITE, le directeur vers la GAUCHE.
    # ------------------------------------------------------------------
    ('es-04-tu-o-usted', 3, ELLE, MOYEN, 'left', OFICINA,
     'She is the colleague who welcomes the new one: direct, warm, already on first-name terms.',
     'She greets him, guesses his name as a question, says her own, then says welcome.',
     None,
     'keeps an open, friendly smile and waits for the answer, her mouth closed'),
    ('es-04-tu-o-usted', 4, IL, MOYEN, 'right', OFICINA,
     'His first day, and his Mexican manners come out in full: formal, polite, a little stiff, eager to do everything right.',
     'He says how pleased he is to meet her, then asks formally how she is.',
     None,
     'listens without speaking, his mouth closed, polite and attentive'),
    ('es-04-tu-o-usted', 5, ELLE, MOYEN, 'left', OFICINA,
     "« Madam » at thirty-two: it makes her laugh, and the laugh is kind. She sets him straight the Madrid way.",
     'She repeats two words in amused disbelief, laughs, then tells him warmly how things are done here.',
     None,
     'her mouth closes into a wide amused smile that stays, her eyes still laughing'),
    ('es-04-tu-o-usted', 7, IL, MOYEN, 'right', OFICINA,
     'He tries the familiar form for the first time, and the first name feels strange in his mouth: hesitant, willing, a little shy.',
     'He agrees in one word, then asks how she is in the familiar form, pausing before her name.',
     None,
     'waits for the answer with a shy half-smile, his mouth closed'),
    ('es-04-tu-o-usted', 8, ELLE, MOYEN, 'left', OFICINA,
     'He got it: she is pleased, and already moving on to the next thing.',
     'She says « very good », then tells him to come and meet the team.',
     None,
     'keeps a bright smile and waits, her mouth closed, ready to go'),
    ('es-04-tu-o-usted', 10, IL, MOYEN, 'right', OFICINA,
     'Coffee break: he is more at ease now, and he asks the whole group a polite question, in the plural he grew up with.',
     'He asks the group one short polite question.',
     None,
     'waits for the answer, friendly, his mouth closed'),
    ('es-04-tu-o-usted', 11, ELLE, MOYEN, 'left', OFICINA,
     'Second lesson of the day, and she enjoys it: teasing, warm, the teacher of the group.',
     'She repeats one word as a question, says the Madrid word, then says the whole question the Madrid way.',
     None,
     'keeps a teasing smile, her mouth closed, her eyebrows up, waiting for him to try'),
    ('es-04-tu-o-usted', 12, IL, MOYEN, 'right', OFICINA,
     'He repeats the new form slowly, and it dawns on him as he speaks: the verb changes too. Dismay and amusement at once.',
     'He repeats the two words with a pause between them, then exclaims about the verb.',
     None,
     'keeps a half-dismayed, half-amused smile, his mouth closed'),
    ('es-04-tu-o-usted', 13, ELLE, MOYEN, 'left', OFICINA,
     'Dry, kind consolation: the Canaries say it his way. This is her driest moment, and the warmth is in her eyes.',
     'She agrees in one word, then reassures him in one short sentence, deadpan.',
     None,
     'keeps a deadpan half-smile, her mouth closed, her eyes warm'),
    ('es-04-tu-o-usted', 15, IL, MOYEN, 'right', ASCENSOR,
     'Two o\'clock, going down for lunch, proud of the morning\'s lesson: he greets the gentleman in the lift the new familiar way, bright and easy.',
     'He greets cheerfully, then asks how the other is, in the familiar form.',
     None,
     'keeps his cheerful smile and waits for the answer, his mouth closed'),
    ('es-04-tu-o-usted', 16, IL, MOYEN, 'left', ASCENSOR,
     'An elderly gentleman of the old school: the familiar form from a stranger stops him. Stern and kind at once, he corrects, and he means it.',
     'He repeats one word as a question, then says, slowly and clearly, that the formal form is the one to use.',
     None,
     'holds a steady, stern look, his mouth closed, one eyebrow still up, waiting to be obeyed'),
    ('es-04-tu-o-usted', 17, IL, MOYEN, 'right', ASCENSOR,
     'Caught out for the third time today, and he knows it: small, apologetic, and already smiling at himself.',
     'He apologises in one word, then asks again, formally, how the gentleman is.',
     None,
     'keeps an apologetic smile that reaches his eyes, his mouth closed'),
    ('es-04-tu-o-usted', 18, IL, MOYEN, 'left', ASCENSOR,
     'The hardness has gone out of him: the young man corrected himself, and the elder is pleased. Formal, warm, a welcome.',
     'He answers that he is well, thanks him, then says welcome to the company.',
     None,
     'keeps a warm, dignified smile, his mouth closed, and waits'),
]


# ⚠️ UN GESTE DIFFERENT PAR REPLIQUE D'ANA (22 oct. 2026). Jacques : « dans
#    l'aeroport, Anna fait toujours le meme geste avec les mains ; le geste est
#    bien, mais repetitif, ca fait machinal -- les Espagnols parlent beaucoup avec
#    leurs mains ». Ses quatre plans moyens ouvraient tous les deux mains. Chaque
#    geste est ecrit par sa GEOMETRIE (nom-du-geste), avec son amplitude
#    (verbe-sans-plafond), et TENU jusqu'a la fin (geste-qui-revient). Le cote se
#    dit par l'image (cote-du-corps).
GESTES = {
    # Relu par Fable le 22 oct. : pas de tapis nomme (objet hors champ, du cote ou
    # les fantomes apparaissaient), a hauteur de POITRINE (a la taille, la main
    # entrait dans le flou de l'epaule), l'autre main immobile comme dans l'image.
    ("es-01-llegada-madrid", 6):
        "As she says the first words, her forearm nearer the right edge of the picture comes up from the elbow "
        "until the hand is level with her chest, palm open and fingers together, turned towards the right edge "
        "of the picture, and it stays there while she speaks, well short of the dark shoulder; her other hand "
        "hangs relaxed at her side, exactly as in the image.",
    # La main sur le REVERS du trench : la phrase TENUE de ce plan le dit aussi
    # (sinon « on ne voit que le trench » contredisait la main sur la poitrine).
    ("es-01-llegada-madrid", 9):
        # 1re prise (22 oct.) : elle a joint les deux mains a la taille, comme au plan 11.
        # D'ou UNE seule main qui MONTE, et l'autre dite immobile d'abord.
        "Her hand nearer the right edge of the picture stays hanging at her side, exactly as in the image, for "
        "the whole shot. Only her other hand moves: on her first word it rises from her side up to her chest and "
        "lays itself flat over the lapel of her coat, over her heart, just below her collarbone, and it stays "
        "there, warm and still, the beige fabric of the trench coat showing all around it.",
    # Pas de doigts entrelaces : ils fondent ensemble chez ces modeles.
    ("es-01-llegada-madrid", 11):
        "On her first words her hand nearer the left edge of the picture closes loosely round the fingers of the "
        "other, in front of her waist, a few centimetres from her coat, and they stay joined there while she "
        "speaks.",
    ("es-01-llegada-madrid", 15):
        "Her hand nearer the right edge of the picture rises to waist height, palm down and relaxed, and rocks "
        "once gently from side to side, a few centimetres, then stays there, open and easy, while she finishes; "
        "her other hand hangs relaxed at her side.",
    # 22 oct. 2026 : Mark et la voisine, meme regle (voir l'acquis du jour dans
    # video/verifier_prompt.py) -- l'autre main immobile D'ABORD.
    # Mark : la question polie
    ('es-01-llegada-madrid', 5):
        'Only one of his hands is in the picture, the one nearer the right edge, hanging low at his side; the other stays hidden behind the blurred beige shoulder for the whole shot. Only that visible hand moves: as he starts his question it comes up from the elbow to waist height, palm open and turned up, a small polite offering, and it stays there until he has finished.',
    # Mark : « moi » -- le nouveau travail
    ('es-01-llegada-madrid', 10):
        'Only one of his hands is in the picture, the one nearer the right edge, hanging low at his side; the other stays hidden behind the blurred beige shoulder for the whole shot. Only that visible hand moves: on his first word it rises to his chest and lays its fingertips flat on his black T-shirt, just below the collar of his jacket, as if to say « me », and it stays there.',
    # Mark : il montre le chemin qu'il espere
    ('es-01-llegada-madrid', 14):
        'Only one of his hands is in the picture, the one nearer the right edge, hanging low at his side; the other stays hidden behind the blurred beige shoulder for the whole shot. Only that visible hand moves: on his first words it rises to waist height, the elbow kept at his side, and the forearm alone points loosely with two fingers towards the right edge of the picture, a little downwards, the way ahead, and it stays there while he speaks.',
    # Mark : le bonjour
    ('es-02-el-carro', 2):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: as he says good morning it rises to the height of his shoulder, palm out and open, a small friendly greeting, and it stays raised while he asks his question.',
    # Mark : la surprise heureuse
    ('es-02-el-carro', 5):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: on his first words it comes up to waist height, palm open and turned up, fingers spread, in happy surprise, and it stays there.',
    # Mark : il compte les mots nouveaux
    ('es-02-el-carro', 7):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: as he repeats the new words it rises in front of his chest, two fingers raised, the thumb and the index, counting, and it stays there holding them up.',
    # Mark : sur de lui
    ('es-02-el-carro', 11):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: on his first word it rises to waist height, palm down and flat, and makes one slow, sure sweep a few centimetres out to the side, then stays there, palm down, calm and certain.',
    # Mark : pris en faute
    ('es-02-el-carro', 13):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: as he hesitates it rises to the back of his own neck and rests there until he finishes.',
    # Mark : la main a plat sur la poitrine en riant
    ('es-02-el-carro', 15):
        'His hand nearer the car stays resting on the box in the open boot, exactly as in the image, for the whole shot. Only his other hand moves: with his laugh it comes up and lays itself flat on the middle of his chest, and it stays there while he laughs.',
    # La voisine : la main sur le coeur -- quelqu'un de chez elle
    ('es-02-el-carro', 3):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: on the word she repeats it rises to her chest and lays itself flat over her heart, on the lapel of her navy coat, and it stays there, warm and still.',
    # La voisine : l'index de la maitresse d'ecole
    ('es-02-el-carro', 6):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: as she starts to explain it rises to the height of her shoulder, index finger raised, the small gesture of a teacher asking for attention, and it stays raised while she speaks.',
    # La voisine : « muy bien »
    ('es-02-el-carro', 8):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: on her first words it rises in front of her chest and makes a small circle with the thumb and the index finger, the other fingers open, and it stays there.',
    # La voisine : la main sur la hanche, pratique
    ('es-02-el-carro', 10):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: on her first word it settles on her hip, fingers forward, elbow out to the side, and it stays there, practical and sure.',
    # La voisine : la main « plus ou moins »
    ('es-02-el-carro', 12):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: as she repeats the word it rises to the height of her chest, palm down and fingers spread, and tilts gently from side to side, the « more or less » of the hand, then stays there.',
    # La voisine : elle rit, la main sur le ventre
    ('es-02-el-carro', 14):
        'Her hand stays on the black handle of her shopping trolley, exactly as in the image, for the whole shot. Only her other hand moves, the one nearer the right edge of the picture, which starts low at her side by the hem of her coat: with her laugh it rises and rests flat on her stomach, just above her waist, and it stays there while she laughs.',
    # ------------------------------------------------------------------
    # es-03 EL CAFE (22 oct. 2026). Mark : la main cote machine (bord gauche) posee
    # sur le zinc, l'autre bouge. Le serveur : la main cote machine (bord gauche) a
    # plat sur le zinc, sur son torchon ; l'autre bouge. Ana : la main cote bord
    # droit sur le zinc ; l'autre bouge.
    # ------------------------------------------------------------------
    # Mark : la demande polie, paume offerte
    ('es-03-el-cafe', 3):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: as he asks for his coffee it comes up from the elbow to waist height, palm open and turned up, a small polite offering, and it stays there until he has finished.',
    # Mark : la surprise heureuse, la main ouverte vers elle
    ('es-03-el-cafe', 7):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on his first word it comes up level with his chest, palm open and turned towards the right edge of the picture, fingers spread in happy surprise, and it stays there.',
    # Mark : il repete la formule, l'index leve pour la retenir
    ('es-03-el-cafe', 9):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: as he repeats the formula it rises in front of his chest with the index finger pointing up, the way one holds on to a sentence one has just learned, and it stays there.',
    # Mark : perdu, la main a la tempe
    ('es-03-el-cafe', 11):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on the unknown word it rises to the side of his head and its fingertips scratch once above his ear, puzzled, and the hand stays there while he asks.',
    # Mark : « la meme chose » -- il montre la commande, vers la droite
    ('es-03-el-cafe', 14):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on « lo mismo » it rises to waist height and its index finger points towards the right edge of the picture, a little downwards, at the order that was just given, and it stays pointing there.',
    # Mark, lundi : le bonjour sur de lui, main levee
    ('es-03-el-cafe', 17):
        'His hand nearer the left edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on his good morning it rises to the height of his shoulder, palm out and open, the greeting of a regular, and it stays raised while he orders.',
    # Le serveur : le pouce frotte l'index -- l'argent
    ('es-03-el-cafe', 4):
        'His hand nearer the left edge of the picture stays flat on the white cloth on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on « se paga » it comes up to chest height and its thumb rubs slowly against the tips of the index and middle fingers, the gesture for money, and it stays there, still rubbing, while he laughs.',
    # Le serveur : trois doigts pour trois cafes
    ('es-03-el-cafe', 10):
        'His hand nearer the left edge of the picture stays flat on the white cloth on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: as he names the three coffees it rises in front of his chest with three fingers up, the thumb and the little finger folded in, counting, and it stays there holding them up.',
    # Le serveur : le pouce dresse -- « muy bien »
    ('es-03-el-cafe', 18):
        'His hand nearer the left edge of the picture stays flat on the white cloth on the zinc counter, exactly as in the image, for the whole shot. Only his other hand moves: on « muy bien » it rises to the height of his shoulder, closed in a loose fist with the thumb pointing straight up, and it stays there while he calls the order.',
    # Ana : elle le reconnait, l'index vers lui
    ('es-03-el-cafe', 6):
        'Her hand nearer the right edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only her other hand moves: on « ¡Anda! » it rises to the height of her chin and its index finger points towards the left edge of the picture, the gesture of recognising someone, and it stays pointing there, delighted.',
    # Ana : elle explique, les deux mains sur le comptoir
    ('es-03-el-cafe', 8):
        'Her hand nearer the right edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only her other hand moves: as she starts to explain it comes down and settles flat on the zinc a hand\'s width from the first, both hands on the counter and her elbows out, the pose of someone settling in to explain, and it stays there.',
    # Ana : deux doigts, un cafe et une tostada
    ('es-03-el-cafe', 13):
        'Her hand nearer the right edge of the picture stays resting on the zinc counter, exactly as in the image, for the whole shot. Only her other hand moves: as she orders it rises in front of her chest with two fingers up, the index and the middle finger, one for the coffee and one for the toast, and it stays there holding them up.',
    # ------------------------------------------------------------------
    # es-04 TU O USTED (22 oct. 2026). Mark au bureau : la main cote bord gauche sur
    # le dossier de la chaise, l'autre bouge. Lucia : la tasse blanche dans la main
    # cote bord droit, l'autre bouge. Ascenseur -- Mark : une main dans la poche
    # (bord gauche), l'autre bouge ; le directeur : la mallette dans la main cote
    # bord droit, l'autre bouge.
    # ------------------------------------------------------------------
    # Mark : la main sur le coeur, politesse mexicaine
    ('es-04-tu-o-usted', 4):
        'His hand nearer the left edge of the picture stays resting on the back of the grey office chair, exactly as in the image, for the whole shot. Only his other hand moves: on « mucho gusto » it rises to his chest and lays itself flat on the lapel of his jacket, over his heart, the formal greeting of a well-brought-up man, and it stays there.',
    # Mark : il essaie le tu, la paume hesitante
    ('es-04-tu-o-usted', 7):
        'His hand nearer the left edge of the picture stays resting on the back of the grey office chair, exactly as in the image, for the whole shot. Only his other hand moves: on « vale » it comes up to waist height, palm open and turned up, and rocks once from side to side, a few centimetres, unsure, then stays there, open.',
    # Mark : la question au groupe, la main qui balaie vers la droite
    ('es-04-tu-o-usted', 10):
        'His hand nearer the left edge of the picture stays resting on the back of the grey office chair, exactly as in the image, for the whole shot. Only his other hand moves: on « ustedes » it rises to shoulder height, palm open and facing the right edge of the picture, and sweeps a few centimetres towards that edge, taking in the whole room, then stays there, open.',
    # Mark : le verbe change aussi -- les doigts au front
    ('es-04-tu-o-usted', 12):
        'His hand nearer the left edge of the picture stays resting on the back of the grey office chair, exactly as in the image, for the whole shot. Only his other hand moves: on « coméis » it rises to his forehead and lays its fingertips flat on it, as the thing dawns on him, and it stays there while he exclaims.',
    # Mark, ascenseur : le bonjour leger
    ('es-04-tu-o-usted', 15):
        'His hand nearer the left edge of the picture stays in his trouser pocket, exactly as in the image, for the whole shot. Only his other hand moves: on « hola » it comes up to shoulder height, palm out and open, an easy greeting between neighbours, and it stays raised while he asks.',
    # Mark, ascenseur : pardon, la main a plat sur la poitrine
    ('es-04-tu-o-usted', 17):
        'His hand nearer the left edge of the picture stays in his trouser pocket, exactly as in the image, for the whole shot. Only his other hand moves: on « perdón » it rises and lays itself flat on his chest, on his light-blue shirt below the knot of his collar, apologising, and it stays there while he asks again.',
    # Lucia : le salut, paume ouverte tenue
    ('es-04-tu-o-usted', 3):
        'Her hand nearer the right edge of the picture stays holding the white mug at waist height, exactly as in the image, for the whole shot. Only her other hand moves: on « hola » it rises to the height of her shoulder, palm open and turned towards the left edge of the picture, fingers together, a greeting held still, and it stays there while she speaks.',
    # Lucia : « tranquilo », la main qui tapote l'air
    ('es-04-tu-o-usted', 5):
        'Her hand nearer the right edge of the picture stays holding the white mug at waist height, exactly as in the image, for the whole shot. Only her other hand moves: on « tutéame » it rises in front of her chest, palm down, and pats the air twice towards the left edge of the picture, a few centimetres each time, the gesture for « relax », then stays there, palm down.',
    # Lucia : « ven », les doigts qui appellent
    ('es-04-tu-o-usted', 8):
        'Her hand nearer the right edge of the picture stays holding the white mug at waist height, exactly as in the image, for the whole shot. Only her other hand moves: on « ven » it rises to waist height, palm up, and its fingers curl twice towards herself, calling him along, then the hand stays there, open and waiting.',
    # Lucia : « vosotros », l'arc qui prend tout le monde
    ('es-04-tu-o-usted', 11):
        'Her hand nearer the right edge of the picture stays holding the white mug at waist height, exactly as in the image, for the whole shot. Only her other hand moves: on « vosotros » it rises to chest height, palm up, and sweeps one slow arc from the left edge of the picture towards the middle, taking in everyone in the room, and it stays at the end of the arc, palm up.',
    # Lucia : pince-sans-rire, la main sur la hanche
    ('es-04-tu-o-usted', 13):
        'Her hand nearer the right edge of the picture stays holding the white mug at waist height, exactly as in the image, for the whole shot. Only her other hand moves: on « tranquilo » it settles on her hip, fingers forward and elbow out to the side, and it stays there, easy and sure, while she delivers the consolation.',
    # Le directeur : l'index qui remue une fois
    ('es-04-tu-o-usted', 16):
        'His hand nearer the right edge of the picture stays holding the handle of his dark leather briefcase at his side, exactly as in the image, for the whole shot. Only his other hand moves: on « de usted » it rises in front of his chest with the index finger up and wags once from side to side, a few centimetres, the correction of an elder, then stays up, still.',
    # Le directeur : la paume qui s'ouvre -- bienvenue
    ('es-04-tu-o-usted', 18):
        'His hand nearer the right edge of the picture stays holding the handle of his dark leather briefcase at his side, exactly as in the image, for the whole shot. Only his other hand moves: on « bienvenido » it comes up to chest height and turns its open palm towards the left edge of the picture, welcoming, and it stays there, palm up.',
}
# La tenue d'un plan qui pose une main sur la poitrine (voir GESTES, plan 9).
TENUE_PLAN = {
    ("es-01-llegada-madrid", 9):
        "Across her chest we see only the beige trench coat, the plain grey knit of her sweater, the brown "
        "leather strap and her hand resting on the lapel, from the first frame to the last.",
    ("es-01-llegada-madrid", 10):
        "Across his chest we see only his grey jacket, his black T-shirt, plain and unmarked, and his fingertips "
        "resting on it, from the first frame to the last.",
    ("es-02-el-carro", 3):
        "Across her chest we see only her navy coat, her plain white blouse and her hand resting on the lapel, "
        "from the first frame to the last.",
    ("es-02-el-carro", 7):
        "Across his chest we see only his plain white T-shirt and his raised hand in front of it, from the first "
        "frame to the last.",
    ("es-02-el-carro", 15):
        "Across his chest we see only his plain white T-shirt and his hand resting flat on it, from the first "
        "frame to the last.",
    # es-03 : le serveur (chemise blanche, gilet noir) ; Mark le lundi (chemise et veste) ; les
    # gestes qui touchent la poitrine.
    ("es-03-el-cafe", 4):
        "Across his chest we see only his plain white shirt and his plain black waistcoat, from the first frame "
        "to the last.",
    ("es-03-el-cafe", 10):
        "Across his chest we see only his plain white shirt, his plain black waistcoat and his three raised "
        "fingers in front of it, from the first frame to the last.",
    ("es-03-el-cafe", 18):
        "Across his chest we see only his plain white shirt and his plain black waistcoat, from the first frame "
        "to the last.",
    ("es-03-el-cafe", 9):
        "Across his chest we see only his plain mid-grey knit sweater, the white collar of his T-shirt and his "
        "raised hand in front of it, from the first frame to the last.",
    ("es-03-el-cafe", 17):
        "Across his chest we see only his plain light-blue shirt and his dark jacket, open and unmarked, from "
        "the first frame to the last.",
    ("es-03-el-cafe", 13):
        "Across her chest we see only her plain rust-coloured sweater, the brown leather strap of her bag and "
        "her two raised fingers in front of it, from the first frame to the last.",
    # es-04 : le directeur (costume gris, chemise blanche, cravate unie) ; les gestes qui touchent
    # la poitrine.
    ("es-04-tu-o-usted", 4):
        "Across his chest we see only his plain light-blue shirt, his dark jacket and his hand resting flat on "
        "the lapel, from the first frame to the last.",
    ("es-04-tu-o-usted", 17):
        "Across his chest we see only his plain light-blue shirt, his dark jacket and his hand resting flat on "
        "the shirt, from the first frame to the last.",
    ("es-04-tu-o-usted", 16):
        "Across his chest we see only his white shirt, his plain dark tie and his dark grey suit jacket, from "
        "the first frame to the last.",
    ("es-04-tu-o-usted", 18):
        "Across his chest we see only his white shirt, his plain dark tie and his dark grey suit jacket, from "
        "the first frame to the last.",
}


def ecrire(sc, n, P, cadre, cote, fond, emotion, parole, mains, apres):
    mains = GESTES.get((sc, n), mains)
    f = lambda s: s.format(plan=cadre[0], cadrage=cadre[1], cote=cote, **P)
    regard = (" %s speaks towards a point just beyond the %s edge of the picture, level with %s own eyes."
              % (P["He"], cote, P["his"]))
    blocs = [f(CAMERA), emotion, parole + regard + " Let %s face follow the voice." % P["his"]]
    if mains:
        blocs.append(mains)
    # ⚠️ KLING A INCRUSTE DE FAUX SOUS-TITRES (21 oct. 2026, es-01 plan 13) : deux
    #    lignes de lettres blanches illisibles sur la poitrine d'Ana, de 2,8 s a la
    #    fin -- 0,40 $. Remede de la garde negative : ne pas nommer le texte,
    #    REMPLIR la place avec ce qui s'y trouve, du debut a la fin.
    blocs.append(TENUE_PLAN.get((sc, n)) or TENUE[(sc, P["he"])])
    blocs.append(BORD_PLAN.get((sc, n)) or BORD[(sc, P["he"], cadre[0])])
    blocs.append("Finally %s stops speaking and %s. %s blinks, %s breathes, and %s holds that expression "
                 "the whole time %s waits." % (P["he"], apres, P["He"], P["he"], P["he"], P["he"]))
    blocs += [f(fond), f(FIN)]
    d = os.path.join(RACINE, "video", "episode-" + sc, "_essai-avatar", "prompts")
    os.makedirs(d, exist_ok=True)
    texte = "\n\n".join(blocs) + "\n"
    # LE COTE SE DIT PAR LE BORD DE L'IMAGE, jamais par le corps (cote-du-corps,
    # 6 oct.) -- releve par la relecture du 21 oct. : « to his LEFT » contredisait
    # « beyond the left edge of the frame » deux phrases plus loin.
    texte = re.sub(r"off screen to (?:his|her) (LEFT|RIGHT)",
                   lambda m: "off screen beyond the %s edge of the picture" % m.group(1), texte)
    io.open(os.path.join(d, "plan%02d.txt" % n), "w", encoding="utf-8").write(texte)


if __name__ == "__main__":
    for x in PLANS:
        ecrire(*x)
    print("%d prompts ecrits" % len(PLANS))
