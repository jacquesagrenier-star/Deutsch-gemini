# Brief cloud — le polonais, 8e langue d'interface de l'app allemande

Demandé par Jacques le 12 oct. 2026 : une version polonaise de l'application
pour apprendre l'allemand (des Polonais qui apprennent l'allemand). Exigence en
vigueur : **toutes les langues d'interface ont le même contenu** (interface,
grammaire, corpus, exercices, examen, exercices d'articles, scènes,
prononciation). Lis d'abord `CLAUDE.md`, puis ce brief en entier.

## Le modèle à copier : le portugais du Brésil

Le portugais (`pt`) est la dernière langue ajoutée, de bout en bout :
`git show 88ccf9e` (v765 : interface, grammaire, câblage, A1-A2), puis v766-v769
(`git log --oneline 88ccf9e^..c1f0a3a`). Fais **la même chose pour `pl`**, aux
mêmes endroits. L'arabe (`ar`) a été câblé en v772 (`git show 4943806`) avec le
script `.claude/polonais/outils/cablage_ar.py` : c'est ton gabarit pour le
câblage des cartes, avec `pl` APRÈS `ar` (rangs : celui de `ar` + 2).

Réglages : code `pl`, `LANGUE_TAG` `pl-PL`, `LOCALES_ABO` `pl-PL`, drapeau 🇵🇱,
libellé « Polski », repli `pl → en → fr`. Guillemets polonais „ ”. Registre :
le même que l'interface française (vérifie si elle tutoie ; si oui, « ty »).

## ⚠️ Une autre session travaille en même temps : l'arabe

La session `arabe-contenu` pose en ce moment les champs `_ar` dans les données
B1 à C1, dans `pruefung.json`, `exercices.json`, les exercices d'articles
d'`index.html`, `LANGUES_PRUEFUNG`, `visuel/prototype/construire.py` et
`tests/prononciation.py`. Si tu écris aux mêmes lignes, les deux PR seront en
conflit. D'où deux phases.

### Phase 1 — à faire et à poser maintenant (branche `polonais`)

1. **Interface** : toutes les clés de traduction (bloc `pl` à côté de `pt`),
   `UI_LANGS`, `LANGUE_TAG`, `LOCALES_ABO`, `DRAPEAUX_LANGUE`, `REPLI_LANGUE`,
   `SUFFIXE_LANGUE`, `SUFFIXE_CHAMEAU`, sélecteur de langue. Le vérificateur
   signale toute clé absente d'une langue.
2. **`grammaire.json`** : les fiches en polonais (comme `pt` en v765).
3. **Câblage des cartes** (gabarit `cablage_ar.py`) : `RANGS_CARTE`, chargeur
   des verbes, tuples des cartes, recherche, phrases à construire, catégories
   d'adverbes et d'expressions, `VOICE_PREFEREES`.
4. **Corpus A1 et A2 posés** (l'arabe ne touche plus ces niveaux) :
   `python tests/corpus_langue.py --langue pl etat | reste <fichier> <niveau> <n> | pose <lot.json>`.
   Format de lot dans `tests/corpus_langue.py` ; un brouillon compact
   `num|traduction|exemple[|perfekt|praeteritum|konj2][|kategorie]` se convertit
   avec `.claude/polonais/outils/lot.py` (adapte la garde « lettres mêlées » au
   polonais : elle a été écrite pour l'arabe).
   ⚠️ `corpus_langue.py` doit connaître `pl` : regarde comment il gère `ar`/`pt`.
5. **Scènes** : `visuel/prototype/traductions/<scène>.pl.json` (nouveaux
   fichiers, modèle `*.pt.json`) et les textes de la page des scènes. Ne touche
   pas `construire.py` (phase 2).

### Phase 2 — à préparer en fichiers, PAS à poser

Écris les traductions dans `polonais/` (dossier à toi seul), prêtes à poser :
- corpus B1, B2, C1 : un lot par fichier et par tranche, `polonais/lots/*.json`,
  au format exact de `corpus_langue.py pose` ;
- examen : `polonais/examen/t*.json`, clés `section/i[/j]|base` (relevé des 720
  champs français : `.claude/polonais/outils/examen_dump.jsonl` ; outil de pose :
  `poser_examen.py` — ajoute `pl` à la liste des langues qui gardent « » si besoin) ;
- exercices d'articles : `polonais/articles/t_pl.json` (relevé :
  `articles_dump.jsonl`, exemple ukrainien `exemple_articles_uk.json`) ; dans
  `patch_articles.py`, ajoute les genres polonais à `GENRES` ;
- exercices de grammaire : `polonais/exercices/` (méthode `exos_dump.py`,
  `exos_convertir.py`, écrite pour `pt` : adapte à `pl`) ;
- prononciation : le dictionnaire de règles `PL` pour `tests/prononciation.py`,
  dans `polonais/prononciation_pl.py`.
Ces fichiers seront posés après la fusion de l'arabe, en une étape mécanique.
Fais la phase 2 dans cet ordre : corpus, examen, articles, exercices, prononciation.

## Qualité

- Chaque carte a un seul sens : celui que montrent le français, l'anglais ET
  l'exemple allemand. Traduction et exemple polonais disent la même chose.
- **Les explications de grammaire s'écrivent CONTRE le polonais**, pas traduites
  du français : le polonais a sept cas (dont l'instrumental et le locatif : dire
  à quel cas allemand chacun correspond, et où ça ne colle pas), pas d'article
  (l'article allemand est la vraie difficulté), l'aspect verbal (≠ Perfekt /
  Präteritum), un ordre des mots libre (le verbe en 2e position est la règle
  allemande à marteler), un seul « tu/vous » de politesse différent (Pan/Pani ≠
  Sie). Prononciation : écrire les règles contre le polonais (ch, sch ≈ sz,
  ei, eu, ü, ö, le r, les voyelles longues), pas contre le français.
- Pas de traduction mot à mot des remarques françaises (« (nom autrichien) » se
  dit en polonais).

## Règles de travail (non négociables)

- Branche **`polonais`**, à partir de `main`. Un commit par étape ou par lot,
  poussé aussitôt (la session peut s'arrêter à tout moment). PR vers `main` à la
  fin de la phase 1 ; la phase 2 continue sur la même branche. **Ne fusionne pas.**
  Jamais de push sur `main`. Pas de changement de version.
- **Pas de sous-agents, pas d'agents en parallèle.**
- **L'allemand et l'espagnol ne doivent pas changer.** Tout fichier réécrit est
  identique à l'original hors champs `pl`. Avant chaque push :
  `python tests/verifier.py` et `node tests/syntaxe.js`. Si Playwright est
  disponible, `fusion-espagnol/parcours.py --app de` doit donner 0 écart contre
  `fusion-espagnol/references/de-v765.json` ; sinon, dis-le dans la PR.
- Pas de heredoc Git Bash pour du code avec antislashs : de vrais fichiers.
- La voix de la visite guidée en polonais est PAYANTE : ne la fais pas.
- Message final court, en français : ce qui est posé (phase 1), ce qui est prêt
  en fichiers (phase 2), chiffres, lien de la PR.
