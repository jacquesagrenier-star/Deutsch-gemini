# -*- coding: utf-8 -*-
"""Les noms des personnages dans les phrases d'exemple, langue par langue.

VALIDES par Jacques le 14 nov. 2026 (pflege/PERSONNAGES.md, « je valide ») : un nom ne change
plus que sur sa decision ; alors on le change ICI seulement, puis  python pflege/outils/construire.py

Dans les sources, un nom s'ecrit entre accolades : {Elif}, {Frau Hoffmann}.
Les phrases sont ecrites pour que le nom reste au NOMINATIF dans les langues a cas
(uk, ru, pl) : la forme ci-dessous vaut telle quelle.

Ordre : de | fr | en | tr | uk | fa | ar | pt | pl | ru | es  (l'espagnol, 16 nov. : les memes noms, rien
de change ; seule la forme espagnole est ajoutee)
"""

LANGUES_EX = ["de", "fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "es"]

_TABLE = {
    "Elif": "Elif | Elif | Elif | Elif | Еліф | الیف | إليف | Elif | Elif | Элиф | Elif",
    "Amira": "Amira | Amira | Amira | Amira | Аміра | امیره | أميرة | Amira | Amira | Амира | Amira",
    "Arun": "Arun | Arun | Arun | Arun | Арун | آرون | آرون | Arun | Arun | Арун | Arun",
    "Yusuf": "Yusuf | Yusuf | Yusuf | Yusuf | Юсуф | یوسف | يوسف | Yusuf | Yusuf | Юсуф | Yusuf",
    "Olena": "Olena | Olena | Olena | Olena | Олена | اولنا | أولينا | Olena | Olena | Олена | Olena",
    "Jonas": "Jonas | Jonas | Jonas | Jonas | Йонас | یوناس | يوناس | Jonas | Jonas | Йонас | Jonas",
    "Frau Hoffmann": "Frau Hoffmann | Mme Hoffmann | Ms Hoffmann | Hoffmann Hanım | пані Гофман | خانم هافمن | السيدة هوفمان | a senhora Hoffmann | pani Hoffmann | госпожа Хофман | la señora Hoffmann",
    "Dr. Sommer": "Dr. Sommer | la Dre Sommer | Dr Sommer | Dr. Sommer | лікарка Зоммер | دکتر زومر | الدكتورة زومر | a Dra. Sommer | doktor Sommer | доктор Зоммер | la Dra. Sommer",
    "Herr Brandt": "Herr Brandt | M. Brandt | Mr Brandt | Brandt Bey | пан Брандт | آقای برانت | السيد برانت | o senhor Brandt | pan Brandt | господин Брандт | el señor Brandt",
    "Frau Lehmann": "Frau Lehmann | Mme Lehmann | Mrs Lehmann | Lehmann Hanım | пані Леман | خانم لیمان | السيدة ليمان | a senhora Lehmann | pani Lehmann | госпожа Леман | la señora Lehmann",
    "Herr Schulze": "Herr Schulze | M. Schulze | Mr Schulze | Schulze Bey | пан Шульце | آقای شولتسه | السيد شولتسه | o senhor Schulze | pan Schulze | господин Шульце | el señor Schulze",
    "Frau Weber": "Frau Weber | Mme Weber | Mrs Weber | Weber Hanım | пані Вебер | خانم وبر | السيدة فيبر | a senhora Weber | pani Weber | госпожа Вебер | la señora Weber",
    "Frau Kowalski": "Frau Kowalski | Mme Kowalski | Mrs Kowalski | Kowalski Hanım | пані Ковальська | خانم کوالسکی | السيدة كوفالسكي | a senhora Kowalski | pani Kowalska | госпожа Ковальская | la señora Kowalski",
}

PERSONNAGES = {}
for _nom, _ligne in _TABLE.items():
    _f = [x.strip() for x in _ligne.split("|")]
    assert len(_f) == 11, _nom
    PERSONNAGES[_nom] = dict(zip(LANGUES_EX, _f))
