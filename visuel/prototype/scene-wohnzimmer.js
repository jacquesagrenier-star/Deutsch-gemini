// GENERE par construire.py -- ne pas modifier a la main.
window.SCENE = {
 "image": "wohnzimmer.webp",
 "points": [
  {
   "id": "decke",
   "mot": "Decke",
   "genre": "die",
   "pluriel": "Decken",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     0,
     92,
     15.5
    ]
   ],
   "fr": "couverture",
   "en": "blanket",
   "tr": "battaniye",
   "uk": "ковдра",
   "fa": "پتو",
   "pt": "cobertor",
   "ar": "بطانية",
   "pl": "koc",
   "ru": "одеяло, плед"
  },
  {
   "id": "wand",
   "mot": "Wand",
   "genre": "die",
   "pluriel": "Wände",
   "niveau": "A1",
   "theme": "wohnen_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     15.5,
     92,
     38
    ]
   ],
   "fr": "mur",
   "en": "wall",
   "tr": "duvar",
   "uk": "стіна",
   "fa": "دیوار",
   "pt": "parede",
   "ar": "جدار",
   "pl": "ściana",
   "ru": "стена"
  },
  {
   "id": "boden",
   "mot": "Boden",
   "genre": "der",
   "pluriel": "Böden",
   "niveau": "A2",
   "theme": "natur_a2",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     66,
     92,
     34
    ]
   ],
   "fr": "le sol",
   "en": "ground, floor",
   "tr": "zemin / toprak",
   "uk": "земля, підлога",
   "fa": "زمین، کف",
   "pt": "chão, solo",
   "ar": "أرض، تربة",
   "pl": "ziemia, podłoże",
   "ru": "почва, пол"
  },
  {
   "id": "lampe",
   "mot": "Lampe",
   "genre": "die",
   "pluriel": "Lampen",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Lampenschirm",
     "genre": "der",
     "niveau": "B1",
     "theme": "moebel_haushalt_b1",
     "fr": "abat-jour",
     "en": "lampshade",
     "tr": "lamba şapkası",
     "uk": "абажур",
     "fa": "آباژور",
     "pt": "cúpula (de abajur)",
     "ar": "غطاء المصباح",
     "pl": "abażur",
     "ru": "абажур"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     41.8,
     15.5,
     16.4,
     9.6
    ]
   ],
   "fr": "lampe",
   "en": "lamp",
   "tr": "lamba",
   "uk": "лампа",
   "fa": "چراغ",
   "pt": "luminária",
   "ar": "مصباح",
   "pl": "lampa",
   "ru": "лампа"
  },
  {
   "id": "regenschirm",
   "mot": "Regenschirm",
   "genre": "der",
   "pluriel": "Regenschirme",
   "niveau": "A1",
   "theme": "wetter_a1",
   "personne": null,
   "aussi": [],
   "sur": "lampe",
   "devant": 0,
   "boites": [
    [
     47.2,
     25,
     5.2,
     14.5
    ]
   ],
   "fr": "parapluie",
   "en": "umbrella",
   "tr": "şemsiye",
   "uk": "парасолька",
   "fa": "چتر",
   "pt": "guarda-chuva",
   "ar": "مظلّة",
   "pl": "parasol",
   "ru": "зонт"
  },
  {
   "id": "schrank",
   "mot": "Schrank",
   "genre": "der",
   "pluriel": "Schränke",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     34,
     22,
     21
    ]
   ],
   "fr": "armoire",
   "en": "closet, wardrobe",
   "tr": "dolap",
   "uk": "шафа",
   "fa": "کمد",
   "pt": "armário",
   "ar": "خزانة",
   "pl": "szafa",
   "ru": "шкаф"
  },
  {
   "id": "ball",
   "mot": "Ball",
   "genre": "der",
   "pluriel": "Bälle",
   "niveau": "A1",
   "theme": "sport_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Fußball",
     "genre": "der",
     "niveau": "A1",
     "theme": "sport_a1",
     "fr": "football",
     "en": "soccer",
     "tr": "futbol",
     "uk": "футбол",
     "fa": "فوتبال",
     "pt": "futebol",
     "ar": "كرة القدم",
     "pl": "piłka nożna",
     "ru": "футбол"
    }
   ],
   "sur": "schrank",
   "devant": 0,
   "boites": [
    [
     12.4,
     30.8,
     6.6,
     3.6
    ]
   ],
   "fr": "ballon",
   "en": "ball",
   "tr": "top",
   "uk": "м'яч",
   "fa": "توپ",
   "pt": "bola",
   "ar": "كرة",
   "pl": "piłka",
   "ru": "мяч"
  },
  {
   "id": "bild",
   "mot": "Bild",
   "genre": "das",
   "pluriel": "Bilder",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Gemälde",
     "genre": "das",
     "niveau": "A2",
     "theme": "musik_kunst_a2",
     "fr": "peinture/tableau",
     "en": "painting",
     "tr": "tablo",
     "uk": "картина, полотно",
     "fa": "تابلوی نقاشی",
     "pt": "pintura, quadro",
     "ar": "لوحة زيتية",
     "pl": "obraz (malowany)",
     "ru": "картина (живопись)"
    }
   ],
   "sur": "wand",
   "devant": 0,
   "boites": [
    [
     27.5,
     34.5,
     19.8,
     9.8
    ]
   ],
   "fr": "tableau",
   "en": "picture",
   "tr": "resim",
   "uk": "картина",
   "fa": "تابلو، عکس",
   "pt": "quadro",
   "ar": "صورة، لوحة",
   "pl": "obraz",
   "ru": "картина, изображение"
  },
  {
   "id": "fenster",
   "mot": "Fenster",
   "genre": "das",
   "pluriel": "Fenster",
   "niveau": "A1",
   "theme": "wohnen_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     52.8,
     22,
     27,
     29.5
    ]
   ],
   "fr": "fenêtre",
   "en": "window",
   "tr": "pencere",
   "uk": "вікно",
   "fa": "پنجره",
   "pt": "janela",
   "ar": "نافذة",
   "pl": "okno",
   "ru": "окно"
  },
  {
   "id": "heizkoerper",
   "mot": "Heizkörper",
   "genre": "der",
   "pluriel": "Heizkörper",
   "niveau": "B1",
   "theme": "wohnen_b1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     55.6,
     52.6,
     11.4,
     3.6
    ]
   ],
   "fr": "radiateur",
   "en": "radiator",
   "tr": "kalorifer peteği",
   "uk": "радіатор",
   "fa": "رادیاتور",
   "pt": "aquecedor (radiador)",
   "ar": "مشعاع التدفئة",
   "pl": "grzejnik, kaloryfer",
   "ru": "батарея (отопления)"
  },
  {
   "id": "pflanze",
   "mot": "Pflanze",
   "genre": "die",
   "pluriel": "Pflanzen",
   "niveau": "A1",
   "theme": "natur_a1",
   "personne": null,
   "aussi": [
    {
     "mot": "Lichterkette",
     "genre": "die",
     "niveau": "B1",
     "theme": "moebel_haushalt_b1",
     "fr": "guirlande lumineuse",
     "en": "string of fairy lights",
     "tr": "ışık zinciri",
     "uk": "гірлянда",
     "fa": "ریسهٔ چراغ",
     "pt": "pisca-pisca, cordão de luzes",
     "ar": "سلسلة أضواء",
     "pl": "girlanda świetlna, lampki",
     "ru": "гирлянда"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     62,
     40,
     18,
     23.4
    ]
   ],
   "fr": "la plante",
   "en": "plant",
   "tr": "bitki",
   "uk": "рослина",
   "fa": "گیاه",
   "pt": "planta",
   "ar": "نبات",
   "pl": "roślina",
   "ru": "растение"
  },
  {
   "id": "stehlampe",
   "mot": "Stehlampe",
   "genre": "die",
   "pluriel": "Stehlampen",
   "niveau": "A2",
   "theme": "moebel_haushalt_a2",
   "personne": null,
   "aussi": [
    {
     "mot": "Lampe",
     "genre": "die",
     "niveau": "A1",
     "theme": "moebel_haushalt_a1",
     "fr": "lampe",
     "en": "lamp",
     "tr": "lamba",
     "uk": "лампа",
     "fa": "چراغ",
     "pt": "luminária",
     "ar": "مصباح",
     "pl": "lampa",
     "ru": "лампа"
    },
    {
     "mot": "Lampenschirm",
     "genre": "der",
     "niveau": "B1",
     "theme": "moebel_haushalt_b1",
     "fr": "abat-jour",
     "en": "lampshade",
     "tr": "lamba şapkası",
     "uk": "абажур",
     "fa": "آباژور",
     "pt": "cúpula (de abajur)",
     "ar": "غطاء المصباح",
     "pl": "abażur",
     "ru": "абажур"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     77,
     40.6,
     7.6,
     24
    ]
   ],
   "fr": "lampadaire",
   "en": "floor lamp",
   "tr": "ayaklı lamba",
   "uk": "торшер",
   "fa": "چراغ پایه‌بلند",
   "pt": "luminária de chão",
   "ar": "مصباح أرضي",
   "pl": "lampa stojąca",
   "ru": "торшер"
  },
  {
   "id": "socke",
   "mot": "Socke",
   "genre": "die",
   "pluriel": "Socken",
   "niveau": "A1",
   "theme": "kleidung_a1",
   "personne": null,
   "aussi": [],
   "sur": "stehlampe",
   "devant": 0,
   "boites": [
    [
     79.4,
     40.6,
     4.2,
     4.9
    ]
   ],
   "fr": "chaussette",
   "en": "sock",
   "tr": "çorap",
   "uk": "шкарпетка",
   "fa": "جوراب",
   "pt": "meia",
   "ar": "جورب",
   "pl": "skarpetka",
   "ru": "носок"
  },
  {
   "id": "regal",
   "mot": "Regal",
   "genre": "das",
   "pluriel": "Regale",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     86,
     43,
     7.6,
     26
    ]
   ],
   "fr": "étagère",
   "en": "shelf",
   "tr": "raf",
   "uk": "полиця",
   "fa": "قفسه",
   "pt": "estante",
   "ar": "رفّ",
   "pl": "regał, półka",
   "ru": "полка, стеллаж"
  },
  {
   "id": "goldfisch",
   "mot": "Goldfisch",
   "genre": "der",
   "pluriel": "Goldfische",
   "niveau": "A2",
   "theme": "tiere_a2",
   "personne": null,
   "aussi": [
    {
     "mot": "Fisch",
     "genre": "der",
     "niveau": "A1",
     "theme": "tiere_a1",
     "fr": "poisson",
     "en": "fish",
     "tr": "balık",
     "uk": "риба",
     "fa": "ماهی",
     "pt": "peixe",
     "ar": "سمكة",
     "pl": "ryba",
     "ru": "рыба"
    }
   ],
   "sur": "regal",
   "devant": 0,
   "boites": [
    [
     88.2,
     39.4,
     5,
     3.6
    ]
   ],
   "fr": "poisson rouge",
   "en": "goldfish",
   "tr": "japon balığı",
   "uk": "золота рибка",
   "fa": "ماهی قرمز",
   "pt": "peixinho dourado",
   "ar": "سمكة ذهبية",
   "pl": "złota rybka",
   "ru": "золотая рыбка"
  },
  {
   "id": "fahrrad",
   "mot": "Fahrrad",
   "genre": "das",
   "pluriel": "Fahrräder",
   "niveau": "A1",
   "theme": "verkehr_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 1,
   "boites": [
    [
     75,
     53.4,
     17.6,
     17.2
    ]
   ],
   "fr": "vélo",
   "en": "bicycle",
   "tr": "bisiklet",
   "uk": "велосипед",
   "fa": "دوچرخه",
   "pt": "bicicleta",
   "ar": "درّاجة",
   "pl": "rower",
   "ru": "велосипед"
  },
  {
   "id": "tuer",
   "mot": "Tür",
   "genre": "die",
   "pluriel": "Türen",
   "niveau": "A1",
   "theme": "wohnen_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     92.3,
     10.8,
     7.7,
     89.2
    ]
   ],
   "fr": "porte",
   "en": "door",
   "tr": "kapı",
   "uk": "двері",
   "fa": "در",
   "pt": "porta",
   "ar": "باب",
   "pl": "drzwi",
   "ru": "дверь"
  },
  {
   "id": "sofa",
   "mot": "Sofa",
   "genre": "das",
   "pluriel": "Sofas",
   "niveau": "A1",
   "theme": "moebel_haushalt_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     10.8,
     53.2,
     56.6,
     15
    ]
   ],
   "fr": "canapé",
   "en": "sofa",
   "tr": "kanepe",
   "uk": "диван",
   "fa": "مبل",
   "pt": "sofá",
   "ar": "أريكة، كنبة",
   "pl": "kanapa",
   "ru": "диван"
  },
  {
   "id": "buch",
   "mot": "Buch",
   "genre": "das",
   "pluriel": "Bücher",
   "niveau": "A1",
   "theme": "schule_a1",
   "personne": null,
   "aussi": [],
   "sur": "sofa",
   "devant": 0,
   "boites": [
    [
     41.6,
     58.4,
     11.4,
     2.6
    ]
   ],
   "fr": "livre",
   "en": "book",
   "tr": "kitap",
   "uk": "книжка",
   "fa": "کتاب",
   "pt": "livro",
   "ar": "كتاب",
   "pl": "książka",
   "ru": "книга"
  },
  {
   "id": "gitarre",
   "mot": "Gitarre",
   "genre": "die",
   "pluriel": "Gitarren",
   "niveau": "A1",
   "theme": "musik_kunst_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     22.2,
     47.6,
     4.6,
     5.8
    ]
   ],
   "fr": "guitare",
   "en": "guitar",
   "tr": "gitar",
   "uk": "гітара",
   "fa": "گیتار",
   "pt": "violão, guitarra",
   "ar": "غيتار",
   "pl": "gitara",
   "ru": "гитара"
  },
  {
   "id": "turnschuh",
   "mot": "Turnschuh",
   "genre": "der",
   "pluriel": "Turnschuhe",
   "niveau": "A2",
   "theme": "kleidung_a2",
   "personne": null,
   "aussi": [
    {
     "mot": "Schuh",
     "genre": "der",
     "niveau": "A1",
     "theme": "kleidung_a1",
     "fr": "chaussure",
     "en": "shoe",
     "tr": "ayakkabı",
     "uk": "черевик",
     "fa": "کفش",
     "pt": "sapato",
     "ar": "حذاء",
     "pl": "but",
     "ru": "ботинок, туфля"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     20.6,
     66.2,
     13.2,
     3.2
    ]
   ],
   "fr": "basket",
   "en": "trainer",
   "tr": "spor ayakkabı",
   "uk": "кросівка",
   "fa": "کفش ورزشی",
   "pt": "tênis (calçado)",
   "ar": "حذاء رياضي",
   "pl": "trampek, but sportowy",
   "ru": "кроссовки, кеды"
  },
  {
   "id": "fernseher",
   "mot": "Fernseher",
   "genre": "der",
   "pluriel": "Fernseher",
   "niveau": "A1",
   "theme": "medien_technologie_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     55.2,
     10.6,
     14.8
    ]
   ],
   "fr": "télévision",
   "en": "television",
   "tr": "televizyon",
   "uk": "телевізор",
   "fa": "تلویزیون",
   "pt": "televisão, TV",
   "ar": "تلفاز",
   "pl": "telewizor",
   "ru": "телевизор"
  },
  {
   "id": "pizza",
   "mot": "Pizza",
   "genre": "die",
   "pluriel": "Pizzen",
   "niveau": "B1",
   "theme": "essen_trinken_b1",
   "personne": null,
   "aussi": [
    {
     "mot": "Teller",
     "genre": "der",
     "niveau": "A1",
     "theme": "kueche_kochen_a1",
     "fr": "assiette",
     "en": "plate",
     "tr": "tabak",
     "uk": "тарілка",
     "fa": "بشقاب",
     "pt": "prato",
     "ar": "صحن",
     "pl": "talerz",
     "ru": "тарелка"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     7.2,
     69.2,
     12,
     2.2
    ]
   ],
   "fr": "pizza",
   "en": "pizza",
   "tr": "pizza",
   "uk": "піца",
   "fa": "پیتزا",
   "pt": "pizza",
   "ar": "بيتزا",
   "pl": "pizza",
   "ru": "пицца"
  },
  {
   "id": "couchtisch",
   "mot": "Couchtisch",
   "genre": "der",
   "pluriel": "Couchtische",
   "niveau": "A2",
   "theme": "moebel_haushalt_a2",
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
     "ar": "طاولة",
     "pl": "stół",
     "ru": "стол"
    }
   ],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     32.4,
     69.2,
     42.6,
     12.4
    ]
   ],
   "fr": "table basse",
   "en": "coffee table",
   "tr": "orta sehpa",
   "uk": "журнальний столик",
   "fa": "میز جلومبلی",
   "pt": "mesa de centro",
   "ar": "طاولة القهوة",
   "pl": "stolik kawowy, ława",
   "ru": "журнальный столик"
  },
  {
   "id": "tasse",
   "mot": "Tasse",
   "genre": "die",
   "pluriel": "Tassen",
   "niveau": "A1",
   "theme": "kueche_kochen_a1",
   "personne": null,
   "aussi": [],
   "sur": "couchtisch",
   "devant": 0,
   "boites": [
    [
     34.8,
     69.4,
     5.6,
     2.3
    ]
   ],
   "fr": "tasse",
   "en": "cup",
   "tr": "fincan",
   "uk": "чашка",
   "fa": "فنجان",
   "pt": "xícara",
   "ar": "فنجان",
   "pl": "filiżanka, kubek",
   "ru": "чашка"
  },
  {
   "id": "pizzakarton",
   "mot": "Karton",
   "genre": "der",
   "pluriel": "Kartons",
   "niveau": "A2",
   "theme": "wohnen_a2",
   "personne": null,
   "aussi": [
    {
     "mot": "Pizza",
     "genre": "die",
     "niveau": "B1",
     "theme": "essen_trinken_b1",
     "fr": "pizza",
     "en": "pizza",
     "tr": "pizza",
     "uk": "піца",
     "fa": "پیتزا",
     "pt": "pizza",
     "ar": "بيتزا",
     "pl": "pizza",
     "ru": "пицца"
    }
   ],
   "sur": "couchtisch",
   "devant": 0,
   "boites": [
    [
     53.3,
     64,
     20.6,
     8
    ]
   ],
   "fr": "carton",
   "en": "cardboard box",
   "tr": "karton kutu",
   "uk": "картонна коробка",
   "fa": "جعبهٔ مقوایی",
   "pt": "caixa de papelão",
   "ar": "صندوق كرتون",
   "pl": "karton",
   "ru": "картонная коробка"
  },
  {
   "id": "hund",
   "mot": "Hund",
   "genre": "der",
   "pluriel": "Hunde",
   "niveau": "A1",
   "theme": "tiere_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     44.8,
     74.2,
     27.4,
     7.4
    ]
   ],
   "fr": "chien",
   "en": "dog",
   "tr": "köpek",
   "uk": "собака",
   "fa": "سگ",
   "pt": "cachorro",
   "ar": "كلب",
   "pl": "pies",
   "ru": "собака"
  },
  {
   "id": "eimer",
   "mot": "Eimer",
   "genre": "der",
   "pluriel": "Eimer",
   "niveau": "A2",
   "theme": "moebel_haushalt_a2",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     16.1,
     80.2,
     14.8,
     10.6
    ]
   ],
   "fr": "le seau",
   "en": "bucket",
   "tr": "kova",
   "uk": "відро",
   "fa": "سطل",
   "pt": "balde",
   "ar": "دلو",
   "pl": "wiadro",
   "ru": "ведро"
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
   "sur": "eimer",
   "devant": 0,
   "boites": [
    [
     16.1,
     80.2,
     15.2,
     5
    ]
   ],
   "fr": "bouteille",
   "en": "bottle",
   "tr": "şişe",
   "uk": "пляшка",
   "fa": "بطری",
   "pt": "garrafa",
   "ar": "زجاجة",
   "pl": "butelka",
   "ru": "бутылка"
  },
  {
   "id": "karton",
   "mot": "Karton",
   "genre": "der",
   "pluriel": "Kartons",
   "niveau": "A2",
   "theme": "wohnen_a2",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     69.4,
     80,
     23,
     12.6
    ]
   ],
   "fr": "carton",
   "en": "cardboard box",
   "tr": "karton kutu",
   "uk": "картонна коробка",
   "fa": "جعبهٔ مقوایی",
   "pt": "caixa de papelão",
   "ar": "صندوق كرتون",
   "pl": "karton",
   "ru": "картонная коробка"
  },
  {
   "id": "katze",
   "mot": "Katze",
   "genre": "die",
   "pluriel": "Katzen",
   "niveau": "A1",
   "theme": "tiere_a1",
   "personne": null,
   "aussi": [],
   "sur": "karton",
   "devant": 0,
   "boites": [
    [
     79.3,
     80,
     10.4,
     5.8
    ]
   ],
   "fr": "chat",
   "en": "cat",
   "tr": "kedi",
   "uk": "кіт",
   "fa": "گربه",
   "pt": "gato",
   "ar": "قطة",
   "pl": "kot",
   "ru": "кошка"
  },
  {
   "id": "luftballon",
   "mot": "Luftballon",
   "genre": "der",
   "pluriel": "Luftballons",
   "niveau": "A2",
   "theme": "feste_feiertage_a2",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     76.6,
     70.2,
     15.8,
     7.6
    ]
   ],
   "fr": "ballon de baudruche",
   "en": "balloon",
   "tr": "balon",
   "uk": "повітряна кулька",
   "fa": "بادکنک",
   "pt": "bexiga, balão",
   "ar": "بالون",
   "pl": "balon, balonik",
   "ru": "воздушный шарик"
  },
  {
   "id": "luftballon-links",
   "mot": "Luftballon",
   "genre": "der",
   "pluriel": "Luftballons",
   "niveau": "A2",
   "theme": "feste_feiertage_a2",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     0,
     87.2,
     22.8,
     12.8
    ]
   ],
   "fr": "ballon de baudruche",
   "en": "balloon",
   "tr": "balon",
   "uk": "повітряна кулька",
   "fa": "بادکنک",
   "pt": "bexiga, balão",
   "ar": "بالون",
   "pl": "balon, balonik",
   "ru": "воздушный шарик"
  },
  {
   "id": "koffer",
   "mot": "Koffer",
   "genre": "der",
   "pluriel": "Koffer",
   "niveau": "A1",
   "theme": "reisen_urlaub_a1",
   "personne": null,
   "aussi": [],
   "sur": null,
   "devant": 0,
   "boites": [
    [
     34.5,
     81,
     25,
     19
    ]
   ],
   "fr": "valise",
   "en": "suitcase",
   "tr": "bavul",
   "uk": "валіза",
   "fa": "چمدان",
   "pt": "mala",
   "ar": "حقيبة سفر",
   "pl": "walizka",
   "ru": "чемодан"
  }
 ],
 "grosPlans": [],
 "titre": "Nach der Party",
 "alt": "Le salon de la colocation de Mark au lendemain d'une fête : un ballon sur l'armoire, un parapluie suspendu à la lampe, une chaussette sur le lampadaire, un chat dans un carton, un chien sous la table basse, et la valise de Mark sur le seuil.",
 "consigne": "Mark rentre de voyage… et ses colocataires ont fait la fête. Touche un objet.",
 "exclus": [
  "Wand",
  "Boden",
  "Decke"
 ],
 "couches": {
  "A1": {
   "titre": "Noms et articles"
  },
  "A2": {
   "titre": "Wo? — les prépositions",
   "qs": [
    {
     "q": "Wo liegt der Ball?",
     "c": [
      "auf dem Schrank",
      "unter dem Schrank",
      "neben dem Fenster"
     ],
     "f": "ball",
     "r": "schrank",
     "phrase": "Der Ball liegt auf dem Schrank.",
     "sens": "Le ballon est sur l'armoire.",
     "n": "<b>Wo?</b> → datif : der Schrank → auf <b>dem</b> Schrank."
    },
    {
     "q": "Wo liegt der Hund?",
     "c": [
      "unter dem Couchtisch",
      "auf dem Couchtisch",
      "neben dem Sofa"
     ],
     "f": "hund",
     "r": "couchtisch",
     "phrase": "Der Hund liegt unter dem Couchtisch.",
     "sens": "Le chien est couché sous la table basse.",
     "n": "<b>unter</b> = sous. Datif : der Couchtisch → unter <b>dem</b> Couchtisch."
    },
    {
     "q": "Wo sitzt die Katze?",
     "c": [
      "im Karton",
      "auf dem Karton",
      "hinter dem Karton"
     ],
     "f": "katze",
     "r": "karton",
     "phrase": "Die Katze sitzt im Karton.",
     "sens": "Le chat est assis dans le carton.",
     "n": "<b>im</b> = in + dem. Datif : der Karton → in <b>dem</b> (im) Karton."
    },
    {
     "q": "Wo hängt der Regenschirm?",
     "c": [
      "an der Lampe",
      "am Fenster",
      "an der Tür"
     ],
     "f": "regenschirm",
     "r": "lampe",
     "phrase": "Der Regenschirm hängt an der Lampe.",
     "sens": "Le parapluie est accroché à la lampe.",
     "n": "Accroché : <b>an</b> + datif. die Lampe → an <b>der</b> Lampe."
    },
    {
     "q": "Wo steht das Fahrrad?",
     "c": [
      "vor dem Regal",
      "hinter dem Regal",
      "auf dem Regal"
     ],
     "f": "fahrrad",
     "r": "regal",
     "phrase": "Das Fahrrad steht vor dem Regal.",
     "sens": "Le vélo est devant l'étagère.",
     "n": "<b>vor</b> = devant. Datif : das Regal → vor <b>dem</b> Regal."
    },
    {
     "q": "Wo steht die Gitarre?",
     "c": [
      "zwischen dem Schrank und dem Sofa",
      "auf dem Sofa",
      "unter dem Sofa"
     ],
     "f": "gitarre",
     "r": "sofa",
     "phrase": "Die Gitarre steht zwischen dem Schrank und dem Sofa.",
     "sens": "La guitare est entre l'armoire et le canapé.",
     "n": "<b>zwischen</b> = entre, au datif pour les deux : zwischen <b>dem</b> Schrank und <b>dem</b> Sofa."
    },
    {
     "q": "Wo liegen die Turnschuhe?",
     "c": [
      "unter dem Sofa",
      "auf dem Sofa",
      "neben dem Fernseher"
     ],
     "f": "turnschuh",
     "r": "sofa",
     "phrase": "Die Turnschuhe liegen unter dem Sofa.",
     "sens": "Les baskets sont sous le canapé.",
     "n": "Pluriel : die Turnschuhe <b>liegen</b>. Datif : unter <b>dem</b> Sofa."
    },
    {
     "q": "Wo steht das Glas mit dem Goldfisch?",
     "c": [
      "auf dem Regal",
      "unter dem Regal",
      "neben dem Fahrrad"
     ],
     "f": "goldfisch",
     "r": "regal",
     "phrase": "Das Glas mit dem Goldfisch steht auf dem Regal.",
     "sens": "Le bocal avec le poisson rouge est sur l'étagère.",
     "n": "<b>auf</b> + datif : auf <b>dem</b> Regal. Et <b>mit</b> est toujours au datif : mit <b>dem</b> Goldfisch."
    },
    {
     "q": "Wo hängt die Socke?",
     "c": [
      "an der Stehlampe",
      "am Fenster",
      "an der Tür"
     ],
     "f": "socke",
     "r": "stehlampe",
     "phrase": "Die Socke hängt an der Stehlampe.",
     "sens": "La chaussette est accrochée au lampadaire.",
     "n": "<b>an</b> + datif : die Stehlampe → an <b>der</b> Stehlampe."
    },
    {
     "q": "Wo ist der Heizkörper?",
     "c": [
      "unter dem Fenster",
      "über dem Fenster",
      "neben der Tür"
     ],
     "f": "heizkoerper",
     "r": "fenster",
     "phrase": "Der Heizkörper ist unter dem Fenster.",
     "sens": "Le radiateur est sous la fenêtre.",
     "n": "<b>unter</b> + datif : das Fenster → unter <b>dem</b> Fenster."
    }
   ]
  },
  "B1": {
   "titre": "Wo? ou Wohin? — Mark range",
   "qs": [
    {
     "q": "Der Ball liegt noch auf ___ Schrank.",
     "c": [
      "dem",
      "den",
      "der"
     ],
     "f": "ball",
     "r": "schrank",
     "phrase": "Der Ball liegt noch auf dem Schrank.",
     "sens": "Le ballon est encore sur l'armoire.",
     "n": "Un état (<b>liegen</b>, Wo?) → datif : auf <b>dem</b> Schrank.",
     "revise": {
      "mot": "liegen",
      "cat": "verbe"
     }
    },
    {
     "q": "Mark ___ den Ball in den Schrank.",
     "c": [
      "legt",
      "liegt",
      "steht"
     ],
     "f": "ball",
     "r": "schrank",
     "phrase": "Mark legt den Ball in den Schrank.",
     "sens": "Mark met le ballon dans l'armoire.",
     "n": "<b>legen</b> = poser à plat, un geste (Wohin?) → accusatif : in <b>den</b> Schrank. <b>liegen</b> = être posé, un état.",
     "revise": {
      "mot": "legen",
      "cat": "verbe"
     }
    },
    {
     "q": "Die Tasse ___ auf dem Couchtisch.",
     "c": [
      "steht",
      "stellt",
      "legt"
     ],
     "f": "tasse",
     "r": "couchtisch",
     "phrase": "Die Tasse steht auf dem Couchtisch.",
     "sens": "La tasse est sur la table basse.",
     "n": "Un état → <b>stehen</b> + datif : auf <b>dem</b> Couchtisch.",
     "revise": {
      "mot": "stehen",
      "cat": "verbe"
     }
    },
    {
     "q": "Mark stellt die Tasse auf ___ Regal.",
     "c": [
      "das",
      "dem",
      "den"
     ],
     "f": "tasse",
     "r": "regal",
     "phrase": "Mark stellt die Tasse auf das Regal.",
     "sens": "Mark pose la tasse sur l'étagère.",
     "n": "<b>stellen</b> = poser debout, un geste (Wohin?) → accusatif : das Regal → auf <b>das</b> Regal (aufs Regal).",
     "revise": {
      "mot": "stellen",
      "cat": "verbe"
     }
    },
    {
     "q": "Noch hängt der Regenschirm an ___ Lampe.",
     "c": [
      "der",
      "die",
      "den"
     ],
     "f": "regenschirm",
     "r": "lampe",
     "phrase": "Noch hängt der Regenschirm an der Lampe.",
     "sens": "Le parapluie est encore accroché à la lampe.",
     "n": "<b>hängen</b> pour un état (Wo?) → datif : an <b>der</b> Lampe."
    },
    {
     "q": "Mark hängt den Regenschirm an ___ Tür.",
     "c": [
      "die",
      "der",
      "den"
     ],
     "f": "regenschirm",
     "r": "tuer",
     "phrase": "Mark hängt den Regenschirm an die Tür.",
     "sens": "Mark accroche le parapluie à la porte.",
     "n": "Le même verbe <b>hängen</b>, mais un geste (Wohin?) → accusatif : an <b>die</b> Tür. C'est le cas qui dit si ça bouge."
    },
    {
     "q": "Mark legt das Buch ___ Regal.",
     "c": [
      "ins",
      "im",
      "in der"
     ],
     "f": "buch",
     "r": "regal",
     "phrase": "Mark legt das Buch ins Regal.",
     "sens": "Mark met le livre sur l'étagère.",
     "n": "Wohin? → accusatif : in + das = <b>ins</b>. <b>im</b> (in dem) répondrait à Wo?",
     "revise": {
      "mot": "legen",
      "cat": "verbe"
     }
    },
    {
     "q": "Die Flaschen stehen ___ Eimer.",
     "c": [
      "im",
      "in den",
      "ins"
     ],
     "f": "flasche",
     "r": "eimer",
     "phrase": "Die Flaschen stehen im Eimer.",
     "sens": "Les bouteilles sont dans le seau.",
     "n": "Un état (<b>stehen</b>) → datif : in dem = <b>im</b> Eimer.",
     "revise": {
      "mot": "stehen",
      "cat": "verbe"
     }
    },
    {
     "q": "Die Katze springt gleich auf ___ Sofa.",
     "c": [
      "das",
      "dem",
      "der"
     ],
     "f": "katze",
     "r": "sofa",
     "phrase": "Die Katze springt gleich auf das Sofa.",
     "sens": "Le chat va sauter sur le canapé tout de suite.",
     "n": "Un mouvement vers un lieu (Wohin?) → accusatif : auf <b>das</b> Sofa (aufs Sofa)."
    },
    {
     "q": "Die Luftballons liegen auf ___ Boden.",
     "c": [
      "dem",
      "den",
      "die"
     ],
     "f": "luftballon",
     "r": "boden",
     "phrase": "Die Luftballons liegen auf dem Boden.",
     "sens": "Les ballons sont par terre.",
     "n": "Un état → datif : der Boden → auf <b>dem</b> Boden.",
     "revise": {
      "mot": "liegen",
      "cat": "verbe"
     }
    }
   ]
  },
  "B2": {
   "titre": "Relatives et passif d'état",
   "qs": [
    {
     "q": "Die Lampe, an ___ ein Regenschirm hängt, ist rund.",
     "c": [
      "der",
      "die",
      "dem"
     ],
     "f": "lampe",
     "r": "regenschirm",
     "phrase": "Die Lampe, an der ein Regenschirm hängt, ist rund.",
     "sens": "La lampe à laquelle est accroché un parapluie est ronde.",
     "n": "Préposition + relatif : <b>an der</b> (die Lampe, datif féminin)."
    },
    {
     "q": "Der Hund, ___ unter dem Tisch schläft, hat die Party verpasst.",
     "c": [
      "der",
      "den",
      "dem"
     ],
     "f": "hund",
     "phrase": "Der Hund, der unter dem Tisch schläft, hat die Party verpasst.",
     "sens": "Le chien qui dort sous la table a raté la fête.",
     "n": "Sujet de la relative, masculin → <b>der</b>."
    },
    {
     "q": "Die Katze, ___ Kopf aus dem Karton schaut, wirkt ganz ruhig.",
     "c": [
      "deren",
      "dessen",
      "die"
     ],
     "f": "katze",
     "r": "karton",
     "phrase": "Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.",
     "sens": "Le chat dont la tête dépasse du carton a l'air tout calme.",
     "n": "Possession, antécédent féminin (die Katze) → <b>deren</b> (dont la tête)."
    },
    {
     "q": "Das Regal, vor ___ das Fahrrad steht, ist voller Bücher.",
     "c": [
      "dem",
      "das",
      "den"
     ],
     "f": "regal",
     "r": "fahrrad",
     "phrase": "Das Regal, vor dem das Fahrrad steht, ist voller Bücher.",
     "sens": "L'étagère devant laquelle est le vélo est pleine de livres.",
     "n": "<b>vor</b> + relatif, un état (Wo?) → datif : das Regal → <b>vor dem</b>."
    },
    {
     "q": "Die Tür ist ___.",
     "c": [
      "geöffnet",
      "öffnend",
      "öffnet"
     ],
     "f": "tuer",
     "phrase": "Die Tür ist geöffnet.",
     "sens": "La porte est ouverte.",
     "n": "Passif d'état : <b>sein</b> + participe passé. La porte a été ouverte, et elle le reste."
    },
    {
     "q": "Die Lichterkette ist um die Pflanze ___.",
     "c": [
      "gewickelt",
      "wickelt",
      "wickelnd"
     ],
     "f": "pflanze",
     "phrase": "Die Lichterkette ist um die Pflanze gewickelt.",
     "sens": "La guirlande lumineuse est enroulée autour de la plante.",
     "n": "Passif d'état : <b>ist</b> + participe. Et <b>um</b> veut toujours l'accusatif : um <b>die</b> Pflanze."
    }
   ]
  },
  "C1": {
   "titre": "Hypothèses",
   "qs": [
    {
     "q": "Überall liegen Luftballons: Die Party ___ sehr lang gewesen sein.",
     "c": [
      "muss",
      "soll",
      "will"
     ],
     "f": "luftballon",
     "phrase": "Die Party muss sehr lang gewesen sein.",
     "sens": "La fête a dû être très longue.",
     "n": "<b>müssen</b> + infinitif passé = presque certain, déduit de ce qu'on voit : les ballons partout."
    },
    {
     "q": "Wer hat den Regenschirm an die Lampe gehängt? Das ___ einer der Gäste gewesen sein.",
     "c": [
      "dürfte",
      "sollte",
      "wollte"
     ],
     "f": "regenschirm",
     "r": "lampe",
     "phrase": "Das dürfte einer der Gäste gewesen sein.",
     "sens": "C'était sans doute l'un des invités.",
     "n": "<b>dürfte</b> + infinitif passé = probablement : une hypothèse prudente."
    },
    {
     "q": "Niemand weiß, wem die Socke gehört. Sie ___ einem Gast gehören.",
     "c": [
      "könnte",
      "muss",
      "soll"
     ],
     "f": "socke",
     "phrase": "Sie könnte einem Gast gehören.",
     "sens": "Elle appartient peut-être à un invité.",
     "n": "<b>könnte</b> = c'est possible, mais rien ne le prouve. <b>muss</b> serait une certitude."
    },
    {
     "q": "Hätte Mark die Party nicht verpasst, ___ er jetzt auch müde.",
     "c": [
      "wäre",
      "ist",
      "war"
     ],
     "f": "koffer",
     "phrase": "Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.",
     "sens": "Si Mark n'avait pas raté la fête, il serait lui aussi fatigué maintenant.",
     "n": "Condition irréelle (hätte … verpasst), conséquence au présent → subjonctif II : <b>wäre</b>."
    }
   ]
  }
 },
 "traductions": {
  "en": {
   "champs": {
    "alt": "Mark's flat-share living room the morning after a party: a ball on the wardrobe, an umbrella hanging from the lamp, a sock on the floor lamp, a cat in a cardboard box, a dog under the coffee table, and Mark's suitcase on the threshold.",
    "consigne": "Mark is back from a trip… and his flatmates have had a party. Tap an object."
   },
   "couches": {
    "A1": "Nouns and articles",
    "A2": "Wo? — prepositions",
    "B1": "Wo? or Wohin? — Mark tidies up",
    "B2": "Relative clauses and the state passive",
    "C1": "Hypotheses"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> → dative: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = under. Dative: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dative: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Hanging: <b>an</b> + dative. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = in front of. Dative: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = between, dative for both: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Plural: die Turnschuhe <b>liegen</b>. Dative: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + dative: auf <b>dem</b> Regal. And <b>mit</b> always takes the dative: mit <b>dem</b> Goldfisch.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + dative: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + dative: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "A state (<b>liegen</b>, Wo?) → dative: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = to lay flat, an action (Wohin?) → accusative: in <b>den</b> Schrank. <b>liegen</b> = to lie, a state.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "A state → <b>stehen</b> + dative: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = to put upright, an action (Wohin?) → accusative: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> for a state (Wo?) → dative: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "The same verb <b>hängen</b>, but an action (Wohin?) → accusative: an <b>die</b> Tür. The case tells you whether something moves.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → accusative: in + das = <b>ins</b>. <b>im</b> (in dem) would answer Wo?",
    "B1 | Die Flaschen stehen im Eimer.": "A state (<b>stehen</b>) → dative: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "A movement towards a place (Wohin?) → accusative: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "A state → dative: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Preposition + relative pronoun: <b>an der</b> (die Lampe, feminine dative).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Subject of the relative clause, masculine → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Possession, feminine antecedent (die Katze) → <b>deren</b> (whose head).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + relative pronoun, a state (Wo?) → dative: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "State passive: <b>sein</b> + past participle. The door was opened, and it stays open.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "State passive: <b>ist</b> + participle. And <b>um</b> always takes the accusative: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + perfect infinitive = almost certain, deduced from what you see: balloons everywhere.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + perfect infinitive = probably: a cautious guess.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = it's possible, but nothing proves it. <b>muss</b> would be a certainty.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Unreal condition (hätte … verpasst), present result → subjunctive II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "The ball is on the cupboard.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "The dog is lying under the coffee table.",
    "A2 | Die Katze sitzt im Karton.": "The cat is sitting in the box.",
    "A2 | Der Regenschirm hängt an der Lampe.": "The umbrella hangs on the lamp.",
    "A2 | Das Fahrrad steht vor dem Regal.": "The bicycle is in front of the shelf.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "The guitar is between the cupboard and the sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "The trainers are under the sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "The bowl with the goldfish is on the shelf.",
    "A2 | Die Socke hängt an der Stehlampe.": "The sock hangs on the floor lamp.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "The radiator is under the window.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "The ball is still on the cupboard.",
    "B1 | Mark legt den Ball in den Schrank.": "Mark puts the ball in the cupboard.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "The cup is on the coffee table.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Mark puts the cup on the shelf.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "The umbrella is still hanging on the lamp.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Mark hangs the umbrella on the door.",
    "B1 | Mark legt das Buch ins Regal.": "Mark puts the book on the shelf.",
    "B1 | Die Flaschen stehen im Eimer.": "The bottles are in the bucket.",
    "B1 | Die Katze springt gleich auf das Sofa.": "The cat is about to jump onto the sofa.",
    "B1 | Die Luftballons liegen auf dem Boden.": "The balloons are on the floor.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "The lamp with an umbrella hanging on it is round.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "The dog sleeping under the table missed the party.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "The cat whose head is peeking out of the box looks very calm.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "The shelf the bicycle is in front of is full of books.",
    "B2 | Die Tür ist geöffnet.": "The door is open.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "The string of lights is wrapped around the plant.",
    "C1 | Die Party muss sehr lang gewesen sein.": "The party must have gone on very long.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "That was probably one of the guests.",
    "C1 | Sie könnte einem Gast gehören.": "It might belong to a guest.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "If Mark had not missed the party, he would be tired now too."
   }
  },
  "tr": {
   "champs": {
    "alt": "Bir partinin ertesi sabahı Mark'ın paylaşımlı evinin oturma odası: dolabın üstünde bir top, lambadan sarkan bir şemsiye, ayaklı lambanın üstünde bir çorap, karton kutuda bir kedi, orta sehpanın altında bir köpek ve kapı eşiğinde Mark'ın valizi.",
    "consigne": "Mark seyahatten dönüyor… ve ev arkadaşları parti vermiş. Bir nesneye dokun."
   },
   "couches": {
    "A1": "İsimler ve artikeller",
    "A2": "Wo? — edatlar",
    "B1": "Wo? mu, Wohin? mu? — Mark topluyor",
    "B2": "İlgi cümleleri ve durum edilgeni",
    "C1": "Varsayımlar"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> → Dativ: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = altında. Dativ: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dativ: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Asılı: <b>an</b> + Dativ. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = önünde. Dativ: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = arasında, ikisi için de Dativ: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Çoğul: die Turnschuhe <b>liegen</b>. Dativ: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: auf <b>dem</b> Regal. <b>mit</b> ise her zaman Dativ alır: mit <b>dem</b> Goldfisch.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Bir durum (<b>liegen</b>, Wo?) → Dativ: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = yatırarak koymak, bir hareket (Wohin?) → Akkusativ: in <b>den</b> Schrank. <b>liegen</b> = yatay durmak, bir durum.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Bir durum → <b>stehen</b> + Dativ: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = dik koymak, bir hareket (Wohin?) → Akkusativ: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "Durum için <b>hängen</b> (Wo?) → Dativ: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Aynı fiil <b>hängen</b>, ama bir hareket (Wohin?) → Akkusativ: an <b>die</b> Tür. Bir şeyin hareket edip etmediğini hâl söyler.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → Akkusativ: in + das = <b>ins</b>. <b>im</b> (in dem) Wo? sorusunu yanıtlardı.",
    "B1 | Die Flaschen stehen im Eimer.": "Bir durum (<b>stehen</b>) → Dativ: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Bir yere doğru hareket (Wohin?) → Akkusativ: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "Bir durum → Dativ: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Edat + ilgi zamiri: <b>an der</b> (die Lampe, dişil Dativ).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "İlgi cümlesinin öznesi, eril → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "İyelik, önceki isim dişil (die Katze) → <b>deren</b> (başı).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + ilgi zamiri, bir durum (Wo?) → Dativ: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "Durum edilgeni: <b>sein</b> + geçmiş zaman ortacı. Kapı açıldı ve öyle kalıyor.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Durum edilgeni: <b>ist</b> + ortaç. <b>um</b> ise her zaman Akkusativ alır: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + geçmiş mastar = neredeyse kesin, görülenden çıkarılıyor: her yerde balonlar.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + geçmiş mastar = muhtemelen: temkinli bir varsayım.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = mümkün, ama hiçbir şey kanıtlamıyor. <b>muss</b> kesinlik olurdu.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Gerçek dışı koşul (hätte … verpasst), şimdiki sonuç → Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "Top dolabın üstünde.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "Köpek sehpanın altında yatıyor.",
    "A2 | Die Katze sitzt im Karton.": "Kedi kutunun içinde oturuyor.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Şemsiye lambada asılı.",
    "A2 | Das Fahrrad steht vor dem Regal.": "Bisiklet rafın önünde duruyor.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "Gitar dolapla kanepenin arasında duruyor.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Spor ayakkabılar kanepenin altında.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "Japon balığının olduğu kavanoz rafın üstünde duruyor.",
    "A2 | Die Socke hängt an der Stehlampe.": "Çorap ayaklı lambada asılı.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "Kalorifer pencerenin altında.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Top hâlâ dolabın üstünde.",
    "B1 | Mark legt den Ball in den Schrank.": "Mark topu dolaba koyuyor.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Fincan sehpanın üstünde duruyor.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Mark fincanı rafa koyuyor.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "Şemsiye hâlâ lambada asılı.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Mark şemsiyeyi kapıya asıyor.",
    "B1 | Mark legt das Buch ins Regal.": "Mark kitabı rafa koyuyor.",
    "B1 | Die Flaschen stehen im Eimer.": "Şişeler kovanın içinde.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Kedi birazdan kanepeye atlayacak.",
    "B1 | Die Luftballons liegen auf dem Boden.": "Balonlar yerde.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Üstünde şemsiye asılı olan lamba yuvarlak.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Masanın altında uyuyan köpek partiyi kaçırdı.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Başı kutudan çıkan kedi çok sakin görünüyor.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "Bisikletin önünde durduğu raf kitap dolu.",
    "B2 | Die Tür ist geöffnet.": "Kapı açık.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Işık zinciri bitkiye sarılmış.",
    "C1 | Die Party muss sehr lang gewesen sein.": "Parti çok uzun sürmüş olmalı.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "Bu misafirlerden biri olsa gerek.",
    "C1 | Sie könnte einem Gast gehören.": "Bir misafirin olabilir.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Mark partiyi kaçırmasaydı o da şimdi yorgun olurdu."
   }
  },
  "uk": {
   "champs": {
    "alt": "Вітальня у спільній квартирі Марка наступного ранку після вечірки: м'яч на шафі, парасолька, що висить на лампі, шкарпетка на торшері, кіт у картонній коробці, пес під журнальним столиком і валіза Марка на порозі.",
    "consigne": "Марк повертається з поїздки… а його сусіди влаштували вечірку. Торкнись предмета."
   },
   "couches": {
    "A1": "Іменники й артиклі",
    "A2": "Wo? — прийменники",
    "B1": "Wo? чи Wohin? — Марк прибирає",
    "B2": "Відносні речення й пасив стану",
    "C1": "Припущення"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> → Dativ: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = під. Dativ: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dativ: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Висить: <b>an</b> + Dativ. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = перед. Dativ: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = між, Dativ для обох: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Множина: die Turnschuhe <b>liegen</b>. Dativ: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: auf <b>dem</b> Regal. А <b>mit</b> завжди вимагає Dativ: mit <b>dem</b> Goldfisch.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Стан (<b>liegen</b>, Wo?) → Dativ: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = класти, дія (Wohin?) → Akkusativ: in <b>den</b> Schrank. <b>liegen</b> = лежати, стан.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Стан → <b>stehen</b> + Dativ: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = ставити, дія (Wohin?) → Akkusativ: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> для стану (Wo?) → Dativ: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Те саме дієслово <b>hängen</b>, але дія (Wohin?) → Akkusativ: an <b>die</b> Tür. Саме відмінок показує, чи є рух.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → Akkusativ: in + das = <b>ins</b>. <b>im</b> (in dem) відповідало б на Wo?",
    "B1 | Die Flaschen stehen im Eimer.": "Стан (<b>stehen</b>) → Dativ: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Рух до місця (Wohin?) → Akkusativ: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "Стан → Dativ: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Прийменник + відносний займенник: <b>an der</b> (die Lampe, Dativ жіночого роду).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Підмет відносного речення, чоловічий рід → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Присвійність, попередник жіночого роду (die Katze) → <b>deren</b> (чия голова).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + відносний займенник, стан (Wo?) → Dativ: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "Пасив стану: <b>sein</b> + дієприкметник минулого часу. Двері відчинили, і вони так і лишаються.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Пасив стану: <b>ist</b> + дієприкметник. А <b>um</b> завжди вимагає Akkusativ: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + інфінітив минулого = майже напевно, висновок з того, що видно: скрізь кульки.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + інфінітив минулого = мабуть: обережне припущення.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = можливо, але ніщо цього не доводить. <b>muss</b> означало б певність.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Нереальна умова (hätte … verpasst), наслідок у теперішньому → Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "М'яч лежить на шафі.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "Собака лежить під журнальним столиком.",
    "A2 | Die Katze sitzt im Karton.": "Кіт сидить у коробці.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Парасолька висить на лампі.",
    "A2 | Das Fahrrad steht vor dem Regal.": "Велосипед стоїть перед полицею.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "Гітара стоїть між шафою та диваном.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Кросівки лежать під диваном.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "Акваріум із золотою рибкою стоїть на полиці.",
    "A2 | Die Socke hängt an der Stehlampe.": "Шкарпетка висить на торшері.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "Батарея під вікном.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "М'яч ще лежить на шафі.",
    "B1 | Mark legt den Ball in den Schrank.": "Марк кладе м'яч у шафу.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Чашка стоїть на журнальному столику.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Марк ставить чашку на полицю.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "Парасолька ще висить на лампі.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Марк вішає парасольку на двері.",
    "B1 | Mark legt das Buch ins Regal.": "Марк кладе книжку на полицю.",
    "B1 | Die Flaschen stehen im Eimer.": "Пляшки стоять у відрі.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Кіт зараз стрибне на диван.",
    "B1 | Die Luftballons liegen auf dem Boden.": "Повітряні кульки лежать на підлозі.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Лампа, на якій висить парасолька, кругла.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Собака, що спить під столом, проспала вечірку.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Кіт, чия голова визирає з коробки, здається зовсім спокійним.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "Полиця, перед якою стоїть велосипед, повна книжок.",
    "B2 | Die Tür ist geöffnet.": "Двері відчинені.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Гірлянда обмотана навколо рослини.",
    "C1 | Die Party muss sehr lang gewesen sein.": "Вечірка, мабуть, тривала дуже довго.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "Це, напевно, був хтось із гостей.",
    "C1 | Sie könnte einem Gast gehören.": "Вона, можливо, належить комусь із гостей.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Якби Марк не пропустив вечірку, він теж був би зараз утомлений."
   }
  },
  "fa": {
   "champs": {
    "alt": "نشیمن خانهٔ اشتراکی مارک، صبحِ بعد از یک مهمانی: یک توپ روی کمد، یک چتر آویزان از لامپ، یک جوراب روی چراغ پایه‌بلند، یک گربه در جعبهٔ مقوایی، یک سگ زیر میز جلومبلی و چمدان مارک در آستانهٔ در.",
    "consigne": "مارک از سفر برمی‌گردد… و هم‌خانه‌هایش مهمانی گرفته‌اند. یک چیز را لمس کن."
   },
   "couches": {
    "A1": "اسم‌ها و حرف‌های تعریف",
    "A2": "<span lang=\"de\">Wo?</span> — حرف‌های اضافه",
    "B1": "<span lang=\"de\">Wo?</span> یا <span lang=\"de\">Wohin?</span> — مارک مرتب می‌کند",
    "B2": "جمله‌های موصولی و مجهولِ حالت",
    "C1": "فرض‌ها و گمان‌ها"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> ← Dativ: <span lang=\"de\">der Schrank</span> ← <span lang=\"de\">auf <b>dem</b> Schrank</span>.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = زیرِ. Dativ: <span lang=\"de\">der Couchtisch</span> ← <span lang=\"de\">unter <b>dem</b> Couchtisch</span>.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = <span lang=\"de\">in + dem</span>. Dativ: <span lang=\"de\">der Karton</span> ← <span lang=\"de\">in <b>dem</b> (im) Karton</span>.",
    "A2 | Der Regenschirm hängt an der Lampe.": "آویزان: <b>an</b> + Dativ. <span lang=\"de\">die Lampe</span> ← <span lang=\"de\">an <b>der</b> Lampe</span>.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = جلوی. Dativ: <span lang=\"de\">das Regal</span> ← <span lang=\"de\">vor <b>dem</b> Regal</span>.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = بینِ، برای هر دو Dativ: <span lang=\"de\">zwischen <b>dem</b> Schrank und <b>dem</b> Sofa</span>.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "جمع: <span lang=\"de\">die Turnschuhe <b>liegen</b></span>. Dativ: <span lang=\"de\">unter <b>dem</b> Sofa</span>.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: <span lang=\"de\">auf <b>dem</b> Regal</span>. و <b>mit</b> همیشه Dativ می‌گیرد: <span lang=\"de\">mit <b>dem</b> Goldfisch</span>.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: <span lang=\"de\">die Stehlampe</span> ← <span lang=\"de\">an <b>der</b> Stehlampe</span>.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: <span lang=\"de\">das Fenster</span> ← <span lang=\"de\">unter <b>dem</b> Fenster</span>.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "یک حالت (<b>liegen</b>، <span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">auf <b>dem</b> Schrank</span>.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = افقی گذاشتن، یک حرکت (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">in <b>den</b> Schrank</span>. <b>liegen</b> = افقی قرار داشتن، یک حالت.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "یک حالت ← <b>stehen</b> + Dativ: <span lang=\"de\">auf <b>dem</b> Couchtisch</span>.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = ایستاده گذاشتن، یک حرکت (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">das Regal</span> ← <span lang=\"de\">auf <b>das</b> Regal (aufs Regal)</span>.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> برای حالت (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">an <b>der</b> Lampe</span>.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "همان فعل <b>hängen</b>، ولی یک حرکت (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">an <b>die</b> Tür</span>. این حالتِ دستوری است که نشان می‌دهد چیزی جابه‌جا می‌شود یا نه.",
    "B1 | Mark legt das Buch ins Regal.": "<span lang=\"de\">Wohin?</span> ← Akkusativ: <span lang=\"de\">in + das = <b>ins</b></span>. <b>im</b> (<span lang=\"de\">in dem</span>) پاسخِ <span lang=\"de\">Wo?</span> می‌بود.",
    "B1 | Die Flaschen stehen im Eimer.": "یک حالت (<b>stehen</b>) ← Dativ: <span lang=\"de\">in dem = <b>im</b> Eimer</span>.",
    "B1 | Die Katze springt gleich auf das Sofa.": "حرکت به سوی یک جا (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">auf <b>das</b> Sofa (aufs Sofa)</span>.",
    "B1 | Die Luftballons liegen auf dem Boden.": "یک حالت ← Dativ: <span lang=\"de\">der Boden</span> ← <span lang=\"de\">auf <b>dem</b> Boden</span>.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "حرف اضافه + ضمیر موصولی: <b>an der</b> (<span lang=\"de\">die Lampe</span>، Dativِ مؤنث).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "نهادِ جملهٔ موصولی، مذکر ← <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "مالکیت، مرجعِ مؤنث (<span lang=\"de\">die Katze</span>) ← <b>deren</b> (که سرش).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + ضمیر موصولی، یک حالت (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">das Regal</span> ← <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "مجهولِ حالت: <b>sein</b> + اسم مفعول. در را باز کرده‌اند و همان‌طور باز مانده است.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "مجهولِ حالت: <b>ist</b> + اسم مفعول. و <b>um</b> همیشه Akkusativ می‌گیرد: <span lang=\"de\">um <b>die</b> Pflanze</span>.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + مصدرِ گذشته = تقریباً قطعی، از آنچه می‌بینیم: بادکنک‌ها همه‌جا.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + مصدرِ گذشته = احتمالاً: گمانی محتاطانه.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = ممکن است، ولی چیزی ثابتش نمی‌کند. <b>muss</b> یعنی یقین.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "شرطِ غیرواقعی (<span lang=\"de\">hätte … verpasst</span>)، نتیجه در زمان حال ← Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "توپ روی کمد است.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "سگ زیر میز جلومبلی دراز کشیده است.",
    "A2 | Die Katze sitzt im Karton.": "گربه در جعبه نشسته است.",
    "A2 | Der Regenschirm hängt an der Lampe.": "چتر به چراغ آویزان است.",
    "A2 | Das Fahrrad steht vor dem Regal.": "دوچرخه جلوی قفسه است.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "گیتار بین کمد و کاناپه است.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "کفش‌های ورزشی زیر کاناپه هستند.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "تنگ ماهی قرمز روی قفسه است.",
    "A2 | Die Socke hängt an der Stehlampe.": "جوراب به چراغ ایستاده آویزان است.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "شوفاژ زیر پنجره است.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "توپ هنوز روی کمد است.",
    "B1 | Mark legt den Ball in den Schrank.": "مارک توپ را در کمد می‌گذارد.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "فنجان روی میز جلومبلی است.",
    "B1 | Mark stellt die Tasse auf das Regal.": "مارک فنجان را روی قفسه می‌گذارد.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "چتر هنوز به چراغ آویزان است.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "مارک چتر را به در آویزان می‌کند.",
    "B1 | Mark legt das Buch ins Regal.": "مارک کتاب را در قفسه می‌گذارد.",
    "B1 | Die Flaschen stehen im Eimer.": "بطری‌ها در سطل هستند.",
    "B1 | Die Katze springt gleich auf das Sofa.": "گربه همین حالا روی کاناپه می‌پرد.",
    "B1 | Die Luftballons liegen auf dem Boden.": "بادکنک‌ها روی زمین هستند.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "چراغی که چتر به آن آویزان است، گرد است.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "سگی که زیر میز خوابیده، مهمانی را از دست داده است.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "گربه‌ای که سرش از جعبه بیرون است، کاملاً آرام به نظر می‌رسد.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "قفسه‌ای که دوچرخه جلویش است، پر از کتاب است.",
    "B2 | Die Tür ist geöffnet.": "در باز است.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "ریسهٔ چراغ دور گیاه پیچیده شده است.",
    "C1 | Die Party muss sehr lang gewesen sein.": "مهمانی حتماً خیلی طولانی بوده است.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "احتمالاً یکی از مهمان‌ها بوده است.",
    "C1 | Sie könnte einem Gast gehören.": "شاید مال یکی از مهمان‌ها باشد.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "اگر مارک مهمانی را از دست نداده بود، حالا او هم خسته بود."
   }
  },
  "ar": {
   "champs": {
    "alt": "غرفة الجلوس في السكن المشترك لمارك صباح اليوم التالي لحفلة: كرة فوق الخزانة، ومظلة معلّقة بالمصباح، وجورب على المصباح الأرضي، وقطة في صندوق من الكرتون، وكلب تحت الطاولة المنخفضة، وحقيبة مارك عند العتبة.",
    "consigne": "مارك عائد من السفر… وزملاؤه في السكن أقاموا حفلة. المس شيئًا."
   },
   "couches": {
    "A1": "الأسماء وأدوات التعريف",
    "A2": "<span lang=\"de\">Wo?</span> — حروف الجر",
    "B1": "<span lang=\"de\">Wo?</span> أم <span lang=\"de\">Wohin?</span> — مارك يرتّب",
    "B2": "الجمل الموصولة ومجهول الحالة",
    "C1": "الافتراضات"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> ← Dativ: <span lang=\"de\">der Schrank</span> ← <span lang=\"de\">auf <b>dem</b> Schrank</span>.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = تحت. Dativ: <span lang=\"de\">der Couchtisch</span> ← <span lang=\"de\">unter <b>dem</b> Couchtisch</span>.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = <span lang=\"de\">in + dem</span>. Dativ: <span lang=\"de\">der Karton</span> ← <span lang=\"de\">in <b>dem</b> (im) Karton</span>.",
    "A2 | Der Regenschirm hängt an der Lampe.": "معلَّق: <b>an</b> + Dativ. <span lang=\"de\">die Lampe</span> ← <span lang=\"de\">an <b>der</b> Lampe</span>.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = أمام. Dativ: <span lang=\"de\">das Regal</span> ← <span lang=\"de\">vor <b>dem</b> Regal</span>.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = بين، وDativ للاثنين: <span lang=\"de\">zwischen <b>dem</b> Schrank und <b>dem</b> Sofa</span>.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "الجمع: <span lang=\"de\">die Turnschuhe <b>liegen</b></span>. Dativ: <span lang=\"de\">unter <b>dem</b> Sofa</span>.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: <span lang=\"de\">auf <b>dem</b> Regal</span>. و<b>mit</b> يأخذ Dativ دائمًا: <span lang=\"de\">mit <b>dem</b> Goldfisch</span>.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: <span lang=\"de\">die Stehlampe</span> ← <span lang=\"de\">an <b>der</b> Stehlampe</span>.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: <span lang=\"de\">das Fenster</span> ← <span lang=\"de\">unter <b>dem</b> Fenster</span>.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "حالة (<b>liegen</b>، <span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">auf <b>dem</b> Schrank</span>.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = يضع الشيء أفقيًا، وهي حركة (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">in <b>den</b> Schrank</span>. <b>liegen</b> = يكون موضوعًا، وهي حالة.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "حالة ← <b>stehen</b> + Dativ: <span lang=\"de\">auf <b>dem</b> Couchtisch</span>.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = يضع الشيء واقفًا، وهي حركة (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">das Regal</span> ← <span lang=\"de\">auf <b>das</b> Regal (aufs Regal)</span>.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> للحالة (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">an <b>der</b> Lampe</span>.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "الفعل نفسه <b>hängen</b>، لكنها حركة (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">an <b>die</b> Tür</span>. الحالة الإعرابية هي التي تقول إن كان هناك حركة.",
    "B1 | Mark legt das Buch ins Regal.": "<span lang=\"de\">Wohin?</span> ← Akkusativ: <span lang=\"de\">in + das = <b>ins</b></span>. أما <b>im</b> (<span lang=\"de\">in dem</span>) فيجيب عن <span lang=\"de\">Wo?</span>.",
    "B1 | Die Flaschen stehen im Eimer.": "حالة (<b>stehen</b>) ← Dativ: <span lang=\"de\">in dem = <b>im</b> Eimer</span>.",
    "B1 | Die Katze springt gleich auf das Sofa.": "حركة نحو مكان (<span lang=\"de\">Wohin?</span>) ← Akkusativ: <span lang=\"de\">auf <b>das</b> Sofa (aufs Sofa)</span>.",
    "B1 | Die Luftballons liegen auf dem Boden.": "حالة ← Dativ: <span lang=\"de\">der Boden</span> ← <span lang=\"de\">auf <b>dem</b> Boden</span>.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "حرف جر + ضمير موصول: <b>an der</b> (<span lang=\"de\">die Lampe</span>، Dativ المؤنث).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "فاعل الجملة الموصولة، مذكر ← <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "ملكية، والاسم المرجعي مؤنث (<span lang=\"de\">die Katze</span>) ← <b>deren</b> (التي رأسها).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + ضمير موصول، حالة (<span lang=\"de\">Wo?</span>) ← Dativ: <span lang=\"de\">das Regal</span> ← <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "مجهول الحالة: <b>sein</b> + اسم المفعول. فُتح الباب وبقي مفتوحًا.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "مجهول الحالة: <b>ist</b> + اسم المفعول. و<b>um</b> يأخذ Akkusativ دائمًا: <span lang=\"de\">um <b>die</b> Pflanze</span>.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + المصدر الماضي = شبه مؤكد، نستنتجه مما نراه: البالونات في كل مكان.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + المصدر الماضي = على الأرجح: افتراض حذر.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = هذا ممكن، لكن لا شيء يثبته. أما <b>muss</b> فيعني اليقين.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "شرط غير واقعي (<span lang=\"de\">hätte … verpasst</span>)، والنتيجة في الحاضر ← Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "الكرة على الخزانة.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "الكلب مستلقٍ تحت الطاولة الصغيرة.",
    "A2 | Die Katze sitzt im Karton.": "القطة جالسة في الصندوق.",
    "A2 | Der Regenschirm hängt an der Lampe.": "المظلّة معلّقة على المصباح.",
    "A2 | Das Fahrrad steht vor dem Regal.": "الدراجة أمام الرفّ.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "الغيتار بين الخزانة والأريكة.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "الحذاء الرياضي تحت الأريكة.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "الحوض الذي فيه السمكة الذهبية على الرفّ.",
    "A2 | Die Socke hängt an der Stehlampe.": "الجورب معلّق على المصباح الأرضي.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "المدفأة تحت النافذة.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "ما زالت الكرة على الخزانة.",
    "B1 | Mark legt den Ball in den Schrank.": "يضع مارك الكرة في الخزانة.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "الفنجان على الطاولة الصغيرة.",
    "B1 | Mark stellt die Tasse auf das Regal.": "يضع مارك الفنجان على الرفّ.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "ما زالت المظلّة معلّقة على المصباح.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "يعلّق مارك المظلّة على الباب.",
    "B1 | Mark legt das Buch ins Regal.": "يضع مارك الكتاب في الرفّ.",
    "B1 | Die Flaschen stehen im Eimer.": "الزجاجات في الدلو.",
    "B1 | Die Katze springt gleich auf das Sofa.": "ستقفز القطة على الأريكة حالاً.",
    "B1 | Die Luftballons liegen auf dem Boden.": "البالونات على الأرض.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "المصباح الذي تتدلّى منه مظلّة مستدير.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "الكلب النائم تحت الطاولة فاتته الحفلة.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "القطة التي يطلّ رأسها من الصندوق تبدو هادئة تماماً.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "الرفّ الذي أمامه الدراجة مليء بالكتب.",
    "B2 | Die Tür ist geöffnet.": "الباب مفتوح.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "سلسلة الأضواء ملفوفة حول النبتة.",
    "C1 | Die Party muss sehr lang gewesen sein.": "لا بدّ أن الحفلة كانت طويلة جداً.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "على الأرجح كان ذلك أحد الضيوف.",
    "C1 | Sie könnte einem Gast gehören.": "ربما تكون لأحد الضيوف.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "لو لم تفت مارك الحفلة، لكان هو أيضاً متعباً الآن."
   }
  },
  "pt": {
   "champs": {
    "alt": "A sala da república do Mark no dia seguinte a uma festa: uma bola em cima do armário, um guarda-chuva pendurado na luminária, uma meia no abajur de pé, um gato numa caixa de papelão, um cachorro debaixo da mesa de centro, e a mala do Mark na porta.",
    "consigne": "Mark volta de viagem… e os colegas de apartamento fizeram festa. Toque num objeto."
   },
   "couches": {
    "A1": "Substantivos e artigos",
    "A2": "Wo? — as preposições",
    "B1": "Wo? ou Wohin? — Mark arruma",
    "B2": "Relativas e passiva de estado",
    "C1": "Hipóteses"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> → Dativ: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = debaixo de. Dativ: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dativ: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Pendurado: <b>an</b> + Dativ. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = na frente de. Dativ: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = entre, no Dativ para os dois: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Plural: die Turnschuhe <b>liegen</b>. Dativ: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: auf <b>dem</b> Regal. E <b>mit</b> sempre pede Dativ: mit <b>dem</b> Goldfisch.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Um estado (<b>liegen</b>, Wo?) → Dativ: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = pôr deitado, um gesto (Wohin?) → Akkusativ: in <b>den</b> Schrank. <b>liegen</b> = estar deitado, um estado.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Um estado → <b>stehen</b> + Dativ: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = pôr em pé, um gesto (Wohin?) → Akkusativ: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> para um estado (Wo?) → Dativ: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "O mesmo verbo <b>hängen</b>, mas um gesto (Wohin?) → Akkusativ: an <b>die</b> Tür. É o caso que diz se há movimento.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → Akkusativ: in + das = <b>ins</b>. <b>im</b> (in dem) responderia a Wo?",
    "B1 | Die Flaschen stehen im Eimer.": "Um estado (<b>stehen</b>) → Dativ: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Um movimento em direção a um lugar (Wohin?) → Akkusativ: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "Um estado → Dativ: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Preposição + relativo: <b>an der</b> (die Lampe, Dativ feminino).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Sujeito da relativa, masculino → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Posse, antecedente feminino (die Katze) → <b>deren</b> (cuja cabeça).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + relativo, um estado (Wo?) → Dativ: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "Passiva de estado: <b>sein</b> + particípio passado. A porta foi aberta e continua assim.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Passiva de estado: <b>ist</b> + particípio. E <b>um</b> sempre pede o Akkusativ: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + infinitivo passado = quase certo, deduzido do que se vê: balões por todo lado.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + infinitivo passado = provavelmente: uma hipótese cautelosa.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = é possível, mas nada prova. <b>muss</b> seria uma certeza.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Condição irreal (hätte … verpasst), consequência no presente → Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "A bola está em cima do armário.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "O cachorro está deitado debaixo da mesa de centro.",
    "A2 | Die Katze sitzt im Karton.": "O gato está sentado na caixa.",
    "A2 | Der Regenschirm hängt an der Lampe.": "O guarda-chuva está pendurado na luminária.",
    "A2 | Das Fahrrad steht vor dem Regal.": "A bicicleta está em frente à estante.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "O violão está entre o armário e o sofá.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Os tênis estão debaixo do sofá.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "O aquário com o peixinho dourado está na estante.",
    "A2 | Die Socke hängt an der Stehlampe.": "A meia está pendurada no abajur de pé.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "O aquecedor fica debaixo da janela.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "A bola ainda está em cima do armário.",
    "B1 | Mark legt den Ball in den Schrank.": "Mark põe a bola no armário.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "A xícara está na mesa de centro.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Mark põe a xícara na estante.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "O guarda-chuva ainda está pendurado na luminária.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Mark pendura o guarda-chuva na porta.",
    "B1 | Mark legt das Buch ins Regal.": "Mark põe o livro na estante.",
    "B1 | Die Flaschen stehen im Eimer.": "As garrafas estão no balde.",
    "B1 | Die Katze springt gleich auf das Sofa.": "O gato vai já pular no sofá.",
    "B1 | Die Luftballons liegen auf dem Boden.": "Os balões estão no chão.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "A luminária em que está pendurado um guarda-chuva é redonda.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "O cachorro que dorme debaixo da mesa perdeu a festa.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "O gato cuja cabeça aparece na caixa parece bem tranquilo.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "A estante em frente à qual está a bicicleta está cheia de livros.",
    "B2 | Die Tür ist geöffnet.": "A porta está aberta.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "O pisca-pisca está enrolado na planta.",
    "C1 | Die Party muss sehr lang gewesen sein.": "A festa deve ter sido muito longa.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "Isso provavelmente foi um dos convidados.",
    "C1 | Sie könnte einem Gast gehören.": "Talvez seja de um convidado.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Se Mark não tivesse perdido a festa, agora também estaria cansado."
   }
  },
  "pl": {
   "champs": {
    "alt": "Salon we wspólnym mieszkaniu Marka dzień po imprezie: piłka na szafie, parasol zawieszony na lampie, skarpetka na lampie stojącej, kot w kartonie, pies pod stolikiem kawowym, a walizka Marka na progu.",
    "consigne": "Mark wraca z podróży… a jego współlokatorzy zrobili imprezę. Dotknij przedmiotu."
   },
   "couches": {
    "A1": "Rzeczowniki i rodzajniki",
    "A2": "Wo? — przyimki",
    "B1": "Wo? czy Wohin? — Mark sprząta",
    "B2": "Zdania względne i strona bierna stanu",
    "C1": "Przypuszczenia"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> → Dativ: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = pod. Dativ: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dativ: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Zawieszony: <b>an</b> + Dativ. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = przed. Dativ: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = między, oba w Dativ: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Liczba mnoga: die Turnschuhe <b>liegen</b>. Dativ: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: auf <b>dem</b> Regal. A <b>mit</b> zawsze wymaga Dativ: mit <b>dem</b> Goldfisch (po polsku narzędnik: „ze złotą rybką”).",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Stan (<b>liegen</b>, Wo?) → Dativ: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = położyć, ruch (Wohin?) → Akkusativ: in <b>den</b> Schrank. <b>liegen</b> = leżeć, stan.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Stan → <b>stehen</b> + Dativ: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = postawić, ruch (Wohin?) → Akkusativ: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> jako stan (Wo?) → Dativ: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Ten sam czasownik <b>hängen</b>, ale ruch (Wohin?) → Akkusativ: an <b>die</b> Tür. To przypadek mówi, czy jest ruch — jak w polskim „na drzwiach” / „na drzwi”.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → Akkusativ: in + das = <b>ins</b>. <b>im</b> (in dem) odpowiadałoby na Wo?",
    "B1 | Die Flaschen stehen im Eimer.": "Stan (<b>stehen</b>) → Dativ: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Ruch w stronę miejsca (Wohin?) → Akkusativ: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "Stan → Dativ: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Przyimek + zaimek względny: <b>an der</b> (die Lampe, Dativ rodzaju żeńskiego).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Podmiot zdania względnego, rodzaj męski → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Przynależność, poprzednik rodzaju żeńskiego (die Katze) → <b>deren</b> (którego głowa — a po polsku „kot, którego głowa”: inny rodzaj!).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + zaimek względny, stan (Wo?) → Dativ: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "Strona bierna stanu: <b>sein</b> + imiesłów. Drzwi ktoś otworzył — i nadal są otwarte.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Strona bierna stanu: <b>ist</b> + imiesłów. A <b>um</b> zawsze wymaga Akkusativ: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + bezokolicznik przeszły = prawie pewne, wywnioskowane z tego, co widać: wszędzie balony.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + bezokolicznik przeszły = prawdopodobnie: ostrożne przypuszczenie.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = to możliwe, ale nic tego nie dowodzi. <b>muss</b> oznaczałoby pewność.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Warunek nierzeczywisty (hätte … verpasst), skutek w teraźniejszości → Konjunktiv II: <b>wäre</b>."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "Piłka leży na szafie.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "Pies leży pod stolikiem.",
    "A2 | Die Katze sitzt im Karton.": "Kot siedzi w kartonie.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Parasol wisi na lampie.",
    "A2 | Das Fahrrad steht vor dem Regal.": "Rower stoi przed regałem.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "Gitara stoi między szafą a kanapą.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Trampki leżą pod kanapą.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "Słój ze złotą rybką stoi na regale.",
    "A2 | Die Socke hängt an der Stehlampe.": "Skarpetka wisi na lampie stojącej.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "Grzejnik jest pod oknem.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Piłka wciąż leży na szafie.",
    "B1 | Mark legt den Ball in den Schrank.": "Mark wkłada piłkę do szafy.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Filiżanka stoi na stoliku.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Mark stawia filiżankę na regale.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "Parasol wciąż wisi na lampie.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Mark wiesza parasol na drzwiach.",
    "B1 | Mark legt das Buch ins Regal.": "Mark kładzie książkę na regale.",
    "B1 | Die Flaschen stehen im Eimer.": "Butelki stoją w wiadrze.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Kot zaraz wskoczy na kanapę.",
    "B1 | Die Luftballons liegen auf dem Boden.": "Balony leżą na podłodze.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Lampa, na której wisi parasol, jest okrągła.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Pies, który śpi pod stołem, przegapił imprezę.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Kot, którego głowa wystaje z kartonu, wygląda na zupełnie spokojnego.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "Regał, przed którym stoi rower, jest pełen książek.",
    "B2 | Die Tür ist geöffnet.": "Drzwi są otwarte.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Lampki są owinięte wokół rośliny.",
    "C1 | Die Party muss sehr lang gewesen sein.": "Impreza musiała trwać bardzo długo.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "To był zapewne jeden z gości.",
    "C1 | Sie könnte einem Gast gehören.": "Być może należy do któregoś z gości.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Gdyby Mark nie przegapił imprezy, teraz też byłby zmęczony."
   }
  },
  "ru": {
   "champs": {
    "alt": "Гостиная в квартире, которую Марк снимает с соседями, наутро после вечеринки: мяч на шкафу, зонт висит на лампе, носок на торшере, кошка в коробке, собака под журнальным столиком, а чемодан Марка — на пороге.",
    "consigne": "Марк вернулся из поездки… а его соседи устроили вечеринку. Нажми на предмет."
   },
   "couches": {
    "A1": "Существительные и артикли",
    "A2": "Wo? — предлоги",
    "B1": "Wo? или Wohin? — Марк наводит порядок",
    "B2": "Относительные придаточные и пассив состояния",
    "C1": "Предположения"
   },
   "questions": {
    "A2 | Der Ball liegt auf dem Schrank.": "<b>Wo?</b> (где?) → Dativ: der Schrank → auf <b>dem</b> Schrank.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "<b>unter</b> = под. Dativ: der Couchtisch → unter <b>dem</b> Couchtisch.",
    "A2 | Die Katze sitzt im Karton.": "<b>im</b> = in + dem. Dativ: der Karton → in <b>dem</b> (im) Karton.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Висит: <b>an</b> + Dativ. die Lampe → an <b>der</b> Lampe.",
    "A2 | Das Fahrrad steht vor dem Regal.": "<b>vor</b> = перед. Dativ: das Regal → vor <b>dem</b> Regal.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "<b>zwischen</b> = между, Dativ для обоих: zwischen <b>dem</b> Schrank und <b>dem</b> Sofa.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Множественное число: die Turnschuhe <b>liegen</b>. Dativ: unter <b>dem</b> Sofa.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "<b>auf</b> + Dativ: auf <b>dem</b> Regal. А после <b>mit</b> всегда Dativ: mit <b>dem</b> Goldfisch.",
    "A2 | Die Socke hängt an der Stehlampe.": "<b>an</b> + Dativ: die Stehlampe → an <b>der</b> Stehlampe.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "<b>unter</b> + Dativ: das Fenster → unter <b>dem</b> Fenster.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Состояние (<b>liegen</b>, Wo?) → Dativ: auf <b>dem</b> Schrank.",
    "B1 | Mark legt den Ball in den Schrank.": "<b>legen</b> = класть, действие (Wohin?) → Akkusativ: in <b>den</b> Schrank. <b>liegen</b> = лежать, состояние. Как «в шкафу / в шкаф».",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Состояние → <b>stehen</b> + Dativ: auf <b>dem</b> Couchtisch.",
    "B1 | Mark stellt die Tasse auf das Regal.": "<b>stellen</b> = ставить, действие (Wohin?) → Akkusativ: das Regal → auf <b>das</b> Regal (aufs Regal).",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "<b>hängen</b> для состояния (Wo?) → Dativ: an <b>der</b> Lampe.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Тот же глагол <b>hängen</b>, но действие (Wohin?) → Akkusativ: an <b>die</b> Tür. Есть ли движение, показывает падеж.",
    "B1 | Mark legt das Buch ins Regal.": "Wohin? → Akkusativ: in + das = <b>ins</b>. <b>im</b> (in dem) отвечало бы на Wo?",
    "B1 | Die Flaschen stehen im Eimer.": "Состояние (<b>stehen</b>) → Dativ: in dem = <b>im</b> Eimer.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Движение к месту (Wohin?) → Akkusativ: auf <b>das</b> Sofa (aufs Sofa).",
    "B1 | Die Luftballons liegen auf dem Boden.": "Состояние → Dativ: der Boden → auf <b>dem</b> Boden.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Предлог + относительное местоимение: <b>an der</b> (die Lampe, Dativ женского рода).",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Подлежащее придаточного, мужской род → <b>der</b>.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Принадлежность, существительное женского рода (die Katze) → <b>deren</b> (голова которой).",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "<b>vor</b> + относительное местоимение, состояние (Wo?) → Dativ: das Regal → <b>vor dem</b>.",
    "B2 | Die Tür ist geöffnet.": "Пассив состояния: <b>sein</b> + причастие, как «дверь открыта». Её открыли, и она так и осталась.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Пассив состояния: <b>ist</b> + причастие. И <b>um</b> всегда требует Akkusativ: um <b>die</b> Pflanze.",
    "C1 | Die Party muss sehr lang gewesen sein.": "<b>müssen</b> + инфинитив прошедшего = почти наверняка, вывод из того, что видно: повсюду шарики.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "<b>dürfte</b> + инфинитив прошедшего = вероятно: осторожная гипотеза.",
    "C1 | Sie könnte einem Gast gehören.": "<b>könnte</b> = это возможно, но ничто этого не доказывает. <b>muss</b> было бы уверенностью.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Нереальное условие (hätte … verpasst), следствие в настоящем → Konjunktiv II: <b>wäre</b>. По-русски: «Не пропусти Марк вечеринку, он бы сейчас тоже был уставшим»."
   },
   "sens": {
    "A2 | Der Ball liegt auf dem Schrank.": "Мяч лежит на шкафу.",
    "A2 | Der Hund liegt unter dem Couchtisch.": "Собака лежит под журнальным столиком.",
    "A2 | Die Katze sitzt im Karton.": "Кошка сидит в коробке.",
    "A2 | Der Regenschirm hängt an der Lampe.": "Зонт висит на лампе.",
    "A2 | Das Fahrrad steht vor dem Regal.": "Велосипед стоит перед полкой.",
    "A2 | Die Gitarre steht zwischen dem Schrank und dem Sofa.": "Гитара стоит между шкафом и диваном.",
    "A2 | Die Turnschuhe liegen unter dem Sofa.": "Кроссовки лежат под диваном.",
    "A2 | Das Glas mit dem Goldfisch steht auf dem Regal.": "Банка с золотой рыбкой стоит на полке.",
    "A2 | Die Socke hängt an der Stehlampe.": "Носок висит на торшере.",
    "A2 | Der Heizkörper ist unter dem Fenster.": "Батарея под окном.",
    "B1 | Der Ball liegt noch auf dem Schrank.": "Мяч ещё лежит на шкафу.",
    "B1 | Mark legt den Ball in den Schrank.": "Марк кладёт мяч в шкаф.",
    "B1 | Die Tasse steht auf dem Couchtisch.": "Чашка стоит на журнальном столике.",
    "B1 | Mark stellt die Tasse auf das Regal.": "Марк ставит чашку на полку.",
    "B1 | Noch hängt der Regenschirm an der Lampe.": "Зонт ещё висит на лампе.",
    "B1 | Mark hängt den Regenschirm an die Tür.": "Марк вешает зонт на дверь.",
    "B1 | Mark legt das Buch ins Regal.": "Марк кладёт книгу на полку.",
    "B1 | Die Flaschen stehen im Eimer.": "Бутылки стоят в ведре.",
    "B1 | Die Katze springt gleich auf das Sofa.": "Кошка сейчас прыгнет на диван.",
    "B1 | Die Luftballons liegen auf dem Boden.": "Воздушные шары лежат на полу.",
    "B2 | Die Lampe, an der ein Regenschirm hängt, ist rund.": "Лампа, на которой висит зонт, круглая.",
    "B2 | Der Hund, der unter dem Tisch schläft, hat die Party verpasst.": "Собака, которая спит под столом, пропустила вечеринку.",
    "B2 | Die Katze, deren Kopf aus dem Karton schaut, wirkt ganz ruhig.": "Кошка, чья голова выглядывает из коробки, выглядит совсем спокойной.",
    "B2 | Das Regal, vor dem das Fahrrad steht, ist voller Bücher.": "Полка, перед которой стоит велосипед, полна книг.",
    "B2 | Die Tür ist geöffnet.": "Дверь открыта.",
    "B2 | Die Lichterkette ist um die Pflanze gewickelt.": "Гирлянда обмотана вокруг растения.",
    "C1 | Die Party muss sehr lang gewesen sein.": "Вечеринка, должно быть, была очень долгой.",
    "C1 | Das dürfte einer der Gäste gewesen sein.": "Это, вероятно, был один из гостей.",
    "C1 | Sie könnte einem Gast gehören.": "Он, возможно, принадлежит кому-то из гостей.",
    "C1 | Hätte Mark die Party nicht verpasst, wäre er jetzt auch müde.": "Если бы Марк не пропустил вечеринку, он тоже сейчас был бы уставшим."
   }
  }
 }
};
