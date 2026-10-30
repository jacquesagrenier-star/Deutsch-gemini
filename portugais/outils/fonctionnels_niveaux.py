# -*- coding: utf-8 -*-
"""Les mots-outils A2-C1 du portugais (du Portugal), avec leurs phrases, ecrites ici.

Meme format que phrases_a1.FONCTIONNELS (session socle) : « mot | traduction |
categorie | phrase | sa traduction », sous les cles du fichier allemand
(funktionswort.json), chacune nourrissant un theme du moteur. niveaux.py les
ajoute a fonctionnels.json avec leur niveau. Un mot n'apparait qu'a UN niveau
dans une categorie (A1 compris) ; un autre sens prend un autre libelle.
BROUILLON : a faire relire par un lusophone du Portugal.
"""

FONCTIONNELS = {
"A2": {
"konjunktionen": """
enquanto | pendant que, tandis que | Temps | Ela lia enquanto eu cozinhava. | Elle lisait pendant que je cuisinais.
assim que | dès que | Temps | Telefono-te assim que chegar. | Je te téléphone dès que j'arrive.
logo que | dès que | Temps | Logo que acabes, podes sair. | Dès que tu auras fini, tu pourras sortir.
antes que | avant que | Temps | Vamos embora antes que chova. | Partons avant qu'il pleuve.
até que | jusqu'à ce que | Temps | Espera aqui até que eu volte. | Attends ici jusqu'à ce que je revienne.
embora | bien que | Opposition | Embora esteja frio, vou nadar. | Bien qu'il fasse froid, je vais nager.
como | comme (cause) | Cause | Como estava a chover, ficámos em casa. | Comme il pleuvait, nous sommes restés à la maison.
por isso | c'est pourquoi | Conséquence | Estava cansado, por isso deitei-me cedo. | J'étais fatigué, c'est pourquoi je me suis couché tôt.
portanto | donc | Conséquence | Não tenho carro, portanto vou de comboio. | Je n'ai pas de voiture, donc je prends le train.
nem… nem | ni… ni | Choix | Não bebo nem café nem chá. | Je ne bois ni café ni thé.
ou… ou | soit… soit | Choix | Ou vens agora, ou vou sozinho. | Soit tu viens maintenant, soit j'y vais seul.
tanto… como | aussi bien… que | Addition | Fala tanto inglês como francês. | Il parle aussi bien anglais que français.
para que | pour que | But | Fala devagar para que eu perceba. | Parle lentement pour que je comprenne.
""",
"praepositionen": """
durante | pendant | Temps | Choveu durante a noite toda. | Il a plu pendant toute la nuit.
há (+ durée) | il y a | Temps | Cheguei há duas semanas. | Je suis arrivé il y a deux semaines.
daqui a | dans (+ durée) | Temps | O comboio parte daqui a dez minutos. | Le train part dans dix minutes.
a partir de | à partir de | Temps | A loja está fechada a partir de amanhã. | Le magasin est fermé à partir de demain.
por volta de | vers, aux alentours de | Temps | Chego por volta das oito. | J'arrive vers huit heures.
através de | à travers, par | Lieu | Passámos através do parque. | Nous sommes passés à travers le parc.
dentro de | dans, à l'intérieur de | Lieu | As chaves estão dentro da mala. | Les clés sont dans le sac.
fora de | hors de | Lieu | Moro fora da cidade. | J'habite en dehors de la ville.
junto a | près de, au bord de | Lieu | Jantámos junto ao rio. | Nous avons dîné au bord du fleuve.
à volta de | autour de | Lieu | Demos uma volta à volta do lago. | Nous avons fait un tour autour du lac.
contra | contre | Opposition | Votei contra a proposta. | J'ai voté contre la proposition.
segundo | selon | Point de vue | Segundo o médico, não é grave. | Selon le médecin, ce n'est pas grave.
""",
"pronomen": """
alguém | quelqu'un | Indéfinis | Está alguém em casa? | Il y a quelqu'un à la maison ?
ninguém | personne | Indéfinis | Não vi ninguém na rua. | Je n'ai vu personne dans la rue.
algo | quelque chose | Indéfinis | Queres algo para beber? | Tu veux quelque chose à boire ?
nada | rien | Indéfinis | Não comprei nada. | Je n'ai rien acheté.
tudo | tout | Indéfinis | Correu tudo bem. | Tout s'est bien passé.
cada | chaque | Indéfinis | Cada aluno tem o seu livro. | Chaque élève a son livre.
cada um | chacun | Indéfinis | Cada um paga a sua parte. | Chacun paie sa part.
qualquer | n'importe quel | Indéfinis | Podes vir a qualquer hora. | Tu peux venir à n'importe quelle heure.
o próprio | lui-même | Insistance | O próprio diretor veio falar connosco. | Le directeur lui-même est venu nous parler.
um ao outro | l'un l'autre | Réciproque | Ajudam-se um ao outro. | Ils s'aident l'un l'autre.
connosco | avec nous | Pronoms compléments | Vens jantar connosco? | Tu viens dîner avec nous ?
consigo | avec lui, avec vous (soi) | Pronoms compléments | O senhor traz o documento consigo? | Vous avez le document sur vous ?
""",
"artikelwoerter": """
o vosso | votre (à vous tous) | Possessifs | A vossa casa é linda. | Votre maison est magnifique.
deles | leur (à eux) | Possessifs | O carro deles é novo. | Leur voiture est neuve.
delas | leur (à elles) | Possessifs | A casa delas fica no centro. | Leur maison est dans le centre.
todo o | tout le | Quantité | Trabalhei todo o dia. | J'ai travaillé toute la journée.
todos os | tous les | Quantité | Vou ao ginásio todos os dias. | Je vais à la salle de sport tous les jours.
outro | un autre | Quantité | Queres outro café? | Tu veux un autre café ?
vários | plusieurs | Quantité | Tenho vários amigos em Faro. | J'ai plusieurs amis à Faro.
alguns | quelques | Quantité | Faltam alguns minutos. | Il reste quelques minutes.
nenhum | aucun | Quantité | Não tenho nenhum problema. | Je n'ai aucun problème.
bastante | assez, pas mal de | Quantité | Há bastante gente na praia. | Il y a pas mal de monde à la plage.
demasiado | trop (de) | Quantité | Comi demasiado bolo. | J'ai mangé trop de gâteau.
""",
"zahlen": """
primeiro | premier | Ordinaux | Moro no primeiro andar. | J'habite au premier étage.
segundo | deuxième | Ordinaux | É a segunda vez que venho cá. | C'est la deuxième fois que je viens ici.
terceiro | troisième | Ordinaux | Vire na terceira rua à direita. | Tournez dans la troisième rue à droite.
último | dernier | Ordinaux | É o último comboio da noite. | C'est le dernier train de la nuit.
cem | cent | Centaines | O bilhete custa cem euros. | Le billet coûte cent euros.
cento e vinte | cent vingt | Centaines | Pesa cento e vinte quilos. | Il pèse cent vingt kilos.
duzentos | deux cents | Centaines | A sala tem duzentos lugares. | La salle a deux cents places.
mil | mille | Centaines | Mais de mil pessoas vieram ao concerto. | Plus de mille personnes sont venues au concert.
metade | la moitié | Fractions | Comi metade da pizza. | J'ai mangé la moitié de la pizza.
um quarto | un quart | Fractions | Falta um quarto para as nove. | Il est neuf heures moins le quart.
o dobro | le double | Fractions | Paguei o dobro do preço. | J'ai payé le double du prix.
""",
},
"B1": {
"konjunktionen": """
caso | au cas où | Condition | Caso precises de ajuda, liga-me. | Au cas où tu aurais besoin d'aide, appelle-moi.
desde que | à condition que | Condition | Podes ir, desde que voltes cedo. | Tu peux y aller, à condition de rentrer tôt.
a não ser que | à moins que | Condition | Vou a pé, a não ser que chova. | J'y vais à pied, à moins qu'il pleuve.
mesmo que | même si | Opposition | Mesmo que me peças, não vou. | Même si tu me le demandes, je n'irai pas.
ainda que | même si, bien que | Opposition | Ainda que seja caro, compro-o. | Même s'il est cher, je l'achète.
apesar de | malgré, bien que | Opposition | Apesar do frio, saímos. | Malgré le froid, nous sommes sortis.
no entanto | cependant | Opposition | É caro; no entanto, vale a pena. | C'est cher ; cependant, ça vaut la peine.
pelo contrário | au contraire | Opposition | Não estou cansado; pelo contrário! | Je ne suis pas fatigué ; au contraire !
além disso | en plus, de plus | Addition | O hotel é barato e, além disso, fica no centro. | L'hôtel est bon marché et, en plus, il est dans le centre.
ou seja | c'est-à-dire | Explication | Chego dia 5, ou seja, sexta-feira. | J'arrive le 5, c'est-à-dire vendredi.
visto que | étant donné que | Cause | Visto que não vens, vou sozinho. | Étant donné que tu ne viens pas, j'y vais seul.
já que | puisque | Cause | Já que estás aqui, ajuda-me. | Puisque tu es là, aide-moi.
de modo que | de sorte que | Conséquence | Perdi o comboio, de modo que cheguei tarde. | J'ai raté le train, de sorte que je suis arrivé tard.
sempre que | chaque fois que | Temps | Sempre que vou a Lisboa, como pastéis de Belém. | Chaque fois que je vais à Lisbonne, je mange des pastéis de Belém.
""",
"partikeln": """
pois | eh oui, bien sûr | Mots de l'oral | — Está calor! — Pois está! | — Il fait chaud ! — Eh oui !
pois é | c'est vrai, eh oui | Mots de l'oral | — O comboio atrasou outra vez. — Pois é. | — Le train a encore eu du retard. — Eh oui.
então | alors, bon | Mots de l'oral | Então, como correu a viagem? | Alors, comment s'est passé le voyage ?
afinal | finalement, en fait | Mots de l'oral | Afinal não vens? | Finalement, tu ne viens pas ?
olha | écoute, tiens | Mots de l'oral | Olha, amanhã não posso. | Écoute, demain je ne peux pas.
pronto | bon, voilà, c'est tout | Mots de l'oral | Pronto, está decidido. | Bon, c'est décidé.
lá | donc, voyons (insistance) | Mots de l'oral | Diz lá o que se passa. | Dis-moi donc ce qui se passe.
se calhar | peut-être | Mots de l'oral | Se calhar chove amanhã. | Peut-être qu'il pleuvra demain.
""",
"praepositionen": """
apesar de | malgré | Opposition | Apesar da chuva, o jogo continuou. | Malgré la pluie, le match a continué.
em vez de | au lieu de | Opposition | Em vez de ires de carro, vai de comboio. | Au lieu d'y aller en voiture, prends le train.
graças a | grâce à | Cause | Graças a ti, consegui o emprego. | Grâce à toi, j'ai obtenu le travail.
por causa de | à cause de | Cause | Fiquei em casa por causa da greve. | Je suis resté à la maison à cause de la grève.
quanto a | quant à | Point de vue | Quanto ao preço, falamos depois. | Quant au prix, nous en parlerons après.
sem ser | à part, sauf | Exception | Vêm todos, sem ser o Rui. | Tout le monde vient, sauf Rui.
exceto | sauf, excepté | Exception | Abre todos os dias exceto segunda. | C'est ouvert tous les jours sauf le lundi.
ao longo de | tout au long de | Temps | Ao longo do ano, fizemos três viagens. | Tout au long de l'année, nous avons fait trois voyages.
""",
"pronomen": """
cujo | dont le | Relatifs | O vizinho cujo cão ladra muito mudou-se. | Le voisin dont le chien aboie beaucoup a déménagé.
o qual | lequel | Relatifs | É a empresa para a qual trabalho. | C'est l'entreprise pour laquelle je travaille.
o que (relatif) | ce que, ce qui | Relatifs | Faz o que quiseres. | Fais ce que tu veux.
onde (relatif) | où | Relatifs | A casa onde nasci já não existe. | La maison où je suis né n'existe plus.
quem (relatif) | qui (après une préposition) | Relatifs | A pessoa com quem falei foi simpática. | La personne avec qui j'ai parlé a été sympathique.
""",
},
"B2": {
"konjunktionen": """
por mais que | avoir beau | Opposition | Por mais que tente, não consigo. | J'ai beau essayer, je n'y arrive pas.
se bem que | bien que | Opposition | Se bem que seja tarde, ainda há tempo. | Bien qu'il soit tard, il reste du temps.
contudo | pourtant, toutefois | Opposition | Estudou muito; contudo, chumbou. | Il a beaucoup étudié ; pourtant, il a échoué.
todavia | toutefois | Opposition | A ideia é boa; todavia, é cara. | L'idée est bonne ; toutefois, elle est chère.
aliás | d'ailleurs | Addition | Não gosto do filme; aliás, nem o vi até ao fim. | Je n'aime pas ce film ; d'ailleurs, je ne l'ai même pas vu jusqu'au bout.
isto é | c'est-à-dire | Explication | O curso dura um semestre, isto é, seis meses. | Le cours dure un semestre, c'est-à-dire six mois.
dado que | étant donné que | Cause | Dado que ninguém respondeu, adiámos. | Étant donné que personne n'a répondu, nous avons reporté.
uma vez que | puisque | Cause | Uma vez que estás cá, ficas para jantar. | Puisque tu es là, reste dîner.
à medida que | à mesure que | Temps | À medida que o tempo passa, esqueço-me. | À mesure que le temps passe, j'oublie.
a fim de que | afin que | But | Repito, a fim de que todos percebam. | Je répète, afin que tous comprennent.
""",
"praepositionen": """
perante | face à, devant | Point de vue | Perante o problema, decidimos agir. | Face au problème, nous avons décidé d'agir.
mediante | moyennant | Moyen | A entrada é feita mediante reserva. | L'entrée se fait sur réservation.
consoante | selon, suivant | Point de vue | O preço varia consoante a época. | Le prix varie selon la saison.
a respeito de | au sujet de | Point de vue | Falámos a respeito do novo projeto. | Nous avons parlé du nouveau projet.
em relação a | par rapport à | Comparaison | Em relação ao ano passado, vendemos mais. | Par rapport à l'an dernier, nous avons vendu davantage.
a fim de | afin de | But | Saímos cedo a fim de evitar o trânsito. | Nous sommes partis tôt afin d'éviter la circulation.
""",
"artikelwoerter": """
ambos | les deux | Quantité | Ambos os irmãos vivem no Porto. | Les deux frères vivent à Porto.
tal | tel | Comparaison | Nunca vi tal coisa. | Je n'ai jamais vu une telle chose.
certo | un certain | Quantité | Há certas coisas que não se dizem. | Il y a certaines choses qu'on ne dit pas.
imenso | énormément de | Quantité | Havia imensa gente na festa. | Il y avait énormément de monde à la fête.
""",
},
"C1": {
"konjunktionen": """
conquanto | bien que (soutenu) | Opposition | Conquanto seja difícil, é possível. | Bien que ce soit difficile, c'est possible.
contanto que | pourvu que | Condition | Aceito, contanto que me paguem a horas. | J'accepte, pourvu qu'on me paie à temps.
porquanto | puisque (soutenu) | Cause | Não veio, porquanto estava doente. | Il n'est pas venu, puisqu'il était malade.
na medida em que | dans la mesure où | Condition | Ajudamos na medida em que for possível. | Nous aiderons dans la mesure du possible.
de modo a | de façon à | But | Organizámo-nos de modo a poupar tempo. | Nous nous sommes organisés de façon à gagner du temps.
não obstante | néanmoins, nonobstant | Opposition | O projeto avançou, não obstante as críticas. | Le projet a avancé, malgré les critiques.
""",
"praepositionen": """
aquando de | lors de | Temps | Aquando da visita, o museu estava fechado. | Lors de la visite, le musée était fermé.
em prol de | en faveur de | But | Lutam em prol dos direitos humanos. | Ils luttent en faveur des droits humains.
à luz de | à la lumière de | Point de vue | À luz dos novos dados, mudámos de ideias. | À la lumière des nouvelles données, nous avons changé d'avis.
mercê de | grâce à (soutenu) | Cause | Mercê do seu esforço, foi promovido. | Grâce à ses efforts, il a été promu.
no âmbito de | dans le cadre de | Point de vue | No âmbito do projeto, visitámos três escolas. | Dans le cadre du projet, nous avons visité trois écoles.
""",
"pronomen": """
outrem | autrui | Indéfinis | Não se deve desejar o mal de outrem. | Il ne faut pas souhaiter le mal d'autrui.
o mesmo | celui-ci, ce dernier (administratif) | Reprise | O requerente deve indicar a morada do mesmo. | Le demandeur doit indiquer son adresse.
""",
},
}
