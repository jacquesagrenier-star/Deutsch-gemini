// Les <script> inline d'une page de theme s'analysent-ils ? Sans navigateur, sans l'executer (aucun verrou necessaire).
//   node visuel/syntaxe_page.js visuel/prototype/gato.html [autres pages...]
// Ne dit rien de ce que la page affiche : les questions se relisent avec visuel/echantillon_theme.py (sous le verrou).
const fs = require("fs"), vm = require("vm");
let fautes = 0;
for (const f of process.argv.slice(2)) {
  const html = fs.readFileSync(f, "utf8");
  const blocs = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  blocs.forEach((code, n) => {
    try { new vm.Script(code, {filename: f + " #" + (n + 1)}); }
    catch (e) { fautes++; console.log("FAUTE  " + f + " bloc " + (n + 1) + " : " + e.message + "\n" + (e.stack || "").split("\n").slice(0, 3).join("\n")); }
  });
  console.log((fautes ? "" : "OK     ") + f + " : " + blocs.length + " bloc(s)");
}
process.exit(fautes ? 1 : 0);
