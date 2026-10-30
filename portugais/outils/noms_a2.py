# -*- coding: utf-8 -*-
"""Les noms du A2 portugais, par theme. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que noms_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'A2'

# (id du theme, nom portugais, theme source dont on reprend l'icone)
THEMES = [
    ('familia_a2_pt', 'Família e relações', 'familie_a2'),
    ('trabalho_a2_pt', 'Trabalho e profissões', 'berufe_a2'),
    ('comida_a2_pt', 'Comida e cozinha 1', 'las_frutas'),
    ('comida_a2_pt_2', 'Comida e cozinha 2', 'las_frutas'),
    ('casa_a2_pt', 'A casa 1', 'nom_casa'),
    ('casa_a2_pt_2', 'A casa 2', 'nom_casa'),
    ('saude_a2_pt', 'O corpo e a saúde', 'la_salud'),
    ('roupa_a2_pt', 'Roupa e aparência', 'la_moda'),
    ('natureza_a2_pt', 'Natureza e ambiente 1', 'tiere_a2'),
    ('natureza_a2_pt_2', 'Natureza e ambiente 2', 'tiere_a2'),
    ('viagens_a2_pt', 'Viagens e transportes 1', 'el_viaje'),
    ('viagens_a2_pt_2', 'Viagens e transportes 2', 'el_viaje'),
    ('cidade_a2_pt', 'A cidade', 'los_servicios'),
    ('escola_a2_pt', 'Escola e estudos', 'los_estudios'),
    ('cultura_a2_pt', 'Tempos livres e cultura 1', 'el_arte'),
    ('cultura_a2_pt_2', 'Tempos livres e cultura 2', 'el_arte'),
    ('desporto_a2_pt', 'Desporto', 'el_deporte'),
    ('media_a2_pt', 'Media e comunicação', 'la_tecnologia'),
    ('dinheiro_a2_pt', 'Dinheiro e economia', 'einkaufen_geld_a2'),
    ('sentimentos_a2_pt', 'Sentimentos e caráter', 'gefuehle_charakter_a2'),
    ('sociedade_a2_pt', 'Sociedade e política', 'politik_gesellschaft_a2'),
    ('lei_a2_pt', 'Lei e segurança', 'la_seguridad'),
    ('tempo_a2_pt', 'O tempo', 'zeit_kalender_a2'),
    ('quotidiano_a2_pt', 'Palavras do dia a dia', 'grundwortschatz_a2'),
]

NOMS = {
"familia_a2_pt": """
o adolescente | l'adolescent, jeune | A monitora cuida de dez adolescentes. | L'animatrice s'occupe de dix adolescents. | g?
a amizade | l'amitié | A nossa amizade dura vinte anos. | Notre amitié dure depuis vingt ans.
o antepassado | l'ancêtre | Os antepassados dele eram galegos. | Ses ancêtres étaient galiciens.
o apoio | le soutien | Obrigado pelo teu apoio. | Merci pour ton soutien.
o avós | les grands-parents | Os meus avós moram no interior. | Mes grands-parents habitent à la campagne. | pl=avoses
o bisavô | l'arrière-grand-père | O meu bisavô nasceu em 1910. | Mon arrière-grand-père est né en 1910.
o conflito | le conflit | Houve um conflito entre os vizinhos. | Il y a eu un conflit entre voisins.
o conhecido | la connaissance (personne) | Um conhecido mostrou-me o apartamento. | Une connaissance m'a montré l'appartement.
o contacto | le contact | Continuamos em contacto. | Nous restons en contact.
o convite | l'invitation | Recebi o convite por e-mail. | J'ai reçu l'invitation par courriel.
o cônjuge | le conjoint | O cônjuge também precisa de assinar. | Le conjoint doit signer aussi.
a decisão | la décision | Foi uma decisão difícil. | Ce fut une décision difficile. | pl=decisões
a desculpa | l'excuse | Ele sempre tem uma boa desculpa na ponta da língua. | Il a toujours une bonne excuse toute prête.
a discussão | la dispute | Tivemos uma discussão parva. | Nous avons eu une dispute idiote. | pl=discussões
o divórcio | le divorce | O divórcio foi difícil. | Le divorce a été difficile.
a esposa | l'épouse | A esposa dele é médica. | Sa femme est médecin. | g?
o estado civil | la situation familiale | Qual é o teu estado civil? | Quelle est ta situation familiale ? | pl=estados civis
a etapa | l'étape | A primeira etapa da viagem foi a mais longa. | La première étape du voyage a été la plus longue.
a experiência | l'expérience | Ele tem muita experiência no setor. | Il a beaucoup d'expérience dans le secteur.
o favor | le service, la faveur | Eu votaria a favor do novo parque. | Moi, je voterais pour le nouveau parc.
o genro | le gendre | O genro dele mora no Chile. | Son gendre vit au Chili.
a geração | la génération | Ele é da geração dos meus pais. | Il est de la génération de mes parents. | pl=gerações
o gémeo | le jumeau | Os gémeos são muito parecidos. | Les jumeaux se ressemblent beaucoup.
a herança | l'héritage | A casa é uma herança de família. | La maison est un héritage familial.
a infância | l'enfance | Ele passou a infância no campo. | Il a passé son enfance à la campagne.
a juventude | la jeunesse | Na juventude ele viajou muito. | Dans sa jeunesse il a beaucoup voyagé.
a madrinha | la marraine | A madrinha veio à festa. | La marraine est venue à la fête.
a meta | l'objectif | A minha meta é terminar em junho. | Mon objectif est de finir en juin.
o nascimento | la naissance | O nascimento foi na primavera. | La naissance a eu lieu au printemps.
a neta | la petite-fille | A minha neta está a aprender a andar. | Ma petite-fille apprend à marcher.
a nora | la belle-fille | A minha nora é médica. | Ma belle-fille est médecin.
o padrinho | le parrain | O padrinho deu-lhe o relógio de presente. | Son parrain lui a offert la montre.
o parceiro | le partenaire, compagnon | Ela está a procurar um parceiro para o projeto. | Elle cherche un partenaire pour le projet.
o parente | le parent (famille) | Esse parente mora no Canadá. | Ce parent vit au Canada.
o parentesco | le lien de parenté | Não sei que parentesco eles têm. | Je ne sais pas quel lien de parenté ils ont.
a relação | la relation | A nossa relação é muito próxima. | Notre relation est très étroite. | pl=relações
a sogra | la belle-mère | A minha sogra vem nos visitar. | Ma belle-mère vient nous rendre visite.
a velhice | la vieillesse | A velhice tem as suas vantagens. | La vieillesse a ses avantages.
a visita | la visite | Esperamos uma visita hoje à tarde. | Nous attendons une visite cet après-midi.
""",
"trabalho_a2_pt": """
a agenda | l'agenda | Anoto na agenda. | Je le note dans l'agenda.
o agricultor | l'agriculteur | O agricultor trabalha de manhã cedo. | L'agriculteur travaille tôt le matin.
a ama | le baby-sitter | Ele ama o trabalho acima de tudo. | Il aime son travail par-dessus tout.
o autor | l'auteur | Quem é o autor deste livro? | Qui est l'auteur de ce livre ?
o bico | le petit boulot | Além da faculdade, eu tenho um bico. | À côté de mes études, j'ai un petit boulot.
o canalizador | le plombier | O canalizador conserta o cano. | Le plombier répare la tuyauterie.
o cargo | le poste | Finalmente ele aceitou o cargo. | Finalement il a accepté le poste.
o comerciante | le commerçant | Ele é comerciante no varejo. | Il est commerçant dans le commerce de détail. | g?
o currículo | CV | Envio o meu currículo para a empresa. | J'envoie mon CV à l'entreprise.
o dentista | le dentiste | O dentista examina os meus dentes. | Le dentiste examine mes dents.
o departamento | le service | Trabalho no departamento de vendas. | Je travaille au service des ventes.
o dia de trabalho | le jour ouvré | O meu dia de trabalho começa às oito. | Ma journée de travail commence à huit heures. | pl=dias de trabalho
o dono de casa | l'homme au foyer | O meu vizinho é dono de casa. | Mon voisin est homme au foyer. | pl=donos de casa
o enfermeiro | l'infirmier | O meu irmão trabalha como enfermeiro. | Mon frère travaille comme infirmier.
o engenheiro | l'ingénieur | O engenheiro está a planejar a ponte nova. | L'ingénieur planifie le nouveau pont.
a entrevista de emprego | l'entretien d'embauche | A entrevista de emprego foi muito bem. | L'entretien d'embauche s'est très bien passé. | g? | pl=entrevistas de emprego
a escrivaninha | le bureau (meuble) | Tenho papéis por toda a escrivaninha. | J'ai des papiers partout sur le bureau.
o fotógrafo | le photographe | O fotógrafo tira fotos bonitas. | Le photographe prend de belles photos.
o funcionário | l'employé, collaborateur | A empresa tem vinte funcionários. | L'entreprise a vingt employés.
o home office | le télétravail | Hoje estou a trabalhar de home office. | Je travaille en télétravail aujourd'hui. | g? | pl=homes offices
a hora extra | l'heure supplémentaire | Ele fez muitas horas extras. | Il a fait beaucoup d'heures supplémentaires. | g? | pl=horas extras
o mecânico | le mécanicien | O mecânico conserta o meu carro. | Le mécanicien répare ma voiture.
o meio período | le temps partiel | Ela trabalha meio período desde o ano passado. | Elle travaille à temps partiel depuis l'année dernière. | pl=meios períodos
o modelo | le mannequin | Ela trabalha como modelo em Milão. | Elle travaille comme mannequin à Milan.
o músico | le musicien | O músico ensaia todo dia. | Le musicien s'exerce tous les jours.
a oficina | l'atelier (formation) | Deixei o carro na oficina. | J'ai laissé la voiture au garage. | g?
o orçamento | le budget, le devis | O orçamento está alto demais. | Le devis est trop élevé.
o pedido | la commande | O seu pedido chega amanhã. | Votre commande arrive demain.
o período integral | le temps plein | Ele trabalha em período integral nesta empresa. | Il travaille à temps plein dans cette entreprise. | pl=períodos integrais
o programador | le programmeur | O programador escreve código novo. | Le programmeur écrit du nouveau code.
a reformada | la retraitée | A minha mãe está reformada há dois anos. | Ma mère est retraitée depuis deux ans. | g?
o reformado | le retraité | O meu vizinho está reformado há um ano. | Mon voisin est retraité depuis un an.
o relatório | le rapport | Entrego o relatório na sexta. | Je rends le rapport vendredi.
a secretária | la secrétaire | A secretária atende o telefone. | La secrétaire répond au téléphone. | g?
a tinta | l'encre | A tinta preta acabou. | L'encre noire est finie.
o turno | le tour, le poste | Trabalho no turno da tarde. | Je travaille de l'après-midi.
o técnico | le technicien | O técnico vem amanhã de manhã. | Le technicien vient demain matin.
o veterinário | le vétérinaire | O veterinário trata animais doentes. | Le vétérinaire soigne les animaux malades.
""",
"comida_a2_pt": """
o abacate | l'avocat (fruit) | Ponho abacate na salada. | Je mets de l'avocat dans la salade.
a abobrinha | la courgette | Faço a abobrinha grelhada. | Je fais griller la courgette.
o abridor de latas | l'ouvre-boîte | O abridor de latas está na gaveta. | L'ouvre-boîte est dans le tiroir. | pl=abridores de latas
a abóbora | la citrouille, la courge | Fazemos sopa de abóbora no outono. | En automne, on fait de la soupe à la citrouille.
o alho-poró | le poireau | O alho-poró tem um sabor suave. | Le poireau a un goût doux. | g? | pl=alhos-porós
a ameixa | la prune | Estas ameixas vêm da árvore do meu avô. | Ces prunes viennent de l'arbre de mon grand-père.
a amora | la mûre | No campo colhemos amoras. | À la campagne, on cueille des mûres.
o ananás | l'ananas | O ananás está na caixa ao lado. | L'ananas est dans la caisse d'à côté. | pl=ananases
a assadeira | plaque de four | O bolo está na assadeira. | Le gâteau est sur la plaque de four.
o avental | le tablier | Visto o avental para cozinhar. | Je mets le tablier pour cuisiner.
o batedor | le fouet | O batedor bate os ovos. | Le fouet bat les œufs.
a berinjela | l'aubergine | A berinjela é roxa por fora. | L'aubergine est violette à l'extérieur.
o brócolis | le brocoli | A minha filha come brócolis sem reclamar. | Ma fille mange du brocoli sans protester. | pl=brócolis
a cafeteira | la machine à café | De manhã, ligo a cafeteira. | Le matin, j'allume la machine à café.
a cereja | la cerise | As cerejas são minha fruta favorita. | Les cerises sont mon fruit préféré.
o champignon | le champignon de Paris | Faço uma omelete com champignons. | Je fais une omelette aux champignons.
o chocolate | le chocolat | Eu como um pedaço de chocolate todo dia. | Je mange un carré de chocolat chaque jour. | g?
o coco | la noix de coco | É difícil abrir um coco. | C'est difficile d'ouvrir une noix de coco.
a colher de pau | la cuillère en bois | Eu mexo com a colher de pau. | Je remue avec la cuillère en bois. | g? | pl=colheres de pau
a compota | la confiture | A compota tem gosto de morango. | La confiture a un goût de fraises. | g?
a couve-flor | le chou-fleur | A couve-flor é branca e grande. | Le chou-fleur est blanc et gros. | pl=couves-flores
o creme de leite | la crème | O creme deixa o café cremoso. | La crème rend le café onctueux. | pl=cremes de leite | ex?
o damasco | l'abricot | Os damascos estão baratos esta semana. | Les abricots sont bon marché cette semaine.
a ementa de bebidas | la carte des boissons |  |  | g? | pl=ementas de bebidas | ex=?
a ervilha | le petit pois | A criança não gosta de ervilhas. | L'enfant n'aime pas les petits pois.
o espinafre | l'épinard | O espinafre tem muito ferro. | Les épinards contiennent beaucoup de fer.
a farinha | la farine | A receita leva meio quilo de farinha. | La recette demande un demi-kilo de farine.
o feijão | le haricot | As vagens estão muito frescas. | Les haricots verts sont très frais. | pl=feijões | ex?
a framboesa | la framboise | Faço uma torta com framboesas. | Je fais une tarte aux framboises.
o ingrediente | l'ingrédient | Falta um ingrediente. | Il manque un ingrédient.
o iogurte | le yaourt | No pequeno-almoço eu como iogurte com mirtilos. | Au petit-déjeuner, je mange du yaourt avec des myrtilles.
o kiwi | le kiwi | O kiwi tem muita vitamina C. | Le kiwi contient beaucoup de vitamine C.
o legumes | le légumes | Come mais legumes! | Mange plus de légumes ! | g? | pl=legumes
a linguiça | la saucisse | Na feira eu compro linguiça fresca. | Au marché, j'achète de la saucisse fraîche. | g?
a louça | la vaisselle | Depois de comer eu lavo a louça. | Après le repas, je fais la vaisselle. | g?
a massa | la pâte | Deixe a massa descansar uma hora. | Laisse reposer la pâte une heure.
o mel | le miel | O mel vem das nossas próprias abelhas. | Le miel vient de nos propres abeilles. | pl=méis
a melancia | la pastèque | No verão comemos melancia na praia. | En été, on mange de la pastèque à la plage.
o melão | le melon | Este melão está a cheirar muito bem. | Ce melon sent très bon. | pl=melões
o milho | le maïs | Na salada há milho e tomate. | Dans la salade, il y a du maïs et de la tomate.
""",
"comida_a2_pt_2": """
o mirtilo | la myrtille, le bleuet | No pequeno-almoço como iogurte com mirtilos. | Au petit-déjeuner, je mange un yaourt aux myrtilles.
a mostarda | la moutarde | A mostarda combina bem com a linguiça. | La moutarde va bien avec la saucisse. | g?
a máquina de café | la machine à café | A máquina de café faz muito barulho de manhã. | La machine à café fait beaucoup de bruit le matin. | g? | pl=máquinas de café
a noz | la noix | As nozes são boas para o cérebro. | Les noix sont bonnes pour le cerveau.
a peneira | la passoire |  |  | g? | ex=?
a pimenta-do-reino | le poivre | Eu gosto de pimenta-do-reino. | J'aime le poivre noir. | pl=pimentas-dos-reinos
o pãozinho | le petit pain | No pequeno-almoço eu como dois pãezinhos. | Au petit-déjeuner, je mange deux petits pains. | ex?
o pêssego | la pêche | Quero um quilo de pêssegos, por favor. | Je voudrais un kilo de pêches, s'il vous plaît.
o refrigerante | la limonade | A limonada está gelada. | La limonade est glacée. | g? | ex?
o repolho | le chou | Este repolho pesa quase dois quilos. | Ce chou pèse presque deux kilos.
a rodela | la rondelle | Corte o limão em rodelas. | Coupe le citron en rondelles.
o sabor | le goût | Há um sabor muito forte. | Ça a un goût très fort.
o saca-rolhas | le tire-bouchon | Preciso de um saca-rolhas para a garrafa. | J'ai besoin d'un tire-bouchon pour la bouteille. | g? | pl=sacas-rolhas
a tampa | le couvercle | Ponha a tampa na panela para ferver mais rápido. | Mets le couvercle sur la marmite pour que ça bouille plus vite.
a tangerina | la mandarine | As crianças descascam as tangerinas sozinhas. | Les enfants épluchent les mandarines tout seuls.
o tempero | l'épice | Este tempero é muito picante. | Cette épice est très piquante.
a tigela | le saladier | Misturo a massa na tigela. | Je mélange la pâte dans le saladier.
a toranja | le pamplemousse | A toranja é um pouco amarga. | Le pamplemousse est un peu amer.
a tábua | la planche | Corte o pão na tábua. | Coupe le pain sur la planche.
o vapor | la vapeur | Sai vapor da panela. | De la vapeur sort de la marmite.
o vinagre | le vinaigre | Tempere a salada com vinagre. | Assaisonne la salade au vinaigre.
""",
"casa_a2_pt": """
o algodão | le coton | Prefiro camisas de algodão. | Je préfère les chemises en coton. | pl=algodões
o alicate | la pince | Ele corta o fio com o alicate. | Il coupe le câble avec la pince.
o aquecedor | le poêle | O aquecedor aquece a sala toda. | Le poêle chauffe toute la pièce.
o aspirador de pó | l'aspirateur | O aspirador faz muito barulho. | L'aspirateur fait beaucoup de bruit. | pl=aspiradores de pó | ex?
o azulejo | le carreau | Os azulejos são do século passado. | Les carreaux datent du siècle dernier.
o balde | le seau | Encha o balde de água. | Remplis le seau d'eau.
a bandeja | le plateau | Traga a bandeja da cozinha. | Apporte le plateau de la cuisine.
o banquinho | le tabouret | Sente-se no banquinho, por favor. | Assieds-toi sur le tabouret, s'il te plaît.
a bengala | le bâton | O velhinho anda de bengala. | Le vieil homme marche avec un bâton. | g?
o cabide | le cintre | Não há mais cabides no armário. | Il n'y a plus de cintres dans l'armoire.
a caixa de correio | la boîte aux lettres | Não há nada na caixa de correio. | Il n'y a rien dans la boîte aux lettres. | pl=caixas de correio
a caixa de ferramentas | la boîte à outils | A caixa de ferramentas está no porão. | La boîte à outils est au sous-sol. | pl=caixas de ferramentas
a caixa de mudança | le carton de déménagement | A caixa de mudança já está cheia. | Le carton de déménagement est déjà plein. | g? | pl=caixas de mudança
a caixa de papelão | le carton | O gato está dentro da caixa de papelão. | Le chat est dans le carton. | pl=caixas de papelão
a caixinha | la boîte | Na caixinha há fotos antigas. | Il y a de vieilles photos dans la boîte.
o caixote | la caisse | Os livros ainda estão no caixote. | Les livres sont encore dans la caisse.
o caixote do lixo | la corbeille |  |  | pl=caixotes do lixo | ex=?
a campainha | la sonnette | Alguém está a tocar a campainha. | Quelqu'un sonne à la porte.
o canto | le coin | Há um abajur no canto. | Il y a une lampe dans le coin.
a caçarola | la cocotte | O ensopado é feito em panela de barro. | Le ragoût se fait en cocotte en terre. | ex?
a cerca | la clôture | Puseram uma cerca ao redor da obra. | Ils ont mis une clôture autour du chantier.
a cesta | le panier | Deixe a fruta na cesta. | Laisse les fruits dans le panier.
o cesto | le panier | O cesto está cheio de maçãs. | Le panier est plein de pommes.
o cesto de roupa suja | le panier à linge | O cesto de roupa suja está a transbordar. | Le panier à linge est débordant. | pl=cestos de roupa suja
a chave de fenda | le tournevis | Passe-me a chave de fenda pequena. | Passe-moi le petit tournevis. | pl=chaves de fenda
o condomínio | la copropriété | O condomínio reúne-se em maio. | La copropriété se réunit en mai.
a corrente | la chaîne | A corrente da bicicleta arrebentou. | La chaîne du vélo a cassé. | g?
o couro | le cuir | Um cinto de couro. | Une ceinture en cuir.
o criado-mudo | la table de chevet | O criado-mudo tem uma gaveta. | La table de chevet a un tiroir. | pl=criados-mudos
a cúpula | l'abat-jour | Uma meia está pendurada na cúpula do abajur. | Une chaussette pend à l'abat-jour de la lampe.
o degrau | la marche | Cuidado com o último degrau. | Attention à la dernière marche.
o depósito | le débarras | Guardamos as malas no depósito. | Nous gardons les valises au débarras.
o esfregão | la serpillière | Passo o esfregão aos sábados. | Je passe la serpillière le samedi. | pl=esfregões
a estante de livros | la bibliothèque (meuble) | A estante de livros está cheia. | La bibliothèque est pleine. | g? | pl=estantes de livros
a fechadura | la serrure | Trocaram a fechadura na semana passada. | Ils ont changé la serrure la semaine dernière.
a ferramenta | l'outil | Ele guarda as ferramentas na garagem. | Il range les outils dans le garage.
o ferro | le fer | A grade é de ferro. | La grille est en fer.
o financiamento imobiliário | le prêt immobilier | Pagamos o financiamento todo mês. | Nous payons le prêt chaque mois. | pl=financiamentos imobiliários | ex?
a fita adesiva | le ruban adhésif | Cole o papel com fita adesiva. | Colle le papier avec du ruban adhésif. | pl=fitas adesivas
a furadeira | la perceuse | Preciso da furadeira para pendurar a estante. | J'ai besoin de la perceuse pour fixer l'étagère.
""",
"casa_a2_pt_2": """
o gancho | le crochet | Pendura o casaco no gancho! | Accroche ton manteau au crochet !
a grade | la grille | A grade do parque fecha às dez. | La grille du parc ferme à dix heures.
o gás | le gaz | Os gases dos carros poluem o ar. | Les gaz d'échappement des voitures polluent l'air. | pl=gases
o hall de entrada | le hall d'entrée |  |  | pl=halls de entrada | ex=?
o inquilino | le locataire | O inquilino paga no início do mês. | Le locataire paie en début de mois.
o jardim da frente | le jardin devant | Flores crescem no jardim da frente. | Des fleurs poussent dans le jardin devant la maison. | pl=jardins da frente
a lareira | la cheminée | Acendemos a lareira ao anoitecer. | Nous avons allumé la cheminée à la tombée du jour.
a luminária de chão | le lampadaire | A luminária de chão fica ao lado do sofá. | Le lampadaire est à côté du canapé. | pl=luminárias de chão
a lã | la laine | O suéter é de lã. | Le pull est en laine.
a mancha | la tache | Há uma mancha na toalha de mesa. | Il y a une tache sur la nappe.
o martelo | le marteau | Preciso de um martelo para o prego. | J'ai besoin d'un marteau pour le clou.
a mesa de centro | la table basse | A chávena está em cima da mesa de centro. | La tasse est sur la table basse. | pl=mesas de centro
o metal | le métal | A porta é de metal. | La porte est en métal.
a moradia | le logement | O preço da moradia sobe. | Le prix du logement augmente.
a mudança | le déménagement | A mudança é no sábado. | Le déménagement est samedi.
o muro | le mur (extérieur) | O muro do jardim caiu com a tempestade. | Le mur du jardin est tombé avec l'orage.
a máquina | la machine | A máquina lava sem fazer barulho. | La machine lave très silencieusement. | g?
o papelão | le carton | Guarde os livros em uma caixa de papelão. | Range les livres dans une boîte en carton. | pl=papelões
o parafuso | la vis | O parafuso está frouxo. | La vis est desserrée.
a pilha | la pile | O comando precisa de pilhas novas. | La télécommande a besoin de piles neuves.
o pisca-pisca | la guirlande lumineuse | Há um pisca-pisca ao redor da planta. | Il y a une guirlande lumineuse autour de la plante. | pl=piscas-piscas
a poeira | la poussière | Há poeira nas estantes. | Il y a de la poussière sur les étagères.
a poltrona | le fauteuil | A poltrona fica perto da janela. | Le fauteuil est près de la fenêtre. | g?
a prateleira | l'étagère | Ponha os pratos na prateleira de cima. | Mets les assiettes sur l'étagère du haut.
o prego | le clou | Falta um prego na tábua. | Il manque un clou dans la planche.
a proprietária | la propriétaire (bailleuse) | A proprietária mora no térreo. | La propriétaire habite au rez-de-chaussée. | g?
o proprietário | le propriétaire | O proprietário mora em outra cidade. | Le propriétaire habite une autre ville.
o pátio interno | la cour intérieure | O pátio interno é muito verde. | La cour intérieure est très verdoyante. | pl=pátios internos
o pôster | le poster | No meu quarto há um pôster da minha banda favorita. | Dans ma chambre, il y a un poster de mon groupe préféré.
o radiador | le radiateur | O radiador fica embaixo da janela. | Le radiateur est sous la fenêtre.
a reforma | les travaux | O apartamento está em reforma. | L'appartement est en travaux.
o sabão | la lessive | O sabão acabou. | La lessive est finie. | pl=sabões
a sala | le salon, séjour | Na sala tem um sofá grande. | Il y a un grand canapé dans le salon.
a tarefas domésticas | le ménage, tâches ménagères | Nas tarefas de casa todo mundo ajuda. | Tout le monde aide aux tâches ménagères. | pl=tarefas domésticas | ex?
o tecido | le tissu | É um tecido muito macio. | C'est un tissu très doux.
a tesoura | les ciseaux | Passa-me a tesoura, por favor. | Donne-moi les ciseaux, s'il te plaît. | g?
o tijolo | la brique | A casa é de tijolo. | La maison est en brique.
o toldo | le store (auvent) | Sentamos na sombra, debaixo do toldo. | Nous nous asseyons à l'ombre, sous le store.
a tomada | la prise | Não há nenhuma tomada perto da cama. | Il n'y a pas de prise près du lit.
a tábua de passar | la planche à repasser | A tábua de passar está fechada. | La planche à repasser est pliée. | g? | pl=tábuas de passar
o térreo | le rez-de-chaussée | Vamos situar a cozinha no térreo. | Nous placerons la cuisine au rez-de-chaussée.
o vaso | le pot de fleurs | Regue os vasos da varanda. | Arrose les pots du balcon.
a vassoura | le balai | A vassoura está atrás da porta. | Le balai est derrière la porte.
o ventilador | le ventilateur | Em agosto o ventilador não para. | En août le ventilateur ne s'arrête pas.
o vidro | le verre (matière) | A garrafa é de vidro. | La bouteille est en verre.
a vizinha | la voisine | A minha vizinha rega as minhas plantas. | Ma voisine arrose mes fleurs.
a vizinhança | le voisinage | A vizinhança é muito tranquila. | Le voisinage est très calme. | g?
""",
"saude_a2_pt": """
a alergia | l'allergie | Tenho alergia a pólen. | Je suis allergique au pollen.
a balança | la balance (pèse-personne) | Suba na balança, por favor. | Montez sur la balance, s'il vous plaît.
o bem-estar | le bien-être | O desporto melhora o bem-estar. | Le sport améliore le bien-être. | pl=bens-estares
a bochecha | la joue | Ele deu um beijo na bochecha dela. | Il lui a fait un bisou sur la joue.
o bumbum | les fesses | Depois do passeio longo de bicicleta o meu bumbum está a doer. | Après la longue balade à vélo, j'ai mal aux fesses.
o calcanhar | le talon | Estes sapatos machucam o meu calcanhar. | Ces chaussures me font mal au talon.
a calma | le calme | Preciso de um pouco de calma. | J'ai besoin d'un peu de calme.
o consultório | le cabinet, la consultation | O consultório abre às nove. | Le cabinet ouvre à neuf heures.
os cosméticos | les cosmétiques, soins de beauté | Os cosméticos ficam no primeiro andar. | Les cosmétiques se trouvent au premier étage.
o cotovelo | le coude | Não ponha os cotovelos na mesa. | Ne mets pas les coudes sur la table.
a coxa | la cuisse | O médico aplica a injeção na coxa dele. | Le médecin lui fait la piqûre dans la cuisse.
o creme | la crème | Este creme é bom para pele seca. | Cette crème est bonne pour la peau sèche.
o dedo do pé | l'orteil | Bati o dedo do pé na mesa. | Je me suis cogné l'orteil contre la table. | pl=dedos do pé
a dieta | le régime | Estou de dieta desde janeiro. | Je suis au régime depuis janvier.
o doutor | le docteur | Amanhã vou ao doutor. | Je vais chez le docteur demain.
o enjoo | la nausée | O enjoo vem da comida. | La nausée vient de la nourriture.
o equilíbrio | l'équilibre | Busco um equilíbrio entre trabalho e família. | Je cherche un équilibre entre travail et famille.
o exame | l'analyse | Vou fazer um exame de sangue. | Je fais une analyse de sang.
o ferimento | la blessure | O ferimento já está melhor. | La blessure va déjà mieux.
a gota | la goutte | Toma dez gotas antes de comer. | Prends dix gouttes avant le repas. | g?
o hábito | l'habitude | É um bom hábito. | C'est une bonne habitude.
o lenço | le mouchoir |  |  | ex=?
o lábio | la lèvre | Com o frio os meus lábios racham. | Avec le froid, j'ai les lèvres gercées.
a maca | la table d'examen | A médica pede que ele deite-se na maca. | La médecin lui demande de s'allonger sur la table d'examen.
a meditação | la méditation | Ele pratica meditação toda manhã. | Il pratique la méditation chaque matin. | pl=meditações
a morte | la mort | Depois da morte do pai ele mudou-se. | Après la mort de son père, il a déménagé.
a nuca | la nuque | Estou com frio na nuca: onde está o meu cachecol? | J'ai froid à la nuque : où est mon écharpe ?
a operação | l'opération | A operação correu bem. | L'opération s'est bien passée. | pl=operações
o paciente | le patient | O paciente espera a sua vez. | Le patient attend son tour.
a palma | la paume | Ponha a palma da mão sobre a mesa. | Posez la paume de la main sur la table.
a palma da mão | la paume | Ele segura a bola na palma da mão. | Il tient le ballon dans la paume de sa main. | pl=palmas da mão
o peito | la poitrine | Respire fundo e estufe o peito. | Respirez profondément et bombez la poitrine.
o perfume | le parfum | O teu perfume tem um cheiro muito bom. | Ton parfum sent très bon.
o peso | le poids | Perdi peso este ano. | J'ai perdu du poids cette année.
o plano de saúde | l'assurance maladie | O meu seguro-saúde paga os custos. | Mon assurance maladie prend en charge les frais. | pl=planos de saúde | ex?
o queixo | le menton | Levante um pouco o queixo. | Levez un peu le menton.
a respiração | la respiration | A respiração lenta ajuda a dormir. | La respiration lente aide à dormir. | pl=respirações
a seringa | la seringue | A enfermeira prepara a seringa. | L'infirmière prépare la seringue.
o sintoma | le symptôme | O primeiro sintoma foi a febre. | Le premier symptôme a été la fièvre.
a sobrancelha | le sourcil | O meu irmão tem sobrancelhas muito grossas. | Mon frère a les sourcils très fournis.
a tensão | la tension | Sinto tensão nos ombros. | Je sens de la tension dans les épaules. | pl=tensões
a testa | le front | Ele está com a testa quente: acho que está com febre. | Il a le front chaud : je crois qu'il a de la fièvre.
a tontura | le vertige | A tontura não dura muito. | Le vertige ne dure pas longtemps. | g?
o tornozelo | la cheville | No futebol eu torci o tornozelo. | Au foot, je me suis foulé la cheville.
o traseiro | le derrière, les fesses | Caí sentado e o meu traseiro dói. | Je suis tombé assis et j'ai mal au derrière.
o tratamento | le traitement | O tratamento dura duas semanas. | Le traitement dure deux semaines.
o umbigo | le nombril | Com essa t-shirt curta dá para ver o umbigo dela. | Avec ce t-shirt court, on voit son nombril.
a unha | l'ongle | A unha dela quebrou. | Son ongle s'est cassé.
a urgência | l'urgence | A urgência só foi percebida tarde. | L'urgence n'a été reconnue que tardivement.
a vacina | le vaccin | Tomei a vacina ontem. | On m'a fait le vaccin hier.
o xarope | le sirop | Tome o xarope depois de comer. | Prends le sirop après le repas.
""",
"roupa_a2_pt": """
a aparência | l'allure, l'apparence | Ele está com boa aparência hoje. | Il a bonne mine aujourd'hui.
a barba | la barbe | Ele deixou a barba crescer no inverno. | Il s'est laissé pousser la barbe en hiver.
o bigode | la moustache | O pai dele tem bigode. | Son père a une moustache.
o bolso | la poche | Levo as chaves no bolso. | J'ai les clés dans la poche.
o botão | le bouton | Caiu um botão da camisa. | Un bouton de la chemise est tombé. | pl=botões
a capa de chuva | l'imperméable | A capa de chuva mantém-me seco. | L'imperméable me garde au sec. | g? | pl=capas de chuva
o colar | le collier | Dei um colar de prata a ela. | Je lui ai offert un collier en argent.
a estatura | la taille (d'une personne) | Ele é de estatura média. | Il est de taille moyenne.
o estilo | le style | Ela tem um estilo muito pessoal. | Elle a un style très personnel.
o fato de banho | le maillot de bain |  |  | pl=fatos de banho | ex=?
a gravata | la cravate | Não gosto de usar gravata. | Je n'aime pas porter de cravate.
a manga | la manche | Uma camisa de manga curta. | Une chemise à manches courtes.
a maquiagem | le maquillage | Ela não usa maquiagem. | Elle ne porte pas de maquillage.
a moda | la mode | Essa jaqueta está na moda. | Cette veste est à la mode.
o penteado | la coiffure | Gosto do teu penteado novo. | J'aime ta nouvelle coiffure.
a peça de roupa | le vêtement | É uma peça de inverno. | C'est un vêtement d'hiver. | pl=peças de roupa | ex?
o piercing | le piercing | A minha prima tem um piercing no nariz. | Ma cousine a un piercing au nez.
o pijama | le pyjama | O pijama é macio e quente. | Le pyjama est doux et chaud.
a pulseira | le bracelet | Ela usa uma pulseira no pulso. | Elle porte un bracelet au poignet.
o relógio de pulso | la montre | O meu relógio de pulso está adiantado cinco minutos. | Ma montre avance de cinq minutes. | pl=relógios de pulso
a roupa íntima | les sous-vêtements | Vou comprar roupa íntima nova. | J'achète de nouveaux sous-vêtements. | g? | pl=roupas íntimas
o roupão | le peignoir |  |  | pl=roupões | ex=?
a ruga | la ride | Ele tem algumas rugas ao redor dos olhos. | Il a quelques rides autour des yeux.
o salto | le talon | Não consigo andar de salto. | Je ne peux pas marcher en talons.
o sorriso | le sourire | Ela tem um sorriso lindo. | Elle a un sourire magnifique.
a tatuagem | le tatouage | O meu irmão tem uma tatuagem no braço. | Mon frère a un tatouage sur le bras.
o zíper | la fermeture éclair | O zíper está quebrado. | La fermeture éclair est cassée.
""",
"natureza_a2_pt": """
o anão | le nain | No jardim tem um anãozinho. | Il y a un petit nain dans le jardin. | pl=anões | ex?
o arco-íris | l'arc-en-ciel | O arco-íris é colorido. | L'arc-en-ciel est coloré. | g? | pl=arcos-íris
a baleia | la baleine | A baleia é o maior animal do mar. | La baleine est le plus grand animal de la mer. | g?
a borboleta | le papillon | A borboleta voa de flor em flor. | Le papillon vole de fleur en fleur. | g?
o burro | l'âne | O burro carrega as bolsas pesadas. | L'âne porte les sacs lourds.
a cachoeira | la cascade | A cachoeira faz muito barulho. | La cascade est très bruyante. | g?
o caracol | l'escargot | Depois da chuva há caracóis por toda parte. | Après la pluie, il y a des escargots partout. | g?
a caverna | la grotte | A caverna é escura e fria. | La grotte est sombre et froide. | g?
a colina | la colline | O vilarejo fica sobre uma colina. | Le village est sur une colline. | g?
a costa | la côte | As minhas costas estão a doer. | J'ai mal au dos.
o deserto | le désert | O deserto é enorme e silencioso. | Le désert est immense et silencieux.
o dragão | le dragon | No conto de fadas um cavaleiro luta contra um dragão. | Dans le conte, un chevalier combat un dragon. | pl=dragões
o efeito estufa | l'effet de serre | O efeito estufa aquece a Terra. | L'effet de serre réchauffe la Terre. | pl=efeitos estufas
a energia | l'énergie | A energia solar é mais limpa. | L'énergie solaire est plus propre.
a energia eólica | l'énergie éolienne | A energia eólica cresce rápido na Alemanha. | L'énergie éolienne se développe rapidement en Allemagne. | g? | pl=energias eólicas
a energia solar | l'énergie solaire | A energia solar está cada vez mais popular. | L'énergie solaire devient de plus en plus populaire. | g? | pl=energias solares
o esquilo | l'écureuil | O esquilo junta nozes. | L'écureuil ramasse des noix.
a formiga | la fourmi | As formigas carregam uma folha. | Les fourmis transportent une feuille.
a fumaça | la fumée | A fumaça espalhou-se pela cidade. | La fumée passait au-dessus de la ville. | g?
a gaivota | la mouette | As gaivotas voam em círculos sobre o porto. | Les mouettes tournent au-dessus du port.
o galho | la branche | Um pássaro pousa no galho. | Un oiseau se pose sur la branche.
o ganso | l'oie | No Natal tem ganso. | À Noël, il y a une oie.
a geleira | le glacier | A geleira está a derreter aos poucos. | Le glacier fond lentement. | g?
o golfinho | le dauphin | O golfinho pula para fora da água. | Le dauphin bondit hors de l'eau.
a grama | l'herbe | As crianças brincam na grama. | Les enfants jouent dans l'herbe.
o granizo | la grêle | O granizo danificou o carro. | La grêle a endommagé la voiture.
o incêndio | l'incendie | Houve um incêndio na floresta. | Il y a eu un incendie dans la forêt.
o lobo | le loup | Os lobos voltaram a viver nesta floresta. | Des loups vivent de nouveau dans cette forêt.
a margem | la rive | Na margem há muitos pássaros. | Beaucoup d'oiseaux sont assis sur la rive.
o monte | le mont, la colline | Há um monte de trabalho. | Il y a un tas de travail.
o ninho | le nid | Na árvore tem um ninho com quatro ovos. | Il y a un nid avec quatre œufs dans l'arbre.
o orvalho | la rosée | De manhã tem orvalho na grama. | La rosée est sur l'herbe le matin.
o ouriço | l'hérisson | O ouriço enrola-se. | Le hérisson se met en boule.
a paisagem | le paysage | A paisagem daqui é linda. | Le paysage d'ici est magnifique.
o papagaio | le perroquet | O papagaio sabe repetir palavras. | Le perroquet peut répéter des mots.
o planeta | la planète | O planeta aquece a cada ano. | La planète se réchauffe chaque année.
o plástico | le plastique | Evitamos o plástico descartável. | Nous évitons le plastique jetable.
a poluição | la pollution | A poluição do ar preocupa. | La pollution de l'air inquiète. | pl=poluições
o pombo | le pigeon, la colombe | Há muitos pombos sentados na praça. | Beaucoup de pigeons sont sur la place.
a previsão do tempo | bulletin météo | A previsão do tempo diz que vai chover. | Le bulletin météo prévoit de la pluie. | g? | pl=previsões do tempo
""",
"natureza_a2_pt_2": """
a proteção da natureza | la protection de la nature | A proteção da natureza é muito importante para mim. | La protection de la nature est très importante pour moi. | g? | pl=proteções da natureza
a ratazana | le rat | Havia uma ratazana no porão. | Il y avait un rat dans la cave.
o relvado | la pelouse | Fazemos um piquenique no relvado. | Nous faisons un pique-nique sur la pelouse.
a rosa | une rose (la fleur) | Ele dá rosas vermelhas para ela. | Il lui offre des roses rouges. | g?
o saco de lixo | le sac poubelle | Leve o saco de lixo para fora, por favor. | Sors le sac poubelle, s'il te plaît. | pl=sacos de lixo
o sapo | la grenouille | O sapo pula na água. | La grenouille saute dans l'eau.
a seca | la sécheresse | A seca durou o verão inteiro. | La sécheresse a duré tout l'été.
a semente | la graine | Plantamos umas sementes no jardim. | Nous plantons des graines dans le jardin.
a separação do lixo | tri des déchets | Aqui a separação do lixo é obrigatória. | Le tri des déchets est obligatoire chez nous. | g? | pl=separações do lixo
o tubarão | le requin | O tubarão nada no mar profundo. | Le requin nage dans les profondeurs de la mer. | pl=tubarões
o vale | la vallée | O vale é muito verde na primavera. | La vallée est très verte au printemps.
o vulcão | le volcan | O vulcão está calmo há anos. | Le volcan est calme depuis des années. | pl=vulcões
o zoológico | le zoo | No domingo vamos ao zoológico. | Dimanche, nous allons au zoo.
""",
"viagens_a2_pt": """
a agência | l'agence | Reservei em uma agência de viagens. | J'ai réservé dans une agence de voyages.
a alfândega | la douane | Na alfândega revistaram a minha mala. | À la douane ils ont fouillé ma valise.
o apartamento de temporada | la appartement de vacances | Alugamos um apartamento de temporada na praia. | Nous louons un appartement de vacances au bord de la mer. | pl=apartamentos de temporada
o aquecimento | le chauffage | O aquecimento não funciona. | Le chauffage ne fonctionne pas.
a areia | le sable | A areia está muito quente. | Le sable est très chaud.
a aterrissagem | l'atterrissage | O piloto anuncia a aterrissagem. | Le pilote annonce l'atterrissage.
a barraca | la tente | Na barraca, durmo num isolante térmico. | Dans la tente, je dors sur un tapis de sol.
o barulho | le bruit | Há muito barulho na rua. | Il y a beaucoup de bruit dans la rue.
o bilhete | le billet, l'entrée | Compramos os bilhetes pela internet. | Nous achetons les billets sur internet.
a bomba de gasolina | la station-service |  |  | pl=bombas de gasolina | ex=?
o camping | le camping | Dormimos em um camping perto do rio. | Nous dormons dans un camping près du fleuve.
o cartão-postal | la carte postale | Vou mandar-te um cartão-postal de Évora. | Je t'envoie une carte postale de Évora. | g? | pl=cartões-postais
o check-in | l'enregistrement | O check-in fecha uma hora antes. | L'enregistrement ferme une heure avant. | pl=checks-ins
a chegada | l'arrivée | A chegada está prevista para o meio-dia. | L'arrivée est prévue à midi.
a ciclovia | la piste cyclable | Em Lisboa a ciclovia muitas vezes é vermelha. | À Lisbonne, la piste cyclable est souvent rouge. | g?
o cofre | le coffre-fort | Guarde o passaporte no cofre. | Rangez le passeport dans le coffre-fort.
a concha | le coquillage | As crianças procuram conchas na praia. | Les enfants cherchent des coquillages sur la plage.
o controle alfandegário | le contrôle douanier | Estamos a esperar no controle alfandegário. | Nous attendons au contrôle douanier. | pl=controles alfandegários
o cruzamento | le carrefour | Vire à direita no cruzamento. | Tourne à droite au carrefour.
o câmbio | le change, la monnaie rendue | Onde posso fazer câmbio? | Où puis-je changer de l'argent ?
a decolagem | le décollage | A decolagem atrasa meia hora. | Le décollage est retardé d'une demi-heure.
o destino | la destination | O nosso destino é Coimbra. | Notre destination est Coimbra.
a direita | la droite | O banco fica à direita. | La banque est à droite.
a distância | la distance | Que distância há até o centro? | Quelle distance jusqu'au centre ?
o embarque | l'embarquement | O embarque começa em dez minutos. | L'embarquement commence dans dix minutes.
a escala | l'escale | O voo tem uma escala em Lisboa. | Le vol a une escale à Lisbonne.
a esquerda | la gauche | Vire à esquerda depois da ponte. | Tourne à gauche après le pont.
o estacionamento | la place de parking | O estacionamento está completamente lotado. | Le parking est complètement plein.
a estadia | le séjour | Tenha uma boa estadia. | Bon séjour.
a esteira | le tapis roulant | As malas saem pela esteira três. | Les valises sortent par le tapis trois.
a esteira de bagagens | le tapis à bagages | A minha mala já vai chegar na esteira. | Ma valise arrive bientôt au tapis à bagages. | pl=esteiras de bagagens | ex?
o estrangeiro | l'étranger | Temos muitos hóspedes estrangeiros. | Nous avons beaucoup d'hôtes étrangers.
a excursão | l'excursion | Fazemos uma excursão ao lago. | Nous faisons une excursion au lac. | pl=excursões
o exterior | l'étranger (pays) | O meu irmão mora no exterior há anos. | Mon frère vit à l'étranger depuis des années.
a fatura | la facture | Eu revisaria a fatura antes de pagar. | Moi, je vérifierais la facture avant de payer.
a fronteira | la frontière | Passamos a fronteira de manhã. | Nous passons la frontière le matin.
o guarda-sol | le parasol | Abra o guarda-sol, está muito sol. | Ouvre le parasol, il y a beaucoup de soleil. | pl=guardas-sóis
o guia | le guide (livre) | Comprei um guia da cidade. | J'ai acheté un guide de la ville.
a hospedagem | l'hébergement | A hospedagem está incluída. | L'hébergement est inclus.
a hospedeira de bordo | l'hôtesse de l'air | A comissária distribui as bebidas. | L'hôtesse distribue les boissons. | pl=hospedeiras de bordo | ex?
""",
"viagens_a2_pt_2": """
o hóspede | le client (d'un hôtel) | O hóspede do doze vai embora hoje. | Le client de la douze part aujourd'hui.
o ICE | l'ICE (train rapide allemand) | Com o ICE chego a Porto em quatro horas. | Avec l'ICE, je suis à Porto en quatre heures.
a informação | le renseignement | No balcão o senhor recebe informações. | Au guichet, vous obtiendrez un renseignement. | pl=informações
o isolante térmico | le tapis de sol | Na barraca, durmo num isolante térmico. | Dans la tente, je dors sur un tapis de sol. | pl=isolantes térmicos
o itinerário | l'itinéraire | O roteiro inclui três cidades. | L'itinéraire comprend trois villes. | ex?
a largada | le départ, le décollage | A largada está marcada para as dez horas. | Le départ est prévu pour dix heures. | g?
a lembrança | le souvenir | Tenho boas lembranças daquela época. | J'ai de beaux souvenirs de cette époque.
o leste | l'est | O sol nasce no leste. | Le soleil se lève à l'est.
a mapa da cidade | le plan de la ville | Sem mapa da cidade eu não acho o caminho. | Sans plan de la ville, je ne trouve pas le chemin. | g? | pl=mapas da cidade
o motor | le moteur | O motor está a fazer um barulho estranho. | Le moteur fait un bruit étrange.
a máquina de bilhetes | le distributeur de billets | A máquina de bilhetes fica embaixo, no saguão. | Le distributeur de billets se trouve en bas dans le hall. | g? | pl=máquinas de bilhetes
o navio | le bateau, le navire | O navio parte toda manhã. | Le bateau part tous les matins.
o norte | le nord | Moramos no norte do país. | Nous habitons dans le nord du pays.
o oeste | l'ouest | A costa oeste é muito bonita. | La côte ouest est très belle.
a onda | la vague | Hoje tem ondas grandes. | Aujourd'hui il y a de grandes vagues.
a passadeira | le passage piéton | Atravesse sempre na passadeira. | Traverse toujours au passage piéton.
o peão | le piéton | Os peões atravessam a rua. | Les piétons traversent la rue. | pl=peões
o piloto | le pilote | O piloto anuncia a aterrissagem. | Le pilote annonce l'atterrissage.
a placa | le panneau | Não vi a placa de pare. | Je n'ai pas vu le panneau stop.
o pneu | le pneu | O pneu furou de repente. | Le pneu est soudainement crevé.
o poste de luz | le réverbère | Há uma caixa de correio ao lado do poste. | Il y a une boîte aux lettres à côté du réverbère. | pl=postes de luz | ex?
o propósito | le but | Qual é o propósito da sua viagem? | Quel est le but de votre voyage ?
a pá | la pelle | Com a pá, ele faz um castelo de areia. | Avec la pelle, il fait un château de sable.
o quarto duplo | la chambre double | Gostaríamos de um quarto duplo. | Nous voudrions une chambre double. | pl=quartos duplos
o rececionista | le réceptionniste | O rececionista fala inglês. | Le réceptionniste parle anglais.
a receção | la réception | Deixe a chave na receção. | Laissez la clé à la réception. | pl=receções
a reclamação | la réclamation | Quero fazer uma reclamação. | Je veux faire une réclamation. | pl=reclamações
a retirada de bagagens | la livraison des bagages | A retirada de bagagens fica logo à direita. | La livraison des bagages est juste à droite. | g? | pl=retiradas de bagagens
a rota | l'itinéraire | Escolhemos a rota mais curta. | Nous choisissons l'itinéraire le plus court.
a rotatória | le rond-point | Pegue a segunda saída da rotatória. | Prends la deuxième sortie du rond-point.
a roupa de banho | le maillot de bain | Esqueci a roupa de banho em casa. | J'ai oublié le maillot à la maison. | pl=roupas de banho
a segurança | la sécurité | O controle de segurança é rápido. | Le contrôle de sécurité est rapide.
o seguro | l'assurance | O seguro cobre a bagagem. | L'assurance couvre les bagages.
o serviço | le service | O serviço é excelente. | Le service est excellent.
o sul | le sud | No sul faz mais calor. | Dans le sud il fait plus chaud.
o terminal | le terminal | Saímos do terminal dois. | Nous partons du terminal deux.
o turista | le touriste | Há muitos turistas em agosto. | Il y a beaucoup de touristes en août.
a visita guiada | la visite guidée, circuit | A visita guiada pelo centro histórico dura uma hora. | La visite de la vieille ville dure une heure. | g? | pl=visitas guiadas
a vista | la vue | O quarto tem vista para o mar. | La chambre a vue sur la mer.
o visto | le visa | Para este país precisamos de visto. | Nous avons besoin d'un visa pour ce pays.
o voo de conexão | le vol de correspondance | O nosso voo de conexão está atrasado. | Notre vol de correspondance a du retard. | pl=voos de conexão
""",
"cidade_a2_pt": """
a agência bancária | l'agence bancaire | A agência abre às oito e meia. | L'agence ouvre à huit heures et demie. | pl=agências bancárias | ex?
o arranha-céu | le gratte-ciel | O arranha-céu tem quarenta andares. | Le gratte-ciel a quarante étages. | g? | pl=arranhas-céus
o bairro residencial | le quartier résidentiel | O bairro residencial é ótimo para famílias. | Le quartier résidentiel est très adapté aux familles. | pl=bairros residenciais
a banca | le kiosque | Na banca eu compro um jornal. | J'achète un journal au kiosque.
o bloco | le bloc, l'immeuble | Ela mora no bloco em frente. | Elle habite dans l'immeuble d'en face.
o calçadão | la zone piétonne | O calçadão está sempre cheio de gente. | La zone piétonne est toujours pleine de monde. | pl=calçadões
a carteira | la carte, le permis | A minha carteira está quase vazia. | Mon porte-monnaie est presque vide.
o castelo | le château, la serrure | O castelo está aberto para visitantes. | Le château est ouvert aux visiteurs.
o documento | le document | Traga todos os documentos. | Apportez tous les documents.
o empréstimo | le prêt | Pedimos um empréstimo ao banco. | Nous demandons un prêt à la banque.
a entrada | l'entrée | A entrada fica do outro lado. | L'entrée est de l'autre côté. | g?
o envelope | l'enveloppe | Coloque a carta no envelope. | Mets la lettre dans l'enveloppe.
o envio | l'envoi | O envio leva três dias. | L'envoi prend trois jours.
o formulário | le formulaire | Preencha o formulário, por favor. | Remplissez le formulaire, s'il vous plaît.
o guichê | le guichet | Vá ao guichê número quatro. | Allez au guichet numéro quatre.
o imposto | l'impôt | Os impostos sobem todo ano. | Les impôts augmentent chaque année.
o juro | l'intérêt | O juro é muito baixo. | L'intérêt est très bas.
a loja de departamentos | le grand magasin | A loja de departamentos tem cinco andares. | Le grand magasin a cinq étages. | g? | pl=lojas de departamentos
o lugar | le lieu, l'endroit | É um lugar tranquilo para ler. | C'est un endroit tranquille pour lire.
o meio | le milieu, centre | O hotel fica no meio da cidade. | L'hôtel se trouve au centre de la ville.
o multibanco | le distributeur | Saco dinheiro no multibanco. | Je retire de l'argent au distributeur.
o pacote | le colis | A operadora oferece pacotes de viagem baratos. | Le voyagiste propose des voyages organisés à prix abordable.
a parada | l'arrêt, l'appui | O Autocarro não faz parada aqui. | L'autobus ne s'arrête pas ici. | g?
a poupança | l'épargne | Todo mês ponho dinheiro na poupança. | Je mets de l'argent sur mon compte épargne chaque mois.
o prazo | le délai, l'échéance | O prazo termina em trinta de junho. | Le délai se termine le trente juin.
o selo | le timbre | Preciso de dois selos para o Canadá. | J'ai besoin de deux timbres pour le Canada.
a taxa | les frais | O banco cobra uma taxa. | La banque prélève des frais.
o trâmite | la démarche | É um trâmite muito lento. | C'est une démarche très lente.
""",
"escola_a2_pt": """
a admissão | l'admission | A sua admissão foi confirmada. | Son admission a été confirmée. | pl=admissões
a aluna | l'élève (fille) | Ela é a melhor aluna da turma. | Elle est la meilleure élève de la classe. | g?
o anfiteatro | l'amphithéâtre | O auditório está lotado hoje. | L'amphithéâtre est plein aujourd'hui. | ex?
a anotação | la note | Faço uma anotação. | Je prends une note. | pl=anotações
as anotações | les notes de cours | Reviso as anotações antes da prova. | Je révise mes notes avant l'examen.
a apostila | polycopié | A apostila ajuda-me a estudar. | Le polycopié m'aide à étudier. | g?
a bolsa de estudos | la bourse | Ele conseguiu uma bolsa para estudar fora. | Il a obtenu une bourse pour étudier ailleurs. | pl=bolsas de estudos | ex?
o conhecimento | la connaissance | Ele tem bons conhecimentos de espanhol. | Il a de bonnes connaissances en espagnol.
o diploma | le diplôme | Ele tem diploma de engenheiro. | Il a un diplôme d'ingénieur.
a dúvida | le doute, la question | Se tiver dúvidas, pergunte. | Si tu as des doutes, demande.
o esforço | l'effort | Aprender uma língua exige esforço. | Apprendre une langue demande des efforts.
o estojo | la trousse | O meu estojo está cheio de canetas. | Ma trousse est pleine de stylos.
o estágio | le stage | Ela está a fazer estágio numa empresa. | Elle fait un stage dans une entreprise.
o globo | le globe | No globo, procuramos o Canadá. | Sur le globe, nous cherchons le Canada.
a história | l'histoire | História é a minha matéria preferida. | L'histoire est ma matière préférée. | g?
o jardim de infância | le jardin d'enfants | A minha filha vai ao jardim de infância. | Ma fille va au jardin d'enfants. | pl=jardins de infância
o livro didático | le manuel scolaire | O livro didático está em cima da mesa. | Le manuel scolaire est sur la table. | pl=livros didáticos
a matrícula | l'inscription | A matrícula custa mil euros. | L'inscription coûte mille euros.
o mestrado | le master | Ele faz mestrado em história. | Il fait un master d'histoire.
a palestra | la conférence | A palestra começa às cinco. | La conférence commence à cinq heures.
o papelzinho | le bout de papier, mot | No papelzinho está o número de telefone. | Le numéro de téléphone est sur le bout de papier.
a pesquisa | la recherche | Ela trabalha em uma pesquisa sobre o clima. | Il travaille sur une recherche sur le climat.
a prática | la pratique, le stage | A bolsa é muito prática. | Le sac est très pratique.
o restaurante universitário | la cafétéria universitaire |  |  | g? | pl=restaurantes universitários | ex=?
o resultado | le résultat | Os resultados saem na sexta. | Les résultats sortent vendredi.
a sala de aula | la salle de cours | A sala de aula fica no primeiro andar. | La salle est au premier étage. | pl=salas de aula
o tema | le sujet, thème | O tema de hoje é o meio ambiente. | Le sujet d'aujourd'hui, c'est l'environnement.
a teoria | la théorie | A teoria é mais fácil que a prática. | La théorie est plus facile que la pratique.
o texto | le texte | Lê o texto mais uma vez. | Relis le texte.
""",
"cultura_a2_pt": """
o anjo | l'ange | Na árvore tem um anjinho. | Un petit ange est posé sur l'arbre. | ex?
o ator | l'acteur | O ator fala cinco idiomas. | L'acteur parle cinq langues.
o balão | le ballon de baudruche | Depois da festa há balões por toda parte. | Après la fête, il y a des ballons partout. | pl=balões
a banda | le groupe (de musique) | A banda dela toca no sábado. | Son groupe joue samedi. | g?
a bexiga | le ballon de baudruche | Depois da festa tem bexiga por todo lado. | Après la fête, il y a des ballons partout. | g?
a bilheteria | le guichet | Compramos na bilheteria. | Nous achetons au guichet.
o brinde | le toast | Fizemos um brinde aos noivos. | Nous avons porté un toast aux mariés.
a bruxa | la sorcière | A criança está fantasiada de bruxa. | L'enfant est déguisé en sorcière. | g?
a caminhada | la randonnée | Com tempo bom eu planejaria uma caminhada. | S'il faisait beau, je prévoirais une randonnée. | g?
o carnaval | le carnaval | O carnaval dura vários dias. | Le carnaval dure plusieurs jours.
o cartaz | l'affiche | No cartaz está a data. | La date est indiquée sur l'affiche.
a celebração | la célébration | A celebração dura três dias. | La célébration dure trois jours. | pl=celebrações
a cena | la scène | A última cena é linda. | La dernière scène est magnifique.
a charada | l'énigme, jeu de devinettes | A minha avó resolve uma charada por dia. | Ma grand-mère fait une grille chaque jour.
o circo | le cirque | O circo só fica uma semana na cidade. | Le cirque n'est en ville qu'une semaine.
o clube | le club | O meu filho está num clube de xadrez. | Mon fils fait partie d'un club d'échecs.
a comédia | la comédie | Vimos uma comédia muito engraçada. | Nous avons vu une comédie très drôle.
o convidado | l'invité | Hoje temos dez convidados. | Nous avons dix invités aujourd'hui.
o coral | le chœur | O coral canta na igreja. | La chorale chante dans l'église.
a corda | la corde | Uma corda arrebentou. | Une corde s'est cassée.
o desenho | le dessin | O desenho mostra uma paisagem. | Le dessin représente un paysage.
o desfile | le défilé | O desfile passa pela avenida. | Le défilé passe par l'avenue.
o Dia das Mães | la fête des mères | No Dia das Mães eu dou flores para a minha mãe. | À la fête des mères, j'offre des fleurs à ma mère. | pl=Dias das Mães
o Dia dos Pais | la fête des pères | No Dia dos Pais os pais costumam sair. | À la fête des pères, les pères sortent souvent. | pl=Dias dos Pais
o diretor | le réalisateur | O diretor ganhou um prémio. | Le réalisateur a gagné un prix.
o disco | le disque, l'album | Quando jovem, eu gastava tudo em discos. | Jeune, je dépensais tout en disques.
o entusiasmo | l'enthousiasme, l'espoir | Ela falou da viagem com muito entusiasmo. | Elle a parlé de son voyage avec beaucoup d'enthousiasme.
o esboço | l'esquisse | O esboço ainda não está pronto. | L'esquisse n'est pas encore terminée.
o escritor | l'écrivain | O escritor faz uma leitura hoje à noite. | L'écrivain fait une lecture ce soir.
a escultura | la sculpture | A escultura está na praça. | La sculpture est sur la place.
o estojo de violão | l'étui à guitare | O estojo do violão está aberto. | L'étui à guitare est ouvert. | pl=estojos de violão | ex?
a estreia | la sortie, la première | A estreia é na sexta. | La sortie est vendredi.
o estresse | le stress | O estresse tira-me o sono. | Le stress m'empêche de dormir.
a exposição | l'exposition | A exposição fecha em junho. | L'exposition ferme en juin. | pl=exposições
a fantasia | le déguisement | Estou a usar uma fantasia de pirata. | Je porte un déguisement de pirate.
a feira | la foire | A feira dura uma semana. | La foire dure une semaine.
o festival | le festival | Em julho tem um festival grande. | En juillet, il y a un grand festival.
o filme ou livro policial | le polar |  |  | pl=filmes ous livros policiais | ex=?
a galeria | la galerie | Visitamos uma galeria pequena. | Nous visitons une petite galerie.
o género | le genre | O meu género favorito é a comédia. | Mon genre préféré est la comédie.
""",
"cultura_a2_pt_2": """
o interesse | l'intérêt | Ela tem muito interesse por música. | Elle a un grand intérêt pour la musique. | g?
o jogo de tabuleiro | le jeu de société |  |  | pl=jogos de tabuleiro | ex=?
a legenda | le sous-titre | Vejo os filmes com legendas. | Je regarde les films avec sous-titres.
a letra | les paroles, la lettre | Ninguém consegue ler a letra dele. | Personne ne peut lire son écriture.
a lágrima | la larme | Uma lágrima caiu na carta. | Une larme est tombée sur la lettre.
a obra | l'œuvre | É a obra mais famosa do museu. | C'est l'œuvre la plus connue du musée.
o orgulho | la fierté | Ele fala da filha com orgulho. | Il parle de sa fille avec fierté.
a orquestra | l'orchestre | A orquestra toca hoje à noite. | L'orchestre joue ce soir.
o personagem | le personnage | O personagem principal é uma menina. | Le personnage principal est une fille.
a pintura | la peinture | A pintura é do século dezessete. | La peinture est du dix-septième siècle.
o poema | le poème | Decorei um poema. | J'ai appris un poème par cœur.
o presente de natal | le cadeau de Noël | Abrimos o presente de Natal de manhã. | Nous ouvrons le cadeau de Noël le matin. | pl=presentes de natal
a procissão | la procession | A procissão sai às oito. | La procession sort à huit heures. | pl=procissões
o prémio | le prix | Ele recebeu um prémio importante. | Il a reçu un prix important.
o público | le public | O público aplaudiu muito. | Le public a beaucoup applaudi.
a quebra-cabeça | le puzzle | O quebra-cabeça tem mil peças. | Le puzzle a mille pièces. | g? | pl=quebras-cabeças
o quiz | le quiz, jeu de questions | Às sextas tem um quiz na televisão. | Le vendredi, il y a un quiz à la télévision.
o riso | le rire | O riso dela alegrava a casa toda. | Son rire égayait toute la maison.
o ritmo | le rythme | Este ritmo é muito contagiante. | Ce rythme est très entraînant.
o romance | le roman | Estou a ler um romance longo. | Je lis un long roman.
o roteiro | le scénario | O roteiro é muito original. | Le scénario est très original.
o réveillon | le réveillon du nouvel an | No réveillon comemos doze uvas. | Au réveillon nous mangeons douze raisins.
a sessão | la séance | A sessão das dez está lotada. | La séance de dix heures est pleine. | pl=sessões
a surpresa | la surprise | Foi uma surpresa muito agradável. | Ce fut une très agréable surprise.
o tambor | le tambour | O menino toca tambor na festa. | L'enfant joue du tambour à la fête.
o trabalho manual | le bricolage | As crianças adoram este trabalho manual. | Ce bricolage amuse les enfants. | pl=trabalhos manuais
a tradição | la tradition | É uma tradição muito antiga. | C'est une tradition très ancienne. | pl=tradições
a vergonha | la honte, la gêne | Tenho vergonha de falar em público. | J'ai honte de parler en public.
o violino | le violon | O violino soa lindamente. | Le violon sonne magnifiquement.
a véspera de ano-novo | le réveillon du Nouvel An | No réveillon comemos doze uvas. | Au réveillon nous mangeons douze raisins. | pl=vésperas de ano-novo | ex?
o ânimo | le moral | A notícia esfria o ânimo da equipa. | La nouvelle atténue l'enthousiasme dans l'équipe.
""",
"desporto_a2_pt": """
o basquetebol | le basket-ball | Ele joga basquetebol há anos. | Il joue au basket-ball depuis des années. | g?
a bolsa de desporto | le sac de sport | A minha bolsa de desporto está no carro. | Mon sac de sport est dans la voiture. | pl=bolsas de desporto
o campeonato | le championnat | O campeonato começa em março. | Le championnat commence en mars.
o campo de desportos | le terrain de sport | O campo de desportos fica atrás da escola. | Le terrain de sport est derrière l'école. | pl=campos de desportos
o campo de futebol | le terrain de football | O campo de futebol está molhado. | Le terrain de football est mouillé. | pl=campos de futebol
a corrida de fundo | la course de fond | Participo de uma corrida de longa distância. | Je participe à une course de fond. | pl=corridas de fundo | ex?
o handebol | l'handball | O handebol é muito popular na Alemanha. | Le handball est très populaire en Allemagne.
a medalha | la médaille | Ele ganhou uma medalha de ouro. | Il a gagné une médaille d'or.
a paixão | la passion, les supporters | A sua paixão é o ciclismo. | Sa passion est le cyclisme. | pl=paixões
o torneio | le tournoi | Ela está a treinar para um torneio de ténis. | Elle s'entraîne pour un tournoi de tennis.
o treinador | l'entraîneur | O treinador destacou o desempenho da equipa. | L'entraîneur mettait en avant la performance de l'équipe.
o voleibol | le volley-ball |  |  | g? | ex=?
o árbitro | l'arbitre | O árbitro apita o fim do jogo. | L'arbitre siffle la fin.
""",
"media_a2_pt": """
o anúncio | la publicité | Há anúncios demais. | Il y a trop de publicités.
o aparelho | l'appareil | O aparelho não funciona mais. | L'appareil ne fonctionne plus.
o arquivo | le fichier | O arquivo é pesado demais. | Le fichier est trop lourd.
o artigo | l'article | Li um artigo interessante. | J'ai lu un article intéressant.
o auscultadores | le casque audio | Escuto música com os auscultadores. | J'écoute de la musique avec mon casque. | pl=auscultadores
a bateria | la batterie | A minha bateria está a acabar. | Ma batterie est presque vide.
o cabo | le câble | O cabo é curto demais. | Le câble est trop court.
a caixa de som | le haut-parleur | A caixa de som está ao lado dos livros. | Le haut-parleur est à côté des livres. | pl=caixas de som
o canal | la chaîne | Mude de canal, por favor. | Change de chaîne, s'il te plaît.
a capa | la une, la couverture | A notícia saiu na capa. | La nouvelle est sortie à la une.
o carregador | le chargeur | Esqueci o meu carregador. | J'ai oublié mon chargeur.
a chamada | l'appel | Tenho uma chamada perdida. | J'ai un appel manqué.
a conexão | la connexion | A conexão está muito lenta. | La connexion est très lente. | pl=conexões
o conselho | le conseil | Preciso do teu conselho. | J'ai besoin de ton conseil.
a conversa | la conversation | Tivemos uma conversa longa. | Nous avons eu une longue conversation.
o dado | la donnée | Preencha os seus dados pessoais. | Remplissez vos données personnelles.
o debate | le débat | O debate durou duas horas. | Le débat a duré deux heures.
o destinatário | le destinataire | O destinatário não mora mais aqui. | Le destinataire n'habite plus ici.
o e-book | le livre électronique | Nas férias eu prefiro ler um e-book. | En vacances, je préfère lire un livre électronique. | g? | pl=es-books
o exemplo | l'exemple | Dê-me um exemplo, por favor. | Donne-moi un exemple, s'il te plaît.
a explicação | l'explication | Preciso de uma explicação. | J'ai besoin d'une explication. | pl=explicações
a fonte | la source | Ele não citou a fonte do dado. | Il n'a pas cité la source de la donnée.
o gesto | le geste | Entendi pelo gesto dele. | Je l'ai compris à son geste.
a imprensa | la presse | A imprensa fala do assunto. | La presse parle du sujet.
o incidente | le fait divers | O incidente aconteceu de madrugada. | L'incident s'est produit à l'aube.
a ligação | l'appel téléphonique | Recebi uma ligação importante. | J'ai reçu un appel important. | pl=ligações
o link | le lien | Clica no link do e-mail. | Clique sur le lien dans le courriel.
o mal-entendido | le malentendu | Foi só um mal-entendido. | Ce n'était qu'un malentendu. | pl=mais-entendidos
a manchete | le titre | A manchete ocupa a página inteira. | Le titre occupe toute la page.
a máquina fotográfica | l'appareil photo | Leva a máquina fotográfica! | Emporte l'appareil photo ! | g? | pl=máquinas fotográficas
a notícia | la nouvelle | Tenho uma boa notícia. | J'ai une bonne nouvelle.
a opinião | l'opinion | Qual é a tua opinião? | Quelle est ton opinion ? | pl=opiniões
a palavra-passe | le mot de passe | Esqueci a minha palavra-passe. | J'ai oublié mon mot de passe. | pl=palavras-passes
a pasta | le dossier | Salve a foto nessa pasta. | Range la photo dans ce dossier.
o portátil | l'ordinateur portable | Trabalho com o portátil no comboio. | Je travaille sur l'ordinateur portable dans le train. | pl=portáteis
o programa | l'émission | É o meu programa favorito. | C'est mon émission préférée.
a programação | le programme | A programação da nova temporada é mais ousada. | La programmation de la nouvelle saison est plus audacieuse. | pl=programações
a publicidade | la publicité | A publicidade influencia muito. | La publicité influence beaucoup.
a página | la page | A página não carrega. | La page ne charge pas.
a rede | le réseau | Não há rede no subsolo. | Il n'y a pas de réseau au sous-sol.
a reportagem | le reportage | Vimos uma reportagem sobre o clima. | Nous avons vu un reportage sur le climat.
o resumo | le résumé | Escreva um resumo da lição. | Écris un résumé de la leçon.
o silêncio | le silence | Houve um silêncio constrangedor. | Il y a eu un silence gênant.
o site | le site web | Este site carrega muito rápido. | Ce site web se charge très vite.
o sotaque | l'accent | Ele tem sotaque do sul. | Il a l'accent du sud.
o tablet | la tablette | As crianças estudam com o tablet. | Les enfants apprennent avec la tablette.
o teclado | le clavier | O teclado espanhol tem o ñ. | Le clavier espagnol a le ñ.
a tradução | la traduction | A tradução não é exata. | La traduction n'est pas exacte. | pl=traduções
o utilizador | l'utilisateur | Digite o teu nome de utilizador. | Écris ton nom d'utilisateur.
a voz | la voix | Ele fala em voz baixa. | Il parle à voix basse.
o wi-fi | wifi | O wi-fi não funciona aqui. | Le wifi ne fonctionne pas ici. | g? | pl=wis-fis
""",
"dinheiro_a2_pt": """
o atendimento | le service | O atendimento deste hotel é excelente. | Le service dans cet hôtel est excellent.
o carrinho de compras | le caddie | Para o carrinho de compras, preciso de uma moeda. | Pour le caddie, il me faut une pièce. | pl=carrinhos de compras
o centavo | le centime | Custa noventa centavos. | Ça coûte quatre-vingt-dix centimes.
o cheque | le chèque | Pagaram-me com um cheque. | On m'a payé par chèque.
a conta bancária | le compte bancaire | O dinheiro já está na minha conta. | L'argent est déjà sur mon compte. | pl=contas bancárias | ex?
a conta poupança | le compte épargne | Todo mês ponho dinheiro na poupança. | Je mets de l'argent sur mon compte épargne chaque mois. | g? | pl=contas poupanças | ex?
a conta à ordem | le compte courant | O meu salário cai na conta à ordem. | Mon salaire est versé sur le compte courant. | pl=contas às ordens
o cupom fiscal | le ticket de caisse | Guarda bem a nota. | Garde bien le ticket de caisse. | g? | pl=cupons fiscais | ex?
a dívida | la dette | Ele pagou toda a dívida. | Il a payé toute la dette.
a feira de antiguidades | le marché aux puces |  |  | pl=feiras de antiguidades | ex=?
o folheto | le prospectus, brochure | No folheto estão todas as ofertas. | Toutes les offres sont dans le prospectus.
o ganho | le gain, le bénéfice | Ganho vinte por cento de desconto. | J'obtiens vingt pour cent de rabais.
o gasto | la dépense | Os gastos sobem todo mês. | Les dépenses augmentent chaque mois.
o holerite | la fiche de paie | O holerite chega no dia trinta. | La fiche de paie arrive le trente.
a máquina automática | le distributeur automatique | Compro o bilhete na máquina. | J'achète le billet au distributeur. | pl=máquinas automáticas | ex?
o ouro | l'or | O anel é de ouro. | La bague est en or.
a perda | la perte | Foi uma perda importante. | Ce fut une perte importante.
o porta-moedas | le porte-monnaie | O meu porta-moedas ficou no Autocarro. | Mon porte-monnaie est resté dans le bus. | g? | pl=portas-moedas
a prata | l'argent (métal) | A corrente é de prata. | La chaîne est en argent. | g?
o produto | le produit | Este produto é muito barato. | Ce produit est très bon marché.
a troca | l'échange (achat) | A troca é possível em até catorze dias. | L'échange est possible dans les quatorze jours. | g?
""",
"sentimentos_a2_pt": """
o alívio | le soulagement | O alívio veio na hora. | Le soulagement est arrivé immédiatement.
a atitude | l'attitude | A atitude dele mudou depois. | Son attitude a changé ensuite.
o caráter | le caractère | Ele tem um temperamento forte. | Il a un caractère fort. | ex?
a confiança | la confiance | Tenho muita confiança nela. | J'ai beaucoup confiance en elle.
a confusão | la confusion | A confusão dela era compreensível. | Sa confusion était compréhensible. | g? | pl=confusões
a curiosidade | la curiosité | A curiosidade dela a leva a toda parte. | Sa curiosité l'emmène partout. | g?
o defeito | le défaut | Todos temos algum defeito. | Nous avons tous un défaut.
a despedida | l'adieu, le départ | A despedida foi difícil para ela. | Les adieux lui ont été difficiles. | g?
o humor | l'humeur, l'humour | Hoje ele está de mau humor. | Aujourd'hui il est de mauvaise humeur.
a mentira | le mensonge | Nunca vou perdoar essa mentira dele. | Je ne lui pardonnerai jamais ce mensonge.
o nervosismo | nervosité | O nervosismo dele era visível. | Sa nervosité était perceptible.
a paciência | la patience | É preciso de ter paciência. | Il faut avoir de la patience.
a personalidade | la personnalité | Gosto muito da personalidade dela. | Sa personnalité me plaît beaucoup.
a satisfação | la satisfaction | Sinto uma grande satisfação. | Je ressens une grande satisfaction. | g? | pl=satisfações
o tédio | l'ennui | O tédio deixa-me cansado. | L'ennui me fatigue.
o vontade | l'envie | Ele tem muita força de vontade. | Il a beaucoup de volonté. | g?
""",
"sociedade_a2_pt": """
o alemão | l'Allemand, Allemande | Muitos alemães vão para a Itália no verão. | Beaucoup d'Allemands vont en Italie l'été. | pl=alemães
o austríaco | l'Autrichien | O meu colega é austríaco. | Mon collègue est autrichien.
a bandeira | le drapeau | Em frente da câmara municipal tremula uma bandeira. | Un drapeau flotte devant l'hôtel de ville.
o candidato | le candidat | O candidato conversa com os cidadãos. | Le candidat parle avec les citoyens.
a capital | la capitale | Lisboa é a capital da Alemanha. | Lisbonne est la capitale de l'Allemagne. | g?
o cartão de cidadão | la carte d'identité | Por favor, mostre-me o seu documento. | Montrez-moi votre carte d'identité, s'il vous plaît. | pl=cartões de cidadão | ex?
a democracia | la démocratie | A Alemanha é uma democracia. | L'Allemagne est une démocratie.
o Deus | le dieu | Ela acredita em Deus. | Elle croit en Dieu. | g? | pl=Deus
a eleição | l'élection | A eleição é em setembro. | L'élection a lieu en septembre. | g? | pl=eleições
o europeu | l'Européen | Como europeu, eu não preciso de visto. | En tant qu'Européen, je n'ai pas besoin de visa. | g?
a guerra | la guerre | A guerra durou quatro anos. | La guerre a duré quatre ans. | g?
o luxemburguês | le Luxembourgeois | Muitos luxemburgueses falam três línguas. | Beaucoup de Luxembourgeois parlent trois langues. | g? | pl=luxemburgueses
o ministro | le ministre | O ministro faz um discurso importante. | Le ministre prononce un discours important.
o ordem | l'ordre | Ele recusou-se a cumprir a ordem. | Il a refusé d'obéir à l'ordre. | g?
o parlamento | le parlement | O parlamento discute a lei nova. | Le parlement discute de la nouvelle loi.
o partido | le parti politique | Este partido ganha muitos votos. | Ce parti gagne beaucoup de voix.
a permissão | l'autorisation, permission | Sem permissão de trabalho ele não pode trabalhar. | Sans permis de travail, il n'a pas le droit de travailler. | g? | pl=permissões
a rainha | la reine | A rainha faz um discurso. | La reine prononce un discours. | g?
o rei | le roi | O rei morava neste castelo. | Le roi habitait dans ce château.
a Suíça | la Suisse | No verão vamos para a Suíça. | Cet été, nous allons en Suisse. | g?
o suíço | le Suisse (habitant) | O meu vizinho é suíço. | Mon voisin est suisse.
a terra natal | le pays d'origine | A minha terra natal é um vilarejo pequeno. | Mon pays d'origine est un petit village. | pl=terras natais
a votação | le vote | A votação termina às dezoito horas. | Le vote se termine à dix-huit heures. | g? | pl=votações
""",
"lei_a2_pt": """
o acidente | l'accident | Houve um acidente na estrada. | Il y a eu un accident sur la route.
o alarme | l'alarme | O alarme tocou de noite. | L'alarme a sonné la nuit.
a ambulância | l'ambulance | A ambulância chegou em cinco minutos. | L'ambulance est arrivée en cinq minutes.
o bombeiro | le pompier | Os bombeiros apagaram o incêndio. | Les pompiers ont éteint l'incendie.
o capacete | le casque | Use capacete na moto. | Porte un casque à moto.
a esquadra | le commissariat | A esquadra fica na avenida. | Le commissariat est sur l'avenue.
o ladrão | le voleur | O ladrão entrou pela janela. | Le voleur est entré par la fenêtre. | pl=ladrões
a multa | l'amende | Levei uma multa por estacionar mal. | J'ai eu une amende pour stationnement.
o perigo | le danger | Não há perigo. | Il n'y a pas de danger.
a polícia | la police | Chamamos a polícia. | Nous appelons la police.
a queixa | la plainte | Eu registraria queixa do roubo agora mesmo. | Moi, je porterais plainte pour le vol tout de suite.
o roubo | le vol | Registramos o roubo ontem. | Nous avons déclaré le vol hier.
a testemunha | le témoin | Há duas testemunhas do acidente. | Il y a deux témoins de l'accident.
""",
"tempo_a2_pt": """
o fim | la fin | No fim do filme ela chorou. | À la fin du film, elle a pleuré.
o futuro | l'avenir | Ninguém conhece o futuro. | Personne ne connaît l'avenir.
o passado | passé | Ele raramente fala do passado. | Il parle rarement du passé.
a quinze minutos | le quart d'heure | Volto em quinze minutos. | Je reviens dans quinze minutes. | g? | pl=quinzes minutos
""",
"quotidiano_a2_pt": """
o agradecimento | le remerciement | Ele merece o agradecimento de todos. | Les remerciements de tous lui reviennent.
a atenção | l'attention | Ele perde a atenção em dez minutos. | Il perd l'attention au bout de dix minutes. | pl=atenções
o caso | le cas | Em caso de acidente, chama-se a polícia. | En cas d'accident, on appelle la police.
a chance | la chance, l'occasion | Eu daria outra chance a ele. | Moi, je lui donnerais une autre chance.
o cilindro | le cylindre | O cilindro rola da mesa. | Le cylindre roule et tombe de la table.
o cubo | le cube | O cubo tem seis lados. | Le cube a six faces.
a culpa | la faute | A culpa não é tua. | Ce n'est pas de ta faute.
o cumprimento | la salutation | Cumprimento os meus vizinhos toda manhã. | Je salue mes voisins chaque matin.
a dica | l'astuce, conseil | Obrigado pela boa dica! | Merci pour ce bon conseil ! | g?
a dúzia | la douzaine | Uma dúzia de ovos. | Une douzaine d'œufs.
a esfera | la sphère | A esfera é perfeitamente redonda. | La sphère est parfaitement ronde. | g?
o esforço físico | l'effort physique | O esforço físico o cansa. | L'effort physique le fatigue. | pl=esforços físicos
a falha | la défaillance | Foi uma falha do sistema. | C'était une défaillance du système.
a fatia | la tranche | Ponha duas fatias de queijo. | Mets deux tranches de fromage.
a fileira | la rangée, file | Sentamos na primeira fileira. | Nous nous sommes assis au premier rang.
o litro | le litre | Compro dois litros de leite. | J'achète deux litres de lait.
o motivo | la raison | Não há motivo para preocupação. | Il n'y a aucune raison de s'inquiéter.
o movimento | le mouvement | Ele fez um movimento brusco. | Il a fait un mouvement brusque.
a noção | l'idée, notion | Na época ninguém tinha noção do alcance desta decisão. | La portée de cette décision n'était claire pour personne à l'époque. | pl=noções
o objetivo | le but, objectif | O meu objetivo é a prova em junho. | Mon objectif, c'est l'examen de juin.
o oval | l'ovale | O oval parece um ovo. | L'ovale ressemble à un œuf.
a pane | la panne | O carro deu pane na autoestrada. | Nous sommes tombés en panne sur l'autoroute.
o passo | le pas | Dê um passo para trás. | Fais un pas en arrière.
a pirâmide | la pyramide | A pirâmide fica no meio do deserto. | La pyramide se dresse au milieu du désert. | g?
o por cento | pourcent | Só dez por cento responderam. | Seuls dix pour cent ont répondu. | pl=pores centos
a postura | la posture | Essa postura é ruim para as costas. | Cette posture est mauvaise pour le dos.
o pote | le pot, le bocal | Sobrou meio pote de compota. | Il reste un demi-pot de confiture.
o problema | le problème | Temos um problema com o carro. | Nous avons un problème avec la voiture.
o quilo | le kilo | Um quilo de tomates, por favor. | Un kilo de tomates, s'il vous plaît.
a regra | la règle | Esta regra vale para todos. | Cette règle vaut pour tout le monde.
o resto | le reste |  |  | ex=?
o retângulo | le rectangle | O retângulo tem o dobro do comprimento da largura. | Le rectangle est deux fois plus long que large.
o risco | le risque | Não quero correr esse risco. | Je ne veux pas prendre ce risque.
o senhor | le monsieur | Bom dia, senhor Meier! | Bonjour, monsieur Meier !
a situação | la situation | Nesta situação eu não sei o que fazer. | Dans cette situation, je ne sais plus quoi faire. | pl=situações
a solução | la solution | Buscamos uma solução rápida. | Nous cherchons une solution rapide. | pl=soluções
a soma | la somme | A soma de todos os números é cem. | La somme de tous les nombres est cent. | g?
a tentativa | la tentative | Ele conseguiu na terceira tentativa. | Il a réussi au troisième essai.
o terço | le tiers | Um terço da turma faltou hoje. | Un tiers de la classe est absent aujourd'hui.
o verso | le dos, le verso | A resposta está no verso. | La réponse est au verso.
""",
}
