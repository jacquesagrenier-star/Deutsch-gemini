# -*- coding: utf-8 -*-
"""Les exercices de paires de l'espagnol : ser / estar, por / para.

    python fusion-espagnol/exos_paires.py     # (re)ecrit les deux jeux dans espanol/datos/ejercicios.json

Recommandes par Gemini et ChatGPT (10 oct. 2026), et le plus gros manque de
l'espagnol : il n'avait que des exercices de conjugaison. Le meme mecanisme
que les duos allemands (weil / obwohl) : deux options, une seule juste, et
c'est le SENS qui tranche.

REGLES D'ECRITURE
  - Une seule reponse juste. Ecartes : « es / esta jubilado », « por / para
    Navidad », « va por / para el centro » -- les deux se disent.
  - La traduction ne souffle pas la reponse. Quand le francais dirait « par »
    (ou l'anglais « by », « through »), elle porte le meme trou que la phrase
    espagnole -- la lecon des duos allemands (v410).
  - Pas de vosotros : ces phrases servent aussi en Amerique latine.
Chaque ligne : (phrase avec ___, reponse, l'autre option, traduction fr,
traduction en, explication fr, explication en).
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "espanol", "datos", "ejercicios.json")

SER_ESTAR = [
 ("Mi hermana ___ enfermera.", "es", "está", "Ma sœur est infirmière.", "My sister is a nurse.", "Un métier : ce qu'elle EST → ser.", "A profession: what she IS → ser."),
 ("Mi hermana ___ cansada hoy.", "está", "es", "Ma sœur est fatiguée aujourd'hui.", "My sister is tired today.", "Un état passager → estar.", "A passing state → estar."),
 ("Madrid ___ en España.", "está", "es", "Madrid est en Espagne.", "Madrid is in Spain.", "Le lieu prend estar, même quand il ne change jamais.", "Location takes estar, even when it never changes."),
 ("La fiesta ___ en casa de Ana.", "es", "está", "La fête est chez Ana.", "The party is at Ana's.", "Un ÉVÉNEMENT : l'endroit où il a lieu prend ser.", "An EVENT: where it takes place takes ser."),
 ("___ las tres de la tarde.", "Son", "Están", "Il est trois heures de l'après-midi.", "It's three in the afternoon.", "L'heure → ser.", "The time → ser."),
 ("Yo ___ canadiense.", "soy", "estoy", "Je suis canadien.", "I'm Canadian.", "L'origine, la nationalité → ser.", "Origin, nationality → ser."),
 ("La mesa ___ de madera.", "es", "está", "La table est en bois.", "The table is made of wood.", "La matière → ser.", "Material → ser."),
 ("La sopa ___ fría, caliéntala.", "está", "es", "La soupe est froide, fais-la chauffer.", "The soup is cold, heat it up.", "Son état en ce moment → estar.", "Its state right now → estar."),
 ("Este chico ___ muy listo: siempre saca buenas notas.", "es", "está", "Ce garçon est très intelligent : il a toujours de bonnes notes.", "This boy is very clever: he always gets good marks.", "ser listo = être intelligent (une qualité).", "ser listo = to be clever (a quality)."),
 ("¿___ lista? Nos vamos.", "Estás", "Eres", "Tu es prête ? On y va.", "Are you ready? Let's go.", "estar listo = être prêt.", "estar listo = to be ready."),
 ("La película ___ aburrida: me dormí.", "es", "está", "Le film est ennuyeux : je me suis endormi.", "The film is boring: I fell asleep.", "ser aburrido = ennuyeux (une qualité du film).", "ser aburrido = boring (a quality of the film)."),
 ("Los niños ___ aburridos: no tienen nada que hacer.", "están", "son", "Les enfants s'ennuient : ils n'ont rien à faire.", "The children are bored: they have nothing to do.", "estar aburrido = s'ennuyer (un état).", "estar aburrido = to be bored (a state)."),
 ("Esta paella ___ muy rica.", "está", "es", "Cette paella est délicieuse.", "This paella is delicious.", "estar rico = être délicieux (au goût, maintenant).", "estar rico = to taste delicious (right now)."),
 ("Su familia ___ muy rica: tienen tres casas.", "es", "está", "Sa famille est très riche : ils ont trois maisons.", "Her family is very rich: they have three houses.", "ser rico = être riche.", "ser rico = to be wealthy."),
 ("Nosotros ___ en la biblioteca.", "estamos", "somos", "Nous sommes à la bibliothèque.", "We're at the library.", "Le lieu où l'on se trouve → estar.", "Where you are → estar."),
 ("Las llaves ___ en la mesa.", "están", "son", "Les clés sont sur la table.", "The keys are on the table.", "Le lieu d'un objet → estar.", "Where an object is → estar."),
 ("Mi padre ___ de mal humor esta mañana.", "está", "es", "Mon père est de mauvaise humeur ce matin.", "My father is in a bad mood this morning.", "L'humeur → estar.", "Mood → estar."),
 ("Ellos ___ hermanos.", "son", "están", "Ils sont frères.", "They're brothers.", "Un lien, une identité → ser.", "A relationship, an identity → ser."),
 ("Yo ___ estudiando español.", "estoy", "soy", "J'étudie l'espagnol (en ce moment).", "I'm studying Spanish.", "L'action en cours : estar + gérondif.", "An action in progress: estar + gerund."),
 ("Este libro ___ de mi abuela.", "es", "está", "Ce livre est à ma grand-mère.", "This book belongs to my grandmother.", "L'appartenance → ser.", "Possession → ser."),
 ("La tienda ___ cerrada.", "está", "es", "Le magasin est fermé.", "The shop is closed.", "Le résultat d'une action (on a fermé) → estar.", "The result of an action (someone closed it) → estar."),
 ("El concierto ___ mañana a las ocho.", "es", "está", "Le concert est demain à huit heures.", "The concert is tomorrow at eight.", "Un événement, sa date → ser.", "An event and its date → ser."),
 ("¿Cómo ___ tu madre? —Bien, gracias.", "está", "es", "Comment va ta mère ? — Bien, merci.", "How's your mother? — Fine, thanks.", "La santé, comment on va → estar.", "Health, how someone is doing → estar."),
 ("¿Cómo ___ tu madre? —Alta y muy simpática.", "es", "está", "Comment est ta mère ? — Grande et très sympathique.", "What's your mother like? — Tall and very nice.", "Comment elle EST (description) → ser.", "What she IS like (description) → ser."),
 ("Mi abuelo ___ muerto desde hace años.", "está", "es", "Mon grand-père est mort depuis des années.", "My grandfather has been dead for years.", "Le piège : estar muerto, même si c'est définitif.", "The trap: estar muerto, even though it's final."),
 ("La boda ___ en una iglesia del centro.", "es", "está", "Le mariage a lieu dans une église du centre.", "The wedding is in a church downtown.", "Un événement : où il a lieu → ser.", "An event: where it takes place → ser."),
 ("Hoy ___ muy guapa con ese vestido.", "estás", "eres", "Tu es très belle aujourd'hui avec cette robe.", "You look lovely today in that dress.", "Comment tu es AUJOURD'HUI → estar.", "How you look TODAY → estar."),
 ("El café ___ amargo; por eso le pongo azúcar.", "es", "está", "Le café est amer ; c'est pour ça que j'y mets du sucre.", "Coffee is bitter; that's why I add sugar.", "Une propriété du café en général → ser.", "A property of coffee in general → ser."),
 ("La ventana ___ abierta.", "está", "es", "La fenêtre est ouverte.", "The window is open.", "Un état résultant → estar.", "A resulting state → estar."),
 ("Ella ___ de vacaciones en México.", "está", "es", "Elle est en vacances au Mexique.", "She's on holiday in Mexico.", "estar de vacaciones : une situation passagère.", "estar de vacaciones: a temporary situation."),
 ("Cuando era niño, mi casa ___ muy pequeña.", "era", "estaba", "Quand j'étais enfant, ma maison était très petite.", "When I was a child, my house was very small.", "Une description dans le passé → ser (à l'imparfait).", "A description in the past → ser (imperfect)."),
 ("Ayer ___ enfermo y no fui a clase.", "estuve", "fui", "Hier j'étais malade et je ne suis pas allé en cours.", "Yesterday I was ill and didn't go to class.", "Un état (malade) → estar, même au passé.", "A state (ill) → estar, in the past too."),
 ("El agua del mar ___ salada.", "es", "está", "L'eau de mer est salée.", "Sea water is salty.", "Une propriété → ser.", "A property → ser."),
 ("Hoy el mar ___ muy tranquilo.", "está", "es", "Aujourd'hui la mer est très calme.", "The sea is very calm today.", "Son état aujourd'hui → estar.", "Its state today → estar."),
 ("Nosotros ___ de Montreal.", "somos", "estamos", "Nous sommes de Montréal.", "We're from Montreal.", "L'origine → ser.", "Origin → ser."),
 ("El partido ___ a las nueve.", "es", "está", "Le match est à neuf heures.", "The match is at nine.", "Un événement, son heure → ser.", "An event and its time → ser."),
 ("La comida ___ lista.", "está", "es", "Le repas est prêt.", "Lunch is ready.", "estar listo = être prêt.", "estar listo = to be ready."),
 ("Mi hermano ___ más alto que yo.", "es", "está", "Mon frère est plus grand que moi.", "My brother is taller than me.", "Une description physique → ser.", "A physical description → ser."),
 ("¿Dónde ___ el baño?", "está", "es", "Où sont les toilettes ?", "Where's the bathroom?", "Le lieu → estar.", "Location → estar."),
 ("Hoy ___ martes.", "es", "está", "Aujourd'hui, c'est mardi.", "Today is Tuesday.", "Le jour, la date → ser.", "The day, the date → ser."),
 ("El cielo ___ nublado esta mañana.", "está", "es", "Le ciel est nuageux ce matin.", "The sky is cloudy this morning.", "Un état du moment → estar.", "A state of the moment → estar."),
 ("Este anillo ___ de oro.", "es", "está", "Cette bague est en or.", "This ring is made of gold.", "La matière → ser.", "Material → ser."),
 ("Ana ___ embarazada de tres meses.", "está", "es", "Ana est enceinte de trois mois.", "Ana is three months pregnant.", "Un état → estar. Et un faux ami : embarazada = enceinte, pas « embarrassée ».", "A state → estar. And a false friend: embarazada = pregnant, not embarrassed."),
 ("Ese restaurante ___ muy caro.", "es", "está", "Ce restaurant est très cher.", "That restaurant is very expensive.", "Une caractéristique du restaurant → ser.", "A feature of the restaurant → ser."),
 ("Los tomates ___ verdes todavía; no se pueden comer.", "están", "son", "Les tomates ne sont pas encore mûres ; on ne peut pas les manger.", "The tomatoes aren't ripe yet; you can't eat them.", "estar verde = ne pas être mûr (un état). ser verde = être de couleur verte.", "estar verde = unripe (a state). ser verde = to be green in colour."),
 ("Mi coche ___ rojo.", "es", "está", "Ma voiture est rouge.", "My car is red.", "La couleur, une propriété → ser.", "Colour, a property → ser."),
 ("Yo ___ de acuerdo contigo.", "estoy", "soy", "Je suis d'accord avec toi.", "I agree with you.", "Une expression figée : estar de acuerdo.", "A set phrase: estar de acuerdo."),
 ("La conferencia ___ en el aula 3.", "es", "está", "La conférence a lieu dans la salle 3.", "The lecture is in room 3.", "Un événement : où il a lieu → ser.", "An event: where it takes place → ser."),
 ("El profesor ___ enfermo hoy.", "está", "es", "Le professeur est malade aujourd'hui.", "The teacher is ill today.", "Un état → estar.", "A state → estar."),
 ("Juan ___ muy simpático: todo el mundo lo quiere.", "es", "está", "Juan est très sympathique : tout le monde l'aime.", "Juan is very nice: everybody likes him.", "Le caractère → ser.", "Personality → ser."),
 ("___ muy contento con mi nuevo trabajo.", "Estoy", "Soy", "Je suis très content de mon nouveau travail.", "I'm very happy with my new job.", "Une émotion, un état → estar.", "An emotion, a state → estar."),
]

POR_PARA = [
 ("Este regalo es ___ ti.", "para", "por", "Ce cadeau est pour toi.", "This present is for you.", "Le destinataire → para.", "The recipient → para."),
 ("Gracias ___ tu ayuda.", "por", "para", "Merci pour ton aide.", "Thanks for your help.", "On remercie POUR quelque chose reçu : la cause → por.", "You thank someone FOR something received: the cause → por."),
 ("Estudio español ___ viajar a México.", "para", "por", "J'étudie l'espagnol pour voyager au Mexique.", "I'm studying Spanish to travel to Mexico.", "Le but (afin de) → para.", "The goal (in order to) → para."),
 ("Paseamos ___ el parque.", "por", "para", "Nous nous promenons dans le parc.", "We're walking around the park.", "Le passage, à travers → por.", "Movement through a place → por."),
 ("Salgo ___ Madrid mañana.", "para", "por", "Je pars pour Madrid demain.", "I'm leaving for Madrid tomorrow.", "La destination → para.", "The destination → para."),
 ("Te llamo ___ la mañana.", "por", "para", "Je t'appelle le matin.", "I'll call you in the morning.", "Le moment de la journée → por la mañana, por la tarde.", "Part of the day → por la mañana, por la tarde."),
 ("Necesito el informe ___ el lunes.", "para", "por", "J'ai besoin du rapport pour lundi.", "I need the report by Monday.", "L'échéance → para.", "The deadline → para."),
 ("Compré el coche ___ cinco mil euros.", "por", "para", "J'ai acheté la voiture cinq mille euros.", "I bought the car for five thousand euros.", "Le prix, l'échange → por.", "Price, exchange → por."),
 ("Lo hago ___ ti, porque te quiero.", "por", "para", "Je le fais pour toi, parce que je t'aime.", "I do it for your sake, because I love you.", "Tu es la RAISON (porque te quiero) → por.", "You're the REASON (porque te quiero) → por."),
 ("Me multaron ___ ir demasiado rápido.", "por", "para", "On m'a mis une amende pour excès de vitesse.", "I was fined for going too fast.", "La cause → por.", "The cause → por."),
 ("Entró ___ la ventana.", "por", "para", "Il est entré ___ la fenêtre.", "He came in ___ the window.", "Le passage (par la fenêtre) → por.", "The way through (through the window) → por."),
 ("___ mí, es la mejor película del año.", "Para", "Por", "Pour moi, c'est le meilleur film de l'année.", "For me, it's the best film of the year.", "L'opinion : para mí = à mon avis.", "Opinion: para mí = in my view."),
 ("Hay que estudiar mucho ___ aprobar.", "para", "por", "Il faut beaucoup étudier pour réussir.", "You have to study a lot to pass.", "Le but → para.", "The goal → para."),
 ("El tren ___ Barcelona sale a las diez.", "para", "por", "Le train pour Barcelone part à dix heures.", "The train to Barcelona leaves at ten.", "La destination → para.", "The destination → para."),
 ("Te mando la foto ___ correo electrónico.", "por", "para", "Je t'envoie la photo ___ courriel.", "I'm sending you the photo ___ email.", "Le moyen → por.", "The means → por."),
 ("Cambié mi bicicleta ___ una guitarra.", "por", "para", "J'ai échangé mon vélo contre une guitare.", "I swapped my bike for a guitar.", "L'échange → por.", "An exchange → por."),
 ("Este libro fue escrito ___ Cervantes.", "por", "para", "Ce livre a été écrit ___ Cervantes.", "This book was written ___ Cervantes.", "L'auteur d'un passif → por.", "The agent of a passive → por."),
 ("¿___ qué estudias español? —Porque me gusta.", "Por", "Para", "Pourquoi étudies-tu l'espagnol ? — Parce que ça me plaît.", "Why do you study Spanish? — Because I like it.", "On demande la CAUSE (porque…) → por qué.", "Asking for the CAUSE (porque…) → por qué."),
 ("¿___ qué sirve esta herramienta?", "Para", "Por", "À quoi sert cet outil ?", "What is this tool for?", "On demande le BUT, l'usage → para qué.", "Asking for the PURPOSE → para qué."),
 ("Hablamos ___ teléfono una hora.", "por", "para", "Nous avons parlé au téléphone une heure.", "We talked on the phone for an hour.", "Le moyen → por teléfono.", "The means → por teléfono."),
 ("Muchas gracias ___ venir.", "por", "para", "Merci beaucoup d'être venu.", "Thank you so much for coming.", "Remercier de quelque chose → gracias por.", "Thanking for something → gracias por."),
 ("Está muy alto ___ su edad.", "para", "por", "Il est très grand pour son âge.", "He's very tall for his age.", "La comparaison (pour quelqu'un de son âge) → para.", "Comparison (for someone his age) → para."),
 ("Pasaré ___ tu casa esta tarde.", "por", "para", "Je passerai chez toi cet après-midi.", "I'll drop by your place this afternoon.", "Passer quelque part → pasar por.", "Dropping by a place → pasar por."),
 ("Ahorro dinero ___ comprar una casa.", "para", "por", "J'économise pour acheter une maison.", "I'm saving money to buy a house.", "Le but → para.", "The goal → para."),
 ("Trabaja ___ una empresa alemana.", "para", "por", "Elle travaille pour une entreprise allemande.", "She works for a German company.", "L'employeur, celui à qui le travail est destiné → para.", "The employer, who the work is for → para."),
 ("Los deberes son ___ el viernes.", "para", "por", "Les devoirs sont pour vendredi.", "The homework is due on Friday.", "L'échéance → para.", "The deadline → para."),
 ("Caminamos ___ la playa al atardecer.", "por", "para", "Nous marchons sur la plage au coucher du soleil.", "We walk along the beach at sunset.", "Le parcours, à travers ou le long de → por.", "Moving along or through → por."),
 ("Lo hice ___ miedo.", "por", "para", "Je l'ai fait ___ peur.", "I did it ___ fear.", "La cause (à cause de la peur) → por.", "The cause (because of fear) → por."),
 ("Muchas gracias ___ las flores.", "por", "para", "Merci beaucoup pour les fleurs.", "Thank you very much for the flowers.", "On remercie de quelque chose reçu → por.", "Thanking for something received → por."),
 ("El avión ___ Lima sale con retraso.", "para", "por", "L'avion pour Lima part en retard.", "The plane to Lima is leaving late.", "La destination → para.", "The destination → para."),
 ("Fuimos a Granada ___ ver la Alhambra.", "para", "por", "Nous sommes allés à Grenade pour voir l'Alhambra.", "We went to Granada to see the Alhambra.", "Le but → para.", "The goal → para."),
 ("Pagué veinte euros ___ la entrada.", "por", "para", "J'ai payé vingt euros pour l'entrée.", "I paid twenty euros for the ticket.", "Le prix → por.", "The price → por."),
 ("La carta llegó ___ correo.", "por", "para", "La lettre est arrivée ___ la poste.", "The letter came ___ post.", "Le moyen → por.", "The means → por."),
 ("Trabajé mucho ___ terminar a tiempo.", "para", "por", "J'ai beaucoup travaillé pour finir à temps.", "I worked hard to finish on time.", "Le but → para.", "The goal → para."),
 ("Se cayó ___ las escaleras.", "por", "para", "Il est tombé dans l'escalier.", "He fell down the stairs.", "Le passage (le long de l'escalier) → por.", "Movement along the stairs → por."),
 ("Te doy mi libro ___ el tuyo.", "por", "para", "Je te donne mon livre contre le tien.", "I'll give you my book in exchange for yours.", "L'échange → por.", "An exchange → por."),
 ("Esta habitación es ___ los invitados.", "para", "por", "Cette chambre est pour les invités.", "This room is for the guests.", "Le destinataire → para.", "The recipient → para."),
 ("Lo felicitaron ___ su trabajo.", "por", "para", "On l'a félicité pour son travail.", "They congratulated him on his work.", "La raison des félicitations → por.", "The reason for the praise → por."),
 ("___ ser extranjero, habla muy bien español.", "Para", "Por", "Pour un étranger, il parle très bien espagnol.", "For a foreigner, he speaks Spanish very well.", "La comparaison (pour quelqu'un qui est étranger) → para.", "Comparison (for someone who is foreign) → para."),
 ("Se preocupa mucho ___ su hijo.", "por", "para", "Il s'inquiète beaucoup pour son fils.", "He worries a lot about his son.", "preocuparse por : la cause de l'inquiétude.", "preocuparse por: the cause of the worry."),
 ("Salimos ___ la puerta de atrás.", "por", "para", "Nous sommes sortis ___ la porte de derrière.", "We left ___ the back door.", "Le passage → por.", "The way through → por."),
 ("Tengo que terminar este trabajo ___ mañana.", "para", "por", "Je dois finir ce travail pour demain.", "I have to finish this work by tomorrow.", "L'échéance → para.", "The deadline → para."),
 ("Votaron ___ él en las elecciones.", "por", "para", "Ils ont voté pour lui aux élections.", "They voted for him in the election.", "votar por : en faveur de quelqu'un.", "votar por: in favour of someone."),
 ("Uso estas tijeras ___ cortar papel.", "para", "por", "J'utilise ces ciseaux pour couper du papier.", "I use these scissors to cut paper.", "L'usage, le but → para.", "Use, purpose → para."),
 ("Viajamos ___ toda Europa en tren.", "por", "para", "Nous avons voyagé dans toute l'Europe en train.", "We travelled all over Europe by train.", "Le parcours à travers un lieu → por.", "Travelling through a place → por."),
 ("La reunión se canceló ___ la lluvia.", "por", "para", "La réunion a été annulée à cause de la pluie.", "The meeting was cancelled because of the rain.", "La cause → por.", "The cause → por."),
 ("Necesito gafas ___ leer.", "para", "por", "J'ai besoin de lunettes pour lire.", "I need glasses to read.", "Le but, l'usage → para.", "Purpose, use → para."),
 ("Dos ___ dos son cuatro.", "por", "para", "Deux fois deux font quatre.", "Two times two is four.", "La multiplication → por.", "Multiplication → por."),
 ("Me quedé en casa ___ cuidar a mi madre.", "para", "por", "Je suis resté à la maison pour m'occuper de ma mère.", "I stayed at home to look after my mother.", "Le but → para.", "The goal → para."),
 ("Lo vendió ___ poco dinero.", "por", "para", "Il l'a vendu pour peu d'argent.", "He sold it for very little money.", "Le prix → por.", "The price → por."),
]

INDICE = {
    "ser": ("(identité, origine, heure, événement → ser ; lieu, état → estar)",
            "(identity, origin, time, event → ser; location, state → estar)"),
    "por": ("(but, destination, échéance → para ; cause, passage, échange, moyen → por)",
            "(goal, destination, deadline → para; cause, route, exchange, means → por)"),
}


def construire(lignes, sujet, indice):
    out = []
    for q, bon, autre, tfr, ten, efr, een in lignes:
        assert q.count("___") == 1, q
        # Les deux options dans un ordre FIXE (ser avant estar, por avant
        # para) : leur place ne doit pas trahir la reponse.
        opts = sorted([bon, autre], key=lambda x: x.lower().startswith(("est", "para")))
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
    assert len(SER_ESTAR) >= 50 and len(POR_PARA) >= 50, (len(SER_ESTAR), len(POR_PARA))
    for liste in (SER_ESTAR, POR_PARA):
        assert len({l[0] for l in liste}) == len(liste), "phrase en double"
    d = json.load(io.open(CHEMIN, encoding="utf-8"))
    d["jeux"]["serEstarExercises"] = construire(SER_ESTAR, "ser ou estar", INDICE["ser"])
    d["jeux"]["porParaExercises"] = construire(POR_PARA, "por ou para", INDICE["por"])
    io.open(CHEMIN, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("ser/estar : %d   por/para : %d" % (len(SER_ESTAR), len(POR_PARA)))


if __name__ == "__main__":
    main()
