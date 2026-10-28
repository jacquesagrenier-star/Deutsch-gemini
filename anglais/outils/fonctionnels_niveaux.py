# -*- coding: utf-8 -*-
"""Les mots-outils A2-C1 de l'anglais, avec leurs phrases, ecrites ici.

Meme format que phrases_a1.FONCTIONNELS : « mot | traduction | categorie |
exemple anglais | exemple francais », sous les cles du fichier allemand
(funktionswort.json), chacune nourrissant un theme du moteur. niveaux.py les
ajoute a fonctionnels.json avec leur niveau. Anglais americain.
"""

FONCTIONNELS = {
"A2": {
"konjunktionen": """
while | pendant que | Temps | She read while I cooked. | Elle lisait pendant que je cuisinais.
before | avant que, avant de | Temps | Wash your hands before you eat. | Lave-toi les mains avant de manger.
after | après que, après | Temps | We went for a walk after we had lunch. | Nous sommes allés nous promener après le déjeuner.
until | jusqu'à ce que | Temps | Wait here until I come back. | Attends ici jusqu'à ce que je revienne.
as soon as | dès que | Temps | I'll call you as soon as I arrive. | Je t'appellerai dès que j'arriverai.
although | bien que | Opposition | Although it was raining, we went out. | Bien qu'il ait plu, nous sommes sortis.
that | que | Liaison | I think that he's right. | Je pense qu'il a raison.
both … and | à la fois … et | Addition | She speaks both French and English. | Elle parle à la fois français et anglais.
either … or | soit … soit, ou … ou | Choix | We can either walk or take the bus. | On peut soit marcher, soit prendre l'autobus.
neither … nor | ni … ni | Choix | He drinks neither tea nor coffee. | Il ne boit ni thé ni café.
so … that | si … que | Conséquence | It was so cold that we stayed inside. | Il faisait si froid que nous sommes restés à l'intérieur.
as … as | aussi … que | Comparaison | She's as tall as her brother. | Elle est aussi grande que son frère.
""",
"praepositionen": """
since | depuis (un moment) | Temps | I've been here since Monday. | Je suis ici depuis lundi.
for (+ durée) | depuis, pendant (une durée) | Temps | We waited for two hours. | Nous avons attendu deux heures.
ago | il y a | Temps | I moved here three years ago. | J'ai emménagé ici il y a trois ans.
through | à travers, par | Lieu | We drove through the city. | Nous avons traversé la ville en voiture.
across | de l'autre côté de, à travers | Lieu | The bank is across the street. | La banque est de l'autre côté de la rue.
along | le long de | Lieu | We walked along the river. | Nous avons marché le long de la rivière.
towards | vers | Lieu | She ran towards the door. | Elle a couru vers la porte.
like | comme | Manière | She sings like a professional. | Elle chante comme une professionnelle.
except | sauf | Manière | Everyone came except Tom. | Tout le monde est venu sauf Tom.
against | contre | Lieu | Lean the bike against the wall. | Appuie le vélo contre le mur.
above | au-dessus de | Lieu | There's a shelf above the sink. | Il y a une étagère au-dessus de l'évier.
below | en dessous de | Lieu | It's ten degrees below zero. | Il fait dix degrés sous zéro.
into | dans (avec mouvement) | Lieu | She walked into the room. | Elle est entrée dans la pièce.
out of | hors de, de (en sortant) | Lieu | He took his keys out of his pocket. | Il a sorti ses clés de sa poche.
""",
"pronomen": """
myself | moi-même, me | Réfléchis | I cut myself while cooking. | Je me suis coupé en cuisinant.
yourself | toi-même, te | Réfléchis | Help yourself to some cake! | Sers-toi du gâteau !
himself · herself | lui-même, elle-même, se | Réfléchis | She taught herself to play the guitar. | Elle a appris la guitare toute seule.
ourselves | nous-mêmes, nous | Réfléchis | We enjoyed ourselves at the party. | Nous nous sommes bien amusés à la fête.
themselves | eux-mêmes, se | Réfléchis | The kids made dinner themselves. | Les enfants ont fait le dîner eux-mêmes.
each other | l'un l'autre, se | Réciproque | They love each other. | Ils s'aiment.
everyone | tout le monde | Indéfinis | Everyone is welcome. | Tout le monde est le bienvenu.
nobody | personne | Indéfinis | Nobody answered the phone. | Personne n'a répondu au téléphone.
someone | quelqu'un | Indéfinis | Someone left a bag on the bus. | Quelqu'un a laissé un sac dans le bus.
something | quelque chose | Indéfinis | I have something for you. | J'ai quelque chose pour toi.
nothing | rien | Indéfinis | There's nothing in the fridge. | Il n'y a rien dans le frigo.
everything | tout | Indéfinis | Everything is ready. | Tout est prêt.
""",
"artikelwoerter": """
a few | quelques | Quantité | I'll be back in a few minutes. | Je reviens dans quelques minutes.
a little | un peu de | Quantité | Add a little salt. | Ajoute un peu de sel.
few | peu de | Quantité | Few people know this place. | Peu de gens connaissent cet endroit.
little | peu de | Quantité | There's little hope now. | Il y a peu d'espoir maintenant.
enough | assez de | Quantité | We don't have enough chairs. | Nous n'avons pas assez de chaises.
too much | trop de (indénombrable) | Quantité | You put too much sugar in it. | Tu y as mis trop de sucre.
too many | trop de (dénombrable) | Quantité | There are too many cars downtown. | Il y a trop de voitures au centre-ville.
both | les deux | Quantité | Both my parents are teachers. | Mes deux parents sont professeurs.
each | chaque | Quantité | Each room has its own bathroom. | Chaque chambre a sa propre salle de bain.
another | un autre | Quantité | Can I have another cookie? | Je peux avoir un autre biscuit ?
""",
# Les nombres A2 (28 oct. 2026) : l'A1 compte dans les repères ; l'A2 passe aux
# ordinaux, aux centaines et aux fractions simples.
"zahlen": """
fifth | 5e, cinquième | Ordinaux | My office is on the fifth floor. | Mon bureau est au cinquième étage.
eighth | 8e, huitième | Ordinaux | Today is the eighth of June. | Aujourd'hui, c'est le 8 juin.
ninth | 9e, neuvième | Ordinaux | She finished ninth in the race. | Elle a fini neuvième de la course.
twelfth | 12e, douzième | Ordinaux | It's our twelfth wedding anniversary. | C'est notre douzième anniversaire de mariage.
twentieth | 20e, vingtième | Ordinaux | He was born in the twentieth century. | Il est né au vingtième siècle.
a hundred and fifty | 150 (cent cinquante) | Centaines | The ticket costs a hundred and fifty dollars. | Le billet coûte cent cinquante dollars.
two thousand | 2 000 (deux mille) | Milliers | The town has two thousand people. | La ville compte deux mille habitants.
one and a half | 1,5 (un et demi) | Fractions | The movie lasts one and a half hours. | Le film dure une heure et demie.
a couple of | deux, quelques | Quantités | I'll be back in a couple of minutes. | Je reviens dans deux minutes.
""",
},
"B1": {
"konjunktionen": """
unless | à moins que | Condition | We'll eat outside unless it rains. | Nous mangerons dehors à moins qu'il pleuve.
as long as | tant que, du moment que | Condition | You can stay as long as you're quiet. | Tu peux rester tant que tu es silencieux.
in case | au cas où | Condition | Take an umbrella in case it rains. | Prends un parapluie au cas où il pleuvrait.
whereas | alors que | Opposition | He loves the city, whereas she prefers the country. | Il adore la ville, alors qu'elle préfère la campagne.
even though | même si, bien que | Opposition | Even though I was tired, I went out. | Même si j'étais fatigué, je suis sorti.
so that | pour que, afin que | But | Speak slowly so that everyone understands. | Parle lentement pour que tout le monde comprenne.
since | puisque | Cause | Since you're here, you can help me. | Puisque tu es là, tu peux m'aider.
as | comme, puisque | Cause | As it was late, we took a taxi. | Comme il était tard, nous avons pris un taxi.
whether | si (alternative) | Liaison | I don't know whether he's coming. | Je ne sais pas s'il vient.
once | une fois que | Temps | Once you finish, call me. | Une fois que tu as fini, appelle-moi.
by (+ -ing) | en (+ participe présent) | Manière | You learn by making mistakes. | On apprend en faisant des erreurs.
as far as | autant que | Liaison | As far as I know, the store is open. | Autant que je sache, le magasin est ouvert.
now that | maintenant que | Cause | Now that you're here, we can start. | Maintenant que tu es là, nous pouvons commencer.
the more…, the more… | plus…, plus… | Comparaison | The more you read, the more you learn. | Plus tu lis, plus tu apprends.
whenever | chaque fois que | Temps | Call me whenever you need help. | Appelle-moi chaque fois que tu as besoin d'aide.
""",
"partikeln": """
you know | tu sais, tu vois | Oral | It's, you know, a bit expensive. | C'est, tu sais, un peu cher.
I mean | enfin, je veux dire | Oral | He's nice. I mean, he's not my best friend. | Il est gentil. Enfin, ce n'est pas mon meilleur ami.
kind of | un peu, plutôt | Oral | I'm kind of tired today. | Je suis un peu fatigué aujourd'hui.
sort of | en quelque sorte, à peu près | Oral | It's sort of a café and a bookstore. | C'est une sorte de café-librairie.
just | juste, simplement (pour adoucir) | Oral | I just wanted to say thank you. | Je voulais simplement te dire merci.
though | pourtant, quand même (en fin de phrase) | Oral | It's expensive. It's really good, though. | C'est cher. C'est vraiment bon, quand même.
""",
"zahlen": """
twenty-five thousand | 25 000 (vingt-cinq mille) | Grands nombres | The stadium holds twenty-five thousand people. | Le stade accueille vingt-cinq mille personnes.
a hundred thousand | 100 000 (cent mille) | Grands nombres | The town has a hundred thousand inhabitants. | La ville compte cent mille habitants.
a million | 1 000 000 (un million) | Grands nombres | The house costs a million dollars. | La maison coûte un million de dollars.
a billion | 1 000 000 000 (un milliard) — faux ami de « billion » | Grands nombres | The company is worth a billion dollars. | L'entreprise vaut un milliard de dollars.
nineteen eighty-four | 1984 — les années se lisent par paires | Années | She was born in nineteen eighty-four. | Elle est née en 1984.
twenty-first | 21e, vingt et unième | Ordinaux | We live in the twenty-first century. | Nous vivons au vingt et unième siècle.
thirtieth | 30e, trentième | Ordinaux | Today is my parents' thirtieth anniversary. | C'est aujourd'hui le trentième anniversaire de mariage de mes parents.
hundredth | 100e, centième | Ordinaux | It's the town's hundredth birthday. | C'est le centième anniversaire de la ville.
""",
"praepositionen": """
despite | malgré | Opposition | Despite the rain, we went for a walk. | Malgré la pluie, nous sommes allés nous promener.
unlike | contrairement à | Opposition | Unlike his brother, he loves sports. | Contrairement à son frère, il adore le sport.
among | parmi | Lieu | She's among the best students. | Elle est parmi les meilleures élèves.
beside | à côté de | Lieu | Come and sit beside me. | Viens t'asseoir à côté de moi.
as for | quant à | Liaison | As for me, I'm staying home. | Quant à moi, je reste à la maison.
except for | à l'exception de | Liaison | Everyone came except for Tom. | Tout le monde est venu à l'exception de Tom.
in spite of | en dépit de | Opposition | In spite of his age, he still runs every day. | Malgré son âge, il court encore tous les jours.
due to | en raison de | Cause | The flight was canceled due to fog. | Le vol a été annulé en raison du brouillard.
instead of | au lieu de | Manière | Let's walk instead of taking the bus. | Marchons au lieu de prendre le bus.
according to | selon | Liaison | According to the forecast, it will snow. | Selon la météo, il va neiger.
beyond | au-delà de | Lieu | The village is just beyond the hill. | Le village est juste après la colline.
within | dans (un délai), à l'intérieur de | Temps | Please reply within two days. | Merci de répondre sous deux jours.
apart from | à part | Liaison | Apart from Tom, everyone came. | À part Tom, tout le monde est venu.
""",
"pronomen": """
whose | dont, à qui | Relatifs | That's the man whose dog bit me. | C'est l'homme dont le chien m'a mordu.
whom | que, qui (soutenu) | Relatifs | The woman to whom I spoke was very kind. | La femme à qui j'ai parlé était très gentille.
whatever | quoi que, tout ce que | Indéfinis | Take whatever you want. | Prends tout ce que tu veux.
whoever | quiconque, qui que | Indéfinis | Whoever calls, tell them I'm out. | Qui que ce soit qui appelle, dis que je suis sorti.
anyone | n'importe qui, quelqu'un | Indéfinis | Anyone can learn to cook. | N'importe qui peut apprendre à cuisiner.
""",
"artikelwoerter": """
either | l'un ou l'autre | Quantité | You can take either bus. | Tu peux prendre l'un ou l'autre bus.
neither | aucun des deux | Quantité | Neither answer is correct. | Aucune des deux réponses n'est correcte.
several | plusieurs | Quantité | I've been there several times. | J'y suis allé plusieurs fois.
plenty of | plein de, largement | Quantité | We have plenty of time. | Nous avons largement le temps.
most | la plupart des | Quantité | Most people like music. | La plupart des gens aiment la musique.
""",
},
"B2": {
"konjunktionen": """
provided that | à condition que | Condition | You can borrow the car provided that you fill it up. | Tu peux emprunter la voiture à condition de faire le plein.
as though | comme si | Manière | He talks as though he knew everything. | Il parle comme s'il savait tout.
even if | même si | Opposition | I'll go even if it rains. | J'irai même s'il pleut.
so as to | afin de | But | Leave early so as to avoid the traffic. | Pars tôt afin d'éviter la circulation.
nevertheless | néanmoins | Opposition | It was risky; nevertheless, they did it. | C'était risqué ; néanmoins, ils l'ont fait.
therefore | par conséquent | Conséquence | The road was closed; therefore, we took the highway. | La route était fermée ; nous avons donc pris l'autoroute.
moreover | de plus | Ajout | The apartment is cheap. Moreover, it's near the subway. | L'appartement est bon marché. De plus, il est près du métro.
whereby | par lequel | Liaison | They signed an agreement whereby both sides share the costs. | Ils ont signé un accord par lequel les deux parties partagent les frais.
""",
"praepositionen": """
regarding | concernant | Liaison | I'm calling regarding your application. | J'appelle au sujet de votre candidature.
throughout | tout au long de, partout dans | Temps | It rained throughout the night. | Il a plu toute la nuit.
alongside | aux côtés de, le long de | Lieu | She worked alongside the best scientists. | Elle a travaillé aux côtés des meilleurs scientifiques.
via | par, via | Manière | We flew to Rome via London. | Nous sommes allés à Rome en passant par Londres.
amid | au milieu de, sur fond de | Lieu | The store closed amid rumors of bankruptcy. | Le magasin a fermé sur fond de rumeurs de faillite.
on behalf of | au nom de, de la part de | Liaison | I'm writing on behalf of my client. | J'écris au nom de mon client.
""",
"artikelwoerter": """
a great deal of | énormément de | Quantité | It took a great deal of effort. | Cela a demandé énormément d'efforts.
quite a few | pas mal de | Quantité | Quite a few people came to the meeting. | Pas mal de gens sont venus à la réunion.
hardly any | presque pas de | Quantité | There's hardly any milk left. | Il ne reste presque plus de lait.
a number of | un certain nombre de | Quantité | A number of students complained. | Un certain nombre d'élèves se sont plaints.
""",
},
"C1": {
"konjunktionen": """
inasmuch as | dans la mesure où | Cause | The plan failed, inasmuch as nobody followed it. | Le projet a échoué, dans la mesure où personne ne l'a suivi.
lest | de peur que | But | He wrote it down lest he forget. | Il l'a noté de peur de l'oublier.
no sooner… than | à peine… que | Temps | No sooner had I sat down than the phone rang. | À peine étais-je assis que le téléphone a sonné.
not only… but also | non seulement… mais aussi | Ajout | She speaks not only French but also Japanese. | Elle parle non seulement français, mais aussi japonais.
hence | d'où | Conséquence | The bridge was closed, hence the delay. | Le pont était fermé, d'où le retard.
""",
"praepositionen": """
notwithstanding | nonobstant, malgré | Opposition | Notwithstanding the rain, the parade went ahead. | Malgré la pluie, le défilé a eu lieu.
in light of | à la lumière de | Liaison | In light of the new facts, we changed our minds. | À la lumière des nouveaux faits, nous avons changé d'avis.
pursuant to | conformément à | Liaison | Pursuant to the contract, payment is due in May. | Conformément au contrat, le paiement est dû en mai.
by virtue of | en vertu de | Cause | He got the job by virtue of his experience. | Il a obtenu le poste en raison de son expérience.
in the wake of | à la suite de | Temps | Prices rose in the wake of the storm. | Les prix ont augmenté à la suite de la tempête.
with regard to | en ce qui concerne | Liaison | With regard to your question, the answer is yes. | En ce qui concerne votre question, la réponse est oui.
""",
"pronomen": """
whereby | par lequel | Relatifs | It's a system whereby everyone pays the same. | C'est un système selon lequel tout le monde paie la même chose.
whichever | quel que soit celui qui | Indéfinis | Take whichever seat you like. | Prends la place que tu veux.
""",
},
}
