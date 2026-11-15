# -*- coding: utf-8 -*-
"""Les photos de l'ORAL D'ENTRAINEMENT du manuel (donnees/entrainement/sprechen.json), session manuel-sprechen, 15 nov. 2026.

    python pflege/examen/images/prompts_entrainement.py              # ecrit les entr-2a-*.prompt.txt (gratuit)
    python pflege/examen/images/prompts_entrainement.py --recadrer   # les 8 photos 1A : les scenes Soins recadrees (gratuit)
    python pflege/examen/outils/generer_image.py entr-2a-hygiene --prompts pflege/examen/images/prompts_entrainement.py
        # le controle du prompt ; avec --payer : 0,15 $, APRES l'accord de Jacques
    python pflege/examen/images/prompts_entrainement.py --web        # les PNG faits -> img/entr-2a-*.webp et leur « src »

1A : huit photos, une par serie 101-108, prises telles quelles dans les scenes de pflege-scenes
(~/.wortando/pflege/scenes/soins-<nom>.png, 1536 x 2752) et recadrees en 4:5 sur les personnes (RECADRAGE : le haut du
cadre, en part de la hauteur). Aucune depense.
2A : seize photos, une par sujet d'expose (series 111-118), 4:3 comme l'examen, aux regles de prompts.py (une vraie photo
en reference de style, rien d'ecrit, regards hors de l'objectif, chaque soignant avec son portrait maitre et sa tenue).
Les personnes sans nom (une residente, un visiteur) sont decrites sans reference et ne reviennent nulle part ailleurs.
La description allemande de chaque photo est dans sprechen.json (« beschreibung ») : le prompt la suit.
"""
import importlib.util
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
TELC = os.path.join(RACINE, "visuel", "prototype", "telc-pflege")
DONNEES = os.path.join(TELC, "donnees", "entrainement", "sprechen.json")
LOCAL = os.path.join(os.path.expanduser("~"), ".wortando", "pflege")

_spec = importlib.util.spec_from_file_location("prompts_examen", os.path.join(ICI, "prompts.py"))
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)
TETE, SANS_TEXTE, soignant = P.TETE, P.SANS_TEXTE, P.soignant
VERT, BLANC = P.VERT, P.BLANC

# 1A : serie -> (scene de pflege-scenes, haut du cadre 4:5 en part de la hauteur)
RECADRAGE = {
    101: ("soins-aufnahme", 0.21), 102: ("soins-bad", 0.15), 103: ("soins-pause", 0.20), 104: ("soins-telefon", 0.25),
    105: ("soins-uebergabe", 0.18), 106: ("soins-visite", 0.20), 107: ("soins-altenheim", 0.20), 108: ("soins-ambulant", 0.12),
}


def ref(n):
    return ["first", "second", "third", "fourth"][n - 1]


def elif_(n):
    return soignant("Elif", "a young nurse of twenty-nine from Turkey", ref(n), "she",
                    "a plain white short-sleeved nurse's tunic with a V-neck, plain white trousers and white closed nursing "
                    "shoes, a black pen clipped to the breast pocket, a slim black wristwatch, her long dark-brown hair in a "
                    "low ponytail")


def jonas(n):
    return soignant("Jonas", "a German senior nurse of thirty-eight", ref(n), "he",
                    BLANC.replace("white closed shoes", "white trainers") + ", a pair of trauma scissors and a black pen in the breast pocket")


def arun(n):
    return soignant("Arun", "a nurse of thirty-one from Kerala in India, working in this care home", ref(n), "he",
                    VERT + ", his thin black-framed glasses on")


def olena(n):
    return soignant("Olena", "a nurse of forty-four from Ukraine, working in this care home", ref(n), "she", VERT)


def yusuf(n):
    return soignant("Yusuf", "a nurse of thirty-four from Syria", ref(n), "he", BLANC)


def amira(n):
    return ("AMIRA, a young home-care nurse of twenty-six from Tunisia. The %s reference picture shows Amira: her face and "
            "build stay exactly as in it, and her hair stays covered as in it. She wears a plain navy-blue jersey headscarf "
            "pinned under the chin, covering her hair and neck, a plain navy-blue polo shirt, dark-grey trousers, a zipped "
            "navy-blue fleece jacket left open, and black trainers." % ref(n))


def sommer(n):
    return ("DR. SOMMER, a German hospital doctor of forty. The %s reference picture shows Dr. Sommer: her face, hair and "
            "build stay exactly as in it. She wears a white doctor's coat, open, over a plain pale-blue blouse, dark-grey "
            "trousers and dark-grey trainers, a black stethoscope around her neck." % ref(n))


def personne(qui, n, regard=""):
    """un patient ou un resident nomme, d'apres son portrait maitre"""
    return ("%s, the person of the %s reference picture (that picture gives the face, the hair and the build; here the "
            "person is in the place described below), the face, skin and hair exactly as in it%s" % (qui, ref(n), regard))


def piece(n, quoi):
    return ("The %s reference picture is a real phone photograph taken in %s: use it for the photographic look and for the "
            "building (walls, floor, furniture style); this picture is set as described below.\n\n" % (ref(n), quoi))


H = "a hospital ward of the same hospital"
A = "the same care home"
PHOTOS = {
    "entr-2a-hygiene": {
        "refs": ["perso:arun", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a nurse disinfecting his hands at a wall dispenser in the corridor of a care home",
                             lumiere="soft daylight from a window at the end of the corridor") + piece(2, A) + arun(1) +
        " He stands in the middle of the picture in front of a closed pale wooden room door, turned three-quarters to the "
        "right of the picture, rubbing his hands together under a plain white wall-mounted disinfectant dispenser with a "
        "chrome lever, his eyes on his hands, concentrated.\n\nTHE CORRIDOR: warm white walls, a pale wooden handrail, a "
        "light wood-look floor, a green potted plant further back." + SANS_TEXTE,
    },
    "entr-2a-ernaehrung": {
        "refs": ["perso:herr-schulze", "perso:olena", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a carer helping an old man at lunch in the dining room of a care home",
                             lumiere="warm midday daylight from large windows") + piece(3, A) +
        personne("HERR SCHULZE, a resident of eighty-seven", 1, ": white hair, a short white beard, a skin-coloured hearing "
                 "aid, a grey cardigan over a checked shirt") + ". He sits at a light oak table on the right of the picture, "
        "a white soup plate of vegetable soup and a spoon in front of him, a napkin on his chest, looking at the glass with "
        "a hesitant face.\n\n" + olena(2) + " She sits beside him on the left of the picture, turned towards him, holding "
        "out a glass of water with both hands at the height of his chin, her eyes on his face, encouraging.\n\n"
        "THE TABLE: a white tablecloth, a small jug of water, a basket with two slices of bread." + SANS_TEXTE,
    },
    "entr-2a-angehoerige": {
        "refs": ["perso:frau-lehmann", "perso:frau-krueger", "perso:jonas", "scene:soins-uebergabe"],
        "texte": TETE.format(quoi="a nurse showing a daughter how to help her mother sit up in a hospital bed",
                             lumiere="soft daylight from the window") +
        "The fourth reference picture is a real phone photograph of the same hospital room: use it for the room, the bed, "
        "the furniture and the photographic look.\n\n" +
        personne("THE MOTHER, a patient of seventy-four", 1, ": short wavy silver-grey hair, round gold-framed glasses") +
        ", in a pale-blue hospital gown, sits on the edge of the bed in the middle of the picture, her feet on the floor, "
        "one bandaged foot in a wide black bandage shoe, smiling a little shyly.\n\n" +
        personne("THE DAUGHTER, a woman of about forty-five", 2, ": shoulder-length dark-blonde hair") +
        ", in a grey jumper and dark jeans, stands on the right of the picture and supports her mother's elbow with both "
        "hands, her eyes on Jonas.\n\n" + jonas(3) + " He stands on the left of the picture, one hand on the mother's "
        "back, showing the daughter where to hold, smiling." + SANS_TEXTE,
    },
    "entr-2a-dokumentation": {
        "refs": ["perso:jonas", "scene:soins-aufnahme"],
        "texte": TETE.format(quoi="a nurse typing on a tablet in the corridor of a hospital ward",
                             lumiere="soft daylight from a window at the end of the corridor") + piece(2, H) + jonas(1) +
        " He stands in the middle of the picture beside a grey steel care trolley with folded white towels and boxes of "
        "gloves, holding a tablet in his left hand and typing with his right forefinger, his eyes on the tablet, focused. "
        "The tablet screen shows only plain pale-blue panels.\n\nTHE CORRIDOR: warm white walls, a pale wooden handrail, "
        "closed pale wooden doors, a pale grey vinyl floor." + SANS_TEXTE,
    },
    "entr-2a-demenz": {
        "refs": ["perso:herr-schulze", "perso:elif", "scene:soins-zimmer"],
        "texte": TETE.format(quoi="a nurse sitting at the hospital bedside of an old man, showing him a family photograph",
                             lumiere="soft afternoon daylight from the window") +
        "The third reference picture is a real phone photograph of a room of the same hospital: use it for the room, the "
        "bed and the photographic look.\n\n" +
        personne("THE OLD MAN, a patient of eighty-seven", 1, ": white hair, a short white beard, a skin-coloured hearing aid") +
        ", in a pale-blue hospital gown, lies half upright in the bed on the right of the picture, looking at the photograph "
        "with a soft, slightly lost smile.\n\n" + elif_(2) + " She sits on a chair beside the bed, on the left of the picture, "
        "holding his hand with one hand and with the other a small printed family photograph turned towards him (it shows "
        "only a smiling family in a garden, no writing), her eyes on his face." + SANS_TEXTE,
    },
    "entr-2a-aggression": {
        "refs": ["perso:yusuf", "scene:soins-aufnahme"],
        "texte": TETE.format(quoi="a nurse calmly talking to an upset visitor in the corridor of a hospital ward",
                             lumiere="the white ceiling light of the corridor in the evening") + piece(2, H) + yusuf(1) +
        " He stands on the right of the picture, facing the visitor at an arm's length, both open hands raised a little in "
        "front of his chest in a calm gesture, his face calm and attentive.\n\nTHE VISITOR, a man of about fifty-five with "
        "short grey hair and a grey stubble, in a brown leather jacket over a dark-blue jumper and jeans, stands on the left "
        "of the picture, his face red and angry, his mouth open as he speaks, one arm thrown out to the side. He never "
        "touches the nurse.\n\nTHE CORRIDOR: warm white walls, a pale wooden handrail, closed pale wooden doors." + SANS_TEXTE,
    },
    "entr-2a-lebensende": {
        "refs": ["perso:olena", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a carer sitting quietly at the bedside of a very old woman in a care home room",
                             lumiere="the soft warm light of a small bedside lamp, the curtains half drawn") + piece(2, A) +
        olena(1) + " She sits on a chair beside the bed on the left of the picture, leaning a little forward, holding the "
        "old woman's hand in both hands, her eyes on the woman's face, calm and gentle.\n\nTHE OLD WOMAN, about ninety-five, "
        "very thin, with thin white hair, lies peacefully in the bed on the right of the picture, her eyes closed, her face "
        "calm, a white duvet up to her chest.\n\nTHE ROOM: a wooden care bed, a bedside cabinet with a small vase of "
        "yellow roses and a small lamp, a framed landscape painting on the wall." + SANS_TEXTE,
    },
    "entr-2a-kultur": {
        "refs": ["perso:olena", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a carer talking with an elderly resident wearing a headscarf, while a young woman translates",
                             lumiere="soft daylight from the window") + piece(2, A) +
        "THE RESIDENT, a woman of about eighty with a round kind face, wearing a loosely tied pale-green floral headscarf "
        "and a long dark-green cardigan, sits in an armchair in the middle of the picture, listening with an attentive face.\n\n" +
        olena(1) + " She sits on a chair on the left of the picture, facing the resident, explaining with an open hand.\n\n"
        "THE YOUNG WOMAN, about twenty-five, with long black hair in a loose braid, in a beige trench coat over a white "
        "jumper, crouches beside the armchair on the right of the picture, one hand on the armrest, her eyes on the resident "
        "as she translates." + SANS_TEXTE,
    },
    "entr-2a-dekubitus": {
        "refs": ["perso:arun", "perso:olena", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="two carers turning an old woman onto her side in a care bed, with pillows",
                             lumiere="soft morning daylight from the window") + piece(3, A) + arun(1) +
        " He stands on the far side of the bed, on the right of the picture, gently holding the woman's shoulder and hip as "
        "she lies turned towards him.\n\n" + olena(2) + " She stands on the near side, on the left of the picture, tucking a "
        "long white positioning pillow along the woman's back.\n\nTHE OLD WOMAN, about eighty-five, with short white hair, "
        "in a pale-yellow nightdress, lies on her side, her knees slightly bent, a white pillow between them, looking calm.\n\n"
        "THE ROOM: a wooden care bed with the side rail lowered, a bedside cabinet, a window with light curtains." + SANS_TEXTE,
    },
    "entr-2a-anleitung": {
        "refs": ["perso:jonas", "perso:elif", "scene:soins-stationszimmer"],
        "texte": TETE.format(quoi="a senior nurse showing a new colleague something at a medication trolley in the nurses' office",
                             lumiere="soft daylight from the window") +
        "The third reference picture is a real phone photograph of the same nurses' office: use it for the room, the "
        "furniture and the photographic look.\n\n" + jonas(1) + " He stands on the left of the picture beside a white "
        "medication trolley with drawers, holding up a plain white medication box without any label and pointing at it with "
        "a pen, explaining.\n\n" + elif_(2) + " She stands on the right of the picture, turned towards him, holding a small "
        "notebook and a pen, listening attentively, her eyes on the box." + SANS_TEXTE,
    },
    "entr-2a-medikamente": {
        "refs": ["perso:amira", "scene:soins-ambulant"],
        "texte": TETE.format(quoi="a home-care nurse filling a weekly pill organiser at the kitchen table of an elderly client",
                             lumiere="soft morning light from a tall old window") +
        "The second reference picture is a real phone photograph of the same old apartment: use it for the style of the "
        "apartment and for the photographic look; this picture is set in its small kitchen.\n\n" + amira(1) +
        " She sits at a small wooden kitchen table in the middle of the picture, concentrated, putting a small white tablet "
        "into one compartment of a clear plastic weekly pill organiser with seven coloured lids, plain, without letters. "
        "Beside it lie a sheet of paper with only grey lines and empty boxes and two plain white medicine boxes.\n\n"
        "THE KITCHEN: pale-yellow walls, a red coffee machine on the counter, a window with a white frame." + SANS_TEXTE,
    },
    "entr-2a-technik": {
        "refs": ["perso:frau-weber", "scene:soins-altenheim"],
        "texte": TETE.format(quoi="a small white care robot in the common room of a care home, in front of two old ladies",
                             lumiere="warm afternoon light from the large windows") +
        "The second reference picture is a real phone photograph of the same common room: use it for the room, the "
        "furniture and the photographic look.\n\nTHE ROBOT, about one metre twenty tall, smooth white plastic with rounded "
        "shapes, stands on the right of the picture on small wheels; a round face screen shows only two simple round dark "
        "eyes, and nothing else.\n\n" +
        personne("FRAU WEBER, a resident of eighty-one", 1, ": short white curly hair, small pearl earrings, a lilac twin-set") +
        ", sits in an armchair in the middle of the picture, leaning forward towards the robot with a curious, amused smile.\n\n"
        "ANOTHER RESIDENT, a woman of about ninety with thin white hair in a bun and a navy-blue cardigan, sits beside her on "
        "the left of the picture, looking at the robot with raised eyebrows, a little doubtful." + SANS_TEXTE,
    },
    "entr-2a-schlaf": {
        "refs": ["perso:herr-brandt", "perso:yusuf", "scene:soins-zimmer"],
        "texte": TETE.format(quoi="a night nurse coming quietly into a dark hospital room where an old patient lies awake",
                             lumiere="the dark of the night, only the dim light from the corridor through the open door and "
                                     "the small beam of a pen torch") +
        "The third reference picture is a real phone photograph of the same hospital room by day: use it for the room and "
        "the furniture. Now it is the middle of the night.\n\n" +
        personne("HERR BRANDT, a patient of eighty-two", 1, ": white hair, a white moustache") +
        ", in pale-blue pyjamas, lies in the bed on the right of the picture, awake, his eyes open towards the door.\n\n" +
        yusuf(2) + " He comes in through the door on the left of the picture, on tiptoe, holding a small pen torch pointed "
        "down at the floor, his eyes on the patient." + SANS_TEXTE,
    },
    "entr-2a-ankommen": {
        "refs": ["perso:elif", "scene:soins-ambulant"],
        "texte": TETE.format(quoi="a young woman with a large suitcase in front of an old apartment building in a German city",
                             lumiere="grey autumn daylight") +
        "The second reference picture is a real phone photograph taken in the same city: use it for the photographic look "
        "and the style of the old buildings; this picture is set outside, on the pavement.\n\nELIF, a young woman of "
        "twenty-nine from Turkey. The first reference picture shows Elif: her face, hair and build stay exactly as in it. "
        "Today she wears a camel-coloured coat, a grey scarf, dark jeans and white trainers, her long dark-brown hair loose. "
        "She stands in the middle of the picture beside a large dark-red suitcase and a backpack, looking down at her phone "
        "(its screen shows only a plain pale map with no writing), a little lost, with a hopeful half-smile.\n\n"
        "THE STREET: an old apartment building with a big wooden front door, tall windows, a bicycle against a tree, "
        "autumn leaves on the cobbled pavement. No house numbers, no signs, no shop names." + SANS_TEXTE,
    },
    "entr-2a-einsamkeit": {
        "refs": ["scene:soins-ambulant"],
        "texte": TETE.format(quoi="an old man sitting alone at a kitchen table, looking out of the window",
                             lumiere="grey, soft daylight from the window") +
        "The reference picture is a real phone photograph of an old apartment in the same city: use it for the style of "
        "the apartment and for the photographic look; this picture is set in another kitchen.\n\nTHE OLD MAN, about "
        "eighty, bald with a white fringe, a tired, quiet face, in a brown cardigan over a light-blue shirt, sits alone at "
        "a small table on the left of the picture, his hands around a white cup, looking out of the window on the right "
        "of the picture. A second chair at the table is empty.\n\nTHE KITCHEN: an old wooden table with a plain oilcloth, "
        "a radio switched off on the windowsill, a single plate on the draining board." + SANS_TEXTE,
    },
    "entr-2a-missverstaendnisse": {
        "refs": ["perso:sommer", "perso:elif", "scene:soins-stationszimmer"],
        "texte": TETE.format(quoi="a doctor explaining something to a nurse in the nurses' office of a hospital ward",
                             lumiere="soft daylight from the window") +
        "The third reference picture is a real phone photograph of the same nurses' office: use it for the room, the "
        "furniture and the photographic look.\n\n" + sommer(1) + " She stands on the left of the picture, explaining "
        "quickly, one hand moving in the air.\n\n" + elif_(2) + " She stands on the right of the picture, writing on a "
        "brown clipboard with a pen, her eyebrows drawn together in a small frown of concentration, her eyes on the "
        "clipboard." + SANS_TEXTE,
    },
}


def recadrer():
    from PIL import Image
    d = json.load(io.open(DONNEES, encoding="utf-8"))
    for s in d["series"]:
        if s["id"] not in RECADRAGE:
            continue
        scene, haut = RECADRAGE[s["id"]]
        im = Image.open(os.path.join(LOCAL, "scenes", scene + ".png")).convert("RGB")
        w, h = im.size
        ch = int(w * 5 / 4)
        y = min(int(h * haut), h - ch)
        im = im.crop((0, y, w, y + ch))
        im.thumbnail((1120, 1400))
        nom = "entr-1a-" + scene.replace("soins-", "")
        im.save(os.path.join(TELC, "img", nom + ".webp"), "WEBP", quality=80, method=6)
        s["taches"][0]["bild"]["src"] = "img/" + nom + ".webp"
        print("  %s -> img/%s.webp" % (scene, nom))
    io.open(DONNEES, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def web():
    from PIL import Image
    d = json.load(io.open(DONNEES, encoding="utf-8"))
    faits = 0
    for s in d["series"]:
        for t in s["taches"]:
            for th in t.get("themen", []):
                nom = "entr-2a-" + th["id"]
                src = os.path.join(LOCAL, "examen", "scenes", nom + ".png")
                if not os.path.exists(src):
                    print("  pas encore : %s" % nom)
                    continue
                im = Image.open(src).convert("RGB")
                im.thumbnail((1400, 1400))
                im.save(os.path.join(TELC, "img", nom + ".webp"), "WEBP", quality=80, method=6)
                th["bilder"][0]["src"] = "img/" + nom + ".webp"
                faits += 1
    io.open(DONNEES, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("%d image(s) en place." % faits)


def main():
    if "--recadrer" in sys.argv:
        return recadrer()
    if "--web" in sys.argv:
        return web()
    for nom, p in PHOTOS.items():
        io.open(os.path.join(ICI, nom + ".prompt.txt"), "w", encoding="utf-8", newline="\n").write(p["texte"].strip() + "\n")
        print("  %s  (%d mots, references : %s)" % (nom, len(p["texte"].split()), ", ".join(p["refs"])))


if __name__ == "__main__":
    main()
