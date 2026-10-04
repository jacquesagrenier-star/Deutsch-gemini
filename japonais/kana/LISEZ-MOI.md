# Module kana — hiragana et katakana

Données de la première étape de l'app de japonais : apprendre à lire les deux alphabets syllabiques. Interface prévue en français et en anglais.

Rien ici n'est branché sur l'app d'allemand. Ce dossier vit sur la branche `japonais-kana` et n'est lu par aucune page en production.

## Contenu

| Fichier | Contenu |
|---|---|
| `kana.json` | **248 signes** : romaji Hepburn, place dans le tableau gojūon, nombre de traits, groupe d'apprentissage, SVG associés. **Généré** par `outils/construire.py` : ne pas le modifier à la main. |
| `traits/` | **177 SVG KanjiVG**, un par caractère Unicode, avec les traits numérotés. Copiés sans modification (CC BY-SA 3.0, voir `LICENCES.md`). Le nom de fichier est le point de code : `03042.svg` = あ. |
| `confusions.json` | **32 groupes** de signes faciles à confondre, avec ce qui les distingue à l'œil, en français (`fr`) et en anglais (`en`). |
| `mnemoniques.json` | **92 moyens mnémotechniques** (46 hiragana + 46 katakana de base), écrits séparément en français et en anglais. **Brouillon à relire.** |
| `planche.html` | Planche de contrôle : tous les signes avec romaji, nombre de traits, groupe et tracé KanjiVG. À ouvrir dans un navigateur pour repérer une erreur à l'œil. |
| `LICENCES.md` | Attribution KanjiVG et ce qu'impose le partage à l'identique. |
| `outils/` | `construire.py` (refait `kana.json` et le vérifie), `planche.py` (refait la planche), `mnemoniques_source.py` (source des mnémoniques). Python 3 seul, aucune dépendance. |

### Ce que couvre `kana.json`

| Catégorie (`categorie`) | Hiragana | Katakana |
|---|---|---|
| `base` — les 46 signes du tableau, ん compris | 46 | 46 |
| `dakuten` / `handakuten` — が, ざ, だ, ば, ぱ… | 25 | 25 |
| `yoon` — きゃ, しゅ, ちょ… | 33 | 33 |
| `petit-tsu` — っ / ッ | 1 | 1 |
| `allongement` — ー | — | 1 |
| `etendu` — katakana pour les mots étrangers (ティ, ファ, ヴ…) | — | 33 |
| `rare` — ゐ ゑ ヰ ヱ, obsolètes | 2 | 2 |

Chaque entrée porte :

- `romaji` en Hepburn modifié (し = shi, ち = chi, つ = tsu, ふ = fu, じ/ぢ = ji, ず/づ = zu, を = o, ん = n). `romaji_variante` donne la graphie historique quand elle existe (を → wo, ゐ → wi).
- `gojuon` : la rangée (`gyo`, ex. か行, et la `consonne`) et la colonne (`dan`, ex. あ段, et la `voyelle`). Les yōon et les katakana étendus n'ont pas de case : ils gardent la rangée de leur premier signe ou `null`.
- `traits` : le total, et dans `composants` le compte et le SVG de chaque caractère. Un signe composé (きゃ, ティ) renvoie aux SVG de ses deux caractères : KanjiVG ne dessine pas de combinaisons, et en fabriquer serait déjà un tracé maison.
- `statut` : `courant`, `particule seulement` (を, ヲ) ou `obsolète` (ゐ ゑ ヰ ヱ), plus une `note` en clair.
- Pour les katakana étendus : `tableau_1991` (1 ou 2) et un mot d'`exemple`.

## Ordre d'apprentissage proposé

**Hiragana d'abord, en entier, puis katakana dans le même ordre.** Les hiragana écrivent la grammaire et les mots japonais : on en a besoin dès la première phrase. Les katakana servent surtout aux mots empruntés ; ils réutilisent les mêmes sons et la même grille, donc ils vont beaucoup plus vite une fois la grille en tête.

Dans chaque alphabet, on suit les **rangées du tableau gojūon**, une rangée par groupe (`groupes` dans `kana.json`) :

| Groupes | Contenu | Pourquoi |
|---|---|---|
| H01 | あ い う え お | Les cinq voyelles : chaque autre signe est une consonne + l'une d'elles. |
| H02 → H10 | か行, さ行, た行, な行, は行, ま行, や行, ら行, わ行 + ん | Une rangée = 5 signes au plus, une seule consonne nouvelle à la fois. L'ordre est celui du tableau et des dictionnaires japonais : l'apprendre dans cet ordre, c'est aussi apprendre à chercher un mot. |
| H11 → H13 | が/ざ, だ/ば, ぱ | Rien de nouveau à dessiner : deux traits (゛) ou un rond (゜) changent la consonne. Groupes de 10 parce que la forme est déjà connue. |
| H14 → H16 | yōon, en trois lots (き し ち に / ひ み り / ぎ じ び ぴ) | Une règle, pas des signes nouveaux : un signe en -i + petit ゃ ゅ ょ. Le dernier lot combine deux règles déjà vues. |
| H17 | っ | La consonne doublée, une fois que l'on lit des mots entiers. |
| K01 → K16 | Même parcours en katakana | |
| K17 | ッ et ー | Omniprésents dans les mots empruntés (コーヒー, ベッド). |
| K18 | Katakana étendus courants (tableau 1 de 1991) | ティ, ファ, シェ, ジェ… : fréquents dans les mots modernes. |
| K19, K20 | Katakana étendus rares (tableau 2) | ヴァ, ウィ, トゥ, クァ… : à voir quand on les rencontre. |
| R | ゐ ゑ ヰ ヱ | Facultatif, pour la culture et les enseignes. |

Pourquoi des rangées plutôt qu'un ordre par fréquence ou par ressemblance :

- **Petits lots** : 3 à 5 signes nouveaux à la fois (10 à 12 pour les groupes qui n'ajoutent qu'une règle), ce que la mémoire de travail encaisse.
- **Une seule nouveauté par lot** : une consonne, ou une règle. On sait toujours ce que l'on est en train d'apprendre.
- **La grille sert de mémoire** : quand on a oublié un signe, on peut le retrouver par sa case (« la colonne e de la rangée k »).
- **Les pièges tombent dans des lots différents** : さ (H03) et ち (H04), シ (K03) et ツ (K04), ソ (K03) et ン (K10). C'est voulu : on apprend chaque signe seul, puis `confusions.json` sert à des **exercices de contraste ciblés** une fois les deux signes vus. Mélanger deux signes jumeaux dès le premier contact produit justement la confusion.
- Les irrégularités (し shi, ち chi, つ tsu, ふ fu, を o) sont signalées dans la description des groupes au moment où elles arrivent.

## Vérifications faites

`python japonais/kana/outils/construire.py` refait `kana.json` et échoue au moindre écart :

1. **Romaji** recalculé depuis les **noms Unicode** des caractères (ex. `HIRAGANA LETTER SI` → shi, `KATAKANA LETTER SMALL YA`) et comparé au tableau saisi, pour les 248 signes, composés compris.
2. **Rangée et colonne gojūon** recoupées contre les mêmes noms Unicode, et l'ordre des points de code contre l'ordre du tableau.
3. **Nombre de traits** de `kana.json` = nombre de traits du SVG KanjiVG, par construction (il est compté dans le fichier), pour chaque signe et chaque composant.
4. Ce même compte recoupé contre un tableau des traits **saisi de mémoire** d'après les manuels usuels, pour les 92 signes de base : aucun écart. Dakuten = signe de base + 2 traits, handakuten = + 1 : vérifié pour les 50.
5. Comptes par catégorie (46 / 25 / 33 / 33) et absence de doublons.
6. Le script a été testé en y injectant des erreurs (ち → ti, ネ à 3 traits, une voyelle fausse, シェ → sye) : il les attrape toutes.

Les trois JSON s'analysent avec `json.load`. Les romaji de `confusions.json` et `mnemoniques.json` concordent avec `kana.json`.

## Ce qui manque ou reste douteux

- **Wikipédia n'a pas pu être consulté** (réseau bloqué dans l'environnement de travail). La vérification indépendante repose sur la base Unicode, qui confirme le romaji et la grille, mais **pas la liste des katakana étendus** : les tableaux 1 et 2 de la notice de 1991 « 外来語の表記 » ont été saisis de mémoire, à recouper contre le texte officiel. Les mots d'exemple de ces signes sont aussi à relire.
- **Variantes d'écriture** : KanjiVG suit les manuels (き 4 traits, さ 3, そ 1, り 2), mais beaucoup de polices et d'enseignants écrivent き et さ attachés, そ en 2 traits ou り en 1 trait. Les entrées concernées portent une `note_traits`. Si l'app affiche une police où le bas de き est attaché, l'élève verra une différence avec le tracé KanjiVG.
- **Pas de SVG pour les signes composés** (きゃ, ティ…) : on affiche les deux SVG côte à côte. Assembler un SVG unique est possible (simple mise en page des deux fichiers), mais ce serait une œuvre dérivée, donc sous CC BY-SA.
- **16 SVG en trop** dans `traits/`, non utilisés par `kana.json` mais gardés car récupérés avec le reste : petits ぁ ぃ ぅ ぇ ぉ ゎ ヮ ヵ ヶ ゕ ゖ, et ゔ ヷ ヸ ヹ ヺ. Les petits ァ ィ ゥ ェ ォ katakana, eux, servent aux katakana étendus.
- **Numéros de traits** : ce sont ceux de KanjiVG, petits et gris (taille 8 sur 109). Pour l'app il faudra sans doute les agrandir ou animer le tracé, ce qui modifie les SVG : partage à l'identique (voir `LICENCES.md`).
- **`mnemoniques.json` est un brouillon** : le français est à juger par un francophone, l'anglais par un anglophone. Certaines images reposent sur un mot que l'élève doit connaître (め = « œil », ニ = « deux » en japonais). Quelques associations sont communes à tous les cours (た = t + a, の = panneau barré).
- **`confusions.json`** décrit les formes telles qu'elles apparaissent dans une police standard ; les distinctions kana/kanji (ロ/口, カ/力, エ/工, ニ/二, ハ/八) dépendent beaucoup de la police, et le contexte reste le seul critère fiable, ce que le fichier dit.
- Pas d'**audio** : ni enregistrement ni synthèse vocale ici.
- ゐ ゑ ヰ ヱ n'ont ni mnémonique ni confusion : facultatifs.
