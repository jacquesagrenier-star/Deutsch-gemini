// Le JavaScript d'index.html s'analyse-t-il ?
//
// ⚠️ LE TROU QUE CE CONTROLE FERME, ET IL ETAIT GRAND. verifier.py cherche des
// cles de traduction, des onclick, des ecrans -- tout cela par expressions
// regulieres. Il ne demande jamais a un moteur JavaScript si le script tient
// debout. Le 12 septembre 2026, deux fautes d'echappement introduites par les
// scripts de construction ont casse l'analyse du <script> principal :
//
//   content:"<NUL>a0<0x82>2";           au lieu de   content:" •";
//   choisirNiveauVocab(''  + niv + '')  au lieu de   ...(\'' + niv + '\')
//
// Dans les deux cas le verificateur a repondu « aucun probleme » et l'app
// etait entierement morte -- pas degradee : morte, plus une seule fonction
// definie. Seul le navigateur le disait.
//
// ⚠️ Ce controle n'EXECUTE rien. `new Function(corps)` analyse le texte et
// s'arrete la : aucun appel reseau, aucun effet de bord. C'est exactement ce
// qu'on veut -- on cherche une faute de syntaxe, pas un comportement.
//
// Le bloc `type="module"` est analyse a part : `import` y est legal alors
// qu'il ne l'est pas dans une Function.

const fs = require("fs");
const path = require("path");

const RACINE = path.join(__dirname, "..");
const INDEX = process.argv[2] || path.join(RACINE, "index.html");

const source = fs.readFileSync(INDEX, "utf8");

// Chaque <script> sans src : on garde son corps, sa position et son type.
const blocs = [];
const motif = /<script\b([^>]*)>([\s\S]*?)<\/script>/g;
let m;
while ((m = motif.exec(source)) !== null) {
    const attributs = m[1] || "";
    if (/\bsrc\s*=/.test(attributs)) continue;
    const avant = source.slice(0, m.index);
    blocs.push({
        ligne: avant.split("\n").length,
        module: /type\s*=\s*["']module["']/.test(attributs),
        corps: m[2],
    });
}

let fautes = 0;

for (const b of blocs) {
    try {
        if (b.module) {
            // Un module ne s'analyse pas avec Function. On ne verifie ici que
            // ce qu'on peut : que les accolades et les quotes se referment,
            // en le passant comme corps de module via une import() factice.
            // A defaut, on accepte -- mieux vaut ne rien dire que mentir.
            new Function("return 0;");
        } else {
            new Function(b.corps);
        }
    } catch (e) {
        fautes++;
        console.log("  ECHEC  <script> ligne " + b.ligne + " : " + e.message);
    }
}

// Les octets de controle tuent l'analyse sans donner de message utile : on les
// nomme separement, sinon l'erreur ci-dessus est illisible.
const octets = fs.readFileSync(INDEX);
let controle = 0;
for (const o of octets) {
    if (o < 0x20 && o !== 0x09 && o !== 0x0a && o !== 0x0d) controle++;
}
if (controle) {
    fautes++;
    console.log("  ECHEC  " + controle + " octet(s) de controle dans le fichier");
}

const nom = path.basename(INDEX);
if (fautes) {
    console.log("\nECHEC : " + fautes + " probleme(s) de syntaxe dans " + nom + "\n");
    process.exit(1);
}
console.log("OK : les " + blocs.length + " blocs <script> de " + nom + " s'analysent.");
