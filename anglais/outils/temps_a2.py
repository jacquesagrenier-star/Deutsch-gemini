# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » de l'anglais, A2 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

TEMPS = [
{
"id": "temps-past-simple", "titre": "Past simple — le passé terminé",
"texte": "Une action finie, à un moment passé précis (yesterday, last week, in 2019, ago). Verbes réguliers : <b>-ed</b> ; irréguliers : une forme à apprendre (go → went). Question et négation : <b>did</b> + verbe nu.<br><em>I worked late. She went home. Did you see it? We didn't stay.</em> (J'ai travaillé tard. Elle est rentrée. Tu l'as vu ? Nous ne sommes pas restés.)",
"serie": "tempsPastSimpleEnExercises", "kicker": "Past simple",
"questions": """
I ___ my grandmother last weekend. | visited | visit / have visited | J'ai rendu visite à ma grand-mère le week-end dernier. | Last weekend : past simple, -ed.
She ___ in Boston for ten years, then moved to Denver. | lived | lives / has lived | Elle a vécu dix ans à Boston, puis elle a déménagé à Denver. | Une période finie : past simple.
We ___ to the beach yesterday. | went | goed / go | Nous sommes allés à la plage hier. | Go → went.
He ___ a new car last month. | bought | buyed / buys | Il a acheté une nouvelle voiture le mois dernier. | Buy → bought.
I ___ him at the party. | saw | seed / seen | Je l'ai vu à la fête. | See → saw.
They ___ dinner at eight. | had | haved / has | Ils ont soupé à huit heures. | Have → had.
She ___ me a long email. | wrote | writed / written | Elle m'a écrit un long courriel. | Write → wrote.
I ___ my gloves on the bus. | lost | losed / lose | J'ai perdu mes gants dans l'autobus. | Lose → lost.
We ___ a great time in Vermont. | had | have / did have got | Nous avons passé un super moment au Vermont. | Have a good time → had.
He ___ the bus because he was late. | missed | miss / missing | Il a raté l'autobus parce qu'il était en retard. | Regular : -ed.
The movie ___ at nine and ended at eleven. | started | starts / start | Le film a commencé à neuf heures et s'est terminé à onze heures. | -ed.
I ___ the whole afternoon in the library. | spent | spended / spend | J'ai passé tout l'après-midi à la bibliothèque. | Spend → spent.
She ___ the window because it was hot. | opened | open / opens | Elle a ouvert la fenêtre parce qu'il faisait chaud. | -ed.
We ___ about it for hours. | talked | talk / talken | Nous en avons parlé pendant des heures. | -ed.
The kids ___ in the snow all morning. | played | plaied / play | Les enfants ont joué dans la neige toute la matinée. | Voyelle + y : -ed (played).
He ___ to call me. | tried | tryed / try | Il a essayé de m'appeler. | Consonne + y → -ied.
She ___ the bus to Providence. | took | taked / taken | Elle a pris l'autobus pour Providence. | Take → took.
I ___ a strange noise last night. | heard | heared / hear | J'ai entendu un bruit étrange hier soir. | Hear → heard.
We ___ our friends at the airport. | met | meeted / meet | Nous avons retrouvé nos amis à l'aéroport. | Meet → met.
The store ___ at six yesterday. | closed | close / closes | Le magasin a fermé à six heures hier. | -ed.
He ___ his arm playing hockey. | broke | breaked / broken | Il s'est cassé le bras en jouant au hockey. | Break → broke.
I ___ a sandwich for lunch. | ate | eated / eaten | J'ai mangé un sandwich au dîner. | Eat → ate.
She ___ home at midnight. | came | comed / come | Elle est rentrée à minuit. | Come → came.
They ___ the game 3–1. | won | winned / win | Ils ont gagné le match 3 à 1. | Win → won.
I ___ the answer, but I forgot it. | knew | knowed / known | Je connaissais la réponse, mais je l'ai oubliée. | Know → knew.
The train ___ twenty minutes late. | left | leaved / leave | Le train est parti avec vingt minutes de retard. | Leave → left.
We ___ the dog for a walk. | took | taked / take | Nous avons promené le chien. | Take → took.
She ___ ten miles on Sunday. | ran | runned / run | Elle a couru dix milles dimanche. | Run → ran.
I ___ to bed early last night. | went | go / have gone | Je suis allé me coucher tôt hier soir. | Last night : past simple.
He ___ his homework two hours ago. | finished | has finished / finish | Il a fini ses devoirs il y a deux heures. | Ago : past simple.
___ you see the game last night? | Did | Do / Have | Tu as vu le match hier soir ? | Question : Did + verbe nu.
Did she ___ the email? | send | sent / sends | Est-ce qu'elle a envoyé le courriel ? | Après did, le verbe reste nu.
Where ___ you go on vacation? | did | do / were | Où es-tu allé en vacances ? | Where + did + you + verbe nu.
What did you ___ for dinner? | have | had / has | Qu'est-ce que tu as mangé au souper ? | Did + verbe nu.
I ___ like the movie. | didn't | don't / wasn't | Je n'ai pas aimé le film. | Négation : didn't + verbe nu.
We didn't ___ the train. | catch | caught / catched | Nous n'avons pas attrapé le train. | Didn't + verbe nu.
She ___ come to the meeting. | didn't | doesn't / wasn't | Elle n'est pas venue à la réunion. | Didn't + verbe nu.
He ___ tired after the trip. | was | were / did | Il était fatigué après le voyage. | Be : he was.
We ___ at home all day. | were | was / did | Nous sommes restés à la maison toute la journée. | Be : we were.
___ you at work yesterday? | Were | Did / Was | Tu étais au travail hier ? | Question avec be : Were you…?
The weather ___ terrible last week. | was | were / did | Il a fait un temps affreux la semaine dernière. | It was.
It ___ cold, so we went for a walk. | wasn't | didn't / weren't | Il ne faisait pas froid, alors nous sommes allés marcher. | Négation de be : it wasn't.
They ___ happy with the hotel. | weren't | wasn't / didn't | Ils n'étaient pas contents de l'hôtel. | They weren't.
When ___ you start learning English? | did | do / were | Quand as-tu commencé à apprendre l'anglais ? | When + did + verbe nu.
How much ___ the tickets cost? | did | do / were | Combien ont coûté les billets ? | How much + did + verbe nu.
I ___ my phone in the taxi. | left | leaved / leave | J'ai oublié mon téléphone dans le taxi. | Leave → left.
She ___ a beautiful song at the wedding. | sang | singed / sung | Elle a chanté une belle chanson au mariage. | Sing → sang.
We ___ a lot of photos in Quebec City. | took | taked / takes | Nous avons pris beaucoup de photos à Québec. | Take → took.
My father ___ me how to swim. | taught | teached / teach | Mon père m'a appris à nager. | Teach → taught.
He ___ the door and left. | shut | shutted / shuts | Il a fermé la porte et il est parti. | Shut → shut (même forme).
I ___ my mind yesterday. | changed | change / chang | J'ai changé d'avis. | -ed.
""",
},
{
"id": "temps-past-continuous", "titre": "Past continuous — l'action en cours dans le passé",
"texte": "Ce qui était en train de se passer à un moment du passé : <b>was / were + -ing</b>. Souvent interrompu par une action courte au past simple, avec <b>when</b> ; deux actions longues en parallèle avec <b>while</b>.<br><em>I was cooking when the phone rang.</em> (Je cuisinais quand le téléphone a sonné.)",
"serie": "tempsPastContinuEnExercises", "kicker": "Past continuous",
"questions": """
I ___ reading in bed when you called. | was | were / did | Je lisais au lit quand tu as appelé. | I + was + -ing.
They ___ playing outside when it started to rain. | were | was / did | Ils jouaient dehors quand il a commencé à pleuvoir. | They + were + -ing.
At eight o'clock last night, we were ___ dinner. | having | had / have | Hier soir à huit heures, nous étions en train de souper. | Were + -ing.
She was ___ a shower when the lights went out. | taking | took / take | Elle prenait une douche quand les lumières se sont éteintes. | Was + -ing.
What ___ you doing at ten last night? | were | did / was | Que faisais-tu hier soir à dix heures ? | What + were + you + -ing.
It ___ snowing when we left the house. | was | were / did | Il neigeait quand nous sommes sortis de la maison. | It + was + -ing.
I was walking home when I ___ an old friend. | met | was meeting / meet | Je rentrais à pied quand j'ai croisé un vieil ami. | L'action courte qui interrompt : past simple.
He ___ his leg while he was skiing. | broke | was breaking / breaks | Il s'est cassé la jambe en faisant du ski. | L'événement court : past simple.
While I was cooking, my husband ___ the table. | was setting | set up / sets | Pendant que je cuisinais, mon mari mettait la table. | Deux actions longues en parallèle : while + -ing des deux côtés.
The phone rang ___ I was in the shower. | while | during / when I | Le téléphone a sonné pendant que j'étais sous la douche. | While + sujet + verbe.
I fell asleep ___ the movie. | during | while / when | Je me suis endormi pendant le film. | During + nom (pas de verbe).
We ___ watching TV when the power went out. | were | was / are | Nous regardions la télé quand le courant a été coupé. | We + were + -ing.
She ___ sleeping when the alarm went off. | wasn't | weren't / didn't | Elle ne dormait pas quand l'alarme a sonné. | Négation : wasn't + -ing.
They ___ listening to the teacher. | weren't | wasn't / didn't | Ils n'écoutaient pas l'enseignant. | Négation : weren't + -ing.
___ it raining when you got to the airport? | Was | Were / Did | Est-ce qu'il pleuvait quand tu es arrivé à l'aéroport ? | Question : Was + it + -ing.
___ you sleeping when I texted you? | Were | Was / Did | Tu dormais quand je t'ai écrit ? | Question : Were + you + -ing.
When I arrived, everybody ___. | was dancing | were dancing / danced to | Quand je suis arrivé, tout le monde dansait. | Everybody = singulier : was.
The sun ___ and the birds were singing. | was shining | shone up / were shining | Le soleil brillait et les oiseaux chantaient. | Une description de décor : past continuous.
I ___ my keys while I was running for the bus. | dropped | was dropping / drop | J'ai fait tomber mes clés en courant après l'autobus. | Action courte : past simple.
He was driving too fast when the police ___ him. | stopped | were stopping / stops | Il roulait trop vite quand la police l'a arrêté. | Action courte : past simple.
At midnight, I was still ___ on my essay. | working | worked / work | À minuit, je travaillais encore à ma dissertation. | Was + -ing.
My parents ___ in Montreal when I was born. | were living | was living / lived in at | Mes parents habitaient à Montréal quand je suis né. | Situation en cours à ce moment-là : were + -ing.
While she was studying, her roommate ___ music. | was playing | played up / were playing | Pendant qu'elle étudiait, sa colocataire jouait de la musique. | While + deux actions longues.
I saw an accident while I ___ to work. | was driving | drove / were driving | J'ai vu un accident en allant au travail en voiture. | L'action longue : was + -ing.
What were you ___ about? | talking | talked / talk | De quoi parliez-vous ? | Were + -ing.
Sorry, I ___ listening. Can you repeat? | wasn't | didn't / weren't | Désolé, je n'écoutais pas. Tu peux répéter ? | I wasn't + -ing.
The kids were ___ in the yard all afternoon. | playing | played / play | Les enfants ont joué dans la cour tout l'après-midi. | Were + -ing.
When the fire started, everyone ___. | was sleeping | were sleeping / slept in | Quand l'incendie a commencé, tout le monde dormait. | Everyone : was.
Where were you going when I ___ you? | saw | was seeing / see | Où allais-tu quand je t'ai vu ? | L'action courte : past simple.
It was raining, so we ___ inside. | stayed | were staying in / stay | Il pleuvait, alors nous sommes restés à l'intérieur. | La décision, l'événement : past simple.
She ___ dinner when I got home. | was making | made up / makes | Elle préparait le souper quand je suis rentré. | Was + -ing (en cours).
We met while we ___ in Paris. | were studying | studied at / was studying | Nous nous sommes rencontrés pendant nos études à Paris. | While + were + -ing.
I cut my finger while I ___ vegetables. | was chopping | chopped / were chopping | Je me suis coupé le doigt en coupant des légumes. | While + was + -ing.
He ___ a book when I came in. | was reading | read up / reads | Il lisait un livre quand je suis entré. | Was + -ing.
They were arguing when the teacher ___ in. | walked | was walking / walks | Ils se disputaient quand l'enseignant est entré. | Action courte : past simple.
A man ___ in front of the store. | was standing | were standing / stands | Un homme se tenait devant le magasin. | Description : was + -ing.
""",
},
{
"id": "temps-futur", "titre": "Le futur — will, going to, present continuous",
"texte": "Trois façons de parler de l'avenir. <b>Will</b> : une décision prise sur le moment, une promesse, une prévision. <b>Going to</b> : une intention déjà décidée, ou ce qu'on voit venir. <b>Present continuous</b> : un rendez-vous fixé.<br><em>I'll help you. I'm going to sell my car. We're meeting at six.</em> (Je vais t'aider. Je vais vendre ma voiture. On se voit à six heures.)",
"serie": "tempsFuturEnExercises", "kicker": "Le futur",
"questions": """
The phone's ringing. — I ___ get it. | 'll | 'm going to / get | Le téléphone sonne. — Je réponds. | Décision sur le moment : will.
I promise I ___ tell anyone. | won't | don't / 'm not | Je promets que je ne le dirai à personne. | Promesse : will / won't.
Look at those clouds! It's ___ rain. | going to | will to / goes to | Regarde ces nuages ! Il va pleuvoir. | Ce qu'on voit venir : going to.
We've decided: we're ___ move to Portland. | going to | will / go to | C'est décidé : nous allons déménager à Portland. | Intention déjà décidée : going to.
I think the Red Sox ___ win tonight. | will | are winning / win | Je pense que les Red Sox vont gagner ce soir. | Prévision avec « I think » : will.
I'm ___ my parents on Sunday — it's all arranged. | visiting | visit / will visiting | Je vais voir mes parents dimanche, c'est organisé. | Rendez-vous fixé : present continuous.
What ___ you going to do this summer? | are | will / do | Qu'est-ce que tu vas faire cet été ? | What are you going to + verbe.
She ___ be thirty next year. | will | is going / is being | Elle aura trente ans l'an prochain. | Un fait futur : will.
I'm hungry. — I ___ make you a sandwich. | 'll | 'm making / make | J'ai faim. — Je vais te faire un sandwich. | Offre spontanée : will.
___ you help me with this box? | Will | Are / Do you will | Tu peux m'aider avec cette boîte ? | Demande : Will you…?
He ___ to start a new job in May. | is going | will / goes | Il va commencer un nouvel emploi en mai. | Is going to + verbe.
Don't worry, it ___ be fine. | will | is going / is | Ne t'inquiète pas, ça va bien aller. | Rassurer, prédire : will.
We're ___ dinner with the Smiths tonight. | having | have / will having | Nous soupons avec les Smith ce soir. | Projet arrangé : present continuous.
Careful! You're going ___ fall! | to | for / will | Attention ! Tu vas tomber ! | Going to + verbe.
I ___ probably be late. | 'll | 'm / 'm going | Je serai sans doute en retard. | Probably + will.
She ___ come to the party — she's sick. | won't | doesn't / isn't going | Elle ne viendra pas à la fête, elle est malade. | Won't = will not.
They ___ going to buy a house. | aren't | won't / don't | Ils ne vont pas acheter de maison. | Négation : aren't going to.
When ___ you be back? | will | are / do | Quand seras-tu de retour ? | When will you be…?
I've bought the paint. I'm ___ paint the kitchen this weekend. | going to | will / go | J'ai acheté la peinture. Je vais repeindre la cuisine ce week-end. | Intention préparée : going to.
The plane ___ at 6:30 tomorrow morning. | leaves | is leave / will leaving | L'avion part demain matin à 6 h 30. | Horaire officiel : present simple.
The movie ___ at eight, so let's eat before. | starts | will starting / is start | Le film commence à huit heures, alors mangeons avant. | Horaire : present simple.
Wait, I ___ carry that for you. | 'll | 'm carrying / carry | Attends, je vais te porter ça. | Offre sur le moment : will.
Do you think she ___ like the gift? | will | is going / likes to | Tu crois qu'elle aimera le cadeau ? | Prévision : will.
I ___ call you when I get home. | 'll | 'm calling / call | Je t'appelle quand je rentre. | Promesse : will.
When I ___ to the hotel, I'll call you. | get | will get / am getting | Quand j'arriverai à l'hôtel, je t'appellerai. | Après when (futur), present simple.
If it ___ tomorrow, we'll stay home. | rains | will rain / is raining tomorrow | S'il pleut demain, nous resterons à la maison. | Après if, present simple.
As soon as she ___, we'll start. | arrives | will arrive / arrived | Dès qu'elle arrivera, on commencera. | As soon as + present simple.
I'm sure you ___ pass the test. | will | are going pass / pass to | Je suis sûr que tu réussiras l'examen. | I'm sure + will.
___ I open the window? — Yes, please, it's hot. | Shall | Will / Do | Veux-tu que j'ouvre la fenêtre ? — Oui, s'il te plaît, il fait chaud. | Proposer son aide : Shall I…?
What time ___ you meeting the doctor? | are | will / do | À quelle heure vois-tu le médecin ? | Rendez-vous : present continuous.
Next year, I ___ learn to drive. | 'm going to | will to / 'm go to | L'an prochain, je vais apprendre à conduire. | Intention : going to.
It's ten to nine. We ___ miss the bus! | 're going to | will to / go to | Il est neuf heures moins dix. On va rater l'autobus ! | Ce qu'on voit venir : going to.
Maybe I ___ see you at the game. | 'll | 'm seeing / see | Peut-être que je te verrai au match. | Maybe + will.
They ___ get married in June — they've booked the church. | are going to | will to / go to | Ils vont se marier en juin ; ils ont réservé l'église. | Projet décidé : going to.
I ___ forget your birthday this year, I promise. | won't | 'm not / don't | Je n'oublierai pas ton anniversaire cette année, promis. | Promesse : won't.
Robots ___ do most of the housework in the future. | will | are doing / do to | Les robots feront la plupart des tâches ménagères à l'avenir. | Prévision : will.
""",
},
{
"id": "temps-forme-de-base", "titre": "La forme de base — retrouver le verbe du dictionnaire",
"texte": "Pour chercher un verbe dans le dictionnaire, il faut sa forme de base, sans <b>to</b> : à partir d'une forme conjuguée (went, bought, written, says), retrouver le verbe nu.<br><em>went → go · bought → buy · written → write · she says → say.</em>",
"serie": "tempsFormeDeBaseEnExercises", "kicker": "La forme de base",
"questions": """
She went home early. — « went » vient de : ___ | go | went / gone | Elle est rentrée tôt. | went = passé de go.
I bought a new coat. — « bought » vient de : ___ | buy | bring / bought | J'ai acheté un nouveau manteau. | bought = passé de buy.
He brought some wine. — « brought » vient de : ___ | bring | buy / bright | Il a apporté du vin. | brought = passé de bring.
I thought about you. — « thought » vient de : ___ | think | thank / teach | J'ai pensé à toi. | thought = passé de think.
She taught me French. — « taught » vient de : ___ | teach | think / take | Elle m'a appris le français. | taught = passé de teach.
We caught the last bus. — « caught » vient de : ___ | catch | cut / come | Nous avons attrapé le dernier autobus. | caught = passé de catch.
They fought all the time. — « fought » vient de : ___ | fight | find / feel | Ils se disputaient tout le temps. | fought = passé de fight.
I found my wallet. — « found » vient de : ___ | find | fight / fund | J'ai retrouvé mon portefeuille. | found = passé de find.
He felt sick. — « felt » vient de : ___ | feel | fall / fill | Il s'est senti malade. | felt = passé de feel.
She fell on the ice. — « fell » vient de : ___ | fall | feel / fill | Elle est tombée sur la glace. | fell = passé de fall.
I left my bag on the bus. — « left » vient de : ___ | leave | live / lift | J'ai oublié mon sac dans l'autobus. | left = passé de leave.
We lived in Ohio. — « lived » vient de : ___ | live | leave / life | Nous avons habité en Ohio. | lived = passé de live (régulier).
He lost his job. — « lost » vient de : ___ | lose | loose / last | Il a perdu son emploi. | lost = passé de lose.
I sent you an email. — « sent » vient de : ___ | send | sell / sit | Je t'ai envoyé un courriel. | sent = passé de send.
They sold their house. — « sold » vient de : ___ | sell | send / hold | Ils ont vendu leur maison. | sold = passé de sell.
She told me everything. — « told » vient de : ___ | tell | talk / toll | Elle m'a tout raconté. | told = passé de tell.
I held the baby. — « held » vient de : ___ | hold | help / hide | J'ai tenu le bébé. | held = passé de hold.
We sat in the back. — « sat » vient de : ___ | sit | set / seat | Nous nous sommes assis au fond. | sat = passé de sit.
He stood by the door. — « stood » vient de : ___ | stand | stay / stop | Il se tenait près de la porte. | stood = passé de stand.
I understood the question. — « understood » vient de : ___ | understand | understood / undertake | J'ai compris la question. | understood = passé de understand.
She wore a blue dress. — « wore » vient de : ___ | wear | were / war | Elle portait une robe bleue. | wore = passé de wear.
I've written three pages. — « written » vient de : ___ | write | ride / wrote | J'ai écrit trois pages. | written = participe de write.
Have you eaten? — « eaten » vient de : ___ | eat | ate / heat | Tu as mangé ? | eaten = participe de eat.
She has driven all night. — « driven » vient de : ___ | drive | drove / drink | Elle a conduit toute la nuit. | driven = participe de drive.
They have chosen a name. — « chosen » vient de : ___ | choose | chose / cheese | Ils ont choisi un nom. | chosen = participe de choose.
I've forgotten his name. — « forgotten » vient de : ___ | forget | forgot / forgive | J'ai oublié son nom. | forgotten = participe de forget.
The glass is broken. — « broken » vient de : ___ | break | broke / bring | Le verre est cassé. | broken = participe de break.
He has given up. — « given » vient de : ___ | give | gave / get | Il a abandonné. | given = participe de give.
I've never ridden a horse. — « ridden » vient de : ___ | ride | rode / write | Je ne suis jamais monté à cheval. | ridden = participe de ride.
The sun has risen. — « risen » vient de : ___ | rise | raise / rose | Le soleil s'est levé. | risen = participe de rise.
She has spoken to the manager. — « spoken » vient de : ___ | speak | spoke / spell | Elle a parlé au gérant. | spoken = participe de speak.
It was stolen last night. — « stolen » vient de : ___ | steal | stole / stay | Ça a été volé hier soir. | stolen = participe de steal.
I've known her for years. — « known » vient de : ___ | know | knew / now | Je la connais depuis des années. | known = participe de know.
The tree has grown a lot. — « grown » vient de : ___ | grow | grew / grown | L'arbre a beaucoup poussé. | grown = participe de grow.
She says hello. — « says » vient de : ___ | say | says / sea | Elle dit bonjour. | -s de la 3e personne : say.
He does yoga. — « does » vient de : ___ | do | does / dose | Il fait du yoga. | does = do à la 3e personne.
She has a dog. — « has » vient de : ___ | have | has / had | Elle a un chien. | has = have à la 3e personne.
He tries hard. — « tries » vient de : ___ | try | trie / tries | Il fait de gros efforts. | -ies → -y : try.
She studied law. — « studied » vient de : ___ | study | studie / studied | Elle a étudié le droit. | -ied → -y : study.
We stopped for gas. — « stopped » vient de : ___ | stop | stopp / step | Nous nous sommes arrêtés pour faire le plein. | Consonne doublée : stop.
He's running late. — « running » vient de : ___ | run | runn / ran | Il est en retard. | Consonne doublée : run.
She's making soup. — « making » vient de : ___ | make | mak / made | Elle fait de la soupe. | Le -e retombe : make.
I was. — « was » vient de : ___ | be | was / is | J'étais. | was = passé de be.
They were tired. — « were » vient de : ___ | be | were / wear | Ils étaient fatigués. | were = passé de be.
I paid the bill. — « paid » vient de : ___ | pay | paid / pray | J'ai payé la facture. | paid = passé de pay.
She laid the baby on the bed. — « laid » vient de : ___ | lay | lie / lead | Elle a couché le bébé sur le lit. | laid = passé de lay.
He led the team. — « led » vient de : ___ | lead | lie / let | Il a dirigé l'équipe. | led = passé de lead.
They met in college. — « met » vient de : ___ | meet | mean / melt | Ils se sont rencontrés à l'université. | met = passé de meet.
She has sung in a choir. — « sung » vient de : ___ | sing | sang / song | Elle a chanté dans une chorale. | sung = participe de sing.
I meant it. — « meant » vient de : ___ | mean | meet / mend | Je le pensais vraiment. | meant = passé de mean.
""",
},
]
