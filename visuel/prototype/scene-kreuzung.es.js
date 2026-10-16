// GENERE par construire.py (espanol/kreuzung.json) -- ne pas modifier a la main.
window.SCENE = {
 "image": "kreuzung.webp",
 "points": [
  {
   "id": "gebaeude",
   "mot": "edificio",
   "genre": "el",
   "pluriel": "los edificios",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "casa",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_casa",
     "fr": "la maison",
     "en": "the house",
     "pt": "a casa",
     "ar": "بيت"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     0,
     100,
     15
    ]
   ],
   "fr": "l'immeuble, le bâtiment",
   "en": "the building",
   "pt": "o prédio, o edifício",
   "ar": "عمارة، مبنى",
   "pl": "budynek",
   "ru": "здание",
   "latam": null
  },
  {
   "id": "strasse",
   "mot": "calle",
   "genre": "la",
   "pluriel": "las calles",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "cruce",
     "genre": "el",
     "niveau": "A2",
     "theme": "orientarse",
     "fr": "le carrefour",
     "en": "the crossroads",
     "pt": "o cruzamento",
     "ar": "تقاطع"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     31,
     100,
     13
    ],
    [
     0,
     44,
     100,
     42
    ]
   ],
   "fr": "la rue",
   "en": "the street",
   "pt": "a rua",
   "ar": "شارع",
   "pl": "ulica",
   "ru": "улица",
   "latam": null
  },
  {
   "id": "buergersteig",
   "mot": "acera",
   "genre": "la",
   "pluriel": "las aceras",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     92,
     100,
     8
    ]
   ],
   "fr": "le trottoir",
   "en": "the pavement",
   "pt": "a calçada",
   "ar": "رصيف",
   "pl": "chodnik",
   "ru": "тротуар",
   "latam": {
    "mot": "banqueta",
    "genre": "la",
    "pluriel": "las banquetas"
   }
  },
  {
   "id": "baeckerei",
   "mot": "panadería",
   "genre": "la",
   "pluriel": "las panaderías",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     3,
     18,
     26,
     13
    ]
   ],
   "fr": "la boulangerie",
   "en": "the bakery",
   "pt": "a padaria",
   "ar": "مخبز",
   "pl": "piekarnia",
   "ru": "булочная, пекарня",
   "latam": null
  },
  {
   "id": "brot",
   "mot": "pan",
   "genre": "el",
   "pluriel": "los panes",
   "niveau": "A1",
   "theme": "la_comida",
   "personne": null,
   "aussi": [
    {
     "mot": "pretzel",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_comida",
     "fr": "le bretzel",
     "en": "the pretzel",
     "pt": "o pretzel",
     "ar": "بريتزل (كعك ألماني مملّح)"
    },
    {
     "mot": "escaparate",
     "genre": "el",
     "niveau": "A1",
     "theme": "las_compras",
     "fr": "la vitrine",
     "en": "the shop window",
     "pt": "a vitrine",
     "ar": "واجهة المتجر",
     "latam": {
      "mot": "aparador",
      "genre": "el",
      "pluriel": "los aparadores"
     }
    }
   ],
   "sur": "baeckerei",
   "devant": 0,
   "boites": [
    [
     4,
     20,
     13,
     10.3
    ]
   ],
   "fr": "le pain",
   "en": "bread",
   "pt": "o pão",
   "ar": "خبز",
   "pl": "chleb",
   "ru": "хлеб",
   "latam": null
  },
  {
   "id": "apotheke",
   "mot": "farmacia",
   "genre": "la",
   "pluriel": "las farmacias",
   "niveau": "A1",
   "theme": "el_cuerpo",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     30.5,
     16.7,
     19.5,
     11.6
    ]
   ],
   "fr": "la pharmacie",
   "en": "the chemist's",
   "pt": "a farmácia",
   "ar": "صيدلية",
   "pl": "apteka",
   "ru": "аптека",
   "latam": null
  },
  {
   "id": "post",
   "mot": "oficina de correos",
   "genre": "la",
   "pluriel": "las oficinas de correos",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     50,
     16.4,
     8.5,
     11.6
    ]
   ],
   "fr": "le bureau de poste",
   "en": "the post office",
   "pt": "a agência dos correios",
   "ar": "مكتب البريد",
   "pl": "poczta",
   "ru": "почта",
   "latam": null
  },
  {
   "id": "briefkasten-post",
   "mot": "buzón",
   "genre": "el",
   "pluriel": "los buzones",
   "niveau": "A2",
   "theme": "la_vivienda",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     50.2,
     23,
     4.7,
     5
    ]
   ],
   "fr": "la boîte aux lettres",
   "en": "the letterbox",
   "pt": "a caixa de correio",
   "ar": "صندوق البريد",
   "pl": "skrzynka pocztowa",
   "ru": "почтовый ящик",
   "latam": null
  },
  {
   "id": "cafe",
   "mot": "cafetería",
   "genre": "la",
   "pluriel": "las cafeterías",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "mesa",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_casa",
     "fr": "la table",
     "en": "the table",
     "pt": "a mesa",
     "ar": "طاولة"
    },
    {
     "mot": "silla",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_casa",
     "fr": "la chaise",
     "en": "the chair",
     "pt": "a cadeira",
     "ar": "كرسي"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     61.8,
     15,
     33,
     13
    ]
   ],
   "fr": "le café (l'établissement)",
   "en": "the café",
   "pt": "a cafeteria, o café",
   "ar": "مقهى",
   "pl": "kawiarnia",
   "ru": "кафе",
   "latam": null
  },
  {
   "id": "markise",
   "mot": "toldo",
   "genre": "el",
   "pluriel": "los toldos",
   "niveau": "A2",
   "theme": "nom_casa",
   "personne": null,
   "aussi": [],
   "sur": "cafe",
   "devant": 0,
   "boites": [
    [
     62.7,
     15,
     31.6,
     4.3
    ]
   ],
   "fr": "le store (auvent)",
   "en": "the awning",
   "pt": "o toldo",
   "ar": "مظلّة (قماشية)",
   "pl": "markiza",
   "ru": "маркиза, навес",
   "latam": null
  },
  {
   "id": "bus",
   "mot": "autobús",
   "genre": "el",
   "pluriel": "los autobuses",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     31.9,
     32,
     12.6
    ]
   ],
   "fr": "l'autobus",
   "en": "the bus",
   "pt": "o ônibus",
   "ar": "حافلة",
   "pl": "autobus",
   "ru": "автобус",
   "latam": null
  },
  {
   "id": "wartehaeuschen",
   "mot": "marquesina",
   "genre": "la",
   "pluriel": "las marquesinas",
   "niveau": "B1",
   "theme": "la_movilidad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     0,
     39.2,
     16,
     10.8
    ]
   ],
   "fr": "l'abribus",
   "en": "the bus shelter",
   "pt": "o abrigo de ônibus",
   "ar": "مظلّة موقف الحافلات",
   "pl": "wiata przystankowa",
   "ru": "павильон остановки",
   "latam": null
  },
  {
   "id": "haltestelle",
   "mot": "parada",
   "genre": "la",
   "pluriel": "las paradas",
   "niveau": "A1",
   "theme": "el_transporte",
   "personne": null,
   "aussi": [
    {
     "mot": "señal",
     "genre": "la",
     "niveau": "A2",
     "theme": "orientarse",
     "fr": "le panneau",
     "en": "the sign",
     "pt": "a placa, o sinal",
     "ar": "لافتة، إشارة"
    }
   ],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     15.7,
     37.5,
     3.6,
     13.3
    ]
   ],
   "fr": "l'arrêt",
   "en": "the stop",
   "pt": "o ponto, a parada",
   "ar": "موقف، محطة توقّف",
   "pl": "przystanek",
   "ru": "остановка",
   "latam": null
  },
  {
   "id": "frau-rot",
   "mot": "mujer",
   "genre": "la",
   "pluriel": "las mujeres",
   "niveau": "A1",
   "theme": "la_familia",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     19.9,
     44.2,
     3.9,
     6.9
    ]
   ],
   "fr": "la femme, l'épouse",
   "en": "the wife, the woman",
   "pt": "a mulher, a esposa",
   "ar": "امرأة، زوجة",
   "pl": "kobieta / żona",
   "ru": "женщина, жена",
   "latam": null
  },
  {
   "id": "auto-dunkel",
   "mot": "coche",
   "genre": "el",
   "pluriel": "los coches",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "aparcamiento",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_ciudad",
     "fr": "la place de stationnement",
     "en": "the parking space",
     "pt": "a vaga (de estacionamento)",
     "ar": "موقف سيارات",
     "latam": {
      "mot": "estacionamiento",
      "genre": "el",
      "pluriel": "los estacionamientos"
     }
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     32.3,
     34.4,
     18.8,
     6.2
    ]
   ],
   "fr": "la voiture",
   "en": "the car",
   "pt": "o carro",
   "ar": "سيارة",
   "pl": "samochód",
   "ru": "машина, автомобиль",
   "latam": {
    "mot": "carro",
    "genre": "el",
    "pluriel": "los carros"
   }
  },
  {
   "id": "auto-silber",
   "mot": "coche",
   "genre": "el",
   "pluriel": "los coches",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "aparcamiento",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_ciudad",
     "fr": "la place de stationnement",
     "en": "the parking space",
     "pt": "a vaga (de estacionamento)",
     "ar": "موقف سيارات",
     "latam": {
      "mot": "estacionamiento",
      "genre": "el",
      "pluriel": "los estacionamientos"
     }
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     51,
     33.1,
     14.8,
     4.3
    ]
   ],
   "fr": "la voiture",
   "en": "the car",
   "pt": "o carro",
   "ar": "سيارة",
   "pl": "samochód",
   "ru": "машина, автомобиль",
   "latam": {
    "mot": "carro",
    "genre": "el",
    "pluriel": "los carros"
   }
  },
  {
   "id": "parkuhr",
   "mot": "parquímetro",
   "genre": "el",
   "pluriel": "los parquímetros",
   "niveau": "B1",
   "theme": "la_movilidad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     54.8,
     33.9,
     2.7,
     6.4
    ]
   ],
   "fr": "le parcmètre",
   "en": "the parking meter",
   "pt": "o parquímetro",
   "ar": "عدّاد مواقف",
   "pl": "parkometr",
   "ru": "паркомат",
   "latam": null
  },
  {
   "id": "schild-klein",
   "mot": "señal",
   "genre": "la",
   "pluriel": "las señales",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     49.1,
     37,
     2.9,
     3
    ]
   ],
   "fr": "le panneau",
   "en": "the sign",
   "pt": "a placa, o sinal",
   "ar": "لافتة، إشارة",
   "pl": "znak drogowy",
   "ru": "дорожный знак",
   "latam": null
  },
  {
   "id": "schild-gross",
   "mot": "señal",
   "genre": "la",
   "pluriel": "las señales",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     73.7,
     38.6,
     5,
     3
    ]
   ],
   "fr": "le panneau",
   "en": "the sign",
   "pt": "a placa, o sinal",
   "ar": "لافتة، إشارة",
   "pl": "znak drogowy",
   "ru": "дорожный знак",
   "latam": null
  },
  {
   "id": "ampel-mitte",
   "mot": "semáforo",
   "genre": "el",
   "pluriel": "los semáforos",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     72.4,
     43,
     8,
     13.5
    ]
   ],
   "fr": "le feu de circulation",
   "en": "the traffic light",
   "pt": "o semáforo, o sinal",
   "ar": "إشارة المرور",
   "pl": "sygnalizacja świetlna, światła",
   "ru": "светофор",
   "latam": null
  },
  {
   "id": "ampel-seite",
   "mot": "semáforo",
   "genre": "el",
   "pluriel": "los semáforos",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     78.2,
     27.6,
     2.6,
     3
    ]
   ],
   "fr": "le feu de circulation",
   "en": "the traffic light",
   "pt": "o semáforo, o sinal",
   "ar": "إشارة المرور",
   "pl": "sygnalizacja świetlna, światła",
   "ru": "светофор",
   "latam": null
  },
  {
   "id": "lieferwagen",
   "mot": "furgoneta",
   "genre": "la",
   "pluriel": "las furgonetas",
   "niveau": "A1",
   "theme": "el_transporte",
   "personne": null,
   "aussi": [
    {
     "mot": "camión",
     "genre": "el",
     "niveau": "A1",
     "theme": "el_transporte",
     "fr": "le camion",
     "en": "the lorry, the truck",
     "pt": "o caminhão",
     "ar": "شاحنة"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     84.7,
     22.2,
     15.3,
     12.8
    ]
   ],
   "fr": "la camionnette",
   "en": "the van",
   "pt": "a van, a caminhonete",
   "ar": "شاحنة صغيرة",
   "pl": "samochód dostawczy",
   "ru": "фургон для доставки",
   "latam": {
    "mot": "camioneta",
    "genre": "la",
    "pluriel": "las camionetas"
   }
  },
  {
   "id": "zebrastreifen",
   "mot": "paso de cebra",
   "genre": "el",
   "pluriel": "los pasos de cebra",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     16,
     54.3,
     60,
     9
    ]
   ],
   "fr": "le passage piéton",
   "en": "the zebra crossing",
   "pt": "a faixa de pedestres",
   "ar": "ممرّ المُشاة",
   "pl": "przejście dla pieszych, zebra",
   "ru": "пешеходный переход, «зебра»",
   "latam": {
    "mot": "paso peatonal",
    "genre": "el",
    "pluriel": "los pasos peatonales"
   }
  },
  {
   "id": "zebrastreifen-2",
   "mot": "paso de cebra",
   "genre": "el",
   "pluriel": "los pasos de cebra",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     68,
     47.5,
     22.5,
     8
    ]
   ],
   "fr": "le passage piéton",
   "en": "the zebra crossing",
   "pt": "a faixa de pedestres",
   "ar": "ممرّ المُشاة",
   "pl": "przejście dla pieszych, zebra",
   "ru": "пешеходный переход, «зебра»",
   "latam": {
    "mot": "paso peatonal",
    "genre": "el",
    "pluriel": "los pasos peatonales"
   }
  },
  {
   "id": "fussgaenger",
   "mot": "peatón",
   "genre": "el",
   "pluriel": "los peatones",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [
    {
     "mot": "hombre",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_familia",
     "fr": "l'homme",
     "en": "the man",
     "pt": "o homem",
     "ar": "رجل"
    },
    {
     "mot": "mochila",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ropa",
     "fr": "le sac à dos",
     "en": "the backpack",
     "pt": "a mochila",
     "ar": "حقيبة ظهر"
    }
   ],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     51.8,
     48.6,
     4.8,
     8.3
    ]
   ],
   "fr": "le piéton",
   "en": "the pedestrian",
   "pt": "o pedestre",
   "ar": "مُشاة",
   "pl": "pieszy",
   "ru": "пешеход",
   "latam": null
  },
  {
   "id": "frau-tasche",
   "mot": "mujer",
   "genre": "la",
   "pluriel": "las mujeres",
   "niveau": "A1",
   "theme": "la_familia",
   "personne": null,
   "aussi": [
    {
     "mot": "bolsa",
     "genre": "la",
     "niveau": "A1",
     "theme": "las_compras",
     "fr": "le sac",
     "en": "the bag",
     "pt": "a sacola",
     "ar": "كيس"
    }
   ],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     60.3,
     49.7,
     6.7,
     7.6
    ]
   ],
   "fr": "la femme, l'épouse",
   "en": "the wife, the woman",
   "pt": "a mulher, a esposa",
   "ar": "امرأة، زوجة",
   "pl": "kobieta / żona",
   "ru": "женщина, жена",
   "latam": null
  },
  {
   "id": "taxi",
   "mot": "taxi",
   "genre": "el",
   "pluriel": "los taxis",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [
    {
     "mot": "coche",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_ciudad",
     "fr": "la voiture",
     "en": "the car",
     "pt": "o carro",
     "ar": "سيارة",
     "latam": {
      "mot": "carro",
      "genre": "el",
      "pluriel": "los carros"
     }
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     1.8,
     59.5,
     41.2,
     11.3
    ]
   ],
   "fr": "le taxi",
   "en": "the taxi",
   "pt": "o táxi",
   "ar": "سيارة أجرة، تاكسي",
   "pl": "taksówka",
   "ru": "такси",
   "latam": null
  },
  {
   "id": "strassenbahn",
   "mot": "tranvía",
   "genre": "el",
   "pluriel": "los tranvías",
   "niveau": "A1",
   "theme": "el_transporte",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     78.4,
     48,
     21.6,
     17
    ]
   ],
   "fr": "le tramway",
   "en": "the tram",
   "pt": "o bonde",
   "ar": "ترام",
   "pl": "tramwaj",
   "ru": "трамвай",
   "latam": null
  },
  {
   "id": "motorrad",
   "mot": "moto",
   "genre": "la",
   "pluriel": "las motos",
   "niveau": "A1",
   "theme": "el_transporte",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     69.5,
     15.2,
     6.5
    ]
   ],
   "fr": "la moto",
   "en": "the motorbike",
   "pt": "a moto",
   "ar": "درّاجة نارية",
   "pl": "motocykl",
   "ru": "мотоцикл",
   "latam": null
  },
  {
   "id": "radweg",
   "mot": "carril bici",
   "genre": "el",
   "pluriel": "los carriles bici",
   "niveau": "B1",
   "theme": "la_movilidad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     11.6,
     72,
     88.4,
     16
    ]
   ],
   "fr": "la piste cyclable",
   "en": "the cycle lane",
   "pt": "a ciclovia",
   "ar": "مسار الدرّاجات",
   "pl": "ścieżka rowerowa",
   "ru": "велосипедная дорожка",
   "latam": {
    "mot": "ciclovía",
    "genre": "la",
    "pluriel": "las ciclovías"
   }
  },
  {
   "id": "radfahrer",
   "mot": "ciclista",
   "genre": "el",
   "pluriel": "los ciclistas",
   "niveau": "B1",
   "theme": "la_movilidad",
   "personne": null,
   "aussi": [
    {
     "mot": "bicicleta",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ciudad",
     "fr": "le vélo",
     "en": "the bicycle",
     "pt": "a bicicleta",
     "ar": "درّاجة"
    },
    {
     "mot": "chaqueta",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ropa",
     "fr": "la veste",
     "en": "the jacket",
     "pt": "a jaqueta, o casaco",
     "ar": "سترة، جاكيت"
    }
   ],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     69,
     70.9,
     18.4,
     11.9
    ]
   ],
   "fr": "le cycliste",
   "en": "the cyclist",
   "pt": "o/a ciclista",
   "ar": "راكب درّاجة",
   "pl": "rowerzysta",
   "ru": "велосипедист",
   "latam": null
  },
  {
   "id": "helm",
   "mot": "casco",
   "genre": "el",
   "pluriel": "los cascos",
   "niveau": "A2",
   "theme": "la_seguridad",
   "personne": null,
   "aussi": [],
   "sur": "radfahrer",
   "devant": 0,
   "boites": [
    [
     76.3,
     70.9,
     3,
     1.4
    ]
   ],
   "fr": "le casque",
   "en": "the helmet",
   "pt": "o capacete",
   "ar": "خوذة",
   "pl": "kask",
   "ru": "шлем",
   "latam": null
  },
  {
   "id": "kiosk",
   "mot": "quiosco",
   "genre": "el",
   "pluriel": "los quioscos",
   "niveau": "B1",
   "theme": "nom_paisaje",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 2,
   "boites": [
    [
     1.3,
     73.2,
     29.2,
     24.3
    ]
   ],
   "fr": "le kiosque",
   "en": "the newsstand",
   "pt": "a banca (de jornal)",
   "ar": "كشك",
   "pl": "kiosk",
   "ru": "киоск",
   "latam": null
  },
  {
   "id": "flasche",
   "mot": "botella",
   "genre": "la",
   "pluriel": "las botellas",
   "niveau": "A1",
   "theme": "la_comida",
   "personne": null,
   "aussi": [],
   "sur": "kiosk",
   "devant": 0,
   "boites": [
    [
     10.6,
     81,
     12,
     6.8
    ]
   ],
   "fr": "la bouteille",
   "en": "bottle",
   "pt": "a garrafa",
   "ar": "زجاجة",
   "pl": "butelka",
   "ru": "бутылка",
   "latam": null
  },
  {
   "id": "briefkasten",
   "mot": "buzón",
   "genre": "el",
   "pluriel": "los buzones",
   "niveau": "A2",
   "theme": "la_vivienda",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 2,
   "boites": [
    [
     34,
     81.7,
     9.7,
     11.5
    ]
   ],
   "fr": "la boîte aux lettres",
   "en": "the letterbox",
   "pt": "a caixa de correio",
   "ar": "صندوق البريد",
   "pl": "skrzynka pocztowa",
   "ru": "почтовый ящик",
   "latam": null
  },
  {
   "id": "laterne",
   "mot": "farola",
   "genre": "la",
   "pluriel": "las farolas",
   "niveau": "A2",
   "theme": "orientarse",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 2,
   "boites": [
    [
     43.5,
     60.2,
     8.3,
     37.6
    ]
   ],
   "fr": "le réverbère",
   "en": "the street lamp",
   "pt": "o poste de luz",
   "ar": "عمود إنارة",
   "pl": "latarnia uliczna",
   "ru": "фонарь",
   "latam": {
    "mot": "farol",
    "genre": "el",
    "pluriel": "los faroles"
   }
  },
  {
   "id": "anna",
   "mot": "mujer",
   "genre": "la",
   "pluriel": "las mujeres",
   "niveau": "A1",
   "theme": "la_familia",
   "personne": "Anna",
   "aussi": [
    {
     "mot": "móvil",
     "genre": "el",
     "niveau": "A1",
     "theme": "la_casa",
     "fr": "le téléphone portable",
     "en": "the mobile phone",
     "pt": "o celular",
     "ar": "هاتف محمول",
     "latam": {
      "mot": "celular",
      "genre": "el",
      "pluriel": "los celulares"
     }
    },
    {
     "mot": "chaqueta",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ropa",
     "fr": "la veste",
     "en": "the jacket",
     "pt": "a jaqueta, o casaco",
     "ar": "سترة، جاكيت"
    }
   ],
   "sur": null,
   "devant": 3,
   "boites": [
    [
     48.8,
     79.5,
     7.8,
     16.5
    ]
   ],
   "fr": "la femme, l'épouse",
   "en": "the wife, the woman",
   "pt": "a mulher, a esposa",
   "ar": "امرأة، زوجة",
   "pl": "kobieta / żona",
   "ru": "женщина, жена",
   "latam": null
  },
  {
   "id": "ampel-vorne",
   "mot": "semáforo",
   "genre": "el",
   "pluriel": "los semáforos",
   "niveau": "A1",
   "theme": "la_ciudad",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 2,
   "boites": [
    [
     56.5,
     78.5,
     12.3,
     21.5
    ]
   ],
   "fr": "le feu de circulation",
   "en": "the traffic light",
   "pt": "o semáforo, o sinal",
   "ar": "إشارة المرور",
   "pl": "sygnalizacja świetlna, światła",
   "ru": "светофор",
   "latam": null
  },
  {
   "id": "fahrradstaender",
   "mot": "aparcabicis",
   "genre": "el",
   "pluriel": "los aparcabicis",
   "niveau": "B1",
   "theme": "la_movilidad",
   "personne": null,
   "aussi": [
    {
     "mot": "bicicleta",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ciudad",
     "fr": "le vélo",
     "en": "the bicycle",
     "pt": "a bicicleta",
     "ar": "درّاجة"
    }
   ],
   "sur": null,
   "devant": 2,
   "boites": [
    [
     73.3,
     84.7,
     26.2,
     14.6
    ]
   ],
   "fr": "le support à vélos",
   "en": "the bike rack",
   "pt": "o bicicletário",
   "ar": "موقف درّاجات",
   "pl": "stojak na rowery",
   "ru": "велопарковка",
   "latam": {
    "mot": "bicicletero",
    "genre": "el",
    "pluriel": "los bicicleteros"
   }
  },
  {
   "id": "haus",
   "mot": "casa",
   "genre": "la",
   "pluriel": "las casas",
   "niveau": "A1",
   "theme": "la_casa",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     0,
     100,
     18
    ]
   ],
   "fr": "la maison",
   "en": "the house",
   "pt": "a casa",
   "ar": "بيت",
   "pl": "dom",
   "ru": "дом",
   "latam": null
  }
 ],
 "grosPlans": [],
 "titre": "En el cruce",
 "alt": "Un carrefour de Berlin vu d'un premier étage : boulangerie, pharmacie, poste et café, un arrêt de bus, un tram, un taxi, des piétons sur le passage, un cycliste sur la piste rouge ; au premier plan, Anna cherche son chemin sur son téléphone, entre le kiosque, la boîte aux lettres et les vélos.",
 "consigne": "Anna cherche son chemin dans Berlin. Touche un bâtiment, un véhicule ou une personne.",
 "exclus": [],
 "couches": {
  "A1": {
   "titre": "Noms et articles"
  },
  "A2": {
   "titre": "¿Dónde está? — en la ciudad",
   "qs": [
    {
     "q": "¿Dónde está la farmacia?",
     "c": [
      "entre la panadería y la oficina de correos",
      "al lado de la cafetería",
      "en la esquina"
     ],
     "f": "apotheke",
     "r": "post",
     "phrase": "La farmacia está entre la panadería y la oficina de correos.",
     "sens": "La pharmacie est entre la boulangerie et la poste.",
     "n": "<b>entre</b> = entre, sans « de » : entre la panadería y la oficina de correos."
    },
    {
     "q": "¿Dónde está la cafetería?",
     "c": [
      "en la esquina",
      "entre la panadería y la farmacia",
      "al lado del quiosco"
     ],
     "f": "cafe",
     "phrase": "La cafetería está en la esquina.",
     "sens": "Le café est au coin.",
     "n": "Au coin : <b>en la esquina</b>. Le lieu se dit avec <b>estar</b>."
    },
    {
     "q": "¿Dónde está la panadería?",
     "c": [
      "enfrente del quiosco",
      "al lado del quiosco",
      "detrás del quiosco"
     ],
     "f": "baeckerei",
     "r": "kiosk",
     "phrase": "La panadería está enfrente del quiosco.",
     "sens": "La boulangerie est en face du kiosque.",
     "n": "<b>enfrente de</b> = en face de. de + el = <b>del</b> : enfrente <b>del</b> quiosco."
    },
    {
     "q": "¿Qué hay delante de la oficina de correos?",
     "c": [
      "un buzón",
      "un taxi",
      "un quiosco"
     ],
     "f": "briefkasten-post",
     "r": "post",
     "phrase": "Delante de la oficina de correos hay un buzón.",
     "sens": "Devant la poste, il y a une boîte aux lettres.",
     "n": "Pour dire ce qu'il y a, sans article défini → <b>hay</b> + un / una."
    },
    {
     "q": "¿Dónde espera la mujer del abrigo rojo?",
     "c": [
      "en la parada",
      "delante de la farmacia",
      "en el carril bici"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "La mujer del abrigo rojo espera en la parada.",
     "sens": "La femme au manteau rouge attend à l'arrêt.",
     "n": "<b>en</b> = à, dans : le lieu où l'on est (en la parada).",
     "latam": {
      "c": [
       "en la parada",
       "delante de la farmacia",
       "en la ciclovía"
      ]
     }
    },
    {
     "q": "¿Por dónde va el ciclista?",
     "c": [
      "por el carril bici",
      "por la acera",
      "en el autobús"
     ],
     "f": "radfahrer",
     "r": "radweg",
     "phrase": "El ciclista va por el carril bici.",
     "sens": "Le cycliste roule sur la piste cyclable.",
     "n": "<b>por</b> = le long de, par où l'on passe : va <b>por</b> el carril bici.",
     "latam": {
      "c": [
       "por la ciclovía",
       "por la banqueta",
       "en el autobús"
      ],
      "phrase": "El ciclista va por la ciclovía."
     }
    },
    {
     "q": "¿Dónde está Anna?",
     "c": [
      "entre la farola y el semáforo",
      "delante de la panadería",
      "en la parada"
     ],
     "f": "anna",
     "r": "ampel-vorne",
     "phrase": "Anna está entre la farola y el semáforo.",
     "sens": "Anna est entre le lampadaire et le feu.",
     "n": "<b>entre</b> … <b>y</b> … : entre la farola y el semáforo.",
     "latam": {
      "c": [
       "entre el farol y el semáforo",
       "delante de la panadería",
       "en la parada"
      ],
      "phrase": "Anna está entre el farol y el semáforo."
     }
    },
    {
     "q": "¿Dónde están las bicicletas?",
     "c": [
      "en el aparcabicis",
      "en la parada",
      "delante de correos"
     ],
     "f": "fahrradstaender",
     "phrase": "Las bicicletas están en el aparcabicis.",
     "sens": "Les vélos sont au porte-vélos.",
     "n": "Pluriel → <b>están</b>.",
     "latam": {
      "c": [
       "en el bicicletero",
       "en la parada",
       "delante de correos"
      ],
      "phrase": "Las bicicletas están en el bicicletero."
     }
    },
    {
     "q": "¿Dónde están los peatones?",
     "c": [
      "en el paso de cebra",
      "en el carril bici",
      "en la cafetería"
     ],
     "f": "fussgaenger",
     "r": "zebrastreifen",
     "phrase": "Los peatones están en el paso de cebra.",
     "sens": "Les piétons sont sur le passage piéton.",
     "n": "Pluriel → <b>están</b>. El paso de cebra = le passage piéton.",
     "latam": {
      "c": [
       "en el paso peatonal",
       "en la ciclovía",
       "en la cafetería"
      ],
      "phrase": "Los peatones están en el paso peatonal."
     }
    },
    {
     "q": "¿Dónde está el quiosco?",
     "c": [
      "en la acera",
      "en la calle",
      "en la panadería"
     ],
     "f": "kiosk",
     "r": "buergersteig",
     "phrase": "El quiosco está en la acera.",
     "sens": "Le kiosque est sur le trottoir.",
     "n": "La acera = le trottoir ; la calle = la chaussée, la rue.",
     "latam": {
      "c": [
       "en la banqueta",
       "en la calle",
       "en la panadería"
      ],
      "phrase": "El quiosco está en la banqueta."
     }
    }
   ]
  },
  "B1": {
   "titre": "Indiquer le chemin — l'impératif de usted",
   "qs": [
    {
     "q": "Anna pregunta: —Perdone, ¿cómo ___ a la farmacia?",
     "c": [
      "llego",
      "llega",
      "llegué"
     ],
     "f": "anna",
     "r": "apotheke",
     "phrase": "Perdone, ¿cómo llego a la farmacia?",
     "sens": "Excusez-moi, comment aller à la pharmacie ?",
     "n": "Pour demander son chemin : <b>¿Cómo llego a…?</b> (llegar, je)."
    },
    {
     "q": "___ la calle por el paso de cebra.",
     "c": [
      "Cruce",
      "Cruza",
      "Cruzar"
     ],
     "f": "zebrastreifen",
     "phrase": "Cruce la calle por el paso de cebra.",
     "sens": "Traversez la rue au passage piéton.",
     "n": "Impératif de <b>usted</b> = subjonctif présent : cruzar → <b>cruce</b> (z → c devant e).",
     "latam": {
      "q": "___ la calle por el paso peatonal.",
      "phrase": "Cruce la calle por el paso peatonal."
     }
    },
    {
     "q": "___ hasta que el semáforo se ponga verde.",
     "c": [
      "Espere",
      "Espera",
      "Esperar"
     ],
     "f": "ampel-vorne",
     "phrase": "Espere hasta que el semáforo se ponga verde.",
     "sens": "Attendez que le feu passe au vert.",
     "n": "Usted → <b>espere</b>. Et <b>hasta que</b> + avenir prend le subjonctif : se ponga."
    },
    {
     "q": "Siga todo recto ___ la esquina.",
     "c": [
      "hasta",
      "desde",
      "por"
     ],
     "f": "cafe",
     "phrase": "Siga todo recto hasta la esquina.",
     "sens": "Continuez tout droit jusqu'au coin.",
     "n": "<b>hasta</b> = jusqu'à. <b>Siga todo recto</b> = continuez tout droit."
    },
    {
     "q": "La farmacia está justo ___ usted, entre la panadería y correos.",
     "c": [
      "delante de",
      "detrás de",
      "debajo de"
     ],
     "f": "apotheke",
     "r": "baeckerei",
     "phrase": "La farmacia está justo delante de usted, entre la panadería y correos.",
     "sens": "La pharmacie est juste devant vous, entre la boulangerie et la poste.",
     "n": "<b>delante de</b> = devant."
    },
    {
     "q": "Para ir a correos, ___ por delante de la farmacia.",
     "c": [
      "pase",
      "pasa",
      "pasar"
     ],
     "f": "post",
     "r": "apotheke",
     "phrase": "Para ir a correos, pase por delante de la farmacia.",
     "sens": "Pour aller à la poste, passez devant la pharmacie.",
     "n": "Usted → <b>pase</b>. <b>pasar por delante de</b> = passer devant."
    },
    {
     "q": "La furgoneta ___ de la calle lateral.",
     "c": [
      "sale",
      "salga",
      "salir"
     ],
     "f": "lieferwagen",
     "phrase": "La furgoneta sale de la calle lateral.",
     "sens": "La camionnette sort de la rue latérale.",
     "n": "On DÉCRIT ce qu'elle fait → indicatif : <b>sale</b>. <b>salga</b> serait un ordre (usted).",
     "latam": {
      "q": "La camioneta ___ de la calle lateral.",
      "phrase": "La camioneta sale de la calle lateral."
     }
    },
    {
     "q": "No ___ la calle con el semáforo en rojo.",
     "c": [
      "cruce",
      "cruza",
      "cruzar"
     ],
     "f": "ampel-vorne",
     "phrase": "No cruce la calle con el semáforo en rojo.",
     "sens": "Ne traversez pas la rue quand le feu est rouge.",
     "n": "À la forme négative, usted reste au subjonctif : <b>no cruce</b>."
    }
   ]
  },
  "B2": {
   "titre": "Relatives et se",
   "qs": [
    {
     "q": "La cafetería, ___ toldo es rojo, tiene mesas fuera.",
     "c": [
      "cuyo",
      "cuya",
      "que"
     ],
     "f": "cafe",
     "r": "markise",
     "phrase": "La cafetería, cuyo toldo es rojo, tiene mesas fuera.",
     "sens": "Le café, dont le store est rouge, a des tables dehors.",
     "n": "<b>cuyo</b> s'accorde avec ce qui est possédé : el toldo → <b>cuyo</b>."
    },
    {
     "q": "La mujer ___ espera en la parada lleva un abrigo rojo.",
     "c": [
      "que",
      "quien",
      "cuya"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "La mujer que espera en la parada lleva un abrigo rojo.",
     "sens": "La femme qui attend à l'arrêt porte un manteau rouge.",
     "n": "Sujet d'une relative qui précise de quelle femme il s'agit → <b>que</b>."
    },
    {
     "q": "La farmacia a ___ quiere ir Anna está enfrente.",
     "c": [
      "la que",
      "que",
      "quien"
     ],
     "f": "apotheke",
     "r": "anna",
     "phrase": "La farmacia a la que quiere ir Anna está enfrente.",
     "sens": "La pharmacie où Anna veut aller est en face.",
     "n": "Préposition + relatif : a <b>la que</b> (la farmacia)."
    },
    {
     "q": "A lo largo de la acera ___ un carril bici rojo.",
     "c": [
      "hay",
      "está",
      "es"
     ],
     "f": "radweg",
     "r": "buergersteig",
     "phrase": "A lo largo de la acera hay un carril bici rojo.",
     "sens": "Le long du trottoir, il y a une piste cyclable rouge.",
     "n": "Une chose qu'on présente (un carril) → <b>hay</b>.",
     "latam": {
      "q": "A lo largo de la banqueta ___ una ciclovía roja.",
      "c": [
       "hay",
       "está",
       "es"
      ],
      "phrase": "A lo largo de la banqueta hay una ciclovía roja."
     }
    },
    {
     "q": "En la panadería se ___ pan.",
     "c": [
      "vende",
      "venden",
      "vendes"
     ],
     "f": "brot",
     "r": "baeckerei",
     "phrase": "En la panadería se vende pan.",
     "sens": "À la boulangerie, on vend du pain.",
     "n": "Passif avec <b>se</b> : le verbe s'accorde avec ce qui est vendu (el pan, singulier) → <b>se vende</b>."
    },
    {
     "q": "En el quiosco se ___ bebidas.",
     "c": [
      "venden",
      "vende",
      "vendo"
     ],
     "f": "flasche",
     "r": "kiosk",
     "phrase": "En el quiosco se venden bebidas.",
     "sens": "Au kiosque, on vend des boissons.",
     "n": "Pluriel (bebidas) → <b>se venden</b>."
    }
   ]
  },
  "C1": {
   "titre": "Hypothèses et probabilité",
   "qs": [
    {
     "q": "Anna mira el móvil sin saber adónde ir: ___ haberse perdido.",
     "c": [
      "debe de",
      "quiere",
      "suele"
     ],
     "f": "anna",
     "phrase": "Debe de haberse perdido.",
     "sens": "Elle a dû se perdre.",
     "n": "<b>deber de</b> + infinitif = une déduction : c'est probable.",
     "latam": {
      "q": "Anna mira el celular sin saber adónde ir: ___ haberse perdido."
     }
    },
    {
     "q": "La calle está mojada: ___ llovido hace poco.",
     "c": [
      "habrá",
      "habría",
      "hubo"
     ],
     "f": "strasse",
     "phrase": "Habrá llovido hace poco.",
     "sens": "Il a dû pleuvoir il y a peu.",
     "n": "Futur antérieur de probabilité : <b>habrá</b> llovido = il a dû pleuvoir."
    },
    {
     "q": "Si el semáforo estuviera en verde, Anna ya ___ la calle.",
     "c": [
      "habría cruzado",
      "cruzaría",
      "cruzó"
     ],
     "f": "ampel-vorne",
     "r": "anna",
     "phrase": "Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.",
     "sens": "Si le feu était au vert, Anna aurait déjà traversé la rue.",
     "n": "Condition irréelle (estuviera), action déjà faite → conditionnel passé : <b>habría cruzado</b>."
    },
    {
     "q": "Puede que la furgoneta ___ pedidos a la cafetería.",
     "c": [
      "lleve",
      "lleva",
      "llevará"
     ],
     "f": "lieferwagen",
     "r": "cafe",
     "phrase": "Puede que la furgoneta lleve pedidos a la cafetería.",
     "sens": "La camionnette apporte peut-être des commandes au café.",
     "n": "<b>puede que</b> + subjonctif : une possibilité → <b>lleve</b>.",
     "latam": {
      "q": "Puede que la camioneta ___ pedidos a la cafetería.",
      "phrase": "Puede que la camioneta lleve pedidos a la cafetería."
     }
    }
   ]
  }
 },
 "traductions": {
  "en": {
   "champs": {
    "alt": "A Berlin street crossing seen from a first floor: a bakery, a pharmacy, a post office and a café, a bus stop, a tram, a taxi, pedestrians on the crossing, a cyclist on the red lane; in the foreground, Anna looks for her way on her phone, between the kiosk, the postbox and the bikes.",
    "consigne": "Anna is looking for her way in Berlin. Tap a building, a vehicle or a person."
   },
   "couches": {
    "A1": "Nouns and articles",
    "A2": "¿Dónde está? — in town",
    "B1": "Giving directions — the usted imperative",
    "B2": "Relative clauses and se",
    "C1": "Hypotheses and probability"
   },
   "questions": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "<b>entre</b> = between, with no « de »: entre la panadería y la oficina de correos.",
    "A2 | La cafetería está en la esquina.": "On the corner: <b>en la esquina</b>. Location takes <b>estar</b>.",
    "A2 | La panadería está enfrente del quiosco.": "<b>enfrente de</b> = opposite. de + el = <b>del</b>: enfrente <b>del</b> quiosco.",
    "A2 | Delante de la oficina de correos hay un buzón.": "To say what there is, without « the » → <b>hay</b> + un / una.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "<b>en</b> = at, in: where someone is (en la parada).",
    "A2 | El ciclista va por la ciclovía.": "<b>por</b> = along, the way you go: va <b>por</b> el carril bici.",
    "A2 | El ciclista va por el carril bici.": "<b>por</b> = along, the way you go: va <b>por</b> el carril bici.",
    "A2 | Anna está entre el farol y el semáforo.": "<b>entre</b> … <b>y</b> …: between the street lamp and the traffic light.",
    "A2 | Anna está entre la farola y el semáforo.": "<b>entre</b> … <b>y</b> …: between the street lamp and the traffic light.",
    "A2 | Las bicicletas están en el bicicletero.": "Plural → <b>están</b>.",
    "A2 | Las bicicletas están en el aparcabicis.": "Plural → <b>están</b>.",
    "A2 | Los peatones están en el paso peatonal.": "Plural → <b>están</b>. El paso de cebra = the zebra crossing.",
    "A2 | Los peatones están en el paso de cebra.": "Plural → <b>están</b>. El paso de cebra = the zebra crossing.",
    "A2 | El quiosco está en la banqueta.": "La acera = the pavement; la calle = the road, the street.",
    "A2 | El quiosco está en la acera.": "La acera = the pavement; la calle = the road, the street.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "To ask the way: <b>¿Cómo llego a…?</b> (llegar, I).",
    "B1 | Cruce la calle por el paso peatonal.": "<b>usted</b> imperative = present subjunctive: cruzar → <b>cruce</b> (z → c before e).",
    "B1 | Cruce la calle por el paso de cebra.": "<b>usted</b> imperative = present subjunctive: cruzar → <b>cruce</b> (z → c before e).",
    "B1 | Espere hasta que el semáforo se ponga verde.": "Usted → <b>espere</b>. And <b>hasta que</b> + future takes the subjunctive: se ponga.",
    "B1 | Siga todo recto hasta la esquina.": "<b>hasta</b> = as far as. <b>Siga todo recto</b> = go straight on.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "<b>delante de</b> = in front of.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "Usted → <b>pase</b>. <b>pasar por delante de</b> = to go past.",
    "B1 | La camioneta sale de la calle lateral.": "We DESCRIBE what it does → indicative: <b>sale</b>. <b>salga</b> would be an order (usted).",
    "B1 | La furgoneta sale de la calle lateral.": "We DESCRIBE what it does → indicative: <b>sale</b>. <b>salga</b> would be an order (usted).",
    "B1 | No cruce la calle con el semáforo en rojo.": "In the negative, usted stays in the subjunctive: <b>no cruce</b>.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "<b>cuyo</b> agrees with what is owned: el toldo → <b>cuyo</b>.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "Subject of a relative clause saying which woman → <b>que</b>.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "Preposition + relative: a <b>la que</b> (la farmacia).",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "Something introduced (un carril) → <b>hay</b>.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "Something introduced (un carril) → <b>hay</b>.",
    "B2 | En la panadería se vende pan.": "Passive with <b>se</b>: the verb agrees with what is sold (el pan, singular) → <b>se vende</b>.",
    "B2 | En el quiosco se venden bebidas.": "Plural (bebidas) → <b>se venden</b>.",
    "C1 | Debe de haberse perdido.": "<b>deber de</b> + infinitive = a deduction: it's likely.",
    "C1 | Habrá llovido hace poco.": "Future perfect of probability: <b>habrá</b> llovido = it must have rained.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "Unreal condition (estuviera), action already done → conditional perfect: <b>habría cruzado</b>.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjunctive: a possibility → <b>lleve</b>.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjunctive: a possibility → <b>lleve</b>."
   },
   "sens": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "The pharmacy is between the bakery and the post office.",
    "A2 | La cafetería está en la esquina.": "The café is on the corner.",
    "A2 | La panadería está enfrente del quiosco.": "The bakery is opposite the kiosk.",
    "A2 | Delante de la oficina de correos hay un buzón.": "In front of the post office there is a letterbox.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "The woman in the red coat is waiting at the stop.",
    "A2 | El ciclista va por la ciclovía.": "The cyclist is riding on the cycle lane.",
    "A2 | El ciclista va por el carril bici.": "The cyclist is riding on the cycle lane.",
    "A2 | Anna está entre el farol y el semáforo.": "Anna is between the lamppost and the traffic light.",
    "A2 | Anna está entre la farola y el semáforo.": "Anna is between the lamppost and the traffic light.",
    "A2 | Las bicicletas están en el bicicletero.": "The bicycles are at the bike rack.",
    "A2 | Las bicicletas están en el aparcabicis.": "The bicycles are at the bike rack.",
    "A2 | Los peatones están en el paso peatonal.": "The pedestrians are on the zebra crossing.",
    "A2 | Los peatones están en el paso de cebra.": "The pedestrians are on the zebra crossing.",
    "A2 | El quiosco está en la banqueta.": "The kiosk is on the pavement.",
    "A2 | El quiosco está en la acera.": "The kiosk is on the pavement.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "Excuse me, how do I get to the pharmacy?",
    "B1 | Cruce la calle por el paso peatonal.": "Cross the street at the zebra crossing.",
    "B1 | Cruce la calle por el paso de cebra.": "Cross the street at the zebra crossing.",
    "B1 | Espere hasta que el semáforo se ponga verde.": "Wait until the light turns green.",
    "B1 | Siga todo recto hasta la esquina.": "Go straight ahead to the corner.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "The pharmacy is right in front of you, between the bakery and the post office.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "To get to the post office, walk past the pharmacy.",
    "B1 | La camioneta sale de la calle lateral.": "The van is coming out of the side street.",
    "B1 | La furgoneta sale de la calle lateral.": "The van is coming out of the side street.",
    "B1 | No cruce la calle con el semáforo en rojo.": "Don't cross the street when the light is red.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "The café, whose awning is red, has tables outside.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "The woman waiting at the stop is wearing a red coat.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "The pharmacy Anna wants to go to is across the street.",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "Along the pavement there is a red cycle lane.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "Along the pavement there is a red cycle lane.",
    "B2 | En la panadería se vende pan.": "Bread is sold at the bakery.",
    "B2 | En el quiosco se venden bebidas.": "Drinks are sold at the kiosk.",
    "C1 | Debe de haberse perdido.": "She must have got lost.",
    "C1 | Habrá llovido hace poco.": "It probably rained a little while ago.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "If the light were green, Anna would already have crossed the street.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "The van may be bringing orders to the café.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "The van may be bringing orders to the café."
   }
  },
  "tr": {
   "champs": {
    "alt": "Birinci kattan görülen bir Berlin kavşağı: fırın, eczane, postane ve kafe, otobüs durağı, tramvay, taksi, yaya geçidinde yayalar, kırmızı yolda bir bisikletli; önde Anna, büfe, posta kutusu ve bisikletler arasında telefonundan yolunu arıyor.",
    "consigne": "Anna Berlin'de yolunu arıyor. Bir binaya, bir araca ya da bir kişiye dokun."
   },
   "couches": {
    "A1": "İsimler ve artikeller"
   },
   "questions": {},
   "sens": {}
  },
  "uk": {
   "champs": {
    "alt": "Берлінське перехрестя, видно з другого поверху: пекарня, аптека, пошта й кав'ярня, зупинка автобуса, трамвай, таксі, пішоходи на переході, велосипедист на червоній доріжці; на передньому плані Анна шукає дорогу в телефоні, між кіоском, поштовою скринькою та велосипедами.",
    "consigne": "Анна шукає дорогу в Берліні. Торкнись будівлі, транспорту чи людини."
   },
   "couches": {
    "A1": "Іменники й артиклі"
   },
   "questions": {},
   "sens": {}
  },
  "fa": {
   "champs": {
    "alt": "یک چهارراه در برلین از طبقهٔ اول: نانوایی، داروخانه، اداره پست و کافه، ایستگاه اتوبوس، تراموا، تاکسی، عابران روی خط عابر، یک دوچرخه‌سوار روی مسیر قرمز؛ در جلوی تصویر، آنا میان دکه، صندوق پست و دوچرخه‌ها با گوشی‌اش دنبال راهش می‌گردد.",
    "consigne": "آنا در برلین دنبال راهش می‌گردد. یک ساختمان، یک وسیلهٔ نقلیه یا یک آدم را لمس کن."
   },
   "couches": {
    "A1": "اسم‌ها و حرف‌های تعریف"
   },
   "questions": {},
   "sens": {}
  },
  "ar": {
   "champs": {
    "alt": "تقاطع في برلين يُرى من الطابق الأول: مخبز وصيدلية ومكتب بريد ومقهى، وموقف حافلات، وترام، وسيارة أجرة، ومشاة على ممر المشاة، وراكب دراجة على المسار الأحمر؛ وفي المقدمة تبحث آنا عن طريقها في هاتفها، بين الكشك وصندوق البريد والدراجات.",
    "consigne": "آنا تبحث عن طريقها في برلين. المس مبنى أو مركبة أو شخصًا."
   },
   "couches": {
    "A1": "الأسماء وأدوات التعريف",
    "A2": "¿Dónde está? — في المدينة",
    "B1": "وصف الطريق — أمر usted",
    "B2": "الجمل الموصولة وse",
    "C1": "الفرضيات والاحتمال"
   },
   "questions": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "<b>entre</b> = بين، بلا «de»: entre la panadería y la oficina de correos.",
    "A2 | La cafetería está en la esquina.": "في الزاوية: <b>en la esquina</b>. المكان يُقال بـ <b>estar</b>.",
    "A2 | La panadería está enfrente del quiosco.": "<b>enfrente de</b> = مقابل. de + el = <b>del</b>: enfrente <b>del</b> quiosco.",
    "A2 | Delante de la oficina de correos hay un buzón.": "لقول ما يوجد، بلا أداة تعريف ← <b>hay</b> + un / una.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "<b>en</b> = في، عند: مكان الوجود (en la parada).",
    "A2 | El ciclista va por la ciclovía.": "<b>por</b> = على طول، عبر ما يُمَرّ به: va <b>por</b> el carril bici.",
    "A2 | El ciclista va por el carril bici.": "<b>por</b> = على طول، عبر ما يُمَرّ به: va <b>por</b> el carril bici.",
    "A2 | Anna está entre el farol y el semáforo.": "<b>entre</b> … <b>y</b> … = بين … و…: entre la farola y el semáforo.",
    "A2 | Anna está entre la farola y el semáforo.": "<b>entre</b> … <b>y</b> … = بين … و…: entre la farola y el semáforo.",
    "A2 | Las bicicletas están en el bicicletero.": "جمع ← <b>están</b>.",
    "A2 | Las bicicletas están en el aparcabicis.": "جمع ← <b>están</b>.",
    "A2 | Los peatones están en el paso peatonal.": "جمع ← <b>están</b>. El paso de cebra = ممرّ المشاة.",
    "A2 | Los peatones están en el paso de cebra.": "جمع ← <b>están</b>. El paso de cebra = ممرّ المشاة.",
    "A2 | El quiosco está en la banqueta.": "La acera = الرصيف؛ la calle = الشارع، الطريق.",
    "A2 | El quiosco está en la acera.": "La acera = الرصيف؛ la calle = الشارع، الطريق.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "للسؤال عن الطريق: <b>¿Cómo llego a…?</b> (llegar، أنا).",
    "B1 | Cruce la calle por el paso peatonal.": "أمر <b>usted</b> = subjuntivo المضارع: cruzar → <b>cruce</b> (z → c قبل e).",
    "B1 | Cruce la calle por el paso de cebra.": "أمر <b>usted</b> = subjuntivo المضارع: cruzar → <b>cruce</b> (z → c قبل e).",
    "B1 | Espere hasta que el semáforo se ponga verde.": "Usted → <b>espere</b>. و<b>hasta que</b> + مستقبل تأخذ subjuntivo: se ponga.",
    "B1 | Siga todo recto hasta la esquina.": "<b>hasta</b> = حتى. <b>Siga todo recto</b> = واصل مستقيماً.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "<b>delante de</b> = أمام.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "Usted → <b>pase</b>. <b>pasar por delante de</b> = يمرّ أمام.",
    "B1 | La camioneta sale de la calle lateral.": "نحن نَصِف ما تفعله ← indicativo: <b>sale</b>. أما <b>salga</b> فتكون أمراً (usted).",
    "B1 | La furgoneta sale de la calle lateral.": "نحن نَصِف ما تفعله ← indicativo: <b>sale</b>. أما <b>salga</b> فتكون أمراً (usted).",
    "B1 | No cruce la calle con el semáforo en rojo.": "في النفي، يبقى usted في subjuntivo: <b>no cruce</b>.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "<b>cuyo</b> يطابق الشيء المملوك: el toldo → <b>cuyo</b>.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "فاعل جملة موصولة تحدّد أيّ امرأة نقصد ← <b>que</b>.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "حرف جرّ + موصول: a <b>la que</b> (la farmacia).",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "شيء نقدّمه (un carril) → <b>hay</b>.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "شيء نقدّمه (un carril) → <b>hay</b>.",
    "B2 | En la panadería se vende pan.": "المبني للمجهول بـ <b>se</b>: الفعل يطابق ما يُباع (el pan، مفرد) ← <b>se vende</b>.",
    "B2 | En el quiosco se venden bebidas.": "جمع (bebidas) → <b>se venden</b>.",
    "C1 | Debe de haberse perdido.": "<b>deber de</b> + مصدر = استنتاج: هذا محتمل.",
    "C1 | Habrá llovido hace poco.": "المستقبل التامّ للاحتمال: <b>habrá</b> llovido = لا بدّ أنها أمطرت.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "شرط غير واقعي (estuviera)، وفعل تمّ بالفعل ← condicional الماضي: <b>habría cruzado</b>.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjuntivo: احتمال ← <b>lleve</b>.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjuntivo: احتمال ← <b>lleve</b>."
   },
   "sens": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "الصيدلية بين المخبز ومكتب البريد.",
    "A2 | La cafetería está en la esquina.": "المقهى عند الزاوية.",
    "A2 | La panadería está enfrente del quiosco.": "المخبز مقابل الكشك.",
    "A2 | Delante de la oficina de correos hay un buzón.": "أمام مكتب البريد صندوق بريد.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "المرأة ذات المعطف الأحمر تنتظر في المحطّة.",
    "A2 | El ciclista va por la ciclovía.": "راكب الدراجة يسير على مسار الدراجات.",
    "A2 | El ciclista va por el carril bici.": "راكب الدراجة يسير على مسار الدراجات.",
    "A2 | Anna está entre el farol y el semáforo.": "آنا بين عمود الإنارة وإشارة المرور.",
    "A2 | Anna está entre la farola y el semáforo.": "آنا بين عمود الإنارة وإشارة المرور.",
    "A2 | Las bicicletas están en el bicicletero.": "الدراجات في موقف الدراجات.",
    "A2 | Las bicicletas están en el aparcabicis.": "الدراجات في موقف الدراجات.",
    "A2 | Los peatones están en el paso peatonal.": "المشاة على ممرّ المشاة.",
    "A2 | Los peatones están en el paso de cebra.": "المشاة على ممرّ المشاة.",
    "A2 | El quiosco está en la banqueta.": "الكشك على الرصيف.",
    "A2 | El quiosco está en la acera.": "الكشك على الرصيف.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "عفواً، كيف أصل إلى الصيدلية؟",
    "B1 | Cruce la calle por el paso peatonal.": "اعبر الشارع عند ممرّ المشاة.",
    "B1 | Cruce la calle por el paso de cebra.": "اعبر الشارع عند ممرّ المشاة.",
    "B1 | Espere hasta que el semáforo se ponga verde.": "انتظر حتى تصبح الإشارة خضراء.",
    "B1 | Siga todo recto hasta la esquina.": "تابع مستقيماً حتى الزاوية.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "الصيدلية أمامك مباشرة، بين المخبز ومكتب البريد.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "للوصول إلى مكتب البريد، امرّ أمام الصيدلية.",
    "B1 | La camioneta sale de la calle lateral.": "تخرج الشاحنة الصغيرة من الشارع الجانبي.",
    "B1 | La furgoneta sale de la calle lateral.": "تخرج الشاحنة الصغيرة من الشارع الجانبي.",
    "B1 | No cruce la calle con el semáforo en rojo.": "لا تعبر الشارع والإشارة حمراء.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "المقهى ذو المظلّة الحمراء له طاولات في الخارج.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "المرأة التي تنتظر في المحطّة ترتدي معطفاً أحمر.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "الصيدلية التي تريد آنا الذهاب إليها في الجهة المقابلة.",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "على طول الرصيف يوجد مسار أحمر للدراجات.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "على طول الرصيف يوجد مسار أحمر للدراجات.",
    "B2 | En la panadería se vende pan.": "في المخبز يُباع الخبز.",
    "B2 | En el quiosco se venden bebidas.": "في الكشك تُباع المشروبات.",
    "C1 | Debe de haberse perdido.": "لا بدّ أنها ضلّت الطريق.",
    "C1 | Habrá llovido hace poco.": "على الأرجح أمطرت قبل قليل.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "لو كانت الإشارة خضراء، لكانت آنا قد عبرت الشارع.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "ربما تنقل الشاحنة الصغيرة طلبيات إلى المقهى.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "ربما تنقل الشاحنة الصغيرة طلبيات إلى المقهى."
   }
  },
  "pt": {
   "champs": {
    "alt": "Um cruzamento de Berlim visto de um primeiro andar: padaria, farmácia, correio e café, um ponto de ônibus, um bonde, um táxi, pedestres na faixa, um ciclista na ciclovia vermelha; em primeiro plano, Anna procura o caminho no celular, entre a banca, a caixa de correio e as bicicletas.",
    "consigne": "Anna procura o caminho em Berlim. Toque num prédio, num veículo ou numa pessoa."
   },
   "couches": {
    "A1": "Substantivos e artigos",
    "A2": "¿Dónde está? — na cidade",
    "B1": "Indicar o caminho — o imperativo de usted",
    "B2": "Relativas e se",
    "C1": "Hipóteses e probabilidade"
   },
   "questions": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "<b>entre</b> = entre, sem « de »: entre la panadería y la oficina de correos.",
    "A2 | La cafetería está en la esquina.": "Na esquina: <b>en la esquina</b>. O lugar se diz com <b>estar</b>.",
    "A2 | La panadería está enfrente del quiosco.": "<b>enfrente de</b> = em frente a. de + el = <b>del</b>: enfrente <b>del</b> quiosco.",
    "A2 | Delante de la oficina de correos hay un buzón.": "Para dizer o que há, sem artigo definido → <b>hay</b> + un / una.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "<b>en</b> = em, no, na: o lugar onde se está (en la parada).",
    "A2 | El ciclista va por la ciclovía.": "<b>por</b> = ao longo de, por onde se passa: va <b>por</b> el carril bici.",
    "A2 | El ciclista va por el carril bici.": "<b>por</b> = ao longo de, por onde se passa: va <b>por</b> el carril bici.",
    "A2 | Anna está entre el farol y el semáforo.": "<b>entre</b> … <b>y</b> …: entre o poste de luz e o semáforo.",
    "A2 | Anna está entre la farola y el semáforo.": "<b>entre</b> … <b>y</b> …: entre o poste de luz e o semáforo.",
    "A2 | Las bicicletas están en el bicicletero.": "Plural → <b>están</b>.",
    "A2 | Las bicicletas están en el aparcabicis.": "Plural → <b>están</b>.",
    "A2 | Los peatones están en el paso peatonal.": "Plural → <b>están</b>. El paso de cebra = a faixa de pedestres.",
    "A2 | Los peatones están en el paso de cebra.": "Plural → <b>están</b>. El paso de cebra = a faixa de pedestres.",
    "A2 | El quiosco está en la banqueta.": "La acera = a calçada; la calle = a rua.",
    "A2 | El quiosco está en la acera.": "La acera = a calçada; la calle = a rua.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "Para perguntar o caminho: <b>¿Cómo llego a…?</b> (llegar, eu).",
    "B1 | Cruce la calle por el paso peatonal.": "Imperativo de <b>usted</b> = subjuntivo presente: cruzar → <b>cruce</b> (z → c antes de e).",
    "B1 | Cruce la calle por el paso de cebra.": "Imperativo de <b>usted</b> = subjuntivo presente: cruzar → <b>cruce</b> (z → c antes de e).",
    "B1 | Espere hasta que el semáforo se ponga verde.": "Usted → <b>espere</b>. E <b>hasta que</b> + futuro leva o subjuntivo: se ponga.",
    "B1 | Siga todo recto hasta la esquina.": "<b>hasta</b> = até. <b>Siga todo recto</b> = siga reto.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "<b>delante de</b> = na frente de.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "Usted → <b>pase</b>. <b>pasar por delante de</b> = passar na frente de.",
    "B1 | La camioneta sale de la calle lateral.": "DESCREVE-SE o que ela faz → indicativo: <b>sale</b>. <b>salga</b> seria uma ordem (usted).",
    "B1 | La furgoneta sale de la calle lateral.": "DESCREVE-SE o que ela faz → indicativo: <b>sale</b>. <b>salga</b> seria uma ordem (usted).",
    "B1 | No cruce la calle con el semáforo en rojo.": "Na forma negativa, usted continua no subjuntivo: <b>no cruce</b>.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "<b>cuyo</b> concorda com o que é possuído: el toldo → <b>cuyo</b>.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "Sujeito de uma relativa que diz de qual mulher se trata → <b>que</b>.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "Preposição + relativo: a <b>la que</b> (la farmacia).",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "Uma coisa que se apresenta (un carril) → <b>hay</b>.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "Uma coisa que se apresenta (un carril) → <b>hay</b>.",
    "B2 | En la panadería se vende pan.": "Passiva com <b>se</b>: o verbo concorda com o que é vendido (el pan, singular) → <b>se vende</b>.",
    "B2 | En el quiosco se venden bebidas.": "Plural (bebidas) → <b>se venden</b>.",
    "C1 | Debe de haberse perdido.": "<b>deber de</b> + infinitivo = uma dedução: é provável.",
    "C1 | Habrá llovido hace poco.": "Futuro composto de probabilidade: <b>habrá</b> llovido = deve ter chovido.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "Condição irreal (estuviera), ação já feita → condicional composto: <b>habría cruzado</b>.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjuntivo: uma possibilidade → <b>lleve</b>.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "<b>puede que</b> + subjuntivo: uma possibilidade → <b>lleve</b>."
   },
   "sens": {
    "A2 | La farmacia está entre la panadería y la oficina de correos.": "A farmácia fica entre a padaria e os correios.",
    "A2 | La cafetería está en la esquina.": "O café fica na esquina.",
    "A2 | La panadería está enfrente del quiosco.": "A padaria fica em frente ao quiosque.",
    "A2 | Delante de la oficina de correos hay un buzón.": "Em frente aos correios há uma caixa de correio.",
    "A2 | La mujer del abrigo rojo espera en la parada.": "A mulher de casaco vermelho espera no ponto.",
    "A2 | El ciclista va por la ciclovía.": "O ciclista anda na ciclovia.",
    "A2 | El ciclista va por el carril bici.": "O ciclista anda na ciclovia.",
    "A2 | Anna está entre el farol y el semáforo.": "Anna está entre o poste e o semáforo.",
    "A2 | Anna está entre la farola y el semáforo.": "Anna está entre o poste e o semáforo.",
    "A2 | Las bicicletas están en el bicicletero.": "As bicicletas estão no bicicletário.",
    "A2 | Las bicicletas están en el aparcabicis.": "As bicicletas estão no bicicletário.",
    "A2 | Los peatones están en el paso peatonal.": "Os pedestres estão na faixa de pedestres.",
    "A2 | Los peatones están en el paso de cebra.": "Os pedestres estão na faixa de pedestres.",
    "A2 | El quiosco está en la banqueta.": "O quiosque fica na calçada.",
    "A2 | El quiosco está en la acera.": "O quiosque fica na calçada.",
    "B1 | Perdone, ¿cómo llego a la farmacia?": "Com licença, como chego à farmácia?",
    "B1 | Cruce la calle por el paso peatonal.": "Atravesse a rua na faixa de pedestres.",
    "B1 | Cruce la calle por el paso de cebra.": "Atravesse a rua na faixa de pedestres.",
    "B1 | Espere hasta que el semáforo se ponga verde.": "Espere até o semáforo ficar verde.",
    "B1 | Siga todo recto hasta la esquina.": "Siga em frente até a esquina.",
    "B1 | La farmacia está justo delante de usted, entre la panadería y correos.": "A farmácia fica bem na sua frente, entre a padaria e os correios.",
    "B1 | Para ir a correos, pase por delante de la farmacia.": "Para ir aos correios, passe em frente à farmácia.",
    "B1 | La camioneta sale de la calle lateral.": "A van sai da rua lateral.",
    "B1 | La furgoneta sale de la calle lateral.": "A van sai da rua lateral.",
    "B1 | No cruce la calle con el semáforo en rojo.": "Não atravesse a rua com o semáforo vermelho.",
    "B2 | La cafetería, cuyo toldo es rojo, tiene mesas fuera.": "O café, cujo toldo é vermelho, tem mesas do lado de fora.",
    "B2 | La mujer que espera en la parada lleva un abrigo rojo.": "A mulher que espera no ponto usa um casaco vermelho.",
    "B2 | La farmacia a la que quiere ir Anna está enfrente.": "A farmácia aonde Anna quer ir fica em frente.",
    "B2 | A lo largo de la banqueta hay una ciclovía roja.": "Ao longo da calçada há uma ciclovia vermelha.",
    "B2 | A lo largo de la acera hay un carril bici rojo.": "Ao longo da calçada há uma ciclovia vermelha.",
    "B2 | En la panadería se vende pan.": "Na padaria se vende pão.",
    "B2 | En el quiosco se venden bebidas.": "No quiosque se vendem bebidas.",
    "C1 | Debe de haberse perdido.": "Ela deve ter se perdido.",
    "C1 | Habrá llovido hace poco.": "Deve ter chovido há pouco.",
    "C1 | Si el semáforo estuviera en verde, Anna ya habría cruzado la calle.": "Se o semáforo estivesse verde, Anna já teria atravessado a rua.",
    "C1 | Puede que la camioneta lleve pedidos a la cafetería.": "Pode ser que a van leve encomendas para o café.",
    "C1 | Puede que la furgoneta lleve pedidos a la cafetería.": "Pode ser que a van leve encomendas para o café."
   }
  },
  "pl": {
   "champs": {
    "alt": "Skrzyżowanie w Berlinie widziane z pierwszego piętra: piekarnia, apteka, poczta i kawiarnia, przystanek autobusowy, tramwaj, taksówka, piesi na przejściu, rowerzysta na czerwonej ścieżce rowerowej; na pierwszym planie Anna szuka drogi w telefonie, między kioskiem, skrzynką pocztową a rowerami.",
    "consigne": "Anna szuka drogi w Berlinie. Dotknij budynku, pojazdu albo osoby."
   },
   "couches": {
    "A1": "Rzeczowniki i rodzajniki"
   },
   "questions": {},
   "sens": {}
  },
  "ru": {
   "champs": {
    "alt": "Берлинский перекрёсток, вид со второго этажа: булочная, аптека, почта и кафе, автобусная остановка, трамвай, такси, пешеходы на переходе, велосипедист на красной велодорожке; на переднем плане Анна ищет дорогу в телефоне — между киоском, почтовым ящиком и велосипедами.",
    "consigne": "Анна ищет дорогу в Берлине. Нажми на здание, транспорт или человека."
   },
   "couches": {
    "A1": "Существительные и артикли"
   },
   "questions": {},
   "sens": {}
  }
 }
};
