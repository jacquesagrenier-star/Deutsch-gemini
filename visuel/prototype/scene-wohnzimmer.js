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
   "pl": "koc"
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
   "pl": "ściana"
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
   "pl": "ziemia, podłoże"
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
     "pl": "abażur"
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
   "pl": "lampa"
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
   "pl": "parasol"
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
   "pl": "szafa"
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
     "pl": "piłka nożna"
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
   "pl": "piłka"
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
     "pl": "obraz (malowany)"
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
   "pl": "obraz"
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
   "pl": "okno"
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
   "pl": "grzejnik, kaloryfer"
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
     "pl": "girlanda świetlna, lampki"
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
   "pl": "roślina"
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
     "pl": "lampa"
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
     "pl": "abażur"
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
   "pl": "lampa stojąca"
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
   "pl": "skarpetka"
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
   "pl": "regał, półka"
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
     "pl": "ryba"
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
   "pl": "złota rybka"
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
   "pl": "rower"
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
   "pl": "drzwi"
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
   "pl": "kanapa"
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
   "pl": "książka"
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
   "pl": "gitara"
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
     "pl": "but"
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
   "pl": "trampek, but sportowy"
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
   "pl": "telewizor"
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
     "pl": "talerz"
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
   "pl": "pizza"
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
     "pl": "stół"
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
   "pl": "stolik kawowy, ława"
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
   "pl": "filiżanka, kubek"
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
     "pl": "pizza"
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
   "pl": "karton"
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
   "pl": "pies"
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
   "pl": "wiadro"
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
   "pl": "butelka"
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
   "pl": "karton"
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
   "pl": "kot"
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
   "pl": "balon, balonik"
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
   "pl": "balon, balonik"
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
   "pl": "walizka"
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
   }
  }
 }
};
