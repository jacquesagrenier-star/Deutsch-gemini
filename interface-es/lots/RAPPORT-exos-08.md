# Rapport — exos-08 (15 nov. 2026)

## Ce qui est fait

- `interface-es/lots/exos-08.es.json` : **140 exercices sur 140**, chacun avec `translation`, `hint`, `explanation`
  (420 textes). Contrôle `exos.py controle` : **0 faute, 0 avis**.
- Jeux : `zuInfinitivExercises` #48-60 (13), `wortstellungV2Exercises` #0-52 (53),
  `wortstellungSubExercises` #0-49 (50), `wortstellungFrageExercises` #0-23 (24).
- Les explications répétées de la source (« Le verbe conjugué est le DEUXIÈME élément… », « Un groupe entier
  compte pour UN seul élément… », « Après « weil », le verbe conjugué (…) va à la fin. ») ont **une seule**
  formulation espagnole chacune, comme dans la source.

## Explications réécrites contre l'espagnol

Aucune explication de ce lot ne comparait au français (« comme en français », piège propre au français) :
rien n'a donc été réécrit, et aucune règle n'a été ajoutée. Seules les **gloses** françaises ont été mises
en espagnol :

- `zuInfinitivExercises#57` : « afin de » → «para» ; `#58` : « sans » → «sin» ; `#59` : « au lieu de » → «en lugar de».
- `wortstellungSubExercises#40` : « da (puisque) » → «da» (ya que).

## Choix de traduction

- **ihr → ustedes**, écrit en toutes lettres quand la phrase serait sinon ambiguë (zu#52, Sub#5, #15, #25, #35,
  Frage#2, #16, #20, #22) ; **Sie → usted** (Frage#23).
- **Perfekt → pretérito** (V2#14, #18, #19, #20, #33, #35, #41, #43, #51 ; Frage#5, #7, #15).
- Adjectif d'une personne « ich / du » sans genre connu : **cansado(a)**, **contento(a)** (même forme que les lots
  précédents) ; *glücklich* → **feliz**, qui évite le double genre.
- *obwohl* → **aunque + indicatif** (fait réel), pas le subjonctif du français.
- *da* → **ya que**, *weil* → **porque**, pour garder les deux conjonctions distinctes.
- *zufrieden* → **contento(a)** (plus naturel que *satisfecho*).

## Doutes

- `wortstellungV2Exercises#5` : « juegan fútbol » (sans *al*, usage du Mexique et de la Colombie) ; l'Argentine dit « juegan al fútbol ».
- `wortstellungV2Exercises#24` : *fand statt* → « el partido se jugó » (plutôt que « tuvo lugar »).
- `wortstellungV2Exercises#28` : *fuhren los* → « partimos » (le départ en véhicule ne se dit pas).
- `wortstellungV2Exercises#30` : *einen guten Bäcker* → « un buen panadero » (littéral ; on dirait aussi « una buena panadería »).
- `wortstellungV2Exercises#32` : *Jetzt habe ich es verstanden* → « Ahora lo entendí. » (« Ahora lo he entendido » possible).
- `wortstellungSubExercises#16` : *Der Lehrer* → « El maestro » (« El profesor » si l'on pense au lycée).
- `wortstellungSubExercises#49` : *ein Feuer machen* → « Hacemos fuego ».
- `wortstellungFrageExercises#4` : *Sind wir spät dran?* → « ¿Vamos tarde? ».
- `wortstellungFrageExercises#19` : *Was ist er von Beruf?* → « ¿A qué se dedica él? ».
- Sujets *er / sie* gardés (« él », « ella ») là où la phrase espagnole perdrait qui parle ; omis ailleurs.

## Sources fautives ou écartées de l'allemand (j'ai suivi l'allemand)

- `wortstellungV2Exercises#31` : *Hier kann man gut essen.* — le français dit « Ici, on mange bien. » (sans *pouvoir*) ; rendu « Aquí se puede comer bien. ».
- `wortstellungV2Exercises#47` : *Abends wird es hier sehr ruhig.* — le français dit « c'est très calme » ; *wird* = devient ; rendu « se pone muy tranquilo ».
- `wortstellungV2Exercises#34` : *zu spät* — le français dit « en retard » ; rendu « demasiado tarde ».
- `wortstellungV2Exercises#52` : *Bis morgen ist alles fertig.* — présent allemand à valeur de futur ; rendu au futur (« estará listo »), comme le français.
- Aucune faute relevée dans l'allemand.

## À trancher

- « juegan fútbol » / « juegan al fútbol » (V2#5).
- « cansado(a) » : la forme à parenthèse est celle des lots précédents ; à unifier si une autre convention est retenue pour toute l'interface.
