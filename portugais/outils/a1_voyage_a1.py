# -*- coding: utf-8 -*-
"""L'A1 voyage du portugais, a Lisbonne : 12 escales, 2 etapes « installe »,
la suite en 8 etapes. Meme format que anglais/outils/a1_voyage_a1.py (le
moteur : chargerA1Voyage, preparerA1Voyage). SOURCE : on corrige ici, puis
python portugais/outils/construire.py.

- « mots » NOMME des mots du corpus A1 portugais (nom sans article, infinitif,
  expression) : construire.py ecarte et signale ceux qui n'y sont pas.
- « blocs » : « phrase avec … | sens avec … | 3 mots portugais | leurs 3 sens » ;
  l'exemple prend le 3e mot.
- « dialogue » : « eux|moi | replique | sens ».
"""

ESCALES = [
{"id": "arriver", "pour": "tous", "icone": "🛬", "s": "Arriver à Lisbonne et s'installer à l'hôtel",
 "scenes": ["flughafen", "hotel"],
 "mots": "aeroporto, avião, voo, mala de viagem, bagagem, bilhete, passageiro, hotel, quarto, chave, elevador, reserva, nome, apelido, país, nacionalidade, táxi, cama, toalha, duche, almofada, noite, chegar, reservar, ficar, Olá!, Boa noite!",
 "tableau": {"t": "Arriver : chegar",
  "l": "eu chego a Lisboa | j'arrive à Lisbonne\ntu chegas tarde | tu arrives tard\nele · ela chega hoje | il · elle arrive aujourd'hui\nnós chegamos ao aeroporto | nous arrivons à l'aéroport\neles chegam de avião | ils arrivent en avion\no meu voo chega às seis | mon vol arrive à six heures",
  "a": "Chegar a : arriver à (chegar a Lisboa, chegar ao hotel). Le portugais n'a qu'une préposition là où le français hésite entre à et en."},
 "blocs": """Tenho uma reserva em nome de … . | J'ai une réservation au nom de … . | Silva / Martin / Tremblay | Silva / Martin / Tremblay
Queria um quarto para … . | Je voudrais une chambre pour … . | uma noite / duas noites / uma semana | une nuit / deux nuits / une semaine
Onde é … , por favor? | Où est … , s'il vous plaît ? | o elevador / a saída / a paragem de táxis | l'ascenseur / la sortie / la station de taxis
Pode dar-me … ? | Pouvez-vous me donner … ? | uma toalha / outra almofada / a palavra-passe do wi-fi | une serviette / un autre oreiller / le mot de passe du wifi""",
 "dialogue": {"t": "À la réception de l'hôtel", "l": """eux | Boa noite, bem-vindo! Tem reserva? | Bonsoir, bienvenue ! Vous avez une réservation ?
moi | Sim, tenho uma reserva em nome de Tremblay. | Oui, j'ai une réservation au nom de Tremblay.
eux | Muito bem. Pode mostrar-me o passaporte? | Très bien. Pouvez-vous me montrer votre passeport ?
moi | Aqui está. A que horas é o pequeno-almoço? | Voici. À quelle heure est le petit-déjeuner ?
eux | Das sete às dez. Aqui está a chave, quarto 412. | De sept à dix heures. Voici la clé, chambre 412.
moi | Muito obrigado! | Merci beaucoup !"""}},

{"id": "manger", "pour": "tous", "icone": "🍽️", "s": "Manger : la pastelaria, le restaurant",
 "scenes": ["fruehstueck", "restaurant"],
 "mots": "pequeno-almoço, almoço, jantar, café, bica, galão, chá, água, sumo, leite, pão, ovo, sandes, sopa, salada, bacalhau, sardinha, pastel de nata, sobremesa, ementa, conta, gorjeta, empregado de mesa, mesa, copo, prato, comer, beber, pedir, Queria…, Bom apetite!",
 "tableau": {"t": "Vouloir poliment : queria",
  "l": "queria um café | je voudrais un café\nqueres água? | tu veux de l'eau ?\nele queria a sopa | il voudrait la soupe\nqueríamos uma mesa para dois | nous voudrions une table pour deux\neles queriam a conta | ils voudraient l'addition\nnão quero sobremesa | je ne veux pas de dessert",
  "a": "Queria (imparfait de querer) est la forme polie de tous les jours. Pour commander : Para mim, o bacalhau (pour moi, la morue). Le pain et les olives posés sur la table se paient s'ils sont entamés."},
 "blocs": """Queria … , se faz favor. | Je voudrais … , s'il vous plaît. | uma bica / um sumo de laranja / um copo de água | un expresso / un jus d'orange / un verre d'eau
Uma mesa para … , por favor. | Une table pour … , s'il vous plaît. | dois / quatro / uma pessoa | deux / quatre / une personne
Para mim, … . | Pour moi, … . | a sopa / a salada / o bacalhau | la soupe / la salade / la morue
Pode trazer … ? | Pouvez-vous apporter … ? | a ementa / a conta / mais pão | la carte / l'addition / encore du pain""",
 "dialogue": {"t": "Au restaurant", "l": """eux | Boa tarde! Já escolheram? | Bonjour ! Vous avez choisi ?
moi | Sim. Para mim, a sopa e o bacalhau, por favor. | Oui. Pour moi, la soupe et la morue, s'il vous plaît.
eux | Muito bem. E para beber? | Très bien. Et comme boisson ?
moi | Um copo de vinho branco, se faz favor. | Un verre de vin blanc, s'il vous plaît.
eux | Aqui está. Bom apetite! | Voilà. Bon appétit !
moi | Obrigado! A conta, se faz favor. | Merci ! L'addition, s'il vous plaît."""}},

{"id": "marche", "pour": "tous", "icone": "🍎", "s": "Le marché et la boulangerie",
 "scenes": ["markt-obst-heimisch", "baeckerei"],
 "mots": "mercado, fruta, maçã, banana, laranja, limão, morango, legume, batata, tomate, cebola, pão, bolo, padaria, saco, preço, dinheiro, comprar, pagar, Quanto custa?",
 "tableau": {"t": "Acheter : comprar, pagar",
  "l": "eu compro maçãs | j'achète des pommes\ntu pagas em dinheiro | tu paies en espèces\nela compra pão todos os dias | elle achète du pain tous les jours\nnós pagamos com cartão | nous payons par carte\nquanto custa? | combien ça coûte ?\nquanto custam? | combien coûtent-ils ?",
  "a": "Quanto custa? pour une chose, Quanto custam? pour plusieurs. Au marché, on achète au kilo (um quilo) ou à la pièce. Le prix : 2,50 € se dit dois euros e cinquenta."},
 "blocs": """Queria … , por favor. | Je voudrais … , s'il vous plaît. | um quilo de maçãs / seis ovos / um pão | un kilo de pommes / six œufs / un pain
Quanto custam … ? | Combien coûtent … ? | os morangos / os tomates / as laranjas | les fraises / les tomates / les oranges
Posso pagar … ? | Je peux payer … ? | com cartão / em dinheiro / com o telemóvel | par carte / en espèces / avec mon portable""",
 "dialogue": {"t": "Au marché", "l": """eux | Bom dia! O que vai ser? | Bonjour ! Qu'est-ce que ce sera ?
moi | Bom dia! Quanto custam os morangos? | Bonjour ! Combien coûtent les fraises ?
eux | Três euros a caixa. Estão muito doces. | Trois euros la barquette. Elles sont très sucrées.
moi | Então levo duas caixas. | Alors j'en prends deux barquettes.
eux | São seis euros. Mais alguma coisa? | Ça fait six euros. Autre chose ?
moi | Não, é tudo, obrigado. | Non, c'est tout, merci."""}},

{"id": "ville", "pour": "tous", "icone": "🗺️", "s": "En ville : trouver son chemin",
 "scenes": ["stadtplatz", "park"],
 "mots": "cidade, rua, praça, avenida, bairro, esquina, ponte, castelo, rio, museu, igreja, banco, mapa, semáforo, passadeira, virar, atravessar, procurar, encontrar, Desculpe.",
 "tableau": {"t": "Où se trouve… ? : ficar, haver",
  "l": "onde fica o castelo? | où se trouve le château ?\nhá um banco aqui perto? | y a-t-il une banque près d'ici ?\nhá um parque à esquerda | il y a un parc à gauche\nvire à direita na esquina | tournez à droite au coin\nsiga sempre em frente | continuez tout droit\nfica a dez minutos | c'est à dix minutes",
  "a": "Ficar pour situer un lieu (fica ali), haver pour dire qu'il y en a un (há uma farmácia). Lisbonne monte et descend : a subir (en montant), a descer (en descendant)."},
 "blocs": """Desculpe, onde fica … ? | Excusez-moi, où se trouve … ? | o castelo / a estação de metro / a Praça do Comércio | le château / la station de métro / la place du Commerce
Há … aqui perto? | Y a-t-il … près d'ici ? | um banco / uma farmácia / uma casa de banho | une banque / une pharmacie / des toilettes
É … ? | C'est … ? | longe / perto / à esquerda | loin / près / à gauche""",
 "dialogue": {"t": "Demander son chemin", "l": """moi | Desculpe, onde fica o castelo? | Excusez-moi, où se trouve le château ?
eux | Siga sempre em frente e vire à esquerda na igreja. | Continuez tout droit et tournez à gauche à l'église.
moi | É longe? | C'est loin ?
eux | Não, são dez minutos a pé, mas é sempre a subir. | Non, c'est à dix minutes à pied, mais ça monte tout le temps.
moi | Muito obrigada! | Merci beaucoup !
eux | De nada. Bom passeio! | De rien. Bonne promenade !"""}},

{"id": "transports", "pour": "tous", "icone": "🚋", "s": "Se déplacer : le métro, l'elétrico, le comboio",
 "scenes": ["kreuzung", "ubahn"],
 "mots": "metro, autocarro, elétrico, comboio, táxi, barco, estação, paragem, bilhete, viagem, atraso, apanhar, sair, ir, voltar, chegar",
 "tableau": {"t": "Prendre : apanhar",
  "l": "apanho o metro | je prends le métro\napanhas o elétrico? | tu prends le tram ?\nela apanha o comboio às oito | elle prend le train à huit heures\nnós apanhamos o barco | nous prenons le bateau\neles apanham um táxi | ils prennent un taxi\nsaio na próxima paragem | je descends au prochain arrêt",
  "a": "Au Portugal, apanhar (attraper) un transport ; au Brésil, pegar. Ir de : ir de metro, ir de comboio ; mais ir a pé, à pied."},
 "blocs": """Um bilhete para … , por favor. | Un billet pour … , s'il vous plaît. | Sintra / Cascais / o Porto | Sintra / Cascais / Porto
Este autocarro vai para … ? | Ce bus va à … ? | Belém / o aeroporto / o centro | Belém / l'aéroport / le centre
A que horas parte … ? | À quelle heure part … ? | o comboio / o barco / o último metro | le train / le bateau / le dernier métro""",
 "dialogue": {"t": "Au guichet de la gare", "l": """moi | Bom dia. Um bilhete para Sintra, por favor. | Bonjour. Un billet pour Sintra, s'il vous plaît.
eux | Só ida ou ida e volta? | Aller simple ou aller-retour ?
moi | Ida e volta. A que horas parte o próximo comboio? | Aller-retour. À quelle heure part le prochain train ?
eux | Às dez e um quarto, na linha três. | À dix heures et quart, voie trois.
moi | Obrigado! | Merci !"""}},

{"id": "achats", "pour": "tous", "icone": "🛍️", "s": "Les achats : vêtements, tailles, prix",
 "scenes": ["kleidergeschaeft", "supermarkt"],
 "mots": "loja, roupa, camisa, t-shirt, calças, saia, vestido, casaco, camisola, sapato, tamanho, cor, preço, saldos, provador, saco, cartão, caro, barato, comprar, trocar, Quanto custa?",
 "tableau": {"t": "Ce, cette : este, esta, esse",
  "l": "este casaco é bonito | cette veste est jolie\nesta camisa é cara | cette chemise est chère\nestes sapatos são confortáveis | ces chaussures sont confortables\nessa saia fica-te bem | cette jupe te va bien\nposso experimentar? | je peux essayer ?\nlevo esta | je prends celle-ci",
  "a": "Este pour ce qui est près de moi, esse pour ce qui est près de toi, aquele pour ce qui est loin des deux. Ficar bem : aller bien (un vêtement)."},
 "blocs": """Posso experimentar … ? | Je peux essayer … ? | este casaco / estas calças / aquela camisa | cette veste / ce pantalon / cette chemise-là
Tem … ? | Vous l'avez … ? | noutra cor / num tamanho maior / em azul | dans une autre couleur / en plus grand / en bleu
É … demais. | C'est trop … . | grande / pequeno / caro | grand / petit / cher""",
 "dialogue": {"t": "Dans un magasin de vêtements", "l": """eux | Boa tarde. Posso ajudar? | Bonjour. Je peux vous aider ?
moi | Sim, quanto custa este casaco? | Oui, combien coûte cette veste ?
eux | Sessenta euros. Está em saldos. | Soixante euros. Elle est en soldes.
moi | Posso experimentar? | Je peux l'essayer ?
eux | Claro, o provador é ali. | Bien sûr, la cabine est là-bas.
moi | Fica-me bem. Levo este! | Elle me va bien. Je la prends !"""}},

{"id": "sante", "pour": "tous", "icone": "💊", "s": "La santé : pharmacie, médecin",
 "scenes": ["apotheke", "arztpraxis"],
 "mots": "farmácia, médico, hospital, centro de saúde, cabeça, barriga, costas, febre, constipação, gripe, dor, medicamento, comprimido, receita, consulta, doente, doer",
 "tableau": {"t": "Avoir mal : doer",
  "l": "dói-me a cabeça | j'ai mal à la tête\ndói-te a barriga? | tu as mal au ventre ?\ndói-lhe o pé | il a mal au pied\ndoem-me as costas | j'ai mal au dos\ntenho febre | j'ai de la fièvre\nestou constipado | je suis enrhumé",
  "a": "Doer se construit comme gostar en français familier : la partie du corps est le sujet, et le verbe s'accorde avec elle (dói-me o pé, doem-me os pés)."},
 "blocs": """Dói-me … . | J'ai mal … . | a cabeça / a garganta / o estômago | à la tête / à la gorge / à l'estomac
Tem alguma coisa para … ? | Vous avez quelque chose pour … ? | a tosse / a febre / as dores de cabeça | la toux / la fièvre / les maux de tête
Queria marcar … . | Je voudrais prendre … . | uma consulta / uma consulta para hoje / uma consulta com a médica | un rendez-vous / un rendez-vous pour aujourd'hui / un rendez-vous avec la médecin""",
 "dialogue": {"t": "À la pharmacie", "l": """eux | Bom dia, diga. | Bonjour, je vous écoute.
moi | Bom dia. Estou constipada e dói-me a garganta. | Bonjour. Je suis enrhumée et j'ai mal à la gorge.
eux | Tem febre? | Vous avez de la fièvre ?
moi | Não, só tosse. | Non, juste de la toux.
eux | Tome isto, um comprimido três vezes por dia. | Prenez ceci, un comprimé trois fois par jour.
moi | Precisa de receita? | Il faut une ordonnance ?
eux | Não, não precisa. | Non, ce n'est pas nécessaire."""}},

{"id": "imprevus", "pour": "tous", "icone": "🧳", "s": "Les imprévus : perdre, attendre, réparer",
 "scenes": ["fahrradwerkstatt", "buergeramt"],
 "mots": "mala de viagem, chave, telemóvel, dinheiro, cartão, atraso, bicicleta, perder, esperar, procurar, encontrar, ajudar, Peço desculpa.",
 "tableau": {"t": "Le passé : perdi, esqueci",
  "l": "perdi a chave | j'ai perdu la clé\nesqueci-me do telemóvel | j'ai oublié mon portable\nalguém encontrou uma mala? | quelqu'un a trouvé une valise ?\no comboio chegou atrasado | le train est arrivé en retard\nesperei uma hora | j'ai attendu une heure\npode ajudar-me? | pouvez-vous m'aider ?",
  "a": "Le perfeito pour ce qui vient d'arriver : perdi (j'ai perdu), esqueci-me (j'ai oublié, avec le pronom après le verbe)."},
 "blocs": """Perdi … . | J'ai perdu … . | a chave / o passaporte / o cartão | la clé / le passeport / la carte
Esqueci-me … . | J'ai oublié … . | do telemóvel / da mala / do guarda-chuva | mon portable / mon sac / mon parapluie
Pode … , por favor? | Pouvez-vous … , s'il vous plaît ? | ajudar-me / telefonar / esperar | m'aider / téléphoner / attendre""",
 "dialogue": {"t": "Aux objets trouvés", "l": """moi | Boa tarde. Perdi a minha mala no elétrico. | Bonjour. J'ai perdu mon sac dans le tram.
eux | De que cor é? | De quelle couleur est-il ?
moi | É preta, pequena. | Il est noir, petit.
eux | Um momento… É esta? | Un instant… C'est celui-ci ?
moi | Sim! Muito obrigada! | Oui ! Merci beaucoup !"""}},

{"id": "services", "pour": "tous", "icone": "🧺", "s": "Les services : laverie, coiffeur, banque",
 "scenes": ["waschsalon", "friseur"],
 "mots": "roupa, banco, dinheiro, moeda, cartão, cabelo, lavar, pagar, mudar, esperar",
 "tableau": {"t": "Pouvoir : poder",
  "l": "posso pagar com cartão? | je peux payer par carte ?\npodes ajudar-me? | tu peux m'aider ?\npode cortar curto | vous pouvez couper court\npodemos esperar | nous pouvons attendre\nnão podem entrar | ils ne peuvent pas entrer\nonde posso lavar a roupa? | où puis-je laver mes vêtements ?",
  "a": "Poder : posso, podes, pode. Pode… ? (avec o senhor, a senhora sous-entendus) est la façon polie de demander un service."},
 "blocs": """Queria … , por favor. | Je voudrais … , s'il vous plaît. | cortar o cabelo / lavar a roupa / trocar dinheiro | me faire couper les cheveux / laver mon linge / changer de l'argent
Pode … ? | Vous pouvez … ? | cortar um pouco / esperar um momento / dar-me moedas | couper un peu / attendre un instant / me donner des pièces""",
 "dialogue": {"t": "Chez le coiffeur", "l": """eux | Bom dia! Tem marcação? | Bonjour ! Vous avez un rendez-vous ?
moi | Não. Pode cortar-me o cabelo agora? | Non. Pouvez-vous me couper les cheveux maintenant ?
eux | Pode esperar dez minutos? | Vous pouvez attendre dix minutes ?
moi | Posso, claro. | Oui, bien sûr.
eux | Como quer? | Comment le voulez-vous ?
moi | Só um pouco mais curto, por favor. | Juste un peu plus court, s'il vous plaît."""}},

{"id": "rencontrer", "pour": "tous", "icone": "🤝", "s": "Rencontrer des gens, être invité",
 "scenes": ["familie", "geburtstag"],
 "mots": "amigo, vizinho, família, nome, idade, profissão, país, festa, aniversário, presente, falar, conhecer, apresentar, Muito prazer., Parabéns!",
 "tableau": {"t": "Se présenter : ser, ter, morar",
  "l": "sou canadiano | je suis canadien\ntenho trinta anos | j'ai trente ans\nmoro em Lisboa há um ano | j'habite à Lisbonne depuis un an\ntrabalho num banco | je travaille dans une banque\nfalo francês e um pouco de português | je parle français et un peu portugais\napresento-te a minha mulher | je te présente ma femme",
  "a": "L'âge se dit avec ter : tenho trinta anos. Há + durée : depuis (moro aqui há um ano). Entre jeunes et amis, on passe vite au tu."},
 "blocs": """Apresento-te … . | Je te présente … . | a minha mulher / o meu irmão / a minha colega | ma femme / mon frère / ma collègue
Moro em Lisboa há … . | J'habite à Lisbonne depuis … . | um ano / seis meses / duas semanas | un an / six mois / deux semaines
Obrigado pelo … ! | Merci pour le … ! | jantar / convite / presente | dîner / l'invitation / le cadeau""",
 "dialogue": {"t": "Chez des amis", "l": """eux | Olá! Entra, entra. Esta é a minha mulher, a Teresa. | Salut ! Entre, entre. Voici ma femme, Teresa.
moi | Muito prazer, Teresa. | Enchanté, Teresa.
eux | O prazer é meu. De onde és? | Tout le plaisir est pour moi. D'où viens-tu ?
moi | Sou de Montreal, mas moro em Lisboa há um ano. | Je suis de Montréal, mais j'habite à Lisbonne depuis un an.
eux | E gostas de Lisboa? | Et tu aimes Lisbonne ?
moi | Adoro! | J'adore !"""}},

{"id": "plage", "pour": "voyage", "icone": "🏖️", "s": "La plage et le temps qu'il fait",
 "scenes": ["strand", "camping"],
 "mots": "praia, sol, calor, chuva, vento, nuvem, tempo, verão, temperatura, óculos de sol, nadar, Está bem.",
 "tableau": {"t": "Il fait… : estar, fazer",
  "l": "está sol | il fait soleil\nestá calor · está frio | il fait chaud · il fait froid\nestá vento | il y a du vent\nestá a chover | il pleut\nfaz bom tempo | il fait beau\nestão trinta graus | il fait trente degrés",
  "a": "Estar pour le temps qu'il fait en ce moment (está calor), fazer dans quelques tournures (faz bom tempo). L'Atlantique est froid, même en été : a água está fria !"},
 "blocs": """Hoje está … . | Aujourd'hui, il fait … . | calor / sol / vento | chaud / soleil / du vent
Vamos … ? | On va … ? | à praia / nadar / apanhar sol | à la plage / nager / bronzer""",
 "dialogue": {"t": "À la plage de Cascais", "l": """moi | Que calor! A água está boa? | Quelle chaleur ! L'eau est bonne ?
eux | Está fria, é o Atlântico! | Elle est froide, c'est l'Atlantique !
moi | Vamos nadar na mesma? | On va nager quand même ?
eux | Vamos! | Allons-y !"""}},

{"id": "visiter", "pour": "voyage", "icone": "🏛️", "s": "Visiter : musées, belvédères, horaires",
 "scenes": ["museum", "bibliothek"],
 "mots": "museu, castelo, igreja, bilhete, hora, horário, segunda-feira, domingo, abrir, fechar, visitar, Que horas são?",
 "tableau": {"t": "Ouvrir, fermer : abrir, fechar",
  "l": "o museu abre às dez | le musée ouvre à dix heures\nfecha às seis | il ferme à six heures\nestá fechado à segunda-feira | il est fermé le lundi\no bilhete custa dez euros | le billet coûte dix euros\nhá desconto para estudantes? | y a-t-il une réduction pour les étudiants ?\na entrada é grátis ao domingo | l'entrée est gratuite le dimanche",
  "a": "À + heure : às dez (a + as). À segunda-feira : le lundi (chaque lundi). Beaucoup de musées de Lisbonne ferment le lundi."},
 "blocs": """A que horas … ? | À quelle heure … ? | abre o museu / fecha o castelo / começa a visita | ouvre le musée / ferme le château / commence la visite
Queria … bilhetes, por favor. | Je voudrais … billets, s'il vous plaît. | dois / três / quatro | deux / trois / quatre""",
 "dialogue": {"t": "À l'entrée du musée", "l": """moi | Boa tarde. Dois bilhetes, por favor. | Bonjour. Deux billets, s'il vous plaît.
eux | São vinte euros. Há desconto para estudantes. | Ça fait vingt euros. Il y a une réduction pour les étudiants.
moi | Sou estudante! A que horas fecha? | Je suis étudiant ! À quelle heure fermez-vous ?
eux | Às seis. Boa visita! | À six heures. Bonne visite !"""}},
]

INSTALLE = [
{"id": "logement", "pour": "installe", "icone": "🏠", "s": "Le logement : chercher, louer, les voisins",
 "scenes": ["umzug", "wohnzimmer"],
 "mots": "casa, apartamento, quarto, cozinha, sala, casa de banho, varanda, andar, elevador, vizinho, chave, contrato, morar, mudar",
 "tableau": {"t": "Il y a, il n'y a pas : há, não há",
  "l": "há duas divisões | il y a deux pièces\nhá varanda? | il y a un balcon ?\nnão há elevador | il n'y a pas d'ascenseur\no apartamento tem cozinha | l'appartement a une cuisine\nfica no terceiro andar | c'est au troisième étage\nquanto é a renda? | combien est le loyer ?",
  "a": "Au Portugal, on décrit un logement par le nombre de chambres : um T2 = deux chambres et un salon. Le loyer : a renda."},
 "blocs": """O apartamento tem … ? | L'appartement a … ? | varanda / elevador / garagem | un balcon / un ascenseur / un garage
Fica no … andar. | C'est au … étage. | primeiro / segundo / último | premier / deuxième / dernier""",
 "dialogue": {"t": "Visiter un appartement", "l": """moi | Bom dia. Venho ver o apartamento. | Bonjour. Je viens voir l'appartement.
eux | Entre. Tem dois quartos e uma varanda. | Entrez. Il a deux chambres et un balcon.
moi | Há elevador? | Il y a un ascenseur ?
eux | Não há, mas é só o segundo andar. | Non, mais ce n'est que le deuxième étage.
moi | E quanto é a renda? | Et combien est le loyer ?"""}},

{"id": "demarches", "pour": "installe", "icone": "🏛️", "s": "Les démarches : mairie, formulaires",
 "scenes": ["buergeramt", "buero"],
 "mots": "nome, apelido, morada, telefone, e-mail, assinatura, nacionalidade, data, pergunta, resposta, escrever, assinar, soletrar, Pode repetir?",
 "tableau": {"t": "Les questions du guichet",
  "l": "qual é o seu nome? | quel est votre nom ?\nqual é o seu apelido? | quel est votre nom de famille ?\nqual é a sua morada? | quelle est votre adresse ?\npode soletrar? | pouvez-vous épeler ?\nassine aqui, por favor | signez ici, s'il vous plaît\ntem o número de contribuinte? | vous avez votre numéro fiscal ?",
  "a": "Au guichet, on vous dit o senhor, a senhora, et le possessif devient o seu, a sua (votre). Le número de contribuinte (NIF) est demandé partout au Portugal."},
 "blocs": """O meu … é … . | Mon … est … . | apelido é Martin / nome é Paul / e-mail é paul@exemplo.pt | nom de famille est Martin / prénom est Paul / courriel est paul@exemplo.pt""",
 "dialogue": {"t": "Au guichet de la mairie", "l": """eux | Bom dia. Qual é o seu apelido? | Bonjour. Quel est votre nom de famille ?
moi | Tremblay. | Tremblay.
eux | Pode soletrar, por favor? | Pouvez-vous épeler, s'il vous plaît ?
moi | T-R-E-M-B-L-A-Y. | T-R-E-M-B-L-A-Y.
eux | Obrigado. Assine aqui, por favor. | Merci. Signez ici, s'il vous plaît."""}},
]

SUITE = [
 {"id": "famille", "icone": "👨‍👩‍👧", "s": "La famille et les proches", "scene": "familie", "themes": ["familia_pt", "apresentar_pt"],
  "tableau": {"t": "Avoir : ter",
   "l": "tenho um irmão | j'ai un frère\ntens filhos? | tu as des enfants ?\nela tem uma família grande | elle a une grande famille\ntemos um cão | nous avons un chien\neles têm três netos | ils ont trois petits-enfants\nnão tenho irmãs | je n'ai pas de sœurs",
   "a": "Têm (ils ont) prend un accent ; tem (il a) n'en a pas. La négation se place devant le verbe : não tenho."}},
 {"id": "maison", "icone": "🛏️", "s": "La maison et la chambre", "scene": "schlafzimmer", "themes": ["casa_pt"],
  "tableau": {"t": "Où sont les choses : em cima de, debaixo de",
   "l": "as chaves estão em cima da mesa | les clés sont sur la table\no gato está debaixo da cama | le chat est sous le lit\na roupa está no armário | les vêtements sont dans l'armoire\no candeeiro está ao lado do sofá | la lampe est à côté du canapé\no jardim fica atrás da casa | le jardin est derrière la maison\nhá um quadro na parede | il y a un tableau au mur",
   "a": "De se soude à l'article : em cima da mesa (de + a), ao lado do sofá (de + o). Em aussi : no armário, na parede."}},
 {"id": "cuisine", "icone": "🍳", "s": "Manger et cuisiner", "scene": "kueche", "themes": ["comida_pt", "cafe_pt"],
  "tableau": {"t": "Du, de la : pas d'article",
   "l": "como pão ao pequeno-almoço | je mange du pain au petit-déjeuner\nhá leite? | il y a du lait ?\nnão há açúcar | il n'y a pas de sucre\nprecisamos de ovos | il nous faut des œufs\nnão como carne | je ne mange pas de viande\nquanto açúcar? quantos ovos? | combien de sucre ? combien d'œufs ?",
   "a": "Le portugais n'a pas de partitif : comer pão, beber água. Quanto pour ce qui ne se compte pas, quantos (quantas) pour ce qui se compte."}},
 {"id": "travail", "icone": "💼", "s": "Le travail et le bureau", "scene": "buero", "themes": ["trabalho_pt"],
  "tableau": {"t": "Ce que je fais : trabalhar, ser",
   "l": "trabalho num escritório | je travaille dans un bureau\nsou professor | je suis professeur\nela é enfermeira | elle est infirmière\ncomeço às nove | je commence à neuf heures\nacabo às seis | je finis à six heures\ntenho uma reunião | j'ai une réunion",
   "a": "Le métier sans article après ser : sou professor (je suis professeur). Num, numa : dans un, dans une (em + um)."}},
 {"id": "ecole", "icone": "📚", "s": "L'école et les études", "scene": "klassenzimmer", "themes": ["escola_pt"],
  "tableau": {"t": "Étudier, apprendre : estudar, aprender",
   "l": "estudo português | j'étudie le portugais\naprendes depressa | tu apprends vite\no professor explica bem | le professeur explique bien\nnão percebo esta palavra | je ne comprends pas ce mot\ntemos exame na sexta | nous avons un examen vendredi\nescreve no caderno | écris dans le cahier",
   "a": "Perceber : comprendre (au Portugal) ; entender existe aussi. Escreve ! (écris !) : l'impératif de tu a la forme de ele."}},
 {"id": "loisirs", "icone": "⚽", "s": "Les loisirs et le sport", "scene": "sportplatz", "themes": ["lazer_pt", "animais_pt"],
  "tableau": {"t": "Aimer : gostar de",
   "l": "gosto de futebol | j'aime le football\ngostas de nadar? | tu aimes nager ?\nela gosta muito de fado | elle aime beaucoup le fado\nnão gostamos de correr | nous n'aimons pas courir\neles adoram o mar | ils adorent la mer\njogo ténis ao sábado | je joue au tennis le samedi",
   "a": "Gostar se construit toujours avec de : gosto de música, gosto do Benfica (de + o). Jogar pour un sport, brincar pour les jeux d'enfants."}},
 {"id": "corps", "icone": "🩺", "s": "Le corps et la santé", "scene": "untersuchung", "themes": ["corpo_pt", "roupa_pt"],
  "tableau": {"t": "Avoir mal : doer",
   "l": "dói-me a cabeça | j'ai mal à la tête\ndoem-me os pés | j'ai mal aux pieds\ntenho febre | j'ai de la fièvre\nestou constipado | je suis enrhumé\nsinto-me melhor | je me sens mieux\nvisto o casaco | je mets ma veste",
   "a": "Doer s'accorde avec la partie du corps : dói-me o braço, doem-me os braços. Vestir : mettre, porter un vêtement."}},
 {"id": "societe", "icone": "📱", "s": "La ville, le temps, le quotidien", "scene": "musik", "themes": ["cidade_pt", "tempo_pt", "clima_pt", "compras_pt", "transportes_pt", "dia_pt", "numeros_pt", "formas_pt"],
  "tableau": {"t": "Le futur proche : ir + infinitif",
   "l": "vou trabalhar amanhã | je vais travailler demain\nvais sair hoje? | tu vas sortir aujourd'hui ?\nvai chover | il va pleuvoir\nvamos jantar fora | nous allons dîner dehors\nvão chegar tarde | ils vont arriver tard\nno sábado vou a Sintra | samedi, je vais à Sintra",
   "a": "Ir + infinitif est le futur de la conversation. Le futur simple (trabalharei) sonne écrit."}},
]
