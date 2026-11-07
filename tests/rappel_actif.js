// Le rappel actif des cartes (essai « rappel_actif », pour tous depuis le 7 nov.
// 2026) : l'echelle par mot, la regle « une sur trois », les leurres et les fautes
// d'orthographe.
//
//   node tests/rappel_actif.js
//
// Aucun navigateur, aucun verrou : la logique vit entre deux marques dans
// index.html (« RAPPEL ACTIF : LOGIQUE PURE (debut) » ... « (fin) »), sans DOM ni
// stockage. On l'extrait, on l'execute dans un bac a sable, et on la passe :
//   1. sur des cas ecrits a la main (les regles, une par une) ;
//   2. sur TOUT le corpus allemand et espagnol des noms, verbes et adjectifs :
//      les leurres d'une carte ne sont jamais la bonne reponse sous une autre
//      forme (meme mot, meme sens, autre genre), et ses fausses orthographes
//      sont toutes differentes de la bonne, differentes entre elles, et jamais
//      un vrai mot du corpus.

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
vm.runInContext(source.slice(a, b) + "\n;this.R = { RAPPEL_ECART, RAPPEL_ARTICLES, empreinteRappel, dejaVuRappel, pointsRappel, formeSelonPoints, tourDuRappel, normRappel, plierRappel, sensPlieRappel, ecartLettresRappel, debutCommunRappel, leurresDejaVus, variantesMot, fautesOrthographe, ordreDesChoix };", ctx);
const R = ctx.R;

let ok = 0, ko = 0;
const fautes = [];
function verifier(cond, msg){
    if(cond) ok++;
    else { ko++; if(fautes.length < 40) fautes.push(msg); }
}
function egal(x, y, msg){ verifier(x === y, msg + " -- attendu " + JSON.stringify(y) + ", obtenu " + JSON.stringify(x)); }

// ---------- 1. L'echelle par mot ----------
egal(R.formeSelonPoints(0), null, "0 point (mot nouveau) : la carte qu'on retourne");
egal(R.formeSelonPoints(1), "choisir", "1 point : trois mots differents");
egal(R.formeSelonPoints(2), "proches", "2 points : trois mots plus proches");
egal(R.formeSelonPoints(3), "orthographe", "3 points : le meme mot ecrit de trois facons");
egal(R.formeSelonPoints(4), "orthographe", "maitrise : l'orthographe aussi");
egal(R.pointsRappel({ srsHits: 2 }), 2, "points = srsHits");
egal(R.pointsRappel({ srsHits: 1, mastered: true }), 4, "maitrise = 4 points");
egal(R.pointsRappel({ srsHits: 0, due: 99 }), 0, "un mot rate (Encore) retombe a 0 point : carte ordinaire");
// « Vu » = le contraire exact d'estNeuf(), la definition du reste de l'app.
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
egal(jouer([1,1,1,1,1].map(Boolean), [false, true, true, true, true]), "01001", "pas de choix possibles : la suivante prend le tour");

// ---------- 3. Les fausses orthographes, a la main ----------
const F = (langue, mode, mot, article, mots) => R.fautesOrthographe({ langue, mode, mot, article, cle: "t:" + mot },
    f => (mots || []).indexOf(f) >= 0);
function controlerFautes(liste, bonne, msg){
    egal(liste.length, 2, msg + " : deux fausses orthographes");
    verifier(liste.every(x => x !== bonne), msg + " : aucune n'est la bonne (" + liste.join(" | ") + ")");
    verifier(new Set(liste).size === liste.length, msg + " : toutes differentes (" + liste.join(" | ") + ")");
}
{
    const l = F("de", "nomen", "Schlüssel", "der");
    controlerFautes(l, "der Schlüssel", "der Schlüssel");
    verifier(l.some(x => /Schlussel|Schlüsel|Schlüßel/.test(x)), "der Schlüssel : une faute d'orthographe parmi les deux (" + l.join(" | ") + ")");
    const t = F("de", "nomen", "Tisch", "der");
    controlerFautes(t, "der Tisch", "der Tisch (rien a deformer : majuscule et article)");
    verifier(t.indexOf("der tisch") >= 0 && t.some(x => /^(die|das) Tisch$/.test(x)), "der Tisch : la majuscule et l'article (" + t.join(" | ") + ")");
    controlerFautes(F("de", "nomen", "Straße", "die"), "die Straße", "die Straße");
    controlerFautes(F("de", "verben", "sich beeilen", ""), "sich beeilen", "sich beeilen");
    verifier(F("de", "verben", "sich beeilen", "").every(x => /^sich /.test(x)), "sich beeilen : le « sich » reste");
    egal(F("de", "verben", "sich freuen", "").length, 0, "sich freuen : aucune faute realiste, la carte retombe sur les leurres proches");
    controlerFautes(F("de", "adjektive", "müde", ""), "müde", "müde");
    // « schön » n'a qu'une faute possible, « schon », qui est un vrai mot : aucune
    // orthographe, la carte retombe sur les leurres proches.
    egal(F("de", "adjektive", "schön", "", ["schon"]).length, 0, "schön : « schon » est un mot, pas de fautes");
    // Jamais un vrai mot : « Tasse » est un mot, donc pas une faute de « Tasche ».
    const ta = F("de", "nomen", "Tasse", "die", ["tase", "tasße"]);
    verifier(ta.every(x => !/ Tase$/.test(x)), "die Tasse : « Tase » est un mot du corpus de l'essai, il est ecarte (" + ta.join(" | ") + ")");
    const ll = F("es", "nomen", "llave", "la");
    controlerFautes(ll, "la llave", "la llave");
    verifier(ll.some(x => /yave|llabe/.test(x)), "la llave : ll/y ou b/v (" + ll.join(" | ") + ")");
    controlerFautes(F("es", "nomen", "canción", "la"), "la canción", "la canción");
    verifier(F("es", "nomen", "canción", "la").some(x => /cancion|canzión|cansión/.test(x)), "la canción : l'accent ou c/s");
    controlerFautes(F("es", "nomen", "niña", "la"), "la niña", "la niña");
    controlerFautes(F("es", "verben", "hablar", ""), "hablar", "hablar");
    verifier(F("es", "nomen", "leche", "la").every(x => !/lece/.test(x)), "la leche : le h de « ch » ne tombe pas");
    verifier(F("es", "nomen", "casa", "la").every(x => !/^(los|las) /.test(x)), "es : l'article faux garde le nombre (la -> el, jamais los ni las)");
    egal(JSON.stringify(F("de", "nomen", "Schlüssel", "der")), JSON.stringify(l), "les memes fautes d'un appel a l'autre (aucun hasard)");
    const e = R.ecartLettresRappel("der Schlüsel", "der Schlüssel").filter(x => x.diff).map(x => x.c).join("");
    egal(e, "s", "l'ecart souligne la lettre qui manque");
    const e2 = R.ecartLettresRappel("der schlüssel", "der Schlüssel").filter(x => x.diff).map(x => x.c).join("");
    egal(e2, "S", "l'ecart souligne la majuscule");
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
        nom("bureau", 6, "Taste", "die", "la clé", true),                  // meme sens
        nom("ville", 7, "Bahnhof", "der", "la gare", true),
        nom("hiver", 8, "Schlitten", "der", "la luge", true),              // meme article, meme debut
        { themeId: "verbes", index: 9, mode: "verben", word: { infinitif: "gehen" }, _vu: true, _sens: "aller" }
    ];
    const l = R.leurresDejaVus(cible, pool, 2, dep, false);
    egal(l.length, 2, "deux leurres");
    egal(l.map(x => x.texte).sort().join(" | "), "das Handtuch | der Aufzug", "1 point : le meme lieu d'abord, deja vus seulement");
    verifier(!l.some(x => /Rezeption|Taste|gehen|Schlüssel/.test(x.texte)), "ni jamais vu, ni meme sens, ni autre categorie, ni meme mot");
    const p = R.leurresDejaVus(cible, pool, 2, dep, true);
    egal(p.map(x => x.texte).sort().join(" | "), "der Aufzug | der Schlitten",
         "2 points : plus proches -- meme theme et meme article (Aufzug), meme article et meme debut (Schlitten)");
    egal(JSON.stringify(R.leurresDejaVus(cible, pool, 2, dep, true)), JSON.stringify(p), "les leurres ne changent pas d'un appel a l'autre");
    const arzt = nom("metier", 1, "Arzt", "der", "le médecin", true, "Ärztin");
    const l3 = R.leurresDejaVus(arzt, [arzt, nom("metier", 2, "Ärztin", "die", "la médecin (femme)", true, "Arzt"),
                                       nom("metier", 3, "Lehrer", "der", "le professeur", true)], 2, dep, true);
    egal(l3.map(x => x.texte).join(" | "), "der Lehrer", "l'autre genre d'un nom de personne n'est jamais un leurre");
    const ch = R.ordreDesChoix("hotel:1", "der Schlüssel", l);
    egal(ch.length, 3, "trois choix");
    egal(ch.filter(c => c.juste).length, 1, "un seul juste");
}

// ---------- 5. Tout le corpus ----------
function lireJson(f){ return JSON.parse(fs.readFileSync(path.join(RACINE, f), "utf8")); }
function marcher(x, f){ if(Array.isArray(x)) x.forEach(y => marcher(y, f)); else if(x && typeof x === "object"){ if(f(x) === false) return; Object.values(x).forEach(y => marcher(y, f)); } }
function corpus(langue, fichiers){
    const cartes = [];
    const mots = new Set();
    const ajouter = t => String(t || "").split(/[\s\/,]+/).forEach(x => { const n = R.normRappel(x); if(n) mots.add(n); });
    lireJson(fichiers.themes).themes.forEach(t => (t.mots || []).forEach((m, i) => {
        const w = [m.mot, m.genre || "", m.pluriel || "", m.traduction || ""];
        w[8] = m.feminin || m.masculin || "";
        ajouter(m.mot); ajouter(m.pluriel); ajouter(w[8]);
        cartes.push({ themeId: t.id, index: i, mode: "nomen", word: w, _vu: true, _sens: (m.article_fr || "") + (m.traduction || "") });
    }));
    let iv = 0, ia = 0;
    marcher(lireJson(fichiers.verbes), x => {
        if(!x.infinitif) return;
        ajouter(x.infinitif);
        let pr = x.praesens;
        if(typeof pr === "string"){ try{ pr = JSON.parse(pr.replace(/'/g, '"')); }catch(e){ pr = null; } }
        if(pr && typeof pr === "object") Object.values(pr).forEach(ajouter);
        cartes.push({ themeId: "verben", index: iv++, mode: "verben", word: { infinitif: x.infinitif }, _vu: true, _sens: x.traduction || "" });
        return false;
    });
    marcher(lireJson(fichiers.adjectifs), x => {
        if(!x.mot) return;
        ajouter(x.mot);
        if(!/\//.test(x.mot)) cartes.push({ themeId: "adjektive", index: ia++, mode: "adjektive", word: [x.mot], _vu: true, _sens: x.traduction || "" });
        return false;
    });
    (fichiers.autres || []).forEach(f => marcher(lireJson(f), x => { if(x.mot) ajouter(x.mot); if(x.wort) ajouter(x.wort); }));
    let n = 0, nl = 0, sansFautes = 0;
    const parMode = {};
    cartes.forEach(c => { (parMode[c.mode] = parMode[c.mode] || []).push(c); });
    cartes.forEach(c => {
        const mot = c.mode === "verben" ? c.word.infinitif : c.word[0];
        if(!mot || !String(mot).trim()) return;
        n++;
        // Les fausses orthographes, comme l'app les fabrique.
        const soi = new Set([R.normRappel(mot)]);
        const l = R.fautesOrthographe({ langue, mode: c.mode, mot, article: c.mode === "nomen" ? c.word[1] : "", cle: c.themeId + ":" + c.index },
                                      f => !soi.has(f) && mots.has(f));
        if(l.length < 2) sansFautes++;
        const art = c.mode === "nomen" ? String(c.word[1] || "").split(/[\/\s]/)[0] : "";
        const bonne = (art ? art + " " : "") + String(mot).normalize("NFC").trim();
        if(l.length){
            verifier(l.length === 2, langue + " : deux fautes ou aucune pour " + bonne);
            verifier(l.every(x => x !== bonne), langue + " : une fausse orthographe identique a la bonne pour " + bonne);
            verifier(new Set(l).size === l.length, langue + " : deux fausses orthographes identiques pour " + bonne + " (" + l.join(" | ") + ")");
            l.forEach(x => {
                const motFaux = (art && x.indexOf(" ") > 0 && (R.RAPPEL_ARTICLES[langue] || []).indexOf(x.split(" ")[0].toLowerCase()) >= 0) ? x.slice(x.indexOf(" ") + 1) : x;
                const memeMot = R.normRappel(motFaux) === R.normRappel(mot);   // article ou majuscule seuls
                verifier(memeMot || !mots.has(R.normRappel(motFaux)), langue + " : « " + x + " » est un vrai mot du corpus (pour " + bonne + ")");
            });
        }
        // Les leurres, dans sa categorie, comme la seance les voit (tous vus).
        // Une carte sur sept, contre toute sa categorie.
        if(n % 7) return;
        nl++;
        [false, true].forEach(proches => {
            const ll = R.leurresDejaVus(c, parMode[c.mode], 2, dep, proches);
            const repC = R.plierRappel(dep.reponse(c)), sensC = R.sensPlieRappel(c._sens), motC = R.plierRappel(mot);
            ll.forEach(x => {
                verifier(R.plierRappel(x.texte) !== repC, langue + " : leurre identique a la reponse pour " + mot);
                verifier(R.sensPlieRappel(x.it._sens) !== sensC, langue + " : leurre « " + x.texte + " » de meme sens que « " + mot + " »");
                verifier(x.it.mode === c.mode, langue + " : leurre d'une autre categorie pour " + mot);
                const motL = R.plierRappel(x.it.mode === "verben" ? x.it.word.infinitif : x.it.word[0]);
                verifier(motL !== motC, langue + " : leurre du meme mot pour " + mot);
                if(c.mode === "nomen") verifier(motL !== R.plierRappel(c.word[8] || "") && R.plierRappel(x.it.word[8] || "") !== motC,
                                               langue + " : leurre de l'autre genre pour " + mot);
            });
        });
    });
    console.log("  " + langue + " : " + n + " mots, fautes pour " + (n - sansFautes) + " (les " + sansFautes
        + " autres retombent sur les leurres proches), leurres de " + nl + " cartes");
}
corpus("de", { themes: "themes.json", verbes: "verbe.json", adjectifs: "adjectif.json",
               autres: ["adverbe.json", "redewendung.json", "funktionswort.json"].filter(f => fs.existsSync(path.join(RACINE, f))) });
corpus("es", { themes: "espanol/datos/temas.json", verbes: "espanol/datos/verbos.json", adjectifs: "espanol/datos/adjetivos.json",
               autres: ["espanol/datos/adverbios.json", "espanol/datos/expresiones.json", "espanol/datos/funcionales.json"].filter(f => fs.existsSync(path.join(RACINE, f))) });

if(ko){
    console.log("ECHEC : " + ko + " verification(s) sur " + (ok + ko));
    fautes.forEach(f => console.log("  - " + f));
    if(ko > fautes.length) console.log("  (et " + (ko - fautes.length) + " autres)");
    process.exit(1);
}
console.log("OK : " + ok + " verifications (echelle, une sur trois, fautes, leurres, corpus de et es).");
