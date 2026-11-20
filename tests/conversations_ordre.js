// LA PLACE DU PIEGE DANS LES CONVERSATIONS, SUR L'ORDRE AFFICHE (ligne 150, 20 nov. 2026)
//
// Dans les donnees, la reponse fautive (« faux ») est ecrite en dernier : 1 539 noeuds sur 1 644. La page
// visuel/prototype/conversation.html ne les affiche plus dans l'ordre du fichier : ordreDesChoix() donne a chaque noeud
// un ordre d'affichage deterministe. Ce test LIT CETTE FONCTION DANS LA PAGE (entre ses deux marques) et l'applique a
// toutes les conversations (conversation/donnees/*.json, toutes langues, et pflege/datos/dialogues.json) :
//   - l'ordre affiche est une permutation des choix du noeud (aucun perdu, aucun en double), la meme a chaque appel ;
//   - une demande de repetition reste a la fin ; un noeud sans piege garde l'ordre du fichier ;
//   - NULLE PART le piege ne tient la meme place dans plus de 60 % des noeuds : ni dans l'ensemble, ni par nombre de
//     choix, ni dans une conversation (des qu'elle a six noeuds a piege), que la place se compte depuis le debut
//     (1re, 2e…) ou comme « la derniere ».
// Sans navigateur. La sonde a l'ecran : tests/conversations_ordre.py (sous le verrou).
//
//   node tests/conversations_ordre.js            le controle (code 1 si un seuil est depasse)
//   node tests/conversations_ordre.js --fichier  la meme mesure sur l'ORDRE DU FICHIER (l'etat d'avant)

const fs = require("fs");
const path = require("path");
const RACINE = path.join(__dirname, "..");
const SEUIL = 0.60, MIN = 6;
const page = fs.readFileSync(path.join(RACINE, "visuel", "prototype", "conversation.html"), "utf8");
const a = page.indexOf("// [debut-ordre-choix]"), b = page.indexOf("// [fin-ordre-choix]");
if(a < 0 || b < a){ console.log("ECHEC : les marques [debut-ordre-choix] / [fin-ordre-choix] sont introuvables dans conversation.html"); process.exit(1); }
const m = { exports: {} };
new Function("module", page.slice(a, b) + "\nmodule.exports = { ordreDesChoix };")(m);
const ordreDesChoix = m.exports.ordreDesChoix;
const DU_FICHIER = process.argv.indexOf("--fichier") >= 0;

// Toutes les conversations : { nom, id, noeuds }
const convs = [];
const dossier = path.join(RACINE, "visuel", "prototype", "conversation", "donnees");
fs.readdirSync(dossier).filter(f => f.endsWith(".json")).sort().forEach(f => {
    let d; try{ d = JSON.parse(fs.readFileSync(path.join(dossier, f), "utf8")); }catch(e){ return; }
    if(d && d.noeuds) convs.push({ nom: f, id: d.id, noeuds: d.noeuds });
});
const soins = path.join(RACINE, "pflege", "datos", "dialogues.json");
if(fs.existsSync(soins)){
    (JSON.parse(fs.readFileSync(soins, "utf8")).dialogues || []).forEach(d => convs.push({ nom: "soins " + d.id, id: d.id, noeuds: d.noeuds }));
}

const pbs = [];
const compter = () => ({ n: 0, places: {}, dernier: 0 });
const ajouter = (c, place, taille) => { c.n++; c.places[place] = (c.places[place] || 0) + 1; if(place === taille - 1) c.dernier++; };
const pire = c => Math.max(c.dernier, ...Object.values(c.places)) / (c.n || 1);
const dire = c => Object.keys(c.places).sort().map(p => "place " + (Number(p) + 1) + " : " + c.places[p]).join(", ") + " ; en dernier : " + c.dernier;
const tout = compter(), parTaille = {};
let noeuds = 0, sansPiege = 0, deplaces = 0;

convs.forEach(conv => {
    const ordre = ordreDesChoix({ id: conv.id, noeuds: conv.noeuds });
    const encore = ordreDesChoix({ id: conv.id, noeuds: conv.noeuds });
    const ici = compter();
    Object.keys(conv.noeuds).forEach(id => {
        const ch = conv.noeuds[id].choix || [];
        if(!ch.length) return;
        noeuds++;
        const o = DU_FICHIER ? ch.map((c, i) => i) : ordre[id];
        if(!o || o.length !== ch.length || o.slice().sort((x, y) => x - y).some((v, i) => v !== i)){
            pbs.push(conv.nom + " / " + id + " : l'ordre affiche n'est pas une permutation des choix"); return;
        }
        if(JSON.stringify(o) !== JSON.stringify(DU_FICHIER ? o : encore[id])) pbs.push(conv.nom + " / " + id + " : l'ordre change d'un appel a l'autre");
        const pieges = o.map((i, place) => ch[i].faux ? place : -1).filter(p => p >= 0);
        if(!pieges.length){
            sansPiege++;
            if(o.some((v, i) => v !== i)) pbs.push(conv.nom + " / " + id + " : un noeud sans piege a change d'ordre");
            return;
        }
        if(o.some((v, i) => v !== i)) deplaces++;
        // une demande de repetition reste a la fin
        const corps = o.filter(i => !(ch[i].repete && !ch[i].faux)).length;
        if(!DU_FICHIER && o.slice(0, corps).some(i => ch[i].repete && !ch[i].faux)) pbs.push(conv.nom + " / " + id + " : une demande de repetition n'est plus a la fin");
        // la place du (premier) piege, parmi les choix qui ne sont pas une demande de repetition
        const place = pieges[0];
        ajouter(ici, place, corps); ajouter(tout, place, corps);
        parTaille[corps] = parTaille[corps] || compter(); ajouter(parTaille[corps], place, corps);
    });
    if(ici.n >= MIN && pire(ici) > SEUIL) pbs.push(conv.nom + " : le piege tient la meme place dans " + Math.round(100 * pire(ici)) + " % de ses " + ici.n + " noeuds (" + dire(ici) + ")");
});
if(tout.n && pire(tout) > SEUIL) pbs.push("ensemble : le piege tient la meme place dans " + Math.round(100 * pire(tout)) + " % des " + tout.n + " noeuds (" + dire(tout) + ")");
Object.keys(parTaille).forEach(t => {
    const c = parTaille[t];
    if(c.n >= MIN && pire(c) > SEUIL) pbs.push("noeuds a " + t + " choix : le piege tient la meme place dans " + Math.round(100 * pire(c)) + " % des " + c.n + " noeuds");
});

console.log((DU_FICHIER ? "ORDRE DU FICHIER (avant)" : "ORDRE AFFICHE") + " : " + convs.length + " conversations, " + noeuds + " noeuds a choix, " + tout.n + " avec un piege (" + deplaces + " reordonnes), " + sansPiege + " sans piege");
console.log("  place du piege, ensemble : " + dire(tout) + " -- au plus " + Math.round(100 * pire(tout)) + " %");
Object.keys(parTaille).sort().forEach(t => console.log("  noeuds a " + t + " choix (" + parTaille[t].n + ") : " + dire(parTaille[t]) + " -- au plus " + Math.round(100 * pire(parTaille[t])) + " %"));
if(pbs.length){
    console.log("ECHEC : " + pbs.length + " probleme(s)");
    pbs.slice(0, 15).forEach(p => console.log("   " + p));
    process.exit(1);
}
console.log("OK : nulle part le piege ne tient la meme place dans plus de " + Math.round(100 * SEUIL) + " % des noeuds.");
