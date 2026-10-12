# Brief cloud — l'arabe au même niveau de contenu que les autres langues

Demandé par Jacques le 12 oct. 2026 : « mettre toutes les langues au même niveau
pour le contenu ». en, tr, uk, fa et pt sont complets. **Il reste l'arabe.**
Lis d'abord `CLAUDE.md` (règles du dépôt), puis ce brief en entier.

## Règles de travail (non négociables)

- Branche **`arabe-contenu`** (elle existe déjà, ce brief y est). Commits
  fréquents, **un commit par lot posé**, poussés aussitôt : si la session
  s'arrête (limite de 5 h), rien de fait ne se perd. Termine par **une pull
  request vers `main`**. **Ne fusionne pas.** Jamais de push sur `main`.
- **Pas d'agents en parallèle, pas de sous-agents** : la session partage la
  limite de 5 h du forfait de Jacques.
- **Ne change pas le numéro de version** (`APP_VERSION`, badge, `version.json`).
- **L'allemand ne doit pas changer.** Tu n'ajoutes QUE des champs arabes. Tout
  fichier réécrit doit être identique à l'original hors champs `_ar` / `Ar`
  (les outils fournis le vérifient ; si tu en écris un, il doit le vérifier).
- Avant chaque push : `python tests/verifier.py` et `node tests/syntaxe.js`.
- Pas de heredoc Git Bash pour écrire du code contenant des antislashs :
  écris de vrais fichiers.
- Si `python -X utf8 fusion-espagnol/parcours.py --app de ...` peut tourner
  dans ton environnement (Playwright), lance-le et compare à
  `fusion-espagnol/references/de-v765.json` : 0 écart attendu. Sinon, dis-le
  dans la PR : Jacques le lancera sur le PC avant la fusion.

## Qualité de la traduction

- Arabe standard moderne (فصحى), registre neutre, celui d'un manuel.
- Chaque carte a un **seul sens** : celui que montrent la traduction française,
  l'anglaise ET la phrase d'exemple allemande. « der Gang » = ممرّ si l'exemple
  parle d'un couloir. La traduction et l'exemple arabes doivent dire la même chose.
- Les précisions utiles à l'apprenant se gardent, en arabe, entre parenthèses :
  (نمساوية), (سويسرية), (عامية), (مذكر)... comme dans les brouillons fournis.
- Pas de lettres latines mêlées à un mot arabe (l'outil `lot.py` le refuse).
  Les termes de grammaire allemands (Akkusativ, Dativ, Modalpartikel) peuvent
  rester en caractères latins, comme mots entiers.
- Les guillemets « » sont permis en arabe.
- Modèle de ton et de format : les brouillons A1-A2 déjà posés (v772, champs
  `traduction_ar` / `exemple_ar` dans les six fichiers) et
  `.claude/arabe/brouillons/b_th_b1_*.txt`.

## État au départ (v772)

- Corpus : A1 + A2 posés (2 086 / 8 052 cartes). Câblage d'`index.html` fait
  (rangs des cartes, verbes, recherche, phrases à construire, catégories).
- **Brouillons déjà rédigés, PAS encore posés** :
  `.claude/arabe/brouillons/b_th_b1_1.txt` … `b_th_b1_6.txt` = thèmes B1,
  numéros #46 à #2327 du relevé. Relis-les vite, pose-les en premier.

## Le travail, dans cet ordre

### 1. Corpus B1, B2, C1 (≈ 6 000 cartes)

Outil du dépôt : `python tests/corpus_langue.py --langue ar etat | reste <fichier> <niveau> <n> | pose <lot.json>`.
- `reste themes.json B1 2200 > reste.txt` donne les cartes manquantes
  (« #num der Wort [B1 Thème] fr=... | en=... » + « exem: ... »).
- Tu écris un brouillon compact, une carte par ligne :
  `num|traduction|exemple` ; pour les verbes
  `num|traduction|exemple|perfekt|praeteritum|konj2` (exemples arabes de chaque
  temps) ; pour funktionswort `...|kategorie`.
  Regarde une entrée A2 déjà posée de chaque fichier pour voir les champs exacts.
- `python .claude/arabe/outils/lot.py reste.txt <fichier.json> brouillon.txt lot.json`
  puis `python tests/corpus_langue.py --langue ar pose lot.json`.
- Restant : thèmes B1 (#2328 et suivants, plus les #1-#45 s'il y en a) puis
  B2 449, C1 948 ; verbes B1 515, B2 180, C1 272 ; adjectifs B1 337, B2 104,
  C1 291 ; adverbes B1 147, B2 120, C1 52 ; redewendung B1 151, B2 149, C1 100 ;
  funktionswort B1 46, B2 5. Vérifie avec `etat`.
- Lots de 150-300 cartes. Un commit par lot.

### 2. Examen (`pruefung.json`, 720 champs)

- `.claude/arabe/outils/examen_dump.jsonl` : les 720 champs français, avec leur id
  (`section/i[/j]|base`). Format des traductions : un JSON `{id: texte}` ;
  pour `options`, une LISTE de même longueur, même ordre (la bonne réponse
  reste à la même place). Exemple complet en persan :
  `.claude/arabe/outils/exemple_examen_fa.json`.
- `python .claude/arabe/outils/poser_examen.py pruefung.json ar t1.json t2.json ... --ecrire`
  (sans `--ecrire` : contrôle seul).
- Puis dans `index.html` : ajouter `"ar"` à `LANGUES_PRUEFUNG`, et
  `correctAr` / `optionsAr` dans les constructeurs Lesen et Hören, à côté de
  `correctPt` / `optionsPt` (cherche `optionsPt`).

### 3. Exercices d'articles codés en dur (`index.html`)

- `.claude/arabe/outils/articles_dump.jsonl` : les textes français, ids
  `E|def.nom.m`, `D|sujet`, `R|ARTICLES_X|i`, `M|i`. Exemple complet en
  ukrainien : `.claude/arabe/outils/exemple_articles_uk.json`.
- `python .claude/arabe/outils/patch_articles.py index.html ar uk t_ar.json .claude/arabe/outils/articles_dump.jsonl --ecrire`
  (`uk` = la langue posée juste avant ; les genres arabes sont déjà dans l'outil).

### 4. Exercices de grammaire (`exercices.json`, ≈ 2 317 exercices, 40 jeux)

- Méthode du portugais (v768) : `.claude/arabe/outils/exos_dump.py` (relevé de
  ce qui manque par jeu) et `exos_convertir.py` (brouillon compact → fichier de
  correction), puis `tests/lot_exos.py`. **Ces deux scripts sont écrits pour
  `pt`** : adapte-les à `ar` (`_ar`, `Ar`), et lis `tests/lot_exos.py` avant.
- Les « moules » de `exos_convertir.py` fabriquent une explication à partir du
  français par remplacements ; pour l'arabe, écrire les explications
  directement est souvent plus sûr. Le garde-fou « FRANCAIS RESTANT » doit rester.
- Ajoute `"ar"` (et `optionsAr` / `correctAr`) à `tests/trous_langue.py`.

### 5. Petits câblages

- `visuel/prototype/construire.py` : `CHAMPS_MOT` reçoit `"ar": "traduction_ar"` ;
  reconstruis les scènes ; les fichiers `scene-*.js` ne doivent différer que par
  les clés `ar`.
- `tests/prononciation.py` : les exemples incluent `traduction_ar` ;
  régénère `prononciation.json`.

## Fin

- `python tests/corpus_langue.py --langue ar etat` → 100 %.
- PR vers `main` : ce qui est fait, chiffres par fichier, ce qui n'a pas pu
  être vérifié (parcours), et toute carte douteuse que tu as laissée.
- Supprime `.claude/arabe/` dans le dernier commit de la branche (outils
  temporaires), sauf si un script mérite d'entrer dans `tests/`.
