# Licences — module kana

## KanjiVG — ordre des traits (`traits/`)

Les 177 fichiers SVG du dossier `traits/` viennent **tels quels** du projet **KanjiVG** :

- Site : https://kanjivg.tagaini.net/
- Dépôt : https://github.com/KanjiVG/kanjivg (dossier `kanji/`, branche `master`, commit `70a0b7ae0c18ceb5cb358274b029cce0234a43bc`, récupéré le 4 octobre 2026)
- Auteur : Ulrich Apel et les contributeurs de KanjiVG
- Licence : **Creative Commons Attribution – Partage dans les mêmes conditions 3.0** (CC BY-SA 3.0), https://creativecommons.org/licenses/by-sa/3.0/

Aucun tracé n'a été dessiné ni retouché : chaque fichier garde son en-tête de copyright d'origine. Les numéros de traits sont ceux que KanjiVG place dans chaque fichier (groupe `StrokeNumbers`).

### Ce que la licence exige

1. **Attribution.** Partout où ces tracés sont montrés (app, site, document), mentionner KanjiVG avec un lien vers https://kanjivg.tagaini.net/ et la licence. Dans l'app, la place naturelle est la carte « Crédits » des réglages, comme pour WikDict et Leipzig dans l'app d'allemand. Formulation possible :
   > Ordre des traits : KanjiVG (https://kanjivg.tagaini.net), © Ulrich Apel et contributeurs, sous licence CC BY-SA 3.0.
2. **Partage à l'identique.** Toute version **modifiée** de ces SVG (recoloration, animation, tracés fusionnés, conversion en un autre format) doit être diffusée sous CC BY-SA 3.0 ou une licence compatible, et donc pouvoir être réutilisée par d'autres aux mêmes conditions. Afficher les SVG sans les modifier n'entraîne pas cette obligation pour le reste de l'app.
3. Ne pas retirer l'en-tête de copyright des fichiers.

### Fichiers qui en dérivent

- `kana.json`, champ `traits` (et `composants[].traits`) : nombre de traits **compté** dans les SVG KanjiVG. Un nombre est un fait plutôt qu'une œuvre, mais on cite la source par prudence (le champ `sources` de `kana.json` le fait).
- `planche.html` affiche les SVG par lien, sans les modifier : la mention KanjiVG figure en haut de la page.

## Unicode

Les noms de caractères Unicode (via le module `unicodedata` de Python) servent seulement à **vérifier** le romaji et le classement gojūon dans `outils/construire.py`. Rien n'en est copié dans les fichiers produits. Licence Unicode : https://www.unicode.org/license.txt

## Contenu original de ce dossier

`kana.json` (hors comptage de traits), `confusions.json`, `mnemoniques.json`, les documents et les scripts de `outils/` ont été rédigés pour ce projet. Leur licence reste à choisir par le propriétaire du dépôt. Les moyens mnémotechniques ont été écrits pour l'occasion, sans recopier un cours existant. Quelques associations sont pourtant des idées que presque tous les cours partagent, parce que la forme les impose (た = « t » + « a », ん ≈ « n », の = panneau barré, つ = tsunami) : à garder en tête si l'on veut un ensemble entièrement distinctif.
