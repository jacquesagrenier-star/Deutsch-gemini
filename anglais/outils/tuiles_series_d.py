# -*- coding: utf-8 -*-
"""Questions ajoutees aux tuiles « Connecteurs » et « Ordre des mots » (28 oct. 2026),
pour approcher les panneaux allemands (15 options pour les connecteurs).
Format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

Q = {
"relierPhrasesEnExercises": """
It was raining. We went out. → ___ it was raining, we went out. | Although | Because / So | Il pleuvait. Nous sommes sortis. → Bien qu'il pleuve, nous sommes sortis. | Contraste : although.
I was hungry. I made a sandwich. → I was hungry, ___ I made a sandwich. | so | but / although | J'avais faim. Je me suis fait un sandwich. → J'avais faim, alors je me suis fait un sandwich. | Conséquence : so.
She missed the bus. She was late. → She was late ___ she missed the bus. | because | although / so | Elle a raté l'autobus. Elle était en retard. → Elle était en retard parce qu'elle avait raté l'autobus. | Cause : because.
He's rich. He's not happy. → He's rich, ___ he's not happy. | but | so / because | Il est riche. Il n'est pas heureux. → Il est riche, mais il n'est pas heureux. | Contraste : but.
Finish your homework. Then you can play. → You can play ___ you finish your homework. | after | before / unless | Finis tes devoirs. Ensuite tu pourras jouer. → Tu pourras jouer après avoir fini tes devoirs. | Après = after.
Take a coat. It might get cold. → Take a coat ___ it gets cold. | in case | unless / so that | Prends un manteau. Il pourrait faire froid. → Prends un manteau au cas où il ferait froid. | Au cas où = in case.
You must hurry. Otherwise you'll be late. → You'll be late ___ you hurry. | unless | if / when | Dépêche-toi, sinon tu seras en retard. → Tu seras en retard à moins de te dépêcher. | Unless = sauf si.
I'll call you. I'll arrive. → I'll call you ___ I arrive. | as soon as | as long as / although | Je t'appellerai. J'arriverai. → Je t'appellerai dès que j'arriverai. | Dès que = as soon as.
I like tea. My wife likes coffee. → I like tea, ___ my wife likes coffee. | whereas | so / because | J'aime le thé. Ma femme aime le café. → J'aime le thé, alors que ma femme aime le café. | Opposition : whereas.
He studied hard. He wanted to pass. → He studied hard ___ he could pass. | so that | because of / although | Il a beaucoup étudié. Il voulait réussir. → Il a beaucoup étudié pour pouvoir réussir. | But : so that.
She was cooking. The phone rang. → The phone rang ___ she was cooking. | while | during / until | Elle cuisinait. Le téléphone a sonné. → Le téléphone a sonné pendant qu'elle cuisinait. | Pendant que = while.
It was cold. We stayed inside. → It was ___ cold that we stayed inside. | so | such / too | Il faisait froid. Nous sommes restés dedans. → Il faisait si froid que nous sommes restés dedans. | So + adjectif + that.
It was a long trip. We were exhausted. → It was ___ a long trip that we were exhausted. | such | so / too | Le voyage était long. Nous étions épuisés. → C'était un si long voyage que nous étions épuisés. | Such + a + nom + that.
He didn't call. He didn't write. → He ___ called nor wrote. | neither | either / not | Il n'a pas appelé. Il n'a pas écrit. → Il n'a ni appelé ni écrit. | Neither … nor.
We can take the train. We can drive. → We can ___ take the train or drive. | either | neither / both | Nous pouvons prendre le train. Nous pouvons conduire. → Nous pouvons soit prendre le train, soit conduire. | Either … or.
She speaks French. She speaks Spanish. → She speaks ___ French and Spanish. | both | either / neither | Elle parle français. Elle parle espagnol. → Elle parle à la fois français et espagnol. | Both … and.
I'll wait. You'll come back. → I'll wait ___ you come back. | until | by / while | J'attendrai. Tu reviendras. → J'attendrai jusqu'à ce que tu reviennes. | Jusqu'à ce que = until.
The store was closed. We went home. → The store was closed. ___, we went home. | Therefore | However / Although | Le magasin était fermé. Nous sommes rentrés. → Le magasin était fermé. Nous sommes donc rentrés. | Conséquence (soutenu) : therefore.
The hotel was cheap. It was very clean. → The hotel was cheap. ___, it was very clean. | Moreover | However / Otherwise | L'hôtel était bon marché. Il était très propre. → L'hôtel était bon marché. De plus, il était très propre. | Addition : moreover.
It's late. Let's go home. → ___ it's late, let's go home. | Since | Although / Unless | Il est tard. Rentrons. → Puisqu'il est tard, rentrons. | Puisque = since.
""",

"direAutrementEnExercises": """
Although it was raining, we went out. = ___ the rain, we went out. | Despite | Although / Because of | Bien qu'il pleuvait, nous sommes sortis. = Malgré la pluie, nous sommes sortis. | Despite + nom.
Despite her age, she runs every day. = ___ she's old, she runs every day. | Although | Despite / Because | Malgré son âge, elle court tous les jours. = Bien qu'elle soit âgée, elle court tous les jours. | Although + proposition.
We stayed home because of the storm. = We stayed home ___ there was a storm. | because | because of / despite | Nous sommes restés à la maison à cause de la tempête. = … parce qu'il y avait une tempête. | Because + proposition.
He left early because he was tired. = He left early ___ his tiredness. | because of | because / although | Il est parti tôt parce qu'il était fatigué. = … à cause de sa fatigue. | Because of + nom.
If you don't hurry, you'll miss the bus. = ___ you hurry, you'll miss the bus. | Unless | If / Although | Si tu ne te dépêches pas, tu vas rater l'autobus. = À moins de te dépêcher, … | Unless = if … not.
She studied hard, so she passed. = She passed ___ she studied hard. | because | so / although | Elle a beaucoup étudié, alors elle a réussi. = Elle a réussi parce qu'elle a beaucoup étudié. | Cause : because.
He's tired, but he keeps working. = ___ he's tired, he keeps working. | Even though | Because / So | Il est fatigué, mais il continue à travailler. = Même s'il est fatigué, il continue. | Even though.
It was very cold, so we stayed in. = It was ___ cold that we stayed in. | so | such / very | Il faisait très froid, alors nous sommes restés à l'intérieur. = Il faisait si froid que … | So … that.
I went to bed early because I wanted to be rested. = I went to bed early ___ be rested. | in order to | because to / so that to | Je me suis couché tôt parce que je voulais être reposé. = … pour être reposé. | But : in order to + verbe.
She saved money in order to buy a car. = She saved money ___ she could buy a car. | so that | in order / because | Elle a économisé pour acheter une voiture. = … pour pouvoir acheter une voiture. | So that + proposition.
After he finished dinner, he went out. = After ___ dinner, he went out. | finishing | he finish / to finish | Après avoir fini de souper, il est sorti. | After + -ing.
Before she left, she locked the door. = Before ___, she locked the door. | leaving | she leaving / to leave | Avant de partir, elle a verrouillé la porte. | Before + -ing.
While I was walking home, I saw Tom. = ___ home, I saw Tom. | Walking | Walked / To walk | En rentrant à pied, j'ai vu Tom. | Participe présent : action simultanée.
The movie was boring, but we stayed. = ___ the movie was boring, we stayed. | Although | Because / So | Le film était ennuyeux, mais nous sommes restés. = Bien que le film soit ennuyeux, … | Although.
In spite of the traffic, we arrived on time. = ___ there was traffic, we arrived on time. | Even though | In spite / Despite | Malgré la circulation, nous sommes arrivés à l'heure. = Même s'il y avait de la circulation, … | Proposition : even though.
He didn't come because he was sick. = He was sick, ___ he didn't come. | so | because / although | Il n'est pas venu parce qu'il était malade. = Il était malade, alors il n'est pas venu. | Conséquence : so.
You can borrow it if you bring it back. = You can borrow it ___ you bring it back. | as long as | unless / although | Tu peux l'emprunter si tu le rapportes. = … à condition de le rapporter. | As long as = à condition que.
I'll go even if it rains. = I'll go ___ it rains or not. | whether | if / unless | J'irai même s'il pleut. = J'irai, qu'il pleuve ou non. | Whether … or not.
""",

"asLikeEnExercises": """
She sings ___ an angel. | like | as / as if | Elle chante comme un ange. | Like + nom : comparaison.
He works ___ a nurse at the hospital. | as | like / as a like | Il travaille comme infirmier à l'hôpital. | As = en tant que (fonction réelle).
___ I said, the store is closed. | As | Like / Such as | Comme je l'ai dit, le magasin est fermé. | As + proposition (soutenu).
It looks ___ rain. | like | as / as if it | On dirait qu'il va pleuvoir. | Look like + nom.
It looks ___ it's going to rain. | as if | like as / as like | On dirait qu'il va pleuvoir. | Look as if + proposition.
Do ___ you're told! | as | like as / such as | Fais ce qu'on te dit ! | Do as you're told (expression).
He talks ___ he knew everything. | as if | like as / so as | Il parle comme s'il savait tout. | As if + proposition.
I used my coat ___ a pillow. | as | like / such | J'ai utilisé mon manteau comme oreiller. | As = en guise de.
She's tall, ___ her mother. | like | as / as if | Elle est grande, comme sa mère. | Like + nom.
___ a teacher, I hear that question every day. | As | Like / Such as | En tant qu'enseignant, j'entends cette question tous les jours. | As = en tant que.
I like fruit, ___ apples and bananas. | such as | as / like as | J'aime les fruits, comme les pommes et les bananes. | Exemples : such as (ou like).
She's not ___ tall as her sister. | as | so as / like | Elle n'est pas aussi grande que sa sœur. | As … as.
He looks just ___ his father. | like | as / as if | Il ressemble tout à fait à son père. | Look like = ressembler à.
Leave everything ___ it is. | as | like / such as | Laisse tout comme c'est. | As + proposition.
___ usual, he was late. | As | Like / As if | Comme d'habitude, il était en retard. | Expression : as usual.
It feels ___ silk. | like | as / such as | Ça a la douceur de la soie. | Feel like + nom.
""",

"sinceAsForEnExercises": """
I've lived here ___ 2015. | since | as / for | J'habite ici depuis 2015. | Temps, point de départ : since.
___ you're already up, can you make coffee? | Since | Since that / For | Puisque tu es déjà levé, peux-tu faire du café ? | Cause : since = puisque.
I've been waiting ___ an hour. | for | since / as | J'attends depuis une heure. | Durée : for.
___ it was late, we took a taxi. | As | Like / For | Comme il était tard, nous avons pris un taxi. | Cause : as = comme.
We stayed inside, ___ it was raining hard. | for | since that / like | Nous sommes restés à l'intérieur, car il pleuvait fort. | Cause (littéraire) : for, après une virgule.
She hasn't called ___ Monday. | since | for / as | Elle n'a pas appelé depuis lundi. | Point de départ : since.
___ he grew older, he became wiser. | As | Since / For | En vieillissant, il est devenu plus sage. | As = à mesure que.
___ I don't have a car, I take the bus. | Since | For / Like | Comme je n'ai pas de voiture, je prends l'autobus. | Cause : since.
They've been married ___ thirty years. | for | since / as | Ils sont mariés depuis trente ans. | Durée : for.
___ she was leaving, the phone rang. | As | For / Since | Au moment où elle partait, le téléphone a sonné. | As = au moment où.
It's been years ___ I last saw him. | since | for / as | Ça fait des années que je ne l'ai pas vu. | It's been … since.
I'll go first, ___ I know the way. | since | for that / like | Je passe devant, puisque je connais le chemin. | Cause : since.
He's been sick ___ last week. | since | for / as | Il est malade depuis la semaine dernière. | Point de départ : since.
___ you know, the meeting is canceled. | As | Like / Since | Comme tu le sais, la réunion est annulée. | As you know.
We talked ___ hours. | for | since / as | Nous avons parlé pendant des heures. | Durée : for.
""",

"ordreAdjectifsEnExercises": """
She has ___. | a beautiful long dress | a long beautiful dress / a dress long beautiful | Elle a une belle robe longue. | Opinion avant taille.
They live in ___. | a big old house | an old big house / a house big old | Ils habitent une grande vieille maison. | Taille avant âge.
He bought ___. | a new red car | a red new car / a car new red | Il a acheté une nouvelle voiture rouge. | Âge avant couleur.
I want ___. | a small round table | a round small table / a table round small | Je veux une petite table ronde. | Taille avant forme.
She wore ___. | a lovely white cotton shirt | a cotton white lovely shirt / a white lovely cotton shirt | Elle portait une jolie chemise blanche en coton. | Opinion, couleur, matière.
We ate at ___. | a nice little Italian restaurant | an Italian little nice restaurant / a little nice Italian restaurant | Nous avons mangé dans un charmant petit restaurant italien. | Opinion, taille, origine.
Our neighbors have ___. | two big black dogs | big two black dogs / two black big dogs | Nos voisins ont deux gros chiens noirs. | Le nombre en premier.
It's ___. | an old wooden bridge | a wooden old bridge / an bridge old wooden | C'est un vieux pont en bois. | Âge avant matière.
My aunt bought ___. | a beautiful leather bag | a leather beautiful bag / a bag beautiful leather | Ma tante a acheté un beau sac en cuir. | Opinion avant matière.
He drives ___. | a fast German car | a German fast car / a car fast German | Il conduit une voiture allemande rapide. | Qualité avant origine.
They have ___. | a cute little puppy | a little cute puppy / a puppy cute little | Ils ont un adorable petit chiot. | Opinion avant taille.
I found ___. | an old French coin | a French old coin / an coin old French | J'ai trouvé une vieille pièce française. | Âge avant origine.
She lives in ___. | a tall modern building | a modern tall building / a building tall modern | Elle habite un grand immeuble moderne. | Taille avant âge.
We need ___. | a large square box | a square large box / a box large square | Il nous faut une grande boîte carrée. | Taille avant forme.
He gave me ___. | a nice blue wool sweater | a wool blue nice sweater / a blue nice wool sweater | Il m'a donné un joli chandail bleu en laine. | Opinion, couleur, matière.
It was ___. | a long hot summer | a hot long summer / a summer long hot | Ce fut un long été chaud. | Taille ou durée avant température.
""",

"placeNotEnExercises": """
I ___ like spinach. | don't | not / no | Je n'aime pas les épinards. | Présent : don't + verbe.
She ___ coming tonight. | isn't | doesn't / not | Elle ne vient pas ce soir. | Be + not + -ing.
They ___ finished yet. | haven't | didn't / don't | Ils n'ont pas encore fini. | Have + not + participe.
He ___ swim. | can't | doesn't can / not can | Il ne sait pas nager. | Modal + not.
We ___ go to the party last night. | didn't | weren't / don't | Nous ne sommes pas allés à la fête hier soir. | Passé : didn't + verbe nu.
I told him ___ to worry. | not | don't / no | Je lui ai dit de ne pas s'inquiéter. | Infinitif négatif : not to.
Try ___ to be late. | not | don't / no | Essaie de ne pas être en retard. | Not to + verbe.
I hope ___. | not | don't / no | J'espère que non. | I hope not.
___ everyone likes jazz. | Not | No / Don't | Ce n'est pas tout le monde qui aime le jazz. | Not + everyone.
I have ___ money. | no | not / don't | Je n'ai pas d'argent. | No + nom = pas de.
I don't have ___ money. | any | no / none | Je n'ai pas d'argent. | Don't … any.
There's ___ milk left. | no | not / none of | Il ne reste plus de lait. | No + nom.
___ of my friends came. | None | No / Not | Aucun de mes amis n'est venu. | None of = aucun de.
She ___ never been to Paris. | has | hasn't / doesn't | Elle n'est jamais allée à Paris. | Never suffit : une seule négation.
I ___ anything. | didn't see | didn't see nothing / saw not | Je n'ai rien vu. | Une seule négation : didn't … anything.
I saw ___. | nothing | anything / not nothing | Je n'ai rien vu. | Une seule négation : nothing.
___ you coming? | Aren't | Don't / Not | Tu ne viens pas ? | Question négative : Aren't you…?
Why ___ you call me? | didn't | not / don't did | Pourquoi tu ne m'as pas appelé ? | Why didn't you…?
It's ___ a good idea. | not | no / don't | Ce n'est pas une bonne idée. | Be + not.
He ___ to work on Fridays. | doesn't go | don't go / not goes | Il ne va pas travailler le vendredi. | Doesn't + verbe nu.
""",
}
