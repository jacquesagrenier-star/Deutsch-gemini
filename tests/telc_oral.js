// Controle de l'oral du telc A2·B1 (visuel/prototype/telc/oral.html), sans navigateur.
//
// Usage : node tests/telc_oral.js
//
// Ne 6 nov. 2026 (session « telc : Parler + examen blanc ») d'un retour de testeuse B1 : des reponses C1 dans un oral
// B1 decouragent. Le controle verifie :
//   1. l'interface en francais ET en anglais : memes cles, rien de vide (UI, COACH, ATTEND, sujets) ;
//   2. chaque replique [qui, allemand, francais, anglais] complete ;
//   3. les repliques reprises du DTZ gardent EXACTEMENT leur allemand (sinon leur clip et leur voix ne collent plus) ;
//   4. chaque exercice a deux reponses modeles, une A2 et une B1, et aucun autre niveau ; aucun texte ne parle de
//      B2, C1 ou C2 ;
//   5. aucun chiffre dans ce qui se dit en allemand (les nombres se disent en lettres, CLAUDE.md), sauf les noms
//      de niveau A2 et B1 des verdicts d'Anna, deja enregistres ;
//   6. les sujets : cinq points et cinq tours par planification, les repliques de chaque avis presentes ;
//   7. les juges : chaque modele B1 est juge B1, chaque modele A2 au moins A2 (sinon un juge ou un modele est faux).
"use strict";
const fs = require("fs");
const path = require("path");
const RACINE = path.dirname(__dirname);
const PAGE = path.join(RACINE, "visuel", "prototype", "telc", "oral.html");
const DTZ = path.join(RACINE, "visuel", "prototype", "dtz-oral.html");

const fautes = [];
const faute = (ou, quoi) => fautes.push(ou + " : " + quoi);

function scriptDe(fichier){
  const h = fs.readFileSync(fichier, "utf8");
  const m = [...h.matchAll(/<script>([\s\S]*?)<\/script>/g)];
  return m.map(x => x[1]).join("\n");
}
// un faux DOM, juste assez pour que la page se charge
function faux(){
  const e = { children: [], style: {}, dataset: {}, textContent: "", innerHTML: "", hidden: false, disabled: false,
    classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
    setAttribute(){}, getAttribute(){ return null; }, appendChild(c){ this.children.push(c); return c; },
    append(...c){ this.children.push(...c); }, remove(){}, querySelector(){ return null; }, querySelectorAll(){ return []; },
    scrollIntoView(){}, addEventListener(){}, focus(){} };
  return e;
}
function charger(fichier, lang, exporter){
  const doc = { documentElement: faux(), getElementById: () => faux(), createElement: () => faux(), title: "" };
  const fen = { parent: null, addEventListener(){}, scrollTo(){}, SpeechRecognition: null, webkitSpeechRecognition: null, speechSynthesis: null };
  fen.parent = fen;
  const stock = {};
  const ls = { getItem: k => stock[k] || null, setItem: (k, v) => { stock[k] = String(v); } };
  const loc = { search: "?lang=" + lang, href: "" };
  const fetch0 = () => Promise.resolve({ ok: false, json: () => ({}) });
  const code = scriptDe(fichier) + "\n;return {" + exporter + "};";
  const f = new Function("document", "window", "localStorage", "location", "fetch", "Zoom", "history", "SpeechSynthesisUtterance", "Audio", code);
  return f(doc, fen, ls, loc, fetch0, { init(){} }, { back(){} }, function(){}, function(){});
}

const P = charger(PAGE, "fr", "UI, COACH, ATTEND, AIDE, L, MODELES_1A, MODELES_1B, PLAN, AVIS, JUGES, u, STICHWORTE");
// --json : les textes allemands, pour visuel/prototype/telc/outils/relecture_oral.py (la relecture germanophone)
if (process.argv.includes("--json")){
  const sansRe = o => JSON.parse(JSON.stringify(o, (k, v) => v instanceof RegExp ? undefined : v));
  process.stdout.write(JSON.stringify({ L: P.L, MODELES_1A: P.MODELES_1A, MODELES_1B: P.MODELES_1B, PLAN: sansRe(P.PLAN), AVIS: sansRe(P.AVIS), AIDE: P.AIDE, STICHWORTE: P.STICHWORTE }));
  process.exit(0);
}
const PE = charger(PAGE, "en", "u");

// 1. l'interface
const kf = Object.keys(P.UI.fr), ke = Object.keys(P.UI.en);
kf.filter(k => !ke.includes(k)).forEach(k => faute("UI", "cle « " + k + " » sans anglais"));
ke.filter(k => !kf.includes(k)).forEach(k => faute("UI", "cle « " + k + " » sans francais"));
for (const l of ["fr", "en"]) for (const k in P.UI[l]) if (!String(P.UI[l][k]).trim()) faute("UI." + l, "cle « " + k + " » vide");
if (PE.u("titre") === P.u("titre")) faute("UI", "l'anglais ne s'applique pas (lang=en donne le titre francais)");
for (const nom of ["COACH", "ATTEND"]) for (const k in P[nom]) for (const l of ["fr", "en"]){
  const v = P[nom][k][l];
  if (!v || (Array.isArray(v) ? !v.length || v.some(x => !String(x).trim()) : !String(v).trim())) faute(nom + "." + k, "pas de texte « " + l + " »");
}
if (P.ATTEND.p1a.fr.length !== P.ATTEND.p1a.en.length) faute("ATTEND", "fr et en n'ont pas le meme nombre de lignes");

// 2. les repliques
for (const id in P.L){
  const r = P.L[id];
  if (r.length !== 4 || r.some(x => !String(x || "").trim())) faute("L." + id, "replique incomplete (qui, allemand, francais, anglais)");
  if (!["anna", "mark"].includes(r[0])) faute("L." + id, "personne inconnue « " + r[0] + " »");
}

// 3. les repliques reprises du DTZ : meme allemand, mot pour mot
const D = charger(DTZ, "fr", "L");
for (const id in P.L){
  if (/^t_/.test(id)) continue;   // « t_... » : ecrites pour le telc
  if (!D.L[id]) faute("L." + id, "id sans « t_ » mais absent de l'oral du DTZ : renommer en t_" + id);
  else if (D.L[id][1] !== P.L[id][1]) faute("L." + id, "l'allemand differe de celui du DTZ : son clip et sa voix ne collent plus");
}

// 4. les modeles : A2 et B1, rien d'autre
const listes = [["MODELES_1A", P.MODELES_1A]];
for (const q in P.MODELES_1B) listes.push(["MODELES_1B." + q, P.MODELES_1B[q]]);
for (const s in P.PLAN) P.PLAN[s].tours.forEach((t, k) => listes.push(["PLAN." + s + "." + (k + 1), [{ niv: "A2", de: t.a2 }, { niv: "B1", de: t.b1 }]]));
for (const s in P.AVIS){
  listes.push(["AVIS." + s + ".avis", P.AVIS[s].avis]);
  for (const c of ["A", "B"]) listes.push(["AVIS." + s + ".reaction." + c, (P.AVIS[s].reaction || {})[c] || []]);
}
for (const [ou, liste] of listes){
  const nivs = liste.map(m => m.niv).sort().join(",");
  if (nivs !== "A2,B1") faute(ou, "il faut un modele A2 et un modele B1 (trouve : " + (nivs || "aucun") + ")");
  liste.forEach(m => {
    if (m.id){ if (!P.L[m.id]) faute(ou, "modele « " + m.id + " » sans replique"); return; }
    if (!Array.isArray(m.de) || m.de.length !== 3 || m.de.some(x => !String(x || "").trim())) faute(ou, "modele " + m.niv + " incomplet (allemand, francais, anglais)");
  });
}
const tout = JSON.stringify([P.UI, P.COACH, P.ATTEND, P.AIDE, P.L, P.MODELES_1A, P.MODELES_1B, P.PLAN, P.AVIS]);
const haut = tout.match(/\b(B2|C1|C2)\b/g);
if (haut) faute("textes", "un niveau au-dessus du B1 est nomme : " + [...new Set(haut)].join(", "));

// 5. pas de chiffre dans l'allemand dit
const dits = [];
for (const id in P.L) dits.push(["L." + id, P.L[id][1]]);
for (const [ou, liste] of listes) liste.forEach(m => { if (m.de) dits.push([ou + " " + m.niv, m.de[0]]); });
dits.forEach(([ou, t]) => { t = t.replace(/\b[AB][12]\b/g, ""); if (/\d/.test(t)) faute(ou, "un chiffre dans l'allemand dit (« " + t.match(/\S*\d\S*/)[0] + " ») : l'ecrire en lettres"); });

// 6. les sujets
for (const s in P.PLAN){
  const S = P.PLAN[s];
  if (S.punkte.length !== 5 || S.tours.length !== 5) faute("PLAN." + s, "il faut cinq points et cinq tours");
  if (!P.L[S.intro]) faute("PLAN." + s, "consigne d'Anna absente (" + S.intro + ")");
  S.tours.forEach((t, k) => { if (!P.L[t.m]) faute("PLAN." + s, "proposition de Mark absente au point " + (k + 1)); });
  if (!S.blatt || !S.titre.fr || !S.titre.en) faute("PLAN." + s, "feuille ou titre absent");
}
for (const s in P.AVIS){
  const S = P.AVIS[s];
  for (const k of ["frage", "gegenA", "gegenB"]) if (!P.L[S[k]]) faute("AVIS." + s, "replique « " + k + " » absente");
  if (!S.blatt || !S.titre.fr || !S.titre.en) faute("AVIS." + s, "feuille ou titre absent");
}

// 7. les juges contre les modeles
const RANG = { moins: 0, A2: 1, B1: 2 };
function juger(ou, juge, texte, niv){
  const r = P.JUGES[juge](texte);
  if (niv === "B1" && r.niveau !== "B1") faute(ou, "le modele B1 est juge " + r.niveau + " par " + juge);
  if (niv === "A2" && RANG[r.niveau] < 1) faute(ou, "le modele A2 est juge « " + r.niveau + " » par " + juge);
}
const texte = m => m.id ? P.L[m.id][1] : m.de[0];
P.MODELES_1A.forEach(m => juger("MODELES_1A", "p1a", texte(m), m.niv));
for (const q in P.MODELES_1B) P.MODELES_1B[q].forEach(m => juger("MODELES_1B." + q, "p1b", texte(m), m.niv));
for (const s in P.AVIS){
  P.AVIS[s].avis.forEach(m => juger("AVIS." + s + ".avis", "p3a", texte(m), m.niv));
  for (const c of ["A", "B"]) P.AVIS[s].reaction[c].forEach(m => juger("AVIS." + s + ".reaction." + c, "p3b", texte(m), m.niv));
}
// la planification se juge sur les cinq tours : les cinq reponses B1 d'un sujet doivent faire un B1
for (const s in P.PLAN){
  const r = P.JUGES.p2(P.PLAN[s].tours.map(t => t.b1[0]));
  if (r.niveau !== "B1") faute("PLAN." + s, "les cinq reponses B1 sont jugees " + r.niveau);
}

const n = { repliques: Object.keys(P.L).length, modeles: listes.reduce((x, l) => x + l[1].length, 0), cles: kf.length };
if (fautes.length){
  console.log(fautes.length + " probleme(s) dans l'oral du telc :");
  fautes.forEach(f => console.log("  - " + f));
  process.exit(1);
}
console.log("Oral du telc : aucun probleme (" + n.repliques + " repliques, " + n.modeles + " reponses modeles A2 / B1, " + n.cles + " cles fr / en).");
