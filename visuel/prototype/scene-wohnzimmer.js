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
   "fa": "پتو"
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
   "fa": "دیوار"
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
   "fa": "زمین، کف"
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
     "fa": "آباژور"
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
   "fa": "چراغ"
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
   "fa": "چتر"
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
   "fa": "کمد"
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
     "fa": "فوتبال"
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
   "fa": "توپ"
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
     "fa": "تابلوی نقاشی"
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
   "fa": "تابلو، عکس"
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
   "fa": "پنجره"
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
   "fa": "رادیاتور"
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
     "fa": "ریسهٔ چراغ"
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
   "fa": "گیاه"
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
     "fa": "چراغ"
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
     "fa": "آباژور"
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
   "fa": "چراغ پایه‌بلند"
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
   "fa": "جوراب"
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
   "fa": "قفسه"
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
     "fa": "ماهی"
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
   "fa": "ماهی قرمز"
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
   "fa": "دوچرخه"
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
   "fa": "در"
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
   "fa": "مبل"
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
   "fa": "کتاب"
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
   "fa": "گیتار"
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
     "fa": "کفش"
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
   "fa": "کفش ورزشی"
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
   "fa": "تلویزیون"
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
     "fa": "بشقاب"
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
   "fa": "پیتزا"
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
     "fa": "میز"
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
   "fa": "میز جلومبلی"
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
   "fa": "فنجان"
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
     "fa": "پیتزا"
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
   "fa": "جعبهٔ مقوایی"
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
   "fa": "سگ"
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
   "fa": "سطل"
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
   "fa": "بطری"
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
   "fa": "جعبهٔ مقوایی"
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
   "fa": "گربه"
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
   "fa": "بادکنک"
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
   "fa": "بادکنک"
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
   "fa": "چمدان"
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
  }
 },
 "traductions": {
  "en": {
   "champs": {
    "alt": "Mark's flat-share living room the morning after a party: a ball on the wardrobe, an umbrella hanging from the lamp, a sock on the floor lamp, a cat in a cardboard box, a dog under the coffee table, and Mark's suitcase on the threshold.",
    "consigne": "Mark is back from a trip… and his flatmates have had a party. Tap an object."
   },
   "couches": {
    "A1": "Nouns and articles"
   },
   "questions": {}
  },
  "tr": {
   "champs": {
    "alt": "Bir partinin ertesi sabahı Mark'ın paylaşımlı evinin oturma odası: dolabın üstünde bir top, lambadan sarkan bir şemsiye, ayaklı lambanın üstünde bir çorap, karton kutuda bir kedi, orta sehpanın altında bir köpek ve kapı eşiğinde Mark'ın valizi.",
    "consigne": "Mark seyahatten dönüyor… ve ev arkadaşları parti vermiş. Bir nesneye dokun."
   },
   "couches": {
    "A1": "İsimler ve artikeller"
   },
   "questions": {}
  },
  "uk": {
   "champs": {
    "alt": "Вітальня у спільній квартирі Марка наступного ранку після вечірки: м'яч на шафі, парасолька, що висить на лампі, шкарпетка на торшері, кіт у картонній коробці, пес під журнальним столиком і валіза Марка на порозі.",
    "consigne": "Марк повертається з поїздки… а його сусіди влаштували вечірку. Торкнись предмета."
   },
   "couches": {
    "A1": "Іменники й артиклі"
   },
   "questions": {}
  },
  "fa": {
   "champs": {
    "alt": "نشیمن خانهٔ اشتراکی مارک، صبحِ بعد از یک مهمانی: یک توپ روی کمد، یک چتر آویزان از لامپ، یک جوراب روی چراغ پایه‌بلند، یک گربه در جعبهٔ مقوایی، یک سگ زیر میز جلومبلی و چمدان مارک در آستانهٔ در.",
    "consigne": "مارک از سفر برمی‌گردد… و هم‌خانه‌هایش مهمانی گرفته‌اند. یک چیز را لمس کن."
   },
   "couches": {
    "A1": "اسم‌ها و حرف‌های تعریف"
   },
   "questions": {}
  },
  "ar": {
   "champs": {
    "alt": "غرفة الجلوس في السكن المشترك لمارك صباح اليوم التالي لحفلة: كرة فوق الخزانة، ومظلة معلّقة بالمصباح، وجورب على المصباح الأرضي، وقطة في صندوق من الكرتون، وكلب تحت الطاولة المنخفضة، وحقيبة مارك عند العتبة.",
    "consigne": "مارك عائد من السفر… وزملاؤه في السكن أقاموا حفلة. المس شيئًا."
   },
   "couches": {
    "A1": "الأسماء وأدوات التعريف"
   },
   "questions": {}
  }
 }
};
