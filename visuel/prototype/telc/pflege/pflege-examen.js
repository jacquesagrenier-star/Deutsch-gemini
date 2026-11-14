// LE TELC DEUTSCH B1·B2 PFLEGE AVEC ELIF -- L'EXAMEN BLANC ET L'ENTRAINEMENT (14 nov. 2026, session
// pflege-examen ; decisions de Jacques du 14 nov. : la grande version, l'examen blanc COMPLET, les 9 langues).
//
// LE FORMAT EST CELUI DU TELC (pflege/FORMAT-TELC-PFLEGE.md), LE CONTENU EST A WORTANDO : 59 questions (ecoute 23,
// lecture 18, elements de langue 18), l'ecrit A ou B sur 20, l'oral en cinq temps sur 100, puis le certificat
// (bareme.js : l'oral decide). Les donnees : donnees/modell-1/<epreuve>.json ; l'interface : donnees/interface.json
// (fr, en) et donnees/langues/interface.<langue>.json ; les aides traduites : donnees/modell-1/langues/<epreuve>.<l>.json.
//
// CE QUI EST REPRIS DU MODULE TELC A2·B1, SANS Y TOUCHER : ../../dtz/commun.js (la voix, les pistes enregistrees,
// le lecteur unique d'iOS, le chronometre, le panneau, le stockage local, parler() vers l'app, DTZ.partie /
// DTZ.charger / DTZ.surRetour) et ../telc-commun.js (textesTelc, le dictionnaire des 7 autres langues).
// examen-blanc.js de l'A2·B1 n'est pas repris : ses etapes et son bareme y sont ecrits en dur.
//
// LE MODELE D'UNE QUESTION (toutes epreuves) : {cle, nr, typ, frage, o, bon, erkl_fr, erkl_en, relire}
//   typ « abc »   : trois choix, item.o ; « rf » : richtig (0) ou falsch (1) ; « zuord » : un choix dans la liste
//   de la partie (teil.wahl), avec « x » (aucune ligne) quand teil.mitX ; SB 1 : chaque mot une fois (teil.einmal).
// Une partie porte ses questions directement (teil.items), par conversation (teil.gespraeche) ou par texte
// (teil.texte) ; un document (doc) peut porter des trous {n}.
"use strict";

(() => {
const B = PF_BAREME;
const MODELL = "modell-1";
const EPR = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"];
const AUTRES = !["fr", "en"].includes(LANGUE);
const PF = { d: {}, tr: {}, items: [], parNr: {}, teile: [], lecture: null };
const ANTWORTZEIT = 8;          // secondes pour repondre apres chaque texte de l'ecoute, a l'examen
const PREFIXE_PISTE = "pf1-";   // les cles des pistes enregistrees (donnees/voix-pflege.json)

// ---------------------------------------------------------------- le chargement
function json(url, facultatif){
  return fetch(url, { cache: "no-cache" })
    .then(r => { if (!r.ok) throw new Error(url); return r.json(); })
    .catch(e => { if (facultatif) return {}; throw e; });
}
DTZ.charger(Promise.all([
  json("donnees/interface.json"),
  AUTRES ? json("donnees/langues/interface." + LANGUE + ".json", true) : Promise.resolve({}),
  // une epreuve pas encore ecrite laisse sa tuile grisee (« bientot ») : son fichier est facultatif
  ...EPR.map(e => json("donnees/" + MODELL + "/" + e + ".json", true)),
  ...EPR.map(e => AUTRES ? json("donnees/" + MODELL + "/langues/" + e + "." + LANGUE + ".json", true) : Promise.resolve({})),
  json("donnees/voix-pflege.json", true)
]).then(([ui, uiL, ...reste]) => {
  textesTelc({ fr: ui.fr, en: ui.en });
  if (AUTRES) Object.assign(TXT, uiL || {});
  EPR.forEach((e, k) => { PF.d[e] = reste[k]; Object.assign(PF.tr, reste[EPR.length + k] || {}); });
  const m = reste[2 * EPR.length] || {};
  for (const k in m) if (k[0] !== "_") DTZ_PISTES[k] = m[k];
  for (const e of EPR) for (const w in (PF.d[e].voix || {})) DTZ_VOIX[w] = { sexe: PF.d[e].voix[w].sexe };
  indexer();
  inscrire();
}));

// une aide traduite : le champ « X_<langue> », sinon le fichier de la langue (cle.X), sinon le francais
function tr(o, champ){
  if (!o) return "";
  return o[champ + "_" + LANGUE] || PF.tr[o.cle + "." + champ] || o[champ + "_fr"] || "";
}
const ABCX = "abcdefghij";
const lettre = v => v === "x" ? "x" : ABCX[v];
const groupesDe = teil => teil.gespraeche || teil.texte || null;
const itemsDe = teil => teil.items || [].concat(...(groupesDe(teil) || []).map(g => g.items));

function indexer(){
  PF.items = []; PF.teile = [];
  ["hoeren", "lesen", "sprachbausteine"].forEach(e => (PF.d[e].teile || []).forEach(t => {
    PF.teile.push({ epr: e, teil: t });
    itemsDe(t).forEach(it => { PF.items.push({ epr: e, teil: t, it }); PF.parNr[it.nr] = { epr: e, teil: t, it }; });
  }));
  PF.items.sort((a, b) => a.it.nr - b.it.nr);
}
function choixDe(teil, it){
  if (it.typ === "abc") return it.o.map((w, k) => ({ v: k, l: "abc"[k], t: w }));
  if (it.typ === "rf") return [{ v: 0, l: "", t: "richtig" }, { v: 1, l: "", t: "falsch" }];
  const w = (teil.wahl || []).map((x, k) => ({ v: k, l: ABCX[k], t: teil.einmal ? (typeof x === "string" ? x : x.titre) : "" }));
  if (teil.mitX) w.push({ v: "x", l: "x", t: "" });
  return w;
}
const juste = (it, r) => r !== null && r !== undefined && String(r) === String(it.bon);
const pointsDe = (rep, epr) => PF.items.filter(x => !epr || x.epr === epr).filter(x => juste(x.it, rep[x.it.nr])).length;
const sur = epr => PF.items.filter(x => x.epr === epr).length;

// ---------------------------------------------------------------- petits outils d'ecran
function ecran(titre){ silence(); arreterSon(); fermerPanneau(); $("titre").textContent = titre || T("pf_titre"); $("suite").hidden = true; window.scrollTo(0, 0); }
function bouton(texte, action){ const s = $("suite"); s.hidden = false; s.disabled = false; s.textContent = texte; s.onclick = () => { s.hidden = true; action(); }; }
// Jonas, le tuteur (Praxisanleiter) : pas d'image avant la validation des personnages, un monogramme
const jonas = texte => '<div class="mark"><span class="mono" aria-hidden="true">J</span><div class="bulle">' + esc(texte) + '</div></div>';
const deuxPts = DEUX_POINTS_TELC;
function garderScroll(f){ const y = window.scrollY; f(); window.scrollTo(0, y); }
function fmt(s){ s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); }
const vir = n => { const x = String(Math.round(n * 10) / 10); return ["fr", "tr", "uk", "ru", "pl", "pt"].includes(LANGUE) ? x.replace(".", ",") : x; };
const nomNiveau = n => T(n === "b2" ? "pf_niv_b2" : n === "b1" ? "pf_niv_b1" : "pf_niv_unter");

// ================================================================= LES QUESTIONS
// mode : « ex » (examen : rien n'est corrige), « tr » (entrainement : on repond, puis « Corriger »), « co » (corrige)
function carteQuestion(teil, it, rep, mode, opts){
  const r = rep[it.nr], ch = choixDe(teil, it), corrige = mode === "co";
  const pris = teil.einmal ? new Set(Object.keys(rep).filter(n => Number(n) !== it.nr && itemsDe(teil).some(i => i.nr === Number(n))).map(n => String(rep[n]))) : new Set();
  const ligne = it.typ !== "abc" && !teil.einmal;
  const boutons = ch.map(c => {
    let cls = "opt";
    if (corrige){ if (String(c.v) === String(it.bon)) cls += " juste"; else if (String(c.v) === String(r)) cls += " faux"; }
    else if (String(c.v) === String(r)) cls += " pris";
    const occupe = !corrige && pris.has(String(c.v));
    return '<button class="' + cls + (occupe ? " occupe" : "") + '" data-nr="' + it.nr + '" data-v="' + c.v + '"' + (corrige ? " disabled" : "") +
      (occupe ? ' aria-label="' + esc(T("pf_mot_pris", { m: c.t || c.l })) + '"' : "") + '>' +
      (c.l ? '<b>' + c.l + '</b>' : "") + (c.t ? '<span lang="de">' + esc(c.t) + '</span>' : "") + '</button>';
  }).join("");
  let aide = "";
  if (corrige){
    const ok = juste(it, r), bonne = ch.find(c => String(c.v) === String(it.bon));
    const dite = GUILLEMETS_TELC[0] + (bonne.l ? bonne.l + (bonne.t ? " · " : "") : "") + (bonne.t || "").replace(/[.…]$/, "") + GUILLEMETS_TELC[1];
    aide = '<div class="aide"><div class="verdict ' + (ok ? "ok" : "ko") + '">' +
      esc(ok ? T("pf_juste") : r === null || r === undefined ? T("pf_vide", { m: dite }) : T("pf_faux", { m: dite })) + '</div>' +
      (tr(it, "erkl") ? '<div class="erkl">' + esc(tr(it, "erkl")) + '</div>' : "") + '</div>';
  }
  const frage = it.frage ? '<span class="frage" lang="de">' + esc(it.frage) + '</span>'
    : '<span class="frage">' + esc(it.wer_nom ? T("pf_meinung", { n: it.wer_nom }) : T("pf_ta_reponse")) + '</span>';
  return '<div class="q' + (opts && opts.ici ? " ici" : "") + '" id="q' + it.nr + '"><div class="tete"><span class="num">' + it.nr + '</span>' + frage + '</div>' +
    '<div class="choix' + (ligne ? " ligne" : "") + '">' + boutons + '</div>' + aide + '</div>';
}

// un document : en-tete, objet, paragraphes ; {n} devient le trou n (rempli par la reponse, ou corrige)
function docHtml(doc, teil, rep, mode){
  if (!doc) return "";
  const trou = n => {
    const it = itemsDe(teil).find(i => i.nr === n), r = rep[n];
    if (!it) return "(" + n + ")";
    const ch = choixDe(teil, it), c = ch.find(x => String(x.v) === String(r));
    const cls = mode === "co" ? (juste(it, r) ? " ok" : " ko") : "";
    return '<a class="trou' + cls + '" href="#q' + n + '">' + (c ? esc(c.t || c.l) : "(" + n + ")") + '</a>';
  };
  const para = p => esc(p).replace(/\{(\d+)\}/g, (m, n) => trou(Number(n)));
  return '<div class="doc lettre" dir="ltr">' +
    (doc.art ? '<div class="k" lang="de">' + esc(doc.art) + '</div>' : "") +
    (doc.kopf || []).map(l => '<div class="petit" lang="de">' + esc(l) + '</div>').join("") +
    (doc.betreff ? '<div class="objet" lang="de">' + esc(doc.betreff) + '</div>' : "") +
    (doc.absaetze || []).map(p => '<p lang="de">' + para(p) + '</p>').join("") + '</div>';
}

// la liste a associer (objets des courriels, phrases de l'ecoute 4, plan de soins, mots de SB 1)
function wahlHtml(teil){
  if (!teil.wahl) return "";
  if (teil.einmal) return '<div class="doc kasten" dir="ltr">' + teil.wahl.map((w, k) => '<span><b>' + ABCX[k] + '</b> <span lang="de">' + esc(w) + '</span></span>').join("") + '</div>';
  return '<div class="doc liste" dir="ltr">' + teil.wahl.map((w, k) => {
    if (typeof w === "string") return '<p><b>' + ABCX[k] + '</b> <span lang="de">' + esc(w) + '</span></p>';
    return '<div class="plan"><div class="plan-t"><b>' + ABCX[k] + '</b> <span lang="de">' + esc(w.titre) + '</span></div>' +
      (w.lignes || []).map(([e, t]) => '<div class="plan-l" lang="de"><i>' + esc(e) + '</i> ' + esc(t) + '</div>').join("") + '</div>';
  }).join("") + '</div>';
}

function transcription(audio){
  return '<details class="transcription"><summary>' + esc(T("pf_transcription")) + '</summary>' +
    audio.map(l => '<p lang="de"><b>' + esc(qui(l.wer)) + '</b>' + deuxPts + esc(l.text) + '</p>').join("") + '</details>';
}
function qui(wer){
  for (const e of EPR){ const v = (PF.d[e].voix || {})[wer]; if (v) return (v.nom || wer).split(",")[0].split(" (")[0]; }
  return wer;
}

// ---------------------------------------------------------------- une partie a l'ecran
// o : {mode, rep, ecoute (true : boutons d'ecoute de l'entrainement), ici (la cle du texte qui passe), apres}
function vueTeil(epr, teil, o){
  const rep = o.rep, mode = o.mode;
  let h = '<div class="bloc"><div class="section">' + esc(teil.titre) + '</div>' +
    '<p class="consigne" lang="de">' + esc(teil.consigne_de) + '<span class="fr">' + esc(tr(teil, "consigne")) + '</span></p>' +
    (o.entete || "") + '</div>';
  const ecouter = (cle, audio) => o.ecoute ? '<button class="jouer" data-jouer="' + cle + '">' + ICONE_SON + ' ' + esc(T("pf_ecouter")) + '</button>' : "";
  const corrigeAudio = audio => mode === "co" && audio ? transcription(audio) : "";
  // l'intro (le rapport d'admission de la lecture 2), la liste a associer, le document a trous
  if (teil.intro) h += '<div class="bloc">' + docHtml(teil.intro, teil, rep, mode) + '</div>';
  if (teil.wahl) h += '<div class="bloc">' + wahlHtml(teil) + '</div>';
  if (teil.doc) h += '<div class="bloc">' + docHtml(teil.doc, teil, rep, mode) + '</div>';
  // l'exemple (ecoute 1 et 4)
  if (teil.beispiel){
    const b = teil.beispiel, c = choixDe(teil, b).find(x => String(x.v) === String(b.bon));
    h += '<div class="bloc exemple' + (o.ici === b.cle ? " ici" : "") + '"><div class="section">' + esc(T("pf_beispiel")) + '</div>' +
      ecouter(b.cle, b.audio) +
      (b.frage ? '<p lang="de"><b>' + esc(b.frage) + '</b></p>' : '<p>' + esc(T("pf_meinung", { n: b.wer_nom || "" })) + '</p>') +
      '<p class="petit">' + esc(T("pf_solution")) + deuxPts + '<b lang="de">' + esc(c.l + (c.t ? " " + c.t : "")) + '</b></p>' +
      (tr(b, "erkl") && o.mode !== "ex" ? '<p class="petit">' + esc(tr(b, "erkl")) + '</p>' : "") + corrigeAudio(b.audio) + '</div>';
  }
  const groupes = groupesDe(teil);
  if (groupes){
    groupes.forEach((g, k) => {
      h += '<div class="bloc' + (o.ici === g.cle ? " ici" : "") + '">' +
        '<div class="section">' + esc(T(teil.gespraeche ? "pf_gespraech" : "pf_text", { n: k + 1 })) + (g.titre ? " · " + '<span lang="de">' + esc(g.titre) + '</span>' : "") + '</div>' +
        (tr(g, "situation") && mode !== "ex" ? '<p class="petit">' + esc(tr(g, "situation")) + '</p>' : "") +
        ecouter(g.cle, g.audio) + (g.doc ? docHtml(g.doc, teil, rep, mode) : "") +
        g.items.map(it => carteQuestion(teil, it, rep, mode)).join("") + corrigeAudio(g.audio) + '</div>';
    });
  } else {
    // une partie a un seul enregistrement (ecoute 3) : le bouton d'ecoute une fois, en tete
    if (teil.audio) h += '<div class="bloc' + (o.ici === teil.cle ? " ici" : "") + '">' + ecouter(teil.cle, teil.audio) +
      (tr(teil, "situation") && mode !== "ex" ? '<p class="petit">' + esc(tr(teil, "situation")) + '</p>' : "") + corrigeAudio(teil.audio) + '</div>';
    h += '<div class="bloc">' + teil.items.map(it => {
      const avant = it.doc ? docHtml(it.doc, teil, rep, mode) : "";
      return (it.audio ? '<div class="' + (o.ici === it.cle ? "ici" : "") + '">' + ecouter(it.cle, it.audio) + '</div>' : "") + avant +
        carteQuestion(teil, it, rep, mode, { ici: o.ici === it.cle }) + (it.audio ? corrigeAudio(it.audio) : "");
    }).join("") + '</div>';
  }
  return h;
}

// les reponses : un toucher sur un choix ; SB 1 : un mot deja pris ailleurs y est retire
function brancherChoix(rep, mode, rendre){
  $("zone").querySelectorAll("[data-nr][data-v]").forEach(b => b.onclick = () => {
    if (mode === "co") return;
    const nr = Number(b.dataset.nr), v = b.dataset.v === "x" ? "x" : Number(b.dataset.v), x = PF.parNr[nr];
    if (x.teil.einmal) for (const n in rep) if (Number(n) !== nr && String(rep[n]) === String(v) && itemsDe(x.teil).some(i => i.nr === Number(n))) rep[n] = null;
    rep[nr] = String(rep[nr]) === String(v) ? null : v;
    garderScroll(rendre);
  });
}
function cleAudio(teil, cle){
  if (teil.beispiel && teil.beispiel.cle === cle) return teil.beispiel.audio;
  if (teil.cle === cle) return teil.audio;
  const g = (groupesDe(teil) || []).find(x => x.cle === cle); if (g) return g.audio;
  const it = itemsDe(teil).find(x => x.cle === cle); return it && it.audio;
}
const jouerCle = (cle, audio) => jouerPiste(PREFIXE_PISTE + cle, audio);

// ================================================================= L'ENTRAINEMENT PAR EPREUVE
// Une epreuve a la fois, partie par partie, sans chronometre ; « Corriger » montre les reponses, l'explication et,
// pour l'ecoute, la transcription. Rien ne compte pour l'examen blanc.
function entrainement(epr, k){
  const teile = PF.d[epr].teile;
  k = k || 0;
  const teil = teile[k], rep = {}; let mode = "tr";
  ecran(T("pf_epr_" + epr));
  DTZ.surRetour(() => { accueil(); return true; });
  const rendre = () => {
    $("zone").innerHTML = ongletsTeile(epr, k) + (k === 0 && mode === "tr" ? '<div class="bloc">' + jonas(T("pf_jonas_" + epr)) + '</div>' : "") +
      vueTeil(epr, teil, { mode, rep, ecoute: epr === "hoeren" });
    brancherChoix(rep, mode, rendre);
    $("zone").querySelectorAll("[data-jouer]").forEach(b => b.onclick = () => { debloquerSon(); arreterSon(); jouerCle(b.dataset.jouer, cleAudio(teil, b.dataset.jouer)); });
    $("zone").querySelectorAll("[data-teil]").forEach(b => b.onclick = () => entrainement(epr, Number(b.dataset.teil)));
    if (mode === "tr") bouton(T("pf_corriger"), () => {
      mode = "co";
      itemsDe(teil).forEach(it => { if (rep[it.nr] !== null && rep[it.nr] !== undefined) parler("exercice", { juste: juste(it, rep[it.nr]) }); });
      const n = itemsDe(teil).filter(it => juste(it, rep[it.nr])).length;
      resultat("tr_" + teil.cle, { bons: n, sur: itemsDe(teil).length });
      rendre(); window.scrollTo(0, 0);
    });
    else {
      const n = itemsDe(teil).filter(it => juste(it, rep[it.nr])).length;
      const tete = $("zone").querySelector(".bloc .section");
      if (tete) tete.insertAdjacentHTML("afterend", '<div class="score">' + n + ' / ' + itemsDe(teil).length + '</div>');
      if (k + 1 < teile.length) bouton(T("pf_partie_suivante", { t: teile[k + 1].titre }), () => entrainement(epr, k + 1));
      else bouton(T("pf_retour_accueil"), accueil);
    }
  };
  rendre();
}
function ongletsTeile(epr, k){
  const teile = PF.d[epr].teile;
  return '<div class="bloc"><div class="onglets">' + teile.map((t, j) => '<button class="onglet' + (j === k ? " actif" : "") + '" data-teil="' + j + '">' + esc(T("pf_teil", { n: t.teil })) + '</button>').join("") + '</div></div>';
}

// ================================================================= L'EXAMEN BLANC
// L'etat (stockage local wortando_telc_pflege_blanc) : {debut, etape, rep, schreiben, sprechen, vorbereitung,
// grilles, fini}. On peut quitter et reprendre : l'etape en cours recommence, les reponses deja donnees restent.
const ETAPES = ["hoeren", "lesen", "schreiben", "vorbereitung", "sprechen", "grilles"];
const MINUTES = { hoeren: 25, lesen: 60, schreiben: 30, vorbereitung: 20, sprechen: 16 };
let BL = null;
const sauver = () => ecrire("blanc", BL);
function garderRetourExamen(){
  DTZ.surRetour(() => { confirmer(T("pf_quitter_q"), () => { arreterLecture(); arreterChrono(); accueil(); }, T("pf_quitter")); return true; });
}
function blancIntro(){
  ecran(T("pf_blanc"));
  BL = lire("blanc", null);
  DTZ.surRetour(() => { accueil(); return true; });
  const enCours = BL && !BL.fini;
  const lignes = ETAPES.map((e, k) => '<div class="mode" style="cursor:default"><b>' + (k + 1) + '. ' + esc(T("pf_e_" + e)) + '</b>' +
    '<span>' + esc(T("pf_e_" + e + "_s")) + '</span><span style="font-weight:600;color:var(--encre)">' + esc(T("pf_e_" + e + "_q")) + '</span></div>').join("");
  $("zone").innerHTML = '<div class="bloc">' + jonas(T("pf_blanc_intro")) + '</div>' +
    '<div class="bloc"><h2>' + esc(T("pf_deroule")) + '</h2>' + lignes +
    (enCours ? '<button class="secondaire" id="pfNouveau">' + esc(T("pf_recommencer")) + '</button>' : "") + '</div>';
  if (enCours){
    bouton(T("pf_reprendre", { e: T("pf_e_" + ETAPES[BL.etape]) }), etape);
    $("pfNouveau").onclick = () => confirmer(T("pf_recommencer_q"), nouveau, T("pf_recommencer"));
  } else bouton(T("pf_commencer"), nouveau);
}
function nouveau(){
  BL = { debut: Date.now(), etape: 0, rep: {}, schreiben: null, sprechen: {}, vorbereitung: "", grilles: {}, fini: false };
  sauver(); etape();
}
function suivante(){ arreterChrono(); BL.etape++; sauver(); etape(); }
function etape(){
  arreterChrono();
  const e = ETAPES[BL.etape];
  if (!e) return verdict();
  ecran(T("pf_e_" + e));
  garderRetourExamen();
  if (e === "grilles") return grilles();
  $("zone").innerHTML = '<div class="bloc"><div class="petit">' + esc(T("pf_etape", { n: BL.etape + 1, sur: ETAPES.length })) + '</div>' +
    '<h2>' + esc(T("pf_e_" + e)) + '</h2><p><b>' + esc(T("pf_minutes", { m: MINUTES[e] })) + '</b> · ' + esc(T("pf_e_" + e + "_s")) + '</p>' +
    '<p>' + esc(T("pf_e_" + e + "_q")) + '</p><p class="petit">' + esc(T(e === "hoeren" ? "pf_entree_ecoute" : e === "vorbereitung" ? "pf_entree_vorb" : e === "sprechen" ? "pf_entree_oral" : "pf_entree")) + '</p></div>';
  bouton(T("pf_go"), () => {
    debloquerSon();
    if (e === "hoeren") return examenHoeren();
    if (e === "lesen") return examenLesen();
    if (e === "schreiben") return schreiben("ex");
    if (e === "vorbereitung") return vorbereitung();
    if (e === "sprechen") return sprechen("ex");
  });
}

// ---------------------------------------------------------------- l'ecoute, a l'examen : une seule fois, a la suite
function arreterLecture(){ if (PF.lecture) PF.lecture.stop = true; PF.lecture = null; arreterSon(); }
async function examenHoeren(){
  const L = PF.lecture = { stop: false };
  const teile = PF.d.hoeren.teile;
  chrono(MINUTES.hoeren * 60, "haut");
  const rendre = (teil, ici, info) => garderScroll(() => {
    $("zone").innerHTML = '<div class="bloc"><div class="petit">' + esc(info || "") + '</div></div>' + vueTeil("hoeren", teil, { mode: "ex", rep: BL.rep, ici });
    brancherChoix(BL.rep, "ex", () => { sauver(); rendre(teil, ici, info); });
  });
  const pause = async (s, teil, ici, libelle) => {
    for (let t = s; t > 0; t--){ if (L.stop) return; rendre(teil, ici, T(libelle, { s: t })); await attendre(1); }
  };
  for (const teil of teile){
    if (L.stop) return;
    window.scrollTo(0, 0);
    rendre(teil, null, T("pf_ecoute_consigne"));
    await jouerCle(teil.cle + "-consigne", teil.audio_consigne); if (L.stop) return;
    if (teil.lesezeit) { await pause(teil.lesezeit, teil, null, "pf_ecoute_lire"); if (L.stop) return; }
    const morceaux = [];
    if (teil.beispiel) morceaux.push(teil.beispiel);
    if (teil.audio) morceaux.push(teil);
    else (groupesDe(teil) || teil.items).forEach(g => morceaux.push(g));
    for (const m of morceaux){
      if (L.stop) return;
      rendre(teil, m.cle, T("pf_ecoute_en_cours"));
      const q = document.querySelector(".ici"); if (q) try{ q.scrollIntoView({ block: "start", behavior: "smooth" }); }catch(e){}
      await jouerCle(m.cle, m.audio); if (L.stop) return;
      await pause(m === teil ? ANTWORTZEIT * 2 : ANTWORTZEIT, teil, m.cle, "pf_ecoute_repondre");
    }
  }
  if (L.stop) return;
  PF.lecture = null; arreterChrono(); sauver();
  $("zone").innerHTML = '<div class="bloc"><h2>' + esc(T("pf_etape_finie")) + '</h2><p>' + esc(T("pf_ecoute_finie")) + '</p></div>';
  bouton(T("pf_etape_suivante"), suivante);
}

// ---------------------------------------------------------------- lecture + elements de langue : 60 min, onglets libres
function examenLesen(){
  const teile = PF.teile.filter(x => x.epr !== "hoeren");
  let k = 0, fini = false;
  const finir = () => { if (fini) return; fini = true; arreterChrono(); sauver(); suivante(); };
  chrono(RAPIDE ? 30 : MINUTES.lesen * 60, "bas", finir);
  const rendre = () => {
    const x = teile[k];
    const onglets = '<div class="bloc"><div class="onglets">' + teile.map((t, j) => {
      const its = itemsDe(t.teil), faits = its.filter(i => BL.rep[i.nr] !== null && BL.rep[i.nr] !== undefined).length;
      return '<button class="onglet' + (j === k ? " actif" : "") + '" data-ong="' + j + '">' + esc(t.teil.court || t.teil.titre) + ' · ' + faits + '/' + its.length + '</button>';
    }).join("") + '</div></div>';
    $("zone").innerHTML = onglets + vueTeil(x.epr, x.teil, { mode: "ex", rep: BL.rep });
    brancherChoix(BL.rep, "ex", () => { sauver(); rendre(); });
    $("zone").querySelectorAll("[data-ong]").forEach(b => b.onclick = () => { k = Number(b.dataset.ong); rendre(); window.scrollTo(0, 0); });
    const vides = PF.items.filter(i => i.epr !== "hoeren" && (BL.rep[i.it.nr] === null || BL.rep[i.it.nr] === undefined)).length;
    if (k + 1 < teile.length) bouton(T("pf_partie_suivante", { t: teile[k + 1].teil.court || teile[k + 1].teil.titre }), () => { k++; rendre(); window.scrollTo(0, 0); });
    else bouton(T("pf_rendre"), () => vides ? confirmer(T("pf_rendre_q", { n: vides }), finir, T("pf_rendre")) : finir());
  };
  rendre();
}

// ================================================================= L'ECRIT
// A (le rapport d'admission) ou B (le rapport biographique) : la fiche, 120-170 mots. Le contenu se calcule sur
// la fiche (chaque information a ses mots reperes) ; forme, correction et vocabulaire se notent a la grille.
const mots = t => (String(t || "").match(/[A-Za-zÄÖÜäöüß0-9-]+/g) || []).length;
function infosTrouvees(aufgabe, texte){
  const t = String(texte || "").toLowerCase();
  return aufgabe.infos.map(i => ({ i, ok: i.mots.some(m => new RegExp(m, "i").test(t)) }));
}
function ficheHtml(a){
  return '<div class="doc fiche" dir="ltr"><div class="k" lang="de">' + esc(a.fiche.titre) + '</div>' +
    (a.fiche.kopf || []).map(l => '<div class="petit" lang="de">' + esc(l) + '</div>').join("") +
    a.fiche.rubriken.map(r => '<div class="rubrik"><div class="rubrik-t" lang="de">' + esc(r.titre) + '</div>' +
      r.zeilen.map(([f, w]) => '<div class="zeile" lang="de"><span>' + esc(f) + '</span><b>' + esc(w) + '</b></div>').join("") + '</div>').join("") + '</div>';
}
function schreiben(mode, choix){
  const S = PF.d.schreiben;
  const ex = mode === "ex";
  ecran(T("pf_epr_schreiben"));
  if (ex) garderRetourExamen(); else DTZ.surRetour(() => { accueil(); return true; });
  const etat = ex ? (BL.schreiben = BL.schreiben || { aufgabe: null, text: "" }) : { aufgabe: choix || null, text: "" };
  if (!etat.aufgabe){
    $("zone").innerHTML = (ex ? "" : '<div class="bloc">' + jonas(T("pf_jonas_schreiben")) + '</div>') +
      '<div class="bloc"><p class="consigne" lang="de">' + esc(S.consigne_de) + '<span class="fr">' + esc(tr(S, "consigne")) + '</span></p>' +
      S.aufgaben.map(a => '<button class="mode" data-auf="' + a.id + '"><b lang="de">' + esc(T("pf_aufgabe", { a: a.id })) + ' · ' + esc(a.titre) + '</b><span>' + esc(tr(a, "resume")) + '</span></button>').join("") + '</div>';
    $("zone").querySelectorAll("[data-auf]").forEach(b => b.onclick = () => { etat.aufgabe = b.dataset.auf; if (ex) sauver(); schreiben(mode, etat.aufgabe); });
    return;
  }
  const a = S.aufgaben.find(x => x.id === etat.aufgabe);
  let fini = false;
  const rendreTexte = () => {
    if (fini) return; fini = true; arreterChrono();
    etat.text = $("pfTexte") ? $("pfTexte").value : etat.text;
    if (ex){ sauver(); suivante(); } else grilleSchreiben(a, etat.text, g => {
      const p = B.punkteSchreiben(g);
      resultat("tr_schreiben", { aufgabe: a.id, punkte: p });
      parler("exercice", { juste: p >= 7 });
    });
  };
  if (ex) chrono(RAPIDE ? 30 : MINUTES.schreiben * 60, "bas", rendreTexte);
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("pf_aufgabe", { a: a.id })) + ' · <span lang="de">' + esc(a.titre) + '</span></div>' +
      '<p class="consigne" lang="de">' + esc(a.consigne_de) + '<span class="fr">' + esc(tr(a, "consigne")) + '</span></p></div>' +
    '<div class="bloc">' + ficheHtml(a) + '</div>' +
    (ex ? "" : '<div class="bloc"><details><summary>' + esc(T("pf_redemittel")) + '</summary><ul class="redemittel">' + a.redemittel.map(r => '<li lang="de">' + esc(r) + '</li>').join("") + '</ul></details></div>') +
    '<div class="bloc"><textarea id="pfTexte" lang="de" rows="12" spellcheck="false" placeholder="' + esc(T("pf_ecrire_ici")) + '">' + esc(etat.text || "") + '</textarea>' +
      '<p class="petit" id="pfMots"></p></div>';
  const ta = $("pfTexte"), compte = () => {
    const n = mots(ta.value);
    $("pfMots").textContent = T("pf_mots", { n }) + (n < 120 ? " · " + T("pf_mots_peu") : n > 170 ? " · " + T("pf_mots_trop") : "");
  };
  ta.oninput = () => { compte(); if (ex){ etat.text = ta.value; sauver(); } };
  compte();
  bouton(T("pf_rendre_texte"), () => mots(ta.value) < 20 ? confirmer(T("pf_rendre_court"), rendreTexte, T("pf_rendre")) : rendreTexte());
}

// la grille de l'ecrit : le contenu calcule, les trois autres criteres choisis sur les descripteurs, le modele
function grilleSchreiben(a, texte, quandFini, libelleFin){
  ecran(T("pf_grille_schreiben"));
  const trouvees = infosTrouvees(a, texte), n = trouvees.filter(x => x.ok).length;
  const inhalt = B.inhaltPunkte(a.infos.length, n);
  const g = { inhalt, gestaltung: null, korrektheit: null, wortschatz: null };
  const rendre = () => {
    const pret = ["gestaltung", "korrektheit", "wortschatz"].every(k => g[k] !== null) || !inhalt;
    $("zone").innerHTML =
      '<div class="bloc"><h2>' + esc(T("pf_crit_inhalt")) + ' · ' + inhalt + ' / 5</h2>' +
        '<p class="petit">' + esc(T("pf_inhalt_explique", { n, sur: a.infos.length })) + '</p>' +
        '<ul class="crit">' + trouvees.map(x => '<li class="' + (x.ok ? "ok" : "") + '">' + esc(tr(x.i, "label")) + '</li>').join("") + '</ul>' +
        (inhalt ? "" : '<p><b>' + esc(T("pf_inhalt_zero")) + '</b></p>') + '</div>' +
      (inhalt ? ["gestaltung", "korrektheit", "wortschatz"].map(k => selecteur(k, 5, g[k], "schreiben")).join("") : "") +
      '<div class="bloc"><details><summary>' + esc(T("pf_ton_texte")) + '</summary><p lang="de" class="entendu">' + esc(texte || "—") + '</p></details>' +
        '<details><summary>' + esc(T("pf_modele")) + '</summary>' + a.modele.map(p => '<p lang="de">' + esc(p) + '</p>').join("") + '</details></div>' +
      '<div class="bloc"><div class="score">' + B.punkteSchreiben(g) + ' / 20</div><p class="petit" style="text-align:center">' + esc(nomNiveau(B.niveauSchreiben(B.punkteSchreiben(g)))) + '</p>' +
        '<p class="petit">' + esc(T("pf_estimation_ecrit")) + '</p></div>';
    brancherSelecteurs(g, () => garderScroll(rendre));
    if (pret) bouton(libelleFin || T("pf_terminer"), () => quandFini(Object.assign({}, g)));
    else $("suite").hidden = true;
  };
  rendre();
}
// un critere note sur ses crans : les six descripteurs (B2 tres bien … 0), on touche celui qui decrit le mieux
function selecteur(cle, surN, valeur, epr){
  const crans = B.CRANS[surN];
  return '<div class="bloc"><h2>' + esc(T("pf_crit_" + cle)) + (valeur !== null && valeur !== undefined ? ' · ' + valeur + ' / ' + surN : "") + '</h2>' +
    '<p class="petit">' + esc(T("pf_crit_" + cle + "_q")) + '</p><div class="choix">' +
    crans.map((c, k) => '<button class="opt' + (valeur === c ? " pris" : "") + '" data-crit="' + cle + '" data-val="' + c + '"><b>' + B.STUFEN[k] + '</b><span>' +
      esc(T("pf_desc_" + epr + "_" + cle + "_" + k)) + '</span></button>').join("") + '</div></div>';
}
function brancherSelecteurs(g, rendre){
  $("zone").querySelectorAll("[data-crit]").forEach(b => b.onclick = () => { g[b.dataset.crit] = Number(b.dataset.val); rendre(); });
}

// ================================================================= L'ORAL
// La Pruferin (Frau Neumann) mene l'entretien, Elif est la partenaire. 1A la photo, 1B les questions, 2A l'expose
// (un sujet sur deux), 2B les questions sur l'expose, 3 la discussion avec Elif. Le micro ecoute (ou on ecrit) ;
// les points de tache s'estiment sur ce qui a ete dit (criteres des donnees), la langue a la grille.
const Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
const DANS_APP = window.parent !== window;
let ecouteApp = null;
window.addEventListener("message", e => {
  const d = e.data;
  if (!d || d.source !== "wortando-app" || d.type !== "micro" || !ecouteApp) return;
  if (d.etat === "texte") ecouteApp.surTexte(d.texte || "");
  else if (d.etat === "fin"){ const f = ecouteApp; ecouteApp = null; f.surFin(d.texte || ""); }
  else if (d.etat === "indisponible"){ const f = ecouteApp; ecouteApp = null; f.surFin(null); }
});
// le meme micro que l'oral du telc A2·B1 (oral.html, ecouter()), recopie ici
function ecouterMicro(surTexte, surFin){
  if (Reco){
    let actif = true, finals = "", provisoire = "", reco = null, fini = false;
    const total = () => (finals + " " + provisoire).replace(/\s+/g, " ").trim();
    const terminer = () => { if (fini) return; fini = true; surFin(total()); };
    const lancer = () => {
      reco = new Reco(); reco.lang = "de-DE"; reco.continuous = true; reco.interimResults = true;
      reco.onresult = ev => {
        provisoire = "";
        for (let i = ev.resultIndex; i < ev.results.length; i++){ const r = ev.results[i]; if (r.isFinal) finals += " " + r[0].transcript; else provisoire += " " + r[0].transcript; }
        surTexte(total());
      };
      reco.onerror = ev => { if (ev && (ev.error === "not-allowed" || ev.error === "service-not-allowed")){ actif = false; if (!finals){ fini = true; surFin(null); } } };
      reco.onend = () => { if (actif){ try{ lancer(); }catch(e){ terminer(); } } else setTimeout(terminer, 150); };
      reco.start();
    };
    try{ lancer(); }catch(e){ setTimeout(() => surFin(null), 0); return { arreter(){} }; }
    return { arreter(){ actif = false; try{ reco.stop(); }catch(e){} setTimeout(terminer, 1800); } };
  }
  if (DANS_APP){
    ecouteApp = { surTexte, surFin };
    parler("micro", { action: "start", langue: "de-DE" });
    return { arreter(){ parler("micro", { action: "stop" }); } };
  }
  setTimeout(() => surFin(null), 0);
  return { arreter(){} };
}
// le tour de parole : le micro (avec le temps qui passe et la limite), ou le clavier ; quandFini({text, sec})
function aToi(conteneur, consigne, limiteS, quandFini){
  const z = document.createElement("div"); z.className = "micro-zone";
  z.innerHTML = '<button class="micro" type="button" aria-label="' + esc(T("pf_parler")) + '">🎙</button><div class="micro-info"></div>' +
    '<div class="entendu" lang="de" hidden></div><button class="lien" type="button">' + esc(T("pf_ecrire_place")) + '</button>';
  conteneur.appendChild(z);
  const m = z.querySelector(".micro"), info = z.querySelector(".micro-info"), entendu = z.querySelector(".entendu"), clavier = z.querySelector(".lien");
  info.textContent = consigne;
  let ec = null, debut = 0, minuterie = null, coupe = null, rendu = false;
  const rendre = (t, sec) => { if (rendu) return; rendu = true; z.remove(); quandFini({ text: t || "", sec: sec || 0 }); };
  const arreter = () => { if (!ec) return; clearInterval(minuterie); clearTimeout(coupe); m.classList.remove("ecoute"); m.textContent = "…"; m.disabled = true; ec.arreter(); ec = null; };
  m.onclick = () => {
    if (ec){ arreter(); return; }
    silence(); entendu.hidden = false; entendu.textContent = "";
    m.classList.add("ecoute"); m.textContent = "■"; debut = Date.now();
    const tic = () => { info.textContent = T("pf_ecoute_tic", { t: fmt((Date.now() - debut) / 1000), l: fmt(limiteS) }); };
    tic(); minuterie = setInterval(tic, 500);
    coupe = setTimeout(arreter, limiteS * 1000);
    ec = ecouterMicro(t => { entendu.textContent = t; }, t => {
      clearInterval(minuterie); clearTimeout(coupe); ec = null;
      if (t === null){ m.classList.remove("ecoute"); m.textContent = "🎙"; m.disabled = false; info.textContent = T("pf_micro_ko"); clavier.click(); return; }
      rendre(t, (Date.now() - debut) / 1000);
    });
  };
  clavier.onclick = () => {
    if (ec) return;
    clavier.remove(); m.remove();
    const ta = document.createElement("textarea"); ta.lang = "de"; ta.rows = 5; ta.placeholder = T("pf_ecrire_place_q");
    const ok = document.createElement("button"); ok.className = "secondaire"; ok.type = "button"; ok.textContent = T("pf_valider");
    // a l'ecrit, la duree est estimee sur la longueur : une personne parle environ 100 mots par minute en B1
    ok.onclick = () => { if (ta.value.trim()) rendre(ta.value.trim(), mots(ta.value) * 0.6); };
    z.append(ta, ok); ta.focus();
  };
}
// UNE VALEUR DE TACHE QUI DEPEND DU SUJET CHOISI EN 2A : « X_nach_thema » (2B), le champ du sujet (2A), sinon la tache
function themeChoisi(thema){ const t2a = PF.d.sprechen.taches.find(x => x.themen); return thema && t2a ? t2a.themen.find(x => x.id === thema) : null; }
function valeur(t, nom, thema){
  const th = themeChoisi(thema);
  if (th && t[nom + "_nach_thema"]) return t[nom + "_nach_thema"][th.id];
  if (th && t.themen && th[nom]) return th[nom];
  return t[nom];
}
// ce qu'une partie de l'oral a obtenu : les criteres de la tache (mots minimum, mots reperes), et le cran
function estimer(tache, rep, thema){
  const t = (rep && rep.text) || "", n = mots(t);
  const res = (valeur(tache, "kriterien", thema) || []).map(k => {
    let ok = true;
    if (k.min_woerter) ok = ok && n >= k.min_woerter;
    if (k.mots) ok = ok && (k.mots.filter(m => new RegExp(m, "i").test(t)).length >= (k.mindestens || 1));
    return { k, ok };
  });
  const r = res.length ? res.filter(x => x.ok).length / res.length : 0;
  const idx = !n ? 5 : r >= 1 ? 0 : r >= 0.75 ? 1 : r >= 0.5 ? 2 : r >= 0.25 ? 3 : 4;
  return { res, punkte: B.CRANS[tache.sur][idx], idx };
}
function sprechen(mode, depart){
  const S = PF.d.sprechen, ex = mode === "ex";
  const etat = ex ? BL.sprechen : { thema: null, reponses: {} };
  if (ex) etat.reponses = etat.reponses || {};
  const taches = S.taches;
  let k = depart || 0;
  if (ex) garderRetourExamen(); else DTZ.surRetour(() => { accueil(); return true; });
  if (ex) chrono(MINUTES.sprechen * 60, "haut");
  const suite = () => { k++; if (k < taches.length) tache(); else fin(); };
  const tache = async () => {
    const t = taches[k];
    ecran(T("pf_epr_sprechen") + " · " + t.teil);
    if (ex) garderRetourExamen(); else DTZ.surRetour(() => { accueil(); return true; });
    // 2A : le sujet d'abord (deux au choix) ; 2B suit le sujet choisi
    if (t.themen && !etat.thema){
      $("zone").innerHTML = '<div class="bloc"><div class="section">' + esc(t.teil) + ' · ' + esc(tr(t, "nom")) + '</div>' +
        '<p class="consigne" lang="de">' + esc(t.consigne_de) + '<span class="fr">' + esc(tr(t, "consigne")) + '</span></p>' +
        t.themen.map(th => '<button class="mode" data-th="' + th.id + '"><b lang="de">' + esc(th.titre) + '</b><span lang="de">' + esc(th.stichworte.join(" · ")) + '</span></button>').join("") + '</div>';
      $("zone").querySelectorAll("[data-th]").forEach(b => b.onclick = () => { etat.thema = b.dataset.th; if (ex) sauver(); tache(); });
      return;
    }
    const th = (t.themen || t.tours_nach_thema) ? themeChoisi(etat.thema) : null;
    const redemittel = valeur(t, "redemittel", etat.thema), muster = valeur(t, "muster", etat.thema);
    const bloc = document.createElement("div"); bloc.className = "bloc";
    bloc.innerHTML = '<div class="section">' + esc(t.teil) + ' · ' + esc(tr(t, "nom")) + '</div>' +
      '<p class="consigne" lang="de">' + esc(t.consigne_de) + '<span class="fr">' + esc(tr(t, "consigne")) + '</span></p>' +
      (t.bild ? '<div class="photo-texte"><div class="k">' + esc(T("pf_bild")) + '</div><p lang="de">' + esc(t.bild.beschreibung) + '</p><p class="petit">' + esc(T("pf_bild_bientot")) + '</p></div>' : "") +
      (th ? '<div class="doc"><div class="k" lang="de">' + esc(th.titre) + '</div><p lang="de">' + esc(th.stichworte.join(" · ")) + '</p>' +
        (th.bilder || []).map(b => '<p class="petit" lang="de">▫ ' + esc(b) + '</p>').join("") + '</div>' : "") +
      (t.aussagen ? '<div class="doc liste">' + t.aussagen.map(a => '<p lang="de">„' + esc(a) + '“</p>').join("") + '</div>' : "") +
      (!ex && redemittel ? '<details><summary>' + esc(T("pf_redemittel")) + '</summary><ul class="redemittel">' + redemittel.map(r => '<li lang="de">' + esc(r) + '</li>').join("") + '</ul></details>' : "");
    $("zone").innerHTML = ""; $("zone").appendChild(bloc);
    const fil = document.createElement("div"); fil.className = "bloc"; $("zone").appendChild(fil);
    const bulle = (wer, texte) => { const d = document.createElement("div"); d.className = "dit-oral"; d.innerHTML = '<span class="mono petit-mono" aria-hidden="true">' + esc(qui(wer)[0]) + '</span><p lang="de"><b>' + esc(qui(wer)) + '</b>' + deuxPts + esc(texte) + '</p>'; fil.appendChild(d); };
    // les repliques : la Pruferin (et, a la partie 3, Elif), puis l'apprenant, autant de tours que la tache
    // chaque tour : ce que disent la Pruferin ou Elif ({wer, text}), puis la reponse ({consigne, limite})
    const tours = valeur(t, "tours", etat.thema) || [];
    const textes = [];
    let sec = 0;
    for (let j = 0; j < tours.length; j++){
      const tour = tours[j], dits = [].concat(tour.dit || []);
      for (const l of dits) bulle(l.wer, l.text);
      if (dits.length) await jouerCle(t.cle + (th && t.tours_nach_thema ? "-" + th.id : "") + "-" + j, dits);
      if (!document.body.contains(fil)) return;   // on a quitte l'ecran pendant la voix
      const rep = await new Promise(r => aToi(fil, T(tour.consigne || t.consigne_micro || "pf_a_toi"), tour.limite || t.limite, r));
      textes.push(rep.text); sec += rep.sec;
      const v = document.createElement("div"); v.className = "entendu"; v.lang = "de"; v.textContent = rep.text || "—"; fil.appendChild(v);
    }
    const rep = { text: textes.join(" "), sec };
    etat.reponses[t.cle] = rep;
    if (ex){ sauver(); bouton(T("pf_continuer"), suite); return; }
    // l'entrainement guide : l'estimation de la tache, et une reponse modele
    const e = estimer(t, rep, etat.thema);
    const retour = document.createElement("div"); retour.className = "bloc verdict";
    retour.innerHTML = '<h3>' + esc(T("pf_retour_tache")) + ' · ' + e.punkte + ' / ' + t.sur + '</h3><ul class="crit">' +
      e.res.map(x => '<li class="' + (x.ok ? "ok" : "") + '">' + esc(tr(x.k, "label")) + '</li>').join("") + '</ul>' +
      '<p class="petit">' + esc(T("pf_limite_oral")) + '</p>' +
      (muster ? '<details><summary>' + esc(T("pf_modele")) + '</summary>' + [].concat(muster).map(p => '<p lang="de">' + esc(p) + '</p>').join("") + '</details>' : "");
    $("zone").appendChild(retour);
    parler("exercice", { juste: e.idx <= 3 });
    bouton(T("pf_continuer"), suite);
  };
  const fin = () => {
    if (ex){ arreterChrono(); sauver(); suivante(); return; }
    grilleSprechen(etat, g => { resultat("tr_sprechen", { punkte: B.punkteSprechen(g) }); accueil(); }, T("pf_retour_accueil"));
  };
  tache();
}
// la grille de l'oral : les cinq taches estimees (modifiables), la langue sur les descripteurs, le total
function grilleSprechen(etat, quandFini, libelleFin){
  ecran(T("pf_grille_sprechen"));
  const S = PF.d.sprechen, g = {};
  S.taches.forEach(t => { g[t.cle] = estimer(t, (etat.reponses || {})[t.cle], etat.thema).punkte; });
  ["aussprache", "fluessigkeit", "korrektheit", "wortschatz"].forEach(c => { g[c] = null; });
  g.abgelesen = false;
  const rendre = () => {
    const pret = ["aussprache", "fluessigkeit", "korrektheit", "wortschatz"].every(c => g[c] !== null);
    const total = B.punkteSprechen(g);
    $("zone").innerHTML =
      '<div class="bloc"><h2>' + esc(T("pf_taches")) + '</h2><p class="petit">' + esc(T("pf_taches_explique")) + '</p>' +
        '<div class="detail">' + S.taches.map(t => '<span>' + esc(t.teil + " · " + tr(t, "nom")) + '</span><b>' + B.borner(t.sur, g[t.cle]) + ' / ' + t.sur + '</b>').join("") + '</div>' +
        '<label class="case"><input type="checkbox" id="pfLu"' + (g.abgelesen ? " checked" : "") + '> ' + esc(T("pf_abgelesen")) + '</label></div>' +
      [["aussprache", 15], ["fluessigkeit", 10], ["korrektheit", 10], ["wortschatz", 15]].map(([c, n]) => selecteur(c, n, g[c], "sprechen")).join("") +
      '<div class="bloc"><div class="score">' + vir(total) + ' / 100</div><p class="petit" style="text-align:center">' + esc(nomNiveau(B.niveauSprechen(total))) + '</p>' +
        '<p class="petit">' + esc(T("pf_estimation_oral")) + '</p></div>';
    brancherSelecteurs(g, () => garderScroll(rendre));
    $("pfLu").onchange = ev => { g.abgelesen = ev.target.checked; garderScroll(rendre); };
    if (pret) bouton(libelleFin || T("pf_terminer"), () => quandFini(Object.assign({}, g)));
    else $("suite").hidden = true;
  };
  rendre();
}

// ---------------------------------------------------------------- la preparation de l'oral : 20 min, les fiches 2 et 3
function vorbereitung(){
  const S = PF.d.sprechen;
  let fini = false;
  const finir = () => { if (fini) return; fini = true; arreterChrono(); BL.vorbereitung = $("pfNotes") ? $("pfNotes").value : BL.vorbereitung; sauver(); suivante(); };
  chrono(RAPIDE ? 30 : MINUTES.vorbereitung * 60, "bas", finir);
  const t2 = S.taches.find(t => t.themen), t3 = S.taches.find(t => t.aussagen);
  $("zone").innerHTML = '<div class="bloc"><p>' + esc(T("pf_vorb_texte")) + '</p></div>' +
    '<div class="bloc"><div class="section">' + esc(t2.teil) + ' · ' + esc(tr(t2, "nom")) + '</div>' +
      t2.themen.map(th => '<div class="doc"><div class="k" lang="de">' + esc(th.titre) + '</div><p lang="de">' + esc(th.stichworte.join(" · ")) + '</p></div>').join("") + '</div>' +
    '<div class="bloc"><div class="section">' + esc(t3.teil) + ' · ' + esc(tr(t3, "nom")) + '</div><p lang="de">' + esc(t3.situation_de) + '</p>' +
      '<div class="doc liste">' + t3.aussagen.map(a => '<p lang="de">„' + esc(a) + '“</p>').join("") + '</div></div>' +
    '<div class="bloc"><textarea id="pfNotes" lang="de" rows="8" placeholder="' + esc(T("pf_notes")) + '">' + esc(BL.vorbereitung || "") + '</textarea></div>';
  $("pfNotes").oninput = () => { BL.vorbereitung = $("pfNotes").value; sauver(); };
  bouton(T("pf_vorb_pret"), finir);
}

// ---------------------------------------------------------------- les grilles, puis le verdict
function grilles(){
  if (!BL.grilles.schreiben){
    const a = BL.schreiben && BL.schreiben.aufgabe ? PF.d.schreiben.aufgaben.find(x => x.id === BL.schreiben.aufgabe) : null;
    if (!a){ BL.grilles.schreiben = { inhalt: 0 }; sauver(); return grilles(); }
    return grilleSchreiben(a, BL.schreiben.text, g => { BL.grilles.schreiben = g; sauver(); grilles(); }, T("pf_grille_suivante"));
  }
  if (!BL.grilles.sprechen) return grilleSprechen(BL.sprechen, g => { BL.grilles.sprechen = g; sauver(); BL.etape++; sauver(); verdict(); }, T("pf_voir_verdict"));
  BL.etape++; sauver(); verdict();
}
function verdict(){
  arreterChrono();
  BL = BL || lire("blanc", null);
  if (!BL) return blancIntro();
  ecran(T("pf_verdict"));
  DTZ.surRetour(() => { accueil(); return true; });
  const hls = pointsDe(BL.rep), ph = pointsDe(BL.rep, "hoeren"), pl = pointsDe(BL.rep, "lesen"), ps = pointsDe(BL.rep, "sprachbausteine");
  const schr = B.punkteSchreiben(BL.grilles.schreiben || {}), spr = B.punkteSprechen(BL.grilles.sprechen || {});
  const r = B.resultat({ hls, schreiben: schr, sprechen: spr });
  const ligne = (lib, n, s, niv) => '<span>' + esc(lib) + '</span><b>' + vir(n) + ' / ' + s + (niv ? ' · ' + esc(nomNiveau(niv)) : "") + '</b>';
  const pourquoi = r.sprechen === "unter" ? "pf_pourquoi_oral" : r.zertifikat ? "pf_pourquoi_" + r.zertifikat : "pf_pourquoi_ecrit";
  $("zone").innerHTML =
    '<div class="bloc">' + jonas(T(r.zertifikat ? "pf_jonas_" + r.zertifikat : "pf_jonas_rien")) +
      '<span class="niveau ' + (r.zertifikat || "moins") + '">' + esc(r.zertifikat ? T("pf_zertifikat", { n: r.zertifikat.toUpperCase() }) : T("pf_kein_zertifikat")) + '</span>' +
      '<p>' + esc(T(pourquoi)) + '</p></div>' +
    '<div class="bloc"><h2>' + esc(T("pf_resultats")) + '</h2><div class="detail">' +
      ligne(T("pf_epr_hoeren"), ph, sur("hoeren")) + ligne(T("pf_epr_lesen"), pl, sur("lesen")) + ligne(T("pf_epr_sprachbausteine"), ps, sur("sprachbausteine")) +
      ligne(T("pf_hls"), hls, 59, r.hls) + ligne(T("pf_epr_schreiben"), schr, 20, r.schreiben) + ligne(T("pf_epr_sprechen"), spr, 100, r.sprechen) +
      '</div><p class="petit">' + esc(T("pf_regle")) + '</p><p class="petit">' + esc(T("pf_estimation")) + '</p></div>' +
    '<div class="bloc"><h2>' + esc(T("pf_corrige")) + '</h2><p class="petit">' + esc(T("pf_corrige_s")) + '</p><div class="onglets">' +
      PF.teile.map((x, j) => '<button class="onglet" data-cor="' + j + '">' + esc(x.teil.court || x.teil.titre) + ' · ' + itemsDe(x.teil).filter(i => juste(i, BL.rep[i.nr])).length + '/' + itemsDe(x.teil).length + '</button>').join("") + '</div></div>' +
    '<div class="bloc boutons"><button class="secondaire" id="pfRefaire">' + esc(T("pf_refaire")) + '</button></div>';
  $("zone").querySelectorAll("[data-cor]").forEach(b => b.onclick = () => corrige(Number(b.dataset.cor)));
  $("pfRefaire").onclick = () => confirmer(T("pf_recommencer_q"), nouveau, T("pf_recommencer"));
  bouton(T("pf_retour_accueil"), accueil);
  if (!BL.fini){
    BL.fini = true; sauver();
    const res = { hls, hoeren: ph, lesen: pl, sprachbausteine: ps, schreiben: schr, sprechen: spr, niveaux: r, zertifikat: r.zertifikat };
    ecrire("dernier", { date: new Date().toLocaleDateString(DATE_TELC), zertifikat: r.zertifikat, hls, schreiben: schr, sprechen: spr });
    resultat("blanc", res);
    parler("resultat", Object.assign({ mode: "examen_blanc_telc_pflege", modell: 1 }, res));
  }
}
function corrige(j){
  const x = PF.teile[j];
  ecran(x.teil.titre);
  DTZ.surRetour(() => { verdict(); return true; });
  $("zone").innerHTML = vueTeil(x.epr, x.teil, { mode: "co", rep: BL.rep, ecoute: x.epr === "hoeren" });
  $("zone").querySelectorAll("[data-jouer]").forEach(b => b.onclick = () => { debloquerSon(); arreterSon(); jouerCle(b.dataset.jouer, cleAudio(x.teil, b.dataset.jouer)); });
  if (j + 1 < PF.teile.length) bouton(T("pf_partie_suivante", { t: PF.teile[j + 1].teil.court || PF.teile[j + 1].teil.titre }), () => corrige(j + 1));
  else bouton(T("pf_verdict"), verdict);
}

// ================================================================= L'ACCUEIL ET LES INSCRIPTIONS
// L'accueil de commun.js est ecrit pour Mark (son image, sa bulle) : celui des Soins le remplace. Les tuiles
// gardent data-ent, que le « ‹ » de commun.js lit pour savoir qu'on est a l'accueil (et fermer alors le cadre).
const pret = e => !!(PF.d[e] && (PF.d[e].teile || PF.d[e].aufgaben || PF.d[e].taches));
function pfAccueil(){
  silence(); arreterSon(); arreterChrono(); fermerPanneau(); arreterLecture(); DTZ.retour = null;
  $("titre").textContent = T("pf_titre"); $("suite").hidden = true;
  const der = lire("dernier", null), bl = lire("blanc", null);
  $("zone").innerHTML =
    '<div class="bloc">' + jonas(T("pf_intro")) + '</div>' +
    '<div class="bloc"><h2>' + esc(T("pf_blanc")) + '</h2><p class="petit">' + esc(T("pf_blanc_s")) + '</p>' +
      '<button class="mode" id="pfBlanc"><b>' + esc(bl && !bl.fini ? T("pf_reprendre", { e: T("pf_e_" + ETAPES[bl.etape]) }) : T("pf_commencer")) + '</b><span>' + esc(T("pf_blanc_d")) + '</span></button>' +
      (der ? '<p class="dernier">' + esc(T("pf_dernier", { d: der.date, z: der.zertifikat ? T("pf_zertifikat", { n: der.zertifikat.toUpperCase() }) : T("pf_kein_zertifikat") })) + '</p>' : "") + '</div>' +
    '<div class="bloc"><h2>' + esc(T("pf_entrainement")) + '</h2><p class="petit">' + esc(T("pf_entrainement_s")) + '</p><div class="tuiles">' +
      EPR.map(e => pret(e) ? '<button class="tuile" data-ent="' + e + '">' + esc(T("pf_epr_" + e)) + '<small>' + esc(T("pf_epr_" + e + "_s")) + '</small></button>'
        : '<button class="tuile" disabled>' + esc(T("pf_epr_" + e)) + '<small>' + esc(T("bientot")) + '</small></button>').join("") + '</div></div>' +
    '<p class="petit" style="text-align:center">' + esc(T("pf_maquette")) + '</p>';
  $("pfBlanc").onclick = blancIntro;
  document.querySelectorAll("[data-ent]").forEach(b => b.onclick = () => {
    const e = b.dataset.ent;
    if (e === "schreiben") return schreiben("tr");
    if (e === "sprechen") return sprechen("tr");
    entrainement(e, 0);
  });
  window.scrollTo(0, 0);
}
function inscrire(){
  accueil = pfAccueil;   // la fonction globale de commun.js, que son « ‹ » appelle
  EPR.forEach((e, k) => DTZ.partie({ id: e, ordre: 10 * (k + 1), titre: T("pf_epr_" + e), sous: T("pf_epr_" + e + "_s"),
    ouvrir: () => e === "schreiben" ? schreiben("tr") : e === "sprechen" ? sprechen("tr") : entrainement(e, 0) }));
  DTZ.partie({ id: "BLANC", ordre: 99, titre: T("pf_blanc"), sous: T("pf_blanc_s"), ouvrir: blancIntro });
}

// pour le controle et les sondes : le calcul, et l'index des questions (rien d'ecrit)
window.PFLEGE = { PF, juste, pointsDe, estimer, infosTrouvees, itemsDe, choixDe };
})();
