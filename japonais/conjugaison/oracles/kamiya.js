/*
 * Oracle n°1 : kamiya-codec 4.16.1 (licence Unlicense, domaine public),
 * https://github.com/fasiha/kamiya-codec — d'après les Handbooks de Taeko Kamiya.
 *
 * Utilisé SEULEMENT pour fabriquer les réponses attendues des tests, jamais par conjugaison.js.
 *
 *   npm install --no-save kamiya-codec@4.16.1   (dans un dossier hors dépôt)
 *   NODE_PATH=<ce dossier>/node_modules node oracles/kamiya.js > oracles/kamiya.json
 *
 * Sortie : { "kanji|kana|classe": { "kanji": { forme: [candidats] }, "kana": {...} } }
 *
 * Adaptateur assumé : kamiya ne reconnaît する et 来る que seuls, et 行く que seul.
 * Pour 勉強する, 持って来る, 出て行く, on conjugue la base et on remet le préfixe.
 * vs-s et vz ne sont pas soumis à kamiya : il ne connaît pas ces classes.
 */
var k = require('kamiya-codec');
var mots = require('./mots-tests.json');

var VERBE = {
  dictionnaire: [[], 'Dictionary'], masu: [['Masu'], 'Dictionary'], masen: [['Masu'], 'Negative'],
  mashita: [['Masu'], 'Ta'], masen_deshita: [['Masu'], 'Negative'], mashou: [['Masu'], 'Volitional'],
  te: [[], 'Te'], ta: [[], 'Ta'], nai: [['Nai'], 'Dictionary'], nakatta: [['Nai'], 'Ta'],
  potentiel: [['Potential'], 'Dictionary'], potentiel_familier: [['Potential'], 'Dictionary'],
  passif: [['ReruRareru'], 'Dictionary'], causatif: [['SeruSaseru'], 'Dictionary'],
  causatif_passif: [['CausativePassive'], 'Dictionary'], volitif: [[], 'Volitional'],
  imperatif: [[], 'Imperative'], ba: [[], 'Conditional'], tara: [[], 'Tara'],
  tai: [['Tai'], 'Dictionary'], te_iru: [['TeIru'], 'Dictionary']
};
var ADJ = {
  present: 'Present', negatif: 'Negative', passe: 'Past', passe_negatif: 'NegativePast',
  adverbe: 'Adverbial', te: 'ConjunctiveTe', ba: 'Conditional', attributif: 'Prenomial',
  poli: 'Present', poli_negatif: 'Negative', poli_passe: 'Past'
};

function base(mot, classe) {
  // [préfixe, verbe que kamiya connaît]
  var bases = { 'vs-i': ['する'], 'vs': ['する'], 'vk': ['来る', 'くる'], 'v5k-s': ['行く', 'いく'] };
  var b = bases[classe];
  if (!b) return ['', mot];
  if (classe === 'vs') return [mot, 'する'];
  for (var i = 0; i < b.length; i++) {
    if (mot.slice(-b[i].length) === b[i]) return [mot.slice(0, -b[i].length), b[i]];
  }
  return ['', mot];
}

var sortie = {};
mots.forEach(function (m) {
  var classe = m[2];
  if (classe === 'vs-s' || classe === 'vz') return;
  var r = {};
  [['kanji', m[0]], ['kana', m[1]]].forEach(function (p) {
    var formes = {};
    if (classe.indexOf('adj') === 0) {
      Object.keys(ADJ).forEach(function (f) {
        try { formes[f] = k.adjConjugate(p[1], ADJ[f], classe !== 'adj-na'); } catch (e) { formes[f] = []; }
      });
    } else {
      var b = base(p[1], classe);
      var typeII = classe === 'v1' || classe === 'v1-s';
      Object.keys(VERBE).forEach(function (f) {
        try {
          formes[f] = k.conjugateAuxiliaries(b[1], VERBE[f][0], VERBE[f][1], typeII).map(function (x) { return b[0] + x; });
        } catch (e) { formes[f] = []; }
      });
    }
    r[p[0]] = formes;
  });
  sortie[m.join('|')] = r;
});
process.stdout.write(JSON.stringify(sortie, null, 1) + '\n');
