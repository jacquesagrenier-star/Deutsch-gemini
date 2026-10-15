# Rapport — ejercicios-a (perfektExercises¦20 → falsosAmigosExercises¦51), 15 oct. 2026

## Fait

399 exercices traduits, dans l'ordre de la source, en quatre lots :

| Lot | Contenu | Lignes | `pose --essai` |
|---|---|---|---|
| `ejercicios-02.txt` | perfektExercises 20-69, konjunktiv2Exercises 0-49 | 100 | 100 entrees verifiees |
| `ejercicios-03.txt` | konjunktiv2Exercises 50-69, infinitivExercises 0-69, adverbienNuanceExercises 0-9 | 100 | 100 entrees verifiees |
| `ejercicios-04.txt` | adverbienNuanceExercises 10-55, serEstarExercises 0-50, porParaExercises 0-2 | 100 | 100 entrees verifiees |
| `ejercicios-05.txt` | porParaExercises 3-49, falsosAmigosExercises 0-51 | 99 | 99 entrees verifiees |

Les quatre lots passés ensemble en un seul `pose --essai` : 399 entrées vérifiées. Couverture contrôlée
par script : les 399 `jeu|idx` de la source sont présents une fois chacun, dans le même ordre.
Rien n'a été posé (jamais `pose` sans `--essai`), rien n'a été commité.

Conventions suivies :
- `debut` = 20 premiers caractères de la question, copiés par script depuis la source (pas à la main).
- `hint_ar` = `=` pour perfekt / konjunktiv (indices purement espagnols) ; traduit partout ailleurs.
- `question_ar` (7e colonne) seulement pour infinitivExercises (« … — ما المصدر؟ ») et
  adverbienNuanceExercises (« … إلى أيّ عائلة ينتمي «x»؟ »), les deux seuls jeux où `question_en` diffère.
- Flèches « ← ». Mots espagnols en lettres latines entre « ». Aucun « | » dans les textes.
- Terminologie reprise du lot 01 : الماضي البسيط (pretérito), الماضي الناقص (imperfecto), avec
  « (كان + المضارع) » ajouté à chaque explication d'imparfait.
- Subjonctif : « المنصوب (subjuntivo) » dans l'explication, « المضارع المنصوب من «venir»: venga · … » pour la
  conjugaison ; comparaisons avec le français retirées, remplacées par l'appui arabe (« أريد أن تأتي »,
  « قبل أن », « لكي ») ; pour « ojalá », mention de son origine arabe (« إن شاء الله »).
- ser/estar : hint « (الهوية، الأصل، الساعة، الحدث ← ser؛ المكان، الحالة ← estar) » ; aux idx 0 et 14, rappel
  que l'arabe n'a pas de verbe « être » au présent (جملة اسمية) alors que l'espagnol en exige un.
- por/para : hint « (الغاية، الوجهة، الموعد ← para؛ السبب، المرور، المبادلة، الوسيلة ← por) ».
- Faux amis : hint « (الكلمة التي تشبه الفرنسية أو الإنجليزية غالبًا ما تكون الفخّ) » ; chaque explication
  donne le sens réel en arabe et nomme le mot français ou anglais trompeur.
- Les blancs « ___ » des traductions françaises (porPara 10, 14, 16, 27, 32, 40) sont gardés en arabe,
  pour ne pas souffler la réponse.

## Doutes (à relire)

- `konjunktiv2Exercises|64` : la source espagnole a « encuentres » (subjonctif présent) mais le français dit
  « que tu aies trouvé » ; traduit au passé comme le français (« يسعدني أنّك وجدت عملًا »).
- `konjunktiv2Exercises|*` : le choix du terme « المنصوب (subjuntivo) » est le mien (aucun terme arabe pour le
  subjonctif n'existait encore dans l'app) ; à valider ou à remplacer d'un coup (chercher/remplacer).
- `adverbienNuanceExercises|49` (« legalmente » → Discurso) : la classification de la source me paraît
  discutable (c'est plutôt une manière) ; traduit fidèlement.
- `adverbienNuanceExercises|36` (« seguramente » → Duda) : rendu « على الأرجح » pour rester dans le doute.
- `infinitivExercises|35`, `|53` : le français est au passé composé (« nous avons ramé / conversé »), mais
  l'indice dit « présent, nous » ; traduit au présent (نجدّف / نتحادث), comme le lot 01 pour « remamos ».
- `infinitivExercises|63`, `|65` : la source donne comme infinitif « entrenar un modelo » / « persuadir con
  datos » (une locution, pas un verbe) ; recopié tel quel.
- `serEstarExercises|42`, `falsosAmigosExercises|0` : le piège « embarazada » est expliqué contre l'anglais
  « embarrassed » (en arabe, aucune ressemblance ne joue).
- `falsosAmigosExercises|36` : piège présenté contre l'anglais « actual » (le français « actuel » n'est pas
  un piège, il a le même sens).
- `falsosAmigosExercises|46` : « emocionado » rendu « متحمّس » ; le français « j'ai vraiment hâte » est
  plus libre.
- Faux amis en général : une vingtaine de pièges n'existent que pour un francophone (largo/large,
  constipado, carpeta/carpette, jubilación/retraite, gamba/jambe, mantel/manteau, rubio/rouge,
  sueldo/soldes, entender/entendre, exprimir/exprimer, subir, atender/attendre, quitar/quitter,
  contestar/contester, bizarro, suceso/succès, nombre, carta/carte, firma/ferme, tabla/tableau). Je les
  présente comme « ressemblance trompeuse avec le français » et donne le vrai sens ; pour un arabophone
  sans français, l'exercice reste utile comme vocabulaire, mais le « piège » est moins senti.
- `python espanol/ar/poser.py controle` signalera des « mots latins » dans ces lots (listes de conjugaison
  « venga · vengas… », « subjuntivo », « gerundio »), exactement comme pour le lot 01 : attendu.

## Sources qui me semblent fautives

- `porParaExercises|10`, `|14`, `|16`, `|27`, `|32`, `|40` : la traduction française contient un blanc
  « ___ » (sans doute voulu pour ne pas donner la réponse, mais c'est le seul jeu où c'est fait).
- `konjunktiv2Exercises|64` : voir ci-dessus (temps du français ≠ temps de l'espagnol).
- `adverbienNuanceExercises|49` : voir ci-dessus.
