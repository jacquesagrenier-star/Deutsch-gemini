# -*- coding: utf-8 -*-
"""Les regles de prononciation pour les russophones : le dictionnaire RU.

Meme forme que PT dans tests/prononciation.py : pour chaque id de regle,
(court, explication). cablage_ru.py recopie le bloc ci-dessous (de « # LE
RUSSE » a l'accolade fermante) dans tests/prononciation.py, juste apres PT,
et y ajoute "ru" a LANGUES, la fusion RU dans construire() et la colonne
traduction_ru des exemples.

Ecrit CONTRE le russe, pas traduit du francais ni de l'ukrainien :
- « ю » et « ё » ne sont pas ü et ö (ce sont « й » + voyelle) ;
- le russe adoucit les consonnes devant е et и, l'allemand jamais : Tee
  n'est pas « тье » ;
- le russe n'a pas de h : ni « х » rauque, ni « г » ;
- le russe assourdit deja les consonnes finales (дуб -> « дуп ») : la regle
  -b -d -g est la plus facile de toutes ;
- le russe n'a pas de longueur vocalique et reduit les o inaccentues.
Guillemets « » sans espaces, tutoiement (« ты ») comme dans l'app.
Non relu par un natif.
"""

# LE RUSSE : a part, (court, explication) par regle.
# Ecrit CONTRE le russe : ю/ё ne sont pas ü/ö, pas de consonne molle devant
# e et i, h n'est ni « х » ni « г », et l'assourdissement final existe deja
# en russe (дуб = « дуп »). Non relu par un natif.
RU = {
 "u-trema": ("«и» с округлёнными губами",
             "В русском такого звука нет: скажи «и» и, не двигая языком, вытяни губы трубочкой, как для свиста. Это не «ю»: müde — не «мюде», в ü нет «й»."),
 "o-trema": ("«э» с округлёнными губами",
             "В русском такого звука нет: скажи «э» и, не двигая языком, округли губы. Это не «ё»: schön — не «шён», в ö нет «й»."),
 "a-trema": ("как «э»",
             "ä звучит как русское «э» в словах «это», «эхо»: Käse ≈ «кэзе», spät ≈ «шпэт»."),
 "u": ("как «у»",
       "u — это русское «у»: gut ≈ «гут», Buch ≈ «бух». Трудный звук — ü, а не u."),
 "ei": ("как «ай»",
        "ei читается «ай», как в слове «чай»: Wein ≈ «вайн», klein ≈ «клайн». Никогда не «эй»."),
 "ie": ("долгое «и»",
        "ie — это долгое «и», e не произносится: Liebe ≈ «лиибе». И не смягчай согласный перед i и e: в немецком они всегда твёрдые — die звучит «ди» без мягкости, Tee — «тээ», а не «тье»."),
 "eu": ("как «ой»",
        "eu и äu читаются «ой»: neu ≈ «ной», heute ≈ «хойте»."),
 "au": ("как «ау» в одном слоге",
        "au — это «ау» в одном слоге, как в слове «пауза»: Haus ≈ «хаус», Frau ≈ «фрау»."),
 "longueur": ("долгий или краткий",
              "Гласный долгий перед h или когда он удвоен (Tee, Sohn), краткий перед удвоенным согласным (Bett, kommen). В русском долготы нет, а в немецком она меняет слово. И не «акай»: безударное o остаётся «о»."),
 "sch": ("как «ш»",
         "sch — это русское «ш»: Schule ≈ «шуле», Fisch ≈ «фиш»."),
 "sp-st": ("в начале слова: «шп», «шт»",
           "В начале слова (или его части) sp и st читаются «шп» и «шт»: Straße ≈ «штрасе», sprechen ≈ «шпрехен»."),
 "ch-doux": ("мягкое «хь»",
             "После e, i, ä, ö, ü, ei, eu, l, n и r звук ch мягкий: почти как «х» в слове «хитрый», только ещё легче, язык у нёба: Milch, leicht. Не заменяй его на «ш»."),
 "ch-dur": ("как «х»",
            "После a, o, u и au ch — это русское «х», как в словах «хата», «дух»: Nacht ≈ «нахт», Buch ≈ «бух», Bauch ≈ «баух»."),
 "z": ("как «ц»",
       "z (и tz) всегда читается «ц»: Zeit ≈ «цайт», Katze ≈ «катце». Никогда не «з»."),
 "v": ("почти всегда «ф»",
       "v почти всегда читается «ф»: Vater ≈ «фатер», viel ≈ «филь». Несколько заимствованных слов сохраняют «в» (Vase, Klavier)."),
 "w": ("как «в»",
       "w читается как русское «в»: Wasser ≈ «вассер», wo ≈ «во»."),
 "s": ("«з» перед гласным",
       "Перед гласным s читается как «з»: Sonne ≈ «зоне», Hose ≈ «хозе»."),
 "eszett": ("как «с»",
            "ß и ss — это твёрдое «с». ß стоит после долгого гласного (groß), ss — после краткого (essen)."),
 "j": ("как «й»",
       "j читается как «й»: Jahr ≈ «яр», jung ≈ «юнг». Никогда не «дж» и не «ж»."),
 "h": ("в начале — выдох, после гласного — немое",
       "В русском такого звука нет. В начале слова или слога h — лёгкий выдох, как когда дышишь на стекло: не грубое «х» и не «г». Hund. После гласного h не читается и удлиняет гласный: gehen, Uhr."),
 "r": ("горловое",
       "Немецкое r обычно произносят в горле, как французское, без раскатов: rot, Brot. Русское раскатистое «р» поймут, но оно звучит с акцентом."),
 "pf": ("«п» + «ф» вместе",
        "pf: «п» и «ф» вместе, слышны оба: Apfel ≈ «апфель», Kopf ≈ «копф». Не упрощай до «ф»."),
 "er-final": ("лёгкое «а»",
              "В конце слова -er звучит как лёгкое «а», без «р»: Vater ≈ «фата», Mutter ≈ «мута»."),
 "ig-final": ("«-ихь» с мягким «х»",
              "В конце слова -ig читается «-ихь», с мягким ch, как в Milch: richtig, billig."),
 "b-d-g-final": ("«п», «т», «к»",
                 "В конце слова b, d и g оглушаются и звучат как «п», «т», «к» — точно как в русском, где «дуб» звучит «дуп», а «год» — «гот»: Kind ≈ «кинт», Tag ≈ «так», gelb ≈ «гельп»."),
}
