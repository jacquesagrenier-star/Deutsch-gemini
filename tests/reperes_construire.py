# -*- coding: utf-8 -*-
"""Construit reperes.json (allemand) et espanol/datos/reperes.json (espagnol).

LES REPERES (v879, 19 oct. 2026). Jacques, apres son cours d'espagnol : les
jours, les mois et les nombres (jusqu'a 100, puis 1000), « tres tot dans
l'apprentissage », avec leur prononciation -- et « les nombres tout ensemble,
les mois tout ensemble, les jours tous ensemble ». D'ou cinq blocs, jamais
melanges : trois de nombres d'affilee, puis les jours, puis les mois.

Chaque bloc : t (titre), l (le tableau : [forme, sens]), a (l'astuce), x
(nombres seulement : des nombres composes pour s'exercer, hors tableau), et
p (jours et mois : des suites a dire a voix haute). Le sens d'un nombre est
le nombre en chiffres (une chaine) ; celui d'un jour ou d'un mois, un objet
par langue d'interface.

Relancer :  python tests/reperes_construire.py   (ecrit les deux fichiers)
Controle :  python tests/reperes.py
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]

def par_langue(*textes):
    assert len(textes) == len(LANGUES), textes[0]
    return dict(zip(LANGUES, textes))

JOURS = [
    ("lundi", "Monday", "Pazartesi", "понеділок", "دوشنبه", "الاثنين", "segunda-feira", "poniedziałek", "понедельник"),
    ("mardi", "Tuesday", "Salı", "вівторок", "سه‌شنبه", "الثلاثاء", "terça-feira", "wtorek", "вторник"),
    ("mercredi", "Wednesday", "Çarşamba", "середа", "چهارشنبه", "الأربعاء", "quarta-feira", "środa", "среда"),
    ("jeudi", "Thursday", "Perşembe", "четвер", "پنجشنبه", "الخميس", "quinta-feira", "czwartek", "четверг"),
    ("vendredi", "Friday", "Cuma", "п'ятниця", "جمعه", "الجمعة", "sexta-feira", "piątek", "пятница"),
    ("samedi", "Saturday", "Cumartesi", "субота", "شنبه", "السبت", "sábado", "sobota", "суббота"),
    ("dimanche", "Sunday", "Pazar", "неділя", "یکشنبه", "الأحد", "domingo", "niedziela", "воскресенье"),
]
MOIS = [
    ("janvier", "January", "Ocak", "січень", "ژانویه", "يناير", "janeiro", "styczeń", "январь"),
    ("février", "February", "Şubat", "лютий", "فوریه", "فبراير", "fevereiro", "luty", "февраль"),
    ("mars", "March", "Mart", "березень", "مارس", "مارس", "março", "marzec", "март"),
    ("avril", "April", "Nisan", "квітень", "آوریل", "أبريل", "abril", "kwiecień", "апрель"),
    ("mai", "May", "Mayıs", "травень", "مه", "مايو", "maio", "maj", "май"),
    ("juin", "June", "Haziran", "червень", "ژوئن", "يونيو", "junho", "czerwiec", "июнь"),
    ("juillet", "July", "Temmuz", "липень", "ژوئیه", "يوليو", "julho", "lipiec", "июль"),
    ("août", "August", "Ağustos", "серпень", "اوت", "أغسطس", "agosto", "sierpień", "август"),
    ("septembre", "September", "Eylül", "вересень", "سپتامبر", "سبتمبر", "setembro", "wrzesień", "сентябрь"),
    ("octobre", "October", "Ekim", "жовтень", "اکتبر", "أكتوبر", "outubro", "październik", "октябрь"),
    ("novembre", "November", "Kasım", "листопад", "نوامبر", "نوفمبر", "novembro", "listopad", "ноябрь"),
    ("décembre", "December", "Aralık", "грудень", "دسامبر", "ديسمبر", "dezembro", "grudzień", "декабрь"),
]

# v904 (21 oct. 2026) : LES COULEURS. Jacques : « on devrait apprendre les
# couleurs au debut de A1 ». Un bloc juste apres les jours. Chaque ligne porte
# sa teinte (l[2], « #rrggbb ») : le tableau la montre, on apprend en voyant.
COULEURS = [
    ("rouge", "red", "kırmızı", "червоний", "قرمز", "أحمر", "vermelho", "czerwony", "красный"),
    ("bleu", "blue", "mavi", "синій", "آبی", "أزرق", "azul", "niebieski", "синий"),
    ("vert", "green", "yeşil", "зелений", "سبز", "أخضر", "verde", "zielony", "зелёный"),
    ("jaune", "yellow", "sarı", "жовтий", "زرد", "أصفر", "amarelo", "żółty", "жёлтый"),
    ("noir", "black", "siyah", "чорний", "سیاه", "أسود", "preto", "czarny", "чёрный"),
    ("blanc", "white", "beyaz", "білий", "سفید", "أبيض", "branco", "biały", "белый"),
    ("gris", "gray", "gri", "сірий", "خاکستری", "رمادي", "cinza", "szary", "серый"),
    ("marron", "brown", "kahverengi", "коричневий", "قهوه‌ای", "بني", "marrom", "brązowy", "коричневый"),
    ("orange", "orange", "turuncu", "помаранчевий", "نارنجی", "برتقالي", "laranja", "pomarańczowy", "оранжевый"),
    ("rose", "pink", "pembe", "рожевий", "صورتی", "وردي", "rosa", "różowy", "розовый"),
    ("violet", "purple", "mor", "фіолетовий", "بنفش", "بنفسجي", "roxo", "fioletowy", "фиолетовый"),
]
TEINTES = ["#d93a32", "#2f6fd6", "#2e9e4f", "#f2c500", "#1c1c1c", "#ffffff", "#8c8c8c",
           "#7a4a24", "#f28a1a", "#f2a0c0", "#7d3fb5"]
COULEURS_MOTS = {"de": ["rot", "blau", "grün", "gelb", "schwarz", "weiß", "grau", "braun", "orange", "rosa", "lila"],
                 "es": ["rojo", "azul", "verde", "amarillo", "negro", "blanco", "gris", "marrón", "naranja", "rosa", "morado"]}

TITRES = {
    "couleurs": par_langue("Les couleurs", "Colors", "Renkler", "Кольори",
                           "رنگ‌ها", "الألوان", "As cores", "Kolory", "Цвета"),
    "n0-20": par_langue("Les nombres de 0 à 20", "Numbers from 0 to 20", "0'dan 20'ye sayılar", "Числа від 0 до 20",
                        "عددهای 0 تا 20", "الأعداد من 0 إلى 20", "Os números de 0 a 20", "Liczby od 0 do 20", "Числа от 0 до 20"),
    "n20-100": par_langue("Les dizaines, jusqu'à 100", "Tens, up to 100", "Onluklar, 100'e kadar", "Десятки, до 100",
                          "دهگان‌ها، تا 100", "العشرات حتى 100", "As dezenas, até 100", "Dziesiątki, do 100", "Десятки, до 100"),
    "n100-1000": par_langue("Les centaines, jusqu'à 1000", "Hundreds, up to 1,000", "Yüzler, 1000'e kadar", "Сотні, до 1000",
                            "صدگان‌ها، تا 1000", "المئات حتى 1000", "As centenas, até 1000", "Setki, do 1000", "Сотни, до 1000"),
    "jours": par_langue("Les jours de la semaine", "The days of the week", "Haftanın günleri", "Дні тижня",
                        "روزهای هفته", "أيام الأسبوع", "Os dias da semana", "Dni tygodnia", "Дни недели"),
    "mois": par_langue("Les mois de l'année", "The months of the year", "Yılın ayları", "Місяці року",
                       "ماه‌های سال", "أشهر السنة", "Os meses do ano", "Miesiące roku", "Месяцы года"),
}

ASTUCES = {
  "de": {
    "couleurs": par_langue(
        "Les couleurs sont des adjectifs : das Auto ist rot. Devant un nom, elles prennent une terminaison : ein rotes Auto. orange, rosa et lila ne changent jamais.",
        "Colors are adjectives: das Auto ist rot. Before a noun they take an ending: ein rotes Auto. orange, rosa and lila never change.",
        "Renkler sıfattır: das Auto ist rot. Bir isimden önce ek alırlar: ein rotes Auto. orange, rosa ve lila hiç değişmez.",
        "Кольори — це прикметники: das Auto ist rot. Перед іменником вони мають закінчення: ein rotes Auto. orange, rosa і lila ніколи не змінюються.",
        "رنگ‌ها صفت هستند: das Auto ist rot. پیش از اسم پسوند می‌گیرند: ein rotes Auto. orange، rosa و lila هیچ‌وقت تغییر نمی‌کنند.",
        "الألوان صفات: das Auto ist rot. وقبل الاسم تأخذ نهاية: ein rotes Auto. أما orange وrosa وlila فلا تتغير أبدًا.",
        "As cores são adjetivos: das Auto ist rot. Antes de um substantivo, ganham uma terminação: ein rotes Auto. orange, rosa e lila nunca mudam.",
        "Kolory to przymiotniki: das Auto ist rot. Przed rzeczownikiem dostają końcówkę: ein rotes Auto. orange, rosa i lila nigdy się nie zmieniają.",
        "Цвета — это прилагательные: das Auto ist rot. Перед существительным у них есть окончание: ein rotes Auto. orange, rosa и lila никогда не меняются."),
    "n0-20": par_langue(
        "elf et zwölf sont à part. De 13 à 19 : l'unité puis zehn (dreizehn = trois-dix). Attention : sechzehn et siebzehn perdent une lettre. Au téléphone, zwei se dit souvent zwo.",
        "elf and zwölf are special. From 13 to 19: the unit, then zehn (dreizehn = three-ten). Careful: sechzehn and siebzehn drop a letter. On the phone, zwei is often said zwo.",
        "elf ve zwölf ayrıdır. 13'ten 19'a: önce birler, sonra zehn (dreizehn = üç-on). Dikkat: sechzehn ve siebzehn bir harf kaybeder. Telefonda zwei çoğu zaman zwo denir.",
        "elf і zwölf — окремі слова. Від 13 до 19: спершу одиниці, потім zehn (dreizehn = три-десять). Увага: sechzehn і siebzehn втрачають літеру. По телефону zwei часто кажуть zwo.",
        "elf و zwölf جدا هستند. از 13 تا 19: اول یکان، بعد zehn (dreizehn = سه-ده). دقت کن: sechzehn و siebzehn یک حرف کم دارند. پشت تلفن zwei را اغلب zwo می‌گویند.",
        "elf وzwölf كلمتان خاصتان. من 13 إلى 19: الآحاد ثم zehn (dreizehn = ثلاثة-عشرة). انتبه: sechzehn وsiebzehn تفقدان حرفًا. في الهاتف تُقال zwei غالبًا zwo.",
        "elf e zwölf são à parte. De 13 a 19: a unidade, depois zehn (dreizehn = três-dez). Atenção: sechzehn e siebzehn perdem uma letra. Ao telefone, zwei costuma virar zwo.",
        "elf i zwölf są osobne. Od 13 do 19: jedności, potem zehn (dreizehn = trzy-dziesięć). Uwaga: sechzehn i siebzehn tracą literę. Przez telefon zwei mówi się często zwo.",
        "elf и zwölf — особые слова. С 13 до 19: сначала единицы, потом zehn (dreizehn = три-десять). Внимание: sechzehn и siebzehn теряют букву. По телефону zwei часто говорят zwo."),
    "n20-100": par_langue(
        "L'unité vient AVANT la dizaine, reliée par und : einundzwanzig = un-et-vingt, 21. Attention : dreißig s'écrit avec ß ; sechzig et siebzig sont raccourcis.",
        "The unit comes BEFORE the ten, joined by und: einundzwanzig = one-and-twenty, 21. Careful: dreißig has ß; sechzig and siebzig are shortened.",
        "Birler onluktan ÖNCE gelir, und ile bağlanır: einundzwanzig = bir-ve-yirmi, 21. Dikkat: dreißig ß ile yazılır; sechzig ve siebzig kısalır.",
        "Одиниці стоять ПЕРЕД десятками, через und: einundzwanzig = один-і-двадцять, 21. Увага: dreißig пишеться з ß; sechzig і siebzig скорочені.",
        "یکان پیش از دهگان می‌آید و با und وصل می‌شود: einundzwanzig = یک-و-بیست، یعنی 21. دقت کن: dreißig با ß نوشته می‌شود؛ sechzig و siebzig کوتاه شده‌اند.",
        "تأتي الآحاد قبل العشرات وتُربط بـ und: einundzwanzig = واحد-و-عشرون، أي 21. انتبه: dreißig تُكتب بـ ß، وsechzig وsiebzig مختصرتان.",
        "A unidade vem ANTES da dezena, ligada por und: einundzwanzig = um-e-vinte, 21. Atenção: dreißig se escreve com ß; sechzig e siebzig são encurtados.",
        "Jedności idą PRZED dziesiątkami, połączone und: einundzwanzig = jeden-i-dwadzieścia, 21. Uwaga: dreißig pisze się z ß; sechzig i siebzig są skrócone.",
        "Единицы идут ПЕРЕД десятками, через und: einundzwanzig = один-и-двадцать, 21. Внимание: dreißig пишется с ß; sechzig и siebzig сокращены."),
    "n100-1000": par_langue(
        "Tout s'écrit en un seul mot : dreihundertfünfundvierzig = 345. On dit hundert ou einhundert, tausend ou eintausend.",
        "It's all one word: dreihundertfünfundvierzig = 345. You can say hundert or einhundert, tausend or eintausend.",
        "Hepsi tek kelime yazılır: dreihundertfünfundvierzig = 345. hundert ya da einhundert, tausend ya da eintausend denir.",
        "Усе пишеться одним словом: dreihundertfünfundvierzig = 345. Кажуть hundert або einhundert, tausend або eintausend.",
        "همه با هم یک کلمه نوشته می‌شود: dreihundertfünfundvierzig = 345. می‌گویند hundert یا einhundert، و tausend یا eintausend.",
        "يُكتب العدد كله كلمة واحدة: dreihundertfünfundvierzig = 345. يُقال hundert أو einhundert، وtausend أو eintausend.",
        "Tudo se escreve numa só palavra: dreihundertfünfundvierzig = 345. Diz-se hundert ou einhundert, tausend ou eintausend.",
        "Wszystko pisze się jednym słowem: dreihundertfünfundvierzig = 345. Mówi się hundert albo einhundert, tausend albo eintausend.",
        "Всё пишется одним словом: dreihundertfünfundvierzig = 345. Говорят hundert или einhundert, tausend или eintausend."),
    "jours": par_langue(
        "Tous masculins : der Montag. « Lundi » (quand ?) se dit am Montag.",
        "All masculine: der Montag. “On Monday” is am Montag.",
        "Hepsi eril: der Montag. “Pazartesi günü” am Montag denir.",
        "Усі чоловічого роду: der Montag. «У понеділок» — am Montag.",
        "همه مذکرند: der Montag. «روز دوشنبه» می‌شود am Montag.",
        "كلها مذكرة: der Montag. «يوم الاثنين» تُقال am Montag.",
        "Todos masculinos: der Montag. “Na segunda-feira” se diz am Montag.",
        "Wszystkie są rodzaju męskiego: der Montag. „W poniedziałek” to am Montag.",
        "Все мужского рода: der Montag. «В понедельник» — am Montag."),
    "mois": par_langue(
        "Tous masculins : der Januar. « En janvier » se dit im Januar.",
        "All masculine: der Januar. “In January” is im Januar.",
        "Hepsi eril: der Januar. “Ocak'ta” im Januar denir.",
        "Усі чоловічого роду: der Januar. «У січні» — im Januar.",
        "همه مذکرند: der Januar. «در ژانویه» می‌شود im Januar.",
        "كلها مذكرة: der Januar. «في يناير» تُقال im Januar.",
        "Todos masculinos: der Januar. “Em janeiro” se diz im Januar.",
        "Wszystkie są rodzaju męskiego: der Januar. „W styczniu” to im Januar.",
        "Все мужского рода: der Januar. «В январе» — im Januar."),
  },
  "es": {
    "couleurs": par_langue(
        "Les couleurs en -o s'accordent : un libro rojo, una mesa roja. Les autres ne changent qu'au pluriel : una mesa azul, dos mesas azules. En Amérique latine, marrón se dit souvent café.",
        "Colors ending in -o agree: un libro rojo, una mesa roja. The others only change in the plural: una mesa azul, dos mesas azules. In Latin America, marrón is often café.",
        "-o ile biten renkler uyum yapar: un libro rojo, una mesa roja. Diğerleri yalnızca çoğulda değişir: una mesa azul, dos mesas azules. Latin Amerika'da marrón yerine çoğu zaman café denir.",
        "Кольори на -o узгоджуються: un libro rojo, una mesa roja. Інші змінюються лише в множині: una mesa azul, dos mesas azules. У Латинській Америці marrón часто кажуть café.",
        "رنگ‌هایی که به -o ختم می‌شوند مطابقت دارند: un libro rojo، una mesa roja. بقیه فقط در جمع تغییر می‌کنند: una mesa azul، dos mesas azules. در آمریکای لاتین به marrón اغلب café می‌گویند.",
        "الألوان المنتهية بـ -o تطابق الاسم: un libro rojo، una mesa roja. والبقية لا تتغير إلا في الجمع: una mesa azul، dos mesas azules. في أمريكا اللاتينية تُقال marrón غالبًا café.",
        "As cores em -o concordam: un libro rojo, una mesa roja. As outras só mudam no plural: una mesa azul, dos mesas azules. Na América Latina, marrón costuma ser café.",
        "Kolory zakończone na -o się odmieniają: un libro rojo, una mesa roja. Pozostałe zmieniają się tylko w liczbie mnogiej: una mesa azul, dos mesas azules. W Ameryce Łacińskiej marrón to często café.",
        "Цвета на -o согласуются: un libro rojo, una mesa roja. Остальные меняются только во множественном числе: una mesa azul, dos mesas azules. В Латинской Америке marrón часто называют café."),
    "n0-20": par_langue(
        "uno devient un devant un nom masculin : un libro, una mesa. De 16 à 19, un seul mot : dieciséis (dix-et-six).",
        "uno becomes un before a masculine noun: un libro, una mesa. From 16 to 19, one word: dieciséis (ten-and-six).",
        "uno, eril bir isimden önce un olur: un libro, una mesa. 16'dan 19'a tek kelime: dieciséis (on-ve-altı).",
        "uno перед іменником чоловічого роду стає un: un libro, una mesa. Від 16 до 19 — одне слово: dieciséis (десять-і-шість).",
        "uno پیش از اسم مذکر un می‌شود: un libro، una mesa. از 16 تا 19 یک کلمه است: dieciséis (ده-و-شش).",
        "uno تصبح un قبل الاسم المذكر: un libro، una mesa. من 16 إلى 19 كلمة واحدة: dieciséis (عشرة-و-ستة).",
        "uno vira un antes de um substantivo masculino: un libro, una mesa. De 16 a 19, uma só palavra: dieciséis (dez-e-seis).",
        "uno przed rzeczownikiem rodzaju męskiego to un: un libro, una mesa. Od 16 do 19 jedno słowo: dieciséis (dziesięć-i-sześć).",
        "uno перед существительным мужского рода становится un: un libro, una mesa. С 16 до 19 — одно слово: dieciséis (десять-и-шесть)."),
    "n20-100": par_langue(
        "Jusqu'à 29, un seul mot : veintiuno, veintidós. À partir de 31, trois mots avec y : treinta y uno. 100 se dit cien.",
        "Up to 29, one word: veintiuno, veintidós. From 31 on, three words with y: treinta y uno. 100 is cien.",
        "29'a kadar tek kelime: veintiuno, veintidós. 31'den itibaren y ile üç kelime: treinta y uno. 100: cien.",
        "До 29 — одне слово: veintiuno, veintidós. Від 31 — три слова з y: treinta y uno. 100 — cien.",
        "تا 29 یک کلمه است: veintiuno، veintidós. از 31 به بعد سه کلمه با y: treinta y uno. عدد 100 می‌شود cien.",
        "حتى 29 كلمة واحدة: veintiuno، veintidós. ابتداءً من 31 ثلاث كلمات مع y: treinta y uno. والعدد 100 هو cien.",
        "Até 29, uma só palavra: veintiuno, veintidós. A partir de 31, três palavras com y: treinta y uno. 100 é cien.",
        "Do 29 jedno słowo: veintiuno, veintidós. Od 31 trzy słowa z y: treinta y uno. 100 to cien.",
        "До 29 — одно слово: veintiuno, veintidós. С 31 — три слова с y: treinta y uno. 100 — cien."),
    "n100-1000": par_langue(
        "cien tout seul, mais ciento devant la suite : ciento uno. Les centaines s'accordent : doscientas personas. À part : quinientos, setecientos, novecientos. 1000 = mil.",
        "cien on its own, but ciento before more: ciento uno. Hundreds agree: doscientas personas. Irregular: quinientos, setecientos, novecientos. 1000 = mil.",
        "Tek başına cien, devamı varsa ciento: ciento uno. Yüzler uyum yapar: doscientas personas. Düzensiz: quinientos, setecientos, novecientos. 1000 = mil.",
        "Окремо — cien, але ciento, коли далі є число: ciento uno. Сотні узгоджуються: doscientas personas. Неправильні: quinientos, setecientos, novecientos. 1000 = mil.",
        "به‌تنهایی cien، ولی اگر عددی بعدش بیاید ciento: ciento uno. صدگان‌ها مطابقت دارند: doscientas personas. بی‌قاعده: quinientos، setecientos، novecientos. 1000 = mil.",
        "وحدها cien، لكن ciento إذا تلاها عدد: ciento uno. المئات تطابق الاسم: doscientas personas. شاذة: quinientos، setecientos، novecientos. و1000 = mil.",
        "cien sozinho, mas ciento antes de mais números: ciento uno. As centenas concordam: doscientas personas. Irregulares: quinientos, setecientos, novecientos. 1000 = mil.",
        "Samo cien, ale ciento, gdy coś następuje: ciento uno. Setki się odmieniają: doscientas personas. Nieregularne: quinientos, setecientos, novecientos. 1000 = mil.",
        "Отдельно — cien, но ciento, если дальше есть число: ciento uno. Сотни согласуются: doscientas personas. Неправильные: quinientos, setecientos, novecientos. 1000 = mil."),
    "jours": par_langue(
        "Sans majuscule, et masculins : el lunes. « Lundi » (quand ?) se dit el lunes, sans préposition.",
        "No capital letter, and masculine: el lunes. “On Monday” is just el lunes.",
        "Büyük harfle yazılmaz ve erildir: el lunes. “Pazartesi günü” sadece el lunes denir.",
        "Без великої літери, чоловічого роду: el lunes. «У понеділок» — просто el lunes.",
        "با حرف کوچک نوشته می‌شوند و مذکرند: el lunes. «روز دوشنبه» فقط el lunes است.",
        "تُكتب بحرف صغير وهي مذكرة: el lunes. «يوم الاثنين» تُقال el lunes فقط.",
        "Sem maiúscula, e masculinos: el lunes. “Na segunda-feira” é só el lunes.",
        "Małą literą i rodzaju męskiego: el lunes. „W poniedziałek” to po prostu el lunes.",
        "Со строчной буквы, мужского рода: el lunes. «В понедельник» — просто el lunes."),
    "mois": par_langue(
        "Sans majuscule : enero, febrero. « En janvier » se dit en enero.",
        "No capital letter: enero, febrero. “In January” is en enero.",
        "Büyük harfle yazılmaz: enero, febrero. “Ocak'ta” en enero denir.",
        "Без великої літери: enero, febrero. «У січні» — en enero.",
        "با حرف کوچک: enero، febrero. «در ژانویه» می‌شود en enero.",
        "بحرف صغير: enero، febrero. «في يناير» تُقال en enero.",
        "Sem maiúscula: enero, febrero. “Em janeiro” se diz en enero.",
        "Małą literą: enero, febrero. „W styczniu” to en enero.",
        "Со строчной буквы: enero, febrero. «В январе» — en enero."),
  },
}

NOMBRES = {
  "de": {
    "n0-20": ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
              "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig"],
    "n20-100": [("zwanzig", 20), ("einundzwanzig", 21), ("zweiundzwanzig", 22), ("dreißig", 30), ("vierzig", 40),
                ("fünfzig", 50), ("sechzig", 60), ("siebzig", 70), ("achtzig", 80), ("neunzig", 90), ("hundert", 100)],
    "x20-100": [("dreiundzwanzig", 23), ("einunddreißig", 31), ("fünfunddreißig", 35), ("dreiundvierzig", 43),
                ("siebenundvierzig", 47), ("achtundfünfzig", 58), ("vierundsechzig", 64), ("sechsundsiebzig", 76),
                ("neunundachtzig", 89), ("zweiundneunzig", 92)],
    "n100-1000": [("hundert", 100), ("zweihundert", 200), ("dreihundert", 300), ("vierhundert", 400), ("fünfhundert", 500),
                  ("sechshundert", 600), ("siebenhundert", 700), ("achthundert", 800), ("neunhundert", 900), ("tausend", 1000)],
    "x100-1000": [("hunderteins", 101), ("hundertzwanzig", 120), ("zweihundertfünfzig", 250), ("dreihundertfünfundvierzig", 345),
                  ("fünfhundertfünf", 505), ("sechshundertachtzig", 680), ("siebenhundertzwölf", 712), ("neunhundertneunundneunzig", 999)],
  },
  "es": {
    "n0-20": ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
              "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"],
    "n20-100": [("veinte", 20), ("veintiuno", 21), ("veintidós", 22), ("treinta", 30), ("treinta y uno", 31), ("cuarenta", 40),
                ("cincuenta", 50), ("sesenta", 60), ("setenta", 70), ("ochenta", 80), ("noventa", 90), ("cien", 100)],
    "x20-100": [("veintitrés", 23), ("veintiséis", 26), ("treinta y cinco", 35), ("cuarenta y tres", 43), ("cuarenta y siete", 47),
                ("cincuenta y ocho", 58), ("sesenta y cuatro", 64), ("setenta y seis", 76), ("ochenta y nueve", 89), ("noventa y dos", 92)],
    "n100-1000": [("cien", 100), ("doscientos", 200), ("trescientos", 300), ("cuatrocientos", 400), ("quinientos", 500),
                  ("seiscientos", 600), ("setecientos", 700), ("ochocientos", 800), ("novecientos", 900), ("mil", 1000)],
    "x100-1000": [("ciento uno", 101), ("ciento veinte", 120), ("doscientos cincuenta", 250), ("trescientos cuarenta y cinco", 345),
                  ("quinientos cinco", 505), ("seiscientos ochenta", 680), ("setecientos doce", 712), ("novecientos noventa y nueve", 999)],
  },
}
JOURS_MOTS = {"de": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
              "es": ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
MOIS_MOTS = {"de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
             "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]}

def suites(mots, sens, tailles):
    """Des suites a dire a voix haute : [[texte, sens par langue], ...]."""
    out, i = [], 0
    for n in tailles:
        morceau = list(range(i, i + n))
        out.append([", ".join(mots[k] for k in morceau),
                    {lg: ", ".join(sens[k][j] for k in morceau) for j, lg in enumerate(LANGUES)}])
        i += n
    return out

def construire(langue):
    N = NOMBRES[langue]
    reperes = []
    reperes.append({"id": "n0-20", "type": "nombre", "t": TITRES["n0-20"], "a": ASTUCES[langue]["n0-20"],
                    "l": [[m, str(i)] for i, m in enumerate(N["n0-20"])], "x": []})
    reperes.append({"id": "n20-100", "type": "nombre", "t": TITRES["n20-100"], "a": ASTUCES[langue]["n20-100"],
                    "l": [[m, str(v)] for m, v in N["n20-100"]], "x": [[m, str(v)] for m, v in N["x20-100"]]})
    reperes.append({"id": "n100-1000", "type": "nombre", "t": TITRES["n100-1000"], "a": ASTUCES[langue]["n100-1000"],
                    "l": [[m, str(v)] for m, v in N["n100-1000"]], "x": [[m, str(v)] for m, v in N["x100-1000"]]})
    jours = [par_langue(*s) for s in JOURS]
    reperes.append({"id": "jours", "type": "suite", "t": TITRES["jours"], "a": ASTUCES[langue]["jours"],
                    "l": [[m, jours[i]] for i, m in enumerate(JOURS_MOTS[langue])],
                    "p": suites(JOURS_MOTS[langue], JOURS, [3, 4])})
    couleurs = [par_langue(*s) for s in COULEURS]
    reperes.append({"id": "couleurs", "type": "couleur", "t": TITRES["couleurs"], "a": ASTUCES[langue]["couleurs"],
                    "l": [[m, couleurs[i], TEINTES[i]] for i, m in enumerate(COULEURS_MOTS[langue])]})
    mois = [par_langue(*s) for s in MOIS]
    reperes.append({"id": "mois", "type": "suite", "t": TITRES["mois"], "a": ASTUCES[langue]["mois"],
                    "l": [[m, mois[i]] for i, m in enumerate(MOIS_MOTS[langue])],
                    "p": suites(MOIS_MOTS[langue], MOIS, [4, 4, 4])})
    # v880 : l'alphabet, le genre, le pluriel (voir reperes_suite.py).
    import reperes_suite as rs
    # v882 : la prononciation sous chaque nombre espagnol (3e element, par langue d'interface).
    if langue == "es":
        for r in reperes:
            if r["type"] == "nombre":
                for l in r["l"]:
                    pr = rs.PRONONCIATION_NOMBRES_ES_FR.get(l[0])
                    if pr:
                        l.append({"fr": pr})
    reperes.append({"id": "alphabet", "type": "lettre", "t": rs.TITRES["alphabet"], "a": rs.ASTUCES[langue]["alphabet"],
                    "l": [[nom, lettre, conf] for lettre, nom, conf in rs.ALPHABET[langue]],
                    "p": [[s, mot] for s, mot in rs.EPELER[langue]]})
    for id_, l, x in rs.GENRE[langue]:
        reperes.append({"id": id_, "type": "genre", "t": rs.TITRES[id_], "a": rs.ASTUCES[langue][id_],
                        "l": [list(e) for e in l], "x": [list(e) for e in x]})
    reperes.append({"id": "pluriel", "type": "pluriel", "t": rs.TITRES["pluriel"], "a": rs.ASTUCES[langue]["pluriel"],
                    "l": [list(e) for e in rs.PLURIEL[langue][0]], "x": [list(e) for e in rs.PLURIEL[langue][1]]})
    return {
        "_lisez_moi": [
            "Les repères (v879-v880, v904) : nombres, jours, couleurs, mois, alphabet, genre, pluriel, très tôt dans la séance du jour. Fichier DÉRIVÉ : le refaire avec python tests/reperes_construire.py, jamais à la main.",
            "Blocs dans l'ordre, jamais mélangés. type « nombre » : sens = le nombre en chiffres ; x = nombres composés pour s'exercer. type « suite » : sens par langue ; p = suites à dire à voix haute. type « couleur » : [mot, sens par langue, teinte #rrggbb]. type « lettre » : [nom dit, lettre, lettres qui se confondent] ; p = [épellation dite, mot]. type « genre » : [mot avec article, règle] (« ⚠️ » = exception) ; x = mots pour s'exercer. type « pluriel » : l = [pluriel, règle] ; x = [singulier, pluriel, règle, leurre, leurre].",
            "Les pourcentages du genre sont MESURÉS sur les noms de nos thèmes (19 oct. 2026), pas recopiés d'une grammaire.",
            "Contrôle : python tests/reperes.py.",
        ],
        "reperes": reperes,
    }

def ecrire(chemin, d):
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")

if __name__ == "__main__":
    ecrire(os.path.join(RACINE, "reperes.json"), construire("de"))
    ecrire(os.path.join(RACINE, "espanol", "datos", "reperes.json"), construire("es"))
    print("reperes.json et espanol/datos/reperes.json ecrits")
