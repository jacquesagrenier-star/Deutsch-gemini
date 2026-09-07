// Sort le bloc I18N d'index.html en JSON, en l'EVALUANT au lieu de le lire a
// coups d'expressions regulieres. Une cle ecrite apres une virgule sur la meme
// ligne, une chaine sur trois lignes, un gabarit `...` : tout ce qui fait
// echouer un decoupage textuel passe ici sans effort, et c'est exactement ce
// que le navigateur lira.
//
//     node tests/i18n_dump.js            > i18n.json
//     node tests/i18n_dump.js fr en      seulement ces langues
const fs = require("fs"), path = require("path"), vm = require("vm");
const src = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");
const d = src.indexOf("const I18N = {");
if(d < 0){ console.error("bloc I18N introuvable"); process.exit(2); }
const f = src.indexOf("\n};", d);
const bloc = src.slice(d, f + 3);
const ctx = { resultat: null };
vm.createContext(ctx);
vm.runInContext(bloc + "\nresultat = I18N;", ctx);
const veut = process.argv.slice(2);
const out = {};
for(const [lang, obj] of Object.entries(ctx.resultat)){
    if(veut.length && !veut.includes(lang)) continue;
    out[lang] = obj;
}
process.stdout.write(JSON.stringify(out, null, 1));
