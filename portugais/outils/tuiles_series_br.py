# -*- coding: utf-8 -*-
"""Les series des tuiles de grammaire ecrites pour le Bresil (lot P5, 11 nov. 2026).

La conversion automatique (bresil.py) garde le « tu » et des usages du
Portugal (queres, moras, vieste, a vossa casa, vem ca, toda a semana, chumbou,
conhecemo-lo...) : ces series-ci sont donc reecrites en entier, avec « voce »,
et remplacent la serie europeenne dans portugais/datos-br/.

Meme format que tuiles_series.py et SERIES_BR de bresil_textes.py :
question | bonne | fausse / fausse | traduction | explication
"""

SERIES_BR_TUILES = {
"pronomesTonicosPtExercises": ("pronomes-tonicos", """
Este presente é para ___. | você | te / ti | Ce cadeau est pour toi. | Au Brésil, après une préposition : para você.
Você quer vir ___? | comigo | com mim / com eu | Tu veux venir avec moi ? | Com + mim = comigo.
Isto é para ___ ou para ele? | mim | eu / me | C'est pour moi ou pour lui ? | Après une préposition : mim.
Ela pensa muito em ___. | mim | eu / me | Elle pense beaucoup à moi. | Après em : mim.
Falaram de ___? | nós | conosco / nos | Ils ont parlé de nous ? | Après de : nós.
Você quer jantar ___? | conosco | com nós / connosco | Tu veux dîner avec nous ? | Com + nós = conosco (connosco au Portugal).
Comprei isto pensando ___. | nele | no ele / em ele | J'ai acheté ça en pensant à lui. | Em + ele = nele.
Esta bolsa é ___. | dela | de ela / sua dela | Ce sac est à elle. | De + ela = dela.
Já falei ___. | com eles | comeles / com os | J'ai déjà parlé avec eux. | Com eles, en deux mots.
Para ___, o melhor é a praia. | mim | me / eu | Pour moi, le mieux, c'est la plage. | Para mim : à mon avis.
Gosto muito de ___, Ana. | você | te / ti | Je t'aime beaucoup, Ana. | Gostar de + você.
Sem ___ não consigo! | você | te / tu | Sans toi, je n'y arrive pas ! | Après sem : você.
O senhor trouxe o passaporte ___? | com o senhor | consigo mesmo / com si | Vous avez votre passeport sur vous ? | Au Brésil, on dit com o senhor, com você.
"""),
"possessivosTuilePtExercises": ("possessivos-tuile", """
Esta é ___ irmã, a Rita. | minha | meu / minhas | Voici ma sœur, Rita. | Au Brésil, l'article devant le possessif est facultatif : minha irmã.
___ carro está na garagem. | Meu | Minha / Meus | Ma voiture est au garage. | Meu + nom masculin.
Onde estão ___ chaves? | suas | seus / sua | Où sont tes clés ? | Avec você : seu, sua — suas chaves.
O Pedro perdeu o celular ___. | dele | dela / deles | Pedro a perdu son téléphone. | Pour éviter l'ambiguïté de seu : o celular dele.
A Ana e a casa ___ são lindas. | dela | dele / delas | Ana et sa maison sont belles. | Dela : à elle.
Os vizinhos venderam a casa ___. | deles | dele / delas | Les voisins ont vendu leur maison. | Deles : à eux.
___ filhos estudam em Recife. | Nossos | Nossas / Nosso | Nos enfants étudient à Recife. | Nossos + nom masculin pluriel.
O senhor esqueceu o ___ casaco. | seu | teu / sua | Vous avez oublié votre manteau. | O senhor, a senhora → seu, sua.
Este livro é ___? — É meu. | seu | sua / teu | Ce livre est à toi ? — Il est à moi. | Avec você : seu.
A casa de ___ é muito pequena. | vocês | seu / vosso | Votre maison est très petite. | À plusieurs : de vocês (vosso ne se dit plus au Brésil).
Um amigo ___ vem jantar. | meu | de mim / o meu | Un ami à moi vient dîner. | Um amigo meu : un de mes amis.
Lavei ___ mãos. | as | as minhas / minhas | Je me suis lavé les mains. | Les parties du corps : l'article seul.
"""),
"horasDatasPtExercises": ("horas-datas", """
___ três horas. | São | É / Está | Il est trois heures. | Au pluriel : são duas, são três…
___ uma hora. | É | São / Está | Il est une heure. | Une heure, midi, minuit : é.
São duas e ___. | meia | meio / metade | Il est deux heures et demie. | E meia : et demie.
São ___ para as cinco. | quinze | um quarto / quarta | Il est cinq heures moins le quart. | Au Brésil : quinze para as cinco.
Almoçamos ao ___. | meio-dia | meia-dia / meio dia | Nous déjeunons à midi. | Meio-dia, avec un trait d'union.
O trem parte ___ oito. | às | a / as | Le train part à huit heures. | À + as = às.
O jogo é ___ uma. | à | às / a | Le match est à une heure. | À + a (uma hora) = à.
Hoje é dia ___ de março. | primeiro | um / primeira | Aujourd'hui, c'est le premier mars. | Le premier du mois : dia primeiro.
Estamos em ___. | 2026 | o 2026 / no 2026 | Nous sommes en 2026. | L'année, sans article : em 2026.
A reunião é ___ segunda-feira. | na | em a / à | La réunion est lundi. | Le jour : na segunda-feira.
O museu abre ___ terça a domingo. | de | desde / da | Le musée ouvre du mardi au dimanche. | De… a… : du… au…
São onze ___ dez. | e | com / mais | Il est onze heures dix. | Les minutes après : e.
Chego ___ das nove. | por volta | a volta / pela volta | J'arrive vers neuf heures. | Vers : por volta de.
"""),
"prepContracoesPtExercises": ("prep-contracoes", """
Moro ___ Rio. | no | em o / ao | J'habite à Rio. | Em + o = no.
O livro está ___ mesa. | na | em a / à | Le livre est sur la table. | Em + a = na.
Ele vem ___ Porto. | do | de o / ao | Il vient de Porto. | De + o = do.
Vamos ___ praia. | à | a a / da | Allons à la plage. | A + a = à (à l'oral, on entend aussi na praia).
Dei o livro ___ professor. | ao | a o / o | J'ai donné le livre au professeur. | A + o = ao.
Passei ___ ponte. | pela | pelo / por a | Je suis passé par le pont. | Por + a = pela.
Gosto ___ seu casaco. | do | o / de o | J'aime ton manteau. | Gostar de + o = do.
Ela está ___ escritório. | no | ao / em o | Elle est au bureau. | Em + o = no.
Moro ___ São Paulo. | em | no / na | J'habite à São Paulo. | Les villes sans article : em São Paulo.
Esta carta é ___ Ana. | da | à / de a | Cette lettre est d'Ana. | De + a = da.
Trabalho ___ hospital. | num | dum / no um | Je travaille dans un hôpital. | Em + um = num (ou em um, très courant au Brésil).
Saiu ___ casa às oito. | de | desde / pra | Il est sorti de chez lui à huit heures. | Sair de casa : de chez soi, sans article.
Vou ___ casa da minha mãe. | à | a a / em a | Je vais chez ma mère. | A + a casa = à casa (à l'oral, on entend aussi na casa).
Obrigado ___ ajuda. | pela | por a / para a | Merci pour l'aide. | Obrigado por : por + a = pela.
"""),
"verbosPrepPtExercises": ("verbos-prep", """
Gosto ___ chocolate. | de | o / em | J'aime le chocolat. | Gostar de.
Penso muito ___ você. | em | de / a | Je pense beaucoup à toi. | Pensar em.
Ela sonhou ___ o avô. | com | de / em | Elle a rêvé de son grand-père. | Sonhar com.
Preciso ___ ajuda. | de | a / em | J'ai besoin d'aide. | Precisar de.
Isso depende ___ tempo. | do | de o / ao | Ça dépend du temps. | Depender de : de + o = do.
Chegamos ___ São Paulo às dez. | a | para / de | Nous sommes arrivés à São Paulo à dix heures. | Chegar a (à l'oral, on entend aussi chegar em).
Você se lembra ___ mim? | de | a / em | Tu te souviens de moi ? | Lembrar-se de.
Ela casou ___ um médico. | com | de / a | Elle s'est mariée avec un médecin. | Casar com.
Nós nos esquecemos ___ chaves. | das | de as / as | Nous avons oublié les clés. | Esquecer-se de : de + as = das.
Confio ___ você. | em | de / a | J'ai confiance en toi. | Confiar em.
Ele se parece ___ pai. | com o | ao / do | Il ressemble à son père. | Parecer-se com.
Eu a ajudei ___ fazer as malas. | a | para / de | Je l'ai aidée à faire les valises. | Ajudar alguém a + infinitif.
Desisti ___ curso. | do | ao / o | J'ai abandonné le cours. | Desistir de.
Ela riu ___ piada. | da | com a / à | Elle a ri de la blague. | Rir de.
Ele se interessa ___ arte. | por | de / em | Il s'intéresse à l'art. | Interessar-se por.
"""),
"porqueEmboraPtExercises": ("porque-embora", """
Fiquei em casa ___ estava doente. | porque | embora / mas | Je suis resté à la maison parce que j'étais malade. | La cause : porque + indicatif.
___ estivesse doente, fui trabalhar. | Embora | Porque / Como | Bien que je sois malade, je suis allé travailler. | L'opposition : embora + subjuntivo.
___ estava chovendo, ficamos em casa. | Como | Embora / Mas | Comme il pleuvait, nous sommes restés à la maison. | Como en tête : la cause.
Não fui à festa ___ estava cansado. | pois | embora / mas | Je ne suis pas allé à la fête, car j'étais fatigué. | Car : pois.
Gosto de café, ___ prefiro chá. | mas | porque / embora | J'aime le café, mais je préfère le thé. | Mais : mas.
___ do frio, fomos à praia. | Apesar | Embora / Porque | Malgré le froid, nous sommes allés à la plage. | Apesar de + nom.
Saímos ___ chovesse. | embora | porque / apesar | Nous sommes sortis bien qu'il pleuve. | Embora + subjuntivo.
Cancelaram o jogo ___ da chuva. | por causa | porque / embora | Ils ont annulé le match à cause de la pluie. | À cause de : por causa de.
Estudou muito; ___, foi reprovado. | no entanto | porque / como | Il a beaucoup étudié ; pourtant, il a échoué. | Pourtant : no entanto.
Está calor, ___ vamos à praia. | por isso | embora / porque | Il fait chaud, alors nous allons à la plage. | La conséquence : por isso.
Não comprei o casaco ___ era caro demais. | porque | embora / por causa | Je n'ai pas acheté le manteau parce qu'il était trop cher. | Porque + phrase.
___ tenha pouco dinheiro, viaja muito. | Embora | Porque / Como | Bien qu'il ait peu d'argent, il voyage beaucoup. | Embora + subjuntivo (tenha).
"""),
"quandoEnquantoPtExercises": ("quando-enquanto", """
___ cheguei, eles já tinham jantado. | Quando | Enquanto / Até que | Quand je suis arrivé, ils avaient déjà dîné. | Quand, au passé : quando + indicatif.
___ eu cozinho, ele põe a mesa. | Enquanto | Desde / Até que | Pendant que je cuisine, il met la table. | Pendant que : enquanto.
Eu te ligo ___ chegar. | assim que | enquanto / até que | Je t'appelle dès que j'arrive. | Dès que : assim que + futuro do subjuntivo.
Espere aqui ___ eu voltar. | até | enquanto / desde | Attends ici jusqu'à ce que je revienne. | Até + infinitif personnel (ou até que + subjuntivo).
___ que moro em São Paulo, ando de metrô. | Desde | Até / Assim | Depuis que j'habite à São Paulo, je prends le métro. | Depuis que : desde que + indicatif.
Lave as mãos ___ de comer, não depois! | antes | depois / enquanto | Lave-toi les mains avant de manger, pas après ! | Avant de : antes de + infinitif.
Primeiro jantamos; ___, vimos um filme. | depois | antes / quando | D'abord nous avons dîné ; ensuite, nous avons regardé un film. | Ensuite : depois.
___ era criança, morava no interior. | Quando | Enquanto / Desde | Quand j'étais enfant, j'habitais à la campagne. | Quando + imperfeito.
Sempre que ___ ao Rio, como uma feijoada. | vou | vá / ir | Chaque fois que je vais à Rio, je mange une feijoada. | Une habitude : sempre que + indicatif.
Logo que ___ notícias, eu te aviso. | tiver | tenho / tenha | Dès que j'aurai des nouvelles, je te préviendrai. | Logo que + futur : tiver.
Fiquei acordado ___ ele chegar. | até | enquanto / desde | Je suis resté éveillé jusqu'à ce qu'il arrive. | Jusqu'à ce que : até + infinitif personnel.
"""),
"seCasoPtExercises": ("se-caso", """
___ chover, ficamos em casa. | Se | Quando que / Caso | S'il pleut, nous restons à la maison. | Se + futuro do subjuntivo (chover).
___ chova, levo o guarda-chuva. | Caso | Quando / Se | Au cas où il pleuvrait, je prends le parapluie. | Caso + subjuntivo présent (chova).
Vou, ___ que me paguem. | desde | se / caso | J'y vais, à condition qu'on me paie. | À condition que : desde que + subjuntivo.
Vou a pé, a não ser que ___. | chova | chove / chover | J'y vais à pied, à moins qu'il pleuve. | A não ser que + subjuntivo.
Se eu ___ rico, comprava um barco. | fosse | for / sou | Si j'étais riche, j'achèterais un bateau. | L'irréel : se + imperfeito do subjuntivo.
Se ___ tempo amanhã, vamos à praia. | tivermos | temos / tivéssemos | Si nous avons le temps demain, nous irons à la plage. | Le futur possible : se + futuro do subjuntivo.
Não sei ___ ele vem. | se | que se / caso | Je ne sais pas s'il vient. | La question indirecte : se.
Me ligue ___ precise de alguma coisa. | caso | quando / se | Appelle-moi si tu as besoin de quelque chose. | Caso + subjuntivo présent (precise).
Se eu ___ sabido, teria vindo. | tivesse | tiver / tinha | Si j'avais su, je serais venu. | Se + mais-que-perfeito do subjuntivo.
Leve o casaco, ___ faça frio. | caso | se / quando | Prends le manteau, au cas où il ferait froid. | Caso + subjuntivo présent (faça).
"""),
"ordemAdjetivoPtExercises": ("ordem-adjetivo", """
Comprei um carro ___. | novo | nova / novos | J'ai acheté une voiture neuve. | L'adjectif se met en général après le nom.
Ela tem olhos ___. | verdes | verdas / verde | Elle a les yeux verts. | Verde, verdes : même forme au masculin et au féminin.
O Rui é um ___ amigo. | bom | bem / boa | Rui est un bon ami. | Bom se met souvent devant le nom.
Salvador é uma cidade ___. | bonita | bonitas / bonito | Salvador est une belle ville. | Bonita : accord au féminin.
Foi um ___ homem. | grande | grandes / grando | Ce fut un grand homme. | Devant le nom, grande = remarquable.
Ele é um homem ___: mede dois metros. | grande | grandes / grand | C'est un homme grand : il mesure deux mètres. | Après le nom, grande = de grande taille.
É um ___ amigo da família: nós o conhecemos há trinta anos. | velho | velha / velhos | C'est un vieil ami de la famille : nous le connaissons depuis trente ans. | Avant le nom, velho = de longue date.
Moram numa casa ___ e escura. | pequena | pequeno / pequenas | Ils habitent une maison petite et sombre. | Deux adjectifs coordonnés : après le nom.
Gosto de vinho ___. | tinto | tintos / tinta | J'aime le vin rouge. | Vinho tinto : le vin rouge.
Pobre ___! Perdeu tudo. | homem | do homem / homem pobre | Le pauvre homme ! Il a tout perdu. | Devant le nom, pobre = malheureux.
É a ___ vez que eu te digo isso. | última | último / ultima | C'est la dernière fois que je te le dis. | Última, avec l'accent.
Tenho uma ___ notícia para você. | boa | bem / bom | J'ai une bonne nouvelle pour toi. | Boa + nom féminin.
"""),
"perguntasOrdemPtExercises": ("perguntas-ordem", """
Onde ___ você mora? | é que | que é / és que | Où est-ce que tu habites ? | À l'oral : interrogatif + é que.
O que você ___ fazendo? | está | é / estás | Qu'est-ce que tu es en train de faire ? | Estar + gérondif.
Por que você não ___? | veio | vieste / vem-se | Pourquoi n'es-tu pas venu ? | Por que, en deux mots, pour poser la question.
Como você ___ chama? | se | te / si | Comment tu t'appelles ? | Você se chama.
Quanto ___ este casaco? | custa | custas / se custa | Combien coûte ce manteau ? | Le verbe s'accorde avec ce qu'on achète.
Seu aniversário é amanhã, ___? | né | não é verdade que / pois | Ton anniversaire est demain, n'est-ce pas ? | À l'oral : né ? (não é ?).
Você já jantou? — ___. | Já | Sim, jantou / Jantaste | Tu as déjà dîné ? — Oui. | On répond par le mot clé : já.
De onde você ___? | é | está / és | D'où viens-tu ? | Ser de : l'origine.
Com quem você ___ ontem? | falou | falaste / se falou | Avec qui as-tu parlé hier ? | Você + verbe à la 3e personne.
A que horas ___ o filme? | começa | começas / se começa | À quelle heure commence le film ? | Dans la question, le sujet suit souvent le verbe.
Qual ___ o seu número? | é | e / está | Quel est ton numéro ? | Qual é… ?
Você ___ o quê? | disse | dizes / se disse | Tu as dit quoi ? | À l'oral, o quê en fin de phrase.
"""),
"adverbiosFamiliaPtExercises": ("adverbios-familia", """
Vou à academia toda ___. | semana | a semana / semanas | Je vais à la salle de sport chaque semaine. | Au Brésil : toda semana (sans article) = chaque semaine.
___ vou à praia no domingo. | Às vezes | Vezes / As vezes | Parfois, je vais à la plage le dimanche. | Às vezes, avec l'accent grave.
Ele chega ___ atrasado. | sempre | jamais / nunca não | Il arrive toujours en retard. | Sempre : toujours.
Moro ___, perto da escola. | aqui | lá longe / ali longe | J'habite ici, près de l'école. | Aqui : là où je suis.
O café fica ___, do outro lado da rua. | ali | aqui / cá | Le café est là-bas, de l'autre côté de la rue. | Ali : là-bas, qu'on peut montrer.
Vem ___! | aqui | aí / lá | Viens ici ! | Au Brésil : vem aqui (vem cá se dit aussi).
Comi ___. | demais | muito de / demasiado de | J'ai trop mangé. | Demais après le verbe : trop.
Ele é ___ simpático. | bastante | bastantes / bastante de | Il est assez sympathique. | Bastante devant un adjectif ne varie pas.
___ chove em agosto. | Raramente | Raramento / Raro | Il pleut rarement en août. | Raro → raramente.
Fala ___ alto! | tão | tanto / muito tão | Il parle si fort ! | Tão + adjectif ou adverbe.
Estou ___ cansado. | muito | muito de / bem de | Je suis très fatigué. | Muito : très.
___, faça o que você quiser. | Enfim | Afim / Fim | Bref, fais ce que tu veux. | Enfim : bref, enfin.
"""),
"falsosAmigosTuilePtExercises": ("falsos-amigos-tuile", """
Hoje vou ___ às sete. (me réveiller) | acordar | me acordar / despertar-me | Aujourd'hui, je vais me réveiller à sept heures. | Acordar = se réveiller (pas « accorder »).
Comprei ___ para o sanduíche. (du jambon) | presunto | jambão / salame | J'ai acheté du jambon pour le sandwich. | Presunto = le jambon (pas un « présumé »).
O ___ é um animal com oito braços. (la pieuvre) | polvo | pó / poulpo | La pieuvre a huit bras. | Polvo = la pieuvre.
Esse cara é muito ___. (agaçant) | chato | chateado / gato | Ce type est très agaçant. | Chato = pénible (pas « chat »).
Estou ___ com esse barulho. (agacé) | chateado | chato / chatice | Je suis agacé par ce bruit. | Chateado = contrarié, agacé.
Ela está ___: vai ter um bebê. | grávida | grave / gravada | Elle est enceinte : elle va avoir un bébé. | Grávida = enceinte (pas « grave »).
Deixei a ___ com os documentos no carro. (la chemise) | pasta | massa / macarrão | J'ai laissé la chemise avec les documents dans la voiture. | Pasta = chemise, porte-documents ; les pâtes = o macarrão.
Vou ___ o telefone. (répondre au) | atender | esperar / atentar | Je vais répondre au téléphone. | Atender = répondre, accueillir (pas « attendre »).
Ontem ___ um jogo de futebol na televisão. (j'ai regardé) | assisti a | atendi / assisti | Hier, j'ai regardé un match à la télé. | Assistir a = regarder (un spectacle).
Passamos o fim de semana num ___. (une petite ferme) | sítio | site / lugarzinho | Nous avons passé le week-end dans une petite propriété à la campagne. | Au Brésil, sítio = petite propriété rurale (pas « site »).
Comi um ___ de chocolate. (un gâteau) | bolo | bol / bolinha | J'ai mangé un gâteau au chocolat. | Bolo = gâteau ; le bol = a tigela.
Bebi um ___ de água. (un verre) | copo | taça / copa | J'ai bu un verre d'eau. | Copo = verre ; a copa = la Coupe (du monde).
A ___ de hoje é pudim. (le dessert) | sobremesa | sobre-mesa / desserto | Le dessert d'aujourd'hui, c'est le flan. | A sobremesa = le dessert.
Ele vestiu um ___ azul para o casamento. (un costume) | terno | fato / costume | Il a mis un costume bleu pour le mariage. | Au Brésil : terno ; costume = l'habitude, fato = un fait.
É ___ dele acordar cedo. (son habitude) | costume | terno / hábito de | Il a l'habitude de se lever tôt. | Costume = coutume, habitude.
Recebi uma ___ da minha avó. (une lettre) | carta | letra / cartão | J'ai reçu une lettre de ma grand-mère. | Carta = lettre (courrier).
A ___ desta música é bonita. (les paroles) | letra | carta / palavra | Les paroles de cette chanson sont belles. | Letra = les paroles, ou une lettre de l'alphabet.
Ela tirou uma ___ excelente. (une note) | nota | notícia / ponto | Elle a eu une excellente note. | A nota = la note (scolaire, ou le billet).
Esta peça de teatro tem uma ___ muito bonita. (une scène) | cena | ceia / jantar | Cette pièce de théâtre a une très belle scène. | Cena = la scène ; a ceia = le souper.
Que ___! Perdi o ônibus. (Quel ennui) | chatice | chato / chateza | Quelle barbe ! J'ai raté le bus. | Chatice = un ennui, une corvée.
Joguei o papel na ___. (la poubelle) | lixeira | caixote / lixo | J'ai jeté le papier à la poubelle. | Au Brésil : a lixeira (caixote do lixo au Portugal).
"""),
}
