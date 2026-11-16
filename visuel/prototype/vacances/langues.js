// « Les vacances et le voyage » dans les langues d'interface sans phrase traduite jusqu'ici (lot 8 de l'alignement des
// thèmes, 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour
// qui apprend l'espagnol.
//
// LE CHEMIN NATIF : la page raconte au passé les voyages d'Anna, de Mark et de la famille, étape par étape, à la personne
// que pose la question (je, tu, nous, ou le sujet de l'étape). On donne ici chaque étape conjuguée dans chaque langue :
// le passé slave s'accorde au genre (« собрал / собрала / собрали ») — pour « je » et « tu », dont le genre n'est pas
// connu, les deux formes, comme le « allé(e) » du français ; le polonais porte la personne dans le verbe (spakowałem,
// spakowałaś, spakowaliśmy) ; le turc, le persan et l'arabe ont une forme par personne, et l'arabe accorde le verbe au
// sujet (le duel de Ben et Mia quand le sujet est sous-entendu : « بنيا »). Le possessif suit la personne
// (« свой чемодан », « bavulumu / bavulunu », « حقيبتي / حقيبتها »).
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesVacances(D, APPRENDRE){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);

  // ---------- les sujets : [nom, genre, pronom] ----------
  const SUJ = {
    ru: {Anna: ["Анна", "f", "она"], Mark: ["Марк", "m", "он"], familia: ["Семья", "f", "она"], BenMia: ["Бен и Мия", "pl", "они"]},
    uk: {Anna: ["Анна", "f", "вона"], Mark: ["Марк", "m", "він"], familia: ["Родина", "f", "вона"], BenMia: ["Бен і Мія", "pl", "вони"]},
    pl: {Anna: ["Anna", "f"], Mark: ["Mark", "m"], familia: ["Rodzina", "f"], BenMia: ["Ben i Mia", "pl"]},
    tr: {Anna: ["Anna"], Mark: ["Mark"], familia: ["Aile"], BenMia: ["Ben ve Mia"]},
    fa: {Anna: ["آنا"], Mark: ["مارک"], familia: ["خانواده"], BenMia: ["بن و میا"]},
    ar: {Anna: ["آنا"], Mark: ["مارك"], familia: ["العائلة"], BenMia: ["بن وميا"]}
  };
  // ---------- les étapes ----------
  // ru, uk, pl : [3e m, 3e f, 3e pluriel, complément] ; tr, fa : [je, tu, nous, sujet] ; ar : {p: [je, tu, nous], v: verbe
  // avant le sujet, d: verbe sans sujet (le sujet d'avant), c: complément}
  const ET = {
    ru: {"anna-koffer": ["собрал", "собрала", "собрали", "свой чемодан"], "anna-flughafen": ["поехал", "поехала", "поехали", "в аэропорт"],
         "anna-flug": ["полетел", "полетела", "полетели", "в Малагу"], "anna-meer": ["плавал", "плавала", "плавали", "в море"],
         "anna-eis": ["ел", "ела", "ели", "мороженое на пляже"], "anna-altstadt": ["осмотрел", "осмотрела", "осмотрели", "старый город"],
         "anna-souvenirs": ["купил", "купила", "купили", "сувениры"], "mark-rucksack": ["собрал", "собрала", "собрали", "свой рюкзак"],
         "mark-zug": ["поехал", "поехала", "поехали", "в Гамбург на поезде"], "mark-hotel": ["приехал", "приехала", "приехали", "в гостиницу"],
         "mark-hafen": ["прокатился", "прокатилась", "прокатились", "на катере по порту"], "mark-fisch": ["съел", "съела", "съели", "бутерброд с рыбой"],
         "mark-museum": ["пошёл", "пошла", "пошли", "в музей"], "mark-postkarte": ["написал", "написала", "написали", "открытку"],
         "familia-auto": ["поехал", "поехала", "поехали", "на машине на Балтийское море"], "familia-wohnung": ["снял", "сняла", "сняли", "квартиру на время отпуска"],
         "familia-sandburg": ["построил", "построила", "построили", "замок из песка"], "familia-baden": ["купался", "купалась", "купались", "в море"],
         "familia-rad": ["катался", "каталась", "катались", "на велосипеде вдоль пляжа"], "familia-karten": ["играл", "играла", "играли", "в карты"]},
    uk: {"anna-koffer": ["зібрав", "зібрала", "зібрали", "свою валізу"], "anna-flughafen": ["поїхав", "поїхала", "поїхали", "до аеропорту"],
         "anna-flug": ["полетів", "полетіла", "полетіли", "до Малаги"], "anna-meer": ["плавав", "плавала", "плавали", "у морі"],
         "anna-eis": ["їв", "їла", "їли", "морозиво на пляжі"], "anna-altstadt": ["оглянув", "оглянула", "оглянули", "старе місто"],
         "anna-souvenirs": ["купив", "купила", "купили", "сувеніри"], "mark-rucksack": ["зібрав", "зібрала", "зібрали", "свій рюкзак"],
         "mark-zug": ["поїхав", "поїхала", "поїхали", "до Гамбурга поїздом"], "mark-hotel": ["приїхав", "приїхала", "приїхали", "до готелю"],
         "mark-hafen": ["покатався", "покаталася", "покаталися", "на катері по порту"], "mark-fisch": ["зʼїв", "зʼїла", "зʼїли", "бутерброд із рибою"],
         "mark-museum": ["пішов", "пішла", "пішли", "до музею"], "mark-postkarte": ["написав", "написала", "написали", "листівку"],
         "familia-auto": ["поїхав", "поїхала", "поїхали", "машиною до Балтійського моря"], "familia-wohnung": ["зняв", "зняла", "зняли", "квартиру на час відпустки"],
         "familia-sandburg": ["збудував", "збудувала", "збудували", "замок із піску"], "familia-baden": ["купався", "купалася", "купалися", "у морі"],
         "familia-rad": ["катався", "каталася", "каталися", "на велосипеді вздовж пляжу"], "familia-karten": ["грав", "грала", "грали", "в карти"]},
    pl: {"anna-koffer": ["spakował", "spakowała", "spakowali", "swoją walizkę"], "anna-flughafen": ["pojechał", "pojechała", "pojechali", "na lotnisko"],
         "anna-flug": ["poleciał", "poleciała", "polecieli", "do Malagi"], "anna-meer": ["pływał", "pływała", "pływali", "w morzu"],
         "anna-eis": ["zjadł", "zjadła", "zjedli", "lody na plaży"], "anna-altstadt": ["zwiedził", "zwiedziła", "zwiedzili", "stare miasto"],
         "anna-souvenirs": ["kupił", "kupiła", "kupili", "pamiątki"], "mark-rucksack": ["spakował", "spakowała", "spakowali", "swój plecak"],
         "mark-zug": ["pojechał", "pojechała", "pojechali", "pociągiem do Hamburga"], "mark-hotel": ["dotarł", "dotarła", "dotarli", "do hotelu"],
         "mark-hafen": ["popłynął", "popłynęła", "popłynęli", "statkiem po porcie"], "mark-fisch": ["zjadł", "zjadła", "zjedli", "kanapkę z rybą"],
         "mark-museum": ["poszedł", "poszła", "poszli", "do muzeum"], "mark-postkarte": ["napisał", "napisała", "napisali", "pocztówkę"],
         "familia-auto": ["pojechał", "pojechała", "pojechali", "samochodem nad Bałtyk"], "familia-wohnung": ["wynajął", "wynajęła", "wynajęli", "mieszkanie wakacyjne"],
         "familia-sandburg": ["zbudował", "zbudowała", "zbudowali", "zamek z piasku"], "familia-baden": ["kąpał", "kąpała", "kąpali", "się w morzu"],
         "familia-rad": ["jeździł", "jeździła", "jeździli", "na rowerze wzdłuż plaży"], "familia-karten": ["grał", "grała", "grali", "w karty"]},
    tr: {"anna-koffer": ["bavulumu topladım", "bavulunu topladın", "bavullarımızı topladık", "bavulunu topladı"],
         "anna-flughafen": ["havalimanına gittim", "havalimanına gittin", "havalimanına gittik", "havalimanına gitti"],
         "anna-flug": ["Málaga'ya uçtum", "Málaga'ya uçtun", "Málaga'ya uçtuk", "Málaga'ya uçtu"],
         "anna-meer": ["denizde yüzdüm", "denizde yüzdün", "denizde yüzdük", "denizde yüzdü"],
         "anna-eis": ["plajda dondurma yedim", "plajda dondurma yedin", "plajda dondurma yedik", "plajda dondurma yedi"],
         "anna-altstadt": ["eski şehri gezdim", "eski şehri gezdin", "eski şehri gezdik", "eski şehri gezdi"],
         "anna-souvenirs": ["hediyelik eşya aldım", "hediyelik eşya aldın", "hediyelik eşya aldık", "hediyelik eşya aldı"],
         "mark-rucksack": ["sırt çantamı hazırladım", "sırt çantanı hazırladın", "sırt çantalarımızı hazırladık", "sırt çantasını hazırladı"],
         "mark-zug": ["trenle Hamburg'a gittim", "trenle Hamburg'a gittin", "trenle Hamburg'a gittik", "trenle Hamburg'a gitti"],
         "mark-hotel": ["otele vardım", "otele vardın", "otele vardık", "otele vardı"],
         "mark-hafen": ["limanda tekne turu yaptım", "limanda tekne turu yaptın", "limanda tekne turu yaptık", "limanda tekne turu yaptı"],
         "mark-fisch": ["balık ekmek yedim", "balık ekmek yedin", "balık ekmek yedik", "balık ekmek yedi"],
         "mark-museum": ["müzeye gittim", "müzeye gittin", "müzeye gittik", "müzeye gitti"],
         "mark-postkarte": ["bir kartpostal yazdım", "bir kartpostal yazdın", "bir kartpostal yazdık", "bir kartpostal yazdı"],
         "familia-auto": ["arabayla Baltık Denizi'ne gittim", "arabayla Baltık Denizi'ne gittin", "arabayla Baltık Denizi'ne gittik", "arabayla Baltık Denizi'ne gitti"],
         "familia-wohnung": ["bir tatil dairesi kiraladım", "bir tatil dairesi kiraladın", "bir tatil dairesi kiraladık", "bir tatil dairesi kiraladı"],
         "familia-sandburg": ["kumdan bir kale yaptım", "kumdan bir kale yaptın", "kumdan bir kale yaptık", "kumdan bir kale yaptılar"],
         "familia-baden": ["denizde yüzdüm", "denizde yüzdün", "denizde yüzdük", "denizde yüzdüler"],
         "familia-rad": ["sahil boyunca bisiklete bindim", "sahil boyunca bisiklete bindin", "sahil boyunca bisiklete bindik", "sahil boyunca bisiklete bindi"],
         "familia-karten": ["kâğıt oynadım", "kâğıt oynadın", "kâğıt oynadık", "kâğıt oynadı"]},
    fa: {"anna-koffer": ["چمدانم را بستم", "چمدانت را بستی", "چمدان‌هایمان را بستیم", "چمدانش را بست"],
         "anna-flughafen": ["به فرودگاه رفتم", "به فرودگاه رفتی", "به فرودگاه رفتیم", "به فرودگاه رفت"],
         "anna-flug": ["با هواپیما به مالاگا رفتم", "با هواپیما به مالاگا رفتی", "با هواپیما به مالاگا رفتیم", "با هواپیما به مالاگا رفت"],
         "anna-meer": ["در دریا شنا کردم", "در دریا شنا کردی", "در دریا شنا کردیم", "در دریا شنا کرد"],
         "anna-eis": ["در ساحل بستنی خوردم", "در ساحل بستنی خوردی", "در ساحل بستنی خوردیم", "در ساحل بستنی خورد"],
         "anna-altstadt": ["از شهر قدیمی دیدن کردم", "از شهر قدیمی دیدن کردی", "از شهر قدیمی دیدن کردیم", "از شهر قدیمی دیدن کرد"],
         "anna-souvenirs": ["سوغاتی خریدم", "سوغاتی خریدی", "سوغاتی خریدیم", "سوغاتی خرید"],
         "mark-rucksack": ["کوله‌پشتی‌ام را بستم", "کوله‌پشتی‌ات را بستی", "کوله‌پشتی‌هایمان را بستیم", "کوله‌پشتی‌اش را بست"],
         "mark-zug": ["با قطار به هامبورگ رفتم", "با قطار به هامبورگ رفتی", "با قطار به هامبورگ رفتیم", "با قطار به هامبورگ رفت"],
         "mark-hotel": ["به هتل رسیدم", "به هتل رسیدی", "به هتل رسیدیم", "به هتل رسید"],
         "mark-hafen": ["با قایق در بندر گشت زدم", "با قایق در بندر گشت زدی", "با قایق در بندر گشت زدیم", "با قایق در بندر گشت زد"],
         "mark-fisch": ["یک ساندویچ ماهی خوردم", "یک ساندویچ ماهی خوردی", "یک ساندویچ ماهی خوردیم", "یک ساندویچ ماهی خورد"],
         "mark-museum": ["به موزه رفتم", "به موزه رفتی", "به موزه رفتیم", "به موزه رفت"],
         "mark-postkarte": ["یک کارت‌پستال نوشتم", "یک کارت‌پستال نوشتی", "یک کارت‌پستال نوشتیم", "یک کارت‌پستال نوشت"],
         "familia-auto": ["با ماشین به دریای بالتیک رفتم", "با ماشین به دریای بالتیک رفتی", "با ماشین به دریای بالتیک رفتیم", "با ماشین به دریای بالتیک رفت"],
         "familia-wohnung": ["یک آپارتمان برای تعطیلات اجاره کردم", "یک آپارتمان برای تعطیلات اجاره کردی", "یک آپارتمان برای تعطیلات اجاره کردیم", "یک آپارتمان برای تعطیلات اجاره کرد"],
         "familia-sandburg": ["یک قلعهٔ شنی ساختم", "یک قلعهٔ شنی ساختی", "یک قلعهٔ شنی ساختیم", "یک قلعهٔ شنی ساختند"],
         "familia-baden": ["در دریا آب‌تنی کردم", "در دریا آب‌تنی کردی", "در دریا آب‌تنی کردیم", "در دریا آب‌تنی کردند"],
         "familia-rad": ["در امتداد ساحل دوچرخه‌سواری کردم", "در امتداد ساحل دوچرخه‌سواری کردی", "در امتداد ساحل دوچرخه‌سواری کردیم", "در امتداد ساحل دوچرخه‌سواری کرد"],
         "familia-karten": ["ورق بازی کردم", "ورق بازی کردی", "ورق بازی کردیم", "ورق بازی کرد"]},
    ar: {"anna-koffer": {p: ["حزمتُ حقيبتي", "حزمتَ حقيبتك", "حزمنا حقائبنا"], v: "حزمت", d: "حزمت", c: "حقيبتها"},
         "anna-flughafen": {p: ["ذهبتُ إلى المطار", "ذهبتَ إلى المطار", "ذهبنا إلى المطار"], v: "ذهبت", d: "ذهبت", c: "إلى المطار"},
         "anna-flug": {p: ["سافرتُ بالطائرة إلى مالقة", "سافرتَ بالطائرة إلى مالقة", "سافرنا بالطائرة إلى مالقة"], v: "سافرت", d: "سافرت", c: "بالطائرة إلى مالقة"},
         "anna-meer": {p: ["سبحتُ في البحر", "سبحتَ في البحر", "سبحنا في البحر"], v: "سبحت", d: "سبحت", c: "في البحر"},
         "anna-eis": {p: ["أكلتُ بوظة على الشاطئ", "أكلتَ بوظة على الشاطئ", "أكلنا بوظة على الشاطئ"], v: "أكلت", d: "أكلت", c: "بوظة على الشاطئ"},
         "anna-altstadt": {p: ["زرتُ المدينة القديمة", "زرتَ المدينة القديمة", "زرنا المدينة القديمة"], v: "زارت", d: "زارت", c: "المدينة القديمة"},
         "anna-souvenirs": {p: ["اشتريتُ تذكارات", "اشتريتَ تذكارات", "اشترينا تذكارات"], v: "اشترت", d: "اشترت", c: "تذكارات"},
         "mark-rucksack": {p: ["حزمتُ حقيبة ظهري", "حزمتَ حقيبة ظهرك", "حزمنا حقائب ظهرنا"], v: "حزم", d: "حزم", c: "حقيبة ظهره"},
         "mark-zug": {p: ["ذهبتُ إلى هامبورغ بالقطار", "ذهبتَ إلى هامبورغ بالقطار", "ذهبنا إلى هامبورغ بالقطار"], v: "ذهب", d: "ذهب", c: "إلى هامبورغ بالقطار"},
         "mark-hotel": {p: ["وصلتُ إلى الفندق", "وصلتَ إلى الفندق", "وصلنا إلى الفندق"], v: "وصل", d: "وصل", c: "إلى الفندق"},
         "mark-hafen": {p: ["قمتُ بجولة بالقارب في الميناء", "قمتَ بجولة بالقارب في الميناء", "قمنا بجولة بالقارب في الميناء"], v: "قام", d: "قام", c: "بجولة بالقارب في الميناء"},
         "mark-fisch": {p: ["أكلتُ شطيرة سمك", "أكلتَ شطيرة سمك", "أكلنا شطيرة سمك"], v: "أكل", d: "أكل", c: "شطيرة سمك"},
         "mark-museum": {p: ["ذهبتُ إلى المتحف", "ذهبتَ إلى المتحف", "ذهبنا إلى المتحف"], v: "ذهب", d: "ذهب", c: "إلى المتحف"},
         "mark-postkarte": {p: ["كتبتُ بطاقة بريدية", "كتبتَ بطاقة بريدية", "كتبنا بطاقة بريدية"], v: "كتب", d: "كتب", c: "بطاقة بريدية"},
         "familia-auto": {p: ["ذهبتُ بالسيارة إلى بحر البلطيق", "ذهبتَ بالسيارة إلى بحر البلطيق", "ذهبنا بالسيارة إلى بحر البلطيق"], v: "ذهبت", d: "ذهبت", c: "بالسيارة إلى بحر البلطيق"},
         "familia-wohnung": {p: ["استأجرتُ شقة لقضاء العطلة", "استأجرتَ شقة لقضاء العطلة", "استأجرنا شقة لقضاء العطلة"], v: "استأجرت", d: "استأجرت", c: "شقة لقضاء العطلة"},
         "familia-sandburg": {p: ["بنيتُ قلعة من الرمل", "بنيتَ قلعة من الرمل", "بنينا قلعة من الرمل"], v: "بنى", d: "بنيا", c: "قلعة من الرمل"},
         "familia-baden": {p: ["سبحتُ في البحر", "سبحتَ في البحر", "سبحنا في البحر"], v: "سبح", d: "سبحا", c: "في البحر"},
         "familia-rad": {p: ["ركبتُ الدراجة على طول الشاطئ", "ركبتَ الدراجة على طول الشاطئ", "ركبنا الدراجات على طول الشاطئ"], v: "ركبت", d: "ركبت", c: "الدراجات على طول الشاطئ"},
         "familia-karten": {p: ["لعبتُ الورق", "لعبتَ الورق", "لعبنا الورق"], v: "لعبت", d: "لعبت", c: "الورق"}}
  };
  const QUAND = {
    ru: {anna: "В октябре", mark: "В прошлые выходные", familia: "Прошлым летом"},
    uk: {anna: "У жовтні", mark: "Минулих вихідних", familia: "Минулого літа"},
    pl: {anna: "W październiku", mark: "W zeszły weekend", familia: "Zeszłego lata"},
    tr: {anna: "Ekimde", mark: "Geçen hafta sonu", familia: "Geçen yaz"},
    fa: {anna: "در ماه اکتبر", mark: "آخر هفتهٔ گذشته", familia: "تابستان گذشته"},
    ar: {anna: "في أكتوبر،", mark: "في عطلة نهاية الأسبوع الماضية،", familia: "في الصيف الماضي،"}
  };
  const LIENS = {ru: ["Сначала", "Потом", "Затем", "Наконец"], uk: ["Спочатку", "Потім", "Далі", "Нарешті"], pl: ["Najpierw", "Potem", "Następnie", "Na koniec"],
                 tr: ["Önce", "Sonra", "Ardından", "En sonunda"], fa: ["اول", "بعد", "سپس", "در آخر"], ar: ["أولًا،", "ثم", "بعد ذلك", "وأخيرًا"]};
  const METEO = {
    ru: {sonne: "Светило солнце.", warm: "Было тепло.", regen: "Шёл дождь.", kalt: "Было холодно.", schnee: "Шёл снег."},
    uk: {sonne: "Світило сонце.", warm: "Було тепло.", regen: "Ішов дощ.", kalt: "Було холодно.", schnee: "Ішов сніг."},
    pl: {sonne: "Świeciło słońce.", warm: "Było ciepło.", regen: "Padał deszcz.", kalt: "Było zimno.", schnee: "Padał śnieg."},
    tr: {sonne: "Hava güneşliydi.", warm: "Hava sıcaktı.", regen: "Yağmur yağdı.", kalt: "Hava soğuktu.", schnee: "Kar yağdı."},
    fa: {sonne: "هوا آفتابی بود.", warm: "هوا گرم بود.", regen: "باران آمد.", kalt: "هوا سرد بود.", schnee: "برف آمد."},
    ar: {sonne: "كان الجو مشمسًا.", warm: "كان الجو دافئًا.", regen: "أمطرت.", kalt: "كان الجو باردًا.", schnee: "تساقط الثلج."}
  };
  const OBJET = {
    ru: {pass: "паспорт", badeanzug: "купальник", hut: "шляпа", sandalen: "сандалии", kamera: "фотоаппарат", sonnenbrille: "солнцезащитные очки",
         sonnencreme: "солнцезащитный крем", regenschirm: "зонт", pullover: "свитер", ladegeraet: "зарядное устройство", stadtplan: "план города"},
    uk: {pass: "паспорт", badeanzug: "купальник", hut: "капелюх", sandalen: "сандалі", kamera: "фотоапарат", sonnenbrille: "сонцезахисні окуляри",
         sonnencreme: "сонцезахисний крем", regenschirm: "парасолька", pullover: "светр", ladegeraet: "зарядний пристрій", stadtplan: "план міста"},
    pl: {pass: "paszport", badeanzug: "strój kąpielowy", hut: "kapelusz", sandalen: "sandały", kamera: "aparat fotograficzny", sonnenbrille: "okulary przeciwsłoneczne",
         sonnencreme: "krem z filtrem", regenschirm: "parasol", pullover: "sweter", ladegeraet: "ładowarka", stadtplan: "plan miasta"},
    tr: {pass: "pasaport", badeanzug: "mayo", hut: "şapka", sandalen: "sandaletler", kamera: "fotoğraf makinesi", sonnenbrille: "güneş gözlüğü",
         sonnencreme: "güneş kremi", regenschirm: "şemsiye", pullover: "kazak", ladegeraet: "şarj aleti", stadtplan: "şehir haritası"},
    fa: {pass: "گذرنامه", badeanzug: "مایو", hut: "کلاه", sandalen: "صندل‌ها", kamera: "دوربین عکاسی", sonnenbrille: "عینک آفتابی",
         sonnencreme: "کرم ضدآفتاب", regenschirm: "چتر", pullover: "پلیور", ladegeraet: "شارژر", stadtplan: "نقشهٔ شهر"},
    ar: {pass: "جواز السفر", badeanzug: "ملابس السباحة", hut: "القبعة", sandalen: "الصنادل", kamera: "الكاميرا", sonnenbrille: "النظارات الشمسية",
         sonnencreme: "كريم الوقاية من الشمس", regenschirm: "المظلة", pullover: "الكنزة", ladegeraet: "الشاحن", stadtplan: "خريطة المدينة"}
  };
  // ---------- la chambre et les nuits ----------
  const NB = {ru: ["", "одну", "две", "три", "четыре", "пять", "шесть", "семь", "восемь"], uk: ["", "одну", "дві", "три", "чотири", "пʼять", "шість", "сім", "вісім"],
              pl: ["", "jedną", "dwie", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem"], tr: ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz"],
              fa: ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت"], ar: ["", "", "", "ثلاث", "أربع", "خمس", "ست", "سبع", "ثماني"]};
  const NUITS = {   // « pour deux nuits » (complément) et « Deux nuits. » (seul)
    ru: x => [NB.ru[x] + " " + (x === 1 ? "ночь" : x < 5 ? "ночи" : "ночей"), (x === 1 ? "Одна" : maj(NB.ru[x])) + " " + (x === 1 ? "ночь" : x < 5 ? "ночи" : "ночей")],
    uk: x => [NB.uk[x] + " " + (x === 1 ? "ніч" : x < 5 ? "ночі" : "ночей"), (x === 1 ? "Одна" : maj(NB.uk[x])) + " " + (x === 1 ? "ніч" : x < 5 ? "ночі" : "ночей")],
    pl: x => [NB.pl[x] + " " + (x === 1 ? "noc" : x < 5 ? "noce" : "nocy"), (x === 1 ? "Jedna" : maj(NB.pl[x])) + " " + (x === 1 ? "noc" : x < 5 ? "noce" : "nocy")],
    tr: x => [NB.tr[x] + " gece", maj(NB.tr[x]) + " gece"],
    fa: x => [NB.fa[x] + " شب", NB.fa[x] + " شب"],
    ar: x => [x === 1 ? "لليلة واحدة" : x === 2 ? "لليلتين" : "ل" + NB.ar[x] + " ليالٍ", x === 1 ? "ليلة واحدة" : x === 2 ? "ليلتان" : NB.ar[x] + " ليالٍ"]
  };
  const CHAMBRE = {ru: ["одноместный номер", "двухместный номер"], uk: ["одномісний номер", "двомісний номер"], pl: ["pokój jednoosobowy", "pokój dwuosobowy"],
                   tr: ["tek kişilik bir oda", "çift kişilik bir oda"], fa: ["یک اتاق یک‌تخته", "یک اتاق دوتخته"], ar: ["غرفة مفردة", "غرفة مزدوجة"]};
  const ch = (lg, c) => CHAMBRE[lg][c === "doppel" ? 1 : 0];
  const RESERVE = {
    ru: (c, x) => maj(ch("ru", c)) + " на " + NUITS.ru(x)[0] + ".", uk: (c, x) => maj(ch("uk", c)) + " на " + NUITS.uk(x)[0] + ".",
    pl: (c, x) => maj(ch("pl", c)) + " na " + NUITS.pl(x)[0] + ".", tr: (c, x) => maj(NUITS.tr(x)[0]) + " için " + ch("tr", c) + ".",
    fa: (c, x) => ch("fa", c) + " برای " + NUITS.fa(x)[0] + ".", ar: (c, x) => ch("ar", c) + " " + NUITS.ar(x)[0] + "."
  };
  const ACCUEIL = {
    ru: (c, x) => "Здравствуйте, я забронировал(а) " + ch("ru", c) + " на " + NUITS.ru(x)[0] + ".",
    uk: (c, x) => "Добрий день, я забронював / забронювала " + ch("uk", c) + " на " + NUITS.uk(x)[0] + ".",
    pl: (c, x) => "Dzień dobry, zarezerwowałem / zarezerwowałam " + ch("pl", c) + " na " + NUITS.pl(x)[0] + ".",
    tr: (c, x) => "Merhaba, " + NUITS.tr(x)[0] + " için " + ch("tr", c) + " ayırttım.",
    fa: (c, x) => "سلام، " + ch("fa", c) + " برای " + NUITS.fa(x)[0] + " رزرو کرده‌ام.",
    ar: (c, x) => "مرحبًا، حجزت " + ch("ar", c) + " " + NUITS.ar(x)[0] + "."
  };
  const PETITDEJ = {
    ru: ["Нет, завтрак не включён.", "Да, завтрак включён."], uk: ["Ні, сніданок не включено.", "Так, сніданок включено."],
    pl: ["Nie, śniadanie nie jest wliczone.", "Tak, śniadanie jest wliczone."], tr: ["Hayır, kahvaltı dahil değil.", "Evet, kahvaltı dahil."],
    fa: ["نه، صبحانه شامل نیست.", "بله، صبحانه شامل است."], ar: ["لا، الفطور غير مشمول.", "نعم، الفطور مشمول."]
  };

  // ---------- une étape à une personne (k = 0 je, 1 tu, 3 nous ; sinon le sujet s de l'étape) ----------
  const deux = (m, f) => f === m + "а" ? m + "(а)" : m + " / " + f;
  const PRON = {ru: ["Я", "Ты", "", "Мы"], uk: ["Я", "Ти", "", "Ми"]};
  function etape(lg, e, k, s, sansSujet){
    const x = ET[lg][e.cle];
    if (lg === "ru" || lg === "uk"){
      if (!s) return PRON[lg][k] + " " + (k === 3 ? x[2] : deux(x[0], x[1])) + " " + x[3] + ".";
      const [n, g, p] = SUJ[lg][s], v = g === "pl" ? x[2] : g === "f" ? x[1] : x[0];
      return (sansSujet ? p : n) + " " + v + " " + x[3] + ".";
    }
    if (lg === "pl"){
      if (!s){ const v = k === 0 ? x[0] + "em / " + x[1] + "m" : k === 1 ? x[0] + "eś / " + x[1] + "ś" : x[2] + "śmy"; return maj(v) + " " + x[3] + "."; }
      const [n, g] = SUJ.pl[s], v = g === "pl" ? x[2] : g === "f" ? x[1] : x[0];
      return sansSujet ? v + " " + x[3] + "." : n + " " + v + " " + x[3] + ".";
    }
    if (lg === "tr" || lg === "fa"){
      if (!s) return maj(x[k === 3 ? 2 : k]) + ".";
      // la page peut aussi dire une étape avec un autre sujet que le sien (le vrai ou faux) : la 3e personne au nombre du sujet
      const pl = s === "BenMia", f = troisieme(lg, x[3], pl);
      return sansSujet ? f + "." : SUJ[lg][s][0] + " " + f + ".";      // sans sujet : dans une suite, après « Sonra »
    }
    // l'arabe : le verbe devant le sujet s'accorde à son genre (au singulier devant Ben et Mia), le possessif aussi
    if (!s) return x.p[k === 3 ? 2 : k] + ".";
    const g = SEXE_AR[s], v = VERBE_AR[e.cle][g === "f" ? 1 : 0], c = typeof x.c === "string" ? x.c : x.c[g];
    return sansSujet ? (s === "BenMia" ? x.d : v) + " " + c + "." : v + " " + SUJ.ar[s][0] + " " + c + ".";
  }
  // le turc et le persan : la 3e personne du singulier ou du pluriel, quelle que soit celle de l'étape
  function troisieme(lg, t, pl){
    if (lg === "tr"){
      const sing = t.replace(/l[ae]r$/, ""), voy = (sing.match(/[aeıioöuü]/g) || ["a"]).pop();
      return pl ? sing + ("aıou".includes(voy) ? "lar" : "ler") : sing;
    }
    const sing = t.replace(/ند$/, "");
    return pl ? sing.replace(/‌اش را/, "‌شان را").replace(/ش را/, "شان را") + "ند" : sing;
  }
  const SEXE_AR = {Anna: "f", Mark: "m", familia: "f", BenMia: "pl"};
  const VERBE_AR = {"anna-koffer": ["حزم", "حزمت"], "anna-flughafen": ["ذهب", "ذهبت"], "anna-flug": ["سافر", "سافرت"], "anna-meer": ["سبح", "سبحت"],
    "anna-eis": ["أكل", "أكلت"], "anna-altstadt": ["زار", "زارت"], "anna-souvenirs": ["اشترى", "اشترت"], "mark-rucksack": ["حزم", "حزمت"],
    "mark-zug": ["ذهب", "ذهبت"], "mark-hotel": ["وصل", "وصلت"], "mark-hafen": ["قام", "قامت"], "mark-fisch": ["أكل", "أكلت"], "mark-museum": ["ذهب", "ذهبت"],
    "mark-postkarte": ["كتب", "كتبت"], "familia-auto": ["ذهب", "ذهبت"], "familia-wohnung": ["استأجر", "استأجرت"], "familia-sandburg": ["بنى", "بنت"],
    "familia-baden": ["سبح", "سبحت"], "familia-rad": ["ركب", "ركبت"], "familia-karten": ["لعب", "لعبت"]};
  ET.ar["anna-koffer"].c = {f: "حقيبتها", m: "حقيبته", pl: "حقيبتيهما"};
  ET.ar["mark-rucksack"].c = {f: "حقيبة ظهرها", m: "حقيبة ظهره", pl: "حقيبتي ظهرهما"};
  const minuscule = (lg, s, t) => s === "familia" && ["ru", "uk", "pl", "tr"].includes(lg) ? t.charAt(0).toLowerCase() + t.slice(1) : t;

  const R = {};
  for (const lg of LANGUES){
    R[lg] = {
      etape: (e, k, s) => etape(lg, e, k, s),
      suite: etapes => etapes.map((e, i) => {
        const meme = i && etapes[i - 1].sujet === e.sujet && e.sujet !== "familia";
        const t = etape(lg, e, null, e.sujet, meme);
        return LIENS[lg][i] + " " + (lg === "ar" || meme ? t : minuscule(lg, e.sujet, t));
      }).join(" "),
      quand: e => QUAND[lg][e.voyage] + " " + minuscule(lg, e.sujet, etape(lg, e, null, e.sujet)),
      nuits: x => NUITS[lg](x)[1] + ".",
      reserve: (c, x) => RESERVE[lg](c, x),
      accueil: (c, x) => ACCUEIL[lg](c, x),
      petitdej: oui => PETITDEJ[lg][oui ? 1 : 0]
    };
  }

  // ---------- le branchement dans la donnée (la météo et les objets se traduisent par leur champ de langue) ----------
  const manque = [];
  for (const lg of LANGUES){
    for (const e of D.etapes) if (!ET[lg][e.cle]) manque.push("etape " + e.cle + " " + lg);
    for (const f in D.meteo){ if (METEO[lg][f]) D.meteo[f][lg] = METEO[lg][f]; else manque.push("meteo " + f + " " + lg); }
    for (const o in D.objets){ if (OBJET[lg][o]) D.objets[o][lg] = OBJET[lg][o]; else manque.push("objet " + o + " " + lg); }
    for (const v in D.voyages) if (!QUAND[lg][v]) manque.push("voyage " + v + " " + lg);
  }
  if (manque.length) console.error("vacances/langues.js : morceaux absents", manque);
  return R;
}
