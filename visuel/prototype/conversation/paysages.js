// LES TROIS PAYSAGES DE LA CONVERSATION (session de la seance du jour, 11 nov. 2026), au gabarit de PAYSAGES_SEANCE.
// A : la terrasse (deux personnes a une table, une bulle chacune) ; B : le banc au parc (une bulle entre elles) ;
// C : les bulles seules au-dessus des collines. Teinte : la terre de Sienne (TEINTES_PAYSAGE.conv).
// Dans l'app, la variante choisie par Jacques entre dans PAYSAGES_SEANCE.conv, et TEINTE_CONVERSATION dans TEINTES_PAYSAGE.conv.
const PAYSAGES_CONVERSATION = {"A":{"ar":"M0 100V72C80 64 220 64 320 72V100Z","av":"M0 100V90H320V100Z","milieu":"","supM":"","sup":"<path d=\"M120 90V74c0-6 3.6-9 8-9s8 3 8 9V90z\"/><circle cx=\"128\" cy=\"58\" r=\"6.2\"/><path d=\"M184 90V74c0-6 3.6-9 8-9s8 3 8 9V90z\"/><circle cx=\"192\" cy=\"58\" r=\"6.2\"/><rect x=\"143\" y=\"73\" width=\"34\" height=\"3\" rx=\"1\"/><rect x=\"158.5\" y=\"76\" width=\"3\" height=\"14\"/><path d=\"M88 26h40a7 7 0 0 1 7 7v9a7 7 0 0 1-7 7h-20l-9 8v-8h-11a7 7 0 0 1-7-7v-9a7 7 0 0 1 7-7z\"/><path d=\"M192 16h34a7 7 0 0 1 7 7v8a7 7 0 0 1-7 7h-11v7l-8-7h-15a7 7 0 0 1-7-7v-8a7 7 0 0 1 7-7z\"/><rect x=\"262\" y=\"60\" width=\"3\" height=\"30\"/><path d=\"M246 62h34l-6-10h-22z\"/>","supA":"","astre":[44,26,11]},"B":{"ar":"M0 100V68C60 58 140 60 200 66S290 74 320 64V100Z","av":"M0 100V88C100 82 220 84 320 90V100Z","milieu":"","supM":"","sup":"<rect x=\"58\" y=\"58\" width=\"4\" height=\"32\"/><circle cx=\"60\" cy=\"48\" r=\"15\"/><circle cx=\"47\" cy=\"57\" r=\"10\"/><circle cx=\"73\" cy=\"57\" r=\"10\"/><rect x=\"120\" y=\"69\" width=\"72\" height=\"3\" rx=\"1\"/><rect x=\"120\" y=\"81\" width=\"72\" height=\"3.4\" rx=\"1\"/><rect x=\"124\" y=\"84\" width=\"3\" height=\"7\"/><rect x=\"185\" y=\"84\" width=\"3\" height=\"7\"/><path d=\"M134 82V72c0-5 3-8 7-8s7 3 7 8V82z\"/><circle cx=\"141\" cy=\"58\" r=\"5.6\"/><path d=\"M164 82V72c0-5 3-8 7-8s7 3 7 8V82z\"/><circle cx=\"171\" cy=\"58\" r=\"5.6\"/><path d=\"M146 24h22a6 6 0 0 1 6 6v6a6 6 0 0 1-6 6h-8l-5 6v-6h-9a6 6 0 0 1-6-6v-6a6 6 0 0 1 6-6z\"/><rect x=\"248\" y=\"52\" width=\"2.6\" height=\"38\"/><path d=\"M243 54h12l-2-6h-8z\"/>","supA":"","astre":[272,26,12]},"C":{"ar":"M0 100V74C80 66 230 66 320 76V100Z","av":"M0 100V90C100 86 220 86 320 91V100Z","milieu":"","supM":"","sup":"<path d=\"M40 22h52a8 8 0 0 1 8 8v12a8 8 0 0 1-8 8h-30l-10 9v-9h-12a8 8 0 0 1-8-8V30a8 8 0 0 1 8-8z\"/><path d=\"M130 44h40a7 7 0 0 1 7 7v9a7 7 0 0 1-7 7h-8v8l-9-8h-23a7 7 0 0 1-7-7v-9a7 7 0 0 1 7-7z\"/><path d=\"M210 16h30a6 6 0 0 1 6 6v7a6 6 0 0 1-6 6h-16l-7 6v-6h-7a6 6 0 0 1-6-6v-7a6 6 0 0 1 6-6z\"/><path d=\"M22 90q2-14 7-20q-1 11 2 20zM34 90q-2-10-7-15q7 4 11 15zM288 90q2-14 7-20q-1 11 2 20zM300 90q-2-10-7-15q7 4 11 15z\"/>","supA":"","astre":[284,22,10]}};
const TEINTE_CONVERSATION = "#A0522D";
// Le dessin, recopie de paysageSeance() : rend le SVG (320 x 100, preserveAspectRatio none) a poser en bas d'ecran,
// et la couleur du sol, a prolonger sous le dessin. nuit : true de nuit.
function dessinerPaysageConversation(variante, nuit){
  const melange = (hex, cible, k) => { const h = c => [1, 3, 5].map(i => parseInt(c.substr(i, 2), 16)), a = h(hex), b = h(cible);
    return "#" + a.map((v, i) => Math.round(v + (b[i] - v) * k).toString(16).padStart(2, "0")).join(""); };
  const L = PAYSAGES_CONVERSATION[variante] || PAYSAGES_CONVERSATION.A, b = TEINTE_CONVERSATION, fond = nuit ? "#0B1626" : "#FFFFFF";
  const ar = melange(b, fond, nuit ? .62 : .52), av = melange(b, fond, nuit ? .42 : .26), lum = nuit ? "#E8EDF4" : "#FFE3A0";
  const [x, y, r] = L.astre;
  const astre = nuit
    ? '<path d="M' + x + " " + (y - r) + "a" + r + " " + r + " 0 1 0 0 " + (2 * r) + "a" + (r * .72).toFixed(1) + " " + (r * .88).toFixed(1) + " 0 1 1 0-" + (2 * r) + 'z" fill="' + lum + '"/><g fill="' + lum + '" opacity=".75"><circle cx="30" cy="16" r="1.2"/><circle cx="118" cy="10" r="1"/><circle cx="196" cy="22" r="1.2"/><circle cx="304" cy="12" r="1"/><circle cx="150" cy="34" r=".9"/></g>'
    : '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + lum + '"/>';
  const svg = '<svg viewBox="0 0 320 100" preserveAspectRatio="none" aria-hidden="true">' + astre + '<path d="' + L.ar + '" fill="' + ar + '"/>'
    + '<g fill="' + av + '" color="' + av + '"><path d="' + L.av + '"/>' + (L.sup || "") + '</g></svg>';
  // le fond de tout l'ecran, comme la seance : un degrade de la teinte
  const fondEcran = "linear-gradient(180deg," + (nuit ? melange(b, fond, .58) + " 0%," + melange(b, fond, .82) : melange(b, fond, .42) + " 0%," + melange(b, fond, .72)) + " 100%)";
  return { svg, sol: av, fondEcran };
}
if (typeof module !== "undefined") module.exports = { PAYSAGES_CONVERSATION, TEINTE_CONVERSATION, dessinerPaysageConversation };
