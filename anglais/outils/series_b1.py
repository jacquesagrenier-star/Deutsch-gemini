# -*- coding: utf-8 -*-
"""Les series B1 allongees (28 oct. 2026) : des questions a la suite des
douze de chaque fiche (grammaire_b1.py), pour approcher le volume des series
allemandes. Meme format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

SUPPLEMENTS = {
"ppContinuEnExercises": """
I've been ___ this report since eight o'clock. | writing | wrote / write | J'écris ce rapport depuis huit heures. | Have been + -ing.
She's ___ waiting for the bus for twenty minutes. | been | being / be | Elle attend l'autobus depuis vingt minutes. | Has been + -ing.
How long ___ you been living in Boston? | have | did / are | Depuis combien de temps habites-tu à Boston ? | How long have you been + -ing?
It's been ___ all night. The streets are flooded. | raining | rain / rained | Il a plu toute la nuit. Les rues sont inondées. | Has been + -ing : traces visibles.
They ___ been arguing all morning. | have | has / are | Ils se disputent depuis ce matin. | They have been.
He ___ been working here for long. He started in May. | hasn't | haven't / isn't | Il ne travaille pas ici depuis longtemps. Il a commencé en mai. | Négation : hasn't been.
Your hands are dirty. What have you been ___? | doing | done / do | Tu as les mains sales. Qu'est-ce que tu as fait ? | Activité récente : been + -ing.
I've been ___ to call you all week. | trying | tried / try | J'essaie de t'appeler depuis le début de la semaine. | Have been + -ing.
We've been ___ about moving to Denver. | thinking | thought / think | Nous pensons à déménager à Denver. | Have been + -ing.
I've ___ this movie three times. | seen | been seeing / seeing | J'ai vu ce film trois fois. | Un nombre de fois : simple.
She has ___ two cups of coffee already. | had | been having / having | Elle a déjà bu deux tasses de café. | Un résultat chiffré : simple.
I've been ___ my keys for ten minutes. Have you seen them? | looking for | looked for / look for | Je cherche mes clés depuis dix minutes. Tu les as vues ? | Have been + -ing.
I've ___ my keys! Here they are. | found | been finding / finding | J'ai trouvé mes clés ! Les voici. | Une action unique et finie : simple.
How long has she ___ for the company? | been working | worked since / works | Depuis combien de temps travaille-t-elle pour l'entreprise ? | How long + been + -ing.
I've ___ him for years. | known | been knowing / knowing | Je le connais depuis des années. | Know : verbe d'état, jamais au continu.
She's ___ that car since 2015. | had | been having / having | Elle a cette voiture depuis 2015. | Have (posséder) : verbe d'état.
The kids have been ___ video games all afternoon. | playing | played / play | Les enfants jouent aux jeux vidéo depuis le début de l'après-midi. | Have been + -ing.
We've been ___ for this trip for months. | saving | saved / save | Nous économisons pour ce voyage depuis des mois. | Have been + -ing.
I'm sorry I'm late. Have you been ___ long? | waiting | waited / wait | Désolé du retard. Tu attends depuis longtemps ? | Have you been + -ing?
He's been ___ a lot lately. He looks tired. | working | worked / works | Il travaille beaucoup ces temps-ci. Il a l'air fatigué. | Lately + have been + -ing.
I've been feeling sick ___ yesterday. | since | for / ago | Je me sens malade depuis hier. | Point de départ : since.
She's been studying Japanese ___ three years. | for | since / ago | Elle étudie le japonais depuis trois ans. | Durée : for.
It ___ snowing since Monday. | has been | is / was being | Il neige depuis lundi. | Has been + -ing.
We ___ been talking about you! | have | has / are | On parlait justement de toi ! | We have been + -ing.
Someone's ___ eating my cookies! There are only two left. | been | being / be | Quelqu'un a mangé mes biscuits ! Il n'en reste que deux. | Has been + -ing : traces.
I've ___ painting the fence, but I haven't finished. | been | being / be | J'ai peint la clôture, mais je n'ai pas fini. | Activité pas finie : continu.
I've ___ the fence. Doesn't it look great? | painted | been painting / paint | J'ai peint la clôture. Elle est belle, non ? | Le travail fini : simple.
I've been ___ a lot of podcasts lately. | listening to | listened to / listen to | J'écoute beaucoup de balados ces temps-ci. | Have been + -ing.
My back has been ___ since the accident. | hurting | hurt / hurts | J'ai mal au dos depuis l'accident. | Has been + -ing.
I haven't been ___ much TV recently. | watching | watched / watch | Je ne regarde pas beaucoup la télé ces derniers temps. | Haven't been + -ing.
""",

"pastPerfectEnExercises": """
I ___ never eaten sushi before I went to Japan. | had | have / did | Je n'avais jamais mangé de sushis avant d'aller au Japon. | Avant un autre passé : had + participe.
When we arrived, the party ___ already ended. | had | has / was | Quand nous sommes arrivés, la fête était déjà finie. | Had + participe.
She was upset because she ___ her job. | had lost | has lost / loses | Elle était bouleversée parce qu'elle avait perdu son emploi. | La cause antérieure : past perfect.
By the time I woke up, my roommate ___ to work. | had gone | has gone / goes | Le temps que je me réveille, mon colocataire était parti travailler. | By the time + past perfect.
I ___ the movie before, so I knew the ending. | had seen | have seen / see | J'avais déjà vu le film, alors je connaissais la fin. | Had + participe.
He said he ___ to Boston twice. | had been | has been / is | Il a dit qu'il était allé deux fois à Boston. | Discours rapporté : had been.
After she ___ the dishes, she sat down. | had done | has done / does | Après avoir fait la vaisselle, elle s'est assise. | After + past perfect.
We ___ waited long when the doctor came in. | hadn't | haven't / didn't | Nous n'avions pas attendu longtemps quand le médecin est entré. | Négation : hadn't + participe.
___ she left when you got there? | Had | Has / Did | Était-elle déjà partie quand tu es arrivé ? | Question : Had + sujet + participe.
I realized I ___ my umbrella on the bus. | had left | have left / leave | Je me suis rendu compte que j'avais oublié mon parapluie dans l'autobus. | Antériorité : past perfect.
They ___ dinner when I called, so they didn't answer. | were having | had had / have | Ils étaient en train de souper quand j'ai appelé, alors ils n'ont pas répondu. | Action en cours : past continuous.
They ___ dinner when I called, so they were free to talk. | had finished | have finished / finished up | Ils avaient fini de souper quand j'ai appelé, alors ils pouvaient parler. | Action terminée avant : past perfect.
It was the best meal I ___ ever eaten. | had | have / did | C'était le meilleur repas que j'aie jamais mangé. | Superlatif dans un récit : had ever.
The ground was white. It ___ during the night. | had snowed | has snowed / snows | Le sol était blanc. Il avait neigé pendant la nuit. | Explication antérieure.
He ___ the email before he read my message. | had sent | has sent / sends | Il avait envoyé le courriel avant de lire mon message. | Had + participe.
I didn't know who she was. I ___ met her before. | hadn't | haven't / didn't | Je ne savais pas qui elle était. Je ne l'avais jamais rencontrée. | Hadn't + participe.
When I got home, I found that someone ___ into the house. | had broken | has broken / breaks | En rentrant, j'ai découvert que quelqu'un était entré par effraction. | Had + participe.
She ___ in Montreal for years before she moved to Boston. | had lived | has lived / lives | Elle avait vécu des années à Montréal avant d'emménager à Boston. | Durée avant un passé.
The movie ___ started by the time we found our seats. | had | has / have | Le film avait commencé le temps qu'on trouve nos places. | Had + participe.
I was hungry because I ___ eaten all day. | hadn't | haven't / didn't | J'avais faim parce que je n'avais rien mangé de la journée. | Hadn't + participe.
As soon as he ___ the news, he called his mother. | had heard | has heard / hears | Dès qu'il a appris la nouvelle, il a appelé sa mère. | As soon as + past perfect.
They asked me if I ___ the report. | had read | have read / reading | Ils m'ont demandé si j'avais lu le rapport. | Discours rapporté : had + participe.
The teacher was angry because nobody ___ their homework. | had done | has done / does | L'enseignante était fâchée parce que personne n'avait fait ses devoirs. | Had + participe.
I'd never ___ a moose until I visited Maine. | seen | saw / see | Je n'avais jamais vu d'orignal avant de visiter le Maine. | 'd = had, suivi d'un participe.
By 2015, he ___ three novels. | had written | has written / writes | En 2015, il avait écrit trois romans. | By + date passée : past perfect.
When she opened the box, she saw that the cake ___. | had melted | has melted / melts | Quand elle a ouvert la boîte, elle a vu que le gâteau avait fondu. | Had + participe.
He felt better after he ___ a nap. | had taken | has taken / takes | Il s'est senti mieux après avoir fait une sieste. | After + past perfect.
I knew the city well because I ___ there as a student. | had lived | have lived / live | Je connaissais bien la ville parce que j'y avais vécu étudiant. | Had + participe.
Everyone ___ gone home when the fire alarm went off. | had | has / have | Tout le monde était rentré quand l'alarme incendie s'est déclenchée. | Had + participe.
""",

"conditionnelsEnExercises": """
If it ___ sunny tomorrow, we'll go to the beach. | is | will be / would be | S'il fait soleil demain, nous irons à la plage. | Conditionnel 1 : if + présent, will.
If you ___ now, you'll catch the train. | leave | will leave / left | Si tu pars maintenant, tu attraperas le train. | If + présent.
If I see Tom, I ___ him. | 'll tell | told / would told | Si je vois Tom, je lui dirai. | Conditionnel 1 : will + verbe nu.
If she ___ the job, she'll move to Chicago. | gets | will get / got | Si elle obtient le poste, elle déménagera à Chicago. | If + présent.
If I ___ a car, I'd drive to work. | had | have / would have | Si j'avais une voiture, j'irais au travail en voiture. | Conditionnel 2 : if + prétérit.
If we ___ more time, we would visit Vermont. | had | have / will have | Si nous avions plus de temps, nous visiterions le Vermont. | If + prétérit.
If I won the lottery, I ___ quit my job. | would | will / did | Si je gagnais à la loterie, je quitterais mon emploi. | Would + verbe nu.
What would you do if you ___ a million dollars? | had | have / would have | Que ferais-tu si tu avais un million de dollars ? | If + prétérit.
If he ___ so much, he wouldn't be so tired. | didn't work | doesn't work / wouldn't work | S'il ne travaillait pas autant, il ne serait pas si fatigué. | Négation au prétérit.
If you mix blue and yellow, you ___ green. | get | would get / got | Si on mélange le bleu et le jaune, on obtient du vert. | Vérité générale : if + présent, présent.
If you ___ water to 100 degrees, it boils. | heat | will heat / would heat | Si on chauffe l'eau à 100 degrés, elle bout. | Vérité générale : présent des deux côtés.
I'll call you ___ I need help. | if | unless / when not | Je t'appellerai si j'ai besoin d'aide. | Si = if.
You can't come in ___ you have a ticket. | unless | if / when | Tu ne peux pas entrer à moins d'avoir un billet. | Unless = à moins que, si … ne … pas.
___ you hurry, you'll be late. | Unless | If / Without | Si tu ne te dépêches pas, tu seras en retard. | Unless = if not.
If I ___ you, I wouldn't buy that. | were | was being / am | Si j'étais toi, je n'achèterais pas ça. | If I were you.
If she lived closer, we ___ each other more often. | would see | will see / saw | Si elle habitait plus près, nous nous verrions plus souvent. | Would + verbe nu.
If you ___ tired, go to bed. | are | were / would be | Si tu es fatigué, va te coucher. | If + présent, impératif.
I'd travel more if I ___ afraid of flying. | weren't | wasn't being / am not | Je voyagerais davantage si je n'avais pas peur de l'avion. | If + prétérit (were).
If it ___ this weekend, the game will be canceled. | snows | will snow / snowed | S'il neige ce week-end, le match sera annulé. | If + présent.
If they ___ the price, more people would buy it. | lowered | lower / will lower | S'ils baissaient le prix, plus de gens l'achèteraient. | If + prétérit.
Would you help me if I ___ you? | asked | ask / will ask | M'aiderais-tu si je te le demandais ? | If + prétérit.
If you don't wear a coat, you ___ cold. | 'll get | would get / got | Si tu ne mets pas de manteau, tu auras froid. | Conditionnel 1.
As long as you ___ careful, you can borrow my car. | are | will be / were | Tant que tu fais attention, tu peux emprunter ma voiture. | As long as + présent.
If I ___ how to cook, I'd make dinner. | knew | know / would know | Si je savais cuisiner, je ferais le souper. | If + prétérit.
She'd be happier if she ___ a new job. | found | finds / will find | Elle serait plus heureuse si elle trouvait un nouvel emploi. | If + prétérit.
If you see my brother, ___ him to call me. | tell | you tell / will tell | Si tu vois mon frère, dis-lui de m'appeler. | If + présent, impératif.
If the store ___ open, we'll buy some bread. | is | will be / would be | Si le magasin est ouvert, nous achèterons du pain. | If + présent.
If dogs could talk, what ___ they say? | would | will / do | Si les chiens pouvaient parler, que diraient-ils ? | Situation imaginaire : would.
""",

"passifEnExercises": """
This house ___ built in 1850. | was | is / has | Cette maison a été construite en 1850. | Passif au passé : was + participe.
Coffee ___ grown in Colombia. | is | was being / has | On cultive du café en Colombie. | Passif au présent : is + participe.
The thief ___ caught by the police. | was | is being / has | Le voleur a été attrapé par la police. | Was + participe.
The windows are ___ every week. | cleaned | cleaning / clean | On nettoie les fenêtres chaque semaine. | Are + participe.
The new library will ___ next year. | be opened | open / be opening | La nouvelle bibliothèque ouvrira l'an prochain. | Will be + participe.
Our flight has ___ canceled. | been | be / being | Notre vol a été annulé. | Has been + participe.
The cake was made ___ my grandmother. | by | from / of | Le gâteau a été fait par ma grand-mère. | L'auteur de l'action : by.
The car is ___ washed right now. | being | been / be | La voiture est en train d'être lavée. | Is being + participe.
The emails ___ sent this morning. | were | was / are | Les courriels ont été envoyés ce matin. | Pluriel au passé : were.
Many books ___ written about the war. | have been | has been / are being written | Beaucoup de livres ont été écrits sur la guerre. | Have been + participe.
The museum ___ visited by thousands of people every year. | is | are / has | Le musée est visité par des milliers de personnes chaque année. | Is + participe.
I ___ born in Quebec City. | was | am / have been | Je suis né à Québec. | Être né = was born.
Where ___ you born? | were | are / did | Où es-tu né ? | Question : Were you born…?
The keys were ___ in the car. | found | find / founded | Les clés ont été retrouvées dans la voiture. | Find → found.
The game was ___ because of the rain. | canceled | cancel / canceling | Le match a été annulé à cause de la pluie. | Was + participe.
The phone ___ invented by Alexander Graham Bell. | was | is / has | Le téléphone a été inventé par Alexander Graham Bell. | Was + participe.
These shoes ___ made in Italy. | are | is / has | Ces chaussures sont fabriquées en Italie. | Pluriel : are + participe.
The package will be ___ tomorrow. | delivered | deliver / delivering | Le colis sera livré demain. | Will be + participe.
You ___ allowed to park here. | aren't | don't / haven't | Tu n'as pas le droit de stationner ici. | Négation : aren't allowed.
The meeting ___ been moved to Friday. | has | have / is | La réunion a été déplacée à vendredi. | Has been + participe.
The bridge is ___ repaired. It will reopen in May. | being | been / be | Le pont est en réparation. Il rouvrira en mai. | Is being + participe.
The building ___ destroyed by a fire in 1872. | was | is / were | L'immeuble a été détruit par un incendie en 1872. | Was + participe.
The winner ___ announced tonight. | will be | will / has | Le gagnant sera annoncé ce soir. | Will be + participe.
French is ___ in Quebec. | spoken | speaking / spoke | On parle français au Québec. | Is + participe.
This room ___ cleaned yet. | hasn't been | isn't / didn't | Cette chambre n'a pas encore été nettoyée. | Hasn't been + participe.
The children ___ taken to school by bus. | are | is / has | Les enfants sont conduits à l'école en autobus. | Are + participe.
The song was ___ by a famous singer. | written | wrote / write | La chanson a été écrite par un chanteur célèbre. | Write → written.
Has the bill ___ paid? | been | be / being | La facture a-t-elle été payée ? | Has … been + participe.
Mistakes ___ made. | were | was / has | Des erreurs ont été commises. | Pluriel : were + participe.
The museum ___ closed on Mondays. | is | are / has | Le musée est fermé le lundi. | Is + participe.
These photos ___ taken in Maine last summer. | were | was / are | Ces photos ont été prises dans le Maine l'été dernier. | Were + participe.
Dinner will ___ served at seven. | be | being / been | Le souper sera servi à sept heures. | Will be + participe.
The tickets have already ___ sold out. | been | be / being | Les billets ont déjà tous été vendus. | Have been + participe.
The new road ___ being built right now. | is | are / has | La nouvelle route est en construction en ce moment. | Is being + participe.
""",

"discoursIndirectEnExercises": """
« I'm hungry. » → He said he ___ hungry. | was | is / has been | « J'ai faim. » → Il a dit qu'il avait faim. | Présent → prétérit.
« I like jazz. » → She said she ___ jazz. | liked | likes / has liked | « J'aime le jazz. » → Elle a dit qu'elle aimait le jazz. | Présent → prétérit.
« I'm leaving. » → He said he ___ leaving. | was | is / were | « Je pars. » → Il a dit qu'il partait. | Am → was.
« I'll call you. » → She said she ___ call me. | would | will / should | « Je t'appellerai. » → Elle a dit qu'elle m'appellerait. | Will → would.
« I can drive. » → He said he ___ drive. | could | can / would | « Je sais conduire. » → Il a dit qu'il savait conduire. | Can → could.
« I saw the movie. » → She said she ___ the movie. | had seen | has seen / sees | « J'ai vu le film. » → Elle a dit qu'elle avait vu le film. | Prétérit → past perfect.
« I've finished. » → He said he ___. | had finished | has finished / finishes | « J'ai fini. » → Il a dit qu'il avait fini. | Present perfect → past perfect.
« We must go. » → They said they ___ go. | had to | must have / have | « Nous devons partir. » → Ils ont dit qu'ils devaient partir. | Must → had to.
He ___ me he was sorry. | told | said / spoke | Il m'a dit qu'il était désolé. | Tell + personne.
She ___ she was sorry. | said | told / told me to | Elle a dit qu'elle était désolée. | Say, sans personne.
He said ___ me that he was busy. | to | at / for | Il m'a dit qu'il était occupé. | Say something to someone.
« Do you like it? » → She asked me ___ I liked it. | if | that / do | « Tu aimes ? » → Elle m'a demandé si j'aimais. | Question fermée : if.
« Where is the station? » → He asked where the station ___. | was | is it / was it | « Où est la gare ? » → Il a demandé où était la gare. | Pas d'inversion dans la question rapportée.
« What time is it? » → She asked me what time ___. | it was | was it / is it | « Quelle heure est-il ? » → Elle m'a demandé l'heure. | Sujet + verbe, sans inversion.
« Close the door. » → He told me ___ the door. | to close | close / closing | « Ferme la porte. » → Il m'a dit de fermer la porte. | Ordre rapporté : tell + to.
« Don't be late. » → She told us ___ late. | not to be | to not be / don't be | « Ne soyez pas en retard. » → Elle nous a dit de ne pas être en retard. | Ordre négatif : not to.
« Can you help me? » → He asked me ___ help him. | to | if / for | « Tu peux m'aider ? » → Il m'a demandé de l'aider. | Demande : ask + to.
« I'm working today. » → She said she was working ___. | that day | today / yesterday | « Je travaille aujourd'hui. » → Elle a dit qu'elle travaillait ce jour-là. | Today → that day.
« I saw him yesterday. » → He said he had seen him ___. | the day before | yesterday / tomorrow | « Je l'ai vu hier. » → Il a dit qu'il l'avait vu la veille. | Yesterday → the day before.
« I'll do it tomorrow. » → She said she would do it ___. | the next day | tomorrow / yesterday | « Je le ferai demain. » → Elle a dit qu'elle le ferait le lendemain. | Tomorrow → the next day.
« This is my car. » → He said that was ___ car. | his | my / her | « C'est ma voiture. » → Il a dit que c'était sa voiture. | Les possessifs changent avec la personne.
« Are you coming? » → They asked ___ I was coming. | whether | that / do | « Tu viens ? » → Ils ont demandé si je venais. | If ou whether.
« How old are you? » → She asked me how old ___. | I was | was I / am I | « Quel âge as-tu ? » → Elle m'a demandé mon âge. | Sujet + verbe.
« I don't know. » → He said he ___ know. | didn't | doesn't / hadn't | « Je ne sais pas. » → Il a dit qu'il ne savait pas. | Don't → didn't.
« We're going to move. » → They said they ___ going to move. | were | are / have been | « Nous allons déménager. » → Ils ont dit qu'ils allaient déménager. | Are → were.
« Why are you crying? » → She asked me why ___. | I was crying | was I crying / am I crying | « Pourquoi pleures-tu ? » → Elle m'a demandé pourquoi je pleurais. | Sujet + verbe.
« I may be late. » → He said he ___ be late. | might | may have / can | « Je serai peut-être en retard. » → Il a dit qu'il serait peut-être en retard. | May → might.
She told me she ___ me later. | would call | will call / calls | Elle m'a dit qu'elle m'appellerait plus tard. | Will → would.
""",

"relativesEnExercises": """
The woman ___ teaches us is from Ireland. | who | which / whose | La femme qui nous enseigne est irlandaise. | Une personne, sujet : who.
The book ___ is on the table is mine. | which | who / whose | Le livre qui est sur la table est à moi. | Une chose : which (ou that).
I have a friend ___ brother plays for the Red Sox. | whose | who / which | J'ai un ami dont le frère joue pour les Red Sox. | Possession : whose.
That's the café ___ we first met. | where | which / who | C'est le café où nous nous sommes rencontrés. | Un lieu : where.
2020 was the year ___ everything changed. | when | where / which | 2020 a été l'année où tout a changé. | Un moment : when.
The man ___ I met yesterday is a chef. | — | whose / which | L'homme que j'ai rencontré hier est chef cuisinier. | Pronom complément : on peut l'omettre.
This is the car ___ I want to buy. | that | who / whose | C'est la voiture que je veux acheter. | Une chose, complément : that (ou rien).
The people ___ live upstairs are very noisy. | who | which / whose | Les gens qui habitent en haut sont très bruyants. | Personnes, sujet : who.
I didn't hear ___ she said. | what | that / which | Je n'ai pas entendu ce qu'elle a dit. | Ce que = what.
___ she said made me laugh. | What | That / Which | Ce qu'elle a dit m'a fait rire. | Ce que = what.
The girl ___ phone was stolen called the police. | whose | who / who's | La fille dont le téléphone a été volé a appelé la police. | Whose + nom.
The town ___ I grew up is very small. | where | which / when | La ville où j'ai grandi est très petite. | Where = où (lieu).
The town ___ I grew up in is very small. | — | where / when | La ville où j'ai grandi est très petite. | Avec la préposition à la fin, pas de where.
That's the doctor ___ I told you about. | — | about whom / whose | C'est le médecin dont je t'ai parlé. | Pronom omis, préposition à la fin.
The movie, ___ was filmed in Boston, won an award. | which | that / who | Le film, qui a été tourné à Boston, a gagné un prix. | Entre virgules : which (jamais that).
My sister, ___ lives in Chicago, is a nurse. | who | that / which | Ma sœur, qui habite à Chicago, est infirmière. | Entre virgules, une personne : who.
Is this the bus ___ goes to the airport? | that | who / where | Est-ce l'autobus qui va à l'aéroport ? | Une chose, sujet : that (ou which).
I'll never forget the day ___ my son was born. | when | where / which | Je n'oublierai jamais le jour où mon fils est né. | Un moment : when.
He's the only person ___ understands me. | who | which / whose | C'est la seule personne qui me comprend. | Une personne, sujet : who.
Everything ___ he said was true. | that | what / who | Tout ce qu'il a dit était vrai. | Après everything : that (jamais what).
The hotel ___ we stayed at was cheap. | — | where / whose | L'hôtel où nous avons logé était bon marché. | Préposition à la fin, pronom omis.
She married a man ___ she met at work. | — | whose / where | Elle a épousé un homme qu'elle a rencontré au travail. | Pronom complément omis.
Do you know the reason ___ he left? | why | which / where | Connais-tu la raison pour laquelle il est parti ? | La raison pour laquelle = the reason why.
The students ___ passed the exam got a certificate. | who | which / whose | Les élèves qui ont réussi l'examen ont reçu un certificat. | Personnes, sujet : who.
The company ___ he works for is in Seattle. | — | where / whose | L'entreprise pour laquelle il travaille est à Seattle. | Préposition à la fin.
I lost the watch ___ my father gave me. | that | who / whose | J'ai perdu la montre que mon père m'avait donnée. | Une chose, complément : that.
The restaurant, ___ opened last year, is already famous. | which | that / where | Le restaurant, qui a ouvert l'an dernier, est déjà célèbre. | Entre virgules : which.
""",

"deductionEnExercises": """
She's been working all night. She ___ be exhausted. | must | can't / might not | Elle a travaillé toute la nuit. Elle doit être épuisée. | Certitude positive : must.
He ___ be at work. His car isn't here. | can't | must / mustn't | Il ne peut pas être au travail. Sa voiture n'est pas là. | Impossibilité : can't.
Don't wait for me. I ___ be late. | might | must / can't | Ne m'attendez pas. Je serai peut-être en retard. | Possibilité : might.
It ___ rain later, so take an umbrella. | may | must / can't | Il pourrait pleuvoir plus tard, alors prends un parapluie. | Possibilité : may.
The lights are off. They ___ be asleep. | must | can't / should | Les lumières sont éteintes. Ils doivent dormir. | Déduction logique : must.
That ___ be Jane. She's in Florida this week. | can't | must / might | Ça ne peut pas être Jane. Elle est en Floride cette semaine. | Impossibilité : can't.
Someone is knocking. It ___ be the mail carrier. | could | can't / mustn't | On frappe. C'est peut-être le facteur. | Possibilité : could.
She ___ have missed the bus. She's never late. | must | can't / should | Elle a dû rater l'autobus. Elle n'est jamais en retard. | Déduction au passé : must have + participe.
He ___ have stolen the money. He was in the hospital. | can't | must / might | Il ne peut pas avoir volé l'argent. Il était à l'hôpital. | Impossibilité au passé : can't have.
I'm not sure where she is. She ___ have gone home. | might | must / can't | Je ne sais pas où elle est. Elle est peut-être rentrée. | Possibilité au passé : might have.
The ground is wet. It must have ___ last night. | rained | rain / raining | Le sol est mouillé. Il a dû pleuvoir hier soir. | Must have + participe.
You must have ___ very worried. | been | be / being | Tu as dû être très inquiet. | Must have been.
They ___ be brothers. They look exactly alike. | must | can't / mustn't | Ils doivent être frères. Ils se ressemblent comme deux gouttes d'eau. | Certitude : must.
He ___ be hungry. He just ate a huge pizza. | can't | must / mustn't | Il ne peut pas avoir faim. Il vient de manger une énorme pizza. | Impossibilité : can't.
I can't find my wallet. I ___ have dropped it on the street. | might | can't / mustn't | Je ne trouve pas mon portefeuille. Je l'ai peut-être fait tomber dans la rue. | Might have + participe.
She speaks perfect French. She ___ have lived in France. | must | can't / shouldn't | Elle parle parfaitement français. Elle a dû vivre en France. | Must have.
That restaurant ___ be expensive. Look at all the fancy cars. | must | can't / mustn't | Ce restaurant doit être cher. Regarde toutes ces voitures de luxe. | Déduction : must.
The test ___ be that hard. Everyone passed. | can't | must / mustn't | L'examen ne peut pas être si difficile. Tout le monde a réussi. | Impossibilité : can't.
Where's Tom? — I don't know. He ___ be in the garage. | may | must / can't | Où est Tom ? — Je ne sais pas. Il est peut-être dans le garage. | Possibilité : may.
You ___ have seen him. He left yesterday. | can't | must / mustn't | Tu ne peux pas l'avoir vu. Il est parti hier. | Can't have + participe.
The baby is crying. She ___ be hungry. | might | can't / mustn't | Le bébé pleure. Elle a peut-être faim. | Possibilité : might.
He didn't answer. He ___ not have heard the phone. | may | should / can | Il n'a pas répondu. Il n'a peut-être pas entendu le téléphone. | May not have + participe.
Look at her tan! She must have ___ on vacation. | been | gone / be | Regarde son bronzage ! Elle a dû être en vacances. | Must have been.
They ___ have arrived yet. The plane lands at nine. | can't | mustn't / must | Ils ne peuvent pas déjà être arrivés. L'avion atterrit à neuf heures. | Can't have + participe.
It ___ be true, but I doubt it. | could | must / can't | C'est possible, mais j'en doute. | Possibilité faible : could.
You ___ be Anna! I've heard so much about you. | must | can / might not | Tu dois être Anna ! On m'a tellement parlé de toi. | Certitude : must.
He's wearing a uniform. He ___ be a police officer. | must | can't / mustn't | Il porte un uniforme. Il doit être policier. | Déduction : must.
She ___ be at the gym. She goes every Tuesday. | might | can't / mustn't | Elle est peut-être au gym. Elle y va tous les mardis. | Possibilité : might.
That ___ be the right address. There's no house here. | can't | must / mustn't | Ça ne peut pas être la bonne adresse. Il n'y a pas de maison ici. | Impossibilité : can't.
They ___ have gone out. Their car is gone. | must | can't / shouldn't | Ils ont dû sortir. Leur voiture n'est plus là. | Must have + participe.
I ___ have left the oven on. Let me check. | might | must / can't | J'ai peut-être laissé le four allumé. Je vais vérifier. | Might have + participe.
""",

"beUsedToEnExercises": """
I'm used to ___ in a big city. | living | live / lived | J'ai l'habitude de vivre dans une grande ville. | Be used to + -ing.
She isn't used ___ such cold weather. | to | with / at | Elle n'a pas l'habitude d'un temps aussi froid. | Be used to + nom.
He'll get used to ___ on the left in London. | driving | drive / drove | Il s'habituera à conduire à gauche à Londres. | Get used to + -ing.
We ___ used to the noise after a while. | got | get to / were | Nous nous sommes habitués au bruit au bout d'un moment. | Get used to au passé : got used to.
I ___ to play hockey when I was a kid. | used | was used / am used | Je jouais au hockey quand j'étais petit. | Habitude passée : used to + verbe nu.
I'm ___ to working nights now. | used | use / using | J'ai maintenant l'habitude de travailler de nuit. | Be used to.
Are you used ___ the food here yet? | to | at / for | Es-tu habitué à la nourriture d'ici ? | Be used to + nom.
It took me months to get used to ___ English every day. | speaking | speak / spoke | Il m'a fallu des mois pour m'habituer à parler anglais tous les jours. | Get used to + -ing.
She ___ used to wearing glasses yet. | isn't | doesn't / didn't use | Elle n'a pas encore l'habitude de porter des lunettes. | Be used to : isn't used to.
You'll ___ used to it. Don't worry. | get | be getting to / used | Tu t'y habitueras. Ne t'inquiète pas. | Get used to.
My dad ___ used to his new phone. | is getting | gets to / is get | Mon père s'habitue à son nouveau téléphone. | Is getting used to : en train de s'habituer.
I'm not used to ___ so early. | getting up | get up / got up | Je n'ai pas l'habitude de me lever si tôt. | Be used to + -ing.
We used to ___ in Maine, but we moved. | live | living / lived | Nous habitions dans le Maine, mais nous avons déménagé. | Used to + verbe nu.
Did you use to ___ the bus to work? | take | taking / took | Prenais-tu l'autobus pour aller au travail ? | Did you use to + verbe nu.
I've ___ used to the time difference. | gotten | got to / been get | Je me suis habitué au décalage horaire. | Present perfect : have gotten used to (américain).
He's used to ___ alone. He doesn't mind. | eating | eat / ate | Il a l'habitude de manger seul. Ça ne le dérange pas. | Be used to + -ing.
They aren't used to ___ in such a small apartment. | living | live / lived | Ils n'ont pas l'habitude de vivre dans un si petit appartement. | Be used to + -ing.
I'll never get used to ___ up at 5 a.m. | waking | wake / woke | Je ne m'habituerai jamais à me réveiller à 5 h. | Get used to + -ing.
She ___ to smoke, but she quit years ago. | used | was used / is used | Elle fumait, mais elle a arrêté il y a des années. | Used to + verbe nu.
Is he used to ___ a uniform? | wearing | wear / wore | A-t-il l'habitude de porter un uniforme ? | Be used to + -ing.
New students soon get used ___ the rules. | to | with / at | Les nouveaux élèves s'habituent vite aux règles. | Get used to + nom.
At first it was hard, but now I'm used ___ it. | to | with / at | Au début, c'était difficile, mais maintenant j'y suis habitué. | Be used to + it.
I used ___ eat meat, but I'm vegetarian now. | to | for / at | Je mangeais de la viande, mais maintenant je suis végétarien. | Habitude passée : used to + verbe nu.
Cats get used ___ new homes slowly. | to | for / with | Les chats s'habituent lentement à une nouvelle maison. | Get used to + nom.
""",

"phrasalVerbs1EnExercises": """
I need to ___ up early tomorrow. | get | take / put | Je dois me lever tôt demain. | Get up = se lever.
Can you ___ off the TV? Nobody's watching. | turn | put / take | Tu peux éteindre la télé ? Personne ne regarde. | Turn off = éteindre.
___ on your coat. It's freezing. | Put | Take / Turn | Mets ton manteau. Il gèle. | Put on = mettre (un vêtement).
Please ___ off your shoes at the door. | take | put / turn | Enlève tes chaussures à la porte, s'il te plaît. | Take off = enlever.
I'm looking ___ my glasses. Have you seen them? | for | after / up | Je cherche mes lunettes. Tu les as vues ? | Look for = chercher.
If you don't know a word, look it ___. | up | for / after | Si tu ne connais pas un mot, cherche-le (dans le dictionnaire). | Look up = chercher une information.
She takes ___ her mother. They have the same smile. | after | over / up | Elle tient de sa mère. Elles ont le même sourire. | Take after = ressembler à (un parent).
Our flight took ___ an hour late. | off | up / out | Notre vol a décollé avec une heure de retard. | Take off = décoller.
I'm going to ___ up yoga this year. | take | get / put | Je vais me mettre au yoga cette année. | Take up = commencer (une activité).
Let's ___ out for dinner tonight. | go | get / take | Sortons souper ce soir. | Go out = sortir.
The alarm went ___ at six. | off | out / up | Le réveil a sonné à six heures. | Go off = sonner.
We ran ___ of gas on the highway. | out | off / away | Nous sommes tombés en panne d'essence sur l'autoroute. | Run out of = manquer de.
I ran ___ an old friend at the supermarket. | into | out / over | Je suis tombé sur un vieil ami au supermarché. | Run into = croiser par hasard.
They broke ___ after five years together. | up | down / out | Ils ont rompu après cinq ans ensemble. | Break up = rompre.
My car broke ___ on the way to work. | down | up / out | Ma voiture est tombée en panne en allant au travail. | Break down = tomber en panne.
The meeting was called ___ because of the storm. | off | out / up | La réunion a été annulée à cause de la tempête. | Call off = annuler.
Can you ___ me up at the airport? | pick | take / get | Peux-tu venir me chercher à l'aéroport ? | Pick up = aller chercher.
I can't put ___ with this noise anymore! | up | on / off | Je ne supporte plus ce bruit ! | Put up with = supporter.
She came ___ with a great idea. | up | out / over | Elle a eu une super idée. | Come up with = trouver (une idée).
Hold ___, I'll be right back. | on | up / off | Attends une seconde, je reviens tout de suite. | Hold on = patienter.
Don't give ___! You can do it. | up | in / out | N'abandonne pas ! Tu peux y arriver. | Give up = abandonner.
I'll ___ back to you tomorrow with an answer. | get | give / come | Je te reviens demain avec une réponse. | Get back to someone = recontacter.
How are you getting ___ at your new school? | on | over / up | Comment ça se passe dans ta nouvelle école ? | Get on = se débrouiller (aussi « get along »).
It took him weeks to get ___ the flu. | over | through / off | Il lui a fallu des semaines pour se remettre de la grippe. | Get over = se remettre de.
Could you fill ___ this form, please? | in | up / on | Pourriez-vous remplir ce formulaire, s'il vous plaît ? | Fill in / fill out = remplir.
I need to work ___ more. I'm out of shape. | out | up / off | Je dois faire plus de sport. Je ne suis pas en forme. | Work out = s'entraîner.
Let's set ___ early to avoid the traffic. | off | up / on | Partons tôt pour éviter la circulation. | Set off = se mettre en route.
The kids grew ___ in Vermont. | up | out / on | Les enfants ont grandi au Vermont. | Grow up = grandir.
""",

"gerondifInfinitifEnExercises": """
I stopped ___ meat ten years ago. | eating | to eat / eat | J'ai arrêté de manger de la viande il y a dix ans. | Stop + -ing = arrêter de.
On the way home, we stopped ___ gas. | to buy | buying / buy | En rentrant, nous nous sommes arrêtés pour prendre de l'essence. | Stop + to = s'arrêter pour.
Remember ___ your passport! | to take | taking / take | N'oublie pas de prendre ton passeport ! | Remember + to = penser à (avant).
I remember ___ my grandparents' farm as a child. | visiting | to visit / visit | Je me souviens d'avoir visité la ferme de mes grands-parents quand j'étais enfant. | Remember + -ing = se souvenir (d'un passé).
I'll never forget ___ the ocean for the first time. | seeing | to see / see | Je n'oublierai jamais la première fois que j'ai vu l'océan. | Forget + -ing = un souvenir.
Don't forget ___ the door. | to lock | locking / lock | N'oublie pas de verrouiller la porte. | Forget + to = oublier de faire.
I tried ___ him, but his phone was off. | to call | calling / call | J'ai essayé de l'appeler, mais son téléphone était éteint. | Try + to = faire un effort pour.
If you can't sleep, try ___ a hot bath. | taking | to take / take | Si tu n'arrives pas à dormir, essaie de prendre un bain chaud. | Try + -ing = essayer (pour voir si ça marche).
I regret ___ him that. It was mean. | telling | to tell / tell | Je regrette de lui avoir dit ça. C'était méchant. | Regret + -ing = regretter un acte passé.
We regret ___ you that your flight is canceled. | to inform | informing / inform | Nous avons le regret de vous informer que votre vol est annulé. | Regret + to = avoir le regret de (annonce).
She went on ___ after the break. | talking | to talk / talk | Elle a continué à parler après la pause. | Go on + -ing = continuer.
After the history lesson, he went on ___ about science. | to talk | talking / talk | Après la leçon d'histoire, il est passé à la science. | Go on + to = passer à autre chose.
I need ___ my hair cut. | to get | getting / get | Je dois me faire couper les cheveux. | Need + to.
The car needs ___. It's so dirty. | washing | to wash / wash | La voiture a besoin d'être lavée. Elle est très sale. | Need + -ing = a besoin d'être (sens passif).
I like ___ early on weekdays. | getting up | get up / got up | J'aime me lever tôt en semaine. | Like + -ing (ou to).
I'd like ___ you something. | to ask | asking / ask | J'aimerais te demander quelque chose. | Would like + to.
She began ___ the piano at five. | to play | play / played | Elle a commencé le piano à cinq ans. | Begin + to (ou -ing).
Did you remember ___ the cat? | to feed | feeding / feed | As-tu pensé à nourrir le chat ? | Remember + to.
I remember ___ the cat, but I don't remember when. | feeding | to feed / feed | Je me souviens d'avoir nourri le chat, mais pas à quelle heure. | Remember + -ing.
He stopped ___ when he saw the police. | running | to run / run | Il a arrêté de courir quand il a vu la police. | Stop + -ing.
She stopped ___ hello to her neighbor. | to say | saying / say | Elle s'est arrêtée pour dire bonjour à sa voisine. | Stop + to.
Try ___ the window. Maybe it's less hot. | opening | to opening / open to | Essaie d'ouvrir la fenêtre. Il fera peut-être moins chaud. | Try + -ing = une solution à tester.
I'm trying ___ more water. | to drink | drinking / drink | J'essaie de boire plus d'eau. | Try + to = faire l'effort.
I prefer ___ to walking. | cycling | to cycle / cycle | Je préfère le vélo à la marche. | Prefer + -ing … to + -ing.
""",
}
