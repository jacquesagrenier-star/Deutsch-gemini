# Rapport — exos-09 (espagnol d'Amérique latine)

## Fait

- `interface-es/lots/exos-09.es.json` : **140 exercices sur 140**, chacun avec `translation`, `hint`, `explanation`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Répartition : `wortstellungFrageExercises` #24-50 (27), `wortstellungTekamoloExercises` #0-49 (50),
  `wortstellungNichtExercises` #0-49 (50), `possessivExercises` #0-12 (13).

## Explications réécrites contre l'espagnol

**Aucune.** Aucune explication de ce lot ne compare au français (« comme en français », piège du
français) : toutes décrivent l'allemand seul. Elles sont traduites, sans règle ajoutée.

Choix de termes :
- les indices gardent les termes allemands de la source (*Nominativ, Akkusativ, Dativ, Genitiv*) ;
  les explications, que la source donne en français (« Nominatif masculin »), sont en espagnol
  (*Nominativo, Acusativo, Dativo, Genitivo*) ;
- TeKaMoLo : *temporal, causal, modal, local* ; « tiempo, causa, manera, lugar ».

## Choix de traduction à connaître

- `wortstellungTekamoloExercises#0-29` : comme le français, la phrase espagnole **suit l'ordre
  allemand** des compléments (« Me voy mañana por las vacaciones a Berlín. »), puisque la question
  porte sur cet ordre. L'espagnol en est un peu raide, exprès.
- `ihr` → *ustedes*, `Sie` → *usted* ; le pronom sujet est écrit quand il distingue deux cartes
  voisines (séries `nicht#0-34` : « Él no entiende eso. » / « Ella… » / « Ustedes… » / « Ellos… »).
- Perfekt → pretérito (« ¿Ya comiste? », « ¿Les gustó la película? », « ¿Cuándo llegaron ustedes? »).
- Vocabulaire : *carro, autobús, manejar, afuera, el clima* (pour *das Wetter*).

## Doutes

- `wortstellungNichtExercises#47` — « zu zweit » rendu « de a dos » (« Ellos no vienen solos, sino de
  a dos. ») ; courant en Amérique du Sud, moins au Mexique (« de dos en dos », « en pareja » disent
  autre chose). À relire.
- `wortstellungTekamoloExercises#37` — « aufgehört » sans complément : « Él lo dejó el año pasado por
  los niños. » (le « lo » est une béquille espagnole).
- `wortstellungTekamoloExercises#9` et `#29` — « laufen » rendu « correr », comme le français ; en
  allemand courant ce peut être « aller à pied ».
- `wortstellungTekamoloExercises#35` — « am Freitag » rendu « El viernes » (un vendredi ou chaque
  vendredi, ambigu comme l'allemand ; le français dit « Le vendredi », l'habitude).
- `wortstellungFrageExercises#28` — « Sollen wir schon anfangen? » : « ¿Debemos empezar ya? »
  (« ¿Empezamos ya? » serait plus naturel, moins proche de *sollen*).
- `possessivExercises#2, #8, #12` — « Kind » rendu « hijo » (« Mi hijo juega afuera. ») : avec un
  possessif, « mi niño » sonne moins bien ; le neutre allemand ne se voit plus.
- `wortstellungNichtExercises#42` — « laut / leise » : « en voz alta / en voz baja ».

## Sources fautives

- `wortstellungTekamoloExercises#34` (« Wir fahren heute wegen des Wetters langsam. ») et `#37`
  (« Er hat letztes Jahr wegen der Kinder aufgehört. ») : l'explication commune dit « le complément
  de TEMPS vient avant celui de LIEU », mais ces deux phrases **n'ont pas de complément de lieu**
  (temps avant cause). Traduite telle quelle ; à corriger dans toutes les langues.
- `wortstellungNichtExercises#44` (« Ich trinke nicht Tee, sondern Kaffee. ») : le français « pas de
  thé, mais du café » ; rien de faux, simple remarque (l'espagnol : « No tomo té, sino café. »).
- `wortstellungNichtExercises#14` : « ihn est un pronom défini » — formulation discutable (un pronom
  personnel), traduite telle quelle.
- `wortstellungTekamoloExercises#0-29` : le champ `reponse` (« temporel », « causal », « modal ») est
  en français et ne figure pas dans `champs` : à traduire ailleurs si l'app l'affiche.

## À trancher

- « de a dos » (`nicht#47`), voir plus haut.
- *el clima* contre *el tiempo* pour « das Wetter » (`tekamolo#2, #18, #34`) : *el clima* est l'usage
  courant au Mexique et en Colombie ; *el tiempo* est plus exact.
