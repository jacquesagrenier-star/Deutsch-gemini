# Rapport — exos-13 (espagnol d'Amérique latine)

## Fait

- `interface-es/lots/exos-13.es.json` : **140 exercices sur 140**, chacun avec exactement ses `champs`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Répartition : `positionsverbenExercises` #0-53 (54 ; translation, hint, explanation),
  `partikelnNuanceExercises` #0-49 (50 ; question, translation, hint, explanation, correct, options),
  `weilObwohlExercises` #0-35 (36 ; translation, hint, explanation).
- Fait en une passe par jeu, relue ; le fichier est produit par un script du scratchpad
  (`exos-13_construire.py`) qui recopie `_question` depuis la source.

## Explications réécrites contre l'espagnol

Aucune explication de ce lot ne dit « comme en français » : tout est traduit, sans règle ajoutée.
Ce qui a dû changer parce que la source s'appuie sur le français :

- `weilObwohlExercises` #0-11 et #14-27 : la phrase modèle en fin d'explication (« → … bien qu'il
  pleuve ») devient la phrase espagnole complète, avec **aunque + indicatif** (faits réels :
  « aunque llueve », « aunque tiene carro »), *porque*, et *Como* en tête de phrase (#2).
- `partikelnNuanceExercises` : les indices « pas « peut-être » » (#11, #49) et « pas « mais » »
  (#6, #34-36) deviennent « no «quizás» » et « no «pero» » ; #6 « pas une opposition (« mais ») » →
  « no una oposición («pero») » ; #11 « comme « quel/quelle... ! » » → « como «¡qué…!» ».

## Choix de traduction à connaître

- `weilObwohlExercises` : quand la traduction française garde le trou « ___ » (28 exercices), la
  traduction espagnole le garde aussi ; les huit autres (#12, #13, #28-35) sont complètes, comme la source.
- Verbes de position : *stehen / liegen* → « está » la plupart du temps (l'espagnol ne distingue
  pas), « está de pie » (#37), « está echado » (#33, le chien), « está acostado » (#35, #42),
  « está colgado/a » ; *stellen / legen* → « poner ». « wohin? » et « wo? » restent allemands dans
  l'indice ; « verbe faible / fort » → *verbo débil / fuerte* (comme les lots précédents).
- Options des particules (13, même ordre) : « Rassurance » → *Dar tranquilidad*, « Permission
  rassurante » → *Permiso tranquilizador*, « désinvolture » → *desenfado*, « Résignation (« c'est
  comme ça ») » → *Resignación («así es»)*.
- Consigne des particules : « <phrase allemande> ¿Qué matiz aporta «doch» aquí? ».
- *Sie* → usted (`positionsverben#46` « Siéntese… »). Perfekt → pretérito (#29 « Puse la bolsa… »,
  `weilObwohl#31` « Él aprobó aunque estudió poco. »).
- Vocabulaire : *carro, autobús, refrigerador, el suelo, la bolsa* (Tasche), *el estante* (Regal),
  *el armario* (Schrank), *vamos tarde* (spät dran sein).
- Masculin par défaut pour « ich » sans indice de genre (« Estoy sentado », « estoy cansado »,
  « estoy enfermo », « estoy lleno »), comme le français de la source.

## Doutes

- `partikelnNuance#6`, `#34`, `#35`, `#36` (*aber* de surprise) : rendu par « ¡Vaya, …! ». L'espagnol
  a exactement le même emploi avec *pero* (« ¡Pero qué bonito! »), ce qui pourrait servir d'appui ;
  je ne l'ai pas ajouté (absent de la source, et l'indice dit « no «pero» »). À décider.
- `partikelnNuance#2`, `#18`, `#19`, `#20` (*denn*) : rendu par « ¿Y …? » (« ¿Y dónde estabas? »),
  le plus proche du ton ; `#1`, `#16` (*mal*) : « un momentito » ; `#15`, `#17` : « A ver, … ».
- `partikelnNuance#11` « ¡Qué desorden, de verdad! » et `#49` « ¡Qué suertudo eres! » (*suertudo* :
  familier, compris partout).
- `partikelnNuance#7` « Was machst du eigentlich? » : « ¿qué haces? » (comme le français) ; pourrait
  aussi vouloir dire « ¿a qué te dedicas? ».
- `weilObwohl#3` « gehe ich noch aus » : « todavía voy a salir » (le « noch » allemand est gardé ; la
  traduction française à trou l'omet).
- `positionsverben#21` « Die Katze » → « El gato » (générique) ; `#15`, `#16` *Schrank* de cuisine →
  « el armario » (plutôt que *la alacena*).
- `positionsverben#22`, `#23` « über den / dem Stuhl » → « en el respaldo de la silla », comme le français.

## À trancher

- *kaputt* pour une voiture (`weilObwohl#4`, `#32`) : « descompuesto » (Mexique) ; la Colombie dit
  plutôt « dañado » / « varado ».
- *Tasche* (`positionsverben#29`, `#30`) : « la bolsa » (Mexique) contre « el bolso » (Colombie).
- *stehen* (`positionsverben#37`) : « de pie » (neutre) contre « parado » (courant en Amérique).

## Sources fautives

- Aucune faute dans l'allemand.
- `positionsverben#34`, `#35` : le français (« Je couche le bébé. », « Le bébé est couché. ») omet
  « ins Bett / im Bett » ; l'espagnol le rend (« en la cama »).
- `weilObwohl#3` : le français à trou (« je sors ») omet « noch » (voir Doutes).
- `partikelnNuance#49` : l'option correcte est « Exaspération, emphase forte » pour « Du bist
  vielleicht ein Glückspilz! », que l'explication dit « admirative ou exaspérée selon le ton » —
  l'étiquette ne colle qu'à moitié (traduit tel quel).
