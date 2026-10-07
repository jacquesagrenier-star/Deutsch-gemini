# Kanji N5 : pilote des mnémotechniques en français

**Statut : brouillon à relire.** Ce dossier sert à juger la méthode sur les kanji du niveau JLPT N5 avant de l'étendre aux quelque 2 000 autres. Aucun texte n'est validé.

> **Droit d'auteur (règle du 7 oct. 2026)** : ne jamais consulter WaniKani, Heisig (*Remembering the Kanji* / *Les kanji dans la tête*), KanjiDamage ni les histoires de Kanji Koohii, et n'en rien reproduire, même traduit. Une mnémotechnique qui ressemble à une de leurs histoires se réécrit. Détails : `LICENCES.md`, section « Mnémoniques ».

## Ce qu'il y a dans le dossier

| Fichier | Rôle |
|---|---|
| `mnemoniques_n5.json` | Une entrée par kanji : sens retenu, lecture retenue et ses comptes, composants, mnémotechniques français et anglais, confiance, exemples. **Généré**, ne pas modifier à la main. |
| `composants.json` | Le lexique des composants KanjiVG : un nom français et un nom anglais par composant, les kanji où il apparaît, ceux où un mnémotechnique le cite. **Généré.** |
| `a-relire.html` | Le lot en cours (20 kanji au plus) à juger, puis l'état des 79 kanji. À ouvrir dans un navigateur et à imprimer. **Généré.** |
| `textes/textes_n5.json` | **Les textes écrits à la main** : sens choisi, mnémotechniques, confiance et sa raison. C'est ici qu'on corrige. |
| `textes/noms_composants.json` | Le nom de chaque composant, avec son `origine` (sens KANJIDIC2 ou nom écrit pour Wortando). Changer un nom ici le change partout. |
| `textes/a_relire.json` | Le titre et les kanji du lot en cours de relecture. |
| `charte-des-sons.md` | La charte des sons : le rendu français fixé pour chaque son japonais difficile. `construire.py` en lit les identifiants. |
| `construire.py` | Refait les trois fichiers générés et vérifie tout. |

Pour reconstruire :

```
python japonais/kanji/construire.py                    # clone KanjiVG dans ~/.cache/kanjivg au besoin
python japonais/kanji/construire.py --kanjivg DOSSIER  # ou une copie locale de KanjiVG
```

Le script n'utilise que la bibliothèque standard de Python. Il s'arrête en erreur (code 1) si un texte ne respecte pas les règles ci-dessous, et n'écrit alors pas la page HTML.

## La méthode

Pour chaque kanji N5 de `japonais/kanji.json` :

1. **Le sens retenu** : un seul mot, choisi à la main **parmi** les sens français de KANJIDIC2 (et un mot anglais parmi les sens anglais). Le script refuse un sens qui n'est pas mot pour mot dans KANJIDIC.
2. **La lecture à retenir** : calculée, pas choisie. Le script prend chaque mot N5 de `japonais/mots.json` qui contient le kanji et **aligne** son écriture sur sa lecture en kana : chaque kanji doit y prendre une de ses lectures KANJIDIC, éventuellement modifiée de façon régulière (sonorisation 日 → び dans 曜日, gémination 学 → がっ dans 学校). La lecture la plus fréquente gagne ; en cas d'égalité, on compte sur tous les niveaux N5 à N1. Le nombre de mots est noté dans `lecture.mots_n5`, et tous les comptes dans `comptes_lecture`.
   - Quand deux découpes sont possibles parce que KANJIDIC donne le même son en on et en kun (気 : キ et き), le script préfère la découpe qui ne change pas de type de lecture dans le mot (元気 : tout en on). Sinon le mot est écarté.
   - Les mots qui ne s'alignent pas (lectures spéciales comme 今日 きょう, 一日 ついたち, お母さん おかあさん) ne votent pas ; ils sont listés dans `mots_n5_non_alignes`.
   - Une dérogation est possible (`lecture_derogation` dans `textes/textes_n5.json`, avec une raison écrite) mais **aucune n'est utilisée** : ce pilote applique la règle telle quelle, pour qu'on voie où elle donne un résultat discutable.
3. **Les composants** : les groupes `kvg:element` de KanjiVG, au premier niveau sous le kanji (`composants`), plus les éléments plus profonds (`sous_composants`). Un kanji sans sous-groupe est son propre composant. `traits_libres` compte les traits que KanjiVG ne range dans aucun élément nommé.
4. **Le mnémotechnique français** : une ou deux phrases qui relient les composants, le sens et le son de la lecture. Le morceau qui porte le son est en **gras**, la lecture en romaji Hepburn est écrite à côté entre parenthèses.
5. **Le mnémotechnique anglais**, écrit séparément, avec un son anglais.
6. **Deux notes** sur le texte **français** seulement, chacune avec sa raison (haute / moyenne / basse) :
   - `confiance` : **le son**. Le morceau en gras fait-il entendre la lecture ?
   - `lien` (depuis le 7 oct.) : **l'image mène-t-elle d'elle-même au sens ?** Le pilote du 4 oct. a montré que la note du son ne suffit pas : trois des quatre refus étaient notés « haute » en son, mais reliaient l'image au sens par un lien arbitraire (des autocollants pour « homme », Djibouti pour « heure », un smash de tennis pour « ciel »).
   - Une mnémotechnique n'est **proposée** que si les deux notes valent au moins « moyenne ».
   - `avis_jacques` garde chaque verdict (`ok` / `refuse`, date, remarque) **avec le texte jugé** (`mnemo_juge`) : un verdict ne vaut que pour ce texte-là, une réécriture repart à juger. `propositions_fr` contient les réécritures en attente de choix.
   - **La charte des sons** (`charte-des-sons.md`, depuis le 7 oct.), sur un principe fixé par Jacques : *un rendu n'est refusé que s'il fait retenir un autre son japonais* (le r et le j français sont donc acceptés ; h, chi, tsu, u et n final restent stricts) : `construire.py` repère dans la lecture les sons difficiles (r, h, tsu, ji, n final, voyelle longue…). Chaque texte et chaque réécriture donne, dans `charte`, un verdict par son : `ok` ou `écart : …`. Un oubli est une erreur ; un écart rend la mnémotechnique **hors charte**, même validée.
   - Le script en tire un `etat` : **validée** (ok sur le texte actuel), **refusée**, **hors charte** (un écart à la charte), **à juger** (les deux notes au moins moyennes), **à réécrire** (une note basse).
7. **La lecture enseignée** (`lecture_enseignee`, depuis le 7 oct.) : chaque texte écrit quelle lecture il enseigne, **on** (sino-japonaise) ou **kun** (japonaise), et le script vérifie que c'est la lecture retenue. Il calcule aussi `lecture_la_plus_utile` : celle que portent le plus de mots JLPT, tous niveaux N5 à N1. Quand ce n'est pas la lecture enseignée, il le signale, avec un écart **net** (au moins deux fois plus de mots, et cinq de plus) ou **faible** (petits comptes, à ne pas surinterpréter).
8. **Une deuxième mnémotechnique** (`autres_lectures`, depuis le 7 oct.) quand la lecture la plus utile n'est pas la lecture enseignée avec un écart net : on garde la lecture enseignée et on ajoute un texte français pour l'autre, avec les mêmes notes, la même charte et ses propres exemples (pris sur tous les niveaux, les formes sans sonorisation d'abord). Les 8 écarts nets en ont une : 中 人 女 小 山 長 食 高.
9. **Deux mots N5 d'exemple** pris dans `mots.json`, avec leur lecture.

Ce que `construire.py` vérifie pour chaque kanji : le sens est un sens KANJIDIC ; chaque mnémotechnique contient le mot du sens et la lecture « (romaji) » exacte ; il a un morceau en gras ; chaque composant cité appartient bien à la décomposition KanjiVG et son nom du lexique figure dans les deux textes ; deux composants n'ont jamais le même nom ; les deux notes sont présentes et valides ; les réécritures de `propositions_fr` suivent les mêmes règles que le texte ; chaque verdict cite le texte jugé ; le lot de relecture compte 1 à 20 kanji. Le romaji est calculé à partir des kana, pas recopié.

## Les chiffres

| | |
|---|---:|
| Kanji N5 dans `kanji.json` | **79** |
| Kanji traités | **79** |
| Confiance haute | 52 |
| Confiance moyenne | 21 |
| Confiance basse | 6 (九, 何, 半, 左, 本, 白) |
| Lien image-sens haute / moyenne / basse (7 oct.) | 41 / 21 / 17 |
| États au 7 oct., après le lot 1 et la charte assouplie : validée / hors charte / à juger / à réécrire | 18 / 8 / 41 / 12 |
| Lecture la plus utile non enseignée : écart net (couvert par une 2e mnémotechnique) / faible | 8 (8) / 19 |
| Lectures retenues on / kun | 39 / 40 |
| Composants KanjiVG distincts | 80, tous nommés |
| … dont cités dans au moins un mnémotechnique | 72 |
| Lectures marquées fragiles (`lecture_fragile`) | 50 |
| Kanji qui n'apparaissent que dans un seul mot N5 | 23 |

**Où la confiance baisse, et pourquoi.** Trois défauts reviennent :

- **Le h japonais** (はん, ほん, ひだり, ひがし, ひゃく) n'existe pas en français : on l'entend « an », « on ». 半 et 本 sont notés bas pour cette seule raison.
- **Le r japonais** est battu, comme en espagnol ; le r français est roulé dans la gorge. Tous les mnémotechniques en r (人 り, 円 まる, 来 ライ, 左 ひだり, 白 しろ) trompent sur la consonne : au mieux moyenne.
- **Les lectures longues de trois syllabes** (九 ここの, 左 ひだり) ne tiennent dans aucun mot français courant ; il faut une coupure artificielle.

Ailleurs, les jeux de mots les plus solides tiennent dans une tournure parlée qui sonne exactement comme la lecture : « n'a qu'à » (中 なか), « t'as qu'à » (高 たか), « qui t'a » (北 きた), « il y a ma » (山 やま), « autocollant » (男 おとこ), « guette sous » (月 ゲツ).

## Écart 79 / 103

La liste N5 de `kanji.json` compte **79 kanji** alors qu'on en attendait 103. L'écart n'est pas corrigé ici. Ce que les données permettent de dire :

- `kanji.json` vient du relevé Tanos de kanji-data, qui **ne garde qu'un niveau par kanji, le plus difficile** quand un kanji figure dans deux listes (voir `japonais/RAPPORT.md`).
- Le champ `jlpt_ancien_kanjidic` (l'ancien niveau 4 du JLPT d'avant 2010, noté dans KANJIDIC2) compte **102 kanji**. Les 79 kanji N5 en font tous partie. Les 23 autres sont rangés en N4 par `kanji.json` (et un en N3) : 会 口 古 多 安 少 店 手 新 目 社 空 立 花 言 買 足 週 道 飲 駅 魚 耳.
- Plusieurs d'entre eux servent déjà de composants ici (口, 目, 言, 耳) : ils ont un nom dans le lexique, mais pas encore de mnémotechnique.

À trancher avec la liste d'origine sur https://www.tanos.co.uk/jlpt/ avant de fixer le périmètre N5.

## Ce que Jacques juge : le français

- Le jeu de mots **s'entend-il** ? Lire la phrase à voix haute, sans regarder le romaji, et voir si le morceau en gras ramène la lecture.
- L'**image** relie-t-elle bien les composants au sens ? Est-elle drôle, visuelle, jamais vulgaire ni méprisante ?
- Les **mots** sont-ils connus de tous les francophones ? Deux sont propres à la France : « kawa » (川, argot pour le café) et « Nénette » (年, vieilli). Le Québec ne les connaît pas forcément.
- Les **noms des composants** (`textes/noms_composants.json`) sont-ils simples et faciles à revoir d'un kanji à l'autre ? Un nom changé là change partout.
- La page `a-relire.html` présente le lot en cours, deux cases à cocher par version, puis le tableau des 79 kanji avec leurs deux notes et leur état.

## Ce qu'un relecteur japonais natif doit vérifier

Ce n'est pas le même travail : le japonais ne doit pas être jugé par quelqu'un qui ne le parle pas.

1. **Le choix de lecture.** La règle « la lecture la plus fréquente dans les mots N5 » donne parfois une lecture qu'aucun enseignant ne présenterait en premier. 50 kanji sont marqués `lecture_fragile` (égalité départagée par les autres niveaux, un seul mot N5, lecture d'une seule syllabe, ou aucun mot N5 aligné). Les plus discutables :
   - 人 → **り** (de 一人 ひとり, 二人 ふたり), plutôt que ジン ou ひと ;
   - 日 → **び** (forme sonorisée dans 曜日), à égalité avec か (les dates), devant ニチ ;
   - 三 み, 四 よ, 六 む, 八 や : lectures des petits nombres (三つ, 三日…), justes mais fragmentaires ;
   - 入 → い (入れる), à égalité avec はい (入る) ; 聞 → き, à égalité avec ブン ;
   - 上 → ジョウ (上手 seulement), à égalité avec あ, うえ, うわ ;
   - 母 → ボ et 父 → ちち : **aucun** mot N5 ne s'aligne (お母さん, お父さん ont une lecture spéciale), la lecture vient des autres niveaux.
   Pour imposer une autre lecture, renseigner `lecture_derogation` avec la raison ; le mnémotechnique sera alors à réécrire.
2. **La justesse des exemples.** Les exemples sont tirés de `mots.json` par le script, mais l'alignement est une heuristique : vérifier que le kanji y a bien la lecture indiquée, et que les mots marqués « autre lecture » ou « lecture spéciale » sont bien lus comme indiqué. Les sens anglais viennent de Waller ; il n'y a pas de sens français des mots, faute de JMdict (voir `japonais/RAPPORT.md`).
3. **Les sens retenus.** Chacun est un sens KANJIDIC, mais le choix entre plusieurs (月 « mois » plutôt que « lune », 気 « esprit » plutôt que « air ») mérite un avis.
4. **Les décompositions KanjiVG** partielles : 17 kanji ont des traits que KanjiVG ne nomme pas (`traits_libres` > 0 : 万 先 円 北 左 年 本 来 母 白 行 電 前 南 今 五 半). Et 書 a pour partie basse une forme de 曰 (« dire »), que le lexique range sous « soleil ».

## Limites connues

- 23 kanji n'apparaissent que dans un seul mot N5 : ils n'ont qu'un exemple, ou un second exemple sous une autre lecture (marqué `autre_lecture`).
- Les mnémotechniques anglais n'ont pas de note de confiance ; ils ont été écrits plus vite que les français.
- Le romaji est en Hepburn modifié (ō, ū pour les voyelles longues), calculé par le script.
