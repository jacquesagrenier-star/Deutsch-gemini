# -*- coding: utf-8 -*-
"""L'americain et le britannique au-dela de l'A1, et les pluriels des niveaux.

Complete variante.py (l'A1) sans le modifier : niveaux.py applique ces tables
aux mots et aux phrases de l'A2-C1 seulement. SOURCE : on corrige ici.
"""
import io, json, os, re

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))

# (americain, britannique) : l'orthographe, formes flechies comprises. Une
# liste, pas une regle : « -ise » est aussi americain (advise, exercise, surprise).
ORTHOGRAPHE = [
    ("organization", "organisation"), ("organizations", "organisations"),
    ("civilization", "civilisation"), ("civilizations", "civilisations"),
    ("globalization", "globalisation"), ("specialization", "specialisation"),
    ("authorization", "authorisation"), ("realization", "realisation"),
    ("modernization", "modernisation"), ("privatization", "privatisation"),
    ("criticize", "criticise"), ("criticized", "criticised"), ("criticizes", "criticises"), ("criticizing", "criticising"),
    ("emphasize", "emphasise"), ("emphasized", "emphasised"), ("emphasizes", "emphasises"),
    ("summarize", "summarise"), ("summarized", "summarised"), ("summarizes", "summarises"),
    ("specialize", "specialise"), ("specialized", "specialised"), ("specializes", "specialises"),
    ("apologizing", "apologising"), ("apologizes", "apologises"),
    ("recognizes", "recognises"), ("recognizing", "recognising"), ("realizing", "realising"),
    ("organizer", "organiser"), ("organizers", "organisers"),
    ("memorize", "memorise"), ("memorized", "memorised"),
    ("prioritize", "prioritise"), ("prioritized", "prioritised"),
    ("minimize", "minimise"), ("maximize", "maximise"), ("characterize", "characterise"),
    ("characterized", "characterised"), ("legalize", "legalise"), ("mobilize", "mobilise"),
    ("finalize", "finalise"), ("standardize", "standardise"), ("sympathize", "sympathise"),
    ("stabilize", "stabilise"), ("utilize", "utilise"), ("visualize", "visualise"),
    ("analyze", "analyse"), ("analyzed", "analysed"), ("analyzes", "analyses"), ("analyzing", "analysing"),
    ("paralyze", "paralyse"), ("paralyzed", "paralysed"),
    ("behaviors", "behaviours"), ("neighboring", "neighbouring"), ("honors", "honours"),
("favorable", "favourable"), ("favor", "favour"), ("favors", "favours"),
    ("rumor", "rumour"), ("rumors", "rumours"), ("vapor", "vapour"), ("odor", "odour"),
    ("endeavor", "endeavour"), ("armor", "armour"), ("savor", "savour"), ("vigor", "vigour"),
    ("glamor", "glamour"), ("tumor", "tumour"), ("colored", "coloured"),
    ("fiber", "fibre"), ("fibers", "fibres"), ("caliber", "calibre"), ("somber", "sombre"),
    ("centimeter", "centimetre"), ("centimeters", "centimetres"), ("millimeter", "millimetre"),
    ("offense", "offence"), ("offenses", "offences"), ("pretense", "pretence"),
    ("dialog", "dialogue"), ("analog", "analogue"), ("program", "programme"), ("programs", "programmes"),
    ("catalogs", "catalogues"), ("monolog", "monologue"),
    ("fulfill", "fulfil"), ("enroll", "enrol"), ("enrollment", "enrolment"), ("installment", "instalment"),
    ("skillful", "skilful"), ("willful", "wilful"),
    ("labeled", "labelled"), ("labeling", "labelling"), ("modeled", "modelled"), ("modeling", "modelling"),
    ("leveled", "levelled"), ("signaled", "signalled"), ("fueled", "fuelled"), ("quarreled", "quarrelled"),
    ("counselor", "counsellor"), ("jeweler", "jeweller"), ("marvelous", "marvellous"),
    ("traveling", "travelling"), ("canceled", "cancelled"),
    ("aging", "ageing"), ("judgment", "judgement"), ("acknowledgment", "acknowledgement"),
    ("plow", "plough"), ("mold", "mould"), ("moldy", "mouldy"), ("smolder", "smoulder"),
    ("pediatrician", "paediatrician"), ("anesthesia", "anaesthesia"), ("anemia", "anaemia"),
    ("diarrhea", "diarrhoea"), ("encyclopedia", "encyclopaedia"), ("maneuver", "manoeuvre"),
    ("estrogen", "oestrogen"), ("fetus", "foetus"), ("orthopedic", "orthopaedic"),
    ("gynecologist", "gynaecologist"), ("hemorrhage", "haemorrhage"),
    ("tire", "tyre"), ("tires", "tyres"),
    ("curb", "kerb"), ("pajama", "pyjama"), ("aluminum", "aluminium"), ("skeptical", "sceptical"),
    ("skeptic", "sceptic"), ("whiskey", "whisky"), ("percent", "per cent"),
    ("ax", "axe"),
]
# Seulement les tetes ou le sens est sur : « check » (verbe), « draft »
# (brouillon), « practice » (nom) ne passent pas dans les phrases.
PAS_DANS_LES_PHRASES = {"tire", "tires"}

# Le vocabulaire : (americain, britannique). Repris de l'ancien
# english_britam.json (A2-B1), complete.
VOCABULAIRE = [
    ("apartment", "flat"), ("elevator", "lift"), ("fall", "autumn"), ("vacation", "holiday"),
    ("line", "queue"), ("sidewalk", "pavement"), ("highway", "motorway"), ("truck", "lorry"),
    ("gas", "petrol"), ("drugstore", "chemist's"), ("mail", "post"), ("mailman", "postman"),
    ("schedule", "timetable"), ("round-trip ticket", "return ticket"), ("one-way ticket", "single ticket"),
    ("first floor", "ground floor"), ("cookie", "biscuit"), ("chips", "crisps"), ("french fries", "chips"),
    ("candy", "sweets"), ("eggplant", "aubergine"), ("zucchini", "courgette"), ("cilantro", "coriander"),
    ("arugula", "rocket"), ("garbage", "rubbish"), ("trash can", "bin"), ("faucet", "tap"),
    ("closet", "wardrobe"), ("stove", "cooker"), ("diaper", "nappy"), ("pacifier", "dummy"),
    ("stroller", "pushchair"), ("parking lot", "car park"), ("gas station", "petrol station"),
    ("windshield", "windscreen"), ("hood", "bonnet"), ("trunk", "boot"), ("freeway", "motorway"),
    ("intersection", "crossroads"), ("crosswalk", "zebra crossing"), ("subway", "underground"),
    ("movie theater", "cinema"), ("movie", "film"), ("soccer", "football"), ("cell phone", "mobile phone"),
    ("zip code", "postcode"), ("principal", "head teacher"), ("grade", "mark"), ("semester", "term"),
    ("eraser", "rubber"), ("backpack", "rucksack"), ("sweater", "jumper"), ("sneakers", "trainers"),
    ("pants", "trousers"), ("vest", "waistcoat"), ("undershirt", "vest"), ("purse", "handbag"),
    ("wallet", "wallet"), ("restroom", "toilet"), ("check", "bill"), ("resume", "CV"),
    ("raise", "pay rise"), ("vacation day", "day off"), ("attorney", "solicitor"), ("lawyer", "lawyer"),
    ("realtor", "estate agent"), ("real estate agent", "estate agent"), ("drugstore", "chemist's"),
    ("pharmacist", "chemist"), ("ER", "A&E"), ("emergency room", "A&E"), ("Band-Aid", "plaster"),
    ("flashlight", "torch"), ("wrench", "spanner"), ("duct tape", "gaffer tape"), ("yard", "garden"),
    ("fire department", "fire brigade"), ("downtown", "city centre"), ("mall", "shopping centre"),
    ("bill", "note"), ("checking account", "current account"), ("ATM", "cash machine"),
    ("apartment building", "block of flats"), ("townhouse", "terraced house"), ("rent", "rent"),
    ("roommate", "flatmate"), ("comforter", "duvet"), ("plastic wrap", "cling film"),
    ("aluminum foil", "tin foil"), ("can", "tin"), ("takeout", "takeaway"), ("appetizer", "starter"),
    ("dessert", "pudding"), ("ground beef", "mince"), ("cotton candy", "candyfloss"),
    ("public school", "state school"), ("private school", "public school"), ("college", "university"),
    ("freshman", "first-year student"), ("tuition", "tuition fees"), ("bathrobe", "dressing gown"),
    ("fanny pack", "bum bag"), ("tuxedo", "dinner jacket"), ("pantyhose", "tights"),
    ("hood", "bonnet"), ("license plate", "number plate"), ("traffic circle", "roundabout"),
    ("rest stop", "service station"), ("detour", "diversion"), ("sedan", "saloon"),
    ("trailer", "caravan"), ("RV", "camper van"), ("railroad", "railway"), ("conductor", "guard"),
    ("vacationer", "holidaymaker"), ("airplane", "aeroplane"), ("baggage", "luggage"),
    ("carry-on", "hand luggage"), ("fall semester", "autumn term"),
]
# Ou le mot britannique a un autre sens courant en americain : on ne remplace
# pas ces tetes dans le sens GB -> US (« post », « bill », « mark », « vest »…).
AMBIGUS_GB = {"post", "bill", "note", "mark", "term", "vest", "rubber", "boot", "bonnet", "chips", "guard",
              "rocket", "tin", "public school", "university", "garden", "toilet", "pudding", "lawyer", "wallet",
              "rent", "luggage", "film", "chemist", "tights", "day off", "starter", "torch", "dummy", "football"}
# Les memes mots, mais pour un nom vedette (la carte) : sans ambiguite.
US_VERS_GB_VOCAB = {}
GB_VERS_US_VOCAB = {}
for _us, _gb in VOCABULAIRE:
    if _us.lower() == _gb.lower():
        continue
    US_VERS_GB_VOCAB.setdefault(_us.lower(), _gb)
    if _gb.lower() not in AMBIGUS_GB:
        GB_VERS_US_VOCAB.setdefault(_gb.lower(), _us)


def _britam():
    """Les paires de l'ancien module (english_britam.json) : « flat 🇬🇧 / apartment 🇺🇸 »."""
    try:
        d = json.load(io.open(os.path.join(RACINE, "english_britam.json"), encoding="utf-8"))
    except Exception:
        return
    for liste in d.values():
        for e in liste:
            m = re.match(r"^\s*(.+?)\s*🇬🇧\s*/\s*(.+?)\s*🇺🇸", e.get("mot", ""))
            if not m:
                continue
            gb, us = m.group(1).strip(), m.group(2).strip()
            US_VERS_GB_VOCAB.setdefault(us.lower(), gb)
            if gb.lower() not in AMBIGUS_GB:
                GB_VERS_US_VOCAB.setdefault(gb.lower(), us)


_britam()

# Les phrases de la banque ont ete ecrites pour l'allemand et l'espagnol :
# leurs villes et leur monnaie passent en Amerique (anglais ET francais).
LIEUX = [
    ("Berlin", "Boston"), ("Munich", "Chicago"), ("Hamburg", "Seattle"), ("Cologne", "Philadelphia"),
    ("Frankfurt", "Denver"), ("Stuttgart", "Portland"), ("Dresden", "Baltimore"), ("Leipzig", "Pittsburgh"),
    ("Vienna", "Montreal"), ("Zurich", "Toronto"), ("Madrid", "New York"), ("Barcelona", "San Francisco"),
    ("Seville", "Miami"), ("Valencia", "San Diego"), ("Málaga", "Los Angeles"), ("Bilbao", "Portland"),
    ("Granada", "Santa Fe"), ("Salamanca", "Providence"),
    ("euros", "dollars"), ("euro", "dollar"),
]

# Les pluriels que la regle (construire.pluriel) manque.
PLURIELS_IRREGULIERS = {
    "life": "lives", "wife": "wives", "knife": "knives", "leaf": "leaves", "half": "halves", "shelf": "shelves",
    "thief": "thieves", "wolf": "wolves", "loaf": "loaves", "calf": "calves", "self": "selves", "scarf": "scarves",
    "crisis": "crises", "analysis": "analyses", "thesis": "theses", "hypothesis": "hypotheses", "basis": "bases",
    "diagnosis": "diagnoses", "synthesis": "syntheses", "emphasis": "emphases", "axis": "axes", "oasis": "oases",
    "phenomenon": "phenomena", "criterion": "criteria", "medium": "media", "curriculum": "curricula",
    "bacterium": "bacteria", "datum": "data", "stimulus": "stimuli", "nucleus": "nuclei", "cactus": "cacti",
    "fungus": "fungi", "appendix": "appendices", "index": "indexes", "matrix": "matrices",
    "sheep": "sheep", "deer": "deer", "fish": "fish", "species": "species", "series": "series", "means": "means",
    "aircraft": "aircraft", "offspring": "offspring", "headquarters": "headquarters", "salmon": "salmon",
    "trout": "trout", "moose": "moose", "bison": "bison", "shrimp": "shrimp",
    "goose": "geese", "mouse": "mice", "louse": "lice", "ox": "oxen", "foot": "feet", "tooth": "teeth",
    "policeman": "policemen", "fireman": "firemen", "chairman": "chairmen", "fisherman": "fishermen",
    "businessman": "businessmen", "businesswoman": "businesswomen", "salesman": "salesmen",
    "craftsman": "craftsmen", "spokesman": "spokesmen", "snowman": "snowmen", "gentleman": "gentlemen",
    "passer-by": "passers-by", "mother-in-law": "mothers-in-law", "father-in-law": "fathers-in-law",
    "son-in-law": "sons-in-law", "daughter-in-law": "daughters-in-law", "brother-in-law": "brothers-in-law",
    "sister-in-law": "sisters-in-law", "potato": "potatoes", "tomato": "tomatoes", "hero": "heroes",
    "echo": "echoes", "volcano": "volcanoes", "mosquito": "mosquitoes", "veto": "vetoes",
    "studio": "studios", "logo": "logos", "kangaroo": "kangaroos", "casino": "casinos", "memo": "memos",
    "avocado": "avocados", "euro": "euros", "ego": "egos", "silo": "silos", "solo": "solos", "tattoo": "tattoos",
    "cello": "cellos", "disco": "discos", "taxi": "taxis", "chef": "chefs", "roof": "roofs", "chief": "chiefs",
    "belief": "beliefs", "proof": "proofs", "cliff": "cliffs", "giraffe": "giraffes",
}

# Les noms qui n'existent qu'au pluriel (drapeau plt) : pas de pluriel a montrer.
PLURIEL_SEUL = set("""
scissors pliers tongs tweezers headphones earphones savings lyrics cosmetics customs thanks dishes jeans pants
shorts trousers clothes glasses sunglasses goods earnings surroundings belongings outskirts premises stairs
congratulations remains groceries leftovers outdoors whereabouts riches proceeds lecture notes manners
""".split())

# Les noms qui ne se comptent pas (pas de pluriel affiche).
INDENOMBRABLES = set("""
advice information news furniture equipment luggage baggage homework housework knowledge research evidence
progress traffic weather money music water air rice bread butter cheese meat milk sugar salt flour oil
honey jam cream yogurt soup pasta spaghetti cereal chocolate coffee tea juice beer wine garlic pepper
spinach lettuce broccoli cabbage celery parsley cauliflower asparagus corn
patience courage honesty kindness happiness sadness anger fear love hate jealousy loneliness pride shame
health wealth poverty unemployment employment inflation pollution climate electricity energy fuel
gas petrol oxygen carbon steel iron gold silver copper wood plastic glass paper cotton wool leather silk
fun luck safety security justice freedom peace violence crime education literature art poetry software
hardware data feedback accommodation transportation transport machinery jewelry clothing underwear footwear
garbage trash rubbish litter waste dust dirt mud sand soil grass hay snow ice rain fog thunder lightning
sunshine heat cold warmth humidity scenery vocabulary grammar pronunciation spelling mathematics math
physics chemistry biology economics politics history geography psychology philosophy medicine
nature wildlife livestock cattle staff personnel police public audience management leadership
childhood adulthood youth old age retirement healthcare welfare insurance tax rent
stuff nonsense laughter applause behavior behaviour permission access support help assistance
""".split())

# Les tetes qu'on ne prend pas : trop allemandes ou espagnoles, ou des
# gloses plutot que des mots anglais courants.
ECARTES = set(s.strip().lower() for s in re.split(r"[|\n]", """
euro|euros|pretzel|bratwurst|sauerkraut|schnitzel|tapas|paella|siesta|bullfight|bullfighter|flamenco
oktoberfest|bundestag|chancellor|federal state|registration office|citizens' office|deposit bottle
deposit|vhs|adult education centre|adult education center|abitur|fiesta|churros|sangria|tortilla
gazpacho|chorizo|serrano ham|sherry|matador|corrida|torero|piñata|mariachi|tequila|taco|burrito
nacho|empanada|mate|poncho|sombrero|guacamole|quesadilla|tamale|plaza|bodega|hacienda|pueblo
lederhosen|dirndl|stein|beer garden|christmas market|advent calendar|carnival procession|kindergarten teacher
Sie|du|duzen|siezen|thing|things|stuff|it|one|ones|that|this|what|which|who|someone|something|anything
the same|other|others|own|person|people|man|woman|time|way|day|year|thing
""") if s.strip())
