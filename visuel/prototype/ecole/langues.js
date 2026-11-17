// « L'école et la garderie » dans les langues d'interface sans phrase traduite jusqu'ici (lot 5 de l'alignement des
// thèmes, 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour
// qui apprend l'espagnol.
//
// LE CHEMIN NATIF : la page fabrique ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot
// d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps). On donne ici les morceaux
// dans chaque langue et la petite grammaire de chacune : le nombre qui régit le nom (две тетради, пять тетрадей ;
// dwóch zeszytów ; دفترين, ثلاثة دفاتر), le datif de « Бену нужен », le mois au génitif (28 декабря), le suffixe turc
// après l'heure et le mois (saat 15.30'da, 28 Aralık'ta), l'accusatif polonais de la matière (Ben ma matematykę).
// Les prénoms sont transcrits là où la langue n'a pas l'alphabet latin (Бен, Мия ; بن، ميا).
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesEcole(D, APPRENDRE){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const JOURS = {
    tr: ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"],
    uk: ["понеділок", "вівторок", "середа", "четвер", "пʼятниця", "субота", "неділя"],
    pl: ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
    ru: ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"],
    fa: ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"],
    ar: ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
  };
  const QUAND = {
    tr: JOURS.tr.map(j => j + " günü"),
    uk: ["у понеділок", "у вівторок", "у середу", "у четвер", "у пʼятницю", "у суботу", "у неділю"],
    pl: ["w poniedziałek", "we wtorek", "w środę", "w czwartek", "w piątek", "w sobotę", "w niedzielę"],
    ru: ["в понедельник", "во вторник", "в среду", "в четверг", "в пятницу", "в субботу", "в воскресенье"],
    fa: JOURS.fa,
    ar: JOURS.ar.map(j => "يوم " + j)
  };
  const MOIS = {   // le mois après le jour du mois (génitif en uk, pl, ru)
    tr: ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
    uk: ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"],
    pl: ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "września", "października", "listopada", "grudnia"],
    ru: ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"],
    fa: ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن", "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"],
    ar: ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
  };
  // le turc : le suffixe du locatif suit le dernier mot lu (« on beş » -> 'te, « otuz » -> 'da, « Aralık » -> 'ta)
  const SUF_U = {1: "'de", 2: "'de", 3: "'te", 4: "'te", 5: "'te", 6: "'da", 7: "'de", 8: "'de", 9: "'da"};
  const SUF_D = {1: "'da", 2: "'de", 3: "'da", 4: "'ta", 5: "'de"};
  const sufNb = n => n % 10 ? SUF_U[n % 10] : SUF_D[n / 10];
  const SUF_MOIS = ["'ta", "'ta", "'ta", "'da", "'ta", "'da", "'da", "'ta", "'de", "'de", "'da", "'ta"];
  const hm = (h, m) => h + ":" + String(m).padStart(2, "0");
  const A_HEURE = {
    tr: (h, m) => "saat " + h + "." + String(m).padStart(2, "0") + sufNb(m || h),
    uk: (h, m) => "о " + hm(h, m), pl: (h, m) => "o " + hm(h, m), ru: (h, m) => "в " + hm(h, m),
    fa: (h, m) => "ساعت " + hm(h, m), ar: (h, m) => "في الساعة " + hm(h, m)
  };
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
  const NOMS = {
    tr: {}, pl: {},
    uk: {Ben: "Бен", Mia: "Мія", Katrin: "Катрін", Jan: "Ян", Anna: "Анна", Mark: "Марк"},
    ru: {Ben: "Бен", Mia: "Мия", Katrin: "Катрин", Jan: "Ян", Anna: "Анна", Mark: "Марк"},
    fa: {Ben: "بن", Mia: "میا", Katrin: "کاترین", Jan: "یان", Anna: "آنا", Mark: "مارک"},
    ar: {Ben: "بن", Mia: "ميا", Katrin: "كاترين", Jan: "يان", Anna: "آنا", Mark: "مارك"}
  };
  const nomDe = (lg, n) => (NOMS[lg] || {})[n] || n;

  // ---------- les fournitures ----------
  // tr, fa : le nom (après un nombre, il reste au singulier) ; uk, ru : [nominatif, génitif sg., nominatif pl., génitif pl., genre]
  // pl : [nominatif, génitif sg., génitif pl.] ; ar : [singulier, duel (génitif), pluriel, genre]
  const OBJ = {
    tr: {schultasche: "okul çantası", federmaeppchen: "kalemlik", heft: "defter", bleistift: "kurşun kalem", lineal: "cetvel", radiergummi: "silgi", buch: "kitap", schere: "makas"},
    uk: {schultasche: ["портфель", "портфеля", "портфелі", "портфелів", "m"], federmaeppchen: ["пенал", "пенала", "пенали", "пеналів", "m"],
         heft: ["зошит", "зошита", "зошити", "зошитів", "m"], bleistift: ["олівець", "олівця", "олівці", "олівців", "m"],
         lineal: ["лінійка", "лінійки", "лінійки", "лінійок", "f"], radiergummi: ["гумка", "гумки", "гумки", "гумок", "f"],
         buch: ["книжка", "книжки", "книжки", "книжок", "f"], schere: ["ножиці", "ножиць", "ножиці", "ножиць", "pl"]},
    ru: {schultasche: ["ранец", "ранца", "ранцы", "ранцев", "m"], federmaeppchen: ["пенал", "пенала", "пеналы", "пеналов", "m"],
         heft: ["тетрадь", "тетради", "тетради", "тетрадей", "f"], bleistift: ["карандаш", "карандаша", "карандаши", "карандашей", "m"],
         lineal: ["линейка", "линейки", "линейки", "линеек", "f"], radiergummi: ["ластик", "ластика", "ластики", "ластиков", "m"],
         buch: ["книга", "книги", "книги", "книг", "f"], schere: ["ножницы", "ножниц", "ножницы", "ножниц", "pl"]},
    pl: {schultasche: ["tornister", "tornistra", "tornistrów"], federmaeppchen: ["piórnik", "piórnika", "piórników"], heft: ["zeszyt", "zeszytu", "zeszytów"],
         bleistift: ["ołówek", "ołówka", "ołówków"], lineal: ["linijka", "linijki", "linijek"], radiergummi: ["gumka", "gumki", "gumek"],
         buch: ["książka", "książki", "książek"], schere: ["nożyczki", "nożyczek", "nożyczek"]},
    fa: {schultasche: "کیف مدرسه", federmaeppchen: "جامدادی", heft: "دفتر", bleistift: "مداد", lineal: "خط‌کش", radiergummi: "پاک‌کن", buch: "کتاب", schere: "قیچی"},
    ar: {schultasche: ["حقيبة مدرسية", "حقيبتين مدرسيتين", "حقائب مدرسية", "f"], federmaeppchen: ["مقلمة", "مقلمتين", "مقالم", "f"],
         heft: ["دفتر", "دفترين", "دفاتر", "m"], bleistift: ["قلم رصاص", "قلمي رصاص", "أقلام رصاص", "m"], lineal: ["مسطرة", "مسطرتين", "مساطر", "f"],
         radiergummi: ["ممحاة", "ممحاتين", "مماحٍ", "f"], buch: ["كتاب", "كتابين", "كتب", "m"], schere: ["مقص", "مقصين", "مقصات", "m"]}
  };
  // les clés espagnoles des mêmes objets
  const OBJ_ES = {mochila: "schultasche", estuche: "federmaeppchen", cuaderno: "heft", lapiz: "bleistift", regla: "lineal", goma: "radiergummi", libro: "buch", tijeras: "schere"};
  const cleObj = k => APPRENDRE === "es" ? OBJ_ES[k] : k;
  const nomObj = (lg, k) => { const o = OBJ[lg][cleObj(k)]; return Array.isArray(o) ? o[0] : o; };

  // ---------- les lieux des enfants : [le lieu, « vers le lieu », « au lieu »] ----------
  const LIEU = {
    tr: {kita: ["kreş", "kreşe", "kreşte"], kindergarten: ["anaokulu", "anaokuluna", "anaokulunda"], grundschule: ["ilkokul", "ilkokula", "ilkokulda"], schule: ["okul", "okula", "okulda"]},
    uk: {kita: ["дитсадок", "до дитсадка", "у дитсадку"], kindergarten: ["дитячий садок", "до дитячого садка", "у дитячому садку"],
         grundschule: ["початкова школа", "до початкової школи", "у початковій школі"], schule: ["школа", "до школи", "у школі"]},
    pl: {kita: ["przedszkole", "do przedszkola", "w przedszkolu"], kindergarten: ["przedszkole", "do przedszkola", "w przedszkolu"],
         grundschule: ["szkoła podstawowa", "do szkoły podstawowej", "w szkole podstawowej"], schule: ["szkoła", "do szkoły", "w szkole"]},
    ru: {kita: ["детский сад", "в детский сад", "в детском саду"], kindergarten: ["садик", "в садик", "в садике"],
         grundschule: ["начальная школа", "в начальную школу", "в начальной школе"], schule: ["школа", "в школу", "в школе"]},
    fa: {kita: ["مهدکودک", "به مهدکودک", "در مهدکودک"], kindergarten: ["کودکستان", "به کودکستان", "در کودکستان"],
         grundschule: ["دبستان", "به دبستان", "در دبستان"], schule: ["مدرسه", "به مدرسه", "در مدرسه"]},
    ar: {kita: ["الحضانة", "إلى الحضانة", "في الحضانة"], kindergarten: ["روضة الأطفال", "إلى روضة الأطفال", "في روضة الأطفال"],
         grundschule: ["المدرسة الابتدائية", "إلى المدرسة الابتدائية", "في المدرسة الابتدائية"], schule: ["المدرسة", "إلى المدرسة", "في المدرسة"],
         guarderia: ["الحضانة", "إلى الحضانة", "في الحضانة"], colegio: ["المدرسة", "إلى المدرسة", "في المدرسة"], escuela: ["المدرسة", "إلى المدرسة", "في المدرسة"]}
  };

  // ---------- les actions (l'id est le même dans les deux langues apprises) ----------
  const ACT = {
    tr: {bringen_kita: "Katrin, Mia'yı kreşe götürüyor.", bringen_schule: "Jan, Ben'i okula götürüyor.", abholen_kita: "Mark, Mia'yı kreşten alıyor.",
         abholen_schule: "Jan, Ben'i okuldan alıyor.", anmelden: "Katrin, Mia'yı kreşe kaydettiriyor.", sprechen: "Katrin öğretmenle konuşuyor.",
         anrufen: "Katrin okulu arıyor.", krank: "Ben hasta.", packen: "Ben okul çantasını hazırlıyor.", hausaufgaben: "Ben ödevlerini yapıyor.",
         schreiben: "Ben defterine yazıyor.", malen: "Mia bir resim yapıyor.", spielen: "Ben teneffüste oynuyor.", elternabend: "Jan ve Katrin veli toplantısına gidiyor."},
    uk: {bringen_kita: "Катрін відводить Мію до дитсадка.", bringen_schule: "Ян відводить Бена до школи.", abholen_kita: "Марк забирає Мію з дитсадка.",
         abholen_schule: "Ян забирає Бена зі школи.", anmelden: "Катрін записує Мію до дитсадка.", sprechen: "Катрін розмовляє з учителькою.",
         anrufen: "Катрін телефонує до школи.", krank: "Бен хворий.", packen: "Бен збирає портфель.", hausaufgaben: "Бен робить домашнє завдання.",
         schreiben: "Бен пише в зошиті.", malen: "Мія малює картину.", spielen: "Бен грається на перерві.", elternabend: "Ян і Катрін ідуть на батьківські збори."},
    pl: {bringen_kita: "Katrin odprowadza Mię do przedszkola.", bringen_schule: "Jan odprowadza Bena do szkoły.", abholen_kita: "Mark odbiera Mię z przedszkola.",
         abholen_schule: "Jan odbiera Bena ze szkoły.", anmelden: "Katrin zapisuje Mię do przedszkola.", sprechen: "Katrin rozmawia z nauczycielką.",
         anrufen: "Katrin dzwoni do szkoły.", krank: "Ben jest chory.", packen: "Ben pakuje tornister.", hausaufgaben: "Ben odrabia lekcje.",
         schreiben: "Ben pisze w zeszycie.", malen: "Mia maluje obrazek.", spielen: "Ben bawi się na przerwie.", elternabend: "Jan i Katrin idą na zebranie rodziców."},
    ru: {bringen_kita: "Катрин отводит Мию в детский сад.", bringen_schule: "Ян отводит Бена в школу.", abholen_kita: "Марк забирает Мию из детского сада.",
         abholen_schule: "Ян забирает Бена из школы.", anmelden: "Катрин записывает Мию в детский сад.", sprechen: "Катрин разговаривает с учительницей.",
         anrufen: "Катрин звонит в школу.", krank: "Бен болен.", packen: "Бен собирает ранец.", hausaufgaben: "Бен делает домашнее задание.",
         schreiben: "Бен пишет в тетради.", malen: "Мия рисует картину.", spielen: "Бен играет на перемене.", elternabend: "Ян и Катрин идут на родительское собрание."},
    fa: {bringen_kita: "کاترین میا را به مهدکودک می‌برد.", bringen_schule: "یان بن را به مدرسه می‌برد.", abholen_kita: "مارک میا را از مهدکودک می‌آورد.",
         abholen_schule: "یان بن را از مدرسه می‌آورد.", anmelden: "کاترین میا را در مهدکودک ثبت‌نام می‌کند.", sprechen: "کاترین با خانم معلم صحبت می‌کند.",
         anrufen: "کاترین به مدرسه زنگ می‌زند.", krank: "بن بیمار است.", packen: "بن کیف مدرسه‌اش را آماده می‌کند.", hausaufgaben: "بن تکالیفش را انجام می‌دهد.",
         schreiben: "بن در دفترش می‌نویسد.", malen: "میا یک نقاشی می‌کشد.", spielen: "بن در زنگ تفریح بازی می‌کند.", elternabend: "یان و کاترین به جلسهٔ اولیا می‌روند."},
    ar: {bringen_kita: "تأخذ كاترين ميا إلى الحضانة.", bringen_schule: "يأخذ يان بن إلى المدرسة.", abholen_kita: "يصطحب مارك ميا من الحضانة.",
         abholen_schule: "يصطحب يان بن من المدرسة.", anmelden: "تسجّل كاترين ميا في الحضانة.", sprechen: "تتحدث كاترين مع المعلمة.",
         anrufen: "تتصل كاترين بالمدرسة.", krank: "بن مريض.", packen: "يحضّر بن حقيبته المدرسية.", hausaufgaben: "يحلّ بن واجباته المدرسية.",
         schreiben: "يكتب بن في دفتره.", malen: APPRENDRE === "es" ? "ترسم ميا في الحضانة." : "ترسم ميا لوحة.", spielen: "يلعب بن في الاستراحة.",
         elternabend: "يذهب يان وكاترين إلى اجتماع أولياء الأمور."}
  };

  // ---------- les raisons du mot d'absence : [la phrase seule, la proposition après « parce que »] ----------
  const RAISON = {
    tr: {krank: ["Hasta.", "hasta"], fieber: ["Ateşi var.", "ateşi var"], arzt: ["Doktordan randevusu var.", "doktordan randevusu var"]},
    uk: {krank: ["Він хворий.", "він хворий"], fieber: ["У нього температура.", "у нього температура"], arzt: ["Він записаний до лікаря.", "він записаний до лікаря"]},
    pl: {krank: ["Jest chory.", "jest chory"], fieber: ["Ma gorączkę.", "ma gorączkę"], arzt: ["Ma wizytę u lekarza.", "ma wizytę u lekarza"]},
    ru: {krank: ["Он болен.", "он болен"], fieber: ["У него температура.", "у него температура"], arzt: ["Он записан к врачу.", "он записан к врачу"]},
    fa: {krank: ["او بیمار است.", "بیمار است"], fieber: ["او تب دارد.", "تب دارد"], arzt: ["او نزد پزشک وقت دارد.", "نزد پزشک وقت دارد"]},
    ar: {krank: ["إنه مريض.", "لأنه مريض"], fieber: ["لديه حمّى.", "لأن لديه حمّى"], arzt: ["لديه موعد عند الطبيب.", "لأن لديه موعدًا عند الطبيب"]}
  };
  // ---------- les papiers (« C'est un emploi du temps. ») ----------
  const PAPIER = {
    tr: {stundenplan: "Bu bir ders programı.", entschuldigung: "Bu bir mazeret yazısı.", elternabend: "Bu bir veli toplantısı daveti.", ferien: "Bu bir tatil takvimi.", liste: "Bu bir okul malzemeleri listesi."},
    uk: {stundenplan: "Це розклад уроків.", entschuldigung: "Це записка про відсутність.", elternabend: "Це запрошення на батьківські збори.", ferien: "Це календар канікул.", liste: "Це список шкільного приладдя."},
    pl: {stundenplan: "To plan lekcji.", entschuldigung: "To usprawiedliwienie.", elternabend: "To zaproszenie na zebranie rodziców.", ferien: "To kalendarz ferii.", liste: "To lista przyborów szkolnych."},
    ru: {stundenplan: "Это расписание уроков.", entschuldigung: "Это записка об отсутствии.", elternabend: "Это приглашение на родительское собрание.", ferien: "Это календарь каникул.", liste: "Это список школьных принадлежностей."},
    fa: {stundenplan: "این یک برنامهٔ درسی است.", entschuldigung: "این یک غیبت‌نامه است.", elternabend: "این یک دعوت‌نامه برای جلسهٔ اولیاست.", ferien: "این یک تقویم تعطیلات است.", liste: "این یک فهرست لوازم‌التحریر است."},
    ar: {stundenplan: "هذا جدول الحصص.", entschuldigung: "هذه رسالة تبرير غياب.", elternabend: "هذه دعوة إلى اجتماع أولياء الأمور.", ferien: "هذا تقويم العطل المدرسية.", liste: "هذه قائمة الأدوات المدرسية."}
  };
  // ---------- qui va chercher Mia ----------
  const ABHOLER = {
    tr: {Katrin: "annesi", Jan: "babası", Anna: "halası", Mark: "ailenin bir arkadaşı"},
    uk: {Katrin: "її мама", Jan: "її тато", Anna: "її тітка", Mark: "друг родини"},
    pl: {Katrin: "jej mama", Jan: "jej tata", Anna: "jej ciocia", Mark: "przyjaciel rodziny"},
    ru: {Katrin: "её мама", Jan: "её папа", Anna: "её тётя", Mark: "друг семьи"},
    fa: {Katrin: "مادرش", Jan: "پدرش", Anna: "عمه‌اش", Mark: "یکی از دوستان خانواده"},
    ar: {Katrin: "أمها", Jan: "أبوها", Anna: "عمّتها", Mark: "صديق العائلة"}
  };
  // ---------- l'emploi du temps : les matières (pl : [nominatif, accusatif]) et les rangs de l'heure de cours ----------
  const MATIERE = {
    tr: {deutsch: "Almanca", mathe: "matematik", sport: "beden eğitimi", kunst: "resim", musik: "müzik", sachunterricht: "hayat bilgisi", englisch: "İngilizce"},
    uk: {deutsch: "німецька мова", mathe: "математика", sport: "фізкультура", kunst: "образотворче мистецтво", musik: "музика", sachunterricht: "природознавство", englisch: "англійська мова"},
    pl: {deutsch: ["niemiecki", "niemiecki"], mathe: ["matematyka", "matematykę"], sport: ["wychowanie fizyczne", "wychowanie fizyczne"], kunst: ["plastyka", "plastykę"],
         musik: ["muzyka", "muzykę"], sachunterricht: ["przyroda", "przyrodę"], englisch: ["angielski", "angielski"]},
    ru: {deutsch: "немецкий язык", mathe: "математика", sport: "физкультура", kunst: "рисование", musik: "музыка", sachunterricht: "окружающий мир", englisch: "английский язык"},
    fa: {deutsch: "آلمانی", mathe: "ریاضی", sport: "ورزش", kunst: "هنر", musik: "موسیقی", sachunterricht: "علوم", englisch: "انگلیسی"},
    ar: {deutsch: APPRENDRE === "es" ? "الإسبانية" : "الألمانية", mathe: "الرياضيات", sport: "التربية البدنية", kunst: "الفنون", musik: "الموسيقى", sachunterricht: "العلوم", englisch: "الإنجليزية"}
  };
  const matNom = (lg, c) => { const m = MATIERE[lg][c]; return Array.isArray(m) ? m[0] : m; };
  const RANG = {
    tr: ["", "birinci", "ikinci", "üçüncü", "dördüncü", "beşinci", "altıncı"],
    uk: ["", "першому", "другому", "третьому", "четвертому", "пʼятому", "шостому"],
    pl: ["", "pierwszej", "drugiej", "trzeciej", "czwartej", "piątej", "szóstej"],
    ru: ["", "первом", "втором", "третьем", "четвёртом", "пятом", "шестом"],
    fa: ["", "اول", "دوم", "سوم", "چهارم", "پنجم", "ششم"],
    ar: ["", "الأولى", "الثانية", "الثالثة", "الرابعة", "الخامسة", "السادسة"]
  };
  const NB = {tr: ["", "bir", "iki", "üç", "dört", "beş"], fa: ["", "یک", "دو", "سه", "چهار", "پنج"]};

  // ---------- les phrases, langue par langue ----------
  const B = {
    tr: {
      obj: k => "Bu " + nomObj("tr", k) + ".",
      liste: (k, n) => "Ben'e " + NB.tr[n] + " " + OBJ.tr[cleObj(k)] + " lazım.",
      wohin: (e, k, ou) => ou ? "Saat sabah on. " + e + " " + LIEU.tr[k][2] + "." : e + " " + (e === "Mia" ? "dört" : "yedi") + " yaşında. " + maj(LIEU.tr[k][1]) + " gidiyor.",
      mot: (jours, r) => "Ben " + jours.map(j => JOURS.tr[j - 1]).join(" ve ") + " okula gelemiyor, çünkü " + RAISON.tr[r][1] + ".",
      reunion: (j, h, m, s) => "Veli toplantısı " + QUAND.tr[j - 1] + " " + A_HEURE.tr(h, m) + ", " + s + " numaralı sınıfta.",
      ferien: (jj, mm, vac) => jj + " " + MOIS.tr[mm - 1] + SUF_MOIS[mm - 1] + " Ben " + (vac ? "tatilde" : "okula gidiyor") + ".",
      abholung: (j, qui, h, m) => QUAND.tr[j - 1] + " Mia'yı " + A_HEURE.tr(h, m) + " " + qui + " alıyor.",
      cours: (j, r, c) => QUAND.tr[j - 1] + " " + RANG.tr[r + 1] + " derste Ben'in " + matNom("tr", c) + " dersi var.",
      jourCours: (j, c) => "Ben'in " + matNom("tr", c) + " dersi " + QUAND.tr[j - 1] + ".",
      fin: (j, h, m) => QUAND.tr[j - 1] + " okul " + A_HEURE.tr(h, m) + " bitiyor.",
      pause: (h, m) => "Teneffüs " + A_HEURE.tr(h, m) + " başlıyor."
    },
    uk: {
      obj: k => "Це " + nomObj("uk", k) + ".",
      liste: (k, n) => { const [s, g, p, gp, ge] = OBJ.uk[cleObj(k)];
        if (n === 1) return "Бенові " + {m: "потрібен", f: "потрібна", pl: "потрібні"}[ge] + " " + s + ".";
        if (ge === "pl") return "Бенові " + (n < 5 ? "потрібні " : "потрібно ") + ["", "", "дві", "три", "чотири", "пʼять"][n] + " " + (n < 5 ? "пари" : "пар") + " ножиць.";
        if (n <= 4) return "Бенові потрібні " + (ge === "f" ? ["", "", "дві", "три", "чотири"] : ["", "", "два", "три", "чотири"])[n] + " " + p + ".";
        return "Бенові потрібно пʼять " + gp + "."; },
      wohin: (e, k, ou) => ou ? "Десята ранку. " + nomDe("uk", e) + " " + LIEU.uk[k][2] + "."
        : (e === "Mia" ? "Мії чотири роки. Вона ходить " : "Бенові сім років. Він ходить ") + LIEU.uk[k][1] + ".",
      mot: (jours, r) => "Бен не прийде до школи " + jours.map(j => QUAND.uk[j - 1]).join(" і ") + ", бо " + RAISON.uk[r][1] + ".",
      reunion: (j, h, m, s) => "Батьківські збори " + QUAND.uk[j - 1] + " " + A_HEURE.uk(h, m) + " у кабінеті " + s + ".",
      ferien: (jj, mm, vac) => jj + " " + MOIS.uk[mm - 1] + (vac ? " у Бена канікули." : " Бен іде до школи."),
      abholung: (j, qui, h, m) => maj(QUAND.uk[j - 1]) + " " + nomDe("uk", qui) + " забирає Мію " + A_HEURE.uk(h, m) + ".",
      cours: (j, r, c) => maj(QUAND.uk[j - 1]) + " на " + RANG.uk[r + 1] + " уроці в Бена " + matNom("uk", c) + ".",
      jourCours: (j, c) => "У Бена " + matNom("uk", c) + " " + QUAND.uk[j - 1] + ".",
      fin: (j, h, m) => maj(QUAND.uk[j - 1]) + " уроки закінчуються " + A_HEURE.uk(h, m) + ".",
      pause: (h, m) => "Велика перерва починається " + A_HEURE.uk(h, m) + "."
    },
    pl: {
      obj: k => "To " + nomObj("pl", k) + ".",
      liste: (k, n) => { const [s, g, gp] = OBJ.pl[cleObj(k)];
        return "Ben potrzebuje " + (n === 1 ? g : ["", "", "dwóch", "trzech", "czterech", "pięciu"][n] + " " + gp) + "."; },
      wohin: (e, k, ou) => ou ? "Jest dziesiąta rano. " + e + " jest " + LIEU.pl[k][2] + "."
        : e + (e === "Mia" ? " ma cztery lata. Chodzi " : " ma siedem lat. Chodzi ") + LIEU.pl[k][1] + ".",
      mot: (jours, r) => "Bena nie ma w szkole " + jours.map(j => QUAND.pl[j - 1]).join(" i ") + ", bo " + RAISON.pl[r][1] + ".",
      reunion: (j, h, m, s) => "Zebranie rodziców jest " + QUAND.pl[j - 1] + " " + A_HEURE.pl(h, m) + " w sali " + s + ".",
      ferien: (jj, mm, vac) => jj + " " + MOIS.pl[mm - 1] + (vac ? " Ben ma wolne od szkoły." : " Ben idzie do szkoły."),
      abholung: (j, qui, h, m) => maj(QUAND.pl[j - 1]) + " " + qui + " odbiera Mię " + A_HEURE.pl(h, m) + ".",
      cours: (j, r, c) => maj(QUAND.pl[j - 1]) + " na " + RANG.pl[r + 1] + " lekcji Ben ma " + MATIERE.pl[c][1] + ".",
      jourCours: (j, c) => "Ben ma " + MATIERE.pl[c][1] + " " + QUAND.pl[j - 1] + ".",
      fin: (j, h, m) => maj(QUAND.pl[j - 1]) + " lekcje kończą się " + A_HEURE.pl(h, m) + ".",
      pause: (h, m) => "Duża przerwa zaczyna się " + A_HEURE.pl(h, m) + "."
    },
    ru: {
      obj: k => "Это " + nomObj("ru", k) + ".",
      liste: (k, n) => { const [s, g, p, gp, ge] = OBJ.ru[cleObj(k)];
        if (n === 1) return "Бену " + {m: "нужен", f: "нужна", pl: "нужны"}[ge] + " " + s + ".";
        if (ge === "pl") return "Бену " + (n < 5 ? "нужны " : "нужно ") + ["", "", "две", "три", "четыре", "пять"][n] + " " + (n < 5 ? "пары" : "пар") + " ножниц.";
        if (n <= 4) return "Бену нужны " + (ge === "f" ? ["", "", "две", "три", "четыре"] : ["", "", "два", "три", "четыре"])[n] + " " + g + ".";
        return "Бену нужно пять " + gp + "."; },
      wohin: (e, k, ou) => ou ? "Десять часов утра. " + nomDe("ru", e) + " " + LIEU.ru[k][2] + "."
        : (e === "Mia" ? "Мие четыре года. Она ходит " : "Бену семь лет. Он ходит ") + LIEU.ru[k][1] + ".",
      mot: (jours, r) => "Бена не будет в школе " + jours.map(j => QUAND.ru[j - 1]).join(" и ") + ", потому что " + RAISON.ru[r][1] + ".",
      reunion: (j, h, m, s) => "Родительское собрание " + QUAND.ru[j - 1] + " " + A_HEURE.ru(h, m) + " в кабинете " + s + ".",
      ferien: (jj, mm, vac) => jj + " " + MOIS.ru[mm - 1] + (vac ? " у Бена каникулы." : " Бен идёт в школу."),
      abholung: (j, qui, h, m) => maj(QUAND.ru[j - 1]) + " " + nomDe("ru", qui) + " забирает Мию " + A_HEURE.ru(h, m) + ".",
      cours: (j, r, c) => maj(QUAND.ru[j - 1]) + " на " + RANG.ru[r + 1] + " уроке у Бена " + matNom("ru", c) + ".",
      jourCours: (j, c) => "У Бена " + matNom("ru", c) + " " + QUAND.ru[j - 1] + ".",
      fin: (j, h, m) => maj(QUAND.ru[j - 1]) + " уроки заканчиваются " + A_HEURE.ru(h, m) + ".",
      pause: (h, m) => "Большая перемена начинается " + A_HEURE.ru(h, m) + "."
    },
    fa: {
      obj: k => "این " + nomObj("fa", k) + " است.",
      liste: (k, n) => "بن به " + NB.fa[n] + " " + OBJ.fa[cleObj(k)] + " نیاز دارد.",
      wohin: (e, k, ou) => ou ? "ساعت ده صبح است. " + nomDe("fa", e) + " " + LIEU.fa[k][2] + " است."
        : nomDe("fa", e) + (e === "Mia" ? " چهار سال دارد. او " : " هفت سال دارد. او ") + LIEU.fa[k][1] + " می‌رود.",
      mot: (jours, r) => "بن " + jours.map(j => JOURS.fa[j - 1]).join(" و ") + " به مدرسه نمی‌آید، چون " + RAISON.fa[r][1] + ".",
      reunion: (j, h, m, s) => "جلسهٔ اولیا " + JOURS.fa[j - 1] + " " + A_HEURE.fa(h, m) + " در کلاس " + s + " است.",
      ferien: (jj, mm, vac) => "روز " + jj + " " + MOIS.fa[mm - 1] + "، بن " + (vac ? "در تعطیلات است." : "به مدرسه می‌رود."),
      abholung: (j, qui, h, m) => JOURS.fa[j - 1] + " " + nomDe("fa", qui) + " " + A_HEURE.fa(h, m) + " دنبال میا می‌رود.",
      cours: (j, r, c) => JOURS.fa[j - 1] + "، زنگ " + RANG.fa[r + 1] + "، بن " + matNom("fa", c) + " دارد.",
      jourCours: (j, c) => "بن " + JOURS.fa[j - 1] + " " + matNom("fa", c) + " دارد.",
      fin: (j, h, m) => JOURS.fa[j - 1] + " مدرسه " + A_HEURE.fa(h, m) + " تمام می‌شود.",
      pause: (h, m) => "زنگ تفریح " + A_HEURE.fa(h, m) + " شروع می‌شود."
    },
    ar: {
      obj: k => { const [s, , , g] = OBJ.ar[cleObj(k)]; return (g === "f" ? "هذه " : "هذا ") + s + "."; },
      liste: (k, n) => { const [s, d, p, g] = OBJ.ar[cleObj(k)];
        if (n === 1) return "يحتاج بن إلى " + s + ".";
        if (n === 2) return "يحتاج بن إلى " + d + ".";
        return "يحتاج بن إلى " + (g === "f" ? ["", "", "", "ثلاث", "أربع", "خمس"] : ["", "", "", "ثلاثة", "أربعة", "خمسة"])[n] + " " + p + "."; },
      wohin: (e, k, ou) => ou ? "إنها الساعة العاشرة صباحًا. " + nomDe("ar", e) + " " + LIEU.ar[k][2] + "."
        : (e === "Mia" ? "عمر ميا أربع سنوات. تذهب " : "عمر بن سبع سنوات. يذهب ") + LIEU.ar[k][1] + ".",
      mot: (jours, r) => "يتغيّب بن عن المدرسة " + jours.map(j => QUAND.ar[j - 1]).join(" و") + " " + RAISON.ar[r][1] + ".",
      reunion: (j, h, m, s) => "اجتماع أولياء الأمور " + QUAND.ar[j - 1] + " " + A_HEURE.ar(h, m) + " في القاعة " + s + ".",
      ferien: (jj, mm, vac) => "في " + jj + " " + MOIS.ar[mm - 1] + "، " + (vac ? "يكون بن في العطلة." : "يذهب بن إلى المدرسة."),
      abholung: (j, qui, h, m) => QUAND.ar[j - 1] + "، " + (qui === "Katrin" || qui === "Anna" ? "تصطحب " : "يصطحب ") + nomDe("ar", qui) + " ميا " + A_HEURE.ar(h, m) + ".",
      cours: (j, r, c) => "يدرس بن " + matNom("ar", c) + " " + QUAND.ar[j - 1] + " في الحصة " + RANG.ar[r + 1] + ".",
      jourCours: (j, c) => "يدرس بن " + matNom("ar", c) + " " + QUAND.ar[j - 1] + ".",
      fin: (j, h, m) => QUAND.ar[j - 1] + "، تنتهي المدرسة " + A_HEURE.ar(h, m) + ".",
      pause: (h, m) => "تبدأ الاستراحة الكبيرة " + A_HEURE.ar(h, m) + "."
    }
  };
  for (const lg in B){ B[lg].auJour = n => QUAND[lg][n - 1]; B[lg].nom = n => nomDe(lg, n); B[lg].aHeure = A_HEURE[lg]; }

  // ---------- le branchement dans la donnée (les traductions des boutons et des fiches) ----------
  const manque = [];
  for (const lg of LANGUES){
    D.jours[lg] = JOURS[lg];
    for (const k in D.objets[APPRENDRE]){ if (OBJ[lg][cleObj(k)]) D.objets[APPRENDRE][k].trad[lg] = [nomObj(lg, k), nomObj(lg, k)]; else manque.push("objet " + k + " " + lg); }
    for (const k in D.lieux[APPRENDRE]){ if (LIEU[lg][k]) D.lieux[APPRENDRE][k].trad[lg] = LIEU[lg][k]; else manque.push("lieu " + k + " " + lg); }
    for (const a of D.actions[APPRENDRE]){ if (ACT[lg][a.id]) a.t[lg] = ACT[lg][a.id]; else manque.push("action " + a.id + " " + lg); }
    for (const k in D.raisons[APPRENDRE]){ if (RAISON[lg][k]) D.raisons[APPRENDRE][k].t[lg] = RAISON[lg][k][0]; else manque.push("raison " + k + " " + lg); }
    for (const k in D.papiers[APPRENDRE]){ if (PAPIER[lg][k]) D.papiers[APPRENDRE][k].t[lg] = PAPIER[lg][k].replace(/^(Bu |Це |To |Это |این |هذا |هذه )/, "").replace(/( است)?\.$/, ""); else manque.push("papier " + k + " " + lg); }
    for (const q in D.abholer){ if (ABHOLER[lg][q]) D.abholer[q].t[lg] = ABHOLER[lg][q]; else manque.push("abholer " + q + " " + lg); }
    for (const c in D.matieresTrad){ if (MATIERE[lg][c]) D.matieresTrad[c][lg] = matNom(lg, c); else manque.push("matiere " + c + " " + lg); }
    for (const c in D.matieres[APPRENDRE]){ const t = D.matieres[APPRENDRE][c].t; if (t) t[lg] = matNom(lg, c); }
  }
  if (manque.length) console.error("ecole/langues.js : morceaux absents", manque);
  const R = {};
  for (const lg of LANGUES) R[lg] = Object.assign({papier: k => PAPIER[lg][k]}, B[lg]);
  return R;
}
