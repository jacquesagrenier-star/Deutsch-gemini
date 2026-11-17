# Rapport : thèmes B1, lot 01 (15 nov. 2026)

## Fait

- `lots/corpus-themes-B1-01.es.json` : **240 cartes sur 240** (480 champs : traduction + exemple).
  Thèmes : Familie (39), Berufe (68), Essen und Trinken (61), Obst und Gemüse (20), Kleidung (18), Wohnen (34).
- Contrôle `corpus_lots.py controle` : **0 faute, 2 avis** (les deux doublons acceptés ci-dessous).
- Les mots d'Autriche et de Suisse portent la précision « (Austria) » / « (Suiza) » / « (Austria, Baviera) »,
  comme la source le fait déjà pour *Schlagobers* : 208 Coiffeur, 217 Fleischhauer, 218 Pensionist, 219 Pöstler,
  338 Glace, 341 Jause, 351 Faschiertes, 352 Müesli, 353 Poulet, 422 Erdapfel, 424 Schwammerl, 425 Marille,
  426 Rüebli. Cela distingue aussi les paires Metzger / Fleischhauer, Briefträger / Pöstler,
  Hackfleisch / Faschiertes, Hühnchen / Poulet. La source française ne porte pas ces précisions : à retirer
  si on veut suivre le français à la lettre (il y aurait alors quatre doublons de plus).

## Doublons acceptés

- 154 Anwalt / 170 Rechtsanwalt → *el abogado* : l'espagnol n'a qu'un mot.
- 295 Nachtisch / 336 Dessert → *el postre* : l'espagnol n'a qu'un mot.

## Sources fautives ou bancales

- **305 Chip** (thème Essen und Trinken) : sens « puce électronique » et phrase sur la carte de crédit, dans le
  thème de la nourriture. Rendu fidèlement (*el chip (electrónico)*) ; le mot attendu dans ce thème serait
  plutôt *die Chips* (las papas fritas de bolsa).
- **67 Nachwuchs** (thème Familie) : le français dit « relève, jeunes talents », l'anglais « offspring, young
  talent », et la phrase parle d'un club sportif. Suivi le français et la phrase (*la nueva generación, los
  jóvenes talentos*) ; le sens familial (*la descendencia, los hijos*) n'est pas rendu.
- **575 Zuhause** : la phrase allemande emploie l'adverbe « zu Hause », pas le nom « das Zuhause ».
- **323 Pfannkuchen** : le français « crêpe, beignet » mêle deux sens régionaux ; rendu par le sens de la
  phrase (*el panqueque*).
- **198 Stadtführer** : « personne ou livre » ; en espagnol le genre change (*el guía* / *la guía*), les deux
  sont donnés.
- **58 Waise** : nom féminin en allemand, phrase au masculin (« Er wurde … Waise ») ; rendu *Quedó huérfano*.

## Doutes (à relire)

- 50 Erziehung : *la crianza, la educación (de los hijos)*.
- 56 Sorgerecht : *la custodia (de los hijos)* (Mexique : aussi *la patria potestad*, qui n'est pas la même chose).
- 59 Elterngeld : *el subsidio parental* (pas d'équivalent ; *prestación parental* possible).
- 65 Mutterschutz : *la protección de la maternidad* plutôt que *licencia de maternidad*, à cause de la phrase
  (« depuis le début de la grossesse »).
- 69 Ehepaar : *el matrimonio (la pareja casada)*.
- 167 Wirt : *el dueño (de un bar o restaurante)*.
- 187 / 188 Fitnesstrainer : *el entrenador físico* (aussi *instructor de gimnasio*).
- 193 Betreuerin : *la monitora, la encargada (de un grupo)*.
- 195 Polizistin : *la policía (mujer)*.
- 196 / 197 Fachmann, Fachfrau : *el profesional, el especialista (del oficio)*, pour ne pas répéter
  181 Experte ni 206 Spezialist.
- 216 Tagesmutter : *la cuidadora de niños (en su casa)*.
- 220 Serviceangestellte : *el empleado de servicio* (calque ; en pratique un mesero).
- 328 Kloß / 343 Knödel : *la bola de masa (de papa)* / *(de pan o de papa)* — pas de mot espagnol.
- 334 Schnitzel : *la milanesa (escalope empanizado)*.
- 350 Quark : *el quark (queso fresco cremoso)*.
- 586 Obergeschoss : phrase rendue « en el primer piso alto » (voir À trancher).

## À trancher

Mots où le Mexique et la Colombie divergent, ou qu'un soignant devrait relire :

1. **165 Hebamme** : *la partera* (Mexique, Colombie) ; *matrona* (Chili, Espagne), *obstetra / obstetriz*
   (Pérou, Équateur). Métier de santé : à faire relire.
2. **174 / 175 Altenpfleger(in)** : *el cuidador / la cuidadora de personas mayores*. En Allemagne c'est un
   métier de soin diplômé ; *enfermero geriátrico* ou *auxiliar de geriatría* seraient plus proches du statut.
3. **204 Pfleger** : *el cuidador, el enfermero* — même question (Pflegefachkraft = enfermero ; Pflegehelfer = auxiliar).
4. **176 / 177 Arzthelfer(in)** : *el / la asistente médico(a)* (aussi *auxiliar de consultorio*).
5. **172 / 173 Ernährungsberater(in)** : *nutricionista* (Colombie, général) contre *nutriólogo* (Mexique).
6. **60 Elternzeit** : *la licencia parental* (Amérique) ; *permiso parental* existe aussi au Mexique.
7. **62 Kindertagesstätte / 66 Krippe** : *la guardería* / *la guardería (para bebés)* ; Colombie : *jardín
   infantil*, *sala cuna*.
8. **81 Kinderwagen** : *el cochecito de bebé* ; Mexique *la carriola*, Colombie *el coche*.
9. **161 Handwerker** : *el técnico (de un oficio manual), el artesano* — « artesano » seul évoque l'artisanat
   d'art ; le Mexique dirait aussi *el maestro*.
10. **318 Ketchup** : *el kétchup* ; Mexique *la cátsup*, Colombie *la salsa de tomate*.
11. **323 Pfannkuchen** : *el panqueque* ; Mexique *el hot cake*, Colombie *la panqueca / el pancake*.
12. **325 (phrase) et 418 (phrase)** : *pastel* pour Kuchen (Mexique) ; Colombie *torta, ponqué*.
13. **414 Rote Bete** : *la remolacha, el betabel* (les deux donnés).
14. **417 Zucchini** : *el calabacín, la calabacita* (les deux donnés).
15. **425 Marille** : *el albaricoque, el chabacano* ; *damasco* dans le Cône Sud.
16. **430 Limette** : *la lima, el limón verde* — au Mexique et en Colombie « limón » désigne déjà le citron vert.
17. **489 Reißverschluss** : *el cierre, la cremallera* ; Mexique aussi *el zíper*.
18. **494 Jogginghose** : *el pantalón deportivo* ; Mexique *los pants*, Colombie *la sudadera*.
19. **563 Abstellraum** : *la bodega, el cuarto de almacenamiento* ; Colombie *el depósito, el cuarto útil*.
20. **582 Lift / 81 (phrase)** : *el ascensor, el elevador* — *elevador* au Mexique, *ascensor* ailleurs ;
    les phrases disent *ascensor*.
21. **586 Obergeschoss** : « im ersten Obergeschoss » = premier niveau au-dessus du rez-de-chaussée ; « primer
    piso » veut dire cela au Mexique mais le rez-de-chaussée en Colombie. Rendu « primer piso alto ».
22. **587 Badewanne** : *la tina, la bañera*.
23. **555 / 557 / 573 Miete** : *la renta* dans les phrases (consigne : rentar) ; Colombie *el arriendo*.
