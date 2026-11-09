// LE TELC A2·B1 AVEC MARK ET ANNA -- ECRIRE (6 nov. 2026, session « telc Ecrire »).
//
// La partie S du telc, d'apres preparation-examens/FORMAT-TELC.md (le format seul, jamais le contenu) :
// « Schreiben », item 57, a la toute fin de l'ecrit, apres l'ecoute : repondre a un message court qui pose une
// question (wann, was, warum nicht, welches, wie lange, wo, wohin), en plus d'un mot ; 10 minutes ; critere I sur 5.
// S donne aussi les trois criteres d'ensemble de l'ecrit (II Kommunikative Gestaltung, III Formale Richtigkeit,
// IV Spektrum sprachlicher Mittel, 10 points chacun), notes sur le courriel (partie LS) ET la reponse courte.
//
// CE FICHIER PORTE AUSSI LA PARTIE LS (le courriel, items 29-31, donnees/lesen-schreiben.json) et le moteur des
// deux textes de l'ecrit (decision de l'assemblage, 1dbd788 : telc.html ne charge que schreiben.js pour les deux) :
//   LS « Lesen und Schreiben », juste apres les Sprachbausteine (35 minutes pour les deux) : 29 un Richtig/Falsch et
//      30 un choix a 2 sur un courriel recu qui pose des questions (3 points de Lesen chacune), 31 la reponse a ce
//      courriel (critere I, 15 points de Schreiben) ;
//   LS : 29 · 30 · 31 (ecrire) · ✓ (la grille) · M (les lettres modeles A2 et B1, annotees)
//   S  : 57 (ecrire) · ✓ · M
// L'organisation est celle des Sprachbausteine (decision de Jacques du 4 nov.) : une page par exercice,
// « Section · … », des points de progression qu'on touche pour sauter, « ‹ » vers la liste, « Continuer » en bas ;
// en fin de section, un recapitulatif, puis Refaire / Un autre sujet / Section suivante / Toutes les sections.
// En tete de chaque section, « La tache a l'examen » : ce qu'on demande, le temps, les points, comment s'y prendre
// (retour de Marina, l'enseignante, 1er nov. : le cahier du commerce « n'explique pas le format »).
//
// CE QUE LA PAGE NE JUGE PAS, et le dit : ni la grammaire ni l'orthographe. Comme les JUGES de dtz-oral.html, elle
// regarde ce qu'un programme peut voir : la longueur, la formule d'appel et la salutation, le registre (du / Sie,
// assortis au message recu), les connecteurs, des indices de chaque point de la consigne. Le reste, l'eleve le juge
// avec la grille de l'examinateur (criteres I a IV, descriptions B1 / A2 / sous A2), puis il compare aux lettres
// modeles.
//
// Donnees : donnees/schreiben.json (la reponse courte, la grille, le bareme, les formules utiles) et
// donnees/lesen-schreiben.json (les courriels de la partie LS). Controle : python tests/telc_ecrire.py.
// Textes en francais et en anglais (textesTelc, champTelc de telc-commun.js).

"use strict";

// ======================================================================================================
// LA PARTIE LS : LIRE ET ECRIRE, LE COURRIEL (ses textes, ses donnees, sa tuile, son epreuve d'examen blanc)
// ======================================================================================================
const LS_EN = {
  ls_titre: "Reading and writing", ls_sous: "An email to read, then your reply",
  ls_section: "Section · Reading and writing",
  sch_rf_consigne: "Read the email. Is the statement true or false?",
  sch_ab_consigne: "Read the email again. Which answer fits?",
  sch_mark_ls: "In the telc, this email comes right after the Sprachbausteine: two questions to check you have understood it, then you reply to it. Those two questions help you: they show you what the email is asking for.",
  sch_ecrire_ls: "Reply to {p}. Write something for each question. Don't forget the opening and the closing.",
  sch_points_titre: "The points to cover",
  sch_longueur_ls: "The exam sets no word count: what matters is answering every question. Wortando's guide: about 40 to 80 words at A2, 80 to 120 at B1.",
  sch_temps_ls: "In the exam, this part and the Sprachbausteine share 35 minutes: allow about 20 minutes for this email.",
  sch_chrono_ls: "Start the timer (20 min suggested)",
  sch_v_court_ls: "That is short for answering every question.",
  sch_q_score: "Questions 29 and 30: {n} out of 2",
  sch_modele_a2: "A2 model letter", sch_modele_b1: "B1 model letter",
  ls_t_quoi: "You read an email (from a friend, a colleague, a neighbour, a school) that asks 3 or 4 questions. First two comprehension questions: 29 true or false, 30 a choice between two answers. Then you reply to the email (31): an answer to each question, with an opening and a closing.",
  ls_t_temps: "35 minutes for the Sprachbausteine, this email and your reply together. Allow about 20 minutes for writing.",
  ls_t_points: "29 and 30 are worth 3 reading points each. Your reply is worth up to 15 points for the task (criterion I), and it also counts, together with the short reply at the end, in criteria II to IV (30 points).",
  ls_t_e1: "Underline every question in the email (every “?”): those are your points.",
  ls_t_e2: "Choose du or Sie from the opening you received (Lieber Tobias / Sehr geehrte Frau …).",
  ls_t_e3: "Opening, then one sentence that reacts to the email (thanks, good news, sorry…).",
  ls_t_e4: "One paragraph per question, each with a reason or a detail (weil, denn, deshalb, wenn).",
  ls_t_e5: "An offer or a question back, then the closing and your name.",
  ls_t_e6: "Keep 2 or 3 minutes to check: verb in second place, verb at the end after weil and dass, capital letters on nouns.",
  ls_ex_rendre: "Hand in my email",
  ls_ex_note: "Mark your email for the task (criterion I). Criteria II to IV will be marked with the short reply, at the end of the written exam."
};
textesTelc({ en: LS_EN, fr: {
  ls_titre: "Lire et écrire", ls_sous: "Un courriel à lire, puis ta réponse",
  ls_section: "Section · Lire et écrire",
  sch_rf_consigne_de: "Lesen Sie die E-Mail. Ist die Aussage richtig oder falsch?",
  sch_rf_consigne: "Lis le courriel. L'affirmation est-elle juste ou fausse ?",
  sch_ab_consigne_de: "Lesen Sie die E-Mail noch einmal. Welche Antwort passt?",
  sch_ab_consigne: "Relis le courriel. Quelle réponse convient ?",
  sch_richtig: "Richtig", sch_falsch: "Falsch",
  sch_mark_ls: "Au telc, ce courriel arrive juste après les Sprachbausteine : deux questions pour vérifier que tu l'as compris, puis tu y réponds. Les deux questions t'aident : elles te montrent ce que le courriel demande.",
  sch_ecrire_ls_de: "Antworten Sie {p}. Schreiben Sie zu jeder Frage etwas. Vergessen Sie Anrede und Gruß nicht.",
  sch_ecrire_ls: "Réponds à {p}. Écris quelque chose pour chaque question. N'oublie ni la formule d'appel ni la salutation.",
  sch_points_titre: "Les points à traiter",
  sch_longueur_ls: "Le modèle d'examen ne fixe pas de nombre de mots : ce qui compte, c'est de répondre à chaque question. Repère de Wortando : environ 40 à 80 mots au A2, 80 à 120 au B1.",
  sch_temps_ls: "À l'examen, cette partie et les Sprachbausteine ont 35 minutes ensemble : compte environ 20 minutes pour ce courriel.",
  sch_chrono_ls: "Lancer le chrono (20 min conseillées)",
  sch_v_court_ls: "C'est court pour répondre à toutes les questions.",
  sch_q_score: "Questions 29 et 30 : {n} sur 2",
  sch_modele_a2: "Lettre modèle A2", sch_modele_b1: "Lettre modèle B1",
  // LA TACHE EN BREF (retour de Marina, 1er nov. : le cahier du commerce « n'explique pas le format ») : ce qu'on
  // demande, le temps, les points, comment s'y prendre
  ls_t_quoi: "Tu lis un courriel (d'un ami, d'un collègue, d'une voisine, d'une école) qui pose 3 ou 4 questions. D'abord deux questions de compréhension : 29 juste ou faux, 30 un choix entre deux réponses. Puis tu réponds à ce courriel (31) : une réponse à chaque question, avec une formule d'appel et une salutation.",
  ls_t_temps: "35 minutes pour les Sprachbausteine, ce courriel et ta réponse ensemble. Compte environ 20 minutes pour écrire.",
  ls_t_points: "29 et 30 valent 3 points de lecture chacune. Ta réponse vaut jusqu'à 15 points pour la tâche (critère I), et elle compte aussi, avec la réponse courte de la fin, dans les critères II à IV (30 points).",
  ls_t_e1: "Souligne chaque question du courriel (chaque « ? ») : ce sont tes points.",
  ls_t_e2: "Choisis du ou Sie d'après la formule d'appel reçue (Lieber Tobias / Sehr geehrte Frau …).",
  ls_t_e3: "La formule d'appel, puis une phrase qui réagit au courriel (merci, bonne nouvelle, désolé…).",
  ls_t_e4: "Un paragraphe par question, chacun avec une raison ou un détail (weil, denn, deshalb, wenn).",
  ls_t_e5: "Une proposition ou une question en retour, puis la salutation et ton nom.",
  ls_t_e6: "Garde 2 ou 3 minutes pour relire : le verbe en 2e place, le verbe à la fin après weil et dass, les majuscules des noms.",
  ls_ex_rendre: "Rendre mon courriel",
  ls_ex_note: "Note ton courriel pour la tâche (critère I). Les critères II à IV se noteront avec la réponse courte, à la fin de l'écrit."
}});

const LS_DONNEES = { series: [] };

DTZ.charger(fetch("donnees/lesen-schreiben.json", { cache: "no-cache" })
  .then(r => { if (!r.ok) throw new Error("lesen-schreiben.json"); return r.json(); })
  .then(d => { LS_DONNEES.series = d.series || []; }));

DTZ.partie({ id: "LS", ordre: 30, titre: T("ls_titre"), sous: T("ls_sous"), ouvrir: () => ouvrirSchreiben("LS") });

// L'EXAMEN BLANC : 29 et 30 comptent en Lesen (3 points chacune), le courriel 31 en Schreiben (critere I, 15, note par
// la grille hors chrono, a la fin de l'examen).
// « minutes : 0 » : la partie partage les 35 minutes des Sprachbausteine.
TELC.epreuve({ id: "LS", ordre: 30, minutes: 0, sur: { Lesen: 6, Schreiben: 15 },
  lancer: (fini, o) => examenSchreiben("LS", fini, o), grille: (finiGrille, o) => grilleSchreiben("LS", finiGrille, o) });

// ======================================================================================================
// LA PARTIE S : ECRIRE, LA REPONSE COURTE, ET LE MOTEUR COMMUN AUX DEUX TEXTES
// ======================================================================================================
const SCH_EN = LANGUE === "en";

const S_EN = {
  s_titre: "Write", s_sous: "A short message, 10 minutes",
  s_section: "Section · Write",
  sch_situation: "The situation:",
  sch_de: "From:", sch_a: "To:",
  sch_juste: "Correct!", sch_faux: "Not quite.",
  sch_mark_s: "This is the very last task of the written exam, after the listening: 10 minutes to reply to a short message. Look at the question word first (wann, warum, wohin…): your answer must answer it, in more than one word.",
  sch_ecrire_s: "You receive this message. Reply to it, in more than one word.",
  sch_tu_reponds: "You are replying for Mark: make up any details you need.",
  sch_longueur_s: "Wortando's guide: two sentences at A2 (10 to 20 words), three or four at B1 (20 to 40 words).",
  sch_temps_s: "In the exam: 10 minutes.",
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
  sch_v_court_s: "In the telc, you must write more than one word.",
  sch_v_long: "That is long: check it over rather than adding more.",
  sch_v_anrede_ok: "Opening: “{m}”.",
  sch_v_anrede_ko: "No opening at the start (Liebe …, Hallo …, Sehr geehrte …).",
  sch_v_gruss_ok: "Closing at the end: “{m}”.",
  sch_v_gruss_ko: "No closing at the end (Viele Grüße, Liebe Grüße, Mit freundlichen Grüßen…).",
  sch_v_gruss_froid: "“Mit freundlichen Grüßen” is a bit cold for a friend: “Viele Grüße” or “Liebe Grüße” will fit better.",
  sch_v_sie_informel: "Are you saying du? The text has “{m}” in the middle of a sentence: that is the formal Sie. Keep the same register throughout.",
  sch_v_du_formel: "The message uses Sie, and your text has “{m}”: keep “Sie” throughout.",
  sch_v_registre_ok: "The register ({r}) seems to hold from start to finish.",
  sch_v_conn: "Linking words found: {m}.",
  sch_v_conn_aucun: "No linking words found: connect your sentences (und, aber, denn, weil, dass…).",
  sch_v_sub: "Subordinate clauses (weil, dass, wenn, ob…): a B1 feature.",
  sch_v_sub_aucune: "No subordinate clause yet (weil, dass, wenn, ob…): this is often what takes you to B1.",
  sch_v_question: "A question back: the exchange goes on.",
  sch_v_point_ok: "seems covered",
  sch_v_point_ko: "to check",
  sch_v_frage_ok: "The question “{f}” seems to have its answer.",
  sch_v_frage_ko: "I can't see an obvious answer to “{f}”. {c}",
  sch_grille: "The grid: you be the judge",
  sch_grille_s: "Read your text again against each description, then choose. This is the examiner's grid, simplified.",
  sch_coche: "I have answered:",
  sch_b1p: "B1, fully", sch_b1: "B1, mostly", sch_a2p: "A2, fully", sch_a2: "A2, mostly", sch_moins: "Not A2 yet",
  sch_desc_b1: "B1", sch_desc_a2: "A2", sch_desc_moins: "Below A2",
  sch_estimation: "Estimate for this text: {p} out of {s}",
  sch_estimation_note: "In the exam, writing is worth 60 points: the Sprachbausteine (5), the email (15), the voicemail notes (5), the short message (5) and criteria II to IV for both texts together (30). Here, this text alone.",
  sch_remplir: "Choose a level for all four criteria to see the estimate.",
  sch_incoherent: "You chose B1 for the task, but {n} point(s) are not ticked: at B1, every question gets an answer.",
  sch_voir_modeles: "See the model letters",
  sch_modeles: "Two model letters",
  sch_modeles_s: "The same questions, two levels. Tap an underlined passage to read the note.",
  sch_message_a2: "A2 model reply", sch_message_b1: "B1 model reply",
  sch_passer: "What takes you from A2 to B1",
  sch_terminer: "Finish the section",
  sch_recap: "Summary",
  sch_pas_estime: "No estimate: the grid has not been filled in.",
  sch_mark_b1: "Well done, that is a B1 text! Keep the habit: a reason or a detail for every question.",
  sch_mark_a2: "That is a good A2. To aim for B1, read the B1 model letter again: every answer there gets a reason, linked with weil, dass or wenn.",
  sch_mark_moins: "It's a start. Go through the points to cover one by one: a full sentence for each, an opening, a closing. That is what the useful phrases are for.",
  sch_refaire: "Redo the section", sch_suivante: "Next section", sch_toutes: "All sections",
  sch_autre: "Another topic",
  sch_reg_du: "du", sch_reg_sie: "Sie", sch_reg_beide: "du or Sie",
  sch_formules_note: "Phrases marked “du” go with the informal register, those marked “Sie” with the formal one.",
  sch_t_titre: "In the exam: the task in brief",
  sch_t_quoi: "What you have to do", sch_t_temps: "Time", sch_t_points: "Points", sch_t_comment: "How to go about it",
  s_t_quoi: "You receive a short message (a text, a note, an email) that asks one question: wann, was, warum nicht, welches, wie lange, wo or wohin. You reply in a few sentences; one word is not enough.",
  s_t_temps: "10 minutes, at the very end of the written exam, after the listening.",
  s_t_points: "5 points for your reply (criterion I). Together with your email, it also counts in criteria II to IV (30 points).",
  s_t_e1: "Find the question word: your first sentence answers it.",
  s_t_e2: "Add a reason or a detail (weil, denn, deshalb), or a question back.",
  s_t_e3: "Opening and closing; du or Sie, like the message.",
  s_t_e4: "Read it through once: the verb in the right place, capital letters on nouns.",
  sch_ex_rendre: "Hand in my reply",
  sch_ex_valider: "Confirm my marks",
  sch_ex_note_s: "Mark your reply for the task (criterion I), then criteria II to IV on your two texts together, as the examiner does.",
  sch_ex_note_seul: "Mark your reply for the task (criterion I), then criteria II to IV (here on this text alone, since the email was not written in this mock exam).",
  sch_ex_ton_courriel: "Your email (31)", sch_ex_ta_reponse: "Your short reply (57)",
  sch_ex_pas_aide: "Mock exam: no help, no hints. The page does not mark grammar: you mark yourself with the examiner's grid."
};
textesTelc({ en: S_EN, fr: {
  s_titre: "Écrire", s_sous: "Un message court, 10 minutes",
  s_section: "Section · Écrire",
  sch_situation: "La situation :",
  sch_de: "De :", sch_a: "À :",
  sch_juste: "Juste !", sch_faux: "Pas tout à fait.",
  sch_mark_s: "C'est la toute dernière tâche de l'écrit, après l'écoute : 10 minutes pour répondre à un message court. Regarde d'abord le mot interrogatif (wann, warum, wohin…) : ta réponse doit lui répondre, en plus d'un mot.",
  sch_ecrire_s_de: "Sie bekommen diese Nachricht. Antworten Sie. Schreiben Sie mehr als ein Wort.",
  sch_ecrire_s: "Tu reçois ce message. Réponds-y, en plus d'un mot.",
  sch_tu_reponds: "Tu réponds à la place de Mark : invente les détails qu'il te faut.",
  sch_longueur_s: "Repère de Wortando : deux phrases au A2 (10 à 20 mots), trois ou quatre au B1 (20 à 40 mots).",
  sch_temps_s: "À l'examen : 10 minutes.",
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
  sch_message_a2: "Réponse modèle A2", sch_message_b1: "Réponse modèle B1",
  sch_passer: "Ce qui fait passer de A2 à B1",
  sch_terminer: "Terminer la section",
  sch_recap: "Récapitulatif",
  sch_pas_estime: "Pas d'estimation : la grille n'est pas remplie.",
  sch_mark_b1: "Bravo, c'est un texte de niveau B1 ! Garde ce réflexe : une raison ou un détail pour chaque question.",
  sch_mark_a2: "C'est un bon A2. Pour viser le B1, relis la lettre modèle B1 : chaque réponse y reçoit une raison, reliée par weil, dass ou wenn.",
  sch_mark_moins: "C'est un début. Reprends les points à traiter un par un : une phrase complète pour chacun, une formule d'appel, une salutation. Les formules utiles sont là pour ça.",
  sch_refaire: "Refaire la section", sch_suivante: "Section suivante", sch_toutes: "Toutes les sections",
  sch_autre: "Un autre sujet",
  sch_reg_du: "du", sch_reg_sie: "Sie", sch_reg_beide: "du ou Sie",
  sch_formules_note: "Les tournures marquées « du » vont avec le tutoiement, celles marquées « Sie » avec le vouvoiement.",
  sch_frage_wann: "Wann?", sch_frage_was: "Was?", sch_frage_warum_nicht: "Warum nicht?", sch_frage_welches: "Welches?", sch_frage_wie_lange: "Wie lange?", sch_frage_wo: "Wo?", sch_frage_wohin: "Wohin?",
  // LA TACHE EN BREF (retour de Marina, 1er nov.)
  sch_t_titre: "À l'examen : la tâche en bref",
  sch_t_quoi: "Ce qu'on demande", sch_t_temps: "Le temps", sch_t_points: "Les points", sch_t_comment: "Comment s'y prendre",
  s_t_quoi: "Tu reçois un message court (un SMS, un mot, un courriel) qui pose une question : wann, was, warum nicht, welches, wie lange, wo ou wohin. Tu y réponds en quelques phrases ; un seul mot ne suffit pas.",
  s_t_temps: "10 minutes, à la toute fin de l'écrit, après l'écoute.",
  s_t_points: "5 points pour ta réponse (critère I). Avec ton courriel, elle compte aussi dans les critères II à IV (30 points).",
  s_t_e1: "Repère le mot interrogatif : ta première phrase y répond.",
  s_t_e2: "Ajoute une raison ou un détail (weil, denn, deshalb), ou une question en retour.",
  s_t_e3: "Formule d'appel et salutation ; du ou Sie, comme le message.",
  s_t_e4: "Relis une fois : le verbe à sa place, les majuscules des noms.",
  // L'EXAMEN BLANC
  sch_ex_rendre: "Rendre ma réponse",
  sch_ex_valider: "Valider mes notes",
  sch_ex_note_s: "Note ta réponse pour la tâche (critère I), puis les critères II à IV sur tes deux textes ensemble, comme l'examinateur.",
  sch_ex_note_seul: "Note ta réponse pour la tâche (critère I), puis les critères II à IV (ici sur ce texte seul : le courriel n'a pas été écrit dans cet examen blanc).",
  sch_ex_ton_courriel: "Ton courriel (31)", sch_ex_ta_reponse: "Ta réponse courte (57)",
  sch_ex_pas_aide: "Examen blanc : sans aide ni indice. La page ne note pas la grammaire : tu te notes toi-même avec la grille de l'examinateur."
}});

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
    ".sch-texte{white-space:pre-wrap;direction:ltr;text-align:left;background:var(--papier);border:1px solid var(--papier-trait);border-radius:10px;padding:10px 12px;font-size:14px;line-height:1.55}" +
    ".sch-tache{background:var(--carte);border-radius:16px;padding:10px 12px}" +
    ".sch-tache summary{font-weight:900;cursor:pointer;font-size:15px}" +
    ".sch-tache h3{margin:10px 0 2px;font-size:13px;font-weight:900;text-transform:uppercase;letter-spacing:.04em;color:var(--ambre-f)}" +
    ".sch-tache p{font-weight:600;font-size:14px;line-height:1.5}" +
    ".sch-tache ol{margin:2px 0 0;padding-left:20px;font-weight:600;font-size:14px;line-height:1.5;display:flex;flex-direction:column;gap:3px}";
  document.head.appendChild(st);
})();

// SCH.d : donnees/schreiben.json (la reponse courte, la grille, le bareme, les formules) ;
// les courriels : LS_DONNEES.series (partie LS, plus haut)
const SCH = { d: null, mode: null, serie: null, i: 0, etat: null, ex: null, courrielExamen: null };

DTZ.charger(fetch("donnees/schreiben.json", { cache: "no-cache" })
  .then(r => { if (!r.ok) throw new Error("schreiben.json"); return r.json(); })
  .then(d => { SCH.d = d; }));

DTZ.partie({ id: "S", ordre: 60, titre: T("s_titre"), sous: T("s_sous"), ouvrir: () => ouvrirSchreiben("S") });

// L'EXAMEN BLANC : la reponse courte (critere I, 5) et les criteres II-IV de l'ecrit sur les deux textes (30).
TELC.epreuve({ id: "S", ordre: 60, minutes: 10, sur: { Schreiben: 35 },
  lancer: (fini, o) => examenSchreiben("S", fini, o), grille: (finiGrille, o) => grilleSchreiben("S", finiGrille, o) });

// les pages de chaque partie, dans l'ordre ; le libelle de leur point de progression
const SCH_PAGES = {
  LS: [{id: "q29", pt: "29"}, {id: "q30", pt: "30"}, {id: "ecrire", pt: "31"}, {id: "verifier", pt: "✓"}, {id: "modeles", pt: "M"}],
  S: [{id: "ecrire", pt: "57"}, {id: "verifier", pt: "✓"}, {id: "modeles", pt: "M"}]
};
const seriesDe = mode => mode === "LS" ? (LS_DONNEES.series) : SCH.d.series;

// ============ L'OUVERTURE ============
async function ouvrirSchreiben(mode, serie){
  SCH.mode = mode; SCH.ex = null;
  SCH.serie = serie || await choisirSerie(seriesDe(mode), () => [], "SCH" + mode);
  // ce que l'eleve a deja fait sur ce sujet (son texte, ses reponses, sa grille) reste la quand il revient
  SCH.etat = Object.assign({ q: {}, texte: "", coches: [], crit: {} }, lire("sch_" + mode + "_" + SCH.serie.id, {}));
  SCH.i = 0;
  DTZ.surRetour(() => { toutesLesSectionsSch(); return true; });
  page();
}
function garder(){ ecrire("sch_" + SCH.mode + "_" + SCH.serie.id, SCH.etat); }

function toutesLesSectionsSch(){
  arreterChrono();
  // ouverte directement sur cette partie depuis le panneau du bloc telc (TELC.direct) : on ferme le cadre
  if (TELC.direct){ silence(); parler("fermer"); if (window.parent === window) accueil(); return; }
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
  return '<div class="bloc"><div class="section">' + esc(T(SCH.mode === "LS" ? "ls_section" : "s_section")) + '</div>' + pointsSch() + (SCH.i === 0 ? TELC.noteEntrainement() : "") + '</div>';
}

function bulleMark(texte){
  return '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(texte) + '</div></div>';
}

// LA TACHE A L'EXAMEN : ce qu'on demande, le temps, les points, comment s'y prendre. Ouverte a la premiere visite
// d'une section, repliee ensuite.
function tacheHtml(ouverte){
  const p = SCH.mode === "LS" ? "ls" : "s", n = SCH.mode === "LS" ? 6 : 4;
  const etapes = []; for (let k = 1; k <= n; k++) etapes.push('<li>' + esc(T(p + "_t_e" + k)) + '</li>');
  return '<details class="sch-tache"' + (ouverte ? " open" : "") + '><summary>' + esc(T("sch_t_titre")) + '</summary>' +
    '<h3>' + esc(T("sch_t_quoi")) + '</h3><p>' + esc(T(p + "_t_quoi")) + '</p>' +
    '<h3>' + esc(T("sch_t_temps")) + '</h3><p>' + esc(T(p + "_t_temps")) + '</p>' +
    '<h3>' + esc(T("sch_t_points")) + '</h3><p>' + esc(T(p + "_t_points")) + '</p>' +
    '<h3>' + esc(T("sch_t_comment")) + '</h3><ol>' + etapes.join("") + '</ol></details>';
}
function rienFait(){ return !SCH.etat.texte && Object.keys(SCH.etat.q).length === 0; }

// le message recu, mis en page comme les lettres des Sprachbausteine (jamais en image)
function docRecu(mode, s){
  if (mode === "LS"){
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

function situation(s){
  return '<p class="petit"><b>' + esc(T("sch_situation")) + '</b> ' + esc(champTelc(s, "situation")) + '</p>';
}
const destinataire = (mode, s) => mode === "LS" ? s.mail.von.split(",")[0] : s.nachricht.von;
const consigneEcrire = (mode, s) => '<p class="consigne" lang="de">' +
  esc(mode === "LS" ? T("sch_ecrire_ls_de", {p: destinataire(mode, s)}) : T("sch_ecrire_s_de")) +
  '<span class="fr">' + esc(mode === "LS" ? T("sch_ecrire_ls", {p: destinataire(mode, s)}) : T("sch_ecrire_s")) + '</span></p>';

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
  b.hidden = !libelle; b.disabled = false; if (!libelle) return;
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
    '<div class="dit"><img src="' + MARK_IMG + '" alt="Mark"><span class="erkl">' + esc(champTelc(f, "erkl")) + '</span></div></div>';
  const premier = SCH.i === 0 && rienFait();
  $("zone").innerHTML = enteteSch() +
    (SCH.i === 0 ? '<div class="bloc">' + (premier ? bulleMark(T("sch_mark_ls")) : "") + tacheHtml(premier) + '</div>' : "") +
    '<div class="bloc"><p class="consigne" lang="de">' + esc(T(f.typ === "rf" ? "sch_rf_consigne_de" : "sch_ab_consigne_de")) +
      '<span class="fr">' + esc(T(f.typ === "rf" ? "sch_rf_consigne" : "sch_ab_consigne")) + '</span></p>' + situation(SCH.serie) + docRecu("LS", SCH.serie) +
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
  const points = ls
    ? '<div class="q"><div class="frage">' + esc(T("sch_points_titre")) + '</div><ol class="sch-liste">' +
        s.punkte.map(p => '<li><span class="de" lang="de">' + esc(p.de) + '</span><span class="tr">' + esc(champTelc(p, "aide")) + '</span></li>').join("") + '</ol></div>'
    : '<div class="q"><div class="frage" lang="de">' + esc(T("sch_frage_" + s.frage.replace(" ", "_"))) + '</div><p class="petit">' + esc(champTelc(s, "conseil")) + '</p></div>';
  const premier = !ls && rienFait();
  $("zone").innerHTML = enteteSch() +
    '<div class="bloc">' + (premier ? bulleMark(T("sch_mark_s")) : "") + tacheHtml(premier) + '</div>' +
    '<div class="bloc">' + consigneEcrire(SCH.mode, s) + situation(s) + docRecu(SCH.mode, s) + points +
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
    chrono((ls ? SCH.d.temps.ls_conseil_min : SCH.d.temps.s_min) * 60, "bas", () => { $("schTemps").hidden = false; });
  };
  $("schFormules").onclick = formules;
  suite(T("sch_verifier"), () => {
    if (motsDe(zone.value) === 0){ ouvrir('<p><b>' + esc(T("sch_vide")) + '</b></p><button class="secondaire" id="okP">' + esc(T("continuer")) + '</button>'); $("okP").onclick = fermerPanneau; return; }
    arreterChrono(); pageSuivante();
  });
}

// les formules utiles, dans le panneau, marquees du / Sie
function formules(){
  const reg = r => r === "du" ? T("sch_reg_du") : r === "Sie" ? T("sch_reg_sie") : T("sch_reg_beide");
  ouvrir('<div class="sch-form"><h2>' + esc(T("sch_formules")) + '</h2><p class="petit">' + esc(T("sch_formules_note")) + '</p>' +
    SCH.d.redemittel.map(g => '<h3>' + esc(champTelc(g, "titre")) + '</h3><ul>' + g.items.map(it =>
      '<li><span class="de" lang="de">' + esc(it.de) + '<span class="reg">' + esc(reg(it.reg)) + '</span></span><span class="tr">' + esc(champTelc(it, "sens")) + '</span></li>').join("") + '</ul>').join("") +
    '</div><button class="secondaire" id="fermerP">' + esc(T("fermer")) + '</button>');
  $("fermerP").onclick = fermerPanneau;
}

// ============ CE QUE LA PAGE VOIT ============
// Comme les JUGES de dtz-oral.html : ce qu'un programme peut voir sans juger la langue.
const LETTRE = "\\p{L}";
function motsDe(t){ return String(t || "").split(/\s+/).filter(w => /\p{L}/u.test(w)).length; }
// un mot entier, insensible a la casse, lettres accentuees comprises (\b ne connait pas l'allemand)
function motRe(m, drapeaux){ return new RegExp("(^|[^" + LETTRE + "])(" + m + ")(?![" + LETTRE + "])", drapeaux || "iu"); }
const SUBORD = ["weil", "dass", "wenn", "ob", "obwohl", "damit", "als", "bevor", "nachdem", "während", "falls"];
const COORD = ["und", "aber", "oder", "denn", "deshalb", "trotzdem", "dann", "außerdem", "zwar", "sondern"];

// La salutation de fin : ce que les gens tapent vraiment, pas seulement la forme des manuels (retour du 9 nov. 2026 :
// « No closing » alors qu'il y en avait une). Clavier sans tréma (Grusse, Gruesse), Grüße ou Gruß seuls, LG, Alles Gute,
// Bis nächste Woche, Deine Kirsty. On regarde les trois dernières lignes, avant un éventuel P.S.
const GRUSS_ADJ = "(?:viel|lieb|herzlich|best|sch(?:ö|oe)n|freundlich)e[nms]?";
const GRUSS_PARTOUT = [
  "(?:mit\\s+)?" + GRUSS_ADJ + "(?:\\s+" + GRUSS_ADJ + ")?\\s+gr(?:ü|ue|u)(?:ß|ss|β)(?:en?)?[^\\n]*",
  "bis\\s+(?:bald|morgen|dann|sonntag|samstag|sp(?:ä|ae)ter)",
  "tsch(?:ü|ue|u)ss?",
  "ciao|tschau"
].map(m => motRe(m, "iu"));
const GRUSS_LIGNE = new RegExp("^(?:" + [
  "gr(?:(?:ü|ue|u)(?:ß|ss|β)e|u(?:ß|ss|β))(?!" + "\\p{L}).*",
  "(?:lg|vg|mfg|sg)(?!\\p{L}).*",
  "alles\\s+(?:gute|liebe)(?!\\p{L}).*",
  "mach['’]?s\\s+gut.*",
  "bis(?:\\s+\\p{L}+){1,3}[\\s!.,]*",
  "(?:dein|deine|euer|eure)(?:\\s+\\p{L}+){1,2}[\\s!.,]*"
].join("|") + ")$", "iu");
function salutationDe(lignes){
  const ps = lignes.findIndex((l, k) => k > 0 && /^p\.?\s?s\b/i.test(l));
  const dernieres = (ps > 0 ? lignes.slice(0, ps) : lignes).slice(-3);
  for (const brute of dernieres){
    const l = brute.normalize("NFC");
    for (const re of GRUSS_PARTOUT){ const m = l.match(re); if (m) return m[2].trim(); }
    const m = l.match(GRUSS_LIGNE);
    if (m) return m[0].trim();
  }
  return null;
}

function analyser(mode, s, texte){
  const ls = mode === "LS";
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
  const salut = salutationDe(lignes);
  out.push(salut ? { c: "ok", t: T("sch_v_gruss_ok", {m: salut}) } : { c: "ko", t: T("sch_v_gruss_ko") });
  if (salut && s.registre === "informel" && /mit freundlichen/i.test(salut)) out.push({ c: "inf", t: T("sch_v_gruss_froid") });
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
    out.push(indice(s.indices) ? { c: "ok", t: T("sch_v_frage_ok", {f}) } : { c: "inf", t: T("sch_v_frage_ko", {f, c: champTelc(s, "conseil")}) });
  }
  return out;
}

// ============ LA GRILLE ============
const PALIERS = ["b1p", "b1", "a2p", "a2", "moins"];
// les points d'un critere : I vaut 15 pour le courriel, 5 pour la reponse courte ; II-IV, 10 (FORMAT-TELC.md)
function ptsCritere(mode, id, palier){
  const b = SCH.d.bareme, k = PALIERS.indexOf(palier);
  if (k < 0) return null;
  if (id === "I") return (mode === "LS" ? b.email_I : b.kurz_I)[k];
  return b.ensemble[k];
}
function surSch(mode){ const b = SCH.d.bareme; return (mode === "LS" ? b.email_I[0] : b.kurz_I[0]) + 3 * b.ensemble[0]; }
// l'estimation, quand les quatre criteres sont choisis : {points, sur, niveau}
function estimation(){
  const c = SCH.etat.crit || {};
  if (!SCH.d.kriterien.every(k => c[k.id])) return null;
  const points = SCH.d.kriterien.reduce((t, k) => t + ptsCritere(SCH.mode, k.id, c[k.id]), 0), sur = surSch(SCH.mode);
  // les seuils du telc (FORMAT-TELC.md) : B1 a 70 %, A2 a 40 %
  const niveau = points >= 0.7 * sur ? "b1" : points >= 0.4 * sur ? "a2" : "moins";
  return { points, sur, niveau };
}

// un critere de la grille : son nom, ses trois descriptions, les cinq paliers avec leurs points
function critereHtml(mode, k, pris, sansPoints){
  return '<div class="sch-crit"><h3>' + esc(champTelc(k, "titre")) + '<small lang="de">' + esc(k.de) + '</small></h3>' +
    '<p class="sch-desc"><b>' + esc(T("sch_desc_b1")) + '</b> · ' + esc(champTelc(k, "b1")) + '</p>' +
    '<p class="sch-desc"><b>' + esc(T("sch_desc_a2")) + '</b> · ' + esc(champTelc(k, "a2")) + '</p>' +
    '<p class="sch-desc"><b>' + esc(T("sch_desc_moins")) + '</b> · ' + esc(champTelc(k, "moins")) + '</p>' +
    '<div class="sch-niv">' + PALIERS.map(p => '<button type="button" data-crit="' + k.id + '" data-p="' + p + '" class="' + (pris === p ? "pris" : "") + '" aria-pressed="' + (pris === p) + '">' + esc(T("sch_" + p)) + (sansPoints ? "" : ' · ' + ptsCritere(mode, k.id, p)) + '</button>').join("") + '</div></div>';
}
function brancherCriteres(choix, apres){
  document.querySelectorAll("[data-crit]").forEach(b => b.onclick = () => {
    choix[b.dataset.crit] = b.dataset.p;
    document.querySelectorAll('[data-crit="' + b.dataset.crit + '"]').forEach(x => { const on = x === b; x.classList.toggle("pris", on); x.setAttribute("aria-pressed", on); });
    apres();
  });
}

function pageVerifier(){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const v = analyser(SCH.mode, s, SCH.etat.texte || "");
  const coches = ls ? '<div class="q"><div class="frage">' + esc(T("sch_coche")) + '</div>' + s.punkte.map((p, k) =>
      '<label class="sch-coche"><input type="checkbox" data-coche="' + k + '"' + (SCH.etat.coches.includes(k) ? " checked" : "") + '><span><span lang="de">' + esc(p.de) + '</span><br><span class="petit">' + esc(champTelc(p, "aide")) + '</span></span></label>').join("") + '</div>' : "";
  $("zone").innerHTML = enteteSch() +
    '<div class="bloc"><h2>' + esc(T("sch_ton_texte")) + '</h2><div class="sch-texte" lang="de">' + esc(SCH.etat.texte || "") + '</div></div>' +
    '<div class="bloc"><h2>' + esc(T("sch_voit")) + '</h2><p class="petit">' + esc(T("sch_voit_s")) + '</p><ul class="sch-v">' +
      v.map(x => '<li class="' + x.c + '"><b>' + (x.c === "ok" ? "✓" : x.c === "ko" ? "✗" : "•") + '</b><span>' + esc(x.t) + '</span></li>').join("") + '</ul></div>' +
    '<div class="bloc"><h2>' + esc(T("sch_grille")) + '</h2><p class="petit">' + esc(T("sch_grille_s")) + '</p>' + coches +
      SCH.d.kriterien.map(k => critereHtml(SCH.mode, k, (SCH.etat.crit || {})[k.id])).join("") +
      '<div id="schEstim"></div></div>';
  document.querySelectorAll("[data-coche]").forEach(b => b.onchange = () => {
    const k = Number(b.dataset.coche);
    SCH.etat.coches = SCH.etat.coches.filter(x => x !== k).concat(b.checked ? [k] : []);
    garder(); afficherEstimation();
  });
  SCH.etat.crit = SCH.etat.crit || {};
  brancherCriteres(SCH.etat.crit, () => {
    garder(); afficherEstimation();
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
  const html = m.lignes.map(ligne => {
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
  const g = GUILLEMETS_TELC;
  return { lettre: '<div class="doc lettre sch-modele" dir="ltr">' + html + '</div>',
    notes: '<ol class="sch-notes">' + m.notes.map((n, j) => '<li data-li="' + prefixe + j + '"><span class="ex" lang="de">' + g[0] + esc(n.de) + g[1] + '</span> — ' + esc(champTelc(n, "note")) + '</li>').join("") + '</ol>' };
}

function pageModeles(){
  const s = SCH.serie, ls = SCH.mode === "LS";
  const a2 = modeleHtml(s.modeles.a2, "a"), b1 = modeleHtml(s.modeles.b1, "b");
  const passer = champTelc(s, "passer") || [];
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
      '<button class="secondaire" id="schToutes">' + esc(T("sch_toutes")) + '</button></div>';
  // refaire : le meme sujet, page blanche ; un autre sujet : choisirSerie() prend le moins recemment fait
  $("schRefaire").onclick = () => { ecrire("sch_" + SCH.mode + "_" + s.id, {}); ouvrirSchreiben(SCH.mode, s); };
  $("schAutre").onclick = () => ouvrirSchreiben(SCH.mode);
  TELC.continuerPartie(SCH.mode);
  $("schToutes").onclick = toutesLesSectionsSch;
  DTZ.surRetour(() => { toutesLesSectionsSch(); return true; });
  window.scrollTo(0, 0);
}

// ============ L'EXAMEN BLANC ============
// L'appel d'examen-blanc.js (session telc-parler-blanc, 74fa58d), en deux temps :
//   1. lancer(fini, o), PENDANT le chrono : la copie, sans aide (ni Mark, ni indice, ni formules, ni compteur, ni
//      correction de 29-30). « Rendre », ou terminer() a zero du chrono, appelle fini() avec ce que la page sait
//      compter seule : LS {Lesen : 3 par bonne reponse a 29-30, Schreiben : 0}, S {Schreiben : 0} ; le texte va dans
//      detail, pour la grille.
//   2. grille(finiGrille, o), HORS chrono, a la fin de l'examen (au retour de l'oral, avant le verdict) : la page ne
//      jugeant pas la langue, l'eleve se note avec la grille de l'examinateur. LS : le critere I du courriel (15).
//      S : le critere I de la reponse courte (5) et les criteres II-IV sur les DEUX textes (30). Les points
//      s'ajoutent a ceux de fini().
// L'oral s'ouvre dans une autre page entre les deux : rien n'est garde en memoire, tout passe par detail. Le
// courriel rendu en LS est recopie dans le detail de S (SCH.courrielExamen, sinon le resultat LS de l'examen blanc).
// La serie tourne avec le numero de l'examen blanc (o.numero), comme les Sprachbausteine.
function serieExamen(mode, o){
  const pool = seriesDe(mode);
  return pool.length ? pool[((o && o.numero) || 0) % pool.length] : null;
}

function examenSchreiben(mode, fini, o){
  silence(); arreterChrono(); fermerPanneau();
  const s = serieExamen(mode, o), ls = mode === "LS";
  if (!s){ setTimeout(() => fini({}), 0); return {}; }
  const ex = { mode, serie: s, q: {}, texte: "" };
  let rendu = false;
  if (ls) SCH.courrielExamen = null;
  $("titre").textContent = T(ls ? "ls_titre" : "s_titre");
  const questions = ls ? s.fragen.map(f => {
    const opts = f.typ === "rf" ? [T("sch_richtig"), T("sch_falsch")] : f.o;
    return '<div class="q"><div class="tete"><span class="num">' + f.n + '</span><span class="frage" lang="de">' + esc(f.de) + '</span></div>' +
      '<div class="choix' + (f.typ === "rf" ? " ligne" : "") + '">' + opts.map((x, k) =>
        '<button class="opt" data-exq="' + f.n + '" data-k="' + k + '">' + (f.typ === "rf" ? "" : '<b>' + "ab"[k] + '</b>') + '<span lang="de">' + esc(x) + '</span></button>').join("") + '</div></div>';
  }).join("") : "";
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T(ls ? "ls_section" : "s_section")) + ' · ' + esc(T("examen")) + '</div><p class="petit">' + esc(T("sch_ex_pas_aide")) + '</p></div>' +
    '<div class="bloc">' + (ls ? '<p class="consigne" lang="de">' + esc(T("sch_rf_consigne_de")) + '</p>' : "") + docRecu(mode, s) + questions + '</div>' +
    '<div class="bloc">' + consigneEcrire(mode, s) +
      '<textarea class="sch-zone' + (ls ? "" : " court") + '" id="exTexte" lang="de" spellcheck="false" autocapitalize="sentences" placeholder="' + esc(T("sch_placeholder")) + '"></textarea></div>';
  $("exTexte").oninput = () => { ex.texte = $("exTexte").value; };
  document.querySelectorAll("[data-exq]").forEach(b => b.onclick = () => {
    ex.q[b.dataset.exq] = Number(b.dataset.k);
    document.querySelectorAll('[data-exq="' + b.dataset.exq + '"]').forEach(x => x.classList.toggle("pris", x === b));
  });
  const rendre = () => {
    if (rendu) return; rendu = true;
    const zone = $("exTexte"); if (zone) ex.texte = zone.value;
    const bons = ls ? s.fragen.filter(f => ex.q[f.n] === f.bon).length : 0;
    const detail = { mode, serie: s.id, texte: ex.texte,
      questions: ls ? s.fragen.map(f => ({ n: f.n, rep: ex.q[f.n] === undefined ? null : ex.q[f.n], bon: f.bon })) : null };
    if (ls) SCH.courrielExamen = { serie: s.id, texte: ex.texte };
    else detail.courriel = courrielDeLExamen();
    fini({ pts: ls ? { Lesen: 3 * bons, Schreiben: 0 } : { Schreiben: 0 }, detail });
  };
  suite(T(ls ? "ls_ex_rendre" : "sch_ex_rendre"), rendre);
  window.scrollTo(0, 0);
  return { terminer: rendre };
}

// le courriel rendu plus tot dans le meme examen blanc : en memoire, sinon dans l'etat de l'examen blanc
function courrielDeLExamen(){
  if (SCH.courrielExamen) return SCH.courrielExamen;
  try{ const r = typeof BL !== "undefined" && BL && BL.res && BL.res.LS; if (r && r.detail && r.detail.texte !== undefined) return { serie: r.detail.serie, texte: r.detail.texte }; }catch(e){}
  return null;
}

function grilleSchreiben(mode, finiGrille, o){
  silence(); arreterChrono(); fermerPanneau();
  const ls = mode === "LS", d = (o && o.detail) || {};
  const s = seriesDe(mode).find(x => x.id === d.serie) || null;
  const texte = d.texte || "";
  const courriel = ls ? null : d.courriel;
  const crit = {};
  const criteres = SCH.d.kriterien.filter(k => ls ? k.id === "I" : true);
  const textes = ls ? '<div class="sch-texte" lang="de">' + esc(texte) + '</div>'
    : (courriel ? '<h2>' + esc(T("sch_ex_ton_courriel")) + '</h2><div class="sch-texte" lang="de">' + esc(courriel.texte || "") + '</div>' : "") +
      '<h2>' + esc(T("sch_ex_ta_reponse")) + '</h2><div class="sch-texte" lang="de">' + esc(texte) + '</div>';
  const punkte = ls && s ? '<ol class="sch-liste">' + s.punkte.map(p => '<li><span class="de" lang="de">' + esc(p.de) + '</span><span class="tr">' + esc(champTelc(p, "aide")) + '</span></li>').join("") + '</ol>' : "";
  $("titre").textContent = T(ls ? "ls_titre" : "s_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T(ls ? "ls_section" : "s_section")) + ' · ' + esc(T("examen")) + '</div>' +
      '<p class="petit">' + esc(T(ls ? "ls_ex_note" : courriel ? "sch_ex_note_s" : "sch_ex_note_seul")) + '</p>' +
      (s ? docRecu(mode, s) : "") + textes + punkte + '</div>' +
    '<div class="bloc">' + criteres.map(k => critereHtml(mode, k, null, false)).join("") + '</div>';
  const pret = () => criteres.every(k => crit[k.id]);
  brancherCriteres(crit, () => { $("suite").disabled = !pret(); });
  suite(T("sch_ex_valider"), () => {
    if (!pret()) return;
    const ecrit = criteres.reduce((t, k) => t + ptsCritere(mode, k.id, crit[k.id]), 0);
    finiGrille({ pts: { Schreiben: ecrit }, detail: { crit: Object.assign({}, crit) } });
  });
  $("suite").disabled = !pret();
  window.scrollTo(0, 0);
}
