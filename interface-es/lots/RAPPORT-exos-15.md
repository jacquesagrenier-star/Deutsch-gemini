# Rapport — exos-15 (espagnol d'Amérique latine)

## Fait

- `interface-es/lots/exos-15.es.json` : **140 exercices sur 140**, chacun avec exactement ses `champs`
  (`translation`, `hint`, `explanation` ; les sept `blocsConnecteursExercises` : `question`, `explanation`).
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Répartition : `wennWannExercises` #21-52 (32), `aberSondernExercises` #0-49 (50),
  `premierePlaceExercises` #0-50 (51), `blocsConnecteursExercises` #0-6 (7).
- Script de fabrication (scratchpad) : `exos-15_gen.py` ; les explications et indices répétés dans la
  source sont une seule et même chaîne en espagnol.

## Explications réécrites contre l'espagnol

Aucune explication de ce lot ne dit « comme en français » : toutes sont **traduites, sans règle
ajoutée**. Trois points où l'espagnol change la donne, sans que j'aie touché au texte :

- **aber / sondern** (`aberSondernExercises#0-49`) : l'espagnol a la même paire, **pero / sino**
  (le français n'a que « mais »). Les traductions disent donc *sino* là où l'allemand dit *sondern*
  et *pero* là où il dit *aber* — la traduction donne la réponse à qui la lit. Je n'ai **pas** écrit
  « sondern = sino » dans les explications (absent de la source) ; à décider si on veut l'ajouter,
  ce serait l'aide la plus forte de tout le jeu. Devant un verbe conjugué : *sino que*
  (`#24`, `#39`, `#48`).
- **wenn / wann** (`wennWannExercises#21-52`) : l'espagnol distingue par l'accent, **cuándo** (wann)
  et **cuando** (wenn). Les traductions le montrent (`#34` « Dime, por favor, cuándo terminas. » /
  `#35` « Llámame cuando termines. ») ; l'explication reste celle de la source (« cada vez que »,
  « si »). Même question : ajouter « wann = cuándo, con tilde » ? Non fait.
- **Première place** (`premierePlaceExercises`, `blocsConnecteursExercises`) : « inversion » →
  *inversión*, « comme d'habitude » → *como de costumbre*. L'espagnol omet le pronom sujet, donc
  les traductions ne montrent pas l'ordre sujet-verbe ; rien à réécrire, mais « sujeto y luego
  verbo, como de costumbre » parle de l'allemand, pas de l'espagnol.

Termes : *subordinada, principal, el primer lugar, el lugar 1 / 2, la coma, verbo con partícula,
verbo pronominal, conjunción subordinante* (« subordonnant »), *oración* (« phrase »).

## Choix de traduction à connaître

- `wenn` + futur → *cuando* + subjonctif (« Cuando llegues a casa, comemos. ») ; `wenn` d'habitude →
  indicatif (« Cuando llueve, llevo un paraguas. ») ; `wennWann#48` et `premierePlace#5`, `#25` → *si*.
- `ihr` → *ustedes* : `premierePlaceExercises#13` (« wartet » → « esperen aquí, por favor »).
- Perfekt et Präteritum → pretérito (« No dormí, sino que trabajé. ») ; imperfecto pour un état
  (« Aunque estaba cansado… », « La película no era divertida… ») ; `premierePlace#44`
  « no lo he vuelto a ver » (touche le présent).
- Vocabulaire : *carro, autobús, el cuarto* (Zimmer), *tomar café*, *Hamburgo, Milán, Berlín*.
- `blocsConnecteursExercises` : le champ `question` est la phrase à construire, rendue en espagnol ;
  `_question` garde le français (clé de contrôle).

## Doutes

- `aberSondernExercises#13` « erst am Abend » → « pero no antes de la noche » (« hasta la noche »,
  mexicain, se comprend à l'envers ailleurs).
- `aberSondernExercises#19` « ich hätte Lust dazu » → « pero yo tendría ganas ».
- `aberSondernExercises#28` « hungrig » → « hambriento » (pour garder l'adjectif qui remplace
  « cansado » ; « tiene hambre » serait plus courant).
- `aberSondernExercises#35` « pero sí muy luminoso » : le *sí* est idiomatique, absent de l'allemand.
- `aberSondernExercises#46` « günstig » → « barata ».
- `wennWannExercises#23` « Lee enseguida cuando ha comprado un libro nuevo. » : calque voulu de la
  phrase allemande, un peu raide.
- `wennWannExercises#27` « Wir sind traurig » → « Nos ponemos tristes ».
- `premierePlaceExercises#2` et `#22` « bis der Zug kommt » → « hasta que llegue el tren » (le
  français dit « en attendant que »).
- `premierePlaceExercises#29` « Als ich klein war » → masculin (« pequeño »), comme le français.
- `premierePlaceExercises#41` « gingen wir wieder » → « nos fuimos de nuevo ».
- `premierePlaceExercises#45` « ausfiel » → « Como cancelaron el autobús ».
- `premierePlaceExercises#50` « verstand » → imperfecto « entendía ».

## Sources fautives ou discutables

- `premierePlaceExercises#31` (« ruf mich ») et `#49` (« nimm ») : l'explication commune dit « le
  verbe de la principale vient juste après, et le sujet ensuite », or ce sont des impératifs sans
  sujet. Traduite telle quelle ; `#13` a, lui, sa propre explication (« même à l'impératif »).
- `aberSondernExercises#27` : « Même début que la phrase précédente du même couple » suppose que
  l'exercice `#26` vient d'être vu ; dans un tirage mélangé, la phrase tombe à vide. Traduite telle quelle.
- `aberSondernExercises#17` : « Compare avec la phrase où « difficile » remplaçait vraiment » — même
  remarque (renvoi à `#16`).
- `premierePlaceExercises#22` : « Même phrase que plus haut, retournée » — même remarque (renvoi à `#2`).
- `wennWannExercises#28-52` : l'explication de « wann » dit « même dans une question indirecte » aussi
  sous les questions directes (`#28`, `#32`, `#36`…) : générique, pas faux.
- `premierePlaceExercises#4`, `#27`, `#47` : le français dit « Bien qu'il fût… » ; l'allemand est un
  simple Präteritum, rendu « Aunque estaba / era… ».

## À trancher

- Ajouter ou non « = sino » / « = pero » et « = cuándo (con tilde) » / « = cuando » dans les
  explications d'`aberSondern` et de `wennWann` (voir plus haut).
- `aberSondernExercises#41` « Krankenschwester » → « enfermera » ; `#14` « Krankenpfleger » →
  « enfermero » : rien à signaler, mais un soignant peut vouloir relire la paire médico / médica (`#41`, `#42`).
