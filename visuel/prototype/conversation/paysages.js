// LE PAYSAGE DE LA CONVERSATION (session de la seance du jour, 11 nov. 2026), au gabarit de PAYSAGES_SEANCE : B, le banc
// au parc (une bulle entre deux personnes), choisi par Jacques le 12 nov. parmi trois dessins (la terrasse et les bulles
// seules ne sont pas deployes). Teinte : la terre de Sienne. Dans l'app, le meme dessin est PAYSAGES_SEANCE.conv, et
// TEINTE_CONVERSATION est TEINTES_PAYSAGE.conv.
const PAYSAGES_CONVERSATION = {"B":{"ar":"M0 100V68C60 58 140 60 200 66S290 74 320 64V100Z","av":"M0 100V88C100 82 220 84 320 90V100Z","milieu":"","supM":"","sup":"<rect x=\"58\" y=\"58\" width=\"4\" height=\"32\"/><circle cx=\"60\" cy=\"48\" r=\"15\"/><circle cx=\"47\" cy=\"57\" r=\"10\"/><circle cx=\"73\" cy=\"57\" r=\"10\"/><rect x=\"120\" y=\"69\" width=\"72\" height=\"3\" rx=\"1\"/><rect x=\"120\" y=\"81\" width=\"72\" height=\"3.4\" rx=\"1\"/><rect x=\"124\" y=\"84\" width=\"3\" height=\"7\"/><rect x=\"185\" y=\"84\" width=\"3\" height=\"7\"/><path d=\"M134 82V72c0-5 3-8 7-8s7 3 7 8V82z\"/><circle cx=\"141\" cy=\"58\" r=\"5.6\"/><path d=\"M164 82V72c0-5 3-8 7-8s7 3 7 8V82z\"/><circle cx=\"171\" cy=\"58\" r=\"5.6\"/><path d=\"M146 24h22a6 6 0 0 1 6 6v6a6 6 0 0 1-6 6h-8l-5 6v-6h-9a6 6 0 0 1-6-6v-6a6 6 0 0 1 6-6z\"/><rect x=\"248\" y=\"52\" width=\"2.6\" height=\"38\"/><path d=\"M243 54h12l-2-6h-8z\"/>","supA":"","astre":[272,26,12]}};
const TEINTE_CONVERSATION = "#A0522D";
// Le dessin, recopie de paysageSeance() : rend le SVG (320 x 100, preserveAspectRatio none) a poser en bas d'ecran,
// et la couleur du sol, a prolonger sous le dessin. nuit : true de nuit.
function dessinerPaysageConversation(variante, nuit){
  const melange = (hex, cible, k) => { const h = c => [1, 3, 5].map(i => parseInt(c.substr(i, 2), 16)), a = h(hex), b = h(cible);
    return "#" + a.map((v, i) => Math.round(v + (b[i] - v) * k).toString(16).padStart(2, "0")).join(""); };
  const L = PAYSAGES_CONVERSATION[variante] || PAYSAGES_CONVERSATION.B, b = TEINTE_CONVERSATION, fond = nuit ? "#0B1626" : "#FFFFFF";
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
