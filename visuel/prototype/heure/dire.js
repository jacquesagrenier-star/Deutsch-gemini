// « L'HEURE ET LES DATES » : la fabrique des phrases (theme illustre, 16 nov. 2026 ; decision de Jacques : « Oui, fais
// [...] le theme de l'heure »). Rien n'est ecrit phrase par phrase : chaque phrase sort d'une heure (h, m), d'une date
// (jour, mois) ou d'un rendez-vous de l'agenda, par les regles de chaque langue. Le meme fichier sert a la page
// (visuel/prototype/heure.html, le global Dire) et au banc hors navigateur (node tests/heure_banc.js), qui fait dire
// toutes les heures de 0:00 a 23:59 et toutes les dates de l'annee.
//
// Les langues APPRISES : de, es, us (anglais americain), gb (britannique). Les nombres sont toujours en LETTRES (regle
// des voix du 28 oct. : rien a ajouter a audio/lectures). Les TRADUCTIONS, dans les dix langues d'interface des pages :
//   - fr : en lettres, comme on le dit (« deux heures et demie ») -- c'est la que se voit le piege de « halb drei » ;
//   - en : l'anglais de la page elle-meme (britannique, « half past two »), de : l'allemand de la page ;
//   - pt (Bresil), tr, uk, pl, ru, fa, ar : l'heure en chiffres a la maniere de chaque langue (14h30, 14.30, 14:30,
//     ۱۴:۳۰), les jours et les mois declines ou il le faut (у середу, во вторник, we wtorek, 3 Mayıs'ta).
// Le chemin natif des lots des six langues (visuel/<theme>/langues.py) : la phrase traduite est fabriquee par la meme
// regle, avec les memes choix, jamais recopiee. Points a relire par un natif : retours/A-RELIRE-THEMES-<LG>.md.
(function(racine){
"use strict";

// ---------------------------------------------------------------- les nombres en lettres
const DE_N = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn",
  "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"];
const DE_D = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig"];
const nDe = n => n < 20 ? DE_N[n] : (n % 10 ? (n % 10 === 1 ? "ein" : DE_N[n % 10]) + "und" : "") + DE_D[Math.floor(n / 10)];
const ES_N = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce",
  "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
  "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"];
const ES_D = ["", "", "", "treinta", "cuarenta", "cincuenta"];
const nEs = n => n < 30 ? ES_N[n] : ES_D[Math.floor(n / 10)] + (n % 10 ? " y " + ES_N[n % 10] : "");
// « la una », « las veintiuna » : l'heure est feminine
const nEsF = n => nEs(n).replace(/uno$/, "una");
const EN_N = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
  "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
const EN_D = ["", "", "twenty", "thirty", "forty", "fifty"];
const nEn = n => n < 20 ? EN_N[n] : EN_D[Math.floor(n / 10)] + (n % 10 ? "-" + EN_N[n % 10] : "");
const FR_N = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
  "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"];
const FR_D = ["", "", "vingt", "trente", "quarante", "cinquante"];
const nFr = n => n < 20 ? FR_N[n] : FR_D[Math.floor(n / 10)] + (n % 10 === 1 ? " et un" : n % 10 ? "-" + FR_N[n % 10] : "");
const nFrF = n => nFr(n).replace(/(^|\s)un$/, "$1une");

const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
// LE TROU D'UNE QUESTION : chaque sorte marque entre ⟦ ⟧ ce qu'une question peut demander (la preposition « am », le
// moment « abends », le jour « Dienstag ») ; phrase() efface les marques, trou() remplace la premiere par « ___ »
const M = s => "⟦" + s + "⟧";
const h12 = h => (h % 12) || 12;
const suivante = h => (h + 1) % 24;
const deux = n => (n < 10 ? "0" : "") + n;

// ---------------------------------------------------------------- les jours, les mois (0 = lundi, 0 = janvier)
const JOURS = {
  de: ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
  es: ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"],
  en: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
  fr: ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
  pt: ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"],
  tr: ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"],
  uk: ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"],
  ru: ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"],
  pl: ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
  fa: ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"],
  ar: ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
};
// les jours en abrege, en tete des colonnes du calendrier (l'americain commence au dimanche : voir grille())
const JOURS_COURTS = {de: ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"], es: ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"], en: ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]};
const MOIS = {
  de: ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
  es: ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
  en: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  fr: ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
  pt: ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
  tr: ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
  fa: ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن", "ژوئیه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"],
  ar: ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
};
// les cas des langues slaves et les suffixes du turc, ecrits une fois par mot
const MOIS_CAS = {
  uk: {nom: ["січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"],
       gen: ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"],
       ins: ["січнем", "лютим", "березнем", "квітнем", "травнем", "червнем", "липнем", "серпнем", "вереснем", "жовтнем", "листопадом", "груднем"],
       loc: ["січні", "лютому", "березні", "квітні", "травні", "червні", "липні", "серпні", "вересні", "жовтні", "листопаді", "грудні"]},
  ru: {nom: ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"],
       gen: ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"],
       ins: ["январём", "февралём", "мартом", "апрелем", "маем", "июнем", "июлем", "августом", "сентябрём", "октябрём", "ноябрём", "декабрём"],
       loc: ["январе", "феврале", "марте", "апреле", "мае", "июне", "июле", "августе", "сентябре", "октябре", "ноябре", "декабре"]},
  pl: {nom: ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"],
       gen: ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "września", "października", "listopada", "grudnia"],
       ins: ["styczniem", "lutym", "marcem", "kwietniem", "majem", "czerwcem", "lipcem", "sierpniem", "wrześniem", "październikiem", "listopadem", "grudniem"],
       loc: ["styczniu", "lutym", "marcu", "kwietniu", "maju", "czerwcu", "lipcu", "sierpniu", "wrześniu", "październiku", "listopadzie", "grudniu"]},
  // le turc : le mois minuscule hors d'une date (TDK), son ablatif et son locatif ; dans une date, majuscule + apostrophe
  tr: {min: ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"],
       abl: ["ocaktan", "şubattan", "marttan", "nisandan", "mayıstan", "hazirandan", "temmuzdan", "ağustostan", "eylülden", "ekimden", "kasımdan", "aralıktan"],
       loc: ["ocakta", "şubatta", "martta", "nisanda", "mayısta", "haziranda", "temmuzda", "ağustosta", "eylülde", "ekimde", "kasımda", "aralıkta"],
       locDate: ["'ta", "'ta", "'ta", "'da", "'ta", "'da", "'da", "'ta", "'de", "'de", "'da", "'ta"]}
};
const JOURS_CAS = {
  // accusatif apres la preposition (у середу, во вторник, we wtorek), genre (був / була / було)
  uk: {acc: ["у понеділок", "у вівторок", "у середу", "у четвер", "у п'ятницю", "у суботу", "у неділю"], g: ["m", "m", "f", "m", "f", "f", "f"], etait: {m: "був", f: "була"}},
  ru: {acc: ["в понедельник", "во вторник", "в среду", "в четверг", "в пятницу", "в субботу", "в воскресенье"], g: ["m", "m", "f", "m", "f", "f", "n"], etait: {m: "был", f: "была", n: "было"}},
  pl: {acc: ["w poniedziałek", "we wtorek", "w środę", "w czwartek", "w piątek", "w sobotę", "w niedzielę"], g: ["m", "m", "f", "m", "m", "f", "f"], etait: {m: "był", f: "była"}},
  // le passe turc : pazartesiydi, salıydı, pazardı
  tr: {passe: ["pazartesiydi", "salıydı", "çarşambaydı", "perşembeydi", "cumaydı", "cumartesiydi", "pazardı"]},
  pt: {sur: ["na segunda-feira", "na terça-feira", "na quarta-feira", "na quinta-feira", "na sexta-feira", "no sábado", "no domingo"]}
};

// ---------------------------------------------------------------- les rendez-vous de l'agenda
// court : l'etiquette dans l'agenda dessine (la langue apprise) ; g : le genre, la ou le verbe s'accorde (arabe)
const EVTS = ["yoga", "arzt", "fussball", "party", "konzert"];
const EVT = {
  de: {yoga: "der Yogakurs", arzt: "der Termin beim Arzt", fussball: "das Fußballtraining", party: "die Party", konzert: "das Konzert"},
  es: {yoga: "la clase de yoga", arzt: "la cita con el médico", fussball: "el entrenamiento de fútbol", party: "la fiesta", konzert: "el concierto"},
  us: {yoga: "the yoga class", arzt: "the doctor's appointment", fussball: "soccer practice", party: "the party", konzert: "the concert"},
  gb: {yoga: "the yoga class", arzt: "the doctor's appointment", fussball: "football practice", party: "the party", konzert: "the concert"},
  fr: {yoga: "le cours de yoga", arzt: "le rendez-vous chez le médecin", fussball: "l'entraînement de foot", party: "la fête", konzert: "le concert"},
  pt: {yoga: "a aula de ioga", arzt: "a consulta médica", fussball: "o treino de futebol", party: "a festa", konzert: "o show"},
  tr: {yoga: "yoga dersi", arzt: "doktor randevusu", fussball: "futbol antrenmanı", party: "parti", konzert: "konser"},
  uk: {yoga: "заняття йогою", arzt: "прийом у лікаря", fussball: "футбольне тренування", party: "вечірка", konzert: "концерт"},
  ru: {yoga: "занятие йогой", arzt: "приём у врача", fussball: "футбольная тренировка", party: "вечеринка", konzert: "концерт"},
  pl: {yoga: "lekcja jogi", arzt: "wizyta u lekarza", fussball: "trening piłki nożnej", party: "impreza", konzert: "koncert"},
  fa: {yoga: "کلاس یوگا", arzt: "وقت دکتر", fussball: "تمرین فوتبال", party: "مهمانی", konzert: "کنسرت"},
  ar: {yoga: "درس اليوغا", arzt: "موعد الطبيب", fussball: "تمرين كرة القدم", party: "الحفلة", konzert: "الحفل الموسيقي"}
};
const EVT_COURT = {
  de: {yoga: "Yoga", arzt: "Arzt", fussball: "Fußball", party: "Party", konzert: "Konzert"},
  es: {yoga: "Yoga", arzt: "Médico", fussball: "Fútbol", party: "Fiesta", konzert: "Concierto"},
  us: {yoga: "Yoga", arzt: "Doctor", fussball: "Soccer", party: "Party", konzert: "Concert"},
  gb: {yoga: "Yoga", arzt: "Doctor", fussball: "Football", party: "Party", konzert: "Concert"}
};
const EVT_F_AR = {party: true};
// les durees (en minutes) : dauert zwei Stunden, dura media hora, lasts an hour and a half
const DUREES = [20, 30, 45, 60, 90, 120, 180];
const DUREE = {
  de: {20: "zwanzig Minuten", 30: "eine halbe Stunde", 45: "fünfundvierzig Minuten", 60: "eine Stunde", 90: "anderthalb Stunden", 120: "zwei Stunden", 180: "drei Stunden"},
  es: {20: "veinte minutos", 30: "media hora", 45: "cuarenta y cinco minutos", 60: "una hora", 90: "una hora y media", 120: "dos horas", 180: "tres horas"},
  en: {20: "twenty minutes", 30: "half an hour", 45: "forty-five minutes", 60: "an hour", 90: "an hour and a half", 120: "two hours", 180: "three hours"},
  fr: {20: "vingt minutes", 30: "une demi-heure", 45: "quarante-cinq minutes", 60: "une heure", 90: "une heure et demie", 120: "deux heures", 180: "trois heures"},
  pt: {20: "vinte minutos", 30: "meia hora", 45: "quarenta e cinco minutos", 60: "uma hora", 90: "uma hora e meia", 120: "duas horas", 180: "três horas"},
  tr: {20: "yirmi dakika", 30: "yarım saat", 45: "kırk beş dakika", 60: "bir saat", 90: "bir buçuk saat", 120: "iki saat", 180: "üç saat"},
  uk: {20: "двадцять хвилин", 30: "пів години", 45: "сорок п'ять хвилин", 60: "годину", 90: "півтори години", 120: "дві години", 180: "три години"},
  ru: {20: "двадцать минут", 30: "полчаса", 45: "сорок пять минут", 60: "час", 90: "полтора часа", 120: "два часа", 180: "три часа"},
  pl: {20: "dwadzieścia minut", 30: "pół godziny", 45: "czterdzieści pięć minut", 60: "godzinę", 90: "półtorej godziny", 120: "dwie godziny", 180: "trzy godziny"},
  fa: {20: "بیست دقیقه", 30: "نیم ساعت", 45: "چهل و پنج دقیقه", 60: "یک ساعت", 90: "یک ساعت و نیم", 120: "دو ساعت", 180: "سه ساعت"},
  ar: {20: "عشرين دقيقة", 30: "نصف ساعة", 45: "خمسًا وأربعين دقيقة", 60: "ساعة", 90: "ساعة ونصفًا", 120: "ساعتين", 180: "ثلاث ساعات"}
};

// ---------------------------------------------------------------- l'allemand
// L'HEURE COURANTE (sur douze heures) : « halb drei » = 2 h 30 -- la demi-heure VERS trois heures, le piege du
// francophone ; « Viertel nach / vor », « fünf vor halb », « kurz vor / nach ». « ein Uhr » mais « halb eins ».
function courDe(h, m){
  const a = h12(h), s = h12(suivante(h));
  if (m === 0) return (a === 1 ? "ein" : nDe(a)) + " Uhr";
  if (m === 2) return "kurz nach " + nDe(a);
  if (m === 58) return "kurz vor " + nDe(s);
  if (m === 15) return "Viertel nach " + nDe(a);
  if (m === 45) return "Viertel vor " + nDe(s);
  if (m === 30) return "halb " + nDe(s);
  if (m === 25) return "fünf vor halb " + nDe(s);
  if (m === 35) return "fünf nach halb " + nDe(s);
  if (m < 30) return nDe(m) + " nach " + nDe(a);
  return nDe(60 - m) + " vor " + nDe(s);
}
// L'HEURE OFFICIELLE (sur vingt-quatre heures : la gare, la radio, l'agenda) : « vierzehn Uhr dreißig », « ein Uhr fünf »
const offDe = (h, m) => (h === 1 ? "ein" : nDe(h)) + " Uhr" + (m ? " " + nDe(m) : "");
const MOMENTS_DE = h => h <= 4 ? "nachts" : h <= 9 ? "morgens" : h <= 11 ? "vormittags" : h <= 13 ? "mittags" : h <= 17 ? "nachmittags" : h <= 22 ? "abends" : "nachts";
// « um neun Uhr », « um halb fünf nachmittags » : le matin se passe de moment dans un agenda
const umDe = (h, m) => "um " + courDe(h, m) + (h >= 12 ? " " + MOMENTS_DE(h) : "");
// « von neun bis elf Uhr », « von halb zehn bis elf Uhr », « von drei bis fünf Uhr nachmittags »
function vonBisDe(h1, m1, h2, m2){
  const x = m1 === 0 ? nDe(h12(h1)) : courDe(h1, m1);
  return "von " + x + " bis " + courDe(h2, m2) + (h2 >= 12 ? " " + MOMENTS_DE(h2) : "");
}
// les ordinaux : der dritte Mai (nominatif), am dritten Mai (datif) ; -te jusqu'a 19, -ste a partir de 20
function ordDe(n, fin){
  const r = n === 1 ? "erst" : n === 3 ? "dritt" : n === 7 ? "siebt" : n === 8 ? "acht" : n < 20 ? nDe(n) + "t" : nDe(n) + "st";
  return r + fin;
}
// les formes FAUSSES qu'un apprenant fabrique (les leurres) : *dreite, *einte, *achtte
const ORD_FAUX_DE = {1: "eint", 3: "dreit", 8: "achtt"};
const evtDe = e => EVT.de[e];

const DE = {
  heure: p => "Es ist " + (p.style === "o" ? offDe(p.h, p.m) : courDe(p.h, p.m) + (p.style === "m" ? " " + M(MOMENTS_DE(p.h)) : "")) + ".",
  jour: p => "Heute ist " + JOURS.de[p.j] + ".",
  demain: p => "Heute ist " + JOURS.de[(p.j + 6) % 7] + ". Morgen ist " + M(JOURS.de[p.j]) + ".",
  hier: p => "Heute ist " + JOURS.de[(p.j + 1) % 7] + ". Gestern war " + M(JOURS.de[p.j]) + ".",
  moisApres: p => "Nach dem " + MOIS.de[(p.mo + 11) % 12] + " kommt der " + M(MOIS.de[p.mo]) + ".",
  moisAvant: p => "Vor dem " + MOIS.de[(p.mo + 1) % 12] + " kommt der " + M(MOIS.de[p.mo]) + ".",
  weekend: () => "Samstag und Sonntag sind " + M("das Wochenende") + ".",
  date: p => "Heute ist der " + M(ordDe(p.d, "e")) + " " + MOIS.de[p.mo] + ".",
  anniv: p => "Ich habe am " + M(ordDe(p.d, "en") + " " + MOIS.de[p.mo]) + " Geburtstag.",
  annivMois: p => "Ich habe " + M("im") + " " + MOIS.de[p.mo] + " Geburtstag.",
  agenda: p => maj(evtDe(p.e)) + " ist am " + JOURS.de[p.j] + " " + umDe(p.h, p.m) + ".",
  agendaRep: p => "Am " + JOURS.de[p.j] + " " + umDe(p.h, p.m) + ".",
  evtJour: p => maj(evtDe(p.e)) + " ist " + M("am") + " " + JOURS.de[p.j] + ".",
  evtDebut: p => maj(evtDe(p.e)) + " beginnt " + M("um") + umDe(p.h, p.m).slice(2) + ".",
  vonBis: p => maj(evtDe(p.e)) + " ist " + vonBisDe(p.h, p.m, p.h2, p.m2) + ".",
  vonBisRep: p => maj(vonBisDe(p.h, p.m, p.h2, p.m2)) + ".",
  duree: p => maj(evtDe(p.e)) + " dauert " + DUREE.de[p.min] + ".",
  dureeRep: p => maj(DUREE.de[p.min]) + ".",
  midi: () => M("Am") + " Mittag essen wir.",
  minuit: () => "Die Party endet " + M("um") + " Mitternacht.",
  finde: () => M("Am") + " Wochenende arbeite ich nicht.",
  midiPile: p => p.n ? "Es ist Mittag." : "Es ist Mitternacht."
};

// ---------------------------------------------------------------- l'espagnol
// « Es la una », « Son las dos » ; jusqu'a la demie, « y » (y cuarto, y media) ; apres, l'heure suivante « menos »
// (las tres menos cuarto) -- d'ou « Es la una menos cuarto » a 12 h 45.
function courEs(h, m){
  const a = h12(m > 30 ? suivante(h) : h);
  const tete = a === 1 ? "la una" : "las " + nEs(a);
  const verbe = a === 1 ? "Es" : "Son";
  let reste = "";
  if (m === 15) reste = " y cuarto";
  else if (m === 30) reste = " y media";
  else if (m === 45) reste = " menos cuarto";
  else if (m > 0 && m < 30) reste = " y " + nEs(m);
  else if (m > 30) reste = " menos " + nEs(60 - m);
  return {verbe, texte: tete + reste};
}
// l'heure officielle : « las catorce treinta », « las catorce cero cinco », « las catorce horas » ; « la una »
function offEs(h, m){
  const tete = h === 1 ? "la una" : "las " + nEsF(h);
  return {verbe: h === 1 ? "Es" : "Son", texte: tete + (m === 0 ? (h === 1 ? "" : " horas") : " " + (m < 10 ? "cero " : "") + nEs(m))};
}
const MOMENTS_ES = h => h === 0 ? "de la noche" : h <= 5 ? "de la madrugada" : h <= 11 ? "de la mañana" : h === 12 ? "del mediodía" : h <= 19 ? "de la tarde" : "de la noche";
// « a las nueve de la mañana », « a la una y media de la tarde »
const aEs = (h, m) => "a " + courEs(h, m).texte + " " + MOMENTS_ES(h);
// « de las nueve a las once », « de la una a las dos y media » (le moment une fois, a la fin)
const deAEs = (h1, m1, h2, m2) => "de " + courEs(h1, m1).texte + " a " + courEs(h2, m2).texte + " " + MOMENTS_ES(h2);
const ORD_ES = {2: "segundo", 3: "tercero", 4: "cuarto", 5: "quinto", 6: "sexto", 7: "séptimo", 8: "octavo", 9: "noveno", 10: "décimo"};
const ES = {
  // la lecture courante marque le verbe (es / son), le moment marque son nom (de la tarde)
  heure: p => { const x = p.style === "o" ? offEs(p.h, p.m) : courEs(p.h, p.m);
    return (p.style === "c" ? M(x.verbe) : x.verbe) + " " + x.texte + (p.style === "m" ? " " + MOMENTS_ES(p.h).replace(/(\S+)$/, M("$1")) : "") + "."; },
  jour: p => "Hoy es " + JOURS.es[p.j] + ".",
  demain: p => "Hoy es " + JOURS.es[(p.j + 6) % 7] + ". Mañana es " + M(JOURS.es[p.j]) + ".",
  hier: p => "Hoy es " + JOURS.es[(p.j + 1) % 7] + ". Ayer fue " + M(JOURS.es[p.j]) + ".",
  moisApres: p => "Después de " + MOIS.es[(p.mo + 11) % 12] + " viene " + M(MOIS.es[p.mo]) + ".",
  moisAvant: p => "Antes de " + MOIS.es[(p.mo + 1) % 12] + " viene " + M(MOIS.es[p.mo]) + ".",
  weekend: () => "El sábado y el domingo son " + M("el fin de semana") + ".",
  date: p => "Hoy es el " + M(nEs(p.d)) + " de " + MOIS.es[p.mo] + ".",
  anniv: p => "Mi cumpleaños es el " + M(nEs(p.d) + " de " + MOIS.es[p.mo]) + ".",
  annivMois: p => "Mi cumpleaños es " + M("en") + " " + MOIS.es[p.mo] + ".",
  agenda: p => maj(EVT.es[p.e]) + " es el " + JOURS.es[p.j] + " " + aEs(p.h, p.m) + ".",
  agendaRep: p => "El " + JOURS.es[p.j] + " " + aEs(p.h, p.m) + ".",
  evtJour: p => maj(EVT.es[p.e]) + " es " + M("el") + " " + JOURS.es[p.j] + ".",
  // « a las nueve », « a la una » : le trou prend « a las » ou « a la »
  evtDebut: p => maj(EVT.es[p.e]) + " empieza " + aEs(p.h, p.m).replace(/^a (las?) /, (x, art) => M("a " + art) + " ") + ".",
  vonBis: p => maj(EVT.es[p.e]) + " es " + deAEs(p.h, p.m, p.h2, p.m2) + ".",
  vonBisRep: p => maj(deAEs(p.h, p.m, p.h2, p.m2)) + ".",
  duree: p => maj(EVT.es[p.e]) + " dura " + DUREE.es[p.min] + ".",
  dureeRep: p => maj(DUREE.es[p.min]) + ".",
  midi: () => "Comemos " + M("a") + " mediodía.",
  minuit: () => "La fiesta termina " + M("a") + " medianoche.",
  finde: () => M("El") + " fin de semana no trabajo.",
  midiPile: p => p.n ? "Es mediodía." : "Es medianoche."
};

// ---------------------------------------------------------------- l'anglais (us : americain, gb : britannique)
// Deux facons de lire l'heure, qu'on n'oppose jamais dans une meme question : avec past / to (« half past two »,
// « quarter to seven » ; en americain « a quarter past ») et comme une montre numerique (« two thirty », « six
// forty-five », « six oh five ») -- la facon americaine de tous les jours. a.m. / p.m. : jamais d'heure sur 24 h ;
// 12 p.m. = midi, 12 a.m. = minuit.
function analogEn(v, h, m){
  const a = nEn(h12(h)), s = nEn(h12(suivante(h))), q = v === "us" ? "a quarter" : "quarter";
  if (m === 0) return a + " o'clock";
  if (m === 2) return "just after " + a;
  if (m === 58) return (v === "us" ? "almost " : "nearly ") + s;
  if (m === 15) return q + " past " + a;
  if (m === 30) return "half past " + a;
  if (m === 45) return q + " to " + s;
  if (m < 30) return nEn(m) + " past " + a;
  return nEn(60 - m) + " to " + s;
}
const digitalEn = (h, m, oclock) => nEn(h12(h)) + (m === 0 ? (oclock ? " o'clock" : "") : " " + (m < 10 ? "oh " + nEn(m) : nEn(m)));
// « two thirty p.m. », « nine a.m. » ; midi et minuit pile : noon, midnight
const ampmEn = (h, m) => (m === 0 && h === 12) ? "noon" : (m === 0 && h === 0) ? "midnight" : digitalEn(h, m, false) + (h < 12 ? " a.m." : " p.m.");
const MOMENTS_EN = h => h === 0 ? "at night" : h <= 11 ? "in the morning" : h <= 17 ? "in the afternoon" : h <= 21 ? "in the evening" : "at night";
const momentEn = (h, m) => (m === 0 && h === 12) ? "noon" : (m === 0 && h === 0) ? "midnight" : digitalEn(h, m, false) + " " + MOMENTS_EN(h);
// « from nine to eleven a.m. », « from eleven a.m. to one p.m. »
function fromToEn(h1, m1, h2, m2){
  const meme = (h1 < 12) === (h2 < 12);
  return "from " + (meme ? digitalEn(h1, m1, false) : ampmEn(h1, m1)) + " to " + ampmEn(h2, m2);
}
const ORD_EN = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
  "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"];
const ordEn = n => n <= 20 ? ORD_EN[n] : n === 30 ? "thirtieth" : EN_D[Math.floor(n / 10)] + "-" + ORD_EN[n % 10];
// l'ecrit : 1st, 2nd, 3rd, 4th, 11th, 12th, 13th, 21st, 22nd, 23rd, 31st
const ordEnEcrit = n => n + ((n % 100 >= 11 && n % 100 <= 13) ? "th" : ["th", "st", "nd", "rd"][n % 10] || "th");
const ORD_FAUX_EN = {1: "oneth", 2: "twoth", 3: "threeth", 5: "fiveth", 8: "eightth", 9: "nineth", 12: "twelveth"};
// la date dite : « May third » (americain) ; « the third of May » (britannique)
const dateEn = (v, d, mo) => v === "us" ? MOIS.en[mo] + " " + ordEn(d) : "the " + ordEn(d) + " of " + MOIS.en[mo];
function EN_(v){
  const ev = e => EVT[v][e];
  return {
    heure: p => "It's " + (p.style === "d" ? digitalEn(p.h, p.m, true) : p.style === "p" ? ampmEn(p.h, p.m)
      : p.style === "m" ? momentEn(p.h, p.m).replace(" " + MOMENTS_EN(p.h), " " + M(MOMENTS_EN(p.h))) : analogEn(v, p.h, p.m)) + ".",
    jour: p => "Today is " + JOURS.en[p.j] + ".",
    demain: p => "Today is " + JOURS.en[(p.j + 6) % 7] + ". Tomorrow is " + M(JOURS.en[p.j]) + ".",
    hier: p => "Today is " + JOURS.en[(p.j + 1) % 7] + ". Yesterday was " + M(JOURS.en[p.j]) + ".",
    moisApres: p => "After " + MOIS.en[(p.mo + 11) % 12] + " comes " + M(MOIS.en[p.mo]) + ".",
    moisAvant: p => "Before " + MOIS.en[(p.mo + 1) % 12] + " comes " + M(MOIS.en[p.mo]) + ".",
    weekend: () => "Saturday and Sunday are " + M("the weekend") + ".",
    // la date : le trou est l'ordinal (May ___ ; the ___ of May)
    date: p => "Today is " + (v === "us" ? MOIS.en[p.mo] + " " + M(ordEn(p.d)) : "the " + M(ordEn(p.d)) + " of " + MOIS.en[p.mo]) + ".",
    anniv: p => "My birthday is on " + M(dateEn(v, p.d, p.mo)) + ".",
    annivMois: p => "My birthday is " + M("in") + " " + MOIS.en[p.mo] + ".",
    agenda: p => maj(ev(p.e)) + " is on " + JOURS.en[p.j] + " at " + ampmEn(p.h, p.m) + ".",
    agendaRep: p => "On " + JOURS.en[p.j] + " at " + ampmEn(p.h, p.m) + ".",
    evtJour: p => maj(ev(p.e)) + " is " + M("on") + " " + JOURS.en[p.j] + ".",
    evtDebut: p => maj(ev(p.e)) + " starts " + M("at") + " " + ampmEn(p.h, p.m) + ".",
    vonBis: p => maj(ev(p.e)) + " is " + fromToEn(p.h, p.m, p.h2, p.m2) + ".",
    vonBisRep: p => maj(fromToEn(p.h, p.m, p.h2, p.m2)) + ".",
    duree: p => maj(ev(p.e)) + " lasts " + DUREE.en[p.min] + ".",
    dureeRep: p => maj(DUREE.en[p.min]) + ".",
    midi: () => "We have lunch " + M("at") + " noon.",
    minuit: () => "The party ends " + M("at") + " midnight.",
    finde: () => "I don't work " + M(v === "us" ? "on" : "at") + " the weekend.",
    midiPile: p => p.n ? "It's noon." : "It's midnight.",
    // les moments de la journee avec leur preposition (in the morning, at night)
    matin: () => "I work " + M("in") + " the morning.",
    aprem: () => "I go shopping " + M("in") + " the afternoon.",
    soir: () => "I read " + M("in") + " the evening.",
    nuit: () => "I sleep " + M("at") + " night."
  };
}
const US = EN_("us"), GB = EN_("gb");

// ---------------------------------------------------------------- les traductions
// le francais : en lettres. « deux heures et demie », « trois heures moins le quart », « midi et demi »
function heureFr(h, m){
  return h === 12 ? "midi" : h === 0 ? "minuit" : nFrF(h12(h)) + (h12(h) === 1 ? " heure" : " heures");
}
function courFr(h, m){
  const a = heureFr(h), s = heureFr(suivante(h)), demi = (h === 12 || h === 0) ? "demi" : "demie";
  if (m === 0) return a;
  if (m === 15) return a + " et quart";
  if (m === 30) return a + " et " + demi;
  if (m === 45) return s + " moins le quart";
  if (m < 30) return a + " " + nFr(m);
  return s + " moins " + nFr(60 - m);
}
const offFr = (h, m) => nFrF(h) + (h === 0 || h === 1 ? " heure" : " heures") + (m ? " " + nFr(m) : "");
// le moment : ni a midi ni a minuit (« midi et quart ») ; 1 h a 11 h « du matin »
const momFr = (h, m) => (h === 12 || h === 0 || (h === 11 && m > 30) || (h === 23 && m > 30)) ? "" : h <= 11 ? " du matin" : h <= 18 ? " de l'après-midi" : " du soir";
const hFr = (h, m) => h + " h" + (m ? " " + deux(m) : "");
const dateFr = (d, mo) => (d === 1 ? "1er" : d) + " " + MOIS.fr[mo];
const FR = {
  heure: p => "Il est " + (p.style === "o" ? offFr(p.h, p.m) : courFr(p.h, p.m) + (p.style === "m" ? momFr(p.h, p.m) : "")) + ".",
  jour: p => "Aujourd'hui, c'est " + JOURS.fr[p.j] + ".",
  demain: p => "Aujourd'hui, c'est " + JOURS.fr[(p.j + 6) % 7] + ". Demain, c'est " + JOURS.fr[p.j] + ".",
  hier: p => "Aujourd'hui, c'est " + JOURS.fr[(p.j + 1) % 7] + ". Hier, c'était " + JOURS.fr[p.j] + ".",
  moisApres: p => "Après " + MOIS.fr[(p.mo + 11) % 12] + " vient " + MOIS.fr[p.mo] + ".",
  moisAvant: p => "Avant " + MOIS.fr[(p.mo + 1) % 12] + " vient " + MOIS.fr[p.mo] + ".",
  weekend: () => "Samedi et dimanche, c'est le week-end.",
  date: p => "Aujourd'hui, nous sommes le " + dateFr(p.d, p.mo) + ".",
  anniv: p => "Mon anniversaire est le " + dateFr(p.d, p.mo) + ".",
  annivMois: p => "Mon anniversaire est en " + MOIS.fr[p.mo] + ".",
  agenda: p => maj(EVT.fr[p.e]) + " est " + JOURS.fr[p.j] + " à " + hFr(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS.fr[p.j]) + " à " + hFr(p.h, p.m) + ".",
  evtJour: p => maj(EVT.fr[p.e]) + " est " + JOURS.fr[p.j] + ".",
  evtDebut: p => maj(EVT.fr[p.e]) + " commence à " + hFr(p.h, p.m) + ".",
  vonBis: p => maj(EVT.fr[p.e]) + " a lieu de " + hFr(p.h, p.m) + " à " + hFr(p.h2, p.m2) + ".",
  vonBisRep: p => "De " + hFr(p.h, p.m) + " à " + hFr(p.h2, p.m2) + ".",
  duree: p => maj(EVT.fr[p.e]) + " dure " + DUREE.fr[p.min] + ".",
  dureeRep: p => maj(DUREE.fr[p.min]) + ".",
  midi: () => "Nous mangeons à midi.",
  minuit: () => "La fête se termine à minuit.",
  finde: () => "Le week-end, je ne travaille pas.",
  midiPile: p => p.n ? "Il est midi." : "Il est minuit.",
  matin: () => "Je travaille le matin.",
  aprem: () => "Je fais les courses l'après-midi.",
  soir: () => "Je lis le soir.",
  nuit: () => "Je dors la nuit."
};
// l'heure en chiffres : 12 h pour l'heure courante (« halb drei » : 2:30), 24 h pour l'officielle et avec un moment
const chiffres = (p, sep) => { const h = p.style === "c" || p.style === "d" ? h12(p.h) : p.h; return h + sep + deux(p.m); };
const FA_CHIFFRES = "۰۱۲۳۴۵۶۷۸۹";
const fa = s => String(s).replace(/[0-9]/g, c => FA_CHIFFRES[c]);
// le portugais du Bresil : « São 14h30 », « É 1h » ; « às 9h », « à 1h »
const hPt = (h, m) => h + "h" + (m ? deux(m) : "");
const PT = {
  heure: p => { const h = p.style === "c" || p.style === "d" ? h12(p.h) : p.h; return (h === 1 ? "É " : "São ") + hPt(h, p.m) + "."; },
  jour: p => "Hoje é " + JOURS.pt[p.j] + ".",
  demain: p => "Hoje é " + JOURS.pt[(p.j + 6) % 7] + ". Amanhã é " + JOURS.pt[p.j] + ".",
  hier: p => "Hoje é " + JOURS.pt[(p.j + 1) % 7] + ". Ontem foi " + JOURS.pt[p.j] + ".",
  moisApres: p => "Depois de " + MOIS.pt[(p.mo + 11) % 12] + " vem " + MOIS.pt[p.mo] + ".",
  moisAvant: p => "Antes de " + MOIS.pt[(p.mo + 1) % 12] + " vem " + MOIS.pt[p.mo] + ".",
  weekend: () => "Sábado e domingo são o fim de semana.",
  date: p => "Hoje é dia " + (p.d === 1 ? "1º" : p.d) + " de " + MOIS.pt[p.mo] + ".",
  anniv: p => "Meu aniversário é dia " + (p.d === 1 ? "1º" : p.d) + " de " + MOIS.pt[p.mo] + ".",
  annivMois: p => "Meu aniversário é em " + MOIS.pt[p.mo] + ".",
  agenda: p => maj(EVT.pt[p.e]) + " é " + JOURS_CAS.pt.sur[p.j] + (p.h === 1 ? " à " : " às ") + hPt(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS_CAS.pt.sur[p.j]) + (p.h === 1 ? " à " : " às ") + hPt(p.h, p.m) + ".",
  evtJour: p => maj(EVT.pt[p.e]) + " é " + JOURS_CAS.pt.sur[p.j] + ".",
  evtDebut: p => maj(EVT.pt[p.e]) + " começa" + (p.h === 1 ? " à " : " às ") + hPt(p.h, p.m) + ".",
  vonBis: p => maj(EVT.pt[p.e]) + " é das " + hPt(p.h, p.m) + " às " + hPt(p.h2, p.m2) + ".",
  vonBisRep: p => "Das " + hPt(p.h, p.m) + " às " + hPt(p.h2, p.m2) + ".",
  duree: p => maj(EVT.pt[p.e]) + " dura " + DUREE.pt[p.min] + ".",
  dureeRep: p => maj(DUREE.pt[p.min]) + ".",
  midi: () => "Almoçamos ao meio-dia.",
  minuit: () => "A festa termina à meia-noite.",
  finde: () => "No fim de semana, não trabalho.",
  midiPile: p => p.n ? "É meio-dia." : "É meia-noite."
};
// le turc : « 9.00'da » -- le suffixe suit le dernier nombre prononce (dokuz -> 'da, üç -> 'te, yirmi -> 'de)
const TR_UNITE = ["'da", "'de", "'de", "'te", "'te", "'te", "'da", "'de", "'de", "'da"];
const TR_DIZAINE = ["", "'da", "'de", "'da", "'ta", "'de"];
const trSuf = n => n === 0 ? "'da" : n % 10 ? TR_UNITE[n % 10] : TR_DIZAINE[n / 10];
const hTr = (h, m) => h + "." + deux(m);
const saatTr = (h, m) => "saat " + hTr(h, m) + trSuf(m || h);
const TRK = {
  heure: p => "Saat " + chiffres(p, ".") + ".",
  jour: p => "Bugün " + JOURS.tr[p.j] + ".",
  demain: p => "Bugün " + JOURS.tr[(p.j + 6) % 7] + ". Yarın " + JOURS.tr[p.j] + ".",
  hier: p => "Bugün " + JOURS.tr[(p.j + 1) % 7] + ". Dün " + JOURS_CAS.tr.passe[p.j] + ".",
  moisApres: p => maj(MOIS_CAS.tr.abl[(p.mo + 11) % 12]) + " sonra " + MOIS_CAS.tr.min[p.mo] + " gelir.",
  moisAvant: p => maj(MOIS_CAS.tr.abl[(p.mo + 1) % 12]) + " önce " + MOIS_CAS.tr.min[p.mo] + " gelir.",
  weekend: () => "Cumartesi ve pazar hafta sonudur.",
  date: p => "Bugün " + p.d + " " + MOIS.tr[p.mo] + ".",
  anniv: p => "Doğum günüm " + p.d + " " + MOIS.tr[p.mo] + MOIS_CAS.tr.locDate[p.mo] + ".",
  annivMois: p => "Doğum günüm " + MOIS_CAS.tr.loc[p.mo] + ".",
  agenda: p => maj(EVT.tr[p.e]) + " " + JOURS.tr[p.j] + " " + saatTr(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS.tr[p.j]) + " " + saatTr(p.h, p.m) + ".",
  evtJour: p => maj(EVT.tr[p.e]) + " " + JOURS.tr[p.j] + " günü.",
  evtDebut: p => maj(EVT.tr[p.e]) + " " + saatTr(p.h, p.m) + " başlıyor.",
  vonBis: p => maj(EVT.tr[p.e]) + " saat " + hTr(p.h, p.m) + " ile " + hTr(p.h2, p.m2) + " arasında.",
  vonBisRep: p => "Saat " + hTr(p.h, p.m) + " ile " + hTr(p.h2, p.m2) + " arası.",
  duree: p => maj(EVT.tr[p.e]) + " " + DUREE.tr[p.min] + " sürüyor.",
  dureeRep: p => maj(DUREE.tr[p.min]) + ".",
  midi: () => "Öğlen yemek yiyoruz.",
  minuit: () => "Parti gece yarısı bitiyor.",
  finde: () => "Hafta sonu çalışmıyorum.",
  midiPile: p => p.n ? "Şu an öğle vakti." : "Şu an gece yarısı."
};
// l'ukrainien, le russe, le polonais : le jour a l'accusatif apres la preposition, le mois au genitif dans une date
const hSl = (h, m) => h + ":" + deux(m);
const UK = {
  heure: p => "Зараз " + chiffres(p, ":") + ".",
  jour: p => "Сьогодні " + JOURS.uk[p.j] + ".",
  demain: p => "Сьогодні " + JOURS.uk[(p.j + 6) % 7] + ". Завтра " + JOURS.uk[p.j] + ".",
  hier: p => "Сьогодні " + JOURS.uk[(p.j + 1) % 7] + ". Учора " + JOURS_CAS.uk.etait[JOURS_CAS.uk.g[p.j]] + " " + JOURS.uk[p.j] + ".",
  moisApres: p => "Після " + MOIS_CAS.uk.gen[(p.mo + 11) % 12] + " йде " + MOIS_CAS.uk.nom[p.mo] + ".",
  moisAvant: p => "Перед " + MOIS_CAS.uk.ins[(p.mo + 1) % 12] + " іде " + MOIS_CAS.uk.nom[p.mo] + ".",
  weekend: () => "Субота й неділя — це вихідні.",
  date: p => "Сьогодні " + p.d + " " + MOIS_CAS.uk.gen[p.mo] + ".",
  anniv: p => "Мій день народження — " + p.d + " " + MOIS_CAS.uk.gen[p.mo] + ".",
  annivMois: p => "Мій день народження в " + MOIS_CAS.uk.loc[p.mo] + ".",
  agenda: p => maj(EVT.uk[p.e]) + " — " + JOURS_CAS.uk.acc[p.j] + " о " + hSl(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS_CAS.uk.acc[p.j]) + " о " + hSl(p.h, p.m) + ".",
  evtJour: p => maj(EVT.uk[p.e]) + " — " + JOURS_CAS.uk.acc[p.j] + ".",
  evtDebut: p => maj(EVT.uk[p.e]) + " починається о " + hSl(p.h, p.m) + ".",
  vonBis: p => maj(EVT.uk[p.e]) + " — з " + hSl(p.h, p.m) + " до " + hSl(p.h2, p.m2) + ".",
  vonBisRep: p => "З " + hSl(p.h, p.m) + " до " + hSl(p.h2, p.m2) + ".",
  duree: p => maj(EVT.uk[p.e]) + " триває " + DUREE.uk[p.min] + ".",
  dureeRep: p => maj(DUREE.uk[p.min]) + ".",
  midi: () => "Опівдні ми обідаємо.",
  minuit: () => "Вечірка закінчується опівночі.",
  finde: () => "На вихідних я не працюю.",
  midiPile: p => p.n ? "Зараз полудень." : "Зараз північ."
};
const RU = {
  heure: p => "Сейчас " + chiffres(p, ":") + ".",
  jour: p => "Сегодня " + JOURS.ru[p.j] + ".",
  demain: p => "Сегодня " + JOURS.ru[(p.j + 6) % 7] + ". Завтра " + JOURS.ru[p.j] + ".",
  hier: p => "Сегодня " + JOURS.ru[(p.j + 1) % 7] + ". Вчера " + JOURS_CAS.ru.etait[JOURS_CAS.ru.g[p.j]] + " " + JOURS.ru[p.j] + ".",
  moisApres: p => "После " + MOIS_CAS.ru.gen[(p.mo + 11) % 12] + " идёт " + MOIS_CAS.ru.nom[p.mo] + ".",
  moisAvant: p => "Перед " + MOIS_CAS.ru.ins[(p.mo + 1) % 12] + " идёт " + MOIS_CAS.ru.nom[p.mo] + ".",
  weekend: () => "Суббота и воскресенье — это выходные.",
  date: p => "Сегодня " + p.d + " " + MOIS_CAS.ru.gen[p.mo] + ".",
  anniv: p => "Мой день рождения — " + p.d + " " + MOIS_CAS.ru.gen[p.mo] + ".",
  annivMois: p => "Мой день рождения в " + MOIS_CAS.ru.loc[p.mo] + ".",
  agenda: p => maj(EVT.ru[p.e]) + " — " + JOURS_CAS.ru.acc[p.j] + " в " + hSl(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS_CAS.ru.acc[p.j]) + " в " + hSl(p.h, p.m) + ".",
  evtJour: p => maj(EVT.ru[p.e]) + " — " + JOURS_CAS.ru.acc[p.j] + ".",
  evtDebut: p => maj(EVT.ru[p.e]) + " начинается в " + hSl(p.h, p.m) + ".",
  vonBis: p => maj(EVT.ru[p.e]) + " — с " + hSl(p.h, p.m) + " до " + hSl(p.h2, p.m2) + ".",
  vonBisRep: p => "С " + hSl(p.h, p.m) + " до " + hSl(p.h2, p.m2) + ".",
  duree: p => maj(EVT.ru[p.e]) + " длится " + DUREE.ru[p.min] + ".",
  dureeRep: p => maj(DUREE.ru[p.min]) + ".",
  midi: () => "В полдень мы обедаем.",
  minuit: () => "Вечеринка заканчивается в полночь.",
  finde: () => "В выходные я не работаю.",
  midiPile: p => p.n ? "Сейчас полдень." : "Сейчас полночь."
};
const PL = {
  heure: p => "Jest " + chiffres(p, ":") + ".",
  jour: p => "Dzisiaj jest " + JOURS.pl[p.j] + ".",
  demain: p => "Dzisiaj jest " + JOURS.pl[(p.j + 6) % 7] + ". Jutro jest " + JOURS.pl[p.j] + ".",
  hier: p => "Dzisiaj jest " + JOURS.pl[(p.j + 1) % 7] + ". Wczoraj " + JOURS_CAS.pl.etait[JOURS_CAS.pl.g[p.j]] + " " + JOURS.pl[p.j] + ".",
  moisApres: p => "Po " + MOIS_CAS.pl.loc[(p.mo + 11) % 12] + " jest " + MOIS_CAS.pl.nom[p.mo] + ".",
  moisAvant: p => "Przed " + MOIS_CAS.pl.ins[(p.mo + 1) % 12] + " jest " + MOIS_CAS.pl.nom[p.mo] + ".",
  weekend: () => "Sobota i niedziela to weekend.",
  date: p => "Dzisiaj jest " + p.d + " " + MOIS_CAS.pl.gen[p.mo] + ".",
  anniv: p => "Moje urodziny są " + p.d + " " + MOIS_CAS.pl.gen[p.mo] + ".",
  annivMois: p => "Moje urodziny są " + (p.mo === 8 ? "we " : "w ") + MOIS_CAS.pl.loc[p.mo] + ".",
  agenda: p => maj(EVT.pl[p.e]) + " jest " + JOURS_CAS.pl.acc[p.j] + " o " + hSl(p.h, p.m) + ".",
  agendaRep: p => maj(JOURS_CAS.pl.acc[p.j]) + " o " + hSl(p.h, p.m) + ".",
  evtJour: p => maj(EVT.pl[p.e]) + " jest " + JOURS_CAS.pl.acc[p.j] + ".",
  evtDebut: p => maj(EVT.pl[p.e]) + " zaczyna się o " + hSl(p.h, p.m) + ".",
  vonBis: p => maj(EVT.pl[p.e]) + " jest od " + hSl(p.h, p.m) + " do " + hSl(p.h2, p.m2) + ".",
  vonBisRep: p => "Od " + hSl(p.h, p.m) + " do " + hSl(p.h2, p.m2) + ".",
  duree: p => maj(EVT.pl[p.e]) + " trwa " + DUREE.pl[p.min] + ".",
  dureeRep: p => maj(DUREE.pl[p.min]) + ".",
  midi: () => "W południe jemy obiad.",
  minuit: () => "Impreza kończy się o północy.",
  finde: () => "W weekend nie pracuję.",
  midiPile: p => p.n ? "Jest południe." : "Jest północ."
};
// le persan : les chiffres persans ; l'arabe : les chiffres latins, comme le reste des themes
const FA = {
  heure: p => "ساعت " + fa(chiffres(p, ":")) + " است.",
  jour: p => "امروز " + JOURS.fa[p.j] + " است.",
  demain: p => "امروز " + JOURS.fa[(p.j + 6) % 7] + " است. فردا " + JOURS.fa[p.j] + " است.",
  hier: p => "امروز " + JOURS.fa[(p.j + 1) % 7] + " است. دیروز " + JOURS.fa[p.j] + " بود.",
  moisApres: p => "بعد از " + MOIS.fa[(p.mo + 11) % 12] + "، " + MOIS.fa[p.mo] + " می‌آید.",
  moisAvant: p => "قبل از " + MOIS.fa[(p.mo + 1) % 12] + "، " + MOIS.fa[p.mo] + " می‌آید.",
  weekend: () => "شنبه و یکشنبه تعطیلات آخر هفته‌اند.",
  date: p => "امروز " + fa(p.d) + " " + MOIS.fa[p.mo] + " است.",
  anniv: p => "تولد من " + fa(p.d) + " " + MOIS.fa[p.mo] + " است.",
  annivMois: p => "تولد من در ماه " + MOIS.fa[p.mo] + " است.",
  agenda: p => EVT.fa[p.e] + " " + JOURS.fa[p.j] + " ساعت " + fa(hSl(p.h, p.m)) + " است.",
  agendaRep: p => JOURS.fa[p.j] + " ساعت " + fa(hSl(p.h, p.m)) + ".",
  evtJour: p => EVT.fa[p.e] + " " + JOURS.fa[p.j] + " است.",
  evtDebut: p => EVT.fa[p.e] + " ساعت " + fa(hSl(p.h, p.m)) + " شروع می‌شود.",
  vonBis: p => EVT.fa[p.e] + " از ساعت " + fa(hSl(p.h, p.m)) + " تا " + fa(hSl(p.h2, p.m2)) + " است.",
  vonBisRep: p => "از ساعت " + fa(hSl(p.h, p.m)) + " تا " + fa(hSl(p.h2, p.m2)) + ".",
  duree: p => EVT.fa[p.e] + " " + DUREE.fa[p.min] + " طول می‌کشد.",
  dureeRep: p => DUREE.fa[p.min] + ".",
  midi: () => "ظهر ناهار می‌خوریم.",
  minuit: () => "مهمانی نیمه‌شب تمام می‌شود.",
  finde: () => "آخر هفته کار نمی‌کنم.",
  midiPile: p => p.n ? "ظهر است." : "نیمه‌شب است."
};
const AR = {
  heure: p => "الساعة " + chiffres(p, ":") + ".",
  jour: p => "اليوم " + JOURS.ar[p.j] + ".",
  demain: p => "اليوم " + JOURS.ar[(p.j + 6) % 7] + ". غدًا " + JOURS.ar[p.j] + ".",
  hier: p => "اليوم " + JOURS.ar[(p.j + 1) % 7] + ". أمس كان " + JOURS.ar[p.j] + ".",
  moisApres: p => "بعد " + MOIS.ar[(p.mo + 11) % 12] + " يأتي " + MOIS.ar[p.mo] + ".",
  moisAvant: p => "قبل " + MOIS.ar[(p.mo + 1) % 12] + " يأتي " + MOIS.ar[p.mo] + ".",
  weekend: () => "السبت والأحد هما عطلة نهاية الأسبوع.",
  date: p => "اليوم " + p.d + " " + MOIS.ar[p.mo] + ".",
  anniv: p => "عيد ميلادي في " + p.d + " " + MOIS.ar[p.mo] + ".",
  annivMois: p => "عيد ميلادي في شهر " + MOIS.ar[p.mo] + ".",
  agenda: p => EVT.ar[p.e] + " يوم " + JOURS.ar[p.j] + " الساعة " + hSl(p.h, p.m) + ".",
  agendaRep: p => "يوم " + JOURS.ar[p.j] + " الساعة " + hSl(p.h, p.m) + ".",
  evtJour: p => EVT.ar[p.e] + " يوم " + JOURS.ar[p.j] + ".",
  evtDebut: p => (EVT_F_AR[p.e] ? "تبدأ " : "يبدأ ") + EVT.ar[p.e] + " الساعة " + hSl(p.h, p.m) + ".",
  vonBis: p => EVT.ar[p.e] + " من الساعة " + hSl(p.h, p.m) + " إلى الساعة " + hSl(p.h2, p.m2) + ".",
  vonBisRep: p => "من الساعة " + hSl(p.h, p.m) + " إلى الساعة " + hSl(p.h2, p.m2) + ".",
  duree: p => (EVT_F_AR[p.e] ? "تستغرق " : "يستغرق ") + EVT.ar[p.e] + " " + DUREE.ar[p.min] + ".",
  dureeRep: p => DUREE.ar[p.min] + ".",
  midi: () => "نتناول الغداء ظهرًا.",
  minuit: () => "تنتهي الحفلة عند منتصف الليل.",
  finde: () => "لا أعمل في عطلة نهاية الأسبوع.",
  midiPile: p => p.n ? "إنه الظهر." : "إنه منتصف الليل."
};

// ---------------------------------------------------------------- l'acces
const APPRISES = {de: DE, es: ES, us: US, gb: GB};
// les traductions : l'anglais d'interface est le britannique de la page (« half past two ») ; l'allemand d'interface
// (pour qui apprend l'espagnol) est l'allemand de la page
const TRADS = {fr: FR, en: GB, de: DE, pt: PT, tr: TRK, uk: UK, ru: RU, pl: PL, fa: FA, ar: AR};
// « two thirty p.m. » finit deja sur un point : pas de second
const point = s => s.replace(/\.\.$/, ".");
const sansMarque = s => s.replace(/[⟦⟧]/g, "");
const Dire = {
  // la phrase dans la langue apprise : Dire.phrase("de", "heure", {h: 14, m: 30, style: "c"}) -> « Es ist halb drei. »
  phrase(L, sorte, p){ return point(sansMarque(APPRISES[L][sorte](p || {}))); },
  // la meme phrase avec un trou : {texte: « Heute ist der ___ Mai. », rep: « dritte »} ; null sans marque
  trou(L, sorte, p){
    const s = point(APPRISES[L][sorte](p || {})), x = s.match(/⟦([^⟧]*)⟧/);
    return x ? {texte: sansMarque(s.replace(x[0], "___")), rep: x[1]} : null;
  },
  // sa traduction dans la langue d'interface, ou null (une sorte propre a une langue apprise, une langue absente)
  trad(lg, sorte, p){ const t = TRADS[lg]; return t && t[sorte] ? point(t[sorte](p || {})) : null; },
  // les morceaux, pour les questions a trou et les leurres
  courDe, offDe, courEs, offEs, analogEn, digitalEn, ampmEn, momentEn, courFr, offFr,
  MOMENTS_DE, MOMENTS_ES, MOMENTS_EN, umDe, aEs, ordDe, ORD_FAUX_DE, ORD_ES, ordEn, ordEnEcrit, ORD_FAUX_EN, dateEn,
  nDe, nEs, nEsF, nEn, nFr, h12, deux, fa,
  JOURS, JOURS_COURTS, MOIS, EVTS, EVT, EVT_COURT, DUREES, DUREE,
  // le jour de la semaine d'une date (0 = lundi)
  jourSemaine(an, mo, d){ return (new Date(Date.UTC(an, mo, d)).getUTCDay() + 6) % 7; },
  joursDuMois(an, mo){ return new Date(Date.UTC(an, mo + 1, 0)).getUTCDate(); }
};
if (typeof module !== "undefined" && module.exports) module.exports = Dire; else racine.Dire = Dire;
})(typeof window !== "undefined" ? window : this);
