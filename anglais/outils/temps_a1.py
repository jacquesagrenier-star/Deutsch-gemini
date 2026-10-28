# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » de l'anglais, A1 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

TEMPS = [
{
"id": "temps-present-simple", "titre": "Present simple — le présent des habitudes",
"texte": "Ce qu'on fait d'habitude, ce qui est toujours vrai. Le verbe nu, avec <b>-s</b> à la 3<sup>e</sup> personne (he, she, it) ; <b>do / does</b> pour la question et la négation.<br><em>She works in Boston. Do you like coffee? He doesn't drive.</em> (Elle travaille à Boston. Tu aimes le café ? Il ne conduit pas.)",
"serie": "tempsPresentSimpleEnExercises", "kicker": "Present simple",
"questions": """
I ___ tea every afternoon. | drink | drinks / drinking | Je bois du thé tous les après-midi. | I + verbe nu.
She ___ in a bank downtown. | works | work / working | Elle travaille dans une banque au centre-ville. | She + verbe + -s.
My parents ___ in Florida. | live | lives / living | Mes parents habitent en Floride. | They (my parents) + verbe nu.
He ___ the bus to school. | takes | take / taking | Il prend l'autobus pour aller à l'école. | He + verbe + -s.
We ___ dinner at six. | have | has / having | Nous soupons à six heures. | We + have.
My brother ___ two cats. | has | have / haves | Mon frère a deux chats. | He, she, it + has (pas « haves »).
The store ___ at nine. | opens | open / opening | Le magasin ouvre à neuf heures. | It + verbe + -s.
She ___ TV after dinner. | watches | watchs / watch | Elle regarde la télé après le souper. | Après -ch : -es (watches).
He ___ his homework in the evening. | does | do / dos | Il fait ses devoirs le soir. | Do → does à la 3e personne.
My sister ___ to the gym on Mondays. | goes | go / gos | Ma sœur va au gym le lundi. | Go → goes.
The baby ___ a lot at night. | cries | crys / cry | Le bébé pleure beaucoup la nuit. | Consonne + y → -ies.
She ___ English very well. | speaks | speak / speaking | Elle parle très bien anglais. | She + verbe + -s.
Water ___ at 100 degrees Celsius. | boils | boil / is boil | L'eau bout à 100 degrés Celsius. | Une vérité générale : present simple.
The sun ___ in the east. | rises | rise / is rise | Le soleil se lève à l'est. | Une vérité générale : present simple, -s.
___ you like pizza? | Do | Does / Are | Tu aimes la pizza ? | Question : Do + you + verbe nu.
___ she work on Saturdays? | Does | Do / Is | Est-ce qu'elle travaille le samedi ? | Question : Does + she + verbe nu.
Does he ___ in Cambridge? | live | lives / living | Est-ce qu'il habite à Cambridge ? | Après does, le verbe reste nu.
Where ___ your parents live? | do | does / are | Où habitent tes parents ? | Where + do + they.
What time ___ the movie start? | does | do / is | À quelle heure commence le film ? | The movie = it → does.
I ___ like mushrooms. | don't | doesn't / not | Je n'aime pas les champignons. | Négation : I don't + verbe nu.
He ___ eat meat. | doesn't | don't / isn't | Il ne mange pas de viande. | Négation : he doesn't + verbe nu.
She doesn't ___ a car. | have | has / having | Elle n'a pas de voiture. | Après doesn't, le verbe reste nu.
We ___ watch TV during dinner. | don't | doesn't / aren't | Nous ne regardons pas la télé pendant le souper. | We don't + verbe nu.
My dad ___ cook. My mom does. | doesn't | don't / isn't | Mon père ne cuisine pas. Ma mère, oui. | He doesn't + verbe nu.
I ___ to work by bike. | go | goes / going | Je vais au travail à vélo. | I + verbe nu.
Tom and Lisa ___ in the same office. | work | works / working | Tom et Lisa travaillent dans le même bureau. | They + verbe nu.
Everybody ___ her. | knows | know / knowing | Tout le monde la connaît. | Everybody = singulier → -s.
My dog ___ to sleep on the sofa. | loves | love / loving | Mon chien adore dormir sur le canapé. | It + verbe + -s.
She ___ her teeth twice a day. | brushes | brushs / brush | Elle se brosse les dents deux fois par jour. | Après -sh : -es.
He ___ the dishes after dinner. | washes | washs / wash | Il lave la vaisselle après le souper. | Après -sh : -es.
I usually ___ up at seven. | get | gets / getting | Je me lève habituellement à sept heures. | Usually : habitude → present simple.
She never ___ late. | arrives | arrive / arriving | Elle n'arrive jamais en retard. | Never + verbe au present simple (-s).
How often ___ you go to the movies? | do | does / are | À quelle fréquence vas-tu au cinéma ? | How often + do + you.
He always ___ the same sandwich. | orders | order / ordering | Il commande toujours le même sandwich. | Always + present simple.
They sometimes ___ basketball after school. | play | plays / playing | Ils jouent parfois au basket après l'école. | They + verbe nu.
The train ___ at 8:15 every day. | leaves | leave / leaving | Le train part à 8 h 15 tous les jours. | Horaire régulier : present simple.
My grandmother ___ a lot of books. | reads | read / reading | Ma grand-mère lit beaucoup de livres. | She + verbe + -s.
I ___ what you mean. | understand | understands / am understanding | Je comprends ce que tu veux dire. | Understand est un verbe d'état : present simple.
She ___ a new phone. | wants | want / is wanting | Elle veut un nouveau téléphone. | Want : verbe d'état, present simple.
This bag ___ to me. | belongs | belong / is belonging | Ce sac m'appartient. | Belong : verbe d'état.
___ he play the piano? | Does | Do / Has | Est-ce qu'il joue du piano ? | Question à la 3e personne : Does.
Yes, I ___. | do | does / am | Oui. (réponse à « Do you…? ») | Réponse courte : Yes, I do.
No, she ___. | doesn't | don't / isn't | Non. (réponse à « Does she…? ») | Réponse courte : No, she doesn't.
It ___ a lot in Seattle. | rains | rain / raining | Il pleut beaucoup à Seattle. | It + verbe + -s.
My phone ___ two hundred dollars. | costs | cost / costing | Mon téléphone coûte deux cents dollars. | It + verbe + -s.
The kids ___ school at three. | finish | finishes / finishing | Les enfants finissent l'école à trois heures. | They + verbe nu.
He ___ for the newspaper. | writes | write / writing | Il écrit pour le journal. | He + verbe + -s.
What ___ she do? — She's a nurse. | does | do / is | Que fait-elle (comme métier) ? — Elle est infirmière. | What does she do? = quel est son métier ?
My mom ___ to call me on Sundays. | likes | like / liking | Ma mère aime m'appeler le dimanche. | She + verbe + -s.
Cats ___ milk. | like | likes / liking | Les chats aiment le lait. | Pluriel : verbe nu.
""",
},
{
"id": "temps-present-continuous", "titre": "Present continuous — ce qui se passe maintenant",
"texte": "Une action en cours, en ce moment ou en cette période : <b>am / is / are + verbe en -ing</b>. Le français dit « je suis en train de… », ou simplement le présent.<br><em>I'm cooking. She isn't sleeping. Are you listening?</em> (Je cuisine. Elle ne dort pas. Tu écoutes ?)",
"serie": "tempsPresentContinuEnExercises", "kicker": "Present continuous",
"questions": """
I ___ cooking dinner right now. | am | is / are | Je suis en train de préparer le souper. | I + am + -ing.
She ___ talking on the phone. | is | are / am | Elle parle au téléphone. | She + is + -ing.
They ___ playing in the yard. | are | is / am | Ils jouent dans la cour. | They + are + -ing.
Look! It's ___. | snowing | snow / snows | Regarde ! Il neige. | Look! : en ce moment → -ing.
We're ___ for the bus. | waiting | wait / waits | Nous attendons l'autobus. | Be + -ing.
He's ___ a shower. | taking | take / takeing | Il prend une douche. | Take → taking (le -e tombe).
The kids are ___ in the pool. | swimming | swiming / swim | Les enfants nagent dans la piscine. | Swim → swimming (consonne doublée).
Why are you ___? | running | runing / run | Pourquoi tu cours ? | Run → running.
She's ___ a letter to her grandma. | writing | writting / write | Elle écrit une lettre à sa grand-mère. | Write → writing (le -e tombe).
I'm ___ on the couch. | sitting | siting / sit | Je suis assis sur le canapé. | Sit → sitting.
The baby is ___. | sleeping | sleep / sleeps | Le bébé dort. | Is + -ing.
___ you listening to me? | Are | Do / Is | Tu m'écoutes ? | Question : Are + you + -ing.
___ she working today? | Is | Does / Are | Est-ce qu'elle travaille aujourd'hui ? | Question : Is + she + -ing.
What ___ you doing in the garage? | are | do / is | Qu'est-ce que tu fais dans le garage ? | What + are + you + -ing.
Where ___ he going? | is | does / are | Où va-t-il ? | Where + is + he + -ing.
I'm not ___ TV, I'm reading. | watching | watch / watches | Je ne regarde pas la télé, je lis. | Négation : am not + -ing.
He ___ working right now. | isn't | doesn't / don't | Il ne travaille pas en ce moment. | Négation : isn't + -ing.
We ___ eating meat this month. | aren't | don't / isn't | Nous ne mangeons pas de viande ce mois-ci. | Négation : aren't + -ing.
My brother is ___ in Chicago this year. | living | live / lives | Mon frère vit à Chicago cette année. | Une situation temporaire : -ing.
I'm ___ a great book at the moment. | reading | read / reads | Je lis un excellent livre en ce moment. | At the moment → -ing.
Be quiet! The baby ___. | is sleeping | sleeps / sleep | Silence ! Le bébé dort. | Be quiet! : maintenant → present continuous.
Listen! Someone ___ at the door. | is knocking | knocks / knock | Écoute ! Quelqu'un frappe à la porte. | Listen! : maintenant.
She usually ___ the bus, but today she's walking. | takes | is taking / take | D'habitude, elle prend l'autobus, mais aujourd'hui elle marche. | Usually : habitude → present simple.
He ___ his car today because it's sunny. | is washing | washes / wash | Il lave sa voiture aujourd'hui parce qu'il fait soleil. | Today, maintenant : present continuous.
I ___ jeans every day. | wear | am wearing / wears | Je porte un jean tous les jours. | Every day : habitude → present simple.
Look, she ___ a red dress today. | is wearing | wears / wear | Regarde, elle porte une robe rouge aujourd'hui. | Today, ce qu'on voit : -ing.
I ___ you. | love | am loving / loves | Je t'aime. | Love : verbe d'état, pas de -ing.
I ___ the answer to that question. | know | am knowing / knows | Je connais la réponse à cette question. | Know : verbe d'état, pas de -ing.
She ___ a new bike. | needs | is needing / need | Elle a besoin d'un nouveau vélo. | Need : verbe d'état.
They ___ a house near the lake. | own | are owning / owns | Ils possèdent une maison près du lac. | Own : verbe d'état.
Hurry up! Everybody ___ for you. | is waiting | waits / are waiting | Dépêche-toi ! Tout le monde t'attend. | Everybody = singulier → is.
Right now, my parents ___ dinner in the kitchen. | are having | have / is having | En ce moment, mes parents soupent dans la cuisine. | They + are + -ing ; have dinner peut prendre -ing.
I'm ___ to music. | listening | listen / listenning | J'écoute de la musique. | Listen → listening (pas de doublement).
She's ___ her bike to work this week. | riding | rideing / ride | Elle va au travail à vélo cette semaine. | Ride → riding.
He's ___ the table for dinner. | setting | seting / set | Il met la table pour le souper. | Set → setting.
Why ___ she crying? | is | does / are | Pourquoi pleure-t-elle ? | Why + is + she + -ing.
The phone is ___. Can you get it? | ringing | ring / rings | Le téléphone sonne. Tu peux répondre ? | Is + -ing.
Are they ___ to the party tonight? | coming | come / comming | Ils viennent à la fête ce soir ? | Come → coming.
It ___ raining anymore. | isn't | doesn't / don't | Il ne pleut plus. | Négation : isn't + -ing.
Prices ___ going up every month. | are | is / do | Les prix augmentent tous les mois. | Une évolution en cours : are + -ing.
I'm ___ dinner with Anna tonight. | having | have / has | Je soupe avec Anna ce soir. | Un projet fixé : present continuous.
We're ___ to Maine next weekend. | driving | drive / driveing | On va en voiture dans le Maine le week-end prochain. | Un projet prévu : -ing.
Is your brother ___ for a new job? | looking | look / looks | Ton frère cherche un nouvel emploi ? | Is + -ing.
You ___ standing on my foot! | are | is / do | Tu es sur mon pied ! | You + are + -ing.
""",
},
]
