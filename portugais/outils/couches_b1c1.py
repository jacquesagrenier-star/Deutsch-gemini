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
T_MARCHE = "Faire ses courses : quantités et prix"

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
"familie": {
"B1": ("Les possessifs : o pai dela, o seu copo", """
vater | anna | O pai ___ serve batatas. | dela | seu / dele | O pai dela serve batatas. | Son père sert des pommes de terre. | Pour dire « à elle » sans doute possible : <b>dela</b>, après le nom.
bruder | wasser | O irmão deita água no ___ copo. | seu | sua / seus | O irmão deita água no seu copo. | Le frère verse de l'eau dans son verre. | <b>o seu</b> + copo (masculin) ; <b>deitar</b> = verser, au Portugal.
mutter | baby | A mãe segura o ___ bebé. | seu | sua / dele | A mãe segura o seu bebé. | La mère tient son bébé. | <b>o seu bebé</b> (ou <b>o bebé dela</b>).
opa |  | O avô fala da ___ juventude. | sua | seu / dele | O avô fala da sua juventude. | Le grand-père raconte sa jeunesse. | <b>a juventude</b> → <b>a sua</b> ; de + a sua = <b>da sua</b>.
oma | opa | A avó ouve o ___. | marido | seu marido dela / marido seu | A avó ouve o marido. | La grand-mère écoute son mari. | Pour la famille proche, le portugais se passe souvent du possessif : <b>o marido</b>.
anna | bruder | A Anna e o irmão adoram os ___ avós. | seus | suas / deles seus | A Anna e o irmão adoram os seus avós. | Anna et son frère aiment leurs grands-parents. | <b>os seus</b> + avós (masculin pluriel).
opa |  | Almoçamos todos os domingos em casa dos ___ avós. | nossos | nossas / nosso | Almoçamos todos os domingos em casa dos nossos avós. | Nous mangeons chaque dimanche chez nos grands-parents. | <b>em casa de</b> = chez ; de + os nossos = <b>dos nossos</b>.
katze | stuhl | O gato dorme na ___ cadeira. | sua | seu / dele | O gato dorme na sua cadeira. | Le chat dort sur sa chaise. | <b>a cadeira</b> → <b>a sua</b> ; em + a sua = <b>na sua</b>.
"""),
"B2": ("De : l'appartenance et la matière", """
vater |  | Este é o prato ___ pai. | do | de o / ao | Este é o prato do pai. | C'est l'assiette du père. | L'appartenance : de + o = <b>do</b>.
baby | mutter | O bebé está sentado ao colo ___ mãe. | da | de a / à | O bebé está sentado ao colo da mãe. | Le bébé est assis sur les genoux de la mère. | <b>ao colo de</b> = sur les genoux de.
opa |  | A história ___ avô tem muita graça. | do | de o / ao | A história do avô tem muita graça. | L'histoire du grand-père est drôle. | <b>ter graça</b> = être drôle.
fenster |  | Apesar ___ sol, comem lá dentro. | do | de o / o | Apesar do sol, comem lá dentro. | Malgré le soleil, ils mangent à l'intérieur. | <b>apesar de</b> + o = <b>apesar do</b>.
blume |  | A cor ___ túlipas é amarela. | das | de as / às | A cor das túlipas é amarela. | La couleur des tulipes est jaune. | de + as = <b>das</b>.
fenster |  | A janela ___ sala de jantar é grande. | da | de a / na | A janela da sala de jantar é grande. | La fenêtre de la salle à manger est grande. | de + a = <b>da</b>.
"""),
"C1": (T_HYPO, """
opa |  | O avô ___ estar a contar uma história engraçada. | deve | pode-se / tem | O avô deve estar a contar uma história engraçada. | Le grand-père doit raconter une histoire drôle. | Déduction : <b>dever</b> + estar a.
katze | oma | ___ que o gato seja da avó. | Pode ser | Deve ser / Se calhar | Pode ser que o gato seja da avó. | Le chat appartient peut-être à la grand-mère. | <b>pode ser que</b> + conjuntivo.
tisch |  | Depois do almoço ainda ___ haver bolo. | deve | pode-se / tem | Depois do almoço ainda deve haver bolo. | Après le repas, il devrait encore y avoir du gâteau. | Probable : <b>dever haver</b>.
opa |  | ___ que o avô foi cozinheiro. | Dizem | Diz-se-lhe / Digam | Dizem que o avô foi cozinheiro. | Il paraît que le grand-père était cuisinier autrefois. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"friseur": {
"B1": ("Le corps : lavo o cabelo, penteio-me", """
haar | anna | A Anna vai ___ o cabelo. | cortar | cortar-se / fazer cortar | A Anna vai cortar o cabelo. | Anna se fait couper les cheveux. | Au Portugal, <b>cortar o cabelo</b> veut aussi dire « se faire couper les cheveux ».
haar |  | Lavo ___ cabelo todas as manhãs. | o | meu / o meu-me | Lavo o cabelo todas as manhãs. | Je me lave les cheveux tous les matins. | Avec une partie du corps : l'article, pas le possessif.
buerste |  | ___ depressa. | Penteio-me | Me penteio / Penteio | Penteio-me depressa. | Je me coiffe vite. | <b>pentear-se</b> : pronom après le verbe.
mann |  | Depois do trabalho, o homem lava ___ mãos. | as | suas / as suas-se | Depois do trabalho, o homem lava as mãos. | Après le travail, l'homme se lave les mains. | L'article : <b>lava as mãos</b>.
mantel |  | ___ o sobretudo. | Vestes | Vestes-te / Te vestes | Vestes o sobretudo. | Tu mets ton manteau. | <b>vestir</b> un vêtement : sans pronom réfléchi.
spiegel | anna | A Anna ___ ao espelho. | olha-se | se olha / olha-lhe | A Anna olha-se ao espelho. | Anna se regarde dans le miroir. | <b>olhar-se ao espelho</b> (au Portugal : <b>ao</b> espelho).
sofa |  | ___ no sofá. | Sentamo-nos | Sentamos-nos / Nos sentamos | Sentamo-nos no sofá. | Nous nous asseyons sur le canapé. | Devant <b>-nos</b>, le s tombe : <b>sentamo-nos</b>.
schere |  | Nunca ___ o cabelo a mim mesmo. | corto | me corto / corto-me | Nunca corto o cabelo a mim mesmo. | Je ne me coupe jamais les cheveux moi-même. | <b>a mim mesmo</b> = moi-même.
"""),
"B2": ("Quanto mais…, mais…", """
haar |  | Quanto mais curto é o cabelo, ___ depressa seca. | mais | o mais / tanto | Quanto mais curto é o cabelo, mais depressa seca. | Plus les cheveux sont courts, plus ils sèchent vite. | <b>quanto mais…, mais…</b>.
frau | zeitschrift | Quanto mais a senhora espera, mais ___. | lê | leia / ler | Quanto mais a senhora espera, mais lê. | Plus la dame attend, plus elle lit. | Indicatif dans les deux parties.
haar |  | ___ mais se lava o cabelo, mais seco fica. | Quanto | Tanto / Como | Quanto mais se lava o cabelo, mais seco fica. | Plus on se lave souvent les cheveux, plus ils deviennent secs. | <b>quanto mais</b>.
anna |  | Quanto ___ é o corte, mais contente fica a Anna. | melhor | mais bom / mais melhor | Quanto melhor é o corte, mais contente fica a Anna. | Meilleure est la coupe, plus Anna est contente. | <b>bom</b> → <b>melhor</b> : <b>quanto melhor</b>.
kasse | mann | Quanto mais clientes vêm, mais o homem ___. | ganha | ganhe / ganhar | Quanto mais clientes vêm, mais o homem ganha. | Plus il vient de clients, plus l'homme gagne d'argent. | Indicatif.
haar |  | Quanto mais comprido é o cabelo, ___ demora o corte. | mais | menos mais / tanto | Quanto mais comprido é o cabelo, mais demora o corte. | Plus les cheveux sont longs, plus la coupe dure longtemps. | <b>comprido</b> = long (cheveux, objet).
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ estar contente com o corte. | deve | pode-se / tem | Ela deve estar contente com o corte. | Elle doit être contente de la coupe. | Déduction : <b>dever</b>.
frau | sofa | A senhora no sofá ___ ser a próxima cliente. | pode | deve de / há | A senhora no sofá pode ser a próxima cliente. | La dame sur le canapé est peut-être la prochaine cliente. | Possibilité : <b>poder</b>.
mantel | anna | O sobretudo ___ da Anna. | será | seja / foi-se | O sobretudo será da Anna. | Le manteau est sans doute à Anna. | Futur de supposition : <b>será</b>.
mann |  | Este cabeleireiro ___ o melhor do bairro. | seria | será-se / seja | Este cabeleireiro seria o melhor do bairro. | Ce coiffeur serait le meilleur du quartier. | Le conditionnel de la rumeur.
"""),
},
"camping": {
"B1": ("Le futur : vou nadar, nadarei", """
see | anna | Amanhã a Anna ___ nadar no lago. | vai | irá a / vá | Amanhã a Anna vai nadar no lago. | Demain, Anna nagera dans le lac. | Le futur de l'oral : <b>ir</b> + infinitif.
zelt |  | Esta noite ___ na tenda. | dormirão | dormiram / dormem-se | Esta noite dormirão na tenda. | Cette nuit, ils dormiront dans la tente. | Futuro simples : <b>dormirão</b> (≠ dormiram, passé).
gitarre | anna | Vou ___ uma canção. | tocar-te | te tocar / tocar-te-ei | Vou tocar-te uma canção. | Je vais te jouer une chanson. | <b>vou</b> + infinitif-pronom.
topf |  | A sopa ___ pronta daqui a nada. | vai estar | estará-se / vai a estar | A sopa vai estar pronta daqui a nada. | La soupe sera bientôt prête. | <b>vai estar</b>.
boot |  | Amanhã de manhã ___ de barco. | vamos | iremos a / vamos a ir | Amanhã de manhã vamos de barco. | Demain matin, nous irons en barque. | <b>ir de barco</b> ; vamos.
feuer |  | ___ a fogueira mais tarde? | Apagas | Apagarás-te / Apagues | Apagas a fogueira mais tarde? | Tu éteindras le feu plus tard ? | À l'oral, le présent sert souvent de futur.
himmel |  | Esta noite ___ frio. | vai estar | vai a estar / estará-se | Esta noite vai estar frio. | Il va faire froid cette nuit. | Le temps qu'il fera : <b>vai estar</b> frio.
mann |  | O homem vai ___ a salsicha já. | comer | comer-se / come | O homem vai comer a salsicha já. | L'homme va manger sa saucisse tout de suite. | <b>vai</b> + infinitif.
"""),
"B2": ("L'irréel : se fosse…, iam", """
see |  | Se não ___ tão escuro, iam nadar. | estivesse | estiver / está | Se não estivesse tão escuro, iam nadar. | S'il ne faisait pas si sombre, ils iraient nager. | <b>se</b> + imperfeito do conjuntivo ; principale à l'imperfeito (oral).
zelt |  | Se ___ tempo, ficavam mais uma semana. | tivessem | tiverem / têm | Se tivessem tempo, ficavam mais uma semana. | S'ils avaient le temps, ils resteraient une semaine de plus. | <b>tivessem</b>.
mann |  | Se o homem tivesse fome, ___ a salsicha. | comia | coma / comer | Se o homem tivesse fome, comia a salsicha. | Si l'homme avait faim, il mangerait la saucisse. | Principale : imperfeito (ou <b>comeria</b>).
gitarre | anna | Quem me dera tocar guitarra tão bem ___ a Anna. | como | do que / que | Quem me dera tocar guitarra tão bem como a Anna. | J'aimerais savoir jouer de la guitare aussi bien qu'Anna. | <b>quem me dera</b> + infinitif ; <b>tão bem como</b>.
boot |  | Se o barco ___ maior, todos podiam ir. | fosse | for / era | Se o barco fosse maior, todos podiam ir. | Si la barque était plus grande, tout le monde pourrait monter. | <b>ser</b> → <b>fosse</b>.
holz |  | Se ao menos ___ trazido mais lenha! | tivessem | tiverem / tinham-se | Se ao menos tivessem trazido mais lenha! | Si seulement ils avaient apporté plus de bois ! | Le regret : <b>se ao menos</b> + tivesse + participe.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ estar a gostar muito da noite. | deve | pode-se / tem | Ela deve estar a gostar muito da noite. | Elle doit beaucoup apprécier la soirée. | Déduction : <b>dever</b>.
mann | anna | O homem ___ ser primo da Anna. | pode | deve de / há | O homem pode ser primo da Anna. | L'homme est peut-être le cousin d'Anna. | Possibilité : <b>poder</b>.
mond |  | ___ quase dez horas. | Serão | Sejam / Foram-se | Serão quase dez horas. | Il doit être presque dix heures. | L'heure supposée : futur <b>serão</b>.
wald |  | ___ que há lobos na floresta. | Dizem | Diz / Digam | Dizem que há lobos na floresta. | Il paraît qu'il y a des loups dans la forêt. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"strand": {
"B1": (T_PERFEITO, """
anna |  | A Anna ___ de avião para Espanha. | foi | ia / vai | A Anna foi de avião para Espanha. | Anna a pris l'avion pour l'Espagne. | Le portugais n'hésite pas entre deux auxiliaires : un seul perfeito, <b>foi</b>.
meer | anna | Hoje de manhã ela ___ no mar. | nadou | nadava / nada | Hoje de manhã ela nadou no mar. | Ce matin, elle a nagé dans la mer. | <b>nadar</b> → <b>nadou</b>.
eis | anna | Ela ___ um gelado. | comprou | comprava / compra | Ela comprou um gelado. | Elle a acheté une glace. | <b>comprar</b> → <b>comprou</b> ; la glace = <b>o gelado</b>.
ball | junge | O rapaz ___ a bola para a água. | atirou | atirava / atira | O rapaz atirou a bola para a água. | Le garçon a lancé le ballon dans l'eau. | <b>atirar</b> → <b>atirou</b>.
hund |  | O cão ___ à sombra. | adormeceu | adormecia / adormece | O cão adormeceu à sombra. | Le chien s'est endormi à l'ombre. | <b>adormecer</b> → <b>adormeceu</b>.
buch | handtuch | A Anna ___ o livro em cima da toalha. | pôs | punha / põe | A Anna pôs o livro em cima da toalha. | Anna a posé son livre sur la serviette. | <b>pôr</b> → <b>pôs</b>.
boot | meer | O barco ___ para o mar hoje de manhã. | saiu | saía / sai | O barco saiu para o mar hoje de manhã. | Le bateau a pris la mer ce matin. | <b>sair</b> → <b>saiu</b>.
anna | sonne | A Anna ___ o dia todo ao sol. | esteve | estava / está | A Anna esteve o dia todo ao sol. | Anna est restée toute la journée au soleil. | Une période finie : <b>esteve</b>.
"""),
"B2": ("Relatives et participes", """
anna | eis | A mulher ___ come um gelado chama-se Anna. | que | quem / qual | A mulher que come um gelado chama-se Anna. | La femme qui mange une glace s'appelle Anna. | Sujet : <b>que</b>.
junge | ball | O rapaz, ___ bola é colorida, brinca na água. | cuja | cujo / que a | O rapaz, cuja bola é colorida, brinca na água. | Le garçon au ballon multicolore joue dans l'eau. | <b>cuja</b> + bola.
insel | leuchtturm | A ilha na ___ se ergue um farol é pequena. | qual | que / onde | A ilha na qual se ergue um farol é pequena. | L'île sur laquelle se dresse un phare est petite. | <b>na qual</b> (ou <b>onde</b>).
hund |  | O cão ___ está deitado à sombra. | adormecido | adormecida / adormecer | O cão adormecido está deitado à sombra. | Le chien endormi est couché à l'ombre. | Participe adjectif : <b>adormecido</b>.
eis |  | O gelado já está meio ___. | comido | comida / comer | O gelado já está meio comido. | La glace est déjà à moitié mangée. | <b>o gelado</b> → <b>comido</b>.
meer |  | Aqui, no verão, ___ muito. | nada-se | nadam-se / se nada | Aqui, no verão, nada-se muito. | Ici, on nage beaucoup en été. | Le se impersonnel : <b>nada-se</b>.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ estar a sentir-se muito bem de férias. | deve | pode-se / tem | Ela deve estar a sentir-se muito bem de férias. | Elle doit se sentir très bien en vacances. | Déduction : <b>dever</b>.
hund | junge | ___ que o cão seja do rapaz. | Pode ser | Deve ser / Se calhar | Pode ser que o cão seja do rapaz. | Le chien appartient peut-être au garçon. | <b>pode ser que</b> + conjuntivo.
meer | junge | A água já ___ bastante quente. | estará | esteja / estava-se | A água já estará bastante quente. | L'eau doit déjà être assez chaude. | Futur de supposition : <b>estará</b>.
leuchtturm |  | ___ que do farol se vê até África. | Dizem | Diz / Digam | Dizem que do farol se vê até África. | Il paraît que du phare, on peut voir jusqu'en Afrique. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"winter": {
"B1": ("Ter frio, ficar bem : le portugais sans datif", """
anna |  | Ela ___ frio. | tem | está / é | Ela tem frio. | Elle a froid. | Avoir froid : <b>ter frio</b>.
muetze | anna | O gorro ___ bem. | fica-lhe | fica-a / lhe fica-se | O gorro fica-lhe bem. | Le bonnet lui va bien. | <b>ficar bem a alguém</b> : <b>fica-lhe bem</b>.
schal | schneemann | A Anna pôs um cachecol ___ boneco de neve. | ao | o / no | A Anna pôs um cachecol ao boneco de neve. | Anna a noué une écharpe au bonhomme de neige. | <b>pôr algo a alguém</b> : a + o = <b>ao</b>.
handschuh |  | Ela ___ as luvas. | calçou | vestiu-se / pôs-se | Ela calçou as luvas. | Elle a mis les gants. | Gants, chaussures : <b>calçar</b>.
hund |  | O cão usa um casaco para não ___ frio. | ter | estar / ter-se | O cão usa um casaco para não ter frio. | Le chien porte un manteau pour ne pas avoir froid. | <b>para não ter frio</b>.
stiefel | anna | As botas são ___. | dela | suas dela / delas | As botas são dela. | Les bottes sont à elle. | <b>são dela</b> : à elle.
karotte | schneemann | A Anna dá uma cenoura ___ boneco de neve para o nariz. | ao | o / do | A Anna dá uma cenoura ao boneco de neve para o nariz. | Anna donne une carotte au bonhomme de neige comme nez. | <b>dar algo a</b> : <b>ao</b>.
besen |  | Com a vassoura, ela ___ o caminho. | limpa | limpe / limpou-se | Com a vassoura, ela limpa o caminho. | Avec le balai, elle dégage le chemin. | <b>limpar</b> au présent.
"""),
"B2": (T_PASSIF, """
anna | schneemann | A mulher ___ faz um boneco de neve chama-se Anna. | que | quem / qual | A mulher que faz um boneco de neve chama-se Anna. | La femme qui fait un bonhomme de neige s'appelle Anna. | Sujet : <b>que</b>.
hund |  | O cão, ___ casaco é vermelho, fareja a neve. | cujo | cuja / que o | O cão, cujo casaco é vermelho, fareja a neve. | Le chien au manteau rouge renifle la neige. | <b>cujo</b> + casaco.
haus | auto | A casa em frente da ___ está o carro é amarela. | qual | que / quem | A casa em frente da qual está o carro é amarela. | La maison devant laquelle est la voiture est jaune. | <b>em frente da qual</b>.
auto |  | O carro está ___ de neve. | coberto | coberta / cobrido | O carro está coberto de neve. | La voiture est couverte de neige. | <b>cobrir</b> → <b>coberto</b>.
besen |  | O caminho ainda tem de ser ___. | varrido | varrida / varrer | O caminho ainda tem de ser varrido. | Le chemin doit encore être balayé. | Passif : <b>ter de ser</b> + participe.
kerze | fenster-2 | A vela ___ está na janela. | acesa | aceso / acendida | A vela acesa está na janela. | La bougie allumée est à la fenêtre. | Participe court accordé : <b>acesa</b>.
"""),
"C1": (T_HYPO, """
schneemann | anna | O boneco de neve ___ agradar-lhe muito. | deve | pode-se / tem | O boneco de neve deve agradar-lhe muito. | Le bonhomme de neige doit beaucoup lui plaire. | Déduction : <b>dever</b>.
fahrrad |  | A bicicleta ___ estar ali desde ontem à noite. | pode | deve de / há | A bicicleta pode estar ali desde ontem à noite. | Le vélo est peut-être là depuis hier soir. | Possibilité : <b>poder</b>.
schnee |  | A neve ___ ficar até amanhã. | deverá | deveria-se / deva | A neve deverá ficar até amanhã. | La neige devrait tenir jusqu'à demain. | Probable : <b>deverá</b>.
himmel |  | ___ que vai ser o inverno mais frio dos últimos dez anos. | Dizem | Diz-se-lhe / Digam | Dizem que vai ser o inverno mais frio dos últimos dez anos. | Il paraît que ce sera l'hiver le plus froid depuis dix ans. | Le ouï-dire : <b>dizem que</b>.
"""),
},
"bauernhof": {
"B1": ("Les verbes pronominaux : deita-se, lembras-te", """
anna | pferd | A Anna ___ com o cavalo. | alegra-se | se alegra / alegra | A Anna alegra-se com o cavalo. | Anna est contente de voir le cheval. | <b>alegrar-se com</b> ; pronom après le verbe.
hund | boden | O cão ___ no chão. | deita-se | se deita / deita | O cão deita-se no chão. | Le chien se couche par terre. | <b>deitar-se</b>.
katze | mauer | O gato ___ no muro. | senta-se | se senta / senta | O gato senta-se no muro. | Le chat s'assied sur le muret. | <b>sentar-se</b>.
onkel |  | ___ depois do trabalho. | Lavo-me | Me lavo / Lavo | Lavo-me depois do trabalho. | Je me lave après le travail. | En tête de phrase : jamais le pronom devant.
bank |  | ___ no banco. | Sentamo-nos | Nos sentamos / Sentamos-nos | Sentamo-nos no banco. | Nous nous asseyons sur le banc. | <b>sentamo-nos</b> : le s tombe devant nos.
haus |  | ___ da quinta? | Lembras-te | Te lembras / Lembras | Lembras-te da quinta? | Tu te souviens de la ferme ? | <b>lembrar-se de</b> ; la ferme = <b>a quinta</b>, au Portugal.
cousin |  | O primo da Anna lava ___ mãos. | as | suas / se as | O primo da Anna lava as mãos. | Le cousin d'Anna se lave les mains. | Le corps : l'article, pas de pronom (<b>lava as mãos</b>).
huhn-2 |  | As galinhas ___ depressa. | mexem-se | se mexem / mexem-nas | As galinhas mexem-se depressa. | Les poules bougent vite. | <b>mexer-se</b> = bouger.
"""),
"B2": ("Antes de, depois de, desde que, até", """
anna | pferd | Antes de ___ ao cavalo, a Anna lava as maçãs. | dar de comer | dá de comer / desse de comer | Antes de dar de comer ao cavalo, a Anna lava as maçãs. | Avant de nourrir le cheval, Anna lave les pommes. | <b>antes de</b> + infinitif (même sujet).
onkel | schwein | Depois de ___ a palha, o tio dá de comer ao porco. | ir buscar | foi buscar / vai buscar | Depois de ir buscar a palha, o tio dá de comer ao porco. | Après avoir été chercher la paille, son oncle nourrit le cochon. | <b>depois de</b> + infinitif ; <b>ir buscar</b> = aller chercher.
hund |  | O cão vive na quinta ___ um ano. | há | desde / faz-se | O cão vive na quinta há um ano. | Le chien vit à la ferme depuis un an. | Depuis + durée : <b>há</b> + durée.
katze |  | O gato dorme depois de ___. | comer | comeu / coma | O gato dorme depois de comer. | Le chat dort après avoir mangé. | <b>depois de</b> + infinitif.
anna |  | ___ que trabalha na quinta, a Anna levanta-se cedo. | Desde | Há / Depois | Desde que trabalha na quinta, a Anna levanta-se cedo. | Depuis qu'Anna travaille à la ferme, elle se lève tôt. | <b>desde que</b> (depuis que) + indicatif.
hund | anna | O cão espera até a Anna o ___. | chamar | chama / chamou | O cão espera até a Anna o chamar. | Le chien attend qu'Anna l'appelle. | <b>até</b> + infinitif personnel (sujet différent).
"""),
"C1": (T_HYPO, """
pferd | anna | O cavalo ___ ser muito meigo. | deve | pode-se / tem | O cavalo deve ser muito meigo. | Le cheval doit être très gentil. | Déduction : <b>dever</b> ; <b>meigo</b> = doux, gentil.
hund | cousin | O cão ___ ser do primo da Anna. | pode | deve de / há | O cão pode ser do primo da Anna. | Le chien appartient peut-être au cousin d'Anna. | Possibilité : <b>poder</b>.
ei | korb | Os ovos ___ de hoje de manhã. | serão | sejam / foram-se | Os ovos serão de hoje de manhã. | Les œufs datent sans doute de ce matin. | Futur de supposition : <b>serão</b>.
haus |  | A quinta ___ mais de cem anos. | teria | terá-se / tenha | A quinta teria mais de cem anos. | La ferme aurait plus de cent ans. | Le conditionnel de la rumeur.
"""),
},
"buergeramt": {
"B1": ("Les prépositions : de, há, com, para, a, sem", """
mark |  | O Mark é ___ Canadá. | do | de / no | O Mark é do Canadá. | Mark vient du Canada. | L'origine : <b>ser de</b> ; le Canada prend l'article : <b>do</b>.
mark |  | Ele está em Lisboa ___ um mês. | há | desde / por | Ele está em Lisboa há um mês. | Il est à Lisbonne depuis un mois. | Depuis + durée : <b>há</b>.
kugelschreiber | formular | O Mark preenche o impresso ___ uma esferográfica. | com | de / por | O Mark preenche o impresso com uma esferográfica. | Mark remplit le formulaire avec un stylo. | L'instrument : <b>com</b> ; le stylo = <b>a esferográfica</b>, au Portugal.
formular |  | O impresso é ___ o registo da morada. | para | por / a | O impresso é para o registo da morada. | Le formulaire est pour la déclaration de domicile. | La destination : <b>para</b>.
tuer |  | O Mark vai ___ Loja do Cidadão. | à | na / para a de | O Mark vai à Loja do Cidadão. | Mark va à l'espace citoyen. | <b>ir a</b> : a + a = <b>à</b> ; la Loja do Cidadão réunit les services publics au Portugal.
frau |  | A senhora trabalha ___ Loja do Cidadão. | na | à / pela | A senhora trabalha na Loja do Cidadão. | La femme travaille à l'espace citoyen. | Où l'on est : <b>em</b> + a = <b>na</b>.
pass | mark | O Mark não vem ___ o passaporte. | sem | com / nem | O Mark não vem sem o passaporte. | Mark ne vient pas sans son passeport. | <b>sem</b>.
frau-2 | baby | A jovem espera com o ___ bebé. | seu | sua / dele | A jovem espera com o seu bebé. | La jeune femme attend avec son bébé. | <b>o seu bebé</b>.
"""),
"B2": ("Não só… mas também, tanto… como, nem… nem", """
pass | formular | O Mark precisa não só do passaporte, ___ também do impresso. | mas | e / como | O Mark precisa não só do passaporte, mas também do impresso. | Mark a besoin non seulement de son passeport, mais aussi du formulaire. | <b>não só… mas também</b>.
frau |  | A senhora fala tanto português ___ inglês. | como | que / e | A senhora fala tanto português como inglês. | La femme parle aussi bien portugais qu'anglais. | <b>tanto… como</b>.
frau-2 |  | A jovem não traz ___ livro nem jornal. | nem | ou / não | A jovem não traz nem livro nem jornal. | La jeune femme n'a ni livre ni journal avec elle. | <b>nem… nem</b>.
mark | formular | ___ o Mark assina hoje, ou volta na próxima semana. | Ou | Nem / Quer | Ou o Mark assina hoje, ou volta na próxima semana. | Soit Mark signe aujourd'hui, soit il revient la semaine prochaine. | <b>ou… ou</b> : soit… soit.
kugelschreiber | mark | Quanto mais depressa o Mark escreve, mais cedo ___. | acaba | acabe / acabar | Quanto mais depressa o Mark escreve, mais cedo acaba. | Plus Mark écrit vite, plus tôt il a fini. | <b>quanto mais…, mais…</b>.
fenster |  | O gabinete é pequeno, ___ é luminoso. | mas | pois / porém que | O gabinete é pequeno, mas é luminoso. | Le bureau est certes petit, mais lumineux. | L'opposition : <b>mas</b>.
"""),
"C1": (T_HYPO, """
formular | mark | O impresso ___ ser importante. | deve | pode-se / tem | O impresso deve ser importante. | Le formulaire doit être important. | Déduction : <b>dever</b>.
frau-2 |  | A jovem também ___ ser nova em Lisboa. | pode | deve de / há | A jovem também pode ser nova em Lisboa. | La jeune femme est peut-être aussi nouvelle à Lisbonne. | Possibilité : <b>poder</b>.
uhr |  | A marcação ___ terminar daqui a dez minutos. | deverá | deveria-se / deva | A marcação deverá terminar daqui a dez minutos. | Le rendez-vous devrait être fini dans dix minutes. | Probable : <b>deverá</b> ; un rendez-vous administratif = <b>uma marcação</b>.
stuhl |  | ___ que na Loja do Cidadão se espera muito. | Dizem | Diz-se-lhe / Digam | Dizem que na Loja do Cidadão se espera muito. | Il paraît qu'on attend longtemps à l'espace citoyen. | Le ouï-dire ; après <b>que</b>, le se passe devant.
"""),
},
"fahrradwerkstatt": {
"B1": ("Alguém, ninguém, algo, nada, se", """
mark | mann | ___ me pode ajudar? | Alguém | Ninguém / Algo | Alguém me pode ajudar? | Quelqu'un peut-il m'aider ? | <b>alguém</b> = quelqu'un ; il attire le pronom devant.
zange | kette | ___ de um alicate para a corrente. | Precisa-se | Precisam-se / Se precisa | Precisa-se de um alicate para a corrente. | Il faut une pince pour la chaîne. | <b>precisa-se de</b> = on a besoin de.
kette |  | ___ está avariado: a corrente! | Algo | Nada / Alguém | Algo está avariado: a corrente! | Quelque chose est cassé : la chaîne ! | <b>algo</b> = quelque chose.
rad |  | A roda está em ordem, não falta ___. | nada | algo / ninguém | A roda está em ordem, não falta nada. | La roue est en bon état, il ne manque rien. | Après <b>não</b> : <b>nada</b>.
tuer |  | Na oficina não está ___ além do Mark e do mecânico. | ninguém | alguém / nada | Na oficina não está ninguém além do Mark e do mecânico. | Dans l'atelier, il n'y a personne à part Mark et le mécanicien. | Après <b>não</b> : <b>ninguém</b>.
fahrrad-3 |  | Em Lisboa ___ cada vez mais de bicicleta. | anda-se | andam-se / se anda | Em Lisboa anda-se cada vez mais de bicicleta. | À Lisbonne, on fait de plus en plus de vélo. | Le se impersonnel : <b>anda-se</b>.
werkzeug | mann | ___ viu as minhas ferramentas? | Alguém | Ninguém / Algo | Alguém viu as minhas ferramentas? | Quelqu'un a-t-il vu mes outils ? | <b>alguém</b>.
tasse |  | Queres beber ___? Há café. | alguma coisa | nada / alguém | Queres beber alguma coisa? Há café. | Veux-tu boire quelque chose ? Il y a du café. | <b>alguma coisa</b> = quelque chose (courant).
"""),
"B2": ("Le passif sans ser : se, ficar, a + infinitif", """
kette |  | A corrente ___ facilmente. | arranja-se | arranjam-se / se arranja | A corrente arranja-se facilmente. | La chaîne se répare facilement. | Le se passif : <b>arranja-se</b>.
rad |  | A roda está ___ arranjar ainda hoje. | por | para ser / de | A roda está por arranjar ainda hoje. | La roue est à réparer aujourd'hui même. | <b>estar por</b> + infinitif : reste à faire.
werkzeug |  | Aqui ___ bicicletas. | arranjam-se | arranja-se / se arranjam | Aqui arranjam-se bicicletas. | Ici, on répare des vélos. | Accord avec <b>bicicletas</b>.
oel | kette | A corrente tem de ser ___. | oleada | oleado / olear | A corrente tem de ser oleada. | La chaîne doit être huilée. | Passif : <b>ter de ser</b> + participe accordé.
fahrrad-2 |  | A bicicleta vermelha já não se ___ vender. | consegue | conseguem / pode-se | A bicicleta vermelha já não se consegue vender. | Le vélo rouge ne peut plus se vendre. | <b>já não se consegue</b> + infinitif.
tuer |  | A oficina ___ às dezoito horas. | fecha | é fechada-se / fecha-se a | A oficina fecha às dezoito horas. | On ferme l'atelier à dix-huit heures. | Le portugais dit simplement : <b>a oficina fecha</b>.
"""),
"C1": (T_HYPO, """
rad | mark | ___ estar estragada. | Deve | Pode-se / Tem | Deve estar estragada. | Elle doit être cassée. | Déduction : <b>dever</b> (la roue → <b>estragada</b>).
hund | mann | O cão ___ ser do mecânico. | pode | deve de / há | O cão pode ser do mecânico. | Le chien appartient peut-être au mécanicien. | Possibilité : <b>poder</b>.
werkzeug |  | O arranjo ___ demorar uma hora. | deverá | deveria-se / deva | O arranjo deverá demorar uma hora. | La réparation devrait durer une heure. | Probable : <b>deverá</b>.
tuer |  | Esta oficina ___ a melhor do bairro. | seria | será-se / seja | Esta oficina seria a melhor do bairro. | Cet atelier serait le meilleur du quartier. | Le conditionnel de la rumeur.
"""),
},
"heimwerken": {
"B1": ("L'impératif : dá-me, não caias", """
hammer | mark | Mark, ___-me o martelo, por favor! | dá | dás / dê | Mark, dá-me o martelo, por favor! | Mark, donne-moi le marteau, s'il te plaît ! | Tu : la forme de ele (<b>dá</b>) ; pronom après.
papier |  | ___ bem as instruções! | Lê | Lês / Leia-te | Lê bem as instruções! | Lis bien la notice ! | <b>ler</b>, tu : <b>lê</b>.
pinsel | eimer | ___ o pincel em cima do balde! | Põe | Pões / Ponha-te | Põe o pincel em cima do balde! | Pose le pinceau sur le seau ! | <b>pôr</b>, tu : <b>põe</b>.
handschuh |  | ___ as luvas! | Calça | Calças / Calce-te | Calça as luvas! | Mets les gants ! | <b>calçar</b> les gants ; tu : <b>calça</b>.
leiter |  | Mark, não ___ da escada! | caias | cais / cai | Mark, não caias da escada! | Mark, ne tombe pas de l'échelle ! | Négatif : le subjonctif (<b>não caias</b>).
mark |  | ___ uma pausa! | Façamos | Fazemos-nos / Faz | Façamos uma pausa! | Faisons une pause ! | Nós : le subjonctif (<b>façamos</b>) ; à l'oral, <b>Vamos fazer uma pausa!</b>
katze | fenster | Bichano, ___ da janela! | desce | desças / desce-te | Bichano, desce da janela! | Minou, descends de la fenêtre ! | Tu : <b>desce</b>.
leiter |  | Senhor vizinho, ___-me a escada, por favor! | segure | segura / seguras | Senhor vizinho, segure-me a escada, por favor! | Monsieur le voisin, tenez-moi l'échelle, s'il vous plaît ! | O senhor : le subjonctif (<b>segure</b>).
"""),
"B2": ("Le but : para, para que", """
farbe |  | O Mark comprou tinta ___ pintar a parede de azul. | para | para que / a fim que | O Mark comprou tinta para pintar a parede de azul. | Mark a acheté de la peinture pour peindre le mur en bleu. | Même sujet : <b>para</b> + infinitif.
regal | papier | Ele lê as instruções para que a estante não ___. | caia | cai / cair-se | Ele lê as instruções para que a estante não caia. | Il lit la notice pour que l'étagère ne tombe pas. | Sujet différent : <b>para que</b> + conjuntivo.
handschuh |  | Ele esqueceu-se ___ calçar as luvas. | de | a / em | Ele esqueceu-se de calçar as luvas. | Il a oublié de mettre les gants. | <b>esquecer-se de</b>.
regal | mark | Não é fácil ___ uma estante sozinho. | montar | de montar / a montar | Não é fácil montar uma estante sozinho. | Ce n'est pas facile de monter une étagère tout seul. | <b>é fácil</b> + infinitif, sans « de ».
farbe |  | A parede já está meio ___. | pintada | pintado / pintar | A parede já está meio pintada. | Le mur est déjà à moitié peint. | État : <b>a parede</b> → <b>pintada</b>.
papier |  | Sem ___ as instruções, não se monta uma estante. | ler | lê / leres-se | Sem ler as instruções, não se monta uma estante. | Sans lire la notice, on ne monte pas d'étagère. | <b>sem</b> + infinitif.
"""),
"C1": (T_HYPO, """
papier | mark | As instruções ___ ser difíceis de perceber. | devem | deve / podem-se | As instruções devem ser difíceis de perceber. | La notice doit être difficile à comprendre. | Déduction, au pluriel : <b>devem</b> (as instruções).
katze |  | ___ que o gato seja do vizinho. | Pode ser | Deve ser / Se calhar | Pode ser que o gato seja do vizinho. | Le chat appartient peut-être au voisin. | <b>pode ser que</b> + conjuntivo.
regal |  | A estante ___ estar pronta hoje à noite. | deverá | deveria-se / deva | A estante deverá estar pronta hoje à noite. | L'étagère devrait être finie ce soir. | Probable : <b>deverá</b>.
farbe |  | ___ que antigamente vivia um pintor neste apartamento. | Consta | Constam / Conste | Consta que antigamente vivia um pintor neste apartamento. | Il paraît qu'un peintre habitait autrefois dans l'appartement. | Le ouï-dire, soutenu : <b>consta que</b>.
"""),
},
"sportplatz": {
"B1": ("Raconter : le perfeito et l'imperfeito", """
mark | ball | O Mark ___ a bola para a baliza. | rematou | rematava / remata | O Mark rematou a bola para a baliza. | Mark a tiré le ballon dans le but. | <b>rematar</b> = tirer ; le but = <b>a baliza</b>, au Portugal.
torwart |  | O guarda-redes ___ na relva. | caiu | caía / cai | O guarda-redes caiu na relva. | Le gardien est tombé dans l'herbe. | <b>cair</b> → <b>caiu</b> ; le gardien = <b>o guarda-redes</b>.
mannschaft | mark | Os jogadores ___ para o Mark. | correram | corriam / correm | Os jogadores correram para o Mark. | Les joueurs ont couru vers Mark. | <b>correr</b> → <b>correram</b>.
trainerin |  | A treinadora ___ palmas. | bateu | batia / bate | A treinadora bateu palmas. | L'entraîneuse a applaudi. | <b>bater palmas</b> = applaudir.
mark |  | O Mark ___ de alegria. | gritou | gritava / grita | O Mark gritou de alegria. | Mark a crié de joie. | <b>gritar</b> → <b>gritou</b>.
uhr |  | O jogo ___ às dez horas. | começou | começava / começa | O jogo começou às dez horas. | Le match a commencé à dix heures. | <b>começar</b> → <b>começou</b>.
bank | mann | Os espectadores ___ sentados no banco. | estavam | estiveram-se / estão | Os espectadores estavam sentados no banco. | Les spectateurs étaient assis sur le banc. | Le décor : imperfeito (<b>estavam</b>).
mark |  | No fim, a equipa do Mark ___. | ganhou | ganhava / ganha | No fim, a equipa do Mark ganhou. | À la fin, l'équipe de Mark a gagné. | <b>ganhar</b> → <b>ganhou</b> ; l'équipe = <b>a equipa</b>.
"""),
"B2": ("Porque, embora, quando, assim que", """
mark |  | O Mark festeja porque ___ um golo. | marcou | marcasse / marque | O Mark festeja porque marcou um golo. | Mark exulte parce qu'il a marqué un but. | <b>porque</b> + indicatif ; le but marqué = <b>o golo</b>.
torwart |  | O guarda-redes ri-se, embora não ___ defendido a bola. | tenha | tem / tinha | O guarda-redes ri-se, embora não tenha defendido a bola. | Le gardien rit, bien qu'il n'ait pas arrêté le ballon. | <b>embora</b> + conjuntivo composé.
trainerin | mark | Quando o Mark ___ o golo, a treinadora bateu palmas. | marcou | marcava / marcar | Quando o Mark marcou o golo, a treinadora bateu palmas. | Quand Mark a marqué le but, l'entraîneuse a applaudi. | <b>quando</b> au passé : indicatif.
flasche | mark | O Mark bebe água assim que o jogo ___. | acabar | acaba / acabe | O Mark bebe água assim que o jogo acabar. | Mark boit de l'eau dès que le match est fini. | <b>assim que</b> + futur : futuro do conjuntivo.
bank |  | Os espectadores estão sentados ___ os jogadores correm. | enquanto | assim que / embora | Os espectadores estão sentados enquanto os jogadores correm. | Les spectateurs sont assis pendant que les joueurs courent. | <b>enquanto</b>.
trainerin |  | Treinam todos os sábados para ___ em forma. | se manterem | manterem-se-em / se mantêm | Treinam todos os sábados para se manterem em forma. | Ils s'entraînent chaque samedi pour rester en forme. | <b>para</b> + infinitif personnel (<b>se manterem</b>).
"""),
"C1": (T_HYPO, """
mark |  | ___ ser o primeiro golo dele. | Deve | Pode-se / Tem | Deve ser o primeiro golo dele. | Ce doit être son premier but. | Déduction : <b>dever</b>.
mann |  | O senhor idoso ___ ser vizinho do Mark. | pode | deve de / há | O senhor idoso pode ser vizinho do Mark. | Le vieux monsieur est peut-être le voisin de Mark. | Possibilité : <b>poder</b>.
uhr |  | O jogo ___ estar a acabar. | deve | pode-se / tem | O jogo deve estar a acabar. | Le match devrait bientôt être fini. | <b>dever</b> + estar a : sans doute en train de.
trainerin |  | A treinadora ___ sido profissional. | teria | terá-se / tenha | A treinadora teria sido profissional. | Il paraît que l'entraîneuse était professionnelle autrefois. | La rumeur sur le passé : <b>teria sido</b>.
"""),
},
"umzug": {
"B1": ("Em cima, lá dentro, com ele : dire où sans répéter", """
stuhl | tisch | Ali está a mesa. ___ dela está uma cadeira. | Em cima | Dentro / Debaixo | Ali está a mesa. Em cima dela está uma cadeira. | Voilà la table. Il y a une chaise dessus. | <b>em cima dela</b> = dessus (de la table).
pflanze | karton | Esta é a caixa da Anna. Lá ___ está uma planta. | dentro | em cima / fora | Esta é a caixa da Anna. Lá dentro está uma planta. | Voici le carton d'Anna. Dedans, il y a une plante. | Dedans : <b>lá dentro</b>.
hammer | bruder | O irmão tem um martelo. Vai trabalhar com ___ mais tarde. | ele | o / lhe | O irmão tem um martelo. Vai trabalhar com ele mais tarde. | Le frère a un marteau. Il s'en servira plus tard. | Après une préposition, un objet se dit <b>ele, ela</b>.
anna |  | ___ é que a Anna está ansiosa? Pela casa nova. | Por que | De que / O que | Por que é que a Anna está ansiosa? Pela casa nova. | De quoi Anna se réjouit-elle ? De son nouvel appartement. | <b>estar ansioso por</b> → <b>por que</b>.
anna |  | A Anna gosta da casa. Gosta de falar ___. | dela | dele / a ela | A Anna gosta da casa. Gosta de falar dela. | Anna aime l'appartement. Elle aime en parler. | <b>falar de</b> + ela = <b>dela</b>.
bruder | pizza | ___ que pensa o irmão? Na pizza! | Em | De / A | Em que pensa o irmão? Na pizza! | À quoi pense le frère ? À la pizza ! | <b>pensar em</b> → <b>em que</b>.
koffer | buch | Os livros estão no chão. A mala está ao ___. | lado | lado deles / pé de | Os livros estão no chão. A mala está ao lado. | Les livres sont par terre. La valise est à côté. | À côté : <b>ao lado</b>.
"""),
"B2": ("Le futur antérieur : terá feito", """
karton-2 | anna | Até à noite, a Anna ___ desempacotado todas as caixas. | terá | tinha / teria | Até à noite, a Anna terá desempacotado todas as caixas. | D'ici ce soir, Anna aura déballé tous les cartons. | Futur antérieur : <b>terá</b> + participe.
gluehbirne | bruder | Daqui a nada, o irmão ___ enroscado a lâmpada. | terá | tem / teve | Daqui a nada, o irmão terá enroscado a lâmpada. | Dans un instant, le frère aura vissé l'ampoule. | <b>terá enroscado</b>.
bruder |  | Daqui a uma hora, o irmão já ___ ido para casa. | terá | tinha / tenha | Daqui a uma hora, o irmão já terá ido para casa. | Dans une heure, le frère sera déjà rentré chez lui. | Toujours <b>ter</b> : <b>terá ido</b>.
anna | karton | A Anna está cansada. ___ carregado muito. | Terá | Teria / Tinha-se | A Anna está cansada. Terá carregado muito. | Anna est fatiguée. Elle a sans doute beaucoup porté. | Supposition sur le passé : <b>terá</b> + participe.
pizza | bruder | Quem pediu a pizza? ___ sido o irmão. | Terá | Será / Tenha | Quem pediu a pizza? Terá sido o irmão. | Qui a commandé la pizza ? C'est sans doute le frère. | <b>terá sido</b>.
anna |  | Na próxima semana, a Anna já se ___ habituado à casa nova. | terá | tinha / teria-se | Na próxima semana, a Anna já se terá habituado à casa nova. | La semaine prochaine, Anna se sera habituée au nouvel appartement. | Après <b>já</b>, le pronom devant : <b>se terá habituado</b>.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ estar ansiosa pela casa nova. | deve | pode-se / tem | Ela deve estar ansiosa pela casa nova. | Elle doit se réjouir de son nouvel appartement. | Déduction : <b>dever</b>.
buch | regal | ___ os livros vão para a estante branca. | Se calhar | Talvez que / Deve | Se calhar os livros vão para a estante branca. | Les livres iront peut-être dans l'étagère blanche. | <b>se calhar</b> + indicatif.
pizza | bruder | A pizza ___ para a Anna e o irmão. | será | seja / foi-se | A pizza será para a Anna e o irmão. | La pizza est sans doute pour Anna et son frère. | Futur de supposition.
fenster |  | A casa ___ muito sossegada. | seria | será-se / seja | A casa seria muito sossegada. | L'appartement serait très calme. | Le conditionnel de la rumeur ; <b>sossegado</b> = calme.
"""),
},
"untersuchung": {
"B1": ("Les consignes du médecin : respire fundo, por favor", """
brust | hand-aerztin-haut | A médica ___ os pulmões dele. | ausculta | escuta-se / ouve-lhe | A médica ausculta os pulmões dele. | La médecin ausculte ses poumons. | <b>auscultar</b>.
mark |  | ___ fundo, por favor! | Inspire | Inspira-se / Inspiras | Inspire fundo, por favor! | Inspirez profondément, s'il vous plaît ! | Consigne polie : le subjonctif (<b>inspire</b>).
mark | unterhose | O Mark ___ até às cuecas. | despiu-se | se despiu / despiu | O Mark despiu-se até às cuecas. | Mark s'est déshabillé jusqu'au caleçon. | <b>despir-se</b> → <b>despiu-se</b>.
stethoskop | brust | A médica põe-___ o estetoscópio no peito. | lhe | o / se | A médica põe-lhe o estetoscópio no peito. | La médecin pose le stéthoscope sur sa poitrine. | <b>lhe</b> : à lui (sur lui).
mark | waage | O Mark vai ___ para a balança. | subir | subir-se / sobe | O Mark vai subir para a balança. | Mark va tout de suite monter sur la balance. | <b>subir para</b> : monter sur.
waage | mark | Depois fica ___ na balança. | quieto | quieta / quietamente | Depois fica quieto na balança. | Ensuite, il reste immobile sur la balance. | <b>ficar quieto</b> = rester immobile.
"""),
"B2": (T_PASSIF, """
brust | hand-aerztin-haut | Os pulmões dele estão a ser ___. | auscultados | auscultadas / auscultar | Os pulmões dele estão a ser auscultados. | Ses poumons sont en train d'être auscultés. | <b>estar a ser</b> + participe accordé (os pulmões).
mark | brust | O doente, ___ peito está a ser auscultado, chama-se Mark. | cujo | cuja / que o | O doente, cujo peito está a ser auscultado, chama-se Mark. | Le patient dont on ausculte la poitrine s'appelle Mark. | <b>cujo</b> + peito.
aerztin | mark | A médica ___ o examina é a médica de família dele. | que | quem / qual | A médica que o examina é a médica de família dele. | La médecin qui l'examine est sa médecin de famille. | Après <b>que</b>, le pronom devant : <b>que o examina</b>.
waage | mark | A balança para a ___ ele vai subir está encostada à parede. | qual | que / quem | A balança para a qual ele vai subir está encostada à parede. | La balance sur laquelle il va monter est contre le mur. | <b>para a qual</b>.
waage |  | Daqui a pouco, a altura dele também vai ser ___. | medida | medido / medir | Daqui a pouco, a altura dele também vai ser medida. | Dans un instant, on mesurera aussi sa taille. | Passif : <b>vai ser</b> + participe accordé.
mark |  | O Mark fica quieto enquanto ___ examinado. | é | está-se / seja | O Mark fica quieto enquanto é examinado. | Mark reste tranquille pendant qu'on l'examine. | Passif au présent : <b>é examinado</b>.
"""),
"C1": ("Hypothèses et irréel", """
arm-l |  | Ele ___ fazer muito desporto. | deve | pode-se / tem | Ele deve fazer muito desporto. | Il doit faire beaucoup de sport. | Déduction : <b>dever</b> ; le sport = <b>o desporto</b>.
mark |  | Ele ___ ser saudável. | deverá | deveria-se / deva | Ele deverá ser saudável. | Il est sans doute en bonne santé. | Probable : <b>deverá</b>.
aerztin |  | ___ que esta médica é muito minuciosa. | Dizem | Diz-se-lhe / Digam | Dizem que esta médica é muito minuciosa. | Il paraît que cette médecin est très minutieuse. | Le ouï-dire.
aerztin | brust | Se o ritmo cardíaco ___ irregular, ela mandava-o ao cardiologista. | fosse | for / era | Se o ritmo cardíaco fosse irregular, ela mandava-o ao cardiologista. | Si son rythme cardiaque était irrégulier, elle l'enverrait chez le cardiologue. | Irréel du présent : <b>se fosse</b>.
mark |  | Se ele não se ___ despido, ela não o teria podido auscultar. | tivesse | tiver / tinha | Se ele não se tivesse despido, ela não o teria podido auscultar. | S'il ne s'était pas déshabillé, elle n'aurait pas pu l'ausculter. | Irréel du passé : <b>se tivesse</b> + participe.
aerztin | mark | Sem exame, não ___ saber ao certo. | se podia | podia-se-se / se pode-se | Sem exame, não se podia saber ao certo. | Sans examen, on ne pourrait pas le savoir exactement. | Après <b>não</b>, le se devant : <b>não se podia</b>.
"""),
},
"untersuchung-dos": {
"B1": ("Les consignes du médecin : vire-se, respire", """
mark |  | ___-se, por favor! | Vire | Vira / Viras | Vire-se, por favor! | Retournez-vous, s'il vous plaît ! | Le vouvoiement : <b>vire-se</b>.
mark | ruecken | O Mark virou-se para ela poder ___ as costas. | auscultar-lhe | lhe auscultar / auscultar-se | O Mark virou-se para ela poder auscultar-lhe as costas. | Mark s'est retourné pour qu'elle puisse ausculter son dos. | <b>auscultar-lhe as costas</b> : le pronom remplace le possessif.
stethoskop | ruecken | A médica põe o estetoscópio ___ costas dele. | nas | na / às | A médica põe o estetoscópio nas costas dele. | La médecin pose le stéthoscope sur son dos. | Le dos = <b>as costas</b> (pluriel) : em + as = <b>nas</b>.
arm-l |  | Ele deixa os braços ___. | caídos | caída / cair-se | Ele deixa os braços caídos. | Il laisse pendre ses bras, détendus. | <b>deixar</b> + participe accordé.
handflaeche-r |  | Ele segura as mãos de modo a ___ as palmas. | mostrar | mostre / mostrando-se | Ele segura as mãos de modo a mostrar as palmas. | Il tient les mains de façon à ce qu'on voie les paumes. | <b>de modo a</b> + infinitif.
ruecken |  | ___ e inspire com calma, por favor! | Expire | Expira-se / Expiras | Expire e inspire com calma, por favor! | Expirez et inspirez calmement, s'il vous plaît ! | Le vouvoiement : <b>expire</b>.
"""),
"B2": (T_PASSIF, """
ruecken | hand-aerztin-haut | As costas dele estão a ser ___. | auscultadas | auscultados / auscultar | As costas dele estão a ser auscultadas. | Son dos est en train d'être ausculté. | <b>as costas</b> (fém. pluriel) → <b>auscultadas</b>.
mark | ruecken | É o doente ___ costas a médica ausculta. | cujas | cujos / que as | É o doente cujas costas a médica ausculta. | C'est le patient dont la médecin ausculte le dos. | <b>cujas</b> + costas.
aerztin | ruecken | A médica, ___ estetoscópio está nas costas dele, ouve com atenção. | cujo | cuja / que o | A médica, cujo estetoscópio está nas costas dele, ouve com atenção. | La médecin, dont le stéthoscope est posé sur son dos, écoute attentivement. | <b>cujo</b> + estetoscópio.
mark |  | Depois de ele se ___ virado, ela auscultou-lhe as costas. | ter | tinha / tivesse | Depois de ele se ter virado, ela auscultou-lhe as costas. | Après qu'il s'est retourné, elle a ausculté son dos. | <b>depois de</b> + <b>ter</b> + participe.
ruecken |  | Antes de as costas ___ auscultadas, ele tem de inspirar fundo. | serem | sejam / são | Antes de as costas serem auscultadas, ele tem de inspirar fundo. | Avant que le dos puisse être ausculté, il doit inspirer profondément. | Infinitif personnel passif : <b>serem</b> + participe.
schulterblatt | wirbelsaeule | As omoplatas, entre as ___ fica a coluna, veem-se bem. | quais | que / quem | As omoplatas, entre as quais fica a coluna, veem-se bem. | Les omoplates, entre lesquelles se trouve la colonne, se voient bien. | <b>entre as quais</b>.
"""),
"C1": ("Hypothèses et irréel", """
mark |  | Ele já ___ sido auscultado muitas vezes. | terá | teria / tenha | Ele já terá sido auscultado muitas vezes. | Il a sans doute déjà été ausculté souvent. | Supposition sur le passé : <b>terá sido</b>.
ruecken |  | Se ___ dores nas costas, já o teria dito à médica. | tivesse | tiver / tinha-se | Se tivesse dores nas costas, já o teria dito à médica. | S'il avait mal au dos, il l'aurait dit à la médecin. | <b>se tivesse</b> + conditionnel passé.
aerztin | ruecken | Caso ela ___ algum ruído, mandava-o fazer um raio-X. | ouvisse | ouça / ouvir | Caso ela ouvisse algum ruído, mandava-o fazer um raio-X. | À supposer qu'elle entende un bruit, elle lui ferait passer une radio. | <b>caso</b> + conjuntivo imparfait pour l'hypothèse.
mark |  | ___ que o Mark nunca esteve gravemente doente. | Consta | Constam / Conste | Consta que o Mark nunca esteve gravemente doente. | Il paraît que Mark n'a jamais été gravement malade. | Le ouï-dire, soutenu : <b>consta que</b>.
wirbelsaeule |  | A postura direita dele ___ do muito desporto que faz. | virá | venha / veio-se | A postura direita dele virá do muito desporto que faz. | Sa posture droite vient sans doute de tout le sport qu'il fait. | Futur de supposition : <b>virá</b>.
aerztin |  | Se não ___ ouvido nada, já teria parado. | tivesse | tiver / teria | Se não tivesse ouvido nada, já teria parado. | Si elle n'avait rien entendu, elle aurait arrêté depuis longtemps. | Irréel du passé.
"""),
},
"waschsalon": {
"B1": ("Deixar : laisser, laisser faire", """
anna | waschmaschine | A Anna ___ a máquina a trabalhar. | deixa | faz / põe-se | A Anna deixa a máquina a trabalhar. | Anna fait tourner la machine à laver. | <b>deixar</b> + a + infinitif : laisser tourner.
korb | boden | Ela deixa o cesto ___ chão. | no | ao / para o | Ela deixa o cesto no chão. | Elle laisse le panier par terre. | <b>no chão</b>.
frau | maedchen | A senhora deixa a menina ___ com o telemóvel. | brincar | brinca / a brincar-se | A senhora deixa a menina brincar com o telemóvel. | La femme laisse la fille jouer avec le téléphone. | <b>deixar alguém</b> + infinitif.
anna |  | ___-me ajudar-te! | Deixa | Deixas / Deixe-te | Deixa-me ajudar-te! | Laisse-moi t'aider ! | Impératif, tu : <b>deixa-me</b>.
jacke |  | Deixo o casaco ___ casa. | em | na / à | Deixo o casaco em casa. | Je laisse ma veste à la maison. | À la maison : <b>em casa</b>, sans article.
jeans | korb | A Anna ___ as calças de ganga no cesto. | deixou | deixava / deixa-se | A Anna deixou as calças de ganga no cesto. | Anna a laissé le jean dans le panier. | Le jean = <b>as calças de ganga</b>, au Portugal.
waschmaschine |  | Ela ___ lavar a roupa. | mandou | deixou-se / fez-se | Ela mandou lavar a roupa. | Elle a fait laver le linge. | Faire faire : <b>mandar</b> + infinitif.
tuer |  | ___ para casa! | Vamos | Deixemos / Vamos-nos | Vamos para casa! | Rentrons à la maison ! | <b>vamos</b> = allons, rentrons.
"""),
"B2": ("Le participe comme adjectif", """
waschmaschine-3 |  | A máquina a ___ faz barulho. | trabalhar | trabalhada / trabalha | A máquina a trabalhar faz barulho. | La machine à laver en marche est bruyante. | Le portugais dit « en train de » avec <b>a</b> + infinitif.
pullover-2 | tisch | A camisola ___ está em cima da mesa. | dobrada | dobrado / dobrar | A camisola dobrada está em cima da mesa. | Le pull plié est sur la table. | Participe accordé : <b>dobrada</b>.
frau | bank | A senhora que está a ___ está sentada no banco. | ler | lida / lendo-se | A senhora que está a ler está sentada no banco. | La femme qui lit est assise sur le banc. | <b>estar a ler</b>.
handy | maedchen | A menina segura um telemóvel ___. | desligado | desligada / desligar | A menina segura um telemóvel desligado. | La fille tient un téléphone éteint. | <b>o telemóvel</b> → <b>desligado</b>.
tuer |  | A porta ___ continua fechada. | fechada | fechado / fechar | A porta fechada continua fechada. | La porte fermée reste fermée. | <b>a porta</b> → <b>fechada</b>.
hemd | anna | A Anna segura uma camisa ainda por ___. | lavar | lavada / lavar-se | A Anna segura uma camisa ainda por lavar. | Anna tient une chemise pas encore lavée. | <b>por</b> + infinitif : pas encore fait.
"""),
"C1": (T_HYPO, """
korb | anna | Ela não ___ ter lavado roupa há muito tempo. | deve | pode-se / tem | Ela não deve ter lavado roupa há muito tempo. | Elle n'a pas dû faire de lessive depuis longtemps. | Déduction sur le passé : <b>deve ter</b> + participe.
maedchen | frau | A menina ___ ser neta da senhora. | pode | deve de / há | A menina pode ser neta da senhora. | La fille est peut-être la petite-fille de la femme. | Possibilité : <b>poder</b>.
waschmaschine |  | A roupa ___ estar pronta daqui a uma hora. | deverá | deveria-se / deva | A roupa deverá estar pronta daqui a uma hora. | Le linge devrait être prêt dans une heure. | Probable : <b>deverá</b>.
tuer |  | ___ que a lavandaria vai fechar em breve. | Dizem | Diz-se-lhe / Digam | Dizem que a lavandaria vai fechar em breve. | Il paraît que la laverie va bientôt fermer. | Le ouï-dire ; la laverie = <b>a lavandaria</b>.
"""),
},
"kreuzung": {
"B1": ("Indiquer le chemin", """
anna | apotheke | Desculpe, como é que ___ à farmácia? | se vai | vai-se / se vá | Desculpe, como é que se vai à farmácia? | Excusez-moi, comment aller à la pharmacie ? | Après <b>como é que</b>, le se devant : <b>se vai</b>.
zebrastreifen |  | ___ a rua, ali na passadeira. | Atravesse | Atravessa-se / Atravesses | Atravesse a rua, ali na passadeira. | Traversez la rue, là, au passage piéton. | Vouvoiement : <b>atravesse</b> ; le passage piéton = <b>a passadeira</b>.
ampel-vorne |  | Espere até o semáforo ___ verde. | ficar | fica / fique-se | Espere até o semáforo ficar verde. | Attendez que le feu passe au vert. | <b>até</b> + infinitif personnel.
apotheke | baeckerei | Depois, a farmácia fica mesmo à ___ frente. | sua | seu / dela | Depois, a farmácia fica mesmo à sua frente. | La pharmacie est alors juste devant vous. | <b>à sua frente</b> = devant vous.
post | apotheke | ___ pela farmácia e já lá está. | Passe | Passa-se / Passas | Passe pela farmácia e já lá está. | Passez devant la pharmacie, et vous y êtes. | <b>passar por</b> : passer devant.
lieferwagen |  | A carrinha ___ da rua lateral. | sai | sae / saia-se | A carrinha sai da rua lateral. | La camionnette sort de la rue latérale. | <b>sair</b> → <b>sai</b> ; la camionnette = <b>a carrinha</b>.
fussgaenger | zebrastreifen | Os peões atravessam ___ passadeira. | na | à / pela de | Os peões atravessam na passadeira. | Les piétons traversent sur le passage piéton. | Les piétons = <b>os peões</b>, au Portugal.
baeckerei | anna | A Anna vai já entrar ___ padaria. | na | à / para a de | A Anna vai já entrar na padaria. | Anna va tout de suite entrer dans la boulangerie. | <b>entrar em</b> : na padaria.
ampel-vorne |  | Não atravesse com o sinal ___, por favor! | vermelho | vermelha / encarnado-se | Não atravesse com o sinal vermelho, por favor! | Ne traversez pas au rouge, s'il vous plaît ! | <b>o sinal</b> → <b>vermelho</b>.
cafe |  | O café fica na ___, mesmo ao lado da rua lateral. | esquina | canto / curva | O café fica na esquina, mesmo ao lado da rua lateral. | Le café est au coin, juste à côté de la rue latérale. | Le coin de rue : <b>a esquina</b>.
"""),
"B2": ("De, apesar de et les relatives", """
radweg | buergersteig | Ao longo ___ passeio há uma ciclovia vermelha. | do | de o / ao | Ao longo do passeio há uma ciclovia vermelha. | Le long du trottoir court une piste cyclable rouge. | <b>ao longo de</b> + o = <b>ao longo do</b>.
briefkasten | kiosk | Perto ___ quiosque há um marco do correio amarelo. | do | de o / ao | Perto do quiosque há um marco do correio amarelo. | Non loin du kiosque, il y a une boîte aux lettres jaune. | La boîte aux lettres de rue = <b>o marco do correio</b>.
radfahrer |  | Apesar ___ rua molhada, o ciclista anda depressa. | da | de a / à | Apesar da rua molhada, o ciclista anda depressa. | Malgré la rue mouillée, le cycliste roule vite. | <b>apesar de</b> + a = <b>da</b>.
frau-rot | haltestelle | A mulher, ___ casaco é vermelho, espera pelo autocarro. | cujo | cuja / que o | A mulher, cujo casaco é vermelho, espera pelo autocarro. | La femme au manteau rouge attend le bus. | <b>cujo</b> + casaco.
fussgaenger |  | O homem ___ leva uma mochila atravessa na passadeira. | que | quem / qual | O homem que leva uma mochila atravessa na passadeira. | L'homme qui porte un sac à dos traverse sur le passage piéton. | Sujet : <b>que</b>.
cafe | markise | O café em frente do ___ há mesas tem um toldo vermelho. | qual | que / quem | O café em frente do qual há mesas tem um toldo vermelho. | Le café devant lequel il y a des tables a un store rouge. | <b>em frente do qual</b> ; le store = <b>o toldo</b>.
"""),
"C1": (T_HYPO, """
anna |  | Ela ___ ter-se perdido. | deve | pode-se / tem | Ela deve ter-se perdido. | Elle s'est sans doute perdue. | Déduction sur le passé : <b>deve ter-se perdido</b>.
strasse |  | ___ ter chovido há pouco. | Deve | Pode-se / Tem | Deve ter chovido há pouco. | Il a dû pleuvoir tout à l'heure. | <b>deve ter</b> + participe.
ampel-vorne | anna | Se o semáforo ___ verde, a Anna já teria atravessado. | estivesse | estiver / está | Se o semáforo estivesse verde, a Anna já teria atravessado. | Si le feu était vert, Anna aurait déjà traversé la rue. | Irréel : <b>se estivesse</b>.
lieferwagen | cafe | ___ estar a trazer mercadoria para o café. | Pode | Deve de / Há | Pode estar a trazer mercadoria para o café. | Il apporte peut-être des marchandises pour le café. | Possibilité : <b>poder</b> + estar a.
"""),
},
"markt-gemuese-frucht": {
"B1": (T_MARCHE, """
tomate |  | Queria meio quilo ___ tomates. | de | dos / com | Queria meio quilo de tomates. | Je voudrais une livre de tomates. | Au Portugal, on compte en <b>quilos</b> : <b>meio quilo de</b>.
pilz |  | Quanto ___ os cogumelos? | custam | custa / custem | Quanto custam os cogumelos? | Combien coûtent les champignons ? | Pluriel : <b>custam</b>.
gurke | zucchini | O pepino é mais ___ do que a curgete. | comprido | comprida / longo de | O pepino é mais comprido do que a curgete. | Le concombre est plus long que la courgette. | Long (objet) : <b>comprido</b>.
salat |  | Levo ___ alface. | uma | um / umas | Levo uma alface. | Je prends une salade. | <b>a alface</b> est féminin.
spargel |  | Os espargos são ___ região? | da | de a / na | Os espargos são da região? | Les asperges viennent-elles de la région ? | <b>ser de</b> : de + a = <b>da</b>.
"""),
"B2": (T_PASSIF, """
spargel |  | Os espargos são ___ frescos todas as manhãs. | colhidos | colhidas / colher | Os espargos são colhidos frescos todas as manhãs. | Les asperges sont récoltées fraîches chaque matin. | Passif : <b>são colhidos</b>.
tomate-main | anna | Os tomates ___ a Anna tem na mão estão muito maduros. | que | quem / cujos | Os tomates que a Anna tem na mão estão muito maduros. | Les tomates qu'Anna tient à la main sont très mûres. | Objet : <b>que</b>.
paprika | mais | Ao lado dos pimentos ___ e amarelos está o milho. | vermelhos | vermelhas / vermelho | Ao lado dos pimentos vermelhos e amarelos está o milho. | À côté des poivrons rouges et jaunes, il y a le maïs. | <b>os pimentos</b> → <b>vermelhos</b>.
kuerbis |  | As abóboras já estão ___. | colhidas | colhidos / colheram | As abóboras já estão colhidas. | Les citrouilles sont déjà récoltées. | État : <b>estar</b> + participe accordé.
mangold |  | A acelga, ___ talos são vermelhos e amarelos, é muito saudável. | cujos | cujas / que os | A acelga, cujos talos são vermelhos e amarelos, é muito saudável. | Les blettes aux tiges rouges et jaunes sont très saines. | <b>cujos</b> + talos (masculin pluriel).
"""),
"C1": ("Hypothèses, apesar de, quanto mais", """
tomate-main |  | Apesar ___ preço alto, a Anna leva os tomates de cacho. | do | de o / ao | Apesar do preço alto, a Anna leva os tomates de cacho. | Malgré le prix élevé, Anna prend les tomates en grappe. | <b>apesar do</b>.
tomate |  | Quanto mais maduros estão os tomates, mais intenso é o ___. | sabor | gosto de / sabores | Quanto mais maduros estão os tomates, mais intenso é o sabor. | Plus les tomates sont mûres, plus leur goût est intense. | <b>quanto mais…, mais…</b>.
kuerbis |  | Se a abóbora não ___ tão pesada, a Anna levava-a. | fosse | for / era | Se a abóbora não fosse tão pesada, a Anna levava-a. | Si la citrouille n'était pas si lourde, Anna l'emporterait. | Irréel : <b>se fosse</b>.
pilz |  | Os cogumelos ___ sido apanhados no bosque. | terão | teriam-se / tenham | Os cogumelos terão sido apanhados no bosque. | Les champignons ont sans doute été cueillis en forêt. | Supposition sur le passé : <b>terão sido</b>.
artischocke |  | As alcachofras devem ser bem ___ antes de cozinhar. | lavadas | lavados / lavar | As alcachofras devem ser bem lavadas antes de cozinhar. | Il faut bien laver les artichauts avant de les cuire. | Passif : <b>devem ser</b> + participe accordé.
"""),
},
"markt-gemuese-wurzel": {
"B1": (T_MARCHE, """
karotte |  | Queria um molho ___ cenouras. | de | das / com | Queria um molho de cenouras. | Je voudrais une botte de carottes. | Une botte : <b>um molho de</b>.
kartoffel |  | Dois quilos de ___, por favor. | batatas | batata / as batatas | Dois quilos de batatas, por favor. | Deux kilos de pommes de terre, s'il vous plaît. | Quantité + <b>de</b> + nom pluriel.
blumenkohl |  | Quanto ___ a couve-flor? | custa | custam / custe | Quanto custa a couve-flor? | Combien coûte le chou-fleur ? | Singulier : <b>custa</b>.
kohl | rosenkohl | A couve é ___ do que as couves-de-bruxelas. | maior | mais grande / tão grande | A couve é maior do que as couves-de-bruxelas. | Le chou est plus gros que les choux de Bruxelles. | <b>maior</b>.
knoblauch |  | Ainda preciso de uma cabeça ___ alho para o molho. | de | do / com | Ainda preciso de uma cabeça de alho para o molho. | Il me faut encore une tête d'ail pour la sauce. | <b>uma cabeça de alho</b>.
"""),
"B2": (T_PASSIF, """
kartoffel |  | As batatas ___ colhidas na semana passada. | foram | eram / estiveram | As batatas foram colhidas na semana passada. | Les pommes de terre ont été récoltées la semaine dernière. | Passif au passé : <b>foram</b> + participe.
lauch | kohl | O alho-francês, ___ folhas são verde-escuras, está ao lado da couve. | cujas | cujos / que as | O alho-francês, cujas folhas são verde-escuras, está ao lado da couve. | Le poireau aux feuilles vert foncé est à côté du chou. | <b>cujas</b> + folhas.
radieschen-main |  | A Anna compra rabanetes ___. | frescos | frescas / fresco | A Anna compra rabanetes frescos. | Anna achète des radis frais. | <b>os rabanetes</b> → <b>frescos</b>.
kohl |  | Os legumes ___ se vendem aqui são da região. | que | quem / onde | Os legumes que se vendem aqui são da região. | Les légumes vendus ici viennent de la région. | Après <b>que</b>, le se devant.
zwiebel |  | As cebolas devem ser ___ em lugar seco. | guardadas | guardados / guardar | As cebolas devem ser guardadas em lugar seco. | Les oignons doivent être conservés au sec. | <b>devem ser</b> + participe accordé.
"""),
"C1": ("Hypothèses, devido a, quanto mais", """
kohl |  | ___ à época, em outubro há muita couve. | Devido | Por causa / Graças | Devido à época, em outubro há muita couve. | En raison de la saison, il y a beaucoup de chou en octobre. | <b>devido a</b> = en raison de.
brokkoli |  | Quanto mais frescos são os legumes, ___ vitaminas têm. | mais | o mais / tantas | Quanto mais frescos são os legumes, mais vitaminas têm. | Plus les légumes sont frais, plus ils contiennent de vitamines. | <b>quanto mais…, mais…</b>.
knoblauch |  | Se ___ sabido, não tinha comprado alho no supermercado. | tivesse | tiver / tinha | Se tivesse sabido, não tinha comprado alho no supermercado. | Si j'avais su, je n'aurais pas acheté d'ail au supermarché. | Irréel du passé.
karotte |  | As cenouras parecem ter sido ___ há pouco. | colhidas | colhidos / colher | As cenouras parecem ter sido colhidas há pouco. | Les carottes semblent avoir été récoltées fraîchement. | <b>parecer ter sido</b> + participe.
radieschen-main |  | A Anna ___ comprado os rabanetes para uma salada. | terá | teria-se / tenha | A Anna terá comprado os rabanetes para uma salada. | Anna a sans doute acheté les radis pour une salade. | Supposition : <b>terá</b> + participe.
"""),
},
"markt-obst-heimisch": {
"B1": (T_MARCHE, """
erdbeere |  | Queria uma caixinha ___ morangos. | de | dos / com | Queria uma caixinha de morangos. | Je voudrais une barquette de fraises. | <b>uma caixinha de</b>.
apfel |  | Um quilo de ___, por favor. | maçãs | maçã / as maçãs | Um quilo de maçãs, por favor. | Un kilo de pommes, s'il vous plaît. | <b>um quilo de</b> + pluriel.
pfirsich | aprikose | Os pêssegos são ___ do que os alperces. | maiores | mais grandes / maior | Os pêssegos são maiores do que os alperces. | Les pêches sont plus grosses que les abricots. | <b>maiores</b> (pluriel) ; l'abricot = <b>o alperce</b>.
himbeere |  | Quanto ___ as framboesas? | custam | custa / custem | Quanto custam as framboesas? | Combien coûtent les framboises ? | <b>custam</b>.
pflaume |  | Levo meio quilo ___ ameixas. | de | das / com | Levo meio quilo de ameixas. | Je prends une livre de prunes. | <b>meio quilo de</b>.
"""),
"B2": (T_PASSIF, """
erdbeere |  | São morangos ___ da região. | frescos | frescas / fresco | São morangos frescos da região. | Ce sont des fraises fraîches de la région. | <b>os morangos</b> (masc.) → <b>frescos</b>.
apfel |  | As maçãs são ___ aqui, no Oeste. | cultivadas | cultivados / cultivar | As maçãs são cultivadas aqui, no Oeste. | Les pommes sont cultivées ici, dans l'Ouest. | Passif accordé ; l'Oeste, région de vergers au nord de Lisbonne.
anna | apfel-main | A mulher ___ escolhe uma maçã chama-se Anna. | que | quem / qual | A mulher que escolhe uma maçã chama-se Anna. | La femme qui choisit une pomme s'appelle Anna. | Sujet : <b>que</b>.
brombeere | kirsche | A caixa ___ estão as amoras está ao lado das cerejas. | onde | que / cuja | A caixa onde estão as amoras está ao lado das cerejas. | La caisse où sont les mûres est à côté des cerises. | <b>onde</b>.
rhabarber |  | O ruibarbo é muitas vezes ___ para fazer bolos. | usado | usada / usar | O ruibarbo é muitas vezes usado para fazer bolos. | La rhubarbe est souvent utilisée pour faire des gâteaux. | Passif : <b>é usado</b>.
"""),
"C1": ("Hypothèses, tendo em conta, quanto mais", """
erdbeere |  | Quanto mais maduros estão os morangos, mais ___ são. | doces | doce / dulces | Quanto mais maduros estão os morangos, mais doces são. | Plus les fraises sont mûres, plus elles sont sucrées. | <b>quanto mais…, mais…</b>.
apfel |  | ___ em conta as longas viagens, prefiro fruta da terra. | Tendo | Tendo-se / Tenho | Tendo em conta as longas viagens, prefiro fruta da terra. | Vu les longs trajets de transport, je préfère acheter des fruits d'ici. | <b>tendo em conta</b> = vu, compte tenu de.
kirsche |  | Se as cerejas ___ mais baratas, levava dois quilos. | fossem | forem / são | Se as cerejas fossem mais baratas, levava dois quilos. | Si les cerises étaient moins chères, j'en prendrais deux kilos. | Irréel : <b>se fossem</b>.
rhabarber |  | Embora o ruibarbo ___ ácido, a Anna gosta de fazer bolos com ele. | seja | é / for | Embora o ruibarbo seja ácido, a Anna gosta de fazer bolos com ele. | Bien que la rhubarbe soit acide, Anna aime faire des gâteaux avec. | <b>embora</b> + conjuntivo.
himbeere |  | As framboesas ___ sido apanhadas hoje de manhã. | terão | teriam-se / tenham | As framboesas terão sido apanhadas hoje de manhã. | Les framboises ont sans doute été cueillies ce matin. | <b>terão sido</b>.
"""),
},
"markt-obst-sued": {
"B1": (T_MARCHE, """
ananas |  | Quanto custa ___ ananás? | um | uma / uns | Quanto custa um ananás? | Combien coûte un ananas ? | <b>o ananás</b> : masculin (et le mot du Portugal ; au Brésil, abacaxi).
wassermelone |  | Levo uma fatia ___ melancia, por favor. | de | da / com | Levo uma fatia de melancia, por favor. | Je prends un morceau de pastèque, s'il vous plaît. | <b>uma fatia de</b>.
wassermelone | melone | A melancia é ___ do que o melão. | maior | mais grande / maiora | A melancia é maior do que o melão. | La pastèque est plus grosse que le melon. | <b>maior</b>.
mango |  | As mangas já estão ___? | maduras | maduros / madura | As mangas já estão maduras? | Les mangues sont-elles déjà mûres ? | <b>as mangas</b> → <b>maduras</b>.
zitrone |  | Queria três ___. | limões | limãos / limães | Queria três limões. | Je voudrais trois citrons. | <b>o limão</b> → <b>os limões</b>.
"""),
"B2": (T_PASSIF, """
banane |  | A fruta tropical é quase sempre ___ de barco. | importada | importado / importar | A fruta tropical é quase sempre importada de barco. | Les fruits exotiques sont généralement importés par bateau. | <b>a fruta</b> (collectif) → <b>importada</b>.
mango |  | A manga, ___ casca é vermelha e verde, já está madura. | cuja | cujo / que a | A manga, cuja casca é vermelha e verde, já está madura. | La mangue à la peau rouge et verte est déjà mûre. | <b>cuja</b> + casca.
papaya |  | Há uma papaia ___ em cima das outras. | cortada | cortado / cortar | Há uma papaia cortada em cima das outras. | Une papaye coupée est posée sur les autres. | Participe accordé.
banane | anna | As bananas ___ a Anna leva vêm da Madeira. | que | quem / cujas | As bananas que a Anna leva vêm da Madeira. | Les bananes qu'Anna prend viennent de Madère. | Objet : <b>que</b> ; la banane de Madère, fierté portugaise.
kokosnuss |  | O coco já está ___. | aberto | aberta / abrido | O coco já está aberto. | La noix de coco est déjà ouverte. | <b>o coco</b> → <b>aberto</b>.
"""),
"C1": ("Hypothèses, apesar de, quanto mais", """
mango |  | Apesar ___ longa viagem, as mangas aqui são bastante baratas. | da | de a / à | Apesar da longa viagem, as mangas aqui são bastante baratas. | Malgré leur long trajet, les mangues sont assez bon marché ici. | <b>apesar da</b>.
feige |  | Quanto mais escuros são os figos, mais ___ são. | doces | doce / dulces | Quanto mais escuros são os figos, mais doces são. | Plus les figues sont foncées, plus elles sont sucrées. | <b>quanto mais…, mais…</b>.
ananas |  | Se a Anna ___ mais tempo, comprava um ananás e descascava-o. | tivesse | tiver / tem | Se a Anna tivesse mais tempo, comprava um ananás e descascava-o. | Si Anna avait plus de temps, elle achèterait un ananas et l'éplucherait. | Irréel : <b>se tivesse</b>.
avocado |  | Os abacates não ___ guardar no frigorífico. | se devem | devem-se-se / se deve | Os abacates não se devem guardar no frigorífico. | Il ne faut pas conserver les avocats au réfrigérateur. | Après <b>não</b>, le se devant ; accord avec abacates.
kokosnuss |  | O coco ___ ter sido aberto com um martelo. | deve | pode-se / tem | O coco deve ter sido aberto com um martelo. | La noix de coco a dû être ouverte avec un marteau. | Déduction sur le passé : <b>deve ter sido</b>.
"""),
},
"post": {
"B1": ("Le pronom complément : lhe, lha, -lhe", """
brief | anna | A Anna envia uma carta ___ mãe. | à | a / da | A Anna envia uma carta à mãe. | Anna envoie une lettre à sa mère. | <b>enviar algo a alguém</b> : a + a = <b>à</b>.
mann | anna | O homem dá-___ um recibo. | lhe | a / se | O homem dá-lhe um recibo. | L'homme lui donne un reçu. | À elle : <b>lhe</b>.
brief | mann | A Anna dá-___ a carta. | lhe | o / se | A Anna dá-lhe a carta. | Anna lui donne la lettre. | À lui : <b>lhe</b>.
brief | mann | A carta? Ela dá-___. | lha | lhe a / a | A carta? Ela dá-lha. | La lettre ? Elle la lui donne. | lhe + a = <b>lha</b>.
paket-3 | frau | A senhora quer enviar uma encomenda ___ neto. | ao | o / do | A senhora quer enviar uma encomenda ao neto. | La femme veut envoyer un colis à son petit-fils. | a + o = <b>ao</b> ; le colis = <b>a encomenda</b>.
briefmarke |  | Podes comprar-___ um selo? | me | mim / eu | Podes comprar-me um selo? | Tu peux m'acheter un timbre ? | <b>me</b>, après l'infinitif.
anna | mann | A Anna mostra o cartão de cidadão ___ homem. | ao | o / do | A Anna mostra o cartão de cidadão ao homem. | Anna montre sa carte d'identité à l'homme. | La carte d'identité portugaise : <b>o cartão de cidadão</b>.
mann | frau | O homem explica o preço ___ senhora. | à | a / da | O homem explica o preço à senhora. | L'homme explique le prix à la femme. | a + a = <b>à</b>.
"""),
"B2": ("Le passif", """
paket | waage | A encomenda está a ser ___. | pesada | pesado / pesar | A encomenda está a ser pesada. | Le colis est en train d'être pesé. | <b>a encomenda</b> → <b>pesada</b>.
brief |  | A carta vai ser ___ amanhã. | entregue | entregada / entregar | A carta vai ser entregue amanhã. | La lettre sera distribuée demain. | <b>entregar</b> → <b>entregue</b> (participe court, partout).
paket-2 |  | A encomenda ___ enviada ontem. | foi | era / esteve | A encomenda foi enviada ontem. | Le colis a été envoyé hier. | Passif au passé : <b>foi</b>.
brief-2 | korb | As cartas já estão ___. | separadas | separados / separar | As cartas já estão separadas. | Les lettres sont déjà triées. | État : <b>estar</b> + participe accordé.
paket-4 |  | Aqui também se ___ encomendas. | enviam | envia / enviem | Aqui também se enviam encomendas. | Ici, on envoie aussi des colis. | Le se passif s'accorde : <b>enviam</b> ; après também, devant.
briefmarke | umschlag | O selo tem de ser ___ no envelope. | colado | colada / colar | O selo tem de ser colado no envelope. | Le timbre doit être collé sur l'enveloppe. | <b>tem de ser</b> + participe.
"""),
"C1": (T_HYPO, """
brief | anna | A carta ___ ser para alguém importante. | deve | pode-se / tem | A carta deve ser para alguém importante. | La lettre doit être pour quelqu'un d'important. | Déduction : <b>dever</b>.
paket-3 | frau | A encomenda da senhora idosa ___ ser um presente. | pode | deve de / há | A encomenda da senhora idosa pode ser um presente. | Le colis de la vieille dame est peut-être un cadeau. | Possibilité : <b>poder</b>.
brief |  | A carta ___ chegar daqui a dois dias. | deverá | deveria-se / deva | A carta deverá chegar daqui a dois dias. | La lettre devrait arriver dans deux jours. | Probable : <b>deverá</b>.
schalter |  | ___ que esta estação dos correios vai fechar em breve. | Dizem | Diz-se-lhe / Digam | Dizem que esta estação dos correios vai fechar em breve. | Il paraît que cette poste va bientôt fermer. | Le ouï-dire ; la poste = <b>os correios</b>.
"""),
},
"stadtplatz": {
"B1": ("Há, está, fica : situer sur la place", """
eis | anna | Hoje a Anna ___ um gelado. | come | coma / comendo | Hoje a Anna come um gelado. | Aujourd'hui, Anna mange une glace. | Le portugais garde l'ordre sujet-verbe après <b>hoje</b>.
anna | brunnen | A Anna está ___ junto ao chafariz. | sentada | sentado / sentar | A Anna está sentada junto ao chafariz. | C'est au bord de la fontaine qu'Anna est assise. | <b>a Anna</b> → <b>sentada</b> ; la fontaine = <b>o chafariz</b>.
hund | anna | À frente da Anna ___ um cão sentado. | está | há-se / é | À frente da Anna está um cão sentado. | Devant Anna, il y a un chien assis. | Un être précis à un endroit : <b>está</b>.
mann | zeitung | Debaixo do guarda-sol, um homem ___ o jornal. | lê | lê-se / leia | Debaixo do guarda-sol, um homem lê o jornal. | Sous le parasol, un homme lit le journal. | <b>ler</b> → <b>lê</b>.
platz |  | Ao sábado ___ muita gente à praça. | vem | vêm-se / há | Ao sábado vem muita gente à praça. | Le samedi, beaucoup de gens viennent sur la place. | <b>muita gente</b> est singulier : <b>vem</b> ; le samedi = <b>ao sábado</b>.
denkmal |  | Em cima do monumento ___ um homem de bronze. | há | têm / estão | Em cima do monumento há um homem de bronze. | Sur le monument se dresse un homme en bronze. | Il y a : <b>há</b>.
kaffee | anna | Depois, a Anna ___ um café. | toma | tome / tomando | Depois, a Anna toma um café. | Ensuite, Anna boit un café. | Boire un café : <b>tomar um café</b>.
strassenbahn |  | Atrás da praça ___ um elétrico. | passa | passa-se / passe | Atrás da praça passa um elétrico. | Derrière la place passe un tram. | Le tram de Lisbonne : <b>o elétrico</b>.
"""),
"B2": ("Como se + conjuntivo imparfait", """
hund |  | O cão olha como se ___ fome. | tivesse | tem / tenha | O cão olha como se tivesse fome. | Le chien regarde comme s'il avait faim. | <b>como se</b> + imperfeito do conjuntivo.
anna | hund | A Anna ri-se como se o cão lhe ___ contado uma anedota. | tivesse | tinha / tiver | A Anna ri-se como se o cão lhe tivesse contado uma anedota. | Anna rit comme si le chien lui avait raconté une blague. | Pour le passé : <b>como se tivesse</b> + participe.
mann |  | O senhor lê como se ___ sozinho na praça. | estivesse | está / esteja | O senhor lê como se estivesse sozinho na praça. | Le monsieur lit comme s'il était seul sur la place. | <b>estivesse</b>.
denkmal |  | A estátua parece que ___ começar a andar. | vai | vá / ia-se | A estátua parece que vai começar a andar. | La statue a l'air de vouloir se mettre en marche. | <b>parece que vai</b> : on dirait qu'elle va.
himmel |  | Está tanto calor como se já ___ verão. | fosse | for / é | Está tanto calor como se já fosse verão. | Il fait aussi chaud que si c'était déjà l'été. | <b>como se fosse</b>.
vogel-2 | platz | Os pombos andam por ali como se a praça ___ deles. | fosse | for / é | Os pombos andam por ali como se a praça fosse deles. | Les pigeons se promènent comme si la place leur appartenait. | <b>como se fosse deles</b>.
"""),
"C1": (T_HYPO, """
anna | hund | Ela ___ achar o cão engraçado. | deve | pode-se / tem | Ela deve achar o cão engraçado. | Elle doit trouver le chien drôle. | Déduction : <b>dever</b>.
hund | eis | ___ o cão ganhe um bocado de gelado. | Talvez | Se calhar / Deve | Talvez o cão ganhe um bocado de gelado. | Le chien aura peut-être un morceau de glace. | <b>talvez</b> + conjuntivo.
mann | tisch | O senhor ___ sentar-se aqui todos os sábados. | deve | pode-se / tem | O senhor deve sentar-se aqui todos os sábados. | Le monsieur est sans doute assis ici tous les samedis. | Probable : <b>dever</b>.
brunnen |  | O chafariz ___ mais de cem anos. | teria | terá-se / tenha | O chafariz teria mais de cem anos. | La fontaine aurait plus de cent ans. | Le conditionnel de la rumeur.
"""),
},
"ubahn": {
"B1": ("E, mas, ou, porque, mas sim", """
fahrkarte | mark | O Mark tem um bilhete ___ um café. | e | mas / ou | O Mark tem um bilhete e um café. | Mark a un billet et un café. | <b>e</b> = et.
mark | ubahn | O Mark despacha-se ___ o metro vai partir. | porque | mas / ou | O Mark despacha-se porque o metro vai partir. | Mark se dépêche, car le métro va partir. | La cause : <b>porque</b> (ou <b>pois</b>).
mann | gitarre | O homem não canta, ___ toca guitarra. | mas sim | mas também / senão que | O homem não canta, mas sim toca guitarra. | L'homme ne chante pas, il joue de la guitare. | Après une négation, la rectification : <b>mas sim</b>.
brezel | zeitung | Queres um pastel ___ um jornal? | ou | e / mas | Queres um pastel ou um jornal? | Tu veux une pâtisserie ou un journal ? | <b>ou</b> = ou.
kiosk | brezel | O quiosque é pequeno, ___ tem muitos pastéis. | mas | ou / porque | O quiosque é pequeno, mas tem muitos pastéis. | Le kiosque est petit, mais il a beaucoup de pâtisseries. | <b>mas</b> = mais.
regenschirm | frau | A senhora tem um guarda-chuva, ___ lá fora está a chover. | pois | mas / ou | A senhora tem um guarda-chuva, pois lá fora está a chover. | La dame a un parapluie, car il pleut dehors. | <b>pois</b> = car.
hund | bank | O cão não ladra, ___ está sentado ao lado do banco. | mas sim | ou / e não | O cão não ladra, mas sim está sentado ao lado do banco. | Le chien n'aboie pas, il est assis tranquillement à côté du banc. | <b>mas sim</b>.
kaffee | mark | O Mark bebe o café ___ entra no metro. | e | mas / ou | O Mark bebe o café e entra no metro. | Mark boit du café et monte dans le métro. | <b>e</b>.
"""),
"B2": ("Se, caso : la condition", """
ubahn | mark | Caso o metro ___ atrasado, o Mark apanha o autocarro. | venha | vem / vier | Caso o metro venha atrasado, o Mark apanha o autocarro. | Si jamais le métro a du retard, Mark prend le bus. | <b>caso</b> + conjuntivo présent.
mark | tuer | Se o Mark não ___ depressa, perde o metro. | entrar | entra / entre | Se o Mark não entrar depressa, perde o metro. | Si Mark ne monte pas vite, il rate le métro. | <b>se</b> + futur : futuro do conjuntivo.
regenschirm | frau | Quando ___, a senhora leva o guarda-chuva. | chove | chova / chover-se | Quando chove, a senhora leva o guarda-chuva. | Quand il pleut, la dame prend son parapluie. | Une habitude : <b>quando</b> + indicatif.
brezel |  | Se ___ fome, compra um pastel! | tiveres | tens / tenhas | Se tiveres fome, compra um pastel! | Si tu as faim, achète-toi une pâtisserie ! | <b>se tiveres</b>.
kaffee | mark | Se o Mark ___ lugar sentado, bebe o café. | arranjar | arranja / arranje | Se o Mark arranjar lugar sentado, bebe o café. | Si Mark trouve une place assise, il boit son café. | <b>arranjar lugar</b> = trouver une place.
fahrkarte |  | Só se pode entrar se se ___ bilhete. | tiver | tem / tenha | Só se pode entrar se se tiver bilhete. | On n'a le droit de monter que si l'on a un billet. | <b>se se tiver</b> : « si on a ».
"""),
"C1": (T_HYPO, """
mark |  | Ele ___ estar bem-disposto. | deve | pode-se / tem | Ele deve estar bem-disposto. | Il doit être de bonne humeur. | <b>bem-disposto</b> = de bonne humeur.
frau | koffer | A senhora ___ ir para o aeroporto. | pode | deve de / há | A senhora pode ir para o aeroporto. | La dame part peut-être à l'aéroport. | Possibilité : <b>poder</b>.
hund | frau | O cão ___ da senhora. | será | seja / foi-se | O cão será da senhora. | Le chien appartient sans doute à la dame. | Futur de supposition.
treppe |  | Esta estação de metro ___ mais de cem anos. | teria | terá-se / tenha | Esta estação de metro teria mais de cem anos. | Cette station de métro aurait plus de cent ans. | Le conditionnel de la rumeur.
"""),
},
"weihnachtsmarkt": {
"B1": ("Le pronom complément : compra-a, dá-lhe", """
stern | mark | A estrela? O Mark ___. | compra-a | compra-la / a compra | A estrela? O Mark compra-a. | L'étoile ? Mark l'achète. | <b>a</b> après le verbe : <b>compra-a</b>.
mann | mark | O homem dá-___ a estrela. | lhe | o / a | O homem dá-lhe a estrela. | L'homme lui donne l'étoile. | À lui : <b>lhe</b>.
tasse | handschuh | A caneca? O Mark segura-___ com luvas. | a | la / lhe | A caneca? O Mark segura-a com luvas. | La tasse ? Mark la tient avec des gants. | <b>a</b> (la caneca).
brezel-2 | kind | Os pastéis? Foi a mãe que os ___. | comprou | comprou-os / comprava | Os pastéis? Foi a mãe que os comprou. | Les pâtisseries ? C'est la mère qui les a achetées. | Après <b>que</b>, le pronom devant : <b>que os comprou</b>.
kind | frau | Ela dá-___ a mão. | lhe | o / se | Ela dá-lhe a mão. | Elle lui donne la main. | <b>dar a mão a alguém</b> : <b>lhe</b>.
hund | mark | O cão olha para ___. | ele | o / lhe | O cão olha para ele. | Le chien le regarde. | <b>olhar para</b> + pronom tonique : <b>para ele</b>.
frau | brezel-2 | Ela gosta dos ___. | pastéis | pastels / pastelões | Ela gosta dos pastéis. | Elle aime les pâtisseries. | <b>o pastel</b> → <b>os pastéis</b>.
kerze | mark | As velas? O Mark compra-___ para a mãe. | as | las / lhes | As velas? O Mark compra-as para a mãe. | Les bougies ? Mark les achète pour sa mère. | <b>as</b> : compra-as.
"""),
"B2": ("Les noms composés : nom + de + nom", """
stand |  | O mercado ___ Natal é muito bonito. | de | do / da | O mercado de Natal é muito bonito. | Le marché de Noël est très joli. | Le portugais relie par <b>de</b> : <b>mercado de Natal</b>.
lichterkette |  | As luzes ___ Natal brilham. | de | do / das | As luzes de Natal brilham. | Les guirlandes lumineuses de Noël brillent. | <b>as luzes de Natal</b>.
stern |  | É uma estrela ___ madeira. | de | da / em | É uma estrela de madeira. | C'est une étoile en bois. | La matière : <b>de</b>.
baum |  | A árvore ___ Natal está na praça. | de | do / da | A árvore de Natal está na praça. | Le sapin de Noël est sur la place. | <b>a árvore de Natal</b>.
handschuh |  | Comprei umas luvas ___ inverno. | de | do / para o | Comprei umas luvas de inverno. | J'ai acheté des gants d'hiver. | <b>luvas de inverno</b>.
uhr | turm | O relógio ___ torre marca as seis. | da | de / na | O relógio da torre marca as seis. | L'horloge du clocher indique six heures. | Une tour précise : <b>da torre</b>.
"""),
"C1": (T_HYPO, """
mark |  | Ele ___ gostar do mercado de Natal. | deve | pode-se / tem | Ele deve gostar do mercado de Natal. | Il doit aimer le marché de Noël. | Déduction : <b>dever</b>.
stern | mark | A estrela ___ ser um presente para a mãe dele. | pode | deve de / há | A estrela pode ser um presente para a mãe dele. | L'étoile est peut-être un cadeau pour sa mère. | Possibilité : <b>poder</b>.
hund | mann | O cão ___ do homem da banca. | será | seja / foi-se | O cão será do homem da banca. | Le chien appartient sans doute à l'homme de l'étal. | Futur de supposition ; l'étal = <b>a banca</b>.
kirche |  | Este mercado de Natal ___ o mais antigo da cidade. | seria | será-se / seja | Este mercado de Natal seria o mais antigo da cidade. | Ce marché de Noël serait le plus ancien de la ville. | Le conditionnel de la rumeur.
"""),
},
"zug": {
"B1": ("En voyage : de, para, por, em", """
mark |  | O Mark viaja ___ comboio. | de | no / em o | O Mark viaja de comboio. | Mark voyage en train. | Le moyen : <b>de comboio</b>.
berg | mark | Ele vai ___ a serra. | para | à / na | Ele vai para a serra. | Il va à la montagne. | <b>ir para</b> ; la montagne (région) = <b>a serra</b>.
fenster | mark | Ele olha ___ janela. | pela | para a / da | Ele olha pela janela. | Il regarde par la fenêtre. | À travers : <b>por</b> + a = <b>pela</b>.
koffer | mark | Ele ___ a mala no porta-bagagens. | pôs | punha / põe | Ele pôs a mala no porta-bagagens. | Il a posé sa valise sur le porte-bagages. | <b>pôr</b> → <b>pôs</b>.
koffer |  | Agora a mala está ___ porta-bagagens. | no | ao / para o | Agora a mala está no porta-bagagens. | Maintenant, la valise est sur le porte-bagages. | Position : <b>no</b>.
kuh | wiese | As vacas estão ___ prado. | no | ao / para o | As vacas estão no prado. | Les vaches sont dans le pré. | <b>no prado</b>.
fluss | bruecke | O comboio passa ___ cima do rio. | por | em / de | O comboio passa por cima do rio. | Le train traverse la rivière. | <b>passar por cima de</b> : passer au-dessus.
fahrkarte | tisch | O Mark ___ o bilhete em cima da mesa. | pousou | pousava / pousa | O Mark pousou o bilhete em cima da mesa. | Mark a posé le billet sur la table. | <b>pousar</b> → <b>pousou</b>.
"""),
"B2": (T_PASSIF, """
mark | fenster | O homem ___ olha pela janela chama-se Mark. | que | quem / qual | O homem que olha pela janela chama-se Mark. | L'homme qui regarde par la fenêtre s'appelle Mark. | Sujet : <b>que</b>.
dorf | kirche | A aldeia, ___ igreja tem uma torre pontiaguda, fica no vale. | cuja | cujo / que a | A aldeia, cuja igreja tem uma torre pontiaguda, fica no vale. | Le village dont l'église a un clocher pointu est dans la vallée. | <b>cuja</b> + igreja.
tisch | laptop | A mesa em ___ está o portátil é cinzenta. | que | qual / quem | A mesa em que está o portátil é cinzenta. | La table sur laquelle est l'ordinateur portable est grise. | <b>em que</b> (ou <b>na qual</b>).
fahrkarte |  | O bilhete tem de ser ___ no comboio. | validado | validada / validar | O bilhete tem de ser validado no comboio. | Le billet doit être contrôlé dans le train. | Passif : <b>tem de ser</b> + participe.
kaffee |  | O café ainda não foi ___. | bebido | bebida / beber | O café ainda não foi bebido. | Le café n'est pas encore bu. | Passif : <b>foi bebido</b>.
zeitung | tisch | O jornal, ___ fotografias mostram florestas, está em cima da mesa. | cujas | cujos / que as | O jornal, cujas fotografias mostram florestas, está em cima da mesa. | Le journal dont les photos montrent des forêts est sur la table. | <b>cujas</b> + fotografias.
"""),
"C1": (T_HYPO, """
fenster | mark | A paisagem ___ agradar-lhe. | deve | pode-se / tem | A paisagem deve agradar-lhe. | Le paysage doit lui plaire. | Déduction : <b>dever</b>.
schal |  | O cachecol vermelho ___ ser de alguém que volta já. | pode | deve de / há | O cachecol vermelho pode ser de alguém que volta já. | L'écharpe rouge appartient peut-être à quelqu'un qui va revenir. | Possibilité : <b>poder</b>.
uhr |  | O comboio ___ chegar ao Porto daqui a uma hora. | deverá | deveria-se / deva | O comboio deverá chegar ao Porto daqui a uma hora. | Le train devrait arriver à Porto dans une heure. | Probable : <b>deverá</b>.
dorf |  | ___ que nesta aldeia se faz o melhor queijo da região. | Dizem | Diz-se-lhe / Digam | Dizem que nesta aldeia se faz o melhor queijo da região. | Il paraît que dans ce village, on trouve le meilleur fromage de la région. | Le ouï-dire ; après <b>que</b>, le se devant.
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
