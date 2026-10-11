// GENERE par construire.py -- ne pas modifier a la main.
window.SCENE = {
 "image": "kreuzung.webp",
 "points": [
  {
   "id": "gebaeude",
   "mot": "Gebäude",
   "genre": "das",
   "pluriel": "Gebäude",
   "niveau": "A1",
   "theme": "stadt_gebaeude_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Haus",
     "genre": "das",
     "niveau": "A1",
     "theme": "wohnen_a1",
     "fr": "maison",
     "en": "house",
     "tr": "ev",
     "uk": "будинок",
     "fa": "خانه"
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
   "fr": "bâtiment",
   "en": "building",
   "tr": "bina",
   "uk": "будівля",
   "fa": "ساختمان"
  },
  {
   "id": "strasse",
   "mot": "Straße",
   "genre": "die",
   "pluriel": "Straßen",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Kreuzung",
     "genre": "die",
     "niveau": "B1",
     "theme": "verkehr_b1",
     "fr": "carrefour",
     "en": "intersection",
     "tr": "kavşak",
     "uk": "перехрестя",
     "fa": "چهارراه"
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
   "fr": "rue",
   "en": "street",
   "tr": "sokak",
   "uk": "вулиця",
   "fa": "خیابان"
  },
  {
   "id": "buergersteig",
   "mot": "Bürgersteig",
   "genre": "der",
   "pluriel": "Bürgersteige",
   "niveau": "B1",
   "theme": "stadt_gebaeude_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Gehsteig",
     "genre": "der",
     "niveau": "B1",
     "theme": "verkehr_b1",
     "fr": "trottoir",
     "en": "pavement",
     "tr": "kaldırım",
     "uk": "тротуар (австр.)",
     "fa": "پیاده‌رو (واژهٔ اتریشی)"
    }
   ],
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
   "fr": "trottoir",
   "en": "sidewalk",
   "tr": "kaldırım",
   "uk": "тротуар",
   "fa": "پیاده‌رو"
  },
  {
   "id": "baeckerei",
   "mot": "Bäckerei",
   "genre": "die",
   "pluriel": "Bäckereien",
   "niveau": "A2",
   "theme": "stadt_gebaeude_a2",
   "personne": null,
   "aussi": [
    {
     "mot": "Schaufenster",
     "genre": "das",
     "niveau": "B1",
     "theme": "einkaufen_geld_b1",
     "fr": "vitrine",
     "en": "shop window",
     "tr": "vitrin",
     "uk": "вітрина",
     "fa": "ویترین"
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
   "fr": "boulangerie",
   "en": "bakery",
   "tr": "ekmek fırını",
   "uk": "пекарня",
   "fa": "نانوایی"
  },
  {
   "id": "brot",
   "mot": "Brot",
   "genre": "das",
   "pluriel": "Brote",
   "niveau": "A1",
   "theme": "essen_trinken_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Brezel",
     "genre": "die",
     "niveau": "A2",
     "theme": "essen_trinken_a2",
     "fr": "bretzel",
     "en": "pretzel",
     "tr": "pretzel",
     "uk": "крендель",
     "fa": "نان پرتزل"
    },
    {
     "mot": "Brötchen",
     "genre": "das",
     "niveau": "A2",
     "theme": "essen_trinken_a2",
     "fr": "petit pain",
     "en": "bread roll",
     "tr": "küçük ekmek",
     "uk": "булочка",
     "fa": "نان کوچک"
    },
    {
     "mot": "Schaufenster",
     "genre": "das",
     "niveau": "B1",
     "theme": "einkaufen_geld_b1",
     "fr": "vitrine",
     "en": "shop window",
     "tr": "vitrin",
     "uk": "вітрина",
     "fa": "ویترین"
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
   "fr": "pain",
   "en": "bread",
   "tr": "ekmek",
   "uk": "хліб",
   "fa": "نان"
  },
  {
   "id": "apotheke",
   "mot": "Apotheke",
   "genre": "die",
   "pluriel": "Apotheken",
   "niveau": "A1",
   "theme": "gesundheit_a1",
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
   "fr": "pharmacie",
   "en": "pharmacy",
   "tr": "eczane",
   "uk": "аптека",
   "fa": "داروخانه"
  },
  {
   "id": "post",
   "mot": "Post",
   "genre": "die",
   "pluriel": "—",
   "niveau": "A2",
   "theme": "stadt_gebaeude_a2",
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
   "fr": "poste, courrier",
   "en": "post office, mail",
   "tr": "posta",
   "uk": "пошта",
   "fa": "پست"
  },
  {
   "id": "briefkasten-post",
   "mot": "Briefkasten",
   "genre": "der",
   "pluriel": "Briefkästen",
   "niveau": "B1",
   "theme": "wohnen_b1",
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
   "fr": "boîte aux lettres",
   "en": "mailbox",
   "tr": "posta kutusu",
   "uk": "поштова скринька",
   "fa": "صندوق نامه"
  },
  {
   "id": "cafe",
   "mot": "Café",
   "genre": "das",
   "pluriel": "Cafés",
   "niveau": "A1",
   "theme": "stadt_gebaeude_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Tisch",
     "genre": "der",
     "niveau": "A1",
     "theme": "moebel_haushalt_a1",
     "fr": "table",
     "en": "table",
     "tr": "masa",
     "uk": "стіл",
     "fa": "میز"
    },
    {
     "mot": "Stuhl",
     "genre": "der",
     "niveau": "A1",
     "theme": "moebel_haushalt_a1",
     "fr": "chaise",
     "en": "chair",
     "tr": "sandalye",
     "uk": "стілець",
     "fa": "صندلی"
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
   "fr": "café (l'établissement)",
   "en": "café",
   "tr": "kafe",
   "uk": "кав'ярня",
   "fa": "کافه"
  },
  {
   "id": "markise",
   "mot": "Markise",
   "genre": "die",
   "pluriel": "Markisen",
   "niveau": "B2",
   "theme": "stadt_gebaeude_b2",
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
   "fr": "store (auvent)",
   "en": "awning",
   "tr": "tente",
   "uk": "маркіза",
   "fa": "سایه‌بان"
  },
  {
   "id": "bus",
   "mot": "Bus",
   "genre": "der",
   "pluriel": "Busse",
   "niveau": "A1",
   "theme": "verkehr_a1",
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
   "fr": "bus",
   "en": "bus",
   "tr": "otobüs",
   "uk": "автобус",
   "fa": "اتوبوس"
  },
  {
   "id": "wartehaeuschen",
   "mot": "Wartehäuschen",
   "genre": "das",
   "pluriel": "Wartehäuschen",
   "niveau": "B1",
   "theme": "verkehr_b1",
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
   "fr": "abribus",
   "en": "bus shelter",
   "tr": "otobüs durağı sığınağı",
   "uk": "навіс зупинки",
   "fa": "سایبان ایستگاه"
  },
  {
   "id": "haltestelle",
   "mot": "Haltestelle",
   "genre": "die",
   "pluriel": "Haltestellen",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Schild",
     "genre": "das",
     "niveau": "A2",
     "theme": "moebel_haushalt_a2",
     "fr": "le panneau",
     "en": "sign",
     "tr": "tabela",
     "uk": "табличка, вивіска",
     "fa": "تابلو"
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
   "fr": "arrêt",
   "en": "stop",
   "tr": "durak",
   "uk": "зупинка",
   "fa": "ایستگاه"
  },
  {
   "id": "frau-rot",
   "mot": "Frau",
   "genre": "die",
   "pluriel": "Frauen",
   "niveau": "A1",
   "theme": "familie_a1",
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
   "fr": "femme/épouse",
   "en": "woman, wife",
   "tr": "kadın / eş",
   "uk": "жінка, дружина",
   "fa": "زن، همسر"
  },
  {
   "id": "auto-dunkel",
   "mot": "Auto",
   "genre": "das",
   "pluriel": "Autos",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Parkplatz",
     "genre": "der",
     "niveau": "A2",
     "theme": "verkehr_a2",
     "fr": "place de parking",
     "en": "parking lot",
     "tr": "otopark",
     "uk": "парковка",
     "fa": "جای پارک"
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
   "fr": "voiture",
   "en": "car",
   "tr": "araba",
   "uk": "автомобіль",
   "fa": "خودرو"
  },
  {
   "id": "auto-silber",
   "mot": "Auto",
   "genre": "das",
   "pluriel": "Autos",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Parkplatz",
     "genre": "der",
     "niveau": "A2",
     "theme": "verkehr_a2",
     "fr": "place de parking",
     "en": "parking lot",
     "tr": "otopark",
     "uk": "парковка",
     "fa": "جای پارک"
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
   "fr": "voiture",
   "en": "car",
   "tr": "araba",
   "uk": "автомобіль",
   "fa": "خودرو"
  },
  {
   "id": "parkuhr",
   "mot": "Parkuhr",
   "genre": "die",
   "pluriel": "Parkuhren",
   "niveau": "B1",
   "theme": "verkehr_b1",
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
   "fr": "parcmètre",
   "en": "parking meter",
   "tr": "parkmetre",
   "uk": "паркомат",
   "fa": "پارکومتر"
  },
  {
   "id": "schild-klein",
   "mot": "Verkehrszeichen",
   "genre": "das",
   "pluriel": "Verkehrszeichen",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Schild",
     "genre": "das",
     "niveau": "A2",
     "theme": "moebel_haushalt_a2",
     "fr": "le panneau",
     "en": "sign",
     "tr": "tabela",
     "uk": "табличка, вивіска",
     "fa": "تابلو"
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
   "fr": "panneau de signalisation",
   "en": "road sign",
   "tr": "trafik işareti",
   "uk": "дорожній знак",
   "fa": "تابلوی راهنمایی"
  },
  {
   "id": "schild-gross",
   "mot": "Verkehrszeichen",
   "genre": "das",
   "pluriel": "Verkehrszeichen",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Schild",
     "genre": "das",
     "niveau": "A2",
     "theme": "moebel_haushalt_a2",
     "fr": "le panneau",
     "en": "sign",
     "tr": "tabela",
     "uk": "табличка, вивіска",
     "fa": "تابلو"
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
   "fr": "panneau de signalisation",
   "en": "road sign",
   "tr": "trafik işareti",
   "uk": "дорожній знак",
   "fa": "تابلوی راهنمایی"
  },
  {
   "id": "ampel-mitte",
   "mot": "Ampel",
   "genre": "die",
   "pluriel": "Ampeln",
   "niveau": "A1",
   "theme": "verkehr_a1",
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
   "fr": "feu de circulation",
   "en": "traffic light",
   "tr": "trafik ışığı",
   "uk": "світлофор",
   "fa": "چراغ راهنمایی"
  },
  {
   "id": "ampel-seite",
   "mot": "Ampel",
   "genre": "die",
   "pluriel": "Ampeln",
   "niveau": "A1",
   "theme": "verkehr_a1",
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
   "fr": "feu de circulation",
   "en": "traffic light",
   "tr": "trafik ışığı",
   "uk": "світлофор",
   "fa": "چراغ راهنمایی"
  },
  {
   "id": "lieferwagen",
   "mot": "Lieferwagen",
   "genre": "der",
   "pluriel": "Lieferwagen",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Lkw",
     "genre": "der",
     "niveau": "B1",
     "theme": "verkehr_b1",
     "fr": "poids lourd, camion",
     "en": "lorry, truck",
     "tr": "ağır vasıta",
     "uk": "вантажний автомобіль",
     "fa": "کامیون سنگین"
    },
    {
     "mot": "Laster",
     "genre": "der",
     "niveau": "B1",
     "theme": "verkehr_b1",
     "fr": "camion",
     "en": "lorry, truck",
     "tr": "kamyon",
     "uk": "вантажівка",
     "fa": "کامیون"
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
   "fr": "camionnette de livraison",
   "en": "delivery van",
   "tr": "kamyonet",
   "uk": "фургон",
   "fa": "ون باری"
  },
  {
   "id": "zebrastreifen",
   "mot": "Zebrastreifen",
   "genre": "der",
   "pluriel": "Zebrastreifen",
   "niveau": "A2",
   "theme": "verkehr_a2",
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
   "fr": "passage piéton",
   "en": "zebra crossing",
   "tr": "yaya geçidi",
   "uk": "пішохідний перехід",
   "fa": "خط عابر پیاده"
  },
  {
   "id": "zebrastreifen-2",
   "mot": "Zebrastreifen",
   "genre": "der",
   "pluriel": "Zebrastreifen",
   "niveau": "A2",
   "theme": "verkehr_a2",
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
   "fr": "passage piéton",
   "en": "zebra crossing",
   "tr": "yaya geçidi",
   "uk": "пішохідний перехід",
   "fa": "خط عابر پیاده"
  },
  {
   "id": "fussgaenger",
   "mot": "Fußgänger",
   "genre": "der",
   "pluriel": "Fußgänger",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Mann",
     "genre": "der",
     "niveau": "A1",
     "theme": "familie_a1",
     "fr": "homme/mari",
     "en": "man, husband",
     "tr": "adam / koca",
     "uk": "чоловік",
     "fa": "مرد، شوهر"
    },
    {
     "mot": "Rucksack",
     "genre": "der",
     "niveau": "A1",
     "theme": "reisen_urlaub_a1",
     "fr": "sac à dos",
     "en": "backpack",
     "tr": "sırt çantası",
     "uk": "рюкзак",
     "fa": "کوله‌پشتی"
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
   "fr": "piéton",
   "en": "pedestrian",
   "tr": "yaya",
   "uk": "пішохід",
   "fa": "عابر پیاده"
  },
  {
   "id": "frau-tasche",
   "mot": "Frau",
   "genre": "die",
   "pluriel": "Frauen",
   "niveau": "A1",
   "theme": "familie_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Tasche",
     "genre": "die",
     "niveau": "A1",
     "theme": "einkaufen_geld_a1",
     "fr": "sac",
     "en": "bag",
     "tr": "çanta",
     "uk": "сумка",
     "fa": "کیف"
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
   "fr": "femme/épouse",
   "en": "woman, wife",
   "tr": "kadın / eş",
   "uk": "жінка, дружина",
   "fa": "زن، همسر"
  },
  {
   "id": "taxi",
   "mot": "Taxi",
   "genre": "das",
   "pluriel": "Taxis",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Auto",
     "genre": "das",
     "niveau": "A1",
     "theme": "verkehr_a1",
     "fr": "voiture",
     "en": "car",
     "tr": "araba",
     "uk": "автомобіль",
     "fa": "خودرو"
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
   "fr": "taxi",
   "en": "taxi",
   "tr": "taksi",
   "uk": "таксі",
   "fa": "تاکسی"
  },
  {
   "id": "strassenbahn",
   "mot": "Straßenbahn",
   "genre": "die",
   "pluriel": "Straßenbahnen",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Tram",
     "genre": "die",
     "niveau": "B1",
     "theme": "verkehr_b1",
     "fr": "tramway",
     "en": "tram",
     "tr": "tramvay (kısaltma)",
     "uk": "трамвай (скорочення)",
     "fa": "تراموا (واژهٔ کوتاه)"
    }
   ],
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
   "fr": "tramway",
   "en": "tram",
   "tr": "tramvay",
   "uk": "трамвай",
   "fa": "تراموا"
  },
  {
   "id": "motorrad",
   "mot": "Motorrad",
   "genre": "das",
   "pluriel": "Motorräder",
   "niveau": "B1",
   "theme": "verkehr_b1",
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
   "fr": "moto",
   "en": "motorbike",
   "tr": "motosiklet",
   "uk": "мотоцикл",
   "fa": "موتورسیکلت"
  },
  {
   "id": "radweg",
   "mot": "Radweg",
   "genre": "der",
   "pluriel": "Radwege",
   "niveau": "A2",
   "theme": "verkehr_a2",
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
   "fr": "piste cyclable",
   "en": "cycle lane",
   "tr": "bisiklet yolu",
   "uk": "велодоріжка",
   "fa": "مسیر دوچرخه"
  },
  {
   "id": "radfahrer",
   "mot": "Radfahrer",
   "genre": "der",
   "pluriel": "Radfahrer",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Fahrrad",
     "genre": "das",
     "niveau": "A1",
     "theme": "verkehr_a1",
     "fr": "vélo",
     "en": "bicycle",
     "tr": "bisiklet",
     "uk": "велосипед",
     "fa": "دوچرخه"
    },
    {
     "mot": "Jacke",
     "genre": "die",
     "niveau": "A1",
     "theme": "kleidung_a1",
     "fr": "veste",
     "en": "jacket",
     "tr": "ceket",
     "uk": "куртка",
     "fa": "کاپشن"
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
   "fr": "cycliste",
   "en": "cyclist",
   "tr": "bisikletli",
   "uk": "велосипедист",
   "fa": "دوچرخه‌سوار"
  },
  {
   "id": "helm",
   "mot": "Helm",
   "genre": "der",
   "pluriel": "Helme",
   "niveau": "A2",
   "theme": "verkehr_a2",
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
   "fr": "casque",
   "en": "helmet",
   "tr": "kask",
   "uk": "шолом",
   "fa": "کلاه ایمنی"
  },
  {
   "id": "kiosk",
   "mot": "Kiosk",
   "genre": "der",
   "pluriel": "Kioske",
   "niveau": "A2",
   "theme": "stadt_gebaeude_a2",
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
   "fr": "kiosque",
   "en": "kiosk",
   "tr": "gazete bayii",
   "uk": "кіоск",
   "fa": "دکه"
  },
  {
   "id": "flasche",
   "mot": "Flasche",
   "genre": "die",
   "pluriel": "Flaschen",
   "niveau": "A1",
   "theme": "kueche_kochen_a1",
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
   "fr": "bouteille",
   "en": "bottle",
   "tr": "şişe",
   "uk": "пляшка",
   "fa": "بطری"
  },
  {
   "id": "briefkasten",
   "mot": "Briefkasten",
   "genre": "der",
   "pluriel": "Briefkästen",
   "niveau": "B1",
   "theme": "wohnen_b1",
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
   "fr": "boîte aux lettres",
   "en": "mailbox",
   "tr": "posta kutusu",
   "uk": "поштова скринька",
   "fa": "صندوق نامه"
  },
  {
   "id": "laterne",
   "mot": "Laterne",
   "genre": "die",
   "pluriel": "Laternen",
   "niveau": "A2",
   "theme": "stadt_gebaeude_a2",
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
   "fr": "réverbère",
   "en": "street lamp",
   "tr": "sokak lambası",
   "uk": "ліхтар",
   "fa": "چراغ خیابان"
  },
  {
   "id": "anna",
   "mot": "Frau",
   "genre": "die",
   "pluriel": "Frauen",
   "niveau": "A1",
   "theme": "familie_a1",
   "personne": "Anna",
   "aussi": [
    {
     "mot": "Handy",
     "genre": "das",
     "niveau": "A1",
     "theme": "medien_technologie_a1",
     "fr": "téléphone portable",
     "en": "cell phone",
     "tr": "cep telefonu",
     "uk": "мобільник",
     "fa": "تلفن همراه"
    },
    {
     "mot": "Jacke",
     "genre": "die",
     "niveau": "A1",
     "theme": "kleidung_a1",
     "fr": "veste",
     "en": "jacket",
     "tr": "ceket",
     "uk": "куртка",
     "fa": "کاپشن"
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
   "fr": "femme/épouse",
   "en": "woman, wife",
   "tr": "kadın / eş",
   "uk": "жінка, дружина",
   "fa": "زن، همسر"
  },
  {
   "id": "ampel-vorne",
   "mot": "Ampel",
   "genre": "die",
   "pluriel": "Ampeln",
   "niveau": "A1",
   "theme": "verkehr_a1",
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
   "fr": "feu de circulation",
   "en": "traffic light",
   "tr": "trafik ışığı",
   "uk": "світлофор",
   "fa": "چراغ راهنمایی"
  },
  {
   "id": "fahrradstaender",
   "mot": "Fahrradständer",
   "genre": "der",
   "pluriel": "Fahrradständer",
   "niveau": "B1",
   "theme": "verkehr_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Fahrrad",
     "genre": "das",
     "niveau": "A1",
     "theme": "verkehr_a1",
     "fr": "vélo",
     "en": "bicycle",
     "tr": "bisiklet",
     "uk": "велосипед",
     "fa": "دوچرخه"
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
   "fr": "support à vélos",
   "en": "bike rack",
   "tr": "bisiklet park yeri",
   "uk": "велостоянка",
   "fa": "پایهٔ دوچرخه"
  }
 ],
 "grosPlans": [],
 "titre": "An der Kreuzung",
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
