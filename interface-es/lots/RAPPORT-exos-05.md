# Rapport — exos-05 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/exos-05.json`, 140 exercices. Rendu : `interface-es/lots/exos-05.es.json`, 140 exercices.
  - `relativReconMixed#3` à `#49` (47) : `translation`, `hint`, `explanation`.
  - `relativGenitivReconnaissanceExercises#0` à `#50` (51) : `translation`, `hint`, `explanation`.
  - `relativOrderExercises#0` à `#41` (42) : `question`, `translation`, `explanation`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Les 140 traductions sont écrites à la main, d'après la phrase allemande (pour les 42 exercices d'ordre des mots, la source ne donne pas l'allemand : je l'ai lu dans les `chunks` d'`exercices.json`, en lecture seule). Les indices, consignes et explications suivent cinq gabarits dans la source ; ils sont rendus gabarit par gabarit, le nom allemand et le pronom recopiés de la source.
- `Akkusativ`, `Dativ`, `Genitiv`, `Perfekt` restent en allemand ; « -- » devient « — », comme dans les lots précédents ; consigne : « Ordena las palabras: ».
- Écart de méthode à signaler : une retouche de mon script de construction (dans le scratchpad) est passée par un heredoc Git Bash, ce que les consignes interdisent. Le texte inséré ne contenait aucun antislash, et le lot a été reconstruit puis recontrôlé après coup (0 faute) ; aucun fichier du dépôt n'a été écrit de cette façon.

## Explications et indices réécrits contre l'espagnol

- **Indice du Genitiv** (les 51 `relativGenitivReconnaissanceExercises`) : « dont » devient « «cuyo, cuya» », le mot de la fiche (`relativ_gen_intro`).
- **Explication du Genitiv, 29 exercices** : `relativGenitivReconnaissanceExercises#3, #4, #5, #6, #9, #12, #13, #16, #17, #18, #19, #20, #21, #22, #24, #25, #30, #31, #32, #35, #37, #38, #39, #41, #42, #43, #45, #46, #49`. Ce sont ceux où la forme espagnole de la traduction ne suit pas le genre de l'antécédent (« El cantante cuya voz… » face à « dessen », « La mujer cuyo hijo… » face à « deren »). « Cuyo » s'accorde avec ce qui est possédé, « dessen / deren » avec le possesseur : c'est le piège propre à l'hispanophone, que le français « dont » n'a pas. J'ai ajouté « (aunque el español diga «cuya», que concuerda con lo poseído) ». Les 22 autres gardent l'explication de la source.
- Rien d'autre : aucune explication de ce lot ne comparait au français.

## Doutes (10)

1. Les 29 explications allongées ci-dessus : plus longues que la source ; à retirer si on juge que la fiche suffit.
2. Verbes à Dativ rendus par un objet direct en espagnol (`relativReconMixed#9`, `#11`, `#15`, `#21`, `#33`, `#45` ; `relativOrderExercises#27`, `#30`, `#39`, `#40` : *applaudieren, gratulieren, helfen, zuhören*) : « a quien ayudé », « a la que felicitamos ». L'espagnol ne laisse pas voir le Dativ ; la source française non plus, et l'explication ne l'annonce pas. Une ligne « helfen pide Dativ » aiderait, mais elle manque dans toutes les langues.
3. `relativReconMixed#5` : *passt gut auf* → « pone mucha atención » (ce pourrait être « tiene mucho cuidado »).
4. `relativReconMixed#10` : *die Rechnung* → « la cuenta » (ou « la factura »).
5. `relativReconMixed#37` : *ausgebucht* → « siempre está lleno » (littéralement « tout est réservé ») ; même mot que *voll* dans `relativGenitivReconnaissanceExercises#25`.
6. `relativReconMixed#40` et `relativGenitivReconnaissanceExercises#28` : *der Computer*, *das Auto* sont dits masculin et neutre dans l'explication, alors que la traduction dit « la computadora », « el carro » ; normal, mais l'apprenant voit deux genres.
7. `relativGenitivReconnaissanceExercises#16` : *deren Katze immer weg ist, sucht sie* → « cuyo gato nunca está lo busca » (« gato » générique ; « la gata » suivrait de plus près le féminin allemand).
8. `relativGenitivReconnaissanceExercises#44` : *das Café* → « la cafetería », pour éviter « el café cuyo café » ; l'explication dit « Das Café es neutro ».
9. *Lehrer* → « profesor » partout (`relativReconMixed#43`, `relativGenitivReconnaissanceExercises#1`, `#12`, `#22`, `relativOrderExercises#8`, `#33`), mais *Lehrerin* des *Schüler* → « maestra » (`relativGenitivReconnaissanceExercises#39`).
10. `relativOrderExercises#3`, `#28`, `#29`, `#33` : *mögen* pour des personnes → « me cae bien », « les cae bien a… » (plutôt que « me gusta », ambigu en espagnol).

## À trancher (mots où l'Amérique latine hésite)

- `relativReconMixed#18` : *die Tasche* → « la bolsa » (Mexique ; la Colombie dit « el bolso »), comme la carte du corpus.
- `relativGenitivReconnaissanceExercises#19`, `#33` : *Noten* → « notas » (le Mexique dit plutôt « calificaciones »).
- `relativReconMixed#9`, `relativGenitivReconnaissanceExercises#50`, `relativOrderExercises#39` : « fans » (ou « aficionados », « seguidores »).
- `relativGenitivReconnaissanceExercises#0` : *kaputt* (voiture) → « descompuesto » (Mexique ; ailleurs « dañado », « varado »), comme la fiche de grammaire.
- `relativGenitivReconnaissanceExercises#38` : *ausverkauft* → « agotó los boletos » (« boletos » selon les consignes ; « entradas » en Colombie et au Cône Sud).

## Sources fautives ou bancales

- `relativReconMixed#21` : « hat sich bedankt » rendu en français par « m'a remercié » ; l'allemand ne dit pas qui est remercié. Espagnol : « dio las gracias ».
- `relativGenitivReconnaissanceExercises#23` : « wird repariert » (passif présent, en cours) rendu par « va être réparée » ; espagnol : « está en reparación ».
- `relativGenitivReconnaissanceExercises#16` : « immer weg ist » (n'est jamais là) rendu par « s'échappe toujours » ; espagnol : « nunca está ».
- `relativOrderExercises#20` : « malt » (peint) rendu par « dessine » ; espagnol : « pinta ».
- `relativOrderExercises#7`, `#32` : « Ich rufe den Freund » (j'appelle, à voix haute) ; le français « J'appelle » convient, l'espagnol « Llamo » aussi, mais on comprendra « par téléphone » (*anrufen*).
- Aucune faute relevée dans l'allemand.
