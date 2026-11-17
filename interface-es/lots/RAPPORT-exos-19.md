# Rapport — exos-19 (15 nov. 2026)

## Fait

- `interface-es/lots/exos-19.es.json` : **140 exercices sur 140**, contrôle `exos.py controle` → **0 faute, 0 avis**.
  - `konjunktiv1Exercises#1` à `#50` (50) : translation, explanation.
  - `werdenExercises#0` à `#50` (51) : translation, explanation.
  - `partizipExercises#0` à `#38` (39) : translation, explanation.
- 140 traductions écrites une à une depuis la phrase allemande (relues alignées sur l'allemand, la bonne
  réponse dans le trou). Les explications sont **15 textes distincts** répétés : traduits une fois et posés
  par `exos-19_construire.py` (scratchpad), qui s'arrête si une explication source ne correspond à
  exactement un gabarit.

## Explications réécrites contre l'espagnol

Aucune explication de cette part ne dit « comme en français » ; rien n'a été ajouté. Seules les gloses
françaises ont changé :

- `werdenExercises#18, #19, #20, #21, #28, #37, #38, #45` (« werden seul = devenir ») et
  `#22` à `#27, #29, #39, #40, #41, #47, #48, #50` (« geworden quand werden veut dire devenir ») :
  l'espagnol n'a pas un verbe unique pour « devenir » → **« volverse, llegar a ser »**.
- `werdenExercises#12` à `#17, #34, #35, #36, #46` (supposition) : « = il doit être malade » →
  « = debe de estar enfermo ».
- `partizipExercises` Partizip I : « l'enfant qui dort » → « el niño que duerme » ; Partizip II : « la porte
  (qu'on a) fermée » → « la puerta cerrada (que alguien cerró) » ; attribut étendu : « le pont que la ville
  a prévu » → « el puente que la ciudad planeó ».

## Doutes

- **Supposition avec werden** : l'espagnol a exactement le même tour (futur de conjecture : « estará
  enfermo », « habrá perdido el tren »). Je ne l'ai pas dit dans l'explication (absent de la source), mais
  ce serait une vraie aide pour un hispanophone — à décider. Les traductions alternent « debe de… »
  (`#12, #14, #15, #17, #46`) et le futur de conjecture (`#13, #16, #34, #36`).
- **« Laut … » + Konjunktiv I** (`konjunktiv1Exercises#4, #11, #30, #46`) : le français met le conditionnel
  de presse (« aurait été blessé ») ; j'ai mis l'indicatif (« Según la policía, nadie resultó herido »),
  « según » portant déjà la distance. Le conditionnel de rumeur (« habría resultado ») existe dans la
  presse d'Amérique latine mais est déconseillé par la norme.
- `konjunktiv1Exercises#19` *Laut Wetterbericht solle es morgen schneien* : « mañana debería nevar ».
- `konjunktiv1Exercises#20` *sie baue keine Stellen ab* : « no estaba eliminando puestos de trabajo ».
- `konjunktiv1Exercises#29, #49` *die Lehrerin* : « la profesora » (niveau non précisé) ; `#49` *der Test* :
  « la prueba ».
- `konjunktiv1Exercises#32` *du müssest dich nicht sorgen* : « no tenías que preocuparte » (pas
  d'obligation), le français dit « ne devais pas ».
- `werdenExercises#19` *will Pilot werden* : « quiere ser piloto » (naturel), alors que l'explication dit
  « volverse, llegar a ser ». De même `#28` « cumple treinta años », `#48` « creció rápido », `#50` « se
  cansó mucho », `#24` « empeoró » : l'espagnol n'y montre pas de verbe « devenir ».
- `werdenExercises#23, #25, #40, #47` (passif en *worden*) : « Lo operaron ayer » mais « fue pagada / fue
  enviada / fue remodelado » ; l'Amérique latine dirait aussi « ya se pagó ».
- `werdenExercises#35` *Das wird schon stimmen* : « Seguro que está bien ».
- `partizipExercises#0` : « al niño dormido » dans la traduction, « el niño que duerme » dans l'explication.
- `partizipExercises#22, #34, #38` : *spannend* → « apasionante » (question) et « emocionante » (histoire) ;
  *begeisternd* → « fascinante ».
- `partizipExercises#35` *zum Amt* : « la oficina pública » ; *ausgefüllte Unterlagen* : « documentos ya
  llenados ».

## Sources fautives ou écartées de l'allemand

- `partizipExercises#26` *ein offenes Fenster* : « offen » est un adjectif, pas un participe ; l'explication
  (« Le participe se décline comme un adjectif ») ne s'applique pas vraiment. Traduit tel quel.
- `partizipExercises#12` *der bis Montag zu schreibende Bericht* : c'est le tour « zu + Partizip I »
  (obligation), que l'explication « Attribut étendu » ne nomme pas. Traduit tel quel.
- `partizipExercises#11` : le français dit « la veille », l'allemand *gestern* → « ayer ».
- `partizipExercises#15` : le français dit « La hausse des prix », l'allemand *die steigenden Preise* →
  « Los precios en aumento ».
- `werdenExercises#6` : le français ajoute « j'en suis sûr » pour *schon* → « Seguro que… ».
- `konjunktiv1Exercises#19` : *solle* après « Laut Wetterbericht » reçoit l'explication des modaux ; c'est
  plutôt *sollen* de ouï-dire. `#29` *sollten* et `#24` *müssten* : classés « Konjunktiv II de remplacement »,
  juste.
- `konjunktiv1Exercises#3` : le français dit « Il pense », l'anglais « He says » ; *meint* → « Él dice ».

## À trancher

- *der Kuchen* → « el pastel » (Mexique ; Colombie : « la torta », « el ponqué ») : `werdenExercises#45`,
  `partizipExercises#21`.
- *das Wetter* → « el clima » (`werdenExercises#24`), courant en Amérique latine ; « el tiempo » est plus
  normatif.
- *renoviert* → « remodelado » (`werdenExercises#47`) ; « renovado / reformado » possibles.
- *ein gekochtes Ei* → « un huevo cocido » (`partizipExercises#3`) ; « huevo duro / tibio » selon le pays.
- *im Stau stehen* → « atrapado en el tráfico » (`werdenExercises#34`) ; « trancón » (Colombie),
  « embotellamiento » (Mexique).
