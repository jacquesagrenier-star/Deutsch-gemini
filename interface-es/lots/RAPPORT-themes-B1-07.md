# Rapport — thèmes B1, lot 07 (15 nov. 2026)

## Fait

- `corpus-themes-B1-07.es.json` : **240 cartes** (n 2936 à 3175) : 187 cartes `traduction` + `exemple`,
  53 verbes avec `perfekt`, `praeteritum`, `konjunktiv2`.
  Thèmes : Kapitel 4 (VHS) (3, la fin), Kapitel 5 (46), Kapitel 6 (53), Kapitel 7 (56), Kapitel 8 (45),
  Kapitel 9 (37, le début).
- Contrôle `corpus_lots.py controle` : **240 cartes, 0 faute, 1 avis** (2942 Gegenteil « lo contrario,
  el opuesto » : « lo » n'est pas vu comme un article ; gardé, c'est la forme juste).
- Doublons : aucune carte de ces six thèmes n'a encore de `traduction_es` dans `themes.json` ; comparé
  au lot B1-06 (Kapitel 4, n 2889-2935, déjà rendu) et aux mots de la source B1-08 (Kapitel 9,
  n 3176-3192, pas encore rendus). Aucune collision.

## Précisions ajoutées pour départager (même thème)

- Kapitel 5 : 2963 merkwürdig « raro, curioso » / 2967 seltsam « extraño » / 2971 ungewöhnlich
  « inusual, fuera de lo común » / 2970 üblich/unüblich « habitual/poco habitual ».
- Kapitel 6 : 3007 Notaufnahme « la sala de urgencias » / 3008 Notfall « la emergencia » ;
  3030 versorgen « atender, curar (una herida, a un enfermo) » / 3033 betreuen « cuidar, estar a cargo de » ;
  3028 stürzen « caerse (sufrir una caída) » ; 3003 Leiter « la escalera (de mano) » ;
  2997 Einnahme « la toma (de medicamentos) » (Kapitel 7, 3044 : « el ingreso (de dinero) »).
- Kapitel 7 : 3062 Steckdose « el tomacorriente, el enchufe (de pared) » / 3063 Stecker « la clavija,
  el enchufe (del cable) » ; 3052 Gras « el pasto, la hierba » / 3068 Wiese « el prado, la pradera » ;
  3057 Kuh « la vaca » / 3061 Rind « la res, el ganado vacuno » ; 3054 Hof « el patio, la granja ».
- Kapitel 9 : 3139 Annonce « el anuncio, el aviso » / 3141 Anzeige « el anuncio clasificado » ;
  3159 / 3161 « la debilidad, el punto débil » / « la fortaleza, el punto fuerte ».

## Doublon presque accepté

- 3158 Realität « la realidad » / 3171 Wirklichkeit « la realidad (lo que es de verdad) » : l'espagnol n'a
  qu'un mot ; la parenthèse ne sert qu'à départager les deux cartes. À retirer si le doublon est admis.

## Choix de temps à connaître

- Perfekt rendu au pretérito partout, sauf : 3080 (« Hemos protegido muy poco… », sens présent),
  3082 sich verabschieden et 3092 heizen (« Nos hemos despedido », « Hemos calentado ») : à la 1re personne
  du pluriel des verbes en -ar, le pretérito est identique au présent, et la carte aurait eu deux fois
  la même phrase. 3082 `exemple` et `praeteritum` restent identiques (« Nos despedimos del carro viejo »),
  de même Perfekt = Präteritum pour plusieurs verbes (2973, 2974, 2978, 3027, 3035, 3036, 3083, 3088) :
  l'allemand y dit deux fois la même chose.
- 3138 Perfekt « Ich habe mir das Leben… ganz anders vorgestellt » → imperfecto (« Me imaginaba… »), seul
  temps naturel ici.

## Doutes

- 3022 ansprechbar : le français de la carte (« abordable, disponible ») ne dit pas le sens médical de la
  phrase (un patient qui réagit quand on lui parle). Rendu « que responde (consciente), disponible para
  hablar » ; à relire par un soignant.
- 2976 leisten : trois sens dans une réponse (« lograr, rendir, permitirse (un gasto) ») ; la phrase au
  Konjunktiv II est « sich etwas leisten ».
- 3111 Kostüm « el disfraz, el traje sastre (de mujer) » : le français donne les deux sens, la phrase est le déguisement.
- 3132 total (gut) : « Fue una idea buenísima » (pas de « totalmente buena » en espagnol naturel).
- 3037 Konjunktiv II : « Si tuviera tensión muscular, pediría que me masajearan la espalda » (massieren lassen).
- 3136 Lehrer rendu « maestro » (niveau d'école inconnu).

## Sources fautives ou étranges

- 2961 gleichzeitig : « Sie spricht drei Sprachen gleichzeitig fließend » est bizarre en allemand (on ne
  parle pas trois langues « en même temps ») ; traduit tel quel. Et le mot est donné comme adjectif
  (« simultané ») alors que la phrase l'emploie en adverbe.
- 2957 allmählich : traductions fr / en adverbiales, comme la phrase ; rendu en adverbe.
- 2938 zustimmen : le français passe de « être d'accord » (présent) à « approuver » (passé) ; suivi.
- 2987 : le français de la phrase dit « La soignante », l'allemand « Die Altenpflegerin » (rendu « La cuidadora »).
- 3138 Konjunktiv II : la source est « könnte ich mir… kaum vorstellen », le français « j'imaginerais mal » ;
  suivi l'allemand (« apenas podría imaginarme »).

## À trancher (l'Amérique latine hésite)

- 3062 / 3063 prise et fiche : Mexique « el contacto / la clavija », Colombie « la toma / el enchufe » ;
  rendu « el tomacorriente » / « la clavija », avec « enchufe » précisé dans les deux.
- 3001 Impfpass « la cartilla de vacunación » (Mexique) ; Colombie « el carné de vacunas ».
- 3125 Streichholz « el fósforo, el cerillo » ; 3097 Briefmarke « la estampilla, el sello postal »
  (Mexique : « el timbre ») ; 3127 Zigarette « el cigarrillo » (Mexique : « el cigarro »).
- 3109 Ketchup « el kétchup, la salsa de tomate » (Mexique : « la cátsup »).
- 3059 Mücke « el mosquito, el zancudo » ; 3052 Gras « el pasto, la hierba » ; 3061 Rind « la res ».
- 3152 Lebenslauf « el currículum, la hoja de vida » ; 3156 Praktikum « la pasantía, las prácticas
  profesionales » ; 3166 Teilzeit « el tiempo parcial, el medio tiempo » ; 3155 Mietpreis « el precio del
  alquiler, el precio de la renta ».
- 3147 Griff « el asa, la manija » ; phrase « El asa del bolso » (Mexique : « la bolsa »).
- Soins (à relire par un soignant) : 2986-2987 Altenpfleger/in « el cuidador / la cuidadora de personas
  mayores », 2988 Altersheim « el hogar de ancianos, el asilo », 2992-2993 Arzthelfer/in « el asistente
  médico / la asistente médica », 2998 Entbindungsstation « la sala de maternidad », 3014 Schichtdienst
  « el trabajo por turnos », 3030 Pflegekraft rendu « cuidador », 3034 Pflaster « curita ».
