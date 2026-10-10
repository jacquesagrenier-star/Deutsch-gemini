# -*- coding: utf-8 -*-
"""Trois jeux de pieges de l'espagnol : faux amis, verbes comme gustar, accents.

    python fusion-espagnol/exos_pieges.py     # (re)ecrit les trois jeux dans espanol/datos/ejercicios.json

Demandes par Jacques le 10 oct. 2026, apres ser / estar et por / para
(exos_paires.py, dont on reprend le format et les regles d'ecriture) :
deux options, une seule juste.

  - FAUX AMIS : la traduction donne le sens, il faut choisir le mot espagnol ;
    l'autre option est le mot qui RESSEMBLE au francais (ou a l'anglais).
    Ici la traduction ne cache rien : elle EST la consigne.
  - GUSTAR : l'accord se fait avec la chose aimee, pas avec la personne, et la
    personne passe par me / te / le / nos / les.
  - ACCENTS : seulement des paires ou l'accent CHANGE LE SENS (tu / tu,
    hablo / hablo...). Pas de solo / solo ni de este / este : la RAE n'y
    exige plus d'accent, on enseignerait une regle morte.

Pas de vosotros, pas de mot propre a une seule variante (zumo, patata) :
ces phrases servent en Espagne et en Amerique latine.
Chaque ligne : (phrase avec ___, reponse, l'autre option, traduction fr,
traduction en, explication fr, explication en).
"""
import io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exos_paires import CHEMIN  # noqa : le meme fichier

FAUX_AMIS = [
 ("Me caí delante de todos y estaba muy ___.", "avergonzada", "embarazada", "Je suis tombée devant tout le monde et j'étais très gênée.", "I fell in front of everyone and I was very embarrassed.", "avergonzada = gênée. embarazada = enceinte !", "avergonzada = embarrassed. embarazada = pregnant!"),
 ("Tengo fiebre y estoy ___.", "constipado", "estreñido", "J'ai de la fièvre et je suis enrhumé.", "I have a fever and a cold.", "constipado = enrhumé. Constipé se dit estreñido.", "constipado = having a cold. Constipated is estreñido."),
 ("No como fibra y estoy ___ desde hace tres días.", "estreñido", "constipado", "Je ne mange pas de fibres et je suis constipé depuis trois jours.", "I don't eat fibre and I've been constipated for three days.", "Constipé = estreñido. constipado veut dire enrhumé.", "Constipated = estreñido. constipado means having a cold."),
 ("La película fue un gran ___.", "éxito", "suceso", "Le film a été un grand succès.", "The film was a big hit.", "Le succès = el éxito. un suceso = un fait divers, un événement.", "Success = el éxito. un suceso = an incident, a news item."),
 ("Perdone, busco ___: ¿está al fondo?", "la salida", "el éxito", "Pardon, je cherche la sortie : elle est au fond ?", "Excuse me, I'm looking for the exit: is it at the back?", "La sortie = la salida. el éxito = le succès (piège pour l'anglais exit).", "The exit = la salida. el éxito = success, not exit."),
 ("Pedí el libro prestado en la ___ municipal.", "biblioteca", "librería", "J'ai emprunté le livre à la bibliothèque municipale.", "I borrowed the book from the public library.", "Bibliothèque = biblioteca. librería = librairie, où l'on achète.", "Library = biblioteca. librería = bookshop, where you buy."),
 ("Compré una novela en la ___ de la esquina.", "librería", "biblioteca", "J'ai acheté un roman à la librairie du coin.", "I bought a novel at the bookshop on the corner.", "librería = librairie. On y achète ; à la biblioteca, on emprunte.", "librería = bookshop. You buy there; at the biblioteca you borrow."),
 ("Hay una ___ persa en el salón.", "alfombra", "carpeta", "Il y a un tapis persan dans le salon.", "There's a Persian rug in the living room.", "Un tapis = una alfombra. una carpeta = une chemise, un dossier.", "A rug = una alfombra. una carpeta = a folder."),
 ("Guarda los documentos en esta ___ azul.", "carpeta", "alfombra", "Range les documents dans cette chemise bleue.", "Put the documents in this blue folder.", "carpeta = chemise (de bureau), dossier. Pas une carpette !", "carpeta = folder. Not a carpet!"),
 ("El río es muy ___: mide quinientos kilómetros.", "largo", "ancho", "Le fleuve est très long : il mesure cinq cents kilomètres.", "The river is very long: it's five hundred kilometres.", "largo = long. Large se dit ancho.", "largo = long, not large. Wide is ancho."),
 ("La calle es muy ___: caben cuatro coches uno al lado de otro.", "ancha", "larga", "La rue est très large : quatre voitures y tiennent côte à côte.", "The street is very wide: four cars fit side by side.", "Large = ancho. largo veut dire long.", "Wide = ancho. largo means long."),
 ("Le escribí hace una semana y todavía no me ha ___.", "contestado", "protestado", "Je lui ai écrit il y a une semaine et il ne m'a toujours pas répondu.", "I wrote to him a week ago and he still hasn't answered me.", "contestar = répondre. Contester se dit protestar ou impugnar.", "contestar = to answer, not to contest."),
 ("Para la boda, Ana se compró ___ de seda.", "un vestido", "una ropa", "Pour le mariage, Ana s'est acheté une robe en soie.", "For the wedding, Ana bought herself a silk dress.", "Une robe = un vestido. la ropa = les vêtements en général.", "A dress = un vestido. la ropa = clothes in general."),
 ("Mis ___ viven en Lyon: mi madre y mi padre.", "padres", "parientes", "Mes parents vivent à Lyon : ma mère et mon père.", "My parents live in Lyon: my mother and my father.", "Les parents (père et mère) = los padres. los parientes = la famille élargie.", "Parents = los padres. los parientes = relatives."),
 ("Ella ___ su trabajo el año pasado.", "dejó", "quitó", "Elle a quitté son travail l'an dernier.", "She left her job last year.", "Quitter = dejar (ou salir de). quitar = enlever.", "To leave = dejar. quitar = to take off, remove."),
 ("___ los zapatos antes de entrar.", "Quítate", "Déjate", "Enlève tes chaussures avant d'entrer.", "Take your shoes off before coming in.", "quitar = enlever. quitarse los zapatos = enlever ses chaussures.", "quitar = to remove. quitarse los zapatos = to take your shoes off."),
 ("La enfermera ___ a los pacientes con mucha paciencia.", "atiende", "espera", "L'infirmière s'occupe des patients avec beaucoup de patience.", "The nurse looks after the patients very patiently.", "atender = s'occuper de, servir. Attendre se dit esperar.", "atender = to look after, to serve. To wait is esperar."),
 ("Te ___ en la parada del autobús.", "espero", "atiendo", "Je t'attends à l'arrêt de bus.", "I'll wait for you at the bus stop.", "Attendre = esperar. atender = s'occuper de.", "To wait = esperar. atender = to attend to."),
 ("La empresa ___ grandes pérdidas.", "sufrió", "subió", "L'entreprise a subi de grosses pertes.", "The company suffered heavy losses.", "Subir (au sens de supporter) = sufrir. subir = monter.", "To suffer = sufrir. subir = to go up."),
 ("___ al tercer piso por la escalera.", "Subí", "Monté", "Je suis monté au troisième étage par l'escalier.", "I went up to the third floor by the stairs.", "Monter (un escalier, un étage) = subir. montar = monter à cheval, assembler.", "To go up = subir. montar = to ride, to assemble."),
 ("Me cuesta ___ lo que siento.", "expresar", "exprimir", "J'ai du mal à exprimer ce que je ressens.", "I find it hard to express what I feel.", "Exprimer = expresar. exprimir = presser (un fruit).", "To express = expresar. exprimir = to squeeze."),
 ("___ un limón sobre el pescado.", "Exprime", "Expresa", "Presse un citron sur le poisson.", "Squeeze a lemon over the fish.", "exprimir = presser un fruit. Exprimer, c'est expresar.", "exprimir = to squeeze. To express is expresar."),
 ("Pon las flores en el ___.", "florero", "vaso", "Mets les fleurs dans le vase.", "Put the flowers in the vase.", "Un vase = un florero (ou un jarrón). un vaso = un verre.", "A vase = un florero. un vaso = a glass."),
 ("¿Cuál es tu ___ de teléfono?", "número", "nombre", "Quel est ton numéro de téléphone ?", "What's your phone number?", "Un nombre, un numéro = un número. el nombre = le nom, le prénom.", "A number = un número. el nombre = the name."),
 ("El semáforo está en ___.", "rojo", "rubio", "Le feu est au rouge.", "The traffic light is red.", "Rouge = rojo. rubio = blond.", "Red = rojo. rubio = blond."),
 ("¿Puedo pagar con ___?", "tarjeta", "carta", "Je peux payer par carte ?", "Can I pay by card?", "Une carte (bancaire, de visite) = una tarjeta. una carta = une lettre, ou le menu.", "A card = una tarjeta. una carta = a letter, or the menu."),
 ("Me escribió una ___ de amor.", "carta", "tarjeta", "Il m'a écrit une lettre d'amour.", "He wrote me a love letter.", "Une lettre = una carta.", "A letter = una carta."),
 ("Mi padre cobra la ___ desde 2020.", "jubilación", "retirada", "Mon père touche sa retraite depuis 2020.", "My father has been drawing his pension since 2020.", "La retraite (du travail) = la jubilación. una retirada = un retrait, un repli.", "Retirement, pension = la jubilación. una retirada = a withdrawal."),
 ("Viven en una ___ con vacas y gallinas.", "granja", "firma", "Ils vivent dans une ferme avec des vaches et des poules.", "They live on a farm with cows and hens.", "Une ferme = una granja. una firma = une signature.", "A farm = una granja. una firma = a signature."),
 ("Hace frío: ponte el ___.", "abrigo", "mantel", "Il fait froid : mets ton manteau.", "It's cold: put your coat on.", "Un manteau = un abrigo. un mantel = une nappe.", "A coat = un abrigo. un mantel = a tablecloth."),
 ("Pon el ___ en la mesa antes de comer.", "mantel", "abrigo", "Mets la nappe sur la table avant de manger.", "Put the tablecloth on the table before eating.", "mantel = nappe. Pas un manteau !", "mantel = tablecloth."),
 ("Me duele la ___ derecha.", "pierna", "gamba", "J'ai mal à la jambe droite.", "My right leg hurts.", "La jambe = la pierna. una gamba = une crevette.", "The leg = la pierna. una gamba = a prawn."),
 ("No te ___: habla más alto.", "oigo", "entiendo", "Je ne t'entends pas : parle plus fort.", "I can't hear you: speak louder.", "Entendre = oír. entender = comprendre.", "To hear = oír. entender = to understand."),
 ("No ___ esta palabra: ¿qué significa?", "entiendo", "oigo", "Je ne comprends pas ce mot : qu'est-ce qu'il veut dire ?", "I don't understand this word: what does it mean?", "entender = comprendre, pas entendre.", "entender = to understand."),
 ("En enero hay ___ en todas las tiendas.", "rebajas", "sueldos", "En janvier, il y a des soldes dans tous les magasins.", "In January, there are sales in every shop.", "Les soldes = las rebajas. el sueldo = le salaire.", "Sales = las rebajas. el sueldo = the salary."),
 ("Este pan no lleva ___.", "conservantes", "preservativos", "Ce pain ne contient pas de conservateurs.", "This bread has no preservatives.", "Conservateurs = conservantes. preservativos = préservatifs !", "Preservatives = conservantes. preservativos = condoms!"),
 ("El presidente ___ es muy joven.", "actual", "real", "Le président actuel est très jeune.", "The current president is very young.", "actual = actuel. real = réel, ou royal.", "actual = current, not actual. real = real, or royal."),
 ("En ___, no sé nada de él.", "realidad", "actualidad", "En réalité, je ne sais rien de lui.", "Actually, I know nothing about him.", "En réalité = en realidad. la actualidad = l'actualité.", "Actually = en realidad. la actualidad = current affairs."),
 ("Voy a ___ el partido para verlo luego.", "grabar", "registrar", "Je vais enregistrer le match pour le regarder plus tard.", "I'm going to record the match to watch it later.", "Enregistrer (un son, une vidéo) = grabar. registrar = fouiller, ou inscrire.", "To record = grabar. registrar = to search, or to register."),
 ("La policía ___ la casa del sospechoso.", "registró", "grabó", "La police a fouillé la maison du suspect.", "The police searched the suspect's house.", "registrar = fouiller (une maison, un sac).", "registrar = to search (a house, a bag)."),
 ("Mi padre trabaja en una ___ de coches.", "fábrica", "tela", "Mon père travaille dans une usine de voitures.", "My father works in a car factory.", "Une usine = una fábrica.", "A factory = una fábrica, not fabric."),
 ("Esta camisa es de una ___ muy suave.", "tela", "fábrica", "Cette chemise est faite d'un tissu très doux.", "This shirt is made of a very soft fabric.", "Un tissu = una tela. una fábrica = une usine.", "Fabric = una tela. una fábrica = a factory."),
 ("Mañana hay una ___ sobre arte en la universidad.", "conferencia", "lectura", "Demain, il y a une conférence sur l'art à l'université.", "Tomorrow there's a lecture on art at the university.", "Une conférence = una conferencia. la lectura = la lecture (lire).", "A lecture = una conferencia. la lectura = reading."),
 ("La ___ es mi pasatiempo favorito.", "lectura", "conferencia", "La lecture est mon passe-temps préféré.", "Reading is my favourite pastime.", "La lecture = la lectura.", "Reading = la lectura, not a lecture."),
 ("Te ___ a mi novia, Laura.", "presento", "introduzco", "Je te présente ma copine, Laura.", "Let me introduce my girlfriend, Laura.", "Présenter quelqu'un = presentar. introducir = insérer.", "To introduce someone = presentar. introducir = to insert."),
 ("___ la tarjeta en el cajero.", "Introduce", "Presenta", "Insère la carte dans le distributeur.", "Insert the card into the cash machine.", "introducir = insérer, faire entrer.", "introducir = to insert."),
 ("Estoy muy ___ por el viaje a México.", "emocionado", "excitado", "J'ai vraiment hâte de faire le voyage au Mexique.", "I'm really excited about the trip to Mexico.", "Enthousiaste, impatient = emocionado. excitado a souvent un sens sexuel.", "Excited = emocionado. excitado is usually sexual."),
 ("El periódico cuenta un ___ terrible.", "suceso", "éxito", "Le journal raconte un fait divers terrible.", "The newspaper reports a terrible incident.", "un suceso = un événement, un fait divers. Le succès = el éxito.", "un suceso = an incident. Success = el éxito."),
 ("La empresa lo ___ por llegar siempre tarde.", "despidió", "reenvió", "L'entreprise l'a renvoyé parce qu'il arrivait toujours en retard.", "The company fired him for always arriving late.", "Renvoyer (licencier) = despedir. reenviar = renvoyer un courriel, un colis.", "To fire = despedir. reenviar = to forward, resend."),
 ("Hay ___ de Picasso en el salón.", "un cuadro", "una tabla", "Il y a un tableau de Picasso dans le salon.", "There's a Picasso painting in the living room.", "Un tableau (peinture) = un cuadro. una tabla = une planche, un tableau de chiffres.", "A painting = un cuadro. una tabla = a board, a table of figures."),
 ("¡Qué ___! La puerta estaba abierta y no hay nadie.", "raro", "bizarro", "Comme c'est bizarre ! La porte était ouverte et il n'y a personne.", "How strange! The door was open and nobody's here.", "Bizarre = raro. bizarro = courageux, vaillant.", "Strange = raro. bizarro = brave, gallant."),
 ("Por favor, ___ la luz al salir.", "apaga", "extingue", "S'il te plaît, éteins la lumière en sortant.", "Please turn off the light when you leave.", "Éteindre la lumière = apagar. extinguir = éteindre un incendie.", "To switch off = apagar. extinguir = to put out a fire."),
]

GUSTAR = [
 ("Me ___ el chocolate.", "gusta", "gustan", "J'aime le chocolat.", "I like chocolate.", "Le verbe s'accorde avec ce qui plaît : el chocolate, singulier.", "The verb agrees with what is liked: el chocolate, singular."),
 ("Me ___ los perros.", "gustan", "gusta", "J'aime les chiens.", "I like dogs.", "los perros, pluriel → gustan.", "los perros, plural → gustan."),
 ("Nos ___ bailar.", "gusta", "gustan", "Nous aimons danser.", "We like dancing.", "Devant un infinitif : toujours au singulier.", "Before an infinitive: always singular."),
 ("Me ___ bailar y cantar.", "gusta", "gustan", "J'aime danser et chanter.", "I like dancing and singing.", "Même avec deux infinitifs, gustar reste au singulier.", "Even with two infinitives, gustar stays singular."),
 ("___ la música.", "Me gusta", "Yo gusto", "J'aime la musique.", "I like music.", "On ne dit pas « je plais » : la musique ME plaît → me gusta.", "Not « I please »: music pleases ME → me gusta."),
 ("A mi madre ___ gusta el té.", "le", "la", "Ma mère aime le thé.", "My mother likes tea.", "La personne qui aime passe par le (à elle, à lui).", "The person who likes takes le (to her, to him)."),
 ("A mis padres ___ gusta viajar.", "les", "le", "Mes parents aiment voyager.", "My parents like travelling.", "Plusieurs personnes → les.", "Several people → les."),
 ("A nosotros ___ gusta cocinar.", "nos", "nosotros", "Nous, on aime cuisiner.", "We like cooking.", "« A nosotros » insiste ; le pronom nos reste obligatoire.", "« A nosotros » adds emphasis; the pronoun nos is still required."),
 ("¿A ti ___ gusta el cine?", "te", "tú", "Et toi, tu aimes le cinéma ?", "Do you like the cinema?", "à toi → te gusta.", "to you → te gusta."),
 ("¿A usted ___ gusta el café?", "le", "lo", "Vous aimez le café ?", "Do you like coffee?", "usted prend le, comme él et ella.", "usted takes le, like él and ella."),
 ("A Pedro y a Luis les ___ el tenis.", "gusta", "gustan", "Pedro et Luis aiment le tennis.", "Pedro and Luis like tennis.", "Le piège : deux personnes, mais une seule chose aimée (el tenis) → gusta.", "The trap: two people, but one thing liked (el tenis) → gusta."),
 ("A Ana no le ___ nada las verduras.", "gustan", "gusta", "Ana n'aime pas du tout les légumes.", "Ana doesn't like vegetables at all.", "las verduras, pluriel → gustan.", "las verduras, plural → gustan."),
 ("A los niños les ___ los dulces.", "gustan", "gusta", "Les enfants aiment les sucreries.", "Children like sweets.", "los dulces → gustan.", "los dulces → gustan."),
 ("A ella le ___ los gatos, pero a mí no.", "gustan", "gusta", "Elle aime les chats, mais pas moi.", "She likes cats, but I don't.", "los gatos → gustan.", "los gatos → gustan."),
 ("A mí me gusta el té, ¿y a ti te ___?", "gusta", "gustas", "Moi, j'aime le thé, et toi ?", "I like tea, and do you?", "Toujours le thé qui plaît → gusta, pas gustas.", "It's still the tea that pleases → gusta, not gustas."),
 ("A todos nos ___ las vacaciones.", "gustan", "gusta", "Tout le monde aime les vacances.", "We all like holidays.", "las vacaciones → gustan.", "las vacaciones → gustan."),
 ("¿A quién le ___ el café sin azúcar?", "gusta", "gustan", "Qui aime le café sans sucre ?", "Who likes coffee without sugar?", "el café → gusta.", "el café → gusta."),
 ("Ayer me ___ mucho la fiesta.", "gustó", "gusté", "Hier, la fête m'a beaucoup plu.", "I really enjoyed the party yesterday.", "Au passé aussi, on accorde avec la fête : gustó.", "In the past too, it agrees with the party: gustó."),
 ("Anoche nos ___ mucho los platos del restaurante.", "gustaron", "gustó", "Hier soir, les plats du restaurant nous ont beaucoup plu.", "Last night we really liked the dishes at the restaurant.", "los platos, pluriel → gustaron.", "los platos, plural → gustaron."),
 ("Cuando era niño, me ___ jugar en el parque.", "gustaba", "gustaban", "Quand j'étais enfant, j'aimais jouer au parc.", "When I was a child, I liked playing in the park.", "Un infinitif → singulier, ici à l'imparfait.", "An infinitive → singular, here in the imperfect."),
 ("De joven me ___ los conciertos de rock.", "gustaban", "gustaba", "Jeune, j'aimais les concerts de rock.", "When I was young I liked rock concerts.", "los conciertos → gustaban.", "los conciertos → gustaban."),
 ("¿Te ___ venir conmigo al cine?", "gustaría", "gustarías", "Tu aimerais venir au cinéma avec moi ?", "Would you like to come to the cinema with me?", "Le conditionnel suit la même règle : venir → gustaría.", "The conditional follows the same rule: venir → gustaría."),
 ("Me ___ unos zapatos nuevos.", "gustarían", "gustaría", "J'aimerais bien des chaussures neuves.", "I'd like some new shoes.", "unos zapatos, pluriel → gustarían.", "unos zapatos, plural → gustarían."),
 ("Me ___ que vinieras a mi fiesta.", "encantaría", "encantarías", "Ça me ferait très plaisir que tu viennes à ma fête.", "I'd love you to come to my party.", "Ce qui plaît, c'est « que tu viennes » → singulier.", "What pleases is « that you come » → singular."),
 ("Tú me ___ mucho.", "gustas", "gusta", "Tu me plais beaucoup.", "I like you a lot.", "Ici c'est toi qui plais : tú → gustas.", "Here it's you who pleases: tú → gustas."),
 ("Yo le ___ a María.", "gusto", "gusta", "Je plais à María.", "María likes me.", "C'est moi qui plais : yo → gusto.", "It's me who pleases: yo → gusto."),
 ("Nos ___ tu idea.", "encanta", "encantamos", "Ton idée nous plaît beaucoup.", "We love your idea.", "On accorde avec tu idea, pas avec nosotros.", "It agrees with tu idea, not with nosotros."),
 ("Nos ___ México.", "encanta", "encantan", "Nous adorons le Mexique.", "We love Mexico.", "México, singulier → encanta.", "México, singular → encanta."),
 ("A mis hermanos les ___ los videojuegos.", "encantan", "encanta", "Mes frères adorent les jeux vidéo.", "My brothers love video games.", "los videojuegos → encantan.", "los videojuegos → encantan."),
 ("Les ___ bailar salsa.", "encanta", "encantan", "Ils adorent danser la salsa.", "They love dancing salsa.", "Un infinitif → singulier, même si « ils » sont plusieurs.", "An infinitive → singular, even if « they » are many."),
 ("A los turistas les ___ la playa.", "encanta", "encantan", "Les touristes adorent la plage.", "Tourists love the beach.", "la playa → encanta.", "la playa → encanta."),
 ("Me ___ los pies.", "duelen", "duele", "J'ai mal aux pieds.", "My feet hurt.", "doler fonctionne comme gustar : los pies → duelen.", "doler works like gustar: los pies → duelen."),
 ("¿Te ___ la cabeza?", "duele", "duelen", "Tu as mal à la tête ?", "Does your head hurt?", "la cabeza → duele.", "la cabeza → duele."),
 ("Me ___ los ojos de tanto leer.", "duelen", "duele", "J'ai mal aux yeux à force de lire.", "My eyes hurt from reading so much.", "los ojos → duelen.", "los ojos → duelen."),
 ("Me ___ la espalda desde ayer.", "duele", "duelen", "J'ai mal au dos depuis hier.", "My back has hurt since yesterday.", "la espalda → duele.", "la espalda → duele."),
 ("A mi padre ___ duelen las rodillas.", "le", "lo", "Mon père a mal aux genoux.", "My father's knees hurt.", "à lui → le, comme avec gustar.", "to him → le, as with gustar."),
 ("¿Cuánto te ___ la muela?", "duele", "dueles", "Tu as mal à quel point à la dent ?", "How much does your tooth hurt?", "C'est la dent qui fait mal → duele.", "It's the tooth that hurts → duele."),
 ("A mi abuela le ___ las manos cuando hace frío.", "duelen", "duele", "Ma grand-mère a mal aux mains quand il fait froid.", "My grandmother's hands hurt when it's cold.", "las manos → duelen.", "las manos → duelen."),
 ("A Juan le ___ dos euros para el billete.", "faltan", "falta", "Il manque deux euros à Juan pour le billet.", "Juan is two euros short for the ticket.", "faltar comme gustar : dos euros → faltan.", "faltar works like gustar: dos euros → faltan."),
 ("Me ___ tres páginas para terminar el libro.", "faltan", "falta", "Il me reste trois pages pour finir le livre.", "I have three pages left to finish the book.", "tres páginas → faltan.", "tres páginas → faltan."),
 ("Les ___ experiencia.", "falta", "faltan", "Ils manquent d'expérience.", "They lack experience.", "experiencia, singulier → falta.", "experiencia, singular → falta."),
 ("Nos ___ poco tiempo.", "queda", "quedan", "Il nous reste peu de temps.", "We have little time left.", "quedar (rester) comme gustar : poco tiempo → queda.", "quedar (to be left) like gustar: poco tiempo → queda."),
 ("Me ___ grandes estos pantalones.", "quedan", "queda", "Ce pantalon est trop grand pour moi.", "These trousers are too big for me.", "estos pantalones, pluriel en espagnol → quedan.", "estos pantalones, plural → quedan."),
 ("A ella le ___ muy bien el rojo.", "queda", "quedas", "Le rouge lui va très bien.", "Red really suits her.", "el rojo → queda.", "el rojo → queda."),
 ("A ellos les ___ el fútbol.", "interesa", "interesan", "Le foot les intéresse.", "They're interested in football.", "el fútbol → interesa.", "el fútbol → interesa."),
 ("Le ___ la historia del arte.", "interesa", "interesan", "L'histoire de l'art l'intéresse.", "She's interested in art history.", "la historia → interesa.", "la historia → interesa."),
 ("A nosotros nos ___ las estrellas.", "fascinan", "fascina", "Les étoiles nous fascinent.", "Stars fascinate us.", "las estrellas → fascinan.", "las estrellas → fascinan."),
 ("A mí me ___ mucho los ruidos fuertes.", "molestan", "molesta", "Les bruits forts me dérangent beaucoup.", "Loud noises really bother me.", "los ruidos → molestan.", "los ruidos → molestan."),
 ("¿Te ___ el humo?", "molesta", "molestas", "La fumée te dérange ?", "Does the smoke bother you?", "C'est la fumée qui dérange → molesta.", "It's the smoke that bothers → molesta."),
 ("Le ___ mucho su salud.", "preocupa", "preocupan", "Sa santé l'inquiète beaucoup.", "He's very worried about his health.", "su salud → preocupa.", "su salud → preocupa."),
 ("Me ___ mis exámenes.", "preocupan", "preocupa", "Mes examens m'inquiètent.", "I'm worried about my exams.", "mis exámenes → preocupan.", "mis exámenes → preocupan."),
 ("No me ___ los detalles.", "importan", "importa", "Les détails ne m'importent pas.", "I don't care about the details.", "los detalles → importan.", "los detalles → importan."),
 ("¿Te ___ si abro la ventana?", "importa", "importas", "Ça te dérange si j'ouvre la fenêtre ?", "Do you mind if I open the window?", "Ce qui importe, c'est « si j'ouvre » → singulier.", "What matters is « if I open » → singular."),
 ("¿Qué te ___ mis zapatos nuevos?", "parecen", "parece", "Comment tu trouves mes nouvelles chaussures ?", "What do you think of my new shoes?", "parecer comme gustar : mis zapatos → parecen.", "parecer like gustar: mis zapatos → parecen."),
 ("Me ___ bien tu plan.", "parece", "parezco", "Ton plan me paraît bien.", "Your plan sounds good to me.", "tu plan → parece.", "tu plan → parece."),
 ("Me ___ bien tu hermano.", "cae", "caigo", "Ton frère m'est sympathique.", "I like your brother.", "caer bien = être sympathique à quelqu'un : tu hermano → cae.", "caer bien = to be likeable to someone: tu hermano → cae."),
 ("Me ___ bien tus amigos.", "caen", "cae", "Tes amis me sont sympathiques.", "I like your friends.", "tus amigos → caen.", "tus amigos → caen."),
]

ACENTOS = [
 ("¿___ quieres café?", "Tú", "Tu", "Tu veux du café ?", "Do you want coffee?", "tú (avec accent) = toi, le pronom.", "tú (with accent) = you, the pronoun."),
 ("___ casa es muy bonita.", "Tu", "Tú", "Ta maison est très jolie.", "Your house is very pretty.", "tu (sans accent) = ton, ta.", "tu (no accent) = your."),
 ("___ coche es nuevo.", "El", "Él", "La voiture est neuve.", "The car is new.", "el (sans accent) = l'article le.", "el (no accent) = the article « the »."),
 ("Este regalo es para ___.", "él", "el", "Ce cadeau est pour lui.", "This present is for him.", "él (avec accent) = lui.", "él (with accent) = he, him."),
 ("___ llueve, no salgo.", "Si", "Sí", "S'il pleut, je ne sors pas.", "If it rains, I'm not going out.", "si (sans accent) = si, la condition.", "si (no accent) = if."),
 ("—¿Vienes? —___, claro.", "Sí", "Si", "— Tu viens ? — Oui, bien sûr.", "— Are you coming? — Yes, of course.", "sí (avec accent) = oui.", "sí (with accent) = yes."),
 ("Solo piensa en ___ mismo.", "sí", "si", "Il ne pense qu'à lui-même.", "He only thinks about himself.", "sí (avec accent) = soi, lui-même.", "sí (with accent) = himself, oneself."),
 ("Este libro es para ___.", "mí", "mi", "Ce livre est pour moi.", "This book is for me.", "mí (avec accent) = moi, après une préposition.", "mí (with accent) = me, after a preposition."),
 ("___ hermano vive en Lima.", "Mi", "Mí", "Mon frère vit à Lima.", "My brother lives in Lima.", "mi (sans accent) = mon, ma.", "mi (no accent) = my."),
 ("¿Quieres un ___?", "té", "te", "Tu veux un thé ?", "Would you like a tea?", "té (avec accent) = le thé.", "té (with accent) = tea."),
 ("___ llamo mañana.", "Te", "Té", "Je t'appelle demain.", "I'll call you tomorrow.", "te (sans accent) = te, le pronom.", "te (no accent) = you, the object pronoun."),
 ("No ___ dónde está.", "sé", "se", "Je ne sais pas où il est.", "I don't know where it is.", "sé (avec accent) = je sais (saber).", "sé (with accent) = I know (saber)."),
 ("Ella ___ levanta a las siete.", "se", "sé", "Elle se lève à sept heures.", "She gets up at seven.", "se (sans accent) = se, le pronom.", "se (no accent) = the reflexive pronoun."),
 ("Quiero ___ pan, por favor.", "más", "mas", "Je veux plus de pain, s'il te plaît.", "I want more bread, please.", "más (avec accent) = plus.", "más (with accent) = more."),
 ("Es la casa ___ mi tía.", "de", "dé", "C'est la maison de ma tante.", "It's my aunt's house.", "de (sans accent) = de, la préposition.", "de (no accent) = of, from."),
 ("Quiero que me ___ su número.", "dé", "de", "Je veux qu'il me donne son numéro.", "I want him to give me his number.", "dé (avec accent) = qu'il donne (dar, subjonctif).", "dé (with accent) = give (dar, subjunctive)."),
 ("¿___ hora es?", "Qué", "Que", "Quelle heure est-il ?", "What time is it?", "Dans une question, qué porte un accent.", "In a question, qué takes an accent."),
 ("Creo ___ va a llover.", "que", "qué", "Je crois qu'il va pleuvoir.", "I think it's going to rain.", "que (sans accent) relie deux phrases.", "que (no accent) links two clauses: « that »."),
 ("No sé ___ hacer.", "qué", "que", "Je ne sais pas quoi faire.", "I don't know what to do.", "Question indirecte → qué garde son accent.", "Indirect question → qué keeps its accent."),
 ("El libro ___ compré es muy bueno.", "que", "qué", "Le livre que j'ai acheté est très bon.", "The book I bought is very good.", "Pronom relatif → que, sans accent.", "Relative pronoun → que, no accent."),
 ("¿___ te llamas?", "Cómo", "Como", "Comment tu t'appelles ?", "What's your name?", "Question → cómo, avec accent.", "Question → cómo, with accent."),
 ("___ no tenía dinero, no fui.", "Como", "Cómo", "Comme je n'avais pas d'argent, je n'y suis pas allé.", "As I had no money, I didn't go.", "como (sans accent) = comme, puisque.", "como (no accent) = as, since."),
 ("No sé ___ se dice en español.", "cómo", "como", "Je ne sais pas comment on le dit en espagnol.", "I don't know how to say it in Spanish.", "Question indirecte → cómo.", "Indirect question → cómo."),
 ("¿___ vives?", "Dónde", "Donde", "Où habites-tu ?", "Where do you live?", "Question → dónde.", "Question → dónde."),
 ("Esta es la casa ___ nací.", "donde", "dónde", "Voici la maison où je suis né.", "This is the house where I was born.", "Relatif → donde, sans accent.", "Relative → donde, no accent."),
 ("¿___ llegas?", "Cuándo", "Cuando", "Quand est-ce que tu arrives ?", "When are you arriving?", "Question → cuándo.", "Question → cuándo."),
 ("___ llegues, llámame.", "Cuando", "Cuándo", "Quand tu arriveras, appelle-moi.", "When you arrive, call me.", "Pas une question → cuando, sans accent.", "Not a question → cuando, no accent."),
 ("¿___ cuesta este libro?", "Cuánto", "Cuanto", "Combien coûte ce livre ?", "How much does this book cost?", "Question → cuánto.", "Question → cuánto."),
 ("¿___ es ese chico?", "Quién", "Quien", "Qui est ce garçon ?", "Who is that boy?", "Question → quién.", "Question → quién."),
 ("¿___ no vienes?", "Por qué", "Porque", "Pourquoi tu ne viens pas ?", "Why aren't you coming?", "La question : por qué, en deux mots, avec accent.", "The question: por qué, two words, with accent."),
 ("No voy ___ estoy cansado.", "porque", "por qué", "Je n'y vais pas parce que je suis fatigué.", "I'm not going because I'm tired.", "La réponse : porque, en un mot, sans accent.", "The answer: porque, one word, no accent."),
 ("___ no ha llegado.", "Aún", "Aun", "Il n'est pas encore arrivé.", "He hasn't arrived yet.", "aún (avec accent) = encore, toujours (todavía).", "aún (with accent) = still, yet (todavía)."),
 ("___ así, no lo creo.", "Aun", "Aún", "Même comme ça, je ne le crois pas.", "Even so, I don't believe it.", "aun (sans accent) = même (incluso).", "aun (no accent) = even (incluso)."),
 ("Mi madre ___ en casa.", "está", "esta", "Ma mère est à la maison.", "My mother is at home.", "está (avec accent) = elle est (estar).", "está (with accent) = she is (estar)."),
 ("___ casa es grande.", "Esta", "Está", "Cette maison est grande.", "This house is big.", "esta (sans accent) = cette.", "esta (no accent) = this."),
 ("Ojalá ___ bien tu abuela.", "esté", "este", "Pourvu que ta grand-mère aille bien.", "I hope your grandmother is well.", "esté (avec accent) = subjonctif d'estar.", "esté (with accent) = estar in the subjunctive."),
 ("Ayer Juan ___ con el jefe.", "habló", "hablo", "Hier, Juan a parlé avec le chef.", "Yesterday Juan spoke to the boss.", "habló = il a parlé. hablo = je parle.", "habló = he spoke. hablo = I speak."),
 ("Yo ___ español todos los días.", "hablo", "habló", "Je parle espagnol tous les jours.", "I speak Spanish every day.", "hablo = je parle (présent).", "hablo = I speak (present)."),
 ("Ayer ella ___ a las ocho.", "llegó", "llego", "Hier, elle est arrivée à huit heures.", "Yesterday she arrived at eight.", "llegó = elle est arrivée.", "llegó = she arrived."),
 ("Normalmente ___ al trabajo a las ocho.", "llego", "llegó", "D'habitude, j'arrive au travail à huit heures.", "I usually get to work at eight.", "llego = j'arrive.", "llego = I arrive."),
 ("Mi padre ___ en Francia en 1990.", "trabajó", "trabajo", "Mon père a travaillé en France en 1990.", "My father worked in France in 1990.", "trabajó = il a travaillé.", "trabajó = he worked."),
 ("Ahora ___ en una oficina.", "trabajo", "trabajó", "Maintenant, je travaille dans un bureau.", "Now I work in an office.", "trabajo = je travaille (ou : le travail).", "trabajo = I work (or: work, the noun)."),
 ("El año pasado ___ un libro.", "publicó", "publico", "L'an dernier, il a publié un livre.", "Last year he published a book.", "publicó = il a publié.", "publicó = he published."),
 ("Yo ___ yoga los lunes.", "practico", "práctico", "Je fais du yoga le lundi.", "I do yoga on Mondays.", "practico = je pratique. práctico = pratique (adjectif).", "practico = I practise. práctico = practical."),
 ("Este bolso es muy ___.", "práctico", "practico", "Ce sac est très pratique.", "This bag is very practical.", "práctico = pratique, l'adjectif.", "práctico = practical, the adjective."),
 ("Mañana ___ con el proyecto.", "continúo", "continuo", "Demain, je continue le projet.", "Tomorrow I'll carry on with the project.", "continúo = je continue.", "continúo = I continue."),
 ("Hay un ruido ___ en la calle.", "continuo", "continúo", "Il y a un bruit continu dans la rue.", "There's a constant noise in the street.", "continuo = continu, l'adjectif.", "continuo = continuous, the adjective."),
 ("Te ___ a seguir estudiando.", "animo", "ánimo", "Je t'encourage à continuer d'étudier.", "I encourage you to keep studying.", "animo = j'encourage. ánimo = le courage, l'entrain.", "animo = I encourage. ánimo = spirit, courage."),
 ("Mi ___ trabaja en un banco.", "papá", "papa", "Mon papa travaille dans une banque.", "My dad works in a bank.", "papá = papa (le père). el papa = le pape.", "papá = dad. el papa = the pope."),
 ("El ___ vive en el Vaticano.", "papa", "papá", "Le pape vit au Vatican.", "The pope lives in the Vatican.", "el papa = le pape.", "el papa = the pope."),
 ("Hablo ___ y francés.", "inglés", "ingles", "Je parle anglais et français.", "I speak English and French.", "inglés = anglais. ingles = les aines !", "inglés = English. ingles = groins!"),
 ("Cambia las ___ de la cama.", "sábanas", "sabanas", "Change les draps du lit.", "Change the sheets on the bed.", "sábanas = draps. sabanas = savanes.", "sábanas = sheets. sabanas = savannahs."),
 ("El ___ pasa por el centro de la ciudad.", "río", "rio", "Le fleuve traverse le centre-ville.", "The river runs through the city centre.", "río = le fleuve, la rivière. rio = il a ri (reír).", "río = river. rio = he laughed (reír)."),
]

INDICE = {
    "falsos": ("(le mot qui ressemble au français est souvent le piège)",
               "(the word that looks familiar is often the trap)"),
    "gustar": ("(le verbe s'accorde avec ce qui plaît, pas avec la personne)",
               "(the verb agrees with what is liked, not with the person)"),
    "acentos": ("(ici l'accent change le sens du mot)",
                "(here the accent changes the meaning)"),
}


def construire(lignes, sujet, indice):
    out = []
    for q, bon, autre, tfr, ten, efr, een in lignes:
        assert q.count("___") == 1, q
        assert bon != autre, q
        # Ordre FIXE, alphabetique : la place des options ne doit pas
        # trahir la reponse.
        opts = sorted([bon, autre], key=lambda x: (x.lower(), x))
        out.append({
            "topic": sujet, "question": q, "question_en": q,
            "translation": tfr, "translation_en": ten,
            "hint": indice[0], "hint_en": indice[1],
            "answers": [bon], "correct": bon, "correctEn": bon,
            "explanation": efr, "explanation_en": een,
            "options": opts, "optionsEn": opts,
        })
    return out


def main():
    jeux = (("falsosAmigosExercises", FAUX_AMIS, "falsos amigos", INDICE["falsos"]),
            ("gustarExercises", GUSTAR, "gustar", INDICE["gustar"]),
            ("acentosExercises", ACENTOS, "acentos", INDICE["acentos"]))
    d = json.load(io.open(CHEMIN, encoding="utf-8"))
    for nom, lignes, sujet, indice in jeux:
        assert len(lignes) >= 50, (nom, len(lignes))
        assert len({l[0] for l in lignes}) == len(lignes), "phrase en double dans " + nom
        d["jeux"][nom] = construire(lignes, sujet, indice)
    io.open(CHEMIN, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("   ".join("%s : %d" % (n, len(l)) for n, l, _, _ in jeux))


if __name__ == "__main__":
    main()
