# -*- coding: utf-8 -*-
"""Les verbes, adjectifs et adverbes A1 du portugais (du Portugal). SOURCE :
on corrige ici, puis python portugais/outils/construire.py. Les formes des
verbes sont calculees par conjugaison.py (tables des irreguliers comprises).

Verbe : « infinitif | traduction | phrase au present | sa traduction | drapeaux »
  pron     verbe pronominal (chamar-se) : le pronom suit le verbe, a la
           portugaise (chamo-me), sauf apres une negation (nao me chamo)
  br=...   le verbe du Bresil quand il differe (variante a venir)

Adjectif : « masculin | feminin | traduction | phrase | sa traduction | drapeaux »
  pl=...   pluriel masculin que la regle ne trouve pas
Adverbe : « adverbe | traduction | categorie | phrase | sa traduction »

Brouillon tire du corpus espagnol A1 (ses champs en portugais du Bresil),
recrit en portugais d'Europe.
"""

VERBES = """
viver | vivre | Vivo em Lisboa há dois anos. | Je vis à Lisbonne depuis deux ans.
morar | habiter | Moro aqui há dois anos. | J'habite ici depuis deux ans.
abrir | ouvrir | Podes abrir a janela? | Peux-tu ouvrir la fenêtre ?
fechar | fermer | Fecho a porta à chave. | Je ferme la porte à clé.
limpar | nettoyer | Limpo a cozinha ao sábado. | Je nettoie la cuisine le samedi.
arrumar | ranger | Tenho de arrumar o meu quarto. | Je dois ranger ma chambre.
chamar-se | s'appeler | Chamo-me Ana, e tu? | Je m'appelle Ana, et toi ? | pron
ter | avoir | Tenho duas irmãs. | J'ai deux sœurs.
conhecer | connaître | Conheces o meu primo? | Tu connais mon cousin ?
gostar | aimer (gostar de) | Gosto muito da minha avó. | J'aime beaucoup ma grand-mère.
querer | vouloir | Quero um café, por favor. | Je veux un café, s'il vous plaît.
visitar | rendre visite à | Visitamos os avós ao domingo. | Nous rendons visite aux grands-parents le dimanche.
comer | manger | Comemos às duas. | Nous mangeons à quatorze heures.
almoçar | déjeuner | Almoço no escritório. | Je déjeune au bureau.
beber | boire | Bebo muita água por dia. | Je bois beaucoup d'eau par jour.
cozinhar | cuisiner | O meu pai cozinha ao domingo. | Mon père cuisine le dimanche.
provar | goûter, essayer | Queres provar o queijo? | Tu veux goûter le fromage ?
pedir | commander, demander | Peço sempre a mesma coisa. | Je commande toujours la même chose.
doer | faire mal | Doem-me os pés. | J'ai mal aux pieds.
sentir-se | se sentir | Hoje sinto-me muito melhor. | Aujourd'hui, je me sens beaucoup mieux. | pron
descansar | se reposer | Precisas de descansar uns dias. | Tu as besoin de te reposer quelques jours.
dormir | dormir | Durmo oito horas por noite. | Je dors huit heures par nuit.
respirar | respirer | Respire fundo, por favor. | Respirez profondément, s'il vous plaît.
vestir | porter (un vêtement), mettre | Hoje ela veste um vestido vermelho. | Aujourd'hui, elle porte une robe rouge.
pôr | mettre, poser | Ponho o prato na mesa. | Je mets l'assiette sur la table.
tirar | enlever, prendre | Tira os sapatos, por favor. | Enlève tes chaussures, s'il te plaît.
comprar | acheter | Compro pouca roupa. | J'achète peu de vêtements.
custar | coûter | Quanto custa esta camisa? | Combien coûte cette chemise ?
ir | aller | Vou ao centro de metro. | Je vais au centre en métro.
vir | venir | Vens comigo ao mercado? | Tu viens avec moi au marché ?
andar | marcher | Andamos meia hora por dia. | Nous marchons une demi-heure par jour.
atravessar | traverser | Atravessa na passadeira. | Traverse sur le passage piéton.
virar | tourner | Vire à direita na esquina. | Tournez à droite au coin de la rue.
começar | commencer | O filme começa às oito. | Le film commence à huit heures.
acabar | finir | Acabo de trabalhar às seis. | Je finis de travailler à six heures.
esperar | attendre, espérer | Espero por ti à porta. | Je t'attends à la porte.
durar | durer | A aula dura uma hora. | Le cours dure une heure.
ser | être (permanent) | Sou professor de português. | Je suis professeur de portugais.
estar | être (état, lieu) | Estou em casa. | Je suis à la maison.
fazer | faire | Ao domingo faço o almoço. | Le dimanche, je fais le déjeuner.
poder | pouvoir | Hoje à noite não posso sair. | Ce soir, je ne peux pas sortir.
dizer | dire | Ele diz sempre a verdade. | Il dit toujours la vérité.
ver | voir, regarder | À noite vejo televisão. | Le soir, je regarde la télévision.
dar | donner | Dou-te o meu número. | Je te donne mon numéro.
saber | savoir | Não sei onde está a chave. | Je ne sais pas où est la clé.
sair | sortir, partir | Saio de casa às oito. | Je sors de chez moi à huit heures.
voltar | revenir, retourner | Volto às seis. | Je reviens à six heures.
perceber | comprendre | Não percebo a pergunta. | Je ne comprends pas la question. | br=entender
jogar | jouer (à un jeu, un sport) | Ao sábado jogo futebol. | Le samedi, je joue au foot.
brincar | jouer (enfants) | As crianças brincam no parque. | Les enfants jouent dans le parc.
chegar | arriver | O comboio chega às nove. | Le train arrive à neuf heures.
passar | passer | O autocarro passa de dez em dez minutos. | Le bus passe toutes les dix minutes.
dever | devoir | Deves descansar mais. | Tu dois te reposer davantage.
achar | trouver, penser | Acho que tens razão. | Je crois que tu as raison.
falar | parler | Falo um pouco de português. | Je parle un peu portugais.
trabalhar | travailler | Trabalho num escritório. | Je travaille dans un bureau.
estudar | étudier | Estudo português à terça-feira. | J'étudie le portugais le mardi.
escrever | écrire | Escrevo uma carta à minha avó. | J'écris une lettre à ma grand-mère.
ler | lire | Leio o jornal de manhã. | Je lis le journal le matin.
ouvir | écouter, entendre | Ouço música no comboio. | J'écoute de la musique dans le train.
aprender | apprendre | Aprendo palavras novas todos os dias. | J'apprends de nouveaux mots tous les jours.
ajudar | aider | Podes ajudar-me? | Peux-tu m'aider ?
procurar | chercher | Procuro os meus óculos. | Je cherche mes lunettes.
encontrar | trouver, rencontrer | Não encontro as chaves. | Je ne trouve pas les clés.
precisar | avoir besoin (de) | Preciso de um bocado de tempo. | J'ai besoin d'un peu de temps.
usar | utiliser | Uso o telemóvel para tudo. | J'utilise mon portable pour tout.
correr | courir | Ao sábado corro no parque. | Le samedi, je cours dans le parc.
esquecer | oublier | Esqueço sempre o nome dele. | J'oublie toujours son nom.
lembrar-se | se souvenir | Não me lembro da morada. | Je ne me souviens pas de l'adresse. | pron
viajar | voyager | No verão viajo para os Açores. | L'été, je voyage aux Açores.
pagar | payer | Pago com cartão. | Je paie par carte.
perguntar | demander, poser une question | Vou perguntar na loja. | Je vais demander au magasin.
responder | répondre | Respondo aos e-mails à tarde. | Je réponds aux courriels l'après-midi.
pintar | peindre | Vamos pintar a parede de branco. | Nous allons peindre le mur en blanc.
desenhar | dessiner | A minha filha desenha muito bem. | Ma fille dessine très bien.
voar | voler (dans les airs) | Os pássaros voam alto. | Les oiseaux volent haut.
nadar | nager | Os peixes nadam muito depressa. | Les poissons nagent très vite.
tratar | s'occuper (de) | Trato do cão da minha vizinha. | Je m'occupe du chien de ma voisine.
chover | pleuvoir | Chove desde ontem. | Il pleut depuis hier.
nevar | neiger | Na Serra da Estrela neva em dezembro. | Dans la Serra da Estrela, il neige en décembre.
apresentar | présenter | Apresento-te a minha irmã. | Je te présente ma sœur.
cumprimentar | saluer | Cumprimento os vizinhos todas as manhãs. | Je salue les voisins tous les matins.
soletrar | épeler | Pode soletrar o seu apelido? | Pouvez-vous épeler votre nom de famille ?
repetir | répéter | Pode repetir, por favor? | Pouvez-vous répéter, s'il vous plaît ?
reservar | réserver | Queria reservar uma mesa para dois. | Je voudrais réserver une table pour deux.
servir | servir | Servem o pequeno-almoço até às onze. | Ils servent le petit-déjeuner jusqu'à onze heures.
recomendar | recommander | O que me recomenda? | Que me recommandez-vous ?
jantar | dîner | Jantamos às oito e meia. | Nous dînons à huit heures et demie.
vender | vendre | Aqui vendem fruta fresca. | Ici, on vend des fruits frais.
gastar | dépenser | Gasto pouco em roupa. | Je dépense peu en vêtements.
trocar | changer, échanger | Queria trocar esta camisa. | Je voudrais échanger cette chemise.
mudar | changer | O tempo muda depressa. | Le temps change vite.
devolver | rendre, rapporter | Posso devolver o vestido amanhã? | Je peux rapporter la robe demain ?
escolher | choisir | É difícil escolher uma cor. | C'est difficile de choisir une couleur.
conduzir | conduire | Não sei conduzir. | Je ne sais pas conduire. | br=dirigir
apanhar | prendre (un transport), attraper | Apanho o autocarro na praça. | Je prends le bus sur la place. | br=pegar
subir | monter | Subimos a pé até ao castelo. | Nous montons à pied jusqu'au château.
descer | descendre | Desço na próxima paragem. | Je descends au prochain arrêt.
estacionar | se garer | É difícil estacionar aqui. | C'est difficile de se garer ici.
perder | perdre, rater | Se correres, não perdes o comboio. | Si tu cours, tu ne rates pas le train.
ensinar | enseigner | Ela ensina português às crianças. | Elle enseigne le portugais aux enfants.
mostrar | montrer | Mostras-me o caminho? | Tu me montres le chemin ?
ganhar | gagner | Ele ganha bem nesse emprego. | Il gagne bien dans cet emploi.
assinar | signer | Assine aqui, por favor. | Signez ici, s'il vous plaît.
organizar | organiser | Organizo a reunião de terça-feira. | J'organise la réunion de mardi.
enviar | envoyer | Envio o e-mail hoje à tarde. | J'envoie le courriel cet après-midi.
dançar | danser | Dançamos até às duas. | Nous dansons jusqu'à deux heures.
cantar | chanter | Ela canta muito bem. | Elle chante très bien.
praticar | pratiquer | Pratico português todos os dias. | Je pratique le portugais tous les jours.
aproveitar | profiter (de) | Aproveito muito os domingos. | Je profite beaucoup des dimanches.
acordar | se réveiller | Acordo antes do despertador. | Je me réveille avant le réveil.
levantar-se | se lever | Levanto-me às sete. | Je me lève à sept heures. | pron
tomar | prendre | Tomo duche de manhã. | Je prends une douche le matin.
vestir-se | s'habiller | Visto-me antes do pequeno-almoço. | Je m'habille avant le petit-déjeuner. | pron
pentear-se | se coiffer | Ela penteia-se em frente ao espelho. | Elle se coiffe devant le miroir. | pron
lavar | laver | Lavo as mãos antes de comer. | Je me lave les mains avant de manger.
deitar-se | se coucher | Deitamo-nos às onze. | Nous nous couchons à onze heures. | pron
sentar-se | s'asseoir | Senta-te aqui, por favor. | Assieds-toi ici, s'il te plaît. | pron
ficar | rester, se trouver | Hoje à noite fico em casa. | Ce soir, je reste à la maison.
trazer | apporter | Traz uma cadeira da cozinha. | Apporte une chaise de la cuisine.
"""

ADJECTIFS = """
grande | grande | grand | A cozinha é muito grande. | La cuisine est très grande.
pequeno | pequena | petit | Temos um jardim pequeno. | Nous avons un petit jardin.
novo | nova | neuf, nouveau, jeune | É um apartamento novo. | C'est un appartement neuf.
velho | velha | vieux | O prédio é muito velho. | L'immeuble est très vieux.
limpo | limpa | propre | A casa está limpa. | La maison est propre.
sujo | suja | sale | O chão da cozinha está sujo. | Le sol de la cuisine est sale.
mais velho | mais velha | aîné, plus âgé | O meu irmão mais velho tem trinta anos. | Mon frère aîné a trente ans. | pl=mais velhos
mais novo | mais nova | cadet, plus jeune | A minha irmã mais nova anda na escola. | Ma sœur cadette va à l'école. | pl=mais novos
casado | casada | marié | Ele é casado há cinco anos. | Il est marié depuis cinq ans.
solteiro | solteira | célibataire | A minha tia continua solteira. | Ma tante est toujours célibataire.
simpático | simpática | sympathique, gentil | Os teus pais são muito simpáticos. | Tes parents sont très sympathiques.
saboroso | saborosa | savoureux, bon | Esta sopa está muito saborosa. | Cette soupe est très bonne. | br=gostoso
doce | doce | sucré, doux | A sobremesa está doce demais. | Le dessert est trop sucré.
salgado | salgada | salé | A carne está um bocado salgada. | La viande est un peu salée.
quente | quente | chaud | O café está muito quente. | Le café est très chaud.
frio | fria | froid | A cerveja está bem fresca, mas a sopa está fria. | La bière est bien fraîche, mais la soupe est froide.
fresco | fresca | frais | O peixe está muito fresco. | Le poisson est très frais.
doente | doente | malade | Hoje o meu filho está doente. | Aujourd'hui, mon fils est malade.
saudável | saudável | sain, en bonne santé | Ele tem uma vida muito saudável. | Il mène une vie très saine.
cansado | cansada | fatigué | Estou cansada depois da viagem. | Je suis fatiguée après le voyage.
forte | forte | fort | Ele tem os braços muito fortes. | Il a les bras très forts.
alto | alta | grand (taille), haut | O meu irmão é mais alto do que eu. | Mon frère est plus grand que moi.
baixo | baixa | petit (taille), bas | A minha avó é baixa. | Ma grand-mère est petite.
branco | branca | blanc | Prefiro a camisa branca. | Je préfère la chemise blanche.
preto | preta | noir | Os sapatos pretos ficam bem com tudo. | Les chaussures noires vont avec tout.
vermelho | vermelha | rouge | Essa camisola vermelha fica-te bem. | Ce pull rouge te va bien.
azul | azul | bleu | Tenho umas calças azuis. | J'ai un pantalon bleu. | pl=azuis
verde | verde | vert | A saia verde é muito bonita. | La jupe verte est très jolie.
amarelo | amarela | jaune | O elétrico de Lisboa é amarelo. | Le tram de Lisbonne est jaune.
cinzento | cinzenta | gris | Hoje o céu está cinzento. | Aujourd'hui, le ciel est gris. | br=cinza
castanho | castanha | marron, brun | Ela tem olhos castanhos. | Elle a les yeux marron. | br=marrom
cor-de-rosa | cor-de-rosa | rose | Ele comprou uma camisa cor-de-rosa. | Il a acheté une chemise rose. | pl=cor-de-rosa
roxo | roxa | violet | As flores são roxas. | Les fleurs sont violettes.
claro | clara | clair | Prefiro o azul-claro. | Je préfère le bleu clair.
escuro | escura | foncé, sombre | O quarto está escuro. | La chambre est sombre.
caro | cara | cher | Este casaco é caro demais. | Cette veste est trop chère.
barato | barata | bon marché | Encontrei um casaco barato. | J'ai trouvé une veste bon marché.
curto | curta | court | Prefiro o cabelo curto. | Je préfère les cheveux courts.
comprido | comprida | long | Ela veste um casaco comprido. | Elle porte un long manteau.
tranquilo | tranquila | calme | É um bairro tranquilo. | C'est un quartier calme.
barulhento | barulhenta | bruyant | À noite a rua é muito barulhenta. | La nuit, la rue est très bruyante.
bonito | bonita | joli, beau | A praça é muito bonita. | La place est très jolie.
feio | feia | laid | O prédio é bastante feio. | L'immeuble est assez laid.
próximo | próxima | prochain | Na próxima semana vou ao Porto. | La semaine prochaine, je vais à Porto.
passado | passada | dernier, passé | No ano passado morava em Coimbra. | L'an dernier, j'habitais à Coimbra.
diário | diária | quotidien | Tenho uma rotina diária muito simples. | J'ai une routine quotidienne très simple.
solarengo | solarenga | ensoleillé | Hoje está um dia solarengo. | Aujourd'hui, c'est une journée ensoleillée. | br=ensolarado
nublado | nublada | nuageux | O céu está nublado. | Le ciel est nuageux.
húmido | húmida | humide | O ar está muito húmido. | L'air est très humide. | br=úmido
seco | seca | sec | Aqui o clima é muito seco. | Ici, le climat est très sec.
português | portuguesa | portugais | O meu vizinho é português. | Mon voisin est portugais. | pl=portugueses
francês | francesa | français | Ela é francesa. | Elle est française. | pl=franceses
inglês | inglesa | anglais | O professor é inglês. | Le professeur est anglais. | pl=ingleses
espanhol | espanhola | espagnol | A minha colega é espanhola. | Ma collègue est espagnole. | pl=espanhóis
canadiano | canadiana | canadien | Sou canadiano, de Montreal. | Je suis canadien, de Montréal. | br=canadense
brasileiro | brasileira | brésilien | Ela é brasileira, de São Paulo. | Elle est brésilienne, de São Paulo.
jovem | jovem | jeune | Ele ainda é muito jovem. | Il est encore très jeune. | pl=jovens
amável | amável | aimable | A empregada é muito amável. | La serveuse est très aimable. | pl=amáveis
delicioso | deliciosa | délicieux | A sobremesa está deliciosa. | Le dessert est délicieux.
picante | picante | épicé, piquant | Este molho é muito picante. | Cette sauce est très épicée.
frito | frita | frit | Quero peixe frito. | Je veux du poisson frit.
assado | assada | grillé, rôti | As sardinhas assadas são típicas de junho. | Les sardines grillées sont typiques de juin.
grátis | grátis | gratuit | A entrega é grátis. | La livraison est gratuite. | pl=grátis
usado | usada | d'occasion, usé | Comprei um livro usado. | J'ai acheté un livre d'occasion.
rápido | rápida | rapide | O comboio é mais rápido do que o carro. | Le train est plus rapide que la voiture.
lento | lenta | lent | Este autocarro é muito lento. | Ce bus est très lent.
fácil | fácil | facile | O exame foi fácil. | L'examen était facile. | pl=fáceis
difícil | difícil | difficile | Esta lição é difícil. | Cette leçon est difficile. | pl=difíceis
ocupado | ocupada | occupé | Esta semana estou muito ocupado. | Cette semaine, je suis très occupé.
livre | livre | libre | Na quinta-feira estou livre. | Jeudi, je suis libre.
divertido | divertida | amusant | O filme foi muito divertido. | Le film était très amusant.
aborrecido | aborrecida | ennuyeux | O jogo foi aborrecido. | Le match était ennuyeux. | br=chato
bom | boa | bon | É um bom restaurante. | C'est un bon restaurant. | pl=bons
mau | má | mauvais | Está mau tempo. | Il fait mauvais temps. | pl=maus
melhor | melhor | meilleur | Este caminho é melhor. | Ce chemin est meilleur.
pior | pior | pire | De manhã o trânsito é pior. | Le matin, la circulation est pire.
importante | importante | important | É uma reunião importante. | C'est une réunion importante.
possível | possível | possible | Não é possível chegar mais cedo. | Il n'est pas possible d'arriver plus tôt. | pl=possíveis
necessário | necessária | nécessaire | Não é necessário reservar. | Il n'est pas nécessaire de réserver.
cheio | cheia | plein | O copo está cheio. | Le verre est plein.
vazio | vazia | vide | A rua está vazia. | La rue est vide.
aberto | aberta | ouvert | A loja está aberta. | Le magasin est ouvert.
fechado | fechada | fermé | À segunda-feira o museu está fechado. | Le lundi, le musée est fermé.
pronto | pronta | prêt | Já estou pronto. | Je suis prêt.
contente | contente | content | Estou contente com o resultado. | Je suis content du résultat.
triste | triste | triste | O filme é um bocado triste. | Le film est un peu triste.
feliz | feliz | heureux | É uma família feliz. | C'est une famille heureuse. | pl=felizes
gordo | gorda | gros | O gato está um bocado gordo. | Le chat est un peu gros.
magro | magra | mince | Ele é alto e magro. | Il est grand et mince.
sério | séria | sérieux | É um problema sério. | C'est un problème sérieux.
alegre | alegre | joyeux | Ele tem um feitio alegre. | Il a un caractère joyeux.
verdadeiro | verdadeira | vrai | É uma história verdadeira. | C'est une histoire vraie.
"""

# Les comparatifs irreguliers : bom -> melhor, mau -> pior, grande -> maior.
# « Mais pequeno » est la forme du Portugal (le Bresil dit plutot « menor »).
COMPARATIFS = {"bom": "melhor", "mau": "pior", "grande": "maior"}
# Ceux qui ne se comparent pas (deja comparatifs, nationalites, etats).
SANS_COMPARATIF = {"mais velho", "mais novo", "melhor", "pior", "português", "francês", "inglês",
                   "espanhol", "canadiano", "brasileiro", "casado", "solteiro", "grátis", "aberto",
                   "fechado", "usado", "frito", "assado", "diário", "próximo", "passado", "cheio", "vazio",
                   "pronto", "branco", "preto", "vermelho", "azul", "verde", "amarelo", "cinzento",
                   "castanho", "cor-de-rosa", "roxo", "doente", "nublado", "possível", "necessário"}

ADVERBES = """
hoje | aujourd'hui | Temps | Hoje não trabalho. | Aujourd'hui, je ne travaille pas.
ontem | hier | Temps | Ontem choveu o dia todo. | Hier, il a plu toute la journée.
amanhã | demain | Temps | Amanhã vamos ao médico. | Demain, nous allons chez le médecin.
agora | maintenant | Temps | Agora não posso falar. | Maintenant, je ne peux pas parler.
já | déjà | Temps | A comida já está pronta. | Le repas est déjà prêt.
ainda | encore | Temps | Ele ainda não chegou. | Il n'est pas encore arrivé.
logo | tout à l'heure, bientôt | Temps | Até logo! | À tout à l'heure !
depois | après, ensuite | Temps | Depois vamos ao cinema. | Après, nous allons au cinéma.
antes | avant | Temps | Antes morava no Porto. | Avant, j'habitais à Porto.
cedo | tôt | Temps | Levanto-me cedo. | Je me lève tôt.
tarde | tard | Temps | Ao sábado deito-me tarde. | Le samedi, je me couche tard.
sempre | toujours | Fréquence | Tomo sempre o pequeno-almoço em casa. | Je prends toujours le petit-déjeuner à la maison.
nunca | jamais | Fréquence | Nunca bebo café à noite. | Je ne bois jamais de café le soir.
muitas vezes | souvent | Fréquence | Como fora muitas vezes. | Je mange souvent dehors.
às vezes | parfois | Fréquence | Às vezes vou ao trabalho a pé. | Parfois, je vais au travail à pied.
também | aussi | Manière | Eu também quero ir. | Moi aussi, je veux y aller.
também não | non plus | Manière | Eu também não sei. | Moi non plus, je ne sais pas.
bem | bien | Manière | Falas português muito bem. | Tu parles très bien portugais.
mal | mal | Manière | Esta noite dormi mal. | Cette nuit, j'ai mal dormi.
devagar | lentement | Manière | Fale devagar, por favor. | Parlez lentement, s'il vous plaît.
depressa | vite | Manière | Ele come muito depressa. | Il mange très vite.
talvez | peut-être | Manière | Talvez chova amanhã. | Il pleuvra peut-être demain.
muito | très, beaucoup | Quantité | Este livro é muito bom. | Ce livre est très bon.
bastante | assez | Quantité | A casa é bastante grande. | La maison est assez grande.
demasiado | trop | Quantité | Está demasiado calor. | Il fait trop chaud.
pouco | peu | Quantité | Durmo pouco. | Je dors peu.
um bocado | un peu | Quantité | Estou um bocado cansado. | Je suis un peu fatigué.
aqui | ici | Lieu | Aqui não está ninguém. | Il n'y a personne ici.
aí | là (près de toi) | Lieu | O livro está aí, ao teu lado. | Le livre est là, à côté de toi.
ali | là-bas | Lieu | O museu fica ali. | Le musée est là-bas.
lá | là-bas | Lieu | Lá em cima está mais fresco. | Là-haut, il fait plus frais.
em cima | en haut, dessus | Lieu | A casa de banho fica lá em cima. | La salle de bain est en haut.
em baixo | en bas, dessous | Lieu | Espero por ti lá em baixo. | Je t'attends en bas.
dentro | dedans, à l'intérieur | Lieu | As chaves estão lá dentro. | Les clés sont à l'intérieur.
fora | dehors | Lieu | As crianças brincam lá fora. | Les enfants jouent dehors.
perto | près | Lieu | A estação fica perto. | La gare est tout près.
longe | loin | Lieu | O aeroporto não fica longe. | L'aéroport n'est pas loin.
"""
