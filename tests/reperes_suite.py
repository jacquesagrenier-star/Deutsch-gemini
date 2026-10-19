# -*- coding: utf-8 -*-
"""Les repères, suite (v880, 19 oct. 2026) : l'alphabet, le genre, le pluriel.

Lu par tests/reperes_construire.py (qui écrit reperes.json et
espanol/datos/reperes.json). Jacques : « le genre avec ses exceptions, le
pluriel, l'alphabet pour épeler ».

⚠️ LES POURCENTAGES DU GENRE SONT MESURÉS sur les noms de nos thèmes
(themes.json : 4 268 noms ; temas.json : 1 666), le 19 oct. 2026 -- pas
recopiés d'une grammaire. C'est ainsi qu'on a vu que -ma n'est masculin que
dans 41 % des cas en espagnol (el problema, mais la cama), et que -um ne
l'est que dans 65 % des cas en allemand (das Museum, mais der Raum). Les
exceptions montrées sont des mots A1-A2 de notre corpus.
"""
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]

def par_langue(*textes):
    assert len(textes) == len(LANGUES), textes[0]
    return dict(zip(LANGUES, textes))

TITRES = {
    "alphabet": par_langue("L'alphabet, pour épeler", "The alphabet, to spell", "Alfabe, harf harf söylemek için",
                           "Абетка, щоб диктувати по літерах", "الفبا، برای هجی کردن", "الأبجدية للتهجئة",
                           "O alfabeto, para soletrar", "Alfabet, żeby literować", "Алфавит, чтобы называть по буквам"),
    "genre-die": par_langue("Le genre : les terminaisons en die", "Gender: endings that take die", "Cinsiyet: die alan sonekler",
                            "Рід: закінчення з die", "جنس: پایانه‌هایی که die می‌گیرند", "الجنس: النهايات التي تأخذ die",
                            "O gênero: terminações com die", "Rodzaj: końcówki z die", "Род: окончания с die"),
    "genre-der": par_langue("Le genre : les terminaisons en der", "Gender: endings that take der", "Cinsiyet: der alan sonekler",
                            "Рід: закінчення з der", "جنس: پایانه‌هایی که der می‌گیرند", "الجنس: النهايات التي تأخذ der",
                            "O gênero: terminações com der", "Rodzaj: końcówki z der", "Род: окончания с der"),
    "genre-das": par_langue("Le genre : les terminaisons en das", "Gender: endings that take das", "Cinsiyet: das alan sonekler",
                            "Рід: закінчення з das", "جنس: پایانه‌هایی که das می‌گیرند", "الجنس: النهايات التي تأخذ das",
                            "O gênero: terminações com das", "Rodzaj: końcówki z das", "Род: окончания с das"),
    "genre-m": par_langue("Le genre : les terminaisons masculines (el)", "Gender: masculine endings (el)", "Cinsiyet: eril sonekler (el)",
                          "Рід: закінчення чоловічого роду (el)", "جنس: پایانه‌های مذکر (el)", "الجنس: نهايات المذكر (el)",
                          "O gênero: terminações masculinas (el)", "Rodzaj: końcówki męskie (el)", "Род: окончания мужского рода (el)"),
    "genre-f": par_langue("Le genre : les terminaisons féminines (la)", "Gender: feminine endings (la)", "Cinsiyet: dişil sonekler (la)",
                          "Рід: закінчення жіночого роду (la)", "جنس: پایانه‌های مؤنث (la)", "الجنس: نهايات المؤنث (la)",
                          "O gênero: terminações femininas (la)", "Rodzaj: końcówki żeńskie (la)", "Род: окончания женского рода (la)"),
    "pluriel": par_langue("Le pluriel", "The plural", "Çoğul", "Множина", "جمع", "الجمع", "O plural", "Liczba mnoga", "Множественное число"),
}

ASTUCES = {
  "de": {
    "alphabet": par_langue(
        "Attention : E se dit « é », I « i », U « ou », J « yott », V « faou », W « vé », Z « tsètt ». En épelant, ä se dit « A-Umlaut » et ß « Eszett ».",
        "Watch out: E sounds like “ay”, I like “ee”, U like “oo”, J is “yot”, V is “fow”, W is “vay”, Z is “tset”. When spelling, ä is “A-Umlaut” and ß is “Eszett”.",
        "Dikkat: E “e”, I “i”, U “u”, J “yot”, V “fau”, W “ve”, Z “tset” okunur. Harf harf söylerken ä “A-Umlaut”, ß “Eszett” denir.",
        "Увага: E — «е», I — «і», U — «у», J — «йот», V — «фау», W — «ве», Z — «цет». Коли диктуєш по літерах, ä — «A-Umlaut», ß — «Eszett».",
        "دقت کن: E «اِ»، I «ای»، U «او»، J «یُت»، V «فاو»، W «وِ»، Z «تسِت» خوانده می‌شود. هنگام هجی، ä را «A-Umlaut» و ß را «Eszett» می‌گویند.",
        "انتبه: E تُلفظ «إيه»، وI «إي»، وU «أو»، وJ «يوت»، وV «فاو»، وW «فيه»، وZ «تسيت». عند التهجئة تُقال ä «A-Umlaut» وß «Eszett».",
        "Atenção: E se diz “ê”, I “i”, U “u”, J “iót”, V “fau”, W “vê”, Z “tsét”. Ao soletrar, ä é “A-Umlaut” e ß é “Eszett”.",
        "Uwaga: E czyta się „e”, I „i”, U „u”, J „jot”, V „fau”, W „we”, Z „cet”. Przy literowaniu ä to „A-Umlaut”, a ß to „Eszett”.",
        "Внимание: E — «э», I — «и», U — «у», J — «йот», V — «фау», W — «ве», Z — «цэт». По буквам ä называют «A-Umlaut», а ß — «Eszett»."),
    "genre-die": par_langue(
        "-ung, -heit, -keit, -schaft, -ion, -tät : die, presque sans exception. -e : die 9 fois sur 10 — mais der Name, der Junge, der Käse, das Auge, das Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: die, almost without exception. -e: die 9 times out of 10 — but der Name, der Junge, der Käse, das Auge, das Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: neredeyse istisnasız die. -e: 10'da 9 die — ama der Name, der Junge, der Käse, das Auge, das Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: die, майже без винятків. -e: die у 9 випадках з 10 — але der Name, der Junge, der Käse, das Auge, das Ende.",
        "‏-ung، -heit، -keit، -schaft، -ion، -tät: تقریباً همیشه die. ‏-e: از هر 10 تا 9 تا die است — اما der Name، der Junge، der Käse، das Auge، das Ende.",
        "‏-ung و-heit و-keit و-schaft و-ion و-tät: die تقريبًا بلا استثناء. ‏-e: die في 9 من 10 — لكن der Name وder Junge وder Käse وdas Auge وdas Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: die, quase sem exceção. -e: die 9 em cada 10 vezes — mas der Name, der Junge, der Käse, das Auge, das Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: die, prawie bez wyjątków. -e: die w 9 na 10 przypadków — ale der Name, der Junge, der Käse, das Auge, das Ende.",
        "-ung, -heit, -keit, -schaft, -ion, -tät: die, почти без исключений. -e: die в 9 случаях из 10 — но der Name, der Junge, der Käse, das Auge, das Ende."),
    "genre-der": par_langue(
        "Jours, mois, saisons : der (der Montag, der Juli, der Winter). -ling, -ist, -ismus : der. -er : der 7 fois sur 10, surtout les métiers (der Lehrer) — mais die Mutter, die Schwester, das Fenster.",
        "Days, months, seasons: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: der 7 times out of 10, especially jobs (der Lehrer) — but die Mutter, die Schwester, das Fenster.",
        "Günler, aylar, mevsimler: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: 10'da 7 der, özellikle meslekler (der Lehrer) — ama die Mutter, die Schwester, das Fenster.",
        "Дні, місяці, пори року: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: der у 7 випадках з 10, особливо професії (der Lehrer) — але die Mutter, die Schwester, das Fenster.",
        "روزها، ماه‌ها و فصل‌ها: der (der Montag، der Juli، der Winter). ‏-ling، -ist، -ismus: der. ‏-er: از هر 10 تا 7 تا der، به‌ویژه شغل‌ها (der Lehrer) — اما die Mutter، die Schwester، das Fenster.",
        "الأيام والأشهر والفصول: der (der Montag وder Juli وder Winter). ‏-ling و-ist و-ismus: der. ‏-er: der في 7 من 10، خاصة المهن (der Lehrer) — لكن die Mutter وdie Schwester وdas Fenster.",
        "Dias, meses, estações: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: der 7 em cada 10 vezes, sobretudo profissões (der Lehrer) — mas die Mutter, die Schwester, das Fenster.",
        "Dni, miesiące, pory roku: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: der w 7 na 10 przypadków, zwłaszcza zawody (der Lehrer) — ale die Mutter, die Schwester, das Fenster.",
        "Дни, месяцы, времена года: der (der Montag, der Juli, der Winter). -ling, -ist, -ismus: der. -er: der в 7 случаях из 10, особенно профессии (der Lehrer) — но die Mutter, die Schwester, das Fenster."),
    "genre-das": par_langue(
        "-chen (le petit) : toujours das — das Mädchen, même pour une fille. -ment, -nis, -um : das le plus souvent (der Moment, die Erlaubnis, der Raum font exception). Un verbe devenu nom : das Essen, das Leben.",
        "-chen (little): always das — das Mädchen, even for a girl. -ment, -nis, -um: usually das (der Moment, die Erlaubnis, der Raum are exceptions). A verb used as a noun: das Essen, das Leben.",
        "-chen (küçültme): her zaman das — das Mädchen, bir kız için bile. -ment, -nis, -um: çoğunlukla das (der Moment, die Erlaubnis, der Raum istisnadır). İsim olmuş fiil: das Essen, das Leben.",
        "-chen (зменшувальне): завжди das — das Mädchen, навіть про дівчинку. -ment, -nis, -um: найчастіше das (винятки: der Moment, die Erlaubnis, der Raum). Дієслово як іменник: das Essen, das Leben.",
        "‏-chen (کوچک‌سازی): همیشه das — das Mädchen، حتی برای یک دختر. ‏-ment، -nis، -um: بیشتر das (استثناها: der Moment، die Erlaubnis، der Raum). فعلی که اسم شده: das Essen، das Leben.",
        "‏-chen (التصغير): دائمًا das — das Mädchen، حتى للفتاة. ‏-ment و-nis و-um: das غالبًا (الاستثناءات: der Moment وdie Erlaubnis وder Raum). الفعل حين يصير اسمًا: das Essen وdas Leben.",
        "-chen (diminutivo): sempre das — das Mädchen, mesmo para uma menina. -ment, -nis, -um: das na maioria das vezes (der Moment, die Erlaubnis, der Raum são exceções). Verbo usado como substantivo: das Essen, das Leben.",
        "-chen (zdrobnienie): zawsze das — das Mädchen, nawet o dziewczynce. -ment, -nis, -um: zwykle das (wyjątki: der Moment, die Erlaubnis, der Raum). Czasownik jako rzeczownik: das Essen, das Leben.",
        "-chen (уменьшительное): всегда das — das Mädchen, даже о девочке. -ment, -nis, -um: чаще всего das (исключения: der Moment, die Erlaubnis, der Raum). Глагол в роли существительного: das Essen, das Leben."),
    "pluriel": par_langue(
        "Au pluriel, l'article est toujours die. Féminins : -n ou -en presque toujours (die Lampen, die Frauen). Mots en -er, -el, -en (der, das) : rien, parfois un tréma (die Lehrer, die Äpfel). Mots étrangers : -s (die Autos). Pour le reste, apprends le pluriel avec le mot.",
        "In the plural, the article is always die. Feminine nouns: -n or -en almost always (die Lampen, die Frauen). Words in -er, -el, -en (der, das): nothing, sometimes an umlaut (die Lehrer, die Äpfel). Foreign words: -s (die Autos). For the rest, learn the plural with the word.",
        "Çoğulda artikel her zaman die'dır. Dişil isimler: neredeyse her zaman -n veya -en (die Lampen, die Frauen). -er, -el, -en ile biten der/das isimler: ek yok, bazen Umlaut (die Lehrer, die Äpfel). Yabancı kelimeler: -s (die Autos). Geri kalanında çoğulu kelimeyle birlikte öğren.",
        "У множині артикль завжди die. Жіночий рід: майже завжди -n або -en (die Lampen, die Frauen). Слова на -er, -el, -en (der, das): нічого, іноді умлаут (die Lehrer, die Äpfel). Іншомовні слова: -s (die Autos). В інших випадках вчи множину разом зі словом.",
        "در جمع، حرف تعریف همیشه die است. اسم‌های مؤنث: تقریباً همیشه -n یا -en (die Lampen، die Frauen). واژه‌های مختوم به -er، -el، -en (der، das): بدون پسوند، گاهی با اوملاوت (die Lehrer، die Äpfel). واژه‌های خارجی: -s (die Autos). برای بقیه، جمع را همراه واژه یاد بگیر.",
        "في الجمع تكون أداة التعريف دائمًا die. المؤنث: ‎-n أو ‎-en تقريبًا دائمًا (die Lampen وdie Frauen). الكلمات المنتهية بـ ‎-er و‎-el و‎-en (der وdas): لا شيء، وأحيانًا Umlaut (die Lehrer وdie Äpfel). الكلمات الأجنبية: ‎-s (die Autos). وفي الباقي احفظ الجمع مع الكلمة.",
        "No plural, o artigo é sempre die. Femininos: quase sempre -n ou -en (die Lampen, die Frauen). Palavras em -er, -el, -en (der, das): nada, às vezes um trema (die Lehrer, die Äpfel). Palavras estrangeiras: -s (die Autos). No resto, aprenda o plural junto com a palavra.",
        "W liczbie mnogiej rodzajnik to zawsze die. Rodzaj żeński: prawie zawsze -n lub -en (die Lampen, die Frauen). Słowa na -er, -el, -en (der, das): bez końcówki, czasem z umlautem (die Lehrer, die Äpfel). Słowa obce: -s (die Autos). Liczby mnogiej reszty słów ucz się razem ze słowem.",
        "Во множественном числе артикль всегда die. Женский род: почти всегда -n или -en (die Lampen, die Frauen). Слова на -er, -el, -en (der, das): ничего, иногда умлаут (die Lehrer, die Äpfel). Иностранные слова: -s (die Autos). В остальном учи множественное число вместе со словом."),
  },
  "es": {
    "alphabet": par_langue(
        "h ne se prononce jamais (hache). j (jota), et g devant e ou i, se raclent au fond de la gorge. b et v se disent pareil : on précise « be » et « uve » (en Amérique latine : « be larga », « ve corta »). ñ = eñe.",
        "h is always silent (hache). j (jota), and g before e or i, are a rough throat sound. b and v sound the same, so people say “be” and “uve” (in Latin America: “be larga”, “ve corta”). ñ = eñe.",
        "h hiç okunmaz (hache). j (jota) ve e, i önündeki g gırtlaktan, hırıltılı okunur. b ile v aynı okunur; bu yüzden “be” ve “uve” denir (Latin Amerika'da: “be larga”, “ve corta”). ñ = eñe.",
        "h ніколи не вимовляють (hache). j (jota) і g перед e, i — хрипкий звук з горла. b і v звучать однаково, тому кажуть «be» і «uve» (у Латинській Америці: «be larga», «ve corta»). ñ = eñe.",
        "h هرگز خوانده نمی‌شود (hache). j (jota) و g پیش از e و i مثل «خ» از ته گلو گفته می‌شوند. b و v یکسان خوانده می‌شوند؛ برای همین می‌گویند «be» و «uve» (در آمریکای لاتین: «be larga» و «ve corta»). ñ = eñe.",
        "حرف h لا يُلفظ أبدًا (hache). وj (jota) وg قبل e وi تُلفظان كالخاء. b وv تُلفظان بالطريقة نفسها، لذلك يُقال «be» و«uve» (وفي أمريكا اللاتينية: «be larga» و«ve corta»). ñ = eñe.",
        "O h nunca se pronuncia (hache). O j (jota) e o g antes de e, i soam como um “r” forte da garganta. b e v soam igual: diz-se “be” e “uve” (na América Latina: “be larga”, “ve corta”). ñ = eñe.",
        "h nigdy się nie wymawia (hache). j (jota) i g przed e, i brzmią jak polskie „ch”. b i v brzmią tak samo, więc mówi się „be” i „uve” (w Ameryce Łacińskiej: „be larga”, „ve corta”). ñ = eñe.",
        "h никогда не произносится (hache). j (jota) и g перед e, i звучат как русское «х». b и v звучат одинаково, поэтому говорят «be» и «uve» (в Латинской Америке — «be larga», «ve corta»). ñ = eñe."),
    "genre-m": par_langue(
        "-o, -or, -aje, -ante : el, dans 96 à 100 % de nos mots. Méfie-toi de -ma : el problema, el idioma, el clima (mots savants), mais la cama, la forma. Exceptions à retenir : la mano, la foto, la moto, la flor.",
        "-o, -or, -aje, -ante: el, in 96 to 100% of our words. Careful with -ma: el problema, el idioma, el clima (learned words), but la cama, la forma. Exceptions to remember: la mano, la foto, la moto, la flor.",
        "-o, -or, -aje, -ante: kelimelerimizin %96-100'ünde el. -ma'ya dikkat: el problema, el idioma, el clima (bilimsel kökenli), ama la cama, la forma. Akılda tutulacak istisnalar: la mano, la foto, la moto, la flor.",
        "-o, -or, -aje, -ante: el у 96–100 % наших слів. Обережно з -ma: el problema, el idioma, el clima (книжні слова), але la cama, la forma. Винятки, які варто запам'ятати: la mano, la foto, la moto, la flor.",
        "‏-o، -or، -aje، -ante: در 96 تا 100 درصد واژه‌های ما el. مراقب -ma باش: el problema، el idioma، el clima (واژه‌های علمی)، اما la cama، la forma. استثناهایی که باید به خاطر بسپاری: la mano، la foto، la moto، la flor.",
        "‏-o و-or و-aje و-ante: el في 96 إلى 100٪ من كلماتنا. احذر -ma: el problema وel idioma وel clima (كلمات عالِمة)، لكن la cama وla forma. استثناءات يجب حفظها: la mano وla foto وla moto وla flor.",
        "-o, -or, -aje, -ante: el em 96 a 100% das nossas palavras. Cuidado com -ma: el problema, el idioma, el clima (palavras eruditas), mas la cama, la forma. Exceções para lembrar: la mano, la foto, la moto, la flor.",
        "-o, -or, -aje, -ante: el w 96–100% naszych słów. Uwaga na -ma: el problema, el idioma, el clima (słowa uczone), ale la cama, la forma. Wyjątki do zapamiętania: la mano, la foto, la moto, la flor.",
        "-o, -or, -aje, -ante: el в 96–100 % наших слов. Осторожно с -ma: el problema, el idioma, el clima (книжные слова), но la cama, la forma. Исключения, которые стоит запомнить: la mano, la foto, la moto, la flor."),
    "genre-f": par_langue(
        "-a, -ión, -dad, -tad, -umbre : la. Pièges fréquents : el día, el mapa, el problema, el idioma, el avión, el camión. -e ne dit rien (el padre, la madre, la llave) : apprends l'article avec le mot.",
        "-a, -ión, -dad, -tad, -umbre: la. Common traps: el día, el mapa, el problema, el idioma, el avión, el camión. -e tells you nothing (el padre, la madre, la llave): learn the article with the word.",
        "-a, -ión, -dad, -tad, -umbre: la. Sık tuzaklar: el día, el mapa, el problema, el idioma, el avión, el camión. -e hiçbir şey söylemez (el padre, la madre, la llave): artikeli kelimeyle birlikte öğren.",
        "-a, -ión, -dad, -tad, -umbre: la. Часті пастки: el día, el mapa, el problema, el idioma, el avión, el camión. -e нічого не підказує (el padre, la madre, la llave): вчи артикль разом зі словом.",
        "‏-a، -ión، -dad، -tad، -umbre: la. دام‌های رایج: el día، el mapa، el problema، el idioma، el avión، el camión. ‏-e چیزی نمی‌گوید (el padre، la madre، la llave): حرف تعریف را همراه واژه یاد بگیر.",
        "‏-a و-ión و-dad و-tad و-umbre: la. فخاخ شائعة: el día وel mapa وel problema وel idioma وel avión وel camión. ‏-e لا تدل على شيء (el padre وla madre وla llave): احفظ أداة التعريف مع الكلمة.",
        "-a, -ión, -dad, -tad, -umbre: la. Armadilhas comuns: el día, el mapa, el problema, el idioma, el avión, el camión. -e não diz nada (el padre, la madre, la llave): aprenda o artigo com a palavra.",
        "-a, -ión, -dad, -tad, -umbre: la. Częste pułapki: el día, el mapa, el problema, el idioma, el avión, el camión. -e nic nie mówi (el padre, la madre, la llave): ucz się rodzajnika razem ze słowem.",
        "-a, -ión, -dad, -tad, -umbre: la. Частые ловушки: el día, el mapa, el problema, el idioma, el avión, el camión. -e ничего не подсказывает (el padre, la madre, la llave): учи артикль вместе со словом."),
    "pluriel": par_langue(
        "Voyelle → + s (la casa → las casas). Consonne → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Un mot en -s non accentué ne change pas (el lunes → los lunes). L'accent écrit peut tomber ou apparaître : canción → canciones, joven → jóvenes.",
        "Vowel → + s (la casa → las casas). Consonant → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). A word ending in unstressed -s doesn't change (el lunes → los lunes). The written accent can drop or appear: canción → canciones, joven → jóvenes.",
        "Ünlü → + s (la casa → las casas). Ünsüz → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Vurgusuz -s ile biten kelime değişmez (el lunes → los lunes). Yazılı vurgu düşebilir ya da eklenebilir: canción → canciones, joven → jóvenes.",
        "Голосна → + s (la casa → las casas). Приголосна → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Слово на ненаголошене -s не змінюється (el lunes → los lunes). Знак наголосу може зникнути або з'явитися: canción → canciones, joven → jóvenes.",
        "واکه → + s (la casa → las casas). همخوان → + es (el árbol → los árboles). ‏-z → -ces (el lápiz → los lápices). واژه‌ای که به -s بی‌تکیه ختم شود تغییر نمی‌کند (el lunes → los lunes). علامت تکیه ممکن است بیفتد یا اضافه شود: canción → canciones، joven → jóvenes.",
        "حرف علة → + s (la casa → las casas). حرف ساكن → + es (el árbol → los árboles). ‎-z → -ces (el lápiz → los lápices). الكلمة المنتهية بـ ‎-s غير المنبورة لا تتغير (el lunes → los lunes). علامة النبر قد تسقط أو تظهر: canción → canciones وjoven → jóvenes.",
        "Vogal → + s (la casa → las casas). Consoante → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Palavra em -s átono não muda (el lunes → los lunes). O acento gráfico pode cair ou aparecer: canción → canciones, joven → jóvenes.",
        "Samogłoska → + s (la casa → las casas). Spółgłoska → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Słowo na nieakcentowane -s się nie zmienia (el lunes → los lunes). Akcent graficzny może zniknąć lub się pojawić: canción → canciones, joven → jóvenes.",
        "Гласная → + s (la casa → las casas). Согласная → + es (el árbol → los árboles). -z → -ces (el lápiz → los lápices). Слово на безударное -s не меняется (el lunes → los lunes). Знак ударения может исчезнуть или появиться: canción → canciones, joven → jóvenes."),
  },
}

# L'alphabet : (lettre, nom tel qu'on le dit, lettres qui se confondent). Le nom
# allemand est ecrit comme il se prononce (Zeh pour C, Fau pour V) : c'est lui
# que la voix dit, et que l'apprenant voit.
ALPHABET = {
  "de": [
    ("A", "Ah", ["E", "H"]), ("B", "Beh", ["P", "D"]), ("C", "Zeh", ["Z", "T"]), ("D", "Deh", ["T", "B"]),
    ("E", "Eh", ["I", "Ä"]), ("F", "Eff", ["V", "S"]), ("G", "Geh", ["J", "K"]), ("H", "Hah", ["A", "K"]),
    ("I", "Ih", ["E", "Y"]), ("J", "Jott", ["G", "Y"]), ("K", "Kah", ["Q", "G"]), ("L", "Ell", ["R", "M"]),
    ("M", "Emm", ["N", "L"]), ("N", "Enn", ["M", "L"]), ("O", "Oh", ["U", "Ö"]), ("P", "Peh", ["B", "T"]),
    ("Q", "Kuh", ["K", "U"]), ("R", "Err", ["L", "E"]), ("S", "Ess", ["Z", "F"]), ("T", "Teh", ["D", "P"]),
    ("U", "Uh", ["O", "Ü"]), ("V", "Fau", ["F", "W"]), ("W", "Weh", ["V", "B"]), ("X", "Ix", ["S", "I"]),
    ("Y", "Ypsilon", ["J", "I"]), ("Z", "Zett", ["C", "S"]), ("Ä", "Ä", ["E", "A"]), ("Ö", "Ö", ["O", "Ü"]),
    ("Ü", "Ü", ["U", "I"]), ("ß", "Eszett", ["S", "Z"]),
  ],
  "es": [
    ("A", "a", ["E", "O"]), ("B", "be", ["V", "P"]), ("C", "ce", ["S", "Z"]), ("D", "de", ["T", "B"]),
    ("E", "e", ["I", "A"]), ("F", "efe", ["V", "S"]), ("G", "ge", ["J", "H"]), ("H", "hache", ["J", "G"]),
    ("I", "i", ["E", "Y"]), ("J", "jota", ["G", "H"]), ("K", "ka", ["Q", "C"]), ("L", "ele", ["R", "E"]),
    ("M", "eme", ["N", "Ñ"]), ("N", "ene", ["Ñ", "M"]), ("Ñ", "eñe", ["N", "Y"]), ("O", "o", ["U", "A"]),
    ("P", "pe", ["B", "T"]), ("Q", "cu", ["K", "C"]), ("R", "erre", ["L", "D"]), ("S", "ese", ["Z", "C"]),
    ("T", "te", ["D", "P"]), ("U", "u", ["O", "W"]), ("V", "uve", ["B", "F"]), ("W", "uve doble", ["V", "U"]),
    ("X", "equis", ["S", "J"]), ("Y", "ye", ["I", "J"]), ("Z", "zeta", ["C", "S"]),
  ],
}
# Des mots courts a epeler : (epellation dite, mot).
EPELER = {
  "de": [("Hah, Oh, Teh, Eh, Ell", "Hotel"), ("Teh, Ah, Ix, Ih", "Taxi"), ("Beh, Uh, Ess", "Bus"), ("Zett, Uh, Geh", "Zug"),
         ("Enn, Ah, Emm, Eh", "Name"), ("Eh, Uh, Err, Oh", "Euro"), ("Weh, Ih, Eh, Enn", "Wien"), ("Jott, Uh, Ell, Ih", "Juli")],
  "es": [("hache, o, ele, a", "hola"), ("te, a, equis, i", "taxi"), ("ce, a, ese, a", "casa"), ("pe, e, ese, o", "peso"),
         ("uve, i, ene, o", "vino"), ("jota, u, e, uve, e, ese", "jueves"), ("zeta, u, eme, o", "zumo"), ("ge, e, ene, te, e", "gente")],
}

X = "⚠️ "
# Le genre : (id, tableau [mot avec article, regle], exercices [mot avec article, regle]).
GENRE = {
  "de": [
    ("genre-die",
     [("die Wohnung", "-ung → die · 99 %"), ("die Gesundheit", "-heit · -keit → die · 100 %"), ("die Freundschaft", "-schaft → die · 100 %"),
      ("die Information", "-ion → die · 99 %"), ("die Universität", "-tät → die · 100 %"), ("die Familie", "-ie → die · 94 %"),
      ("die Musik", "-ik → die · 89 %"), ("die Lampe", "-e → die · 90 %"), ("der Junge", X + "-e → der"), ("das Auge", X + "-e → das")],
     [("die Zeitung", "-ung → die · 99 %"), ("die Prüfung", "-ung → die · 99 %"), ("die Krankheit", "-heit · -keit → die · 100 %"),
      ("die Mannschaft", "-schaft → die · 100 %"), ("die Temperatur", "-ur → die · 84 %"), ("die Adresse", "-e → die · 90 %"),
      ("die Suppe", "-e → die · 90 %"), ("die Banane", "-e → die · 90 %"), ("der Name", X + "-e → der"), ("der Käse", X + "-e → der"),
      ("das Ende", X + "-e → das")]),
    ("genre-der",
     [("der Montag", "Montag · Juli · Winter → der"), ("der Frühling", "-ling → der · 80 %"), ("der Polizist", "-ist → der · 85 %"),
      ("der Tourismus", "-ismus → der · 100 %"), ("der Lehrer", "-er → der · 71 %"), ("die Mutter", X + "-er → die"), ("das Fenster", X + "-er → das")],
     [("der Juli", "Montag · Juli · Winter → der"), ("der Winter", "Montag · Juli · Winter → der"), ("der Journalist", "-ist → der · 85 %"),
      ("der Kellner", "-er → der · 71 %"), ("der Bäcker", "-er → der · 71 %"), ("der Schüler", "-er → der · 71 %"),
      ("die Schwester", X + "-er → die"), ("die Butter", X + "-er → die"), ("das Zimmer", X + "-er → das")]),
    ("genre-das",
     [("das Mädchen", "-chen → das"), ("das Brötchen", "-chen → das"), ("das Medikament", "-ment → das · 92 %"),
      ("das Ergebnis", "-nis → das · 83 %"), ("das Museum", "-um → das · 65 %"), ("das Essen", "essen → das Essen"),
      ("der Moment", X + "-ment → der"), ("die Erlaubnis", X + "-nis → die"), ("der Raum", X + "-um → der")],
     [("das Instrument", "-ment → das · 92 %"), ("das Dokument", "-ment → das · 92 %"), ("das Zeugnis", "-nis → das · 83 %"),
      ("das Datum", "-um → das · 65 %"), ("das Studium", "-um → das · 65 %"), ("das Leben", "leben → das Leben"),
      ("das Schwimmen", "schwimmen → das Schwimmen"), ("der Baum", X + "-um → der")]),
  ],
  "es": [
    ("genre-m",
     [("el libro", "-o → el · 99 %"), ("el color", "-or → el · 96 %"), ("el viaje", "-aje → el · 100 %"),
      ("el restaurante", "-ante → el · 100 %"), ("el problema", "-ma → el 41 % · la 59 %"), ("la mano", X + "-o → la"),
      ("la foto", X + "-o → la"), ("la flor", X + "-or → la"), ("la cama", "-ma → el 41 % · la 59 %")],
     [("el piso", "-o → el · 99 %"), ("el baño", "-o → el · 99 %"), ("el ordenador", "-or → el · 96 %"),
      ("el equipaje", "-aje → el · 100 %"), ("el estudiante", "-ante → el · 100 %"), ("el idioma", "-ma → el 41 % · la 59 %"),
      ("el clima", "-ma → el 41 % · la 59 %"), ("la moto", X + "-o → la"), ("la forma", "-ma → el 41 % · la 59 %")]),
    ("genre-f",
     [("la casa", "-a → la · 95 %"), ("la estación", "-ión → la · 99 %"), ("la ciudad", "-dad → la · 100 %"),
      ("la libertad", "-tad → la · 100 %"), ("la costumbre", "-umbre → la · 100 %"), ("el día", X + "-a → el"),
      ("el mapa", X + "-a → el"), ("el avión", X + "-ión → el")],
     [("la cocina", "-a → la · 95 %"), ("la puerta", "-a → la · 95 %"), ("la habitación", "-ión → la · 99 %"),
      ("la lección", "-ión → la · 99 %"), ("la universidad", "-dad → la · 100 %"), ("la edad", "-dad → la · 100 %"),
      ("el tranvía", X + "-a → el"), ("el camión", X + "-ión → el"), ("el idioma", X + "-a → el")]),
  ],
}

# Le pluriel : tableau [pluriel, regle] ; exercices [singulier, pluriel, regle, leurre, leurre].
PLURIEL = {
  "de": (
    [("die Tage", "der Tag → -e"), ("die Stühle", "der Stuhl → ¨-e"), ("die Kinder", "das Kind → -er"), ("die Häuser", "das Haus → ¨-er"),
     ("die Frauen", "die Frau → -en"), ("die Lampen", "die Lampe → -n"), ("die Autos", "das Auto → -s"), ("die Lehrer", "der Lehrer → –"),
     ("die Äpfel", "der Apfel → ¨")],
    [("der Tisch", "die Tische", "-e", "die Tischen", "die Tischer"), ("der Zug", "die Züge", "¨-e", "die Zuge", "die Zügen"),
     ("die Stadt", "die Städte", "¨-e", "die Stadte", "die Stadten"), ("das Buch", "die Bücher", "¨-er", "die Buche", "die Büchen"),
     ("das Bild", "die Bilder", "-er", "die Bilde", "die Bilds"), ("die Zeitung", "die Zeitungen", "-en", "die Zeitunge", "die Zeitungs"),
     ("die Schule", "die Schulen", "-n", "die Schules", "die Schulener"), ("das Hotel", "die Hotels", "-s", "die Hotele", "die Hoteln"),
     ("das Zimmer", "die Zimmer", "–", "die Zimmern", "die Zimmers"), ("der Vater", "die Väter", "¨", "die Vatern", "die Vaters"),
     ("die Tür", "die Türen", "-en", "die Türer", "die Türs"), ("das Handy", "die Handys", "-s", "die Handyen", "die Handye")]),
  "es": (
    [("las casas", "la casa → +s"), ("los libros", "el libro → +s"), ("los árboles", "el árbol → +es"), ("las ciudades", "la ciudad → +es"),
     ("los lápices", "el lápiz → -ces"), ("los lunes", "el lunes → ="), ("las canciones", "la canción → +es (ó → o)"),
     ("los jóvenes", "el joven → +es (o → ó)")],
    [("la casa", "las casas", "+s", "las casaes", "los casas"), ("el libro", "los libros", "+s", "los libroes", "las libros"),
     ("el sofá", "los sofás", "+s", "los sofáes", "los sofá"), ("el árbol", "los árboles", "+es", "los árbols", "los árbol"),
     ("la ciudad", "las ciudades", "+es", "las ciudads", "las ciudadas"), ("la mujer", "las mujeres", "+es", "las mujers", "las mujeras"),
     ("el hotel", "los hoteles", "+es", "los hotels", "los hotelos"), ("el lápiz", "los lápices", "-z → -ces", "los lápizes", "los lápizs"),
     ("la luz", "las luces", "-z → -ces", "las luzes", "las luzs"), ("el lunes", "los lunes", "=", "los luneses", "los lun"),
     ("la crisis", "las crisis", "=", "las crisises", "las crisisas"), ("la canción", "las canciones", "+es (ó → o)", "las canciónes", "las cancións"),
     ("el joven", "los jóvenes", "+es (o → ó)", "los jovenes", "los jóvens"), ("el autobús", "los autobuses", "+es (ú → u)", "los autobúses", "los autobús")]),
}
