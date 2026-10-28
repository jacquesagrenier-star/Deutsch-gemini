# -*- coding: utf-8 -*-
"""Les series B2 allongees (28 oct. 2026) : des questions a la suite des
douze de chaque fiche (grammaire_b2.py), pour approcher le volume des series
allemandes. Meme format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

SUPPLEMENTS = {
"conditionnel3EnExercises": """
If we ___ the map, we wouldn't have gotten lost. | had checked | checked / would check | Si nous avions regardé la carte, nous ne nous serions pas perdus. | Conditionnel 3 : if + past perfect.
If she had called, I ___ picked her up. | would have | would / had | Si elle avait appelé, je serais allé la chercher. | Would have + participe.
If he ___ so fast, he wouldn't have crashed. | hadn't driven | didn't drive / wouldn't drive | S'il n'avait pas roulé si vite, il n'aurait pas eu d'accident. | If + hadn't + participe.
They would have come if you ___ them. | had invited | invited / would invite | Ils seraient venus si tu les avais invités. | If + past perfect.
If I had seen you, I ___ hello. | would have said | would say / had said | Si je t'avais vu, je t'aurais dit bonjour. | Would have + participe.
If it ___ so cold, we would have gone skating. | hadn't been | wasn't / wouldn't be | S'il n'avait pas fait si froid, nous serions allés patiner. | Hadn't been.
We ___ have missed the flight if the taxi had been on time. | wouldn't | won't / didn't | Nous n'aurions pas raté l'avion si le taxi avait été à l'heure. | Wouldn't have + participe.
If you had listened, you ___ what to do. | would have known | would know yesterday / had known | Si tu avais écouté, tu aurais su quoi faire. | Would have + participe.
What would you have done if you ___ the lottery? | had won | won / would win | Qu'aurais-tu fait si tu avais gagné à la loterie ? | If + past perfect.
If I'd known you were vegetarian, I ___ cooked fish. | wouldn't have | won't have / didn't | Si j'avais su que tu étais végétarien, je n'aurais pas cuisiné de poisson. | Wouldn't have + participe.
If she hadn't missed the train, she ___ here now. | would be | would have been yesterday / is | Si elle n'avait pas raté le train, elle serait ici maintenant. | Mixte : passé → conséquence présente.
If I ___ more patient, I would have waited. | were | had been being / am | Si j'étais plus patient (de nature), j'aurais attendu. | Mixte : état présent → conséquence passée.
If he had taken the job, he ___ in Seattle now. | would be living | would have lived / lives | S'il avait accepté le poste, il vivrait à Seattle maintenant. | Mixte : would be + -ing.
___ we left earlier, we would have caught the ferry. | Had | If / Did | Si nous étions partis plus tôt, nous aurions attrapé le traversier. | Inversion : Had we left = If we had left.
___ it not been for your help, I would have failed. | Had | If / Were | Sans ton aide, j'aurais échoué. | Had it not been for = sans.
If you had told me earlier, I ___ have changed my plans. | could | can / will | Si tu me l'avais dit plus tôt, j'aurais pu changer mes plans. | Could have = aurait pu.
If the doctor had come sooner, she ___ have survived. | might | may / will | Si le médecin était venu plus tôt, elle aurait peut-être survécu. | Might have = aurait peut-être.
I would have bought it if it ___ so expensive. | hadn't been | wasn't / wouldn't be | Je l'aurais acheté s'il n'avait pas été si cher. | Hadn't been.
If they hadn't argued, they ___ still be friends. | would | will / had | S'ils ne s'étaient pas disputés, ils seraient encore amis. | Mixte : would + verbe nu.
If I ___ my phone, I could have called you. | hadn't lost | didn't lose / wouldn't lose | Si je n'avais pas perdu mon téléphone, j'aurais pu t'appeler. | Hadn't + participe.
She would have passed the test if she ___ more. | had studied | studied / would study | Elle aurait réussi l'examen si elle avait plus étudié. | If + past perfect.
If we had booked earlier, the tickets ___ cheaper. | would have been | would be yesterday / had been | Si nous avions réservé plus tôt, les billets auraient été moins chers. | Would have been.
If you hadn't reminded me, I ___ forgotten. | would have | will have / had | Si tu ne me l'avais pas rappelé, j'aurais oublié. | Would have + participe.
If I spoke French, I ___ that job in Montreal last year. | would have gotten | would get / had got | Si je parlais français, j'aurais obtenu ce poste à Montréal l'an dernier. | Mixte : état présent → passé.
If the alarm had gone off, I ___ late. | wouldn't have been | won't be / wasn't | Si le réveil avait sonné, je n'aurais pas été en retard. | Wouldn't have been.
If you ___ me the truth, I wouldn't be so angry now. | had told | told / would tell | Si tu m'avais dit la vérité, je ne serais pas si fâché maintenant. | Mixte : if + past perfect, would + présent.
Would you have gone if they ___ you? | had asked | asked / would ask | Y serais-tu allé s'ils te l'avaient demandé ? | If + past perfect.
If he hadn't been so rude, she ___ him. | would have forgiven | would forgive yesterday / forgave | S'il n'avait pas été si impoli, elle lui aurait pardonné. | Would have + participe.
I ___ have gone to the party if I had felt better. | might | may / will | Je serais peut-être allé à la fête si je m'étais senti mieux. | Might have = aurait peut-être.
If we'd left on time, we ___ stuck in traffic. | wouldn't have gotten | won't get / didn't get | Si nous étions partis à l'heure, nous n'aurions pas été coincés dans la circulation. | Wouldn't have + participe.
If she ___ the bus, she would have been on time. | had taken | took / would take | Si elle avait pris l'autobus, elle aurait été à l'heure. | If + past perfect.
If I'd been born in Canada, I ___ French now. | would speak | would have spoken yesterday / spoke | Si j'étais né au Canada, je parlerais français maintenant. | Mixte : passé → présent.
""",

"wishEnExercises": """
I wish I ___ younger. | were | am / would be | J'aimerais être plus jeune. | Regret présent : wish + prétérit (were).
I wish I ___ a car. Taking the bus is so slow. | had | have / would have | J'aimerais avoir une voiture. Prendre l'autobus, c'est si lent. | Wish + prétérit.
She wishes she ___ in California. | lived | lives / would live | Elle aimerait vivre en Californie. | Wish + prétérit.
I wish I ___ the answer. | knew | know / would know | J'aimerais connaître la réponse. | Wish + prétérit.
I wish I ___ to the doctor sooner. | had gone | went / would go | J'aurais aimé aller chez le médecin plus tôt. | Regret passé : wish + past perfect.
He wishes he ___ more when he was young. | had traveled | traveled / would travel | Il aurait aimé voyager davantage quand il était jeune. | Wish + past perfect.
I wish you ___ so much noise. | wouldn't make | don't make / hadn't made | J'aimerais que tu fasses moins de bruit. | Agacement : wish + would.
I wish it ___ stop raining. | would | will / had | J'aimerais qu'il arrête de pleuvoir. | Wish + would : souhait d'un changement.
If only I ___ more time! | had | have / would have | Si seulement j'avais plus de temps ! | If only + prétérit.
If only I ___ listened to my mother. | had | have / would | Si seulement j'avais écouté ma mère. | If only + past perfect.
I wish I ___ swim. | could | can / would | J'aimerais savoir nager. | Wish + could.
I wish I ___ go with you, but I have to work. | could | can / would | J'aimerais pouvoir venir avec toi, mais je dois travailler. | Wish + could.
I wish I ___ eaten so much cake. | hadn't | didn't / wouldn't | J'aurais mieux fait de ne pas manger autant de gâteau. | Wish + hadn't + participe.
Do you wish you ___ more money? | had | have / would have | Aimerais-tu avoir plus d'argent ? | Wish + prétérit.
I ___ you have a great trip! | hope | wish that / would | J'espère que tu feras un excellent voyage ! | Un souhait réaliste : hope.
I ___ you a happy birthday! | wish | hope / want that | Je te souhaite un joyeux anniversaire ! | Wish + personne + nom = souhaiter.
She wishes her boss ___ give her a raise. | would | will / had | Elle aimerait que son patron lui donne une augmentation. | Wish + would.
I wish I ___ so shy. | weren't | wasn't being / am not | J'aimerais ne pas être si timide. | Wish + weren't.
They wish they ___ that house. It has so many problems. | hadn't bought | didn't buy / wouldn't buy | Ils regrettent d'avoir acheté cette maison. Elle a tant de problèmes. | Wish + hadn't + participe.
If only it ___ Friday! | were | is / would | Si seulement on était vendredi ! | If only + were.
I wish I ___ what to say. | knew | know / had know | J'aimerais savoir quoi dire. | Wish + prétérit.
I wish you ___ here. | were | are / will be | J'aimerais que tu sois là. | Wish + were.
He wishes he ___ accepted the offer. | had | has / would | Il regrette de ne pas avoir accepté l'offre. | Wish + had + participe.
I wish people ___ drive more carefully. | would | will / had | J'aimerais que les gens conduisent plus prudemment. | Wish + would : critique.
If only we ___ left earlier! | had | have / would | Si seulement nous étions partis plus tôt ! | If only + past perfect.
I wish I ___ a bigger kitchen. | had | have / would have | J'aimerais avoir une plus grande cuisine. | Wish + prétérit.
She wishes she ___ moved to the city. | hadn't | didn't / wouldn't | Elle regrette d'avoir déménagé en ville. | Wish + hadn't + participe.
If only I ___ cook like my grandmother! | could | can / would | Si seulement je savais cuisiner comme ma grand-mère ! | If only + could.
I wish the neighbors ___ turn their music down. | would | will / had | J'aimerais que les voisins baissent leur musique. | Wish + would.
He wishes he ___ more time with his kids. | spent | spends / would spend yesterday | Il aimerait passer plus de temps avec ses enfants. | Wish + prétérit.
I wish I ___ sold my old guitar. | hadn't | didn't / wouldn't | Je regrette d'avoir vendu ma vieille guitare. | Wish + hadn't + participe.
""",

"passifAvanceEnExercises": """
I'm going to have my hair ___ tomorrow. | cut | to cut / cutting | Je vais me faire couper les cheveux demain. | Have + objet + participe.
She had her purse ___ on the subway. | stolen | steal / stealing | Elle s'est fait voler son sac dans le métro. | Have + objet + participe : ce qu'on subit.
We need to get the roof ___. | fixed | fix / fixing | Nous devons faire réparer le toit. | Get + objet + participe.
Where do you get your car ___? | serviced | service / servicing | Où fais-tu entretenir ta voiture ? | Get + objet + participe.
He had his teeth ___ last week. | cleaned | clean / cleaning | Il s'est fait détartrer les dents la semaine dernière. | Have + objet + participe.
It is ___ that the company will close. | rumored | rumor / rumoring | La rumeur dit que l'entreprise va fermer. | It is + participe + that.
It ___ believed that he left the country. | is | has / does | On croit qu'il a quitté le pays. | It is believed that.
She is said ___ the best chef in Boston. | to be | being / be | On dit que c'est la meilleure cheffe de Boston. | Be said + to + verbe.
The painting is thought ___ stolen in 1990. | to have been | to be / being | On pense que le tableau a été volé en 1990. | Antériorité : to have been + participe.
He is known ___ a great storyteller. | to be | being / be | On le sait excellent conteur. | Be known + to be.
The house needs to ___ painted. | be | being / been | La maison a besoin d'être repeinte. | Need to be + participe.
The work must ___ done by Friday. | be | being / been | Le travail doit être fait d'ici vendredi. | Modal + be + participe.
This medicine should ___ taken with food. | be | being / been | Ce médicament doit être pris avec de la nourriture. | Should be + participe.
The problem could have ___ avoided. | been | be / being | Le problème aurait pu être évité. | Could have been + participe.
I don't like ___ told what to do. | being | be / to being | Je n'aime pas qu'on me dise quoi faire. | Gérondif passif : being + participe.
She hates ___ interrupted. | being | to being / be | Elle déteste qu'on l'interrompe. | Being + participe.
He expected ___ invited to the wedding. | to be | being / be | Il s'attendait à être invité au mariage. | Infinitif passif : to be + participe.
The dog got ___ by a car. | hit | hitting / to hit | Le chien s'est fait heurter par une voiture. | Get + participe (passif familier).
They got ___ last spring. | married | marry / marrying | Ils se sont mariés au printemps dernier. | Get married.
My application is being ___ right now. | reviewed | review / reviewing | Ma candidature est en cours d'examen. | Is being + participe.
The meeting has been ___ until next week. | postponed | postpone / postponing | La réunion a été reportée à la semaine prochaine. | Has been + participe.
We were ___ to wait in the hallway. | asked | asking / ask | On nous a demandé d'attendre dans le couloir. | Passif d'un verbe à deux compléments.
I was ___ a free ticket. | given | gave / giving | On m'a donné un billet gratuit. | Passif : la personne devient sujet.
The students were ___ a difficult question. | asked | ask / asking | On a posé une question difficile aux élèves. | Was/were asked.
She's having her kitchen ___. | remodeled | remodel / remodeling | Elle fait rénover sa cuisine. | Have + objet + participe.
It's ___ that prices will rise again. | expected | expect / expecting | On s'attend à ce que les prix augmentent encore. | It is expected that.
The suspect is ___ to be armed. | believed | believe / believing | On croit que le suspect est armé. | Be believed + to be.
Nothing has ___ decided yet. | been | be / being | Rien n'a encore été décidé. | Has been + participe.
""",

"futursAvancesEnExercises": """
This time next month, I'll be ___ in Rome. | living | live / lived | Le mois prochain à cette heure-ci, je vivrai à Rome. | Will be + -ing.
By the end of the year, I'll ___ saved $5,000. | have | be / had | D'ici la fin de l'année, j'aurai économisé 5 000 $. | Will have + participe.
Don't come at noon. I'll be ___ lunch. | having | had / have | Ne viens pas à midi. Je serai en train de dîner. | Will be + -ing.
By the time you wake up, I'll have ___. | left | leave / leaving | Le temps que tu te réveilles, je serai parti. | Will have + participe.
In two years, she'll have ___ her degree. | finished | finish / finishing | Dans deux ans, elle aura terminé ses études. | Will have + participe.
At 10 a.m. tomorrow, we'll be ___ over the Atlantic. | flying | flown / fly | Demain à 10 h, nous survolerons l'Atlantique. | Will be + -ing.
Will you be ___ the car this evening? | using | used / use | Vas-tu te servir de la voiture ce soir ? | Question polie : will you be + -ing?
By 2030, the city will have ___ a new subway line. | built | build / building | D'ici 2030, la ville aura construit une nouvelle ligne de métro. | Will have + participe.
Next June, we'll have been ___ for twenty years. | married | marrying / marry | En juin prochain, nous serons mariés depuis vingt ans. | Will have been + état.
By the time he retires, he'll have been ___ for forty years. | working | worked / work | Quand il prendra sa retraite, il aura travaillé quarante ans. | Will have been + -ing.
I won't be ___ to the party. I have to work. | coming | come / came | Je ne viendrai pas à la fête. Je dois travailler. | Won't be + -ing.
She ___ have finished by five. She's very fast. | will | is / does | Elle aura fini d'ici cinq heures. Elle est très rapide. | Will have + participe.
They'll be ___ soon, so let's get ready. | arriving | arrived / arrive | Ils vont bientôt arriver, alors préparons-nous. | Will be + -ing.
How long will you have ___ here by next year? | lived | live / living | Depuis combien de temps auras-tu habité ici l'an prochain ? | Will have + participe.
By the time the guests arrive, we ___ cooked everything. | will have | will be / have | Le temps que les invités arrivent, nous aurons tout cuisiné. | Will have + participe.
This time tomorrow, I'll be ___ my exam. | taking | taken / take | Demain à cette heure-ci, je passerai mon examen. | Will be + -ing.
Don't worry. By the time you get there, the rain will have ___. | stopped | stop / stopping | Ne t'inquiète pas. Le temps que tu arrives, la pluie aura cessé. | Will have + participe.
I'll be ___ you at the station at six. | meeting | met / meet | Je t'attendrai à la gare à six heures. | Will be + -ing.
By Friday, I'll have ___ all the books on the list. | read | reading / reads | D'ici vendredi, j'aurai lu tous les livres de la liste. | Will have + participe.
She'll ___ working late every night this week. | be | have / been | Elle travaillera tard tous les soirs cette semaine. | Will be + -ing.
By the end of the tour, the band will have ___ in fifty cities. | played | play / playing | À la fin de la tournée, le groupe aura joué dans cinquante villes. | Will have + participe.
In ten minutes, the movie will have ___. | started | start / starting | Dans dix minutes, le film aura commencé. | Will have + participe.
Next week, I'll be ___ on a new project. | working | worked / work | La semaine prochaine, je travaillerai sur un nouveau projet. | Will be + -ing.
By the time we get to the cabin, it ___ dark. | will have gotten | will get by / gets | Le temps qu'on arrive au chalet, il fera déjà nuit. | Will have + participe.
Don't call me at nine. I'll ___ putting the kids to bed. | be | have / been | Ne m'appelle pas à neuf heures. Je serai en train de coucher les enfants. | Will be + -ing.
In a year, he'll have ___ all over Europe. | traveled | travel / traveling | Dans un an, il aura voyagé partout en Europe. | Will have + participe (traveled, en américain).
By the time you read this, I'll have ___ Boston. | left | leave / leaving | Quand tu liras ceci, j'aurai quitté Boston. | Will have + participe.
This time next year, she'll be ___ at Harvard. | studying | studied / study | L'an prochain à cette heure-ci, elle étudiera à Harvard. | Will be + -ing.
Will you have ___ the book by our next meeting? | finished | finish / finishing | Auras-tu fini le livre d'ici notre prochaine rencontre ? | Will you have + participe.
We'll be ___ the game on TV tonight. | watching | watched / watch | Nous regarderons le match à la télé ce soir. | Will be + -ing.
By December, they'll have ___ married for a year. | been | be / being | En décembre, ils seront mariés depuis un an. | Will have been.
""",

"modauxPasseEnExercises": """
I'm so tired. I ___ have gone to bed earlier. | should | must / can't | Je suis tellement fatigué. J'aurais dû me coucher plus tôt. | Regret : should have + participe.
You ___ have told her. Now she's upset. | shouldn't | mustn't / couldn't | Tu n'aurais pas dû lui dire. Maintenant, elle est fâchée. | Shouldn't have = n'aurait pas dû.
We could have ___ a taxi, but we walked. | taken | take / took | Nous aurions pu prendre un taxi, mais nous avons marché. | Could have + participe.
He ___ have been at home. His car was in the driveway. | must | should / can't | Il devait être chez lui. Sa voiture était dans l'allée. | Déduction : must have.
She ___ have stolen it. She was with me all day. | can't | must / should | Elle ne peut pas l'avoir volé. Elle était avec moi toute la journée. | Impossibilité : can't have.
I ___ have left my keys in the car. I'm not sure. | might | must / should | J'ai peut-être laissé mes clés dans la voiture. Je ne suis pas sûr. | Possibilité : might have.
You should have ___ me. I would have helped. | called | call / calling | Tu aurais dû m'appeler. Je t'aurais aidé. | Should have + participe.
They ___ have arrived by now. Their flight landed at two. | should | must not / can't | Ils devraient être arrivés à l'heure qu'il est. Leur vol a atterri à deux heures. | Attente : should have.
It was a dangerous jump. He ___ have been killed. | could | must / should | C'était un saut dangereux. Il aurait pu se tuer. | Danger évité : could have.
You ___ have cooked. We're going out for dinner. | needn't | mustn't / couldn't | Tu n'avais pas besoin de cuisiner. Nous sortons souper. | Needn't have = c'était inutile.
I didn't need to ___ a ticket. The concert was free. | buy | have bought / bought | Je n'ai pas eu besoin d'acheter de billet. Le concert était gratuit. | Didn't need to : inutile, donc pas fait.
She must have ___ really hungry. She ate everything. | been | be / being | Elle devait avoir très faim. Elle a tout mangé. | Must have been.
We ___ have gone to the beach, but it rained. | would | must / can't | Nous serions allés à la plage, mais il a plu. | Would have = conditionnel passé.
He can't have ___ the email. He would have answered. | read | reading / reads | Il ne peut pas avoir lu le courriel. Il aurait répondu. | Can't have + participe.
I ___ have done better on the test, but I was tired. | could | must / can't | J'aurais pu faire mieux à l'examen, mais j'étais fatigué. | Could have.
You must have ___ the wrong number. | dialed | dial / dialing | Vous avez dû faire un mauvais numéro. | Must have + participe.
Where's my wallet? Someone ___ have taken it. | must | should / need | Où est mon portefeuille ? Quelqu'un a dû le prendre. | Déduction : must have.
They shouldn't have ___ so late. They missed the start. | arrived | arrive / arriving | Ils n'auraient pas dû arriver si tard. Ils ont raté le début. | Shouldn't have + participe.
She ___ have been sick. She looked fine yesterday. | can't | must / should | Elle ne peut pas avoir été malade. Elle avait l'air bien hier. | Can't have been.
I might ___ forgotten to lock the door. | have | had / has | J'ai peut-être oublié de verrouiller la porte. | Might have + participe.
We ___ have taken the highway. This road is so slow. | should | must / can't | Nous aurions dû prendre l'autoroute. Cette route est si lente. | Should have.
He ___ have heard the news. He looks so happy. | must | can't / shouldn't | Il a dû apprendre la nouvelle. Il a l'air si heureux. | Must have.
You could at least have ___ thank you! | said | say / saying | Tu aurais au moins pu dire merci ! | Could have : reproche.
The package ___ have arrived yesterday, but it didn't. | should | must / can't | Le colis aurait dû arriver hier, mais il n'est pas arrivé. | Should have : ce qui était prévu.
You ___ have parked here. Now you have a ticket. | shouldn't | mustn't / couldn't | Tu n'aurais pas dû te garer ici. Maintenant, tu as une contravention. | Shouldn't have.
She must have ___ the meeting. Her calendar was full. | forgotten | forgot / forget | Elle a dû oublier la réunion. Son agenda était plein. | Must have + participe.
They ___ have gotten lost. They have GPS. | can't | mustn't / shouldn't | Ils ne peuvent pas s'être perdus. Ils ont un GPS. | Can't have.
We ___ have taken more photos. | should | must / can't | Nous aurions dû prendre plus de photos. | Should have : regret.
He might have ___ the wrong train. | taken | took / take | Il a peut-être pris le mauvais train. | Might have + participe.
You ___ have bought milk. We already have two bottles. | needn't | mustn't / couldn't | Tu n'avais pas besoin d'acheter du lait. Nous avons déjà deux bouteilles. | Needn't have : inutile.
""",

"verbesIntroducteursEnExercises": """
She suggested ___ the museum. | visiting | to visit / visit | Elle a proposé de visiter le musée. | Suggest + -ing.
He denied ___ the window. | breaking | to break / break | Il a nié avoir cassé la fenêtre. | Deny + -ing.
They admitted ___ wrong. | being | to be / be | Ils ont reconnu avoir eu tort. | Admit + -ing.
The doctor advised him ___ smoking. | to stop | stopping / stop | Le médecin lui a conseillé d'arrêter de fumer. | Advise + personne + to.
She promised ___ me every day. | to call | calling / call | Elle a promis de m'appeler tous les jours. | Promise + to.
He threatened ___ the police. | to call | calling / call | Il a menacé d'appeler la police. | Threaten + to.
They agreed ___ the costs. | to share | sharing / share | Ils ont accepté de partager les frais. | Agree + to.
She apologized ___ forgetting my birthday. | for | of / about | Elle s'est excusée d'avoir oublié mon anniversaire. | Apologize for + -ing.
He accused me ___ lying. | of | for / about | Il m'a accusé de mentir. | Accuse + personne + of + -ing.
She congratulated me ___ passing the exam. | on | for / of | Elle m'a félicité d'avoir réussi l'examen. | Congratulate + on + -ing.
They blamed him ___ the accident. | for | of / on | Ils l'ont tenu responsable de l'accident. | Blame + personne + for.
My boss encouraged me ___ for the job. | to apply | applying / apply | Mon patron m'a encouragé à postuler. | Encourage + personne + to.
I reminded him ___ his medicine. | to take | taking / take | Je lui ai rappelé de prendre son médicament. | Remind + personne + to.
She warned me ___ the ice. | about | of the / for | Elle m'a mis en garde contre la glace. | Warn + about.
He insisted ___ me home. | on driving | to drive / driving | Il a insisté pour me ramener en voiture. | Insist on + -ing.
They invited us ___ dinner. | to | for to / at | Ils nous ont invités à souper. | Invite + to.
She refused ___ to him. | to speak | speaking / speak | Elle a refusé de lui parler. | Refuse + to.
He offered ___ with the dishes. | to help | helping / help | Il a proposé d'aider à faire la vaisselle. | Offer + to.
The teacher told us ___ quiet. | to be | being / be | L'enseignant nous a dit de rester tranquilles. | Tell + personne + to.
I recommend ___ early. | booking | to book / book | Je recommande de réserver tôt. | Recommend + -ing.
She recommended that he ___ a lawyer. | see | sees / to see | Elle lui a recommandé de voir un avocat. | Recommend that + verbe nu (subjonctif).
He explained ___ the plan had changed. | that | me / me that | Il a expliqué que le plan avait changé. | Explain that (pas « explain me »).
She explained the rules ___ us. | to | for / at | Elle nous a expliqué les règles. | Explain something to someone.
He complained ___ the noise. | about | of the / for | Il s'est plaint du bruit. | Complain about.
They persuaded me ___ with them. | to come | coming / come | Ils m'ont convaincu de venir avec eux. | Persuade + personne + to.
She claimed ___ the president. | to have met | meeting / met | Elle a prétendu avoir rencontré le président. | Claim + to have + participe.
""",

"relativesAvanceesEnExercises": """
My neighbor, ___ dog barks all night, is moving. | whose | who / which | Mon voisin, dont le chien aboie toute la nuit, déménage. | Possession : whose.
Boston, ___ is the capital of Massachusetts, is very old. | which | that / where | Boston, qui est la capitale du Massachusetts, est très ancienne. | Entre virgules : which.
The man ___ next to me on the plane was a doctor. | sitting | sat / who sitting | L'homme assis à côté de moi dans l'avion était médecin. | Relative réduite : -ing.
The car ___ in the accident was a total loss. | damaged | damaging / which damaged | La voiture endommagée dans l'accident était une perte totale. | Relative réduite passive : participe.
She didn't call me back, ___ was strange. | which | what / that | Elle ne m'a pas rappelé, ce qui était étrange. | Which reprend toute la phrase.
I have three brothers, all of ___ are taller than me. | whom | who / them | J'ai trois frères, qui sont tous plus grands que moi. | Après une préposition : whom.
We visited two museums, both of ___ were free. | which | them / what | Nous avons visité deux musées, tous deux gratuits. | Of which, pour des choses.
The people ___ in the house are friendly. | living | lived / who living | Les gens qui habitent la maison sont sympathiques. | Relative réduite active : -ing.
Anyone ___ to join is welcome. | wanting | wanted / who wanting | Toute personne qui veut se joindre à nous est la bienvenue. | Relative réduite : -ing.
The book, ___ was published in 1851, is a classic. | which | that / who | Le livre, publié en 1851, est un classique. | Entre virgules : which.
The woman to ___ I spoke was very helpful. | whom | who / which | La femme à qui j'ai parlé a été très serviable. | Préposition + whom (registre soutenu).
The company for ___ she works is in Ohio. | which | that / who | L'entreprise pour laquelle elle travaille est en Ohio. | Préposition + which.
He lost his job, ___ meant he had to move. | which | that / what | Il a perdu son emploi, ce qui l'a obligé à déménager. | Which reprend la phrase.
The students, most of ___ were tired, went home early. | whom | them / who | Les élèves, dont la plupart étaient fatigués, sont rentrés tôt. | Most of whom.
I met a writer ___ novels I've read. | whose | who / which | J'ai rencontré une écrivaine dont j'ai lu les romans. | Whose + nom.
The goods ___ from China arrived late. | shipped | shipping / which shipped | Les marchandises expédiées de Chine sont arrivées en retard. | Participe passé : sens passif.
The road ___ to the beach is closed. | leading | led / who leads | La route qui mène à la plage est fermée. | Relative réduite : -ing.
Is there anyone ___ can help me? | who | which / whose | Y a-t-il quelqu'un qui peut m'aider ? | Personne, sujet : who.
The reason ___ I'm calling is to apologize. | why | which / what | La raison pour laquelle j'appelle, c'est pour m'excuser. | The reason why.
The day ___ I met her, it was snowing. | — | which / where | Le jour où je l'ai rencontrée, il neigeait. | When peut s'omettre après « the day ».
Our hotel, ___ we'd booked months ago, was overbooked. | which | that / what | Notre hôtel, que nous avions réservé des mois plus tôt, était surréservé. | Entre virgules, complément : which (jamais omis).
She has two cars, neither of ___ works. | which | them / what | Elle a deux voitures, dont aucune ne marche. | Neither of which.
The questions ___ in the exam were difficult. | asked | asking / which asked | Les questions posées à l'examen étaient difficiles. | Participe passé.
That's the hotel ___ the president stayed. | where | which / that | C'est l'hôtel où le président a séjourné. | Lieu : where.
""",

"connecteursEnExercises": """
___ she was tired, she finished the race. | Although | Despite / However | Bien qu'elle soit fatiguée, elle a fini la course. | Although + proposition.
___ her injury, she finished the race. | Despite | Although / However | Malgré sa blessure, elle a fini la course. | Despite + nom.
In spite ___ the snow, the school stayed open. | of | at / from | Malgré la neige, l'école est restée ouverte. | In spite of + nom.
He's rich. ___, he isn't happy. | However | Although / Despite | Il est riche. Pourtant, il n'est pas heureux. | However, en début de phrase, suivi d'une virgule.
My brother loves sports, ___ I prefer reading. | whereas | despite / unless | Mon frère adore le sport, alors que moi je préfère lire. | Whereas = alors que (contraste).
I'll go ___ it's raining. | even if | unless / despite | J'irai même s'il pleut. | Even if = même si.
Bring a sweater ___ it gets cold. | in case | unless / despite | Apporte un chandail au cas où il ferait froid. | In case = au cas où.
I spoke slowly ___ everyone could understand. | so that | in case / despite | J'ai parlé lentement pour que tout le monde comprenne. | So that = pour que.
She left early ___ to get stuck in traffic. | so as not | so that not / in order not that | Elle est partie tôt pour ne pas rester coincée dans la circulation. | So as not to = pour ne pas.
___ having little money, they were happy. | Despite | Although / Even though | Malgré leur manque d'argent, ils étaient heureux. | Despite + -ing.
___ the fact that it was late, we kept talking. | Despite | Although / However | Bien qu'il fût tard, nous avons continué à parler. | Despite the fact that + proposition.
We'll have the party outside ___ it rains. | unless | in case / so that | Nous ferons la fête dehors, sauf s'il pleut. | Unless = sauf si.
___ you leave now, you'll miss the train. | Unless | Despite / Although | À moins de partir maintenant, tu vas rater le train. | Unless = si … ne … pas.
The flight was delayed. ___, we missed our connection. | As a result | Although / Despite | Le vol a été retardé. Par conséquent, nous avons raté notre correspondance. | As a result = par conséquent.
He studied hard. ___, he failed the exam. | Nevertheless | Therefore / Because | Il a beaucoup étudié. Il a pourtant échoué à l'examen. | Nevertheless = néanmoins.
It was raining; ___, the game was canceled. | therefore | however / although | Il pleuvait ; le match a donc été annulé. | Therefore = donc.
___ though I've lived here for years, I still get lost. | Even | Although / Despite | Même si j'habite ici depuis des années, je me perds encore. | Even though = même si (fait réel).
She kept smiling ___ she was nervous. | although | despite / however | Elle continuait de sourire bien qu'elle soit nerveuse. | Although + proposition.
The hotel was great, ___ the food was terrible. | but | despite / unless | L'hôtel était super, mais la nourriture était affreuse. | But = mais.
___ I know, the store closes at nine. | As far as | As long as / As well as | Autant que je sache, le magasin ferme à neuf heures. | As far as I know.
You can borrow my car ___ you bring it back by six. | as long as | as far as / even though | Tu peux emprunter ma voiture à condition de la ramener avant six heures. | As long as = à condition que.
___ his age, he runs marathons. | Despite | Although / However | Malgré son âge, il court des marathons. | Despite + nom.
She's a great singer. ___, she can dance. | Besides | Beside / Despite | C'est une excellente chanteuse. En plus, elle sait danser. | Besides = en plus.
We took a taxi ___ we were late. | because | so that / despite | Nous avons pris un taxi parce que nous étions en retard. | Because = parce que.
We were late, ___ we took a taxi. | so | because / although | Nous étions en retard, alors nous avons pris un taxi. | So = alors (conséquence).
""",

"phrasalVerbs2EnExercises": """
I'm really looking forward ___ the holidays. | to | for / at | J'ai vraiment hâte aux vacances. | Look forward to + nom ou -ing.
We need to cut ___ on sugar. | down | off / out | Nous devons réduire le sucre. | Cut down on = réduire.
She's always putting ___ her homework until the last minute. | off | out / on | Elle remet toujours ses devoirs à la dernière minute. | Put off = remettre à plus tard.
Can you figure ___ how this machine works? | out | up / on | Arrives-tu à comprendre comment marche cette machine ? | Figure out = comprendre, trouver.
The story turned ___ to be true. | out | up / over | L'histoire s'est révélée vraie. | Turn out = s'avérer.
He showed ___ two hours late. | up | out / off | Il s'est pointé avec deux heures de retard. | Show up = arriver, se présenter.
Let's not bring ___ politics at dinner. | up | out / on | N'abordons pas la politique au souper. | Bring up = aborder (un sujet).
I'll look ___ the problem and call you back. | into | at / up | Je vais examiner le problème et te rappeler. | Look into = examiner.
She looks ___ to her older sister. | up | over / after | Elle admire sa grande sœur. | Look up to = admirer.
He looks ___ on people without money. | down | up / over | Il méprise les gens sans argent. | Look down on = mépriser.
We need to come up ___ a solution. | with | to / for | Nous devons trouver une solution. | Come up with = trouver.
I came ___ an old photo in a drawer. | across | over / up | Je suis tombé sur une vieille photo dans un tiroir. | Come across = tomber sur.
The company is trying to cut ___ costs. | down on | down to / off from | L'entreprise essaie de réduire les coûts. | Cut down on.
They set ___ a new business last year. | up | out / off | Ils ont créé une nouvelle entreprise l'an dernier. | Set up = créer, mettre en place.
The war broke ___ in 1861. | out | up / down | La guerre a éclaté en 1861. | Break out = éclater.
Can you fill me ___ on what happened? | in | up / out | Tu peux me mettre au courant de ce qui s'est passé ? | Fill someone in = mettre au courant.
I need to catch ___ on sleep. | up | out / on | J'ai besoin de rattraper mon sommeil. | Catch up on = rattraper.
She turned ___ the job because the pay was too low. | down | off / out | Elle a refusé le poste parce que le salaire était trop bas. | Turn down = refuser.
The meeting dragged ___ for three hours. | on | out / up | La réunion a traîné pendant trois heures. | Drag on = s'éterniser.
He pointed ___ a mistake in my report. | out | up / over | Il a signalé une erreur dans mon rapport. | Point out = signaler.
I'll pick ___ some bread on the way home. | up | out / on | Je prendrai du pain en rentrant. | Pick up = acheter en passant.
Don't let me ___. I'm counting on you. | down | off / out | Ne me laisse pas tomber. Je compte sur toi. | Let down = décevoir.
They called ___ the wedding at the last minute. | off | out / up | Ils ont annulé le mariage à la dernière minute. | Call off = annuler.
She takes ___ her father — same eyes, same laugh. | after | over / up | Elle tient de son père : mêmes yeux, même rire. | Take after = ressembler à.
A new manager will take ___ next month. | over | after / up | Un nouveau gérant prendra la relève le mois prochain. | Take over = prendre la direction.
We had to put ___ the trip because of the storm. | off | out / up | Nous avons dû reporter le voyage à cause de la tempête. | Put off = reporter.
Can you look ___ my plants while I'm away? | after | for / into | Peux-tu t'occuper de mes plantes pendant mon absence ? | Look after = s'occuper de.
We need to sort ___ this problem today. | out | up / off | Nous devons régler ce problème aujourd'hui. | Sort out = régler.
He made ___ an excuse for being late. | up | out / off | Il a inventé une excuse pour son retard. | Make up = inventer.
I can't make ___ what he's saying. | out | up / off | Je n'arrive pas à comprendre ce qu'il dit. | Make out = distinguer.
She gave ___ chocolate for a month. | up | in / out | Elle a renoncé au chocolat pendant un mois. | Give up = renoncer à.
""",

"fauxAmisB2EnExercises": """
The project was a success. ___, we finished it on time. | Eventually | Possibly / Actually | Le projet a été une réussite. Finalement, nous l'avons terminé à temps. | Finalement = eventually.
I can ___ change the date, if you prefer. | possibly | eventually / actually | Je peux éventuellement changer la date, si tu préfères. | Éventuellement = possibly.
It would be ___ to save some money. | sensible | sensitive / sensibly | Il serait raisonnable d'économiser un peu d'argent. | Raisonnable = sensible.
Don't be so ___ — it was just a joke. | sensitive | sensible / sensual | Ne sois pas si susceptible, c'était juste une blague. | Sensible, susceptible = sensitive.
Over a thousand people ___ the conference. | attended | assisted / waited | Plus de mille personnes ont assisté à la conférence. | Assister à = attend.
A nurse ___ the doctor during the operation. | assisted | attended / helped at | Une infirmière a assisté le médecin pendant l'opération. | Aider = assist.
The ___ situation is difficult. | current | actual / actually | La situation actuelle est difficile. | Actuel = current.
What's the ___ reason he left? | real | current / present | Quelle est la vraie raison de son départ ? | Réel, véritable = real (ou actual).
I've ___ my goal: I ran a marathon. | achieved | finished / ended | J'ai atteint mon objectif : j'ai couru un marathon. | Réaliser, atteindre = achieve.
Can you ___ the report by tonight? | finish | achieve / end up | Peux-tu terminer le rapport d'ici ce soir ? | Achever = finish.
She ___ to be sick so she could stay home. | pretended | claimed / pretends | Elle a fait semblant d'être malade pour rester à la maison. | Faire semblant = pretend.
He ___ that he had never met her. | claimed | pretended / pretend | Il a prétendu ne l'avoir jamais rencontrée. | Prétendre (affirmer) = claim.
The professor gave a ___ on climate change. | lecture | reading / conference reading | Le professeur a donné un cours magistral sur le climat. | Cours magistral = lecture.
I do a lot of ___ on the train. | reading | lecture / lectures | Je lis beaucoup dans le train. | La lecture = reading.
We need to ___ the meeting after lunch. | resume | summarize / resumé | Nous devons reprendre la réunion après le dîner. | Reprendre = resume.
Please ___ the main points of the article. | summarize | resume / sum | Résume les points principaux de l'article, s'il te plaît. | Résumer = summarize.
She didn't ___ that the store was closed. | realize | achieve / carry out | Elle ne s'était pas rendu compte que le magasin était fermé. | Se rendre compte = realize.
Her parents were very ___ when she lost her job. | supportive | supporting / supportable | Ses parents l'ont beaucoup soutenue quand elle a perdu son emploi. | Qui soutient = supportive.
I can't ___ his attitude anymore. | stand | support / sustain | Je ne supporte plus son attitude. | Supporter (tolérer) = stand.
Their train ___ was nine hours long. | journey | day / journal | Leur trajet en train a duré neuf heures. | Trajet = journey (ou trip).
I read the ___ every morning. | newspaper | journal / journey | Je lis le journal tous les matins. | Le journal = the newspaper.
She keeps a ___ where she writes every night. | journal | newspaper / journey | Elle tient un journal où elle écrit chaque soir. | Journal intime = journal (ou diary).
The concert was a total ___. Nobody came. | disappointment | deception / delusion | Le concert a été une immense déception. Personne n'est venu. | Déception = disappointment.
There's a ___ of three hours for all flights. | delay | deadline / delai | Il y a un retard de trois heures sur tous les vols. | Retard = delay.
""",
}
