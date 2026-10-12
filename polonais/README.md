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
- `examen/t1.json` … `t7.json` — l'examen blanc (`pruefung.json`), 720 champs
  polonais. Poser :
  `python .claude/polonais/outils/poser_examen.py pruefung.json pl polonais/examen/t*.json --ecrire`
  (sans `--ecrire` : pose à blanc, rien n'est écrit).
- `articles/t_pl.json` — les 219 textes des exercices d'articles d'`index.html`
  (genres, cas, phrases). Poser, `<prec>` étant la dernière langue déjà posée
  (`ar` après la fusion de l'arabe) :
  `python .claude/polonais/outils/patch_articles.py index.html pl ar polonais/articles/t_pl.json .claude/polonais/outils/articles_dump.jsonl --ecrire`
- `exercices/corr_<jeu>.json` — exercices de grammaire, 40 jeux sur 40,
  2 317 exercices (traduction, explication, indice, question, réponse et
  options en polonais — les mêmes champs que le portugais). Les brouillons
  texte d'où ils sont tirés sont dans `exercices/brouillons/`
  (`.claude/polonais/outils/exos_convertir.py`). Poser :
  1. dans `tests/lot_exos.py`, ajouter `"pl": "Pl"` au dictionnaire `CHAMEAU` ;
  2. `python tests/lot_exos.py --langue pl --recopier-formes` ;
  3. `for f in polonais/exercices/corr_*.json; do python tests/lot_exos.py --langue pl --poser $f; done` ;
  4. `python tests/lot_exos.py --etat` doit montrer `pl` à 100 %.
- `prononciation_pl.py` — les 25 règles de prononciation, écrites contre le
  polonais. La pose (cinq gestes dans `tests/prononciation.py`) est décrite en
  tête du fichier ; `python polonais/prononciation_pl.py` contrôle qu'il a les
  mêmes règles que le script.

Corpus : 41 lots, 5 966 cartes (thèmes 3 497, verbes 967, adjectifs 732,
adverbes 319, mots-outils 51, expressions 400).

Ordre de pose conseillé : corpus, examen, articles, exercices, prononciation,
puis les deux vérificateurs (`python tests/verifier.py`, `node tests/syntaxe.js`)
et le parcours allemand (`fusion-espagnol/parcours.py`) : l'allemand ne doit
pas changer. Non relu par un natif.

La numérotation des cartes est celle de `corpus_langue.py` (parcours fixe des
six fichiers) : poser des champs `_ar` ne la change pas. Si des cartes sont
**ajoutées** ou **retirées** avant la pose, la garde « le mot allemand au
numéro » arrête le lot au lieu d'écrire au mauvais endroit.
