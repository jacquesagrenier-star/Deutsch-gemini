// LE TELC A2·B1 AVEC MARK ET ANNA -- LIRE (LESEN) (6 nov. 2026, session « telc Lire »).
//
// LE FORMAT EST CELUI DU TELC, JAMAIS SON CONTENU (Testformat de l'Uebungstest telc Deutsch A2·B1,
// preparation-examens/FORMAT-TELC.md) : 45 minutes, 18 questions a 3 points (54 points), en quatre parties :
//   Teil 1 (1-5)    des petites annonces, a associer a cinq situations (8 annonces, 3 de trop) ;
//   Teil 2 (6-9)    un texte court, le detail : 1 Richtig/Falsch et 3 choix a, b, c ;
//   Teil 3 (10-13)  des courriels, le sens global : 4 associations (6 phrases, 2 de trop) ;
//   Teil 4 (14-18)  un texte plus long, le detail : 5 choix a, b, c.
// Au telc, la competence Lesen vaut 60 points : ces 54, plus les 6 des questions 29-30 (« Lire et ecrire »,
// une autre partie du bloc). Les textes sont ecrits pour Wortando (donnees/lesen.json, controle tests/telc.py).
//
// L'ORGANISATION EST CELLE DE L'ORAL DU DTZ ET DES SPRACHBAUSTEINE (decision de Jacques du 4 nov., « DTZ, l'oral :
// sections et exercices ») : la liste des parties ; dans une partie, UNE PAGE PAR QUESTION, avec les points de
// progression qu'on touche pour sauter, « ‹ » vers la liste, « Continuer » en bas ; en fin de partie, le
// recapitulatif, puis Refaire / Partie suivante / Toutes les parties. En plus : l'epreuve entiere, minutee
// (45 min, sans aide, le corrige apres), que l'examen blanc du bloc peut lancer par TELC_LESEN.lancer().
//
// LANGUES : l'interface de cette partie existe en francais et en anglais (TXT_L_FR, TXT_L_EN ; les autres langues
// retombent sur le francais) ; les donnees portent leurs champs *_fr et *_en.
// Ce module ne connait de commun.js que ses fonctions publiques ($, esc, T, TXT, LANGUE, parler, lire, ecrire,
// chrono, arreterChrono, confirmer, choisirSerie, marquerFait, resultat, silence, DTZ, accueil, MARK_IMG) ; il
// s'inscrit par DTZ.partie() comme sprachbausteine.js, et garde tout le reste dans sa fermeture.

"use strict";

const TXT_L_FR = {
  l_titre: "Lire",
  l_sous: "Lesen · 4 parties · 45 min",
  l_section: "Lesen · Teil {n}",
  l_t1: "Petites annonces", l_t2: "Un texte court", l_t3: "Des courriels", l_t4: "Un texte plus long",
  l_t1_s: "5 situations, 8 annonces", l_t2_s: "1 vrai ou faux, 3 choix", l_t3_s: "4 courriels, 6 phrases", l_t4_s: "5 choix",
  l_mark_debut: "Au telc, on commence par lire : 45 minutes, quatre parties, 18 questions à 3 points. Mon conseil : lis d'abord les questions, puis cherche la réponse dans le texte. Les mauvaises réponses reprennent souvent un mot du texte ; la bonne le dit souvent avec d'autres mots.",
  l_parties: "Les quatre parties",
  l_questions: "{n} questions",
  l_dernier: "Dernière fois : {b} / {n}",
  l_complet: "Toute l'épreuve, minutée",
  l_complet_s: "45 minutes, les 18 questions, sans aide ; le corrigé à la fin. Sur 54 points.",
  l_question: "Quelle réponse est la bonne ?",
  l_quelle_annonce: "Quelle annonce correspond à la situation ?",
  l_quelle_phrase: "Quelle phrase correspond à ce courriel ?",
  l_situation: "Situation",
  l_annonce_choisir: "Annonce {l}",
  l_von: "De", l_an: "À",
  l_juste: "Juste !",
  l_faux: "Pas tout à fait : c'est « {m} ».",
  l_trad: "En français : {t}",
  l_continuer: "Continuer",
  l_recap: "Récapitulatif",
  l_score: "{b} sur {n}",
  l_points: "À l'examen, cela ferait {p} points sur {s}.",
  l_mark_bien: "Très bien ! Tu sais où chercher. Garde ce réflexe : la question d'abord, le texte ensuite.",
  l_mark_moyen: "Pas mal ! Relis les explications des questions ratées : le piège est souvent un mot du texte repris dans une mauvaise réponse.",
  l_mark_faible: "C'est un début. Relis chaque explication, puis refais la partie : tu verras que les pièges se ressemblent toujours.",
  l_refaire: "Refaire la partie",
  l_suivante: "Partie suivante : {t}",
  l_section_suivante: "Section suivante : {t}",
  l_toutes: "Toutes les parties",
  l_toutes_sections: "Toutes les sections",
  l_teil_suivant: "Teil {n}",
  l_rendre: "Rendre ma copie",
  l_rendre_q: "Rendre maintenant ? {n} question(s) sans réponse.",
  l_oui_rendre: "Oui, rendre",
  l_temps_fini: "Le temps est écoulé : ta copie est rendue.",
  l_quitter_q: "Quitter l'épreuve ? Elle ne sera pas comptée.",
  l_quitter: "Quitter",
  l_regles: "Comme le jour de l'examen : 45 minutes pour les quatre parties, dans l'ordre que tu veux. Pas de traduction ni d'explication pendant l'épreuve.",
  l_resultat: "Résultat",
  l_sur54: "{p} points sur 54",
  l_niv_b1: "C'est au niveau du B1 pour la lecture (70 % et plus).",
  l_niv_a2: "C'est au niveau de l'A2 pour la lecture (40 % et plus) ; le B1 commence à 70 %.",
  l_niv_moins: "C'est encore sous l'A2 (moins de 40 %). Reprends les parties une par une.",
  l_regle: "Au telc, la lecture vaut 60 points : ces 54, plus les 6 points des questions 29 et 30 (« Lire et écrire »). Le niveau se décide sur l'examen entier, avec un minimum dans chaque compétence.",
  l_corrige: "Le corrigé",
  l_ta_reponse: "Ta réponse : {r}",
  l_sans: "pas de réponse",
  l_bonne: "La bonne réponse : {r}",
  l_rf: ["richtig", "falsch"],
  l_mark_v_b1: "Bravo ! La lecture, c'est solide. Garde ton énergie pour l'écoute, elle vient plus tard dans l'examen.",
  l_mark_v_a2: "C'est un bon début. Regarde surtout les questions ratées dans le corrigé : c'est là que se cachent les points du B1.",
  l_mark_v_moins: "Ne t'inquiète pas : reprenons les parties une par une, avec les explications.",
  l_refaire_epreuve: "Refaire une épreuve"
};
const TXT_L_EN = {
  l_titre: "Reading",
  l_sous: "Lesen · 4 parts · 45 min",
  l_t1: "Small ads", l_t2: "A short text", l_t3: "E-mails", l_t4: "A longer text",
  l_t1_s: "5 situations, 8 ads", l_t2_s: "1 true or false, 3 choices", l_t3_s: "4 e-mails, 6 sentences", l_t4_s: "5 choices",
  l_mark_debut: "In the telc, reading comes first: 45 minutes, four parts, 18 questions worth 3 points each. My tip: read the questions first, then look for the answer in the text. Wrong answers often repeat a word from the text; the right one often says it in other words.",
  l_parties: "The four parts",
  l_questions: "{n} questions",
  l_dernier: "Last time: {b} / {n}",
  l_complet: "The whole test, timed",
  l_complet_s: "45 minutes, all 18 questions, no help; the answers at the end. Out of 54 points.",
  l_question: "Which answer is right?",
  l_quelle_annonce: "Which advert matches the situation?",
  l_quelle_phrase: "Which sentence matches this e-mail?",
  l_situation: "Situation",
  l_annonce_choisir: "Advert {l}",
  l_von: "From", l_an: "To",
  l_juste: "Correct!",
  l_faux: "Not quite: it's “{m}”.",
  l_trad: "In English: {t}",
  l_continuer: "Continue",
  l_recap: "Summary",
  l_score: "{b} out of {n}",
  l_points: "In the exam, that would be {p} points out of {s}.",
  l_mark_bien: "Very good! You know where to look. Keep the habit: questions first, text second.",
  l_mark_moyen: "Not bad! Read the explanations for the questions you missed: the trap is often a word from the text repeated in a wrong answer.",
  l_mark_faible: "It's a start. Read each explanation, then do the part again: you'll see the traps always look alike.",
  l_refaire: "Do this part again",
  l_suivante: "Next part: {t}",
  l_section_suivante: "Next section: {t}",
  l_toutes: "All parts",
  l_toutes_sections: "All sections",
  l_rendre: "Hand in",
  l_rendre_q: "Hand in now? {n} question(s) unanswered.",
  l_oui_rendre: "Yes, hand in",
  l_temps_fini: "Time is up: your paper has been handed in.",
  l_quitter_q: "Leave the test? It won't be counted.",
  l_quitter: "Leave",
  l_regles: "Just like on exam day: 45 minutes for the four parts, in any order. No translations or explanations during the test.",
  l_resultat: "Result",
  l_sur54: "{p} points out of 54",
  l_niv_b1: "That is B1 level for reading (70% or more).",
  l_niv_a2: "That is A2 level for reading (40% or more); B1 starts at 70%.",
  l_niv_moins: "That is still below A2 (under 40%). Go back over the parts one at a time.",
  l_regle: "In the telc, reading is worth 60 points: these 54, plus the 6 points of questions 29 and 30 (“Reading and writing”). The level is decided on the whole exam, with a minimum in each skill.",
  l_corrige: "The answers",
  l_ta_reponse: "Your answer: {r}",
  l_sans: "no answer",
  l_bonne: "The right answer: {r}",
  l_mark_v_b1: "Well done! Your reading is solid. Save your energy for listening; it comes later in the exam.",
  l_mark_v_a2: "A good start. Look closely at the questions you missed in the answers: that's where the B1 points are hiding.",
  l_mark_v_moins: "Don't worry: let's go back over the parts one at a time, with the explanations.",
  l_refaire_epreuve: "Do another test"
};
Object.assign(TXT, LANGUE === "en" ? Object.assign({}, TXT_L_FR, TXT_L_EN) : TXT_L_FR);

const TELC_LESEN = (() => {
  const EN = LANGUE === "en";
  // le champ traduit d'un objet : tr(it, "erkl") lit erkl_en ou erkl_fr ; tr(p, "") lit p.en ou p.fr (les consignes
  // et les phrases du Teil 3) ; sans traduction anglaise, le francais
  const tr = (o, k) => { const c = k ? k + "_" : ""; return (o && (o[c + (EN ? "en" : "fr")] || o[c + "fr"])) || ""; };
  const deS = s => '<span lang="de" dir="ltr">' + esc(s) + '</span>';
  const TEILE = ["T1", "T2", "T3", "T4"];
  const titreTeil = t => T("l_" + t.toLowerCase());
  const RF = ["richtig", "falsch"];
  const DEUX_POINTS = EN ? ": " : " : ";   // l'espace avant les deux-points est francaise

  // le peu de mise en page propre a cette partie (le reste vient de ../dtz/commun.css et de telc.html)
  const style = document.createElement("style");
  style.textContent =
    ".lpoints{display:flex;flex-wrap:wrap;gap:6px}" +
    ".lpoint{width:32px;height:32px;border-radius:50%;border:2px solid var(--trait);background:var(--verre);color:var(--encre);font:900 13px var(--police);cursor:pointer;padding:0}" +
    ".lpoint.ok{border-color:var(--vert);background:var(--vert);color:#fff}.lpoint.ko{border-color:var(--rouge);background:var(--rouge);color:#fff}" +
    ".lpoint.ici{box-shadow:0 0 0 3px var(--ambre)}" +
    ".lsection{font-size:12px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;color:var(--gris)}" +
    "button.annonce{font:inherit;color:inherit;text-align:left;cursor:pointer;width:100%}" +
    "button.annonce:disabled{cursor:default}" +
    ".annonce.juste{border:3px solid var(--vert)}.annonce.faux{border:3px solid var(--rouge);opacity:.85}.annonce.pris{border:3px solid var(--ambre)}" +
    ".lettre .tetemail{font-size:13px;color:var(--gris);margin-bottom:8px;font-weight:700}" +
    ".lrecap .frage s{opacity:.7}.lrecap .erkl{font-weight:600;line-height:1.5;margin:6px 0 0}" +
    ".lboutons{display:flex;flex-direction:column;gap:8px}.lboutons .secondaire{align-self:stretch;text-align:center}";
  document.head.appendChild(style);

  const E = {donnees: null, direct: false, serie: null, teil: null, qs: [], rep: [], i: 0, ex: null};
  // ouverte directement sur cette partie (?partie=L, depuis le panneau du bloc telc de l'app) : le « ‹ » de la liste
  // des parties ramene alors au panneau, comme pour les Sprachbausteine
  E.direct = Q.get("partie") === "L";

  DTZ.charger(fetch("donnees/lesen.json", {cache: "no-cache"})
    .then(r => { if (!r.ok) throw new Error("lesen.json"); return r.json(); })
    .then(d => { E.donnees = d; }));

  // ============ LES QUESTIONS D'UNE PARTIE ============
  // une forme commune : {nr, kind ("lettre" | "rf" | "abc"), options (ce qu'on touche), bon, frage, ...}
  function questions(s, teil){
    const t = s[teil];
    if (teil === "T1"){
      const lettres = t.anzeigen.map(a => a.b);
      return t.items.map(it => ({nr: it.nr, teil, kind: "lettre", options: lettres, bon: it.bon, frage: it.situation,
        frage_tr: tr(it, "situation"), erkl: tr(it, "erkl"), item: it}));
    }
    if (teil === "T3"){
      const lettres = t.saetze.map(x => x.b);
      return t.mails.map(m => ({nr: m.nr, teil, kind: "lettre", options: lettres, bon: m.bon, mail: m, saetze: t.saetze,
        frage: T("l_quelle_phrase"), frage_tr: "", erkl: tr(m, "erkl"), item: m}));
    }
    return t.items.map(it => ({nr: it.nr, teil, kind: it.rf ? "rf" : "abc", options: it.rf ? RF : it.optionen, bon: it.bon,
      frage: it.frage, frage_tr: tr(it, "frage"), options_tr: it.rf ? null : (it["optionen" + (EN ? "_en" : "_fr")] || it.optionen_fr),
      erkl: tr(it, "erkl"), item: it}));
  }
  const toutes = s => [].concat(...TEILE.map(t => questions(s, t)));
  // ce que dit une reponse, en clair : la lettre et sa phrase (Teil 3), la lettre (Teil 1), le mot (a, b, c ; R/F)
  function libelle(q, v){
    if (v === null || v === undefined) return T("l_sans");
    if (q.teil === "T3"){ const p = q.saetze.find(x => x.b === v); return v + " · " + (p ? p.de : ""); }
    if (q.kind === "lettre") return v;
    if (q.kind === "rf") return q.options[v];
    return "abc"[v] + " · " + q.options[v];
  }

  // ============ LE RENDU DES DOCUMENTS ============
  // les annonces du Teil 1 : chacune est un bouton, on la touche pour la choisir (en plus de la rangee de lettres)
  function annonces(s, q, r, montrer){
    return '<div class="doc annonces" lang="de" dir="ltr">' + s.T1.anzeigen.map(a => {
      let c = "annonce";
      if (montrer){ if (a.b === q.bon) c += " juste"; else if (a.b === r) c += " faux"; }
      else if (r === a.b) c += " pris";
      return '<button class="' + c + '" data-v="' + a.b + '" aria-label="' + esc(T("l_annonce_choisir", {l: a.b})) + '"' + (montrer ? " disabled" : "") + '>' +
        '<span class="l">' + a.b + '</span><div class="t">' + esc(a.titel) + '</div>' + esc(a.text) + '</button>';
    }).join("") + '</div>';
  }
  function texte(t){
    const cls = t.typ === "aushang" ? "aushang" : "journal";
    return '<div class="doc ' + cls + '" lang="de" dir="ltr"><div class="k">' + esc(t.kopf) + '</div><h3>' + esc(t.titel) + '</h3>' +
      t.absaetze.map(p => '<p>' + esc(p) + '</p>').join("") + '</div>';
  }
  function courriel(m){
    return '<div class="doc lettre" dir="ltr"><div class="k">E-Mail</div>' +
      '<div class="tetemail">' + esc(T("l_von")) + DEUX_POINTS + '<span lang="de">' + esc(m.von) + '</span><br>' + esc(T("l_an")) + DEUX_POINTS + '<span lang="de">' + esc(m.an) + '</span></div>' +
      m.absaetze.map(p => '<p lang="de">' + esc(p) + '</p>').join("") + '</div>';
  }
  // les boutons de reponse d'une question ; etat : {r, montrer, fige}
  function boutons(q, etat){
    const {r, montrer, fige} = etat;
    const cls = v => { let c = "opt"; if (montrer){ if (v === q.bon) c += " juste"; else if (v === r) c += " faux"; } else if (v === r) c += " pris"; return c; };
    const dis = fige ? " disabled" : "";
    if (q.teil === "T3")
      return '<div class="choix">' + q.saetze.map(p => '<button class="' + cls(p.b) + '" data-q="' + q.nr + '" data-v="' + p.b + '"' + dis + '><b>' + p.b + '</b>' + deS(p.de) + '</button>').join("") + '</div>';
    if (q.kind === "lettre")
      return '<div class="choix ligne">' + q.options.map(l => '<button class="' + cls(l) + '" data-q="' + q.nr + '" data-v="' + l + '"' + dis + '><b>' + l + '</b></button>').join("") + '</div>';
    return '<div class="choix' + (q.kind === "rf" ? " ligne" : "") + '">' + q.options.map((o, k) =>
      '<button class="' + cls(k) + '" data-q="' + q.nr + '" data-v="' + k + '"' + dis + '>' + (q.kind === "abc" ? '<b>' + "abc"[k] + '</b>' : "") + deS(o) + '</button>').join("") + '</div>';
  }
  // la traduction montree apres la reponse : la question et sa bonne reponse dans la langue de l'eleve
  function traduction(q){
    if (q.teil === "T3"){ const p = q.saetze.find(x => x.b === q.bon); return p ? q.bon + " · " + tr(p, "") : ""; }
    if (q.kind === "abc" && q.options_tr) return q.frage_tr + " " + q.options_tr[q.bon];
    return q.frage_tr;
  }
  function aide(q, r){
    const ok = r === q.bon, t = traduction(q);
    return '<div class="aide"><span class="verdict ' + (ok ? "ok" : "ko") + '">' + esc(ok ? T("l_juste") : T("l_faux", {m: libelle(q, q.bon)})) + '</span>' +
      (t ? '<span class="trad">' + esc(T("l_trad", {t})) + '</span>' : "") +
      '<span class="dit"><img src="' + MARK_IMG + '" alt="Mark"><span class="erkl">' + esc(q.erkl) + '</span></span></div>';
  }
  function carte(q, etat){
    return '<div class="q" id="carte"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage"' + (q.teil === "T3" ? "" : ' lang="de"') + '>' + esc(q.frage) + '</span></div>' +
      boutons(q, etat) + (etat.montrer && !etat.corrige ? aide(q, etat.r) : "") + '</div>';
  }
  const consigne = teil => {
    const c = (E.donnees.consignes || {})[teil] || {};
    return '<p class="consigne"><span lang="de">' + esc(c.de || "") + '</span><span class="fr">' + esc(tr(c, "")) + '</span></p>';
  };

  // ============ LA LISTE DES PARTIES ============
  function liste(){
    silence(); arreterChrono(); E.ex = null;
    $("titre").textContent = T("l_titre") + " · Lesen"; $("suite").hidden = true;
    const faits = lire("lesen_teile", {});
    const vu = lire("lesen_vu", false);
    $("zone").innerHTML =
      (vu ? "" : '<div class="bloc"><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T("l_mark_debut")) + '</div></div></div>') +
      '<div class="bloc"><h2>' + esc(T("l_parties")) + '</h2><div class="teils">' + TEILE.map(t => {
        const f = faits[t], n = questions(E.donnees.series[0], t).length;
        return '<button class="teil" data-t="' + t + '"><span>Teil ' + t.slice(1) + ' · ' + esc(titreTeil(t)) + '<br><small>' + esc(T("l_" + t.toLowerCase() + "_s")) + '</small></span>' +
          '<small>' + esc(f ? T("l_dernier", {b: f.bons, n: f.n}) : T("l_questions", {n})) + '</small></button>';
      }).join("") + '</div></div>' +
      '<div class="bloc"><button class="mode" id="lComplet"><b>' + esc(T("l_complet")) + '</b><span>' + esc(T("l_complet_s")) + '</span></button></div>';
    ecrire("lesen_vu", true);
    document.querySelectorAll("[data-t]").forEach(b => b.onclick = () => ouvrirTeil(b.dataset.t));
    $("lComplet").onclick = () => lancer({});
    DTZ.surRetour(() => { toutesLesSections(); return true; });
    window.scrollTo(0, 0);
  }
  function toutesLesSections(){
    if (E.direct){ silence(); parler("fermer"); if (window.parent === window) accueil(); return; }
    accueil();
  }

  // ============ UNE PARTIE, UNE PAGE PAR QUESTION ============
  async function ouvrirTeil(teil, serie){
    E.teil = teil;
    E.serie = serie || await choisirSerie(E.donnees.series, () => [], "L" + teil);
    E.qs = questions(E.serie, teil);
    E.rep = E.qs.map(() => null);
    E.i = 0;
    DTZ.surRetour(() => { liste(); return true; });
    page();
  }
  function points(){
    return '<div class="lpoints">' + E.qs.map((q, k) => {
      const r = E.rep[k], etat = r === null ? "" : (r === q.bon ? " ok" : " ko");
      return '<button class="lpoint' + etat + (k === E.i ? " ici" : "") + '" data-aller="' + k + '" aria-label="' + q.nr + '">' + q.nr + '</button>';
    }).join("") + '</div>';
  }
  function page(){
    silence();
    const s = E.serie, q = E.qs[E.i], r = E.rep[E.i], montrer = r !== null;
    const etat = {r, montrer, fige: montrer};
    $("titre").textContent = "Teil " + E.teil.slice(1) + " · " + titreTeil(E.teil);
    let h = '<div class="bloc"><div class="lsection">' + esc(T("l_section", {n: E.teil.slice(1)})) + ' · ' + esc(titreTeil(E.teil)) + '</div>' + points() + '</div>';
    h += '<div class="bloc">' + (E.i === 0 ? consigne(E.teil) : "");
    if (E.teil === "T1") h += carte(q, etat) + annonces(s, q, r, montrer);
    else if (E.teil === "T3") h += courriel(q.mail) + carte(q, etat);
    else h += carte(q, etat) + texte(s[E.teil].text);
    h += '</div>';
    $("zone").innerHTML = h;
    document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { E.i = Number(b.dataset.aller); page(); });
    document.querySelectorAll("#zone [data-v]:not(:disabled)").forEach(b => b.onclick = () => repondre(q.kind === "lettre" ? b.dataset.v : Number(b.dataset.v)));
    const suite = $("suite");
    suite.hidden = !montrer; suite.textContent = T("l_continuer"); suite.onclick = continuer;
    if (montrer || E.i > 0){ const c = $("carte"); if (c) setTimeout(() => { try{ c.scrollIntoView({block: "center", behavior: "smooth"}); }catch(e){} }, 30); }
    else window.scrollTo(0, 0);
  }
  function repondre(v){
    if (E.rep[E.i] !== null) return;
    E.rep[E.i] = v;
    parler("exercice", {juste: v === E.qs[E.i].bon});
    page();
  }
  function continuer(){
    const apres = E.rep.findIndex((r, k) => r === null && k > E.i), avant = E.rep.findIndex(r => r === null);
    if (apres >= 0){ E.i = apres; page(); return; }
    if (avant >= 0){ E.i = avant; page(); return; }
    recap();
  }
  function lignesCorrige(qs, rep){
    const l = qs.map((q, k) => {
      const ok = rep[k] === q.bon;
      return {ok, h: '<div class="q lrecap"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage">' +
        (ok ? '<span class="ok">✓</span> ' : '<span class="ko">✗</span> ' + (rep[k] === null ? esc(T("l_sans")) : '<s lang="de">' + esc(libelle(q, rep[k])) + '</s>') + ' → ') +
        '<b lang="de">' + esc(libelle(q, q.bon)) + '</b></span></div>' +
        (q.teil === "T1" ? '<p class="petit" lang="de">' + esc(q.frage) + '</p>' : q.teil === "T3" ? '<p class="petit" lang="de">' + esc(q.mail.von + " → " + q.mail.an) + '</p>' : '<p class="petit" lang="de">' + esc(q.frage) + '</p>') +
        '<p class="erkl">' + esc(q.erkl) + '</p></div>'};
    });
    // ce qui est rate d'abord : c'est ce qu'on vient relire
    return l.filter(x => !x.ok).concat(l.filter(x => x.ok)).map(x => x.h).join("");
  }
  function recap(){
    silence(); $("suite").hidden = true;
    const qs = E.qs, n = qs.length, bons = qs.filter((q, k) => E.rep[k] === q.bon).length;
    marquerFait("L" + E.teil, E.serie);
    const faits = lire("lesen_teile", {}); faits[E.teil] = {bons, n, serie: E.serie.id, quand: Date.now()}; ecrire("lesen_teile", faits);
    const mot = bons / n >= 0.8 ? "l_mark_bien" : bons / n >= 0.5 ? "l_mark_moyen" : "l_mark_faible";
    const k = TEILE.indexOf(E.teil), teilSuivant = TEILE[k + 1];
    const partieSuivante = (() => { const o = DTZ.parties, j = o.findIndex(p => p.id === "L"); return j >= 0 && j + 1 < o.length ? o[j + 1] : null; })();
    const teil = E.teil, serie = E.serie;
    $("zone").innerHTML =
      '<div class="bloc"><div class="lsection">' + esc(T("l_section", {n: teil.slice(1)})) + ' · ' + esc(T("l_recap")) + '</div>' +
        '<div class="score">' + esc(T("l_score", {b: bons, n})) + '</div>' +
        '<p class="petit" style="text-align:center">' + esc(T("l_points", {p: bons * 3, s: n * 3})) + '</p>' +
        '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T(mot)) + '</div></div></div>' +
      '<div class="bloc">' + lignesCorrige(qs, E.rep) + '</div>' +
      '<div class="bloc lboutons">' +
        '<button class="secondaire" id="lRefaire">' + esc(T("l_refaire")) + '</button>' +
        (teilSuivant ? '<button class="secondaire" id="lSuivant">' + esc(T("l_suivante", {t: "Teil " + teilSuivant.slice(1) + " · " + titreTeil(teilSuivant)})) + '</button>'
          : partieSuivante ? '<button class="secondaire" id="lSuivant">' + esc(T("l_section_suivante", {t: partieSuivante.titre})) + '</button>' : "") +
        '<button class="secondaire" id="lToutes">' + esc(T("l_toutes")) + '</button></div>';
    $("lRefaire").onclick = () => ouvrirTeil(teil, serie);
    if ($("lSuivant")) $("lSuivant").onclick = () => teilSuivant ? ouvrirTeil(teilSuivant) : partieSuivante.ouvrir();
    $("lToutes").onclick = liste;
    DTZ.surRetour(() => { liste(); return true; });
    window.scrollTo(0, 0);
  }

  // ============ L'EPREUVE ENTIERE, MINUTEE ============
  // opts : {serie (id), minutes (45), fin(resultat)} -- avec fin(), l'examen blanc du bloc recoit le resultat au
  // lieu de l'ecran de resultat : {serie, bons, sur: 18, points, sur_points: 54, rep: {nr: reponse}}.
  async function lancer(opts){
    opts = opts || {};
    const s = (opts.serie && E.donnees.series.find(x => x.id === opts.serie)) || await choisirSerie(E.donnees.series, () => [], "Lexamen");
    const qs = toutes(s);
    E.ex = {s, qs, rep: {}, teil: "T1", opts, debut: Date.now(), rendu: false};
    DTZ.surRetour(() => {
      if (!E.ex || E.ex.rendu) return false;
      confirmer(T("l_quitter_q"), () => { arreterChrono(); E.ex = null; if (opts.fin) opts.fin(null); else liste(); }, T("l_quitter"));
      return true;
    });
    $("titre").textContent = T("l_titre") + " · Lesen";
    chrono((opts.minutes || 45) * 60, "bas", () => { if (E.ex && !E.ex.rendu){ rendre(true); } });
    pageExamen(true);
  }
  function pageExamen(premiere){
    const x = E.ex, s = x.s, teil = x.teil;
    const reste = t => x.qs.filter(q => q.teil === t && x.rep[q.nr] === undefined).length;
    let h = (premiere ? '<div class="bloc"><p class="petit">' + esc(T("l_regles")) + '</p></div>' : "") +
      '<div class="onglets">' + TEILE.map(t => '<button class="onglet' + (t === teil ? " actif" : "") + '" data-o="' + t + '">Teil ' + t.slice(1) +
        (reste(t) ? ' <span class="n">· ' + reste(t) + '</span>' : " ✓") + '</button>').join("") + '</div>';
    h += '<div class="bloc"><div class="lsection">' + esc(T("l_section", {n: teil.slice(1)})) + ' · ' + esc(titreTeil(teil)) + '</div>' + consigne(teil);
    const qs = x.qs.filter(q => q.teil === teil);
    const etat = q => ({r: x.rep[q.nr], montrer: false, fige: false});
    if (teil === "T1"){
      h += qs.map(q => '<div class="q"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage" lang="de">' + esc(q.frage) + '</span></div>' + boutons(q, etat(q)) + '</div>').join("");
      h += '<div class="doc annonces" lang="de" dir="ltr">' + s.T1.anzeigen.map(a => '<div class="annonce"><span class="l">' + a.b + '</span><div class="t">' + esc(a.titel) + '</div>' + esc(a.text) + '</div>').join("") + '</div>';
    } else if (teil === "T3"){
      h += '<div class="choix">' + s.T3.saetze.map(p => '<div class="q" style="padding:8px 10px"><div class="tete"><span class="num">' + p.b + '</span>' + deS(p.de) + '</div></div>').join("") + '</div>';
      h += qs.map(q => courriel(q.mail) + '<div class="q"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage">' + esc(T("l_quelle_phrase")) + '</span></div>' +
        '<div class="choix ligne">' + q.options.map(l => '<button class="opt' + (x.rep[q.nr] === l ? " pris" : "") + '" data-q="' + q.nr + '" data-v="' + l + '"><b>' + l + '</b></button>').join("") + '</div></div>').join("");
    } else {
      h += texte(s[teil].text) + qs.map(q => '<div class="q"><div class="tete"><span class="num">' + q.nr + '</span><span class="frage" lang="de">' + esc(q.frage) + '</span></div>' + boutons(q, etat(q)) + '</div>').join("");
    }
    h += '</div>';
    $("zone").innerHTML = h;
    document.querySelectorAll("[data-o]").forEach(b => b.onclick = () => { x.teil = b.dataset.o; pageExamen(); window.scrollTo(0, 0); });
    document.querySelectorAll("#zone .opt[data-q]").forEach(b => b.onclick = () => {
      const q = x.qs.find(y => String(y.nr) === b.dataset.q);
      x.rep[q.nr] = q.kind === "lettre" ? b.dataset.v : Number(b.dataset.v);
      b.parentNode.querySelectorAll(".opt").forEach(o => o.classList.toggle("pris", o === b));
      // le compteur de l'onglet suit les reponses
      const o = document.querySelector('[data-o="' + teil + '"]'); const n = reste(teil);
      if (o) o.innerHTML = "Teil " + teil.slice(1) + (n ? ' <span class="n">· ' + n + '</span>' : " ✓");
    });
    const i = TEILE.indexOf(teil), suite = $("suite");
    suite.hidden = false;
    suite.textContent = i < TEILE.length - 1 ? T("l_continuer") + " · Teil " + (i + 2) : T("l_rendre");
    suite.onclick = () => {
      if (i < TEILE.length - 1){ x.teil = TEILE[i + 1]; pageExamen(); window.scrollTo(0, 0); return; }
      const vides = x.qs.filter(q => x.rep[q.nr] === undefined).length;
      if (vides) confirmer(T("l_rendre_q", {n: vides}), () => rendre(false), T("l_oui_rendre")); else rendre(false);
    };
    if (premiere) window.scrollTo(0, 0);
  }
  function rendre(tempsFini){
    const x = E.ex; if (!x || x.rendu) return;
    x.rendu = true; arreterChrono(); silence();
    const bons = x.qs.filter(q => x.rep[q.nr] === q.bon).length, pts = bons * 3;
    const res = {serie: x.s.id, bons, sur: x.qs.length, points: pts, sur_points: x.qs.length * 3, rep: Object.assign({}, x.rep), secondes: Math.round((Date.now() - x.debut) / 1000)};
    marquerFait("Lexamen", x.s);
    resultat("L", res);
    if (x.opts.fin){ E.ex = null; x.opts.fin(res); return; }
    const part = pts / 54, niv = part >= 0.7 ? "b1" : part >= 0.4 ? "a2" : "moins";
    const rep = x.qs.map(q => x.rep[q.nr] === undefined ? null : x.rep[q.nr]);
    $("suite").hidden = true;
    $("titre").textContent = T("l_titre") + " · " + T("l_resultat");
    $("zone").innerHTML =
      '<div class="bloc">' + (tempsFini ? '<p class="petit"><b>' + esc(T("l_temps_fini")) + '</b></p>' : "") +
        '<div class="score">' + esc(T("l_score", {b: bons, n: x.qs.length})) + '</div>' +
        '<p style="text-align:center"><b>' + esc(T("l_sur54", {p: pts})) + '</b></p>' +
        '<p class="petit">' + esc(T("l_niv_" + niv)) + '</p><p class="petit">' + esc(T("l_regle")) + '</p>' +
        '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T("l_mark_v_" + niv)) + '</div></div></div>' +
      '<div class="bloc"><h2>' + esc(T("l_corrige")) + '</h2>' + lignesCorrige(x.qs, rep) + '</div>' +
      '<div class="bloc lboutons"><button class="secondaire" id="lEncore">' + esc(T("l_refaire_epreuve")) + '</button>' +
        '<button class="secondaire" id="lToutes">' + esc(T("l_toutes")) + '</button></div>';
    $("lEncore").onclick = () => lancer({});
    $("lToutes").onclick = liste;
    DTZ.surRetour(() => { liste(); return true; });
    window.scrollTo(0, 0);
  }

  DTZ.partie({id: "L", ordre: 10, titre: T("l_titre"), sous: T("l_sous"), ouvrir: () => liste()});
  // pour l'examen blanc du bloc et pour les controles : les donnees, les questions d'une serie, l'epreuve minutee
  return {
    get series(){ return E.donnees ? E.donnees.series : []; },
    questions: s => toutes(s),
    lancer,
    ouvrir: liste
  };
})();
window.TELC_LESEN = TELC_LESEN;
