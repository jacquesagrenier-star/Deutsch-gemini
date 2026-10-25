# Le japonais au niveau de l'allemand et de l'espagnol : état des lieux et plan

25 octobre 2026, v957. **Document à valider par Jacques avant tout code ou toute dépense.**
Rien n'a été publié, payé ni modifié dans `index.html`. Chaque chiffre ci-dessous a été
compté dans les fichiers, avec la source indiquée. Quand un chiffre vient de la mémoire
ou d'une estimation, c'est écrit.

## En bref

- **Il existe beaucoup de matière japonaise, mais rien dans l'app.** `index.html` ne
  contient aucune ligne de japonais. Le travail est réparti sur **huit branches jamais
  fusionnées** (du 4 au 12 oct.) et sur des dossiers locaux non versionnés (`japonais/`,
  `visuel/prototype/eki|genkan|konbini*`, `reports/`).
- **Le japonais ne peut pas suivre le chemin de l'espagnol.** L'espagnol avait déjà le
  format allemand : listes de mots, genre, article, tableaux de conjugaison. Sa fusion a
  surtout consisté à renvoyer des noms de fichiers (table `fichiers` de
  `LANGUE_ESPAGNOL`). Le japonais n'a ni genre ni article. Il s'écrit avec trois
  systèmes (kanji, kana, romaji) et ses lectures s'affichent au-dessus des kanji
  (furigana). Le kanji est un objet d'étude à part entière, et la conjugaison se calcule.
  Il faut donc **du code neuf** à côté de l'existant, pas un simple renvoi.
- **Recommandation** : le même moteur (`index.html?apprendre=ja`), d'abord ouvert au
  compte admin seul. Le premier palier est **« N5 complet »** (le JLPT N5 correspond à peu
  près à l'A1) : toutes les portes qu'un débutant voit en allemand et en espagnol,
  plus les kana et les kanji N5. Le N4 vient ensuite. On commence par ce qui ne coûte
  rien, et le seul gros poste de dépense est le relecteur natif.

---

## 1. Ce qui existe déjà pour le japonais (mesuré)

| Quoi | Où | Chiffre | État |
|---|---|---|---|
| **Fiches de mots** N5 / N4 / N3 | branche `japonais-cartes`, `japonais/cartes/mots-n*.json` | **667 / 630 / 1 651** (2 948) | Toutes en `brouillon`. Verdict machine N5 : 522 BON, 113 À AMÉLIORER, 24 À REMPLACER, 8 FAUX. N4 : 484 / 126 / 14 / 6. **N3 jamais jugé** (0 verdict, 0 phrase) |
| …dont verbes / noms / adjectifs / adverbes | idem, champ `classe` | N5 : 108 / 421 / 88 / 25 ; N4 : 153 / 370 / 50 / 36 ; N3 : 212 / 1 170 / 123 / 82 | Le moteur de conjugaison sait déjà les fléchir |
| **Phrases d'exemple** (Tatoeba) | `japonais/cartes/phrases-n*.json` | **514 / 503 / 0** | Relecture croisée Fable + GPT + Gemini faite le 12 oct. : 766 phrases jugées bonnes par les trois. 3 fautes de kanji corrigées, 129 traductions françaises revues. **251 phrases (+ 77 tirées en échantillon) attendent un natif** (`japonais/cartes/relecture/pour-le-natif.md`, local) |
| Mots bruts N5 à N1 | `japonais-donnees`, `mots.json` | 684 / 640 / 1 730 / 1 812 / 3 427 | Matière première sans glose française |
| **Kanji** (KANJIDIC2) | `japonais-donnees`, `kanji.json` | N5 **79**, N4 166, N3 367, N2 367, N1 1 232 | Sens et lectures. Le N5 « à 102 » (en ajoutant les 23 de l'ancien niveau 4, décidé le 7 oct.) n'est construit nulle part |
| **Mnémoniques des kanji N5** | branche `claude/fervent-noether-2iwytm` (**pas fusionnée** dans `japonais-kanji-mnemo`) | 79 écrites, en français et en anglais | **12 validées**, 33 à juger, 27 hors charte, 7 à réécrire. Seuls 20 kanji ont reçu ton avis |
| **Kana** | `japonais-kana`, `kana/kana.json` | **248 signes**, 177 SVG de traits, 92 mnémoniques | Mnémoniques en `brouillon à relire`, plus une liste de confusions (シ/ツ…) |
| **Moteur de conjugaison** | `japonais-conjugaison`, `conjugaison.js` | 284 593 vérifications réussies | Prêt, jamais branché |
| Script de phrases | `japonais-phrases` | — | A servi, résultats locaux |
| **Document de conception du moteur** | `japonais-moteur`, `moteur/CONCEPTION.md` | — | ⚠️ Daté du 6 oct., **avant** la décision « une seule app » (9 oct.) et la fusion espagnole (10 oct.). Son architecture (une copie d'`index.html` sous `/ja/`) est **dépassée**. Ses parties 2 et 3 restent valables : fiches, furigana, polices mesurées (≈ 300 Ko au N5), audio haché sur la lecture et non sur l'écriture, double répétition espacée mots/kanji |
| **Scènes japonaises** | `visuel/prototype/` (non versionné) + `JAPONAIS-SCENES.md` | 3 scènes : konbini (36 zones, 40 mots), eki (30 / 39), genkan (39 / 47) | Masques SAM tous justes, **0,45 $ dépensés**. Pas jouables : `construire.py` ne lit que le corpus allemand. 23 mots hors du corpus N5-N3 |
| **Mosaïque japonaise** | `japonais/mosaique/` (16 Mo, local) | **60 images + 15 en réserve** | Planches pas encore validées par toi. Notices de 15 artistes et 75 histoires (fr + en) en brouillon, dont 4 anecdotes à confirmer par une source écrite |
| Étude de marché | `reports/Marché du japonais francophone.md` (local) | — | Faite le 3 oct. La **cartographie des concurrents** a été lancée le 4 oct. mais **n'a jamais été rangée** dans `reports/` |
| Relecteur natif | — | **aucun** | Indispensable pour le japonais (rapport qualité du 4 oct.) |

---

## 2. Le tableau langue × contenu

Sources : `themes.json`, `verbe.json`, etc. pour l'allemand ; `espanol/datos/*.json` pour
l'espagnol ; branches `japonais-*` pour le japonais. Toutes les valeurs ont été comptées le
25 oct., sauf celles marquées (m), qui viennent de la mémoire.

| Contenu | Allemand | Espagnol | Japonais |
|---|---|---|---|
| Niveaux | A1 → C1 | A1 → B2 | N5 → N3 en brouillon (≈ A1 → B1), **rien dans l'app** |
| Thèmes de vocabulaire (noms) | **197 thèmes, 4 274 mots** (A1 465 · A2 606 · B1 1 806 · B2 449 · C1 948) | **141 thèmes, 1 795 mots** (505 · 539 · 515 · 236) | 0 thème. 1 961 noms N5-N3 dans les fiches, **pas rangés par thème** |
| Verbes | 1 314 (111 · 236 · 515 · 180 · 272) | 873 (123 · 274 · 314 · 162) | 473 dans les fiches (108 · 153 · 212) |
| Adjectifs | 981 | 604 | 261 dans les fiches |
| Adverbes | 470 | 228 | 143 dans les fiches |
| Expressions | 569 | 245 | 0 |
| Mots-outils | 161 | 152 | 0. **Les particules (は, が, を, に, で…) sont le cœur de la grammaire japonaise** |
| Phrase d'exemple par mot | oui | oui | 1 017 phrases (N5 + N4), 0 en N3 |
| Premiers pas | 8 étapes, 190 éléments | 8 étapes, 191 éléments | 0 |
| A1 voyage | 12 escales + 2 « installé » + 8 étapes de suite, 383 mots | même forme, 376 mots | 0 (escales à réécrire pour le Japon) |
| Fiches de grammaire | 19 rubriques (`grammaire.json`), en 9 langues | 17 fiches, en 4 langues | 0 |
| Feuilles de conjugaison | 42 (A2 12 · B1 12 · B2 10 · C1 8) | 28 (A2 10 · B1 10 · B2 8) | 0 feuille. Moteur prêt |
| Séries d'exercices | 48 jeux, 2 721 questions | 24 jeux, 1 343 questions | 0 |
| Examen blanc | `pruefung.json` : lire 22, écouter 120, écrire 27, parler 35 | 0 | 0 (l'étude voulait un JLPT blanc) |
| Prononciation | 25 règles (voyelles 9 · consonnes 13 · fins 3) | 18 règles | 0. En japonais, la prononciation passe par les kana, les voyelles longues et le っ |
| Repères (nombres, jours, mois…) | 11 | 10 | 0. Les **compteurs** (一つ, 一本, 一枚) sont à ajouter, l'allemand n'en a pas |
| Scènes | 43 | 43 (mêmes images, `mots.json`) | 3 prototypes non jouables |
| Épisodes vidéo | 4, sous-titrés en 9 langues | 4 (fr, en) | 0 |
| Mosaïque | 65 tableaux | 66 tableaux | 60 + 15, non validés |
| Voix ElevenLabs | Aurora, corpus A1-C1 (≈ 25 300 fichiers (m)) | Lolita (Espagne) et Monica (Am. latine), A1-A2. Au-delà, la voix du téléphone | **0. Aucune voix choisie** |
| Langues d'interface | 9 (fr en tr uk fa ar pt pl ru) | 4 (fr en pt ar) | **Décidé le 4 oct. : fr + en seulement** |
| Fiche des stores | 10 langues de texte (m) | annoncé en fr et en | rien |
| **Propre au japonais : kana** | — | — | 248 signes, 177 tracés SVG, 92 mnémoniques en brouillon |
| **Kanji** | — | — | 79 (N5) + 166 (N4) + 367 (N3). 79 mnémoniques N5 écrites, dont **12 validées** |
| **Lectures (furigana, romaji)** | — | — | Calculées dans chaque fiche, en brouillon. Les lectures spéciales (今日 → きょう) sont signalées |
| Relecture par un natif | faite (germanophone, 25 oct.) | — | **aucune** |

**Ce qu'il faut retenir.** Pour les mots N5-N4, le japonais atteint déjà les trois
quarts du volume de l'A1-A2 espagnol (1 297 fiches contre 1 762 noms, verbes, adjectifs
et adverbes), mais aucun mot n'a été relu par un natif. Pour **tout le reste** (parcours, exercices, grammaire, repères, voix,
scènes), il part de zéro.

---

## 3. Ce que ça demande au moteur (mesuré dans `index.html`)

- `LANGUE_APPRISE` n'accepte que `"de"` et `"es"`. Le code contient **95 tests à deux
  branches** (87 `=== "es"`, 8 `!== "es"`) : tout ce qui n'est pas l'espagnol
  **retombe sur l'allemand**. Une troisième langue verrait donc du contenu allemand
  partout où on ne l'a pas prévue. C'est le premier chantier, et c'est invisible
  pour les utilisateurs.
- Rien de ce qui suit n'existe : fiche à plusieurs écritures, furigana (`<ruby>`,
  `lang="ja"`), police japonaise (pile système puis Noto Sans JP, ≈ 300 Ko au N5),
  carte de kana, carte de kanji avec tracé, double répétition espacée (un kanji et les
  mots qui le contiennent).
- Ce qui se reprend tel quel, sur le modèle de l'espagnol : préfixe de stockage
  (`wortandoJa_`), progression Firestore dans sa propre collection (`usuariosJa`, avec
  des règles à coller par toi, comme pour `usuariosEs`), dossier audio propre (`ja/`),
  parcours Playwright avec une référence `ja`, et **0 écart pour l'allemand et
  l'espagnol à chaque étape**.
- Taille estimée par `CONCEPTION.md` : 2 000 à 3 000 lignes neuves, rangées derrière la
  langue japonaise. C'est une estimation, pas une mesure.

---

## 4. Les décisions qui te reviennent

### Décision 1 : même moteur ou app à part ?

**Recommandé : le même moteur, `index.html?apprendre=ja`.** C'est la décision « une
seule app pour toutes les langues » du 9 oct., et la fusion espagnole a montré qu'elle
tient. Une app à part, c'est le chemin de `fork.py` (84 versions de retard en trois
semaines), aujourd'hui abandonné. Deux conditions :
- le japonais reste un **essai réservé à l'admin** (comme `a1_voyage` en v862) tant que le
  N5 n'est pas relu par un natif ;
- les 95 tests à deux branches sont repris un par un **avant** d'ouvrir la porte,
  sous contrôle du parcours allemand et espagnol (0 écart).

### Décision 2 : par quoi commencer ?

**Recommandé, dans cet ordre, sans aucune dépense :**
1. **Ranger** : regrouper les huit branches en une seule branche `japonais`, plus les
   scènes et la mosaïque locales. Rien sur `main`.
2. **Le socle**, invisible pour les utilisateurs : `LANGUE_JAPONAIS`, la porte admin, la
   reprise des 95 tests, le stockage et Firestore à part, le chargeur de fiches, les
   furigana et la police.
3. **Les kana comme Premiers pas japonais** : hiragana puis katakana, avec tracé et
   mnémoniques. Les données sont prêtes, et **personne ne peut lire un mot sans eux**.
4. **Les cartes N5 dans la séance du jour** (667 mots, d'abord avec la voix ja-JP du
   téléphone).
5. **Les kanji N5**, dès que tu as jugé les mnémoniques.

L'autre ordre possible serait de commencer par les kanji, puisque c'est l'angle de
marché (Bunpro couvre déjà la grammaire en français). Mais sans kana ni mots, il n'y a
rien de jouable à faire essayer.

### Décision 3 : que veut dire « même niveau » ?

**Recommandé : le même parcours, palier par palier, plutôt que le même volume.**
- **Palier 1, « N5 complet »** : en japonais, chaque porte qu'un débutant voit en
  allemand et en espagnol. Premiers pas (kana et premiers mots), séance du jour, thèmes
  N5, A1 voyage réécrit pour le Japon (konbini, gare, restaurant…), prononciation,
  repères (avec les compteurs), conjugaison de base (-ます, -て, -ない), séries
  d'exercices sur les particules, scènes, voix, mosaïque, interface fr et en. Plus les
  kana et les kanji N5. **Et la relecture du N5 par un natif avant toute ouverture aux
  testeurs.**
- **Palier 2, « N4 »** (≈ A2) : le même parcours, avec les kanji N4.
- Le **N3** (≈ B1) correspond au trou de marché repéré par l'étude. Il vient après, et
  ses fiches doivent encore être jugées.
- Ce qui n'a pas de sens en japonais n'est pas copié : genre, articles, et les 9
  langues d'interface (fr + en, décidé le 4 oct.).
- **Les scènes : question à part.** L'espagnol reprend les 43 scènes allemandes avec un
  mot par zone. Pour le japonais, recommandé : les 3 scènes japonaises, plus seulement
  les scènes « universelles » (cuisine, chambre, classe, médecin, parc), pas les scènes
  berlinoises. Attention : ajouter le japonais à `mots.json` lierait les trois langues
  dans le vérificateur, qui exige déjà l'espagnol pour chaque mot allemand.

### Décision 4 : les coûts et leur ordre

| Poste | Chiffre | Quand |
|---|---|---|
| Code et données jusqu'au palier 1 | 0 € (sessions Claude et Fable) | Tout de suite |
| **Voix ElevenLabs** (modèle v2, jamais Flash) | Mesuré : kana des mots N5 = 2 103 caractères, N4 = 2 210 (≈ 5 400 chacun avec porteuse) ; phrases N5 = 6 698, N4 = 6 960. **N5 + N4 complets ≈ 25 000 crédits**, plus ≈ 20 000 pour les parcours (estimation) → **un mois Creator, ≈ 22 $**, essai de 2 ou 3 voix compris | Après les cartes N5, quand tu auras écouté un échantillon. On génère **depuis les kana**, pas depuis les kanji (les lectures multiples font sinon dire le mauvais mot) |
| **Relecteur natif** | **Le gros poste.** Estimé le 4 oct. à 1 000-2 000 € pour N5-N3, hors grammaire. Pour le N5 seul, probablement 300-700 € (estimation, à faire chiffrer) | Avant d'ouvrir aux testeurs. **À chercher dès maintenant**, puisque c'est le délai le plus long |
| Images des scènes | 0,15 $ par scène (fal, mesuré). Une dizaine de scènes pour le voyage japonais ≈ 2 $ | Avec l'A1 voyage japonais |
| Pilote « l'image devient le kanji » (5 kanji) | < 1 $ (estimé le 7 oct.) | Avec les kanji N5, si tu le veux |
| Mosaïque | 0 € (domaine public) | Il ne manque que ton choix sur les planches |
| Épisodes vidéo | Non chiffré ici, de loin le plus cher par minute | **En dernier**, après le N5 et un natif (le script japonais doit être relu) |

---

## 5. Le plan proposé

| Étape | Contenu | Dépense | Ce qui la prouve |
|---|---|---|---|
| 0 | Ce document. Tu tranches les quatre décisions | 0 | — |
| 1 | Ranger : une branche `japonais`, regroupant les 8 branches, les scènes et la mosaïque. Cartographie des concurrents récupérée ou refaite | 0 | Inventaire refait, mêmes comptes qu'ici |
| 2 | Socle moteur, en essai admin | 0 | Parcours de-v954 et es-v944 à **0 écart**. `?apprendre=ja` ouvre un accueil vide, sans aucun mot allemand |
| 3 | Kana = Premiers pas japonais | 0 | Tu joues hiragana et katakana sur ton téléphone |
| 4 | Cartes N5 + séance du jour (voix du téléphone) | 0 | 667 cartes, furigana, progression dans `usuariosJa` |
| 5 | Voix japonaise : essai, ton choix, puis génération N5 | ≈ 22 $ | `controler_sons.py`, ton écoute |
| 6 | Kanji N5 : cartes, tracés KanjiVG, mnémoniques | 0 (pilote image < 1 $) | Tes jugements sur les 79 (ou 102) kanji |
| 7 | Parcours débutant : A1 voyage japonais, repères et compteurs, prononciation, conjugaison de base, exercices sur les particules, scènes | ≈ 2 $ d'images | Le parcours `ja` a sa référence |
| 8 | Natif sur le N5, puis ouverture à des testeurs japonais (à recruter : tes camarades du cours d'allemand ne sont pas ce public) | relecteur | Retours des testeurs |
| 9 | N4, mosaïque, fiche des stores, puis épisodes | voix N4 comprise dans l'étape 5, épisodes à chiffrer | — |

### Ce qui attend déjà ton avis (reste du 4 et du 7 oct.)

- Les **planches de la mosaïque** (`japonais/mosaique/planche-1..3.jpg`).
- Les **33 mnémoniques de kanji à juger** et les 7 à réécrire, dont 男 天 時 何 avec la
  règle « l'image mène au sens ». Le jugement avec le son (voix Nanami dans Edge) n'a
  jamais été fait.
- **Quelle liste de kanji N5 fait foi** : 79 (KANJIDIC2) ou 102 (avec l'ancien niveau 4).
- Les 92 mnémoniques de kana.
- Où vivent les données japonaises tant que le dépôt est public : le contenu payant d'une
  app vendue serait lisible par tous. Ce point rejoint le déménagement vers le dépôt
  privé.
