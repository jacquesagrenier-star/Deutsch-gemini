# Rapport — scenes-10 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/scenes-10.json`, 300 textes ; rendu : `interface-es/lots/scenes-10.es.json`, 300 clés.
- Scènes : untersuchung (18 sens, fin de la scène), waschsalon (59), weihnachtsmarkt (59), winter (59),
  wohnzimmer (67), zug (38 : champs, couches, questions, et les 5 premiers sens A2).
- Par groupe : 10 champs (5 alt, 5 consignes), 25 titres de couche, 134 explications, 131 sens.
- Contrôle `scenes_textes.py controle` : **0 faute**, 1 avis (« du » dans `waschsalon¦questions¦B1 | Lass mich dir helfen!` :
  c'est le pronom allemand cité, « Imperativo de lassen (du) », gardé exprès).
- Script de construction : `scenes-10_construire.py` (scratchpad) ; les textes y sont rangés dans l'ordre de la source.

## Harmonisation

- Titres repris de `scenes-01.es.json` et des lots 01 à 06 : « Sustantivos y artículos », « Wo? — las preposiciones »,
  « Suposiciones », « Relativas y pasiva », « Relativas y pasiva de estado », « Wo? o Wohin? … ».
- Titres neufs : « El verbo lassen », « Los participios usados como adjetivos », « Los pronombres personales: ihn, ihm, sie, ihr »,
  « Las palabras compuestas: der Weihnachtsmarkt, die Lichterkette », « El dativo: mir ist kalt », « Wo? o Wohin? — Mark ordena »,
  « Wo? o Wohin? de viaje ».
- Cas : la source dit « datif / accusatif » → « dativo / acusativo ». « subjonctif II » (wohnzimmer C1) → « Konjunktiv II »,
  comme dans les lots 01 à 04.
- Formules reprises mot pour mot des lots précédents : könnte, dürfte, sollen (« según lo que se dice… »), über = encima de,
  vor = delante de, hinter = detrás de, neben = al lado de, « Sujeto de la relativa », « Pasiva con un verbo modal ».
  Pour müssen, les lots précédents ont deux variantes ; j'ai pris partout « deducción casi segura, como «debe de» ».

## Explications réécrites contre l'espagnol (clés)

- `waschsalon¦questions¦B1 | Anna lässt die Waschmaschine laufen.` — « faire faire » n'existe pas tel quel : « dejar o hacer que algo se haga ».
- `waschsalon¦questions¦B1 | Lasst uns nach Hause gehen!` — « allons… ! » → « ¡vamos a…! ».
- `waschsalon¦questions¦B2 | Die laufende Waschmaschine ist laut.` et `… | Die lesende Frau sitzt auf der Bank.` — l'espagnol n'a pas de
  participe présent adjectif : ajout de « que está funcionando », « que lee ».
- `waschsalon¦questions¦B2 | Der gefaltete Pullover liegt auf dem Tisch.` — ajout de « como «doblado» ».
- `weihnachtsmarkt¦questions¦B1 | Mark kauft ihn.` et `… | Die Mutter hat sie gekauft.` — le genre diffère de l'espagnol
  (der Stern / la estrella, die Brezel / el pretzel) : une phrase le dit, sinon le sens espagnol (« la compra », « lo compró ») contredit le pronom.
- `weihnachtsmarkt¦questions¦B1 | Die Brezeln schmecken ihr.` — « como «gustarle» » (même construction qu'en espagnol).
- `weihnachtsmarkt¦questions¦B2 | Der Markt zu Weihnachten ist der Weihnachtsmarkt.` — ajout de « Al revés que en español ».
- `winter¦questions¦B1 | Ihr ist kalt.` et `… | Der Hund trägt einen Mantel, damit ihm nicht kalt ist.` — « tener frío » ne se dit pas avec haben :
  la personne au datif.
- `winter¦questions¦B1 | Die Mütze steht ihr gut.` — « como «le queda bien» » ; `… | Die Stiefel gehören ihr.` — « como «pertenecerle» ».
- `winter¦questions¦B2 | Der Hund, dessen Mantel rot ist…`, `zug¦questions¦B2 | Das Dorf, dessen Kirche…`, `zug¦… | Die Zeitung, deren Fotos…`,
  `wohnzimmer¦questions¦B2 | Die Katze, deren Kopf…` — « dont » → « cuyo », avec la mise en garde des lots précédents
  (dessen / deren s'accordent avec le possesseur, « cuyo » avec la chose possédée).
- `winter¦questions¦B2 | Das Auto ist mit Schnee bedeckt.`, `wohnzimmer¦questions¦B2 | Die Tür ist geöffnet.`,
  `zug¦questions¦B2 | Der Kaffee ist noch nicht getrunken.` — le passif d'état rapproché de « estar » + participe.
- `wohnzimmer¦questions¦B1 | Mark legt den Ball in den Schrank.` et `… | Mark stellt die Tasse auf das Regal.` — l'espagnol n'a que « poner » :
  « poner acostado » / « poner de pie ».
- `wohnzimmer¦questions¦C1 | Die Party muss sehr lang gewesen sein.` — « como «debe de haber sido» » ; `… | Hätte Mark die Party nicht verpasst…` — « como «estaría» ».

## Doutes / à trancher

- **Waschsalon** : « lavandería de autoservicio » (alt, consigne), « la lavandería » dans le sens C1. Le Mexique dit aussi « lavandería de monedas ».
- **Jeans** : « los jeans » (pluriel en espagnol, die Jeans singulier en allemand) ; le Mexique dit aussi « pantalón de mezclilla ».
- **Calcetín / calcetines** (la Colombie dit « medias »), **suéter**, **cobija**, **banca**, **tenis** (Turnschuhe), **cubeta** (Eimer ; Colombie : « balde »),
  **pecera** pour « das Glas mit dem Goldfisch », **mesa de centro** (Couchtisch), **lámpara de pie** (Stehlampe).
- **Pretzel** : « el pretzel / los pretzels » ; à aligner sur le corpus si celui-ci a choisi autre chose (« el brezel »).
- **Weihnachtsmarkt** : « mercado navideño » dans les textes, « mercado de Navidad » dans le sens B2 qui décompose le mot.
- **Lichterkette** : « guirnalda de luces » (Mexique : « serie de luces »).
- **Hausärztin** : « médica de cabecera » ; « Ärztin » rendu par « la doctora » (usage courant) — à aligner sur le début de la scène untersuchung (lot 09).
- **Unterhose** : « calzoncillos ».
- `winter¦sens¦B1 | Anna gibt dem Schneemann eine Karotte als Nase.` — « le pone… una zanahoria como nariz » (poner plutôt que dar, plus naturel).
- `winter¦sens¦B2 | Der Weg muss noch gefegt werden.` — rendu actif : « Todavía hay que barrer el camino. »
- `untersuchung¦sens¦C1 | Er muss viel Sport treiben.` — lu comme une supposition (couche C1) : « Debe de hacer mucho deporte », le français « Il doit » est ambigu.
- `zug¦champs¦alt` : « Laptop » → « computadora » dans l'alt, « computadora portátil » dans le sens A2.

## Sources fautives ou à regarder

- `weihnachtsmarkt¦sens¦A2 | Die Puppe hängt am Stand.` : le français dit « stand », les autres phrases « étal » pour le même Stand ; rendu partout « puesto ».
- `weihnachtsmarkt¦sens¦C1 | Der Stern könnte…`, `waschsalon¦sens¦C1 | Das Mädchen könnte…` : le français dit « peut-être » ; j'ai suivi l'allemand (« podría »).
- `winter¦sens¦B2 | Der Hund, dessen Mantel rot ist…` : le français simplifie (« au manteau rouge ») ; j'ai gardé la relative (« cuyo abrigo es rojo »),
  puisque la question porte sur dessen.
- `wohnzimmer¦sens¦B1 | Mark legt den Ball in den Schrank.` : l'allemand dit **in** den Schrank (« mete la pelota en el armario »), alors que la phrase
  d'avant dit **auf** dem Schrank ; conforme au français, rien à corriger.
- Aucune faute relevée dans l'allemand.
