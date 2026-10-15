# Rapport : ejercicios-b (492 exercices) + temas (18 mots) — 15 oct. 2026

## Fait

- `ejercicios-06.txt` … `ejercicios-10.txt` : les 492 lignes de `sources/ejercicios-b.txt`
  (gustar 57, acentos 53, futuro 60, condicional 60, imperativo 60, perífrasis 51,
  números 50, demostrativos 50, preposiciones 51), 100 par lot, 92 dans le dernier.
  Chaque lot : `pose --essai` → « N entrees verifiees ».
- `temas-07.txt` : les 18 mots de `sources/temas.txt`, `pose --essai` passé.
- Aucune 7e colonne : dans toute la source b, `question_en` est vide ou identique à `question`.
- Hints : `=` quand l'indice est purement espagnol (`(visitar — yo)`) ; traduits sinon.
  Deux variantes partiellement françaises : `(hablar — tú, négatif)` → `(hablar — tú، نفي)`,
  `(importar — te … : 3e personne)` → `(importar — te …: الغائب)`.
- Flèches : « ← » partout ; là où les deux côtés auraient été latins (`abrir → abre`,
  `-ir → -iendo`), reformulé sans flèche (« من «abrir»: abre », « النهاية -ir تصير -iendo »)
  pour que le bidi ne retourne pas le sens.

## Choix d'écriture (contre l'arabe)

- **gustar** : appui sur تعجبني الشوكولاتة — la chose aimée est le sujet, le verbe s'accorde
  avec elle ; hint et explication le disent explicitement (« كما في العربية »).
  Les glosses « mot à mot » de la source deviennent le littéral arabe (« الشوكولاتة تعجبني »).
  La référence au portugais (`gustar¦34`, « as costas ») est retirée.
- **acentos** : « علامة النبر » pour l'accent écrit ; « مع نبر / بلا نبر ».
- **futuro / condicional** : « المستقبل », « الشرطي (condicional) » ; « comme en français » retiré,
  remplacé pour l'adoucissement par « كما نقول بالعربية «أودّ» بدل «أريد» ».
  Subjonctif : « المنصوب (subjuntivo) », comme dans les lots tiempos déjà faits.
- **imperativo** : « أمر tú », « صيغة الاحترام » pour usted, « المضارع المنصوب بالجمع » pour ustedes.
- **perífrasis** : le gérondif est nommé « الـ gerundio » (avec « الصيغة المنتهية بـ -ando/-iendo »
  à sa première occurrence) ; « المصدر » pour l'infinitif.
- **preposiciones** : « الـ a الشخصية » pour le a personnel ; « le français dit "en bois" » devient
  « كما نقول بالعربية «من الخشب» » (l'arabe aide ici, pas le français).
- **usted** rendu par « حضرتك » quand la phrase le demande (gustar¦9, condicional¦3, ¦48),
  sinon simple impératif/2e personne.
- temas : pas d'article « ال » sur le mot seul, comme `temas-01..06`.

## Doutes (à relire par un natif)

- `gustarExercises|55`, `|56` : « caer bien » glosé « يقع عليّ حسنًا » (littéral, assumé) puis « يروق لي ».
- `gustarExercises|42` : « Me quedan grandes » → « هذا البنطال كبير عليّ » (le pluriel espagnol est
  expliqué dans l'explication, pas visible dans la traduction).
- `acentosExercises|50` : « ingles » rendu « الأُربيّتان (أعلى الفخذين) » — mot rare, à vérifier.
- `acentosExercises|6` : « sí mismo » → « نفسه، ذاته ».
- `futuroExercises|28`, `|29`, `|30`, `|52` (supposition) : « يا ترى » / « لا بدّ أنّ » — registre à confirmer.
- `condicionalExercises|39` : « Yo no diría eso » → « أنا، ما كنت لأقول ذلك ».
- `condicionalExercises|42` : « ¿Tomarías un café conmigo? » → « هل تودّ أن تشرب قهوة معي؟ » (sens, pas forme).
- `imperativoExercises|5`, `|44` : « ten/tenga paciencia » → « اصبر ».
- `numerosExercises|28`, `|45` : « menos veinte » → « إلا ثلثًا », « menos veinticinco » → « إلا خمسًا وعشرين دقيقة ».
- `perifrasisExercises|21` : traduction légèrement raccourcie (« ها هي أولى الندف »).
- `demostrativosExercises|26` : « García » translittéré « غارثيا » (prononciation d'Espagne).
- temas `197|gorro` : « قبّعة صوفية (طاقية) » ; `1760|mesilla` : « طاولة السرير (كومودينو) » — le second
  terme est régional, à garder ou retirer.

## Sources qui semblaient fautives

- Aucune erreur de fond vue. `gustarExercises¦34` mentionne le portugais (« as costas ») dans
  une source française : hors sujet pour toute langue autre que pt.
- `numerosExercises¦28` : la traduction française « six heures moins vingt » et l'explication
  « 5 h 40 » sont cohérentes ; rien à signaler.
