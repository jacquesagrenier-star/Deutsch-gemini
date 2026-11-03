// LE DTZ AVEC MARK ET ANNA -- CE QUI SERT A TOUTES LES PARTIES (3 nov. 2026).
//
// Une page (dtz.html), ce fichier, un module par epreuve : hoeren-lesen.js (Ecouter, Lire) et
// sprechen-schreiben.js (Parler, Ecrire, session « Preparation au DTZ avec Mark et Anna »). Decide par Jacques le
// 3 nov. : c'est une REPETITION -- Mark aide l'eleve a preparer le DTZ, Anna joue l'examinatrice ; l'eleve repond
// pour lui-meme. Mark ne passe pas l'examen.
//
// UN MODULE S'INSCRIT par DTZ.partie() et DTZ.examen() ; l'accueil construit ses tuiles et ses examens blancs a
// partir de ces inscriptions, et ne connait aucune epreuve en particulier :
//   DTZ.partie({id, titre, sous, ordre, ouvrir})        une tuile d'entrainement (ouvrir() affiche ses Teile) ;
//   DTZ.examen({id, titre, sous, ordre, lancer})        un examen blanc de l'accueil ;
//   DTZ.charger(promesse)                               ses donnees, attendues avant l'accueil ;
//   DTZ.surRetour(fn)                                   ce que fait le rond « ‹ » dans l'ecran en cours (fn() vrai =
//                                                       traite ; sinon l'accueil, puis la fermeture du cadre).
// Une tuile sans module charge (Ecrire et Parler tant que leur fichier n'est pas la) s'affiche grisee : « bientot ».
//
// LE VERDICT DE L'EXAMEN ENTIER (Pruefungshandbuch, ch. 1) : Hoeren + Lesen sur 45, A2 des 20, B1 des 33 ;
// Schreiben et Sprechen A2 ou B1 sur criteres ; B1 global = B1 a l'oral ET dans un des deux ecrits.
// DTZ.niveauGlobal() le calcule ; chaque module y verse son resultat par DTZ.resultat().

"use strict";
const Q = new URLSearchParams(location.search);
const LANGUE = (l => ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"].includes(l) ? l : "fr")(((Q.get("lang") || "fr").toLowerCase().split(/[-_]/)[0]));
if (Q.get("nuit") === "1") document.documentElement.classList.add("nuit");
document.documentElement.lang = LANGUE;
document.documentElement.dir = (LANGUE === "fa" || LANGUE === "ar") ? "rtl" : "ltr";
const RAPIDE = Q.get("rapide") === "1";          // pauses raccourcies : pour les essais seulement
const SERIES_EXAMEN = 3;                          // les series 1-3 sont gardees pour l'examen blanc
const MARK_IMG = "../descripcion/Mark-visage.webp";
const ANNA_IMG = "../descripcion/Anna-visage.webp";

// L'INTERFACE : le francais d'abord (maquette du 3 nov. 2026) ; les huit autres langues avant l'ouverture aux
// eleves, ici, comme TEXTES des themes illustres. Un module ajoute ses cles par Object.assign(TXT, {...}).
// Une cle sans traduction retombe sur le francais.
const TXT = {
  titre: "Le DTZ avec Mark et Anna",
  intro: "Le DTZ, c'est l'examen de la fin du cours d'intégration. Je t'aide à le préparer : les messages de mon répondeur, mon courrier, la radio de Berlin… c'est exactement ce qu'on y trouve.",
  entrainement: "Entraînement avec Mark et Anna",
  entrainement_s: "Une partie à la fois, avec une explication après chaque réponse.",
  examen: "Examen blanc",
  examen_s: "Comme le jour de l'examen : minuté, le son une seule fois, sans aide.",
  bientot: "bientôt",
  dernier: "Dernier examen blanc : {s} — {n}",
  suivant: "Suivant", terminer: "Terminer", recommencer: "Recommencer", accueil: "Retour au DTZ",
  feuille: "Feuille de réponses", fermer: "Fermer", continuer: "Continuer",
  verdict: "Verdict", sur: "sur {n}",
  niv_b1: "B1", niv_a2: "A2", niv_moins: "sous A2",
  voix_tel: "Voix du téléphone (maquette) : les voix enregistrées viendront ensuite.",
  maquette: "Maquette : une seule série pour l'instant (série 1), utilisée aussi en entraînement.",
  quitter_q: "Quitter l'examen blanc ? Il ne sera pas compté.", quitter: "Quitter"
};
function T(cle, v){ let s = TXT[cle] || cle; for (const k in (v || {})) s = s.split("{" + k + "}").join(v[k]); return s; }

const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
const ABC = "abcdefghx";
function parler(type, extra){ try{ if (window.parent !== window) parent.postMessage(Object.assign({source: "wortando-scene", type}, extra || {}), "*"); }catch(e){} }
function lire(cle, defaut){ try{ const v = localStorage.getItem("wortando_dtz_" + cle); return v ? JSON.parse(v) : defaut; }catch(e){ return defaut; } }
function ecrire(cle, v){ try{ localStorage.setItem("wortando_dtz_" + cle, JSON.stringify(v)); }catch(e){} }

// ============ LA VOIX ============
// La voix du telephone, en attendant les fichiers : une voix allemande, et pour les dialogues une hauteur par
// personne, pour qu'on entende qui parle. Les fichiers ElevenLabs (v2) prendront la place sans rien changer d'autre.
// DTZ_VOIX : {cle: {sexe}} que chaque module remplit avec ses voix (hoeren.json : « voix »).
const DTZ_VOIX = {};
let VOIX_DE = [];
function chargerVoix(){ try{ VOIX_DE = speechSynthesis.getVoices().filter(v => /^de(-|_|$)/i.test(v.lang)); }catch(e){ VOIX_DE = []; } }
try{ chargerVoix(); speechSynthesis.onvoiceschanged = chargerVoix; }catch(e){}
const HAUTEUR = {aurora: 1, mark: 0.92, anna: 1.06, beamter: 0.8, nachbar: 0.86, dame: 1.12, baeckerin: 1.05, radio_m: 0.95, radio_f: 1.08};
function dire(texte, wer){
  return new Promise(fin => {
    try{
      const u = new SpeechSynthesisUtterance(texte);
      u.lang = "de-DE";
      const sexe = (DTZ_VOIX[wer] || {}).sexe;
      const fem = VOIX_DE.filter(v => /female|frau|anna|petra|helena|katja|marlene|vicki|hedda|sabine/i.test(v.name));
      const mas = VOIX_DE.filter(v => /male|mann|markus|yannick|stefan|hans|conrad|klaus|daniel/i.test(v.name) && !/female/i.test(v.name));
      u.voice = (sexe === "m" ? mas[0] : fem[0]) || VOIX_DE[0] || null;
      u.pitch = HAUTEUR[wer] || 1; u.rate = 0.95;
      // un filet : sans voix allemande, ou si le navigateur refuse de parler hors d'un geste, « onend » ne vient
      // jamais et l'examen resterait fige ; on passe apres la duree qu'aurait prise la phrase
      let fait = false; const finir = () => { if (!fait){ fait = true; fin(); } };
      u.onend = u.onerror = finir;
      setTimeout(() => { if (!fait && RAPIDE) silence(); finir(); }, RAPIDE ? 1500 : 2000 + texte.length * 90);
      speechSynthesis.speak(u);
    }catch(e){ setTimeout(fin, 50); }
  });
}
function silence(){ try{ speechSynthesis.cancel(); }catch(e){} }
async function jouerRepliques(lignes){ for (const l of lignes || []) await dire(l.text, l.wer); }
const attendre = s => new Promise(r => setTimeout(r, RAPIDE ? Math.min(400, s * 1000) : s * 1000));
const ICONE_SON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4zm12.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>';

// ============ LA MINUTERIE ============
let chronoId = null;
function arreterChrono(){ if (chronoId) clearInterval(chronoId); chronoId = null; $("chrono").hidden = true; }
// sens « bas » : a rebours, fin() a zero, en rouge les 5 dernieres minutes ; « haut » : le temps ecoule
function chrono(secondes, sens, fin){
  arreterChrono();
  const debut = Date.now(); $("chrono").hidden = false;
  const tic = () => {
    const ecoule = Math.floor((Date.now() - debut) / 1000), reste = Math.max(0, secondes - ecoule);
    const v = sens === "bas" ? reste : ecoule;
    $("chrono").textContent = Math.floor(v / 60) + ":" + String(v % 60).padStart(2, "0");
    $("chrono").classList.toggle("court", sens === "bas" && reste <= 300);
    if (sens === "bas" && reste <= 0){ arreterChrono(); fin && fin(); }
  };
  tic(); chronoId = setInterval(tic, 1000);
}

// ============ LE PANNEAU (feuille de reponses, confirmations) ============
function ouvrir(h){ $("panneau").innerHTML = h; $("voile").hidden = false; }
function fermerPanneau(){ $("voile").hidden = true; }
$("voile").onclick = ev => { if (ev.target === $("voile")) fermerPanneau(); };
// une question a deux boutons ; oui() si la personne confirme
function confirmer(question, oui, libOui){
  ouvrir('<p><b>' + esc(question) + '</b></p><button class="secondaire" id="ouiP">' + esc(libOui) + '</button><button class="secondaire" id="nonP">' + T("continuer") + '</button>');
  $("ouiP").onclick = () => { fermerPanneau(); oui(); };
  $("nonP").onclick = fermerPanneau;
}

// ============ LA SERIE SUIT LES MOTS ============
// Comme tirage.js des themes illustres : parmi les series d'entrainement, celle dont les mots cles sont le plus dus
// ou neufs ; a egalite, la moins recemment faite (cle : ce que l'on entraine, « HT3 » par exemple). Les series 1-3
// sont gardees pour l'examen blanc, sauf tant qu'il n'y en a pas d'autres (la maquette n'a que la serie 1).
async function choisirSerie(series, motsDe, cle){
  const pool = series.length > SERIES_EXAMEN ? series.slice(SERIES_EXAMEN) : series;
  if (pool.length === 1) return pool[0];
  const faits = lire("faits", {});
  const notes = await Promise.all(pool.map(async s => {
    const mots = motsDe(s), etats = await Tirage.demander(mots);
    const utiles = etats ? etats.filter(e => e && (e.e === "d" || e.e === "n")).length : mots.length;
    return {s, utiles, quand: faits[cle + s.id] || 0};
  }));
  notes.sort((a, b) => b.utiles - a.utiles || a.quand - b.quand);
  return notes[0].s;
}
function marquerFait(cle, s){ const faits = lire("faits", {}); faits[cle + s.id] = Date.now(); ecrire("faits", faits); }

// ============ LE VERDICT DE L'EXAMEN ENTIER ============
// hl : points Hoeren + Lesen sur 45 (ou null) ; schreiben, sprechen : "B1" | "A2" | "moins", en majuscules ou non (ou null).
// Le B1 global demande le B1 a l'oral ET dans un ecrit (Hoeren+Lesen ou Schreiben).
function niveauHL(points){ return points >= 33 ? "b1" : points >= 20 ? "a2" : "moins"; }
function niveauGlobal(hl, schreiben, sprechen){
  // l'oral et l'ecrit envoient « B1 » / « A2 » / « moins » : on accepte les deux casses
  schreiben = schreiben ? String(schreiben).toLowerCase() : null; sprechen = sprechen ? String(sprechen).toLowerCase() : null;
  const nhl = hl === null || hl === undefined ? null : niveauHL(hl);
  if (sprechen === "b1" && (nhl === "b1" || schreiben === "b1")) return "b1";
  const tous = [nhl, schreiben, sprechen].filter(Boolean);
  if (tous.length && tous.some(n => n !== "moins")) return "a2";
  return tous.length ? "moins" : null;
}
// le dernier resultat de chaque epreuve, garde pour l'accueil et le verdict global
function resultat(epreuve, valeur){ const r = lire("resultats", {}); r[epreuve] = Object.assign({quand: Date.now()}, valeur); ecrire("resultats", r); }

// ============ LES INSCRIPTIONS ET L'ACCUEIL ============
const DTZ = {
  parties: [], examens: [], chargements: [], retour: null,
  partie(p){ this.parties.push(p); this.parties.sort((a, b) => a.ordre - b.ordre); },
  examen(e){ this.examens.push(e); this.examens.sort((a, b) => a.ordre - b.ordre); },
  charger(pr){ this.chargements.push(pr); },
  surRetour(fn){ this.retour = fn; },
  niveauGlobal, niveauHL, resultat
};
// les quatre tuiles de l'examen, dans l'ordre du DTZ ; celles qu'aucun module n'a inscrites restent grisees
const TUILES = [{id: "H", titre: "Écouter", sous: "Hören"}, {id: "L", titre: "Lire", sous: "Lesen"}, {id: "S", titre: "Écrire", sous: "Schreiben"}, {id: "Sp", titre: "Parler", sous: "Sprechen"}];
function accueil(){
  silence(); arreterChrono(); fermerPanneau(); DTZ.retour = null;
  $("titre").textContent = T("titre"); $("suite").hidden = true;
  const der = lire("dernier", null);
  const tuiles = TUILES.map(t => {
    const p = DTZ.parties.find(x => x.id === t.id);
    return p ? '<button class="tuile" data-ent="' + t.id + '">' + esc(p.titre) + '<small>' + esc(p.sous) + '</small></button>'
             : '<button class="tuile" disabled>' + esc(t.titre) + '<small>' + esc(t.sous) + ' · ' + T("bientot") + '</small></button>';
  }).join("");
  $("zone").innerHTML =
    '<div class="bloc"><div class="mark"><img src="' + MARK_IMG + '" alt="Mark"><div class="bulle">' + esc(T("intro")) + '</div></div></div>' +
    '<div class="bloc"><h2>' + T("entrainement") + '</h2><p class="petit">' + T("entrainement_s") + '</p><div class="tuiles">' + tuiles + '</div></div>' +
    '<div class="bloc"><h2>' + T("examen") + '</h2><p class="petit">' + T("examen_s") + '</p>' +
      DTZ.examens.map(e => '<button class="mode" data-ex="' + e.id + '"><b>' + esc(e.titre) + '</b><span>' + esc(e.sous) + '</span></button>').join("") +
      (der ? '<p class="dernier">' + T("dernier", {s: esc(der.date), n: esc(der.texte)}) + '</p>' : "") + '</div>' +
    '<p class="petit" style="text-align:center">' + T("maquette") + '<br>' + T("voix_tel") + '</p>';
  document.querySelectorAll("[data-ent]").forEach(b => b.onclick = () => DTZ.parties.find(p => p.id === b.dataset.ent).ouvrir());
  document.querySelectorAll("[data-ex]").forEach(b => b.onclick = () => DTZ.examens.find(e => e.id === b.dataset.ex).lancer());
  window.scrollTo(0, 0);
}

// ============ LE RETOUR ============
// L'ecran en cours decide d'abord (DTZ.surRetour) ; a defaut, retour a l'accueil ; de l'accueil, on ferme le cadre.
$("retour").onclick = () => {
  if (DTZ.retour && DTZ.retour()) return;
  if ($("zone").querySelector("[data-ent]") === null){ accueil(); return; }
  silence(); parler("fermer");
  if (window.parent === window) history.back();
};

// le demarrage, une fois les modules inscrits (appele en bas de dtz.html)
function demarrer(){
  Promise.all(DTZ.chargements).then(accueil)
    .catch(() => { $("zone").innerHTML = '<div class="bloc"><p>Les données du DTZ ne se chargent pas.</p></div>'; });
}
