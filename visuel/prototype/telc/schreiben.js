// LE TELC A2·B1 AVEC MARK ET ANNA -- ECRIRE (6 nov. 2026, session « telc Ecrire »).
//
// Deux parties du telc, d'apres preparation-examens/FORMAT-TELC.md (le format seul, jamais le contenu) :
//   LS  « Lire et ecrire » (Lesen und Schreiben, items 29-31) : un courriel recu qui pose des questions ;
//       29 Richtig/Falsch, 30 un choix a 2, puis 31 la reponse a ce courriel (critere I sur 15) ;
//       35 minutes avec les Sprachbausteine.
//   S   « Ecrire » (Schreiben, item 57) : repondre a un message court qui pose une question (wann, was, warum
//       nicht, welches, wie lange, wo, wohin), en plus d'un mot ; 10 minutes ; critere I sur 5.
// Les criteres II, III, IV (10 points chacun) jugent les deux textes ensemble a l'examen : l'entrainement les
// estime pour le texte que l'on vient d'ecrire.
//
// L'ORGANISATION EST CELLE DES SPRACHBAUSTEINE (et de l'oral du DTZ, decision de Jacques du 4 nov.) : une page par
// exercice, « Section · … », des points de progression qu'on touche pour sauter, « ‹ » vers la liste, « Continuer »
// en bas ; en fin de section, un recapitulatif, puis Refaire / Section suivante / Toutes les sections.
//   LS : 29 · 30 · 31 (ecrire) · ✓ (la grille) · M (les lettres modeles A2 et B1, annotees)
//   S  : 57 (ecrire) · ✓ · M
//
// CE QUE LA PAGE NE FAIT PAS, et le dit : elle ne corrige ni la grammaire ni l'orthographe. Elle compte les mots,
// cherche la formule d'appel et la salutation, le registre (du / Sie), les connecteurs et des indices de chaque
// point ; le reste, c'est l'eleve qui le juge avec la grille, puis il compare aux lettres modeles.
//
// Donnees : donnees/schreiben.json (controle : python tests/telc_schreiben.py). Interface en francais et en anglais
// (?lang=en) ; les autres langues retombent sur le francais, comme le reste de la page.
// Ce module ne connait de commun.js que ses fonctions publiques ($, esc, T, TXT, LANGUE, Q, parler, lire, ecrire,
// DTZ, accueil, MARK_IMG, chrono, arreterChrono, ouvrir, fermerPanneau, choisirSerie, marquerFait, resultat,
// silence) ; il s'inscrit par DTZ.partie() comme sprachbausteine.js.

"use strict";

const SCH_EN = LANGUE === "en";

Object.assign(TXT, {
  ls_titre: "Lire et écrire", ls_sous: "Un courriel à lire, puis ta réponse",
  ls_section: "Section · Lire et écrire",
  s_titre: "Écrire", s_sous: "Un message court, 10 minutes",
  s_section: "Section · Écrire",
  sch_situation: "La situation :",
  sch_de: "De :", sch_a: "À :",
  sch_rf_consigne_de: "Lesen Sie die E-Mail. Ist die Aussage richtig oder falsch?",
  sch_rf_consigne: "Lis le courriel. L'affirmation est-elle juste ou fausse ?",
  sch_ab_consigne_de: "Lesen Sie die E-Mail noch einmal. Welche Antwort passt?",
  sch_ab_consigne: "Relis le courriel. Quelle réponse convient ?",
  sch_richtig: "Richtig", sch_falsch: "Falsch",
  sch_juste: "Juste !", sch_faux: "Pas tout à fait.",
  sch_mark_ls: "Au telc, ce courriel arrive juste après les Sprachbausteine : deux questions pour vérifier que tu l'as compris, puis tu y réponds. Les deux questions t'aident : elles te montrent ce que le courriel demande.",
  sch_mark_s: "C'est la toute dernière tâche de l'écrit, après l'écoute : 10 minutes pour répondre à un message court. Regarde d'abord le mot interrogatif (wann, warum, wohin…) : ta réponse doit lui répondre, en plus d'un mot.",
  sch_ecrire_ls_de: "Antworten Sie {p}. Schreiben Sie zu jeder Frage etwas. Vergessen Sie Anrede und Gruß nicht.",
  sch_ecrire_ls: "Réponds à {p}. Écris quelque chose pour chaque question. N'oublie ni la formule d'appel ni la salutation.",
  sch_ecrire_s_de: "Sie bekommen diese Nachricht. Antworten Sie. Schreiben Sie mehr als ein Wort.",
  sch_ecrire_s: "Tu reçois ce message. Réponds-y, en plus d'un mot.",
  sch_points_titre: "Les points à traiter",
  sch_tu_reponds: "Tu réponds à la place de Mark : invente les détails qu'il te faut.",
  sch_longueur_ls: "Le modèle d'examen ne fixe pas de nombre de mots : ce qui compte, c'est de répondre à chaque question. Repère de Wortando : environ 40 à 80 mots au A2, 80 à 120 au B1.",
  sch_longueur_s: "Repère de Wortando : deux phrases au A2 (10 à 20 mots), trois ou quatre au B1 (20 à 40 mots).",
  sch_temps_ls: "À l'examen, cette partie et les Sprachbausteine ont 35 minutes ensemble : compte environ 20 minutes pour ce courriel.",
  sch_temps_s: "À l'examen : 10 minutes.",
  sch_chrono_ls: "Lancer le chrono (20 min conseillées)",
  sch_chrono_s: "Lancer les 10 minutes",
  sch_temps_fini: "Le temps de l'examen est écoulé. Tu peux finir ton texte, mais le jour J, il faudrait s'arrêter là.",
  sch_formules: "Formules utiles",
  sch_ton_texte: "Ton texte",
  sch_placeholder: "Écris ta réponse ici, en allemand…",
  sch_mots: "{n} mot(s)",
  sch_verifier: "Vérifier mon texte",
  sch_vide: "Écris d'abord quelques phrases.",
  sch_voit: "Ce que la page voit",
  sch_voit_s: "Elle compte et cherche des indices ; elle ne corrige ni la grammaire ni l'orthographe.",
  sch_v_mots: "Longueur : {n} mot(s).",
  sch_v_court_ls: "C'est court pour répondre à toutes les questions.",
  sch_v_court_s: "Au telc, il faut écrire plus d'un mot.",
  sch_v_long: "C'est long : relis-toi plutôt que d'ajouter.",
  sch_v_anrede_ok: "Formule d'appel : « {m} ».",
  sch_v_anrede_ko: "Pas de formule d'appel au début (Liebe …, Hallo …, Sehr geehrte …).",
  sch_v_gruss_ok: "Salutation à la fin : « {m} ».",
  sch_v_gruss_ko: "Pas de salutation à la fin (Viele Grüße, Liebe Grüße, Mit freundlichen Grüßen…).",
  sch_v_gruss_froid: "« Mit freundlichen Grüßen » est un peu froid pour un ami : « Viele Grüße » ou « Liebe Grüße » ira mieux.",
  sch_v_sie_informel: "Tu tutoies ? Le texte contient « {m} » au milieu d'une phrase : c'est le vouvoiement. Garde le même registre partout.",
  sch_v_du_formel: "Le message vouvoie, et ton texte contient « {m} » : garde « Sie » partout.",
  sch_v_registre_ok: "Le registre ({r}) semble tenu du début à la fin.",
  sch_v_conn: "Connecteurs repérés : {m}.",
  sch_v_conn_aucun: "Aucun connecteur repéré : relie tes phrases (und, aber, denn, weil, dass…).",
  sch_v_sub: "Des subordonnées (weil, dass, wenn, ob…) : une marque du B1.",
  sch_v_sub_aucune: "Pas encore de subordonnée (weil, dass, wenn, ob…) : c'est ce qui fait souvent passer au B1.",
  sch_v_question: "Une question en retour : l'échange continue.",
  sch_v_point_ok: "semble traité",
  sch_v_point_ko: "à vérifier",
  sch_v_frage_ok: "La question « {f} » semble avoir sa réponse.",
  sch_v_frage_ko: "Je ne vois pas de réponse évidente à « {f} ». {c}",
  sch_grille: "La grille : à toi de juger",
  sch_grille_s: "Relis ton texte avec chaque description, puis choisis. C'est la grille de l'examinateur, simplifiée.",
  sch_coche: "J'ai répondu à :",
  sch_b1p: "B1, tout à fait", sch_b1: "B1, en gros", sch_a2p: "A2, tout à fait", sch_a2: "A2, en gros", sch_moins: "Pas encore A2",
  sch_desc_b1: "B1", sch_desc_a2: "A2", sch_desc_moins: "Sous A2",
  sch_estimation: "Estimation pour ce texte : {p} sur {s}",
  sch_estimation_note: "À l'examen, l'écrit compte 60 points : les Sprachbausteine (5), le courriel (15), les notes du répondeur (5), le message court (5) et les critères II à IV sur les deux textes ensemble (30). Ici, ce texte seul.",
  sch_remplir: "Choisis un niveau pour les quatre critères pour voir l'estimation.",
  sch_incoherent: "Tu as choisi B1 pour la tâche, mais {n} point(s) ne sont pas cochés : au B1, chaque question a sa réponse.",
  sch_voir_modeles: "Voir les lettres modèles",
  sch_modeles: "Deux lettres modèles",
  sch_modeles_s: "Les mêmes questions, deux niveaux. Touche un passage souligné pour lire la note.",
  sch_modele_a2: "Lettre modèle A2", sch_modele_b1: "Lettre modèle B1",
  sch_message_a2: "Réponse modèle A2", sch_message_b1: "Réponse modèle B1",
  sch_passer: "Ce qui fait passer de A2 à B1",
  sch_terminer: "Terminer la section",
  sch_recap: "Récapitulatif",
  sch_q_score: "Questions 29 et 30 : {n} sur 2",
  sch_pas_estime: "Pas d'estimation : la grille n'est pas remplie.",
  sch_mark_b1: "Bravo, c'est un texte de niveau B1 ! Garde ce réflexe : une raison ou un détail pour chaque question.",
  sch_mark_a2: "C'est un bon A2. Pour viser le B1, relis la lettre modèle B1 : chaque réponse y reçoit une raison, reliée par weil, dass ou wenn.",
  sch_mark_moins: "C'est un début. Reprends les points à traiter un par un : une phrase complète pour chacun, une formule d'appel, une salutation. Les formules utiles sont là pour ça.",
  sch_refaire: "Refaire la section", sch_suivante: "Section suivante", sch_toutes: "Toutes les sections",
  sch_autre: "Un autre sujet",
  sch_reg_du: "du", sch_reg_sie: "Sie", sch_reg_beide: "du ou Sie",
  sch_formules_note: "Les tournures marquées « du » vont avec le tutoiement, celles marquées « Sie » avec le vouvoiement.",
  sch_frage_wann: "Wann?", sch_frage_was: "Was?", sch_frage_warum_nicht: "Warum nicht?", sch_frage_welches: "Welches?", sch_frage_wie_lange: "Wie lange?", sch_frage_wo: "Wo?", sch_frage_wohin: "Wohin?"
});

if (SCH_EN) Object.assign(TXT, {
  ls_titre: "Read and write", ls_sous: "An email to read, then your reply",
  ls_section: "Section · Read and write",
  s_titre: "Write", s_sous: "A short message, 10 minutes",
  s_section: "Section · Write",
  sch_situation: "The situation:",
  sch_de: "From:", sch_a: "To:",
  sch_rf_consigne: "Read the email. Is the statement true or false?",
  sch_ab_consigne: "Read the email again. Which answer fits?",
  sch_juste: "Correct!", sch_faux: "Not quite.",
  sch_mark_ls: "In the telc, this email comes right after the Sprachbausteine: two questions to check you have understood it, then you reply to it. Those two questions help you: they show you what the email is asking for.",
  sch_mark_s: "This is the very last task of the written exam, after the listening: 10 minutes to reply to a short message. Look at the question word first (wann, warum, wohin…): your answer must answer it, in more than one word.",
  sch_ecrire_ls: "Reply to {p}. Write something for each question. Don't forget the opening and the closing.",
  sch_ecrire_s: "You receive this message. Reply to it, in more than one word.",
  sch_points_titre: "The points to cover",
  sch_tu_reponds: "You are replying for Mark: make up any details you need.",
  sch_longueur_ls: "The exam sets no word count: what matters is answering every question. Wortando's guide: about 40 to 80 words at A2, 80 to 120 at B1.",
  sch_longueur_s: "Wortando's guide: two sentences at A2 (10 to 20 words), three or four at B1 (20 to 40 words).",
  sch_temps_ls: "In the exam, this part and the Sprachbausteine share 35 minutes: allow about 20 minutes for this email.",
  sch_temps_s: "In the exam: 10 minutes.",
  sch_chrono_ls: "Start the timer (20 min suggested)",
  sch_chrono_s: "Start the 10 minutes",
  sch_temps_fini: "The exam time is up. You can finish your text, but on the day you would have to stop here.",
  sch_formules: "Useful phrases",
  sch_ton_texte: "Your text",
  sch_placeholder: "Write your reply here, in German…",
  sch_mots: "{n} word(s)",
  sch_verifier: "Check my text",
  sch_vide: "Write a few sentences first.",
  sch_voit: "What the page can see",
  sch_voit_s: "It counts and looks for clues; it does not correct grammar or spelling.",
  sch_v_mots: "Length: {n} word(s).",
  sch_v_court_ls: "That is short for answering every question.",
  sch_v_court_s: "In the telc, you must write more than one word.",
  sch_v_long: "That is long: check it over rather than adding more.",
  sch_v_anrede_ok: "Opening: \"{m}\".",
  sch_v_anrede_ko: "No opening at the start (Liebe …, Hallo …, Sehr geehrte …).",
  sch_v_gruss_ok: "Closing at the end: \"{m}\".",
  sch_v_gruss_ko: "No closing at the end (Viele Grüße, Liebe Grüße, Mit freundlichen Grüßen…).",
  sch_v_gruss_froid: "\"Mit freundlichen Grüßen\" is a bit cold for a friend: \"Viele Grüße\" or \"Liebe Grüße\" will fit better.",
  sch_v_sie_informel: "Are you saying du? The text has \"{m}\" in the middle of a sentence: that is the formal Sie. Keep the same register throughout.",
  sch_v_du_formel: "The message uses Sie, and your text has \"{m}\": keep \"Sie\" throughout.",
  sch_v_registre_ok: "The register ({r}) seems to hold from start to finish.",
  sch_v_conn: "Linking words found: {m}.",
  sch_v_conn_aucun: "No linking words found: connect your sentences (und, aber, denn, weil, dass…).",
  sch_v_sub: "Subordinate clauses (weil, dass, wenn, ob…): a B1 feature.",
  sch_v_sub_aucune: "No subordinate clause yet (weil, dass, wenn, ob…): this is often what takes you to B1.",
  sch_v_question: "A question back: the exchange goes on.",
  sch_v_point_ok: "seems covered",
  sch_v_point_ko: "to check",
  sch_v_frage_ok: "The question \"{f}\" seems to have its answer.",
  sch_v_frage_ko: "I can't see an obvious answer to \"{f}\". {c}",
  sch_grille: "The grid: you be the judge",
  sch_grille_s: "Read your text again against each description, then choose. This is the examiner's grid, simplified.",
  sch_coche: "I have answered:",
  sch_b1p: "B1, fully", sch_b1: "B1, mostly", sch_a2p: "A2, fully", sch_a2: "A2, mostly", sch_moins: "Not A2 yet",
  sch_desc_moins: "Below A2",
  sch_estimation: "Estimate for this text: {p} out of {s}",
  sch_estimation_note: "In the exam, writing is worth 60 points: the Sprachbausteine (5), the email (15), the voicemail notes (5), the short message (5) and criteria II to IV for both texts together (30). Here, this text alone.",
  sch_remplir: "Choose a level for all four criteria to see the estimate.",
  sch_incoherent: "You chose B1 for the task, but {n} point(s) are not ticked: at B1, every question gets an answer.",
  sch_voir_modeles: "See the model letters",
  sch_modeles: "Two model letters",
  sch_modeles_s: "The same questions, two levels. Tap an underlined passage to read the note.",
  sch_modele_a2: "A2 model letter", sch_modele_b1: "B1 model letter",
  sch_message_a2: "A2 model reply", sch_message_b1: "B1 model reply",
  sch_passer: "What takes you from A2 to B1",
  sch_terminer: "Finish the section",
  sch_recap: "Summary",
  sch_q_score: "Questions 29 and 30: {n} out of 2",
  sch_pas_estime: "No estimate: the grid has not been filled in.",
  sch_mark_b1: "Well done, that is a B1 text! Keep the habit: a reason or a detail for every question.",
  sch_mark_a2: "That is a good A2. To aim for B1, read the B1 model letter again: every answer there gets a reason, linked with weil, dass or wenn.",
  sch_mark_moins: "It's a start. Go through the points to cover one by one: a full sentence for each, an opening, a closing. That is what the useful phrases are for.",
  sch_refaire: "Redo the section", sch_suivante: "Next section", sch_toutes: "All sections",
  sch_autre: "Another topic",
  sch_reg_beide: "du or Sie", niv_moins: "below A2",
  sch_formules_note: "Phrases marked \"du\" go with the informal register, those marked \"Sie\" with the formal one."
});

// un champ des donnees dans la langue de l'interface : « x_en » en anglais s'il existe, sinon « x_fr »
// (les notes des modeles et la grille ont « fr » / « en » sans suffixe)
function trS(o, cle){
  if (!o) return "";
  if (cle === undefined) return (SCH_EN && o.en) || o.fr || "";
  return (SCH_EN && o[cle + "_en"]) || o[cle + "_fr"] || "";
}

// le style propre a ces pages, ajoute par le module pour ne pas toucher a telc.html
(function(){
  const st = document.createElement("style");
  st.textContent =
    ".sch-zone{width:100%;min-height:220px;border:2px solid var(--trait);border-radius:14px;padding:10px 12px;font:600 16px/1.5 var(--police);color:var(--encre);background:var(--papier);resize:vertical;direction:ltr}" +
    ".sch-zone:focus{outline:none;border-color:var(--ambre)}" +
    ".sch-zone.court{min-height:120px}" +
    ".sch-compte{font-size:13px;font-weight:800;color:var(--gris);text-align:right}" +
    ".sch-liste{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px;line-height:1.45}" +
    ".sch-liste .de{font-weight:800;direction:ltr;unicode-bidi:isolate}" +
    ".sch-liste .tr{display:block;font-size:13px;color:var(--gris);font-weight:700}" +
    ".sch-rangee{display:flex;flex-wrap:wrap;gap:8px;align-items:center}" +
    ".sch-temps{font-size:13px;font-weight:800;color:var(--rouge)}" +
    ".sch-v{display:flex;flex-direction:column;gap:6px;margin:0;padding:0;list-style:none}" +
    ".sch-v li{display:flex;gap:8px;align-items:baseline;line-height:1.45;font-weight:700;font-size:14px}" +
    ".sch-v li b{flex:0 0 18px;text-align:center}" +
    ".sch-v li.ok b{color:var(--vert)} .sch-v li.ko b{color:var(--rouge)} .sch-v li.inf b{color:var(--ambre-f)}" +
    ".sch-coche{display:flex;gap:10px;align-items:flex-start;font-weight:700;line-height:1.4;cursor:pointer}" +
    ".sch-coche input{width:20px;height:20px;margin-top:1px;accent-color:var(--vert);flex:0 0 auto}" +
    ".sch-crit{background:var(--carte);border-radius:16px;padding:11px 12px;display:flex;flex-direction:column;gap:8px}" +
    ".sch-crit h3{margin:0;font-size:15px;font-weight:900}" +
    ".sch-crit h3 small{font-weight:700;color:var(--gris);font-size:12px;margin-left:6px}" +
    ".sch-desc{font-size:13px;line-height:1.45;font-weight:600;margin:0}" +
    ".sch-desc b{font-weight:900}" +
    ".sch-niv{display:flex;flex-wrap:wrap;gap:6px}" +
    ".sch-niv button{border:2px solid var(--trait);background:var(--verre);color:var(--encre);border-radius:999px;padding:6px 11px;font:800 13px var(--police);cursor:pointer}" +
    ".sch-niv button.pris{border-color:var(--encre);background:var(--encre);color:var(--verre)}" +
    ".sch-estim{background:var(--carte);border-radius:16px;padding:12px;display:flex;flex-direction:column;gap:8px;align-items:center;text-align:center}" +
    ".sch-estim .p{font-size:22px;font-weight:900}" +
    ".sch-modele{white-space:normal}" +
    ".sch-modele mark{background:rgba(232,162,58,.22);color:inherit;border-bottom:2px solid var(--ambre);border-radius:3px;padding:0 1px;cursor:pointer}" +
    ".sch-modele mark.actif{background:rgba(232,162,58,.5)}" +
    ".sch-modele sup{font-weight:900;color:var(--ambre-f);font-size:10px;margin-left:1px}" +
    ".sch-notes{margin:0;padding-left:22px;display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:1.45;font-weight:600}" +
    ".sch-notes li.actif{background:rgba(232,162,58,.18);border-radius:8px}" +
    ".sch-notes .ex{font-weight:800;direction:ltr;unicode-bidi:isolate}" +
    ".sch-niveau{align-self:flex-start;border-radius:999px;padding:3px 12px;font-weight:900;font-size:13px;color:#fff}" +
    ".sch-niveau.a2{background:var(--ambre-f)} .sch-niveau.b1{background:var(--vert)}" +
    ".sch-form h3{margin:6px 0 2px;font-size:15px;font-weight:900}" +
    ".sch-form ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:6px}" +
    ".sch-form li{background:var(--carte);border-radius:12px;padding:8px 10px;line-height:1.4}" +
    ".sch-form li .de{font-weight:800;direction:ltr;unicode-bidi:isolate;display:block}" +
    ".sch-form li .tr{font-size:13px;color:var(--gris);font-weight:700}" +
    ".sch-form li .reg{font-size:11px;font-weight:900;border:1px solid var(--trait);border-radius:999px;padding:0 6px;margin-left:6px;color:var(--gris)}" +
    ".sch-texte{white-space:pre-wrap;direction:ltr;text-align:left;background:var(--papier);border:1px solid var(--papier-trait);border-radius:10px;padding:10px 12px;font-size:14px;line-height:1.55}";
  document.head.appendChild(st);
})();

const SCH = { d: null, mode: null, serie: null, i: 0, etat: null };

DTZ.charger(fetch("donnees/schreiben.json", { cache: "no-cache" })
  .then(r => { if (!r.ok) throw new Error("schreiben.json"); return r.json(); })
  .then(d => { SCH.d = d; }));

DTZ.partie({ id: "LS", ordre: 30, titre: T("ls_titre"), sous: T("ls_sous"), ouvrir: () => ouvrirSchreiben("LS") });
DTZ.partie({ id: "S", ordre: 60, titre: T("s_titre"), sous: T("s_sous"), ouvrir: () => ouvrirSchreiben("S") });

// les pages de chaque partie, dans l'ordre ; le libelle de leur point de progression
const SCH_PAGES = {
  LS: [{id: "q29", pt: "29"}, {id: "q30", pt: "30"}, {id: "ecrire", pt: "31"}, {id: "verifier", pt: "✓"}, {id: "modeles", pt: "M"}],
  S: [{id: "ecrire", pt: "57"}, {id: "verifier", pt: "✓"}, {id: "modeles", pt: "M"}]
};

// ============ L'OUVERTURE ============
async function ouvrirSchreiben(mode, serie){
  SCH.mode = mode;
  const series = mode === "LS" ? SCH.d.email : SCH.d.kurz;
  SCH.serie = serie || await choisirSerie(series, () => [], "SCH" + mode);
  // ce que l'eleve a deja fait sur ce sujet (son texte, ses reponses, sa grille) reste la quand il revient
  SCH.etat = Object.assign({ q: {}, texte: "", coches: [], crit: {} }, lire("sch_" + mode + "_" + SCH.serie.id, {}));
  SCH.i = 0;
  DTZ.surRetour(() => { toutesLesSectionsSch(); return true; });
  page();
}
function garder(){ ecrire("sch_" + SCH.mode + "_" + SCH.serie.id, SCH.etat); }

function toutesLesSectionsSch(){
  arreterChrono();
  // ouverte directement sur cette partie depuis le panneau du bloc telc (?partie=LS ou S) : on ferme le cadre
  if (Q.get("partie") === SCH.mode){ silence(); parler("fermer"); if (window.parent === window) accueil(); return; }
  accueil();
}

// ============ LES MORCEAUX COMMUNS ============
function pointsSch(){
  const pages = SCH_PAGES[SCH.mode];
  return '<div class="points">' + pages.map((p, k) => {
    let etat = "";
    if (p.id === "q29" || p.id === "q30"){
      const f = SCH.serie.fragen.find(x => "q" + x.n === p.id), r = SCH.etat.q[f.n];
      if (r !== undefined) etat = r === f.bon ? " ok" : " ko";
    } else if (p.id === "ecrire" && motsDe(SCH.etat.texte) > 0) etat = " ok";
    else if (p.id === "verifier" && estimation()) etat = " ok";
    return '<button class="point' + etat + (k === SCH.i ? " ici" : "") + '" data-aller="' + k + '" aria-label="' + esc(p.pt) + '">' + esc(p.pt) + '</button>';
  }).join("") + '</div>';
}

function enteteSch(){
  return '<div class="bloc"><div class="section">' + esc(T(SCH.mode === "LS" ? "ls_section" : "s_section")) + '</div>' + pointsSch() + '</div>';
}

function bulleMark(texte){
  return '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(texte) + '</div></div>';
}

// le message recu, mis en page comme les lettres des Sprachbausteine (jamais en image)
function docRecu(){
  const s = SCH.serie;
  if (SCH.mode === "LS"){
    const m = s.mail;
    return '<div class="doc lettre" dir="ltr"><div class="k">E-Mail</div>' +
      '<div class="petit" lang="de">' + esc(T("sch_de")) + ' ' + esc(m.von) + ' · ' + esc(T("sch_a")) + ' ' + esc(m.an) + '</div>' +
      '<div class="objet" lang="de">' + esc(m.betreff) + '</div>' +
      m.lignes.map(l => '<p lang="de">' + esc(l) + '</p>').join("") + '</div>';
  }
  const n = s.nachricht;
  return '<div class="doc lettre" dir="ltr"><div class="k">' + esc(n.art) + '</div>' +
    n.lignes.map(l => '<p lang="de">' + esc(l) + '</p>').join("") + '</div>';
}

function situation(){
  return '<p class="petit"><b>' + esc(T("sch_situation")) + '</b> ' + esc(trS(SCH.serie, "situation")) + '</p>';
}

// ============ LES PAGES ============
function page(){
  silence();
  const p = SCH_PAGES[SCH.mode][SCH.i];
  $("titre").textContent = T(SCH.mode === "LS" ? "ls_titre" : "s_titre");
  if (p.id !== "ecrire") arreterChrono();
  ({ q29: pageQuestion, q30: pageQuestion, ecrire: pageEcrire, verifier: pageVerifier, modeles: pageModeles })[p.id](p);
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { SCH.i = Number(b.dataset.aller); page(); });
  window.scrollTo(0, 0);
}

function suite(libelle, action){
  const b = $("suite");
  b.hidden = !libelle; if (!libelle) return;
  b.textContent = libelle; b.onclick = action;
}
function pageSuivante(){
  if (SCH.i + 1 < SCH_PAGES[SCH.mode].length){ SCH.i++; page(); } else recapSch();
}

// 29 et 30 : le courriel a comprendre
function pageQuestion(p){
  const f = SCH.serie.fragen.find(x => "q" + x.n === p.id), r = SCH.etat.q[f.n];
  const opts = f.typ === "rf" ? [T("sch_richtig"), T("sch_falsch")] : f.o;
  const choix = opts.map((o, k) => {
    let cls = "opt";
    if (r !== undefined){ if (k === f.bon) cls += " juste"; else if (k === r) cls += " faux"; }
    return '<button class="' + cls + '" data-choix="' + k + '"' + (r !== undefined ? " disabled" : "") + '>' +
      (f.typ === "rf" ? "" : '<b>' + "ab"[k] + '</b>') + '<span lang="de">' + esc(o) + '</span></button>';
  }).join("");
  const aide = r === undefined ? "" :
    '<div class="aide"><div class="verdict ' + (r === f.bon ? "ok" : "ko") + '">' + esc(T(r === f.bon ? "sch_juste" : "sch_faux")) + '</div>' +
    '<div class="dit"><img src="' + MARK_IMG + '" alt="Mark"><span class="erkl">' + esc(trS(f)) + '</span></div></div>';
  const premier = SCH.i === 0 && Object.keys(SCH.etat.q).length === 0;
  $("zone").innerHTML = enteteSch() +
    (premier ? '<div class="bloc">' + bulleMark(T("sch_mark_ls")) + '</div>' : "") +
    '<div class="bloc"><p class="consigne" lang="de">' + esc(T(f.typ === "rf" ? "sch_rf_consigne_de" : "sch_ab_consigne_de")) +
      '<span class="fr">' + esc(T(f.typ === "rf" ? "sch_rf_consigne" : "sch_ab_consigne")) + '</span></p>' + situation() + docRecu() +
    '<div class="q" id="carte"><div class="tete"><span class="num">' + f.n + '</span><span class="frage" lang="de">' + esc(f.de) + '</span></div>' +
      '<div class="choix' + (f.typ === "rf" ? " ligne" : "") + '">' + choix + '</div>' + aide + '</div></div>';
  document.querySelectorAll("[data-choix]").forEach(b => b.onclick = () => {
    if (SCH.etat.q[f.n] !== undefined) return;
    const k = Number(b.dataset.choix), juste = k === f.bon;
    SCH.etat.q[f.n] = k; garder();
    parler("exercice", { juste }); if (juste) parler("bonne");
    page();
    setTimeout(() => { const c = $("carte"); if (c) try{ c.scrollIntoView({block: "center", behavior: "smooth"}); }catch(e){} }, 30);
  });
  suite(r === undefined ? null : T("continuer"), pageSuivante);
}

// 31 ou 57 : ecrire
function pageEcrire(){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const destinataire = ls ? s.mail.von.split(",")[0] : s.nachricht.von;
  const points = ls
    ? '<div class="q"><div class="frage">' + esc(T("sch_points_titre")) + '</div><ol class="sch-liste">' +
        s.punkte.map(p => '<li><span class="de" lang="de">' + esc(p.de) + '</span><span class="tr">' + esc(trS(p)) + '</span></li>').join("") + '</ol></div>'
    : '<div class="q"><div class="frage" lang="de">' + esc(T("sch_frage_" + s.frage.replace(" ", "_"))) + '</div><p class="petit">' + esc(trS(s, "conseil")) + '</p></div>';
  $("zone").innerHTML = enteteSch() +
    (!ls && !SCH.etat.texte ? '<div class="bloc">' + bulleMark(T("sch_mark_s")) + '</div>' : "") +
    '<div class="bloc">' +
      '<p class="consigne" lang="de">' + esc(ls ? T("sch_ecrire_ls_de", {p: destinataire}) : T("sch_ecrire_s_de")) +
        '<span class="fr">' + esc(ls ? T("sch_ecrire_ls", {p: destinataire}) : T("sch_ecrire_s")) + '</span></p>' +
      situation() + docRecu() + points +
      '<p class="petit">' + esc(T("sch_tu_reponds")) + '</p>' +
      '<p class="petit">' + esc(T(ls ? "sch_longueur_ls" : "sch_longueur_s")) + '</p>' +
      '<p class="petit">' + esc(T(ls ? "sch_temps_ls" : "sch_temps_s")) + '</p>' +
      '<div class="sch-rangee"><button class="secondaire" id="schChrono" type="button">' + esc(T(ls ? "sch_chrono_ls" : "sch_chrono_s")) + '</button>' +
        '<button class="secondaire" id="schFormules" type="button">' + esc(T("sch_formules")) + '</button></div>' +
      '<p class="sch-temps" id="schTemps" hidden>' + esc(T("sch_temps_fini")) + '</p>' +
    '</div>' +
    '<div class="bloc"><h2>' + esc(T("sch_ton_texte")) + '</h2>' +
      '<textarea class="sch-zone' + (ls ? "" : " court") + '" id="schTexte" lang="de" spellcheck="false" autocapitalize="sentences" placeholder="' + esc(T("sch_placeholder")) + '"></textarea>' +
      '<div class="sch-compte" id="schCompte"></div></div>';
  const zone = $("schTexte");
  zone.value = SCH.etat.texte || "";
  const compter = () => { $("schCompte").textContent = T("sch_mots", {n: motsDe(zone.value)}); };
  compter();
  zone.oninput = () => { SCH.etat.texte = zone.value; garder(); compter(); };
  $("schChrono").onclick = () => {
    $("schTemps").hidden = true;
    if (ls) chrono(SCH.d.temps.ls_conseil_min * 60, "bas", () => { $("schTemps").hidden = false; });
    else chrono(SCH.d.temps.s_min * 60, "bas", () => { $("schTemps").hidden = false; });
  };
  $("schFormules").onclick = formules;
  suite(T("sch_verifier"), () => {
    if (motsDe(zone.value) === 0){ ouvrir('<p><b>' + esc(T("sch_vide")) + '</b></p><button class="secondaire" id="okP">' + esc(T("continuer")) + '</button>'); $("okP").onclick = fermerPanneau; return; }
    arreterChrono(); pageSuivante();
  });
}

// les formules utiles, dans le panneau ; celles du registre de la serie d'abord marquees
function formules(){
  const reg = r => r === "du" ? T("sch_reg_du") : r === "Sie" ? T("sch_reg_sie") : T("sch_reg_beide");
  ouvrir('<div class="sch-form"><h2>' + esc(T("sch_formules")) + '</h2><p class="petit">' + esc(T("sch_formules_note")) + '</p>' +
    SCH.d.redemittel.map(g => '<h3>' + esc(trS(g)) + '</h3><ul>' + g.items.map(it =>
      '<li><span class="de" lang="de">' + esc(it.de) + '<span class="reg">' + esc(reg(it.reg)) + '</span></span><span class="tr">' + esc(trS(it)) + '</span></li>').join("") + '</ul>').join("") +
    '</div><button class="secondaire" id="fermerP">' + esc(T("fermer")) + '</button>');
  $("fermerP").onclick = fermerPanneau;
}

// ============ CE QUE LA PAGE VOIT ============
const LETTRE = "\\p{L}";
function motsDe(t){ return String(t || "").split(/\s+/).filter(w => /\p{L}/u.test(w)).length; }
// un mot entier, insensible a la casse, lettres accentuees comprises (\b ne connait pas l'allemand)
function motRe(m, drapeaux){ return new RegExp("(^|[^" + LETTRE + "])(" + m + ")(?![" + LETTRE + "])", drapeaux || "iu"); }
const SUBORD = ["weil", "dass", "wenn", "ob", "obwohl", "damit", "als", "bevor", "nachdem", "während", "falls"];
const COORD = ["und", "aber", "oder", "denn", "deshalb", "trotzdem", "dann", "außerdem", "zwar", "sondern"];

function analyser(texte){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const lignes = texte.split(/\n/).map(l => l.trim()).filter(Boolean);
  const bas = texte.toLowerCase();
  const out = [];   // {c: "ok" | "ko" | "inf", t}
  const n = motsDe(texte);
  out.push({ c: "inf", t: T("sch_v_mots", {n}) });
  if (ls ? n < 30 : n < 2) out.push({ c: "ko", t: T(ls ? "sch_v_court_ls" : "sch_v_court_s") });
  if (ls ? n > 160 : n > 60) out.push({ c: "inf", t: T("sch_v_long") });
  // la formule d'appel et la salutation
  const anrede = lignes.length ? lignes[0].match(/^(liebe[rs]?|hallo|hi|sehr geehrte[rs]?|guten tag|moin|servus)\b[^,\n]*/i) : null;
  out.push(anrede ? { c: "ok", t: T("sch_v_anrede_ok", {m: anrede[0].trim()}) } : { c: "ko", t: T("sch_v_anrede_ko") });
  const fin = lignes.slice(-3).join(" \n ");
  const gruss = fin.match(/(mit freundlichen grüßen|mit freundlichen grüssen|(viele|liebe|herzliche|beste|schöne) grü(ß|ss)e[^\n]*|bis (bald|morgen|dann|sonntag|samstag|später)|tschüss|ciao)/i);
  out.push(gruss ? { c: "ok", t: T("sch_v_gruss_ok", {m: gruss[0].trim()}) } : { c: "ko", t: T("sch_v_gruss_ko") });
  if (gruss && s.registre === "informel" && /mit freundlichen/i.test(gruss[0])) out.push({ c: "inf", t: T("sch_v_gruss_froid") });
  // le registre : Sie au milieu d'une phrase dans un texte qui tutoie, du dans un texte qui vouvoie
  if (s.registre === "informel"){
    const m = texte.match(/[^.!?:\n]\s+(Sie|Ihnen|Ihr|Ihre|Ihren|Ihrem|Ihrer)(?![\p{L}])/u);
    out.push(m ? { c: "ko", t: T("sch_v_sie_informel", {m: m[1]}) } : { c: "ok", t: T("sch_v_registre_ok", {r: "du"}) });
  } else {
    const m = texte.match(motRe("du|dich|dir|dein|deine|deinen|deinem|deiner|euch|euer"));
    out.push(m ? { c: "ko", t: T("sch_v_du_formel", {m: m[2]}) } : { c: "ok", t: T("sch_v_registre_ok", {r: "Sie"}) });
  }
  // les connecteurs
  const trouves = SUBORD.concat(COORD).filter(c => motRe(c).test(texte));
  out.push(trouves.length ? { c: "ok", t: T("sch_v_conn", {m: trouves.join(", ")}) } : { c: "ko", t: T("sch_v_conn_aucun") });
  const subs = SUBORD.filter(c => motRe(c).test(texte));
  out.push(subs.length ? { c: "ok", t: T("sch_v_sub") } : { c: "inf", t: T("sch_v_sub_aucune") });
  if (/\?/.test(texte)) out.push({ c: "ok", t: T("sch_v_question") });
  // les points (LS) ou la question (S) : des indices seulement
  const indice = l => (l || []).some(x => { try{ return new RegExp(x, "iu").test(bas); }catch(e){ return false; } });
  if (ls){
    s.punkte.forEach(p => out.push(indice(p.indices) ? { c: "ok", t: p.de + " — " + T("sch_v_point_ok") } : { c: "inf", t: p.de + " — " + T("sch_v_point_ko") }));
  } else {
    const f = T("sch_frage_" + s.frage.replace(" ", "_"));
    out.push(indice(s.indices) ? { c: "ok", t: T("sch_v_frage_ok", {f}) } : { c: "inf", t: T("sch_v_frage_ko", {f, c: trS(s, "conseil")}) });
  }
  return out;
}

// ============ LA GRILLE ============
const PALIERS = ["b1p", "b1", "a2p", "a2", "moins"];
function ptsCritere(id, palier){
  const b = SCH.d.bareme, k = PALIERS.indexOf(palier);
  if (k < 0) return null;
  if (id === "I") return (SCH.mode === "LS" ? b.email_I : b.kurz_I)[k];
  return b.ensemble[k];
}
function surSch(){ const b = SCH.d.bareme; return (SCH.mode === "LS" ? b.email_I[0] : b.kurz_I[0]) + 3 * b.ensemble[0]; }
// l'estimation, quand les quatre criteres sont choisis : {points, sur, niveau}
function estimation(){
  const c = SCH.etat.crit || {};
  if (!SCH.d.kriterien.every(k => c[k.id])) return null;
  const points = SCH.d.kriterien.reduce((t, k) => t + ptsCritere(k.id, c[k.id]), 0), sur = surSch();
  // les seuils du telc (FORMAT-TELC.md) : B1 a 70 %, A2 a 40 %
  const niveau = points >= 0.7 * sur ? "b1" : points >= 0.4 * sur ? "a2" : "moins";
  return { points, sur, niveau };
}

function pageVerifier(){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const v = analyser(SCH.etat.texte || "");
  const coches = ls ? '<div class="q"><div class="frage">' + esc(T("sch_coche")) + '</div>' + s.punkte.map((p, k) =>
      '<label class="sch-coche"><input type="checkbox" data-coche="' + k + '"' + (SCH.etat.coches.includes(k) ? " checked" : "") + '><span><span lang="de">' + esc(p.de) + '</span><br><span class="petit">' + esc(trS(p)) + '</span></span></label>').join("") + '</div>' : "";
  const crit = SCH.d.kriterien.map(k => {
    const pris = (SCH.etat.crit || {})[k.id];
    return '<div class="sch-crit"><h3>' + esc(trS(k)) + '<small lang="de">' + esc(k.de) + '</small></h3>' +
      '<p class="sch-desc"><b>' + esc(T("sch_desc_b1")) + '</b> · ' + esc(trS(k, "b1")) + '</p>' +
      '<p class="sch-desc"><b>' + esc(T("sch_desc_a2")) + '</b> · ' + esc(trS(k, "a2")) + '</p>' +
      '<p class="sch-desc"><b>' + esc(T("sch_desc_moins")) + '</b> · ' + esc(trS(k, "moins")) + '</p>' +
      '<div class="sch-niv">' + PALIERS.map(p => '<button type="button" data-crit="' + k.id + '" data-p="' + p + '" class="' + (pris === p ? "pris" : "") + '" aria-pressed="' + (pris === p) + '">' + esc(T("sch_" + p)) + ' · ' + ptsCritere(k.id, p) + '</button>').join("") + '</div></div>';
  }).join("");
  $("zone").innerHTML = enteteSch() +
    '<div class="bloc"><h2>' + esc(T("sch_ton_texte")) + '</h2><div class="sch-texte" lang="de">' + esc(SCH.etat.texte || "") + '</div></div>' +
    '<div class="bloc"><h2>' + esc(T("sch_voit")) + '</h2><p class="petit">' + esc(T("sch_voit_s")) + '</p><ul class="sch-v">' +
      v.map(x => '<li class="' + x.c + '"><b>' + (x.c === "ok" ? "✓" : x.c === "ko" ? "✗" : "•") + '</b><span>' + esc(x.t) + '</span></li>').join("") + '</ul></div>' +
    '<div class="bloc"><h2>' + esc(T("sch_grille")) + '</h2><p class="petit">' + esc(T("sch_grille_s")) + '</p>' + coches + crit +
      '<div id="schEstim"></div></div>';
  document.querySelectorAll("[data-coche]").forEach(b => b.onchange = () => {
    const k = Number(b.dataset.coche);
    SCH.etat.coches = SCH.etat.coches.filter(x => x !== k).concat(b.checked ? [k] : []);
    garder(); afficherEstimation();
  });
  document.querySelectorAll("[data-crit]").forEach(b => b.onclick = () => {
    SCH.etat.crit = Object.assign({}, SCH.etat.crit, {[b.dataset.crit]: b.dataset.p}); garder();
    document.querySelectorAll('[data-crit="' + b.dataset.crit + '"]').forEach(x => { const on = x === b; x.classList.toggle("pris", on); x.setAttribute("aria-pressed", on); });
    afficherEstimation();
    document.querySelectorAll(".point")[SCH_PAGES[SCH.mode].findIndex(p => p.id === "verifier")].classList.toggle("ok", !!estimation());
  });
  afficherEstimation();
  suite(T("sch_voir_modeles"), pageSuivante);
}

function afficherEstimation(){
  const e = estimation(), ls = SCH.mode === "LS";
  if (!e){ $("schEstim").innerHTML = '<p class="petit">' + esc(T("sch_remplir")) + '</p>'; return; }
  const manque = ls ? SCH.serie.punkte.length - SCH.etat.coches.length : 0;
  const alerte = ls && manque > 0 && /^b1/.test(SCH.etat.crit.I) ? '<p class="petit">' + esc(T("sch_incoherent", {n: manque})) + '</p>' : "";
  $("schEstim").innerHTML = '<div class="sch-estim"><div class="p">' + esc(T("sch_estimation", {p: e.points, s: e.sur})) + '</div>' +
    '<span class="niveau ' + e.niveau + '">' + esc(T("niv_" + e.niveau)) + '</span>' + alerte +
    '<p class="petit">' + esc(T("sch_estimation_note")) + '</p></div>';
}

// ============ LES LETTRES MODELES ============
// les passages notes sont soulignes et numerotes ; toucher un passage met sa note en avant (et l'inverse)
function modeleHtml(m, prefixe){
  const places = m.notes.map(() => null);
  const html = m.lignes.map((ligne, li) => {
    const ici = [];
    m.notes.forEach((n, j) => {
      if (places[j]) return;
      const pos = ligne.indexOf(n.de);
      if (pos >= 0 && !ici.some(x => pos < x.fin && pos + n.de.length > x.debut)){ ici.push({ debut: pos, fin: pos + n.de.length, j }); places[j] = true; }
    });
    ici.sort((a, b) => a.debut - b.debut);
    let h = "", cur = 0;
    ici.forEach(x => {
      h += esc(ligne.slice(cur, x.debut)) + '<mark data-note="' + prefixe + x.j + '">' + esc(ligne.slice(x.debut, x.fin)) + '</mark><sup>' + (x.j + 1) + '</sup>';
      cur = x.fin;
    });
    return '<p lang="de">' + h + esc(ligne.slice(cur)) + '</p>';
  }).join("");
  return { lettre: '<div class="doc lettre sch-modele" dir="ltr">' + html + '</div>',
    notes: '<ol class="sch-notes">' + m.notes.map((n, j) => '<li data-li="' + prefixe + j + '"><span class="ex" lang="de">' + (SCH_EN ? "“" : "« ") + esc(n.de) + (SCH_EN ? "”" : " »") + '</span> — ' + esc(trS(n)) + '</li>').join("") + '</ol>' };
}

function pageModeles(){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const a2 = modeleHtml(s.modeles.a2, "a"), b1 = modeleHtml(s.modeles.b1, "b");
  const passer = (SCH_EN && s.passer_en) || s.passer_fr || [];
  $("zone").innerHTML = enteteSch() +
    '<div class="bloc"><h2>' + esc(T("sch_modeles")) + '</h2><p class="petit">' + esc(T("sch_modeles_s")) + '</p></div>' +
    (SCH.etat.texte ? '<div class="bloc"><h2>' + esc(T("sch_ton_texte")) + '</h2><div class="sch-texte" lang="de">' + esc(SCH.etat.texte) + '</div></div>' : "") +
    '<div class="bloc"><span class="sch-niveau a2">A2</span><h2>' + esc(T(ls ? "sch_modele_a2" : "sch_message_a2")) + '</h2>' + a2.lettre + a2.notes + '</div>' +
    '<div class="bloc"><span class="sch-niveau b1">B1</span><h2>' + esc(T(ls ? "sch_modele_b1" : "sch_message_b1")) + '</h2>' + b1.lettre + b1.notes + '</div>' +
    '<div class="bloc"><h2>' + esc(T("sch_passer")) + '</h2><ul class="sch-liste">' + passer.map(x => '<li>' + esc(x) + '</li>').join("") + '</ul></div>';
  const allumer = id => {
    document.querySelectorAll(".sch-modele mark, .sch-notes li").forEach(x => x.classList.toggle("actif", x.dataset.note === id || x.dataset.li === id));
  };
  document.querySelectorAll(".sch-modele mark").forEach(m => m.onclick = () => {
    allumer(m.dataset.note);
    const li = document.querySelector('[data-li="' + m.dataset.note + '"]');
    if (li) try{ li.scrollIntoView({block: "center", behavior: "smooth"}); }catch(e){}
  });
  document.querySelectorAll(".sch-notes li").forEach(li => li.onclick = () => allumer(li.dataset.li));
  suite(T("sch_terminer"), recapSch);
}

// ============ LE RECAPITULATIF ============
function recapSch(){
  silence(); arreterChrono(); suite(null);
  const s = SCH.serie, ls = SCH.mode === "LS", e = estimation();
  marquerFait("SCH" + SCH.mode, s);
  const bons = ls ? s.fragen.filter(f => SCH.etat.q[f.n] === f.bon).length : 0;
  resultat(SCH.mode, { serie: s.id, bons: ls ? bons : null, mots: motsDe(SCH.etat.texte), points: e ? e.points : null, sur: e ? e.sur : null, niveau: e ? e.niveau : null });
  parler("fini", { bons: ls ? bons : (e && e.niveau !== "moins" ? 1 : 0), faits: ls ? 2 : 1 });
  const mot = !e ? "sch_mark_moins" : e.niveau === "b1" ? "sch_mark_b1" : e.niveau === "a2" ? "sch_mark_a2" : "sch_mark_moins";
  const ordre = DTZ.parties, k = ordre.findIndex(p => p.id === SCH.mode);
  const suivante = k >= 0 && k + 1 < ordre.length ? ordre[k + 1] : null;
  $("titre").textContent = T(ls ? "ls_titre" : "s_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T(ls ? "ls_section" : "s_section")) + ' · ' + esc(T("sch_recap")) + '</div>' +
      (e ? '<div class="score">' + e.points + '<span style="font-size:18px"> / ' + e.sur + '</span></div><span class="niveau ' + e.niveau + '">' + esc(T("niv_" + e.niveau)) + '</span>'
         : '<p class="petit" style="text-align:center">' + esc(T("sch_pas_estime")) + '</p>') +
      (ls ? '<p class="petit" style="text-align:center">' + esc(T("sch_q_score", {n: bons})) + '</p>' : "") +
      '<p class="petit" style="text-align:center">' + esc(T("sch_mots", {n: motsDe(SCH.etat.texte)})) + '</p>' +
      bulleMark(T(mot)) + '</div>' +
    '<div class="bloc boutons">' +
      '<button class="secondaire" id="schRefaire">' + esc(T("sch_refaire")) + '</button>' +
      '<button class="secondaire" id="schAutre">' + esc(T("sch_autre")) + '</button>' +
      (suivante ? '<button class="secondaire" id="schSuivante">' + esc(T("sch_suivante")) + ' : ' + esc(suivante.titre) + '</button>' : "") +
      '<button class="secondaire" id="schToutes">' + esc(T("sch_toutes")) + '</button></div>';
  // refaire : le meme sujet, page blanche ; un autre sujet : choisirSerie() prend le moins recemment fait
  $("schRefaire").onclick = () => { ecrire("sch_" + SCH.mode + "_" + s.id, {}); ouvrirSchreiben(SCH.mode, s); };
  $("schAutre").onclick = () => ouvrirSchreiben(SCH.mode);
  if (suivante) $("schSuivante").onclick = () => suivante.ouvrir();
  $("schToutes").onclick = toutesLesSectionsSch;
  DTZ.surRetour(() => { toutesLesSectionsSch(); return true; });
  window.scrollTo(0, 0);
}
