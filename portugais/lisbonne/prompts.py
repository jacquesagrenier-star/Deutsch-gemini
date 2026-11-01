# -*- coding: utf-8 -*-
"""Les prompts des 26 scenes de Lisbonne qui suivent le pilote, et leurs mots prevus. GRATUIT.

    python portugais/lisbonne/prompts.py            # ecrit visuel/scenes/<nom>.prompt.txt,
                                                    # portugais/lisbonne/references.json et mots-prevus.json
    python portugais/lisbonne/prompts.py --montrer eletrico-28

Bible : portugais/lisbonne/HISTOIRE-LISBONNE.md (Jacques, 1er nov. 2026 : « Fais les cinq au complet. »).
Le pilote (aeroporto-lisboa, casa-graca, pastelaria, miradouro) a ses prompts ecrits a la main dans
visuel/scenes/ ; ce script ne les touche pas, il les decrit seulement dans references.json et
mots-prevus.json.

Memes regles que les scenes de Camille : photo reelle, 9:16, trois bandes, « every surface is plain »,
aucune negation, et une personne qui revient entre TOUJOURS par son image (regle personne-sans-reference) :
Leo par personnages/Leo.png et Leo-droite.png ; Dona Fernanda, Beatriz et Sr. Albano par leur decoupe
du pilote (personnages/lisbonne/) ; Rui, Lucas, la professora Helena et tia Conceicao seront decoupes
de leur premiere scene reussie (albergue, aula-portugues, aula-portugues, acores). Un lieu qui revient
(la pastelaria au match, le hall de l'aeroport au depart) entre par son image de la premiere scene.

Puis : python video/verifier_prompt.py est appele par visuel/generer_scene.py ; les mots, par
python portugais/lisbonne/verifier_mots.py.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))
SCENES = os.path.join(RACINE, "visuel", "scenes")

ORD = ["first", "second", "third", "fourth"]

# Les personnes et les lieux qui reviennent : (fichier, ce que l'image montre, ce qui doit rester).
REF = {
    "leo": ("personnages/Leo.png", None, None),
    "leo-cote": ("personnages/Leo-droite.png", None, None),
    "fernanda": ("personnages/lisbonne/fernanda.png", "the landlady, the small round old woman with short white hair",
                 "her face, her short white hair, her build and her apron printed with large red flowers"),
    "beatriz": ("personnages/lisbonne/beatriz.png", "the waitress, the young woman with round red glasses",
                "her face, her dark hair pinned up, her round red glasses and her build"),
    "albano": ("personnages/lisbonne/albano.png", "the owner of the pastry shop, the man with the thick white moustache",
               "his face, his thick white moustache, his bald head, his build and his red-and-blue checked shirt"),
    "rui": ("personnages/lisbonne/rui.png", "the hostel receptionist, the young man with the black beard",
            "his face, his black beard, his build and his grey wool cardigan"),
    "lucas": ("personnages/lisbonne/lucas.png", "the classmate in the green cap",
              "his face, his green cap and his build"),
    "lieu-pastelaria": ("visuel/scenes/pastelaria.png", "the place: the same small pastry shop",
                        "the blue and white tiled walls, the dark wooden shelves, the long marble counter, the chrome coffee machine, the round white lamps and the clock stay exactly as in it"),
    "lieu-aeroporto": ("visuel/scenes/aeroporto-lisboa.png", "the place: the same baggage hall of Lisbon airport",
                       "the polished stone floor, the baggage belt, the grey seats, the clock, the tall windows and the exit doors stay exactly as in it"),
}

LEO = ("his face, his wavy dark-brown hair, his short stubble, his build, his height and his clothes, the royal-blue "
       "hooded sweatshirt with its red band across the chest, the white t-shirt, the cream scarf with small blue "
       "embroidered flowers, the dark-blue jeans and the white canvas sneakers, stay exactly as in them.")
LEO_ETE = ("his face, his wavy dark-brown hair, his short stubble, his build and his height stay exactly as in them; "
           "it is summer, and he wears ")


def paragraphe_refs(refs, tenue_ete=None):
    """Le paragraphe des references, dans l'ordre ou la commande les passe."""
    phrases = []
    i = 0
    if refs[:2] == ["leo", "leo-cote"]:
        corps = LEO if not tenue_ete else LEO_ETE + tenue_ete + "."
        phrases.append("The first reference picture shows the young man from the front, the second shows him "
                       "from his side: " + corps)
        i = 2
    for r in refs[i:]:
        _, qui, garde = REF[r]
        if r.startswith("lieu-"):
            phrases.append("The %s reference picture shows %s: %s." % (ORD[i], qui, garde))
        else:
            phrases.append("The %s reference picture shows %s: %s stay exactly as in it." % (ORD[i], qui, garde))
        i += 1
    return "\n\n".join(phrases)


def prompt(s):
    # « one single continuous view » : la premiere prise du tram (1er nov.) est sortie en TROIS panneaux,
    # les trois bandes du prompt lues comme trois photos.
    tete = ("A real photograph of %s, in a tall vertical picture made of one single continuous view, caught as it happens, as %s would take it with a "
            "good phone camera. Taken with a 24 mm lens at %s, everything in sharp focus. %s; the textures of real %s."
            % (s["lieu"], s["qui"], s["camera"], s["lumiere"], s["textures"]))
    plat = ("Every surface in the picture is plain: %s, and the clothes are plain cloth. Each object stands clearly on "
            "its own, with a band of bare %s around it, so that the eye can tell at once where everything is."
            % (s["plain"], s["vide"]))
    bandes = ["The picture is built in three bands, from the bottom edge to the top edge."]
    for titre, lignes in s["bandes"]:
        bandes.append(titre + ":\n" + "\n".join("- " + l + (";" if k < len(lignes) - 1 else ".")
                                                for k, l in enumerate(lignes)))
    morceaux = [tete]
    if s["refs"]:
        morceaux.append(paragraphe_refs(s["refs"], s.get("ete")))
    morceaux += [plat] + bandes + [s["fin"]]
    return "\n\n".join(morceaux) + "\n"


L = "the young man of the reference pictures"

S = {}

# ---------------------------------------------------------------- AUTOMNE (A1)
S["eletrico-28"] = dict(
    n=2, titre="No elétrico 28", titre_fr="Dans le tram 28",
    lieu="the inside of an old yellow Lisbon tram climbing a steep cobbled street on a sunny September afternoon",
    qui="a passenger", camera="standing eye height near the back door of the tram, looking down the whole length of the aisle in one view, from the passengers close by to the driver far away at the front",
    lumiere="Bright afternoon sunlight through the side windows and warm reflections on the varnished wood",
    textures="varnished wood, polished brass, worn leather straps, glass, painted metal, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the tram walls are plain varnished wood, the seats are plain wood slats, the bags are plain single colours, the signs are plain cream rectangles",
    vide="wooden floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands in the aisle on the left of the middle, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; he holds a leather strap hanging from the ceiling with one hand and the handle of his bright grass-green hard-shell suitcase with the other, his eyebrows raised in surprise",
        "his suitcase is stuck in the open folding door of the tram on the right of the picture, the door half closed on it",
        "a small old lady in a black dress and a black cardigan, a shopping basket on her arm, pushes the suitcase out of the door with a firm bump of her hip, smiling, completely calm",
    ]), ("THE MIDDLE OF THE TRAM, from left to right", [
        "on the left, wooden seats where a young mother sits with a small boy on her knees; the boy looks at the suitcase, delighted",
        "in the centre, two tourists in sun hats hold a paper map between them",
        "on the right, a man in a grey suit stands holding a folded newspaper",
    ]), ("THE FAR END OF THE SAME AISLE, across the upper third of the picture", [
        "at the far end of the aisle, small in the distance and seen through the same wooden interior, the driver in a dark-blue uniform jacket and cap sits at the brass controls with his back to us",
        "beyond him, through the front window of the same tram, the steep cobbled street climbs between pale-yellow and white houses, and a church tower stands at the top against a blue sky",
    ])],
    fin="The tram is full but each person stands clearly on their own: between them, the same bare wooden floor and the same bare wooden walls.",
    mots=["elétrico", "mala", "porta", "janela", "banco", "criança", "mapa", "jornal", "cesto", "rua", "igreja", "céu", "condutor", "turista", "chapéu"],
    hors={"pega": ["a", "la poignée (de maintien)"]},
)

S["financas"] = dict(
    n=5, titre="Nas Finanças, o NIF", titre_fr="Aux impôts, le numéro fiscal",
    lieu="a Portuguese tax office open to the public on a September morning",
    qui="a visitor", camera="standing eye height from the entrance of the waiting room, looking across the rows of seats towards the counters",
    lumiere="Even white light from the ceiling panels and soft daylight from a high window",
    textures="plastic, painted metal, laminate, paper, glass, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the screens are dark, the display panel above the counters is plain black, the forms are plain white paper with grey lines, the chairs are plain grey plastic",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " sits on a chair of the first row, on the left of the middle, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; he has fallen fast asleep after the long wait, his head resting on the shoulder of the old man sitting next to him, his mouth a little open, a small paper ticket still between his fingers",
        "the old man beside him, in a grey jacket and a flat cap, sits very straight and wide awake, and looks down at the sleeping head on his shoulder with patient amusement",
        "on the chair beside him, his orange notebook and a pen",
        "a ticket machine of grey metal stands on a post at the left edge of the picture",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "rows of grey plastic chairs, where a young woman rocks a baby in a pram, and a man in a suit taps his foot",
        "on the right, a water fountain with a stack of paper cups",
    ]), ("THE COUNTERS, across the upper third of the picture", [
        "three counters behind glass partitions; at the middle one, a clerk with grey hair and glasses stamps a form for a woman in a red coat",
        "above the counters, the plain black display panel",
        "on the wall, a round white clock with a black rim and two black hands, and a tall green plant in a pot in the corner",
    ])],
    fin="The waiting room is calm and orderly: between the people, the same bare floor and the same bare white walls.",
    mots=["cadeira", "bilhete", "caderno", "caneta", "relógio", "funcionário", "balcão", "carrinho", "bebé", "vidro", "formulário", "máquina", "óculos", "casaco"],
    hors={"senha": ["a", "le ticket numéroté (d'attente)"]},
)

S["mercearia"] = dict(
    n=7, titre="Na mercearia", titre_fr="À l'épicerie",
    lieu="a small old corner grocery shop in the Graça district of Lisbon on a September evening",
    qui="a customer", camera="standing eye height from the shop door, looking towards the counter at the back",
    lumiere="Warm light from a bare bulb above the counter and the blue evening light from the door",
    textures="wood, cardboard, tin, glass, dried fish, fruit skins, paper, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the tins are plain colours with blank sides, the crates are plain unpainted wood, the fruit has plain unmarked skins, the paper bags are plain brown",
    vide="tiled floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "wooden crates of fruit and vegetables line the bottom of the picture: oranges, tomatoes, potatoes, onions and lettuces with plain unmarked skins",
        L + " stands in the middle, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; he holds in both arms a whole dried salt cod, stiff and flat as a wooden board, taller than he is, its tail above his head, and looks at it in disbelief",
        "on the right, a little grey cat sits on a sack of potatoes and watches him",
    ]), ("THE MIDDLE OF THE SHOP, from left to right", [
        "on the left, wooden shelves with tins of sardines in rows, bottles of olive oil and packets of rice",
        "in the centre, the old wooden counter with an old scale on it and a basket of eggs",
        "behind the counter, the grocer, a tall thin man of sixty in a grey work coat, holds out both hands as if to say: it's a whole one, what did you expect, with a big grin",
    ]), ("THE BACK OF THE SHOP, across the upper third of the picture", [
        "from a wooden beam above the counter hang three more whole dried salt cods and a bunch of garlic",
        "high shelves with bottles of wine and a calendar with a plain picture of the sea",
        "a bare light bulb hangs from the ceiling on its cord",
    ])],
    fin="The shop is small and full but tidy: between the things, the same bare tiled floor and the same bare wooden shelves.",
    mots=["bacalhau", "laranja", "tomate", "batata", "cebola", "alface", "gato", "sardinha", "azeite", "arroz", "balcão", "balança", "ovo", "vinho", "alho", "garrafa", "lata"],
    hors={"merceeiro": ["o", "l'épicier"]},
)

S["albergue"] = dict(
    n=8, titre="No albergue, o primeiro dia", titre_fr="À l'auberge, le premier jour",
    lieu="the reception of a youth hostel in the Alfama district of Lisbon on a sunny October morning",
    qui="a guest", camera="standing eye height from the hostel entrance, looking across the reception counter towards the back wall and the street door on the right",
    lumiere="Morning daylight from a tall open door and warm light from a lamp on the counter",
    textures="painted wood, old stone, glazed tiles, paper, metal keys, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the big city map on the wall is pale green and pale blue crossed by thin coloured lines with no words, the keys hang on plain wooden pegs, the backpacks are plain single colours, the screen is dark",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the wooden reception counter crosses the bottom of the picture, with a bell, a small lamp, a pile of folded towels and a jar of pens on it",
        L + " stands behind the counter, on the left of the middle, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; he points with great confidence to the right, towards the open street door, his chin up, very sure of himself",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "on the left, behind the young man, his colleague, a young man of twenty-nine with a thick black beard and a grey wool cardigan, waves both arms wildly in the opposite direction, to the left, his face in comic despair",
        "on the right, three young travellers with big backpacks walk obediently out of the open door, following the direction the young man shows",
        "a wooden bench with a guitar case lying on it",
    ]), ("THE BACK WALL, across the upper third of the picture", [
        "a big city map of Lisbon on the wall, with a red pin on the castle at the top left",
        "a board of wooden pegs where room keys hang",
        "a band of blue and white glazed tiles along the wall, and a ceiling fan above",
    ])],
    fin="The reception is cheerful and uncluttered: between the people, the same bare stone floor and the same bare white walls.",
    mots=["balcão", "mapa", "chave", "toalha", "candeeiro", "porta", "mochila", "banco", "parede", "azulejo", "castelo", "colega", "viajante", "caneta"],
    hors={"albergue": ["o", "l'auberge de jeunesse"], "receção": ["a", "la réception"]},
)

S["tasca"] = dict(
    n=9, titre="Na tasca", titre_fr="À la tasca",
    lieu="a small old family restaurant in Lisbon at lunchtime on an October weekday",
    qui="a diner", camera="sitting eye height from a neighbouring table, looking across the young man's table towards the kitchen door and the blackboard",
    lumiere="Daylight from the street window and warm light from wall lamps",
    textures="paper tablecloths, glazed earthenware, wood, glass, bread crust, olives, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the tablecloths are plain white paper, the plates are plain white earthenware, the blackboard shows only chalk drawings of a fish and a pig, the jug is plain white",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "a small square table with a white paper tablecloth crosses the bottom of the picture",
        "on it, the remains of a feast: an empty bread basket with crumbs, an empty dish with only olive stones, an empty little plate where butter was, a jug of red wine and a glass",
        L + " sits at the table on the left of the middle, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; he leans back in his chair, both hands on his full belly, satisfied, his cheeks round",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "on the left, an old couple eat grilled fish at the next table",
        "on the right, the waiter, a man of fifty in a white shirt and a black waistcoat, arrives carrying a big plate of grilled meat with rice and chips in one hand, and with the other hand he lays a small paper bill on the table, with a polite and very knowing smile",
    ]), ("THE BACK OF THE ROOM, across the upper third of the picture", [
        "a blackboard on the wall with chalk drawings of a fish and a pig",
        "the open kitchen door, with steam and a cook in a white hat at the stove",
        "a television high on the wall, its screen dark, and a framed photograph of a football team",
    ])],
    fin="The room is small and lively: between the tables, the same bare tiled floor and the same bare white walls.",
    mots=["mesa", "toalha", "pão", "cesto", "azeitona", "manteiga", "prato", "vinho", "copo", "empregado", "peixe", "carne", "arroz", "televisão", "fotografia", "cozinheiro", "conta", "cadeira"],
    hors={"tasca": ["a", "le petit restaurant populaire"], "couvert": ["o", "le couvert (pain, olives, beurre facturés)"], "quadro de giz": ["o", "le tableau noir (du menu)"]},
)

S["estendal"] = dict(
    n=10, titre="O estendal", titre_fr="Le linge étendu",
    lieu="a narrow sunny lane of the Graça district of Lisbon seen from a third-floor window on an October Saturday",
    qui="a neighbour", camera="the height of a third-floor window, looking down into the lane and across at the facades opposite",
    lumiere="Bright midday sunlight and sharp shadows across the lane",
    textures="glazed tiles, painted plaster, wrought iron, cotton laundry, wooden pegs, cobblestones and skin",
    refs=["leo", "leo-cote", "fernanda"],
    plain="the laundry is plain single-coloured cloth, the umbrella is plain black, the tiles of the facades are plain green and white squares",
    vide="wall or bare cobblestones",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the window sill of the young man's room crosses the bottom of the picture, with a laundry line stretched from it on two pulleys across the lane, laden with shirts, towels and socks held by wooden pegs",
        L + " leans out of his window on the left, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; one hand holds a wooden peg in the air, the other hand reaches down too late, his face frozen in horror",
    ]), ("THE LANE BELOW, from left to right", [
        "far below in the cobbled lane, a bald man in a cardigan walks under a big black umbrella against the sun; on top of his umbrella lies one royal-blue sock; he holds the sock up between two fingers at arm's length and looks up at the window with comic dignity",
        "a small white dog on a lead stops to sniff the air",
        "a scooter is parked against the wall",
    ]), ("THE FACADES, across the upper third of the picture", [
        "the facade opposite is covered in plain green and white tiles, with windows with green shutters and wrought-iron balconies full of flower pots with red geraniums",
        "at the window directly below the young man's, the landlady of the third reference picture leans out and laughs, her hand over her mouth, a yellow canary in its white cage hanging beside her window",
        "above the roofs, a strip of deep blue sky and a seagull",
    ])],
    fin="The lane is narrow and sunny: between the facades, the same bare cobblestones and the same strip of sky.",
    mots=["roupa", "janela", "toalha", "camisa", "meia", "guarda-chuva", "cão", "rua", "varanda", "vaso", "flor", "azulejo", "gaivota", "céu", "gaiola", "vizinho", "telhado", "mota"],
    hors={"estendal": ["o", "l'étendoir, le linge étendu"], "mola": ["a", "la pince à linge"], "canário": ["o", "le canari"], "corda": ["a", "la corde"]},
)

S["castanhas"] = dict(
    n=11, titre="As castanhas", titre_fr="Les châtaignes",
    lieu="a small square of Lisbon on a cool November evening around Saint Martin's day",
    qui="a passer-by", camera="standing eye height from the edge of the square, looking at the chestnut cart and the tram stop behind it",
    lumiere="The orange glow of street lamps and the blue evening sky",
    textures="black iron, coal, smoke, roasted chestnut shells, newspaper, wool, cotton, denim and skin",
    refs=["leo", "leo-cote", "beatriz"],
    plain="the paper cones are plain grey paper, the cart is plain black iron, the bags are plain single colours",
    vide="pavement or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the chestnut seller's black iron cart stands on the right of the middle, shaped like a little steam engine with a chimney, chestnuts roasting on the coals",
        "the seller, a man of seventy in a flat cap and a scarf, holds out a paper cone full of hot chestnuts",
        L + " stands just left of the cart, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; a great cloud of thick white smoke from the chimney has wrapped him completely, so that only his arm sticking out of the cloud is clearly seen, holding a paper cone of chestnuts",
    ]), ("THE MIDDLE OF THE SQUARE, from left to right", [
        "on the left, the waitress of the third reference picture, in a red wool coat, laughs and waves the smoke away with her hand",
        "a wooden bench with fallen yellow leaves under it",
        "a tram stop with a little glass shelter, an old couple waiting in it",
    ]), ("THE BACK OF THE SQUARE, across the upper third of the picture", [
        "old houses with lit windows and wrought-iron balconies",
        "a tall tree with yellow autumn leaves",
        "an old black iron street lamp glowing orange, and a deep blue evening sky",
    ])],
    fin="The square is calm and cosy: between the people, the same bare pavement and the same bare walls.",
    mots=["castanha", "fumo", "chaminé", "chapéu", "cachecol", "casaco", "banco", "folha", "árvore", "candeeiro", "paragem", "varanda", "casal", "jornal"],
    hors={"castanheiro": ["o", "le vendeur de châtaignes"], "cartucho": ["o", "le cornet de papier"]},
)

S["aula-portugues"] = dict(
    n=12, titre="Na aula de português", titre_fr="Au cours de portugais",
    lieu="a classroom of a Portuguese language school for foreigners in Lisbon on a November evening",
    qui="a student", camera="sitting eye height from the back row, looking towards the whiteboard and the teacher",
    lumiere="White ceiling lights and the dark blue evening in the windows",
    textures="laminate desks, plastic chairs, a whiteboard, paper, pens, cotton, wool, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the whiteboard is plain white with only two marker drawings on it, the books are plain single colours with blank covers, the posters are plain coloured rectangles",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "two desks in the first row of the picture; on the left one, an open orange notebook, a pen and a dictionary",
        L + " sits at the left desk, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; he leans towards his neighbour and argues with one finger raised, frowning",
        "at the right desk, his classmate, a young man of twenty-seven in a green cap and a yellow t-shirt, argues back with both hands open, frowning too",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "two more students watch them with amusement: an older woman with grey braids and a young man with round glasses",
        "a coat rack by the window with three coats and an umbrella",
    ]), ("THE FRONT OF THE CLASSROOM, across the upper third of the picture", [
        "the whiteboard, with two identical simple drawings of a city bus in blue marker, one on the left and one on the right, and a large blue equals sign between them",
        "the teacher, a woman of fifty with short grey hair and a bright yellow scarf, stands between the two drawings, arms crossed, eyebrows raised, waiting for them to finish",
        "a clock above the board and a map of Portugal and Brazil side by side on the wall, plain green shapes on plain blue",
    ])],
    fin="The classroom is small and bright: between the desks, the same bare floor and the same bare white walls.",
    mots=["mesa", "cadeira", "caderno", "caneta", "dicionário", "colega", "aluno", "aluna", "professora", "quadro", "relógio", "mapa", "janela", "casaco", "guarda-chuva", "autocarro", "cachecol", "boné"],
    hors={"cabide": ["o", "le portemanteau"]},
)

# ---------------------------------------------------------------- HIVER (A2)
S["mercado"] = dict(
    n=13, titre="No mercado", titre_fr="Au marché",
    lieu="the fish hall of a covered market in Lisbon on a December morning",
    qui="a shopper", camera="standing eye height in the aisle, looking along the fish stalls",
    lumiere="Cool daylight from the high glass roof and white lamps above the stalls",
    textures="crushed ice, fish scales, wet stone, steel, rubber aprons, paper, wool, denim and skin",
    refs=["leo", "leo-cote", "albano"],
    plain="the price signs are plain white cards with only numbers, the crates are plain white plastic, the aprons are plain colours",
    vide="wet stone floor",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the fish stall crosses the bottom of the picture: beds of crushed ice with sardines, a big sea bream, mackerel, an octopus and prawns, and a steel scale",
        L + " stands in front of the stall, on the left of the middle, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; he takes one startled step back, his hands raised, because the big sea bream on the ice stares at him with its round eye",
    ]), ("THE MIDDLE OF THE HALL, from left to right", [
        "behind the stall, the fishwife, a strong woman of fifty in a yellow rubber apron and rubber gloves, holds up a big fish by the tail and calls out with her mouth wide open",
        "on the right, the owner of the pastry shop of the third reference picture, a basket on his arm, laughs at the young man",
        "a woman with a shopping trolley chooses prawns",
    ]), ("THE HALL, across the upper third of the picture", [
        "rows of other stalls with fruit and vegetables",
        "the high iron roof with glass panels and a big round clock hanging from a beam",
        "seagulls perched on the iron beams",
    ])],
    fin="The hall is busy but orderly: between the stalls, the same bare wet stone floor.",
    mots=["peixe", "sardinha", "gelo", "polvo", "camarão", "balança", "avental", "luva", "cesto", "carrinho", "fruta", "relógio", "gaivota", "mercado", "preço", "cliente"],
    hors={"dourada": ["a", "la dorade"], "peixeira": ["a", "la poissonnière"], "carapau": ["o", "le chinchard"]},
)

S["consoada"] = dict(
    n=14, titre="A consoada", titre_fr="Le réveillon de Noël",
    lieu="the dining room of an old Lisbon apartment on Christmas Eve, during the family dinner",
    qui="a guest", camera="sitting eye height from the end of the table, looking along it towards the window and the Christmas tree",
    lumiere="Warm light from a chandelier and candles on the table, the night blue in the window",
    textures="white linen, china, glass, salt cod, cabbage, a cake with candied fruit, wood, wool, cotton and skin",
    refs=["leo", "leo-cote", "fernanda"],
    plain="the tablecloth is plain white linen, the plates are plain white china, the tablet screen shows only the face of an old smiling woman, the paper crowns are plain gold",
    vide="tablecloth or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the long table crosses the bottom of the picture: a big dish of boiled salt cod with potatoes, cabbage and eggs, a jug of olive oil, glasses of wine, and in the middle a big ring-shaped cake decorated with candied fruit, one slice cut",
        L + " sits on the left side of the table, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; he holds up between two fingers a small dried broad bean he has just found in his slice of cake, his face torn between pride and worry",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "around the table, the family applauds and laughs: the landlady of the third reference picture at the head of the table, her son and his wife, and two teenage grandchildren",
        "on the table near the young man, a tablet leans against the jug, its screen showing the face of an old smiling woman with grey hair waving from far away",
        "a sleeping cat on a chair",
    ]), ("THE BACK OF THE ROOM, across the upper third of the picture", [
        "a Christmas tree with plain red and gold balls and lights, and a nativity scene on a small table",
        "a window with lace curtains and the night outside",
        "the yellow canary in its white cage on top of a cupboard",
    ])],
    fin="The room is warm and crowded but each person sits clearly on their own: between them, the same bare white tablecloth and the same bare walls.",
    mots=["bacalhau", "batata", "couve", "ovo", "azeite", "vinho", "copo", "bolo", "mesa", "toalha", "prato", "árvore", "vela", "janela", "cortina", "gato", "gaiola", "família", "neto", "neta"],
    hors={"bolo-rei": ["o", "la galette des rois portugaise"], "fava": ["a", "la fève"], "presépio": ["o", "la crèche"], "consoada": ["a", "le réveillon de Noël"], "tablet": ["o", "la tablette"]},
)

S["passagem-de-ano"] = dict(
    n=15, titre="A passagem de ano", titre_fr="Le Nouvel An",
    lieu="the great riverside square of Lisbon at midnight on New Year's Eve, under the fireworks",
    qui="someone in the crowd", camera="standing eye height in the crowd, looking across the square towards the triumphal arch and the river",
    lumiere="The bursting colours of fireworks and the golden light of the arcades",
    textures="stone paving, glass, paper, wool coats, scarves, cotton and skin",
    refs=["leo", "leo-cote", "fernanda"],
    plain="the little bags of raisins are plain paper, the coats are plain colours, the bottles are plain glass",
    vide="paving",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands on the left of the middle, a dark-grey wool coat open over his sweatshirt, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; his cheeks are puffed out like a hamster's, full of raisins, and he tries to smile and speak at the same time, a little paper bag of raisins in his hand",
        "beside him on the right, the landlady of the third reference picture, in a black coat and a red scarf, eats her raisins one by one very calmly, counting on her fingers",
    ]), ("THE MIDDLE OF THE SQUARE, from left to right", [
        "the crowd: people in coats raise glasses of sparkling wine, a couple kisses, a father carries a small girl on his shoulders",
        "a young man in a woolly hat holds up a phone to film the fireworks",
    ]), ("THE BACK, across the upper third of the picture", [
        "the great triumphal arch of the square and its yellow arcades",
        "above the river, fireworks burst in gold, red and green in the black sky",
        "the dark river with the lights of the bridge in the distance",
    ])],
    fin="The square is full and joyful, but the people in front stand clearly on their own, with bare paving around their feet.",
    mots=["saco", "casaco", "cachecol", "copo", "garrafa", "praça", "arco", "rio", "ponte", "fogo", "céu", "gorro", "telemóvel", "multidão"],
    hors={"passas": ["as", "les raisins secs (douze, aux douze coups)"], "fogo de artifício": ["o", "le feu d'artifice"], "espumante": ["o", "le vin mousseux"]},
)

S["chuva"] = dict(
    n=16, titre="A chuva", titre_fr="La pluie",
    lieu="a steep shopping street of Lisbon paved with black and white stones on a rainy January afternoon",
    qui="a passer-by", camera="standing eye height in the middle of the sloping street, looking up it",
    lumiere="Grey rainy daylight and the warm glow of shop windows on the wet stones",
    textures="wet black and white paving stones, umbrellas, raincoats, glass shop windows, cotton, rubber and skin",
    refs=["leo", "leo-cote", "beatriz"],
    plain="the umbrellas are plain single colours, the shop windows show plain goods without signs, the raincoats are plain colours",
    vide="wet paving",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the wet pavement of small black and white stones, shining with puddles",
        L + " stands on the left of the middle, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; his black umbrella has been turned inside out by the wind, its ribs sticking up, and he holds it up looking at it in dismay, his hair dripping",
        "on the right, a small old lady in a plastic rain hat and shiny red rubber boots walks up the slope past him, perfectly calm, pulling a shopping trolley",
    ]), ("THE MIDDLE OF THE STREET, from left to right", [
        "in a shop doorway on the left, the waitress of the third reference picture, in a yellow raincoat, laughs and holds out her own umbrella towards him",
        "people pass under umbrellas of red, green and blue",
        "a lit shoe shop window and a lit bookshop window",
    ]), ("THE TOP OF THE STREET, across the upper third of the picture", [
        "the street climbs between old pastel facades with iron balconies",
        "a yellow tram waits at the top of the slope",
        "a heavy grey sky and slanting rain",
    ])],
    fin="The street is wet and grey but each person stands clearly on their own: between them, the same bare shining paving.",
    mots=["chuva", "guarda-chuva", "impermeável", "bota", "carrinho", "montra", "sapataria", "livraria", "rua", "elétrico", "céu", "vento", "poça", "chapéu"],
    hors={"calçada": ["a", "le pavé portugais"]},
)

S["fado"] = dict(
    n=17, titre="Na casa de fado", titre_fr="Dans la maison de fado",
    lieu="a small fado house in the Alfama district of Lisbon on a Sunday night, during a song",
    qui="a guest", camera="sitting eye height from one of the tables, looking across the room towards the singer and the musicians",
    lumiere="Dim warm candlelight on the tables and a soft lamp on the singer",
    textures="stone walls, dark wood, candle wax, glass, wine, the wood of guitars, wool, cotton and skin",
    refs=["leo", "leo-cote", "rui"],
    plain="the tablecloths are plain red and white checks, the bottles are plain dark glass, the walls are plain whitewashed stone",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "a small table with a red and white checked cloth, a candle in a bottle, two glasses of red wine",
        L + " sits at it on the left, seen from his head down to his waist; his body is turned in three-quarter view towards the right of the picture; he leans towards the woman at the next table, his hand beside his mouth, caught in the middle of whispering",
    ]), ("THE MIDDLE OF THE ROOM, from left to right", [
        "every other guest at the small tables has turned round towards the young man, each with one finger on the lips; an old lady glares at him over her glasses",
        "a waiter has stopped in the middle of the room, a tray in his hand, his finger on his lips too",
    ]), ("THE BACK OF THE ROOM, across the upper third of the picture", [
        "the singer of the third reference picture stands with his eyes closed and a black shawl over his shoulders, singing with all his heart",
        "beside him, two musicians on chairs: one plays a round Portuguese guitar with twelve strings, the other a classical guitar",
        "the whitewashed stone vault, an old lantern on the wall, and a framed portrait of a woman in a black shawl",
    ])],
    fin="The room is small and quiet: between the tables, the same bare stone floor and the same bare whitewashed walls.",
    mots=["fado", "mesa", "toalha", "vela", "garrafa", "copo", "vinho", "músico", "empregado", "bandeja", "xaile", "parede", "candeeiro", "quadro"],
    hors={"guitarra portuguesa": ["a", "la guitare portugaise"], "viola": ["a", "la guitare classique (au Portugal)"], "fadista": ["o", "le chanteur de fado"]},
)

S["elevador"] = dict(
    n=18, titre="No elevador da Bica", titre_fr="Au funiculaire de la Bica",
    lieu="a steep narrow street of Lisbon where a small old yellow funicular climbs on its rails, on a cold February morning",
    qui="a neighbour", camera="standing eye height at the bottom of the street, looking up the rails",
    lumiere="Pale winter sunlight between the houses",
    textures="yellow painted metal, steel rails, cobblestones, old plaster, iron balconies, wool, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the funicular is plain yellow with white roof, the facades are plain pastel plaster, the laundry is plain colours",
    vide="cobblestones or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the two steel rails run up the middle of the cobbled street from the bottom edge",
        L + " runs up the street beside the rails on the left of the middle, seen whole from his head to his white sneakers, his back half turned to us, his body in three-quarter view towards the right of the picture; he is out of breath, one arm stretched out towards the funicular",
    ]), ("THE MIDDLE OF THE STREET, from left to right", [
        "the small yellow funicular car stands still on the rails just ahead of him, its doors open and its passengers seated",
        "the driver in a dark-blue uniform leans out of the open door with his chin on his hand, waiting patiently with a bored, amused face",
        "a cat sits on a doorstep on the right",
    ]), ("THE TOP OF THE STREET, across the upper third of the picture", [
        "the narrow street rises steeply between pastel houses with iron balconies and laundry",
        "at the very top, a glimpse of the river shining in the sun",
        "a pale winter sky",
    ])],
    fin="The street is narrow and steep: between the people, the same bare cobblestones and the same bare walls.",
    mots=["rua", "carril", "porta", "condutor", "uniforme", "passageiro", "gato", "varanda", "roupa", "rio", "céu", "casa", "degrau"],
    hors={"elevador": ["o", "le funiculaire (à Lisbonne)"], "ascensor": ["o", "le funiculaire"]},
)

S["cacilheiro"] = dict(
    n=19, titre="No cacilheiro", titre_fr="Dans le bac de Cacilhas",
    lieu="the open upper deck of the orange ferry that crosses the river from Lisbon to Cacilhas on a windy February afternoon",
    qui="a passenger", camera="standing eye height at the back of the deck, looking across it towards the city on the far bank",
    lumiere="Bright winter sunlight and sparkling water",
    textures="painted steel, wooden benches, ropes, water, bread, wool, denim and skin",
    refs=["leo", "leo-cote", "rui"],
    plain="the ferry is plain orange and white, the benches are plain wood, the life rings are plain orange",
    vide="deck",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands on the left of the middle by the rail, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; his hands are still raised, open and empty, at the height of his mouth, and his mouth is open wide in shock",
        "a big seagull flies off just above his hands with his whole pork sandwich in its beak",
        "beside him on the right, the bearded colleague of the third reference picture bites into his own sandwich, laughing so hard he nearly chokes",
    ]), ("THE MIDDLE OF THE DECK, from left to right", [
        "wooden benches where passengers sit: a woman reading, a boy with a bicycle",
        "an orange life ring on the rail and coiled ropes",
    ]), ("THE RIVER, across the upper third of the picture", [
        "the wide sparkling river and, on the far bank, the city of Lisbon on its hills with the castle on top",
        "on the right, the long red suspension bridge",
        "other seagulls in a blue sky",
    ])],
    fin="The deck is open and windy: between the people, the same bare painted deck.",
    mots=["barco", "gaivota", "sandes", "banco", "corda", "bicicleta", "rio", "cidade", "castelo", "ponte", "céu", "passageiro", "colega"],
    hors={"cacilheiro": ["o", "le bac de Cacilhas"], "bifana": ["a", "le sandwich au porc"], "boia": ["a", "la bouée"]},
)

S["metro-azulejos"] = dict(
    n=20, titre="No metro", titre_fr="Dans le métro",
    lieu="the entrance hall of an old Lisbon metro station whose walls are covered with blue and white tiles, on a February morning",
    qui="a commuter", camera="standing eye height in front of the ticket gates, looking across them towards the escalator",
    lumiere="Even white light from the ceiling",
    textures="glazed tiles, brushed steel, glass, plastic cards, wool coats, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the tiles are plain blue and white with simple waves and fish drawn on them, the cards are plain green, the screens are dark",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "a row of steel ticket gates crosses the bottom of the picture, with glass flaps",
        L + " stands at the left gate, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; he presses a green card on the reader for the third time, the glass flaps stay shut, and he looks at the card in disbelief",
        "at the next gate, a girl of eight with a school bag taps her card with a big smile and walks straight through the open flaps",
    ]), ("THE MIDDLE OF THE HALL, from left to right", [
        "a ticket machine against the wall on the left",
        "commuters in coats walk towards the escalator; a man with a briefcase, a woman with a coffee",
    ]), ("THE BACK OF THE HALL, across the upper third of the picture", [
        "the walls covered in blue and white tiles drawn with waves, fish and boats",
        "the escalator going down, with people on it",
        "a station clock hanging from the ceiling",
    ])],
    fin="The hall is bright and orderly: between the people, the same bare floor and the same tiled walls.",
    mots=["metro", "bilhete", "cartão", "azulejo", "máquina", "pasta", "café", "relógio", "escada", "criança", "mochila", "peixe", "barco"],
    hors={"torniquete": ["o", "le tourniquet"], "escada rolante": ["a", "l'escalier mécanique"]},
)

# ---------------------------------------------------------------- PRINTEMPS (A2 -> B1)
S["25-de-abril"] = dict(
    n=21, titre="O 25 de Abril", titre_fr="Le 25 avril",
    lieu="the great avenue of Lisbon on the 25th of April, during the parade for the Carnation Revolution",
    qui="someone in the crowd", camera="standing eye height on the pavement, looking along the avenue",
    lumiere="Bright spring sunshine through the trees",
    textures="red carnations, cloth banners, stone pavement, leaves, cotton, denim and skin",
    refs=["leo", "leo-cote", "beatriz"],
    plain="the banners are plain red cloth, the flags are the plain green and red Portuguese flag, the balloons are plain red",
    vide="pavement",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands on the left of the middle, in his sweatshirt, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; he holds a single red carnation in both hands, moved, with a gentle smile",
        "beside him, the waitress of the third reference picture holds the arm of her grandmother, a tiny old lady of ninety in a black coat, who has just given him the carnation and pats his hand",
    ]), ("THE MIDDLE OF THE AVENUE, from left to right", [
        "the parade walks down the avenue: people of all ages carrying red carnations, a man with a carnation in his buttonhole, children on their parents' shoulders",
        "plain red banners and green and red flags",
    ]), ("THE AVENUE, across the upper third of the picture", [
        "the wide avenue lined with tall plane trees in fresh spring leaves",
        "old buildings with balconies where people lean out",
        "a clear blue sky",
    ])],
    fin="The avenue is full but each person in front stands clearly on their own, with bare pavement around their feet.",
    mots=["cravo", "flor", "bandeira", "avenida", "árvore", "varanda", "avó", "neta", "criança", "multidão", "céu", "casaco"],
    hors={"desfile": ["o", "le défilé"], "faixa": ["a", "la banderole"]},
)

S["feira-da-ladra"] = dict(
    n=22, titre="Na Feira da Ladra", titre_fr="Au marché aux puces",
    lieu="the open-air flea market of Lisbon on a sunny April Saturday morning",
    qui="a shopper", camera="standing eye height in an alley between the stalls",
    lumiere="Bright spring sunlight and the shade of trees",
    textures="old tiles, worn leather, brass, wood, cloth spread on the ground, paper, cotton, denim and skin",
    refs=["leo", "leo-cote", "lucas"],
    plain="the old tiles are plain blue on white with simple flowers, the old books have plain worn covers, the cloths on the ground are plain colours",
    vide="ground",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "a cloth spread on the ground with old things laid out: tiles, keys, an old radio, brass candlesticks, records and a pair of boots",
        L + " crouches on the left, seen whole; his body is turned in three-quarter view towards the right of the picture; he holds up proudly in both hands an old blue and white tile panel showing a painted yellow canary in a cage, beaming",
        "his classmate of the third reference picture stands beside him and haggles with the seller, three fingers raised",
    ]), ("THE MIDDLE OF THE MARKET, from left to right", [
        "the seller, a big man with a cigarette behind his ear, sitting on a folding chair under a parasol",
        "other stalls with old clothes on hangers, a mirror and an old bicycle",
    ]), ("THE BACK, across the upper third of the picture", [
        "a large white church with a dome above the market",
        "trees with fresh green leaves",
        "a blue spring sky",
    ])],
    fin="The market is lively but each thing lies clearly on its own: between the stalls, the same bare dusty ground.",
    mots=["azulejo", "chave", "rádio", "disco", "bota", "espelho", "bicicleta", "cadeira", "igreja", "árvore", "céu", "vendedor", "preço", "canário"],
    hors={"feira": ["a", "la foire, le marché"], "castiçal": ["o", "le chandelier"], "guarda-sol": ["o", "le parasol"]},
)

S["sintra"] = dict(
    n=23, titre="Em Sintra", titre_fr="À Sintra",
    lieu="the terrace in front of the colourful palace of Pena on its hilltop near Sintra, on a foggy April morning",
    qui="a tourist", camera="standing eye height on the terrace, facing the palace",
    lumiere="Soft white fog light",
    textures="stone, fog, moss, ironwork, cotton, denim and skin",
    refs=["leo", "leo-cote"],
    plain="the fog is plain white, the umbrellas are plain colours, the tourist's camera is plain black",
    vide="paving",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands in the middle, seen whole from his head to his white sneakers, facing the camera; he poses with his arms spread wide and a huge proud smile, presenting the palace behind him",
        "a tourist couple stands on the right, one of them taking his picture with a phone, the other covering her mouth to keep from laughing",
    ]), ("THE MIDDLE OF THE TERRACE, from left to right", [
        "a stone wall with a low iron railing",
        "a bench wet with fog, and a stone statue of a lion",
    ]), ("THE BACK, across the upper third of the picture", [
        "behind him, nothing but a thick white wall of fog: of the palace only the very tip of one yellow tower appears faintly at the top of the picture",
        "dark green trees fading into the fog at the edges",
    ])],
    fin="The terrace is quiet and white: between the people, the same bare stone paving and the same white fog.",
    mots=["palácio", "nevoeiro", "torre", "muro", "banco", "turista", "árvore", "telemóvel", "leão", "casal"],
    hors={"estátua": ["a", "la statue"]},
)

S["futebol-cafe"] = dict(
    n=24, titre="O jogo no café", titre_fr="Le match au café",
    lieu="the same small pastry shop of the reference picture in the evening, during the football derby on television",
    qui="a customer", camera="standing eye height near the door, looking along the counter towards the television high on the wall",
    lumiere="Warm light from the round lamps and the flickering light of the television",
    textures="marble, glass, chrome, glazed tiles, scarves, beer glasses, cotton and skin",
    refs=["leo", "leo-cote", "lieu-pastelaria", "albano"],
    plain="the scarves are plain red or plain green, the television screen shows only a green football pitch with small players, the glasses are plain",
    vide="floor or bare wall",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the end of the marble counter on the right, with glasses of beer, a plate of small fried snacks and a bowl of lupin beans",
        L + " stands alone, on the left of the middle, seen from his head down to his knees, a plain green scarf around his neck; his body is turned in three-quarter view towards the right of the picture; he jumps up with both arms raised, cheering a goal at the top of his voice",
    ]), ("THE MIDDLE OF THE SHOP, from left to right", [
        "everyone else in the shop wears a plain red scarf and has frozen in silent dismay, turning slowly to look at him: the owner of the fourth reference picture behind the counter with a towel over his shoulder, an old man in a flat cap, two young men with beers",
    ]), ("THE BACK OF THE SHOP, across the upper third of the picture", [
        "a television high on the tiled wall, showing a green football pitch",
        "the shelves of bottles and cups and the clock, as in the reference picture",
    ])],
    fin="The shop is crowded but each person stands clearly on their own: between them, the same bare floor and the same tiled walls.",
    mots=["televisão", "cachecol", "cerveja", "copo", "balcão", "prato", "taça", "toalha", "jogo", "golo", "garrafa", "relógio", "boné"],
    hors={"tremoço": ["o", "le lupin (graine)"], "dérbi": ["o", "le derby"], "adepto": ["o", "le supporter"]},
)

S["santos-populares"] = dict(
    n=25, titre="Os Santos Populares", titre_fr="La fête des saints populaires",
    lieu="a little square of the Alfama district of Lisbon on the night of the 12th of June, during the street festival of Saint Anthony",
    qui="a reveller", camera="standing eye height at the edge of the square, looking across it towards the grill and the dancers",
    lumiere="Colourful paper garlands lit by strings of bulbs, and the orange glow of the grill",
    textures="paper garlands, smoke, grilled sardines, bread, basil plants, cobblestones, cotton, denim and skin",
    refs=["leo", "leo-cote", "fernanda", "beatriz"],
    plain="the paper garlands are plain bright colours, the little flags are plain colours, the paper plates are plain white",
    vide="cobblestones",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands on the left of the middle, in his white t-shirt, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; he holds a grilled sardine on a slice of bread in one hand, grease dripping, and a small pot of basil in the other, and looks around helplessly for somewhere to put one of them down",
        "beside him, the waitress of the fourth reference picture laughs and offers him a paper napkin",
    ]), ("THE MIDDLE OF THE SQUARE, from left to right", [
        "the landlady of the third reference picture dances joyfully with an old man in a flat cap, her arms raised",
        "a man grills sardines on a big smoking charcoal grill",
        "long wooden tables with paper plates, jugs of wine and small pots of basil with paper flowers on them",
    ]), ("THE TOP OF THE PICTURE, across the upper third", [
        "paper garlands and strings of bulbs criss-cross the square between the old houses",
        "windows and balconies with people leaning out",
        "a dark blue night sky",
    ])],
    fin="The square is full and festive but each person stands clearly on their own: between them, the same bare cobblestones.",
    mots=["sardinha", "pão", "guardanapo", "prato", "vinho", "mesa", "fumo", "varanda", "janela", "praça", "festa", "noite", "lâmpada", "bandeira"],
    hors={"manjerico": ["o", "le petit pot de basilic (fête de saint Antoine)"], "grelha": ["a", "le gril"], "arraial": ["o", "la fête de quartier"], "fita": ["a", "la guirlande"]},
)

# ---------------------------------------------------------------- ETE (B1)
ETE = "only his white t-shirt, the cream scarf with small blue embroidered flowers, light-grey shorts and his white canvas sneakers, and his royal-blue sweatshirt is tied around his waist by its sleeves"

S["praia-surf"] = dict(
    n=26, titre="Na Costa da Caparica", titre_fr="À la plage de Caparica",
    lieu="a long sandy beach on the Atlantic south of Lisbon on a sunny July morning, during a surf lesson",
    qui="a friend on the beach", camera="standing eye height at the edge of the water, looking out to sea",
    lumiere="Bright summer sunlight and sparkling foam",
    textures="wet sand, foam, surfboards, wetsuits, skin and sun",
    refs=["leo", "leo-cote"], ete="a black wetsuit",
    plain="the surfboards are plain white or plain yellow, the wetsuits are plain black, the umbrellas are plain colours",
    vide="sand or bare water",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "the wet sand and the edge of the foam",
        "the surf teacher, a sunburnt woman with a whistle around her neck, stands in the shallow water and holds her forehead in her hand",
    ]), ("THE MIDDLE OF THE PICTURE, the waves, from left to right", [
        "four students stand proudly upright on their white boards, riding a small wave",
        "in the middle of them, " + L + ", in a black wetsuit, lies flat on his stomach on a yellow board, his arms around it, and waves at the camera with one hand, grinning",
    ]), ("THE BACK, across the upper third of the picture", [
        "the blue Atlantic and more small waves",
        "a red and white lifeguard tower on the beach on the right, with a flag",
        "a clear blue sky with a few seagulls",
    ])],
    fin="The beach is wide and open: between the people, the same bare water and the same bare sand.",
    mots=["praia", "areia", "onda", "mar", "prancha", "professora", "apito", "bandeira", "gaivota", "céu", "sol"],
    hors={"fato de surf": ["o", "la combinaison de surf"], "nadador-salvador": ["o", "le sauveteur"]},
)

S["comboio-cascais"] = dict(
    n=27, titre="No comboio para Cascais", titre_fr="Dans le train de Cascais",
    lieu="the inside of a suburban train running along the sea from Lisbon to Cascais on a sunny July afternoon",
    qui="a passenger", camera="sitting eye height from the seat across the aisle",
    lumiere="Bright sunlight through the windows and the blue glitter of the sea",
    textures="plastic seats, glass, paper, ink, cotton and skin",
    refs=["leo", "leo-cote"], ete=ETE,
    plain="the seats are plain blue, the notebook pages are plain cream with lines of handwriting too small to read",
    vide="seat or bare window",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " sits by the window on the left, seen from his head down to his knees; his body is turned in three-quarter view towards the right of the picture; he writes in his open orange notebook on his knees, frowning with concentration, a pen in his hand",
        "opposite him, an old man in a straw hat and a white shirt leans forward and points with one finger at a word in the notebook, kindly correcting it, while the young man looks up at him, surprised and grateful",
    ]), ("THE MIDDLE OF THE CARRIAGE, from left to right", [
        "other passengers: a girl with headphones, a mother with a beach bag and a child with a bucket and spade",
    ]), ("THE WINDOWS, across the upper third of the picture", [
        "through the large windows, the sea glitters right beside the track, with a lighthouse and a fort on the shore",
        "a clear summer sky",
    ])],
    fin="The carriage is calm and bright: between the people, the same bare floor and the same bare windows.",
    mots=["comboio", "janela", "caderno", "caneta", "chapéu", "camisa", "auscultadores", "balde", "pá", "saco", "mar", "farol", "céu"],
    hors={"forte": ["o", "le fort"]},
)

S["acores"] = dict(
    n=28, titre="Em São Miguel", titre_fr="À São Miguel, aux Açores",
    lieu="the steaming volcanic ground of Furnas on the island of São Miguel in the Azores on an August morning, where pots of stew are cooked underground",
    qui="a visitor", camera="standing eye height at the edge of the cooking holes, looking across them towards the green hills",
    lumiere="Soft morning light through drifting steam",
    textures="steaming earth, iron pots, ropes, wood, green grass, cotton, denim and skin",
    refs=["leo", "leo-cote"], ete=ETE,
    plain="the pots are plain dark iron, the cloth bags are plain white",
    vide="earth or bare grass",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        "steaming holes in the earth covered by little mounds, each marked with a wooden stake",
        "two men in work clothes pull a big iron pot out of the ground with ropes, in a cloud of steam",
        L + " stands on the left of the middle, seen whole; his body is turned in three-quarter view towards the right of the picture; he listens with a gentle, moved smile",
        "beside him, a small old woman of seventy-nine in a black cardigan, leaning on a walking stick, holds his arm and talks to him warmly",
    ]), ("THE MIDDLE OF THE PICTURE, from left to right", [
        "a wooden table with plates and a basket of bread waiting for the stew",
        "a few other families waiting for their pots",
    ]), ("THE BACK, across the upper third of the picture", [
        "green hills with hydrangea hedges of blue flowers",
        "a calm crater lake below the hills",
        "a pale sky with soft clouds",
    ])],
    fin="The place is calm and green: between the people, the same bare earth and the same drifting steam.",
    mots=["panela", "terra", "vapor", "corda", "mesa", "prato", "pão", "cesto", "bengala", "avó", "tia", "lago", "colina", "flor", "céu"],
    hors={"cozido": ["o", "le pot-au-feu"], "hortênsia": ["a", "l'hortensia"], "caldeira": ["a", "la source chaude (volcanique)"]},
)

S["despedida"] = dict(
    n=29, titre="A despedida", titre_fr="Le départ, la fête",
    lieu="the rooftop terrace of the youth hostel in the Alfama district of Lisbon on an August evening, during a farewell party",
    qui="a friend", camera="standing eye height on the terrace, looking across it towards the river",
    lumiere="The golden light of the setting sun and strings of small bulbs",
    textures="terracotta tiles, wooden crates, plastic chairs, glasses, cake, cotton and skin",
    refs=["leo", "leo-cote", "rui", "beatriz"], ete="his white t-shirt, the cream scarf with small blue embroidered flowers, his dark-blue jeans and his white canvas sneakers",
    plain="the sweatshirt is plain red, the cake is plain white, the bunting is plain colours",
    vide="terracotta floor",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands in the middle, seen from his head down to his knees, facing the camera; laughing, he lets the bearded colleague of the third reference picture pull a plain red hooded sweatshirt over his head, on top of his royal-blue one",
        "the waitress of the fourth reference picture holds a cake with one candle and laughs",
    ]), ("THE MIDDLE OF THE TERRACE, from left to right", [
        "a young man in a green cap claps his hands",
        "a table of wooden crates with glasses, bottles and a bowl of crisps",
        "plastic chairs and a guitar leaning against the wall",
    ]), ("THE BACK, across the upper third of the picture", [
        "the terracotta roofs of Alfama tumbling down towards the river",
        "the river shining gold, and a big white ship",
        "an orange evening sky",
    ])],
    fin="The terrace is joyful and open: between the people, the same bare terracotta floor and the whole city beyond.",
    mots=["bolo", "vela", "copo", "garrafa", "cadeira", "mesa", "guitarra", "rio", "navio", "céu", "camisola", "festa", "amigo", "amiga"],
    hors={"terraço": ["o", "la terrasse sur le toit"], "caixote": ["o", "la caisse en bois"]},
)

S["aeroporto-partida"] = dict(
    n=30, titre="A partida", titre_fr="Le départ",
    lieu="the same baggage hall of Lisbon airport as in the third reference picture, at the end of August",
    qui="a traveller", camera="standing eye height from beside the baggage belt, looking across the hall towards the exit doors",
    lumiere="Bright late-summer daylight from the windows",
    textures="polished stone floor, rubber, steel, glass, a birdcage, cotton, denim and skin",
    refs=["leo", "leo-cote", "lieu-aeroporto", "fernanda"],
    plain="the screens are dark, the suitcases are plain single colours, the clothes are plain cloth",
    vide="polished floor",
    bandes=[("THE FOREGROUND, along the bottom of the picture", [
        L + " stands on the left of the middle with his bright grass-green suitcase, seen whole from his head to his white sneakers; his body is turned in three-quarter view towards the right of the picture; he leans towards a newly arrived young traveller and corrects him with one finger raised and a proud, teacherly smile",
        "the newly arrived traveller, a young man with a big backpack and a plain red tuque, looks lost and nods",
    ]), ("THE MIDDLE OF THE HALL, from left to right", [
        "the landlady of the fourth reference picture stands beside them with tears in her eyes, holding up her yellow canary in its little white cage, as if the bird too had come to say goodbye",
        "the grey seats and the clock, as in the reference picture",
    ]), ("THE BACK OF THE HALL, across the upper third of the picture", [
        "the tall windows and a white airplane on the airfield",
        "the open exit doors",
    ])],
    fin="The hall is calm and bright: between the people, the same bare polished floor.",
    mots=["aeroporto", "mala", "mochila", "gaiola", "cadeira", "relógio", "janela", "avião", "porta", "viajante", "gorro"],
    hors={"canário": ["o", "le canari"]},
)

# Le pilote, deja paye (prompts ecrits a la main) : decrit ici pour references.json et mots-prevus.json.
PILOTE = {
    "aeroporto-lisboa": dict(n=1, titre="No aeroporto", titre_fr="À l'aéroport", refs=["leo", "leo-cote"],
        mots=["aeroporto", "mala", "telemóvel", "lenço", "camisola", "criança", "boné", "carrinho", "mulher", "jornal", "cadeira", "senhor", "relógio", "porta", "flor", "janela", "avião", "táxi", "céu", "bagagem"],
        hors={"tapete rolante": ["o", "le tapis à bagages"]}),
    "casa-graca": dict(n=3, titre="Em casa da Dona Fernanda", titre_fr="Chez Dona Fernanda", refs=["leo", "leo-cote"],
        mots=["mala", "tapete", "cadeira", "gato", "azulejo", "escada", "degrau", "porta", "campainha", "chave", "avental", "gaiola", "caixa de correio", "janela", "vaso", "flor", "quadro", "candeeiro", "telhado"],
        hors={"canário": ["o", "le canari"], "corrimão": ["o", "la rampe"], "senhoria": ["a", "la propriétaire (logeuse)"]}),
    "pastelaria": dict(n=4, titre="Na pastelaria", titre_fr="À la pastelaria", refs=["leo", "leo-cote"],
        mots=["pastel de nata", "bolo", "pão", "montra", "balcão", "bica", "chávena", "açúcar", "colher", "guardanapo", "prato", "galão", "copo", "máquina", "garrafa", "relógio", "jornal", "sumo", "elétrico", "óculos", "bigode", "avental", "empregada", "lápis", "caixa"],
        hors={"pastelaria": ["a", "la pâtisserie-café"], "pires": ["o", "la soucoupe"], "banco alto": ["o", "le tabouret de bar"]}),
    "miradouro": dict(n=6, titre="No miradouro", titre_fr="Au belvédère", refs=["leo", "leo-cote"],
        mots=["escada", "árvore", "banco", "casal", "músico", "cão", "muro", "candeeiro", "gaivota", "castelo", "igreja", "rio", "barco", "ponte", "céu", "sol", "saco", "cidade", "senhora"],
        hors={"miradouro": ["o", "le belvédère"], "guitarra": ["a", "la guitare"], "telhado": ["o", "le toit"], "alho-francês": ["o", "le poireau"]}),
}

# Les mots des scenes absents du corpus portugais (verifie le 1er nov. 2026 : le corpus, derive de la liste
# allemande, n'a ni « mar » ni « lago ») : ils passent dans hors_corpus, a ajouter au corpus avant que la
# scene soit jouable. Un mot absent qui n'est pas ici arrete le script.
TRAD = {
    "telhado": ["o", "le toit"], "senhora": ["a", "la dame"], "alface": ["a", "la laitue"], "alho": ["o", "l'ail"],
    "lata": ["a", "la boîte de conserve"], "viajante": ["o", "le voyageur"], "castanha": ["a", "la châtaigne"],
    "fumo": ["o", "la fumée"], "chaminé": ["a", "la cheminée"], "folha": ["a", "la feuille"],
    "dicionário": ["o", "le dictionnaire"], "professora": ["a", "la professeure"], "polvo": ["o", "la pieuvre"],
    "camarão": ["o", "la crevette"], "couve": ["a", "le chou"], "vela": ["a", "la bougie"],
    "multidão": ["a", "la foule"], "impermeável": ["o", "l'imperméable"], "sapataria": ["a", "le magasin de chaussures"],
    "xaile": ["o", "le châle"], "carril": ["o", "le rail"], "cravo": ["o", "l'œillet"], "rádio": ["o", "la radio"],
    "vendedor": ["o", "le vendeur"], "canário": ["o", "le canari"], "palácio": ["o", "le palais"], "torre": ["a", "la tour"],
    "taça": ["a", "le bol"], "golo": ["o", "le but"], "lâmpada": ["a", "l'ampoule"], "mar": ["o", "la mer"],
    "prancha": ["a", "la planche (de surf)"], "panela": ["a", "la marmite"], "terra": ["a", "la terre"],
    "lago": ["o", "le lac"], "guitarra": ["a", "la guitare"], "amiga": ["a", "l'amie"],
}


def corpus():
    d = json.load(io.open(os.path.join(RACINE, "portugais", "datos", "themes.json"), encoding="utf-8"))
    return {m["mot"] for t in d["themes"] for m in t["mots"]}


def ranger_mots(s, connus):
    """mots du corpus d'un cote, mots a ajouter de l'autre, quel que soit l'endroit ou la scene les range."""
    hors = dict(s["hors"])
    mots = []
    for w in s["mots"]:
        if w in connus:
            mots.append(w)
        elif w in TRAD:
            hors.setdefault(w, TRAD[w])
        else:
            sys.exit("  %s : « %s » absent du corpus et sans traduction dans TRAD" % (s["titre"], w))
    for w in list(hors):
        if w in connus:
            del hors[w]
            mots.append(w)
    return mots, hors


def main():
    args = sys.argv[1:]
    if args[:1] == ["--montrer"]:
        print(prompt(S[args[1]]))
        return
    references, prevus = {}, {"_lisez_moi": "Fait par portugais/lisbonne/prompts.py ; controle : verifier_mots.py. Les mots sont la forme du corpus portugais (sans article)."}
    tout = dict(PILOTE, **S)
    connus = corpus()
    for nom, s in sorted(tout.items(), key=lambda kv: kv[1]["n"]):
        if nom in S:
            io.open(os.path.join(SCENES, nom + ".prompt.txt"), "w", encoding="utf-8").write(prompt(s))
        references[nom] = {"n": s["n"], "titre": s["titre"], "titre_fr": s["titre_fr"],
                           "refs": [REF[r][0] for r in s["refs"]]}
        mots, hors = ranger_mots(s, connus)
        prevus[nom] = {"mots": mots, "hors_corpus": {w: {"genre": g, "traduction": t} for w, (g, t) in hors.items()}}
    io.open(os.path.join(ICI, "references.json"), "w", encoding="utf-8").write(json.dumps(references, ensure_ascii=False, indent=1) + "\n")
    io.open(os.path.join(ICI, "mots-prevus.json"), "w", encoding="utf-8").write(json.dumps(prevus, ensure_ascii=False, indent=1) + "\n")
    print("%d prompts ecrits, %d scenes decrites." % (len(S), len(tout)))


if __name__ == "__main__":
    main()
