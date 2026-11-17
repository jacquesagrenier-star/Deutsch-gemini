# Rapport : exercices d'articles (articles.es.json)

## Fait

- `interface-es/lots/articles.es.json` : 219 clés sur 219 (44 `E|`, 5 `D|`, 120 `R|`, 50 `M|`).
- Contrôle `textes.py controle` : **0 faute, 2 avis** (`E|def.gen.m`, `E|def.gen.n` : le « des » relevé
  est l'article allemand du Genitiv, pas du français).
- Aucun script écrit ; le JSON a été posé avec l'outil Write.

## Les explications (E|) : ce qui a été réécrit pour un hispanophone

- Nominativ = « el sujeto de la oración » ; Akkusativ = « el complemento directo (el que en español
  reemplazas por «lo» o «la») » ; Dativ = « el complemento indirecto, el «le» del español » ;
  Genitiv = « «de» + el poseedor » (« del hombre », « de un… », « de ningún… »). L'ancrage est donné
  en entier à la première forme de chaque cas, en rappel court ensuite.
- `E|def.nom.n` : ajout « un género que el español no tiene ». `E|def.nom.pl` : ajout « la misma para
  los tres géneros ».
- `E|def.dat.f` : ajout « No lo confundas con el der masculino del Nominativ » (repris de l'idée du russe).
- `E|neg.nom.m` : ajout « kein niega el sustantivo (como «ningún» o «no… un») », l'espagnol n'ayant
  pas d'article négatif.
- Les noms des cas et les formes allemandes restent en allemand, sans guillemets, comme la source.

## Choix de vocabulaire

- Auto → el carro ; Wohnung → el apartamento ; Zeitung → el periódico ; Zimmer → la habitación ;
  Brille → los lentes ; kaputt → descompuesta ; Regal → el estante ; Film → la película.
- Lehrer / Lehrerin → profesor / profesora (aucun contexte d'école primaire) ; Ärztin → la doctora ;
  Arzt → el médico.
- Les sujets « él » / « ella » sont écrits (le verbe seul ne dit pas le genre) ; « yo » et « nosotros »
  sont omis.
- Le « a » personnel et le « le » redoublé sont mis partout au Dativ (« Le ayudo al hombre »), ce qui
  montre justement le complément indirect annoncé dans les explications.

## Doutes

- `R|ARTICLES_AKKUSATIV_DEF|5` « Wir besuchen die Schule » : rendu « Visitamos la escuela » comme le
  français et l'anglais ; en allemand, « die Schule besuchen » veut d'abord dire « aller à l'école »
  (« Vamos a la escuela »).
- `R|ARTICLES_DATIV_DEF|0`, `|7`, `|8`, `M|2`, `M|15`, `M|33`, `M|37`, `M|49` et les formes négatives :
  « Le ayudo a… » (usage du Mexique, et qui montre le Dativ) plutôt que « Lo ayudo » (courant en
  Colombie et dans le Cône Sud). À trancher.
- `R|ARTICLES_AKKUSATIV_DEF|2`, `INDEF|3`, `M|30` : « Me como la / una manzana » (naturel) plutôt que
  « Como la manzana ».
- `R|ARTICLES_AKKUSATIV_NEG|0`, `|4`, `|6`, `M|36`, `M|45` : « No tengo perro / carro », « no busca
  apartamento » sans article, forme naturelle ; « ningún » est gardé ailleurs.
- `R|ARTICLES_GENITIV_NEG|0` à `|3` : « La opinión de ningún profesor cuenta más aquí », calque de la
  structure allemande (elle-même artificielle), correct mais raide.
- `R|ARTICLES_GENITIV_NEG|5` « keiner Blumen » (pluriel) : rendu au singulier, « de ninguna flor ».
- `M|27` « Ich fahre mit einem Auto » : « Voy en un carro » (l'article est gardé pour l'exercice) ;
  `M|40`, `M|46` : « No voy en tren / en carro ».
- `R|ARTICLES_NOMINATIV_NEG|2`, `M|35` « eine Katze » : « un gato » (le mot générique en espagnol).

## Sources fautives ou flottantes

- `M|39` « Ich nehme keinen Zug » : le français dit « Je ne prends pas le train », l'anglais « a train » ;
  suivi l'allemand : « No tomo ningún tren ».
- `R|ARTICLES_AKKUSATIV_NEG|3` : le français « Je n'ai pas le temps » ajoute un article ; « No tengo tiempo ».
- `R|ARTICLES_GENITIV_INDEF|8` « leise » : français « douce », anglais « quiet » ; rendu « suave ».
- `R|ARTICLES_GENITIV_DEF|10` et `INDEF|9` « Zimmer » : français « chambre », anglais « room » ; rendu
  « la habitación ».
- `D|objet` : le français dit « qui subit l'action ? », l'anglais « what receives… » ; rendu
  « ¿quién o qué recibe la acción? ».

## À trancher

- « Le ayudo » / « Lo ayudo » (voir Doutes).
- « los lentes » (Mexique, Colombie « las gafas » aussi courant) pour `R|ARTICLES_AKKUSATIV_NEG|5`.
- « descompuesta » (Mexique) / « dañada » (Colombie) pour la lampe, `R|ARTICLES_NOMINATIV_DEF|5`.
