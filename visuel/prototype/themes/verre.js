/* LE VERRE DES BOUTONS POSES SUR LES IMAGES (v1107, Jacques, 4 nov. 2026)
   Maquette : .claude/maquette-verre-boutons.html (https://claude.ai/artifact/2XAbaphjgyVa79msFg4st7).
   Jacques : « les boutons, ça ne prenne pas de place le moins possible » ; « le vert pour continuer. Lui pourrait
   être un transparent vert » ; « un vert presque transparent. On voit que c'est vert, mais puis adaptif ».

   Une balise par page (scènes, thèmes illustrés, DTZ oral), rien d'autre : ce fichier pose sa feuille de style et
   s'occupe de tout.
   - « Continuer » et les boutons du bas (.suite, .bas button) : un VERT TRÈS DOUX, presque transparent.
   - Le rond « ‹ » (#retourChoix des scènes, .retour des thèmes) : un VERRE CLAIR.
   Le même liseré de lumière, le même reflet en haut et les mêmes rayons partout ; seule la densité change.

   ADAPTATIF : le bouton regarde ce qui passe dessous. Le texte passe au foncé sur du clair et au blanc sur du sombre,
   et le voile ne s'épaissit que si le texte ne se lirait plus (4,5 : 1 pour un bouton, 3 : 1 pour un rond, seuils
   de tests/audit-contraste.js). Il garde sa couleur tant que l'autre ne demande pas nettement moins de voile
   (10 points), pour ne pas clignoter quand une limite de l'image passe sous le bouton.
   ⚠️ LE COÛT SUR L'IPHONE (consigne du chef) : chaque image n'est lue qu'UNE fois, réduite à 32 px de large, et ce sont
   ces pixels qu'on garde (pas le canevas : iOS vide les canevas en arrière-plan). Les recalculs sont regroupés
   (au plus un toutes les 120 ms) et attendent la fin d'une animation. Une image d'une autre adresse (canevas
   « sali ») est traitée comme un fond uni. */
(function(){
  "use strict";
  if (window.__verreBoutons) return; window.__verreBoutons = true;

  const BLANC = [255,255,255], FONCE = [28,36,48];
  const PAL = {
    vert:   {f:{tc:[70,180,120], ink:[20,83,47]}, w:{tc:[24,100,62], ink:BLANC}, min:.18, max:.85, seuil:4.5},
    neutre: {f:{tc:BLANC, ink:FONCE},            w:{tc:[18,26,36], ink:BLANC},  min:.09, max:.60, seuil:3}
  };
  const SELECTEURS = [[".suite, .bas button", "vert"], ["#retourChoix, button.retour#retour", "neutre"]];
  const PAS = .03, LARGEUR_LUE = 32;

  /* ---------- la feuille ---------- */
  const css = `
@property --v-haut{syntax:"<color>"; inherits:false; initial-value:transparent}
@property --v-bas{syntax:"<color>"; inherits:false; initial-value:transparent}
.verre-v{background:linear-gradient(180deg, var(--v-haut), var(--v-bas)) !important; color:var(--v-encre) !important;
  border-color:transparent !important; overflow:hidden !important; isolation:isolate;
  -webkit-backdrop-filter:blur(var(--v-flou)) saturate(1.5) !important; backdrop-filter:blur(var(--v-flou)) saturate(1.5) !important;
  box-shadow:inset 0 -8px 14px -10px rgba(0,0,0,.22), 0 8px 22px rgba(0,0,0,.18), 0 1px 3px rgba(0,0,0,.10) !important;
  transition:color .35s ease, text-shadow .35s ease, --v-haut .35s ease, --v-bas .35s ease !important}
.verre-v.v-pose{position:relative}
.verre-v::before{content:"" !important; position:absolute !important; inset:2px !important; border-radius:inherit; z-index:-1; pointer-events:none;
  background:linear-gradient(180deg, rgba(255,255,255,.42) 0%, rgba(255,255,255,.14) 36%, rgba(255,255,255,0) 52%) !important}
.verre-v::after{content:"" !important; position:absolute !important; inset:0 !important; border-radius:inherit; pointer-events:none; padding:1.5px;
  background:linear-gradient(140deg, #fff 0%, rgba(255,255,255,.55) 22%, rgba(255,255,255,.06) 48%, rgba(255,255,255,.25) 74%, rgba(255,255,255,.95) 100%) !important;
  -webkit-mask:linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite:xor; mask-composite:exclude}
.verre-v.v-blanc{text-shadow:0 1px 2px rgba(0,0,0,.45) !important}
.verre-v.v-fonce{text-shadow:0 0 3px rgba(255,255,255,.55) !important}
.verre-v svg{fill:currentColor}
@media (prefers-reduced-motion: reduce){ .verre-v{transition:none !important} }`;
  const st = document.createElement("style"); st.id = "verreBoutonsCss"; st.textContent = css;
  (document.head || document.documentElement).appendChild(st);

  /* ---------- la lecture ---------- */
  const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const lum = c => 0.2126*lin(c[0]) + 0.7152*lin(c[1]) + 0.0722*lin(c[2]);
  const ratio = (a, b) => { const x = Math.max(a, b), y = Math.min(a, b); return (x + .05) / (y + .05); };
  const PIXELS = new Map();   // src -> {w, h, px} ou null (image illisible)
  function pixels(img){
    const cle = img.currentSrc || img.src;
    if (PIXELS.has(cle)) return PIXELS.get(cle);
    if (!img.complete || !img.naturalWidth) return null;
    let r = null;
    try{
      const w = LARGEUR_LUE, h = Math.max(1, Math.round(w * img.naturalHeight / img.naturalWidth));
      const c = document.createElement("canvas"); c.width = w; c.height = h;
      const x = c.getContext("2d", {willReadFrequently:true}); x.drawImage(img, 0, 0, w, h);
      r = {w, h, px: x.getImageData(0, 0, w, h).data};
      c.width = c.height = 0;
    }catch(e){ r = null; }
    PIXELS.set(cle, r); return r;
  }
  function couleurFond(el){
    for (let n = el; n && n.nodeType === 1; n = n.parentElement){
      const m = getComputedStyle(n).backgroundColor.match(/rgba?\(([^)]+)\)/);
      if (m){ const p = m[1].split(",").map(parseFloat); if ((p.length < 4 || p[3] > .5)) return p.slice(0, 3); }
    }
    return document.documentElement.classList.contains("nuit") ? [18,30,42] : [220,230,236];
  }
  /* Ce qu'il y a sous le bouton : les pixels de l'image (s'il y en a une), sinon la couleur du fond. */
  function dessous(b){
    const r = b.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return null;
    const ancien = b.style.pointerEvents; b.style.pointerEvents = "none";
    const echantillon = [];
    let fond = null;
    // La ligne du texte seulement (le milieu du bouton), comme dans la maquette : ce que le texte doit vaincre.
    const fxs = r.width > 80 ? [.34, .42, .5, .58, .66] : [.4, .5, .6];
    for (const fx of fxs) for (const fy of [.42, .58]){
      const x = r.left + r.width * fx, y = r.top + r.height * fy;
      const pile = document.elementsFromPoint ? document.elementsFromPoint(x, y) : [];
      const img = pile.find(e => e.tagName === "IMG" && !b.contains(e));
      const P = img ? pixels(img) : null;
      if (P){
        const ri = img.getBoundingClientRect();
        const ix = Math.floor((x - ri.left) / ri.width * P.w), iy = Math.floor((y - ri.top) / ri.height * P.h);
        if (ix >= 0 && iy >= 0 && ix < P.w && iy < P.h){
          // un petit voisinage : l'image réduite fait déjà le flou
          for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++){
            const xx = Math.min(P.w - 1, Math.max(0, ix + dx)), yy = Math.min(P.h - 1, Math.max(0, iy + dy)), i = (yy * P.w + xx) * 4;
            echantillon.push([P.px[i], P.px[i+1], P.px[i+2]]);
          }
          continue;
        }
      }
      if (!fond) fond = couleurFond(pile.find(e => !b.contains(e) && e !== b) || document.body);
      echantillon.push(fond);
    }
    b.style.pointerEvents = ancien;
    return echantillon;
  }
  function besoin(ech, tenue, P){
    const li = lum(tenue.ink), tc = tenue.tc;
    let dernier = null;
    for (let a = P.min; a <= P.max + 1e-6; a += PAS){
      const vals = ech.map(c => ratio(li, lum([a*tc[0] + (1-a)*c[0], a*tc[1] + (1-a)*c[1], a*tc[2] + (1-a)*c[2]]))).sort((p, q) => p - q);
      const c = vals[Math.floor(vals.length * .05)];
      if (c >= P.seuil) return {a, ok:true};
      dernier = {a, c, ok:false};
    }
    return dernier;
  }
  function choisir(b, P){
    const ech = dessous(b); if (!ech) return;
    const x = {f: besoin(ech, P.f, P), w: besoin(ech, P.w, P)};
    const note = r => r.ok ? r.a : 1 + (P.seuil - r.c);
    let k = note(x.f) <= note(x.w) ? "f" : "w";
    const avant = b.dataset.verreTenue;
    if (avant && avant !== k && note(x[avant]) - note(x[k]) < .10) k = avant;
    const t = P[k], a = x[k].a, rgba = (c, al) => "rgba(" + c[0] + "," + c[1] + "," + c[2] + "," + al.toFixed(2) + ")";
    b.dataset.verreTenue = k;
    b.style.setProperty("--v-haut", rgba(t.tc, Math.min(1, a + .03)));
    b.style.setProperty("--v-bas", rgba(t.tc, a));
    b.style.setProperty("--v-encre", rgba(t.ink, 1));
    b.classList.toggle("v-blanc", k === "w"); b.classList.toggle("v-fonce", k === "f");
  }

  /* ---------- les boutons et le rythme ---------- */
  function boutons(){
    const l = [];
    SELECTEURS.forEach(([sel, nom]) => document.querySelectorAll(sel).forEach(b => {
      if (!b.classList.contains("verre-v")){
        b.classList.add("verre-v");
        b.style.setProperty("--v-flou", nom === "vert" ? "8px" : "6px");
        if (getComputedStyle(b).position === "static") b.classList.add("v-pose");
      }
      if (b.offsetParent !== null || getComputedStyle(b).position === "fixed") l.push([b, PAL[nom]]);
    }));
    return l;
  }
  let prevu = 0, dernier = 0, reports = 0;
  function animationEnCours(){
    if (!document.getAnimations) return false;
    return document.getAnimations().some(a => a.playState === "running" && a.effect && a.effect.getTiming && isFinite(a.effect.getTiming().iterations)
      && !(a.effect.target && a.effect.target.classList && a.effect.target.classList.contains("verre-v")));
  }
  function maj(){
    prevu = 0;
    if (document.hidden) return;
    if (animationEnCours() && reports < 8){ reports++; plus_tard(150); return; }
    reports = 0; dernier = performance.now();
    boutons().forEach(([b, P]) => { try{ choisir(b, P); }catch(e){} });
  }
  function plus_tard(ms){ if (!prevu) prevu = setTimeout(() => requestAnimationFrame(maj), ms); }
  function demander(){ plus_tard(Math.max(0, 120 - (performance.now() - dernier))); }

  addEventListener("scroll", demander, {passive:true, capture:true});
  addEventListener("resize", demander, {passive:true});
  addEventListener("touchmove", demander, {passive:true});
  addEventListener("touchend", demander, {passive:true});
  addEventListener("wheel", demander, {passive:true});
  addEventListener("transitionend", demander, true);
  addEventListener("animationend", demander, true);
  addEventListener("load", demander, true);   // une image qui arrive
  document.addEventListener("visibilitychange", () => { if (!document.hidden) demander(); });
  function observer(){
    // ⚠️ Nos propres retouches (le style et la classe des boutons) ne relancent pas le calcul : sinon il tournerait sans fin.
    new MutationObserver(recs => { if (recs.some(r => !(r.target.classList && r.target.classList.contains("verre-v")))) demander(); })
      .observe(document.body, {childList:true, subtree:true, attributes:true, attributeFilter:["hidden", "class", "style", "src"]});
    demander();
  }
  if (document.body) observer(); else document.addEventListener("DOMContentLoaded", observer);
})();
