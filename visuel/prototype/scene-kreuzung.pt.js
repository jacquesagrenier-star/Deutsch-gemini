// GENERE par portugais/outils/scenes.py (depuis scene-kreuzung.js) -- ne pas modifier a la main.
window.SCENE = {
 "image": "kreuzung.webp",
 "points": [
  {
   "id": "gebaeude",
   "mot": "edifício",
   "genre": "o",
   "pluriel": "os edifícios",
   "niveau": "A1",
   "personne": null,
   "aussi": [
    {
     "mot": "casa",
     "genre": "a",
     "niveau": "A1",
     "theme": "casa_pt",
     "fr": "maison"
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
   "fr": "bâtiment"
  },
  {
   "id": "strasse",
   "mot": "rua",
   "genre": "a",
   "pluriel": "as ruas",
   "niveau": "A1",
   "theme": "cidade_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "cruzamento",
     "genre": "o",
     "niveau": "A2",
     "theme": "viagens_a2_pt",
     "fr": "carrefour"
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
   "fr": "rue"
  },
  {
   "id": "buergersteig",
   "mot": "passeio",
   "genre": "o",
   "pluriel": "os passeios",
   "niveau": "B1",
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
   "fr": "trottoir"
  },
  {
   "id": "baeckerei",
   "mot": "padaria",
   "genre": "a",
   "pluriel": "as padarias",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "boulangerie"
  },
  {
   "id": "brot",
   "mot": "pão",
   "genre": "o",
   "pluriel": "os pães",
   "niveau": "A1",
   "theme": "comida_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "pretzel",
     "genre": "o",
     "niveau": "A2",
     "fr": "bretzel"
    },
    {
     "mot": "papo-seco",
     "genre": "o",
     "niveau": "A2",
     "fr": "petit pain"
    },
    {
     "mot": "montra",
     "genre": "a",
     "niveau": "A1",
     "theme": "compras_pt",
     "fr": "vitrine"
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
   "fr": "pain"
  },
  {
   "id": "apotheke",
   "mot": "farmácia",
   "genre": "a",
   "pluriel": "as farmácias",
   "niveau": "A1",
   "theme": "corpo_pt",
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
   "fr": "pharmacie"
  },
  {
   "id": "post",
   "mot": "correios",
   "genre": "os",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "poste, courrier"
  },
  {
   "id": "briefkasten-post",
   "mot": "caixa do correio",
   "genre": "a",
   "pluriel": "as caixas do correio",
   "niveau": "B1",
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
   "fr": "boîte aux lettres"
  },
  {
   "id": "cafe",
   "mot": "pastelaria",
   "genre": "a",
   "pluriel": "as pastelarias",
   "niveau": "A1",
   "theme": "cidade_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "mesa",
     "genre": "a",
     "niveau": "A1",
     "theme": "casa_pt",
     "fr": "table"
    },
    {
     "mot": "cadeira",
     "genre": "a",
     "niveau": "A1",
     "theme": "casa_pt",
     "fr": "chaise"
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
   "fr": "café (l'établissement)"
  },
  {
   "id": "markise",
   "mot": "toldo",
   "genre": "o",
   "pluriel": "os toldos",
   "niveau": "A2",
   "theme": "casa_a2_pt_2",
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
   "fr": "store (auvent)"
  },
  {
   "id": "bus",
   "mot": "autocarro",
   "genre": "o",
   "pluriel": "os autocarros",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "bus"
  },
  {
   "id": "wartehaeuschen",
   "mot": "abrigo",
   "genre": "o",
   "pluriel": "os abrigos",
   "niveau": "B1",
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
   "fr": "abribus"
  },
  {
   "id": "haltestelle",
   "mot": "paragem",
   "genre": "a",
   "pluriel": "as paragens",
   "niveau": "A1",
   "theme": "transportes_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "placa",
     "genre": "a",
     "niveau": "A2",
     "theme": "viagens_a2_pt_2",
     "fr": "le panneau"
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
   "fr": "arrêt"
  },
  {
   "id": "frau-rot",
   "mot": "mulher",
   "genre": "a",
   "pluriel": "as mulheres",
   "niveau": "A1",
   "theme": "familia_pt",
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
   "fr": "femme/épouse"
  },
  {
   "id": "auto-dunkel",
   "mot": "carro",
   "genre": "o",
   "pluriel": "os carros",
   "niveau": "A1",
   "theme": "cidade_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "estacionamento",
     "genre": "o",
     "niveau": "A1",
     "theme": "cidade_pt",
     "fr": "place de parking"
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
   "fr": "voiture"
  },
  {
   "id": "auto-silber",
   "mot": "carro",
   "genre": "o",
   "pluriel": "os carros",
   "niveau": "A1",
   "theme": "cidade_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "estacionamento",
     "genre": "o",
     "niveau": "A1",
     "theme": "cidade_pt",
     "fr": "place de parking"
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
   "fr": "voiture"
  },
  {
   "id": "parkuhr",
   "mot": "parquímetro",
   "genre": "o",
   "pluriel": "os parquímetros",
   "niveau": "B1",
   "theme": "viagens_b1_pt",
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
   "fr": "parcmètre"
  },
  {
   "id": "schild-klein",
   "mot": "sinal de trânsito",
   "genre": "o",
   "pluriel": "os sinais de trânsito",
   "niveau": "B1",
   "personne": null,
   "aussi": [
    {
     "mot": "placa",
     "genre": "a",
     "niveau": "A2",
     "theme": "viagens_a2_pt_2",
     "fr": "le panneau"
    }
   ],
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
   "fr": "panneau de signalisation"
  },
  {
   "id": "schild-gross",
   "mot": "sinal de trânsito",
   "genre": "o",
   "pluriel": "os sinais de trânsito",
   "niveau": "B1",
   "personne": null,
   "aussi": [
    {
     "mot": "placa",
     "genre": "a",
     "niveau": "A2",
     "theme": "viagens_a2_pt_2",
     "fr": "le panneau"
    }
   ],
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
   "fr": "panneau de signalisation"
  },
  {
   "id": "ampel-mitte",
   "mot": "semáforo",
   "genre": "o",
   "pluriel": "os semáforos",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "feu de circulation"
  },
  {
   "id": "ampel-seite",
   "mot": "semáforo",
   "genre": "o",
   "pluriel": "os semáforos",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "feu de circulation"
  },
  {
   "id": "lieferwagen",
   "mot": "carrinha",
   "genre": "a",
   "pluriel": "as carrinhas",
   "niveau": "A1",
   "theme": "transportes_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "camião",
     "genre": "o",
     "niveau": "A1",
     "theme": "transportes_pt",
     "fr": "poids lourd, camion"
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
   "fr": "camionnette de livraison"
  },
  {
   "id": "zebrastreifen",
   "mot": "passadeira",
   "genre": "a",
   "pluriel": "as passadeiras",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "passage piéton"
  },
  {
   "id": "zebrastreifen-2",
   "mot": "passadeira",
   "genre": "a",
   "pluriel": "as passadeiras",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "passage piéton"
  },
  {
   "id": "fussgaenger",
   "mot": "peão",
   "genre": "o",
   "pluriel": "os peões",
   "niveau": "A2",
   "theme": "viagens_a2_pt_2",
   "personne": null,
   "aussi": [
    {
     "mot": "homem",
     "genre": "o",
     "niveau": "A1",
     "theme": "familia_pt",
     "fr": "homme/mari"
    },
    {
     "mot": "mochila",
     "genre": "a",
     "niveau": "A1",
     "theme": "roupa_pt",
     "fr": "sac à dos"
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
   "fr": "piéton"
  },
  {
   "id": "frau-tasche",
   "mot": "mulher",
   "genre": "a",
   "pluriel": "as mulheres",
   "niveau": "A1",
   "theme": "familia_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "mala",
     "genre": "a",
     "niveau": "A1",
     "theme": "roupa_pt",
     "fr": "sac"
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
   "fr": "femme/épouse"
  },
  {
   "id": "taxi",
   "mot": "táxi",
   "genre": "o",
   "pluriel": "os táxis",
   "niveau": "A1",
   "theme": "cidade_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "carro",
     "genre": "o",
     "niveau": "A1",
     "theme": "cidade_pt",
     "fr": "voiture"
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
   "fr": "taxi"
  },
  {
   "id": "strassenbahn",
   "mot": "elétrico",
   "genre": "o",
   "pluriel": "os elétricos",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "tramway"
  },
  {
   "id": "motorrad",
   "mot": "mota",
   "genre": "a",
   "pluriel": "as motas",
   "niveau": "A1",
   "theme": "transportes_pt",
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
   "fr": "moto"
  },
  {
   "id": "radweg",
   "mot": "ciclovia",
   "genre": "a",
   "pluriel": "as ciclovias",
   "niveau": "A2",
   "theme": "viagens_a2_pt",
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
   "fr": "piste cyclable"
  },
  {
   "id": "radfahrer",
   "mot": "ciclista",
   "genre": "a",
   "pluriel": "as ciclistas",
   "niveau": "B1",
   "theme": "viagens_b1_pt",
   "personne": null,
   "aussi": [
    {
     "mot": "bicicleta",
     "genre": "a",
     "niveau": "A1",
     "theme": "cidade_pt",
     "fr": "vélo"
    },
    {
     "mot": "casaco",
     "genre": "o",
     "niveau": "A1",
     "theme": "roupa_pt",
     "fr": "veste"
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
   "fr": "cycliste"
  },
  {
   "id": "helm",
   "mot": "capacete",
   "genre": "o",
   "pluriel": "os capacetes",
   "niveau": "A2",
   "theme": "lei_a2_pt",
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
   "fr": "casque"
  },
  {
   "id": "kiosk",
   "mot": "quiosque",
   "genre": "o",
   "pluriel": "os quiosques",
   "niveau": "A2",
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
   "fr": "kiosque"
  },
  {
   "id": "flasche",
   "mot": "garrafa",
   "genre": "a",
   "pluriel": "as garrafas",
   "niveau": "A1",
   "theme": "comida_pt",
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
   "fr": "bouteille"
  },
  {
   "id": "briefkasten",
   "mot": "caixa do correio",
   "genre": "a",
   "pluriel": "as caixas do correio",
   "niveau": "B1",
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
   "fr": "boîte aux lettres"
  },
  {
   "id": "laterne",
   "mot": "candeeiro de rua",
   "genre": "o",
   "pluriel": "os candeeiros de rua",
   "niveau": "A2",
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
   "fr": "réverbère"
  },
  {
   "id": "anna",
   "mot": "mulher",
   "genre": "a",
   "pluriel": "as mulheres",
   "niveau": "A1",
   "theme": "familia_pt",
   "personne": "Anna",
   "aussi": [
    {
     "mot": "telemóvel",
     "genre": "o",
     "niveau": "A1",
     "theme": "casa_pt",
     "fr": "téléphone portable"
    },
    {
     "mot": "casaco",
     "genre": "o",
     "niveau": "A1",
     "theme": "roupa_pt",
     "fr": "veste"
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
   "fr": "femme/épouse"
  },
  {
   "id": "ampel-vorne",
   "mot": "semáforo",
   "genre": "o",
   "pluriel": "os semáforos",
   "niveau": "A1",
   "theme": "cidade_pt",
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
   "fr": "feu de circulation"
  },
  {
   "id": "fahrradstaender",
   "mot": "suporte de bicicletas",
   "genre": "o",
   "pluriel": "os suportes de bicicletas",
   "niveau": "B1",
   "personne": null,
   "aussi": [
    {
     "mot": "bicicleta",
     "genre": "a",
     "niveau": "A1",
     "theme": "cidade_pt",
     "fr": "vélo"
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
   "fr": "support à vélos"
  },
  {
   "id": "haus",
   "mot": "casa",
   "genre": "a",
   "pluriel": "as casas",
   "niveau": "A1",
   "theme": "casa_pt",
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
   "fr": "maison"
  }
 ],
 "grosPlans": [],
 "titre": "No cruzamento",
 "alt": "Un carrefour de Lisbonne vu d'un premier étage : boulangerie, pharmacie, poste et café, un arrêt de bus, un tram, un taxi, des piétons sur le passage, un cycliste sur la piste rouge ; au premier plan, Anna cherche son chemin sur son téléphone, entre le kiosque, la boîte aux lettres et les vélos.",
 "consigne": "Anna cherche son chemin dans Lisbonne. Touche un bâtiment, un véhicule ou une personne.",
 "exclus": [],
 "couches": {
  "A1": {
   "titre": "Noms et articles"
  },
  "A2": {
   "titre": "Onde está? — les prépositions de lieu",
   "qs": [
    {
     "q": "Onde está a padaria?",
     "c": [
      "em frente do quiosque",
      "ao lado do quiosque",
      "atrás do quiosque"
     ],
     "f": "baeckerei",
     "r": "kiosk",
     "phrase": "A padaria está em frente do quiosque.",
     "sens": "La boulangerie est en face du kiosque.",
     "n": "<b>em frente de</b> = en face de. <b>em frente de</b> + o quiosque = <b>em frente do</b> quiosque."
    },
    {
     "q": "Onde está a caixa do correio?",
     "c": [
      "à frente dos correios",
      "à frente da padaria",
      "ao lado do autocarro"
     ],
     "f": "briefkasten-post",
     "r": "post",
     "phrase": "A caixa do correio está à frente dos correios.",
     "sens": "La petite boîte aux lettres est devant la poste.",
     "n": "<b>à frente de</b> = devant. <b>à frente de</b> + os correios = <b>à frente dos</b> correios."
    },
    {
     "q": "Onde está a mulher?",
     "c": [
      "na paragem",
      "à frente da farmácia",
      "na ciclovia"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "A mulher está na paragem.",
     "sens": "La femme au manteau rouge attend à l'arrêt.",
     "n": "<b>em</b> + a = <b>na</b> : na paragem."
    },
    {
     "q": "Onde está o ciclista?",
     "c": [
      "na ciclovia",
      "no passeio",
      "no autocarro"
     ],
     "f": "radfahrer",
     "r": "radweg",
     "phrase": "O ciclista está na ciclovia.",
     "sens": "Le cycliste roule sur la piste cyclable.",
     "n": "<b>em</b> + a = <b>na</b> : na ciclovia."
    },
    {
     "q": "Onde está a Anna?",
     "c": [
      "entre o candeeiro de rua e o semáforo",
      "à frente da padaria",
      "na paragem"
     ],
     "f": "anna",
     "r": "ampel-vorne",
     "phrase": "A Anna está entre o candeeiro de rua e o semáforo.",
     "sens": "Anna est entre le lampadaire et le feu.",
     "n": "<b>entre</b> … <b>e</b> … = entre … et …"
    },
    {
     "q": "Onde estão os suportes de bicicletas?",
     "c": [
      "junto do suporte de bicicletas",
      "na paragem",
      "à frente dos correios"
     ],
     "f": "fahrradstaender",
     "r": null,
     "phrase": "Os suportes de bicicletas estão junto do suporte de bicicletas.",
     "sens": "Les vélos sont au porte-vélos.",
     "n": "<b>junto de</b> = près de, contre. <b>junto de</b> + o suporte de bicicletas = <b>junto do</b> suporte de bicicletas."
    },
    {
     "q": "Onde estão os peões?",
     "c": [
      "na passadeira",
      "na ciclovia",
      "na pastelaria"
     ],
     "f": "fussgaenger",
     "r": "zebrastreifen",
     "phrase": "Os peões estão na passadeira.",
     "sens": "Les piétons sont sur le passage piéton.",
     "n": "<b>em</b> + a = <b>na</b> : na passadeira."
    },
    {
     "q": "Onde está o quiosque?",
     "c": [
      "no passeio",
      "na rua",
      "na padaria"
     ],
     "f": "kiosk",
     "r": "buergersteig",
     "phrase": "O quiosque está no passeio.",
     "sens": "Le kiosque est sur le trottoir.",
     "n": "<b>em</b> + o = <b>no</b> : no passeio."
    }
   ]
  },
  "B1": {
   "titre": "Indiquer le chemin",
   "qs": [
    {
     "q": "Desculpe, como é que ___ à farmácia?",
     "c": [
      "se vai",
      "vai-se",
      "se vá"
     ],
     "f": "anna",
     "r": "apotheke",
     "phrase": "Desculpe, como é que se vai à farmácia?",
     "sens": "Excusez-moi, comment aller à la pharmacie ?",
     "n": "Après <b>como é que</b>, le se devant : <b>se vai</b>."
    },
    {
     "q": "___ a rua, ali na passadeira.",
     "c": [
      "Atravesse",
      "Atravessa-se",
      "Atravesses"
     ],
     "f": "zebrastreifen",
     "r": null,
     "phrase": "Atravesse a rua, ali na passadeira.",
     "sens": "Traversez la rue, là, au passage piéton.",
     "n": "Vouvoiement : <b>atravesse</b> ; le passage piéton = <b>a passadeira</b>."
    },
    {
     "q": "Espere até o semáforo ___ verde.",
     "c": [
      "ficar",
      "fica",
      "fique-se"
     ],
     "f": "ampel-vorne",
     "r": null,
     "phrase": "Espere até o semáforo ficar verde.",
     "sens": "Attendez que le feu passe au vert.",
     "n": "<b>até</b> + infinitif personnel."
    },
    {
     "q": "Depois, a farmácia fica mesmo à ___ frente.",
     "c": [
      "sua",
      "seu",
      "dela"
     ],
     "f": "apotheke",
     "r": "baeckerei",
     "phrase": "Depois, a farmácia fica mesmo à sua frente.",
     "sens": "La pharmacie est alors juste devant vous.",
     "n": "<b>à sua frente</b> = devant vous."
    },
    {
     "q": "___ pela farmácia e já lá está.",
     "c": [
      "Passe",
      "Passa-se",
      "Passas"
     ],
     "f": "post",
     "r": "apotheke",
     "phrase": "Passe pela farmácia e já lá está.",
     "sens": "Passez devant la pharmacie, et vous y êtes.",
     "n": "<b>passar por</b> : passer devant."
    },
    {
     "q": "A carrinha ___ da rua lateral.",
     "c": [
      "sai",
      "sae",
      "saia-se"
     ],
     "f": "lieferwagen",
     "r": null,
     "phrase": "A carrinha sai da rua lateral.",
     "sens": "La camionnette sort de la rue latérale.",
     "n": "<b>sair</b> → <b>sai</b> ; la camionnette = <b>a carrinha</b>."
    },
    {
     "q": "Os peões atravessam ___ passadeira.",
     "c": [
      "na",
      "à",
      "pela de"
     ],
     "f": "fussgaenger",
     "r": "zebrastreifen",
     "phrase": "Os peões atravessam na passadeira.",
     "sens": "Les piétons traversent sur le passage piéton.",
     "n": "Les piétons = <b>os peões</b>, au Portugal."
    },
    {
     "q": "A Anna vai já entrar ___ padaria.",
     "c": [
      "na",
      "à",
      "para a de"
     ],
     "f": "baeckerei",
     "r": "anna",
     "phrase": "A Anna vai já entrar na padaria.",
     "sens": "Anna va tout de suite entrer dans la boulangerie.",
     "n": "<b>entrar em</b> : na padaria."
    },
    {
     "q": "Não atravesse com o sinal ___, por favor!",
     "c": [
      "vermelho",
      "vermelha",
      "encarnado-se"
     ],
     "f": "ampel-vorne",
     "r": null,
     "phrase": "Não atravesse com o sinal vermelho, por favor!",
     "sens": "Ne traversez pas au rouge, s'il vous plaît !",
     "n": "<b>o sinal</b> → <b>vermelho</b>."
    },
    {
     "q": "O café fica na ___, mesmo ao lado da rua lateral.",
     "c": [
      "esquina",
      "canto",
      "curva"
     ],
     "f": "cafe",
     "r": null,
     "phrase": "O café fica na esquina, mesmo ao lado da rua lateral.",
     "sens": "Le café est au coin, juste à côté de la rue latérale.",
     "n": "Le coin de rue : <b>a esquina</b>."
    }
   ]
  },
  "B2": {
   "titre": "De, apesar de et les relatives",
   "qs": [
    {
     "q": "Ao longo ___ passeio há uma ciclovia vermelha.",
     "c": [
      "do",
      "de o",
      "ao"
     ],
     "f": "radweg",
     "r": "buergersteig",
     "phrase": "Ao longo do passeio há uma ciclovia vermelha.",
     "sens": "Le long du trottoir court une piste cyclable rouge.",
     "n": "<b>ao longo de</b> + o = <b>ao longo do</b>."
    },
    {
     "q": "Perto ___ quiosque há um marco do correio amarelo.",
     "c": [
      "do",
      "de o",
      "ao"
     ],
     "f": "briefkasten",
     "r": "kiosk",
     "phrase": "Perto do quiosque há um marco do correio amarelo.",
     "sens": "Non loin du kiosque, il y a une boîte aux lettres jaune.",
     "n": "La boîte aux lettres de rue = <b>o marco do correio</b>."
    },
    {
     "q": "Apesar ___ rua molhada, o ciclista anda depressa.",
     "c": [
      "da",
      "de a",
      "à"
     ],
     "f": "radfahrer",
     "r": null,
     "phrase": "Apesar da rua molhada, o ciclista anda depressa.",
     "sens": "Malgré la rue mouillée, le cycliste roule vite.",
     "n": "<b>apesar de</b> + a = <b>da</b>."
    },
    {
     "q": "A mulher, ___ casaco é vermelho, espera pelo autocarro.",
     "c": [
      "cujo",
      "cuja",
      "que o"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "A mulher, cujo casaco é vermelho, espera pelo autocarro.",
     "sens": "La femme au manteau rouge attend le bus.",
     "n": "<b>cujo</b> + casaco."
    },
    {
     "q": "O homem ___ leva uma mochila atravessa na passadeira.",
     "c": [
      "que",
      "quem",
      "qual"
     ],
     "f": "fussgaenger",
     "r": null,
     "phrase": "O homem que leva uma mochila atravessa na passadeira.",
     "sens": "L'homme qui porte un sac à dos traverse sur le passage piéton.",
     "n": "Sujet : <b>que</b>."
    },
    {
     "q": "O café em frente do ___ há mesas tem um toldo vermelho.",
     "c": [
      "qual",
      "que",
      "quem"
     ],
     "f": "cafe",
     "r": "markise",
     "phrase": "O café em frente do qual há mesas tem um toldo vermelho.",
     "sens": "Le café devant lequel il y a des tables a un store rouge.",
     "n": "<b>em frente do qual</b> ; le store = <b>o toldo</b>."
    }
   ]
  },
  "C1": {
   "titre": "Hypothèses : deve, talvez, dizem que",
   "qs": [
    {
     "q": "Ela ___ ter-se perdido.",
     "c": [
      "deve",
      "pode-se",
      "tem"
     ],
     "f": "anna",
     "r": null,
     "phrase": "Ela deve ter-se perdido.",
     "sens": "Elle s'est sans doute perdue.",
     "n": "Déduction sur le passé : <b>deve ter-se perdido</b>."
    },
    {
     "q": "___ ter chovido há pouco.",
     "c": [
      "Deve",
      "Pode-se",
      "Tem"
     ],
     "f": "strasse",
     "r": null,
     "phrase": "Deve ter chovido há pouco.",
     "sens": "Il a dû pleuvoir tout à l'heure.",
     "n": "<b>deve ter</b> + participe."
    },
    {
     "q": "Se o semáforo ___ verde, a Anna já teria atravessado.",
     "c": [
      "estivesse",
      "estiver",
      "está"
     ],
     "f": "ampel-vorne",
     "r": "anna",
     "phrase": "Se o semáforo estivesse verde, a Anna já teria atravessado.",
     "sens": "Si le feu était vert, Anna aurait déjà traversé la rue.",
     "n": "Irréel : <b>se estivesse</b>."
    },
    {
     "q": "___ estar a trazer mercadoria para o café.",
     "c": [
      "Pode",
      "Deve de",
      "Há"
     ],
     "f": "lieferwagen",
     "r": "cafe",
     "phrase": "Pode estar a trazer mercadoria para o café.",
     "sens": "Il apporte peut-être des marchandises pour le café.",
     "n": "Possibilité : <b>poder</b> + estar a."
    }
   ]
  }
 },
 "traductions": {}
};
