# -*- coding: utf-8 -*-
"""Les questions des tuiles de grammaire portugaises (11 nov. 2026, lot P5).
Format : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python portugais/outils/construire.py.
Portugais du Portugal ; la variante Bresil est derivee par bresil.py.
BROUILLON : a faire relire par un lusophone du Portugal.
"""

Q = {
# ------------------------------------------------------------------ Pronoms
"pronomesTonicosPtExercises": """
Este presente é para ___. | ti | tu / te | Ce cadeau est pour toi. | Après une préposition : mim, ti, ele, ela…
Queres vir ___? | comigo | com mim / com eu | Tu veux venir avec moi ? | Com + mim = comigo.
Vou ao cinema ___. | contigo | com ti / com tu | Je vais au cinéma avec toi. | Com + ti = contigo.
Os meus pais jantam ___ ao domingo. | connosco | com nós / conosco | Mes parents dînent avec nous le dimanche. | Com + nós = connosco (au Portugal, deux n).
Isto é para ___ ou para mim? | ti | tu / te | C'est pour toi ou pour moi ? | Après para : ti.
Sem ___ não consigo! | ti | tu / te | Sans toi, je n'y arrive pas ! | Après sem : ti.
Ela pensa muito em ___. | mim | me / eu | Elle pense beaucoup à moi. | Après em : mim.
O senhor traz o passaporte ___? | consigo | com si / com ele | Vous avez votre passeport sur vous ? | Com + si (o senhor) = consigo.
Gosto muito de ___, Ana. | ti | tu / te | Je t'aime beaucoup, Ana. | Gostar de + ti.
Entre ___ e mim não há segredos. | ti | tu / te | Entre toi et moi, il n'y a pas de secrets. | Après entre : ti.
Falaram de ___? | nós | nos / connosco | Ils ont parlé de nous ? | Après de : nós.
Comprei isto a pensar ___. | nele | em ele / no ele | J'ai acheté ça en pensant à lui. | Em + ele = nele.
Esta mala é ___. | dela | de ela / sua dela | Ce sac est à elle. | De + ela = dela.
Já falei ___. | com eles | comeles / com os | J'ai déjà parlé avec eux. | Com eles : pas de contraction.
Para ___, o melhor é o mar. | mim | me / eu | Pour moi, le mieux, c'est la mer. | Après para : mim.
""",
"possessivosTuilePtExercises": """
Esta é ___ irmã, a Rita. | a minha | minha a / o meu | Voici ma sœur, Rita. | Au Portugal : l'article devant le possessif.
___ carro está na garagem. | O meu | Meu o / A minha | Ma voiture est au garage. | O meu + nom masculin.
Onde estão ___ chaves? | as tuas | os teus / tuas as | Où sont tes clés ? | As tuas + nom féminin pluriel.
O Pedro perdeu o telemóvel ___. | dele | seu dele / dela | Pedro a perdu son téléphone. | À lui : dele (après le nom).
A Ana e a casa ___ são lindas. | dela | dele / sua dela | Ana et sa maison sont magnifiques. | À elle : dela.
Os vizinhos venderam a casa ___. | deles | dele / seus | Les voisins ont vendu leur maison. | À eux : deles.
___ filhos estudam em Coimbra. | Os nossos | As nossas / Nossos os | Nos enfants étudient à Coimbra. | Os nossos + nom masculin pluriel.
O senhor esqueceu-se do ___ casaco. | seu | teu / dele | Vous avez oublié votre manteau. | À la personne qu'on vouvoie : o seu.
Este livro é ___? — É meu. | teu | tua / ti | Ce livre est à toi ? — Il est à moi. | Après é, l'article tombe souvent : é teu, é meu.
A ___ casa é muito pequena. | vossa | vosso / seu | Votre maison est très petite. | À vous tous : o vosso, a vossa.
Um amigo ___ vem jantar. | meu | o meu / de mim | Un ami à moi vient dîner. | Après un, pas d'article : um amigo meu.
Lavei ___ mãos. | as | as minhas / minhas | Je me suis lavé les mains. | Le corps : l'article, pas le possessif.
""",
# ------------------------------------------------------------------ Nombres
"horasDatasPtExercises": """
___ três horas. | São | É / Está | Il est trois heures. | Dès deux heures : são.
___ uma hora. | É | São / Está | Il est une heure. | Une heure : é (singulier).
São duas e ___. | meia | meio / metade | Il est deux heures et demie. | Et demie : e meia.
São cinco menos ___. | um quarto | quarto / um quarta | Il est cinq heures moins le quart. | Moins le quart : menos um quarto.
Almoçamos ao ___. | meio-dia | meia-dia / meio dia | Nous déjeunons à midi. | Midi : o meio-dia.
O comboio parte ___ oito. | às | as / a | Le train part à huit heures. | À + as = às.
O jogo é ___ uma. | à | a / às | Le match est à une heure. | À une heure : à uma.
Hoje é dia ___ de março. | primeiro | um / primeira | Aujourd'hui, c'est le premier mars. | Le 1er : dia primeiro (ou dia um).
Estamos em ___. | 2026 | o 2026 / no 2026 | Nous sommes en 2026. | L'année : em 2026, sans article.
A reunião é ___ segunda-feira. | na | à / em a | La réunion est lundi. | Un jour : na segunda-feira.
O museu abre ___ terça a domingo. | de | da / desde | Le musée ouvre du mardi au dimanche. | De… a… : de terça a domingo.
São onze ___ dez. | e | mais / com | Il est onze heures dix. | Les minutes : onze e dez.
Chego ___ das nove. | por volta | pela volta / a volta | J'arrive vers neuf heures. | Vers : por volta de.
""",
"numerosConcordanciaPtExercises": """
Tenho ___ irmãs. | duas | dois / doas | J'ai deux sœurs. | Dois devient duas au féminin.
Comprei ___ maçã. | uma | um / umas | J'ai acheté une pomme. | Um, uma : accordé.
A sala tem ___ cadeiras. | duzentas | duzentos / dois centos | La salle a deux cents chaises. | Les centaines s'accordent : duzentas cadeiras.
Moro no ___ andar. | segundo | dois / segunda | J'habite au deuxième étage. | L'ordinal s'accorde : o segundo andar.
É a ___ vez que venho a Lisboa. | terceira | terceiro / três | C'est la troisième fois que je viens à Lisbonne. | A vez : terceira.
O bilhete custa ___ euros. | cem | cento / centos | Le billet coûte cent euros. | Cent tout seul : cem.
A cidade tem ___ e vinte mil habitantes. | cento | cem / centos | La ville a cent vingt mille habitants. | Cent suivi d'un nombre : cento.
Portugal tem dez ___ de habitantes. | milhões | milhão / mil | Le Portugal a dix millions d'habitants. | Milhão, milhões + de.
Comi ___ da pizza. | metade | meia / meio | J'ai mangé la moitié de la pizza. | La moitié : a metade.
Quero ___ quilo de queijo. | meio | meia / metade | Je veux un demi-kilo de fromage. | Un demi-kilo : meio quilo (meio devant un nom masculin).
São ___ e meia. | duas | dois / doze | Il est deux heures et demie. | As horas sont féminines : duas.
Pagou o ___ do preço. | dobro | duplo / dois | Il a payé le double du prix. | Le double : o dobro.
Foi o ___ a chegar. | último | ultimo / última | Il a été le dernier à arriver. | Dernier : último (accent).
Mil ___ euros é muito dinheiro. | e quinhentos | quinhentos / cinco cem | Mille cinq cents euros, c'est beaucoup d'argent. | Mil e quinhentos.
""",
# ------------------------------------------------------------------ Prepositions
"prepContracoesPtExercises": """
Moro ___ Porto. | no | em o / ao | J'habite à Porto. | Em + o = no (o Porto prend l'article).
O livro está ___ mesa. | na | em a / à | Le livre est sur la table. | Em + a = na.
Venho ___ Brasil. | do | de o / ao | Je viens du Brésil. | De + o = do.
Vamos ___ praia. | à | a a / na | Allons à la plage. | A + a = à.
Dei o livro ___ professor. | ao | a o / o | J'ai donné le livre au professeur. | A + o = ao.
Passei ___ ponte. | pela | por a / pelo | Je suis passé par le pont. | Por + a = pela.
Gosto ___ teu casaco. | do | de o / o | J'aime ton manteau. | Gostar de + o = do.
Ela está ___ escritório. | no | em o / ao | Elle est au bureau. | Em + o = no.
Moro ___ Lisboa. | em | na / no | J'habite à Lisbonne. | Lisboa ne prend pas d'article : em Lisboa.
Esta carta é ___ Ana. | da | de a / à | Cette lettre est d'Ana. | De + a Ana = da Ana.
Trabalho ___ hospital. | num | em um / dum | Je travaille dans un hôpital. | Em + um = num.
Saiu ___ casa às oito. | de | da / desde | Il est parti de chez lui à huit heures. | Casa (chez soi) : sans article, de casa.
Vou ___ casa da minha mãe. | a | à / na | Je vais chez ma mère. | Ir a casa de alguém : chez quelqu'un.
Obrigado ___ ajuda. | pela | por a / para a | Merci pour ton aide. | Por + a = pela.
""",
"prepLugarTempoPtExercises": """
Cheguei ___ duas semanas. | há | desde / faz | Je suis arrivé il y a deux semaines. | Il y a + durée : há.
Moro aqui ___ 2020. | desde | há / de | J'habite ici depuis 2020. | Depuis + date : desde.
Moro aqui ___ três anos. | há | desde / durante | J'habite ici depuis trois ans. | Depuis + durée : há.
O comboio parte ___ dez minutos. | daqui a | em / há | Le train part dans dix minutes. | Dans + durée (futur) : daqui a.
Choveu ___ a noite toda. | durante | por todo / desde | Il a plu toute la nuit. | Pendant : durante.
Trabalho ___ nove às cinco. | das | de / desde | Je travaille de neuf heures à cinq heures. | De… à… : das… às…
Fico ___ sexta-feira. | até | a / para | Je reste jusqu'à vendredi. | Jusqu'à : até.
O gato está ___ cama. | debaixo da | debaixo a / sob a | Le chat est sous le lit. | Debaixo de + a = debaixo da.
A farmácia fica ___ banco. | ao lado do | ao lado o / junto o | La pharmacie est à côté de la banque. | Ao lado de + o = ao lado do.
Encontramo-nos ___ estação. | em frente da | em frente a da / diante a | Retrouvons-nous en face de la gare. | Em frente de + a = em frente da.
A escola fica ___ do rio. | perto | ao pé / perto a | L'école est près de la rivière. | Près de : perto de.
___ inverno, anoitece cedo. | No | Em o / Ao | En hiver, il fait nuit tôt. | Une saison : no inverno.
A loja abre ___ partir das nove. | a | à / de | Le magasin ouvre à partir de neuf heures. | À partir de : a partir de.
___ manhã, bebo um café. | De | À / Na | Le matin, je bois un café. | Le matin : de manhã ; le soir : à noite.
""",
"verbosPrepPtExercises": """
Gosto ___ chocolate. | de | o / em | J'aime le chocolat. | Gostar de.
Penso muito ___ ti. | em | a / de | Je pense beaucoup à toi. | Pensar em.
Ela sonhou ___ o avô. | com | de / em | Elle a rêvé de son grand-père. | Sonhar com.
Preciso ___ ajuda. | de | a / em | J'ai besoin d'aide. | Precisar de.
Isso depende ___ tempo. | do | de o / ao | Ça dépend du temps. | Depender de + o = do.
Chegámos ___ Lisboa às dez. | a | em / para | Nous sommes arrivés à Lisbonne à dix heures. | Chegar a (au Portugal).
Lembras-te ___ mim? | de | em / a | Tu te souviens de moi ? | Lembrar-se de.
Ela casou ___ um médico. | com | a / de | Elle a épousé un médecin. | Casar com.
Esquecemo-nos ___ chaves. | das | as / de as | Nous avons oublié les clés. | Esquecer-se de + as = das.
Confio ___ ti. | em | a / de | J'ai confiance en toi. | Confiar em.
Ele parece-se ___ pai. | com o | ao / do | Il ressemble à son père. | Parecer-se com.
Ajudei-a ___ fazer as malas. | a | de / para | Je l'ai aidée à faire les valises. | Ajudar alguém a + infinitif.
Desisti ___ curso. | do | o / ao | J'ai abandonné le cours. | Desistir de.
Ela riu-se ___ piada. | da | à / com a | Elle a ri de la blague. | Rir-se de.
Interessa-se ___ arte. | por | em / de | Il s'intéresse à l'art. | Interessar-se por.
""",
# ------------------------------------------------------------------ Connecteurs
"porqueEmboraPtExercises": """
Fiquei em casa ___ estava doente. | porque | embora / mas | Je suis resté à la maison parce que j'étais malade. | La cause : porque + indicatif.
___ estivesse doente, fui trabalhar. | Embora | Porque / Como | Bien que je sois malade, je suis allé travailler. | L'opposition : embora + conjuntivo.
___ estava a chover, ficámos em casa. | Como | Embora / Mas | Comme il pleuvait, nous sommes restés à la maison. | Como en tête : la cause.
Não fui à festa ___ estava cansado. | pois | embora / mas | Je ne suis pas allé à la fête, car j'étais fatigué. | Car : pois.
Gosto de café, ___ prefiro chá. | mas | porque / embora | J'aime le café, mais je préfère le thé. | Mais : mas.
___ do frio, fomos à praia. | Apesar | Embora / Porque | Malgré le froid, nous sommes allés à la plage. | Apesar de + nom.
Saímos ___ chovesse. | embora | porque / apesar | Nous sommes sortis bien qu'il pleuve. | Embora + conjuntivo.
Cancelaram o jogo ___ da chuva. | por causa | porque / embora | Ils ont annulé le match à cause de la pluie. | À cause de : por causa de.
Estudou muito; ___, chumbou. | no entanto | porque / como | Il a beaucoup étudié ; pourtant, il a échoué. | Pourtant : no entanto.
Está calor, ___ vamos à praia. | por isso | embora / porque | Il fait chaud, alors nous allons à la plage. | La conséquence : por isso.
Não comprei o casaco ___ era caro demais. | porque | embora / por causa | Je n'ai pas acheté le manteau parce qu'il était trop cher. | Porque + phrase.
___ tenha pouco dinheiro, viaja muito. | Embora | Porque / Como | Bien qu'il ait peu d'argent, il voyage beaucoup. | Embora + conjuntivo (tenha).
""",
"quandoEnquantoPtExercises": """
___ cheguei, já tinham jantado. | Quando | Enquanto / Até que | Quand je suis arrivé, ils avaient déjà dîné. | Quand, au passé : quando + indicatif.
___ eu cozinho, ele põe a mesa. | Enquanto | Desde / Até que | Pendant que je cuisine, il met la table. | Pendant que : enquanto.
Telefono-te ___ chegar. | assim que | enquanto / até que | Je t'appelle dès que j'arrive. | Dès que : assim que + futuro do conjuntivo.
Espera aqui ___ eu voltar. | até | enquanto / desde | Attends ici jusqu'à ce que je revienne. | Até + infinitif personnel (ou até que + conjuntivo).
___ que moro em Lisboa, ando de elétrico. | Desde | Até / Assim | Depuis que j'habite à Lisbonne, je prends le tram. | Depuis que : desde que + indicatif.
Lava as mãos ___ de comer, não depois! | antes | depois / enquanto | Lave-toi les mains avant de manger, pas après ! | Avant de : antes de + infinitif.
Primeiro jantámos; ___, vimos um filme. | depois | antes / quando | D'abord nous avons dîné ; ensuite, nous avons regardé un film. | Ensuite : depois.
___ era criança, morava no campo. | Quando | Enquanto / Desde | Quand j'étais enfant, j'habitais à la campagne. | Quando + imperfeito.
Sempre que ___ ao Porto, como uma francesinha. | vou | vá / ir | Chaque fois que je vais à Porto, je mange une francesinha. | Une habitude : sempre que + indicatif.
Logo que ___ notícias, aviso-te. | tiver | tenho / tenha | Dès que j'aurai des nouvelles, je te préviendrai. | Logo que + futur : tiver.
Fiquei acordado ___ ele chegar. | até | enquanto / desde | Je suis resté éveillé jusqu'à ce qu'il arrive. | Jusqu'à ce que : até + infinitif personnel.
""",
"seCasoPtExercises": """
___ chover, ficamos em casa. | Se | Caso / Quando que | S'il pleut, nous restons à la maison. | Se + futuro do conjuntivo.
___ chova, levo o guarda-chuva. | Caso | Se / Quando | Au cas où il pleuvrait, je prends le parapluie. | Caso + conjuntivo présent.
Vou, ___ que me paguem. | desde | caso / se | J'y vais, à condition qu'on me paie. | Desde que + conjuntivo : à condition que.
Vou a pé, a não ser que ___. | chova | chove / chover | J'y vais à pied, à moins qu'il pleuve. | A não ser que + conjuntivo.
Se eu ___ rico, comprava um barco. | fosse | for / sou | Si j'étais riche, j'achèterais un bateau. | Hypothèse irréelle : se + imperfeito do conjuntivo.
Se ___ tempo amanhã, vamos à praia. | tivermos | temos / tivéssemos | Si nous avons le temps demain, nous irons à la plage. | Se + futur : tivermos.
Não sei ___ ele vem. | se | caso / que se | Je ne sais pas s'il vient. | Question indirecte : se (si).
Levo o casaco, ___ fazer frio. | não vá | caso / se calhar | Je prends le manteau, des fois qu'il fasse froid. | Não vá + infinitif : au cas où (familier).
Ligue-me ___ precise de alguma coisa. | caso | se / quando | Appelez-moi au cas où vous auriez besoin de quelque chose. | Caso + conjuntivo.
Se ___ sabido, tinha vindo. | tivesse | tiver / tinha | Si j'avais su, je serais venu. | Irréel du passé : se tivesse + participe.
""",
# ------------------------------------------------------------------ Ordre des mots
"ordemAdjetivoPtExercises": """
Comprei um carro ___. | novo | nova / novos | J'ai acheté une voiture neuve. | L'adjectif suit le nom, accordé.
Ela tem uns olhos ___. | verdes | verde / verdas | Elle a les yeux verts. | Les couleurs suivent le nom.
O Rui é um ___ amigo. | bom | bem / boa | Rui est un bon ami. | Bom se place souvent avant le nom.
Lisboa é uma cidade ___. | bonita | bonito / bonitas | Lisbonne est une jolie ville. | Après le nom, accordé.
Foi um ___ homem. | grande | grando / grandes | Ce fut un grand homme. | Avant le nom, grande = grand (important).
Ele é um homem ___: mede dois metros. | grande | grand / grandes | C'est un homme grand : il mesure deux mètres. | Après le nom, grande = de grande taille.
É um ___ amigo da família: conhecemo-lo há trinta anos. | velho | velha / velhos | C'est un vieil ami de la famille : nous le connaissons depuis trente ans. | Avant le nom, velho = de longue date.
Vivem numa casa ___ e escura. | pequena | pequeno / pequenas | Ils vivent dans une maison petite et sombre. | Deux adjectifs après le nom, accordés.
Gosto de vinho ___. | tinto | tinta / tintos | J'aime le vin rouge. | Le vin rouge : vinho tinto (pas vermelho).
Pobre ___! Perdeu tudo. | homem | homem pobre / do homem | Pauvre homme ! Il a tout perdu. | Avant le nom, pobre = malheureux.
É a ___ vez que te digo. | última | ultima / último | C'est la dernière fois que je te le dis. | Les ordinaux précèdent le nom.
Tenho uma ___ notícia para ti. | boa | bom / bem | J'ai une bonne nouvelle pour toi. | Boa, accordé, avant le nom.
""",
"negacaoPtExercises": """
Não vi ___. | ninguém | alguém / nenhum | Je n'ai vu personne. | Não… ninguém : la double négation est obligatoire.
Não comprei ___. | nada | algo / tudo | Je n'ai rien acheté. | Não… nada.
___ vou a Paris. | Nunca | Não nunca / Jamais não | Je ne vais jamais à Paris. | Nunca en tête : pas de não.
Não vou ___. | nunca | jamais não / sempre | Je n'y vais jamais. | Après le verbe : não… nunca.
Não tenho ___ dúvida. | nenhuma | nenhum / alguma não | Je n'ai aucun doute. | Nenhum s'accorde : nenhuma dúvida.
Ele não bebe café ___ chá. | nem | e / ou | Il ne boit ni café ni thé. | Ni : nem.
___ ninguém sabe. | Ainda | Não ainda / Já não não | Personne ne sait encore. | Ninguém en tête suffit.
Já não ___ lá. | moro | não moro / morei não | Je n'y habite plus. | Já não + verbe : ne… plus.
Não ___ disse nada. | me | -me / mim | Il ne m'a rien dit. | Après não, le pronom devant.
Não quero ___ nada. | mais | menos / nunca | Je ne veux plus rien. | Não… mais nada : plus rien.
Ninguém ___ ajudou. | me | -me / mim | Personne ne m'a aidé. | Après ninguém, le pronom devant.
Não conheço ___ deles. | nenhum | nada / ninguém | Je n'en connais aucun. | Nenhum deles : aucun d'eux.
""",
"perguntasOrdemPtExercises": """
Onde ___ moras? | é que | que é / és que | Où est-ce que tu habites ? | À l'oral : interrogatif + é que.
O que ___ fazes? | é que | que é / és que | Qu'est-ce que tu fais ? | O que é que…
Porque é que não ___? | vieste | vieste-te / tu vieste | Pourquoi n'es-tu pas venu ? | Après porque é que : sujet-verbe.
Como ___ chamas? | te | -te / tu | Comment t'appelles-tu ? | Après como, le pronom devant.
Quanto ___ este casaco? | custa | custa-se / custas | Combien coûte ce manteau ? | Quanto + verbe.
Fazes anos amanhã, ___? | não fazes | não é verdade / pois | Ton anniversaire, c'est demain, n'est-ce pas ? | La question-écho portugaise : on reprend le verbe.
Gostaste do filme? — ___. | Gostei | Gostas / Gostei-me | Tu as aimé le film ? — Oui. | Au Portugal, on répond souvent en reprenant le verbe.
Já jantaste? — ___. | Já | Sim já / Jantaste | Tu as déjà dîné ? — Oui. | Já : oui (c'est fait).
De onde ___? | és | é que és / estás | D'où es-tu ? | Ser de : l'origine.
Com quem ___ ontem? | falaste | falaste-te / tu falou | Avec qui as-tu parlé hier ? | La préposition passe devant l'interrogatif.
A que horas ___ o filme? | começa | começa-se / começas | À quelle heure commence le film ? | Le sujet suit souvent le verbe.
Qual ___ o teu número? | é | está / e | Quel est ton numéro ? | Qual é…?
""",
# ------------------------------------------------------------------ Adverbes
"adverbiosMentePtExercises": """
Ele fala ___. (lento) | lentamente | lentomente / lenta | Il parle lentement. | -mente sur le féminin : lenta → lentamente.
___, chegámos a tempo. (feliz) | Felizmente | Felizamente / Feliz | Heureusement, nous sommes arrivés à temps. | Adjectif sans féminin : feliz → felizmente.
Ela canta muito ___. (bom) | bem | bom / boamente | Elle chante très bien. | Bom → bem.
Dormi ___ esta noite. (mau) | mal | mau / maumente | J'ai mal dormi cette nuit. | Mau → mal.
Respondeu ___. (rápido) | rapidamente | rapidomente / rápidamente | Il a répondu rapidement. | Rápida → rapidamente (l'accent tombe).
É ___ impossível. (total) | totalmente | totalamente / total | C'est totalement impossible. | Total → totalmente.
___ não vou. (provável) | Provavelmente | Provavélmente / Provável | Je n'irai probablement pas. | Provável → provavelmente (sans accent).
Ela vive ___ sozinha. (complet) | completamente | completomente / completa | Elle vit complètement seule. | Completa → completamente.
Conduz ___! (cuidadoso) | cuidadosamente | cuidadosomente / cuidadosa | Conduis prudemment ! | Cuidadosa → cuidadosamente.
""",
"adverbiosFamiliaPtExercises": """
Vou ao ginásio ___ semana. | toda a | todo a / toda | Je vais à la salle de sport toute la semaine. | La fréquence : toda a semana.
___ vou à praia ao domingo. | Às vezes | Vezes / As vezes | Parfois, je vais à la plage le dimanche. | Parfois : às vezes (avec accent).
Ele chega ___ atrasado. | sempre | nunca não / jamais | Il arrive toujours en retard. | Toujours : sempre.
Moro ___, ao pé da escola. | aqui | ali longe / lá longe | J'habite ici, près de l'école. | Ici : aqui (près de moi).
O café fica ___, do outro lado da rua. | ali | aqui / cá | Le café est là-bas, de l'autre côté de la rue. | Là : ali.
Vem ___! | cá | lá / aí | Viens ici ! | Avec un verbe de mouvement : cá.
Comi ___. | demais | demasiado de / muito de | J'ai trop mangé. | Trop : demais (après le verbe).
Ele é ___ simpático. | bastante | bastante de / bastantes | Il est assez sympathique. | Assez : bastante.
___ chove em agosto. | Raramente | Raro / Raramento | Il pleut rarement en août. | Rarement : raramente.
Fala ___ alto! | tão | tanto / muito tão | Il parle si fort ! | Si (intensité) : tão + adjectif ou adverbe.
Estou ___ cansado. | muito | muito de / bem de | Je suis très fatigué. | Très : muito.
___, faz o que quiseres. | Enfim | Fim / Afim | Bref, fais ce que tu veux. | Enfim : bref, enfin.
""",
# ------------------------------------------------------------------ Faux amis
"falsosAmigosTuilePtExercises": """
Hoje vou ___ às sete. (me réveiller) | acordar | despertar-me / acordar-me | Aujourd'hui, je vais me réveiller à sept heures. | Acordar = se réveiller (pas « accorder »).
Comprei ___ para o almoço. (du jambon cru) | presunto | jambão / fiambre | J'ai acheté du jambon cru pour le déjeuner. | O presunto = le jambon cru (le jambon cuit : o fiambre).
O ___ é um animal com oito braços. (la pieuvre) | polvo | pó / poulpo | La pieuvre est un animal à huit bras. | O polvo = la pieuvre (pas la poudre : o pó).
Esse rapaz é muito ___. (agaçant) | chato | gato / chateado | Ce garçon est très agaçant. | Chato = pénible, agaçant (le chat : o gato).
Estou ___ com este barulho. (agacé) | aborrecido | aborrecível / aborrecer | Je suis agacé par ce bruit. | Aborrecido = ennuyé, agacé (pas « abhorré »).
Ela está ___: vai ter um bebé. | grávida | gravada / grave | Elle est enceinte : elle va avoir un bébé. | Grávida = enceinte.
Deixei a ___ no carro. (le cartable) | pasta | massa / pastinha | J'ai laissé le cartable dans la voiture. | A pasta = le cartable, le dossier (les pâtes : a massa).
Vou ___ o telefone. (répondre au) | atender | atentar / esperar | Je vais répondre au téléphone. | Atender = répondre, recevoir (attendre : esperar).
Ontem ___ um jogo de futebol na televisão. (j'ai regardé) | assisti a | assisti / atendi | Hier, j'ai regardé un match de foot à la télévision. | Assistir a = regarder, être spectateur de.
Ponho ___ na sopa. (du persil) | salsa | sauce / molho | Je mets du persil dans la soupe. | A salsa = le persil (la sauce : o molho).
Este ___ é muito bonito. (cet endroit) | sítio | site / sitio | Cet endroit est très beau. | O sítio = l'endroit, le lieu.
Comi um ___ de chocolate. (un gâteau) | bolo | bol / bolinho | J'ai mangé un gâteau au chocolat. | O bolo = le gâteau (le bol : a tigela).
Bebi um ___ de água. (un verre) | copo | copa / taça | J'ai bu un verre d'eau. | O copo = le verre.
A ___ de hoje é arroz-doce. (le dessert) | sobremesa | sobre-mesa / desserto | Le dessert d'aujourd'hui, c'est le riz au lait. | A sobremesa = le dessert.
Ele vestiu um ___ azul para o casamento. (un costume) | fato | facto / costume | Il a mis un costume bleu pour le mariage. | O fato = le costume (o costume = l'habitude).
É ___ dele acordar cedo. (son habitude) | costume | fato / hábito de | Il a l'habitude de se lever tôt. | O costume = l'habitude.
O ___ é muito simpático. (le garçon) | rapaz | rapace / rapariga | Le garçon est très sympathique. | O rapaz = le garçon.
Recebi uma ___ da minha avó. (une lettre) | carta | cartão / letra | J'ai reçu une lettre de ma grand-mère. | A carta = la lettre (et a carta de condução = le permis).
A ___ desta música é bonita. (les paroles) | letra | carta / palavra | Les paroles de cette chanson sont belles. | A letra = l'écriture, les paroles.
Ficámos ___ com a notícia. (contents) | contentes | contidos / contados | Nous avons été contents de la nouvelle. | Contente = content (pas « contenu »).
Ela tirou uma ___ excelente. (une note) | nota | notícia / ponto | Elle a eu une excellente note. | A nota = la note (scolaire, ou le billet de banque).
Ponha o lixo no ___. (la poubelle) | caixote do lixo | lixeira / poubela | Mettez les déchets dans la poubelle. | Au Portugal : o caixote do lixo.
Esta peça de teatro tem uma ___ muito bonita. (une scène) | cena | ceia / jantar | Cette pièce a une très belle scène. | A cena = la scène (le dîner : o jantar ; a ceia = le souper).
Que ___! Perdi o comboio. (Quel ennui) | chatice | chato / chateza | Quelle barbe ! J'ai raté le train. | A chatice = la barbe, l'embêtement.
""",
}
