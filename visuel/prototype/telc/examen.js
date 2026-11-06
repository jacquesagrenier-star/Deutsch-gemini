// LE TELC A2·B1 -- L'EXAMEN BLANC (6 nov. 2026, session « telc : Parler + examen blanc », decision de Jacques du
// 6 nov. : le telc en quatre sessions paralleles, celle-ci fait l'oral et l'examen blanc).
//
// UN EXAMEN COMPLET, DANS L'ORDRE ET AU CHRONOMETRE DE L'EPREUVE (preparation-examens/FORMAT-TELC.md) :
//   1. Lesen                                     45 min   items 1-18
//   2. Sprachbausteine + Lesen und Schreiben     35 min   19-28, 29-30, le courriel 31
//   3. Hoeren + Hoeren und Schreiben            ≈ 35 min   32-51, les repondeurs 52-56 (l'ecoute suit le son)
//   4. Schreiben                                 10 min   la reponse courte 57
//   5. une pause, puis l'oral (parler.html?examen=blanc, environ 15 min), qui revient ici pour le verdict.
// Le verdict suit le bareme du telc : 240 points, 60 par competence ; B1 = 70 % du total ET 70 % dans 3 des 4
// competences ET 40 % dans chacune ; A2 = 40 %, 40 % dans 3 des 4, 10 % dans chacune (verdictTelc()).
//
// CE MODULE NE CONNAIT AUCUNE EPREUVE : il enchaine celles que les autres modules inscrivent. Les sessions Lire,
// Ecrire et Ecouter branchent leur partie ainsi, sans toucher a ce fichier :
//
//   DTZ.partie({id: "L", ..., ouvrir, examen: lancer})      (ou window.TELC_EXAMEN.L = lancer)
//
//   lancer(o) affiche la partie EN MODE EXAMEN dans o.zone (#zone) : pas d'explication, pas de corrige, le bouton
//   o.suite (#suite) pour avancer. Il recoit :
//     o.id        la partie (« L », « SB », « LS », « H », « HS », « S ») ;
//     o.numero    le numero de cet examen blanc (0, 1, 2...) : pour tourner parmi les series gardees a l'examen
//                 (PROFIL.seriesExamen, les series 1 a N) ;
//     o.fini(res) a appeler UNE fois, a la fin : res = les points de la partie par competence, sur l'echelle du
//                 telc, et un detail libre pour le corrige :
//                   L  {lesen}          sur 54 (18 × 3)          SB {schreiben} sur 5 (10 × 0,5)
//                   LS {lesen, schreiben} sur 6 et 15 (29-30 ; le courriel 31, critere I)
//                   H  {hoeren}         sur 60 (20 × 3)          HS {schreiben} sur 5 (5 × 1)
//                   S  {schreiben}      sur 35 : le message 57 (5) + les criteres II a IV des deux textes (3 × 10),
//                                       que la session Ecrire juge a la fin de l'ecrit ;
//                   + {detail: {...}} au choix de la partie.
//   lancer() peut rendre {terminer()} : appele quand le chronometre arrive a zero, il doit appeler o.fini() avec ce
//   qui est rempli. Sans terminer(), la partie est close a zero avec 0 point.
//   Une partie sans lancer est sautee (« pas encore prete ») et le verdict reste partiel.
//
// Les Sprachbausteine n'ont pas encore de mode examen dans sprachbausteine.js : examenSB(), plus bas, en tient lieu
// (la lettre entiere, les 10 trous, sans corrige), et s'efface des que le module en inscrit un.
//
// L'etat de l'examen en cours (stockage local wortando_telc_blanc) survit au passage par la page de l'oral :
// {debut, etape, numero, res: {L: {lesen}, SB: {...}, ..., Sp: {sprechen}}, fini}. parler.html y ecrit res.Sp.

"use strict";

Object.assign(TXT, {
  bl_titre: "Examen blanc complet",
  bl_sous: "Dans l’ordre du telc : lire, Sprachbausteine, écouter, écrire (125 min), puis l’oral (environ 15 min).",
  bl_intro: "Au telc, on commence par lire. Garde ton énergie pour l’écoute : elle vient tard. Chaque partie a son chronomètre, comme le jour de l’examen, et rien n’est corrigé avant la fin.",
  bl_deroule: "Le déroulé",
  bl_e_L: "Lire", bl_e_L_s: "Lesen · 45 min",
  bl_e_SBLS: "Sprachbausteine, lire et écrire", bl_e_SBLS_s: "Sprachbausteine · Lesen und Schreiben · 35 min",
  bl_e_HHS: "Écouter", bl_e_HHS_s: "Hören · Hören und Schreiben · environ 35 min",
  bl_e_S: "Écrire", bl_e_S_s: "Schreiben · 10 min",
  bl_e_PAUSE: "La pause", bl_e_PAUSE_s: "Entre l’écrit et l’oral",
  bl_e_Sp: "Parler", bl_e_Sp_s: "Mündliche Prüfung · à deux · environ 15 min",
  bl_p_L: "Lire", bl_p_SB: "Sprachbausteine", bl_p_LS: "Lire et écrire (le courriel)", bl_p_H: "Écouter",
  bl_p_HS: "Écouter et noter (les répondeurs)", bl_p_S: "Écrire (la réponse courte)", bl_p_Sp: "Parler",
  bl_pret: "prête", bl_pas_pret: "pas encore prête",
  bl_note_pas_pret: "Les parties pas encore prêtes sont sautées : le verdict sera partiel. Elles arrivent une à une.",
  bl_go: "Commencer", bl_commencer: "Commencer l’examen", bl_reprendre: "Reprendre l’examen en cours : {e}", bl_recommencer: "Recommencer à zéro",
  bl_etape: "Étape {n} sur {sur}",
  bl_minutes: "{m} minutes",
  bl_entree_s: "Le chronomètre démarre quand tu touches « Commencer ». À zéro, la partie s’arrête et ce qui est rempli compte.",
  bl_entree_ecoute: "Le chronomètre montre le temps prévu ; l’écoute suit l’enregistrement et ne s’arrête pas à zéro.",
  bl_rien_pret: "Aucune partie de cette étape n’est encore prête : elle est sautée.",
  bl_temps: "Temps écoulé : la partie s’arrête ici, ce qui est rempli compte.",
  bl_etape_finie: "Étape terminée", bl_suite: "Étape suivante",
  bl_pause_texte: "L’écrit est fini. Respire, bois un verre d’eau. L’oral se passe à deux, avec Anna et moi. Il s’ouvre dans une autre page, et tu reviens ici pour le verdict.",
  bl_vers_oral: "Passer l’oral",
  bl_oral_texte: "Environ 15 minutes à deux, sans préparation, sauf une minute avant la partie 3. Anna mène l’entretien, je suis l’autre candidat.",
  bl_verdict: "Le verdict de l’examen blanc",
  bl_lesen: "Lire (Lesen)", bl_hoeren: "Écouter (Hören)", bl_schreiben: "Écrire (Schreiben)", bl_sprechen: "Parler (Sprechen)",
  bl_total: "Total", bl_incomplet: "incomplet",
  bl_regle: "Au telc A2·B1, le B1 demande 70 % du total (168 / 240), au moins 70 % (42 / 60) dans trois compétences sur quatre et 40 % (24 / 60) dans chacune. L’A2 demande 40 % du total (96 / 240), 40 % dans trois compétences et 10 % (6 / 60) dans chacune.",
  bl_partiel: "Verdict partiel : pas encore de {liste}. Le niveau s’affichera quand toutes les parties de l’examen existeront.",
  bl_mark_b1: "B1 ! Si c’était aujourd’hui, tu aurais le B1 au telc. Garde ce rythme jusqu’au jour de l’examen.",
  bl_mark_a2: "A2, et le B1 n’est pas loin. Regarde ta compétence la plus basse : c’est elle qui te retient.",
  bl_mark_moins: "Pas encore l’A2, et c’est normal à ce stade. Reprends les parties une à une en entraînement, puis refais l’examen blanc.",
  bl_mark_partiel: "Voilà où tu en es dans les parties déjà prêtes. Le verdict complet viendra avec les autres.",
  bl_estimation: "Écrire et Parler sont des estimations : l’app mesure le contenu de tes réponses, pas leur correction ni ta prononciation.",
  bl_refaire: "Refaire l’examen blanc", bl_retour: "Retour au telc",
  bl_terminer_partie: "Terminer cette partie", bl_terminer_q: "Terminer cette partie ? {n} trou(s) sans réponse.",
  bl_dernier: "{n} / 240 · {niv}", bl_dernier_partiel: "{n} points · partiel"
});
if (LANGUE === "en") Object.assign(TXT, {
  bl_titre: "Full mock exam",
  bl_sous: "In telc order: reading, Sprachbausteine, listening, writing (125 min), then speaking (about 15 min).",
  bl_intro: "In the telc, you start with reading. Save your energy for listening: it comes late. Every part has its timer, as on the day of the exam, and nothing is marked until the end.",
  bl_deroule: "The running order",
  bl_e_L: "Reading", bl_e_L_s: "Lesen · 45 min",
  bl_e_SBLS: "Sprachbausteine, reading and writing", bl_e_SBLS_s: "Sprachbausteine · Lesen und Schreiben · 35 min",
  bl_e_HHS: "Listening", bl_e_HHS_s: "Hören · Hören und Schreiben · about 35 min",
  bl_e_S: "Writing", bl_e_S_s: "Schreiben · 10 min",
  bl_e_PAUSE: "The break", bl_e_PAUSE_s: "Between the written and the oral exam",
  bl_e_Sp: "Speaking", bl_e_Sp_s: "Mündliche Prüfung · in pairs · about 15 min",
  bl_p_L: "Reading", bl_p_SB: "Sprachbausteine", bl_p_LS: "Reading and writing (the email)", bl_p_H: "Listening",
  bl_p_HS: "Listening and note-taking (the voicemails)", bl_p_S: "Writing (the short reply)", bl_p_Sp: "Speaking",
  bl_pret: "ready", bl_pas_pret: "not ready yet",
  bl_note_pas_pret: "Parts that aren't ready yet are skipped: the verdict will be partial. They're arriving one by one.",
  bl_go: "Start", bl_commencer: "Start the exam", bl_reprendre: "Resume the exam in progress: {e}", bl_recommencer: "Start again from scratch",
  bl_etape: "Step {n} of {sur}",
  bl_minutes: "{m} minutes",
  bl_entree_s: "The timer starts when you tap “Start”. When it reaches zero, the part stops and what you've filled in counts.",
  bl_entree_ecoute: "The timer shows the planned time; the listening follows the recording and doesn't stop at zero.",
  bl_rien_pret: "No part of this step is ready yet: it is skipped.",
  bl_temps: "Time's up: the part stops here, what you've filled in counts.",
  bl_etape_finie: "Step finished", bl_suite: "Next step",
  bl_pause_texte: "The written exam is over. Breathe, have a glass of water. The speaking test is done in pairs, with Anna and me. It opens in another page, and you come back here for the verdict.",
  bl_vers_oral: "Take the speaking test",
  bl_oral_texte: "About 15 minutes in pairs, with no preparation time, except one minute before part 3. Anna leads the conversation, I'm the other candidate.",
  bl_verdict: "The mock exam verdict",
  bl_lesen: "Reading (Lesen)", bl_hoeren: "Listening (Hören)", bl_schreiben: "Writing (Schreiben)", bl_sprechen: "Speaking (Sprechen)",
  bl_total: "Total", bl_incomplet: "incomplete",
  bl_regle: "In the telc A2·B1, B1 requires 70% of the total (168 / 240), at least 70% (42 / 60) in three of the four skills and 40% (24 / 60) in each. A2 requires 40% of the total (96 / 240), 40% in three skills and 10% (6 / 60) in each.",
  bl_partiel: "Partial verdict: no {liste} yet. The level will be shown once every part of the exam exists.",
  bl_mark_b1: "B1! If this were the real thing, you'd get B1 in the telc. Keep this pace until exam day.",
  bl_mark_a2: "A2, and B1 isn't far off. Look at your lowest skill: that's the one holding you back.",
  bl_mark_moins: "Not A2 yet, and that's normal at this stage. Go back over the parts one by one in practice mode, then take the mock exam again.",
  bl_mark_partiel: "Here's where you stand in the parts that are ready. The full verdict will come with the others.",
  bl_estimation: "Writing and speaking are estimates: the app measures the content of your answers, not their accuracy or your pronunciation.",
  bl_refaire: "Retake the mock exam", bl_retour: "Back to the telc",
  bl_terminer_partie: "Finish this part", bl_terminer_q: "Finish this part? {n} gap(s) unanswered.",
  bl_dernier: "{n} / 240 · {niv}", bl_dernier_partiel: "{n} points · partial",
  // les cles de commun.js dont l'examen blanc se sert
  quitter_q: "Leave the mock exam? It won't be counted.", quitter: "Leave", continuer: "Continue",
  niv_b1: "B1", niv_a2: "A2", niv_moins: "below A2", sur: "out of {n}"
});

const BLANC_ETAPES = [
  { id: "L", minutes: 45, parties: ["L"] },
  { id: "SBLS", minutes: 35, parties: ["SB", "LS"] },
  { id: "HHS", minutes: 35, parties: ["H", "HS"], forcer: false },   // l'ecoute suit l'enregistrement
  { id: "S", minutes: 10, parties: ["S"] },
  { id: "PAUSE", pause: true },
  { id: "Sp", oral: true }
];
// ce que vaut chaque partie, par competence (FORMAT-TELC.md, « Les points »)
const BLANC_SUR = { L: {lesen: 54}, SB: {schreiben: 5}, LS: {lesen: 6, schreiben: 15}, H: {hoeren: 60}, HS: {schreiben: 5}, S: {schreiben: 35}, Sp: {sprechen: 60} };
const COMPETENCES = ["lesen", "hoeren", "schreiben", "sprechen"];
window.TELC_EXAMEN = window.TELC_EXAMEN || {};

// le lanceur d'une partie en mode examen : celui que son module inscrit, sinon celui de window.TELC_EXAMEN
function blancLanceur(id){
  const p = DTZ.parties.find(x => x.id === id);
  if (p && typeof p.examen === "function") return p.examen;
  return typeof window.TELC_EXAMEN[id] === "function" ? window.TELC_EXAMEN[id] : null;
}
const blancPrete = id => id === "Sp" || !!blancLanceur(id);

// LE VERDICT DU TELC : c = {lesen, hoeren, schreiben, sprechen}, chacune sur 60
function verdictTelc(c){
  const v = COMPETENCES.map(k => Number(c[k]) || 0), tot = v.reduce((x, y) => x + y, 0);
  if (tot >= 168 && v.filter(x => x >= 42).length >= 3 && v.every(x => x >= 24)) return "b1";
  if (tot >= 96 && v.filter(x => x >= 24).length >= 3 && v.every(x => x >= 6)) return "a2";
  return "moins";
}
DTZ.verdictTelc = verdictTelc;

let BL = null, BL_COURANT = null;
function blancSauver(){ ecrire("blanc", BL); }
function blancUrl(page, extra){
  const p = new URLSearchParams();
  ["apprendre", "lang", "nuit", "rapide"].forEach(k => { if (Q.get(k)) p.set(k, Q.get(k)); });
  for (const k in (extra || {})) p.set(k, extra[k]);
  return page + "?" + p.toString();
}
const vir = n => LANGUE === "fr" ? String(Math.round(n * 10) / 10).replace(".", ",") : String(Math.round(n * 10) / 10);
function blancEcran(titre){ silence(); fermerPanneau(); $("titre").textContent = titre || T("bl_titre"); $("suite").hidden = true; window.scrollTo(0, 0); }
function blancBouton(texte, action){ const s = $("suite"); s.hidden = false; s.disabled = false; s.textContent = texte; s.onclick = action; }
// pendant l'examen, « ‹ » demande avant de quitter ; l'examen en cours reste garde (on peut le reprendre)
function blancGarderRetour(){
  DTZ.surRetour(() => { confirmer(T("quitter_q"), () => { blancArreterPartie(); arreterChrono(); accueil(); }, T("quitter")); return true; });
}
function blancArreterPartie(){ BL_COURANT = null; silence(); }

// ---------------------------------------------------------------- l'entree
function blancIntro(){
  blancEcran();
  arreterChrono();
  BL = lire("blanc", null);
  DTZ.surRetour(() => { accueil(); return true; });
  const enCours = BL && !BL.fini && BL.etape < BLANC_ETAPES.length;
  const lignes = BLANC_ETAPES.map((E, k) => {
    const parties = E.pause ? "" : (E.oral ? ["Sp"] : E.parties).map(id =>
      '<span class="petit" style="display:block">' + esc(T("bl_p_" + id)) + ' · ' + esc(blancPrete(id) ? T("bl_pret") : T("bl_pas_pret")) + '</span>').join("");
    return '<div class="mode" style="cursor:default"><b>' + (k + 1) + '. ' + esc(T("bl_e_" + E.id)) + '</b><span>' + esc(T("bl_e_" + E.id + "_s")) + '</span>' + parties + '</div>';
  }).join("");
  const manque = Object.keys(BLANC_SUR).filter(id => !blancPrete(id));
  $("zone").innerHTML =
    '<div class="bloc"><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T("bl_intro")) + '</div></div></div>' +
    '<div class="bloc"><h2>' + esc(T("bl_deroule")) + '</h2>' + lignes +
      (manque.length ? '<p class="petit">' + esc(T("bl_note_pas_pret")) + '</p>' : "") +
      (enCours ? '<button class="secondaire" id="blNouveau">' + esc(T("bl_recommencer")) + '</button>' : "") + '</div>';
  if (enCours){
    blancBouton(T("bl_reprendre", {e: T("bl_e_" + BLANC_ETAPES[BL.etape].id)}), blancEtape);
    $("blNouveau").onclick = blancNouveau;
  } else blancBouton(T("bl_commencer"), blancNouveau);
}
function blancNouveau(){
  BL = { debut: Date.now(), etape: 0, numero: lire("blancs_faits", 0), res: {}, fini: false };
  blancSauver();
  blancEtape();
}

// ---------------------------------------------------------------- les etapes
function blancEtape(){
  arreterChrono();
  const E = BLANC_ETAPES[BL.etape];
  if (!E) return blancVerdict();
  blancGarderRetour();
  const n = T("bl_etape", {n: BL.etape + 1, sur: BLANC_ETAPES.length});
  blancEcran(T("bl_e_" + E.id));
  if (E.pause || E.oral){
    $("zone").innerHTML = '<div class="bloc"><div class="petit">' + esc(n) + '</div><h2>' + esc(T("bl_e_" + E.id)) + '</h2>' +
      '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T(E.pause ? "bl_pause_texte" : "bl_oral_texte")) + '</div></div></div>';
    if (E.pause) blancBouton(T("bl_suite"), () => { BL.etape++; blancSauver(); blancEtape(); });
    else blancBouton(T("bl_vers_oral"), () => { silence(); location.href = blancUrl("parler.html", { examen: "blanc" }); });
    return;
  }
  const pretes = E.parties.filter(blancPrete);
  $("zone").innerHTML = '<div class="bloc"><div class="petit">' + esc(n) + '</div><h2>' + esc(T("bl_e_" + E.id)) + '</h2>' +
    '<p><b>' + esc(T("bl_minutes", {m: E.minutes})) + '</b> · ' + esc(T("bl_e_" + E.id + "_s")) + '</p>' +
    E.parties.map(id => '<p class="petit">' + esc(T("bl_p_" + id)) + ' · ' + esc(blancPrete(id) ? T("bl_pret") : T("bl_pas_pret")) + '</p>').join("") +
    '<p class="petit">' + esc(pretes.length ? T(E.forcer === false ? "bl_entree_ecoute" : "bl_entree_s") : T("bl_rien_pret")) + '</p></div>';
  if (!pretes.length){
    E.parties.forEach(id => { BL.res[id] = { absent: true }; });
    blancSauver();
    blancBouton(T("bl_suite"), () => { BL.etape++; blancSauver(); blancEtape(); });
    return;
  }
  blancBouton(T("bl_go"), () => {
    BL.tempsFini = false; blancSauver();
    chrono(RAPIDE ? 20 : E.minutes * 60, "bas", () => blancTempsEcoule(E));
    blancPartie(E, 0);
  });
}
function blancTempsEcoule(E){
  if (E.forcer === false) return;
  BL.tempsFini = true; blancSauver();
  const c = BL_COURANT;
  if (!c) return;
  try{ if (c.h && typeof c.h.terminer === "function") c.h.terminer(); }catch(e){}
  if (BL_COURANT === c) c.fini({});   // terminer() absent, ou qui n'a pas rendu : 0 point
}
function blancBorner(id, res){
  const out = {};
  for (const c in BLANC_SUR[id]) out[c] = Math.min(BLANC_SUR[id][c], Math.max(0, Number(res && res[c]) || 0));
  if (res && res.detail) out.detail = res.detail;
  return out;
}
function blancPartie(E, k){
  if (k >= E.parties.length) return blancFinEtape(E);
  const id = E.parties[k], lancer = blancLanceur(id);
  if (!lancer){ BL.res[id] = { absent: true }; blancSauver(); return blancPartie(E, k + 1); }
  if (BL.tempsFini){ BL.res[id] = Object.assign(blancBorner(id, {}), { temps: true }); blancSauver(); return blancPartie(E, k + 1); }
  let rendu = false;
  const fini = res => {
    if (rendu) return; rendu = true;
    BL_COURANT = null;
    BL.res[id] = blancBorner(id, res);
    blancSauver();
    blancPartie(E, k + 1);
  };
  blancEcran(T("bl_p_" + id));
  $("zone").innerHTML = "";
  BL_COURANT = { id, fini, h: null };
  const cour = BL_COURANT;
  try{ cour.h = lancer({ id, zone: $("zone"), suite: $("suite"), numero: BL.numero || 0, fini, rapide: RAPIDE, langue: LANGUE }) || {}; }
  catch(e){ fini({}); }
  blancGarderRetour();
}
function blancFinEtape(E){
  arreterChrono();
  const temps = BL.tempsFini;
  BL.etape++; BL.tempsFini = false; blancSauver();
  blancEcran(T("bl_e_" + E.id));
  $("zone").innerHTML = '<div class="bloc"><h2>' + esc(T("bl_etape_finie")) + '</h2>' + (temps ? '<p>' + esc(T("bl_temps")) + '</p>' : "") + '</div>';
  blancBouton(T("bl_suite"), blancEtape);
}

// ---------------------------------------------------------------- le verdict
function blancVerdict(){
  arreterChrono();
  BL = lire("blanc", null) || BL;
  if (!BL) return blancIntro();
  blancEcran(T("bl_verdict"));
  DTZ.surRetour(() => { accueil(); return true; });
  const comp = {lesen: 0, hoeren: 0, schreiben: 0, sprechen: 0}, manque = [], compManque = new Set();
  for (const id in BLANC_SUR){
    const r = BL.res[id];
    if (!r || r.absent){ manque.push(id); Object.keys(BLANC_SUR[id]).forEach(c => compManque.add(c)); continue; }
    for (const c in BLANC_SUR[id]) comp[c] += Math.min(BLANC_SUR[id][c], Math.max(0, Number(r[c]) || 0));
  }
  const total = COMPETENCES.reduce((n, c) => n + comp[c], 0);
  const complet = manque.length === 0;
  const niv = complet ? verdictTelc(comp) : null;
  const pct = n => Math.round(n / 240 * 100) + "%";
  const lignes = COMPETENCES.map(c => '<span>' + esc(T("bl_" + c)) + (compManque.has(c) ? ' · <i>' + esc(T("bl_incomplet")) + '</i>' : "") +
    '</span><b>' + vir(comp[c]) + ' / 60</b>').join("") +
    '<span>' + esc(T("bl_total")) + '</span><b>' + vir(total) + ' / 240</b>';
  const mot = complet ? "bl_mark_" + niv : "bl_mark_partiel";
  $("zone").innerHTML =
    '<div class="bloc"><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T(mot)) + '</div></div>' +
      '<div class="score">' + vir(total) + '</div><p class="petit" style="text-align:center">' + esc(T("sur", {n: 240})) + '</p>' +
      (complet ? '<span class="niveau ' + niv + '">' + esc(T("niv_" + niv)) + '</span>' : "") +
      '<div class="jauge"><i style="width:' + pct(total) + '"></i><s style="left:40%"><em>A2 · 96</em></s><s style="left:70%"><em>B1 · 168</em></s></div>' +
      '<div class="detail">' + lignes + '</div>' +
      (complet ? "" : '<p class="petit">' + esc(T("bl_partiel", {liste: manque.map(id => T("bl_p_" + id)).join(", ")})) + '</p>') +
      '<p class="petit">' + esc(T("bl_regle")) + '</p><p class="petit">' + esc(T("bl_estimation")) + '</p></div>' +
    '<div class="bloc boutons"><button class="secondaire" id="blRefaire">' + esc(T("bl_refaire")) + '</button>' +
      '<button class="secondaire" id="blRetour">' + esc(T("bl_retour")) + '</button></div>';
  $("blRefaire").onclick = blancNouveau;
  $("blRetour").onclick = accueil;
  // compte une seule fois : le dernier examen blanc de l'accueil, le resultat pour l'app
  if (!BL.fini){
    BL.fini = true; blancSauver();
    ecrire("blancs_faits", (BL.numero || 0) + 1);
    const d = new Date();
    ecrire("dernier", { date: d.toLocaleDateString(LANGUE === "en" ? "en-GB" : "fr-FR"),
      texte: complet ? T("bl_dernier", {n: vir(total), niv: T("niv_" + niv)}) : T("bl_dernier_partiel", {n: vir(total)}) });
    resultat("blanc", { points: total, niveau: niv, competences: comp, partiel: !complet });
    parler("resultat", { mode: "examen_blanc_telc", points: total, sur: 240, niveau: niv, competences: comp, partiel: !complet });
  }
}

// ---------------------------------------------------------------- les Sprachbausteine en mode examen
// En attendant le mode examen de sprachbausteine.js : la lettre entiere, les dix trous, a, b ou c, sans corrige.
// La lettre : parmi les series gardees a l'examen (PROFIL.seriesExamen), sinon toutes, a tour de role.
function examenSB(o){
  const toutes = (typeof SB !== "undefined" && SB.series) || [];
  const pool = SERIES_EXAMEN > 0 ? toutes.slice(0, SERIES_EXAMEN) : toutes;
  if (!pool.length){ setTimeout(() => o.fini({}), 0); return {}; }
  const s = pool[(o.numero || 0) % pool.length];
  const rep = s.luecken.map(() => null);
  const trouHtml = n => {
    const k = s.luecken.findIndex(l => l.n === n), r = rep[k];
    return '<span class="trou" id="blT' + n + '">' + (r === null ? "(" + n + ")" : esc(s.luecken[k].o[r])) + '</span>';
  };
  const rendre = () => {
    const lettre = '<div class="doc lettre" dir="ltr"><div class="k">' + (s.registre === "formel" ? "Brief" : "E-Mail") + '</div>' +
      '<div class="objet" lang="de">' + esc(s.betreff) + '</div>' +
      s.absaetze.map(p => '<p lang="de">' + esc(p).replace(/\{(\d+)\}/g, (m, n) => trouHtml(Number(n))) + '</p>').join("") + '</div>';
    const lignes = s.luecken.map((l, k) => '<div class="q"><div class="tete"><span class="num">' + l.n + '</span></div><div class="choix ligne">' +
      l.o.map((w, j) => '<button class="opt' + (rep[k] === j ? " pris" : "") + '" data-k="' + k + '" data-j="' + j + '"><b>' + "abc"[j] + '</b><span lang="de">' + esc(w) + '</span></button>').join("") +
      '</div></div>').join("");
    o.zone.innerHTML = '<div class="bloc"><p class="consigne" lang="de">' + esc(T("sb_consigne_de")) + '</p>' + lettre + '</div><div class="bloc">' + lignes + '</div>';
    o.zone.querySelectorAll("[data-k]").forEach(b => b.onclick = () => { rep[Number(b.dataset.k)] = Number(b.dataset.j); const y = window.scrollY; rendre(); window.scrollTo(0, y); });
  };
  let fait = false;
  const finir = () => {
    if (fait) return; fait = true;
    const bons = s.luecken.filter((l, k) => rep[k] === l.bon).length;
    o.fini({ schreiben: bons / 2, detail: { serie: s.id, bons, sur: 10, rep: rep.slice() } });
  };
  rendre();
  blancBouton(T("bl_terminer_partie"), () => {
    const vides = rep.filter(r => r === null).length;
    if (vides) confirmer(T("bl_terminer_q", {n: vides}), finir, T("bl_terminer_partie")); else finir();
  });
  return { terminer: finir };
}
if (!window.TELC_EXAMEN.SB) window.TELC_EXAMEN.SB = examenSB;

// ---------------------------------------------------------------- les inscriptions
DTZ.examen({ id: "blanc", ordre: 10, titre: T("bl_titre"), sous: T("bl_sous"), lancer: blancIntro });
// une « partie » sans tuile (PROFIL.tuiles ne la nomme pas) : c'est par elle que telc.html?partie=BLANC rouvre
// l'examen blanc, au retour de la page de l'oral (&etape=verdict) ou quand on quitte l'oral en cours
DTZ.partie({ id: "BLANC", ordre: 99, titre: T("bl_titre"), sous: T("bl_sous"),
  ouvrir: () => (Q.get("etape") === "verdict" ? blancVerdict() : blancIntro()) });
