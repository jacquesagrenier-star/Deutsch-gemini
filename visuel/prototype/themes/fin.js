// L'ECRAN DE FIN DES THEMES ILLUSTRES, une seule source pour les 22 pages (8 nov. 2026, retour de Jacques en seance :
// « 6 bonnes reponses sur 8 », « un peu sec », « comme en blanc », « il faudrait avoir des encouragements »).
// Le bareme et les textes sont ceux des scenes (bilan() de visuel/prototype/index.html) : un compliment qu'on recoit quoi
// qu'on fasse ne veut plus rien dire. Bon resultat : confettis et son. Resultat faible : sobre, jamais de reproche
// (les points non gagnes restent neutres, pas rouges). Les boutons restent ceux de chaque page.
const Fin = (() => {
  const TEXTES = {
    sansFaute: {fr: "sans faute, bravo !", en: "no mistakes, well done!", tr: "hatasız, bravo!", uk: "без помилок, браво!", fa: "بدون اشتباه، آفرین!", ar: "بلا أخطاء، أحسنت!", pt: "sem erros, parabéns!", pl: "bez błędu, brawo!", ru: "без ошибок, браво!", de: "fehlerfrei, super!", es: "¡sin errores, bravo!"},
    bienJoue:  {fr: "bien joué.", en: "well played.", tr: "iyi iş.", uk: "добре.", fa: "خوب بود.", ar: "أحسنت.", pt: "muito bem.", pl: "dobra robota.", ru: "молодец.", de: "gut gemacht.", es: "bien hecho."},
    caViendra: {fr: "ça viendra : on retient aussi en se trompant.", en: "it will come: we also learn from mistakes.", tr: "olacak: hata yaparak da öğreniriz.", uk: "усе прийде: ми вчимося й на помилках.", fa: "کم‌کم یاد می‌گیری: از اشتباه هم یاد می‌گیریم.", ar: "سيأتي ذلك: نتعلم من أخطائنا أيضًا.", pt: "vai chegar lá: também se aprende errando.", pl: "przyjdzie z czasem: na błędach też się uczymy.", ru: "всё придёт: на ошибках тоже учатся.", de: "das kommt noch: Aus Fehlern lernt man auch.", es: "ya llegará: también se aprende al equivocarse."},
    pasGrave:  {fr: "pas grave, on retient aussi en se trompant.", en: "no problem, we also learn from mistakes.", tr: "sorun değil, hata yaparak da öğreniriz.", uk: "нічого страшного, ми вчимося й на помилках.", fa: "اشکالی ندارد، از اشتباه هم یاد می‌گیریم.", ar: "لا بأس، نتعلم من أخطائنا أيضًا.", pt: "tudo bem, também se aprende errando.", pl: "nic nie szkodzi, na błędach też się uczymy.", ru: "ничего страшного, на ошибках тоже учатся.", de: "kein Problem, aus Fehlern lernt man auch.", es: "no pasa nada, también se aprende al equivocarse."}
  };

  const style = document.createElement("style");
  style.textContent = `
.fin-image{display:block;width:176px;max-width:56%;aspect-ratio:600/510;object-fit:cover;border-radius:18px;box-shadow:0 6px 20px rgba(20,30,40,.14);margin-top:6px}
.fin-phrase{font-size:23px;font-weight:900;line-height:1.25;color:var(--encre);max-width:30ch}
.fin-compte{font-size:16px;font-weight:600;color:var(--gris)}
.fin-points{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;max-width:250px;margin:2px 0 6px;color:var(--gris)}
.fin-points i{display:block;width:12px;height:12px;border-radius:50%;background:currentColor;opacity:.22;animation:finPoint .32s calc(var(--r) * 55ms) both cubic-bezier(.2,1.5,.5,1)}
.fin-points.bon i.g{background:var(--vert);opacity:1}
.fin-points.doux i.g{background:var(--ambre-f);opacity:1}
@keyframes finPoint{from{transform:scale(0)}to{transform:scale(1)}}
.confetti-piece{position:fixed;top:0;left:0;border-radius:2px;pointer-events:none;z-index:9999;animation-name:confettiBurst;animation-timing-function:cubic-bezier(.15,.7,.4,1);animation-fill-mode:forwards}
@keyframes confettiBurst{0%{transform:translate(-50%,-50%) rotate(0deg) scale(1);opacity:1}100%{transform:translate(calc(-50% + var(--dx)),calc(-50% + var(--dy))) rotate(var(--rot)) scale(.4);opacity:0}}
@media (prefers-reduced-motion:reduce){.confetti-piece{display:none}.fin-points i{animation:none}}`;
  document.head.appendChild(style);

  // la vignette du theme (celle de l'accueil), chargee d'avance : l'ecran de fin ne doit pas sauter quand elle arrive
  const nom = location.pathname.split("/").pop().replace(/\.html$/, "");
  const source = "themes/" + nom + ".webp";
  new Image().src = source;
  const image = '<img class="fin-image" src="' + source + '" alt="" onerror="this.remove()">';

  // « bien joué. » dans les scenes suit un tiret ; ici il ouvre sa ligne. toLocaleUpperCase : le i turc (« İyi iş. »).
  const majuscule = (s, l) => s.replace(/\p{L}/u, c => c.toLocaleUpperCase(l));
  const mot = (cle, l) => majuscule(TEXTES[cle][l] || TEXTES[cle].fr, l);

  function confettis(){
    const couleurs = ["#3b82f6", "#8b5cf6", "#22c55e", "#f59e0b", "#ef4444", "#06b6d4"];
    const cx = innerWidth / 2, cy = innerHeight * 0.35;
    for (let k = 0; k < 28; k++){
      const e = document.createElement("div"), a = Math.random() * Math.PI * 2, d = 90 + Math.random() * 150;
      e.className = "confetti-piece";
      e.style.left = cx + "px"; e.style.top = cy + "px";
      e.style.background = couleurs[Math.floor(Math.random() * couleurs.length)];
      e.style.setProperty("--dx", Math.cos(a) * d + "px");
      e.style.setProperty("--dy", Math.sin(a) * d - 70 + "px");
      e.style.setProperty("--rot", (Math.random() * 720 - 360) + "deg");
      e.style.width = (5 + Math.random() * 5) + "px";
      e.style.height = (8 + Math.random() * 8) + "px";
      e.style.animationDuration = (0.8 + Math.random() * 0.6) + "s";
      document.body.appendChild(e);
      e.addEventListener("animationend", () => e.remove());
    }
  }

  // Le meme bareme que bilan() des scenes.
  const cleDuBilan = (b, n) => b === n ? "sansFaute" : b * 2 >= n ? "bienJoue" : b > 0 ? "caViendra" : "pasGrave";

  // Rend le contenu de la fin d'une partie, et fete un bon resultat (a appeler une fois, dans le toucher qui clot la partie).
  function bilan(langue, b, n, score){
    const cle = n ? cleDuBilan(b, n) : "";
    const bon = cle === "sansFaute" || cle === "bienJoue";
    let points = "";
    for (let k = 0; k < n; k++) points += '<i' + (k < b ? ' class="g"' : '') + ' style="--r:' + k + '"></i>';
    if (bon){ confettis(); try{ Voix.bravo(); }catch(e){} }
    return '<div class="fin">' + image
      + (cle ? '<div class="fin-phrase">' + mot(cle, langue) + '</div>' : '')
      + '<div class="fin-compte">' + score + '</div>'
      + (n ? '<div class="fin-points ' + (bon ? 'bon' : 'doux') + '" aria-hidden="true">' + points + '</div>' : '')
      + '</div>';
  }

  // « Tout est revu pour aujourd'hui » : aucune partie jouee, donc ni son ni confettis.
  function revu(texte, suite){
    return '<div class="fin">' + image + '<div class="fin-phrase">' + texte + '</div>'
      + (suite ? '<div class="fin-compte">' + suite + '</div>' : '') + '</div>';
  }

  return {bilan, revu};
})();
