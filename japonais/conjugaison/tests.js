/*
 * Tests de conjugaison.js — `node japonais/conjugaison/tests.js`
 *
 * 1. Cas attendus (oracles/attendus.json) : réponses tirées de kamiya-codec,
 *    japanese-verb-conjugator-v2 et, pour les cas qu'ils ne couvrent pas ou ratent,
 *    de décisions vérifiées avec UniDic. Chaque cas porte sa source.
 *    Aucun ne vient de conjugaison.js. Voir oracles/fabriquer.py.
 * 2. Contrat de l'interface (classes non gérées, entrées incohérentes, variantes).
 * 3. Échantillon large : tous les verbes et adjectifs courants de JMdict
 *    (oracles/jmdict-courants.json). Aucun plantage, aucune forme vide, aucune forme
 *    nulle hors des cas prévus ; les classes non gérées sont comptées et nommées.
 * 4. Si kamiya-codec est installé (NODE_PATH), comparaison avec lui sur l'échantillon
 *    entier, en information seulement : ses écarts connus sont décrits dans LISEZ-MOI.md.
 */
'use strict';
var path = require('path');
var C = require('./conjugaison.js');
var attendus = require('./oracles/attendus.json');
var jmdict = require('./oracles/jmdict-courants.json');

var total = 0, echecs = [];
function verifie(ok, message) {
  total++;
  if (!ok) echecs.push(message);
}
function egal(a, b) { return JSON.stringify(a) === JSON.stringify(b); }

// ------------------------------------------------------------ 1. cas attendus
var parSource = {};
attendus.forEach(function (c) {
  var f = C.forme(c.kanji, c.kana, c.classe, c.forme);
  var obtenu = f ? f[c.ecriture] : null;
  var src = c.source.indexOf('décision') === 0 ? 'décision vérifiée (UniDic)' : c.source;
  parSource[src] = (parSource[src] || 0) + 1;
  verifie(obtenu === c.attendu,
    c.kanji + ' (' + c.kana + ', ' + c.classe + ') ' + c.forme + ' [' + c.ecriture + '] : attendu ' +
    c.attendu + ', obtenu ' + obtenu + '  — source : ' + c.source);
});
var nbAttendus = total;

// ------------------------------------------------------------ 2. contrat
function contrat(nom, ok) { verifie(ok, 'contrat : ' + nom); }

contrat('classe archaïque v4r refusée', C.conjuguer('有る', 'ある', 'v4r') === null);
contrat('erreur() explique le refus', /non gérée/.test(C.erreur('有る', 'ある', 'v4r')));
contrat('classe absente refusée', C.conjuguer('書く', 'かく') === null);
contrat('lecture absente refusée', C.conjuguer('書く', '', 'v5k') === null);
contrat('terminaison incohérente refusée (書く déclaré v5r)', C.conjuguer('書く', 'かく', 'v5r') === null);
contrat('ichidan sans る refusé', C.conjuguer('書く', 'かく', 'v1') === null);
contrat('vk qui ne se lit pas くる refusé', C.conjuguer('帰る', 'かえる', 'vk') === null);
contrat('vs-i sans する refusé', C.conjuguer('勉強', 'べんきょう', 'vs-i') === null);
contrat('adj-ix qui ne se lit pas いい refusé', C.conjuguer('高い', 'たかい', 'adj-ix') === null);
contrat('erreur() vaut null quand tout va bien', C.erreur('書く', 'かく', 'v5k') === null);
contrat('forme inconnue -> null', C.forme('書く', 'かく', 'v5k', 'subjonctif') === null);
contrat('mot sans kanji : le champ kanji reprend le kana',
  egal(C.forme(null, 'しゃべる', 'v5r', 'te'), { kanji: 'しゃべって', kana: 'しゃべって' }));
contrat('mot en katakana', egal(C.forme('サボる', 'サボる', 'v5r', 'nai'), { kanji: 'サボらない', kana: 'サボらない' }));
contrat('c\'est la classe qui décide : 帰る v5r != 変える v1',
  C.forme('帰る', 'かえる', 'v5r', 'nai').kana === 'かえらない' && C.forme('変える', 'かえる', 'v1', 'nai').kana === 'かえない');
contrat('c\'est la classe qui décide : 切る v5r != 着る v1',
  C.forme('切る', 'きる', 'v5r', 'te').kana === 'きって' && C.forme('着る', 'きる', 'v1', 'te').kana === 'きて');
contrat('potentiel ichidan : forme familière notée à part',
  C.forme('食べる', 'たべる', 'v1', 'potentiel').kana === 'たべられる' &&
  C.forme('食べる', 'たべる', 'v1', 'potentiel_familier').kana === 'たべれる');
contrat('potentiel godan : pas de forme familière', C.forme('書く', 'かく', 'v5k', 'potentiel_familier') === null);
contrat('composé de ある : である -> でない', C.forme(null, 'である', 'v5r-i', 'nai').kana === 'でない');
contrat('composé de ある : 事がある -> 事がなかった', C.forme('事がある', 'ことがある', 'v5r-i', 'nakatta').kanji === '事がなかった');
contrat('composé de ある : pas de potentiel', C.forme('事がある', 'ことがある', 'v5r-i', 'potentiel') === null);
contrat('composé de いい : どうでもいい -> どうでもよかった', C.forme(null, 'どうでもいい', 'adj-ix', 'passe').kana === 'どうでもよかった');
contrat('composé de 行く écrit en kana', C.forme('上手くいく', 'うまくいく', 'v5k-s', 'ta').kanji === '上手くいった');
contrat('行く lu ゆく : て en いって', egal(C.forme('行く', 'ゆく', 'v5k-s', 'te'), { kanji: '行って', kana: 'いって' }));
contrat('composé de 来る écrit en kana', egal(C.forme('持ってくる', 'もってくる', 'vk', 'nai'), { kanji: '持ってこない', kana: 'もってこない' }));
contrat('くる seul en kana', egal(C.forme(null, 'くる', 'vk', 'masu'), { kanji: 'きます', kana: 'きます' }));
contrat('vs : le nom reçoit する', C.forme('料理', 'りょうり', 'vs', 'te_iru').kanji === '料理している');
contrat('vs-s : 察しない donné en variante',
  C.conjuguer('察する', 'さっする', 'vs-s').variantes.nai.some(function (v) { return v.kana === 'さっしない'; }));
contrat('adj-na : じゃない donné en variante',
  C.conjuguer('静か', 'しずか', 'adj-na').variantes.negatif[0].kanji === '静かじゃない');
contrat('causatif-passif court du godan en variante',
  C.conjuguer('書く', 'かく', 'v5k').variantes.causatif_passif[0].kana === 'かかされる');
contrat('pas de causatif-passif court pour un verbe en す', !C.conjuguer('話す', 'はなす', 'v5s').variantes.causatif_passif);
contrat('toutes les clés de forme sont présentes (verbe)',
  egal(Object.keys(C.conjuguer('書く', 'かく', 'v5k').formes), C.FORMES_VERBE));
contrat('toutes les clés de forme sont présentes (adjectif)',
  egal(Object.keys(C.conjuguer('高い', 'たかい', 'adj-i').formes), C.FORMES_ADJECTIF));
contrat('fonction pure : deux appels, même résultat, entrée intacte',
  egal(C.conjuguer('問う', 'とう', 'v5u-s'), C.conjuguer('問う', 'とう', 'v5u-s')));
contrat('les tableaux exportés sont des copies', (function () {
  C.CLASSES_VERBES.push('x'); return !C.classeGeree('x');
})());
var nbContrat = total - nbAttendus;

// ------------------------------------------------------------ 3. échantillon JMdict
// Formes qui ont le droit d'être nulles, par classe.
var NULLES_PERMISES = {
  _verbe: ['potentiel_familier'],
  'v1': ['potentiel_familier'], 'vz': [], 'vk': [],
  'v5r-i': ['potentiel', 'potentiel_familier', 'passif', 'causatif', 'causatif_passif', 'te_iru'],
  'v5aru': ['potentiel', 'potentiel_familier', 'passif', 'causatif', 'causatif_passif',
    'imperatif', 'tai', 'te_iru', 'volitif'],
  _adjectif: ['imperatif']
};
var SANS_POTENTIEL = ['わかる', 'できる'];
var nonGerees = {}, refus = [], nbEchantillon = 0, nbFormes = 0;
var avantEchantillon = total;
jmdict.forEach(function (e) {
  var kanji = e[0], kana = e[1], classe = e[2];
  if (!C.classeGeree(classe)) {
    nonGerees[classe] = nonGerees[classe] || [];
    nonGerees[classe].push(kanji || kana);
    return;
  }
  nbEchantillon++;
  var r;
  try { r = C.conjuguer(kanji, kana, classe); } catch (err) {
    verifie(false, 'JMdict : ' + (kanji || kana) + ' ' + classe + ' plante : ' + err.message);
    return;
  }
  if (r === null) {
    refus.push((kanji || kana) + ' (' + kana + ', ' + classe + ') : ' + C.erreur(kanji, kana, classe));
    return;
  }
  var permises = NULLES_PERMISES[classe] ||
    (r.nature === 'adjectif' ? NULLES_PERMISES._adjectif : NULLES_PERMISES._verbe);
  Object.keys(r.formes).forEach(function (nom) {
    var f = r.formes[nom];
    nbFormes++;
    if (f === null) {
      var ok = permises.indexOf(nom) >= 0 ||
        (/^potentiel/.test(nom) && SANS_POTENTIEL.indexOf(kana) >= 0) ||
        (nom === 'potentiel_familier' && r.nature === 'verbe');
      verifie(ok, 'JMdict : ' + (kanji || kana) + ' ' + classe + ' : ' + nom + ' nul sans raison');
    } else {
      verifie(typeof f.kanji === 'string' && f.kanji !== '' && typeof f.kana === 'string' && f.kana !== '',
        'JMdict : ' + (kanji || kana) + ' ' + classe + ' : ' + nom + ' vide');
      // La lecture ne doit contenir aucun kanji.
      verifie(!/[一-鿿]/.test(f.kana), 'JMdict : ' + (kanji || kana) + ' ' + nom + ' : kanji dans la lecture ' + f.kana);
    }
  });
});
// Les rares refus doivent être des entrées réellement incohérentes : on les montre.
verifie(refus.length <= 5, 'JMdict : trop d\'entrées refusées (' + refus.length + ')');
var nbJmdict = total - avantEchantillon;

// ------------------------------------------------------------ 4. kamiya-codec (facultatif)
var kamiya = null;
try { kamiya = require('kamiya-codec'); } catch (e) { /* absent : on saute */ }
var comparaison = null;
if (kamiya) {
  comparaison = { compares: 0, accords: 0 };
  var KM = { nai: [['Nai'], 'Dictionary'], te: [[], 'Te'], ta: [[], 'Ta'], masu: [['Masu'], 'Dictionary'],
    volitif: [[], 'Volitional'], passif: [['ReruRareru'], 'Dictionary'], causatif: [['SeruSaseru'], 'Dictionary'] };
  jmdict.forEach(function (e) {
    var classe = e[2];
    if (!/^(v1|v5[ukgstnbmr])$/.test(classe)) return;
    var r = C.conjuguer(e[0], e[1], classe);
    if (!r) return;
    Object.keys(KM).forEach(function (nom) {
      var k;
      try { k = kamiya.conjugateAuxiliaries(e[1], KM[nom][0], KM[nom][1], classe === 'v1'); } catch (err) { return; }
      comparaison.compares++;
      if (k.indexOf(r.formes[nom].kana) >= 0) comparaison.accords++;
    });
  });
}

// ------------------------------------------------------------ bilan
console.log('Cas attendus (oracles)     : ' + nbAttendus);
Object.keys(parSource).sort().forEach(function (s) { console.log('   ' + parSource[s] + '\t' + s); });
console.log('Contrat de l\'interface     : ' + nbContrat);
console.log('Échantillon JMdict courant : ' + nbEchantillon + ' mots gérés, ' + nbFormes + ' formes, ' + nbJmdict + ' vérifications');
if (refus.length) console.log('   refusés (entrée incohérente) : ' + refus.join(' ; '));
var cles = Object.keys(nonGerees).sort();
console.log('   classes non gérées : ' + (cles.length ? cles.map(function (c) {
  return c + ' (' + nonGerees[c].length + ', ex. ' + nonGerees[c].slice(0, 3).join(' ') + ')';
}).join(', ') : 'aucune'));
if (comparaison) {
  console.log('kamiya-codec sur l\'échantillon (v1 et godan réguliers, 7 formes) : ' + comparaison.accords + '/' + comparaison.compares + ' accords');
}
console.log('');
if (echecs.length) {
  echecs.slice(0, 60).forEach(function (m) { console.log('ÉCHEC  ' + m); });
  if (echecs.length > 60) console.log('… et ' + (echecs.length - 60) + ' autres');
  console.log('\n' + echecs.length + ' échec(s) sur ' + total + ' vérifications.');
  process.exit(1);
}
console.log('Tout passe : ' + total + ' vérifications.');
