# Rapport — exos-06 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/exos-06.json`, 140 exercices. Rendu : `interface-es/lots/exos-06.es.json`, 140 exercices.
  - `relativOrderExercises#42` à `#69` (28) : `question`, `translation`, `explanation`.
  - `relativGenitivOrderExercises#0` à `#7` (8) : `question`, `translation`, `explanation`.
  - `relativGenitivOrderExercises#8` à `#53` (46) : `translation`, `hint`, `explanation`.
  - `adjektiveDeklinationExercises#0` à `#49` (50) : `question`, `translation`, `hint`, `explanation`.
  - `praepReconnaissanceExercises#0` à `#7` (8) : `question`, `translation`, `hint`, `explanation`, `options` (et `correct` pour `#3`).
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Les 140 traductions sont écrites à la main d'après la phrase allemande. Pour les 36 exercices d'ordre des mots, la source ne donne pas l'allemand (`reponse` vide) : je l'ai lu dans les `chunks` d'`exercices.json` (lecture seule).
- Les explications et indices qui suivent un gabarit dans la source sont rendus gabarit par gabarit ; les formes allemandes citées dans les explications des adjectifs sont comparées à la source par le script de construction.
- Même formulation que le lot 05 pour ce qui continue le même jeu (« Ordena las palabras: », « …va al final del todo de la relativa. »).
- Vocabulaire : el carro, el celular, el refrigerador, el apartamento, el pastel, tomar (café, leche, agua).

## Explications réécrites contre l'espagnol

- `relativGenitivOrderExercises#8` à `#53`, les 37 exercices où la réponse est « dessen » / « deren » (tous sauf `#28`-`#31`, `#40`, `#41`, `#47`, `#50`, `#53`) :
  - l'**explication** ajoute « (al revés que «cuyo», que concuerda con lo que sigue) » : en espagnol *cuyo* s'accorde avec la chose possédée, en allemand *dessen / deren* avec l'antécédent ; c'est le piège propre à l'hispanophone, que le français (« dont », invariable) n'a pas ;
  - l'**indice** devient « (¿cuál es el género del antecedente en alemán?) » : le genre espagnol de la traduction diffère souvent (*der Film* / la película, *das Haus* / la casa, *die Prüfung* / el examen).
- `relativGenitivOrderExercises#1` : « deren » vient de « die Frau », pas de « Sohn » — avec « al revés que «cuyo», que concuerda con «hijo» ».
- `relativGenitivOrderExercises#48` (réponse « auf deren ») : l'explication de la source ne dit rien de « auf » ; j'ai ajouté « Con «warten auf», la preposición va delante: auf deren Ergebnis. »

Les autres explications (ordre des mots, adjectifs, prépositions) ne comparaient pas au français : traduites telles quelles.

## Doutes (10)

1. `relativGenitivOrderExercises#8`-`#53` : la parenthèse sur « cuyo » répétée 37 fois ; à raccourcir si on la juge lourde.
2. `relativGenitivOrderExercises#12`, `#15`, `#35` : « a cuyo curso asisto », « a cuyo jefe conozco », « a cuyo hermano conozco » — corrects, mais soutenus ; `#47` « cuyo remitente no conozco » sans « a » (l'expéditeur est inconnu).
3. `relativGenitivOrderExercises#19` : « Los libros cuyas páginas faltan » garde *cuyo* pour rester dans la leçon ; l'usage courant dirait « a los que les faltan páginas ».
4. `adjektiveDeklinationExercises#6`-`#9`, `#25`-`#28` : *die kleine Frau* → « la mujer pequeña » (ou « bajita ») ; `#2`, `#21`-`#23` : *ein großer Mann* → « un hombre alto » (le français dit « grand homme »).
5. `adjektiveDeklinationExercises#31`-`#34` : *meine kleinen Kinder* → « mis hijos pequeños » (avec le possessif) ; ailleurs *Kinder* → « niños ».
6. `adjektiveDeklinationExercises#31`, indice : « como un artículo indefinido en plural » traduit tel quel, alors que *ein* n'a pas de pluriel (défaut de la source, toutes langues).
7. `adjektiveDeklinationExercises#36` : *nicht lecker* → « no es rico ».
8. `praepReconnaissanceExercises#0`, `#2`, `#3`, `#4` : deux sens donnés là où le français n'en donne qu'un (« para, por », « a causa de, por », « sobre, encima de », « a través de, por »), parce que *für / wegen / durch* se rendent souvent par « por ».
9. `relativOrderExercises#48` : *die Katze* → « el gato » (générique) ; `#61`, `relativGenitivOrderExercises#12`, `#33` : *Lehrer / Professor* → « profesor ».
10. `relativGenitivOrderExercises#43` (*der Ort*) et `#49` (*das Dorf*) : tous deux « el pueblo ».

## À trancher (mots où l'Amérique latine hésite)

- `adjektiveDeklinationExercises#9`, `#28` : *die Tasche* → « la bolsa » (Mexique ; la Colombie dit « el bolso », le Cône Sud « la cartera »).
- `relativOrderExercises#62`, `relativGenitivOrderExercises#51`, `adjektiveDeklinationExercises#41` : *Torte / Kuchen* → « pastel » (Mexique ; Colombie « torta », « ponqué »).
- `relativGenitivOrderExercises#8`, `relativGenitivOrderExercises#0` : *kaputt* (voiture) → « descompuesto » (Mexique ; Colombie « dañado », « varado »).
- `relativGenitivOrderExercises#25` : *eng* → « angosta » (ou « estrecha »).
- `relativOrderExercises#67` : *der Aufsatz* → « la redacción » (ou « el ensayo »).

## Sources fautives ou bancales

- `relativOrderExercises#69` : l'allemand dit « Wir loben den Spieler » (nous louons), le français « Nous félicitons ». Suivi l'allemand : « Elogiamos al jugador… ».
- `relativOrderExercises#62` : *die Torte … gebacken hat*, français « le gâteau … a préparé » ; espagnol « el pastel que mi abuela horneó ».
- `relativGenitivOrderExercises#4`, `#5` : « Er ist der Autor », « Sie ist die Sängerin », français « C'est… » ; espagnol « Él es… », « Ella es… ».
- `relativGenitivOrderExercises#49` : *wird kleiner*, français « se dépeuple » ; espagnol « se hace más pequeño ».
- `relativGenitivOrderExercises#19` : français « auxquels il manque des pages » pour *deren Seiten fehlen* (voir doute 3).
- `relativGenitivOrderExercises#48` : réponse « auf deren », mais l'indice et l'explication de la source ne parlent que du genre ; la préposition n'est annoncée nulle part (complété en espagnol, à compléter dans les autres langues).
- `relativGenitivOrderExercises#8`-`#53` : le `topic` de ces 46 exercices à trous est rangé dans un jeu nommé « …OrderExercises » ; sans effet sur la traduction, signalé pour mémoire.
