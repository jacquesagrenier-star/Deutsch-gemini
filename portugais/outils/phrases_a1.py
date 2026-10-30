# -*- coding: utf-8 -*-
"""Expressions et mots-outils de l'A1 portugais (du Portugal), avec leurs
phrases. SOURCE : on corrige ici, puis python portugais/outils/construire.py.

Ligne : « mot | traduction | categorie | phrase portugaise | sa traduction ».
La categorie s'affiche telle quelle (en francais, comme l'anglais).
Portugal d'abord : « se faz favor », « até já », « obrigado » accorde a celui
qui parle (une femme dit « obrigada »), « tu » entre proches, « o senhor / a
senhora » avec un inconnu (« voce » est delicat au Portugal).
"""

EXPRESSIONS = """
Olá! | Bonjour ! Salut ! | Saluer | Olá! Chamo-me Ana. | Bonjour ! Je m'appelle Ana.
Bom dia! | Bonjour ! (le matin) | Saluer | Bom dia! Dormiste bem? | Bonjour ! Tu as bien dormi ?
Boa tarde! | Bonjour ! (l'après-midi) | Saluer | Boa tarde, tem uma mesa para dois? | Bonjour, vous avez une table pour deux ?
Boa noite! | Bonsoir ! Bonne nuit ! | Saluer | Boa noite, até amanhã. | Bonne nuit, à demain.
Adeus! | Au revoir ! | Saluer | Adeus, até para a semana! | Au revoir, à la semaine prochaine !
Tchau! | Salut ! (en partant) | Saluer | Tchau, mãe! | Salut, maman !
Até logo! | À tout à l'heure ! À plus tard ! | Saluer | Tenho de ir. Até logo! | Je dois y aller. À plus tard !
Até já! | À tout de suite ! | Saluer | Vou só à padaria. Até já! | Je vais juste à la boulangerie. À tout de suite !
Até amanhã! | À demain ! | Saluer | Até amanhã às nove. | À demain, à neuf heures.
Como estás? | Comment vas-tu ? | Se présenter | Olá, Rui! Como estás? | Salut, Rui ! Comment vas-tu ?
Tudo bem? | Ça va ? | Se présenter | Olá! Tudo bem? — Tudo, e contigo? | Salut ! Ça va ? — Oui, et toi ?
Estou bem, obrigado. | Je vais bien, merci. | Se présenter | Estou bem, obrigada. E tu? | Je vais bien, merci. Et toi ?
Muito prazer. | Enchanté. | Se présenter | Sou a Marta. — Muito prazer, Marta. | Je suis Marta. — Enchanté, Marta.
Como te chamas? | Comment tu t'appelles ? | Se présenter | Como te chamas? — Chamo-me Paulo. | Comment tu t'appelles ? — Je m'appelle Paulo.
Chamo-me… | Je m'appelle… | Se présenter | Chamo-me Marie e sou francesa. | Je m'appelle Marie et je suis française.
De onde és? | D'où viens-tu ? | Se présenter | De onde és? — Sou de Montreal. | D'où viens-tu ? — Je suis de Montréal.
Sou de… | Je suis de… | Se présenter | Sou de França, mas vivo no Canadá. | Je suis de France, mais je vis au Canada.
Quantos anos tens? | Quel âge as-tu ? | Se présenter | Quantos anos tens? — Tenho vinte e cinco. | Quel âge as-tu ? — J'en ai vingt-cinq.
Por favor. | S'il vous plaît. S'il te plaît. | Politesse | Um café, por favor. | Un café, s'il vous plaît.
Se faz favor. | S'il vous plaît. (au Portugal) | Politesse | A conta, se faz favor. | L'addition, s'il vous plaît.
Obrigado. | Merci. (dit par un homme) | Politesse | Obrigado pela ajuda. | Merci pour ton aide.
Obrigada. | Merci. (dite par une femme) | Politesse | Obrigada, é muito simpático. | Merci, c'est très gentil.
Muito obrigado. | Merci beaucoup. | Politesse | Muito obrigado por tudo. | Merci beaucoup pour tout.
De nada. | De rien. | Politesse | Obrigada! — De nada. | Merci ! — De rien.
Com licença. | Pardon, vous permettez ? | Politesse | Com licença, posso passar? | Pardon, je peux passer ?
Desculpe. | Excusez-moi. | Politesse | Desculpe, onde fica a estação? | Excusez-moi, où est la gare ?
Peço desculpa. | Je suis désolé. | Politesse | Peço desculpa, estou atrasado. | Je suis désolé, je suis en retard.
Não faz mal. | Ce n'est pas grave. | Politesse | Desculpa! — Não faz mal. | Pardon ! — Ce n'est pas grave.
Claro! | Bien sûr ! | Réagir | Posso sentar-me aqui? — Claro! | Je peux m'asseoir ici ? — Bien sûr !
Sim. | Oui. | Réagir | Tens fome? — Sim, muita! | Tu as faim ? — Oui, très !
Não. | Non. | Réagir | Queres chá? — Não, obrigado. | Tu veux du thé ? — Non, merci.
Está bem. | D'accord. | Réagir | Encontramo-nos às seis? — Está bem! | On se retrouve à six heures ? — D'accord !
Eu também. | Moi aussi. | Réagir | Adoro esta canção. — Eu também! | J'adore cette chanson. — Moi aussi !
Não sei. | Je ne sais pas. | Réagir | Onde está o Rui? — Não sei. | Où est Rui ? — Je ne sais pas.
Tanto faz. | Peu importe. Ça m'est égal. | Réagir | Para mim, a hora tanto faz. | L'heure m'est égale.
Que giro! | Que c'est mignon ! Génial ! | Réagir | Olha este cão! Que giro! | Regarde ce chien ! Qu'il est mignon !
Fixe! | Super ! Cool ! | Réagir | Vamos à praia amanhã? — Fixe! | On va à la plage demain ? — Super !
Não percebo. | Je ne comprends pas. | En classe | Desculpe, não percebo. | Excusez-moi, je ne comprends pas.
Pode repetir? | Pouvez-vous répéter ? | En classe | Pode repetir, por favor? | Pouvez-vous répéter, s'il vous plaît ?
Mais devagar, por favor. | Plus lentement, s'il vous plaît. | En classe | Fale mais devagar, por favor. | Parlez plus lentement, s'il vous plaît.
Como se diz…? | Comment dit-on… ? | En classe | Como se diz « merci » em português? | Comment dit-on « merci » en portugais ?
O que quer dizer…? | Que veut dire… ? | En classe | O que quer dizer « saudade »? | Que veut dire « saudade » ?
Queria… | Je voudrais… | Au quotidien | Queria um galão e uma torrada. | Je voudrais un grand café au lait et une tartine.
Quanto custa? | Combien ça coûte ? | Au quotidien | Quanto custa esta camisa? | Combien coûte cette chemise ?
A conta, se faz favor. | L'addition, s'il vous plaît. | Au quotidien | Desculpe, a conta, se faz favor. | Excusez-moi, l'addition, s'il vous plaît.
Para levar. | À emporter. | Au quotidien | Um café para levar. | Un café à emporter.
Que horas são? | Quelle heure est-il ? | Au quotidien | Desculpe, que horas são? | Excusez-moi, quelle heure est-il ?
São três e um quarto. | Il est trois heures et quart. | Au quotidien | Já são três e um quarto: estamos atrasados. | Il est déjà trois heures et quart : nous sommes en retard.
É uma e meia. | Il est une heure et demie. | Au quotidien | É uma e meia, vamos almoçar? | Il est une heure et demie, on va déjeuner ?
em ponto | pile (à l'heure exacte) | Au quotidien | Ele chegou às nove em ponto. | Il est arrivé à neuf heures pile.
todos os dias | tous les jours | Au quotidien | Estudo português todos os dias. | J'étudie le portugais tous les jours.
de carro | en voiture | Au quotidien | Vamos de carro até à praia. | Nous allons en voiture jusqu'à la plage.
ter saudades de | manquer à quelqu'un | Au quotidien | Tenho saudades da minha família. | Ma famille me manque.
ter vontade de | avoir envie de | Au quotidien | Tenho vontade de ir à praia. | J'ai envie d'aller à la plage.
Bom apetite! | Bon appétit ! | Vœux | Aqui está. Bom apetite! | Voilà. Bon appétit !
Saúde! | Santé ! À tes souhaits ! | Vœux | Saúde! Aos amigos! | Santé ! Aux amis !
Parabéns! | Joyeux anniversaire ! Félicitations ! | Vœux | Parabéns! Quantos anos fazes? | Joyeux anniversaire ! Tu as quel âge ?
Bom fim de semana! | Bon week-end ! | Vœux | Até segunda! Bom fim de semana! | À lundi ! Bon week-end !
Boa viagem! | Bon voyage ! | Vœux | Boa viagem e manda notícias! | Bon voyage, et donne des nouvelles !
Feliz Natal! | Joyeux Noël ! | Vœux | Feliz Natal e bom Ano Novo! | Joyeux Noël et bonne année !
Felicidades! | Bonne continuation ! | Vœux | Adeus, Marta, felicidades! | Au revoir, Marta, bonne continuation !
"""

# Les mots-outils, ranges comme ceux de l'anglais (cles du moteur commun).
FONCTIONNELS = {
"artikelwoerter": """
o | le | Articles | O livro está na mesa. | Le livre est sur la table.
a | la | Articles | A porta está aberta. | La porte est ouverte.
os | les (masc.) | Articles | Os meninos estão a dormir. | Les garçons dorment.
as | les (fém.) | Articles | As janelas estão fechadas. | Les fenêtres sont fermées.
um | un | Articles | Quero um café. | Je veux un café.
uma | une | Articles | Tenho uma pergunta. | J'ai une question.
uns | des (masc.) | Articles | Comprei uns livros usados. | J'ai acheté des livres d'occasion.
umas | des (fém.) | Articles | Tenho umas perguntas para ti. | J'ai quelques questions pour toi.
este | ce (ici) | Démonstratifs | Este bairro é muito bonito. | Ce quartier est très joli.
esta | cette (ici) | Démonstratifs | Esta semana tenho muito trabalho. | Cette semaine, j'ai beaucoup de travail.
estes | ces (ici) | Démonstratifs | Estes sapatos ficam-me grandes. | Ces chaussures sont trop grandes pour moi.
esse | ce (près de toi) | Démonstratifs | Passa-me esse caderno, por favor. | Passe-moi ce cahier, s'il te plaît.
essa | cette (près de toi) | Démonstratifs | Gosto dessa ideia. | Cette idée me plaît.
aquele | ce (là-bas) | Démonstratifs | Aquele prédio é do século quinze. | Ce bâtiment-là date du quinzième siècle.
aquela | cette (là-bas) | Démonstratifs | Aquela praça é a do Comércio. | Cette place-là, c'est celle du Commerce.
isto | ceci | Démonstratifs | Isto não funciona. | Ceci ne fonctionne pas.
isso | cela | Démonstratifs | Isso já eu sabia. | Ça, je le savais déjà.
aquilo | cela (là-bas) | Démonstratifs | O que é aquilo? | Qu'est-ce que c'est, là-bas ?
o meu | mon | Possessifs | O meu irmão mora em Faro. | Mon frère habite à Faro.
a minha | ma | Possessifs | A minha irmã é médica. | Ma sœur est médecin.
o teu | ton | Possessifs | O teu casaco está na cadeira. | Ta veste est sur la chaise.
a tua | ta | Possessifs | A tua mala está aqui. | Ton sac est ici.
o seu | son, votre | Possessifs | O senhor esqueceu-se do seu guarda-chuva. | Monsieur, vous avez oublié votre parapluie.
o nosso | notre | Possessifs | O nosso apartamento é pequeno. | Notre appartement est petit.
a nossa | notre (fém.) | Possessifs | A nossa equipa ganhou. | Notre équipe a gagné.
dele | son, sa (à lui) | Possessifs | Esta é a casa dele. | C'est sa maison (à lui).
dela | son, sa (à elle) | Possessifs | O carro dela é vermelho. | Sa voiture (à elle) est rouge.
""",
"pronomen": """
eu | je, moi | Pronoms | Eu moro em Lisboa. | Moi, j'habite à Lisbonne.
tu | tu | Pronoms | Tu falas inglês? | Tu parles anglais ?
ele | il | Pronoms | Ele trabalha num banco. | Il travaille dans une banque.
ela | elle | Pronoms | Ela é a minha irmã. | C'est ma sœur.
você | vous (à éviter souvent au Portugal) | Pronoms | Você é do Porto? | Vous êtes de Porto ?
o senhor | vous (à un homme) | Pronoms | O senhor mora aqui? | Vous habitez ici, monsieur ?
a senhora | vous (à une femme) | Pronoms | A senhora precisa de ajuda? | Vous avez besoin d'aide, madame ?
nós | nous | Pronoms | Nós vamos de comboio. | Nous, nous y allons en train.
a gente | on, nous (familier) | Pronoms | A gente vê-se amanhã. | On se voit demain.
vocês | vous (pluriel) | Pronoms | Vocês vêm amanhã? | Vous venez demain ?
eles | ils | Pronoms | Eles chegam amanhã. | Ils arrivent demain.
elas | elles | Pronoms | Elas chegaram primeiro. | Elles sont arrivées les premières.
me | me | Pronoms compléments | Ele telefonou-me ontem. | Il m'a appelé hier.
te | te | Pronoms compléments | Espero-te à porta. | Je t'attends à la porte.
se | se | Pronoms compléments | Ele levanta-se às seis. | Il se lève à six heures.
nos | nous | Pronoms compléments | Ela convidou-nos para jantar. | Elle nous a invités à dîner.
lhe | lui, vous | Pronoms compléments | Dei-lhe o livro ontem. | Je lui ai donné le livre hier.
o / a | le, la (complément) | Pronoms compléments | Conheço-a há anos. | Je la connais depuis des années.
mim | moi (après une préposition) | Pronoms compléments | Este pacote é para mim. | Ce colis est pour moi.
ti | toi (après une préposition) | Pronoms compléments | Não faço isto por ti. | Je ne fais pas ça pour toi.
comigo | avec moi | Pronoms compléments | Vens comigo? | Tu viens avec moi ?
contigo | avec toi | Pronoms compléments | Quero falar contigo um momento. | Je veux te parler un instant.
o que | que, quoi | Mots interrogatifs | O que queres? | Qu'est-ce que tu veux ?
quem | qui | Mots interrogatifs | Quem é aquele senhor? | Qui est ce monsieur ?
como | comment | Mots interrogatifs | Como estás? | Comment vas-tu ?
quando | quand | Mots interrogatifs | Quando chega o comboio? | Quand arrive le train ?
onde | où | Mots interrogatifs | Onde fica a casa de banho? | Où sont les toilettes ?
quanto | combien | Mots interrogatifs | Quanto custa? | Combien ça coûte ?
porquê | pourquoi (en fin de phrase) | Mots interrogatifs | Não vens? Porquê? | Tu ne viens pas ? Pourquoi ?
porque | pourquoi | Mots interrogatifs | Porque não vens? | Pourquoi tu ne viens pas ?
qual | lequel, quel | Mots interrogatifs | Qual preferes? | Lequel préfères-tu ?
""",
"praepositionen": """
de | de | Prépositions | Sou do Canadá. | Je suis du Canada.
em | dans, en, à | Prépositions | Moro em Lisboa. | J'habite à Lisbonne.
a | à | Prépositions | Vou a Sintra amanhã. | Je vais à Sintra demain.
para | pour, vers | Prépositions | Este presente é para ti. | Ce cadeau est pour toi.
com | avec | Prépositions | Vou com o meu irmão. | J'y vais avec mon frère.
sem | sans | Prépositions | Um café sem açúcar. | Un café sans sucre.
por | par, pour | Prépositions | Obrigado por tudo. | Merci pour tout.
até | jusqu'à | Prépositions | Trabalho até às seis. | Je travaille jusqu'à six heures.
desde | depuis | Prépositions | Moro aqui desde janeiro. | J'habite ici depuis janvier.
entre | entre | Prépositions | O banco fica entre duas lojas. | La banque est entre deux magasins.
sobre | sur, à propos de | Prépositions | É um livro sobre Lisboa. | C'est un livre sur Lisbonne.
no / na | dans le, dans la (em + o, em + a) | Contractions | O gato está na cadeira. | Le chat est sur la chaise.
do / da | du, de la (de + o, de + a) | Contractions | A porta da garagem está aberta. | La porte du garage est ouverte.
ao / à | au, à la (a + o, a + a) | Contractions | Vamos ao mercado e à praia. | Nous allons au marché et à la plage.
pelo / pela | par le, par la (por + o, por + a) | Contractions | Passamos pela Baixa. | Nous passons par la Baixa.
num / numa | dans un, dans une (em + um) | Contractions | Trabalho numa loja. | Je travaille dans un magasin.
em cima de | sur, au-dessus de | Prépositions de lieu | As chaves estão em cima da mesa. | Les clés sont sur la table.
debaixo de | sous | Prépositions de lieu | O gato dorme debaixo da cama. | Le chat dort sous le lit.
em frente de | devant, en face de | Prépositions de lieu | Espero-te em frente do cinema. | Je t'attends devant le cinéma.
atrás de | derrière | Prépositions de lieu | O jardim fica atrás da casa. | Le jardin est derrière la maison.
ao lado de | à côté de | Prépositions de lieu | A farmácia fica ao lado do banco. | La pharmacie est à côté de la banque.
perto de | près de | Prépositions de lieu | Moro perto da praia. | J'habite près de la plage.
longe de | loin de | Prépositions de lieu | O aeroporto não fica longe do centro. | L'aéroport n'est pas loin du centre.
antes de | avant (de) | Prépositions de temps | Lava as mãos antes de comer. | Lave-toi les mains avant de manger.
depois de | après | Prépositions de temps | Depois da aula vamos ao parque. | Après le cours, nous allons au parc.
""",
"konjunktionen": """
e | et | Conjonctions | Pão e queijo. | Du pain et du fromage.
ou | ou | Conjonctions | Chá ou café? | Thé ou café ?
mas | mais | Conjonctions | Quero ir, mas não posso. | Je veux y aller, mais je ne peux pas.
porque | parce que | Conjonctions | Não saio porque está a chover. | Je ne sors pas parce qu'il pleut.
quando | quand | Conjonctions | Telefono-te quando chegar. | Je t'appelle quand j'arrive.
se | si | Conjonctions | Se tiveres tempo, liga-me. | Si tu as le temps, appelle-moi.
que | que | Conjonctions | Acho que vai chover. | Je crois qu'il va pleuvoir.
então | alors, donc | Conjonctions | Está a chover, então fico em casa. | Il pleut, alors je reste à la maison.
""",
}
