"use strict";
// LE DTZ AVEC MARK ET ANNA -- ECOUTER (HOEREN) ET LIRE (LESEN), et l'examen blanc qui les regroupe (3 nov. 2026).
//
// LE FORMAT EST CELUI DU DTZ, JAMAIS SON CONTENU (Pruefungshandbuch 2009) : Hoeren 25 min, 20 items en 4 Teile ;
// Lesen 45 min, 25 items en 5 Teile ; verdict sur 45 (A2 des 20, B1 des 33). Tous les textes sont les notres,
// dans la vie de Mark a Berlin (donnees/hoeren.json, lesen.json, controles par tests/dtz.py).
//
// DEUX MODES :
//   Entrainement -- un Teil a la fois ; apres CHAQUE reponse, l'explication, la traduction et un mot de Mark ;
//                   la transcription apres la derniere question d'un texte ; on peut reecouter. Les mots cles de
//                   chaque question entrent dans la repetition espacee de l'app (message « reponse », comme les
//                   themes illustres) ;
//   Examen blanc -- sobre et minute ; le son passe UNE fois, avec ses pauses, comme l'enregistrement de
//                   l'examen ; feuille de reponses ; verdict puis corrige, transcriptions comprises.
// Les outils communs (voix, minuterie, panneau, tirage, verdict global) sont dans commun.js.

Object.assign(TXT, {
  hoeren_s: "Hören · 4 parties · 25 min", lesen_s: "Lesen · 5 parties · 45 min",
  choisir_teil: "Quelle partie ?",
  H_T1: "Annonces au téléphone et par haut-parleur", H_T2: "Informations à la radio", H_T3: "Conversations", H_T4: "Avis à la radio",
  L_T1: "Listes et panneaux", L_T2: "Petites annonces", L_T3: "Presse et avis", L_T4: "Brochures d'information", L_T5: "Lettre à compléter",
  questions: "{n} questions",
  ex_complet: "Écouter et lire", ex_complet_s: "Hören 25 min, puis Lesen 45 min, comme l'écrit du DTZ (sans l'expression écrite). Sur 45.",
  ex_hoeren: "Écouter seulement", ex_hoeren_s: "Hören, 25 min. Sur 20.",
  ex_lesen: "Lire seulement", ex_lesen_s: "Lesen, 45 min. Sur 25.",
  ex_regles: "Le son passe une seule fois, avec les pauses de l'enregistrement. Pas de traduction, pas d'explication : le corrigé vient après le verdict.",
  ecouter_titre: "Écouter", lire_titre: "Lire",
  ecouter_btn: "Écouter", reecouter: "Réécouter", en_cours: "Écoute…",
  exemple: "Exemple", juste: "Juste !", faux: "Pas tout à fait.", bonne: "La bonne réponse : {r}",
  transcription: "Ce qu'on entendait", trad: "En français : {t}",
  fin_teil: "{b} bonnes réponses sur {n}",
  mark_bien: "Bien joué ! Cette partie, tu la tiens.", mark_moyen: "On progresse. On la refait bientôt ?", mark_dur: "Celle-là est difficile. Relisons les explications ensemble.",
  rendre: "Rendre ma copie",
  rendre_q: "Rendre maintenant ? Il reste du temps, et {n} question(s) sans réponse.",
  oui_rendre: "Oui, rendre", continuer: "Continuer",
  pause: "Pause de 5 minutes avant Lesen.", pause_passer: "Passer la pause",
  hoeren_fin: "Fin de l'écoute. Tes réponses sont gardées.",
  joue: "Écoute en cours — le son ne passe qu'une fois.", lecture_t: "Temps de lecture",
  v_b1: "Le B1 est atteint en Écouter et Lire.", v_a2: "Le A2 est atteint ; il manque {n} point(s) pour le B1.", v_moins: "Il manque {n} point(s) pour le A2.",
  v_regle: "Au DTZ, Hören et Lesen comptent ensemble : A2 dès 20 sur 45, B1 dès 33. Pour le B1 de l'examen entier, il faut aussi le B1 à l'oral.",
  v_tendance: "Tendance : {n}, si l'autre partie va aussi bien.",
  v_seul: "Partie seule : le seuil officiel porte sur Hören et Lesen ensemble ; ce résultat donne une tendance.",
  corrige: "Voir le corrigé", ta_reponse: "Ta réponse : {r}", sans_reponse: "Pas de réponse",
  mark_v_b1: "B1 ! Bravo : Écouter et Lire, c'est gagné.", mark_v_a2: "A2, c'est un début. Le B1 n'est pas loin : on s'entraîne encore ?", mark_v_moins: "Ouf, c'est dur. Reprenons les parties une par une."
});
const de = s => '<span lang="de" dir="ltr">' + esc(s) + '</span>';

let H = null, L = null;
// les reponses en cours : celles de l'examen s'il y en a un, sinon celles de l'entrainement
const REP = () => (EX ? EX.rep : ENT ? ENT.rep : null);

// ============ LES UNITES : ce qui s'affiche ensemble (un texte et ses questions) ============
// Hoeren T1/T2 : une annonce, une question. T3 : une conversation, deux questions (l'exemple en a une).
// T4 : l'intro, les avis, les phrases a-f. Lesen : un document et toutes ses questions.
function question(part, it, extra){
  return Object.assign({
    id: part + it.nr, part, nr: it.nr, beispiel: !!it.beispiel,
    kind: it.rf ? "rf" : "abc", options: it.optionen, bon: it.bon,
    frage: it.frage, frage_fr: it.frage_fr, options_fr: it.optionen_fr,
    erkl_fr: it.erkl_fr, mark_fr: it.mark_fr, mots: it.mots || []
  }, extra || {});
}
function unitesHoeren(s, teil){
  if (teil === "T4"){
    const t4 = s.T4, lettres = t4.saetze.map(x => x.b);
    return [{teil, intro: t4.intro, saetze: t4.saetze, thema: t4.thema, thema_fr: t4.thema_fr,
      cle: s.id + "-T4-intro",
      aussagen: t4.aussagen.map(a => ({audio: a.audio, cle: s.id + "-T4-" + a.nr, q: question("H", {nr: a.nr, beispiel: a.beispiel, frage: a.beispiel ? T("exemple") : "Person " + a.nr,
        bon: a.bon, erkl_fr: a.erkl_fr, mark_fr: a.mark_fr, mots: a.mots, frage_fr: ""}, {kind: "lettre", lettres, options: lettres, bon: a.bon})})),
      get questions(){ return this.aussagen.map(a => a.q); }}];
  }
  if (teil === "T3"){
    const us = [], conv = {};
    s.T3.forEach(it => {
      if (!it.gespraech){ us.push({teil, audio: it.audio, rollen: it.rollen, cle: s.id + "-T3-" + it.nr, questions: [question("H", it)]}); return; }
      if (!conv[it.gespraech]){ conv[it.gespraech] = {teil, audio: null, questions: []}; us.push(conv[it.gespraech]); }
      if (it.audio){ conv[it.gespraech].audio = it.audio; conv[it.gespraech].rollen = it.rollen; conv[it.gespraech].cle = s.id + "-T3-" + it.nr; }
      conv[it.gespraech].questions.push(question("H", it));
    });
    return us;
  }
  return s[teil].map(it => ({teil, audio: it.audio, typ: it.typ, cle: s.id + "-" + teil + "-" + it.nr, questions: [question("H", it)]}));
}
function unitesLesen(s, teil){
  const t = s[teil];
  if (teil === "T1") return [{teil, doc: t.dokument, situation: t.situation, questions: t.items.map(it => question("L", it))}];
  if (teil === "T2"){
    const lettres = t.anzeigen.map(a => a.b).concat("x");
    return [{teil, anzeigen: t.anzeigen, questions: t.items.map(it => question("L", {nr: it.nr, beispiel: it.beispiel, frage: it.situation, frage_fr: it.situation_fr,
      erkl_fr: it.erkl_fr, mark_fr: it.mark_fr, mots: it.mots}, {kind: "lettre", lettres, options: lettres, bon: it.bon}))}];
  }
  if (teil === "T3") return t.texte.map(tx => ({teil, texte: tx, questions: tx.items.map(it => question("L", it))}));
  if (teil === "T4") return [{teil, doc: t.dokument, questions: t.items.map(it => question("L", it))}];
  return [{teil, brief: t.brief, questions: t.luecken.map(lu => question("L", {nr: lu.nr, beispiel: lu.beispiel, frage: phraseDuTrou(t.brief, lu.nr), optionen: lu.optionen, bon: lu.bon,
    erkl_fr: lu.erkl_fr, mots: lu.mots, frage_fr: ""}))}];
}
// La phrase du trou, sous ses trois choix : sur un telephone, la lettre est deja loin quand on arrive au trou 24.
function phraseDuTrou(b, nr){
  const p = [b.betreff].concat(b.text).find(x => x.includes("{" + nr + "}")) || "";
  const phrases = p.split(/(?<=[.?!,])\s+/);
  const ph = phrases.find(x => x.includes("{" + nr + "}")) || p;
  return ph.replace("{" + nr + "}", "___").replace(/\{\d+\}/g, "…");
}
const unites = (part, s, teil) => part === "H" ? unitesHoeren(s, teil) : unitesLesen(s, teil);
const TEILE = {H: ["T1", "T2", "T3", "T4"], L: ["T1", "T2", "T3", "T4", "T5"]};
const consigneLesen = (s, teil) => s[teil].aufgabe;

// ============ LE RENDU DES DOCUMENTS ET DES QUESTIONS ============
function rendreDoc(u){
  if (u.doc && u.doc.typ === "wegweiser")
    return '<div class="doc wegweiser" lang="de"><div class="t">' + esc(u.doc.titel) + '</div>' +
      u.doc.zeilen.map(z => '<div class="z"><b>' + esc(z.etage) + '</b><span>' + esc(z.inhalt) + '</span></div>').join("") + '</div>';
  if (u.doc && u.doc.typ === "broschuere")
    return '<div class="doc brochure" lang="de"><div class="k">' + esc(u.doc.titel) + '<small>' + esc(u.doc.kopf) + '</small></div>' +
      u.doc.abschnitte.map(a => '<div class="s"><b>' + esc(a.titel) + '</b>' + esc(a.text) + '</div>').join("") + '</div>';
  if (u.anzeigen)
    return '<div class="doc annonces" lang="de">' + u.anzeigen.map(a => '<div class="annonce"><span class="l">' + a.b + '</span><div class="t">' + esc(a.titel) + '</div>' + esc(a.text) + '</div>').join("") + '</div>';
  if (u.texte){
    const t = u.texte, cls = t.typ === "zeitung" ? "journal" : t.typ === "aushang" ? "aushang" : "lettre";
    return '<div class="doc ' + cls + '" lang="de"><div class="k">' + esc(t.kopf) + '</div><h3>' + esc(t.titel) + '</h3>' +
      t.absaetze.map(p => '<p>' + esc(p).replace(/\n/g, "<br>") + '</p>').join("") + '</div>';
  }
  if (u.brief){
    // le trou se remplit du mot choisi : on relit sa phrase entiere avant de passer au suivant
    const b = u.brief, trou = (txt) => esc(txt).replace(/\{(\d+)\}/g, (m, n) => {
      const q = u.questions.find(x => String(x.nr) === n), v = q && (q.beispiel ? q.bon : (REP() || {})[q.id]);
      return '<span class="trou' + (n === "0" ? " ex" : "") + '">(' + n + ') ' + (v !== undefined && q ? esc(q.options[v]) : "……") + '</span>';
    });
    return '<div class="doc lettre" lang="de"><div class="entete"><div class="adr">' + esc(b.absender) + '</div></div><div class="adr">' + esc(b.empfaenger) + '</div>' +
      '<div class="date">' + esc(b.datum) + '</div><div class="objet">' + trou(b.betreff) + '</div>' + b.text.map(p => '<p>' + trou(p) + '</p>').join("") + '</div>';
  }
  return "";
}
function rendreT4(u){
  return '<div class="doc"><p class="consigne" lang="de">' + esc(u.thema) + '</p><div class="choix">' +
    u.saetze.map(x => '<div class="q" style="padding:8px 10px"><div class="tete"><span class="num">' + x.b + '</span><span class="frage" lang="de">' + esc(x.de) + '</span></div></div>').join("") + '</div></div>';
}
function libelle(q, v){
  if (v === undefined || v === null) return T("sans_reponse");
  if (q.kind === "lettre") return v;
  if (q.kind === "rf") return q.options[v];
  return ABC[v] + " · " + q.options[v];
}
function rendreQuestion(q, etat){
  // etat : {choisi, montrer (bonne et mauvaise visibles), fige}
  const rep = etat.choisi, fige = etat.fige || q.beispiel;
  const choisi = q.beispiel ? q.bon : rep;
  let boutons;
  if (q.kind === "lettre"){
    boutons = '<div class="choix ligne">' + q.lettres.map(l => {
      let c = "opt"; if (choisi === l) c += etat.montrer || q.beispiel ? (l === q.bon ? " juste" : " faux") : " pris";
      else if (etat.montrer && l === q.bon) c += " juste";
      return '<button class="' + c + '" data-q="' + q.id + '" data-v="' + l + '"' + (fige ? " disabled" : "") + '><b>' + l + '</b></button>';
    }).join("") + '</div>';
  } else {
    boutons = '<div class="choix' + (q.kind === "rf" ? " ligne" : "") + '">' + q.options.map((o, i) => {
      let c = "opt"; if (choisi === i) c += etat.montrer || q.beispiel ? (i === q.bon ? " juste" : " faux") : " pris";
      else if (etat.montrer && i === q.bon) c += " juste";
      return '<button class="' + c + '" data-q="' + q.id + '" data-v="' + i + '"' + (fige ? " disabled" : "") + '>' + (q.kind === "abc" ? '<b>' + ABC[i] + '</b>' : "") + '<span lang="de">' + esc(o) + '</span></button>';
    }).join("") + '</div>';
  }
  let aide = "";
  if ((etat.montrer && !etat.corrige) || (q.beispiel && etat.aide)){
    const ok = q.beispiel || rep === q.bon;
    aide = '<div class="aide">' + (q.beispiel ? '<span class="verdict">' + T("exemple") + '</span>' :
      '<span class="verdict ' + (ok ? "ok" : "ko") + '">' + (ok ? T("juste") : T("faux") + " " + T("bonne", {r: esc(libelle(q, q.bon))})) + '</span>') +
      (q.frage_fr ? '<span class="trad">' + T("trad", {t: esc(q.frage_fr + (q.options_fr && q.kind === "abc" ? " — " + q.options_fr[q.bon] : ""))}) + '</span>' : "") +
      (etat.aide && q.erkl_fr ? '<span class="erkl">' + esc(q.erkl_fr) + '</span>' : "") +
      (etat.aide && q.mark_fr ? '<span class="dit"><img src="' + MARK_IMG + '" alt="">' + esc(q.mark_fr) + '</span>' : "") + '</div>';
  }
  if (etat.corrige && !q.beispiel){
    aide += '<div class="aide"><span class="petit">' + T("ta_reponse", {r: esc(libelle(q, rep))}) + '</span>' +
      (rep !== q.bon ? '<span class="verdict ok">' + T("bonne", {r: esc(libelle(q, q.bon))}) + '</span>' : '<span class="verdict ok">' + T("juste") + '</span>') +
      (q.frage_fr ? '<span class="trad">' + T("trad", {t: esc(q.frage_fr)}) + '</span>' : "") +
      (q.erkl_fr ? '<span class="erkl">' + esc(q.erkl_fr) + '</span>' : "") + '</div>';
  }
  const num = q.beispiel ? "0" : q.nr;
  return '<div class="q' + (q.beispiel ? " ex" : "") + '" id="q-' + q.id + '"><div class="tete"><span class="num">' + num + '</span><span class="frage" lang="de">' + esc(q.frage) + '</span></div>' + boutons + aide + '</div>';
}
// qui parle : le role donne par l'item (Frau Brandt, Beamter), sinon Mark, Sprecher ou Sprecherin -- jamais le nom de
// la voix, qui ne dit rien a l'eleve
const qui = (wer, rollen) => (rollen && rollen[wer]) || (wer === "mark" ? "Mark" : ((H.voix[wer] || {}).sexe === "m" ? "Sprecher" : "Sprecherin"));
function rendreTranscription(lignes, rollen){
  return '<div class="transcription" lang="de">' + lignes.map(l => '<div><span class="wer">' + esc(qui(l.wer, rollen)) + '</span><br>' + esc(l.text) + '</div>').join("") + '</div>';
}

function choisirTeil(part){
  DTZ.surRetour(null);
  $("titre").textContent = part === "H" ? T("ecouter_titre") + " · Hören" : T("lire_titre") + " · Lesen";
  const s0 = (part === "H" ? H : L).series[0];
  $("zone").innerHTML = '<div class="bloc"><h2>' + T("choisir_teil") + '</h2><div class="teils">' + TEILE[part].map(t => {
    const n = unites(part, s0, t).reduce((a, u) => a + u.questions.filter(q => !q.beispiel).length, 0);
    return '<button class="teil" data-t="' + t + '"><span>Teil ' + t.slice(1) + ' · ' + T(part + "_" + t) + '</span><small>' + T("questions", {n}) + '</small></button>';
  }).join("") + '</div></div>';
  document.querySelectorAll("[data-t]").forEach(b => b.onclick = () => entrainement(part, b.dataset.t));
  window.scrollTo(0, 0);
}

// ============ L'ENTRAINEMENT ============
// la serie : celle dont les mots cles de ce Teil sont le plus dus (choisirSerie() de commun.js)
const motsDuTeil = (part, teil) => s => [].concat(...unites(part, s, teil).map(u => [].concat(...u.questions.map(q => q.mots))));
let ENT = null;
async function entrainement(part, teil){
  silence(); EX = null;
  const s = await choisirSerie((part === "H" ? H : L).series, motsDuTeil(part, teil), part + teil);
  DTZ.surRetour(() => { silence(); choisirTeil(part); return true; });
  ENT = {part, teil, s, us: unites(part, s, teil), rang: 0, rep: {}, bons: 0, faits: 0};
  $("titre").textContent = "Teil " + teil.slice(1) + " · " + T(part + "_" + teil);
  montrerUnite();
}
function montrerUnite(){
  const e = ENT, u = e.us[e.rang];
  const fini = u.questions.every(q => q.beispiel || e.rep[q.id] !== undefined);
  let h = '<div class="bloc">';
  if (e.part === "H"){
    const consigne = e.rang === 0 ? H.consignes[e.teil] : null;
    if (consigne) h += '<p class="consigne"><span lang="de">' + esc(consigne.de) + '</span><span class="fr">' + esc(consigne.fr) + '</span></p>';
    if (e.teil === "T4"){
      h += rendreT4(u) + '<div class="lecteur"><button class="jouer" id="jouer">' + ICONE_SON + T("ecouter_btn") + '</button></div>';
      if (fini) h += rendreTranscription(u.intro.concat(...u.aussagen.map(a => a.audio)));
    } else {
      h += '<div class="lecteur"><button class="jouer" id="jouer">' + ICONE_SON + T(e.joue ? "reecouter" : "ecouter_btn") + '</button></div>';
      if (fini) h += '<p class="petit">' + T("transcription") + '</p>' + rendreTranscription(u.audio, u.rollen);
    }
  } else {
    if (e.rang === 0) h += '<p class="consigne" lang="de">' + esc(consigneLesen(e.s, e.teil)) + '</p>';
    if (u.situation) h += '<p class="consigne" lang="de">' + esc(u.situation) + '</p>';
    h += rendreDoc(u);
  }
  h += u.questions.map((q, i) => (e.part === "H" && e.teil === "T4" ? '<div class="lecteur"><button class="jouer" data-a="' + i + '">' + ICONE_SON + esc(q.beispiel ? T("exemple") : q.frage) + '</button></div>' : "") +
    rendreQuestion(q, {choisi: e.rep[q.id], montrer: e.rep[q.id] !== undefined, fige: e.rep[q.id] !== undefined, aide: true})).join("");
  h += '</div>';
  $("zone").innerHTML = h;
  // a l'entrainement, chaque personne du micro-trottoir se reecoute seule
  document.querySelectorAll("[data-a]").forEach(b => b.onclick = async () => { arreterSon(); debloquerSon(); b.disabled = true; const a = u.aussagen[+b.dataset.a]; await jouerPiste(a.cle, a.audio); b.disabled = false; });
  const jb = $("jouer");
  if (jb) jb.onclick = async () => {
    jb.disabled = true; jb.innerHTML = ICONE_SON + T("en_cours");
    silence(); debloquerSon();
    if (e.teil === "T4"){ await jouerPiste(u.cle, u.intro); for (const a of u.aussagen){ await attendre(1); await jouerPiste(a.cle, a.audio); } }
    else await jouerPiste(u.cle, u.audio);
    e.joue = true; jb.disabled = false; jb.innerHTML = ICONE_SON + T("reecouter");
  };
  document.querySelectorAll("#zone .opt:not(:disabled)").forEach(b => b.onclick = () => repondreEntrainement(b.dataset.q, b.dataset.v));
  const reste = e.rang < e.us.length - 1;
  $("suite").hidden = !fini;
  $("suite").textContent = reste ? T("suivant") : T("terminer");
  $("suite").onclick = () => { silence(); if (reste){ e.rang++; e.joue = false; montrerUnite(); window.scrollTo(0, 0); } else finEntrainement(); };
}
function repondreEntrainement(id, v){
  const e = ENT, u = e.us[e.rang], q = u.questions.find(x => x.id === id);
  const val = q.kind === "lettre" ? v : +v;
  e.rep[id] = val; e.faits++;
  const ok = val === q.bon; if (ok) e.bons++;
  parler("exercice", {juste: ok}); if (ok) parler("bonne");
  q.mots.forEach(m => parler("reponse", {mot: m.mot, genre: m.genre || null, cat: m.cat || null, juste: ok}));
  const y = window.scrollY; montrerUnite(); window.scrollTo(0, y);
  const el = $("q-" + id); if (el && el.getBoundingClientRect().bottom > innerHeight - 80) el.scrollIntoView({behavior: "smooth", block: "center"});
}
function finEntrainement(){
  const e = ENT; marquerFait(e.part + e.teil, e.s);
  DTZ.surRetour(() => { choisirTeil(e.part); return true; });
  parler("fini", {bons: e.bons, faits: e.faits});
  const r = e.faits ? e.bons / e.faits : 0;
  $("suite").hidden = true;
  $("zone").innerHTML = '<div class="bloc" style="align-items:center;text-align:center"><div class="score">' + e.bons + ' / ' + e.faits + '</div><p>' + T("fin_teil", {b: e.bons, n: e.faits}) + '</p>' +
    '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + T(r >= 0.75 ? "mark_bien" : r >= 0.5 ? "mark_moyen" : "mark_dur") + '</div></div>' +
    '<button class="secondaire" id="refaire" style="align-self:center">' + T("recommencer") + '</button><button class="secondaire" id="autre" style="align-self:center">' + T("accueil") + '</button></div>';
  $("refaire").onclick = () => entrainement(e.part, e.teil);
  $("autre").onclick = accueil;
  window.scrollTo(0, 0);
}


let EX = null;

function serieExamen(){
  // la prochaine serie d'examen pas encore faite ; toutes faites : on recommence par la plus ancienne
  const faits = lire("examens", {}), n = Math.min(SERIES_EXAMEN, H.series.length, L.series.length);
  let meilleur = 0;
  for (let i = 0; i < n; i++) if ((faits[H.series[i].id] || 0) < (faits[H.series[meilleur].id] || 0)) meilleur = i;
  return meilleur;
}
function lancerExamen(quoi){
  const i = serieExamen(); ENT = null; debloquerSon();   // dans le geste : iOS laissera ensuite jouer les pistes
  EX = {quoi, sH: H.series[i], sL: L.series[i], rep: {}, etape: null, teilL: "T1", fin: false};
  DTZ.surRetour(() => { if (!EX || EX.fin) return false; confirmer(T("quitter_q"), () => { silence(); EX = null; accueil(); }, T("quitter")); return true; });
  if (quoi === "L") examenLesen(); else examenHoeren();
}
function questionsDe(part, s){ return [].concat(...TEILE[part].map(t => [].concat(...unites(part, s, t).map(u => u.questions)))).filter(q => !q.beispiel); }
function brancherReponses(){
  document.querySelectorAll("#zone .opt:not(:disabled)").forEach(b => b.onclick = () => {
    const id = b.dataset.q, q = trouverQ(id);
    EX.rep[id] = q.kind === "lettre" ? b.dataset.v : +b.dataset.v;
    b.parentNode.querySelectorAll(".opt").forEach(x => x.classList.toggle("pris", x === b));
    if (id[0] === "L" && EX.teilL === "T5"){ const y = window.scrollY; afficherTeilLesen(); window.scrollTo(0, y); }   // le trou se remplit
  });
}
function trouverQ(id){ return questionsDe(id[0], id[0] === "H" ? EX.sH : EX.sL).find(q => q.id === id); }

// HOEREN : l'enregistrement deroule tout seul, comme le jour de l'examen. Chaque Teil s'affiche avec ses
// questions (la feuille de l'examen), la question qui passe est encadree, le son ne se rejoue pas.
async function examenHoeren(){
  const s = EX.sH, jeton = EX;
  $("titre").textContent = T("examen") + " · Hören";
  chrono(25 * 60, "haut");
  for (const teil of TEILE.H){
    if (EX !== jeton) return;
    const us = unitesHoeren(s, teil);
    afficherTeilHoeren(teil, us);
    await jouerPiste("consigne-" + teil, [{wer: "aurora", text: H.consignes[teil].de}]); await attendre(2);
    if (teil === "T4"){
      await attendre(60);                                      // une minute pour lire les phrases a-f
      if (EX !== jeton) return;
      await jouerPiste(us[0].cle, us[0].intro);
      for (const a of us[0].aussagen){
        if (EX !== jeton) return;
        marquer(a.q.id); await attendre(2); await jouerPiste(a.cle, a.audio); await attendre(a.q.beispiel ? 3 : 10);
      }
    } else {
      for (const u of us){
        if (EX !== jeton) return;
        const q0 = u.questions[0];
        marquer(q0.id);
        const annonce = q0.beispiel ? "Beispiel." : "Nummer " + u.questions.map(q => q.nr).join(" und ") + ".";
        await jouerPiste(q0.beispiel ? "beispiel" : "nummer-" + u.questions.map(q => q.nr).join("-"), [{wer: "aurora", text: annonce}]);
        await attendre(teil === "T3" ? 8 : 5);                  // le temps de lire la question
        await jouerPiste(u.cle, u.audio);
        await attendre(teil === "T3" ? 12 : 8);                 // le temps de repondre
      }
    }
  }
  if (EX !== jeton) return;
  await jouerPiste("consigne-ende", [{wer: "aurora", text: H.consignes.ende.de}]);
  marquer(null);
  if (EX.quoi === "HL") pauseAvantLesen(); else rendreCopie();
}
function afficherTeilHoeren(teil, us){
  let h = '<div class="bloc"><p class="ecoute"><i></i>' + T("joue") + '</p><h2>Teil ' + teil.slice(1) + '</h2><p class="consigne" lang="de">' + esc(H.consignes[teil].de) + '</p>';
  if (teil === "T4") h += rendreT4(us[0]);
  h += us.map(u => u.questions.map(q => rendreQuestion(q, {choisi: EX.rep[q.id]})).join("")).join("") + '</div>';
  h += '<button class="secondaire" id="voirFeuille">' + T("feuille") + '</button>';
  $("zone").innerHTML = h; brancherReponses(); $("voirFeuille").onclick = feuilleReponses;
  window.scrollTo(0, 0); $("suite").hidden = true;
}
function marquer(id){
  document.querySelectorAll(".q.joue").forEach(x => x.classList.remove("joue"));
  const el = id && $("q-" + id); if (el){ el.classList.add("joue"); el.scrollIntoView({behavior: "smooth", block: "start"}); }
}
function pauseAvantLesen(){
  arreterChrono(); silence();
  $("zone").innerHTML = '<div class="bloc" style="text-align:center;align-items:center"><p><b>' + T("hoeren_fin") + '</b></p><p>' + T("pause") + '</p></div>';
  chrono(5 * 60, "bas", examenLesen);
  $("suite").hidden = false; $("suite").textContent = T("pause_passer"); $("suite").onclick = examenLesen;
}

// LESEN : 45 minutes, les cinq Teile en onglets, dans l'ordre que l'on veut, comme sur le papier.
function examenLesen(){
  silence(); EX.etape = "L";
  $("titre").textContent = T("examen") + " · Lesen";
  chrono(45 * 60, "bas", () => rendreCopie());
  afficherTeilLesen();
}
function afficherTeilLesen(){
  const s = EX.sL, teil = EX.teilL;
  const nb = t => unitesLesen(s, t).reduce((a, u) => a + u.questions.filter(q => !q.beispiel && EX.rep[q.id] === undefined).length, 0);
  let h = '<div class="onglets">' + TEILE.L.map(t => '<button class="onglet' + (t === teil ? " actif" : "") + '" data-o="' + t + '">Teil ' + t.slice(1) + (nb(t) ? ' <span class="n">· ' + nb(t) + '</span>' : " ✓") + '</button>').join("") + '</div>';
  h += '<div class="bloc"><p class="consigne" lang="de">' + esc(consigneLesen(s, teil)) + '</p>';
  unitesLesen(s, teil).forEach(u => {
    if (u.situation) h += '<p class="consigne" lang="de">' + esc(u.situation) + '</p>';
    h += rendreDoc(u) + u.questions.map(q => rendreQuestion(q, {choisi: EX.rep[q.id]})).join("");
  });
  h += '</div><button class="secondaire" id="voirFeuille">' + T("feuille") + '</button>';
  $("zone").innerHTML = h; brancherReponses();
  document.querySelectorAll("[data-o]").forEach(b => b.onclick = () => { EX.teilL = b.dataset.o; afficherTeilLesen(); window.scrollTo(0, 0); });
  $("voirFeuille").onclick = feuilleReponses;
  const i = TEILE.L.indexOf(teil);
  $("suite").hidden = false;
  $("suite").textContent = i < 4 ? T("suivant") + " · Teil " + (i + 2) : T("rendre");
  $("suite").onclick = () => { if (i < 4){ EX.teilL = TEILE.L[i + 1]; afficherTeilLesen(); window.scrollTo(0, 0); } else confirmerRendre(); };
}
function confirmerRendre(){
  const vides = questionsDe("L", EX.sL).filter(q => EX.rep[q.id] === undefined).length;
  confirmer(T("rendre_q", {n: vides}), rendreCopie, T("oui_rendre"));
}

// LA FEUILLE DE REPONSES : la grille de l'examen, 1-20 et 1-25 ; toucher une case y mene.
function feuilleReponses(corrige){
  const parts = EX.quoi === "HL" ? ["H", "L"] : [EX.quoi];
  let h = '<h2>' + T("feuille") + '</h2>';
  parts.forEach(p => {
    const qs = questionsDe(p, p === "H" ? EX.sH : EX.sL);
    h += '<p class="petit">' + (p === "H" ? "Hören" : "Lesen") + '</p><div class="feuille">' + qs.map(q => {
      const v = EX.rep[q.id], val = v === undefined ? "–" : q.kind === "lettre" ? v : q.kind === "rf" ? (v === 0 ? "R" : "F") : ABC[v];
      const c = v === undefined ? " vide" : corrige === true ? (v === q.bon ? " juste" : " faux") : "";
      return '<button class="case' + c + '" data-aller="' + q.id + '">' + q.nr + '<span>' + val + '</span></button>';
    }).join("") + '</div>';
  });
  h += '<button class="secondaire" id="fermerF">' + T("fermer") + '</button>';
  ouvrir(h);
  $("fermerF").onclick = fermerPanneau;
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => {
    const id = b.dataset.aller; fermerPanneau();
    if (id[0] === "L" && EX.etape === "L" && !EX.fin){
      const t = TEILE.L.find(t => unitesLesen(EX.sL, t).some(u => u.questions.some(q => q.id === id)));
      if (t !== EX.teilL){ EX.teilL = t; afficherTeilLesen(); }
    }
    const el = $("q-" + id); if (el) el.scrollIntoView({behavior: "smooth", block: "center"});
  });
}


// LE VERDICT : Hoeren et Lesen ensemble, sur 45 ; A2 des 20, B1 des 33 (Pruefungshandbuch, ch. 1).
function rendreCopie(){
  silence(); arreterChrono(); EX.fin = true; DTZ.surRetour(null);
  const parts = EX.quoi === "HL" ? ["H", "L"] : [EX.quoi];
  const res = {};
  parts.forEach(p => {
    const s = p === "H" ? EX.sH : EX.sL;
    res[p] = {total: 0, bons: 0, teile: TEILE[p].map(t => {
      const qs = [].concat(...unites(p, s, t).map(u => u.questions)).filter(q => !q.beispiel);
      const b = qs.filter(q => EX.rep[q.id] === q.bon).length;
      return {t, b, n: qs.length};
    })};
    res[p].teile.forEach(x => { res[p].total += x.n; res[p].bons += x.b; });
  });
  const total = parts.reduce((a, p) => a + res[p].total, 0), bons = parts.reduce((a, p) => a + res[p].bons, 0);
  // une partie seule : la tendance, ramenee au bareme entier (45 au DTZ) pour la comparer aux seuils
  const sur45 = EX.quoi === "HL" ? bons : Math.round(bons * PROFIL.sur / total);
  const niv = niveauHL(sur45);
  const texte = bons + "/" + total + " → " + T("niv_" + niv);
  const faits = lire("examens", {}); faits[EX.sH.id] = Date.now(); ecrire("examens", faits);
  ecrire("dernier", {date: new Date().toLocaleDateString("fr-FR", {day: "numeric", month: "long"}), texte});
  if (EX.quoi === "HL") resultat("HL", {points: bons, niveau: niv, serie: EX.sH.id});
  parler("resultat", {mode: "examen", serie: EX.sH.id, hoeren: res.H ? res.H.bons : null, lesen: res.L ? res.L.bons : null, niveau: niv});
  parler("fini", {bons, faits: total});
  $("titre").textContent = T("verdict");
  const pct = v => Math.round(v * 100 / PROFIL.sur) + "%";
  let h = '<div class="bloc"><div class="score">' + bons + ' <span style="font-size:20px;color:var(--gris)">' + T("sur", {n: total}) + '</span></div>' +
    '<span class="niveau ' + niv + '">' + T("niv_" + niv) + '</span>';
  if (EX.quoi === "HL") h += '<div class="jauge"><i style="width:' + pct(bons) + '"></i><s style="left:' + pct(PROFIL.a2) + '"><em>A2 · ' + PROFIL.a2 + '</em></s><s style="left:' + pct(PROFIL.b1) + '"><em>B1 · ' + PROFIL.b1 + '</em></s></div>';
  h += '<p><b>' + (EX.quoi !== "HL" ? T("v_tendance", {n: T("niv_" + niv)}) : niv === "b1" ? T("v_b1") : niv === "a2" ? T("v_a2", {n: PROFIL.b1 - bons}) : T("v_moins", {n: PROFIL.a2 - bons})) + '</b></p>' +
    '<p class="petit">' + T(EX.quoi === "HL" ? "v_regle" : "v_seul") + '</p><div class="detail">';
  parts.forEach(p => res[p].teile.forEach(x => { h += '<span>' + (p === "H" ? "Hören" : "Lesen") + ' · Teil ' + x.t.slice(1) + ' · ' + T(p + "_" + x.t) + '</span><b>' + x.b + ' / ' + x.n + '</b>'; }));
  h += '</div><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + T("mark_v_" + niv) + '</div></div>' +
    '<button class="secondaire" id="corr">' + T("corrige") + '</button><button class="secondaire" id="feuilleC">' + T("feuille") + '</button></div>';
  $("zone").innerHTML = h;
  $("corr").onclick = corrige;
  $("feuilleC").onclick = () => feuilleReponses(true);
  $("suite").hidden = false; $("suite").textContent = T("accueil"); $("suite").onclick = accueil;
  window.scrollTo(0, 0);
}
function corrige(){
  const parts = EX.quoi === "HL" ? ["H", "L"] : [EX.quoi];
  let h = "";
  parts.forEach(p => {
    const s = p === "H" ? EX.sH : EX.sL;
    TEILE[p].forEach(t => {
      h += '<div class="bloc"><h2>' + (p === "H" ? "Hören" : "Lesen") + ' · Teil ' + t.slice(1) + '</h2>';
      unites(p, s, t).forEach(u => {
        if (p === "L") h += rendreDoc(u);
        if (p === "H" && t === "T4") h += rendreT4(u);
        h += u.questions.map(q => rendreQuestion(q, {choisi: EX.rep[q.id], montrer: true, fige: true, corrige: true})).join("");
        if (p === "H") h += rendreTranscription(t === "T4" ? u.intro.concat(...u.aussagen.map(a => a.audio)) : u.audio, u.rollen);
      });
      h += '</div>';
    });
  });
  $("zone").innerHTML = h; $("titre").textContent = T("corrige");
  $("suite").hidden = false; $("suite").textContent = T("accueil"); $("suite").onclick = accueil;
  window.scrollTo(0, 0);
}


// ============ LES INSCRIPTIONS ============
DTZ.partie({id: "H", ordre: 1, titre: T("ecouter_titre"), sous: T("hoeren_s"), ouvrir: () => choisirTeil("H")});
DTZ.partie({id: "L", ordre: 2, titre: T("lire_titre"), sous: T("lesen_s"), ouvrir: () => choisirTeil("L")});
DTZ.examen({id: "HL", ordre: 1, titre: T("ex_complet"), sous: T("ex_complet_s"), lancer: () => lancerExamen("HL")});
DTZ.examen({id: "H", ordre: 2, titre: T("ex_hoeren"), sous: T("ex_hoeren_s"), lancer: () => lancerExamen("H")});
DTZ.examen({id: "L", ordre: 3, titre: T("ex_lesen"), sous: T("ex_lesen_s"), lancer: () => lancerExamen("L")});
DTZ.charger(Promise.all([fetch("donnees/hoeren.json").then(r => r.json()), fetch("donnees/lesen.json").then(r => r.json())])
  .then(([h, l]) => { H = h; L = l; Object.assign(DTZ_VOIX, h.voix); }));
// les pistes enregistrees : facultatives -- sans manifeste, tout passe par la voix du telephone
DTZ.charger(fetch("donnees/voix-hoeren.json").then(r => r.ok ? r.json() : {}).catch(() => ({})).then(m => Object.assign(DTZ_PISTES, m)));
