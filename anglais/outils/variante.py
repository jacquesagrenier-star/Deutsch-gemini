# -*- coding: utf-8 -*-
"""L'americain et le britannique : ce que construire.py change d'un cours a l'autre.

La base est AMERICAINE (decide par Jacques le 27 oct. 2026) ;
le cours britannique (anglais/datos-gb) est calcule, jamais ecrit a la main.
Si Jacques choisit le britannique comme base, on n'inverse que le sens de lecture
de ces tables.

Deux sortes de differences :
  - l'ORTHOGRAPHE (color / colour) : une liste de mots, pas une regle -- « -or
    -> -our » casserait doctor, et « -ize -> -ise » size ;
  - le VOCABULAIRE (apartment / flat) : la carte du mot change dans
    noms_a1.py (drapeau gb=) ; dans les PHRASES des autres mots, seuls les
    remplacements surs sont faits ici (« fall » ou « check » sont aussi des
    verbes : on n'y touche pas dans les phrases).
"""

# (americain, britannique). Les formes flechies sont listees : c'est plus sur
# qu'une regle, et ca se relit.
ORTHOGRAPHE = [
    ("color", "colour"), ("colors", "colours"), ("colorful", "colourful"),
    ("favorite", "favourite"), ("favorites", "favourites"),
    ("neighbor", "neighbour"), ("neighbors", "neighbours"),
    ("neighborhood", "neighbourhood"), ("neighborhoods", "neighbourhoods"),
    ("center", "centre"), ("centers", "centres"),
    ("theater", "theatre"), ("theaters", "theatres"),
    ("meter", "metre"), ("meters", "metres"), ("liter", "litre"), ("liters", "litres"),
    ("kilometer", "kilometre"), ("kilometers", "kilometres"),
    ("gray", "grey"),
    ("traveled", "travelled"), ("traveling", "travelling"),
    ("traveler", "traveller"), ("travelers", "travellers"),
    ("canceled", "cancelled"), ("canceling", "cancelling"),
    ("organize", "organise"), ("organized", "organised"), ("organizes", "organises"), ("organizing", "organising"),
    ("realize", "realise"), ("realized", "realised"), ("realizes", "realises"),
    ("recognize", "recognise"), ("recognized", "recognised"),
    ("apologize", "apologise"), ("apologized", "apologised"),
    ("jewelry", "jewellery"), ("pajamas", "pyjamas"),
    ("defense", "defence"), ("license", "licence"),
    ("harbor", "harbour"), ("honor", "honour"), ("humor", "humour"),
    ("labor", "labour"), ("flavor", "flavour"), ("flavors", "flavours"),
    ("behavior", "behaviour"), ("airplane", "aeroplane"), ("airplanes", "aeroplanes"),
    ("cozy", "cosy"), ("mustache", "moustache"), ("catalog", "catalogue"),
]

# Remplacements de vocabulaire faits dans TOUTES les phrases du cours britannique.
# Seulement des mots sans autre sens courant dans nos phrases.
VOCABULAIRE_PHRASES = [
    ("apartments", "flats"), ("apartment", "flat"),
    ("elevators", "lifts"), ("elevator", "lift"),
    ("cell phones", "mobile phones"), ("cell phone", "mobile phone"),
    ("subway", "underground"),
    ("vacations", "holidays"), ("vacation", "holiday"),
    ("cookies", "biscuits"), ("cookie", "biscuit"),
    ("trucks", "lorries"), ("truck", "lorry"),
    ("sidewalks", "pavements"), ("sidewalk", "pavement"),
    ("parking lots", "car parks"), ("parking lot", "car park"),
    ("gas stations", "petrol stations"), ("gas station", "petrol station"),
    ("movie theaters", "cinemas"), ("movie theater", "cinema"),
    ("movies", "films"), ("movie", "film"),
    ("sweaters", "jumpers"), ("sweater", "jumper"),
    ("sneakers", "trainers"), ("sneaker", "trainer"),
    ("faucets", "taps"), ("faucet", "tap"),
    ("closets", "wardrobes"), ("closet", "wardrobe"),
    ("last names", "surnames"), ("last name", "surname"),
    ("moms", "mums"), ("mom", "mum"),
    ("math", "maths"), ("soccer", "football"),
    ("motorcycles", "motorbikes"), ("motorcycle", "motorbike"),
    ("erasers", "rubbers"), ("eraser", "rubber"),
    ("pants", "trousers"), ("purses", "handbags"), ("purse", "handbag"),
    ("stove", "cooker"), ("bathtub", "bath"),
    ("driver's license", "driving licence"), ("city hall", "town hall"),
    ("trash", "rubbish"), ("garbage", "rubbish"),
    ("candy", "sweets"), ("french fries", "chips"),
    ("gotten", "got"), ("the check, please", "the bill, please"), ("the check", "the bill"),
    ("911", "999"),
]

# « the store », « a store » -> shop : pas le verbe « to store ».
DETERMINANTS_STORE = r"(the|a|this|that|my|your|our|his|her|their|grocery|clothing|shoe|book|toy|candy)"

# Mots qui trahissent une phrase britannique dans la banque (phrases ecrites
# pour l'allemand et l'espagnol) : on ne la prend pas pour le cours americain.
MARQUES_BRITANNIQUES = [
    "flat", "flats", "lift", "lifts", "mobile", "lorry", "lorries", "petrol", "autumn",
    "biscuit", "biscuits", "trousers", "jumper", "jumpers", "trainers", "pavement",
    "motorway", "rubbish", "queue", "queues", "timetable", "mum", "maths", "cinema",
    "chemist", "chemist's", "fortnight", "holiday", "holidays", "rubber", "rucksack",
    "car park", "postman", "post", "shop assistant", "underground", "football", "tap",
    "cooker", "wardrobe", "surname", "bin", "crisps", "chips", "sweets",
    "learnt", "spelt", "dreamt", "got to know", "whilst", "film", "films", "storey",
    "ground floor", "first floor", "single ticket", "return ticket", "pounds", "pound",
]
