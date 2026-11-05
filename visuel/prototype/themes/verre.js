/* LE VERRE DES BOUTONS POSES SUR LES IMAGES (v1107 ; v1110 : le verre d'Apple et le rond qui avance)
   Jacques, 4 nov. 2026 : « le meme verre, mais V-E-R-R-E. Donc, transparent, la meme chose qu'Apple » ; pour
   Continuer, un rond centre en bas avec une fleche (« Une fleche plutot » ; « on va le placer au centre »).
   Maquette : .claude/maquette-choix-verre.html.

   Une balise par page (scenes, themes illustres, DTZ oral), rien d'autre : ce fichier pose sa feuille de style et
   s'occupe de tout.
   - « Continuer » / « Commencer » (.suite, quand son libelle est court et sans fleche) : un ROND de 56 px centre en
     bas, zone de toucher 64 px, une fleche ; le mot reste dans le bouton pour les lecteurs d'ecran.
   - Les autres boutons du bas (.suite a long libelle, .bas button) : le meme verre, avec leur texte.
   - Le rond « ‹ » (#retourChoix des scenes, .retour des themes) : le meme verre.
   ADAPTATIF : le bouton regarde ce qui passe dessous. L'encre (texte ou fleche) passe au petrole fonce sur du clair
   et au clair sur du sombre ; le voile, presque nul (5 %), ne s'epaissit que si l'encre ne se lirait plus (4,5 : 1
   pour un texte, 3 : 1 pour une fleche ou un chevron, seuils de tests/audit-contraste.js). Il garde son encre tant
   que l'autre ne demande pas nettement moins de voile (10 points), pour ne pas clignoter.
   ⚠️ LE COUT SUR L'IPHONE : chaque image n'est lue qu'UNE fois, reduite a 32 px de large, et ce sont ces pixels
   qu'on garde (pas le canevas : iOS vide les canevas en arriere-plan). Les recalculs sont regroupes (au plus un
   toutes les 120 ms) et attendent la fin d'une animation. Une image d'une autre adresse (canevas « sali ») est
   traitee comme un fond uni. */
(function(){
  "use strict";
  if (window.__verreBoutons) return; window.__verreBoutons = true;

  const BLANC = [255,255,255], PETROLE = [23,58,78], CLAIR = [243,245,248], NUIT = [18,26,36];
  const APPLE = {f:{tc:BLANC, ink:PETROLE}, w:{tc:NUIT, ink:CLAIR}, min:.05, max:.60};
  const SEUIL_TEXTE = 4.5, SEUIL_ICONE = 3;
  const PAS = .03, LARGEUR_LUE = 32;
  const fleche = (c, gauche) => 'url("data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="'
      + (gauche ? "M25 16H8M14 9.5L7.5 16l6.5 6.5" : "M7 16h17M18 9.5l6.5 6.5-6.5 6.5")
      + '" fill="none" stroke="rgb(' + c.join(",") + ')" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>') + '")';

  /* ---------- la feuille ---------- */
  const css = `
@property --v-haut{syntax:"<color>"; inherits:false; initial-value:transparent}
@property --v-bas{syntax:"<color>"; inherits:false; initial-value:transparent}
.verre-v{--v-haut:rgba(255,255,255,.08); --v-bas:rgba(255,255,255,.05); --v-encre:rgb(23,58,78); --v-fleche:${fleche(PETROLE, false)}}
html.nuit .verre-v{--v-haut:rgba(18,26,36,.08); --v-bas:rgba(18,26,36,.05); --v-encre:rgb(243,245,248); --v-fleche:${fleche(CLAIR, false)}}
html[dir="rtl"] .verre-v{--v-fleche:${fleche(PETROLE, true)}}
html.nuit[dir="rtl"] .verre-v{--v-fleche:${fleche(CLAIR, true)}}
.verre-v{--v-reflet:linear-gradient(180deg, rgba(255,255,255,.30) 0%, rgba(255,255,255,.05) 30%, rgba(255,255,255,0) 48%), radial-gradient(60% 40% at 50% 110%, rgba(255,255,255,.22), rgba(255,255,255,0) 70%);
  background:var(--v-reflet), linear-gradient(180deg, var(--v-haut), var(--v-bas)) !important; color:var(--v-encre) !important;
  border-color:transparent !important; overflow:hidden !important; isolation:isolate;
  -webkit-backdrop-filter:blur(12px) saturate(1.15) brightness(1.04) !important; backdrop-filter:blur(12px) saturate(1.15) brightness(1.04) !important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.55), inset 0 -1px 0 rgba(255,255,255,.18), 0 8px 22px rgba(20,30,40,.14) !important;
  transition:color .35s ease, text-shadow .35s ease, --v-haut .35s ease, --v-bas .35s ease !important}
html.nuit .verre-v{--v-reflet:linear-gradient(180deg, rgba(255,255,255,.12) 0%, rgba(255,255,255,.02) 30%, rgba(255,255,255,0) 48%);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(255,255,255,.06), 0 8px 22px rgba(0,0,0,.3) !important}
.verre-v.v-pose{position:relative}
.verre-v::before{content:none !important}
.verre-v::after{content:"" !important; position:absolute !important; inset:0 !important; border-radius:inherit; pointer-events:none; padding:1.5px;
  background:linear-gradient(140deg, #fff 0%, rgba(255,255,255,.55) 22%, rgba(255,255,255,.06) 48%, rgba(255,255,255,.25) 74%, rgba(255,255,255,.95) 100%) !important;
  -webkit-mask:linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite:xor; mask-composite:exclude; opacity:.8}
.verre-v.v-blanc{text-shadow:0 1px 3px rgba(0,0,0,.6) !important}
.verre-v.v-fonce{text-shadow:0 0 4px rgba(255,255,255,.75), 0 0 1px rgba(255,255,255,.6) !important}
.verre-v svg{fill:currentColor}
/* le rond qui avance : 64 px de zone de toucher, le verre (56 px) dessine dans le ::before */
.verre-v.v-rond{left:calc(50% - 32px) !important; right:auto !important; width:64px !important; height:64px !important; min-height:64px !important;
  padding:0 !important; border-radius:50% !important; font-size:0 !important; color:transparent !important; text-shadow:none !important;
  background:none !important; box-shadow:none !important; -webkit-backdrop-filter:none !important; backdrop-filter:none !important}
.verre-v.v-rond::before{content:"" !important; position:absolute; inset:4px; border-radius:50%; z-index:-1; pointer-events:none;
  background:var(--v-fleche) center / 26px 26px no-repeat, var(--v-reflet), linear-gradient(180deg, var(--v-haut), var(--v-bas));
  -webkit-backdrop-filter:blur(12px) saturate(1.15) brightness(1.04); backdrop-filter:blur(12px) saturate(1.15) brightness(1.04);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.55), inset 0 -1px 0 rgba(255,255,255,.18), 0 8px 22px rgba(20,30,40,.14);
  transition:--v-haut .35s ease, --v-bas .35s ease}
.verre-v.v-rond::after{inset:4px !important}
.verre-v.v-rond:focus-visible{outline:2px solid #E8A23A; outline-offset:-2px}
@media (prefers-reduced-motion: reduce){ .verre-v, .verre-v.v-rond::before{transition:none !important} }`;
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
    // La ligne du texte (ou le centre du rond) seulement : ce que l'encre doit vaincre.
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
  function besoin(ech, tenue, P, seuil){
    const li = lum(tenue.ink), tc = tenue.tc;
    let dernier = null;
    for (let a = P.min; a <= P.max + 1e-6; a += PAS){
      const vals = ech.map(c => ratio(li, lum([a*tc[0] + (1-a)*c[0], a*tc[1] + (1-a)*c[1], a*tc[2] + (1-a)*c[2]]))).sort((p, q) => p - q);
      const c = vals[Math.floor(vals.length * .05)];
      if (c >= seuil) return {a, ok:true};
      dernier = {a, c, ok:false};
    }
    return dernier;
  }
  function choisir(b, P){
    const ech = dessous(b); if (!ech) return;
    const icone = b.classList.contains("v-rond") || b.id === "retourChoix" || b.classList.contains("retour");
    const seuil = icone ? SEUIL_ICONE : SEUIL_TEXTE;
    const x = {f: besoin(ech, P.f, P, seuil), w: besoin(ech, P.w, P, seuil)};
    const note = r => r.ok ? r.a : 1 + (seuil - r.c);
    let k = note(x.f) <= note(x.w) ? "f" : "w";
    const avant = b.dataset.verreTenue;
    if (avant && avant !== k && note(x[avant]) - note(x[k]) < .10) k = avant;
    const t = P[k], a = x[k].a, rgba = (c, al) => "rgba(" + c[0] + "," + c[1] + "," + c[2] + "," + al.toFixed(2) + ")";
    b.dataset.verreTenue = k;
    b.style.setProperty("--v-haut", rgba(t.tc, Math.min(1, a + .03)));
    b.style.setProperty("--v-bas", rgba(t.tc, a));
    b.style.setProperty("--v-encre", rgba(t.ink, 1));
    b.style.setProperty("--v-fleche", fleche(t.ink, document.documentElement.dir === "rtl"));
    b.classList.toggle("v-blanc", k === "w"); b.classList.toggle("v-fonce", k === "f");
  }

  /* ---------- les boutons et le rythme ---------- */
  // Le rond : « Continuer », « Commencer »… un libelle court et sans fleche. « Continuer avec mes cartes → » garde son
  // texte, et un bouton marque data-rond="non" aussi (« Encore une fois », qui relance la scene).
  const enRond = b => b.classList.contains("suite") && b.dataset.rond !== "non" && !/[→←›‹]/.test(b.textContent) && b.textContent.trim().length <= 16;
  const SEL = ".suite, .bas button, #retourChoix, button.retour#retour";
  /* v1111 : LA FORME SE POSE TOUT DE SUITE. Jacques, 5 nov. 2026 : « dans les scenes, l'ancien bouton continu
     apparait a chaque fois et non seulement le cercle ». Les scenes creent leur « Continuer » a chaque reponse ; la
     classe attendait le calcul suivant, que les confettis reportaient jusqu'a 1,2 s. Elle se pose maintenant dans
     l'observateur, avant que la page se dessine ; seule la mesure de l'image attend. */
  function classer(){
    document.querySelectorAll(SEL).forEach(b => {
      if (!b.classList.contains("verre-v")){
        b.classList.add("verre-v");
        if (getComputedStyle(b).position === "static") b.classList.add("v-pose");
      }
      const r = enRond(b);
      if (b.classList.contains("v-rond") !== r) b.classList.toggle("v-rond", r);
      if (r && b.getAttribute("aria-label") !== b.textContent.trim()) b.setAttribute("aria-label", b.textContent.trim());
    });
  }
  function boutons(){
    classer();
    return [...document.querySelectorAll(SEL)].filter(b => b.offsetParent !== null || getComputedStyle(b).position === "fixed");
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
    boutons().forEach(b => { try{ choisir(b, APPLE); }catch(e){} });
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
    // ⚠️ Nos propres retouches (le style, la classe et le nom des boutons) ne relancent pas le calcul : sinon il tournerait sans fin.
    new MutationObserver(recs => {
      if (recs.some(r => r.type !== "attributes" || !(r.target.classList && r.target.classList.contains("verre-v")))){ classer(); demander(); }
    }).observe(document.body, {childList:true, subtree:true, characterData:true, attributes:true, attributeFilter:["hidden", "class", "style", "src"]});
    classer(); demander();
  }
  if (document.body) observer(); else document.addEventListener("DOMContentLoaded", observer);
})();
