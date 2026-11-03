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
  function arreter(){
    try{ if (son) son.pause(); }catch(e){}
    try{ if (speechSynthesis.speaking || speechSynthesis.pending) speechSynthesis.cancel(); }catch(e){}
  }
  function dire(texte){
    if (!texte) return;
    arreter();
    const id = sha1(texte);
    if (!connus.has(id)){ telephone(texte); return; }
    son = new Audio(BASE + id + ".mp3" + (R ? "?r=" + R : ""));
    let repli = false;
    const tel = () => { if (!repli){ repli = true; telephone(texte); } };
    son.addEventListener("error", tel, {once: true});
    son.play().catch(tel);
  }
  return {dire, arreter, aUnFichier: texte => connus.has(sha1(texte)), sha1};
})();
