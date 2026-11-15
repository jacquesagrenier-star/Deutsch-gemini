# Rapport — verbe B1, part 01 (15 nov. 2026)

## Fait

- `corpus-verbe-B1-01.es.json` : **240 verbes** (n 347 à 586), 5 champs chacun (traduction + 4 phrases), soit 1 200 valeurs.
- Contrôle `corpus_lots.py controle` : **240 cartes, 0 faute, 0 avis**.
- Écrit en quatre passes de 60 verbes ; brouillons dans le scratchpad (`verbe-B1-01_p1..p4.txt`, `verbe-B1-01_assemble.py`).
- Doublons : comparaison mécanique avec les `traduction_es` des verbes A1-A2 de `verbe.json` et à l'intérieur du lot → **aucune réponse identique**.
- Temps : Perfekt → pretérito, sauf sens lié au présent (*nie*, *immer* : « Nunca he afirmado eso », « Ella siempre ha confiado en él ») ; Präteritum → pretérito pour un fait unique, imperfecto pour un état ou une habitude (le français de la source met souvent un imparfait sur un fait unique : je ne l'ai pas suivi) ; Konjunktiv II → conditionnel (« Me gustaría… » pour *würde gern*).

## Paires proches, départagées par une précision (à relire)

- 533 borgen « prestar, tomar prestado » / leihen (A2) « prestar, pedir prestado » : l'espagnol n'a qu'un mot ; seule la seconde moitié diffère.
- 372 sich bemühen « esforzarse por, procurar » / 373 sich anstrengen « esforzarse, hacer un esfuerzo ».
- 454 wagen « atreverse a, aventurarse a » / 455 sich trauen « atreverse, animarse ».
- 355 bezweifeln « dudar de, poner en duda » / 457 zweifeln « dudar (de) ».
- 426 begründen « fundamentar, argumentar » / 427 rechtfertigen « justificar ».
- 429 beweisen / 430 nachweisen / 431 belegen : « probar, demostrar » / « comprobar, demostrar (con pruebas) » / « acreditar, respaldar (con datos) ».
- 531 zurückgeben « devolver » / 532 zurückzahlen « devolver (dinero), pagar (una deuda) » / 585 erstatten « reembolsar (gastos) ».
- 403 liefern « entregar (mercancía), suministrar » / 545 zustellen « entregar a domicilio (correo, paquetes) » / abgeben (A2) « entregar ».
- 468 verpassen « perder (el autobús, una oportunidad)… » / verlieren (A2) « perder ».
- 530 umtauschen, 375 ändern, 519 tauschen, 561 schalten : tous « cambiar », chacun avec sa parenthèse (wechseln A2 = « cambiar (de algo) »).
- 549 töten « matar » / 569 umbringen « matar, asesinar » ; 438 begrüßen « saludar, dar la bienvenida » / 577 grüßen « saludar » ; 572 annehmen « aceptar, suponer » / 358 akzeptieren « aceptar ».
- 523 losen « echar a la suerte » / 524 auslosen « sortear ».

## Doutes (numéros précis)

- 362 sich auseinandersetzen : « analizar a fondo, enfrentarse a (un tema) » — pas d'équivalent pronominal naturel.
- 385 sich beschäftigen : « ocuparse en, dedicar tiempo a » (pour ne pas répéter sich kümmern « ocuparse de »).
- 475 abschneiden : rendu par « irle bien / mal a alguien » dans les phrases ; la traduction « salir (bien o mal), obtener un resultado ».
- 479 sich aneignen : « asimilar » (apropiarse de sonnait faux pour une langue).
- 481 beherzigen : « tomar muy en cuenta, seguir de corazón (un consejo) ».
- 494 necken : « hacerle bromas a, molestar (con cariño) ».
- 536 stiften, exemple : « Él dona una biblioteca » (le français dit « fonde » ; l'allemand *stiften* = financer par un don).
- 548 reichen : traduction « bastar, pasar… », mais deux phrases disent « alcanza / alcanzó » (plus naturel en Amérique ; « alcanzar » seul aurait doublé erreichen).
- 563 ablegen, 565 aufstellen, 557 aufgehen, 562 wickeln, 566 reißen, 568 abgehen : trois sens dans la traduction, parce que les quatre phrases en montrent trois.
- 377 perfekt « Wir haben uns im Stau befunden » → « Nos encontrábamos en un embotellamiento » (imparfait, comme le français).

## Sources fautives ou bancales

- 526 nachfragen, exemple : « Ich frage nach dem Ergebnis. » est *fragen nach*, pas *nachfragen* (il faudrait « Ich frage nach dem Ergebnis nach » ou « Ich frage noch einmal nach »).
- 559 blasen, exemple : « Das Kind bläst die Kerzen aus » est *ausblasen*.
- 377 sich befinden, perfekt : « Wir haben uns im Stau befunden » est peu naturel en allemand ; le français (« étions coincés ») s'en écarte.
- 480 beherrschen, perfekt : « Er hat das Handwerk beherrscht » (Perfekt d'un verbe d'état, étrange) ; 370 verfügen, perfekt : français « a fait preuve de » ≠ allemand « a disposé de » (j'ai suivi l'allemand).
- 573, 579, 584, 585, 586 : Perfekt et Präteritum de la même phrase → même phrase espagnole (pretérito), c'est voulu. 572 aussi.
- Français à l'imparfait sur un fait unique (421, 422, 423, 439-443, 468, 503 « attrapait un rhume la semaine dernière », 511-515…) : rendu au pretérito.

## À trancher (Amérique latine hésite)

- 476 durchfallen : « reprobar » (Mexique, Colombie « perder el examen », Cône Sud « reprobar / desaprobar »).
- 477 absolvieren, exemple : « Hago unas prácticas profesionales » (Mexique) ; Colombie et Argentine disent « pasantía ».
- 411, exemple : « la piscina » (Mexique : « la alberca »).
- 537 sammeln, exemple : « estampillas » (Mexique : « timbres » ; Espagne : « sellos »).
- 540 verstauen, exemple : « la cajuela » (Mexique) ; Colombie « el baúl », ailleurs « el maletero ».
- 565 aufstellen, exemple : « la carpa » (Amérique du Sud) ; Mexique « la tienda de campaña ».
- 511 explodieren, exemple : « la llanta » (Mexique, Colombie ; Cône Sud « el neumático »).
- 506 frieren, 506/562 : « la chaqueta », « la bufanda » ; Mexique dit aussi « la chamarra ».
- 534 verpachten : « arrendar » (compris partout ; Mexique dit aussi « rentar », déjà pris par mieten).
- 573 einziehen : « el apartamento » (consigne) ; Mexique « el departamento ».
- 444 befehlen : traduction « mandar, dar la orden de », phrases avec « ordenar » (plus naturel avec « a los soldados »).
