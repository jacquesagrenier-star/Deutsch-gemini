# -*- coding: utf-8 -*-
"""La tuile « Prononciation » : les regles de lecture de l'allemand.

    python tests/prononciation.py            # controle seul
    python tests/prononciation.py --ecrire   # ecrit prononciation.json

POURQUOI UNE TUILE ET PAS UNE TRANSCRIPTION SUR CHAQUE CARTE (11 oct. 2026).
Suggestion de Hatice (son mari debute) : « que la prononciation des mots soit
indiquee ». Une transcription par mot serait illisible en API pour un
debutant, et une transcription « a la francaise » ne sert a rien a un Turc :
il en faudrait six, sur 7 000 mots. Or l'allemand se lit presque toujours
comme il s'ecrit : vingt-cinq regles suffisent pour lire n'importe quel mot.

CHAQUE REGLE PARLE A LA LANGUE DE L'UTILISATEUR (demande de Jacques) : le
rapprochement change d'une langue a l'autre -- sch = ş en turc, ш en
ukrainien, ش en persan et en arabe ; ch apres a = х, خ ; et les pieges
propres a chacun (w n'est PAS le و arabe, j n'est PAS le j turc). Les textes
tr / uk / fa / ar sont a faire relire par nos testeurs de ces langues.

LES EXEMPLES SONT DES MOTS DU CORPUS, DEJA ENREGISTRES PAR AURORA : leurs
traductions viennent du corpus (texteTraduit dans l'app, repli compris pour
l'arabe), et le script refuse un exemple sans fichier audio/mp3/<sha1>.mp3.
Rien a generer, rien a deposer.
"""
import hashlib, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = ("fr", "en", "tr", "uk", "fa", "ar", "pt")


def guillemets(t):
    """« x » -> “x” : l'anglais et le turc n'emploient pas les chevrons."""
    return re.sub(r"«\s*(.*?)\s*»", "“\\1”", t)


def L(fr, en, tr, uk, fa, ar):
    return {"fr": fr, "en": guillemets(en), "tr": guillemets(tr), "uk": uk, "fa": fa, "ar": ar}


# (id, graphie, api, court, explication, exemples)
VOYELLES = [
 ("u-trema", "ü", "[y]",
  L("comme le « u » français", "« ee » with rounded lips", "Türkçedeki ü", "«і» з округленими губами", "«ای» با لب‌های گرد", "«ي» بشفتين مستديرتين"),
  L("Le ü se prononce exactement comme le « u » français de « tu » ou « mur ».",
    "English has no ü: say « ee » and round your lips as if to whistle, without moving your tongue.",
    "Almanca ü, Türkçedeki ü ile aynıdır: « gül », « tüy ».",
    "В українській такого звука немає: скажи «і» і, не рухаючи язиком, витягни губи трубочкою.",
    "در فارسی چنین صدایی نیست: «ای» بگو و بی‌آنکه زبانت را تکان دهی، لب‌هایت را مثل سوت زدن گرد کن.",
    "لا يوجد هذا الصوت في العربية: انطق «ي» (إي) ثم دوّر شفتيك كأنك تصفّر، دون أن تحرّك لسانك."),
  ["müde", "Tür", "Brücke"]),
 ("o-trema", "ö", "[ø]",
  L("comme « eu »", "« e » with rounded lips", "Türkçedeki ö", "«е» з округленими губами", "«اِ» با لب‌های گرد", "صوت e بشفتين مستديرتين"),
  L("Le ö se prononce comme « eu » dans « peu » ou « fleur ».",
    "No English equivalent: say the « e » of « bed » (or « ay » for a long ö) with your lips rounded.",
    "Almanca ö, Türkçedeki ö ile aynıdır: « göz », « söz ».",
    "Такого звука немає: скажи «е» і, не рухаючи язиком, округли губи.",
    "در فارسی نیست: «اِ» (مثل «مِهر») بگو و لب‌هایت را گرد کن.",
    "ليس في العربية: انطق صوت e (كما في الإنجليزية bed) مع تدوير الشفتين."),
  ["schön", "hören", "Löffel"]),
 ("a-trema", "ä", "[ɛ]",
  L("comme « è »", "« e » as in bed", "açık e", "як «е»", "مثل «اِ»", "مثل e في bed"),
  L("Le ä se prononce « è », comme dans « mère » ou « fête ».",
    "ä sounds like the « e » in « bed » — longer in Käse, shorter in Mädchen.",
    "ä, « ev » ve « el » kelimelerindeki e gibidir, biraz daha açık.",
    "ä звучить як українське «е»: «день», «село».",
    "ä مانند «اِ» فارسی است: «مِهر»، «دِل».",
    "ä صوت e مفتوح، كما في الكلمة الإنجليزية bed."),
  ["Käse", "spät", "Mädchen"]),
 ("u", "u", "[u]",
  L("comme « ou »", "« oo » as in food", "Türkçedeki u", "як «у»", "مثل «او»", "مثل «ـُو»"),
  L("Le u allemand se dit « ou » : gut se prononce « gout ». Jamais le « u » français, qui s'écrit ü.",
    "u is « oo » as in « food » (long) or « put » (short).",
    "u, Türkçedeki u ile aynıdır: « uzun », « bulut ».",
    "u — це українське «у»: «жук», «рука».",
    "u مانند «او» فارسی است: «دوست»، «نور».",
    "u مثل الضمة الطويلة «ـُو»: «نُور»، «سُور»."),
  ["gut", "Buch", "Hund"]),
 ("ei", "ei", "[aɪ]",
  L("« aï », jamais « è »", "« i » as in wine", "« ay » gibi", "як «ай»", "«اَی»، نه «ای»", "مثل «ـَيْ» في بَيْت"),
  L("ei se prononce « aï », comme dans « aïe » : Wein se dit « vaïn ». Le piège du francophone : le lire « è ».",
    "ei sounds like « i » in « wine » or « my »: Wein rhymes with English « vine ».",
    "ei, Türkçedeki « ay » gibi okunur: « ay », « bayram ». Wein → « vayn ».",
    "ei читається як «ай»: «чай», «край». Wein → «вайн».",
    "ei را «ای» نخوان؛ «اَی» بخوان، مانند «وای!»: Wein ≈ «وایْن».",
    "تُنطق ei «ـَيْ» كما في «بَيْت» و«عَيْن»: Wein ≈ «ڤَيْن»."),
  ["Wein", "klein", "Eis"]),
 ("ie", "ie", "[iː]",
  L("« i » long", "« ee » as in see", "uzun i", "довге «і»", "«ای» کشیده", "«ـِي» طويلة"),
  L("ie se prononce comme un « i » long : Liebe se dit « liibe ». Le e ne s'entend pas.",
    "ie is a long « ee » as in « see »: Liebe sounds like « leeb-uh ».",
    "ie uzun bir i olarak okunur, e okunmaz: Liebe → « liibe ».",
    "ie — це довге «і», «е» не вимовляється: Liebe → «ліібе».",
    "ie یک «ای» کشیده است و e خوانده نمی‌شود: Liebe ≈ «لیبه».",
    "ie ياء ممدودة «ـِي» ولا يُنطق الـ e: Liebe ≈ «ليبه»."),
  ["Liebe", "spielen", "Bier"]),
 ("eu", "eu · äu", "[ɔʏ]",
  L("« oï »", "« oy » as in boy", "« oy » gibi", "як «ой»", "مثل «اُی»", "مثل oy في boy"),
  L("eu et äu se prononcent « oï » : heute se dit « hoïte », neu se dit « noï ».",
    "eu and äu sound like « oy » in « boy »: neu sounds like « noy ».",
    "eu ve äu « oy » gibi okunur: « koy », « boy ». neu → « noy », heute → « hoyte ».",
    "eu і äu читаються як «ой»: neu → «ной», heute → «гойте».",
    "eu و äu را «اُی» بخوان: neu ≈ «نُوی»، heute ≈ «هُویته».",
    "تُنطق eu وäu مثل oy في الإنجليزية boy: neu ≈ «نوي»."),
  ["neu", "heute", "träumen"]),
 ("au", "au", "[aʊ]",
  L("« aou »", "« ow » as in now", "a ve u birlikte", "як «ау» в «пауза»", "«آ» و «او» با هم", "مثل «ـَوْ» في يَوْم"),
  L("au se prononce « aou », comme dans « miaou » : Haus se dit « haouss ».",
    "au sounds like « ow » in « now »: Haus sounds like « house ».",
    "au, a ile u'nun tek hecede birleşmesidir: Haus → « haus », Frau → « frau ».",
    "au — це «ау» в одному складі, як у слові «пауза»: Haus → «гаус».",
    "au یعنی «آ» و «او» با هم در یک هجا: Haus ≈ «هاوس».",
    "تُنطق au «ـَوْ» كما في «يَوْم» و«لَوْن»: Haus ≈ «هَوْس»."),
  ["Haus", "Frau", "Bauch"]),
 ("longueur", "Tee · Bett", "[eː] · [ɛ]",
  L("voyelle longue ou brève", "long or short vowel", "uzun mu, kısa mı", "довгий чи короткий", "کشیده یا کوتاه", "حركة طويلة أم قصيرة"),
  L("Une voyelle est longue devant un h ou quand elle est doublée (Tee, Sohn), brève devant une consonne double (Bett, kommen). En français la longueur ne compte guère ; en allemand, elle change le mot.",
    "A vowel is long before h or when doubled (Tee, Sohn), short before a double consonant (Bett, kommen). The length can change the meaning.",
    "Ünlü, h'den önce ya da çift yazıldığında uzundur (Tee, Sohn); çift ünsüzden önce kısadır (Bett, kommen). Almancada uzunluk anlamı değiştirebilir.",
    "Голосний довгий перед h або коли подвоєний (Tee, Sohn), короткий перед подвоєним приголосним (Bett, kommen). В українській довжини немає, а в німецькій вона змінює слово.",
    "واکه پیش از h یا وقتی دوتایی نوشته شود کشیده است (Tee، Sohn) و پیش از همخوانِ دوتایی کوتاه (Bett، kommen). در آلمانی کشیدگی می‌تواند معنا را عوض کند.",
    "تكون الحركة طويلة قبل h أو إذا تكرّرت (Tee، Sohn)، وقصيرة قبل الحرف المضعّف (Bett، kommen) — كالفرق بين الفتحة والألف في العربية."),
  ["Tee", "Bett", "Sohn", "kommen"]),
]

CONSONNES = [
 ("sch", "sch", "[ʃ]",
  L("comme « ch »", "« sh »", "ş", "ш", "ش", "ش"),
  L("sch se prononce comme le « ch » de « chat » : Schule se dit « choule ».",
    "sch is English « sh »: Schule sounds like « shoo-luh ».",
    "sch, Türkçedeki ş'dir: Schule → « şule », Fisch → « fiş ».",
    "sch — це українське «ш»: Schule → «шуле», Fisch → «фіш».",
    "sch همان «ش» فارسی است: Schule ≈ «شوله»، Fisch ≈ «فیش».",
    "sch هو حرف «ش»: Schule ≈ «شوله»، Fisch ≈ «فيش»."),
  ["Schule", "Fisch", "schön"]),
 ("sp-st", "sp · st", "[ʃp] · [ʃt]",
  L("« chp », « cht » en début de mot", "« shp », « sht » at the start", "kelime başında şp, şt", "на початку слова: шп, шт", "در آغاز واژه: شپ، شت", "في أول الكلمة: شپ، شت"),
  L("Au début d'un mot (ou d'une partie de mot), sp et st se disent « chp » et « cht » : Straße se dit « chtrasse », sprechen « chprèchen ».",
    "At the start of a word, sp and st sound « shp » and « sht »: Straße sounds like « shtrah-suh ».",
    "Kelime başında sp ve st, « şp » ve « şt » okunur: Straße → « ştrase », sprechen → « şprehen ».",
    "На початку слова sp і st читаються «шп» і «шт»: Straße → «штрасе», sprechen → «шпрехен».",
    "در آغاز واژه، sp و st را «شپ» و «شت» بخوان: Straße ≈ «شتراسه»، sprechen ≈ «شپرِخِن».",
    "في أول الكلمة تُنطق sp وst «شپ» و«شت»: Straße ≈ «شتراسه»، sprechen ≈ «شپريخن»."),
  ["Straße", "sprechen", "Sport"]),
 ("ch-doux", "ch (ich)", "[ç]",
  L("un souffle doux, sans équivalent", "like the h in huge", "« hiç »teki h gibi", "м'яке «хь»", "«خ» خیلی نرم", "أخفّ بكثير من «خ»"),
  L("Après e, i, ä, ö, ü, ei, eu, l, n ou r, ch est un souffle doux, la langue contre le palais, comme un « ch » chuchoté en souriant : Milch, leicht. Le son n'existe pas en français ; dire « ch » se comprend, mais ce n'est pas juste.",
    "After e, i, ä, ö, ü, ei, eu, l, n or r, ch is like the « h » at the start of « huge », said more strongly: Milch, leicht.",
    "e, i, ä, ö, ü, ei, eu, l, n ya da r'den sonra ch, « hiç » kelimesindeki h gibidir: Milch → « milh », leicht → « layht ».",
    "Після e, i, ä, ö, ü, ei, eu, l, n, r звук ch м'який: як «хь» у слові «хіба», сказане дуже легко, язик біля піднебіння: Milch, leicht.",
    "پس از e، i، ä، ö، ü، ei، eu، l، n یا r، صدای ch مثل «خ» است اما خیلی نرم‌تر، با زبانی نزدیک به سقف دهان: Milch، leicht.",
    "بعد e وi وä وö وü وei وeu وl وn وr يكون ch نَفَسًا ناعمًا قريبًا من سقف الحلق، أخفّ بكثير من «خ»، مثل h في الإنجليزية huge: Milch، leicht."),
  ["Milch", "leicht", "Küche"]),
 ("ch-dur", "ch (ach)", "[x]",
  L("raclé, comme la jota espagnole", "as in Scottish loch", "boğazdan sert h", "як «х»", "«خ»", "«خ»"),
  L("Après a, o, u et au, ch est un raclement au fond de la gorge, comme la jota espagnole : Nacht, Buch, Bauch.",
    "After a, o, u and au, ch is the sound in Scottish « loch »: Nacht, Buch.",
    "a, o, u ve au'dan sonra ch, boğazdan çıkan sert, hırıltılı bir h'dir: Nacht, Buch. Türkçede tam karşılığı yok.",
    "Після a, o, u, au звук ch — це українське «х»: «хата», «дух». Nacht → «нахт», Buch → «бух».",
    "پس از a، o، u و au، ch همان «خ» فارسی است: Nacht ≈ «ناخت»، Buch ≈ «بوخ».",
    "بعد a وo وu وau يكون ch هو حرف «خ»: Nacht ≈ «ناخت»، Buch ≈ «بوخ»."),
  ["Nacht", "kochen", "Bauch"]),
 ("z", "z · tz", "[ts]",
  L("« ts »", "« ts » as in cats", "« ts »", "ц", "«تس»", "«تس»"),
  L("z (et tz) se prononce toujours « ts » : Zeit se dit « tsaït », Katze « katse ».",
    "z is always « ts » as in « cats »: Zeit sounds like « tsite ».",
    "z her zaman « ts » okunur, Türkçedeki z gibi değil: Zeit → « tsayt », Katze → « katse ».",
    "z — це українське «ц»: Zeit → «цайт», Katze → «катце».",
    "z همیشه «تس» خوانده می‌شود، نه «ز»: Zeit ≈ «تسایت»، Katze ≈ «کاتسه».",
    "تُنطق z دائمًا «تس» وليست «ز»: Zeit ≈ «تسايت»، Katze ≈ «كاتسه»."),
  ["Zeit", "Zug", "Katze"]),
 ("v", "v", "[f]",
  L("le plus souvent « f »", "usually « f »", "çoğunlukla f", "здебільшого «ф»", "بیشتر «ف»", "غالبًا «ف»"),
  L("v se prononce presque toujours « f » : Vater se dit « fater », viel « fil ». Quelques mots venus d'ailleurs gardent le « v » (Vase, Klavier).",
    "v is almost always « f »: Vater sounds like « fah-ter ». A few borrowed words keep « v » (Vase, Klavier).",
    "v neredeyse her zaman f okunur: Vater → « fater », viel → « fil ». Yabancı kökenli birkaç kelime v'yi korur (Vase, Klavier).",
    "v майже завжди читається «ф»: Vater → «фатер», viel → «філ». Кілька запозичених слів зберігають «в» (Vase, Klavier).",
    "v تقریباً همیشه «ف» خوانده می‌شود: Vater ≈ «فاتِر»، viel ≈ «فیل». چند واژهٔ وام‌گرفته «و» را نگه می‌دارند (Vase، Klavier).",
    "تُنطق v «ف» في أغلب الكلمات: Vater ≈ «فاتر»، viel ≈ «فيل». وتبقى «ڤ» في بعض الكلمات الدخيلة (Vase، Klavier)."),
  ["Vater", "Vogel", "viel"]),
 ("w", "w", "[v]",
  L("« v »", "« v », never « w »", "v", "в", "«و» مثل «ورزش»", "ڤ، وليست «و»"),
  L("w se prononce « v » : Wasser se dit « vasser », wo « vo ».",
    "w is English « v », never « w »: Wasser sounds like « vasser ».",
    "w, Türkçedeki v gibi okunur: Wasser → « vaser », wo → « vo ».",
    "w читається як «в» (зуби на нижній губі): Wasser → «васер», wo → «во».",
    "w همان «و» فارسی در «ورزش» است: Wasser ≈ «واسِر»، wo ≈ «وُ».",
    "w ليست «و» العربية: إنها «ڤ» (v)، كما في الإنجليزية very: Wasser ≈ «ڤاسر»، wo ≈ «ڤو»."),
  ["Wasser", "Woche", "wo"]),
 ("s", "s", "[z]",
  L("« z » devant une voyelle", "« z » before a vowel", "ünlüden önce z", "«з» перед голосним", "پیش از واکه «ز»", "«ز» قبل الحركة"),
  L("Devant une voyelle, s se dit « z » : Sonne se dit « zonne », Hose « hoze ».",
    "Before a vowel, s sounds like « z »: Sonne sounds like « zonn-uh ».",
    "Ünlüden önce s, z okunur: Sonne → « zone », sagen → « zagen ».",
    "Перед голосним s читається як «з»: Sonne → «зоне», sagen → «заген».",
    "پیش از واکه، s را «ز» بخوان: Sonne ≈ «زونه»، sagen ≈ «زاگِن».",
    "قبل الحركة تُنطق s «ز»: Sonne ≈ «زونه»، Hose ≈ «هوزه»."),
  ["Sonne", "sagen", "Hose"]),
 ("eszett", "ß · ss", "[s]",
  L("« s » dur", "a sharp « s »", "s", "с", "«س»", "«س»"),
  L("ß et ss se prononcent « s » dur, comme dans « poisson ». ß suit une voyelle longue (groß), ss une voyelle brève (essen).",
    "ß and ss are a sharp « s » as in « see ». ß follows a long vowel (groß), ss a short one (essen).",
    "ß ve ss, Türkçedeki s gibidir. ß uzun ünlüden (groß), ss kısa ünlüden sonra gelir (essen).",
    "ß і ss — це «с». ß стоїть після довгого голосного (groß), ss — після короткого (essen).",
    "ß و ss همان «س» هستند. ß پس از واکهٔ کشیده می‌آید (groß) و ss پس از واکهٔ کوتاه (essen).",
    "ß وss تُنطقان «س». تأتي ß بعد حركة طويلة (groß)، وss بعد حركة قصيرة (essen)."),
  ["groß", "essen", "Straße"]),
 ("j", "j", "[j]",
  L("« y »", "« y » as in yes", "y, j değil", "й", "«ی»", "«ي»"),
  L("j se prononce « y » : Jahr se dit « yar », jung « youngue ».",
    "j is English « y »: Jahr sounds like « yar », jung like « young ».",
    "j, Türkçedeki y gibi okunur, j gibi değil: Jahr → « yar », jung → « yung ».",
    "j читається як «й»: Jahr → «яр», jung → «юнг».",
    "j را «ی» بخوان: Jahr ≈ «یار»، jung ≈ «یونگ».",
    "تُنطق j «ي»: Jahr ≈ «يار»، jung ≈ «يونغ»."),
  ["Jahr", "jung"]),
 ("h", "h", "[h]",
  L("soufflé au début, muet après une voyelle", "breathed at the start, silent after a vowel", "başta okunur, ünlüden sonra okunmaz", "на початку — видих, після голосного — німий", "در آغاز «ه»، پس از واکه خاموش", "«هـ» في البداية، صامتة بعد الحركة"),
  L("Au début d'un mot ou d'une syllabe, h est un vrai souffle, jamais muet comme en français : Hund. Après une voyelle, il ne se prononce pas et allonge la voyelle : gehen, Uhr.",
    "At the start of a word, h is breathed as in « house »: Hund. After a vowel it is silent and makes the vowel long: gehen, Uhr.",
    "Kelime başında h okunur: Hund. Ünlüden sonra okunmaz, ünlüyü uzatır: gehen → « geen », Uhr → « uur ».",
    "На початку слова h — легкий видих, як «г» без голосу: Hund. Після голосного h не читається, а подовжує голосний: gehen, Uhr.",
    "در آغاز واژه h همان «ه» است: Hund. پس از واکه خوانده نمی‌شود و واکه را کشیده می‌کند: gehen، Uhr.",
    "في أول الكلمة h هي «هـ»: Hund. وبعد الحركة لا تُنطق، بل تمدّ الحركة: gehen، Uhr."),
  ["Hund", "gehen", "Uhr"]),
 ("r", "r", "[ʁ]",
  L("au fond de la gorge, comme en français", "from the throat", "boğazdan", "горлове", "نزدیک «غ»", "قريب من «غ»"),
  L("Le r allemand se fait au fond de la gorge, comme le « r » français : rot, Brot. Rien à changer !",
    "The German r is made at the back of the throat, like a French r: rot, Brot. An English r would sound foreign.",
    "Almanca r genellikle boğazdan, Fransızca r gibi söylenir: rot, Brot. Türkçe r de anlaşılır, ama yabancı duyulur.",
    "Німецьке r зазвичай вимовляють у горлі, як французьке. Українське «р» з дрижанням теж зрозуміють, але воно звучить по-іноземному.",
    "r آلمانی از ته گلو ادا می‌شود و به «غ» فارسی نزدیک است: rot، Brot. «ر» فارسی هم فهمیده می‌شود، اما خارجی به گوش می‌رسد.",
    "تُنطق r الألمانية من الحلق، وهي قريبة جدًا من «غ»: rot، Brot. والراء العربية مفهومة أيضًا، لكنها تبدو أجنبية."),
  ["rot", "Brot"]),
 ("pf", "pf", "[pf]",
  L("p + f d'un seul coup", "p and f together", "p ve f birlikte", "п + ф разом", "«پ» و «ف» با هم", "p و«ف» معًا"),
  L("pf se prononce p et f d'un seul coup ; les deux s'entendent : Apfel, Kopf.",
    "pf: say p and f together, both are heard: Apfel, Kopf.",
    "pf: p ve f tek seste birlikte okunur, ikisi de duyulur: Apfel → « apfel ».",
    "pf: «п» і «ф» разом, чути обидва: Apfel → «апфель», Kopf → «копф».",
    "pf را «پ» و «ف» با هم بخوان، هر دو شنیده می‌شوند: Apfel ≈ «اَپفِل»، Kopf ≈ «کُپف».",
    "pf: يُنطق p و«ف» معًا، ويُسمع الاثنان: Apfel، Kopf. (p هي «پ»: باء بلا صوت.)"),
  ["Apfel", "Kopf", "Pferd"]),
]

FINS = [
 ("er-final", "-er", "[ɐ]",
  L("un « a » léger", "a soft « uh »", "hafif bir a", "легке «а»", "«اَ» کوتاه", "فتحة خفيفة"),
  L("À la fin d'un mot, -er se dit comme un « a » léger, sans « r » : Vater ≈ « fata », Mutter ≈ « mouta ».",
    "At the end of a word, -er is a soft « uh », with no r, as in British « father »: Vater, Mutter.",
    "Kelime sonunda -er, r'siz hafif bir a gibidir: Vater ≈ « fata », Mutter ≈ « muta ».",
    "У кінці слова -er звучить як легке «а», без «р»: Vater ≈ «фата», Mutter ≈ «мута».",
    "در پایان واژه، -er مانند یک «اَ» کوتاه و بی «ر» است: Vater ≈ «فاتا»، Mutter ≈ «موتا».",
    "في آخر الكلمة تُنطق -er كفتحة خفيفة بلا راء: Vater ≈ «فاتا»، Mutter ≈ «موتا»."),
  ["Vater", "Mutter", "Fenster"]),
 ("ig-final", "-ig", "[ɪç]",
  L("« -ich », avec le ch doux", "« -ich », with the soft ch", "« -ih »", "«-іх» з м'яким «х»", "«-ایخ» با «خ» نرم", "«-يخ» بخاء ناعمة"),
  L("À la fin d'un mot, -ig se dit « -ich », avec le ch doux de Milch : richtig, billig.",
    "At the end of a word, -ig is said « -ich », with the soft ch of Milch: richtig, billig.",
    "Kelime sonunda -ig, « -ih » diye okunur (« hiç »teki h gibi): richtig → « rihtih », billig → « bilih ».",
    "У кінці слова -ig читається «-іх» з м'яким «х», як у Milch: richtig, billig.",
    "در پایان واژه، -ig را «-ایخ» با «خ» نرم (مثل Milch) بخوان: richtig، billig.",
    "في آخر الكلمة تُنطق -ig «-يخ» بخاء ناعمة كما في Milch: richtig، billig."),
  ["richtig", "billig"]),
 ("b-d-g-final", "-b · -d · -g", "[p] · [t] · [k]",
  L("« p », « t », « k »", "« p », « t », « k »", "p, t, k — Türkçedeki gibi", "«п», «т», «к»", "«پ»، «ت»، «ک»", "p و«ت» و«ك»"),
  L("En fin de mot, b, d et g perdent leur voix et se disent p, t, k : Kind ≈ « kint », Tag ≈ « tak », gelb ≈ « gelp ».",
    "At the end of a word, b, d and g become p, t, k: Kind ≈ « kint », Tag ≈ « tahk », gelb ≈ « gelp ».",
    "Kelime sonunda b, d, g; p, t, k olur — tıpkı Türkçede « kitap » gibi: Kind → « kint », Tag → « tak ».",
    "У кінці слова b, d, g оглушуються і звучать як «п», «т», «к»: Kind → «кінт», Tag → «так». В українській так не роблять, тож варто стежити.",
    "در پایان واژه، b، d و g بی‌واک می‌شوند و «پ»، «ت»، «ک» خوانده می‌شوند: Kind ≈ «کینت»، Tag ≈ «تاک». در فارسی چنین نیست، پس دقت کن.",
    "في آخر الكلمة تفقد b وd وg جهرها فتُنطق p و«ت» و«ك»: Kind ≈ «كِنت»، Tag ≈ «تاك»."),
  ["Kind", "Tag", "gelb"]),
]

# LE PORTUGAIS DU BRESIL (v769) : a part, (court, explication) par regle.
# Ecrit CONTRE le portugais bresilien, pas traduit du francais : le ch dur est
# le « r » de « rato » ; le j n'est jamais le j portugais ; et le Bresilien
# palatalise ti / di (« tchi », « dji ») et ajoute un « i » apres une consonne
# finale -- deux habitudes que l'allemand n'a pas. Non relu par un natif.
PT = {
 "u-trema": ("“i” com os lábios arredondados",
             "O português não tem esse som: diga “i” e, sem mexer a língua, arredonde os lábios como para assobiar."),
 "o-trema": ("“ê” com os lábios arredondados",
             "Não existe em português: diga o “ê” de “você” e, sem mexer a língua, arredonde os lábios."),
 "a-trema": ("como “é” aberto",
             "O ä se pronuncia como o “é” aberto de “café” ou “pé”."),
 "u": ("como o “u” de “uva”",
       "O u alemão é o mesmo “u” do português: gut se diz “gut”. Fácil — o som difícil é o ü."),
 "ei": ("“ai”, como em “pai”",
        "ei se pronuncia “ai”, como em “pai”: Wein se diz “vain”, klein “klain”. Nunca “ei”."),
 "ie": ("“i” longo",
        "ie se pronuncia como um “i” longo: Liebe se diz “liibe”; o e não se ouve. E atenção: antes de i, t e d continuam duros — die é “di”, nunca “dji”."),
 "eu": ("“ói”, como em “dói”",
        "eu e äu se pronunciam “ói”, como em “herói”: heute se diz “hóite”, neu se diz “nói”."),
 "au": ("“au”, como em “mau”",
        "au se pronuncia como em “mau” ou “Paulo”: Haus se diz “haus”, Frau “frau”."),
 "longueur": ("vogal longa ou breve",
              "Uma vogal é longa antes de um h ou quando é dobrada (Tee, Sohn), e breve antes de consoante dupla (Bett, kommen). Em português a duração não importa; em alemão, ela muda a palavra."),
 "sch": ("como “ch” de “chave”",
         "sch se pronuncia como o “ch” de “chave” ou o “x” de “xícara”: Schule se diz “chule”."),
 "sp-st": ("“chp”, “cht” no começo da palavra",
           "No começo de uma palavra (ou de parte dela), sp e st se dizem “chp” e “cht”: Straße se diz “chtrasse”, sprechen “chpréchen” — como o “s” chiado do carioca em “festa”."),
 "ch-doux": ("um sopro suave, sem equivalente",
             "Depois de e, i, ä, ö, ü, ei, eu, l, n ou r, o ch é um sopro suave, com a língua encostada no céu da boca, como um “ch” sussurrado sorrindo: Milch, leicht. O som não existe em português; dizer “ch” se entende, mas não é o certo."),
 "ch-dur": ("como o “r” de “rato”",
            "Depois de a, o, u e au, o ch é raspado no fundo da garganta, como o “r” de “rato” ou de “carro” no Rio de Janeiro: Nacht, Buch, Bauch."),
 "z": ("“ts”",
       "z (e tz) se pronuncia sempre “ts”, como em “tsé-tsé”: Zeit se diz “tsait”, Katze “katse”. Nunca o “z” de “casa”."),
 "v": ("quase sempre “f”",
       "v se pronuncia quase sempre “f”: Vater se diz “fater”, viel “fil”. Algumas palavras de origem estrangeira mantêm o “v” (Vase, Klavier)."),
 "w": ("“v”",
       "w se pronuncia “v”: Wasser se diz “vasser”, wo “vo”."),
 "s": ("“z” antes de vogal",
       "Antes de uma vogal, s se diz “z”, como em “casa”: Sonne se diz “zone”, Hose “hoze”."),
 "eszett": ("“s” forte",
            "ß e ss se pronunciam como um “s” forte, como o “ss” de “passo”. ß vem depois de vogal longa (groß), ss depois de vogal breve (essen)."),
 "j": ("“i”, como em “iate”",
       "j se pronuncia como o “i” de “iate”: Jahr se diz “iar”, jung “iung”. Nunca o “j” de “janela”."),
 "h": ("aspirado no começo, mudo depois de vogal",
       "No começo de uma palavra ou sílaba, o h é um sopro de verdade, como o “r” suave de “rato” em boa parte do Brasil — nunca mudo como em “hora”: Hund. Depois de uma vogal, não se pronuncia e alonga a vogal: gehen, Uhr."),
 "r": ("no fundo da garganta",
       "O r alemão se faz no fundo da garganta, como o “r” de “rato”, e não como o “r” batido de “caro”: rot, Brot."),
 "pf": ("p + f de uma vez",
        "pf se pronuncia p e f de uma só vez; os dois se ouvem: Apfel, Kopf."),
 "er-final": ("um “a” leve",
              "No fim de uma palavra, -er se diz como um “a” leve, sem “r”: Vater ≈ “fáta”, Mutter ≈ “múta”."),
 "ig-final": ("“-ich”, com o ch suave",
              "No fim de uma palavra, -ig se diz “-ich”, com o ch suave de Milch: richtig, billig."),
 "b-d-g-final": ("“p”, “t”, “k”",
                 "No fim de uma palavra, b, d e g perdem a voz e se dizem p, t, k: Kind ≈ “kint”, Tag ≈ “tak”, gelb ≈ “guelp”. E não acrescente um “i” no final: é “kint”, e não “kindi”."),
}

GROUPES = [("voyelles", VOYELLES), ("consonnes", CONSONNES), ("fins", FINS)]


def corpus():
    """mot allemand -> son entree (ses traductions), du plus bas niveau au plus haut."""
    idx = {}
    def ch(n):
        return json.load(io.open(os.path.join(RACINE, n), encoding="utf-8"))
    for t in sorted(ch("themes.json")["themes"], key=lambda t: t.get("niveau", "")):
        for m in t["mots"]:
            idx.setdefault(m["mot"], m)
    for f, k in (("verbe.json", "infinitif"), ("adjectif.json", "mot"), ("adverbe.json", "mot")):
        d = ch(f)
        for n in sorted(d):
            for x in d[n]:
                idx.setdefault(x[k], x)
    return idx


def construire():
    idx = corpus()
    fautes, ids, out = [], set(), []
    for gid, regles in GROUPES:
        g = {"id": gid, "regles": []}
        for rid, graphie, api, court, expl, exemples in regles:
            if rid in ids:
                fautes.append("id en double : " + rid)
            ids.add(rid)
            if rid in PT:
                court = dict(court, pt=PT[rid][0])
                expl = dict(expl, pt=PT[rid][1])
            for nom, v in (("court", court), ("explication", expl)):
                manque = [l for l in LANGUES if not v.get(l)]
                if manque:
                    fautes.append("%s / %s : manque %s" % (rid, nom, manque))
            ex = []
            for mot in exemples:
                e = idx.get(mot)
                h = hashlib.sha1(mot.encode("utf-8")).hexdigest()[:16]
                if not e:
                    fautes.append("%s : « %s » absent du corpus (pas de traduction)" % (rid, mot))
                    continue
                if not os.path.exists(os.path.join(RACINE, "audio", "mp3", h + ".mp3")):
                    fautes.append("%s : « %s » sans voix d'Aurora" % (rid, mot))
                ex.append({"mot": mot, **{c: e[c] for c in ("traduction", "traduction_en", "traduction_tr",
                                                             "traduction_uk", "traduction_fa", "traduction_pt") if e.get(c)}})
            if len(ex) < 2:
                fautes.append("%s : moins de deux exemples" % rid)
            g["regles"].append({"id": rid, "graphie": graphie, "api": api, "court": court,
                                "explication": expl, "exemples": ex})
        out.append(g)
    return {"_note": "Fichier DERIVE : python tests/prononciation.py --ecrire. Ne pas modifier a la main.",
            "groupes": out}, fautes


def main():
    d, fautes = construire()
    n = sum(len(g["regles"]) for g in d["groupes"])
    for f in fautes:
        print("  FAUTE :", f)
    print("%d regles, %d exemples, %d faute(s)" % (n, sum(len(r["exemples"]) for g in d["groupes"] for r in g["regles"]), len(fautes)))
    if fautes:
        sys.exit(1)
    chemin = os.path.join(RACINE, "prononciation.json")
    if "--ecrire" in sys.argv:
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("ecrit :", chemin)
    elif os.path.exists(chemin):
        actuel = json.load(io.open(chemin, encoding="utf-8"))
        print("prononciation.json %s" % ("a jour" if actuel == d else "EN RETARD -- relancer avec --ecrire"))


if __name__ == "__main__":
    main()
