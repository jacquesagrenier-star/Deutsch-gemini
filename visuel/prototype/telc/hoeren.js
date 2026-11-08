// LE TELC A2·B1 AVEC MARK ET ANNA -- ECOUTER (HOEREN), items 32-51
// (6 nov. 2026, session « telc : Ecouter », decision de Jacques du 6 nov. : une session par epreuve).
//
// LE FORMAT DU TELC, JAMAIS SON CONTENU (preparation-examens/FORMAT-TELC.md) ; tous les textes sont les notres
// (donnees/hoeren.json ; controle : python tests/telc_ecouter.py ; relecture : outils/relecture_ecouter.py).
//   Teil 1  une conversation de tous les jours, 2 ecoutes, 30 s de lecture ; 5 associations a-i ;
//   Teil 2  une conversation au travail, 1 ecoute ; 5 richtig / falsch ;
//   Teil 3  5 annonces courtes, 2 ecoutes chacune ; 5 richtig / falsch ;
//   Teil 4  5 avis, 1 ecoute chacun ; 5 associations a-f (une de trop).
//   20 items x 3 = 60 points de Hoeren. Avec Hoeren und Schreiben (hoeren-schreiben.js) : 35 minutes.
//
// Ce que demandait Marina, l'enseignante (journal des retours, 1er nov.) : le cahier du commerce « n'explique pas le
// format ». La partie s'ouvre donc sur « L'ecoute du telc, en bref » (les parties, combien de fois on entend, le
// temps, les points, comment s'y prendre), que le lien « Le format » de chaque page rouvre.
//
// L'ORGANISATION est celle des Sprachbausteine (TELC-ASSEMBLAGE.md) : une page par texte entendu, des points de
// progression, « Continuer » en bas, un recapitulatif (Refaire / Section suivante / Toutes les sections). A
// l'entrainement, le son s'entend le nombre de fois de l'examen, apres le temps de lecture ; une fois la page
// repondue, la correction, l'explication, la transcription, et le son se reecoute librement. A l'examen blanc
// (TELC.epreuve, sur: {Hoeren: 60}), l'enregistrement deroule tout seul, avec ses pauses.
//
// LA VOIX : les pistes enregistrees de commun.js (DTZ_PISTES, manifeste donnees/voix-ecouter.json, facultatif),
// sinon la voix du telephone ; les nombres : la voix du telephone recoit « dit », la lecture en lettres.
//
// TOUT EST DANS UNE FONCTION : les modules du telc partagent la page, et une fonction globale du meme nom qu'une
// autre (toutesLesSections, carte, jouerFichier…) remplacerait la sienne sans un mot. Ce qui sert aussi a
// hoeren-schreiben.js passe par window.TELC_ECOUTE.

(function(){
"use strict";

const H_EN = {
  ho_titre: "Listening", ho_sous: "Hören · 4 parts · 20 questions",
  ho_section: "Section · Listening · Teil {n}",
  ho_T1: "An everyday conversation", ho_T2: "A conversation at work", ho_T3: "Short announcements", ho_T4: "Opinions on the radio",
  ho_HS: "Voicemail messages to note down",
  ho_format: "The format", ho_format_titre: "The telc listening test, in brief",
  ho_format_intro: "It comes after Reading and the Sprachbausteine and lasts about 35 minutes in all. The recording plays by itself: you can't stop it or replay it. You answer on the sheet while you listen.",
  ho_col_pts: "points", ho_une_fois: "heard once", ho_deux_fois: "heard twice",
  ho_lire_s: "{s} s to read first", ho_t_assoc: "match a–{l}", ho_t_rf: "richtig / falsch", ho_t_note: "write a note",
  ho_points_tot: "Listening counts for 60 of the 240 points (25 %). The 5 notes count in Writing.",
  ho_methode_titre: "How to go about it",
  ho_methode: ["Use the reading time: read the questions and guess what you'll need to catch.", "Heard twice: note what you recognise the first time, check the second time.", "Heard once: decide straight away, then move on to the next question.", "Listen for the meaning, not just the words: something planned that doesn't happen, a day mentioned for something else, an opinion that says the opposite of the word you hear."],
  ho_commencer_section: "Start Teil 1",
  ho_mark_debut: "Here is how the listening works. In practice you get the correction straight away, then the transcript — and you hear each text as many times as in the exam.",
  ho_fois_1: "In the exam you hear it only once.", ho_fois_2: "In the exam you hear it twice.",
  ho_lecture: "{s} seconds to read first.",
  ho_commencer: "Listen now",
  ho_ecoute_n: "Listen · {n} of {f}", ho_reecouter: "Listen again", ho_en_cours: "Playing…",
  ho_epuise: "Heard {f} time(s) out of {f}, as in the exam. Answer, then the transcript appears.",
  ho_juste: "Correct!", ho_faux: "Not quite: it's “{r}”.",
  ho_transcription: "What you heard", ho_solutions: "The solutions", ho_aussagen: "The statements",
  ho_situation: "The situation", ho_personne: "Person {n}", ho_extra: "left over",
  ho_continuer: "Continue",
  ho_recap: "Summary", ho_score: "{n} out of {t}",
  ho_points_h: "In the exam: {n} × 3 = {p} points out of 60 in Listening.",
  ho_seuils_h: "In the telc, each skill counts for 60 points. B1 requires 70 % (42 points: 14 correct answers here) in three skills out of four, and at least 40 % (24 points: 8 correct answers) in each. A2 requires 40 %.",
  ho_par_teil: "Teil {n}", ho_mark_bien: "Very good! Keep it up: read first, and listen for the opinion rather than the words.",
  ho_mark_moyen: "Not bad! Reread the explanations for the questions you missed: the same traps keep coming back (something planned that doesn't happen, a day mentioned for something else).",
  ho_mark_faible: "It's early days, and listening is the hardest part. Reread the transcripts, then do the section again: you'll already hear more.",
  ho_refaire: "Do the section again", ho_suivante: "Next section", ho_toutes: "All sections",
  ho_ex_lecture: "Reading time", ho_ex_joue: "Playing", ho_ex_pause: "Time to answer", ho_ex_consigne: "Instructions",
  ho_ta_reponse: "Your answer: {r}", ho_sans_reponse: "no answer",
  ho_voix_tel: "Phone voice for now, until the recorded voices are ready."
};
textesTelc({ en: H_EN, fr: {
  ho_titre: "Écouter", ho_sous: "Hören · 4 parties · 20 questions",
  ho_section: "Section · Écouter · Teil {n}",
  ho_T1: "Une conversation de tous les jours", ho_T2: "Une conversation au travail", ho_T3: "Des annonces courtes", ho_T4: "Des avis à la radio",
  ho_HS: "Des messages de répondeur à noter",
  ho_format: "Le format", ho_format_titre: "L'écoute du telc, en bref",
  ho_format_intro: "Elle vient après la lecture et les Sprachbausteine et dure environ 35 minutes en tout. L'enregistrement passe tout seul : on ne peut ni l'arrêter ni le rejouer. On répond sur la feuille pendant l'écoute.",
  ho_col_pts: "points", ho_une_fois: "entendu 1 fois", ho_deux_fois: "entendu 2 fois",
  ho_lire_s: "{s} s pour lire d'abord", ho_t_assoc: "associer a–{l}", ho_t_rf: "richtig / falsch", ho_t_note: "noter",
  ho_points_tot: "L'écoute compte pour 60 des 240 points (25 %). Les 5 notes comptent dans l'écrit.",
  ho_methode_titre: "Comment s'y prendre",
  ho_methode: ["Profite du temps de lecture : lis les questions, devine ce qu'il faudra attraper.", "Entendu deux fois : à la première écoute, note ce que tu reconnais ; à la seconde, vérifie.", "Entendu une seule fois : décide tout de suite, puis passe à la question suivante.", "Écoute le sens, pas seulement les mots : une chose prévue qui ne se fait pas, un jour dit pour autre chose, un avis qui dit le contraire du mot qu'on entend."],
  ho_commencer_section: "Commencer le Teil 1",
  ho_mark_debut: "Voici comment se passe l'écoute. À l'entraînement, tu as la correction tout de suite, puis la transcription — et tu entends chaque texte autant de fois qu'à l'examen.",
  ho_fois_1: "À l'examen, on l'entend une seule fois.", ho_fois_2: "À l'examen, on l'entend deux fois.",
  ho_lecture: "{s} secondes pour lire d'abord.",
  ho_commencer: "Écouter maintenant",
  ho_ecoute_n: "Écouter · {n} sur {f}", ho_reecouter: "Réécouter", ho_en_cours: "Écoute…",
  ho_epuise: "Entendu {f} fois sur {f}, comme à l'examen. Réponds, puis la transcription s'affiche.",
  ho_juste: "Juste !", ho_faux: "Pas tout à fait : c'est « {r} ».",
  ho_transcription: "Ce qu'on entendait", ho_solutions: "Les solutions", ho_aussagen: "Les phrases",
  ho_situation: "La situation", ho_personne: "Person {n}", ho_extra: "de trop",
  ho_continuer: "Continuer",
  ho_recap: "Récapitulatif", ho_score: "{n} sur {t}",
  ho_points_h: "À l'examen, {n} × 3 = {p} points sur 60 en Écouter.",
  ho_seuils_h: "Au telc, chaque compétence compte sur 60 points. Le B1 demande 70 % (42 points : 14 bonnes réponses ici) dans trois compétences sur quatre, et au moins 40 % (24 points : 8 bonnes réponses) dans chacune. Le A2 demande 40 %.",
  ho_par_teil: "Teil {n}", ho_mark_bien: "Très bien ! Garde ce rythme : lire avant, écouter l'avis plutôt que les mots.",
  ho_mark_moyen: "Pas mal ! Relis les explications des questions ratées : ce sont souvent les mêmes pièges (une chose prévue qui ne se fait pas, un jour dit pour autre chose).",
  ho_mark_faible: "C'est le début, et l'écoute est la partie la plus dure. Relis les transcriptions, puis refais la section : tu entendras déjà mieux.",
  ho_refaire: "Refaire la section", ho_suivante: "Section suivante", ho_toutes: "Toutes les sections",
  ho_ex_lecture: "Temps de lecture", ho_ex_joue: "Écoute en cours", ho_ex_pause: "Temps pour répondre", ho_ex_consigne: "Consigne",
  ho_ta_reponse: "Ta réponse : {r}", ho_sans_reponse: "pas de réponse",
  ho_voix_tel: "Voix du téléphone en attendant les voix enregistrées."
}});
// une liste de textes (la methode) : TXT garde le tableau tel quel
const listeTxt = cle => Array.isArray(TXT[cle]) ? TXT[cle] : [];

// les voix de cette partie, au telephone : une hauteur par personne, pour qu'on entende qui parle
Object.assign(HAUTEUR, {anna: 1.06, brandt: 1.02, f_jung: 1.16, f_mittel: 1.0, f_alt: 0.9, m_jung: 1.04, m_mittel: 0.86, m_alt: 0.76, radio_f: 1.08, radio_m: 0.95});

// le style propre a l'ecoute (la note du repondeur, le bandeau et le tableau du format) : ajoute ici, telc.html et
// commun.css appartenant a l'assemblage
(() => { const st = document.createElement("style"); st.textContent =
  ".fmt{display:flex;flex-wrap:wrap;gap:6px}.fmt span{font-size:12px;font-weight:800;border-radius:999px;padding:4px 10px;background:var(--carte);color:var(--gris)}" +
  ".fmt span.fort{background:var(--encre);color:var(--verre)}" +
  ".fmtt{display:flex;flex-direction:column;gap:6px}" +
  ".fmtt .l{display:grid;grid-template-columns:1fr auto;gap:2px 10px;background:var(--carte);border-radius:12px;padding:8px 10px;font-size:13px;font-weight:700;color:var(--gris)}" +
  ".fmtt .l b{color:var(--encre);font-size:14px;font-weight:900}.fmtt .l em{font-style:normal;font-weight:900;color:var(--ambre-f);text-align:right}" +
  ".fmtt .l .une{color:var(--rouge);font-weight:900;text-align:right}.fmtt .l .deux{text-align:right}.fmtt .l.ici{box-shadow:0 0 0 2px var(--ambre)}" +
  ".methode{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:6px;font-weight:700;line-height:1.45;font-size:14px}" +
  ".lien{border:0;background:none;color:var(--bleu);font:800 13px var(--police);cursor:pointer;padding:0;align-self:flex-start;text-decoration:underline}" +
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
  ".compte{font-size:22px;font-weight:900;font-variant-numeric:tabular-nums}";
  document.head.appendChild(st); })();

// ============ LES DONNEES ============
const E = { d: null, jeton: 0, enCours: null, ecoutes: {} };
const H = { serie: null, us: [], page: 0, rep: {} };
DTZ.charger(fetch("donnees/hoeren.json", {cache: "no-cache"})
  .then(r => { if (!r.ok) throw new Error("hoeren.json"); return r.json(); })
  .then(d => { E.d = d; for (const k in d.voix) DTZ_VOIX[k] = {sexe: d.voix[k].sexe}; }));
// les pistes enregistrees : facultatives -- sans manifeste, tout passe par la voix du telephone
DTZ.charger(fetch("donnees/voix-ecouter.json", {cache: "no-cache"}).then(r => r.ok ? r.json() : {}).catch(() => ({})).then(m => Object.assign(DTZ_PISTES, m)));

DTZ.partie({id: "H", ordre: 40, titre: T("ho_titre"), sous: T("ho_sous"), ouvrir: () => ouvrirH()});
TELC.epreuve({id: "H", ordre: 40, minutes: 35, sur: {Hoeren: 60}, lancer: fini => examenH(fini)});

// ============ LE SON ============
// arreter : tout ce qui joue (silence() de commun.js arrete la voix ET le lecteur), et toute sequence en cours
function stopSon(){ E.jeton++; E.enCours = null; silence(); }
async function direLigne(l){ await dire(l.dit || l.text, l.wer); }
// des segments (les repliques d'une piste chacun), separes par une pause ; une piste enregistree remplace son segment
// (cles[k] dans DTZ_PISTES) ; faux si on a ete interrompu
async function jouerSegments(segs, cles, pause, jeton){
  for (let k = 0; k < segs.length; k++){
    if (E.jeton !== jeton) return false;
    if (k) await attendre(pause);
    const f = cles && DTZ_PISTES[cles[k]];
    if (f && !RAPIDE && await jouerFichier(BASE_PISTES + f)) continue;
    for (const l of segs[k]){ if (E.jeton !== jeton) return false; await direLigne(l); }
  }
  return E.jeton === jeton;
}

// ============ LES UNITES : ce qu'on entend d'un coup, et ses questions ============
// textes : {lettre: texte allemand de la solution}, pour que la correction dise « h · Spiele … » et pas « h » seul
function qLettre(nr, frage, lettres, bon, erkl, textes){ return {nr, kind: "lettre", frage, lettres, bon, erkl, textes}; }
function qRF(it){ return {nr: it.nr, kind: "rf", frage: it.aussage, bon: it.bon, trad: champTelc(it, "aussage"), erkl: champTelc(it, "erkl")}; }
function unitesH(s){
  const t1 = s.T1, t4 = s.T4, l1 = t1.loesungen.map(x => x.b), l4 = t4.saetze.map(x => x.b), c = "telcH" + s.id + "-";
  const x1 = {}, x4 = {}; t1.loesungen.forEach(x => { x1[x.b] = x.text; }); t4.saetze.forEach(x => { x4[x.b] = x.text; });
  return [
    {teil: "T1", fois: 2, lecture: 30, data: t1, rollen: t1.rollen, segs: [t1.audio], cles: [c + "T1"],
     questions: t1.items.map(it => qLettre(it.nr, it.frage, l1, it.bon, champTelc(it, "erkl"), x1))},
    {teil: "T2", fois: 1, lecture: 30, data: s.T2, rollen: s.T2.rollen, segs: [s.T2.audio], cles: [c + "T2"], questions: s.T2.items.map(qRF)},
    ...s.T3.map(a => ({teil: "T3", fois: 2, lecture: 0, data: a, rollen: a.rollen, segs: [a.audio], cles: [c + a.nr], questions: [qRF(a)]})),
    {teil: "T4", fois: 1, lecture: 30, data: t4, rollen: Object.assign({}, t4.rollen), segs: [t4.intro].concat(t4.personen.map(p => p.audio)),
     cles: [c + "T4-intro"].concat(t4.personen.map(p => c + p.nr)), noms: [null].concat(t4.personen.map(p => p.name)),
     questions: t4.personen.map((p, k) => qLettre(p.nr, T("ho_personne", {n: k + 1}), l4, p.bon, champTelc(p, "erkl"), x4))}
  ];
}
const questionsDe = us => [].concat(...us.map(u => u.questions));
const libelle = (q, v) => v === undefined || v === null ? T("ho_sans_reponse") : q.kind === "rf" ? (v ? "richtig" : "falsch") : v + (q.textes && q.textes[v] ? " · " + q.textes[v] : "");

// ============ LE RENDU COMMUN (aussi pour hoeren-schreiben.js) ============
function bandeau(u){
  return '<div class="fmt"><span class="fort">' + esc(T(u.fois === 1 ? "ho_fois_1" : "ho_fois_2")) + '</span>' +
    (u.lecture ? '<span>' + esc(T("ho_lecture", {s: u.lecture})) + '</span>' : "") + '</div>';
}
function consigne(c){ return '<p class="consigne"><span lang="de">' + esc(c.text) + '</span><span class="fr">' + esc(champTelc(c, "text")) + '</span></p>'; }
function mark(texte){ return '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(texte) + '</div></div>'; }
// qui parle : le role donne par le texte, sinon Mark, Anna, Sprecher ou Sprecherin -- jamais le nom de la voix
function qui(wer, rollen){ return (rollen && rollen[wer]) || (wer === "mark" ? "Mark" : wer === "anna" ? "Anna" : ((E.d.voix[wer] || {}).sexe === "m" ? "Sprecher" : "Sprecherin")); }
function transcription(u){
  const blocs = u.segs.map((seg, k) => {
    const nom = u.noms && u.noms[k];
    return (nom ? '<div><span class="wer">' + esc(T("ho_personne", {n: k}) + " · " + nom) + '</span></div>' : "") +
      seg.map(l => '<div><span class="wer">' + esc(nom || qui(l.wer, u.rollen)) + '</span><br>' + esc(l.text) + '</div>').join("");
  });
  return '<div class="transcription" lang="de">' + blocs.join("") + '</div>';
}
// L'ECOUTE DU TELC, EN BREF (le retour de Marina) : les cinq parties, puis la methode ; ici = la partie en cours
function tableauFormat(ici){
  const lignes = [
    {id: "T1", nrs: "32–36", fois: 2, lire: 30, type: T("ho_t_assoc", {l: "i"}), pts: 15},
    {id: "T2", nrs: "37–41", fois: 1, lire: 30, type: T("ho_t_rf"), pts: 15},
    {id: "T3", nrs: "42–46", fois: 2, lire: 0, type: T("ho_t_rf"), pts: 15},
    {id: "T4", nrs: "47–51", fois: 1, lire: 30, type: T("ho_t_assoc", {l: "f"}), pts: 15},
    {id: "HS", nrs: "52–56", fois: 2, lire: 0, type: T("ho_t_note"), pts: 5}
  ];
  return '<div class="fmtt">' + lignes.map(l =>
    '<div class="l' + (l.id === ici ? " ici" : "") + '"><b>' + (l.id === "HS" ? "Hören und Schreiben" : "Teil " + l.id.slice(1)) + ' · ' + esc(T("ho_" + l.id)) + '</b><em>' + l.pts + ' ' + esc(T("ho_col_pts")) + '</em>' +
    '<span>' + l.nrs + ' · ' + esc(l.type) + (l.lire ? ' · ' + esc(T("ho_lire_s", {s: l.lire})) : "") + '</span>' +
    '<span class="' + (l.fois === 1 ? "une" : "deux") + '">' + esc(T(l.fois === 1 ? "ho_une_fois" : "ho_deux_fois")) + '</span></div>').join("") + '</div>';
}
function blocFormat(ici){
  return '<h2>' + esc(T("ho_format_titre")) + '</h2><p class="petit">' + esc(T("ho_format_intro")) + '</p>' + tableauFormat(ici) +
    '<p class="petit">' + esc(T("ho_points_tot")) + '</p><h2>' + esc(T("ho_methode_titre")) + '</h2>' +
    '<ul class="methode">' + listeTxt("ho_methode").map(x => '<li>' + esc(x) + '</li>').join("") + '</ul>';
}
function montrerFormat(ici){ ouvrir(blocFormat(ici) + '<button class="secondaire" id="fermerFmt">' + esc(T("fermer")) + '</button>'); $("fermerFmt").onclick = fermerPanneau; }
// la liste des solutions (Teil 1 : a-i ; Teil 4 : a-f), traduite une fois la page faite
function listeSolutions(lignes, fini, utilisees){
  return '<div class="liste">' + lignes.map(x => '<div' + (fini && utilisees && !utilisees.includes(x.b) ? ' class="pris"' : "") + '><b>' + x.b + '</b><span><span lang="de">' + esc(x.text) + '</span>' +
    (fini ? '<br><i>' + esc(champTelc(x, "text")) + (utilisees && !utilisees.includes(x.b) ? " · " + esc(T("ho_extra")) : "") + '</i>' : "") + '</span></div>').join("") + '</div>';
}
// une question : ses boutons ; etat = {choisi, montrer (correction et explication), fige, corrige}
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
  stopSon(); arreterChrono(); fermerPanneau();
  if (TELC.direct){ parler("fermer"); if (window.parent === window) accueil(); return; }
  accueil();
}
function partieSuivante(id){ const o = DTZ.parties, k = o.findIndex(p => p.id === id); return k >= 0 && k + 1 < o.length ? o[k + 1] : null; }
// Refaire / Section suivante / Toutes les sections, en bas d'un recapitulatif
function boutonsFin(id, refaire){
  const suivante = partieSuivante(id);
  return {h: '<div class="bloc boutons"><button class="secondaire" id="fRefaire">' + esc(T("ho_refaire")) + '</button>' +
      (suivante ? '<button class="secondaire" id="fSuivante">' + esc(T("ho_suivante")) + DEUX_POINTS_TELC + esc(suivante.titre) + '</button>' : "") +
      '<button class="secondaire" id="fToutes">' + esc(T("ho_toutes")) + '</button></div>',
    brancher(){ $("fRefaire").onclick = refaire; if (suivante) $("fSuivante").onclick = () => suivante.ouvrir(); $("fToutes").onclick = toutesLesSections;
      DTZ.surRetour(() => { toutesLesSections(); return true; }); }};
}

// le lecteur d'une page d'entrainement : le temps de lecture, puis le son autant de fois qu'a l'examen ; libre
// une fois la page faite. rendre() redessine la page.
function lecteur(cle, u, fini, rendre){
  const n = E.ecoutes[cle] || 0, peut = fini || n < u.fois;
  let h = '<div class="lecteur" id="lecteur">';
  if (E.enCours === cle) h += '<div class="ecoute"><i></i>' + esc(T("ho_en_cours")) + '</div>';
  else if (!peut) h += '<p class="petit">' + esc(T("ho_epuise", {f: u.fois})) + '</p>';
  else h += '<button class="jouer" id="jouer">' + ICONE_SON + esc(fini ? T("ho_reecouter") : T("ho_ecoute_n", {n: n + 1, f: u.fois})) + '</button>';
  h += '</div>';
  const brancher = () => {
    const b = $("jouer"); if (!b) return;
    b.onclick = async () => {
      debloquerSon();   // dans le geste : iOS laissera ensuite jouer les pistes
      stopSon(); const jeton = E.jeton;
      if (!fini && n === 0 && u.lecture && !RAPIDE){
        // le temps de lecture de l'examen, qu'on peut passer
        let reste = u.lecture;
        $("lecteur").innerHTML = '<span class="compte" id="compte">0:' + String(reste).padStart(2, "0") + '</span><button class="secondaire" id="passer">' + esc(T("ho_commencer")) + '</button>';
        await new Promise(ok => {
          const id = setInterval(() => { reste--; const c = $("compte"); if (c) c.textContent = "0:" + String(Math.max(0, reste)).padStart(2, "0"); if (reste <= 0 || E.jeton !== jeton){ clearInterval(id); ok(); } }, 1000);
          $("passer").onclick = () => { clearInterval(id); ok(); };
        });
        if (E.jeton !== jeton) return;
      }
      E.enCours = cle;
      $("lecteur").innerHTML = '<div class="ecoute"><i></i>' + esc(T("ho_en_cours")) + '</div>';
      const fin = await jouerSegments(u.segs, u.cles, 1.2, jeton);
      if (!fin) return;
      E.enCours = null;
      if (!fini) E.ecoutes[cle] = (E.ecoutes[cle] || 0) + 1;
      rendre(true);
    };
  };
  return {h, brancher};
}

// ============ L'ENTRAINEMENT ============
async function ouvrirH(serie){
  stopSon(); arreterChrono();
  H.serie = serie || await choisirSerie(E.d.series, () => [], "H");
  H.us = unitesH(H.serie); H.page = 0; H.rep = {}; E.ecoutes = {};
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  // en entrant, le format d'abord ; « Refaire la section » va droit au Teil 1
  if (serie) pageH(); else introH();
}
function introH(){
  $("titre").textContent = T("ho_titre");
  $("zone").innerHTML = '<div class="bloc">' + mark(T("ho_mark_debut")) + '</div><div class="bloc">' + blocFormat("T1") + '</div>';
  const suite = $("suite"); suite.hidden = false; suite.textContent = T("ho_commencer_section");
  suite.onclick = () => pageH();
  window.scrollTo(0, 0);
}
function pageH(garderScroll){
  const u = H.us[H.page], qs = questionsDe(H.us), d = E.d;
  const fini = u.questions.every(q => H.rep[q.nr] !== undefined);
  const premiere = H.us.findIndex(x => x.teil === u.teil) === H.page;
  const n = u.teil.slice(1);
  $("titre").textContent = T("ho_titre") + " · Teil " + n;
  let h = '<div class="bloc"><div class="section">' + esc(T("ho_section", {n})) + ' · ' + esc(T("ho_" + u.teil)) + '</div>' +
    pointsDe(qs, u.questions.map(q => q.nr), q => H.rep[q.nr] === undefined ? null : H.rep[q.nr] === q.bon) +
    '<button class="lien" id="voirFmt">' + esc(T("ho_format")) + '</button></div>';
  h += '<div class="bloc">';
  if (premiere) h += consigne(d.consignes[u.teil]) + mark(champTelc(d.conseils[u.teil], "text"));
  h += bandeau(u);
  if (u.teil === "T1" || u.teil === "T2") h += '<p class="petit"><b>' + esc(T("ho_situation")) + DEUX_POINTS_TELC.trimEnd() + '</b> ' + esc(champTelc(u.data, "situation")) + '</p>';
  if (u.teil === "T3") h += '<p class="petit" lang="de">' + esc(u.data.typ) + '</p>';
  if (u.teil === "T1") h += '<p class="consigne" lang="de">' + esc(u.data.frage) + (fini ? '<span class="fr">' + esc(champTelc(u.data, "frage")) + '</span>' : "") + '</p>' +
    '<p class="petit">' + esc(T("ho_solutions")) + '</p>' + listeSolutions(u.data.loesungen, fini, u.questions.map(q => q.bon));
  if (u.teil === "T4") h += '<p class="consigne" lang="de">' + esc(u.data.thema) + (fini ? '<span class="fr">' + esc(champTelc(u.data, "thema")) + '</span>' : "") + '</p>' +
    '<p class="petit">' + esc(T("ho_aussagen")) + '</p>' + listeSolutions(u.data.saetze, fini, u.questions.map(q => q.bon));
  const lec = lecteur("H" + H.page, u, fini, () => pageH(true));
  h += lec.h;
  h += u.questions.map(q => carte(q, {choisi: H.rep[q.nr], montrer: H.rep[q.nr] !== undefined, fige: H.rep[q.nr] !== undefined})).join("");
  if (fini) h += '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + transcription(u);
  h += '</div><p class="petit" style="text-align:center">' + esc(T("ho_voix_tel")) + '</p>';
  const y = window.scrollY;
  $("zone").innerHTML = h;
  lec.brancher();
  $("voirFmt").onclick = () => montrerFormat(u.teil);
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { stopSon(); const nr = +b.dataset.aller; H.page = H.us.findIndex(x => x.questions.some(q => q.nr === nr)); pageH(); const el = $("q" + nr); if (el) setTimeout(() => el.scrollIntoView({block: "center"}), 30); });
  document.querySelectorAll("#zone .opt:not(:disabled)").forEach(b => b.onclick = () => repondreH(+b.dataset.nr, b.dataset.v));
  const suite = $("suite");
  suite.hidden = !fini; suite.textContent = T("ho_continuer");
  suite.onclick = () => { stopSon(); const reste = H.us.findIndex((x, k) => k > H.page && x.questions.some(q => H.rep[q.nr] === undefined));
    const avant = H.us.findIndex(x => x.questions.some(q => H.rep[q.nr] === undefined));
    if (reste >= 0 || avant >= 0){ H.page = reste >= 0 ? reste : avant; pageH(); window.scrollTo(0, 0); } else recapH(); };
  if (garderScroll) window.scrollTo(0, y); else window.scrollTo(0, 0);
}
function repondreH(nr, v){
  if (H.rep[nr] !== undefined) return;
  const q = questionsDe(H.us).find(x => x.nr === nr);
  H.rep[nr] = q.kind === "rf" ? v === "true" : v;
  const ok = H.rep[nr] === q.bon;
  parler("exercice", {juste: ok}); if (ok) parler("bonne");
  // la page finie : le son s'arrete, la transcription s'affiche
  if (H.us[H.page].questions.every(x => H.rep[x.nr] !== undefined)) stopSon();
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
  const s = H.serie, b = bilanH(H.us, H.rep);
  marquerFait("H", s);
  resultat("H", {serie: s.id, bons: b.bons, sur: 20, points: b.points});
  parler("fini", {bons: b.bons, faits: 20});
  const mot = b.bons >= 14 ? "ho_mark_bien" : b.bons >= 8 ? "ho_mark_moyen" : "ho_mark_faible";
  const lignes = [].concat(...H.us.map(u => u.questions.map(q => ({q, ok: H.rep[q.nr] === q.bon}))));
  const fin = boutonsFin("H", () => ouvrirH(s));
  $("titre").textContent = T("ho_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("ho_titre")) + ' · ' + esc(T("ho_recap")) + '</div>' +
      '<div class="score">' + esc(T("ho_score", {n: b.bons, t: 20})) + '</div>' +
      '<p class="petit" style="text-align:center">' + esc(T("ho_points_h", {n: b.bons, p: b.points})) + '</p>' +
      detailTeils(b.parTeil) + mark(T(mot)) + '<p class="petit">' + esc(T("ho_seuils_h")) + '</p></div>' +
    '<div class="bloc">' + lignes.filter(x => !x.ok).concat(lignes.filter(x => x.ok)).map(x => carte(x.q, {choisi: H.rep[x.q.nr], montrer: true, fige: true})).join("") + '</div>' + fin.h;
  fin.brancher();
  window.scrollTo(0, 0);
}

// ============ L'EXAMEN BLANC : HOEREN ============
// Comme l'enregistrement de l'examen : chaque Teil s'affiche avec toutes ses questions, la consigne est dite, le temps
// de lecture passe, le son joue le nombre de fois du format, la question en cours est encadree. Pas de correction
// avant la fin. Les 30 s de lecture de Teil 1 viennent du format ; les autres pauses sont les notres. La minuterie
// est celle de l'examen blanc (minutes: 35, partagees avec Hoeren und Schreiben). fini({pts: {Hoeren}, detail}).
let X = null;
function etatExamen(texte, joue){ const e = $("exEtat"); if (e) e.innerHTML = (joue ? '<i></i>' : "") + esc(texte); }
function marquerEx(nrs){ document.querySelectorAll("#zone .q").forEach(x => x.classList.toggle("joue", nrs.includes(+x.id.slice(1)))); const el = $("q" + nrs[0]); if (el) el.scrollIntoView({behavior: "smooth", block: "center"}); }
// les gestes d'une ecoute d'examen, tant que vivant() (hoeren-schreiben.js s'en sert aussi)
function deroulement(vivant){
  return {
    pause: async (s, texte) => { etatExamen(texte); await attendre(s); return vivant(); },
    ecouter: async (segs, cles, nrs) => { if (nrs) marquerEx(nrs); etatExamen(T("ho_ex_joue"), true); return await jouerSegments(segs, cles, 1.2, E.jeton) && vivant(); },
    // une consigne ou un « Nummer 42 » : sa piste enregistree (cle), sinon la voix du telephone
    dire: async (ligne, cle) => { await jouerSegments([[ligne]], [cle], 0, E.jeton); return vivant(); },
    consigne: async (c, cle) => { etatExamen(T("ho_ex_consigne"), true); await jouerSegments([[c]], [cle], 0, E.jeton); return vivant(); }
  };
}
function feuilleTeil(teil){
  const us = X.us.filter(u => u.teil === teil), u0 = us[0];
  let h = '<div class="bloc"><div class="section">Hören · Teil ' + teil.slice(1) + ' · ' + esc(T("ho_" + teil)) + '</div><div class="ecoute" id="exEtat"></div>' + bandeau(u0);
  h += '<p class="consigne" lang="de">' + esc(E.d.consignes[teil].text) + '</p>';
  if (teil === "T1") h += '<p class="consigne" lang="de">' + esc(u0.data.frage) + '</p>' + listeSolutions(u0.data.loesungen, false);
  if (teil === "T4") h += '<p class="consigne" lang="de">' + esc(u0.data.thema) + '</p>' + listeSolutions(u0.data.saetze, false);
  h += us.map(u => u.questions.map(q => carte(q, {choisi: X.rep[q.nr], montrer: false, fige: false})).join("")).join("") + '</div>';
  $("zone").innerHTML = h;
  document.querySelectorAll("#zone .opt").forEach(b => b.onclick = () => {
    const nr = +b.dataset.nr, q = questionsDe(X.us).find(x => x.nr === nr);
    X.rep[nr] = q.kind === "rf" ? b.dataset.v === "true" : b.dataset.v;
    b.parentNode.querySelectorAll(".opt").forEach(x => x.classList.toggle("pris", x === b));
  });
  window.scrollTo(0, 0);
}
async function examenH(fini, serie){
  stopSon(); debloquerSon();
  const s = serie || await choisirSerie(E.d.series, () => [], "XH");
  const moi = X = {s, us: unitesH(s), rep: {}};
  const jeton = E.jeton, vivant = () => X === moi && E.jeton === jeton, d = E.d, r = deroulement(vivant);
  $("titre").textContent = T("ho_titre") + " · Hören"; $("suite").hidden = true;
  for (const teil of ["T1", "T2", "T3", "T4"]){
    if (!vivant()) return;
    feuilleTeil(teil);
    const us = moi.us.filter(u => u.teil === teil), u0 = us[0];
    if (!await r.consigne(d.consignes[teil], "telc-consigne-" + teil)) return;
    if (u0.lecture && !await r.pause(u0.lecture, T("ho_ex_lecture"))) return;
    if (teil === "T1"){
      const nrs = u0.questions.map(q => q.nr);
      if (!await r.ecouter(u0.segs, u0.cles, nrs) || !await r.pause(10, T("ho_ex_pause")) || !await r.ecouter(u0.segs, u0.cles, nrs) || !await r.pause(15, T("ho_ex_pause"))) return;
    } else if (teil === "T2"){
      if (!await r.ecouter(u0.segs, u0.cles, u0.questions.map(q => q.nr)) || !await r.pause(20, T("ho_ex_pause"))) return;
    } else if (teil === "T3"){
      for (const u of us){
        const nr = u.questions[0].nr;
        marquerEx([nr]);
        if (!await r.dire({wer: "aurora", text: "Nummer " + nr + "."}, "telc-nummer-" + nr)) return;
        if (!await r.pause(5, T("ho_ex_lecture")) || !await r.ecouter(u.segs, u.cles, [nr]) || !await r.pause(4, T("ho_ex_pause")) || !await r.ecouter(u.segs, u.cles, [nr]) || !await r.pause(8, T("ho_ex_pause"))) return;
      }
    } else {
      if (!await r.ecouter([u0.segs[0]], [u0.cles[0]])) return;
      for (let k = 1; k < u0.segs.length; k++){
        if (!await r.pause(2, "") || !await r.ecouter([u0.segs[k]], [u0.cles[k]], [u0.questions[k - 1].nr]) || !await r.pause(10, T("ho_ex_pause"))) return;
      }
    }
  }
  if (!vivant()) return;
  const b = bilanH(moi.us, moi.rep);
  marquerFait("XH", s);
  resultat("H", {examen: true, serie: s.id, bons: b.bons, sur: 20, points: b.points});
  fini({pts: {Hoeren: b.points}, detail: {bons: b.bons, sur: 20, parTeil: b.parTeil, html: corrigeH(moi)}});
}
// le corrige de l'examen : chaque Teil, les reponses, la transcription (HTML, pour le corrige de l'examen blanc)
function corrigeH(x){
  return ["T1", "T2", "T3", "T4"].map(t => {
    const us = x.us.filter(u => u.teil === t);
    return '<div class="bloc"><div class="section">Hören · Teil ' + t.slice(1) + ' · ' + esc(T("ho_" + t)) + '</div>' +
      (t === "T1" ? listeSolutions(us[0].data.loesungen, true, us[0].questions.map(q => q.bon)) : t === "T4" ? listeSolutions(us[0].data.saetze, true, us[0].questions.map(q => q.bon)) : "") +
      us.map(u => u.questions.map(q => carte(q, {choisi: x.rep[q.nr], montrer: true, fige: true, corrige: true})).join("") +
        '<p class="petit">' + esc(T("ho_transcription")) + '</p>' + transcription(u)).join("") + '</div>';
  }).join("");
}

// ce qui sert aussi a hoeren-schreiben.js
window.TELC_ECOUTE = {E, stopSon, direLigne, jouerSegments, bandeau, consigne, mark, transcription, blocFormat, montrerFormat,
  pointsDe, toutesLesSections, boutonsFin, lecteur, deroulement, marquerEx, etatExamen, examenH, detailTeils, ouvrirH};
})();
