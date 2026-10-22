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
    ("es-01-llegada-madrid", 6):
        "As she says the first words, her hand nearer the right edge of the picture rises to the height of her "
        "waist, palm open and fingers together, pointing towards the right of the picture where the baggage belt "
        "is, and it stays there while she speaks; her other hand rests on the strap of her bag.",
    ("es-01-llegada-madrid", 9):
        "On her first word she lays her hand nearer the left edge of the picture flat on her chest, just below "
        "her collarbone, and it stays there, warm and still; her other hand hangs relaxed at her side.",
    ("es-01-llegada-madrid", 11):
        "On her first words her two hands come together in front of her waist, fingers loosely interlaced a few "
        "centimetres from her coat, and they stay joined there while she speaks.",
    ("es-01-llegada-madrid", 15):
        "Her hand nearer the right edge of the picture rises to waist height, palm down and relaxed, and rocks "
        "once gently from side to side, a few centimetres, then stays there, open and easy, while she finishes; "
        "her other hand hangs relaxed at her side.",
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
    blocs.append(TENUE[(sc, P["he"])])
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
