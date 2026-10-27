// Les cles d'interface presentes en francais et ABSENTES d'une autre langue,
// pour l'allemand ET pour l'espagnol.
//
//     node tests/cles_manquantes.js            le resume par langue
//     node tests/cles_manquantes.js --detail   chaque cle, avec ce qui s'affiche
//
// POURQUOI. t() suit REPLI_LANGUE : langue -> anglais -> francais. Une cle
// absente d'une langue ne casse rien et ne se voit dans aucun compteur : elle
// s'affiche en anglais, ou en FRANCAIS si l'anglais manque aussi. Le 27 oct.
// 2026, des captures App Store en anglais montraient encore du francais.
//
// L'ESPAGNOL A UN PIEGE DE PLUS. I18N_ESPAGNOL est verse PAR-DESSUS I18N, cle
// par cle et langue par langue. Une surcharge posee en francais et pas en
// anglais laisse l'anglais sur le texte ALLEMAND (« Learn German » dans l'app
// espagnole) : ni du francais, ni une cle absente, juste la mauvaise langue.
// D'ou la seconde mesure, « surcharge espagnole manquante ».
//
// Les cles de grammaire.json (allemand et espagnol) sont versees comme dans
// chargerCours(), pour mesurer ce que le navigateur lit vraiment.
const fs = require("fs"), path = require("path"), vm = require("vm");
const RACINE = path.join(__dirname, "..");
const src = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");

function bloc(nom){
    const d = src.indexOf("const " + nom + " = {");
    if(d < 0){ console.error("bloc introuvable : " + nom); process.exit(2); }
    const f = src.indexOf("\n};", d);
    const ctx = { r: null };
    vm.createContext(ctx);
    vm.runInContext(src.slice(d, f + 3).replace("const " + nom, "var " + nom) + "\nr = " + nom + ";", ctx);
    return ctx.r;
}

// Le repli tel que l'app le lit (REPLI_LANGUE), pas recopie ici.
const REPLI = (() => {
    const d = src.indexOf("const REPLI_LANGUE = {");
    const f = src.indexOf("};", d);
    const ctx = { r: null };
    vm.createContext(ctx);
    vm.runInContext(src.slice(d, f + 2).replace("const REPLI_LANGUE", "var REPLI_LANGUE") + "\nr = REPLI_LANGUE;", ctx);
    return ctx.r;
})();
const LANGUES = Object.keys(REPLI);
// L'espagnol n'est propose que dans ces langues (LANGUES_UI_AVEC_ESPAGNOL).
const AVEC_ES = (() => {
    const m = src.match(/const LANGUES_UI_AVEC_ESPAGNOL = (\[[^\]]*\])/);
    return m ? JSON.parse(m[1]) : LANGUES;
})();

function avecCours(dico, fichier){
    const out = {};
    for(const l of Object.keys(dico)) out[l] = Object.assign({}, dico[l]);
    const p = path.join(RACINE, fichier);
    if(fs.existsSync(p)){
        const textes = JSON.parse(fs.readFileSync(p, "utf8")).textes || {};
        for(const l of Object.keys(textes)) if(out[l]) Object.assign(out[l], textes[l]);
    }
    return out;
}

const I18N = bloc("I18N");
const ES = bloc("I18N_ESPAGNOL");
const de = avecCours(I18N, "grammaire.json");
const es = avecCours(I18N, "espanol/datos/grammaire.json");
for(const l of Object.keys(ES)) if(es[l]) Object.assign(es[l], ES[l]);

function resoudre(dico, lang, cle){
    for(const c of REPLI[lang]) if(dico[c] && dico[c][cle] !== undefined) return c;
    return null;
}

const detail = process.argv.includes("--detail");
let total = 0;
for(const [nom, dico, langues] of [["allemand", de, LANGUES], ["espagnol", es, AVEC_ES]]){
    console.log("\n== " + nom + " (" + Object.keys(dico.fr).length + " cles en francais)");
    for(const lang of langues){
        if(lang === "fr") continue;
        const absentes = Object.keys(dico.fr).filter(k => dico[lang][k] === undefined);
        const enFr = absentes.filter(k => resoudre(dico, lang, k) === "fr");
        console.log("  " + lang + " : " + absentes.length + " absente(s), dont " + enFr.length + " affichee(s) en FRANCAIS");
        total += enFr.length;
        if(detail) for(const k of enFr) console.log("      " + k + " = " + JSON.stringify(dico.fr[k]).slice(0, 110));
    }
}

// La surcharge espagnole : posee en francais, absente d'une langue ou
// l'espagnol est propose -> cette langue garde le texte de l'allemand.
console.log("\n== surcharge espagnole (I18N_ESPAGNOL) manquante");
let surcharge = 0;
for(const lang of AVEC_ES){
    if(lang === "fr") continue;
    const manque = Object.keys(ES.fr).filter(k => !(ES[lang] && ES[lang][k] !== undefined)
        && !(lang !== "en" && ES.en && ES.en[k] !== undefined && !(I18N[lang] && I18N[lang][k] !== undefined)));
    console.log("  " + lang + " : " + manque.length);
    surcharge += manque.length;
    if(detail) for(const k of manque) console.log("      " + k + " = " + JSON.stringify(ES.fr[k]).slice(0, 110));
}
// Une cle PRESENTE mais dont la valeur est le francais recopie : aucun compteur
// ne la voit (« 🔁 Sens : FR → DE » en anglais, trouve le 27 oct. 2026).
// Un texte identique partout n'est signale que s'il porte un marqueur francais :
// « A1 », « Akkusativ » ou un nom propre sont les memes dans toutes les langues.
const FR = /[èêàçùâîôûœéë]|(?<![\p{L}'’])(?:le|les|des|du|au|aux|et|est|pour|avec|dans|sur|pas|tu|ton|ta|tes|ce|cette|je|mots?|cartes?|une?|sens)(?![\p{L}'’])/iu;
// L'espagnol cite ses propres exemples (« lo · la · le », « hablé ») : ni
// l'accent aigu ni « le » n'y trahissent le francais.
const FR_ES = /[èêàçùâîôûœë]|(?<![\p{L}'’])(?:les|des|du|au|aux|et|est|pour|avec|dans|sur|pas|ton|tes|ce|cette|je|mots?|cartes?|une|sens)(?![\p{L}'’])/iu;
console.log("\n== valeurs recopiees du francais");
let copies = 0;
for(const [nom, dico] of [["allemand", de], ["espagnol", es]]){
    for(const lang of LANGUES){
        if(lang === "fr" || !dico[lang]) continue;
        const k = Object.keys(dico.fr).filter(c => typeof dico.fr[c] === "string" && dico[lang][c] === dico.fr[c]
            && (nom === "espagnol" ? FR_ES : FR).test(dico.fr[c].replace(/<[^>]*>/g, "")));
        if(!k.length) continue;
        console.log("  " + nom + " " + lang + " : " + k.length);
        copies += k.length;
        if(detail) for(const c of k) console.log("      " + c + " = " + JSON.stringify(dico.fr[c]).slice(0, 110));
    }
}
console.log("\n" + total + " cle(s) affichee(s) en francais, " + surcharge + " surcharge(s) espagnole(s) manquante(s), "
    + copies + " valeur(s) recopiee(s) du francais.");
process.exit(total || surcharge || copies ? 1 : 0);
