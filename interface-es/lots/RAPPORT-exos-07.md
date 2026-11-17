# Rapport — exos-07 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/exos-07.json`, 140 exercices. Rendu : `interface-es/lots/exos-07.es.json`, 140 exercices.
  - `praepReconnaissanceExercises#8` à `#49` (42) : `question`, `translation`, `hint`, `explanation`, `options` ; `correct` en plus pour les huit Wechselpräpositionen (`#42` à `#49`).
  - `praepWoWohinExercises#0` à `#49` (50) : `translation`, `hint`, `explanation`.
  - `zuInfinitivExercises#0` à `#47` (48) : `translation`, `hint`, `explanation`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Les traductions sont écrites à la main d'après la phrase allemande ; le fichier est assemblé par un script du scratchpad (écrit avec Write, pas de heredoc), qui vérifie que la forme allemande citée à la fin de chaque explication Wo / Wohin est celle de la source.
- Mêmes formules que le lot 06 pour les prépositions : « — ¿qué caso exige esta preposición? », l'indice, « Depende (Wechselpräposition) », « forma parte del grupo que siempre va con… ». `Akkusativ`, `Dativ`, `Genitiv`, `Wo?`, `Wohin?`, `Wahrnehmungsverb` restent en allemand ; « accusatif + infinitif », en français dans la source, devient « acusativo + infinitivo ».

## Explications réécrites contre l'espagnol

Aucune explication de ce lot ne disait « comme en français ». Seules trois gloses françaises sont remplacées par leur équivalent espagnol, sans règle ajoutée :

- `zuInfinitivExercises#8` : « afin de » → « para ».
- `zuInfinitivExercises#9` : « sans » → « sin » ; `#10` : « au lieu de » → « en lugar de ».
- `zuInfinitivExercises#27` : lassen causatif « (faire faire) » → « (mandar hacer) ».

Rien d'ajouté sur le fait que l'espagnol rend stehen / liegen / sitzen / sein par le seul « estar » (voir doute 1).

## Doutes

1. **Verbes de position** (`praepWoWohinExercises#4` à `#49`) : « stehen », « liegen », « sein » donnent tous « está », et « stellen », « legen » donnent « pone ». La traduction ne laisse donc pas voir la différence que l'explication décrit (« de pie », « horizontal ») ; c'est l'explication qui la porte. J'ai précisé quand l'espagnol le dit naturellement : « está echado » (`#16`), « está parado » (`#30`), « está estacionado » (`#20`), « está sentado », « está colgado ».
2. `praepWoWohinExercises#23` : *Die Kinder laufen vor die Schule* → « corren hacia el frente de la escuela ». Le français (« courent devant l'école ») ne distingue pas du Dativ ; l'espagnol « corren frente a la escuela » non plus, d'où cette tournure, un peu lourde.
3. `praepWoWohinExercises#8` : *die Fensterbank* → « el alféizar de la ventana » (mot exact mais peu courant ; « el borde de la ventana » serait plus simple).
4. `praepWoWohinExercises#10`, `#11` : *der Haken* → « el gancho » ; *die Jacke* → « la chaqueta » (Mexique : aussi « la chamarra »).
5. `praepWoWohinExercises#28`, `#29` : *das Poster* → « el póster » (Colombie : « el afiche » ; Mexique : aussi « el cartel »).
6. *der Schrank* → « el armario » partout (Mexique : « el clóset », « el ropero »).
7. `praepWoWohinExercises#42`, `#43` : *ihr Freund* → « su amigo », comme le français et l'anglais ; l'allemand peut aussi vouloir dire « son petit ami ».
8. `zuInfinitivExercises#27` : *Ich lasse meine Haare schneiden* → « Me mando a cortar el pelo. » L'Amérique latine dit le plus souvent « Me corto el pelo » ou « Voy a cortarme el pelo », qui cachent le causatif ; « Me hago cortar el pelo » existe aussi.
9. `zuInfinitivExercises#20` : *Ich komme gleich essen* → « Ya vengo a comer. » (« Ya voy a comer » se lirait comme un futur).
10. `zuInfinitivExercises#12` : *Ihr dürft jetzt gehen* → « Ya pueden irse. » (ihr → ustedes).
11. `zuInfinitivExercises#45` : *Ich bitte dich, leise zu sprechen* → « Te pido que hables en voz baja. » : l'espagnol demande le subjonctif, la phrase ne montre pas d'infinitif.
12. Traductions des prépositions : *bei* → « en casa de / cerca de », *an* → « en / junto a », *in* → « en / dentro de », *über* → « encima de / sobre », *angesichts* → « ante / en vista de », *samt* → « junto con / incluido ». Le lot 06 séparait deux sens tantôt par « , », tantôt par « / » ; j'ai gardé le « / » de la source.

## Sources fautives ou à revoir

- `zuInfinitivExercises#6` : *bald anzurufen* est rendu par « rappeler bientôt » en français et « call back » en anglais ; l'allemand dit « appeler » (rappeler = zurückrufen). L'espagnol suit l'allemand : « Prometió llamar pronto. »
- `zuInfinitivExercises#47` : l'explication parle de « la règle « bleiben + zu » », qui n'existe nulle part ailleurs (la règle vue est « bleiben + verbe de position = sans zu »). Rendu par le sens : « aquí bleiben va solo…, así que «zu» se usa con normalidad ».
- `praepWoWohinExercises#0` à `#3` : topic « Prépositions » ; les 46 suivants « Verben der Position », y compris des phrases sans verbe de position (`#22`, `#23` spielen / laufen ; `#31` fahren ; `#39` steigen ; `#44` à `#46` sein, que l'explication dit décrire « une position fixe »).
- `praepWoWohinExercises#37` : l'explication dit que « legen » « décrit un déplacement », alors que les autres disent « le fait de poser quelque part » ; traduit tel quel.
- `praepReconnaissanceExercises#9` (*entlang*) : la source ne donne que l'Akkusativ postposé ; antéposé, *entlang* prend le Genitiv ou le Dativ. Rien ajouté.
- `praepReconnaissanceExercises#22` (*nahe*) et `#46` (*über*, traduit « au-dessus de » seulement, alors qu'il veut aussi dire « sur, au sujet de ») : sens partiels dans la source ; pour *über* j'ai mis « encima de / sobre ».

## À trancher

- « el carro » (retenu, consigne) dans `praepWoWohinExercises#20`, `#21`, `#31`, `#38`, `#39`.
- « el florero » pour *die Vase* (`praepWoWohinExercises#1`) : courant au Mexique et en Colombie ; « el jarrón » ailleurs.
- « el alféizar », « el póster », « el armario », « la chaqueta » : voir doutes 3 à 6.
