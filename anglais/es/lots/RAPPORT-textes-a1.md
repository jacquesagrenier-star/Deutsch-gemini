# Rapport — textes A1 en espagnol (2 nov. 2026)

Part : `sources/a1-textes.json`, les 1 662 textes hors corpus du palier A1 (Premiers pas,
A1 voyage, repères, prononciation, conjugaison, fiches de grammaire, tuiles, séries par temps),
rendus en espagnol **neutre** selon `anglais/es/CONSIGNES.md` (palier 2 compris).

## Fait

| fichier | entrées (indices de la source) | contrôle |
|---|---|---|
| `lots/textes-01.es.json` | 350 (0-349) : Premiers pas, escales 1 à 5 | 0 faute |
| `lots/textes-02.es.json` | 350 (350-699) : fin des Premiers pas, A1 voyage jusqu'à la santé | 0 faute |
| `lots/textes-03.es.json` | 350 (700-1049) : fin de l'A1 voyage, nombres 0-13 | 0 faute |
| `lots/textes-04.es.json` | 350 (1050-1399) : repères, prononciation, conjugaison, titres des fiches | 0 faute |
| `lots/textes-05.es.json` | 262 (1400-1661) : les 15 fiches A1, 76 tuiles, 2 séries par temps | 0 faute |

`poser_textes.py controle textes` : **1 662 traduits sur 1 662, 0 faute, 2 avis**. Les deux avis
(« mot francais « est » ») visent `the -est` anglais dans `a1-voyage|Adjectif court…` et
`grammaire|adjectifs|regle` : faux positifs, rien à changer.

Ordre des id identique à la source (les lots sont écrits par un script qui recopie les id depuis
la source par indice ; les traductions ont été pensées avec l'anglais d'origine sous les yeux,
retrouvé dans `anglais/datos/*.json`, et non depuis le seul français).

Un contrôle de plus, propre à ces textes : dans les quiz des Premiers pas (bonne réponse + deux
leurres) et les variantes des blocs de l'A1 voyage, les traductions espagnoles d'un même groupe
restent distinctes — **un seul doublon, qui vient de la source** (voir « Sources fautives »).

## Choix récurrents

- **Registre** : « vous » du français → **usted** dans les phrases dites à un inconnu (hôtel,
  café, pharmacie : « ¿Puede repetir? », « ¿Tiene wifi? ») ; « tu » → tú (fête, amis). Pluriel :
  ustedes (« ¿Están listos para pedir? »). Jamais vosotros (vérifié par grep).
- **Je voudrais** → « Quisiera » ; **Est-ce que je peux avoir… / Can I have…** → « ¿Me da…? » ;
  **Je prends celui-ci / I'll take this one** → « Me llevo este. » ; **Je vais prendre… /
  I'll have the…** → « Voy a pedir… » (évite « tomar », qui ne vaut que pour les boissons en
  Amérique latine) ; **Voilà, tenez / Here you go** → « Aquí tiene. » ; **Enchanté** →
  « Mucho gusto. » (épicène) ; **Je suis perdu** → « Me perdí. » (épicène).
- **Présent en -ing** : rendu par « estar + gerundio » (« estoy comiendo », « está lloviendo »),
  et non par le présent simple + « (en ce moment) » du français, puisque l'espagnol a la forme.
- **Passé** : pretérito indefinido partout (« perdí », « visité », « ¿Desayunaste? »).
- **Premiers pas, groupes de quiz** : les leurres (`l`) n'ont pas d'anglais ; traduits depuis le
  français en gardant l'écart voulu avec la bonne réponse (« Hola, me llamo Marie. » / « Adiós,
  me llamo Marie. » / « Hola, ¿te llamas Marie? »).
- **Blocs à trous de l'A1 voyage** (« Le … ne marche pas. », « Mon … a été annulé. ») : quand
  l'article dépend du genre du mot à insérer, le patron espagnol s'en passe (« … no funciona. »,
  « … está roto. ») ou passe à l'impersonnel (« Cancelaron mi …. »).
- **Repères, prononciation figurée** : refaite en orthographe espagnole, majuscules sur la
  syllabe accentuée comme la source, [θ] entre crochets (SI-rou, UAN, TU, [θ]RI, FOR, FAIV, SIKS,
  SE-ven, EIT, NAIN, TEN, i-LE-ven, TUELV, [θ]er-TIN… TUEN-ti, [θ]ER-di, FOR-di… uan JAN-drid,
  uan [θ]AU-sand). Le **h** de hundred est écrit **J** (« JAN-drid ») : un h espagnol serait muet,
  et la règle `house, hello` dit que le son est plus doux que la j. À relire par un natif.
- **Heures des repères** : « 1 h » → « la una », « 2 h » → « las dos »… ; « Il est 7 h 30. » →
  « Son las 7:30. ».
- **Glossaire suivi** : repères → « Lo básico » (cité dans `a1-voyage|Les dates américaines…`),
  M'ENTRAÎNER → « PRACTICAR », fiche → ficha, cartes → tarjetas, Dictée → Dictado. Noms anglais
  des temps gardés (« El present simple », « El past simple », « Present continuous ») ; la fiche
  « Le présent en -ing » devient « El presente en -ing » (descriptif, comme le français).
- **Prétérit** → « past simple » partout (titres des fiches, A1 voyage « Ayer: el past simple »).

## Écrit CONTRE l'espagnol (ids à relire)

Comparaisons avec l'espagnol ajoutées, ou comparaisons françaises remplacées :

- `premiers-pas|À l'oral, on contracte presque toujours…` — « Un solo verbo para ser y estar ».
- `premiers-pas|On dit le prix en dollars et en cents…` — « En inglés, el punto separa los centavos » (sans « pas la virgule »).
- `a1-voyage|There is devant un singulier…` et `grammaire|there-is|regle` — deux formes pour « hay ».
- `a1-voyage|Deux façons de dire « j'ai mal »…` — la partie du corps sujet, comme en espagnol.
- `a1-voyage|Pour l'âge, on EST…` — « (no «tengo») ».
- `a1-voyage|Le temps passe toujours par it…` — « nunca «is raining»: en inglés el sujeto es obligatorio ».
- `a1-voyage|On pour une surface…` et `grammaire|prepositions|regle` — « donde el español dice «en» para todo, el inglés distingue ».
- `a1-voyage|Some dans les phrases affirmatives…` — « el español no pone nada (quisiera pan = I'd like some bread) ».
- `a1-voyage|Après like, love, hate…` — « Con like, la persona es el sujeto: I like dogs (me gustan los perros) ».
- `a1-voyage|Be + -ing pour ce qui se passe maintenant…` et `conjugaison|Be + verbe en -ing…` — « como «estar + -ando / -iendo» ».
- `a1-voyage|This / these pour ce qui est près de moi…` — « (este / ese) ».
- `reperes|Toujours une majuscule : Monday…` — « (en español, con minúscula) ».
- `reperes|Hundred et thousand ne prennent jamais de s…` — « (en español sí: doscientos) ».
- `reperes|Les couleurs ne s'accordent jamais…` — « (ni femenino ni plural) ».
- `prononciation|Le français n'a qu'un i…` — « El español tiene una sola i ».
- `prononciation|La lettre a se lit de trois façons…` — « entre «a» y «e» » (le français disait « è »).
- `prononciation|Le son [ʌ] est un « eu » bref…` — réécrit : « una a breve, con la boca apenas abierta, entre «a» y «o» … Nunca la u del español: bus no se dice «bus» ».
- `prononciation|Dans une syllabe sans accent…` — « El español, que pronuncia todas sus vocales por igual, no lo tiene ».
- `prononciation|Beaucoup de voyelles anglaises glissent…` — « Una «o» corta y redonda como la del español suena extranjera ».
- `prononciation|Le th de three…` — « es la z de España (zapato). En Latinoamérica no existe: hay que fabricarla. Ni «t» ni «s» ni «f»: three ≠ tree ≠ free » (le français opposait à « sri »).
- `prononciation|Même position de la langue, mais la gorge vibre…` — « Es la d suave de «nada» o «todo», pero al principio de la palabra ».
- `prononciation|Le h anglais s'entend…` — « más suave que la j del español ».
- `prononciation|Le r anglais ne se fait pas dans la gorge…` — « ni la r de «pero» ni la rr de «perro» ».
- `prononciation|Le w est un « ou » très bref…` — « Nunca una «g» («guáter») ni una «b» » (le français disait « jamais un v »).
- `prononciation|En américain, un t entre deux voyelles…` — « como una d suave o la r de «cara» ».
- `prononciation|Le -s du pluriel et de la 3ᵉ personne…` — [z] : « una s con la garganta vibrando, como el zumbido de una abeja ».
- `prononciation|Chaque mot a une syllabe plus forte…` — « No sigue las reglas del español » (le français : « pas toujours à la fin, comme en français »).
- `conjugaison|À l'oral, toujours contracté…` — « Un solo verbo para ser y estar ».
- `grammaire|be|regle` — « (ser y estar: un solo verbo para los dos) ».
- `grammaire|articles|regle` — « donde el español pone «el» o «la» » ; `grammaire|articles|attention` — « aunque en español se diga «es médica», sin artículo ».
- `grammaire|pluriel|attention` — « «la gente» (singular en español, plural en inglés) ».
- `grammaire|present-simple|regle` et `grammaire|questions|regle` — « En español basta la entonación (¿hablas inglés?); en inglés hace falta do ».
- `grammaire|pronoms|attention` — « El tropiezo del hispanohablante: «su» se dice his… » (le français disait « le piège des francophones »).
- `grammaire|there-is|attention` — « «Hace dos días» no se dice con there ».
- `grammaire|can|attention` — « «Sé nadar» se dice I can swim, no I know swim ».
- `grammaire|adjectifs|regle` — « al revés del español ».
- `grammaire|faux-amis|resume`, `regle`, `attention`, `tableau|0..7` — la fiche entière réorientée :
  library ≠ librería, actually ≠ actualmente, to attend ≠ atender, + embarrassed, exit, carpet dans
  la règle ; `tableau|6` « descansar (restar = to subtract) » ; `tableau|3` « a car » et `tableau|5`
  « a journey » ne trompent pas un hispanophone : simple sens (« un carro, un coche », « un viaje »).
- `grammaire|nombres|attention` — « (doscientos, pero two hundred) ».
- `temps|temps-present-continuous|texte` — « El español dice «estoy cocinando» o, a veces, el presente simple ».
- `grammaire-textes|pron_intro` — « los sonidos que más cuestan a un hispanohablante ».

## Doutes (à relire)

- `premiers-pas|salut` → « hola (informal) » et `premiers-pas|bonsoir` → « buenas noches (al llegar) » :
  hello / hi / good evening n'ont pas trois mots espagnols distincts.
- `premiers-pas|Comment allez-vous ?` → « ¿Cómo está usted? » (How are you?, pour le distinguer
  de « ¿Cómo estás? » de `Salut ! Comment ça va ?`).
- `premiers-pas|Voilà, tenez.` et `a1-voyage|Voilà. À quelle heure…` → « Aquí tiene. ».
- `premiers-pas|la station, la gare` → « la estación » ; `premiers-pas|je peux, je sais` → « puedo, sé ».
- `premiers-pas|en retard` → « tarde, con retraso » ; `premiers-pas|Le bus est en retard.` →
  « El autobús viene con retraso. » ; `a1-voyage|mon vol était en retard` → « mi vuelo venía con retraso ».
- `premiers-pas|C'est tout droit.` → « Es todo derecho. » ; `premiers-pas|tout droit` → « derecho, todo recto » (les deux formes dans la case).
- `premiers-pas|Au secours !` → « ¡Ayuda! » (Help!), pas « ¡Socorro! ».
- `premiers-pas|Je regarde seulement.` → « Solo estoy mirando. ».
- `a1-voyage|Je voudrais une miche de pain…` → « Quisiera un pan, por favor. » (a loaf of bread ; « hogaza » est rare en Amérique).
- `a1-voyage|Quatre dollars la barquette…` → « Cuatro dólares la caja. » (a box).
- `a1-voyage|Il fait beau et chaud, environ vingt-sept degrés.` : l'anglais dit « about eighty degrees » (Fahrenheit) ; j'ai suivi le français (« unos veintisiete grados »).
- `a1-voyage|L'eau est chaude ?` → « ¿El agua está tibia? » (Is the water warm?).
- `a1-voyage|Combien de temps dure le séchage ?` → « ¿Cuánto tarda el secado? » (the dryer).
- `a1-voyage|Rencontrer des gens, être invité` → « Conocer gente, recibir una invitación ».
- `a1-voyage|La famille et les proches` → « La familia y los seres queridos ».
- `a1-voyage|Du, de la : some, any` → « Algo de, un poco de: some, any ».
- `a1-voyage|Aimer faire : I like + -ing` → « Me gusta hacer: I like + -ing ».
- `a1-voyage|je prends celui-ci`, `Je prends le bleu.` → « me llevo este », « Me llevo el azul. ».
- `premiers-pas|Se débrouiller et bavarder…` → « Desenvolverse y charlar: pedir que repitan, la hora, el tiempo ».
- `reperes|1 h`… → « la una », « las dos » (en mots, pas « 1:00 »).
- `reperes|ouann HEUN-drid` et les centaines : le h écrit « J » (voir plus haut).
- `prononciation-mot|about|à propos de` → « sobre, acerca de » ; `prononciation-mot|wrong|faux` → « equivocado, incorrecto » ;
  `prononciation-mot|home|la maison` → « la casa, el hogar » (house → « la casa »).
- `conjugaison|il · elle est rentré(e)` → « él · ella volvió a casa » ; `conjugaison|ils ont déjeuné` → « almorzaron ».
- `grammaire|questions|tableau|0` « What » → « qué, cuál » ; `grammaire|pronoms|tableau|0` → « yo · me, mí · mi ».
- `grammaire|this-that|resume` → « Este, ese, estos — cerca o lejos ».
- `grammaire-textes|kicker_cliveesEnExercises` → « Oraciones escindidas » ; `kicker_participialesEnExercises` →
  « Oraciones de participio » ; `kicker_discoursIndirectEnExercises` → « Estilo indirecto » ;
  `kicker_adverbesFamilleEnExercises` → « Los tipos de adverbios » (et `tuiles|adverbien|adverbes-famille|titre` → « Identificar el tipo »).
- `tuiles|konjunktionen|vocab-startPartikelnVokabular|titre` « mots de l'oral » → « palabras del habla ».
- **Genre** : la source est au masculin et je l'ai suivie quand aucune forme épicène n'existe :
  `premiers-pas|Je suis malade.` « Estoy enfermo. », `Je suis fatigué aujourd'hui.` « Hoy estoy cansado. »,
  `Je suis allergique aux noix.` « Soy alérgico a las nueces. », `fatigué`, `malade`, `conjugaison|j'étais fatigué`
  « estaba cansado », `a1-voyage|Non, mais je me sens très fatigué.`, `Je suis allergique ….` et ses trois variantes,
  `Bonjour, je suis votre nouveau ….` et ses variantes (« su nuevo vecino / inquilino / compañero »).
  `Salut ! Je suis Jake. Tu es une amie d'Emma ?` → « ¿Eres amiga de Emma? » (Marie, comme la source).
  « ¡Bienvenidos a Boston! » au pluriel, comme un panneau.

## Sources qui me semblent fautives

Patrons à trous de l'A1 voyage remplis sans accord ni élision (le français affiché est cassé ;
l'anglais, lui, est juste) — traduits correctement :
- `a1-voyage|Ce bus va à à Harvard Square ?`, `…à au centre-ville ?`, `…à à l'aéroport ?` (« à à », « à au »).
- `a1-voyage|Le le chauffage ne marche pas.`, `Le la douche ne marche pas.`, `Le le wifi ne marche pas.`.
- `a1-voyage|Mon ma réservation a été annulé.` (« Mon ma », et « annulé » sans accord).
- `a1-voyage|Désolé, je ai oublié.` (« je ai »).
- `a1-voyage|Le la lampe est cassé.`, `Le la cuisinière est cassé.`.
- `a1-voyage|Mon numéro de téléphone est numéro de téléphone.`, `Mon adresse est adresse.`,
  `Mon nom de famille est nom de famille.` : le trou n'est pas rempli (My phone number is phone number) ;
  rendus avec des points de suspension (« Mi número de teléfono es …. »).
- `a1-voyage|Est-ce que l'électricité est compris ?` (accord) ; `a1-voyage|Je suis ici pour des vacances.` (I'm here for a vacation : « Estoy aquí de vacaciones. »).
- `a1-voyage|C'est tout, merci.` : deux variantes anglaises (thank you / thanks) tombent sur le même
  français, donc un seul id — d'où un **doublon inévitable** dans ce bloc (« Eso es todo, gracias. » deux fois).
- `a1-voyage|Il fait beau et chaud, environ vingt-sept degrés.` : voir Doutes (80 °F ≈ 27 °C, cohérent, mais la conversion est dans le français, pas dans l'anglais).
- `premiers-pas|Le petit-déjeuner est délicieux ?`, `Où est le wifi ?`, `J'ai le wifi.`, `La chambre est comprise ?`,
  `Mon dos va mieux.`, `J'ai besoin de noix.`, `Je me sens mieux demain.` : leurres de quiz volontairement
  bizarres ; traduits tels quels (« ¿El desayuno está delicioso? », « Mañana me siento mejor. »).

## À trancher (Espagne / Amérique latine)

Forme d'Amérique latine écrite, selon la décision du 2 nov. ; la forme d'Espagne entre parenthèses.

- **boleto** (billete) : `premiers-pas|Les transports : bus, métro, billets`, `un billet pour…`, `un billet`,
  `Un billet, s'il vous plaît.`, `un aller-retour`, `un aller simple`, `Un billet pour l'aéroport…`, `Un billet pour la gare…`,
  `a1-voyage|Un billet pour …, s'il vous plaît.` et ses trois variantes, `Combien coûte un billet ?`.
  (Les billets de musée sont « entradas », commun aux deux.)
- **reservación** (reserva) : `premiers-pas|L'hôtel : la réservation, la chambre`, `une réservation`, `J'ai une réservation.`,
  `Vous avez une réservation ?`, `He, she, it : has…`, `a1-voyage|J'ai une réservation au nom de ….` et ses variantes,
  `Bonsoir, bienvenue ! Vous avez une réservation ?`, `Oui, j'ai une réservation au nom de Tremblay.`, `Mon ma réservation a été annulé.`.
- **jugo** (zumo) : `premiers-pas|un jus d'orange`, `Un jus d'orange, s'il vous plaît.`, `a1-voyage|Je voudrais un jus d'orange…`.
- **menú** (carta) : `premiers-pas|la carte`, `Est-ce que je peux avoir la carte ?`, `La carte, s'il vous plaît.`, `Vous voulez la carte ?`,
  `Je peux avoir la carte ?`, `a1-voyage|Je peux avoir la carte ?`.
- **en oferta** (de rebajas) : `premiers-pas|en solde`, `Ces chaussures sont en solde.`, `a1-voyage|ces jeans-là sont en solde`,
  `Quarante dollars, mais il est en solde aujourd'hui : trente.`.
- **suéter** (jersey) : `a1-voyage|Je peux essayer ce pull ?`, `Oui, vous avez ce pull en taille M ?`, `je porte un pull`.
- **jeans** (vaqueros) : `a1-voyage|ces jeans-là sont en solde`, `Je peux essayer ce jean ?`.
- **lentes de sol** (gafas de sol) : `a1-voyage|N'oublie pas tes lunettes de soleil !`, `N'oublie pas les lunettes de soleil !`.
- **rentar** (alquilar) : `a1-voyage|Où puis-je louer … ?` et ses trois variantes, `Peut-on louer … ?` et ses trois variantes,
  `Le logement : chercher, louer, les voisins`.
- **carro** (coche) : `a1-voyage|Où puis-je louer une voiture ?`, `prononciation-mot|car|la voiture`,
  `grammaire|pronoms|exemples|2` (« El carro de Anna es azul. »), `grammaire|adjectifs|regle` (« un carro rojo »),
  `grammaire|faux-amis|tableau|3` (« un carro, un coche », les deux).
- **departamento** (piso) et **compañero de departamento** (compañero de piso) : `a1-voyage|j'habite dans un appartement`,
  `nous habitons avec un colocataire`, `Je cherche un colocataire.`, `Je cherche un appartement.`,
  `Bonjour, je suis votre nouveau colocataire.`, `Visiter un appartement`, `25 Beacon Street, appartement 3.`.
- **renta** (alquiler) : `a1-voyage|Combien coûte le loyer ?`, `Combien est le loyer ?`.
- **refrigerador** (nevera ; heladera en Argentine) : `a1-voyage|Le frigo est cassé.`.
- **estufa** (cocina) : `a1-voyage|Le la cuisinière est cassé.`.
- **sala** (salón) : `a1-voyage|Bonjour ! Entrez. Voici le salon.`.
- **computadora** (ordenador) : `prononciation-mot|computer|l'ordinateur`.
- **nueces** (frutos secos) : `premiers-pas|Je suis allergique aux noix.`, `J'ai besoin de noix.`, `a1-voyage|Je suis allergique aux noix.`.
- **siga derecho / todo derecho** (siga recto / todo recto) : `premiers-pas|allez tout droit`, `Allez tout droit pendant deux minutes.`,
  `C'est tout droit.`, `Allez tout droit au coin.`, `a1-voyage|allez tout droit`, `Allez tout droit et tournez à gauche au parc.`.
- **marrón** : `reperes|marron` (« café » au Mexique, « marrón » en Espagne et au Cône Sud ; marrón est compris partout).
- **ascensor** : `premiers-pas|l'ascenseur`, `L'ascenseur est à gauche.`, `a1-voyage|Où est l'ascenseur…` — j'ai choisi
  **ascensor** (Espagne, Argentine, Colombie, Chili…) et non « elevador » (Mexique) : à confirmer.
- **conducir** : `conjugaison|il · elle sait conduire` (« sabe conducir »), `temps|temps-present-simple|texte` (« Él no conduce. ») —
  « manejar » au Mexique ; « conducir » est compris partout (licencia de conducir).
- **tomar** (coger) : `premiers-pas|je prends le bus`, `Je prends le bus.`, `Je prends le métro.`, `a1-voyage|tu prends le métro`,
  `nous prenons un taxi`, `Est-ce que je peux prendre … ?` et ses variantes, `On peut prendre des photos à l'intérieur ?` —
  « coger » est à proscrire en Amérique ; « tomar » se comprend en Espagne.
- **el tiempo** (clima) pour la météo : `premiers-pas|le temps`, `quel temps fait-il ?`, `Quel temps fait-il ?`,
  `a1-voyage|La plage et le temps qu'il fait`, `Le temps qu'il fait : it's…`, `quel temps fait-il ?`, `Quel temps fait-il demain ?` —
  j'ai gardé « tiempo » (forme des manuels, comprise partout) plutôt que « clima » (Mexique) : à confirmer.
- **llenar** (rellenar) : `a1-voyage|Remplir un formulaire`.
- **Nombre décimal** : `premiers-pas|4,50 $` → « $4.50 » (point et signe devant, comme au Mexique ; l'Espagne écrirait « 4,50 $ ») ;
  l'explication `premiers-pas|On dit le prix en dollars et en cents…` dit seulement « En inglés, el punto separa los centavos ».
  `a1-voyage|il fait 24 °C (75 °F)` : pas de décimale, rien à trancher.
