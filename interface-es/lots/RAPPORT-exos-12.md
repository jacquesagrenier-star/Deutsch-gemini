# Rapport — exos-12 (espagnol d'Amérique latine)

## Fait

- `interface-es/lots/exos-12.es.json` : **140 exercices sur 140**, chacun avec exactement ses `champs`
  (`translation`, `hint`, `explanation` ; `derEinExercises#21` et `#22` n'ont pas d'indice).
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Répartition : `obwohlTrotzdemExercises` #18-54 (37), `derEinExercises` #0-51 (52),
  `wissenKennenExercises` #0-50 (51).

## Explications réécrites contre l'espagnol

Aucune explication de ce lot ne compare au français ; elles sont traduites sans règle ajoutée.
Deux retouches seulement, où l'espagnol aide :

- `derEinExercises#45` (schmecken) et `#51` (gefallen) : ajout de « igual que con «gustar» » après
  « la chose est sujet, la personne au datif ». C'est un appui, pas une règle ; à retirer si l'on veut
  la traduction nue.
- `derEinExercises#48` : « Attention, Rock est masculin en allemand » gardé tel quel (« Ojo: Rock es
  masculino en alemán ») : le piège vaut aussi pour l'espagnol (*la falda*).

Choix de termes :
- cas en espagnol dans les indices et les explications (*nominativo, acusativo, dativo, genitivo*),
  puisque la source les donne en français ; « COD » → *objeto directo* ; « prétérit » → *Präteritum* ;
- « mots en dies- / ein- / der- » → *palabras en dies- / ein- / der-* ; « ein-Wörter » gardé ;
- « reste nu » → *se queda sin terminación* ;
- *trotzdem* → « Aun así, » partout ; *obwohl* → « aunque » + indicatif (faits réels) ;
- `wissen / kennen` : indice « (¿conocer a alguien o algo, o saber un hecho?) » — l'espagnol a la
  même paire *saber / conocer*, rien à réécrire.

## Choix de traduction à connaître

- `ihr` → *ustedes* (`derEin#19`, `#33`, `wissenKennen#12`, `#20`, `#31`) ; `Sie` → *usted*
  (`derEin#34`, `wissenKennen#10`, `#17`, `#26`, `#39`).
- Perfekt → pretérito (« Aunque lo llamé, no vino. », « Cada estudiante aprobó el examen. »).
- Vocabulaire : *carro, autobús, apartamento, el cuarto* (Zimmer), *la tienda* (Laden), *el clima*
  (`derEin#43`), *apurarse* (sich beeilen), *mi papá / mi mamá* (`derEin#23`, `#24`, `wissenKennen#4`).
- Le pronom sujet (*él, ella*) est écrit quand il distingue la phrase ou évite une ambiguïté.

## Doutes

- `wissenKennenExercises#43` — « Ich kenne das Rezept auswendig. » : « Conozco la receta de
  memoria. » pour rester du côté de *kennen* ; l'espagnol dirait plutôt « Me sé la receta de
  memoria », ce qui tirerait l'apprenant vers *wissen*.
- `wissenKennenExercises#42` — « ¿Conoces la diferencia? » (même raison ; « ¿Sabes la diferencia? »
  existe aussi).
- `wissenKennenExercises#15` — « Weißt du seine Telefonnummer? » : « ¿Sabes su número de teléfono? »
  (le français dit « Connais-tu » ; l'espagnol suit l'allemand).
- `wissenKennenExercises#44` — « Seguro que ella sabe una solución. » : un peu raide, comme
  l'allemand (« sabe de una solución » serait plus naturel).
- `wissenKennenExercises#34` — « Du kennst mich doch! » : « ¡Pero si tú me conoces! ».
- `wissenKennenExercises#38` — « in der Nähe » : « cerca » (le français dit « dans le quartier »).
- `derEinExercises#18` — *Tasche* : « bolsa » (Mexique ; « bolso » en Colombie). À trancher.
- `derEinExercises#23`, `#24` — *Vater / Mutter* rendus « papá / mamá » ; « padre / madre » si l'on
  veut le registre neutre de la source.
- `derEinExercises#36` — « dabei » : « No traemos dinero. » ; `#33` « ¿Traen ustedes su pasaporte? ».
- `derEinExercises#7`, `#11` — « Mit diesem Zug / Auto fahre ich nie / nicht » : « En este tren no
  viajo nunca. », « En este carro no voy. » (l'ordre allemand gardé, complément en tête).
- `derEinExercises#38` — *Kinder* : « hijos » (« Ella no tiene hijos. »), « niños » ailleurs.
- `derEinExercises#46` — *Lehrerin* : « maestra ».
- `obwohlTrotzdemExercises#18` — « hat gut geschmeckt » : « sabía bien ».

## Sources fautives

- `wissenKennenExercises#13`, `#15`, `#33`, `#44` : la bonne réponse est *wissen* devant un **nom**
  (« die Antwort », « seine Telefonnummer », « eine Lösung »), mais l'explication commune ne parle que
  de subordonnée, de question indirecte ou de « es / das / nichts ». Elle n'explique pas ces phrases
  (et contredit l'indice « un nom seul → kennen »). Traduite telle quelle ; à compléter dans toutes
  les langues.
- `wissenKennenExercises#48`, `#50` : la réponse est le Präteritum *wusste*, l'explication donne les
  formes du présent (« ich weiß, du weißt, er weiß »). Traduite telle quelle.
- `wissenKennenExercises#3` : « Comparer avec la phrase précédente » suppose que #2 vient juste avant,
  ce qui n'est pas garanti si l'app tire les exercices au hasard.
- `wissenKennenExercises#0-7` ont le topic « wissen ou kennen » (français), #8-50 « wissen / kennen » :
  `topic` n'est pas dans `champs`, à traduire ailleurs si l'app l'affiche.
- `derEinExercises#1` : « ni sujet ni COD marqué » est obscur en français aussi (« Problem » est ici
  attribut, au nominatif) ; traduit au plus près (« sin marca ni de sujeto ni de objeto directo »).
- `derEinExercises#32` : « Wir suchen unsere Wohnung. » (« Nous cherchons notre appartement ») — phrase
  étrange mais fidèle ; rien de faux.
- `obwohlTrotzdemExercises#40` : le français met « Elle l'avait promis » pour le Perfekt « hat es
  versprochen » ; l'espagnol suit l'allemand (« Ella lo prometió. »).

## À trancher

- *Tasche* : bolsa / bolso (`derEin#18`).
- *papá, mamá* ou *padre, madre* dans les phrases d'exemple (`derEin#23`, `#24`).
- L'ajout « igual que con «gustar» » (`derEin#45`, `#51`) : le garder ou non.
