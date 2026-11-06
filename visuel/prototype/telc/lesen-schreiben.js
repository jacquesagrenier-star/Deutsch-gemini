// LE TELC A2·B1 AVEC MARK ET ANNA -- LIRE ET ECRIRE, LE COURRIEL (6 nov. 2026, session « telc Ecrire »).
//
// La partie LS du telc, d'apres preparation-examens/FORMAT-TELC.md (le format seul, jamais le contenu) :
// « Lesen und Schreiben », items 29-31, juste apres les Sprachbausteine (35 minutes pour les deux) :
//   29  un Richtig/Falsch sur un courriel recu qui pose des questions (3 points de Lesen) ;
//   30  un choix a 2 sur le meme courriel (3 points de Lesen) ;
//   31  la reponse a ce courriel : repondre a ses questions, formule d'appel et salutation (critere I, 15 points de
//       Schreiben ; les criteres II-IV, communs aux deux textes de l'ecrit, sont notes par la partie S).
// Les courriels sont ecrits pour Wortando (donnees/lesen-schreiben.json), jamais repris du telc.
//
// CE FICHIER NE FAIT QUE S'INSCRIRE : ses textes, ses donnees, sa tuile et son epreuve d'examen blanc. Le moteur des
// pages (ecrire, la grille, les lettres modeles, le recapitulatif) est commun aux deux textes de l'ecrit et vit dans
// schreiben.js (partie S), avec la grille, le bareme et les formules utiles (donnees/schreiben.json). Les deux
// fichiers vont ensemble ; telc.html les charge tous les deux. Les fonctions de schreiben.js ne sont appelees qu'a
// l'ouverture, une fois tout charge.
// Controle : python tests/telc_ecrire.py ; relecture : outils/relecture_ecrire.py.

"use strict";

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
  ls_t_e1: "Underline every question in the email (every \"?\"): those are your points.",
  ls_t_e2: "Choose du or Sie from the opening you received (Liebe Anna / Sehr geehrte Frau …).",
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
  ls_t_e2: "Choisis du ou Sie d'après la formule d'appel reçue (Liebe Anna / Sehr geehrte Frau …).",
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

// L'EXAMEN BLANC : 29 et 30 comptent en Lesen (3 points chacune), le courriel 31 en Schreiben (critere I, 15).
// « minutes : 0 » : la partie partage les 35 minutes des Sprachbausteine.
TELC.epreuve({ id: "LS", ordre: 30, minutes: 0, sur: { Lesen: 6, Schreiben: 15 }, lancer: fini => examenSchreiben("LS", fini) });
