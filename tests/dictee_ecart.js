// LA CORRECTION DE LA DICTEE DE PHRASE, MOT PAR MOT (7 nov. 2026)
//
// Retour d'un utilisateur (journal-retours, 30bf8a0) : dans « Trabajo con la computadora en casa », il avait ecrit
// « computatora » ; « Trabajo », juste, etait souligne, et tout le retour etait rouge. Ce test lit les fonctions dans
// index.html (alignerDictee, lettresCorrigees, distanceMots, normaliserSaisie, echapperHtml) et verifie :
//  - un mot juste n'est jamais marque ;
//  - un mot oublie ou en trop ne decale pas le reste ;
//  - un mot de quatre lettres ou plus a une lettre pres compte juste (« Presque ! ») ;
//  - les lettres corrigees, et elles seules, sont en gras.
//
//   node tests/dictee_ecart.js

const fs = require("fs");
const path = require("path");
const src = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

function extraire(nom){
    const i = src.indexOf("function " + nom + "(");
    if(i < 0) throw new Error("fonction introuvable : " + nom);
    let k = src.indexOf("{", i), prof = 0;
    for(; k < src.length; k++){
        if(src[k] === "{") prof++;
        else if(src[k] === "}"){ prof--; if(prof === 0) break; }
    }
    return src.slice(i, k + 1);
}
const constante = (nom) => {
    const m = src.match(new RegExp("const " + nom + " = [^;]+;"));
    if(!m) throw new Error("constante introuvable : " + nom);
    return m[0];
};
const code = [constante("DICTEE_MOT_TOLERE"), "const t = k => k;",
    ...["normaliserSaisie", "echapperHtml", "distanceMots", "formeAccents", "accentFaitUnAutreMot", "alignerDictee", "lettresCorrigees"].map(extraire),
    "module.exports = { alignerDictee, lettresCorrigees };"].join("\n");
const m = { exports: {} };
new Function("module", code)(m);
const { alignerDictee, lettresCorrigees } = m.exports;

let echecs = 0;
function verifier(nom, ok, detail){
    console.log((ok ? "OK    " : "ECHEC ") + nom + (ok ? "" : "  -- " + detail));
    if(!ok) echecs++;
}
const types = al => al.paires.map(p => p.t).join(" ");

// 1. La phrase du retour, telle quelle.
const ATTENDU = "Trabajo con la computadora en casa.";
let al = alignerDictee("Trabajo con la computatora en casa", ATTENDU);
verifier("« Trabajo » n'est pas marque", al.paires[0].t === "juste" && al.paires[0].s === "Trabajo", types(al));
verifier("seul « computatora » est apparie a « computadora », a une lettre pres",
    types(al) === "juste juste juste presque juste juste" && al.paires[3].s === "computatora" && al.paires[3].a === "computadora", types(al));
verifier("une lettre pres sur un long mot : compte juste, « Presque ! »", al.juste && al.presque, JSON.stringify(al));
verifier("la correction met en gras le d, et lui seul", lettresCorrigees("computatora", "computadora") === "computa<b>d</b>ora",
    lettresCorrigees("computatora", "computadora"));

// 2. Un mot oublie : le reste ne se decale pas.
al = alignerDictee("Trabajo la computadora en casa", ATTENDU);
verifier("mot oublie : « con » manque, les autres sont justes", types(al) === "juste manque juste juste juste juste", types(al));
verifier("mot oublie : ne compte pas juste", !al.juste, JSON.stringify(al));

// 3. Un mot en trop : le reste ne se decale pas.
al = alignerDictee("Trabajo con la nueva computadora en casa", ATTENDU);
verifier("mot en trop : « nueva » en trop, les autres sont justes", types(al) === "juste juste juste trop juste juste juste", types(al));
verifier("mot en trop : ne compte pas juste", !al.juste, JSON.stringify(al));

// 4. Deux fautes sur un mot : faux, et seulement lui.
al = alignerDictee("Trabajo con la conputatora en casa", ATTENDU);
verifier("deux lettres de travers : faux, le reste juste", types(al) === "juste juste juste faux juste juste", types(al));
verifier("les deux lettres corrigees en gras", lettresCorrigees("conputatora", "computadora") === "co<b>m</b>puta<b>d</b>ora",
    lettresCorrigees("conputatora", "computadora"));

// 5. Un mot court a une lettre pres reste faux : « la » et « le » sont deux mots.
al = alignerDictee("Trabajo con le computadora en casa", ATTENDU);
verifier("mot de moins de quatre lettres : faux", types(al) === "juste juste faux juste juste juste" && !al.juste, types(al));

// 6. L'allemand : casse, accents, ß et ponctuation ne comptent pas.
al = alignerDictee("ich weiss nicht, wo die strasse ist", "Ich weiß nicht, wo die Straße ist.");
verifier("allemand : ß et majuscules ignores, tout juste", types(al) === "juste juste juste juste juste juste juste", types(al));
al = alignerDictee("Ich habe heute keine Zeit", "Ich habe heute keine Zeit mehr.");
verifier("allemand : mot oublie en fin de phrase", types(al) === "juste juste juste juste juste manque", types(al));

// 7. La garde du rappel actif : un autre vrai mot du corpus n'est pas une faute de frappe.
const CORPUS = { plies: new Set(["casa", "cosa", "mesa", "mutter"]), formes: new Set(["casa", "cosa", "mesa", "mutter", "mütter", "esta", "está", "masse", "maße", "el", "él", "schon", "schön"]) };
al = alignerDictee("Trabajo con la computadora en cosa", ATTENDU, { autres: CORPUS, langue: "es" });
verifier("« cosa » pour « casa » : un autre vrai mot, faux", types(al) === "juste juste juste juste juste faux" && !al.juste, types(al));
al = alignerDictee("Trabajo con la computatora en casa", ATTENDU, { autres: CORPUS, langue: "es" });
verifier("« computatora » n'est pas un mot du corpus : toujours « Presque ! »", al.juste && al.presque, types(al));
al = alignerDictee("Die Mutter sind hier", "Die Mütter sind hier.", { autres: CORPUS, langue: "de" });
verifier("« Mutter » pour « Mütter » (un autre mot) : faux, le ü en gras",
    types(al) === "juste faux juste juste" && !al.juste && lettresCorrigees("Mutter", "Mütter", al.paires[1].umlaut) === "M<b>ü</b>tter",
    types(al) + " " + lettresCorrigees("Mutter", "Mütter", al.paires[1].umlaut));
al = alignerDictee("Ich bin mude", "Ich bin müde.", { autres: CORPUS, langue: "de" });
verifier("« mude » pour « müde » (pas un autre mot) : l'accent ne compte pas, juste", types(al) === "juste juste juste" && al.juste, types(al));

// 8. Le corpus de la garde prend aussi les mots des phrases d'exemple (decision du chef, 7 nov.) : « cosa » n'est pas
// une entree du vocabulaire espagnol, mais il est dans ses phrases. motsDuCorpusDictee tel qu'il est dans index.html,
// avec des donnees de remplacement.
const codeCorpus = [constante("DICTEE_MOT_TOLERE"),
    "let MOTS_CORPUS_DICTEE = null, themesLoaded = true;",
    "const themesComptes = () => [{ levels: { A1: { words: [['casa', 'maison', 'la casa es grande', '', '', '', '', '', '']] } } }];",
    "const verbeTheme = { words: [] }, adjektiveTheme = { words: [] }, praepTheme = null, adverbienTheme = null, konjunktionenTheme = null;",
    "const phrasesTraduisibles = () => [{ de: 'Es una cosa importante.', fr: \"C'est une chose importante.\" }];",
    ...["normaliserSaisie", "formeAccents", "motsDuCorpusDictee"].map(extraire),
    "module.exports = { motsDuCorpusDictee };"].join("\n");
const mc = { exports: {} };
new Function("module", codeCorpus)(mc);
const corpusPhrases = mc.exports.motsDuCorpusDictee();
verifier("le corpus prend « cosa » dans une phrase d'exemple", corpusPhrases.plies.has("cosa") && corpusPhrases.plies.has("casa"),
    [...corpusPhrases.plies].join(","));
al = alignerDictee("Trabajo con la computadora en cosa", ATTENDU, { autres: corpusPhrases, langue: "es" });
verifier("« cosa » pour « casa », corpus des phrases : faux", types(al) === "juste juste juste juste juste faux" && !al.juste, types(al));

// 9. La regle commune (8 nov. 2026, ligne 27) : un accent oublie est accepte, sauf s'il donne un autre vrai mot.
al = alignerDictee("Ella esta aqui", "Ella está aquí.", { autres: CORPUS });
verifier("« esta » pour « está » : un autre mot, faux ; « aqui » : pas un autre mot, juste", types(al) === "juste faux juste" && !al.juste, types(al));
verifier("la lettre accentuee en gras", lettresCorrigees("esta", "está", al.paires[1].umlaut) === "est<b>á</b>", lettresCorrigees("esta", "está", al.paires[1].umlaut));
al = alignerDictee("El vive aqui", "Él vive aquí.", { autres: CORPUS });
verifier("un mot de deux lettres compte : « el » pour « él », faux", types(al) === "faux juste juste", types(al));
al = alignerDictee("Das ist schon", "Das ist schön.", { autres: CORPUS });
verifier("« schon » pour « schön » : faux", types(al) === "juste juste faux", types(al));
al = alignerDictee("Die Masse", "Die Maße.", { autres: CORPUS });
verifier("« Masse » pour « Maße » (un autre mot) : faux", types(al) === "juste faux", types(al));
al = alignerDictee("die strasse", "die Straße", { autres: CORPUS });
verifier("« strasse » pour « Straße » (pas un autre mot) : juste", types(al) === "juste juste" && al.juste, types(al));
al = alignerDictee("Ella está", "Ella está.", { autres: CORPUS });
verifier("l'accent ecrit : juste", al.juste && !al.presque, types(al));
verifier("sans corpus : pas de garde", alignerDictee("esta", "está").juste, "");

console.log(echecs ? "\n" + echecs + " echec(s)." : "\nTout passe.");
process.exit(echecs ? 1 : 0);
