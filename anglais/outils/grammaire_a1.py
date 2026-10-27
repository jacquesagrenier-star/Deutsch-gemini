# -*- coding: utf-8 -*-
"""Les fiches de grammaire A1 de l'anglais, en francais, et leurs series.

SOURCE : on corrige ici, puis python anglais/outils/construire.py ecrit
anglais/datos/grammaire.json et anglais/datos/exercices.json (communs a
l'americain et au britannique : les phrases evitent les mots qui different).

Une fiche : id, titre, resume, regle (HTML : <b> seulement), tableau (forme,
explication, exemple), exemples (anglais, francais), attention, et sa serie.
Une question de serie : « phrase avec ___ | bonne reponse | mauvaise 1 /
mauvaise 2 | traduction | explication ».
"""

FICHES = [
{
"id": "be", "titre": "To be : être", "resume": "I am, you are, he is",
"regle": "<b>To be</b> (être) est le verbe le plus utilisé, et il est irrégulier : <b>I am</b>, <b>you are</b>, <b>he / she / it is</b>, <b>we / you / they are</b>. À l'oral, on le contracte presque toujours : <b>I'm</b>, <b>you're</b>, <b>he's</b>. La négation se colle derrière : <b>I'm not</b>, <b>he isn't</b>, <b>they aren't</b>. Pour poser une question, on passe le verbe devant : <b>Are you tired?</b>",
"tableau": [
 ["I am · I'm", "je suis", "I'm a student."],
 ["you are · you're", "tu es, vous êtes", "You're late!"],
 ["he / she / it is · he's", "il / elle est", "She's my sister."],
 ["we / they are · we're", "nous sommes, ils sont", "We're from Quebec."],
 ["isn't · aren't", "négation", "He isn't here. They aren't ready."],
 ["Are you…? · Is she…?", "question", "Is it cold today?"],
],
"exemples": [
 ["I'm hungry.", "J'ai faim."],
 ["How old are you? — I'm twenty.", "Quel âge as-tu ? — J'ai vingt ans."],
 ["Is your brother a teacher?", "Ton frère est professeur ?"],
],
"attention": "Avoir faim, soif, froid, peur, vingt ans : en anglais, on <b>est</b> affamé, assoiffé… <b>I'm hungry</b>, <b>I'm cold</b>, <b>I'm afraid</b>, <b>I'm twenty</b>. Jamais <i>I have twenty years</i>.",
"serie": "beEnExercises", "kicker": "To be : être",
"questions": """
I ___ a student. | am | is / are | Je suis étudiant. | I + am.
She ___ my sister. | is | am / are | C'est ma sœur. | He, she, it + is.
They ___ from Canada. | are | is / am | Ils viennent du Canada. | We, you, they + are.
We ___ very tired today. | are | is / am | Nous sommes très fatigués aujourd'hui. | We + are.
It ___ cold this morning. | is | are / am | Il fait froid ce matin. | It + is : la météo passe par « it is ».
You ___ late! | are | is / am | Tu es en retard ! | You + are, au singulier comme au pluriel.
___ you hungry? | Are | Is / Do | Tu as faim ? | La question passe le verbe devant : Are you…?
___ he your brother? | Is | Are / Does | C'est ton frère ? | Is he…? — pas de do avec be.
I'm twenty ___ old. | years | year / age | J'ai vingt ans. | On EST vingt ans : I'm twenty (years old).
He ___ not at home. | is | are / does | Il n'est pas à la maison. | La négation suit be : he is not, he isn't.
My parents ___ teachers. | are | is / am | Mes parents sont professeurs. | Un sujet pluriel prend are.
I ___ cold, can you close the window? | am | have / is | J'ai froid, tu peux fermer la fenêtre ? | Avoir froid = be cold.
"""
},
{
"id": "articles", "titre": "A, an, the", "resume": "Un, une, le, la — et quand ne rien mettre",
"regle": "<b>A</b> devant un son consonne, <b>an</b> devant un son voyelle : c'est le <b>son</b> qui compte, pas la lettre (<b>an hour</b>, <b>a university</b>). <b>The</b> vaut pour le, la et les : il ne change jamais. Et souvent l'anglais ne met <b>rien</b> là où le français met « le » : pour parler d'une chose en général (<b>I like music</b>), devant les repas, les langues, les jours.",
"tableau": [
 ["a", "un, une (son consonne)", "a book, a car, a university"],
 ["an", "un, une (son voyelle)", "an apple, an egg, an hour"],
 ["the", "le, la, les", "the book, the books"],
 ["(rien)", "en général", "I love cats. Dogs are friendly."],
 ["(rien)", "repas, langues, jours", "I have lunch at noon. I speak English. See you on Monday."],
],
"exemples": [
 ["She's a nurse.", "Elle est infirmière."],
 ["I eat an apple every day.", "Je mange une pomme tous les jours."],
 ["I like music.", "J'aime la musique."],
],
"attention": "Un métier prend <b>a</b> : <b>She's a doctor</b> (et non <i>She's doctor</i>), alors que le français dit « elle est médecin ».",
"serie": "articlesEnExercises", "kicker": "A, an, the",
"questions": """
I have ___ dog. | a | an / the | J'ai un chien. | Son consonne : a.
She eats ___ apple. | an | a / the | Elle mange une pomme. | Son voyelle : an.
We waited for ___ hour. | an | a / the | Nous avons attendu une heure. | Le h ne se prononce pas : an hour.
He's ___ engineer. | an | a / the | Il est ingénieur. | Un métier prend a / an ; ici son voyelle.
My sister is ___ teacher. | a | an / the | Ma sœur est professeur. | Un métier prend toujours un article.
Close ___ door, please. | the | a / an | Ferme la porte, s'il te plaît. | Une porte précise : the.
I like ___. | music | the music / a music | J'aime la musique. | En général : pas d'article.
She speaks ___. | Spanish | the Spanish / a Spanish | Elle parle espagnol. | Pas d'article devant une langue.
It's ___ university in Boston. | a | an / the | C'est une université à Boston. | « You- » : son consonne, donc a.
Where is ___ bathroom? | the | a / an | Où est la salle de bain ? | Celle de la maison, précise : the.
"""
},
{
"id": "pluriel", "titre": "Le pluriel", "resume": "-s, -es, -ies, et les irréguliers",
"regle": "On ajoute <b>-s</b> : <b>book → books</b>. Après s, sh, ch, x : <b>-es</b> (<b>bus → buses</b>, <b>box → boxes</b>). Une consonne + y devient <b>-ies</b> (<b>city → cities</b>), mais <b>boy → boys</b>. Quelques pluriels sont à apprendre par cœur : <b>man → men</b>, <b>woman → women</b>, <b>child → children</b>, <b>person → people</b>, <b>foot → feet</b>, <b>tooth → teeth</b>, <b>mouse → mice</b>.",
"tableau": [
 ["-s", "la règle", "cat → cats"],
 ["-es", "après s, sh, ch, x", "glass → glasses"],
 ["-ies", "consonne + y", "baby → babies"],
 ["-ves", "souvent après f / fe", "knife → knives, leaf → leaves"],
 ["irréguliers", "à apprendre", "child → children, foot → feet"],
 ["(pas de pluriel)", "indénombrables", "water, money, bread, homework"],
],
"exemples": [
 ["I have two children.", "J'ai deux enfants."],
 ["There are many people here.", "Il y a beaucoup de monde ici."],
 ["My feet hurt.", "J'ai mal aux pieds."],
],
"attention": "<b>People</b> est déjà un pluriel : <b>people are</b>, jamais <i>peoples are</i> pour « les gens ». Et <b>money</b>, <b>bread</b>, <b>homework</b> ne prennent jamais de s.",
"serie": "plurielEnExercises", "kicker": "Le pluriel",
"questions": """
I have two ___. | children | childs / childrens | J'ai deux enfants. | child → children.
Three ___ are waiting outside. | men | mans / mens | Trois hommes attendent dehors. | man → men.
I brush my ___ every morning. | teeth | tooths / teeths | Je me brosse les dents tous les matins. | tooth → teeth.
There are two ___ on the table. | boxes | boxs / boxies | Il y a deux boîtes sur la table. | Après x : -es.
New York and Chicago are big ___. | cities | citys / cityes | New York et Chicago sont de grandes villes. | Consonne + y → -ies.
The ___ are playing in the park. | boys | boies / boyes | Les garçons jouent au parc. | Voyelle + y : on garde le y.
Many ___ live in this city. | people | peoples / persons | Beaucoup de gens habitent dans cette ville. | person → people.
Put the ___ in the drawer. | knives | knifes / knife | Mets les couteaux dans le tiroir. | knife → knives.
I don't have much ___. | money | moneys / moneies | Je n'ai pas beaucoup d'argent. | Money est indénombrable : jamais de s.
My ___ hurt after the walk. | feet | foots / feets | J'ai mal aux pieds après la promenade. | foot → feet.
"""
},
{
"id": "present-simple", "titre": "Le présent simple", "resume": "I work, he works — et do / does",
"regle": "Le présent simple dit une <b>habitude</b> ou une vérité : <b>I work in a bank</b>. Une seule terminaison : le <b>-s de la 3ᵉ personne</b> (he, she, it) : <b>she works</b>, <b>he goes</b>, <b>it rains</b>. Pour la négation et la question, l'anglais appelle <b>do</b> (ou <b>does</b> avec he / she / it), et le verbe reste nu : <b>I don't like tea</b>, <b>Does she speak French?</b>",
"tableau": [
 ["I / you / we / they work", "affirmation", "We live in Montreal."],
 ["he / she / it works", "le -s de la 3ᵉ personne", "She plays tennis."],
 ["don't + verbe", "négation", "I don't eat meat."],
 ["doesn't + verbe", "négation (he, she, it)", "He doesn't drive."],
 ["Do you…? Does he…?", "question", "Do you like music?"],
],
"exemples": [
 ["My brother works at night.", "Mon frère travaille la nuit."],
 ["Do you speak English? — Yes, I do.", "Tu parles anglais ? — Oui."],
 ["She doesn't like coffee.", "Elle n'aime pas le café."],
],
"attention": "Avec does, le -s est déjà pris : <b>Does she work?</b>, <b>she doesn't work</b> — jamais <i>she doesn't works</i>.",
"serie": "presentEnExercises", "kicker": "Le présent simple",
"questions": """
She ___ in a hospital. | works | work / working | Elle travaille dans un hôpital. | He, she, it : -s.
I ___ coffee every morning. | drink | drinks / drinking | Je bois du café tous les matins. | I : le verbe nu.
My father ___ to work by bus. | goes | go / gos | Mon père va au travail en bus. | go → goes (-es après o).
They ___ in Toronto. | live | lives / living | Ils habitent à Toronto. | They : le verbe nu.
I ___ like fish. | don't | doesn't / not | Je n'aime pas le poisson. | I + don't.
He ___ speak Spanish. | doesn't | don't / not | Il ne parle pas espagnol. | He + doesn't.
___ you play the guitar? | Do | Does / Are | Tu joues de la guitare ? | You : Do.
___ she have a car? | Does | Do / Is | Elle a une voiture ? | She : Does.
Does he ___ French? | speak | speaks / speaking | Il parle français ? | Après does, le verbe reste nu.
My sister ___ English at school. | studies | studys / study | Ma sœur étudie l'anglais à l'école. | Consonne + y → -ies.
It ___ a lot in April. | rains | rain / raining | Il pleut beaucoup en avril. | It : -s.
We ___ watch TV in the morning. | don't | doesn't / aren't | Nous ne regardons pas la télé le matin. | We + don't.
"""
},
{
"id": "present-continu", "titre": "Le présent en -ing", "resume": "I'm working : en ce moment",
"regle": "Pour ce qui se passe <b>en ce moment</b>, l'anglais emploie <b>be + verbe en -ing</b> : <b>I'm eating</b> (je suis en train de manger). Le présent simple, lui, dit l'habitude : <b>I eat at noon</b>. Le -ing se forme simplement : <b>work → working</b>, un e muet tombe (<b>make → making</b>), et quelques consonnes doublent (<b>run → running</b>, <b>swim → swimming</b>).",
"tableau": [
 ["I'm working", "je travaille (en ce moment)", "I'm working, call me later."],
 ["she's reading", "elle lit (là, maintenant)", "Be quiet, she's reading."],
 ["they aren't sleeping", "négation", "The kids aren't sleeping yet."],
 ["Are you listening?", "question", "Are you listening to me?"],
],
"exemples": [
 ["What are you doing? — I'm cooking.", "Qu'est-ce que tu fais ? — Je cuisine."],
 ["It's raining.", "Il pleut (en ce moment)."],
 ["Look! The baby is sleeping.", "Regarde ! Le bébé dort."],
],
"attention": "Quelques verbes ne se mettent presque jamais en -ing : <b>like</b>, <b>love</b>, <b>want</b>, <b>know</b>, <b>understand</b>. On dit <b>I know</b>, jamais <i>I'm knowing</i>.",
"serie": "continuEnExercises", "kicker": "Le présent en -ing",
"questions": """
Shh! The baby ___ sleeping. | is | are / does | Chut ! Le bébé dort. | be + -ing : the baby is.
I ___ watching TV right now. | am | is / do | Je regarde la télé en ce moment. | I am + -ing.
Look! It ___ snowing! | is | are / does | Regarde ! Il neige ! | It is + -ing.
They are ___ in the pool. | swimming | swiming / swim | Ils nagent dans la piscine. | swim → swimming (consonne doublée).
She's ___ dinner. | making | makeing / make | Elle prépare le dîner. | Le e muet tombe : making.
What ___ you doing? | are | is / do | Qu'est-ce que tu fais ? | You are + -ing.
He ___ every day. | runs | is running / running | Il court tous les jours. | Une habitude : le présent simple.
I ___ the answer. | know | am knowing / knowing | Je connais la réponse. | Know ne se met pas en -ing.
We aren't ___ today. | working | work / works | Nous ne travaillons pas aujourd'hui. | aren't + -ing.
Are you ___ to me? | listening | listen / listens | Tu m'écoutes ? | Are you + -ing ?
"""
},
{
"id": "pronoms", "titre": "Pronoms et possessifs", "resume": "I, me, my — et le 's",
"regle": "Trois formes à ne pas mélanger : le <b>sujet</b> (<b>I</b>, he, she, we, they), le <b>complément</b> (<b>me</b>, him, her, us, them) et le <b>possessif</b> (<b>my</b>, his, her, our, their). Le possessif s'accorde avec le <b>possesseur</b>, pas avec l'objet : <b>his mother</b> (sa mère, à lui), <b>her father</b> (son père, à elle). Pour « le livre de Paul », on dit <b>Paul's book</b>.",
"tableau": [
 ["I · me · my", "je · me, moi · mon", "I love my dog. He loves me."],
 ["he · him · his", "il · le, lui · son (à lui)", "His car is red."],
 ["she · her · her", "elle · la, lui · son (à elle)", "Her name is Anna."],
 ["we · us · our", "nous · nous · notre", "Our house is small."],
 ["they · them · their", "ils · les, leur · leur", "Their kids are at school."],
 ["Paul's", "de Paul", "Paul's sister is a nurse."],
],
"exemples": [
 ["This is my brother. His name is Tom.", "Voici mon frère. Il s'appelle Tom."],
 ["Can you help us?", "Tu peux nous aider ?"],
 ["Anna's car is blue.", "La voiture d'Anna est bleue."],
],
"attention": "Le piège des francophones : « sa » ou « son » se dit <b>his</b> si c'est à un homme, <b>her</b> si c'est à une femme, quel que soit l'objet. <b>Paul and his sister</b>, <b>Marie and her brother</b>.",
"serie": "pronomsEnExercises", "kicker": "Pronoms et possessifs",
"questions": """
Marie lives with ___ brother. | her | his / their | Marie habite avec son frère. | À elle : her.
Paul loves ___ sister. | his | her / its | Paul aime sa sœur. | À lui : his.
Can you help ___? | me | I / my | Tu peux m'aider ? | Complément : me.
___ live in a small apartment. | We | Us / Our | Nous habitons dans un petit appartement. | Sujet : we.
I see ___ every day. | them | they / their | Je les vois tous les jours. | Complément : them.
This is ___ house. We love it. | our | us / we | C'est notre maison. Nous l'adorons. | Possessif : our.
The kids are with ___ parents. | their | them / they | Les enfants sont avec leurs parents. | Possessif : their.
Call ___, she's waiting. | her | she / hers | Appelle-la, elle attend. | Complément féminin : her.
This is ___ car. | Tom's | Tom / of Tom | C'est la voiture de Tom. | Le possesseur + 's.
The dog is in ___ bed. | its | it's / his | Le chien est dans son panier. | Une chose ou un animal : its (sans apostrophe).
"""
},
{
"id": "there-is", "titre": "There is, there are", "resume": "Il y a",
"regle": "« Il y a » se dit <b>there is</b> devant un singulier ou un indénombrable, <b>there are</b> devant un pluriel. À l'oral : <b>there's</b>. Négation : <b>there isn't</b>, <b>there aren't</b> ; question : <b>Is there…? Are there…?</b> Avec any dans les questions et les négations : <b>Are there any eggs?</b>",
"tableau": [
 ["there is · there's", "il y a (singulier)", "There's a bank on the corner."],
 ["there are", "il y a (pluriel)", "There are two bedrooms."],
 ["there isn't · there aren't", "il n'y a pas", "There isn't any milk."],
 ["Is there…? · Are there…?", "est-ce qu'il y a… ?", "Is there a pharmacy near here?"],
],
"exemples": [
 ["There are twenty students in my class.", "Il y a vingt élèves dans ma classe."],
 ["Is there a bus stop near here?", "Est-ce qu'il y a un arrêt de bus près d'ici ?"],
],
"attention": "« Il y a deux jours » ne se dit pas avec there : <b>two days ago</b>.",
"serie": "thereEnExercises", "kicker": "There is, there are",
"questions": """
There ___ a cat in the garden. | is | are / have | Il y a un chat dans le jardin. | Un singulier : there is.
There ___ three bedrooms. | are | is / has | Il y a trois chambres. | Un pluriel : there are.
There ___ any bread. | isn't | aren't / don't | Il n'y a pas de pain. | Bread est indénombrable : there isn't.
___ there a bank near here? | Is | Are / Does | Est-ce qu'il y a une banque près d'ici ? | Question au singulier : Is there…?
___ there any eggs in the fridge? | Are | Is / Do | Il y a des œufs dans le frigo ? | Question au pluriel : Are there…?
There ___ a lot of people at the party. | are | is / has | Il y a beaucoup de monde à la fête. | People est pluriel.
There ___ some milk in the bottle. | is | are / have | Il y a du lait dans la bouteille. | Milk est indénombrable.
I saw him two days ___. | ago | there / before | Je l'ai vu il y a deux jours. | « Il y a » + durée : ago.
"""
},
{
"id": "can", "titre": "Can, can't", "resume": "Pouvoir, savoir faire",
"regle": "<b>Can</b> dit la capacité (<b>I can swim</b>, je sais nager), la possibilité et la permission (<b>Can I sit here?</b>). Il ne change jamais : <b>she can</b>, sans -s. Le verbe qui suit reste nu, sans <i>to</i> : <b>I can speak English</b>. Négation : <b>can't</b> (ou cannot). Question : <b>Can you…?</b>",
"tableau": [
 ["I / she can + verbe", "je peux, je sais", "She can drive."],
 ["can't", "je ne peux pas", "I can't come tomorrow."],
 ["Can you…?", "tu peux… ?", "Can you help me?"],
 ["Can I…?", "je peux… ? (permission)", "Can I open the window?"],
],
"exemples": [
 ["I can't swim.", "Je ne sais pas nager."],
 ["Can you repeat that, please?", "Tu peux répéter, s'il te plaît ?"],
],
"attention": "« Je sais nager » se dit <b>I can swim</b>, pas <i>I know swim</i>. <b>Know</b> sert à connaître une chose ou une personne.",
"serie": "canEnExercises", "kicker": "Can, can't",
"questions": """
She ___ speak three languages. | can | cans / can to | Elle parle trois langues. | Can ne prend jamais de -s.
I can ___ the piano. | play | to play / plays | Je sais jouer du piano. | Après can, le verbe nu.
___ you help me, please? | Can | Do / Are | Tu peux m'aider, s'il te plaît ? | Question : Can you…?
Sorry, I ___ come tonight. | can't | don't can / not can | Désolé, je ne peux pas venir ce soir. | Négation : can't.
___ I sit here? | Can | Do / Am | Je peux m'asseoir ici ? | Permission : Can I…?
My little brother can ___. | swim | swims / swimming | Mon petit frère sait nager. | Savoir faire = can + verbe.
He ___ drive, he's only twelve. | can't | doesn't / isn't | Il ne sait pas conduire, il n'a que douze ans. | can't + verbe.
"""
},
{
"id": "questions", "titre": "Poser une question", "resume": "What, where, when… et l'ordre des mots",
"regle": "Le mot interrogatif vient en tête, puis l'ordre de la question : <b>Where do you live?</b>, <b>What is your name?</b> Avec be, le verbe passe devant le sujet (<b>Where is the station?</b>) ; avec les autres verbes, on appelle <b>do / does</b> (<b>What does she do?</b>). <b>How much</b> (indénombrable, prix) et <b>how many</b> (dénombrable) disent « combien ».",
"tableau": [
 ["What", "que, quoi, quel", "What time is it?"],
 ["Where", "où", "Where do you work?"],
 ["When", "quand", "When is your birthday?"],
 ["Who", "qui", "Who is that man?"],
 ["Why", "pourquoi", "Why are you sad?"],
 ["How", "comment", "How do you spell it?"],
 ["How much · How many", "combien", "How much is it? How many brothers do you have?"],
],
"exemples": [
 ["Where are you from?", "D'où viens-tu ?"],
 ["What do you do? — I'm a nurse.", "Qu'est-ce que tu fais dans la vie ? — Je suis infirmière."],
 ["How many children do they have?", "Combien d'enfants ont-ils ?"],
],
"attention": "<b>What do you do?</b> demande le métier ; <b>What are you doing?</b> demande ce qu'on fait en ce moment.",
"serie": "questionsEnExercises", "kicker": "Poser une question",
"questions": """
___ do you live? — In Montreal. | Where | What / Who | Où habites-tu ? — À Montréal. | Un lieu : where.
___ is your name? | What | How / Who | Comment t'appelles-tu ? | Le nom : What is your name?
___ is your birthday? — In May. | When | Where / What | C'est quand, ton anniversaire ? — En mai. | Un moment : when.
___ is that woman? — My aunt. | Who | What / Which | Qui est cette femme ? — Ma tante. | Une personne : who.
___ are you sad? — Because I'm tired. | Why | How / What | Pourquoi es-tu triste ? — Parce que je suis fatigué. | Une raison : why.
___ much is this shirt? | How | What / Which | Combien coûte cette chemise ? | Un prix : how much.
How ___ sisters do you have? | many | much / lot | Combien de sœurs as-tu ? | Dénombrable : how many.
Where ___ she work? | does | do / is | Où travaille-t-elle ? | She : does.
What time ___ it? | is | does / do | Quelle heure est-il ? | Avec be, pas de do.
Where ___ the bathroom? | is | does / are | Où sont les toilettes ? | The bathroom : is.
"""
},
{
"id": "prepositions", "titre": "In, on, at", "resume": "Le lieu et le temps",
"regle": "Pour le <b>lieu</b> : <b>in</b> = dedans (in the box, in Canada), <b>on</b> = sur une surface (on the table, on the wall), <b>at</b> = à un point précis (at the door, at home, at work). Pour le <b>temps</b> : <b>at</b> + heure (<b>at six</b>), <b>on</b> + jour ou date (<b>on Monday</b>), <b>in</b> + mois, saison, année, partie de la journée (<b>in July</b>, <b>in the morning</b>).",
"tableau": [
 ["in", "dans ; mois, année, saison", "in the kitchen · in May · in the morning"],
 ["on", "sur ; jour, date", "on the table · on Friday · on July 4th"],
 ["at", "à (point précis) ; heure", "at home · at the station · at 8 o'clock"],
 ["at night", "la nuit (exception)", "I sleep at night."],
],
"exemples": [
 ["The keys are on the table.", "Les clés sont sur la table."],
 ["I start work at nine.", "Je commence le travail à neuf heures."],
 ["My birthday is in June.", "Mon anniversaire est en juin."],
],
"attention": "On dit <b>in the morning</b>, <b>in the afternoon</b>, <b>in the evening</b>… mais <b>at night</b>. Et <b>at the weekend</b> (britannique) se dit <b>on the weekend</b> en américain.",
"serie": "prepositionsEnExercises", "kicker": "In, on, at",
"questions": """
The milk is ___ the fridge. | in | on / at | Le lait est dans le frigo. | Dedans : in.
Your phone is ___ the table. | on | in / at | Ton téléphone est sur la table. | Sur une surface : on.
I'm ___ home tonight. | at | in / on | Je suis à la maison ce soir. | At home.
The meeting is ___ ten o'clock. | at | in / on | La réunion est à dix heures. | Une heure : at.
See you ___ Monday! | on | in / at | À lundi ! | Un jour : on.
We go to the beach ___ July. | in | on / at | Nous allons à la plage en juillet. | Un mois : in.
I drink coffee ___ the morning. | in | on / at | Je bois du café le matin. | In the morning.
I never work ___ night. | at | in / on | Je ne travaille jamais la nuit. | At night (l'exception).
She lives ___ Canada. | in | at / on | Elle habite au Canada. | Un pays : in.
There's a picture ___ the wall. | on | in / at | Il y a un tableau au mur. | Sur une surface : on the wall.
"""
},
{
"id": "adjectifs", "titre": "Les adjectifs", "resume": "Invariables, avant le nom ; bigger, the biggest",
"regle": "L'adjectif anglais <b>ne s'accorde jamais</b> : <b>a big house</b>, <b>two big houses</b>. Il se place <b>avant</b> le nom : <b>a red car</b> (une voiture rouge). Pour comparer : les adjectifs courts prennent <b>-er</b> et <b>the -est</b> (<b>big → bigger → the biggest</b>), les longs passent par <b>more</b> et <b>the most</b> (<b>more expensive</b>). « Que » se dit <b>than</b>.",
"tableau": [
 ["a new car · new cars", "invariable", "My shoes are new."],
 ["-er · the -est", "adjectif court", "tall → taller → the tallest"],
 ["more · the most", "adjectif long", "more interesting, the most beautiful"],
 ["good · bad", "irréguliers", "better, the best · worse, the worst"],
 ["than", "que (comparaison)", "She's older than me."],
],
"exemples": [
 ["It's a beautiful day.", "C'est une belle journée."],
 ["My brother is taller than me.", "Mon frère est plus grand que moi."],
 ["This is the best pizza in town.", "C'est la meilleure pizza de la ville."],
],
"attention": "Pas de s à l'adjectif, même au pluriel : <b>green apples</b>, jamais <i>greens apples</i>.",
"serie": "adjectifsEnExercises", "kicker": "Les adjectifs",
"questions": """
I have two ___ cars. | red | reds / redes | J'ai deux voitures rouges. | L'adjectif ne s'accorde pas.
She has a ___ house. | big | bigs / house big | Elle a une grande maison. | L'adjectif avant le nom.
My sister is ___ than me. | older | more old / oldest | Ma sœur est plus âgée que moi. | Court : -er.
This bag is ___ than that one. | more expensive | expensiver / most expensive | Ce sac est plus cher que celui-là. | Long : more.
It's the ___ day of the year. | hottest | hotest / most hot | C'est le jour le plus chaud de l'année. | hot → the hottest (t doublé).
Your English is ___ than mine. | better | gooder / more good | Ton anglais est meilleur que le mien. | good → better.
He's taller ___ his father. | than | that / as | Il est plus grand que son père. | « Que » : than.
It's the ___ restaurant in town. | best | better / goodest | C'est le meilleur restaurant de la ville. | good → the best.
"""
},
{
"id": "passe", "titre": "Le prétérit", "resume": "I worked, I went — et did",
"regle": "Le <b>prétérit</b> raconte une action finie, souvent avec une date : <b>I worked yesterday</b>. Les verbes réguliers prennent <b>-ed</b> (<b>play → played</b>, <b>live → lived</b>, <b>study → studied</b>). Les irréguliers sont à apprendre : <b>go → went</b>, <b>have → had</b>, <b>see → saw</b>. Une seule forme pour toutes les personnes. Négation et question passent par <b>did</b>, et le verbe redevient nu : <b>I didn't go</b>, <b>Did you see it?</b> Be a deux formes : <b>was</b> (I, he, she, it) et <b>were</b> (you, we, they).",
"tableau": [
 ["-ed", "verbes réguliers", "I watched a movie yesterday."],
 ["went, had, saw…", "verbes irréguliers", "We went to the beach."],
 ["didn't + verbe", "négation", "She didn't call me."],
 ["Did you…?", "question", "Did you sleep well?"],
 ["was · were", "be au passé", "I was tired. They were at home."],
],
"exemples": [
 ["I visited my grandparents last week.", "J'ai rendu visite à mes grands-parents la semaine dernière."],
 ["Did you have breakfast? — No, I didn't.", "Tu as pris ton petit-déjeuner ? — Non."],
 ["It was very cold yesterday.", "Il faisait très froid hier."],
],
"attention": "Après did, le verbe ne prend plus la marque du passé : <b>Did you go?</b>, jamais <i>Did you went?</i>",
"serie": "passeEnExercises", "kicker": "Le prétérit",
"questions": """
Yesterday I ___ tennis. | played | play / playing | Hier, j'ai joué au tennis. | Régulier : -ed.
We ___ to the beach last summer. | went | goed / go | Nous sommes allés à la plage l'été dernier. | go → went.
She ___ a cake for my birthday. | made | maked / make | Elle a fait un gâteau pour mon anniversaire. | make → made.
I ___ my keys this morning. | lost | losed / lose | J'ai perdu mes clés ce matin. | lose → lost.
They ___ in Paris for two years. | lived | livd / live | Ils ont vécu à Paris pendant deux ans. | live → lived.
___ you see the movie? | Did | Do / Was | Tu as vu le film ? | Question au passé : Did.
I didn't ___ him at the party. | see | saw / seen | Je ne l'ai pas vu à la fête. | Après didn't, le verbe nu.
It ___ very hot yesterday. | was | were / did | Il faisait très chaud hier. | It : was.
You ___ late this morning! | were | was / did | Tu étais en retard ce matin ! | You : were.
He ___ for the exam all weekend. | studied | studyed / study | Il a révisé l'examen tout le week-end. | Consonne + y → -ied.
"""
},
{
"id": "faux-amis", "titre": "Les faux amis", "resume": "library ≠ librairie, actually ≠ actuellement",
"regle": "Des mots anglais ressemblent à des mots français et veulent dire autre chose. Les apprendre <b>par paires</b> évite les malentendus les plus fréquents. Les plus courants dès le début : <b>library</b> (bibliothèque), <b>actually</b> (en fait), <b>to attend</b> (assister à), <b>a car</b> (une voiture), <b>a journey</b> (un voyage), <b>a coin</b> (une pièce de monnaie).",
"tableau": [
 ["library", "bibliothèque (librairie = bookstore)", "I study at the library."],
 ["actually", "en fait (actuellement = currently)", "Actually, I'm from Belgium."],
 ["to attend", "assister à (attendre = to wait)", "I attend a class on Monday."],
 ["a car", "une voiture (un car = a bus)", "My car is blue."],
 ["a coin", "une pièce (un coin = a corner)", "I need a coin for the cart."],
 ["a journey", "un voyage (une journée = a day)", "The journey takes two hours."],
 ["to rest", "se reposer (rester = to stay)", "I'm tired, I need to rest."],
 ["sensible", "raisonnable (sensible = sensitive)", "That's a sensible idea."],
],
"exemples": [
 ["We're waiting for the bus.", "Nous attendons le bus."],
 ["I bought this book at a bookstore.", "J'ai acheté ce livre dans une librairie."],
],
"attention": "« Je suis actuellement en vacances » se dit <b>I'm currently on vacation</b>. <b>Actually</b> corrige ou précise : « en fait ».",
"serie": "fauxAmisEnExercises", "kicker": "Les faux amis",
"questions": """
I borrow books at the ___. | library | bookstore / librairy | J'emprunte des livres à la bibliothèque. | Bibliothèque = library.
I bought a novel at the ___. | bookstore | library / librairie | J'ai acheté un roman à la librairie. | Librairie = bookstore.
I'm ___ the bus. | waiting for | attending / expecting at | J'attends le bus. | Attendre = to wait (for).
She ___ a concert last night. | attended | waited / expected | Elle a assisté à un concert hier soir. | Assister à = to attend.
___, I'm not French, I'm Swiss. | Actually | Currently / Actual | En fait, je ne suis pas français, je suis suisse. | En fait = actually.
I'm ___ looking for a job. | currently | actually / actual | Je cherche actuellement un emploi. | Actuellement = currently.
I'm tired, I want to ___. | rest | stay / remain | Je suis fatigué, je veux me reposer. | Se reposer = to rest.
Can you ___ with the kids tonight? | stay | rest / remain at | Tu peux rester avec les enfants ce soir ? | Rester = to stay.
The bank is on the ___. | corner | coin / angle | La banque est au coin de la rue. | Le coin de la rue = the corner.
"""
},
]

# Les textes d'interface de la grammaire anglaise, verses dans I18N (fr).
TEXTES = {
    "fiche_entrainer": "M'ENTRAÎNER →",
    "gram_attention": "Attention",
    "orb_es_indice": "Grammaire",
    "gram_indice_kicker": "Grammaire · A1",
    "gram_indice_titre": "Toutes les fiches",
}
