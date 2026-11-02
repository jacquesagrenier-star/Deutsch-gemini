# L'anglais pour les hispanophones : état des lieux et plan

**2 nov. 2026.** Demande de Jacques, transmise par le chef d'orchestre : « j'aimerais
qu'une autre session s'occupe de préparer l'apprentissage de l'anglais pour les
Espagnols ». L'anglais appris (`index.html?apprendre=en`, essai admin) reçoit une
**interface et des explications en espagnol**. L'espagnol devient langue d'interface
**pour l'anglais seulement**.

Modèle : l'interface allemande de l'espagnol (v1065, `espanol/de/AVANCEMENT.md`), dont
on copie la démarche : extraire les textes, les faire traduire par lots contrôlés, les
poser par des scripts qui vérifient, puis brancher le code.

Rien n'a été payé. Chaque chiffre a été compté dans les fichiers le 2 nov. (scripts de
comptage hors du dépôt).

## Où on en est

**Palier 1 (2 nov. 2026, fait, en attente de publication)** : « es » est branché pour l'anglais
appris seulement, et l'interface est traduite en espagnol neutre (1 607 clés d'`I18N` +
58 d'`I18N_ANGLAIS`, deux agents Fable, `poser_autres.py controle` 0 faute). Le code de
l'anglais qui écrivait du français en dur passe par `t()` ou une table espagnole : libellés
des formes sur les cartes de verbes et d'adjectifs, « Quel anglais ? », familles
d'expressions (`FAMILLES_ANGLAISES_ES`), titres courts des scènes (`SCENES_COURTS.es`).
Captures jour et nuit au téléphone simulé : accueil, carte de verbe. Parcours `de` et
`es-moteur` à 0 écart, parcours `en` (interface française) à 0 écart contre le relevé pris
avant (`~/.wortando/anglais-es/en-avant.json`, étalonné deux fois).

| Outil | Rôle |
|---|---|
| `python anglais/es/extraire.py` | sort les textes à traduire → `anglais/es/sources/` |
| `python anglais/es/poser_autres.py controle \| pose` | contrôle les lots `anglais/es/lots/*.es.json`, puis les pose dans `index.html` |
| `anglais/es/CONSIGNES.md` | consignes et glossaire des traducteurs (espagnol neutre, « À trancher ») |
| `python tests/francais_ailleurs.py --app en` | le français resté à l'écran en interface espagnole (étendu le 2 nov.) |
| `tests/verifier.py`, `verifier_espagnol_anglais` | `I18N_ANGLAIS.es` complet |

**Publié en v1070** (2 nov. 2026, essai admin) : Réglages → Administration → « ENGLISH —
ESSAI ANGLAIS », puis Réglages → Langue → « 🌎 Español ».

### Les deux espagnols (décision de Jacques, 2 nov. 2026)

« On va faire les deux. Pour Amérique latine et Espagne. » L'usager choisit dans Réglages →
Langue → « ¿Qué español? » (visible quand l'interface est « Español »), comme « Quel portugais ? ».

**La base est l'Amérique latine, l'Espagne en est dérivée.** Pourquoi dans ce sens :
- c'est le **défaut** : la variante que lisent le plus d'usagers doit être celle qui ne dépend
  de rien (une table oubliée ne touche que l'Espagne) ;
- le palier 1 était déjà écrit en **espagnol neutre**, d'où l'Amérique latine se tire par une
  vingtaine de retouches (agregar, Configuración, alcaldía) ; l'Espagne diffère par peu de
  chose dans une interface qui tutoie un seul usager (vocabulaire, passé récent) ;
- c'est le geste du portugais (`I18N_PORTUGAIS_BRESIL` par-dessus le Portugal) : une table de
  différences, jamais deux traductions complètes.

| Où | Amérique latine (base) | Espagne (différences) |
|---|---|---|
| Interface | `I18N.es` + `I18N_ANGLAIS.es` (lots `anglais/es/lots/`) | `I18N_ES_ESPAGNE`, généré par `python anglais/es/espagne.py pose` depuis la table `INTERFACE` de `anglais/es/espagne.py` (28 clés : Ajustes, añadir, coger el tren, la compra, estantería, ayuntamiento, el tiempo, bricolaje, COMPROBAR, « Has escrito », « Enhorabuena ») |
| Drapeau, prix, voix | 🇲🇽, `es-419`, `es-MX` | 🇪🇸, `es-ES`, `es-ES` |
| Corpus (palier 2) | `traduction_es` / `exemple_es` | une table de mots (coche, ordenador, móvil, zumo, conducir…) appliquée à la pose, plus les phrases à réécrire (vosotros quand une phrase s'adresse à plusieurs) |

Stockage du choix : `wortandoEn_varianteEs` (« latam » par défaut, « es »).

**Reste au palier 2** (relevé par `francais_ailleurs.py`) : tout ce qui vient des **données**
anglaises reste en français — traductions des cartes, prononciation, titres et contenu des
fiches, tuiles, feuilles de conjugaison, Premiers pas, A1 voyage, repères — et la page des
scènes, qui ne connaît pas encore « es » (elle afficherait l'anglais).

---

## 1. Le piège du code « es » : recensement et choix

### Ce que « es » veut déjà dire dans le moteur

| Où | Sens de « es » | Lu par |
|---|---|---|
| `LANGUE_APPRISE === "es"` (101 tests), `html[data-apprendre="es"]` (CSS) | l'espagnol **appris** | `LANGUE_APPRISE` |
| Tables par langue apprise : `SOCLE_PHRASES`, articles, mots-outils de la dictée, séries, `EPISODES`, `EPISODES_SERIE`, `CLIPS_EN_ATTENTE`, `nombreEnMots(n, "es")`, `chiffresEnMots()` | l'espagnol **appris** | `LANGUE_APPRISE` |
| `scene-<nom>.es.js` | la scène de l'espagnol **appris** | nom de fichier |
| `VARIANTE_ESPAGNOL` : `"es"` / `"latam"` | l'**Espagne** (variante de l'espagnol appris) | stockage `wortandoEs_variante` |
| Stockage `wortandoEs_`, Firestore `usuariosEs` / `resumenesEs`, lien `apprendre=es` | l'app espagnole | `PREFIXE_STOCKAGE` |
| `praesens.er_sie_es` dans `anglais/datos/verbes.json` (1 196 fois) | le pronom allemand « es » | — (piège d'outil seulement) |

### Pourquoi le piège de « de » ne se reproduit pas tel quel

Le piège de « de » venait de ce que le moteur appelle **en interne « de » la langue
apprise, quelle qu'elle soit** : la voix (`pickVoice("de")`), l'écoute (`cible: "de"`),
l'index de recherche (`entry.de`), les phrases (`ph.de`). Une interface « de » y
rencontrait la langue apprise. **« es » n'a pas ce double rôle** : il n'apparaît comme
langue apprise que par `LANGUE_APPRISE`, ses tables et ses fichiers, jamais par
`getUiLang()`. Vérifié : les 12 lignes qui lisent `[getUiLang()]` de `index.html` (drapeau,
vidéo d'accueil, dictionnaire, locales, scènes courtes, sens des Premiers pas, remarques…)
visent des tables indexées par la langue d'**interface**, et aucune n'a de clé « es » au
sens de l'espagnol appris. Les données anglaises n'ont aucune clé `"es"` ni aucun champ
`_es` (hors `er_sie_es`). La voix est même juste d'emblée : `voicesForLang("es")` filtre
les voix `es-*` du téléphone, ce qui est exactement la voix de l'espagnol **connu**.
L'audio enregistré (`AUDIO_BASE`) ne sert que la langue apprise.

La seule combinaison interdite est **interface « es » + espagnol appris** (comme
« de » + allemand appris) : la traduction d'un mot serait le mot lui-même. Elle est
fermée par `UI_LANGS`, qui ne proposera « es » qu'à l'anglais appris.

### Décision (de la session) : garder le code ISO « es »

Un code distinct (« es-ui », « hi »…) casserait ce qui marche tout seul avec « es » :
la détection de la langue du téléphone (`navigator.languages` → « es »), `<html lang="es">`
(césure, voix, majuscules), les locales des prix (`Intl`), les étiquettes de voix, et la
convention `_es` / `Es` que lisent `texteTraduit()`, `valeurTraduite()` et les outils.
On garde donc « es », avec une garde et des parades nommées :

| Piège réel | Parade |
|---|---|
| Le repli habituel passe par l'**anglais** (`REPLI_LANGUE` : xx → en → fr). Dans l'app anglaise, l'anglais est la langue **apprise** : un texte espagnol manquant afficherait de l'anglais là où l'on attend le sens, ou du français déguisé (`translation_en` des exercices anglais contient… le français) | `REPLI_LANGUE.es = ["es", "fr"]` ; page des scènes : `REPLI.es` idem ; `tests/verifier.py` exige 100 % d'espagnol partout où le français existe |
| `er_sie_es` ressemble à un champ espagnol | les outils listent les champs posés par nom exact, jamais par suffixe |
| `scene-<nom>.es.js` = scène de l'espagnol appris | l'espagnol des scènes anglaises va **dans** `scene-<nom>.en.js` (champs `_es`), jamais dans un fichier `.es` |
| Le dictionnaire retombe sur la paire `de-en` (`DICT_PAIRS_PAR_LANGUE`) | rester caché en anglais, comme aujourd'hui (à vérifier à l'écran) |
| Les outils génériques (`tests/fusion_langue.py`, `tests/dico_interface.py`) cherchent `es: {` et tomberaient sur `SOCLE_PHRASES` | outils propres dans `anglais/es/` (comme `espanol/de/`) |
| La voix de l'espagnol connu n'a pas d'étiquette | `LANGUE_TAG.es`, `VOICE_PREFEREES.es`, une ligne « Espagnol » dans les réglages des voix |
| Un téléphone en espagnol ouvre l'app **allemande** en anglais (« es » absent de son `UI_LANGS`) | inchangé : l'allemand ne bouge pas |

---

## 2. Ce qu'il faut produire (compté le 2 nov.)

| Bloc | Source | Compte | Mots fr/en à traduire (≈) | Déjà en espagnol |
|---|---|---|---|---|
| Interface | `I18N.fr` | **1 607 clés** | 10 000 | 0 |
| Interface propre à l'anglais | `I18N_ANGLAIS.fr` | 48 clés | 500 | 0 |
| Corpus : noms | `themes.json` | 3 296 | | |
| Corpus : verbes | `verbes.json` | 1 196 | | |
| Corpus : adjectifs | `adjectifs.json` | 1 047 | | |
| Corpus : adverbes | `adverbes.json` | 414 | | |
| Corpus : expressions | `expressions.json` | 592 | | |
| Corpus : mots-outils | `fonctionnels.json` | 212 | | |
| **Corpus, total** (`traduction_es` + `exemple_es`) | | **6 757** | **57 000** | **1 840 phrases** (27 %) sont des traductions anglaises de phrases de notre corpus espagnol : leur espagnol existe, écrit par Wortando ; **3 298 mots** ont un candidat espagnol (à relire, polysémie) |
| Exercices (100 séries, dont les 12 séries par temps) | `exercices.json` | **3 284 questions** | 42 000 (traductions 24 800, explications 17 500) | 0 |
| Fiches de grammaire | `grammaire.json` `fiches` | **66 fiches**, 2 631 textes | 18 600 | 0 |
| Écrans de grammaire, temps, tuiles | `grammaire.json` `textes`, `temps`, `tuiles` | 112 + 60 + 218 textes | 1 700 | 0 |
| A1 voyage | `a1-voyage.json` | 646 textes | 4 000 | |
| Premiers pas | `premiers-pas.json` | 546 textes | 2 200 | |
| Feuilles de conjugaison | `conjugaison.json` | 384 textes | 3 000 | |
| Repères | `reperes.json` | 103 textes | 400 | |
| Prononciation | `prononciation.json` | 30 textes (15 règles) | 700 | 0 |
| Scènes (37, Boston) | `scene-*.en.js` + `anglais/scenes/*.json` | **2 028 textes distincts** (417 mots, 898 sens, 536 notes, 106 titres, 37 descriptions, 34 consignes) | 15 000 | le mot espagnol de chaque mot allemand des scènes existe (`visuel/prototype/espanol/mots.json`, 478) |
| Page des scènes | `TEXTES` de `visuel/prototype/index.html` | ≈ 40 clés | 300 | |
| Mosaïque anglaise | `anglais/mosaique/app/peintres.json` | 19 notices | 2 000 | |

**Au total ≈ 155 000 mots**, soit un peu plus que le chantier allemand (corpus 3 898,
exercices 1 343, fiches 17). Les explications ne se **traduisent** pas : elles se
**réécrivent contre l'espagnol** (section 4).

`anglais/datos-gb/` suit sans travail de plus : mêmes mots, même ordre ; ses phrases
diffèrent par l'orthographe et quelques mots, pas par le sens. Le pas qui fait le
britannique recopiera l'espagnol de l'américain.

---

## 3. Comment (copie de la chaîne allemande, adaptée aux données dérivées)

Différence de fond avec l'allemand : `espanol/datos/` était la **source**, on y posait
les champs directement. `anglais/datos/` est **dérivé** de `anglais/outils/` : tout ce
qui y serait posé à la main disparaîtrait au prochain `construire.py`. D'où :

| Étape | Outil |
|---|---|
| Sortir les textes à traduire | `python anglais/es/extraire.py` → `anglais/es/sources/` (chaque texte avec sa **clé stable** : le texte anglais lui-même, ou `id de fiche + champ`) |
| Pré-remplir ce qui existe | les 1 840 phrases retrouvées dans le corpus espagnol, et les 478 mots des scènes, proposés comme « déjà là » (relus, pas recopiés aveuglément) |
| Traduire | lots dans `anglais/es/lots/` ; consignes `anglais/es/CONSIGNES.md` (glossaire, « écrire contre l'espagnol ») |
| Contrôler un lot | `python anglais/es/poser.py controle <lot>` (même garde-fous que l'allemand : la colonne témoin doit correspondre, balises intactes, pas de français ni d'anglais resté, pas deux cartes à la même réponse) |
| Ranger | `anglais/es/traductions/*.json` : la **mémoire de traduction** (clé anglaise → espagnol). C'est elle, la source. |
| Construire | `anglais/outils/construire.py` lit la mémoire et pose `traduction_es`, `exemple_es`, `translation_es`, `explanation_es`, `es` des fiches… dans `datos/` **et** `datos-gb/` ; `scenes.py` pose les `_es` des scènes |
| Ce qui manque | une phrase anglaise changée plus tard n'a plus sa clé : `extraire.py` la ressort, `tests/verifier.py` la signale |

Le code (`index.html`, page des scènes) se branche comme pour « de » : `UI_LANGS`
(anglais = fr, **es**), `SUFFIXE_LANGUE`, `SUFFIXE_CHAMEAU`, `DRAPEAUX_LANGUE`,
`REPLI_LANGUE` (es → fr), `RANGS_CARTE` (rangs ajoutés **en anglais seulement**),
`RANGS_PP`, `NOM_LANGUE_NATIF` (« Español »), `LOCALES_ABO`, `LANGUE_TAG`, bouton
« Español » caché hors de l'anglais, bloc `es:` d'`I18N` et d'`I18N_ANGLAIS`.

**Le travail de traduction** est confié à des agents (Fable, quota séparé, comme le veut
Jacques), **deux à la fois au plus**, dans l'ordre ci-dessous, chacun avec les consignes et
l'interdiction de toucher à autre chose que `anglais/es/lots/`. Moi : outils, contrôles,
branchement, vérification à l'écran, publication.

### Les paliers

| Palier | Contenu | Preuve |
|---|---|---|
| 0 | Ce plan ; décision de Jacques sur l'espagnol (section 5) | — |
| 1 | Outils (`extraire`, `poser`, mémoire, `construire.py`), branchement de « es » dans le code, **interface complète** (1 607 + 48 clés) | réglages → « Español » en anglais seulement ; parcours `de` et `es-moteur` à 0 écart ; parcours `en` (français) à 0 écart contre un relevé pris avant |
| 2 | **A1 de bout en bout** : corpus A1, grammaire et exercices A1, Premiers pas, A1 voyage, repères, prononciation, scènes (couche des noms) | un compte neuf en anglais, interface espagnole : 🌱, séance, scènes, sans un mot de français |
| 3 | A2 → C1 : corpus, fiches, séries, temps, tuiles, couches A2-C1 des scènes, conjugaison | `tests/francais_ailleurs.py --app en --langues es` (à étendre) : 0 français |
| 4 | Vérification au téléphone simulé, jour et nuit ; relecture d'un échantillon ; rapport | captures ; `verifier.py`, `syntaxe.js` verts |

Chaque palier est publié en **essai admin** (rien ne change pour les testeurs), après les
deux parcours à 0 écart. ⚠️ `index.html` est partagé avec d'autres sessions : le
branchement se fait en une fois, vérifié puis committé aussitôt (fichiers à moi seuls),
et le chef est prévenu avant toute montée de version.

---

## 4. Écrire contre l'espagnol (ce qu'un hispanophone doit lire)

Les explications françaises comparent l'anglais au français. Pour un hispanophone, on les
réécrit (pas de traduction mot à mot), en nommant ses pièges propres :

- **Le sujet obligatoire** : *It's raining*, *It is important* — l'espagnol le laisse tomber
  (*Llueve*, *Es importante*). Erreur n° 1 : « Is raining ».
- **L'adjectif avant le nom et invariable** : *a red car* (pas « a car red »), *two red cars*
  (pas « reds »).
- **do / does / did** pour la question et la négation : *Do you speak English?*, *She doesn't
  work* — l'espagnol n'a ni auxiliaire ni inversion (*¿Hablas inglés?*, *No trabaja*).
- **Le -s de la 3ᵉ personne** (*she works*) et **l'absence de terminaison ailleurs**.
- **to be / to have** pour l'âge et les sensations : *I am 20*, *I'm hungry* (*tengo 20 años,
  tengo hambre*).
- **ser / estar → to be** : un seul verbe en anglais (le contraire du piège des germanophones).
- **Present perfect vs past simple** : ressemble au *pretérito perfecto*, mais l'usage
  diffère (*I've lived here for ten years* = *Llevo diez años viviendo aquí* / *Vivo aquí desde
  hace diez años*) ; *for / since* ≠ *desde hace / desde*.
- **Le possessif selon le possesseur** : *his / her* (*su* ne dit pas qui possède).
- **Pas d'article pour les généralités** : *Dogs are loyal* (*Los perros son leales*) ; *I like
  music* (*Me gusta la música*).
- **like / gustar** : *I like dogs* — le sujet est la personne, l'inverse de *me gustan los perros*.
- **Faux amis hispaniques** : *actually* (en realidad, ≠ actualmente), *embarrassed*
  (avergonzado, ≠ embarazada), *library* (biblioteca, ≠ librería), *carpet* (alfombra, ≠
  carpeta), *exit* (salida, ≠ éxito), *realize* (darse cuenta, ≠ realizar), *assist*
  (ayudar), *attend* (asistir), *sensible* (sensato), *constipated* (estreñido), *fabric*
  (tela), *large* (grande, ≠ largo), *argument* (discusión).
- **Prononciation** : les voyelles longues et courtes (*ship / sheep*, *full / fool*), le **e
  initial** ajouté devant s + consonne (« espeak » pour *speak*), *th* (/θ/ ≠ /t/ ou /s/,
  /ð/), **v ≠ b** (en anglais, la lèvre sur les dents), **h aspiré** (≠ le *j* espagnol, plus
  léger ; *h* muet en espagnol), les finales -ed (/t/, /d/, /ɪd/) et -s, le schwa et l'accent
  tonique, le *r* américain non roulé, *sh* / *ch* (*share / chair*), *j* = /dʒ/ (*job*, pas
  le *j* de *jamón*), le *y* et le *z* sonores.

---

## 5. À décider par Jacques

**Quel espagnol pour l'interface et les traductions ?**

- **Recommandé : un espagnol neutre d'Amérique latine** (« tú », « ustedes », jamais
  « vosotros » ; vocabulaire le plus partagé). C'est l'espagnol du plus grand nombre
  d'hispanophones qui apprennent l'anglais (Mexique, Colombie, Argentine, hispaniques des
  États-Unis), il va de pair avec l'anglais **américain** par défaut, et un Espagnol le lit
  sans peine. Quand un mot diffère vraiment (*car* : el carro / el coche, *computer* : la
  computadora / el ordenador, *cell phone* : el celular / el móvil, *juice* : el jugo /
  el zumo), la carte donne les deux : « el carro (Esp. el coche) ».
- Variante possible : l'espagnol d'Espagne (« vosotros », coche, ordenador), ou les deux
  interfaces (coût d'une seconde relecture, pas d'une seconde traduction).

Le reste n'appelle pas de choix : la voix de l'espagnol connu est celle du téléphone
(aucune dépense) ; l'américain et le britannique reçoivent le même espagnol ; l'essai
reste admin (ouvrir l'anglais aux hispanophones sera une décision à part, avec la porte
d'entrée et la fiche des stores).

---

## 6. Ce qui ne sera pas fait ici (à signaler, comme pour l'allemand)

- **Le dictionnaire** : pas de paire anglais-espagnol câblée (en anglais appris,
  `DICT_PAIRS_PAR_LANGUE` retombe sur les paires allemandes : à garder caché, à vérifier).
- **Les épisodes** : l'anglais n'en a pas encore.
- **La voix de la visite guidée** et toute voix enregistrée en espagnol (dépense, sur accord).
- **La relecture par un hispanophone** : une liste `retours/A-RELIRE-INTERFACE-ES.md` sera
  préparée, comme pour l'allemand.
