// Sort l'allemand des VERBES DE POSITION (« legen ou liegen ? »), en EVALUANT
// le code d'index.html au lieu de le relire a coups d'expressions regulieres
// -- meme procede que tests/phrases_articles.js, et pour la meme raison : ce
// qu'on obtient est exactement ce que le navigateur fabrique.
//
//     node tests/phrases_positionsverben.js            un texte par ligne
//     node tests/phrases_positionsverben.js --json     avec le detail
//
// POURQUOI CE SCRIPT EXISTE. Ces huit verbes (stehen/stellen, liegen/legen,
// sitzen/setzen, haengen/haengen) ne sont pas dans verbe.json : ils vivent en
// dur dans index.html (`positionsverbenTheme`), donc audio/manifest.py ne les
// voyait pas. La plupart de leurs phrases doublent par chance verbe.json ; les
// sept autres (« Ich sitze auf dem Stuhl. »...) n'ont jamais eu de mp3 et
// sortaient a la voix du telephone. Audit du 12 octobre 2026.
//
// Ce qu'on sort est ce que la carte prononce (branche 'positionsverben' de
// loadFlashcard) : l'infinitif, puis les trois phrases qui ont chacune leur
// bouton haut-parleur -- exemple (Praesens), perfekt, praeteritum.
const fs = require("fs"), path = require("path"), vm = require("vm");

const src = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

// UNE SEULE TRANCHE CONTINUE : de la declaration jusqu'a sa fermeture, la
// premiere ligne « }; » qui suit. Si le bloc bouge, le script s'arrete au
// lieu de sortir une liste incomplete.
const DEBUT = "const positionsverbenTheme = {";
const FIN = "\n};";
const d = src.indexOf(DEBUT);
const f = d < 0 ? -1 : src.indexOf(FIN, d);
if (d < 0 || f < 0) {
    console.error("Le bloc positionsverbenTheme n'a pas les bornes attendues.");
    console.error("  debut trouve : " + (d >= 0) + ", fin trouvee : " + (f >= 0));
    process.exit(2);
}
const tranche = src.slice(d, f + FIN.length);

const ctx = {};
vm.createContext(ctx);
vm.runInContext(tranche, ctx);
const verbes = vm.runInContext("positionsverbenTheme.words", ctx);

if (!Array.isArray(verbes) || !verbes.length) {
    console.error("ARRET : positionsverbenTheme.words est vide.");
    process.exit(1);
}
const CHAMPS = ["infinitif", "exemple", "perfekt", "praeteritum"];
const incomplets = verbes.filter(v => CHAMPS.some(c => !v[c]));
if (incomplets.length) {
    console.error("ARRET : " + incomplets.length + " verbe(s) de position sans l'un des champs "
        + CHAMPS.join(", ") + ".");
    console.error("   " + JSON.stringify(incomplets[0].infinitif));
    process.exit(1);
}

const textes = [];
for (const v of verbes) {
    for (const c of CHAMPS) {
        if (!textes.includes(v[c])) textes.push(v[c]);
    }
}
if (process.argv.includes("--json")) {
    process.stdout.write(JSON.stringify(
        { verbes: verbes.length, textes: textes }, null, 1));
} else {
    process.stdout.write(textes.join("\n") + "\n");
}
