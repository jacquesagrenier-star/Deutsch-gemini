# -*- coding: utf-8 -*-
"""Les fiches de grammaire A2 du portugais (du Portugal), en francais, et leurs
series. SOURCE : on corrige ici, puis python portugais/outils/construire.py
(niveaux.py ajoute ces fiches, avec leur niveau, apres celles de l'A1).

Meme format que grammaire_a1.py (session socle). Une question : « phrase avec
___ | bonne reponse | mauvaise 1 / mauvaise 2 | traduction | explication ».
BROUILLON : a faire relire par un lusophone du Portugal.
"""

FICHES = [
{
"id": "imperfeito", "titre": "Le pretérito imperfeito", "resume": "falava, comia, partia — le décor, l'habitude, l'âge",
"regle": "L'<b>imperfeito</b> décrit le passé sans dire quand il commence ni quand il finit : ce qu'on faisait d'habitude (<b>Eu ia à praia todos os verões</b>), le décor d'une histoire (<b>Chovia e estava frio</b>), l'âge, l'heure, l'état d'esprit. Formes : <b>-ava</b> pour les verbes en -ar, <b>-ia</b> pour -er et -ir. Quatre irréguliers seulement : <b>ser</b> (era), <b>ter</b> (tinha), <b>vir</b> (vinha), <b>pôr</b> (punha).",
"tableau": [
 ["falar → falava, falavas, falava, falávamos, falavam", "parlais, parlait…", "Falava com a avó ao domingo."],
 ["comer → comia, comias, comia, comíamos, comiam", "mangeais, mangeait…", "Comíamos sempre às oito."],
 ["partir → partia, partias, partia, partíamos, partiam", "partais, partait…", "O comboio partia às sete."],
 ["ser → era, eras, era, éramos, eram", "étais, était…", "Era uma casa antiga."],
 ["ter → tinha · vir → vinha · pôr → punha", "avais · venais · mettais", "Eu tinha dez anos."],
 ["quando era pequeno, antigamente, todos os dias", "les mots de l'habitude", "Antigamente não havia telemóveis."],
],
"exemples": [
 ["Quando eu era criança, morava no Porto.", "Quand j'étais enfant, j'habitais à Porto."],
 ["Estava sol e as pessoas passeavam na praia.", "Il faisait soleil et les gens se promenaient sur la plage."],
 ["Todos os sábados íamos ao mercado.", "Tous les samedis, nous allions au marché."],
],
"attention": "Au Portugal, l'imperfeito remplace aussi très souvent le conditionnel à l'oral : <b>Eu queria um café</b> (je voudrais un café), <b>Se pudesse, ia</b> (si je pouvais, j'irais). C'est poli et naturel.",
"serie": "imperfeitoPtExercises", "kicker": "L'imperfeito",
"questions": """
Quando eu ___ pequeno, brincava na rua. | era | fui / sou | Quand j'étais petit, je jouais dans la rue. | L'âge, le décor : imperfeito de ser (era).
Antigamente nós ___ no campo. | vivíamos | vivemos / viveremos | Autrefois, nous vivions à la campagne. | Antigamente : une habitude passée, imperfeito.
O meu avô ___ sempre o jornal ao pequeno-almoço. | lia | leu / lê | Mon grand-père lisait toujours le journal au petit-déjeuner. | Sempre, une habitude : imperfeito (lia).
___ muito frio nessa noite. | Estava | Esteve / Está | Il faisait très froid ce soir-là. | Le décor : imperfeito.
Eles ___ dois cães e um gato. | tinham | tiveram / têm | Ils avaient deux chiens et un chat. | Ter à l'imperfeito : tinha, tinham.
Tu ___ ao cinema todas as semanas? | ias | foste / vais | Tu allais au cinéma toutes les semaines ? | Todas as semanas : habitude, imperfeito d'ir (ias).
Ela ___ de Coimbra de comboio todos os dias. | vinha | veio / vem | Elle venait de Coimbra en train tous les jours. | Vir à l'imperfeito : vinha.
Eram oito horas e as lojas ainda ___ fechadas. | estavam | estiveram / estão | Il était huit heures et les magasins étaient encore fermés. | L'heure et le décor : imperfeito.
Eu ___ um café, por favor. | queria | quis / quero | Je voudrais un café, s'il vous plaît. | L'imperfeito de politesse : queria.
A minha mãe ___ a mesa enquanto o meu pai cozinhava. | punha | pôs / põe | Ma mère mettait la table pendant que mon père cuisinait. | Pôr à l'imperfeito : punha.
Nós ___ muito quando éramos estudantes. | saíamos | saímos / sairemos | Nous sortions beaucoup quand nous étions étudiants. | Sair à l'imperfeito : saía, saíamos (avec accent).
De manhã, ela ___ sempre muito cansada. | estava | esteve / está | Le matin, elle était toujours très fatiguée. | Un état qui se répète : imperfeito.
Os meus pais ___ numa fábrica. | trabalhavam | trabalharam / trabalham | Mes parents travaillaient dans une usine. | -ar : -avam.
Quando ___ dez anos, aprendi a nadar. | tinha | tive / tenho | Quand j'avais dix ans, j'ai appris à nager. | L'âge : tinha.
"""
},
{
"id": "perfeito-imperfeito", "titre": "Perfeito ou imperfeito ?", "resume": "fui ou ia, comi ou comia — l'action et le décor",
"regle": "Le <b>perfeito</b> raconte une action terminée, à un moment précis : <b>Ontem fui ao médico</b>. L'<b>imperfeito</b> pose le décor ou dit une habitude : <b>Ia ao médico todos os meses</b>. Dans une même phrase, l'imperfeito est souvent l'action en cours, et le perfeito ce qui l'interrompt : <b>Estava a jantar quando o telefone tocou</b>. Le perfeito portugais couvre aussi le passé composé français : <b>Já comeste?</b> (Tu as déjà mangé ?).",
"tableau": [
 ["ontem, no sábado, em 2019, uma vez", "un moment précis : perfeito", "Ontem choveu muito."],
 ["sempre, todos os dias, antigamente", "une habitude : imperfeito", "Chovia sempre em novembro."],
 ["estava a + infinitif … quando + perfeito", "l'action interrompue", "Estava a dormir quando chegaste."],
 ["de repente, nesse momento", "l'événement : perfeito", "De repente, a luz apagou-se."],
 ["era, havia, estava", "la description : imperfeito", "Era tarde e havia pouca gente."],
],
"exemples": [
 ["Quando era estudante, trabalhei dois anos num café.", "Quand j'étais étudiant, j'ai travaillé deux ans dans un café."],
 ["Estávamos a ver televisão quando a luz foi abaixo.", "Nous regardions la télévision quand le courant a sauté."],
 ["Já viste este filme? — Já, vi-o no ano passado.", "Tu as déjà vu ce film ? — Oui, je l'ai vu l'an dernier."],
],
"attention": "Le portugais n'a pas de passé composé au sens français : <b>tenho falado</b> ne veut pas dire « j'ai parlé » mais « j'ai parlé ces derniers temps, à plusieurs reprises » (voir le B2). Pour « j'ai parlé », c'est <b>falei</b>.",
"serie": "perfeitoImperfeitoPtExercises", "kicker": "Perfeito ou imperfeito ?",
"questions": """
Ontem ___ ao cinema com a Rita. | fui | ia / vou | Hier, je suis allé au cinéma avec Rita. | Ontem, un moment précis : perfeito.
Quando era pequena, ___ ao cinema todos os domingos. | ia | fui / vou | Quand j'étais petite, j'allais au cinéma tous les dimanches. | Todos os domingos : habitude, imperfeito.
Estava a tomar banho quando o telefone ___. | tocou | tocava / toca | Je prenais ma douche quand le téléphone a sonné. | L'événement qui interrompt : perfeito.
___ muito calor quando chegámos a Faro. | Fazia | Fez / Faz | Il faisait très chaud quand nous sommes arrivés à Faro. | Le décor : imperfeito.
Em 2015, ela ___ para Londres. | mudou-se | mudava-se / muda-se | En 2015, elle a déménagé à Londres. | Une date : perfeito.
De repente, o cão ___ a correr. | começou | começava / começa | Tout à coup, le chien s'est mis à courir. | De repente : perfeito.
Já ___ o novo restaurante da esquina? | experimentaste | experimentavas / experimentas | Tu as déjà essayé le nouveau restaurant du coin ? | Já + perfeito : le passé composé français.
Enquanto eu cozinhava, ele ___ a mesa. | punha | pôs / põe | Pendant que je cuisinais, il mettait la table. | Deux actions qui durent en même temps : imperfeito.
A casa ___ grande e tinha um jardim bonito. | era | foi / é | La maison était grande et avait un joli jardin. | La description : imperfeito.
Nesse dia ___ às seis da manhã. | acordei | acordava / acordo | Ce jour-là, je me suis réveillé à six heures du matin. | Nesse dia : un moment précis, perfeito.
Ele ___ três vezes ao Brasil. | foi | ia / vai | Il est allé trois fois au Brésil. | Un nombre de fois : perfeito.
Antes ___ muito, mas agora já não fumo. | fumava | fumei / fumo | Avant je fumais beaucoup, mais maintenant je ne fume plus. | Une habitude finie : imperfeito.
Estávamos a jantar quando a Ana ___. | chegou | chegava / chega | Nous dînions quand Ana est arrivée. | L'arrivée interrompt le dîner : perfeito.
Na semana passada ___ a avó no hospital. | visitámos | visitávamos / visitamos | La semaine dernière, nous avons rendu visite à grand-mère à l'hôpital. | Perfeito, 1re pers. du pluriel : visitámos (avec accent, au Portugal).
"""
},
{
"id": "comparativos", "titre": "Comparer : mais… do que, tão… como", "resume": "mais caro do que, tão alto como, o melhor",
"regle": "Pour comparer : <b>mais … (do) que</b> (plus … que), <b>menos … (do) que</b> (moins … que), <b>tão … como</b> ou <b>tão … quanto</b> (aussi … que). Le superlatif : <b>o / a mais …</b> (<b>a cidade mais bonita</b>). Quatre formes irrégulières : <b>bom → melhor</b>, <b>mau → pior</b>, <b>grande → maior</b>, <b>pequeno → menor</b> ; au Portugal, on dit aussi très couramment <b>mais pequeno</b>. Pour « très, extrêmement » : <b>muito caro</b>, ou le suffixe <b>-íssimo</b> (<b>caríssimo</b>).",
"tableau": [
 ["mais … do que", "plus … que", "O Porto é mais pequeno do que Lisboa."],
 ["menos … do que", "moins … que", "Este hotel é menos caro do que o outro."],
 ["tão … como / quanto", "aussi … que", "A Ana é tão alta como o irmão."],
 ["tanto(s) / tanta(s) … como", "autant de … que", "Tenho tantos livros como tu."],
 ["melhor · pior · maior · menor", "meilleur · pire · plus grand · plus petit", "Este vinho é melhor."],
 ["o / a mais …", "le / la plus …", "É o prédio mais alto da cidade."],
 ["-íssimo", "très, extrêmement", "O exame foi facílimo / dificílimo."],
],
"exemples": [
 ["O comboio é mais rápido do que o autocarro.", "Le train est plus rapide que le bus."],
 ["Esta sopa está ainda melhor do que a de ontem.", "Cette soupe est encore meilleure que celle d'hier."],
 ["É o melhor pastel de nata de Lisboa.", "C'est le meilleur pastel de nata de Lisbonne."],
],
"attention": "On ne dit jamais <b>mais bom</b> ni <b>mais grande</b> : c'est <b>melhor</b>, <b>maior</b>. Mais <b>mais pequeno</b> est normal au Portugal (le Brésil préfère <b>menor</b>).",
"serie": "comparativosPtExercises", "kicker": "Comparer",
"questions": """
O Porto é ___ pequeno do que Lisboa. | mais | tão / muito | Porto est plus petit que Lisbonne. | Plus … que : mais … do que.
Este café é ___ do que o outro. | melhor | mais bom / bem | Ce café est meilleur que l'autre. | Bom → melhor, jamais « mais bom ».
A minha irmã é tão alta ___ eu. | como | do que / que tão | Ma sœur est aussi grande que moi. | Aussi … que : tão … como.
Hoje o tempo está ___ do que ontem. | pior | mais mau / mal | Aujourd'hui, le temps est pire qu'hier. | Mau → pior.
O Brasil é ___ do que Portugal. | maior | mais grande / grandíssimo | Le Brésil est plus grand que le Portugal. | Grande → maior.
É a praia mais bonita ___ Algarve. | do | que / como | C'est la plus belle plage de l'Algarve. | Le superlatif : o / a mais … de (do Algarve).
Tenho ___ trabalho como tu. | tanto | tão / tantos | J'ai autant de travail que toi. | Autant de + nom singulier masculin : tanto.
Este exercício é ___ difícil do que o anterior. | menos | menor / pouco | Cet exercice est moins difficile que le précédent. | Moins … que : menos … do que.
O jantar estava ___! | ótimo | mais ótimo / muito ótimo | Le dîner était excellent ! | Ótimo est déjà un superlatif : pas de « mais » ni de « muito ».
A Joana fala inglês ___ do que eu. | melhor | mais bem / mais boa | Joana parle anglais mieux que moi. | L'adverbe bem → melhor.
Este quarto é o ___ da casa. | maior | mais grande / mais maior | Cette chambre est la plus grande de la maison. | Le superlatif de grande : o maior.
A viagem foi ___: cinco horas sem parar. | longuíssima | muito longuíssima / mais longa | Le voyage a été extrêmement long : cinq heures sans s'arrêter. | -íssimo : longo → longuíssimo (le g garde son u).
Há tantas pessoas aqui ___ no ano passado. | como | do que / que | Il y a autant de monde ici que l'an dernier. | Tanto(s)… como.
O Pedro é ___ velho do que o irmão. | mais | maior / tão | Pedro est plus âgé que son frère. | Pour l'âge : mais velho, mais novo.
"""
},
{
"id": "pronomes-complemento", "titre": "Le pronom complément : vi-o, dei-lhe", "resume": "o, a, os, as · lhe, lhes — et vê-lo, compram-na",
"regle": "Le complément direct (le, la, les) : <b>o, a, os, as</b> ; le complément indirect (lui, leur) : <b>lhe, lhes</b>. Au Portugal, ils se placent <b>après le verbe</b>, avec un trait d'union : <b>Vi-o ontem</b>, <b>Dei-lhe o livro</b>. Ils passent <b>devant</b> après une négation, un mot interrogatif, <b>que</b>, et des mots comme <b>já, também, sempre, só</b> : <b>Não o vi</b>, <b>Já lhe disse</b>. Après un verbe qui finit par <b>-r, -s, -z</b>, le pronom devient <b>-lo, -la, -los, -las</b> et la consonne tombe : <b>comprar + o → comprá-lo</b>. Après <b>-m, -ão, -õe</b>, il devient <b>-no, -na</b> : <b>compram-na</b>.",
"tableau": [
 ["vi-o · vi-a · vi-os · vi-as", "je l'ai vu(e), je les ai vu(e)s", "Conheces o Rui? Conheço-o bem."],
 ["dei-lhe · dei-lhes", "je lui ai donné, je leur ai donné", "Telefonei-lhe ontem."],
 ["não o vi · já lhe disse", "devant : après não, já, que…", "Não a conheço."],
 ["comprar + o → comprá-lo", "-r, -s, -z tombent : -lo, -la", "Vou fazê-lo amanhã."],
 ["fazemos + o → fazemo-lo", "", "Fazemo-lo juntos."],
 ["compram + a → compram-na", "après -m, -ão : -no, -na", "Dão-no aos filhos."],
],
"exemples": [
 ["Onde está o meu casaco? — Deixaste-o no carro.", "Où est mon manteau ? — Tu l'as laissé dans la voiture."],
 ["Ainda não lhe respondi.", "Je ne lui ai pas encore répondu."],
 ["Este bolo está ótimo, tens de prová-lo.", "Ce gâteau est excellent, tu dois le goûter."],
],
"attention": "<b>Lhe</b> est un complément indirect : <b>ajudar alguém</b> est direct en portugais, donc <b>ajudo-o</b> (je l'aide), pas « ajudo-lhe ». À l'inverse, <b>telefonar a alguém</b> : <b>telefono-lhe</b>.",
"serie": "pronomesComplementoPtExercises", "kicker": "Le pronom complément",
"questions": """
Conheces a Marta? — Sim, conheço-___ bem. | a | lhe / la | Tu connais Marta ? — Oui, je la connais bien. | Complément direct féminin : a.
O livro? Ainda não ___ li. | o | lo / lhe | Le livre ? Je ne l'ai pas encore lu. | Après não, le pronom passe devant : não o li.
Telefonei-___ ontem à noite. | lhe | o / a | Je lui ai téléphoné hier soir. | Telefonar a alguém : complément indirect, lhe.
Vou comprar este casaco. Vou comprá-___. | lo | o / no | Je vais acheter ce manteau. Je vais l'acheter. | Après -r : le r tombe, o devient lo (comprá-lo).
Os bilhetes? Eles compraram-___ ontem. | nos | os / los | Les billets ? Ils les ont achetés hier. | Après -m : os devient nos (compraram-nos).
Já ___ disse que não posso. | lhe | o / lhes a | Je lui ai déjà dit que je ne peux pas. | Après já, le pronom passe devant.
A sopa? Fizemo-___ juntos. | la | a / na | La soupe ? Nous l'avons faite ensemble. | Après -s : le s tombe, a devient la (fizemo-la).
Onde estão as chaves? Não ___ encontro. | as | las / lhes | Où sont les clés ? Je ne les trouve pas. | Après não : as, devant le verbe.
Dei-___ um presente aos meus pais. | lhes | os / lhe | J'ai offert un cadeau à mes parents. | À plusieurs personnes, complément indirect : lhes.
Podes ajudar-___? Tenho muitas malas. | me | lhe / mim | Tu peux m'aider ? J'ai beaucoup de valises. | Ajudar alguém : complément direct ; me.
O carro? Vendi-___ no ano passado. | o | lo / no | La voiture ? Je l'ai vendue l'an dernier. | Après une voyelle (vendi), o reste o.
O que ___ disseste? | lhe | o / a | Qu'est-ce que tu lui as dit ? | Après un mot interrogatif, le pronom passe devant.
Vês aquele prédio? Constroem-___ há dois anos. | no | o / lo | Tu vois cet immeuble ? Ils le construisent depuis deux ans. | Après -m : o devient no.
Quero ver o filme. Queres vê-___ comigo? | lo | o / no | Je veux voir le film. Tu veux le voir avec moi ? | Ver + o : vê-lo.
"""
},
{
"id": "imperativo", "titre": "L'impératif : fala, fale, não fales", "resume": "donner un ordre, un conseil, un chemin",
"regle": "Avec <b>tu</b>, l'impératif est la forme du présent de <b>ele</b> : <b>fala</b>, <b>come</b>, <b>abre</b>. Avec <b>você</b>, <b>o senhor</b>, <b>a senhora</b> (le vouvoiement), et avec <b>vocês</b>, on prend le subjonctif présent : <b>fale</b>, <b>coma</b>, <b>falem</b>. À la forme <b>négative</b>, c'est toujours le subjonctif, même avec tu : <b>não fales</b>, <b>não comas</b>. Les pronoms suivent l'impératif affirmatif (<b>diz-me</b>, <b>senta-te</b>) et précèdent le négatif (<b>não me digas</b>).",
"tableau": [
 ["fala! · come! · abre!", "tu, affirmatif (présent de ele)", "Fala mais devagar, por favor."],
 ["não fales · não comas · não abras", "tu, négatif (subjonctif)", "Não comas tanto açúcar."],
 ["fale · coma · abra", "o senhor, a senhora, você", "Siga em frente e vire à direita."],
 ["falem · comam · abram", "vocês", "Entrem, a porta está aberta!"],
 ["sê · vai · faz · diz · põe · vem", "les irréguliers avec tu", "Vem cá! Diz-me a verdade."],
 ["senta-te · não te sentes", "les pronoms", "Senta-te, por favor."],
],
"exemples": [
 ["Vira na segunda rua à esquerda.", "Tourne dans la deuxième rue à gauche."],
 ["Não te preocupes, eu trato disso.", "Ne t'inquiète pas, je m'en occupe."],
 ["Desculpe, pode repetir?", "Excusez-moi, vous pouvez répéter ?"],
],
"attention": "Pour une demande polie, le Portugal préfère souvent une question à l'impératif : <b>Podes fechar a janela?</b>, <b>Importa-se de esperar?</b> (Cela vous dérange d'attendre ?).",
"serie": "imperativoPtExercises", "kicker": "L'impératif",
"questions": """
___ a janela, por favor, está frio. | Fecha | Fechas / Feche-te | Ferme la fenêtre, s'il te plaît, il fait froid. | Tu, affirmatif : la forme de ele (fecha).
Não ___ tão alto, o bebé está a dormir. | fales | fala / falas | Ne parle pas si fort, le bébé dort. | Tu, négatif : le subjonctif (não fales).
Desculpe, ___ em frente e depois vire à esquerda. | siga | segue / sigas | Excusez-moi, continuez tout droit puis tournez à gauche. | O senhor / a senhora : le subjonctif (siga).
Meninos, ___ para a mesa, o jantar está pronto! | venham | vem / vêm | Les enfants, venez à table, le dîner est prêt ! | Vocês : le subjonctif (venham).
___ cá, quero mostrar-te uma coisa. | Vem | Venha-te / Vens | Viens ici, je veux te montrer quelque chose. | Vir, avec tu : vem.
Não te ___, chegamos a tempo. | preocupes | preocupa / preocupas | Ne t'inquiète pas, nous arriverons à temps. | Négatif : não te preocupes.
___ paciente, o médico já vem. | Sê | És / Seja-te | Sois patient, le médecin arrive. | Ser, avec tu : sê.
___-me a verdade! | Diz | Dizes / Diga-te | Dis-moi la vérité ! | Dizer, avec tu : diz ; le pronom suit (diz-me).
Por favor, ___-se. | sente | senta / sentes | Asseyez-vous, je vous prie. | O senhor : sente-se.
Não ___ a porta a ninguém! | abras | abre / abres | N'ouvre la porte à personne ! | Négatif, tu : não abras.
___ o casaco, que vai chover. | Leva | Levas / Leve-te | Prends ton manteau, il va pleuvoir. | Tu, affirmatif : leva.
Não ___ tarde, por favor. | cheguem | chegam / chega | N'arrivez pas en retard, s'il vous plaît. | Vocês, négatif : cheguem (g → gu devant e).
___ os sapatos à entrada. | Tira | Tiras / Tire-te | Enlève tes chaussures à l'entrée. | Tu : tira.
___ a mesa, por favor, os convidados estão a chegar. | Põe | Pões / Ponhas | Mets la table, s'il te plaît, les invités arrivent. | Pôr, avec tu : põe.
"""
},
{
"id": "obrigacao", "titre": "Ter de, dever, é preciso", "resume": "l'obligation, le conseil, l'interdiction",
"regle": "Au Portugal, l'obligation se dit surtout <b>ter de</b> + infinitif : <b>Tenho de trabalhar</b> (je dois travailler). <b>Dever</b> + infinitif est plus doux, un conseil ou une probabilité : <b>Deves descansar</b> (tu devrais te reposer), <b>Ele deve estar em casa</b> (il doit être chez lui). <b>É preciso</b> / <b>é necessário</b> + infinitif : une obligation générale. <b>Precisar de</b> : avoir besoin de (<b>Preciso de ajuda</b>, <b>Preciso de sair</b>). L'interdiction : <b>não se pode</b>, <b>é proibido</b>.",
"tableau": [
 ["ter de + infinitif", "devoir, être obligé de", "Temos de sair às oito."],
 ["dever + infinitif", "devoir (conseil, probabilité)", "Devias ligar à tua mãe."],
 ["é preciso + infinitif", "il faut", "É preciso marcar com antecedência."],
 ["precisar de + nom / infinitif", "avoir besoin de", "Preciso de um táxi."],
 ["não é preciso", "ce n'est pas la peine", "Não é preciso trazer nada."],
 ["não se pode · é proibido", "on ne peut pas · il est interdit", "É proibido fumar."],
],
"exemples": [
 ["Amanhã tenho de acordar às seis.", "Demain, je dois me lever à six heures."],
 ["Não precisas de vir, eu levo as malas.", "Tu n'as pas besoin de venir, je porte les valises."],
 ["Deve haver um engano na conta.", "Il doit y avoir une erreur dans l'addition."],
],
"attention": "Le Brésil dit <b>ter que</b> ; le Portugal dit <b>ter de</b>. Et <b>precisar</b> veut sa préposition : <b>preciso de</b> (et non « preciso ajuda »).",
"serie": "obrigacaoPtExercises", "kicker": "L'obligation",
"questions": """
Amanhã ___ de trabalhar até tarde. | tenho | devo / preciso | Demain, je dois travailler tard. | L'obligation : ter de.
Estás com febre, ___ ir ao médico. | devias | tens / precisas | Tu as de la fièvre, tu devrais aller chez le médecin. | Un conseil : dever (à l'imperfeito, plus doux).
___ preciso reservar mesa ao fim de semana. | É | Há / Tem | Il faut réserver une table le week-end. | Il faut : é preciso.
Preciso ___ um táxi para o aeroporto. | de | que / a | J'ai besoin d'un taxi pour l'aéroport. | Precisar de : la préposition est obligatoire.
O Rui não atende, ___ estar a dormir. | deve | tem de / precisa de | Rui ne répond pas, il doit dormir. | La probabilité : dever.
Não é ___ trazer nada, já temos tudo. | preciso | precisa / devido | Ce n'est pas la peine d'apporter quoi que ce soit, nous avons déjà tout. | Não é preciso : pas la peine.
Aqui é ___ fumar. | proibido | proibida / proíbe | Ici, il est interdit de fumer. | É proibido + infinitif.
Nós temos ___ sair antes das oito. | de | que de / a | Nous devons partir avant huit heures. | Au Portugal : ter de (pas ter que).
Vocês ___ de mostrar o passaporte. | têm | tem / tens | Vous devez montrer le passeport. | Ter, 3e pers. du pluriel : têm (avec accent).
Ela precisa de ___ mais. | descansar | descansa / descansou | Elle a besoin de se reposer davantage. | Precisar de + infinitif.
Não se ___ estacionar aqui. | pode | deve / tem | On ne peut pas se garer ici. | L'interdiction : não se pode.
Tu não ___ de pedir desculpa, a culpa não foi tua. | tens | deves / precisas | Tu n'as pas à t'excuser, ce n'était pas ta faute. | Não ter de : ne pas être obligé.
"""
},
{
"id": "por-para", "titre": "Por ou para ?", "resume": "pour, par, à travers, vers — deux mots pour un",
"regle": "<b>Para</b> regarde vers un but : la destination (<b>Vou para Lisboa</b>), le destinataire (<b>É para ti</b>), le but (<b>para aprender</b>), l'échéance (<b>para sexta-feira</b>). <b>Por</b> regarde ce qu'on traverse ou ce qui cause : le passage (<b>passar pela ponte</b>), la cause (<b>por causa da chuva</b>), l'échange (<b>por dez euros</b>), le moyen (<b>por e-mail</b>), la durée approximative, l'agent du passif (<b>escrito por Saramago</b>). <b>Por</b> se contracte avec l'article : <b>pelo, pela, pelos, pelas</b>.",
"tableau": [
 ["para + lieu", "vers, à (destination)", "Amanhã parto para o Porto."],
 ["para + personne", "pour (destinataire)", "Este presente é para a Ana."],
 ["para + infinitif", "pour, afin de", "Estudo para passar no exame."],
 ["por / pelo / pela + lieu", "par, à travers", "Passámos pelo centro."],
 ["por + cause", "à cause de, pour", "Obrigado pela ajuda."],
 ["por + prix, moyen", "pour (échange), par", "Comprei-o por vinte euros. Mando por e-mail."],
],
"exemples": [
 ["Saímos para a praia às dez e voltámos pela marginal.", "Nous sommes partis pour la plage à dix heures et sommes revenus par le front de mer."],
 ["O trabalho é para segunda-feira.", "Le travail est pour lundi."],
 ["Fiquei em casa por causa da greve.", "Je suis resté à la maison à cause de la grève."],
],
"attention": "<b>Obrigado por</b> (merci pour) prend toujours <b>por</b> : <b>obrigado pelo jantar</b>. Et « par jour, par semaine » : <b>por dia</b>, <b>por semana</b> (ou <b>ao dia</b>).",
"serie": "porParaPtExercises", "kicker": "Por ou para ?",
"questions": """
Amanhã vou ___ Lisboa de comboio. | para | por / pela | Demain, je vais à Lisbonne en train. | La destination : para.
Obrigado ___ jantar, estava ótimo. | pelo | para o / por o | Merci pour le dîner, c'était excellent. | Obrigado por ; por + o = pelo.
Este bolo é ___ a avó. | para | por / pela | Ce gâteau est pour grand-mère. | Le destinataire : para.
Passámos ___ Coimbra no caminho. | por | para / em | Nous sommes passés par Coimbra en chemin. | Le passage : por.
Estudo português ___ falar com os meus sogros. | para | por / pelo | J'étudie le portugais pour parler avec mes beaux-parents. | Le but + infinitif : para.
Comprei esta bicicleta ___ cem euros. | por | para / pela | J'ai acheté ce vélo pour cent euros. | L'échange, le prix : por.
O relatório é ___ sexta-feira. | para | por / pela | Le rapport est pour vendredi. | L'échéance : para.
Ficámos em casa ___ causa da chuva. | por | para / pela | Nous sommes restés à la maison à cause de la pluie. | La cause : por causa de.
Mando-te as fotos ___ e-mail. | por | para / pelo | Je t'envoie les photos par courriel. | Le moyen : por.
Este livro foi escrito ___ Eça de Queirós. | por | para / pelo | Ce livre a été écrit par Eça de Queirós. | L'agent du passif : por.
Gosto de passear ___ praia ao fim da tarde. | pela | para a / por a | J'aime me promener sur la plage en fin d'après-midi. | Le parcours : por + a = pela.
Tomo este medicamento três vezes ___ dia. | por | para / pelo | Je prends ce médicament trois fois par jour. | Par jour : por dia.
Saímos de casa ___ o aeroporto às cinco. | para | por / pelo | Nous sommes partis de la maison pour l'aéroport à cinq heures. | La destination : para.
Troquei o casaco ___ um maior. | por | para / pelo | J'ai échangé le manteau contre un plus grand. | L'échange : trocar por.
"""
},
{
"id": "ja-ainda", "titre": "Já, ainda, ainda não, já não", "resume": "déjà, encore, pas encore, ne… plus",
"regle": "<b>Já</b> : déjà (<b>Já almocei</b>) ; en réponse, il veut dire « oui » : <b>Já fizeste os trabalhos? — Já.</b> <b>Ainda</b> : encore, toujours (<b>Ainda moro aqui</b>). <b>Ainda não</b> : pas encore (<b>Ainda não acabei</b>). <b>Já não</b> : ne… plus (<b>Já não fumo</b>). Avec un pronom complément, <b>já</b> et <b>ainda</b> le font passer devant le verbe : <b>Já te disse</b>, <b>Ainda não o vi</b>.",
"tableau": [
 ["já + verbe", "déjà", "Já conheço o Algarve."],
 ["— Já.", "oui (c'est fait)", "Já jantaste? — Já."],
 ["ainda", "encore, toujours", "Ainda está a chover."],
 ["ainda não", "pas encore", "Ainda não sei."],
 ["já não", "ne… plus", "Já não trabalho lá."],
 ["já te disse · ainda não o vi", "le pronom passe devant", "Já lhe telefonei."],
],
"exemples": [
 ["Já estiveste em Évora? — Ainda não.", "Tu es déjà allé à Évora ? — Pas encore."],
 ["Ainda tens o carro antigo? — Já não, vendi-o.", "Tu as encore ta vieille voiture ? — Non, plus maintenant, je l'ai vendue."],
 ["Já são dez horas!", "Il est déjà dix heures !"],
],
"attention": "« Ne… plus » se dit <b>já não</b> (dans cet ordre), pas « não mais ». <b>Não … mais</b> existe, mais veut dire « ne… plus jamais » dans une langue plus soutenue.",
"serie": "jaAindaPtExercises", "kicker": "Já, ainda",
"questions": """
___ almoçaste? — Já, obrigado. | Já | Ainda / Ainda não | Tu as déjà déjeuné ? — Oui, merci. | Déjà : já.
O Rui ___ não chegou, está atrasado. | ainda | já / mais | Rui n'est pas encore arrivé, il est en retard. | Pas encore : ainda não.
Eu ___ não fumo, deixei há dois anos. | já | ainda / mais | Je ne fume plus, j'ai arrêté il y a deux ans. | Ne… plus : já não.
___ está a chover? Queria sair. | Ainda | Já não / Já | Il pleut encore ? Je voulais sortir. | Encore, toujours : ainda.
Já ___ disse mil vezes! | te | -te / o te | Je te l'ai déjà dit mille fois ! | Après já, le pronom passe devant : já te disse.
Ainda não ___ vi, mas quero ver esse filme. | o | -o / lo | Je ne l'ai pas encore vu, mais je veux voir ce film. | Après ainda não : o, devant.
Tens fome? — ___ não, comi há pouco. | Já | Ainda / Mais | Tu as faim ? — Plus maintenant, j'ai mangé il y a peu. | Já não : ne… plus.
Ela ___ mora na mesma casa? | ainda | já não / já | Elle habite toujours dans la même maison ? | Toujours : ainda.
___ são onze horas, vamos embora. | Já | Ainda / Ainda não | Il est déjà onze heures, allons-nous-en. | Déjà : já.
Já fizeste a mala? — ___. Faço-a hoje à noite. | Ainda não | Já / Já não | Tu as déjà fait ta valise ? — Pas encore. Je la fais ce soir. | Pas encore : ainda não.
Ele ___ trabalha no banco? Pensei que tinha mudado. | ainda | já / mais | Il travaille encore à la banque ? Je pensais qu'il avait changé. | Encore : ainda.
"""
},
{
"id": "demonstrativos", "titre": "Este, esse, aquele · isto, isso, aquilo", "resume": "ici, là, là-bas : trois distances",
"regle": "Le portugais a trois démonstratifs, selon la distance : <b>este</b> (près de moi, ici : <b>aqui</b>), <b>esse</b> (près de toi, là : <b>aí</b>), <b>aquele</b> (loin des deux, là-bas : <b>ali, lá</b>). Ils s'accordent : <b>este, esta, estes, estas</b>. Les formes neutres, pour une chose qu'on ne nomme pas : <b>isto, isso, aquilo</b>. Ils se contractent avec <b>de</b> et <b>em</b> : <b>deste, desse, daquele, neste, nesse, naquele</b> ; et <b>aquele</b> avec <b>a</b> : <b>àquele</b>.",
"tableau": [
 ["este, esta · isto", "celui-ci (près de moi)", "Esta mala é minha. O que é isto?"],
 ["esse, essa · isso", "celui-là (près de toi)", "Essa camisola fica-te bem."],
 ["aquele, aquela · aquilo", "celui-là (loin)", "Aquele prédio ali é o hospital."],
 ["deste, desse, daquele", "de + démonstratif", "Gosto muito desta música."],
 ["neste, nesse, naquele", "em + démonstratif", "Neste momento estou ocupado."],
 ["isso mesmo!", "exactement !", "É isso mesmo."],
],
"exemples": [
 ["Este ano vamos de férias em julho.", "Cette année, nous partons en vacances en juillet."],
 ["Passas-me esse livro, por favor?", "Tu me passes ce livre, s'il te plaît ?"],
 ["Lembras-te daquele verão em Sagres?", "Tu te souviens de cet été à Sagres ?"],
],
"attention": "<b>Isso</b> sert aussi à reprendre ce que l'autre vient de dire : <b>Isso é verdade</b> (c'est vrai), <b>Por isso</b> (c'est pourquoi). Et le temps : <b>este mês</b> (ce mois-ci), <b>nesse dia</b> (ce jour-là), <b>naquela época</b> (à cette époque-là).",
"serie": "demonstrativosPtExercises", "kicker": "Les démonstratifs",
"questions": """
___ casaco que tens vestido é novo? | Esse | Este / Aquilo | Ce manteau que tu portes est neuf ? | Près de toi : esse.
O que é ___ aqui na minha mão? | isto | este / aquilo | Qu'est-ce que c'est, ça, dans ma main ? | Une chose non nommée, près de moi : isto.
Vês ___ castelo lá no alto? | aquele | este / esse | Tu vois ce château là-haut ? | Loin des deux : aquele.
Gosto muito ___ bairro onde moro. | deste | de este / neste | J'aime beaucoup ce quartier où j'habite. | De + este = deste.
___ momento não posso falar. | Neste | Em este / Deste | En ce moment, je ne peux pas parler. | Em + este = neste.
Lembras-te ___ dia na praia? | daquele | de aquele / naquele | Tu te souviens de ce jour à la plage ? | De + aquele = daquele.
___ ano vou aprender a nadar. | Este | Esse / Isto | Cette année, je vais apprendre à nager. | Le temps présent : este ano.
É ___ mesmo, tens razão. | isso | esse / isto | C'est exactement ça, tu as raison. | Reprendre ce que l'autre dit : isso.
Não percebo ___ que ele está a dizer. | aquilo | aquele / esse | Je ne comprends pas ce qu'il est en train de dire. | Aquilo que : ce que (là-bas, de lui).
___ sapatos são teus? Estão aí ao pé de ti. | Esses | Estes / Aqueles | Ces chaussures sont à toi ? Elles sont là, à côté de toi. | Près de toi : esses.
Naquela época não havia ___ tecnologias. | estas | estes / isto | À cette époque-là, ces technologies n'existaient pas. | Accord au féminin pluriel : estas.
Choveu muito ___ semana. | esta | este / isto | Il a beaucoup plu cette semaine. | Semana est féminin : esta.
"""
},
{
"id": "perifrases-a2", "titre": "Acabar de, voltar a, começar a, deixar de", "resume": "venir de, refaire, se mettre à, arrêter de",
"regle": "Quelques verbes + préposition + infinitif disent où en est l'action : <b>acabar de</b> (venir de : <b>Acabei de chegar</b>), <b>voltar a</b> (refaire : <b>Voltou a chover</b>), <b>começar a</b> (se mettre à), <b>deixar de</b> (arrêter de : <b>Deixei de fumar</b>), <b>continuar a</b> (continuer à : <b>Continua a trabalhar</b>), <b>estar para</b> (être sur le point de). Au Portugal, l'action en cours se dit <b>estar a</b> + infinitif, et ce qui dure, <b>andar a</b> + infinitif (<b>Ando a ler um livro ótimo</b>).",
"tableau": [
 ["acabar de + infinitif", "venir de", "Acabámos de jantar."],
 ["voltar a + infinitif", "re-, à nouveau", "Voltei a ver o filme."],
 ["começar a + infinitif", "commencer à, se mettre à", "Começou a nevar."],
 ["deixar de + infinitif", "arrêter de", "Ele deixou de beber café."],
 ["continuar a + infinitif", "continuer à", "Continuo a estudar à noite."],
 ["andar a + infinitif", "être en train de (ces temps-ci)", "Ando a aprender a tocar guitarra."],
],
"exemples": [
 ["O comboio acabou de partir.", "Le train vient de partir."],
 ["Depois do acidente, nunca mais voltou a conduzir.", "Après l'accident, il n'a plus jamais conduit."],
 ["Ando a dormir mal.", "Je dors mal ces temps-ci."],
],
"attention": "<b>Acabar de</b> au présent veut dire « venir de » (<b>Acabo de chegar</b> = je viens d'arriver) ; <b>acabar</b> sans préposition veut dire « finir » (<b>Acabo o trabalho às seis</b>).",
"serie": "perifrasesA2PtExercises", "kicker": "Venir de, arrêter de…",
"questions": """
Acabei ___ chegar, ainda não tirei o casaco. | de | a / por | Je viens d'arriver, je n'ai pas encore enlevé mon manteau. | Venir de : acabar de.
Ontem voltou ___ chover. | a | de / para | Hier, il a recommencé à pleuvoir. | Re-, à nouveau : voltar a.
Ela deixou ___ fumar no ano passado. | de | a / em | Elle a arrêté de fumer l'an dernier. | Arrêter de : deixar de.
De repente, o bebé começou ___ chorar. | a | de / por | Tout à coup, le bébé s'est mis à pleurer. | Se mettre à : começar a.
Apesar do frio, continuamos ___ ir à praia. | a | de / em | Malgré le froid, nous continuons à aller à la plage. | Continuer à : continuar a.
Ando ___ ler um livro muito bom. | a | de / lendo | Je suis en train de lire un très bon livre. | Ces temps-ci : andar a + infinitif.
O filme está ___ começar, despacha-te! | para | a / de | Le film est sur le point de commencer, dépêche-toi ! | Être sur le point de : estar para.
Estou ___ cozinhar, ligo-te daqui a pouco. | a | de / para | Je suis en train de cuisiner, je te rappelle dans un moment. | Au Portugal : estar a + infinitif.
O autocarro ___ de passar, temos de esperar pelo próximo. | acabou | deixou / voltou | Le bus vient de passer, nous devons attendre le prochain. | Venir de : acabar de.
Depois de anos, ___ a falar com o irmão. | voltou | acabou / deixou | Après des années, il a recommencé à parler à son frère. | Recommencer : voltar a.
O meu pai ___ de trabalhar aos sessenta e cinco anos. | deixou | acabou / voltou | Mon père a arrêté de travailler à soixante-cinq ans. | Arrêter : deixar de.
"""
},
]
