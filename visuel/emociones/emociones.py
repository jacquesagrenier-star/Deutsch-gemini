# -*- coding: utf-8 -*-
"""Les emotions et le caractere, troisieme « theme illustre » (3 nov. 2026). ET C'EST FACTURE : 0,15 $ l'image,
chez fal. Accord de Jacques (3 nov.) : « Oui, les trois » -- 48 images, 7,20 $, 9 $ au plus avec les reprises.

    python visuel/emociones/emociones.py                 # celles qui manquent (0,15 $ chacune)
    python visuel/emociones/emociones.py Anna-contento   # celles-la seulement
    python visuel/emociones/emociones.py --montrer       # les prompts seuls, gratuit
    python visuel/emociones/emociones.py --json          # emociones.json seul, gratuit
    python visuel/emociones/emociones.py --refaire Anna-triste   # l'ancienne passe en <nom>-rate.png

UNE EMOTION SE LIT SUR UN VISAGE : six personnes deja faites (Anna, Carmen et Gisela ; Mark, Diego et Ben), 36
portraits, chaque emotion sur trois visages dont au moins un homme et une femme (l'accord contento /
contenta s'y voit). Toujours par RETOUCHE de leur image existante (nano-banana-pro/edit) : le meme visage, jamais
une description seule. UN TRAIT DE CARACTERE DEMANDE UNE SITUATION : douze petites scenes, une par trait, chacune
avec une personne de « Decrire une personne », en paires de contraires.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/emociones/img/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402
sys.path.insert(0, os.path.dirname(ICI))
import personnes as PERS                                     # noqa: E402 -- la fiche commune (6 nov. 2026)

EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "emociones", "img")
# Les sources, en pied, 1536 x 2752 : le depot principal (Descripcion, Mark) et la famille.
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png"}
for n in ("Gisela", "Ben", "Mia", "Heinz", "Peter", "Monika", "Sabine", "Frank", "Jan", "Katrin", "Lena", "Felix", "Sophie"):
    SOURCES[n] = FAMILLE + "/" + n + ".png"
for n in ("Carmen", "Diego", "Marta", "Javier", "Rosa", "Lucas", "Tomas", "Elena", "Ines", "Pablo"):
    SOURCES[n] = PRINCIPAL + "/visuel/descripcion/img/" + n + ".png"
SEXE = {"Anna": "f", "Carmen": "f", "Gisela": "f", "Mark": "m", "Diego": "m", "Ben": "m", "Marta": "f", "Javier": "m",
        "Rosa": "f", "Lucas": "m", "Tomas": "m", "Elena": "f", "Ines": "f", "Pablo": "m",
        "Heinz": "m", "Peter": "m", "Monika": "f", "Sabine": "f", "Frank": "m", "Jan": "m", "Katrin": "f", "Lena": "f",
        "Felix": "m", "Sophie": "f"}
SEXE.update({p: f["sexe"] for p, f in PERS.RESERVES.items()})      # les prenoms reserves (visuel/personnes.json)

# Chaque emotion : ce que le visage doit montrer, sans equivoque (la peur n'est pas la surprise, l'inquietude n'est
# pas la nervosite : chacune a son geste).
EMOTIONS = {
    "contento":    "happy and cheerful: a broad, genuine smile showing the teeth, bright eyes, raised cheeks.",
    "triste":      "sad: the eyes look down, the inner eyebrows are raised, the corners of the mouth turn down, the eyes are moist, close to tears.",
    "enfadado":    "angry: a deep frown, the eyebrows pulled down and together, the lips pressed tightly, glaring at the camera, the arms crossed.",
    "miedo":       "frightened, afraid: the eyes wide open with fear, the eyebrows raised and drawn together, the mouth slightly open, both hands raised in front of the chest as if to protect themselves, leaning back.",
    "sorprendido": "pleasantly surprised, amazed: the eyebrows raised very high, the eyes wide open, the mouth open in a round O, one hand on the cheek. Surprise, not fear.",
    "cansado":     "very tired, sleepy: heavy, half-closed eyelids, dark circles under the eyes, yawning widely with one hand in front of the mouth.",
    "aburrido":    "bored: the head resting heavily on one hand, the cheek pushed up by the hand, the eyes rolled to the side, a flat, expressionless mouth, slumped.",
    "nervioso":    "nervous: biting the nails of one hand, the eyes glancing sideways, the shoulders tense and raised, a small drop of sweat on the forehead.",
    "preocupado":  "worried: a deeply furrowed brow, the eyebrows drawn up and together, one hand pressed against the forehead, the lips pressed, the gaze lost to the side.",
    "orgulloso":   "proud: the chin raised, the chest out, a satisfied closed-mouth smile, holding up a gold medal on a ribbon in one hand.",
    "avergonzado": "embarrassed, ashamed: blushing red cheeks, an awkward, shy smile, one hand covering part of the face, the eyes looking down and away.",
    "enfermo":     "sick with a cold: a pale face, a red nose, feverish, watery eyes, a thick scarf around the neck, holding a paper tissue to the nose.",
}
# Six expressions par personne ; chaque emotion sur trois visages, au moins un homme et une femme. Anna a les
# quatre de la vignette (contente, surprise, fachee, triste : la bande de photomaton).
# 3 nov. : Ben triste et Ben qui a peur, refuses deux fois par le filtre de fal (content_policy_violation : un enfant
# en detresse). On ne contourne pas le filtre : la tristesse passe a Diego, la peur a Mark ; Ben garde quatre visages.
PORTRAITS = {
    "Anna":   ["contento", "triste", "enfadado", "sorprendido", "cansado", "nervioso"],
    "Carmen": ["avergonzado", "orgulloso", "triste", "sorprendido", "miedo", "preocupado"],
    "Gisela": ["avergonzado", "orgulloso", "contento", "enfadado", "aburrido", "enfermo"],
    "Mark":   ["sorprendido", "avergonzado", "cansado", "nervioso", "preocupado", "enfermo", "miedo"],
    "Diego":  ["enfadado", "contento", "miedo", "aburrido", "nervioso", "preocupado", "triste"],
    "Ben":    ["orgulloso", "aburrido", "cansado", "enfermo"],
    # 3 nov., « Oui, vas-y » (Jacques) : deux visages de plus par emotion, une femme et un homme ; chaque emotion passe
    # a cinq visages. Javier et non Lucas : ses lunettes de soleil cachent les yeux. Pas d'enfant dans les emotions fortes.
    "Elena":  ["contento", "triste", "enfadado", "miedo"],
    "Rosa":   ["sorprendido", "cansado", "aburrido", "nervioso"],
    "Marta":  ["preocupado", "orgulloso", "avergonzado", "enfermo"],
    "Tomas":  ["contento", "sorprendido", "nervioso", "avergonzado"],
    "Pablo":  ["triste", "cansado", "orgulloso", "enfermo"],
    "Javier": ["enfadado", "miedo", "aburrido", "preocupado"],
}
# Les traits, en paires de contraires : pour chacun, les personnes et la situation qui le montre sans un mot. La
# premiere est celle de la decouverte (ses phrases ont leur voix). 3 nov., deux de plus par trait (« Anna est
# sympathique [...] revient tres souvent »), avec trois regles : jamais un trait et son contraire pour la meme
# personne, ni deux traits voisins (sympathique et poli, antipathique et grossier, paresseux et desordonne) ; et AUCUN
# trait negatif pour la famille d'Anna (recommandation du chef d'orchestre, appliquee le 3 nov.) : radin, paresseux,
# grossier, desordonne et antipathique vont aux douze de Descripcion.
# 6 nov. 2026 (decision de Jacques, la coherence des personnages, visuel/personnes.json) : AUCUN trait de la liste noire
# (radin, paresseux, grossier, desordonne, antipathique, riche, pauvre) sur Mark, Anna, la famille d'Anna ni les douze
# de Descripcion, qui ont un metier dans « Les metiers » ; ni une situation qui leur donnerait un autre metier
# (l'enseignante severe, l'entraineur, le bureau). Ces images gardent leur visage, mais la personne porte un PRENOM
# RESERVE (Hugo, Sergio, Bruno, Mario, Carlos, Nuria, Paula, Silvia, Irene), qu'aucun autre theme n'emploie : un
# visage, un prenom reserve. visage() donne l'image (trait-<trait>-<visage>.webp) : rien n'est refait ni paye.
TRAITS = {
    "generoso":     [("Marta", "In a cafe, she happily pays the bill for the whole table of friends, handing her card to the waiter while the friends thank her, smiling."),
                     ("Heinz", "In a sunny park, the elderly man happily buys two ice-cream cones from an ice-cream cart and hands them to a small boy and a little girl, who smile up at him delighted."),
                     ("Monika", "At the door of her flat, she hands a big homemade cake and a full bag of groceries to a young neighbour, smiling warmly; the neighbour is touched and thanks her.")],
    "tacano":       [("Sergio", "At a restaurant table with friends, the bill arrives: he hides his wallet behind his back and looks away, pretending not to see the bill, while the friends look at him annoyed."),
                     ("Bruno", "On a sofa with friends watching a film, he hides a big bag of crisps behind his back and shakes his head while a friend reaches out asking for some."),
                     ("Paula", "In an office, colleagues collect money in an envelope for a birthday present; she clutches her purse to her chest and shakes her head, refusing to give anything, while a colleague holds out the envelope, disappointed.")],
    "trabajador":   [("Silvia", "In an office in the evening, the window dark outside, she works hard and concentrated at her desk covered with folders, typing on a laptop, a cup of coffee beside her; the other desks are empty."),
                     ("Sabine", "Late in the evening at a kitchen table under a lamp, she corrects a tall pile of school exercise books with a red pen, concentrated, a cup of tea beside her; the window behind her is dark."),
                     ("Peter", "In a garden under the summer sun, he digs a vegetable bed with a spade, sweating, sleeves rolled up, a wheelbarrow full of soil next to him.")],
    "perezoso":     [("Bruno", "In the middle of the day, he lies lazily on a sofa in a living room watching television, a bag of crisps on his belly, while a big pile of dirty dishes and an overflowing laundry basket wait next to him."),
                     ("Mario", "In a garden, he lies lazily in a hammock with his eyes half closed and a drink in his hand, while in the background other people carry boxes and rake leaves."),
                     ("Sergio", "In an office, he leans far back in his chair with his feet on the desk, yawning and looking at his phone, while a big pile of untouched files waits on the desk and a colleague walks past carrying many folders.")],
    "extrovertido": [("Tomas", "At a lively party, he stands in the middle of a group of people, telling a story with big gestures and laughing loudly; everybody around him laughs too."),
                     ("Sophie", "At a lively party in a living room, she dances in the middle of the room with her arms up, laughing, and pulls other guests in to dance with her."),
                     ("Gisela", "At an outdoor market stall, the elderly woman chats cheerfully with the vendor and two other shoppers at the same time, laughing and gesturing, everyone smiling at her.")],
    "timido":       [("Elena", "At a lively party, she stands alone in a corner, half hidden behind a plant, holding her glass in both hands close to her chest and looking at the floor, while other guests chat in the background."),
                     ("Ben", "At the door of a bright school classroom, the boy stands half hidden behind the door frame, looking shyly at the floor and holding the straps of his school bag with both hands, while other children play inside."),
                     ("Felix", "In a meeting room, all his colleagues turn to look at him because it is his turn to speak; he does not smile: he blushes bright red, hunches his shoulders, hides half of his face behind his sheet of paper and looks down at the table, very uncomfortable.")],
    "educado":      [("Mark", "At the entrance of a building, he holds the door open with a friendly smile for an elderly lady with a shopping bag who walks in and thanks him."),
                     ("Jan", "In a tram, he stands up and kindly offers his seat to an elderly woman with a walking stick, gesturing politely toward the seat; she smiles and thanks him."),
                     ("Lena", "At a bakery counter, she takes her bag of bread rolls from the baker with a warm smile, saying thank you with her hand on her heart; the baker smiles back.")],
    "grosero":      [("Nuria", "In a queue at a bakery counter, she pushes rudely in front of the other customers with her elbow, talking loudly on her phone, while the people in the queue look at her shocked."),
                     ("Hugo", "In a cinema during a film, he talks loudly on his phone with his feet on the seat in front of him, while the other spectators turn around and glare at him, annoyed."),
                     ("Silvia", "On a city pavement, she drops an empty coffee cup and a paper bag on the ground right next to a bin without looking, while a passer-by stares at her, shocked.")],
    "ordenado":     [("Carmen", "She sits at a perfectly tidy desk in a bright study: pencils lined up, folders neatly stacked and labelled, shelves in perfect order behind her; she smiles, satisfied."),
                     ("Katrin", "In a bedroom, she stands smiling in front of a perfectly organised open wardrobe: clothes folded in neat piles by colour, shirts on identical hangers, labelled boxes."),
                     ("Frank", "In a garage, he hangs the last tool on a perfectly organised wall where every tool has its outlined place, with labelled boxes on the shelves and a clean floor; he looks satisfied.")],
    "desordenado":  [("Hugo", "He stands in the middle of a very messy bedroom, scratching his head: clothes all over the floor and the unmade bed, open drawers, books and empty cups everywhere."),
                     ("Nuria", "At a cafe table, she has emptied her overflowing handbag looking for her keys: papers, make-up, receipts, sweets, cables and coins are spread everywhere in a mess, and she rummages through it, confused.")],
    # 6 nov. 2026 : Mark sur sa valise debordante (trait-desordenado-Mark.webp) est retire : Mark, le heros, ne porte
    # aucun trait de la liste noire, et son visage ne se rebaptise pas. L'image reste dans le depot, inutilisee.
    "simpatico":    [("Anna", "On a city street, she kindly helps a lost tourist couple, pointing the way on their paper map with a warm, friendly smile."),
                     ("Peter", "On the doorstep of his house, he warmly welcomes a new young neighbour, shaking her hand with a big friendly smile and chatting cheerfully."),
                     ("Felix", "In a cafe, he laughs warmly with an elderly lady at the next table who is showing him photos on her phone; both smile, a friendly chat.")],
    "antipatico":   [("Carlos", "On a city street, a young woman asks him a question politely; he turns his back on her with a cold, unfriendly face and his arms crossed."),
                     ("Irene", "In the stairwell of an apartment building, a smiling neighbour waves and says hello to her; she frowns, rolls her eyes and turns her head away from him with a cold, sour, unfriendly face, refusing to answer.")],
    # 3 nov., « go » (Jacques) : les adjectifs de personne de sa liste de cours « Adjetivos comunes », deux personnes
    # par mot. Une scene a plusieurs personnes porte la liste des autres (leurs images vont aussi en reference).
    # « feliz » : es feliz (en general) face a esta contento (aujourd'hui, le visage) -- un bel exercice ser / estar.
    # rico et pobre avec tact (Jacques) : une situation, jamais la misere.
    "feliz":        [("Gisela", "On a sunny afternoon in her flowering garden, the elderly woman sits on a bench among roses with a cup of tea, radiant and serene, smiling with her whole face: a woman who is happy with her life."),
                     ("Jan", "In a park on a sunny day, the man carries the little girl from the third reference picture on his shoulders and holds the hand of the boy from the second reference picture; all three laugh, happy together.", ["Ben", "Mia"])],
    "carinoso":     [("Heinz", "In a cosy living room, the elderly man from the first reference picture tenderly holds the hand of the elderly woman from the second reference picture and kisses her forehead; she smiles, moved.", ["Gisela"]),
                     ("Katrin", "On a sofa in the evening, the woman from the first reference picture holds the little girl from the second reference picture in her arms and reads her a picture book, stroking her hair tenderly; both smile.", ["Mia"])],
    "estricto":     [("Irene", "In a classroom, she stands in front of the blackboard as a teacher, pointing firmly at a pupil who is chatting, with a stern, serious face and raised eyebrows; the pupils sit very straight and silent."),
                     ("Carlos", "On a sports field, he is a football coach with a whistle around his neck, pointing at his stopwatch with a stern face while young players run another lap, out of breath.")],
    "estudioso":    [("Lena", "In a quiet university library, she studies attentively at a table covered with open books, colourful notes and highlighters, writing carefully in her notebook."),
                     ("Sophie", "At her desk in a student room in the evening, she revises for an exam with flash cards, books and a neat timetable on the wall, concentrated and motivated.")],
    "inteligente":  [("Felix", "In front of a whiteboard covered with mathematical formulas, he has just found the solution to a hard problem and points at it with a smile, while two colleagues look impressed."),
                     ("Elena", "At a chess club table, she makes the winning move with a calm, clever smile, while her older opponent stares at the board, surprised and impressed.")],
    "independiente":[("Rosa", "In her new flat, she assembles a big wardrobe all by herself with a screwdriver and the instructions, confident and satisfied, boxes and tools around her."),
                     ("Marta", "On a country road, she repairs the flat tyre of her bicycle herself, her bike upside down, tools in hand, calm and capable, a backpack beside her.")],
    "rico":         [("Mario", "On the deck of a beautiful private sailing yacht in a sunny harbour full of luxury boats, he relaxes in elegant clothes with sunglasses on his head, a glass in his hand."),
                     ("Nuria", "In a large luxurious penthouse apartment with designer furniture and a huge window overlooking the city skyline, she sits on an expensive sofa, elegant and relaxed.")],
    "pobre":        [("Bruno", "At a supermarket checkout, he carefully counts a few coins in his open hand to pay for bread and milk; his jacket is old and worn, his face is worried but dignified. A modest, everyday scene, no misery."),
                     ("Hugo", "At the end of the month, in a small, simple, tidy student room, he opens his empty wallet and looks at a single coin, then at a packet of cheap noodles on the table, a little sad but dignified. No misery.")],
}
MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same glasses or beard if any, the same body and the same clothes. ")
MEME_PLUSIEURS = ("The main person is the one in the first reference picture: exactly the same face, age, hair, skin, glasses "
                  "or beard if any, body and clothes. The other reference pictures show the other people of the scene, who also "
                  "keep exactly their own faces, ages, hair and clothes. ")
PORTRAIT = (" A photorealistic head-and-shoulders portrait, from the top of the head to the middle of the chest, facing the "
            "camera, centred. Plain light grey studio background with even soft light, nothing else in the picture, no text, "
            "no logos. Natural skin texture, no retouching. The expression is: ")
SITUATION = (" A photorealistic photograph of a real everyday scene, natural light, natural colours, no text, no logos, "
             "no captions. The person is clearly visible from head to at least the knees, in the centre, and their face "
             "and gesture are easy to read. Scene: ")


def images():
    """{nom de fichier: (source, prompt, format)} -- 36 portraits et 12 situations."""
    out = {}
    for p, emos in PORTRAITS.items():
        for e in emos:
            out[p + "-" + e] = (p, MEME + PORTRAIT + EMOTIONS[e], "1:1", [])
    for t, scenes in TRAITS.items():
        for p, scene, *autres in scenes:
            autres = autres[0] if autres else []
            meme = MEME_PLUSIEURS if autres else MEME
            # un prenom reserve garde le visage (et l'image) de la personne photographiee
            out["trait-" + t + "-" + PERS.visage(p)] = (PERS.visage(p), meme + SITUATION + scene, "4:3", autres)
    return out


def verifier_regles():
    """Jamais un trait et son contraire, ni deux traits voisins, pour la meme personne ; rien de negatif pour la famille."""
    voisins = {("simpatico", "educado"), ("simpatico", "generoso"), ("antipatico", "grosero"), ("perezoso", "desordenado"),
               ("estudioso", "trabajador"), ("carinoso", "simpatico"), ("feliz", "simpatico")}
    # 3 nov. (relecture qualite : Marta etait genereuse ET antipathique) : des traits qui, sans etre contraires, se
    # contredisent chez une meme personne -- l'un servirait de leurre trompeur sur l'image de l'autre.
    incompatibles = {("antipatico", "generoso"), ("antipatico", "carinoso"), ("antipatico", "educado"), ("antipatico", "feliz"),
                     ("grosero", "carinoso"), ("grosero", "simpatico"), ("tacano", "carinoso"), ("perezoso", "estudioso")}
    # 6 nov. 2026 : la liste noire vaut pour TOUS les recurrents (Mark, Anna, la famille, les douze de Descripcion)
    negatifs = PERS.TRAITS_INTERDITS
    par = {}
    for t, scenes in TRAITS.items():
        for p, *_ in scenes:
            par.setdefault(p, set()).add(t)
    fautes = []
    for p, ts in par.items():
        for t in ts:
            if MOTS_TRAITS[t]["contraire"] and MOTS_TRAITS[t]["contraire"] in ts:
                fautes.append("%s : %s et son contraire" % (p, t))
            if PERS.recurrent(p) and t in negatifs:
                fautes.append("%s (personne recurrente, visuel/personnes.json) : %s" % (p, t))
            if not PERS.recurrent(p) and not PERS.reserve(p):
                fautes.append("%s : ni recurrent ni prenom reserve" % p)
        fautes += ["%s : %s et %s, voisins" % (p, a, b) for a, b in voisins if a in ts and b in ts]
        fautes += ["%s : %s et %s, incompatibles" % (p, a, b) for a, b in incompatibles if a in ts and b in ts]
    for t, scenes in TRAITS.items():
        if len({x[0] for x in scenes}) != len(scenes):
            fautes.append("%s : deux fois la meme personne" % t)
    return fautes


# LES MOTS, la seule source : la page les lit dans emociones.json (questions et decouverte), les inventaires des voix
# (audio/manifest.py, manifest_es.py) y lisent les phrases de la decouverte. es = [masculin, feminin] ; latam ne
# porte que ce qui change en Amerique latine (enfadado -> enojado). « miedo » se dit avec tener / haben : c'est la
# lecon (tiene miedo, hat Angst), pas estar / sein.
MOTS_EMOTIONS = {
    # de : « froh » et non « glücklich », que prend feliz (es feliz / esta contento, v1082)
    "contento":    {"es": ["contento", "contenta"], "de": "froh"},
    "triste":      {"es": ["triste", "triste"], "de": "traurig"},
    # de : « wütend » et non « sauer » -- au corpus, sauer est « acide » (Die Zitrone ist sauer), et la reponse aurait
    # fait avancer la carte du gout (3 nov.)
    "enfadado":    {"es": ["enfadado", "enfadada"], "latam": ["enojado", "enojada"], "de": "wütend"},
    "miedo":       {"es": ["miedo", "miedo"], "de": "Angst", "tener": True},
    "sorprendido": {"es": ["sorprendido", "sorprendida"], "de": "überrascht"},
    "cansado":     {"es": ["cansado", "cansada"], "de": "müde"},
    "aburrido":    {"es": ["aburrido", "aburrida"], "de": "gelangweilt"},
    "nervioso":    {"es": ["nervioso", "nerviosa"], "de": "nervös"},
    "preocupado":  {"es": ["preocupado", "preocupada"], "de": "besorgt"},
    "orgulloso":   {"es": ["orgulloso", "orgullosa"], "de": "stolz"},
    "avergonzado": {"es": ["avergonzado", "avergonzada"], "de": "verlegen"},
    "enfermo":     {"es": ["enfermo", "enferma"], "de": "krank"},
}
# En allemand, d'autres tournures avec haben, vraies pour la meme image (l'exercice « ist oder hat? ») :
HABEN = {"enfadado": "schlechte Laune", "enfermo": "eine Erkältung"}
# Les traits, et leur contraire (la paire d'images de l'exercice « lo contrario » / « das Gegenteil »).
MOTS_TRAITS = {
    "generoso":     {"es": ["generoso", "generosa"], "de": "großzügig", "contraire": "tacano"},
    "tacano":       {"es": ["tacaño", "tacaña"], "de": "geizig", "contraire": "generoso"},
    "trabajador":   {"es": ["trabajador", "trabajadora"], "de": "fleißig", "contraire": "perezoso"},
    "perezoso":     {"es": ["perezoso", "perezosa"], "de": "faul", "contraire": "trabajador"},
    "extrovertido": {"es": ["extrovertido", "extrovertida"], "de": "kontaktfreudig", "contraire": "timido"},
    "timido":       {"es": ["tímido", "tímida"], "de": "schüchtern", "contraire": "extrovertido"},
    "educado":      {"es": ["educado", "educada"], "de": "höflich", "contraire": "grosero"},
    "grosero":      {"es": ["grosero", "grosera"], "de": "unhöflich", "contraire": "educado"},
    "ordenado":     {"es": ["ordenado", "ordenada"], "de": "ordentlich", "contraire": "desordenado"},
    "desordenado":  {"es": ["desordenado", "desordenada"], "de": "unordentlich", "contraire": "ordenado"},
    "simpatico":    {"es": ["simpático", "simpática"], "de": "sympathisch", "contraire": "antipatico"},
    "antipatico":   {"es": ["antipático", "antipática"], "de": "unsympathisch", "contraire": "simpatico"},
    # v1082, les adjectifs du cours : un seul contraire parmi eux, rico / pobre
    "feliz":        {"es": ["feliz", "feliz"], "de": "glücklich", "contraire": None},
    "carinoso":     {"es": ["cariñoso", "cariñosa"], "de": "liebevoll", "contraire": None},
    "estricto":     {"es": ["estricto", "estricta"], "de": "streng", "contraire": None},
    "estudioso":    {"es": ["estudioso", "estudiosa"], "de": "lerneifrig", "contraire": None},
    "inteligente":  {"es": ["inteligente", "inteligente"], "de": "intelligent", "contraire": None},
    "independiente":{"es": ["independiente", "independiente"], "de": "selbstständig", "contraire": None},
    "rico":         {"es": ["rico", "rica"], "de": "reich", "contraire": "pobre"},
    "pobre":        {"es": ["pobre", "pobre"], "de": "arm", "contraire": "rico"},
}
# La decouverte : un visage par emotion, deux emotions par personne (des visages varies sur la planche).
DECOUVERTE = {"contento": "Anna", "nervioso": "Anna", "miedo": "Carmen", "orgulloso": "Carmen",
              "avergonzado": "Gisela", "enfermo": "Gisela", "sorprendido": "Mark", "preocupado": "Mark",
              "enfadado": "Diego", "triste": "Diego", "aburrido": "Ben", "cansado": "Ben"}
NOMS = PERS.noms()                                           # Ines -> Inés, Tomas -> Tomás (visuel/personnes.json)


def phrase(langue, p, mot, emotion):
    """La phrase dite et ecrite : « Carmen está triste. », « Carmen tiene miedo. », « Marta es generosa. »,
    « Carmen ist traurig. », « Carmen hat Angst. ». La page fabrique ses phrases avec la meme regle."""
    n, f = NOMS.get(p, p), SEXE[p] == "f"
    if langue == "de":
        return "%s %s %s." % (n, "hat" if mot.get("tener") else "ist", mot["de"])
    forme = (mot.get("latam") if langue == "latam" else None) or mot["es"]
    verbe = "tiene" if mot.get("tener") else ("está" if emotion else "es")
    return "%s %s %s." % (n, verbe, forme[1 if f else 0])


def identifiant(texte):
    import hashlib
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def ecrire_json():
    """La donnee de la page : qui montre quelle emotion, quel trait est montre par qui, les mots, et les phrases de
    la decouverte avec l'identifiant de leur son (sha1 du texte, comme audio/manifest.py)."""
    dec = {}
    for langue in ("es", "latam", "de"):
        dec[langue] = {}
        for e, p in DECOUVERTE.items():
            t = phrase(langue, p, MOTS_EMOTIONS[e], True)
            dec[langue][e] = {"texte": t, "son": identifiant(t)}
        for t_id, scenes in TRAITS.items():
            t = phrase(langue, scenes[0][0], MOTS_TRAITS[t_id], False)
            dec[langue][t_id] = {"texte": t, "son": identifiant(t)}
    gens = list(PORTRAITS) + [x[0] for v in TRAITS.values() for x in v]
    d = {"sexe": {p: SEXE[p] for p in dict.fromkeys(gens)},
         "noms": NOMS, "visages": {p: PERS.visage(p) for p in dict.fromkeys(gens) if PERS.reserve(p)}, "portraits": PORTRAITS, "traits": {t: [x[0] for x in v] for t, v in TRAITS.items()},
         "emotions": MOTS_EMOTIONS, "caracteres": MOTS_TRAITS, "haben": HABEN,
         "decouverte": {"visages": DECOUVERTE, "caracteres": {t: v[0][0] for t, v in TRAITS.items()}, "phrases": dec},
         "sens": sens_des_mots()}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    for chemin in (os.path.join(ICI, "emociones.json"), os.path.join(RACINE, "visuel", "prototype", "emociones", "emociones.json")):
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)


# LE SENS (3 nov. 2026) : un mot qui a deux entrees au corpus (rico : « delicieux » et « riche ») a deux cartes. La page
# envoie avec le mot la traduction francaise de l'entree qu'elle enseigne (« sens ») ; carteDeScene() fait avancer
# celle-la. Ici, les mots dont le theme ne prend pas la premiere entree ; pour les autres, l'entree unique.
SENS_VOULU = {"es": {"rico": "riche"}, "de": {}}
NOMS_DU_THEME = {"de": {"Angst": "die", "Laune": "die", "Erkältung": "die"}, "es": {"miedo": "el"}}


def entrees_du_corpus(langue):
    """[(mot, genre ou None, entree)] : les adjectifs puis les noms du corpus de cette langue."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    adj, noms = ("adjectif.json", "themes.json") if langue == "de" else ("espanol/datos/adjetivos.json", "espanol/datos/temas.json")
    out = [(e["mot"], None, e) for v in lire(adj).values() for e in v if isinstance(e, dict)]
    out += [(m["mot"], m.get("genre"), m) for t in lire(noms)["themes"] for m in t["mots"]]
    return out


def entree_voulue(langue, mot, genre=None):
    """L'entree du corpus que le theme enseigne pour ce mot : celle du sens voulu, sinon la premiere."""
    cands = [e for m, g, e in entrees_du_corpus(langue) if m == mot and (genre is None or g == genre) and (genre or g is None)]
    voulu = SENS_VOULU[langue].get(mot)
    if voulu:
        cands = [e for e in cands if e.get("traduction") == voulu] or cands
    return cands[0] if cands else None


def sens_des_mots():
    """{langue: {cle: traduction francaise}}, la cle comme celle des gloses (« rico », « el miedo »)."""
    out = {}
    for langue in ("de", "es"):
        out[langue] = {}
        mots = [m["de"] if langue == "de" else m["es"][0] for m in list(MOTS_EMOTIONS.values()) + list(MOTS_TRAITS.values()) if not m.get("tener")]
        for w in mots:
            e = entree_voulue(langue, w)
            if e:
                out[langue][w] = e.get("traduction")
        for w, g in NOMS_DU_THEME[langue].items():
            e = entree_voulue(langue, w, g)
            if e:
                out[langue][g + " " + w] = e.get("traduction")
    return out


def ecrire_gloses():
    """La traduction des mots du theme, tiree du CORPUS (relu), pour les langues d'interface ou la page ne traduit pas
    la phrase entiere (ar, tr, uk, fa, pl, ru) : sous la phrase juste, « triste — حزين ». Meme forme que
    familia/gloses.json (cle : article et mot ; valeur : {langue: traduction}). Fichier DERIVE : le refaire."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}
    adj = lambda p: [e for v in lire(p).values() for e in v if isinstance(e, dict)]
    noms = lambda p: [m for t in lire(p)["themes"] for m in t["mots"]]
    voulus = {"de": [m["de"] for m in list(MOTS_EMOTIONS.values()) + list(MOTS_TRAITS.values()) if not m.get("tener")],
              "es": [m["es"][0] for m in list(MOTS_EMOTIONS.values()) + list(MOTS_TRAITS.values()) if not m.get("tener")]}
    out = {"de": {}, "es": {}}
    for langue, adjs, ns, champs, nomsVoulus in (("de", adj("adjectif.json"), noms("themes.json"), LDE, {"Angst": "die", "Laune": "die", "Erkältung": "die"}),
                                                 ("es", adj("espanol/datos/adjetivos.json"), noms("espanol/datos/temas.json"), LES, {"miedo": "el"})):
        for w in voulus[langue]:
            e = entree_voulue(langue, w)
            if e:
                out[langue][w] = {l: e[c] for l, c in champs.items() if e.get(c)}
        for m in ns:
            if nomsVoulus.get(m["mot"]) == m.get("genre"):
                cle = m["genre"] + " " + m["mot"]
                out[langue].setdefault(cle, {l: m[c] for l, c in champs.items() if m.get(c)})
    manque = [w for l in out for w in voulus[l] if w not in out[l]]
    assert not manque, "absents du corpus : %s" % manque
    io.open(os.path.join(RACINE, "visuel", "prototype", "emociones", "gloses.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def textes_a_dire(langue):
    """Pour les inventaires des voix : les phrases de la decouverte, dans cette langue (es, latam, de)."""
    d = json.load(io.open(os.path.join(ICI, "emociones.json"), encoding="utf-8"))
    return [v["texte"] for v in d["decouverte"]["phrases"][langue].values()]


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = images()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    fautes = verifier_regles()
    if fautes:
        sys.exit("  distribution fautive :\n  " + "\n  ".join(fautes))
    os.makedirs(DOSSIER, exist_ok=True)
    # v1078 : une seule scene par trait, nommee trait-<trait>.png ; elle devient trait-<trait>-<personne>.png
    for t, scenes in TRAITS.items():
        vieux = os.path.join(DOSSIER, "trait-" + t)
        if os.path.exists(vieux + ".png"):
            for ext in (".png", "-fal.json"):
                if os.path.exists(vieux + ext):
                    os.replace(vieux + ext, vieux + "-" + PERS.visage(scenes[0][0]) + ext)
    ecrire_json()
    ecrire_gloses()
    if "--json" in sys.argv:
        return
    if refaire and not montrer:
        for n in noms:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY") and not os.path.exists(os.path.join(RACINE, "fal.secret")):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    depots = {}
    for nom in a_faire:
        source, prompt, fmt, autres = tout[nom]
        print("\n  %s\n  %s" % (nom, prompt))
        if montrer:
            continue
        if source not in depots:
            depots[source] = O.deposer(SOURCES[source], "image/png", cle)[0]
        for a in autres:
            if a not in depots:
                depots[a] = O.deposer(SOURCES[a], "image/png", cle)[0]
        corps = {"prompt": prompt, "image_urls": [depots[source]] + [depots[a] for a in autres], "aspect_ratio": fmt, "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            # 3 nov. : Ben triste refuse (HTTP 422) et tout le lot s'arretait. On note la raison et on continue.
            import urllib.request, urllib.error
            raison = str(err)
            try:
                urllib.request.urlopen(urllib.request.Request(soum["response_url"], headers={"Authorization": "Key " + cle}), timeout=60)
            except urllib.error.HTTPError as e:
                raison += " " + e.read().decode("utf-8", "replace")[:400]
            print("  ECHEC", nom, raison)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), raison.replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "source": SOURCES[source], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
