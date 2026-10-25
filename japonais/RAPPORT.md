# Données JLPT brutes — rapport technique

Construit le 4 octobre 2026 par `python japonais/construire.py`. Tous les chiffres ci-dessous sont ceux que le script imprime ; le relancer les redonne.

## En bref

| | Fait ? |
|---|---|
| Listes de vocabulaire Tanos, N5 à N1 | ✅ 8 293 lignes, dans `mots.json` |
| Liste des kanji Tanos | ✅ 2 211 kanji, dans `kanji.json` |
| KANJIDIC2 (sens fr/en, lectures, traits, fréquence) | ✅ version 2025-11-06 |
| **JMdict (sens et gloses françaises des mots)** | ❌ **injoignable depuis l'environnement de construction** |
| Appariement Tanos → JMdict | ❌ pas fait, faute de JMdict (le code est prêt et testé) |
| **Couverture française des mots** | ❌ **non mesurée**, faute de JMdict |
| Couverture française des kanji | ✅ 90,1 % |

Le chiffre le plus important de la tâche — combien de mots ont déjà une traduction française — **manque**. Pour l'obtenir, il suffit de relancer le script sur une machine qui atteint GitHub ou edrdg.org (voir « Ce qui n'a pas pu être fait »).

## 1. Sources réellement utilisées

Le réseau de l'environnement de construction bloquait `tanos.co.uk`, `edrdg.org`, `ftp.edrdg.org`, l'API GitHub et les téléchargements de releases GitHub. Les dépôts git publics et l'archive Ubuntu passaient. Les données ont donc été lues ainsi — aucune n'a été remplacée par une autre source :

| Donnée | Lue depuis | Version |
|---|---|---|
| Vocabulaire Tanos | copie git des listes d'origine de Waller, faite par stephenmk : [yomitan-jlpt-vocab](https://github.com/stephenmk/yomitan-jlpt-vocab), dossier `original_data/` | commit `b062d4e` (26 août 2025) |
| Niveaux des kanji Tanos | relevé du site Tanos par [kanji-data](https://github.com/davidluzgouveia/kanji-data) (`tools/jlpt.py`), champ `jlpt_new` | commit `00fd707` (27 février 2026) |
| KANJIDIC2 | `kanjidic2.xml.gz` non modifié, tel que livré dans le paquet source Ubuntu `kanjidic_2025.11.06` (son script `debian/download` le télécharge tel quel depuis edrdg.org) | `database_version 2025-310`, `date_of_creation 2025-11-06` |
| JMdict | — | **non obtenu** (dernière release jmdict-simplified constatée : `3.6.2+20260928191014`) |

Points de vigilance sur ces copies :

- **Vocabulaire.** Ce n'est pas le HTML du site Tanos mais un CSV `jmdict_seq, kana, kanji, waller_definition`. L'orthographe de Waller est conservée (歯磨, 逆上る, 火燵 sont bien là en N1, comme sur le site d'origine), et stephenmk a ajouté la colonne `jmdict_seq`, son propre appariement. `mots.json` garde la ligne CSV telle quelle (`tanos.texte`) et ses champs (`tanos.champs`). Ce dépôt est sous CC BY-SA 4.0 (voir LICENCES.md).
- **Kanji.** Le relevé de kanji-data parcourt les niveaux N5 → N1 et écrase le niveau à chaque passage : un kanji présent dans deux listes Tanos ne garde que le plus difficile. Je n'ai pas pu le vérifier contre le site.
- **Je n'ai pu comparer aucune de ces copies au site Tanos lui-même.** Une autre copie répandue (open-anki-jlpt-decks, dérivée de Tanos puis corrigée à la main) donne d'autres comptes (N5 718, N4 668, N3 2 140, N2 1 906, N1 2 699) : les listes « Tanos » qui circulent ne sont pas toutes identiques.

## 2. Comptes par niveau

| Niveau | Mots (lignes Tanos) | Attendu | Écart | Kanji | Attendu | Écart |
|---|---:|---:|---:|---:|---:|---:|
| N5 | 684 | 743 | −59 | 79 | 103 | −24 |
| N4 | 640 | 684 | −44 | 166 | 181 | −15 |
| N3 | 1 730 | 1 621 | +109 | 367 | 341 | +26 |
| N2 | 1 812 | 1 910 | −98 | 367 | 400 | −33 |
| N1 | 3 427 | 3 087 | +340 | 1 232 | 1 187 | +45 |
| **Total** | **8 293** | 8 045 | +248 | **2 211** | 2 212 | −1 |

**Les écarts sont importants à chaque niveau**, alors que les totaux sont proches. Je n'ai pas pu trancher, puisque le site d'origine était injoignable. Deux remarques seulement :

- Pour les kanji, les totaux ne diffèrent que d'un (2 211 contre 2 212) : les ordres de grandeur attendus semblent répartir autrement le même ensemble, ou venir d'une autre liste. Les comptes 79 / 166 / 367 / 367 / 1 232 sont ceux que kanji-data a relevés sur Tanos.
- Pour les mots, le compte N5 attendu (743) ne correspond à aucune des deux copies consultées. Le N4 attendu (684) est exactement le N5 de la copie stephenmk : une confusion de lignes est possible quelque part.

À vérifier à la main sur https://www.tanos.co.uk/jlpt/ avant de s'appuyer sur ces chiffres.

Autres constats sur la liste de mots :

- 8 289 paires (kanji, kana) distinctes. Quatre mots figurent à deux niveaux et ont donc deux objets dans `mots.json` : いいえ (N5, N1), しみじみ (N2, N1), それでは (N5, N1), 三日月／みかづき (N2, N1).
- 1 019 mots n'ont pas de forme en kanji dans Tanos (kana seul).
- 14 lignes N1 n'ont pas d'identifiant JMdict dans la copie stephenmk. Ce sont des kanji isolés avec une lecture on, pas des mots : 依 い, 於 お, 仮 か, 割 かつ, 乾 かん, 蓋 がい, 傾 けい, 巨 きょ, 佐 さ, 傷 しょう, 働 どう, 南 なん, 伐 ばつ, 倣 ほう. Ils seront probablement « introuvables » dans JMdict.
- Quelques graphies en pleine chasse : ｘ／バツ (N2), ＯＫ／オーケー et Ｇパン／ジーパン (N1).

## 3. Appariement Tanos → JMdict

**Pas fait** : les 8 293 mots ont `"appariement": {"statut": "jmdict_indisponible"}` et `"jmdict": null`. La colonne `jmdict_seq` de stephenmk est conservée dans `appariement.jmdict_seq_tanos`, mais **elle n'est pas vérifiée** et je ne l'ai pas utilisée comme résultat.

Le code d'appariement est écrit et a été testé sur un petit fichier factice dans les deux formats (JSON jmdict-simplified et XML d'origine), hors dépôt. Ses règles :

1. **Mot Tanos avec kanji** : candidats = les entrées JMdict qui contiennent cette forme en kanji *et* cette lecture en kana appliquée à cette forme (`re_restr` / `appliesToKanji` respectés). Jamais sur le kanji seul ou le kana seul.
2. **Mot Tanos sans kanji** : candidats = les entrées qui ont cette lecture en kana.
3. Un candidat → `unique`. Aucun → `introuvable`. Plusieurs → `ambigu`, puis on retient, dans cet ordre, la première règle qui tranche :
   1. l'entrée dont l'identifiant est celui de la colonne `jmdict_seq` de stephenmk ;
   2. (sans kanji) la seule entrée sans forme kanji, puis la seule marquée `uk` (« s'écrit d'ordinaire en kana ») ;
   3. la seule entrée marquée courante (`common`) ;
   4. à défaut, le plus petit identifiant JMdict.

   La raison retenue est écrite dans `appariement.raison`, avec la liste des candidats.

Le script imprimera la liste des ambigus, des introuvables, et des mots où son choix diffère de l'identifiant de stephenmk.

## 4. Couverture française

### Mots — non mesurée

Sans JMdict, aucun chiffre. Le script calculera, par niveau : les mots avec au moins une glose française ; ceux dont *tous* les sens en ont une ; et une approximation (au moins autant de sens français que de sens anglais).

⚠️ Une précaution pour lire ces chiffres le moment venu : dans le JMdict complet, les gloses d'une langue autre que l'anglais forment, à ma connaissance, des sens séparés, qui ne sont pas alignés sur les sens anglais. « Tous les sens ont une glose française » pourrait donc valoir près de 0 % par construction. C'est pourquoi le script donne aussi l'approximation. Je n'ai pas pu le vérifier sur le vrai fichier. Pour ordre de grandeur, la page Wikipédia de JMdict parle d'environ 15 000 entrées avec gloses françaises, contre 133 000 en allemand : la couverture française des mots sera probablement faible.

### Kanji — mesurée (KANJIDIC2)

| Niveau | Kanji | Avec un sens français | Taux |
|---|---:|---:|---:|
| N5 | 79 | 79 | 100,0 % |
| N4 | 166 | 166 | 100,0 % |
| N3 | 367 | 367 | 100,0 % |
| N2 | 367 | 367 | 100,0 % |
| N1 | 1 232 | 1 013 | 82,2 % |
| **Total** | **2 211** | **1 992** | **90,1 %** |

Les 219 kanji N1 sans sens français sont presque tous des kanji de prénoms (jinmeiyō), que la liste N1 de Tanos inclut :

也亦亨亮伍伎伶伽佑侃侑倖倭冴冶凌凜凪凱勁匡叡叶哉唄啄喬嘉奎嬉孟宏宥尭峻崚嵩嵯嶺巌巴巽庄弥彗彪彬怜恕悌惇惟惣慧憧拳捷捺敦斐旺昂昴晃晋晏晟晨暉暢曙朔李杜柊柚柾栞梧椋椎椰楊楓榛槙槻樺橘檀欣欽毅毬汰沙洲洵洸浩淳渥湧滉漱澪熙燎燦燿爽爾玖玲琉琢琳瑚瑛瑞瑠瑳瑶璃甫皐皓眉眸瞭碧碩磯祐禄禎秦稀稔稜穣竣笙紗紘紬絃絢綜綸綺綾緋翔翠耀耶聡肇胡胤脩舜芙芹茄茅茉茜莉莞菖菫萌萩葵蒔蒼蓉蓮蕉蕗藍衿袈裟詢誼諄諒赳輔迪遥遼邑那郁采隼雛霞靖鞠頌颯馨駿魁鮎鯛鳳鴻鵬鷹麟麿黎黛

Tous les kanji Tanos ont été trouvés dans KANJIDIC2.

### Exemples de sens français, tirés au hasard (graine 20261004)

Faute de JMdict, ce sont des **sens de kanji** (KANJIDIC2), pas des gloses de mots :

| Niveau | Kanji | Français | Anglais |
|---|---|---|---|
| N3 | 市 | marché, ville, cité | market, city, town |
| N4 | 品 | marchandise, dignité, raffinement, article, compteur de plats | goods, refinement, dignity, article, counter for meal courses |
| N1 | 熊 | ours | bear |
| N2 | 仏 | Bouddha, France, défunt | Buddha, the dead, France |
| N2 | 湾 | golfe, baie, crique | gulf, bay, inlet |
| N3 | 辞 | démission, mot, terme, expression | resign, word, term, expression |
| N1 | 功 | réussite, réalisation, succès, mérite, honneur, crédit | achievement, merits, success, honor, credit |
| N3 | 慣 | avoir l'habitude, s'accoutumer, coutumes, expérience | accustomed, get used to, become experienced |
| N1 | 羊 | mouton | sheep |
| N1 | 漠 | vague, obscur, désert, vaste | vague, obscure, desert, wide |

Les sens sont corrects, mais ce sont des mots-clés et non des définitions : « 品 » mélange « marchandise » et « dignité » sans contexte. On y trouve aussi des vestiges peu pédagogiques (盲 : « aveugle, ignorant », lecture kun めくら, un terme aujourd'hui offensant).

## 5. Format des fichiers produits

`mots.json` : `{"meta": {...}, "niveaux": {"N5": [...], ..., "N1": [...]}}`. Chaque mot :

- `niveau`, `kanji` (ou `null`), `kana` — tels que Tanos les donne ;
- `tanos` : fichier, numéro de ligne, `texte` (la ligne CSV d'origine, telle quelle) et `champs` (dont `waller_definition`, la définition anglaise de Waller) ;
- `jmdict` : l'entrée retenue (identifiant, toutes les formes kanji et kana avec leurs balises, et chaque sens avec parties du discours, restrictions, renvois, domaine, dialecte, `misc`, `info`, origine, `fr` et `en` en listes ou `null`) — `null` aujourd'hui ;
- `appariement` : statut, candidats, raison, `jmdict_seq_tanos`.

Remarque : avec le JSON jmdict-simplified, les parties du discours sont des codes (`v5u`) ; avec le XML d'origine, ce sont les libellés développés (« Godan verb with 'u' ending »), car Python développe les entités du DTD.

`kanji.json` : même enveloppe. Chaque kanji : `kanji`, `niveau`, `sens_fr`, `sens_en` (listes ou `null`), `lectures_on`, `lectures_kun`, `nanori`, `traits` (liste : le premier nombre est le bon, les suivants sont des erreurs de compte courantes notées par KANJIDIC), `frequence` (rang parmi les 2 500 les plus fréquents, `null` au-delà), `grade`, `jlpt_ancien_kanjidic` (l'ancien JLPT en 4 niveaux).

## 6. Vérifications faites avant de pousser

- Les deux JSON s'analysent ; deux constructions successives donnent des chiffres identiques.
- 20 entrées tirées au hasard (10 mots, 10 kanji) relues contre les sources brutes : ligne CSV Tanos ; et pour les kanji, bloc XML KANJIDIC2 (sens fr et en, lectures on et kun, traits, fréquence) plus niveau kanji-data. **20 sur 20 conformes.**
- Analyseurs JMdict (JSON et XML) et appariement testés sur un fichier factice : paire unique, forme kanji secondaire, `re_restr`, ambiguïté tranchée par l'identifiant ou faute de mieux, mot en kana seul, introuvable.

## 7. Ce qui n'a pas pu être fait, et pourquoi

1. **JMdict n'a pas été obtenu.** Tentatives : API et releases GitHub de jmdict-simplified (403), `ftp.edrdg.org/pub/Nihongo/JMdict.gz` (403), miroir de l'University of South Florida, `ftp.usf.edu` (403), codeberg (403). Le seul JMdict trouvé ailleurs, le paquet PyPI `jamdict-data`, date d'avril 2021 et **ne contient que l'anglais** : inutilisable, et de toute façon ce n'est pas la version demandée. Aucun paquet Ubuntu ne contient JMdict.
   → **Pour finir le travail** : sur un poste qui atteint GitHub, relancer `python japonais/construire.py` ; il prend tout seul la dernière release `jmdict-all`. Sinon, télécharger `jmdict-all-*.json.zip` depuis https://github.com/scriptin/jmdict-simplified/releases et lancer `python japonais/construire.py --jmdict CHEMIN`. Puis remplacer les sections 3 et 4 de ce rapport par la sortie du script.
2. **Le site Tanos n'a pas été lu directement** : comptes non vérifiés, écarts par niveau inexpliqués (section 2).
3. **KANJIDIC2 vient de la copie Ubuntu du 6 novembre 2025**, pas du fichier du jour d'edrdg.org. Le script essaie d'abord edrdg.org et n'utilise la copie Ubuntu qu'à défaut ; sur un poste qui atteint edrdg.org, `--rafraichir` récupère la version courante.
