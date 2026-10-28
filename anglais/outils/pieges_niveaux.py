# -*- coding: utf-8 -*-
"""Les questions des fiches « Pieges » (faux amis et mots confondus), A2-B2,
tirees des listes de l'ancien module (anglais/outils/ancien/english_pitfalls.json).
Ecrites a la main : une phrase a trous se juge, un tirage au hasard non.
Format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

QUESTIONS = {
"A2": """
___, I've never been to New York. | Actually | Currently / Actual | En fait, je ne suis jamais allé à New York. | En fait = actually (et pas « actuellement »).
She's ___ working from home. | currently | actually / actual | Elle travaille actuellement de chez elle. | Actuellement = currently.
I return my books to the ___ every Friday. | library | bookstore / librairy | Je rends mes livres à la bibliothèque tous les vendredis. | Bibliothèque = library.
You can buy that novel at the ___ on Newbury Street. | bookstore | library / librairy | Tu peux acheter ce roman à la librairie de Newbury Street. | Librairie = bookstore.
After high school, she went to ___ in Boston. | college | collège / high school | Après le lycée, elle est allée à l'université à Boston. | College = l'université aux États-Unis.
My little brother is in ___; he's twelve. | middle school | college / university | Mon petit frère est au collège ; il a douze ans. | Le collège français = middle school.
They have a ___ house with five bedrooms. | large | wide / broad | Ils ont une grande maison avec cinq chambres. | Large = grand.
The river is very ___ here — almost a hundred yards. | wide | large / big | La rivière est très large ici, presque cent verges. | Large (la largeur) = wide.
I need a ___ for the parking meter. | coin | corner / piece | Il me faut une pièce pour le parcomètre. | Une pièce de monnaie = a coin.
Meet me at the ___ of Charles Street. | corner | coin / angle | Retrouve-moi au coin de Charles Street. | Le coin de la rue = the corner.
We keep the old bikes in the ___. | basement | cave / grotto | On garde les vieux vélos à la cave. | La cave d'une maison = the basement (ou the cellar).
Bats live in the ___ near the lake. | cave | basement / cellar | Des chauves-souris vivent dans la grotte près du lac. | Une grotte = a cave.
I'd like a bunch of green ___. | grapes | raisins / grape | Je voudrais une grappe de raisins verts. | Le raisin frais = grapes ; raisins = raisins secs.
There are ___ in my oatmeal. | raisins | grapes / prunes | Il y a des raisins secs dans mon gruau. | Les raisins secs = raisins.
___ here, I'll be back in five minutes. | Stay | Rest / Remain at | Reste ici, je reviens dans cinq minutes. | Rester = to stay.
You look exhausted. Go and ___ for an hour. | rest | stay / remain | Tu as l'air épuisé. Va te reposer une heure. | Se reposer = to rest.
More than five hundred people ___ the meeting. | attended | waited / expected | Plus de cinq cents personnes ont assisté à la réunion. | Assister à = to attend.
We ___ for the bus for twenty minutes. | waited | attended / expected | Nous avons attendu le bus pendant vingt minutes. | Attendre = to wait (for).
This is your last ___ — don't miss it. | chance | luck / hazard | C'est ta dernière occasion, ne la rate pas. | Une occasion = a chance.
Good ___ with your exam tomorrow! | luck | chance / hazard | Bonne chance pour ton examen demain ! | La chance (la bonne fortune) = luck.
Can you ___ me twenty dollars until Monday? | lend | borrow / loan me | Tu peux me prêter vingt dollars jusqu'à lundi ? | Prêter à quelqu'un = lend.
Can I ___ your umbrella? It's raining. | borrow | lend / rent | Je peux emprunter ton parapluie ? Il pleut. | Emprunter à quelqu'un = borrow.
She ___ me a secret. | told | said / spoke | Elle m'a dit un secret. | Dire à quelqu'un : tell + personne.
He ___ that he was tired. | said | told / talked | Il a dit qu'il était fatigué. | Say, sans personne directement après.
Did you ___ that noise? | hear | listen / listen to | Tu as entendu ce bruit ? | Entendre (sans le vouloir) = hear.
I love to ___ jazz on Sunday mornings. | listen to | hear / listen | J'adore écouter du jazz le dimanche matin. | Écouter = listen to, toujours avec « to ».
We ___ a great movie last night. | watched | looked at / saw at | Nous avons regardé un excellent film hier soir. | Regarder ce qui bouge ou dure = watch.
___ this photo of my grandparents. | Look at | Watch / See at | Regarde cette photo de mes grands-parents. | Regarder une image fixe = look at.
Can you ___ the dishes tonight? | do | make / have | Tu peux faire la vaisselle ce soir ? | Une tâche = do.
Let's ___ a cake for her birthday. | make | do / bake up | Faisons un gâteau pour son anniversaire. | Fabriquer, produire = make.
I have to ___ my homework first. | do | make / write up | Je dois d'abord faire mes devoirs. | Homework : do.
She found a new ___ at the hospital. | job | work / travail | Elle a trouvé un nouvel emploi à l'hôpital. | Un emploi = a job (dénombrable).
I have too much ___ this week. | work | job / jobs | J'ai trop de travail cette semaine. | Work est indénombrable : pas de « a ».
The party was really ___ — we danced all night. | fun | funny / funky | La fête était vraiment sympa, on a dansé toute la nuit. | Agréable, amusant = fun.
His jokes are so ___. | funny | fun / funnily | Ses blagues sont tellement drôles. | Drôle (qui fait rire) = funny.
My sister is taller ___ me. | than | then / that | Ma sœur est plus grande que moi. | Que (comparaison) = than.
We had dinner, and ___ we went for a walk. | then | than / that | Nous avons soupé, puis nous sommes allés marcher. | Ensuite = then.
""",

"B1": """
We waited for hours, but ___ the plumber showed up. | eventually | possibly / actually | Nous avons attendu des heures, mais le plombier a fini par arriver. | Finalement = eventually.
I can ___ help you on Friday, if necessary. | possibly | eventually / actually | Je peux éventuellement t'aider vendredi, au besoin. | Éventuellement = possibly.
Wearing a helmet is the ___ thing to do. | sensible | sensitive / sensual | Porter un casque, c'est la chose raisonnable à faire. | Raisonnable = sensible.
My skin is very ___ to the sun. | sensitive | sensible / sensory | Ma peau est très sensible au soleil. | Sensible (émotif, fragile) = sensitive.
Classes will ___ on Monday after the break. | resume | summarize / sum | Les cours reprendront lundi après la pause. | Reprendre = to resume.
Can you ___ the article in two sentences? | summarize | resume / resummarize | Peux-tu résumer l'article en deux phrases ? | Résumer = to summarize.
The restaurant has a perfect ___ near the harbor. | location | rental / renting | Le restaurant a un emplacement parfait près du port. | Un emplacement = a location.
The car ___ cost us three hundred dollars. | rental | location / hire | La location de la voiture nous a coûté trois cents dollars. | Une location = a rental.
The union ___ an apology from the company. | demanded | asked / requested at | Le syndicat a exigé des excuses de l'entreprise. | Exiger = to demand.
Can I ___ you a question? | ask | demand / require | Je peux te poser une question ? | Demander = to ask.
My parents ___ me when I changed careers. | supported | put up / stood | Mes parents m'ont soutenu quand j'ai changé de carrière. | Soutenir = to support.
I can't ___ his jokes anymore. | stand | support / bear with | Je ne supporte plus ses blagues. | Supporter (tolérer) = to stand, to put up with.
She ___ her dream of running the Boston Marathon. | achieved | finished / ended | Elle a réalisé son rêve de courir le marathon de Boston. | Réaliser, accomplir = to achieve.
I need to ___ this report by five. | finish | achieve / accomplish at | Je dois finir ce rapport avant cinq heures. | Achever, terminer = to finish.
The ___ price was twice what they told us. | actual | current / actually | Le prix réel était le double de ce qu'on nous avait dit. | Réel = actual.
The ___ situation is very tense. | current | actual / actually | La situation actuelle est très tendue. | Actuel = current.
I ___ my driving test yesterday, but I failed. | took | passed / made | J'ai passé mon examen de conduite hier, mais je l'ai raté. | Passer (subir) un examen = take.
Great news — she ___ her final exam! | passed | took / succeeded | Bonne nouvelle : elle a réussi son examen final ! | Réussir un examen = pass.
The professor's ___ lasted two hours. | lecture | reading / lesson-reading | Le cours magistral du professeur a duré deux heures. | Un cours magistral = a lecture.
___ is my favorite way to relax. | Reading | Lecture / Lecturing | La lecture est ma façon préférée de me détendre. | La lecture = reading.
The ___ from Boston to Portland takes two hours. | trip | journey day / day | Le trajet de Boston à Portland prend deux heures. | Le trajet = the trip (ou the journey).
It was a long ___ at work. | day | journey / journal | Ça a été une longue journée au travail. | Une journée = a day.
The whole deal was built on ___. | deception | disappointment / deceit-ion | Toute l'affaire reposait sur la tromperie. | Tromperie = deception.
To our great ___, the game was postponed. | disappointment | deception / deceit | À notre grande déception, le match a été reporté. | Déception = disappointment.
He ___ his partners and kept the money. | deceived | disappointed / deceptioned | Il a trompé ses associés et gardé l'argent. | Tromper = to deceive.
The ending of the movie really ___ me. | disappointed | deceived / delusioned | La fin du film m'a vraiment déçu. | Décevoir = to disappoint.
She ___ me all evening — not a single word. | ignored | didn't know / unknew | Elle m'a ignoré toute la soirée, pas un seul mot. | Faire semblant de ne pas voir = to ignore.
I ___ that you had moved to Chicago. | didn't know | ignored / was ignoring | J'ignorais que tu avais déménagé à Chicago. | Ignorer (ne pas savoir) = not to know.
There's a two-hour ___ on all flights to Denver. | delay | deadline / delai | Il y a un retard de deux heures sur tous les vols vers Denver. | Un retard = a delay.
The ___ for applications is March 1. | deadline | delay / time delay | La date limite des candidatures est le 1er mars. | Un délai, une échéance = a deadline.
A good diet can ___ many health problems. | prevent | warn / prevent of | Une bonne alimentation peut prévenir bien des problèmes de santé. | Prévenir (empêcher) = to prevent.
Please ___ me if you're going to be late. | warn | prevent / advertise | Préviens-moi si tu vas être en retard. | Prévenir (avertir) = to warn (ou to let know).
The kids ___ to be asleep when I came in. | pretended | claimed / pretend | Les enfants ont fait semblant de dormir quand je suis entré. | Faire semblant = to pretend.
He ___ that he had never seen the letter. | claimed | pretended / pretexted | Il a prétendu qu'il n'avait jamais vu la lettre. | Prétendre (affirmer) = to claim.
Did you ___ to lock the door? | remember | remind / remember you | As-tu pensé à verrouiller la porte ? | Se souvenir, penser à = remember.
Can you ___ me to call the dentist? | remind | remember / recall | Peux-tu me rappeler d'appeler le dentiste ? | Rappeler à quelqu'un = remind.
My aunt ___ French at a high school in Cambridge. | teaches | learns / learns to | Ma tante enseigne le français dans un lycée de Cambridge. | Enseigner = teach.
I'm ___ to play the guitar. | learning | teaching / taught | J'apprends à jouer de la guitare. | Apprendre (soi-même) = learn.
Can you ___ me a glass of water, please? | bring | take / carry off | Tu peux m'apporter un verre d'eau, s'il te plaît ? | Vers celui qui parle = bring.
Don't forget to ___ your umbrella when you leave. | take | bring / bring away | N'oublie pas de prendre ton parapluie en partant. | Loin de celui qui parle = take.
We took a short ___ to Cape Cod. | trip | travel / travels | Nous avons fait une petite excursion à Cape Cod. | Un séjour, une sortie = a trip (jamais « a travel »).
I love to ___, especially by train. | travel | trip / journey | J'adore voyager, surtout en train. | Voyager = to travel.
She lives ___ in a small apartment. | alone | lonely / lonesome alone | Elle vit seule dans un petit appartement. | Seul (sans personne) = alone.
After the move, he felt very ___. | lonely | alone / only | Après le déménagement, il se sentait très seul. | Seul (et triste) = lonely.
Someone ___ my bike last night. | stole | robbed / stealed | Quelqu'un m'a volé mon vélo hier soir. | Voler un objet = steal.
Two men ___ the gas station on Main Street. | robbed | stole / stealed | Deux hommes ont dévalisé la station-service de Main Street. | Dévaliser un lieu ou une personne = rob.
Can I give you a piece of ___? | advice | advise / advices | Je peux te donner un conseil ? | Le nom = advice (indénombrable).
I ___ you to book early. | advise | advice / advices | Je te conseille de réserver tôt. | Le verbe = advise.
Everyone came ___ my cousin, who was sick. | except | accept / expect | Tout le monde est venu sauf mon cousin, qui était malade. | Sauf = except.
I'm happy to ___ your invitation. | accept | except / expect | Je suis heureux d'accepter ton invitation. | Accepter = accept.
""",

"B2": """
The nurse was very ___ when I told her about my father. | sympathetic | nice / likeable | L'infirmière a été très compatissante quand je lui ai parlé de mon père. | Compatissant = sympathetic.
Your new neighbors seem really ___. | nice | sympathetic / sympathic | Tes nouveaux voisins ont l'air vraiment sympathiques. | Sympathique = nice, friendly.
The guide gives a ___ list of every museum in the city. | comprehensive | understanding / comprehending | Le guide donne une liste complète de tous les musées de la ville. | Complet, exhaustif = comprehensive.
My boss was very ___ when my son was sick. | understanding | comprehensive / comprehensible | Mon patron a été très compréhensif quand mon fils était malade. | Compréhensif = understanding.
I didn't ___ how late it was. | realize | achieve / carry out | Je ne m'étais pas rendu compte de l'heure qu'il était. | Se rendre compte = realize.
The team ___ the project in only six weeks. | carried out | realized / realised out | L'équipe a réalisé le projet en seulement six semaines. | Réaliser (faire) = carry out.
Two players were ___ during the game. | injured | insulted / injuried | Deux joueurs ont été blessés pendant le match. | Blesser = injure.
He ___ the referee and was sent off. | insulted | injured / injuried | Il a injurié l'arbitre et a été expulsé. | Injurier = insult.
This jam contains no artificial ___. | preservatives | condoms / conservatives | Cette confiture ne contient aucun agent de conservation artificiel. | Agent de conservation = preservative.
The champion is a ___ opponent. | formidable | wonderful / great fun | Le champion est un adversaire redoutable. | Redoutable = formidable.
We had a ___ time at the festival! | wonderful | formidable / redoubtable | On a passé un moment formidable au festival ! | Formidable (super) = wonderful, great.
Ice on the sidewalk is a real ___ in winter. | hazard | chance / luck | La glace sur le trottoir est un vrai danger en hiver. | Un danger = a hazard.
We met by ___ at the airport. | chance | hazard / luck by | Nous nous sommes rencontrés par hasard à l'aéroport. | Par hasard = by chance.
The general ___ his troops to retreat. | commanded | ordered at / commended | Le général a ordonné à ses troupes de battre en retraite. | Ordonner (militaire) = command.
Are you ready to ___? | order | command / commend | Vous êtes prêts à commander ? | Commander (au restaurant) = order.
The storm ___ thousands of homes. | affected | effected / effect | La tempête a touché des milliers de foyers. | Le verbe = affect.
The new law had a big ___ on small businesses. | effect | affect / affection | La nouvelle loi a eu un grand effet sur les petites entreprises. | Le nom = effect.
___ your hand if you have a question. | Raise | Rise / Arise | Lève la main si tu as une question. | Raise + complément.
Prices ___ every year in January. | rise | raise / arise to | Les prix augmentent tous les ans en janvier. | Rise, sans complément.
The ___ situation of the country is improving. | economic | economical / economist | La situation économique du pays s'améliore. | De l'économie = economic.
A smaller car is more ___. | economical | economic / economy | Une plus petite voiture est plus économique. | Peu coûteux = economical.
The moon landing was a ___ moment. | historic | historical / history | Le premier pas sur la Lune a été un moment historique. | Qui fait date = historic.
She writes ___ novels set in colonial Boston. | historical | historic / history | Elle écrit des romans historiques qui se passent dans le Boston colonial. | Qui parle du passé = historical.
I love New England, ___ in the fall. | especially | specially / special | J'adore la Nouvelle-Angleterre, surtout à l'automne. | Surtout = especially.
This cake was ___ made for your birthday. | specially | especially / specialy | Ce gâteau a été fait spécialement pour ton anniversaire. | Dans un but précis = specially.
Come and sit ___ me. | beside | besides / aside | Viens t'asseoir à côté de moi. | À côté de = beside.
It's too expensive. ___, I don't really need it. | Besides | Beside / Aside | C'est trop cher. D'ailleurs, je n'en ai pas vraiment besoin. | D'ailleurs, en plus = besides.
Who else is coming, ___ Tom? | besides | beside / aside | Qui d'autre vient, en plus de Tom ? | En plus de = besides.
""",
}
