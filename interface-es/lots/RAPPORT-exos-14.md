# Rapport — exos-14 (15 nov. 2026)

## Fait

- `interface-es/lots/exos-14.es.json` : **140 exercices sur 140**, chacun avec `translation`, `hint`, `explanation`.
  Contrôle `exos.py controle` : **0 faute, 0 avis**.
- Jeux : `weilObwohlExercises` #36-51 (16), `deshalbTrotzdemExercises` #0-49 (50),
  `wennObExercises` #0-52 (53), `wennWannExercises` #0-20 (21).
- 7 indices distincts, 82 explications distinctes (6 explications génériques répétées, 76 propres à une phrase).
- Aucun champ `question`, `correct` ni `options` dans cette part.

## Choix de traduction

- `deshalb` → « por eso » ; `trotzdem` → « aun así » (« y sin embargo » là où le français dit « pourtant ») ;
  `obwohl` → « aunque » + indicatif (fait réel).
- `deshalbTrotzdemExercises#0` à `#27` : la traduction française de la source garde le trou (« Il pleut ___ je reste à
  la maison. ») pour ne pas donner la réponse ; je l'ai gardé aussi (« Llueve, ___ me quedo en casa. »), la phrase
  complète étant dans l'explication, comme dans la source.
- `wenn` temporel + futur → « cuando » + subjonctif (« Llámame cuando empiece la película ») ; habitude → indicatif
  (`wennWannExercises#9`, `#19`).
- Vocabulaire d'Amérique : carro, autobús, tienda, día feriado, abrigo, « paso por ti » (abholen), « descompuesto ».

## Explications réécrites contre l'espagnol

- `wennWannExercises#0` et `#1` : ajout de « («cuándo», con tilde) » et « («cuando», sin tilde) ». L'espagnol
  distingue *wann / wenn* par le seul accent écrit ; c'est le seul ajout par rapport à la source. À retirer si jugé de trop.
- `wennObExercises#4`, `#8`, `#12`, `#16` : les mots français cités (« aucune idée », « se demander », « personne ne
  sait », « pas sûr ») sont remplacés par les mots de la traduction espagnole (« ni idea », « preguntarse », « nadie
  sabe », « no estoy seguro »).
- Explication générique de `ob` : « un «si» al que se le podría añadir «o no» » (le français dit « remplacer par » ; l'indice
  dit « ajouter », que j'ai suivi). Aucun « comme en français » dans cette part ; l'espagnol « si » a la même ambiguïté
  que le français, donc rien d'autre à réécrire.

## Doutes

- `wennObExercises#17`, `#27`, `#50` : « Er ist glücklich, wenn… » rendu au présent (« Él está feliz si aprueba »,
  « queda contenta », « se pone muy contento ») ; le français met un futur. Les deux se défendent.
- `wennWannExercises#13` (« Wir treffen uns, wenn er Zeit hat ») : rendu comme un fait à venir (« cuando él tenga
  tiempo ») ; lecture d'habitude possible (« cuando tiene tiempo »).
- `weilObwohlExercises#44`, `#45` : « es soll regnen » → « dicen que va a llover » (le français dit « il doit pleuvoir »).
- `deshalbTrotzdemExercises#24`, `#25`, `wennObExercises#18`, `#19` : « Schmerzen haben » → « tener dolor »
  (un soignant préférerait peut-être « le duele » / « si te duele »).

## Sources fautives

- Aucune faute dans l'allemand. Français un peu bancal, sans conséquence : `wennObExercises#16` (« Je ne suis pas sûr
  s'il réussit l'examen »), `wennObExercises#4` (« Je n'ai aucune idée si… »).

## À trancher

- « descompuesto » (`deshalbTrotzdemExercises#4`) : mexicain et compris partout ; la Colombie dit plutôt « varado » /
  « dañado ».
- « día feriado » (`weilObwohlExercises#46`, `#47`) : la Colombie dit « festivo ».
