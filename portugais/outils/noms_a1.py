# -*- coding: utf-8 -*-
"""Les noms A1 du portugais (du Portugal), par theme. SOURCE : on corrige ici,
puis python portugais/outils/construire.py.

Une ligne : « article mot | traduction francaise | phrase portugaise | sa
traduction | drapeaux ». Le brouillon vient du corpus espagnol A1 (ses champs
traduction_pt / exemple_pt, ecrits en portugais du BRESIL) : chaque mot et
chaque phrase ont ete recrits en portugais d'Europe -- casa de banho et non
banheiro, autocarro et non onibus, « a minha mae » avec l'article, « estou a
ler » et non « estou lendo », le pronom apres le verbe (« chamo-me »).
Orthographe de l'Accord de 1990, en vigueur au Portugal (atual, receção, elétrico).

Drapeaux :
  pl=...   pluriel irregulier ou que la regle ne trouve pas (construire.pluriel)
  u        pas de pluriel a montrer (indenombrable, mois, sports...)
  br=...   le mot du Bresil quand il differe -- pour la future variante
           (portugais/datos/variantes-br.json), jamais montre aujourd'hui
"""

# (id du theme, nom portugais, theme espagnol dont on reprend l'icone)
THEMES = [
    ("casa_pt", "A casa", "la_casa"),
    ("familia_pt", "A família", "la_familia"),
    ("comida_pt", "A comida", "la_comida"),
    ("corpo_pt", "O corpo e a saúde", "el_cuerpo"),
    ("roupa_pt", "A roupa", "la_ropa"),
    ("cidade_pt", "A cidade", "la_ciudad"),
    ("tempo_pt", "O tempo e as datas", "el_tiempo"),
    ("numeros_pt", "Os números", "los_numeros"),
    ("formas_pt", "As formas", "los_colores"),
    ("animais_pt", "Os animais", "los_animales"),
    ("clima_pt", "O clima", "el_clima"),
    ("apresentar_pt", "Apresentar-se", "presentarse"),
    ("cafe_pt", "O café e o restaurante", "el_restaurante"),
    ("compras_pt", "As compras", "las_compras"),
    ("transportes_pt", "Os transportes", "el_transporte"),
    ("escola_pt", "A escola", "la_escuela"),
    ("trabalho_pt", "O trabalho", "el_trabajo"),
    ("lazer_pt", "O lazer", "el_ocio"),
    ("dia_pt", "O dia a dia", "la_vida_diaria"),
]

NOMS = {}

NOMS["casa_pt"] = """
a casa | la maison | A nossa casa tem um jardim pequeno. | Notre maison a un petit jardin.
o apartamento | l'appartement | Moro num apartamento no centro. | J'habite dans un appartement du centre.
a divisão | la pièce | O apartamento tem três divisões. | L'appartement a trois pièces. | pl=divisões | br=cômodo
o quarto | la chambre | O quarto dá para o pátio. | La chambre donne sur la cour.
a cozinha | la cuisine | Tomamos sempre o pequeno-almoço na cozinha. | Nous prenons toujours le petit-déjeuner dans la cuisine.
a sala | le salon | A sala é a maior divisão da casa. | Le salon est la plus grande pièce de la maison.
a casa de banho | la salle de bain | A casa de banho fica ao fundo do corredor. | La salle de bain est au bout du couloir. | pl=casas de banho | br=banheiro
a sala de jantar | la salle à manger | Comemos na sala de jantar ao domingo. | Nous mangeons dans la salle à manger le dimanche. | pl=salas de jantar
a porta | la porte | Fecha a porta, por favor. | Ferme la porte, s'il te plaît.
a janela | la fenêtre | Abre a janela, está calor. | Ouvre la fenêtre, il fait chaud.
a parede | le mur | As paredes são brancas. | Les murs sont blancs.
o chão | le sol | O chão da cozinha é de madeira. | Le sol de la cuisine est en bois. | pl=chãos
o teto | le plafond | O teto é muito alto. | Le plafond est très haut.
a escada | l'escalier | Subimos pela escada. | Nous montons par l'escalier.
o corredor | le couloir | O corredor é estreito e escuro. | Le couloir est étroit et sombre.
a garagem | le garage | O carro está na garagem. | La voiture est dans le garage.
o jardim | le jardin | No jardim há duas árvores. | Dans le jardin, il y a deux arbres.
o terraço | la terrasse | No verão jantamos no terraço. | En été, nous dînons sur la terrasse.
a varanda | le balcon | Da varanda vê-se o rio. | Depuis le balcon, on voit le fleuve.
a chave | la clé | Perdi as chaves de casa. | J'ai perdu les clés de la maison.
a mesa | la table | A mesa está posta para quatro. | La table est mise pour quatre.
a cadeira | la chaise | Faltam duas cadeiras na sala de jantar. | Il manque deux chaises dans la salle à manger.
o sofá | le canapé | O gato dorme no sofá. | Le chat dort sur le canapé.
a cama | le lit | Faço a cama todas as manhãs. | Je fais le lit tous les matins.
o armário | l'armoire, le placard | Arruma a roupa no armário. | Range les vêtements dans l'armoire.
a estante | l'étagère | A estante está cheia de livros. | L'étagère est pleine de livres.
o candeeiro | la lampe | Acende o candeeiro, não vejo nada. | Allume la lampe, je ne vois rien. | br=abajur
o tapete | le tapis | O tapete da sala é azul. | Le tapis du salon est bleu.
o espelho | le miroir | Há um espelho atrás da porta. | Il y a un miroir derrière la porte.
a cortina | le rideau | Fecha as cortinas, por favor. | Tire les rideaux, s'il te plaît.
o quadro | le tableau | Pendurámos um quadro novo. | Nous avons accroché un nouveau tableau.
o frigorífico | le réfrigérateur | O leite está no frigorífico. | Le lait est dans le réfrigérateur. | br=geladeira
o forno | le four | O pão está no forno. | Le pain est dans le four.
o lava-loiça | l'évier | Os pratos estão no lava-loiça. | Les assiettes sont dans l'évier. | pl=lava-loiças | br=pia
a máquina de lavar | le lave-linge | A máquina de lavar não funciona bem. | Le lave-linge ne fonctionne pas bien. | pl=máquinas de lavar
a máquina da loiça | le lave-vaisselle | Põe os copos na máquina da loiça. | Mets les verres dans le lave-vaisselle. | pl=máquinas da loiça | br=lava-louças
o duche | la douche | Tomo duche antes de sair. | Je prends une douche avant de sortir. | br=chuveiro
a toalha | la serviette | Tira uma toalha lavada. | Prends une serviette propre.
o sabonete | le savon | Já não há sabonete na casa de banho. | Il n'y a plus de savon dans la salle de bain.
a torneira | le robinet | Fecha bem a torneira. | Ferme bien le robinet.
o lixo | les ordures, la poubelle | Leva o lixo lá para fora, por favor. | Sors la poubelle, s'il te plaît. | u
o móvel | le meuble | Compraram móveis novos. | Ils ont acheté de nouveaux meubles.
a gaveta | le tiroir | As colheres estão na gaveta. | Les cuillères sont dans le tiroir.
o cobertor | la couverture | Está frio, tira um cobertor. | Il fait froid, prends une couverture.
a almofada | l'oreiller | Esta almofada é muito dura. | Cet oreiller est très dur. | br=travesseiro
o lençol | le drap | Mudo os lençóis ao sábado. | Je change les draps le samedi.
o computador | l'ordinateur | Trabalho em casa com o computador. | Je travaille à la maison avec l'ordinateur.
o telemóvel | le téléphone portable | Deixei o telemóvel na cozinha. | J'ai laissé le portable dans la cuisine. | br=celular
o comando | la télécommande | Onde está o comando da televisão? | Où est la télécommande de la télé ? | br=controle remoto
o elevador | l'ascenseur | O elevador está avariado outra vez. | L'ascenseur est encore en panne.
o andar | l'étage | Moro no terceiro andar. | J'habite au troisième étage.
o rés-do-chão | le rez-de-chaussée | A padaria fica no rés-do-chão. | La boulangerie est au rez-de-chaussée. | u | br=térreo
"""

NOMS["familia_pt"] = """
a família | la famille | A minha família é bastante grande. | Ma famille est assez grande.
o pai | le père | O meu pai trabalha num banco. | Mon père travaille dans une banque.
a mãe | la mère | A minha mãe cozinha muito bem. | Ma mère cuisine très bien.
o filho | le fils | O filho deles tem oito anos. | Leur fils a huit ans.
a filha | la fille | A filha deles estuda medicina. | Leur fille étudie la médecine.
o irmão | le frère | Tenho um irmão mais velho. | J'ai un frère aîné. | pl=irmãos
a irmã | la sœur | A minha irmã mora em Lisboa. | Ma sœur habite à Lisbonne.
o avô | le grand-père | O meu avô tem noventa anos. | Mon grand-père a quatre-vingt-dix ans.
a avó | la grand-mère | A avó conta-nos histórias. | La grand-mère nous raconte des histoires.
o neto | le petit-fils | Os netos vêm cá ao domingo. | Les petits-enfants viennent le dimanche.
o tio | l'oncle | O meu tio mora no Porto. | Mon oncle habite à Porto.
a tia | la tante | A minha tia é professora. | Ma tante est professeure.
o primo | le cousin | No verão brinco com os meus primos. | En été, je joue avec mes cousins.
o sobrinho | le neveu | O meu sobrinho faz dez anos. | Mon neveu fête ses dix ans.
o marido | le mari | O marido dela é francês. | Son mari est français.
a mulher | la femme, l'épouse | A mulher dele trabalha no hospital. | Sa femme travaille à l'hôpital.
o namorado | le petit ami | Ela vai ao cinema com o namorado. | Elle va au cinéma avec son petit ami.
o casal | le couple | São um casal muito simpático. | C'est un couple très sympathique. | pl=casais
o bebé | le bébé | O bebé dorme a noite toda. | Le bébé dort toute la nuit. | br=bebê
a criança | l'enfant | As crianças brincam no parque. | Les enfants jouent au parc.
o rapaz | le garçon, le jeune homme | Aquele rapaz é o meu vizinho. | Ce garçon est mon voisin. | pl=rapazes | br=moço
a rapariga | la fille, la jeune femme | As raparigas chegam às sete. | Les filles arrivent à sept heures. | br=moça
o homem | l'homme | Está um homem a perguntar por ti. | Il y a un homme qui te demande.
o amigo | l'ami | Vou jantar com uns amigos. | Je vais dîner avec des amis.
o vizinho | le voisin | Os nossos vizinhos são muito simpáticos. | Nos voisins sont très gentils.
o sogro | le beau-père | Os meus sogros chegam amanhã. | Mes beaux-parents arrivent demain.
o cunhado | le beau-frère | O meu cunhado é muito engraçado. | Mon beau-frère est très drôle.
o nome | le prénom, le nom | Qual é o teu nome completo? | Quel est ton nom complet ?
o apelido | le nom de famille | Em Portugal, usa-se muitas vezes dois apelidos. | Au Portugal, on porte souvent deux noms de famille. | br=sobrenome
a idade | l'âge | Que idade tem a tua irmã? | Quel âge a ta sœur ?
o casamento | le mariage | O casamento é em junho. | Le mariage est en juin.
o aniversário | l'anniversaire | Amanhã é o meu aniversário. | Demain, c'est mon anniversaire.
"""

NOMS["comida_pt"] = """
a comida | la nourriture | A comida está muito boa. | La nourriture est très bonne. | u
o pequeno-almoço | le petit-déjeuner | O pequeno-almoço é às oito. | Le petit-déjeuner est à huit heures. | pl=pequenos-almoços | br=café da manhã
o almoço | le déjeuner | O almoço é à uma. | Le déjeuner est à une heure.
o jantar | le dîner | O jantar está pronto. | Le dîner est prêt.
o pão | le pain | Compro pão todas as manhãs. | J'achète du pain tous les matins. | pl=pães
a água | l'eau | Pode trazer-me um copo de água? | Pouvez-vous m'apporter un verre d'eau ? | u
o leite | le lait | Bebo café com leite. | Je prends un café au lait. | u
o café | le café | Um café, por favor. | Un café, s'il vous plaît.
o chá | le thé | À tarde prefiro chá. | L'après-midi, je préfère le thé.
o sumo | le jus | Um sumo de laranja natural. | Un jus d'orange pressé. | br=suco
o vinho | le vin | Este vinho é do Douro. | Ce vin vient du Douro.
a cerveja | la bière | Duas cervejas bem frescas. | Deux bières bien fraîches.
a carne | la viande | À sexta-feira não como carne. | Je ne mange pas de viande le vendredi.
o peixe | le poisson | O peixe está muito fresco. | Le poisson est très frais.
o frango | le poulet | Hoje há frango assado. | Aujourd'hui, il y a du poulet rôti.
o ovo | l'œuf | Quero dois ovos estrelados. | Je veux deux œufs au plat.
o queijo | le fromage | Este queijo é da Serra da Estrela. | Ce fromage vient de la Serra da Estrela.
o açúcar | le sucre | Não ponho açúcar no café. | Je ne mets pas de sucre dans le café. | u
o sal | le sel | Falta sal na sopa. | Il manque du sel dans la soupe. | u
o azeite | l'huile d'olive | Em Portugal cozinha-se com azeite. | Au Portugal, on cuisine à l'huile d'olive. | u
o arroz | le riz | O arroz de legumes está pronto. | Le riz aux légumes est prêt. | u
a batata | la pomme de terre | As batatas fritas estão salgadas. | Les frites sont salées.
o tomate | la tomate | Corta o tomate às rodelas. | Coupe la tomate en rondelles.
a cebola | l'oignon | A cebola faz-me chorar. | L'oignon me fait pleurer.
o legume | le légume | Come mais legumes, por favor. | Mange plus de légumes, s'il te plaît.
a salada | la salade | Peço uma salada mista. | Je commande une salade mixte.
a fruta | le fruit | A fruta está no frigorífico. | Les fruits sont dans le frigo.
a maçã | la pomme | Como uma maçã por dia. | Je mange une pomme par jour.
a banana | la banane | As bananas estão maduras. | Les bananes sont mûres.
a laranja | l'orange | As laranjas do Algarve são famosas. | Les oranges de l'Algarve sont célèbres.
o morango | la fraise | Em maio há morangos. | En mai, il y a des fraises.
a sobremesa | le dessert | O que há de sobremesa? | Qu'y a-t-il comme dessert ?
o bolo | le gâteau | Fiz um bolo de chocolate. | J'ai fait un gâteau au chocolat.
o gelado | la glace | Quero um gelado de chocolate. | Je veux une glace au chocolat. | br=sorvete
a sandes | le sandwich | Vou fazer uma sandes de fiambre. | Je me prépare un sandwich au jambon. | pl=sandes | br=sanduíche
a sopa | la soupe | A sopa está quente. | La soupe est chaude.
o prato | l'assiette, le plat | Põe os pratos na mesa. | Mets les assiettes sur la table.
o copo | le verre | Partiu-se um copo. | Un verre s'est cassé.
a chávena | la tasse | Uma chávena de chá, por favor. | Une tasse de thé, s'il vous plaît. | br=xícara
a colher | la cuillère | Preciso de uma colher para a sopa. | J'ai besoin d'une cuillère pour la soupe.
o garfo | la fourchette | Falta um garfo na mesa. | Il manque une fourchette sur la table.
a faca | le couteau | Esta faca não corta bem. | Ce couteau ne coupe pas bien.
a garrafa | la bouteille | Abre a garrafa de vinho. | Ouvre la bouteille de vin.
a fome | la faim | Tenho muita fome. | J'ai très faim. | u
a sede | la soif | Depois de correr, tenho sede. | Après avoir couru, j'ai soif. | u
o restaurante | le restaurant | Conheço um restaurante muito bom. | Je connais un très bon restaurant.
o empregado de mesa | le serveur | O empregado de mesa traz a ementa. | Le serveur apporte la carte. | pl=empregados de mesa | br=garçom
a empregada de mesa | la serveuse | A empregada de mesa traz-nos dois cafés. | La serveuse nous apporte deux cafés. | pl=empregadas de mesa | br=garçonete
a conta | l'addition | A conta, por favor. | L'addition, s'il vous plaît.
a pizza | la pizza | Sobrou uma fatia de pizza no prato. | Il reste une part de pizza dans l'assiette.
o fiambre | le jambon (cuit) | Uma tosta com fiambre e queijo. | Un croque au jambon et au fromage. | u | br=presunto
o presunto | le jambon cru | O presunto de Chaves é muito bom. | Le jambon cru de Chaves est très bon. | u
"""

NOMS["corpo_pt"] = """
o corpo | le corps | O corpo humano é fascinante. | Le corps humain est fascinant.
a cabeça | la tête | Dói-me a cabeça. | J'ai mal à la tête.
o cabelo | les cheveux | Ela tem o cabelo muito comprido. | Elle a les cheveux très longs.
a cara | le visage | Ele lava a cara com água fria. | Il se lave le visage à l'eau froide.
o olho | l'œil | Ela tem olhos verdes. | Elle a les yeux verts.
a orelha | l'oreille | A criança tapa as orelhas. | L'enfant se bouche les oreilles.
o nariz | le nez | Está-me a sangrar o nariz. | Je saigne du nez.
a boca | la bouche | Abra a boca, por favor. | Ouvrez la bouche, s'il vous plaît.
o dente | la dent | Lavo os dentes três vezes por dia. | Je me brosse les dents trois fois par jour.
o pescoço | le cou | Tenho o pescoço preso. | J'ai le cou raide.
o ombro | l'épaule | Dói-me o ombro direito. | J'ai mal à l'épaule droite.
o braço | le bras | Ele partiu um braço. | Il s'est cassé un bras.
a mão | la main | Lava as mãos antes de comer. | Lave-toi les mains avant de manger. | pl=mãos
o dedo | le doigt | Ela cortou-se num dedo. | Elle s'est coupé un doigt.
as costas | le dos | Ao fim do dia doem-me as costas. | En fin de journée, j'ai mal au dos. | u
a barriga | le ventre | Dói-me a barriga. | J'ai mal au ventre.
o estômago | l'estomac | Tenho o estômago às voltas. | J'ai l'estomac barbouillé.
a perna | la jambe | As minhas pernas estão a tremer. | Mes jambes tremblent.
o joelho | le genou | Magoei-me no joelho. | Je me suis fait mal au genou.
o pé | le pied | Vou para o trabalho a pé. | Je vais au travail à pied.
o coração | le cœur | O coração bate muito depressa. | Le cœur bat très vite. | pl=corações
a pele | la peau | Ela tem a pele muito sensível. | Elle a la peau très sensible.
o sangue | le sang | Não suporto ver sangue. | Je ne supporte pas de voir du sang. | u
o médico | le médecin | O médico chega às dez. | Le médecin arrive à dix heures.
a médica | la médecin | A médica examina-me a garganta. | La médecin m'examine la gorge.
o enfermeiro | l'infirmier | O enfermeiro dá-me a vacina. | L'infirmier me fait le vaccin.
o hospital | l'hôpital | Levaram-no ontem para o hospital. | On l'a emmené à l'hôpital hier.
o centro de saúde | le centre de santé | Tenho consulta no centro de saúde. | J'ai rendez-vous au centre de santé. | pl=centros de saúde | br=posto de saúde
a farmácia | la pharmacie | A farmácia fecha às nove. | La pharmacie ferme à vingt et une heures.
o medicamento | le médicament | Toma o medicamento depois de comer. | Prends le médicament après le repas.
o comprimido | le comprimé | Um comprimido de oito em oito horas. | Un comprimé toutes les huit heures.
a receita | l'ordonnance | Preciso de uma receita do médico. | J'ai besoin d'une ordonnance du médecin.
a dor | la douleur | Sinto uma dor no peito. | Je ressens une douleur dans la poitrine.
a febre | la fièvre | A criança tem febre alta. | L'enfant a beaucoup de fièvre.
a constipação | le rhume | Estou com uma constipação desde segunda-feira. | J'ai un rhume depuis lundi. | pl=constipações | br=resfriado
a gripe | la grippe | A gripe dura uma semana. | La grippe dure une semaine.
a consulta | le rendez-vous (médical) | Tenho consulta no dentista. | J'ai rendez-vous chez le dentiste.
a saúde | la santé | A saúde é o mais importante. | La santé est ce qu'il y a de plus important. | u
"""

NOMS["roupa_pt"] = """
a roupa | les vêtements | Arrumo a roupa de inverno. | Je range les vêtements d'hiver. | u
a camisa | la chemise | Ele veste uma camisa branca. | Il porte une chemise blanche.
a t-shirt | le tee-shirt | Visto uma t-shirt e pronto. | Je mets un tee-shirt et c'est tout. | pl=t-shirts | br=camiseta
as calças | le pantalon | Estas calças ficam-me grandes. | Ce pantalon est trop grand pour moi. | u | br=calça
a saia | la jupe | Ela usa uma saia comprida. | Elle porte une jupe longue.
o vestido | la robe | O vestido azul é lindo. | La robe bleue est magnifique.
o casaco | la veste, le manteau | Leva o casaco, está frio. | Prends ta veste, il fait froid.
a camisola | le pull | Esta camisola é de lã. | Ce pull est en laine. | br=suéter
o sapato | la chaussure | Os sapatos pretos são novos. | Les chaussures noires sont neuves.
os ténis | les baskets | Corro com uns ténis velhos. | Je cours avec de vieilles baskets. | u | br=tênis
a bota | la botte | Quando chove, calço as botas. | Quand il pleut, je mets mes bottes.
a meia | la chaussette | Falta uma meia. | Il manque une chaussette.
o chapéu | le chapeau | No verão ele usa chapéu. | En été, il porte un chapeau.
o boné | la casquette | O miúdo não tira o boné. | Le gamin n'enlève pas sa casquette.
o cachecol | l'écharpe | Põe o cachecol, está vento. | Mets ton écharpe, il y a du vent. | pl=cachecóis
a luva | le gant | Perdi as luvas. | J'ai perdu mes gants.
o cinto | la ceinture | Preciso de um cinto de cabedal. | J'ai besoin d'une ceinture en cuir.
a mala | le sac à main, la valise | A mala está em cima da cadeira. | Le sac est sur la chaise. | br=bolsa
a mochila | le sac à dos | A mochila pesa muito. | Le sac à dos est très lourd.
os óculos | les lunettes | Não encontro os meus óculos. | Je ne trouve pas mes lunettes. | u
o relógio | la montre, l'horloge | O meu relógio parou. | Ma montre s'est arrêtée.
o anel | la bague | Ela usa um anel de prata. | Elle porte une bague en argent. | pl=anéis
o tamanho | la taille (vêtement) | Que tamanho veste? | Quelle taille faites-vous ?
a cor | la couleur | De que cor quer? | De quelle couleur le voulez-vous ?
a loja | le magasin | A loja abre às dez. | Le magasin ouvre à dix heures.
o preço | le prix | O preço parece-me alto. | Le prix me semble élevé.
os saldos | les soldes | Os saldos começam em janeiro. | Les soldes commencent en janvier. | u | br=liquidação
as cuecas | le slip, le caleçon | Levo três cuecas na mala. | J'ai trois slips dans la valise. | u | br=cueca
o gorro | le bonnet (la tuque) | No inverno uso sempre um gorro de lã. | En hiver, je porte toujours un bonnet de laine.
a blusa | le chemisier | Esta blusa cor-de-rosa é de seda. | Ce chemisier rose est en soie.
a sandália | la sandale | No verão uso sandálias. | En été, je porte des sandales.
as calças de ganga | le jean | Visto as calças de ganga azuis. | Je mets mon jean bleu. | u | br=calça jeans
os óculos de sol | les lunettes de soleil | No verão uso sempre óculos de sol. | En été, je porte toujours des lunettes de soleil. | u
"""

NOMS["cidade_pt"] = """
a cidade | la ville | É uma cidade muito tranquila. | C'est une ville très tranquille.
a aldeia | le village | Os meus avós moram numa aldeia. | Mes grands-parents vivent dans un village.
a rua | la rue | Moro na Rua Augusta. | J'habite rue Augusta.
a praça | la place | Encontramo-nos na praça às seis. | On se retrouve sur la place à six heures.
a avenida | l'avenue | A avenida está fechada hoje. | L'avenue est fermée aujourd'hui.
o bairro | le quartier | Alfama é um bairro muito animado. | Alfama est un quartier très animé.
o centro | le centre-ville | Trabalho no centro. | Je travaille dans le centre.
o prédio | l'immeuble | O prédio tem dez andares. | L'immeuble a dix étages.
o parque | le parc | Passeio no parque todas as tardes. | Je me promène dans le parc chaque après-midi.
o mercado | le marché | O mercado abre ao sábado. | Le marché ouvre le samedi.
o supermercado | le supermarché | Vou ao supermercado à sexta-feira. | Je vais au supermarché le vendredi.
o banco | la banque, le banc | O banco fecha às três. | La banque ferme à quinze heures.
os correios | la poste | Tenho de passar pelos correios. | Je dois passer à la poste. | u
a igreja | l'église | A igreja é do século quinze. | L'église date du quinzième siècle.
o museu | le musée | O museu é gratuito ao domingo de manhã. | Le musée est gratuit le dimanche matin.
a biblioteca | la bibliothèque | Estudo na biblioteca. | J'étudie à la bibliothèque.
o cinema | le cinéma | Vamos ao cinema hoje à noite. | Nous allons au cinéma ce soir.
o teatro | le théâtre | O teatro está cheio. | Le théâtre est plein.
o hotel | l'hôtel | O hotel fica perto da estação. | L'hôtel est près de la gare. | pl=hotéis
a estação | la gare | A estação fica a dez minutos. | La gare est à dix minutes. | pl=estações
o aeroporto | l'aéroport | O aeroporto não fica longe do centro. | L'aéroport n'est pas loin du centre.
o autocarro | l'autobus | O autocarro passa de dez em dez minutos. | Le bus passe toutes les dix minutes. | br=ônibus
o metro | le métro | Vou para o trabalho de metro. | Je vais au travail en métro. | br=metrô
o comboio | le train | O comboio parte às sete. | Le train part à sept heures. | br=trem
o elétrico | le tramway | O elétrico 28 sobe até ao castelo. | Le tram 28 monte jusqu'au château. | br=bonde
o carro | la voiture | Estaciono o carro na rua. | Je gare la voiture dans la rue.
a bicicleta | le vélo | Vou ao mercado de bicicleta. | Je vais au marché à vélo.
o táxi | le taxi | Apanhamos um táxi até ao hotel. | Nous prenons un taxi jusqu'à l'hôtel.
o bilhete | le billet, le ticket | Compro o bilhete na internet. | J'achète le billet sur internet. | br=passagem
o semáforo | le feu de circulation | Para no semáforo vermelho. | Arrête-toi au feu rouge.
a passadeira | le passage piéton | Atravessa na passadeira. | Traverse sur le passage piéton. | br=faixa de pedestres
a esquina | le coin de rue | A farmácia fica na esquina. | La pharmacie est au coin de la rue.
a ponte | le pont | Atravessamos a ponte a pé. | Nous traversons le pont à pied.
o trânsito | la circulation | A esta hora há muito trânsito. | À cette heure-ci, il y a beaucoup de circulation. | u
a pessoa | la personne | Há muitas pessoas na praça. | Il y a beaucoup de monde sur la place.
a padaria | la boulangerie | Compro o pão na padaria da esquina. | J'achète le pain à la boulangerie du coin.
a pastelaria | la pâtisserie, le café | Encontramo-nos na pastelaria da praça. | On se retrouve au café-pâtisserie de la place.
o castelo | le château | Do castelo vê-se a cidade toda. | Du château, on voit toute la ville.
o rio | le fleuve, la rivière | O Tejo é um rio muito largo. | Le Tage est un fleuve très large.
o estacionamento | le parking | Não encontro estacionamento nesta rua. | Je ne trouve pas où me garer dans cette rue. | u
"""

NOMS["tempo_pt"] = """
o dia | le jour | Hoje está um dia muito bonito. | Aujourd'hui, c'est une très belle journée.
a semana | la semaine | A semana começa na segunda-feira. | La semaine commence le lundi.
o mês | le mois | Este mês tenho muito trabalho. | Ce mois-ci, j'ai beaucoup de travail. | pl=meses
o ano | l'année | O ano tem doze meses. | L'année a douze mois.
a hora | l'heure | Que horas são? | Quelle heure est-il ?
o minuto | la minute | Espera um minuto, por favor. | Attends une minute, s'il te plaît.
o segundo | la seconde | Um minuto tem sessenta segundos. | Une minute a soixante secondes.
a manhã | le matin | De manhã bebo um café. | Le matin, je bois un café.
a tarde | l'après-midi | Vemo-nos à tarde. | On se voit dans l'après-midi.
a noite | la nuit, le soir | À noite leio um bocado. | Le soir, je lis un moment.
o meio-dia | midi | Almoçamos ao meio-dia. | Nous déjeunons à midi. | u
a meia-noite | minuit | A festa acaba à meia-noite. | La fête finit à minuit. | u
o fim de semana | le week-end | No fim de semana vamos para o campo. | Le week-end, nous allons à la campagne. | pl=fins de semana
a data | la date | Qual é a data de hoje? | Quelle est la date d'aujourd'hui ?
o calendário | le calendrier | Vejo o calendário todas as segundas-feiras. | Je regarde le calendrier tous les lundis.
o momento | le moment | Neste momento não posso falar. | En ce moment, je ne peux pas parler.
o bocado | un moment, un peu | Vamos descansar um bocado. | Nous allons nous reposer un moment.
o século | le siècle | Esta igreja é do século quinze. | Cette église date du quinzième siècle.
a segunda-feira | le lundi | Na segunda-feira começo um curso. | Lundi, je commence un cours. | pl=segundas-feiras
a terça-feira | le mardi | À terça-feira vou ao mercado. | Le mardi, je vais au marché. | pl=terças-feiras
a quarta-feira | le mercredi | Na quarta-feira tenho uma consulta. | Mercredi, j'ai un rendez-vous. | pl=quartas-feiras
a quinta-feira | le jeudi | Na quinta-feira jantamos fora. | Jeudi, nous dînons dehors. | pl=quintas-feiras
a sexta-feira | le vendredi | A sexta-feira é o meu dia preferido. | Le vendredi est mon jour préféré. | pl=sextas-feiras
o sábado | le samedi | Ao sábado dormimos até tarde. | Le samedi, nous dormons tard.
o domingo | le dimanche | Ao domingo almoçamos com a família. | Le dimanche, nous déjeunons en famille.
 janeiro | janvier | Em janeiro faz muito frio. | En janvier, il fait très froid. | u
 fevereiro | février | Fevereiro é o mês mais curto. | Février est le mois le plus court. | u
 março | mars | Em março começa a primavera. | En mars, le printemps commence. | u
 abril | avril | Em abril chove muito. | En avril, il pleut beaucoup. | u
 maio | mai | A minha irmã nasceu em maio. | Ma sœur est née en mai. | u
 junho | juin | Em junho há festas em Lisboa. | En juin, il y a des fêtes à Lisbonne. | u
 julho | juillet | Em julho vamos à praia. | En juillet, nous allons à la plage. | u
 agosto | août | Agosto é um mês de férias. | Août est un mois de vacances. | u
 setembro | septembre | Em setembro volto ao trabalho. | En septembre, je reprends le travail. | u
 outubro | octobre | Em outubro fica mais fresco. | En octobre, il fait plus frais. | u
 novembro | novembre | Em novembro os dias são curtos. | En novembre, les journées sont courtes. | u
 dezembro | décembre | Dezembro é o último mês do ano. | Décembre est le dernier mois de l'année. | u
"""

NOMS["numeros_pt"] = """
 zero | zéro | O termómetro marca zero graus. | Le thermomètre indique zéro degré. | u
 um | un | Só sobrou um. | Il n'en reste qu'un. | u
 dois | deux | Tenho dois irmãos. | J'ai deux frères. | u
 três | trois | O apartamento tem três janelas. | L'appartement a trois fenêtres. | u
 quatro | quatre | Somos quatro lá em casa. | Nous sommes quatre à la maison. | u
 cinco | cinq | O café custa um euro e cinco cêntimos. | Le café coûte un euro cinq. | u
 seis | six | Levanto-me às seis. | Je me lève à six heures. | u
 sete | sept | A semana tem sete dias. | La semaine a sept jours. | u
 oito | huit | A loja abre às oito. | Le magasin ouvre à huit heures. | u
 nove | neuf | Chego às nove. | J'arrive à neuf heures. | u
 dez | dix | Tenho dez minutos. | J'ai dix minutes. | u
 onze | onze | O comboio parte às onze. | Le train part à onze heures. | u
 doze | douze | O ano tem doze meses. | L'année a douze mois. | u
 treze | treize | O meu filho tem treze anos. | Mon fils a treize ans. | u
 catorze | quatorze | Somos catorze no grupo. | Nous sommes quatorze dans le groupe. | u
 quinze | quinze | Volto daqui a quinze minutos. | Je reviens dans quinze minutes. | u
 dezasseis | seize | Tenho dezasseis anos. | J'ai seize ans. | u | br=dezesseis
 dezassete | dix-sept | O autocarro dezassete vai para o centro. | Le bus dix-sept va au centre. | u | br=dezessete
 dezoito | dix-huit | Em Portugal vota-se aos dezoito anos. | Au Portugal, on vote à dix-huit ans. | u
 dezanove | dix-neuf | A minha irmã tem dezanove anos. | Ma sœur a dix-neuf ans. | u | br=dezenove
 vinte | vingt | O livro custa vinte euros. | Le livre coûte vingt euros. | u
 vinte e um | vingt et un | Moro no número vinte e um. | J'habite au numéro vingt et un. | u
 vinte e dois | vingt-deux | Somos vinte e dois na turma. | Nous sommes vingt-deux en classe. | u
 trinta | trente | Setembro tem trinta dias. | Septembre a trente jours. | u
 quarenta | quarante | O meu pai tem quarenta anos. | Mon père a quarante ans. | u
 cinquenta | cinquante | Estão cá cinquenta pessoas. | Il y a cinquante personnes ici. | u
 sessenta | soixante | Uma hora tem sessenta minutos. | Une heure a soixante minutes. | u
 setenta | soixante-dix | A minha avó tem setenta anos. | Ma grand-mère a soixante-dix ans. | u
 oitenta | quatre-vingts | O autocarro leva oitenta passageiros. | Le bus transporte quatre-vingts passagers. | u
 noventa | quatre-vingt-dix | O filme dura noventa minutos. | Le film dure quatre-vingt-dix minutes. | u
 cem | cent | Preciso de cem euros. | J'ai besoin de cent euros. | u
 cento | cent (devant un autre nombre) | O bilhete custa cento e vinte euros. | Le billet coûte cent vingt euros. | u
 duzentos | deux cents | Há duzentos alunos na escola. | Il y a deux cents élèves dans l'école. | u
 trezentos | trois cents | O hotel tem trezentos quartos. | L'hôtel a trois cents chambres. | u
 quinhentos | cinq cents | Para o concerto há quinhentos bilhetes. | Pour le concert, il y a cinq cents billets. | u
 mil | mille | A bicicleta custa mil euros. | Le vélo coûte mille euros. | u
o milhão | le million | A região de Lisboa tem quase três milhões de habitantes. | La région de Lisbonne compte presque trois millions d'habitants. | pl=milhões
 primeiro | premier | Moro no primeiro andar. | J'habite au premier étage. | u
 terceiro | troisième | Moramos no terceiro andar. | Nous habitons au troisième étage. | u
"""

NOMS["formas_pt"] = """
a forma | la forme | Que forma tem a mesa? | Quelle forme a la table ?
o círculo | le cercle | A criança desenha um círculo. | L'enfant dessine un cercle.
o quadrado | le carré | A janela é um quadrado. | La fenêtre est un carré.
a linha | la ligne | Escreve na primeira linha. | Écris sur la première ligne.
o ponto | le point | Falta um ponto no fim. | Il manque un point à la fin.
a risca | la rayure | Gosto da camisa às riscas. | J'aime la chemise à rayures. | br=listra
"""

NOMS["animais_pt"] = """
o animal | l'animal | É um animal muito calmo. | C'est un animal très calme. | pl=animais
o animal de estimação | l'animal de compagnie | Temos um animal de estimação em casa. | Nous avons un animal de compagnie à la maison. | pl=animais de estimação
o cão | le chien | O cão dorme no sofá. | Le chien dort sur le canapé. | pl=cães | br=cachorro
o gato | le chat | O gato sobe ao telhado. | Le chat monte sur le toit.
o pássaro | l'oiseau | Um pássaro canta no jardim. | Un oiseau chante dans le jardin.
o cavalo | le cheval | O cavalo corre pelo campo. | Le cheval court dans le champ.
a vaca | la vache | A vaca come erva. | La vache mange de l'herbe.
o porco | le cochon | O porco está na quinta. | Le cochon est à la ferme.
a ovelha | le mouton, la brebis | As ovelhas estão na serra. | Les moutons sont dans la montagne.
a galinha | la poule | A galinha pôs um ovo. | La poule a pondu un œuf.
o rato | la souris | Há um rato na cozinha. | Il y a une souris dans la cuisine.
o coelho | le lapin | O coelho come cenouras. | Le lapin mange des carottes.
o leão | le lion | O leão vive em África. | Le lion vit en Afrique. | pl=leões
o elefante | l'éléphant | O elefante é enorme. | L'éléphant est énorme.
o macaco | le singe | O macaco está na árvore. | Le singe est dans l'arbre.
o urso | l'ours | O urso dorme no inverno. | L'ours dort en hiver.
a aranha | l'araignée | Há uma aranha na parede. | Il y a une araignée sur le mur.
a mosca | la mouche | Entrou uma mosca pela janela. | Une mouche est entrée par la fenêtre.
a abelha | l'abeille | As abelhas fazem mel. | Les abeilles font du miel.
a tartaruga | la tortue | A tartaruga anda devagar. | La tortue marche lentement.
o rabo | la queue | O cão abana o rabo. | Le chien remue la queue.
a pata | la patte | O gato tem uma pata magoada. | Le chat a une patte blessée.
a árvore | l'arbre | Há uma árvore em frente de casa. | Il y a un arbre devant la maison.
a flor | la fleur | Ofereço-lhe uma flor. | Je lui offre une fleur.
o peixinho-dourado | le poisson rouge | O peixinho-dourado nada no aquário. | Le poisson rouge nage dans son bocal. | pl=peixinhos-dourados
"""

NOMS["clima_pt"] = """
o tempo | le temps (qu'il fait) | Como está o tempo hoje? | Quel temps fait-il aujourd'hui ? | u
o sol | le soleil | Esta manhã está sol. | Il fait soleil ce matin. | u
a chuva | la pluie | A chuva não para. | La pluie ne s'arrête pas. | u
a neve | la neige | A neve cobre a Serra da Estrela. | La neige couvre la Serra da Estrela. | u
o vento | le vent | Hoje está muito vento. | Il y a beaucoup de vent aujourd'hui.
a nuvem | le nuage | Não há uma única nuvem. | Il n'y a pas un seul nuage.
a tempestade | l'orage, la tempête | Vem aí uma tempestade. | Un orage arrive.
o calor | la chaleur | Em agosto faz muito calor. | En août, il fait très chaud. | u
a temperatura | la température | À noite a temperatura desce. | La nuit, la température baisse.
o grau | le degré | Estão vinte graus. | Il fait vingt degrés.
o céu | le ciel | O céu está muito azul. | Le ciel est très bleu.
o nevoeiro | le brouillard | Há nevoeiro na estrada. | Il y a du brouillard sur la route. | u
o gelo | la glace | Cuidado, há gelo. | Fais attention, il y a de la glace. | u
o guarda-chuva | le parapluie | Leva o guarda-chuva, vai chover. | Prends le parapluie, il va pleuvoir. | pl=guarda-chuvas
o clima | le climat | O clima desta região é ameno. | Le climat de cette région est doux.
a primavera | le printemps | Na primavera há muitas flores. | Au printemps, il y a beaucoup de fleurs.
o verão | l'été | No verão vamos para a praia. | L'été, nous allons à la plage. | pl=verões
o outono | l'automne | No outono caem as folhas. | En automne, les feuilles tombent.
o inverno | l'hiver | Aqui o inverno é chuvoso. | Ici, l'hiver est pluvieux.
o boneco de neve | le bonhomme de neige | A Anna faz um boneco de neve em frente de casa. | Anna fait un bonhomme de neige devant la maison. | pl=bonecos de neve
"""

NOMS["apresentar_pt"] = """
o cumprimento | le salut | Um cumprimento a todos. | Un salut à tous.
o país | le pays | De que país és? | De quel pays viens-tu ? | pl=países
a nacionalidade | la nationalité | Tenho dupla nacionalidade. | J'ai la double nationalité.
a língua | la langue | Falo três línguas. | Je parle trois langues.
a profissão | la profession | Qual é a tua profissão? | Quelle est ta profession ? | pl=profissões
a morada | l'adresse | Aponta a minha morada. | Note mon adresse. | br=endereço
o telefone | le téléphone | Dou-te o meu número de telefone. | Je te donne mon numéro de téléphone.
o e-mail | le courriel | Manda-me um e-mail. | Envoie-moi un courriel. | pl=e-mails
a assinatura | la signature | Falta a tua assinatura no papel. | Il manque ta signature sur le papier.
a pergunta | la question | Tenho uma pergunta para ti. | J'ai une question pour toi.
a resposta | la réponse | Não sei a resposta. | Je ne connais pas la réponse.
"""

NOMS["cafe_pt"] = """
a ementa | la carte, le menu | Pode trazer-nos a ementa, por favor? | Vous nous apportez la carte, s'il vous plaît ? | br=cardápio
o prato do dia | le plat du jour | O prato do dia custa nove euros. | Le plat du jour coûte neuf euros. | pl=pratos do dia
a gorjeta | le pourboire | Deixamos uma gorjeta na mesa. | Nous laissons un pourboire sur la table.
a reserva | la réservation | Tenho uma reserva em nome da Ana. | J'ai une réservation au nom d'Ana.
o guardanapo | la serviette (de table) | Pode dar-me outro guardanapo? | Pouvez-vous me donner une autre serviette ?
a toalha de mesa | la nappe | A toalha de mesa é branca. | La nappe est blanche. | pl=toalhas de mesa
o copo de vinho | le verre de vin | Um copo de vinho tinto, por favor. | Un verre de vin rouge, s'il vous plaît. | pl=copos de vinho
o jarro | la carafe, le pichet | Um jarro de água para a mesa. | Une carafe d'eau pour la table.
o balcão | le comptoir | Bebemos o café ao balcão. | Nous buvons le café au comptoir. | pl=balcões
o cozinheiro | le cuisinier | O cozinheiro prepara o bacalhau. | Le cuisinier prépare la morue.
o cliente | le client | O cliente espera à porta. | Le client attend à la porte.
a dose | la portion | Pedimos uma dose de batatas fritas. | Nous commandons une portion de frites. | br=porção
a meia dose | la demi-portion | Uma meia dose chega para mim. | Une demi-portion me suffit. | pl=meias doses
a bebida | la boisson | Que bebida queres? | Quelle boisson veux-tu ?
o limão | le citron | Um chá com limão, por favor. | Un thé au citron, s'il vous plaît. | pl=limões
a azeitona | l'olive | As azeitonas estão muito boas. | Les olives sont très bonnes.
a bica | l'expresso (à Lisbonne) | Uma bica e um pastel de nata, por favor. | Un expresso et un flan pâtissier, s'il vous plaît. | br=cafezinho
o galão | le grand café au lait | Ao pequeno-almoço bebo um galão. | Au petit-déjeuner, je bois un grand café au lait. | pl=galões
o pastel de nata | le flan pâtissier portugais | Os pastéis de nata ainda estão quentes. | Les flans pâtissiers sont encore chauds. | pl=pastéis de nata
a torrada | la tartine grillée | Uma torrada com manteiga, por favor. | Une tartine grillée beurrée, s'il vous plaît.
a tosta mista | le croque-monsieur | Para mim, uma tosta mista. | Pour moi, un croque-monsieur. | pl=tostas mistas | br=misto-quente
o bacalhau | la morue | Em Portugal come-se muito bacalhau. | Au Portugal, on mange beaucoup de morue. | u
a sardinha | la sardine | Em junho comem-se sardinhas assadas. | En juin, on mange des sardines grillées.
a manteiga | le beurre | Falta manteiga para as torradas. | Il manque du beurre pour les tartines. | u
"""

NOMS["compras_pt"] = """
o dinheiro | l'argent | Não tenho dinheiro comigo. | Je n'ai pas d'argent sur moi. | u
a moeda | la pièce de monnaie | Preciso de uma moeda para o carrinho. | J'ai besoin d'une pièce pour le chariot.
o cartão | la carte (bancaire) | Posso pagar com cartão? | Puis-je payer par carte ? | pl=cartões
a caixa | la caisse | Pague na caixa, por favor. | Payez à la caisse, s'il vous plaît. | br=caixa (o)
o carrinho | le chariot | O carrinho está cheio. | Le chariot est plein.
o saco | le sac | Quer um saco? | Voulez-vous un sac ? | br=sacola
o desconto | la remise | Há um desconto de vinte por cento. | Il y a une remise de vingt pour cent.
a promoção | la promotion | O queijo está em promoção. | Le fromage est en promotion. | pl=promoções
o talão | le ticket de caisse | Guarde o talão, por favor. | Gardez le ticket de caisse, s'il vous plaît. | pl=talões | br=recibo
o provador | la cabine d'essayage | O provador fica ao fundo. | La cabine d'essayage est au fond.
a montra | la vitrine | Vi-o na montra. | Je l'ai vu en vitrine. | br=vitrine
o empregado | le vendeur, l'employé | O empregado é muito simpático. | Le vendeur est très aimable. | br=vendedor
a empregada | la vendeuse, l'employée | A empregada ajuda-me a encontrar o meu tamanho. | La vendeuse m'aide à trouver ma taille. | br=vendedora
o presente | le cadeau | Procuro um presente para a minha mãe. | Je cherche un cadeau pour ma mère.
a marca | la marque | Não conheço essa marca. | Je ne connais pas cette marque.
a qualidade | la qualité | É de ótima qualidade. | C'est de très bonne qualité.
o talho | la boucherie | Compro a carne no talho. | J'achète la viande à la boucherie. | br=açougue
"""

NOMS["transportes_pt"] = """
o avião | l'avion | O avião parte às sete. | L'avion part à sept heures. | pl=aviões
o barco | le bateau | Atravessamos o Tejo de barco. | Nous traversons le Tage en bateau.
a mota | la moto | Ele vai para o trabalho de mota. | Il va au travail en moto. | br=moto
o camião | le camion | Um camião bloqueia a rua. | Un camion bloque la rue. | pl=camiões | br=caminhão
o voo | le vol | O meu voo chega ao meio-dia. | Mon vol arrive à midi.
o lugar | la place, le siège | O meu lugar é à janela. | Ma place est côté fenêtre.
o condutor | le conducteur | O condutor abre a porta. | Le conducteur ouvre la porte. | br=motorista
o passageiro | le passager | Hoje há poucos passageiros. | Aujourd'hui, il y a peu de passagers.
a paragem | l'arrêt (de bus) | Saímos na próxima paragem. | Nous descendons au prochain arrêt. | pl=paragens | br=ponto
a mala de viagem | la valise | A minha mala de viagem pesa muito. | Ma valise est très lourde. | pl=malas de viagem
a bagagem | les bagages | Despachamos a bagagem. | Nous enregistrons les bagages. | pl=bagagens
a viagem | le voyage | A viagem demora duas horas. | Le voyage dure deux heures. | pl=viagens
a estrada | la route | A estrada está cortada. | La route est coupée.
a gasolina | l'essence | Preciso de pôr gasolina. | J'ai besoin de prendre de l'essence. | u
o porto | le port | O barco chega ao porto. | Le bateau arrive au port.
o atraso | le retard | O comboio tem dez minutos de atraso. | Le train a dix minutes de retard.
o mapa | la carte, le plan | Olha para o mapa do metro. | Regarde le plan du métro.
a carrinha | la camionnette | Uma carrinha de entregas entra na rua. | Une camionnette de livraison entre dans la rue. | br=van
o cais | le quai | O barco para Cacilhas sai do cais dois. | Le bateau pour Cacilhas part du quai deux. | pl=cais
"""

NOMS["escola_pt"] = """
a escola | l'école | O meu filho vai para a escola de autocarro. | Mon fils va à l'école en bus.
o colégio | l'école privée, le collège | O colégio está fechado hoje. | L'école est fermée aujourd'hui.
a universidade | l'université | Ele estuda na Universidade de Coimbra. | Il étudie à l'université de Coimbra.
a aula | le cours | A aula começa às nove. | Le cours commence à neuf heures.
a turma | la classe | Há vinte alunos na turma. | Il y a vingt élèves dans la classe.
o professor | le professeur | O professor explica muito bem. | Le professeur explique très bien. | pl=professores
o aluno | l'élève | O aluno levanta a mão. | L'élève lève la main.
o estudante | l'étudiant | Sou estudante de português. | Je suis étudiant en portugais.
o exame | l'examen | Tenho um exame na sexta-feira. | J'ai un examen vendredi.
a nota | la note | Ele teve uma nota muito boa. | Il a eu une très bonne note.
o curso | le cours, la formation | Estou a fazer um curso de cozinha. | Je suis un cours de cuisine.
a disciplina | la matière | A minha disciplina preferida é História. | Ma matière préférée est l'histoire.
a lição | la leçon | Hoje estudamos a lição três. | Aujourd'hui, nous étudions la leçon trois. | pl=lições
o livro | le livre | Leio um livro por mês. | Je lis un livre par mois.
o caderno | le cahier | Escreve no caderno. | Écris dans le cahier.
a caneta | le stylo | Emprestas-me uma caneta? | Tu me prêtes un stylo ?
o lápis | le crayon | Ele desenha a lápis. | Il dessine au crayon. | pl=lápis
a borracha | la gomme | Preciso de uma borracha para apagar. | J'ai besoin d'une gomme pour effacer.
a régua | la règle | Traça a linha com a régua. | Trace la ligne avec la règle.
o horário | l'emploi du temps, l'horaire | Vê o horário das aulas. | Regarde l'emploi du temps.
a palavra | le mot | Não percebo esta palavra. | Je ne comprends pas ce mot.
a frase | la phrase | Escreve uma frase completa. | Écris une phrase complète.
o giz | la craie | O professor escreve no quadro com giz. | Le professeur écrit au tableau à la craie. | u
"""

NOMS["trabalho_pt"] = """
o trabalho | le travail | Procuro trabalho desde março. | Je cherche du travail depuis mars.
o escritório | le bureau | O escritório fica no centro. | Le bureau est au centre-ville.
a empresa | l'entreprise | Trabalho numa empresa pequena. | Je travaille dans une petite entreprise.
o chefe | le chef, le patron | O meu chefe chega cedo. | Mon patron arrive tôt.
o colega | le collègue | Almoço com os meus colegas. | Je déjeune avec mes collègues.
o ordenado | le salaire | O ordenado não é muito alto. | Le salaire n'est pas très élevé. | br=salário
o contrato | le contrat | Assino o contrato amanhã. | Je signe le contrat demain.
a reunião | la réunion | A reunião dura uma hora. | La réunion dure une heure. | pl=reuniões
o projeto | le projet | Estamos a trabalhar num projeto novo. | Nous travaillons sur un nouveau projet.
a tarefa | la tâche | Hoje tenho muitas tarefas. | Aujourd'hui, j'ai beaucoup de tâches.
a pausa | la pause | Fazemos uma pausa de dez minutos. | Nous faisons une pause de dix minutes.
a entrevista | l'entretien | Tenho uma entrevista na segunda-feira. | J'ai un entretien lundi.
a fábrica | l'usine | A fábrica fica fora da cidade. | L'usine est en dehors de la ville.
o negócio | l'affaire, le commerce | Ele abriu um negócio na praça. | Il a ouvert un commerce sur la place.
o emprego | l'emploi | Ela tem um emprego novo. | Elle a un nouvel emploi.
"""

NOMS["lazer_pt"] = """
o lazer | les loisirs | O fim de semana é tempo de lazer. | Le week-end est un temps de loisirs. | u
o filme | le film | O filme começa às oito. | Le film commence à huit heures.
a música | la musique | Ouço música enquanto cozinho. | J'écoute de la musique en cuisinant. | u
a canção | la chanson | Gosto muito desta canção. | Cette chanson me plaît beaucoup. | pl=canções
o fado | le fado | Ouvimos fado em Alfama. | Nous écoutons du fado dans l'Alfama. | u
o concerto | le concert | Vamos a um concerto no sábado. | Nous allons à un concert samedi.
o desporto | le sport | Faço desporto três vezes por semana. | Je fais du sport trois fois par semaine. | br=esporte
o jogo | le match, le jeu | O jogo é às cinco. | Le match est à cinq heures.
a equipa | l'équipe | A minha equipa ganhou ontem. | Mon équipe a gagné hier. | br=equipe
o futebol | le football | Ao domingo vemos futebol na televisão. | Le dimanche, nous regardons le foot à la télé. | u
a festa | la fête | A festa acaba tarde. | La fête finit tard.
a dança | la danse | Há dança na praça. | Il y a de la danse sur la place.
a praia | la plage | A praia fica a dez minutos. | La plage est à dix minutes.
a montanha | la montagne | Subimos à montanha no domingo. | Nous montons à la montagne dimanche.
o ginásio | la salle de sport | Vou ao ginásio de manhã. | Je vais à la salle de sport le matin. | br=academia
a piscina | la piscine | A piscina abre em junho. | La piscine ouvre en juin.
a revista | le magazine | Compro uma revista no quiosque. | J'achète un magazine au kiosque.
o jornal | le journal | Leio o jornal com o café. | Je lis le journal avec le café. | pl=jornais
a televisão | la télévision | Vemos televisão depois do jantar. | Nous regardons la télévision après le dîner. | pl=televisões
a fotografia | la photo | Vou tirar-te uma fotografia. | Je vais te prendre en photo. | br=foto
"""

NOMS["dia_pt"] = """
a rotina | la routine | A minha rotina começa às sete. | Ma routine commence à sept heures.
o despertador | le réveil | O despertador toca às seis. | Le réveil sonne à six heures.
a escova de dentes | la brosse à dents | Ponho a escova de dentes no copo. | Je mets la brosse à dents dans le verre. | pl=escovas de dentes
a pasta de dentes | le dentifrice | Acabou a pasta de dentes. | Il n'y a plus de dentifrice. | pl=pastas de dentes | br=creme dental
o pente | le peigne | O pente está na casa de banho. | Le peigne est dans la salle de bain.
o champô | le shampooing | O champô acabou. | Le shampooing est fini. | br=xampu
o costume | l'habitude | Jantar tarde é um costume português. | Dîner tard est une habitude portugaise.
"""
