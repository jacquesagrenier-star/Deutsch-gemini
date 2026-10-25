/*
 * conjugaison.js — générateur de conjugaison japonaise (verbes et adjectifs).
 *
 * JavaScript pur, sans dépendance ni module : collable tel quel dans un <script>.
 * Expose un seul objet global, `Conjugaison` (et `module.exports` sous node).
 *
 *   Conjugaison.conjuguer('帰る', 'かえる', 'v5r')
 *     -> { classe, nature: 'verbe', formes: { te: { kanji: '帰って', kana: 'かえって' }, ... },
 *          variantes: { ... } }
 *
 * C'est la classe JMdict qui décide, jamais la terminaison : 帰る est v5r, 変える est v1.
 * Une forme qui n'existe pas ou n'a pas de sens vaut null. Une classe non gérée,
 * ou une entrée incohérente (lecture qui ne finit pas comme la classe l'annonce),
 * rend null ; Conjugaison.erreur() dit pourquoi.
 */
var Conjugaison = (function () {
  'use strict';

  // Rangées du godan : terminaison du dictionnaire -> [a, i, e, o].
  var RANGEES = {
    'う': ['わ', 'い', 'え', 'お'],
    'く': ['か', 'き', 'け', 'こ'],
    'ぐ': ['が', 'ぎ', 'げ', 'ご'],
    'す': ['さ', 'し', 'せ', 'そ'],
    'つ': ['た', 'ち', 'て', 'と'],
    'ぬ': ['な', 'に', 'ね', 'の'],
    'ぶ': ['ば', 'び', 'べ', 'ぼ'],
    'む': ['ま', 'み', 'め', 'も'],
    'る': ['ら', 'り', 'れ', 'ろ']
  };

  // Forme en て (et donc た) du godan, selon la terminaison.
  var EUPHONIE = {
    'う': 'って', 'つ': 'って', 'る': 'って',
    'く': 'いて', 'ぐ': 'いで', 'す': 'して',
    'ぬ': 'んで', 'ぶ': 'んで', 'む': 'んで'
  };

  // Terminaison attendue pour chaque classe godan.
  var GODAN = {
    'v5u': 'う', 'v5k': 'く', 'v5g': 'ぐ', 'v5s': 'す', 'v5t': 'つ',
    'v5n': 'ぬ', 'v5b': 'ぶ', 'v5m': 'む', 'v5r': 'る',
    'v5k-s': 'く', 'v5r-i': 'る', 'v5u-s': 'う', 'v5aru': 'る'
  };

  var CLASSES_VERBES = ['v1', 'v1-s', 'v5u', 'v5k', 'v5g', 'v5s', 'v5t', 'v5n', 'v5b',
    'v5m', 'v5r', 'v5k-s', 'v5r-i', 'v5u-s', 'v5aru', 'vk', 'vs', 'vs-i', 'vs-s', 'vz'];
  var CLASSES_ADJECTIFS = ['adj-i', 'adj-ix', 'adj-na'];

  // Ordre des formes, utile pour afficher un tableau.
  var FORMES_VERBE = ['dictionnaire', 'masu', 'masen', 'mashita', 'masen_deshita', 'mashou',
    'te', 'ta', 'nai', 'nakatta', 'potentiel', 'potentiel_familier', 'passif', 'causatif',
    'causatif_passif', 'volitif', 'imperatif', 'ba', 'tara', 'tai', 'te_iru'];
  var FORMES_ADJECTIF = ['present', 'negatif', 'passe', 'passe_negatif', 'adverbe', 'te', 'ba',
    'poli', 'poli_negatif', 'poli_passe', 'attributif', 'imperatif'];

  // Verbes dont le potentiel n'a pas de sens (ils expriment déjà une capacité).
  // Clé : lecture en kana. ある (v5r-i) est traité par sa classe.
  var SANS_POTENTIEL = { 'わかる': 1, 'できる': 1 };

  // ---------------------------------------------------------------- outils

  function finit(s, fin) {
    return s.length >= fin.length && s.slice(s.length - fin.length) === fin;
  }

  function sans(s, n) { return s.slice(0, s.length - n); }

  // Un « radical » garde côte à côte la partie kanji et la partie kana.
  // f('ない') ou f('ない', 'こない') : le second argument sert quand la partie kana
  // diffère de la partie kanji (来る : 来ない / こない).
  function radical(kj, kn) {
    return function (suffixeKanji, suffixeKana) {
      return { kanji: kj + suffixeKanji, kana: kn + (suffixeKana === undefined ? suffixeKanji : suffixeKana) };
    };
  }

  function variante(forme, note) {
    return { kanji: forme.kanji, kana: forme.kana, note: note };
  }

  function ajouter(variantes, cle, forme, note) {
    if (!variantes[cle]) variantes[cle] = [];
    variantes[cle].push(variante(forme, note));
  }

  // Formes polies et dérivées du radical en -i (連用形) : ます, たい.
  function polies(formes, ren) {
    formes.masu = ren('ます');
    formes.masen = ren('ません');
    formes.mashita = ren('ました');
    formes.masen_deshita = ren('ませんでした');
    formes.mashou = ren('ましょう');
    formes.tai = ren('たい');
  }

  function vide(liste) {
    var o = {};
    for (var i = 0; i < liste.length; i++) o[liste[i]] = null;
    return o;
  }

  // ---------------------------------------------------------------- verbes

  function godan(kanji, kana, classe, formes, variantes) {
    var fin = GODAN[classe];
    var r = RANGEES[fin];
    var f = radical(sans(kanji, 1), sans(kana, 1));
    var ren = f(r[1]);

    formes.dictionnaire = f(fin);
    polies(formes, function (s) { return f(r[1] + s); });
    formes.nai = f(r[0] + 'ない');
    formes.nakatta = f(r[0] + 'なかった');
    formes.potentiel = f(r[2] + 'る');
    formes.passif = f(r[0] + 'れる');
    formes.causatif = f(r[0] + 'せる');
    formes.causatif_passif = f(r[0] + 'せられる');
    formes.volitif = f(r[3] + 'う');
    formes.imperatif = f(r[2]);
    formes.ba = f(r[2] + 'ば');

    // て / た : la seule partie vraiment irrégulière du godan.
    var te = EUPHONIE[fin];
    if (classe === 'v5k-s') te = 'って';             // 行く : 行って, jamais 行いて
    if (classe === 'v5u-s') te = 'うて';             // 問う, 請う : 問うて, 問うた
    var ta = te.slice(0, -1) + (te.slice(-1) === 'で' ? 'だ' : 'た');
    var fte = f;
    if (classe === 'v5k-s' && finit(kana, 'ゆく')) {
      // 行く lu ゆく : le て se dit いって. Le kanji ne bouge pas, la lecture si.
      var kjTe = finit(kanji, 'ゆく') ? sans(kanji, 2) + 'い' : sans(kanji, 1);
      fte = radical(kjTe, sans(kana, 2) + 'い');
    }
    formes.te = fte(te);
    formes.ta = fte(ta);
    formes.tara = fte(ta + 'ら');
    formes.te_iru = fte(te + 'いる');

    // Causatif court (書かす) et causatif-passif court (書かされる) : courants à l'oral,
    // mais évités pour les verbes en す (話さされる).
    ajouter(variantes, 'causatif', f(r[0] + 'す'), 'forme courte, familière');
    if (fin !== 'す') ajouter(variantes, 'causatif_passif', f(r[0] + 'される'), 'forme courte, la plus courante à l\'oral');

    if (classe === 'v5r-i') {
      // ある : la négation est ない tout court.
      var fa = radical(sans(kanji, 2), sans(kana, 2));
      formes.nai = fa('ない');
      formes.nakatta = fa('なかった');
      formes.potentiel = null;
      formes.passif = null;
      formes.causatif = null;
      formes.causatif_passif = null;
      formes.te_iru = null;
      delete variantes.causatif;
      delete variantes.causatif_passif;
    }

    if (classe === 'v5aru') {
      // いらっしゃる, おっしゃる, なさる, くださる, ござる : ます en -います, impératif en -い.
      var fi = function (s) { return f('い' + s); };
      polies(formes, fi);
      formes.tai = f(r[1] + 'たい');
      formes.imperatif = f('い');
      ajouter(variantes, 'masu', f(r[1] + 'ます'), 'forme régulière en -ります, vieillie');
      formes.potentiel = null;
      formes.passif = null;
      formes.causatif = null;
      formes.causatif_passif = null;
      delete variantes.causatif;
      delete variantes.causatif_passif;
      if (finit(kana, 'ござる')) {
        // ござる ne vit plus qu'à travers ございます.
        formes.imperatif = null;
        formes.tai = null;
        formes.te_iru = null;
        formes.volitif = null;
      }
    }
    return ren;
  }

  function ichidan(kanji, kana, classe, formes, variantes) {
    var f = radical(sans(kanji, 1), sans(kana, 1));
    formes.dictionnaire = f('る');
    polies(formes, f);
    formes.te = f('て');
    formes.ta = f('た');
    formes.nai = f('ない');
    formes.nakatta = f('なかった');
    formes.potentiel = f('られる');
    formes.potentiel_familier = f('れる');
    formes.passif = f('られる');
    formes.causatif = f('させる');
    formes.causatif_passif = f('させられる');
    formes.volitif = f('よう');
    formes.imperatif = f('ろ');
    formes.ba = f('れば');
    formes.tara = f('たら');
    formes.te_iru = f('ている');
    if (classe === 'v1-s') {
      // くれる : impératif くれ ; くれれる n'est pas en usage.
      formes.imperatif = f('');
      formes.potentiel_familier = null;
    } else {
      ajouter(variantes, 'imperatif', f('よ'), 'forme écrite');
    }
  }

  function kuru(kanji, kana, formes, variantes) {
    var pk = sans(kana, 2);
    var kj;
    if (finit(kanji, '来る') || finit(kanji, '來る')) kj = sans(kanji, 1);
    else if (finit(kanji, 'くる')) kj = null;
    else return 'le kanji de vk doit finir par 来る';
    // f(fin, mora) : le kanji garde 来, la lecture prend こ / き / く.
    var f = function (fin, mora) {
      var kn = pk + mora + fin;
      return { kanji: kj === null ? sans(kanji, 2) + mora + fin : kj + fin, kana: kn };
    };
    formes.dictionnaire = f('る', 'く');
    polies(formes, function (s) { return f(s, 'き'); });
    formes.te = f('て', 'き');
    formes.ta = f('た', 'き');
    formes.nai = f('ない', 'こ');
    formes.nakatta = f('なかった', 'こ');
    formes.potentiel = f('られる', 'こ');
    formes.potentiel_familier = f('れる', 'こ');
    formes.passif = f('られる', 'こ');
    formes.causatif = f('させる', 'こ');
    formes.causatif_passif = f('させられる', 'こ');
    formes.volitif = f('よう', 'こ');
    formes.imperatif = f('い', 'こ');
    formes.ba = f('れば', 'く');
    formes.tara = f('たら', 'き');
    formes.te_iru = f('ている', 'き');
    return null;
  }

  function suru(kanji, kana, classe, formes, variantes) {
    // Préfixe : 勉強 dans 勉強する. « vs » donne le nom seul, sans する.
    var pkj, pkn;
    if (classe === 'vs') {
      pkj = kanji; pkn = kana;
    } else {
      if (!finit(kana, 'する')) return 'la lecture d\'un verbe ' + classe + ' doit finir par する';
      pkn = sans(kana, 2);
      if (finit(kanji, 'する') || finit(kanji, '為る')) pkj = sans(kanji, 2);
      else return 'le kanji d\'un verbe ' + classe + ' doit finir par する';
    }
    var f = radical(pkj, pkn);
    formes.dictionnaire = f('する');
    polies(formes, function (s) { return f('し' + s); });
    formes.te = f('して');
    formes.ta = f('した');
    formes.nai = f('しない');
    formes.nakatta = f('しなかった');
    formes.potentiel = f('できる');
    formes.passif = f('される');
    formes.causatif = f('させる');
    formes.causatif_passif = f('させられる');
    formes.volitif = f('しよう');
    formes.imperatif = f('しろ');
    formes.ba = f('すれば');
    formes.tara = f('したら');
    formes.te_iru = f('している');
    ajouter(variantes, 'imperatif', f('せよ'), 'forme écrite');
    if (pkn === '') {
      // する seul : son potentiel est できる, un autre verbe. On le donne quand même,
      // c'est ce qu'un apprenant cherche, mais le kanji de できる n'est pas celui de する.
      formes.potentiel = { kanji: 'できる', kana: 'できる' };
      ajouter(variantes, 'potentiel', { kanji: '出来る', kana: 'できる' }, 'potentiel de する : le verbe できる');
    }
    return null;
  }

  function suruSpecial(kanji, kana, formes, variantes) {
    // 愛する, 察する, 訳する : する collé à un kanji unique, qui glisse vers le godan en す.
    if (!finit(kana, 'する') || !(finit(kanji, 'する') || finit(kanji, '為る'))) {
      return 'un verbe vs-s doit finir par する';
    }
    var f = radical(sans(kanji, 2), sans(kana, 2));
    formes.dictionnaire = f('する');
    polies(formes, function (s) { return f('し' + s); });
    formes.te = f('して');
    formes.ta = f('した');
    formes.nai = f('さない');
    formes.nakatta = f('さなかった');
    formes.potentiel = f('せる');
    formes.passif = f('される');
    formes.causatif = f('させる');
    formes.causatif_passif = f('させられる');
    formes.volitif = f('そう');
    formes.imperatif = f('せよ');
    formes.ba = f('すれば');
    formes.tara = f('したら');
    formes.te_iru = f('している');
    ajouter(variantes, 'nai', f('しない'), 'forme classique (サ変), la plus courante pour certains verbes comme 察する');
    ajouter(variantes, 'nakatta', f('しなかった'), 'forme classique (サ変)');
    ajouter(variantes, 'potentiel', f('し得る'), 'forme écrite');
    ajouter(variantes, 'volitif', f('しよう'), 'forme classique (サ変)');
    ajouter(variantes, 'imperatif', f('しろ'), 'forme orale');
    ajouter(variantes, 'ba', f('せば'), 'forme alignée sur le godan');
    return null;
  }

  function zuru(kanji, kana, formes, variantes) {
    // 信ずる, 感ずる : se conjuguent aujourd'hui comme 信じる (ichidan), sauf le dictionnaire et ば.
    if (!finit(kana, 'ずる') || !finit(kanji, 'ずる')) return 'un verbe vz doit finir par ずる';
    var f = radical(sans(kanji, 2), sans(kana, 2));
    ichidan(sans(kanji, 2) + 'じる', sans(kana, 2) + 'じる', 'v1', formes, {});
    formes.dictionnaire = f('ずる');
    formes.ba = f('ずれば');
    ajouter(variantes, 'dictionnaire', f('じる'), 'forme moderne en -じる');
    ajouter(variantes, 'nai', f('ぜない'), 'forme classique');
    ajouter(variantes, 'passif', f('ぜられる'), 'forme classique');
    ajouter(variantes, 'causatif', f('ぜさせる'), 'forme classique');
    ajouter(variantes, 'imperatif', f('ぜよ'), 'forme écrite');
    ajouter(variantes, 'ba', f('じれば'), 'forme moderne en -じる');
    return null;
  }

  // ---------------------------------------------------------------- adjectifs

  function adjectifI(kanji, kana, classe, formes, variantes) {
    if (!finit(kana, 'い') || !finit(kanji, 'い')) return 'un adjectif en い doit finir par い';
    var f, base = radical(sans(kanji, 1), sans(kana, 1));
    if (classe === 'adj-ix') {
      // いい : toutes les formes fléchies reviennent à よい (よかった, よくない).
      if (!finit(kana, 'いい')) return 'un adjectif adj-ix doit se lire en いい';
      var kj = finit(kanji, 'いい') ? sans(kanji, 2) + 'よ' : sans(kanji, 1);
      f = radical(kj, sans(kana, 2) + 'よ');
    } else {
      f = base;
    }
    formes.present = base('い');
    formes.attributif = base('い');
    formes.poli = base('いです');
    formes.negatif = f('くない');
    formes.passe = f('かった');
    formes.passe_negatif = f('くなかった');
    formes.adverbe = f('く');
    formes.te = f('くて');
    formes.ba = f('ければ');
    formes.poli_negatif = f('くないです');
    formes.poli_passe = f('かったです');
    ajouter(variantes, 'poli_negatif', f('くありません'), 'forme plus soutenue');
    return null;
  }

  function adjectifNa(kanji, kana, formes, variantes) {
    var f = radical(kanji, kana);
    formes.present = f('だ');
    formes.attributif = f('な');
    formes.poli = f('です');
    formes.negatif = f('ではない');
    formes.passe = f('だった');
    formes.passe_negatif = f('ではなかった');
    formes.adverbe = f('に');
    formes.te = f('で');
    formes.ba = f('ならば');
    formes.poli_negatif = f('ではありません');
    formes.poli_passe = f('でした');
    ajouter(variantes, 'negatif', f('じゃない'), 'forme orale');
    ajouter(variantes, 'passe_negatif', f('じゃなかった'), 'forme orale');
    ajouter(variantes, 'ba', f('なら'), 'forme courante');
    ajouter(variantes, 'poli_negatif', f('じゃありません'), 'forme orale');
    return null;
  }

  // ---------------------------------------------------------------- entrée

  function verifier(kanji, kana, classe) {
    if (typeof kana !== 'string' || kana === '') return 'lecture en kana absente';
    if (kanji !== null && kanji !== undefined && typeof kanji !== 'string') return 'kanji invalide';
    if (typeof classe !== 'string') return 'classe absente';
    if (CLASSES_VERBES.indexOf(classe) < 0 && CLASSES_ADJECTIFS.indexOf(classe) < 0) {
      return 'classe non gérée : ' + classe;
    }
    return null;
  }

  function calculer(kanji, kana, classe) {
    var err = verifier(kanji, kana, classe);
    if (err) return { erreur: err };
    if (!kanji) kanji = kana;
    var adjectif = CLASSES_ADJECTIFS.indexOf(classe) >= 0;
    var formes = vide(adjectif ? FORMES_ADJECTIF : FORMES_VERBE);
    var variantes = {};

    if (GODAN[classe]) {
      var fin = GODAN[classe];
      if (!finit(kana, fin) || !finit(kanji, fin)) {
        return { erreur: 'un verbe ' + classe + ' doit finir par ' + fin };
      }
      if (classe === 'v5k-s' && !(finit(kana, 'いく') || finit(kana, 'ゆく'))) {
        return { erreur: 'un verbe v5k-s se lit en いく ou ゆく' };
      }
      godan(kanji, kana, classe, formes, variantes);
    } else if (classe === 'v1' || classe === 'v1-s') {
      if (!finit(kana, 'る') || !finit(kanji, 'る')) return { erreur: 'un verbe ichidan doit finir par る' };
      ichidan(kanji, kana, classe, formes, variantes);
    } else if (classe === 'vk') {
      if (!finit(kana, 'くる')) return { erreur: 'un verbe vk se lit en くる' };
      err = kuru(kanji, kana, formes, variantes);
    } else if (classe === 'vs' || classe === 'vs-i') {
      err = suru(kanji, kana, classe, formes, variantes);
    } else if (classe === 'vs-s') {
      err = suruSpecial(kanji, kana, formes, variantes);
    } else if (classe === 'vz') {
      err = zuru(kanji, kana, formes, variantes);
    } else if (classe === 'adj-i' || classe === 'adj-ix') {
      err = adjectifI(kanji, kana, classe, formes, variantes);
    } else if (classe === 'adj-na') {
      err = adjectifNa(kanji, kana, formes, variantes);
    }
    if (err) return { erreur: err };

    if (!adjectif && SANS_POTENTIEL[kana]) {
      formes.potentiel = null;
      formes.potentiel_familier = null;
      delete variantes.potentiel;
    }
    return {
      kanji: kanji,
      kana: kana,
      classe: classe,
      nature: adjectif ? 'adjectif' : 'verbe',
      formes: formes,
      variantes: variantes
    };
  }

  /** Conjugue un mot. Rend null si la classe n'est pas gérée ou l'entrée incohérente. */
  function conjuguer(kanji, kana, classe) {
    var r = calculer(kanji, kana, classe);
    return r.erreur ? null : r;
  }

  /** Pourquoi conjuguer() rend null pour cette entrée ; null si tout va bien. */
  function erreur(kanji, kana, classe) {
    return calculer(kanji, kana, classe).erreur || null;
  }

  /** Une seule forme : { kanji, kana } ou null. */
  function forme(kanji, kana, classe, nom) {
    var r = conjuguer(kanji, kana, classe);
    if (!r || !(nom in r.formes)) return null;
    return r.formes[nom];
  }

  function classeGeree(classe) {
    return CLASSES_VERBES.indexOf(classe) >= 0 || CLASSES_ADJECTIFS.indexOf(classe) >= 0;
  }

  return {
    conjuguer: conjuguer,
    forme: forme,
    erreur: erreur,
    classeGeree: classeGeree,
    CLASSES_VERBES: CLASSES_VERBES.slice(),
    CLASSES_ADJECTIFS: CLASSES_ADJECTIFS.slice(),
    FORMES_VERBE: FORMES_VERBE.slice(),
    FORMES_ADJECTIF: FORMES_ADJECTIF.slice()
  };
})();

if (typeof module !== 'undefined' && module.exports) module.exports = Conjugaison;
