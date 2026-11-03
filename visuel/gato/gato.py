# -*- coding: utf-8 -*-
"""« Où est le chat ? » -- le theme illustre des PREPOSITIONS DE LIEU, en espagnol et en allemand (3 nov. 2026).
LA SEULE SOURCE du theme : la piece, les places du chat, les phrases, leurs traductions et les prompts des images.

    python visuel/gato/gato.py --json          # visuel/prototype/gato/gato.json seul, gratuit
    python visuel/gato/gato.py --provisoires   # des images DESSINEES (aplats), gratuites, pour essayer la page
    python visuel/gato/gato.py --montrer       # les prompts seuls, gratuit
    python visuel/gato/gato.py --mesurer       # ou est le chat dans chaque image (difference avec la piece vide)
    python visuel/gato/gato.py --payer [ids]   # les images fal qui manquent, 0,15 $ chacune -- ACCORD DE JACQUES

L'ANGLE (regle 2 des themes : pas de theme qui refait une scene). Le salon de Mark (scene « Nach der Party ») fait
deja « Wo? » et « Wo / Wohin » sur SES objets. Ici, UN chat et UNE piece, et seule la place du chat change d'une
image a l'autre : on compare des places, on n'explore pas une piece. La piece est le salon de Jan et Katrin, chez
Ben et Mia (la famille d'Anna, visuel/familia) ; le chat de la maison s'appelle Moritz. Anna, leur tante, passe.

LE MOUVEMENT (Jacques : « Wohin springt die Katze? Auf den Tisch. », avec des images qui montrent le mouvement) :
la question montre l'image d'AVANT et une fleche vers la nouvelle place ; la reponse montre l'image d'APRES. Le
datif dit ou il est, l'accusatif ou il va. En espagnol, la preposition ne change pas : seul « a » s'ajoute apres
salta / se sube (a la mesa, al sofa).

LES IMAGES : la piece vide d'abord (texte -> image), puis des RETOUCHES de cette image avec le meme chat (la
premiere place, sofa-vor, sert de reference du chat) ; Anna, Ben et Mia viennent de leurs images de la famille
(visuel/familia/img, hors depot). Chaque image se verifie contre sa description ; une ratee se refait.
Originaux : visuel/gato/img/ (hors depot) ; webp : visuel/prototype/gato/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype", "gato")
IMG = os.path.join(ICI, "img")
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"      # Anna-quotidien, Ben, Mia (hors depot)
MODELE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15

# ---------------------------------------------------------------------------------------------------------------
# LES NOMS : allemand (genre, mot, pluriel, datif pluriel), espagnol (genre, mot, pluriel)
NOMS = {
    "tisch":   (("der", "Tisch"),   ("la", "mesa")),
    "kissen":  (("das", "Kissen", "Kissen", "Kissen"), ("el", "cojín", "cojines")),
    "stuhl":   (("der", "Stuhl", "Stühle", "Stühlen"), ("la", "silla", "sillas")),
    "sofa":    (("das", "Sofa"),    ("el", "sofá")),
    "schrank": (("der", "Schrank"), ("el", "armario")),
    "regal":   (("das", "Regal"),   ("la", "estantería")),
    "korb":    (("der", "Korb"),    ("la", "cesta")),
    "karton":  (("der", "Karton"),  ("la", "caja")),
    "fenster": (("das", "Fenster"), ("la", "ventana")),
    "tuer":    (("die", "Tür"),     ("la", "puerta")),
    "pflanze": (("die", "Pflanze"), ("la", "planta")),
    "vorhang": (("der", "Vorhang"), ("la", "cortina")),
    "tasche":  (("die", "Tasche"),  ("el", "bolso")),
    "lampe":   (("die", "Lampe"),   ("la", "lámpara")),
    "bild":    (("das", "Bild"),    ("el", "cuadro")),
    "wand":    (("die", "Wand"),    ("la", "pared")),
}
DAT = {"der": "dem", "die": "der", "das": "dem", "pl": "den"}
AKK = {"der": "den", "die": "die", "das": "das", "pl": "die"}
# in dem -> im, an dem -> am ; in das -> ins, an das -> ans, auf das -> aufs (la fiche « Formes contractees »)
KURZ = {("in", "dem"): "im", ("an", "dem"): "am", ("in", "das"): "ins", ("an", "das"): "ans", ("auf", "das"): "aufs"}
# a l'ecrit et dans les choix : im, am, ins, ans ; « auf das » reste entier (aufs se dit, la serie « kurz » l'enseigne)
KURZ_AFFICHE = {"im", "am", "ins", "ans"}
PREP_DE = ["auf", "unter", "in", "vor", "hinter", "neben", "zwischen", "über", "an"]
PREP_ES = ["encima de", "sobre", "debajo de", "dentro de", "en", "delante de", "detrás de", "al lado de", "entre"]


def groupe_de(prep, nom, cas, pluriel=False):
    """« auf dem Tisch », « im Korb », « zwischen den Stühlen », « ins Regal »."""
    g, m = NOMS[nom][0][0], NOMS[nom][0][1]
    if pluriel:
        art, m = ("den" if cas == "dat" else "die"), NOMS[nom][0][3 if cas == "dat" else 2]
        g = "pl"
    else:
        art = (DAT if cas == "dat" else AKK)[g]
    k = KURZ.get((prep, art))
    if k in KURZ_AFFICHE:
        return k + " " + m
    return prep + " " + art + " " + m


def groupe_es(prep, nom, pluriel=False):
    """« encima de la mesa », « detrás del sofá », « entre las sillas », « en la caja »."""
    g, m = NOMS[nom][1][0], NOMS[nom][1][1]
    if pluriel:
        g, m = ("las" if g == "la" else "los"), NOMS[nom][1][2]
    if prep.endswith(" de") and g == "el":
        return prep[:-3] + " del " + m
    return prep + " " + g + " " + m


def mouvement_es(verbe, prep, nom, pluriel=False):
    """« salta a la mesa », « salta al sofá », « se mete debajo de la mesa », « se sienta entre las sillas »."""
    if prep == "a":
        g, m = NOMS[nom][1][:2]
        return verbe + " " + ("al " + m if g == "el" else "a " + g + " " + m)
    return verbe + " " + groupe_es(prep, nom, pluriel)


# ---------------------------------------------------------------------------------------------------------------
# LES PLACES DU CHAT. Pour chacune :
#   de : (preposition, nom, verbe de position, verbe de mouvement, pluriel ?)
#   es : les prepositions JUSTES pour cette image (la premiere est la forme affichee ; aucune des autres n'est
#        jamais proposee comme leurre), puis le mouvement (verbe, preposition de la destination)
#   fr, en, pt : le lieu traduit ; mvDe, mvEs : le mouvement traduit (fr, en, pt), pour qui apprend l'allemand ou
#        l'espagnol -- les verbes ne sont pas les memes (springt / salta, legt sich / se tumba)
#   prompt : ou est le chat, pour la retouche ; prov : (x, y) du chat sur l'image provisoire, en %
P = {}
def place(id, de, es, fr, en, pt, mvDe, mvEs, prompt, prov):
    P[id] = dict(de=de, es=es, fr=fr, en=en, pt=pt, mvDe=mvDe, mvEs=mvEs, prompt=prompt, prov=prov)

place("sofa-vor", ("vor", "sofa", "liegt", "legt sich"), (["delante de"], ("se tumba", "delante de")),
      "devant le canapé", "in front of the sofa", "na frente do sofá",
      ("se couche devant le canapé", "lies down in front of the sofa", "deita na frente do sofá"),
      ("se couche devant le canapé", "lies down in front of the sofa", "deita na frente do sofá"),
      "lying on the floor right in front of the sofa, in the middle of its length", (47, 86))
place("tisch-auf", ("auf", "tisch", "sitzt", "springt"), (["encima de", "sobre", "en"], ("salta", "a")),
      "sur la table", "on the table", "em cima da mesa",
      ("saute sur la table", "jumps onto the table", "pula em cima da mesa"),
      ("saute sur la table", "jumps onto the table", "pula na mesa"),
      "sitting on top of the dining table, in the middle of the table top", (76, 58))
# sous la table : trois essais refuses (le chat au bord, une deuxieme table, un autre cadrage) ; le premier montre le
# chat couche SOUS LA CHAISE de devant, dans le bon cadrage : il devient cette place-la (3 nov.)
place("stuhl-unter", ("unter", "stuhl", "liegt", "kriecht"), (["debajo de"], ("se mete", "debajo de")),
      "sous la chaise", "under the chair", "embaixo da cadeira",
      ("se glisse sous la chaise", "crawls under the chair", "se enfia embaixo da cadeira"),
      ("se glisse sous la chaise", "slips under the chair", "se enfia embaixo da cadeira"),
      "(image faite pour « sous la table » ; elle montre le chat couche sous la chaise de devant)", (66, 80))
place("tisch-neben", ("neben", "tisch", "sitzt", "setzt sich"), (["al lado de"], ("se sienta", "al lado de")),
      "à côté de la table", "next to the table", "ao lado da mesa",
      ("s'assoit à côté de la table", "sits down next to the table", "senta ao lado da mesa"),
      ("s'assoit à côté de la table", "sits down next to the table", "senta ao lado da mesa"),
      "(image faite pour « entre les chaises » ; elle montre le chat assis par terre a cote de la table)", (76, 90))
place("kissen-zwischen", ("zwischen", "kissen", "sitzt", "setzt sich", True), (["entre"], ("se sienta", "entre")),
      "entre les coussins", "between the cushions", "entre as almofadas",
      ("s'assoit entre les coussins", "sits down between the cushions", "senta entre as almofadas"),
      ("s'assoit entre les coussins", "sits down between the cushions", "senta entre as almofadas"),
      "sitting upright on the sofa seat between the two mustard cushions, which now stand close together in the middle of the "
      "sofa, one on each side of the cat", (47, 60))
place("sofa-auf", ("auf", "sofa", "liegt", "springt"), (["encima de", "en", "sobre"], ("salta", "a")),
      "sur le canapé", "on the sofa", "no sofá",
      ("saute sur le canapé", "jumps onto the sofa", "pula no sofá"),
      ("saute sur le canapé", "jumps onto the sofa", "pula no sofá"),
      "lying curled up on the seat of the sofa", (47, 62))
place("sofa-hinter", ("hinter", "sofa", "sitzt", "läuft"), (["detrás de"], ("se esconde", "detrás de")),
      "derrière le canapé", "behind the sofa", "atrás do sofá",
      ("va derrière le canapé", "goes behind the sofa", "vai para trás do sofá"),
      ("se cache derrière le canapé", "hides behind the sofa", "se esconde atrás do sofá"),
      "behind the sofa, between the sofa and the wall: only its head and ears peek out over the top of the sofa back", (52, 50))
place("sofa-unter", ("unter", "sofa", "liegt", "kriecht"), (["debajo de"], ("se mete", "debajo de")),
      "sous le canapé", "under the sofa", "embaixo do sofá",
      ("se glisse sous le canapé", "crawls under the sofa", "se enfia embaixo do sofá"),
      ("se glisse sous le canapé", "slips under the sofa", "se enfia embaixo do sofá"),
      "hidden under the sofa, in the shadow beneath it: its whole body is under the sofa and only its face and its two front "
      "paws peek out from under the front edge of the sofa", (42, 76))
place("korb-in", ("in", "korb", "liegt", "legt sich"), (["en", "dentro de"], ("se mete", "en")),
      "dans le panier", "in the basket", "na cesta",
      ("se couche dans le panier", "lies down in the basket", "deita na cesta"),
      ("se met dans le panier", "gets into the basket", "entra na cesta"),
      "lying inside the round wicker cat basket next to the sofa, its head looking out of the round opening", (66, 80))
place("korb-neben", ("neben", "korb", "sitzt", "setzt sich"), (["al lado de"], ("se sienta", "al lado de")),
      "à côté du panier", "next to the basket", "ao lado da cesta",
      ("s'assoit à côté du panier", "sits down next to the basket", "senta ao lado da cesta"),
      ("s'assoit à côté du panier", "sits down next to the basket", "senta ao lado da cesta"),
      "sitting on the floor right next to the round wicker cat basket, on its right side, clearly outside it", (61, 82))
place("korb-auf", ("auf", "korb", "sitzt", "springt"), (["encima de", "sobre"], ("se sube", "encima de")),
      "sur le panier", "on top of the basket", "em cima da cesta",
      ("saute sur le panier", "jumps onto the basket", "pula em cima da cesta"),
      ("monte sur le panier", "climbs onto the basket", "sobe em cima da cesta"),
      "(image faite pour « a la fenetre » ; elle montre le chat assis sur le panier rond)", (64, 74))
place("karton-in", ("in", "karton", "sitzt", "springt"), (["dentro de", "en"], ("se mete", "en")),
      "dans le carton", "in the box", "dentro da caixa",
      ("saute dans le carton", "jumps into the box", "pula dentro da caixa"),
      ("se met dans le carton", "gets into the box", "entra na caixa"),
      "sitting inside the cardboard box, whose lid is now open; only its head and ears stick out of the top", (15, 86))
place("karton-auf", ("auf", "karton", "sitzt", "springt"), (["encima de", "sobre"], ("se sube", "encima de")),
      "sur le carton", "on the box", "em cima da caixa",
      ("saute sur le carton", "jumps onto the box", "pula em cima da caixa"),
      ("monte sur le carton", "climbs onto the box", "sobe em cima da caixa"),
      "sitting on top of the closed cardboard box", (15, 78))
place("schrank-auf", ("auf", "schrank", "liegt", "klettert"), (["encima de"], ("se sube", "a")),
      "sur l'armoire", "on top of the wardrobe", "em cima do armário",
      ("grimpe sur l'armoire", "climbs onto the wardrobe", "sobe no armário"),
      ("grimpe sur l'armoire", "climbs onto the wardrobe", "sobe no armário"),
      "lying on top of the tall wardrobe, looking down into the room", (22, 13))
place("tuer-vor", ("vor", "tuer", "sitzt", "setzt sich"), (["delante de"], ("se sienta", "delante de")),
      "devant la porte", "in front of the door", "na frente da porta",
      ("s'assoit devant la porte", "sits down in front of the door", "senta na frente da porta"),
      ("s'assoit devant la porte", "sits down in front of the door", "senta na frente da porta"),
      "sitting on the floor in front of the closed door, looking at it", (7, 84))
place("fenster-an", ("an", "fenster", "sitzt", "setzt sich"), (["en"], ("salta", "a")),
      "à la fenêtre", "at the window", "na janela",
      ("s'assoit à la fenêtre", "sits down at the window", "senta na janela"),
      ("saute sur le rebord de la fenêtre", "jumps onto the windowsill", "pula na janela"),
      "sitting upright at the open window, on the floor of the window opening between the two open window panes, its back to "
      "the camera, looking out through the window; it is far from the wicker basket and not on it", (70, 44))
place("regal-in", ("in", "regal", "liegt", "springt"), (["en"], ("salta", "a")),
      "dans l'étagère", "in the bookcase", "na estante",
      ("saute dans l'étagère", "jumps into the bookcase", "pula na estante"),
      ("saute sur l'étagère", "jumps onto the bookcase", "pula na estante"),
      "lying on the empty middle shelf of the white bookcase (the shelf without books)", (92, 45))
place("pflanze-vor", ("vor", "pflanze", "sitzt", "setzt sich"), (["delante de"], ("se sienta", "delante de")),
      "devant la plante", "in front of the plant", "na frente da planta",
      ("s'assoit devant la plante", "sits down in front of the plant", "senta na frente da planta"),
      ("s'assoit devant la plante", "sits down in front of the plant", "senta na frente da planta"),
      "(image faite pour « a cote de la plante » ; elle montre le chat assis devant le pot de la plante)", (85, 84))
place("vorhang-hinter", ("hinter", "vorhang", "sitzt", "läuft"), (["detrás de"], ("se esconde", "detrás de")),
      "derrière le rideau", "behind the curtain", "atrás da cortina",
      ("va derrière le rideau", "goes behind the curtain", "vai para trás da cortina"),
      ("se cache derrière le rideau", "hides behind the curtain", "se esconde atrás da cortina"),
      "hiding behind the long white curtain on the left of the window: the curtain bulges around its shape and its tail and two paws show under the curtain", (61, 86))

# AVEC NOS PERSONNES (Jacques : « Mets de temps en temps nos personnes (Anna, Ben, Mia) pour la vie »). Ces images
# servent aux questions sur les personnes ; tasche-in est aussi une place du chat (le sac d'Anna).
place("tasche-in", ("in", "tasche", "sitzt", "kriecht"), (["dentro de", "en"], ("se mete", "en")),
      "dans le sac", "in the bag", "dentro da bolsa",
      ("se glisse dans le sac", "crawls into the bag", "se enfia na bolsa"),
      ("se met dans le sac", "gets into the bag", "entra na bolsa"),
      "sitting inside Anna's open handbag, which stands on the floor in front of the sofa; only its head sticks out. "
      "Anna (the woman of the third picture, same face, hair and clothes) sits on the sofa and laughs, looking down at the cat", (40, 84))
PERSONNES_IMG = {   # id : (qui, prompt) -- les personnes : Anna (3e image), Ben (4e), Mia (5e)
    "ben-mia":   ("Ben, Mia", "Ben and Mia (the boy and the little girl of the reference pictures) sit side by side on the sofa, "
                  "smiling; the cat sits on the sofa seat between the two children"),
    "mia-tisch": ("Mia", "(image faite pour « Mia sous la table » ; elle montre Mia assise par terre et le chat couche a cote "
                  "d'elle)"),
    "anna-korb": ("Anna", "Anna (the woman of the reference picture) bends down and gently puts the cat into the round wicker basket "
                  "with both hands; the cat is halfway into the basket"),
    "ben-tisch": ("Ben", "(image faite pour « Ben pose le chat sur la chaise » ; elle le montre posant le chat sur la table)"),
}
PERSONNES = {
    # sur l'image ben-mia : le chat entre Ben et Mia ; Ben et Mia sur le canape
    "ben-mia": {"de": {"q": "Wo sitzt die Katze?", "rep": "zwischen Ben und Mia", "phrase": "Die Katze sitzt zwischen Ben und Mia.",
                       "prep": "zwischen"},
                "es": {"q": "¿Dónde está el gato?", "rep": "entre Ben y Mia", "phrase": "El gato está entre Ben y Mia.", "prep": "entre"},
                "fr": "Le chat est assis entre Ben et Mia.", "en": "The cat is sitting between Ben and Mia.",
                "pt": "O gato está sentado entre Ben e Mia.", "frEs": "Le chat est entre Ben et Mia.",
                "enEs": "The cat is between Ben and Mia.", "ptEs": "O gato está entre Ben e Mia.",
                "leurresDe": [("neben", "sofa"), ("unter", "sofa"), ("hinter", "sofa")],
                "leurresEs": [("al lado de", "sofa"), ("debajo de", "sofa"), ("detrás de", "sofa")]},
    "mia-tisch": {"de": {"q": "Wo liegt die Katze?", "rep": "neben Mia", "phrase": "Die Katze liegt neben Mia.", "prep": "neben"},
                  "es": {"q": "¿Dónde está el gato?", "rep": "al lado de Mia", "phrase": "El gato está al lado de Mia.", "prep": "al lado de"},
                  "fr": "Le chat est couché à côté de Mia.", "en": "The cat is lying next to Mia.", "pt": "O gato está deitado ao lado da Mia.",
                  "frEs": "Le chat est à côté de Mia.", "enEs": "The cat is next to Mia.", "ptEs": "O gato está ao lado da Mia.",
                  "leurresDe": [("auf", "tisch"), ("unter", "sofa"), ("in", "karton")],
                  "leurresEs": [("encima de", "tisch"), ("debajo de", "sofa"), ("dentro de", "karton")]},
}
# les gestes de nos personnes : Anna met le chat DANS le panier, Ben le pose SUR la table (Wohin + accusatif)
GESTES = {
    "anna-korb": {"de": {"q": "Wohin legt Anna die Katze?", "rep": ("in", "korb"), "verbe": "legt", "inf": "legen", "faux": "liegt",
                         "phrase": "Anna legt die Katze in den Korb.", "trou": "Anna ___ die Katze in den Korb."},
                  "es": {"q": "¿Dónde pone Anna al gato?", "rep": ("en", "korb"), "phrase": "Anna pone al gato en la cesta."},
                  "fr": "Anna met le chat dans le panier.", "en": "Anna puts the cat into the basket.", "pt": "Anna coloca o gato na cesta.",
                  "leurresDe": [("auf", "korb"), ("neben", "korb")], "leurresEs": [("al lado de", "korb"), ("debajo de", "korb")]},
    "ben-tisch": {"de": {"q": "Wohin setzt Ben die Katze?", "rep": ("auf", "tisch"), "verbe": "setzt", "inf": "setzen", "faux": "sitzt",
                         "phrase": "Ben setzt die Katze auf den Tisch.", "trou": "Ben ___ die Katze auf den Tisch."},
                  "es": {"q": "¿Dónde pone Ben al gato?", "rep": ("encima de", "tisch"), "phrase": "Ben pone al gato encima de la mesa."},
                  "fr": "Ben pose le chat sur la table.", "en": "Ben puts the cat on the table.", "pt": "Ben coloca o gato em cima da mesa.",
                  "leurresDe": [("unter", "tisch"), ("neben", "tisch")], "leurresEs": [("debajo de", "tisch"), ("al lado de", "tisch")]},
}
# EN PLEIN SAUT : le mouvement se voit dans l'image meme (la decouverte « Wohin? », et des questions de mouvement)
SAUTS = {   # id : (place d'arrivee ou None, prompt, phrase de, phrase es, traductions fr/en/pt pour de, puis pour es)
    "saut-tisch":  ("tisch-auf", "in mid-leap from the floor up onto the dining table, its front paws just reaching the table top"),
    "saut-karton": ("karton-in", "in mid-jump, diving head first into the cardboard box, whose flaps are now open"),
    "saut-ueber":  (None, "leaping over the closed cardboard box, in mid-air right above it, front legs stretched forward"),
}
UEBER = {"de": {"q": "Wohin springt die Katze?", "rep": "über den Karton", "phrase": "Die Katze springt über den Karton.", "prep": "über", "nom": "karton",
                "trou": "Die Katze springt über ___ Karton.", "art": "den", "leurres": ["über dem Karton", "auf den Karton", "in den Karton"]},
         "es": {"q": "¿Por dónde salta el gato?", "rep": "por encima de la caja", "phrase": "El gato salta por encima de la caja.",
                "leurres": ["dentro de la caja", "debajo de la caja"]},
         "fr": "Le chat saute par-dessus le carton.", "en": "The cat jumps over the box.", "pt": "O gato pula por cima da caixa."}

# CE QUI EST VRAI DANS TOUTES LES IMAGES (la piece ne bouge pas) : la lampe au-dessus de la table, le tableau au mur,
# au-dessus du canape. C'est la que « über » se dit sans mouvement.
OBJETS = [
    {"id": "lampe", "de": ("Lampe", "hängt", "über", "tisch"), "es": ("lámpara", ["encima de", "sobre"], "tisch"),
     "fr": "La lampe est au-dessus de la table.", "en": "The lamp hangs above the table.", "pt": "A luminária fica em cima da mesa.",
     "frEs": "La lampe est au-dessus de la table.", "enEs": "The lamp is above the table.", "ptEs": "A luminária está em cima da mesa.",
     "leurresDe": [("unter", "tisch"), ("neben", "tisch"), ("auf", "tisch")], "leurresEs": [("debajo de", "tisch"), ("al lado de", "tisch")]},
    {"id": "bild-sofa", "de": ("Bild", "hängt", "über", "sofa"), "es": ("cuadro", ["encima de"], "sofa"),
     "fr": "Le tableau est au-dessus du canapé.", "en": "The picture hangs above the sofa.", "pt": "O quadro fica em cima do sofá.",
     "frEs": "Le tableau est au-dessus du canapé.", "enEs": "The picture is above the sofa.", "ptEs": "O quadro está em cima do sofá.",
     "leurresDe": [("unter", "sofa"), ("neben", "sofa"), ("hinter", "sofa")], "leurresEs": [("debajo de", "sofa"), ("al lado de", "sofa"), ("detrás de", "sofa")]},
    {"id": "bild-wand", "de": ("Bild", "hängt", "an", "wand"), "es": ("cuadro", ["en"], "wand"),
     "fr": "Le tableau est accroché au mur.", "en": "The picture hangs on the wall.", "pt": "O quadro está pendurado na parede.",
     "frEs": "Le tableau est au mur.", "enEs": "The picture is on the wall.", "ptEs": "O quadro está na parede.",
     "leurresDe": [("auf", "wand"), ("in", "wand"), ("hinter", "wand")], "leurresEs": [("detrás de", "wand"), ("debajo de", "wand")]},
]

# deux places VRAIES ensemble sur une meme image (le sac d'Anna est devant le canape, le rideau pend a la fenetre) :
# l'une n'est jamais le leurre de l'autre, ni l'image fausse d'une question sur l'autre. A revoir sur les vraies images.
AUSSI = {"sofa-unter": ["sofa-vor"], "tasche-in": ["sofa-vor"], "vorhang-hinter": ["fenster-an"],
         "kissen-zwischen": ["sofa-auf"], "korb-neben": ["pflanze-vor"], "stuhl-unter": ["tisch-neben"]}

POSTURE = {"sitzt": ("est assis", "is sitting", "está sentado"), "liegt": ("est couché", "is lying", "está deitado")}
TRAD_ES = ("est", "is", "está")       # « El gato está… » : le chat est, the cat is, o gato está

# ---------------------------------------------------------------------------------------------------------------
# LA PIECE ET LES PROMPTS
CHAT = "a black-and-white tuxedo cat with a white chest, white paws and a black back and head"
PIECE = ("A photorealistic photograph of the living room of a young family's apartment in an old Berlin building, "
         "natural soft daylight, realistic, no retouching. The camera stands at the front of the room at the height of an "
         "adult's chest and faces the back wall straight on; the whole room is visible from the left wall to the right wall, "
         "with plenty of free light oak parquet floor in the foreground. Plain white walls, no rug. From left to right: "
         "a white panelled door, closed, at the far left; next to it a tall dark wooden wardrobe; then, against the back "
         "wall but standing about half a metre away from it, a light grey three-seat sofa on tall thin wooden legs with free "
         "space underneath, with two mustard cushions; above the sofa, a framed landscape picture hanging on the wall; a "
         "round wicker cat basket with a cushion inside on the floor to the right of the sofa; a large window with a window "
         "sill and long white curtains, open, reaching down to the floor; a tall green potted plant; and at the far right a "
         "white open bookcase full of books, with one empty middle shelf. In the right half of the foreground, a light wooden "
         "dining table with two matching wooden chairs standing side by side on the near side of the table, with a clear gap "
         "between them, and a white pendant lamp hanging above the table. In the left foreground, a closed plain brown "
         "cardboard box on the floor. Tidy and simple, nothing on the table, no people, no animals, no text, no logos.")
GARDE = ("Exactly the same room as in the first picture: the same camera, the same framing, the same light, and every piece "
         "of furniture in exactly the same place, nothing moved, nothing added, nothing removed. ")
CHAT_REF = " The same cat as in the second picture (same size, same black-and-white markings) is now "


def prompt_de(id):
    if id == "piece":
        return PIECE
    if id == "sofa-vor":
        return GARDE + "A cat has come in: " + CHAT + ", " + P[id]["prompt"] + ". Only the cat is new."
    if id in P:
        return GARDE + CHAT_REF.strip() + " " + P[id]["prompt"] + ". Only the cat's place changes."
    if id in PERSONNES_IMG:
        return GARDE + "The same cat as in the second picture (same size, same markings). " + PERSONNES_IMG[id][1] + \
               ". The people look exactly like in their reference pictures: same face, hair, clothes and height."
    if id in SAUTS:
        return GARDE + CHAT_REF.strip() + " " + SAUTS[id][1] + ". A natural photograph of a real jumping cat, sharp, no motion blur on its face."
    raise KeyError(id)


def references(id):
    """Les images a donner a la retouche : la piece, le chat (sofa-vor), puis les personnes."""
    if id == "piece":
        return []
    refs = [os.path.join(IMG, "piece.png")]
    if id != "sofa-vor":
        refs.append(os.path.join(IMG, "sofa-vor.png"))
    qui = {"tasche-in": "Anna"}.get(id) or (PERSONNES_IMG[id][0] if id in PERSONNES_IMG else "")
    for n in [x.strip() for x in qui.split(",") if x.strip()]:
        refs.append(os.path.join(FAMILLE, ("Anna-quotidien" if n == "Anna" else n) + ".png"))
    return refs


IMAGES = ["piece", "sofa-vor"] + [k for k in P if k != "sofa-vor"] + list(PERSONNES_IMG) + list(SAUTS)

# ---------------------------------------------------------------------------------------------------------------
# LA DONNEE DE LA PAGE


def article_de(nom, cas, pluriel=False):
    return ("den" if cas == "dat" else "die") if pluriel else (DAT if cas == "dat" else AKK)[NOMS[nom][0][0]]


def nom_de(nom, pluriel=False):
    return NOMS[nom][0][3 if pluriel else 1] if pluriel else NOMS[nom][0][1]


def phrase_maj(s):
    return s[0].upper() + s[1:]


def construire():
    d = {"_lisez_moi": "FABRIQUE par visuel/gato/gato.py -- ne pas modifier a la main.", "places": {}, "personnes": {}, "gestes": {},
         "objets": [], "ueber": UEBER, "images": {}, "trad": {"de": {}, "es": {}}, "gloses": {"de": {}, "es": {}}, "kurz": {}}
    tr = d["trad"]
    def trad(app, phrase, fr, en, pt, de=None):
        if phrase in tr[app] and tr[app][phrase]["fr"] != fr:
            raise SystemExit("deux traductions pour « %s » : %s / %s" % (phrase, tr[app][phrase]["fr"], fr))
        tr[app][phrase] = {"fr": fr, "en": en, "pt": pt}
        if de:
            tr[app][phrase]["de"] = de
    for id, p in P.items():
        prep, nom, vWo, vWohin = p["de"][:4]
        pl = len(p["de"]) > 4 and p["de"][4]
        wo, wohin = groupe_de(prep, nom, "dat", pl), groupe_de(prep, nom, "akk", pl)
        # les questions : « Wo sitzt die Katze? » ; « Wohin springt die Katze? » / « Wohin setzt sich die Katze? »
        refl = vWohin.endswith(" sich")
        v = vWohin.replace(" sich", "")
        de = {"prep": prep, "nom": nom, "genre": NOMS[nom][0][0], "mot": NOMS[nom][0][1], "pluriel": bool(pl),
              "wo": wo, "wohin": wohin, "vWo": vWo, "vWohin": vWohin,
              "phrase": "Die Katze " + vWo + " " + wo + ".",
              "mouvement": "Die Katze " + vWohin + " " + wohin + ".",
              "qWo": "Wo " + vWo + " die Katze?",
              "qWohin": "Wohin " + v + (" sich" if refl else "") + " die Katze?",
              "qWohinSie": "Wohin " + v + " sie" + (" sich" if refl else "") + "?",
              "artDat": article_de(nom, "dat", pl), "artAkk": article_de(nom, "akk", pl),
              "trouDat": "Die Katze " + vWo + " " + prep + " ___ " + nom_de(nom, pl) + ".",
              "trouAkk": "Die Katze " + vWohin + " " + prep + " ___ " + (NOMS[nom][0][2] if pl else nom_de(nom)) + "."}
        # les contractions de cette place (in dem -> im) : la serie « kurz »
        for cas, art in (("dat", de["artDat"]), ("akk", de["artAkk"])):
            k = KURZ.get((prep, art)) if not pl else None
            if k:
                de["kurz" + ("Wo" if cas == "dat" else "Wohin")] = k
        verbesEs, mv = p["es"]
        es = {"preps": verbesEs, "nom": nom, "genre": NOMS[nom][1][0], "mot": NOMS[nom][1][1], "pluriel": bool(pl),
              "donde": [groupe_es(x, nom, pl) for x in verbesEs],
              "mvVerbe": mv[0], "mvPrep": mv[1], "mouvement": "El gato " + mouvement_es(mv[0], mv[1], nom, pl) + ".",
              "mvLieu": mouvement_es(mv[0], mv[1], nom, pl)[len(mv[0]) + 1:]}
        es["phrase"] = "El gato está " + es["donde"][0] + "."
        d["places"][id] = {"de": de, "es": es, "aussi": AUSSI.get(id, [])}
        po = POSTURE[vWo]
        trad("de", de["phrase"], "Le chat %s %s." % (po[0], p["fr"]), "The cat %s %s." % (po[1], p["en"]), "O gato %s %s." % (po[2], p["pt"]))
        trad("de", de["mouvement"], "Le chat %s." % p["mvDe"][0], "The cat %s." % p["mvDe"][1], "O gato %s." % p["mvDe"][2])
        for dd in es["donde"]:
            trad("es", "El gato está " + dd + ".", "Le chat est %s." % p["fr"], "The cat is %s." % p["en"], "O gato está %s." % p["pt"],
                 "Die Katze %s %s." % (vWo, wo))
        trad("es", es["mouvement"], "Le chat %s." % p["mvEs"][0], "The cat %s." % p["mvEs"][1], "O gato %s." % p["mvEs"][2])
    for id, q in PERSONNES.items():
        d["personnes"][id] = q
        trad("de", q["de"]["phrase"], q["fr"], q["en"], q["pt"])
        trad("es", q["es"]["phrase"], q["frEs"], q["enEs"], q["ptEs"], q["de"]["phrase"].replace("sitzt", "ist"))
    for id, g in GESTES.items():
        dg = dict(g)
        pr, nom = g["de"]["rep"]
        dg["de"] = dict(g["de"], rep=groupe_de(pr, nom, "akk"), prep=pr, nom=nom, art=article_de(nom, "akk"),
                        leurres=[groupe_de(pr, nom, "dat")]
                        + [groupe_de(a, b, "akk") for a, b in g["leurresDe"]])
        pr, nom = g["es"]["rep"]
        dg["es"] = dict(g["es"], rep=groupe_es(pr, nom), prep=pr, nom=nom, leurres=[groupe_es(a, b) for a, b in g["leurresEs"]])
        d["gestes"][id] = dg
        trad("de", g["de"]["phrase"], g["fr"], g["en"], g["pt"])
        trad("es", g["es"]["phrase"], g["fr"], g["en"], g["pt"], g["de"]["phrase"])
    for o in OBJETS:
        mot, verbe, prep, nom = o["de"]
        g = {"Lampe": "Die", "Bild": "Das"}[mot]
        de = {"sujet": g + " " + mot, "q": "Wo " + verbe + " " + g.lower() + " " + mot + "?", "rep": groupe_de(prep, nom, "dat"),
              "prep": prep, "nom": nom, "art": article_de(nom, "dat"),
              "phrase": g + " " + mot + " " + verbe + " " + groupe_de(prep, nom, "dat") + ".",
              "trou": g + " " + mot + " " + verbe + " " + prep + " ___ " + nom_de(nom) + ".",
              "leurres": [groupe_de(a, b, "dat") for a, b in o["leurresDe"]]}
        mot_es, preps, nom_es = o["es"]
        art_es = "La" if mot_es == "lámpara" else "El"
        es = {"q": "¿Dónde está " + art_es.lower() + " " + mot_es + "?", "rep": [groupe_es(x, nom_es) for x in preps], "nom": nom_es,
              "phrase": art_es + " " + mot_es + " está " + groupe_es(preps[0], nom_es) + ".",
              "leurres": [groupe_es(a, b) for a, b in o["leurresEs"]], "preps": preps}
        d["objets"].append({"id": o["id"], "de": de, "es": es})
        trad("de", de["phrase"], o["fr"], o["en"], o["pt"])
        for r in es["rep"]:
            trad("es", art_es + " " + mot_es + " está " + r + ".", o["frEs"], o["enEs"], o["ptEs"], de["phrase"])
    trad("de", UEBER["de"]["phrase"], UEBER["fr"], UEBER["en"], UEBER["pt"])
    trad("es", UEBER["es"]["phrase"], UEBER["fr"], UEBER["en"], UEBER["pt"], UEBER["de"]["phrase"])
    # les images : la place (ou les personnes, ou le saut), et ou est le chat (mesure, en %)
    mesures = {}
    chemin_mesures = os.path.join(ICI, "mesures.json")
    if os.path.exists(chemin_mesures):
        mesures = json.load(io.open(chemin_mesures, encoding="utf-8"))
    for id in IMAGES[1:]:
        e = {"chat": mesures.get(id) or (list(P[id]["prov"]) if id in P else None)}
        if id in P: e["place"] = id
        if id in PERSONNES: e["personnes"] = id
        if id in GESTES: e["geste"] = id
        if id in SAUTS: e["saut"] = SAUTS[id][0]
        d["images"][id] = e
    gloses(d)
    return d


def gloses(d):
    """La traduction de chaque mot teste, prise au CORPUS RELU, pour les langues ou la phrase n'est pas traduite
    (arabe, turc, ukrainien, persan, polonais, russe) : « der Tisch — стіл »."""
    LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]
    champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)
    def pose(app, cle, w):
        d["gloses"][app][cle] = {l: champ(w, l) for l in LANGUES if champ(w, l)}
    fw = json.load(io.open(os.path.join(RACINE, "funktionswort.json"), encoding="utf-8"))["praepositionen"]
    for w in fw:
        if w["mot"] in PREP_DE: pose("de", w["mot"], w)
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    for t in th:
        for w in t.get("mots", []):
            for k, (de, es) in NOMS.items():
                if w.get("mot") == de[1] and w.get("genre") == de[0] and de[1] not in d["gloses"]["de"]:
                    pose("de", de[1], w)
    verbes = json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8"))
    def parcourir(o, fn):
        if isinstance(o, dict):
            if "infinitif" in o: fn(o)
            for v in o.values(): parcourir(v, fn)
        elif isinstance(o, list):
            for v in o: parcourir(v, fn)
    parcourir(verbes, lambda w: w["infinitif"] in ("liegen", "legen", "sitzen", "setzen") and w["infinitif"] not in d["gloses"]["de"] and pose("de", w["infinitif"], w))
    te = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "temas.json"), encoding="utf-8"))["themes"]
    for t in te:
        for w in t.get("mots", []):
            for k, (de, es) in NOMS.items():
                if w.get("mot") == es[1] and w.get("genre") == es[0] and es[1] not in d["gloses"]["es"]:
                    pose("es", es[1], w)
    ve = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "verbos.json"), encoding="utf-8"))
    parcourir(ve, lambda w: w["infinitif"] == "estar" and "estar" not in d["gloses"]["es"] and pose("es", "estar", w))
    # les prepositions espagnoles : funcionales.json d'abord ; « al lado de » et « dentro de » n'y sont pas, leurs
    # gloses sont celles des cartes de prepositions (index.html, praepTheme) et de leurs equivalents allemands
    fe = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "funcionales.json"), encoding="utf-8"))
    for niv in fe.values():
        for w in niv:
            if w.get("mot") in PREP_ES and w["mot"] not in d["gloses"]["es"]:
                pose("es", w["mot"], w)
    MAIN = {"al lado de": {"fr": "à côté de", "en": "next to", "pt": "ao lado de", "ar": "بجانب", "de": "neben"},
            "dentro de": {"fr": "dans, à l'intérieur de", "en": "inside", "pt": "dentro de", "ar": "داخل", "de": "in, innerhalb von"},
            "encima de": {"fr": "sur, au-dessus de", "en": "on top of", "pt": "em cima de", "ar": "فوق", "de": "auf, über"}}
    for k, v in MAIN.items():
        d["gloses"]["es"].setdefault(k, v)
    manque = [m for m in PREP_DE + [n[0][1] for n in NOMS.values()] + ["liegen", "legen", "sitzen", "setzen"] if m not in d["gloses"]["de"]]
    manque += [m for m in PREP_ES + [n[1][1] for n in NOMS.values()] + ["estar"] if m not in d["gloses"]["es"]]
    if manque:
        raise SystemExit("gloses absentes du corpus : %s" % manque)


def ecrire_voix(d):
    """LES VOIX A ENREGISTRER (strategie des voix, 3 nov. : rien avant le renouvellement du 4 nov., le telephone d'ici
    la) : chaque phrase que la page dit, par langue, et le nombre de caracteres (les credits ElevenLabs). L'espagnol
    se dit deux fois (Lolita pour l'Espagne, Monica pour l'Amerique latine)."""
    v = {"_lisez_moi": "FABRIQUE par visuel/gato/gato.py : les textes a enregistrer (ElevenLabs v2, accord de Jacques).",
         "de": sorted(d["trad"]["de"]), "es": sorted(d["trad"]["es"]) + ["dentro de"]}
    v["credits"] = {"de (Aurora)": sum(len(t) for t in v["de"]), "es (Lolita + Monica)": 2 * sum(len(t) for t in v["es"])}
    io.open(os.path.join(ICI, "voix.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(v, ensure_ascii=False, indent=1) + "\n")
    return v["credits"]


def ecrire_json():
    os.makedirs(PROTO, exist_ok=True)
    d = construire()
    print("  voix a enregistrer (credits) :", ecrire_voix(d))
    io.open(os.path.join(PROTO, "gato.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  visuel/prototype/gato/gato.json : %d places, %d images, %d phrases traduites (de), %d (es)"
          % (len(d["places"]), len(d["images"]), len(d["trad"]["de"]), len(d["trad"]["es"])))


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES PROVISOIRES : la piece en aplats et le chat en rond, pour essayer la page sans rien payer. Elles
# s'ecrivent dans visuel/prototype/gato/ et NE SE COMMITTENT PAS (elles portent « PROVISOIRE »).
def provisoires():
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 900
    f = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    petit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
    def piece():
        im = Image.new("RGB", (W, H), (236, 233, 226))
        d = ImageDraw.Draw(im)
        d.rectangle((0, int(H * .62), W, H), fill=(205, 170, 125))           # le parquet
        box = lambda x0, y0, x1, y1, c, t=None: (d.rectangle((W * x0 / 100, H * y0 / 100, W * x1 / 100, H * y1 / 100), fill=c, outline=(90, 80, 70), width=2),
                                                   t and d.text((W * (x0 + x1) / 200, H * (y0 + y1) / 200), t, fill=(40, 40, 40), font=petit, anchor="mm"))
        box(1, 30, 13, 88, (250, 250, 248), "Tür")
        box(14, 16, 30, 88, (110, 80, 55), "Schrank")
        box(42, 26, 56, 40, (150, 180, 200), "Bild")
        box(33, 50, 62, 64, (175, 178, 182), "Sofa")
        box(33, 64, 62, 72, (160, 162, 168))
        for x in (34, 61): box(x, 72, x + 1, 80, (110, 80, 55))
        box(62, 76, 70, 84, (200, 160, 90), "Korb")
        box(60, 18, 80, 48, (200, 225, 240), "Fenster")
        box(58, 18, 61, 82, (245, 245, 245)); box(79, 18, 82, 82, (245, 245, 245))
        box(82, 50, 88, 84, (70, 140, 70), "Pflanze")
        box(88, 20, 99, 84, (248, 248, 248), "Regal")
        box(64, 60, 90, 64, (190, 150, 100), "Tisch")
        for x in (65, 88): box(x, 64, x + 1, 80, (150, 110, 70))
        box(75, 0, 77, 30, (220, 220, 220)); box(72, 30, 80, 35, (250, 250, 250), "Lampe")
        box(62, 74, 70, 98, (170, 125, 80), "Stuhl"); box(82, 74, 90, 98, (170, 125, 80), "Stuhl")
        box(8, 80, 22, 96, (170, 130, 85), "Karton")
        d.text((W / 2, 22), "PROVISOIRE -- images fal en attente", fill=(160, 40, 40), font=f, anchor="mm")
        return im
    def chat(im, x, y, label):
        d = ImageDraw.Draw(im)
        cx, cy, r = W * x / 100, H * y / 100, 26
        d.polygon([(cx - r, cy - r * .4), (cx - r * .6, cy - r * 1.5), (cx - r * .1, cy - r * .7)], fill=(20, 20, 20))
        d.polygon([(cx + r, cy - r * .4), (cx + r * .6, cy - r * 1.5), (cx + r * .1, cy - r * .7)], fill=(20, 20, 20))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(20, 20, 20), outline=(255, 255, 255), width=4)
        d.ellipse((cx - r * .5, cy, cx + r * .5, cy + r * .9), fill=(255, 255, 255))
        if label: d.text((cx, cy + r + 18), label, fill=(160, 40, 40), font=petit, anchor="mm")
    os.makedirs(PROTO, exist_ok=True)
    base = piece()
    base.save(os.path.join(PROTO, "piece.webp"), quality=80)
    pos_pers = {"ben-mia": (47, 60, "Ben · Mia"), "mia-tisch": (72, 80, "Mia"), "anna-korb": (66, 78, "Anna"), "ben-tisch": (76, 58, "Ben")}
    for id in IMAGES[1:]:
        im = base.copy()
        if id in P: x, y = P[id]["prov"]; lab = ""
        elif id in PERSONNES_IMG: x, y, lab = pos_pers[id]
        else:
            x, y = P[SAUTS[id][0]]["prov"] if SAUTS[id][0] else (15, 70)
            y -= 8; lab = "saut"
        chat(im, x, y, lab)
        im.save(os.path.join(PROTO, id + ".webp"), quality=80)
    print("  %d images provisoires dans visuel/prototype/gato/ (a ne pas committer)" % len(IMAGES))


# ---------------------------------------------------------------------------------------------------------------
# OU EST LE CHAT : la difference avec la piece vide donne sa place (le centre de la plus grande tache), en %.
def mesurer():
    from PIL import Image, ImageChops, ImageFilter
    base = Image.open(os.path.join(PROTO, "piece.webp")).convert("L").resize((300, 225))
    m = {}
    for id in IMAGES[1:]:
        ch = os.path.join(PROTO, id + ".webp")
        if not os.path.exists(ch): continue
        im = Image.open(ch).convert("L").resize((300, 225))
        diff = ImageChops.difference(base, im).filter(ImageFilter.MedianFilter(5)).point(lambda v: 255 if v > 40 else 0)
        bb = diff.getbbox()
        if not bb: continue
        px = diff.load(); xs = ys = n = 0
        for y in range(bb[1], bb[3]):
            for x in range(bb[0], bb[2]):
                if px[x, y]: xs += x; ys += y; n += 1
        m[id] = [round(xs / n / 3, 1), round(ys / n / 2.25, 1)]
        print("  %-16s chat vers %s %%" % (id, m[id]))
    io.open(os.path.join(ICI, "mesures.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(m, indent=1) + "\n")


# ---------------------------------------------------------------------------------------------------------------
def payer(ids):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [i for i in (ids or IMAGES) if not os.path.exists(os.path.join(IMG, i + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = O.cle()
    for id in a_faire:
        prompt, refs = prompt_de(id), references(id)
        manque = [r for r in refs if not os.path.exists(r)]
        if manque:
            print("  %s : reference absente %s -- sautee" % (id, manque)); continue
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = MODELE
        if refs:
            modele = EDIT
            corps["image_urls"] = [O.deposer(r, "image/png", cle)[0] for r in refs]
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(IMG, id + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, id + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "references": [os.path.basename(r) for r in refs], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


def webp():
    """Les originaux (visuel/gato/img/*.png) -> visuel/prototype/gato/*.webp, 1200 px de large."""
    from PIL import Image
    for id in IMAGES:
        src = os.path.join(IMG, id + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB")
        im = im.resize((1200, round(1200 * im.height / im.width)), Image.LANCZOS)
        im.save(os.path.join(PROTO, id + ".webp"), quality=78, method=6)
        print("  ", id)


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        for id in IMAGES:
            print("\n  %s  (%s)\n  %s" % (id, ", ".join(os.path.basename(r) for r in references(id)) or "texte seul", prompt_de(id)))
        print("\n  %d images, %.2f $" % (len(IMAGES), len(IMAGES) * PRIX))
        return
    if "--provisoires" in a:
        provisoires()
    if "--payer" in a:
        payer([x for x in a if not x.startswith("--")])
    if "--webp" in a:
        webp()
    if "--mesurer" in a:
        mesurer()
    ecrire_json()


if __name__ == "__main__":
    main()
