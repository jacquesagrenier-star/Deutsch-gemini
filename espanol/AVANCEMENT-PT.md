# L'espagnol en portugais du Brésil — état du chantier

Chantier du 13 octobre 2026 : rendre `index.html?apprendre=es` complet pour
les usagers dont la langue d'interface est le portugais (`pt`), au même niveau
que le français et l'anglais. Base : v782 (le dossier principal ; la v783 n'y
est pas, Jacques réconcilie lui-même).

## Fait

| Où | Quoi | Compte |
|---|---|---|
| `espanol/datos/temas.json` | `traduction_pt` + `exemple_pt` sur chaque mot | 1 759 entrées |
| `espanol/datos/verbos.json` | idem | 873 |
| `espanol/datos/adjetivos.json` | idem | 597 |
| `espanol/datos/adverbios.json` | idem | 228 |
| `espanol/datos/expresiones.json` | idem | 245 |
| `espanol/datos/funcionales.json` | idem | 152 |
| `espanol/datos/ejercicios.json` | `translation_pt`, `hint_pt`, `explanation_pt`, `question_pt` (126, les questions formulées), `optionsPt`/`correctPt` recopiés quand les options sont les mêmes en fr et en | 1 041 exercices |
| `espanol/datos/grammaire.json` | `textes.pt` (43 clés) + clé `pt` sur chaque texte des 7 fiches, réécrits CONTRE le portugais (pièges de genre, pas de « a » personnel en pt, pas de futur du subjonctif en espagnol, etc.) | 43 + 259 |
| `espanol/datos/prononciation.json` | dérivé : `python tests/prononciation_es.py --ecrire` ; le dictionnaire `PT` du script porte les 18 règles + « c-z.es » / « c-z.latam » | 18 règles, 55 exemples |
| `espanol/datos/variantes.json` | `verbes.coger.remarque.pt` | 1 |
| `index.html` | bloc `I18N_ESPAGNOL.pt` (toutes les clés du bloc `fr`) ; libellés `pt` des catégories d'adverbes et d'expressions (branches es) ; `MOTS_OUTILS_ES_PT` (prépositions, conjonctions, particules espagnoles codées en dur → rangs 20/21/22) ; `UI_LANGS` et `LANGUES_UI_AVEC_ESPAGNOL` = `["fr","en","pt"]` | 125 clés, 25 libellés, 74 mots-outils |
| `visuel/prototype/espanol/*.json` | `titre_pt` sur chaque couche, `n_pt` sur chaque question (et sur les variantes latam) | 236 notes, 40 titres |
| `visuel/prototype/construire.py` | porte le `pt` dans `scene-<scène>.es.js` (sens des mots, titres, notes) ; les `scene-<scène>.js` allemands ne bougent pas | 10 scènes refaites |
| `tests/verifier.py` | exige `pt` partout où il exigeait `fr` et `en` pour l'espagnol (libellés, prononciation) | |
| gustar | indices et explications réécrits en fr, en et pt à partir du mot à mot (« le chocolat ME PLAÎT » : une chose → gusta, plusieurs → gustan) ; clé `op_es_gustar_d` aussi | 57 exercices |

Vérificateurs : `python tests/verifier.py`, `node tests/syntaxe.js`,
`python tests/trous_francais.py` — passés. Parcours : voir le rapport de fin.

## Reste

- **La voix de la visite guidée** en portugais pour l'espagnol : `VOIX_VISITE.languesEs` ne connaît que fr et en (enregistrement payant, hors de ce chantier). En pt, la visite se lit sans narration.
- **Relecture par un natif brésilien** des traductions (comme pour le polonais et le russe).
- Défauts **préexistants**, pas introduits ici, à trancher par Jacques :
  - les noms de thèmes espagnols s'affichent en anglais quelle que soit la langue (`nom_theme` = « The house » ; `nom_theme_es` inutilisé) ;
  - `texteDeFiche(v)` retombe directement sur `fr`, pas par `REPLI_LANGUE` ;
  - deux indices de `condicionalExercises` sont en français dans le bloc anglais (« 3e personne »), corrigés seulement en pt.

## Reprendre

- `python espanol/pt/poser.py etat` : compte des champs `_pt` par fichier ;
  `reste <fichier> [n]` liste ce qui manque ; `pose <lot.txt>` pose un lot
  (`num|mot|traduction_pt|exemple_pt`) avec trois garde-fous ; `controle`
  signale un pt identique au fr/en ou qui sent le français.
- Scènes : poser `titre_pt` / `n_pt` dans `visuel/prototype/espanol/<scène>.json`,
  puis `python visuel/prototype/construire.py <scène>` ; `git diff --stat visuel/prototype/scene-*.js`
  ne doit montrer que des `.es.js`.
- Prononciation : ne jamais éditer `prononciation.json` à la main ; modifier
  `PT` dans `tests/prononciation_es.py` puis `--ecrire`.
- Ne pas ajouter de langue à `LANGUES_UI_AVEC_ESPAGNOL` avant que les données,
  `I18N_ESPAGNOL` et les scènes soient complètes dans cette langue.
