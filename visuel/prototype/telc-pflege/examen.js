// LE TELC DEUTSCH B1·B2 PFLEGE AVEC ELIF -- L'EXAMEN BLANC ET L'ENTRAINEMENT (14 nov. 2026, session
// pflege-examen ; decisions de Jacques du 14 nov. : la grande version, l'examen blanc COMPLET, les 9 langues).
//
// LE FORMAT EST CELUI DU TELC (pflege/FORMAT-TELC-PFLEGE.md), LE CONTENU EST A WORTANDO : 59 questions (ecoute 23,
// lecture 18, elements de langue 18), l'ecrit A ou B sur 20, l'oral en cinq temps sur 100, puis le certificat
// (bareme.js : l'oral decide). Les donnees : donnees/<epreuve>.json (series) ; l'interface : donnees/interface.json ;
// les 9 langues dans les objets eux-memes. Contrat avec l'app : pflege/FORMAT-DONNEES.md, § 6.
//
// CE QUI EST REPRIS DU MODULE TELC A2·B1, SANS Y TOUCHER : ../dtz/commun.js (la voix, les pistes enregistrees,
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
const EPR = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"];
const AUTRES = !["fr", "en"].includes(LANGUE);
const PF = { d: {}, items: [], parNr: {}, teile: [], lecture: null, serie: 1 };
const ANTWORTZEIT = 8;          // secondes pour repondre apres chaque texte de l'ecoute, a l'examen
// les cles des pistes enregistrees : s<id de la serie>-<cle> (donnees/voix-soins.json, entrainement/voix-<epreuve>.json)
const prefixePiste = e => "s" + ((PF.d[e || "hoeren"] || {}).id || PF.serie) + "-";

// ---------------------------------------------------------------- le chargement
// donnees/<epreuve>.json : {_note, voix, series: [{id, titre, …}]} ; une serie est un examen blanc complet. Les 9 langues
// d'interface sont dans les objets (X_fr, X_en, X_tr…) et dans interface.json ({fr: {…}, en: {…}, tr: {…}…}).
// ?serie=N choisit la serie (la premiere sinon) : l'examen blanc garde la sienne dans son etat.
function json(url, facultatif){
  return fetch(url, { cache: "no-cache" })
    .then(r => { if (!r.ok) throw new Error(url); return r.json(); })
    .catch(e => { if (facultatif) return {}; throw e; });
}
// LE MANUEL (15 nov. 2026, decision de Jacques : « un manuel de preparation qui est etoffe pour l'examen du B2 ») :
// le contrat des donnees est pflege/examen/FORMAT-MANUEL.md. Les examens blancs (donnees/<epreuve>.json) sont
// RESERVES a l'examen blanc ; l'entrainement ne lit que donnees/entrainement/<epreuve>.json (series 101 et plus) ;
// le texte des chapitres vit dans donnees/manuel/ (sommaire.json, puis un fichier par chapitre, facultatif).
// les chapitres dont des exemples allemands sont enregistres (bloc « de » a « cle » : piste m-<cle>,
// manifeste donnees/manuel/voix-<chapitre>.json)
const VOIX_CHAPITRES = ["sprechen"];
const CHAPITRES = ["examen", "hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen", "kommunikation", "beruf", "grammatik"];   // le 9 (examens) n'a pas de fichier
Object.assign(PF, { examens: {}, entr: {}, voix: {}, sommaire: [], chap: {} });
// le modele d'examen blanc : ?serie=N, sinon le dernier commence, sinon le premier
PF.serie = Number(Q.get("serie")) || lire("modele", 0) || (lire("blanc", null) || {}).serie || 1;
DTZ.charger(Promise.all([
  json("donnees/interface.json"),
  // une epreuve pas encore ecrite laisse sa tuile grisee (« bientot ») : son fichier est facultatif
  ...EPR.map(e => json("donnees/" + e + ".json", true)),
  json("donnees/voix-soins.json", true),
  ...EPR.map(e => json("donnees/entrainement/" + e + ".json", true)),
  ...["hoeren", "sprechen"].map(e => json("donnees/entrainement/voix-" + e + ".json", true)),
  json("donnees/manuel/sommaire.json", true),
  ...CHAPITRES.map(c => json("donnees/manuel/" + c + ".json", true)),
  Q.get("exemple") ? json("donnees/manuel/_exemple.json", true) : Promise.resolve(null),
  // les Redemittel : UNE source, celle de la section Soins (pflege/datos/redemittel.json, FORMAT-DONNEES.md § 2 bis)
  json("../../../pflege/datos/redemittel.json", true),
  json("../../../pflege/datos/sons.json", true),
  ...VOIX_CHAPITRES.map(c => json("donnees/manuel/voix-" + c + ".json", true)),
  // les sujets d'ecrit de la section Soins (?sujet=, et les renvois « ecrit: » du manuel)
  json("../../../pflege/datos/ecrit.json", true)
]).then(([ui, ...reste]) => {
  textesTelc({ fr: ui.fr, en: ui.en });
  if (AUTRES) Object.assign(TXT, ui[LANGUE] || {});
  const n = EPR.length, pistes = [reste[n], reste[2 * n + 1], reste[2 * n + 2]];
  EPR.forEach((e, k) => {
    const d = reste[k] || {}, t = reste[n + 1 + k] || {};
    PF.examens[e] = d.series || [];
    PF.entr[e] = t.series || [];
    PF.voix[e] = Object.assign({}, d.voix || {}, t.voix || {});
  });
  for (const m of pistes) for (const k in (m || {})) if (k[0] !== "_") DTZ_PISTES[k] = m[k];
  for (const e of EPR) for (const w in PF.voix[e]) DTZ_VOIX[w] = { sexe: PF.voix[e][w].sexe };
  PF.sommaire = (reste[2 * n + 3] || {}).chapitres || [];
  CHAPITRES.forEach((c, k) => { const f = reste[2 * n + 4 + k]; if (f && f.rubriques && f.rubriques.length) PF.chap[c] = f; });
  const ex = reste[2 * n + 4 + CHAPITRES.length];
  PF.rm = reste[2 * n + 5 + CHAPITRES.length] || {};
  PF.sons = reste[2 * n + 6 + CHAPITRES.length] || {};
  VOIX_CHAPITRES.forEach((c, k) => { const m = reste[2 * n + 7 + CHAPITRES.length + k] || {}; for (const x in m) if (x[0] !== "_") DTZ_PISTES[x] = m[x]; });
  PF.ecrit = reste[2 * n + 7 + CHAPITRES.length + VOIX_CHAPITRES.length] || {};
  if (ex && ex.rubriques){
    PF.chap._exemple = ex;
    PF.sommaire = [{ id: "_exemple", nr: "·", titre_fr: "Exemple : chaque sorte de bloc", titre_en: "Example: every kind of block", resume_fr: "Pour voir le rendu du format (?exemple=1).", resume_en: "To see how the format renders (?exemple=1)." }].concat(PF.sommaire);
  }
  // l'ancien etat de l'examen blanc (avant le manuel, une seule cle « blanc ») devient celui de son modele
  const ancien = lire("blanc", null);
  if (ancien && !lire("blanc_" + (ancien.serie || 1), null)) ecrire("blanc_" + (ancien.serie || 1), ancien);
  if (!modeles().includes(PF.serie)) PF.serie = modeles()[0] || 1;
  utiliserExamen(PF.serie);
  inscrire();
}));
// les modeles d'examen blanc : les id presents dans les cinq epreuves
function modeles(){
  const ids = (PF.examens.hoeren || []).map(s => s.id);
  return ids.filter(id => EPR.every(e => !PF.examens[e].length || PF.examens[e].some(s => s.id === id)));
}
// la serie en cours d'une epreuve : PF.d[e] (l'examen blanc et l'entrainement passent tous deux par la)
function utiliser(e, s){ PF.d[e] = Object.assign({ voix: PF.voix[e] || {} }, s || {}); indexer(); }
function utiliserExamen(id){
  PF.serie = id;
  EPR.forEach(e => utiliser(e, PF.examens[e].find(x => x.id === id) || PF.examens[e][0]));
}

// une aide dans la langue d'interface (X_<langue>), sinon le francais
function tr(o, champ){
  if (!o) return "";
  return o[champ + "_" + LANGUE] || o[champ + "_fr"] || "";
}
const ABCX = "abcdefghij";
const lettre = v => v === "x" ? "x" : ABCX[v];
const groupesDe = teil => teil.gespraeche || teil.texte || null;
const itemsDe = teil => teil.items || [].concat(...(groupesDe(teil) || []).map(g => g.items));

function indexer(){
  PF.items = []; PF.teile = [];
  ["hoeren", "lesen", "sprachbausteine"].forEach(e => ((PF.d[e] || {}).teile || []).forEach(t => {
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
const vir = n => { const x = String(Math.round(n * 10) / 10); return ["fr", "tr", "uk", "ru", "pl", "pt", "es"].includes(LANGUE) ? x.replace(".", ",") : x; };
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
const jouerCle = (cle, audio, e) => jouerPiste(prefixePiste(e) + cle, audio);

// ================================================================= L'ENTRAINEMENT PAR EPREUVE
// Une epreuve a la fois, partie par partie, sans chronometre ; « Corriger » montre les reponses, l'explication et,
// pour l'ecoute, la transcription. Rien ne compte pour l'examen blanc.
// La serie vient de donnees/entrainement/<epreuve>.json (jamais d'un examen blanc) ; le retour mene au chapitre.
function entrainement(epr, id, k){
  const s = PF.entr[epr].find(x => x.id === id);
  if (!s) return chapitre(epr);
  utiliser(epr, s);
  const teile = PF.d[epr].teile;
  k = k || 0;
  const teil = teile[k], rep = {}; let mode = "tr";
  ecran(T("pf_epr_" + epr) + " · " + nomSerie(epr, s));
  DTZ.surRetour(() => { chapitre(epr); return true; });
  const rendre = () => {
    $("zone").innerHTML = ongletsTeile(epr, k) + (k === 0 && mode === "tr" ? '<div class="bloc">' + jonas(T("pf_jonas_" + epr)) + '</div>' : "") +
      vueTeil(epr, teil, { mode, rep, ecoute: epr === "hoeren" });
    brancherChoix(rep, mode, rendre);
    $("zone").querySelectorAll("[data-jouer]").forEach(b => b.onclick = () => { debloquerSon(); arreterSon(); jouerCle(b.dataset.jouer, cleAudio(teil, b.dataset.jouer)); });
    $("zone").querySelectorAll("[data-teil]").forEach(b => b.onclick = () => entrainement(epr, id, Number(b.dataset.teil)));
    if (mode === "tr") bouton(T("pf_corriger"), () => {
      mode = "co";
      itemsDe(teil).forEach(it => { if (rep[it.nr] !== null && rep[it.nr] !== undefined) parler("exercice", { juste: juste(it, rep[it.nr]) }); });
      const n = itemsDe(teil).filter(it => juste(it, rep[it.nr])).length;
      resultat("tr_" + epr + "_" + id + "_" + teil.cle, { bons: n, sur: itemsDe(teil).length });
      noterSerie(epr, id, teil.cle, n, itemsDe(teil).length);
      rendre(); window.scrollTo(0, 0);
    });
    else {
      const n = itemsDe(teil).filter(it => juste(it, rep[it.nr])).length;
      const tete = $("zone").querySelector(".bloc .section");
      if (tete) tete.insertAdjacentHTML("afterend", '<div class="score">' + n + ' / ' + itemsDe(teil).length + '</div>');
      if (k + 1 < teile.length) bouton(T("pf_partie_suivante", { t: teile[k + 1].titre }), () => entrainement(epr, id, k + 1));
      else bouton(T("pf_retour_chapitre"), () => chapitre(epr));
    }
  };
  rendre();
}
function ongletsTeile(epr, k){
  const teile = PF.d[epr].teile;
  return '<div class="bloc"><div class="onglets">' + teile.map((t, j) => '<button class="onglet' + (j === k ? " actif" : "") + '" data-teil="' + j + '">' + esc(T("pf_teil", { n: t.teil })) + '</button>').join("") + '</div></div>';
}

// ================================================================= L'EXAMEN BLANC
// L'etat (stockage local wortando_soins_telc_blanc) : {debut, etape, rep, schreiben, sprechen, vorbereitung,
// grilles, fini}. On peut quitter et reprendre : l'etape en cours recommence, les reponses deja donnees restent.
const ETAPES = ["hoeren", "lesen", "schreiben", "vorbereitung", "sprechen", "grilles"];
const MINUTES = { hoeren: 25, lesen: 60, schreiben: 30, vorbereitung: 20, sprechen: 16 };
let BL = null;
const sauver = () => ecrire("blanc_" + BL.serie, BL);
function garderRetourExamen(){
  DTZ.surRetour(() => { confirmer(T("pf_quitter_q"), () => { arreterLecture(); arreterChrono(); chapitre("examens"); }, T("pf_quitter")); return true; });
}
// un modele (une serie des examens blancs) : son etat a lui, wortando_soins_telc_blanc_<id>
function blancIntro(id){
  if (id) PF.serie = id;
  ecrire("modele", PF.serie);
  utiliserExamen(PF.serie);
  ecran(T("pf_blanc") + " · " + T("pf_modele_n", { n: rangModele(PF.serie) }));
  BL = lire("blanc_" + PF.serie, null);
  DTZ.surRetour(() => { chapitre("examens"); return true; });
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
  BL = { debut: Date.now(), serie: PF.serie, etape: 0, rep: {}, schreiben: null, sprechen: {}, vorbereitung: "", grilles: {}, fini: false };
  sauver(); etape();
}
function suivante(){ arreterChrono(); BL.etape++; sauver(); etape(); }
function etape(){
  arreterChrono();
  utiliserExamen(BL.serie);   // toujours : un entrainement a pu mettre sa serie a la place (PF.d)
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
  if (ex) garderRetourExamen(); else DTZ.surRetour(() => { chapitre("schreiben"); return true; });
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
      resultat("tr_schreiben_" + S.id + "_" + a.id, { aufgabe: a.id, punkte: p });
      noterSerie("schreiben", S.id, a.id, p, 20);
      parler("exercice", { juste: p >= 7 });
      chapitre("schreiben");
    }, T("pf_retour_chapitre"));
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
// UNE PHOTO DE L'ORAL : {src, beschreibung} ; tant que l'image n'existe pas (src absent), sa description en allemand.
// La description sert aussi de texte de remplacement pour les lecteurs d'ecran.
function photo(b, grande){
  if (typeof b === "string") b = { beschreibung: b };
  if (b.src) return '<figure class="photo-oral' + (grande ? " grande" : "") + '"><img src="' + esc(b.src) + '" alt="' + esc(b.beschreibung) + '" lang="de" loading="lazy"></figure>';
  return '<div class="photo-texte"><div class="k">' + esc(T("pf_bild")) + '</div><p lang="de">' + esc(b.beschreibung) + '</p>' +
    (grande ? '<p class="petit">' + esc(T("pf_bild_bientot")) + '</p>' : "") + '</div>';
}
function sprechen(mode, depart){
  const S = PF.d.sprechen, ex = mode === "ex";
  const etat = ex ? BL.sprechen : { thema: null, reponses: {} };
  if (ex) etat.reponses = etat.reponses || {};
  const taches = S.taches;
  let k = depart || 0;
  if (ex) garderRetourExamen(); else DTZ.surRetour(() => { chapitre("sprechen"); return true; });
  if (ex) chrono(MINUTES.sprechen * 60, "haut");
  const suite = () => { k++; if (k < taches.length) tache(); else fin(); };
  const tache = async () => {
    const t = taches[k];
    ecran(T("pf_epr_sprechen") + " · " + t.teil);
    if (ex) garderRetourExamen(); else DTZ.surRetour(() => { chapitre("sprechen"); return true; });
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
      (t.bild ? photo(t.bild, true) : "") +
      (th ? '<div class="doc"><div class="k" lang="de">' + esc(th.titre) + '</div><p lang="de">' + esc(th.stichworte.join(" · ")) + '</p>' +
        ((th.bilder || []).length ? '<div class="photos">' + th.bilder.map(b => photo(b, false)).join("") + '</div>' : "") + '</div>' : "") +
      (t.situation_de ? '<p lang="de"><b>' + esc(t.situation_de) + '</b></p>' : "") +
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
      if (dits.length) await jouerCle(t.cle + (th && t.tours_nach_thema ? "-" + th.id : "") + "-" + j, dits, "sprechen");
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
    grilleSprechen(etat, g => {
      const p = B.punkteSprechen(g);
      resultat("tr_sprechen_" + S.id, { punkte: p });
      noterSerie("sprechen", S.id, taches.map(t => t.cle).join("+"), p, 100);
      chapitre("sprechen");
    }, T("pf_retour_chapitre"));
  };
  tache();
}
// la grille de l'oral : les cinq taches estimees (modifiables), la langue sur les descripteurs, le total
function grilleSprechen(etat, quandFini, libelleFin){
  ecran(T("pf_grille_sprechen"));
  const S = PF.d.sprechen, g = {};
  // la cle de la tache (sp1a) devient celle du bareme (t1a)
  const cleB = t => t.cle.replace(/^sp/, "t");
  S.taches.forEach(t => { g[cleB(t)] = estimer(t, (etat.reponses || {})[t.cle], etat.thema).punkte; });
  ["aussprache", "fluessigkeit", "korrektheit", "wortschatz"].forEach(c => { g[c] = null; });
  g.abgelesen = false;
  const rendre = () => {
    const pret = ["aussprache", "fluessigkeit", "korrektheit", "wortschatz"].every(c => g[c] !== null);
    const total = B.punkteSprechen(g);
    $("zone").innerHTML =
      '<div class="bloc"><h2>' + esc(T("pf_taches")) + '</h2><p class="petit">' + esc(T("pf_taches_explique")) + '</p>' +
        '<div class="detail">' + S.taches.map(t => '<span>' + esc(t.teil + " · " + tr(t, "nom")) + '</span><b>' + B.borner(t.sur, g[cleB(t)]) + ' / ' + t.sur + '</b>').join("") + '</div>' +
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
  BL = BL || lire("blanc_" + PF.serie, null);
  if (!BL) return blancIntro();
  utiliserExamen(BL.serie);
  ecran(T("pf_verdict"));
  DTZ.surRetour(() => { chapitre("examens"); return true; });
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
  bouton(T("pf_retour_examens"), () => chapitre("examens"));
  if (!BL.fini){
    BL.fini = true; sauver();
    const res = { hls, hoeren: ph, lesen: pl, sprachbausteine: ps, schreiben: schr, sprechen: spr, niveaux: r, zertifikat: r.zertifikat };
    const der = { date: new Date().toLocaleDateString(DATE_TELC), serie: BL.serie, zertifikat: r.zertifikat, hls, schreiben: schr, sprechen: spr };
    ecrire("dernier", der); ecrire("dernier_" + BL.serie, der);
    resultat("blanc_" + BL.serie, res);
    // LE MESSAGE A L'APP (contrat pflege/FORMAT-DONNEES.md, § 6) : c'est ce que lit le tableau de bord ; l'app
    // recalcule le certificat elle-meme (certificatSoins, memes seuils que bareme.js)
    parler("resultat_examen", { examen: "soins_telc", serie: BL.serie, date: new Date().toISOString(),
      points: { hls, schreiben: schr, sprechen: spr },
      certificat: r.zertifikat ? r.zertifikat.toUpperCase() : "aucun", detail: res });
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

// ================================================================= LE MANUEL : SOMMAIRE, CHAPITRES, BLOCS
// L'accueil de commun.js est ecrit pour Mark (son image, sa bulle) : celui des Soins le remplace par le SOMMAIRE du
// manuel (pflege/examen/FORMAT-MANUEL.md). Les lignes gardent data-ent, que le « ‹ » de commun.js lit pour savoir
// qu'on est a l'accueil (et fermer alors le cadre).

// ---------------------------------------------------------------- la progression (stockage local « manuel »)
const etatManuel = () => Object.assign({ vu: {}, series: {}, ex: {} }, lire("manuel", {}));
function noterManuel(f){ const m = etatManuel(); f(m); ecrire("manuel", m); }
function noterSerie(epr, id, cle, bons, surN){ noterManuel(m => { const k = epr + ":" + id; m.series[k] = m.series[k] || {}; m.series[k][cle] = { bons, sur: surN }; }); }
// les « parties » d'une serie d'entrainement : ses parties (ecoute, lecture, elements de langue), ses taches d'ecrit,
// ou une seule pour l'oral (on joue toutes ses taches a la suite)
function partiesDe(epr, s){
  if (epr === "schreiben") return (s.aufgaben || []).map(a => a.id);
  if (epr === "sprechen") return [(s.taches || []).map(t => t.cle).join("+")];
  return (s.teile || []).map(t => t.cle);
}
function progresSerie(epr, s){
  const fait = etatManuel().series[epr + ":" + s.id] || {}, p = partiesDe(epr, s);
  const faites = p.filter(c => fait[c]);
  return { faites: faites.length, total: p.length, bons: faites.reduce((x, c) => x + fait[c].bons, 0), sur: faites.reduce((x, c) => x + fait[c].sur, 0) };
}
function nomSerie(epr, s){
  if (tr(s, "titre")) return tr(s, "titre");
  const n = PF.entr[epr].indexOf(s) + 1, teile = s.teile || [];
  return T("pf_serie_n", { n }) + (teile.length === 1 && (PF.examens[epr][0] || {}).teile && PF.examens[epr][0].teile.length > 1 ? " · " + T("pf_teil", { n: teile[0].teil }) : "");
}
const rangModele = id => Math.max(1, modeles().indexOf(id) + 1);
// tous les exercices d'un chapitre (blocs « exercice »)
const exercicesDe = c => ((PF.chap[c] || {}).rubriques || []).flatMap(r => (r.blocs || []).filter(b => b.t === "exercice"));
function progresChapitre(c){
  const ch = PF.sommaire.find(x => x.id === c) || {}, m = etatManuel();
  if (c === "examens"){
    const faits = modeles().filter(id => (lire("blanc_" + id, null) || {}).fini).length;
    return modeles().length ? T("pf_prog_modeles", { f: faits, t: modeles().length }) : "";
  }
  if (ch.epreuve && PF.entr[ch.epreuve] && PF.entr[ch.epreuve].length){
    let f = 0, t = 0;
    PF.entr[ch.epreuve].forEach(s => { const p = progresSerie(ch.epreuve, s); f += p.faites; t += p.total; });
    return T("pf_prog_parties", { f, t });
  }
  const ex = exercicesDe(c);
  if (ex.length) return T("pf_prog_exercices", { f: ex.filter(b => m.ex[b.cle]).length, t: ex.length });
  if (!PF.chap[c]) return T("pf_a_venir_court");
  return m.vu[c] ? T("pf_lu") : "";
}

// ---------------------------------------------------------------- le sommaire (l'accueil)
const pret = e => !!(PF.d[e] && (PF.d[e].teile || PF.d[e].aufgaben || PF.d[e].taches));
function pfAccueil(){
  silence(); arreterSon(); arreterChrono(); fermerPanneau(); arreterLecture(); DTZ.retour = null;
  $("titre").textContent = T("pf_titre"); $("suite").hidden = true;
  const ligne = c => '<button class="mode chap" data-ent="' + esc(c.id) + '"><b><span class="chap-nr">' + esc(String(c.nr)) + '</span> ' + esc(tr(c, "titre")) + '</b>' +
    '<span>' + esc(tr(c, "resume")) + '</span>' + (progresChapitre(c.id) ? '<span class="chap-prog">' + esc(progresChapitre(c.id)) + '</span>' : "") + '</button>';
  $("zone").innerHTML =
    '<div class="bloc">' + jonas(T("pf_intro_manuel")) + '</div>' +
    '<div class="bloc"><h2>' + esc(T("pf_manuel")) + '</h2><p class="petit">' + esc(T("pf_manuel_s")) + '</p>' +
      (PF.sommaire.length ? PF.sommaire.map(ligne).join("") : '<p>' + esc(T("pf_a_venir")) + '</p>') + '</div>' +
    '<p class="petit" style="text-align:center">' + esc(T("pf_maquette")) + '</p>';
  document.querySelectorAll("[data-ent]").forEach(b => b.onclick = () => chapitre(b.dataset.ent));
  window.scrollTo(0, 0);
}

// ---------------------------------------------------------------- un chapitre
const TITRES_RUBRIQUES = { attendu: "pf_rub_attendu", pieges: "pf_rub_pieges", strategies: "pf_rub_strategies", guide: "pf_rub_guide" };
function chapitre(c, rubrique){
  if (c === "examens") return examens();
  const ch = PF.sommaire.find(x => x.id === c);
  if (!ch) return accueil();
  ecran(tr(ch, "titre"));
  DTZ.surRetour(() => { accueil(); return true; });
  noterManuel(m => { m.vu[c] = true; });
  const f = PF.chap[c], rubriques = (f && f.rubriques) || [];
  let h = '<div class="bloc"><div class="section">' + esc(T("pf_chap_n", { n: ch.nr })) + '</div><h2>' + esc(tr(ch, "titre")) + '</h2><p>' + esc(tr(ch, "resume")) + '</p>' +
    (rubriques.length > 1 || ch.epreuve ? '<div class="onglets">' + rubriques.map(r => '<button class="onglet" data-rub="' + esc(r.id) + '">' + esc(titreRubrique(r)) + '</button>').join("") +
      (ch.epreuve ? '<button class="onglet" data-rub="_entr">' + esc(T("pf_rub_entrainement")) + '</button>' : "") + '</div>' : "") + '</div>';
  if (!rubriques.length) h += '<div class="bloc"><p>' + esc(T("pf_a_venir")) + '</p></div>';
  rubriques.forEach(r => { h += '<div class="bloc rubrique" id="rub-' + esc(r.id) + '"><h2>' + esc(titreRubrique(r)) + '</h2>' + (r.blocs || []).map(blocHtml).join("") + '</div>'; });
  if (ch.epreuve) h += '<div class="bloc rubrique" id="rub-_entr"><h2>' + esc(T("pf_rub_entrainement")) + '</h2>' + seriesHtml(ch.epreuve) + '</div>';
  $("zone").innerHTML = h;
  brancherBlocs(c);
  $("zone").querySelectorAll("[data-rub]").forEach(b => b.onclick = () => { const x = $("rub-" + b.dataset.rub); if (x) x.scrollIntoView({ behavior: "auto", block: "start" }); });
  const vise = rubrique && $("rub-" + rubrique);
  if (vise) vise.scrollIntoView({ block: "start" }); else window.scrollTo(0, 0);
}
const titreRubrique = r => TITRES_RUBRIQUES[r.id] ? T(TITRES_RUBRIQUES[r.id]) : tr(r, "titre");

// les series d'entrainement d'une epreuve, avec leur progression
function seriesHtml(epr){
  const liste = PF.entr[epr] || [];
  if (!liste.length) return '<p>' + esc(T("pf_series_a_venir")) + '</p>';
  return liste.map(s => {
    const p = progresSerie(epr, s);
    const etat = p.faites ? T("pf_serie_prog", { f: p.faites, t: p.total }) + (epr === "schreiben" || epr === "sprechen" ? "" : " · " + T("pf_serie_justes", { b: p.bons, s: p.sur })) : T("pf_serie_neuve");
    if (epr === "schreiben") return (s.aufgaben || []).map(a => {
      const fait = (etatManuel().series["schreiben:" + s.id] || {})[a.id];
      return '<button class="mode" data-serie="' + s.id + '" data-auf="' + esc(a.id) + '"><b lang="de">' + esc(T("pf_aufgabe", { a: a.art || a.id })) + ' · ' + esc(a.titre) + '</b><span>' + esc(tr(a, "resume")) + '</span>' +
        '<span class="chap-prog">' + esc(fait ? fait.bons + " / 20" : T("pf_serie_neuve")) + '</span></button>';
    }).join("");
    return '<button class="mode" data-serie="' + s.id + '"><b>' + esc(nomSerie(epr, s)) + '</b><span class="chap-prog">' + esc(etat) + '</span></button>';
  }).join("");
}
function ouvrirSerie(epr, id, teil, aufgabe){
  const s = PF.entr[epr].find(x => x.id === id);
  if (!s) return;
  if (epr === "schreiben"){ utiliser("schreiben", s); return schreiben("tr", aufgabe || null); }
  if (epr === "sprechen"){ utiliser("sprechen", s); return sprechen("tr"); }
  const k = teil ? Math.max(0, (s.teile || []).findIndex(t => t.teil === teil)) : 0;
  entrainement(epr, id, k);
}

// ---------------------------------------------------------------- les blocs d'un chapitre
// l'adresse des sons de la section Soins (pflege/datos/sons.json : cle -> fichier) : VIDE tant que l'architecture ne
// l'a pas fixee (les fichiers sont faits, pas deposes) ; vide, la voix du telephone lit la carte
const BASE_SONS_SOINS = "https://deutschai-b6fbb.web.app/pflege/";   // l architecture, 15 nov. : BASE + valeur de sons.json
const ORDRE_NIVEAUX = ["A2", "B1", "B2", "C1"];
function cartesRm(groupe){
  const fonctions = (PF.rm.fonctions || []).map(f => f.id);
  return (PF.rm.cartes || []).filter(c => c.groupe === groupe && !c.retire)
    .sort((a, b) => (fonctions.indexOf(a.fonction) - fonctions.indexOf(b.fonction)) || (ORDRE_NIVEAUX.indexOf(a.niveau) - ORDRE_NIVEAUX.indexOf(b.niveau)));
}
// [[…]] dans un texte d'aide : de l'allemand, montre comme tel (lang="de", de gauche a droite)
const aide = (o, champ) => esc(tr(o, champ || "texte")).replace(/\[\[([^\]]+)\]\]/g, (m, d) => '<span lang="de" dir="ltr" class="de">' + d + '</span>');
const deHtml = t => esc(t || "").split("\n").join("<br>");
const cellule = c => c && c.de !== undefined ? '<span lang="de" dir="ltr">' + deHtml(c.de) + '</span>' : aide(c);
function blocHtml(b){
  switch (b.t){
    case "p": return '<p>' + aide(b) + '</p>';
    case "titre": return '<h3>' + aide(b) + '</h3>';
    case "liste": { const tag = b.ordre ? "ol" : "ul"; return '<' + tag + ' class="liste-manuel">' + (b.items || []).map(i => '<li>' + aide(i) + '</li>').join("") + '</' + tag + '>'; }
    case "de": return '<div class="exemple-de">' + (b.cle ? '<button class="jouer" data-de-son="' + esc(b.cle) + '">' + ICONE_SON + ' ' + esc(T("pf_ecouter")) + '</button>' : "") +
      '<p lang="de" dir="ltr">' + deHtml(b.de) + '</p>' +
      (tr(b, "texte") ? '<details><summary>' + esc(T("pf_traduction")) + '</summary><p>' + aide(b) + '</p></details>' : "") + '</div>';
    case "piege": return '<div class="piege"><div class="piege-t">⚠ ' + esc(T("pf_piege")) + (tr(b, "titre") ? deuxPts + aide(b, "titre") : "") + '</div>' +
      (b.de ? '<p lang="de" dir="ltr" class="piege-de">' + deHtml(b.de) + '</p>' : "") + '<p>' + aide(b) + '</p></div>';
    case "tableau": return '<div class="tableau-manuel"><table>' + (b.entetes ? '<thead><tr>' + b.entetes.map(c => '<th>' + cellule(c) + '</th>').join("") + '</tr></thead>' : "") +
      '<tbody>' + (b.lignes || []).map(l => '<tr>' + l.map(c => '<td>' + cellule(c) + '</td>').join("") + '</tr>').join("") + '</tbody></table></div>';
    case "doc": return docHtml(b.doc, { items: [] }, {}, "tr");
    case "redemittel": {
      // les cartes d'un groupe, rangees par fonction puis par niveau ; leur texte et leur son viennent de la source
      const cartes = cartesRm(b.ref);
      if (!cartes.length) return '<div class="rm">' + (tr(b, "titre") ? '<div class="rm-t">' + aide(b, "titre") + '</div>' : "") + '<p class="petit">' + esc(T("pf_rm_a_venir")) + '</p></div>';
      const fonctions = (PF.rm.fonctions || []).map(f => f.id);
      let h = '<div class="rm">' + (tr(b, "titre") ? '<div class="rm-t">' + aide(b, "titre") + '</div>' : ""), avant = null;
      cartes.forEach(c => {
        if (c.fonction !== avant){
          avant = c.fonction;
          const f = (PF.rm.fonctions || [])[fonctions.indexOf(c.fonction)];
          h += '<h3>' + esc(f ? ((f.titre || {})[LANGUE] || (f.titre || {}).fr || c.fonction) : c.fonction) + '</h3>';
        }
        h += '<div class="rm-l"><button class="jouer petit-jouer" data-rm="' + esc(c.id) + '" aria-label="' + esc(T("pf_ecouter")) + '">' + ICONE_SON + '</button>' +
          '<div><span lang="de" dir="ltr" class="rm-de">' + esc(c.de) + '</span>' + (c.registre ? ' <span class="rm-reg" lang="de">' + esc(c.registre) + '</span>' : "") +
          ' <span class="rm-reg">' + esc(c.niveau || "") + '</span>' +
          '<span class="rm-tr">' + esc((c.trad || {})[LANGUE] || (c.trad || {}).fr || "") + '</span></div></div>';
      });
      return h + '</div>';
    }
    case "exercice": return '<div class="exercice-manuel" data-ex="' + esc(b.cle) + '"></div>';
    case "serie": {
      const s = (PF.entr[b.epreuve] || []).find(x => x.id === b.serie);
      return '<button class="mode" data-serie-bloc="' + esc(b.epreuve) + ':' + b.serie + ':' + (b.teil || "") + '"' + (s ? "" : " disabled") + '><b>' + esc(T("pf_epr_" + b.epreuve)) + ' · ' +
        esc(s ? nomSerie(b.epreuve, s) : T("bientot")) + (b.teil ? ' · ' + esc(T("pf_teil", { n: b.teil })) : "") + '</b>' + (tr(b, "texte") ? '<span>' + aide(b) + '</span>' : "") + '</button>';
    }
    case "renvoi": return '<button class="mode renvoi" data-vers="' + esc(b.vers) + '"' + (/^chapitre:/.test(b.vers) || DANS_APP ? "" : " disabled") + '><b>' +
      esc(/^chapitre:/.test(b.vers) ? T("pf_voir_chapitre") : T("pf_dans_app")) + '</b><span>' + aide(b, "titre") + '</span></button>';
    default: return "";
  }
}
// les exercices sur place : on repond, « Corriger », l'explication et le pas a pas (pas_*)
function exerciceManuel(el, b){
  const rep = {}; let mode = "tr";
  const teil = { items: b.items };
  const rendre = () => {
    el.innerHTML = (tr(b, "consigne") || b.consigne_de ? '<p class="consigne">' + (b.consigne_de ? '<span lang="de">' + esc(b.consigne_de) + '</span>' : "") + '<span class="fr">' + aide(b, "consigne") + '</span></p>' : "") +
      (b.doc ? docHtml(b.doc, teil, rep, mode) : "") +
      b.items.map(it => carteQuestion(teil, it, rep, mode) + (mode === "co" && tr(it, "pas") ? pasHtml(it) : "")).join("") +
      '<div class="boutons">' + (mode === "tr" ? '<button class="secondaire" data-corriger>' + esc(T("pf_corriger")) + '</button>'
        : '<div class="score">' + b.items.filter(it => juste(it, rep[it.nr])).length + ' / ' + b.items.length + '</div><button class="lien" data-refaire>' + esc(T("pf_refaire_ex")) + '</button>') + '</div>';
    el.querySelectorAll("[data-nr][data-v]").forEach(x => x.onclick = () => {
      if (mode === "co") return;
      const nr = Number(x.dataset.nr), v = Number(x.dataset.v);
      rep[nr] = rep[nr] === v ? null : v;
      garderScroll(rendre);
    });
    const c = el.querySelector("[data-corriger]");
    if (c) c.onclick = () => {
      mode = "co";
      const n = b.items.filter(it => juste(it, rep[it.nr])).length;
      b.items.forEach(it => { if (rep[it.nr] !== null && rep[it.nr] !== undefined) parler("exercice", { juste: juste(it, rep[it.nr]) }); });
      noterManuel(m => { m.ex[b.cle] = { bons: n, sur: b.items.length }; });
      garderScroll(rendre);
    };
    const r = el.querySelector("[data-refaire]");
    if (r) r.onclick = () => { for (const k in rep) delete rep[k]; mode = "tr"; garderScroll(rendre); };
  };
  rendre();
}
// tr() renvoie le champ de la langue ; pas_* est une liste : on la lit a part
function pasHtml(it){
  const p = it["pas_" + LANGUE] || it.pas_fr || [];
  return '<ol class="pas">' + p.map(x => '<li>' + esc(x).replace(/\[\[([^\]]+)\]\]/g, (m, d) => '<span lang="de" dir="ltr" class="de">' + d + '</span>') + '</li>').join("") + '</ol>';
}
function brancherBlocs(c){
  const rub = (PF.chap[c] || {}).rubriques || [];
  const tous = rub.flatMap(r => r.blocs || []);
  $("zone").querySelectorAll("[data-ex]").forEach(el => { const b = tous.find(x => x.t === "exercice" && x.cle === el.dataset.ex); if (b) exerciceManuel(el, b); });
  $("zone").querySelectorAll("[data-rm]").forEach(x => x.onclick = async () => {
    const c = (PF.rm.cartes || []).find(y => y.id === x.dataset.rm);
    if (!c) return;
    debloquerSon(); arreterSon();
    // le son de la carte (sons.json de la section Soins), sinon la voix du telephone sur la lecture (nombres en lettres)
    const f = BASE_SONS_SOINS && PF.sons[c.son];
    if (f && !RAPIDE && await jouerFichier(BASE_SONS_SOINS + f)) return;
    jouerRepliques([{ wer: "neutral", text: c.lecture || c.de }]);
  });
  // un exemple allemand enregistre : sa piste m-<cle>, sinon ses repliques (« audio ») a la voix du telephone
  $("zone").querySelectorAll("[data-de-son]").forEach(x => x.onclick = () => {
    const b = tous.find(y => y.t === "de" && y.cle === x.dataset.deSon);
    if (b){ debloquerSon(); arreterSon(); jouerPiste("m-" + b.cle, b.audio || [{ wer: "neutral", text: b.de }]); }
  });
  $("zone").querySelectorAll("[data-serie]").forEach(x => x.onclick = () => {
    const ch = PF.sommaire.find(y => y.id === c);
    ouvrirSerie(ch.epreuve, Number(x.dataset.serie), null, x.dataset.auf);
  });
  $("zone").querySelectorAll("[data-serie-bloc]").forEach(x => x.onclick = () => {
    const [e, id, teil] = x.dataset.serieBloc.split(":");
    ouvrirSerie(e, Number(id), Number(teil) || null);
  });
  $("zone").querySelectorAll("[data-vers]").forEach(x => x.onclick = () => {
    const v = x.dataset.vers;
    if (/^chapitre:/.test(v)) return chapitre(v.slice(9));
    if (/^ecrit:/.test(v) && sujetsEcrits().some(y => y.id === v.slice(6)))
      return ouvrirEcrit(v.slice(6), { retour: () => chapitre(c), libelleFin: T("pf_retour_chapitre") });
    parler("ouvrir", { vers: v });
  });
}

// ---------------------------------------------------------------- le chapitre 9 : les examens blancs, un par modele
function examens(){
  const ch = PF.sommaire.find(x => x.id === "examens") || {};
  ecran(tr(ch, "titre") || T("pf_examens"));
  DTZ.surRetour(() => { accueil(); return true; });
  noterManuel(m => { m.vu.examens = true; });
  $("zone").innerHTML = '<div class="bloc">' + jonas(T("pf_blanc_intro")) + '</div>' +
    '<div class="bloc"><h2>' + esc(T("pf_examens")) + '</h2><p class="petit">' + esc(T("pf_examens_s")) + '</p>' +
    modeles().map(id => {
      const bl = lire("blanc_" + id, null), der = lire("dernier_" + id, null);
      const etat = bl && !bl.fini ? T("pf_reprendre", { e: T("pf_e_" + ETAPES[bl.etape]) }) :
        der ? T("pf_dernier", { d: der.date, z: der.zertifikat ? T("pf_zertifikat", { n: der.zertifikat.toUpperCase() }) : T("pf_kein_zertifikat") }) : T("pf_blanc_d");
      return '<button class="mode" data-modele="' + id + '"><b>' + esc(T("pf_modele_n", { n: rangModele(id) })) + '</b><span>' + esc(etat) + '</span></button>';
    }).join("") + '</div>';
  $("zone").querySelectorAll("[data-modele]").forEach(b => b.onclick = () => blancIntro(Number(b.dataset.modele)));
}

function inscrire(){
  accueil = pfAccueil;   // la fonction globale de commun.js, que son « ‹ » appelle
  // ouvrirTelcPflege(partie) de l'ecran Soins : une epreuve ouvre son chapitre, « blanc » les examens blancs
  EPR.forEach((e, k) => DTZ.partie({ id: e, ordre: 10 * (k + 1), titre: T("pf_epr_" + e), sous: T("pf_epr_" + e + "_s"), ouvrir: () => chapitre(e) }));
  DTZ.partie({ id: "BLANC", ordre: 99, titre: T("pf_blanc"), sous: T("pf_blanc_s"), ouvrir: () => Q.get("serie") ? blancIntro(Number(Q.get("serie"))) : examens() });
}

// ================================================================= L'ECRIT OUVERT SUR UN SUJET (16 nov. 2026)
// « Ma journee au service » (pflege/PLAN-CHAPITRES.md, etape E5) : l'ecran d'un chapitre ouvre cette page sur un
// sujet de la section Soins, lu dans pflege/datos/ecrit.json (session pflege-dialogues, FORMAT-DONNEES.md § 4) :
//     telc.html?apprendre=de&lang=<langue>&sujet=<id du sujet>&depuis=<id du chapitre>
// Un id inconnu (ou ?sujet= vide) donne la liste des sujets, sans erreur. LE CONTRAT AVEC L'APP (le cadre) :
//   - le sujet fini : parler("ecrit_fait", {sujet, depuis, coches, sur, punkte}) ; punkte sur 20 pour un sujet
//     d'examen (examen: true), null sinon ; puis parler("exercice", {juste}) comme les autres epreuves ;
//   - le retour : parler("fermer", {sujet, depuis, fini}) -- le « ‹ » de l'ecran d'ecriture (fini: false) et le
//     bouton « Retour au chapitre » de la fin (fini: true) ; l'app rouvre alors l'ecran du chapitre « depuis ».
// Le brouillon reste sur l'appareil (cle ecrit_<id>), le resultat dans l'etat du manuel (m.ecrits[id]). Un renvoi
// « ecrit:<id> » d'un chapitre du manuel ouvre le sujet ici meme, et revient au chapitre.
// Les textes du sujet sont dans les langues d'ecrit.json ; une langue absente retombe sur le francais.
const ECRIT_TYPES = ["aufnahme", "biografie", "pflegebericht", "sturz", "nachricht"];
const DEPUIS = Q.get("depuis") || "";
const lg = o => !o ? "" : typeof o === "string" ? o : (o[LANGUE] || o.fr || "");
const sujetsEcrits = () => (PF.ecrit && PF.ecrit.sujets) || [];
const niveauSujet = s => s.niveau + (s.niveau_max && s.niveau_max !== s.niveau ? "–" + s.niveau_max : "");
// le cadre se referme ; hors de l'app (la page ouverte seule), on revient a l'accueil du module
function retourCadre(id, fini){
  silence(); arreterSon();
  parler("fermer", { sujet: id || "", depuis: DEPUIS, fini: !!fini });
  if (window.parent === window) accueil();
}
// l'entree par l'adresse (telc.html?sujet=)
function sujetDepuisAdresse(id){
  if (sujetsEcrits().some(x => x.id === id)) ouvrirEcrit(id, { retour: fini => retourCadre(id, fini), libelleFin: T(DEPUIS ? "pf_retour_chapitre" : "pf_terminer") });
  else if (sujetsEcrits().length) listeEcrits({ retour: () => retourCadre("", false) });
  else accueil();
}
function ouvrirEcrit(id, ctx){
  const s = sujetsEcrits().find(x => x.id === id);
  if (!s) return listeEcrits(ctx);
  ecrireSujet(s, ctx);
}
function listeEcrits(ctx){
  ecran(T("pf_ecrit_liste"));
  DTZ.surRetour(() => { (ctx && ctx.retour ? ctx.retour : () => accueil())(false); return true; });
  const S = sujetsEcrits(), faits = etatManuel().ecrits || {};
  const types = ECRIT_TYPES.concat([...new Set(S.map(x => x.type))].filter(t => !ECRIT_TYPES.includes(t)));
  $("zone").innerHTML = '<div class="bloc"><h2>' + esc(T("pf_ecrit_liste")) + '</h2><p class="petit">' + esc(T("pf_ecrit_liste_s")) + '</p></div>' +
    types.map(t => {
      const l = S.filter(x => x.type === t);
      return l.length ? '<div class="bloc"><div class="section">' + esc(T("pf_ecrit_type_" + t)) + '</div>' + l.map(x =>
        '<button class="mode" data-sujet="' + esc(x.id) + '"><b lang="de">' + esc(x.titre_de || x.id) + '</b><span>' + esc(lg(x.titre)) + ' · ' + esc(niveauSujet(x)) +
        (faits[x.id] ? '</span><span class="chap-prog">' + esc(T("pf_ecrit_fait", { n: faits[x.id].coches, sur: faits[x.id].sur })) : "") + '</span></button>').join("") + '</div>' : "";
    }).join("");
  $("zone").querySelectorAll("[data-sujet]").forEach(b => b.onclick = () =>
    ouvrirEcrit(b.dataset.sujet, { retour: () => listeEcrits(ctx), libelleFin: T("pf_ecrit_retour_liste") }));
}
function ficheSoins(f){
  if (!f) return "";
  return '<div class="doc fiche" dir="ltr"><div class="k" lang="de">' + esc(f.titre_de || "") + '</div>' +
    (f.rubriques || []).map(r => '<div class="zeile"><span><span lang="de">' + esc(r.rubrique_de || "") + '</span>' +
      (lg(r.rubrique) && lg(r.rubrique) !== r.rubrique_de ? '<small class="trad-rubrique" dir="auto">' + esc(lg(r.rubrique)) + '</small>' : "") + '</span>' +
      '<b lang="de">' + esc(r.texte_de || (r.champs || []).map(c => (c.coche ? "☑ " : "☐ ") + c.label_de).join(" · ")) + '</b></div>').join("") + '</div>';
}
function ecrireSujet(s, ctx){
  const cle = "ecrit_" + s.id;
  ecran(lg(s.titre) || s.titre_de);
  DTZ.surRetour(() => { ctx.retour(false); return true; });
  const pieges = s.pieges || [];
  const groupes = s.briques_groupes || (s.briques && s.briques.length ? [{ briques: s.briques }] : []);
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("pf_ecrit_type_" + s.type)) + ' · ' + esc(niveauSujet(s)) + '</div>' +
      '<h2 lang="de">' + esc(s.titre_de || "") + '</h2>' +
      '<p class="consigne" lang="de">' + esc(s.consigne_de || "") + '<span class="fr">' + esc(lg(s.consigne)) + '</span></p></div>' +
    '<div class="bloc">' + ficheSoins(s.fiche) + '</div>' +
    (pieges.length ? '<div class="bloc"><details><summary>' + esc(T("pf_ecrit_pieges")) + '</summary><ul class="redemittel">' +
      pieges.map(p => '<li>' + esc(lg(p)) + '</li>').join("") + '</ul></details></div>' : "") +
    (groupes.length ? '<div class="bloc"><details><summary>' + esc(T("pf_ecrit_briques")) + '</summary>' + groupes.map(g =>
      (g.titre_de ? '<div class="rubrik-t"><span lang="de">' + esc(g.titre_de) + '</span>' + (lg(g.titre) ? ' <span class="petit">· ' + esc(lg(g.titre)) + '</span>' : "") + '</div>' : "") +
      '<ul class="briques">' + (g.briques || []).map(b => '<li><span lang="de">' + esc(b.de) + '</span>' + (lg(b.trad) ? '<small>' + esc(lg(b.trad)) + '</small>' : "") + '</li>').join("") + '</ul>').join("") +
      '</details></div>' : "") +
    '<div class="bloc"><textarea id="pfTexte" lang="de" rows="12" spellcheck="false" placeholder="' + esc(T("pf_ecrit_ici")) + '">' + esc(lire(cle, "")) + '</textarea>' +
      '<p class="petit" id="pfMots"></p></div>';
  const ta = $("pfTexte"), compte = () => {
    const n = mots(ta.value);
    $("pfMots").textContent = T("pf_mots", { n }) + (s.examen ? (n < 120 ? " · " + T("pf_mots_peu") : n > 170 ? " · " + T("pf_mots_trop") : "") : "");
  };
  ta.oninput = () => { compte(); ecrire(cle, ta.value); };
  compte();
  const fini = () => comparerSujet(s, ta.value, ctx);
  bouton(T("pf_ecrit_fini"), () => mots(ta.value) < 10 ? confirmer(T("pf_rendre_court"), fini, T("pf_rendre")) : fini());
}
// la comparaison : ce que le texte doit dire (on coche), le modele, et pour un sujet d'examen la note sur 20
function comparerSujet(s, texte, ctx){
  ecran(T("pf_ecrit_comparer"));
  DTZ.surRetour(() => { ecrireSujet(s, ctx); return true; });
  const pts = (s.points && s.points.length) ? s.points : (s.points_cles || []).map((de, k) => ({ id: "p" + k, de }));
  const coches = new Set();
  const g = { gestaltung: null, korrektheit: null, wortschatz: null };
  const grille = ((PF.ecrit || {}).grilles || {})[s.grille];
  const modele = (de, trad, titre, ouvert) => de ? '<details' + (ouvert ? " open" : "") + '><summary>' + esc(titre) + '</summary>' +
    de.split(/\n+/).map(p => '<p lang="de">' + esc(p) + '</p>').join("") +
    (lg(trad) ? '<details class="trad"><summary>' + esc(T("pf_ecrit_traduction")) + '</summary>' + lg(trad).split(/\n+/).map(p => '<p>' + esc(p) + '</p>').join("") + '</details>' : "") + '</details>' : "";
  const rendre = () => {
    const n = coches.size, inhalt = B.inhaltPunkte(pts.length, n);
    const note = B.punkteSchreiben(Object.assign({ inhalt }, g));
    $("zone").innerHTML =
      '<div class="bloc"><details><summary>' + esc(T("pf_ton_texte")) + '</summary><p lang="de" class="entendu">' + esc(texte || "—") + '</p></details></div>' +
      '<div class="bloc"><h2>' + esc(T("pf_ecrit_coches")) + ' · ' + esc(T("pf_ecrit_n", { n, sur: pts.length })) + '</h2>' +
        '<p class="petit">' + esc(T("pf_ecrit_coches_s")) + '</p><div class="coches">' +
        pts.map(p => '<button type="button" class="coche' + (coches.has(p.id) ? " ok" : "") + '" aria-pressed="' + coches.has(p.id) + '" data-pt="' + esc(p.id) + '">' +
          '<b lang="de">' + esc(p.de) + '</b>' + (lg(p.trad) ? '<small>' + esc(lg(p.trad)) + '</small>' : "") + '</button>').join("") + '</div>' +
        (s.examen ? '<p class="petit">' + esc(T("pf_crit_inhalt")) + ' · ' + inhalt + ' / 5. ' + esc(T("pf_ecrit_inhalt")) + '</p>' : "") + '</div>' +
      '<div class="bloc">' + modele(s.corrige_de, s.corrige, T("pf_ecrit_modele", { n: s.corrige_niveau || s.niveau }), true) +
        modele(s.corrige_b1_de, s.corrige_b1, T("pf_ecrit_modele_b1"), false) + '</div>' +
      (s.examen && inhalt ? ["gestaltung", "korrektheit", "wortschatz"].map(k => selecteur(k, 5, g[k], "schreiben")).join("") : "") +
      (s.examen ? '<div class="bloc"><div class="score">' + note + ' / 20</div><p class="petit" style="text-align:center">' + esc(nomNiveau(B.niveauSchreiben(note))) + '</p>' +
        '<p class="petit">' + esc(T("pf_ecrit_estimation")) + '</p></div>' : "") +
      (grille && grille.criteres ? '<div class="bloc"><details><summary>' + esc(lg(grille.titre) || T("pf_ecrit_grille")) + '</summary>' +
        grille.criteres.map(c => '<div class="rubrik"><div class="rubrik-t">' + esc(lg(c.titre)) + '</div><p>' + esc(lg(c.question)) + '</p>' +
          (lg(c.conseil) ? '<p class="petit">' + esc(lg(c.conseil)) + '</p>' : "") + '</div>').join("") + '</details></div>' : "");
    $("zone").querySelectorAll("[data-pt]").forEach(b => b.onclick = () => {
      coches.has(b.dataset.pt) ? coches.delete(b.dataset.pt) : coches.add(b.dataset.pt);
      garderScroll(rendre);
    });
    brancherSelecteurs(g, () => garderScroll(rendre));
    const pret = !s.examen || !inhalt || ["gestaltung", "korrektheit", "wortschatz"].every(k => g[k] !== null);
    if (pret) bouton(ctx.libelleFin || T("pf_terminer"), () => {
      const punkte = s.examen ? note : null;
      noterManuel(m => { m.ecrits = m.ecrits || {}; m.ecrits[s.id] = { date: new Date().toISOString().slice(0, 10), coches: n, sur: pts.length, punkte }; });
      parler("ecrit_fait", { sujet: s.id, depuis: DEPUIS, coches: n, sur: pts.length, punkte });
      parler("exercice", { juste: s.examen ? punkte >= 7 : n * 10 >= pts.length * 7 });
      ctx.retour(true);
    });
    else $("suite").hidden = true;
  };
  rendre();
}

// pour le controle et les sondes : le calcul, et l'index des questions (rien d'ecrit)
window.SOINS_EXAMEN = { PF, juste, pointsDe, estimer, infosTrouvees, itemsDe, choixDe, modeles, progresChapitre, chapitre,
  sujet: sujetDepuisAdresse, sujetsEcrits };
})();
