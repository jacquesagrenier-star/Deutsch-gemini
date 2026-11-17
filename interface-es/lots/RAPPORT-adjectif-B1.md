# Rapport : adjectifs B1 (corpus-adjectif-B1-01 et -02)

## Fait

- `corpus-adjectif-B1-01.es.json` : 240 cartes (n° 259 à 498), contrôle **0 faute**, 12 avis.
- `corpus-adjectif-B1-02.es.json` : 98 cartes (n° 499 à 596), contrôle **0 faute**, 10 avis.
- Les 22 avis sont tous des mots espagnols identiques au français ou à l'anglais
  (*responsable, flexible, liberal, individual, sensible, adaptable, digital, ideal,
  intercultural, cultural, vertical, visible, horizontal, popular, social, virtual*) : justes.
- Croisement avec les `traduction_es` des adjectifs A1 et A2 d'`adjectif.json` et entre les deux
  lots (script `adjectif-B1_doublons.py` du scratchpad, lecture seule) : **un seul doublon**, voulu
  (voir plus bas).

## Paires départagées (pour la relecture)

Mots allemands voisins, réponses rendues distinctes :

- 259 zuverlässig « confiable » / 354 verlässlich « de confianza » / 355 unzuverlässig « poco confiable »
- 327 selbstsicher « seguro de sí, con aplomo » (A2 selbstbewusst = « seguro de sí mismo »)
- 338 gelangweilt « aburrido (que se aburre) » (A2 langweilig = « aburrido »)
- 351 stur « terco » / 353 eigensinnig « obstinado, testarudo »
- 306 vernünftig « razonable » / 553 sinnvoll « sensato, que tiene sentido »
- 365 vollständig « completo, entero » / 379 komplett « completo » / 374 gesamt « total, todo el »
- 362 eben « llano, parejo » (A1 flach = « plano, llano »)
- 390 ernsthaft « serio (de verdad) » (A1 ernst = « serio »)
- 391 gleichzeitig « simultáneo, al mismo tiempo » / 417 zugleich « a la vez »
- 393 merkwürdig « extraño, peculiar » (A2 seltsam = « extraño, raro », komisch = « raro, gracioso »)
- 397 et 527 üblich « usual… » / 479 gewohnt « acostumbrado, de siempre » (A2 gewöhnlich = « común, habitual »)
- 413 total « totalmente, del todo » / 458 völlig « completamente, totalmente »
- 414 überhaupt « para nada (nada bueno) » / 475 gar « bien cocido; (gar nicht) para nada »
- 418 derzeitig « actual, de este momento » (A2 aktuell = « actual »)
- 419 engagiert « comprometido, dedicado » (A2 verlobt = « comprometido »)
- 427 kräftig « robusto, fuerte » (A2 stark = « fuerte »)
- 447 witzig « chistoso, ocurrente » (A1 lustig = « gracioso, divertido »)
- 472 fair « limpio, justo (en el juego y en el trato) » / 287 gerecht « justo, equitativo » (A2 recht = « justo, correcto »)
- 474 frisch « fresco, recién hecho » (A2 kühl = « fresco »)
- 486 korrekt « correcto, exacto » (A2 richtig = « correcto »)
- 521 weiter « otro, más » / 580 sonstig « otro, demás » / 382 zusätzlich « adicional » / 533 alternativ « alternativo »
- 260 verantwortlich « responsable » / 585 zuständig « encargado, responsable (de un trámite) » / 385 schuld (sein) « tener la culpa » / 551 schuldig « culpable »
- 550 preiswert « a buen precio, económico » / 507 sparsam « ahorrativo; económico » / 544 gratis « gratis » (A2 kostenlos = « gratuito, gratis »)
- 566 violett « violeta, morado » (A1 lila = « morado, lila »)
- 572 bereit « dispuesto, listo » (A1 fertig = « listo, terminado »)
- 541 fröhlich « alegre, jovial » / 564 vergnügt « de buen humor, risueño » (A2 froh = « contento, alegre »)
- 520 weiblich « femenino, de sexo femenino » (A2 männlich = « masculino, macho »)

## Doublons acceptés

- **589 chic = « chic, elegante »**, comme A2 *schick* : c'est le même mot dans deux graphies.
- Mêmes mots allemands repris dans une carte double (sans conflit de chaîne, mais sens repris tel quel) :
  292/394 optimistisch, 289/396 tolerant, 343/388 ängstlich, 552/406 sinnlos, 578/395 mündlich.
- 381 sämtlich « todos, la totalidad de » / 594 sämtliche « todos los, la totalidad de los » :
  même mot, deux cartes dans la source ; distinction calquée sur le français.

## Doutes (à relire)

- 398 ansprechbar : la phrase est médicale (patient qui répond après l'anesthésie), le français
  dit « abordable, disponible ». Rendu « que responde (cuando le hablan), disponible ».
- 407 wahnsinnig : « loco, tremendo (intensivo) » ; phrase rendue par « muchísima energía ».
- 430 alleinerziehend : « que cría solo a sus hijos » (pas « madre soltera », qui dit l'état civil).
- 441 ehrenamtlich : « voluntario (sin pago) ».
- 452 befristet/unbefristet : « por tiempo determinado/por tiempo indefinido » (long mais exact).
- 457 musikalisch/unmusikalisch : « dotado para la música/sin oído musical ».
- 470 eventuell : « eventual, posiblemente » (*eventual* est correct en espagnol mais soutenu).
- 591 fällig : « pagadero, que vence » ; phrase « La renta vence el día primero. »
- 588 ausgebildet : « con formación, titulado » ; « enfermera titulada ».
- 557 strafbar : phrase rendue « Eso es un delito y cuesta mucho dinero. »
- 380 mobil : phrase source étrange, rendue « Con esta app tengo movilidad financiera. »

## Sources fautives ou bancales

- 391 gleichzeitig : « Sie spricht drei Sprachen gleichzeitig fließend. » n'a guère de sens
  (parler trois langues « simultanément ») ; traduit littéralement.
- 372 fern/nah : la phrase illustre *weit* et *nah*, pas *fern*.
- 413 à 416, 414, 465, 475, 417 : *total, überhaupt, wirklich, ziemlich, bloß, gar, zugleich* sont
  des adverbes ou particules rangés dans les adjectifs ; traduits comme tels.
- 476 geehrt : la « phrase » est une formule d'appel (« Sehr geehrte Damen und Herren, ») ;
  rendue « Estimados señores y señoras: » (deux-points, usage espagnol).
- 453 : le français de la carte dit « anglophone » pour un journal ; rendu « un periódico en inglés ».

## À trancher

- 586 cool : « cool, genial » (neutre). *Chévere* (Colombie) et *padre* (Mexique) sont régionaux.
- 431 evangelisch : « protestante, evangélico ». En Amérique latine, *evangélico* évoque surtout les
  Églises pentecôtistes ; l'*evangelisch* allemand est le protestantisme luthérien. Phrase :
  « Su familia es protestante. »
- 375 reif : « plátanos » (Mexique) ; la Colombie dit *bananos*, le Cône Sud *bananas*.
- 315 qualifiziert : « calificado » (Amérique) plutôt que *cualificado* (Espagne, piste du corpus).
- 545 live : « en vivo » (Amérique) plutôt que *en directo* (piste du corpus).
- 501 et 591 Miete : « la renta », comme les lots de thèmes (Mexique) ; la Colombie dit *el arriendo*.
- 510 Schwimmbad : « piscina » (le Mexique dit *alberca*).
- 440 behindert : « con discapacidad, discapacitado » — le premier est le terme recommandé pour un soignant.
- 360 betrunken : « borracho, ebrio ».
