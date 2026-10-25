# Brief : fabriquer les cartes de vocabulaire japonais N5 à N3

Tu travailles pour Wortando, une app de flashcards pour francophones. Elle enseigne l'allemand aujourd'hui, et elle enseignera le japonais demain. Jacques, le propriétaire, est francophone. Il ne parle pas japonais. Tout ce que tu écris pour lui est en français.

## Le but

Fabriquer les **données des cartes** de vocabulaire japonais des niveaux JLPT N5, N4 et N3 (3 054 mots), au format « fiche » déjà conçu, avec une page HTML pour que Jacques les relise.

**Hors périmètre** : l'écran de jeu, `index.html` et tout code de l'app. On ne touche pas l'app allemande. Ce qu'on fabrique, ce sont les cartes, pas le jeu.

## Où travailler

- Branche **`japonais-cartes`**, déjà créée. Tu y fais tes commits et tu la pousses. **Ne pousse jamais sur `main`**, et n'ouvre pas de pull request.
- Dossier : `japonais/cartes/`.
- Fais un **commit et un push après chaque lot**, pour qu'un arrêt en cours de route ne perde rien.

## Ce qui existe déjà

| Quoi | Où |
|---|---|
| **Le format fiche** (à suivre) | `japonais/moteur/schema-fiche.json`, `japonais/moteur/CONCEPTION.md` §2, exemple `japonais/moteur/exemples/mot-mizu.json` (sur cette branche) |
| **Tes données d'entrée** : 3 054 mots, avec la liste Tanos, JMdict (sens anglais ordonnés, gloses françaises en vrac) et jusqu'à 3 phrases Tatoeba candidates | `japonais/cartes/sources/mots-n5-n3.json` (extrait sur le PC par `outils/extraire_sources.py` ; **tu ne peux pas le refaire**, puisque le réseau du cloud bloque JMdict) |
| Kanji (sens, lectures on/kun, KANJIDIC2) | `git show origin/japonais-donnees:japonais/kanji.json` |
| Algorithme d'alignement kanji ↔ lecture (pour les furigana) | `git show origin/japonais-kanji-mnemo:japonais/kanji/construire.py` et son `LISEZ-MOI.md` |
| Romaji Hepburn par kana | `git show origin/japonais-kana:japonais/kana/kana.json` |
| Moteur de conjugaison (classes JMdict v1, v5k, adj-i…) | branche `japonais-conjugaison` |
| Page de relecture qui sert de modèle | `git show origin/japonais-kanji-mnemo:japonais/kanji/a-relire.html` |

## Ce qu'on sait de la qualité des sources (vérifié le 4 oct. 2026, y compris par un autre modèle)

- **Gloses françaises JMdict** : elles sont souvent justes, mais livrées **en vrac**, non alignées sur les sens et souvent **par ordre alphabétique**. Exemple : 出口 donne « fuite ; orifice ; passerelle ; sortie ». La bonne traduction n'est pas la première de la liste, **il faut la choisir**. Sur un échantillon, environ 70 % sont utilisables après ce choix, 25 % sont à retoucher et 5 % sont fausses (左 traduit par « droite »). **Le sens anglais de JMdict est la référence fiable**, avec ses sens rangés du plus courant au plus rare.
- **Tanos garde parfois une graphie rare** (明い au lieu de 明るい). La forme courante est dans `jmdict_formes_kanji`, où les formes rares portent « (rare) ». Sur la carte, montre la forme courante.
- **Phrases Tatoeba** : 98 % viennent du corpus Tanaka, écrit par des étudiants, et environ 80 % sont justes. Il y a des contresens hérités, par exemple 私はよく彼に頼っています traduit par « Je suis en bons termes avec lui ». Une phrase dont `appariement` contient « sous-chaîne » est **à rejeter**. Un natif relira le japonais plus tard : toi, tu juges si le **français correspond au japonais**.
- **Ne jamais présenter un brouillon comme vérifié.** Tout ce que tu choisis ou écris porte le statut `brouillon`. Seul Jacques fait passer une fiche à `relu`.

## Ce que chaque fiche doit contenir

Une fiche `type: "mot"` par mot, suivant le schéma :

- `id` : `jmdict:<jmdict_id>`. **Il est stable pour toujours**, car c'est la clé de progression de l'élève. S'il y a deux fois le même id dans un niveau, garde-en un seul et note-le dans le rapport.
- `ecritures` : `kanji` (la forme courante, ou `null` si le mot s'écrit d'habitude en kana : regarde `misc` « usually written using kana alone »), `kana` et `romaji` (**calculé par script**, Hepburn, jamais tapé à la main).
- `furigana` : calculés par l'alignement sur les lectures KANJIDIC. Pour une lecture spéciale (今日 きょう, 大人 おとな), mets un seul bloc pour tout le mot. Si tu as un doute, mets le statut `manquant` avec une note.
- `classe` : le code JMdict du premier sens (v1, v5k, adj-i, adj-na, n…).
- `gloses.fr` :
  - `affichee` : **la traduction de la carte**. Elle est **courte** (ce qu'on lirait au dos d'une flashcard), donne le sens le plus courant, et deux sens au maximum, séparés par « ; ». Choisis-la parmi les gloses JMdict quand l'une convient (`src: "jmdict"`). Sinon, écris-la (`src: "wortando"`), en t'appuyant sur l'anglais.
  - `autres` : les autres traductions acceptables. Un quiz les comptera justes.
  - Ajoute `note` dès que le choix n'est pas évident.
- `gloses.en.affichee` : même règle, à partir de l'anglais JMdict ou de Waller.
- `kanji` : la liste des kanji contenus.
- `phrases` : l'id de **la meilleure phrase** (une seule, deux au plus). Préfère `niveau_respecte`, puis `longueur_dans_la_cible`, puis `francais_direct`, et vérifie que **le français dit ce que dit le japonais**. Si aucune candidate n'est bonne, laisse la liste vide avec une note. Ne fabrique pas de phrase japonaise : c'est le rôle du natif.

Les phrases retenues vont dans des fiches `type: "phrase"`, d'id `phrase:tatoeba:<id jpn>`. Chacune garde le japonais, le français, l'anglais, les ids Tatoeba et **les auteurs** (la licence CC BY oblige à les citer).

## Verdict par fiche (pour Jacques)

Pour chaque fiche, ajoute un champ `verdict_machine` qui prend une valeur parmi `BON`, `A_AMELIORER`, `A_REMPLACER` et `FAUX`, et qui juge **ce que JMdict proposait**. Ajoute aussi `raison` (une phrase courte). C'est la grille déjà retenue avec Jacques. Elle lui dit où regarder en premier.

## Méthode conseillée

1. Un script (`outils/construire.py`, bibliothèque standard seulement) fait tout ce qui est mécanique : id, formes, romaji, furigana, classe, liste des kanji, rejet des phrases « sous-chaîne », et les lots à juger.
2. **Toi**, tu juges par lots d'environ 50 mots. Tu écris tes choix dans `japonais/cartes/decisions/<niveau>-<nnn>.json` (glose affichée, autres, phrase retenue, verdict, raison, note). Ces fichiers sont **la seule chose écrite à la main**.
3. Le script fusionne les décisions et les données mécaniques dans `japonais/cartes/mots-n5.json`, `mots-n4.json` et `mots-n3.json` (format `{"sources": …, "entrees": [...]}`), plus `phrases-n5.json`, etc. Il **vérifie** : schéma respecté, id uniques, glose affichée non vide, phrase retenue présente parmi les candidates, romaji recalculé identique.
4. **L'ordre : le N5 en entier d'abord** (684 mots), puis le N4, puis le N3. Si le temps manque, mieux vaut un N5 complet et propre que trois niveaux à moitié.

## La page à relire

`japonais/cartes/a-relire.html` est un fichier autonome, qui marche hors ligne, sur le modèle de `kanji/a-relire.html`. Il contient :

- Un **filtre par verdict** : `FAUX` et `A_REMPLACER` d'abord, puisque ce sont eux que Jacques doit voir.
- Une carte par mot. Au recto : le japonais, avec ses furigana (`<ruby>`, `lang="ja"`). Au verso : la traduction affichée, les autres, la phrase et sa traduction. En petit : l'anglais JMdict, pour comparer.
- Pour chaque carte, quatre boutons (BON / À AMÉLIORER / À REMPLACER / FAUX) et un champ de correction. Les réponses sont gardées dans `localStorage`, avec un bouton qui **exporte** un JSON. Une page qui perd les réponses de Jacques est le pire défaut possible : ça s'est déjà produit une fois.
- Un lien par niveau. Pour 3 000 cartes, découpe en pages ou charge au fil du défilement.

## Le compte rendu

`japonais/cartes/RAPPORT.md` est écrit en français simple, pour Jacques. Il donne :

- les comptes par niveau et par verdict ;
- ce que tu as écrit toi-même (`src: wortando`) ;
- les mots sans bonne phrase ;
- les doublons ;
- dix exemples de choix difficiles, avec ta raison ;
- **ce qui n'est pas vérifié**.

Ne dis pas « validé » : tout est en brouillon.
