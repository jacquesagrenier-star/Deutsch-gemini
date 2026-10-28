# -*- coding: utf-8 -*-
"""Les series A2 allongees (28 oct. 2026) : des questions a la suite des
douze de chaque fiche (grammaire_a2.py), pour approcher le volume des series
allemandes. Meme format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

SUPPLEMENTS = {
"presentPerfectEnExercises": """
We ___ lived in this neighborhood for years. | have | has / are | Nous habitons ce quartier depuis des années. | We + have + participe.
My sister ___ never seen the ocean. | has | have / is | Ma sœur n'a jamais vu l'océan. | She + has.
Have you ___ been to Canada? | ever | never / yet | Es-tu déjà allé au Canada ? | Question d'expérience : ever.
I've ___ met him. Who is he? | never | ever / yet | Je ne l'ai jamais rencontré. Qui est-ce ? | Never, à l'affirmative = jamais.
She has ___ her homework. Can she go out? | finished | finish / finishing | Elle a fini ses devoirs. Peut-elle sortir ? | Has + participe passé.
They have ___ to Mexico twice. | been | gone / be | Ils sont allés deux fois au Mexique. | Been = aller et revenir.
Where's Paul? — He's ___ to the store. | gone | been / go | Où est Paul ? — Il est parti au magasin. | Gone = il y est encore.
I've ___ a terrible mistake. | made | make / did | J'ai fait une terrible erreur. | Make → made.
Have you ___ my phone? I can't find it. | seen | saw / see | As-tu vu mon téléphone ? Je ne le trouve pas. | See → seen.
We have ___ our new neighbors. | met | meet / meeted | Nous avons rencontré nos nouveaux voisins. | Meet → met.
He's ___ his wallet at home. | left | leaved / leave | Il a oublié son portefeuille à la maison. | Leave → left.
I've ___ that book. It's great! | read | readed / reading | J'ai lu ce livre. Il est super ! | Read → read (prononcé « red »).
She ___ called yet. | hasn't | haven't / didn't | Elle n'a pas encore appelé. | She + hasn't.
We ___ eaten breakfast yet. | haven't | hasn't / didn't | Nous n'avons pas encore déjeuné. | We + haven't.
___ he finished the report? | Has | Have / Did | A-t-il fini le rapport ? | Question : Has + he.
___ they arrived yet? | Have | Has / Did | Sont-ils déjà arrivés ? | Question : Have + they.
I ___ to the dentist last week. | went | have gone / have been | Je suis allé chez le dentiste la semaine dernière. | Last week : past simple.
She ___ in Paris in 2020. | was | has been / is | Elle était à Paris en 2020. | Une date : past simple.
I've lost my glasses. ___ you seen them? | Have | Did / Are | J'ai perdu mes lunettes. Les as-tu vues ? | Have you seen…?
The movie has ___ started. Hurry up! | already | yet / ever | Le film a déjà commencé. Dépêche-toi ! | Already, à l'affirmative.
Have you done your homework ___? | yet | already / just yet | As-tu déjà fait tes devoirs ? | Yet, en fin de question.
I've ___ eaten. I'm not hungry. | just | yet / ever | Je viens de manger. Je n'ai pas faim. | Just = venir de.
It's the best movie I've ___ seen. | ever | never / yet | C'est le meilleur film que j'aie jamais vu. | Superlatif + ever.
How long ___ she lived here? | has | have / did | Depuis combien de temps habite-t-elle ici ? | How long + has she.
He has ___ three emails this morning. | written | wrote / write | Il a écrit trois courriels ce matin. | Write → written.
We've ___ a new car. | bought | buyed / buy | Nous avons acheté une nouvelle voiture. | Buy → bought.
You've ___ a lot! You look different. | changed | change / changing | Tu as beaucoup changé ! Tu as l'air différent. | Résultat visible : present perfect.
The kids have ___ the cookies. There are none left. | eaten | ate / eat | Les enfants ont mangé les biscuits. Il n'en reste plus. | Eat → eaten.
I ___ him yesterday at the gym. | saw | have seen / see | Je l'ai vu hier au gym. | Yesterday : past simple.
She's ___ her leg. She can't walk. | broken | broke / break | Elle s'est cassé la jambe. Elle ne peut pas marcher. | Break → broken.
""",

"forSinceEnExercises": """
I've known Sarah ___ ten years. | for | since / ago | Je connais Sarah depuis dix ans. | Une durée : for.
I've known Sarah ___ 2015. | since | for / ago | Je connais Sarah depuis 2015. | Un point de départ : since.
I met Sarah ten years ___. | ago | since / for | J'ai rencontré Sarah il y a dix ans. | Il y a = ago.
We've been here ___ three o'clock. | since | for / ago | Nous sommes ici depuis trois heures (de l'après-midi). | Une heure précise : since.
We've been here ___ three hours. | for | since / ago | Nous sommes ici depuis trois heures (de temps). | Une durée : for.
He left an hour ___. | ago | since / for | Il est parti il y a une heure. | Ago, après la durée.
She's lived in Texas ___ she was a child. | since | for / ago | Elle vit au Texas depuis son enfance. | Since + proposition.
They've been friends ___ ages. | for | since / ago | Ils sont amis depuis une éternité. | For ages = depuis longtemps.
I haven't eaten ___ breakfast. | since | for / ago | Je n'ai rien mangé depuis le déjeuner. | Since + moment.
I haven't eaten ___ six hours. | for | since / ago | Je n'ai rien mangé depuis six heures. | For + durée.
The store opened two weeks ___. | ago | since / for | Le magasin a ouvert il y a deux semaines. | Ago + past simple.
How ___ have you had this dog? | long | much / many | Depuis combien de temps as-tu ce chien ? | How long… ?
I ___ my job in 2018. | started | have started / start | J'ai commencé mon emploi en 2018. | Une date : past simple.
I ___ at this job since 2018. | have worked | worked / work | Je travaille à cet emploi depuis 2018. | Since : present perfect.
She ___ here for two years. Now she lives in Seattle. | lived | has lived / lives | Elle a habité ici deux ans. Maintenant, elle vit à Seattle. | Période finie : past simple.
We ___ each other since college. | have known | know / knew | Nous nous connaissons depuis l'université. | Since + present perfect (know).
It's been raining ___ this morning. | since | for / ago | Il pleut depuis ce matin. | Since + moment.
I've had this cold ___ a week. | for | since / ago | J'ai ce rhume depuis une semaine. | For + durée.
When did you arrive? — Two days ___. | ago | since / for | Quand es-tu arrivé ? — Il y a deux jours. | Ago.
He hasn't called me ___ his birthday. | since | for / ago | Il ne m'a pas appelé depuis son anniversaire. | Since + moment.
They've been married ___ 1990. | since | for / ago | Ils sont mariés depuis 1990. | Since + année.
They got married thirty years ___. | ago | since / for | Ils se sont mariés il y a trente ans. | Ago + past simple.
I've lived here ___ most of my life. | for | since / ago | J'ai vécu ici la plus grande partie de ma vie. | For + durée.
How long ___ you been waiting? | have | did / are | Depuis combien de temps attends-tu ? | How long have you been…?
She's been a teacher ___ twenty years. | for | since / ago | Elle est enseignante depuis vingt ans. | For + durée.
I haven't seen that movie ___ I was a kid. | since | for / ago | Je n'ai pas vu ce film depuis que je suis petit. | Since + proposition.
We moved to Boston a long time ___. | ago | since / for | Nous avons emménagé à Boston il y a longtemps. | Ago.
He's been sick ___ Monday. | since | for / ago | Il est malade depuis lundi. | Since + jour.
""",

"pastContinuousEnExercises": """
I ___ dinner when the doorbell rang. | was cooking | cooked / am cooking | Je préparais le souper quand on a sonné à la porte. | L'action en cours : was + -ing.
She ___ a book when I came in. | was reading | read / is reading | Elle lisait un livre quand je suis entré. | Was + -ing.
We ___ TV when the power went out. | were watching | watched / was watching | Nous regardions la télé quand le courant a été coupé. | We + were + -ing.
They were ___ on the beach when it started to rain. | walking | walk / walked | Ils marchaient sur la plage quand il a commencé à pleuvoir. | Were + -ing.
He ___ his arm while he was playing football. | broke | was breaking / breaks | Il s'est cassé le bras en jouant au football. | L'événement bref : past simple.
I was sleeping when the phone ___. | rang | was ringing / rings | Je dormais quand le téléphone a sonné. | L'interruption : past simple.
___ you working when I called? | Were | Was / Did | Travaillais-tu quand j'ai appelé ? | Question : Were + you + -ing.
___ she sleeping when you got home? | Was | Were / Did | Dormait-elle quand tu es rentré ? | Question : Was + she + -ing.
I ___ listening, sorry. What did you say? | wasn't | weren't / didn't | Je n'écoutais pas, désolé. Qu'as-tu dit ? | I + wasn't + -ing.
They ___ wearing coats, and they were cold. | weren't | wasn't / didn't | Ils ne portaient pas de manteaux, et ils avaient froid. | They + weren't + -ing.
While she ___, I cleaned the kitchen. | was studying | studied / studies | Pendant qu'elle étudiait, j'ai nettoyé la cuisine. | While + was + -ing.
The birds were ___ and the sun was shining. | singing | sang / sing | Les oiseaux chantaient et le soleil brillait. | Décrire une scène : were + -ing.
What were you ___ at nine last night? | doing | do / did | Que faisais-tu hier soir à neuf heures ? | Were + -ing.
I saw Anna while I ___ for the bus. | was waiting | waited / am waiting | J'ai vu Anna pendant que j'attendais l'autobus. | While + -ing.
He ___ too fast when the police stopped him. | was driving | drove / is driving | Il roulait trop vite quand la police l'a arrêté. | L'action en cours : was + -ing.
At midnight, we ___ still talking. | were | was / did | À minuit, nous parlions encore. | We + were.
She cut her finger while she ___ bread. | was cutting | cut / is cutting | Elle s'est coupé le doigt en coupant du pain. | While + was + -ing.
It ___ snowing when we woke up. | was | were / did | Il neigeait quand nous nous sommes réveillés. | It + was + -ing.
The baby ___ when we arrived. | was crying | cried / cries | Le bébé pleurait quand nous sommes arrivés. | Was + -ing.
It started to snow ___ the night. | during | while / when | Il a commencé à neiger pendant la nuit. | During + nom.
I fell asleep ___ I was watching the movie. | while | during / for | Je me suis endormi pendant que je regardais le film. | While + sujet + verbe.
When I arrived, they ___ dinner. | were having | had / have | Quand je suis arrivé, ils étaient en train de souper. | Were + -ing.
When I arrived, they ___ me a drink. | offered | were offering / offer | Quand je suis arrivé, ils m'ont offert un verre. | Une action brève : past simple.
My phone ___ while I was running. | fell | was falling / falls | Mon téléphone est tombé pendant que je courais. | L'événement : past simple.
Who ___ you talking to on the phone? | were | was / did | À qui parlais-tu au téléphone ? | Were + -ing.
Everyone ___ laughing at his joke. | was | were / did | Tout le monde riait de sa blague. | Everyone = singulier : was.
""",

"futursEnExercises": """
I'm thirsty. — I ___ get you some water. | 'll | 'm going to / get | J'ai soif. — Je vais te chercher de l'eau. | Décision sur le moment : will.
We've booked the tickets. We ___ to see the show on Friday. | 're going | will / go | Nous avons réservé les billets. Nous allons voir le spectacle vendredi. | Projet décidé : going to.
She ___ her parents tomorrow — she's already bought the train ticket. | is visiting | visits / will visiting | Elle rend visite à ses parents demain ; elle a déjà acheté son billet de train. | Rendez-vous fixé : present continuous.
Watch out! You're ___ to drop the glass! | going | will / go | Attention ! Tu vas faire tomber le verre ! | Ce qu'on voit venir : going to.
I think it ___ snow tonight. | will | is going / snows | Je pense qu'il va neiger ce soir. | I think + will.
I ___ help you with your homework, I promise. | 'll | 'm helping / help | Je t'aiderai avec tes devoirs, promis. | Promesse : will.
What time does the train ___? | leave | leaves / leaving | À quelle heure part le train ? | Horaire : present simple (does + verbe nu).
The concert ___ at eight tonight. | starts | will starting / is start | Le concert commence à huit heures ce soir. | Horaire : present simple.
Are you ___ anything this weekend? | doing | do / going do | Fais-tu quelque chose ce week-end ? | Projets : present continuous.
I'm not sure. Maybe I ___ stay home. | 'll | 'm going / stay to | Je ne sais pas. Peut-être que je resterai à la maison. | Maybe + will.
He ___ be twenty next month. | will | is going / is being | Il aura vingt ans le mois prochain. | Un fait futur : will.
We ___ going to move. We like it here. | aren't | won't / don't | Nous n'allons pas déménager. Nous nous plaisons ici. | Aren't going to.
I ___ be late tonight. Don't wait for me. | 'll | 'm going / am | Je serai en retard ce soir. Ne m'attends pas. | Will be.
Will you ___ me a favor? | do | doing / to do | Me rendras-tu un service ? | Will you + verbe nu.
___ you going to call her? | Are | Will / Do | Vas-tu l'appeler ? | Are you going to…?
I'll call you as soon as I ___. | arrive | will arrive / arriving | Je t'appellerai dès que j'arriverai. | As soon as + present simple.
If you ___ hungry, there's pizza in the fridge. | get | will get / got | Si tu as faim, il y a de la pizza dans le frigo. | If + present simple.
I'm sure they ___ like the gift. | will | are going / like to | Je suis sûr qu'ils aimeront le cadeau. | I'm sure + will.
We're ___ a party on Saturday. Can you come? | having | have / will having | Nous faisons une fête samedi. Peux-tu venir ? | Projet arrangé : present continuous.
I ___ tell her. It's a secret. | won't | don't / 'm not | Je ne lui dirai pas. C'est un secret. | Won't = will not.
Who ___ win the game, do you think? | will | is going / wins | Qui va gagner le match, à ton avis ? | Prévision : will.
She's going ___ a doctor one day. | to be | be / will be | Elle va devenir médecin un jour. | Going to + verbe.
The bus ___ in five minutes. | leaves | will leaving / is leave | L'autobus part dans cinq minutes. | Horaire : present simple.
Next summer we ___ to drive across the country. | are going | will / go | L'été prochain, nous allons traverser le pays en voiture. | Intention : going to.
Don't touch that! You'll ___ yourself. | hurt | hurting / to hurt | Ne touche pas à ça ! Tu vas te faire mal. | Will + verbe nu.
""",

"comparatifsEnExercises": """
This box is ___ than that one. | heavier | heavyer / more heavy | Cette boîte est plus lourde que celle-là. | -y → -ier.
My brother is ___ than me. | older | more old / oldest | Mon frère est plus âgé que moi. | Adjectif court : -er.
This is the ___ book I've ever read. | best | better / goodest | C'est le meilleur livre que j'aie jamais lu. | Good → better → the best.
This movie is ___ than the first one. | better | more good / best | Ce film est meilleur que le premier. | Good → better.
Yesterday was ___ than today. | colder | more cold / coldest | Hier, il faisait plus froid qu'aujourd'hui. | Cold → colder.
The weather is getting ___ and ___. | worse … worse | badder … badder / worst … worst | Le temps empire de plus en plus. | Bad → worse ; « de plus en plus » = worse and worse.
Alaska is the ___ state in the US. | largest | larger / most large | L'Alaska est le plus grand État des États-Unis. | Large → the largest.
This is the ___ interesting museum in the city. | most | more / much | C'est le musée le plus intéressant de la ville. | Adjectif long : the most.
She's ___ than her sister. | more patient | patienter / most patient | Elle est plus patiente que sa sœur. | Adjectif long : more.
He runs ___ than me. | faster | more fast / fastest | Il court plus vite que moi. | Fast → faster.
My car is ___ expensive than yours. | less | fewer / least | Ma voiture coûte moins cher que la tienne. | Moins + adjectif = less.
That was the ___ meal I've ever had. | worst | baddest / worse | C'était le pire repas de ma vie. | Bad → worse → the worst.
This exercise is ___ than I thought. | easier | more easy / easyer | Cet exercice est plus facile que je ne le pensais. | Easy → easier.
Boston is ___ from here than New York. | farther | farer / more far | Boston est plus loin d'ici que New York. | Far → farther.
My new apartment is ___ than the old one. | bigger | biger / more big | Mon nouvel appartement est plus grand que l'ancien. | Big → bigger (consonne doublée).
This street is not as busy ___ Main Street. | as | than / like | Cette rue n'est pas aussi animée que Main Street. | Not as … as.
She's as smart ___ her brother. | as | than / that | Elle est aussi intelligente que son frère. | As … as.
Which is ___, a lion or a cat? | more dangerous | dangerouser / the most dangerous | Lequel est le plus dangereux, un lion ou un chat ? | Entre deux : comparatif.
It's the ___ day of my life! | happiest | happyest / most happy | C'est le plus beau jour de ma vie ! | Happy → the happiest.
Today is ___ than yesterday. | hotter | hoter / more hot | Aujourd'hui, il fait plus chaud qu'hier. | Hot → hotter.
That was the ___ test of the year. | hardest | most hard / harder | C'était l'examen le plus difficile de l'année. | Hard → the hardest.
He's the ___ person I know. | funniest | most funny / funnyest | C'est la personne la plus drôle que je connaisse. | Funny → the funniest.
This shirt is ___ than the blue one. | cheaper | more cheap / cheapest | Cette chemise est moins chère que la bleue. | Cheap → cheaper.
Could you speak ___, please? | more slowly | slowlier / most slowly | Pourriez-vous parler plus lentement, s'il vous plaît ? | Adverbe en -ly : more slowly.
The ___ you practice, the better you get. | more | most / much | Plus tu pratiques, plus tu t'améliores. | The more…, the better…
Russia is ___ than Canada. | bigger | more big / biggest | La Russie est plus grande que le Canada. | Comparatif de deux : -er.
""",

"obligationEnExercises": """
You ___ wear a seat belt. It's the law. | must | mustn't / don't have to | Tu dois porter ta ceinture. C'est la loi. | Obligation : must.
You ___ park here. It's a fire lane. | can't | don't have to / needn't | Tu ne peux pas stationner ici. C'est une voie réservée aux pompiers. | Interdiction : can't / mustn't.
We ___ pay. The museum is free on Sundays. | don't have to | mustn't / can't | Nous n'avons pas besoin de payer. Le musée est gratuit le dimanche. | Pas nécessaire : don't have to.
I ___ go to work today. It's a holiday. | don't have to | mustn't / have to | Je n'ai pas besoin d'aller travailler aujourd'hui. C'est un jour férié. | Pas d'obligation : don't have to.
You ___ try the lobster. It's delicious! | should | must not / have | Tu devrais goûter le homard. C'est délicieux ! | Conseil : should.
She ___ to take the bus because her car is broken. | has | have / must | Elle doit prendre l'autobus parce que sa voiture est en panne. | She has to.
I ___ go to the bank yesterday. | had to | must / have to | J'ai dû aller à la banque hier. | Au passé : had to (must n'a pas de passé).
Do I ___ wear a tie? | have to | must to / should to | Est-ce que je dois porter une cravate ? | Question : Do I have to…?
You ___ eat more vegetables. | should | must to / ought | Tu devrais manger plus de légumes. | Conseil : should.
Students ___ use their phones during the exam. | mustn't | don't have to / needn't | Les élèves ne doivent pas utiliser leur téléphone pendant l'examen. | Interdiction : mustn't.
He doesn't ___ work on weekends. | have to | has to / must | Il n'a pas besoin de travailler le week-end. | Doesn't have to + verbe nu.
___ I call you back later? | Should | Must to / Have | Est-ce que je devrais te rappeler plus tard ? | Should I…?
You look sick. You ___ stay home. | should | shouldn't / mustn't | Tu as l'air malade. Tu devrais rester à la maison. | Conseil : should.
You ___ drink so much coffee. | shouldn't | don't have / mustn't to | Tu ne devrais pas boire autant de café. | Conseil négatif : shouldn't.
We ___ leave now, or we'll miss the train. | have to | had to / don't have to | Nous devons partir maintenant, sinon nous allons rater le train. | Obligation : have to.
Did you ___ wait long? | have to | had to / must | As-tu dû attendre longtemps ? | Did you have to + verbe.
Kids ___ go to school until sixteen. | have to | has to / must to | Les enfants doivent aller à l'école jusqu'à seize ans. | They have to.
You ___ be eighteen to vote. | have to | should / don't have to | Il faut avoir dix-huit ans pour voter. | Obligation : have to.
You ___ forget your passport! | mustn't | don't have to / needn't | Tu ne dois pas oublier ton passeport ! | Interdiction, mise en garde : mustn't.
It's a good idea. We ___ ask her. | should | must not / have | C'est une bonne idée. Nous devrions lui demander. | Conseil : should.
I'll ___ work late tomorrow. | have to | must / had to | Je vais devoir travailler tard demain. | Futur : will have to.
She ___ cook tonight. We're ordering pizza. | doesn't have to | mustn't / doesn't must | Elle n'a pas à cuisiner ce soir. Nous commandons de la pizza. | Pas nécessaire : doesn't have to.
What time ___ we have to be there? | do | must / are | À quelle heure devons-nous être là ? | What time do we have to…?
You ___ see that movie. It's amazing! | have to | mustn't / don't have to | Il faut absolument que tu voies ce film. Il est génial ! | Recommandation forte : have to / must.
""",

"quantifieursEnExercises": """
How ___ water do you drink a day? | much | many / lot | Combien d'eau bois-tu par jour ? | Indénombrable : how much.
How ___ cousins do you have? | many | much / lot | Combien de cousins as-tu ? | Dénombrable : how many.
There are ___ apples in the bowl. | some | any / much | Il y a des pommes dans le bol. | Affirmation : some.
Are there ___ eggs in the fridge? | any | some / much | Y a-t-il des œufs dans le frigo ? | Question : any.
I don't have ___ cash on me. | any | some / many | Je n'ai pas d'argent liquide sur moi. | Négation : any.
Can I have ___ water, please? | some | any / many | Je peux avoir de l'eau, s'il vous plaît ? | Demande polie : some.
She has ___ friends. She's never alone. | a lot of | much / a little | Elle a beaucoup d'amis. Elle n'est jamais seule. | A lot of : dénombrable ou non.
We don't have ___ time. Let's hurry. | much | many / few | Nous n'avons pas beaucoup de temps. Dépêchons-nous. | Indénombrable, négation : much.
There aren't ___ people here tonight. | many | much / a little | Il n'y a pas beaucoup de monde ce soir. | Dénombrable, négation : many.
I speak ___ French — just a few words. | a little | a few / many | Je parle un peu français, juste quelques mots. | Indénombrable : a little.
I know ___ words in Japanese. | a few | a little / much | Je connais quelques mots de japonais. | Dénombrable : a few.
There's ___ left in the bottle — just a drop. | very little | very few / many | Il en reste très peu dans la bouteille, juste une goutte. | Indénombrable : little.
___ people came to the meeting, so we canceled it. | Few | Little / Much | Peu de gens sont venus à la réunion, alors nous l'avons annulée. | Dénombrable : few (= pas assez).
Is there ___ sugar? | any | some of / many | Y a-t-il du sucre ? | Question : any.
I've got ___ homework tonight. | a lot of | many / a few | J'ai beaucoup de devoirs ce soir. | Homework est indénombrable : a lot of.
How ___ luggage do you have? | much | many / lots | Combien de bagages as-tu ? | Luggage est indénombrable : how much.
She gave me some good ___. | advice | advices / an advice | Elle m'a donné de bons conseils. | Advice est indénombrable.
There isn't ___ room in the car. | enough | many / few | Il n'y a pas assez de place dans la voiture. | Assez = enough.
We have ___ chairs for everyone. | enough | much / a little | Nous avons assez de chaises pour tout le monde. | Enough + nom.
Would you like ___ more cake? | some | any / many | Voulez-vous encore du gâteau ? | Offre : some.
I didn't buy ___ bread. | any | some / many | Je n'ai pas acheté de pain. | Négation : any.
___ of my friends live in New York. | Some | Any / Much | Certains de mes amis habitent à New York. | Certains = some of.
There's too ___ traffic today. | much | many / few | Il y a trop de circulation aujourd'hui. | Indénombrable : too much.
There are too ___ cars on this road. | many | much / little | Il y a trop de voitures sur cette route. | Dénombrable : too many.
""",

"ingOuToEnExercises": """
I love ___ by the ocean. | walking | to walking / walk on | J'adore marcher au bord de l'océan. | Love + -ing (ou to).
She promised ___ me. | to call | calling / call | Elle a promis de m'appeler. | Promise + to.
He stopped ___ last year. | smoking | to smoke / smoke | Il a arrêté de fumer l'an dernier. | Stop + -ing = arrêter de.
I'm thinking about ___ to Chicago. | moving | to move / move | Je pense à déménager à Chicago. | Après une préposition : -ing.
We need ___ some milk. | to buy | buying / buy to | Nous devons acheter du lait. | Need + to.
Would you like ___ with us? | to come | coming / come | Voudrais-tu venir avec nous ? | Would like + to.
They plan ___ a house next year. | to buy | buying / buy | Ils ont l'intention d'acheter une maison l'an prochain. | Plan + to.
I can't stand ___ in line. | waiting | to waiting / wait in | Je ne supporte pas de faire la queue. | Can't stand + -ing.
She's good at ___. | drawing | to draw / draw | Elle est douée pour le dessin. | Good at + -ing.
I'm looking forward to ___ you. | seeing | see / saw | J'ai hâte de te voir. | Look forward to + -ing.
He agreed ___ us. | to help | helping / help | Il a accepté de nous aider. | Agree + to.
Do you feel like ___ out tonight? | going | to go / go | As-tu envie de sortir ce soir ? | Feel like + -ing.
I learned ___ when I was six. | to swim | swimming / swim | J'ai appris à nager à six ans. | Learn + to.
He suggested ___ at a café downtown. | meeting | to meet / meet | Il a proposé qu'on se retrouve dans un café du centre-ville. | Suggest + -ing.
I'm tired of ___ the same thing every day. | eating | to eat / eat | J'en ai assez de manger la même chose tous les jours. | Tired of + -ing.
They refused ___ the bill. | to pay | paying / pay | Ils ont refusé de payer l'addition. | Refuse + to.
___ is good for your health. | Swimming | Swim / To swimming | La natation est bonne pour la santé. | Sujet de la phrase : -ing.
I went to the store ___ some bread. | to buy | for buy / buying | Je suis allé au magasin pour acheter du pain. | But : to + verbe.
She keeps ___ me the same question. | asking | to ask / ask | Elle n'arrête pas de me poser la même question. | Keep + -ing.
We hope ___ you again soon. | to see | seeing / see | Nous espérons te revoir bientôt. | Hope + to.
I don't mind ___ the dishes. | doing | to do / do | Ça ne me dérange pas de faire la vaisselle. | Mind + -ing.
He seems ___ tired today. | to be | being / be | Il a l'air fatigué aujourd'hui. | Seem + to.
I prefer ___ at home on Sundays. | staying | stay at / stayed | Je préfère rester à la maison le dimanche. | Prefer + -ing (ou to).
Before ___ the house, check the windows. | leaving | to leave / leave | Avant de quitter la maison, vérifie les fenêtres. | Après before : -ing.
She practices ___ the piano every day. | playing | to play / play | Elle s'exerce au piano tous les jours. | Practice + -ing.
It's easy ___ lost in this city. | to get | getting / get | C'est facile de se perdre dans cette ville. | It's easy + to.
""",

"usedToEnExercises": """
I ___ to have a cat when I was little. | used | use / using | J'avais un chat quand j'étais petit. | Habitude passée : used to.
We used to ___ in a small town. | live | living / lived | Nous habitions dans une petite ville. | Used to + verbe nu.
He ___ to smoke, but he quit. | used | uses / was used | Il fumait, mais il a arrêté. | Used to : c'est fini.
Did you use to ___ a bike to school? | ride | rode / riding | Allais-tu à l'école à vélo ? | Did you use to + verbe nu.
She didn't ___ to like coffee. | use | used / using | Elle n'aimait pas le café (avant). | Négation : didn't use to.
There used to ___ a movie theater on this street. | be | been / being | Il y avait un cinéma dans cette rue. | There used to be.
My grandmother used to ___ bread every Sunday. | bake | baking / baked | Ma grand-mère faisait du pain tous les dimanches. | Used to + verbe nu.
I ___ eat meat, but now I'm vegetarian. | used to | use to / am used to | Je mangeais de la viande, mais maintenant je suis végétarien. | Habitude finie : used to.
___ you use to play sports in high school? | Did | Do / Were | Faisais-tu du sport au lycée ? | Question : Did + you + use to.
We ___ go camping every summer. | used to | use to / were used | Nous allions camper tous les étés. | Used to.
I ___ go to the gym on Mondays. It's my routine. | usually | used to / use to | Je vais d'habitude au gym le lundi. C'est ma routine. | Habitude présente : usually.
He didn't use to ___ glasses. | wear | wearing / wore | Il ne portait pas de lunettes (avant). | Didn't use to + verbe nu.
This used to ___ a quiet neighborhood. | be | was / been | C'était un quartier tranquille. | Used to be.
They used to ___ each other, but now they're friends. | hate | hating / hated | Ils se détestaient, mais maintenant ils sont amis. | Used to + verbe nu.
I used to ___ a lot of video games. | play | playing / played | Je jouais beaucoup aux jeux vidéo. | Used to + verbe nu.
She used to have long hair, but now it's ___. | short | shortly / shorten | Elle avait les cheveux longs, mais maintenant ils sont courts. | Le contraste avec maintenant.
Where did you use to ___? | live | lived / living | Où habitais-tu (avant) ? | Did + use to + verbe nu.
I never ___ to be afraid of dogs. | used | use / using | Je n'ai jamais eu peur des chiens, avant. | Never used to.
We used to ___ letters. Now we send emails. | write | writing / wrote | Nous écrivions des lettres. Maintenant, nous envoyons des courriels. | Used to + verbe nu.
My dad used to ___ me to school. | drive | driving / drove | Mon père m'emmenait à l'école en voiture. | Used to + verbe nu.
There ___ to be many trees here. | used | use / were used | Il y avait beaucoup d'arbres ici. | There used to be.
He used to work at a bank, but he doesn't ___. | anymore | already / yet | Il travaillait dans une banque, mais plus maintenant. | Not … anymore = ne … plus.
I used to be afraid of the dark when I was a ___. | kid | kidding / kids | J'avais peur du noir quand j'étais petit. | Une habitude ou un état d'enfance.
""",
}
