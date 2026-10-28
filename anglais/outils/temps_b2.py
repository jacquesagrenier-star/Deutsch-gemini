# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » de l'anglais, B2 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

TEMPS = [
{
"id": "temps-parfaits-continus", "titre": "Les temps parfaits continus",
"texte": "<b>Have been + -ing</b> (present perfect continuous) : une activité qui dure jusqu'à maintenant, ou dont on voit les traces. <b>Had been + -ing</b> (past perfect continuous) : la même chose, avant un moment du passé. Le simple compte un résultat, le continu insiste sur la durée.<br><em>I've been waiting for an hour. She had been crying.</em> (J'attends depuis une heure. Elle avait pleuré.)",
"serie": "tempsParfaitsContinusEnExercises", "kicker": "Les parfaits continus",
"questions": """
I've ___ waiting for you since noon. | been | being / be | Je t'attends depuis midi. | Have been + -ing.
How long have you ___ learning English? | been | being / were | Depuis combien de temps apprends-tu l'anglais ? | How long have you been + -ing?
It ___ raining all day. | has been | is being / was been | Il pleut depuis ce matin, toute la journée. | Has been + -ing : ça dure jusqu'à maintenant.
You're all sweaty. Have you been ___? | running | run / ran | Tu es tout en sueur. Tu as couru ? | Traces d'une activité récente : -ing.
She's been ___ at the same company for twenty years. | working | worked / work | Elle travaille dans la même entreprise depuis vingt ans. | Have been + -ing.
I've ___ three chapters this morning. | written | been writing / writing | J'ai écrit trois chapitres ce matin. | Un nombre, un résultat : present perfect simple.
I've ___ all morning, and I'm still not done. | been writing | written / wrote | J'écris depuis ce matin et je n'ai toujours pas fini. | La durée, l'activité : continu.
We've ___ each other for ages. | known | been knowing / knowing | Nous nous connaissons depuis une éternité. | Know (verbe d'état) : jamais à la forme continue.
They've been ___ about money again. | arguing | argued / argue | Ils se sont encore disputés au sujet de l'argent. | Have been + -ing.
Your eyes are red. ___ you been crying? | Have | Had / Did | Tu as les yeux rouges. Tu as pleuré ? | Question : Have + sujet + been + -ing.
I ___ been sleeping well lately. | haven't | hadn't / didn't | Je ne dors pas bien ces derniers temps. | Négation : haven't been + -ing.
He's been ___ that same jacket since high school. | wearing | worn / wore | Il porte la même veste depuis le lycée. | Have been + -ing.
How many cups of coffee ___ you had today? | have | have been / did | Combien de tasses de café as-tu bues aujourd'hui ? | How many → résultat, compte : simple.
How long have you ___ for the bus? | been waiting | waited for / wait | Depuis combien de temps attends-tu l'autobus ? | How long + continu.
She ___ been feeling well since the accident. | hasn't | isn't / didn't | Elle ne se sent pas bien depuis l'accident. | Hasn't been + -ing.
We'd been ___ for two hours when the car broke down. | driving | driven / drive | Nous roulions depuis deux heures quand la voiture est tombée en panne. | Had been + -ing avant un moment passé.
She was exhausted. She ___ all night. | had been working | has been working / works | Elle était épuisée. Elle avait travaillé toute la nuit. | Past perfect continuous : la durée explique un état passé.
The ground was wet. It ___. | had been raining | has been raining / rains | Le sol était mouillé. Il avait plu. | Traces d'une activité, au passé.
How long ___ they been dating before they got engaged? | had | have / did | Depuis combien de temps sortaient-ils ensemble avant leurs fiançailles ? | Had + been + -ing.
I'd been ___ to call you all week. | meaning | meant / mean | Ça fait toute la semaine que je voulais t'appeler. | Had been meaning to = avoir l'intention depuis un moment.
He ___ smoking for twenty years when he finally quit. | had been | has been / was been | Il fumait depuis vingt ans quand il a enfin arrêté. | Had been + -ing.
I've been ___ this book for weeks, but I've only read half. | reading | read / reads | Je lis ce livre depuis des semaines, mais je n'en ai lu que la moitié. | Activité en cours : continu.
I've ___ this book twice. | read | been reading / reading | J'ai lu ce livre deux fois. | Twice : résultat, simple.
They have ___ in Boston since 2015. | been living | live / been live | Ils vivent à Boston depuis 2015. | Have been + -ing.
The phone's been ___ all morning. | ringing | rung / ring | Le téléphone n'arrête pas de sonner depuis ce matin. | Activité répétée qui dure : continu.
I've ___ my keys. Have you seen them? | lost | been losing / losing | J'ai perdu mes clés. Tu les as vues ? | Un événement unique, un résultat : simple.
What have you been ___ lately? | up to | doing up / up | Qu'est-ce que tu deviens ces temps-ci ? | What have you been up to? = quoi de neuf ?
The kids are dirty — they've been ___ in the mud. | playing | played / play | Les enfants sont sales : ils ont joué dans la boue. | Traces visibles : continu.
I ___ waiting long when the doctor called my name. | hadn't been | haven't been / wasn't been | Je n'attendais pas depuis longtemps quand le médecin m'a appelé. | Hadn't been + -ing.
She's been ___ Spanish for two years, and she's getting good. | studying | studied / study | Elle étudie l'espagnol depuis deux ans et elle commence à être bonne. | Have been + -ing.
""",
},
{
"id": "temps-futurs-avances", "titre": "Future continuous et future perfect",
"texte": "<b>Will be + -ing</b> (future continuous) : ce qui sera en cours à un moment de l'avenir. <b>Will have + participe</b> (future perfect) : ce qui sera terminé avant un moment de l'avenir, souvent avec <b>by</b>.<br><em>This time tomorrow, I'll be flying to Denver. By June, I'll have finished.</em> (Demain à cette heure-ci, je serai dans l'avion pour Denver. D'ici juin, j'aurai fini.)",
"serie": "tempsFutursAvancesEnExercises", "kicker": "Futurs avancés",
"questions": """
This time tomorrow, I'll ___ on a beach in Florida. | be lying | lie / have lain | Demain à cette heure-ci, je serai allongé sur une plage en Floride. | Action en cours à un moment futur : will be + -ing.
By the time you get home, I'll ___ dinner. | have made | be make / made | Le temps que tu rentres, j'aurai préparé le souper. | Terminé avant un moment futur : will have + participe.
Don't call at eight — we'll ___ dinner. | be having | have had / having | N'appelle pas à huit heures : nous serons en train de souper. | Will be + -ing.
By 2030, they ___ the new bridge. | will have built | will build / are building | D'ici 2030, ils auront construit le nouveau pont. | By + date : will have + participe.
Next month, she ___ here for ten years. | will have worked | will work / works | Le mois prochain, ça fera dix ans qu'elle travaille ici. | Durée accomplie à un moment futur.
At noon tomorrow, I'll ___ my driving test. | be taking | have taken / take | Demain midi, je serai en train de passer mon examen de conduite. | Will be + -ing.
I'll have ___ the report by Friday. | finished | finish / finishing | J'aurai fini le rapport d'ici vendredi. | Will have + participe.
Will you ___ the car tomorrow? I'd like to borrow it. | be using | have used / using | Vas-tu te servir de la voiture demain ? J'aimerais l'emprunter. | Question polie sur un projet : will be + -ing.
By the end of the day, we ___ two hundred miles. | will have driven | will drive / drive | D'ici la fin de la journée, nous aurons fait deux cents milles. | Will have + participe.
In ten years, I'll probably ___ in a different city. | be living | have lived / live in | Dans dix ans, je vivrai sans doute dans une autre ville. | Situation en cours dans l'avenir.
She won't ___ by the time we arrive. | have left | be leave / left | Elle ne sera pas partie le temps qu'on arrive. | Won't have + participe.
They ___ the results by Monday. | will have received | will be receiving yet / receive | Ils auront reçu les résultats d'ici lundi. | By Monday : will have + participe.
I'll ___ at the café at four if you want to join me. | be working | have worked / working | Je travaillerai au café à quatre heures si tu veux te joindre à moi. | Will be + -ing.
By the time he retires, he'll ___ forty years. | have taught | be teaching for / taught | Le temps qu'il prenne sa retraite, il aura enseigné quarante ans. | Will have + participe.
The plane ___ by the time we reach the airport. | will have taken off | will take off / takes off | L'avion aura décollé le temps que nous arrivions à l'aéroport. | Will have + participe.
Don't worry, I ___ you. I'll be at the station at six. | won't forget | won't be forgetting you / don't forget | Ne t'inquiète pas, je ne t'oublierai pas. Je serai à la gare à six heures. | Promesse : won't + verbe.
How long will you ___ when you finish your degree? | have been studying | be study / studied | Depuis combien de temps auras-tu étudié quand tu finiras ton diplôme ? | Will have been + -ing.
By next year, I'll have ___ English for five years. | been learning | learning / learn | L'an prochain, ça fera cinq ans que j'apprends l'anglais. | Will have been + -ing : durée à un moment futur.
We'll ___ over Ohio around midnight. | be flying | have flown / fly over | Nous survolerons l'Ohio vers minuit. | Will be + -ing.
Call me after nine. I'll ___ dinner by then. | have finished | be finishing / finished | Appelle-moi après neuf heures. J'aurai fini de souper d'ici là. | By then : will have + participe.
When you get to the party, everyone ___ dancing. | will be | will have / is being | Quand tu arriveras à la fête, tout le monde dansera. | Will be + -ing.
Hopefully, the snow ___ by the weekend. | will have melted | will melting / melts by | Espérons que la neige aura fondu d'ici le week-end. | Will have + participe.
Next Monday I ___ the new office in Seattle. | will be visiting | will have visit / visiting | Lundi prochain, je visiterai le nouveau bureau de Seattle. | Projet prévu : will be + -ing.
By then, prices ___ again. | will have gone up | will go up then / go up | D'ici là, les prix auront encore augmenté. | Will have + participe.
""",
},
]
