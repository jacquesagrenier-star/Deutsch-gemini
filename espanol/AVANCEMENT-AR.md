# L'espagnol en arabe : avancement

Chantier arrêté le 13 octobre 2026 au soir : le crédit hebdomadaire de Fable est épuisé.
Décision de Jacques : on le **relance à la remise à zéro de Fable**.

**15 oct. 2026 : ce qui est « Fait » ci-dessous est PUBLIÉ, inerte** (Jacques : « publier le
travail de Fable pour l'arabe »). Les champs `_ar` sont dans `espanol/datos/` sur `main`, mais
l'app ne propose toujours pas l'espagnol en arabe : `LANGUES_UI_AVEC_ESPAGNOL` vaut
`["fr", "en", "pt"]` tant que le « Reste » n'est pas fait. Le dossier principal n'a donc plus de
travail arabe non publié : la prochaine étape peut se committer normalement.

Le modèle à copier est le chantier portugais : `espanol/AVANCEMENT-PT.md`,
`espanol/pt/poser.py` et le commit v784 (`git show --stat 36bc1ce`).
L'outil arabe est `espanol/ar/poser.py`, et les lots déjà écrits sont dans `espanol/ar/lots/`.

## Fait (mesuré le 13 oct. au soir, JSON valides)

| Fichier | Champs arabes | Couverture |
|---|---|---|
| temas.json | traduction_ar, exemple_ar | 1 759 / 1 759 |
| verbos.json | traduction_ar, exemple_ar | 873 / 873 |
| verbos.json | exemple_<temps>_ar (preterito, imperfecto, perfecto, futuro, condicional, subjuntivo) | identique au pt (872-873 par temps ; soler n'a pas certains temps) |
| adjetivos.json | traduction_ar, exemple_ar | 597 / 597 |
| adverbios.json | traduction_ar, exemple_ar | 228 / 228 |
| expresiones.json | traduction_ar, exemple_ar | 245 / 245 |
| funcionales.json | traduction_ar, exemple_ar | 152 / 152 |
| ejercicios.json | translation_ar, hint_ar, explanation_ar | **150 / 1 041** (lot ejercicios-01) |

## Reste

1. `ejercicios.json` : les 891 exercices restants (translation_ar, hint_ar, explanation_ar), plus `question_ar`
   sur les 126 questions formulées. Pour gustar, le mot à mot de la v784 : « le chocolat me plaît ».
2. `grammaire.json` : `textes.ar` et la clé `ar` des fiches, **réécrits pour un arabophone**.
3. `prononciation.json` (via `tests/prononciation_es.py`, en ajoutant ar) et `variantes.json`.
4. Scènes : `visuel/prototype/espanol/*.json` (`titre_ar`, `n_ar`), puis `visuel/prototype/construire.py`.
5. `index.html` : `I18N_ESPAGNOL.ar` (toutes les clés du bloc pt), libellés ar des catégories,
   rangs ar des mots-outils, puis `LANGUES_UI_AVEC_ESPAGNOL` += "ar" (en tout dernier).
6. `tests/verifier.py` : exiger ar comme pt pour l'espagnol.
7. Relecture (300 traductions au moins, et toutes les fiches), vérification à l'écran
   de droite à gauche, vérificateurs, parcours (de-v783 : 0 écart ; es-v783 : 0 écart attendu).

Le contrôle qui a précédé la publication (15 oct.) : chacun des sept fichiers, une fois ses
champs `_ar` retirés, est identique au commit d'avant. L'arabe n'a rien changé d'autre.
