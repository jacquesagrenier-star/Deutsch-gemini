# Rapport — collisions de l'espagnol (interface de l'allemand)

Source : `interface-es/sources/collisions.json`, 88 groupes.

## Ce qui est fait

- **41 groupes départagés**, 49 corrections dans `collisions-corrections.json`
  (`corriger.py controle` → 0 faute ; rien n'est posé).
- **47 groupes acceptés**, une ligne chacun dans `collisions-acceptees.txt`
  (catégories `noms`, `verbes`, `adjectifs`, comme `relecture_tr/collisions-acceptees.txt`).
- Chaque réponse nouvelle a été comparée à toutes les `traduction_es` des six fichiers :
  aucune n'est déjà la réponse d'un autre mot allemand.

## Comment j'ai tranché

- **Deux sens différents sous un même mot espagnol** → précision entre parenthèses
  (sueño, regla, muñeca, medida, escala, timbre, entrada, salida, dirección, pueblo,
  interés, competencia, corredor, extranjero, tenis, paquete, preparación, recuperación,
  perdón, ascenso, almacenamiento, proveedor, crema, mañana, semestre, tarea).
- **L'espagnol a un autre mot naturel** → Bad « el cuarto de baño », Schneeschmelze
  « el derretimiento de la nieve », Prospekt « el folleto publicitario », Tonleiter
  « la escala musical », Tipp « el consejo práctico, el tip ».
- **Alignement sur l'autre carte du même mot allemand**, qui avait déjà une réponse plus
  précise ailleurs dans le corpus : Anzeige (« el anuncio »), Quittung (« el comprobante de
  pago, el recibo »), Impfung (« la vacunación, la vacuna »), Schaufenster (« la vitrina, el
  aparador »), wert sein (« valer (el esfuerzo), valer la pena »).
- **Synonymes, forme courte / longue, sigle, variante d'Autriche ou de Suisse** → acceptés.

## Mes doutes

- **Team → « el equipo (de trabajo) »** : Team se dit aussi d'une équipe sportive. La
  précision suit le thème de la carte (Arbeit und Büro), pas tout l'usage du mot.
- **Bücherei → « la biblioteca (pública) »** : une Bibliothek peut être publique aussi ; la
  parenthèse n'est qu'un indice (la Bücherei est la bibliothèque de prêt du quartier).
  Si une relectrice la juge trompeuse, accepter le doublon.
- **Differenz → « la diferencia (entre dos cifras) »** : juste dans son thème (Zahlen und
  Mengen), mais Differenz veut dire aussi « désaccord ».
- **Tipp → « el consejo práctico, el tip »** : « el tip » est courant au Mexique et en
  Colombie, mais c'est un anglicisme ; à faire confirmer.
- **Bad → « el cuarto de baño »** et **Toilette → « el baño »** : en Amérique latine on dit
  « el baño » pour les deux ; la carte reste juste, mais « el baño » seul pourrait aussi
  appeler Bad.
- **Sahne → « la crema (de leche) »** : « crema de leche » est le terme de Colombie et du
  Cône Sud ; au Mexique on dit « crema » tout court (d'où la parenthèse).
- **Haltbarkeitsdatum / Verfallsdatum, accepté** : l'allemand distingue « à consommer de
  préférence avant » et « date limite » ; l'espagnol officiel aussi (« fecha de consumo
  preferente »), mais personne ne le dit. À trancher par une locutrice.
- **Verspätung / Verzögerung, accepté** : on pourrait donner « el retraso » à l'un et « la
  demora » à l'autre ; je ne l'ai pas fait, la répartition serait arbitraire.
- **Rezeption / Empfang, accepté** : la carte Empfang est rangée dans « Medien und
  Technologie » alors que son exemple parle du comptoir d'accueil — thème à vérifier côté
  allemand.
- **Volk au niveau A1** (themes.json #2461) : niveau surprenant, hors de ma part.

## Vu en passant (hors de ma part)

- Plusieurs mots allemands présents deux fois ont deux réponses espagnoles différentes
  (Annonce, Impfpass, Festessen, Schlagobers, Wettbewerb, Leitung, Tageskarte, zustellen, Art) :
  pas des collisions, mais une harmonisation serait à faire.
- Près des doublons sans en être : Ratschlag « el consejo (uno concreto) » à côté de Rat
  « el consejo » ; Gang « el corredor; el plato (de una comida) » à côté de Korridor.
