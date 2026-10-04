# Conjugaison japonaise

`conjugaison.js` fabrique les formes des verbes et des adjectifs japonais à partir de
trois données : le mot en kanji, sa lecture en kana et sa **classe JMdict**. Chaque
forme sort en kanji **et** en kana. Il n'y a donc plus besoin de stocker ces formes
écrites à la main.

JavaScript pur, sans dépendance, sans module ni bundler : le fichier se colle tel quel
dans un `<script>` d'`index.html` et définit un seul objet global, `Conjugaison`
(sous node, `require('./conjugaison.js')`).

```
node japonais/conjugaison/tests.js
```

## Exemple

```js
var r = Conjugaison.conjuguer('帰る', 'かえる', 'v5r');
r.formes.te          // { kanji: '帰って', kana: 'かえって' }
r.formes.nai         // { kanji: '帰らない', kana: 'かえらない' }
r.formes.potentiel_familier  // null : n'existe que pour les ichidan et 来る

Conjugaison.forme('来る', 'くる', 'vk', 'nai')        // { kanji: '来ない', kana: 'こない' }
Conjugaison.forme(null, 'しゃべる', 'v5r', 'masu')    // mot sans kanji : le champ kanji reprend le kana
Conjugaison.conjuguer('静か', 'しずか', 'adj-na').variantes.negatif
  // [{ kanji: '静かじゃない', kana: 'しずかじゃない', note: 'forme orale' }]

Conjugaison.conjuguer('有る', 'ある', 'v4r')   // null : classe non gérée
Conjugaison.erreur('有る', 'ある', 'v4r')      // 'classe non gérée : v4r'
Conjugaison.conjuguer('書く', 'かく', 'v5r')   // null : la lecture ne finit pas comme la classe l'annonce
```

Interface : `conjuguer(kanji, kana, classe)`, `forme(kanji, kana, classe, nomDeForme)`,
`erreur(...)`, `classeGeree(classe)`, et les listes `CLASSES_VERBES`, `CLASSES_ADJECTIFS`,
`FORMES_VERBE`, `FORMES_ADJECTIF` (dans l'ordre d'affichage). Les fonctions sont pures.

`conjuguer` rend `{ kanji, kana, classe, nature, formes, variantes }`. Toutes les clés de
`formes` sont toujours présentes ; une forme qui n'existe pas ou n'a pas de sens vaut
`null`, rien n'est inventé. `variantes` garde les formes concurrentes, chacune avec une
note (forme orale, écrite, familière…).

## Formes

**Verbes** : `dictionnaire` ; poli `masu`, `masen`, `mashita`, `masen_deshita`, `mashou` ;
`te`, `ta`, `nai`, `nakatta` ; `potentiel` (et `potentiel_familier`) ; `passif`,
`causatif`, `causatif_passif` ; `volitif`, `imperatif`, `ba`, `tara`, `tai`, `te_iru`.

**Adjectifs** (en い et en な) : `present`, `negatif`, `passe`, `passe_negatif`,
`adverbe` (〜く / 〜に), `te` (〜くて / 〜で), `ba`, `poli`, `poli_negatif`, `poli_passe`,
`attributif` (高い / 静かな) et `imperatif`, toujours `null`.

Choix de la forme principale quand plusieurs coexistent (l'autre va dans `variantes`) :
potentiel ichidan en られる (la forme familière れる dans `potentiel_familier`) ; causatif
long 書かせる (court 書かす en variante) ; causatif-passif long 書かせられる (court
書かされる en variante, sauf pour les verbes en す) ; impératif ichidan en ろ (よ en
variante) ; adjectif en な : ではない (じゃない en variante), ならば (なら en variante).

## Classes

Gérées : `v1`, `v1-s`, `v5u`, `v5k`, `v5g`, `v5s`, `v5t`, `v5n`, `v5b`, `v5m`, `v5r`,
`v5k-s`, `v5r-i`, `v5u-s`, `v5aru`, `vk`, `vs` (nom + する : 料理 → 料理する), `vs-i`,
`vs-s`, `vz`, `adj-i`, `adj-ix`, `adj-na`.

**C'est la classe qui décide, jamais la terminaison** : 帰る, 入る, 走る, 知る, 切る, 要る,
喋る sont `v5r` et se conjuguent en godan (帰って, 切らない) ; 変える, 着る sont `v1`.

Non gérées (renvoient `null`, `erreur()` dit pourquoi) — ce sont celles que JMdict
marque dans ses entrées courantes : `adj-t` (形容動詞 en たる : 確固), `aux-adj` et
`aux-v` (auxiliaires : らしい, 欲しい, ～ている comme entrée à part), `vs-c` (愛す, 託す,
ancêtres en す de する), `vn` (死ぬ archaïque en ぬ irrégulier), `vr` (たり, り),
`v-unspec` ; et en dehors de l'échantillon courant, les classes classiques `v2*`, `v4*`,
`v5uru`, `adj-ku`, `adj-shiku`, `adj-nari`. Pour 死ぬ, 愛す, いらっしゃる…, utiliser
l'autre classe que JMdict leur donne aussi (`v5n`, `v5s`, `v5aru`).

## Exceptions traitées

- **する** et les verbes en する (`vs-i`, `vs`) : します, して, できる (potentiel), される,
  させる, しろ (せよ en variante), すれば.
- **来る** (`vk`) et ses composés (持って来る, やってくる) : le kanji 来 reste, la lecture
  change — 来ない / こない, 来ます / きます, 来い / こい, 来れば / くれば ; こられる, et
  これる en forme familière.
- **行く** (`v5k-s`) et ses composés : 行って, 行った, 行ったら. Lu ゆく : 行って / いって.
- **ある** (`v5r-i`) et ses composés (である, 事がある) : ない, なかった — sans kanji,
  quelle que soit la graphie. Potentiel, passif, causatif et ～ている : `null`.
- **いい / よい** (`adj-ix`) et composés (かっこいい, どうでもいい, 方がいい) : présent いい,
  tout le reste sur よ — よかった, よくない, よければ.
- **問う, 請う, 乞う** (`v5u-s`) : て en うて (問うて, 問うた, 問うたら).
- **いらっしゃる, おっしゃる, なさる, くださる, ござる** (`v5aru`) : ます en います
  (いらっしゃいます, ございます), impératif en い (いらっしゃい, おっしゃい, なさい,
  ください). たい garde 〜りたい (なさりたい). Potentiel, passif, causatif : `null`.
  ござる n'a que ses formes polies et passées : impératif, たい, ている, volitif `null`.
- **くれる** (`v1-s`) : impératif くれ.
- **〜ずる** (`vz` : 信ずる, 感ずる) : conjugué comme 信じる, sauf la forme du dictionnaire
  et 信ずれば ; formes classiques en ぜ (信ぜよ, 信ぜられる) en variantes.
- **〜する à un kanji** (`vs-s` : 愛する, 察する) : formes godan pour la négation, le
  potentiel et le volitif (愛さない, 愛せる, 愛そう), formes サ変 en variantes
  (察しない, 察しよう) — voir les limites.
- **Potentiel sans objet** : わかる et できる n'ont pas de potentiel (`null`).

## D'où viennent les réponses des tests

Aucune réponse attendue ne vient de `conjugaison.js` lui-même : le script qui les fabrique
ne l'importe pas. Les oracles ne servent **que** dans `oracles/`, jamais dans le générateur.

| Source | Licence | Rôle |
|---|---|---|
| [kamiya-codec](https://github.com/fasiha/kamiya-codec) 4.16.1 | Unlicense (domaine public) | conjugueur JS d'après les *Handbooks* de Taeko Kamiya |
| [japanese-verb-conjugator-v2](https://pypi.org/project/japanese-verb-conjugator-v2/) 1.0.1 | BSD | conjugueur Python (verbes) |
| UniDic (`unidic-lite` 1.0.8) via `fugashi` | BSD / MIT | analyseur morphologique : juge des cas tranchés à la main |
| [JMdict](https://www.edrdg.org/jmdict/j_jmdict.html) (EDRDG), via `jamdict-data` 1.5 | **CC BY-SA 4.0** | liste des mots courants et de leur classe |

Le Wiktionnaire n'était pas joignable depuis l'environnement de travail : il n'a pas servi.

`tests.js` vérifie **2 706 cas attendus** sur 70 mots de toutes les classes et toutes les
exceptions, chacun en kanji et en kana (`oracles/attendus.json`, chaque cas porte sa
source) :

- 1 633 où kamiya-codec et japanese-verb-conjugator-v2 donnent la même forme ;
- 510 donnés par kamiya-codec seul (たい, ている, causatif-passif, adjectifs…) ;
- 27 par japanese-verb-conjugator-v2 seul ;
- 536 **décisions** : les cas où les deux conjugueurs se taisent, se contredisent ou se
  trompent. Chacune est écrite dans `oracles/fabriquer.py` avec sa justification, et
  l'analyse UniDic de la réponse est enregistrée avec le cas. Les erreurs d'oracles ainsi
  écartées : 問うて (les deux donnent 問って), 有る → ない (les deux donnent 有らない),
  impératif et ます des honorifiques, potentiel de ある (あれる), composés de 行く et de
  いい, いらっしゃる + ば, くれる → くれ ; et les classes `vs-s` et `vz`, qu'aucun des deux
  ne connaît, entièrement établies ainsi.

S'ajoutent 34 vérifications du contrat de l'interface, puis l'**échantillon large** :
les 7 754 entrées verbales et adjectivales courantes de JMdict (graphie et lecture marquées
news1, ichi1, spec1/2 ou gai1 ; `oracles/jmdict-courants.json`). Les 7 657 de classes gérées
sont toutes conjuguées sans plantage ni refus, et chacune de leurs 144 489 formes est soit
non vide (et sans kanji dans la lecture), soit `null` pour une raison prévue.

Avec `kamiya-codec` installé (`NODE_PATH=…/node_modules node tests.js`), le test compare
aussi tout l'échantillon v1 et godan régulier à kamiya sur 7 formes : 11 823 accords sur
11 844. Les 21 écarts sont 繰る, 刷る, 擦る : kamiya, qui ne reçoit que le kana, les prend
pour くる et する. C'est précisément le cas où la classe doit décider.

Un balayage UniDic des formes de l'échantillon (hors `vs`) n'a montré que des homographes
(育てる est aussi un autre verbe), pas d'erreur de flexion.

Pour refaire les oracles, voir l'en-tête de `oracles/fabriquer.py`, `oracles/kamiya.js` et
`oracles/extraire_jmdict.py` (les paquets s'installent hors du dépôt).

## Limites connues

- **`vs-s` est douteux par nature** : la classe mêle des verbes qui ont glissé vers le
  godan (愛さない, 愛せる) et d'autres restés en サ変 (察しない, 熱しよう). Une seule règle
  par classe ne peut pas avoir raison pour tous ; la forme principale suit le godan, l'autre
  est en variante. À relire mot par mot si ces verbes entrent dans l'app.
- **Potentiel et sens** : le générateur ne sait pas qu'un verbe intransitif comme 育つ,
  並ぶ a un potentiel qui se confond avec un autre verbe (育てる, 並べる), ni qu'un verbe
  non volontaire (降る, 要る) n'a guère de potentiel. Seuls ある, わかる et できる sont
  traités.
- **Forme en ている** : donnée pour tous les verbes sauf ある et ござる, sans juger si elle
  exprime une action en cours ou un état.
- **ゆく** : 行って est lu いって ; la variante ゆって n'est pas donnée.
- **Adjectifs en ない** (少ない, つまらない…) : conjugués mécaniquement (少なくない),
  ce qui est juste mais peut surprendre pour ceux qui sont déjà une négation (下らない →
  下らなくない).
- Le kanji de する seul (為る) est rendu en kana dans toutes les formes.
- JMdict vient de la copie 2021 de `jamdict-data` : des classes ont pu être corrigées depuis.
