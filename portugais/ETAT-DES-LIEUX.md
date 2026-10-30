# Le portugais dans Wortando : état des lieux

29 octobre 2026. **Publié en v1026** (essai admin, A1) ; **A2 à C1 en v1027** (30 oct.). Mandat de Jacques, transmis par le chef d'orchestre : « une
version pour apprendre le portugais », et la base : « On va commencer par le
portugais du Portugal. » Rien n'a été payé ni généré. Chaque chiffre a été
compté dans les fichiers.

## En bref

- **Le socle et l'A1 sont construits**, en essai réservé à l'admin, dans le même
  moteur que l'allemand, l'espagnol, l'anglais et le japonais :
  `index.html?apprendre=pt`. Pour l'essayer : Réglages → Administration →
  « PORTUGUÊS — ESSAI PORTUGAIS ». Le même bouton ramène à la langue d'avant.
- **Portugais d'Europe partout** : casa de banho, autocarro, comboio, elétrico,
  pequeno-almoço, telemóvel ; « a minha mãe » avec l'article ; « estou a ler »
  et non « estou lendo » ; le pronom après le verbe (chamo-me, levanto-me) ;
  falámos avec l'accent au passé ; orthographe de l'Accord de 1990 (atual,
  receção, elétrico). Le mot brésilien est noté à part, pour plus tard.
- **L'action se situe à Lisbonne** (proposition, voir les questions) : Premiers
  pas, A1 voyage, consignes des scènes.
- **La voix** est celle du téléphone, en **pt-PT** (Joana, Catarina, Raquel,
  Duarte… ; une voix brésilienne seulement si l'appareil n'a aucune voix du
  Portugal), sans les voix fantaisie d'Apple. Aucune voix ElevenLabs : chiffrage
  plus bas.
- **L'allemand et l'espagnol n'ont pas bougé** : parcours de et es à 0 écart
  contre les références v1007 (voir « Vérifié »).

## Ce qui est construit

### Le moteur (`index.html`)

Sur le modèle de l'anglais, ligne à ligne :

| Pièce | Portugais |
|---|---|
| Adresse | `?apprendre=pt` (retenue sous `wortando_langueApprise`) |
| Porte | Réglages → Administration → « PORTUGUÊS — ESSAI PORTUGAIS » (`ouvrirEssaiPortugais`) |
| Garde | `gardeEssaiJaponais()` : tout autre compte que l'admin repart vers sa langue d'avant |
| Affichage | liste blanche CSS `html[data-apprendre="pt"]` : séance, mots (noms, verbes, adjectifs, adverbes), « Mis de côté », fiches de grammaire, feuilles de conjugaison, prononciation, Écouter, Écrire, « Quel article ? » |
| Table de langue | `LANGUE_PORTUGAIS` (voix `pt-PT`, données `portugais/`) |
| Libellés propres | `I18N_PORTUGAIS`, en français seulement (`UI_LANGS = ["fr"]`) |
| Stockage local | `wortandoPt_` |
| Firestore | `usersPt` / `resumesPt` — **règles à coller par Jacques** (`portugais/REGLES-FIRESTORE.md`) |
| Grammaire de la langue | celle de l'espagnol : articles `o / a`, pluriel `os / as`, six personnes avec **vós caché** (comme vosotros en Amérique latine), couleurs de der / die |
| Carte de verbe | `carteVerbePortugais` : présent et sa phrase ; déplié : perfeito, imperfeito, futuro, condicional, conjuntivo, imperativo (tu, você, vocês) |
| Carte d'adjectif | masculin · féminin · pluriels, comparatif, superlatif |
| Scènes | `scene-<nom>.pt.js`, page des scènes (`visuel/prototype/index.html`) : `?apprendre=pt`, voix pt-PT, « Certo! » |
| Séance | l'ordre du cours (17 séries), les petits mots connus d'avance, le socle (eu, sou, é, estou, tenho, vou…) |
| Parcours de contrôle | `python fusion-espagnol/parcours.py --app pt` relève ce que montre l'essai |

### Le corpus A1 (`portugais/datos/`, dérivé)

Fabriqué par `python portugais/outils/construire.py` à partir des listes de
`portugais/outils/`. Le brouillon vient du corpus espagnol A1, qui porte pour
chaque mot une traduction et une phrase **en portugais du Brésil** : chaque mot
et chaque phrase ont été **récrits en portugais d'Europe**, la traduction
française reprise ou ajustée.

| Contenu | Nombre |
|---|---:|
| Noms, avec article et pluriel (calculé, exceptions notées) | **510**, en 19 thèmes |
| Verbes, conjugués à 7 temps (`conjugaison.py`, irréguliers en table) | **120** |
| Adjectifs (féminin, pluriels, comparatif, superlatif) | **92** |
| Adverbes | **37** |
| Expressions | **61** |
| Mots-outils (articles, démonstratifs, possessifs, pronoms, interrogatifs, prépositions et contractions, conjonctions) | **91** |
| Fiches de grammaire en français | **17** |
| Questions d'exercices (une série par fiche) | **148** |
| Repères : nombres jusqu'à 1000 (prononciation figurée de Lisbonne), jours, mois, l'heure, couleurs, alphabet, genre (deux), pluriel | **11** |
| Règles de prononciation (e avalé, o en « ou », nasales, s en « ch », lh / nh, r, h, l, accent tonique) | **13** |
| Feuilles de conjugaison A1 | **6** |
| Premiers pas : 8 étapes à Lisbonne | **162** cartes, 64 phrases, un tableau par étape |
| A1 voyage : 12 escales, 2 étapes « installé », 8 de suite | 215 mots, 38 phrases toutes faites, 14 dialogues |
| Scènes `.pt.js` | **43** scènes, 1 644 zones, dont 1 129 reliées à une carte du corpus |
| Mots brésiliens notés (`variantes-br.json`) | 68 noms, 3 verbes, 7 adjectifs |

Les 17 fiches : ser / estar · o, a, um, uma · le pluriel · le présent ·
les irréguliers du quotidien · tu, você, o senhor · no, na, do, da · o meu, a minha ·
les questions · estar a + infinitif · ir + infinitif · le pronom après le verbe ·
gostar de · l'adjectif · le passé (perfeito) · há · les faux amis.

### A2 à C1 (30 oct. 2026)

Écrits par la session « Portugais : les niveaux A2 à C1 »
(`portugais/outils/niveaux.py` et ses listes `noms_<niv>.py`, `mots_<niv>.py`,
`grammaire_<niv>.py`, `temps_<niv>.py`… ; plan : `portugais/PLAN-A2-C1.md`),
appelés par `construire.py` après l'A1, qu'ils ne touchent pas.

| | A2 | B1 | B2 | C1 |
|---|---:|---:|---:|---:|
| Noms | 708 | 1 074 | 431 | 612 |
| Verbes | 321 | 436 | 189 | 127 |
| Adjectifs | 204 | 342 | 114 | 110 |
| Adverbes | 99 | 162 | 86 | 25 |
| Expressions | 79 | 94 | 118 | 53 |
| Fiches (questions) | 10 (130) | 10 (126) | 10 (122) | 9 (110) |

Plus 127 mots-outils, 36 feuilles de conjugaison, « S'entraîner par temps »
(12 séries, 193 questions) et les couches A2, B1, B2, C1 des 43 scènes
(`portugais/scenes/<scène>.json`, fusionnées par `scenes.py`). **Total : 3 335
noms, 1 193 verbes, 862 adjectifs, 56 fiches, 829 questions.**

Dans le moteur : les 39 séries A2-C1 dans l'ordre du cours de la séance,
« S'entraîner par temps » (comme l'anglais), et la carte de verbe montre, quand
ils existent, le perfeito composto, le mais-que-perfeito, les conjuntivos
imperfeito et futuro, le particípio et le gerúndio ; les subjonctifs se lisent
avec leur conjonction devant la personne (« que eu fale », « se ele se
levantasse », « quando tu chegares »). Essayé dans l'app : séances A2 et B1 carte par
carte, fiche B1 et sa série, par temps, verbe A2, couche A2 de la cuisine —
sans allemand ni erreur. Une passe anti-brésilianismes y a trouvé 9 entrées
(grama, abobrinha, tela, endereço, « tem » pour « há », « estou indo »),
signalées à la session A2-C1 pour correction à la source.

### Vérifié (29 oct. 2026)

- `python tests/verifier.py` : aucun problème (lancé avec `audio/mp3` relié au
  dépôt principal, comme l'exige un worktree).
- `node tests/syntaxe.js` : les 8 blocs `<script>` s'analysent.
- `parcours.py --app de` contre `de-v1007` : 128 chemins, **0 écart** ;
  `--app es-moteur` contre `es-v1007` : 77 chemins, **0 écart** (avant et après
  la mise à jour avec `main` et le passage en v1026).
- `parcours.py --app pt` : 42 chemins, aucune erreur JavaScript.
- Essai ciblé dans Chromium (Playwright, sans connexion) : Premiers pas s'ouvre
  sur « olá », les fiches et leurs séries se jouent, la carte de verbe montre
  les sept temps sans vós, « Quel article ? » propose o / a, la séance du jour
  sert « o quarto · os quartos », trois scènes s'ouvrent en portugais sans
  erreur.
- **Essai « apprenant » (nuit du 29 au 30 oct.)**, chaque carte composée affichée
  recto et verso : la séance d'un compte neuf (mots, feuille de conjugaison,
  escale 1 de l'A1 voyage et ses phrases toutes faites, questions de grammaire,
  scène, oral) ; la séance à l'escale 6 (phrases à trou, écoute, verbes,
  adjectifs) ; Premiers pas étape 1 et étape des transports (cartes, tableau,
  écoute, scène, phrase à construire) ; Écouter, dictée, « Mes feuilles »,
  recherche (casa, maison, comboio, Tisch), mode nuit, scène ouverte depuis le
  ruban (`apprendre=pt`). **Aucun texte allemand, aucune erreur JavaScript.**
  Corrigé : la recherche allait chercher le dictionnaire allemand (deux 404 par
  recherche) ; elle s'en passe désormais en portugais.
- **Pas vérifié** : sur un vrai téléphone (voix pt-PT réelle, iPhone), et le
  parcours connecté de l'admin (la garde et Firestore) — à faire par Jacques.

## Ce qui manque

1. ~~A2 à C1~~ : **fait** (nuit du 29 au 30 oct.) par la session « Portugais : les
   niveaux A2 à C1 », branché ici (voir « A2 à C1 » plus haut). Reste sa liste
   de cartes écartées faute d'avoir leur mot dans la phrase
   (`portugais/outils/rapport_niveaux.txt`, 437 cartes).
2. **La mosaïque** (des peintres portugais) : pas faite ici. Aujourd'hui,
   l'essai montre le tableau par défaut (allemand). Je vois une session
   « portugais-la-mosa-que-de » ouverte par le chef : à raccorder.
3. **La voix enregistrée** : chiffrage ci-dessous, rien de généré.
4. **La variante brésilienne** : les mots sont notés (`variantes-br.json`, la
   table des remplacements Portugal → Brésil qui servira de source),
   mais il manque les phrases, la conjugaison (você partout, gerúndio), la voix
   pt-BR et le choix dans les réglages, comme « Quel anglais ? ».
5. **Les à-côtés de l'anglais** : fréquence d'usage (Leipzig), mots voisins
   (un `synonymes.json` vide évite seulement une erreur 404), tuiles de grammaire
   (pronoms, prépositions…), « S'entraîner par temps », épisodes, dictionnaire
   intégré.
6. **L'ouverture à un compte** (comme « OUVRIR L'ANGLAIS » pour Daniel et
   Nicole) : pas faite ; l'admin seul entre.
7. **La relecture par un lusophone du Portugal** avant toute ouverture aux
   testeurs : tout est en brouillon (`statut: brouillon` sur les fiches).

## La voix enregistrée : chiffrage (rien de généré)

Mesuré par `python portugais/outils/chiffrage_voix.py`, qui ne fait que
compter : les textes que l'app dirait en portugais, dédoublonnés, avec la
porteuse des mots seuls (« Palavra: casa. »). Modèle multilingual v2,
1 caractère = 1 crédit.

| | textes | crédits |
|---|---:|---:|
| A1 portugais (mots, pluriels, formes, phrases, Premiers pas, A1 voyage, repères, prononciation, exercices) | 3 929 | **≈ 81 000** |
| Comparatif à l'aveugle de 4 ou 5 voix pt-PT (comme VOIX-A à E de l'anglais) | — | ≈ 1 500 |
| Marge de reprises (5 à 10 %) | — | 4 000 à 8 000 |

En repère : l'A1 anglais en demandait 89 919. Avant de générer, il faudrait
`audio/lectures/pt-pt.json` (7 textes A1 à chiffres : « o elétrico 28 »,
« o 112 », « o número 40 », « quarto 412 »…) et un `audio/generer_pt.py` sur le
modèle de `generer_en.py`. **Rien ne se fait sans l'accord de Jacques.**

## Les scènes à Lisbonne

Les 43 scènes ont leur version portugaise ; aucune n'est écartée. Lisbonne s'y
prête mieux que Boston : le **tram jaune** de la `kreuzung` et de la
`stadtplatz` est l'emblème même de Lisbonne (l'elétrico 28). Ce qui trahit
l'Allemagne, à regarder par Jacques :

| Scène | Ce qui trahit l'Allemagne |
|---|---|
| `zug` (le train) | Alpes et église à bulbe par la fenêtre |
| `weihnachtsmarkt` (marché de Noël) | marché de Noël allemand, bretzels, église de brique |
| `post` et `kreuzung` | boîtes aux lettres jaunes de la Deutsche Post (au Portugal, les CTT sont rouges) |
| `stadtplatz` | église de brique gothique, boîte aux lettres jaune (le tram, lui, passe) |
| `buergeramt` | rebaptisé « Na Loja do Cidadão », l'équivalent portugais |

Les consignes et textes des images disent « Lisbonne » là où l'allemand dit
« Berlin » (et « Porto » pour Hambourg).

## Les questions pour Jacques

Mises à jour le 30 oct. 2026 (le portugais va maintenant de l'A1 au C1, en v1027).

1. **Lisbonne** comme ville de l'action (Premiers pas, A1 voyage, scènes) : d'accord ?
2. **Les scènes** : garder les 43, ou écarter `zug`, `weihnachtsmarkt`, `post` comme pour l'anglais ?
3. **Les règles Firestore** `usersPt` / `resumesPt` : à coller (`portugais/REGLES-FIRESTORE.md`), le jour où tu veux que la progression suive d'un appareil à l'autre. Sans elles, l'essai marche, mais la progression reste sur l'appareil.
4. **La voix ElevenLabs** pour l'A1 (≈ 81 000 crédits, plus un comparatif à l'aveugle d'environ 1 500) : quand tu le voudras. L'A2 doublerait à peu près la somme.
5. **Un relecteur du Portugal** : en connais-tu un ? Tout est en brouillon, de l'A1 au C1.
6. **« Tu » ou « o senhor »** : les cartes tutoient entre proches et vouvoient (o senhor / a senhora) au guichet, comme on le fait au Portugal ; « você », délicat là-bas, n'est enseigné qu'en passant. D'accord ?
7. **Ouvrir l'essai à quelqu'un** (comme l'anglais pour Daniel et Nicole) : à qui, et quand ? Le bouton n'existe pas encore pour le portugais.
8. **La mosaïque portugaise** (des peintres du Portugal) : préparée par une autre session ; en attendant, l'essai montre le tableau par défaut.

## Commandes

```
python portugais/outils/construire.py          (tout : corpus, fiches, parcours, scènes)
python portugais/outils/scenes.py kueche       (une scène seule)
python portugais/outils/conjugaison.py ter     (voir une conjugaison)
python portugais/outils/chiffrage_voix.py      (le chiffrage de la voix)
python fusion-espagnol/parcours.py --app pt --sortie releve-pt.json
```
