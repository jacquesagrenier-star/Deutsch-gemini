# portugais/datos — fichiers DÉRIVÉS

Ne rien corriger ici à la main. On corrige les listes de `portugais/outils/`
(noms_a1.py, mots_a1.py, phrases_a1.py, grammaire_a1.py, conjugaison.py,
reperes_a1.py, prononciation_a1.py, conjugaison_a1.py, premiers_pas_a1.py,
a1_voyage_a1.py), puis :

    python portugais/outils/construire.py

qui refait tous ces fichiers ET les 43 scènes `visuel/prototype/scene-<nom>.pt.js`
(par `portugais/outils/scenes.py`).

Portugais du **Portugal** (décidé par Jacques le 29 oct. 2026). Même forme que
`espanol/datos/` : genre `o` / `a`, pluriel calculé, temps en listes de six
personnes (eu, tu, ele, nós, vós, eles ; vós est caché par le moteur).

`variantes-br.json` : le mot du Brésil quand il diffère (drapeau `br=` des
listes), pour une future variante brésilienne. Le moteur ne le lit pas encore.

Pas de clé `_lisez_moi` dans les fichiers par niveau (verbes, adjectifs…) : le
chargeur prendrait chaque clé pour un niveau. Cette notice-ci en tient lieu.

Deux dérivés à part, qui ne sortent PAS de `construire.py` (ils lisent des
archives gardées hors du dépôt) :

- `frequence.json` (et `../datos-br/frequence.json`) : le classement par
  fréquence d'usage, Leipzig (CC BY), **à l'intérieur d'une catégorie
  seulement**. Après chaque `construire.py` :
  `python portugais/outils/frequence.py --ecrire`
  (archives : `C:/Users/jacqu/.wortando/frequence-pt`).
- `dicc/` : le dictionnaire de la recherche, WikDict pt-fr / fr-pt (CC BY-SA 4.0,
  voir `dicc/LICENSE.txt`), un seul pour le Portugal et le Brésil :
  `python portugais/outils/dicc_construire.py`
  (archives : `C:/Users/jacqu/.wortando/wikdict-pt`).
