# Rapport — exos-03 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/exos-03.json`, 140 exercices. Rendu : `interface-es/lots/exos-03.es.json`, 140 exercices.
  - `konjunktiv2Exercises#15` à `#69` (55) : `translation`, `explanation`, et `hint` pour les 20 « würde + infinitif ».
  - `infinitivExercises#0` à `#69` (70) : `question`, `translation`, `hint`, `explanation`.
  - `kasusReconnaissanceExercises#0` à `#14` (15) : `question`, `translation`, `hint`, `explanation`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Les 140 traductions sont écrites à la main, d'après la phrase allemande. Les explications, indices et consignes, qui suivent une dizaine de gabarits dans la source, ont été rendus gabarit par gabarit (les formes allemandes recopiées de la source), pour que la même phrase française donne partout la même phrase espagnole.
- `ihr` → `ustedes` partout ; `Sie` (`infinitivExercises#60`) → `usted` (« ¿Puedo preguntarle algo? »).

## Explications réécrites contre l'espagnol

- `konjunktiv2Exercises#56` à `#69` (14) : « 2e personne du pluriel » devient « 2.ª persona del plural (ihr: «ustedes», de confianza) », parce que la traduction dit « ustedes » et que l'hispanophone d'Amérique n'a pas de forme propre à *ihr*.
- `infinitivExercises#21`, `#60`, `#64` : après un verbe modal, le second verbe reste à l'infinitif, « igual que en español » (puedes traer).
- `kasusReconnaissanceExercises#0` à `#14`, l'**indice** (le même pour les 15) : les quatre questions françaises « qui/quoi ? — à qui ? » ne séparent pas l'Akkusativ du Dativ en espagnol, où l'objet direct de personne prend aussi « a » (« veo a Juan »). L'indice ajoute donc le test des pronoms : « ¿qué? / ¿a quién? (lo, la) — ¿a quién le…? (le) ».
- `kasusReconnaissanceExercises#0` : « ¿a quién le explica? », avec « les explica » ; `#1` : objet direct, avec « lo veo » (la traduction dit « Veo al perro », dont le « a » pourrait faire croire à un datif) ; `#2` : « el color DEL carro ».

## Doutes (9)

1. `kasusReconnaissanceExercises#0-#14`, indice : plus long que la source ; à relire par quelqu'un qui enseigne (et le leísmo n'est pas un souci en Amérique latine, mais le test lo/le suppose que l'apprenant le sent).
2. `konjunktiv2Exercises#56-#69` : la parenthèse « (ihr: «ustedes», de confianza) » répétée 14 fois ; à retirer si on la juge lourde.
3. `konjunktiv2Exercises#19`, `#33`, `#47`, `#61` (*dürfen*) : « tendrías permiso de » pour le premier, « podría / podríamos / podrían » pour les autres ; l'espagnol ne sépare pas *dürfen* de *können* aussi nettement.
4. `konjunktiv2Exercises#23`, `#65`, `infinitivExercises#10` (*wandern*) : « ir de caminata » (plutôt que « hacer senderismo »).
5. `infinitivExercises#29` : « Él jala el carrito a lo largo de la calle » — « jalar » est du Mexique et de Colombie, le Cône Sud dit « tirar de » ; et *Wagen* rendu par « carrito » d'après le français « chariot ».
6. `infinitivExercises#30` : « a las dieciocho horas », gardé sur 24 heures comme l'allemand (l'usage courant dirait « a las seis de la tarde »).
7. `infinitivExercises#63`, `kasusReconnaissanceExercises#0` : *der Lehrer* → « el profesor » (rien ne dit primaire ou lycée).
8. `infinitivExercises#8` : *Sie reisen* → « Ellos viajan », comme le français ; la majuscule de début de phrase permet aussi « Usted(es) ».
9. `infinitivExercises#57` : *die Rechnung* → « la cuenta » (ce pourrait être « la factura »).

## À trancher (mots où l'Amérique latine hésite)

- `infinitivExercises#9` : *Briefmarken* → « estampillas » (Colombie, Cône Sud ; le Mexique dit « timbres »).
- `infinitivExercises#17` : *Kuchen* → « pastel » (Mexique ; la Colombie dit « torta » ou « ponqué »).
- `konjunktiv2Exercises#53` : *Boot* → « bote » (ou « lancha », « barco »).
- `konjunktiv2Exercises#26`, `#40`, `#68` : « jugar tenis / golf / cartas » sans « a », usage d'Amérique.

## Sources fautives ou bancales

- `konjunktiv2Exercises#24` : l'allemand dit « wenn ich dich brauche » (indicatif), le français « si j'avais besoin de toi ». J'ai suivi l'allemand : « si te necesito ».
- `konjunktiv2Exercises#19` : le français « à ma place » abrège « wenn du an meiner Stelle wärst » ; l'espagnol rend la subordonnée entière.
- `infinitivExercises#18` : « am Samstag » rendu en français par « le samedi » (habitude) ; l'allemand parle d'un samedi : « el sábado ».
- `infinitivExercises#21`, `#60`, `#64` : la consigne demande « l'infinitif du verbe conjugué », mais le verbe conjugué est le modal (*kannst*, *darf*) et la réponse attendue est le second verbe (*bringen*, *fragen*, *zeigen*). L'indice français (« le verbe conjugué est déjà à l'infinitif ») se contredit ; j'ai écrit « el verbo que buscas ya está en infinitivo ». L'exercice lui-même reste bancal dans toutes les langues.
- `infinitivExercises#37`, `#50`, `#55`, `#20` : réponse attendue *fühlen*, *setzen*, *entscheiden*, *treffen* alors que la phrase emploie le verbe pronominal (*sich fühlen*…) ; rien à changer en espagnol, signalé pour mémoire.
