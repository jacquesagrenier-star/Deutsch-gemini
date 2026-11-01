# Traductions décalées : la vérification de toutes les données

1er novembre 2026. Suite du retour de Daria (testeuse ukrainienne) : « Der Chef ist heute nicht im Büro. » traduit « Мій начальник дуже суворий » (« mon chef est très sévère »). Le chef d'orchestre a corrigé les 34 premières phrases en v1056. Ce rapport couvre tout le reste.

## En bref

- **9 traductions fausses trouvées et corrigées** (en plus des 34 phrases du v1056) :
  - 3 en turc dans `themes.json`,
  - 2 en persan dans `funktionswort.json`,
  - 2 en portugais et 2 en arabe dans la prononciation espagnole.
- **Le défaut a une seule vraie cause : la traduction choisie par le mot, pas par la phrase.** Les lots de traduction (`corrections_uk/`, `corrections_fa/`, `corrections_tr/`…) disent `{mot, exemple_<langue>}`, sans la phrase allemande. Un mot présent dans deux thèmes (Chef : Berufe A1 et Büro A1) a reçu la même phrase deux fois, et l'une des deux est fausse. Toutes les erreurs trouvées sauf l'espagnol viennent de là, y compris les 34 du v1056.
- **Le défaut est localisé.** Un échantillon de 105 phrases tiré au hasard dans les lots les plus à risque est juste à 100 %. Les 1 170 traductions de phrases qui portent un chiffre ou un nom propre ne montrent aucun décalage.

## Les 9 corrections

| Fichier | Où | Langue | Phrase source | Avant (traduit en fait) | Après |
|---|---|---|---|---|---|
| `themes.json` | berufe_a1 / Chef | tr | Mein Chef ist sehr streng. | Patron bugün ofiste değil. (le patron n'est pas au bureau) | Patronum çok sert. |
| `themes.json` | berufe_a1 / Kollege | tr | Mein Kollege sitzt neben mir. | İş arkadaşım çok yardımsever. (mon collègue est serviable) | İş arkadaşım yanımda oturuyor. |
| `themes.json` | berufe_a1 / Student | tr | Der Student lernt für die Prüfung. | Öğrenci çok çalışıyor. (l'étudiant travaille beaucoup) | Öğrenci sınava çalışıyor. |
| `funktionswort.json` | partikeln / denn | fa | Was machst du denn? | (je reste à la maison, car je suis malade) | حالا چه کار می‌کنی؟ |
| `funktionswort.json` | praepositionen / während | fa | Während des Urlaubs lese ich viel. | (je cuisine pendant que tu mets la table) | در طول تعطیلات زیاد کتاب می‌خوانم. |
| `tests/prononciation_es.py` → `espanol/datos/prononciation.json` | ll-y, court + explication | pt (2), ar (2) | « un « y » appuyé, presque « j » » (réécrit le 31 oct.) | l'ancienne explication, « comme le y de « yeux » » | un « i » / une ياء appuyés, presque « j » ; « dj » en début de mot (llave) |

Les trois turcs sont la copie **inverse** de celle trouvée par Daria : le v1056 a corrigé l'ukrainien et le persan d'Arbeit Büro A1, mais le turc avait été recopié dans l'autre sens, de Büro vers Berufe. Les deux persans viennent de la conjonction homonyme (denn, während) : `corrections_fa/funktionswort_A2_01.json` et `_B1_01.json`.

Ces neuf traductions sont les miennes et **n'ont pas été relues par un locuteur natif**. Le portugais et l'arabe de ll / y suivent le français du 31 oct. (relecture de Jacques).

### Contrôles

| Contrôle | Résultat |
|---|---|
| `python tests/verifier.py` | 44 231 contrôles passés, aucun problème |
| `node tests/syntaxe.js` | OK |
| Parcours allemand, contre de-v1055 | 0 écart au second passage |
| Parcours espagnol, contre es-v1042 | 0 écart |

Le premier passage allemand avait donné 1 écart : un autre tirage dans « weil ou obwohl ? ». Cet exercice n'est touché par aucune correction, et l'écart ne s'est pas reproduit au second passage : c'était un tirage instable.

## Fichiers et champs couverts

### Famille 1 : périmées (la source a changé après la traduction)

On rejoue tout l'historique git de chaque fichier (`traductions-decalees/rejouer.py`). Pour chaque traduction on retient la source en face de laquelle elle est née, et on la compare à la source actuelle. Par source, on entend la phrase allemande et le français de référence.

On repère une traduction de trois façons, parce que chacune rate quelque chose :

- **par son chemin** (thème, mot) : rate les traductions recopiées d'un autre enregistrement ;
- **par son seul texte** : c'est un filet ;
- **par son mot**, comme le script du chef : il retrouve les **90 alertes du v1056, sans exception**.

On écarte d'office trois sortes d'alertes :

- les changements de ponctuation ou de casse ;
- les temps de verbe qui n'étaient qu'une forme (« hat ausgehandelt ») quand la traduction de la phrase est née (810 alertes) ;
- les indices et explications communs à plusieurs exercices quand leur français n'a pas bougé (156 alertes).

Tout le reste a été relu.

| Données | Traductions examinées | Champs |
|---|---|---|
| `themes.json` | 82 726 | exemple, traduction, perfekt, praeteritum, konjunktiv2 (verbes et adjectifs des chapitres) |
| `verbe.json` | 57 816 | exemple et les trois temps, traduction |
| `exercices.json` | 77 076 | translation, hint, explanation, question |
| `adjectif.json` | 16 677 | exemple, traduction |
| `redewendung.json` | 9 673 | exemple, traduction |
| `adverbe.json` | 7 990 | exemple, traduction |
| `pruefung.json` | 6 480 | frage, options, erkl, trad, consigne, aufgabe |
| `premiers-pas.json`, `a1-voyage.json`, `conjugaison.json`, `reperes.json`, `prononciation.json` | 16 379 | les dictionnaires {fr, en, …} et leurs phrases |
| `funktionswort.json` | 2 737 | exemple, traduction |
| `grammaire.json` | 1 880 | textes (neuf langues, contre le français) |
| Scènes allemandes (`visuel/prototype/traductions/`) | 2 507 × 8 langues | alt, consigne, couches, explications, sens |
| Espagnol (`espanol/datos/`, 14 fichiers) | 69 939 | mêmes champs, en, pt, ar |
| Scènes espagnoles (`visuel/prototype/espanol/*.json`, 44) | ≈ 7 000 | n, sens |
| Anglais et portugais (`anglais/datos/`, `portugais/datos/`) | toutes | exemple_fr (seule langue d'interface) |

Ce qu'on trouve, après les 34 du v1056 :

- **Allemand** : aucune autre traduction restée en place sur une phrase réécrite. Les 503 alertes relues étaient des sens précisés en français (« plat » → « un plat (un mets) ») ou des mots remplacés par un synonyme que la traduction couvrait déjà. Par exemple, le turc « ay » vaut pour Mond comme pour Monat.
- **Espagnol** : ll / y, en portugais et en arabe (ci-dessus).
- **Scènes** : rien. `construire.py` garde le français source à côté de chaque traduction et refuse une traduction périmée. Le contrôle (`scenes_check.py`) compte 0 périmée et 0 orpheline.
- **Anglais, portugais** : rien. Les 11 alertes portugaises sont le passage du Brésil au Portugal (grama → relva, abobrinha → curgete), le français reste juste.

### Famille 2 : jamais alignées (traduction écrite sans voir la phrase)

Il n'existe pas de détecteur qui juge le sens. On a donc mesuré avant de tout relire, avec quatre outils :

1. **`homonymes.py`, le mécanisme lui-même, sans filtre.** Pour chaque mot présent dans plusieurs enregistrements, il cherche une traduction identique en face de deux phrases différentes. Il trouve 27 cas en allemand : 5 fautes (les turcs et les persans ci-dessus), les autres sont des phrases équivalentes (« Mathematik ist mein Lieblingsfach » / « … liebstes Fach »). Il ne trouve rien en espagnol ni en anglais. En portugais, un seul cas, équivalent.
2. **`lots.py`, chaque entrée des lots indexés par le mot**, confrontée à toutes les phrases de ce mot. Cela fait 15 773 champs dans `corrections_uk/`, `_fa/`, `_tr/` et `_vhs/` (285 ne sont plus dans les données). Seuls 9 ont une copie en face d'une autre phrase, dont les deux persans ; les 7 autres sont des phrases équivalentes.
3. **`doublons.py`, la même traduction en face de deux phrases différentes, tous mots confondus.** Un arbitre écarte les cas où plusieurs autres langues coïncident aussi (phrases équivalentes). Il a sorti 444 groupes en allemand et 64 en espagnol, tous relus : pas d'autre faute.
4. **`entites.py`, les chiffres et noms propres** (Berlin, Hamburg, Anna, Wien…) de l'allemand, absents de la traduction. Sur 1 170 traductions concernées, il donne 48 alertes, toutes fausses (nombres en lettres, déclinaisons comme « в Гамбурзі »).

Enfin, un **échantillon tiré au hasard** dans les lots à risque, phrase allemande en face : 30 noms A1 ukrainiens, 30 noms A1 persans, 30 verbes A1 ukrainiens et 15 phrases des lots turcs. Les 105 sont justes.

### Nombre trouvé, par fichier et par langue

| Fichier | tr | fa | uk | pt | ar | en, pl, ru, fr |
|---|---|---|---|---|---|---|
| `themes.json` (v1056, chef) | 32 | 35 | 3 | – | – | – |
| `verbe.json` (v1056, chef) | – | – | – | – | – | 2 (fr, en) |
| `themes.json` (cette vague) | 3 | – | – | – | – | – |
| `funktionswort.json` | – | 2 | – | – | – | – |
| `espanol/datos/prononciation.json` | – | – | – | 2 | 2 | – |
| tout le reste | 0 | 0 | 0 | 0 | 0 | 0 |

(Les lignes du v1056 sont recomptées d'après `corriger_perimees.py` du chef : 72 champs.)

## Ce qui reste non relu

- **Les ≈ 15 500 entrées de lots sans copie** : leur traduction n'a pas de copie à comparer. Seul l'échantillon de 105 les a jugées. Il n'a trouvé aucune faute, ce qui borne le taux sous ≈ 3 % (à 95 %), sans l'exclure tout à fait.
- **Les traductions de mots** (`traduction_<langue>`) : seul l'historique les a vues. Quatre choix turcs sont faibles sans être faux : kriegen « edinmek », festsetzen « tespit etmek », entscheiden « karara bağlamak », Fach « branş ». Je n'y ai pas touché : ils ont été choisis contre les collisions (deux mots allemands ne doivent pas recevoir la même réponse), et les changer en créerait.
- **L'anglais et le portugais n'ont que le français** : aucune autre langue ne peut servir d'arbitre, seul l'historique les couvre.
- **Les scènes japonaises et portugaises de Lisbonne** sont en chantier sur leurs propres sessions et n'ont pas été vues.

## Vu en passant, non corrigé (ce ne sont pas des décalages)

- `exercices.json`, `deshalbTrotzdemExercises` et `weilObwohlExercises` : le turc donne deux phrases sans « ___ » (« Yorgunum. Erken yatıyorum. ») là où les autres langues gardent le trou. C'est le choix de la v410 (« choisir par le SENS » : ne pas trahir le connecteur), pas une erreur.
- `exercices.json`, indices et explications en persan, en turc et en ukrainien de `derEinExercises` et `possessivExercises` : ils sont abrégés (« Datif, féminin. » sans l'exemple ; « à lui » / « à elle » absents de l'indice persan). Rien de faux, mais moins d'aide qu'en français.

## Relancer

Les outils sont dans `retours/traductions-decalees/` ; on les lance depuis la racine du dépôt :

```
python retours/traductions-decalees/homonymes.py fr,en,tr,uk,fa,ar,pt,pl,ru themes.json verbe.json adjectif.json adverbe.json redewendung.json funktionswort.json
python retours/traductions-decalees/lots.py sortie.json
python retours/traductions-decalees/rejouer.py themes.json sortie.json      # puis trier.py sortie.json
```

Quand ajouter le contrôle : dès qu'un **lot indexé par le mot** est appliqué, lancer `homonymes.py`, qui prend quelques secondes. C'est le contrôle qui aurait arrêté la phrase de Daria.
