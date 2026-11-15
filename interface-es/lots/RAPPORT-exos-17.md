# Rapport — exos-17 (15 nov. 2026)

## Fait

- `lots/exos-17.es.json` : **140 exercices sur 140**, chacun avec `translation`, `hint`, `explanation`.
  Contrôle `exos.py controle` : **0 faute, 0 avis**.
- Répartition : `transformationConnecteursExercises` #27 à #49 (23), `ordreInverseExercises` #0 à #53 (54),
  `praepWahlExercises` #0 à #49 (50), `verbenMitPraepExercises` #0 à #12 (13).
- Les explications répétées de la source (une par gabarit) reçoivent partout le même texte espagnol ;
  les phrases allemandes citées (« Compara: «…» → «…» ») sont recopiées de la source, vérifiées par script.
- `translation` des exercices « Transformer » et « Retourner » : la phrase de **départ** (`_question`),
  comme le fait le français, pas la phrase transformée.

## Explications réécrites contre l'espagnol

- `praepWahlExercises#11`, `#39` (bei) : « chez quelqu'un » → « en casa de alguien » ; la traduction de #39
  est « Trabajo en Siemens », celle de #11 « Todavía vivo con mis padres ».
- `praepWahlExercises#5`, `#22`, `#38` (zu) : « aller chez une personne » → « ir a ver a una persona ».
- `praepWahlExercises#18` (in + durée = « dans ») → « dentro de » ; `#19` (vor = « il y a ») → « hace ».
- `praepWahlExercises#1`, `#2` : « rentrer chez soi / être chez soi » → « ir a casa / estar en casa ».
- `verbenMitPraepExercises#4` : « Pas « an » : c'est « für » » était le piège du francophone
  (s'intéresser **à**). L'espagnol dit « interesarse por » : le piège n'est plus annoncé, il reste
  « con este verbo va «für» ».
- `verbenMitPraepExercises#0` : « Jamais « warten für » » gardé (l'hispanophone dit aussi « esperar por »).
- « Comparez » → « Compara » (tutoiement), dans les 54 `ordreInverseExercises`.

## Sources fautives

- `transformationConnecteursExercises#30` et `#31` (bevor → danach) : le français et l'anglais disent que
  « bevor » met l'action **antérieure** dans la subordonnée (texte recopié de « nachdem »). C'est
  l'inverse : « Bevor wir essen » porte l'action **postérieure**. L'espagnol dit « la acción posterior » ;
  le français, l'anglais et les autres langues sont à corriger (si l'on préfère la fidélité, remettre
  « anterior » dans ces deux entrées).
- `ordreInverseExercises#4` : « Nachdem wir gegessen haben, sind wir spazieren gegangen » — la norme veut
  le Plusquamperfekt (« gegessen hatten ») devant un Perfekt, comme dans #7 et #15. De même #30
  (« Nachdem ich umgezogen bin, werde ich… ») est familier. Allemand non touché.
- `praepWahlExercises#25` et `#45` : l'explication range « Bahnhof » parmi les lieux en « auf », alors que
  #23 enseigne « am Bahnhof ». Traduit tel quel.

## Doutes

- `ordreInverseExercises#13` : « Als ich klein war » → « Cuando era pequeño » (masculin, comme le français).
- `ordreInverseExercises#17` : « hat es stark geregnet » → « llovió muy fuerte » (« llovía » serait aussi naturel).
- `ordreInverseExercises#44`, `#45` : « falls » rendu par « En caso de que… » + subjonctif.
- `ordreInverseExercises#46`, `#48` : « solange » → « Mientras » + subjonctif (« Mientras llueva », « Mientras viva aquí »).
- `verbenMitPraepExercises#2` : « Ich freue mich auf das Wochenende » → « Tengo muchas ganas de que llegue el fin de semana ».
- `verbenMitPraepExercises#10` : « Lehrer » → « profesor » (niveau scolaire inconnu).
- `praepWahlExercises#28`, `#29`, `#34` : heures gardées en chiffres comme la source (« de 9 a 18 h », « las 18 h », « las 20 h »).

## À trancher

- `verbenMitPraepExercises#12` : « der Stau » → « el embotellamiento » (Mexique ; « trancón » en Colombie, « tráfico » partout mais moins précis).
- `praepWahlExercises#46` : « im dritten Stock » → « en el tercer piso » (le compte des étages diffère selon les pays).
- `praepWahlExercises#17` : « E-Mail » → « correo electrónico » (« correo » ou « mail » sont aussi courants).
- `ordreInverseExercises#28`, `#42`, `praepWahlExercises#26` : « Auto » → « carro » (consigne) ; `praepWahlExercises#49` : « Ticket » → « boleto ».
