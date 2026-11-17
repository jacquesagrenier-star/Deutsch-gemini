# Rapport — exos-10 (espagnol d'Amérique latine)

## Fait

- `interface-es/lots/exos-10.es.json` : **140 exercices sur 140**, chacun avec exactement les champs de `champs`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Répartition : `possessivExercises` #13-69 (57 : `translation`, `hint`, `explanation`),
  `adverbienNuanceExercises` #0-49 (50 : + `question`),
  `konjunktionenNuanceExercises` #0-32 (33 : + `question`, `correct`, `options`).
- Les trois séries sont très répétitives ; les textes identiques dans la source le sont dans la
  traduction (une seule formulation par explication type). Suite de exos-09 pour les possessifs :
  mêmes phrases, mêmes termes (*Nominativo, Acusativo, Dativo, Genitivo* dans l'explication,
  *Nominativ, Akkusativ…* dans l'indice ; *carro, afuera, hijo* pour *das Kind*).

## Explications réécrites contre l'espagnol

**Aucune explication** de ce lot ne compare au français : toutes décrivent l'allemand seul, elles
sont traduites sans règle ajoutée. Ce qui a dû être adapté à l'espagnol, hors explications :

- `possessivExercises#20-39` et `#60-69` (sein, ihr « à elle », ihr « à eux ») — le français dit
  « son … (à lui) » ; l'espagnol *su* est encore plus ambigu : traduction « Su hermano (de él) /
  (de ella) / (de ellos) », indice « «de él» / «de ella» / «de ellos» ».
- `possessivExercises#50-59` (euer) — le français « votre » suffisait ; en espagnol d'Amérique
  *euer* se rend aussi par *su*. La **traduction** porte donc « (de ustedes) » (« Su hermano (de
  ustedes) es simpático. »), absent de la source, faute de quoi dix phrases seraient identiques à
  celles de sein / ihr. L'**indice**, lui, est resté fidèle à la source (pas de « «de ustedes» ») :
  à ajouter si l'indice est la seule chose affichée avant la réponse (voir « À trancher »).
- `konjunktionenNuanceExercises#9` — « denn (car) » → « «denn» (pues) » ; *pues* est le seul
  équivalent espagnol qui se distingue de *porque* (weil), comme *car* de *parce que*.

## Choix de traduction à connaître

- `question` (adverbes, conjonctions) : la phrase allemande est gardée, seule la consigne est
  traduite — « ¿A qué familia pertenece «heute»? », « ¿Qué tipo de conjunción es «und»? »
  (même forme que les `question` de exos-06).
- Les noms de familles d'adverbes, que la source garde en allemand (*Zeit, Ort/Richtung,
  Häufigkeit, Art und Weise, Grad/Menge, Grund/Folge, Verbindung/Logik, Frageadverbien*), restent
  en allemand.
- `options` / `correct` : « Coordinación (orden de las palabras sin cambio) » et « Subordinación
  (verbo al final) », identiques dans les 33 exercices, même ordre que la source.
- « le piège » de *euer* (indices #51, #53-59) → « ojo con la trampa » : c'est un piège de
  l'allemand, il est gardé.
- Perfekt → pretérito (« Casi no dormí. », « Ella lo entendió de repente. », « Al final él aceptó. »).
- Le pronom sujet (*él, ella*) est écrit à la 3e personne, où le verbe espagnol seul ne dit pas qui.
- « proposition » (subordonnée) → « oración » ; « 2e position » → « segunda posición » (comme exos-09).

## Doutes

- `adverbienNuanceExercises#1` — *der Aufzug* → « el ascensor » (Colombie, Amérique du Sud ;
  le Mexique dit plutôt « el elevador », mais comprend « ascensor »).
- `adverbienNuanceExercises#13` — « keineswegs selbstverständlich » → « Eso no es de ningún modo
  obvio. » (*selbstverständlich* : « obvio » plutôt que « algo que se dé por sentado », plus long).
- `adverbienNuanceExercises#44` — « Das reicht völlig. » → « Eso es más que suficiente. »
- `adverbienNuanceExercises#34` — « oft » → « a menudo » (neutre ; « seguido » est plus mexicain).
- `konjunktionenNuanceExercises#4` / `#15` — *wenn ich ankomme* → « Llamo cuando llegue. »
  (futur, subjonctif) mais *wenn sie ankommt* → « Ella llama cuando llega. » (habitude) : l'allemand
  ne tranche pas, les deux lectures sont possibles dans chaque phrase.
- `konjunktionenNuanceExercises#6` / `#22` — *obwohl es regnet* → « aunque está lloviendo »
  (indicatif : le fait est réel), pas « aunque llueva ».
- `konjunktionenNuanceExercises#30` — *da* → « dado que » (« Él se quedó, dado que ya estaba oscuro. »).
- `konjunktionenNuanceExercises#31` — « Ich fahre oder ich laufe. » → « Voy en carro o voy a pie. »
  (*fahren* peut être le vélo ou le bus ; le français dit « Je roule ou je marche »).
- `konjunktionenNuanceExercises#5` / `#20` — *Kommst du mit* → « ¿Vienes con nosotros…? » (comme le
  français « avec nous » en #5 ; l'allemand ne dit pas avec qui).

## Sources fautives ou discutables

- `adverbienNuanceExercises#25` — « Komm bitte her! » : le français (« Viens ici ! ») oublie
  *bitte*. Suivi l'allemand : « ¡Ven acá, por favor! ».
- `konjunktionenNuanceExercises#23` (« Das ist kein Tee, sondern Kaffee. ») et `#26` (« Ich habe
  Hunger und Durst. ») — l'explication type dit « le verbe reste en 2e position », alors que la
  conjonction y relie deux noms, sans second verbe. Traduit tel quel (défaut de la source, dans
  toutes les langues).
- `konjunktionenNuanceExercises#8` / `#25` / `#32` — le français rend *bevor du kommst*, *nachdem er
  gegessen hatte* par un infinitif (« avant de venir », « après avoir mangé ») ; l'espagnol aussi
  (« antes de venir », « Después de comer, él se fue. »), plus naturel, mais la subordonnée
  conjuguée de l'allemand ne s'y voit plus.
- `adverbienNuanceExercises` — le `topic` est écrit « Adverbes · Famille » (#0-15) puis
  « Adverbes · famille » (#16-49) ; sans effet sur ce lot.

## À trancher

- `possessivExercises#50-59` : ajouter « «de ustedes» » à l'indice, comme « «de él» » ailleurs ?
  (La source française ne marque rien, mais « votre » y levait l'ambiguïté.)
- `adverbienNuanceExercises#1` : « ascensor » ou « elevador ».
