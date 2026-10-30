# Le portugais dans Wortando : état des lieux

29 octobre 2026. **Publié en v1026** (essai admin, A1) ; **A2 à C1 en v1027** (30 oct.), complété en **v1029** (cartes reprises, séries allongées, brésilianismes corrigés) ; **v1032** (30 oct.) : Lisbonne confirmée, l'hiver écarté, la **variante du Brésil** (Réglages → « Quel portugais ? »), la **mosaïque portugaise** (66 tableaux). Mandat de Jacques, transmis par le chef d'orchestre : « une
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
- **L'action se situe à Lisbonne** (décidé par Jacques le 30 oct. : « On prend
  la ville de Lisbonne comme ville d'action. ») : Premiers pas, A1 voyage,
  consignes des scènes, phrases des cartes. Vérifié : aucune autre ville ne
  prend sa place (Berlin ne reste que dans « o Muro de Berlim »).
- **La variante du Brésil** (décidée le 30 oct.) : Réglages → « Quel portugais ? »
  → Portugal 🇵🇹 (la base) ou Brésil 🇧🇷. Deux jeux de données, mêmes mots dans
  le même ordre, comme l'américain et le britannique de l'anglais. Brouillon ;
  liste de relecture : `portugais/RELECTURE-BRESIL.md`.
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
| Firestore | `usersPt` / `resumesPt` — **règles publiées le 30 oct.** par le chef d'orchestre (`portugais/REGLES-FIRESTORE.md`) ; la variante du Brésil partage ces collections |
| Variante | `VARIANTE_PORTUGAIS` (`pt` ou `br`, sous `wortandoPt_variante`), `choisirVariantePortugais()` ; `DOSSIER_PORTUGAIS` = `datos/` ou `datos-br/` (grammaire et exercices compris) ; voix pt-PT ou pt-BR ; scènes avec `variante=br` |
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
| Scènes `.pt.js` | **42** scènes (l'hiver écarté le 30 oct.), 1 614 zones, dont 1 363 reliées à une carte du corpus |
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
(`portugais/scenes/<scène>.json`, fusionnées par `scenes.py`). En v1027 : 3 335
noms, 1 193 verbes, 862 adjectifs, 56 fiches, 829 questions.

**v1029** : les cartes écartées faute de phrase sont reprises (351 phrases
écrites, `phrases_niveaux.py` ; 83 mots retirés), les séries allongées (287
questions écrites, 395 tirées des phrases des cartes), les 9 brésilianismes
corrigés. **Total : 3 522 noms, 1 214 verbes, 991 adjectifs, 425 adverbes, 405
expressions, 218 mots-outils, 56 fiches, 1 511 questions ; 1 387 zones de
scènes reliées à une carte.** Plus aucune carte sans son mot dans sa phrase.

Dans le moteur : les 39 séries A2-C1 dans l'ordre du cours de la séance,
« S'entraîner par temps » (comme l'anglais), et la carte de verbe montre, quand
ils existent, le perfeito composto, le mais-que-perfeito, les conjuntivos
imperfeito et futuro, le particípio et le gerúndio ; les subjonctifs se lisent
avec leur conjonction devant la personne (« que eu fale », « se ele se
levantasse », « quando tu chegares »). Essayé dans l'app : séances A2 et B1 carte par
carte, fiche B1 et sa série, par temps, verbe A2, couche A2 de la cuisine —
sans allemand ni erreur. Une passe anti-brésilianismes y a trouvé 9 entrées
(grama, abobrinha, tela, endereço, « tem » pour « há », « estou indo »),
corrigées à la source en v1029.

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
   niveaux A2 à C1 », branché ici (voir « A2 à C1 » plus haut), complété en v1029.
2. ~~La mosaïque~~ : **branchée en v1032** — les 66 tableaux choisis par
   Jacques (`portugais/mosaique/app/`, session « portugais-la-mosa-que-de »),
   `MOSAIQUE_BASE` du portugais ; les mêmes pour le Portugal et le Brésil. Les
   tableaux brésiliens attendent le choix de Jacques sur sa page ; le code
   de la session mosaïque (commit aaaa318 : `mosaiques-bresil.json`, images
   `brNN.jpg`) sera branché sur la variante Brésil une fois la liste cochée.
3. **La voix enregistrée** : chiffrage ci-dessous, rien de généré.
4. ~~La variante brésilienne~~ : **faite en brouillon** (v1032, voir « La
   variante du Brésil » plus bas). Reste la relecture par un Brésilien, et
   « você » à la place de « tu » si le relecteur le demande.
5. **Les à-côtés de l'anglais** : fréquence d'usage (Leipzig), mots voisins
   (un `synonymes.json` vide évite seulement une erreur 404), tuiles de grammaire
   (pronoms, prépositions…), « S'entraîner par temps », épisodes, dictionnaire
   intégré.
6. **L'ouverture à un compte** : non voulue pour l'instant (Jacques, 30 oct. :
   « on n'ouvre pas l'essai à quelqu'un pour le moment ») ; le bouton n'est pas
   construit, l'admin seul entre.
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

L'**hiver** (`winter`, le bonhomme de neige d'Anna) est **écarté** du portugais
(décision de Jacques, 30 oct.) : `SCENES_ECARTEES_PORTUGAIS` dans le moteur,
`EXCLUES` dans `scenes.py`. Il reste 42 scènes (38 dans le ruban et le panneau,
les marchés et l'examen ayant plusieurs vues). Les autres, passées une à une à
l'œil d'un Portugais :

| Scène | Avis | Pourquoi |
|---|---|---|
| `winter` (l'hiver) | **écartée** | neige et bonhomme de neige : Lisbonne n'en a pas |
| `weihnachtsmarkt` (marché de Noël) | **à demander** (je penche pour écarter) | neige au sol, vin chaud, chalets de bois, église de brique : un marché allemand |
| `zug` (le train) | **à demander** (je penche pour écarter) | par la fenêtre, les Alpes et une église à bulbe bavaroise ; l'intérieur passerait |
| `ubahn` (le métro) | **à demander** | rame jaune et carrelage vert : le métro de Berlin (celui de Lisbonne est blanc et bleu, avec des azulejos) |
| `kreuzung` (le carrefour) | **à demander** (je penche pour garder) | le tram jaune est lisboète ; la colonne Morris, la boîte aux lettres jaune et les façades, berlinoises |
| `stadtplatz` (la place) | **à demander** (je penche pour garder) | église gothique de brique (Allemagne du Nord) ; le tram jaune et les pavés passent |
| `post` (la poste) | garder | seul détail : la boîte jaune à l'extérieur (celles des CTT sont rouges) |
| `bauernhof` (la ferme) | garder | maison de brique et pins, plutôt du Nord, mais plausible dans le Minho |
| `camping` | garder | un lac et des pins : l'Alqueva ou la serra |
| `strand` (la plage) | garder | falaises et phare : l'Algarve |
| `markt-*` (les quatre étals) | garder | un marché ; la rhubarbe et les groseilles de `markt-obst-heimisch` sont rares au Portugal, sans gêner |
| `sportplatz` (le foot) | garder | le football est roi au Portugal |
| `park` (le parc) | garder | tulipes et lac : un jardin de Lisbonne (Estrela) |
| `buergeramt` | garder | bureau neutre, rebaptisé « Na Loja do Cidadão » |
| `fahrradwerkstatt` (l'atelier vélo) | garder | Lisbonne pédale moins (les collines), mais l'atelier existe |
| `waschsalon` (la laverie) | garder | les lavandarias self-service sont courantes à Lisbonne |
| `flughafen` | garder | titré « No aeroporto de Lisboa » |
| les intérieurs (cuisine, chambre, salon, classe, bureau, hôtel, musée, restaurant, café, boulangerie, boutique, coiffeur, pharmacie, médecin, examen, famille, fête, musique, bibliothèque, bricolage, déménagement, supermarché) | garder | aucun signe de pays |

**Pour le Brésil** (questions pour Jacques, rien de tranché) : la **ville** (les
phrases disent encore Lisbonne, avec des euros) et les **scènes à écarter** (la
neige est déjà partie ; le marché de Noël, le train des Alpes et le métro de
Berlin y sont aussi peu crédibles).

## La variante du Brésil (30 oct. 2026)

Les sources du cours sont écrites en portugais d'Europe. La variante est donc
**dérivée** de `portugais/datos/` par `portugais/outils/bresil.py`, appelé par
`construire.py`, vers `portugais/datos-br/` (14 fichiers, mêmes mots dans le même
ordre). Ce que fait la conversion, en une passe :

- **le vocabulaire** : 86 cartes de noms changées (comboio → trem, autocarro →
  ônibus, pequeno-almoço → café da manhã, casa de banho → banheiro, telemóvel →
  celular, paragem → ponto…), l'article accordé quand le genre change (a paragem
  → o ponto) ; les verbes perceber → entender, conduzir → dirigir, apanhar (un
  transport) → pegar, registar → registrar, planear → planejar, magoar →
  machucar ;
- **l'orthographe** : econômico, tênis, Antônio, bebê, fato, contato, recepção,
  registro, úmido, dezesseis… ; falamos (passé) sans accent ; aceito ;
- **la syntaxe** : estar a + infinitif → gérondif (estou lendo), le pronom devant
  le verbe (me chamo, vou me deitar, te darei), « Minha mãe » en tête de phrase,
  ter que ;
- **ce qui ne se convertit pas, écrit à la main** (`bresil_textes.py`) : 72
  explications qui opposaient le Portugal au Brésil, 15 fiches (titre, résumé,
  tableau), 4 séries d'exercices (estar + gérondif, le pronom, le se
  impersonnel, « Brésil ou Portugal ? »), la prononciation (11 règles : te / de
  en « tchi / dji », l final en « ou »…), la prononciation figurée des nombres,
  les titres de 12 scènes ;
- **ce qui ne passe pas** : 145 questions qui enseignent un usage du Portugal ou
  que la conversion casserait (liste dans `portugais/outils/rapport_bresil.txt`).

Dans le moteur : `VARIANTE_PORTUGAIS`, le choix dans les réglages, la voix
pt-BR (le Portugal à défaut), `lang="pt-BR"` sur les cartes, la reconnaissance
vocale pt-BR, les scènes avec `variante=br` (le champ `br` de chaque zone et
des questions A2-C1, ou `omettre` quand la conversion ne sait pas faire).

**Signalé, pas corrigé** : « tu » et sa conjugaison restent (77 phrases) ; les
pronoms o / a après le verbe (« comprá-lo », correct à l'écrit) ; 60 phrases où
le nom a changé de genre et dont l'adjectif n'est pas vérifié.

**Corrigé au passage dans le portugais du Portugal** : quatre phrases A2-C1
où la conversion de la nuit avait collé « nos » au mot d'avant (« último-nos
anos », « próximo-nos dias », « mínimo-nos detalhes ») et « o ordem » (a ordem).

## Les questions pour Jacques

Mises à jour le 30 oct. 2026, après ses réponses (Lisbonne, l'hiver, le Brésil,
les règles publiées, pas d'ouverture de l'essai).

1. **Les scènes à demander** pour le Portugal : `weihnachtsmarkt` et `zug` (je
   penche pour les écarter), `ubahn`, `kreuzung`, `stadtplatz` (voir le tableau
   des scènes).
2. **La ville du Brésil** : garder Lisbonne (un Brésilien en voyage) ou en
   choisir une (São Paulo, Rio) ? Aujourd'hui, les phrases disent Lisbonne et
   les prix sont en euros.
3. **Les scènes à écarter pour le Brésil**, au-delà de l'hiver.
4. **Tu ou você au Brésil** : la conversion garde « tu » ; le relecteur dira s'il
   faut tout passer à « você ».
5. **La voix ElevenLabs** pour l'A1 du Portugal (≈ 81 000 crédits, plus un
   comparatif à l'aveugle d'environ 1 500) ; le Brésil en demanderait autant.
6. **Un relecteur du Portugal** : tout le portugais d'Europe est en brouillon, de
   l'A1 au C1. (Pour le Brésil, l'ancien étudiant de Jacques : liste prête,
   `portugais/RELECTURE-BRESIL.md`.)
7. **Les tableaux brésiliens** : une collection à part pour la variante du Brésil, ou mêlés aux 66 du Portugal ?

## Commandes

```
python portugais/outils/construire.py          (tout : corpus, fiches, parcours, scènes)
python portugais/outils/scenes.py kueche       (une scène seule)
python portugais/outils/conjugaison.py ter     (voir une conjugaison)
python portugais/outils/chiffrage_voix.py      (le chiffrage de la voix)
python fusion-espagnol/parcours.py --app pt --sortie releve-pt.json
```
