// Le rappel actif des cartes (essai « rappel_actif », 6 nov. 2026) : le choix de
// la forme, la regle « une sur trois », les leurres et la tolerance de la saisie.
//
//   node tests/rappel_actif.js
//
// Aucun navigateur, aucun verrou : la logique vit entre deux marques dans
// index.html (« RAPPEL ACTIF : LOGIQUE PURE (debut) » ... « (fin) »), sans DOM ni
// stockage. On l'extrait, on l'execute dans un bac a sable, et on la passe :
//   1. sur des cas ecrits a la main (les regles de la maquette, une par une) ;
//   2. sur TOUT le corpus allemand et espagnol des noms, verbes et adjectifs :
//      chaque mot tape juste est juste, sans article aussi, sans accent
//      « presque » ; et les leurres d'une carte ne sont jamais la bonne reponse
//      sous une autre forme (meme mot, meme sens, autre genre).

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const RACINE = path.join(__dirname, "..");
const source = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");
const DEBUT = "// ---- RAPPEL ACTIF : LOGIQUE PURE (debut) ----";
const FIN = "// ---- RAPPEL ACTIF : LOGIQUE PURE (fin) ----";
const a = source.indexOf(DEBUT), b = source.indexOf(FIN);
if(a < 0 || b < a){ console.error("ECHEC : les marques de la logique pure sont introuvables dans index.html"); process.exit(1); }
const ctx = {};
vm.createContext(ctx);
// Les « const » d'un script ne deviennent pas des proprietes du contexte : on
// les exporte a la main.
vm.runInContext(source.slice(a, b) + "\n;this.R = { RAPPEL_ECART, RAPPEL_ARTICLES, RAPPEL_TOUCHES, empreinteRappel, dejaVuRappel, pointsRappel, formeSelonPoints, tourDuRappel, normRappel, plierRappel, sensPlieRappel, distanceRappel, jugerSaisieRappel, ecartLettresRappel, leurresDejaVus, ordreDesChoix };", ctx);
const R = ctx.R;

let ok = 0, ko = 0;
const fautes = [];
function verifier(cond, msg){
    if(cond) ok++;
    else { ko++; if(fautes.length < 40) fautes.push(msg); }
}
function egal(x, y, msg){ verifier(x === y, msg + " -- attendu " + JSON.stringify(y) + ", obtenu " + JSON.stringify(x)); }

// ---------- 1. La forme selon les points ----------
egal(R.formeSelonPoints(0, "t:1"), "choisir", "0 point (vu, rate) -> choisir");
egal(R.formeSelonPoints(1, "t:1"), "choisir", "1 point -> choisir");
egal(R.formeSelonPoints(3, "t:1"), "taper", "3 points -> taper");
egal(R.formeSelonPoints(4, "t:1"), "taper", "maitrise -> taper");
{
    const f = new Set();
    for(let i = 0; i < 200; i++){
        const x = R.formeSelonPoints(2, "theme:" + i);
        f.add(x);
        egal(R.formeSelonPoints(2, "theme:" + i), x, "2 points : la meme carte donne toujours la meme forme");
    }
    verifier(f.has("choisir") && f.has("taper"), "2 points : les deux formes existent");
}
egal(R.pointsRappel({ srsHits: 2 }), 2, "points = srsHits");
egal(R.pointsRappel({ srsHits: 1, mastered: true }), 4, "maitrise = 4 points");
egal(R.dejaVuRappel({ mastered: false, due: 0, reviews: 0 }), false, "un mot jamais juge n'est pas vu");
egal(R.dejaVuRappel({ srsHits: 0, due: 123 }), true, "un mot rate (Encore) est vu");
// « Vu » = le contraire exact d'estNeuf(), la definition du reste de l'app (le
// lot des petites ameliorations classe ses leurres de phrases dessus).
{
    const m = source.match(/function estNeuf\(st\)\{[\s\S]*?\r?\n\}/);
    verifier(!!m, "estNeuf() introuvable dans index.html");
    if(m){
        const estNeuf = vm.runInNewContext("(" + m[0] + ")");
        [{}, { mastered: false, due: 0, reviews: 0 }, { srsHits: 1 }, { due: 5 }, { mastered: true },
         { reviews: 2 }, { srsHits: 0, due: 0, reviews: 4 }, { srsHits: 3, srsDailyStreak: 2, due: 9 }]
            .forEach(st => egal(R.dejaVuRappel(st), !estNeuf(Object.assign({}, st)), "vu = !estNeuf pour " + JSON.stringify(st)));
    }
}

// ---------- 2. Une carte sur trois, par regle ----------
function jouer(eligibles, possibles){
    let depuis = R.RAPPEL_ECART;
    return eligibles.map((e, i) => {
        const r = R.tourDuRappel(depuis, e, possibles ? possibles[i] : true);
        depuis = r.depuis;
        return r.active ? 1 : 0;
    }).join("");
}
egal(jouer([1,1,1,1,1,1,1,1,1].map(Boolean)), "100100100", "neuf cartes eligibles : la 1re, la 4e, la 7e");
egal(jouer([0,1,0,1,1,0,1,1,1].map(Boolean)), "010000100", "les cartes neuves ne comptent pas dans le tour");
egal(jouer([1,1,1,1,1].map(Boolean), [false, true, true, true, true]), "01001", "pas de leurres : la suivante prend le tour");
egal(jouer([1,1,1,1,1,1].map(Boolean)), jouer([1,1,1,1,1,1].map(Boolean)), "deux passages donnent le meme resultat");

// ---------- 3. La tolerance de la saisie ----------
const DE = { langue: "de", mode: "nomen", article: "der", autres: new Set(["tasche", "mehr"]) };
const j = (saisi, mot, o) => R.jugerSaisieRappel(saisi, mot, o);
egal(j("der Schlüssel", "Schlüssel", DE).verdict, "juste", "avec le bon article");
egal(j("schlüssel", "Schlüssel", DE).verdict, "juste", "sans article ni majuscule");
egal(j("  Der   Schlüssel. ", "Schlüssel", DE).verdict, "juste", "espaces et point ignores");
egal(j("der Schlussel", "Schlüssel", DE).raison, "accent", "umlaut oublie -> presque (accent)");
egal(j("der Schluessel", "Schlüssel", DE).verdict, "presque", "ue pour ü -> presque");
egal(j("die Schlüssel", "Schlüssel", DE).raison, "article", "mauvais article -> presque (article)");
egal(j("die Schlüssel", "Schlüssel", DE).verdict, "presque", "mauvais article compte juste");
egal(j("der Schlüsel", "Schlüssel", DE).raison, "frappe", "une lettre en moins -> frappe");
egal(j("der Shclüssel", "Schlüssel", DE).raison, "frappe", "deux lettres inversees -> frappe");
egal(j("der Tisch", "Schlüssel", DE).verdict, "faux", "un autre mot -> faux");
egal(j("Tasse", "Tasche", { langue: "de", mode: "nomen", article: "die", autres: new Set(["tasse"]) }).raison, "autre",
     "Tasse pour Tasche : un autre mot connu, pas une faute de frappe");
egal(j("Tasse", "Tasche", { langue: "de", mode: "nomen", article: "die", autres: new Set() }).verdict, "faux",
     "Tasse pour Tasche : deux lettres sur six, c'est faux");
egal(j("Bad", "Bus", { langue: "de", mode: "nomen", article: "der" }).verdict, "faux", "mot court : aucune faute de frappe admise");
egal(j("sehr", "mehr", { langue: "de", mode: "adjektive", autres: new Set(["sehr"]) }).raison, "autre", "sehr pour mehr : autre mot");
egal(j("Strasse", "Straße", { langue: "de", mode: "nomen", article: "die" }).raison, "accent", "ss pour ß -> accent");
egal(j("freuen", "sich freuen", { langue: "de", mode: "verben" }).raison, "sich", "verbe sans sich -> presque");
egal(j("sich freuen", "sich freuen", { langue: "de", mode: "verben" }).verdict, "juste", "verbe avec sich -> juste");
egal(j("schuld", "schuld (sein)", { langue: "de", mode: "adjektive" }).verdict, "juste", "parenthese facultative");
egal(j("Stuhl", "Sessel", { langue: "de", mode: "nomen", article: "der", synonymes: ["Stuhl"] }).raison, "synonyme",
     "un mot de meme sens compte juste");
egal(j("", "Tisch", DE).verdict, "vide", "rien de tape");
const ES = { langue: "es", mode: "nomen", article: "la", autres: new Set() };
egal(j("la llave", "llave", ES).verdict, "juste", "es : avec l'article");
egal(j("llave", "llave", ES).verdict, "juste", "es : sans l'article");
egal(j("la yave", "llave", ES).raison, "son", "es : la yave -> meme son (ll = y)");
egal(j("la yave", "llave", ES).verdict, "presque", "es : la yave compte juste");
egal(j("la bentana", "ventana", ES).raison, "son", "es : b pour v -> meme son");
egal(j("el zapato", "zapato", { langue: "es", mode: "nomen", article: "el" }).verdict, "juste", "es : zapato");
egal(j("la vaca", "baca", { langue: "es", mode: "nomen", article: "la", autres: new Set(["vaca"]) }).raison, "autre", "es : un autre mot connu de meme son reste faux");
egal(j("ablar", "hablar", { langue: "es", mode: "verben" }).raison, "son", "es : h muet oublie -> meme son");
egal(j("el llave", "llave", ES).raison, "article", "es : el pour la -> article");
egal(j("la nina", "niña", { langue: "es", mode: "nomen", article: "la" }).raison, "accent", "es : n pour ñ -> accent");
egal(j("la cancion", "canción", { langue: "es", mode: "nomen", article: "la" }).raison, "accent", "es : accent oublie");
egal(j("levantarse", "levantarse", { langue: "es", mode: "verben" }).verdict, "juste", "es : verbe pronominal");
egal(j("la mano", "mano", { langue: "es", mode: "nomen", article: "la" }).verdict, "juste", "es : la mano");
egal(j("das Baby", "Baby", { langue: "de", mode: "nomen", article: "das" }).verdict, "juste", "das");
egal(j("das Joghurt", "Joghurt", { langue: "de", mode: "nomen", article: "der/das" }).verdict, "juste", "der/das : les deux articles");
egal(j("die Eltern", "Eltern", { langue: "de", mode: "nomen", article: "die (Pl.)" }).verdict, "juste", "die (Pl.)");
{
    const e = R.ecartLettresRappel("la yave", "la llave").filter(x => x.diff).map(x => x.c).join("");
    egal(e, "ll", "l'ecart souligne le « ll » de « llave »");
    const e2 = R.ecartLettresRappel("der Schlussel", "der Schlüssel").filter(x => x.diff).map(x => x.c).join("");
    egal(e2, "ü", "l'ecart souligne le ü");
}

// ---------- 4. Les leurres ----------
// Une carte : { themeId, index, mode, word: [mot, genre, pluriel, sens, ..., [8] autre genre] }
function nom(th, i, mot, genre, sens, vu, paire){
    const w = [mot, genre, "", sens]; w[8] = paire || "";
    return { themeId: th, index: i, mode: "nomen", word: w, _vu: vu, _sens: sens };
}
const dep = {
    etat: it => it._vu ? { srsHits: 1, due: 1 } : { mastered: false, due: 0, reviews: 0 },
    reponse: it => it.mode === "nomen" ? (it.word[1] + " " + it.word[0]) : (it.word.infinitif || it.word[0]),
    sens: it => it._sens,
    mode: it => it.mode
};
{
    const cible = nom("hotel", 1, "Schlüssel", "der", "la clé", true);
    const pool = [
        cible,
        nom("hotel", 2, "Handtuch", "das", "la serviette", true),
        nom("hotel", 3, "Aufzug", "der", "l'ascenseur", true),
        nom("hotel", 4, "Rezeption", "die", "la réception", false),        // jamais vu
        nom("bureau", 5, "Schlüssel", "der", "la clé", true),              // le meme mot ailleurs
        nom("bureau", 6, "Taste", "die", "la clé", true),                  // meme sens (la touche / la clé)
        nom("ville", 7, "Bahnhof", "der", "la gare", true),
        { themeId: "verbes", index: 8, mode: "verben", word: { infinitif: "gehen" }, _vu: true, _sens: "aller" }
    ];
    const l = R.leurresDejaVus(cible, pool, 2, dep);
    egal(l.length, 2, "deux leurres");
    egal(l.map(x => x.texte).sort().join(" | "), "das Handtuch | der Aufzug", "le meme lieu d'abord, deja vus seulement");
    verifier(!l.some(x => /Rezeption|Taste|gehen|Schlüssel/.test(x.texte)), "ni jamais vu, ni meme sens, ni autre categorie, ni meme mot");
    egal(JSON.stringify(R.leurresDejaVus(cible, pool, 2, dep)), JSON.stringify(l), "les leurres ne changent pas d'un appel a l'autre");
    const sansLieu = pool.filter(x => x.themeId !== "hotel" || x === cible);
    const l2 = R.leurresDejaVus(cible, sansLieu, 2, dep);
    egal(l2.map(x => x.texte).join(" | "), "der Bahnhof", "un seul leurre possible (les autres sont meme mot ou meme sens)");
    const arzt = nom("metier", 1, "Arzt", "der", "le médecin", true, "Ärztin");
    const l3 = R.leurresDejaVus(arzt, [arzt, nom("metier", 2, "Ärztin", "die", "la médecin (femme)", true, "Arzt"),
                                       nom("metier", 3, "Lehrer", "der", "le professeur", true)], 2, dep);
    egal(l3.map(x => x.texte).join(" | "), "der Lehrer", "l'autre genre d'un nom de personne n'est jamais un leurre");
    const ch = R.ordreDesChoix("hotel:1", "der Schlüssel", l);
    egal(ch.length, 3, "trois choix");
    egal(ch.filter(c => c.juste).length, 1, "un seul juste");
    egal(JSON.stringify(R.ordreDesChoix("hotel:1", "der Schlüssel", l)), JSON.stringify(ch), "l'ordre des choix est fixe");
}

// ---------- 5. Tout le corpus ----------
function corpus(fichierThemes, fichierVerbes, fichierAdj, langue){
    const cartes = [];
    const th = JSON.parse(fs.readFileSync(path.join(RACINE, fichierThemes), "utf8")).themes;
    th.forEach(t => (t.mots || []).forEach((m, i) => {
        const w = [m.mot, m.genre || "", m.pluriel || "", m.traduction || ""];
        w[8] = m.feminin || m.masculin || "";
        cartes.push({ themeId: t.id, index: i, mode: "nomen", word: w, _vu: true, _sens: (m.article_fr || "") + (m.traduction || "") });
    }));
    const marcher = (x, f) => { if(Array.isArray(x)) x.forEach(y => marcher(y, f)); else if(x && typeof x === "object"){ if(f(x) === false) return; Object.values(x).forEach(y => marcher(y, f)); } };
    let iv = 0, ia = 0;
    marcher(JSON.parse(fs.readFileSync(path.join(RACINE, fichierVerbes), "utf8")), x => {
        if(!x.infinitif) return;
        cartes.push({ themeId: "verben", index: iv++, mode: "verben", word: { infinitif: x.infinitif }, _vu: true, _sens: x.traduction || "" });
        return false;
    });
    marcher(JSON.parse(fs.readFileSync(path.join(RACINE, fichierAdj), "utf8")), x => {
        if(!x.mot) return;
        if(!/\//.test(x.mot)) cartes.push({ themeId: "adjektive", index: ia++, mode: "adjektive", word: [x.mot], _vu: true, _sens: x.traduction || "" });
        return false;
    });
    let n = 0, nl = 0, choixManquants = 0;
    const parMode = {};
    cartes.forEach(c => { (parMode[c.mode] = parMode[c.mode] || []).push(c); });
    cartes.forEach(c => {
        const mot = c.mode === "verben" ? c.word.infinitif : c.word[0];
        if(!mot || !String(mot).trim()) return;
        n++;
        const o = { langue: langue, mode: c.mode, article: c.mode === "nomen" ? c.word[1] : "" };
        const tout = c.mode === "nomen" && c.word[1] ? c.word[1].split(/[\/\s]/)[0] + " " + mot : mot;
        egal(R.jugerSaisieRappel(tout, mot, o).verdict, "juste", langue + " : « " + tout + " » tape juste");
        egal(R.jugerSaisieRappel(mot, mot, o).verdict, "juste", langue + " : « " + mot + " » sans article");
        // (« ß ».toUpperCase() donne « SS » : ce cas-la est un « presque », vu plus haut.)
        if(!/ß/.test(mot)) egal(R.jugerSaisieRappel(String(mot).toUpperCase(), mot, o).verdict, "juste", langue + " : « " + mot + " » en majuscules");
        const plie = String(mot).replace(/ß/g, "ss").normalize("NFD").replace(/[̀-ͯ]/g, "");
        if(plie !== mot) egal(R.jugerSaisieRappel(plie, mot, o).verdict, "presque", langue + " : « " + plie + " » sans accent");
        // Les leurres, dans sa categorie, comme la seance les voit (tous vus).
        // Une carte sur sept, contre toute sa categorie : la seance y puise de la
        // meme facon, mais tout le corpus contre tout le corpus prendrait minutes.
        if(n % 7) return;
        nl++;
        const pool = parMode[c.mode];
        const l = R.leurresDejaVus(c, pool, 2, dep);
        if(l.length < 2) choixManquants++;
        const repC = R.plierRappel(dep.reponse(c)), sensC = R.sensPlieRappel(c._sens);
        const motC = R.plierRappel(mot);
        l.forEach(x => {
            verifier(R.plierRappel(x.texte) !== repC, langue + " : leurre identique a la reponse pour " + mot);
            verifier(R.sensPlieRappel(x.it._sens) !== sensC, langue + " : leurre « " + x.texte + " » de meme sens que « " + mot + " » (" + c._sens + ")");
            verifier(x.it.mode === c.mode, langue + " : leurre d'une autre categorie pour " + mot);
            const motL = R.plierRappel(x.it.mode === "verben" ? x.it.word.infinitif : x.it.word[0]);
            verifier(motL !== motC, langue + " : leurre du meme mot pour " + mot);
            if(c.mode === "nomen") verifier(motL !== R.plierRappel(c.word[8] || "") && R.plierRappel(x.it.word[8] || "") !== motC,
                                           langue + " : leurre de l'autre genre pour " + mot);
        });
        if(l.length === 2) verifier(R.plierRappel(l[0].texte) !== R.plierRappel(l[1].texte), langue + " : deux leurres identiques pour " + mot);
    });
    console.log("  " + langue + " : " + n + " mots passes, leurres de " + nl + " cartes" + (choixManquants ? " (" + choixManquants + " sans deux leurres possibles)" : ""));
}
corpus("themes.json", "verbe.json", "adjectif.json", "de");
corpus("espanol/datos/temas.json", "espanol/datos/verbos.json", "espanol/datos/adjetivos.json", "es");

if(ko){
    console.log("ECHEC : " + ko + " verification(s) sur " + (ok + ko));
    fautes.forEach(f => console.log("  - " + f));
    if(ko > fautes.length) console.log("  (et " + (ko - fautes.length) + " autres)");
    process.exit(1);
}
console.log("OK : " + ok + " verifications (forme, une sur trois, tolerance, leurres, corpus de et es).");
