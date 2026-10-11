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
     "en": "the house"
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
     "en": "the crossroads"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     44,
     100,
     42
    ]
   ],
   "fr": "la rue",
   "en": "the street",
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
   "aussi": [
    {
     "mot": "escaparate",
     "genre": "el",
     "niveau": "A1",
     "theme": "las_compras",
     "fr": "la vitrine",
     "en": "the shop window",
     "latam": {
      "mot": "aparador",
      "genre": "el",
      "pluriel": "los aparadores"
     }
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     3.6,
     19,
     19.5,
     11.6
    ]
   ],
   "fr": "la boulangerie",
   "en": "the bakery",
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
     "en": "the pretzel"
    },
    {
     "mot": "escaparate",
     "genre": "el",
     "niveau": "A1",
     "theme": "las_compras",
     "fr": "la vitrine",
     "en": "the shop window",
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
     "en": "the table"
    },
    {
     "mot": "silla",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_casa",
     "fr": "la chaise",
     "en": "the chair"
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
     "en": "the sign"
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
     "en": "the lorry, the truck"
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
     "en": "the man"
    },
    {
     "mot": "mochila",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ropa",
     "fr": "le sac à dos",
     "en": "the backpack"
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
     "en": "the bag"
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
     "en": "the bicycle"
    },
    {
     "mot": "chaqueta",
     "genre": "la",
     "niveau": "A1",
     "theme": "la_ropa",
     "fr": "la veste",
     "en": "the jacket"
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
     "en": "the jacket"
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
     "en": "the bicycle"
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
   "latam": {
    "mot": "bicicletero",
    "genre": "el",
    "pluriel": "los bicicleteros"
   }
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
  }
 },
 "traductions": {
  "en": {
   "champs": {
    "alt": "A Berlin street crossing seen from a first floor: a bakery, a pharmacy, a post office and a café, a bus stop, a tram, a taxi, pedestrians on the crossing, a cyclist on the red lane; in the foreground, Anna looks for her way on her phone, between the kiosk, the postbox and the bikes.",
    "consigne": "Anna is looking for her way in Berlin. Tap a building, a vehicle or a person."
   },
   "couches": {
    "A1": "Nouns and articles"
   },
   "questions": {}
  },
  "tr": {
   "champs": {
    "alt": "Birinci kattan görülen bir Berlin kavşağı: fırın, eczane, postane ve kafe, otobüs durağı, tramvay, taksi, yaya geçidinde yayalar, kırmızı yolda bir bisikletli; önde Anna, büfe, posta kutusu ve bisikletler arasında telefonundan yolunu arıyor.",
    "consigne": "Anna Berlin'de yolunu arıyor. Bir binaya, bir araca ya da bir kişiye dokun."
   },
   "couches": {
    "A1": "İsimler ve artikeller"
   },
   "questions": {}
  },
  "uk": {
   "champs": {
    "alt": "Берлінське перехрестя, видно з другого поверху: пекарня, аптека, пошта й кав'ярня, зупинка автобуса, трамвай, таксі, пішоходи на переході, велосипедист на червоній доріжці; на передньому плані Анна шукає дорогу в телефоні, між кіоском, поштовою скринькою та велосипедами.",
    "consigne": "Анна шукає дорогу в Берліні. Торкнись будівлі, транспорту чи людини."
   },
   "couches": {
    "A1": "Іменники й артиклі"
   },
   "questions": {}
  },
  "fa": {
   "champs": {
    "alt": "یک چهارراه در برلین از طبقهٔ اول: نانوایی، داروخانه، اداره پست و کافه، ایستگاه اتوبوس، تراموا، تاکسی، عابران روی خط عابر، یک دوچرخه‌سوار روی مسیر قرمز؛ در جلوی تصویر، آنا میان دکه، صندوق پست و دوچرخه‌ها با گوشی‌اش دنبال راهش می‌گردد.",
    "consigne": "آنا در برلین دنبال راهش می‌گردد. یک ساختمان، یک وسیلهٔ نقلیه یا یک آدم را لمس کن."
   },
   "couches": {
    "A1": "اسم‌ها و حرف‌های تعریف"
   },
   "questions": {}
  },
  "ar": {
   "champs": {
    "alt": "تقاطع في برلين يُرى من الطابق الأول: مخبز وصيدلية ومكتب بريد ومقهى، وموقف حافلات، وترام، وسيارة أجرة، ومشاة على ممر المشاة، وراكب دراجة على المسار الأحمر؛ وفي المقدمة تبحث آنا عن طريقها في هاتفها، بين الكشك وصندوق البريد والدراجات.",
    "consigne": "آنا تبحث عن طريقها في برلين. المس مبنى أو مركبة أو شخصًا."
   },
   "couches": {
    "A1": "الأسماء وأدوات التعريف"
   },
   "questions": {}
  }
 }
};
