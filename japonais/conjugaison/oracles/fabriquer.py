# -*- coding: utf-8 -*-
"""
Fabrique oracles/attendus.json : les réponses attendues des tests, prises dans des
sources INDÉPENDANTES de conjugaison.js (qui n'est jamais importé ici).

Sources :
  1. kamiya-codec 4.16.1 (Unlicense)      -> oracles/kamiya.json, fait par oracles/kamiya.js
  2. japanese-verb-conjugator-v2 1.0.1 (BSD) — https://pypi.org/project/japanese-verb-conjugator-v2/
     (verbes seulement ; ses règles suivent conjugator.reverso.net)
  3. UniDic (unidic-lite 1.0.8, BSD) lu par fugashi (MIT) : analyseur morphologique fondé
     sur un corpus. Il ne conjugue pas : il vérifie qu'une forme proposée existe et se
     ramène au bon lemme, avec quelle forme de flexion (活用形). Il sert de juge pour
     chaque décision manuelle ci-dessous.

Règle : quand les deux conjugueurs donnent la même forme, c'est la réponse attendue.
Quand un seul en donne une, on la prend. Quand ils se contredisent, se taisent, ou
donnent une forme qu'on refuse (potentiel de ある…), la réponse vient de DECISIONS,
avec sa justification, et UniDic l'analyse ; l'analyse est enregistrée avec le cas.

  python3 -m venv v && v/bin/pip install japanese-verb-conjugator-v2==1.0.1 fugashi unidic-lite
  v/bin/python oracles/fabriquer.py          (depuis japonais/conjugaison/)
"""
import io
import json
import os
import sys

from japanese_verb_conjugator_v2 import (BaseForm, Formality, JapaneseVerbFormGenerator as G,
                                          Polarity, Tense, VerbClass)
import fugashi

ICI = os.path.dirname(os.path.abspath(__file__))
P, F, T = Polarity, Formality, Tense

FORMES_VERBE = ['dictionnaire', 'masu', 'masen', 'mashita', 'masen_deshita', 'mashou',
                'te', 'ta', 'nai', 'nakatta', 'potentiel', 'potentiel_familier', 'passif', 'causatif',
                'causatif_passif', 'volitif', 'imperatif', 'ba', 'tara', 'tai', 'te_iru']
FORMES_ADJ = ['present', 'negatif', 'passe', 'passe_negatif', 'adverbe', 'te', 'ba',
              'poli', 'poli_negatif', 'poli_passe', 'attributif', 'imperatif']

# --------------------------------------------------------------- oracle n°2

def jvc(mot, classe):
    if classe.startswith('adj') or classe in ('vs-s', 'vz'):
        return {}
    vc = {'v1': VerbClass.ICHIDAN, 'v1-s': VerbClass.ICHIDAN, 'vk': VerbClass.IRREGULAR,
          'vs': VerbClass.IRREGULAR, 'vs-i': VerbClass.IRREGULAR}.get(classe, VerbClass.GODAN)
    if classe == 'vs':
        mot = mot + 'する'
    appels = {
        'dictionnaire': (G.generate_plain_form, dict(tense=T.NONPAST, polarity=P.POSITIVE)),
        'nai': (G.generate_plain_form, dict(tense=T.NONPAST, polarity=P.NEGATIVE)),
        'nakatta': (G.generate_plain_form, dict(tense=T.PAST, polarity=P.NEGATIVE)),
        'masu': (G.generate_polite_form, dict(tense=T.NONPAST, polarity=P.POSITIVE)),
        'masen': (G.generate_polite_form, dict(tense=T.NONPAST, polarity=P.NEGATIVE)),
        'mashita': (G.generate_polite_form, dict(tense=T.PAST, polarity=P.POSITIVE)),
        'masen_deshita': (G.generate_polite_form, dict(tense=T.PAST, polarity=P.NEGATIVE)),
        'mashou': (G.generate_volitional_form, dict(formality=F.POLITE, polarity=P.POSITIVE)),
        'te': (G.generate_te_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'ta': (G.generate_ta_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'tara': (G.generate_tara_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'potentiel': (G.generate_potential_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'volitif': (G.generate_volitional_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'imperatif': (G.generate_imperative_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'ba': (G.generate_provisional_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'causatif': (G.generate_causative_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
        'passif': (G.generate_passive_form, dict(formality=F.PLAIN, polarity=P.POSITIVE)),
    }
    r = {}
    for forme, (fn, kw) in appels.items():
        try:
            r[forme] = [fn(mot, vc, **kw)]
        except Exception:
            r[forme] = []
    return r

# --------------------------------------------------------------- choix d'une variante

def filtre(forme, classe):
    """Quand un oracle propose plusieurs formes, laquelle est « la » forme de cette clé."""
    ichi = classe in ('v1', 'v1-s', 'vk')
    na = classe == 'adj-na'
    fins = {
        'masen': 'ません', 'masen_deshita': 'ませんでした', 'volitif': 'う', 'ba': 'ば',
        'mashou': 'ましょう',
    }
    if forme == 'te_iru':
        return lambda s: s.endswith('ている') or s.endswith('でいる')
    if forme in fins:
        return lambda s: s.endswith(fins[forme])
    if forme == 'potentiel' and ichi:
        return lambda s: s.endswith('られる')
    if forme == 'potentiel_familier':
        return lambda s: ichi and not s.endswith('られる')
    if forme == 'imperatif' and classe in ('v1', 'vk'):
        return lambda s: not s.endswith('よ')
    if classe.startswith('adj'):
        if forme == 'te':
            return lambda s: s.endswith('て') or s.endswith('で')
        if forme == 'poli':
            return lambda s: s.endswith('です')
        if forme == 'poli_passe':
            return lambda s: s.endswith('でした')
        if forme == 'poli_negatif':
            return lambda s: s.endswith('ではありません')
        if na:
            na_fins = {'present': 'だ', 'negatif': 'ではない', 'passe': 'だった',
                       'passe_negatif': 'ではなかった'}
            if forme in na_fins:
                return lambda s: s.endswith(na_fins[forme])
        if forme in ('passe', 'passe_negatif'):
            return lambda s: not s.endswith('でした')
    return lambda s: True

# --------------------------------------------------------------- décisions manuelles
# Clé : (kana du mot, classe, forme). Valeur : (attendu kanji, attendu kana, justification).
# Une valeur None/None = la forme n'existe pas ou n'a pas de sens.
# « K » = kamiya-codec, « J » = japanese-verb-conjugator-v2, « U » = UniDic.

NUL = (None, None)
DECISIONS = {}

def decide(kana, classe, formes, kanji_att, kana_att, pourquoi, kanji=None):
    """kanji= : la décision ne vaut que pour cette graphie (請う et 乞う se lisent tous deux こう)."""
    for f in formes.split():
        DECISIONS[(kanji, kana, classe, f)] = (kanji_att, kana_att, pourquoi)

# --- Ce que les oracles ne couvrent pas : forme courte du potentiel ichidan nulle ailleurs.
GODAN = ['v5u', 'v5k', 'v5g', 'v5s', 'v5t', 'v5n', 'v5b', 'v5m', 'v5r', 'v5k-s', 'v5r-i', 'v5u-s', 'v5aru']

# --- ある (v5r-i)
decide('ある', 'v5r-i', 'potentiel', None, None,
       'K et J donnent あれる ; or あれる n\'est pas un potentiel en usage (U l\'analyse comme impératif あれ + る). ある n\'a pas de potentiel.')
decide('ある', 'v5r-i', 'passif causatif causatif_passif', None, None,
       'K donne れる/せる/せられる (défaut : radical vide), J donne あられる/あらせる ; formes sans emploi courant pour ある (あらせられる est un honorifique figé), on rend null.')
decide('ある', 'v5r-i', 'nai', 'ない', 'ない',
       'K et J donnent ない en kana mais 有らない pour la graphie 有る (ils appliquent la règle godan au kanji) ; la négation de ある est ない, sans kanji, quelle que soit la graphie : c\'est la raison d\'être de la classe v5r-i.')
decide('ある', 'v5r-i', 'nakatta', 'なかった', 'なかった', 'idem pour le passé négatif.')
decide('ある', 'v5r-i', 'te_iru', None, None,
       'K donne あっている : ある exprime déjà un état, ～ている n\'a pas de sens ici.')
# --- 問う / 請う / 乞う (v5u-s) : て en うて
for kn, kj in (('とう', '問'), ('こう', '請'), ('こう', '乞')):
    pre = kn[:-1]
    m = kj + 'う'
    decide(kn, 'v5u-s', 'te', kj + 'うて', pre + 'うて', 'K et J donnent 〜って (règle générale des verbes en う) ; JMdict classe ces verbes v5u-s justement pour la forme en うて ; U analyse 〜うて = 連用形-ウ音便.', m)
    decide(kn, 'v5u-s', 'ta', kj + 'うた', pre + 'うた', 'idem, た en うた (U : 連用形-ウ音便 + た).', m)
    decide(kn, 'v5u-s', 'tara', kj + 'うたら', pre + 'うたら', 'idem, たら en うたら.', m)
    decide(kn, 'v5u-s', 'te_iru', kj + 'うている', pre + 'うている', 'idem, ている sur うて.', m)
# --- honorifiques v5aru
HONO = [('いらっしゃる', 'いらっしゃる'), ('おっしゃる', '仰る'), ('なさる', '為さる'), ('くださる', '下さる'), ('ござる', '御座る')]
for kn, kj in HONO:
    s_kn, s_kj = kn[:-1], kj[:-1]
    if kn != 'ござる':
        decide(kn, 'v5aru', 'imperatif', s_kj + 'い', s_kn + 'い',
               'J donne 〜い, K donne 〜れ sauf pour いらっしゃる ; l\'impératif de la classe v5aru est en い (いらっしゃい, おっしゃい, なさい, ください) ; U : 命令形.')
    for f, fin in (('masu', 'ます'), ('masen', 'ません'), ('mashita', 'ました'),
                   ('masen_deshita', 'ませんでした'), ('mashou', 'ましょう')):
        decide(kn, 'v5aru', f, s_kj + 'い' + fin, s_kn + 'い' + fin,
               'J donne 〜います, K seulement pour ござる/いらっしゃる (en kana) ; la classe v5aru est définie par ce ます en います ; U : 連用形-イ音便 + ます.')
    decide(kn, 'v5aru', 'potentiel passif causatif causatif_passif', None, None,
           'K et J appliquent la règle godan (いらっしゃれる, 仰られる…) ; un verbe honorifique n\'a pas de potentiel, de passif ni de causatif d\'usage : null.')
for kn, kj in HONO[:4]:
    decide(kn, 'v5aru', 'tai', kj[:-1] + 'りたい', kn[:-1] + 'りたい',
           'K donne 〜いたい (son cas particulier du 連用形 en い déborde sur たい), J n\'a pas たい. Le 連用形 en い est une イ音便 réservée à ます et à l\'impératif ; devant たい on garde 〜り (なさりたい) : U analyse 〜り = 連用形-一般, et くださいたい comme impératif + たい.')
decide('ござる', 'v5aru', 'imperatif tai te_iru volitif', None, None,
       'ござる ne vit plus que dans ございます ; ces formes n\'ont pas d\'emploi : null.')
# --- する seul : potentiel できる, en kana
decide('する', 'vs-i', 'potentiel', 'できる', 'できる',
       'Le potentiel de する est le verbe できる ; K donne できる ; J donne 出来る. On garde l\'écriture en kana, recommandée (公用文) et la plus fréquente.')
for kn, kj in (('べんきょうする', '勉強'), ('うんどうする', '運動'), ('りょうり', '料理')):
    pre = kn[:-2] if kn.endswith('する') else kn
    decide(kn, 'vs-i' if kn.endswith('する') else 'vs', 'potentiel', kj + 'できる', pre + 'できる',
           'Potentiel en できる : K donne 〜できる, J 〜出来る ; même choix d\'écriture que pour する.')
# --- 来る : forme familière du potentiel (ら抜き)
decide('くる', 'vk', 'potentiel_familier', '来れる', 'これる', 'K donne 来れる (sa seule forme de potentiel), J ne la donne pas ; lecture これる, U : 来 未然形 + れる.')
decide('もってくる', 'vk', 'potentiel_familier', '持って来れる', 'もってこれる', 'idem pour le composé.')
# --- impératif de くれる (v1-s)
decide('くれる', 'v1-s', 'imperatif', '呉れ', 'くれ', 'v1-s n\'existe que pour くれる, dont l\'impératif est くれ (K et J donnent くれろ, règle ichidan) ; U : 命令形.')
# --- vs-s : aucun conjugueur ne gère la classe, tout vient d'UniDic
for kn, kj in (('あいする', '愛'), ('さっする', '察')):
    p = kn[:-2]
    for f, fin, why in (
        ('dictionnaire', 'する', 'forme du dictionnaire'),
        ('masu', 'します', 'U : 連用形 し + ます'), ('masen', 'しません', 'U'), ('mashita', 'しました', 'U'),
        ('masen_deshita', 'しませんでした', 'U'), ('mashou', 'しましょう', 'U'),
        ('te', 'して', 'U : 連用形 + て'), ('ta', 'した', 'U'), ('tara', 'したら', 'U'), ('tai', 'したい', 'U'),
        ('te_iru', 'している', 'U'),
        ('nai', 'さない', 'forme godan (五段化), la plus courante pour 愛する ; U analyse 愛さ = 五段-サ行 未然形. 察しない est donné en variante.'),
        ('nakatta', 'さなかった', 'idem'),
        ('potentiel', 'せる', 'U : 五段-サ行 仮定形/可能 ; 愛せる est l\'usage courant.'),
        ('passif', 'される', 'U : 未然形 さ + れる'), ('causatif', 'させる', 'U : さ + せる'),
        ('causatif_passif', 'させられる', 'U'), ('volitif', 'そう', 'forme godan, U : 意志推量形'),
        ('imperatif', 'せよ', 'forme écrite de l\'impératif サ変 ; U : 命令形'), ('ba', 'すれば', 'U : 仮定形 すれ + ば'),
    ):
        decide(kn, 'vs-s', f, kj + fin, p + fin, 'vs-s (aucun oracle conjugueur) : ' + why)
    decide(kn, 'vs-s', 'potentiel_familier', None, None, 'pas de forme familière hors ichidan')
# --- vz : idem, rattaché à 〜じる
for kn, kj in (('しんずる', '信'), ('かんずる', '感')):
    p = kn[:-2]
    for f, fin, why in (
        ('dictionnaire', 'ずる', 'forme du dictionnaire'),
        ('masu', 'じます', 'U : 連用形 じ + ます'), ('masen', 'じません', 'U'), ('mashita', 'じました', 'U'),
        ('masen_deshita', 'じませんでした', 'U'), ('mashou', 'じましょう', 'U'),
        ('te', 'じて', 'U'), ('ta', 'じた', 'U'), ('tara', 'じたら', 'U'), ('tai', 'じたい', 'U'),
        ('te_iru', 'じている', 'U'), ('nai', 'じない', 'U : 未然形 じ + ない'), ('nakatta', 'じなかった', 'U'),
        ('potentiel', 'じられる', 'U'), ('potentiel_familier', 'じれる', 'ら抜き de 〜じる, U'),
        ('passif', 'じられる', 'U'), ('causatif', 'じさせる', 'U'), ('causatif_passif', 'じさせられる', 'U'),
        ('volitif', 'じよう', 'U'), ('imperatif', 'じろ', 'U : 命令形'), ('ba', 'ずれば', 'U : 仮定形 ずれ + ば'),
    ):
        decide(kn, 'vz', f, kj + fin, p + fin, 'vz (aucun oracle conjugueur) : ' + why)
# --- composés de 行く : J ne reconnaît que 行く seul et applique la règle des verbes en く
for f, fin in (('te', 'って'), ('ta', 'った'), ('tara', 'ったら')):
    decide('でていく', 'v5k-s', f, '出て行' + fin, 'でてい' + fin,
           'K (adapté : base 行く + préfixe) donne 〜行' + fin + ' ; J donne 〜行い' + fin[1:] + ', faute de reconnaître le composé. La classe v5k-s couvre justement les composés de 行く ; U analyse 行っ = 連用形-促音便.')
decide('いらっしゃる', 'v5aru', 'ba', 'いらっしゃれば', 'いらっしゃれば',
       'K donne いらっしゃいば (son exception d\'impératif déborde sur ば), J いらっしゃれば ; le ば se forme sur le 仮定形 régulier : U analyse いらっしゃれ = 仮定形.')
decide('くださる', 'v5aru', 'te_iru', '下さっている', 'くださっている',
       'K lève une erreur pour くださる hors forme du dictionnaire, J n\'a pas de ている ; て régulier + いる (« 来てくださっている ») ; U : 連用形-促音便 + て + いる.')
# --- potentiels sans objet
decide('わかる', 'v5r', 'potentiel', None, None, 'K et J donnent 分かれる, qui est un autre verbe (se séparer) : 分かる exprime déjà la capacité.')
decide('できる', 'v1', 'potentiel potentiel_familier', None, None, 'できる est lui-même un potentiel : できられる n\'existe pas.')
# --- adjectifs : formes polies et impératif, absentes de K pour les adjectifs en い
for kn, kj, cl in (('たかい', '高', 'adj-i'), ('あたらしい', '新し', 'adj-i'), ('さむい', '寒', 'adj-i'),
                   ('おおきい', '大き', 'adj-i'), ('すくない', '少な', 'adj-i'), ('よい', '良', 'adj-i'),
                   ('いい', '良', 'adj-ix'), ('かっこいい', '格好', 'adj-ix')):
    p = kn[:-1]
    neg_kj, neg_kn = kj, p
    if cl == 'adj-ix':
        neg_kj = kj if kj == '良' else kj + 'よ'
        neg_kn = kn[:-2] + 'よ'
    pres_kj = kj + 'い' if cl == 'adj-i' else (kj + 'い' if kj == '良' else kj + 'いい')
    decide(kn, cl, 'poli', pres_kj + 'です', kn + 'です', 'K ne donne pas la forme polie ; adjectif + です, U : 形容詞 終止形 + です.')
    decide(kn, cl, 'poli_negatif', neg_kj + 'くないです', neg_kn + 'くないです', 'K ne la donne pas ; négatif + です, U.')
    decide(kn, cl, 'poli_passe', neg_kj + 'かったです', neg_kn + 'かったです', 'K ne la donne pas ; passé + です, U.')
    decide(kn, cl, 'te', neg_kj + 'くて', neg_kn + 'くて', 'K donne 〜く et 〜くて ; la clé « te » est 〜くて (〜く est la clé « adverbe »).')
for f, fin in (('negatif', 'くない'), ('passe', 'かった'), ('passe_negatif', 'くなかった'),
               ('adverbe', 'く'), ('ba', 'ければ')):
    decide('かっこいい', 'adj-ix', f, '格好よ' + fin, 'かっこよ' + fin,
           'K ne reconnaît que いい/良い/よい seuls et traite かっこいい comme régulier (かっこいかった) ; la classe adj-ix couvre les composés de いい, fléchis sur よい ; U analyse 〜よ' + fin + ' comme 良い + flexion, et かっこいかった comme 怒る.')
for cl, mots in (('adj-i', 'たかい'), ('adj-ix', 'いい'), ('adj-na', 'しずか')):
    decide(mots, cl, 'imperatif', None, None, 'un adjectif n\'a pas d\'impératif : null (K n\'en propose pas).')

# --------------------------------------------------------------- UniDic

TAGGER = fugashi.Tagger()

def analyse(s):
    out = []
    for m in TAGGER(s):
        f = m.feature
        out.append('%s[%s %s %s]' % (m.surface, f.lemma, f.cType or '', f.cForm or ''))
    return ' '.join(out)

# --------------------------------------------------------------- assemblage

def main():
    mots = json.load(io.open(os.path.join(ICI, 'mots-tests.json'), encoding='utf-8'))
    kam = json.load(io.open(os.path.join(ICI, 'kamiya.json'), encoding='utf-8'))
    cas, non_resolus = [], []
    for kanji, kana, classe in mots:
        formes = FORMES_ADJ if classe.startswith('adj') else FORMES_VERBE
        k_entree = kam.get('|'.join([kanji, kana, classe]), {})
        for ecriture, mot in (('kanji', kanji), ('kana', kana)):
            j_res = jvc(mot, classe)
            k_res = k_entree.get(ecriture, {})
            for forme in formes:
                ok = filtre(forme, classe)
                K = [x for x in k_res.get(forme, []) if ok(x)]
                J = [x for x in j_res.get(forme, []) if ok(x)]
                d = DECISIONS.get((kanji, kana, classe, forme)) or DECISIONS.get((None, kana, classe, forme))
                if d is None and forme == 'potentiel_familier' and classe == 'v1-s':
                    d = (None, None, 'くれる : くれられる (donné par J) est déjà marginal, sa forme courte くれれる n\'est pas en usage : null.')
                if d is None and forme == 'potentiel_familier' and classe not in ('v1', 'vk'):
                    d = (None, None, 'la forme familière en れる (ら抜き) n\'existe que pour les ichidan et 来る.')
                if d is None and forme == 'imperatif' and classe.startswith('adj'):
                    d = (None, None, 'un adjectif n\'a pas d\'impératif : null.')
                if d is not None:
                    att = d[0] if ecriture == 'kanji' else d[1]
                    source = 'décision : ' + d[2]
                elif K and J:
                    inter = [x for x in K if x in J]
                    if len(inter) != 1:
                        non_resolus.append((kanji, kana, classe, ecriture, forme, K, J)); continue
                    att, source = inter[0], 'kamiya-codec + japanese-verb-conjugator-v2'
                elif K or J:
                    seul = K or J
                    if len(seul) != 1:
                        non_resolus.append((kanji, kana, classe, ecriture, forme, K, J)); continue
                    att, source = seul[0], 'kamiya-codec' if K else 'japanese-verb-conjugator-v2'
                else:
                    non_resolus.append((kanji, kana, classe, ecriture, forme, K, J)); continue
                c = {
                    'kanji': kanji, 'kana': kana, 'classe': classe, 'ecriture': ecriture,
                    'forme': forme, 'attendu': att, 'source': source,
                }
                # Pour garder le fichier lisible : les réponses brutes des oracles et
                # l'analyse UniDic ne sont gardées que pour les cas tranchés à la main.
                if d is not None:
                    c['kamiya'] = k_res.get(forme, [])
                    c['jvc'] = j_res.get(forme, [])
                    c['unidic'] = analyse(att) if att else None
                cas.append(c)
    for n in non_resolus:
        print('NON RÉSOLU', n, file=sys.stderr)
    with io.open(os.path.join(ICI, 'attendus.json'), 'w', encoding='utf-8') as f:
        f.write('[\n' + ',\n'.join(json.dumps(c, ensure_ascii=False) for c in cas) + '\n]\n')
    print('%d cas, %d non résolus' % (len(cas), len(non_resolus)), file=sys.stderr)
    return 1 if non_resolus else 0


if __name__ == '__main__':
    sys.exit(main())
