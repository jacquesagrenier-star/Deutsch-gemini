// Exerce le VRAI code de « Quel article ? » (v540), extrait d'index.html, sur
// les VRAIES donnees de themes.json. Le bloc va de QUIZ_ARTICLE_TAILLE a la fin
// de startQuizArticle().
//
// Ce que ce banc surveille avant tout : LE TIRAGE EN TIERS EGAUX. C'est la
// seule chose qui separe un exercice d'un score qui felicite l'ignorance, et
// c'est aussi la premiere qu'une « simplification » ferait sauter.
const fs = require("fs");
const src = fs.readFileSync("index.html", "utf8");

const i = src.indexOf("const QUIZ_ARTICLE_TAILLE = 30;");
const k = src.indexOf("\n}", src.indexOf("function startQuizArticle(){")) + 2;
if (i < 0 || k < 2) throw new Error("bloc introuvable dans index.html");
const BLOC = src.slice(i, k);

// ---- L'environnement, reduit a ce que le bloc lit -------------------------
globalThis.SUFFIXE_LANGUE = { fr: "_fr", en: "_en", tr: "_tr", uk: "_uk", fa: "_fa" };
globalThis.RANGS_CARTE = {
  nomen: { traduction: { fr: 3, en: 4, tr: 12, uk: 15, fa: 17 } }
};
const REPLI = { fr: ["fr"], en: ["en", "fr"], tr: ["tr", "en", "fr"],
                uk: ["uk", "en", "fr"], fa: ["fa", "en", "fr"] };
globalThis.texteCarte = (carte, type, quoi, lang) => {
  const rangs = RANGS_CARTE[type][quoi];
  for (const code of REPLI[lang]) if (carte[rangs[code]]) return carte[rangs[code]];
  return "";
};
globalThis.I18N = {
  fr: { label_plural: "Pluriel :" }, en: { label_plural: "Plural:" },
  tr: { label_plural: "Çoğul:" }, uk: { label_plural: "Множина:" },
  fa: { label_plural: "جمع:" }
};
globalThis.t = c => c;
globalThis.showInfoToast = () => { throw new Error("l'exercice s'est declare vide"); };
globalThis.openOrbPanel = () => {};
globalThis.shuffleArray = a => a;            // ordre fige : le banc doit etre reproductible
globalThis.sansDoublons = a => a;
globalThis.LEVELS = ["A1", "A2", "B1", "B2", "C1"];
// La seance ne sert a rien ici : on veut mesurer l'equilibre sur TOUT le
// reservoir, pas sur les quarante cartes du jour.
globalThis.cartesDeSession = () => [];
let SERVI = null;
globalThis.startExerciseSet = (liste, kicker) => { SERVI = { liste, kicker }; };

// ---- Les vraies donnees ---------------------------------------------------
const brut = JSON.parse(fs.readFileSync("themes.json", "utf8"));
const themes = brut.themes.map(t => {
  const niveau = (t.niveau || "A1").toUpperCase();
  const words = (t.mots || []).map(w => {
    const c = [];
    c[0] = w.mot || ""; c[1] = w.genre || "der"; c[2] = w.pluriel || "—";
    c[3] = w.traduction || ""; c[4] = w.traduction_en || "";
    c[12] = w.traduction_tr || ""; c[15] = w.traduction_uk || ""; c[17] = w.traduction_fa || "";
    return c;
  });
  return { levels: { [niveau]: { id: t.id, words } } };
});
globalThis.themesComptes = () => themes;

eval(BLOC + "\nglobalThis.startQuizArticle = startQuizArticle;"
   + "\nglobalThis.construireQuizArticle = construireQuizArticle;"
   + "\nglobalThis.QUIZ_ARTICLE_TAILLE = QUIZ_ARTICLE_TAILLE;");

let ko = 0;
const ok = (n, v) => { console.log("  " + (v ? "OK   " : "ECHEC") + "  " + n); if (!v) ko++; };

// ---- Le desequilibre qu'on corrige ---------------------------------------
console.log("\nLE DEFAUT QU'ON EVITE : REPONDRE « DIE » A TOUT");
const tous = [];
themes.forEach(t => Object.values(t.levels).forEach(l => l.words.forEach(w => tous.push(w))));
const naturel = { der: 0, die: 0, das: 0 };
tous.forEach(w => { if (naturel[w[1]] !== undefined) naturel[w[1]]++; });
const totalTrois = naturel.der + naturel.die + naturel.das;
const partDie = naturel.die / totalTrois;
console.log("     reservoir reel : der " + naturel.der + " · die " + naturel.die
            + " · das " + naturel.das);
ok("un tirage naturel donnerait plus de 45 % a « die » (" + (partDie * 100).toFixed(1) + " %)",
   partDie > 0.45);

// ---- La serie servie ------------------------------------------------------
console.log("\nLA SERIE SERVIE");
startQuizArticle();
ok("une serie est servie", !!SERVI);
ok("elle porte " + QUIZ_ARTICLE_TAILLE + " questions", SERVI.liste.length === QUIZ_ARTICLE_TAILLE);
ok("le kicker est celui du quiz", SERVI.kicker === "kicker_quiz_article");

const compte = { der: 0, die: 0, das: 0 };
SERVI.liste.forEach(e => { compte[e.correct]++; });
console.log("     serie servie   : der " + compte.der + " · die " + compte.die
            + " · das " + compte.das);
ok("dix « der »", compte.der === 10);
ok("dix « die »", compte.die === 10);
ok("dix « das »", compte.das === 10);
ok("repondre « die » a tout ne donne plus que 33 %",
   Math.abs(compte.die / SERVI.liste.length - 1 / 3) < 0.001);

// ---- La forme de chaque question -----------------------------------------
console.log("\nCHAQUE QUESTION");
const LANGUES = ["", "_en", "_tr", "_uk", "_fa"];
let blancs = 0, options = 0, langues = 0, audio = 0, indices = 0;
SERVI.liste.forEach(e => {
  if (/^___ \S/.test(e.question)) blancs++;
  if (e.options.length === 3 && e.options.join() === "der,die,das") options++;
  if (LANGUES.every(s => e["question" + s] && e["explanation" + s])) langues++;
  if (e.audioDe === e.correct + " " + e.question.slice(4)) audio++;
  if (LANGUES.every(s => e["hint" + s] === "")) indices++;
});
ok("toutes commencent par le blanc « ___ »", blancs === SERVI.liste.length);
ok("toutes offrent der/die/das", options === SERVI.liste.length);
ok("toutes portent leurs CINQ langues", langues === SERVI.liste.length);
ok("la voix lit « der Tisch », pas le blanc", audio === SERVI.liste.length);
ok("aucun indice : le seul possible serait la reponse", indices === SERVI.liste.length);

// ---- La reponse est la vraie, et l'explication enseigne le pluriel --------
console.log("\nLA REPONSE ET CE QU'ELLE APPREND");
const parMot = {};
tous.forEach(w => { parMot[w[0]] = w; });
let justes = 0, pluriels = 0, tirets = 0;
SERVI.liste.forEach(e => {
  const mot = e.question.slice(4);
  const carte = parMot[mot];
  if (carte && carte[1] === e.correct) justes++;
  const pl = (carte[2] || "").trim();
  const aPluriel = pl && pl !== "—" && pl !== "-";
  if (aPluriel && e.explanation.includes("die " + pl)) pluriels++;
  if (!aPluriel && e.explanation.endsWith("—")) tirets++;
});
ok("la bonne reponse est le genre reel du mot", justes === SERVI.liste.length);
ok("l'explication donne le pluriel quand il existe (" + pluriels + " mots)", pluriels > 0);
ok("les mots sans pluriel gardent le tiret, pas un faux pluriel",
   pluriels + tirets === SERVI.liste.length);

// ---- Les genres doubles n'entrent pas ------------------------------------
console.log("\nLES GENRES DOUBLES");
const doubles = tous.filter(w => ["der", "die", "das"].indexOf(w[1]) < 0).map(w => w[0]);
console.log("     ecartes du reservoir : " + doubles.join(", "));
ok("aucun genre double dans la serie",
   SERVI.liste.every(e => ["der", "die", "das"].indexOf(e.correct) >= 0));

// ---- La majuscule du blanc en tete --------------------------------------
// « ___ Mann ist alt. » doit donner « Der Mann ist alt. » ; « ___ Baby » doit
// donner « das Baby ». Les deux regles vivent dans la meme ligne de code, et
// c'est exactement le genre de ligne qu'une prochaine version resimplifie.
console.log("\nLA MAJUSCULE DU BLANC EN TETE");
const iM = src.indexOf("function enonceEstUnePhrase(enonce){");
const kM = src.indexOf("\n}", src.indexOf("function phraseSeuleArticle(phrase, rep){")) + 2;
eval(src.slice(iM, kM) + "\nglobalThis.phraseSeuleArticle = phraseSeuleArticle;"
   + "\nglobalThis.enonceEstUnePhrase = enonceEstUnePhrase;");
ok("une PHRASE garde sa capitale",
   phraseSeuleArticle("___ Mann ist alt. (der Mann, Nominativ)", "der") === "Der Mann ist alt. (der Mann, Nominativ)");
ok("une entree de dictionnaire ne la prend pas",
   phraseSeuleArticle("___ Baby", "das") === "das Baby");
ok("aucune question du quiz ne ressemble a une phrase",
   SERVI.liste.every(e => !enonceEstUnePhrase(e.question)));

console.log("\n" + (ko ? "ECHEC : " + ko + " controle(s)\n" : "OK : tous les controles passent\n"));
process.exit(ko ? 1 : 0);
