# Brief pour une session cloud : traduire les scènes (10 oct. 2026)

Tu reprends un travail commencé en local. Tu n'as pas les notes de mémoire de la session locale : tout ce qu'il te faut est ici, plus `CLAUDE.md` (lis-le d'abord, en entier).

## Règles de cette session

- Branche **`scenes-traduction`**, pull request vers `main` à la fin. **Rien sur `main`** : c'est la production, et `visuel/prototype/` y est publié tel quel.
- Pas de changement de numéro de version (`APP_VERSION`, badge, `version.json`).
- **Pas d'agents en parallèle** : ta session puise dans la même limite de 5 h que le PC de Jacques. Travaille seul, à la suite.
- Avant la PR : `python tests/verifier.py` et `node tests/syntaxe.js`.
- Scripts de modification dans un **fichier**, jamais en heredoc (Git Bash et les heredocs mangent les antislashs).
- Écris un compte rendu `.claude/compte-rendu-scenes-traduction.md` sur la branche : ce qui est fait, ce qui ne l'est pas, ce qui demande l'œil de Jacques.

## Contexte

Les scènes interactives : une image photoréaliste 9:16, l'élève touche le mot demandé (« Trouve ! ») ou répond à des questions par couche de niveau (A1 → C1). Prototype : `visuel/prototype/index.html?scene=<nom>`. L'app les ouvre dans une iframe (`ouvrirSceneSeance()` dans `index.html`, derrière l'essai `scenes`, état `"admin"`).

- Tout ce qui est propre à une scène vit dans `visuel/prototype/<nom>.points.json` ; `python visuel/prototype/construire.py <nom>` regénère `scene-<nom>.js`. Huit fichiers : `klassenzimmer`, `untersuchung`, `untersuchung-dos`, `arztpraxis`, `markt-obst-heimisch`, `markt-obst-sued`, `markt-gemuese-wurzel`, `markt-gemuese-frucht`.
- L'**interface** du prototype est déjà traduite : `?lang=fr|en|tr|uk|fa|ar`, objet `TEXTES` et fonction `T()` dans `visuel/prototype/index.html`. tr/uk/fa/ar non relus par un natif.
- Le **contenu** est encore en français seulement : `titre`, `alt`, `consigne`, `nom_vue`, les `titre` des couches, et dans chaque question le champ **`n`** (l'explication, du HTML avec `<b>`). Environ 180 questions. Les champs allemands (`q`, `c`, `phrase`, les mots) **ne se traduisent pas** : c'est la matière apprise.

## La tâche, dans cet ordre

1. **L'app passe la langue à la scène.** Dans `ouvrirSceneSeance()` (et l'ouverture depuis le tableau admin s'il y en a une), ajouter `&lang=` avec la langue d'interface de l'usager (`getUiLang()`). Vérifie la liste `UI_LANGS` : une langue que le prototype ne connaît pas doit retomber sur le français ou l'anglais proprement, pas casser.
2. **Droite à gauche (fa, ar).** `dir="rtl"` et `lang` sur la page du prototype quand la langue l'exige, et revoir la mise en page en 375 px de large : boutons, bandeau, pastilles de niveau, explications. L'allemand dans une page RTL doit rester lisible (isoler les phrases allemandes, `dir="ltr"` ou `<bdi>`). L'app elle-même gère déjà le RTL pour fa et ar : regarde comment elle fait et fais pareil.
3. **Traduire le contenu des scènes en en, tr, uk, fa, ar**, dans des **fichiers séparés**, pas dans les points.json : `visuel/prototype/traductions/<nom>.<lang>.json`. Raison : les questions sont en pleine relecture sur `main` ; en touchant les points.json tu créerais des conflits. Chaque entrée garde **le texte français source** à côté de sa traduction ; `construire.py` fusionne, et **avertit** quand le français a changé depuis la traduction (la traduction est alors périmée : on affiche le français plutôt qu'une explication fausse). Clé d'une question : ce qui l'identifie de façon stable dans le points.json (regarde s'il existe un identifiant ; sinon la couche + `phrase`).
   - Les explications sont des **explications de grammaire allemande pour des apprenants** : garder les mots allemands en `<b>` intacts, traduire seulement l'explication. Le registre de l'app dans chaque langue : regarde les traductions existantes dans `index.html` (clés tr/uk/fa/ar) et aligne-toi dessus.
   - Pour un apprenant turc, ukrainien, persan ou arabophone, une explication qui compare au français n'a pas de sens : la reformuler pour la langue cible plutôt que de traduire la comparaison.
4. **L'écran de choix de la séance** (`choixSeance` dans `index.html`, et `visuel/prototype/choix-seance.html` s'il sert encore) : vérifier que tous ses textes passent par les clés de traduction de l'app, dans toutes les langues de `UI_LANGS`.
5. **Vérifier dans un navigateur headless** à 375 px : une scène par langue, une en fa et une en ar ; une question de chaque niveau ; capture d'écran dans `.claude/compte-rendu-scenes-traduction/`.

À ne pas toucher : le texte français et allemand des questions (relecture en cours en local), l'état de l'essai `scenes` (Jacques décide de la mise en production).
