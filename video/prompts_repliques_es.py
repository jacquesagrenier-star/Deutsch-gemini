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

IL = {"he": "he", "him": "him", "his": "his", "He": "He", "His": "His"}
ELLE = {"he": "she", "him": "her", "his": "her", "He": "She", "His": "Her"}

# (scene, plan, pronoms, cadre, cote, fond, emotion, parole, mains (ou None), apres)
PLANS = [
    # ---------------- es-01 : Llegada a Madrid ----------------
    ("es-01-llegada-madrid", 5, IL, MOYEN, "left", HALL,
     "He has just come off a long flight from Mexico: polite, a little tired, and unsure of himself in a place that "
     "is still new to him.",
     "He asks a stranger one short question, to someone just off screen beyond the LEFT edge of the picture, his eyebrows rising with it.",
     "His visible hand hangs low at his side, open and empty, exactly as in the image.",
     "listens without speaking, his mouth closed, waiting for her answer"),
    ("es-01-llegada-madrid", 6, ELLE, MOYEN, "right", HALL,
     "She is a traveller herself, waiting for her own suitcase, and she is glad to help: open, friendly, curious "
     "about him.",
     "She answers him and then asks where he comes from, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "Her hands stay at her sides, open and empty, exactly as in the image.",
     "keeps her friendly half-smile and waits for his answer, interested"),
    ("es-01-llegada-madrid", 8, IL, SERRE, "left", HALL,
     "The tiredness lifts a little: he is pleased to be asked, and a first smile comes into his eyes.",
     "He answers in two short sentences, to someone just off screen beyond the LEFT edge of the picture.",
     None,
     "keeps the small smile and listens, his mouth closed"),
    ("es-01-llegada-madrid", 9, ELLE, MOYEN, "right", HALL,
     "She is genuinely delighted for him: a newcomer to her city.",
     "She welcomes him warmly and asks one short question, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "Her hands stay at her sides, open and empty, exactly as in the image.",
     "smiles and waits for his answer"),
    ("es-01-llegada-madrid", 10, IL, MOYEN, "left", HALL,
     "He is proud of this new job and a little nervous about it, and both show.",
     "He answers her in two short sentences, to someone just off screen beyond the LEFT edge of the picture.",
     "His visible hand hangs low at his side, open and empty, exactly as in the image.",
     "keeps a half-smile that reaches his eyes and listens"),
    ("es-01-llegada-madrid", 11, ELLE, MOYEN, "right", HALL,
     "She is pleased for him, and curious.",
     "She says how nice that is and asks him one short question, speaking to someone just off screen beyond the "
     "RIGHT edge of the picture.",
     "Her hands stay at her sides, open and empty, exactly as in the image.",
     "waits for his answer, her eyebrows still slightly raised"),
    ("es-01-llegada-madrid", 12, IL, SERRE, "left", HALL,
     "The small smile of the picture fades as a worry crosses his face: for him, nine o'clock at night is "
     "already late.",
     "He answers, then asks her a short worried question, to someone just off screen beyond the LEFT edge of the picture; his eyebrows "
     "rise on the last word.",
     None,
     "waits for her answer, his eyebrows still raised, his mouth closed"),
    ("es-01-llegada-madrid", 13, ELLE, SERRE, "right", HALL,
     "This is the funny moment of the episode: she cannot believe he thinks nine o'clock is late, and she is "
     "amused, never mocking.",
     "She repeats his word in amused disbelief, then explains with a grin, speaking to someone just off screen to "
     "her RIGHT.",
     None,
     "keeps a broad, amused smile, her mouth closed, enjoying his surprise"),
    ("es-01-llegada-madrid", 14, IL, MOYEN, "left", HALL,
     "He is reassured and hopeful again.",
     "He asks her one short question, to someone just off screen beyond the LEFT edge of the picture.",
     "His visible hand hangs low at his side, open and empty, exactly as in the image.",
     "listens without speaking, his mouth closed"),
    ("es-01-llegada-madrid", 15, ELLE, MOYEN, "right", HALL,
     "She is easy and reassuring: of course there is a metro.",
     "She answers him in two short sentences, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "Her hands stay at her sides, open and empty, exactly as in the image.",
     "smiles at him and waits"),
    ("es-01-llegada-madrid", 16, IL, SERRE, "left", HALL,
     "He is warmly grateful: a stranger made his first evening easier.",
     "He thanks her in one short sentence, to someone just off screen beyond the LEFT edge of the picture.",
     None,
     "keeps a warm smile that reaches his eyes, his mouth closed"),
    ("es-01-llegada-madrid", 17, ELLE, SERRE, "right", HALL,
     "She is warm: she wishes him well and means it.",
     "She answers and wishes him luck in two short sentences, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     None,
     "keeps a warm, open smile, her mouth closed, the goodbye already in her eyes"),
    # ---------------- es-02 : El carro ----------------
    ("es-02-el-carro", 2, IL, MOYEN, "right", RUE,
     "It is moving day and he is in a good mood: polite, cheerful, sure of his Spanish.",
     "He greets an older lady and asks her one short question, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "His hand nearer the car stays resting on the box in the open boot, and his other arm stays relaxed, "
     "exactly as in the image.",
     "listens without speaking, his mouth closed, friendly, waiting for her answer"),
    ("es-02-el-carro", 3, ELLE, MOYEN, "left", RUE,
     "She recognises his Mexican Spanish from a single word, and she is delighted: he is from home.",
     "She repeats his word, then tells him warmly where she is from, speaking to someone just off screen beyond the "
     "LEFT edge of the picture.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "keeps a delighted smile, her mouth closed, looking at him with affection"),
    ("es-02-el-carro", 5, IL, MOYEN, "right", RUE,
     "He is surprised and happy to meet someone from home, and curious.",
     "He asks her two short questions, speaking to someone just off screen beyond the RIGHT edge of the picture, his eyebrows rising.",
     "His hand nearer the car stays resting on the box in the open boot, exactly as in the image.",
     "waits for her answer, smiling, his mouth closed"),
    ("es-02-el-carro", 6, ELLE, MOYEN, "left", RUE,
     "She teaches him the Madrid words the way someone once taught her: kindly, a little amused.",
     "She explains in two short sentences, speaking to someone just off screen beyond the LEFT edge of the picture.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "watches him to see if he got it, a small encouraging smile, her mouth closed"),
    ("es-02-el-carro", 7, IL, MOYEN, "right", RUE,
     "He concentrates hard on the new words, like a student repeating after the teacher.",
     "He repeats the new words carefully, then adds one short word of agreement, speaking to someone just off "
     "screen to his RIGHT.",
     "His hand nearer the car stays resting on the box in the open boot, exactly as in the image.",
     "looks pleased with himself, his mouth closed"),
    ("es-02-el-carro", 8, ELLE, MOYEN, "left", RUE,
     "She is proud of him, and she laughs at herself: it took her a year to say that word.",
     "She praises him, then tells him one short thing about herself with a small laugh, speaking to someone just "
     "off screen to her LEFT.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "her mouth closes into a warm smile that stays"),
    ("es-02-el-carro", 10, ELLE, MOYEN, "left", RUE,
     "Now she is practical, a neighbour who knows the street: the car cannot stay where it is.",
     "She asks him one short question and adds one short sentence, speaking to someone just off screen beyond the "
     "LEFT edge of the picture.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "waits for his answer, one eyebrow slightly raised, her mouth closed"),
    ("es-02-el-carro", 11, IL, MOYEN, "right", RUE,
     "He is completely sure of himself, and the audience knows better.",
     "He answers her in one short, confident sentence, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "His hand nearer the car stays resting on the box in the open boot, exactly as in the image.",
     "keeps a confident smile, his mouth closed"),
    ("es-02-el-carro", 12, ELLE, MOYEN, "left", RUE,
     "She knows exactly what « ahorita » means, because she is Mexican too: knowing, teasing, fond of him.",
     "She repeats his word as a question, then tells him she knows better, speaking to someone just off screen to "
     "her LEFT; one eyebrow rises as she speaks.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "holds his eyes with a knowing half-smile, her mouth closed"),
    ("es-02-el-carro", 13, IL, MOYEN, "right", RUE,
     "Caught out, he hesitates, and a guilty smile spreads across his face.",
     "He answers slowly, hesitating in the middle, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "His hand nearer the car stays resting on the box in the open boot, exactly as in the image.",
     "keeps the guilty smile, his mouth closed"),
    ("es-02-el-carro", 14, ELLE, MOYEN, "left", RUE,
     "She bursts out laughing: she knew it.",
     "She laughs on the first words, then says one short sentence through her laughter, speaking to someone just "
     "off screen to her LEFT.",
     "Her hand stays on the black handle of her shopping trolley, exactly as in the image.",
     "her mouth closes into a broad smile that stays, her eyes still laughing"),
    ("es-02-el-carro", 15, IL, MOYEN, "right", RUE,
     "He laughs with her: they are two Mexicans in Madrid sharing the same joke.",
     "He agrees with her in one word, with a short laugh, speaking to someone just off screen beyond the RIGHT edge of the picture.",
     "His hand nearer the car stays resting on the box in the open boot, exactly as in the image.",
     "his mouth closes into a wide smile that stays"),
]


def ecrire(sc, n, P, cadre, cote, fond, emotion, parole, mains, apres):
    f = lambda s: s.format(plan=cadre[0], cadrage=cadre[1], cote=cote, **P)
    blocs = [f(CAMERA), emotion, parole + " Let %s face follow the voice." % P["his"]]
    if mains:
        blocs.append(mains)
    # ⚠️ KLING A INCRUSTE DE FAUX SOUS-TITRES (21 oct. 2026, es-01 plan 13) : deux
    #    lignes de lettres blanches illisibles sur la poitrine d'Ana, de 2,8 s a la
    #    fin -- 0,40 $. Remede de la garde negative : ne pas nommer le texte,
    #    REMPLIR la place avec ce qui s'y trouve, du debut a la fin.
    blocs.append(TENUE[(sc, P["he"])])
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
