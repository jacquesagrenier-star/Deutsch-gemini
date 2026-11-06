// LE TELC A2·B1 AVEC MARK ET ANNA -- ECOUTER ET NOTER (HOEREN UND SCHREIBEN), items 52-56
// (6 nov. 2026, session « telc : Ecouter »). Charge APRES hoeren.js, dont il reprend les outils (window.TELC_ECOUTE).
//
// LE FORMAT DU TELC, JAMAIS SON CONTENU (preparation-examens/FORMAT-TELC.md) : 5 messages de repondeur, chacun
// entendu 2 fois ; une note a completer par message (un objet, un moment, une heure, un numero) ; 5 x 1 point,
// comptes dans l'ecrit (TELC.epreuve, sur: {Schreiben: 5}). Les messages sont les notres : donnees/hoeren-schreiben.json.
//
// LA SAISIE EST TOLERANTE (verifierNote) : une heure (9:30, 9.30, 9 Uhr 30, halb zehn…), un nombre ou un numero
// (les chiffres seuls : « 45 € » = 45), un mot (sans majuscules, ae = ä, sans article). Pour un mot qui n'est pas
// epele, une lettre de travers compte encore, avec un avertissement : la regle exacte du telc sur l'orthographe des
// notes n'est pas dans FORMAT-TELC.md (a verifier). Un nom epele lettre par lettre (exakt) doit etre exact.
//
// Inscrit aussi un examen blanc de l'ecoute seule (DTZ.examen « Ecouter, comme a l'examen » : Hoeren puis Hoeren und
// Schreiben, 35 min, verdict sur 60), utile tant que l'examen blanc complet (examen-blanc.js) n'est pas la.

(function(){
"use strict";
const O = window.TELC_ECOUTE, E = O.E;

const HS_EN = {
  hs_titre: "Listening and notes", hs_sous: "Hören und Schreiben · 5 messages",
  hs_section: "Section · Listening and notes",
  hs_mark_debut: "Five messages on my voicemail: take the note for me. A word, a time or a number is enough, not a sentence.",
  hs_commencer: "Start the messages",
  hs_verifier: "Check", hs_ecris: "write here", hs_note: "The note",
  hs_presque: "Counted as correct, but watch the spelling: “{r}”.",
  hs_points: "In the exam, that would be {n} point(s) out of 5, counted in Writing (Schreiben).",
  hs_ex_titre: "Listening, as in the exam", hs_ex_sous: "Hören then Hören und Schreiben, 35 min: the audio plays by itself, once or twice depending on the part.",
  hs_ex_regles: "As on exam day: the audio plays by itself, with its reading time and pauses. You can't stop it or replay it. Answer while you listen; the answers come at the end.",
  hs_ex_lancer: "Start listening", hs_ex_fin: "End of the listening test", hs_ex_resultat: "Listening result", hs_ex_corrige: "The answers",
  hs_v_b1: "B1 in Listening: at least 42 points out of 60.",
  hs_v_a2: "A2 in Listening: at least 24 points out of 60. You need {n} more point(s) for B1.",
  hs_v_moins: "Below A2: you need {n} more point(s) to reach 24 out of 60."
};
textesTelc({ en: HS_EN, fr: {
  hs_titre: "Écouter et noter", hs_sous: "Hören und Schreiben · 5 messages",
  hs_section: "Section · Écouter et noter",
  hs_mark_debut: "Cinq messages sur mon répondeur : prends la note à ma place. Un mot, une heure ou un nombre suffit, pas une phrase.",
  hs_commencer: "Commencer les messages",
  hs_verifier: "Vérifier", hs_ecris: "écris ici", hs_note: "La note",
  hs_presque: "Compté juste, mais attention à l'orthographe : « {r} ».",
  hs_points: "À l'examen, cela ferait {n} point(s) sur 5, comptés dans l'écrit (Schreiben).",
  hs_ex_titre: "Écouter, comme à l'examen", hs_ex_sous: "Hören puis Hören und Schreiben, 35 min : le son passe tout seul, une ou deux fois selon la partie.",
  hs_ex_regles: "Comme le jour de l'examen : le son passe tout seul, avec ses temps de lecture et ses pauses. Tu ne peux ni l'arrêter ni le rejouer. Réponds pendant l'écoute ; le corrigé vient à la fin.",
  hs_ex_lancer: "Commencer l'écoute", hs_ex_fin: "Fin de l'écoute", hs_ex_resultat: "Résultat de l'écoute", hs_ex_corrige: "Le corrigé",
  hs_v_b1: "B1 en Écouter : au moins 42 points sur 60.",
  hs_v_a2: "A2 en Écouter : au moins 24 points sur 60. Il manque {n} point(s) pour le B1.",
  hs_v_moins: "Sous le A2 : il manque {n} point(s) pour atteindre 24 sur 60."
}});

const HS = { d: null, serie: null, us: [], page: 0, saisie: {}, verif: {} };
DTZ.charger(fetch("donnees/hoeren-schreiben.json", {cache: "no-cache"})
  .then(r => { if (!r.ok) throw new Error("hoeren-schreiben.json"); return r.json(); })
  .then(d => { HS.d = d; }));

DTZ.partie({id: "HS", ordre: 50, titre: T("hs_titre"), sous: T("hs_sous"), ouvrir: () => ouvrirHS()});
TELC.epreuve({id: "HS", ordre: 50, minutes: 0, sur: {Schreiben: 5}, lancer: fini => examenHS(fini)});
DTZ.examen({id: "telcEcoute", ordre: 40, titre: T("hs_ex_titre"), sous: T("hs_ex_sous"), lancer: () => examenEcoute()});

// ============ LA NOTE ============
function normal(s){
  return String(s || "").toLowerCase().replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss")
    .replace(/[„“"'«»()]/g, " ").replace(/\b(der|die|das|ein|eine|einen|im|am|kiosk)\b/g, " ").replace(/[.,;!?]+$/g, "").replace(/\s+/g, " ").trim();
}
function minutes(s){
  const m = String(s).toLowerCase().replace(/\s+/g, " ").match(/^(\d{1,2})(?:\s*(?::|\.|h|uhr)\s*(\d{2})?)?\s*(?:uhr)?$/);
  if (!m) return null;
  const h = +m[1], mi = m[2] ? +m[2] : 0;
  return h > 24 || mi > 59 ? null : (h % 12) * 60 + mi;
}
function distance(a, b){
  const d = [...Array(b.length + 1).keys()];
  for (let i = 1; i <= a.length; i++){
    let prec = d[0]; d[0] = i;
    for (let j = 1; j <= b.length; j++){ const t = d[j]; d[j] = Math.min(d[j] + 1, d[j - 1] + 1, prec + (a[i - 1] === b[j - 1] ? 0 : 1)); prec = t; }
  }
  return d[b.length];
}
function verifierNote(m, saisie){
  const s = String(saisie || "").trim();
  if (!s) return "faux";
  const formes = [m.loesung].concat(m.akzeptiert || []).map(normal);
  if (formes.includes(normal(s))) return "juste";
  if (m.typ === "uhrzeit"){ const a = minutes(s); return a !== null && a === minutes(m.loesung) ? "juste" : "faux"; }
  if (m.typ === "zahl" || m.typ === "telefon"){ const ch = x => String(x).replace(/\D/g, ""); return ch(s) && ch(s) === ch(m.loesung) ? "juste" : "faux"; }
  if (!m.exakt && formes.some(f => f.length >= 4 && distance(normal(s), f) <= 1)) return "presque";
  return "faux";
}
const noteOk = etat => etat === "juste" || etat === "presque";
function unitesHS(s){ return s.nachrichten.map(m => ({teil: "HS", fois: 2, lecture: 10, data: m, rollen: m.rollen, segs: [m.audio], cles: ["telcHS" + s.id + "-" + m.nr], questions: [{nr: m.nr}]})); }
// la note : ses lignes, la case a remplir a la place de {}
function rendreNotiz(m, valeur, etat, fige){
  const champ = '<input type="text" id="saisie' + m.nr + '" data-nr="' + m.nr + '" autocomplete="off" autocapitalize="off" spellcheck="false" lang="de" placeholder="' + esc(T("hs_ecris")) + '"' +
    ' value="' + esc(valeur || "") + '"' + (fige ? " disabled" : "") + (etat ? ' class="' + (noteOk(etat) ? "ok" : "ko") + '"' : "") + '>';
  return '<div class="notiz" lang="de"><div class="t"><span class="num">' + m.nr + '</span>' + esc(m.notiz.titel) + '</div>' +
    m.notiz.zeilen.map(z => '<div>' + (z.includes("{}") ? esc(z).replace("{}", champ) : esc(z)) + '</div>').join("") + '</div>';
}
function aideNote(m, valeur, etat, corrige){
  return '<div class="aide">' + (corrige ? '<span class="petit">' + esc(T("ho_ta_reponse", {r: valeur || T("ho_sans_reponse")})) + '</span>' : "") +
    '<span class="verdict ' + (noteOk(etat) ? "ok" : "ko") + '">' + esc(etat === "juste" ? T("ho_juste") : etat === "presque" ? T("hs_presque", {r: m.loesung}) : T("ho_faux", {r: m.loesung})) + '</span>' +
    '<div class="dit"><img src="' + MARK_IMG + '" alt=""><span class="erkl">' + esc(champTelc(m, "erkl")) + '</span></div></div>';
}

// ============ L'ENTRAINEMENT ============
async function ouvrirHS(serie){
  O.stopSon(); arreterChrono();
  HS.serie = serie || await choisirSerie(HS.d.series, () => [], "HS");
  HS.us = unitesHS(HS.serie); HS.page = 0; HS.saisie = {}; HS.verif = {}; E.ecoutes = {};
  DTZ.surRetour(() => { O.toutesLesSections(); return true; });
  if (serie) pageHS(); else introHS();
}
function introHS(){
  $("titre").textContent = T("hs_titre");
  $("zone").innerHTML = '<div class="bloc">' + O.mark(T("hs_mark_debut")) + '</div><div class="bloc">' + O.blocFormat("HS") + '</div>';
  const suite = $("suite"); suite.hidden = false; suite.textContent = T("hs_commencer");
  suite.onclick = () => pageHS();
  window.scrollTo(0, 0);
}
function pageHS(garderScroll){
  const u = HS.us[HS.page], m = u.data, d = HS.d, etat = HS.verif[m.nr], fini = !!etat;
  $("titre").textContent = T("hs_titre");
  let h = '<div class="bloc"><div class="section">' + esc(T("hs_section")) + '</div>' +
    O.pointsDe(HS.us.map(x => x.questions[0]), [m.nr], q => HS.verif[q.nr] ? noteOk(HS.verif[q.nr]) : null) +
    '<button class="lien" id="voirFmt">' + esc(T("ho_format")) + '</button></div>';
  h += '<div class="bloc">';
  if (HS.page === 0) h += O.consigne(d.consigne) + O.mark(champTelc(d.conseil, "text"));
  h += O.bandeau(u);
  h += '<p class="petit">' + esc(T("hs_note")) + '</p>' + rendreNotiz(m, HS.saisie[m.nr], etat, fini);
  const lec = O.lecteur("HS" + HS.page, u, fini, () => pageHS(true));
  h += lec.h;
  if (fini) h += aideNote(m, HS.saisie[m.nr], etat) + '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + O.transcription(u);
  h += '</div><p class="petit" style="text-align:center">' + esc(T("ho_voix_tel")) + '</p>';
  const y = window.scrollY;
  $("zone").innerHTML = h;
  lec.brancher();
  $("voirFmt").onclick = () => O.montrerFormat("HS");
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { O.stopSon(); HS.page = HS.us.findIndex(x => x.data.nr === +b.dataset.aller); pageHS(); });
  const champ = $("saisie" + m.nr), suite = $("suite");
  const majSuite = () => { suite.hidden = !fini && !(HS.saisie[m.nr] || "").trim(); };
  if (champ && !fini){
    champ.oninput = () => { HS.saisie[m.nr] = champ.value; majSuite(); };
    champ.onkeydown = ev => { if (ev.key === "Enter" && champ.value.trim()) verifierHS(); };
  }
  suite.textContent = fini ? T("ho_continuer") : T("hs_verifier");
  majSuite();
  suite.onclick = () => {
    if (!fini){ verifierHS(); return; }
    O.stopSon();
    const reste = HS.us.findIndex((x, k) => k > HS.page && !HS.verif[x.data.nr]), avant = HS.us.findIndex(x => !HS.verif[x.data.nr]);
    if (reste >= 0 || avant >= 0){ HS.page = reste >= 0 ? reste : avant; pageHS(); } else recapHS();
  };
  if (garderScroll) window.scrollTo(0, y); else window.scrollTo(0, 0);
}
function verifierHS(){
  const m = HS.us[HS.page].data;
  const etat = verifierNote(m, HS.saisie[m.nr]);
  HS.verif[m.nr] = etat; O.stopSon();
  parler("exercice", {juste: noteOk(etat)}); if (noteOk(etat)) parler("bonne");
  pageHS(true);
}
function recapHS(){
  O.stopSon(); $("suite").hidden = true;
  const s = HS.serie, ms = s.nachrichten, bons = ms.filter(m => noteOk(HS.verif[m.nr])).length;
  marquerFait("HS", s);
  resultat("HS", {serie: s.id, bons, sur: 5});
  parler("fini", {bons, faits: 5});
  const mot = bons >= 4 ? "ho_mark_bien" : bons >= 3 ? "ho_mark_moyen" : "ho_mark_faible";
  const ligne = m => '<div class="q">' + rendreNotiz(m, HS.saisie[m.nr], HS.verif[m.nr], true) + aideNote(m, HS.saisie[m.nr], HS.verif[m.nr]) + '</div>';
  const rates = ms.filter(m => !noteOk(HS.verif[m.nr])), justes = ms.filter(m => noteOk(HS.verif[m.nr]));
  const fin = O.boutonsFin("HS", () => ouvrirHS(s));
  $("titre").textContent = T("hs_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("hs_titre")) + ' · ' + esc(T("ho_recap")) + '</div>' +
      '<div class="score">' + esc(T("ho_score", {n: bons, t: 5})) + '</div>' +
      '<p class="petit" style="text-align:center">' + esc(T("hs_points", {n: bons})) + '</p>' + O.mark(T(mot)) + '</div>' +
    '<div class="bloc">' + rates.concat(justes).map(ligne).join("") + '</div>' + fin.h;
  fin.brancher();
  window.scrollTo(0, 0);
}

// ============ L'EXAMEN BLANC : HOEREN UND SCHREIBEN ============
// Les 5 notes sur une feuille ; pour chaque message : 10 s pour lire la note, le message, 5 s, le message encore,
// 15 s pour ecrire (pauses : les notres). fini({pts: {Schreiben}, detail}).
let Y = null;
async function examenHS(fini, serie){
  O.stopSon(); debloquerSon();
  const s = serie || await choisirSerie(HS.d.series, () => [], "XHS");
  const moi = Y = {s, ms: unitesHS(s), saisie: {}};
  const jeton = E.jeton, vivant = () => Y === moi && E.jeton === jeton, r = O.deroulement(vivant);
  $("titre").textContent = T("hs_titre") + " · Hören und Schreiben"; $("suite").hidden = true;
  $("zone").innerHTML = '<div class="bloc"><div class="section">Hören und Schreiben · ' + esc(T("ho_HS")) + '</div><div class="ecoute" id="exEtat"></div>' + O.bandeau(moi.ms[0]) +
    '<p class="consigne" lang="de">' + esc(HS.d.consigne.text) + '</p>' +
    moi.ms.map(u => '<div class="q" id="q' + u.data.nr + '">' + rendreNotiz(u.data, "", null, false) + '</div>').join("") + '</div>';
  document.querySelectorAll("#zone input[data-nr]").forEach(c => c.oninput = () => { moi.saisie[+c.dataset.nr] = c.value; });
  window.scrollTo(0, 0);
  if (!await r.consigne(HS.d.consigne)) return;
  for (const u of moi.ms){
    const nr = u.data.nr;
    O.marquerEx([nr]); const c = $("saisie" + nr); if (c) c.focus({preventScroll: true});
    if (!await r.pause(u.lecture, T("ho_ex_lecture")) || !await r.ecouter(u.segs, u.cles, [nr]) || !await r.pause(5, T("ho_ex_pause")) || !await r.ecouter(u.segs, u.cles, [nr]) || !await r.pause(15, T("ho_ex_pause"))) return;
  }
  const ende = E.d.consignes.ende;
  await O.direLigne(ende);
  if (!vivant()) return;
  const etats = {}; moi.ms.forEach(u => { etats[u.data.nr] = verifierNote(u.data, moi.saisie[u.data.nr]); });
  const bons = moi.ms.filter(u => noteOk(etats[u.data.nr])).length;
  marquerFait("XHS", s);
  resultat("HS", {examen: true, serie: s.id, bons, sur: 5});
  const html = '<div class="bloc"><div class="section">' + esc(T("hs_titre")) + '</div>' +
    moi.ms.map(u => '<div class="q">' + rendreNotiz(u.data, moi.saisie[u.data.nr], etats[u.data.nr], true) + aideNote(u.data, moi.saisie[u.data.nr], etats[u.data.nr], true) + '</div>' + O.transcription(u)).join("") + '</div>';
  fini({pts: {Schreiben: bons}, detail: {bons, sur: 5, html}});
}

// ============ L'EXAMEN BLANC DE L'ECOUTE SEULE ============
async function examenEcoute(){
  O.stopSon();
  let fini = false;
  DTZ.surRetour(() => { if (fini) return false; confirmer(T("quitter_q"), () => { O.stopSon(); arreterChrono(); Y = null; accueil(); }, T("quitter")); return true; });
  $("titre").textContent = T("hs_ex_titre");
  $("zone").innerHTML = '<div class="bloc">' + O.mark(T("hs_ex_regles")) + '</div><div class="bloc">' + O.blocFormat("") + '</div>';
  const suite = $("suite"); suite.hidden = false; suite.textContent = T("hs_ex_lancer");
  suite.onclick = async () => {
    suite.hidden = true;
    chrono(35 * 60, "haut");
    const h = await new Promise(ok => O.examenH(ok));
    const hs = await new Promise(ok => examenHS(ok));
    fini = true; arreterChrono();
    const p = h.pts.Hoeren, niv = p >= 42 ? "b1" : p >= 24 ? "a2" : "moins";
    const verdict = niv === "b1" ? T("hs_v_b1") : niv === "a2" ? T("hs_v_a2", {n: 42 - p}) : T("hs_v_moins", {n: 24 - p});
    ecrire("dernier", {date: new Date().toLocaleDateString(LANGUE), texte: T("hs_ex_titre") + " · " + p + " / 60"});
    $("titre").textContent = T("hs_ex_resultat");
    $("zone").innerHTML =
      '<div class="bloc" style="align-items:center;text-align:center"><div class="section">' + esc(T("hs_ex_fin")) + '</div>' +
        '<div class="score">' + p + ' / 60</div><span class="niveau ' + niv + '">' + esc(T("niv_" + niv)) + '</span>' +
        '<div class="jauge" style="align-self:stretch"><i style="width:' + Math.round(p / 60 * 100) + '%"></i><s style="left:40%"><em>A2 · 24</em></s><s style="left:70%"><em>B1 · 42</em></s></div>' +
        '<p>' + esc(verdict) + '</p>' + O.detailTeils(h.detail.parTeil) +
        '<p class="petit">' + esc(T("hs_points", {n: hs.pts.Schreiben})) + '</p>' +
        '<p class="petit">' + esc(T("ho_seuils_h")) + '</p></div>' +
      '<div class="bloc"><h2>' + esc(T("hs_ex_corrige")) + '</h2></div>' + h.detail.html + hs.detail.html +
      '<div class="bloc boutons"><button class="secondaire" id="exToutes">' + esc(T("ho_toutes")) + '</button></div>';
    $("exToutes").onclick = O.toutesLesSections;
    DTZ.surRetour(() => { O.toutesLesSections(); return true; });
    window.scrollTo(0, 0);
  };
  window.scrollTo(0, 0);
}

window.TELC_ECOUTE.verifierNote = verifierNote;
window.TELC_ECOUTE.ouvrirHS = ouvrirHS;
window.TELC_ECOUTE.examenHS = examenHS;
window.TELC_ECOUTE.examenEcoute = examenEcoute;
})();
