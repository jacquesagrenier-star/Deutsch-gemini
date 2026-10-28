# -*- coding: utf-8 -*-
"""Les fiches de grammaire B2 de l'anglais, en francais, et leurs series.
Meme format que grammaire_a2.py. SOURCE : on corrige ici, puis
python anglais/outils/construire.py.
"""

FICHES = [
{
"id": "conditionnel-3", "titre": "Le conditionnel 3 et les mixtes", "resume": "If I had known, I would have come — le regret, l'irréel du passé",
"regle": "Le <b>conditionnel 3</b> imagine un passé qui n'a pas eu lieu : <b>if + past perfect, would have + participe</b>. <b>If I had known, I would have come</b> (si j'avais su, je serais venu). On peut remplacer would par <b>could have</b> (aurait pu) ou <b>might have</b> (aurait peut-être). Les <b>mixtes</b> croisent les époques : une condition passée et une conséquence présente (<b>If I had studied medicine, I would be a doctor now</b>), ou l'inverse (<b>If I spoke French, I would have understood</b>).",
"tableau": [
 ["if + had + participe, would have + participe", "si j'avais…, j'aurais…", "If we had left earlier, we would have caught the train."],
 ["could have · might have + participe", "aurait pu · aurait peut-être", "If you had asked, I could have helped."],
 ["if + had + participe, would + verbe", "passé → présent", "If I had saved, I'd be rich now."],
 ["if + prétérit, would have + participe", "présent → passé", "If he were careful, he wouldn't have fallen."],
 ["Had I known…", "inversion (soutenu) = If I had known", "Had I known, I'd have called."],
],
"exemples": [
 ["If it hadn't rained, we would have gone to the beach.", "S'il n'avait pas plu, nous serions allés à la plage."],
 ["I would have called you if I'd had your number.", "Je t'aurais appelé si j'avais eu ton numéro."],
 ["If she had taken the job, she'd be living in Boston now.", "Si elle avait pris le poste, elle vivrait à Boston maintenant."],
],
"attention": "Jamais de would dans la partie en if : « si j'avais su » = <b>if I had known</b>, pas <i>if I would have known</i>. À l'oral, 'd vaut had dans la condition et would dans la conséquence : <b>If I'd known, I'd have come</b>.",
"serie": "conditionnel3EnExercises", "kicker": "Conditionnel 3",
"questions": """
If I ___ known, I would have come. | had | would have / have | Si j'avais su, je serais venu. | If + past perfect : had + participe.
If you had asked me, I ___ have helped you. | would | will / had | Si tu me l'avais demandé, je t'aurais aidé. | Would have + participe.
We would have won if he ___ scored. | had | would have / has | Nous aurions gagné s'il avait marqué. | La condition passée : had + participe.
If she ___ left earlier, she wouldn't have missed the bus. | had | would / has | Si elle était partie plus tôt, elle n'aurait pas raté le bus. | If + had + participe.
If it hadn't rained, we ___ gone hiking. | would have | would / had | S'il n'avait pas plu, nous serions allés en randonnée. | Would have + participe.
If I had studied harder, I ___ a better job now. | would have | would have had / had | Si j'avais travaillé plus, j'aurais un meilleur emploi maintenant. | Mixte : passé → présent : would + verbe.
___ I known, I would have called. | Had | If / Would | Si j'avais su, j'aurais appelé. | Inversion soutenue : Had I known = If I had known.
If you had told me, I ___ have been so worried. | wouldn't | won't / didn't | Si tu me l'avais dit, je ne me serais pas autant inquiété. | Négation : wouldn't have.
He ___ have died if the ambulance had been late. | might | will / must | Il serait peut-être mort si l'ambulance avait été en retard. | Might have = aurait peut-être.
If I spoke Spanish, I ___ understood the movie. | would have | had / would | Si je parlais espagnol, j'aurais compris le film. | Mixte : présent → passé.
If they ___ invested in 2010, they'd be rich today. | had | would have / have | S'ils avaient investi en 2010, ils seraient riches aujourd'hui. | Condition passée : had + participe.
I could have helped if you ___ asked. | had | would have / have | J'aurais pu aider si tu avais demandé. | If + had + participe.
"""
},
{
"id": "wish", "titre": "Wish, if only : le regret et le souhait", "resume": "I wish I had more time — si seulement…",
"regle": "<b>Wish</b> (et <b>if only</b>, plus fort) dit qu'on voudrait que les choses soient autres. Un regret sur le <b>présent</b> : <b>wish + prétérit</b> (<b>I wish I had a car</b> = j'aimerais avoir une voiture). Un regret sur le <b>passé</b> : <b>wish + past perfect</b> (<b>I wish I had studied more</b> = j'aurais aimé étudier plus). Une irritation ou un vœu pour <b>l'avenir</b>, sur quelqu'un d'autre : <b>wish + would</b> (<b>I wish you would stop</b> = si seulement tu arrêtais).",
"tableau": [
 ["wish + prétérit", "regret présent", "I wish I lived closer."],
 ["wish + were", "regret présent avec be", "I wish it were summer."],
 ["wish + had + participe", "regret passé", "I wish I hadn't said that."],
 ["wish + would + verbe", "agacement, souhait (autrui)", "I wish he would call me."],
 ["if only + même temps", "si seulement", "If only I had known!"],
],
"exemples": [
 ["I wish I could speak French fluently.", "J'aimerais parler couramment français."],
 ["If only we had more time!", "Si seulement nous avions plus de temps !"],
 ["She wishes she hadn't sold her house.", "Elle regrette d'avoir vendu sa maison."],
],
"attention": "On ne dit pas <i>I wish I would</i> pour soi-même : <b>I wish I could</b>. Et pour un simple souhait d'avenir poli, l'anglais prend <b>hope</b> : <b>I hope you get the job</b> (j'espère que tu auras le poste).",
"serie": "wishEnExercises", "kicker": "Wish, if only",
"questions": """
I wish I ___ more free time. | had | have / would have | J'aimerais avoir plus de temps libre. | Regret présent : wish + prétérit.
I wish I ___ said that. It was rude. | hadn't | didn't / wouldn't | Je regrette d'avoir dit ça. C'était grossier. | Regret passé : wish + had (not) + participe.
I wish you ___ stop interrupting me! | would | will / had | Si seulement tu arrêtais de m'interrompre ! | Agacement envers quelqu'un : wish + would.
If only I ___ known about the party! | had | have / would | Si seulement j'avais été au courant de la fête ! | Regret passé : if only + had + participe.
I wish it ___ warmer today. | were | is / would | J'aimerais qu'il fasse plus chaud aujourd'hui. | Wish + were (be au prétérit irréel).
She wishes she ___ speak Japanese. | could | can / would | Elle aimerait savoir parler japonais. | Pour soi : wish + could.
I ___ you get the job! | hope | wish / would | J'espère que tu auras le poste ! | Un vœu réaliste pour l'avenir → hope.
I wish I ___ gone to the concert last night. | had | have / would have | J'aurais aimé aller au concert hier soir. | Passé → had + participe.
If only he ___ listen to me! | would | will / does | Si seulement il m'écoutait ! | Le comportement d'autrui → would.
They wish they ___ in a bigger apartment. | lived | live / would live | Ils aimeraient habiter un appartement plus grand. | Wish + prétérit.
I wish I ___ so tired all the time. | weren't | am not / won't be | J'aimerais ne pas être tout le temps aussi fatigué. | Wish + weren't.
Do you ever wish you ___ chosen a different career? | had | have / would | Tu regrettes parfois de ne pas avoir choisi un autre métier ? | Regret passé.
"""
},
{
"id": "passif-avance", "titre": "Le passif avancé : have it done, it is said", "resume": "Faire faire, on dit que…",
"regle": "Trois tournures fréquentes. <b>Have / get + chose + participe</b> = faire faire par quelqu'un d'autre : <b>I had my car repaired</b> (j'ai fait réparer ma voiture). Le <b>passif des verbes d'opinion</b> : <b>It is said that…</b> ou <b>He is said to…</b> (on dit que…, il paraît que…) : <b>He is said to be very rich</b>. Le <b>passif avec un modal</b> : <b>modal + be + participe</b> : <b>It must be done today</b>, <b>It can't be fixed</b>.",
"tableau": [
 ["have + chose + participe", "faire faire", "We're having the kitchen painted."],
 ["get + chose + participe", "faire faire (plus familier)", "I need to get my hair cut."],
 ["It is said / believed that…", "on dit / on croit que…", "It is believed that he left the country."],
 ["sujet + is said to + verbe", "il paraît que…", "She is said to be the best."],
 ["is said to have + participe", "il paraît qu'il a…", "He is said to have won millions."],
 ["modal + be + participe", "passif d'un modal", "This must be signed by Friday."],
],
"exemples": [
 ["I'm having my eyes tested tomorrow.", "Je fais contrôler ma vue demain."],
 ["The painting is thought to be worth a fortune.", "On pense que le tableau vaut une fortune."],
 ["The form has to be filled out in ink.", "Le formulaire doit être rempli à l'encre."],
],
"attention": "<b>I cut my hair</b> veut dire que vous l'avez coupée vous-même ; chez le coiffeur, c'est <b>I had my hair cut</b>. Et <b>He is said to be…</b> garde la personne en sujet, ce que le français ne fait pas.",
"serie": "passifAvanceEnExercises", "kicker": "Passif avancé",
"questions": """
I had my car ___ yesterday. | repaired | repair / repairing | J'ai fait réparer ma voiture hier. | Have + chose + participe passé.
We're having the house ___ next week. | painted | paint / to paint | Nous faisons peindre la maison la semaine prochaine. | Have + chose + participe.
You should get your eyes ___. | tested | test / testing | Tu devrais faire contrôler ta vue. | Get + chose + participe.
It ___ said that the hotel is haunted. | is | says / has | On dit que l'hôtel est hanté. | It is said that = on dit que.
He is said ___ very rich. | to be | being / be | Il paraît qu'il est très riche. | Be said + to + verbe.
She is believed to ___ the country last year. | have left | leave / left | On croit qu'elle a quitté le pays l'an dernier. | Action passée : to have + participe.
This form must ___ signed by Friday. | be | being / been | Ce formulaire doit être signé avant vendredi. | Modal + be + participe.
The problem can't ___ solved overnight. | be | been / to be | Le problème ne peut pas être réglé du jour au lendemain. | Can't + be + participe.
I need to ___ my hair cut. | get | do / make | Je dois aller me faire couper les cheveux. | Faire faire = get (ou have).
The suspect is thought ___ in Canada. | to be | being / is | On pense que le suspect est au Canada. | Be thought + to + verbe.
The windows ___ cleaned every spring. | are | have / do | Les fenêtres sont lavées chaque printemps. | Passif présent : are + participe.
The report should have ___ sent yesterday. | been | be / being | Le rapport aurait dû être envoyé hier. | Modal passé passif : should have been + participe.
"""
},
{
"id": "futurs-avances", "titre": "Le futur continu et le futur antérieur", "resume": "I'll be working — I'll have finished",
"regle": "<b>Will be + -ing</b> (futur continu) : une action <b>en cours</b> à un moment de l'avenir : <b>This time tomorrow, I'll be flying to Chicago</b>. Il sert aussi à demander poliment les projets de quelqu'un : <b>Will you be using the car tonight?</b> <b>Will have + participe</b> (futur antérieur) : une action <b>terminée</b> avant un moment de l'avenir, souvent avec <b>by</b> : <b>By June, I'll have finished my degree</b>.",
"tableau": [
 ["will be + -ing", "serai en train de", "At 8 p.m. I'll be watching the game."],
 ["Will you be + -ing?", "question polie sur les projets", "Will you be joining us?"],
 ["will have + participe", "aurai fini, serai parti", "I'll have left by then."],
 ["by + moment", "d'ici, avant", "By next year, we'll have saved enough."],
 ["will have been + -ing", "cela fera… que", "In May, I'll have been living here for ten years."],
],
"exemples": [
 ["Don't call at nine — I'll be putting the kids to bed.", "N'appelle pas à neuf heures, je serai en train de coucher les enfants."],
 ["By the time you arrive, we'll have eaten.", "Le temps que tu arrives, nous aurons mangé."],
 ["Next year she'll have worked here for twenty years.", "L'an prochain, cela fera vingt ans qu'elle travaille ici."],
],
"attention": "Après <b>by the time</b>, <b>when</b>, <b>before</b>, l'anglais garde le présent : <b>By the time you arrive</b>, pas <i>will arrive</i>, même si le français dit « quand tu arriveras ».",
"serie": "futursAvancesEnExercises", "kicker": "Futurs avancés",
"questions": """
This time tomorrow, I'll be ___ on the beach. | lying | lie / lain | Demain à cette heure-ci, je serai allongé sur la plage. | Will be + -ing : en cours dans l'avenir.
By June, I'll ___ finished my degree. | have | be / had | D'ici juin, j'aurai fini mes études. | Will have + participe : terminé avant.
Don't call at eight — we'll ___ having dinner. | be | have / being | N'appelle pas à huit heures, nous serons en train de dîner. | Will be + -ing.
By the time you get here, the movie will have ___. | started | start / starting | Le temps que tu arrives, le film aura commencé. | Will have + participe.
___ you be using the car tonight? | Will | Do / Are | Tu vas te servir de la voiture ce soir ? | Question polie : Will you be + -ing?
By next year, they'll have ___ enough money. | saved | save / saving | D'ici l'an prochain, ils auront économisé assez d'argent. | Will have + participe.
In May, I'll have been ___ here for ten years. | living | live / lived | En mai, cela fera dix ans que j'habite ici. | Will have been + -ing : la durée jusqu'à un moment futur.
By the time you ___, we'll have eaten. | arrive | will arrive / arrived | Le temps que tu arrives, nous aurons mangé. | Après by the time : le présent.
At midnight, she'll still be ___. | working | work / worked | À minuit, elle sera encore en train de travailler. | Will be + -ing.
I won't have ___ the report by Friday. | finished | finish / finishing | Je n'aurai pas fini le rapport d'ici vendredi. | Won't have + participe.
Will you have ___ dinner by eight? | had | have / having | Vous aurez dîné avant huit heures ? | Will have + participe : had.
This time next week, we'll be ___ to Chicago. | flying | fly / flown | La semaine prochaine à cette heure-ci, nous serons dans l'avion pour Chicago. | Will be + -ing.
"""
},
{
"id": "modaux-passe", "titre": "Should have, could have, must have", "resume": "J'aurais dû, j'aurais pu, il a dû",
"regle": "Un modal suivi de <b>have + participe</b> parle du <b>passé</b>. <b>Should have</b> = j'aurais dû (un reproche, un regret) : <b>You should have told me</b>. <b>Could have</b> = j'aurais pu (une possibilité non réalisée) : <b>We could have won</b>. <b>Would have</b> = je l'aurais fait (si…). <b>Must have</b> = il a dû (déduction, presque sûr) ; <b>can't have</b> = il n'a pas pu ; <b>might have</b> = il a peut-être. <b>Needn't have</b> = ce n'était pas la peine (mais on l'a fait).",
"tableau": [
 ["should have + participe", "aurait dû", "I should have studied more."],
 ["shouldn't have + participe", "n'aurait pas dû", "You shouldn't have said that."],
 ["could have + participe", "aurait pu", "You could have been hurt!"],
 ["must have + participe", "a dû (déduction)", "She must have missed the bus."],
 ["can't have + participe", "n'a pas pu", "He can't have seen us."],
 ["needn't have + participe", "ce n'était pas la peine", "You needn't have brought anything."],
],
"exemples": [
 ["I should have listened to you.", "J'aurais dû t'écouter."],
 ["You could have called!", "Tu aurais pu appeler !"],
 ["They must have forgotten about the meeting.", "Ils ont dû oublier la réunion."],
],
"attention": "<b>Didn't need to go</b> (je n'ai pas eu besoin d'y aller, et je n'y suis pas allé) n'est pas <b>needn't have gone</b> (j'y suis allé pour rien). Et « tu aurais dû » se dit <b>you should have</b>, jamais <i>you would have must</i>.",
"serie": "modauxPasseEnExercises", "kicker": "Modaux au passé",
"questions": """
I ___ have studied more for the exam. | should | must / can | J'aurais dû étudier davantage pour l'examen. | Regret → should have.
You ___ have told me! I would have helped. | could | must / can't | Tu aurais pu me le dire ! Je t'aurais aidé. | Possibilité non saisie → could have.
She's late. She must have ___ the bus. | missed | miss / missing | Elle est en retard. Elle a dû rater le bus. | Must have + participe : déduction.
He ___ have seen us — it was too dark. | can't | mustn't / shouldn't | Il n'a pas pu nous voir, il faisait trop sombre. | Impossible → can't have.
You shouldn't have ___ so much. Now you're sick. | eaten | eat / ate | Tu n'aurais pas dû manger autant. Maintenant tu es malade. | Shouldn't have + participe.
I might have ___ my phone at the café. | left | leave / leaving | J'ai peut-être laissé mon téléphone au café. | Might have + participe.
You ___ have brought a gift — but thank you! | needn't | mustn't / couldn't | Ce n'était pas la peine d'apporter un cadeau, mais merci ! | On l'a fait pour rien → needn't have.
We ___ have won if we had played better. | could | must / should to | Nous aurions pu gagner si nous avions mieux joué. | Could have : possibilité non réalisée.
The streets are wet. It ___ have rained. | must | should / can't | Les rues sont mouillées. Il a dû pleuvoir. | Déduction → must have.
They should have ___ earlier. | left | leave / leaving | Ils auraient dû partir plus tôt. | Should have + participe.
She ___ have known the answer — she's a genius. | must | can't / shouldn't | Elle a dû connaître la réponse, c'est un génie. | Presque sûr → must have.
You ___ have been hurt! Be more careful. | could | must / should | Tu aurais pu te blesser ! Fais plus attention. | Un danger évité → could have.
"""
},
{
"id": "verbes-introducteurs", "titre": "Rapporter : suggest, deny, admit, advise", "resume": "Les verbes qui rapportent sans citer",
"regle": "Au-delà de say et tell, chaque verbe introducteur a sa <b>construction</b>. <b>Suggest + -ing</b> ou <b>suggest that + sujet + verbe</b> : <b>She suggested going</b> / <b>She suggested that we go</b> (jamais <i>suggested us to go</i>). <b>Deny</b> et <b>admit + -ing</b> : <b>He denied taking it</b>. <b>Advise, warn, remind, ask, tell + personne + to</b> : <b>She advised me to wait</b>. <b>Apologize for + -ing</b>, <b>accuse someone of + -ing</b>, <b>insist on + -ing</b>.",
"tableau": [
 ["suggest + -ing / that…", "proposer de", "He suggested taking a taxi."],
 ["deny · admit + -ing", "nier · reconnaître avoir…", "She admitted making a mistake."],
 ["advise · warn · remind + personne + to", "conseiller · avertir · rappeler de", "They warned us not to swim."],
 ["refuse · offer · promise + to", "refuser · proposer · promettre de", "He offered to drive me home."],
 ["accuse of · apologize for · insist on + -ing", "accuser de · s'excuser de · tenir à", "He apologized for being late."],
],
"exemples": [
 ["She suggested that we meet at noon.", "Elle a proposé qu'on se retrouve à midi."],
 ["He denied breaking the window.", "Il a nié avoir cassé la vitre."],
 ["The doctor advised me to rest.", "Le médecin m'a conseillé de me reposer."],
],
"attention": "<b>Suggest</b> ne prend jamais personne + to : <i>He suggested me to come</i> est faux ; on dit <b>He suggested that I come</b> ou <b>He suggested coming</b>.",
"serie": "verbesIntroducteursEnExercises", "kicker": "Verbes introducteurs",
"questions": """
She suggested ___ a taxi. | taking | to take / take | Elle a proposé de prendre un taxi. | Suggest + -ing.
He denied ___ the money. | stealing | to steal / steal | Il a nié avoir volé l'argent. | Deny + -ing.
The doctor advised me ___ more water. | to drink | drinking / drink | Le médecin m'a conseillé de boire plus d'eau. | Advise + personne + to.
She admitted ___ a mistake. | making | to make / make | Elle a reconnu avoir fait une erreur. | Admit + -ing.
They warned us ___ swim in the river. | not to | to not / don't | Ils nous ont avertis de ne pas nager dans la rivière. | Warn + personne + not to.
He apologized ___ being late. | for | of / to | Il s'est excusé d'être en retard. | Apologize for + -ing.
She suggested that we ___ at noon. | meet | to meet / meeting | Elle a proposé qu'on se retrouve à midi. | Suggest that + sujet + verbe.
He offered ___ me home. | to drive | driving / drive | Il a proposé de me raccompagner en voiture. | Offer + to.
They accused him ___ lying. | of | for / about | Ils l'ont accusé de mentir. | Accuse someone of + -ing.
Remind me ___ the tickets. | to buy | buying / buy | Rappelle-moi d'acheter les billets. | Remind + personne + to.
He insisted ___ paying for dinner. | on | to / for | Il a tenu à payer le dîner. | Insist on + -ing.
She refused ___ the contract. | to sign | signing / sign | Elle a refusé de signer le contrat. | Refuse + to.
"""
},
{
"id": "relatives-avancees", "titre": "Relatives non déterminatives et réduites", "resume": "My sister, who lives in Ohio,… — the man sitting there",
"regle": "Une relative <b>non déterminative</b> ajoute une information non indispensable, entre <b>virgules</b> : <b>My sister, who lives in Ohio, is a nurse</b>. Elle prend <b>who</b> ou <b>which</b>, jamais <b>that</b>, et le relatif ne peut pas disparaître. <b>Which</b> peut reprendre toute la phrase : <b>He passed, which surprised everyone</b> (ce qui). On peut aussi <b>réduire</b> une relative : <b>the man (who is) sitting there</b> → <b>the man sitting there</b> ; <b>a book (that was) written in 1850</b> → <b>a book written in 1850</b>.",
"tableau": [
 [", who …,", "qui (information ajoutée, personne)", "My boss, who is French, speaks four languages."],
 [", which …,", "qui, que (chose)", "The Charles River, which runs through Boston, freezes in winter."],
 [", which (toute la phrase)", "ce qui", "It rained all week, which was annoying."],
 ["nom + -ing", "qui fait (réduite)", "The woman talking to Tom is my aunt."],
 ["nom + participe passé", "qui a été fait (réduite)", "The paintings stolen last year were found."],
 ["some of whom · most of which", "dont certains · dont la plupart", "I have ten cousins, most of whom live in Maine."],
],
"exemples": [
 ["Boston, which was founded in 1630, is one of the oldest cities in the US.", "Boston, fondée en 1630, est l'une des plus vieilles villes des États-Unis."],
 ["The kids playing outside are my neighbors'.", "Les enfants qui jouent dehors sont ceux de mes voisins."],
 ["He forgot my birthday, which really hurt.", "Il a oublié mon anniversaire, ce qui m'a vraiment blessé."],
],
"attention": "« Ce qui » qui reprend une phrase entière se dit <b>which</b>, pas <i>what</i> : <b>He was late, which made me angry</b>.",
"serie": "relativesAvanceesEnExercises", "kicker": "Relatives avancées",
"questions": """
My brother, ___ lives in Chicago, is a lawyer. | who | that / which | Mon frère, qui habite à Chicago, est avocat. | Entre virgules, une personne → who (jamais that).
The Freedom Trail, ___ is 2.5 miles long, starts on the Common. | which | that / who | Le Freedom Trail, long de 4 km, part du Common. | Entre virgules, une chose → which.
He passed the exam, ___ surprised everyone. | which | what / that | Il a réussi l'examen, ce qui a surpris tout le monde. | Ce qui (toute la phrase) → which.
The woman ___ to Tom is my aunt. | talking | talks / who talking | La femme qui parle à Tom est ma tante. | Relative réduite : nom + -ing.
The paintings ___ last year were found. | stolen | stealing / stole | Les tableaux volés l'an dernier ont été retrouvés. | Réduite passive : nom + participe passé.
I have ten cousins, most of ___ live in Maine. | whom | who / them | J'ai dix cousins, dont la plupart vivent dans le Maine. | Après une préposition : whom.
She bought three dresses, none of ___ fit her. | which | them / what | Elle a acheté trois robes, dont aucune ne lui va. | None of which.
Our teacher, ___ classes are always fun, is retiring. | whose | who / which | Notre professeur, dont les cours sont toujours amusants, prend sa retraite. | Possession → whose.
The train ___ for New York leaves at nine. | leaving | leaves / that leaving | Le train pour New York part à neuf heures. | Réduite : nom + -ing.
It rained all day, ___ ruined our picnic. | which | that / it | Il a plu toute la journée, ce qui a gâché notre pique-nique. | Which reprend la phrase.
The house, ___ was built in 1890, needs a new roof. | which | that / where | La maison, construite en 1890, a besoin d'un nouveau toit. | Non déterminative : which.
A letter ___ in French arrived this morning. | written | writing / wrote | Une lettre écrite en français est arrivée ce matin. | Réduite passive : written.
"""
},
{
"id": "connecteurs", "titre": "Although, despite, whereas, unless", "resume": "Bien que, malgré, alors que, à moins que",
"regle": "L'opposition se dit de deux façons. <b>Although / even though + sujet + verbe</b> : <b>Although it was raining, we went out</b>. <b>Despite / in spite of + nom ou -ing</b> : <b>Despite the rain, we went out</b> / <b>Despite being tired, she kept working</b>. <b>Whereas / while</b> oppose deux faits (alors que). <b>However</b> commence une nouvelle phrase, suivi d'une virgule. <b>Unless</b> = à moins que (if… not). <b>In case</b> = au cas où. <b>So that</b> = pour que.",
"tableau": [
 ["although · even though + phrase", "bien que, même si", "Although he's rich, he's unhappy."],
 ["despite · in spite of + nom / -ing", "malgré", "Despite the cost, they bought it."],
 ["whereas · while", "alors que, tandis que", "I like tea, whereas she prefers coffee."],
 ["However, …", "Cependant, …", "It's cheap. However, it's far."],
 ["unless", "à moins que", "I'll go unless it rains."],
 ["in case · so that", "au cas où · pour que", "Take a map in case you get lost."],
],
"exemples": [
 ["Even though she was tired, she finished the race.", "Même si elle était fatiguée, elle a fini la course."],
 ["In spite of the traffic, we arrived on time.", "Malgré la circulation, nous sommes arrivés à l'heure."],
 ["He's quiet, whereas his brother is very talkative.", "Il est calme, alors que son frère est très bavard."],
],
"attention": "<b>Despite</b> n'est jamais suivi de <b>of</b> ni d'une phrase : <i>despite of the rain</i> et <i>despite it was raining</i> sont faux. On dit <b>despite the rain</b> ou <b>despite the fact that it was raining</b>.",
"serie": "connecteursEnExercises", "kicker": "Connecteurs",
"questions": """
___ it was raining, we went for a walk. | Although | Despite / However | Bien qu'il pleuve, nous sommes allés nous promener. | Avant une phrase (sujet + verbe) → although.
___ the rain, we went for a walk. | Despite | Although / Even though | Malgré la pluie, nous sommes allés nous promener. | Avant un nom → despite.
In spite ___ the traffic, we arrived on time. | of | — / that | Malgré la circulation, nous sommes arrivés à l'heure. | In spite of + nom.
I like tea, ___ my wife prefers coffee. | whereas | despite / unless | J'aime le thé, alors que ma femme préfère le café. | Opposition de deux faits → whereas.
The hotel is cheap. ___, it's far from downtown. | However | Although / Despite | L'hôtel est bon marché. Cependant, il est loin du centre. | En début de phrase, avec une virgule → however.
I'll come ___ I have to work late. | unless | if / despite | Je viendrai, à moins que je doive travailler tard. | À moins que → unless.
Take an umbrella ___ it rains. | in case | unless / despite | Prends un parapluie au cas où il pleuvrait. | Au cas où → in case.
Despite ___ tired, she kept working. | being | she was / be | Malgré sa fatigue, elle a continué à travailler. | Despite + -ing.
He saved money ___ he could buy a car. | so that | in case / unless | Il a économisé pour pouvoir acheter une voiture. | Pour que → so that.
___ though he's rich, he's not happy. | Even | Despite / Although | Même s'il est riche, il n'est pas heureux. | Even though + phrase.
She went to work ___ having a fever. | despite | although / even though | Elle est allée travailler malgré sa fièvre. | Despite + -ing.
You won't pass ___ you study. | unless | if / whereas | Tu ne réussiras pas à moins de travailler. | Unless = if… not.
"""
},
{
"id": "phrasal-verbs-2", "titre": "Les phrasal verbs (2)", "resume": "come up with, put up with, look forward to",
"regle": "Certains phrasal verbs ont <b>deux particules</b> : <b>come up with</b> (trouver une idée), <b>put up with</b> (supporter), <b>look forward to</b> (avoir hâte de), <b>get along with</b> (s'entendre avec), <b>run out of</b> (être à court de), <b>catch up with</b> (rattraper). Ils ne se séparent jamais : <b>I can't put up with it</b>. D'autres changent de sens selon le contexte : <b>take off</b> (décoller, enlever, avoir du succès), <b>turn out</b> (s'avérer), <b>bring up</b> (élever, aborder).",
"tableau": [
 ["come up with", "trouver (une idée)", "She came up with a great plan."],
 ["put up with", "supporter", "I can't put up with the noise."],
 ["look forward to + -ing", "avoir hâte de", "I'm looking forward to seeing you."],
 ["run out of", "manquer de, être à court de", "We ran out of gas."],
 ["turn out", "s'avérer", "It turned out to be easy."],
 ["take off", "décoller ; enlever ; percer", "Her career took off."],
],
"exemples": [
 ["We need to come up with a solution.", "Nous devons trouver une solution."],
 ["The party turned out to be a lot of fun.", "La fête s'est révélée très amusante."],
 ["I'll catch up with you later.", "Je te rattrape plus tard."],
],
"attention": "Après <b>look forward to</b>, to est une préposition : <b>I look forward to hearing from you</b>, jamais <i>to hear</i>.",
"serie": "phrasalVerbs2EnExercises", "kicker": "Phrasal verbs (2)",
"questions": """
She came up ___ a great idea. | with | to / for | Elle a eu une excellente idée. | Come up with = trouver (une idée).
I can't put up ___ this noise anymore. | with | to / on | Je ne supporte plus ce bruit. | Put up with = supporter.
I'm looking forward ___ you. | to seeing | to see / seeing | J'ai hâte de te voir. | Look forward to + -ing.
We've run out ___ coffee. | of | — / from | Nous n'avons plus de café. | Run out of.
The rumor turned ___ to be false. | out | up / over | La rumeur s'est révélée fausse. | Turn out = s'avérer.
The plane took ___ on time. | off | up / out | L'avion a décollé à l'heure. | Take off = décoller.
Go ahead, I'll catch up ___ you. | with | to / on | Vas-y, je te rattrape. | Catch up with = rattraper.
She was brought ___ by her grandparents. | up | out / over | Elle a été élevée par ses grands-parents. | Bring up = élever.
He gets along well ___ his coworkers. | with | to / by | Il s'entend bien avec ses collègues. | Get along with.
Don't let me down — I'm ___ on you. | counting | count up / relying to | Ne me laisse pas tomber, je compte sur toi. | Count on = compter sur.
We had to call ___ the meeting because of the snow. | off | out / down | Nous avons dû annuler la réunion à cause de la neige. | Call off = annuler.
The fire alarm went ___ in the middle of the night. | off | out / up | L'alarme incendie s'est déclenchée en pleine nuit. | Go off = se déclencher.
"""
},
{
"id": "faux-amis-b2", "titre": "Les faux amis (2)", "resume": "eventually, sensible, library, achieve…",
"regle": "Ces mots ressemblent au français mais n'ont <b>pas le même sens</b>. <b>Eventually</b> = finalement (pas éventuellement : <b>possibly</b>). <b>Actually</b> = en fait (pas actuellement : <b>currently</b>). <b>Sensible</b> = raisonnable (sensible = <b>sensitive</b>). <b>Library</b> = bibliothèque (librairie = <b>bookstore</b>). <b>Achieve</b> = réussir, atteindre (achever = <b>finish</b>). <b>Attend</b> = assister à (attendre = <b>wait</b>). <b>Deceive</b> = tromper (décevoir = <b>disappoint</b>). <b>Resume</b> = reprendre (résumer = <b>summarize</b>).",
"tableau": [
 ["eventually", "finalement ≠ éventuellement (possibly)", "Eventually, we found the hotel."],
 ["sensible", "raisonnable ≠ sensible (sensitive)", "That's a sensible idea."],
 ["library", "bibliothèque ≠ librairie (bookstore)", "I borrowed it from the library."],
 ["attend", "assister à ≠ attendre (wait)", "Did you attend the meeting?"],
 ["deceive", "tromper ≠ décevoir (disappoint)", "He deceived his partners."],
 ["resume", "reprendre ≠ résumer (summarize)", "The game resumed after the rain."],
],
"exemples": [
 ["We waited for hours, but eventually the bus came.", "Nous avons attendu des heures, mais le bus a fini par arriver."],
 ["She's very sensitive to criticism.", "Elle est très sensible à la critique."],
 ["Actually, I'm from Montreal, not Quebec City.", "En fait, je viens de Montréal, pas de Québec."],
],
"attention": "D'autres pièges à connaître : <b>pretend</b> (faire semblant ≠ prétendre : <b>claim</b>), <b>assist</b> (aider ≠ assister à : <b>attend</b>), <b>large</b> (grand ≠ large : <b>wide</b>), <b>preservative</b> (conservateur ≠ préservatif : <b>condom</b>).",
"serie": "fauxAmisB2EnExercises", "kicker": "Faux amis (2)",
"questions": """
We waited for an hour, but ___ the bus came. | eventually | possibly / actually | Nous avons attendu une heure, mais le bus a fini par arriver. | Finalement = eventually.
I'm not sure. I'll ___ come, if I have time. | possibly | eventually / actually | Je ne suis pas sûr. Je viendrai éventuellement, si j'ai le temps. | Éventuellement = possibly.
That's a very ___ decision. | sensible | sensitive / sensitively | C'est une décision très raisonnable. | Raisonnable = sensible.
She's very ___ to the cold. | sensitive | sensible / sensual | Elle est très sensible au froid. | Sensible (français) = sensitive.
I borrowed this book from the ___. | library | bookstore / librairy | J'ai emprunté ce livre à la bibliothèque. | Bibliothèque = library.
I bought this book at the ___. | bookstore | library / bookshelf | J'ai acheté ce livre à la librairie. | Librairie = bookstore.
Did you ___ the meeting yesterday? | attend | assist / wait | As-tu assisté à la réunion hier ? | Assister à = attend.
I'm ___ for the bus. | waiting | attending / expecting | J'attends le bus. | Attendre = wait for.
The results ___ me. I expected better. | disappointed | deceived / deluded | Les résultats m'ont déçu. Je m'attendais à mieux. | Décevoir = disappoint.
___, I'm a nurse, not a doctor. | Actually | Currently / Eventually | En fait, je suis infirmier, pas médecin. | En fait = actually.
He ___ to be asleep when I came in. | pretended | claimed / pretends to | Il a fait semblant de dormir quand je suis entré. | Faire semblant = pretend.
Can you ___ the article in three sentences? | summarize | resume / sum | Tu peux résumer l'article en trois phrases ? | Résumer = summarize.
"""
},
]
