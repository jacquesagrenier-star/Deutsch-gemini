// LE BANC DE « L'HEURE ET LES DATES », hors navigateur (16 nov. 2026).
//
//     node tests/heure_banc.js           # les controles, et visuel/heure/banc.txt (les cas pieges, a relire)
//     node tests/heure_banc.js --tout    # en plus, toutes les heures et toutes les dates a l'ecran
//
// Il fait dire par visuel/prototype/heure/dire.js (le code meme de la page) :
//   - toutes les heures de 0:00 a 23:55 par pas de cinq minutes, plus « kurz nach / kurz vor » (h:02, h:58), dans
//     chaque langue apprise (de, es, us, gb) et chaque facon de lire (courante, officielle, avec le moment ; en
//     anglais : past / to, numerique, a.m. / p.m.) ;
//   - toutes les dates de 2027, plus le 29 fevrier 2028 ;
//   - leurs traductions dans les dix langues d'interface des pages.
// Il verifie : aucun « undefined », « NaN », chiffre (les nombres en lettres, regle des voix du 28 oct.), double
// espace ou double point dans une phrase apprise ; deux heures differentes ne se disent jamais pareil ; et les cas
// pieges ecrits a la main plus bas (halb drei, Viertel vor, es la una, 12 a.m. / p.m., le 1er, le 31).
"use strict";
const fs = require("fs"), path = require("path");
const RACINE = path.dirname(__dirname);
const Dire = require(path.join(RACINE, "visuel", "prototype", "heure", "dire.js"));
const TOUT = process.argv.includes("--tout");
const fautes = [];
const APPRISES = ["de", "es", "us", "gb"];
const STYLES = {de: ["c", "o", "m"], es: ["c", "o", "m"], us: ["c", "d", "p", "m"], gb: ["c", "d", "p", "m"]};
const UI = ["fr", "en", "de", "pt", "tr", "uk", "ru", "pl", "fa", "ar"];
const MINUTES = [];
for (let m = 0; m < 60; m += 5) MINUTES.push(m);
MINUTES.push(2, 58);
const HEURES = [];
for (let h = 0; h < 24; h++) for (const m of MINUTES) HEURES.push([h, m]);

function propre(t, ou, chiffresPermis){
  if (typeof t !== "string" || !t) { fautes.push(ou + " : vide"); return; }
  if (/undefined|NaN|\bnull\b(?! Uhr)/.test(t)) fautes.push(ou + " : « " + t + " »");
  if (/ {2}|\s[.,]|\.\.$/.test(t)) fautes.push(ou + " : espacement ou point « " + t + " »");
  if (!chiffresPermis && /[0-9]/.test(t)) fautes.push(ou + " : un chiffre dans une phrase dite « " + t + " »");
}
const lignes = [];
// 1. LES HEURES
for (const L of APPRISES){
  for (const st of STYLES[L]){
    const vu = new Map();
    for (const [h, m] of HEURES){
      const t = Dire.phrase(L, "heure", {h, m, style: st});
      propre(t, L + " " + st + " " + h + ":" + Dire.deux(m), false);
      // deux heures differentes ne se disent jamais pareil : sur douze heures pour la lecture courante et numerique,
      // sur vingt-quatre pour l'officielle, a.m. / p.m. et le moment
      const cle = (st === "c" || st === "d") ? (h % 12) + ":" + m : h + ":" + m;
      if (vu.has(t) && vu.get(t) !== cle) fautes.push(L + " " + st + " : « " + t + " » pour " + vu.get(t) + " et " + cle);
      vu.set(t, cle);
      if (TOUT) lignes.push(L + " " + st + " " + h + ":" + Dire.deux(m) + "  " + t);
    }
  }
}
// leurs traductions
for (const lg of UI) for (const [h, m] of HEURES) for (const st of ["c", "o", "m"]) {
  const t = Dire.trad(lg, "heure", {h, m, style: st});
  propre(t, "trad " + lg + " " + st + " " + h + ":" + m, lg !== "fr" && lg !== "en" && lg !== "de");
}
// 2. LES DATES : toute l'annee 2027, et le 29 fevrier 2028
const DATES = [];
for (let mo = 0; mo < 12; mo++) for (let d = 1; d <= Dire.joursDuMois(2027, mo); d++) DATES.push([2027, mo, d]);
DATES.push([2028, 1, 29]);
if (Dire.joursDuMois(2027, 1) !== 28 || Dire.joursDuMois(2028, 1) !== 29) fautes.push("fevrier : 28 jours en 2027, 29 en 2028");
const SORTES_DATE = ["date", "anniv", "annivMois", "jour", "demain", "hier", "moisApres", "moisAvant"];
for (const [an, mo, d] of DATES){
  const j = Dire.jourSemaine(an, mo, d), p = {d, mo, j};
  for (const L of APPRISES) for (const s of SORTES_DATE) {
    const t = Dire.phrase(L, s, p);
    propre(t, L + " " + s + " " + an + "-" + (mo + 1) + "-" + d, false);
    if (TOUT && (s === "date" || s === "anniv")) lignes.push(L + " " + an + "-" + Dire.deux(mo + 1) + "-" + Dire.deux(d) + "  " + t);
  }
  for (const lg of UI) for (const s of SORTES_DATE) propre(Dire.trad(lg, s, p), "trad " + lg + " " + s + " " + (mo + 1) + "-" + d, true);
}
// 3. L'AGENDA : chaque rendez-vous, chaque jour, des heures de 8 h a 21 h 30, chaque duree
const SORTES_AGENDA = ["agenda", "agendaRep", "evtJour", "evtDebut", "vonBis", "vonBisRep", "duree", "dureeRep"];
for (const e of Dire.EVTS) for (let j = 0; j < 7; j++) for (let h = 8; h <= 21; h++) for (const m of [0, 15, 30, 45]) for (const min of Dire.DUREES) {
  const fin = h * 60 + m + min; if (fin >= 24 * 60) continue;
  const p = {e, j, h, m, h2: Math.floor(fin / 60), m2: fin % 60, min};
  for (const L of APPRISES) for (const s of SORTES_AGENDA) propre(Dire.phrase(L, s, p), L + " " + s + " " + JSON.stringify(p), false);
  for (const lg of UI) for (const s of SORTES_AGENDA) propre(Dire.trad(lg, s, p), "trad " + lg + " " + s + " " + JSON.stringify(p), true);
}
for (const L of APPRISES) for (const s of ["weekend", "midi", "minuit", "finde"]) propre(Dire.phrase(L, s, {}), L + " " + s, false);
for (const n of [0, 1]) { for (const L of APPRISES) propre(Dire.phrase(L, "midiPile", {n}), L + " midiPile", false); for (const lg of UI) propre(Dire.trad(lg, "midiPile", {n}), "trad " + lg + " midiPile", true); }

// 4. LES CAS PIEGES, ecrits a la main : la phrase attendue, mot pour mot
const H = (L, h, m, style) => Dire.phrase(L, "heure", {h, m, style});
const T = (lg, h, m, style) => Dire.trad(lg, "heure", {h, m, style});
const A = [
  // l'allemand : halb drei = 2 h 30 (le piege du francophone) ; Viertel ; « ein Uhr » mais « halb eins » ; l'officielle
  ["halb drei, a 2 h 30", H("de", 2, 30, "c"), "Es ist halb drei."],
  ["halb drei, a 14 h 30", H("de", 14, 30, "c"), "Es ist halb drei."],
  ["halb eins, a 0 h 30", H("de", 0, 30, "c"), "Es ist halb eins."],
  ["halb eins, a 12 h 30", H("de", 12, 30, "c"), "Es ist halb eins."],
  ["Viertel nach", H("de", 2, 15, "c"), "Es ist Viertel nach zwei."],
  ["Viertel vor", H("de", 2, 45, "c"), "Es ist Viertel vor drei."],
  ["Viertel vor eins", H("de", 12, 45, "c"), "Es ist Viertel vor eins."],
  ["fünf vor halb", H("de", 2, 25, "c"), "Es ist fünf vor halb drei."],
  ["fünf nach halb", H("de", 2, 35, "c"), "Es ist fünf nach halb drei."],
  ["zwanzig vor", H("de", 2, 40, "c"), "Es ist zwanzig vor drei."],
  ["kurz vor", H("de", 2, 58, "c"), "Es ist kurz vor drei."],
  ["kurz nach", H("de", 3, 2, "c"), "Es ist kurz nach drei."],
  ["ein Uhr", H("de", 1, 0, "c"), "Es ist ein Uhr."],
  ["zwölf Uhr a minuit", H("de", 0, 0, "c"), "Es ist zwölf Uhr."],
  ["officielle 14:30", H("de", 14, 30, "o"), "Es ist vierzehn Uhr dreißig."],
  ["officielle 1:05", H("de", 1, 5, "o"), "Es ist ein Uhr fünf."],
  ["officielle 21:00", H("de", 21, 0, "o"), "Es ist einundzwanzig Uhr."],
  ["officielle 0:00", H("de", 0, 0, "o"), "Es ist null Uhr."],
  ["officielle 23:45", H("de", 23, 45, "o"), "Es ist dreiundzwanzig Uhr fünfundvierzig."],
  ["le moment, 19 h", H("de", 19, 0, "m"), "Es ist sieben Uhr abends."],
  ["le moment, 7 h", H("de", 7, 0, "m"), "Es ist sieben Uhr morgens."],
  // l'espagnol : es la una / son las ; menos ; la una menos cuarto a 12 h 45 ; l'officielle au feminin
  ["es la una", H("es", 1, 0, "c"), "Es la una."],
  ["es la una y cuarto, 13 h 15", H("es", 13, 15, "c"), "Es la una y cuarto."],
  ["es la una menos cuarto, 12 h 45", H("es", 12, 45, "c"), "Es la una menos cuarto."],
  ["es la una menos cuarto, 0 h 45", H("es", 0, 45, "c"), "Es la una menos cuarto."],
  ["son las dos y media", H("es", 2, 30, "c"), "Son las dos y media."],
  ["menos cuarto", H("es", 2, 45, "c"), "Son las tres menos cuarto."],
  ["menos veinticinco", H("es", 2, 35, "c"), "Son las tres menos veinticinco."],
  ["las doce a minuit", H("es", 0, 0, "c"), "Son las doce."],
  ["officielle 21:30, au feminin", H("es", 21, 30, "o"), "Son las veintiuna treinta."],
  ["officielle 14:05", H("es", 14, 5, "o"), "Son las catorce cero cinco."],
  ["de la tarde", H("es", 14, 30, "m"), "Son las dos y media de la tarde."],
  ["de la mañana", H("es", 9, 0, "m"), "Son las nueve de la mañana."],
  ["del mediodía", H("es", 12, 0, "m"), "Son las doce del mediodía."],
  ["de la noche, minuit", H("es", 0, 0, "m"), "Son las doce de la noche."],
  ["a las / a la", Dire.aEs(13, 30), "a la una y media de la tarde"],
  // l'anglais : 12 a.m. = minuit, 12 p.m. = midi ; six forty-five ; oh five ; a quarter (americain) / quarter (britannique)
  ["12:30 = twelve thirty p.m.", H("us", 12, 30, "p"), "It's twelve thirty p.m."],
  ["0:30 = twelve thirty a.m.", H("us", 0, 30, "p"), "It's twelve thirty a.m."],
  ["12:00 = noon", H("us", 12, 0, "p"), "It's noon."],
  ["0:00 = midnight", H("gb", 0, 0, "p"), "It's midnight."],
  ["14:30 = two thirty p.m.", H("us", 14, 30, "p"), "It's two thirty p.m."],
  ["6:45 numerique", H("us", 6, 45, "d"), "It's six forty-five."],
  ["6:05 numerique", H("us", 6, 5, "d"), "It's six oh five."],
  ["3:00 numerique", H("gb", 3, 0, "d"), "It's three o'clock."],
  ["a quarter to (us)", H("us", 6, 45, "c"), "It's a quarter to seven."],
  ["quarter to (gb)", H("gb", 6, 45, "c"), "It's quarter to seven."],
  ["half past", H("gb", 2, 30, "c"), "It's half past two."],
  ["twenty-five past", H("gb", 2, 25, "c"), "It's twenty-five past two."],
  ["almost (us)", H("us", 2, 58, "c"), "It's almost three."],
  ["nearly (gb)", H("gb", 2, 58, "c"), "It's nearly three."],
  // les dates
  ["der erste Mai", Dire.phrase("de", "date", {d: 1, mo: 4}), "Heute ist der erste Mai."],
  ["der dritte Mai", Dire.phrase("de", "date", {d: 3, mo: 4}), "Heute ist der dritte Mai."],
  ["der siebte", Dire.phrase("de", "date", {d: 7, mo: 6}), "Heute ist der siebte Juli."],
  ["der achte", Dire.phrase("de", "date", {d: 8, mo: 2}), "Heute ist der achte März."],
  ["der zwanzigste (-ste)", Dire.phrase("de", "date", {d: 20, mo: 0}), "Heute ist der zwanzigste Januar."],
  ["der einunddreißigste", Dire.phrase("de", "date", {d: 31, mo: 11}), "Heute ist der einunddreißigste Dezember."],
  ["am dritten Mai (datif)", Dire.phrase("de", "anniv", {d: 3, mo: 4}), "Ich habe am dritten Mai Geburtstag."],
  ["am ersten", Dire.phrase("de", "anniv", {d: 1, mo: 0}), "Ich habe am ersten Januar Geburtstag."],
  ["el uno de mayo", Dire.phrase("es", "date", {d: 1, mo: 4}), "Hoy es el uno de mayo."],
  ["el tres de mayo", Dire.phrase("es", "date", {d: 3, mo: 4}), "Hoy es el tres de mayo."],
  ["el treinta y uno", Dire.phrase("es", "date", {d: 31, mo: 11}), "Hoy es el treinta y uno de diciembre."],
  ["el veintiuno", Dire.phrase("es", "anniv", {d: 21, mo: 2}), "Mi cumpleaños es el veintiuno de marzo."],
  ["May first", Dire.phrase("us", "date", {d: 1, mo: 4}), "Today is May first."],
  ["May third", Dire.phrase("us", "date", {d: 3, mo: 4}), "Today is May third."],
  ["the third of May", Dire.phrase("gb", "date", {d: 3, mo: 4}), "Today is the third of May."],
  ["thirty-first", Dire.phrase("us", "anniv", {d: 31, mo: 11}), "My birthday is on December thirty-first."],
  ["twenty-second", Dire.ordEn(22), "twenty-second"],
  ["thirtieth", Dire.ordEn(30), "thirtieth"],
  ["1st", Dire.ordEnEcrit(1), "1st"], ["2nd", Dire.ordEnEcrit(2), "2nd"], ["3rd", Dire.ordEnEcrit(3), "3rd"],
  ["11th", Dire.ordEnEcrit(11), "11th"], ["12th", Dire.ordEnEcrit(12), "12th"], ["13th", Dire.ordEnEcrit(13), "13th"],
  ["21st", Dire.ordEnEcrit(21), "21st"], ["22nd", Dire.ordEnEcrit(22), "22nd"], ["23rd", Dire.ordEnEcrit(23), "23rd"], ["31st", Dire.ordEnEcrit(31), "31st"],
  // les jours : le 16 nov. 2026 est un lundi, le 1er janv. 2027 un vendredi
  ["16 nov. 2026, lundi", Dire.jourSemaine(2026, 10, 16), 0],
  ["1er janv. 2027, vendredi", Dire.jourSemaine(2027, 0, 1), 4],
  ["29 fevr. 2028, mardi", Dire.jourSemaine(2028, 1, 29), 1],
  // l'agenda
  ["um halb fünf nachmittags", Dire.phrase("de", "agenda", {e: "fussball", j: 2, h: 16, m: 30}), "Das Fußballtraining ist am Mittwoch um halb fünf nachmittags."],
  ["el jueves a las diez", Dire.phrase("es", "agenda", {e: "arzt", j: 3, h: 10, m: 0}), "La cita con el médico es el jueves a las diez de la mañana."],
  ["on Saturday at eight p.m.", Dire.phrase("us", "agenda", {e: "party", j: 5, h: 20, m: 0}), "The party is on Saturday at eight p.m."],
  ["von neun bis halb elf", Dire.phrase("de", "vonBisRep", {h: 9, m: 0, h2: 10, m2: 30}), "Von neun bis halb elf."],
  ["de la una a las dos", Dire.phrase("es", "vonBisRep", {h: 13, m: 0, h2: 14, m2: 0}), "De la una a las dos de la tarde."],
  ["from eleven a.m. to one p.m.", Dire.phrase("gb", "vonBisRep", {h: 11, m: 0, h2: 13, m2: 0}), "From eleven a.m. to one p.m."],
  // les traductions
  ["fr : deux heures et demie", T("fr", 14, 30, "c"), "Il est deux heures et demie."],
  ["fr : midi et quart", T("fr", 12, 15, "c"), "Il est midi et quart."],
  ["fr : minuit et demi", T("fr", 0, 30, "c"), "Il est minuit et demi."],
  ["fr : trois heures moins le quart", T("fr", 14, 45, "c"), "Il est trois heures moins le quart."],
  ["fr : vingt et une heures", T("fr", 21, 0, "o"), "Il est vingt et une heures."],
  ["fr : une heure du matin", T("fr", 1, 0, "m"), "Il est une heure du matin."],
  ["fr : le 1er mai", Dire.trad("fr", "date", {d: 1, mo: 4}), "Aujourd'hui, nous sommes le 1er mai."],
  ["en : half past two", T("en", 14, 30, "c"), "It's half past two."],
  ["de : halb drei", Dire.trad("de", "heure", {h: 14, m: 30, style: "c"}), "Es ist halb drei."],
  ["ru : во вторник", Dire.trad("ru", "agendaRep", {j: 1, h: 9, m: 0}), "Во вторник в 9:00."],
  ["pl : we wtorek", Dire.trad("pl", "agendaRep", {j: 1, h: 9, m: 0}), "We wtorek o 9:00."],
  ["uk : у середу", Dire.trad("uk", "agendaRep", {j: 2, h: 9, m: 0}), "У середу о 9:00."],
  ["tr : 9.00'da", Dire.trad("tr", "agendaRep", {j: 0, h: 9, m: 0}), "Pazartesi saat 9.00'da."],
  ["tr : 13.30'da", Dire.trad("tr", "evtDebut", {e: "konzert", h: 13, m: 30}), "Konser saat 13.30'da başlıyor."],
  ["tr : 20.00'de", Dire.trad("tr", "evtDebut", {e: "party", h: 20, m: 0}), "Parti saat 20.00'de başlıyor."],
  ["tr : 3 Mayıs'ta", Dire.trad("tr", "anniv", {d: 3, mo: 4}), "Doğum günüm 3 Mayıs'ta."],
  ["ru : была среда", Dire.trad("ru", "hier", {j: 2}), "Сегодня четверг. Вчера была среда."],
  ["ru : было воскресенье", Dire.trad("ru", "hier", {j: 6}), "Сегодня понедельник. Вчера было воскресенье."],
  ["pl : we wrześniu", Dire.trad("pl", "annivMois", {mo: 8}), "Moje urodziny są we wrześniu."],
  ["fa : chiffres persans", Dire.trad("fa", "heure", {h: 14, m: 30, style: "o"}), "ساعت ۱۴:۳۰ است."]
];
let justes = 0;
for (const [quoi, obtenu, attendu] of A){
  if (obtenu === attendu) justes++;
  else fautes.push("piege « " + quoi + " » : « " + obtenu + " » au lieu de « " + attendu + " »");
}

// 5. LE RELEVE A RELIRE A LA MAIN : chaque cas piege, et les heures charnieres dans les quatre langues
const r = ["# Le banc de « L'heure et les dates » : ce qu'il faut relire a la main", "",
  "Fait par `node tests/heure_banc.js` (" + HEURES.length + " heures x " + APPRISES.length + " langues, " + DATES.length + " dates, l'agenda, 10 langues d'interface).", "",
  "## Les cas pieges (" + justes + " / " + A.length + " justes)", ""];
A.forEach(([q, o, a]) => r.push("- " + q + " : " + o + (o === a ? "" : "   <-- attendu : " + a)));
r.push("", "## Les heures charnieres, dans chaque langue et chaque lecture", "");
for (const [h, m] of [[0, 0], [0, 30], [0, 45], [1, 0], [1, 30], [11, 45], [12, 0], [12, 15], [12, 30], [12, 45], [13, 0], [14, 30], [18, 45], [23, 30], [23, 58]]){
  r.push("### " + h + ":" + Dire.deux(m));
  for (const L of APPRISES) r.push("- " + L + " : " + STYLES[L].map(st => H(L, h, m, st)).join(" · "));
  r.push("- fr : " + ["c", "o", "m"].map(st => T("fr", h, m, st)).join(" · "));
  r.push("");
}
r.push("## Les dates charnieres", "");
for (const [mo, d] of [[0, 1], [1, 28], [2, 1], [4, 3], [6, 7], [7, 8], [8, 21], [10, 22], [11, 23], [11, 31]]){
  r.push("- " + (d + "/" + (mo + 1)) + " : " + APPRISES.map(L => Dire.phrase(L, "date", {d, mo})).join(" · ") + " · " + APPRISES.map(L => Dire.phrase(L, "anniv", {d, mo})).join(" · "));
}
fs.writeFileSync(path.join(RACINE, "visuel", "heure", "banc.md"), r.join("\n") + "\n");
if (TOUT) console.log(lignes.join("\n"));
console.log("heures : " + HEURES.length + " par langue et par lecture ; dates : " + DATES.length + " ; cas pieges : " + justes + " / " + A.length + " justes");
if (fautes.length){
  console.log("\nFAUTES (" + fautes.length + ") :\n  " + fautes.slice(0, 60).join("\n  "));
  process.exit(1);
}
console.log("OK : aucune faute. Releve a relire : visuel/heure/banc.md");
