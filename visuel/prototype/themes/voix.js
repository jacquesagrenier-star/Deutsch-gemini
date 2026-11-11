// LA VOIX DES THEMES ILLUSTRES -- commune a tous les themes (3 nov. 2026).
//
// Jacques : « il manquait aussi des paroles dites [...] Puis il y a certains endroits où il n'y a pas non plus aucun
// audio » ; « Pour le moment, on va mettre les voix du téléphone. Quand il n'y a pas de voix. » Une seule regle pour
// toutes les pages :
//   1. le FICHIER ENREGISTRE s'il existe (les memes que l'app : sha1 du texte ecrit, seize caracteres ; Aurora pour
//      l'allemand, Lolita en Espagne et Monica en Amerique latine pour l'espagnol) ;
//   2. sinon LA VOIX DU TELEPHONE, choisie comme dans l'app : la meilleure voix locale de la langue apprise et de sa
//      variante, jamais une voix fantaisie (VOIX_A_FUIR d'index.html : Albert, Bubbles, Zarvox...).
// On SAIT a l'avance quels textes ont un fichier (themes/sons.json, fait par visuel/voix_themes.py) : sur iPhone,
// play() et speak() doivent partir dans le geste meme ; attendre qu'un fichier echoue pour se rabattre sur le
// telephone ferait taire la page.
// Parametres de la page : apprendre=es|de|en, variante=latam|es (espagnol) ou gb (anglais), r=<AUDIO_REVISION>.
// L'anglais (themes illustres en anglais, 3 nov. 2026) : Sarah (en-us/) quand sons.json connait le texte, sinon la
// voix du telephone en-US, ou en-GB pour le britannique (jamais Sarah, qui est americaine).
// L'APP ANDROID (8 nov. 2026) : sa vue web n'a pas speechSynthesis ; index.html en pose un, branche sur le module natif
// (installerSyntheseNative), et la page le reprend ici de son cadre. Sans ce module, rien : la voix du telephone se tait.
try{ if (!("speechSynthesis" in window) && window.parent !== window && window.parent.speechSynthesis){ window.speechSynthesis = window.parent.speechSynthesis; window.SpeechSynthesisUtterance = window.parent.SpeechSynthesisUtterance; } }catch(e){}
const Voix = (() => {
  const Q = new URLSearchParams(location.search);
  // le portugais (lot P3, 11 nov. 2026) : aucune voix enregistree, la voix du telephone pt-PT, ou pt-BR (variante=br)
  const APP = ["de", "en", "pt"].includes(Q.get("apprendre")) ? Q.get("apprendre") : "es";
  const LATAM = APP === "es" && Q.get("variante") === "latam", GB = APP === "en" && Q.get("variante") === "gb";
  const BR = APP === "pt" && Q.get("variante") === "br";
  const DOSSIER = APP === "de" ? "" : APP === "en" ? (GB ? "en-gb-sans-voix" : "en-us") : APP === "pt" ? "pt-sans-voix" : LATAM ? "es-419" : "es-es";
  const BASE = "https://deutschai-b6fbb.web.app/" + (DOSSIER ? DOSSIER + "/" : "");
  const R = Q.get("r") || "";
  const TAG = APP === "de" ? "de-DE" : APP === "en" ? (GB ? "en-GB" : "en-US") : APP === "pt" ? (BR ? "pt-BR" : "pt-PT") : LATAM ? "es-MX" : "es-ES";
  // les memes listes qu'index.html (voiceQualityScore, VOIX_A_FUIR) : a garder ensemble
  const BONNES = ["natural", "neural", "enhanced", "premium", "online", "google", "siri", "wavenet"];
  const MAUVAISES = ["compact", "espeak", "kompakt"];
  const A_FUIR = ["albert", "bad news", "bahh", "bells", "boing", "bubbles", "cellos", "good news", "jester", "organ", "pipe organ",
    "superstar", "trinoids", "whisper", "wobble", "zarvox", "deranged", "hysterical", "junior", "ralph", "kathy", "fred", "princess",
    "bruce", "agnes", "vicki", "eddy", "flo", "grandma", "grandpa", "reed", "rocko", "sandy", "shelley"];
  const fuir = v => {
    const nom = ((v && v.name) || "").toLowerCase(), uri = ((v && v.voiceURI) || "").toLowerCase();
    const prenom = nom.replace(/^(microsoft|google|apple)\s+/, "").split(/[\s(]/)[0];
    return uri.indexOf("eloquence") !== -1 || A_FUIR.includes(prenom) || A_FUIR.includes(nom.split(" (")[0]);
  };
  const langue = v => ((v && v.lang) || "").replace("_", "-").toLowerCase();
  const score = v => {
    const nom = ((v && v.name) || "").toLowerCase();
    let s = 0;
    BONNES.forEach(h => { if (nom.indexOf(h) !== -1) s += 10; });
    MAUVAISES.forEach(h => { if (nom.indexOf(h) !== -1) s -= 10; });
    if (v && v.localService === false) s -= 100;        // une voix distante ne passe qu'a defaut (v452)
    if (langue(v) === TAG.toLowerCase()) s += 2;
    if (fuir(v)) s -= 50;
    return s;
  };
  let choisie;
  function voixTelephone(){
    if (choisie !== undefined) return choisie;
    try{
      const toutes = speechSynthesis.getVoices().filter(v => langue(v).startsWith(APP));
      const variante = toutes.filter(v => langue(v) === TAG.toLowerCase());
      choisie = (variante.length ? variante : toutes).sort((a, b) => score(b) - score(a) || a.name.localeCompare(b.name))[0] || null;
      if (!toutes.length) choisie = undefined;            // les voix ne sont pas encore la : on redemandera
    }catch(e){ choisie = null; }
    return choisie || null;
  }
  try{ speechSynthesis.addEventListener("voiceschanged", () => { choisie = undefined; }); }catch(e){}
  // le SHA-1 synchrone d'index.html (sha1Hex) : le nom du fichier se calcule dans le geste
  function sha1(texte){
    const o = new TextEncoder().encode(texte), n = o.length, blocs = ((n + 8) >> 6) + 1, m = new Uint32Array(blocs * 16);
    for (let i = 0; i < n; i++) m[i >> 2] |= o[i] << (24 - (i % 4) * 8);
    m[n >> 2] |= 0x80 << (24 - (n % 4) * 8);
    m[blocs * 16 - 1] = n * 8;
    let h0 = 0x67452301, h1 = 0xEFCDAB89, h2 = 0x98BADCFE, h3 = 0x10325476, h4 = 0xC3D2E1F0;
    const w = new Uint32Array(80);
    for (let j = 0; j < blocs * 16; j += 16){
      for (let i = 0; i < 16; i++) w[i] = m[j + i];
      for (let i = 16; i < 80; i++){ const v = w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]; w[i] = (v << 1) | (v >>> 31); }
      let a = h0, b = h1, c = h2, d = h3, e = h4;
      for (let i = 0; i < 80; i++){
        let f, k;
        if (i < 20){ f = (b & c) | (~b & d); k = 0x5A827999; }
        else if (i < 40){ f = b ^ c ^ d; k = 0x6ED9EBA1; }
        else if (i < 60){ f = (b & c) | (b & d) | (c & d); k = 0x8F1BBCDC; }
        else { f = b ^ c ^ d; k = 0xCA62C1D6; }
        const t = (((a << 5) | (a >>> 27)) + f + e + k + w[i]) >>> 0;
        e = d; d = c; c = ((b << 30) | (b >>> 2)) >>> 0; b = a; a = t;
      }
      h0 = (h0 + a) >>> 0; h1 = (h1 + b) >>> 0; h2 = (h2 + c) >>> 0; h3 = (h3 + d) >>> 0; h4 = (h4 + e) >>> 0;
    }
    return [h0, h1, h2, h3, h4].map(x => x.toString(16).padStart(8, "0")).join("").slice(0, 16);
  }
  // les textes qui ont un fichier, par dossier (themes/sons.json)
  let connus = new Set();
  fetch("themes/sons.json?r=" + encodeURIComponent(R)).then(r => r.json()).then(d => { connus = new Set(d[DOSSIER || "de"] || []); }).catch(() => {});
  let son = null;
  function telephone(texte){
    try{
      if (!("speechSynthesis" in window)) return;
      // cancel() seulement s'il y a quelque chose a couper : sur un moteur au repos il rend muet l'enonce suivant (v449)
      if (speechSynthesis.speaking || speechSynthesis.pending) speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(texte);
      u.lang = TAG; const v = voixTelephone(); if (v) u.voice = v; u.rate = 0.9;
      speechSynthesis.speak(u);
    }catch(e){}
  }
  // COUPER EN FONDU (5 nov. 2026, Jacques : on passe a l'image ou a la question suivante pendant qu'une phrase est
  // dite, et la voix continuait dessus ; « elegamment »). arreter(true) baisse le fichier enregistre en ~120 ms puis
  // le met en pause ; la voix du telephone, elle, se coupe par cancel(). Sur iPhone, le volume d'un <audio> est en
  // lecture seule : le fondu y devient un arret net. `tour` annule aussi une phrase en attente derriere le son de
  // reussite (dire() juste apres bravo()) : on avance quand on veut, sans attendre la fin de rien.
  const FONDU = 120;
  let tour = 0;
  // LE LECTEUR BENI (8 nov. 2026). La phrase de l'enonce est dite des l'entree dans la carte, donc souvent HORS DU
  // GESTE : la premiere carte d'une partie vient apres le « await Tirage.demander() » de demarrer(), et iOS refuse alors
  // un play() sur un <audio> neuf. Une fois qu'un element a joue dans un toucher, iOS le laisse rejouer, meme avec une
  // autre source : au premier toucher dans la page, on lui fait jouer 50 ms de silence, et un enonce vide debloque la
  // voix du telephone. Sans aucun toucher dans la page, l'enonce se tait et le haut-parleur reste la.
  const SILENCE = "data:audio/wav;base64,UklGRrQBAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YZABAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA";
  let beni = null;
  function benir(){
    if (beni) return;
    try{ const a = new Audio(SILENCE); const p = a.play(); if (p && p.catch) p.catch(() => {}); beni = a; }catch(e){}
    try{ if (!speechSynthesis.speaking && !speechSynthesis.pending) speechSynthesis.speak(new SpeechSynthesisUtterance("")); }catch(e){}
  }
  // la phrase du telephone qui attend la fin du son de reussite : annulee par arreter() (la meteo, a15f561, 5 nov. :
  // « Llueve » entendu sur la photo d'un jour de printemps, la phrase de la question d'avant)
  let attenteTel = null;
  function fondre(s){
    try{
      if (s.paused || s.muted){ s.pause(); return; }
      const v0 = s.volume, reprise = s.vReprise = (s.vReprise || 0) + 1;     // le lecteur beni repart : ce fondu-la s'arrete
      s.volume = v0 * 0.98;
      if (Math.abs(s.volume - v0) < 1e-6){ s.pause(); return; }     // volume fige (iPhone) : arret net
      const t0 = Date.now();
      const pas = () => {
        if (s.vReprise !== reprise) return;
        const k = (Date.now() - t0) / FONDU;
        if (k >= 1 || s.paused){ try{ s.pause(); }catch(e){} return; }
        s.volume = v0 * (1 - k);
        setTimeout(pas, 16);                                         // pas requestAnimationFrame : il dort en arriere-plan
      };
      pas();
    }catch(e){ try{ s.pause(); }catch(_){} }
  }
  function arreter(fondu){
    tour++;
    if (attenteTel){ clearTimeout(attenteTel); attenteTel = null; }
    const s = son; son = null;
    if (s){ if (fondu === true) fondre(s); else try{ s.pause(); }catch(e){} }
    try{ if (speechSynthesis.speaking || speechSynthesis.pending) speechSynthesis.cancel(); }catch(e){}
  }
  // UN SEUL BRANCHEMENT POUR LES DIX-SEPT PAGES : tout bouton touche (Continuer, Commencer, un onglet, une reponse,
  // le retour, Terminer, Encore) coupe la phrase en cours, en phase de capture, donc AVANT le geste de la page. Un
  // bouton qui parle (reecouter, une reponse juste) relance ensuite sa propre phrase par dire(), comme avant. Le son
  // de reussite ne passe pas par `son` : il n'est jamais coupe. La loupe et son voile (zoom.js) ne coupent rien.
  try{
    document.addEventListener("click", e => {
      benir();
      const b = e.target && e.target.closest ? e.target.closest("button, [role=tab]") : null;
      if (!b || b.closest(".zoom-voile, .zoom-loupe, [data-garde-voix]")) return;
      arreter(true);
    }, true);
  }catch(e){}
  // REECOUTER (6 nov. 2026, Jacques : « lorsqu'on est dans les themes, qu'on a une image, d'etre capable de reecouter
  // la phrase »). A chaque question neuve (une .consigne posee dans #zone) qui n'a pas deja son haut-parleur, un rond
  // haut-parleur s'ajoute au bout de la consigne -- en haut, loin du rond « → » et des reponses. Il redit la derniere
  // phrase dite dans cette question (apres la reponse : la phrase juste) ; avant, la phrase de l'enonce quand elle est
  // entiere (pas de trou a remplir) ; sans l'une ni l'autre, il reste cache. Il passe par dire() : le fondu et la
  // phrase en attente derriere le son de reussite s'appliquent comme partout.
  // A COTE DE LA PHRASE, ET DITE DES L'ENTREE (8 nov. 2026, Jacques, theme ecole : le haut-parleur etait au bout de la
  // consigne francaise alors qu'il dit « ¿Qué necesita Ben? »). Quand l'enonce se dit (entier, dans la langue apprise),
  // le rond se pose dans l'enonce et la phrase part a l'entree de la carte, sans toucher. Sinon (enonce vide, phrase a
  // trou, ecoute qui parle deja) : rien ne part, et le rond reste au bout de la consigne. La place se decide a l'entree
  // de la carte et ne change plus : une phrase a trou completee apres la reponse ne fait pas sauter le bouton.
  // la phrase dite, et la consigne de la question ou elle l'a ete (une question neuve = une consigne neuve ; pas de
  // remise a zero dans l'observateur, qui passe APRES le code de la page et effacerait une phrase dite au rendu)
  let ditQuestion = "", ditConsigne = null;
  const dejaDit = z => { const c = z && z.querySelector(".consigne"); return c && c === ditConsigne ? ditQuestion : ""; };
  const HP = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 0 0 1.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06ZM18.584 5.106a.75.75 0 0 1 1.06 0c3.808 3.807 3.808 9.98 0 13.788a.75.75 0 0 1-1.06-1.06 8.25 8.25 0 0 0 0-11.668.75.75 0 0 1 0-1.06Z"/><path d="M15.932 7.757a.75.75 0 0 1 1.061 0 6 6 0 0 1 0 8.486.75.75 0 0 1-1.06-1.061 4.5 4.5 0 0 0 0-6.364.75.75 0 0 1 0-1.06Z"/></svg>';
  function phraseEnonce(z){
    const e = z && z.querySelector(".enonce");
    if (!e || e.querySelector("#trou, .trou")) return "";
    const ls = e.querySelectorAll("[lang]");
    const t = (ls.length ? Array.from(ls).map(x => x.textContent).join(" ") : "").replace(/\s+/g, " ").trim();
    return /_{2,}/.test(t) ? "" : t;
  }
  function majReecoute(){
    const z = document.getElementById("zone"), b = z && z.querySelector(".v-redire");
    if (b) b.hidden = !(dejaDit(z) || phraseEnonce(z));
  }
  let cartePosee = null, dansEnonce = false;
  function poserReecoute(){
    const z = document.getElementById("zone"); if (!z) return;
    const c = z.querySelector(".consigne");
    if (!c || z.querySelector(".ecoute:not(.v-redire), #ecoute")) return;
    const neuve = c !== cartePosee;
    if (neuve){ cartePosee = c; dansEnonce = !!phraseEnonce(z); }
    if (!z.querySelector(".v-redire")){              // a poser, ou a remettre : la page a pu recrire l'enonce
      const b = document.createElement("button");
      b.type = "button"; b.className = "ecoute v-redire"; b.innerHTML = HP;
      let nom = "";
      try{ if (typeof T === "function") nom = T("ecouter"); }catch(e){}
      b.setAttribute("aria-label", nom && nom !== "ecouter" ? nom : "Réécouter");
      b.addEventListener("click", () => { const t = dejaDit(z) || phraseEnonce(z); if (t) dire(t); });
      const e = dansEnonce && z.querySelector(".enonce");
      if (e){ e.classList.add("v-hp"); e.appendChild(b); } else c.appendChild(b);
    }
    majReecoute();
    if (neuve) direEntree(z);
  }
  // la phrase de l'enonce, une fois par carte : jamais apres la reponse (une page qui redessine sa carte), jamais par-
  // dessus ce que la page vient de dire
  function direEntree(z){
    try{ if (typeof repondu !== "undefined" && repondu) return; }catch(e){}
    if (dejaDit(z)) return;
    const t = phraseEnonce(z);
    if (t) dire(t, true);
  }
  function brancherReecoute(){
    const z = document.getElementById("zone"); if (!z) return;
    const st = document.createElement("style");
    st.textContent = ".consigne .v-redire{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;"
      + "min-width:34px;vertical-align:middle;margin:-4px 0 0;margin-inline-start:8px;padding:0}"
      + ".consigne .v-redire svg{width:18px;height:18px}.consigne .v-redire[hidden]{display:none}"
      // dans l'enonce : hors du flux, et une marge reservee des deux cotes quand le texte est centre -- il ne bouge pas
      + ".enonce.v-hp{position:relative;padding-right:50px}.enonce.centre.v-hp{padding-left:50px}"
      + ".enonce .v-redire{position:absolute;right:8px;top:50%;transform:translateY(-50%);display:inline-flex;align-items:center;"
      + "justify-content:center;width:34px;height:34px;min-width:34px;margin:0;padding:0}"
      + ".enonce .v-redire svg{width:18px;height:18px}.enonce .v-redire[hidden]{display:none}";
    (document.head || document.documentElement).appendChild(st);
    new MutationObserver(() => {
      poserReecoute();
    }).observe(z, {childList: true, subtree: true});
    poserReecoute();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", brancherReecoute); else brancherReecoute();
  // LE SON DE REUSSITE (3 nov. 2026, Jacques sur iPhone : le « +1 » sans le son des cartes et des scenes). Comme les
  // scenes (sonBravo de visuel/prototype/index.html) : le son de l'APP quand la page est dans son cadre (meme
  // origine : la kalimba des cartes, quel qu'il soit), sinon une copie des trois notes en WAV joue par un <audio>
  // (iOS le joue meme en silencieux), sinon des oscillateurs. A appeler DANS le toucher de la reponse.
  const NOTES = [1046.5, 1318.51, 1567.98];
  let wav = null, ctxSecours = null, finBravo = 0;
  try{
    const H = window.OfflineAudioContext || window.webkitOfflineAudioContext;
    if (H){
      const ecart = 0.11, duree = 0.35, taux = 44100;
      const ctx = new H(1, Math.ceil(taux * ((NOTES.length - 1) * ecart + duree + 0.05)), taux);
      NOTES.forEach((f, k) => {
        const o = ctx.createOscillator(), g = ctx.createGain(), t = k * ecart;
        o.type = "triangle"; o.frequency.value = f;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.55, t + 0.008); g.gain.exponentialRampToValueAtTime(0.001, t + duree);
        o.connect(g); g.connect(ctx.destination); o.start(t); o.stop(t + duree + 0.02);
      });
      const fini = buf => {
        const n = buf.length, v = new DataView(new ArrayBuffer(44 + n * 2));
        const ec = (p, s) => { for (let i = 0; i < s.length; i++) v.setUint8(p + i, s.charCodeAt(i)); };
        ec(0, "RIFF"); v.setUint32(4, 36 + n * 2, true); ec(8, "WAVE"); ec(12, "fmt "); v.setUint32(16, 16, true); v.setUint16(20, 1, true);
        v.setUint16(22, 1, true); v.setUint32(24, taux, true); v.setUint32(28, taux * 2, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true);
        ec(36, "data"); v.setUint32(40, n * 2, true);
        const d = buf.getChannelData(0);
        for (let i = 0; i < n; i++){ const s = Math.max(-1, Math.min(1, d[i])); v.setInt16(44 + i * 2, s < 0 ? s * 0x8000 : s * 0x7FFF, true); }
        wav = new Audio(URL.createObjectURL(new Blob([v.buffer], {type: "audio/wav"}))); wav.preload = "auto";
      };
      const r = ctx.startRendering();
      if (r && r.then) r.then(fini).catch(() => {}); else ctx.oncomplete = e => fini(e.renderedBuffer);
    }
  }catch(e){}
  function secours(){
    try{
      const C = window.AudioContext || window.webkitAudioContext; if (!C) return;
      ctxSecours = ctxSecours || new C(); if (ctxSecours.resume) ctxSecours.resume().catch(() => {});
      const t0 = ctxSecours.currentTime;
      NOTES.forEach((f, k) => {
        const o = ctxSecours.createOscillator(), g = ctxSecours.createGain(), t = t0 + k * 0.11;
        o.type = "triangle"; o.frequency.value = f;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.32, t + 0.008); g.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
        o.connect(g); g.connect(ctxSecours.destination); o.start(t); o.stop(t + 0.4);
      });
    }catch(e){}
  }
  function bravo(){
    finBravo = Date.now() + APRES_BRAVO;
    try{ const app = window.parent; if (app && app !== window && typeof app.playMasteredSound === "function"){ app.playMasteredSound(); return; } }catch(e){}
    try{ if (wav){ wav.currentTime = 0; const p = wav.play(); if (p && p.catch) p.catch(secours); return; } }catch(e){}
    secours();
  }
  // LA PHRASE APRES LE SON : une phrase demandee juste apres bravo() attend la fin des trois notes. Sur iPhone, un
  // son ne peut partir que DANS le toucher : on le lance donc tout de suite, muet, puis on le reprend du debut, le
  // son coupe retire, une fois le bravo fini (l'element a ete lance par le geste, iOS le laisse rejouer) ; la voix du
  // telephone est debloquee de meme par un enonce vide.
  const APRES_BRAVO = 650;
  function dire(texte, entree){
    if (!texte) return;
    arreter();
    try{ ditQuestion = texte; ditConsigne = document.querySelector("#zone .consigne"); majReecoute(); }catch(e){}
    const attente = Math.max(0, finBravo - Date.now());
    const id = sha1(texte), ce = tour;
    if (!connus.has(id)){
      if (!attente){ telephone(texte); return; }
      try{ speechSynthesis.speak(new SpeechSynthesisUtterance("")); }catch(e){}
      attenteTel = setTimeout(() => { attenteTel = null; if (ce === tour) telephone(texte); }, attente);
      return;
    }
    const url = BASE + id + ".mp3" + (R ? "?r=" + R : "");
    let s;
    if (entree && beni){                             // hors du geste : l'element que le premier toucher a debloque
      s = beni; s.vReprise = (s.vReprise || 0) + 1;
      try{ s.pause(); s.loop = false; s.muted = false; s.volume = 1; s.src = url; }catch(e){}
    } else s = new Audio(url);
    son = s;
    let repli = false;
    const tel = () => { if (!repli && ce === tour){ repli = true; if (s === son) telephone(texte); } };
    s.addEventListener("error", tel, {once: true});
    if (!attente){ s.play().catch(tel); return; }
    // 7 nov. 2026 : PLUS DE SECOND play() HORS DU GESTE. Le fichier part muet ET EN BOUCLE dans le toucher ; a la fin
    // du son de reussite, on le ramene au debut et on lui rend le son, sans le mettre en pause ni le relancer. Avant,
    // pause() puis play() dans un setTimeout : si iOS refusait ce second play(), .catch(tel) passait au telephone alors
    // que le fichier existait (hypothese de la session des emotions, invisible dans Chromium). La boucle empeche un
    // fichier plus court que le son de reussite (« Si. ») de s'arreter avant d'etre entendu.
    s.muted = true; s.loop = true;
    const p = s.play();
    const reprendre = () => {
      if (s !== son) return;
      try{ s.loop = false; s.currentTime = 0; s.muted = false; if (s.paused) s.play().catch(tel); }catch(e){ tel(); }
    };
    if (p && p.then) p.then(() => setTimeout(reprendre, attente)).catch(() => setTimeout(() => { if (s === son){ s.loop = false; s.muted = false; s.play().catch(tel); } }, attente));
    else setTimeout(reprendre, attente);
  }
  return {dire, arreter, bravo, aUnFichier: texte => connus.has(sha1(texte)), sha1};
})();
