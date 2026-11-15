# Le manuel de préparation au telc Deutsch B1·B2 Pflege : le format des données (le contrat)

15 nov. 2026, session « pflege-examen ». Plan : [PLAN-MANUEL.md](PLAN-MANUEL.md). Page :
`visuel/prototype/telc-pflege/telc.html`. Contrôle : `python tests/pflege_examen.py`.

**Ce contrat est stable** à partir du commit qui le crée. Les sessions qui écrivent du contenu ne changent pas ce
format. Si un besoin ne rentre pas dedans, on le demande à pflege-examen, qui change le code, le contrôle et ce
fichier ensemble.

## 1. Qui écrit quoi : un fichier par épreuve, jamais deux sessions sur le même fichier

```
visuel/prototype/telc-pflege/donnees/
  hoeren.json, lesen.json, …                ← les EXAMENS BLANCS (modèles 1, 2…) : pflege-examen seulement
  entrainement/<épreuve>.json               ← les séries d'ENTRAÎNEMENT d'une épreuve
  entrainement/voix-<épreuve>.json          ← le manifeste des pistes enregistrées de ces séries (hoeren, sprechen)
  manuel/sommaire.json                      ← les 10 chapitres, dans l'ordre : pflege-examen seulement
  manuel/<chapitre>.json                    ← le texte d'un chapitre (rubriques et blocs)
  manuel/_exemple.json                      ← chaque sorte de bloc, pour voir le rendu : telc.html?exemple=1
```

Chaque session possède ses fichiers, et les autres n'y écrivent pas. La répartition décidée par le chef est notée
au § 7.

**Tous ces fichiers existent déjà, vides** (`"series": []`, `"rubriques": []`), pour que la page ne demande jamais
un fichier absent. On les remplit, on ne les crée pas. Un chapitre aux rubriques vides s'affiche « Bientôt ».

**Les outils :**
- `python tests/pflege_examen.py` : le contrôle complet, examens, entraînement, réserve et manuel, avant chaque
  commit ;
- `python visuel/prototype/telc-pflege/outils/a_traduire.py` : ce qui manque dans chaque langue, `es` compris ;
  `--sortie f.json --langue l` puis `--appliquer t.json --langue l`. Il couvre l'entraînement et le manuel ; les
  blocs y sont repérés par leur chemin ;
- `python visuel/prototype/telc-pflege/outils/voix_soins.py --entrainement hoeren` : le chiffrage des voix des
  séries d'écoute, à blanc. Rien n'est enregistré sans l'accord.

## 2. Les examens blancs sont réservés

- Les séries de `donnees/<épreuve>.json` sont les **examens blancs**. Elles ne servent qu'à l'examen blanc et
  n'apparaissent jamais dans l'entraînement.
- Leurs `id` vont de 1 à 99 et sont les mêmes dans les cinq fichiers. Chaque série est complète : 59 questions,
  l'écrit A et l'écrit B, l'oral.
- Le contrôle refuse une série d'entraînement qui reprend une phrase allemande d'un examen blanc : question, choix,
  document ou réplique.

## 3. Les séries d'entraînement : `entrainement/<épreuve>.json`

```json
{ "_note": "…", "voix": { … facultatif, comme dans hoeren.json … },
  "series": [ { "id": 101, "titre_fr": "…", "titre_en": "…", …, "teile": [ … ] } ] }
```

- `id` : **101 et plus**, unique dans le fichier. Les pistes enregistrées s'appellent `s<id>-<clé>`, par exemple
  `s101-H1m1`, comme `s1-…` pour l'examen.
- `titre_*` est facultatif. Sans titre, la page affiche « Série 1 », « Série 2 »…, dans l'ordre du fichier.
- **Écoute, lecture et éléments de langue.** `teile` contient une ou plusieurs parties, chacune entière et
  exactement au format de l'examen :
  - même structure et mêmes clés que dans `hoeren.json`, `lesen.json` et `sprachbausteine.json` (le modèle d'une
    question est en tête d'`examen.js`) ;
  - même nombre de questions ;
  - même numérotation que l'examen : la lecture partie 2 va toujours de 28 à 32.

  Une série peut ne porter que la partie 2 : elle s'affiche alors comme « Série N · partie 2 ».
- **L'écrit** (`schreiben`) : `consigne_de` et `consigne_*`, puis `aufgaben`. Chaque tâche a :
  - `id`, unique dans le fichier, et `art`, qui vaut "A" (rapport d'admission) ou "B" (rapport biographique) ;
  - tout ce que porte une tâche de l'examen : `titre`, `resume_*`, `consigne_de`, `consigne_*`, la fiche, `infos`
    et leurs `mots`, `modele` (120 à 170 mots), `redemittel`.
- **L'oral** (`sprechen`) : `taches`, avec une ou plusieurs tâches au format de l'examen (`sp1a`, `sp1b`, `sp2a` et
  ses deux `themen`, `sp2b`, `sp3`). Leurs `cle` sont celles de l'examen, `sur` compris.
- **Les langues** : chaque champ traduit `X` d'un objet existe en `X_fr`, `X_en`, `X_tr`, `X_uk`, `X_fa`, `X_pt`,
  `X_ar`, `X_pl`, `X_ru`, avec les mêmes `{x}`. **`X_es` est prévu** : l'espagnol sera la 10e langue d'interface. Il
  n'est pas encore exigé, mais le contrôle compte ce qui manque. L'allemand n'est jamais traduit.
- **L'audio** : les nombres sont écrits en lettres dans tout texte dit, et chaque `wer` a sa voix avec son
  `voice_id`. Pas d'accent dans l'examen et dans l'entraînement : ce sont les voix de l'examen.
- Rien n'est enregistré sans l'accord du chef **et** de Jacques. Le manifeste `entrainement/voix-<épreuve>.json` a
  la forme de `voix-soins.json`.

## 4. Le sommaire : `manuel/sommaire.json`

```json
{ "chapitres": [ { "id": "hoeren", "nr": 1, "epreuve": "hoeren", "titre_fr": "…", "resume_fr": "…", … } ] }
```

| nr | id | epreuve | contenu |
|---|---|---|---|
| 0 | `examen` | — | L'examen en un coup d'œil |
| 1 | `hoeren` | hoeren | Hören |
| 2 | `lesen` | lesen | Lesen |
| 3 | `sprachbausteine` | sprachbausteine | Sprachbausteine |
| 4 | `schreiben` | schreiben | Schreiben |
| 5 | `sprechen` | sprechen | Sprechen |
| 6 | `kommunikation` | — | Communiquer au travail (Redemittel) |
| 7 | `beruf` | — | Écrire au travail |
| 8 | `grammatik` | — | La grammaire qui rapporte des points |
| 9 | `examens` | — | Les examens blancs. Pas de fichier : la page les liste |

- **Un chapitre qui a une `epreuve`** reçoit automatiquement, après ses rubriques, la rubrique « S'entraîner ». Elle
  contient toutes les séries de `entrainement/<épreuve>.json`, avec leur progression.
- **Un chapitre aux rubriques vides** s'affiche « Bientôt ».

## 5. Un chapitre : `manuel/<id>.json`

```json
{ "id": "lesen",
  "rubriques": [ { "id": "attendu", "blocs": [ … ] },
                 { "id": "pieges", "blocs": [ … ] },
                 { "id": "strategies", "blocs": [ … ] },
                 { "id": "guide", "blocs": [ … ] },
                 { "id": "fiche-aedl", "titre_fr": "…", "titre_en": "…", …, "blocs": [ … ] } ] }
```

- Les rubriques `attendu`, `pieges`, `strategies` et `guide` prennent le titre de l'interface : « Ce qu'on
  attend », « Les pièges », « Les stratégies », « Exercice guidé ».
- Toute autre rubrique porte son `titre_*`.
- Chaque rubrique a un `id` unique dans le chapitre. La page l'ouvre directement avec
  `telc.html?chapitre=lesen&rubrique=pieges`.

### Les blocs

Le champ `t` donne la sorte du bloc. Les textes d'aide sont en `texte_*` (ou `titre_*`) dans les 9 langues, plus
l'espagnol. Dans un texte d'aide, **l'allemand s'écrit entre doubles crochets** : `[[die Verabreichung]]`. La page
le montre en allemand (`lang="de"`, de gauche à droite même en arabe), et le contrôle vérifie que chaque langue a
les mêmes `[[…]]` que le français. Les champs allemands (`de`, `frage`, `o`, les documents) ne prennent pas de
crochets.

| t | champs | ce que la page montre |
|---|---|---|
| `p` | `texte_*` | un paragraphe |
| `titre` | `texte_*` | un intertitre |
| `liste` | `items`: [{`texte_*`}], `ordre` (vrai : 1, 2, 3…) | une liste, numérotée ou non |
| `de` | `de` (allemand, `\n` permis), `texte_*` (la traduction, facultative) | un exemple allemand, et « Traduction » à déplier |
| `piege` | `titre_*`, `de` (facultatif), `texte_*` | un encadré « Piège » : un exemple de notre cru et son explication |
| `tableau` | `entetes`: [cellule], `lignes`: [[cellule…]] ; une cellule = {`texte_*`} ou {`de`} | un tableau |
| `doc` | `doc`: {`art`, `kopf`, `betreff`, `absaetze`} (comme dans les examens) | un document allemand (courriel, extrait de plan…) |
| `redemittel` | `ref` (un groupe : `patient`, `famille`, `collegues`, `releve`, `sbar`, `visite`, `negociation`, `telephone`), `titre_*` (facultatif) | les cartes de ce groupe, lues dans la **source unique** `pflege/datos/redemittel.json` (FORMAT-DONNEES.md § 2 bis), rangées par fonction puis par niveau, avec leur son |
| `exercice` | `cle`, `consigne_de` (facultatif), `consigne_*`, `doc` (facultatif), `items`: [question] | des questions à faire sur place, puis « Corriger » |
| `serie` | `epreuve`, `serie` (id d'entraînement), `teil` (facultatif), `texte_*` | un bouton vers une série d'entraînement, ouverte à cette partie |
| `renvoi` | `vers` (`dialogue:<id>`, `grammaire:<id>`, `ecrit:<id>`, `theme:<id>`, `scene:<id>`, `chapitre:<id>`), `titre_*` | « Dans l'app : … ». Un `chapitre:` s'ouvre dans la page ; les autres envoient `parler("ouvrir", {vers})` à l'app |

- **Une question d'`exercice`** suit le modèle des examens : `nr` (1, 2, 3… dans le bloc), `typ` (« abc » ou « rf »),
  `frage`, `o` (trois choix pour « abc »), `bon`, `erkl_*` et, facultatif, `pas_*`. `pas_*` est une liste de
  phrases : le raisonnement pas à pas, montré après « Corriger » ; il sert à l'exercice guidé.
- **`relire: true`** se pose sur tout bloc, sur une phrase de Redemittel ou sur une question d'exercice dont le
  contenu métier doit être validé par une infirmière : dose, geste, soin, droit. `python tests/pflege_examen.py
  --relire` en sort la liste.
- **Les `cle`** d'`exercice` sont uniques dans tout le manuel ; la progression s'y rattache.
- **Les Redemittel n'ont qu'une source** (décision de l'architecture, 15 nov.) : `pflege/datos/redemittel.json`,
  construit par la chaîne de la session dialogues (`textes.py`), sons compris (`pflege/datos/sons.json`, voix
  d'Aurora). Ses cartes portent `id` (`soins_rm_<groupe>_<rang>`, stable), `groupe`, `fonction`, `niveau`,
  `registre`, `de`, `lecture` (les nombres en lettres), `trad`, `situation`, `son`, `relire`. Les phrases sans
  dialogue s'écrivent dans `pflege/sources/redemittel/<groupe>.json`, au format source du § 2 bis. Avant d'en
  écrire une, on regarde les environ 180 cartes des dialogues d01-d26 : celles d'un groupe comptent déjà pour le
  chapitre. Un même `de` deux fois est refusé.

## 6. La progression (stockage local, `wortando_soins_telc_manuel`)

```
{ vu: { <chapitre>: true },
  series: { "<épreuve>:<id>": { <clé de la partie>: { bons, sur } } },
  ex: { <clé d'exercice>: { bons, sur } } }
```

- La page l'écrit, et les données ne la portent jamais.
- La ligne d'un chapitre dans le sommaire affiche :
  - pour un chapitre d'épreuve, les parties faites sur toutes les parties de ses séries ;
  - pour un autre chapitre, les exercices faits sur ses exercices, ou « Lu » s'il n'en a pas.
- L'examen blanc garde son état par modèle (`blanc_<id>`). Le résultat part vers l'app au format du contrat
  (`resultat_examen`, `soins_telc`, `serie`).

## 7. La répartition (consigne de Jacques du 15 nov. : « rapidement, pas en 2 ou 3 semaines »)

Cinq sessions en parallèle (A et B lancées par le chef le 15 nov. ; C et D proposées à Jacques), chacune dans son worktree tiré de `claude/pflege-examen-1cc3a5`. Chacune n'écrit **que**
ses fichiers. Elle ne touche ni `examen.js`, ni `telc.html`, ni `interface.json`, ni `tests/`, ni les outils
existants : un besoin dans l'un d'eux se demande à pflege-examen.

| Session | Chapitres | Fichiers (sous `visuel/prototype/telc-pflege/`, sauf mention) | Voix (plafond) | Images |
|---|---|---|---|---|
| A · manuel-hoeren (local_32d21ba9) | 1 | `donnees/entrainement/hoeren.json`, `voix-hoeren.json` ; `donnees/manuel/hoeren.json` | 53 000 crédits (≈ 8,75 $) | — |
| B · manuel-lesen-sprach (local_7b006a7a) | 2, 3, 8 | `donnees/entrainement/lesen.json`, `sprachbausteine.json` ; `donnees/manuel/lesen.json`, `sprachbausteine.json`, `grammatik.json` | — | — |
| C · L'écrit | 4, 7 | `donnees/entrainement/schreiben.json` ; `donnees/manuel/schreiben.json`, `beruf.json` | — | — |
| D · L'oral et la communication | 5, 6 | `donnees/entrainement/sprechen.json`, `voix-sprechen.json` ; `donnees/manuel/sprechen.json`, `kommunikation.json` ; `img/entr-*.webp` ; `pflege/examen/images/prompts_entrainement.py` et ses `entr-*` ; les phrases sans dialogue `pflege/sources/redemittel/<groupe>.json` (construction et sons : la session dialogues) | 64 000 crédits (≈ 10,50 $), dont environ 24 000 pour les sons des Redemittel, produits par la chaîne des dialogues | 16 photos 2A (plafond 3 $) ; les 1A reprennent les scènes |
| E · pflege-examen | 0, 9 | `donnees/manuel/sommaire.json`, `examen.json` ; l'examen blanc 2 (`donnees/<épreuve>.json`, série 2) ; le code, ce contrat, le contrôle, l'intégration | 15 600 crédits (≈ 2,60 $) | 7 photos (plafond 1,50 $) |

- **Les Redemittel du chapitre 6** : source unique `pflege/datos/redemittel.json` (§ 5), décidée par
  l'architecture le 15 nov. Le chapitre 6 n'y met que des blocs `{"t":"redemittel","ref":"<groupe>"}` et leur
  explication.
- **Les voix** : chaque lot est annoncé au chef avec son coût réel avant d'être lancé. Il faut l'accord de Jacques,
  confirmé dans la session qui dépense si ses permissions l'exigent. Après chaque lot : `python
  audio/controler_sons.py`.
- **Les essais au navigateur** : un port à soi. Le 8794 est déjà pris par deux serveurs : un `python -m
  http.server` sur un port occupé répond pour l'autre dossier. Une sonde Playwright passe sous le verrou
  `~/.wortando/verrou-parcours`.
