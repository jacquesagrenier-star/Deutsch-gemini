// « Manger et goûter » dans les langues d'interface sans phrase traduite jusqu'ici (lot 10 de l'alignement des thèmes,
// 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour qui
// apprend l'espagnol.
//
// LE CHEMIN NATIF : traduire() de la page (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste
// de courses, le café, la commande et l'addition) a ici son équivalent dans chaque langue, avec ses morceaux (aliments,
// saveurs, contenants, contenus, produits, carte du café) et sa grammaire : l'accusatif de « любит торт », le génitif
// après la négation polonaise (« nie lubi cytryn ») et après une quantité (« килограмм апельсинов »), l'accusatif
// turc (« pastayı sever »), le « را » persan, le verbe arabe accordé à qui parle ou agit. Une livre allemande (Pfund)
// se dit « ½ kg » : 500 g, comme en Allemagne.
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesManger(D, APPRENDRE, nomDe){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
  const prix = c => Math.floor(c / 100) + "," + String(c % 100).padStart(2, "0") + " €";
  const sexe = p => D.sexe[p] || "m";
  const NOMS = {
    ru: {Anna: "Анна", Carmen: "Кармен", Gisela: "Гизела", Mark: "Марк", Diego: "Диего", Ben: "Бен", Mia: "Мия", Marta: "Марта", Javier: "Хавьер", Rosa: "Роза",
         Lucas: "Лукас", Tomas: "Томас", Elena: "Елена", Ines: "Инес", Pablo: "Пабло", Heinz: "Хайнц", Peter: "Петер", Felix: "Феликс"},
    uk: {Anna: "Анна", Carmen: "Кармен", Gisela: "Гізела", Mark: "Марк", Diego: "Дієго", Ben: "Бен", Mia: "Мія", Marta: "Марта", Javier: "Хавʼєр", Rosa: "Роза",
         Lucas: "Лукас", Tomas: "Томас", Elena: "Елена", Ines: "Інес", Pablo: "Пабло", Heinz: "Гайнц", Peter: "Петер", Felix: "Фелікс"},
    fa: {Anna: "آنا", Carmen: "کارمن", Gisela: "گیزلا", Mark: "مارک", Diego: "دیه‌گو", Ben: "بن", Mia: "میا", Marta: "مارتا", Javier: "خاویر", Rosa: "روزا",
         Lucas: "لوکاس", Tomas: "توماس", Elena: "النا", Ines: "اینس", Pablo: "پابلو", Heinz: "هاینتس", Peter: "پتر", Felix: "فلیکس"},
    ar: {Anna: "آنا", Carmen: "كارمن", Gisela: "غيزيلا", Mark: "مارك", Diego: "دييغو", Ben: "بن", Mia: "ميا", Marta: "مارتا", Javier: "خافيير", Rosa: "روزا",
         Lucas: "لوكاس", Tomas: "توماس", Elena: "إيلينا", Ines: "إينيس", Pablo: "بابلو", Heinz: "هاينتس", Peter: "بيتر", Felix: "فيليكس"}
  };
  const nom = (lg, p) => (NOMS[lg] || {})[p] || nomDe(p);
  const ET = {ru: " и ", uk: " і ", pl: " i ", tr: " ve ", fa: " و ", ar: " و"};
  const liste = (lg, t) => t.length < 2 ? t[0] : t.slice(0, -1).join(lg === "ar" ? " و" : ", ") + ET[lg] + t[t.length - 1];

  // ---------- les aliments : objet (accusatif / pl : + génitif après la négation) et la phrase de saveur ----------
  const AL = {
    ru: {tarta: ["торт", "Торт сладкий."], chocolate: ["шоколад", "Шоколад сладкий."], limon: ["лимоны", "Лимон кислый."], picante: ["острую еду", "Блюдо острое."],
         cafe: ["чёрный кофе", "Чёрный кофе горький."], sopa: ["суп", "Суп солёный."], pretzel: ["крендели", "Крендель солёный."], fresa: ["клубнику", "Клубника сладкая."],
         pescado: ["рыбу", ""], galleta: ["печенье", "Печенье сладкое."], pizza: ["пиццу", ""], queso: ["сыр", ""], tomate: ["помидоры", ""]},
    uk: {tarta: ["торт", "Торт солодкий."], chocolate: ["шоколад", "Шоколад солодкий."], limon: ["лимони", "Лимон кислий."], picante: ["гостру їжу", "Страва гостра."],
         cafe: ["чорну каву", "Чорна кава гірка."], sopa: ["суп", "Суп солоний."], pretzel: ["брецелі", "Брецель солоний."], fresa: ["полуницю", "Полуниця солодка."],
         pescado: ["рибу", ""], galleta: ["печиво", "Печиво солодке."], pizza: ["піцу", ""], queso: ["сир", ""], tomate: ["помідори", ""]},
    pl: {tarta: ["ciasto", "ciasta", "Ciasto jest słodkie."], chocolate: ["czekoladę", "czekolady", "Czekolada jest słodka."], limon: ["cytryny", "cytryn", "Cytryna jest kwaśna."],
         picante: ["ostre jedzenie", "ostrego jedzenia", "Danie jest ostre."], cafe: ["czarną kawę", "czarnej kawy", "Czarna kawa jest gorzka."],
         sopa: ["zupę", "zupy", "Zupa jest słona."], pretzel: ["precle", "precli", "Precel jest słony."], fresa: ["truskawki", "truskawek", "Truskawki są słodkie."],
         pescado: ["ryby", "ryb", ""], galleta: ["ciastka", "ciastek", "Ciastka są słodkie."], pizza: ["pizzę", "pizzy", ""], queso: ["ser", "sera", ""], tomate: ["pomidory", "pomidorów", ""]},
    tr: {tarta: ["pastayı", "Pasta tatlı."], chocolate: ["çikolatayı", "Çikolata tatlı."], limon: ["limonu", "Limon ekşi."], picante: ["acılı yemekleri", "Yemek acılı."],
         cafe: ["sade kahveyi", "Sade kahve acı."], sopa: ["çorbayı", "Çorba tuzlu."], pretzel: ["pretzelleri", "Pretzel tuzlu."], fresa: ["çilekleri", "Çilekler tatlı."],
         pescado: ["balığı", ""], galleta: ["bisküvileri", "Bisküviler tatlı."], pizza: ["pizzayı", ""], queso: ["peyniri", ""], tomate: ["domatesleri", ""]},
    fa: {tarta: ["کیک", "کیک شیرین است."], chocolate: ["شکلات", "شکلات شیرین است."], limon: ["لیمو", "لیمو ترش است."], picante: ["غذای تند", "غذا تند است."],
         cafe: ["قهوهٔ تلخ", "قهوهٔ سیاه تلخ است."], sopa: ["سوپ", "سوپ شور است."], pretzel: ["پرتزل", "پرتزل شور است."], fresa: ["توت‌فرنگی", "توت‌فرنگی‌ها شیرین‌اند."],
         pescado: ["ماهی", ""], galleta: ["بیسکویت", "بیسکویت‌ها شیرین‌اند."], pizza: ["پیتزا", ""], queso: ["پنیر", ""], tomate: ["گوجه‌فرنگی", ""]},
    ar: {tarta: ["الكعكة", "الكعكة حلوة."], chocolate: ["الشوكولاتة", "الشوكولاتة حلوة."], limon: ["الليمون", "الليمون حامض."], picante: ["الطعام الحار", "الطبق حار."],
         cafe: ["القهوة السوداء", "القهوة السوداء مرة."], sopa: ["الحساء", "الحساء مالح."], pretzel: ["البريتزل", "البريتزل مالح."], fresa: ["الفراولة", "الفراولة حلوة."],
         pescado: ["السمك", ""], galleta: ["البسكويت", "البسكويت حلو."], pizza: ["البيتزا", ""], queso: ["الجبن", ""], tomate: ["الطماطم", ""]}
  };
  const saveurDe = k => { const a = D.aliments[k]; return a && a.saveur || null; };
  // trop … / quelque chose de … : [adverbe « trop sucré », « quelque chose de sucré »]
  const SAV = {
    ru: {dulce: ["Слишком сладко!", "что-то сладкое"], salado: ["Слишком солёно!", "что-то солёное"], picante: ["Слишком остро!", "что-то острое"],
         amargo: ["Слишком горько!", "что-то горькое"], acido: ["Слишком кисло!", "что-то кислое"]},
    uk: {dulce: ["Занадто солодко!", "щось солодке"], salado: ["Занадто солоно!", "щось солоне"], picante: ["Занадто гостро!", "щось гостре"],
         amargo: ["Занадто гірко!", "щось гірке"], acido: ["Занадто кисло!", "щось кисле"]},
    pl: {dulce: ["Za słodkie!", "czegoś słodkiego"], salado: ["Za słone!", "czegoś słonego"], picante: ["Za ostre!", "czegoś ostrego"],
         amargo: ["Za gorzkie!", "czegoś gorzkiego"], acido: ["Za kwaśne!", "czegoś kwaśnego"]},
    tr: {dulce: ["Çok tatlı!", "tatlı bir şey"], salado: ["Çok tuzlu!", "tuzlu bir şey"], picante: ["Çok acılı!", "acılı bir şey"],
         amargo: ["Çok acı!", "acı bir şey"], acido: ["Çok ekşi!", "ekşi bir şey"]},
    fa: {dulce: ["خیلی شیرین است!", "چیزی شیرین"], salado: ["خیلی شور است!", "چیزی شور"], picante: ["خیلی تند است!", "چیزی تند"],
         amargo: ["خیلی تلخ است!", "چیزی تلخ"], acido: ["خیلی ترش است!", "چیزی ترش"]},
    ar: {dulce: ["حلو جدًا!", "شيئًا حلوًا"], salado: ["مالح جدًا!", "شيئًا مالحًا"], picante: ["حار جدًا!", "شيئًا حارًّا"],
         amargo: ["مر جدًا!", "شيئًا مرًّا"], acido: ["حامض جدًا!", "شيئًا حامضًا"]}
  };
  // ---------- les quantités : le contenant et le contenu (génitif en uk, pl, ru) ----------
  const CT = {
    ru: {kilo: "килограмм", botella: "бутылка", vaso: "стакан", taza: "чашка", trozo: "кусок", lata: "банка", docena: "десяток", loncha: "ломтик", litro: "литр", poco: "немного"},
    uk: {kilo: "кілограм", botella: "пляшка", vaso: "склянка", taza: "чашка", trozo: "шматок", lata: "банка", docena: "десяток", loncha: "скибочка", litro: "літр", poco: "трохи"},
    pl: {kilo: "kilogram", botella: "butelka", vaso: "szklanka", taza: "filiżanka", trozo: "kawałek", lata: "puszka", docena: "tuzin", loncha: "plasterek", litro: "litr", poco: "trochę"},
    tr: {kilo: "bir kilo", botella: "bir şişe", vaso: "bir bardak", taza: "bir fincan", trozo: "bir dilim", lata: "bir kutu", docena: "bir düzine", loncha: "bir dilim", litro: "bir litre", poco: "biraz"},
    fa: {kilo: "یک کیلو", botella: "یک بطری", vaso: "یک لیوان", taza: "یک فنجان", trozo: "یک تکه", lata: "یک قوطی", docena: "یک دوجین", loncha: "یک برش", litro: "یک لیتر", poco: "کمی"},
    ar: {kilo: "كيلو", botella: "زجاجة", vaso: "كوب", taza: "فنجان", trozo: "قطعة", lata: "علبة", docena: "دزينة", loncha: "شريحة", litro: "لتر", poco: "قليل من"}
  };
  const CU = {
    ru: {naranja: "апельсинов", agua: "воды", leche: "молока", te: "чая", tarta: "торта", tomate: "помидоров", huevo: "яиц", queso: "сыра", azucar: "сахара"},
    uk: {naranja: "апельсинів", agua: "води", leche: "молока", te: "чаю", tarta: "торта", tomate: "помідорів", huevo: "яєць", queso: "сиру", azucar: "цукру"},
    pl: {naranja: "pomarańczy", agua: "wody", leche: "mleka", te: "herbaty", tarta: "ciasta", tomate: "pomidorów", huevo: "jajek", queso: "sera", azucar: "cukru"},
    tr: {naranja: "portakal", agua: "su", leche: "süt", te: "çay", tarta: "pasta", tomate: "domates", huevo: "yumurta", queso: "peynir", azucar: "şeker"},
    fa: {naranja: "پرتقال", agua: "آب", leche: "شیر", te: "چای", tarta: "کیک", tomate: "گوجه‌فرنگی", huevo: "تخم‌مرغ", queso: "پنیر", azucar: "شکر"},
    ar: {naranja: "برتقال", agua: "ماء", leche: "حليب", te: "شاي", tarta: "كعك", tomate: "طماطم", huevo: "بيض", queso: "جبن", azucar: "السكر"}
  };
  // ---------- la liste de courses : le produit (génitif en uk, pl, ru) et les unités ----------
  const PROD = {
    ru: {tomates: "помидоров", patatas: "картофеля", queso: "сыра", naranjas: "апельсинов", jamon: "ветчины", arroz: "риса", leche: "молока", agua: "воды", aceite: "масла",
         nudeln: "макарон", manzanas: "яблок", cafe: "кофе", galletas: "печенья"},
    uk: {tomates: "помідорів", patatas: "картоплі", queso: "сиру", naranjas: "апельсинів", jamon: "шинки", arroz: "рису", leche: "молока", agua: "води", aceite: "олії",
         nudeln: "макаронів", manzanas: "яблук", cafe: "кави", galletas: "печива"},
    pl: {tomates: "pomidorów", patatas: "ziemniaków", queso: "sera", naranjas: "pomarańczy", jamon: "szynki", arroz: "ryżu", leche: "mleka", agua: "wody", aceite: "oleju",
         nudeln: "makaronu", manzanas: "jabłek", cafe: "kawy", galletas: "ciastek"},
    tr: {tomates: "domates", patatas: "patates", queso: "peynir", naranjas: "portakal", jamon: "jambon", arroz: "pirinç", leche: "süt", agua: "su", aceite: "zeytinyağı",
         nudeln: "makarna", manzanas: "elma", cafe: "kahve", galletas: "bisküvi"},
    fa: {tomates: "گوجه‌فرنگی", patatas: "سیب‌زمینی", queso: "پنیر", naranjas: "پرتقال", jamon: "ژامبون", arroz: "برنج", leche: "شیر", agua: "آب", aceite: "روغن",
         nudeln: "ماکارونی", manzanas: "سیب", cafe: "قهوه", galletas: "بیسکویت"},
    ar: {tomates: "طماطم", patatas: "بطاطس", queso: "جبن", naranjas: "برتقال", jamon: "لحم مقدد", arroz: "أرز", leche: "حليب", agua: "ماء", aceite: "زيت",
         nudeln: "معكرونة", manzanas: "تفاح", cafe: "قهوة", galletas: "بسكويت"}
  };
  const UNITE = {ru: {kg: "кг", g: "г", l: "л", p: ["пачка", "пачки"]}, uk: {kg: "кг", g: "г", l: "л", p: ["пачка", "пачки"]},
                 pl: {kg: "kg", g: "g", l: "l", p: ["opakowanie", "opakowania"]}, tr: {kg: "kg", g: "g", l: "l", p: ["paket", "paket"]},
                 fa: {kg: "کیلو", g: "گرم", l: "لیتر", p: ["بسته", "بسته"]}, ar: {kg: "كغ", g: "غ", l: "ل", p: ["علبة", "علبة"]}};
  // « 1 kg Tomaten », « ½ kg queso », « 2 Packungen Kekse », « 1 Pfund Tomaten » (½ kg)
  function ligneListe(lg, ecrit, prod){
    const [n, u] = ecrit.split(" "), U = UNITE[lg];
    let q = n, unite;
    if (/^Pfund/.test(u)){ q = n === "1" ? "½" : String(+n / 2); unite = U.kg; }
    else if (/^Packung/.test(u)) unite = U.p[n === "1" ? 0 : 1];
    else unite = U[u] || u;
    return lg === "ar" ? q + " " + unite + " " + PROD.ar[prod] : q + " " + unite + " " + PROD[lg][prod];
  }
  // ---------- le café : [ce qu'on dit, ce qu'on fait] ----------
  const CAFE = {
    ru: {carta: ["Меню, пожалуйста.", "Марк просит меню."], pedir: ["Мне кофе, пожалуйста.", "Марк заказывает кофе."], camarera: ["Пожалуйста.", "Официантка приносит кофе."],
         cuenta: ["Счёт, пожалуйста.", "Марк просит счёт."], pagar: ["Можно заплатить картой?", "Марк платит картой."], propina: ["Это вам.", "Томас оставляет чаевые."]},
    uk: {carta: ["Меню, будь ласка.", "Марк просить меню."], pedir: ["Мені каву, будь ласка.", "Марк замовляє каву."], camarera: ["Прошу.", "Офіціантка приносить каву."],
         cuenta: ["Рахунок, будь ласка.", "Марк просить рахунок."], pagar: ["Можна заплатити карткою?", "Марк платить карткою."], propina: ["Це вам.", "Томас залишає чайові."]},
    pl: {carta: ["Poproszę kartę.", "Mark prosi o kartę."], pedir: ["Poproszę kawę.", "Mark zamawia kawę."], camarera: ["Proszę bardzo.", "Kelnerka przynosi kawę."],
         cuenta: ["Poproszę rachunek.", "Mark prosi o rachunek."], pagar: ["Mogę zapłacić kartą?", "Mark płaci kartą."], propina: ["To dla pani.", "Tomás zostawia napiwek."]},
    tr: {carta: ["Menü lütfen.", "Mark menüyü istiyor."], pedir: ["Bir kahve lütfen.", "Mark bir kahve sipariş ediyor."], camarera: ["Buyurun.", "Garson kahveyi getiriyor."],
         cuenta: ["Hesap lütfen.", "Mark hesabı istiyor."], pagar: ["Kartla ödeyebilir miyim?", "Mark kartla ödüyor."], propina: ["Bu sizin için.", "Tomás bahşiş bırakıyor."]},
    fa: {carta: ["لطفاً منو را بیاورید.", "مارک منو را می‌خواهد."], pedir: ["یک قهوه، لطفاً.", "مارک یک قهوه سفارش می‌دهد."], camarera: ["بفرمایید.", "پیشخدمت قهوه را می‌آورد."],
         cuenta: ["صورت‌حساب، لطفاً.", "مارک صورت‌حساب را می‌خواهد."], pagar: ["می‌توانم با کارت پرداخت کنم؟", "مارک با کارت پرداخت می‌کند."], propina: ["این برای شماست.", "توماس انعام می‌گذارد."]},
    ar: {carta: ["قائمة الطعام من فضلك.", "يطلب مارك قائمة الطعام."], pedir: ["قهوة من فضلك.", "يطلب مارك قهوة."], camarera: ["تفضّل.", "تُحضر النادلة القهوة."],
         cuenta: ["الحساب من فضلك.", "يطلب مارك الحساب."], pagar: ["هل يمكنني الدفع بالبطاقة؟", "يدفع مارك بالبطاقة."], propina: ["هذا لك.", "يترك توماس بقشيشًا."]}
  };
  const ANONYMES = {
    ru: {Kellner: "мужчина с седыми волосами", Kellnerin: "женщина с кудрявыми волосами"}, uk: {Kellner: "чоловік із сивим волоссям", Kellnerin: "жінка з кучерявим волоссям"},
    pl: {Kellner: "mężczyzna z siwymi włosami", Kellnerin: "kobieta z kręconymi włosami"}, tr: {Kellner: "kır saçlı adam", Kellnerin: "kıvırcık saçlı kadın"},
    fa: {Kellner: "مرد موجوگندمی", Kellnerin: "زن موفرفری"}, ar: {Kellner: "الرجل ذو الشعر الرمادي", Kellnerin: "المرأة ذات الشعر المجعد"}
  };
  const ROLE = {
    ru: {camarero: "официант", camarera: "официантка", cliente: "посетитель", Kellner: "официант", Kellnerin: "официантка"},
    uk: {camarero: "офіціант", camarera: "офіціантка", cliente: "відвідувач", Kellner: "офіціант", Kellnerin: "офіціантка"},
    pl: {camarero: "kelner", camarera: "kelnerka", cliente: "klient", Kellner: "kelner", Kellnerin: "kelnerka"},
    tr: {camarero: "garson", camarera: "garson", cliente: "müşteri", Kellner: "garson", Kellnerin: "garson"},
    fa: {camarero: "پیشخدمت", camarera: "پیشخدمت", cliente: "مشتری", Kellner: "پیشخدمت", Kellnerin: "پیشخدمت"},
    ar: {camarero: "النادل", camarera: "النادلة", cliente: "زبون", Kellner: "النادل", Kellnerin: "النادلة"}
  };
  // ---------- la carte : [un (complément), deux (complément), un (sujet de « coûte »)] ----------
  const CARTE = {
    ru: {cafe: ["кофе", "два кофе", "Кофе"], te: ["чай", "два чая", "Чай"], zumo: ["апельсиновый сок", "два апельсиновых сока", "Апельсиновый сок"],
         agua: ["бутылку воды", "две бутылки воды", "Бутылка воды"], cerveza: ["пиво", "два пива", "Пиво"], tarta: ["кусок торта", "два куска торта", "Кусок торта"],
         bocadillo: ["бутерброд", "два бутерброда", "Бутерброд"], helado: ["мороженое", "две порции мороженого", "Мороженое"]},
    uk: {cafe: ["каву", "дві кави", "Кава"], te: ["чай", "два чаї", "Чай"], zumo: ["апельсиновий сік", "два апельсинові соки", "Апельсиновий сік"],
         agua: ["пляшку води", "дві пляшки води", "Пляшка води"], cerveza: ["пиво", "два пива", "Пиво"], tarta: ["шматок торта", "два шматки торта", "Шматок торта"],
         bocadillo: ["бутерброд", "два бутерброди", "Бутерброд"], helado: ["морозиво", "дві порції морозива", "Морозиво"]},
    pl: {cafe: ["kawę", "dwie kawy", "Kawa"], te: ["herbatę", "dwie herbaty", "Herbata"], zumo: ["sok pomarańczowy", "dwa soki pomarańczowe", "Sok pomarańczowy"],
         agua: ["wodę", "dwie wody", "Woda"], cerveza: ["piwo", "dwa piwa", "Piwo"], tarta: ["kawałek ciasta", "dwa kawałki ciasta", "Kawałek ciasta"],
         bocadillo: ["kanapkę", "dwie kanapki", "Kanapka"], helado: ["lody", "dwie porcje lodów", "Lody"]},
    tr: {cafe: ["bir kahve", "iki kahve", "Bir kahve"], te: ["bir çay", "iki çay", "Bir çay"], zumo: ["bir portakal suyu", "iki portakal suyu", "Bir portakal suyu"],
         agua: ["bir su", "iki su", "Bir su"], cerveza: ["bir bira", "iki bira", "Bir bira"], tarta: ["bir dilim pasta", "iki dilim pasta", "Bir dilim pasta"],
         bocadillo: ["bir sandviç", "iki sandviç", "Bir sandviç"], helado: ["bir dondurma", "iki dondurma", "Bir dondurma"]},
    fa: {cafe: ["یک قهوه", "دو قهوه", "یک قهوه"], te: ["یک چای", "دو چای", "یک چای"], zumo: ["یک آب پرتقال", "دو آب پرتقال", "یک آب پرتقال"],
         agua: ["یک بطری آب", "دو بطری آب", "یک بطری آب"], cerveza: ["یک آبجو", "دو آبجو", "یک آبجو"], tarta: ["یک تکه کیک", "دو تکه کیک", "یک تکه کیک"],
         bocadillo: ["یک ساندویچ", "دو ساندویچ", "یک ساندویچ"], helado: ["یک بستنی", "دو بستنی", "یک بستنی"]},
    ar: {cafe: ["قهوة", "فنجانين من القهوة", "القهوة"], te: ["شايًا", "كوبين من الشاي", "الشاي"], zumo: ["عصير برتقال", "كوبين من عصير البرتقال", "عصير البرتقال"],
         agua: ["زجاجة ماء", "زجاجتي ماء", "زجاجة الماء"], cerveza: ["بيرة", "زجاجتي بيرة", "البيرة"], tarta: ["قطعة كعك", "قطعتي كعك", "قطعة الكعك"],
         bocadillo: ["شطيرة", "شطيرتين", "الشطيرة"], helado: ["بوظة", "طبقين من البوظة", "البوظة"]}
  };
  // l'allemand appris : une Brezel à la place du bocadillo
  const CARTE_DE = {ru: ["крендель", "два кренделя", "Крендель"], uk: ["брецель", "два брецелі", "Брецель"], pl: ["precel", "dwa precle", "Precel"],
                    tr: ["bir pretzel", "iki pretzel", "Bir pretzel"], fa: ["یک پرتزل", "دو پرتزل", "یک پرتزل"], ar: ["بريتزل", "قطعتي بريتزل", "البريتزل"]};
  const carte = (lg, cle) => APPRENDRE === "de" && cle === "bocadillo" ? CARTE_DE[lg] : CARTE[lg][cle];
  const PL_SUJET = {pl: ["helado"]};       // « Lody kosztują »

  const POSITIF = r => r === "encanta" || r === "gusta";
  const B = {
    ru: {
      aime: g => nom("ru", g.p) + {encanta: " обожает ", gusta: " любит ", no: " не любит ", nada: " совсем не любит "}[g.r] + AL.ru[g.a][0] + ".",
      dit: (k, r) => POSITIF(r) ? "Очень вкусно!" : r === "nada" ? "Какая гадость!" : saveurDe(k) ? SAV.ru[saveurDe(k)][0] : "Я не люблю " + AL.ru[k][0] + ".",
      probar: (p, s) => nom("ru", p) + " пробует " + SAV.ru[s][1] + ".", saveur: k => AL.ru[k][1],
      qte: (c, d) => maj(CT.ru[c]) + " " + CU.ru[d] + ".",
      role: (q, mot) => maj(q) + " — " + ROLE.ru[mot] + ".",
      commande: (qui, cuenta, items, total) => qui + (cuenta ? (items.pl ? " просят счёт: " : " просит счёт: ") : (items.pl ? " берут " : " берёт ")) + items.l + ". С вас " + prix(total) + ".",
      cuesta: (cle, p) => carte("ru", cle)[2] + " стоит " + prix(p) + "."
    },
    uk: {
      aime: g => nom("uk", g.p) + {encanta: " обожнює ", gusta: " любить ", no: " не любить ", nada: " зовсім не любить "}[g.r] + AL.uk[g.a][0] + ".",
      dit: (k, r) => POSITIF(r) ? "Дуже смачно!" : r === "nada" ? "Яка гидота!" : saveurDe(k) ? SAV.uk[saveurDe(k)][0] : "Я не люблю " + AL.uk[k][0] + ".",
      probar: (p, s) => nom("uk", p) + " куштує " + SAV.uk[s][1] + ".", saveur: k => AL.uk[k][1],
      qte: (c, d) => maj(CT.uk[c]) + " " + CU.uk[d] + ".",
      role: (q, mot) => maj(q) + " — " + ROLE.uk[mot] + ".",
      commande: (qui, cuenta, items, total) => qui + (cuenta ? (items.pl ? " просять рахунок: " : " просить рахунок: ") : (items.pl ? " беруть " : " бере ")) + items.l + ". З вас " + prix(total) + ".",
      cuesta: (cle, p) => carte("uk", cle)[2] + " коштує " + prix(p) + "."
    },
    pl: {
      aime: g => nom("pl", g.p) + {encanta: " uwielbia " + AL.pl[g.a][0], gusta: " lubi " + AL.pl[g.a][0], no: " nie lubi " + AL.pl[g.a][1], nada: " w ogóle nie lubi " + AL.pl[g.a][1]}[g.r] + ".",
      dit: (k, r) => POSITIF(r) ? "Pyszne!" : r === "nada" ? "Obrzydliwe!" : saveurDe(k) ? SAV.pl[saveurDe(k)][0] : "Nie lubię " + AL.pl[k][1] + ".",
      probar: (p, s) => nom("pl", p) + " próbuje " + SAV.pl[s][1] + ".", saveur: k => AL.pl[k][2],
      qte: (c, d) => maj(CT.pl[c]) + " " + CU.pl[d] + ".",
      role: (q, mot) => maj(q) + " to " + ROLE.pl[mot] + ".",
      commande: (qui, cuenta, items, total) => qui + (cuenta ? (items.pl ? " proszą o rachunek: " : " prosi o rachunek: ") : (items.pl ? " biorą " : " bierze ")) + items.l + ". Razem " + prix(total) + ".",
      cuesta: (cle, p) => carte("pl", cle)[2] + ((PL_SUJET.pl.includes(cle)) ? " kosztują " : " kosztuje ") + prix(p) + "."
    },
    tr: {
      aime: g => nom("tr", g.p) + " " + AL.tr[g.a][0] + {encanta: " çok sever", gusta: " sever", no: " sevmez", nada: " hiç sevmez"}[g.r] + ".",
      dit: (k, r) => POSITIF(r) ? "Çok lezzetli!" : r === "nada" ? "İğrenç!" : saveurDe(k) ? SAV.tr[saveurDe(k)][0] : maj(AL.tr[k][0]) + " sevmem.",
      probar: (p, s) => nom("tr", p) + " " + SAV.tr[s][1] + " tadıyor.", saveur: k => AL.tr[k][1],
      qte: (c, d) => maj(CT.tr[c]) + " " + CU.tr[d] + ".",
      role: (q, mot) => maj(q) + " " + ROLE.tr[mot] + ".",
      commande: (qui, cuenta, items, total) => qui + (cuenta ? " hesabı istiyor: " + items.l : " " + items.l + (items.pl ? " alıyorlar" : " alıyor")) + ". Toplam " + prix(total) + ".",
      cuesta: (cle, p) => carte("tr", cle)[2] + " " + prix(p) + "."
    },
    fa: {
      aime: g => nom("fa", g.p) + " " + AL.fa[g.a][0] + " را " + {encanta: "خیلی دوست دارد", gusta: "دوست دارد", no: "دوست ندارد", nada: "اصلاً دوست ندارد"}[g.r] + ".",
      dit: (k, r) => POSITIF(r) ? "خیلی خوشمزه است!" : r === "nada" ? "چقدر بدمزه است!" : saveurDe(k) ? SAV.fa[saveurDe(k)][0] : AL.fa[k][0] + " را دوست ندارم.",
      probar: (p, s) => nom("fa", p) + " " + SAV.fa[s][1] + " می‌چشد.", saveur: k => AL.fa[k][1],
      qte: (c, d) => CT.fa[c] + " " + CU.fa[d] + ".",
      role: (q, mot) => q + " " + ROLE.fa[mot] + " است.",
      commande: (qui, cuenta, items, total) => qui + (cuenta ? " صورت‌حساب را می‌خواه" + (items.pl ? "ند: " : "د: ") + items.l : " " + items.l + (items.pl ? " سفارش می‌دهند" : " سفارش می‌دهد")) + ". می‌شود " + prix(total) + ".",
      cuesta: (cle, p) => carte("fa", cle)[2] + " " + prix(p) + " است."
    },
    ar: {
      aime: g => { const f = sexe(g.p) === "f";
        return {encanta: (f ? "تعشق " : "يعشق "), gusta: (f ? "تحب " : "يحب "), no: (f ? "لا تحب " : "لا يحب "), nada: (f ? "لا تحب " : "لا يحب ")}[g.r] + nom("ar", g.p) + " " + AL.ar[g.a][0] + (g.r === "nada" ? " أبدًا." : "."); },
      dit: (k, r) => POSITIF(r) ? "لذيذ جدًا!" : r === "nada" ? "مقرف!" : saveurDe(k) ? SAV.ar[saveurDe(k)][0] : "لا أحب " + AL.ar[k][0] + ".",
      probar: (p, s) => (sexe(p) === "f" ? "تتذوّق " : "يتذوّق ") + nom("ar", p) + " " + SAV.ar[s][1] + ".", saveur: k => AL.ar[k][1],
      qte: (c, d) => CT.ar[c] + " " + CU.ar[d] + ".",
      role: (q, mot, f) => q + (f ? " هي " : " هو ") + ROLE.ar[mot] + ".",
      commande: (qui, cuenta, items, total, f) => (f ? "تطلب " : "يطلب ") + qui + (cuenta ? " الحساب: " : " ") + items.l + ". المبلغ " + prix(total) + ".",
      cuesta: (cle, p) => "سعر " + carte("ar", cle)[2] + " " + prix(p) + "."
    }
  };

  // ---------- traduire(q) : la même forme que la page ----------
  // les leurres de « ce que dit la personne » : délicieux, très bon, dégoûtant, trop …
  const DIT = {ru: ["Очень вкусно!", "Очень хорошо!", "Какая гадость!"], uk: ["Дуже смачно!", "Дуже добре!", "Яка гидота!"], pl: ["Pyszne!", "Bardzo dobre!", "Obrzydliwe!"],
               tr: ["Çok lezzetli!", "Çok güzel!", "İğrenç!"], fa: ["خیلی خوشمزه است!", "خیلی خوب است!", "چقدر بدمزه است!"], ar: ["لذيذ جدًا!", "جيد جدًا!", "مقرف!"]};
  const R = {};
  for (const lg of LANGUES){
    const b = B[lg];
    R[lg] = {ditTr: {pos: DIT[lg][0], bon: DIT[lg][1], asco: DIT[lg][2], trop: s => SAV[lg][s][0]}, traduire(q, quiCafe){
      if (!q) return null;
      if (q.aime) return b.aime(q.aime);
      if (q.probar) return b.probar(q.probar.p, saveurDe(q.probar.a));
      if (q.saveur) return b.saveur(q.saveur) || null;
      if (q.dit) return b.dit(q.dit.a, q.dit.r);
      if (q.qte) return b.qte(q.qte.c, q.qte.d);
      if (q.liste) return ligneListe(lg, q.liste[0], q.liste[3]) + ".";
      if (q.cafe){ const c = CAFE[lg][q.cafe.id]; return c ? c[q.cafe.fait ? 1 : 0] : null; }
      if (q.role){ const p = q.role.p, qui = (D.anonymes || {})[p] ? quiCafe(p, lg) : nom(lg, p); return b.role(qui, q.role.mot, sexe(p) === "f"); }
      if (q.commande){ const c = q.commande, qui = c.qui.map(p => nom(lg, p)).join(ET[lg]);
        const t = c.items.map(([it, n]) => carte(lg, it.cle)[n > 1 ? 1 : 0]);
        return b.commande(qui, c.cuenta, {l: liste(lg, t), pl: c.qui.length > 1}, c.total, sexe(c.qui[0]) === "f"); }
      if (q.cuesta) return b.cuesta(q.cuesta.cle, q.cuesta.p);
      return null;
    }};
  }

  // ---------- le branchement dans la donnée (les traductions des boutons : contenant, contenu, produit, carte, figurants) ----------
  const manque = [];
  for (const lg of LANGUES){
    for (const c in D.tradContenants){ if (CT[lg][c]) D.tradContenants[c][lg] = CT[lg][c]; else manque.push("contenant " + c + " " + lg); }
    for (const d in D.contenus){ if (CU[lg][d]) D.contenus[d].tr[lg] = CU[lg][d]; else manque.push("contenu " + d + " " + lg); }
    for (const p in D.produits){ if (PROD[lg][p]) D.produits[p][lg] = PROD[lg][p]; else manque.push("produit " + p + " " + lg); }
    for (const k in D.tradCarte){ if (CARTE[lg][k]) D.tradCarte[k][lg] = CARTE[lg][k].slice(0, 2); else manque.push("carte " + k + " " + lg); }
    for (const k in (D.tradCarteDe || {})) D.tradCarteDe[k][lg] = CARTE_DE[lg].slice(0, 2);
    for (const a in (D.anonymes || {})) if (ANONYMES[lg][a]) D.anonymes[a][lg] = ANONYMES[lg][a];
    for (const m of D.cafe){ if (CAFE[lg][m.id]) m.tr[lg] = CAFE[lg][m.id]; else manque.push("cafe " + m.id + " " + lg); }
    for (const k in D.tradAliments) if (!AL[lg][k]) manque.push("aliment " + k + " " + lg);
  }
  if (manque.length) console.error("manger/langues.js : morceaux absents", manque);
  return R;
}
