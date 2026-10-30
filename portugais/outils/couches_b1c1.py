# -*- coding: utf-8 -*-
"""Les couches B1, B2 et C1 des scenes en portugais du Portugal, ECRITES pour
le portugais sur les faits de l'image (memes zones f et reperes r que
l'allemand, memes faits que ses couches). SOURCE : on corrige ici, puis

    python portugais/outils/couches_b1c1.py

qui les verse dans portugais/scenes/<scene>.json (sans toucher a la couche A2).
Les mots sont ceux de la table du socle (portugais/outils/scenes.py, MOTS).

Une ligne : « f | r | question | bonne | fausse / fausse | phrase | sens | note ».
Le portugais n'a pas les cas de l'allemand : ou la couche allemande enseigne
le datif ou la declinaison, la portugaise enseigne ce qui, en portugais, se
trompe au meme endroit (le pronom lhe, l'accord de l'adjectif, le perfeito...).
BROUILLON : a faire relire par un lusophone du Portugal.
"""
import io, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "portugais", "scenes")

T_PERFEITO = "Le perfeito : ce qui s'est passé"
T_PASSIF = "Passif et relatives"
T_HYPO = "Hypothèses : deve, talvez, dizem que"

COUCHES = {
"kueche": {
"B1": (T_PERFEITO, """
karotte | mark | O Mark ___ a cenoura. | cortou | cortava / corta | O Mark cortou a cenoura. | Mark a coupé la carotte. | <b>cortar</b> → ele <b>cortou</b> : l'action est finie, perfeito.
ei | pfanne | Ele ___ dois ovos. | estrelou | estrelava / estrela | Ele estrelou dois ovos. | Il a fait frire deux œufs. | <b>estrelar</b> (des œufs au plat) → <b>estrelou</b>.
topf |  | A sopa já ___ uma hora. | cozeu | cozia / coze | A sopa já cozeu uma hora. | La soupe a déjà cuit une heure. | <b>cozer</b> → <b>cozeu</b> (-er : -eu).
brot | tisch | O Mark ___ o pão em cima da mesa. | pôs | punha / põe | O Mark pôs o pão em cima da mesa. | Mark a posé le pain sur la table. | <b>pôr</b> est irrégulier : <b>pus, pôs</b>.
katze | stuhl | O gato ___ para a cadeira. | saltou | saltava / salta | O gato saltou para a cadeira. | Le chat a sauté sur la chaise. | <b>saltar para</b> : le mouvement vers ; perfeito <b>saltou</b>.
milch | tisch | O Mark ___ o leite na mesa. | deixou | deixava / deixa | O Mark deixou o leite na mesa. | Mark a mis le lait sur la table. | <b>deixar</b> → <b>deixou</b>.
handtuch | backofen | O Mark ___ a toalha no forno. | pendurou | pendurava / pendura | O Mark pendurou a toalha no forno. | Mark a accroché le torchon au four. | <b>pendurar</b> → <b>pendurou</b>.
mark |  | Esta noite, o Mark ___ para os colegas de casa. | cozinhou | cozinhava / cozinhará | Esta noite, o Mark cozinhou para os colegas de casa. | Ce soir, Mark a cuisiné pour ses colocataires. | Une action finie, ce soir : <b>cozinhou</b>.
"""),
"B2": (T_PASSIF, """
karotte | messer | A cenoura está a ser ___. | cortada | cortado / cortar | A cenoura está a ser cortada. | La carotte est en train d'être coupée. | L'action en cours au passif : <b>estar a ser</b> + participe accordé (a cenoura → <b>cortada</b>).
tisch | kartoffel | A mesa ___ estão os legumes é de madeira. | onde | que / quem | A mesa onde estão os legumes é de madeira. | La table sur laquelle sont les légumes est en bois. | Un lieu : <b>onde</b> (ou <b>em que</b>).
katze | stuhl | O gato ___ está na cadeira olha para a mesa. | que | quem / onde | O gato que está na cadeira olha para a mesa. | Le chat qui est assis sur la chaise regarde la table. | Le sujet de la relative : <b>que</b>.
buch | tisch | O livro, ___ páginas estão cheias de imagens, está na mesa. | cujas | cujos / que as | O livro, cujas páginas estão cheias de imagens, está na mesa. | Le livre dont les pages sont pleines d'images est sur la table. | <b>cujo</b> s'accorde avec ce qui suit : páginas → <b>cujas</b>.
ei | pfanne | Os ovos na frigideira já estão ___. | estrelados | estrelado / estrelando | Os ovos na frigideira já estão estrelados. | Les œufs dans la poêle sont déjà cuits. | Un état : <b>estar</b> + participe accordé (os ovos → <b>estrelados</b>).
topf |  | A sopa ainda tem de ___ dez minutos. | cozer | ser cozida / cozida | A sopa ainda tem de cozer dez minutos. | La soupe doit encore cuire dix minutes. | <b>ter de</b> + infinitif ; cozer est ici intransitif.
"""),
"C1": (T_HYPO, """
topf | mark | O Mark sorri: a sopa ___ cheirar bem. | deve | pode / tem de | A sopa deve cheirar bem. | La soupe doit sentir bon. | <b>dever</b> + infinitif : une déduction presque sûre.
katze | karotte | ___ o gato esteja à espera de um pedaço de cenoura. | Talvez | Deve / Se calhar que | Talvez o gato esteja à espera de um pedaço de cenoura. | Le chat espère peut-être un morceau de carotte. | <b>talvez</b> + conjuntivo (<b>esteja</b>).
topf | mark | O tacho é enorme: o Mark ___ à espera de convidados. | estará | estava / esteja | O Mark estará à espera de convidados. | Mark attend sans doute des invités. | Le futur de supposition : <b>estará</b> = il est sans doute.
mark |  | ___ que o Mark faz a melhor sopa da casa. | Dizem | Dizem-se / Diga | Dizem que o Mark faz a melhor sopa da casa. | Il paraît que Mark fait la meilleure soupe de la colocation. | Le ouï-dire : <b>dizem que</b>, <b>diz-se que</b>.
"""),
},
"fruehstueck": {
"B1": ("Le pronom complément : lhe, o, a", """
kuchen-mark | mark | A empregada traz-___ um bolo. | lhe | o / se | A empregada traz-lhe um bolo. | La serveuse lui apporte un gâteau. | À qui ? complément indirect : <b>lhe</b>, après le verbe.
tasse | mark | O café sabe-___ bem. | lhe | o / a | O café sabe-lhe bem. | Il trouve le café bon. | <b>saber bem a alguém</b> : être bon pour quelqu'un ; <b>lhe</b>.
serveuse | kuchen-mark | O Mark pediu um bolo ___ empregada. | à | a / da | O Mark pediu um bolo à empregada. | Mark a commandé un gâteau à la serveuse. | <b>pedir algo a alguém</b> : a + a = <b>à</b>.
salz |  | Podes passar-___ o sal, por favor? | me | mim / eu | Podes passar-me o sal, por favor? | Tu peux me passer le sel, s'il te plaît ? | Complément indirect : <b>me</b>, après l'infinitif.
jacke | monsieur | O casaco é ___ homem ali ao fundo? | do | o / ao | O casaco é do homem ali ao fundo? | La veste appartient-elle à l'homme là-bas au fond ? | L'appartenance : <b>ser de</b> (de + o = <b>do</b>).
teller | mark | A empregada dá o prato ___ cliente. | ao | o / do | A empregada dá o prato ao cliente. | La serveuse tend l'assiette au client. | <b>dar algo a alguém</b> : a + o = <b>ao</b>.
messer | broetchen | O Mark corta o papo-seco ___ a faca. | com | de / por | O Mark corta o papo-seco com a faca. | Mark coupe le petit pain avec le couteau. | L'instrument : <b>com</b>.
serveuse | mark | O Mark agradece-___ o bolo. | lhe | a / o | O Mark agradece-lhe o bolo. | Mark la remercie pour le gâteau. | <b>agradecer algo a alguém</b> : <b>lhe</b> (alors que le français dit « la »).
"""),
"B2": ("Relatives et passif d'état", """
mark | kuchen-mark | O cliente a ___ a empregada traz o bolo chama-se Mark. | quem | que / qual | O cliente a quem a empregada traz o bolo chama-se Mark. | Le client à qui la serveuse apporte le gâteau s'appelle Mark. | Une personne, après une préposition : <b>a quem</b>.
serveuse | kuchen-mark | A empregada, ___ usa óculos, traz o bolo. | que | quem / cuja | A empregada, que usa óculos, traz o bolo. | La serveuse, qui porte des lunettes, apporte le gâteau. | Sujet : <b>que</b>.
tisch | mark | A mesa ___ o Mark está sentado fica junto à janela. | a que | que / onde que | A mesa a que o Mark está sentado fica junto à janela. | La table à laquelle Mark est assis est près de la fenêtre. | <b>sentar-se à mesa</b> : la préposition passe devant le relatif (<b>a que</b>, ou <b>à qual</b>).
tisch |  | A mesa já está ___. | posta | posto / pôs | A mesa já está posta. | La table est déjà mise. | <b>pôr a mesa</b> → <b>a mesa está posta</b> (accord au féminin).
broetchen | teller | O papo-seco já está ___. | cortado | cortada / corta | O papo-seco já está cortado. | Le petit pain est déjà coupé. | Un état : <b>estar</b> + participe accordé.
tuer |  | A porta está ___. | aberta | aberto / abrida | A porta está aberta. | La porte est ouverte. | <b>abrir</b> → <b>aberto</b>, ici au féminin.
"""),
"C1": (T_HYPO, """
kuchen-mark | mark | O Mark ___ ter muita fome. | deve | pode / há de | O Mark deve ter muita fome. | Mark doit avoir très faim. | <b>dever</b> : la déduction.
jacke | monsieur | ___ que o casaco seja do homem ali ao fundo. | Pode ser | Deve ser / É | Pode ser que o casaco seja do homem ali ao fundo. | La veste appartient peut-être à l'homme là-bas au fond. | <b>pode ser que</b> + conjuntivo (<b>seja</b>).
mark | serveuse | O Mark ___ cliente habitual aqui. | será | seja / foi | O Mark será cliente habitual aqui. | Mark est sans doute un habitué ici. | Futur de supposition : <b>será</b>.
kuchen |  | ___ que a tarte de maçã daqui é a melhor de Lisboa. | Diz-se | Dizem-se / Diga-se | Diz-se que a tarte de maçã daqui é a melhor de Lisboa. | Il paraît que la tarte aux pommes d'ici est la meilleure de Lisbonne. | Le ouï-dire : <b>diz-se que</b>.
"""),
},
"kleidergeschaeft": {
"B1": ("L'accord de l'adjectif", """
pullover | anna | A Anna segura uma camisola ___. | amarela | amarelo / amarelas | A Anna segura uma camisola amarela. | Anna tient un pull jaune. | <b>a camisola</b> est féminin : <b>amarela</b>.
kleid |  | O vestido ___ está pendurado à esquerda. | vermelho | vermelha / vermelhos | O vestido vermelho está pendurado à esquerda. | La robe rouge est accrochée tout à gauche. | <b>o vestido</b> : masculin en portugais.
schuh-main | monsieur | O homem experimenta um sapato ___. | castanho | castanha / castanhos | O homem experimenta um sapato castanho. | L'homme essaie une chaussure marron. | « Marron » au Portugal : <b>castanho</b> (qui s'accorde).
schal | verkaeuferin | A empregada dobra um cachecol ___. | às riscas | riscada / riscados | A empregada dobra um cachecol às riscas. | La vendeuse plie une écharpe rayée. | Rayé : <b>às riscas</b>, invariable.
tasche-noire | regal | Na estante há uma mala ___. | preta | preto / pretas | Na estante há uma mala preta. | Sur l'étagère, il y a un sac noir. | <b>a mala</b> → <b>preta</b>.
hose-anna | anna | A Anna veste umas calças azul-___. | claras | claro / clara | A Anna veste umas calças azul-claras. | Anna porte un pantalon bleu clair. | <b>as calças</b> est pluriel ; dans <b>azul-claro</b>, seul le second mot s'accorde.
monsieur |  | O homem de cabelo ___ experimenta sapatos. | grisalho | grisalha / cinzentos | O homem de cabelo grisalho experimenta sapatos. | L'homme aux cheveux gris essaie des chaussures. | Les cheveux gris : <b>cabelo grisalho</b> (au singulier en portugais).
mantel | anzug | Um sobretudo ___ está ao lado do fato. | castanho | castanha / castanhos | Um sobretudo castanho está ao lado do fato. | Un manteau marron est accroché à côté du costume. | <b>o sobretudo</b> → <b>castanho</b> ; et <b>o fato</b> = le costume, au Portugal.
"""),
"B2": (T_PASSIF, """
anna | pullover | A mulher ___ segura a camisola amarela chama-se Anna. | que | quem / qual | A mulher que segura a camisola amarela chama-se Anna. | La femme qui tient le pull jaune s'appelle Anna. | Sujet de la relative : <b>que</b>.
monsieur | schuh-sol | O homem, ___ sapato ainda está no chão, experimenta o outro. | cujo | cuja / que o | O homem, cujo sapato ainda está no chão, experimenta o outro. | L'homme dont la chaussure est encore par terre essaie l'autre. | <b>cujo</b> + nom masculin (sapato).
spiegel | hocker | O espelho em frente ___ qual está o banquinho tem moldura de madeira. | do | o / ao | O espelho em frente do qual está o banquinho tem moldura de madeira. | Le miroir devant lequel est le tabouret a un cadre en bois. | <b>em frente de</b> + <b>o qual</b> = <b>em frente do qual</b>.
korb |  | As meias ___ estão no cesto são coloridas. | que | onde / cujas | As meias que estão no cesto são coloridas. | Les chaussettes qui sont dans le panier sont multicolores. | Sujet : <b>que</b>.
pullover-stapel | regal | As camisolas na estante estão bem ___. | dobradas | dobrados / dobrar | As camisolas na estante estão bem dobradas. | Les pulls sur l'étagère sont soigneusement pliés. | Un état : <b>estar</b> + participe accordé (as camisolas → <b>dobradas</b>).
schal | verkaeuferin | O cachecol está a ser dobrado ___ empregada. | pela | por / pelo | O cachecol está a ser dobrado pela empregada. | L'écharpe est en train d'être pliée par la vendeuse. | L'agent du passif : <b>por</b> + a = <b>pela</b>.
"""),
"C1": (T_HYPO, """
pullover | anna | A camisola ___ agradar-lhe. | deve | pode / há de | A camisola deve agradar-lhe. | Le pull doit lui plaire. | Déduction : <b>dever</b>.
kabine | anna | ___ ela vai experimentá-la já no provador. | Se calhar | Talvez que / Deve | Se calhar ela vai experimentá-la já no provador. | Elle va peut-être l'essayer tout de suite dans la cabine. | <b>se calhar</b> (peut-être, très portugais) + indicatif.
schuh-main | monsieur | O homem ___ comprar os sapatos. | deverá | deveria-se / deva | O homem deverá comprar os sapatos. | L'homme va sans doute acheter les chaussures. | <b>deverá</b> + infinitif : probable.
verkaeuferin |  | ___ que a empregada trabalha aqui há trinta anos. | Parece | Parecem / Pareça | Parece que a empregada trabalha aqui há trinta anos. | Il paraît que la vendeuse travaille ici depuis trente ans. | Le ouï-dire : <b>parece que</b>.
"""),
},
"supermarkt": {
"B1": ("Comparer : mais… do que, o mais…", """
tuete | tasche | O saco é ___ do que a mala. | maior | mais grande / tão grande | O saco é maior do que a mala. | Le sac en papier est plus grand que le sac à main. | <b>grande</b> → <b>maior</b>.
maedchen | anna | A menina é mais ___ do que a Anna. | pequena | pequeno / menor que | A menina é mais pequena do que a Anna. | La fille est plus petite qu'Anna. | Au Portugal : <b>mais pequeno</b> (ou <b>menor</b>), accordé.
mann | anna | O homem na caixa é mais ___ do que a Anna. | velho | velha / maior | O homem na caixa é mais velho do que a Anna. | L'homme à la caisse est plus âgé qu'Anna. | L'âge : <b>mais velho</b>, <b>mais novo</b>.
banane | maedchen | As bananas são tão amarelas ___ o casaco da menina. | como | do que / que tão | As bananas são tão amarelas como o casaco da menina. | Les bananes sont aussi jaunes que la veste de la fille. | <b>tão … como</b> = aussi … que.
saft | dose | O sumo está mais ___ do que as latas. | alto | alta / acima | O sumo está mais alto do que as latas. | Le jus est placé plus haut que les boîtes de conserve. | <b>mais alto</b> (le sumo, masculin).
kaese | anna | A Anna gosta de leite, mas de queijo gosta ___. | mais | melhor / maior | A Anna gosta de leite, mas de queijo gosta mais. | Anna aime bien le lait, mais elle préfère le fromage. | Aimer davantage : <b>gostar mais</b>.
maedchen |  | Do que a menina mais gosta é ___ chocolate. | de | o / do | Do que a menina mais gosta é de chocolate. | Ce que la fille préfère, c'est le chocolat. | <b>gostar de</b> garde son <b>de</b> : <b>é de chocolate</b>.
brot |  | Este é o pão ___ fresco da loja. | mais | melhor / tão | Este é o pão mais fresco da loja. | C'est le pain le plus frais du magasin. | Le superlatif : <b>o … mais</b> + adjectif.
"""),
"B2": ("La politesse : le conditionnel et l'imperfeito", """
tuete | mann | ___ dar-me um saco, por favor? | Podia | Pode-se / Poderei | Podia dar-me um saco, por favor? | Pourriez-vous me donner un sac, s'il vous plaît ? | Au Portugal, la politesse orale passe par l'imperfeito : <b>podia</b>.
kaese | anna | ___ um bocado de queijo, se faz favor. | Queria | Quero-me / Quis | Queria um bocado de queijo, se faz favor. | Je voudrais un morceau de fromage. | <b>queria</b> : je voudrais ; <b>se faz favor</b> : s'il vous plaît, très portugais.
korb |  | ___ a amabilidade de me ajudar com o cesto? | Teria | Terá-se / Tem-se | Teria a amabilidade de me ajudar com o cesto? | Auriez-vous la gentillesse de m'aider avec le panier ? | Une formule soignée : <b>teria a amabilidade de</b>.
kasse | anna | ___ de pagar com cartão. | Gostava | Gostei / Goste | Gostava de pagar com cartão. | Je voudrais payer par carte. | <b>gostava de</b> = j'aimerais (oral).
mann |  | ___-se que lhe faça uma pergunta? | Importa | Importam / Importe | Importa-se que lhe faça uma pergunta? | Puis-je vous poser une question ? | <b>Importa-se que</b> + conjuntivo : « cela vous dérange-t-il que… ».
milch |  | No seu lugar, eu ___ o leite fresco. | levava | levei / levo | No seu lugar, eu levava o leite fresco. | À votre place, je prendrais le lait frais. | L'hypothèse, à l'oral : l'imperfeito (<b>levava</b>) au lieu de levaria.
"""),
"C1": (T_HYPO, """
maedchen | regal | Ela ___ ter querido chocolate. | deve | pode / há de | Ela deve ter querido chocolate. | Elle a dû vouloir du chocolat. | Déduction sur le passé : <b>dever ter</b> + participe.
mann | kasse | O homem na caixa ___ ser o patrão. | pode | deve de / tem de | O homem na caixa pode ser o patrão. | L'homme à la caisse est peut-être le patron. | Une possibilité : <b>poder</b>.
kasse |  | A loja ___ fechar daqui a pouco. | deve | pode-se / há | A loja deve fechar daqui a pouco. | Le magasin devrait bientôt fermer. | Probable : <b>dever</b>.
brot |  | ___ que o pão daqui é o melhor do bairro. | Dizem | Diz / Digam | Dizem que o pão daqui é o melhor do bairro. | Il paraît que le pain d'ici est le meilleur du quartier. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"restaurant": {
"B1": ("Les quantités : um copo de água, uma fatia de bolo", """
glas | mark | O Mark pede um copo ___ água. | de | com / da | O Mark pede um copo de água. | Mark commande un verre d'eau. | Quantité + <b>de</b> + nom, sans article.
suppe | frau | A senhora come um prato ___ sopa. | de | da / com | A senhora come um prato de sopa. | La dame mange une assiette de soupe. | <b>um prato de sopa</b>.
flasche | tisch | Na mesa há uma ___ de água. | garrafa | garrafão / copo | Na mesa há uma garrafa de água. | Sur la table, il y a une bouteille d'eau. | <b>a garrafa</b> = la bouteille.
kuchen | mark | O Mark queria uma ___ de bolo. | fatia | peça / bocado de | O Mark queria uma fatia de bolo. | Mark voudrait un morceau de gâteau. | Une part de gâteau : <b>uma fatia</b> (une tranche).
korb | kellnerin | A empregada traz um cesto ___ pão. | de | com o / do | A empregada traz um cesto de pão. | La serveuse apporte une corbeille de pain. | <b>um cesto de pão</b>.
tasse | mark | O Mark também pede uma ___ de café. | chávena | xícara / taça | O Mark também pede uma chávena de café. | Mark commande aussi une tasse de café. | Au Portugal : <b>a chávena</b> (au Brésil, xícara).
flasche-2 | regal | Na estante há muitas garrafas ___ vinho. | de | do / com | Na estante há muitas garrafas de vinho. | Sur l'étagère, il y a beaucoup de bouteilles de vin. | <b>garrafas de vinho</b>.
fleisch | mann | O senhor come um ___ de carne. | bife | bocadinho / fatia | O senhor come um bife. | Le monsieur mange un morceau de viande. | Une pièce de viande grillée : <b>um bife</b>.
"""),
"B2": ("Algo, nada, tudo + adjectif", """
speisekarte | mark | O Mark queria comer algo ___. | quente | de quente / quentes | O Mark queria comer algo quente. | Mark voudrait manger quelque chose de chaud. | <b>algo</b> + adjectif au masculin singulier, sans « de ».
frau |  | A senhora não come nada ___. | doce | de doces / doces | A senhora não come nada doce. | La dame ne mange rien de sucré. | <b>nada</b> + adjectif (ou <b>nada de doce</b>).
speisekarte |  | Hoje há alguma coisa ___ na ementa? | nova | novo / de nova | Hoje há alguma coisa nova na ementa? | Y a-t-il quelque chose de nouveau sur la carte aujourd'hui ? | <b>alguma coisa</b> est féminin : <b>nova</b>.
speisekarte |  | Na ementa há muita coisa ___. | boa | bom / boas coisas | Na ementa há muita coisa boa. | Sur la carte, il y a beaucoup de bonnes choses. | <b>muita coisa</b> + adjectif féminin.
theke |  | O ___ deste restaurante é a cozinha. | melhor | mais bom / bom | O melhor deste restaurante é a cozinha. | Le meilleur de ce restaurant, c'est la cuisine. | L'adjectif substantivé : <b>o melhor</b>.
mark |  | O Mark gosta de provar tudo o que é ___. | novo | nova / novos | O Mark gosta de provar tudo o que é novo. | Mark aime goûter tout ce qui est nouveau. | <b>tudo o que é</b> + adjectif masculin.
"""),
"C1": (T_HYPO, """
mark | speisekarte | Ele ___ ter fome. | deve | pode / tem de | Ele deve ter fome. | Il doit avoir faim. | Déduction : <b>dever</b>.
mann | frau | ___ o casal jante aqui todas as noites. | Talvez | Deve / Pode | Talvez o casal jante aqui todas as noites. | Le couple dîne peut-être ici tous les soirs. | <b>talvez</b> + conjuntivo (<b>jante</b>).
pizza | fenster | A pizza ___ para a mesa junto à janela. | será | seja / foi | A pizza será para a mesa junto à janela. | La pizza doit être pour la table près de la fenêtre. | Futur de supposition : <b>será</b>.
theke |  | Este restaurante ___ a melhor cozinha do bairro. | teria | terá-se / tenha | Este restaurante teria a melhor cozinha do bairro. | Ce restaurant aurait la meilleure cuisine du quartier. | Le conditionnel de la rumeur : <b>teria</b>.
"""),
},
"arztpraxis": {
"B1": ("Pôr, estar, deixar : la position et le geste", """
ball | tasche | A bola ___ em cima da mala. | está | pôs / põe | A bola está em cima da mala. | Le ballon est sur le sac. | La position : <b>estar</b>.
ball | tasche | O Mark ___ a bola em cima da mala. | pôs | está / estava | O Mark pôs a bola em cima da mala. | Mark a posé le ballon sur le sac. | Le geste : <b>pôr</b> (perfeito : <b>pôs</b>).
aerztin | hocker | A médica está ___ num banquinho. | sentada | sentado / sentar | A médica está sentada num banquinho. | La médecin est assise sur un tabouret. | <b>estar sentado</b>, accordé (a médica → <b>sentada</b>).
schuh | tasche | O Mark ___ os sapatos ao lado da mala. | deixou | ficou / esteve | O Mark deixou os sapatos ao lado da mala. | Mark a mis ses chaussures à côté du sac. | <b>deixar</b> : poser et laisser.
schuh | tasche | Os sapatos ___ ao lado da mala. | estão | põem / deixam | Os sapatos estão ao lado da mala. | Les chaussures sont à côté du sac. | La position : <b>estar</b>.
jacke | tuer | O Mark ___ o casaco ao lado da porta. | pendurou | pendurava / pendura | O Mark pendurou o casaco ao lado da porta. | Mark a accroché sa veste à côté de la porte. | <b>pendurar</b> → <b>pendurou</b>.
glas | schreibtisch | O copo está ___ secretária. | em cima da | em cima a / na cima da | O copo está em cima da secretária. | Le verre est sur le bureau. | <b>em cima de</b> + a = <b>em cima da</b> ; <b>a secretária</b> = le bureau (meuble).
karte | schreibtisch | A médica ___ o cartão de utente em cima da secretária. | pousou | pousava / pousa | A médica pousou o cartão de utente em cima da secretária. | La médecin a posé la carte de santé sur le bureau. | <b>pousar</b> : poser doucement ; <b>o cartão de utente</b>, la carte du système de santé portugais.
"""),
"B2": ("Relatives et passif d'état", """
mark | knie | O doente, ___ joelho está ferido, chama-se Mark. | cujo | cuja / que o | O doente, cujo joelho está ferido, chama-se Mark. | Le patient dont le genou est blessé s'appelle Mark. | <b>cujo</b> + nom masculin (joelho).
aerztin | verband | A médica, ___ segura uma ligadura, sorri. | que | quem / cuja | A médica, que segura uma ligadura, sorri. | La médecin, qui tient un bandage à la main, sourit. | Sujet : <b>que</b>.
mark | aerztin | O doente a ___ a médica sorri chama-se Mark. | quem | que / qual | O doente a quem a médica sorri chama-se Mark. | Le patient à qui la médecin sourit s'appelle Mark. | <b>sorrir a alguém</b> → <b>a quem</b>.
tasche | ball | A mala em cima da ___ está a bola é do Mark. | qual | que / quem | A mala em cima da qual está a bola é do Mark. | Le sac sur lequel est posé le ballon appartient à Mark. | Après une préposition longue : <b>da qual</b>.
fenster |  | A janela está ___. | fechada | fechado / fecha | A janela está fechada. | La fenêtre est fermée. | État : <b>estar</b> + participe accordé.
pflaster | knie | O penso já está ___. | posto | posta / pôs | O penso já está posto. | Le pansement est déjà posé. | <b>pôr</b> → <b>posto</b> ; o penso, masculin.
"""),
"C1": (T_HYPO, """
mark | ball | O Mark ___ ter caído a jogar futebol. | deve | pode-se / tem de | O Mark deve ter caído a jogar futebol. | Mark a dû tomber en jouant au foot. | Déduction sur le passé : <b>deve ter</b> + participe.
verband | aerztin | Se calhar a médica ___ uma ligadura daqui a pouco. | põe-lhe | ponha-lhe / lhe põe | Se calhar a médica põe-lhe uma ligadura daqui a pouco. | La médecin va peut-être lui mettre un bandage tout de suite. | <b>se calhar</b> + indicatif ; pronom après le verbe.
mark |  | ___ não deve ser nada de grave. | Não | Nem / Nunca | Não deve ser nada de grave. | Ce n'est sans doute rien de grave. | <b>não deve ser</b> = ce n'est sans doute pas.
aerztin |  | ___ que a médica é muito boa. | Dizem | Diz-se-lhe / Digam | Dizem que a médica é muito boa. | On dit que la médecin est très bonne. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"wohnzimmer": {
"B1": ("Onde ? Para onde ? — em et para", """
ball | schrank | A bola ainda está ___ armário. | em cima do | para o / ao | A bola ainda está em cima do armário. | Le ballon est encore sur l'armoire. | La position : <b>em cima de</b>.
ball | schrank | O Mark põe a bola ___ armário. | no | para o / ao | O Mark põe a bola no armário. | Mark met le ballon dans l'armoire. | <b>pôr em</b> : là où la chose se retrouve (<b>no</b> armário).
tasse | couchtisch | A chávena está ___ mesa de centro. | na | para a / à | A chávena está na mesa de centro. | La tasse est sur la table basse. | Position : em + a = <b>na</b>.
tasse | regal | O Mark põe a chávena ___ estante. | na | para a / à | O Mark põe a chávena na estante. | Mark pose la tasse sur l'étagère. | <b>pôr na estante</b>.
regenschirm | lampe | O guarda-chuva ainda está pendurado ___ candeeiro. | no | ao / para o | O guarda-chuva ainda está pendurado no candeeiro. | Le parapluie est encore accroché à la lampe. | <b>pendurado em</b> : no candeeiro.
regenschirm | tuer | O Mark pendura o guarda-chuva ___ porta. | na | para a / à | O Mark pendura o guarda-chuva na porta. | Mark accroche le parapluie à la porte. | <b>pendurar em</b> : na porta.
buch | regal | O Mark arruma o livro ___ estante. | na | para a / à | O Mark arruma o livro na estante. | Mark range le livre sur l'étagère. | <b>arrumar em</b>.
flasche | eimer | As garrafas estão ___ balde. | no | ao / para o | As garrafas estão no balde. | Les bouteilles sont dans le seau. | em + o = <b>no</b>.
katze | sofa | O gato vai saltar ___ o sofá. | para | em / no | O gato vai saltar para o sofá. | Le chat va sauter sur le canapé tout de suite. | Un mouvement vers : <b>saltar para</b>.
luftballon | boden | Os balões estão ___ chão. | no | ao / para o | Os balões estão no chão. | Les ballons sont par terre. | Par terre : <b>no chão</b>.
"""),
"B2": ("Relatives et passif d'état", """
lampe | regenschirm | O candeeiro ___ qual está pendurado um guarda-chuva é redondo. | no | ao / do | O candeeiro no qual está pendurado um guarda-chuva é redondo. | La lampe à laquelle est accroché un parapluie est ronde. | <b>pendurado em</b> + o qual = <b>no qual</b>.
hund |  | O cão ___ dorme debaixo da mesa perdeu a festa. | que | quem / qual | O cão que dorme debaixo da mesa perdeu a festa. | Le chien qui dort sous la table a raté la fête. | Sujet : <b>que</b>.
katze | karton | O gato, ___ cabeça sai da caixa de cartão, parece calmo. | cuja | cujo / que a | O gato, cuja cabeça sai da caixa de cartão, parece calmo. | Le chat dont la tête dépasse du carton a l'air tout calme. | <b>cujo</b> s'accorde avec <b>cabeça</b> : <b>cuja</b>.
regal | fahrrad | A estante em frente da ___ está a bicicleta está cheia de livros. | qual | que / quem | A estante em frente da qual está a bicicleta está cheia de livros. | L'étagère devant laquelle est le vélo est pleine de livres. | <b>em frente da qual</b>.
tuer |  | A porta está ___. | aberta | aberto / abrida | A porta está aberta. | La porte est ouverte. | <b>abrir</b> → <b>aberto</b>, ici au féminin.
pflanze |  | As luzinhas estão ___ à volta da planta. | enroladas | enrolados / enrolar | As luzinhas estão enroladas à volta da planta. | La guirlande lumineuse est enroulée autour de la plante. | État : <b>estar</b> + participe accordé (as luzinhas → <b>enroladas</b>).
"""),
"C1": (T_HYPO, """
luftballon |  | A festa ___ ter sido muito longa. | deve | pode-se / tem de | A festa deve ter sido muito longa. | La fête a dû être très longue. | Déduction sur le passé : <b>deve ter sido</b>.
regenschirm | lampe | ___ sido um dos convidados. | Terá | Teria-se / Tenha | Terá sido um dos convidados. | C'était sans doute l'un des invités. | Supposition sur le passé : <b>terá sido</b>.
socke |  | ___ ser de um convidado. | Pode | Deve de / Há | Pode ser de um convidado. | Elle appartient peut-être à un invité. | Une possibilité : <b>pode ser</b>.
koffer |  | Se o Mark não ___ perdido a festa, agora também estaria cansado. | tivesse | tiver / tinha-se | Se o Mark não tivesse perdido a festa, agora também estaria cansado. | Si Mark n'avait pas raté la fête, il serait lui aussi fatigué maintenant. | Irréel du passé : <b>se tivesse</b> + participe.
"""),
},
"park": {
"B1": ("Onde ? Para onde ? — a, para, por, em", """
ball | hund | A Anna atira a bola ___ cão. | ao | o / no | A Anna atira a bola ao cão. | Anna lance le ballon au chien. | <b>atirar algo a alguém</b> : a + o = <b>ao</b>.
hund | gras | O cão corre ___ relva. | pela | para a / à | O cão corre pela relva. | Le chien court sur l'herbe. | Parcourir un espace : <b>por</b> + a = <b>pela</b>.
fahrrad | junge | O rapaz anda ___ bicicleta. | de | na / com a | O rapaz anda de bicicleta. | Le garçon fait du vélo. | Le moyen de transport : <b>andar de</b> bicicleta.
buch | decke | A Anna pôs o livro ___ manta. | na | para a / à | A Anna pôs o livro na manta. | Anna a posé son livre sur la couverture. | <b>pôr em</b> : na manta.
buch | decke | Agora o livro está ___ manta. | na | para a / pela | Agora o livro está na manta. | Maintenant, le livre est sur la couverture. | Position : em + a = <b>na</b>.
vogel | bank | O pássaro ___ no banco. | pousou | pousava / pousa | O pássaro pousou no banco. | L'oiseau s'est posé sur le banc. | <b>pousar</b> (un oiseau) → perfeito <b>pousou</b>.
monsieur | bank | O homem está sentado ___ banco a ler. | no | ao / para o | O homem está sentado no banco a ler. | L'homme est assis sur le banc et lit. | <b>sentado no banco</b> ; <b>a ler</b> = en train de lire.
boot | see | Duas pessoas remam ___ lago. | no | ao / pelo do | Duas pessoas remam no lago. | Deux personnes rament sur le lac. | em + o = <b>no</b>.
"""),
"B2": ("Relatives et participes", """
anna | ball | A mulher ___ atira a bola ao cão chama-se Anna. | que | quem / qual | A mulher que atira a bola ao cão chama-se Anna. | La femme qui lance le ballon au chien s'appelle Anna. | Sujet : <b>que</b>.
junge | helm | O rapaz, ___ capacete é azul, anda de bicicleta. | cujo | cuja / que o | O rapaz, cujo capacete é azul, anda de bicicleta. | Le garçon au casque bleu fait du vélo. | <b>cujo</b> + capacete (masculin).
bank | monsieur | O banco ___ qual o homem está sentado é verde. | no | ao / do | O banco no qual o homem está sentado é verde. | Le banc sur lequel l'homme est assis est vert. | <b>sentado em</b> + o qual = <b>no qual</b>.
hund | ball | O cão, ___ a correr, quer apanhar a bola. | sempre | que / onde | O cão, sempre a correr, quer apanhar a bola. | Le chien qui court veut attraper le ballon. | Le portugais dit l'action en cours avec <b>a</b> + infinitif, même sans verbe : <b>sempre a correr</b>.
buch | decke | Na manta há um livro ___. | aberto | aberta / abrido | Na manta há um livro aberto. | Sur la couverture, il y a un livre ouvert. | Participe employé comme adjectif : <b>aberto</b>.
decke | gras | A manta está ___ na relva. | estendida | estendido / estender | A manta está estendida na relva. | La couverture est étalée sur l'herbe. | État : <b>estar</b> + participe accordé.
"""),
"C1": (T_HYPO, """
anna | hund | Ela ___ conhecer o cão. | deve | pode / tem de | Ela deve conhecer o cão. | Elle doit connaître le chien. | Déduction : <b>dever</b>.
hund | ball | Se calhar o cão ___ a bola já a seguir. | apanha | apanhe / apanhará-se | Se calhar o cão apanha a bola já a seguir. | Le chien va peut-être attraper le ballon tout de suite. | <b>se calhar</b> + indicatif présent.
monsieur | bank | O homem ___ vir cá todos os domingos. | deve | pode-se / há | O homem deve vir cá todos os domingos. | L'homme vient sans doute ici chaque dimanche. | Probable : <b>dever</b>.
see |  | ___ que no lago há peixes enormes. | Dizem | Dizem-se / Digam | Dizem que no lago há peixes enormes. | Il paraît qu'il y a d'énormes poissons dans le lac. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"geburtstag": {
"B1": ("Lhe, lhes : donner, offrir, féliciter", """
geschenk | mark | A Anna dá-___ um presente. | lhe | o / se | A Anna dá-lhe um presente. | Anna lui donne un cadeau. | À qui ? <b>lhe</b>, après le verbe.
mark |  | Todos lhe dão os ___. | parabéns | felicidades-lhe / parabém | Todos lhe dão os parabéns. | Tout le monde lui souhaite un bon anniversaire. | <b>dar os parabéns a alguém</b> ; après <b>todos</b>, le pronom passe devant.
geschenk | mark | O presente agrada-___. | lhe | o / se | O presente agrada-lhe. | Le cadeau lui plaît. | <b>agradar a alguém</b> : <b>lhe</b>.
geschenk | mark | A Anna oferece uma lembrança ___ namorado. | ao | o / do | A Anna oferece uma lembrança ao namorado. | Anna offre un petit quelque chose à son ami. | <b>oferecer algo a alguém</b> : a + o = <b>ao</b>.
handy | mark | O amigo tira uma fotografia ___ Mark. | ao | do / o | O amigo tira uma fotografia ao Mark. | L'ami prend une photo de Mark. | Au Portugal : <b>tirar uma fotografia a alguém</b>.
mark |  | O Mark agradece ___ amigos a festa. | aos | os / dos | O Mark agradece aos amigos a festa. | Mark remercie ses amis pour la fête. | <b>agradecer algo a alguém</b> : a + os = <b>aos</b>.
kerze | torte | As velas estão ___ bolo. | no | ao / pelo | As velas estão no bolo. | Les bougies sont sur le gâteau. | em + o = <b>no</b>.
saft |  | A Anna vai já levar sumo ___ convidados. | aos | os / dos | A Anna vai já levar sumo aos convidados. | Anna va tout de suite apporter du jus aux invités. | a + os = <b>aos</b>.
"""),
"B2": (T_PASSIF, """
geschenk | anna | O presente ___ a Anna tem na mão é verde. | que | quem / cujo | O presente que a Anna tem na mão é verde. | Le cadeau qu'Anna tient à la main est vert. | Objet de la relative : <b>que</b>.
freund | mark | O amigo ___ fotografa o Mark está sentado no sofá. | que | quem / qual | O amigo que fotografa o Mark está sentado no sofá. | L'ami qui photographie Mark est assis sur le canapé. | Sujet : <b>que</b>.
torte | kerze | O bolo no ___ ardem cinco velas é de chocolate. | qual | que / quem | O bolo no qual ardem cinco velas é de chocolate. | Le gâteau sur lequel brûlent cinq bougies est au chocolat. | <b>no qual</b> (em + o qual).
kerze | torte | As velas vão ser ___ daqui a pouco. | apagadas | apagados / apagar | As velas vão ser apagadas daqui a pouco. | Les bougies vont être soufflées tout de suite. | Passif au futur proche : <b>vão ser</b> + participe accordé.
geschenk-2 |  | O presente vermelho está bem ___. | embrulhado | embrulhada / embrulhar | O presente vermelho está bem embrulhado. | Le cadeau rouge est joliment emballé. | État : <b>estar</b> + participe (o presente → <b>embrulhado</b>).
freundin |  | A amiga, ___ cabelo é ruivo, bate palmas. | cujo | cuja / que o | A amiga, cujo cabelo é ruivo, bate palmas. | L'amie aux cheveux roux applaudit. | <b>cujo</b> s'accorde avec <b>cabelo</b>, pas avec amiga.
"""),
"C1": (T_HYPO, """
geschenk | mark | O presente ___ ser uma surpresa. | deve | pode-se / há | O presente deve ser uma surpresa. | Le cadeau doit être une surprise. | Déduction : <b>dever</b>.
geschenk-2 |  | O presente vermelho ___ dos pais dele. | será | seja / foi | O presente vermelho será dos pais dele. | Le cadeau rouge vient peut-être de ses parents. | Futur de supposition : <b>será</b>.
pizza |  | A pizza ___ acabar daqui a nada. | deve | pode-se / tem | A pizza deve acabar daqui a nada. | La pizza devrait être bientôt finie. | Probable : <b>dever</b>.
torte | anna | ___ que foi a Anna que fez o bolo. | Parece | Parecem / Pareça | Parece que foi a Anna que fez o bolo. | Il paraît qu'Anna a fait le gâteau elle-même. | Le ouï-dire : <b>parece que</b>.
"""),
},
}


def lignes(bloc):
    for l in bloc.strip().splitlines():
        if l.strip() and not l.strip().startswith("#"):
            yield [c.strip() for c in l.split("|")]


def construire():
    n = 0
    for nom, couches in COUCHES.items():
        p = os.path.join(SORTIE, nom + ".json")
        doc = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {"_lisez_moi": "", "couches": {}}
        for niv, (titre, bloc) in couches.items():
            qs = []
            for cols in lignes(bloc):
                assert len(cols) == 8, "%s %s : %d colonnes : %s" % (nom, niv, len(cols), cols[2])
                f, r, q, bonne, fausses, phrase, sens, note = cols
                fausses = [x.strip() for x in fausses.split("/")]
                assert bonne not in fausses, "%s : bonne reponse parmi les fausses : %s" % (nom, q)
                assert "___" in q, "%s : question sans trou : %s" % (nom, q)
                qs.append({"q": q, "c": [bonne] + fausses, "f": f, "r": r or None, "phrase": phrase, "sens": sens, "n": note})
            doc["couches"][niv] = {"titre": titre, "qs": qs}
            n += len(qs)
        doc["couches"] = {k: doc["couches"][k] for k in ("A2", "B1", "B2", "C1") if k in doc["couches"]}
        with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    print("Couches B1-C1 : %d scenes, %d questions." % (len(COUCHES), n))


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    construire()
