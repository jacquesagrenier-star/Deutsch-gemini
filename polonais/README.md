# Polonais — phase 2, prête à poser

Ce que le brief (`.claude/brief-cloud-polonais.md`) réserve à **après la fusion
de l'arabe** : les mêmes fichiers que la session `arabe-contenu` modifie en ce
moment. Tout est ici en fichiers ; rien n'est posé dans les données de l'app.

## Contenu

- `lots/<fichier>_<niveau>_<tranche>.json` — corpus B1, B2, C1, au format exact
  de `tests/corpus_langue.py pose`. Chaque lot a été posé à blanc sur une copie
  du fichier au moment où il a été écrit (garde-fous de l'outil : mot allemand
  au numéro, relecture).
  Poser : `for f in polonais/lots/*.json; do python tests/corpus_langue.py --langue pl pose $f; done`
- `examen/` — `pruefung.json` (à venir).
- `articles/` — exercices d'articles (à venir).
- `exercices/` — exercices de grammaire (à venir).
- `prononciation_pl.py` — règles de prononciation (à venir).

La numérotation des cartes est celle de `corpus_langue.py` (parcours fixe des
six fichiers) : poser des champs `_ar` ne la change pas. Si des cartes sont
**ajoutées** ou **retirées** avant la pose, la garde « le mot allemand au
numéro » arrête le lot au lieu d'écrire au mauvais endroit.
