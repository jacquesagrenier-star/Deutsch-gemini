// « Faire les courses » dans les langues d'interface sans phrase traduite jusqu'ici (lot 7 de l'alignement des
// thèmes, 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour
// qui apprend l'espagnol.
//
// LE CHEMIN NATIF : traduire() de la page assemble ses phrases (où acheter quoi, qui est où, le dialogue au comptoir,
// les prix, comparer, la monnaie rendue, commander, les emballages). On donne ici les morceaux dans chaque langue et la
// grammaire de chacune : le magasin aux trois cas (« в булочной / в булочную », « fırında / fırına / fırından »), le
// produit à l'accusatif (« купить колбасу », « kupić kiełbasę »), le verbe accordé au nombre (стоит / стоят), le
// comparatif invariable (дороже, أغلى), l'accord du verbe arabe avec Mark ou Anna.
// Les prix gardent leurs chiffres (« 4,20 € ») ; la voix ne dit que la langue apprise.
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesCourses(D, APPRENDRE){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
  const prix = c => Math.floor(c / 100) + "," + String(c % 100).padStart(2, "0") + " €";
  const NOM = {uk: {Mark: "Марк", Anna: "Анна"}, ru: {Mark: "Марк", Anna: "Анна"}, fa: {Mark: "مارک", Anna: "آنا"}, ar: {Mark: "مارك", Anna: "آنا"}};
  const nom = (lg, n) => (NOM[lg] || {})[n] || n;

  // ---------- les magasins : [le magasin, « au magasin », « vers le magasin »] (tr : + « du magasin », « nous y sommes ») ----------
  const MAG = {
    tr: {baeckerei: ["fırın", "fırında", "fırına", "fırından", "Fırındayız"], metzgerei: ["kasap", "kasapta", "kasaba", "kasaptan", "Kasaptayız"],
         supermarkt: ["süpermarket", "süpermarkette", "süpermarkete", "süpermarketten", "Süpermarketteyiz"], markt: ["pazar", "pazarda", "pazara", "pazardan", "Pazardayız"],
         apotheke: ["eczane", "eczanede", "eczaneye", "eczaneden", "Eczanedeyiz"], kiosk: ["büfe", "büfede", "büfeye", "büfeden", "Büfedeyiz"],
         drogerie: ["kozmetik mağazası", "kozmetik mağazasında", "kozmetik mağazasına", "kozmetik mağazasından", "Kozmetik mağazasındayız"],
         buchhandlung: ["kitapçı", "kitapçıda", "kitapçıya", "kitapçıdan", "Kitapçıdayız"]},
    uk: {baeckerei: ["пекарня", "у пекарні", "до пекарні"], metzgerei: ["мʼясна крамниця", "у мʼясній крамниці", "до мʼясної крамниці"],
         supermarkt: ["супермаркет", "у супермаркеті", "до супермаркету"], markt: ["ринок", "на ринку", "на ринок"], apotheke: ["аптека", "в аптеці", "до аптеки"],
         kiosk: ["кіоск", "у кіоску", "до кіоску"], drogerie: ["магазин побутової хімії", "у магазині побутової хімії", "до магазину побутової хімії"],
         buchhandlung: ["книгарня", "у книгарні", "до книгарні"]},
    pl: {baeckerei: ["piekarnia", "w piekarni", "do piekarni"], metzgerei: ["sklep mięsny", "w sklepie mięsnym", "do sklepu mięsnego"],
         supermarkt: ["supermarket", "w supermarkecie", "do supermarketu"], markt: ["targ", "na targu", "na targ"], apotheke: ["apteka", "w aptece", "do apteki"],
         kiosk: ["kiosk", "w kiosku", "do kiosku"], drogerie: ["drogeria", "w drogerii", "do drogerii"], buchhandlung: ["księgarnia", "w księgarni", "do księgarni"]},
    ru: {baeckerei: ["булочная", "в булочной", "в булочную"], metzgerei: ["мясная лавка", "в мясной лавке", "в мясную лавку"],
         supermarkt: ["супермаркет", "в супермаркете", "в супермаркет"], markt: ["рынок", "на рынке", "на рынок"], apotheke: ["аптека", "в аптеке", "в аптеку"],
         kiosk: ["киоск", "в киоске", "в киоск"], drogerie: ["магазин бытовой химии", "в магазине бытовой химии", "в магазин бытовой химии"],
         buchhandlung: ["книжный магазин", "в книжном магазине", "в книжный магазин"]},
    fa: {baeckerei: ["نانوایی"], metzgerei: ["قصابی"], supermarkt: ["سوپرمارکت"], markt: ["بازار"], apotheke: ["داروخانه"], kiosk: ["دکهٔ روزنامه‌فروشی"],
         drogerie: ["فروشگاه لوازم بهداشتی"], buchhandlung: ["کتاب‌فروشی"]},
    ar: {baeckerei: ["المخبز"], metzgerei: ["الملحمة"], supermarkt: ["السوبرماركت"], markt: ["السوق"], apotheke: ["الصيدلية"], kiosk: ["الكشك"],
         drogerie: ["متجر مواد التجميل والتنظيف"], buchhandlung: ["المكتبة"]}
  };
  for (const lg of ["fa", "ar"]) for (const k in MAG[lg]){ const n = MAG[lg][k][0]; MAG[lg][k] = lg === "fa" ? [n, "در " + n, "به " + n, "از " + n] : [n, "في " + n, "إلى " + n, "من " + n]; }

  // ---------- les produits : la forme d'objet (« acheter du pain ») ; ar [indéfini, défini] ----------
  const PROD = {
    tr: {brot: "ekmek", kuchen: "pasta", fleisch: "et", wurst: "salam", medikamente: "ilaç", tabletten: "hap", zeitung: "gazete", buch: "kitap",
         zahnpasta: "diş macunu", seife: "sabun", obst: "meyve", gemuese: "sebze"},
    uk: {brot: "хліб", kuchen: "торт", fleisch: "мʼясо", wurst: "ковбасу", medikamente: "ліки", tabletten: "таблетки", zeitung: "газету", buch: "книжку",
         zahnpasta: "зубну пасту", seife: "мило", obst: "фрукти", gemuese: "овочі"},
    pl: {brot: "chleb", kuchen: "ciasto", fleisch: "mięso", wurst: "kiełbasę", medikamente: "leki", tabletten: "tabletki", zeitung: "gazetę", buch: "książkę",
         zahnpasta: "pastę do zębów", seife: "mydło", obst: "owoce", gemuese: "warzywa"},
    ru: {brot: "хлеб", kuchen: "торт", fleisch: "мясо", wurst: "колбасу", medikamente: "лекарства", tabletten: "таблетки", zeitung: "газету", buch: "книгу",
         zahnpasta: "зубную пасту", seife: "мыло", obst: "фрукты", gemuese: "овощи"},
    fa: {brot: "نان", kuchen: "کیک", fleisch: "گوشت", wurst: "کالباس", medikamente: "دارو", tabletten: "قرص", zeitung: "روزنامه", buch: "کتاب",
         zahnpasta: "خمیردندان", seife: "صابون", obst: "میوه", gemuese: "سبزی"},
    ar: {brot: ["خبزًا", "الخبز"], kuchen: ["كعكة", "الكعك"], fleisch: ["لحمًا", "اللحم"], wurst: ["نقانق", "النقانق"], medikamente: ["أدوية", "الأدوية"],
         tabletten: ["أقراصًا", "الأقراص"], zeitung: ["جريدة", "الجريدة"], buch: ["كتابًا", "الكتب"], zahnpasta: ["معجون أسنان", "معجون الأسنان"],
         seife: ["صابونًا", "الصابون"], obst: ["فواكه", "الفواكه"], gemuese: ["خضارًا", "الخضار"]}
  };
  const prod = (lg, p) => { const x = PROD[lg][p.id]; return Array.isArray(x) ? x[0] : x; };
  const prodDef = (lg, p) => { const x = PROD[lg][p.id]; return Array.isArray(x) ? x[1] : x; };

  // ---------- les articles : [nom, pluriel ?] ; tr : [nom, ablatif] ----------
  const ART = {
    tr: {butter: ["tereyağı", "tereyağından"], kaese: ["peynir", "peynirden"], brot: ["ekmek", "ekmekten"], milch: ["süt", "sütten"], kaffee: ["kahve", "kahveden"],
         aepfel: ["elmalar", "elmalardan"], tomaten: ["domatesler", "domateslerden"], eier: ["yumurtalar", "yumurtalardan"], kuchen: ["pasta", "pastadan"],
         zeitung: ["gazete", "gazeteden"], buch: ["kitap", "kitaptan"], schokolade: ["çikolata", "çikolatadan"], reis: ["pirinç", "pirinçten"], erdbeeren: ["çilekler", "çileklerden"]},
    uk: {butter: "масло", kaese: "сир", brot: "хліб", milch: "молоко", kaffee: "кава", aepfel: "яблука", tomaten: "помідори", eier: "яйця", kuchen: "торт",
         zeitung: "газета", buch: "книжка", schokolade: "шоколад", reis: "рис", erdbeeren: "полуниці"},
    pl: {butter: "masło", kaese: "ser", brot: "chleb", milch: "mleko", kaffee: "kawa", aepfel: "jabłka", tomaten: "pomidory", eier: "jajka", kuchen: "ciasto",
         zeitung: "gazeta", buch: "książka", schokolade: "czekolada", reis: "ryż", erdbeeren: "truskawki"},
    ru: {butter: "масло", kaese: "сыр", brot: "хлеб", milch: "молоко", kaffee: "кофе", aepfel: "яблоки", tomaten: "помидоры", eier: "яйца", kuchen: "торт",
         zeitung: "газета", buch: "книга", schokolade: "шоколад", reis: "рис", erdbeeren: "клубника"},
    fa: {butter: "کره", kaese: "پنیر", brot: "نان", milch: "شیر", kaffee: "قهوه", aepfel: "سیب‌ها", tomaten: "گوجه‌فرنگی‌ها", eier: "تخم‌مرغ‌ها", kuchen: "کیک",
         zeitung: "روزنامه", buch: "کتاب", schokolade: "شکلات", reis: "برنج", erdbeeren: "توت‌فرنگی‌ها"},
    ar: {butter: "الزبدة", kaese: "الجبن", brot: "الخبز", milch: "الحليب", kaffee: "القهوة", aepfel: "التفاح", tomaten: "الطماطم", eier: "البيض", kuchen: "الكعكة",
         zeitung: "الجريدة", buch: "الكتاب", schokolade: "الشوكولاتة", reis: "الأرز", erdbeeren: "الفراولة"}
  };
  // le russe « клубника » est un singulier collectif : стоит ; les pluriels réels suivent l'allemand (die Äpfel)
  const PL_SAUF = {ru: ["erdbeeren"]};
  const art = (lg, a) => { const x = ART[lg][a.id]; return Array.isArray(x) ? x[0] : x; };
  const pluriel = (lg, a) => !!(a.de && a.de[1]) && !(PL_SAUF[lg] || []).includes(a.id);

  // ---------- les emballages et la commande : [nominatif, accusatif] (uk, pl, ru) ----------
  const EMB = {
    tr: {nudeln: "bir paket makarna", marmelade: "bir kavanoz reçel", zahnpasta: "bir tüp diş macunu", chips: "bir paket cips", wasser: "bir şişe su",
         tomatendose: "bir kutu domates", milch: "bir litre süt"},
    uk: {nudeln: ["пачка макаронів", "пачку макаронів"], marmelade: ["банка джему", "банку джему"], zahnpasta: ["тюбик зубної пасти", "тюбик зубної пасти"],
         chips: ["пачка чипсів", "пачку чипсів"], wasser: ["пляшка води", "пляшку води"], tomatendose: ["банка томатів", "банку томатів"], milch: ["літр молока", "літр молока"]},
    pl: {nudeln: ["paczka makaronu", "paczkę makaronu"], marmelade: ["słoik dżemu", "słoik dżemu"], zahnpasta: ["tubka pasty do zębów", "tubkę pasty do zębów"],
         chips: ["paczka chipsów", "paczkę chipsów"], wasser: ["butelka wody", "butelkę wody"], tomatendose: ["puszka pomidorów", "puszkę pomidorów"], milch: ["litr mleka", "litr mleka"]},
    ru: {nudeln: ["пачка макарон", "пачку макарон"], marmelade: ["банка варенья", "банку варенья"], zahnpasta: ["тюбик зубной пасты", "тюбик зубной пасты"],
         chips: ["пачка чипсов", "пачку чипсов"], wasser: ["бутылка воды", "бутылку воды"], tomatendose: ["банка помидоров", "банку помидоров"], milch: ["литр молока", "литр молока"]},
    fa: {nudeln: "یک بسته ماکارونی", marmelade: "یک شیشه مربا", zahnpasta: "یک تیوب خمیردندان", chips: "یک بسته چیپس", wasser: "یک بطری آب",
         tomatendose: "یک قوطی گوجه‌فرنگی", milch: "یک لیتر شیر"},
    ar: {nudeln: "علبة معكرونة", marmelade: "برطمان مربى", zahnpasta: "أنبوب معجون أسنان", chips: "كيس رقائق بطاطس", wasser: "زجاجة ماء",
         tomatendose: "علبة طماطم", milch: "لتر حليب"}
  };
  const COMMANDE = {
    tr: {brot: "bir ekmek", kuchen: "bir pasta", zeitung: "bir gazete", buch: "bir kitap", brezel: "bir pretzel", kaffee: "bir kahve", tuete: "bir poşet",
         wasser: "bir şişe su", nudeln: "bir paket makarna", marmelade: "bir kavanoz reçel", tomatendose: "bir kutu domates", zahnpasta: "bir tüp diş macunu",
         kiloaepfel: "bir kilo elma", stueckkaese: "bir parça peynir", apfel: "bir elma", schoko: "bir sıcak çikolata"},
    uk: {brot: "хліб", kuchen: "торт", zeitung: "газету", buch: "книжку", brezel: "брецель", kaffee: "каву", tuete: "пакет", wasser: "пляшку води",
         nudeln: "пачку макаронів", marmelade: "банку джему", tomatendose: "банку томатів", zahnpasta: "тюбик зубної пасти", kiloaepfel: "кілограм яблук",
         stueckkaese: "шматок сиру", apfel: "яблуко", schoko: "гарячий шоколад"},
    pl: {brot: "chleb", kuchen: "ciasto", zeitung: "gazetę", buch: "książkę", brezel: "precel", kaffee: "kawę", tuete: "torebkę", wasser: "butelkę wody",
         nudeln: "paczkę makaronu", marmelade: "słoik dżemu", tomatendose: "puszkę pomidorów", zahnpasta: "tubkę pasty do zębów", kiloaepfel: "kilogram jabłek",
         stueckkaese: "kawałek sera", apfel: "jabłko", schoko: "gorącą czekoladę"},
    ru: {brot: "хлеб", kuchen: "торт", zeitung: "газету", buch: "книгу", brezel: "крендель", kaffee: "кофе", tuete: "пакет", wasser: "бутылку воды",
         nudeln: "пачку макарон", marmelade: "банку варенья", tomatendose: "банку помидоров", zahnpasta: "тюбик зубной пасты", kiloaepfel: "килограмм яблок",
         stueckkaese: "кусок сыра", apfel: "яблоко", schoko: "горячий шоколад"},
    fa: {brot: "یک نان", kuchen: "یک کیک", zeitung: "یک روزنامه", buch: "یک کتاب", brezel: "یک پرتزل", kaffee: "یک قهوه", tuete: "یک کیسه",
         wasser: "یک بطری آب", nudeln: "یک بسته ماکارونی", marmelade: "یک شیشه مربا", tomatendose: "یک قوطی گوجه‌فرنگی", zahnpasta: "یک تیوب خمیردندان",
         kiloaepfel: "یک کیلو سیب", stueckkaese: "یک تکه پنیر", apfel: "یک سیب", schoko: "یک شکلات داغ"},
    ar: {brot: "رغيف خبز", kuchen: "كعكة", zeitung: "جريدة", buch: "كتابًا", brezel: "بريتزل", kaffee: "قهوة", tuete: "كيسًا", wasser: "زجاجة ماء",
         nudeln: "علبة معكرونة", marmelade: "برطمان مربى", tomatendose: "علبة طماطم", zahnpasta: "أنبوب معجون أسنان", kiloaepfel: "كيلو تفاح",
         stueckkaese: "قطعة جبن", apfel: "تفاحة", schoko: "شوكولاتة ساخنة"}
  };
  const nomin = x => Array.isArray(x) ? x[0] : x, accus = x => Array.isArray(x) ? x[1] : x;

  // ---------- les rôles (client, vendeur) et les répliques ----------
  const ROLE = {
    tr: {K: {m: "müşteri", f: "müşteri"}, V: {m: "satıcı", f: "satıcı"}},
    uk: {K: {m: "покупець", f: "покупчиня"}, V: {m: "продавець", f: "продавчиня"}},
    pl: {K: {m: "klient", f: "klientka"}, V: {m: "sprzedawca", f: "sprzedawczyni"}},
    ru: {K: {m: "покупатель", f: "покупательница"}, V: {m: "продавец", f: "продавщица"}},
    fa: {K: {m: "مشتری", f: "مشتری"}, V: {m: "فروشنده", f: "فروشنده"}},
    ar: {K: {m: "الزبون", f: "الزبونة"}, V: {m: "البائع", f: "البائعة"}}
  };
  const LIGNES = {
    de: {
      tr: {V1: "İyi günler! Ne arzu edersiniz?", K1: "Altı tane küçük ekmek istiyorum, lütfen.", V2: "Başka bir şey?", K2: "Hayır, teşekkürler. Bu kadar.",
           V3: "Poşet ister misiniz?", K3: "Hayır, teşekkürler. Çantam var.", V4: "Nakit mi ödüyorsunuz, kartla mı?", K4: "Kartla, lütfen.",
           V5: "Toplam 4,20 €.", K5: "Buyurun, beş euro.", K6: "Elmalar ne kadar?", V7: "Kilosu 2,90 €.", K8: "Kartla ödeyebilir miyim?", V8: "Evet, tabii.",
           K9: "Pirinci nerede bulabilirim?", V9: "Arkadaki rafta, makarnaların yanında.", V10: "Buyurun, fişiniz.", K10: "Çok teşekkürler. Hoşça kalın!",
           V11: "220 gram oldu. Biraz fazla olabilir mi?", K11: "Evet, olur.", K12: "Peynir indirimde mi?", V12: "Evet, bu hafta sadece 1,99 €.",
           K13: "Bu bana çok pahalı.", V13: "Bugün çilekler ucuz.", K14: "Tam buğday ekmeğiniz var mı?", V14: "Hayır, maalesef hiç kalmadı.", V15: "Sıradaki, lütfen!"},
      uk: {V1: "Добрий день! Що бажаєте?", K1: "Мені, будь ласка, шість булочок.", V2: "Щось іще?", K2: "Ні, дякую. Це все.",
           V3: "Вам потрібен пакет?", K3: "Ні, дякую. У мене є сумка.", V4: "Платите готівкою чи карткою?", K4: "Карткою, будь ласка.",
           V5: "З вас 4,20 €.", K5: "Ось пʼять євро.", K6: "Скільки коштують яблука?", V7: "Кілограм коштує 2,90 €.", K8: "Можна заплатити карткою?",
           V8: "Так, звичайно.", K9: "Де знайти рис?", V9: "На полиці в глибині, біля макаронів.", V10: "Ось ваш чек.", K10: "Щиро дякую. До побачення!",
           V11: "Тут 220 грамів. Можна трохи більше?", K11: "Так, усе гаразд.", K12: "Сир зі знижкою?", V12: "Так, цього тижня він коштує лише 1,99 €.",
           K13: "Для мене це задорого.", V13: "Сьогодні полуниці дешеві.", K14: "У вас є цільнозерновий хліб?", V14: "Ні, на жаль, уже немає.", V15: "Наступний, будь ласка!"},
      pl: {V1: "Dzień dobry! Co podać?", K1: "Poproszę sześć bułek.", V2: "Coś jeszcze?", K2: "Nie, dziękuję. To wszystko.",
           V3: "Potrzebuje pan torebki?", K3: "Nie, dziękuję. Mam torbę.", V4: "Płaci pan gotówką czy kartą?", K4: "Kartą, poproszę.",
           V5: "Razem 4,20 €.", K5: "Proszę, pięć euro.", K6: "Ile kosztują jabłka?", V7: "Kilogram kosztuje 2,90 €.", K8: "Czy mogę zapłacić kartą?",
           V8: "Tak, oczywiście.", K9: "Gdzie znajdę ryż?", V9: "Na półce z tyłu, obok makaronu.", V10: "Proszę, oto paragon.", K10: "Dziękuję bardzo. Do widzenia!",
           V11: "Jest 220 gramów. Może być trochę więcej?", K11: "Tak, w porządku.", K12: "Czy ser jest w promocji?", V12: "Tak, w tym tygodniu kosztuje tylko 1,99 €.",
           K13: "To dla mnie za drogo.", V13: "Dziś truskawki są tanie.", K14: "Czy jest chleb pełnoziarnisty?", V14: "Niestety już nie ma.", V15: "Następna osoba, proszę!"},
      ru: {V1: "Здравствуйте! Что вам угодно?", K1: "Дайте, пожалуйста, шесть булочек.", V2: "Что-нибудь ещё?", K2: "Нет, спасибо. Это всё.",
           V3: "Вам нужен пакет?", K3: "Нет, спасибо. У меня есть сумка.", V4: "Вы платите наличными или картой?", K4: "Картой, пожалуйста.",
           V5: "С вас 4,20 €.", K5: "Вот пять евро.", K6: "Сколько стоят яблоки?", V7: "Килограмм стоит 2,90 €.", K8: "Можно заплатить картой?",
           V8: "Да, конечно.", K9: "Где найти рис?", V9: "На полке в глубине, рядом с макаронами.", V10: "Вот ваш чек.", K10: "Большое спасибо. До свидания!",
           V11: "Здесь 220 граммов. Можно чуть больше?", K11: "Да, хорошо.", K12: "Сыр по акции?", V12: "Да, на этой неделе он стоит всего 1,99 €.",
           K13: "Для меня это слишком дорого.", V13: "Сегодня клубника дешёвая.", K14: "У вас есть цельнозерновой хлеб?", V14: "Нет, к сожалению, уже нет.", V15: "Следующий, пожалуйста!"},
      fa: {V1: "روز بخیر! چه میل دارید؟", K1: "شش تا نان کوچک می‌خواهم، لطفاً.", V2: "چیز دیگری هم می‌خواهید؟", K2: "نه، ممنون. همین.",
           V3: "کیسه لازم دارید؟", K3: "نه، ممنون. کیف دارم.", V4: "نقد پرداخت می‌کنید یا با کارت؟", K4: "با کارت، لطفاً.",
           V5: "می‌شود 4,20 €.", K5: "بفرمایید، پنج یورو.", K6: "سیب‌ها چند است؟", V7: "کیلویی 2,90 €.", K8: "می‌توانم با کارت پرداخت کنم؟",
           V8: "بله، البته.", K9: "برنج را کجا پیدا کنم؟", V9: "در قفسهٔ ته مغازه، کنار ماکارونی.", V10: "بفرمایید، رسیدتان.", K10: "خیلی ممنون. خداحافظ!",
           V11: "220 گرم است. کمی بیشتر اشکالی ندارد؟", K11: "بله، اشکالی ندارد.", K12: "پنیر تخفیف دارد؟", V12: "بله، این هفته فقط 1,99 € است.",
           K13: "این برای من خیلی گران است.", V13: "امروز توت‌فرنگی ارزان است.", K14: "نان سبوس‌دار دارید؟", V14: "نه، متأسفانه دیگر نمانده.", V15: "نفر بعدی، لطفاً!"},
      ar: {V1: "مرحبًا! ماذا تريد؟", K1: "أريد ستة أرغفة صغيرة من فضلك.", V2: "هل تريد شيئًا آخر؟", K2: "لا، شكرًا. هذا كل شيء.",
           V3: "هل تحتاج إلى كيس؟", K3: "لا، شكرًا. معي حقيبة.", V4: "هل تدفع نقدًا أم بالبطاقة؟", K4: "بالبطاقة من فضلك.",
           V5: "المبلغ 4,20 €.", K5: "تفضّل، خمسة يورو.", K6: "كم سعر التفاح؟", V7: "الكيلو بـ 2,90 €.", K8: "هل يمكنني الدفع بالبطاقة؟",
           V8: "نعم، بالطبع.", K9: "أين أجد الأرز؟", V9: "على الرف في الخلف، بجانب المعكرونة.", V10: "تفضّل، هذا إيصالك.", K10: "شكرًا جزيلًا. مع السلامة!",
           V11: "الوزن 220 غرامًا. هل يمكن أن يكون أكثر قليلًا؟", K11: "نعم، لا بأس.", K12: "هل الجبن عليه تخفيض؟", V12: "نعم، هذا الأسبوع سعره 1,99 € فقط.",
           K13: "هذا غالٍ جدًا بالنسبة لي.", V13: "الفراولة رخيصة اليوم.", K14: "هل عندكم خبز أسمر؟", V14: "لا، للأسف لم يبقَ منه شيء.", V15: "التالي من فضلك!"}
    },
    es: {
      ar: {V1: "صباح الخير. ماذا تريد؟", K1: "أريد ستة أرغفة صغيرة من فضلك.", V2: "هل تريد شيئًا آخر؟", K2: "لا، شكرًا. هذا كل شيء.",
           V3: "هل تريد كيسًا؟", K3: "لا، شكرًا. معي واحد.", V4: "هل تدفع نقدًا أم بالبطاقة؟", K4: "بالبطاقة من فضلك.",
           V5: "المبلغ 4,20 €.", K5: "تفضّل، خمسة يورو.", K6: "كم سعر التفاح؟", V7: "الكيلو بـ 2,90 €.", K8: "هل يمكنني الدفع بالبطاقة؟",
           V8: "نعم، طبعًا.", K9: "أين الأرز؟", V9: "هناك في الخلف، بجانب المعكرونة.", V10: "تفضّل، هذا إيصالك.", K10: "شكرًا. مع السلامة!",
           V11: "الوزن 220 غرامًا. هل هذا مناسب؟", K11: "نعم، جيد.", K12: "هل الجبن عليه تخفيض؟", V12: "نعم، هذا الأسبوع سعره 1,99 € فقط.",
           K13: "هذا غالٍ جدًا بالنسبة لي.", V13: "الفراولة رخيصة اليوم.", K14: "هل عندكم خبز أسمر؟", V14: "لا، آسفة، لم يبقَ منه شيء.", V15: "التالي من فضلك!"}
    }
  };
  // ---------- ce que font Mark et Anna (moments) ----------
  const FAIT = {
    tr: {"baeckerei-bestellen": "Mark küçük ekmek sipariş ediyor.", "baeckerei-tuete": "Satıcı Mark'a bir poşet veriyor.", "baeckerei-bar": "Mark nakit ödüyor.",
         "metzgerei-wiegen": "Satıcı jambonu tartıyor.", "markt-fragen": "Anna elmaların fiyatını soruyor.", "kasse-karte": "Mark kartla ödüyor.",
         "kasse-bon": "Mark fişi alıyor.", "regal-suchen": "Mark pirinci arıyor."},
    uk: {"baeckerei-bestellen": "Марк замовляє булочки.", "baeckerei-tuete": "Продавчиня дає Маркові пакет.", "baeckerei-bar": "Марк платить готівкою.",
         "metzgerei-wiegen": "Продавець зважує шинку.", "markt-fragen": "Анна питає ціну яблук.", "kasse-karte": "Марк платить карткою.",
         "kasse-bon": "Марк отримує чек.", "regal-suchen": "Марк шукає рис."},
    pl: {"baeckerei-bestellen": "Mark zamawia bułki.", "baeckerei-tuete": "Sprzedawczyni daje Markowi torebkę.", "baeckerei-bar": "Mark płaci gotówką.",
         "metzgerei-wiegen": "Sprzedawca waży szynkę.", "markt-fragen": "Anna pyta o cenę jabłek.", "kasse-karte": "Mark płaci kartą.",
         "kasse-bon": "Mark dostaje paragon.", "regal-suchen": "Mark szuka ryżu."},
    ru: {"baeckerei-bestellen": "Марк заказывает булочки.", "baeckerei-tuete": "Продавщица даёт Марку пакет.", "baeckerei-bar": "Марк платит наличными.",
         "metzgerei-wiegen": "Продавец взвешивает ветчину.", "markt-fragen": "Анна спрашивает цену яблок.", "kasse-karte": "Марк платит картой.",
         "kasse-bon": "Марк получает чек.", "regal-suchen": "Марк ищет рис."},
    fa: {"baeckerei-bestellen": "مارک نان کوچک سفارش می‌دهد.", "baeckerei-tuete": "فروشنده یک کیسه به مارک می‌دهد.", "baeckerei-bar": "مارک نقد پرداخت می‌کند.",
         "metzgerei-wiegen": "فروشنده ژامبون را وزن می‌کند.", "markt-fragen": "آنا قیمت سیب‌ها را می‌پرسد.", "kasse-karte": "مارک با کارت پرداخت می‌کند.",
         "kasse-bon": "مارک رسید را می‌گیرد.", "regal-suchen": "مارک دنبال برنج می‌گردد."},
    ar: {"baeckerei-bestellen": "يطلب مارك أرغفة صغيرة.", "baeckerei-tuete": "تعطي البائعة مارك كيسًا.", "baeckerei-bar": "يدفع مارك نقدًا.",
         "metzgerei-wiegen": "يزن البائع لحم الخنزير المقدد.", "markt-fragen": "تسأل آنا عن سعر التفاح.", "kasse-karte": "يدفع مارك بالبطاقة.",
         "kasse-bon": "يتسلّم مارك الإيصال.", "regal-suchen": "يبحث مارك عن الأرز."}
  };
  // l'espagnol nomme le jambon (« jamón ») là où l'allemand dit le jambon cuit : « لحم الخنزير » se lit mal en arabe
  if (APPRENDRE === "es") FAIT.ar["metzgerei-wiegen"] = "يزن البائع الجامون.";

  // ---------- les phrases, langue par langue ----------
  const P = (lg, pe) => nom(lg, pe.n);
  const B = {
    tr: {
      ou: (p, m) => maj(prod("tr", p)) + " nereden alınır? " + maj(MAG.tr[m.id][3]) + ".",
      sommes: m => MAG.tr[m.id][4] + ".",
      aller: (pe, p, m, zu) => zu ? pe.n + "'" + (pe.n === "Mark" ? "ın" : "nın") + " " + prod("tr", p) + " alması gerekiyor. " + maj(MAG.tr[m.id][2]) + " gidiyor."
        : pe.n + " " + prod("tr", p) + " alıyor. " + maj(MAG.tr[m.id][1]) + ".",
      estLa: (pe, m) => pe.n + " " + MAG.tr[m.id][1] + ".",
      dit: (role, t) => maj(role) + " şöyle diyor: «" + t + "»",
      coute: (a, c) => maj(art("tr", a)) + " " + prix(c) + ".",
      compare: (a, b, plus) => maj(art("tr", a)) + " " + ART.tr[b.id][1] + " daha " + (plus ? "pahalı." : "ucuz."),
      plusCher: plus => plus ? "daha pahalı" : "daha ucuz",
      rendu: (pe, t, b, r) => "Toplam " + prix(t) + ". " + pe.n + " " + b / 100 + " euroluk banknotla ödüyor. " + prix(r) + " para üstü alıyor.",
      kostet: a => maj(art("tr", a)) + " ne kadar?",
      commande: k => maj(COMMANDE.tr[k]) + " istiyorum.",
      emb: (e, c) => maj(EMB.tr[e.id]) + " " + prix(c) + ".",
      demande: e => maj(EMB.tr[e.id]) + ", lütfen.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "Süpermarkette hemen her şey alınır." : maj(MAG.tr[m.id][1]) + " " + ps.map(p => prod("tr", p)).join(" ve ") + " alınır."
    },
    uk: {
      ou: (p, m) => "Де купують " + prod("uk", p) + "? " + maj(MAG.uk[m.id][1]) + ".",
      sommes: m => "Ми " + MAG.uk[m.id][1] + ".",
      aller: (pe, p, m, zu) => zu ? (pe.s === "f" ? "Анні" : "Маркові") + " треба купити " + prod("uk", p) + ". " + (pe.s === "f" ? "Вона йде " : "Він іде ") + MAG.uk[m.id][2] + "."
        : P("uk", pe) + " купує " + prod("uk", p) + ". " + (pe.s === "f" ? "Вона " : "Він ") + MAG.uk[m.id][1] + ".",
      estLa: (pe, m) => P("uk", pe) + " " + MAG.uk[m.id][1] + ".",
      dit: (role, t) => maj(role) + " каже: «" + t + "»",
      coute: (a, c) => maj(art("uk", a)) + (pluriel("uk", a) ? " коштують " : " коштує ") + prix(c) + ".",
      compare: (a, b, plus) => maj(art("uk", a)) + (pluriel("uk", a) ? " коштують " : " коштує ") + (plus ? "більше" : "менше") + ", ніж " + art("uk", b) + ".",
      plusCher: plus => plus ? "дорожче" : "дешевше",
      rendu: (pe, t, b, r) => "З вас " + prix(t) + ". " + P("uk", pe) + " платить купюрою " + b / 100 + " євро. " + (pe.s === "f" ? "Їй" : "Йому") + " дають " + prix(r) + " решти.",
      kostet: a => "Скільки " + (pluriel("uk", a) ? "коштують " : "коштує ") + art("uk", a) + "?",
      commande: k => "Дайте, будь ласка, " + COMMANDE.uk[k] + ".",
      emb: (e, c) => maj(nomin(EMB.uk[e.id])) + " коштує " + prix(c) + ".",
      demande: e => maj(accus(EMB.uk[e.id])) + ", будь ласка.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "У супермаркеті можна купити майже все." : maj(MAG.uk[m.id][1]) + " купують " + ps.map(p => prod("uk", p)).join(" і ") + "."
    },
    pl: {
      ou: (p, m) => "Gdzie kupuje się " + prod("pl", p) + "? " + maj(MAG.pl[m.id][1]) + ".",
      sommes: m => "Jesteśmy " + MAG.pl[m.id][1] + ".",
      aller: (pe, p, m, zu) => zu ? pe.n + " musi kupić " + prod("pl", p) + ". Idzie " + MAG.pl[m.id][2] + "."
        : pe.n + " kupuje " + prod("pl", p) + ". Jest " + MAG.pl[m.id][1] + ".",
      estLa: (pe, m) => pe.n + " jest " + MAG.pl[m.id][1] + ".",
      dit: (role, t) => maj(role) + " mówi: „" + t + "”",
      coute: (a, c) => maj(art("pl", a)) + (pluriel("pl", a) ? " kosztują " : " kosztuje ") + prix(c) + ".",
      compare: (a, b, plus) => maj(art("pl", a)) + (pluriel("pl", a) ? " kosztują " : " kosztuje ") + (plus ? "więcej" : "mniej") + " niż " + art("pl", b) + ".",
      plusCher: plus => plus ? "droższy" : "tańszy",
      rendu: (pe, t, b, r) => "Razem " + prix(t) + ". " + pe.n + " płaci banknotem " + b / 100 + " euro. Dostaje " + prix(r) + " reszty.",
      kostet: a => "Ile " + (pluriel("pl", a) ? "kosztują " : "kosztuje ") + art("pl", a) + "?",
      commande: k => "Poproszę " + COMMANDE.pl[k] + ".",
      emb: (e, c) => maj(nomin(EMB.pl[e.id])) + " kosztuje " + prix(c) + ".",
      demande: e => maj(accus(EMB.pl[e.id])) + ", poproszę.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "W supermarkecie można kupić prawie wszystko." : maj(MAG.pl[m.id][1]) + " kupuje się " + ps.map(p => prod("pl", p)).join(" i ") + "."
    },
    ru: {
      ou: (p, m) => "Где покупают " + prod("ru", p) + "? " + maj(MAG.ru[m.id][1]) + ".",
      sommes: m => "Мы " + MAG.ru[m.id][1] + ".",
      aller: (pe, p, m, zu) => zu ? (pe.s === "f" ? "Анне" : "Марку") + " нужно купить " + prod("ru", p) + ". " + (pe.s === "f" ? "Она идёт " : "Он идёт ") + MAG.ru[m.id][2] + "."
        : P("ru", pe) + " покупает " + prod("ru", p) + ". " + (pe.s === "f" ? "Она " : "Он ") + MAG.ru[m.id][1] + ".",
      estLa: (pe, m) => P("ru", pe) + " " + MAG.ru[m.id][1] + ".",
      dit: (role, t) => maj(role) + " говорит: «" + t + "»",
      coute: (a, c) => maj(art("ru", a)) + (pluriel("ru", a) ? " стоят " : " стоит ") + prix(c) + ".",
      compare: (a, b, plus) => maj(art("ru", a)) + (plus ? " дороже, чем " : " дешевле, чем ") + art("ru", b) + ".",
      plusCher: plus => plus ? "дороже" : "дешевле",
      rendu: (pe, t, b, r) => "С вас " + prix(t) + ". " + P("ru", pe) + " платит купюрой в " + b / 100 + " евро. " + (pe.s === "f" ? "Ей" : "Ему") + " дают " + prix(r) + " сдачи.",
      kostet: a => "Сколько " + (pluriel("ru", a) ? "стоят " : "стоит ") + art("ru", a) + "?",
      commande: k => "Дайте, пожалуйста, " + COMMANDE.ru[k] + ".",
      emb: (e, c) => maj(nomin(EMB.ru[e.id])) + " стоит " + prix(c) + ".",
      demande: e => maj(accus(EMB.ru[e.id])) + ", пожалуйста.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "В супермаркете можно купить почти всё." : maj(MAG.ru[m.id][1]) + " покупают " + ps.map(p => prod("ru", p)).join(" и ") + "."
    },
    fa: {
      ou: (p, m) => prod("fa", p) + " را از کجا می‌خرند؟ " + MAG.fa[m.id][3] + ".",
      sommes: m => "ما " + MAG.fa[m.id][1] + " هستیم.",
      aller: (pe, p, m, zu) => zu ? P("fa", pe) + " باید " + prod("fa", p) + " بخرد. او " + MAG.fa[m.id][2] + " می‌رود."
        : P("fa", pe) + " " + prod("fa", p) + " می‌خرد. او " + MAG.fa[m.id][1] + " است.",
      estLa: (pe, m) => P("fa", pe) + " " + MAG.fa[m.id][1] + " است.",
      dit: (role, t) => role + " می‌گوید: «" + t + "»",
      coute: (a, c) => "قیمت " + art("fa", a) + " " + prix(c) + " است.",
      compare: (a, b, plus) => art("fa", a) + " از " + art("fa", b) + (plus ? " گران‌تر است." : " ارزان‌تر است."),
      plusCher: plus => plus ? "گران‌تر" : "ارزان‌تر",
      rendu: (pe, t, b, r) => "می‌شود " + prix(t) + ". " + P("fa", pe) + " با یک اسکناس " + b / 100 + " یورویی پرداخت می‌کند. " + prix(r) + " باقی پول می‌گیرد.",
      kostet: a => "قیمت " + art("fa", a) + " چند است؟",
      commande: k => COMMANDE.fa[k] + " می‌خواهم.",
      emb: (e, c) => EMB.fa[e.id] + " " + prix(c) + " است.",
      demande: e => EMB.fa[e.id] + "، لطفاً.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "در سوپرمارکت تقریباً همه چیز می‌خرند." : MAG.fa[m.id][1] + " " + ps.map(p => prod("fa", p)).join(" و ") + " می‌خرند."
    },
    ar: {
      ou: (p, m) => "من أين نشتري " + prodDef("ar", p) + "؟ " + MAG.ar[m.id][3] + ".",
      sommes: m => "نحن " + MAG.ar[m.id][1] + ".",
      aller: (pe, p, m, zu) => { const f = pe.s === "f";
        return zu ? "على " + P("ar", pe) + " أن " + (f ? "تشتري " : "يشتري ") + prod("ar", p) + ". " + (f ? "تذهب " : "يذهب ") + MAG.ar[m.id][2] + "."
          : (f ? "تشتري " : "يشتري ") + P("ar", pe) + " " + prod("ar", p) + ". " + (f ? "إنها " : "إنه ") + MAG.ar[m.id][1] + "."; },
      estLa: (pe, m) => P("ar", pe) + " " + MAG.ar[m.id][1] + ".",
      dit: (role, t, s) => (s === "f" ? "تقول " : "يقول ") + role + ": «" + t + "»",
      coute: (a, c) => "سعر " + art("ar", a) + " " + prix(c) + ".",
      compare: (a, b, plus) => art("ar", a) + (plus ? " أغلى من " : " أرخص من ") + art("ar", b) + ".",
      plusCher: plus => plus ? "أغلى" : "أرخص",
      rendu: (pe, t, b, r) => "المبلغ " + prix(t) + ". " + (pe.s === "f" ? "تدفع " : "يدفع ") + P("ar", pe) + " بورقة نقدية من فئة " + b / 100 + " يورو. "
        + (pe.s === "f" ? "تأخذ " : "يأخذ ") + prix(r) + " باقيًا.",
      kostet: a => "كم سعر " + art("ar", a) + "؟",
      commande: k => "أريد " + COMMANDE.ar[k] + ".",
      emb: (e, c) => "سعر " + EMB.ar[e.id] + " " + prix(c) + ".",
      demande: e => EMB.ar[e.id] + " من فضلك.",
      decouverte: (m, ps) => m.id === "supermarkt" ? "في السوبرماركت نشتري كل شيء تقريبًا." : MAG.ar[m.id][1] + " نشتري " + ps.map(p => prod("ar", p)).join(" و") + "."
    }
  };

  // ---------- traduire(q) : la même forme que la page ----------
  for (const lg in B){
    const b = B[lg];
    b.mag = (m, k) => MAG[lg][m.id][k];
    b.traduire = q => {
      if (q.ou) return b.ou(q.ou.p, q.ou.m);
      if (q.sommes) return b.sommes(q.sommes);
      if (q.aller) return b.aller(q.aller.pe, q.aller.p, q.aller.m, q.aller.zu);
      if (q.estLa) return b.estLa(q.estLa.pe, q.estLa.m);
      if (q.fait) return q.fait[lg] || null;
      if (q.qui){ const {id, r, s} = q.qui; return b.dit(ROLE[lg][r][s], LIGNES[APPRENDRE][lg][id], s); }
      if (q.paire) return LIGNES[APPRENDRE][lg][q.paire.q] + " — " + LIGNES[APPRENDRE][lg][q.paire.r];
      if (q.coute) return b.coute(q.coute.a, q.coute.c);
      if (q.compare) return b.compare(q.compare.a, q.compare.b, q.compare.plus);
      if (q.rendu) return b.rendu(q.rendu.pe, q.rendu.t, q.rendu.b, q.rendu.r);
      if (q.kostet) return b.kostet(q.kostet);
      if (q.commande) return b.commande(q.commande);
      if (q.emb) return b.emb(q.emb.e, q.emb.c);
      if (q.demande) return b.demande(q.demande);
      return null;
    };
  }

  // ---------- le branchement dans la donnée (les traductions des choix : rôle, réplique, emballage, magasin) ----------
  const manque = [];
  for (const lg of LANGUES){
    D.tradRoles[lg] = ROLE[lg];
    for (const id in D.lignes){ const t = LIGNES[APPRENDRE][lg][id]; if (!t) { manque.push("ligne " + id + " " + lg); continue; }
      const l = D.lignes[id]; (l.tr[APPRENDRE] = l.tr[APPRENDRE] || {})[lg] = t; }
    for (const id in D.tradEmb){ if (EMB[lg][id]) D.tradEmb[id][lg] = nomin(EMB[lg][id]); else manque.push("emballage " + id + " " + lg); }
    for (const id in D.tradCommande){ if (COMMANDE[lg][id]) D.tradCommande[id][lg] = COMMANDE[lg][id]; else manque.push("commande " + id + " " + lg); }
    for (const m of D.magasins){ if (!m[APPRENDRE] || !m[APPRENDRE].mot) continue; if (MAG[lg][m.id]) m.tr[lg] = MAG[lg][m.id].slice(0, 3); else manque.push("magasin " + m.id + " " + lg); }
    for (const p of D.produits){ if (PROD[lg][p.id]) p.tr[lg] = prod(lg, p); else manque.push("produit " + p.id + " " + lg); }
    for (const a of D.articles){ if (ART[lg][a.id]) a.tr[lg] = art(lg, a); else manque.push("article " + a.id + " " + lg); }
    for (const m of D.moments){ if (FAIT[lg][m.id]) m.fait[lg] = FAIT[lg][m.id]; else manque.push("moment " + m.id + " " + lg); }
  }
  if (manque.length) console.error("courses/langues.js : morceaux absents", manque);
  const R = {};
  for (const lg of LANGUES) R[lg] = B[lg];
  return R;
}
