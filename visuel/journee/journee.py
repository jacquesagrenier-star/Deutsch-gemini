# -*- coding: utf-8 -*-
"""« La journee », theme illustre (3 nov. 2026, vague 1 de Jacques : « la journee (verbes pronominaux, l'heure) »).
LA SEULE SOURCE du theme : les trois journees, leurs etapes, les verbes et leurs formes, les faits de frequence, les
prompts des images. La page (visuel/prototype/journee.html) lit journee.json, fabrique ses phrases avec les memes
regles, et ne contient aucune phrase ecrite a la main.

    python visuel/journee/journee.py --json        # journee.json et gloses.json seuls, gratuit
    python visuel/journee/journee.py --montrer     # les prompts des images, gratuit
    python visuel/journee/journee.py --provisoire  # des images provisoires (aplats + visages), gratuit, A NE PAS COMMITTER
    python visuel/journee/journee.py --web         # les webp a partir des originaux
    python visuel/journee/journee.py               # les images qui manquent : FACTURE, 0,15 $ l'image (accord de Jacques)
    python visuel/journee/journee.py anna-3        # celle-la seulement (facture)

TROIS JOURNEES, on suit des personnes et le temps qui passe (pas les scenes fruehstueck et schlafzimmer, qui sont des
lieux et leurs objets) : un lundi d'Anna (Berlin, son guichet de l'aeroport), le samedi de Mark (sa colocation, il
s'entraine chaque jour), un jour d'ecole chez Jan et Katrin (la famille d'Anna : Ben 7 ans, Mia 4 ans).
L'HEURE se dit EN LETTRES partout (« a las siete menos cuarto », « um halb sieben ») : aucune phrase dite n'a de
chiffre, rien a ajouter a audio/lectures. L'horloge de chaque image est DESSINEE par la page, a l'heure exacte : un
modele d'image met rarement les aiguilles ou on les veut, et les prompts interdisent toute horloge dans la photo.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/journee/img/.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "visuel", "prototype", "journee")
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "journee", "img")
EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png",
           "Jan": FAMILLE + "/Jan.png", "Katrin": FAMILLE + "/Katrin.png", "Ben": FAMILLE + "/Ben.png", "Mia": FAMILLE + "/Mia.png",
           # les lieux deja photographies : la cuisine vert sauge et le salon de la colocation de Mark (video/LIEUX.md)
           "cuisine-mark": RACINE + "/visuel/prototype/kueche.webp", "salon-mark": RACINE + "/visuel/prototype/wohnzimmer.webp"}
SEXE = {"Anna": "f", "Mark": "m", "Jan": "m", "Katrin": "f", "Ben": "m", "Mia": "f"}

# ---------------------------------------------------------------------------------------------------------------
# LES SUJETS : comment on les nomme dans chaque langue, et le pronom allemand qui les remplace (« Was macht Anna? »
# -> « Sie steht auf. »). n = 3 (troisieme personne) ou 5 (pluriel), l'indice des formes ci-dessous.
SUJETS = {
    "Anna":    {"es": "Anna", "de": "Anna", "fr": "Anna", "en": "Anna", "pt": "Anna", "pron": "sie", "n": 2, "qui": ["Anna"]},
    "Mark":    {"es": "Mark", "de": "Mark", "fr": "Mark", "en": "Mark", "pt": "Mark", "pron": "er", "n": 2, "qui": ["Mark"]},
    "Katrin":  {"es": "Katrin", "de": "Katrin", "fr": "Katrin", "en": "Katrin", "pt": "Katrin", "pron": "sie", "n": 2, "qui": ["Katrin"]},
    "Jan":     {"es": "Jan", "de": "Jan", "fr": "Jan", "en": "Jan", "pt": "Jan", "pron": "er", "n": 2, "qui": ["Jan"]},
    "BenMia":  {"es": "Ben y Mia", "de": "Ben und Mia", "fr": "Ben et Mia", "en": "Ben and Mia", "pt": "Ben e Mia", "pron": "sie", "n": 4, "qui": ["Ben", "Mia"]},
    "familia": {"es": "La familia", "de": "Die Familie", "fr": "La famille", "en": "The family", "pt": "A família", "pron": "sie", "n": 2, "qui": ["Jan", "Katrin", "Ben", "Mia"]},
}
# (« abends » se tait devant « zu Abend » : « Anna isst um halb acht zu Abend », pas « um halb acht abends zu Abend »)
# Les personnes des exercices de conjugaison, dans l'ordre des formes : yo, tu, il/elle, nosotros, ellos.
PERSONNES = {"es": ["Yo", "Tú", None, "Nosotros", None], "de": ["Ich", "Du", None, "Wir", None],
             "fr": ["Je", "Tu", None, "Nous", None], "en": ["I", "You", None, "We", None], "pt": ["Eu", "Você", None, "Nós", None]}

# ---------------------------------------------------------------------------------------------------------------
# LES VERBES. Chaque entree : le mot du CORPUS qu'elle fait avancer (es, de : l'infinitif tel que verbos.json et
# verbe.json le rangent ; carteDeScene() le cherche par l'infinitif), ses cinq formes, et la meme chose traduite.
#   es : pr (pronom reflechi par personne, ou absent), v (le verbe), c (ce qui suit) ; latam : ce qui change en
#        Amerique latine (la voix de Monica, variante=latam).
#   de : v (le verbe conjugue), r (pronom reflechi), o (un objet court, avant l'heure), c (ce qui suit l'heure), p (la
#        particule separable, a la fin). Phrase : S v r o HEURE c p -- « Anna zieht sich um Viertel nach sieben an. »
#   fr, en, pt : la phrase traduite a chaque personne, {S} le sujet, {H} l'heure ; {P} un possessif anglais.
#   groupe : les verbes qui se ressemblent a l'image (le lit, la table, la salle de bains...), jamais leurres l'un de
#   l'autre ; leurre: False pour les verbes a objet (« despierta a Mia »), qui ne vont pas a n'importe quel sujet.
REFL_ES = ["me", "te", "se", "nos", "se"]
REFL_DE = ["mich", "dich", "sich", "uns", "sich"]
VERBES = {
    "despertarse": {
        "es": {"mot": "despertarse", "pr": REFL_ES, "v": ["despierto", "despiertas", "despierta", "despertamos", "despiertan"], "piege": ["desperto", "despertas", "desperta", "despertamos", "despertan"]},
        "de": {"mot": "aufwachen", "v": ["wache", "wachst", "wacht", "wachen", "wachen"], "p": "auf"},
        "fr": ["je me réveille {H}", "tu te réveilles {H}", "{S} se réveille {H}", "nous nous réveillons {H}", "{S} se réveillent {H}"],
        "en": ["I wake up {H}", "you wake up {H}", "{S} wakes up {H}", "we wake up {H}", "{S} wake up {H}"],
        "pt": ["eu acordo {H}", "você acorda {H}", "{S} acorda {H}", "nós acordamos {H}", "{S} acordam {H}"],
        "groupe": "lit"},
    "levantarse": {
        "es": {"mot": "levantarse", "pr": REFL_ES, "v": ["levanto", "levantas", "levanta", "levantamos", "levantan"]},
        "de": {"mot": "aufstehen", "v": ["stehe", "stehst", "steht", "stehen", "stehen"], "p": "auf"},
        "fr": ["je me lève {H}", "tu te lèves {H}", "{S} se lève {H}", "nous nous levons {H}", "{S} se lèvent {H}"],
        "en": ["I get up {H}", "you get up {H}", "{S} gets up {H}", "we get up {H}", "{S} get up {H}"],
        "pt": ["eu me levanto {H}", "você se levanta {H}", "{S} se levanta {H}", "nós nos levantamos {H}", "{S} se levantam {H}"],
        "groupe": "lit"},
    "ducharse": {
        "es": {"mot": "ducharse", "pr": REFL_ES, "v": ["ducho", "duchas", "ducha", "duchamos", "duchan"]},
        "de": {"mot": "duschen", "v": ["dusche", "duschst", "duscht", "duschen", "duschen"]},
        "fr": ["je me douche {H}", "tu te douches {H}", "{S} se douche {H}", "nous nous douchons {H}", "{S} se douchent {H}"],
        "en": ["I take a shower {H}", "you take a shower {H}", "{S} takes a shower {H}", "we take a shower {H}", "{S} take a shower {H}"],
        "pt": ["eu tomo banho {H}", "você toma banho {H}", "{S} toma banho {H}", "nós tomamos banho {H}", "{S} tomam banho {H}"],
        "groupe": "bain"},
    "vestirse": {
        "es": {"mot": "vestirse", "pr": REFL_ES, "v": ["visto", "vistes", "viste", "vestimos", "visten"], "piege": ["vesto", "vestes", "veste", "vestimos", "vesten"]},
        "de": {"mot": "sich anziehen", "v": ["ziehe", "ziehst", "zieht", "ziehen", "ziehen"], "r": REFL_DE, "p": "an"},
        "fr": ["je m'habille {H}", "tu t'habilles {H}", "{S} s'habille {H}", "nous nous habillons {H}", "{S} s'habillent {H}"],
        "en": ["I get dressed {H}", "you get dressed {H}", "{S} gets dressed {H}", "we get dressed {H}", "{S} get dressed {H}"],
        "pt": ["eu me visto {H}", "você se veste {H}", "{S} se veste {H}", "nós nos vestimos {H}", "{S} se vestem {H}"],
        "groupe": "habit"},
    "desayunar": {
        "es": {"mot": "desayunar", "v": ["desayuno", "desayunas", "desayuna", "desayunamos", "desayunan"]},
        "de": {"mot": "frühstücken", "v": ["frühstücke", "frühstückst", "frühstückt", "frühstücken", "frühstücken"]},
        "fr": ["je prends mon petit-déjeuner {H}", "tu prends ton petit-déjeuner {H}", "{S} prend son petit-déjeuner {H}", "nous prenons notre petit-déjeuner {H}", "{S} prennent leur petit-déjeuner {H}"],
        "en": ["I have breakfast {H}", "you have breakfast {H}", "{S} has breakfast {H}", "we have breakfast {H}", "{S} have breakfast {H}"],
        "pt": ["eu tomo café da manhã {H}", "você toma café da manhã {H}", "{S} toma café da manhã {H}", "nós tomamos café da manhã {H}", "{S} tomam café da manhã {H}"],
        "groupe": "table"},
    "ir-trabajo": {
        "es": {"mot": "ir", "v": ["voy", "vas", "va", "vamos", "van"], "c": "al trabajo en metro"},
        "de": {"mot": "fahren", "v": ["fahre", "fährst", "fährt", "fahren", "fahren"], "c": "mit der U-Bahn zur Arbeit"},
        "fr": ["je vais au travail en métro {H}", "tu vas au travail en métro {H}", "{S} va au travail en métro {H}", "nous allons au travail en métro {H}", "{S} vont au travail en métro {H}"],
        "en": ["I take the subway to work {H}", "you take the subway to work {H}", "{S} takes the subway to work {H}", "we take the subway to work {H}", "{S} take the subway to work {H}"],
        "pt": ["eu vou para o trabalho de metrô {H}", "você vai para o trabalho de metrô {H}", "{S} vai para o trabalho de metrô {H}", "nós vamos para o trabalho de metrô {H}", "{S} vão para o trabalho de metrô {H}"],
        "groupe": "trajet"},
    "trabajar-aeropuerto": {
        "es": {"mot": "trabajar", "v": ["trabajo", "trabajas", "trabaja", "trabajamos", "trabajan"], "c": "en el aeropuerto"},
        "de": {"mot": "arbeiten", "v": ["arbeite", "arbeitest", "arbeitet", "arbeiten", "arbeiten"], "c": "am Flughafen"},
        "fr": ["je travaille à l'aéroport {H}", "tu travailles à l'aéroport {H}", "{S} travaille à l'aéroport {H}", "nous travaillons à l'aéroport {H}", "{S} travaillent à l'aéroport {H}"],
        "en": ["I work at the airport {H}", "you work at the airport {H}", "{S} works at the airport {H}", "we work at the airport {H}", "{S} work at the airport {H}"],
        "pt": ["eu trabalho no aeroporto {H}", "você trabalha no aeroporto {H}", "{S} trabalha no aeroporto {H}", "nós trabalhamos no aeroporto {H}", "{S} trabalham no aeroporto {H}"],
        "groupe": "travail"},
    "volver": {
        "es": {"mot": "volver", "v": ["vuelvo", "vuelves", "vuelve", "volvemos", "vuelven"], "c": "a casa", "piege": ["volvo", "volves", "volve", "volvemos", "volven"]},
        "de": {"mot": "kommen", "v": ["komme", "kommst", "kommt", "kommen", "kommen"], "c": "nach Hause"},
        "fr": ["je rentre à la maison {H}", "tu rentres à la maison {H}", "{S} rentre à la maison {H}", "nous rentrons à la maison {H}", "{S} rentrent à la maison {H}"],
        "en": ["I come home {H}", "you come home {H}", "{S} comes home {H}", "we come home {H}", "{S} come home {H}"],
        "pt": ["eu volto para casa {H}", "você volta para casa {H}", "{S} volta para casa {H}", "nós voltamos para casa {H}", "{S} voltam para casa {H}"],
        "groupe": "trajet"},
    "cenar": {
        "es": {"mot": "cenar", "v": ["ceno", "cenas", "cena", "cenamos", "cenan"]},
        "de": {"mot": "essen", "v": ["esse", "isst", "isst", "essen", "essen"], "c": "zu Abend"},
        "fr": ["je dîne {H}", "tu dînes {H}", "{S} dîne {H}", "nous dînons {H}", "{S} dînent {H}"],
        "en": ["I have dinner {H}", "you have dinner {H}", "{S} has dinner {H}", "we have dinner {H}", "{S} have dinner {H}"],
        "pt": ["eu janto {H}", "você janta {H}", "{S} janta {H}", "nós jantamos {H}", "{S} jantam {H}"],
        "groupe": "table"},
    "acostarse": {
        "es": {"mot": "acostarse", "pr": REFL_ES, "v": ["acuesto", "acuestas", "acuesta", "acostamos", "acuestan"], "piege": ["acosto", "acostas", "acosta", "acostamos", "acostan"]},
        # « ins Bett gehen » n'est pas au corpus ; « das Bett » (A1) l'est : c'est lui qui avance
        "de": {"mot": "Bett", "genre": "das", "v": ["gehe", "gehst", "geht", "gehen", "gehen"], "c": "ins Bett"},
        "fr": ["je me couche {H}", "tu te couches {H}", "{S} se couche {H}", "nous nous couchons {H}", "{S} se couchent {H}"],
        "en": ["I go to bed {H}", "you go to bed {H}", "{S} goes to bed {H}", "we go to bed {H}", "{S} go to bed {H}"],
        "pt": ["eu vou para a cama {H}", "você vai para a cama {H}", "{S} vai para a cama {H}", "nós vamos para a cama {H}", "{S} vão para a cama {H}"],
        "groupe": "lit"},
    "correr": {
        "es": {"mot": "correr", "v": ["salgo", "sales", "sale", "salimos", "salen"], "c": "a correr"},
        "de": {"mot": "joggen", "v": ["gehe", "gehst", "geht", "gehen", "gehen"], "c": "joggen"},
        "fr": ["je vais courir {H}", "tu vas courir {H}", "{S} va courir {H}", "nous allons courir {H}", "{S} vont courir {H}"],
        "en": ["I go running {H}", "you go running {H}", "{S} goes running {H}", "we go running {H}", "{S} go running {H}"],
        "pt": ["eu vou correr {H}", "você vai correr {H}", "{S} vai correr {H}", "nós vamos correr {H}", "{S} vão correr {H}"],
        "groupe": "sport"},
    "afeitarse": {
        "es": {"mot": "afeitarse", "pr": REFL_ES, "v": ["afeito", "afeitas", "afeita", "afeitamos", "afeitan"]},
        "de": {"mot": "rasieren", "v": ["rasiere", "rasierst", "rasiert", "rasieren", "rasieren"], "r": REFL_DE},
        "fr": ["je me rase {H}", "tu te rases {H}", "{S} se rase {H}", "nous nous rasons {H}", "{S} se rasent {H}"],
        "en": ["I shave {H}", "you shave {H}", "{S} shaves {H}", "we shave {H}", "{S} shave {H}"],
        "pt": ["eu faço a barba {H}", "você faz a barba {H}", "{S} faz a barba {H}", "nós fazemos a barba {H}", "{S} fazem a barba {H}"],
        "groupe": "bain", "masculin": True},
    "trabajar-portatil": {
        "es": {"mot": "trabajar", "v": ["trabajo", "trabajas", "trabaja", "trabajamos", "trabajan"], "c": "con el portátil", "latam": {"c": "en la computadora"}},
        "de": {"mot": "arbeiten", "v": ["arbeite", "arbeitest", "arbeitet", "arbeiten", "arbeiten"], "c": "am Laptop"},
        "fr": ["je travaille sur mon ordinateur portable {H}", "tu travailles sur ton ordinateur portable {H}", "{S} travaille sur son ordinateur portable {H}", "nous travaillons sur notre ordinateur portable {H}", "{S} travaillent sur leur ordinateur portable {H}"],
        "en": ["I work on my laptop {H}", "you work on your laptop {H}", "{S} works on {P} laptop {H}", "we work on our laptop {H}", "{S} work on their laptop {H}"],
        "pt": ["eu trabalho no notebook {H}", "você trabalha no notebook {H}", "{S} trabalha no notebook {H}", "nós trabalhamos no notebook {H}", "{S} trabalham no notebook {H}"],
        "groupe": "travail"},
    "cocinar": {
        "es": {"mot": "cocinar", "v": ["cocino", "cocinas", "cocina", "cocinamos", "cocinan"]},
        "de": {"mot": "kochen", "v": ["koche", "kochst", "kocht", "kochen", "kochen"]},
        "fr": ["je fais la cuisine {H}", "tu fais la cuisine {H}", "{S} fait la cuisine {H}", "nous faisons la cuisine {H}", "{S} font la cuisine {H}"],
        "en": ["I cook {H}", "you cook {H}", "{S} cooks {H}", "we cook {H}", "{S} cook {H}"],
        "pt": ["eu cozinho {H}", "você cozinha {H}", "{S} cozinha {H}", "nós cozinhamos {H}", "{S} cozinham {H}"],
        "groupe": "table"},
    "despertar": {
        "es": {"mot": "despertar", "v": ["despierto", "despiertas", "despierta", "despertamos", "despiertan"], "c": "a Mia"},
        "de": {"mot": "wecken", "v": ["wecke", "weckst", "weckt", "wecken", "wecken"], "o": "Mia"},
        "fr": ["je réveille Mia {H}", "tu réveilles Mia {H}", "{S} réveille Mia {H}", "nous réveillons Mia {H}", "{S} réveillent Mia {H}"],
        "en": ["I wake Mia up {H}", "you wake Mia up {H}", "{S} wakes Mia up {H}", "we wake Mia up {H}", "{S} wake Mia up {H}"],
        "pt": ["eu acordo a Mia {H}", "você acorda a Mia {H}", "{S} acorda a Mia {H}", "nós acordamos a Mia {H}", "{S} acordam a Mia {H}"],
        "groupe": "lit", "leurre": False},
    "lavarse-dientes": {
        "es": {"mot": "lavarse", "pr": REFL_ES, "v": ["lavo", "lavas", "lava", "lavamos", "lavan"], "c": "los dientes"},
        # « sich die Zaehne putzen » : le reflechi est au DATIF (ich putze MIR die Zaehne) -- le piege de l'exercice
        "de": {"mot": "putzen", "v": ["putze", "putzt", "putzt", "putzen", "putzen"], "r": ["mir", "dir", "sich", "uns", "sich"], "c": "die Zähne", "datif": True},
        "fr": ["je me brosse les dents {H}", "tu te brosses les dents {H}", "{S} se brosse les dents {H}", "nous nous brossons les dents {H}", "{S} se brossent les dents {H}"],
        "en": ["I brush my teeth {H}", "you brush your teeth {H}", "{S} brushes {P} teeth {H}", "we brush our teeth {H}", "{S} brush their teeth {H}"],
        "pt": ["eu escovo os dentes {H}", "você escova os dentes {H}", "{S} escova os dentes {H}", "nós escovamos os dentes {H}", "{S} escovam os dentes {H}"],
        "groupe": "bain"},
    "peinar": {
        "es": {"mot": "peinar", "v": ["peino", "peinas", "peina", "peinamos", "peinan"], "c": "a Mia"},
        # « Katrin kaemmt Mia die Haare » : kaemmen n'est pas au corpus, « das Haar » (A1) l'est
        "de": {"mot": "Haar", "genre": "das", "v": ["kämme", "kämmst", "kämmt", "kämmen", "kämmen"], "o": "Mia", "c": "die Haare"},
        "fr": ["je coiffe Mia {H}", "tu coiffes Mia {H}", "{S} coiffe Mia {H}", "nous coiffons Mia {H}", "{S} coiffent Mia {H}"],
        "en": ["I brush Mia's hair {H}", "you brush Mia's hair {H}", "{S} brushes Mia's hair {H}", "we brush Mia's hair {H}", "{S} brush Mia's hair {H}"],
        "pt": ["eu penteio a Mia {H}", "você penteia a Mia {H}", "{S} penteia a Mia {H}", "nós penteamos a Mia {H}", "{S} penteiam a Mia {H}"],
        "groupe": "habit", "leurre": False},
    "llevar-colegio": {
        "es": {"mot": "llevar", "v": ["llevo", "llevas", "lleva", "llevamos", "llevan"], "c": "a los niños al colegio", "latam": {"c": "a los niños a la escuela"}},
        "de": {"mot": "bringen", "v": ["bringe", "bringst", "bringt", "bringen", "bringen"], "o": "die Kinder", "c": "zur Schule"},
        "fr": ["j'emmène les enfants à l'école {H}", "tu emmènes les enfants à l'école {H}", "{S} emmène les enfants à l'école {H}", "nous emmenons les enfants à l'école {H}", "{S} emmènent les enfants à l'école {H}"],
        "en": ["I take the children to school {H}", "you take the children to school {H}", "{S} takes the children to school {H}", "we take the children to school {H}", "{S} take the children to school {H}"],
        "pt": ["eu levo as crianças para a escola {H}", "você leva as crianças para a escola {H}", "{S} leva as crianças para a escola {H}", "nós levamos as crianças para a escola {H}", "{S} levam as crianças para a escola {H}"],
        "groupe": "trajet", "leurre": False},
    "ponerse-pijama": {
        "es": {"mot": "ponerse", "pr": REFL_ES, "v": ["pongo", "pones", "pone", "ponemos", "ponen"], "c": "el pijama", "piege": ["pono", "pones", "pone", "ponemos", "ponen"]},
        "de": {"mot": "anziehen", "v": ["ziehe", "ziehst", "zieht", "ziehen", "ziehen"], "c": "den Schlafanzug", "p": "an"},
        "fr": ["je mets mon pyjama {H}", "tu mets ton pyjama {H}", "{S} met son pyjama {H}", "nous mettons notre pyjama {H}", "{S} mettent leur pyjama {H}"],
        "en": ["I put on my pajamas {H}", "you put on your pajamas {H}", "{S} puts on {P} pajamas {H}", "we put on our pajamas {H}", "{S} put on their pajamas {H}"],
        "pt": ["eu visto o pijama {H}", "você veste o pijama {H}", "{S} veste o pijama {H}", "nós vestimos o pijama {H}", "{S} vestem o pijama {H}"],
        "groupe": "habit"},
}

# ---------------------------------------------------------------------------------------------------------------
# LES TROIS JOURNEES. Une etape : le verbe, le sujet, l'heure (h, m), l'image (et son prompt plus bas).
JOURS = {
    "anna": {"titre": {"es": "Un lunes de Anna", "de": "Annas Montag"}, "etapes": [
        ("despertarse", "Anna", 6, 30), ("levantarse", "Anna", 6, 45), ("ducharse", "Anna", 7, 0), ("vestirse", "Anna", 7, 15),
        ("desayunar", "Anna", 7, 30), ("ir-trabajo", "Anna", 8, 15), ("trabajar-aeropuerto", "Anna", 9, 0), ("volver", "Anna", 18, 0),
        ("cenar", "Anna", 19, 30), ("acostarse", "Anna", 22, 30)]},
    "mark": {"titre": {"es": "El sábado de Mark", "de": "Marks Samstag"}, "etapes": [
        ("despertarse", "Mark", 8, 30), ("correr", "Mark", 9, 0), ("ducharse", "Mark", 10, 0), ("afeitarse", "Mark", 10, 15),
        ("desayunar", "Mark", 10, 30), ("trabajar-portatil", "Mark", 11, 0), ("cocinar", "Mark", 20, 0), ("acostarse", "Mark", 23, 30)]},
    "familia": {"titre": {"es": "Un día en familia", "de": "Ein Tag in der Familie"}, "etapes": [
        ("despertar", "Katrin", 6, 45), ("desayunar", "familia", 7, 0), ("lavarse-dientes", "BenMia", 7, 15), ("peinar", "Katrin", 7, 30),
        ("llevar-colegio", "Jan", 7, 45), ("cenar", "familia", 18, 30), ("ponerse-pijama", "BenMia", 19, 30), ("acostarse", "BenMia", 20, 0)]},
}

# ---------------------------------------------------------------------------------------------------------------
# LA FREQUENCE : des faits sur les habitudes, montres par une semaine a cocher (lundi -> dimanche). Aucun ne
# contredit une image : Mark s'entraine chaque jour (sa fiche), sa barbe de trois jours dit « a veces » ; Mia a quatre
# ans et Katrin la coiffe ; Anna prend le metro. f : siempre / a veces / nunca. {A} : l'adverbe, a sa place.
# jours : la semaine d'un « a veces », fixe (Jan ne mene a l'ecole qu'en semaine, Anna dine en famille le week-end).
FREQUENCES = [
    {"qui": "Anna", "f": "siempre", "es": "Anna {A} desayuna en casa.", "de": "Anna frühstückt {A} zu Hause.",
     "fr": "Anna prend toujours son petit-déjeuner à la maison.", "en": "Anna always has breakfast at home.", "pt": "Anna sempre toma café da manhã em casa.", "dei": "Anna frühstückt immer zu Hause."},
    {"qui": "Anna", "f": "nunca", "es": "Anna {A} va al trabajo en coche.", "de": "Anna fährt {A} mit dem Auto zur Arbeit.",
     "fr": "Anna ne va jamais au travail en voiture.", "en": "Anna never drives to work.", "pt": "Anna nunca vai para o trabalho de carro.", "dei": "Anna fährt nie mit dem Auto zur Arbeit."},
    {"qui": "Anna", "f": "a veces", "jours": [0, 0, 0, 0, 0, 1, 1], "es": "Anna {A} cena con su familia.", "de": "Anna isst {A} mit ihrer Familie zu Abend.",
     "fr": "Anna dîne parfois avec sa famille.", "en": "Anna sometimes has dinner with her family.", "pt": "Anna às vezes janta com a família.", "dei": "Anna isst manchmal mit ihrer Familie zu Abend."},
    {"qui": "Mark", "f": "siempre", "es": "Mark {A} sale a correr.", "de": "Mark geht {A} joggen.",
     "fr": "Mark va toujours courir.", "en": "Mark always goes running.", "pt": "Mark sempre vai correr.", "dei": "Mark geht immer joggen."},
    {"qui": "Mark", "f": "a veces", "jours": [1, 0, 0, 1, 0, 1, 0], "es": "Mark {A} se afeita.", "de": "Mark rasiert sich {A}.",
     "fr": "Mark se rase parfois.", "en": "Mark sometimes shaves.", "pt": "Mark às vezes faz a barba.", "dei": "Mark rasiert sich manchmal."},
    {"qui": "Mark", "f": "a veces", "jours": [0, 1, 0, 0, 1, 1, 0], "es": "Mark {A} cocina.", "de": "Mark kocht {A}.",
     "fr": "Mark fait parfois la cuisine.", "en": "Mark sometimes cooks.", "pt": "Mark às vezes cozinha.", "dei": "Mark kocht manchmal."},
    {"qui": "Mark", "f": "nunca", "es": "Mark {A} se acuesta temprano.", "de": "Mark geht {A} früh ins Bett.",
     "fr": "Mark ne se couche jamais tôt.", "en": "Mark never goes to bed early.", "pt": "Mark nunca vai para a cama cedo.", "dei": "Mark geht nie früh ins Bett."},
    {"qui": "BenMia", "f": "siempre", "es": "Ben y Mia {A} se lavan los dientes.", "de": "Ben und Mia putzen sich {A} die Zähne.",
     "fr": "Ben et Mia se brossent toujours les dents.", "en": "Ben and Mia always brush their teeth.", "pt": "Ben e Mia sempre escovam os dentes.", "dei": "Ben und Mia putzen sich immer die Zähne."},
    {"qui": "Mia", "f": "nunca", "es": "Mia {A} se peina sola.", "de": "Mia kämmt sich {A} allein.",
     "fr": "Mia ne se coiffe jamais seule.", "en": "Mia never brushes her hair by herself.", "pt": "Mia nunca se penteia sozinha.", "dei": "Mia kämmt sich nie allein."},
    {"qui": "Jan", "f": "a veces", "jours": [1, 0, 1, 0, 0, 0, 0], "es": "Jan {A} lleva a los niños al colegio.", "es_latam": "Jan {A} lleva a los niños a la escuela.", "de": "Jan bringt die Kinder {A} zur Schule.",
     "fr": "Jan emmène parfois les enfants à l'école.", "en": "Jan sometimes takes the children to school.", "pt": "Jan às vezes leva as crianças para a escola.", "dei": "Jan bringt die Kinder manchmal zur Schule."},
    {"qui": "Katrin", "f": "siempre", "es": "Katrin {A} despierta a Mia.", "de": "Katrin weckt Mia {A}.",
     "fr": "Katrin réveille toujours Mia.", "en": "Katrin always wakes Mia up.", "pt": "Katrin sempre acorda a Mia.", "dei": "Katrin weckt Mia immer."},
    {"qui": "BenMia", "f": "nunca", "es": "Ben y Mia {A} se acuestan tarde.", "de": "Ben und Mia gehen {A} spät ins Bett.",
     "fr": "Ben et Mia ne se couchent jamais tard.", "en": "Ben and Mia never go to bed late.", "pt": "Ben e Mia nunca vão para a cama tarde.", "dei": "Ben und Mia gehen nie spät ins Bett."},
]
ADVERBES = {"siempre": {"es": "siempre", "de": "immer"}, "a veces": {"es": "a veces", "de": "manchmal"}, "nunca": {"es": "nunca", "de": "nie"}}

# ---------------------------------------------------------------------------------------------------------------
# L'HEURE EN LETTRES : la meme regle que la page (journee.html, heureEs / heureDe). Le matin sans precision ; l'apres-
# midi et le soir avec « de la tarde / de la noche » et « abends », qui levent l'ambiguite d'un cadran a douze heures.
NOMBRES_ES = ["doce", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce"]
NOMBRES_DE = ["zwölf", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf"]


def heure_es(h, m):
    hh = h + 1 if m > 30 else h
    n = hh % 12
    base = ("a la una" if n == 1 else "a las " + NOMBRES_ES[n])
    base += {0: "", 15: " y cuarto", 30: " y media", 45: " menos cuarto"}[m]
    if 12 <= h < 20:
        base += " de la tarde"
    elif h >= 20:
        base += " de la noche"
    return base


def heure_de(h, m, soir=True):
    n = h % 12 or 12
    s = n + 1 if n < 12 else 1
    nom = lambda k: "ein" if k == 1 else NOMBRES_DE[k]
    base = {0: "um %s Uhr" % nom(n), 15: "um Viertel nach %s" % NOMBRES_DE[n], 30: "um halb %s" % NOMBRES_DE[s],
            45: "um Viertel vor %s" % NOMBRES_DE[s]}[m]
    return base + (" abends" if h >= 18 and soir else "")


def heure_trad(h, m, langue):
    if langue == "fr":
        return "à %d h%s" % (h, " %02d" % m if m else "")
    if langue == "en":
        return "at %d:%02d %s" % (h % 12 or 12, m, "a.m." if h < 12 else "p.m.")
    if langue == "pt":
        return "às %dh%s" % (h, "%02d" % m if m else "")
    if langue == "de":
        return heure_de(h, m)


def phrase_es(verbe, sujet, h, m, latam=False):
    v = VERBES[verbe]["es"]
    n = SUJETS[sujet]["n"]
    c = ((v.get("latam") or {}).get("c") if latam else None) or v.get("c")
    mots = [SUJETS[sujet]["es"], (v["pr"][n] + " " if v.get("pr") else "") + v["v"][n]] + ([c] if c else []) + [heure_es(h, m)]
    return " ".join(mots) + "."


def phrase_de(verbe, sujet, h, m):
    v = VERBES[verbe]["de"]
    n = SUJETS[sujet]["n"]
    mots = [SUJETS[sujet]["de"], v["v"][n]] + ([v["r"][n]] if v.get("r") else []) + ([v["o"]] if v.get("o") else []) \
        + [heure_de(h, m, "Abend" not in v.get("c", ""))] + ([v["c"]] if v.get("c") else []) + ([v["p"]] if v.get("p") else [])
    return " ".join(mots) + "."


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES : une par etape, en 4:3, par RETOUCHE des images existantes (le meme visage, jamais une description
# seule). Les lieux qui reviennent (la chambre d'Anna, sa cuisine ; la salle de bains de Mark) recoivent la premiere
# image du lieu en reference, apres son tournage (video/LIEUX.md : le modele remeuble la piece a chaque plan).
SANS_HEURE = ("Absolutely no clock, watch, alarm-clock display, phone screen, oven display or any other object showing "
              "the time anywhere in the picture. ")
STYLE = (" A photorealistic photograph of a real everyday moment in Berlin, natural colours, the light of that time of "
         "day, no text, no logos, no captions. The people are clearly visible, their faces and gestures easy to read. ")
MEME = ("The same people as in the reference pictures: exactly the same faces, ages, hair, skin, glasses or beard if "
        "any, and the same bodies. ")
NOVEMBRE = "It is November: before eight in the morning and after five in the afternoon it is dark outside the windows. "
IMAGES = {
    # Anna, un lundi : son appartement (la chambre de anna-1 sert de lieu a anna-2, anna-4 et anna-10)
    "anna-1": (["Anna"], None, "Early morning, still dark outside: Anna lies in bed under a light-grey duvet in a small, cosy bedroom with white walls and a wooden bedside table with a small lamp switched on; she has just opened her eyes and stretches one arm, still sleepy, her phone lying face down on the bedside table."),
    "anna-2": (["Anna"], "anna-1", "The same bedroom as in the last reference picture, same bed, same bedside lamp: Anna, in pyjamas, sits up on the edge of the bed and puts her feet on the floor, about to stand up, stretching and yawning."),
    "anna-3": (["Anna"], None, "In a small bathroom with white tiles, Anna is in the shower behind a clear glass door, seen from the shoulders up only, eyes closed, warm water running over her wet hair; steam on the glass. Nothing below the shoulders is visible."),
    "anna-4": (["Anna"], "anna-1", "The same bedroom as in the last reference picture: Anna, her hair done, stands in front of an open wooden wardrobe and puts on a dark-blue cardigan over a white blouse, getting dressed for work."),
    "anna-5": (["Anna"], None, "Early morning, dark outside the window: Anna, dressed for work, has breakfast alone at a small round kitchen table in a bright, simple kitchen with light-blue cupboards: a cup of coffee and a bread roll with jam; she drinks her coffee."),
    "anna-6": (["Anna"], None, "On a Berlin U-Bahn platform in the morning, among a few commuters, Anna in a warm coat with a scarf and a handbag steps into a yellow U-Bahn train whose doors are open."),
    "anna-7": (["Anna"], None, "At the information counter of Berlin airport, Anna in her work clothes (a plain uniform-style shirt and a name badge on a lanyard) helps a traveller with a suitcase, smiling, pointing at a screen on the counter (the screen faces away from the camera)."),
    "anna-8": (["Anna"], None, "In the evening, dark outside, Anna in her warm coat with a shopping bag unlocks the front door of an old Berlin apartment building with a key, coming home after work; a warm light above the door."),
    "anna-9": (["Anna"], "anna-5", "The same kitchen as in the last reference picture, same light-blue cupboards and round table, in the evening with the warm ceiling light on and the window dark: Anna, in a comfortable sweater, eats a plate of pasta and a salad alone at the table."),
    "anna-10": (["Anna"], "anna-1", "The same bedroom as in the last reference picture, at night, only the bedside lamp on: Anna in pyjamas gets into bed, pulling up the light-grey duvet, a book on the bedside table, about to switch off the lamp."),
    # Mark, un samedi : sa colocation (la cuisine vert sauge de la scene kueche, le salon de wohnzimmer)
    "mark-1": (["Mark"], None, "On a Saturday morning, daylight through the curtains, Mark wakes up in a simple bedroom of a shared flat (white walls, a wooden bed, clothes on a chair); he opens his eyes, rubs his face, still sleepy, the duvet pulled up to his chest."),
    "mark-2": (["Mark"], None, "On a bright Saturday morning in a Berlin park with autumn trees, Mark goes running: in running clothes and sports shoes, jogging along a path, energetic and smiling."),
    "mark-3": (["Mark"], None, "In a small bathroom with grey tiles, Mark is in the shower behind a clear glass door, seen from the shoulders up only, eyes closed, water running over his wet hair; steam on the glass. Nothing below the shoulders is visible."),
    "mark-4": (["Mark"], "mark-3", "The same bathroom as in the last reference picture: Mark, a towel around his neck, shaves in front of the mirror above the washbasin, white shaving foam on his cheeks and a razor in his hand; we see him and his reflection."),
    "mark-5": (["Mark", "cuisine-mark"], None, "The kitchen of the last reference picture (sage-green wall, white fridge, wooden table), without the party and without the other people, late on a sunny Saturday morning: Mark, in a T-shirt, has breakfast alone at the wooden table, a big cup of coffee, muesli and orange juice."),
    "mark-6": (["Mark", "salon-mark"], None, "The living room of the last reference picture, tidy, with nobody else, on a Saturday late morning: Mark sits at a small desk by the big window and works on his laptop (the screen faces away from the camera), concentrated, a cup next to him."),
    "mark-7": (["Mark", "cuisine-mark"], None, "The kitchen of the last reference picture (sage-green wall, white fridge, wooden table), in the evening, dark outside, the ceiling light on, nobody else: Mark cooks at the stove, stirring a big pan of vegetables with a wooden spoon, happy."),
    "mark-8": (["Mark"], "mark-1", "The same bedroom as in the last reference picture, late at night, only a small lamp on: Mark, tired, in a T-shirt, gets into bed and pulls up the duvet, yawning."),
    # La famille de Jan et Katrin, un jour d'ecole
    "familia-1": (["Katrin", "Mia"], None, "Early morning, dark outside, in a child's bedroom with a small bed and soft toys: Katrin sits on the edge of the bed and gently wakes up her little daughter Mia (4), stroking her hair; Mia opens her eyes sleepily."),
    "familia-2": (["Jan", "Katrin", "Ben", "Mia"], None, "Early morning, dark outside, the warm kitchen light on: the whole family has breakfast together at a wooden kitchen table: Jan and Katrin drink coffee, Ben (7) eats cereal, Mia (4) drinks a glass of milk; everybody is already dressed."),
    "familia-3": (["Ben", "Mia"], None, "In a family bathroom, Ben (7) and his little sister Mia (4) stand side by side in front of the washbasin and brush their teeth with toothbrushes, white toothpaste foam, looking at each other in the mirror and laughing. Both are fully dressed."),
    "familia-4": (["Katrin", "Mia"], None, "In a bright hallway at home, Katrin kneels behind her little daughter Mia (4) and brushes her hair with a hairbrush, making a ponytail; Mia, dressed, with her small backpack, waits patiently."),
    "familia-5": (["Jan", "Ben", "Mia"], None, "On a Berlin pavement in the morning, in front of a primary school, Jan holds the hands of Ben (7, with a school bag) and Mia (4, with a small backpack), walking them to school; other children arrive."),
    "familia-6": (["Jan", "Katrin", "Ben", "Mia"], "familia-2", "The same kitchen as in the last reference picture, in the evening, dark outside, the warm ceiling light on: the whole family has dinner together at the wooden table, a big bowl of soup and bread, everybody talking and laughing."),
    "familia-7": (["Ben", "Mia"], "familia-1", "In the same child's bedroom as in the last reference picture, in the evening, a small lamp on: Ben (7) and Mia (4) put on their pyjamas; Mia pulls the pyjama top over her head, Ben buttons his pyjama shirt. Their clothes of the day lie on a chair."),
    "familia-8": (["Jan", "Ben", "Mia"], "familia-1", "In the same child's bedroom as in the last reference picture, at night, only a small night light on: Ben (7) and Mia (4), in pyjamas, lie in their beds under their duvets, about to sleep, while Jan sits on the edge of a bed and switches off the lamp."),
}


def etapes():
    """[(jour, rang, verbe, sujet, h, m)], dans l'ordre des journees."""
    return [(j, i, v, s, h, m) for j, d in JOURS.items() for i, (v, s, h, m) in enumerate(d["etapes"])]


def verifier():
    """Les formes sont celles du CORPUS (verbos.json, verbe.json) quand le corpus a le mot ; chaque etape a son image."""
    def walk(o, acc):
        if isinstance(o, dict):
            if "infinitif" in o: acc[o["infinitif"]] = o
            for v in o.values(): walk(v, acc)
        elif isinstance(o, list):
            for v in o: walk(v, acc)
    es, de = {}, {}
    walk(json.load(io.open(os.path.join(RACINE, "espanol/datos/verbos.json"), encoding="utf-8")), es)
    walk(json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8")), de)
    cles = ["ich", "du", "er_sie_es", "wir", "sie_Sie"]
    fautes, absents = [], []
    # « sale a correr » / « geht joggen » : le verbe conjugue n'est pas le mot enseigne (salir, gehen)
    for k, v in VERBES.items():
        e, d = v["es"], v["de"]
        if k == "correr":
            continue
        if e["mot"] in es:
            corp = [es[e["mot"]]["praesens"][c] for c in cles]
            mien = [((e["pr"][i] + " ") if e.get("pr") else "") + e["v"][i] for i in range(5)]
            if corp != mien: fautes.append("es %s : %s / corpus %s" % (k, mien, corp))
        elif e["mot"] not in es: absents.append("es " + e["mot"])
        if d.get("genre"):
            pass                                  # un nom du corpus (das Bett, das Haar) : verifie par ecrire_gloses
        elif d["mot"] in de:
            corp = [de[d["mot"]]["praesens"][c] for c in cles]
            # le corpus ecrit « stehe auf », « ziehe mich an » : on compare le verbe, le reflechi et la particule
            mien = [" ".join([d["v"][i]] + ([d["r"][i]] if d.get("r") and d["mot"].startswith("sich ") else []) + ([d["p"]] if d.get("p") else [])) for i in range(5)]
            if corp != mien: fautes.append("de %s : %s / corpus %s" % (k, mien, corp))
        else: absents.append("de " + d["mot"])
    manque = [("%s-%d" % (j, i + 1)) for j, i, *_ in etapes() if ("%s-%d" % (j, i + 1)) not in IMAGES]
    return fautes, sorted(set(absents)), manque


def ecrire_json():
    dec = {"es": {}, "latam": {}, "de": {}}
    for j, i, v, s, h, m in etapes():
        cle = "%s-%d" % (j, i + 1)
        for langue, t in (("es", phrase_es(v, s, h, m)), ("latam", phrase_es(v, s, h, m, True)), ("de", phrase_de(v, s, h, m))):
            dec[langue][cle] = {"texte": t, "son": identifiant(t)}
    d = {"_lisez_moi": "FICHIER DERIVE de visuel/journee/journee.py (python visuel/journee/journee.py --json) : ne pas corriger ici.",
         "sujets": SUJETS, "personnes": PERSONNES, "verbes": VERBES, "jours": JOURS, "frequences": FREQUENCES, "adverbes": ADVERBES,
         "sexe": SEXE, "decouverte": dec}
    os.makedirs(SORTIE, exist_ok=True)
    io.open(os.path.join(SORTIE, "journee.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def ecrire_gloses():
    """La traduction des mots du theme, tiree du CORPUS (relu), pour les langues d'interface ou la page ne traduit pas
    la phrase entiere (es : ar ; de : tr, uk, fa, ar, pl, ru). Comme familia/gloses.json. Fichier DERIVE."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    def walk(o, acc, cle):
        if isinstance(o, dict):
            if cle in o: acc.setdefault(o[cle], o)
            for v in o.values(): walk(v, acc, cle)
        elif isinstance(o, list):
            for v in o: walk(v, acc, cle)
    LDE = {"tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa", "ar": "traduction_ar", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"ar": "traduction_ar"}
    out = {"es": {}, "de": {}}
    for langue, fichiers, champs in (("es", ["espanol/datos/verbos.json", "espanol/datos/adverbios.json"], LES),
                                     ("de", ["verbe.json", "adverbe.json"], LDE)):
        corpus = {}
        for f in fichiers:
            walk(lire(f), corpus, "infinitif" if os.path.basename(f).startswith("verb") else "mot")   # « adverbios » contient « verb »
        voulus = [v[langue]["mot"] for v in VERBES.values() if not v[langue].get("genre")] + [a[langue] for a in ADVERBES.values()] \
            + {"es": ["después", "antes", "luego", "primero"], "de": ["zuerst", "dann", "danach"]}[langue]
        for w in voulus:
            if w in corpus:
                out[langue][w] = {l: corpus[w][c] for l, c in champs.items() if corpus[w].get(c)}
        # les noms des moments de la journee (la manana, der Abend) : themes.json / temas.json
        noms = {"es": [("la", "mañana"), ("la", "tarde"), ("la", "noche")], "de": [("der", "Morgen"), ("der", "Abend"), ("das", "Bett"), ("das", "Haar")]}[langue]
        for t in lire("espanol/datos/temas.json" if langue == "es" else "themes.json")["themes"]:
            for mo in t["mots"]:
                if (mo.get("genre"), mo["mot"]) in noms:
                    out[langue].setdefault(mo["genre"] + " " + mo["mot"], {l: mo[c] for l, c in champs.items() if mo.get(c)})
    io.open(os.path.join(SORTIE, "gloses.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def textes_a_dire(langue):
    """Pour les inventaires des voix : les phrases de la decouverte (es, latam, de)."""
    d = json.load(io.open(os.path.join(SORTIE, "journee.json"), encoding="utf-8"))
    return [v["texte"] for v in d["decouverte"][langue].values()]


def provisoire():
    """Des images PROVISOIRES pour construire la page sans depense : un aplat a la couleur du moment, les visages des
    personnes (descripcion/, familia/) et le geste ecrit. Jamais committees : les vraies les remplacent."""
    from PIL import Image, ImageDraw, ImageFont
    visages = {p: os.path.join(RACINE, "visuel", "prototype", "familia" if p != "Mark" else "descripcion", p + "-visage.webp") for p in SEXE}
    try:
        police = ImageFont.truetype("arial.ttf", 46)
    except OSError:
        police = ImageFont.load_default()
    for j, i, v, s, h, m in etapes():
        cle = "%s-%d" % (j, i + 1)
        fond = (40, 52, 80) if (h < 8 or h >= 18) else (205, 222, 236)
        im = Image.new("RGB", (960, 720), fond)
        qui = IMAGES[cle][0]
        gens = [p for p in qui if p in SEXE]
        for k, p in enumerate(gens):
            try:
                vis = Image.open(visages[p]).convert("RGB").resize((240, 240))
                im.paste(vis, (60 + k * 260, 120))
            except OSError:
                pass
        dr = ImageDraw.Draw(im)
        dr.text((60, 440), VERBES[v]["es"]["mot"] + " / " + VERBES[v]["de"]["mot"], fill=(232, 162, 58), font=police)
        dr.text((60, 510), "PROVISOIRE", fill=(200, 71, 58), font=police)
        im.save(os.path.join(SORTIE, cle + ".webp"), "WEBP", quality=70)
    print("  %d images provisoires dans %s (a ne pas committer)" % (len(etapes()), os.path.relpath(SORTIE, RACINE)))


def web():
    """Les webp de la page (960 x 720, 4:3) a partir des originaux, et les vignettes de la decouverte (320 x 240)."""
    from PIL import Image
    manque = []
    for cle in IMAGES:
        src = os.path.join(DOSSIER, cle + ".png")
        if not os.path.exists(src):
            manque.append(cle)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, cle + ".webp"), "WEBP", quality=78, method=6)
    print("  webp faits dans %s" % os.path.relpath(SORTIE, RACINE) + ("" if not manque else " ; MANQUENT : " + ", ".join(manque)))


def prompt(cle):
    qui, lieu, scene = IMAGES[cle]
    gens = [p for p in qui if p in SEXE]
    noms = ", ".join("%s (reference picture %d)" % (p, k + 1) for k, p in enumerate(gens))
    return MEME + "The people: " + noms + ". " + NOVEMBRE + SANS_HEURE + STYLE + "Scene: " + scene


def generer(noms, montrer):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(DOSSIER, exist_ok=True)
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    depots = {}
    def deposer(chemin):
        if chemin not in depots:
            typ = "image/webp" if chemin.endswith(".webp") else "image/png"
            depots[chemin] = O.deposer(chemin, typ, cle)[0]
        return depots[chemin]
    for nom in a_faire:
        qui, lieu, _ = IMAGES[nom]
        refs = [SOURCES[p] for p in qui] + ([os.path.join(DOSSIER, lieu + ".png")] if lieu else [])
        texte = prompt(nom) + (" The place is exactly the one of the last reference picture." if lieu else "")
        print("\n  %s  (%s)\n  %s" % (nom, ", ".join(os.path.basename(r) for r in refs), texte))
        if montrer:
            continue
        if lieu and not os.path.exists(refs[-1]):
            print("  ATTENTE : le lieu %s n'est pas encore fait" % lieu)
            continue
        corps = {"prompt": texte, "image_urls": [deposer(r) for r in refs], "aspect_ratio": "4:3", "resolution": "2K",
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
            "prompt": texte, "sources": refs, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


def main():
    fautes, absents, manque = verifier()
    if fautes or manque:
        sys.exit("  donnee fautive :\n  " + "\n  ".join(fautes + ["image manquante : " + m for m in manque]))
    if absents:
        print("  absents du corpus (hors jeu dans l'app tant qu'ils n'y sont pas) : " + ", ".join(absents))
    ecrire_json()
    ecrire_gloses()
    if "--json" in sys.argv:
        return
    if "--provisoire" in sys.argv:
        return provisoire()
    if "--web" in sys.argv:
        return web()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(IMAGES)
    inconnus = [n for n in noms if n not in IMAGES]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    generer(noms, "--montrer" in sys.argv)


if __name__ == "__main__":
    main()
