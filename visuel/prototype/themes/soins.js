// LES THEMES ILLUSTRES DES SOINS (Wortando Pflege, « Ma journee au service », 16 nov. 2026).
//
// Le moteur commun des pages visuel/prototype/soins-theme-<cle>.html. Il suit le modele des themes illustres
// (visuel/THEMES-ILLUSTRES.md) : le tirage suit les mots (themes/tirage.js), jamais deux fois la meme sorte de suite,
// jamais deux fois la meme question dans une partie, les boutons tout en bas, la traduction APRES la reponse, la
// phrase juste dite en entier, le mot choisi traduit apres une erreur.
//
// UNE DIFFERENCE, VOULUE : les questions ne se fabriquent pas dans la page, mais dans le generateur du theme
// (pflege/outils/themes_soins/<cle>.py), depuis ses donnees, et arrivent en BANQUE dans soins-theme-<cle>/donnees.json.
// Ainsi chaque phrase allemande est connue d'avance : ses traductions dans les dix langues d'interface sont relues et
// controlees (aucune ne manque), les nombres sont deja en lettres, et la reserve se compte sans navigateur.
//
// La langue apprise est toujours l'allemand. Les langues d'interface : fr en es pt tr uk pl ru ar fa (decision de
// Jacques du 16 nov. : « la traduction pour la langue de l'apprenant dans toutes les langues [...] dont l'espagnol »).
//
// Ce que la page fournit avant de charger ce fichier : CLE (« schmerz »), et, si elle veut, des sortes de rendu de
// plus dans RENDUS_PAGE. Le reste est ici.
const Q = new URLSearchParams(location.search);
const APPRENDRE = "de";
const LANGUES_SOINS = ["fr", "en", "es", "pt", "tr", "uk", "pl", "ru", "ar", "fa"];
const LANGUE = (l => LANGUES_SOINS.includes(l) ? l : "fr")(((Q.get("lang") || "fr").toLowerCase().split(/[-_]/)[0]));
if (Q.get("nuit") === "1") document.documentElement.classList.add("nuit");
document.documentElement.lang = LANGUE;
document.documentElement.dir = (LANGUE === "fa" || LANGUE === "ar") ? "rtl" : "ltr";
const SEANCE = Q.get("seance") === "1";
// vingt questions seul, six dans la seance du jour (ou le reglage « Questions par scene et par theme »)
const NB = SEANCE ? Math.max(2, Math.min(12, parseInt(Q.get("nb"), 10) || 6)) : 20;
const NEUFS_MAX = SEANCE ? 3 : 10;

// les textes communs a tous les themes de soins ; ceux d'un theme sont dans sa donnee (D.textes)
const TEXTES_SOINS = {
  ecouter:   {fr:"Écouter", en:"Listen", es:"Escuchar", pt:"Ouvir", tr:"Dinle", uk:"Слухати", pl:"Posłuchaj", ru:"Слушать", ar:"استمع", fa:"گوش بده"},
  reecouter: {fr:"Réécouter", en:"Listen again", es:"Volver a escuchar", pt:"Ouvir de novo", tr:"Tekrar dinle", uk:"Послухати ще раз", pl:"Posłuchaj jeszcze raz", ru:"Послушать ещё раз", ar:"استمع مرة أخرى", fa:"دوباره گوش بده"},
  commencer: {fr:"Commencer", en:"Start", es:"Empezar", pt:"Começar", tr:"Başla", uk:"Почати", pl:"Zacznij", ru:"Начать", ar:"ابدأ", fa:"شروع"},
  suivant:   {fr:"Continuer", en:"Continue", es:"Continuar", pt:"Continuar", tr:"Devam", uk:"Далі", pl:"Dalej", ru:"Дальше", ar:"متابعة", fa:"ادامه"},
  terminer:  {fr:"Terminer", en:"Finish", es:"Terminar", pt:"Terminar", tr:"Bitir", uk:"Завершити", pl:"Zakończ", ru:"Завершить", ar:"إنهاء", fa:"پایان"},
  bonne:     {fr:"La bonne réponse : {r}", en:"The right answer: {r}", es:"La respuesta correcta: {r}", pt:"A resposta certa: {r}", tr:"Doğru cevap: {r}", uk:"Правильна відповідь: {r}", pl:"Prawidłowa odpowiedź: {r}", ru:"Правильный ответ: {r}", ar:"الإجابة الصحيحة: {r}", fa:"پاسخ درست: {r}"},
  score:     {fr:"{b} bonnes réponses sur {n}", en:"{b} correct answers out of {n}", es:"{b} respuestas correctas de {n}", pt:"{b} respostas certas de {n}", tr:"{n} sorudan {b} doğru", uk:"{b} правильних відповідей із {n}", pl:"{b} poprawnych odpowiedzi na {n}", ru:"{b} правильных ответов из {n}", ar:"{b} إجابات صحيحة من {n}", fa:"{b} پاسخ درست از {n}"},
  retourAria:{fr:"Retour", en:"Back", es:"Volver", pt:"Voltar", tr:"Geri", uk:"Назад", pl:"Wstecz", ru:"Назад", ar:"رجوع", fa:"بازگشت"},
  vrai:      {fr:"Richtig", en:"Richtig", es:"Richtig", pt:"Richtig", tr:"Richtig", uk:"Richtig", pl:"Richtig", ru:"Richtig", ar:"Richtig", fa:"Richtig"},
  faux:      {fr:"Falsch", en:"Falsch", es:"Falsch", pt:"Falsch", tr:"Falsch", uk:"Falsch", pl:"Falsch", ru:"Falsch", ar:"Falsch", fa:"Falsch"}
};
// les textes de l'encore et du « tout est revu » viennent de tirage.js ; l'espagnol n'y est pas encore
const TIRAGE_ES = {revu: "Todo está repasado por hoy.", encore: "Más preguntas", prochaine: "Próximo repaso: {d}"};
const tirageTexte = k => (TIRAGE_TEXTES[k] || {})[LANGUE] || (LANGUE === "es" ? TIRAGE_ES[k] : null) || TIRAGE_TEXTES[k].fr;

let D = null;
function T(cle, v){
  const t = (D && D.textes && D.textes[cle]) || TEXTES_SOINS[cle] || {};
  let s = t[LANGUE] || t.fr || cle;
  for (const k in (v || {})) s = s.split("{" + k + "}").join(v[k]);
  return s;
}

// ---------- utilitaires ----------
const $ = id => document.getElementById(id);
const melanger = a => a.map(v => [Math.random(), v]).sort((x, y) => x[0] - y[0]).map(v => v[1]);
const hasard = a => a[Math.floor(Math.random() * a.length)];
const cible = t => '<span lang="de" dir="ltr">' + t + '</span>';
// en persan et en arabe, un passage en lettres latines (un mot allemand cite) s'isole, sinon l'algorithme bidi le retourne
const isoler = s => document.documentElement.dir !== "rtl" ? s : s.replace(/[A-Za-zÀ-ÿßäöüÄÖÜ„“"]+(?:[ ()\-.,:„“"]+[A-Za-zÀ-ÿßäöüÄÖÜ„“"]+)*/g, m => '<span dir="ltr">' + m + '</span>');
const traduction = t => t ? '<span class="trad" dir="auto">' + isoler(t) + '</span>' : "";
function parler(type, extra){ try{ parent.postMessage(Object.assign({source: "wortando-scene", type}, extra || {}), "*"); }catch(e){} }
function dire(texte){ Voix.dire(texte); }
const HP = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';

// la traduction d'une phrase allemande de la banque (relue, dans les dix langues), et d'un mot (le corpus des Soins)
const tradPhrase = p => (((D.phrases || {})[p] || {})[LANGUE]) || null;
const glose = m => { const g = (m && m.glose) || {}; return g[LANGUE] || (LANGUE === "es" ? null : g.fr) || ""; };
// le mot choisi a-t-il une traduction sure ? seulement s'il est un mot de la donnee (D.gloses : texte -> {langue: ...})
const gloseTexte = t => { const g = (D.gloses || {})[t]; return g ? (g[LANGUE] || "") : ""; };

// ---------- les images ----------
// Une image qui manque encore (les images d'un theme se font apres ses textes) montre sa description, en gris :
// la page reste jouable, et l'on voit ce qui manque.
function srcImage(nom){ return "soins-theme-" + CLE + "/" + nom + ".webp"; }
function imageHtml(nom, classe){
  const desc = ((D.images || {})[nom] || {}).alt || nom;
  return '<img class="' + (classe || "photo") + '" alt="" src="' + srcImage(nom) + '" data-desc="' + desc.replace(/"/g, "&quot;") + '" onerror="this.outerHTML=\'<div class=&quot;' + (classe || "photo") + ' manque&quot;>\'+this.dataset.desc+\'</div>\'">';
}
// l'echelle de la douleur (NRS 0-10), dessinee : rien d'ecrit dans une image generee
function echelleHtml(n){
  const cases = [];
  for (let i = 0; i <= 10; i++){
    const teinte = i <= 3 ? "#7FC8A0" : i <= 6 ? "#F2C14E" : "#E07A5F";
    cases.push('<div class="case' + (i === n ? " pointee" : "") + '" style="--t:' + teinte + '"><b>' + i + '</b></div>');
  }
  return '<div class="echelle" dir="ltr" aria-hidden="true">' + cases.join("") + '</div>';
}
// ce qu'une question montre : une image, une echelle, un document, une citation, plusieurs choses
function visuelHtml(v){
  if (!v) return "";
  if (Array.isArray(v)) return v.map(visuelHtml).join("");
  if (v.img) return imageHtml(v.img);
  if (v.echelle !== undefined) return echelleHtml(v.echelle);
  if (v.doc) return '<div class="papier" lang="de" dir="ltr">' + v.doc + '</div>';
  if (v.cite) return '<div class="citation" dir="ltr">' + (v.visage ? imageHtml(v.visage, "visage") : "") + '<div class="bulle" lang="de">„' + v.cite + '“</div></div>';
  if (v.duo) return '<div class="duo">' + v.duo.map(n => imageHtml(n, "img")).join("") + '</div>';
  return "";
}

// ---------- la partie ----------
let file = [], rang = 0, bons = 0, repondu = false;
// LE MOT DE LA QUESTION (regle 3 des themes : un mot appris compte partout). « theme » : le theme de soins avec son
// niveau (soins_koerper_b1), pour que l'app fasse avancer la carte de SOINS et non une carte du corpus general.
let motQ = null, questionQ = null, choixTexte = null;
function viser(q){ questionQ = q; motQ = D.mots[q.mot]; }
function juger(ok, choisi){
  if (repondu) return; repondu = true;
  const q = questionQ;
  if (ok) bons++;
  parler("exercice", Tirage.question({juste: ok})); if (ok){ parler("bonne"); Voix.bravo(); }
  if (motQ) parler("reponse", {mot: motQ.mot, genre: motQ.genre || null, cat: motQ.cat || null, theme: motQ.theme || null, juste: ok});
  if (!ok && file[rang]) Tirage.remettre(file, rang, file[rang], NB);
  const m = $("msg"); m.className = "retourMsg " + (ok ? "ok" : "ko");
  const bonne = q.bonneTexte || q.bonne;
  const gChoisi = !ok && choisi ? gloseTexte(choisi) : "";
  m.innerHTML = (ok ? cible(D.bravo || "Sehr gut!") : T("bonne", {r: cible(bonne)}))
    + (q.phrase && (ok || q.phrase !== bonne) ? '<span class="phrase">' + cible(q.phrase) + '</span>' : "")
    + traduction(tradPhrase(q.phrase || bonne))
    + (q.aide ? '<span class="aide">' + isoler(T(q.aide)) + '</span>' : "")
    + (gChoisi ? '<span class="mot choisi"><s>' + cible(choisi) + '</s> · <span>' + gChoisi + '</span></span>' : "")
    + (motQ ? '<span class="mot' + (gChoisi ? " bon" : "") + '"><button type="button" class="ecoute" id="redire" aria-label="' + T("ecouter") + '">' + HP + '</button>'
             + cible(motQ.dit || motQ.affiche) + ' · <span>' + glose(motQ) + '</span></span>' : "");
  if (motQ) $("redire").addEventListener("click", () => dire(motQ.dit || motQ.affiche));
  dire(q.dit || q.phrase || bonne);
  const s = $("suite"); s.textContent = rang + 1 >= file.length ? T("terminer") : T("suivant"); s.hidden = false;
}
function boutons(conteneur, options, bonne){
  let bon;
  options.forEach(o => {
    const b = document.createElement("button"); b.type = "button"; b.lang = "de"; b.dir = "ltr"; b.textContent = o; if (o === bonne) bon = b;
    b.addEventListener("click", () => {
      conteneur.querySelectorAll("button").forEach(x => { x.disabled = true; if (x === bon) x.classList.add("juste"); });
      if (b !== bon) b.classList.add("faux");
      choixTexte = o;
      if ($("trou")) $("trou").textContent = bonne;
      juger(o === bonne, o);
    });
    conteneur.appendChild(b);
  });
}
function rangeeImages(conteneur, noms, bonne){
  let bon;
  conteneur.className = "rangee" + (noms.length === 3 ? " trois" : "");
  noms.forEach(n => {
    const b = document.createElement("button"); b.type = "button"; b.dataset.id = n;
    b.innerHTML = imageHtml(n, "img"); if (n === bonne) bon = b;
    b.addEventListener("click", () => {
      conteneur.querySelectorAll("button").forEach(x => { x.disabled = true; if (x === bon) x.classList.add("juste"); });
      if (b !== bon) b.classList.add("faux");
      juger(n === bonne, null);
    });
    conteneur.appendChild(b);
  });
}
const avecTrou = s => s.replace("___", '<span class="trou" id="trou">?</span>');
// UNE QUESTION DE LA BANQUE A L'ECRAN. Ses champs : sorte, mot (rang dans D.mots), consigne (cle de D.textes),
// visuel, enonce (allemand, avec ___ s'il y a un trou), choix (textes) OU images (noms), bonne, phrase (la phrase
// juste entiere), dit (ce que la voix dit apres, si ce n'est pas la phrase), ecoute (un texte a faire ecouter d'abord).
function poser(q){
  viser(q); choixTexte = null;
  const z = $("zone");
  z.innerHTML = '<p class="consigne">' + isoler(T(q.consigne)) + '</p>' + visuelHtml(q.visuel)
    + (q.ecoute ? '<button type="button" class="ecoute grand" id="ecoute" aria-label="' + T("reecouter") + '">' + HP + '</button>' : "")
    + (q.enonce ? '<div class="enonce' + (q.centre ? " centre" : "") + '">' + cible(avecTrou(q.enonce)) + '</div>' : "")
    + '<div class="choix' + (q.centre ? " centre" : "") + '" id="choix"></div><p class="retourMsg" id="msg"></p>';
  if (q.ecoute) $("ecoute").addEventListener("click", () => dire(q.ecoute));
  if (q.images) rangeeImages($("choix"), melanger(q.images.slice()), q.bonne);
  else boutons($("choix"), q.ordreFixe ? q.choix.slice() : melanger(q.choix.slice()), q.bonne);
  return true;
}

// LES SORTES : chaque sorte de la banque sait viser un mot (ses questions qui portent ce mot), sinon une au hasard
let BANQUE = {};
const EX = {};
function preparerSortes(){
  BANQUE = {};
  D.questions.forEach(q => { (BANQUE[q.sorte] = BANQUE[q.sorte] || []).push(q); });
  Object.keys(BANQUE).forEach(s => {
    EX[s] = w => {
      const cand = BANQUE[s].filter(q => !w || D.mots[q.mot] === w);
      if (!cand.length) return false;
      return poser(hasard(cand));
    };
  });
}
let SORTES = [];
function motsDuTheme(){ return D.mots.filter(m => !m.horsJeu); }
let vus = Tirage.vus(), sorteCourante = null, derniereSorte = null;
// la cle d'une question : sa sorte et son identifiant dans la banque (unique)
function cleQuestion(){ return sorteCourante + "|" + (questionQ ? questionQ.id : ""); }
function montrer(){
  repondu = false; $("suite").hidden = true;
  $("compte").textContent = (rang + 1) + " / " + file.length;
  $("barre").style.width = (rang / file.length * 100) + "%";
  const garde = dire; dire = () => {};
  const essai = (w, strict) => {
    const autres = melanger(SORTES.filter(x => x !== derniereSorte));
    for (const so of autres){
      for (let n = 0; n < 25; n++){
        motQ = null; questionQ = null; choixTexte = null; sorteCourante = so;
        if (!EX[so](w)) break;
        if (!vus.has(cleQuestion())) return so;
      }
    }
    if (strict) return null;
    if (derniereSorte) for (let n = 0; n < 25; n++){
      motQ = null; questionQ = null; sorteCourante = derniereSorte;
      if (!EX[derniereSorte](w)) break;
      if (!vus.has(cleQuestion())) return derniereSorte;
    }
    for (const so of autres.concat(derniereSorte ? [derniereSorte] : [])){
      motQ = null; questionQ = null; sorteCourante = so;
      if (EX[so](w)) return so;
    }
    return null;
  };
  let fait = essai(file[rang], true);
  for (let j = rang + 1; !fait && j < file.length; j++){
    fait = essai(file[j], true);
    if (fait) [file[rang], file[j]] = [file[j], file[rang]];
  }
  if (!fait) fait = essai(file[rang], false);
  dire = garde;
  if (questionQ && questionQ.ecoute) dire(questionQ.ecoute);
  vus.add(cleQuestion()); derniereSorte = fait;
  window.scrollTo(0, 0); document.body.scrollTop = 0;
}
function fin(){
  $("barre").style.width = "100%"; $("compte").textContent = file.length + " / " + file.length; $("suite").hidden = true;
  $("zone").innerHTML = Fin.bilan(LANGUE, bons, file.length, T("score", {b: bons, n: file.length})) + boutonsBas();
  brancherEncore();
  $("terminer").addEventListener("click", () => parler("fini", {bons, faits: file.length}));
}
function toutRevu(prochaine){
  $("barre").style.width = "100%"; $("compte").textContent = ""; $("suite").hidden = true;
  const quand = Tirage.revu(prochaine, LANGUE);
  $("zone").innerHTML = Fin.revu(tirageTexte("revu"), quand ? tirageTexte("prochaine").replace("{d}", quand) : "") + boutonsBas();
  brancherEncore();
  $("terminer").addEventListener("click", () => parler("fini", {bons: 0, faits: 0}));
}
const boutonEncore = () => SEANCE ? "" : '<button type="button" class="second" id="encore">' + tirageTexte("encore") + '</button>';
const boutonsBas = () => '<div class="bas">' + boutonEncore() + '<button type="button" id="terminer">' + T("terminer") + '</button></div>';
function brancherEncore(){ const b = $("encore"); if (b) b.addEventListener("click", encoreDesQuestions); }
async function encoreDesQuestions(){
  const mots = motsDuTheme();
  file = Tirage.supplement(mots, await Tirage.demander(mots), NB); rang = 0; bons = 0; vus = Tirage.vus(); derniereSorte = null;
  if (!file.length) return toutRevu(null);
  montrer();
}
async function demarrer(){
  const mots = motsDuTheme();
  const plan = Tirage.plan(mots, await Tirage.demander(mots), NB, NEUFS_MAX);
  file = plan.file; rang = 0; bons = 0; vus = Tirage.vus(); derniereSorte = null;
  if (!file.length) return toutRevu(plan.prochaine);
  montrer();
}

// ---------- la decouverte ----------
// Des cartes (D.decouverte) : une image ou une echelle, le mot ou la phrase, sa traduction, la voix au toucher.
function decouvrir(){
  $("compte").textContent = ""; $("barre").style.width = "0%";
  const z = $("zone");
  z.innerHTML = '<p class="consigne">' + isoler(T("intro")) + '</p><div class="fiche" id="fiche"></div><div class="planche" id="planche"></div>'
    + (D.textes.regle ? '<p class="regle">' + isoler(T("regle")) + '</p>' : "");
  const cartes = D.decouverte;
  const montrerCarte = (c, parle) => {
    $("planche").querySelectorAll("button").forEach((b, i) => b.classList.toggle("choisi", cartes[i] === c));
    $("fiche").innerHTML = '<div class="visu">' + visuelHtml(c.visuel) + '</div><div><div class="mot">' + cible(c.texte) + '</div>'
      + traduction(c.trad ? (c.trad[LANGUE] || "") : tradPhrase(c.texte))
      + (c.dit && c.dit !== c.texte ? '<div class="dit">' + cible(c.dit) + '</div>' + traduction(tradPhrase(c.dit)) : "")
      + '<div class="ligne"><button type="button" class="ecoute" id="ecoute" aria-label="' + T("ecouter") + '">' + HP + '</button></div></div>';
    $("ecoute").addEventListener("click", () => dire(c.dit || c.texte));
    if (parle) dire(c.dit || c.texte);
  };
  cartes.forEach(c => {
    const b = document.createElement("button"); b.type = "button"; b.className = "vignette";
    b.innerHTML = '<div class="visu">' + visuelHtml(c.vignette || c.visuel) + '</div><span lang="de" dir="ltr">' + c.court + '</span>';
    b.addEventListener("click", () => montrerCarte(c, true));
    $("planche").appendChild(b);
  });
  montrerCarte(cartes[0], false);
  const s = $("suite"); s.textContent = T("commencer"); s.hidden = false;
  s.onclick = () => { s.onclick = null; Voix.arreter(); demarrer(); };
}

// ---------- le depart ----------
$("suite").addEventListener("click", () => { if (!file.length || repondu === false) return; rang++; if (rang >= file.length) fin(); else montrer(); });
$("retour").addEventListener("click", () => parler("fermer"));
fetch("soins-theme-" + CLE + "/donnees.json?v=" + (typeof VERSION_DONNEES !== "undefined" ? VERSION_DONNEES : 1)).then(r => r.json()).then(d => {
  D = d;
  D.mots.forEach(m => { m.affiche = m.affiche || ((m.genre ? m.genre + " " : "") + m.mot); });
  preparerSortes();
  SORTES = Object.keys(BANQUE);
  $("retour").setAttribute("aria-label", T("retourAria"));
  $("titre").textContent = T("titre");
  document.title = T("titre");
  Zoom.init({direct: "img.photo, .duo img, .fiche img, .citation img", loupe: ".rangee button", langue: LANGUE});
  if (SEANCE && Q.get("decouvrir") !== "1") demarrer(); else decouvrir();
});
// pour les controles (tests/themes_illustres.py, visuel/voix_themes.py) : ce que la page peut dire
function textesAVoix(){ return D ? D.mots.map(m => m.dit || m.affiche).concat(D.decouverte.map(c => c.dit || c.texte)) : []; }
