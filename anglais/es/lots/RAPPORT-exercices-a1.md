# Rapport : exercices A1 et textes des scènes en espagnol (2 nov. 2026)

## Chiffres

- `exercices-01.es.json` : 184 questions (adjectifs → prépositions de lieu), `exercices-02.es.json` : 203 (prépositions de temps → there). **387 / 387**, dans l'ordre de la source.
- `textes-90.es.json` : **75 / 75** textes de scènes (37 `alt`, 37 `consigne`, 1 titre de couche A1 : « Los sustantivos »).
- `PYTHONIOENCODING=utf-8 python anglais/es/poser_textes.py controle` : textes 1741/1741, **0 faute**, 2 avis (tous deux dans des lots d'une autre session : « -est » anglais pris pour « est ») ; exercices 387/387, **0 faute, 0 avis**.
- Espagnol neutre, tutoiement, aucun « vosotros ». Les lots ont été produits par un script du scratchpad qui attache les id de la source dans l'ordre (aucun id retapé à la main).

## Les scènes : déplacées à Boston

Le français des scènes anglaises dit encore Berlin, Hambourg, le Brandebourg, l'Espagne et le Bürgeramt (il vient de la scène allemande). En espagnol, j'ai suivi la consigne « les scènes se passent à Boston » et les titres anglais de `anglais/outils/scenes.py` :

- Berlin → Boston partout (buero, friseur, fruehstueck, kleidergeschaeft, kueche, museum, musik, park, restaurant, sportplatz, umzug, winter) ; `park` → « el parque Boston Common » ; `flughafen` → « el aeropuerto Logan de Boston » ; `buergeramt` → « el ayuntamiento de Boston » (titre anglais *At City Hall*).
- `hotel` (alt + consigne) : Hambourg **retiré**, « fuera de la ciudad » — je n'ai pas inventé de ville. À trancher si on veut en nommer une (New York ?).
- `bauernhof` consigne : « dans le Brandebourg » → « en el campo ».
- `strand` alt : « en Espagne » retiré (« Anna en la playa »).
- `klassenzimmer` alt : « Un cours d'espagnol du soir » → « Una clase de idiomas por la noche en Boston ». Pour un hispanophone qui apprend l'anglais, « clase de español » sonne faux ; mais si le tableau de l'image montre de l'espagnol, « idiomas » reste vrai. **Doute à vérifier sur l'image.**
- `musik` : l'alt décrit une école de musique (le titre anglais dit *Music at home*) ; j'ai suivi l'alt, qui décrit l'image.

## Doutes par id

- `beEnExercises|___ he your brother?` et `pronomsSujetObjetEnExercises|___ is my brother.` : le français dit « C'est ton frère ? / C'est mon frère » ; j'ai rendu la phrase anglaise (« ¿Es tu hermano? », « Él es mi hermano. »).
- `fauxAmisEnExercises|I'm tired, I want to ___.` et `questionsEnExercises|___ are you sad?` : « Estoy cansado » au masculin — c'est le locuteur de la phrase, pas l'usager ; la source française est au masculin aussi.
- `prepLieuEnExercises|Welcome ___ Boston!` : « ¡Bienvenidos a Boston! », comme `textes-01` (premiers pas). C'est une phrase d'exercice, pas un texte qui vise l'usager.
- `heureDatesEnExercises|1999 is read ___.` et `2010 is usually read ___.` : la traduction française est déjà une méta-phrase (« se lit par paires ») ; rendue de même en espagnol, avec les formes anglaises gardées.
- `tempsPresentSimpleEnExercises|Yes, I ___.` / `No, she ___.` : traductions « Sí. (respuesta a «Do you…?») », comme la source.
- `tempsPresentContinuEnExercises|Prices ___ going up every month.` : « Los precios suben cada mes » (présent simple espagnol ; « están subiendo » serait plus proche mais lourd).
- `tempsPresentContinuEnExercises|It ___ raining anymore.` : « Ya no llueve. »
- `pronomsSujetObjetEnExercises|Is this your umbrella? — No, ___ isn't.` : « — No. » comme la source ; la question est sur `it`, que l'espagnol n'a pas.
- `prepLieuEnExercises|The bank is ___ the post office and the café.` : « la oficina de correos » (« el correo » seul est ambigu).
- `heureDatesEnExercises|It's 8 p.m. — It's eight in the ___.` : « ocho de la noche » — l'espagnol n'a pas de « evening » ; l'explication le dit.

## Sources qui me semblent fautives ou bancales

- `demonstratifsEnExercises|___ is my friend Paul.` : la traduction française (« Je te présente mon ami Paul ») est une adaptation, pas la phrase ; gardée telle quelle en espagnol (« Te presento a mi amigo Paul »), fidèle à l'usage.
- `heureDatesEnExercises|It's 7:10. — It's ten ___ seven.` : l'explication dit « américain : after » alors que l'app enseigne l'américain par défaut et que la bonne réponse est *past* ; les deux sont justes, j'ai écrit « past (en Estados Unidos, también after) ».
- `prepTempsEnExercises|I usually have coffee ___ breakfast.` : la traduction française dit « avec le déjeuner » (québécisme pour le petit-déjeuner) ; en espagnol « el desayuno ».
- `prepTempsEnExercises|I'll call you ___ lunch.` : « après le dîner » (dîner = midi au Québec) ; en espagnol « el almuerzo ».
- `tempsPresentContinuEnExercises|I ___ cooking dinner right now.` et les « souper » : rendus « la cena ».
- `thereEnExercises|I saw him two days ___.` : la question porte sur *ago*, pas sur *there* ; rangée dans la série « there » sans doute parce que « il y a » se dit *there is* **et** *ago*. Explication adaptée (« «Hace» + tiempo: ago »), car l'espagnol n'a pas cette ambiguïté.
- `possessifsEnExercises|___ raining again.` et `pronomsSujetObjetEnExercises|___'s raining.` : même point enseigné deux fois (normal, séries différentes).
- `pronomsEnExercises|The dog is in ___ bed.` : « dans son panier » — j'ai écrit « en su cama » (la phrase anglaise).

## Explications réécrites contre l'espagnol (comparaison ajoutée)

Le français comparé a été retiré partout ; une comparaison avec l'espagnol a été ajoutée seulement là où le piège est réel :

- **Sujet obligatoire / it** : `beEnExercises|It ___ cold this morning.` ; `continuEnExercises|Look! It ___ snowing!` ; `possessifsEnExercises|___ raining again.` ; `presentEnExercises|It ___ a lot in April.` ; `pronomsSujetObjetEnExercises|___'s raining.` (« «Is raining» es un error ») ; `pronomsSujetObjetEnExercises|___ live in Boston.` et `Can ___ come in?` (I toujours écrit, en majuscule).
- **Ser / estar = be** : `beEnExercises|We ___ very tired today.`
- **Tener → be** (âge, faim, froid) : `beEnExercises|___ you hungry?`, `I'm twenty ___ old.`, `I ___ cold…` ; `nombresEnExercises|My sister is ___ (13).`, `I'm ___ years old.`
- **do / does / did** pour la question et la négation : `beEnExercises|___ he your brother?` (pas de do avec be) ; `presentEnExercises|He ___ speak Spanish.`, `___ you play the guitar?` ; `tempsPresentSimpleEnExercises|I ___ like mushrooms.` (« «No like» es un error ») ; `questionsEnExercises|What time ___ it?`
- **like ≠ gustar** (la personne est le sujet) : `presentEnExercises|I ___ like fish.` ; `tempsPresentSimpleEnExercises|___ you like pizza?`
- **Pas d'article pour les généralités** : `articlesEnExercises|I like ___.`, `She speaks ___.` (+ majuscule des langues) ; `tempsPresentSimpleEnExercises|Water ___ at 100 degrees…`, `Cats ___ milk.`
- **Article devant une profession** : `articlesEnExercises|He's ___ engineer.`, `My sister is ___ teacher.` ; `beEnExercises|I ___ a student.`
- **Adjectif invariable** : `adjectifsEnExercises|I have two ___ cars.` (« ni plural ni femenino »).
- **his / her selon le possesseur** : `possessifsEnExercises|She lost ___ keys.` (« «Su» no lo distingue; el inglés sí »).
- **Possessif pour les parties du corps** : `possessifsEnExercises|I washed ___ hair.`, `He broke ___ arm.`
- **hay = there is / there are** : `pronomsSujetObjetEnExercises|___ are many parks in Boston.` ; `thereEnExercises|There ___ three bedrooms.` (« «Hay» no cambia; en inglés sí »).
- **since / for = desde / desde hace** : `prepTempsEnExercises|I've worked here ___ May.`, `I've worked here ___ six months.`
- **ago = hace, en fin de phrase** : `heureDatesEnExercises|She left two hours ___.` ; `thereEnExercises|I saw him two days ___.`
- **arrive at / in, jamais « arrive to »** : `prepLieuEnExercises|I arrived ___ the airport…` ; **near sans « of »** : `There's a park ___ my house.`
- **Faux amis** : `fauxAmisEnExercises|Actually…` (en realidad ≠ actualmente), `library` / `bookstore` (biblioteca ≠ librería), `attended` (asistir, sans préposition), `waiting for` (attend ≠ asistir).
- **Une seule négation** : `tempsPresentSimpleEnExercises|She never ___ late.`
- **what time, pas « what hour »** : `heureDatesEnExercises|What ___ is it? — It's six o'clock.` ; **what is your name, pas « how »** : `questionsEnExercises|___ is your name?`
- **Pronom après préposition** : `pronomsSujetObjetEnExercises|Between you and ___…` (« no «I» »).

Aucune comparaison douteuse n'a été ajoutée ; les explications purement formelles (-ies, -es, consonne doublée, past / to…) sont restées des traductions courtes.

## À trancher (Amérique latine écrite / Espagne)

Les lots d'exercices et de scènes n'ont qu'une colonne : j'ai écrit la forme d'Amérique latine (comme les lots `corpus-*`), ou la forme comprise des deux quand elle existe.

- **auto / coche (carro)** : `adjectifsEnExercises|I have two ___ cars.`, `demonstratifsEnExercises|Is ___ your car over there?`, `nombresEnExercises|This car costs two ___ dollars.`, `possessifsEnExercises|Your car is fast, but ___ is faster.`, `prepLieuEnExercises|I left my bag ___ the car.`, `The car is parked ___ the house.`, `presentEnExercises|___ she have a car?`, `pronomsEnExercises|This is ___ car.`, `tempsPresentContinuEnExercises|He ___ his car today…`, `We're ___ to Maine next weekend.`, `tempsPresentSimpleEnExercises|She doesn't ___ a car.` ; scènes `apotheke|alt`, `fahrradwerkstatt|alt`, `winter|alt`. Les cartes du corpus disent « el carro, el auto » ; j'ai pris « auto », compris en Espagne.
- **estacionado / aparcado** : `prepLieuEnExercises|The car is parked ___ the house.`
- **manejar / conducir** : `canEnExercises|He ___ drive, he's only twelve.`
- **apartamento** (neutre ; corpus : departamento / piso) : `possessifsEnExercises|We love ___ new apartment.`, `pronomsEnExercises|___ live in a small apartment.` ; scènes `geburtstag`, `heimwerken`, `kueche`, `umzug`, `wohnzimmer`.
- **refrigerador / nevera** : `prepositionsEnExercises|The milk is ___ the fridge.`, `thereEnExercises|___ there any eggs in the fridge?`
- **jeans / vaqueros** : `tempsPresentContinuEnExercises|I ___ jeans every day.` ; `waschsalon|alt`.
- **básquetbol / baloncesto** : `tempsPresentSimpleEnExercises|They sometimes ___ basketball after school.`
- **champiñones** (neutre ; hongos / setas) : `tempsPresentSimpleEnExercises|I ___ like mushrooms.`
- **la tarea / los deberes** : `tempsPresentSimpleEnExercises|He ___ his homework in the evening.`
- **papas / patatas** : `familie|alt`, `kueche|alt`, `markt-gemuese-wurzel|alt`. **jugo / zumo** : `baeckerei`, `familie`, `fruehstueck`, `geburtstag` (alt). **pastel / tarta** : `baeckerei`, `fruehstueck`, `geburtstag`, `restaurant` (alt ; « tarta de fresas » gardé pour la tarte).
- **mesera, mesero / camarera, camarero** : `fruehstueck|alt`, `restaurant|alt`.
- **lentes / gafas** : `bibliothek|alt`, `friseur|alt`, `klassenzimmer|consigne`, `restaurant|alt`.
- **suéter / jersey** : `kleidergeschaeft|alt`, `schlafzimmer|alt`, `waschsalon|alt`. **curitas / tiritas** : `apotheke|alt`. **boleto / billete** : `flughafen|alt`. **computadora portátil / portátil** : `bibliothek|alt`. **pasantía / prácticas** : `buero|alt`, `buero|consigne`. **banca / banco** : `park`, `sportplatz`, `waschsalon`, `winter` (alt). **balde / cubo**, **bombilla / foco**, **canasta / cesta** : `fahrradwerkstatt|alt` ; **bombilla** aussi dans `umzug|alt`. **audífonos / auriculares** : `museum|alt`. **la sala / el salón** : `geburtstag|alt`, `wohnzimmer|alt`. **vitrina / escaparate** : `apotheke`, `baeckerei`, `fahrradwerkstatt`, `friseur`, `waschsalon` (alt).
- **Marché** (`markt-*|alt`) : arvejas (guisantes, chícharos), frijoles (judías), repollos (coles), batatas (boniatos, camotes), remolachas (betabeles), albaricoques (chabacanos, damascos), duraznos (melocotones), aguacates (paltas), toronjas (pomelos). Les scènes espagnoles de l'app (`visuel/prototype/espanol/mots.json`) emploient les formes d'Espagne.
- **Nombres décimaux** : aucun dans ces sources (heures « 3:15 », « 8:15 » : deux-points dans les deux espagnols).
