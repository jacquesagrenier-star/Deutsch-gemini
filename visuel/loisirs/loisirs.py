# -*- coding: utf-8 -*-
"""« Les loisirs », theme illustre de la vague 2 (3 nov. 2026), en espagnol et en allemand. LA SEULE SOURCE du theme :
les activites, les personnes, leurs fiches (ce qu'elles aiment, a quelle frequence), les morceaux de phrases dans les
langues apprises et dans les langues de traduction, les gloses du corpus et les prompts des images.

    python visuel/loisirs/loisirs.py                 # loisirs.json et gloses.json seuls (gratuit)
    python visuel/loisirs/loisirs.py --montrer       # les prompts des images et leur cout (gratuit)
    python visuel/loisirs/loisirs.py --provisoires   # des images d'essai (photo de la personne + etiquette), A NE PAS COMMITTER
    python visuel/loisirs/loisirs.py --payer futbol guitarra   # FACTURE, 0,15 $ l'image (accord de Jacques d'abord)
    python visuel/loisirs/loisirs.py --webp          # les originaux -> visuel/prototype/loisirs/<activite>.webp
    python visuel/loisirs/loisirs.py --visages       # les visages ronds des fiches (gratuit)

Ce qu'on y apprend (demande du chef d'orchestre, 3 nov.) :
  - ce qu'on aime faire : « A Heinz le gusta leer » (me gusta + infinitif, le pronom le / les), « Heinz liest gern »
    (gern apres le verbe, nicht gern) ;
  - jugar ou tocar (jugar AL futbol, tocar LA guitarra), spielen, machen ou fahren (Fussball spielen, Sport machen,
    Rad fahren) ;
  - la frequence : siempre, a menudo, a veces, rara vez, nunca ; immer, oft, manchmal, selten, nie -- montree par un
    calendrier de quatre semaines (28, 16, 6, 1, 0 jours), jamais par une phrase seule ;
  - proposer une sortie : ¿Quieres + infinitif? ¿Vamos a + infinitif? ; Hast du Lust, ... zu + infinitif? Wollen wir
    ... + infinitif? ; et repondre selon ce que la personne aime (sa fiche).
Les instruments sont ceux de la scene de la musique (Gitarre, Klavier, Geige ; guitarra, piano, violin).

UNE IMAGE PAR ACTIVITE (15), chacune avec UNE personne deja faite (Decrire une personne, la famille d'Anna), par
RETOUCHE de son image en pied (nano-banana-pro/edit) : le meme visage, sur le fond de studio gris clair des autres
themes. Aucun lieu connu n'est montre (decision du 3 nov. sur la continuite des lieux : rien a reprendre des scenes).
Ce que l'image ne montre pas (aimer, la frequence) est montre par la FICHE de la personne (son visage, un coeur ou une
croix devant le pictogramme de l'activite) et par le CALENDRIER : la page dessine les deux depuis cette donnee, et
aucune question ne dit autre chose que ce qui est a l'ecran.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/loisirs/img/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype", "loisirs")
IMG = os.path.join(os.path.expanduser("~"), ".wortando", "loisirs", "img")
EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
# Les sources, en pied, 1536 x 2752 : le depot principal (Decrire une personne) et la famille d'Anna (hors depot)
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
DESCRIPCION = ("Carmen", "Diego", "Marta", "Javier", "Rosa", "Lucas", "Tomas", "Elena", "Ines", "Pablo")

# ---------------------------------------------------------------------------------------------------------------
# LES PERSONNES : leur nom a l'ecran, leur sexe (obrigado / obrigada, el / la), le dossier de leur visage
PERSONNES = {
    "Felix":  ("Felix", "m", "familia"),   "Rosa":   ("Rosa", "f", "descripcion"),  "Diego":  ("Diego", "m", "descripcion"),
    "Ines":   ("Inés", "f", "descripcion"), "Gisela": ("Gisela", "f", "familia"),   "Sophie": ("Sophie", "f", "familia"),
    "Tomas":  ("Tomás", "m", "descripcion"), "Katrin": ("Katrin", "f", "familia"),  "Javier": ("Javier", "m", "descripcion"),
    "Elena":  ("Elena", "f", "descripcion"), "Carmen": ("Carmen", "f", "descripcion"), "Heinz": ("Heinz", "m", "familia"),
    "Pablo":  ("Pablo", "m", "descripcion"), "Marta":  ("Marta", "f", "descripcion"), "Lena":   ("Lena", "f", "familia"),
}

# ---------------------------------------------------------------------------------------------------------------
# LES ACTIVITES. Pour chacune : la personne de la photo et ce que l'image doit montrer ; puis les morceaux de phrase.
#   es : v (il / elle), vpl (ils), reste (« al futbol »), inf (« jugar al futbol »), verbe (l'infinitif du corpus),
#        nom ([mot, article] du corpus ou None), art (l'article apres le verbe, pour « al, el, la ? »), sorte
#   de : v, vpl, ich, reste (« Fussball », « Rad » ; rien pour tanzen), inf (l'infinitif seul), verbe, nom, sorte
#   fr : v, vpl, reste, neg (le reste apres « ne ... jamais » : « de velo »), inf
#   en : v3 (« plays soccer »), vpl, inf, ing
#   pt (portugais du Bresil, la langue d'interface) : v3, vpl, inf
A = {}
def activite(id, qui, montre, es, de, fr, en, pt):
    A[id] = {"qui": qui, "montre": montre, "es": es, "de": de, "fr": fr, "en": en, "pt": pt}

SPORT = ("in comfortable sportswear (a plain t-shirt or jersey, sports shorts or leggings, sports shoes) instead of "
         "the usual clothes, ")
activite("futbol", "Felix", SPORT + "playing football: kicking a classic black-and-white football with the right foot, the ball in the air just in front of the foot, a dynamic, joyful pose.",
         {"v": "juega", "vpl": "juegan", "reste": "al fútbol", "inf": "jugar al fútbol", "verbe": "jugar", "nom": ["fútbol", "el"], "art": "al", "sorte": "jugar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Fußball", "inf": "spielen", "verbe": "spielen", "nom": ["Fußball", "der"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "au football", "neg": "au football", "inf": "jouer au football"},
         {"v3": "plays soccer", "vpl": "play soccer", "inf": "play soccer", "ing": "playing soccer"},
         {"v3": "joga futebol", "vpl": "jogam futebol", "inf": "jogar futebol"})
activite("tenis", "Rosa", SPORT + "playing tennis: hitting a yellow tennis ball with a tennis racket in a forehand swing, the ball clearly visible next to the racket.",
         {"v": "juega", "vpl": "juegan", "reste": "al tenis", "inf": "jugar al tenis", "verbe": "jugar", "nom": ["tenis", "el"], "art": "al", "sorte": "jugar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Tennis", "inf": "spielen", "verbe": "spielen", "nom": ["Tennis", "das"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "au tennis", "neg": "au tennis", "inf": "jouer au tennis"},
         {"v3": "plays tennis", "vpl": "play tennis", "inf": "play tennis", "ing": "playing tennis"},
         {"v3": "joga tênis", "vpl": "jogam tênis", "inf": "jogar tênis"})
activite("baloncesto", "Diego", SPORT + "playing basketball: dribbling an orange basketball with one hand, the ball bouncing near the floor, the other arm out for balance.",
         {"v": "juega", "vpl": "juegan", "reste": "al baloncesto", "inf": "jugar al baloncesto", "verbe": "jugar", "nom": ["baloncesto", "el"], "art": "al", "sorte": "jugar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Basketball", "inf": "spielen", "verbe": "spielen", "nom": ["Basketball", "der"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "au basket", "neg": "au basket", "inf": "jouer au basket"},
         {"v3": "plays basketball", "vpl": "play basketball", "inf": "play basketball", "ing": "playing basketball"},
         {"v3": "joga basquete", "vpl": "jogam basquete", "inf": "jogar basquete"})
activite("guitarra", "Ines", "playing an acoustic guitar: sitting on a simple wooden stool, the guitar resting on the knee, the fingers of the left hand on the neck and the right hand strumming the strings, smiling.",
         {"v": "toca", "vpl": "tocan", "reste": "la guitarra", "inf": "tocar la guitarra", "verbe": "tocar", "nom": ["guitarra", "la"], "art": "la", "sorte": "tocar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Gitarre", "inf": "spielen", "verbe": "spielen", "nom": ["Gitarre", "die"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "de la guitare", "neg": "de la guitare", "inf": "jouer de la guitare"},
         {"v3": "plays the guitar", "vpl": "play the guitar", "inf": "play the guitar", "ing": "playing the guitar"},
         {"v3": "toca violão", "vpl": "tocam violão", "inf": "tocar violão"})
activite("piano", "Gisela", "playing the piano: sitting on a piano bench at a black upright piano, seen from the side and slightly from the front so that her face is visible, both hands on the keys, enjoying the music.",
         {"v": "toca", "vpl": "tocan", "reste": "el piano", "inf": "tocar el piano", "verbe": "tocar", "nom": ["piano", "el"], "art": "el", "sorte": "tocar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Klavier", "inf": "spielen", "verbe": "spielen", "nom": ["Klavier", "das"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "du piano", "neg": "du piano", "inf": "jouer du piano"},
         {"v3": "plays the piano", "vpl": "play the piano", "inf": "play the piano", "ing": "playing the piano"},
         {"v3": "toca piano", "vpl": "tocam piano", "inf": "tocar piano"})
activite("violin", "Sophie", "playing the violin: standing, the violin held under the chin on the left shoulder, the bow drawn across the strings with the right hand, concentrated and happy.",
         {"v": "toca", "vpl": "tocan", "reste": "el violín", "inf": "tocar el violín", "verbe": "tocar", "nom": ["violín", "el"], "art": "el", "sorte": "tocar"},
         {"v": "spielt", "vpl": "spielen", "ich": "spiele", "reste": "Geige", "inf": "spielen", "verbe": "spielen", "nom": ["Geige", "die"], "sorte": "spielen"},
         {"v": "joue", "vpl": "jouent", "reste": "du violon", "neg": "du violon", "inf": "jouer du violon"},
         {"v3": "plays the violin", "vpl": "play the violin", "inf": "play the violin", "ing": "playing the violin"},
         {"v3": "toca violino", "vpl": "tocam violino", "inf": "tocar violino"})
activite("bici", "Tomas", "wearing a bicycle helmet, riding a city bicycle: sitting on the saddle and pedalling, both hands on the handlebars, seen from the side, the whole bicycle visible, the face turned towards the camera, smiling.",
         {"v": "monta", "vpl": "montan", "reste": "en bicicleta", "inf": "montar en bicicleta", "verbe": "montar", "nom": ["bicicleta", "la"], "art": None, "sorte": "montar"},
         {"v": "fährt", "vpl": "fahren", "ich": "fahre", "reste": "Rad", "inf": "fahren", "verbe": "fahren", "nom": ["Rad", "das"], "sorte": "fahren"},
         {"v": "fait", "vpl": "font", "reste": "du vélo", "neg": "de vélo", "inf": "faire du vélo"},
         {"v3": "rides a bike", "vpl": "ride a bike", "inf": "ride a bike", "ing": "riding a bike"},
         {"v3": "anda de bicicleta", "vpl": "andam de bicicleta", "inf": "andar de bicicleta"})
activite("deporte", "Katrin", SPORT + "exercising: lifting a small dumbbell in each hand above the shoulders, a rolled-out exercise mat and a water bottle on the floor next to her, energetic and smiling.",
         {"v": "hace", "vpl": "hacen", "reste": "deporte", "inf": "hacer deporte", "verbe": "hacer", "nom": ["deporte", "el"], "art": None, "sorte": "hacer"},
         {"v": "macht", "vpl": "machen", "ich": "mache", "reste": "Sport", "inf": "machen", "verbe": "machen", "nom": ["Sport", "der"], "sorte": "machen"},
         {"v": "fait", "vpl": "font", "reste": "du sport", "neg": "de sport", "inf": "faire du sport"},
         {"v3": "does sports", "vpl": "do sports", "inf": "do sports", "ing": "doing sports"},
         {"v3": "pratica esporte", "vpl": "praticam esporte", "inf": "praticar esporte"})
activite("fotos", "Javier", "taking photos: holding a black camera with a lens up to his eye with both hands, about to take a picture, a camera strap around his neck.",
         {"v": "saca", "vpl": "sacan", "reste": "fotos", "inf": "sacar fotos", "verbe": "sacar", "nom": ["foto", "la"], "art": None, "sorte": "sacar"},
         {"v": "macht", "vpl": "machen", "ich": "mache", "reste": "Fotos", "inf": "machen", "verbe": "machen", "nom": ["Foto", "das"], "sorte": "machen"},
         {"v": "prend", "vpl": "prennent", "reste": "des photos", "neg": "de photos", "inf": "prendre des photos"},
         {"v3": "takes photos", "vpl": "take photos", "inf": "take photos", "ing": "taking photos"},
         {"v3": "tira fotos", "vpl": "tiram fotos", "inf": "tirar fotos"})
activite("bailar", "Elena", "dancing joyfully: caught mid-spin in a lively dance move, one arm raised above the head, the hair and the clothes moving, a big smile.",
         {"v": "baila", "vpl": "bailan", "reste": "", "inf": "bailar", "verbe": "bailar", "nom": None, "art": None, "sorte": None},
         {"v": "tanzt", "vpl": "tanzen", "ich": "tanze", "reste": "", "inf": "tanzen", "verbe": "tanzen", "nom": None, "sorte": None},
         {"v": "danse", "vpl": "dansent", "reste": "", "neg": "", "inf": "danser"},
         {"v3": "dances", "vpl": "dance", "inf": "dance", "ing": "dancing"},
         {"v3": "dança", "vpl": "dançam", "inf": "dançar"})
activite("cantar", "Carmen", "singing: holding a microphone close to the mouth with one hand, the mouth open, singing with joy, the other hand raised.",
         {"v": "canta", "vpl": "cantan", "reste": "", "inf": "cantar", "verbe": "cantar", "nom": None, "art": None, "sorte": None},
         {"v": "singt", "vpl": "singen", "ich": "singe", "reste": "", "inf": "singen", "verbe": "singen", "nom": None, "sorte": None},
         {"v": "chante", "vpl": "chantent", "reste": "", "neg": "", "inf": "chanter"},
         {"v3": "sings", "vpl": "sing", "inf": "sing", "ing": "singing"},
         {"v3": "canta", "vpl": "cantam", "inf": "cantar"})
activite("leer", "Heinz", "reading a book: sitting in a comfortable armchair, holding an open book with both hands, reading attentively with reading glasses on the nose.",
         {"v": "lee", "vpl": "leen", "reste": "", "inf": "leer", "verbe": "leer", "nom": None, "art": None, "sorte": None},
         {"v": "liest", "vpl": "lesen", "ich": "lese", "reste": "", "inf": "lesen", "verbe": "lesen", "nom": None, "sorte": None},
         {"v": "lit", "vpl": "lisent", "reste": "", "neg": "", "inf": "lire"},
         {"v3": "reads", "vpl": "read", "inf": "read", "ing": "reading"},
         {"v3": "lê", "vpl": "leem", "inf": "ler"})
activite("cocinar", "Pablo", "cooking: wearing a kitchen apron over the clothes, standing behind a small table with a portable cooking hob, stirring a pan of vegetables with a wooden spoon, a chopping board with tomatoes next to the pan.",
         {"v": "cocina", "vpl": "cocinan", "reste": "", "inf": "cocinar", "verbe": "cocinar", "nom": None, "art": None, "sorte": None},
         {"v": "kocht", "vpl": "kochen", "ich": "koche", "reste": "", "inf": "kochen", "verbe": "kochen", "nom": None, "sorte": None},
         {"v": "cuisine", "vpl": "cuisinent", "reste": "", "neg": "", "inf": "cuisiner"},
         {"v3": "cooks", "vpl": "cook", "inf": "cook", "ing": "cooking"},
         {"v3": "cozinha", "vpl": "cozinham", "inf": "cozinhar"})
activite("pintar", "Marta", "painting: standing in front of a wooden easel with a canvas on which a colourful landscape is half painted, holding a paintbrush in one hand and a palette of paints in the other.",
         {"v": "pinta", "vpl": "pintan", "reste": "", "inf": "pintar", "verbe": "pintar", "nom": None, "art": None, "sorte": None},
         {"v": "malt", "vpl": "malen", "ich": "male", "reste": "", "inf": "malen", "verbe": "malen", "nom": None, "sorte": None},
         {"v": "peint", "vpl": "peignent", "reste": "", "neg": "", "inf": "peindre"},
         {"v3": "paints", "vpl": "paint", "inf": "paint", "ing": "painting"},
         {"v3": "pinta", "vpl": "pintam", "inf": "pintar"})
activite("correr", "Lena", SPORT + "jogging: running at an easy pace, caught mid-stride with one foot off the floor, seen from the side, the face turned towards the camera, smiling.",
         {"v": "corre", "vpl": "corren", "reste": "", "inf": "correr", "verbe": "correr", "nom": None, "art": None, "sorte": None},
         {"v": "joggt", "vpl": "joggen", "ich": "jogge", "reste": "", "inf": "joggen", "verbe": "joggen", "nom": None, "sorte": None},
         {"v": "court", "vpl": "courent", "reste": "", "neg": "", "inf": "courir"},
         {"v3": "goes jogging", "vpl": "go jogging", "inf": "go jogging", "ing": "jogging"},
         {"v3": "corre", "vpl": "correm", "inf": "correr"})

# La planche d'essai (6 images, 0,90 $), a montrer a Jacques avant le reste : un sport, un instrument, un vehicule, un
# geste simple, une personne agee assise, un mouvement -- ce qui peut rater est dedans.
ESSAI = ["futbol", "guitarra", "piano", "bici", "leer", "bailar"]

# ---------------------------------------------------------------------------------------------------------------
# LES FICHES : ce que chaque personne aime (True) ou n'aime pas (False), et a quelle frequence elle le fait.
# Regles (verifiees par verifier()) : l'activite de sa photo est aimee, et souvent ou tous les jours ; aimer -> immer,
# oft ou manchmal ; ne pas aimer -> selten ou nie ; deux activites aimees et deux pas aimees par personne.
FREQ = ["immer", "oft", "manchmal", "selten", "nie"]
JOURS = {"immer": 28, "oft": 16, "manchmal": 6, "selten": 1, "nie": 0}
FICHES = {
    "Felix":  [("futbol", True, "oft"), ("fotos", True, "manchmal"), ("bailar", False, "nie"), ("piano", False, "selten")],
    "Rosa":   [("tenis", True, "oft"), ("correr", True, "manchmal"), ("cantar", False, "selten"), ("pintar", False, "nie")],
    "Diego":  [("baloncesto", True, "oft"), ("guitarra", True, "manchmal"), ("cocinar", False, "selten"), ("leer", False, "nie")],
    "Ines":   [("guitarra", True, "immer"), ("cantar", True, "oft"), ("futbol", False, "nie"), ("deporte", False, "selten")],
    "Gisela": [("piano", True, "immer"), ("cocinar", True, "oft"), ("baloncesto", False, "nie"), ("bici", False, "selten")],
    "Sophie": [("violin", True, "oft"), ("bailar", True, "manchmal"), ("cocinar", False, "selten"), ("tenis", False, "nie")],
    "Tomas":  [("bici", True, "immer"), ("deporte", True, "oft"), ("piano", False, "nie"), ("pintar", False, "selten")],
    "Katrin": [("deporte", True, "oft"), ("leer", True, "manchmal"), ("cantar", False, "nie"), ("futbol", False, "selten")],
    "Javier": [("fotos", True, "immer"), ("cocinar", True, "manchmal"), ("bailar", False, "nie"), ("correr", False, "selten")],
    "Elena":  [("bailar", True, "immer"), ("cantar", True, "manchmal"), ("baloncesto", False, "nie"), ("fotos", False, "selten")],
    "Carmen": [("cantar", True, "oft"), ("pintar", True, "manchmal"), ("correr", False, "nie"), ("tenis", False, "selten")],
    "Heinz":  [("leer", True, "immer"), ("fotos", True, "manchmal"), ("baloncesto", False, "nie"), ("bailar", False, "selten")],
    "Pablo":  [("cocinar", True, "oft"), ("futbol", True, "manchmal"), ("violin", False, "nie"), ("bailar", False, "selten")],
    "Marta":  [("pintar", True, "immer"), ("leer", True, "oft"), ("bici", False, "nie"), ("deporte", False, "selten")],
    "Lena":   [("correr", True, "oft"), ("tenis", True, "manchmal"), ("pintar", False, "nie"), ("fotos", False, "selten")],
}

# LES ADVERBES de frequence, a la forme du corpus (adverbe.json, espanol/datos/adverbios.json) et dans les langues de
# traduction. « a menudo » manque au corpus espagnol : espanol/ajouts/loisirs.json le propose (accord de Jacques).
ADV = {"es": {"immer": "siempre", "oft": "a menudo", "manchmal": "a veces", "selten": "rara vez", "nie": "nunca"},
       "de": {f: f for f in FREQ},
       "fr": {"immer": "toujours", "oft": "souvent", "manchmal": "parfois", "selten": "rarement", "nie": "jamais"},
       "en": {"immer": "always", "oft": "often", "manchmal": "sometimes", "selten": "rarely", "nie": "never"},
       "pt": {"immer": "sempre", "oft": "com frequência", "manchmal": "às vezes", "selten": "raramente", "nie": "nunca"}}

# LES MOTS DU THEME qui ne sont pas des noms ou des verbes d'activite : la frequence, aimer, proposer
MOTS_AUTRES = {"es": [("siempre", "adverbe"), ("a menudo", "adverbe"), ("a veces", "adverbe"), ("rara vez", "adverbe"),
                      ("nunca", "adverbe"), ("gustar", "verbe"), ("querer", "verbe")],
               "de": [("immer", "adverbe"), ("oft", "adverbe"), ("manchmal", "adverbe"), ("selten", "adverbe"),
                      ("nie", "adverbe"), ("gern", "adverbe"), ("Lust", "die")]}

# ---------------------------------------------------------------------------------------------------------------
STYLE = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same "
         "skin, the same glasses or beard if any, the same body shape. Keep the same clothes unless other clothes are "
         "described. A photorealistic photograph of a real person, natural skin texture, no retouching. The person is ")
CADRE = (" The whole person is visible from head to feet with a small margin, in the centre of the picture, and the "
         "activity is obvious at first sight. Plain light grey studio background with even soft light, only the "
         "objects needed for the activity, no text, no logos, no other people.")


def prompt(id):
    return STYLE + A[id]["montre"] + CADRE


def source(id):
    qui = A[id]["qui"]
    if qui in DESCRIPCION:
        return PRINCIPAL + "/visuel/descripcion/img/" + qui + ".png"
    return FAMILLE + "/" + qui + ".png"


def verifier():
    fautes = []
    for p, f in FICHES.items():
        photo = [a for a, x in A.items() if x["qui"] == p]
        if len(photo) != 1: fautes.append("%s : %d photo(s)" % (p, len(photo)))
        acts = [a for a, _, _ in f]
        if len(set(acts)) != len(acts): fautes.append("%s : une activite deux fois" % p)
        if photo and (photo[0], True) not in [(a, g) for a, g, _ in f]: fautes.append("%s n'aime pas l'activite de sa photo" % p)
        for a, g, q in f:
            if a not in A: fautes.append("%s : activite inconnue %s" % (p, a))
            if g and q not in ("immer", "oft", "manchmal"): fautes.append("%s aime %s mais %s" % (p, a, q))
            if not g and q not in ("selten", "nie"): fautes.append("%s n'aime pas %s mais %s" % (p, a, q))
            if photo and a == photo[0] and q not in ("immer", "oft"): fautes.append("%s : sa photo, %s" % (p, q))
        if sum(1 for _, g, _ in f if g) != 2: fautes.append("%s : pas deux activites aimees" % p)
    if set(PERSONNES) != set(FICHES): fautes.append("personnes et fiches ne concordent pas")
    for a, x in A.items():
        for l in ("es", "de", "fr", "en", "pt"):
            for k in {"es": ("v", "vpl", "reste", "inf", "verbe"), "de": ("v", "vpl", "ich", "reste", "inf", "verbe"),
                      "fr": ("v", "vpl", "reste", "neg", "inf"), "en": ("v3", "vpl", "inf", "ing"), "pt": ("v3", "vpl", "inf")}[l]:
                if k not in x[l]: fautes.append("%s : %s.%s manque" % (a, l, k))
    if fautes:
        raise SystemExit("  donnee fautive :\n  " + "\n  ".join(fautes))


# ---------------------------------------------------------------------------------------------------------------
# LES GLOSES : la traduction de chaque mot du theme, prise au CORPUS RELU (pour « Tu as choisi : » et le mot montre
# sous la reponse) ; et les conjugaisons du present (les leurres de « la bonne forme »)
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]


def lire(*ch):
    return json.load(io.open(os.path.join(RACINE, *ch), encoding="utf-8"))


def gloses_et_formes():
    champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)
    gl = {"de": {}, "es": {}}
    formes = {"de": {}, "es": {}}
    def pose(app, cle, w):
        if cle not in gl[app]:
            gl[app][cle] = {l: champ(w, l) for l in LANGUES if champ(w, l) and not (app == "de" and l == "de")}
    noms = {"de": {tuple(x["de"]["nom"]) for x in A.values() if x["de"]["nom"]} | {("Lust", "die")},
            "es": {tuple(x["es"]["nom"]) for x in A.values() if x["es"]["nom"]}}
    verbes = {"de": {x["de"]["verbe"] for x in A.values()}, "es": {x["es"]["verbe"] for x in A.values()} | {"gustar", "querer"}}
    advs = {"de": set(FREQ) | {"gern"}, "es": set(ADV["es"].values())}
    for t in lire("themes.json")["themes"]:
        for w in t.get("mots", []):
            if (w.get("mot"), w.get("genre")) in noms["de"]: pose("de", w["mot"], w)
    for t in lire("espanol", "datos", "temas.json")["themes"]:
        for w in t.get("mots", []):
            if (w.get("mot"), w.get("genre")) in noms["es"]: pose("es", w["mot"], w)
    for app, fichier in (("de", ("verbe.json",)), ("es", ("espanol", "datos", "verbos.json"))):
        for l in lire(*fichier).values():
            for w in l:
                if w.get("infinitif") in verbes[app]:
                    pose(app, w["infinitif"], w)
                    formes[app].setdefault(w["infinitif"], w.get("praesens"))
    for app, fichier in (("de", ("adverbe.json",)), ("es", ("espanol", "datos", "adverbios.json"))):
        for l in lire(*fichier).values():
            if isinstance(l, list):
                for w in l:
                    if w.get("mot") in advs[app]: pose(app, w["mot"], w)
    # ce que le corpus n'a pas encore (espanol/ajouts/loisirs.json le propose) : la glose est ecrite ici, les cartes
    # attendent l'ajout au corpus
    MAIN = {"fútbol": {"fr": "le football", "en": "soccer", "pt": "o futebol", "ar": "كرة القدم", "de": "der Fußball"},
            "tenis": {"fr": "le tennis", "en": "tennis", "pt": "o tênis", "ar": "التنس", "de": "das Tennis"},
            "baloncesto": {"fr": "le basket", "en": "basketball", "pt": "o basquete", "ar": "كرة السلة", "de": "der Basketball"},
            "a menudo": {"fr": "souvent", "en": "often", "pt": "com frequência", "ar": "غالبًا", "de": "oft"}}
    hors = []
    for k, v in MAIN.items():
        if k not in gl["es"]:
            gl["es"][k] = v; hors.append(k)
    manque = [m for m in [n for n, _ in noms["de"]] + list(verbes["de"]) + list(advs["de"]) if m not in gl["de"]]
    manque += [m for m in [n for n, _ in noms["es"]] + list(verbes["es"]) + list(advs["es"]) if m not in gl["es"]]
    manque += [v for app in ("de", "es") for v in verbes[app] if not formes[app].get(v)]
    if manque:
        raise SystemExit("  absents du corpus : %s" % manque)
    return gl, formes, hors


def construire():
    verifier()
    gl, formes, hors = gloses_et_formes()
    d = {"_lisez_moi": "FABRIQUE par visuel/loisirs/loisirs.py -- ne pas modifier a la main.",
         "personnes": {k: {"nom": v[0], "sexe": v[1], "visage": ("loisirs/visage-" + k if v[2] == "descripcion" else "familia/" + k + "-visage") + ".webp"} for k, v in PERSONNES.items()},
         "activites": {k: {l: x[l] for l in ("es", "de", "fr", "en", "pt")} | {"qui": x["qui"]} for k, x in A.items()},
         "fiches": {p: [{"a": a, "gern": g, "freq": q} for a, g, q in f] for p, f in FICHES.items()},
         "freq": FREQ, "jours": JOURS, "adv": ADV, "autres": MOTS_AUTRES, "formes": formes, "gloses": gl,
         "horsCorpus": hors}
    return d


def ecrire_json():
    d = construire()
    os.makedirs(PROTO, exist_ok=True)
    io.open(os.path.join(PROTO, "loisirs.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  -> visuel/prototype/loisirs/loisirs.json (%d activites, %d personnes, %d faits ; hors corpus : %s)"
          % (len(A), len(FICHES), sum(len(f) for f in FICHES.values()), ", ".join(d["horsCorpus"]) or "rien"))


# ---------------------------------------------------------------------------------------------------------------
def provisoires():
    """Des images d'ESSAI, gratuites : la personne en pied (son webp de Decrire ou de la famille) et le nom de
    l'activite, sur le gris des autres. Pour essayer la page avant les vraies images. A NE PAS COMMITTER."""
    from PIL import Image, ImageDraw, ImageFont
    W, H = 900, 1200
    try:
        f = ImageFont.truetype("arialbd.ttf", 60)
    except OSError:
        f = ImageFont.load_default()
    for id, x in A.items():
        qui = x["qui"]
        dossier = "descripcion" if qui in DESCRIPCION else "familia"
        im = Image.new("RGB", (W, H), (214, 216, 220))
        p = Image.open(os.path.join(RACINE, "visuel", "prototype", dossier, qui + ".webp")).convert("RGBA")
        p.thumbnail((W, H - 170))
        im.paste(p, ((W - p.width) // 2, H - p.height), p)
        dr = ImageDraw.Draw(im)
        dr.rectangle((0, 0, W, 120), fill=(168, 106, 14))
        dr.text((W // 2, 60), "ESSAI · " + x["es"]["inf"], fill=(255, 255, 255), font=f, anchor="mm")
        im.save(os.path.join(PROTO, id + ".webp"), quality=70)
    print("  %d images provisoires dans visuel/prototype/loisirs/ (a ne pas committer)" % len(A))


def visages():
    """Les visages ronds de la fiche, gratuits : ceux de « Decrire une personne » sont cadres pour la loupe (le haut
    de l'image, la tete en bas) ; on recadre la tete sur la silhouette detouree (le haut du detourage, 15 % de la
    hauteur du corps), sur le gris des fiches -> visuel/prototype/loisirs/visage-<Nom>.webp. La famille garde les siens."""
    from PIL import Image
    for qui in [p for p in PERSONNES if p in DESCRIPCION]:
        src = PRINCIPAL + "/visuel/descripcion/img/" + qui + "-detoure.png"
        if not os.path.exists(src):
            src = os.path.join(RACINE, "visuel", "prototype", "descripcion", qui + ".webp")
        im = Image.open(src).convert("RGBA")
        a = im.split()[3].point(lambda v: 255 if v > 40 else 0)
        x0, y0, x1, y1 = a.getbbox()
        h = y1 - y0
        tete = a.crop((x0, y0, x1, y0 + int(h * .12))).getbbox()      # les colonnes de la tete
        cx = x0 + (tete[0] + tete[2]) / 2
        cote = int(h * .155)
        cy = y0 + int(h * .068)
        boite = (int(cx - cote / 2), int(cy - cote / 2), int(cx + cote / 2), int(cy + cote / 2))
        fond = Image.new("RGBA", (cote, cote), (214, 216, 220, 255))
        fond.alpha_composite(im.crop(boite))
        fond.convert("RGB").resize((240, 240), Image.LANCZOS).save(os.path.join(PROTO, "visage-" + qui + ".webp"), quality=82)
        print("   visage-%s.webp" % qui)


def payer(ids):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [i for i in (ids or list(A)) if not os.path.exists(os.path.join(IMG, i + ".png"))]
    inconnus = [i for i in a_faire if i not in A]
    if inconnus:
        raise SystemExit("  inconnu : " + ", ".join(inconnus))
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for id in a_faire:
        src = source(id)
        if not os.path.exists(src):
            print("  %s : source absente %s -- sautee" % (id, src)); continue
        corps = {"prompt": prompt(id), "image_urls": [O.deposer(src, "image/png", cle)[0]], "aspect_ratio": "3:4",
                 "resolution": "2K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", id, err)
            io.open(os.path.join(IMG, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), id, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(IMG, id + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), id, soum.get("request_id"), PRIX))
        io.open(os.path.join(IMG, id + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt(id), "source": src, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


def webp():
    """Les originaux -> visuel/prototype/loisirs/<activite>.webp, 900 px de large (3:4)."""
    from PIL import Image
    for id in A:
        src = os.path.join(IMG, id + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB")
        im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
        im.save(os.path.join(PROTO, id + ".webp"), quality=78, method=6)
        print("  ", id)


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        ids = [x for x in a if not x.startswith("--")] or list(A)
        for id in ids:
            print("\n  %s  (%s)\n  %s" % (id, os.path.basename(source(id)), prompt(id)))
        print("\n  %d images, %.2f $ ; la planche d'essai : %s (%.2f $)" % (len(ids), len(ids) * PRIX, ", ".join(ESSAI), len(ESSAI) * PRIX))
        return
    if "--provisoires" in a:
        provisoires()
    if "--payer" in a:
        payer([x for x in a if not x.startswith("--")])
    if "--webp" in a:
        webp()
    if "--visages" in a:
        visages()
    ecrire_json()


if __name__ == "__main__":
    main()
