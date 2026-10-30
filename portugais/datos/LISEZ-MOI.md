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
