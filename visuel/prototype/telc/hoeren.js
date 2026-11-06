// LE TELC A2·B1 AVEC MARK ET ANNA -- ECOUTER (HOEREN) ET ECOUTER ET NOTER (HOEREN UND SCHREIBEN)
// (6 nov. 2026, session « telc : Ecouter », decision de Jacques du 6 nov. : une session par epreuve).
//
// LE FORMAT DU TELC, JAMAIS SON CONTENU (preparation-examens/FORMAT-TELC.md) ; tous les textes sont les notres
// (donnees/hoeren.json, controle : python tests/telc_hoeren.py).
//   Hoeren, items 32-51, 20 x 3 = 60 points :
//     Teil 1  une conversation de tous les jours, 2 ecoutes, 30 s de lecture ; 5 associations a-i ;
//     Teil 2  une conversation au travail, 1 ecoute ; 5 richtig / falsch ;
//     Teil 3  5 annonces courtes, 2 ecoutes chacune ; 5 richtig / falsch ;
//     Teil 4  5 avis, 1 ecoute chacun ; 5 associations a-f (une de trop).
//   Hoeren und Schreiben, items 52-56 : 5 messages de repondeur, 2 ecoutes chacun, une note a completer ;
//     5 x 1 point, comptes dans l'ecrit (Schreiben).
//   Les deux ensemble : 35 minutes.
//
// DEUX PARTIES DANS L'ACCUEIL (DTZ.partie, tuiles « H » et « HS » du profil telc) et UN EXAMEN BLANC D'ECOUTE
// (DTZ.examen, « Ecouter, comme a l'examen »). L'organisation est celle des Sprachbausteine et de l'oral du DTZ
// (decision du 4 nov., « Meme organisation pour le futur bloc telc ») : une page par exercice (ici, par texte
// entendu), des points de progression qu'on touche pour sauter a une question, « Continuer » en bas, puis un
// recapitulatif (Refaire la section / Section suivante / Toutes les sections).
//
// A l'entrainement, le son s'entend le nombre de fois de l'examen (1 ou 2), apres le temps de lecture ; une fois
// toutes les questions de la page repondues, la correction, l'explication, la transcription, et le son se reecoute
// librement. A l'examen blanc, l'enregistrement deroule tout seul, avec ses pauses.
//
// L'INTERFACE : francais et anglais (?lang=en), les deux ici ; les autres langues retombent sur le francais.
// LA VOIX : celle du telephone, en attendant les voix enregistrees (ElevenLabs multilingual v2, sur accord de
// Jacques). Une replique qui recevra un fichier portera « mp3 » (chemin depuis cette page) : il sera joue a la
// place, sans rien changer d'autre. Les nombres : la voix recoit « dit », la lecture en lettres.
//
// Pour l'examen blanc complet du telc (assemble par la session des examens) : window.TELC_HOEREN.examen({fin})
// deroule Hoeren puis Hoeren und Schreiben et rend {hoeren: {bons, sur, points}, hs: {bons, sur}} a fin().
//
// Ce module ne connait de commun.js que ses fonctions publiques ($, esc, T, TXT, LANGUE, Q, RAPIDE, parler, lire,
// ecrire, dire, silence, attendre, chrono, arreterChrono, confirmer, choisirSerie, marquerFait, resultat, DTZ,
// DTZ_VOIX, HAUTEUR, accueil, MARK_IMG, ICONE_SON) ; il ne modifie pas commun.js.

"use strict";

const HO_EN = LANGUE === "en";
Object.assign(TXT, {
  ho_titre: "Écouter", ho_sous: "Hören · 4 parties · 20 questions",
  hs_titre: "Écouter et noter", hs_sous: "Hören und Schreiben · 5 messages",
  ho_section: "Section · Écouter · Teil {n}", hs_section: "Section · Écouter et noter",
  ho_T1: "Une conversation de tous les jours", ho_T2: "Une conversation au travail", ho_T3: "Des annonces courtes", ho_T4: "Des avis à la radio",
  ho_mark_debut: "À l'écoute du telc, il y a quatre parties et vingt questions. Certains textes passent deux fois, d'autres une seule : je te le dis à chaque fois. Ici, tu as la correction tout de suite, puis la transcription.",
  hs_mark_debut: "Cinq messages sur mon répondeur : prends la note à ma place. Un mot, une heure ou un nombre suffit, pas une phrase.",
  ho_fois_1: "À l'examen, on l'entend une seule fois.", ho_fois_2: "À l'examen, on l'entend deux fois.",
  ho_lecture: "{s} secondes pour lire d'abord.",
  ho_lire_avant: "Lis d'abord : {t}", ho_commencer: "Écouter maintenant",
  ho_ecouter: "Écouter", ho_ecoute_n: "Écouter · {n} sur {f}", ho_reecouter: "Réécouter", ho_en_cours: "Écoute…",
  ho_epuise: "Entendu {f} fois sur {f}, comme à l'examen. Réponds, puis la transcription s'affiche.",
  ho_juste: "Juste !", ho_faux: "Pas tout à fait : c'est « {r} ».",
  ho_presque: "Compté juste, mais attention à l'orthographe : « {r} ».",
  ho_transcription: "Ce qu'on entendait", ho_solutions: "Les solutions", ho_aussagen: "Les phrases",
  ho_situation: "La situation", ho_personne: "Person {n}", ho_extra: "de trop",
  ho_continuer: "Continuer", ho_verifier: "Vérifier", ho_ecris: "écris ici",
  ho_note: "La note",
  ho_recap: "Récapitulatif", ho_score: "{n} sur {t}",
  ho_points_h: "À l'examen, {n} × 3 = {p} points sur 60 en Écouter.",
  ho_seuils_h: "Au telc, chaque compétence compte sur 60 points. Le B1 demande 70 % (42 points : 14 bonnes réponses ici) dans trois compétences sur quatre, et au moins 40 % (24 points : 8 bonnes réponses) dans chacune. Le A2 demande 40 %.",
  ho_points_hs: "À l'examen, cela ferait {n} point(s) sur 5, comptés dans l'écrit (Schreiben).",
  ho_par_teil: "Teil {n}", ho_mark_bien: "Très bien ! Garde ce rythme : lire avant, écouter l'avis plutôt que les mots.",
  ho_mark_moyen: "Pas mal ! Relis les explications des questions ratées : ce sont souvent les mêmes pièges (une chose prévue qui ne se fait pas, un jour dit pour autre chose).",
  ho_mark_faible: "C'est le début, et l'écoute est la partie la plus dure. Relis les transcriptions, puis refais la section : tu entendras déjà mieux.",
  ho_refaire: "Refaire la section", ho_suivante: "Section suivante", ho_toutes: "Toutes les sections",
  ho_ex_titre: "Écouter, comme à l'examen", ho_ex_sous: "Hören puis Hören und Schreiben, 35 min : le son passe tout seul, une ou deux fois selon la partie.",
  ho_ex_regles: "Comme le jour de l'examen : le son passe tout seul, avec ses temps de lecture et ses pauses. Tu ne peux ni l'arrêter ni le rejouer. Réponds pendant l'écoute ; le corrigé vient à la fin.",
  ho_ex_lancer: "Commencer l'écoute",
  ho_ex_lecture: "Temps de lecture", ho_ex_joue: "Écoute en cours", ho_ex_pause: "Temps pour répondre", ho_ex_consigne: "Consigne",
  ho_ex_fin: "Fin de l'écoute", ho_ex_resultat: "Résultat de l'écoute",
  ho_v_b1: "B1 en Écouter : au moins 42 points sur 60.",
  ho_v_a2: "A2 en Écouter : au moins 24 points sur 60. Il manque {n} point(s) pour le B1.",
  ho_v_moins: "Sous le A2 : il manque {n} point(s) pour atteindre 24 sur 60.",
  ho_corrige: "Le corrigé", ho_ta_reponse: "Ta réponse : {r}", ho_sans_reponse: "pas de réponse", ho_bonne: "La bonne réponse : {r}",
  ho_voix_tel: "Voix du téléphone en attendant les voix enregistrées."
});
if (HO_EN) Object.assign(TXT, {
  ho_titre: "Listening", ho_sous: "Hören · 4 parts · 20 questions",
  hs_titre: "Listening and notes", hs_sous: "Hören und Schreiben · 5 messages",
  ho_section: "Section · Listening · Teil {n}", hs_section: "Section · Listening and notes",
  ho_T1: "An everyday conversation", ho_T2: "A conversation at work", ho_T3: "Short announcements", ho_T4: "Opinions on the radio",
  ho_mark_debut: "The telc listening test has four parts and twenty questions. Some texts are played twice, others only once: I'll tell you each time. Here you get the correction straight away, then the transcript.",
  hs_mark_debut: "Five messages on my voicemail: take the note for me. A word, a time or a number is enough, not a sentence.",
  ho_fois_1: "In the exam you hear it only once.", ho_fois_2: "In the exam you hear it twice.",
  ho_lecture: "{s} seconds to read first.",
  ho_lire_avant: "Read first: {t}", ho_commencer: "Listen now",
  ho_ecouter: "Listen", ho_ecoute_n: "Listen · {n} of {f}", ho_reecouter: "Listen again", ho_en_cours: "Playing…",
  ho_epuise: "Heard {f} times out of {f}, as in the exam. Answer, then the transcript appears.",
  ho_juste: "Correct!", ho_faux: "Not quite: it's “{r}”.",
  ho_presque: "Counted as correct, but watch the spelling: “{r}”.",
  ho_transcription: "What you heard", ho_solutions: "The solutions", ho_aussagen: "The statements",
  ho_situation: "The situation", ho_personne: "Person {n}", ho_extra: "left over",
  ho_continuer: "Continue", ho_verifier: "Check", ho_ecris: "write here",
  ho_note: "The note",
  ho_recap: "Summary", ho_score: "{n} out of {t}",
  ho_points_h: "In the exam: {n} × 3 = {p} points out of 60 in Listening.",
  ho_seuils_h: "In the telc, each skill counts for 60 points. B1 requires 70% (42 points: 14 correct answers here) in three skills out of four, and at least 40% (24 points: 8 correct answers) in each. A2 requires 40%.",
  ho_points_hs: "In the exam, that would be {n} point(s) out of 5, counted in Writing (Schreiben).",
  ho_par_teil: "Teil {n}", ho_mark_bien: "Very good! Keep it up: read first, and listen for the opinion rather than the words.",
  ho_mark_moyen: "Not bad! Reread the explanations for the questions you missed: the same traps keep coming back (something planned that doesn't happen, a day mentioned for something else).",
  ho_mark_faible: "It's early days, and listening is the hardest part. Reread the transcripts, then do the section again: you'll already hear more.",
  ho_refaire: "Do the section again", ho_suivante: "Next section", ho_toutes: "All sections",
  ho_ex_titre: "Listening, as in the exam", ho_ex_sous: "Hören then Hören und Schreiben, 35 min: the audio plays by itself, once or twice depending on the part.",
  ho_ex_regles: "As on exam day: the audio plays by itself, with its reading time and pauses. You can't stop it or replay it. Answer while you listen; the answers come at the end.",
  ho_ex_lancer: "Start listening",
  ho_ex_lecture: "Reading time", ho_ex_joue: "Playing", ho_ex_pause: "Time to answer", ho_ex_consigne: "Instructions",
  ho_ex_fin: "End of the listening test", ho_ex_resultat: "Listening result",
  ho_v_b1: "B1 in Listening: at least 42 points out of 60.",
  ho_v_a2: "A2 in Listening: at least 24 points out of 60. You need {n} more point(s) for B1.",
  ho_v_moins: "Below A2: you need {n} more point(s) to reach 24 out of 60.",
  ho_corrige: "The answers", ho_ta_reponse: "Your answer: {r}", ho_sans_reponse: "no answer", ho_bonne: "The right answer: {r}",
  ho_voix_tel: "Phone voice for now, until the recorded voices are ready.",
  quitter_q: "Quit the mock exam? It won't be counted.", quitter: "Quit", continuer: "Continue"
});
// la traduction d'un champ des donnees : « champ_en » en anglais (a defaut le francais), « champ_fr » sinon
const trad = (o, champ) => !o ? "" : (HO_EN && o[champ + "_en"]) || o[champ + "_fr"] || "";
const langueTrad = o => HO_EN ? (o.en || o.fr) : o.fr;
const deS = s => '<span lang="de" dir="ltr">' + esc(s) + '</span>';

// les voix de cette partie, au telephone : une hauteur par personne, pour qu'on entende qui parle
Object.assign(HAUTEUR, {anna: 1.06, brandt: 1.02, f_jung: 1.16, f_mittel: 1.0, f_alt: 0.9, m_jung: 1.04, m_mittel: 0.86, m_alt: 0.76, radio_f: 1.08, radio_m: 0.95});

// le style propre a cette partie (la note du repondeur, le bandeau du format) : ajoute ici plutot que dans
// telc.html, que les autres parties du telc modifient en meme temps
(() => { const st = document.createElement("style"); st.textContent =
  ".fmt{display:flex;flex-wrap:wrap;gap:6px}.fmt span{font-size:12px;font-weight:800;border-radius:999px;padding:4px 10px;background:var(--carte);color:var(--gris)}" +
  ".fmt span.fort{background:var(--encre);color:var(--verre)}" +
  ".notiz{direction:ltr;text-align:left;background:#FFF6C9;color:#1C2430;border-radius:4px;padding:14px 14px 12px;box-shadow:0 6px 14px rgba(0,0,0,.10);font-size:15px;line-height:1.7;transform:rotate(-.4deg)}" +
  "html.nuit .notiz{background:#3B3A26;color:#F2F0DC}" +
  ".notiz .t{font-weight:900;border-bottom:1px solid rgba(0,0,0,.18);padding-bottom:4px;margin-bottom:6px}" +
  ".notiz .num{font-weight:900;color:var(--ambre-f);margin-right:6px}" +
  ".notiz input{font:800 16px var(--police);color:inherit;background:rgba(255,255,255,.55);border:0;border-bottom:2px solid var(--ambre);border-radius:4px 4px 0 0;padding:2px 6px;width:9.5em;max-width:60%}" +
  "html.nuit .notiz input{background:rgba(0,0,0,.25)}" +
  ".notiz input.ok{border-color:var(--vert);color:var(--vert)}.notiz input.ko{border-color:var(--rouge);color:var(--rouge)}" +
  ".liste{direction:ltr;display:flex;flex-direction:column;gap:4px;background:var(--papier);border:1px solid var(--papier-trait);border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.4}" +
  ".liste div{display:flex;gap:8px}.liste b{min-width:16px;color:var(--ambre-f)}.liste i{font-size:12px;color:var(--gris);font-weight:600}" +
  ".liste .pris{opacity:.45}" +
  ".compte{font-size:22px;font-weight:900;font-variant-numeric:tabular-nums}" +
  ".ex-teil .q.joue{box-shadow:0 0 0 3px var(--ambre)}";
  document.head.appendChild(st); })();

const HO = {d: null, serie: null, us: [], page: 0, rep: {}, ecoutes: {}, jeton: 0, direct: !!Q.get("partie"),
            hs: null, saisie: {}, verif: {}};
let HO_AUDIO = null;

DTZ.charger(fetch("donnees/hoeren.json", {cache: "no-cache"})
  .then(r => { if (!r.ok) throw new Error("hoeren.json"); return r.json(); })
  .then(d => { HO.d = d; for (const k in d.voix) DTZ_VOIX[k] = {sexe: d.voix[k].sexe}; }));

DTZ.partie({id: "H", ordre: 40, titre: T("ho_titre"), sous: T("ho_sous"), ouvrir: () => ouvrirH()});
DTZ.partie({id: "HS", ordre: 50, titre: T("hs_titre"), sous: T("hs_sous"), ouvrir: () => ouvrirHS()});
DTZ.examen({id: "telcH", ordre: 40, titre: T("ho_ex_titre"), sous: T("ho_ex_sous"), lancer: () => examenEcoute()});

// ============ LE SON ============
// arreter : tout ce qui joue, et toute sequence en cours (le jeton change)
function stopSon(){ HO.jeton++; HO.enCours = null; silence(); if (HO_AUDIO){ try{ HO_AUDIO.pause(); }catch(e){} HO_AUDIO = null; } }
function jouerFichier(src){
  return new Promise(ok => {
    try{ const a = new Audio(src); HO_AUDIO = a; a.onended = () => ok(true); a.onerror = () => ok(false); a.play().catch(() => ok(false)); }
    catch(e){ ok(false); }
  });
}
async function direLigne(l){
  if (l.mp3 && await jouerFichier(l.mp3)) return;
  await dire(l.dit || l.text, l.wer);
}
// des segments (une liste de repliques chacun) separes par une pause ; faux si on a ete interrompu
async function jouerSegments(segs, pause, jeton){
  for (let k = 0; k < segs.length; k++){
    if (HO.jeton !== jeton) return false;
    if (k) await attendre(pause);
    for (const l of segs[k]){ if (HO.jeton !== jeton) return false; await direLigne(l); }
  }
  return HO.jeton === jeton;
}

// ============ LES UNITES DE HOEREN : ce qu'on entend d'un coup, et ses questions ============
function qLettre(nr, frage, lettres, bon, erkl, extra){ return Object.assign({nr, kind: "lettre", frage, lettres, bon, erkl}, extra || {}); }
function qRF(it){ return {nr: it.nr, kind: "rf", frage: it.aussage, bon: it.bon, trad: trad(it, "aussage"), erkl: trad(it, "erkl")}; }
function unitesH(s){
  const t1 = s.T1, t4 = s.T4, l1 = t1.loesungen.map(x => x.b), l4 = t4.saetze.map(x => x.b);
  return [
    {teil: "T1", fois: 2, lecture: 30, data: t1, rollen: t1.rollen, segs: [t1.audio],
     questions: t1.items.map(it => qLettre(it.nr, it.frage, l1, it.bon, trad(it, "erkl")))},
    {teil: "T2", fois: 1, lecture: 30, data: s.T2, rollen: s.T2.rollen, segs: [s.T2.audio], questions: s.T2.items.map(qRF)},
    ...s.T3.map((a, k) => ({teil: "T3", fois: 2, lecture: 0, data: a, rollen: a.rollen, segs: [a.audio], questions: [qRF(a)], rang: k})),
    {teil: "T4", fois: 1, lecture: 30, data: t4, rollen: Object.assign({}, t4.rollen), segs: [t4.intro].concat(t4.personen.map(p => p.audio)),
     noms: [null].concat(t4.personen.map(p => p.name)),
     questions: t4.personen.map((p, k) => qLettre(p.nr, T("ho_personne", {n: k + 1}), l4, p.bon, trad(p, "erkl")))}
  ];
}
const questionsH = us => [].concat(...us.map(u => u.questions));
const libelle = (q, v) => v === undefined || v === null ? T("ho_sans_reponse") : q.kind === "rf" ? (v ? "richtig" : "falsch") : v;

// ============ LE RENDU COMMUN ============
function bandeau(u){
  return '<div class="fmt"><span class="fort">' + esc(T(u.fois === 1 ? "ho_fois_1" : "ho_fois_2")) + '</span>' +
    (u.lecture ? '<span>' + esc(T("ho_lecture", {s: u.lecture})) + '</span>' : "") + '</div>';
}
function consigne(c){ return '<p class="consigne"><span lang="de">' + esc(c.de) + '</span><span class="fr">' + esc(langueTrad(c)) + '</span></p>'; }
function mark(texte){ return '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(texte) + '</div></div>'; }
// qui parle : le role donne par le texte, sinon Mark, Sprecher ou Sprecherin -- jamais le nom de la voix
function qui(wer, rollen){ return (rollen && rollen[wer]) || (wer === "mark" ? "Mark" : wer === "anna" ? "Anna" : ((HO.d.voix[wer] || {}).sexe === "m" ? "Sprecher" : "Sprecherin")); }
function transcription(u){
  const blocs = u.segs.map((seg, k) => {
    const nom = u.noms && u.noms[k];
    return (nom ? '<div><span class="wer">' + esc(T("ho_personne", {n: k}) + " · " + nom) + '</span></div>' : "") +
      seg.map(l => '<div><span class="wer">' + esc(nom || qui(l.wer, u.rollen)) + '</span><br>' + esc(l.text) + '</div>').join("");
  });
  return '<div class="transcription" lang="de">' + blocs.join("") + '</div>';
}
// la liste des solutions (Teil 1 : a-i ; Teil 4 : a-f), traduite une fois la page faite
function liste(lignes, fini, utilisees){
  return '<div class="liste">' + lignes.map(x => '<div' + (fini && utilisees && !utilisees.includes(x.b) ? ' class="pris"' : "") + '><b>' + x.b + '</b><span><span lang="de">' + esc(x.de) + '</span>' +
    (fini ? '<br><i>' + esc(langueTrad(x)) + (utilisees && !utilisees.includes(x.b) ? " · " + esc(T("ho_extra")) : "") + '</i>' : "") + '</span></div>').join("") + '</div>';
}
// une question : ses boutons ; etat = {choisi, montrer (correction et explication), fige}
function carte(q, etat){
  const ch = etat.choisi, valeurs = q.kind === "rf" ? [true, false] : q.lettres;
  const boutons = '<div class="choix ligne">' + valeurs.map(v => {
    let c = "opt";
    if (etat.montrer){ if (v === q.bon) c += " juste"; else if (v === ch) c += " faux"; }
    else if (v === ch) c += " pris";
    return '<button class="' + c + '" data-nr="' + q.nr + '" data-v="' + v + '"' + (etat.fige ? " disabled" : "") + '>' +
      (q.kind === "rf" ? '<span lang="de">' + (v ? "richtig" : "falsch") + '</span>' : '<b>' + v + '</b>') + '</button>';
  }).join("") + '</div>';
  let aide = "";
  if (etat.montrer){
    const ok = ch === q.bon;
    aide = '<div class="aide">' + (etat.corrige ? '<span class="petit">' + esc(T("ho_ta_reponse", {r: libelle(q, ch)})) + '</span>' : "") +
      '<span class="verdict ' + (ok ? "ok" : "ko") + '">' + esc(ok ? T("ho_juste") : T("ho_faux", {r: libelle(q, q.bon)})) + '</span>' +
      (q.trad ? '<span class="trad">' + esc(q.trad) + '</span>' : "") +
      (q.erkl ? '<div class="dit"><img src="' + MARK_IMG + '" alt=""><span class="erkl">' + esc(q.erkl) + '</span></div>' : "") + '</div>';
  }
  return '<div class="q" id="q' + q.nr + '"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage" lang="de">' + esc(q.frage) + '</span></div>' + boutons + aide + '</div>';
}
function pointsDe(qs, ici, etatDe){
  return '<div class="points">' + qs.map(q => {
    const e = etatDe(q);
    return '<button class="point' + (e === true ? " ok" : e === false ? " ko" : "") + (ici.includes(q.nr) ? " ici" : "") + '" data-aller="' + q.nr + '" aria-label="' + q.nr + '">' + q.nr + '</button>';
  }).join("") + '</div>';
}
function toutesLesSections(){
  stopSon(); arreterChrono();
  if (HO.direct){ parler("fermer"); if (window.parent === window) accueil(); return; }
  accueil();
}
function partieSuivante(id){ const o = DTZ.parties, k = o.findIndex(p => p.id === id); return k >= 0 && k + 1 < o.length ? o[k + 1] : null; }

// le lecteur d'une page d'entrainement : le temps de lecture, puis le son autant de fois qu'a l'examen ; libre
// une fois la page faite
function lecteur(cle, u, fini, rendre){
  const n = HO.ecoutes[cle] || 0, peut = fini || n < u.fois;
  let h = '<div class="lecteur" id="lecteur">';
  if (HO.enCours === cle) h += '<div class="ecoute"><i></i>' + esc(T("ho_en_cours")) + '</div>';
  else if (!peut) h += '<p class="petit">' + esc(T("ho_epuise", {f: u.fois})) + '</p>';
  else h += '<button class="jouer" id="jouer">' + ICONE_SON + esc(fini ? T("ho_reecouter") : T("ho_ecoute_n", {n: n + 1, f: u.fois})) + '</button>';
  h += '</div>';
  const brancher = () => {
    const b = $("jouer"); if (!b) return;
    b.onclick = async () => {
      stopSon(); const jeton = HO.jeton;
      if (!fini && n === 0 && u.lecture && !RAPIDE){
        // le temps de lecture de l'examen, qu'on peut passer
        let reste = u.lecture;
        $("lecteur").innerHTML = '<span class="compte" id="compte">0:' + String(reste).padStart(2, "0") + '</span><button class="secondaire" id="passer">' + esc(T("ho_commencer")) + '</button>';
        await new Promise(ok => {
          const id = setInterval(() => { reste--; const c = $("compte"); if (c) c.textContent = "0:" + String(Math.max(0, reste)).padStart(2, "0"); if (reste <= 0 || HO.jeton !== jeton){ clearInterval(id); ok(); } }, 1000);
          $("passer").onclick = () => { clearInterval(id); ok(); };
        });
        if (HO.jeton !== jeton) return;
      }
      $("lecteur").innerHTML = '<div class="ecoute"><i></i>' + esc(T("ho_en_cours")) + '</div>';
      HO.enCours = cle;
      const fin = await jouerSegments(u.segs, 1.2, jeton);
      if (!fin) return;
      HO.enCours = null;
      if (!fini) HO.ecoutes[cle] = (HO.ecoutes[cle] || 0) + 1;
      rendre(true);
    };
  };
  return {h, brancher};
}

// ============ HOEREN, L'ENTRAINEMENT ============
async function ouvrirH(serie){
  stopSon(); arreterChrono();
  const d = HO.d;
  HO.serie = serie || await choisirSerie(d.hoeren, () => [], "H");
  HO.us = unitesH(HO.serie); HO.page = 0; HO.rep = {}; HO.ecoutes = {};
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  pageH();
}
function pageH(garderScroll){
  const u = HO.us[HO.page], qs = questionsH(HO.us), d = HO.d;
  const fini = u.questions.every(q => HO.rep[q.nr] !== undefined);
  const premiere = HO.us.findIndex(x => x.teil === u.teil) === HO.page;
  const n = u.teil.slice(1);
  $("titre").textContent = T("ho_titre") + " · Teil " + n;
  let h = '<div class="bloc"><div class="section">' + esc(T("ho_section", {n})) + ' · ' + esc(T("ho_" + u.teil)) + '</div>' +
    pointsDe(qs, u.questions.map(q => q.nr), q => HO.rep[q.nr] === undefined ? null : HO.rep[q.nr] === q.bon) + '</div>';
  if (HO.page === 0 && !Object.keys(HO.rep).length) h += '<div class="bloc">' + mark(T("ho_mark_debut")) + '</div>';
  h += '<div class="bloc">';
  if (premiere) h += consigne(d.consignes[u.teil]) + mark(langueTrad(d.conseils[u.teil]));
  h += bandeau(u);
  if (u.teil === "T1" || u.teil === "T2") h += '<p class="petit"><b>' + esc(T("ho_situation")) + ' :</b> ' + esc(trad(u.data, "situation")) + '</p>';
  if (u.teil === "T3") h += '<p class="petit" lang="de">' + esc(u.data.typ) + '</p>';
  if (u.teil === "T1") h += '<p class="consigne" lang="de">' + esc(u.data.frage) + (fini ? '<span class="fr">' + esc(trad(u.data, "frage")) + '</span>' : "") + '</p>' +
    '<p class="petit">' + esc(T("ho_solutions")) + '</p>' + liste(u.data.loesungen, fini, u.questions.map(q => q.bon));
  if (u.teil === "T4") h += '<p class="consigne" lang="de">' + esc(u.data.thema) + (fini ? '<span class="fr">' + esc(trad(u.data, "thema")) + '</span>' : "") + '</p>' +
    '<p class="petit">' + esc(T("ho_aussagen")) + '</p>' + liste(u.data.saetze, fini, u.questions.map(q => q.bon));
  const lec = lecteur("H" + HO.page, u, fini, () => pageH(true));
  h += lec.h;
  h += u.questions.map(q => carte(q, {choisi: HO.rep[q.nr], montrer: HO.rep[q.nr] !== undefined, fige: HO.rep[q.nr] !== undefined})).join("");
  if (fini) h += '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + transcription(u);
  h += '</div><p class="petit" style="text-align:center">' + esc(T("ho_voix_tel")) + '</p>';
  const y = window.scrollY;
  $("zone").innerHTML = h;
  lec.brancher();
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { stopSon(); const nr = +b.dataset.aller; HO.page = HO.us.findIndex(x => x.questions.some(q => q.nr === nr)); pageH(); const el = $("q" + nr); if (el) setTimeout(() => el.scrollIntoView({block: "center"}), 30); });
  document.querySelectorAll("#zone .opt:not(:disabled)").forEach(b => b.onclick = () => repondreH(+b.dataset.nr, b.dataset.v));
  const suite = $("suite");
  suite.hidden = !fini; suite.textContent = T("ho_continuer");
  suite.onclick = () => { stopSon(); const reste = HO.us.findIndex((x, k) => k > HO.page && x.questions.some(q => HO.rep[q.nr] === undefined));
    const avant = HO.us.findIndex(x => x.questions.some(q => HO.rep[q.nr] === undefined));
    if (reste >= 0 || avant >= 0){ HO.page = reste >= 0 ? reste : avant; pageH(); window.scrollTo(0, 0); } else recapH(); };
  if (garderScroll) window.scrollTo(0, y); else window.scrollTo(0, 0);
}
function repondreH(nr, v){
  if (HO.rep[nr] !== undefined) return;
  const q = questionsH(HO.us).find(x => x.nr === nr);
  HO.rep[nr] = q.kind === "rf" ? v === "true" : v;
  const ok = HO.rep[nr] === q.bon;
  parler("exercice", {juste: ok}); if (ok) parler("bonne");
  const u = HO.us[HO.page];
  // la page finie : le son s'arrete, la transcription s'affiche
  if (u.questions.every(x => HO.rep[x.nr] !== undefined)) stopSon();
  pageH(true);
  const el = $("q" + nr); if (el && el.getBoundingClientRect().bottom > innerHeight - 80) el.scrollIntoView({behavior: "smooth", block: "center"});
}
function bilanH(us, rep){
  const parTeil = {};
  for (const u of us) for (const q of u.questions){ const t = parTeil[u.teil] || (parTeil[u.teil] = {b: 0, t: 0}); t.t++; if (rep[q.nr] === q.bon) t.b++; }
  const bons = Object.values(parTeil).reduce((a, t) => a + t.b, 0);
  return {bons, sur: 20, points: bons * 3, parTeil};
}
function detailTeils(parTeil){
  return '<div class="detail">' + Object.keys(parTeil).map(t => '<span>' + esc(T("ho_par_teil", {n: t.slice(1)})) + ' · ' + esc(T("ho_" + t)) + '</span><b>' + parTeil[t].b + ' / ' + parTeil[t].t + '</b>').join("") + '</div>';
}
function recapH(){
  stopSon(); $("suite").hidden = true;
  const s = HO.serie, b = bilanH(HO.us, HO.rep);
  marquerFait("H", s);
  resultat("H", {serie: s.id, bons: b.bons, sur: 20, points: b.points});
  parler("fini", {bons: b.bons, faits: 20});
  const mot = b.bons >= 14 ? "ho_mark_bien" : b.bons >= 8 ? "ho_mark_moyen" : "ho_mark_faible";
  const lignes = HO.us.map(u => u.questions.map(q => ({q, u, ok: HO.rep[q.nr] === q.bon}))).flat();
  const ligne = x => carte(x.q, {choisi: HO.rep[x.q.nr], montrer: true, fige: true});
  const suivante = partieSuivante("H");
  $("titre").textContent = T("ho_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("ho_titre")) + ' · ' + esc(T("ho_recap")) + '</div>' +
      '<div class="score">' + esc(T("ho_score", {n: b.bons, t: 20})) + '</div>' +
      '<p class="petit" style="text-align:center">' + esc(T("ho_points_h", {n: b.bons, p: b.points})) + '</p>' +
      detailTeils(b.parTeil) + mark(T(mot)) + '<p class="petit">' + esc(T("ho_seuils_h")) + '</p></div>' +
    '<div class="bloc">' + lignes.filter(x => !x.ok).concat(lignes.filter(x => x.ok)).map(ligne).join("") + '</div>' +
    '<div class="bloc boutons">' +
      '<button class="secondaire" id="hoRefaire">' + esc(T("ho_refaire")) + '</button>' +
      (suivante ? '<button class="secondaire" id="hoSuivante">' + esc(T("ho_suivante")) + ' : ' + esc(suivante.titre) + '</button>' : "") +
      '<button class="secondaire" id="hoToutes">' + esc(T("ho_toutes")) + '</button></div>';
  $("hoRefaire").onclick = () => ouvrirH(s);
  if (suivante) $("hoSuivante").onclick = () => suivante.ouvrir();
  $("hoToutes").onclick = toutesLesSections;
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  window.scrollTo(0, 0);
}

// ============ HOEREN UND SCHREIBEN : LA NOTE ============
// La saisie est comparee selon le type : une heure (9:30, 9.30, 9 Uhr 30, halb zehn…), un nombre ou un numero
// (les chiffres seuls), un mot (sans majuscules, ae = ä, sans article). Pour un mot qui n'est pas epele, une lettre
// de travers compte encore, avec un avertissement : la regle exacte du telc sur l'orthographe des notes n'est pas
// dans FORMAT-TELC.md (a verifier dans le manuel). Un nom epele (exakt) doit etre exact.
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
function unitesHS(s){ return s.nachrichten.map(m => ({teil: "HS", fois: 2, lecture: 10, data: m, rollen: m.rollen, segs: [m.audio], questions: [{nr: m.nr}]})); }
// la note : ses lignes, la case a remplir a la place de {}
function rendreNotiz(m, valeur, etat, fige){
  const champ = '<input type="text" id="saisie' + m.nr + '" data-nr="' + m.nr + '" autocomplete="off" autocapitalize="off" spellcheck="false" lang="de" placeholder="' + esc(T("ho_ecris")) + '"' +
    ' value="' + esc(valeur || "") + '"' + (fige ? " disabled" : "") + (etat ? ' class="' + (noteOk(etat) ? "ok" : "ko") + '"' : "") + '>';
  return '<div class="notiz" lang="de"><div class="t"><span class="num">' + m.nr + '</span>' + esc(m.notiz.titel) + '</div>' +
    m.notiz.zeilen.map(z => '<div>' + (z.includes("{}") ? esc(z).replace("{}", champ) : esc(z)) + '</div>').join("") + '</div>';
}
function aideNote(m, valeur, etat, corrige){
  return '<div class="aide">' + (corrige ? '<span class="petit">' + esc(T("ho_ta_reponse", {r: valeur || T("ho_sans_reponse")})) + '</span>' : "") +
    '<span class="verdict ' + (noteOk(etat) ? "ok" : "ko") + '">' + esc(etat === "juste" ? T("ho_juste") : etat === "presque" ? T("ho_presque", {r: m.loesung}) : T("ho_faux", {r: m.loesung})) + '</span>' +
    '<div class="dit"><img src="' + MARK_IMG + '" alt=""><span class="erkl">' + esc(trad(m, "erkl")) + '</span></div></div>';
}
async function ouvrirHS(serie){
  stopSon(); arreterChrono();
  HO.hs = serie || await choisirSerie(HO.d.notizen, () => [], "HS");
  HO.us = unitesHS(HO.hs); HO.page = 0; HO.saisie = {}; HO.verif = {}; HO.ecoutes = {};
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  pageHS();
}
function pageHS(garderScroll){
  const u = HO.us[HO.page], m = u.data, d = HO.d, etat = HO.verif[m.nr], fini = !!etat;
  $("titre").textContent = T("hs_titre");
  let h = '<div class="bloc"><div class="section">' + esc(T("hs_section")) + '</div>' +
    pointsDe(HO.us.map(x => x.questions[0]), [m.nr], q => HO.verif[q.nr] ? noteOk(HO.verif[q.nr]) : null) + '</div>';
  if (HO.page === 0 && !Object.keys(HO.verif).length) h += '<div class="bloc">' + mark(T("hs_mark_debut")) + '</div>';
  h += '<div class="bloc">';
  if (HO.page === 0) h += consigne(d.consignes.HS) + mark(langueTrad(d.conseils.HS));
  h += bandeau(u);
  h += '<p class="petit">' + esc(T("ho_note")) + '</p>' + rendreNotiz(m, HO.saisie[m.nr], etat, fini);
  const lec = lecteur("HS" + HO.page, u, fini, () => pageHS(true));
  h += lec.h;
  if (fini) h += aideNote(m, HO.saisie[m.nr], etat) + '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + transcription(u);
  h += '</div><p class="petit" style="text-align:center">' + esc(T("ho_voix_tel")) + '</p>';
  const y = window.scrollY;
  $("zone").innerHTML = h;
  lec.brancher();
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { stopSon(); HO.page = HO.us.findIndex(x => x.data.nr === +b.dataset.aller); pageHS(); });
  const champ = $("saisie" + m.nr), suite = $("suite");
  const majSuite = () => { suite.hidden = !fini && !(HO.saisie[m.nr] || "").trim(); };
  if (champ && !fini){
    champ.oninput = () => { HO.saisie[m.nr] = champ.value; majSuite(); };
    champ.onkeydown = ev => { if (ev.key === "Enter" && champ.value.trim()) verifierHS(); };
  }
  suite.textContent = fini ? T("ho_continuer") : T("ho_verifier");
  majSuite();
  suite.onclick = () => {
    if (!fini){ verifierHS(); return; }
    stopSon();
    const reste = HO.us.findIndex((x, k) => k > HO.page && !HO.verif[x.data.nr]), avant = HO.us.findIndex(x => !HO.verif[x.data.nr]);
    if (reste >= 0 || avant >= 0){ HO.page = reste >= 0 ? reste : avant; pageHS(); } else recapHS();
  };
  if (garderScroll) window.scrollTo(0, y); else window.scrollTo(0, 0);
}
function verifierHS(){
  const m = HO.us[HO.page].data;
  const etat = verifierNote(m, HO.saisie[m.nr]);
  HO.verif[m.nr] = etat; stopSon();
  parler("exercice", {juste: noteOk(etat)}); if (noteOk(etat)) parler("bonne");
  pageHS(true);
}
function recapHS(){
  stopSon(); $("suite").hidden = true;
  const s = HO.hs, ms = s.nachrichten, bons = ms.filter(m => noteOk(HO.verif[m.nr])).length;
  marquerFait("HS", s);
  resultat("HS", {serie: s.id, bons, sur: 5});
  parler("fini", {bons, faits: 5});
  const mot = bons >= 4 ? "ho_mark_bien" : bons >= 3 ? "ho_mark_moyen" : "ho_mark_faible";
  const ligne = m => '<div class="q">' + rendreNotiz(m, HO.saisie[m.nr], HO.verif[m.nr], true) + aideNote(m, HO.saisie[m.nr], HO.verif[m.nr]) + '</div>';
  const rates = ms.filter(m => !noteOk(HO.verif[m.nr])), justes = ms.filter(m => noteOk(HO.verif[m.nr]));
  const suivante = partieSuivante("HS");
  $("titre").textContent = T("hs_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("hs_titre")) + ' · ' + esc(T("ho_recap")) + '</div>' +
      '<div class="score">' + esc(T("ho_score", {n: bons, t: 5})) + '</div>' +
      '<p class="petit" style="text-align:center">' + esc(T("ho_points_hs", {n: bons})) + '</p>' + mark(T(mot)) + '</div>' +
    '<div class="bloc">' + rates.concat(justes).map(ligne).join("") + '</div>' +
    '<div class="bloc boutons">' +
      '<button class="secondaire" id="hsRefaire">' + esc(T("ho_refaire")) + '</button>' +
      (suivante ? '<button class="secondaire" id="hsSuivante">' + esc(T("ho_suivante")) + ' : ' + esc(suivante.titre) + '</button>' : "") +
      '<button class="secondaire" id="hsToutes">' + esc(T("ho_toutes")) + '</button></div>';
  $("hsRefaire").onclick = () => ouvrirHS(s);
  if (suivante) $("hsSuivante").onclick = () => suivante.ouvrir();
  $("hsToutes").onclick = toutesLesSections;
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  window.scrollTo(0, 0);
}

// ============ L'EXAMEN BLANC D'ECOUTE ============
// Hoeren puis Hoeren und Schreiben, comme l'enregistrement de l'examen : chaque Teil s'affiche avec toutes ses
// questions, la consigne est dite, le temps de lecture passe, le son joue le nombre de fois du format, la question
// en cours est encadree. Pas de correction avant la fin. Les pauses autres que les 30 s de Teil 1 sont les notres.
let HX = null;
async function examenEcoute(opts){
  stopSon();
  opts = opts || {};
  const d = HO.d;
  const sH = opts.serieH || await choisirSerie(d.hoeren, () => [], "XH");
  const sHS = opts.serieHS || await choisirSerie(d.notizen, () => [], "XHS");
  HX = {sH, sHS, us: unitesH(sH), ms: unitesHS(sHS), rep: {}, saisie: {}, fin: opts.fin || null, fini: false};
  DTZ.surRetour(() => { if (!HX || HX.fini) return false; confirmer(T("quitter_q"), () => { stopSon(); arreterChrono(); HX = null; accueil(); }, T("quitter")); return true; });
  $("titre").textContent = T("ho_ex_titre"); $("suite").hidden = true;
  $("zone").innerHTML = '<div class="bloc">' + mark(T("ho_ex_regles")) + '<div class="fmt">' +
    ["T1", "T2", "T3", "T4"].map(t => '<span>Teil ' + t.slice(1) + ' · ' + esc(T("ho_" + t)) + '</span>').join("") + '<span>' + esc(T("hs_titre")) + '</span></div></div>';
  $("suite").hidden = false; $("suite").textContent = T("ho_ex_lancer");
  $("suite").onclick = () => { $("suite").hidden = true; deroulerExamen(); };
  window.scrollTo(0, 0);
}
function etatExamen(texte, joue){
  const e = $("exEtat"); if (e) e.innerHTML = (joue ? '<i></i>' : "") + esc(texte);
}
function marquerEx(nrs){ document.querySelectorAll("#zone .q").forEach(x => x.classList.toggle("joue", nrs.includes(+x.id.slice(1)))); const el = $("q" + nrs[0]); if (el) el.scrollIntoView({behavior: "smooth", block: "center"}); }
function feuilleTeil(teil){
  const us = HX.us.filter(u => u.teil === teil), u0 = us[0];
  let h = '<div class="bloc ex-teil"><div class="section">Teil ' + teil.slice(1) + ' · ' + esc(T("ho_" + teil)) + '</div><div class="ecoute" id="exEtat"></div>' + bandeau(u0);
  h += '<p class="consigne" lang="de">' + esc(HO.d.consignes[teil].de) + '</p>';
  if (teil === "T1") h += '<p class="consigne" lang="de">' + esc(u0.data.frage) + '</p>' + liste(u0.data.loesungen, false);
  if (teil === "T4") h += '<p class="consigne" lang="de">' + esc(u0.data.thema) + '</p>' + liste(u0.data.saetze, false);
  h += us.map(u => u.questions.map(q => carte(q, {choisi: HX.rep[q.nr], montrer: false, fige: false})).join("")).join("") + '</div>';
  $("zone").innerHTML = h;
  document.querySelectorAll("#zone .opt").forEach(b => b.onclick = () => {
    const nr = +b.dataset.nr, q = questionsH(HX.us).find(x => x.nr === nr);
    HX.rep[nr] = q.kind === "rf" ? b.dataset.v === "true" : b.dataset.v;
    b.parentNode.querySelectorAll(".opt").forEach(x => x.classList.toggle("pris", x === b));
  });
  window.scrollTo(0, 0);
}
function feuilleHS(){
  let h = '<div class="bloc ex-teil"><div class="section">' + esc(T("hs_titre")) + ' · Hören und Schreiben</div><div class="ecoute" id="exEtat"></div>' + bandeau(HX.ms[0]) +
    '<p class="consigne" lang="de">' + esc(HO.d.consignes.HS.de) + '</p>' +
    HX.ms.map(u => '<div class="q" id="q' + u.data.nr + '">' + rendreNotiz(u.data, HX.saisie[u.data.nr], null, false) + '</div>').join("") + '</div>';
  $("zone").innerHTML = h;
  document.querySelectorAll("#zone input[data-nr]").forEach(c => c.oninput = () => { HX.saisie[+c.dataset.nr] = c.value; });
  window.scrollTo(0, 0);
}
async function deroulerExamen(){
  const jeton = ++HO.jeton, vivant = () => HX && HO.jeton === jeton, d = HO.d;
  chrono(35 * 60, "haut");
  const pause = async (s, texte) => { etatExamen(texte); await attendre(s); return vivant(); };
  const ecouter = async (segs, nrs) => { if (nrs) marquerEx(nrs); etatExamen(T("ho_ex_joue"), true); return await jouerSegments(segs, 1.2, jeton) && vivant(); };
  const consigneDite = async c => { etatExamen(T("ho_ex_consigne"), true); await direLigne({wer: c.wer, text: c.de, dit: c.dit}); return vivant(); };
  for (const teil of ["T1", "T2", "T3", "T4"]){
    if (!vivant()) return;
    feuilleTeil(teil);
    const us = HX.us.filter(u => u.teil === teil), u0 = us[0];
    if (!await consigneDite(d.consignes[teil])) return;
    if (u0.lecture && !await pause(u0.lecture, T("ho_ex_lecture"))) return;
    if (teil === "T1"){
      const nrs = u0.questions.map(q => q.nr);
      if (!await ecouter(u0.segs, nrs) || !await pause(10, T("ho_ex_pause")) || !await ecouter(u0.segs, nrs) || !await pause(15, T("ho_ex_pause"))) return;
    } else if (teil === "T2"){
      if (!await ecouter(u0.segs, u0.questions.map(q => q.nr)) || !await pause(20, T("ho_ex_pause"))) return;
    } else if (teil === "T3"){
      for (const u of us){
        const nr = u.questions[0].nr;
        marquerEx([nr]); await direLigne({wer: "aurora", text: "Nummer " + nr + ".", dit: "Nummer " + nr + "."});
        if (!await pause(5, T("ho_ex_lecture")) || !await ecouter(u.segs, [nr]) || !await pause(4, T("ho_ex_pause")) || !await ecouter(u.segs, [nr]) || !await pause(8, T("ho_ex_pause"))) return;
      }
    } else {
      if (!await ecouter([u0.segs[0]])) return;
      for (let k = 1; k < u0.segs.length; k++){
        const nr = u0.questions[k - 1].nr;
        if (!await pause(2, "") || !await ecouter([u0.segs[k]], [nr]) || !await pause(10, T("ho_ex_pause"))) return;
      }
    }
  }
  if (!vivant()) return;
  feuilleHS();
  if (!await consigneDite(d.consignes.HS)) return;
  for (const u of HX.ms){
    const nr = u.data.nr;
    marquerEx([nr]); const c = $("saisie" + nr); if (c) c.focus({preventScroll: true});
    if (!await pause(u.lecture, T("ho_ex_lecture")) || !await ecouter(u.segs, [nr]) || !await pause(5, T("ho_ex_pause")) || !await ecouter(u.segs, [nr]) || !await pause(15, T("ho_ex_pause"))) return;
  }
  await direLigne({wer: d.consignes.ende.wer, text: d.consignes.ende.de});
  if (!vivant()) return;
  finExamen();
}
function finExamen(){
  arreterChrono(); HX.fini = true;
  const bH = bilanH(HX.us, HX.rep);
  const etats = {}; HX.ms.forEach(u => { etats[u.data.nr] = verifierNote(u.data, HX.saisie[u.data.nr]); });
  const bHS = HX.ms.filter(u => noteOk(etats[u.data.nr])).length;
  const res = {hoeren: {serie: HX.sH.id, bons: bH.bons, sur: 20, points: bH.points}, hs: {serie: HX.sHS.id, bons: bHS, sur: 5}};
  resultat("H", Object.assign({examen: true}, res.hoeren)); resultat("HS", Object.assign({examen: true}, res.hs));
  marquerFait("XH", HX.sH); marquerFait("XHS", HX.sHS);
  if (HX.fin){ const f = HX.fin; f(res); return; }
  const p = bH.points, niv = p >= 42 ? "b1" : p >= 24 ? "a2" : "moins";
  const verdict = niv === "b1" ? T("ho_v_b1") : niv === "a2" ? T("ho_v_a2", {n: 42 - p}) : T("ho_v_moins", {n: 24 - p});
  const corrH = ["T1", "T2", "T3", "T4"].map(t => {
    const us = HX.us.filter(u => u.teil === t);
    return '<div class="bloc"><div class="section">Teil ' + t.slice(1) + ' · ' + esc(T("ho_" + t)) + '</div>' +
      (t === "T1" ? liste(us[0].data.loesungen, true, us[0].questions.map(q => q.bon)) : t === "T4" ? liste(us[0].data.saetze, true, us[0].questions.map(q => q.bon)) : "") +
      us.map(u => u.questions.map(q => carte(q, {choisi: HX.rep[q.nr], montrer: true, fige: true, corrige: true})).join("") +
        '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + transcription(u)).join("") + '</div>';
  }).join("");
  const corrHS = '<div class="bloc"><div class="section">' + esc(T("hs_titre")) + '</div>' +
    HX.ms.map(u => '<div class="q">' + rendreNotiz(u.data, HX.saisie[u.data.nr], etats[u.data.nr], true) + aideNote(u.data, HX.saisie[u.data.nr], etats[u.data.nr], true) + '</div>' + transcription(u)).join("") + '</div>';
  const der = new Date();
  ecrire("dernier", {date: der.toLocaleDateString(LANGUE), texte: T("ho_ex_titre") + " · " + p + " / 60"});
  $("titre").textContent = T("ho_ex_resultat");
  $("zone").innerHTML =
    '<div class="bloc" style="align-items:center;text-align:center"><div class="section">' + esc(T("ho_ex_fin")) + '</div>' +
      '<div class="score">' + p + ' / 60</div><span class="niveau ' + niv + '">' + esc(T("niv_" + niv)) + '</span>' +
      '<div class="jauge" style="align-self:stretch"><i style="width:' + Math.round(p / 60 * 100) + '%"></i><s style="left:40%"><em>A2 · 24</em></s><s style="left:70%"><em>B1 · 42</em></s></div>' +
      '<p>' + esc(verdict) + '</p>' + detailTeils(bH.parTeil) +
      '<p class="petit">' + esc(T("ho_points_hs", {n: bHS})) + '</p>' +
      '<p class="petit">' + esc(T("ho_seuils_h")) + '</p></div>' +
    '<div class="bloc"><h2>' + esc(T("ho_corrige")) + '</h2></div>' + corrH + corrHS +
    '<div class="bloc boutons"><button class="secondaire" id="exAccueil">' + esc(T("ho_toutes")) + '</button></div>';
  $("exAccueil").onclick = toutesLesSections;
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  window.scrollTo(0, 0);
}

window.TELC_HOEREN = {examen: examenEcoute, ouvrirHoeren: ouvrirH, ouvrirNotizen: ouvrirHS, verifierNote};
