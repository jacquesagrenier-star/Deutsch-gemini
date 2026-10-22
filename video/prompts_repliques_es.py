# -*- coding: utf-8 -*-
"""Les prompts des repliques de la serie espagnole (es-01, es-02), ecrits d'un seul gabarit.

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
Ce fichier est la source ; les planNN.txt se regenerent, ils ne s'editent pas.
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
    blocs.append(BORD[(sc, P["he"], cadre[0])])
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
