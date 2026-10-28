# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » de l'anglais, B1 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

TEMPS = [
{
"id": "temps-present-perfect", "titre": "Present perfect ou past simple ?",
"texte": "<b>Have / has + participe passé</b> relie le passé au présent : une expérience (ever, never), un résultat visible maintenant, une période pas finie (today, this week, for, since). Dès qu'on date l'action (yesterday, in 2020, ago), c'est le <b>past simple</b>.<br><em>I've lost my keys. — I lost them yesterday.</em> (J'ai perdu mes clés. — Je les ai perdues hier.)",
"serie": "tempsPresentPerfectEnExercises", "kicker": "Present perfect / past simple",
"questions": """
I ___ to Chicago three times. | have been | went / was | Je suis allé trois fois à Chicago. | Une expérience, sans date : present perfect.
I ___ to Chicago last summer. | went | have been / have gone | Je suis allé à Chicago l'été dernier. | Last summer : date précise → past simple.
___ you ever eaten lobster? | Have | Did / Do | As-tu déjà mangé du homard ? | Ever : expérience → present perfect.
Did you ___ lobster in Maine? | eat | eaten / ate | As-tu mangé du homard dans le Maine ? | Did + verbe nu.
She has ___ her phone. She can't find it anywhere. | lost | lose / losed | Elle a perdu son téléphone. Elle ne le trouve nulle part. | Résultat visible maintenant : has + participe.
We ___ here since 2018. | have lived | lived / live | Nous habitons ici depuis 2018. | Since + présent français → present perfect.
They ___ married for ten years. | have been | are / were since | Ils sont mariés depuis dix ans. | For + durée qui continue : present perfect.
He ___ in Boston for ten years, then moved to Texas. | lived | has lived / lives | Il a habité dix ans à Boston, puis il a déménagé au Texas. | Période finie : past simple.
I ___ him since high school. | have known | know / knew | Je le connais depuis le lycée. | Since : present perfect (know, verbe d'état).
I haven't seen her ___ Monday. | since | for / ago | Je ne l'ai pas vue depuis lundi. | Point de départ : since.
I haven't seen her ___ a week. | for | since / ago | Je ne l'ai pas vue depuis une semaine. | Durée : for.
I saw her two weeks ___. | ago | since / for | Je l'ai vue il y a deux semaines. | Il y a… = ago, avec le past simple.
Have you finished your homework ___? | yet | already / still | As-tu déjà fini tes devoirs ? | Question, « déjà » = yet (en fin de phrase).
I've ___ finished. Can I go? | already | yet / still yet | J'ai déjà fini. Je peux y aller ? | Affirmation : already, avant le participe.
She hasn't called ___. | yet | already / still | Elle n'a pas encore appelé. | Négation : yet (pas encore).
I've ___ come back from the gym. | just | yet / ever | Je viens de rentrer du gym. | Venir de… = have just + participe.
This is the best pizza I've ___ had. | ever | never / yet | C'est la meilleure pizza que j'aie jamais mangée. | Superlatif + I've ever.
I've ___ been to Alaska. | never | ever / yet | Je ne suis jamais allé en Alaska. | Never + participe.
When ___ you arrive? | did | have / has | Quand es-tu arrivé ? | When : question de date → past simple.
How long ___ you worked here? | have | did / are | Depuis combien de temps travailles-tu ici ? | How long + present perfect = depuis combien de temps.
He ___ three books this year. | has written | wrote last / writes | Il a écrit trois livres cette année. | This year (pas finie) : present perfect.
He ___ three books in 2019. | wrote | has written / writes | Il a écrit trois livres en 2019. | In 2019 : past simple.
My parents have ___ to Florida. They're back next week. | gone | been / went | Mes parents sont partis en Floride. Ils reviennent la semaine prochaine. | Gone = ils y sont encore.
My parents have ___ to Florida. They loved it. | been | gone / went | Mes parents sont allés en Floride. Ils ont adoré. | Been = ils y sont allés et sont revenus.
Oh no! I ___ my coffee on the keyboard. | 've spilled | spill / was spilling | Oh non ! J'ai renversé mon café sur le clavier. | Résultat sous nos yeux : present perfect.
The game ___ at seven and ended at ten. | started | has started / starts | Le match a commencé à sept heures et a fini à dix heures. | Récit daté : past simple.
Prices ___ a lot recently. | have gone up | went up / go up | Les prix ont beaucoup augmenté récemment. | Recently : present perfect.
I ___ a lot of coffee today. | 've had | had yesterday / have | J'ai bu beaucoup de café aujourd'hui. | Today (pas fini) : present perfect.
She ___ her keys this morning, but she found them. | lost | has lost / loses | Elle a perdu ses clés ce matin, mais elle les a retrouvées. | Ce matin (fini), histoire close : past simple.
We ___ each other for years. | haven't seen | didn't see / don't see | Nous ne nous sommes pas vus depuis des années. | For + négation : present perfect.
Has she ___ the report yet? | sent | send / sended | A-t-elle déjà envoyé le rapport ? | Has + participe.
They ___ the house in 2015. | bought | have bought / buy | Ils ont acheté la maison en 2015. | In 2015 : past simple.
They ___ in that house since 2015. | have lived | lived / live | Ils habitent cette maison depuis 2015. | Since : present perfect.
I ___ that movie. Let's watch something else. | 've seen | saw yesterday / see | J'ai déjà vu ce film. Regardons autre chose. | Expérience : present perfect.
I ___ that movie last week. | saw | have seen / see | J'ai vu ce film la semaine dernière. | Last week : past simple.
Where ___ you been? I've been waiting for an hour! | have | did / were | Où étais-tu passé ? Ça fait une heure que j'attends ! | Where have you been?
Where ___ you go last night? | did | have / were | Où es-tu allé hier soir ? | Last night : past simple.
It's the first time I ___ snow. | 've seen | see / saw | C'est la première fois que je vois de la neige. | It's the first time + present perfect.
Shakespeare ___ many plays. | wrote | has written / writes | Shakespeare a écrit de nombreuses pièces. | Personne décédée : période finie → past simple.
She ___ four novels so far. | has published | published / publishes | Elle a publié quatre romans jusqu'ici. | So far : present perfect.
I ___ my wallet! Can you lend me ten dollars? | 've forgotten | forget / was forgetting | J'ai oublié mon portefeuille ! Tu peux me prêter dix dollars ? | Conséquence maintenant : present perfect.
How many times ___ you been to Canada? | have | did / are | Combien de fois es-tu allé au Canada ? | How many times + present perfect.
What time ___ the meeting start? | did | has / have | À quelle heure la réunion a-t-elle commencé ? | Heure précise : past simple.
I've lived here ___ I was a child. | since | for / when | J'habite ici depuis que je suis enfant. | Since + proposition.
Has anyone ___ my glasses? | seen | saw / see | Quelqu'un a vu mes lunettes ? | Has + participe.
He ___ his leg, so he can't play this weekend. | 's broken | broke last / breaks | Il s'est cassé la jambe, alors il ne peut pas jouer ce week-end. | Conséquence présente : present perfect.
The company ___ in 1998. | was founded | has been founded / is founded | L'entreprise a été fondée en 1998. | Date : past simple (passif).
We ___ any rain this month. | haven't had | didn't have / don't have | Nous n'avons pas eu de pluie ce mois-ci. | This month : present perfect.
""",
},
{
"id": "temps-past-perfect", "titre": "Past perfect — le passé avant le passé",
"texte": "<b>Had + participe passé</b>, à toutes les personnes : une action déjà accomplie avant un autre moment du passé. C'est le plus-que-parfait français.<br><em>When I arrived, the train had left.</em> (Quand je suis arrivé, le train était parti.)",
"serie": "tempsPastPerfectEnExercises", "kicker": "Past perfect",
"questions": """
When we got to the theater, the movie ___ started. | had already | has already / already | Quand nous sommes arrivés au cinéma, le film avait déjà commencé. | Antérieur à un autre passé : had + participe.
I ___ never seen the ocean before that trip. | had | have / did | Je n'avais jamais vu l'océan avant ce voyage. | Never… before, dans un récit : past perfect.
She was tired because she ___ all night. | had worked | has worked / works | Elle était fatiguée parce qu'elle avait travaillé toute la nuit. | La cause, antérieure : past perfect.
By the time the police arrived, the thief ___. | had escaped | has escaped / escapes | Le temps que la police arrive, le voleur s'était enfui. | By the time + past simple, had + participe.
After she ___ dinner, she went for a walk. | had eaten | has eaten / eats | Après avoir soupé, elle est allée marcher. | After + past perfect.
He told me he ___ the movie before. | had seen | has seen / sees | Il m'a dit qu'il avait déjà vu le film. | Discours rapporté au passé : had + participe.
I couldn't get in because I ___ my keys. | had lost | have lost / lose | Je ne pouvais pas entrer parce que j'avais perdu mes clés. | Cause antérieure : past perfect.
When I ___ home, my roommate had already cooked dinner. | got | had got / get | Quand je suis rentré, mon colocataire avait déjà fait le souper. | L'action de référence : past simple.
They ___ each other for years before they got married. | had known | have known / know | Ils se connaissaient depuis des années avant de se marier. | Durée avant un moment passé : had + participe.
___ you ever been to Boston before you moved here? | Had | Have / Did | Étais-tu déjà allé à Boston avant d'emménager ici ? | Question : Had + sujet + participe.
She ___ finished her homework when her friends came over. | hadn't | hasn't / didn't | Elle n'avait pas fini ses devoirs quand ses amis sont passés. | Négation : hadn't + participe.
The store ___ closed by the time we got there. | had | has / have | Le magasin avait fermé le temps qu'on arrive. | Had + participe.
I realized I ___ the stove on. | had left | have left / leave | Je me suis rendu compte que j'avais laissé la cuisinière allumée. | Realized + action antérieure.
He ___ the book three times before the exam. | had read | has read / reads | Il avait lu le livre trois fois avant l'examen. | Avant un moment passé : past perfect.
The kids were happy because they ___ the game. | had won | have won / win | Les enfants étaient contents parce qu'ils avaient gagné le match. | Cause antérieure.
When I opened the fridge, someone ___ all the milk. | had drunk | has drunk / drinks | Quand j'ai ouvert le frigo, quelqu'un avait bu tout le lait. | Drink → drunk.
We arrived late. The concert ___ an hour earlier. | had started | has started / starts | Nous sommes arrivés en retard. Le concert avait commencé une heure plus tôt. | Earlier, dans un récit : past perfect.
The ground was wet. It ___ during the night. | had rained | has rained / rains | Le sol était mouillé. Il avait plu pendant la nuit. | Explication antérieure.
I ___ him before, so I didn't recognize him. | hadn't met | haven't met / didn't meet yet | Je ne l'avais jamais rencontré, alors je ne l'ai pas reconnu. | Négation : hadn't + participe.
She asked me if I ___ lunch. | had had | have had / has | Elle m'a demandé si j'avais déjà dîné. | Had + had (participe de have).
As soon as the guests ___, we started cleaning. | had left | have left / leave | Dès que les invités furent partis, nous avons commencé à ranger. | As soon as + past perfect.
It was the first time I ___ a moose. | had seen | have seen / see | C'était la première fois que je voyais un orignal. | It was the first time + past perfect.
He was nervous because he ___ flown before. | had never | has never / never had | Il était nerveux parce qu'il n'avait jamais pris l'avion. | Had never + participe.
I'd ___ the email before you called. | sent | send / sending | J'avais envoyé le courriel avant que tu appelles. | 'd = had, suivi d'un participe.
I'd ___ you if I had time. | help | helped / helping | Je t'aiderais si j'avais le temps. | 'd = would, suivi du verbe nu.
By 2010, she ___ in four different countries. | had lived | has lived / lives | En 2010, elle avait vécu dans quatre pays différents. | By + date passée : past perfect.
When I woke up, my husband ___ to work. | had already gone | has already gone / already goes | Quand je me suis réveillée, mon mari était déjà parti travailler. | Already + past perfect.
They ___ dinner when we arrived, so we ate alone. | had finished | have finished / finish | Ils avaient fini de souper quand nous sommes arrivés, alors nous avons mangé seuls. | Antériorité : past perfect.
He said he ___ the keys on the table. | had put | has put / puts | Il a dit qu'il avait posé les clés sur la table. | Put → put.
The house looked different. They ___ it. | had painted | have painted / paint | La maison avait l'air différente. Ils l'avaient repeinte. | Explication d'un état passé.
""",
},
{
"id": "temps-conditionnel", "titre": "Would — le conditionnel",
"texte": "<b>Would + verbe nu</b> traduit le conditionnel français : une hypothèse, un souhait, une demande polie. Avec <b>if + prétérit</b> pour une situation imaginaire ; <b>would have + participe</b> pour un passé qui n'a pas eu lieu.<br><em>If I had more time, I would travel. I would have called you.</em> (Si j'avais plus de temps, je voyagerais. Je t'aurais appelé.)",
"serie": "tempsConditionnelEnExercises", "kicker": "Le conditionnel",
"questions": """
If I had more money, I ___ a house. | would buy | will buy / bought | Si j'avais plus d'argent, j'achèterais une maison. | Hypothèse : if + prétérit, would + verbe.
If she ___ the answer, she would tell us. | knew | knows / would know | Si elle connaissait la réponse, elle nous la dirait. | Après if, prétérit (jamais would).
I ___ love to come, but I'm busy. | would | will / am | J'aimerais beaucoup venir, mais je suis occupé. | Would love to = aimerais beaucoup.
___ you like some coffee? | Would | Will / Do | Voulez-vous du café ? | Offre polie : Would you like…?
I'd ___ a table for two, please. | like | liked / liking | Je voudrais une table pour deux, s'il vous plaît. | I'd like = je voudrais.
What ___ you do if you won the lottery? | would | will / did | Que ferais-tu si tu gagnais à la loterie ? | Would + sujet + verbe.
If I ___ you, I'd see a doctor. | were | am / would be | Si j'étais toi, j'irais voir un médecin. | If I were you : conseil.
It ___ be nice to see you again. | would | will to / is | Ce serait bien de te revoir. | Would be = serait.
I wouldn't ___ that if I were you. | do | did / doing | Je ne ferais pas ça si j'étais toi. | Wouldn't + verbe nu.
If it ___ this weekend, we'll stay home. | rains | rained / would rain | S'il pleut ce week-end, nous resterons à la maison. | Possible et réel : if + présent, will.
If it ___ warmer, we'd go to the beach. | were | is / would be | S'il faisait plus chaud, nous irions à la plage. | Imaginaire : if + prétérit.
She ___ help you if you asked her. | would | will / did | Elle t'aiderait si tu lui demandais. | Would + verbe nu.
___ you mind closing the door? | Would | Will you / Do | Ça vous dérangerait de fermer la porte ? | Would you mind + -ing.
He said he ___ call me later. | would | will / is | Il a dit qu'il m'appellerait plus tard. | Discours rapporté : will → would.
If I had known, I ___ you. | would have helped | would help / helped | Si j'avais su, je t'aurais aidé. | Passé imaginaire : would have + participe.
If you ___ earlier, you would have caught the train. | had left | left / would leave | Si tu étais parti plus tôt, tu aurais attrapé le train. | If + past perfect.
I ___ come, but nobody told me. | would have | will have / would | Je serais venu, mais personne ne me l'a dit. | Would have + participe.
She ___ have passed if she had studied. | would | will / had | Elle aurait réussi si elle avait étudié. | Would have + participe.
We ___ have gone if we'd known it was so expensive. | wouldn't | won't / didn't | Nous n'y serions pas allés si nous avions su que c'était si cher. | Wouldn't have + participe.
I'd rather ___ in tonight. | stay | to stay / staying | Je préférerais rester à la maison ce soir. | I'd rather + verbe nu.
You ___ wear a coat. It's freezing. | should | would / will | Tu devrais mettre un manteau. Il gèle. | Conseil : should (devrais).
We ___ go to the movies tonight, if you want. | could | would can / will can | On pourrait aller au cinéma ce soir, si tu veux. | Pourrait = could.
If I could fly, I ___ to Hawaii. | would go | will go / went | Si je pouvais voler, j'irais à Hawaï. | Would + verbe nu.
What would you do ___ you lost your passport? | if | when / would | Que ferais-tu si tu perdais ton passeport ? | Hypothèse : if.
I would ___ you, but my phone was dead. | have called | call / called | Je t'aurais appelé, mais mon téléphone était déchargé. | Would have + participe.
If she ___ more, she'd be healthier. | exercised | exercises / would exercise | Si elle faisait plus d'exercice, elle serait en meilleure santé. | If + prétérit.
How ___ you feel if this happened to you? | would | will / do | Comment te sentirais-tu si ça t'arrivait ? | How would you feel…?
I ___ be happy to help. | would | will to / am to | Je serais heureux d'aider. | Would be happy to = serais heureux de.
It would be better if you ___ earlier. | came | come / would come | Ce serait mieux si tu venais plus tôt. | If + prétérit.
If we'd taken a taxi, we ___ late. | wouldn't have been | won't be / weren't | Si nous avions pris un taxi, nous n'aurions pas été en retard. | Would have been.
I wish I ___ speak Spanish. | could | can / would can | J'aimerais savoir parler espagnol. | I wish + could.
Could you ___ me the salt, please? | pass | passed / passing | Pourrais-tu me passer le sel, s'il te plaît ? | Could you + verbe nu.
In your place, I ___ accept the offer. | would | will / am | À ta place, j'accepterais l'offre. | À ta place = would.
She would have ___ the job if she'd applied. | gotten | got to / get | Elle aurait eu le poste si elle avait postulé. | Would have + participe (gotten, en américain).
When I was a kid, we ___ go to the lake every summer. | would | will / should | Quand j'étais petit, on allait au lac tous les étés. | Would = habitude passée (comme used to).
""",
},
]
