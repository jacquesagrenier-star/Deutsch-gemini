# Rapport — scenes-03 (15 nov. 2026)

## Fait

- `lots/scenes-03.es.json` : **300 textes sur 300**, contrôle `scenes_textes.py controle` → **0 faute, 7 avis**.
- Scènes : flughafen (fin : questions A2-C1 et sens, 49), friseur (59), fruehstueck (59),
  geburtstag (59), heimwerken (59), hotel (début : champs, couches, questions A2, 15).
- Par groupe : 5 `alt`, 5 `consigne`, 25 titres de couches, 131 explications (`questions`), 134 `sens`.
- Les 7 avis « du français ? » sont de l'allemand cité : `je … desto` (3) et `Imperativo (du)` / `du ziehst` (4). Rien à corriger.
- Vocabulaire aligné sur le corpus déjà traduit (`lots/corpus-*.es.json`) : la mesera, el panecillo, el pastel,
  el estante, el basurero, el boleto, la báscula, el balde, el celular, el jugo, la chaqueta, el abrigo, las instrucciones.

## Explications réécrites contre l'espagnol

- `friseur¦questions¦B1 | Anna lässt sich die Haare schneiden.` — `sich` rapproché de « se ».
- `friseur¦questions¦B1 | Ich wasche mir jeden Morgen die Haare.` — ajout : l'espagnol dit « me » dans les deux cas, l'allemand distingue mir / mich.
- `fruehstueck¦questions¦B1 | Die Kellnerin bringt ihm einen Kuchen.` — le datif rapproché de « le ».
- `fruehstueck¦questions¦B1 | Der Kaffee schmeckt ihm gut.` et `geburtstag¦questions¦B1 | Das Geschenk gefällt ihm.` — « como «gustar» » (même construction en espagnol).
- `fruehstueck¦questions¦B1 | Mark dankt ihr für den Kuchen.` — « on remercie à quelqu'un » devient « como «darle las gracias» ».
- `geburtstag¦questions¦B1 | Alle gratulieren ihm zum Geburtstag.` — le piège est autre pour un hispanophone : « lo felicitan » (accusatif) contre le datif allemand ; ajout « (no ihn) ».
- `fruehstueck¦questions¦B2 | Der Tisch ist schon gedeckt.` — passif d'état = « estar » + participe.
- `fruehstueck¦questions¦B2 | Die Tür ist geöffnet.` — glose ajoutée au passif d'action : « (la abren) ».
- `heimwerken¦questions¦B2 | … um die Wand blau zu streichen.` / `… damit das Regal nicht umfällt.` — « para » + infinitif / « para que ».
- `heimwerken¦questions¦B2 | Ohne die Anleitung zu lesen…` — « sans + infinitif » → « sin + infinitivo ».
- `heimwerken¦questions¦B1 | Lass uns eine Pause machen!` — « faisons… » → « hagamos… ».
- `müssen` (flughafen, friseur, heimwerken C1) — ajout « como «debe de» » ; les `sens` C1 suivent : müssen → « debe de », könnte → « podría », dürfte → « probablemente », sollen → « Dicen que… ».
- `friseur¦couches¦B2` — « Plus… plus » → « Cuanto más… más ».

## Doutes / à trancher

- **Pinsel** (heimwerken, sens A2 et B1) : rendu « la brocha » (on peint un mur), alors que le corpus donne « el pincel ». À aligner si l'étiquette de la scène dit « el pincel ».
- **Torte / Kuchen** : les deux rendus « el pastel » (Mexique) ; la Colombie dit « torta » / « ponqué ». Le corpus a « el pastel de capas, la torta » pour Torte.
- **Eimer** : « el balde » (corpus) ; au Mexique « la cubeta ».
- **Schalter** (flughafen) : « el mostrador » (comptoir d'enregistrement), pas « la ventanilla » du corpus. **Theke** (friseur) : « el mostrador ».
- **Regal** : « el estante » partout, y compris le meuble que Mark monte (Mexique : « librero » ; « estantería » sent l'Espagne).
- `hotel¦questions¦A2 | Die Schlüssel hängen im Regal.` et `Die Klingel steht auf der Rezeption.` : explications seulement dans ma part ; « el timbre » pour la sonnette du comptoir dans l'alt (ou « la campanilla »).
- `flughafen¦sens¦C1 | Der Pilot könnte ihr Flugzeug fliegen.` : « Puede que el piloto pilotee el avión de ella » (« su avión » serait ambigu).
- `friseur¦sens¦B1 | Ich schneide mir die Haare nie selbst.` : « yo mismo » — le genre du locuteur est inconnu.
- `geburtstag¦sens¦B2 | Die Kerzen werden gleich ausgeblasen.` : passif rendu par « se van a soplar » (le passif en « ser » serait artificiel).
- `geburtstag¦sens¦B1 | Anna schenkt ihrem Freund…` : « su amigo » (Anna n'a pas de compagnon, règle des scènes).
- Titre de couche C1 « Hypothèses » → « Hipótesis » (littéral ; « Suposiciones » possible) : à harmoniser avec les autres parts.
- `friseur¦champs¦consigne` : « A Anna le están cortando el pelo. » ; alt hotel : « marrón » pour la valise (« café » prêtait à confusion avec la tasse), « ascensor » (Mexique : « elevador »).

## Sources fautives ou qui s'écartent de l'allemand

- `friseur¦sens¦A2 | Der Mann steht hinter dem Stuhl.` : le français dit « fauteuil » ; rendu « la silla » (Stuhl).
- `friseur¦sens¦A2 | Die Frau sitzt auf dem Sofa.` : le français dit « la dame » ; gardé « la señora » (l'image montre une vieille dame).
- `flughafen¦sens¦B1` (deux phrases) : le français dit « son passeport », l'allemand « den Pass » → « el pasaporte ».
- `fruehstueck¦sens¦C1 | Der Apfelkuchen…` : le français dit « tarte aux pommes », l'alt « gâteau aux pommes » ; « pastel de manzana » aux deux endroits.
- `geburtstag¦sens¦B2 | Die Freundin, deren Haare rot sind…` : le français contourne la relative (« aux cheveux roux ») ; rendu « cuyo pelo es rojo », qui montre `deren`.
- Aucune faute relevée dans l'allemand.
