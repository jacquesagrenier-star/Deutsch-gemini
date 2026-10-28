# -*- coding: utf-8 -*-
"""Les series C1 allongees (28 oct. 2026) : des questions a la suite des
douze de chaque fiche (grammaire_c1.py), pour approcher le volume des series
allemandes. Meme format : question | bonne | fausse / fausse | traduction | explication.
Les cinq autres fiches sont dans series_c1_suite.py.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""
from series_c1_suite import SUITE

SUPPLEMENTS = {
"inversionEnExercises": """
Never ___ I been so embarrassed. | have | did / was | Je n'ai jamais été aussi gêné. | Never + inversion : have I.
Never before ___ such a storm hit the city. | had | has / did | Jamais une telle tempête n'avait frappé la ville. | Never before + had + sujet.
Rarely ___ we see him these days. | do | did / are | Nous le voyons rarement ces temps-ci. | Rarely + do + sujet.
Seldom ___ she been so happy. | has | did / does | Elle a rarement été aussi heureuse. | Seldom + has + sujet.
Not only ___ he lie, but he also stole money. | did | has / was | Non seulement il a menti, mais il a aussi volé de l'argent. | Not only + did + sujet.
Not only ___ the hotel cheap, it was also beautiful. | was | did / had | Non seulement l'hôtel était bon marché, mais il était aussi magnifique. | Avec be : was + sujet.
Hardly ___ we arrived when the show started. | had | have / did | À peine étions-nous arrivés que le spectacle a commencé. | Hardly + had + sujet + participe … when.
Scarcely had she left ___ the phone rang. | when | than / that | Elle venait à peine de partir que le téléphone a sonné. | Scarcely … when.
No sooner ___ I paid than the price dropped. | had | have / did | J'avais à peine payé que le prix a baissé. | No sooner had … than.
Only later ___ I realize my mistake. | did | had / was | Ce n'est que plus tard que j'ai compris mon erreur. | Only later + did + sujet.
Only by working together ___ we succeed. | can | we can / could we be | Ce n'est qu'en travaillant ensemble que nous réussirons. | Only by + -ing + inversion.
Only when the lights went out ___ we notice the stars. | did | we did / had | Ce n'est que quand les lumières se sont éteintes que nous avons vu les étoiles. | Only when … + inversion.
Not until the next morning ___ they find the car. | did | had / they did | Ce n'est que le lendemain matin qu'ils ont trouvé la voiture. | Not until … + did + sujet.
Under no circumstances ___ employees share passwords. | may | they may / do | Les employés ne doivent en aucun cas partager leurs mots de passe. | Under no circumstances + modal + sujet.
On no account ___ you leave the children alone. | should | you should / do | Tu ne dois sous aucun prétexte laisser les enfants seuls. | On no account + inversion.
In no way ___ I responsible for this. | am | I am / do | Je ne suis en aucun cas responsable de ça. | In no way + am + sujet.
At no point ___ he mention the money. | did | he did / has | À aucun moment il n'a parlé de l'argent. | At no point + did + sujet.
Little ___ she realize how famous she would become. | did | she did / had | Elle était loin de se douter qu'elle deviendrait si célèbre. | Little + did + sujet.
Nowhere ___ you find better pizza. | will | you will / do you will | Nulle part tu ne trouveras de meilleure pizza. | Nowhere + will + sujet.
So tired ___ that she fell asleep at her desk. | was she | she was / did she | Elle était si fatiguée qu'elle s'est endormie à son bureau. | So + adjectif + inversion.
Such ___ his anger that nobody dared to speak. | was | is it / did | Sa colère était telle que personne n'osait parler. | Such + be + sujet.
___ you need any help, please call me. | Should | Would / If | Si vous avez besoin d'aide, appelez-moi. | Should + sujet = if.
___ I in your position, I would resign. | Were | Was / If | Si j'étais à votre place, je démissionnerais. | Were + sujet = if … were.
___ it not for the rain, we would go out. | Were | Was / Had | S'il n'y avait pas la pluie, nous sortirions. | Were it not for = sans.
Had we ___ the risks, we wouldn't have invested. | known | knew / know | Si nous avions connu les risques, nous n'aurions pas investi. | Had + sujet + participe.
Not once ___ he say thank you. | did | he did / has he | Pas une seule fois il n'a dit merci. | Not once + did + sujet.
Never ___ I forget that day. | will | I will / shall I be | Je n'oublierai jamais ce jour-là. | Never + will + sujet.
Only in Boston ___ you find so many universities. | do | you do / does | Ce n'est qu'à Boston qu'on trouve autant d'universités. | Only + lieu + inversion.
Rarely ___ such a talented student come along. | does | do / is | Il est rare qu'un élève aussi doué se présente. | Rarely + does + sujet singulier.
Not a word ___ she say all evening. | did | she did / had | Elle n'a pas dit un mot de la soirée. | Not a + nom + inversion.
In vain ___ they search for the missing hiker. | did | they did / had | Ils ont cherché en vain le randonneur disparu. | In vain + inversion (littéraire).
Not only ___ she speak French, she also writes it. | does | is / has | Non seulement elle parle français, mais elle l'écrit aussi. | Not only + does + sujet.
Never ___ the team played so well. | had | did / was | Jamais l'équipe n'avait aussi bien joué. | Never + had + sujet.
Hardly ___ anyone noticed the change. | had | did / was | Presque personne n'avait remarqué le changement. | Hardly + had + sujet.
Only if you apply now ___ you get a discount. | will | you will / do | Ce n'est qu'en postulant maintenant que vous aurez un rabais. | Only if + inversion.
Not since the 1990s ___ the city seen such growth. | has | did / is | La ville n'a pas connu une telle croissance depuis les années 1990. | Not since + has + sujet.
Here ___ the bus! | comes | come / is coming | Voilà l'autobus ! | Here + verbe + sujet nominal.
Here ___ comes! | she | her / comes she | La voilà ! | Avec un pronom : pas d'inversion (here she comes).
Down ___ the rain. | came | come / did come | La pluie s'est mise à tomber à verse. | Adverbe de lieu + verbe + sujet (style narratif).
Nor ___ I ever seen anything like it. | have | did / do | Et je n'ai jamais rien vu de tel non plus. | Nor + inversion.
So beautiful ___ the view that we stayed for hours. | was | were / did | La vue était si belle que nous sommes restés des heures. | So + adjectif + inversion.
""",

"cliveesEnExercises": """
It was my sister ___ found the keys. | who | which / what | C'est ma sœur qui a trouvé les clés. | It was + personne + who.
It's the noise ___ bothers me, not the heat. | that | what / who | C'est le bruit qui me dérange, pas la chaleur. | It's + chose + that.
It was in Boston ___ we first met. | that | where it / which | C'est à Boston que nous nous sommes rencontrés. | It was + lieu + that.
It was last summer ___ she quit her job. | that | when it / which | C'est l'été dernier qu'elle a quitté son emploi. | It was + moment + that.
___ I really want is to travel. | What | That / Which | Ce que je veux vraiment, c'est voyager. | What + proposition + is.
What we need ___ more time. | is | are / it is | Ce dont nous avons besoin, c'est de plus de temps. | What … is.
What he did ___ to quit on the spot. | was | did / is | Ce qu'il a fait, c'est démissionner sur-le-champ. | What + sujet + did + was.
What I love about her ___ her honesty. | is | it is / are | Ce que j'aime chez elle, c'est son honnêteté. | What … is.
All I did ___ ask a question. | was | did / is | Je n'ai fait que poser une question. | All + sujet + did + was.
All you need ___ a good pair of shoes. | is | are / it is | Tout ce qu'il te faut, c'est une bonne paire de chaussures. | All … is.
The place ___ I feel most relaxed is the beach. | where | that it / what | L'endroit où je me sens le plus détendu, c'est la plage. | The place where … is.
The person ___ helped me most was my teacher. | who | which / what | La personne qui m'a le plus aidé, c'était mon enseignant. | The person who … was.
The reason ___ I called is to invite you. | why | what / which | La raison de mon appel, c'est de t'inviter. | The reason why … is.
The thing ___ worries me is the cost. | that | what / who | Ce qui m'inquiète, c'est le coût. | The thing that … is.
It wasn't until midnight ___ he came home. | that | when / which | Ce n'est qu'à minuit qu'il est rentré. | It wasn't until … that.
It's not what you say ___ matters, it's how you say it. | that | what / who | Ce n'est pas ce que tu dis qui compte, c'est la façon de le dire. | It's not … that.
Was it you ___ left the door open? | who | which / what | C'est toi qui as laissé la porte ouverte ? | Question clivée : Was it … who.
It's because of the snow ___ the school is closed. | that | why / what | C'est à cause de la neige que l'école est fermée. | It's because … that.
What surprised everyone ___ that he resigned. | was | did / it was | Ce qui a surpris tout le monde, c'est qu'il ait démissionné. | What … was that.
What happened ___ that the car broke down. | was | did / is that | Ce qui s'est passé, c'est que la voiture est tombée en panne. | What happened was that.
The last thing I want ___ to hurt you. | is | was it / are | La dernière chose que je veux, c'est te faire de la peine. | The last thing … is.
It was ___ who told me the news, not you. | she | hers / herself | C'est elle qui m'a annoncé la nouvelle, pas toi. | It was she (soutenu) ou It was her (courant) ; jamais hers.
It was the chef ___ the president thanked. | whom | which / what | C'est le chef que le président a remercié. | Complément, soutenu : whom (ou that).
What I don't understand ___ why she left. | is | was it / are | Ce que je ne comprends pas, c'est pourquoi elle est partie. | What … is.
The one thing I regret ___ not learning Spanish. | is | it is / are | La seule chose que je regrette, c'est de ne pas avoir appris l'espagnol. | The one thing … is.
It's Tom's car ___ is blocking the driveway. | that | what / where | C'est la voiture de Tom qui bloque l'allée. | It's … that.
Where I grew up ___ a small town in Maine. | was | were / it was | L'endroit où j'ai grandi, c'était une petite ville du Maine. | Where … was.
Why she left ___ still a mystery. | is | are / it is | La raison de son départ reste un mystère. | Proposition sujet + is.
It was only when I got home ___ I noticed the scratch. | that | when / which | Ce n'est qu'en rentrant que j'ai remarqué l'égratignure. | It was only when … that.
What we did next ___ call a taxi. | was | were / did | Ce que nous avons fait ensuite, c'est appeler un taxi. | What + did + was + verbe.
All that matters ___ that you're safe. | is | are / it is | Tout ce qui compte, c'est que tu sois sain et sauf. | All that matters is.
It was the hotel staff ___ called the ambulance. | who | which / what | C'est le personnel de l'hôtel qui a appelé l'ambulance. | It was … who.
It's you ___ I want to thank. | that | what / which | C'est toi que je veux remercier. | It's + personne + that (complément).
What makes this city special ___ its history. | is | are / it is | Ce qui rend cette ville spéciale, c'est son histoire. | What … is.
The only person ___ knows the code is my boss. | who | which / whose | La seule personne qui connaît le code, c'est mon patron. | The only person who.
What I'm trying to say ___ that I'm sorry. | is | are / it is | Ce que j'essaie de dire, c'est que je suis désolé. | What … is that.
It's not the money ___ I'm worried about. | that | what / who | Ce n'est pas l'argent qui m'inquiète. | It's not … that … about.
It was here ___ the Declaration was read aloud. | that | where it / which | C'est ici que la Déclaration a été lue à voix haute. | It was + lieu + that.
Something ___ annoys me is people who are always late. | that | what / who | Une chose qui m'agace, ce sont les gens toujours en retard. | Something that … is.
""",

"subjonctifEnExercises": """
I suggest that he ___ a doctor. | see | sees / saw | Je suggère qu'il voie un médecin. | Suggest that + verbe nu (subjonctif).
It's crucial that she ___ the truth. | know | knows / knew | Il est crucial qu'elle sache la vérité. | It's crucial that + verbe nu.
The teacher insisted that every student ___ the essay. | rewrite | rewrites / rewrote | L'enseignant a exigé que chaque élève réécrive la dissertation. | Insist that + verbe nu.
We request that all guests ___ by noon. | check out | checks out / checked out | Nous demandons que tous les clients libèrent la chambre avant midi. | Request that + verbe nu.
It's necessary that he ___ present. | be | is / was | Il est nécessaire qu'il soit présent. | Be (subjonctif de be).
They recommended that the bridge ___ closed. | be | is / was | Ils ont recommandé que le pont soit fermé. | Passif au subjonctif : be + participe.
The law requires that every driver ___ insurance. | have | has / had | La loi exige que chaque conducteur soit assuré. | Require that + verbe nu.
She asked that her name ___ mentioned. | not be | is not / wasn't | Elle a demandé que son nom ne soit pas mentionné. | Négation : not + verbe nu.
It's essential that we ___ late. | not be | aren't / won't be | Il est essentiel que nous ne soyons pas en retard. | Not be.
The doctor advised that she ___ smoking. | stop | stops / stopped | Le médecin a conseillé qu'elle arrête de fumer. | Advise that + verbe nu.
I propose that the meeting ___ postponed. | be | is / will be | Je propose que la réunion soit reportée. | Propose that + be + participe.
It's vital that the door ___ locked at night. | be | is / will be | Il est vital que la porte soit verrouillée la nuit. | Be + participe.
He demanded that the company ___ him. | refund | refunds / refunded | Il a exigé que l'entreprise le rembourse. | Demand that + verbe nu.
It's important that every child ___ breakfast. | eat | eats / ate | Il est important que chaque enfant déjeune. | Important that + verbe nu.
My mother insisted that I ___ home before ten. | be | was / am | Ma mère a exigé que je sois rentré avant dix heures. | Insist that + be.
If he ___ here, he would know what to do. | were | was being / is | S'il était là, il saurait quoi faire. | Subjonctif passé : were.
I wish she ___ a little more patient. | were | is / be | J'aimerais qu'elle soit un peu plus patiente. | Wish + were.
He acts as though he ___ the owner. | were | is being / be | Il se comporte comme s'il était le propriétaire. | As though + were.
It's high time you ___ a job. | found | find / will find | Il est grand temps que tu trouves un emploi. | It's high time + prétérit.
I'd rather you ___ me the truth. | told | tell / will tell | Je préférerais que tu me dises la vérité. | Would rather + sujet + prétérit.
Suppose he ___ the offer — what then? | refused | refuses / would refuse | Suppose qu'il refuse l'offre — et après ? | Suppose + prétérit.
God ___ America. | bless | blesses / blessed | Que Dieu bénisse l'Amérique. | Subjonctif figé : verbe nu.
Long ___ the king! | live | lives / lived | Vive le roi ! | Subjonctif figé.
___ it may, we must continue. | Be that as | Be as that / As be it | Quoi qu'il en soit, nous devons continuer. | Expression figée : Be that as it may.
Come what ___, I'll stand by you. | may | might / will | Quoi qu'il arrive, je serai à tes côtés. | Expression figée : Come what may.
So ___ it. | be | is / being | Ainsi soit-il. | Subjonctif figé.
The committee voted that the plan ___ adopted. | be | is / was | Le comité a voté l'adoption du plan. | Vote that + be + participe.
It's recommended that passengers ___ two hours early. | arrive | arrives / arrived | Il est recommandé aux passagers d'arriver deux heures à l'avance. | Recommended that + verbe nu.
It was suggested that we ___ the meeting online. | hold | held / holds | On a suggéré que nous tenions la réunion en ligne. | Suggested that + verbe nu, même au passé.
She urged that he ___ the contract carefully. | read | reads / had read | Elle a insisté pour qu'il lise attentivement le contrat. | Urge that + verbe nu.
It's imperative that the report ___ finished today. | be | is / will be | Il est impératif que le rapport soit terminé aujourd'hui. | Imperative that + be.
They asked that we ___ photographs inside. | not take | don't take / not to take | Ils ont demandé que nous ne prenions pas de photos à l'intérieur. | Not + verbe nu.
The coach suggested that she ___ more. | train | trains / to train | L'entraîneur a suggéré qu'elle s'entraîne davantage. | Suggest that + verbe nu.
It's urgent that he ___ the hospital. | call | calls / called | Il est urgent qu'il appelle l'hôpital. | Urgent that + verbe nu.
The board decided that the CEO ___ replaced. | be | is / was | Le conseil a décidé que le PDG serait remplacé. | Decide that + be + participe (formel).
I move that the meeting ___ adjourned. | be | is / will be | Je propose que la séance soit levée. | Formule de séance : move that + be.
It's advisable that guests ___ their valuables in the safe. | leave | leaves / left | Il est conseillé aux clients de laisser leurs objets de valeur dans le coffre. | Advisable that + verbe nu.
She insisted that the meeting ___ in person. | take place | takes place / took place | Elle a exigé que la réunion ait lieu en personne. | Insist that + verbe nu.
It's desirable that every employee ___ the training. | complete | completes / completed | Il est souhaitable que chaque employé suive la formation. | Desirable that + verbe nu.
He requested that he ___ disturbed. | not be | is not / wasn't | Il a demandé qu'on ne le dérange pas. | Not be + participe.
Whether he ___ guilty or not, he deserves a fair trial. | be | is being / were be | Qu'il soit coupable ou non, il mérite un procès équitable. | Subjonctif littéraire : whether he be (courant : is).
""",

"ellipseEnExercises": """
I'm hungry. — So ___ I. | am | do / have | J'ai faim. — Moi aussi. | So + auxiliaire de la phrase (am).
She likes sushi. — So ___ her husband. | does | is / has | Elle aime les sushis. — Son mari aussi. | Présent simple : does.
We went to the game. — So ___ we. | did | went / were | Nous sommes allés au match. — Nous aussi. | Passé simple : did.
He can't drive. — Neither ___ his brother. | can | does / can't | Il ne sait pas conduire. — Son frère non plus. | Neither + auxiliaire affirmatif.
I've never been to Paris. — Neither ___ I. | have | do / haven't | Je ne suis jamais allé à Paris. — Moi non plus. | Neither + have.
I don't eat meat. — ___ do I. | Neither | So / Either | Je ne mange pas de viande. — Moi non plus. | Neither do I.
I don't eat meat. — I don't ___. | either | neither / too | Je ne mange pas de viande. — Moi non plus. | I don't either.
I love this song. — Me ___. | too | either / neither | J'adore cette chanson. — Moi aussi. | Familier : me too.
I don't like spiders. — Me ___. | neither | too / so | Je n'aime pas les araignées. — Moi non plus. | Familier : me neither.
Are you coming tonight? — I think ___. | so | it / yes | Tu viens ce soir ? — Je crois que oui. | I think so.
Is it going to snow? — I hope ___! I hate snow. | not | no / don't | Va-t-il neiger ? — J'espère que non ! Je déteste la neige. | I hope not.
Did she pass? — I believe ___. | so | it / that | A-t-elle réussi ? — Je crois que oui. | I believe so.
Will they win? — I doubt ___. | it | so / that so | Vont-ils gagner ? — J'en doute. | Doubt it (pas « doubt so »).
Is he angry? — I'm afraid ___. | so | it / yes | Est-il fâché ? — J'en ai bien peur. | I'm afraid so.
Can you come? — I'd love ___, but I can't. | to | it / so | Tu peux venir ? — J'adorerais, mais je ne peux pas. | Love to (verbe sous-entendu).
You don't have to help, but you can if you want ___. | to | it / so | Tu n'es pas obligé d'aider, mais tu peux si tu veux. | Want to (verbe sous-entendu).
These shoes are too small. Do you have bigger ___? | ones | one / them | Ces chaussures sont trop petites. En avez-vous de plus grandes ? | Pluriel : ones.
I lost my umbrella, so I bought a new ___. | one | ones / it | J'ai perdu mon parapluie, alors j'en ai acheté un neuf. | Singulier : one.
Which jacket do you prefer? — The red ___. | one | ones / it | Quelle veste préfères-tu ? — La rouge. | The + adjectif + one.
She said she'd call, and she ___. | did | called / has | Elle a dit qu'elle appellerait, et elle l'a fait. | Did remplace le verbe.
He doesn't speak French, but his wife ___. | does | is / speaks it | Il ne parle pas français, mais sa femme oui. | Does remplace le verbe.
I haven't finished yet, but Tom ___. | has | did / is | Je n'ai pas encore fini, mais Tom oui. | Has (present perfect).
You look tired. — I ___. I didn't sleep. | am | do / look | Tu as l'air fatigué. — Je le suis. Je n'ai pas dormi. | I am (be sous-entendu).
I thought it would be easy, and it ___. | was | did / were | Je pensais que ce serait facile, et ça l'a été. | Was remplace « was easy ».
She's never been late, ___ she? | has | is / does | Elle n'a jamais été en retard, n'est-ce pas ? | Question-tag : auxiliaire positif après never.
You like coffee, ___ you? | don't | do / aren't | Tu aimes le café, n'est-ce pas ? | Question-tag négatif.
Let's go, ___ we? | shall | will / don't | Allons-y, d'accord ? | Let's … shall we?
Nobody called, ___ they? | did | didn't / do | Personne n'a appelé, n'est-ce pas ? | Nobody : tag positif avec they.
If you need a pen, I can lend you ___. | one | it / ones | Si tu as besoin d'un stylo, je peux t'en prêter un. | One remplace a pen.
I asked him to stop, but he ___. | wouldn't | won't / wouldn't it | Je lui ai demandé d'arrêter, mais il n'a pas voulu. | Ellipse après le modal : he wouldn't (stop).
Some people like winter; others ___. | don't | aren't / doesn't | Certains aiment l'hiver, d'autres non. | Don't remplace « don't like winter ».
I'd love to help. — So ___ I. | would | do / am | J'adorerais aider. — Moi aussi. | So + would.
He won't come. — Neither ___ she. | will | won't / does | Il ne viendra pas. — Elle non plus. | Neither + will.
She can't come, and ___ can I. | neither | either / so | Elle ne peut pas venir, et moi non plus. | And neither can I.
I'll call you if I can, but I may not be able ___. | to | it / so | Je t'appellerai si je peux, mais je n'en serai peut-être pas capable. | Able to (verbe sous-entendu).
Have you finished? — Not ___. | yet | still / already | As-tu fini ? — Pas encore. | Not yet.
Do you want the large pizza or the small ___? | one | ones / it | Tu veux la grande pizza ou la petite ? | One remplace pizza.
He's taller than his father ___. | is | does / has | Il est plus grand que son père. | Comparaison : auxiliaire repris (is).
She runs faster than I ___. | do | am / run it | Elle court plus vite que moi. | Comparaison : do reprend « run ».
""",
**SUITE,
}
