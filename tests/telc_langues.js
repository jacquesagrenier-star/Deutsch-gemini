// Controle des langues des pages du telc (visuel/prototype/telc/) : une langue de LANGUES_PAGES_TELC (index.html),
// autre que le francais et l'anglais ecrits dans les modules, doit avoir TOUS ses textes traduits.
//
// Usage : node tests/telc_langues.js
// 1. refait la liste des textes anglais (outils/langues.js extraire) et verifie que langues/source.json n'a pas change :
//    un texte ajoute ou modifie dans une page sans sa traduction ferait retomber cette langue sur le francais ;
// 2. pour chaque langue ouverte dans l'app : 0 manque, 0 defaut (variables, balises), langues/<lg>.js present et a
//    jour de langues/<lg>.json.
"use strict";
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const RACINE = path.dirname(__dirname);
const TELC = path.join(RACINE, "visuel", "prototype", "telc");
let fautes = 0;

const html = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");
const m = html.match(/const LANGUES_PAGES_TELC = (\[[^\]]*\]);/);
if (!m){ console.log("LANGUES_PAGES_TELC introuvable dans index.html"); process.exit(1); }
const ouvertes = JSON.parse(m[1]).filter(l => l !== "fr" && l !== "en");

// 1. la source est-elle a jour ?
const src = path.join(TELC, "langues", "source.json");
const avant = fs.readFileSync(src, "utf8");
execFileSync(process.execPath, [path.join(TELC, "outils", "langues.js"), "extraire"], { cwd: TELC, stdio: "pipe" });
const apres = fs.readFileSync(src, "utf8");
if (avant.replace(/\r\n/g, "\n") !== apres.replace(/\r\n/g, "\n")){
  console.log("langues/source.json n'etait pas a jour : des textes des pages ont change. Traduire les nouveaux, puis relancer.");
  fautes++;
}
const source = JSON.parse(apres);

// 2. chaque langue ouverte
for (const lg of ouvertes){
  const fj = path.join(TELC, "langues", lg + ".json"), fs_ = path.join(TELC, "langues", lg + ".js");
  if (!fs.existsSync(fj) || !fs.existsSync(fs_)){ console.log(lg + " : langues/" + lg + ".json ou .js absent"); fautes++; continue; }
  const d = JSON.parse(fs.readFileSync(fj, "utf8"));
  const manque = source.filter(x => !(typeof d[x.en] === "string" && d[x.en].trim()));
  const var_ = s => (s.match(/\{[a-z_]+\}/g) || []).sort().join(" ");
  const defauts = source.filter(x => typeof d[x.en] === "string" && var_(x.en) !== var_(d[x.en]));
  // le .js doit etre celui que construirait le .json
  const js = fs.readFileSync(fs_, "utf8");
  const dico = JSON.parse(js.slice(js.indexOf("=") + 1).trim().replace(/;$/, ""));
  const decale = source.filter(x => typeof d[x.en] === "string" && d[x.en].trim() && dico[x.en] !== d[x.en]).length;
  console.log(lg + " : " + (source.length - manque.length) + " / " + source.length + " ; " + defauts.length + " defaut(s) de variables ; " +
              (decale ? decale + " texte(s) ou " + lg + ".js n'est pas a jour (node outils/langues.js construire " + lg + ")" : lg + ".js a jour"));
  fautes += manque.length + defauts.length + decale;
}
console.log(fautes ? "\n" + fautes + " probleme(s)." : "\nOK : les " + ouvertes.length + " langues ouvertes sont completes.");
process.exitCode = fautes ? 1 : 0;
