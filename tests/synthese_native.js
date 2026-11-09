// La voix du telephone dans l'app Android (installerSyntheseNative, index.html).
//     node tests/synthese_native.js
// Sans navigateur : le code est extrait de la page et tourne contre un faux
// module natif. Ce qu'il ne prouve pas : qu'un telephone parle pour de bon.
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const page = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");
const debut = page.indexOf("function installerSyntheseNative(){");
if (debut < 0) { console.error("ECHEC : installerSyntheseNative absente"); process.exit(1); }
let i = page.indexOf("{", debut), n = 0, fin = -1;
for (; i < page.length; i++) {
    if (page[i] === "{") n++;
    else if (page[i] === "}" && --n === 0) { fin = i + 1; break; }
}
const SOURCE = page.slice(debut, fin);

let echecs = 0, faits = 0;
function ok(c, m) { faits++; if (!c) { echecs++; console.error("ECHEC : " + m); } }
const pause = ms => new Promise(r => setTimeout(r, ms));

function fauxModule(options = {}) {
    const m = {
        parles: [], arrets: 0, attente: [], languesEssais: 0,
        speak(o) {
            m.parles.push(o);
            if (options.refuser) return Promise.reject(new Error("refus"));
            return new Promise((res, rej) => m.attente.push({res, rej}));
        },
        stop() { m.arrets++; return Promise.resolve(); },
        getSupportedLanguages() {
            m.languesEssais++;
            if (m.languesEssais <= (options.echecsLangues || 0)) return Promise.reject(new Error("pas pret"));
            return Promise.resolve({languages: ["en-US", "en-GB", "pt-PT", "pt-BR", "ja-JP"]});
        },
        finir() { m.attente.shift().res(); }
    };
    return m;
}

function monde({module, reelle} = {}) {
    const w = {setTimeout, Promise, console, Object, Number, Math, String, Set, isFinite, Error,
        document: {documentElement: {lang: ""}}};
    w.window = w;
    if (reelle) { w.speechSynthesis = reelle; w.SpeechSynthesisUtterance = function () {}; }
    w.pluginNatif = nom => (module && nom === "TextToSpeech" ? module : null);
    vm.createContext(w);
    vm.runInContext(SOURCE, w);
    return w;
}

function enonce(w, texte, champs) {
    const u = new w.SpeechSynthesisUtterance(texte);
    u.journal = [];
    u.onstart = () => u.journal.push("start");
    u.onend = () => u.journal.push("end");
    u.onerror = e => u.journal.push("error:" + e.error);
    return Object.assign(u, champs);
}

(async () => {
    // 1. iPhone et web : le vrai moteur n'est jamais remplace
    {
        const reelle = {vrai: true}, m = fauxModule(), w = monde({module: m, reelle});
        w.installerSyntheseNative();
        ok(w.speechSynthesis === reelle, "le vrai speechSynthesis a ete remplace");
        ok(m.languesEssais === 0, "le module a ete appele alors que le vrai moteur existe");
    }
    // 2. Android 16 et avant : pas de module, rien, sans erreur
    {
        const w = monde({});
        let erreur = null;
        try { w.installerSyntheseNative(); } catch (e) { erreur = e; }
        ok(!erreur, "exception sans le module : " + erreur);
        ok(!("speechSynthesis" in w), "speechSynthesis pose sans le module");
    }
    // 3. Une phrase : langue, debit, evenements, etats
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        const u = enonce(w, "Good morning", {lang: "en-GB", rate: 0.9});
        w.speechSynthesis.speak(u);
        await pause(60);
        ok(m.parles.length === 1, "speak natif non appele");
        const p = m.parles[0];
        ok(p.text === "Good morning" && p.lang === "en-GB" && p.rate === 0.9 && p.volume === 1, "parametres : " + JSON.stringify(p));
        ok(w.speechSynthesis.speaking === true, "speaking faux pendant la phrase");
        ok(u.journal.join() === "start", "evenements avant la fin : " + u.journal);
        m.finir();
        await pause(60);
        ok(u.journal.join() === "start,end", "evenements : " + u.journal);
        ok(w.speechSynthesis.speaking === false, "speaking vrai apres la fin");
    }
    // 4. La file : une phrase a la fois, dans l'ordre
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        const a = enonce(w, "a b", {lang: "pt-PT"}), b = enonce(w, "c d", {lang: "pt-BR"});
        w.speechSynthesis.speak(a);
        w.speechSynthesis.speak(b);
        await pause(60);
        ok(m.parles.length === 1, "deux phrases parties ensemble");
        ok(w.speechSynthesis.pending === true, "pending faux avec une phrase en file");
        m.finir();
        await pause(60);
        ok(m.parles.length === 2 && m.parles[1].lang === "pt-BR", "seconde phrase non partie");
        ok(w.speechSynthesis.pending === false, "pending vrai, file vide");
    }
    // 5. cancel : la phrase coupee, la file videe, une fin tardive ignoree
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        const a = enonce(w, "un", {lang: "ja-JP"}), b = enonce(w, "deux", {lang: "ja-JP"});
        w.speechSynthesis.speak(a);
        w.speechSynthesis.speak(b);
        await pause(60);
        w.speechSynthesis.cancel();
        await pause(60);
        ok(m.arrets === 1, "stop natif : " + m.arrets);
        ok(a.journal.join() === "start,error:interrupted", "phrase coupee : " + a.journal);
        ok(b.journal.join() === "error:canceled", "phrase en file : " + b.journal);
        ok(!w.speechSynthesis.speaking && !w.speechSynthesis.pending, "etat apres cancel");
        const c = enonce(w, "trois", {lang: "ja-JP"});
        w.speechSynthesis.speak(c);
        await pause(60);
        m.finir();          // la fin tardive de « un »
        await pause(60);
        ok(a.journal.indexOf("end") < 0, "fin tardive transmise a la phrase coupee");
        ok(c.journal.join() === "start" && w.speechSynthesis.speaking, "la fin tardive a termine la phrase suivante : " + c.journal);
        m.finir();
        await pause(60);
        ok(c.journal.join() === "start,end" && !w.speechSynthesis.speaking, "phrase suivante : " + c.journal);
    }
    // 6. cancel au repos : rien au natif
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        w.speechSynthesis.cancel();
        ok(m.arrets === 0, "stop natif au repos");
    }
    // 7. Rien a dire : l'amorce au volume 0 et l'enonce vide
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        const a = enonce(w, "a", {volume: 0, rate: 10}), v = enonce(w, "");
        w.speechSynthesis.speak(a);
        w.speechSynthesis.speak(v);
        await pause(150);
        ok(m.parles.length === 0, "le natif a parle pour une amorce");
        ok(a.journal.join() === "start,end" && v.journal.join() === "start,end", "amorce : " + a.journal + " / " + v.journal);
    }
    // 8. Un refus (langue absente du telephone) : erreur, et la suite part
    {
        const m = fauxModule({refuser: true}), w = monde({module: m});
        w.installerSyntheseNative();
        const a = enonce(w, "un", {lang: "ja-JP"}), b = enonce(w, "deux", {lang: "ja-JP"});
        w.speechSynthesis.speak(a);
        w.speechSynthesis.speak(b);
        await pause(150);
        ok(a.journal.join() === "start,error:synthesis-failed", "refus : " + a.journal);
        ok(b.journal.join() === "start,error:synthesis-failed", "suite du refus : " + b.journal);
        ok(!w.speechSynthesis.speaking, "moteur reste occupe apres un refus");
    }
    // 9. La langue de la voix passe avant celle de l'enonce ; un debit hors bornes
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        w.speechSynthesis.speak(enonce(w, "ola", {lang: "pt-BR", voice: {lang: "pt-PT"}, rate: 10}));
        await pause(60);
        ok(m.parles[0].lang === "pt-PT", "langue de la voix : " + m.parles[0].lang);
        ok(m.parles[0].rate === 4, "debit borne : " + m.parles[0].rate);
    }
    // 10. Les voix : moteur pas encore pret, reprises, puis voiceschanged
    {
        const m = fauxModule({echecsLangues: 1}), w = monde({module: m});
        w.installerSyntheseNative();
        let prop = 0, ecoute = 0;
        w.speechSynthesis.onvoiceschanged = () => prop++;
        w.speechSynthesis.addEventListener("voiceschanged", () => ecoute++);
        ok(w.speechSynthesis.getVoices().length === 0, "des voix avant le chargement");
        await pause(600);
        const v = w.speechSynthesis.getVoices();
        ok(v.length === 5 && v.some(x => x.lang === "en-GB"), "voix : " + v.length);
        ok(prop === 1 && ecoute === 1, "voiceschanged : " + prop + "/" + ecoute);
    }
    // 11. Une seconde installation ne remplace rien
    {
        const m = fauxModule(), w = monde({module: m});
        w.installerSyntheseNative();
        const s = w.speechSynthesis;
        w.installerSyntheseNative();
        ok(w.speechSynthesis === s, "installation en double");
    }
    if (echecs) { console.error(echecs + " echec(s) sur " + faits + " verifications"); process.exit(1); }
    console.log("OK : " + faits + " verifications");
})();
