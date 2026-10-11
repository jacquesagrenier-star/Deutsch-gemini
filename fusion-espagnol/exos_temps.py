# -*- coding: utf-8 -*-
"""Les trois jeux de temps de l'espagnol, reecrits : preterito, imperfecto, subjuntivo.

    python fusion-espagnol/exos_temps.py     # (re)ecrit les trois jeux dans espanol/datos/ejercicios.json

POURQUOI (10 oct. 2026). Les anciens jeux avaient ete FABRIQUES : la phrase
d'exemple du present de chaque verbe, mise mecaniquement a un autre temps.
Le resultat etait faux des qu'on le lisait : « Corri en el parque los
sabados » (une habitude : imparfait), « Viví aqui desde hace dos años »
(desde hace veut le present), « Es importante que no pueda salir esta
noche ». Jacques veut l'espagnol « tres, tres solide » avant de le montrer
a des amis qui l'ont etudie a l'universite.

LES REGLES D'ECRITURE
  - Chaque phrase porte le DECLENCHEUR de son temps : ayer, el año pasado,
    hace dos dias (preterito) ; de niño, antes, todos los veranos, mientras
    (imperfecto) ; quiero que, ojala, cuando + avenir, para que (subjuntivo).
    Pas de phrase ou deux temps seraient aussi justes.
  - La bonne forme n'est PAS ecrite ici : elle est lue dans verbos.json
    (conjugaisons verifiees), a la personne donnee. Aucune faute de frappe
    possible dans les reponses.
  - La personne est dans l'indice : « (comer — yo) ». Une reponse a taper
    doit etre unique.
  - Ni vosotros, ni mot qui change en Amerique latine (coche, piso, movil...).
Chaque ligne : (phrase avec ___, infinitif, personne 1/2/3/4/6, traduction
fr, traduction en, cle du declencheur).
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
PERSONNES = {1: (0, "yo"), 2: (1, "tú"), 3: (2, "él, ella"), 4: (3, "nosotros"), 6: (5, "ellos, ellas")}

PRETERITO = [
 ("Ayer ___ paella con mis amigos.", "comer", 1, "Hier, j'ai mangé une paella avec mes amis.", "Yesterday I ate paella with my friends.", "ayer"),
 ("Anoche mis padres ___ a las once.", "llegar", 6, "Hier soir, mes parents sont arrivés à onze heures.", "Last night my parents arrived at eleven.", "anoche"),
 ("El verano pasado ___ a México.", "viajar", 4, "L'été dernier, nous sommes allés au Mexique.", "Last summer we travelled to Mexico.", "pasado"),
 ("Hace dos días Ana me ___ una carta.", "escribir", 3, "Il y a deux jours, Ana m'a écrit une lettre.", "Two days ago Ana wrote me a letter.", "hace"),
 ("¿Qué ___ el sábado pasado?", "hacer", 2, "Qu'est-ce que tu as fait samedi dernier ?", "What did you do last Saturday?", "pasado"),
 ("En 2015 ___ a vivir a Madrid.", "ir", 1, "En 2015, je suis allé vivre à Madrid.", "In 2015 I went to live in Madrid.", "fecha"),
 ("Ayer ___ un día muy largo.", "ser", 3, "Hier, ça a été une très longue journée.", "Yesterday was a very long day.", "ayer"),
 ("La semana pasada no ___ ir a clase.", "poder", 1, "La semaine dernière, je n'ai pas pu aller en cours.", "Last week I couldn't go to class.", "pasado"),
 ("Anoche ___ ocho horas.", "dormir", 1, "Cette nuit, j'ai dormi huit heures.", "Last night I slept for eight hours.", "anoche"),
 ("El lunes pasado el profesor nos ___ un examen.", "dar", 3, "Lundi dernier, le professeur nous a donné un examen.", "Last Monday the teacher gave us a test.", "pasado"),
 ("Ayer ___ las llaves en casa.", "olvidar", 1, "Hier, j'ai oublié mes clés à la maison.", "Yesterday I left my keys at home.", "ayer"),
 ("Hace un año ___ a mi mejor amiga.", "conocer", 1, "Il y a un an, j'ai rencontré ma meilleure amie.", "A year ago I met my best friend.", "hace"),
 ("El año pasado mi hermana ___ un bebé.", "tener", 3, "L'année dernière, ma sœur a eu un bébé.", "Last year my sister had a baby.", "pasado"),
 ("¿Dónde ___ ustedes las vacaciones el verano pasado?", "pasar", 6, "Où avez-vous passé les vacances l'été dernier ?", "Where did you spend your holidays last summer?", "pasado"),
 ("Ayer le ___ la verdad a mi madre.", "decir", 1, "Hier, j'ai dit la vérité à ma mère.", "Yesterday I told my mother the truth.", "ayer"),
 ("El sábado ___ al fútbol con mis primos.", "jugar", 1, "Samedi, j'ai joué au foot avec mes cousins.", "On Saturday I played football with my cousins.", "jour"),
 ("Anoche ___ una película muy buena.", "ver", 4, "Hier soir, nous avons vu un très bon film.", "Last night we watched a very good film.", "anoche"),
 ("De repente ___ a llover.", "empezar", 3, "Soudain, il s'est mis à pleuvoir.", "Suddenly it started to rain.", "soudain"),
 ("Ayer ___ veinte euros por este libro.", "pagar", 1, "Hier, j'ai payé ce livre vingt euros.", "Yesterday I paid twenty euros for this book.", "ayer"),
 ("El martes pasado ___ la cartera en el autobús.", "perder", 2, "Mardi dernier, tu as perdu ton portefeuille dans le bus.", "Last Tuesday you lost your wallet on the bus.", "pasado"),
 ("En 1492 Colón ___ a América.", "llegar", 3, "En 1492, Colomb est arrivé en Amérique.", "In 1492 Columbus reached America.", "fecha"),
 ("Picasso ___ en Málaga en 1881.", "nacer", 3, "Picasso est né à Málaga en 1881.", "Picasso was born in Málaga in 1881.", "fecha"),
 ("Cervantes ___ en 1616.", "morir", 3, "Cervantes est mort en 1616.", "Cervantes died in 1616.", "fecha"),
 ("Ayer mis amigos me ___ con la mudanza.", "ayudar", 6, "Hier, mes amis m'ont aidé pour le déménagement.", "Yesterday my friends helped me with the move.", "ayer"),
 ("Hace una hora ___ la cena.", "preparar", 1, "Il y a une heure, j'ai préparé le dîner.", "An hour ago I made dinner.", "hace"),
 ("El viernes pasado ___ hasta las tres de la mañana.", "bailar", 4, "Vendredi dernier, nous avons dansé jusqu'à trois heures du matin.", "Last Friday we danced until three in the morning.", "pasado"),
 ("Ayer ___ a mi abuela en el hospital.", "visitar", 1, "Hier, j'ai rendu visite à ma grand-mère à l'hôpital.", "Yesterday I visited my grandmother in hospital.", "ayer"),
 ("Anoche no ___ nada: no tenía hambre.", "cenar", 1, "Hier soir, je n'ai rien mangé : je n'avais pas faim.", "Last night I didn't have any dinner: I wasn't hungry.", "anoche"),
 ("Ayer el partido ___ a las nueve.", "empezar", 3, "Hier, le match a commencé à neuf heures.", "Yesterday the match started at nine.", "ayer"),
 ("Ayer ___ a casa muy tarde.", "volver", 4, "Hier, nous sommes rentrés très tard.", "Yesterday we got home very late.", "ayer"),
 ("Hace tres años ___ a conducir.", "aprender", 1, "Il y a trois ans, j'ai appris à conduire.", "Three years ago I learnt to drive.", "hace"),
 ("El mes pasado mi hermano ___ una moto nueva.", "comprar", 3, "Le mois dernier, mon frère a acheté une moto neuve.", "Last month my brother bought a new motorbike.", "pasado"),
 ("Ayer ___ a mi jefe por teléfono.", "llamar", 1, "Hier, j'ai appelé mon chef au téléphone.", "Yesterday I phoned my boss.", "ayer"),
 ("Anoche ___ mucho en la fiesta.", "cantar", 4, "Hier soir, nous avons beaucoup chanté à la fête.", "Last night we sang a lot at the party.", "anoche"),
 ("El domingo ___ dos horas en el parque.", "correr", 1, "Dimanche, j'ai couru deux heures dans le parc.", "On Sunday I ran for two hours in the park.", "jour"),
 ("Ayer por fin ___ el trabajo.", "terminar", 1, "Hier, j'ai enfin terminé le travail.", "Yesterday I finally finished the work.", "ayer"),
 ("Hace cinco minutos ___ el tren.", "salir", 3, "Le train est parti il y a cinq minutes.", "The train left five minutes ago.", "hace"),
 ("En el año 2000 ___ en Madrid por primera vez.", "estar", 1, "En l'an 2000, je suis allé à Madrid pour la première fois.", "In 2000 I was in Madrid for the first time.", "fecha"),
 ("Ayer ___ dos veces.", "llover", 3, "Hier, il a plu deux fois.", "Yesterday it rained twice.", "veces"),
 ("___ en esa casa de 2010 a 2018.", "vivir", 4, "Nous avons vécu dans cette maison de 2010 à 2018.", "We lived in that house from 2010 to 2018.", "duree"),
 ("Ayer ___ una hora en la piscina.", "nadar", 1, "Hier, j'ai nagé une heure à la piscine.", "Yesterday I swam for an hour at the pool.", "ayer"),
 ("La semana pasada ___ tu mensaje, pero no pude contestar.", "leer", 1, "La semaine dernière, j'ai lu ton message, mais je n'ai pas pu répondre.", "Last week I read your message, but I couldn't reply.", "pasado"),
 ("Ayer ___ tarde a la reunión.", "llegar", 2, "Hier, tu es arrivé en retard à la réunion.", "Yesterday you were late for the meeting.", "ayer"),
 ("Anoche mis vecinos ___ mucho ruido.", "hacer", 6, "Hier soir, mes voisins ont fait beaucoup de bruit.", "Last night my neighbours made a lot of noise.", "anoche"),
 ("Hace un mes ___ mi primer sueldo.", "recibir", 1, "Il y a un mois, j'ai reçu mon premier salaire.", "A month ago I got my first salary.", "hace"),
 ("Ayer ___ las ventanas para ventilar.", "abrir", 4, "Hier, nous avons ouvert les fenêtres pour aérer.", "Yesterday we opened the windows to air the room.", "ayer"),
 ("Anoche ___ una pizza a domicilio.", "pedir", 4, "Hier soir, nous nous sommes fait livrer une pizza.", "Last night we ordered a pizza.", "anoche"),
 ("El sábado pasado ___ a mis padres al aeropuerto.", "llevar", 1, "Samedi dernier, j'ai conduit mes parents à l'aéroport.", "Last Saturday I took my parents to the airport.", "pasado"),
 ("Ayer no ___ nada en el supermercado.", "encontrar", 1, "Hier, je n'ai rien trouvé au supermarché.", "Yesterday I couldn't find anything at the supermarket.", "ayer"),
 ("Una vez ___ a Shakira en un concierto.", "ver", 1, "Une fois, j'ai vu Shakira en concert.", "I once saw Shakira in concert.", "veces"),
 ("Ayer ___ las fotos del viaje a mi familia.", "mandar", 1, "Hier, j'ai envoyé les photos du voyage à ma famille.", "Yesterday I sent the trip photos to my family.", "ayer"),
 ("La semana pasada mi padre ___ de trabajo.", "cambiar", 3, "La semaine dernière, mon père a changé de travail.", "Last week my father changed jobs.", "pasado"),
 ("Hace dos semanas ___ el pasaporte.", "perder", 1, "Il y a deux semaines, j'ai perdu mon passeport.", "Two weeks ago I lost my passport.", "hace"),
 ("El domingo ___ para toda la familia.", "cocinar", 1, "Dimanche, j'ai cuisiné pour toute la famille.", "On Sunday I cooked for the whole family.", "jour"),
 ("Ayer ___ la casa entera.", "limpiar", 4, "Hier, nous avons nettoyé toute la maison.", "Yesterday we cleaned the whole house.", "ayer"),
 ("Llegué a casa, ___ y me acosté.", "cenar", 1, "Je suis rentré, j'ai dîné et je me suis couché.", "I got home, had dinner and went to bed.", "suite"),
 ("Ella abrió la puerta, ___ a su alrededor y entró.", "mirar", 3, "Elle a ouvert la porte, a regardé autour d'elle et est entrée.", "She opened the door, looked around and went in.", "suite"),
 ("Ayer los niños ___ al parque después de comer.", "ir", 6, "Hier, les enfants sont allés au parc après le déjeuner.", "Yesterday the children went to the park after lunch.", "ayer"),
 ("Ayer mi tía nos ___ un regalo de Perú.", "traer", 3, "Hier, ma tante nous a apporté un cadeau du Pérou.", "Yesterday my aunt brought us a present from Peru.", "ayer"),
 ("Anoche ___ que estabas enferma.", "saber", 1, "Hier soir, j'ai appris que tu étais malade.", "Last night I found out you were ill.", "anoche"),
 ("El año pasado ___ en un restaurante.", "trabajar", 1, "L'année dernière, j'ai travaillé dans un restaurant.", "Last year I worked in a restaurant.", "pasado"),
 ("Ayer el tren ___ con una hora de retraso.", "salir", 3, "Hier, le train est parti avec une heure de retard.", "Yesterday the train left an hour late.", "ayer"),
 ("Anoche ___ a mi novio en la estación.", "esperar", 1, "Hier soir, j'ai attendu mon copain à la gare.", "Last night I waited for my boyfriend at the station.", "anoche"),
 ("El viernes por fin ___ la casa.", "vender", 4, "Vendredi, nous avons enfin vendu la maison.", "On Friday we finally sold the house.", "jour"),
 ("Ayer mi hermano no ___ venir.", "querer", 3, "Hier, mon frère n'a pas voulu venir.", "Yesterday my brother refused to come.", "ayer"),
 ("El martes ___ con la profesora sobre el examen.", "hablar", 1, "Mardi, j'ai parlé de l'examen avec la professeure.", "On Tuesday I talked to the teacher about the exam.", "jour"),
 ("Ayer ___ el autobús de las ocho.", "tomar", 1, "Hier, j'ai pris le bus de huit heures.", "Yesterday I took the eight o'clock bus.", "ayer"),
 ("La semana pasada ___ a la playa.", "ir", 4, "La semaine dernière, nous sommes allés à la plage.", "Last week we went to the beach.", "pasado"),
 ("Anoche tus padres ___ dos veces.", "llamar", 6, "Hier soir, tes parents ont appelé deux fois.", "Last night your parents called twice.", "veces"),
 ("El jueves ___ el autobús equivocado.", "tomar", 4, "Jeudi, nous avons pris le mauvais bus.", "On Thursday we took the wrong bus.", "jour"),
]

IMPERFECTO = [
 ("De niño ___ al fútbol todos los días.", "jugar", 1, "Enfant, je jouais au foot tous les jours.", "As a child I played football every day.", "enfance"),
 ("Cuando era pequeña, ___ en un pueblo.", "vivir", 1, "Quand j'étais petite, je vivais dans un village.", "When I was little, I lived in a village.", "enfance"),
 ("Antes mi padre ___ los sábados.", "trabajar", 3, "Avant, mon père travaillait le samedi.", "My father used to work on Saturdays.", "antes"),
 ("Todos los veranos ___ a la playa con nuestros primos.", "ir", 4, "Tous les étés, nous allions à la plage avec nos cousins.", "Every summer we used to go to the beach with our cousins.", "habitude"),
 ("___ las ocho cuando llegó el tren.", "ser", 6, "Il était huit heures quand le train est arrivé.", "It was eight o'clock when the train arrived.", "heure"),
 ("Cuando ___ diez años, aprendí a nadar.", "tener", 1, "Quand j'avais dix ans, j'ai appris à nager.", "When I was ten, I learnt to swim.", "heure"),
 ("Mientras yo ___, mi hermano veía la tele.", "cocinar", 1, "Pendant que je cuisinais, mon frère regardait la télé.", "While I was cooking, my brother was watching TV.", "mientras"),
 ("___ cuando sonó el teléfono.", "dormir", 1, "Je dormais quand le téléphone a sonné.", "I was asleep when the phone rang.", "interrompue"),
 ("Mi abuela siempre nos ___ cuentos antes de dormir.", "leer", 3, "Ma grand-mère nous lisait toujours des histoires avant de dormir.", "My grandmother always read us stories at bedtime.", "habitude"),
 ("De niño, mi casa ___ grande y tenía un jardín.", "ser", 3, "Quand j'étais enfant, ma maison était grande et avait un jardin.", "When I was a child, my house was big and had a garden.", "enfance"),
 ("Hacía sol y los niños ___ en la playa.", "jugar", 6, "Il faisait beau et les enfants jouaient sur la plage.", "It was sunny and the children were playing on the beach.", "decor"),
 ("Antes ___ más tiempo libre.", "tener", 4, "Avant, nous avions plus de temps libre.", "We used to have more free time.", "antes"),
 ("Cuando ___ estudiante, compartía casa con dos amigos.", "ser", 1, "Quand j'étais étudiant, je partageais une maison avec deux amis.", "When I was a student, I shared a house with two friends.", "periode"),
 ("De niños, los domingos ___ con nuestros abuelos.", "comer", 4, "Enfants, le dimanche, nous déjeunions chez nos grands-parents.", "As children, we used to have lunch with our grandparents on Sundays.", "enfance"),
 ("Antes la gente ___ más cartas.", "escribir", 6, "Avant, les gens écrivaient plus de lettres.", "People used to write more letters.", "antes"),
 ("Mientras ___, escuchaba música.", "estudiar", 1, "Pendant que j'étudiais, j'écoutais de la musique.", "While I was studying, I used to listen to music.", "mientras"),
 ("Cuando llegaste, yo ___ la cena.", "preparar", 1, "Quand tu es arrivé, je préparais le dîner.", "When you arrived, I was making dinner.", "interrompue"),
 ("En aquella época mi madre ___ en un banco.", "trabajar", 3, "À cette époque, ma mère travaillait dans une banque.", "At that time my mother worked in a bank.", "periode"),
 ("De niños ___ mucho a nuestros primos.", "ver", 4, "Enfants, nous voyions souvent nos cousins.", "As children we saw our cousins a lot.", "enfance"),
 ("Antes siempre ___ el autobús de las siete.", "tomar", 1, "Avant, je prenais toujours le bus de sept heures.", "I always used to take the seven o'clock bus.", "antes"),
 ("Cuando salimos, ___ mucho frío.", "hacer", 3, "Quand nous sommes sortis, il faisait très froid.", "When we went out, it was very cold.", "decor"),
 ("De niño, mi pueblo ___ tranquilo y bonito.", "ser", 3, "Quand j'étais enfant, mon village était calme et joli.", "When I was a child, my village was quiet and pretty.", "enfance"),
 ("Cuando ___ en Madrid, iba al Prado cada mes.", "vivir", 1, "Quand je vivais à Madrid, j'allais au Prado tous les mois.", "When I lived in Madrid, I went to the Prado every month.", "periode"),
 ("Cuando era niño, mi perro siempre me ___ en la puerta.", "esperar", 3, "Quand j'étais enfant, mon chien m'attendait toujours à la porte.", "When I was a child, my dog always waited for me at the door.", "enfance"),
 ("Mientras los niños ___, nosotros limpiamos la cocina.", "dormir", 6, "Pendant que les enfants dormaient, nous avons nettoyé la cuisine.", "While the children were sleeping, we cleaned the kitchen.", "mientras"),
 ("Antes no ___ conducir.", "saber", 1, "Avant, je ne savais pas conduire.", "I didn't use to know how to drive.", "antes"),
 ("Cuando mi abuelo ___ joven, tocaba la guitarra.", "ser", 3, "Quand mon grand-père était jeune, il jouait de la guitare.", "When my grandfather was young, he played the guitar.", "periode"),
 ("___ las tres de la mañana y no podía dormir.", "ser", 6, "Il était trois heures du matin et je n'arrivais pas à dormir.", "It was three in the morning and I couldn't sleep.", "heure"),
 ("Mi madre ___ treinta años cuando nací.", "tener", 3, "Ma mère avait trente ans quand je suis né.", "My mother was thirty when I was born.", "heure"),
 ("En aquella época, todos los días ___ de casa a las seis.", "salir", 1, "À cette époque, je partais de chez moi à six heures tous les jours.", "At that time, I left home at six every day.", "periode"),
 ("De niña ___ ser veterinaria.", "querer", 1, "Petite, je voulais être vétérinaire.", "As a girl I wanted to be a vet.", "enfance"),
 ("Antes este barrio ___ más bonito.", "ser", 3, "Avant, ce quartier était plus joli.", "This neighbourhood used to be nicer.", "antes"),
 ("De joven, los sábados ___ al cine con mis amigos.", "ir", 1, "Jeune, le samedi, j'allais au cinéma avec mes amis.", "When I was young, I went to the cinema with my friends on Saturdays.", "periode"),
 ("Mientras ___ por el parque, vi a un viejo amigo.", "caminar", 1, "Pendant que je marchais dans le parc, j'ai vu un vieil ami.", "While I was walking through the park, I saw an old friend.", "mientras"),
 ("Cuando sonó el despertador, ___ un sueño precioso.", "tener", 1, "Quand le réveil a sonné, je faisais un rêve magnifique.", "When the alarm went off, I was having a lovely dream.", "interrompue"),
 ("En mi antiguo colegio, los profesores ___ muy estrictos.", "ser", 6, "Dans mon ancienne école, les professeurs étaient très stricts.", "At my old school, the teachers were very strict.", "decor"),
 ("Antes mis abuelos ___ en el campo.", "vivir", 6, "Avant, mes grands-parents vivaient à la campagne.", "My grandparents used to live in the country.", "antes"),
 ("De niños, cada verano ___ un mes en la playa.", "pasar", 4, "Enfants, chaque été, nous passions un mois à la plage.", "As children, we spent a month at the beach every summer.", "enfance"),
 ("Cuando la conocí, ___ un vestido rojo.", "llevar", 3, "Quand je l'ai rencontrée, elle portait une robe rouge.", "When I met her, she was wearing a red dress.", "decor"),
 ("Mientras tú ___ la tele, yo trabajaba.", "ver", 2, "Pendant que tu regardais la télé, moi, je travaillais.", "While you were watching TV, I was working.", "mientras"),
 ("Antes ___ más deporte.", "hacer", 1, "Avant, je faisais plus de sport.", "I used to do more sport.", "antes"),
 ("De niño ___ miedo de los perros.", "tener", 1, "Enfant, j'avais peur des chiens.", "As a child I was afraid of dogs.", "enfance"),
 ("Cuando ___ en la universidad, leía muchísimo.", "estar", 1, "Quand j'étais à l'université, je lisais énormément.", "When I was at university, I read a huge amount.", "periode"),
 ("Antes mi abuelo ___ todos los días al bar del pueblo.", "ir", 3, "Avant, mon grand-père allait tous les jours au bar du village.", "My grandfather used to go to the village bar every day.", "antes"),
 ("Mientras ___ en el tren, leía el periódico.", "viajar", 1, "Pendant que je voyageais en train, je lisais le journal.", "While I was travelling on the train, I read the paper.", "mientras"),
 ("___ cansada y me fui a la cama.", "estar", 1, "J'étais fatiguée et je suis allée me coucher.", "I was tired and went to bed.", "decor"),
 ("Cuando entré, mis padres ___ en la cocina.", "hablar", 6, "Quand je suis entré, mes parents parlaient dans la cuisine.", "When I came in, my parents were talking in the kitchen.", "interrompue"),
 ("Cuando éramos pequeños, ___ en el río.", "nadar", 4, "Quand nous étions petits, nous nagions dans la rivière.", "When we were little, we used to swim in the river.", "enfance"),
 ("Antes no ___ café.", "beber", 1, "Avant, je ne buvais pas de café.", "I didn't use to drink coffee.", "antes"),
 ("En aquella época ___ mucho a mis padres.", "llamar", 1, "À cette époque, j'appelais souvent mes parents.", "At that time I called my parents a lot.", "periode"),
 ("Cuando llegamos, la ciudad ___ llena de turistas.", "estar", 3, "Quand nous sommes arrivés, la ville était pleine de touristes.", "When we arrived, the city was full of tourists.", "decor"),
 ("Mientras mi hermana ___ la cena, yo ponía la mesa.", "preparar", 3, "Pendant que ma sœur préparait le dîner, je mettais la table.", "While my sister was making dinner, I was laying the table.", "mientras"),
 ("De joven, mi padre ___ en una banda de rock.", "tocar", 3, "Jeune, mon père jouait dans un groupe de rock.", "When he was young, my father played in a rock band.", "periode"),
 ("Siempre que ___, íbamos al museo.", "llover", 3, "Chaque fois qu'il pleuvait, nous allions au musée.", "Whenever it rained, we went to the museum.", "habitude"),
 ("Cuando ___ niña, no había internet.", "ser", 1, "Quand j'étais petite, il n'y avait pas internet.", "When I was a girl, there was no internet.", "enfance"),
 ("Antes ___ en autobús al trabajo.", "ir", 1, "Avant, j'allais au travail en bus.", "I used to go to work by bus.", "antes"),
 ("Mi primera bicicleta ___ roja.", "ser", 3, "Mon premier vélo était rouge.", "My first bike was red.", "decor"),
 ("Antes, todos los inviernos ___ mucho en mi pueblo.", "nevar", 3, "Avant, il neigeait beaucoup chaque hiver dans mon village.", "It used to snow a lot every winter in my village.", "antes"),
 ("___ las diez cuando terminó la película.", "ser", 6, "Il était dix heures quand le film s'est terminé.", "It was ten o'clock when the film ended.", "heure"),
 ("Mientras ellos ___, nosotros bailábamos.", "cantar", 6, "Pendant qu'ils chantaient, nous dansions.", "While they were singing, we were dancing.", "mientras"),
 ("De pequeño ___ mucho a los videojuegos.", "jugar", 1, "Petit, je jouais beaucoup aux jeux vidéo.", "As a kid I played video games a lot.", "enfance"),
 ("Cuando vivíamos en Lima, ___ ceviche cada semana.", "comer", 4, "Quand nous vivions à Lima, nous mangions du ceviche chaque semaine.", "When we lived in Lima, we ate ceviche every week.", "periode"),
 ("Antes las tiendas ___ los domingos.", "cerrar", 6, "Avant, les magasins fermaient le dimanche.", "Shops used to close on Sundays.", "antes"),
 ("Cuando me llamaste, ___ en la ducha.", "estar", 1, "Quand tu m'as appelé, j'étais sous la douche.", "When you called me, I was in the shower.", "interrompue"),
 ("En esa época ___ poco dinero.", "ganar", 1, "À cette époque, je gagnais peu d'argent.", "At that time I earned little money.", "periode"),
 ("Antes mi abuela ___ el pan en casa.", "hacer", 3, "Avant, ma grand-mère faisait le pain à la maison.", "My grandmother used to bake bread at home.", "antes"),
 ("Cuando ___ quince años, quería ser actor.", "tener", 1, "Quand j'avais quinze ans, je voulais être acteur.", "When I was fifteen, I wanted to be an actor.", "heure"),
 ("Mientras ___ el informe, se fue la luz.", "escribir", 1, "Pendant que j'écrivais le rapport, il y a eu une coupure de courant.", "While I was writing the report, the power went off.", "interrompue"),
 ("Cuando llegué, los niños ___ felices en el jardín.", "jugar", 6, "Quand je suis arrivé, les enfants jouaient joyeusement dans le jardin.", "When I arrived, the children were playing happily in the garden.", "decor"),
 ("Antes ___ más a menudo a mis amigos.", "ver", 1, "Avant, je voyais mes amis plus souvent.", "I used to see my friends more often.", "antes"),
]

SUBJUNTIVO = [
 ("Quiero que ___ a mi fiesta.", "venir", 2, "Je veux que tu viennes à ma fête.", "I want you to come to my party.", "souhait"),
 ("Espero que mañana ___ buen tiempo.", "hacer", 3, "J'espère qu'il fera beau demain.", "I hope the weather is nice tomorrow.", "souhait"),
 ("Ojalá mi hermano ___ trabajo pronto.", "encontrar", 3, "Pourvu que mon frère trouve vite du travail.", "I hope my brother finds a job soon.", "ojala"),
 ("Es importante que ___ mucha agua.", "beber", 2, "Il est important que tu boives beaucoup d'eau.", "It's important that you drink plenty of water.", "necessite"),
 ("No creo que ___ hoy.", "llover", 3, "Je ne crois pas qu'il pleuve aujourd'hui.", "I don't think it'll rain today.", "doute"),
 ("Me alegra que ___ aquí.", "estar", 2, "Je suis content que tu sois là.", "I'm glad you're here.", "emotion"),
 ("Cuando ___ a casa, te llamo.", "llegar", 1, "Quand j'arriverai à la maison, je t'appelle.", "When I get home, I'll call you.", "cuando"),
 ("Te lo explico otra vez para que lo ___.", "entender", 2, "Je te l'explique encore une fois pour que tu le comprennes.", "I'll explain it again so that you understand.", "but"),
 ("Antes de que ___ los invitados, limpiamos la casa.", "llegar", 6, "Avant que les invités arrivent, nous nettoyons la maison.", "Before the guests arrive, we're cleaning the house.", "avant"),
 ("Te aconsejo que ___ temprano.", "salir", 2, "Je te conseille de partir tôt.", "I advise you to leave early.", "conseil"),
 ("Es posible que ___ tarde.", "llegar", 4, "Il est possible que nous arrivions en retard.", "We may arrive late.", "possible"),
 ("Busco una casa que ___ jardín.", "tener", 3, "Je cherche une maison qui ait un jardin.", "I'm looking for a house with a garden.", "relative"),
 ("Mis padres quieren que ___ medicina.", "estudiar", 1, "Mes parents veulent que j'étudie la médecine.", "My parents want me to study medicine.", "souhait"),
 ("Espero que ustedes lo ___ bien.", "pasar", 6, "J'espère que vous passerez un bon moment.", "I hope you have a good time.", "souhait"),
 ("Ojalá ___ verte pronto.", "poder", 1, "Pourvu que je puisse te voir bientôt.", "I hope I can see you soon.", "ojala"),
 ("Es necesario que ___ el contrato antes de firmar.", "leer", 2, "Il faut que tu lises le contrat avant de signer.", "You need to read the contract before you sign.", "necessite"),
 ("Dudo que ___ la verdad.", "decir", 3, "Je doute qu'il dise la vérité.", "I doubt he's telling the truth.", "doute"),
 ("Siento que no ___ venir.", "poder", 2, "Je regrette que tu ne puisses pas venir.", "I'm sorry you can't come.", "emotion"),
 ("Cuando ___ mayor, quiero ser piloto.", "ser", 1, "Quand je serai grand, je veux être pilote.", "When I grow up, I want to be a pilot.", "cuando"),
 ("Hablo despacio para que me ___.", "entender", 2, "Je parle lentement pour que tu me comprennes.", "I speak slowly so that you understand me.", "but"),
 ("Llámame antes de que ___.", "salir", 2, "Appelle-moi avant de partir.", "Call me before you leave.", "avant"),
 ("Te pido que no ___ tanto ruido.", "hacer", 2, "Je te demande de ne pas faire autant de bruit.", "I'm asking you not to make so much noise.", "conseil"),
 ("Puede que ___ razón.", "tener", 2, "Il se peut que tu aies raison.", "You may be right.", "possible"),
 ("Necesito a alguien que ___ alemán.", "hablar", 3, "J'ai besoin de quelqu'un qui parle allemand.", "I need someone who speaks German.", "relative"),
 ("La profesora quiere que ___ el capítulo tres.", "leer", 4, "La professeure veut que nous lisions le chapitre trois.", "The teacher wants us to read chapter three.", "souhait"),
 ("Espero que ___ un buen viaje.", "tener", 2, "J'espère que tu feras bon voyage.", "I hope you have a good trip.", "souhait"),
 ("Ojalá mañana no ___.", "llover", 3, "Pourvu qu'il ne pleuve pas demain.", "I hope it doesn't rain tomorrow.", "ojala"),
 ("Es mejor que ___ en taxi.", "ir", 4, "Il vaut mieux que nous y allions en taxi.", "We'd better go by taxi.", "necessite"),
 ("No pienso que ___ tan difícil.", "ser", 3, "Je ne pense pas que ce soit si difficile.", "I don't think it's that difficult.", "doute"),
 ("Me encanta que ___ juntos.", "estar", 4, "J'adore que nous soyons ensemble.", "I love that we're together.", "emotion"),
 ("Cuando ___ dinero, me compraré una moto.", "tener", 1, "Quand j'aurai de l'argent, je m'achèterai une moto.", "When I have money, I'll buy myself a motorbike.", "cuando"),
 ("Te mando la dirección para que no te ___.", "perder", 2, "Je t'envoie l'adresse pour que tu ne te perdes pas.", "I'm sending you the address so you don't get lost.", "but"),
 ("Termina los deberes antes de que ___ tu padre.", "volver", 3, "Finis tes devoirs avant que ton père rentre.", "Finish your homework before your father gets back.", "avant"),
 ("Te recomiendo que ___ esta película.", "ver", 2, "Je te recommande de voir ce film.", "I recommend you see this film.", "conseil"),
 ("Es probable que mis padres ___ en marzo.", "volver", 6, "Il est probable que mes parents reviennent en mars.", "My parents will probably come back in March.", "possible"),
 ("No hay nadie que ___ esto.", "saber", 3, "Il n'y a personne qui sache ça.", "There's nobody who knows this.", "relative"),
 ("Quiero que me ___ la verdad.", "decir", 2, "Je veux que tu me dises la vérité.", "I want you to tell me the truth.", "souhait"),
 ("Espero que mis amigos ___ a la boda.", "venir", 6, "J'espère que mes amis viendront au mariage.", "I hope my friends come to the wedding.", "souhait"),
 ("Ojalá ___ suerte en la entrevista.", "tener", 2, "Pourvu que tu aies de la chance à l'entretien.", "I hope you're lucky in the interview.", "ojala"),
 ("Es importante que los niños ___ ocho horas.", "dormir", 6, "Il est important que les enfants dorment huit heures.", "It's important that children sleep eight hours.", "necessite"),
 ("No creo que ellos ___ en casa.", "estar", 6, "Je ne crois pas qu'ils soient à la maison.", "I don't think they're at home.", "doute"),
 ("Me molesta que siempre ___ tarde.", "llegar", 2, "Ça m'agace que tu arrives toujours en retard.", "It annoys me that you're always late.", "emotion"),
 ("Cuando ___ el verano, iremos a la playa.", "llegar", 3, "Quand l'été arrivera, nous irons à la plage.", "When summer comes, we'll go to the beach.", "cuando"),
 ("Trabajo mucho para que mis hijos ___ mejor.", "vivir", 6, "Je travaille beaucoup pour que mes enfants vivent mieux.", "I work hard so that my children have a better life.", "but"),
 ("Antes de que ___ la película, compramos palomitas.", "empezar", 3, "Avant que le film commence, nous achetons du pop-corn.", "Before the film starts, we're buying popcorn.", "avant"),
 ("El médico me pide que ___ menos sal.", "comer", 1, "Le médecin me demande de manger moins de sel.", "The doctor asks me to eat less salt.", "conseil"),
 ("Busco un trabajo que ___ cerca de casa.", "estar", 3, "Je cherche un travail qui soit près de chez moi.", "I'm looking for a job near home.", "relative"),
 ("Queremos que nuestros hijos ___ idiomas.", "aprender", 6, "Nous voulons que nos enfants apprennent des langues.", "We want our children to learn languages.", "souhait"),
 ("Espero que no ___ nada grave.", "ser", 3, "J'espère que ce n'est rien de grave.", "I hope it's nothing serious.", "souhait"),
 ("Ojalá el autobús ___ a tiempo.", "llegar", 3, "Pourvu que le bus arrive à l'heure.", "I hope the bus arrives on time.", "ojala"),
 ("Es necesario que ___ antes de las diez.", "salir", 4, "Il faut que nous partions avant dix heures.", "We need to leave before ten.", "necessite"),
 ("Dudo que mi jefe me ___ vacaciones.", "dar", 3, "Je doute que mon chef me donne des vacances.", "I doubt my boss will give me time off.", "doute"),
 ("Me sorprende que no ___ nada.", "saber", 2, "Ça m'étonne que tu ne saches rien.", "I'm surprised you don't know anything.", "emotion"),
 ("Cuando ___ a Madrid, visita el Prado.", "ir", 2, "Quand tu iras à Madrid, visite le Prado.", "When you go to Madrid, visit the Prado.", "cuando"),
 ("Te dejo las llaves para que ___ entrar.", "poder", 2, "Je te laisse les clés pour que tu puisses entrer.", "I'm leaving you the keys so you can get in.", "but"),
 ("Cierra la ventana antes de que ___ a llover.", "empezar", 3, "Ferme la fenêtre avant qu'il commence à pleuvoir.", "Shut the window before it starts to rain.", "avant"),
 ("Le pido a mi hermano que me ___ con la mudanza.", "ayudar", 3, "Je demande à mon frère de m'aider pour le déménagement.", "I'm asking my brother to help me with the move.", "conseil"),
 ("Puede que mañana ___ en casa todo el día.", "estar", 1, "Il se peut que je reste à la maison toute la journée demain.", "I may be at home all day tomorrow.", "possible"),
 ("¿Conoces a alguien que ___ un piano?", "vender", 3, "Tu connais quelqu'un qui vende un piano ?", "Do you know anyone selling a piano?", "relative"),
 ("Mi madre quiere que ___ la mesa.", "poner", 4, "Ma mère veut que nous mettions la table.", "My mother wants us to lay the table.", "souhait"),
 ("Espero que ___ la carta pronto.", "recibir", 2, "J'espère que tu recevras vite la lettre.", "I hope you get the letter soon.", "souhait"),
 ("Ojalá ___ verdad.", "ser", 3, "Pourvu que ce soit vrai.", "I hope it's true.", "ojala"),
 ("Es importante que tus padres ___ la verdad.", "saber", 6, "Il est important que tes parents sachent la vérité.", "It's important that your parents know the truth.", "necessite"),
 ("No es verdad que ___ tanto.", "trabajar", 1, "Ce n'est pas vrai que je travaille autant.", "It isn't true that I work that much.", "doute"),
 ("Me alegro de que ___ un trabajo.", "encontrar", 2, "Je suis content que tu aies trouvé un travail.", "I'm glad you've found a job.", "emotion"),
 ("Cuando ___ el libro, te lo presto.", "terminar", 1, "Quand j'aurai fini le livre, je te le prête.", "When I finish the book, I'll lend it to you.", "cuando"),
 ("Hago una lista para que no ___ nada.", "olvidar", 4, "Je fais une liste pour que nous n'oubliions rien.", "I'm making a list so that we don't forget anything.", "but"),
 ("Vámonos antes de que ___ tarde.", "ser", 3, "Partons avant qu'il soit trop tard.", "Let's go before it's too late.", "avant"),
 ("Te aconsejo que ___ con ella.", "hablar", 2, "Je te conseille de lui parler.", "I advise you to talk to her.", "conseil"),
 ("Es posible que ___ a vivir a Chile.", "ir", 4, "Il est possible que nous allions vivre au Chili.", "We might go and live in Chile.", "possible"),
]

RAISONS = {
 "preterito": {
  "ayer": ("« ayer » : une action terminée, à un moment précis → prétérit.", "« ayer »: a finished action at a definite time → preterite."),
  "anoche": ("« anoche » : un moment précis et terminé → prétérit.", "« anoche »: a definite, finished time → preterite."),
  "pasado": ("« el … pasado » : une période terminée → prétérit.", "« el … pasado »: a finished period → preterite."),
  "hace": ("« hace + durée » (il y a…) date un événement terminé → prétérit.", "« hace + time » (… ago) dates a finished event → preterite."),
  "fecha": ("Une date : un événement daté et terminé → prétérit.", "A date: a dated, finished event → preterite."),
  "jour": ("« el sábado », « el domingo » : un jour précis, passé → prétérit.", "« el sábado », « el domingo »: one specific past day → preterite."),
  "soudain": ("« de repente » : un événement soudain → prétérit.", "« de repente »: a sudden event → preterite."),
  "veces": ("On compte les fois (« una vez », « dos veces ») : des actions terminées → prétérit.", "Counting occurrences (« una vez », « dos veces »): finished actions → preterite."),
  "duree": ("Une durée fermée (« de 2010 a 2018 ») : l'action est vue comme terminée → prétérit.", "A closed period (« de 2010 a 2018 »): the action is seen as finished → preterite."),
  "suite": ("Une suite d'actions qui font avancer le récit → prétérit.", "A sequence of actions moving the story on → preterite."),
 },
 "imperfecto": {
  "enfance": ("« de niño », « cuando era pequeño » : comment c'était, ce qu'on faisait d'habitude → imparfait.", "« de niño », « cuando era pequeño »: what things were like, what you used to do → imperfect."),
  "antes": ("« antes » (autrefois) : une habitude ou un état passés → imparfait.", "« antes » (in the past): a past habit or state → imperfect."),
  "habitude": ("Une habitude du passé (« todos los veranos », « siempre que ») → imparfait.", "A past habit (« todos los veranos », « siempre que ») → imperfect."),
  "periode": ("Une période du passé, sans limite précise (« en aquella época », « cuando vivía… ») → imparfait.", "An open period in the past (« en aquella época », « cuando vivía… ») → imperfect."),
  "mientras": ("« mientras » : une action en cours, en toile de fond → imparfait.", "« mientras »: an action in progress, in the background → imperfect."),
  "interrompue": ("L'action en cours au moment où autre chose arrive → imparfait (l'autre action, au prétérit).", "The action in progress when something else happens → imperfect (the other one in the preterite)."),
  "decor": ("Le décor, l'état ou la description d'une scène passée → imparfait.", "The background, a state or a description in the past → imperfect."),
  "heure": ("L'heure et l'âge, dans le passé → toujours l'imparfait.", "Time of day and age, in the past → always the imperfect."),
 },
 "subjuntivo": {
  "souhait": ("Un souhait sur quelqu'un d'autre (« quiero que », « espero que ») → subjonctif. Le français dit parfois le futur (« j'espère qu'il viendra ») : l'espagnol, jamais.", "A wish about someone else (« quiero que », « espero que ») → subjunctive."),
  "ojala": ("« ojalá » (pourvu que) → toujours le subjonctif.", "« ojalá » (let's hope) → always the subjunctive."),
  "necessite": ("« es importante / necesario / mejor que » : une nécessité, pas un fait → subjonctif.", "« es importante / necesario / mejor que »: a necessity, not a fact → subjunctive."),
  "doute": ("Le doute ou la négation d'une opinion (« no creo que », « dudo que ») → subjonctif.", "Doubt or a denied opinion (« no creo que », « dudo que ») → subjunctive."),
  "emotion": ("Une émotion face à un fait (« me alegra que », « siento que ») → subjonctif, comme en français.", "An emotion about a fact (« me alegra que », « siento que ») → subjunctive."),
  "cuando": ("« cuando » tourné vers l'avenir → subjonctif. Le français met le futur (« quand j'arriverai ») : l'espagnol, jamais (pas « cuando llegaré »).", "« cuando » about the future → subjunctive, never the future (not « cuando llegaré »)."),
  "but": ("« para que » (pour que) → toujours le subjonctif.", "« para que » (so that) → always the subjunctive."),
  "avant": ("« antes de que » (avant que) → toujours le subjonctif.", "« antes de que » (before) → always the subjunctive."),
  "conseil": ("Un conseil ou une demande (« te aconsejo que », « te pido que ») → subjonctif. Le français dit souvent « de + infinitif ».", "Advice or a request (« te aconsejo que », « te pido que ») → subjunctive."),
  "possible": ("« es posible que », « puede que », « es probable que » → subjonctif.", "« es posible que », « puede que », « es probable que » → subjunctive."),
  "relative": ("On cherche quelque chose (ou quelqu'un) dont l'existence n'est pas sûre → subjonctif dans la relative.", "Looking for something (or someone) that may not exist → subjunctive in the relative clause."),
 },
}
TEMPS = {
 "preterito": ("Pretérito", "praeteritumExercises", "prétérit", "preterite", PRETERITO),
 "imperfecto": ("Imperfecto", "perfektExercises", "imparfait", "imperfect", IMPERFECTO),
 "subjuntivo": ("Subjuntivo", "konjunktiv2Exercises", "subjonctif présent", "present subjunctive", SUBJUNTIVO),
}


def main():
    verbos = json.load(io.open(os.path.join(DATOS, "verbos.json"), encoding="utf-8"))
    idx = {x["infinitif"]: x for n in verbos.values() for x in n}
    chemin = os.path.join(DATOS, "ejercicios.json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    for cle, (topic, jeu, nom_fr, nom_en, lignes) in TEMPS.items():
        assert len(lignes) >= 50, (jeu, len(lignes))
        assert len({l[0] for l in lignes}) == len(lignes), "phrase en double dans " + jeu
        sortie = []
        for q, inf, pers, tfr, ten, raison in lignes:
            assert q.count("___") == 1, q
            assert inf in idx, "verbe absent du corpus : " + inf
            formes = idx[inf][cle]
            rang, sujet = PERSONNES[pers]
            bonne = formes[rang]
            rfr, ren = RAISONS[cle][raison]
            liste = " · ".join(f for i, f in enumerate(formes) if i != 4)
            sortie.append({
                "topic": topic, "question": q,
                "translation": tfr, "translation_en": ten,
                "hint": "(%s — %s)" % (inf, sujet), "hint_en": "(%s — %s)" % (inf, sujet),
                "answers": [bonne], "correct": bonne,
                "explanation": "%s %s de « %s » : %s." % (rfr, nom_fr[0].upper() + nom_fr[1:], inf, liste),
                "explanation_en": "%s %s of « %s »: %s." % (ren, nom_en[0].upper() + nom_en[1:], inf, liste),
            })
        d["jeux"][jeu] = sortie
        print("%-22s %d questions" % (jeu, len(sortie)))
    io.open(chemin, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
