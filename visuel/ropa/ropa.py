# -*- coding: utf-8 -*-
"""Les vetements, quatrieme « theme illustre » (3 nov. 2026) : S'HABILLER SELON LA METEO ET L'OCCASION.
ET C'EST FACTURE : 0,15 $ l'image, chez fal -- rien ne part sans l'accord de Jacques, donne dans cette session.

    python visuel/ropa/ropa.py --json            # ropa.json et gloses.json seuls, gratuit
    python visuel/ropa/ropa.py --montrer         # les prompts des images, gratuit
    python visuel/ropa/ropa.py                   # les images qui manquent (0,15 $ chacune)
    python visuel/ropa/ropa.py Anna-lluvia       # celles-la seulement
    python visuel/ropa/ropa.py --refaire Anna-lluvia   # l'ancienne passe en <nom>-rate<k>.png

Pas de magasin (la scene kleidergeschaeft le montre deja, regle 2 de Jacques) : des PERSONNES HABILLEES. Les douze
de « Decrire une personne » (Mark et Anna compris), avec la tenue qu'elles portent deja (gratuite, deja publiee :
visuel/prototype/descripcion/<Nom>.webp), puis deux tenues de situation chacune -- il pleut, il fait froid, il fait
chaud, un mariage, le sport --, faites par RETOUCHE de leur image (nano-banana-pro/edit) : le meme visage, la meme
pose, le meme fond de studio. Le fond reste le studio : une rue sous la pluie donnerait la reponse a « Llueve.
¿Quien va bien vestido? ». La meteo est un pictogramme dessine par la page.

Chaque tenue est decrite PIECE PAR PIECE et COULEUR PAR COULEUR (TENUES) : c'est la meme liste qui fait le prompt
et les questions. Une image ne sert que si elle la respecte ; sinon elle se refait. Une piece dont la couleur ne se
nomme pas sans hesiter (turquoise, beige, corail) n'a pas de couleur (None) ; une piece qu'on n'oserait pas nommer
(le polo de Javier, le haut ample de Marta) est marquee « q »: False -- jamais demandee, mais elle compte comme
portee (on ne la propose pas comme leurre).
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/ropa/img/ (journal : depenses.log).
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "visuel", "prototype", "ropa")
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "ropa", "img")
EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"

# ---------- les pieces ----------
# es : [mot du corpus, article, nombre dans la phrase (s/p), forme ecrite] ; latam : la forme d'Amerique latine
# (espanol/datos/variantes.json) ; de : [mot du corpus, article, forme ecrite, genre de la forme (m, f, n, p)].
# fam : les familles qu'une piece occupe -- un leurre n'est jamais d'une famille deja portee (« unos vaqueros » face
# a un pantalon noir, « una chaqueta » face a un costume se discuteraient).
# deVerbe : comment on la met en allemand (anziehen ; aufsetzen pour ce qui va sur la tete ou le nez ; umbinden).
PIECES = {
    "camiseta":    {"es": ["camiseta", "la", "s", "camiseta"], "de": ["T-Shirt", "das", "T-Shirt", "n"], "fam": ["haut"]},
    "camisa":      {"es": ["camisa", "la", "s", "camisa"], "de": ["Hemd", "das", "Hemd", "n"], "fam": ["haut"]},
    "blusa":       {"es": ["blusa", "la", "s", "blusa"], "de": ["Bluse", "die", "Bluse", "f"], "fam": ["haut"]},
    "jersey":      {"es": ["jersey", "el", "s", "jersey"], "de": ["Pullover", "der", "Pullover", "m"], "fam": ["haut"]},
    "chaqueta":    {"es": ["chaqueta", "la", "s", "chaqueta"], "de": ["Jacke", "die", "Jacke", "f"], "fam": ["dessus"]},
    "abrigo":      {"es": ["abrigo", "el", "s", "abrigo"], "de": ["Mantel", "der", "Mantel", "m"], "fam": ["dessus"]},
    "impermeable": {"es": ["impermeable", "el", "s", "impermeable"], "de": ["Regenjacke", "die", "Regenjacke", "f"], "fam": ["dessus"]},
    "pantalon":    {"es": ["pantalón", "el", "s", "pantalón"], "de": ["Hose", "die", "Hose", "f"], "fam": ["jambes"]},
    "vaqueros":    {"es": ["vaqueros", "los", "p", "vaqueros"], "de": ["Jeans", "die", "Jeans", "f"], "fam": ["jambes"]},
    "cortos":      {"es": ["pantalones cortos", "los", "p", "pantalones cortos"], "de": ["Shorts", "die", "Shorts", "p"], "fam": ["jambes"]},
    "banador":     {"es": ["bañador", "el", "s", "bañador"], "de": ["Badehose", "die", "Badehose", "f"], "fam": ["jambes"]},
    "falda":       {"es": ["falda", "la", "s", "falda"], "de": ["Rock", "der", "Rock", "m"], "fam": ["jambes", "robe"]},
    "vestido":     {"es": ["vestido", "el", "s", "vestido"], "de": ["Kleid", "das", "Kleid", "n"], "fam": ["jambes", "robe", "haut"]},
    "traje":       {"es": ["traje", "el", "s", "traje"], "de": ["Anzug", "der", "Anzug", "m"], "fam": ["dessus", "jambes"]},
    "corbata":     {"es": ["corbata", "la", "s", "corbata"], "de": ["Krawatte", "die", "Krawatte", "f"], "fam": ["cravate"], "deVerbe": "um"},
    "zapatos":     {"es": ["zapato", "el", "p", "zapatos"], "de": ["Schuh", "der", "Schuhe", "p"], "fam": ["pieds"]},
    "zapatillas":  {"es": ["zapatilla", "la", "p", "zapatillas"], "de": ["Turnschuh", "der", "Turnschuhe", "p"], "fam": ["pieds"]},
    "botas":       {"es": ["bota", "la", "p", "botas"], "de": ["Stiefel", "der", "Stiefel", "p"], "fam": ["pieds"]},
    "sandalias":   {"es": ["sandalia", "la", "p", "sandalias"], "de": ["Sandale", "die", "Sandalen", "p"], "fam": ["pieds"]},
    "sombrero":    {"es": ["sombrero", "el", "s", "sombrero"], "de": ["Hut", "der", "Hut", "m"], "fam": ["tete"], "deVerbe": "auf"},
    "gorra":       {"es": ["gorra", "la", "s", "gorra"], "de": ["Kappe", "die", "Kappe", "f"], "fam": ["tete"], "deVerbe": "auf"},
    "gorro":       {"es": ["gorro", "el", "s", "gorro"], "de": ["Mütze", "die", "Mütze", "f"], "fam": ["tete"], "deVerbe": "auf"},
    "bufanda":     {"es": ["bufanda", "la", "s", "bufanda"], "de": ["Schal", "der", "Schal", "m"], "fam": ["cou"], "deVerbe": "um"},
    "guantes":     {"es": ["guante", "el", "p", "guantes"], "de": ["Handschuh", "der", "Handschuhe", "p"], "fam": ["mains"]},
    "gafasSol":    {"es": ["gafas de sol", "las", "p", "gafas de sol"], "de": ["Sonnenbrille", "die", "Sonnenbrille", "f"], "fam": ["lunettes"], "deVerbe": "auf"},
    "paraguas":    {"es": ["paraguas", "el", "s", "paraguas"], "de": ["Regenschirm", "der", "Regenschirm", "m"], "fam": ["parapluie"], "deVerbe": None},
}
# Ce qui manque aux corpus (3 nov.), a ajouter avec l'accord de Jacques : les reponses sur ces mots ne comptent pas
# tant qu'ils n'y sont pas (l'app les dit « hors jeu »), mais ils servent deja dans les phrases.
ABSENTS = {"es": ["impermeable", "pantalones cortos"], "de": ["Shorts", "Badehose", "Sonnenbrille"]}

# Les couleurs : es [masc. sing., fem. sing., masc. plur., fem. plur.], de le radical (rosa ne se decline pas).
COULEURS = {
    "rojo":     {"es": ["rojo", "roja", "rojos", "rojas"], "de": "rot", "en": "red"},
    "azul":     {"es": ["azul", "azul", "azules", "azules"], "de": "blau", "en": "blue"},
    "verde":    {"es": ["verde", "verde", "verdes", "verdes"], "de": "grün", "en": "green"},
    "amarillo": {"es": ["amarillo", "amarilla", "amarillos", "amarillas"], "de": "gelb", "en": "yellow"},
    "negro":    {"es": ["negro", "negra", "negros", "negras"], "de": "schwarz", "en": "black"},
    "blanco":   {"es": ["blanco", "blanca", "blancos", "blancas"], "de": "weiß", "en": "white"},
    "gris":     {"es": ["gris", "gris", "grises", "grises"], "de": "grau", "en": "grey"},
    "marron":   {"es": ["marrón", "marrón", "marrones", "marrones"], "de": "braun", "en": "brown"},
    "rosa":     {"es": ["rosa", "rosa", "rosa", "rosa"], "de": "rosa", "en": "pink"},
}
# Les couleurs qu'une photo peut faire hesiter (le bleu marine et le noir, le gris fonce et le noir...) : jamais
# l'une comme leurre de l'autre.
VOISINES = {"negro": ["gris", "azul", "marron"], "gris": ["negro", "blanco", "azul"], "azul": ["negro", "gris", "verde"],
            "verde": ["azul"], "rojo": ["rosa", "marron"], "rosa": ["rojo"], "marron": ["negro", "rojo"], "blanco": ["gris"], "amarillo": []}

# ---------- les situations ----------
SITUATIONS = ["diario", "lluvia", "frio", "calor", "boda", "deporte"]
# le mot que la question « quel temps, quelle occasion » fait avancer (forme du corpus)
MOT_SITUATION = {"es": {"lluvia": {"mot": "lluvia", "genre": "la"}, "frio": {"mot": "frío", "cat": "adjectif"}, "calor": {"mot": "calor", "genre": "el"},
                        "boda": {"mot": "boda", "genre": "la"}, "deporte": {"mot": "deporte", "genre": "el"}},
                 "de": {"lluvia": {"mot": "Regen", "genre": "der"}, "frio": {"mot": "kalt", "cat": "adjectif"}, "calor": {"mot": "heiß", "cat": "adjectif"},
                        "boda": {"mot": "Hochzeit", "genre": "die"}, "deporte": {"mot": "Sport", "genre": "der"}}}
# Ce qui est TYPIQUE d'une situation (la bonne reponse de « ¿Que se pone? »), et ce qui y est franchement deplace (ses
# leurres). Rien de discutable : des lunettes de soleil sous la neige, un chapeau sous la pluie ne sont pas des fautes,
# ils ne sont donc ni l'un ni l'autre.
TYPIQUE = {"lluvia": ["impermeable", "botas", "paraguas"], "frio": ["abrigo", "bufanda", "gorro", "guantes", "botas"],
           "calor": ["sandalias", "sombrero", "gafasSol", "cortos"], "boda": ["traje", "corbata", "vestido"],
           "deporte": ["zapatillas", "cortos", "gorra"]}
DEPLACE = {"lluvia": ["sandalias", "banador", "cortos", "gafasSol"], "frio": ["sandalias", "banador", "cortos"],
           "calor": ["abrigo", "bufanda", "gorro", "guantes"], "boda": ["banador", "cortos", "gorra", "impermeable"],
           "deporte": ["traje", "corbata", "vestido"]}
# « Llueve. ¿Quien va bien vestido? » : les tenues qui ne vont franchement pas (le sport par la chaleur, si : jamais
# l'un contre l'autre)
CONTRAIRES = {"lluvia": ["calor", "boda", "deporte"], "frio": ["calor", "boda", "deporte"], "calor": ["frio", "lluvia", "boda"],
              "boda": ["calor", "deporte", "lluvia", "frio"], "deporte": ["boda", "frio", "lluvia"]}
# ponerse / quitarse, anziehen / ausziehen : ce qu'on met en sortant (pone) et qu'on enleve en rentrant (quita)
METTRE = {"diario": {"pone": ["chaqueta", "zapatos", "zapatillas", "botas"], "quita": ["chaqueta", "zapatos", "zapatillas", "botas"]},
          "lluvia": {"pone": ["impermeable", "botas"], "quita": ["impermeable", "botas"]},
          "frio": {"pone": ["abrigo", "bufanda", "gorro", "guantes", "botas"], "quita": ["abrigo", "bufanda", "gorro", "guantes", "botas"]},
          "calor": {"pone": ["sombrero", "gafasSol", "gorra"], "quita": ["sandalias", "camiseta"]},
          "boda": {"pone": ["traje", "corbata", "vestido", "zapatos"], "quita": ["corbata", "zapatos", "traje"]},
          "deporte": {"pone": ["zapatillas", "gorra", "cortos"], "quita": ["zapatillas"]}}

# ---------- les personnes et leurs tenues ----------
SEXE = {"Mark": "m", "Anna": "f", "Diego": "m", "Elena": "f", "Pablo": "m", "Marta": "f", "Javier": "m", "Ines": "f",
        "Tomas": "m", "Carmen": "f", "Lucas": "m", "Rosa": "f"}
NOMS = {"Ines": "Inés", "Tomas": "Tomás"}
# Ce que la personne porte toujours (personnages.json de Descripcion) : des lunettes de vue ou de soleil occupent la
# famille « lunettes » (Lucas porte les siennes partout, c'est son signe ; sa piece gafasSol est dans chaque tenue).
LUNETTES = {"Diego", "Marta", "Carmen", "Lucas"}
# La tenue de tous les jours, LUE sur l'image publiee de Descripcion (verifiee le 3 nov. sur la planche des dix et sur
# Mark et Anna) : [piece, couleur ou None] ou [piece, couleur, {"q": False}].
NQ = {"q": False}
TENUES_DIARIO = {
    "Mark":   [["chaqueta", "gris"], ["camiseta", "negro"], ["vaqueros", "azul"], ["zapatillas", "negro"]],
    "Anna":   [["camisa", "azul"], ["pantalon", "negro"], ["zapatos", "negro"]],
    "Diego":  [["camiseta", "azul"], ["vaqueros", "azul"], ["zapatillas", "blanco"]],
    "Elena":  [["camiseta", "rosa"], ["pantalon", "negro"], ["zapatillas", "blanco"]],
    "Pablo":  [["camiseta", "verde"], ["pantalon", None], ["zapatos", "marron"]],
    "Marta":  [["camiseta", "amarillo", NQ], ["pantalon", "verde"], ["zapatos", "negro"]],
    "Javier": [["camiseta", "rojo", NQ], ["vaqueros", "azul"], ["zapatos", "negro"]],
    "Ines":   [["camiseta", None], ["vaqueros", "negro"], ["zapatillas", "blanco"]],
    "Tomas":  [["camiseta", None], ["pantalon", None], ["zapatillas", "gris"]],
    "Carmen": [["blusa", "azul"], ["pantalon", "negro"], ["zapatos", "negro"]],
    "Lucas":  [["camiseta", None], ["vaqueros", "azul"], ["botas", "marron"], ["gafasSol", None]],
    "Rosa":   [["camiseta", None, NQ], ["pantalon", "gris"], ["zapatillas", "blanco"]],
}
# Les 24 tenues de situation : chacun des douze en a deux. L'ordre des pieces est celui de la phrase.
# 3 nov., apres verification des 24 images : les bottines de Pablo, Javier, Diego et Carmen, sous le pantalon, se
# lisent comme des chaussures -- NQ : portees, jamais demandees (« zapatos » serait aussi juste).
TENUES = {
    "Anna-lluvia":    [["impermeable", "amarillo"], ["vaqueros", "azul"], ["botas", "verde"], ["paraguas", "rojo"]],
    "Elena-lluvia":   [["impermeable", "rojo"], ["pantalon", "negro"], ["botas", "amarillo"], ["paraguas", "azul"]],
    "Pablo-lluvia":   [["impermeable", "azul"], ["pantalon", "gris"], ["botas", "negro", NQ], ["paraguas", "verde"]],
    "Javier-lluvia":  [["impermeable", "verde"], ["vaqueros", "azul"], ["botas", "marron", NQ], ["paraguas", "negro"]],
    "Rosa-lluvia":    [["impermeable", "rosa"], ["pantalon", "negro"], ["botas", "rojo"], ["paraguas", "amarillo"]],
    "Mark-frio":      [["abrigo", "negro"], ["bufanda", "rojo"], ["gorro", "gris"], ["guantes", "negro"], ["vaqueros", "azul"], ["botas", "marron"]],
    "Diego-frio":     [["abrigo", "marron"], ["bufanda", "verde"], ["gorro", "verde"], ["guantes", "marron"], ["vaqueros", "azul"], ["botas", "negro", NQ]],
    "Marta-frio":     [["abrigo", "rojo"], ["bufanda", "blanco"], ["gorro", "blanco"], ["guantes", "rojo"], ["pantalon", "negro"], ["botas", "negro"]],
    "Carmen-frio":    [["abrigo", "azul"], ["bufanda", "amarillo"], ["gorro", "rojo"], ["guantes", "azul"], ["pantalon", "negro"], ["botas", "marron", NQ]],
    "Lucas-frio":     [["abrigo", "gris"], ["bufanda", "azul"], ["gorro", "azul"], ["guantes", "negro"], ["vaqueros", "azul"], ["botas", "marron"], ["gafasSol", None]],
    "Anna-calor":     [["camiseta", "rojo"], ["falda", "blanco"], ["sombrero", None], ["gafasSol", None], ["sandalias", "marron"]],
    "Pablo-calor":    [["camiseta", "blanco"], ["cortos", "azul"], ["gorra", "rojo"], ["gafasSol", None], ["sandalias", "negro"]],
    "Ines-calor":     [["vestido", "amarillo"], ["sombrero", "blanco"], ["gafasSol", None], ["sandalias", "blanco"]],
    "Tomas-calor":    [["camiseta", "blanco"], ["banador", "rojo"], ["gafasSol", None], ["sandalias", "marron"]],
    "Rosa-calor":     [["camiseta", "verde"], ["cortos", "blanco"], ["sombrero", None], ["sandalias", "negro"]],
    "Mark-boda":      [["traje", "azul"], ["camisa", "blanco"], ["corbata", "rojo"], ["zapatos", "negro"]],
    "Marta-boda":     [["vestido", "azul"], ["zapatos", "azul"]],
    "Javier-boda":    [["traje", "negro"], ["camisa", "blanco"], ["corbata", "amarillo"], ["zapatos", "negro"]],
    "Ines-boda":      [["vestido", "verde"], ["zapatos", "negro"]],
    "Carmen-boda":    [["vestido", "rosa"], ["zapatos", "blanco"]],
    "Diego-deporte":  [["camiseta", "amarillo"], ["cortos", "negro"], ["zapatillas", "blanco"]],
    "Elena-deporte":  [["camiseta", "azul"], ["cortos", "gris"], ["zapatillas", "blanco"], ["gorra", "rosa"]],
    "Tomas-deporte":  [["camiseta", "gris"], ["cortos", "azul"], ["zapatillas", "rojo"]],
    "Lucas-deporte":  [["camiseta", "rojo"], ["pantalon", "negro"], ["zapatillas", "blanco"], ["gorra", "azul"], ["gafasSol", None]],
}

# ---------- les prompts (les memes listes) ----------
EN_PIECE = {"camiseta": "a plain short-sleeved t-shirt", "camisa": "a long-sleeved button-up shirt", "blusa": "a blouse",
            "jersey": "a knitted jumper", "chaqueta": "a jacket", "abrigo": "a long warm winter coat, closed",
            "impermeable": "a hooded rain jacket (raincoat), closed", "pantalon": "long trousers", "vaqueros": "jeans",
            "cortos": "knee-length shorts", "banador": "knee-length swim shorts", "falda": "a knee-length skirt",
            "vestido": "a dress", "traje": "a two-piece suit (jacket and matching trousers)", "corbata": "a tie",
            "zapatos": "leather shoes", "zapatillas": "running sneakers", "botas": "boots", "sandalias": "sandals",
            "sombrero": "a wide-brimmed sun hat", "gorra": "a baseball cap", "gorro": "a knitted woolly hat",
            "bufanda": "a thick scarf around the neck", "guantes": "warm gloves on both hands", "gafasSol": "sunglasses",
            "paraguas": "a closed umbrella held in one hand, its tip resting on the floor"}
EN_PIECE_SANS_COULEUR = {"sombrero": "a natural straw sun hat with a wide brim", "gafasSol": "dark sunglasses"}
CONTEXTE = {"lluvia": "dressed for a rainy day", "frio": "dressed warmly for a cold, snowy winter day",
            "calor": "dressed for a hot summer day at the beach", "boda": "dressed elegantly as a guest at a wedding",
            "deporte": "dressed to go jogging"}
MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same body and build, the same glasses, sunglasses, beard, earrings or tattoo if any. ")
CADRE = (" Nothing else is worn: no other jacket, hat, bag or accessory, and the colours are exactly the ones given, clearly "
         "visible. A photorealistic photograph, natural skin texture, no retouching. Full body from head to feet, standing "
         "straight, facing the camera, arms naturally at the sides, a friendly "
         "natural smile. The whole body fills the height of the picture with a small even margin above the head and below "
         "the feet. Plain light grey studio background with even soft light, nothing else in the picture, no text, no logos.")


def prompt(nom):
    p, sit = nom.split("-")
    morceaux = []
    for piece, couleur, *_ in TENUES[nom]:
        if couleur is None:
            morceaux.append(EN_PIECE_SANS_COULEUR.get(piece, EN_PIECE[piece]))
        else:
            mot = EN_PIECE[piece]
            art, reste = (mot.split(" ", 1) + [""])[:2] if mot.startswith(("a ", "an ")) else ("", mot)
            morceaux.append(("a " if art else "") + COULEURS[couleur]["en"].upper() + " " + (reste if art else mot))
    vetu = ", ".join(morceaux[:-1]) + " and " + morceaux[-1]
    return MEME + "Now %s, wearing: %s." % (CONTEXTE[sit], vetu) + CADRE


def sources():
    s = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png"}
    for n in SEXE:
        s.setdefault(n, PRINCIPAL + "/visuel/descripcion/img/" + n + ".png")
    return s


# ---------- les phrases (la page fabrique les siennes avec la meme regle) ----------
def es_piece(piece, couleur, latam, defini=False):
    mot, art, nb, forme = PIECES[piece]["es"]
    var = VARIANTES.get(mot) if latam else None
    genre = art in ("la", "las")
    if var:
        genre = var["genre"] in ("la", "las")
        forme = var["mot"] if nb == "s" else var["pluriel"]
    if defini:
        a = ("las" if genre else "los") if nb == "p" else ("la" if genre else "el")
    else:
        a = ("unas" if genre else "unos") if nb == "p" else ("una" if genre else "un")
    c = ""
    if couleur:
        c = " " + COULEURS[couleur]["es"][(2 if nb == "p" else 0) + (1 if genre else 0)]
    return a + " " + forme + c


def de_piece(piece, couleur):
    """accusatif apres « tragt » : einen roten Mantel, eine rote Jacke, ein rotes Kleid, rote Schuhe."""
    mot, art, forme, g = PIECES[piece]["de"]
    a = {"m": "einen ", "f": "eine ", "n": "ein ", "p": ""}[g]
    c = ""
    if couleur:
        r = COULEURS[couleur]["de"]
        c = (r if r == "rosa" else r + {"m": "en", "f": "e", "n": "es", "p": "e"}[g]) + " "
    return a + c + forme


def liste(morceaux, et):
    return morceaux[0] if len(morceaux) == 1 else ", ".join(morceaux[:-1]) + " " + et + " " + morceaux[-1]


SIT_ES = {"lluvia": "Llueve.", "frio": "Hace frío.", "calor": "Hace calor.", "boda": "{P} va a una boda.", "deporte": "{P} va a hacer deporte."}
SIT_DE = {"lluvia": "Es regnet.", "frio": "Es ist kalt.", "calor": "Es ist heiß.", "boda": "{P} geht zu einer Hochzeit.", "deporte": "{P} macht Sport."}


def phrase(langue, p, sit, pieces):
    """« Llueve. Anna lleva un impermeable amarillo, unas botas verdes y un paraguas rojo. »"""
    n = NOMS.get(p, p)
    vus = [x for x in pieces if len(x) < 3 or x[2].get("q", True)]
    if langue == "de":
        corps = "%s trägt %s." % (n, liste([de_piece(x[0], x[1]) for x in vus], "und"))
        intro = SIT_DE.get(sit)
    else:
        lis = [es_piece(x[0], x[1], langue == "latam") for x in vus]
        # « y » devient « e » devant un son « i » : « un abrigo e impermeable » n'arrive pas ici (toujours un article)
        corps = "%s lleva %s." % (n, liste(lis, "y"))
        intro = SIT_ES.get(sit)
    if intro:
        intro = intro.replace("{P}", n)
        if "{P}" in (SIT_DE.get(sit, "") if langue == "de" else SIT_ES.get(sit, "")):
            # « Marta va a una boda. Lleva un vestido azul. » / « Marta geht zu einer Hochzeit. Sie trägt... » : le
            # prenom ne se repete pas
            if langue == "de":
                corps = ("Sie " if SEXE[p] == "f" else "Er ") + corps[len(n) + 1:]
            else:
                corps = corps[len(n) + 1:]
                corps = corps[0].upper() + corps[1:]
        return intro + " " + corps
    return corps


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def lire(p):
    return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))


VARIANTES = lire("espanol/datos/variantes.json")["noms"]


def toutes_les_tenues():
    """{cle: {p, sit, img, pieces}} -- les tenues de tous les jours et celles de situation dont l'image est faite."""
    out = {}
    for p, pieces in TENUES_DIARIO.items():
        out[p + "-diario"] = {"p": p, "sit": "diario", "img": "descripcion/" + p + ".webp", "pieces": pieces}
    for nom, pieces in TENUES.items():
        p, sit = nom.split("-")
        img = "ropa/" + nom + ".webp"
        out[nom] = {"p": p, "sit": sit, "img": img, "pieces": pieces,
                    "faite": os.path.exists(os.path.join(RACINE, "visuel", "prototype", img))}
    return out


def verifier():
    fautes = []
    for nom, t in toutes_les_tenues().items():
        fams = [f for x in t["pieces"] for f in PIECES[x[0]]["fam"]]
        if len(fams) != len(set(fams)) and t["sit"] != "diario":
            fautes.append("%s : deux pieces de la meme famille" % nom)
        for x in t["pieces"]:
            if x[0] not in PIECES or (x[1] and x[1] not in COULEURS):
                fautes.append("%s : %s inconnu" % (nom, x))
        if t["p"] in LUNETTES and t["p"] != "Lucas" and any(x[0] == "gafasSol" for x in t["pieces"]):
            fautes.append("%s : lunettes de soleil sur des lunettes de vue" % nom)
    par = {}
    for nom in TENUES:
        par.setdefault(nom.split("-")[0], []).append(nom)
    fautes += ["%s : %d tenues de situation" % (p, len(v)) for p, v in par.items() if len(v) != 2]
    return fautes


def ecrire_json():
    tenues = toutes_les_tenues()
    dec = {l: {} for l in ("es", "latam", "de")}
    for nom, t in tenues.items():
        for l in dec:
            tx = phrase(l, t["p"], t["sit"], t["pieces"])
            dec[l][nom] = {"texte": tx, "son": identifiant(tx)}
    metres = {p: v["metres"] for p, v in lire("visuel/prototype/descripcion/personnages.json").items() if p in SEXE}
    d = {"_lisez_moi": "DERIVE de visuel/ropa/ropa.py (python visuel/ropa/ropa.py --json) : le refaire, pas le corriger.",
         "sexe": SEXE, "noms": NOMS, "metres": metres, "lunettes": sorted(LUNETTES),
         "pieces": PIECES, "couleurs": COULEURS, "voisines": VOISINES, "variantes": {k: v for k, v in VARIANTES.items()
                                                                                 if k in {PIECES[x]["es"][0] for x in PIECES}},
         "situations": SITUATIONS, "motSituation": MOT_SITUATION, "typique": TYPIQUE, "deplace": DEPLACE,
         "contraires": CONTRAIRES, "mettre": METTRE, "absents": ABSENTS,
         "tenues": {k: v for k, v in tenues.items() if v.get("faite", True)},
         "phrases": {l: {k: v for k, v in dec[l].items() if tenues[k].get("faite", True)} for l in dec}}
    os.makedirs(SORTIE, exist_ok=True)
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    io.open(os.path.join(SORTIE, "ropa.json"), "w", encoding="utf-8", newline="\n").write(texte)
    return d


def ecrire_gloses():
    """La traduction des mots du theme, tiree du CORPUS relu, pour les langues d'interface ou la page ne traduit pas
    la phrase (ar, tr, uk, fa, pl, ru) : « el abrigo — معطف ». Cle : article et mot (un nom), le mot seul (un adjectif,
    un verbe). Comme familia/gloses.json. Les mots absents du corpus n'ont pas de glose."""
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}

    def plats(p, cle):
        out = []
        def tour(x):
            if isinstance(x, dict):
                if cle in x and isinstance(x[cle], str):
                    out.append(x)
                else:
                    for v in x.values():
                        tour(v)
            elif isinstance(x, list):
                for v in x:
                    tour(v)
        tour(lire(p))
        return out
    noms = lambda p: [m for t in lire(p)["themes"] for m in t["mots"]]
    out = {"de": {}, "es": {}}
    for l, fnoms, fadj, fverb, champs in (("de", "themes.json", "adjectif.json", "verbe.json", LDE),
                                           ("es", "espanol/datos/temas.json", "espanol/datos/adjetivos.json", "espanol/datos/verbos.json", LES)):
        vNoms = {(PIECES[x][l][1], PIECES[x][l][0]) for x in PIECES}
        vNoms |= {(m["genre"], m["mot"]) for m in MOT_SITUATION[l].values() if m.get("genre")}
        vAdj = {COULEURS[c][l] if l == "de" else COULEURS[c]["es"][0] for c in COULEURS} | {m["mot"] for m in MOT_SITUATION[l].values() if m.get("cat")}
        vVerb = {"de": {"tragen", "anziehen", "ausziehen"}, "es": {"llevar", "ponerse", "quitarse"}}[l]
        for m in noms(fnoms):
            if (m.get("genre"), m["mot"]) in vNoms:
                out[l].setdefault(m["genre"] + " " + m["mot"], {k: m[c] for k, c in champs.items() if m.get(c)})
        for e in plats(fadj, "mot"):
            if e["mot"] in vAdj:
                out[l].setdefault(e["mot"], {k: e[c] for k, c in champs.items() if e.get(c)})
        for e in plats(fverb, "infinitif"):
            if e["infinitif"] in vVerb:
                out[l].setdefault(e["infinitif"], {k: e[c] for k, c in champs.items() if e.get(c)})
    io.open(os.path.join(SORTIE, "gloses.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return out


def textes_a_dire(langue):
    """Pour les inventaires des voix : les phrases de la decouverte (es, latam, de)."""
    d = json.load(io.open(os.path.join(SORTIE, "ropa.json"), encoding="utf-8"))
    return [v["texte"] for v in d["phrases"][langue].values()]


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    fautes = verifier()
    if fautes:
        sys.exit("  tenues fautives :\n  " + "\n  ".join(fautes))
    d = ecrire_json()
    g = ecrire_gloses()
    print("  ropa.json : %d tenues (%d de situation) ; gloses : es %d, de %d" % (len(d["tenues"]), sum(1 for t in d["tenues"].values() if t["sit"] != "diario"), len(g["es"]), len(g["de"])))
    if "--json" in sys.argv:
        return
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(TENUES)
    inconnus = [n for n in noms if n not in TENUES]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(DOSSIER, exist_ok=True)
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
    if montrer:
        for n in a_faire:
            print("\n  %s  (source : %s)\n  %s" % (n, sources()[n.split("-")[0]], prompt(n)))
        return
    if not os.environ.get("FAL_KEY") and os.path.exists(PRINCIPAL + "/fal.secret"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    depots = {}
    for nom in a_faire:
        p = nom.split("-")[0]
        texte = prompt(nom)
        print("\n  %s\n  %s" % (nom, texte))
        if p not in depots:
            depots[p] = O.deposer(sources()[p], "image/png", cle)[0]
        corps = {"prompt": texte, "image_urls": [depots[p]], "aspect_ratio": "9:16", "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": texte, "source": sources()[p], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
