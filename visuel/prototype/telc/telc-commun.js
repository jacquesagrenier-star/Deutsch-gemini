// LE TELC A2·B1 -- CE QUI SERT A TOUTES SES PARTIES (6 nov. 2026, session « examens DTZ / telc », qui garde le bloc
// et l'assemblage). Charge APRES ../dtz/commun.js, AVANT les modules des parties.
//
// Le bloc telc a ete accelere par Jacques le 6 nov. (decision 1c40ee6) : quatre sessions font chacune leur partie,
// en francais ET en anglais. Elles s'accordent sur ce fichier, qu'elles ne modifient pas (le demander a la session
// « examens DTZ / telc ») :
//
// 1. LES TEXTES. Un module ecrit ses textes une fois par langue et les verse dans TXT de commun.js :
//        textesTelc({ fr: {cle: "…"}, en: {cle: "…"} });
//    T(cle) donne alors la langue d'interface, et le francais pour une cle qui manque (commun.js ne connait que TXT).
// 2. LES DONNEES. Un champ traduit s'ecrit « nom_fr », « nom_en » (comme pruefung.json) ; champTelc(o, "erkl")
//    donne la langue d'interface, sinon le francais. L'allemand de l'examen n'a pas de suffixe.
// 3. L'EXAMEN BLANC. Une partie qui peut s'y jouer s'inscrit ici, en plus de DTZ.partie() :
//        TELC.epreuve({ id: "LS", ordre: 30, minutes: 0, sur: {Lesen: 6, Schreiben: 15},
//                       lancer: fini => { …la partie minutee, sans aide… ; fini({pts: {Lesen: 6, Schreiben: 11}, detail}) } });
//    Les points se donnent PAR COMPETENCE (Lesen, Hoeren, Schreiben, Sprechen), parce qu'une partie du telc peut
//    compter dans deux : « Lire et ecrire » donne 6 points de Lesen (items 29-30) et 15 de Schreiben (le courriel 31).
//    Le telc compte 60 points par competence (preparation-examens/FORMAT-TELC.md) :
//      L  Lesen 54 · SB Schreiben 5 · LS Lesen 6 + Schreiben 15 · H Hoeren 60 · HS Schreiben 5 ·
//      S  Schreiben 5, plus les trois criteres d'ensemble de l'ecrit (II-IV, 30) sur le courriel ET la reponse
//         courte, que la partie S donne pour les deux textes · Sp Sprechen 60.
//    « minutes » : 0 pour une partie qui partage son temps avec la precedente (SB et LS : 35 min ensemble ; H et HS :
//    35 min ensemble). « detail » : ce que le corrige montrera. L'examen blanc (examen-blanc.js) enchaine les epreuves
//    inscrites dans l'ordre de l'examen, additionne les points par competence et calcule le niveau avec niveauTelc().
// 4. LES IDENTIFIANTS des parties (tuiles de telc.html) : L Lire, SB Sprachbausteine, LS Lire et ecrire (le
//    courriel), H Ecouter, HS Ecouter et noter (les repondeurs), S Ecrire (la reponse courte), Sp Parler.

"use strict";

// LES AUTRES LANGUES D'INTERFACE (7 nov. 2026, Jacques : « s'assurer qu'ils sont traduits dans toutes les langues »).
// Les modules ecrivent en francais et en anglais ; pour tr, uk, fa, ar, pt, pl et ru, telc.html charge
// langues/<langue>.js, un dictionnaire de l'anglais vers la langue (window.TELC_DICO), derive de langues/<langue>.json
// par outils/langues.js. Un texte absent du dictionnaire retombe sur le francais.
const TELC_DICO = (LANGUE !== "fr" && LANGUE !== "en" && window.TELC_DICO) || null;
function dicoTelc(en){
  if (!TELC_DICO || en == null) return null;
  if (Array.isArray(en)){ const r = en.map(dicoTelc); return r.every(x => x != null) ? r : null; }
  return Object.prototype.hasOwnProperty.call(TELC_DICO, en) ? TELC_DICO[en] : null;
}
function textesTelc(t){
  Object.assign(TXT, (t && t.fr) || {}, (t && t[LANGUE]) || {});
  if (TELC_DICO && t && t.en && !t[LANGUE]) for (const k in t.en){ const v = dicoTelc(t.en[k]); if (v != null) TXT[k] = v; }
}
function champTelc(o, nom){
  if (!o) return "";
  return o[nom + "_" + LANGUE] || dicoTelc(o[nom + "_en"]) || o[nom + "_fr"] || o[nom] || "";
}
// un objet {fr, en} (une consigne, une phrase) dans la langue d'interface
function objetTelc(o){
  return (o && (o[LANGUE] || dicoTelc(o.en) || o.fr)) || "";
}
// les deux-points, les guillemets et les dates selon la langue d'interface
const DEUX_POINTS_TELC = LANGUE === "fr" ? " : " : ": ";
const GUILLEMETS_TELC = ({ fr: ["« ", " »"], en: ["“", "”"], pt: ["“", "”"], tr: ["“", "”"], pl: ["„", "”"],
                           uk: ["«", "»"], ru: ["«", "»"], fa: ["«", "»"], ar: ["«", "»"] })[LANGUE] || ["“", "”"];
const DATE_TELC = ({ fr: "fr-FR", en: "en-GB", tr: "tr-TR", uk: "uk-UA", fa: "fa-IR", ar: "ar", pt: "pt-BR",
                     pl: "pl-PL", ru: "ru-RU" })[LANGUE] || "fr-FR";

const TELC = {
  epreuves: [],
  epreuve(e){ this.epreuves.push(e); this.epreuves.sort((a, b) => a.ordre - b.ordre); }
};

// LE NIVEAU AU TELC (FORMAT-TELC.md, Uebungstest 1, p. 44) : 240 points, 60 par competence.
//   B1 = 70 % du total (168) ET 70 % (42) dans 3 des 4 competences ET 40 % (24) dans chacune ;
//   A2 = 40 % du total (96) ET 40 % (24) dans 3 des 4 ET 10 % (6) dans chacune.
// pts : {Lesen, Hoeren, Schreiben, Sprechen}, chacun sur 60. Une competence absente (l'oral pas encore passe)
// rend le niveau « incomplet » : on ne promet pas un B1 sur trois competences.
function niveauTelc(pts){
  const C = ["Lesen", "Hoeren", "Schreiben", "Sprechen"];
  if (C.some(c => typeof pts[c] !== "number")) return "incomplet";
  const v = C.map(c => pts[c]), total = v.reduce((a, b) => a + b, 0);
  const regle = (pTotal, pTrois, pChacune) =>
    total >= 240 * pTotal && v.filter(x => x >= 60 * pTrois).length >= 3 && v.every(x => x >= 60 * pChacune);
  return regle(0.7, 0.7, 0.4) ? "b1" : regle(0.4, 0.4, 0.1) ? "a2" : "moins";
}

// LES TEXTES COMMUNS EN ANGLAIS : ceux de commun.js (francais seulement) et les tuiles du profil.
textesTelc({ en: {
  titre: "telc A2·B1 with Mark and Anna",
  intro: "At telc Deutsch A2·B1 you read first, then come the Sprachbausteine, the emails, the listening and the speaking test in pairs, with no picture. Anna and I will help you get ready, part by part.",
  entrainement: "Practice with Mark and Anna",
  entrainement_s: "One part at a time, with an explanation after every answer.",
  examen: "Mock exam",
  examen_s: "Like on exam day: timed, no help.",
  bientot: "soon",
  dernier: "Last mock exam: {s} — {n}",
  suivant: "Next", terminer: "Finish", recommencer: "Start again", accueil: "Back to telc",
  feuille: "Answer sheet", fermer: "Close", continuer: "Continue",
  verdict: "Result", sur: "out of {n}",
  niv_b1: "B1", niv_a2: "A2", niv_moins: "below A2",
  voix_tel: "Phone voice (prototype): recorded voices will come later.",
  maquette: "Prototype: few series for now.",
  quitter_q: "Leave the mock exam? It won't count.", quitter: "Leave"
}});
if (LANGUE !== "fr" && PROFIL.tuiles){
  const EN = {L: "Reading", SB: "Sprachbausteine", LS: "Reading and writing", H: "Listening",
              HS: "Listening and notes", S: "Writing", Sp: "Speaking"};
  PROFIL.tuiles.forEach(t => { if (EN[t.id]) t.titre = LANGUE === "en" ? EN[t.id] : (dicoTelc(EN[t.id]) || t.titre); });
}
