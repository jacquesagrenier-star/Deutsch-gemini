// « Fêtes et invitations » dans les langues d'interface sans phrase traduite jusqu'ici (lot 6 de l'alignement des
// thèmes, 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour
// qui apprend l'espagnol.
//
// LE CHEMIN NATIF : la page assemble ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse
// à l'invitation selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation). On donne ici les
// morceaux dans chaque langue, rangés par clé, et la grammaire de chacune : le cas des prénoms (Анну, Feliksa,
// Anna'yı), le possessif réfléchi (на свой праздник, na swoją imprezę), le jour à l'accusatif ou au génitif
// (в субботу, до среды), le suffixe turc après l'heure, l'accord du verbe arabe avec qui agit (يدعو / تدعو).
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesFetes(D, APPRENDRE){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const sexe = n => (D.personnes[APPRENDRE] || {})[n] || D.sexe[n] || "m";
  const PARTIES = s => s.split(/ und | y | e /);
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);

  // ---------- les jours ----------
  const JOURS = {
    tr: ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"],
    uk: ["понеділок", "вівторок", "середа", "четвер", "пʼятниця", "субота", "неділя"],
    pl: ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
    ru: ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"],
    fa: ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"],
    ar: ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
  };
  const QUAND = {   // « samedi » au sens de « ce samedi-là »
    tr: JOURS.tr.map(j => j + " günü"),
    uk: ["у понеділок", "у вівторок", "у середу", "у четвер", "у пʼятницю", "у суботу", "у неділю"],
    pl: ["w poniedziałek", "we wtorek", "w środę", "w czwartek", "w piątek", "w sobotę", "w niedzielę"],
    ru: ["в понедельник", "во вторник", "в среду", "в четверг", "в пятницу", "в субботу", "в воскресенье"],
    fa: JOURS.fa, ar: JOURS.ar.map(j => "يوم " + j)
  };
  const JUSQUA = {  // « d'ici mercredi »
    tr: JOURS.tr.map(j => j + " gününe kadar"),
    uk: ["до понеділка", "до вівторка", "до середи", "до четверга", "до пʼятниці", "до суботи", "до неділі"],
    pl: ["do poniedziałku", "do wtorku", "do środy", "do czwartku", "do piątku", "do soboty", "do niedzieli"],
    ru: ["до понедельника", "до вторника", "до среды", "до четверга", "до пятницы", "до субботы", "до воскресенья"],
    fa: JOURS.fa.map(j => "تا " + j), ar: JOURS.ar.map(j => "قبل يوم " + j)
  };
  const SUF_U = {1: "'de", 2: "'de", 3: "'te", 4: "'te", 5: "'te", 6: "'da", 7: "'de", 8: "'de", 9: "'da"};
  const SUF_D = {1: "'da", 2: "'de", 3: "'da", 4: "'ta", 5: "'de"};
  const sufNb = n => n % 10 ? SUF_U[n % 10] : SUF_D[n / 10];
  const HEURE = {
    tr: h => "saat " + h + ".00" + sufNb(h), uk: h => "о " + h + ":00", pl: h => "o " + h + ":00", ru: h => "в " + h + ":00",
    fa: h => "ساعت " + h + ":00", ar: h => "في الساعة " + h + ":00"
  };

  // ---------- les prénoms : [nominatif, accusatif, génitif] (tr : [nom, acc, gén]) ----------
  const NOMS = {
    tr: {Anna: ["Anna", "Anna'yı", "Anna'nın"], Lena: ["Lena", "Lena'yı", "Lena'nın"], Felix: ["Felix", "Felix'i", "Felix'in"], Sophie: ["Sophie", "Sophie'yi", "Sophie'nin"],
         Mark: ["Mark", "Mark'ı", "Mark'ın"], Jan: ["Jan", "Jan'ı", "Jan'ın"], Katrin: ["Katrin", "Katrin'i", "Katrin'in"], Gisela: ["Gisela", "Gisela'yı", "Gisela'nın"],
         Heinz: ["Heinz", "Heinz'ı", "Heinz'ın"], Ben: ["Ben", "Ben'i", "Ben'in"]},
    uk: {Anna: ["Анна", "Анну", "Анни"], Lena: ["Лена", "Лену", "Лени"], Felix: ["Фелікс", "Фелікса", "Фелікса"], Sophie: ["Софі", "Софі", "Софі"],
         Mark: ["Марк", "Марка", "Марка"], Jan: ["Ян", "Яна", "Яна"], Katrin: ["Катрін", "Катрін", "Катрін"], Gisela: ["Гізела", "Гізелу", "Гізели"],
         Heinz: ["Гайнц", "Гайнца", "Гайнца"], Ben: ["Бен", "Бена", "Бена"]},
    ru: {Anna: ["Анна", "Анну", "Анны"], Lena: ["Лена", "Лену", "Лены"], Felix: ["Феликс", "Феликса", "Феликса"], Sophie: ["Софи", "Софи", "Софи"],
         Mark: ["Марк", "Марка", "Марка"], Jan: ["Ян", "Яна", "Яна"], Katrin: ["Катрин", "Катрин", "Катрин"], Gisela: ["Гизела", "Гизелу", "Гизелы"],
         Heinz: ["Хайнц", "Хайнца", "Хайнца"], Ben: ["Бен", "Бена", "Бена"]},
    pl: {Anna: ["Anna", "Annę", "Anny"], Lena: ["Lena", "Lenę", "Leny"], Felix: ["Felix", "Feliksa", "Feliksa"], Sophie: ["Sophie", "Sophie", "Sophie"],
         Mark: ["Mark", "Marka", "Marka"], Jan: ["Jan", "Jana", "Jana"], Katrin: ["Katrin", "Katrin", "Katrin"], Gisela: ["Gisela", "Giselę", "Giseli"],
         Heinz: ["Heinz", "Heinza", "Heinza"], Ben: ["Ben", "Bena", "Bena"]},
    fa: {Anna: "آنا", Lena: "لنا", Felix: "فلیکس", Sophie: "سوفی", Mark: "مارک", Jan: "یان", Katrin: "کاترین", Gisela: "گیزلا", Heinz: "هاینتس", Ben: "بن"},
    ar: {Anna: "آنا", Lena: "لينا", Felix: "فيليكس", Sophie: "صوفي", Mark: "مارك", Jan: "يان", Katrin: "كاترين", Gisela: "غيزيلا", Heinz: "هاينتس", Ben: "بن",
         "Inés": "إينيس", Javier: "خافيير", Carmen: "كارمن", "Tomás": "توماس", Elena: "إيلينا", Diego: "دييغو", Marta: "مارتا"}
  };
  const ET = {tr: " ve ", uk: " і ", pl: " i ", ru: " и ", fa: " و ", ar: " و"};
  // le prénom (ou les prénoms) au cas voulu : 0 nominatif, 1 accusatif, 2 génitif
  const N = (lg, n, c) => PARTIES(n).map(p => { const x = NOMS[lg][p]; return Array.isArray(x) ? x[c || 0] : (x || p); }).join(ET[lg]);

  // ---------- les fêtes : [la fête, quand, le souhait], et le genre en arabe ----------
  const FETES = {
    de: {
      tr: {geburtstag: ["bir doğum günü", null, "Doğum günün kutlu olsun!"], weihnachten: ["Noel", "aralıkta", "Mutlu Noeller!"],
           silvester: ["yılbaşı gecesi", "31 Aralık'ta", "İyi yıllar!"], neujahr: ["yılbaşı", "1 Ocak'ta", "Mutlu yıllar!"],
           ostern: ["Paskalya", "martta ya da nisanda", "Mutlu Paskalyalar!"], karneval: ["karnaval", null, null],
           hochzeit: ["bir düğün", null, "Evliliğiniz kutlu olsun!"], muttertag: ["Anneler Günü", "mayısta", "Anneler Günün kutlu olsun, anneciğim!"]},
      uk: {geburtstag: ["день народження", null, "З днем народження!"], weihnachten: ["Різдво", "у грудні", "Веселого Різдва!"],
           silvester: ["новорічна ніч", "31 грудня", "З наступаючим Новим роком!"], neujahr: ["Новий рік", "1 січня", "З Новим роком!"],
           ostern: ["Великдень", "у березні або у квітні", "Веселого Великодня!"], karneval: ["карнавал", null, null],
           hochzeit: ["весілля", null, "Вітаю з весіллям!"], muttertag: ["День матері", "у травні", "З Днем матері, мамо!"]},
      pl: {geburtstag: ["urodziny", null, "Wszystkiego najlepszego z okazji urodzin!"], weihnachten: ["Boże Narodzenie", "w grudniu", "Wesołych Świąt!"],
           silvester: ["sylwester", "31 grudnia", "Szczęśliwego Nowego Roku!"], neujahr: ["Nowy Rok", "1 stycznia", "Szczęśliwego Nowego Roku!"],
           ostern: ["Wielkanoc", "w marcu lub w kwietniu", "Wesołych Świąt Wielkanocnych!"], karneval: ["karnawał", null, null],
           hochzeit: ["ślub", null, "Gratulacje z okazji ślubu!"], muttertag: ["Dzień Matki", "w maju", "Wszystkiego najlepszego z okazji Dnia Matki, mamo!"]},
      ru: {geburtstag: ["день рождения", null, "С днём рождения!"], weihnachten: ["Рождество", "в декабре", "С Рождеством!"],
           silvester: ["новогодняя ночь", "31 декабря", "С наступающим Новым годом!"], neujahr: ["Новый год", "1 января", "С Новым годом!"],
           ostern: ["Пасха", "в марте или в апреле", "Со светлой Пасхой!"], karneval: ["карнавал", null, null],
           hochzeit: ["свадьба", null, "Поздравляю со свадьбой!"], muttertag: ["День матери", "в мае", "С Днём матери, мама!"]},
      fa: {geburtstag: ["یک جشن تولد", null, "تولدت مبارک!"], weihnachten: ["کریسمس", "در دسامبر", "کریسمس مبارک!"],
           silvester: ["شب سال نو", "31 دسامبر", "سال نو مبارک!"], neujahr: ["روز اول سال نو", "1 ژانویه", "سال نو مبارک!"],
           ostern: ["عید پاک", "در مارس یا آوریل", "عید پاک مبارک!"], karneval: ["کارناوال", null, null],
           hochzeit: ["یک عروسی", null, "ازدواجتان مبارک!"], muttertag: ["روز مادر", "در ماه مه", "روز مادر مبارک، مامان!"]},
      ar: {geburtstag: ["عيد ميلاد", null, "عيد ميلاد سعيد!"], weihnachten: ["عيد الميلاد المجيد", "في ديسمبر", "عيد ميلاد مجيد!"],
           silvester: ["ليلة رأس السنة", "في 31 ديسمبر", "كل عام وأنتم بخير!", "f"], neujahr: ["رأس السنة الميلادية", "في 1 يناير", "سنة سعيدة!"],
           ostern: ["عيد الفصح", "في مارس أو أبريل", "عيد فصح سعيد!"], karneval: ["الكرنفال", null, null],
           hochzeit: ["حفل زفاف", null, "ألف مبروك على الزواج!"], muttertag: ["عيد الأم", "في مايو", "كل عام وأنتِ بخير يا أمي!"]}
    },
    es: {
      ar: {cumpleanos: ["عيد ميلاد", null, "عيد ميلاد سعيد!"], navidad: ["عيد الميلاد المجيد", "في 25 ديسمبر", "عيد ميلاد مجيد!"],
           nochevieja: ["ليلة رأس السنة", "في 31 ديسمبر", "سنة سعيدة!", "f"], anonuevo: ["رأس السنة الميلادية", "في 1 يناير", "سنة سعيدة!"],
           reyes: ["عيد الملوك المجوس", "في 6 يناير", "عيدًا سعيدًا!"], semanasanta: ["أسبوع الآلام", "في مارس أو أبريل", null],
           carnaval: ["الكرنفال", null, null], boda: ["حفل زفاف", null, "ألف مبروك للعروسين!"], muertos: ["يوم الموتى (في المكسيك)", "في 1 و2 نوفمبر", null]}
    }
  };
  // le jour de la fête dans une phrase (« C'est l'anniversaire de Lena aujourd'hui. »)
  const SITU = {
    tr: {anniv: p => "Bugün " + N("tr", p, 2) + " doğum günü.", mariage: "Meslektaşın bugün evleniyor."},
    uk: {anniv: p => "Сьогодні в " + N("uk", p, 2) + " день народження.", mariage: "Твоя колега сьогодні виходить заміж."},
    pl: {anniv: p => "Dziś " + p + " ma urodziny.", mariage: "Twoja koleżanka z pracy dziś wychodzi za mąż."},
    ru: {anniv: p => "Сегодня у " + N("ru", p, 2) + " день рождения.", mariage: "Твоя коллега сегодня выходит замуж."},
    fa: {anniv: p => "امروز تولد " + N("fa", p) + " است.", mariage: "همکارت امروز ازدواج می‌کند."},
    ar: {anniv: p => "اليوم عيد ميلاد " + N("ar", p) + ".", mariage: "زميلتك تتزوج اليوم."}
  };
  const SITU_CLE = {geburtstag: "anniv", cumpleanos: "anniv", hochzeit: "mariage", boda: "mariage"};

  // ---------- ce qu'on apporte : [le défini, l'indéfini], en forme de glose ; et l'objet dans la phrase ----------
  const APP = {
    de: {
      tr: {kuchen: ["pasta", "bir pasta", "pastayı"], salat: ["salata", "bir salata", "salatayı"], brot: ["ekmek", "ekmek", "ekmeği"], getraenk: ["içecekler", "içecek", "içecekleri"],
           nachtisch: ["tatlı", "bir tatlı", "tatlıyı"], saft: ["meyve suyu", "meyve suyu", "meyve suyunu"], luftballon: ["balonlar", "balon", "balonları"], kerze: ["mumlar", "mum", "mumları"]},
      uk: {kuchen: ["торт", "торт"], salat: ["салат", "салат"], brot: ["хліб", "хліб"], getraenk: ["напої", "напої"], nachtisch: ["десерт", "десерт"],
           saft: ["сік", "сік"], luftballon: ["повітряні кульки", "повітряні кульки"], kerze: ["свічки", "свічки"]},
      pl: {kuchen: ["ciasto", "ciasto"], salat: ["sałatkę", "sałatkę"], brot: ["chleb", "chleb"], getraenk: ["napoje", "napoje"], nachtisch: ["deser", "deser"],
           saft: ["sok", "sok"], luftballon: ["balony", "balony"], kerze: ["świeczki", "świeczki"]},
      ru: {kuchen: ["торт", "торт"], salat: ["салат", "салат"], brot: ["хлеб", "хлеб"], getraenk: ["напитки", "напитки"], nachtisch: ["десерт", "десерт"],
           saft: ["сок", "сок"], luftballon: ["воздушные шарики", "воздушные шарики"], kerze: ["свечи", "свечи"]},
      fa: {kuchen: ["کیک", "یک کیک"], salat: ["سالاد", "یک سالاد"], brot: ["نان", "نان"], getraenk: ["نوشیدنی‌ها", "نوشیدنی"], nachtisch: ["دسر", "یک دسر"],
           saft: ["آبمیوه", "آبمیوه"], luftballon: ["بادکنک‌ها", "بادکنک"], kerze: ["شمع‌ها", "شمع"]},
      ar: {kuchen: ["الكعكة", "كعكة"], salat: ["السلطة", "سلطة"], brot: ["الخبز", "خبزًا"], getraenk: ["المشروبات", "مشروبات"], nachtisch: ["الحلوى", "حلوى"],
           saft: ["العصير", "عصيرًا"], luftballon: ["البالونات", "بالونات"], kerze: ["الشموع", "شموعًا"]}
    },
    es: {
      ar: {ensalada: ["السلطة", "سلطة"], pan: ["الخبز", "خبزًا"], postre: ["الحلوى", "حلوى"], bebida: ["المشروبات", "مشروبات"], fruta: ["الفواكه", "فواكه"],
           globo: ["البالونات", "بالونات"], uva: ["العنب", "عنبًا"]}
    }
  };
  // ---------- les motifs de l'agenda (« je dois travailler ») ----------
  const MOTIF = {
    de: {
      tr: {arbeiten: "çalışmam gerekiyor", eltern: "ailemi ziyaret ediyorum", arzt: "doktordan randevum var", training: "antrenmanım var", kino: "arkadaşlarımla sinemaya gidiyorum"},
      uk: {arbeiten: "мені треба працювати", eltern: "я відвідую батьків", arzt: "у мене прийом у лікаря", training: "у мене тренування", kino: "я йду в кіно з друзями"},
      pl: {arbeiten: "muszę pracować", eltern: "odwiedzam rodziców", arzt: "mam wizytę u lekarza", training: "mam trening", kino: "idę z przyjaciółmi do kina"},
      ru: {arbeiten: "мне нужно работать", eltern: "я навещаю родителей", arzt: "у меня приём у врача", training: "у меня тренировка", kino: "я иду в кино с друзьями"},
      fa: {arbeiten: "باید کار کنم", eltern: "به دیدن پدر و مادرم می‌روم", arzt: "نزد پزشک وقت دارم", training: "تمرین دارم", kino: "با دوستانم به سینما می‌روم"},
      ar: {arbeiten: "عليّ أن أعمل", eltern: "أزور والديّ", arzt: "لديّ موعد عند الطبيب", training: "لديّ تدريب", kino: "أذهب إلى السينما مع أصدقائي"}
    },
    es: {ar: {trabajo: "أعمل", padres: "أزور والديّ", medico: "لديّ موعد عند الطبيب", clase: "لديّ درس ألمانية", cine: "أذهب إلى السينما مع أصدقائي"}}
  };
  // ---------- les invitations : [l'événement (genre en ar), la phrase « … fête … »] ----------
  const INVIT = {
    de: {
      tr: {mark: ["parti", "Mark doğum gününü kutluyor."], ben: ["kutlama", "Ben doğum gününü kutluyor."], felix: ["parti", "Felix yılbaşı gecesini kutluyor."],
           anna: ["parti", null], grosseltern: ["yemek", "Gisela ve Heinz Noel'i kutluyor."], lena: ["kahvaltı", "Lena Paskalya'yı kutluyor."]},
      uk: {mark: ["вечірка", "Марк святкує свій день народження."], ben: ["свято", "Бен святкує свій день народження."], felix: ["вечірка", "Фелікс зустрічає Новий рік."],
           anna: ["вечірка", null], grosseltern: ["обід", "Гізела і Гайнц святкують Різдво."], lena: ["сніданок", "Лена святкує Великдень."]},
      pl: {mark: ["impreza", "Mark świętuje swoje urodziny."], ben: ["przyjęcie", "Ben świętuje swoje urodziny."], felix: ["impreza", "Felix świętuje sylwestra."],
           anna: ["impreza", null], grosseltern: ["obiad", "Gisela i Heinz świętują Boże Narodzenie."], lena: ["śniadanie", "Lena świętuje Wielkanoc."]},
      ru: {mark: ["вечеринка", "Марк празднует свой день рождения."], ben: ["праздник", "Бен празднует свой день рождения."], felix: ["вечеринка", "Феликс встречает Новый год."],
           anna: ["вечеринка", null], grosseltern: ["обед", "Гизела и Хайнц празднуют Рождество."], lena: ["завтрак", "Лена празднует Пасху."]},
      fa: {mark: ["مهمانی", "مارک تولدش را جشن می‌گیرد."], ben: ["جشن", "بن تولدش را جشن می‌گیرد."], felix: ["مهمانی", "فلیکس شب سال نو را جشن می‌گیرد."],
           anna: ["مهمانی", null], grosseltern: ["ناهار", "گیزلا و هاینتس کریسمس را جشن می‌گیرند."], lena: ["صبحانه", "لنا عید پاک را جشن می‌گیرد."]},
      ar: {mark: ["الحفلة", "يحتفل مارك بعيد ميلاده.", "f"], ben: ["الاحتفال", "يحتفل بن بعيد ميلاده."], felix: ["الحفلة", "يحتفل فيليكس بليلة رأس السنة.", "f"],
           anna: ["الحفلة", null, "f"], grosseltern: ["الغداء", "تحتفل غيزيلا وهاينتس بعيد الميلاد المجيد."], lena: ["الفطور", "تحتفل لينا بعيد الفصح."]}
    },
    es: {
      ar: {mark: ["الحفلة", "يحتفل مارك بعيد ميلاده.", "f"], ines: ["العشاء", "تحتفل إينيس بليلة رأس السنة."], boda: ["حفل الزفاف", "يحتفل خافيير ومارتا بزفافهما."],
           carmen: ["الحفلة", "تحتفل كارمن بعيد الملوك المجوس.", "f"], tomas: ["الحفلة", null, "f"]}
    }
  };
  // « Je t'invite à ma fête » (zuDe : l'allemand) : [à ma …, à sa … (réfléchi)] ; en arabe [ma, sa (m), sa (f)]
  const ZU = {
    tr: {Party: ["partime", "partisine"], Geburtstag: ["doğum günüme", "doğum gününe"], Fest: ["kutlamama", "kutlamasına"], Feier: ["kutlamama", "kutlamasına"],
         Einweihungsparty: ["yeni ev partime", "yeni ev partisine"]},
    uk: {Party: ["на моє свято", "на своє свято"], Geburtstag: ["на мій день народження", "на свій день народження"], Fest: ["на моє свято", "на своє свято"],
         Feier: ["на моє свято", "на своє свято"], Einweihungsparty: ["на моє новосілля", "на своє новосілля"]},
    pl: {Party: ["na moją imprezę", "na swoją imprezę"], Geburtstag: ["na moje urodziny", "na swoje urodziny"], Fest: ["na moje przyjęcie", "na swoje przyjęcie"],
         Feier: ["na moją uroczystość", "na swoją uroczystość"], Einweihungsparty: ["na moją parapetówkę", "na swoją parapetówkę"]},
    ru: {Party: ["на мой праздник", "на свой праздник"], Geburtstag: ["на мой день рождения", "на свой день рождения"], Fest: ["на мой праздник", "на свой праздник"],
         Feier: ["на мой праздник", "на свой праздник"], Einweihungsparty: ["на моё новоселье", "на своё новоселье"]},
    fa: {Party: ["به جشنم", "به جشنش"], Geburtstag: ["به جشن تولدم", "به جشن تولدش"], Fest: ["به جشنم", "به جشنش"], Feier: ["به جشنم", "به جشنش"],
         Einweihungsparty: ["به جشن خانهٔ جدیدم", "به جشن خانهٔ جدیدش"]},
    ar: {Party: ["إلى حفلتي", "إلى حفلته", "إلى حفلتها"], Geburtstag: ["إلى عيد ميلادي", "إلى عيد ميلاده", "إلى عيد ميلادها"],
         Fest: ["إلى احتفالي", "إلى احتفاله", "إلى احتفالها"], Feier: ["إلى احتفالي", "إلى احتفاله", "إلى احتفالها"],
         Einweihungsparty: ["إلى حفلة بيتي الجديد", "إلى حفلة بيته الجديد", "إلى حفلة بيتها الجديد"]}
  };
  // ---------- les phrases de Mark (moments) ----------
  const MOMENT = {
    tr: {einladen: "Mark arkadaşlarını davet ediyor.", karte: "Mark kız arkadaşının doğum gününü kutluyor.", mitbringen: "Mark bir salata getiriyor.",
         absagen: "Mark telefonda gelemeyeceğini söylüyor.", planen: "Mark ve Anna bir parti planlıyor.", feiern: "Mark doğum gününü kutluyor."},
    uk: {einladen: "Марк запрошує своїх друзів.", karte: "Марк вітає свою подругу з днем народження.", mitbringen: "Марк приносить салат.",
         absagen: "Марк відмовляється телефоном.", planen: "Марк і Анна планують вечірку.", feiern: "Марк святкує свій день народження."},
    pl: {einladen: "Mark zaprasza swoich przyjaciół.", karte: "Mark składa przyjaciółce życzenia urodzinowe.", mitbringen: "Mark przynosi sałatkę.",
         absagen: "Mark odwołuje przyjście przez telefon.", planen: "Mark i Anna planują imprezę.", feiern: "Mark świętuje swoje urodziny."},
    ru: {einladen: "Марк приглашает своих друзей.", karte: "Марк поздравляет подругу с днём рождения.", mitbringen: "Марк приносит салат.",
         absagen: "Марк отказывается по телефону.", planen: "Марк и Анна планируют вечеринку.", feiern: "Марк празднует свой день рождения."},
    fa: {einladen: "مارک دوستانش را دعوت می‌کند.", karte: "مارک تولد دوستش را تبریک می‌گوید.", mitbringen: "مارک یک سالاد می‌آورد.",
         absagen: "مارک تلفنی می‌گوید که نمی‌تواند بیاید.", planen: "مارک و آنا یک مهمانی را برنامه‌ریزی می‌کنند.", feiern: "مارک تولدش را جشن می‌گیرد."},
    ar: {einladen: "يدعو مارك أصدقاءه.", karte: "يهنّئ مارك صديقته بعيد ميلادها.", mitbringen: "يُحضر مارك سلطة.",
         absagen: "يعتذر مارك عن الحضور عبر الهاتف.", planen: APPRENDRE === "es" ? "يخطّط مارك لحفلة مع صديقة." : "يخطّط مارك وآنا لحفلة.", feiern: "يحتفل مارك بعيد ميلاده."}
  };
  // ---------- l'arabe seul, pour qui apprend l'espagnol : la conjugaison et « Te invito al … » ----------
  const CONJ_AR = [   // dans l'ordre de conjEs (v, p) ; {A} : ce qu'on apporte ; {V} : le verbe accordé avec {P}
    ["poder", "du", "هل تستطيع أن تأتي إلى حفلتي؟"], ["poder", "ich", "آسف، لا أستطيع المجيء."], ["traer", "ich", "أُحضر {A}."],
    ["traer", "er_sie_es", "{V} {P} {A}."], ["traer", "du", "ماذا تُحضر أنت؟"], ["invitar", "ich", "أدعوك إلى عيد ميلادي."],
    ["invitar", "sie_Sie", "يدعوك خافيير ومارتا إلى حفل زفافهما."], ["celebrar", "wir", "يوم السبت نحتفل بعيد ميلاد مارك."],
    ["venir", "du", "هل تأتي إلى عشاء ليلة رأس السنة؟"], ["ir", "ich", "شكرًا! طبعًا سآتي إلى حفلتك."], ["ir", "wir", "يوم السبت نذهب إلى حفل زفاف خافيير ومارتا."]
  ];
  const AL_AR = {"cumpleaños": "إلى عيد ميلاد {H}", boda: "إلى حفل زفاف {H}", cena: "إلى عشاء ليلة رأس السنة", fiesta: "إلى حفلة {H}"};

  // ---------- les phrases, langue par langue ----------
  const apporteAr = (p, a) => (sexe(p) === "f" ? "تُحضر " : "يُحضر ") + N("ar", p) + " " + a + ".";
  const verbeAr = (p, m, f, pl) => PARTIES(p).length > 1 ? pl || m : sexe(PARTIES(p)[0]) === "f" ? f : m;
  const F = l => FETES[APPRENDRE][l], A = l => APP[APPRENDRE][l], I = l => INVIT[APPRENDRE][l], M = l => MOTIF[APPRENDRE][l];
  const B = {
    tr: {
      fete: k => "Bu " + F("tr")[k][0] + ".",
      quand: k => maj(F("tr")[k][0]) + " " + F("tr")[k][1] + ".",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.tr.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.tr.mariage : "Bugün " + F("tr")[k][0].replace(/^bir /, "") + ".",
      apporte: (p, k, f) => p + " " + (f === "def" ? A("tr")[k][2] : A("tr")[k][1]) + " getiriyor.",
      motif: (j, m) => QUAND.tr[j] + " " + M("tr")[m] + ".",
      reponse: (j, m) => m === null ? "Davet için teşekkürler! Memnuniyetle gelirim." : "Davet için teşekkürler, ama maalesef gelemiyorum. " + QUAND.tr[j] + " " + M("tr")[m] + ".",
      oui: j => "İyi fikir! " + QUAND.tr[j] + " boşum.",
      non: (j, m, x) => QUAND.tr[j] + " olmaz: " + M("tr")[m] + ". " + QUAND.tr[x] + " nasıl?",
      accord: (a, b, j) => a + " ve " + b + " " + QUAND.tr[j] + " buluşuyor.",
      invitePerso: (H, P) => H + ", " + N("tr", P, 1) + " partisine davet ediyor.",
      leider: j => QUAND.tr[j] + " maalesef gelemem.",
      gern: H => "Teşekkürler, " + H + "! Partine memnuniyetle gelirim.",
      inviteA: (H, P, mot) => H + ", " + N("tr", P, 1) + " " + ZU.tr[mot][1] + " davet ediyor.",
      libre: j => QUAND.tr[j] + " boşum.",
      invite: mot => "Seni " + ZU.tr[mot][0] + " davet ediyorum.",
      evtJour: (inv, j) => maj(I("tr")[inv.id][0]) + " " + QUAND.tr[j] + ".",
      evtHeure: inv => maj(I("tr")[inv.id][0]) + " " + HEURE.tr(inv.heure) + " başlıyor.",
      repondre: (invite, j) => invite + " " + JUSQUA.tr[j] + " cevap vermeli.",
      inviteQui: (inv, invite) => inv.hote.replace(" und ", " ve ") + ", " + N("tr", invite, 1) + " davet ediyor."
    },
    uk: {
      fete: k => "Це " + F("uk")[k][0] + ".",
      quand: k => maj(F("uk")[k][0]) + " — " + F("uk")[k][1] + ".",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.uk.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.uk.mariage : "Сьогодні " + F("uk")[k][0] + ".",
      apporte: (p, k, f) => N("uk", p) + " приносить " + A("uk")[k][f === "def" ? 0 : 1] + ".",
      motif: (j, m) => maj(QUAND.uk[j]) + " " + M("uk")[m] + ".",
      reponse: (j, m) => m === null ? "Дякую за запрошення! Із задоволенням прийду." : "Дякую за запрошення, але, на жаль, не можу. " + maj(QUAND.uk[j]) + " " + M("uk")[m] + ".",
      oui: j => "Гарна ідея! " + maj(QUAND.uk[j]) + " в мене є час.",
      non: (j, m, x) => maj(QUAND.uk[j]) + " не можу: " + M("uk")[m] + ". Може, " + QUAND.uk[x] + "?",
      accord: (a, b, j) => N("uk", a) + " і " + N("uk", b) + " зустрічаються " + QUAND.uk[j] + ".",
      invitePerso: (H, P) => N("uk", H) + " запрошує " + N("uk", P, 1) + " на своє свято.",
      leider: j => maj(QUAND.uk[j]) + ", на жаль, не можу прийти.",
      gern: H => "Дякую, " + N("uk", H) + "! Із задоволенням прийду на твоє свято.",
      inviteA: (H, P, mot) => N("uk", H) + " запрошує " + N("uk", P, 1) + " " + ZU.uk[mot][1] + ".",
      libre: j => maj(QUAND.uk[j]) + " в мене є час.",
      invite: mot => "Запрошую тебе " + ZU.uk[mot][0] + ".",
      evtJour: (inv, j) => maj(I("uk")[inv.id][0]) + " " + QUAND.uk[j] + ".",
      evtHeure: inv => maj(I("uk")[inv.id][0]) + " починається " + HEURE.uk(inv.heure) + ".",
      repondre: (invite, j) => N("uk", invite) + " має відповісти " + JUSQUA.uk[j] + ".",
      inviteQui: (inv, invite) => N("uk", inv.hote) + (inv.s === "pl" ? " запрошують " : " запрошує ") + N("uk", invite, 1) + "."
    },
    pl: {
      fete: k => "To " + F("pl")[k][0] + ".",
      quand: k => maj(F("pl")[k][0]) + " " + (k === "geburtstag" ? "są " : "jest ") + F("pl")[k][1] + ".",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.pl.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.pl.mariage : "Dziś jest " + F("pl")[k][0] + ".",
      apporte: (p, k, f) => p + " przynosi " + A("pl")[k][f === "def" ? 0 : 1] + ".",
      motif: (j, m) => maj(QUAND.pl[j]) + " " + M("pl")[m] + ".",
      reponse: (j, m) => m === null ? "Dziękuję za zaproszenie! Chętnie przyjdę." : "Dziękuję za zaproszenie, ale niestety nie mogę. " + maj(QUAND.pl[j]) + " " + M("pl")[m] + ".",
      oui: j => "Dobry pomysł! " + maj(QUAND.pl[j]) + " mam czas.",
      non: (j, m, x) => maj(QUAND.pl[j]) + " nie mogę: " + M("pl")[m] + ". Może " + QUAND.pl[x] + "?",
      accord: (a, b, j) => a + " i " + b + " spotykają się " + QUAND.pl[j] + ".",
      invitePerso: (H, P) => H + " zaprasza " + N("pl", P, 1) + " na swoją imprezę.",
      leider: j => maj(QUAND.pl[j]) + " niestety nie mogę przyjść.",
      gern: H => "Dziękuję, " + H + "! Chętnie przyjdę na twoją imprezę.",
      inviteA: (H, P, mot) => H + " zaprasza " + N("pl", P, 1) + " " + ZU.pl[mot][1] + ".",
      libre: j => maj(QUAND.pl[j]) + " mam czas.",
      invite: mot => "Zapraszam cię " + ZU.pl[mot][0] + ".",
      evtJour: (inv, j) => maj(I("pl")[inv.id][0]) + " jest " + QUAND.pl[j] + ".",
      evtHeure: inv => maj(I("pl")[inv.id][0]) + " zaczyna się " + HEURE.pl(inv.heure) + ".",
      repondre: (invite, j) => invite + " musi odpowiedzieć " + JUSQUA.pl[j] + ".",
      inviteQui: (inv, invite) => inv.hote.replace(" und ", " i ") + (inv.s === "pl" ? " zapraszają " : " zaprasza ") + N("pl", invite, 1) + "."
    },
    ru: {
      fete: k => "Это " + F("ru")[k][0] + ".",
      quand: k => maj(F("ru")[k][0]) + " — " + F("ru")[k][1] + ".",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.ru.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.ru.mariage : "Сегодня " + F("ru")[k][0] + ".",
      apporte: (p, k, f) => N("ru", p) + " приносит " + A("ru")[k][f === "def" ? 0 : 1] + ".",
      motif: (j, m) => maj(QUAND.ru[j]) + " " + M("ru")[m] + ".",
      reponse: (j, m) => m === null ? "Спасибо за приглашение! С удовольствием приду." : "Спасибо за приглашение, но, к сожалению, я не могу. " + maj(QUAND.ru[j]) + " " + M("ru")[m] + ".",
      oui: j => "Хорошая идея! " + maj(QUAND.ru[j]) + " у меня есть время.",
      non: (j, m, x) => maj(QUAND.ru[j]) + " не могу: " + M("ru")[m] + ". Может, " + QUAND.ru[x] + "?",
      accord: (a, b, j) => N("ru", a) + " и " + N("ru", b) + " встречаются " + QUAND.ru[j] + ".",
      invitePerso: (H, P) => N("ru", H) + " приглашает " + N("ru", P, 1) + " на свой праздник.",
      leider: j => maj(QUAND.ru[j]) + ", к сожалению, не смогу прийти.",
      gern: H => "Спасибо, " + N("ru", H) + "! С удовольствием приду на твой праздник.",
      inviteA: (H, P, mot) => N("ru", H) + " приглашает " + N("ru", P, 1) + " " + ZU.ru[mot][1] + ".",
      libre: j => maj(QUAND.ru[j]) + " у меня есть время.",
      invite: mot => "Приглашаю тебя " + ZU.ru[mot][0] + ".",
      evtJour: (inv, j) => maj(I("ru")[inv.id][0]) + " " + QUAND.ru[j] + ".",
      evtHeure: inv => maj(I("ru")[inv.id][0]) + " начинается " + HEURE.ru(inv.heure) + ".",
      repondre: (invite, j) => N("ru", invite) + (sexe(invite) === "f" ? " должна" : " должен") + " ответить " + JUSQUA.ru[j] + ".",
      inviteQui: (inv, invite) => N("ru", inv.hote) + (inv.s === "pl" ? " приглашают " : " приглашает ") + N("ru", invite, 1) + "."
    },
    fa: {
      fete: k => "این " + F("fa")[k][0] + " است.",
      quand: k => F("fa")[k][0] + " " + F("fa")[k][1] + " است.",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.fa.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.fa.mariage : "امروز " + F("fa")[k][0].replace(/^یک /, "") + " است.",
      apporte: (p, k, f) => N("fa", p) + " " + (f === "def" ? A("fa")[k][0] + " را" : A("fa")[k][1]) + " می‌آورد.",
      motif: (j, m) => QUAND.fa[j] + " " + M("fa")[m] + ".",
      reponse: (j, m) => m === null ? "ممنون از دعوتت! با کمال میل می‌آیم." : "ممنون از دعوتت، ولی متأسفانه نمی‌توانم. " + QUAND.fa[j] + " " + M("fa")[m] + ".",
      oui: j => "فکر خوبی است! " + QUAND.fa[j] + " وقت دارم.",
      non: (j, m, x) => QUAND.fa[j] + " نمی‌توانم: " + M("fa")[m] + ". " + QUAND.fa[x] + " چطور است؟",
      accord: (a, b, j) => N("fa", a) + " و " + N("fa", b) + " " + QUAND.fa[j] + " همدیگر را می‌بینند.",
      invitePerso: (H, P) => N("fa", H) + " " + N("fa", P) + " را به جشنش دعوت می‌کند.",
      leider: j => QUAND.fa[j] + " متأسفانه نمی‌توانم بیایم.",
      gern: H => "ممنون، " + N("fa", H) + "! با کمال میل به جشنت می‌آیم.",
      inviteA: (H, P, mot) => N("fa", H) + " " + N("fa", P) + " را " + ZU.fa[mot][1] + " دعوت می‌کند.",
      libre: j => QUAND.fa[j] + " وقت دارم.",
      invite: mot => "تو را " + ZU.fa[mot][0] + " دعوت می‌کنم.",
      evtJour: (inv, j) => I("fa")[inv.id][0] + " " + QUAND.fa[j] + " است.",
      evtHeure: inv => I("fa")[inv.id][0] + " " + HEURE.fa(inv.heure) + " شروع می‌شود.",
      repondre: (invite, j) => N("fa", invite) + " باید " + JUSQUA.fa[j] + " جواب بدهد.",
      inviteQui: (inv, invite) => N("fa", inv.hote) + " " + N("fa", invite) + " را دعوت " + (inv.s === "pl" ? "می‌کنند." : "می‌کند.")
    },
    ar: {
      fete: k => (F("ar")[k][3] === "f" ? "هذه " : "هذا ") + F("ar")[k][0] + ".",
      quand: k => F("ar")[k][0] + " " + F("ar")[k][1] + ".",
      situation: (k, p) => SITU_CLE[k] === "anniv" ? SITU.ar.anniv(p) : SITU_CLE[k] === "mariage" ? SITU.ar.mariage : "اليوم " + F("ar")[k][0] + ".",
      apporte: (p, k, f) => apporteAr(p, A("ar")[k][f === "def" ? 0 : 1]),
      motif: (j, m) => QUAND.ar[j] + " " + M("ar")[m] + ".",
      reponse: (j, m) => m === null ? "شكرًا على الدعوة! سآتي بكل سرور." : "شكرًا على الدعوة، لكن للأسف لا أستطيع. " + QUAND.ar[j] + " " + M("ar")[m] + ".",
      oui: j => "فكرة جيدة! لديّ وقت " + QUAND.ar[j] + ".",
      non: (j, m, x) => QUAND.ar[j] + " لا أستطيع: " + M("ar")[m] + ". ما رأيك في " + QUAND.ar[x] + "؟",
      accord: (a, b, j) => (sexe(a) === "f" ? "تلتقي " : "يلتقي ") + N("ar", a) + " و" + N("ar", b) + " " + QUAND.ar[j] + ".",
      invitePerso: (H, P) => (sexe(H) === "f" ? "تدعو " : "يدعو ") + N("ar", H) + " " + N("ar", P) + (sexe(H) === "f" ? " إلى حفلتها." : " إلى حفلته."),
      leider: j => QUAND.ar[j] + " للأسف لا أستطيع المجيء.",
      gern: H => "شكرًا يا " + N("ar", H) + "! سآتي إلى حفلتك بكل سرور.",
      inviteA: (H, P, mot) => (sexe(H) === "f" ? "تدعو " : "يدعو ") + N("ar", H) + " " + N("ar", P) + " " + ZU.ar[mot][sexe(H) === "f" ? 2 : 1] + ".",
      libre: j => "لديّ وقت " + QUAND.ar[j] + ".",
      invite: mot => "أدعوك " + ZU.ar[mot][0] + ".",
      evtJour: (inv, j) => I("ar")[inv.id][0] + " " + QUAND.ar[j] + ".",
      evtHeure: inv => (I("ar")[inv.id][2] === "f" ? "تبدأ " : "يبدأ ") + I("ar")[inv.id][0] + " " + HEURE.ar(inv.heure) + ".",
      repondre: (invite, j) => "على " + N("ar", invite) + " أن " + (sexe(invite) === "f" ? "ترد " : "يرد ") + JUSQUA.ar[j] + ".",
      inviteQui: (inv, invite) => verbeAr(inv.hote, "يدعو ", "تدعو ") + N("ar", inv.hote) + " " + N("ar", invite) + ".",
      // l'espagnol seulement
      inviteEs: (mot, h) => "أدعوك " + AL_AR[mot].replace("{H}", h ? N("ar", h) : "") + ".",
      conj: (x, k, P) => { const c = CONJ_AR.find(y => y[0] === x.v && y[1] === x.p); if (!c) return null;
        return c[2].replace("{A}", A("ar")[k][0]).replace("{V}", sexe(P) === "f" ? "تُحضر" : "يُحضر").replace("{P}", N("ar", P)); }
    }
  };

  // ---------- le branchement dans la donnée (les traductions des boutons, de la fête, des moments) ----------
  const manque = [];
  const poser = (obj, cle, lg, v, quoi) => { if (v === undefined) manque.push(quoi + " " + cle + " " + lg); else obj[lg] = v; };
  for (const lg of LANGUES){
    D.jours[lg] = JOURS[lg];
    for (const k in D.fetes[APPRENDRE]) poser(D.fetes[APPRENDRE][k].t, k, lg, F(lg)[k] && F(lg)[k].slice(0, 3), "fete");
    for (const k in D.apports[APPRENDRE]) poser(D.apports[APPRENDRE][k].t, k, lg, A(lg)[k] && A(lg)[k].slice(0, 2), "apport");
    for (const k in D.motifs[APPRENDRE]) poser(D.motifs[APPRENDRE][k].t, k, lg, M(lg)[k], "motif");
    for (const inv of D.invitations[APPRENDRE]) poser(inv.t, inv.id, lg, I(lg)[inv.id] && I(lg)[inv.id].slice(0, 2), "invitation");
    for (const m of D.moments){ poser(m.t, m.id, lg, MOMENT[lg][m.id], "moment"); if (m.t_es) m.t_es[lg] = MOMENT[lg][m.id]; }
    if (APPRENDRE === "de") for (const x of D.zuDe) poser(x.t, x.mot, lg, ZU[lg][x.mot] && ZU[lg][x.mot][0], "zu");
    if (APPRENDRE === "es") for (const x of D.alEs) poser(x.t, x.mot, lg, AL_AR[x.mot], "al");
  }
  if (manque.length) console.error("fetes/langues.js : morceaux absents", manque);
  const R = {};
  for (const lg of LANGUES){ R[lg] = B[lg]; R[lg].nom = n => N(lg, n); }
  return R;
}
