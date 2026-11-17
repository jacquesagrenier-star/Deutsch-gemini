# Rapport — exos-16 (15 nov. 2026)

## Fait

- `interface-es/lots/exos-16.es.json` : **140 exercices sur 140**. Contrôle `exos.py controle` : **0 faute, 0 avis**.
- Jeux : `blocsConnecteursExercises` #7-119 (113 : `question` + `explanation`, et `hint` pour ceux au Perfekt ou au Futur),
  `transformationConnecteursExercises` #0-26 (27 : `translation`, `hint`, `explanation`).
- 8 indices distincts, 82 explications distinctes. Les explications sont faites d'une cinquantaine de phrases types, traduites une
  seule fois chacune et recomposées par script (`exos-16_build.py`, dans le scratchpad) : une même phrase française
  donne partout la même phrase espagnole. Les exemples allemands après « → » sont recopiés tels quels.
- Aucun champ `correct` ni `options` dans cette part.

## Choix de traduction

- `blocsConnecteursExercises` : `_question` est la phrase **française** à construire en allemand ; elle est recopiée
  telle quelle (clé de contrôle) et le champ `question` porte la phrase espagnole, traduite depuis la réponse allemande.
- Un connecteur allemand = un mot espagnol, pour que l'apprenant devine lequel construire : `weil` → « porque »
  (même en tête : « Porque comí demasiado… », #24, #33, #16), `da` → « como » / « ya que », `denn` → « pues »,
  `deshalb / deswegen / darum` → « por eso », `also` → « así que », `trotzdem` → « aun así », `dennoch` → « sin
  embargo », `obwohl` → « aunque » + indicatif, `falls` → « en caso de que », `sodass` → « de modo que »,
  `sobald` → « en cuanto », `solange` → « mientras » + subjonctif, `danach` → « después », `dann` → « luego ».
- « él / ella » gardés quand l'allemand dit `er / sie` (le genre ne se lit pas sur le verbe espagnol).
- Perfekt → pretérito (« fuimos », « llovió ») ; « no nos hemos visto » (#10) garde le perfecto, le sens touche le présent.
- Termes de temps : la source dit « parfait, prétérit, plus-que-parfait, futur » en français ; j'ai mis les noms
  allemands (*Perfekt, Präteritum, Plusquamperfekt, Futur*), comme le font déjà les indices et les phrases types de
  la source (« au Perfekt », « Au Futur »).
- Vocabulaire d'Amérique : carro, autobús, apartamento, « descompuesto » (kaputt), « apurarnos » (sich beeilen),
  « tocar el timbre », « adentro / afuera ».

## Explications réécrites contre l'espagnol

- Aucune explication de cette part ne compare au français : rien à réécrire sur le fond. Seule la ponctuation
  change : le tiret français « — sujet, puis verbe » devient une parenthèse ou « con sujeto y luego verbo », pour
  éviter deux deux-points dans la même phrase (phrases types « L'autre ordre… », « aber / denn / sondern… »,
  « und / oder… », « deshalb n'en est pas une — c'est un adverbe »).

## Doutes

- `blocsConnecteursExercises#16`, `#24`, `#33` : « Porque… » en tête de phrase est moins naturel que « Como… » en
  espagnol ; gardé pour ne pas confondre `weil` avec `da` (#60, #61 : « Como… »).
- `blocsConnecteursExercises#48` (« deshalb komme ich später ») : « por eso vengo más tarde » ; « voy » ou « llego »
  se défendent.
- `blocsConnecteursExercises#66`, `#69`, `#71`, `#72`, `#53`, `#54` : `falls`, `solange`, `sobald`, `wenn`, `bis` +
  présent allemand rendus au subjonctif (« en caso de que llueva », « mientras viva aquí », « en cuanto esté en
  casa », « cuando esté en casa », « hasta que llegue »). La lecture d'habitude (« mientras vivo aquí ») est possible.
- `blocsConnecteursExercises#88`, `#89` : « sino que vengo mañana », « sino que está enferma » — l'allemand répète le
  verbe (« sondern ich komme morgen »), le français non (« mais demain ») ; j'ai suivi l'allemand.
- `blocsConnecteursExercises#117` (« sind wir gewandert ») : « hicimos senderismo » ; « salimos a caminar » est plus
  courant mais moins précis.
- `transformationConnecteursExercises#3` (« Ich kann nicht kommen ») : « No puedo ir ».
- `transformationConnecteursExercises#15` (« hat es gut geschmeckt ») : « estaba rica ».

## Sources fautives ou à regarder

- `blocsConnecteursExercises#42` : fr « il est libre demain » pour « er hat morgen frei » (il a congé) ; rendu
  « mañana tiene el día libre ».
- `blocsConnecteursExercises#76` : fr « qu'elle venait plus tard » pour « dass sie später kommt » (présent) ; rendu
  « Ella dijo que viene más tarde ».
- `blocsConnecteursExercises#111` : fr « Quand le film s'est terminé » pour « Als der Film zu Ende war » — sans
  conséquence, mais l'explication type parle du Perfekt de la principale seulement, ce qui est juste.
- `blocsConnecteursExercises#51`, `#52` : l'explication type ne nomme que « aber » et « sondern » ; à partir de #83
  la même phrase nomme aussi « denn ». Traduit tel quel dans les deux cas.
- `blocsConnecteursExercises#109` (« Bevor du gehst, mach bitte das Licht aus. ») :
  l'explication type dit « le sujet vient après lui », alors que #109 est un impératif
  sans sujet. Traduit tel quel.

## À trancher

- « carro » (Mexique, Colombie) partout pour `Auto` ; « tomar agua » pour `Wasser trinken` (#19 des transformations).
- « pues » pour `denn` : un peu écrit, mais c'est le seul mot qui le distingue de « porque » (`weil`) dans les
  transformations `weil ↔ denn`, où les deux phrases doivent se lire différemment.
