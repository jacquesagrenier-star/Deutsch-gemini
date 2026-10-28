# -*- coding: utf-8 -*-
"""Tuiles « Ordre des mots » et « Adverbes » de l'anglais (28 oct. 2026) :
deux fiches neuves (elles vont aussi dans la liste des fiches) et leurs series.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

FICHES = [
{
"id": "ordre-des-mots", "niveau": "A2", "titre": "L'ordre des mots",
"resume": "Sujet, verbe, complément — et où placer always, not, very",
"regle": "La phrase anglaise suit presque toujours l'ordre <b>sujet + verbe + complément</b>, puis <b>lieu</b>, puis <b>temps</b> : <b>I met Anna at the café yesterday</b>. Rien ne s'intercale entre le verbe et son complément : <b>I like coffee very much</b> (jamais <i>I like very much coffee</i>). Les adverbes de fréquence (<b>always</b>, <b>often</b>, <b>never</b>) se placent <b>avant le verbe</b>, mais <b>après be</b> : <b>She always walks</b>, <b>She is always late</b>. Dans une question, l'auxiliaire passe devant le sujet (<b>Where do you live?</b>) ; dans une question <b>indirecte</b>, non (<b>Do you know where she lives?</b>).",
"tableau": [
 ["sujet + verbe + complément + lieu + temps", "l'ordre de base", "We had lunch in Salem on Sunday."],
 ["always, often, never + verbe", "fréquence avant le verbe", "He never drinks coffee."],
 ["be + always, often, never", "après be", "She's often tired."],
 ["auxiliaire + sujet + verbe ?", "question directe", "Where does he work?"],
 ["… where + sujet + verbe", "question indirecte", "Can you tell me where he works?"],
 ["opinion, taille, âge, couleur + nom", "l'ordre des adjectifs", "a nice big old red car"],
],
"exemples": [
 ["I really enjoyed the concert last night.", "J'ai vraiment aimé le concert hier soir."],
 ["Do you know what time it is?", "Sais-tu quelle heure il est ?"],
 ["She usually takes the bus to work.", "Elle prend habituellement l'autobus pour aller au travail."],
],
"attention": "Le français place souvent l'adverbe après le verbe (<i>je bois souvent du café</i>) ; l'anglais le met avant : <b>I often drink coffee</b>.",
"serie": "ordreDesMotsEnExercises", "kicker": "L'ordre des mots",
"questions": """
I ___ coffee in the morning. | always drink | drink always / always am drinking | Je bois toujours du café le matin. | Adverbe de fréquence avant le verbe.
She ___ late. | is never | never is / is late never | Elle n'est jamais en retard. | Après be : is never.
I enjoy ___. | jazz very much | very much coffee / much very coffee | J'aime beaucoup le jazz. | Rien entre le verbe et son complément.
We met ___. | at the café yesterday | yesterday at the café / at yesterday the café | Nous nous sommes rencontrés au café hier. | Lieu, puis temps.
Where ___ work? | does your sister | your sister does / your sister | Où travaille ta sœur ? | Question : auxiliaire + sujet + verbe.
Can you tell me where ___? | the station is | is the station / does the station is | Peux-tu me dire où est la gare ? | Question indirecte : sujet + verbe.
Do you know what time ___ now? | it is | is it / does it | Sais-tu quelle heure il est ? | Question indirecte : pas d'inversion.
She ___ to work by bike. | usually goes | goes usually / usually is going always | Elle va habituellement au travail à vélo. | Usually avant le verbe.
They ___ been to Canada. | have never | never have / have been never | Ils ne sont jamais allés au Canada. | Avec un auxiliaire : après le premier auxiliaire.
He speaks ___. | English very well | very well English / English well very | Il parle très bien anglais. | Complément d'abord, manière ensuite.
I ___ understand. | don't | not / no | Je ne comprends pas. | Négation : don't + verbe.
She bought ___. | a beautiful old wooden table | a wooden old beautiful table / an old beautiful wooden table | Elle a acheté une belle vieille table en bois. | Opinion, âge, matière.
He has ___. | a big black dog | a black big dog / a dog big black | Il a un gros chien noir. | Taille avant couleur.
What ___ at the weekend? | did you do | you did / did you did | Qu'as-tu fait pendant la fin de semaine ? | Did + sujet + verbe nu.
I wonder where ___. | he went | did he go / went he | Je me demande où il est allé. | Question indirecte : sujet + verbe.
Why ___ so sad? | are you | you are / do you | Pourquoi es-tu si triste ? | Avec be : be + sujet.
I can ___ swim. | also | too also / as well | Je sais aussi nager. | Also avant le verbe principal.
I can swim ___. | too | also / either | Je sais nager aussi. | Too en fin de phrase.
She ___ at home on Sundays. | is usually | usually is / is at home usually | Elle est d'habitude à la maison le dimanche. | Après be.
Who ___ the window? | broke | did break / did broke | Qui a cassé la fenêtre ? | Who sujet : pas de did.
Who ___ you call? | did | does / was | Qui as-tu appelé ? | Who complément : did.
I ___ him yesterday. | saw | yesterday saw / have yesterday seen | Je l'ai vu hier. | Temps en fin de phrase.
It's ___ to walk at night. | not safe | safe not / no safe | Ce n'est pas sûr de marcher la nuit. | Not après be.
Please ___ the door. | don't open | not open / open not | N'ouvre pas la porte, s'il te plaît. | Impératif négatif : don't + verbe.
She gave ___. | me the keys | the keys me / to me the keys | Elle m'a donné les clés. | Personne, puis chose (ou the keys to me).
""",
},
{
"id": "adverbes", "niveau": "A2", "titre": "Les adverbes",
"resume": "quickly, well, always, here — dire comment, quand, où, combien",
"regle": "L'adverbe dit <b>comment</b> (manière : <b>slowly</b>, <b>well</b>), <b>quand</b> (temps : <b>now</b>, <b>yesterday</b>), <b>combien de fois</b> (fréquence : <b>always</b>, <b>sometimes</b>), <b>où</b> (lieu : <b>here</b>, <b>outside</b>) ou <b>à quel point</b> (degré : <b>very</b>, <b>quite</b>). Beaucoup se forment avec <b>-ly</b> sur l'adjectif : <b>quick → quickly</b>, <b>happy → happily</b>, <b>careful → carefully</b>. Quelques-uns sont irréguliers : <b>good → well</b>, <b>fast → fast</b>, <b>hard → hard</b> (<b>hardly</b> veut dire « à peine »).",
"tableau": [
 ["adjectif + -ly", "manière", "slow → slowly, careful → carefully"],
 ["-y → -ily", "orthographe", "easy → easily, happy → happily"],
 ["good → well", "irrégulier", "She sings well."],
 ["fast, hard, late", "même forme", "He works hard. (hardly = à peine)"],
 ["always, often, never", "fréquence", "I never smoke."],
 ["very, quite, too", "degré", "It's too hot."],
],
"exemples": [
 ["Please drive carefully.", "Conduis prudemment, s'il te plaît."],
 ["She speaks English very well.", "Elle parle très bien anglais."],
 ["I hardly slept last night.", "J'ai à peine dormi la nuit dernière."],
],
"attention": "Après be, seem, look, feel, on garde l'<b>adjectif</b> : <b>You look tired</b>, <b>It feels soft</b> (jamais <i>tiredly</i>, <i>softly</i>).",
"serie": "adverbesEnExercises", "kicker": "Les adverbes",
"questions": """
Please drive ___. | carefully | careful / carefuly | Conduis prudemment, s'il te plaît. | Careful → carefully.
She speaks English very ___. | well | good / goodly | Elle parle très bien anglais. | Good → well.
He's a ___ driver. | careful | carefully / carefuly | C'est un conducteur prudent. | Devant un nom : adjectif.
He runs very ___. | fast | fastly / faster than | Il court très vite. | Fast : même forme.
She works ___. She never stops. | hard | hardly / hardy | Elle travaille dur. Elle ne s'arrête jamais. | Hard = dur.
I ___ slept last night. I'm exhausted. | hardly | hard / hardily | J'ai à peine dormi la nuit dernière. Je suis épuisé. | Hardly = à peine.
The test was ___ easy. | surprisingly | surprising / surprise | L'examen était étonnamment facile. | Adverbe devant un adjectif.
She smiled ___. | happily | happyly / happy | Elle a souri joyeusement. | -y → -ily.
I can do it ___. | easily | easyly / easy | Je peux le faire facilement. | Easy → easily.
You look ___. | tired | tiredly / tire | Tu as l'air fatigué. | Après look : adjectif.
This soup tastes ___. | delicious | deliciously / delicious-ly | Cette soupe est délicieuse. | Après taste : adjectif.
He arrived ___ again. | late | lately / latest | Il est encore arrivé en retard. | Late = en retard.
I haven't seen her ___. | lately | late / latest | Je ne l'ai pas vue ces derniers temps. | Lately = récemment.
Speak ___, the baby is sleeping. | quietly | quiet / quite | Parle doucement, le bébé dort. | Quiet → quietly.
It's ___ cold today. | quite | quiet / quietly | Il fait assez froid aujourd'hui. | Quite = assez, plutôt.
She ___ forgets her keys. | often | oft / oftenly | Elle oublie souvent ses clés. | Fréquence avant le verbe.
I'll do it ___. | later | lately / late | Je le ferai plus tard. | Plus tard = later.
Come ___! | here | hear / there here | Viens ici ! | Lieu : here.
The kids are playing ___. | outside | outsides / out of | Les enfants jouent dehors. | Lieu : outside.
It's ___ hot to go running. | too | to / two | Il fait trop chaud pour aller courir. | Too = trop.
She sings ___ beautifully. | really | real / reallyly | Elle chante vraiment magnifiquement. | Really devant un adverbe.
He answered ___. | correctly | correct / correctely | Il a répondu correctement. | Correct → correctly.
They lived ___ ever after. | happily | happy / happyly | Ils vécurent heureux pour toujours. | Happily ever after.
I ___ agree with you. | completely | complete / completly | Je suis entièrement d'accord avec toi. | Complete → completely.
She's ___ intelligent. | extremely | extreme / extremly | Elle est extrêmement intelligente. | Extreme → extremely.
""",
},
]

Q = {
"placeAdverbesEnExercises": """
We ___ eat out on Fridays. | often | are often / eat often out | Nous mangeons souvent au restaurant le vendredi. | Avant le verbe.
He ___ home before six. | is never | never is / is home never | Il n'est jamais à la maison avant six heures. | Après be.
I have ___ seen the ocean. | never | ever / not never | Je n'ai jamais vu l'océan. | Entre l'auxiliaire et le participe.
Have you ___ been to Boston? | ever | never / already ever | Es-tu déjà allé à Boston ? | Ever dans la question.
She ___ goes to the gym. | sometimes | some times / is sometimes | Elle va parfois au gym. | Avant le verbe.
___, I'm tired. | Sometimes | Some time / Ever | Parfois, je suis fatigué. | Sometimes peut ouvrir la phrase.
They ___ answer their phone. | rarely | are rarely / rare | Ils répondent rarement au téléphone. | Avant le verbe.
I ___ forget your birthday. | will never | never will / will forget never | Je n'oublierai jamais ton anniversaire. | Après will.
She ___ late for work. | is always | always is / is late always | Elle est toujours en retard au travail. | Après be.
You ___ be careful. | should always | always should / should be always careful | Tu devrais toujours faire attention. | Après le modal.
I ___ have breakfast at seven. | usually | am usually / have usually | Je déjeune habituellement à sept heures. | Avant le verbe.
He ___ been here before. | has already | already has / has been already | Il est déjà venu ici. | Already entre l'auxiliaire et le participe.
I don't ___ eat meat. | often | ever often / never | Je ne mange pas souvent de viande. | Don't + often + verbe.
We go to the beach ___. | every summer | summer every / each summers | Nous allons à la plage chaque été. | Expressions longues : en fin de phrase.
I ___ walk to work. | sometimes | some time / am sometimes | Je vais parfois au travail à pied. | Avant le verbe.
She ___ angry. | rarely gets | gets rarely / rarely is getting | Elle se fâche rarement. | Avant le verbe principal.
Do you ___ cook at home? | often | oft / often do | Cuisines-tu souvent à la maison ? | Question : après le sujet.
I ___ there. | have never been | never have been / have been never | Je n'y suis jamais allé. | Have + never + participe.
They ___ happy together. | always seem | seem always / are always seem | Ils ont toujours l'air heureux ensemble. | Avant le verbe (seem n'est pas be).
I ___ finished. | 've just | just 've / 've finished just | Je viens de finir. | Just entre l'auxiliaire et le participe.
""",

"questionsIndirectesEnExercises": """
Excuse me, where ___? | is the bathroom | the bathroom is / does the bathroom | Où sont les toilettes ? | Question directe avec be : be + sujet.
Could you tell me where ___? | the bathroom is | is the bathroom / the bathroom does | Pourriez-vous me dire où sont les toilettes ? | Question indirecte : sujet + verbe.
What time ___ the store open? | does | is / do | À quelle heure ouvre le magasin ? | Does + sujet + verbe nu.
Do you know what time ___? | the store opens | does the store open / the store does open | Savez-vous à quelle heure ouvre le magasin ? | Indirecte : sujet + verbe conjugué.
How old ___? | is she | she is / does she | Quel âge a-t-elle ? | Be + sujet.
I don't know how old ___. | she is | is she / does she | Je ne sais pas quel âge elle a. | Indirecte : sujet + verbe.
Why ___ leave so early? | did he | he did / he | Pourquoi est-il parti si tôt ? | Did + sujet + verbe nu.
I wonder why ___ so early. | he left | did he leave / he did leave | Je me demande pourquoi il est parti si tôt. | Indirecte : sujet + verbe au passé.
What ___ want? | do you | you / are you | Que veux-tu ? | Do + sujet + verbe.
Tell me what ___. | you want | do you want / want you | Dis-moi ce que tu veux. | Indirecte : sujet + verbe.
Is he coming? → I don't know ___ he's coming. | if | that / what | Est-ce qu'il vient ? → Je ne sais pas s'il vient. | Oui/non indirecte : if (ou whether).
Can you swim? → She asked me ___ I could swim. | if | that / what | Sais-tu nager ? → Elle m'a demandé si je savais nager. | If + sujet + verbe.
How much ___? | does it cost | it costs / it does cost | Combien ça coûte ? | Does + sujet + verbe nu.
Do you know how much ___? | it costs | does it cost / costs it | Savez-vous combien ça coûte ? | Indirecte : sujet + verbe.
Where ___ live? | does she | she does / is she | Où habite-t-elle ? | Does + sujet + verbe nu.
I have no idea where ___. | she lives | does she live / lives she | Je n'ai aucune idée de l'endroit où elle habite. | Indirecte.
Who ___ to? | were you talking | you were talking / talking you were | À qui parlais-tu ? | Préposition en fin de question.
What ___ about? | is the book | the book is / does the book | De quoi parle le livre ? | Be + sujet, préposition à la fin.
Can you remember where ___ the car? | you parked | did you park / parked you | Te souviens-tu où tu as garé la voiture ? | Indirecte : sujet + verbe.
Which bus ___ to Harvard? | goes | does go / is going it | Quel autobus va à Harvard ? | Which bus est sujet : pas de does.
""",

"adverbesFamilleEnExercises": """
« always » est un adverbe de ___ | fréquence | manière / lieu | always = toujours. | Combien de fois ? → fréquence.
« slowly » est un adverbe de ___ | manière | temps / degré | slowly = lentement. | Comment ? → manière.
« yesterday » est un adverbe de ___ | temps | lieu / fréquence | yesterday = hier. | Quand ? → temps.
« here » est un adverbe de ___ | lieu | temps / manière | here = ici. | Où ? → lieu.
« very » est un adverbe de ___ | degré | manière / fréquence | very = très. | À quel point ? → degré.
« sometimes » est un adverbe de ___ | fréquence | temps / lieu | sometimes = parfois. | Fréquence.
« carefully » est un adverbe de ___ | manière | degré / lieu | carefully = prudemment. | Manière.
« soon » est un adverbe de ___ | temps | lieu / degré | soon = bientôt. | Temps.
« outside » est un adverbe de ___ | lieu | manière / temps | outside = dehors. | Lieu.
« quite » est un adverbe de ___ | degré | fréquence / manière | quite = assez, plutôt. | Degré.
« never » est un adverbe de ___ | fréquence | degré / temps | never = jamais. | Fréquence.
« well » est un adverbe de ___ | manière | degré / lieu | well = bien. | Manière.
« already » est un adverbe de ___ | temps | fréquence / manière | already = déjà. | Temps.
« everywhere » est un adverbe de ___ | lieu | fréquence / degré | everywhere = partout. | Lieu.
« too » (too hot) est un adverbe de ___ | degré | manière / lieu | too = trop. | Degré.
« often » est un adverbe de ___ | fréquence | manière / temps | often = souvent. | Fréquence.
« quickly » est un adverbe de ___ | manière | temps / degré | quickly = vite. | Manière.
« tomorrow » est un adverbe de ___ | temps | lieu / fréquence | tomorrow = demain. | Temps.
« upstairs » est un adverbe de ___ | lieu | degré / temps | upstairs = en haut, à l'étage. | Lieu.
« almost » est un adverbe de ___ | degré | fréquence / lieu | almost = presque. | Degré.
« rarely » est un adverbe de ___ | fréquence | manière / lieu | rarely = rarement. | Fréquence.
« hard » (work hard) est un adverbe de ___ | manière | degré / temps | hard = dur, avec effort. | Manière.
« recently » est un adverbe de ___ | temps | fréquence / lieu | recently = récemment. | Temps.
« nearby » est un adverbe de ___ | lieu | temps / degré | nearby = tout près. | Lieu.
« extremely » est un adverbe de ___ | degré | manière / fréquence | extremely = extrêmement. | Degré.
""",
}
