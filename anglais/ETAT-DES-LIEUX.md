# L'anglais dans Wortando : état des lieux et plan

27 octobre 2026, v982. Mandat de Jacques, transmis par le chef d'orchestre : « faire la
version pour apprendre l'anglais ». Rien n'a été supprimé, payé ni publié en écrivant ce
document. Chaque chiffre a été compté dans les fichiers ; une estimation est signalée
comme telle.

## Où on en est (mis à jour le 27 oct. 2026, au soir)

**Décidé par Jacques le 27 oct.** : anglais **américain par défaut, britannique en
variante** ; même moteur et même structure que l'allemand, l'espagnol et le japonais ;
mêmes images de scènes ; l'anglais se situe à **Boston**.

**Construit (branche `anglais`, essai admin)** :
- le **socle** : `?apprendre=en`, porte « ENGLISH — ESSAI ANGLAIS » dans l'Administration,
  garde (tout autre compte repart en allemand), liste blanche CSS, stockage `wortandoEn_`,
  Firestore `usersEn` / `resumesEn` (règles écrites dans `firestore.rules`, **à coller**),
  interface en français, choix « Quel anglais ? » (américain / britannique) dans les réglages ;
- le **corpus A1**, en deux jeux complets (`anglais/datos/` et `anglais/datos-gb/`) :
  **553 noms en 19 thèmes, 133 verbes** (formes calculées, irréguliers listés), **91
  adjectifs** (comparatif, superlatif), **41 adverbes, 55 expressions, 73 mots-outils** ;
  chaque mot a sa phrase d'exemple anglaise et sa traduction française ;
- la **grammaire A1** en français : **13 fiches** (to be, a / an / the, pluriel, présent
  simple, présent en -ing, pronoms et possessifs, there is, can, questions, in / on / at,
  adjectifs, prétérit, faux amis) et **126 questions** en 13 séries « M'entraîner » ;
- la **séance du jour** en anglais (mots seulement, comme le japonais à ses débuts).

**Ajouté en v984 (27 oct., au soir)** :
- **37 scènes** en anglais, à Boston (`anglais/outils/scenes.py` → `scene-<nom>.en.js`) :
  1 415 zones, dont 1 044 renvoient à une carte du corpus A1 ; couche « Les noms »
  (découvrir, trouver) ; ruban « Explorer les scènes » et scène du jour dans la séance.
  Les six scènes trop européennes sont écartées (décision de Jacques) ;
- **Premiers pas** : 8 étapes de voyage à Boston (arrivée, café, chemin, transports,
  hôtel, achats, santé, bavarder), 168 cartes, 70 phrases, un tableau de grammaire par étape ;
- **repères** : nombres jusqu'à 1000 (prononciation figurée), jours, mois, l'heure,
  couleurs, pluriel ;
- **prononciation** : 15 règles (i court et long, th, h, r, t américain, -s, -ed, accent
  tonique…), avec la version britannique du r et du t ; et le son du jour ;
- **feuilles de conjugaison A1** (to be, présent simple, -ing, can, was / were, prétérit) ;
- **cartes-phrases** dans la séance : écoute, oral, ordre, dictée et questions de grammaire
  anglaise, comme en allemand et en espagnol.

**Reste** (la mosaïque est faite, v1013) : les couches A2-C1 des scènes (questions
écrites pour l'anglais), l'A1 voyage, la voix (ElevenLabs, sur accord), puis la relecture
par un anglophone avant toute ouverture aux testeurs.

**Publié** : v983, le 27 oct. 2026 (parcours allemand 128 chemins et espagnol 77 chemins
à 0 écart). Pour l'essayer : Réglages → Administration → « ENGLISH — ESSAI ANGLAIS ».

### Les scènes à Boston : celles que l'image trahit (relevé du 27 oct., rien de généré)

Les 43 images ont été regardées. Celles-ci montrent l'Europe au point de ne pas passer
pour Boston :

| Scène | Ce qui trahit l'Europe |
|---|---|
| `kreuzung` (le carrefour) | Tout Berlin : tram et bus jaunes, arrêt « H », taxi Mercedes crème, deux boîtes aux lettres jaunes de la Deutsche Post, croix verte de pharmacie, colonne à affiches, piste cyclable rouge |
| `ubahn` (le métro) | Rame jaune et carrelage vert du U-Bahn berlinois, présentoir à bretzels (le métro de Boston est vert, orange, rouge ou bleu) |
| `zug` (le train) | Paysage bavarois par la fenêtre : Alpes, église à bulbe, champs de colza |
| `stadtplatz` (la place) | Tram jaune, église de brique gothique, boîte aux lettres jaune, façades à jardinières (la Green Line de Boston est verte) |
| `weihnachtsmarkt` (marché de Noël) | Marché de Noël allemand (bretzels, vin chaud, église de brique) : Boston en a, mais l'image reste très allemande |
| `post` (la poste) | Boîte aux lettres jaune derrière la vitre (américaine : bleue) ; l'intérieur passe |

Les autres passent pour Boston (intérieurs, marché, parc, plage, hiver…), parfois avec
un détail de second plan (bâtisse de brique rouge du `bauernhof`, bretzels de la
`baeckerei`) qui ne gêne pas. Le `buergeramt` (bureau des citoyens) n'a pas d'équivalent
américain : son image passe, mais il faudra lui donner un autre rôle (bureau de la ville,
DMV…).

## En bref

- **Un ancien module anglais dort dans `index.html`.** Il a été construit en août pour
  des germanophones, puis adapté aux francophones (v220-223). Il est **masqué pour tous
  depuis la v727** (`ANGLAIS_EN_RETRAIT = true`, décision du 10 oct. : l'espagnol a pris
  sa place). Personne ne le voit, ni testeur ni admin. Ses **données valent la peine
  d'être gardées** (≈ 450 fiches déjà écrites pour des francophones). Son **code, lui,
  n'a pas d'avenir** : c'est un second moteur, à côté du vrai.
- **Recommandé : le même moteur que l'espagnol et le japonais**, `index.html?apprendre=en`,
  en **essai réservé à l'admin** comme le japonais. L'anglais est bien plus proche de
  l'espagnol que le japonais : alphabet latin, mots, phrases, conjugaison. Il réutilise
  donc la carte, la séance, les exercices et les scènes, presque sans code neuf.
- **Le corpus A1 se dérive en grande partie de ce qui existe.** Chaque mot allemand et
  espagnol porte déjà sa traduction anglaise et une phrase d'exemple **traduite en
  anglais ET en français**. Union mesurée des deux corpus A1 : **≈ 680 noms, 160 verbes,
  140 adjectifs, 60 adverbes, 90 expressions**. Il faut les relire et les compléter, pas
  les inventer.
- **Variante, en attente de ta confirmation** : américain par défaut, britannique en
  variante, comme l'Espagne et l'Amérique latine. Les données sont conçues pour les deux.

---

## 1. L'ancien module anglais (mesuré)

### Ce qu'il est

| Pièce | Où | Chiffre |
|---|---|---|
| Axe « direction » | `getLearningDirection()` (28 appels), `data-learning-dir` sur `<body>`, clé `…learningDirection` | `LEARNING_DIRS = ["de", "en"]` |
| Interrupteur | `ANGLAIS_EN_RETRAIT = true` (v727) | Force `"de"` même si `"en"` est stocké |
| Tuiles | 14 tuiles `.orb-en` sur l'accueil (« Verben », « Adjektive », « Artikel », « Zeiten », « Modalverben », « Präpositionen », « Satzbau & Fragen », « Vergleich »… **titres encore en allemand**), dont 6 « bientôt » (`comingSoon`) | 22 occurrences de `orb-en` |
| Modules de cartes | `ENGLISH_MODULES` + `openEnglishModule()` | 6 modules, mode de carte `englishmodule` |
| Grammaire | `ENGLISH_GRAMMAR_CONTENT` + `artikelExercises` | ⚠️ `artikelExercises` est le jeu **anglais** (a / an / the), malgré son nom |
| Libellés | clés `en_module_*`, `orb_en_*`, `home_title_*_en_dir` | 253 lignes dans les dictionnaires |
| Progression | `progressKey()` isolait la progression par direction | — |

### Ses données (6 fichiers à la racine)

| Fichier | Contenu | A1 | A2 | B1 | B2 | Total |
|---|---|---|---|---|---|---|
| `english_themes.json` | mots par catégorie, glose fr + définition en anglais, exemple en + fr | 35 | 36 | 30 | — | **101** |
| `english_verbs.json` | verbes irréguliers, trois formes (`be → was/were → been`) | 25 | 35 | 25 | 15 | **100** |
| `phrasal_verbs.json` | `get up`, `give up`… | — | 31 | 42 | 16 | **89** |
| `english_pitfalls.json` | **faux amis** (`actually` ≠ actuellement) et pièges, avec `piege` en français | — | 18 | 26 | 14 | **58** |
| `english_expressions.json` | `It depends.`, `By the way`… | — | 16 | 22 | 10 | **48** |
| `english_britam.json` | paires GB / US (`flat 🇬🇧 / apartment 🇺🇸`) | — | 27 | 30 | — | **57** |

Total : **453 fiches**, toutes déjà pour des **francophones** (glose et phrase en français).

### Ce que je propose d'en faire (rien n'est supprimé sans ton accord)

| Pièce | Proposition |
|---|---|
| Les 6 fichiers JSON | **Récupérés** : versés dans le nouveau corpus (`anglais/datos/`), au niveau prévu. `english_britam.json` devient la base de la variante GB/US ; `english_pitfalls.json` devient la fiche et la série « Faux amis » ; `english_verbs.json` sert à vérifier les verbes irréguliers. Les originaux restent en place tant que le vieux code les lit. |
| Les 14 tuiles `.orb-en`, `ENGLISH_MODULES`, `openEnglishModule`, `ENGLISH_GRAMMAR_CONTENT`, `artikelExercises`, l'axe `getLearningDirection` | **À retirer, plus tard, sur ton accord**, une fois l'anglais du moteur en place. Ils sont invisibles aujourd'hui ; les retirer ne change rien pour personne, mais touche environ 30 fonctions : c'est un chantier propre, à faire sous contrôle des deux parcours, pas en passant. |
| Un lien gardé quelque part (favori, ancienne app) vers l'ancien anglais | Aucun : l'ancien module n'avait pas d'adresse, seulement une valeur stockée, déjà neutralisée par `ANGLAIS_EN_RETRAIT`. |

### ⚠️ La collision de noms

`data-learning-dir="en"` (sur `<body>`, l'ancien module) et `data-apprendre="en"` (sur
`<html>`, le moteur) n'ont rien à voir. Le premier ne vaut jamais `"en"` tant que
`ANGLAIS_EN_RETRAIT` est vrai. Règle tenue dans le code neuf : **on ne teste que
`LANGUE_APPRISE === "en"`**, jamais `getLearningDirection()`. Ne jamais remettre
`ANGLAIS_EN_RETRAIT` à `false`, sous peine de faire revivre deux anglais en même temps.

Un autre piège, plus subtil : partout, `_en` veut dire « **traduit** en anglais »
(`traduction_en`, `exemple_en`, `I18N.en`). Pour l'anglais appris, le mot vedette **est**
l'anglais. Le corpus anglais met donc le mot dans `mot` et l'exemple dans `exemple`, comme
l'espagnol, et n'a **pas** de champ `traduction_en`.

---

## 2. Le chemin recommandé : le même moteur

| Ce qu'il faut | Comme le japonais | Pour l'anglais |
|---|---|---|
| Adresse | `?apprendre=ja` | `?apprendre=en` |
| Porte | Réglages → Administration → « 日本語 — ESSAI JAPONAIS » | « ENGLISH — ESSAI ANGLAIS » |
| Garde | `gardeEssaiJaponais()` renvoie tout autre compte vers l'allemand | la même garde, étendue à `"en"` |
| Affichage | **liste blanche** CSS `html[data-apprendre="ja"]` | liste blanche `html[data-apprendre="en"]`, ouverte tuile par tuile |
| Stockage local | `wortandoJa_` | `wortandoEn_` |
| Firestore | `usersJa` / `resumesJa` | `usersEn` / `resumesEn` (**règles à coller par toi** ; sans elles, la progression reste sur l'appareil) |
| Données | `japonais/datos/` | `anglais/datos/` (même forme que `espanol/datos/`) |
| Table de langue | `LANGUE_JAPONAIS` | `LANGUE_ANGLAIS` (voix `en-US` ou `en-GB` du téléphone) |
| Libellés propres | `I18N_JAPONAIS` | `I18N_ANGLAIS` |

**Pourquoi une liste blanche, pas une liste noire comme l'espagnol.** Le moteur contient
78 tests `=== "es"` : tout ce qui n'est pas l'espagnol retombe sur l'allemand. Une tuile
oubliée montrerait donc de l'allemand à un anglophile. On ne montre que ce qui a son
contenu anglais, et on ouvre au fur et à mesure.

**L'allemand et l'espagnol ne doivent pas bouger d'un pixel** : les deux parcours
Playwright (`de-v959`, `es-v959`) à 0 écart avant chaque push.

---

## 3. Public et interface

- **Francophones d'abord, interface en français seulement.** Une interface anglaise pour
  apprendre l'anglais n'aurait pas de sens (la traduction d'un mot serait le mot lui-même).
- **Plus tard, à proposer** : l'anglais est la langue la plus demandée par les publics de
  nos autres interfaces (turc, ukrainien, persan, arabe, portugais, polonais, russe). Le
  corpus dérivé de l'allemand porte déjà ces traductions pour chaque mot (celles du mot
  allemand, de même sens) : c'est un marché à part, plus vaste que les francophones, qui
  coûterait surtout de la relecture. **À trancher après l'A1 français.**

---

## 4. Le contenu, par palier

Le palier 1, « **A1 complet** », reprend chaque porte qu'un débutant voit en allemand et
en espagnol :

| Contenu | Allemand A1 | Espagnol A1 | Anglais A1 : d'où il vient |
|---|---|---|---|
| Noms par thème | 465 (32 thèmes) | 506 | Union des deux : **≈ 680 têtes anglaises**, avec exemple en + fr. Regroupées par thème, dédoublonnées, relues |
| Verbes | 111 | 123 | Union ≈ **160**. Les formes (3ᵉ personne, prétérit, participe, -ing) sont **calculées**, et les irréguliers vérifiés contre `english_verbs.json` |
| Adjectifs | 104 | 88 | Union ≈ **140**, plus comparatif et superlatif calculés |
| Adverbes | 52 | 28 | Union ≈ **60** |
| Expressions | 68 | 39 | Union ≈ **90** |
| Mots-outils | — | 89 | **À écrire** : articles, pronoms, possessifs, prépositions, conjonctions, quantifieurs, mots interrogatifs |
| Grammaire en français | 19 rubriques | 17 fiches | **À écrire** : *to be* / *to have*, a / an / the, pluriel, présent simple et *do/does*, présent en *-ing*, pronoms et possessifs, *there is / there are*, *can*, prépositions de lieu et de temps, questions, **faux amis** (repris de `english_pitfalls.json`) |
| Séries d'exercices | 48 | 24 | **À écrire** pour chaque fiche A1 |
| Conjugaison | 42 feuilles | 28 | Feuilles A1 : *be*, *have*, présent simple, présent en *-ing*, *can* |
| Prononciation | 25 règles | 18 | **À écrire** : *th*, *h* aspiré, voyelles courtes et longues, *-s* et *-ed*, accent tonique, lettres muettes |
| Repères | 11 | 10 | Nombres, jours, mois, heure, couleurs, alphabet (épeler son nom) |
| Premiers pas | 8 étapes, 190 éléments | 8, 191 | **À écrire** sur le modèle espagnol |
| Scènes | 43 | 43 (mêmes images, `mots.json`) | **Les mêmes images et zones**, avec le mot anglais de chaque mot allemand (≈ 480 mots, dérivables de `traduction_en`, à relire). `construire.py` fera `scene-<scène>.en.js` |
| Mosaïque | 65 tableaux | 66 | **67 tableaux de peintres américains**, choisis par toi le 29 oct. (v1013) : `anglais/mosaique/` |
| Voix | Aurora (ElevenLabs) | Lolita / Monica | **ElevenLabs en américain, A1-A2** (accordé le 29 oct., `audio/generer_en.py`, `audio/mp3/en-us/`) ; le téléphone pour B1-C1 et pour le britannique |

Paliers suivants : A2 (les fichiers de l'ancien module sont surtout A2-B1 : phrasal verbs,
GB/US, expressions), puis B1-C1, sur le même modèle.

### Sources et licences

| Source | Licence | Usage |
|---|---|---|
| Nos corpus allemand et espagnol (phrases écrites par Wortando) | à nous | Base du corpus A1 dérivé |
| Leipzig Corpora Collection (anglais) | CC BY, attribution obligatoire | Classement par fréquence, comme `frequence.json` |
| WikDict (en-fr) | CC BY-SA | Dictionnaire intégré, comme l'allemand (surtout pas FreeDict, sous AGPL) |
| Tatoeba | CC BY 2.0 FR, auteur de chaque phrase à citer | Phrases d'appoint, si besoin |
| CMUdict | licence BSD | Vérifier la prononciation américaine |

Chacune s'ajoute à la carte « Crédits » le jour où elle entre dans l'app.

---

## 5. La variante : américain ou britannique ?

**Décidé par Jacques le 27 oct. 2026 : américain par défaut, britannique en variante**
(« Va pour l'anglais américain par défaut, avec le britannique en variante »). Comme
Espagne / Amérique latine :

- **Base américaine** : c'est l'anglais du plus grand nombre (Amérique du Nord, médias,
  internet), et celui que des Québécois entendent tous les jours.
- **Variante britannique** dans les réglages, qui change :
  - le **vocabulaire** (`apartment` → `flat`, `elevator` → `lift`, `fall` → `autumn`) : 44
    noms et 2 adjectifs de l'A1 ont leur mot britannique (`noms_a1.py`, drapeau `gb=`) ; les
    57 paires de `english_britam.json` (A2-B1) serviront au palier suivant ;
  - l'**orthographe** (`color` → `colour`, `center` → `centre`, `traveled` → `travelled`),
    par une liste de mots, pas par une règle (« -or → -our » casserait *doctor*) ;
  - la **voix** du téléphone (`en-GB` au lieu de `en-US`).
- Dans chaque mode, la carte cite l'autre forme en note (« 🇬🇧 flat »), comme la carte
  espagnole cite le mot d'Amérique latine.

Construit ainsi : deux jeux de données complets (`anglais/datos/`, `anglais/datos-gb/`),
mêmes mots dans le même ordre, pour que la progression suive quand on change de variante.

---

## 6. Le plan

| Étape | Contenu | Dépense | Ce qui la prouve |
|---|---|---|---|
| 0 | Ce document | 0 | — **fait** |
| 1 | **Socle** (**fait**), en essai admin : `?apprendre=en`, garde, liste blanche, stockage et Firestore à part, `LANGUE_ANGLAIS`, `I18N_ANGLAIS`, porte dans l'Administration | 0 | Parcours `de` et `es` à **0 écart**. `?apprendre=en` ouvre un accueil sans un mot d'allemand |
| 2 | **Corpus A1** (**fait**, à relire) dérivé et relu (`anglais/outils/construire.py` → `anglais/datos/`), variante US / GB | 0 | La séance du jour en anglais, cartes avec exemple et traduction |
| 3 | Grammaire A1 en français, faux amis, séries d'exercices (**fait**), feuilles de conjugaison (à faire) | 0 | Tuile Grammaire, séries jouables |
| 4 | Prononciation, son du jour, repères, Premiers pas | 0 | Le 🌱 d'un compte neuf en anglais |
| 5 | Scènes (mots anglais de chaque scène, à Boston) | 0 | Scènes jouables en anglais |
| 6 | Relecture par un anglophone, puis ouverture aux testeurs | relecteur, à chiffrer | Retours |
| 7 | Mosaïque (faite, v1013), voix ElevenLabs (ton accord), fiche des stores, A2 | voix à chiffrer | — |

Les étapes 1 à 5 se font sans dépense, une version à la fois, chacune poussée sur `main`
en essai admin après les deux parcours à 0 écart.

## 7. Ce qui t'attend

1. ~~Américain ou britannique comme base~~ : **décidé**, américain par défaut.
2. **Le sort de l'ancien module** : d'accord pour retirer ses tuiles et son code une fois
   l'A1 du moteur en place ? (Les données, elles, sont gardées.)
3. **Les règles Firestore `usersEn` / `resumesEn`** à coller dans la console, le jour où
   tu veux que la progression de l'essai suive d'un appareil à l'autre.
4. Plus tard : les autres interfaces (turc, ukrainien, arabe…), la voix, un
   relecteur anglophone.
