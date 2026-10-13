# Brief cloud — le russe, 9e langue d'interface de l'app allemande

Demandé par Jacques le 12 oct. 2026 : une version russe de l'application pour
apprendre l'allemand (des russophones qui apprennent l'allemand). Exigence en
vigueur : **toutes les langues d'interface ont le même contenu** (interface,
grammaire, corpus, exercices, examen, exercices d'articles, scènes,
prononciation). Lis d'abord `CLAUDE.md`, puis ce brief en entier.

## ⚠️ Deux autres sessions travaillent en même temps

L'arabe (branche `arabe-contenu`) et le polonais (branche `polonais`) modifient
en ce moment `index.html` (bloc de traductions, listes de langues, câblage des
cartes, examen, articles) et les données (`themes.json`, `verbe.json`,
`adjectif.json`, `adverbe.json`, `redewendung.json`, `funktionswort.json`,
`grammaire.json`, `pruefung.json`, `exercices.json`), ainsi que
`visuel/prototype/construire.py` et `tests/prononciation.py`.

**Donc : tu ne modifies AUCUN fichier existant du dépôt.** Tu PRÉPARES tout dans
un dossier à toi, `russe/`, plus des fichiers NEUFS de scènes. L'intégration se
fera plus tard, en une étape mécanique, une fois l'arabe et le polonais fusionnés.
Pour que cette étape soit sûre, tu écris aussi les scripts qui poseront tes
fichiers, et tu les ESSAIES sur une copie jetable du dépôt (voir « Preuve »).

## Le modèle à copier

Le portugais du Brésil (`pt`) est la dernière langue ajoutée de bout en bout :
`git show 88ccf9e` (v765 : interface, grammaire, câblage, A1-A2), puis
`git log --oneline 88ccf9e^..c1f0a3a` (v766-v769). L'arabe a été câblé en v772
(`git show 4943806`) par `.claude/russe/outils/cablage_ar.py`. Regarde aussi
comment l'**ukrainien** (`uk`) est traité : c'est la langue la plus proche,
mais NE COPIE PAS l'ukrainien, traduis depuis le français, l'anglais et
l'allemand.

Réglages : code `ru`, `LANGUE_TAG` `ru-RU`, `LOCALES_ABO` `ru-RU`, libellé
« Русский ». Drapeau : **ne mets pas de drapeau national** ; propose dans la PR
un symbole neutre (par exemple 🌐 ou les lettres « RU ») et laisse Jacques
choisir. Repli `ru → en → fr`. Guillemets « ». Registre : le même que
l'interface française (vérifie si elle tutoie ; si oui, « ты »).

## Ce qu'il faut produire, dans `russe/`

1. `russe/interface.json` : `{clé: texte}` pour TOUTES les clés que porte la
   langue `pt` dans `index.html` (même liste, aucune de plus ni de moins).
2. `russe/grammaire.json` : les champs russes de `grammaire.json`, au format
   qui permet de les poser (identifiant de fiche → champs).
3. Corpus A1 à C1 (8 052 cartes) : `russe/lots/*.json` au format exact de
   `python tests/corpus_langue.py --langue ru pose <lot.json>` ; le relevé vient
   de `... --langue ru reste <fichier> <niveau> <n>`. Brouillon compact
   `num|traduction|exemple[|perfekt|praeteritum|konj2][|kategorie]` converti par
   `.claude/russe/outils/lot.py` (sa garde « lettres mêlées » vise l'arabe :
   adapte-la au cyrillique).
4. Examen : `russe/examen/t*.json`, clés `section/i[/j]|base` (relevé :
   `.claude/russe/outils/examen_dump.jsonl` ; exemple de format :
   `exemple_examen_fa.json` ; outil de pose : `poser_examen.py`, ajoute `ru` aux
   langues qui gardent « »). Les `options` sont des listes de même longueur et
   même ordre.
5. Exercices d'articles : `russe/articles/t_ru.json` (relevé `articles_dump.jsonl`,
   exemple `exemple_articles_uk.json`) ; dans une copie de `patch_articles.py`
   rangée dans `russe/outils/`, ajoute les genres russes à `GENRES`.
6. Exercices de grammaire (`exercices.json`, ≈ 2 317, 40 jeux) :
   `russe/exercices/` (méthode `exos_dump.py` + `exos_convertir.py`, écrits pour
   `pt` : adapte à `ru` dans `russe/outils/` ; lis `tests/lot_exos.py`).
7. Scènes : `visuel/prototype/traductions/<scène>.ru.json` — fichiers NEUFS,
   ceux-là tu peux les committer directement (modèle `*.pt.json`), plus les
   textes de la page des scènes dans `russe/scenes-page.json`.
8. Prononciation : le dictionnaire de règles `RU` pour `tests/prononciation.py`,
   dans `russe/prononciation_ru.py`.
9. Câblage : `russe/outils/cablage_ru.py`, sur le modèle de `cablage_ar.py`,
   avec `ru` APRÈS `pl` (les rangs de `pl` seront ceux de `ar` + 2 ; ceux de `ru`,
   ceux de `ar` + 4) — documente l'hypothèse en tête du script.
10. `russe/outils/poser_tout.py` : pose 1 à 9 dans l'ordre, en s'arrêtant à la
    première erreur.

Ordre de travail conseillé : interface, grammaire, corpus A1-A2, scènes, puis
corpus B1-C1, examen, articles, exercices, prononciation, câblage, poser_tout.

## Qualité

- Chaque carte a un seul sens : celui que montrent le français, l'anglais ET
  l'exemple allemand. Traduction et exemple russes disent la même chose.
- **Les explications de grammaire s'écrivent CONTRE le russe**, pas traduites du
  français : le russe a six cas (dire à quel cas allemand chacun répond : le
  génitif russe de la quantité et de la négation n'a pas d'équivalent ; le
  prépositionnel ≈ Dativ de lieu), pas d'article (l'article allemand est la vraie
  difficulté), l'aspect verbal (≠ Perfekt / Präteritum), pas de verbe « être »
  au présent (« Ich BIN müde » : le verbe ne se saute pas), un ordre des mots
  libre (le verbe en 2e position est la règle allemande à marteler), « вы » de
  politesse ≈ Sie. Prononciation contre le russe : h aspiré, ü, ö, le r, les
  voyelles longues, ei/eu, l'absence de réduction des voyelles inaccentuées.
- Les remarques pour l'apprenant se disent en russe : (австр.), (швейц.), (разг.).

## Preuve (obligatoire avant la PR)

Dans une copie jetable du dépôt (`cp -r` hors du dépôt, ou `git worktree` dans
`/tmp`), lance `poser_tout.py`, puis `python tests/verifier.py`,
`node tests/syntaxe.js` et `python tests/corpus_langue.py --langue ru etat`.
Note les résultats dans la PR. Ne committe RIEN de cette copie : tes
fichiers des sections 1 à 10 restent la seule chose versionnée (avec les
scènes `*.ru.json`). Comme l'arabe et le polonais ne seront pas encore fusionnés
dans ta copie, le câblage `ru` aura des rangs « en avance » : c'est attendu,
signale seulement ce qui casse pour une autre raison.

## Règles de travail (non négociables)

- Branche **`russe`** (elle existe, ce brief y est). Un commit par étape ou par
  lot, poussé aussitôt (la session peut s'arrêter à tout moment). PR vers `main`
  à la fin. **Ne fusionne pas.** Jamais de push sur `main`. Pas de changement de
  version.
- **Pas de sous-agents, pas d'agents en parallèle.**
- Pas de heredoc Git Bash pour du code avec antislashs : de vrais fichiers.
- La voix de la visite guidée en russe est PAYANTE : ne la fais pas.
- Message final court, en français : ce qui est prêt, chiffres par section,
  résultat de la preuve, lien de la PR.
