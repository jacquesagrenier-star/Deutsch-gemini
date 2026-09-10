// Exerce le VRAI code du plafond de mots neufs (v521), extrait d'index.html.
// Le bloc va de cartesEchues() a cartesCommencees() : tout ce qui decide de
// ce qu'une seance contient.
const fs = require("fs");
const src = fs.readFileSync("index.html", "utf8");

const i = src.indexOf("function cartesEchues(items){");
const j = src.indexOf("// Le repli quand la seance ressort vide");
const k = src.indexOf("\n}", src.indexOf("function cartesCommencees(items){")) + 2;
if (i < 0 || j < 0 || k < 2) throw new Error("bloc introuvable dans index.html");
const BLOC = src.slice(i, k);

const magasin = {};
globalThis.localStorage = {
  getItem: n => (n in magasin ? magasin[n] : null),
  setItem: (n, v) => { magasin[n] = String(v); },
  removeItem: n => { delete magasin[n]; }
};
let AUJOURD_HUI = "2026-09-10";
globalThis.getTodayStr = () => AUJOURD_HUI;

// Le magasin de progression, reduit a ce que ces fonctions lisent.
const etats = {};
globalThis.getWordState = (t, i2) => etats[t + ":" + i2] || {};
const poser = (n, etat) => { for (let x = 0; x < n; x++) etats["t:" + x] = etat; };

globalThis.currentCards = [];
globalThis.currentCardsFull = [];

eval(BLOC + "\nglobalThis.cartesDeSession = cartesDeSession;"
   + "\nglobalThis.cartesCommencees = cartesCommencees;"
   + "\nglobalThis.placeNeufsRestante = placeNeufsRestante;"
   + "\nglobalThis.noterMotNeuf = noterMotNeuf;"
   + "\nglobalThis.ajouterSerieNeufs = ajouterSerieNeufs;"
   + "\nglobalThis.estNeuf = estNeuf;"
   + "\nglobalThis.retardEnAttente = retardEnAttente;"
   + "\nglobalThis.trancheSupplementaire = trancheSupplementaire;"
   + "\nglobalThis.PLAFOND_NEUFS = PLAFOND_NEUFS;"
   + "\nglobalThis.TAILLE_SEANCE = TAILLE_SEANCE;"
   + "\nglobalThis.SUPPLEMENT_SEANCE = SUPPLEMENT_SEANCE;");

let ko = 0;
const ok = (n, v) => { console.log("  " + (v ? "OK   " : "ECHEC") + "  " + n); if (!v) ko++; };
const paquet = n => Array.from({ length: n }, (_, x) => ({ themeId: "t", index: x }));
const vider = () => { for (const c of Object.keys(etats)) delete etats[c];
                      for (const c of Object.keys(magasin)) delete magasin[c]; };

console.log("\nLE DEFAUT QU'ON CORRIGE : 462 CARTES D'UN COUP");
vider();
ok("un paquet neuf de 462 n'en sert que " + PLAFOND_NEUFS,
   cartesDeSession(paquet(462)).length === PLAFOND_NEUFS);

console.log("\nLES ECHEANCES PASSENT AVANT, ET REMPLISSENT LA SEANCE");
vider();
poser(462, {});                                   // tout est neuf
for (let x = 0; x < 10; x++) etats["t:" + x] = { srsHits: 2, due: 1000 };  // 10 dues
let s = cartesDeSession(paquet(462));
ok("10 echeances + " + PLAFOND_NEUFS + " neufs", s.length === 10 + PLAFOND_NEUFS);
ok("les echeances sont en tete", s.slice(0, 10).every(it => it.index < 10));

console.log("\nLA SEANCE A UNE TAILLE FIXE, MEME APRES UNE LONGUE ABSENCE");
vider();
poser(462, {});
for (let x = 0; x < 300; x++) etats["t:" + x] = { srsHits: 2, due: 5000 - x };
s = cartesDeSession(paquet(462));
ok("300 cartes en retard : la seance en fait " + TAILLE_SEANCE,
   s.length === TAILLE_SEANCE);
ok("aucun mot neuf tant que le retard remplit la seance",
   s.every(it => it.index < 300));
ok("les PLUS EN RETARD d'abord",
   s[0].index === 299 && s[1].index === 298);
ok("le reste attend, et se compte pour le panneau d'information",
   retardEnAttente(paquet(462)) === 300 - TAILLE_SEANCE);

console.log("\n« EN FAIRE PLUS » : LE RETARD D'ABORD, LES NEUFS ENSUITE");
globalThis.currentCardsFull = paquet(462);
globalThis.currentCards = s;
let t2 = trancheSupplementaire();
ok("la tranche suivante prend du retard, pas du neuf", t2.neufs === false);
ok("elle fait " + SUPPLEMENT_SEANCE + " cartes", t2.cartes.length === SUPPLEMENT_SEANCE);
ok("et ne redonne pas ce qui vient d'etre servi",
   t2.cartes.every(it => !s.some(x => x.index === it.index)));
vider();
poser(462, {});                                   // plus aucun retard
globalThis.currentCards = cartesDeSession(paquet(462));
t2 = trancheSupplementaire();
ok("sans retard, la tranche est faite de mots neufs", t2.neufs === true);

console.log("\nLA DOSE SE CONSOMME, ET ELLE TIENT LA JOURNEE");
vider();
ok("dose entiere au reveil", placeNeufsRestante() === PLAFOND_NEUFS);
for (let x = 0; x < 9; x++) noterMotNeuf();
ok("apres 9 reponses il reste " + (PLAFOND_NEUFS - 9),
   placeNeufsRestante() === PLAFOND_NEUFS - 9);
ok("une seance ne sert plus que le reste",
   cartesDeSession(paquet(462)).length === PLAFOND_NEUFS - 9);
for (let x = 0; x < 6; x++) noterMotNeuf();
ok("dose epuisee : plus aucun mot neuf", cartesDeSession(paquet(462)).length === 0);

console.log("\n« ENCORE 15 » N'OUVRE QU'UNE SERIE, ET SEULEMENT AUJOURD'HUI");
ajouterSerieNeufs();
ok("une serie de plus, pas deux", placeNeufsRestante() === PLAFOND_NEUFS);
ok("la seance repart avec " + PLAFOND_NEUFS,
   cartesDeSession(paquet(462)).length === PLAFOND_NEUFS);
AUJOURD_HUI = "2026-09-11";
ok("demain : le plafond reprend sa valeur, le bonus est oublie",
   placeNeufsRestante() === PLAFOND_NEUFS);
AUJOURD_HUI = "2026-09-10";

console.log("\nLE REPLI NE REOUVRE PAS LA VANNE");
vider();
poser(100, {});                                   // 100 mots jamais vus
for (let x = 0; x < 12; x++) etats["t:" + x] = { srsHits: 1, due: Date.now() + 9e8 };
ok("commencees = les 12 entames, PAS les 88 neufs",
   cartesCommencees(paquet(100)).length === 12);
etats["t:0"] = { mastered: true, due: Date.now() + 9e8 };
ok("un mot maitrise n'y revient pas", cartesCommencees(paquet(100)).length === 11);

console.log("\nCE QUI COMPTE COMME NEUF");
ok("jamais touche", estNeuf({}) === true);
ok("un « Encore » n'est plus neuf (il a une echeance)",
   estNeuf({ srsHits: 0, due: 1234 }) === false);
ok("une reussite n'est plus neuve", estNeuf({ srsHits: 1 }) === false);
ok("un mot maitrise n'est pas neuf", estNeuf({ mastered: true }) === false);

console.log("\nSTOCKAGE ILLISIBLE");
magasin["deutschAI_neufsDuJour"] = "{pas du JSON";
ok("la dose repart entiere plutot que de jeter",
   placeNeufsRestante() === PLAFOND_NEUFS);

console.log("\nL'ENTRETIEN S'ELOIGNE AU LIEU DE TOURNER EN ROND");
const a2 = src.indexOf("const SRS_ENTRETIEN_JOURS = ");
const b2 = src.indexOf("\n}", src.indexOf("function joursEntretien(state){")) + 2;
if (a2 < 0 || b2 < 2) throw new Error("SRS_ENTRETIEN_JOURS introuvable");
eval(src.slice(a2, b2) + "\nglobalThis.joursEntretien = joursEntretien;"
   + "\nglobalThis.SRS_ENTRETIEN_JOURS = SRS_ENTRETIEN_JOURS;");
ok("premier controle a 16 jours", joursEntretien({}) === 16);
ok("puis 35", joursEntretien({ entretiens: 1 }) === 35);
ok("puis 90", joursEntretien({ entretiens: 2 }) === 90);
ok("« Hallo » confirme 5 fois : deux ans", joursEntretien({ entretiens: 5 }) === 730);
ok("jamais au-dela du dernier barreau",
   joursEntretien({ entretiens: 99 }) ===
   SRS_ENTRETIEN_JOURS[SRS_ENTRETIEN_JOURS.length - 1]);
ok("l'echelle ne redescend jamais",
   SRS_ENTRETIEN_JOURS.every((v, i2) => i2 === 0 || v > SRS_ENTRETIEN_JOURS[i2 - 1]));

console.log(ko ? "\n" + ko + " ECHEC(S)\n" : "\nTout passe.\n");
process.exit(ko ? 1 : 0);
