# -*- coding: utf-8 -*-
"""Les fiches de grammaire A2 de l'anglais, en francais, et leurs series.

SOURCE : on corrige ici, puis python anglais/outils/construire.py (niveaux.py)
les ajoute a anglais/datos/grammaire.json et exercices.json, apres l'A1.
Meme format que grammaire_a1.py. Les phrases evitent les mots qui different
entre l'americain et le britannique (les fiches sont communes aux deux).

Une question : « phrase avec ___ | bonne reponse | mauvaise 1 / mauvaise 2 |
traduction | explication ».
"""

FICHES = [
{
"id": "present-perfect", "titre": "Le present perfect", "resume": "I have seen, I've never been — le passé qui touche le présent",
"regle": "Le <b>present perfect</b> se forme avec <b>have / has + participe passé</b> : <b>I have seen</b>, <b>she has finished</b>. Il relie le passé au présent : une expérience de vie (<b>I've been to Boston</b>), un résultat visible maintenant (<b>I've lost my keys</b>), une action pas encore finie (<b>I've lived here for ten years</b>). On ne dit <b>pas quand</b> : dès qu'un moment passé précis apparaît (<b>yesterday</b>, <b>in 2020</b>, <b>last week</b>), on passe au prétérit. Ses mots fidèles : <b>ever</b> (déjà, dans une question), <b>never</b>, <b>already</b>, <b>yet</b>, <b>just</b>.",
"tableau": [
 ["I / you / we / they have + participe", "j'ai…, tu as…", "I've finished. They have left."],
 ["he / she / it has + participe", "il / elle a…", "She's visited Canada twice."],
 ["haven't · hasn't", "négation", "I haven't seen him. It hasn't rained."],
 ["Have you…? · Has she…?", "question", "Have you ever eaten lobster?"],
 ["already · just", "déjà · venir de", "I've already paid. He's just arrived."],
 ["yet", "déjà ? (question) · pas encore (négation)", "Have you finished yet? Not yet."],
],
"exemples": [
 ["I've never been to New York.", "Je ne suis jamais allé à New York."],
 ["She has just called.", "Elle vient d'appeler."],
 ["Have you seen my glasses?", "Tu as vu mes lunettes ?"],
],
"attention": "Le passé composé français se traduit souvent par le <b>prétérit</b>, pas par le present perfect : « J'ai vu Tom hier » = <b>I saw Tom yesterday</b>, jamais <i>I have seen it yesterday</i>. Et l'américain parlé emploie volontiers le prétérit avec just et already (<b>I just ate</b>), là où le britannique garde le present perfect (<b>I've just eaten</b>).",
"serie": "presentPerfectEnExercises", "kicker": "Le present perfect",
"questions": """
I ___ never been to Chicago. | have | has / am | Je ne suis jamais allé à Chicago. | I + have + participe.
She ___ lost her keys again. | has | have / is | Elle a encore perdu ses clés. | He, she, it + has.
Have you ever ___ sushi? | eaten | ate / eat | Tu as déjà mangé des sushis ? | Have + participe passé : eat → eaten.
We have ___ the tickets. | bought | buyed / buy | Nous avons acheté les billets. | buy → bought → bought, irrégulier.
I saw Tom ___. | yesterday | ever / yet | J'ai vu Tom hier. | Un moment passé précis → prétérit, pas de present perfect.
Has the mail arrived ___? | yet | already / ever | Le courrier est-il déjà arrivé ? | Dans une question, « déjà » attendu = yet, en fin de phrase.
They haven't finished ___. | yet | already / just | Ils n'ont pas encore fini. | Négation + yet = pas encore.
He has ___ left — you just missed him. | just | yet / ever | Il vient de partir, tu l'as raté de peu. | Just = venir de, entre has et le participe.
I ___ my homework last night. | did | have done / has done | J'ai fait mes devoirs hier soir. | Last night = moment précis → prétérit.
How many times ___ you been to Boston? | have | did / are | Combien de fois es-tu allé à Boston ? | Expérience de vie, sans date → present perfect.
She has ___ a lot of new friends this year. | made | make / maked | Elle s'est fait beaucoup de nouveaux amis cette année. | make → made ; this year n'est pas fini → present perfect.
I've ___ paid, so let's go. | already | yet / ever | J'ai déjà payé, allons-y. | Already = déjà (dans une affirmation).
"""
},
{
"id": "for-since", "titre": "For, since, ago", "resume": "Depuis combien de temps, depuis quand, il y a",
"regle": "Le français dit « depuis » au <b>présent</b> : « J'habite ici depuis dix ans ». L'anglais emploie le <b>present perfect</b>, parce que l'action commencée dans le passé dure encore : <b>I have lived here for ten years</b>. <b>For</b> + une <b>durée</b> (for two hours, for a week), <b>since</b> + un <b>point de départ</b> (since Monday, since 2019, since I was a child). <b>Ago</b>, lui, compte en arrière à partir de maintenant, avec le <b>prétérit</b> : <b>I arrived two days ago</b> (il y a deux jours).",
"tableau": [
 ["for + durée", "depuis (combien de temps)", "for three years, for a long time"],
 ["since + point de départ", "depuis (quand)", "since June, since 8 o'clock"],
 ["How long have you…?", "depuis combien de temps… ?", "How long have you known her?"],
 ["durée + ago + prétérit", "il y a", "We met five years ago."],
],
"exemples": [
 ["I've known Anna for ages.", "Je connais Anna depuis une éternité."],
 ["She has worked here since March.", "Elle travaille ici depuis mars."],
 ["He left an hour ago.", "Il est parti il y a une heure."],
],
"attention": "Jamais de présent simple avec for ou since : « Je suis ici depuis une semaine » = <b>I've been here for a week</b>, et non <i>I am here since a week</i> — c'est l'erreur la plus fréquente des francophones.",
"serie": "forSinceEnExercises", "kicker": "For, since, ago",
"questions": """
I've lived in Boston ___ five years. | for | since / ago | J'habite à Boston depuis cinq ans. | Une durée → for.
She has worked here ___ 2019. | since | for / ago | Elle travaille ici depuis 2019. | Un point de départ → since.
We met two years ___. | ago | for / since | Nous nous sommes rencontrés il y a deux ans. | Il y a = ago, après la durée, avec le prétérit.
I ___ here since Monday. | have been | am / was | Je suis ici depuis lundi. | Depuis + action qui dure → present perfect.
How long ___ you known him? | have | do / are | Depuis combien de temps le connais-tu ? | How long + present perfect.
They've been married ___ a long time. | for | since / during | Ils sont mariés depuis longtemps. | A long time est une durée → for.
I haven't seen her ___ Christmas. | since | for / ago | Je ne l'ai pas vue depuis Noël. | Noël est un point de départ → since.
He called ten minutes ___. | ago | before / since | Il a appelé il y a dix minutes. | Ago compte depuis maintenant.
She's had that car ___ she was twenty. | since | for / when | Elle a cette voiture depuis ses vingt ans. | Since peut introduire une phrase entière.
I've waited ___ an hour! | for | since / during | J'attends depuis une heure ! | Une heure = durée → for.
We moved here three months ___. | ago | since / for | Nous avons emménagé ici il y a trois mois. | Ago + prétérit (moved).
I have known her ___ we were kids. | since | for / ago | Je la connais depuis notre enfance. | Point de départ → since.
"""
},
{
"id": "past-continuous", "titre": "Le past continuous", "resume": "I was working when… — le décor et l'action",
"regle": "Le <b>past continuous</b> se forme avec <b>was / were + verbe en -ing</b> : <b>I was reading</b>, <b>they were sleeping</b>. Il décrit une action <b>en cours</b> à un moment du passé, comme l'imparfait français de « j'étais en train de ». On le combine souvent avec le prétérit : l'action longue (le décor) au past continuous, l'action courte qui l'interrompt au prétérit, avec <b>when</b> ou <b>while</b> : <b>I was cooking when the phone rang</b>.",
"tableau": [
 ["I / he / she / it was + -ing", "j'étais en train de…", "I was watching TV."],
 ["you / we / they were + -ing", "tu étais, nous étions…", "We were having dinner."],
 ["wasn't · weren't + -ing", "négation", "She wasn't listening."],
 ["was / were … + -ing ?", "question", "What were you doing at 8?"],
 ["long + when + court", "pendant que… soudain", "I was walking home when it started to rain."],
 ["while + long", "pendant que", "While I was sleeping, someone called."],
],
"exemples": [
 ["At nine o'clock I was still sleeping.", "À neuf heures, je dormais encore."],
 ["It was snowing when we left.", "Il neigeait quand nous sommes partis."],
 ["What were you doing when I called?", "Que faisais-tu quand j'ai appelé ?"],
],
"attention": "L'imparfait d'<b>habitude</b> ne se traduit pas par le past continuous : « Quand j'étais petit, je jouais au hockey » = <b>I played hockey</b> ou <b>I used to play hockey</b>, pas <i>I was playing</i>. Et les verbes d'état (know, want, like) ne prennent pas -ing : <b>I knew</b>, pas <i>I was knowing</i>.",
"serie": "pastContinuousEnExercises", "kicker": "Le past continuous",
"questions": """
I ___ reading when you called. | was | were / am | Je lisais quand tu as appelé. | I + was + -ing.
They ___ playing cards all evening. | were | was / are | Ils ont joué aux cartes toute la soirée. | They + were.
She was cooking when the lights ___ out. | went | were going / go | Elle cuisinait quand la lumière s'est éteinte. | L'action courte qui interrompt → prétérit.
___ I was driving, I heard a strange noise. | While | When / During | Pendant que je conduisais, j'ai entendu un bruit bizarre. | While + action longue en cours.
What ___ you doing at midnight? | were | was / did | Que faisais-tu à minuit ? | You + were + -ing.
It ___ raining, so we stayed home. | was | were / is | Il pleuvait, alors nous sommes restés à la maison. | It + was + -ing : le décor.
He wasn't ___ attention. | paying | pay / paid | Il ne faisait pas attention. | Was / wasn't + verbe en -ing.
I ___ the answer, but I didn't say anything. | knew | was knowing / know | Je connaissais la réponse, mais je n'ai rien dit. | Know est un verbe d'état : pas de -ing.
We were walking in the park when we ___ Tom. | saw | were seeing / see | Nous nous promenions dans le parc quand nous avons vu Tom. | Action courte → prétérit.
The kids ___ sleeping when I got home. | were | was / did | Les enfants dormaient quand je suis rentré. | Kids est pluriel → were.
When I was young, I ___ tennis every weekend. | played | was playing / play | Quand j'étais jeune, je jouais au tennis tous les week-ends. | Une habitude passée → prétérit (ou used to), pas le past continuous.
At 7 a.m. the sun ___ rising. | was | were / is | À 7 h, le soleil se levait. | Le sun est singulier → was.
"""
},
{
"id": "futurs", "titre": "Les futurs : will, going to, -ing", "resume": "Décider, prévoir, avoir prévu",
"regle": "L'anglais a trois façons de parler de l'avenir. <b>Will</b> + verbe : une décision prise sur le moment (<b>I'll get it!</b>), une promesse, une prédiction (<b>It will be cold tomorrow</b>). <b>Be going to</b> + verbe : une intention déjà décidée (<b>I'm going to study law</b>) ou ce qu'on voit venir (<b>Look at those clouds, it's going to rain</b>). Le <b>présent en -ing</b> : un rendez-vous, un projet déjà organisé (<b>I'm seeing the dentist on Friday</b>).",
"tableau": [
 ["will + verbe · 'll", "décision immédiate, promesse, prédiction", "I'll call you tonight."],
 ["won't + verbe", "négation de will", "Don't worry, I won't forget."],
 ["am / is / are going to + verbe", "intention, ce qu'on voit venir", "We're going to buy a house."],
 ["am / is / are + -ing", "rendez-vous, projet organisé", "She's flying to Chicago tomorrow."],
],
"exemples": [
 ["The phone's ringing. — I'll answer it.", "Le téléphone sonne. — Je réponds."],
 ["I'm going to learn the guitar this year.", "Je vais apprendre la guitare cette année."],
 ["What are you doing this weekend?", "Que fais-tu ce week-end ?"],
],
"attention": "Après <b>when</b>, <b>if</b>, <b>as soon as</b>, <b>before</b>, l'anglais met le <b>présent</b> là où le français met le futur : « Quand j'arriverai, je t'appellerai » = <b>When I arrive, I'll call you</b>, et non <i>When I will arrive</i>.",
"serie": "futursEnExercises", "kicker": "Les futurs",
"questions": """
It's cold in here. — I ___ close the window. | 'll | 'm going to / 'm closing | Il fait froid ici. — Je vais fermer la fenêtre. | Décision prise sur le moment → will.
Look at the sky! It's ___ rain. | going to | will / going | Regarde le ciel ! Il va pleuvoir. | On voit venir la pluie → going to.
I ___ my grandparents on Sunday — it's all arranged. | am visiting | will visit / visit | Je rends visite à mes grands-parents dimanche, c'est organisé. | Projet organisé → présent en -ing.
Don't worry, I ___ tell anyone. | won't | don't / am not | Ne t'inquiète pas, je ne le dirai à personne. | Une promesse → won't (will not).
When I ___ home, I'll call you. | get | will get / am going to get | Quand je serai rentré, je t'appellerai. | Après when : le présent, pas will.
We're ___ to buy a new car next year. | going | will / go | Nous allons acheter une nouvelle voiture l'an prochain. | Intention déjà décidée → be going to.
I think it ___ be sunny tomorrow. | will | is / does | Je pense qu'il fera beau demain. | Prédiction (I think) → will.
What time ___ you leaving tomorrow? | are | will / do | À quelle heure pars-tu demain ? | Projet organisé → be + -ing.
She ___ going to study medicine. | is | will / does | Elle va étudier la médecine. | She + is going to.
If it rains, we ___ stay home. | 'll | are / would | S'il pleut, nous resterons à la maison. | If + présent, puis will.
The meeting ___ at 10 a.m. tomorrow. | starts | will starting / is start | La réunion commence demain à 10 h. | Un horaire fixé → présent simple.
I'll wait here until you ___ back. | come | will come / are going to come | J'attends ici jusqu'à ce que tu reviennes. | Après until : le présent.
"""
},
{
"id": "comparatifs", "titre": "Comparatifs et superlatifs", "resume": "bigger, more expensive, the best",
"regle": "Adjectif <b>court</b> (une syllabe, ou deux en -y) : on ajoute <b>-er</b> et <b>the -est</b> : <b>cheap → cheaper → the cheapest</b>, <b>happy → happier → the happiest</b>. Adjectif <b>long</b> : <b>more</b> et <b>the most</b> : <b>expensive → more expensive → the most expensive</b>. On compare avec <b>than</b> (que) : <b>Boston is older than Chicago</b>. L'égalité : <b>as … as</b> (aussi … que) ; <b>not as … as</b> (pas aussi … que). Trois irréguliers à connaître : <b>good → better → the best</b>, <b>bad → worse → the worst</b>, <b>far → farther → the farthest</b>.",
"tableau": [
 ["court + -er than", "plus … que", "This bag is cheaper than that one."],
 ["the + court + -est", "le plus …", "It's the tallest building in Boston."],
 ["more + long + than", "plus … que", "The train is more comfortable than the bus."],
 ["the most + long", "le plus …", "It's the most beautiful park in the city."],
 ["as … as · not as … as", "aussi … que · pas aussi … que", "He's as tall as his father."],
 ["less + adjectif + than", "moins … que", "This one is less expensive."],
],
"exemples": [
 ["My sister is younger than me.", "Ma sœur est plus jeune que moi."],
 ["This is the best pizza in town.", "C'est la meilleure pizza de la ville."],
 ["Today isn't as cold as yesterday.", "Aujourd'hui, il ne fait pas aussi froid qu'hier."],
],
"attention": "Les consonnes doublent : <b>big → bigger</b>, <b>hot → hotter</b>. Et pas de double comparatif : <b>more cheap</b> et <b>more cheaper</b> sont des fautes ; on dit <b>cheaper</b>. « Le plus … du monde » se dit <b>in the world</b>, pas <i>of the world</i>.",
"serie": "comparatifsEnExercises", "kicker": "Comparatifs et superlatifs",
"questions": """
This hotel is ___ than the other one. | cheaper | more cheap / cheapest | Cet hôtel est moins cher que l'autre. | Cheap est court → cheaper.
It's the ___ day of the year. | hottest | most hot / hotter | C'est le jour le plus chaud de l'année. | Hot → hottest, la consonne double.
This book is ___ interesting than the movie. | more | most / -er | Ce livre est plus intéressant que le film. | Interesting est long → more.
She's the ___ student in the class. | best | goodest / better | C'est la meilleure élève de la classe. | Good → better → the best.
My cold is ___ today than yesterday. | worse | badder / worst | Mon rhume est pire aujourd'hui qu'hier. | Bad → worse → the worst.
Tom is as tall ___ his brother. | as | than / like | Tom est aussi grand que son frère. | As … as : l'égalité.
New York is bigger ___ Boston. | than | that / as | New York est plus grand que Boston. | Plus … que = -er than.
This is the most expensive restaurant ___ the city. | in | of / than | C'est le restaurant le plus cher de la ville. | Le plus … de + lieu = in.
I'm ___ than my sister. | happier | more happy / happyer | Je suis plus heureux que ma sœur. | Happy → happier : le y devient i.
The bus is ___ comfortable than the train. | less | fewer / least | Le bus est moins confortable que le train. | Moins + adjectif = less.
It's not ___ cold as last winter. | as | so / more | Il ne fait pas aussi froid que l'hiver dernier. | Not as … as.
Which is the ___ way to the station? | fastest | most fast / faster | Quel est le chemin le plus rapide pour la gare ? | Fast → the fastest.
"""
},
{
"id": "obligation", "titre": "Must, have to, should", "resume": "L'obligation, le conseil, l'interdiction",
"regle": "<b>Must</b> et <b>have to</b> disent l'obligation (devoir). <b>Have to</b> est le plus courant à l'oral, et le seul possible aux autres temps : <b>I had to work</b>, <b>you'll have to wait</b>. <b>Should</b> donne un <b>conseil</b> (tu devrais) : <b>You should see a doctor</b>. Le piège est à la négation : <b>mustn't</b> = c'est <b>interdit</b> ; <b>don't have to</b> = ce n'est <b>pas nécessaire</b>. Must, should et can ne prennent ni -s ni to : <b>she must go</b>.",
"tableau": [
 ["must + verbe", "devoir (obligation forte, règle)", "You must wear a seatbelt."],
 ["have to · has to + verbe", "devoir (obligation)", "She has to get up at six."],
 ["had to · will have to", "devoir au passé · au futur", "We had to wait an hour."],
 ["mustn't + verbe", "ne pas avoir le droit de", "You mustn't smoke here."],
 ["don't / doesn't have to", "ne pas être obligé de", "You don't have to come."],
 ["should · shouldn't + verbe", "devoir (conseil) : tu devrais", "You shouldn't drink so much coffee."],
],
"exemples": [
 ["I have to go now.", "Je dois partir maintenant."],
 ["You should try the clam chowder.", "Tu devrais goûter la chaudrée de palourdes."],
 ["Tomorrow is Sunday, so I don't have to work.", "Demain c'est dimanche, donc je n'ai pas besoin de travailler."],
],
"attention": "<b>You mustn't go</b> (tu ne dois pas y aller : c'est interdit) et <b>You don't have to go</b> (tu n'es pas obligé d'y aller) disent deux choses très différentes, alors que le français dit « tu ne dois pas » dans les deux cas.",
"serie": "obligationEnExercises", "kicker": "Must, have to, should",
"questions": """
You ___ smoke in the hospital. It's forbidden. | mustn't | don't have to / shouldn't to | Tu n'as pas le droit de fumer à l'hôpital. C'est interdit. | Interdiction → mustn't.
It's Saturday. I ___ get up early. | don't have to | mustn't / have to | C'est samedi. Je n'ai pas besoin de me lever tôt. | Pas nécessaire → don't have to.
You look tired. You ___ go to bed. | should | must to / have | Tu as l'air fatigué. Tu devrais aller te coucher. | Un conseil → should.
She ___ work late yesterday. | had to | must / musted | Elle a dû travailler tard hier. | Must n'a pas de passé : had to.
He ___ to wear a uniform at work. | has | have / must | Il doit porter un uniforme au travail. | He + has to.
You should ___ a doctor. | see | to see / seeing | Tu devrais voir un médecin. | Should + verbe nu, sans to.
Passengers ___ show their tickets. | must | mustn't / don't have to | Les passagers doivent montrer leur billet. | Une règle → must.
___ we bring anything to the party? | Do we have to | Have we to / Must we to | On doit apporter quelque chose à la fête ? | Question : Do we have to…?
You ___ eat so much sugar. It's bad for you. | shouldn't | mustn't to / don't should | Tu ne devrais pas manger autant de sucre. | Conseil négatif → shouldn't.
We'll ___ wait for the next bus. | have to | must / should to | Nous allons devoir attendre le prochain bus. | Au futur : will have to.
She doesn't ___ cook tonight; we're eating out. | have to | must / has to | Elle n'a pas besoin de cuisiner ce soir, nous mangeons dehors. | Doesn't + have to (sans s).
You ___ tell anyone. It's a secret! | mustn't | don't have to / shouldn't to | Tu ne dois le dire à personne. C'est un secret ! | Interdiction → mustn't.
"""
},
{
"id": "quantifieurs", "titre": "Some, any, much, many, a few, a little", "resume": "Dire la quantité",
"regle": "Tout dépend de ce qu'on compte. Les noms <b>dénombrables</b> (apples, friends) prennent <b>many</b> (beaucoup), <b>a few</b> (quelques) et <b>few</b> (peu). Les <b>indénombrables</b> (water, time, money, advice) prennent <b>much</b>, <b>a little</b> et <b>little</b>. <b>A lot of</b> va avec les deux. <b>Some</b> s'emploie dans l'affirmation et dans une offre (<b>Would you like some tea?</b>), <b>any</b> dans la question et la négation (<b>Do you have any brothers?</b> · <b>There isn't any milk</b>).",
"tableau": [
 ["many · a few · few", "beaucoup · quelques · peu (dénombrable)", "many cars, a few days"],
 ["much · a little · little", "beaucoup · un peu · peu (indénombrable)", "much time, a little sugar"],
 ["a lot of", "beaucoup de (les deux)", "a lot of people, a lot of money"],
 ["some", "du, des (affirmation, offre)", "I bought some bread."],
 ["any", "du, des (question, négation)", "We don't have any eggs."],
 ["How many…? · How much…?", "combien… ?", "How much does it cost?"],
],
"exemples": [
 ["I have a few questions.", "J'ai quelques questions."],
 ["Could I have a little milk, please?", "Je pourrais avoir un peu de lait, s'il vous plaît ?"],
 ["There aren't many tourists in winter.", "Il n'y a pas beaucoup de touristes en hiver."],
],
"attention": "<b>Advice</b>, <b>information</b>, <b>news</b>, <b>furniture</b>, <b>luggage</b> sont indénombrables en anglais : <b>some advice</b> (des conseils), <b>a piece of information</b> (une information), jamais <i>an advice</i> ni <i>informations</i>. Et <b>a few</b> (quelques, c'est positif) n'est pas <b>few</b> (peu, c'est négatif).",
"serie": "quantifieursEnExercises", "kicker": "Quantifieurs",
"questions": """
How ___ money do you have? | much | many / few | Combien d'argent as-tu ? | Money est indénombrable → much.
How ___ people are coming? | many | much / little | Combien de personnes viennent ? | People est dénombrable → many.
I need ___ advice. | some | an / a few | J'ai besoin de conseils. | Advice est indénombrable : some advice, jamais an advice.
There isn't ___ milk left. | any | some / many | Il ne reste plus de lait. | Négation → any.
Would you like ___ coffee? | some | any / many | Tu veux du café ? | Une offre → some, même dans une question.
I have ___ friends in Boston, so I'm not alone. | a few | a little / few | J'ai quelques amis à Boston, donc je ne suis pas seul. | Quelques (positif) + dénombrable → a few.
Could you add ___ salt? | a little | a few / many | Tu pourrais ajouter un peu de sel ? | Un peu + indénombrable → a little.
Do you have ___ questions? | any | some / much | Avez-vous des questions ? | Une vraie question → any.
There were ___ people at the concert. | a lot of | much / a little | Il y avait beaucoup de monde au concert. | A lot of va avec tout.
She doesn't have ___ time today. | much | many / few | Elle n'a pas beaucoup de temps aujourd'hui. | Time (le temps) est indénombrable → much.
I have a ___ information for you. | piece of | few / an | J'ai une information pour toi. | Information ne se compte pas : a piece of information.
Very ___ students failed the exam. | few | little / much | Très peu d'élèves ont raté l'examen. | Peu + dénombrable → few.
"""
},
{
"id": "ing-ou-to", "titre": "Verbe + -ing ou verbe + to", "resume": "I enjoy cooking, I want to cook",
"regle": "Quand un verbe en suit un autre, le premier décide de la forme du second. Après <b>enjoy, like, love, hate, finish, mind, avoid, keep, suggest, stop</b> : la forme en <b>-ing</b> (<b>I enjoy swimming</b>). Après <b>want, need, decide, hope, plan, learn, promise, forget, would like</b> : <b>to</b> + verbe (<b>I want to swim</b>). Après une <b>préposition</b> (in, at, of, about, before, after), toujours <b>-ing</b> : <b>I'm interested in learning English</b>, <b>Thanks for coming</b>.",
"tableau": [
 ["enjoy · finish · mind · avoid · keep + -ing", "aimer · finir · déranger · éviter · continuer de", "I've finished cleaning."],
 ["like · love · hate + -ing", "aimer, adorer, détester (en général)", "She loves dancing."],
 ["want · need · decide · hope · plan + to", "vouloir · avoir besoin · décider · espérer · prévoir de", "We decided to stay."],
 ["would like + to", "voudrais", "I'd like to order, please."],
 ["préposition + -ing", "de, à, avant de… + infinitif", "Before leaving, lock the door."],
 ["Do you mind + -ing?", "ça vous dérange de… ?", "Do you mind waiting a minute?"],
],
"exemples": [
 ["I don't mind waiting.", "Ça ne me dérange pas d'attendre."],
 ["She's learning to drive.", "Elle apprend à conduire."],
 ["He's good at fixing things.", "Il est doué pour réparer les choses."],
],
"attention": "<b>I'd like to go</b> (je voudrais y aller, maintenant) n'est pas <b>I like going</b> (j'aime y aller, en général). Et après une préposition, jamais d'infinitif : <b>I'm tired of waiting</b>, pas <i>tired of to wait</i>.",
"serie": "ingOuToEnExercises", "kicker": "-ing ou to",
"questions": """
I enjoy ___ in the morning. | running | to run / run | J'aime courir le matin. | Enjoy + -ing.
She wants ___ a doctor. | to become | becoming / become | Elle veut devenir médecin. | Want + to.
Have you finished ___ your homework? | doing | to do / do | Tu as fini de faire tes devoirs ? | Finish + -ing.
We decided ___ at home. | to stay | staying / stay | Nous avons décidé de rester à la maison. | Decide + to.
Do you mind ___ the window? | opening | to open / open | Ça vous dérange d'ouvrir la fenêtre ? | Mind + -ing.
I'd like ___ a table for two. | to book | booking / book | Je voudrais réserver une table pour deux. | Would like + to.
Thanks for ___ me. | helping | to help / help | Merci de m'avoir aidé. | Après for (préposition) → -ing.
He's interested in ___ photography. | learning | to learn / learn | Il s'intéresse à l'apprentissage de la photo. | Après in (préposition) → -ing.
Try to avoid ___ during rush hour. | driving | to drive / drive | Essaie d'éviter de conduire aux heures de pointe. | Avoid + -ing.
I hope ___ you soon. | to see | seeing / see | J'espère te voir bientôt. | Hope + to.
She kept ___ the same question. | asking | to ask / ask | Elle n'arrêtait pas de poser la même question. | Keep + -ing = continuer de, ne pas arrêter de.
Don't forget ___ the lights off. | to turn | turning / turn | N'oublie pas d'éteindre les lumières. | Forget + to : oublier de faire.
"""
},
{
"id": "used-to", "titre": "Used to", "resume": "Ce qu'on faisait avant, et qu'on ne fait plus",
"regle": "<b>Used to</b> + verbe dit une habitude ou un état du passé <b>qui a cessé</b> : <b>I used to smoke</b> (je fumais, avant). Il correspond à l'imparfait d'habitude français, avec l'idée « plus maintenant ». La forme ne change pas avec la personne : <b>she used to live here</b>. Négation et question passent par <b>did</b>, et used perd alors son d : <b>I didn't use to like coffee</b>, <b>Did you use to play sports?</b>",
"tableau": [
 ["used to + verbe", "avant, je… (plus maintenant)", "We used to live in Ohio."],
 ["didn't use to + verbe", "avant, je ne… pas", "He didn't use to wear glasses."],
 ["Did … use to + verbe?", "est-ce qu'avant… ?", "Did you use to walk to school?"],
 ["never used to", "ne… jamais (avant)", "I never used to cook."],
],
"exemples": [
 ["There used to be a cinema on this street.", "Il y avait un cinéma dans cette rue, avant."],
 ["I used to hate vegetables, but now I love them.", "Avant, je détestais les légumes, mais maintenant je les adore."],
 ["Did your parents use to read to you?", "Tes parents te faisaient la lecture quand tu étais petit ?"],
],
"attention": "Ne pas confondre avec <b>be used to</b> + -ing (avoir l'habitude de, B1) : <b>I used to work at night</b> (avant, je travaillais la nuit) ≠ <b>I'm used to working at night</b> (j'ai l'habitude de travailler la nuit). Et pas de used to au présent : « d'habitude » se dit <b>usually</b>.",
"serie": "usedToEnExercises", "kicker": "Used to",
"questions": """
I ___ to play the piano, but I stopped. | used | use / am used | Je jouais du piano, mais j'ai arrêté. | Habitude passée qui a cessé → used to.
She used to ___ in Chicago. | live | living / lived | Elle habitait à Chicago, avant. | Used to + verbe nu.
Did you ___ to have long hair? | use | used / using | Avant, tu avais les cheveux longs ? | Après did : use, sans d.
He didn't ___ to like sports. | use | used / uses | Avant, il n'aimait pas le sport. | Didn't + use to.
There ___ to be a bakery here. | used | use / was | Il y avait une boulangerie ici, avant. | There used to be = il y avait (avant).
I ___ walk to work, but now I drive. | used to | use to / am used | J'allais au travail à pied, mais maintenant je conduis. | Le contraste avant / maintenant → used to.
We ___ go to the beach every summer when I was a kid. | used to | were used / use to | Nous allions à la plage chaque été quand j'étais petit. | Habitude d'enfance → used to.
I ___ get up at six on weekdays. | usually | use to / used | Je me lève d'habitude à six heures en semaine. | Au présent, l'habitude se dit usually.
My father used to ___ me stories. | tell | telling / told | Mon père me racontait des histoires. | Used to + verbe nu.
___ she use to work here? | Did | Does / Was | Est-ce qu'elle travaillait ici, avant ? | Question au passé → Did.
They never used ___ a car. | to have | have / having | Ils n'ont jamais eu de voiture, avant. | Never used to + verbe.
I used to be shy, but I'm not ___. | anymore | already / yet | J'étais timide, mais je ne le suis plus. | Not anymore = ne… plus.
"""
},
]
