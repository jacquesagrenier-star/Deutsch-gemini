// LES PAGES DU TELC DANS LES AUTRES LANGUES D'INTERFACE (7 nov. 2026, decision de Jacques : « s'assurer qu'ils sont
// traduits dans toutes les langues »).
//
// Les pages sont ecrites en francais et en anglais. Pour les autres langues, un DICTIONNAIRE par langue va de
// l'anglais vers la langue : langues/<langue>.js (window.TELC_DICO = { "texte anglais": "traduction" }), consulte
// par textesTelc(), champTelc() et objetTelc() de telc-commun.js, et par u(), tr() et la replique de oral.html.
// Un texte absent du dictionnaire retombe sur le francais : rien ne casse, mais la langue n'est ouverte dans l'app
// (LANGUES_PAGES_TELC d'index.html) que lorsque « controler » ne trouve plus aucun manque.
//
//   node outils/langues.js extraire            -> langues/source.json : chaque texte anglais, avec son francais et
//                                                 l'endroit ou il sert (a donner aux traducteurs)
//   node outils/langues.js construire <lg>     -> langues/<lg>.js a partir de langues/<lg>.json ({anglais: trad})
//   node outils/langues.js controler [<lg>...] -> ce qui manque, langue par langue (code de sortie 1 s'il manque)
//
// Les textes allemands de l'examen ne se traduisent jamais : ils ne sont pas dans la source.

"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ICI = path.dirname(__dirname);           // visuel/prototype/telc
const LANGUES = ["tr", "uk", "fa", "ar", "pt", "pl", "ru"];
const MODULES = ["telc-commun.js", "lesen.js", "sprachbausteine.js", "schreiben.js", "hoeren.js",
                 "hoeren-schreiben.js", "sprechen.js", "examen-blanc.js"];

// un objet qui accepte tout (le DOM, DTZ, fetch…) : les modules s'evaluent sans navigateur
function bouchon(){
  const f = function(){ return p; };
  const p = new Proxy(f, { get: (t, k) => k === Symbol.toPrimitive ? (() => "") : (k === "then" ? undefined : p),
                           set: () => true, apply: () => p, construct: () => p });
  return p;
}

const SOURCE = new Map();   // anglais -> {fr, ou:Set}
function ajouter(en, fr, ou){
  if (typeof en !== "string" || !en.trim()) return;
  if (!/[A-Za-z]/.test(en)) return;            // ponctuation, nombres seuls
  const e = SOURCE.get(en) || { fr: typeof fr === "string" ? fr : "", ou: new Set() };
  if (!e.fr && typeof fr === "string") e.fr = fr;
  e.ou.add(ou);
  SOURCE.set(en, e);
}
function paire(en, fr, ou){
  if (Array.isArray(en)) en.forEach((x, i) => paire(x, Array.isArray(fr) ? fr[i] : "", ou));
  else ajouter(en, fr, ou);
}

function extraireModules(){
  const B = bouchon();
  const ctx = { console, Promise, setTimeout: () => 0, clearTimeout(){}, setInterval: () => 0, clearInterval(){},
                URLSearchParams, Date, Math, JSON, Object, Array, String, Number, RegExp, Map, Set, Symbol, Error,
                document: B, location: { search: "?lang=en", href: "" }, localStorage: B, speechSynthesis: B,
                SpeechSynthesisUtterance: function(){ return B; }, Audio: function(){ return B; },
                fetch: () => new Promise(() => {}), navigator: B, addEventListener(){}, requestAnimationFrame: () => 0 };
  ctx.window = ctx; ctx.parent = ctx; ctx.globalThis = ctx;
  vm.createContext(ctx);
  // comme telc.html : son profil (le script en ligne qui pose PROFIL_EXAMEN), tirage.js, puis le vrai commun.js du DTZ
  const page = fs.readFileSync(path.join(ICI, "telc.html"), "utf8");
  const profil = [...page.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).find(s => s.includes("PROFIL_EXAMEN"));
  vm.runInContext(profil, ctx, { filename: "telc.html (profil)" });
  vm.runInContext(fs.readFileSync(path.join(ICI, "..", "themes", "tirage.js"), "utf8"), ctx, { filename: "tirage.js" });
  vm.runInContext(fs.readFileSync(path.join(ICI, "..", "dtz", "commun.js"), "utf8"), ctx, { filename: "commun.js" });
  let courant = "";
  for (const m of MODULES){
    courant = m;
    const code = fs.readFileSync(path.join(ICI, m), "utf8");
    vm.runInContext(code, ctx, { filename: m });
    if (m === "telc-commun.js"){
      // a partir d'ici, chaque appel des modules est releve (telc-commun.js a deja verse ses propres textes)
      ctx.textesTelc = t => {
        const en = (t && t.en) || {}, fr = (t && t.fr) || {};
        for (const k in en) paire(en[k], fr[k], courant + ":" + k);
      };
    }
  }
  // les textes de telc-commun.js lui-meme (son appel a eu lieu avant le releve) : relus dans son code
  const tc = fs.readFileSync(path.join(ICI, "telc-commun.js"), "utf8");
  const i = tc.indexOf("textesTelc({ en: {");
  if (i >= 0){
    const corps = tc.slice(i + "textesTelc({ en: ".length, tc.indexOf("}});", i) + 1);
    const o = vm.runInNewContext("(" + corps + ")");
    for (const k in o) ajouter(o[k], "", "telc-commun.js:" + k);
  }
  const m2 = tc.match(/const EN = (\{[^}]*\})/);
  if (m2){ const o = vm.runInNewContext("(" + m2[1] + ")"); for (const k in o) ajouter(o[k], "", "telc-commun.js:tuile " + k); }
}

function extraireDonnees(){
  const dossier = path.join(ICI, "donnees");
  for (const f of fs.readdirSync(dossier).filter(x => x.endsWith(".json"))){
    const d = JSON.parse(fs.readFileSync(path.join(dossier, f), "utf8"));
    (function marche(o, chemin){
      if (Array.isArray(o)) return o.forEach((x, i) => marche(x, chemin + "[" + i + "]"));
      if (!o || typeof o !== "object") return;
      for (const k of Object.keys(o)){
        const m = k.match(/^(.*)_en$/);
        if (m) paire(o[k], o[m[1] + "_fr"], "donnees/" + f + ":" + chemin + "." + m[1]);
        else if (k === "en" && "fr" in o) paire(o.en, o.fr, "donnees/" + f + ":" + chemin);
        else marche(o[k], chemin + "." + k);
      }
    })(d, "");
  }
}

function extraireOral(){
  const html = fs.readFileSync(path.join(ICI, "oral.html"), "utf8");
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  const code = scripts.join("\n;\n");
  const noms = [...new Set([...code.matchAll(/^const ([A-Z][A-Z0-9_]*)\s*=/gm)].map(m => m[1]))];
  const B = bouchon();
  const ctx = { console, Promise, setTimeout: () => 0, clearTimeout(){}, setInterval: () => 0, clearInterval(){},
                URLSearchParams, Date, Math, JSON, Object, Array, String, Number, RegExp, Map, Set, Symbol, Error,
                document: B, location: { search: "?lang=en", href: "" }, localStorage: B, sessionStorage: B,
                speechSynthesis: B, SpeechSynthesisUtterance: function(){ return B; }, navigator: B, fetch: () => new Promise(() => {}),
                Audio: function(){ return B; }, addEventListener(){}, requestAnimationFrame: () => 0 };
  ctx.window = ctx; ctx.parent = ctx; ctx.globalThis = ctx;
  vm.createContext(ctx);
  const sortie = noms.map(n => "typeof " + n + " !== 'undefined' ? " + n + " : undefined").join(",");
  try{
    vm.runInContext(code + "\n;globalThis.__X = [" + sortie + "];", ctx, { filename: "oral.html" });
  }catch(e){
    // la page peut lancer une erreur apres ses declarations (le DOM bouchonne) : on garde ce qui est defini
    try{ vm.runInContext("globalThis.__X = [" + sortie + "];", ctx); }catch(e2){ throw e; }
  }
  const X = ctx.__X || [];
  noms.forEach((n, i) => {
    const v = X[i];
    if (n === "UI" && v && v.en){ for (const k in v.en) ajouter(v.en[k], (v.fr || {})[k], "oral:UI." + k); return; }
    (function marche(o, chemin){
      if (Array.isArray(o)){
        // une replique : [qui, allemand, francais, anglais]
        if (o.length === 4 && (o[0] === "anna" || o[0] === "mark") && typeof o[3] === "string"){ ajouter(o[3], o[2], "oral:" + chemin); return; }
        return o.forEach((x, j) => marche(x, chemin + "[" + j + "]"));
      }
      if (!o || typeof o !== "object") return;
      if ("en" in o && "fr" in o){ paire(o.en, o.fr, "oral:" + chemin); return; }
      // une reponse modele : {niv, de: [allemand, francais, anglais]}
      if (Array.isArray(o.de) && o.de.length === 3 && o.de.every(x => typeof x === "string")){
        ajouter(o.de[2], o.de[1], "oral:" + chemin + ".de");
        for (const k of Object.keys(o)) if (k !== "de") marche(o[k], chemin + "." + k);
        return;
      }
      for (const k of Object.keys(o)) marche(o[k], chemin + "." + k);
    })(v, n);
  });
}

function extraire(){
  extraireModules(); extraireDonnees(); extraireOral();
  const liste = [...SOURCE.entries()].map(([en, e]) => ({ en, fr: e.fr, ou: [...e.ou].slice(0, 3) }));
  fs.mkdirSync(path.join(ICI, "langues"), { recursive: true });
  fs.writeFileSync(path.join(ICI, "langues", "source.json"), JSON.stringify(liste, null, 1) + "\n");
  const car = liste.reduce((a, x) => a + x.en.length, 0);
  console.log("langues/source.json :", liste.length, "textes,", car, "caracteres anglais");
}

function charger(lg){
  const f = path.join(ICI, "langues", lg + ".json");
  return fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, "utf8")) : {};
}
function source(){ return JSON.parse(fs.readFileSync(path.join(ICI, "langues", "source.json"), "utf8")); }

// les {n}, {m}, les balises et les mots allemands entre guillemets doivent survivre a la traduction
function defauts(en, tr){
  const pl = s => (s.match(/\{[a-z_]+\}/g) || []).sort().join(" ");
  const bal = s => (s.match(/<\/?[a-z]+[^>]*>/gi) || []).length;
  const out = [];
  if (pl(en) !== pl(tr)) out.push("variables " + pl(en) + " / " + pl(tr));
  if (bal(en) !== bal(tr)) out.push("balises HTML " + bal(en) + " / " + bal(tr));
  return out;
}

function construire(lg){
  const d = charger(lg), s = source();
  const dico = {};
  let manque = 0;
  for (const x of s){ if (typeof d[x.en] === "string" && d[x.en].trim()) dico[x.en] = d[x.en]; else manque++; }
  const js = "// " + lg + " : dictionnaire anglais -> " + lg + " des pages du telc. DERIVE de langues/" + lg + ".json par\n" +
             "// node outils/langues.js construire " + lg + " -- ne pas corriger ici.\n" +
             "window.TELC_DICO = " + JSON.stringify(dico) + ";\n";
  fs.writeFileSync(path.join(ICI, "langues", lg + ".js"), js);
  console.log("langues/" + lg + ".js :", Object.keys(dico).length, "textes ;", manque, "manquant(s)");
}

function controler(lgs){
  const s = source();
  let total = 0;
  for (const lg of (lgs.length ? lgs : LANGUES)){
    const d = charger(lg);
    const manque = s.filter(x => !(typeof d[x.en] === "string" && d[x.en].trim()));
    const fautes = s.filter(x => typeof d[x.en] === "string").map(x => ({x, f: defauts(x.en, d[x.en])})).filter(y => y.f.length);
    const js = fs.existsSync(path.join(ICI, "langues", lg + ".js"));
    console.log(lg + " :", s.length - manque.length, "/", s.length, "traduits ;", fautes.length, "defaut(s) ;", js ? "langues/" + lg + ".js present" : "PAS de langues/" + lg + ".js");
    manque.slice(0, 5).forEach(x => console.log("    manque :", x.en.slice(0, 90)));
    fautes.slice(0, 5).forEach(y => console.log("    defaut :", y.f.join(", "), "--", y.x.en.slice(0, 70)));
    total += manque.length + fautes.length + (js ? 0 : 1);
  }
  process.exitCode = total ? 1 : 0;
}

const [cmd, ...args] = process.argv.slice(2);
if (cmd === "extraire") extraire();
else if (cmd === "construire") args.forEach(construire);
else if (cmd === "controler") controler(args);
else console.log("usage : node outils/langues.js extraire | construire <lg>... | controler [<lg>...]");
