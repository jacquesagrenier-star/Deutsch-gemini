# L'espagnol en allemand : avancement

**1er nov. 2026 : chantier « interface allemande »** (branche `claude/interface-allemande-2fd6e4`).
Décision de Jacques du 1er nov. : ouvrir l'espagnol aux germanophones (« Anglais,
portugais du Brésil, puis on va faire aussi l'allemand. Puis on va faire aussi l'arabe »).
L'allemand devient une **langue d'interface**, proposée **seulement quand on apprend
l'espagnol** (`UI_LANGS` de l'espagnol = fr, en, pt, ar, de). L'app allemande ne la
propose jamais : une interface allemande pour apprendre l'allemand donnerait le mot
pour sa propre traduction.

Modèle : la chaîne arabe (`espanol/ar/`, 15 oct.), elle-même copie du portugais.

## Comment c'est fait

| Étape | Outil |
|---|---|
| Sortir les textes à traduire (hors corpus) | `python espanol/de/extraire.py` → `espanol/de/sources/` |
| Corpus, phrases des temps, exercices | `python espanol/de/poser.py etat \| reste \| pose [--essai] \| controle` |
| Le reste (interface, grammaire, scènes, parcours…) | `python espanol/de/poser_autres.py controle \| pose [nom…]` |
| Consignes données aux traducteurs | `espanol/de/CONSIGNES.md` (glossaire commun, « écrire contre l'allemand ») |
| Lots traduits | `espanol/de/lots/` ; comptes rendus `RAPPORT-*.md` |

## ⚠️ « de » désignait déjà la langue APPRISE

Dans une partie du code, « de » ne veut pas dire « allemand » mais « la langue qu'on
apprend » (héritage d'avant la fusion de l'espagnol) : la voix (`pickVoice("de")` = voix
espagnole en espagnol), l'écoute (`ecouteLangues()` : `cible: "de"`), l'index de
recherche (`entry.de` = le mot appris), les phrases (`ph.de`). Une interface « de »
y entrait en collision :

- **Écouter** lisait deux fois le mot espagnol (connu = cible = « de ») → `connuAllemand`
  dans `contenuEcoute()`, voix `VOIX_ALLEMAND_CONNU` (« de-connu », une voix allemande) ;
- **la recherche** affichait le mot espagnol comme sa propre traduction → `tradRecherche()` ;
- **les réglages des voix** n'offraient pas de voix pour la langue connue → ligne « de-connu ».

Les champs `*_de` eux-mêmes n'existaient nulle part : aucune donnée allemande n'en porte.

## Ce qui est branché dans `index.html`

`SUFFIXE_LANGUE`, `SUFFIXE_CHAMEAU`, `DRAPEAUX_LANGUE` (🇩🇪), `REPLI_LANGUE` (de → en → fr),
`RANGS_CARTE` (de : nomen 27-28, adjektive 25-26, funktionswort 32-34, expression 33-35),
les chargeurs (rangs ajoutés **en espagnol seulement** : l'objet allemand ne change pas),
`RANGS_PP` (Premiers pas, 33-35), `NOM_LANGUE_NATIF`, `LOCALES_ABO`, la consigne de la
dictée, « Écrire » (`question_de`), l'écoute de phrases, les boutons « Deutsch » (cachés
hors de l'espagnol), `UI_LANGS` et `LANGUES_UI_AVEC_ESPAGNOL`. Données : bloc `de:` de
`I18N`, `"de"` de `I18N_ESPAGNOL`, `MOTS_OUTILS_ES_DE`, `de:` des catégories et de
`SCENES_COURTS`. Page des scènes : `TEXTES.de`, `LANGUE`, `REPLI`. `construire.py` porte
l'allemand dans les `scene-*.es.js` (les `scene-*.js` allemands ne bougent pas).

## Fait (1er nov. 2026)

| Où | Quoi | Compte |
|---|---|---|
| `index.html` | `I18N.de` (toute l'interface), `I18N_ESPAGNOL.de`, catégories, mots-outils, vignettes | 1 607 + 142 + 25 + 74 + 39 |
| corpus `espanol/datos/` | `traduction_de` + `exemple_de` (temas, verbos, adjetivos, adverbios, expresiones, funcionales), **0 collision** | 3 898 (+ 51 adjectifs de « Mon cours ») |
| `verbos.json` | `exemple_<temps>_de` | 873 × 6 |
| `ejercicios.json` | `translation_de`, `hint_de`, `explanation_de`, `question_de`, `optionsDe`, `correctDe` | 1 343 |
| `grammaire.json` | `textes.de` + `de` dans les 17 fiches, **réécrites contre l'allemand** | 43 + 278 |
| prononciation | `DE` de `tests/prononciation_es.py` (puis `--ecrire`) | 20 règles |
| conjugaison, Premiers pas, A1 voyage, repères, variantes | clé `de` après `ar` | 224 + 667 + 746 + 98 + 1 |
| scènes | `titre_de`, `n_de`, `sens_de`, `alt_de`, `consigne_de` dans `visuel/prototype/espanol/*.json`, puis `construire.py` | 2 430 |
| mosaïque | `de` dans `espanol/mosaique/peintres.json` | 22 |

Contrôles : `poser.py etat` 6 114 / 6 114, `poser_autres.py controle` 0 faute partout,
`tests/verifier.py` (nouveau : `verifier_allemand_espagnol`, l'allemand partout où l'arabe
existe), `tests/francais_ailleurs.py --app es --langues de` (et `--reference en`, nouveau,
pour l'anglais resté : le repli de l'allemand), parcours `de` et `es-moteur` à 0 écart.

## Reste

- **Relecture par un germanophone** : `retours/A-RELIRE-INTERFACE-DE.md` ; doutes par id dans
  `espanol/de/lots/RAPPORT-*.md`.
- Restent en anglais pour un germanophone : le **dictionnaire** (pas de paire WikDict es-de
  câblée), les **épisodes** (fr/en), la **voix de la visite guidée** (comme pt et ar).
- **Arriver jusqu'à l'espagnol** : un téléphone en allemand qui ouvre `wortando.com` tombe sur
  l'allemand appris (interface anglaise) ; l'espagnol s'ouvre par `?apprendre=es`. Décision
  produit à prendre (porte d'entrée pour les germanophones).
- Les adjectifs de « Mon cours » (admin) ont leur allemand dans les données, mais leur
  chargeur ne lit que fr/en (comme pour pt et ar).

## Reprendre

Un texte espagnol ajouté plus tard (nouvelle clé, nouvelle fiche, nouvelle scène) : relancer
`python espanol/de/extraire.py`, puis `poser_autres.py controle <nom>` liste ce qui manque ;
`poser.py etat` pour le corpus et les exercices ; `tests/verifier.py` le signale aussi.
⚠️ `tests/fusion_langue.py` et `tests/dico_interface.py` ne savent pas poser « de » : ils
cherchent `de: {` dans tout le fichier et tombent sur une autre table (`de: { A1: [...] }`).
