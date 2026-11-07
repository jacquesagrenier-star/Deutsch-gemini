// LE TELC A2·B1 -- L'EXAMEN BLANC (6 nov. 2026, session « telc : Parler + examen blanc », decision de Jacques du
// 6 nov. : le telc en quatre sessions paralleles, celle-ci fait l'oral et l'examen blanc).
//
// UN EXAMEN COMPLET, DANS L'ORDRE ET AU CHRONOMETRE DE L'EPREUVE (preparation-examens/FORMAT-TELC.md, l'Uebungstest 1
// du telc, le meme document que le Modelltest de Marina) :
//   1. Lesen                                     45 min   items 1-18
//   2. Sprachbausteine + Lesen und Schreiben     35 min   19-28, 29-30, le courriel 31
//   3. Hoeren + Hoeren und Schreiben            ≈ 35 min   32-51, les repondeurs 52-56 (l'ecoute suit le son)
//   4. Schreiben                                 10 min   la reponse courte 57
//   5. une pause, puis l'oral (oral.html?examen=blanc, environ 15 min), qui revient ici pour le verdict
//      (telc.html?partie=BLANC&etape=verdict).
// Le verdict : niveauTelc() de telc-commun.js (240 points, 60 par competence, regle 70 % / 40 %). Une competence dont
// une partie manque encore n'est pas comptee : le niveau dit « incomplet », on ne promet pas un B1 sur trois
// competences.
//
// CE MODULE NE CONNAIT AUCUNE EPREUVE : il enchaine celles que les modules inscrivent par TELC.epreuve() (le mode
// d'emploi est en tete de telc-commun.js) :
//   TELC.epreuve({id, ordre, minutes, sur: {Lesen: 54}, lancer: (fini, o) => { … ; fini({pts: {Lesen: x}, detail}) }})
// lancer() affiche la partie minutee, sans aide, dans #zone, avance avec #suite. Il recoit en second argument
// o = {numero (le numero de cet examen blanc, pour tourner parmi les series gardees), zone, suite, rapide, langue}.
// Il peut rendre {terminer()} : appele a zero du chronometre, terminer() appelle fini() avec ce qui est rempli ; sans
// lui, la partie est close a 0 point. Les minutes et l'ordre des etapes sont ceux de l'examen, ci-dessous : une partie
// inscrite prend sa place dans son etape, une partie absente est sautee (« pas encore prete »).
//
// Les Sprachbausteine n'ont pas encore de mode examen dans sprachbausteine.js : examenSB(), plus bas, en tient lieu
// (la lettre entiere, les dix trous, sans corrige) et s'efface des que ce module inscrit le sien.
//
// L'etat de l'examen en cours (stockage local wortando_telc_blanc) survit au passage par la page de l'oral :
// {debut, etape, numero, res: {L: {pts, detail}, …, Sp: {pts: {Sprechen}}}, fini}. oral.html y ecrit res.Sp.

"use strict";

textesTelc({
fr: {
  bl_titre: "Examen blanc complet",
  bl_sous: "Dans l’ordre du telc : lire, Sprachbausteine, écouter, écrire (125 min), puis l’oral (environ 15 min).",
  bl_intro: "Au telc, on commence par lire. Garde ton énergie pour l’écoute : elle vient tard. Chaque étape a son chronomètre, comme le jour de l’examen, et rien n’est corrigé avant la fin.",
  bl_deroule: "Le déroulé",
  bl_e_L: "Lire", bl_e_L_s: "Lesen · 45 min",
  bl_e_L_q: "Quatre parties, 18 questions : des petites annonces à associer, un texte court, des courriels, un texte plus long. 3 points par question.",
  bl_e_SBLS: "Sprachbausteine, lire et écrire", bl_e_SBLS_s: "Sprachbausteine · Lesen und Schreiben · 35 min",
  bl_e_SBLS_q: "Une lettre à 10 trous (0,5 point chacun), puis un courriel à lire (2 questions, 3 points chacune) et à écrire : tu réponds à ses questions, avec formule d’appel et salutation (15 points).",
  bl_e_HHS: "Écouter", bl_e_HHS_s: "Hören · Hören und Schreiben · environ 35 min",
  bl_e_HHS_q: "Quatre écoutes, 20 questions (3 points chacune) : certaines s’entendent deux fois, d’autres une seule. Puis 5 messages de répondeur : tu notes l’information demandée (1 point chacun).",
  bl_e_S: "Écrire", bl_e_S_s: "Schreiben · 10 min",
  bl_e_S_q: "Une réponse courte à un message qui te pose une question : plus d’un mot (5 points). Pour les deux textes écrits, trois critères en plus : communication, correction, richesse de la langue (30 points).",
  bl_e_PAUSE: "La pause", bl_e_PAUSE_s: "Entre l’écrit et l’oral",
  bl_e_PAUSE_q: "Prends ton temps : l’examen t’attend.",
  bl_e_Sp: "Parler", bl_e_Sp_s: "Mündliche Prüfung · à deux · environ 15 min",
  bl_e_Sp_q: "Trois parties à deux, sans image : se présenter et répondre (6 points), planifier ensemble (12), donner et justifier son avis (12), plus prononciation, correction et richesse de la langue (30).",
  bl_p_L: "Lire", bl_p_SB: "Sprachbausteine", bl_p_LS: "Lire et écrire (le courriel)", bl_p_H: "Écouter",
  bl_p_HS: "Écouter et noter (les répondeurs)", bl_p_S: "Écrire (la réponse courte)", bl_p_Sp: "Parler",
  bl_pret: "prête", bl_pas_pret: "pas encore prête", bl_deux_points: " : ",
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
  bl_Lesen: "Lire (Lesen)", bl_Hoeren: "Écouter (Hören)", bl_Schreiben: "Écrire (Schreiben)", bl_Sprechen: "Parler (Sprechen)",
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
},
en: {
  bl_titre: "Full mock exam",
  bl_sous: "In telc order: reading, Sprachbausteine, listening, writing (125 min), then speaking (about 15 min).",
  bl_intro: "In the telc, you start with reading. Save your energy for listening: it comes late. Every step has its timer, as on the day of the exam, and nothing is marked until the end.",
  bl_deroule: "The running order",
  bl_e_L: "Reading", bl_e_L_s: "Lesen · 45 min",
  bl_e_L_q: "Four parts, 18 questions: short ads to match, a short text, emails, a longer text. 3 points per question.",
  bl_e_SBLS: "Sprachbausteine, reading and writing", bl_e_SBLS_s: "Sprachbausteine · Lesen und Schreiben · 35 min",
  bl_e_SBLS_q: "A letter with 10 gaps (0.5 points each), then an email to read (2 questions, 3 points each) and to answer: you reply to its questions, with an opening and a closing (15 points).",
  bl_e_HHS: "Listening", bl_e_HHS_s: "Hören · Hören und Schreiben · about 35 min",
  bl_e_HHS_q: "Four recordings, 20 questions (3 points each): some are played twice, others only once. Then 5 voicemail messages: you note down the information asked for (1 point each).",
  bl_e_S: "Writing", bl_e_S_s: "Schreiben · 10 min",
  bl_e_S_q: "A short reply to a message that asks you a question: more than one word (5 points). For the two written texts, three more criteria: communication, accuracy, range of language (30 points).",
  bl_e_PAUSE: "The break", bl_e_PAUSE_s: "Between the written and the oral exam",
  bl_e_PAUSE_q: "Take your time: the exam will wait for you.",
  bl_e_Sp: "Speaking", bl_e_Sp_s: "Mündliche Prüfung · in pairs · about 15 min",
  bl_e_Sp_q: "Three parts in pairs, no picture: introduce yourself and answer (6 points), plan together (12), give and justify your opinion (12), plus pronunciation, accuracy and range of language (30).",
  bl_p_L: "Reading", bl_p_SB: "Sprachbausteine", bl_p_LS: "Reading and writing (the email)", bl_p_H: "Listening",
  bl_p_HS: "Listening and note-taking (the voicemails)", bl_p_S: "Writing (the short reply)", bl_p_Sp: "Speaking",
  bl_pret: "ready", bl_pas_pret: "not ready yet", bl_deux_points: ": ",
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
  bl_Lesen: "Reading (Lesen)", bl_Hoeren: "Listening (Hören)", bl_Schreiben: "Writing (Schreiben)", bl_Sprechen: "Speaking (Sprechen)",
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
  bl_dernier: "{n} / 240 · {niv}", bl_dernier_partiel: "{n} points · partial"
}});

// les etapes de l'examen, dans son ordre et a ses minutes
const BLANC_ETAPES = [
  { id: "L", minutes: 45, parties: ["L"] },
  { id: "SBLS", minutes: 35, parties: ["SB", "LS"] },
  { id: "HHS", minutes: 35, parties: ["H", "HS"], forcer: false },   // l'ecoute suit l'enregistrement
  { id: "S", minutes: 10, parties: ["S"] },
  { id: "PAUSE", pause: true },
  { id: "Sp", oral: true }
];
// ce que vaut chaque partie, par competence (telc-commun.js, FORMAT-TELC.md « Les points »)
const BLANC_SUR = { L: {Lesen: 54}, SB: {Schreiben: 5}, LS: {Lesen: 6, Schreiben: 15}, H: {Hoeren: 60}, HS: {Schreiben: 5}, S: {Schreiben: 35}, Sp: {Sprechen: 60} };
const COMPETENCES = ["Lesen", "Hoeren", "Schreiben", "Sprechen"];

const blancEpreuve = id => TELC.epreuves.find(e => e.id === id) || null;
const blancPrete = id => id === "Sp" || !!blancEpreuve(id);

let BL = null, BL_COURANT = null;
function blancSauver(){ ecrire("blanc", BL); }
function blancUrl(page, extra){
  const p = new URLSearchParams();
  ["apprendre", "lang", "nuit", "rapide"].forEach(k => { if (Q.get(k)) p.set(k, Q.get(k)); });
  for (const k in (extra || {})) p.set(k, extra[k]);
  return page + "?" + p.toString();
}
const vir = n => { const x = String(Math.round(n * 10) / 10); return ["fr", "tr", "uk", "ru", "pl", "pt"].includes(LANGUE) ? x.replace(".", ",") : x; };
function blancEcran(titre){ silence(); fermerPanneau(); $("titre").textContent = titre || T("bl_titre"); $("suite").hidden = true; window.scrollTo(0, 0); }
function blancBouton(texte, action){ const s = $("suite"); s.hidden = false; s.disabled = false; s.textContent = texte; s.onclick = action; }
const blancMark = texte => '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(texte) + '</div></div>';
// pendant l'examen, « ‹ » demande avant de quitter ; l'examen en cours reste garde (on peut le reprendre)
function blancGarderRetour(){
  DTZ.surRetour(() => { confirmer(T("quitter_q"), () => { BL_COURANT = null; silence(); arreterChrono(); accueil(); }, T("quitter")); return true; });
}

// ---------------------------------------------------------------- l'entree
function blancIntro(){
  blancEcran();
  arreterChrono();
  BL = lire("blanc", null);
  DTZ.surRetour(() => { accueil(); return true; });
  const enCours = BL && !BL.fini && BL.etape < BLANC_ETAPES.length;
  const lignes = BLANC_ETAPES.map((E, k) => {
    const parties = E.pause ? "" : (E.oral ? ["Sp"] : E.parties).map(id =>
      '<span class="petit" style="display:block">· ' + esc(T("bl_p_" + id)) + esc(DEUX_POINTS_TELC) + esc(blancPrete(id) ? T("bl_pret") : T("bl_pas_pret")) + '</span>').join("");
    return '<div class="mode" style="cursor:default"><b>' + (k + 1) + '. ' + esc(T("bl_e_" + E.id)) + '</b><span>' + esc(T("bl_e_" + E.id + "_s")) + '</span>' +
      '<span style="font-weight:600;color:var(--encre)">' + esc(T("bl_e_" + E.id + "_q")) + '</span>' + parties + '</div>';
  }).join("");
  const manque = Object.keys(BLANC_SUR).filter(id => !blancPrete(id));
  $("zone").innerHTML =
    '<div class="bloc">' + blancMark(T("bl_intro")) + '</div>' +
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
      '<p>' + esc(T("bl_e_" + E.id + "_q")) + '</p>' + blancMark(T(E.pause ? "bl_pause_texte" : "bl_oral_texte")) + '</div>';
    if (E.pause) blancBouton(T("bl_suite"), () => { BL.etape++; blancSauver(); blancEtape(); });
    else blancBouton(T("bl_vers_oral"), () => { silence(); location.href = blancUrl("oral.html", { examen: "blanc" }); });
    return;
  }
  const pretes = E.parties.filter(blancPrete);
  $("zone").innerHTML = '<div class="bloc"><div class="petit">' + esc(n) + '</div><h2>' + esc(T("bl_e_" + E.id)) + '</h2>' +
    '<p><b>' + esc(T("bl_minutes", {m: E.minutes})) + '</b> · ' + esc(T("bl_e_" + E.id + "_s")) + '</p>' +
    '<p>' + esc(T("bl_e_" + E.id + "_q")) + '</p>' +
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
// les points d'une partie, bornes a son bareme ; res = {pts: {Lesen: x}, detail}
function blancBorner(id, res){
  const sur = BLANC_SUR[id], pts = (res && res.pts) || {}, out = { pts: {} };
  for (const c in sur) out.pts[c] = Math.min(sur[c], Math.max(0, Number(pts[c]) || 0));
  if (res && res.detail) out.detail = res.detail;
  return out;
}
function blancPartie(E, k){
  if (k >= E.parties.length) return blancFinEtape(E);
  const id = E.parties[k], ep = blancEpreuve(id);
  if (!ep){ BL.res[id] = { absent: true }; blancSauver(); return blancPartie(E, k + 1); }
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
  const cour = BL_COURANT = { id, fini, h: null };
  try{ cour.h = ep.lancer(fini, { numero: BL.numero || 0, zone: $("zone"), suite: $("suite"), rapide: RAPIDE, langue: LANGUE }) || {}; }
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
// LES GRILLES HORS CHRONO (6 nov., demande de telc-ecrire) : une partie qui fait noter l'eleve lui-meme (la grille
// I-IV de l'ecrit) appelle fini() des « Rendre », pendant le chrono, puis inscrit sa grille ; l'examen blanc les
// passe toutes ici, a la fin de l'examen, juste avant le verdict :
//   TELC.epreuve({id: "S", …, lancer, grille: (finiGrille, o) => { … ; finiGrille({pts: {Schreiben: 22}, detail}) }})
//   o = {detail (le detail rendu par fini()), numero, zone, suite, rapide, langue}.
//   Les points de la grille S'AJOUTENT a ceux de fini() ({remplace: true} : ils les remplacent), bornes au bareme.
function blancGrilles(){
  const attente = TELC.epreuves.filter(e => typeof e.grille === "function" && BL.res[e.id] && !BL.res[e.id].absent && !BL.res[e.id].grilleFaite);
  if (!attente.length) return false;
  const e = attente[0], r = BL.res[e.id];
  let rendu = false;
  const finiGrille = res => {
    if (rendu) return; rendu = true;
    const pts = (res && res.pts) || {}, avant = r.pts || {}, total = {};
    for (const c in BLANC_SUR[e.id]) total[c] = (res && res.remplace ? 0 : Number(avant[c]) || 0) + (Number(pts[c]) || 0);
    BL.res[e.id] = Object.assign(blancBorner(e.id, { pts: total, detail: r.detail }), { grilleFaite: true, grille: (res && res.detail) || null });
    blancSauver();
    blancVerdict();
  };
  blancEcran(T("bl_p_" + e.id));
  $("zone").innerHTML = "";
  DTZ.surRetour(() => { confirmer(T("quitter_q"), () => { silence(); accueil(); }, T("quitter")); return true; });
  try{ e.grille(finiGrille, { detail: r.detail || null, numero: BL.numero || 0, zone: $("zone"), suite: $("suite"), rapide: RAPIDE, langue: LANGUE }); }
  catch(err){ finiGrille({}); }
  return true;
}
function blancVerdict(){
  arreterChrono();
  BL = lire("blanc", null) || BL;
  if (!BL) return blancIntro();
  if (!BL.fini && blancGrilles()) return;
  // l'oral passe par sa page : sa part arrive dans res.Sp ; a defaut, le dernier oral fait depuis le debut de l'examen
  if (!BL.res.Sp){
    const r = lire("resultats", {}).Sp;
    if (r && r.quand >= BL.debut && typeof r.points === "number") BL.res.Sp = { pts: { Sprechen: r.points } };
  }
  blancEcran(T("bl_verdict"));
  DTZ.surRetour(() => { accueil(); return true; });
  const comp = {Lesen: 0, Hoeren: 0, Schreiben: 0, Sprechen: 0}, manque = [], compManque = new Set();
  for (const id in BLANC_SUR){
    const r = BL.res[id];
    if (!r || r.absent){ manque.push(id); Object.keys(BLANC_SUR[id]).forEach(c => compManque.add(c)); continue; }
    for (const c in BLANC_SUR[id]) comp[c] += Math.min(BLANC_SUR[id][c], Math.max(0, Number((r.pts || {})[c]) || 0));
  }
  // niveauTelc ne recoit que les competences completes : une seule qui manque, et c'est « incomplet »
  const pourNiveau = {};
  COMPETENCES.forEach(c => { if (!compManque.has(c)) pourNiveau[c] = comp[c]; });
  const niv = niveauTelc(pourNiveau), complet = niv !== "incomplet";
  const total = COMPETENCES.reduce((n, c) => n + comp[c], 0);
  const pct = n => Math.round(n / 240 * 100) + "%";
  const lignes = COMPETENCES.map(c => '<span>' + esc(T("bl_" + c)) + (compManque.has(c) ? ' · <i>' + esc(T("bl_incomplet")) + '</i>' : "") +
    '</span><b>' + vir(comp[c]) + ' / 60</b>').join("") +
    '<span>' + esc(T("bl_total")) + '</span><b>' + vir(total) + ' / 240</b>';
  $("zone").innerHTML =
    '<div class="bloc">' + blancMark(T(complet ? "bl_mark_" + niv : "bl_mark_partiel")) +
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
    ecrire("dernier", { date: new Date().toLocaleDateString(DATE_TELC),
      texte: complet ? T("bl_dernier", {n: vir(total), niv: T("niv_" + niv)}) : T("bl_dernier_partiel", {n: vir(total)}) });
    resultat("blanc", { points: total, niveau: niv, competences: comp });
    parler("resultat", { mode: "examen_blanc_telc", points: total, sur: 240, niveau: niv, competences: comp });
  }
}

// ---------------------------------------------------------------- les Sprachbausteine en mode examen
// En attendant le mode examen de sprachbausteine.js : la lettre entiere, les dix trous, a, b ou c, sans corrige.
// La lettre : parmi les series gardees a l'examen (PROFIL.seriesExamen), sinon toutes, a tour de role.
function examenSB(fini, o){
  const toutes = (typeof SB !== "undefined" && SB.series) || [];
  const pool = SERIES_EXAMEN > 0 ? toutes.slice(0, SERIES_EXAMEN) : toutes;
  if (!pool.length){ setTimeout(() => fini({}), 0); return {}; }
  const s = pool[((o && o.numero) || 0) % pool.length];
  const rep = s.luecken.map(() => null);
  const trouHtml = n => {
    const k = s.luecken.findIndex(l => l.n === n), r = rep[k];
    return '<span class="trou">' + (r === null ? "(" + n + ")" : esc(s.luecken[k].o[r])) + '</span>';
  };
  const rendre = () => {
    const lettre = '<div class="doc lettre" dir="ltr"><div class="k">' + (s.registre === "formel" ? "Brief" : "E-Mail") + '</div>' +
      '<div class="objet" lang="de">' + esc(s.betreff) + '</div>' +
      s.absaetze.map(p => '<p lang="de">' + esc(p).replace(/\{(\d+)\}/g, (m, n) => trouHtml(Number(n))) + '</p>').join("") + '</div>';
    const lignes = s.luecken.map((l, k) => '<div class="q"><div class="tete"><span class="num">' + l.n + '</span></div><div class="choix ligne">' +
      l.o.map((w, j) => '<button class="opt' + (rep[k] === j ? " pris" : "") + '" data-k="' + k + '" data-j="' + j + '"><b>' + "abc"[j] + '</b><span lang="de">' + esc(w) + '</span></button>').join("") +
      '</div></div>').join("");
    $("zone").innerHTML = '<div class="bloc"><p class="consigne" lang="de">' + esc(T("sb_consigne_de")) + '</p>' + lettre + '</div><div class="bloc">' + lignes + '</div>';
    $("zone").querySelectorAll("[data-k]").forEach(b => b.onclick = () => { rep[Number(b.dataset.k)] = Number(b.dataset.j); const y = window.scrollY; rendre(); window.scrollTo(0, y); });
  };
  let fait = false;
  const finir = () => {
    if (fait) return; fait = true;
    const bons = s.luecken.filter((l, k) => rep[k] === l.bon).length;
    fini({ pts: { Schreiben: bons / 2 }, detail: { serie: s.id, bons, sur: 10, rep: rep.slice() } });
  };
  rendre();
  blancBouton(T("bl_terminer_partie"), () => {
    const vides = rep.filter(r => r === null).length;
    if (vides) confirmer(T("bl_terminer_q", {n: vides}), finir, T("bl_terminer_partie")); else finir();
  });
  return { terminer: finir };
}
if (!blancEpreuve("SB")) TELC.epreuve({ id: "SB", ordre: 20, minutes: 0, sur: { Schreiben: 5 }, lancer: examenSB, secours: true });

// ---------------------------------------------------------------- les inscriptions
DTZ.examen({ id: "blanc", ordre: 10, titre: T("bl_titre"), sous: T("bl_sous"), lancer: blancIntro });
// une « partie » sans tuile (PROFIL.tuiles ne la nomme pas) : c'est par elle que telc.html?partie=BLANC rouvre
// l'examen blanc, au retour de la page de l'oral (&etape=verdict) ou quand on quitte l'oral en cours
DTZ.partie({ id: "BLANC", ordre: 99, titre: T("bl_titre"), sous: T("bl_sous"),
  ouvrir: () => (Q.get("etape") === "verdict" ? blancVerdict() : blancIntro()) });
