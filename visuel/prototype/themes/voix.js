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
const Voix = (() => {
  const Q = new URLSearchParams(location.search);
  const APP = ["de", "en"].includes(Q.get("apprendre")) ? Q.get("apprendre") : "es";
  const LATAM = APP === "es" && Q.get("variante") === "latam", GB = APP === "en" && Q.get("variante") === "gb";
  const DOSSIER = APP === "de" ? "" : APP === "en" ? (GB ? "en-gb-sans-voix" : "en-us") : LATAM ? "es-419" : "es-es";
  const BASE = "https://deutschai-b6fbb.web.app/" + (DOSSIER ? DOSSIER + "/" : "");
  const R = Q.get("r") || "";
  const TAG = APP === "de" ? "de-DE" : APP === "en" ? (GB ? "en-GB" : "en-US") : LATAM ? "es-MX" : "es-ES";
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
  // la phrase du telephone qui attend la fin du son de reussite : annulee par arreter() (la meteo, a15f561, 5 nov. :
  // « Llueve » entendu sur la photo d'un jour de printemps, la phrase de la question d'avant)
  let attenteTel = null;
  function fondre(s){
    try{
      if (s.paused || s.muted){ s.pause(); return; }
      const v0 = s.volume;
      s.volume = v0 * 0.98;
      if (Math.abs(s.volume - v0) < 1e-6){ s.pause(); return; }     // volume fige (iPhone) : arret net
      const t0 = Date.now();
      const pas = () => {
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
      const b = e.target && e.target.closest ? e.target.closest("button, [role=tab]") : null;
      if (!b || b.closest(".zoom-voile, .zoom-loupe, [data-garde-voix]")) return;
      arreter(true);
    }, true);
  }catch(e){}
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
  function dire(texte){
    if (!texte) return;
    arreter();
    const attente = Math.max(0, finBravo - Date.now());
    const id = sha1(texte), ce = tour;
    if (!connus.has(id)){
      if (!attente){ telephone(texte); return; }
      try{ speechSynthesis.speak(new SpeechSynthesisUtterance("")); }catch(e){}
      attenteTel = setTimeout(() => { attenteTel = null; if (ce === tour) telephone(texte); }, attente);
      return;
    }
    const s = son = new Audio(BASE + id + ".mp3" + (R ? "?r=" + R : ""));
    let repli = false;
    const tel = () => { if (!repli){ repli = true; if (s === son) telephone(texte); } };
    s.addEventListener("error", tel, {once: true});
    if (!attente){ s.play().catch(tel); return; }
    s.muted = true;
    const p = s.play();
    const reprendre = () => { if (s !== son) return; try{ s.pause(); s.currentTime = 0; s.muted = false; s.play().catch(tel); }catch(e){ tel(); } };
    if (p && p.then) p.then(() => setTimeout(reprendre, attente)).catch(() => setTimeout(() => { if (s === son){ s.muted = false; s.play().catch(tel); } }, attente));
    else setTimeout(reprendre, attente);
  }
  return {dire, arreter, bravo, aUnFichier: texte => connus.has(sha1(texte)), sha1};
})();
