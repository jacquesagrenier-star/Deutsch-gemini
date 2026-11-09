// LE TELC A2·B1 AVEC MARK ET ANNA -- LES SPRACHBAUSTEINE (4 nov. 2026, session « examens DTZ / telc »).
//
// Le format du telc (preparation-examens/FORMAT-TELC.md) : une lettre ou un courriel complet, 10 trous, 3 choix
// par trou, 0,5 point chacun. Les seules questions de grammaire de l'examen. Les lettres sont ecrites pour Wortando
// (donnees/sprachbausteine.json), jamais reprises du telc.
//
// L'ORGANISATION EST CELLE DE L'ORAL DU DTZ (decision de Jacques du 4 nov., « DTZ, l'oral : sections et
// exercices » : « Meme organisation pour le futur bloc telc ») :
//   - la liste des sections : l'accueil de commun.js (les tuiles), ou le panneau du bloc telc dans l'app quand la
//     page est ouverte directement sur cette partie (?partie=SB) ;
//   - dans la section, UNE PAGE PAR EXERCICE (ici, par trou) : « Section · Sprachbausteine », des points de
//     progression qu'on touche pour sauter a un trou, « ‹ » vers la liste, « Continuer » en bas ;
//   - en fin de section, le recapitulatif des reponses et du retour de Mark, puis Refaire la section / Section
//     suivante / Toutes les sections.
//
// Ce module ne connait de commun.js que ses fonctions publiques ($, esc, T, TXT, parler, lire, ecrire, DTZ, accueil,
// MARK_IMG) ; il s'inscrit par DTZ.partie() comme hoeren-lesen.js.

"use strict";

// TOUT LE MODULE DANS SA PORTEE : les modules du telc partagent la page (telc.html), et des noms comme
// points(), recap() ou continuer() se remplaceraient l'un l'autre sans rien dire. Seul SB sort (window.SB).
(() => {

// Les textes en francais et en anglais (telc-commun.js : textesTelc). Les explications des trous et la situation
// viennent des donnees : erkl_fr / erkl_en, situation_fr / situation_en (champTelc ; le francais tant que l'anglais
// manque).
const SB_EN = {
  sb_titre: "Sprachbausteine",
  sb_sous: "A letter, 10 gaps",
  sb_section: "Section · Sprachbausteine",
  sb_consigne_fr: "Read the letter. For each gap, choose the word that fits.",
  sb_mark_debut: "At telc, the Sprachbausteine come right after the reading: a letter with 10 gaps. Each gap is worth only half a point, but these are the only grammar questions in the whole exam. My tip: always read what comes BEFORE and AFTER the gap — the case, the position of the verb, the preposition that follows.",
  sb_trou: "Gap {n}",
  sb_question: "Which word goes in this gap?",
  sb_juste: "Correct!",
  sb_faux: "Not quite: it's “{m}”.",
  sb_recap: "Summary",
  sb_score: "{n} out of 10",
  sb_points: "In the exam, that would be {p} point(s) out of 5.",
  sb_mark_bien: "Very good! You already spot what the gap needs. Keep that habit on exam day.",
  sb_mark_moyen: "Not bad! Reread the explanations for the gaps you missed: the same traps keep coming back (the case after a preposition, the verb at the end after “weil” or “dass”).",
  sb_mark_faible: "It's a start, and that's normal. Reread each explanation below, then do the letter again: you'll see the same little words always come back.",
  sb_refaire: "Redo the section",
  sb_suivante: "Next section",
  sb_toutes: "All sections",
  sb_situation: "The situation",
  sb_de: "From", sb_a: "To", sb_objet: "Subject"
};
textesTelc({ en: SB_EN, fr: {
  sb_titre: "Sprachbausteine",
  sb_sous: "Une lettre, 10 trous",
  sb_section: "Section · Sprachbausteine",
  sb_consigne_de: "Lesen Sie den Brief. Welches Wort passt in die Lücke? Wählen Sie a, b oder c.",
  sb_consigne_fr: "Lis la lettre. Pour chaque trou, choisis le mot qui convient.",
  sb_mark_debut: "Au telc, les Sprachbausteine viennent juste après la lecture : une lettre avec 10 trous. Chaque trou ne vaut qu'un demi-point, mais ce sont les seules questions de grammaire de l'examen. Mon truc : lis toujours ce qui vient AVANT et APRÈS le trou — le cas, la place du verbe, la préposition qui suit.",
  sb_trou: "Trou {n}",
  sb_question: "Quel mot va dans ce trou ?",
  sb_juste: "Juste !",
  sb_faux: "Pas tout à fait : c'est « {m} ».",
  sb_recap: "Récapitulatif",
  sb_score: "{n} sur 10",
  sb_points: "À l'examen, cela ferait {p} point(s) sur 5.",
  sb_mark_bien: "Très bien ! Tu repères déjà ce que le trou demande. Garde ce réflexe le jour de l'examen.",
  sb_mark_moyen: "Pas mal ! Relis les explications des trous ratés : ce sont souvent les mêmes pièges qui reviennent (le cas après la préposition, le verbe à la fin après « weil » ou « dass »).",
  sb_mark_faible: "C'est le début, et c'est normal. Relis chaque explication ci-dessous, puis refais la lettre : tu verras que les mêmes petits mots reviennent toujours.",
  sb_refaire: "Refaire la section",
  sb_suivante: "Section suivante",
  sb_toutes: "Toutes les sections",
  sb_situation: "La situation",
  sb_de: "De", sb_a: "À", sb_objet: "Objet"
}});

const SB = { series: [], serie: null, rep: [], i: 0 };
// « De : » en francais, « From: » en anglais
const DEUXPTS = () => LANGUE === "fr" ? " : " : ": ";

DTZ.charger(fetch("donnees/sprachbausteine.json", { cache: "no-cache" })
  .then(r => { if (!r.ok) throw new Error("sprachbausteine.json"); return r.json(); })
  .then(d => { SB.series = d.series || []; }));

DTZ.partie({ id: "SB", ordre: 20, titre: T("sb_titre"), sous: T("sb_sous"), ouvrir: () => ouvrirSB() });

// LA LETTRE DU JOUR : choisirSerie() de commun.js, la moins recemment faite (les trous ne portent pas de mots
// du corpus a faire reviser : la liste des mots est vide). L'examen blanc du telc n'existe pas encore : le profil
// garde 0 serie pour lui (seriesExamen, telc.html), et les quatre lettres servent toutes a l'entrainement.
async function ouvrirSB(serie){
  SB.serie = serie || await choisirSerie(SB.series, () => [], "SB");
  SB.rep = SB.serie.luecken.map(() => null);
  SB.i = 0;
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  pageTrou();
}

function toutesLesSections(){
  if (TELC.direct){ silence(); parler("fermer"); if (window.parent === window) accueil(); return; }
  accueil();
}

// les points de progression : un par trou, on les touche pour y aller
function points(){
  return '<div class="points" role="tablist">' + SB.serie.luecken.map((l, k) => {
    const r = SB.rep[k], etat = r === null ? "" : (r === l.bon ? " ok" : " ko");
    return '<button class="point' + etat + (k === SB.i ? " ici" : "") + '" data-aller="' + k + '" aria-label="' + esc(T("sb_trou", {n: l.n})) + '">' + l.n + '</button>';
  }).join("") + '</div>';
}

// un trou dans la lettre : vide, choisi (juste ou faux), ou celui de la page
function trou(n){
  const k = SB.serie.luecken.findIndex(l => l.n === n);
  const l = SB.serie.luecken[k], r = SB.rep[k];
  if (r === null) return '<span class="trou' + (k === SB.i ? " actif" : "") + '" id="trou' + n + '">(' + n + ')</span>';
  return '<span class="trou ' + (r === l.bon ? "ok" : "ko") + (k === SB.i ? " actif" : "") + '" id="trou' + n + '">' + esc(l.o[r]) + '</span>';
}

function lettre(apresParagraphe){
  const s = SB.serie;
  const tete = '<div class="k">' + (s.registre === "formel" ? "Brief" : "E-Mail") + '</div>' +
    '<div class="petit" lang="de">' + esc(T("sb_de")) + DEUXPTS() + esc(s.von) + ' · ' + esc(T("sb_a")) + DEUXPTS() + esc(s.an) + '</div>' +
    '<div class="objet" lang="de">' + esc(s.betreff) + '</div>';
  const corps = s.absaetze.map((p, k) => {
    const html = esc(p).replace(/\{(\d+)\}/g, (m, n) => trou(Number(n)));
    return '<p lang="de">' + html + '</p>' + (apresParagraphe && apresParagraphe(k, p) || "");
  }).join("");
  return '<div class="doc lettre" dir="ltr">' + tete + corps + '</div>';
}

function pageTrou(){
  silence(); $("titre").textContent = T("sb_titre");
  const s = SB.serie, l = s.luecken[SB.i], r = SB.rep[SB.i];
  const ici = new RegExp("\\{" + l.n + "\\}");
  const carte = () => {
    const opts = l.o.map((o, k) => {
      let cls = "opt";
      if (r !== null){ if (k === l.bon) cls += " juste"; else if (k === r) cls += " faux"; }
      return '<button class="' + cls + '" data-choix="' + k + '"' + (r !== null ? " disabled" : "") + '><b>' + "abc"[k] + '</b><span lang="de">' + esc(o) + '</span></button>';
    }).join("");
    const aide = r === null ? "" :
      '<div class="aide"><div class="verdict ' + (r === l.bon ? "ok" : "ko") + '">' + esc(r === l.bon ? T("sb_juste") : T("sb_faux", {m: l.o[l.bon]})) + '</div>' +
      '<div class="dit"><img src="' + MARK_IMG + '" alt="Mark"><span class="erkl">' + esc(champTelc(l, "erkl")) + '</span></div></div>';
    return '<div class="q" id="carte"><div class="tete"><span class="num">' + l.n + '</span><span class="frage">' + esc(T("sb_question")) + '</span></div>' +
      '<div class="choix">' + opts + '</div>' + aide + '</div>';
  };
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("sb_section")) + '</div>' + points() + '</div>' +
    (SB.i === 0 && r === null && SB.rep.every(x => x === null)
      ? '<div class="bloc"><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T("sb_mark_debut")) + '</div></div>' + TELC.noteEntrainement() + '</div>' : "") +
    '<div class="bloc"><p class="consigne" lang="de">' + esc(T("sb_consigne_de")) + '<span class="fr">' + esc(T("sb_consigne_fr")) + '</span></p>' +
    '<p class="petit"><b>' + esc(T("sb_situation")) + DEUXPTS().trimEnd() + '</b> ' + esc(champTelc(s, "situation")) + '</p>' +
    lettre((k, p) => ici.test(p) ? carte() : "") + '</div>';
  document.querySelectorAll("[data-aller]").forEach(b => b.onclick = () => { SB.i = Number(b.dataset.aller); pageTrou(); });
  document.querySelectorAll("[data-choix]").forEach(b => b.onclick = () => choisir(Number(b.dataset.choix)));
  const suite = $("suite");
  suite.hidden = r === null; suite.textContent = T("continuer");
  suite.onclick = continuer;
  const cible = $("carte");
  if (cible) setTimeout(() => { try{ cible.scrollIntoView({block: "center", behavior: SB.i === 0 ? "auto" : "smooth"}); }catch(e){} }, 30);
}

function choisir(k){
  if (SB.rep[SB.i] !== null) return;
  SB.rep[SB.i] = k;
  const juste = k === SB.serie.luecken[SB.i].bon;
  parler("exercice", { juste });
  pageTrou();
}

function continuer(){
  const reste = SB.rep.findIndex((r, k) => r === null && k > SB.i);
  const avant = SB.rep.findIndex(r => r === null);
  if (reste >= 0){ SB.i = reste; pageTrou(); return; }
  if (avant >= 0){ SB.i = avant; pageTrou(); return; }
  recap();
}

function recap(){
  silence(); $("suite").hidden = true;
  SB.i = -1;   // plus de trou « de la page » : la lettre du recapitulatif est complete
  const s = SB.serie, bons = s.luecken.filter((l, k) => SB.rep[k] === l.bon).length;
  marquerFait("SB", s);
  resultat("SB", { serie: s.id, bons, sur: 10 });
  const mot = bons >= 8 ? "sb_mark_bien" : bons >= 5 ? "sb_mark_moyen" : "sb_mark_faible";
  const lignes = s.luecken.map((l, k) => {
    const ok = SB.rep[k] === l.bon;
    return '<div class="q"><div class="tete"><span class="num">' + l.n + '</span><span class="frage">' +
      (ok ? '<span class="ok">✓</span> ' : '<span class="ko">✗</span> <s lang="de">' + esc(l.o[SB.rep[k]]) + '</s> → ') +
      '<b lang="de">' + esc(l.o[l.bon]) + '</b></span></div><p class="erkl">' + esc(champTelc(l, "erkl")) + '</p></div>';
  });
  // ce qui est rate d'abord : c'est ce qu'on vient relire
  const rates = lignes.filter((x, k) => SB.rep[k] !== s.luecken[k].bon), justes = lignes.filter((x, k) => SB.rep[k] === s.luecken[k].bon);
  $("titre").textContent = T("sb_titre");
  $("zone").innerHTML =
    '<div class="bloc"><div class="section">' + esc(T("sb_section")) + ' · ' + esc(T("sb_recap")) + '</div>' +
      '<div class="score">' + esc(T("sb_score", {n: bons})) + '</div>' +
      '<p class="petit" style="text-align:center">' + esc(T("sb_points", {p: String(bons / 2).replace(".", ",")})) + '</p>' +
      '<div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T(mot)) + '</div></div></div>' +
    '<div class="bloc">' + lettre() + '</div>' +
    '<div class="bloc">' + rates.concat(justes).join("") + '</div>' +
    '<div class="bloc boutons">' +
      '<button class="secondaire" id="sbRefaire">' + esc(T("sb_refaire")) + '</button>' +
      '<button class="secondaire" id="sbToutes">' + esc(T("sb_toutes")) + '</button></div>';
  $("sbRefaire").onclick = () => ouvrirSB(s);
  TELC.continuerPartie("SB");
  $("sbToutes").onclick = toutesLesSections;
  DTZ.surRetour(() => { toutesLesSections(); return true; });
  window.scrollTo(0, 0);
}

window.SB = SB;
})();
