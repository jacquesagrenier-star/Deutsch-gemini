# -*- coding: utf-8 -*-
"""Les fiches de grammaire C1 de l'anglais, en francais, et leurs series.
Meme format que grammaire_a2.py. SOURCE : on corrige ici, puis
python anglais/outils/construire.py.
"""

FICHES = [
{
"id": "inversion", "titre": "L'inversion : Never have I…", "resume": "Mettre en relief par un adverbe négatif",
"regle": "Dans un registre soutenu, quand une phrase commence par une expression <b>négative ou restrictive</b>, l'auxiliaire passe <b>avant le sujet</b>, comme dans une question : <b>Never have I seen such a mess</b> (jamais je n'ai vu…). Les déclencheurs : <b>never, rarely, seldom, hardly… when, no sooner… than, not only… but also, only then, only after, under no circumstances, at no time, little</b>. Sans auxiliaire, on fait appel à <b>do / does / did</b> : <b>Rarely does he complain</b>.",
"tableau": [
 ["Never / Rarely + auxiliaire + sujet", "jamais / rarement", "Rarely do we see snow in April."],
 ["Not only + aux. + sujet…, but also", "non seulement… mais aussi", "Not only did she win, but she also broke the record."],
 ["Hardly had + sujet + participe… when", "à peine… que", "Hardly had I arrived when it started to rain."],
 ["No sooner had… than", "à peine… que", "No sooner had we left than the phone rang."],
 ["Only then / Only after + aux. + sujet", "ce n'est qu'alors / qu'après", "Only then did I understand."],
 ["Under no circumstances + aux. + sujet", "en aucun cas", "Under no circumstances should you open this door."],
],
"exemples": [
 ["Never have I tasted such good lobster.", "Jamais je n'ai goûté un homard aussi bon."],
 ["Little did they know what was coming.", "Ils étaient loin de se douter de ce qui allait arriver."],
 ["Only after the meeting did she realize her mistake.", "Ce n'est qu'après la réunion qu'elle a compris son erreur."],
],
"attention": "L'inversion appartient à l'écrit soigné et aux discours. À l'oral courant, on dit simplement <b>I've never seen such a mess</b>. Et <b>Only then</b> déclenche l'inversion, pas <b>then</b> seul.",
"serie": "inversionEnExercises", "kicker": "L'inversion",
"questions": """
Never ___ I seen such a beautiful sunset. | have | I have / had I | Jamais je n'ai vu un aussi beau coucher de soleil. | Never en tête → auxiliaire avant le sujet : have I.
Rarely ___ he complain about anything. | does | he does / do | Il se plaint rarement de quoi que ce soit. | Sans auxiliaire → does + sujet + verbe nu.
Not only ___ she win, but she also broke the record. | did | she did / has | Non seulement elle a gagné, mais elle a aussi battu le record. | Not only + did + sujet.
Hardly had I sat down ___ the phone rang. | when | than / that | À peine m'étais-je assis que le téléphone a sonné. | Hardly… when.
No sooner had we left ___ it started to rain. | than | when / that | À peine étions-nous partis qu'il s'est mis à pleuvoir. | No sooner… than.
Only then ___ I understand what she meant. | did | I did / do | Ce n'est qu'alors que j'ai compris ce qu'elle voulait dire. | Only then + did + sujet.
Under no circumstances ___ you open this door. | should | you should / you must | Vous ne devez en aucun cas ouvrir cette porte. | Under no circumstances + aux. + sujet.
Little ___ they know what was waiting for them. | did | they did / had they | Ils étaient loin de se douter de ce qui les attendait. | Little + did + sujet.
Seldom ___ we eaten such a delicious meal. | have | we have / did we | Rarement avons-nous mangé un repas aussi délicieux. | Seldom + have + sujet.
At no time ___ the passengers in danger. | were | they were / did | À aucun moment les passagers n'ont été en danger. | At no time + were + sujet.
Only after the exam ___ she relax. | did | she did / she | Ce n'est qu'après l'examen qu'elle s'est détendue. | Only after + did + sujet.
___ I known, I would have come sooner. | Had | If / Did | Si j'avais su, je serais venu plus tôt. | L'inversion remplace if : Had I known.
"""
},
{
"id": "clivees", "titre": "Les phrases clivées : It was… who, What I need is…", "resume": "Mettre un élément en relief",
"regle": "Pour souligner un élément, l'anglais coupe la phrase en deux. <b>It is / It was + élément + who / that…</b> : <b>It was Anna who called</b> (c'est Anna qui a appelé), <b>It's the price that worries me</b>. <b>What + sujet + verbe + is / was…</b> : <b>What I need is a vacation</b> (ce dont j'ai besoin, c'est de vacances). Variantes : <b>All I want is…</b> (tout ce que je veux, c'est…), <b>The reason why… is that…</b>, <b>The thing is…</b>.",
"tableau": [
 ["It is / was + élément + who / that", "c'est… qui / que", "It was in Boston that they met."],
 ["What + phrase + is / was", "ce que…, c'est", "What I love is the ocean."],
 ["What + sujet + do + is + verbe", "ce que fait…, c'est", "What she did was call the police."],
 ["All + sujet + verbe + is", "tout ce que…, c'est", "All I want is some sleep."],
 ["The reason (why)… is that", "si…, c'est que", "The reason I'm late is that the bus broke down."],
],
"exemples": [
 ["It was my sister who told me.", "C'est ma sœur qui me l'a dit."],
 ["What surprised me was his calm.", "Ce qui m'a surpris, c'est son calme."],
 ["All we need now is a little luck.", "Tout ce qu'il nous faut maintenant, c'est un peu de chance."],
],
"attention": "Le français « c'est… que » est bien plus fréquent que son équivalent anglais : à l'oral, l'anglais met souvent l'accent avec la <b>voix</b> plutôt qu'avec la structure (<b>ANNA called</b>).",
"serie": "cliveesEnExercises", "kicker": "Phrases clivées",
"questions": """
It was Anna ___ called you. | who | which / what | C'est Anna qui t'a appelé. | Une personne → who (ou that).
It's the price ___ worries me. | that | what / who | C'est le prix qui m'inquiète. | Une chose → that.
___ I need is a long vacation. | What | That / Which | Ce dont j'ai besoin, ce sont de longues vacances. | Ce que / ce dont… = What.
All I want ___ some peace and quiet. | is | are / it's | Tout ce que je veux, c'est un peu de calme. | All… is.
It was in 2015 ___ they moved to Boston. | that | when it / which | C'est en 2015 qu'ils ont emménagé à Boston. | It was + moment + that.
What she did ___ call the police. | was | did / is that | Ce qu'elle a fait, c'est appeler la police. | What + sujet + did + was + verbe.
The reason I'm late ___ that the bus broke down. | is | it's / because | Si je suis en retard, c'est que le bus est tombé en panne. | The reason… is that.
What surprised me ___ his calm. | was | were / it was | Ce qui m'a surpris, c'est son calme. | What + verbe + was.
It wasn't me ___ broke the window! | who | which / what | Ce n'est pas moi qui ai cassé la vitre ! | It wasn't… who.
What I like about Boston ___ its old streets. | is | are / it is | Ce que j'aime à Boston, ce sont ses vieilles rues. | Le verbe s'accorde avec What : is.
It's not money ___ makes people happy. | that | what / who | Ce n'est pas l'argent qui rend les gens heureux. | It's not… that.
The thing ___, I don't have time. | is | it's / was that | Le problème, c'est que je n'ai pas le temps. | The thing is… = le problème, c'est que.
"""
},
{
"id": "subjonctif", "titre": "Le subjonctif anglais", "resume": "I suggest that he be, It's vital that she leave",
"regle": "L'anglais a un <b>subjonctif</b> discret : le <b>verbe nu</b>, sans -s, à toutes les personnes. On le trouve après des verbes et adjectifs d'exigence ou de recommandation, surtout à l'écrit soutenu et en anglais américain : <b>suggest, recommend, insist, demand, require, propose</b> et <b>it is essential / vital / important / necessary that</b>. <b>The doctor recommends that he rest</b> (pas <i>rests</i>). Avec be : <b>be</b> partout : <b>It's vital that everyone be on time</b>. Le britannique dit souvent <b>should</b> : <b>that he should rest</b>.",
"tableau": [
 ["suggest / recommend that + verbe nu", "proposer / recommander que", "I suggest that she call him."],
 ["insist / demand that + verbe nu", "exiger que", "They demanded that he leave."],
 ["it's essential / vital that + verbe nu", "il est essentiel que", "It's essential that you be there."],
 ["that + sujet + not + verbe", "négation", "I recommend that he not drive."],
 ["were (irréel)", "if I were, as if it were", "If I were you…"],
 ["formules figées", "subjonctif résiduel", "God bless America. Long live the king."],
],
"exemples": [
 ["The judge ordered that the man be released.", "Le juge a ordonné que l'homme soit libéré."],
 ["It's important that she take her medicine every day.", "Il est important qu'elle prenne son médicament tous les jours."],
 ["We insist that he apologize.", "Nous exigeons qu'il s'excuse."],
],
"attention": "La forme ressemble à une faute (<b>she take</b>, <b>he be</b>) : c'est voulu. Le français a un subjonctif bien plus large ; l'anglais ne l'emploie qu'après ces mots d'exigence.",
"serie": "subjonctifEnExercises", "kicker": "Le subjonctif",
"questions": """
The doctor recommends that he ___ for a week. | rest | rests / rested | Le médecin recommande qu'il se repose une semaine. | Recommend that + verbe nu, sans -s.
It's essential that everyone ___ on time. | be | is / are | Il est essentiel que tout le monde soit à l'heure. | It's essential that + be.
They demanded that the manager ___. | resign | resigns / resigned | Ils ont exigé que le directeur démissionne. | Demand that + verbe nu.
I suggest that she ___ him tomorrow. | call | calls / will call | Je propose qu'elle l'appelle demain. | Suggest that + verbe nu.
It's vital that the patient ___ alone. | not be left | isn't left / not is left | Il est vital que le patient ne soit pas laissé seul. | Négation : not + be + participe.
The judge ordered that the prisoner ___ released. | be | is / was | Le juge a ordonné que le prisonnier soit libéré. | Order that + be.
We insist that he ___. | apologize | apologizes / apologized | Nous exigeons qu'il s'excuse. | Insist that + verbe nu.
It's important that she ___ her medicine. | take | takes / taking | Il est important qu'elle prenne son médicament. | Verbe nu : take.
I recommend that you ___ drive tonight. | not | don't / no | Je vous recommande de ne pas conduire ce soir. | that + you + not + verbe.
If I ___ you, I'd accept the offer. | were | am / was being | Si j'étais vous, j'accepterais l'offre. | Irréel : were.
The rules require that each member ___ a fee. | pay | pays / paid | Le règlement exige que chaque membre paie une cotisation. | Require that + verbe nu.
She speaks as if she ___ the boss. | were | is / be | Elle parle comme si elle était la patronne. | As if + were (irréel).
"""
},
{
"id": "ellipse", "titre": "Ellipse et substitution : so do I, I hope so", "resume": "Ne pas répéter : so, neither, do, one",
"regle": "L'anglais évite de répéter. <b>So + auxiliaire + sujet</b> = moi aussi (affirmation) : <b>I love jazz. — So do I.</b> <b>Neither / Nor + auxiliaire + sujet</b> = moi non plus : <b>I can't swim. — Neither can I.</b> <b>So</b> et <b>not</b> remplacent une proposition après think, hope, expect, suppose, be afraid : <b>I hope so / I hope not</b>, <b>I don't think so</b>. <b>One / ones</b> remplace un nom : <b>the blue one</b>. L'auxiliaire seul reprend le verbe : <b>She said she'd come, and she did.</b>",
"tableau": [
 ["So + aux. + sujet", "moi aussi", "I'm tired. — So am I."],
 ["Neither / Nor + aux. + sujet", "moi non plus", "I didn't go. — Neither did I."],
 ["I think so · I hope not", "je pense que oui · j'espère que non", "Will it rain? — I hope not."],
 ["one · ones", "celui, celle, ceux", "I prefer the red one."],
 ["auxiliaire seul", "reprise du verbe", "He said he'd help, and he did."],
 ["to (sans le verbe)", "reprise d'un infinitif", "I wanted to go, but I didn't have time to."],
],
"exemples": [
 ["I've never been to Maine. — Neither have I.", "Je ne suis jamais allé dans le Maine. — Moi non plus."],
 ["Is the store open? — I'm afraid not.", "Le magasin est ouvert ? — J'ai bien peur que non."],
 ["These shoes are too small. Do you have bigger ones?", "Ces chaussures sont trop petites. Vous en avez de plus grandes ?"],
],
"attention": "L'auxiliaire suit le temps et la personne de la phrase d'origine : <b>She has finished. — So have I.</b> / <b>He went. — So did I.</b> Et l'oral familier dit volontiers <b>Me too</b> et <b>Me neither</b>.",
"serie": "ellipseEnExercises", "kicker": "Ellipse et substitution",
"questions": """
I love jazz. — So ___ I. | do | am / have | J'adore le jazz. — Moi aussi. | Présent simple → do.
I can't swim. — Neither ___ I. | can | do / am | Je ne sais pas nager. — Moi non plus. | Même auxiliaire : can.
She's tired. — So ___ I. | am | do / is | Elle est fatiguée. — Moi aussi. | Be → am.
I didn't go to the party. — Neither ___ I. | did | do / was | Je ne suis pas allé à la fête. — Moi non plus. | Prétérit → did.
Will it rain tomorrow? — I hope ___. | not | no / don't | Il va pleuvoir demain ? — J'espère que non. | I hope not = j'espère que non.
Is he coming? — I think ___. | so | it / yes | Il vient ? — Je pense que oui. | I think so.
I don't like this shirt. Can I see the blue ___? | one | ones / it | Je n'aime pas cette chemise. Je peux voir la bleue ? | Un nom singulier → one.
These apples are bad. Give me some fresh ___. | ones | one / them | Ces pommes sont abîmées. Donne-m'en des fraîches. | Pluriel → ones.
He said he would help us, and he ___. | did | helped us / was | Il a dit qu'il nous aiderait, et il l'a fait. | L'auxiliaire seul reprend le verbe.
I've been to Chicago. — So ___ I. | have | did / am | Je suis allé à Chicago. — Moi aussi. | Present perfect → have.
I wanted to call you, but I didn't have time ___. | to | to it / it | Je voulais t'appeler, mais je n'ai pas eu le temps. | To reprend l'infinitif.
Is the museum open on Mondays? — I'm afraid ___. | not | no / don't | Le musée est ouvert le lundi ? — J'ai bien peur que non. | I'm afraid not.
"""
},
{
"id": "participiales", "titre": "Les participiales : Having finished…", "resume": "Réduire une subordonnée à un participe",
"regle": "Une proposition peut se réduire à un <b>participe</b> quand elle a le même sujet que la principale. <b>-ing</b> pour deux actions simultanées ou une cause : <b>Feeling tired, she went to bed</b> (comme elle était fatiguée…). <b>Having + participe</b> pour une action antérieure : <b>Having finished his work, he went home</b>. <b>Participe passé</b> pour un sens passif : <b>Built in 1800, the house needs repairs</b>. On garde parfois la conjonction : <b>While waiting…</b>, <b>After leaving…</b>, <b>When asked…</b>",
"tableau": [
 ["-ing, …", "en faisant, comme…", "Walking home, I met Tom."],
 ["Having + participe, …", "après avoir…", "Having eaten, we left."],
 ["Participe passé, …", "sens passif", "Written in 1850, the book is still popular."],
 ["Not + -ing, …", "ne… pas, comme… ne… pas", "Not knowing the way, I asked."],
 ["While / After / Before + -ing", "conjonction + participe", "Before leaving, lock the door."],
 ["When asked / If needed", "quand on lui demande / si besoin", "When asked, he refused to answer."],
],
"exemples": [
 ["Having lived in Boston for years, she knows every street.", "Ayant vécu à Boston pendant des années, elle connaît chaque rue."],
 ["Not knowing what to say, he stayed silent.", "Ne sachant que dire, il est resté silencieux."],
 ["Founded in 1636, Harvard is the oldest university in the US.", "Fondée en 1636, Harvard est la plus ancienne université des États-Unis."],
],
"attention": "Le participe doit avoir le <b>même sujet</b> que la principale. <i>Walking down the street, the rain started</i> est faux (la pluie ne marchait pas) : <b>Walking down the street, I got caught in the rain</b>.",
"serie": "participialesEnExercises", "kicker": "Participiales",
"questions": """
___ his work, he went home. | Having finished | Finishing had / Finished having | Après avoir fini son travail, il est rentré chez lui. | Action antérieure → Having + participe.
___ tired, she went to bed early. | Feeling | Felt / Having felt being | Comme elle était fatiguée, elle s'est couchée tôt. | Cause, simultanée → -ing.
___ in 1636, Harvard is the oldest university in the US. | Founded | Founding / Having founded | Fondée en 1636, Harvard est la plus ancienne université américaine. | Sens passif → participe passé.
___ the way, I asked a police officer. | Not knowing | Knowing not / Don't knowing | Comme je ne connaissais pas le chemin, j'ai demandé à un policier. | Négation : Not + -ing.
Before ___, lock the door. | leaving | leave / to leave | Avant de partir, ferme la porte à clé. | Before + -ing.
___ home, I met an old friend. | Walking | Walked / Having walk | En rentrant à pied, j'ai croisé un vieil ami. | Simultané → -ing.
When ___, he refused to comment. | asked | asking / ask | Quand on l'a interrogé, il a refusé de commenter. | When + participe passé (sens passif).
___ by the noise, the baby started crying. | Woken | Waking / Having woke | Réveillé par le bruit, le bébé s'est mis à pleurer. | Passif → participe passé.
___ seen the movie before, I knew the ending. | Having | Had / Being | Comme j'avais déjà vu le film, je connaissais la fin. | Having + participe.
While ___ for the bus, she read the news. | waiting | waited / wait | En attendant le bus, elle a lu les nouvelles. | While + -ing.
___ carefully, the plan could work. | Done | Doing / Having do | Bien exécuté, le plan pourrait marcher. | Sens passif → participe passé.
After ___ the contract, they celebrated. | signing | sign / signed to | Après avoir signé le contrat, ils ont fêté ça. | After + -ing.
"""
},
{
"id": "modaux-nuances", "titre": "Les nuances des modaux", "resume": "had better, would rather, needn't have, be supposed to",
"regle": "Au-delà des modaux de base : <b>had better</b> (+ verbe nu) = on ferait mieux de, avec un risque à la clé : <b>You'd better hurry</b>. <b>Would rather</b> (+ verbe nu) = préférer : <b>I'd rather stay home</b> ; avec un autre sujet, prétérit : <b>I'd rather you didn't smoke</b>. <b>Be supposed to</b> = être censé : <b>You're supposed to wear a helmet</b>. <b>Needn't have</b> (inutile mais fait) ≠ <b>didn't need to</b> (pas nécessaire, pas fait). <b>May / might as well</b> = autant (faute de mieux) : <b>We might as well walk</b>.",
"tableau": [
 ["had better ('d better) + verbe nu", "ferait mieux de", "You'd better not be late."],
 ["would rather + verbe nu", "préférerait", "I'd rather walk."],
 ["would rather + sujet + prétérit", "préférerait que", "I'd rather you stayed."],
 ["be supposed to + verbe", "être censé", "The train is supposed to arrive at six."],
 ["needn't have + participe", "ce n'était pas la peine (fait)", "You needn't have waited."],
 ["might as well + verbe", "autant (faute de mieux)", "It's late; we might as well stay."],
],
"exemples": [
 ["We'd better leave now, or we'll miss the train.", "On ferait mieux de partir maintenant, sinon on va rater le train."],
 ["I'd rather you didn't tell anyone.", "Je préférerais que tu n'en parles à personne."],
 ["You're not supposed to park here.", "Tu n'es pas censé te garer ici."],
],
"attention": "<b>Had better</b> parle du présent ou de l'avenir malgré son « had » : <b>You'd better go now</b>. Sa négation est <b>had better not</b> : <i>hadn't better</i> est rare.",
"serie": "modauxNuancesEnExercises", "kicker": "Nuances des modaux",
"questions": """
You'd better ___ now, or you'll miss the bus. | leave | to leave / leaving | Tu ferais mieux de partir maintenant, sinon tu vas rater le bus. | Had better + verbe nu.
I'd rather ___ home tonight. | stay | to stay / staying | Je préférerais rester à la maison ce soir. | Would rather + verbe nu.
I'd rather you ___ smoke in here. | didn't | don't / won't | Je préférerais que tu ne fumes pas ici. | Autre sujet → prétérit.
You're ___ to wear a helmet on the bike. | supposed | suppose / supposing | Tu es censé porter un casque à vélo. | Be supposed to.
You ___ have brought a gift, but thank you! | needn't | mustn't / couldn't | Ce n'était pas la peine d'apporter un cadeau, mais merci ! | Fait inutilement → needn't have.
I ___ to work yesterday, so I slept in. | didn't need | needn't have / mustn't | Je n'avais pas besoin de travailler hier, alors j'ai fait la grasse matinée. | Pas nécessaire (et pas fait) → didn't need to.
The bus is late. We might ___ well walk. | as | so / also | Le bus est en retard. Autant y aller à pied. | Might as well.
You'd better ___ tell her. She'll be upset. | not | don't / not to | Tu ferais mieux de ne pas lui dire. Elle sera contrariée. | Had better not + verbe.
The meeting was ___ to start at nine. | supposed | suppose / supposing | La réunion était censée commencer à neuf heures. | Was supposed to.
Would you rather ___ tea or coffee? | have | to have / having | Tu préfères du thé ou du café ? | Would rather + verbe nu.
We ___ better hurry — the store closes soon. | had | have / would | On ferait mieux de se dépêcher, le magasin ferme bientôt. | Had better.
He's not ___ to know about the party. | supposed | suppose / supposing | Il n'est pas censé être au courant de la fête. | Not supposed to.
"""
},
{
"id": "emphase", "titre": "L'emphase : do, such, so", "resume": "I do like it! — It was such a good day",
"regle": "<b>Do / does / did</b> devant le verbe insiste dans une affirmation : <b>I do like your hat!</b> (j'adore vraiment), <b>She did call, I promise</b>. <b>So + adjectif / adverbe</b> et <b>such (a) + adjectif + nom</b> renforcent : <b>It was so cold</b>, <b>It was such a cold day</b>, <b>such nice people</b>. Avec <b>that</b>, ils introduisent une conséquence : <b>It was so late that we took a taxi</b>. Autres renforts : <b>the very</b> (le même, celui-là précisément), <b>whatever / at all</b> dans la négation (<b>no money whatsoever</b>), <b>by far</b> devant un superlatif.",
"tableau": [
 ["do / does / did + verbe", "insistance", "I did lock the door!"],
 ["so + adjectif", "si, tellement", "The view is so beautiful."],
 ["such a + adjectif + nom", "un(e) tellement…", "It's such a beautiful view."],
 ["such + adjectif + nom pluriel", "de tels…", "They're such nice people."],
 ["so… that · such… that", "si… que", "She was so tired that she fell asleep."],
 ["by far the + superlatif", "de loin le…", "It's by far the best pizza in town."],
],
"exemples": [
 ["I do hope you can come.", "J'espère vraiment que tu pourras venir."],
 ["It was such a long flight that I slept the whole time.", "C'était un vol si long que j'ai dormi tout du long."],
 ["That's the very house where I was born.", "C'est la maison même où je suis né."],
],
"attention": "<b>So</b> va avec un adjectif seul (<b>so nice</b>), <b>such</b> avec un nom (<b>such a nice day</b>). <i>So a nice day</i> et <i>such nice</i> (sans nom) sont faux.",
"serie": "emphaseEnExercises", "kicker": "L'emphase",
"questions": """
I ___ like your new haircut! | do | am / does | J'aime vraiment ta nouvelle coupe ! | Insistance → do + verbe nu.
She ___ call you yesterday — check your phone! | did | has / was | Elle t'a bien appelé hier, regarde ton téléphone ! | Insistance au passé → did + verbe nu.
It was ___ a beautiful day. | such | so / so much | C'était une si belle journée. | Such a + adjectif + nom.
The view is ___ beautiful. | so | such / such a | La vue est si belle. | So + adjectif seul.
They're ___ nice people. | such | so / such a | Ce sont des gens si gentils. | Such + adjectif + nom pluriel.
It was so late ___ we took a taxi. | that | so / than | Il était si tard que nous avons pris un taxi. | So… that.
It's ___ the best restaurant in town. | by far | far by / much more | C'est de loin le meilleur restaurant de la ville. | By far + superlatif.
He ___ say he would come. I heard him. | did | was / has | Il a bien dit qu'il viendrait. Je l'ai entendu. | Insistance : did say.
There's no reason ___ to panic. | whatsoever | at all whatsoever / whatever ever | Il n'y a absolument aucune raison de paniquer. | Renfort négatif → whatsoever.
That's the ___ book I was looking for! | very | same very / very same the | C'est exactement le livre que je cherchais ! | The very = celui-là même.
She was ___ tired that she fell asleep on the train. | so | such / such a | Elle était si fatiguée qu'elle s'est endormie dans le train. | So + adjectif + that.
It was ___ good food that we came back the next day. | such | so / such a | La nourriture était si bonne que nous sommes revenus le lendemain. | Such + nom indénombrable.
"""
},
{
"id": "registre", "titre": "Le registre : formel ou courant", "resume": "purchase ou buy, require ou need",
"regle": "L'anglais a souvent <b>deux mots</b> pour la même idée : un mot d'origine latine ou française, <b>formel</b> (lettres, administration, écrits), et un verbe simple ou un phrasal verb, <b>courant</b> (conversation). <b>Purchase / buy</b>, <b>require / need</b>, <b>commence / start</b>, <b>inquire / ask</b>, <b>assist / help</b>, <b>obtain / get</b>, <b>reside / live</b>, <b>postpone / put off</b>, <b>tolerate / put up with</b>. Le francophone a tendance à choisir le mot latin, qui sonne trop raide à l'oral.",
"tableau": [
 ["purchase · buy", "acheter (formel · courant)", "Tickets may be purchased online. / I bought a ticket."],
 ["require · need", "avoir besoin de", "Applicants require a visa. / I need a visa."],
 ["commence · start", "commencer", "The ceremony will commence at noon."],
 ["inquire · ask", "se renseigner, demander", "I'm writing to inquire about the position."],
 ["postpone · put off", "reporter", "The meeting was postponed. / Let's put it off."],
 ["reside · live", "résider, habiter", "Applicants must reside in Massachusetts."],
],
"exemples": [
 ["We regret to inform you that the flight has been canceled.", "Nous avons le regret de vous informer que le vol a été annulé."],
 ["Sorry, the flight's been canceled.", "Désolé, le vol est annulé."],
 ["Please do not hesitate to contact us.", "N'hésitez pas à nous contacter."],
],
"attention": "Entre amis, <b>I'll assist you</b> ou <b>I wish to purchase</b> sonne comme un formulaire. À l'oral, préférez <b>I'll help you</b>, <b>I want to buy</b>. À l'inverse, une lettre de motivation évite <b>get</b> et <b>a lot of</b>.",
"serie": "registreEnExercises", "kicker": "Registre",
"questions": """
(Formel) Tickets may be ___ at the box office. | purchased | bought up / got | (Formel) Les billets peuvent être achetés à la billetterie. | Formel : purchase.
(Courant) I ___ a new phone yesterday. | bought | purchased / acquired | (Courant) Je me suis acheté un nouveau téléphone hier. | Courant : buy.
(Formel) All visitors are ___ to sign in. | required | needed / got | (Formel) Tous les visiteurs doivent signer le registre. | Formel : be required to.
(Formel) The ceremony will ___ at noon. | commence | kick off / start up | (Formel) La cérémonie commencera à midi. | Formel : commence.
(Formel) I am writing to ___ about the position. | inquire | ask around / check out | (Formel) Je vous écris pour me renseigner sur le poste. | Formel : inquire.
(Courant) Let's ___ the meeting until Friday. | put off | postpone the / defer of | (Courant) Reportons la réunion à vendredi. | Courant : put off.
(Formel) Applicants must ___ in Massachusetts. | reside | live up / stay at | (Formel) Les candidats doivent résider dans le Massachusetts. | Formel : reside.
(Courant) Can you ___ me with these boxes? | help | assist / aid | (Courant) Tu peux m'aider avec ces cartons ? | Courant : help.
(Formel) Please do not ___ to contact us. | hesitate | wait / stop | (Formel) N'hésitez pas à nous contacter. | Formule de lettre.
(Courant) I can't ___ this noise anymore. | put up with | tolerate of / endure with | (Courant) Je ne supporte plus ce bruit. | Courant : put up with.
(Formel) We ___ to inform you that your order is delayed. | regret | are sorry / feel bad | (Formel) Nous avons le regret de vous informer que votre commande est retardée. | Formel : we regret to inform you.
(Formel) Further information can be ___ from the website. | obtained | gotten / had | (Formel) Vous trouverez plus d'informations sur le site. | Formel : obtain.
"""
},
{
"id": "faux-amis-c1", "titre": "Les faux amis (3)", "resume": "consistent, eventual, susceptible, deception…",
"regle": "Les faux amis du niveau avancé, qui piègent même les bons élèves. <b>Consistent</b> = constant, cohérent (consistant = <b>substantial</b>). <b>Susceptible</b> = sensible, prédisposé (susceptible = <b>touchy</b>). <b>Deception</b> = tromperie (déception = <b>disappointment</b>). <b>Abusive</b> = injurieux, violent (abusif = <b>excessive, unfair</b>). <b>Formidable</b> = redoutable (formidable = <b>great, terrific</b>). <b>Candid</b> = franc (candide = <b>naive</b>). <b>Contemplate</b> = envisager (contempler = <b>gaze at</b>). <b>Exhaustive</b> = complet, exhaustif ; <b>exhausting</b> = épuisant.",
"tableau": [
 ["consistent", "constant, cohérent ≠ consistant (substantial)", "Her work is very consistent."],
 ["susceptible to", "sensible à, prédisposé ≠ susceptible (touchy)", "Children are susceptible to colds."],
 ["deception", "tromperie ≠ déception (disappointment)", "The scam was based on deception."],
 ["formidable", "redoutable ≠ formidable (terrific)", "She's a formidable opponent."],
 ["candid", "franc ≠ candide (naive)", "Thanks for your candid opinion."],
 ["contemplate", "envisager ≠ contempler (gaze at)", "They're contemplating a move to Maine."],
],
"exemples": [
 ["He's very touchy about his age.", "Il est très susceptible quand on parle de son âge."],
 ["The meal was terrific!", "Le repas était formidable !"],
 ["To my great disappointment, the concert was canceled.", "À ma grande déception, le concert a été annulé."],
],
"attention": "D'autres encore : <b>to be confident</b> (être sûr de soi ≠ avoir confiance en quelqu'un : <b>trust</b>), <b>delay</b> (retard ≠ délai : <b>deadline</b>), <b>issue</b> (problème, question ≠ issue : <b>outcome</b>), <b>agenda</b> (ordre du jour ≠ agenda : <b>planner</b>).",
"serie": "fauxAmisC1EnExercises", "kicker": "Faux amis (3)",
"questions": """
Don't joke about his weight — he's very ___. | touchy | susceptible / sensible | Ne plaisante pas sur son poids, il est très susceptible. | Susceptible (français) = touchy.
Older people are more ___ to the flu. | susceptible | touchy / sensitive of | Les personnes âgées sont plus sensibles à la grippe. | Susceptible to = prédisposé à.
To my great ___, the concert was canceled. | disappointment | deception / delusion | À ma grande déception, le concert a été annulé. | Déception = disappointment.
The fraud was based on ___. | deception | disappointment / delusion | La fraude reposait sur la tromperie. | Deception = tromperie.
The meal was ___! I loved it. | terrific | formidable / fearsome | Le repas était formidable ! J'ai adoré. | Formidable (français) = terrific, great.
She's a ___ opponent; nobody beats her easily. | formidable | terrific / great fun | C'est une adversaire redoutable ; personne ne la bat facilement. | Formidable = redoutable.
Thank you for your ___ answer; I appreciate the honesty. | candid | naive / candide | Merci pour ta réponse franche, j'apprécie l'honnêteté. | Candid = franc.
They're ___ moving to the countryside. | contemplating | gazing at / admiring | Ils envisagent de s'installer à la campagne. | Contemplate = envisager.
His results are very ___: always good. | consistent | substantial / consisting | Ses résultats sont très réguliers : toujours bons. | Consistent = constant.
We had a ___ breakfast before the hike. | substantial | consistent / consisting | Nous avons pris un petit-déjeuner consistant avant la randonnée. | Consistant = substantial.
What's the ___ for the report? Friday? | deadline | delay / term | Quel est le délai pour le rapport ? Vendredi ? | Délai (date limite) = deadline.
I ___ my doctor completely. | trust | am confident / confide | J'ai entièrement confiance en mon médecin. | Avoir confiance en = trust.
"""
},
]
