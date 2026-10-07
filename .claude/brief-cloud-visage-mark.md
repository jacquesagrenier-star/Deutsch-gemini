# Brief pour une session cloud : le visage de Mark (7 oct. 2026)

Tu reprends un travail commencé en local. Tu n'as pas les notes de mémoire de la session locale : tout ce qu'il te faut est ici, plus `CLAUDE.md`.

## Règles de cette session

- Travaille sur une branche **`visage-mark`** et termine par une pull request. **Ne pousse rien sur `main`** : `main` est la production, et `visuel/prototype/` est publié tel quel sur GitHub Pages.
- Ne change pas le numéro de version (badge, `APP_VERSION`, `version.json`) : la mise en ligne se fera en local, demain.
- Avant la PR : `python tests/verifier.py` et `node tests/syntaxe.js` si tu touches `index.html`.
- Écris tes scripts de modification dans un **fichier**, jamais en heredoc (il mange les `\n`).
- Jacques (le propriétaire) relit à l'œil : montre-lui les images de contrôle avant et après chaque correction.

## Contexte : les scènes interactives

Une image photoréaliste 9:16, l'app pose les étiquettes, l'élève touche le mot demandé. Prototype : `visuel/prototype/index.html?scene=arztpraxis` (en ligne : https://jacquesagrenier-star.github.io/Deutsch-gemini/visuel/prototype/?scene=arztpraxis).

- Tout ce qui est propre à une scène vit dans `visuel/prototype/<nom>.points.json`. Puis `python visuel/prototype/construire.py <nom>` regénère `scene-<nom>.js`. Ne jamais recopier `index.html` pour une scène.
- Les parties du corps sont des zones `ellipses`. Les gros plans (`net: true`) sont découpés dans l'image source : `arztpraxis-visage-mark.webp`, `-main-mark`, `-pieds-mark`, `-affiche`.
- **Une cible est un MOT, pas une zone** : chaque zone porte tous ses noms (champ `aussi`).
- Toucher ce qui est **posé sur** l'objet demandé est juste (champ `sur`, dans ce sens seulement).
- L'étiquette se place d'après **l'image réelle**, jamais d'après le prompt (« droit » et « gauche » se lisent sur l'image).

## La tâche, dans cet ordre

1. **Gros plan du visage de Mark (arztpraxis)**, remarques de Jacques du 6 oct. (aussi dans `retours/journal-retours.md`) :
   - l'œil DROIT de l'image est trop à droite ;
   - l'oreille DROITE répond « der Kopf » au lieu de « das Ohr » ;
   - der Hals mord sur le menton : **das Kinn ne bouge pas**, descendre le cou ;
   - das Haar est à centrer sur les cheveux ;
   - die Stirn doit pouvoir se toucher.

   **MESURER D'ABORD** :
   `python visuel/prototype/grille_gros_plan.py 43.5 29 56.5 40.5 0.25 4 sortie.png visage-mark`
   (grille de 0,25 %). Les ellipses placées sur une grille de 1 % tombaient à côté. Regarde l'image produite, corrige, regénère la grille et compare.
2. Relire de la même façon la main, les pieds, puis l'affiche : l'ovale de das Poster déborde sur la tête de Mark.
3. Seulement si le temps le permet : faire qu'une bonne réponse dans la scène compte comme une révision du mot (répétition espacée). L'essai s'appelle `scenes`, dans l'objet `ESSAIS` d'`index.html` (état `"admin"`). Ne le passe **pas** à `"tous"` : c'est Jacques qui décide de la mise en production.

À ne pas toucher : les questions A2-C1 du médecin (brouillon que Jacques doit relire) et les traductions tr/uk/fa de der Knöchel.
