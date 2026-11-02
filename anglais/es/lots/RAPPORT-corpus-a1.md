# Rapport — cartes A1 du corpus anglais en espagnol (2 nov. 2026)

Part : les six sources `anglais/es/sources/a1-corpus-*.json`, traduites selon `anglais/es/CONSIGNES.md`
(palier 2 : Amérique latine en base, colonnes d'Espagne quand le mot ou la phrase diffère).

## Fait

| source | cartes | lots | avec une forme d'Espagne | contrôle |
|---|---|---|---|---|
| themes | 602 | `corpus-themes-01` à `-04.es.json` (151 / 151 / 151 / 149) | 106 | 0 faute, 0 avis |
| verbes | 145 | `corpus-verbes-01.es.json` | 16 | 0 faute, 0 avis |
| adjectifs | 121 | `corpus-adjectifs-01.es.json` | 12 | 0 faute, 0 avis |
| adverbes | 53 | `corpus-adverbes-01.es.json` | 3 | 0 faute, 0 avis |
| expressions | 80 | `corpus-expressions-01.es.json` | 20 | 0 faute, 0 avis |
| fonctionnels | 72 | `corpus-fonctionnels-01.es.json` | 11 | 0 faute, 0 avis |
| **total** | **1 073** | 9 fichiers | **168** | `poser.py controle` : 0 faute, 0 avis |

Ordre des id identique à la source (les lots ont été posés par un script du scratchpad qui vérifie
le mot anglais de chaque rangée contre la source ; rien d'autre que `lots/` n'a été écrit).
Les 322 `es_existant` ont été relus : repris quand ils étaient justes et neutres, passés en colonne
d'Espagne quand ils portaient un mot d'Espagne (coche, ordenador, móvil, portátil, nevera, gafas,
vaqueros, camarera, bocadillo, coge, aparco, quedamos…) ou un *pretérito perfecto* (« He perdido »,
« Han comprado », « Me he hecho daño », « se ha parado »).

## Règles que j'ai suivies (à valider)

- **Temps du passé** : Amérique latine au *pretérito indefinido* (« Perdí », « Compraron ») ; la
  colonne d'Espagne porte le *perfecto* seulement quand l'anglais est au *present perfect* ou décrit
  un fait tout récent que l'Espagne dit au perfecto (« He perdido las llaves », « ¿Qué has dicho? »,
  « He olvidado mi contraseña », « ¿Has dormido bien? »). Un passé simple anglais ordinaire
  (« He broke his arm », « My team won yesterday ») reste à l'indefinido pour les deux.
- **Cartes qui se confondraient** (même groupe, même mot espagnol) : départagées par un synonyme ou
  une précision — *name* « el nombre » / *first name* « el nombre de pila » ; *bank* « el banco » /
  *bench* « la banca, el banco (para sentarse) » ; *roof* « el tejado, el techo » / *ceiling*
  « el techo » ; *food* « la comida, los alimentos » / *meal* « la comida (desayuno, almuerzo o
  cena) » ; *storm* « la tormenta, el temporal » / *thunderstorm* « la tormenta eléctrica » ;
  *checkout* « la caja » / *cash register* « la caja registradora » ; *homework* « la tarea (escolar),
  los deberes » / *task* « la tarea, el trabajo » ; *wait* « esperar (aguardar) » / *hope* « tener
  esperanza, esperar (que pase algo) » ; *win* / *earn* ; *start* « empezar » / *begin*
  « comenzar » ; *Hello!* « ¡Hola! » / *Hi!* « ¡Hola!, ¡Qué tal! » ; *Good evening!* / *Good night!*.
- **Mots-outils** : la précision grammaticale est écrite après un tiret (« su, sus — de él »,
  « un, una — ante sonido vocálico ») et non entre parenthèses, parce que le contrôleur efface les
  parenthèses avant de comparer : *his* / *its* / *their* entre parenthèses étaient « indécidables ».
  À regarder à l'écran ; si les parenthèses sont préférées, c'est le contrôleur qu'il faudrait
  assouplir pour ces trois cartes.
- **Pas de genre pour l'usager** dans l'interface ; dans les **phrases d'exemple**, un locuteur
  genré reste quand la source l'imposait : « Estoy cansada después del viaje » (`adjectifs tired`,
  es_existant repris), « Estoy sentado en el sofá » (`verbes sit`), « Estoy muy ocupado »
  (`adjectifs busy`), « No estoy seguro » (`adjectifs sure`), « Estoy cansado porque trabajé mucho »
  (`fonctionnels because`). *Welcome!* → « ¡Bienvenido!, ¡Bienvenida! », phrase « ¡Bienvenidos a
  nuestra casa! » (des invités, pas l'usager).

## Doutes (à relire)

- `themes|home_a1|toilet` : « el sanitario, el inodoro », phrase « ¿Dónde está el baño, por favor? »
  (le mot courant est « baño », déjà pris par *bathroom*) ; Espagne « el aseo, el váter ».
- `themes|time_a1|evening` : « la tarde-noche, el anochecer » — l'espagnol n'a pas de mot ; *afternoon*
  = « la tarde », *night* = « la noche ».
- `themes|home_a1|rug` « el tapete, la alfombra » / `carpet` « la alfombra, la moqueta » : la
  distinction est faible en Amérique latine.
- `themes|home_a1|stove` : Amérique latine « la estufa » ; Espagne « la cocina (el aparato), los fogones »,
  phrase « La cocina tiene cuatro fuegos » — *kitchen* est aussi « la cocina ».
- `themes|clothes_a1|sneaker` : singulier anglais rendu au pluriel (« Estos tenis son muy ligeros »),
  « el tenis » seul étant bizarre ; Espagne « zapatillas ».
- `themes|clothes_a1|pajamas` : « la pijama, el pijama » (féminin au Mexique et en Colombie,
  masculin en Espagne et en Argentine).
- `themes|city_a1|bench` : « la banca » (Mexique, Colombie) choisi pour ne pas heurter *bank* ;
  l'Argentine et le Chili disent aussi « el banco ».
- `themes|city_a1|sidewalk` : « la acera, la vereda » (banqueta au Mexique, andén en Colombie :
  aucun mot commun à toute l'Amérique latine).
- `themes|time_a1|Thursday` « El jueves cenamos fuera » et `city_a1|factory` « fuera del pueblo » :
  « fuera » gardé (compris partout) alors que `adverbes outside` dit « afuera » en base.
- `themes|school_a1|classroom` « el aula, el salón de clases » ; `school_a1|teacher` au féminin dans la
  phrase (« La profesora explica muy bien ») pour varier avec *professor*.
- `themes|freetime_a1|competition` : « la competencia » en base (Amérique latine), « la competición »
  en Espagne.
- `verbes|A1|watch` : « observar, ver (la tele, un partido) », phrase « Los niños observan a los
  jugadores » — pour ne pas répéter *see* « ver » et *look* « mirar ».
- `verbes|A1|meet` : base « reunirse con, encontrarse con, conocer » ; Espagne « quedar con » et
  « He quedado con mis amigos ».
- `verbes|A1|become` : « Voy a hacerme profesor » (locuteur masculin, comme la source).
- `verbes|A1|carry` : base « cargar, llevar (algo pesado) » ; en Espagne « cargar » veut dire charger,
  d'où la colonne « llevar ».
- `adjectifs|A1|narrow` : « El callejón es estrecho y apretado » (la source dit deux fois la même chose).
- `adjectifs|A1|light` : « ligero, liviano, claro (color) » — « liviano » est le mot courant en
  Amérique latine, « ligero » est compris partout.
- `adverbes|A1|straight ahead` : base « derecho, todo recto » (« Siga derecho ») ; Espagne « todo recto ».
- `expressions Good evening! / Good night!` : « ¡Buenas tardes!, ¡Buenas noches! (al llegar) » /
  « ¡Buenas noches!, ¡Que descanses! (al despedirse) ».
- `expressions I'm in!` : base « ¡Cuenta conmigo!, ¡Me sumo! » ; Espagne « ¡Me apunto! ».
- `expressions How nice!` : base « ¡Qué lindo!, ¡Qué amable! » ; Espagne « ¡Qué bonito!, ¡Qué detalle! ».
- `fonctionnels|pronomen|it` : « ello, eso — una cosa o un animal; a menudo no se traduce » (long pour
  une carte).
- `fonctionnels|pronomen|which` : « cuál, cuáles — entre varios », mais la phrase dit « ¿Qué color te
  gusta? » (l'Espagne dit « qué », l'Amérique latine accepte « cuál color »).
- `fonctionnels|pronomen|him` : « lo, le, él », phrase « Lo veo todos los días » ; pas de colonne pour
  le leísmo de Madrid (« Le veo »).

## Sources qui me semblent fautives

- `expressions|A1|How do you say… in English?` : la phrase **anglaise** contient un mot français,
  « How do you say « pomme » in English? ». Pour un hispanophone il faudrait « manzana » (ma
  traduction dit «manzana») ; à corriger dans la source anglaise, que je n'ai pas touchée.
- `themes|work_a1|desk` : la phrase (« The desk is at the far end », ex_fr « Le comptoir »,
  es_existant « El mostrador ») parle d'un comptoir, pas du meuble *desk*. Traduit « el escritorio »
  / « El escritorio está al fondo ».
- `themes|clothes_a1|purse` : fr « le sac à main » mais ex_fr « Mon porte-monnaie est resté dans le
  bus ». Traduit comme sac à main (« la cartera, el bolso »).
- `themes|home_a1|room` : fr « la pièce », ex_fr « Ma chambre » ; `freetime_a1|gym` : fr « la salle de
  sport », phrase « PE class is in the gym » (gymnase). Sens suivi : la phrase anglaise.
- `verbes|A1|let` : es_existant « Te presento a mi hermana » perd *let* ; écrit « Déjame presentarte a
  mi hermana ».
- `shopping_a1|cash register` : « The cashier is at the cash register » — tautologie, gardée.

## À trancher (Espagne ≠ Amérique latine)

Toutes ces cartes portent déjà les deux formes dans les lots (colonnes 3-4) ; voici les paires.

**Mots**
- el carro, el auto / el coche — `travel_a1|car`, et les phrases de `home_a1|garage`,
  `travel_a1|gas`, `feelings_a1|problem`, `adjectifs expensive`, `adjectifs American`,
  `fonctionnels my`, `verbes park`.
- la computadora / el ordenador — `work_a1|computer`, `verbes save` ; la computadora portátil, la laptop /
  el portátil — `tech_a1|laptop`.
- el celular / el móvil — `tech_a1|cell phone`, `verbes use`.
- el jugo / el zumo — `food_a1|juice`, `fonctionnels or`.
- manejar / conducir — `verbes drive`, `travel_a1|driver` ; la licencia de conducir / el carnet de conducir.
- el departamento / el piso — `home_a1|apartment`, `verbes rent` (rentar / alquilar) ;
  el piso (étage) / la planta — `home_a1|floor`.
- la papa / la patata ; el boleto / el billete ; el pastel / la tarta (`cake`, et les phrases de
  `grandmother`, `butter`, `oven`, `bring`, `good`, `sweet`, `piece`) ; el sándwich / el bocadillo
  (`sandwich`, `ham`) ; el almuerzo / la comida (`lunch`) ; los dulces / los caramelos, las golosinas ;
  el hongo / la seta ; el pimiento, el pimentón / el pimiento ; el tazón / el bol, el cuenco.
- el refrigerador / la nevera (`fridge`, `fruit`, `no`) ; la estufa / la cocina ; el clóset / el armario ;
  el estante / la estantería ; la cobija / la manta ; la tina / la bañera ; el sanitario / el aseo, el váter ;
  la llave del agua / el grifo ; la sala / el salón ; el ascensor, el elevador / el ascensor ;
  el alquiler, la renta / el alquiler ; la alfombra / la moqueta.
- el mesero, la mesera / el camarero, la camarera (et `adjectifs kind`) ; el menú / la carta
  (`menu`, `Can I have…?`) ; el pedido, la orden / el pedido ; la reservación / la reserva ;
  ordenar (en un restaurante) / pedir.
- la curita / la tirita ; el suéter / el jersey ; los jeans / los vaqueros ; los shorts / el pantalón
  corto ; el tenis / la zapatilla deportiva ; la cartera / el bolso (`purse`, et les phrases de
  `bag`-`How much is it?`, `this`, `yours`, `in`, `adjectifs light`) ; los lentes / las gafas ;
  los lentes de sol / las gafas de sol ; la pijama / el pijama.
- la alcaldía, la municipalidad / el ayuntamiento ; el correo / la oficina de correos ;
  el estacionamiento / el aparcamiento ; la gasolinera, la estación de servicio / la gasolinera ;
  la banca / el banco ; la acera, la vereda / la acera ; el zoológico / el zoo ; el embotellamiento /
  el atasco ; el pasto / la hierba, el césped ; el día feriado / el día festivo.
- las compras / la compra (`shopping`, `supermarket`, `list`, `verbes shop`) ; la promoción, el
  descuento / las rebajas, la oferta ; el vendedor / el dependiente ; el recibo, el ticket / el ticket ;
  la escuela / el colegio (`school`, `long`, `pick up`, `their`, `to`) ; el pizarrón / la pizarra ;
  el borrador / la goma de borrar ; la tarea / los deberes (`homework`, `verbes do`) ; la materia /
  la asignatura ; tomar un curso / hacer un curso ; el bolígrafo, la pluma / el bolígrafo, el boli.
- el pasatiempo / la afición ; el básquetbol / el baloncesto ; la competencia / la competición ;
  el video / el vídeo ; internet, el internet / internet ; el control remoto / el mando a distancia ;
  el enojo / el enfado ; enojado / enfadado ; el pedazo / el trozo ; afuera / fuera ; adentro / dentro ;
  derecho / todo recto ; marrón, café / marrón ; roto, descompuesto / roto, estropeado ;
  amigable, cordial / amable, simpático ; el esposo / el marido ; la esposa / la mujer.
- empacar / hacer la maleta ; estacionar / aparcar ; andar en bici / montar en bici (`bike`, `ride`) ;
  reunirse con / quedar con ; cargar / llevar ; tomar / coger (`take`, `towel`, `umbrella`, `taxi`).
- Tomar una foto / hacer una foto ; Está bien / Vale ; ¡Chao! / ¡Adiós! ; Disculpe / Perdone ;
  ¡Buen provecho! / ¡Que aproveche! ; ¡Felicidades! / ¡Enhorabuena! ; Tengo ganas de… / Me apetece… ;
  ¡Cuenta conmigo! / ¡Me apunto! ; ¡Qué lindo! / ¡Qué detalle!.

**Grammaire**
- ustedes / vosotros : `fonctionnels you` (colonne 3) et la phrase de `school_a1|page`
  (« Abran el libro » / « Abrid el libro »).
- indefinido / perfecto (voir « Règles ») : `key`, `furniture`, `finger`, `knee`, `watch`, `year`,
  `ticket`, `message`, `password`, `verbes say`, `adjectifs new`, `Good morning!`, `Can you repeat…?`,
  `Never mind.`, `I'm glad.`, `Let's take a break.`, `Congratulations!`, `How nice!`, `because`.
- « Nos vemos » / « Quedamos » : `city_a1|square`, `OK.`, `At what time?`.

**Reste indécis à l'intérieur de l'Amérique latine** (une seule forme écrite, la plus large) : el
plátano, la banana (banano, cambur) ; la fresa (frutilla) ; los lentes (anteojos) ; la cobija (frazada) ;
el calcetín, la media ; el tenis (zapatillas) ; la sartén (el sartén) ; el autobús (camión, colectivo,
micro, guagua) ; el pizarrón (tablero) ; el bolígrafo (lapicera, lapicero, esfero) ; la banca ;
la acera (banqueta, vereda, andén) ; la gripe (gripa) ; la chaqueta (chamarra, campera) ; « Ando en
bicicleta » (Mexique, Chili) plutôt que « Monto ».

**Nombres décimaux** : aucun dans ces six sources (« un euro con cincuenta » est écrit en lettres).
