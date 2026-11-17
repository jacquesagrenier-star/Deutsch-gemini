# Rapport — exos-18 (15 nov. 2026)

## Fait

- `interface-es/lots/exos-18.es.json` : **140 exercices sur 140**, contrôle `exos.py controle` → **0 faute, 0 avis**.
  - `verbenMitPraepExercises#13` à `#49` (37) : translation, hint, explanation.
  - `passivExercises#0` à `#51` (52) : translation, explanation.
  - `konjunktiv2VergangenheitExercises#0` à `#49` (50) : translation, explanation.
  - `konjunktiv1Exercises#0` (1) : translation, explanation.
- 140 traductions écrites une à une depuis la phrase allemande ; l'indice (1 texte, 37 fois) et les
  explications (37 « verbe + préposition » sur un même gabarit, puis 15 textes distincts répétés) sont
  traduits une fois et posés par le script `exos-18_construire.py` (scratchpad), qui s'arrête si une
  explication source ne correspond à aucun gabarit.

## Explications réécrites contre l'espagnol

Aucune explication de cette part ne compare au français ; rien n'a été ajouté. Seules les **gloses
françaises** sont devenues espagnoles :

- `passivExercises#27, #28, #29, #31, #32` (passif d'état) : « c'est fermé / on ferme » → « está cerrado /
  se cierra ». Le couple estar / se-pasiva rend la différence de lui-même ; je n'ai pas ajouté de phrase
  « comme estar en espagnol » (absente de la source) — à ajouter si l'on veut, c'est une aide réelle.
- `passivExercises#38` à `#45` (remplacements du passif) : « on peut / on doit » → « se puede / se debe ».
- `konjunktiv2VergangenheitExercises` : « = je t'aurais appelé » → « = te habría llamado » ; « = je serais
  venu » → « = habría venido » ; « = tu aurais dû venir plus tôt » → « = deberías haber venido antes ».

## Doutes

- `konjunktiv2VergangenheitExercises#1, #6, #7, #15, #19, #24…` (explication « sein → wäre ») : la glose
  française « je serais venu » montrait l'auxiliaire être ; l'espagnol n'a que *haber* (« habría venido »),
  donc la glose n'illustre plus le choix sein / haben. Laissé tel quel (rien à ajouter d'après la consigne) ;
  une phrase du genre « el español solo usa haber » serait utile, à décider.
- Explication « La condition… La consecuencia va en el mismo tiempo » (`#3, #10, #11, #17, #22, #27, #30,
  #36, #40, #47, #48`) : vrai en allemand (deux Konjunktiv II), alors que l'espagnol met *hubiera* puis
  *habría*. Traduit fidèlement, sans avertissement.
- « fast / beinahe + Konjunktiv II » (`#5, #6, #15, #18, #28, #32, #42`) : rendu par « casi » + pretérito
  (« Casi perdimos el tren », « Casi me caí ») ; l'Amérique latine dit aussi le présent (« casi me caigo »).
- `passivExercises#51` *Die Brücke soll nächstes Jahr gebaut werden* : « debe construirse » (comme le
  français « doit être construit ») ; le sens est plutôt « está previsto que se construya ».
- `verbenMitPraepExercises#32` *sich beschäftigen mit moderner Kunst* : « Ella se ocupa del arte moderno »
  (le français dit « s'intéresse de près à »).
- `verbenMitPraepExercises#28` *erzählt von ihrer Reise* : « Ella cuenta sobre su viaje ».
- `konjunktiv2VergangenheitExercises#31` et `#37` *Sie hätten…* : lu « ils » comme le français
  (« podrían », « deberían ») ; la forme espagnole vaut aussi pour *ustedes*, donc sans risque.
- Phrases en « ich » sans genre marqué : masculin, comme le français (contento, dormido, solo).

## Sources fautives ou bancales

- `konjunktiv2VergangenheitExercises#27` et `#30` : la conséquence est au Konjunktiv II **présent**
  (« wären wir jetzt schon da », « hätten wir jetzt ein Zimmer ») alors que l'explication dit « La
  conséquence suit au même temps ». L'explication ne colle pas à ces deux phrases (dans les 3 langues).
- `konjunktiv2VergangenheitExercises#29` *Das wäre nicht ___ gewesen* (réponse « nötig ») : le trou est un
  adjectif, l'explication parle du choix de wäre — hors sujet pour ce trou.
- `verbenMitPraepExercises#42` : la réponse est « zum » alors que l'explication cite « gratulieren zu » ;
  cohérent mais l'apprenant doit deviner la contraction.
- `passivExercises#3` : français « est opéré tout de suite » ; rien de fautif, mais passif présent à sens
  futur possible. Sans conséquence.

## Doublons acceptés

Sans objet (pas de cartes).

## À trancher

- `passivExercises#6` *das Rathaus* → « el ayuntamiento » (Mexique) ; la Colombie dit « la alcaldía ».
- `verbenMitPraepExercises#39` *sich bewerben um* → « Me postulo para el puesto » (Amérique latine) ;
  autre choix : « Solicito el puesto ».
- `passivExercises#26` *renoviert* → « remodelado » (Mexique, Colombie) plutôt que « renovado / reformado ».
- `passivExercises#34` *Glatteis* → « el hielo en la carretera » (pas de mot unique en Amérique latine).
- `passivExercises#22` *geparkt* → « estacionarse » (Mexique) ; la Colombie dit « parquear ».
- `konjunktiv2VergangenheitExercises#36, #48` *sich beeilen* → « apurarse » (américain ; « darse prisa » en
  Espagne).
