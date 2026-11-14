# -*- coding: utf-8 -*-
"""Les 7 photos de l'oral de l'examen blanc telc Pflege (1A et les trois photos de chaque sujet de 2A).

    python pflege/examen/images/prompts.py          # ecrit pflege/examen/images/<nom>.prompt.txt (gratuit)
    python pflege/examen/outils/generer_image.py oral-1a                 # le controle du prompt, RIEN n'est paye
    python pflege/examen/outils/generer_image.py oral-1a --payer         # 0,15 $, APRES l'accord (chef + Jacques)

LES REGLES DE PFLEGE-SCENES (message du 14 nov.), reprises ici :
  - une vraie photo AVEC des personnes en reference de style, toujours (sans elle, des scenes sortent dessinees) ;
  - « A real photograph, taken with a good phone camera… » en tete, puis « the textures of real … » ;
  - rien d'ecrit (verifier a la loupe, effacer avec visuel/effacer_texte.py) ; pas d'heure a une horloge ;
  - la gauche et la droite se disent par l'IMAGE ; les regards jamais vers l'objectif, on dit ou vont les yeux ;
  - chaque soignant avec SON portrait maitre en reference (~/.wortando/pflege/personnages/<id>.png) et sa tenue
    reprise mot pour mot de pflege/scenes/portraits.py (branche de pflege-scenes) ; Frau Weber et Herr Schulze tels
    qu'ils sont dans la scene de la maison de retraite (soins-altenheim).
Les references de chaque photo sont listees dans REFS : generer_image.py les passe dans cet ordre, et le prompt les
nomme dans le meme ordre.
"""
import io
import os

ICI = os.path.dirname(os.path.abspath(__file__))

TETE = ("A real photograph, taken with a good phone camera and looking exactly like a phone photograph, of {quoi}, "
        "in a wide horizontal picture, everything in sharp focus. Natural colours, {lumiere}. The textures of real "
        "cotton, wool, plastic, steel, skin and hair, with the true depth and the slight lens perspective of a "
        "photograph.\n\n")
SANS_TEXTE = ("\n\nThe whole picture carries no writing, numbers, print, symbol or logo anywhere: the clothes have no "
              "name badge, no embroidery and no brand, every paper is blank or carries only grey lines and empty boxes, "
              "and every screen shows only plain pale-blue panels.")

# les soignants (portraits maitres de pflege-scenes, 14 nov.) : L'IMAGE FAIT FOI. Une ligne par reference, selon la
# consigne de pflege-scenes (« the Nth reference picture shows <role> : her face, hair and build stay exactly as in
# it »), puis la tenue seule ; aucun trait du visage ni des cheveux qui pourrait contredire le portrait.
def soignant(nom, qui, ref, il, tenue):
    poss = {"he": "his", "she": "her"}[il]
    return ("%s, %s. The %s reference picture shows %s: %s face, hair and build stay exactly as in it. %s wears %s."
            % (nom.upper(), qui, ref, nom, poss, il.capitalize(), tenue))


VERT = "a plain sage-green short-sleeved polo shirt, navy-blue trousers and black closed shoes"
BLANC = "a plain white short-sleeved nurse's tunic, plain white trousers and white closed shoes"
OLENA = soignant("Olena", "a nurse of forty-four from Ukraine, working in this care home", "first", "she",
                 VERT)
ARUN = soignant("Arun", "a nurse of thirty-one from Kerala in India, working in this care home", "first", "he",
                VERT + ", his thin black-framed glasses on")
YUSUF = soignant("Yusuf", "a nurse of thirty-four from Syria, on the night shift", "first", "he", BLANC)
JONAS = soignant("Jonas", "a German senior nurse of thirty-eight", "second", "he",
                 BLANC.replace("white closed shoes", "white trainers") +
                 ", a pair of trauma scissors and a black pen in the breast pocket")
ELIF = soignant("Elif", "a young nurse of twenty-nine from Turkey", "first", "she",
                "a plain white short-sleeved nurse's tunic with a V-neck, plain white trousers and white closed nursing "
                "shoes, a black pen clipped to the breast pocket, a slim black wristwatch, her long dark-brown hair in a "
                "low ponytail")
# Amira porte au travail un foulard en jersey bleu marine (decision de Jacques : « Amira seulement ») ; au jogging,
# un foulard de sport du meme bleu
AMIRA_SPORT = ("AMIRA, a young nurse of twenty-six from Tunisia. The third reference picture shows Amira: her face and "
               "build stay exactly as in it, and her hair stays covered as in it. Today she wears a close-fitting "
               "navy-blue sports headscarf in jersey covering her hair and neck, a long-sleeved navy-blue running top, "
               "black running trousers and grey running shoes.")
# Frau Weber et Herr Schulze : des decoupes de la scene soins-altenheim (pflege-scenes, 14 nov.), table et objets
# compris dans le cadre : la reference sert pour la PERSONNE seulement
WEBER = ("FRAU WEBER, a resident of eighty-one, the woman of the {ref} reference picture (that picture gives her face, her hair and "
         "her clothes; here she is in the place described below), her face, skin and hair exactly as in it: short "
         "white curly hair, small pearl earrings, a lilac twin-set")
SCHULZE = ("HERR SCHULZE, a resident of eighty-seven, the man of the {ref} reference picture (that picture gives his face, his "
           "hair and his clothes; here he is in the place described below), his face, skin and hair "
           "exactly as in it: white hair, a short white beard, a skin-coloured hearing aid at his ear, a grey cardigan "
           "over a white shirt")
KRUEGER = ("FRAU KRÜGER, a woman of about forty-five, the woman of the first reference picture (that picture gives her "
           "face, her hair and her clothes; here she is in the place described below), her face and hair exactly as in "
           "it: shoulder-length dark-blonde hair, a navy-blue raincoat over a grey jumper and dark jeans")

PHOTOS = {
    # 1A : la photo de la partie 1A (description de sprechen.json, tache sp1a)
    "oral-1a": {
        "refs": ["perso:olena", "perso:frau-weber", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a carer helping an old woman walk with a walker along a bright corridor of a care home",
                             lumiere="soft daylight from a large window at the end of the corridor") +
        "The third reference picture is a real phone photograph taken in the common room of the same care home: use it "
        "for the photographic look and for the warm, homely style of the house; this picture is set in another room of the house.\n\n" +
        WEBER.format(ref="second") + ", with grey trousers and soft dark-red slippers, walks slowly "
        "in the middle of the picture, holding the handles of a grey four-wheeled walker with a small basket, looking "
        "ahead along the corridor with a small proud smile.\n\n" + OLENA + " She walks beside Frau Weber, on the left of "
        "the picture, one hand lightly on Frau Weber's back, her eyes on Frau Weber's feet, smiling.\n\n"
        "THE CORRIDOR: warm white walls with a pale wooden handrail along the wall on the right of the picture, a "
        "light wood-look floor, two green potted plants by the wall, a large window at the far end showing trees, and a "
        "closed pale wooden door on the left. The moment is calm and friendly." + SANS_TEXTE,
    },
    # 2A « Schmerzen erkennen », photo 1
    "oral-schmerz-1": {
        "refs": ["perso:frau-weber", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="an old woman in pain, sitting in an armchair in the common room of a care home",
                             lumiere="soft afternoon daylight from the window") +
        "The second reference picture is a real phone photograph of the same common room: use it for the room, the "
        "furniture and the photographic look.\n\n" + WEBER.format(ref="first") +
        ", sits alone in a green armchair in the middle of the picture, leaning a little to the left of the picture, one "
        "hand pressed on her hip on the left of the picture, her face screwed up in pain, her eyes half closed, her lips "
        "pressed together. A cup of tea stands untouched on a small table beside her. Nobody else is close to her; the "
        "rest of the room is calm and blurred a little behind her." + SANS_TEXTE,
    },
    # 2A « Schmerzen erkennen », photo 2
    "oral-schmerz-2": {
        "refs": ["perso:arun", "perso:herr-schulze", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a nurse at the bedside of an old man in a care home, filling in a pain observation sheet",
                             lumiere="soft morning daylight from the window") +
        "The third reference picture is a real phone photograph of the same care home: use it for the photographic look "
        "and the homely style of the rooms; this picture is set in another room of the house.\n\n" + SCHULZE.format(ref="second") + ", lies in a bed "
        "with pale wooden boards on the right of the picture, his head on a white pillow, a cream blanket up to his "
        "chest, looking at the nurse with a slightly troubled face.\n\n" + ARUN + " He sits on a chair beside the bed, on "
        "the left of the picture, turned towards Herr Schulze, a brown clipboard on his knee, writing with a blue pen on "
        "a white sheet that shows only a row of five simple drawn faces, from smiling to sad, and empty grey boxes; his "
        "eyes go from the sheet to Herr Schulze's face.\n\n"
        "THE ROOM: warm white walls, a window with light curtains, a small bedside cabinet with a glass of water." + SANS_TEXTE,
    },
    # 2A « Schmerzen erkennen », photo 3
    "oral-schmerz-3": {
        "refs": ["perso:frau-krueger", "perso:jonas", "scene:soins-aufnahme"],
        "texte": TETE.format(quoi="a woman talking with a nurse in a hospital corridor",
                             lumiere="soft daylight from a window at the end of the corridor") +
        "The third reference picture is a real phone photograph taken on the same hospital ward: use it for the "
        "photographic look; the corridor has the same warm white walls and the same pale grey vinyl floor as in that "
        "photograph.\n\n" + KRUEGER + ", stands on the left of the picture, holding the strap of her handbag, her face "
        "worried, her eyes on Jonas as she speaks.\n\n" + JONAS + " He stands on the right of the picture, facing her, "
        "listening attentively, one hand slightly raised in a calm, reassuring gesture.\n\n"
        "THE CORRIDOR: a pale wooden handrail along the wall, two closed pale wooden doors, a grey steel trolley with "
        "folded white towels further back." + SANS_TEXTE,
    },
    # 2A « Schichtarbeit », photo 1
    "oral-schicht-1": {
        "refs": ["perso:yusuf", "scene:soins-stationszimmer"],
        "texte": TETE.format(quoi="a nurse alone at night in the nurses' office of a hospital ward",
                             lumiere="the warm light of one desk lamp and the cold glow of a computer screen, the window behind dark") +
        "The second reference picture is a real phone photograph of the same nurses' office by day: use it for the room "
        "and the furniture, and for the photographic look. Now it is the middle of the night.\n\n" + YUSUF + " He sits "
        "alone at the desk in the middle of the picture, in front of a computer screen showing only plain pale-blue "
        "panels, one hand covering a big yawn, his eyes half closed, his shoulders tired. A mug stands beside the "
        "keyboard. The window behind him is black." + SANS_TEXTE,
    },
    # 2A « Schichtarbeit », photo 2
    "oral-schicht-2": {
        "refs": ["perso:elif", "scene:soins-aufnahme"],
        "texte": TETE.format(quoi="a young nurse eating a bread roll standing up in a hospital corridor",
                             lumiere="soft daylight from a window at the end of the corridor") +
        "The second reference picture is a real phone photograph taken on the same hospital ward: use it for the "
        "photographic look; the corridor has the same warm white walls and the same pale grey vinyl floor as in that "
        "photograph.\n\n" + ELIF + " She stands in the middle of the picture beside a "
        "grey steel care trolley, taking a quick bite of a bread roll held in one hand, a small paper bag in the other, "
        "her eyes turned down the corridor towards a patient's door on the right of the picture, in a hurry.\n\n"
        "THE CORRIDOR: a pale wooden handrail along the wall, closed pale wooden doors, a hand sanitiser pump bottle on "
        "the trolley." + SANS_TEXTE,
    },
    # 2A « Schichtarbeit », photo 3
    "oral-schicht-3": {
        "refs": ["perso:elif", "perso:olena", "perso:amira"],
        "texte": TETE.format(quoi="three women jogging together along a path in a city park in the morning",
                             lumiere="fresh morning sunlight through the trees") +
        "The three reference pictures are real phone photographs of the three women, in their work clothes; here they "
        "are in sports clothes.\n\n"
        "ELIF, a young nurse of twenty-nine from Turkey. The first reference picture shows Elif: her face, hair and "
        "build stay exactly as in it. Today she wears a white running top, black running tights and white running "
        "shoes, her long dark-brown hair in a ponytail. She runs on the left of the picture.\n\n"
        "OLENA, a nurse of forty-four from Ukraine. The second reference picture shows Olena: her face, hair and build "
        "stay exactly as in it. Today she wears a sage-green running jacket, dark-grey running trousers and grey "
        "running shoes. She runs in the middle.\n\n" + AMIRA_SPORT +
        " She runs on the right of the picture.\n\n"
        "All three run side by side towards the left of the picture, laughing together, their eyes on each other or on "
        "the path. THE PARK: a gravel path, green lawns, tall trees in autumn colours, a bench far behind." + SANS_TEXTE,
    },
}


def main():
    for nom, p in PHOTOS.items():
        io.open(os.path.join(ICI, nom + ".prompt.txt"), "w", encoding="utf-8", newline="\n").write(p["texte"].strip() + "\n")
        print("  %s  (%d mots, references : %s)" % (nom, len(p["texte"].split()), ", ".join(p["refs"])))


if __name__ == "__main__":
    main()
