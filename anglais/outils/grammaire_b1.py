# -*- coding: utf-8 -*-
"""Les fiches de grammaire B1 de l'anglais, en francais, et leurs series.
Meme format que grammaire_a2.py. SOURCE : on corrige ici, puis
python anglais/outils/construire.py.
"""

FICHES = [
{
"id": "pp-continu", "titre": "Le present perfect continu", "resume": "I've been waiting for an hour — l'action qui dure jusqu'à maintenant",
"regle": "<b>Have / has been + verbe en -ing</b> : <b>I've been working</b>, <b>she's been crying</b>. Il insiste sur la <b>durée</b> d'une activité commencée dans le passé et qui continue, ou qui vient juste de s'arrêter et dont on voit les traces (<b>You're wet! — I've been running.</b>). Avec <b>for</b> et <b>since</b>, il traduit le présent français « depuis » : <b>I've been learning English for two years</b>. Le present perfect simple, lui, compte un <b>résultat</b> : <b>I've read three books</b> (et pas <i>I've been reading three books</i>).",
"tableau": [
 ["have / has been + -ing", "action qui dure jusqu'à maintenant", "We've been waiting for ages."],
 ["How long have you been + -ing?", "depuis combien de temps… ?", "How long have you been living here?"],
 ["haven't been + -ing", "négation", "I haven't been sleeping well."],
 ["durée → continu", "combien de temps", "I've been cleaning all morning."],
 ["résultat, nombre → simple", "combien, quoi", "I've cleaned three rooms."],
],
"exemples": [
 ["It's been raining since this morning.", "Il pleut depuis ce matin."],
 ["She's been working here for five years.", "Elle travaille ici depuis cinq ans."],
 ["Your eyes are red. Have you been crying?", "Tu as les yeux rouges. Tu as pleuré ?"],
],
"attention": "Les verbes d'état (know, like, want, own, believe) ne prennent pas la forme continue : <b>I've known her for years</b>, jamais <i>I've been knowing her</i>.",
"serie": "ppContinuEnExercises", "kicker": "Present perfect continu",
"questions": """
I've been ___ for you for an hour! | waiting | wait / waited | Je t'attends depuis une heure ! | Have been + -ing : l'action dure jusqu'à maintenant.
It ___ raining since noon. | has been | is / was | Il pleut depuis midi. | Depuis + action qui dure → has been + -ing.
How long have you been ___ English? | learning | learn / learned | Depuis combien de temps apprends-tu l'anglais ? | How long + have been + -ing.
I've ___ her since high school. | known | been knowing / knowing | Je la connais depuis le lycée. | Know est un verbe d'état : present perfect simple.
She's tired because she's been ___ all day. | working | worked / work | Elle est fatiguée parce qu'elle a travaillé toute la journée. | La durée explique un résultat visible.
I've ___ three emails this morning. | written | been writing / writing | J'ai écrit trois courriels ce matin. | Un nombre, un résultat → present perfect simple.
They ___ been living here for ten years. | have | has / are | Ils habitent ici depuis dix ans. | They + have been.
You're out of breath. Have you been ___? | running | run / ran | Tu es essoufflé. Tu as couru ? | Les traces d'une activité récente → continu.
He's been playing the piano ___ he was six. | since | for / during | Il joue du piano depuis ses six ans. | Point de départ → since.
We've been talking ___ two hours. | for | since / ago | Nous parlons depuis deux heures. | Durée → for.
I ___ sleeping well lately. | haven't been | am not / didn't | Je ne dors pas bien ces derniers temps. | Négation : haven't been + -ing.
She ___ painted the whole house — it's finished! | has | has been / is | Elle a peint toute la maison, c'est fini ! | Le résultat achevé → present perfect simple.
"""
},
{
"id": "past-perfect", "titre": "Le past perfect", "resume": "I had already left — le passé avant le passé",
"regle": "<b>Had + participe passé</b>, à toutes les personnes : <b>I had finished</b>, <b>she had left</b>. C'est le plus-que-parfait français : une action <b>antérieure</b> à un autre moment du passé. <b>When I arrived, the train had already left</b> (le train était parti avant mon arrivée). Comparer : <b>When I arrived, the train left</b> (il est parti à ce moment-là). On le trouve avec <b>already</b>, <b>just</b>, <b>never… before</b>, <b>by the time</b>, <b>after</b>.",
"tableau": [
 ["had + participe", "j'avais fait, j'étais parti", "She had already eaten."],
 ["hadn't + participe", "négation", "I hadn't seen it before."],
 ["Had you…?", "question", "Had you met him before?"],
 ["by the time + prétérit, had…", "le temps que…, … avait déjà", "By the time we got there, the show had started."],
 ["after + had…, prétérit", "après avoir…", "After she had finished, she went home."],
],
"exemples": [
 ["I had never seen snow before I moved to Boston.", "Je n'avais jamais vu de neige avant de m'installer à Boston."],
 ["He was tired because he had worked all night.", "Il était fatigué parce qu'il avait travaillé toute la nuit."],
 ["When we arrived, everyone had gone home.", "Quand nous sommes arrivés, tout le monde était rentré."],
],
"attention": "Contracté, <b>'d</b> peut être <b>had</b> ou <b>would</b> : <b>I'd left</b> (had, suivi d'un participe) n'est pas <b>I'd leave</b> (would, suivi du verbe nu).",
"serie": "pastPerfectEnExercises", "kicker": "Le past perfect",
"questions": """
When I arrived, the movie ___ already started. | had | has / was | Quand je suis arrivé, le film avait déjà commencé. | Antérieur à un autre passé → had + participe.
She ___ never flown before that trip. | had | has / did | Elle n'avait jamais pris l'avion avant ce voyage. | Never… before, dans un récit au passé → past perfect.
By the time we got home, the kids ___ asleep. | had fallen | have fallen / fell | Le temps qu'on rentre, les enfants s'étaient endormis. | By the time + prétérit, puis had + participe.
I couldn't pay because I had ___ my wallet. | forgotten | forgot / forget | Je n'ai pas pu payer parce que j'avais oublié mon portefeuille. | forget → forgot → forgotten.
After he ___ finished his work, he went out. | had | has / was | Après avoir fini son travail, il est sorti. | After + had + participe.
They ___ met before the party. | hadn't | haven't / didn't have | Ils ne s'étaient jamais rencontrés avant la fête. | Négation : hadn't + participe.
___ you eaten when I called? | Had | Have / Did | Tu avais mangé quand j'ai appelé ? | Question : Had + sujet + participe.
The store was closed. Everyone had ___ home. | gone | went / go | Le magasin était fermé. Tout le monde était rentré. | go → went → gone.
I recognized him because I ___ seen his photo. | had | have / was | Je l'ai reconnu parce que j'avais vu sa photo. | L'action d'avant → past perfect.
When I got to the station, the train ___. | had left | has left / leaves | Quand je suis arrivé à la gare, le train était parti. | Il était déjà parti avant mon arrivée.
She told me she ___ lived in Ohio as a child. | had | has / have | Elle m'a dit qu'elle avait habité l'Ohio enfant. | Récit au passé, action antérieure → had.
I'd ___ the book, so I knew the ending. | read | reading / reads | J'avais lu le livre, donc je connaissais la fin. | I'd + participe = I had read.
"""
},
{
"id": "conditionnels-1-2", "titre": "If : les conditionnels 1 et 2", "resume": "If it rains, I'll stay — If I won, I'd travel",
"regle": "<b>Conditionnel 1</b> (réel, possible) : <b>if + présent, will + verbe</b> : <b>If it rains, we'll stay home</b>. <b>Conditionnel 2</b> (imaginaire, peu probable) : <b>if + prétérit, would + verbe</b> : <b>If I had more time, I would travel</b>. Comme en français, jamais de futur ni de conditionnel <b>après if</b> : « Si j'avais » = <b>If I had</b>, pas <i>If I would have</i>. Avec be, le conditionnel 2 dit volontiers <b>were</b> à toutes les personnes : <b>If I were you…</b> (à ta place…).",
"tableau": [
 ["if + présent, will + verbe", "si…, … (réel)", "If you study, you'll pass."],
 ["if + prétérit, would + verbe", "si…, …-rais (imaginaire)", "If I lived here, I'd walk to work."],
 ["If I were you, I'd…", "à ta place, je…", "If I were you, I'd call her."],
 ["unless = if… not", "à moins que", "We'll go unless it rains."],
 ["would · 'd · wouldn't", "conditionnel", "I'd buy it. I wouldn't do that."],
],
"exemples": [
 ["If you're hungry, I'll make you a sandwich.", "Si tu as faim, je te fais un sandwich."],
 ["If I won the lottery, I'd buy a house on the coast.", "Si je gagnais à la loterie, j'achèterais une maison sur la côte."],
 ["What would you do if you lost your passport?", "Que ferais-tu si tu perdais ton passeport ?"],
],
"attention": "La phrase avec <b>if</b> peut venir en second, sans virgule : <b>I'll call you if I'm late</b>. Et <b>when</b> (quand, c'est sûr) n'est pas <b>if</b> (si, peut-être) : <b>When I get home, I'll call you</b>.",
"serie": "conditionnelsEnExercises", "kicker": "Conditionnels 1 et 2",
"questions": """
If it ___ tomorrow, we'll cancel the picnic. | rains | will rain / would rain | S'il pleut demain, nous annulerons le pique-nique. | Après if : le présent.
If I had more money, I ___ a new car. | would buy | will buy / bought | Si j'avais plus d'argent, j'achèterais une nouvelle voiture. | Conditionnel 2 : would + verbe.
If I ___ you, I'd talk to him. | were | am / would be | À ta place, je lui parlerais. | If I were you = à ta place.
If you heat ice, it ___. | melts | would melt / melted | Si on chauffe la glace, elle fond. | Une vérité générale : présent des deux côtés.
She'll be angry if you ___ late again. | are | will be / were | Elle sera fâchée si tu es encore en retard. | Réel → if + présent.
What ___ you do if you saw a ghost? | would | will / do | Que ferais-tu si tu voyais un fantôme ? | Imaginaire → would.
If he ___ harder, he would pass. | studied | studies / would study | S'il travaillait plus, il réussirait. | Conditionnel 2 : if + prétérit.
We'll miss the bus ___ we hurry. | unless | if / when | Nous allons rater le bus à moins de nous dépêcher. | Unless = if… not.
I ___ go there alone if I were you. | wouldn't | won't / don't | Je n'irais pas là-bas seul, à ta place. | Négation du conditionnel : wouldn't.
If you ___ me, I'll help you. | call | will call / called | Si tu m'appelles, je t'aiderai. | If + présent, will.
If we lived in Boston, we ___ the subway. | would take | will take / took | Si nous habitions à Boston, nous prendrions le métro. | If + prétérit → would.
___ I get home, I'll call you. | When | If / Unless | Quand je rentrerai, je t'appellerai. | C'est sûr → when.
"""
},
{
"id": "passif", "titre": "Le passif", "resume": "It was built in 1900 — be + participe passé",
"regle": "<b>Be + participe passé</b>, au temps voulu : <b>English is spoken here</b> (présent), <b>The bridge was built in 1900</b> (prétérit), <b>The room has been cleaned</b> (present perfect), <b>It will be done tomorrow</b> (futur). On l'emploie quand l'action compte plus que celui qui la fait. Celui-ci, s'il est dit, vient après <b>by</b> : <b>The novel was written by Mark Twain</b>. L'anglais s'en sert bien plus que le français, qui dirait souvent « on » : <b>I was told</b> = on m'a dit.",
"tableau": [
 ["am / is / are + participe", "présent : est fait", "Coffee is grown in Brazil."],
 ["was / were + participe", "passé : a été fait", "The letters were sent yesterday."],
 ["has / have been + participe", "a été fait (jusqu'ici)", "The tickets have been sold."],
 ["will be + participe", "sera fait", "You'll be paid on Friday."],
 ["is being + participe", "est en train d'être fait", "The road is being repaired."],
 ["by + auteur", "par", "It was painted by Homer."],
],
"exemples": [
 ["The museum was opened in 1876.", "Le musée a été inauguré en 1876."],
 ["My bike has been stolen!", "On m'a volé mon vélo !"],
 ["Dinner is served at seven.", "Le dîner est servi à sept heures."],
],
"attention": "« On » se traduit souvent par un passif : <b>We were told to wait</b> (on nous a dit d'attendre). Et le passif anglais peut partir de la personne : <b>She was given a prize</b> (on lui a donné un prix), tournure impossible en français.",
"serie": "passifEnExercises", "kicker": "Le passif",
"questions": """
English ___ spoken all over the world. | is | are / was | L'anglais est parlé partout dans le monde. | Présent passif : is + participe.
The bridge was ___ in 1900. | built | build / building | Le pont a été construit en 1900. | build → built.
My phone ___ stolen last night. | was | is / has | On m'a volé mon téléphone hier soir. | Passé précis → was + participe.
The tickets have already ___ sold. | been | be / being | Les billets ont déjà été vendus. | Present perfect passif : have been + participe.
This painting was painted ___ Winslow Homer. | by | from / of | Ce tableau a été peint par Winslow Homer. | L'auteur de l'action : by.
The road is ___ repaired right now. | being | been / be | La route est en train d'être réparée. | En cours → is being + participe.
The results ___ be announced tomorrow. | will | are / were | Les résultats seront annoncés demain. | Futur passif : will be + participe.
We ___ told to wait outside. | were | was / are | On nous a dit d'attendre dehors. | We → were ; « on nous a dit » = we were told.
Smoking is not ___ in the building. | allowed | allow / allowing | Il est interdit de fumer dans le bâtiment. | Passif : is allowed.
The letters ___ sent yesterday. | were | was / are | Les lettres ont été envoyées hier. | Pluriel → were.
She ___ given a prize for her work. | was | is being / has | On lui a donné un prix pour son travail. | Le passif part de la personne : she was given.
Breakfast is ___ from 7 to 10. | served | serve / serving | Le petit-déjeuner est servi de 7 h à 10 h. | Is + participe passé.
"""
},
{
"id": "discours-indirect", "titre": "Le discours indirect", "resume": "She said she was tired — rapporter des paroles",
"regle": "Pour rapporter ce que quelqu'un a dit au passé, les temps <b>reculent d'un cran</b> : présent → prétérit, present perfect et prétérit → past perfect, will → would, can → could. « I'm tired » → <b>She said (that) she was tired</b>. Les repères changent aussi : <b>now → then</b>, <b>today → that day</b>, <b>tomorrow → the next day</b>, <b>here → there</b>. <b>Say</b> s'emploie sans complément de personne (<b>she said that…</b>), <b>tell</b> en exige un (<b>she told me that…</b>).",
"tableau": [
 ["« I work » → he said he worked", "présent → prétérit", "She said she lived in Boston."],
 ["« I've finished » → she said she had finished", "→ past perfect", "He said he had seen it."],
 ["« I will » → he said he would", "will → would", "They said they would come."],
 ["« I can » → she said she could", "can → could", "He said he couldn't swim."],
 ["say (that) · tell + personne", "dire · dire à quelqu'un", "She told me she was busy."],
 ["ask if / whether · ask + mot interrogatif", "demander si · où, quand…", "He asked if I was ready. She asked where I lived."],
],
"exemples": [
 ["He said he would call me later.", "Il a dit qu'il m'appellerait plus tard."],
 ["She told us that the store had closed.", "Elle nous a dit que le magasin avait fermé."],
 ["They asked me where I came from.", "Ils m'ont demandé d'où je venais."],
],
"attention": "La question rapportée reprend l'ordre d'une phrase affirmative, sans do : <b>She asked where I lived</b>, et non <i>where did I live</i>. Et pas <i>She said me</i> : on dit <b>She told me</b> ou <b>She said to me</b>.",
"serie": "discoursIndirectEnExercises", "kicker": "Discours indirect",
"questions": """
« I'm tired. » → She said she ___ tired. | was | is / has been | « Je suis fatiguée. » → Elle a dit qu'elle était fatiguée. | Présent → prétérit.
« I will help. » → He said he ___ help. | would | will / can | « Je vais aider. » → Il a dit qu'il aiderait. | Will → would.
« I can't swim. » → She said she ___ swim. | couldn't | can't / doesn't | « Je ne sais pas nager. » → Elle a dit qu'elle ne savait pas nager. | Can → could.
« I've lost my keys. » → He said he ___ his keys. | had lost | has lost / lost | « J'ai perdu mes clés. » → Il a dit qu'il avait perdu ses clés. | Present perfect → past perfect.
She ___ me that she was busy. | told | said / spoke | Elle m'a dit qu'elle était occupée. | Tell + personne.
He ___ that he was hungry. | said | told / talked | Il a dit qu'il avait faim. | Say, sans complément de personne.
« Are you ready? » → He asked ___ I was ready. | if | that / what | « Tu es prêt ? » → Il m'a demandé si j'étais prêt. | Question oui / non → ask if.
« Where do you live? » → She asked me where I ___. | lived | did live / do live | « Où habites-tu ? » → Elle m'a demandé où j'habitais. | Ordre affirmatif, pas de do.
« I'll see you tomorrow. » → He said he'd see me ___. | the next day | tomorrow / yesterday | « À demain. » → Il a dit qu'il me verrait le lendemain. | Tomorrow → the next day.
« I live here. » → She said she lived ___. | there | here / this | « J'habite ici. » → Elle a dit qu'elle habitait là. | Here → there.
« We went to Maine. » → They said they ___ to Maine. | had gone | have gone / go | « Nous sommes allés dans le Maine. » → Ils ont dit qu'ils étaient allés dans le Maine. | Prétérit → past perfect.
He asked me what time it ___. | was | is it / was it | Il m'a demandé quelle heure il était. | Question rapportée : sujet + verbe.
"""
},
{
"id": "relatives", "titre": "Les relatives : who, which, that, whose, where", "resume": "The man who called — qui, que, dont, où",
"regle": "<b>Who</b> pour les personnes, <b>which</b> pour les choses, <b>that</b> pour les deux (plus courant à l'oral). <b>Whose</b> = dont (possession) : <b>the woman whose car was stolen</b>. <b>Where</b> = où (un lieu), <b>when</b> = où (un moment). Quand le relatif est <b>complément</b> (que), on peut l'omettre : <b>the book (that) I bought</b>. Quand il est <b>sujet</b> (qui), il est obligatoire : <b>the man who lives next door</b>.",
"tableau": [
 ["who / that", "qui, que (personne)", "the girl who sings"],
 ["which / that", "qui, que (chose)", "the bus that goes downtown"],
 ["(that) — omis", "que (complément)", "the movie we saw"],
 ["whose", "dont (possession)", "the man whose dog barks"],
 ["where · when", "où (lieu) · où (moment)", "the city where I was born, the day when we met"],
],
"exemples": [
 ["That's the woman who helped me.", "C'est la femme qui m'a aidé."],
 ["The book I'm reading is very long.", "Le livre que je lis est très long."],
 ["This is the house where I grew up.", "Voici la maison où j'ai grandi."],
],
"attention": "La préposition se place volontiers à la fin : <b>the friend I told you about</b> (l'ami dont je t'ai parlé), <b>the house we live in</b> (la maison où nous habitons). Et « ce que » se dit <b>what</b> : <b>I know what you want</b>.",
"serie": "relativesEnExercises", "kicker": "Les relatives",
"questions": """
The man ___ lives next door is a doctor. | who | which / whose | L'homme qui habite à côté est médecin. | Une personne, sujet → who.
The bus ___ goes downtown is late. | that | who / whose | Le bus qui va au centre-ville est en retard. | Une chose → that ou which.
That's the woman ___ car was stolen. | whose | who / which | C'est la femme dont la voiture a été volée. | Possession → whose.
This is the town ___ I was born. | where | which / when | C'est la ville où je suis né. | Un lieu → where.
I remember the day ___ we met. | when | where / which | Je me souviens du jour où nous nous sommes rencontrés. | Un moment → when.
The movie ___ we saw was great. | — | who / what | Le film que nous avons vu était super. | Complément : le relatif peut disparaître.
I don't understand ___ you mean. | what | that / which | Je ne comprends pas ce que tu veux dire. | Ce que = what.
The friend I told you ___ is coming tonight. | about | of / from | L'ami dont je t'ai parlé vient ce soir. | La préposition va à la fin : tell about.
Students ___ arrive late must sign in. | who | which / whose | Les élèves qui arrivent en retard doivent signer. | Personnes → who.
The laptop ___ I bought last week is broken. | that | who / what | L'ordinateur que j'ai acheté la semaine dernière est cassé. | Une chose → that.
The hotel ___ we stayed was near the beach. | where | which / what | L'hôtel où nous avons logé était près de la plage. | Un lieu → where.
He's the author ___ books I love. | whose | who / that | C'est l'auteur dont j'adore les livres. | Les livres de l'auteur → whose.
"""
},
{
"id": "deduction", "titre": "Must, might, can't : la déduction", "resume": "He must be tired — il doit être fatigué",
"regle": "Les modaux servent aussi à dire <b>à quel point on est sûr</b>. <b>Must</b> = presque sûr que oui (il doit être…) : <b>She must be at work</b>. <b>Can't</b> = presque sûr que non : <b>That can't be true!</b> <b>Might</b>, <b>may</b>, <b>could</b> = peut-être : <b>It might rain later</b>. Au passé, on ajoute <b>have + participe</b> : <b>He must have missed the bus</b> (il a dû rater le bus).",
"tableau": [
 ["must + verbe", "doit (sûrement)", "You must be hungry."],
 ["can't + verbe", "ne peut pas (sûrement pas)", "He can't be serious."],
 ["might · may · could + verbe", "peut-être", "She might come later."],
 ["must have + participe", "a dû (sûrement)", "They must have left."],
 ["can't have + participe", "n'a pas pu", "She can't have forgotten."],
 ["might have + participe", "a peut-être", "I might have lost it on the bus."],
],
"exemples": [
 ["The lights are off. They must be asleep.", "Les lumières sont éteintes. Ils doivent dormir."],
 ["Take an umbrella, it might rain.", "Prends un parapluie, il risque de pleuvoir."],
 ["He can't have finished already!", "Il ne peut pas avoir déjà fini !"],
],
"attention": "Le contraire de <b>must</b> (déduction) n'est pas <b>mustn't</b> (interdiction) mais <b>can't</b> : <b>He can't be at home</b> (il ne peut pas être chez lui).",
"serie": "deductionEnExercises", "kicker": "La déduction",
"questions": """
You've been walking all day. You ___ be tired. | must | can't / mustn't | Tu marches depuis ce matin. Tu dois être fatigué. | Presque sûr → must.
That ___ be true — he was with me all evening! | can't | mustn't / must | Ça ne peut pas être vrai, il était avec moi toute la soirée ! | Presque sûr que non → can't.
Take a jacket, it ___ get cold tonight. | might | must / can't | Prends une veste, il risque de faire froid ce soir. | Peut-être → might.
Her car isn't here. She ___ have left already. | must | can't / should | Sa voiture n'est pas là. Elle a dû déjà partir. | Déduction sur le passé → must have + participe.
He ___ have forgotten — I reminded him twice! | can't | mustn't / might not | Il ne peut pas avoir oublié, je le lui ai rappelé deux fois ! | Sûrement pas, au passé → can't have.
I can't find my keys. I might have ___ them at work. | left | leave / leaving | Je ne trouve pas mes clés. Je les ai peut-être laissées au travail. | Might have + participe passé.
The phone is ringing. It ___ be Mom. | could | can't to / must to | Le téléphone sonne. C'est peut-être maman. | Possibilité → could.
They've been married for fifty years. They ___ be very happy. | must | can't / mustn't | Ils sont mariés depuis cinquante ans. Ils doivent être très heureux. | Déduction logique → must.
She ___ be at home — I just saw her downtown. | can't | must / might | Elle ne peut pas être chez elle, je viens de la voir au centre-ville. | Impossible → can't.
The streets are wet. It must have ___. | rained | rain / raining | Les rues sont mouillées. Il a dû pleuvoir. | Must have + participe.
I'm not sure, but he ___ be Canadian. | may | must / can't | Je ne suis pas sûr, mais il est peut-être Canadien. | Peut-être → may.
You ___ be joking! | must | can / might not | Tu plaisantes, j'espère ! | Must be joking : tu dois plaisanter.
"""
},
{
"id": "be-used-to", "titre": "Be used to, get used to", "resume": "Avoir l'habitude de, s'habituer à",
"regle": "<b>Be used to + -ing</b> (ou un nom) = <b>avoir l'habitude de</b> : <b>I'm used to getting up early</b>. <b>Get used to + -ing</b> = <b>s'habituer à</b> : <b>You'll get used to the cold</b>. Dans les deux, <b>to</b> est une préposition : il est suivi de <b>-ing</b> ou d'un nom, jamais du verbe nu. À ne pas confondre avec <b>used to + verbe</b> (A2), qui dit ce qu'on faisait avant : <b>I used to live in Paris</b>.",
"tableau": [
 ["be used to + -ing / nom", "avoir l'habitude de", "She's used to working at night."],
 ["get used to + -ing / nom", "s'habituer à", "I'm getting used to the noise."],
 ["not be used to", "ne pas avoir l'habitude", "I'm not used to driving on the left."],
 ["used to + verbe (A2)", "avant, je…", "I used to smoke."],
],
"exemples": [
 ["I'm used to the cold — I grew up in Quebec.", "J'ai l'habitude du froid, j'ai grandi au Québec."],
 ["It took me a year to get used to the food.", "Il m'a fallu un an pour m'habituer à la nourriture."],
 ["He isn't used to speaking in public.", "Il n'a pas l'habitude de parler en public."],
],
"attention": "Trois formes, trois sens : <b>I used to drive</b> (avant, je conduisais), <b>I'm used to driving</b> (j'ai l'habitude de conduire), <b>I'm getting used to driving</b> (je m'habitue à conduire).",
"serie": "beUsedToEnExercises", "kicker": "Be / get used to",
"questions": """
I'm used to ___ up early. | getting | get / got | J'ai l'habitude de me lever tôt. | Be used to + -ing.
You'll soon get used ___ the weather. | to | at / with | Tu t'habitueras vite au temps. | Get used to + nom.
She ___ used to living alone. | is | does / has | Elle a l'habitude de vivre seule. | Be used to : is used to.
I ___ to live in Paris, but now I live in Boston. | used | am used / get used | J'habitais à Paris, mais maintenant j'habite à Boston. | Habitude passée qui a cessé → used to + verbe.
He isn't used to ___ so much. | working | work / worked | Il n'a pas l'habitude de travailler autant. | Not be used to + -ing.
It's hard to ___ used to the time difference. | get | be / use | C'est dur de s'habituer au décalage horaire. | S'habituer = get used to.
Are you used to ___ on the right? | driving | drive / drove | Tu as l'habitude de conduire à droite ? | Be used to + -ing.
I'm slowly ___ used to my new job. | getting | being / using | Je m'habitue peu à peu à mon nouveau travail. | En train de s'habituer → getting used to.
We ___ used to the noise after a few weeks. | got | were / used | Nous nous sommes habitués au bruit au bout de quelques semaines. | Au prétérit : got used to.
My grandmother never ___ used to cell phones. | got | was / use | Ma grand-mère ne s'est jamais habituée aux téléphones portables. | Get au prétérit : got.
She's used ___ hard work. | to | with / at | Elle a l'habitude du travail difficile. | Be used to + nom.
I used to ___ coffee, but now I prefer tea. | drink | drinking / drank | Avant, je buvais du café, mais maintenant je préfère le thé. | Used to + verbe nu.
"""
},
{
"id": "phrasal-verbs-1", "titre": "Les phrasal verbs (1)", "resume": "give up, look after, turn down — verbe + particule",
"regle": "Un <b>phrasal verb</b> est un verbe suivi d'une particule (<b>up, down, out, off, on, after…</b>) qui en change le sens : <b>give</b> (donner) → <b>give up</b> (abandonner), <b>look</b> (regarder) → <b>look after</b> (s'occuper de). Le sens se devine rarement : il s'apprend comme un mot. Avec un complément <b>nom</b>, la particule va avant ou après : <b>turn off the light</b> / <b>turn the light off</b>. Avec un <b>pronom</b>, toujours au milieu : <b>turn it off</b>, jamais <i>turn off it</i>.",
"tableau": [
 ["give up", "abandonner, arrêter", "I gave up smoking."],
 ["look after", "s'occuper de", "She looks after her little brother."],
 ["find out", "découvrir, apprendre", "I found out the truth."],
 ["turn down", "refuser ; baisser", "He turned down the job."],
 ["put off", "remettre à plus tard", "Don't put it off until tomorrow."],
 ["get along (with)", "bien s'entendre (avec)", "I get along with my boss."],
],
"exemples": [
 ["Can you pick me up at six?", "Tu peux venir me chercher à six heures ?"],
 ["We ran out of coffee.", "On n'avait plus de café."],
 ["Turn the TV off, please. — OK, I'll turn it off.", "Éteins la télé, s'il te plaît. — D'accord, je l'éteins."],
],
"attention": "Avec un pronom, la particule se place après lui : <b>pick it up</b>, <b>turn them down</b>, <b>call her back</b>. <i>Pick up it</i> est une faute.",
"serie": "phrasalVerbs1EnExercises", "kicker": "Phrasal verbs (1)",
"questions": """
I'm trying to ___ up sugar. | give | take / put | J'essaie d'arrêter le sucre. | Give up = abandonner, arrêter.
Who's going to look ___ the dog while we're away? | after | for / at | Qui va s'occuper du chien pendant notre absence ? | Look after = s'occuper de.
Can you turn ___ the music? It's too loud. | down | up / off | Tu peux baisser la musique ? C'est trop fort. | Turn down = baisser.
I found ___ that she's moving to Chicago. | out | up / off | J'ai appris qu'elle déménage à Chicago. | Find out = découvrir, apprendre.
Don't put ___ your homework until Sunday night. | off | out / on | Ne remets pas tes devoirs au dimanche soir. | Put off = remettre à plus tard.
I get ___ well with my sister. | along | up / over | Je m'entends bien avec ma sœur. | Get along with = bien s'entendre avec.
The lights are on. Can you turn ___ off? | them | off them / they | Les lumières sont allumées. Tu peux les éteindre ? | Pronom au milieu : turn them off.
We ran ___ of milk. | out | off / down | On n'a plus de lait. | Run out of = ne plus avoir de.
He turned ___ the invitation to the wedding. | down | off / out | Il a refusé l'invitation au mariage. | Turn down = refuser.
Please fill ___ this form. | out | up / on | Remplissez ce formulaire, s'il vous plaît. | Fill out (américain) = remplir un formulaire.
I'll call you ___ in five minutes. | back | up / again | Je te rappelle dans cinq minutes. | Call back = rappeler.
Can you pick ___ up at the station? | me | I / my | Tu peux venir me chercher à la gare ? | Pronom complément au milieu : pick me up.
"""
},
{
"id": "gerondif-infinitif", "titre": "Stop, remember, try : -ing ou to", "resume": "Le même verbe, deux sens",
"regle": "Quelques verbes acceptent les deux formes, mais avec un <b>sens différent</b>. <b>Stop doing</b> = arrêter de faire ; <b>stop to do</b> = s'arrêter pour faire. <b>Remember doing</b> = se souvenir d'avoir fait (le passé) ; <b>remember to do</b> = penser à faire (l'avenir). <b>Forget doing</b> / <b>forget to do</b>, même logique. <b>Try doing</b> = essayer, pour voir (une solution) ; <b>try to do</b> = s'efforcer de (c'est difficile).",
"tableau": [
 ["stop + -ing", "arrêter de", "I stopped smoking."],
 ["stop + to", "s'arrêter pour", "We stopped to buy gas."],
 ["remember + -ing", "se souvenir d'avoir…", "I remember meeting her."],
 ["remember + to", "penser à, ne pas oublier de", "Remember to lock the door."],
 ["try + -ing", "essayer (pour voir)", "Try turning it off and on."],
 ["try + to", "s'efforcer de", "I tried to open it, but I couldn't."],
],
"exemples": [
 ["He stopped to tie his shoe.", "Il s'est arrêté pour lacer sa chaussure."],
 ["I'll never forget seeing the ocean for the first time.", "Je n'oublierai jamais la première fois que j'ai vu l'océan."],
 ["If you can't sleep, try reading a book.", "Si tu n'arrives pas à dormir, essaie de lire un livre."],
],
"attention": "<b>Remember to call</b> regarde vers l'avenir (pense à appeler) ; <b>remember calling</b> regarde le passé (je me souviens d'avoir appelé). Le français dit « se souvenir » et « penser à » : l'anglais garde le même verbe et change la forme.",
"serie": "gerondifInfinitifEnExercises", "kicker": "-ing ou to : le sens change",
"questions": """
I stopped ___ two years ago. Now I don't smoke at all. | smoking | to smoke / smoke | J'ai arrêté de fumer il y a deux ans. Maintenant je ne fume plus du tout. | Arrêter de → stop + -ing.
We stopped ___ a coffee on the way. | to get | getting / get | Nous nous sommes arrêtés en route pour prendre un café. | S'arrêter pour → stop + to.
Remember ___ the windows before you leave. | to close | closing / close | Pense à fermer les fenêtres avant de partir. | Penser à (avenir) → remember + to.
I remember ___ this song as a kid. | hearing | to hear / hear | Je me souviens d'avoir entendu cette chanson enfant. | Souvenir du passé → remember + -ing.
Don't forget ___ the milk! | to buy | buying / buy | N'oublie pas d'acheter le lait ! | Oublier de (avenir) → forget + to.
I'll never forget ___ the Grand Canyon. | visiting | to visit / visit | Je n'oublierai jamais ma visite du Grand Canyon. | Souvenir d'un moment vécu → forget + -ing.
The printer isn't working. Try ___ it off and on again. | turning | to turn / turn | L'imprimante ne marche pas. Essaie de l'éteindre et de la rallumer. | Essayer une solution → try + -ing.
I tried ___ the jar, but it was too tight. | to open | opening / open | J'ai essayé d'ouvrir le bocal, mais il était trop serré. | S'efforcer (sans y arriver) → try + to.
She stopped ___ to her friend. | to talk | talking / talk | Elle s'est arrêtée pour parler à son amie. | Stop + to : s'arrêter pour.
Please stop ___ — I'm trying to sleep! | talking | to talk / talk | Arrête de parler, s'il te plaît, j'essaie de dormir ! | Stop + -ing : arrêter de.
Did you remember ___ your mother? | to call | calling / call | Tu as pensé à appeler ta mère ? | Ne pas oublier de → remember + to.
I don't remember ___ that. Are you sure I said it? | saying | to say / say | Je ne me souviens pas d'avoir dit ça. Tu es sûr que je l'ai dit ? | Souvenir du passé → -ing.
"""
},
]
