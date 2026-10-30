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
"schlafzimmer": {
"B1": ("Onde ? Para onde ? — et le perfeito", """
pullover | koffer | A Anna põe a camisola ___ mala de viagem. | na | para a / à | A Anna põe a camisola na mala de viagem. | Anna met le pull dans la valise. | <b>pôr em</b> : là où la chose se retrouve.
pullover | koffer | Daqui a pouco, a camisola ___ na mala. | vai estar | vai a estar / está a ir | Daqui a pouco, a camisola vai estar na mala. | Dans un instant, le pull sera dans la valise. | Le futur proche : <b>vai estar</b>.
hut | bett | A Anna ___ o chapéu em cima da cama. | pôs | punha / põe | A Anna pôs o chapéu em cima da cama. | Anna a posé le chapeau sur le lit. | <b>pôr</b> au perfeito : <b>pôs</b>.
kamera | bett | A máquina fotográfica ___ em cima da cama. | está | põe / vai | A máquina fotográfica está em cima da cama. | L'appareil photo est sur le lit. | La position : <b>estar</b>.
ladegeraet |  | A Anna quase se ___ do carregador. | esqueceu | esquecia / esquece | A Anna quase se esqueceu do carregador. | Anna a failli oublier le chargeur. | <b>esquecer-se de</b> ; après <b>quase</b>, le pronom passe devant.
wecker |  | O despertador está ___ mesa de cabeceira. | na | à / para a | O despertador está na mesa de cabeceira. | Le réveil est sur la table de nuit. | em + a = <b>na</b>.
anna | bett | A Anna está de pé ao lado ___ cama. | da | de a / à | A Anna está de pé ao lado da cama. | Anna est debout à côté du lit. | <b>ao lado de</b> + a = <b>ao lado da</b>.
koffer | anna | Amanhã a Anna vai de avião ___ o sul. | para | ao / no | Amanhã a Anna vai de avião para o sul. | Demain, Anna part en avion vers le sud. | La destination : <b>para</b>.
"""),
"B2": (T_PASSIF, """
koffer | bett | A mala ___ está em cima da cama é azul. | que | quem / onde | A mala que está em cima da cama é azul. | La valise qui est sur le lit est bleue. | Sujet : <b>que</b>.
pass | bett | O passaporte, sem o ___ a Anna não pode viajar, está na cama. | qual | que / quem | O passaporte, sem o qual a Anna não pode viajar, está na cama. | Le passeport, sans lequel Anna ne peut pas voyager, est sur le lit. | Après une préposition : <b>o qual</b>.
anna | pullover | A mulher, ___ camisola é verde, está a pensar. | cuja | cujo / que a | A mulher, cuja camisola é verde, está a pensar. | La femme au pull vert réfléchit. | <b>cuja</b> + camisola (féminin).
koffer |  | A mala já está meio ___. | feita | feito / fazida | A mala já está meio feita. | La valise est déjà à moitié faite. | <b>fazer a mala</b> → <b>a mala está feita</b>.
koffer |  | Tudo ainda tem de ser ___ hoje. | arrumado | arrumada / arrumar | Tudo ainda tem de ser arrumado hoje. | Tout doit encore être emballé aujourd'hui. | Passif avec <b>ter de ser</b> + participe ; <b>tudo</b> → masculin.
kamera | bett | A máquina com a ___ a Anna quer tirar fotografias está na cama. | qual | que / quem | A máquina com a qual a Anna quer tirar fotografias está na cama. | L'appareil photo avec lequel Anna veut faire des photos est sur le lit. | <b>com a qual</b> (ou <b>com que</b>).
"""),
"C1": (T_HYPO, """
anna | koffer | Ela ___ estar ansiosa pela viagem. | deve | pode-se / tem | Ela deve estar ansiosa pela viagem. | Elle doit se réjouir du voyage. | Déduction : <b>dever</b> ; <b>estar ansioso por</b> = avoir hâte de.
pullover |  | ___ a camisola seja quente demais para o sul. | Talvez | Se calhar / Deve | Talvez a camisola seja quente demais para o sul. | Le pull est peut-être trop chaud pour le sud. | <b>talvez</b> + conjuntivo (<b>seja</b>).
koffer |  | Ela ___ partir amanhã de manhã. | deverá | deveria-se / deva | Ela deverá partir amanhã de manhã. | Elle décolle sans doute demain matin. | Probable : <b>deverá</b>.
bild |  | ___ que naquela praia faz calor o ano inteiro. | Dizem | Diz-se-lhe / Digam | Dizem que naquela praia faz calor o ano inteiro. | Il paraît qu'à cette plage il fait chaud toute l'année. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"hotel": {
"B1": ("Les prépositions de temps : às, a partir de, até, de… a", """
tasse |  | O pequeno-almoço é servido ___ das sete. | a partir | desde / até | O pequeno-almoço é servido a partir das sete. | Le petit-déjeuner est servi à partir de sept heures. | <b>a partir de</b> + as = <b>a partir das</b> sete.
mark |  | O Mark chega ___ sexta-feira à noite. | na | à / em a | O Mark chega na sexta-feira à noite. | Mark arrive vendredi soir. | Un jour : <b>na</b> sexta-feira (ou sans article : <b>sexta-feira</b>).
koffer | mark | Ele fica ___ domingo. | até | a / para | Ele fica até domingo. | Il reste jusqu'à dimanche. | Jusqu'à : <b>até</b>.
schluessel-2 |  | O quarto está pronto ___ três horas. | às | as / nas | O quarto está pronto às três horas. | La chambre est prête à trois heures. | L'heure : a + as = <b>às</b>.
fenster |  | ___ inverno, o hotel é calmo. | No | Em o / Ao | No inverno, o hotel é calmo. | En hiver, l'hôtel est calme. | Une saison : em + o = <b>no</b> inverno.
rezeption |  | A receção está aberta ___ sete às vinte e três. | das | de / desde as | A receção está aberta das sete às vinte e três. | La réception est ouverte de sept heures à vingt-trois heures. | De… à… : <b>das</b> … <b>às</b>.
mark |  | ___ do pequeno-almoço, o Mark vai à cidade. | Depois | Após de / Antes | Depois do pequeno-almoço, o Mark vai à cidade. | Après le petit-déjeuner, Mark va en ville. | <b>depois de</b> + o = <b>depois do</b>.
zeitung | frau | A senhora lê o jornal ___ noite. | à | na / de | A senhora lê o jornal à noite. | Le soir, la femme lit le journal. | Le moment de la journée : <b>de manhã</b>, <b>à tarde</b>, <b>à noite</b>.
"""),
"B2": ("Enquanto, assim que, enquanto não", """
mark | frau | ___ o Mark espera pela chave, a senhora lê o jornal. | Enquanto | Assim que / Logo que | Enquanto o Mark espera pela chave, a senhora lê o jornal. | Pendant que Mark attend la clé, la femme lit le journal. | Simultané : <b>enquanto</b> + indicatif.
schluessel-2 | mark | Assim que o Mark ___ a chave, sobe ao quarto. | tiver | tem / tenha | Assim que o Mark tiver a chave, sobe ao quarto. | Dès que Mark a la clé, il monte dans sa chambre. | <b>assim que</b> + action future : futuro do conjuntivo.
frau |  | A senhora fica no hotel enquanto ___. | chover | chove / chova | A senhora fica no hotel enquanto chover. | La femme reste à l'hôtel tant qu'il pleut. | <b>enquanto</b> (tant que), pour l'avenir : futuro do conjuntivo.
mann | schluessel-2 | O homem sorri ___ dá a chave ao Mark. | enquanto | assim que / quando que | O homem sorri enquanto dá a chave ao Mark. | L'homme sourit en donnant la clé à Mark. | En même temps : <b>enquanto</b>.
telefon |  | Logo que o quarto ___ pronto, a receção telefona. | estiver | está / esteja | Logo que o quarto estiver pronto, a receção telefona. | Dès que la chambre est prête, la réception appelle. | <b>logo que</b> + futuro do conjuntivo.
treppe | aufzug | Enquanto o elevador ___ avariado, os hóspedes usam a escada. | estiver | está-se / estivesse | Enquanto o elevador estiver avariado, os hóspedes usam a escada. | Tant que l'ascenseur est en panne, les clients prennent l'escalier. | <b>avariado</b> = en panne (au Portugal).
"""),
"C1": (T_HYPO, """
mark |  | Ele ___ estar ansioso pelo fim de semana. | deve | pode-se / tem | Ele deve estar ansioso pelo fim de semana. | Il doit se réjouir du week-end. | Déduction : <b>dever</b>.
frau | sofa | A senhora idosa ___ ser cliente habitual. | pode | deve de / há de | A senhora idosa pode ser cliente habitual. | La vieille dame est peut-être une habituée. | Possibilité : <b>poder</b>.
treppe |  | O quarto ___ no segundo andar. | ficará | fique / ficou-se | O quarto ficará no segundo andar. | La chambre doit être au deuxième étage. | Futur de supposition : <b>ficará</b>.
rezeption |  | Este hotel ___ o mais antigo de Lisboa. | seria | será-se / seja | Este hotel seria o mais antigo de Lisboa. | Cet hôtel serait le plus ancien de Lisbonne. | Le conditionnel de la rumeur : <b>seria</b>.
"""),
},
"flughafen": {
"B1": ("Verbe + préposition + infinitif", """
anna | flugzeug | A Anna tenciona ___ para Espanha. | voar | de voar / a voar | A Anna tenciona voar para Espanha. | Anna a l'intention de prendre l'avion pour l'Espagne. | <b>tencionar</b> + infinitif, sans préposition.
pass | frau | Ela não se esquece ___ mostrar o passaporte à senhora. | de | a / em | Ela não se esquece de mostrar o passaporte à senhora. | Elle n'oublie pas de montrer son passeport à la femme. | <b>esquecer-se de</b> + infinitif.
uhr |  | É importante ___ a horas no aeroporto. | estar | de estar / a estar | É importante estar a horas no aeroporto. | Il est important d'être à l'heure à l'aéroport. | <b>é importante</b> + infinitif, sans « de » ; <b>a horas</b> = à l'heure (au Portugal).
koffer-3 | waage | A senhora pede à Anna ___ pôr a mala na balança. | para | de / a | A senhora pede à Anna para pôr a mala na balança. | La femme demande à Anna de mettre la valise sur la balance. | <b>pedir para</b> + infinitif (ou <b>pedir que</b> + conjuntivo).
pilot | zeitung | O piloto não tem tempo ___ ler o jornal. | para | de / a | O piloto não tem tempo para ler o jornal. | Le pilote n'a pas le temps de lire le journal. | <b>ter tempo para</b> + infinitif.
rucksack | anna | A Anna tenta não se ___ da mochila. | esquecer | esquecer-se / esquece | A Anna tenta não se esquecer da mochila. | Anna essaie de ne pas oublier le sac à dos. | <b>tentar</b> + infinitif ; après <b>não</b>, le pronom devant.
flugzeug | anna | A Anna espera ___ a horas. | chegar | de chegar / que chegar | A Anna espera chegar a horas. | Anna espère arriver à l'heure. | <b>esperar</b> + infinitif (même sujet).
pass | frau | A Anna tem ___ mostrar o passaporte à senhora. | de | que de / a | A Anna tem de mostrar o passaporte à senhora. | Anna doit montrer son passeport à la femme. | <b>ter de</b> + infinitif.
"""),
"B2": ("Les questions indirectes : se, onde, quando, quanto", """
anna | flugzeug | A Anna pergunta à senhora ___ o avião está a horas. | se | que / quando se | A Anna pergunta à senhora se o avião está a horas. | Anna demande à la femme si l'avion est à l'heure. | Question oui / non rapportée : <b>se</b>.
koffer-3 | waage | Ela não sabe ___ pesa a mala. | quanto | quanta / o quanto que | Ela não sabe quanto pesa a mala. | Elle ne sait pas combien pèse la valise. | <b>quanto</b> ; le sujet se place souvent après le verbe.
pilot | flugzeug | O piloto sabe ___ está o avião. | onde | aonde que / se | O piloto sabe onde está o avião. | Le pilote sait où est l'avion. | <b>onde</b> (lieu où l'on est).
frau | koffer | A senhora pergunta ___ a Anna tem bagagem de mão. | se | que / quem | A senhora pergunta se a Anna tem bagagem de mão. | La femme demande si Anna a un bagage à main. | <b>perguntar se</b>.
uhr | flugzeug | A Anna quer saber ___ o avião parte. | quando | se quando / que | A Anna quer saber quando o avião parte. | Anna veut savoir quand l'avion décolle. | <b>quando</b>.
zeitung |  | Sabes ___ é o jornal? | de quem | quem / cujo | Sabes de quem é o jornal? | Tu sais à qui est le journal ? | L'appartenance : <b>de quem é</b>.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ estar ansiosa pela viagem. | deve | pode-se / tem de ser | Ela deve estar ansiosa pela viagem. | Elle doit se réjouir du voyage. | Déduction : <b>dever</b>.
pilot | flugzeug | ___ ser o piloto do avião dela. | Pode | Deve de / Há | Pode ser o piloto do avião dela. | Le pilote pilote peut-être son avion. | Possibilité : <b>pode ser</b>.
koffer-3 | waage | A mala grande ___ pesada demais. | estará | esteja / estava-se | A mala grande estará pesada demais. | La grande valise est sans doute trop lourde. | Futur de supposition : <b>estará</b>.
fenster |  | Este aeroporto ___ o mais moderno do país. | seria | será-se / seja | Este aeroporto seria o mais moderno do país. | Cet aéroport serait le plus moderne du pays. | Le conditionnel de la rumeur : <b>seria</b>.
"""),
},
"baeckerei": {
"B1": ("Le possessif : o seu, dele, dela", """
anna | nachbar | A Anna cumprimenta o ___ vizinho. | seu | sua / dele | A Anna cumprimenta o seu vizinho. | Anna salue son voisin. | <b>o seu</b> + nom masculin : son (à elle) ; plus clair : <b>o vizinho dela</b>.
nachbar | zeitung | O vizinho lê o jornal. O jornal é ___. | dele | seu dele / dela | O jornal é dele. | Le journal est à lui. | Pour lever le doute : <b>dele</b> (à lui), <b>dela</b> (à elle).
frau |  | A empregada conhece ___ os clientes do bairro. | todos | toda / tudo | A empregada conhece todos os clientes do bairro. | La vendeuse connaît chaque client du quartier. | <b>todos os</b> + nom pluriel.
hund | nachbar | O cão é ___ senhor que está à mesa. | do | o / ao | O cão é do senhor que está à mesa. | Le chien appartient au monsieur à la table. | L'appartenance : <b>ser de</b> (de + o = <b>do</b>).
broetchen | anna | A Anna compra papos-secos para o ___ colega. | seu | sua / dela | A Anna compra papos-secos para o seu colega. | Anna achète des petits pains pour son collègue. | <b>o seu colega</b> (ou <b>o colega dela</b>).
frau |  | Sabes o nome ___ empregada? | da | de a / à | Sabes o nome da empregada? | Tu connais le nom de la vendeuse ? | de + a = <b>da</b>.
hund | nachbar | O cão espera pelo ___ dono. | seu | sua / deles | O cão espera pelo seu dono. | Le chien attend son maître. | <b>esperar por</b> + o seu = <b>pelo seu</b>.
schalter |  | A padaria é muito querida por todos ___ vizinhos. | os | dos / aos | A padaria é muito querida por todos os vizinhos. | La boulangerie est appréciée de tous les voisins. | <b>todos os</b> vizinhos.
"""),
"B2": ("Le mais-que-perfeito : tinha feito", """
frau | brot | Antes de a Anna chegar, a empregada já ___ cozido o pão. | tinha | tem / teve | Antes de a Anna chegar, a empregada já tinha cozido o pão. | Avant qu'Anna arrive, la vendeuse avait cuit le pain. | Le passé avant le passé : <b>tinha</b> + participe.
nachbar | anna | Quando a Anna entrou, o vizinho já se tinha ___. | sentado | sentada / sentou | Quando a Anna entrou, o vizinho já se tinha sentado. | Quand Anna est entrée, le voisin s'était déjà assis. | <b>sentar-se</b> → <b>tinha-se sentado</b> ; après <b>já</b>, <b>se tinha sentado</b>.
tasse-2 | zeitung | Depois de ___ o café, leu o jornal. | ter bebido | tinha bebido / beber-se | Depois de ter bebido o café, leu o jornal. | Après avoir bu le café, il a lu le journal. | Après une préposition : <b>ter</b> + participe.
hund | tasse-2 | O cão já ___ adormecido antes de o café chegar. | tinha | tem / era | O cão já tinha adormecido antes de o café chegar. | Le chien s'était déjà endormi avant que le café arrive. | Toujours <b>ter</b>, jamais ser.
frau |  | Quando a loja abriu, a empregada já tinha ___ três horas. | trabalhado | trabalhada / trabalhou | Quando a loja abriu, a empregada já tinha trabalhado três horas. | Quand le magasin a ouvert, la vendeuse avait déjà travaillé trois heures. | Le participe ne s'accorde pas avec ter.
muenze | broetchen | A Anna já tinha ___ os papos-secos quando o telemóvel tocou. | pago | pagado / pagos | A Anna já tinha pago os papos-secos quando o telemóvel tocou. | Anna avait déjà payé les petits pains quand son téléphone a sonné. | <b>pagar</b> → <b>pago</b>.
"""),
"C1": (T_HYPO, """
broetchen | anna | Os papos-secos ___ estar fresquinhos. | devem | podem-se / têm | Os papos-secos devem estar fresquinhos. | Les petits pains doivent être frais. | Déduction : <b>dever</b>, accordé au pluriel.
hund | nachbar | ___ que o cão seja do vizinho. | Pode ser | Deve ser / Se calhar | Pode ser que o cão seja do vizinho. | Le chien appartient peut-être au voisin. | <b>pode ser que</b> + conjuntivo.
brot |  | O pão ___ de hoje de manhã. | será | seja / foi-se | O pão será de hoje de manhã. | Le pain date sans doute de ce matin. | Futur de supposition : <b>será</b>.
schalter |  | Esta padaria ___ a melhor do bairro. | seria | será-se / seja | Esta padaria seria a melhor do bairro. | Cette boulangerie serait la meilleure du quartier. | Le conditionnel de la rumeur : <b>seria</b>.
"""),
},
"apotheke": {
"B1": ("La négation : não, nem, nenhum, já não", """
mark |  | O Mark não tem febre, ___ uma constipação. | só | nem / nenhuma | O Mark não tem febre, só uma constipação. | Mark n'a pas de fièvre, juste un rhume. | Le portugais dit <b>não tem febre</b> : pas d'article ; <b>só</b> = seulement.
medikament-6 |  | Os comprimidos ___ são caros. | não | nem / nenhum | Os comprimidos não são caros. | Les comprimés ne sont pas chers. | <b>não</b> devant le verbe.
mark |  | O Mark não tem tempo ___ ir ao médico. | para | de / a | O Mark não tem tempo para ir ao médico. | Mark n'a pas le temps d'aller chez le médecin. | <b>ter tempo para</b>.
mann | stuhl | O senhor idoso não espera ___. | muito | nada / nenhum | O senhor idoso não espera muito. | Le vieux monsieur n'attend pas longtemps. | Pas longtemps : <b>não … muito</b>.
medikament-6 |  | O Mark não toma os comprimidos ___ café. | com | sem / nem | O Mark não toma os comprimidos com café. | Mark ne prend pas les comprimés avec du café. | <b>com café</b>, sans article.
pflaster | frau | A farmacêutica ___ tem pensos. | já não | ainda não / não já | A farmacêutica já não tem pensos. | La pharmacienne n'a plus de pansements. | Ne… plus : <b>já não</b>.
rezept |  | Esta ___ é a minha receita! | não | nem / nenhuma | Esta não é a minha receita! | Ce n'est pas mon ordonnance ! | <b>não</b> avant le verbe ; <b>a receita</b> = l'ordonnance.
flasche-5 |  | O Mark não comprou ___ xarope para a tosse. | nenhum | nada / nem | O Mark não comprou nenhum xarope para a tosse. | Mark n'a pas acheté de sirop contre la toux. | <b>nenhum</b> renforce la négation (ou simplement : <b>não comprou xarope</b>).
"""),
"B2": ("Le discours rapporté", """
frau | mark | A farmacêutica diz que o Mark ___ uma constipação forte. | tem | tenha / tivesse | A farmacêutica diz que o Mark tem uma constipação forte. | La pharmacienne dit que Mark a un gros rhume. | Verbe introducteur au présent : l'indicatif ne change pas.
medikament-6 | frau | Ela diz-lhe que ___ os comprimidos três vezes por dia. | tome | toma / tomasse | Ela diz-lhe que tome os comprimidos três vezes por dia. | Elle dit qu'il doit prendre les comprimés trois fois par jour. | Une consigne rapportée : <b>dizer que</b> + conjuntivo.
mark |  | O médico disse que o Mark não ___ contagioso. | era | é-se / seja | O médico disse que o Mark não era contagioso. | Le médecin a dit que Mark n'est pas contagieux. | Verbe introducteur au passé : présent → imperfeito.
taschentuch | mark | O Mark diz que ___ tosse há três dias. | tem | tenha / tinha-se | O Mark diz que tem tosse há três dias. | Mark dit qu'il tousse depuis trois jours. | <b>ter tosse</b> = tousser ; <b>há três dias</b> = depuis trois jours.
flasche-5 | frau | A farmacêutica explica que o xarope ___ a tosse. | alivia | alivie / aliviasse | A farmacêutica explica que o xarope alivia a tosse. | La pharmacienne explique que le sirop aide contre la toux. | Un fait rapporté au présent : indicatif.
mann | stuhl | O senhor idoso disse que ___ há muito tempo. | estava à espera | está à espera / esteja à espera | O senhor idoso disse que estava à espera há muito tempo. | Le vieux monsieur a dit qu'il attendait depuis longtemps. | Au passé : <b>estava à espera</b> (estar à espera = attendre).
"""),
"C1": (T_HYPO, """
mark | taschentuch | Ele ___ estar constipado. | deve | pode-se / tem | Ele deve estar constipado. | Il doit être enrhumé. | Déduction : <b>dever</b> ; <b>constipado</b> = enrhumé.
mann | stuhl | ___ o senhor esteja à espera do medicamento. | Talvez | Deve / Se calhar | Talvez o senhor esteja à espera do medicamento. | Le vieux monsieur attend peut-être son médicament. | <b>talvez</b> + conjuntivo.
mark |  | O Mark ___ estar bom daqui a dois dias. | deverá | deveria-se / deva | O Mark deverá estar bom daqui a dois dias. | Mark devrait être rétabli dans deux jours. | Probable : <b>deverá</b>.
schalter |  | Esta farmácia ___ a mais antiga do bairro. | seria | será-se / seja | Esta farmácia seria a mais antiga do bairro. | Cette pharmacie serait la plus ancienne du quartier. | Le conditionnel de la rumeur : <b>seria</b>.
"""),
},
"klassenzimmer": {
"B1": ("Pôr, estar, pendurar : le geste et la position", """
rucksack | tisch | A mochila ___ debaixo da mesa. | está | pôs / põe | A mochila está debaixo da mesa. | Le sac à dos est sous la table. | La position : <b>estar</b>.
rucksack | anna | A Anna ___ a mochila debaixo da mesa. | pôs | está / estava | A Anna pôs a mochila debaixo da mesa. | Anna a mis son sac à dos sous la table. | Le geste : <b>pôr</b> → <b>pôs</b>.
handy | schreibtisch | O telemóvel está ___ secretária. | em cima da | em cima a / por cima a | O telemóvel está em cima da secretária. | Le téléphone est sur le bureau. | <b>em cima de</b> + a = <b>em cima da</b>.
handy | lehrer | O professor ___ o telemóvel em cima da secretária. | pousou | pousava / pousa | O professor pousou o telemóvel em cima da secretária. | Le professeur a posé son téléphone sur le bureau. | <b>pousar</b> → <b>pousou</b>.
anna | mark | A Anna está sentada ao lado ___ Mark. | do | de / ao | A Anna está sentada ao lado do Mark. | Anna est assise à côté de Mark. | Devant un prénom, l'article : <b>do</b> Mark.
jacke | tuer | O Mark ___ o casaco na porta. | pendurou | pendurava / pendura | O Mark pendurou o casaco na porta. | Mark a accroché sa veste à la porte. | Perfeito : <b>pendurou</b>.
jacke | tuer | O Mark ___ o casaco na porta. | pendura | pendurou-se / pendure | O Mark pendura o casaco na porta. | Mark accroche sa veste à la porte. | Présent : <b>pendura</b>.
jacke | tuer | Agora o casaco está ___ na porta. | pendurado | pendurada / pendurar | Agora o casaco está pendurado na porta. | La veste est maintenant accrochée à la porte. | <b>estar pendurado</b>, accordé (o casaco).
"""),
"B2": ("Relatives et passif d'état", """
frau |  | A mulher ___ leva um livro debaixo do braço ainda está de pé. | que | quem / cuja | A mulher que leva um livro debaixo do braço ainda está de pé. | La femme qui porte un livre sous le bras est encore debout. | Sujet : <b>que</b>.
lehrer |  | O homem ___ está em frente do quadro é o professor. | que | quem / onde | O homem que está em frente do quadro é o professor. | L'homme qui est devant le tableau est le professeur. | Sujet : <b>que</b>.
lehrer | brille | O homem, ___ óculos estão na ponta do nariz, é o professor. | cujos | cujas / que os | O homem, cujos óculos estão na ponta do nariz, é o professor. | L'homme dont les lunettes sont sur le nez est le professeur. | <b>os óculos</b> (masc. pluriel) → <b>cujos</b>.
anna | heft | A aluna, ___ caderno está aberto na mesa, chama-se Anna. | cujo | cuja / que o | A aluna, cujo caderno está aberto na mesa, chama-se Anna. | La participante dont le cahier est ouvert sur la table s'appelle Anna. | <b>cujo</b> + caderno (masculin).
tisch | rucksack | A mesa debaixo da ___ está a mochila é de madeira. | qual | que / quem | A mesa debaixo da qual está a mochila é de madeira. | La table sous laquelle est le sac à dos est en bois. | <b>debaixo da qual</b>.
tafel |  | O quadro já está ___. | apagado | apagada / apagou | O quadro já está apagado. | Le tableau est déjà effacé. | État : <b>estar</b> + participe accordé (o quadro).
"""),
"C1": (T_HYPO, """
anna | mark | O Mark e a Anna ___ conhecer-se. | devem | deve / podem-se | O Mark e a Anna devem conhecer-se. | Mark et Anna doivent se connaître. | Déduction : <b>devem</b>, au pluriel.
frau |  | A mulher de vestido ___ ter chegado atrasada. | pode | pode-se / há | A mulher de vestido pode ter chegado atrasada. | La femme en robe est peut-être arrivée en retard. | Possibilité sur le passé : <b>pode ter</b> + participe.
lehrer |  | O professor ___ português há muito tempo. | ensinará | ensine / ensinou-se | O professor ensinará português há muito tempo. | Le professeur enseigne sans doute le portugais depuis longtemps. | Futur de supposition : <b>ensinará</b>.
lehrer |  | ___ que o professor é do Porto. | Dizem | Diz-se-lhe / Digam | Dizem que o professor é do Porto. | Il paraît que le professeur vient de Porto. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"buero": {
"B1": ("Les verbes du bureau : ligar, desligar, tomar nota", """
telefon | mark | O Mark ___ a um cliente. | liga | chama / telefona-se | O Mark liga a um cliente. | Mark appelle un client. | Téléphoner : <b>ligar a alguém</b> (ou telefonar a).
heft | mark | Ele ___ nota do número. | toma | faz / tira | Ele toma nota do número. | Il note le numéro. | Noter : <b>tomar nota de</b>.
telefon |  | O Mark ___ ao cliente. | ligou | ligava / liga-se | O Mark ligou ao cliente. | Mark a appelé le client. | Perfeito : <b>ligou</b>.
drucker | frau | A colega ___ uma carta. | imprime | imprima / imprimiu-se | A colega imprime uma carta. | La collègue imprime une lettre. | <b>imprimir</b>.
telefon |  | Podes ___ amanhã, por favor? | ligar-me de volta | me ligar de volta / ligar-me-volta | Podes ligar-me de volta amanhã, por favor? | Tu peux me rappeler demain, s'il te plaît ? | Rappeler : <b>ligar de volta</b> (ou <b>voltar a ligar</b>) ; pronom après l'infinitif.
uhr | mark | Às cinco, o Mark ___ de trabalhar. | para | deixa-se / acaba-se | Às cinco, o Mark para de trabalhar. | À cinq heures, Mark arrête de travailler. | <b>parar de</b> + infinitif (sans accent depuis 1990 : para).
frau | tafel | A colega ___ uma reunião. | prepara | prepare / preparou-se | A colega prepara uma reunião. | La collègue prépare une réunion. | <b>preparar</b>.
telefon |  | O Mark vai ___ o telefone já. | desligar | ligar / desligar-se | O Mark vai desligar o telefone já. | Mark va raccrocher tout de suite. | Raccrocher : <b>desligar</b>.
"""),
"B2": (T_PASSIF, """
mark | telefon | O homem ___ está ao telefone chama-se Mark. | que | quem / qual | O homem que está ao telefone chama-se Mark. | L'homme qui est au téléphone s'appelle Mark. | Sujet : <b>que</b>.
frau |  | A colega, ___ cabelo é grisalho, lê uma carta. | cujo | cuja / que o | A colega, cujo cabelo é grisalho, lê uma carta. | La collègue aux cheveux gris lit une lettre. | <b>cujo</b> s'accorde avec <b>cabelo</b>.
regal | ordner | A estante ___ estão as pastas é de metal. | onde | que / cuja | A estante onde estão as pastas é de metal. | L'étagère où sont les classeurs est en métal. | Le lieu : <b>onde</b>.
drucker |  | A carta está a ser ___. | impressa | imprimida / impresso | A carta está a ser impressa. | La lettre est en train d'être imprimée. | <b>imprimir</b> : participe court <b>impresso</b> avec ser / estar, accordé.
heft |  | O caderno já está meio ___. | preenchido | preenchida / preencher | O caderno já está meio preenchido. | Le cahier est déjà à moitié rempli. | État : <b>estar</b> + participe accordé.
tafel |  | O quadro no ___ estão desenhadas setas está pendurado na parede. | qual | que / onde que | O quadro no qual estão desenhadas setas está pendurado na parede. | Le tableau sur lequel sont dessinées des flèches est accroché au mur. | <b>no qual</b>.
"""),
"C1": (T_HYPO, """
heft | mark | A conversa ___ ser importante. | deve | pode-se / tem | A conversa deve ser importante. | La conversation doit être importante. | Déduction : <b>dever</b>.
frau |  | A colega ___ ser a chefe dele. | pode | deve de / há | A colega pode ser a chefe dele. | La collègue est peut-être sa cheffe. | Possibilité : <b>poder</b>.
mark |  | O Mark ___ conseguir um lugar depois do estágio. | deverá | deveria-se / deva | O Mark deverá conseguir um lugar depois do estágio. | Mark devrait obtenir un poste après le stage. | Probable : <b>deverá</b>.
fenster |  | ___ que a empresa vai mudar de instalações em breve. | Consta | Constam / Conste | Consta que a empresa vai mudar de instalações em breve. | Il paraît que l'entreprise va bientôt déménager. | Le ouï-dire, soutenu : <b>consta que</b>.
"""),
},
"bibliothek": {
"B1": ("Les verbes à préposition", """
anna | buch | A Anna interessa-se ___ história. | pela | na / à | A Anna interessa-se pela história. | Anna s'intéresse à l'histoire. | <b>interessar-se por</b> : por + a = <b>pela</b>.
anna |  | Ela pensa ___ exame. | no | ao / do | Ela pensa no exame. | Elle pense à son examen. | <b>pensar em</b> : em + o = <b>no</b>.
anna |  | Ela está à espera ___ amiga. | da | pela / à | Ela está à espera da amiga. | Elle attend son amie. | <b>estar à espera de</b> (ou <b>esperar por</b>).
student |  | O estudante sonha ___ as férias. | com | de / em | O estudante sonha com as férias. | L'étudiant rêve des vacances. | <b>sonhar com</b>.
heft | anna | A Anna escreve um trabalho ___ o Muro de Berlim. | sobre | de / em | A Anna escreve um trabalho sobre o Muro de Berlim. | Anna écrit un travail sur le mur de Berlin. | <b>sobre</b> = au sujet de.
anna |  | Ela já está ansiosa ___ fim de semana. | pelo | do / ao | Ela já está ansiosa pelo fim de semana. | Elle se réjouit déjà du week-end. | <b>estar ansioso por</b> = avoir hâte de : <b>pelo</b>.
student |  | ___ é que estás à espera? — Da minha amiga. | De quem | Quem / Por que | De quem é que estás à espera? — Da minha amiga. | Qui attends-tu ? — Mon amie. | La préposition passe devant l'interrogatif : <b>de quem</b>.
student |  | O estudante concentra-se ___ livro. | no | ao / do | O estudante concentra-se no livro. | L'étudiant se concentre sur son livre. | <b>concentrar-se em</b>.
"""),
"B2": ("Relatives, passif et participes", """
anna | buch | A estudante ___ lê o livro chama-se Anna. | que | quem / qual | A estudante que lê o livro chama-se Anna. | L'étudiante qui lit le livre s'appelle Anna. | Sujet : <b>que</b>.
student |  | O estudante, ___ cabelo é encaracolado, lê na outra mesa. | cujo | cuja / que o | O estudante, cujo cabelo é encaracolado, lê na outra mesa. | L'étudiant aux cheveux bouclés lit à l'autre table. | <b>cujo</b> + cabelo.
regal | leiter | A estante à ___ está encostada a escada é muito alta. | qual | que / quem | A estante à qual está encostada a escada é muito alta. | L'étagère contre laquelle est l'échelle est très haute. | <b>encostado a</b> + a qual = <b>à qual</b>.
student |  | Aqui não ___ alto. | se fala | fala-se / se falam | Aqui não se fala alto. | Ici, on ne parle pas fort. | Le se impersonnel ; après <b>não</b>, devant.
buch |  | O livro já está lido ___ metade. | até meio | a meia / pela metade de | O livro já está lido até meio. | Le livre est déjà lu à moitié. | À moitié : <b>até meio</b>, <b>a meio</b>.
lampe | buch-2 | O candeeiro ___ está ao lado dos livros. | aceso | acendido / acesa | O candeeiro aceso está ao lado dos livros. | La lampe allumée est à côté des livres. | Participe court comme adjectif : <b>aceso</b> (o candeeiro).
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ ter um exame em breve. | deve | pode-se / tem | Ela deve ter um exame em breve. | Elle doit avoir un examen bientôt. | Déduction : <b>dever</b>.
student |  | ___ que o estudante seja do curso da Anna. | Pode ser | Deve ser / Se calhar | Pode ser que o estudante seja do curso da Anna. | L'étudiant est peut-être dans le cours d'Anna. | <b>pode ser que</b> + conjuntivo.
fenster |  | Lá fora ___ estar bastante frio. | deve | pode-se / tem | Lá fora deve estar bastante frio. | Dehors, il doit faire plutôt froid. | <b>dever</b> : probable.
regal |  | Esta biblioteca ___ mais de um milhão de livros. | teria | terá-se / tenha | Esta biblioteca teria mais de um milhão de livros. | Cette bibliothèque aurait plus d'un million de livres. | Le conditionnel de la rumeur.
"""),
},
"museum": {
"B1": ("Qual ? Que tipo de ? — les interrogatifs", """
skulptur | anna | ___ escultura desenha a Anna? — A do cão. | Que | Qual de / Quanta | Que escultura desenha a Anna? — A do cão. | Quelle sculpture Anna dessine-t-elle ? — Celle du chien. | Devant un nom : <b>que</b> (ou <b>qual</b> + de) ; <b>a do cão</b> = celle du chien.
gemaelde |  | ___ é o quadro de que mais gostas? — O do barco. | Qual | Que / Quem | Qual é o quadro de que mais gostas? — O do barco. | Quel tableau te plaît le plus ? — Celui avec le bateau. | Devant <b>é</b> : <b>qual</b>.
gemaelde-6 |  | Em ___ sala está o cavalo? — Na primeira sala. | que | qual / quê | Em que sala está o cavalo? — Na primeira sala. | Dans quelle salle est le cheval ? — Dans la première salle. | Préposition + <b>que</b> + nom.
gemaelde-3 |  | Que ___ de quadro é este? — Um retrato. | tipo | género de / qual | Que tipo de quadro é este? — Um retrato. | Quel genre de tableau est-ce ? — Un portrait. | <b>que tipo de</b> = quel genre de.
jacke-2 | student | Que casaco ___ o estudante? — Um casaco castanho. | veste | traz-se / veste-se | Que casaco veste o estudante? — Um casaco castanho. | Quel genre de veste porte l'étudiant ? — Une veste marron. | Après un interrogatif, le sujet suit souvent le verbe.
bleistift | anna | Com ___ desenha a Anna? — Com um lápis. | que | qual / quê de | Com que desenha a Anna? — Com um lápis. | Avec quoi Anna dessine-t-elle ? — Avec un crayon à papier. | Préposition + <b>que</b>.
mann | tuer | ___ homem está sentado junto à porta? — O de farda. | Que | Qual de / Quem | Que homem está sentado junto à porta? — O de farda. | Quel homme est assis près de la porte ? — L'homme en uniforme. | <b>que</b> + nom ; <b>a farda</b> = l'uniforme.
mantel | anna | ___ é o sobretudo da Anna? — O cinzento, no banco. | Qual | Que / Quem | Qual é o sobretudo da Anna? — O cinzento, no banco. | Quel manteau est à Anna ? — Le manteau gris sur le banc. | <b>qual é</b> ; « gris » au Portugal : <b>cinzento</b>.
"""),
"B2": ("La manière : a + infinitif, ao + infinitif, gerúndio", """
anna | skulptur | A Anna aprende ___ a escultura. | desenhando | a desenhar-se / desenhada | A Anna aprende desenhando a escultura. | Anna apprend en dessinant la sculpture. | La manière : le gérondif (<b>desenhando</b>), vivant au Portugal dans cet emploi.
kopfhoerer | student | O estudante aprende mais sobre o quadro ___ os auscultadores. | usando | a usar-se / usado | O estudante aprende mais sobre o quadro usando os auscultadores. | L'étudiant en apprend plus sur le tableau en utilisant son casque. | Gérondif de manière : <b>usando</b>.
gemaelde-2 |  | Protegem-se os quadros não ___ tocando. | lhes | os / nos | Protegem-se os quadros não lhes tocando. | On protège les tableaux en ne les touchant pas. | <b>tocar em</b> / <b>tocar a</b> : <b>lhes</b> ; après não, devant.
mann |  | O homem vigia a sala ___ todos os visitantes. | observando | a observar-se / observado | O homem vigia a sala observando todos os visitantes. | L'homme surveille la salle en observant tous les visiteurs. | Gérondif : <b>observando</b>.
skulptur | anna | A Anna memoriza a escultura ___ desenhá-la. | ao | a / por | A Anna memoriza a escultura ao desenhá-la. | Anna retient la sculpture en la dessinant. | <b>ao</b> + infinitif : en (au moment où).
tuer |  | Poupa-se dinheiro ___ ao museu ao domingo. | indo | ir / a ir-se | Poupa-se dinheiro indo ao museu ao domingo. | On économise de l'argent en allant au musée le dimanche. | Gérondif : <b>indo</b>.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ adorar arte. | deve | pode-se / tem | Ela deve adorar arte. | Elle doit aimer l'art. | Déduction : <b>dever</b>.
student |  | O rapaz ___ estudar Belas-Artes. | pode | deve de / há | O rapaz pode estudar Belas-Artes. | Le jeune homme étudie peut-être l'art. | Possibilité : <b>poder</b>.
mann | tuer | O homem junto à porta ___ sentado aqui todos os dias. | estará | esteja / estava-se | O homem junto à porta estará sentado aqui todos os dias. | L'homme près de la porte est sans doute assis ici tous les jours. | Futur de supposition : <b>estará</b>.
gemaelde |  | O quadro do barco ___ muito valioso. | seria | será-se / seja | O quadro do barco seria muito valioso. | Le tableau du bateau aurait beaucoup de valeur. | Le conditionnel de la rumeur.
"""),
},
"musik": {
"B1": ("Saber, poder, ter de, querer", """
mark |  | O Mark já ___ tocar três acordes. | sabe | pode / conhece | O Mark já sabe tocar três acordes. | Mark sait déjà jouer trois accords. | Une compétence apprise : <b>saber</b> + infinitif.
gitarre |  | Ele ___ de praticar todos os dias. | tem | deve / precisa | Ele tem de praticar todos os dias. | Il doit s'exercer tous les jours. | L'obligation : <b>ter de</b>.
frau |  | Na aula não se ___ falar ao telemóvel. | pode | sabe / deve-se | Na aula não se pode falar ao telemóvel. | En cours, on n'a pas le droit de téléphoner. | La permission : <b>poder</b>.
mark |  | Mais tarde, o Mark ___ tocar numa banda. | quer | sabe / pode-se | Mais tarde, o Mark quer tocar numa banda. | Mark veut plus tard jouer dans un groupe. | La volonté : <b>querer</b>.
frau | mark | A senhora gostava que o Mark ___ mais devagar. | tocasse | toque / toca | A senhora gostava que o Mark tocasse mais devagar. | La femme voudrait que Mark joue plus lentement. | <b>gostava que</b> + conjuntivo imperfeito.
gitarre |  | Não ___ segurar a guitarra com tanta força. | deves | tens / sabes | Não deves segurar a guitarra com tanta força. | Tu ne dois pas tenir la guitare aussi fort. | Un conseil : <b>dever</b>.
note |  | O Mark ainda não ___ ler bem as notas. | sabe | pode / conhece | O Mark ainda não sabe ler bem as notas. | Mark ne sait pas encore bien lire les notes. | <b>saber</b> + infinitif.
fenster |  | ___ abrir a janela? | Posso | Sei / Tenho | Posso abrir a janela? | Puis-je ouvrir la fenêtre ? | Demander la permission : <b>posso</b>.
"""),
"B2": ("L'adjectif : accord et place", """
gitarre | mark | O Mark toca numa guitarra ___. | nova | novo / novas | O Mark toca numa guitarra nova. | Mark joue sur une nouvelle guitare. | <b>a guitarra</b> → <b>nova</b>, après le nom.
schal | frau | A senhora usa um cachecol ___. | roxo | roxa / roxos | A senhora usa um cachecol roxo. | La femme porte une écharpe violette. | <b>o cachecol</b> est masculin : <b>roxo</b>.
klavier |  | O piano ___ está encostado à parede. | preto | preta / pretos | O piano preto está encostado à parede. | Le piano noir est contre le mur. | <b>o piano</b> → <b>preto</b>.
geige | schrank | Em cima do armário está um violino ___. | antigo | antiga / velhos | Em cima do armário está um violino antigo. | Sur l'armoire, il y a un vieux violon. | <b>antigo</b> (ancien, de valeur) ; <b>velho</b> (vieux, usé).
lampe-2 | fenster | Ao lado da janela ___ está um candeeiro. | grande | grando / grandes | Ao lado da janela grande está um candeeiro. | À côté de la grande fenêtre, il y a une lampe. | <b>grande</b> ne change pas au féminin.
mark |  | O Mark veste uma t-shirt ___. | verde | verda / verdes | O Mark veste uma t-shirt verde. | Mark porte un t-shirt vert. | <b>verde</b> : même forme au masculin et au féminin.
"""),
"C1": (T_HYPO, """
mark |  | O acorde ___ ser difícil. | deve | pode-se / tem | O acorde deve ser difícil. | L'accord doit être difficile. | Déduction : <b>dever</b>.
geige | frau | ___ que o violino seja da professora. | Pode ser | Deve ser / Se calhar | Pode ser que o violino seja da professora. | Le violon appartient peut-être à la professeure. | <b>pode ser que</b> + conjuntivo.
gitarre | mark | Daqui a uns meses, o Mark ___ tocar bem. | deverá | deveria-se / deva | Daqui a uns meses, o Mark deverá tocar bem. | Mark devrait bien jouer dans quelques mois. | Probable : <b>deverá</b>.
frau |  | A professora ___ tocado numa orquestra. | teria | terá-se / tenha | A professora teria tocado numa orquestra. | Il paraît que la professeure jouait autrefois dans un orchestre. | La rumeur sur le passé : <b>teria</b> + participe.
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
