// « Les loisirs » dans les langues d'interface sans phrase traduite jusqu'ici (lot 9 de l'alignement des thèmes,
// 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour qui
// apprend l'espagnol.
//
// LE CHEMIN NATIF : la page fabrique ses phrases avec cinq fonctions (fait, aime, freq, propose, repond) sur les 15
// activités et les 15 personnes. On donne ici, pour chaque activité, ses formes dans chaque langue, et la grammaire
// de chacune : « любит / любят » + infinitif, « никогда не играет » ; le turc à l'aoriste (futbol oynar / oynamaz,
// oynamayı sever, oynayalım mı?) ; le persan au subjonctif (دوست دارد فوتبال بازی کند) ; l'arabe au nom verbal
// (يحب لعب كرة القدم) et au verbe devant le sujet, accordé à son genre (يلعب فيليكس / تلعب روزا).
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesLoisirs(D, APPRENDRE){
  if (APPRENDRE !== "de" && APPRENDRE !== "es") return {};
  const LANGUES = APPRENDRE === "de" ? ["tr", "uk", "pl", "ru", "fa", "ar"] : ["ar"];
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
  const NOMS = {
    ru: {Felix: "Феликс", Rosa: "Роза", Diego: "Диего", Ines: "Инес", Gisela: "Гизела", Sophie: "Софи", Tomas: "Томас", Katrin: "Катрин",
         Javier: "Хавьер", Elena: "Елена", Carmen: "Кармен", Heinz: "Хайнц", Pablo: "Пабло", Marta: "Марта", Lena: "Лена"},
    uk: {Felix: "Фелікс", Rosa: "Роза", Diego: "Дієго", Ines: "Інес", Gisela: "Гізела", Sophie: "Софі", Tomas: "Томас", Katrin: "Катрін",
         Javier: "Хавʼєр", Elena: "Елена", Carmen: "Кармен", Heinz: "Гайнц", Pablo: "Пабло", Marta: "Марта", Lena: "Лена"},
    fa: {Felix: "فلیکس", Rosa: "روزا", Diego: "دیه‌گو", Ines: "اینس", Gisela: "گیزلا", Sophie: "سوفی", Tomas: "توماس", Katrin: "کاترین",
         Javier: "خاویر", Elena: "النا", Carmen: "کارمن", Heinz: "هاینتس", Pablo: "پابلو", Marta: "مارتا", Lena: "لنا"},
    ar: {Felix: "فيليكس", Rosa: "روزا", Diego: "دييغو", Ines: "إينيس", Gisela: "غيزيلا", Sophie: "صوفي", Tomas: "توماس", Katrin: "كاترين",
         Javier: "خافيير", Elena: "إيلينا", Carmen: "كارمن", Heinz: "هاينتس", Pablo: "بابلو", Marta: "مارتا", Lena: "لينا"}
  };
  const nom = (lg, p) => (NOMS[lg] || {})[p] || D.personnes[p].nom;
  const ET = {ru: " и ", uk: " і ", pl: " i ", tr: " ve ", fa: " و ", ar: " و"};
  const noms = (lg, ps) => ps.map(p => nom(lg, p)).join(ET[lg]);
  const fem = p => D.personnes[p].sexe === "f";

  // ---------- les activités ----------
  // ru, uk : [3e sg, infinitif] ; pl : [3e sg, infinitif, « Może razem … ? »] ; tr : [aoriste, aoriste négatif, nom verbal,
  // nom verbal à l'accusatif, optatif 1re pl] ; fa : [complément, verbe : کردن / زدن / گرفتن / رقصیدن / خواندن / دویدن]
  // ar : [verbe 3e m. sg, complément, nom verbal]
  const A = {
    ru: {futbol: ["играет в футбол", "играть в футбол"], tenis: ["играет в теннис", "играть в теннис"], baloncesto: ["играет в баскетбол", "играть в баскетбол"],
         guitarra: ["играет на гитаре", "играть на гитаре"], piano: ["играет на пианино", "играть на пианино"], violin: ["играет на скрипке", "играть на скрипке"],
         bici: ["катается на велосипеде", "кататься на велосипеде"], deporte: ["занимается спортом", "заниматься спортом"], fotos: ["фотографирует", "фотографировать"],
         bailar: ["танцует", "танцевать"], cantar: ["поёт", "петь"], leer: ["читает", "читать"], cocinar: ["готовит", "готовить"], pintar: ["рисует", "рисовать"],
         correr: ["бегает", "бегать"]},
    uk: {futbol: ["грає у футбол", "грати у футбол"], tenis: ["грає в теніс", "грати в теніс"], baloncesto: ["грає в баскетбол", "грати в баскетбол"],
         guitarra: ["грає на гітарі", "грати на гітарі"], piano: ["грає на піаніно", "грати на піаніно"], violin: ["грає на скрипці", "грати на скрипці"],
         bici: ["катається на велосипеді", "кататися на велосипеді"], deporte: ["займається спортом", "займатися спортом"], fotos: ["фотографує", "фотографувати"],
         bailar: ["танцює", "танцювати"], cantar: ["співає", "співати"], leer: ["читає", "читати"], cocinar: ["готує", "готувати"], pintar: ["малює", "малювати"],
         correr: ["бігає", "бігати"]},
    pl: {futbol: ["gra w piłkę nożną", "grać w piłkę nożną", "zagramy w piłkę nożną"], tenis: ["gra w tenisa", "grać w tenisa", "zagramy w tenisa"],
         baloncesto: ["gra w koszykówkę", "grać w koszykówkę", "zagramy w koszykówkę"], guitarra: ["gra na gitarze", "grać na gitarze", "pogramy na gitarze"],
         piano: ["gra na pianinie", "grać na pianinie", "pogramy na pianinie"], violin: ["gra na skrzypcach", "grać na skrzypcach", "pogramy na skrzypcach"],
         bici: ["jeździ na rowerze", "jeździć na rowerze", "pojeździmy na rowerze"], deporte: ["uprawia sport", "uprawiać sport", "poćwiczymy"],
         fotos: ["robi zdjęcia", "robić zdjęcia", "porobimy zdjęcia"], bailar: ["tańczy", "tańczyć", "potańczymy"], cantar: ["śpiewa", "śpiewać", "pośpiewamy"],
         leer: ["czyta", "czytać", "poczytamy"], cocinar: ["gotuje", "gotować", "ugotujemy coś"], pintar: ["maluje", "malować", "pomalujemy"],
         correr: ["biega", "biegać", "pobiegamy"]},
    tr: {futbol: ["futbol oynar", "futbol oynamaz", "futbol oynamak", "futbol oynamayı", "futbol oynayalım"],
         tenis: ["tenis oynar", "tenis oynamaz", "tenis oynamak", "tenis oynamayı", "tenis oynayalım"],
         baloncesto: ["basketbol oynar", "basketbol oynamaz", "basketbol oynamak", "basketbol oynamayı", "basketbol oynayalım"],
         guitarra: ["gitar çalar", "gitar çalmaz", "gitar çalmak", "gitar çalmayı", "gitar çalalım"],
         piano: ["piyano çalar", "piyano çalmaz", "piyano çalmak", "piyano çalmayı", "piyano çalalım"],
         violin: ["keman çalar", "keman çalmaz", "keman çalmak", "keman çalmayı", "keman çalalım"],
         bici: ["bisiklete biner", "bisiklete binmez", "bisiklete binmek", "bisiklete binmeyi", "bisiklete binelim"],
         deporte: ["spor yapar", "spor yapmaz", "spor yapmak", "spor yapmayı", "spor yapalım"],
         fotos: ["fotoğraf çeker", "fotoğraf çekmez", "fotoğraf çekmek", "fotoğraf çekmeyi", "fotoğraf çekelim"],
         bailar: ["dans eder", "dans etmez", "dans etmek", "dans etmeyi", "dans edelim"],
         cantar: ["şarkı söyler", "şarkı söylemez", "şarkı söylemek", "şarkı söylemeyi", "şarkı söyleyelim"],
         leer: ["kitap okur", "kitap okumaz", "kitap okumak", "kitap okumayı", "kitap okuyalım"],
         cocinar: ["yemek yapar", "yemek yapmaz", "yemek yapmak", "yemek yapmayı", "yemek yapalım"],
         pintar: ["resim yapar", "resim yapmaz", "resim yapmak", "resim yapmayı", "resim yapalım"],
         correr: ["koşar", "koşmaz", "koşmak", "koşmayı", "koşalım"]},
    fa: {futbol: ["فوتبال بازی", "کردن"], tenis: ["تنیس بازی", "کردن"], baloncesto: ["بسکتبال بازی", "کردن"], guitarra: ["گیتار", "زدن"], piano: ["پیانو", "زدن"],
         violin: ["ویولن", "زدن"], bici: ["دوچرخه‌سواری", "کردن"], deporte: ["ورزش", "کردن"], fotos: ["عکس", "گرفتن"], bailar: ["", "رقصیدن"],
         cantar: ["آواز", "خواندن"], leer: ["کتاب", "خواندن"], cocinar: ["آشپزی", "کردن"], pintar: ["نقاشی", "کردن"], correr: ["", "دویدن"]},
    ar: {futbol: ["يلعب", "كرة القدم", "لعب كرة القدم"], tenis: ["يلعب", "التنس", "لعب التنس"], baloncesto: ["يلعب", "كرة السلة", "لعب كرة السلة"],
         guitarra: ["يعزف", "على الغيتار", "العزف على الغيتار"], piano: ["يعزف", "على البيانو", "العزف على البيانو"], violin: ["يعزف", "على الكمان", "العزف على الكمان"],
         bici: ["يركب", "الدراجة", "ركوب الدراجة"], deporte: ["يمارس", "الرياضة", "ممارسة الرياضة"], fotos: ["يلتقط", "الصور", "التقاط الصور"],
         bailar: ["يرقص", "", "الرقص"], cantar: ["يغني", "", "الغناء"], leer: ["يقرأ", "", "القراءة"], cocinar: ["يطبخ", "", "الطبخ"], pintar: ["يرسم", "", "الرسم"],
         correr: ["يركض", "", "الركض"]}
  };
  const ADV = {ru: {immer: "всегда", oft: "часто", manchmal: "иногда", selten: "редко"}, uk: {immer: "завжди", oft: "часто", manchmal: "іноді", selten: "рідко"},
               pl: {immer: "zawsze", oft: "często", manchmal: "czasami", selten: "rzadko"}, tr: {immer: "her zaman", oft: "sık sık", manchmal: "bazen", selten: "nadiren"},
               fa: {immer: "همیشه", oft: "اغلب", manchmal: "گاهی", selten: "به‌ندرت"}, ar: {immer: "دائمًا", oft: "كثيرًا", manchmal: "أحيانًا", selten: "نادرًا"}};
  // le persan : le verbe au présent, au négatif et au subjonctif (3e sg, 2e sg, 1re pl, 1re sg, 3e pl)
  const VFA = {"کردن": ["می‌کن", "نمی‌کن", "کن"], "زدن": ["می‌زن", "نمی‌زن", "بزن"], "گرفتن": ["می‌گیر", "نمی‌گیر", "بگیر"], "رقصیدن": ["می‌رقص", "نمی‌رقص", "برقص"],
               "خواندن": ["می‌خوان", "نمی‌خوان", "بخوان"], "دویدن": ["می‌دو", "نمی‌دو", "بدو"]};
  const FIN_FA = {3: "د", 2: "ی", 1: "یم", 0: "م", 6: "ند"};
  const fa = (a, forme, pers) => { const [c, v] = A.fa[a], t = VFA[v]; return (c ? c + " " : "") + t[forme] + FIN_FA[pers]; };
  // l'arabe : le verbe au féminin (تلعب), à la 2e personne (تلعب) et à la 1re du pluriel (نلعب)
  const arV = (a, f) => f ? "ت" + A.ar[a][0].slice(1) : A.ar[a][0];
  const arO = a => A.ar[a][1] ? " " + A.ar[a][1] : "";
  const mi = s => /[aıou][^aıoueiöü]*$/.test(s) ? " mı" : " mi";       // l'interrogation turque, par l'harmonie

  const B = {
    ru: {
      fait: (p, a) => nom("ru", p) + " " + A.ru[a][0] + ".",
      aime: (ps, a, oui) => noms("ru", ps) + (oui ? "" : " не") + (ps.length > 1 ? " любят " : " любит ") + A.ru[a][1] + ".",
      freq: (p, a, q) => nom("ru", p) + (q === "nie" ? " никогда не " : " " + ADV.ru[q] + " ") + A.ru[a][0] + ".",
      propose: (a, f) => f ? "Давай вместе " + A.ru[a][1] + "?" : "Хочешь " + A.ru[a][1] + "?",
      repond: (a, oui) => oui ? "Да, с удовольствием! Я очень люблю " + A.ru[a][1] + "." : "Нет, спасибо. Я не люблю " + A.ru[a][1] + "."
    },
    uk: {
      fait: (p, a) => nom("uk", p) + " " + A.uk[a][0] + ".",
      aime: (ps, a, oui) => noms("uk", ps) + (oui ? "" : " не") + (ps.length > 1 ? " люблять " : " любить ") + A.uk[a][1] + ".",
      freq: (p, a, q) => nom("uk", p) + (q === "nie" ? " ніколи не " : " " + ADV.uk[q] + " ") + A.uk[a][0] + ".",
      propose: (a, f) => f ? "Давай разом " + A.uk[a][1] + "?" : "Хочеш " + A.uk[a][1] + "?",
      repond: (a, oui) => oui ? "Так, залюбки! Я дуже люблю " + A.uk[a][1] + "." : "Ні, дякую. Я не люблю " + A.uk[a][1] + "."
    },
    pl: {
      fait: (p, a) => nom("pl", p) + " " + A.pl[a][0] + ".",
      aime: (ps, a, oui) => noms("pl", ps) + (oui ? "" : " nie") + (ps.length > 1 ? " lubią " : " lubi ") + A.pl[a][1] + ".",
      freq: (p, a, q) => nom("pl", p) + (q === "nie" ? " nigdy nie " : " " + ADV.pl[q] + " ") + A.pl[a][0] + ".",
      propose: (a, f) => f ? "Może razem " + A.pl[a][2] + "?" : "Masz ochotę " + A.pl[a][1] + "?",
      repond: (a, oui) => oui ? "Tak, chętnie! Bardzo lubię " + A.pl[a][1] + "." : "Nie, dziękuję. Nie lubię " + A.pl[a][1] + "."
    },
    tr: {
      fait: (p, a) => nom("tr", p) + " " + A.tr[a][0] + ".",
      aime: (ps, a, oui) => noms("tr", ps) + " " + A.tr[a][3] + (oui ? " sever" : " sevmez") + (ps.length > 1 ? (oui ? "ler" : "ler") : "") + ".",
      freq: (p, a, q) => nom("tr", p) + (q === "nie" ? " hiç " + A.tr[a][1] : " " + ADV.tr[q] + " " + A.tr[a][0]) + ".",
      propose: (a, f) => f ? "Birlikte " + A.tr[a][4] + mi(A.tr[a][4]) + "?" : maj(A.tr[a][2]) + " ister misin?",
      repond: (a, oui) => oui ? "Evet, memnuniyetle! " + maj(A.tr[a][3]) + " çok severim." : "Hayır, teşekkürler. " + maj(A.tr[a][3]) + " sevmem."
    },
    fa: {
      fait: (p, a) => nom("fa", p) + " " + fa(a, 0, 3) + ".",
      aime: (ps, a, oui) => noms("fa", ps) + (oui ? " دوست دار" : " دوست ندار") + (ps.length > 1 ? "ند " : "د ") + fa(a, 2, ps.length > 1 ? 6 : 3) + ".",
      freq: (p, a, q) => nom("fa", p) + (q === "nie" ? " هرگز " + fa(a, 1, 3) : " " + ADV.fa[q] + " " + fa(a, 0, 3)) + ".",
      propose: (a, f) => f ? "با هم " + fa(a, 2, 1) + "؟" : "دوست داری " + fa(a, 2, 2) + "؟",
      repond: (a, oui) => oui ? "بله، با کمال میل! خیلی دوست دارم " + fa(a, 2, 0) + "." : "نه، ممنون. دوست ندارم " + fa(a, 2, 0) + "."
    },
    ar: {
      fait: (p, a) => arV(a, fem(p)) + " " + nom("ar", p) + arO(a) + ".",
      aime: (ps, a, oui) => (oui ? "" : "لا ") + (fem(ps[0]) ? "تحب " : "يحب ") + noms("ar", ps) + " " + A.ar[a][2] + ".",
      freq: (p, a, q) => q === "nie" ? "لا " + arV(a, fem(p)) + " " + nom("ar", p) + arO(a) + " أبدًا." : arV(a, fem(p)) + " " + nom("ar", p) + arO(a) + " " + ADV.ar[q] + ".",
      propose: (a, f) => f ? "هل " + "ن" + A.ar[a][0].slice(1) + arO(a) + " معًا؟" : "هل تريد أن " + "ت" + A.ar[a][0].slice(1) + arO(a) + "؟",
      repond: (a, oui) => oui ? "نعم، بكل سرور! أحب " + A.ar[a][2] + " كثيرًا." : "لا، شكرًا. لا أحب " + A.ar[a][2] + "."
    }
  };
  const manque = [];
  for (const lg of LANGUES) for (const a in D.activites) if (!A[lg][a]) manque.push("activite " + a + " " + lg);
  for (const lg of ["ru", "uk", "fa", "ar"]) for (const p in D.personnes) if (!NOMS[lg][p]) manque.push("personne " + p + " " + lg);
  if (manque.length) console.error("loisirs/langues.js : morceaux absents", manque);
  const R = {};
  for (const lg of LANGUES) R[lg] = B[lg];
  return R;
}
