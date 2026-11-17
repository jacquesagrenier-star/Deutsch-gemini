# Rapport — themes B1-08 (cartes 3176 à 3415)

## Fait

- 240 cartes sur 240 (Kapitel 9 à 14 (VHS), niveau B1) : 171 noms et adjectifs (traduction + exemple),
  69 verbes (traduction + 4 phrases). Fichier : `lots/corpus-themes-B1-08.es.json`.
- Contrôle `corpus_lots.py controle` : **0 faute, 0 avis**.
- Voisins des mêmes thèmes : aucun mot de ces six chapitres n'a encore de `traduction_es` dans
  `themes.json` ; les autres cartes des Kapitel 9 et 14 sont dans les parts B1-07 et B1-09, pas encore
  rendues au moment de ce lot (voir « À surveiller » plus bas).

## Choix à connaître

- Perfekt → pretérito, sauf sens lié au présent : 3284 (*ha considerado*), 3346 (*han seguido juntos*),
  3391 (*hemos contado*), 3400 (*se ha desarrollado*).
- Präteritum → imperfecto pour un état ou une habitude, pretérito pour un fait ponctuel (le français de
  la source met souvent l'imparfait là où l'allemand raconte un fait : 3287, 3296, 3343, 3353, 3388…).
- *halten* a trois cartes, chacune dans son thème : 3246 « sostener, atajar (el balón) », 3284 « tener
  (por), considerar », 3388 « dar (un discurso) ».
- 3257 *Karriere* : « la carrera (profesional) », parce que « carrera » rend aussi *Studium* dans les
  phrases (3186, 3283) et *Rennen* (3212, autre thème).
- 3382 *behindert* : « discapacitado, con discapacidad » ; les phrases disent « personas con discapacidad ».
- 3275 *alleinerziehend* : « que cría solo a sus hijos » (pas « soltero » : on peut être séparé ou veuf).

## Doutes (à relire)

- 3197 / 3198 *Fitnesstrainer(in)* : « el entrenador físico » (aussi : *instructor de gimnasio*,
  *entrenador personal*).
- 3209 *Motorsport* : « el automovilismo, el deporte de motor » (le mot allemand couvre aussi la moto).
- 3305 *Arbeitszeugnis* : « el certificado de trabajo » ; le document allemand contient une
  appréciation, plus proche d'une *carta de recomendación*.
- 3349 *auftreten* : « presentarse, mostrarse (actuar) ».
- 3357 / 3358 *Betreuer(in)* : « el cuidador, el acompañante » — dans la phrase il s'agit d'enfants en
  excursion ; en contexte de soins, *Betreuer* est aussi le tuteur légal (rechtlicher Betreuer).
- 3399 *sich einsetzen* : « abogar (por algo), esforzarse (por algo) », choisi pour ne pas répéter
  « comprometerse » de 3393 *sich verpflichten* (même thème).
- 3407 *Car-Sharing* : « el carro compartido (carsharing) ».
- 3412 *Folie* : « el plástico para envolver, la lámina ».

## Sources fautives ou bancales

- 3301 perfekt : « Sie ist leider **durch** die Prüfung **durch**gefallen » — redondant ; l'allemand dit
  « bei der Prüfung durchgefallen » ou « durch die Prüfung gefallen ».
- 3266 : « seit Beginn ihrer Schwangerschaft im Mutterschutz » — le Mutterschutz (congé) commence six
  semaines avant la naissance ; le français « congé de maternité depuis le début de sa grossesse » est
  bancal. Rendu par « bajo la protección de la maternidad » (la protection légale, elle, vaut dès la
  grossesse).
- 3314 : « um vier Uhr », le français dit « seize heures » → « a las cuatro ».
- 3331 : « Heute Nacht », le français dit « Ce soir » → « Esta noche ».
- 3346 : « bleiben seit der Schule zusammen » — phrase peu naturelle en allemand (zusammenbleiben se dit
  plutôt d'un couple) ; traduite telle quelle.
- 3324 *Mittel* : le français donne « moyen », la phrase illustre « remède » → « el medio, el remedio ».
- 3243 *bestehen* : la traduction met « réussir (un examen) » en premier, mais les quatre phrases
  n'illustrent que « consister en ».
- 3248 : le français « sont en couple » ; l'allemand « führen eine Beziehung » → « tienen una relación ».

## Doublons acceptés

Aucun à l'intérieur d'un thème. Entre thèmes (sans conséquence pour le contrôle) : *Gemeinde* 3254 et
3414 (même mot, « el municipio »), « la carrera » (3212 *Rennen*, Kap. 10) / « la carrera (profesional) »
(3257, Kap. 11).

## À surveiller avec les parts voisines (B1-07 et B1-09)

- Kapitel 9 : *Wunsch* (3172) à côté de 3192 *sich etwas wünschen* « desear algo » ; *Stärke* (3161).
- Kapitel 14 : *Krippe* (3422) — « la guardería » est prise par 3259 *Kindertagesstätte*, mais dans le
  Kapitel 11, donc pas de conflit ; *bestehen* (3445) et *drehen* (3446) reviennent avec d'autres sens
  que 3243 / 3245 (Kap. 10).

## À trancher (l'Amérique latine hésite)

- 3223 / 3224 *Tormann, Torfrau* et les phrases 3245, 3246, 3397 : « el portero / la portera » (Mexique) ;
  Colombie et Amérique du Sud disent « el arquero / la arquera ». Le verbe « atajar » et « el penal »
  sont communs.
- 3201 *Handball* : « el balonmano » (le Cône Sud dit « el handball »).
- 3200 *Hallenbad* : « la piscina cubierta » (Mexique : « la alberca techada »).
- 3203 *Jogginghose* : « el pantalón deportivo » (Mexique : « los pants » ; Colombie : « la sudadera »).
- 3220 *Sporttasche* : « la bolsa deportiva » (Colombie : « el maletín deportivo »).
- 3225 *Trikot* : « la camiseta (de un equipo) » (Mexique : « la playera », « el jersey »).
- 3269 *Schaufenster* : « la vitrina » (Mexique : « el aparador »).
- 3301 *durchfallen* : « reprobar » (Mexique, compris partout ; Colombie : « perder el examen »).
- 3371 *Lenker* : « el manubrio » ; 3375 *Reifen* : « la llanta », *platt* → « desinflada » (neutre,
  plutôt que « ponchada » / « pinchada ») ; 3372 *Luftpumpe* : « la bomba de aire » (Colombie :
  « el inflador »).
- 3405 / 3406 *Bürgermeister(in)* : « el alcalde / la alcaldesa » (Mexique : « presidente municipal ») ;
  *Rathaus* → « el ayuntamiento » (Colombie : « la alcaldía »).
- 3249 / 3250 *Elterngeld, Elternzeit* : « el subsidio parental », « la licencia parental » (Mexique :
  « permiso ») — réalités allemandes sans équivalent exact.
- 3276 *evangelisch* : « protestante, evangélico » — en Amérique latine « evangélico » évoque les
  Églises pentecôtistes, alors que *evangelisch* désigne l'Église protestante (luthérienne) allemande ;
  la phrase dit « protestante ».
- Pour un soignant : 3304 *Altenpflege* « el cuidado de personas mayores », 3321 *Krankenpflege* « la
  enfermería », 3367 *Heim* « la residencia, el hogar », 3373 *Wirkstoff* → « principio activo »,
  3383 *Altenheim* → « hogar de ancianos ».
