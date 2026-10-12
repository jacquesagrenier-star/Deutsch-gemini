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
     "fa": "خانه",
     "pt": "casa",
     "ar": "بيت، منزل"
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
   "fa": "ساختمان",
   "pt": "prédio, edifício",
   "ar": "مبنى"
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
     "fa": "چهارراه",
     "pt": "cruzamento",
     "ar": "تقاطع"
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
   "fa": "خیابان",
   "pt": "rua",
   "ar": "شارع"
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
     "fa": "پیاده‌رو (واژهٔ اتریشی)",
     "pt": "calçada (Áustria, sul da Alemanha)",
     "ar": "رصيف المشاة (نمساوية)"
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
   "fa": "پیاده‌رو",
   "pt": "calçada",
   "ar": "رصيف المشاة"
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
     "fa": "ویترین",
     "pt": "vitrine",
     "ar": "واجهة المحلّ"
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
   "fa": "نانوایی",
   "pt": "padaria",
   "ar": "مخبز"
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
     "fa": "نان پرتزل",
     "pt": "pretzel",
     "ar": "بريتزل (خبز معقود)"
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
     "fa": "نان کوچک",
     "pt": "pãozinho",
     "ar": "خبز صغير (كعك)"
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
     "fa": "ویترین",
     "pt": "vitrine",
     "ar": "واجهة المحلّ"
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
   "fa": "نان",
   "pt": "pão",
   "ar": "خبز"
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
   "fa": "داروخانه",
   "pt": "farmácia",
   "ar": "صيدلية"
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
   "fa": "پست",
   "pt": "correio",
   "ar": "بريد، مكتب البريد"
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
   "fa": "صندوق نامه",
   "pt": "caixa de correio",
   "ar": "صندوق البريد"
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
     "fa": "میز",
     "pt": "mesa",
     "ar": "طاولة"
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
     "fa": "صندلی",
     "pt": "cadeira",
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
   "fr": "café (l'établissement)",
   "en": "café",
   "tr": "kafe",
   "uk": "кав'ярня",
   "fa": "کافه",
   "pt": "café (o lugar), cafeteria",
   "ar": "مقهى"
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
   "fa": "سایه‌بان",
   "pt": "toldo",
   "ar": "مظلّة (قماشية)"
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
   "fa": "اتوبوس",
   "pt": "ônibus",
   "ar": "حافلة"
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
   "fa": "سایبان ایستگاه",
   "pt": "abrigo do ponto de ônibus",
   "ar": "مظلّة موقف الحافلة"
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
     "fa": "تابلو",
     "pt": "placa",
     "ar": "لافتة"
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
   "fa": "ایستگاه",
   "pt": "ponto (de ônibus)",
   "ar": "موقف (حافلات)"
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
   "fa": "زن، همسر",
   "pt": "mulher / esposa",
   "ar": "امرأة، زوجة"
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
     "fa": "جای پارک",
     "pt": "estacionamento, vaga",
     "ar": "موقف سيارات"
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
   "fa": "خودرو",
   "pt": "carro",
   "ar": "سيارة"
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
     "fa": "جای پارک",
     "pt": "estacionamento, vaga",
     "ar": "موقف سيارات"
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
   "fa": "خودرو",
   "pt": "carro",
   "ar": "سيارة"
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
   "fa": "پارکومتر",
   "pt": "parquímetro",
   "ar": "عدّاد الوقوف"
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
     "fa": "تابلو",
     "pt": "placa",
     "ar": "لافتة"
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
   "fa": "تابلوی راهنمایی",
   "pt": "placa de trânsito",
   "ar": "إشارة مرور (لافتة)"
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
     "fa": "تابلو",
     "pt": "placa",
     "ar": "لافتة"
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
   "fa": "تابلوی راهنمایی",
   "pt": "placa de trânsito",
   "ar": "إشارة مرور (لافتة)"
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
   "fa": "چراغ راهنمایی",
   "pt": "semáforo, farol",
   "ar": "إشارة مرور"
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
   "fa": "چراغ راهنمایی",
   "pt": "semáforo, farol",
   "ar": "إشارة مرور"
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
     "fa": "کامیون سنگین",
     "pt": "caminhão",
     "ar": "شاحنة (اختصار)"
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
     "fa": "کامیون",
     "pt": "caminhão (coloquial)",
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
   "fr": "camionnette de livraison",
   "en": "delivery van",
   "tr": "kamyonet",
   "uk": "фургон",
   "fa": "ون باری",
   "pt": "furgão, van de entrega",
   "ar": "شاحنة توصيل صغيرة"
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
   "fa": "خط عابر پیاده",
   "pt": "faixa de pedestres",
   "ar": "ممرّ المشاة"
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
   "fa": "خط عابر پیاده",
   "pt": "faixa de pedestres",
   "ar": "ممرّ المشاة"
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
     "fa": "مرد، شوهر",
     "pt": "homem / marido",
     "ar": "رجل، زوج"
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
     "fa": "کوله‌پشتی",
     "pt": "mochila",
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
   "fr": "piéton",
   "en": "pedestrian",
   "tr": "yaya",
   "uk": "пішохід",
   "fa": "عابر پیاده",
   "pt": "pedestre",
   "ar": "راجل، ماشٍ"
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
     "fa": "کیف",
     "pt": "bolsa",
     "ar": "حقيبة"
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
   "fa": "زن، همسر",
   "pt": "mulher / esposa",
   "ar": "امرأة، زوجة"
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
     "fa": "خودرو",
     "pt": "carro",
     "ar": "سيارة"
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
   "fa": "تاکسی",
   "pt": "táxi",
   "ar": "سيارة أجرة"
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
     "fa": "تراموا (واژهٔ کوتاه)",
     "pt": "bonde",
     "ar": "ترام"
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
   "fa": "تراموا",
   "pt": "bonde",
   "ar": "ترام"
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
   "fa": "موتورسیکلت",
   "pt": "moto",
   "ar": "درّاجة نارية"
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
   "fa": "مسیر دوچرخه",
   "pt": "ciclovia",
   "ar": "مسار الدرّاجات"
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
     "fa": "دوچرخه",
     "pt": "bicicleta",
     "ar": "درّاجة"
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
     "fa": "کاپشن",
     "pt": "jaqueta",
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
   "fr": "cycliste",
   "en": "cyclist",
   "tr": "bisikletli",
   "uk": "велосипедист",
   "fa": "دوچرخه‌سوار",
   "pt": "ciclista",
   "ar": "راكب دراجة"
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
   "fa": "کلاه ایمنی",
   "pt": "capacete",
   "ar": "خوذة"
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
   "fa": "دکه",
   "pt": "banca, quiosque",
   "ar": "كشك"
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
   "fa": "بطری",
   "pt": "garrafa",
   "ar": "زجاجة"
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
   "fa": "صندوق نامه",
   "pt": "caixa de correio",
   "ar": "صندوق البريد"
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
   "fa": "چراغ خیابان",
   "pt": "poste de luz",
   "ar": "عمود إنارة"
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
     "fa": "تلفن همراه",
     "pt": "celular",
     "ar": "هاتف محمول"
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
     "fa": "کاپشن",
     "pt": "jaqueta",
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
   "fr": "femme/épouse",
   "en": "woman, wife",
   "tr": "kadın / eş",
   "uk": "жінка, дружина",
   "fa": "زن، همسر",
   "pt": "mulher / esposa",
   "ar": "امرأة، زوجة"
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
   "fa": "چراغ راهنمایی",
   "pt": "semáforo, farol",
   "ar": "إشارة مرور"
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
     "fa": "دوچرخه",
     "pt": "bicicleta",
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
   "fr": "support à vélos",
   "en": "bike rack",
   "tr": "bisiklet park yeri",
   "uk": "велостоянка",
   "fa": "پایهٔ دوچرخه",
   "pt": "bicicletário",
   "ar": "حامل الدرّاجات"
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
  },
  "A2": {
   "titre": "Wo? — en ville",
   "qs": [
    {
     "q": "Wo ist die Apotheke?",
     "c": [
      "zwischen der Bäckerei und der Post",
      "neben dem Café",
      "an der Ecke"
     ],
     "f": "apotheke",
     "r": "post",
     "phrase": "Die Apotheke ist zwischen der Bäckerei und der Post.",
     "n": "<b>zwischen</b> + datif pour les deux : zwischen <b>der</b> Bäckerei und <b>der</b> Post."
    },
    {
     "q": "Wo ist das Café?",
     "c": [
      "an der Ecke",
      "zwischen der Bäckerei und der Apotheke",
      "neben dem Kiosk"
     ],
     "f": "cafe",
     "phrase": "Das Café ist an der Ecke.",
     "n": "Au coin de la rue : <b>an der</b> Ecke (die Ecke, datif)."
    },
    {
     "q": "Wo ist die Bäckerei?",
     "c": [
      "gegenüber dem Kiosk",
      "neben dem Kiosk",
      "hinter dem Kiosk"
     ],
     "f": "baeckerei",
     "r": "kiosk",
     "phrase": "Die Bäckerei ist gegenüber dem Kiosk.",
     "n": "<b>gegenüber</b> = en face de, toujours au datif : gegenüber <b>dem</b> Kiosk."
    },
    {
     "q": "Wo steht der kleine Briefkasten?",
     "c": [
      "vor der Post",
      "vor der Bäckerei",
      "neben dem Bus"
     ],
     "f": "briefkasten-post",
     "r": "post",
     "phrase": "Der kleine Briefkasten steht vor der Post.",
     "n": "<b>vor</b> + datif : die Post → vor <b>der</b> Post."
    },
    {
     "q": "Wo wartet die Frau im roten Mantel?",
     "c": [
      "an der Haltestelle",
      "vor der Apotheke",
      "auf dem Radweg"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "Die Frau im roten Mantel wartet an der Haltestelle.",
     "n": "À l'arrêt : <b>an der</b> Haltestelle. Et <b>im</b> roten Mantel = in dem."
    },
    {
     "q": "Wo fährt der Radfahrer?",
     "c": [
      "auf dem Radweg",
      "auf dem Bürgersteig",
      "im Bus"
     ],
     "f": "radfahrer",
     "r": "radweg",
     "phrase": "Der Radfahrer fährt auf dem Radweg.",
     "n": "<b>auf</b> + datif (Wo?) : der Radweg → auf <b>dem</b> Radweg."
    },
    {
     "q": "Wo steht Anna?",
     "c": [
      "zwischen der Laterne und der Ampel",
      "vor der Bäckerei",
      "an der Haltestelle"
     ],
     "f": "anna",
     "r": "ampel-vorne",
     "phrase": "Anna steht zwischen der Laterne und der Ampel.",
     "n": "<b>zwischen</b> + datif : zwischen <b>der</b> Laterne und <b>der</b> Ampel."
    },
    {
     "q": "Wo stehen die Fahrräder?",
     "c": [
      "am Fahrradständer",
      "an der Haltestelle",
      "vor der Post"
     ],
     "f": "fahrradstaender",
     "phrase": "Die Fahrräder stehen am Fahrradständer.",
     "n": "<b>am</b> = an + dem. Datif : der Fahrradständer → <b>am</b> Fahrradständer."
    },
    {
     "q": "Wo sind die Fußgänger?",
     "c": [
      "auf dem Zebrastreifen",
      "auf dem Radweg",
      "im Café"
     ],
     "f": "fussgaenger",
     "r": "zebrastreifen",
     "phrase": "Die Fußgänger sind auf dem Zebrastreifen.",
     "n": "<b>auf</b> + datif : der Zebrastreifen → auf <b>dem</b> Zebrastreifen."
    },
    {
     "q": "Wo steht der Kiosk?",
     "c": [
      "auf dem Bürgersteig",
      "auf der Straße",
      "in der Bäckerei"
     ],
     "f": "kiosk",
     "r": "buergersteig",
     "phrase": "Der Kiosk steht auf dem Bürgersteig.",
     "n": "<b>auf</b> + datif : der Bürgersteig → auf <b>dem</b> Bürgersteig."
    }
   ]
  },
  "B1": {
   "titre": "Indiquer le chemin",
   "qs": [
    {
     "q": "Anna fragt: „Entschuldigung, wie komme ich ___ Apotheke?“",
     "c": [
      "zur",
      "zum",
      "nach"
     ],
     "f": "anna",
     "r": "apotheke",
     "phrase": "Entschuldigung, wie komme ich zur Apotheke?",
     "n": "Vers un lieu : <b>zu</b> + datif. zu + der = <b>zur</b>. <b>nach</b> ne sert que pour les villes et les pays."
    },
    {
     "q": "„Gehen Sie ___ die Straße, dort am Zebrastreifen.“",
     "c": [
      "über",
      "durch",
      "um"
     ],
     "f": "zebrastreifen",
     "phrase": "Gehen Sie über die Straße, dort am Zebrastreifen.",
     "n": "Traverser : <b>über</b> + accusatif (un mouvement) — über <b>die</b> Straße."
    },
    {
     "q": "„Warten Sie, bis die Ampel grün ___.“",
     "c": [
      "wird",
      "ist",
      "werden"
     ],
     "f": "ampel-vorne",
     "phrase": "Warten Sie, bis die Ampel grün wird.",
     "n": "Devenir : <b>werden</b>. La subordonnée envoie le verbe à la fin : bis die Ampel grün <b>wird</b>."
    },
    {
     "q": "„Die Apotheke ist dann direkt ___ Ihnen, zwischen der Bäckerei und der Post.“",
     "c": [
      "vor",
      "nach",
      "bei"
     ],
     "f": "apotheke",
     "r": "baeckerei",
     "phrase": "Die Apotheke ist dann direkt vor Ihnen.",
     "n": "Devant vous : <b>vor</b> + datif → vor <b>Ihnen</b>."
    },
    {
     "q": "„Und die Post? Gehen Sie ___ Apotheke vorbei, dann sind Sie da.“",
     "c": [
      "an der",
      "an die",
      "bei der"
     ],
     "f": "post",
     "r": "apotheke",
     "phrase": "Gehen Sie an der Apotheke vorbei, dann sind Sie da.",
     "n": "<b>an</b> + datif <b>… vorbei</b> = passer devant : an <b>der</b> Apotheke vorbei."
    },
    {
     "q": "Der Lieferwagen kommt aus ___ Seitenstraße.",
     "c": [
      "der",
      "die",
      "den"
     ],
     "f": "lieferwagen",
     "phrase": "Der Lieferwagen kommt aus der Seitenstraße.",
     "n": "<b>aus</b> est toujours suivi du datif, même pour un mouvement : aus <b>der</b> Seitenstraße."
    },
    {
     "q": "Die Fußgänger gehen über ___ Zebrastreifen.",
     "c": [
      "den",
      "dem",
      "der"
     ],
     "f": "fussgaenger",
     "r": "zebrastreifen",
     "phrase": "Die Fußgänger gehen über den Zebrastreifen.",
     "n": "Ils traversent (Wohin?) → accusatif : über <b>den</b> Zebrastreifen."
    },
    {
     "q": "Gleich geht Anna in ___ Bäckerei.",
     "c": [
      "die",
      "der",
      "das"
     ],
     "f": "baeckerei",
     "r": "anna",
     "phrase": "Gleich geht Anna in die Bäckerei.",
     "n": "Wohin? → accusatif : in <b>die</b> Bäckerei. <b>in der</b> Bäckerei répondrait à Wo?"
    },
    {
     "q": "„___ Sie bitte nicht bei Rot über die Straße!“",
     "c": [
      "Gehen",
      "Geht",
      "Gehst"
     ],
     "f": "ampel-vorne",
     "phrase": "Gehen Sie bitte nicht bei Rot über die Straße!",
     "n": "L'impératif de politesse : le verbe d'abord, puis <b>Sie</b> — <b>Gehen Sie</b>."
    },
    {
     "q": "„Das Café? Das ist an ___ Ecke, gleich neben der Seitenstraße.“",
     "c": [
      "der",
      "die",
      "dem"
     ],
     "f": "cafe",
     "phrase": "Das Café ist an der Ecke, gleich neben der Seitenstraße.",
     "n": "Un état (Wo?) → datif : die Ecke → an <b>der</b> Ecke."
    }
   ]
  },
  "B2": {
   "titre": "Génitif et relatives",
   "qs": [
    {
     "q": "___ des Bürgersteigs verläuft ein roter Radweg.",
     "c": [
      "Entlang",
      "Gegenüber",
      "Trotz"
     ],
     "f": "radweg",
     "r": "buergersteig",
     "phrase": "Entlang des Bürgersteigs verläuft ein roter Radweg.",
     "n": "<b>entlang</b> placé devant le nom prend le génitif : entlang <b>des</b> Bürgersteigs. Placé après, l'accusatif : den Bürgersteig entlang."
    },
    {
     "q": "___ des Kiosks steht ein gelber Briefkasten.",
     "c": [
      "Unweit",
      "Wegen",
      "Während"
     ],
     "f": "briefkasten",
     "r": "kiosk",
     "phrase": "Unweit des Kiosks steht ein gelber Briefkasten.",
     "n": "<b>unweit</b> (non loin de) + génitif : unweit <b>des</b> Kiosks."
    },
    {
     "q": "Trotz ___ nassen Straße fährt der Radfahrer schnell.",
     "c": [
      "der",
      "die",
      "den"
     ],
     "f": "radfahrer",
     "phrase": "Trotz der nassen Straße fährt der Radfahrer schnell.",
     "n": "<b>trotz</b> + génitif : die Straße → trotz <b>der</b> nassen Straße (génitif féminin = der)."
    },
    {
     "q": "Die Frau, ___ Mantel rot ist, wartet auf den Bus.",
     "c": [
      "deren",
      "dessen",
      "die"
     ],
     "f": "frau-rot",
     "r": "haltestelle",
     "phrase": "Die Frau, deren Mantel rot ist, wartet auf den Bus.",
     "n": "Possession, antécédent féminin (die Frau) → <b>deren</b> (dont le manteau)."
    },
    {
     "q": "Der Mann, ___ einen Rucksack trägt, geht über den Zebrastreifen.",
     "c": [
      "der",
      "den",
      "dem"
     ],
     "f": "fussgaenger",
     "phrase": "Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.",
     "n": "Sujet de la relative, masculin → <b>der</b>."
    },
    {
     "q": "Das Café, vor ___ Tische stehen, hat eine rote Markise.",
     "c": [
      "dem",
      "das",
      "den"
     ],
     "f": "cafe",
     "r": "markise",
     "phrase": "Das Café, vor dem Tische stehen, hat eine rote Markise.",
     "n": "<b>vor</b> + relatif, un état (Wo?) → datif : das Café → <b>vor dem</b>."
    }
   ]
  },
  "C1": {
   "titre": "Hypothèses",
   "qs": [
    {
     "q": "Anna schaut ratlos auf ihr Handy: Sie ___ sich verlaufen haben.",
     "c": [
      "dürfte",
      "will",
      "soll"
     ],
     "f": "anna",
     "phrase": "Sie dürfte sich verlaufen haben.",
     "n": "<b>dürfte</b> + infinitif passé = probablement : on le devine à son air."
    },
    {
     "q": "Die Straße ist nass: Es ___ vorhin geregnet haben.",
     "c": [
      "muss",
      "darf",
      "will"
     ],
     "f": "strasse",
     "phrase": "Es muss vorhin geregnet haben.",
     "n": "<b>muss</b> + infinitif passé = presque certain, déduit de ce qu'on voit : la rue mouillée."
    },
    {
     "q": "Wäre die Ampel grün, ___ Anna schon über die Straße gegangen.",
     "c": [
      "wäre",
      "hätte",
      "würde"
     ],
     "f": "ampel-vorne",
     "r": "anna",
     "phrase": "Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.",
     "n": "Irréel du passé avec un verbe de mouvement : <b>sein</b> → <b>wäre</b> … gegangen."
    },
    {
     "q": "Niemand weiß, wohin der Lieferwagen fährt. Er ___ Waren für das Café bringen.",
     "c": [
      "könnte",
      "muss",
      "will"
     ],
     "f": "lieferwagen",
     "r": "cafe",
     "phrase": "Er könnte Waren für das Café bringen.",
     "n": "<b>könnte</b> = c'est possible, sans preuve. <b>muss</b> serait une certitude."
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
    "A2": "Wo? — in town",
    "B1": "Giving directions",
    "B2": "Genitive and relative clauses",
    "C1": "Guesses"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + dative for both: zwischen <b>der</b> Bäckerei und <b>der</b> Post.",
    "A2 | Das Café ist an der Ecke.": "On the corner: <b>an der</b> Ecke (die Ecke, dative).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = opposite, always with the dative: gegenüber <b>dem</b> Kiosk.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + dative: die Post → vor <b>der</b> Post.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "At the stop: <b>an der</b> Haltestelle. And <b>im</b> roten Mantel = in dem.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + dative (Wo?): der Radweg → auf <b>dem</b> Radweg.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + dative: zwischen <b>der</b> Laterne und <b>der</b> Ampel.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = an + dem. Dative: der Fahrradständer → <b>am</b> Fahrradständer.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + dative: der Zebrastreifen → auf <b>dem</b> Zebrastreifen.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + dative: der Bürgersteig → auf <b>dem</b> Bürgersteig.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "Towards a place: <b>zu</b> + dative. zu + der = <b>zur</b>. <b>nach</b> is only for towns and countries.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "Crossing: <b>über</b> + accusative (a movement) — über <b>die</b> Straße.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "To become: <b>werden</b>. The subordinate clause sends the verb to the end: bis die Ampel grün <b>wird</b>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "In front of you: <b>vor</b> + dative → vor <b>Ihnen</b>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<b>an</b> + dative <b>… vorbei</b> = to go past: an <b>der</b> Apotheke vorbei.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> always takes the dative, even for a movement: aus <b>der</b> Seitenstraße.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "They are crossing (Wohin?) → accusative: über <b>den</b> Zebrastreifen.",
    "B1 | Gleich geht Anna in die Bäckerei.": "Wohin? → accusative: in <b>die</b> Bäckerei. <b>in der</b> Bäckerei would answer Wo?",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "The polite imperative: the verb first, then <b>Sie</b> — <b>Gehen Sie</b>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "A position (Wo?) → dative: die Ecke → an <b>der</b> Ecke.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> before the noun takes the genitive: entlang <b>des</b> Bürgersteigs. After it, the accusative: den Bürgersteig entlang.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (not far from) + genitive: unweit <b>des</b> Kiosks.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + genitive: die Straße → trotz <b>der</b> nassen Straße (feminine genitive = der).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "Possession, feminine antecedent (die Frau) → <b>deren</b> (whose coat).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "Subject of the relative clause, masculine → <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + relative pronoun, a position (Wo?) → dative: das Café → <b>vor dem</b>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + past infinitive = probably: you can tell from her face.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + past infinitive = almost certain, deduced from what you see: the wet street.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "Unreal past with a verb of movement: <b>sein</b> → <b>wäre</b> … gegangen.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = it's possible, with no proof. <b>muss</b> would be a certainty."
   }
  },
  "tr": {
   "champs": {
    "alt": "Birinci kattan görülen bir Berlin kavşağı: fırın, eczane, postane ve kafe, otobüs durağı, tramvay, taksi, yaya geçidinde yayalar, kırmızı yolda bir bisikletli; önde Anna, büfe, posta kutusu ve bisikletler arasında telefonundan yolunu arıyor.",
    "consigne": "Anna Berlin'de yolunu arıyor. Bir binaya, bir araca ya da bir kişiye dokun."
   },
   "couches": {
    "A1": "İsimler ve artikeller",
    "A2": "Wo? — şehirde",
    "B1": "Yol tarifi",
    "B2": "Genitiv ve ilgi cümleleri",
    "C1": "Tahminler"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + ikisi için de Dativ: zwischen <b>der</b> Bäckerei und <b>der</b> Post.",
    "A2 | Das Café ist an der Ecke.": "Köşede: <b>an der</b> Ecke (die Ecke, Dativ).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = karşısında, her zaman Dativ: gegenüber <b>dem</b> Kiosk.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + Dativ: die Post → vor <b>der</b> Post.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "Durakta: <b>an der</b> Haltestelle. <b>im</b> roten Mantel = in dem.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + Dativ (Wo?): der Radweg → auf <b>dem</b> Radweg.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + Dativ: zwischen <b>der</b> Laterne und <b>der</b> Ampel.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = an + dem. Dativ: der Fahrradständer → <b>am</b> Fahrradständer.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + Dativ: der Zebrastreifen → auf <b>dem</b> Zebrastreifen.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + Dativ: der Bürgersteig → auf <b>dem</b> Bürgersteig.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "Bir yere doğru: <b>zu</b> + Dativ. zu + der = <b>zur</b>. <b>nach</b> yalnızca şehir ve ülkeler için.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "Karşıya geçmek: <b>über</b> + Akkusativ (bir hareket) — über <b>die</b> Straße.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "Olmak (dönüşmek): <b>werden</b>. Yan cümlede fiil sona gider: bis die Ampel grün <b>wird</b>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "Önünüzde: <b>vor</b> + Dativ → vor <b>Ihnen</b>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<b>an</b> + Dativ <b>… vorbei</b> = önünden geçmek: an <b>der</b> Apotheke vorbei.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> hareket olsa bile her zaman Dativ alır: aus <b>der</b> Seitenstraße.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "Karşıya geçiyorlar (Wohin?) → Akkusativ: über <b>den</b> Zebrastreifen.",
    "B1 | Gleich geht Anna in die Bäckerei.": "Wohin? → Akkusativ: in <b>die</b> Bäckerei. <b>in der</b> Bäckerei, Wo? sorusunun cevabı olurdu.",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "Kibar emir kipi: önce fiil, sonra <b>Sie</b> — <b>Gehen Sie</b>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "Bir durum (Wo?) → Dativ: die Ecke → an <b>der</b> Ecke.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> isimden önce gelirse Genitiv alır: entlang <b>des</b> Bürgersteigs. Sonra gelirse Akkusativ: den Bürgersteig entlang.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (-in yakınında) + Genitiv: unweit <b>des</b> Kiosks.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + Genitiv: die Straße → trotz <b>der</b> nassen Straße (dişil Genitiv = der).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "Sahiplik, dişil öncül (die Frau) → <b>deren</b> (mantosu … olan).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "İlgi cümlesinin öznesi, eril → <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + ilgi zamiri, bir durum (Wo?) → Dativ: das Café → <b>vor dem</b>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + geçmiş mastar = muhtemelen: yüz ifadesinden anlaşılıyor.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + geçmiş mastar = neredeyse kesin, görülenden çıkarılır: ıslak yol.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "Hareket fiiliyle gerçek dışı geçmiş: <b>sein</b> → <b>wäre</b> … gegangen.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = mümkün, kanıt yok. <b>muss</b> kesinlik olurdu."
   }
  },
  "uk": {
   "champs": {
    "alt": "Берлінське перехрестя, видно з другого поверху: пекарня, аптека, пошта й кав'ярня, зупинка автобуса, трамвай, таксі, пішоходи на переході, велосипедист на червоній доріжці; на передньому плані Анна шукає дорогу в телефоні, між кіоском, поштовою скринькою та велосипедами.",
    "consigne": "Анна шукає дорогу в Берліні. Торкнись будівлі, транспорту чи людини."
   },
   "couches": {
    "A1": "Іменники й артиклі",
    "A2": "Wo? — у місті",
    "B1": "Як пояснити дорогу",
    "B2": "Genitiv і підрядні означальні",
    "C1": "Припущення"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + Dativ для обох: zwischen <b>der</b> Bäckerei und <b>der</b> Post.",
    "A2 | Das Café ist an der Ecke.": "На розі: <b>an der</b> Ecke (die Ecke, Dativ).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = навпроти, завжди з Dativ: gegenüber <b>dem</b> Kiosk.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + Dativ: die Post → vor <b>der</b> Post.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "На зупинці: <b>an der</b> Haltestelle. А <b>im</b> roten Mantel = in dem.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + Dativ (Wo?): der Radweg → auf <b>dem</b> Radweg.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + Dativ: zwischen <b>der</b> Laterne und <b>der</b> Ampel.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = an + dem. Dativ: der Fahrradständer → <b>am</b> Fahrradständer.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + Dativ: der Zebrastreifen → auf <b>dem</b> Zebrastreifen.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + Dativ: der Bürgersteig → auf <b>dem</b> Bürgersteig.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "До якогось місця: <b>zu</b> + Dativ. zu + der = <b>zur</b>. <b>nach</b> — лише для міст і країн.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "Переходити: <b>über</b> + Akkusativ (рух) — über <b>die</b> Straße.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "Ставати: <b>werden</b>. У підрядному реченні дієслово йде в кінець: bis die Ampel grün <b>wird</b>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "Перед вами: <b>vor</b> + Dativ → vor <b>Ihnen</b>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<b>an</b> + Dativ <b>… vorbei</b> = проходити повз: an <b>der</b> Apotheke vorbei.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> завжди з Dativ, навіть коли є рух: aus <b>der</b> Seitenstraße.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "Вони переходять (Wohin?) → Akkusativ: über <b>den</b> Zebrastreifen.",
    "B1 | Gleich geht Anna in die Bäckerei.": "Wohin? → Akkusativ: in <b>die</b> Bäckerei. <b>in der</b> Bäckerei відповідало б на Wo?",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "Ввічливий наказовий спосіб: спочатку дієслово, потім <b>Sie</b> — <b>Gehen Sie</b>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "Стан (Wo?) → Dativ: die Ecke → an <b>der</b> Ecke.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> перед іменником — Genitiv: entlang <b>des</b> Bürgersteigs. Після нього — Akkusativ: den Bürgersteig entlang.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (недалеко від) + Genitiv: unweit <b>des</b> Kiosks.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + Genitiv: die Straße → trotz <b>der</b> nassen Straße (Genitiv жіночого роду = der).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "Належність, означуване слово жіночого роду (die Frau) → <b>deren</b> (чиє пальто).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "Підмет підрядного речення, чоловічий рід → <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + відносний займенник, стан (Wo?) → Dativ: das Café → <b>vor dem</b>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + інфінітив минулого = мабуть: це видно з її вигляду.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + інфінітив минулого = майже напевно, висновок з того, що видно: мокра вулиця.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "Нереальне минуле з дієсловом руху: <b>sein</b> → <b>wäre</b> … gegangen.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = можливо, без доказів. <b>muss</b> означало б упевненість."
   }
  },
  "fa": {
   "champs": {
    "alt": "یک چهارراه در برلین از طبقهٔ اول: نانوایی، داروخانه، اداره پست و کافه، ایستگاه اتوبوس، تراموا، تاکسی، عابران روی خط عابر، یک دوچرخه‌سوار روی مسیر قرمز؛ در جلوی تصویر، آنا میان دکه، صندوق پست و دوچرخه‌ها با گوشی‌اش دنبال راهش می‌گردد.",
    "consigne": "آنا در برلین دنبال راهش می‌گردد. یک ساختمان، یک وسیلهٔ نقلیه یا یک آدم را لمس کن."
   },
   "couches": {
    "A1": "اسم‌ها و حرف‌های تعریف",
    "A2": "<span lang=\"de\">Wo?</span> — در شهر",
    "B1": "نشان دادن راه",
    "B2": "Genitiv و جمله‌های موصولی",
    "C1": "حدس‌ها"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + Dativ برای هر دو: <span lang=\"de\">zwischen <b>der</b> Bäckerei und <b>der</b> Post</span>.",
    "A2 | Das Café ist an der Ecke.": "سرِ نبش: <span lang=\"de\"><b>an der</b> Ecke</span> (<span lang=\"de\">die Ecke</span>، Dativ).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = روبه‌روی، همیشه با Dativ: <span lang=\"de\">gegenüber <b>dem</b> Kiosk</span>.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + Dativ: <span lang=\"de\">die Post</span> ← <span lang=\"de\">vor <b>der</b> Post</span>.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "در ایستگاه: <span lang=\"de\"><b>an der</b> Haltestelle</span>. و <span lang=\"de\"><b>im</b> roten Mantel</span> = <span lang=\"de\">in dem</span>.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + Dativ (<span lang=\"de\">Wo?</span>): <span lang=\"de\">der Radweg</span> ← <span lang=\"de\">auf <b>dem</b> Radweg</span>.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + Dativ: <span lang=\"de\">zwischen <b>der</b> Laterne und <b>der</b> Ampel</span>.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = <span lang=\"de\">an + dem</span>. Dativ: <span lang=\"de\">der Fahrradständer</span> ← <span lang=\"de\"><b>am</b> Fahrradständer</span>.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + Dativ: <span lang=\"de\">der Zebrastreifen</span> ← <span lang=\"de\">auf <b>dem</b> Zebrastreifen</span>.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + Dativ: <span lang=\"de\">der Bürgersteig</span> ← <span lang=\"de\">auf <b>dem</b> Bürgersteig</span>.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "به سمتِ یک مکان: <b>zu</b> + Dativ. <span lang=\"de\">zu + der</span> = <b>zur</b>. <b>nach</b> فقط برای شهرها و کشورهاست.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "عبور کردن: <b>über</b> + Akkusativ (حرکت) — <span lang=\"de\">über <b>die</b> Straße</span>.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "شدن: <b>werden</b>. در جملهٔ وابسته فعل به آخر می‌رود: <span lang=\"de\">bis die Ampel grün <b>wird</b></span>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "جلوی شما: <b>vor</b> + Dativ ← <span lang=\"de\">vor <b>Ihnen</b></span>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<span lang=\"de\"><b>an</b></span> + Dativ <span lang=\"de\"><b>… vorbei</b></span> = از جلوی چیزی گذشتن: <span lang=\"de\">an <b>der</b> Apotheke vorbei</span>.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> همیشه Dativ می‌گیرد، حتی با حرکت: <span lang=\"de\">aus <b>der</b> Seitenstraße</span>.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "عبور می‌کنند (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">über <b>den</b> Zebrastreifen</span>.",
    "B1 | Gleich geht Anna in die Bäckerei.": "<span lang=\"de\">Wohin?</span> ← Akkusativ: <span lang=\"de\">in <b>die</b> Bäckerei</span>. <span lang=\"de\"><b>in der</b> Bäckerei</span> پاسخِ <span lang=\"de\">Wo?</span> بود.",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "امرِ مؤدبانه: اول فعل، بعد <b>Sie</b> — <span lang=\"de\"><b>Gehen Sie</b></span>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "یک وضعیت (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">die Ecke</span> ← <span lang=\"de\">an <b>der</b> Ecke</span>.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> پیش از اسم، Genitiv می‌گیرد: <span lang=\"de\">entlang <b>des</b> Bürgersteigs</span>. پس از اسم، Akkusativ: <span lang=\"de\">den Bürgersteig entlang</span>.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (نزدیکِ) + Genitiv: <span lang=\"de\">unweit <b>des</b> Kiosks</span>.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + Genitiv: <span lang=\"de\">die Straße</span> ← <span lang=\"de\">trotz <b>der</b> nassen Straße</span> (Genitivِ مؤنث = <span lang=\"de\">der</span>).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "مالکیت، مرجعِ مؤنث (<span lang=\"de\">die Frau</span>) ← <b>deren</b> (که پالتویش).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "فاعلِ جملهٔ موصولی، مذکر ← <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + ضمیرِ موصولی، یک وضعیت (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">das Café</span> ← <span lang=\"de\"><b>vor dem</b></span>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + مصدرِ گذشته = احتمالاً: از قیافه‌اش پیداست.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + مصدرِ گذشته = تقریباً قطعی، از آنچه می‌بینیم: خیابانِ خیس.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "گذشتهٔ غیرواقعی با فعلِ حرکتی: <b>sein</b> ← <span lang=\"de\"><b>wäre</b> … gegangen</span>.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = ممکن است، بی‌مدرک. <b>muss</b> یعنی قطعیت."
   }
  },
  "ar": {
   "champs": {
    "alt": "تقاطع في برلين يُرى من الطابق الأول: مخبز وصيدلية ومكتب بريد ومقهى، وموقف حافلات، وترام، وسيارة أجرة، ومشاة على ممر المشاة، وراكب دراجة على المسار الأحمر؛ وفي المقدمة تبحث آنا عن طريقها في هاتفها، بين الكشك وصندوق البريد والدراجات.",
    "consigne": "آنا تبحث عن طريقها في برلين. المس مبنى أو مركبة أو شخصًا."
   },
   "couches": {
    "A1": "الأسماء وأدوات التعريف",
    "A2": "<span lang=\"de\">Wo?</span> — في المدينة",
    "B1": "وصف الطريق",
    "B2": "الـGenitiv وجمل الصلة",
    "C1": "الافتراضات"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + Dativ للاثنين: <span lang=\"de\">zwischen <b>der</b> Bäckerei und <b>der</b> Post</span>.",
    "A2 | Das Café ist an der Ecke.": "عند الزاوية: <span lang=\"de\"><b>an der</b> Ecke</span> (<span lang=\"de\">die Ecke</span>، Dativ).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = مقابل، دائمًا مع Dativ: <span lang=\"de\">gegenüber <b>dem</b> Kiosk</span>.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + Dativ: <span lang=\"de\">die Post</span> ← <span lang=\"de\">vor <b>der</b> Post</span>.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "في الموقف: <span lang=\"de\"><b>an der</b> Haltestelle</span>. و<span lang=\"de\"><b>im</b> roten Mantel</span> = <span lang=\"de\">in dem</span>.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + Dativ (<span lang=\"de\">Wo?</span>): <span lang=\"de\">der Radweg</span> ← <span lang=\"de\">auf <b>dem</b> Radweg</span>.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + Dativ: <span lang=\"de\">zwischen <b>der</b> Laterne und <b>der</b> Ampel</span>.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = <span lang=\"de\">an + dem</span>. Dativ: <span lang=\"de\">der Fahrradständer</span> ← <span lang=\"de\"><b>am</b> Fahrradständer</span>.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + Dativ: <span lang=\"de\">der Zebrastreifen</span> ← <span lang=\"de\">auf <b>dem</b> Zebrastreifen</span>.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + Dativ: <span lang=\"de\">der Bürgersteig</span> ← <span lang=\"de\">auf <b>dem</b> Bürgersteig</span>.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "نحو مكان: <b>zu</b> + Dativ. <span lang=\"de\">zu + der</span> = <b>zur</b>. و<b>nach</b> للمدن والبلدان فقط.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "العبور: <b>über</b> + Akkusativ (حركة) — <span lang=\"de\">über <b>die</b> Straße</span>.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "يصبح: <b>werden</b>. في الجملة التابعة يذهب الفعل إلى النهاية: <span lang=\"de\">bis die Ampel grün <b>wird</b></span>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "أمامك: <b>vor</b> + Dativ ← <span lang=\"de\">vor <b>Ihnen</b></span>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<span lang=\"de\"><b>an</b></span> + Dativ <span lang=\"de\"><b>… vorbei</b></span> = المرور بجانب: <span lang=\"de\">an <b>der</b> Apotheke vorbei</span>.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> يأخذ Dativ دائمًا، حتى مع الحركة: <span lang=\"de\">aus <b>der</b> Seitenstraße</span>.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "يعبرون (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">über <b>den</b> Zebrastreifen</span>.",
    "B1 | Gleich geht Anna in die Bäckerei.": "<span lang=\"de\">Wohin?</span> ← Akkusativ: <span lang=\"de\">in <b>die</b> Bäckerei</span>. و<span lang=\"de\"><b>in der</b> Bäckerei</span> تجيب عن <span lang=\"de\">Wo?</span>.",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "صيغة الأمر المهذبة: الفعل أولًا ثم <b>Sie</b> — <span lang=\"de\"><b>Gehen Sie</b></span>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "حالة (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">die Ecke</span> ← <span lang=\"de\">an <b>der</b> Ecke</span>.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> قبل الاسم يأخذ Genitiv: <span lang=\"de\">entlang <b>des</b> Bürgersteigs</span>. وبعده Akkusativ: <span lang=\"de\">den Bürgersteig entlang</span>.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (بالقرب من) + Genitiv: <span lang=\"de\">unweit <b>des</b> Kiosks</span>.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + Genitiv: <span lang=\"de\">die Straße</span> ← <span lang=\"de\">trotz <b>der</b> nassen Straße</span> (Genitiv المؤنث = <span lang=\"de\">der</span>).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "ملكية، والسابق مؤنث (<span lang=\"de\">die Frau</span>) ← <b>deren</b> (التي معطفها).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "فاعل جملة الصلة، مذكر ← <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + ضمير الصلة، حالة (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">das Café</span> ← <span lang=\"de\"><b>vor dem</b></span>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + المصدر الماضي = على الأرجح: يظهر ذلك من ملامحها.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + المصدر الماضي = شبه مؤكد، مستنتج مما نراه: الشارع المبلل.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "الماضي غير الواقعي مع فعل حركة: <b>sein</b> ← <span lang=\"de\"><b>wäre</b> … gegangen</span>.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = ممكن، دون دليل. و<b>muss</b> تعني اليقين."
   }
  },
  "pt": {
   "champs": {
    "alt": "Um cruzamento de Berlim visto de um primeiro andar: padaria, farmácia, correio e café, um ponto de ônibus, um bonde, um táxi, pedestres na faixa, um ciclista na ciclovia vermelha; em primeiro plano, Anna procura o caminho no celular, entre a banca, a caixa de correio e as bicicletas.",
    "consigne": "Anna procura o caminho em Berlim. Toque num prédio, num veículo ou numa pessoa."
   },
   "couches": {
    "A1": "Substantivos e artigos",
    "A2": "Wo? — na cidade",
    "B1": "Indicar o caminho",
    "B2": "Genitiv e relativas",
    "C1": "Hipóteses"
   },
   "questions": {
    "A2 | Die Apotheke ist zwischen der Bäckerei und der Post.": "<b>zwischen</b> + Dativ para os dois: zwischen <b>der</b> Bäckerei und <b>der</b> Post.",
    "A2 | Das Café ist an der Ecke.": "Na esquina: <b>an der</b> Ecke (die Ecke, Dativ).",
    "A2 | Die Bäckerei ist gegenüber dem Kiosk.": "<b>gegenüber</b> = em frente a, sempre com Dativ: gegenüber <b>dem</b> Kiosk.",
    "A2 | Der kleine Briefkasten steht vor der Post.": "<b>vor</b> + Dativ: die Post → vor <b>der</b> Post.",
    "A2 | Die Frau im roten Mantel wartet an der Haltestelle.": "No ponto: <b>an der</b> Haltestelle. E <b>im</b> roten Mantel = in dem.",
    "A2 | Der Radfahrer fährt auf dem Radweg.": "<b>auf</b> + Dativ (Wo?): der Radweg → auf <b>dem</b> Radweg.",
    "A2 | Anna steht zwischen der Laterne und der Ampel.": "<b>zwischen</b> + Dativ: zwischen <b>der</b> Laterne und <b>der</b> Ampel.",
    "A2 | Die Fahrräder stehen am Fahrradständer.": "<b>am</b> = an + dem. Dativ: der Fahrradständer → <b>am</b> Fahrradständer.",
    "A2 | Die Fußgänger sind auf dem Zebrastreifen.": "<b>auf</b> + Dativ: der Zebrastreifen → auf <b>dem</b> Zebrastreifen.",
    "A2 | Der Kiosk steht auf dem Bürgersteig.": "<b>auf</b> + Dativ: der Bürgersteig → auf <b>dem</b> Bürgersteig.",
    "B1 | Entschuldigung, wie komme ich zur Apotheke?": "Em direção a um lugar: <b>zu</b> + Dativ. zu + der = <b>zur</b>. <b>nach</b> só serve para cidades e países.",
    "B1 | Gehen Sie über die Straße, dort am Zebrastreifen.": "Atravessar: <b>über</b> + Akkusativ (um movimento) — über <b>die</b> Straße.",
    "B1 | Warten Sie, bis die Ampel grün wird.": "Tornar-se, ficar: <b>werden</b>. A subordinada manda o verbo para o fim: bis die Ampel grün <b>wird</b>.",
    "B1 | Die Apotheke ist dann direkt vor Ihnen.": "Na sua frente: <b>vor</b> + Dativ → vor <b>Ihnen</b>.",
    "B1 | Gehen Sie an der Apotheke vorbei, dann sind Sie da.": "<b>an</b> + Dativ <b>… vorbei</b> = passar em frente a: an <b>der</b> Apotheke vorbei.",
    "B1 | Der Lieferwagen kommt aus der Seitenstraße.": "<b>aus</b> sempre pede Dativ, mesmo num movimento: aus <b>der</b> Seitenstraße.",
    "B1 | Die Fußgänger gehen über den Zebrastreifen.": "Eles atravessam (Wohin?) → Akkusativ: über <b>den</b> Zebrastreifen.",
    "B1 | Gleich geht Anna in die Bäckerei.": "Wohin? → Akkusativ: in <b>die</b> Bäckerei. <b>in der</b> Bäckerei responderia a Wo?",
    "B1 | Gehen Sie bitte nicht bei Rot über die Straße!": "O imperativo formal: primeiro o verbo, depois <b>Sie</b> — <b>Gehen Sie</b>.",
    "B1 | Das Café ist an der Ecke, gleich neben der Seitenstraße.": "Um estado (Wo?) → Dativ: die Ecke → an <b>der</b> Ecke.",
    "B2 | Entlang des Bürgersteigs verläuft ein roter Radweg.": "<b>entlang</b> antes do substantivo pede o Genitiv: entlang <b>des</b> Bürgersteigs. Depois dele, o Akkusativ: den Bürgersteig entlang.",
    "B2 | Unweit des Kiosks steht ein gelber Briefkasten.": "<b>unweit</b> (não longe de) + Genitiv: unweit <b>des</b> Kiosks.",
    "B2 | Trotz der nassen Straße fährt der Radfahrer schnell.": "<b>trotz</b> + Genitiv: die Straße → trotz <b>der</b> nassen Straße (Genitiv feminino = der).",
    "B2 | Die Frau, deren Mantel rot ist, wartet auf den Bus.": "Posse, antecedente feminino (die Frau) → <b>deren</b> (cujo casaco).",
    "B2 | Der Mann, der einen Rucksack trägt, geht über den Zebrastreifen.": "Sujeito da relativa, masculino → <b>der</b>.",
    "B2 | Das Café, vor dem Tische stehen, hat eine rote Markise.": "<b>vor</b> + relativo, um estado (Wo?) → Dativ: das Café → <b>vor dem</b>.",
    "C1 | Sie dürfte sich verlaufen haben.": "<b>dürfte</b> + infinitivo passado = provavelmente: dá para adivinhar pela cara dela.",
    "C1 | Es muss vorhin geregnet haben.": "<b>muss</b> + infinitivo passado = quase certo, deduzido do que se vê: a rua molhada.",
    "C1 | Wäre die Ampel grün, wäre Anna schon über die Straße gegangen.": "Irreal do passado com um verbo de movimento: <b>sein</b> → <b>wäre</b> … gegangen.",
    "C1 | Er könnte Waren für das Café bringen.": "<b>könnte</b> = é possível, sem prova. <b>muss</b> seria uma certeza."
   }
  }
 }
};
