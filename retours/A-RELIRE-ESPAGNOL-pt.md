# L'espagnol en portugais du Brésil : ce qu'un Brésilien doit relire en priorité

Dressé le 1er nov. 2026. Le texte portugais de l'espagnol est complet depuis la v784 (13 oct.), et le
1er nov. ont été ajoutés les 61 mots du cours de Jacques, la prononciation des nombres et les sous-titres des
épisodes. Écrit et relu par des modèles, **jamais par un Brésilien**. Historique : `espanol/AVANCEMENT-PT.md`.

## 1. Les 17 fiches de grammaire (le plus important)

`espanol/datos/grammaire.json`, clé `pt` (259 textes) et `textes.pt` (43 libellés). Elles ont été
**réécrites contre le portugais**, pas traduites : c'est là que se joue la valeur pour ce public.
Vérifier que chaque piège annoncé est juste pour un Brésilien :
- `genero` : les noms dont le genre s'inverse (el color, el dolor, el puente, el árbol, el viaje, la nariz…) ;
- `preposiciones` : le « a » devant une personne (« veo a Ana »), absent du portugais ;
- `subjuntivo` et `futuro-condicional` : le futur du subjonctif portugais (« quando eu chegar ») qui n'a
  pas d'équivalent en espagnol moderne (« cuando llegue ») ;
- `pronombres` : la place du pronom (proclise brésilienne vs espagnol) ;
- `pasados` : « pretérito indefinido / perfecto » face au « pretérito perfeito » brésilien — les noms des
  temps se croisent, risque de confusion ;
- le registre : « você » partout, « o senhor » pour usted ; repérer le portugais d'Europe (« tu », « estás
  a fazer », « autocarro », « comboio ») qui n'a rien à faire ici.

## 2. Les exercices, en particulier les faux amis

`espanol/datos/ejercicios.json`, champs `*_pt`.
- `falsosAmigosExercises` (52) : l'indice portugais dit « a palavra parecida com o português costuma ser a
  armadilha » et les explications ont été adaptées (embarazada ≠ embaraçada, carpeta ≠ carpete, exprimir
  ≠ exprimir, rojo ≠ roxo, despedir ≠ despedir-se). Mais plusieurs questions restent des pièges de
  **francophone** (gamba, mantel, subir, montar, sueldo, retirada, tabla) et le portugais a ses propres
  faux amis, bien plus nombreux, absents ici : **exquisito, oficina, polvo, borracha, apellido, rato, cena,
  pelado, sobremesa, largo (comprido), cachorro, salada, latir, rubio/ruivo, presunto, propina, tirar**.
  Décision pour Jacques : une série de faux amis propre au portugais vaudrait plus que la série actuelle.
- À relire en entier : `serEstarExercises`, `porParaExercises`, `gustarExercises` (le mot à mot « o
  chocolate ME AGRADA »), `preposicionesExercises` (le « a » personnel), `subjuntivoImperfectoExercises`,
  `oracionesSiExercises`.
- `question_pt` manque sur 565 exercices (les jeux de pièges, la question est la phrase espagnole à
  trous) : ce n'est pas un manque, l'app affiche la phrase espagnole. Rien à faire.

## 3. Nouveau le 1er nov. : à relire en premier, car jamais relu par personne

- **Les 61 mots du cours de Jacques** (thèmes « Description physique » et « Adjectifs », B1) :
  `espanol/ajouts/cours-jacques-pt-ar.json`, colonnes 2 et 3 (traduction, exemple). Choix à confirmer :
  « cacheado » pour rizado, « castanho » pour castaño (cheveux et yeux), « legal » pour simpático,
  « estatura média ».
- **La prononciation des nombres** (`tests/reperes_suite.py`, `PRONONCIATION_NOMBRES_ES_PT`) : « θÉ-ro »
  (affiché « THÉ-ro » / « SÉ-ro »), « Ó-tcho », « sé-SSÉN-ta », e final en « ê » pour qu'il ne devienne pas
  « i ». ⚠️ Piège non réglé : un Brésilien lit « ti » et « di » comme « tchi » et « dji » (« béin-**ti**-Ú-no »,
  « **dié**-θi-SÉIS ») ; la règle `d` de la prononciation le dit, mais la ligne du nombre ne le marque pas.
  Proposer une graphie si le relecteur en voit une.
- **Les sous-titres portugais des 4 épisodes** (`scenes/traductions-es-pt-ar.json`, clé `pt`) : surtout les
  jeux de mots (« ¿me regala un café? », « ¡qué padre! » / « ¿tu padre? », « ahorita »), rendus en gardant le
  mot espagnol entre guillemets.

## 4. L'interface propre à l'espagnol

`index.html`, `I18N_ESPAGNOL.pt` (142 clés), et les fiches magasin `.claude/fiche-magasin-espagnol-pt.md`.
- Corrigé le 1er nov. : l'abonnement annonçait « 7 700 palavras do A1 ao C1 » et les examens allemands ;
  il dit « 3.700 palavras do A1 ao B2 » et « O sotaque da Espanha ou da América Latina ».

## 5. Connu, pas à relire

- Pas de dictionnaire espagnol-portugais (WikDict n'a pas la paire) : la recherche retombe sur l'anglais.
- La voix de la visite guidée n'existe pas en portugais (payante, pas demandée).
- (Corrigé le 1er nov. : la première colonne des tableaux de grammaire, en français jusque-là, est
  traduite — `espanol/ar/colonne_fiches.py` ; à relire avec les fiches.)
- Corrigé le 1er nov. : « Escrever » et « Montar a frase » montraient la phrase ANGLAISE à traduire ; ils
  montrent maintenant la phrase portugaise.
- Les textes portugais emploient les guillemets « » (usage du Portugal et du français) : au Brésil on
  écrit plutôt “ ”. À uniformiser si le relecteur le demande.
