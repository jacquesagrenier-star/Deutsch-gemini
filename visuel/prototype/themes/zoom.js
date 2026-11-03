// AGRANDIR LES IMAGES -- commun a tous les themes illustres (3 nov. 2026).
//
// Jacques : « dans les thèmes, on devrait faire comme dans les scènes, donc avoir la possibilité d'agrandir les
// images [...] c'est un peu loin pour voir la couleur des yeux ». Une VISIONNEUSE : l'image en grand sur un fond
// sombre, un bouton pour fermer, et dedans le zoom des scenes (visuel/prototype/index.html, zoomAppliquer) : deux
// doigts pour agrandir jusqu'a x4 autour du point entre les doigts, un doigt pour se deplacer une fois agrandi, un
// double toucher pour passer de 1:1 a x2,5 et retour ; la molette a l'ordinateur.
// Ce qui l'ouvre :
//   - DEUX DOIGTS sur une image de l'exercice (le geste des scenes) : la visionneuse s'ouvre et suit le meme geste ;
//   - un TOUCHER sur une image qui n'est pas une reponse (gros plan des yeux, visage, photo d'une fiche) : `direct` ;
//   - la LOUPE posee sur ce qu'on touche pour repondre (les personnes d'une rangee, l'arbre, les cases de la
//     decouverte), pour ne jamais repondre en voulant regarder : `loupe`.
// Un element qui n'est pas une image (l'arbre en SVG) est COPIE dans la visionneuse : la copie se regarde, elle ne
// repond pas. L'indice « Écarte deux doigts » des scenes (v1068) s'affiche dans la visionneuse les deux premieres fois.
// Une page : <script src="themes/zoom.js?v=3"></script>, puis Zoom.init({direct: "...", loupe: "...", langue}).
const Zoom = (() => {
  const TEXTES = {
    pince: {fr: "Écarte deux doigts pour agrandir", en: "Spread two fingers to zoom in", tr: "Yakınlaştırmak için iki parmağını aç", uk: "Розведи два пальці, щоб збільшити", fa: "برای بزرگ‌نمایی دو انگشتت را از هم باز کن", ar: "باعِد بين إصبعين للتكبير", pt: "Afaste dois dedos para ampliar", pl: "Rozsuń dwa palce, aby powiększyć", ru: "Разведи два пальца, чтобы увеличить", de: "Spreize zwei Finger zum Vergrößern"},
    fermer: {fr: "Fermer", en: "Close", tr: "Kapat", uk: "Закрити", fa: "بستن", ar: "إغلاق", pt: "Fechar", pl: "Zamknij", ru: "Закрыть", de: "Schließen"},
    agrandir: {fr: "Agrandir l'image", en: "Enlarge the picture", tr: "Resmi büyüt", uk: "Збільшити зображення", fa: "بزرگ کردن تصویر", ar: "تكبير الصورة", pt: "Ampliar a imagem", pl: "Powiększ obrazek", ru: "Увеличить картинку", de: "Bild vergrößern"}
  };
  let langue = "fr";
  const T = c => TEXTES[c][langue] || TEXTES[c].fr;
  const CSS = `
.zoom-voile{position:fixed;inset:0;z-index:9000;background:rgba(8,12,18,.94);display:flex;align-items:center;justify-content:center;touch-action:none;overflow:hidden}
.zoom-voile[hidden]{display:none}
.zoom-voile .zoom-contenu{transform-origin:0 0;will-change:transform;user-select:none;-webkit-user-select:none;-webkit-touch-callout:none}
.zoom-voile img.zoom-contenu{max-width:100%;max-height:100%;object-fit:contain;display:block}
.zoom-voile div.zoom-contenu{width:min(100%,900px);pointer-events:none}
.zoom-fermer{position:absolute;top:calc(env(safe-area-inset-top,0px) + 12px);inset-inline-end:14px;width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.4);
  background:rgba(255,255,255,.16);color:#fff;font:700 26px/1 system-ui,sans-serif;cursor:pointer;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);z-index:2}
.zoom-fermer:focus-visible{outline:3px solid #E8A23A;outline-offset:2px}
.zoom-loupe{position:absolute;top:0;inset-inline-end:0;width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.9);display:flex;align-items:center;
  justify-content:center;box-shadow:0 1px 4px rgba(0,0,0,.28);cursor:zoom-in;z-index:2}
/* Jacques, 3 nov. 2026 : « tasser les loupes le plus possible dans le coin droit en haut. Qui prennent le moins de place
   sur le champ. » Un rond de 22 px colle au coin ; le doigt, lui, a une zone de 38 px, surtout hors de l'image
   (::before transparent), pour toucher la loupe sans choisir la personne par erreur. */
.zoom-loupe::before{content:"";position:absolute;inset:-8px}
.zoom-loupe svg{width:13px;height:13px;fill:none;stroke:#1C2430;stroke-width:2.6;stroke-linecap:round}
.zoom-direct{cursor:zoom-in}
.zoom-voile .pince{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;pointer-events:none;animation:zpv 3.4s ease forwards}
@keyframes zpv{0%{opacity:0}8%{opacity:1}86%{opacity:1}100%{opacity:0}}
.zoom-voile .doigts{position:relative;width:150px;height:150px}
.zoom-voile .doigt{position:absolute;left:50%;top:50%;width:42px;height:42px;margin:-21px;border-radius:50%;background:rgba(255,255,255,.22);
  box-shadow:0 0 0 2px rgba(120,200,150,.95),0 0 0 7px rgba(120,200,150,.25),0 6px 14px rgba(0,0,0,.30)}
.zoom-voile .d1{transform:translate(-10px,10px);animation:zd1 1.3s ease-in-out .3s 2}
.zoom-voile .d2{transform:translate(10px,-10px);animation:zd2 1.3s ease-in-out .3s 2}
@keyframes zd1{0%,100%{transform:translate(-10px,10px)}45%,60%{transform:translate(-46px,46px)}}
@keyframes zd2{0%,100%{transform:translate(10px,-10px)}45%,60%{transform:translate(46px,-46px)}}
.zoom-voile .phrase{color:#fff;font:800 15px Nunito,system-ui,sans-serif;padding:9px 16px;border-radius:999px;background:rgba(255,255,255,.18);max-width:86%;text-align:center}
@media (prefers-reduced-motion: reduce){.zoom-voile .pince,.zoom-voile .d1,.zoom-voile .d2{animation:none}}`;
  // l'indice se montre deux fois dans les themes, et plus jamais apres un premier agrandissement, ici OU dans les
  // scenes (meme origine, meme cle que visuel/prototype/index.html : PINCE_ZOOME)
  const VUS = "wortando_pinceThemesVus", ZOOME = "wortando_pinceZoome";
  let voile = null, cont = null, ouvert = false, opts = {direct: "", loupe: "", pincer: ""};
  let Z = {s: 1, x: 0, y: 0, pinch: null, pan: null, bouge: false, dernier: 0};
  const pt = t => [t.clientX, t.clientY];

  function construire(){
    if (voile) return;
    const st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    voile = document.createElement("div"); voile.className = "zoom-voile"; voile.hidden = true;
    voile.setAttribute("role", "dialog"); voile.setAttribute("aria-modal", "true");
    const f = document.createElement("button"); f.type = "button"; f.className = "zoom-fermer"; f.textContent = "×";
    f.setAttribute("aria-label", T("fermer"));
    f.addEventListener("click", e => { e.stopPropagation(); fermer(); });
    voile.appendChild(f);
    document.body.appendChild(voile);
    // un toucher sur le fond ferme (pas sur l'image, pas apres un geste)
    voile.addEventListener("click", e => { e.stopPropagation(); if (Z.bouge){ Z.bouge = false; return; } if (e.target === voile && Z.s === 1) fermer(); });
    voile.addEventListener("wheel", e => {
      e.preventDefault();
      const r = cont.getBoundingClientRect(), s0 = Z.s, s = Math.max(1, Math.min(4, s0 * (e.deltaY < 0 ? 1.15 : 1 / 1.15)));
      const mx = e.clientX - (r.left - Z.x), my = e.clientY - (r.top - Z.y), ix = (mx - Z.x) / s0, iy = (my - Z.y) / s0;
      Z.s = s; Z.x = mx - ix * s; Z.y = my - iy * s; appliquer();
    }, {passive: false});
  }
  // le debut d'un pincement : L, T = la place du contenu sans transformation (il est centre dans le voile)
  function debutPince(e){
    const a = pt(e.touches[0]), b = pt(e.touches[1]), r = cont.getBoundingClientRect(), L = r.left - Z.x, T0 = r.top - Z.y;
    Z.pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]) || 1, m: [(a[0] + b[0]) / 2 - L, (a[1] + b[1]) / 2 - T0], L, T: T0, s: Z.s, x: Z.x, y: Z.y};
    Z.pan = null; Z.bouge = true; retirerPince();
  }
  // LES GESTES : ecoutes sur le document, pour qu'un pincement commence sur l'image de l'exercice et continue dans
  // la visionneuse qu'il vient d'ouvrir (les touchmove suivent l'element du touchstart, pas ce qui est dessous).
  function ecouter(){
    document.addEventListener("touchstart", e => {
      if (!ouvert){
        if (e.touches.length !== 2) return;
        const el = cibleDe(e.target);
        if (!el) return;
        e.preventDefault();
        ouvrir(el);
        debutPince(e);
        return;
      }
      if (e.target.closest && e.target.closest(".zoom-fermer")) return;
      if (e.touches.length === 2) debutPince(e);
      else if (e.touches.length === 1){ Z.bouge = false; if (Z.s > 1) Z.pan = {p: pt(e.touches[0]), x: Z.x, y: Z.y}; }
    }, {passive: false});
    document.addEventListener("touchmove", e => {
      if (!ouvert) return;
      e.preventDefault();
      if (Z.pinch && e.touches.length >= 2){
        const a = pt(e.touches[0]), b = pt(e.touches[1]), p0 = Z.pinch;
        const d = Math.hypot(a[0] - b[0], a[1] - b[1]) || 1, m = [(a[0] + b[0]) / 2 - p0.L, (a[1] + b[1]) / 2 - p0.T];
        const s = Math.max(1, Math.min(4, p0.s * d / p0.d));
        // le point du contenu qui etait sous les doigts y reste
        const ix = (p0.m[0] - p0.x) / p0.s, iy = (p0.m[1] - p0.y) / p0.s;
        Z.s = s; Z.x = m[0] - ix * s; Z.y = m[1] - iy * s; appliquer();
      } else if (Z.pan && e.touches.length === 1 && Z.s > 1){
        const p = pt(e.touches[0]), dx = p[0] - Z.pan.p[0], dy = p[1] - Z.pan.p[1];
        if (Math.abs(dx) + Math.abs(dy) > 8) Z.bouge = true;
        if (Z.bouge){ Z.x = Z.pan.x + dx; Z.y = Z.pan.y + dy; appliquer(); }
      }
    }, {passive: false});
    document.addEventListener("touchend", e => {
      if (!ouvert) return;
      if (e.touches.length < 2) Z.pinch = null;
      if (e.touches.length) return;
      Z.pan = null;
      if (Z.bouge){ setTimeout(() => { Z.bouge = false; }, 350); return; }
      // double toucher : x2,5 autour du doigt, ou retour a 1:1
      const t = Date.now(), c = e.changedTouches[0];
      if (t - Z.dernier < 300 && c && !(e.target.closest && e.target.closest(".zoom-fermer"))){
        if (Z.s > 1){ Z.s = 1; Z.x = 0; Z.y = 0; }
        else { const r = cont.getBoundingClientRect(), s = 2.5; Z.s = s; Z.x = (c.clientX - r.left) * (1 - s); Z.y = (c.clientY - r.top) * (1 - s); }
        appliquer(); Z.dernier = 0; Z.bouge = true; setTimeout(() => { Z.bouge = false; }, 350);
      } else Z.dernier = t;
    }, {passive: true});
    document.addEventListener("keydown", e => { if (e.key === "Escape" && ouvert) fermer(); });
    // le toucher direct, par delegation : les images changent a chaque question
    document.addEventListener("click", e => {
      if (ouvert || !opts.direct || !e.target.closest) return;
      const im = e.target.closest(opts.direct);
      if (im){ e.stopPropagation(); e.preventDefault(); ouvrir(im); }
    }, true);
  }
  // ce que deux doigts agrandissent : une image de l'exercice, ou ce qui porte une loupe
  function cibleDe(t){
    if (!t || !t.closest) return null;
    const porte = opts.loupe && t.closest(opts.loupe);
    if (porte) return contenuDe(porte);
    const im = t.closest("main img, main svg");
    return im ? (im.tagName === "IMG" ? im : im.closest("svg")) : null;
  }
  // data-zoom : une autre image a montrer agrandie (le visage d'une personne en pied)
  function contenuDe(porte){ return porte.dataset && porte.dataset.zoom || (porte.tagName === "IMG" ? porte : porte.querySelector("img") || porte); }
  function appliquer(){
    const W = cont.offsetWidth, H = cont.offsetHeight;
    Z.s = Math.max(1, Math.min(4, Z.s));
    Z.x = Math.min(0, Math.max(W * (1 - Z.s), Z.x));
    Z.y = Math.min(0, Math.max(H * (1 - Z.s), Z.y));
    cont.style.transform = Z.s === 1 ? "" : "translate(" + Z.x + "px," + Z.y + "px) scale(" + Z.s + ")";
    if (Z.s > 1){ try{ localStorage.setItem(ZOOME, "1"); }catch(e){} retirerPince(); }
  }
  function indice(){
    let vus = 0;
    try{ vus = +localStorage.getItem(VUS) || 0; if (localStorage.getItem(ZOOME) === "1") return; }catch(e){ return; }
    if (vus >= 2) return;
    try{ localStorage.setItem(VUS, String(vus + 1)); }catch(e){}
    const el = document.createElement("div"); el.className = "pince"; el.setAttribute("aria-hidden", "true");
    el.innerHTML = '<div class="doigts"><div class="doigt d1"></div><div class="doigt d2"></div></div><div class="phrase"></div>';
    el.querySelector(".phrase").textContent = T("pince");
    voile.appendChild(el);
    el.addEventListener("animationend", ev => { if (ev.target === el) el.remove(); });
  }
  function retirerPince(){ if (voile) voile.querySelectorAll(".pince").forEach(el => el.remove()); }
  // ouvrir(element) : une image (sa source) ou un autre element (copie) ; ouvrir("adresse") aussi
  function ouvrir(el, clavier){
    construire();
    if (cont) cont.remove();
    if (typeof el === "string" || el.tagName === "IMG"){
      cont = document.createElement("img"); cont.alt = "";
      cont.src = typeof el === "string" ? el : (el.currentSrc || el.src);
    } else {
      // la copie garde l'allure de son conteneur (.arbre) ; ses identifiants, dedoubles, sont retires
      cont = document.createElement("div");
      const copie = (el.closest("[class]") || el).cloneNode(true);
      copie.querySelectorAll(".zoom-loupe").forEach(x => x.remove());
      copie.removeAttribute && copie.removeAttribute("id");
      copie.querySelectorAll("[id]:not(clipPath):not(linearGradient):not(radialGradient):not(mask)").forEach(x => x.removeAttribute("id"));
      copie.setAttribute("aria-hidden", "true");
      cont.appendChild(copie);
    }
    cont.className = "zoom-contenu";
    voile.insertBefore(cont, voile.firstChild);
    Z = {s: 1, x: 0, y: 0, pinch: null, pan: null, bouge: false, dernier: 0};
    voile.hidden = false; ouvert = true;
    retirerPince(); indice();
    // au clavier, le bouton fermer prend la main ; au doigt, pas d'anneau de focus sur la photo
    if (clavier) voile.querySelector(".zoom-fermer").focus({preventScroll: true});
  }
  function fermer(){ if (voile){ voile.hidden = true; ouvert = false; retirerPince(); } }
  const LOUPE = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5M10.5 8v5M8 10.5h5"/></svg>';
  // pose les loupes sur ce qui vient d'apparaitre (la page change d'ecran a chaque question)
  function poserLoupes(){
    document.querySelectorAll(opts.loupe).forEach(b => {
      if (b.closest(".zoom-voile") || b.querySelector(":scope > .zoom-loupe")) return;
      if (getComputedStyle(b).position === "static") b.style.position = "relative";
      const l = document.createElement("span"); l.className = "zoom-loupe"; l.setAttribute("role", "button"); l.tabIndex = 0;
      l.setAttribute("aria-label", T("agrandir")); l.innerHTML = LOUPE;
      const go = (e, clavier) => { e.stopPropagation(); e.preventDefault(); ouvrir(contenuDe(b), clavier); };
      l.addEventListener("click", go);
      l.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") go(e, true); });
      b.appendChild(l);
    });
  }
  function init(o){
    opts = Object.assign(opts, o || {});
    langue = opts.langue || "fr";
    construire(); ecouter();
    const marquer = () => {
      if (opts.direct) document.querySelectorAll(opts.direct).forEach(im => im.classList.add("zoom-direct"));
      if (opts.loupe) poserLoupes();
    };
    new MutationObserver(marquer).observe(document.body, {childList: true, subtree: true});
    marquer();
  }
  return {init, ouvrir, fermer};
})();
