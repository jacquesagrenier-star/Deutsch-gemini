# -*- coding: utf-8 -*-
"""Les series A2 allongees (30 oct. 2026), comme anglais/outils/series_a2.py :
des questions ajoutees a la suite de celles de chaque fiche (grammaire_a2.py),
sans toucher a celles-ci. SOURCE : on corrige ici.
Format : question | bonne | fausse / fausse | traduction | explication.
Les fiches de temps (imperfeito, perfeito-imperfeito) sont allongees par
series_temps.py, a partir des phrases des cartes. BROUILLON : a faire relire.
"""

SUPPLEMENTS = {
"comparativosPtExercises": """
O metro é ___ rápido do que o autocarro. | mais | tão / muito | Le métro est plus rapide que le bus. | Plus … que : mais … do que.
A Rita é ___ simpática como a irmã. | tão | tanto / mais que | Rita est aussi sympathique que sa sœur. | Aussi … que : tão … como.
Hoje está ___ frio do que ontem. | menos | menor / pouco | Aujourd'hui, il fait moins froid qu'hier. | Moins … que : menos … do que.
Este é o ___ restaurante do bairro. | melhor | mais bom / bom mais | C'est le meilleur restaurant du quartier. | Le superlatif de bom : o melhor.
A Serra da Estrela é a montanha mais alta ___ Portugal continental. | de | do / que | La Serra da Estrela est la plus haute montagne du Portugal continental. | Superlatif + de (Portugal ne prend pas d'article).
O teu quarto é ___ do que o meu. | maior | mais grande / mais maior | Ta chambre est plus grande que la mienne. | Grande → maior.
A sopa de ontem estava ___ do que esta. | pior | mais má / mais pior | La soupe d'hier était pire que celle-ci. | Mau / má → pior.
Tenho ___ livros como tu. | tantos | tanto / tão | J'ai autant de livres que toi. | Autant de + nom masculin pluriel : tantos.
O bolo ficou ___! | ótimo | muito ótimo / mais ótimo | Le gâteau est excellent ! | Ótimo est déjà un superlatif.
A casa da avó é ___ do que a nossa. | mais pequena | mais pequeno / menos pequena | La maison de grand-mère est plus petite que la nôtre. | Au Portugal : mais pequeno, accordé (a casa → pequena).
Ela canta ___ do que eu. | melhor | mais bem / mais boa | Elle chante mieux que moi. | L'adverbe bem → melhor.
Este exame foi ___. | facílimo | muito facílimo / mais fácil | Cet examen a été extrêmement facile. | -íssimo : fácil → facílimo.
O Douro é o rio ___ bonito do país. | mais | muito / melhor | Le Douro est le plus beau fleuve du pays. | Le superlatif : o … mais + adjectif.
""",
"pronomesComplementoPtExercises": """
Conheces o Pedro? — Conheço-___ desde a escola. | o | lhe / lo | Tu connais Pedro ? — Je le connais depuis l'école. | Complément direct masculin : o.
As cartas? Ainda não ___ li. | as | las / lhes | Les lettres ? Je ne les ai pas encore lues. | Après não : as, devant le verbe.
Escrevi-___ uma mensagem ontem. | lhe | o / a | Je lui ai écrit un message hier. | Escrever a alguém : lhe.
Vou visitá-___ no domingo. | la | a / lhe | Je vais lui rendre visite dimanche. | Visitar alguém : direct ; après -r, a devient la.
Os bolos? Comemo-___ todos. | los | os / nos | Les gâteaux ? Nous les avons tous mangés. | Après -mos : le s tombe, os devient los.
A porta? Fecharam-___ às dez. | na | a / la | La porte ? Ils l'ont fermée à dix heures. | Après -m : a devient na.
Também ___ telefonaste? | lhe | o / a | Tu lui as téléphoné aussi ? | Après também : le pronom devant.
Quero agradecer-___ a ajuda. | lhe | o / a | Je veux vous remercier pour votre aide. | Agradecer algo a alguém : lhe.
Esta música? Adoro-___! | a | la / lhe | Cette chanson ? Je l'adore ! | Après une voyelle : a.
Quem ___ ajudou com as malas? | te | -te / ti | Qui t'a aidé avec les valises ? | Après quem : devant.
Ele faz-___ sempre rir. | nos | -nos-nos / nós | Il nous fait toujours rire. | Nos, après le verbe.
""",
"imperativoPtExercises": """
___ a luz, por favor. | Apaga | Apagas / Apague-te | Éteins la lumière, s'il te plaît. | Tu, affirmatif : apaga.
Não ___ a luz! | apagues | apagas / apaga | N'éteins pas la lumière ! | Tu, négatif : não apagues (g → gu).
(a senhora) ___ aqui, por favor. | Espere | Espera / Esperes | Attendez ici, s'il vous plaît. | La senhora : espere.
(vocês) ___ os livros na página dez. | Abram | Abrem / Abri | Ouvrez vos livres à la page dix. | Vocês : abram.
___ o que quiseres. | Faz | Fazes / Faça-te | Fais ce que tu veux. | Fazer, tu : faz.
Não ___ medo! | tenhas | tens / tem | N'aie pas peur ! | Négatif : não tenhas.
(o senhor) Não se ___! | preocupe | preocupa / preocupes | Ne vous inquiétez pas ! | O senhor, négatif : não se preocupe.
___-te à vontade! | Põe | Pões / Ponha | Mets-toi à l'aise ! | Pôr-se à vontade, tu : põe-te.
(vocês) ___ cuidado com o degrau. | Tenham | Têm / Tende | Faites attention à la marche. | Vocês : tenham.
___ embora, já é tarde! | Vai-te | Vais-te / Vá-te | Va-t'en, il est déjà tard ! | Ir-se embora, tu : vai-te.
""",
"obrigacaoPtExercises": """
Tens ___ estudar mais. | de | que de / a | Tu dois étudier davantage. | Au Portugal : ter de.
Não é ___ reservar: há sempre lugar. | preciso | precisa / preciso de | Ce n'est pas la peine de réserver : il y a toujours de la place. | Não é preciso + infinitif.
Eles ___ chegar a qualquer momento. | devem | têm / precisam | Ils doivent arriver d'un moment à l'autre. | La probabilité : dever.
Preciso ___ falar contigo. | de | que / a | J'ai besoin de te parler. | Precisar de + infinitif.
É ___ estacionar em cima do passeio. | proibido | proibida / proibir | Il est interdit de se garer sur le trottoir. | É proibido + infinitif.
___ comer mais fruta, sabes? | Devias | Tinhas / Precisavas | Tu devrais manger plus de fruits, tu sais ? | Un conseil doux : devias.
Tivemos ___ esperar uma hora. | de | que de / para | Nous avons dû attendre une heure. | Ter de, au passé : tivemos de.
Aqui não se ___ tirar fotografias. | pode | deve-se / tem | Ici, on ne peut pas prendre de photos. | Não se pode.
Não ___ de vir amanhã, está tudo pronto. | precisas | precises / precisa-te | Tu n'as pas besoin de venir demain, tout est prêt. | Não precisar de : pas besoin.
O comboio ___ estar a chegar. | deve | tem de / precisa | Le train doit être sur le point d'arriver. | Dever + estar a : probablement.
""",
"porParaPtExercises": """
O avião ___ Londres parte às seis. | para | por / pela | L'avion pour Londres part à six heures. | La destination : para.
Passámos ___ Ponte Vasco da Gama. | pela | para a / por a | Nous sommes passés par le pont Vasco da Gama. | Por + a = pela.
Obrigada ___ flores! | pelas | para as / por as | Merci pour les fleurs ! | Obrigado/a por + as = pelas.
Fiz a sopa ___ ti. | para | por / pela | J'ai fait la soupe pour toi. | Le destinataire : para.
O trabalho tem de estar pronto ___ amanhã. | para | por / pelo | Le travail doit être prêt pour demain. | L'échéance : para.
Paguei dez euros ___ este livro. | por | para / pelo | J'ai payé dix euros pour ce livre. | Le prix : por.
Vou ___ casa, estou cansado. | para | por / pela | Je rentre à la maison, je suis fatigué. | La direction : para.
Falámos ___ telefone durante uma hora. | ao | pelo / para o | Nous avons parlé au téléphone pendant une heure. | Au Portugal : falar ao telefone.
O museu foi desenhado ___ um arquiteto famoso. | por | para / pelo | Le musée a été dessiné par un architecte célèbre. | L'agent du passif : por.
Saímos cedo ___ evitar o trânsito. | para | por / pelo | Nous sommes partis tôt pour éviter la circulation. | Le but : para + infinitif.
Ele foi preso ___ roubo. | por | para / pelo de | Il a été arrêté pour vol. | La cause : por.
""",
"jaAindaPtExercises": """
___ chegaste? Que rápido! | Já | Ainda / Ainda não | Tu es déjà arrivé ? Quelle rapidité ! | Déjà : já.
O museu ___ não abriu, espera um pouco. | ainda | já / mais | Le musée n'a pas encore ouvert, attends un peu. | Pas encore : ainda não.
Ele ___ não mora em Lisboa, mudou-se para Faro. | já | ainda / mais | Il n'habite plus à Lisbonne, il a déménagé à Faro. | Ne… plus : já não.
Ainda estás a trabalhar? — ___, já acabei. | Não | Já / Ainda | Tu travailles encore ? — Non, j'ai déjà fini. | La réponse négative : não, já acabei.
Já ___ disse que não. | lhe | -lhe / lhe- | Je lui ai déjà dit non. | Après já : devant.
O bebé ___ dorme? — Ainda. | ainda | já não / já | Le bébé dort encore ? — Oui, encore. | Encore : ainda.
Ainda não ___ conhecia. | a | -a / la | Je ne la connaissais pas encore. | Après ainda não : devant.
___ não há bilhetes para o concerto. | Já | Ainda / Mais | Il n'y a plus de billets pour le concert. | Ne… plus : já não.
É ___ cedo para jantar. | ainda | já não / já | C'est encore tôt pour dîner. | Encore : ainda.
Já ___ às dez horas! | são | é / estão | Il est déjà dix heures ! | L'heure, au pluriel : são.
""",
"demonstrativosPtExercises": """
___ livro aqui é meu. | Este | Esse / Aquele | Ce livre-ci est à moi. | Près de moi : este.
Passa-me ___ chávena que tens aí. | essa | esta / aquela | Passe-moi cette tasse que tu as là. | Près de toi : essa.
___ montanhas ao longe são a Serra da Estrela. | Aquelas | Estas / Essas | Ces montagnes au loin sont la Serra da Estrela. | Loin des deux : aquelas.
O que é ___ que tens na mão? | isso | isto / esse | Qu'est-ce que c'est, ce que tu as dans la main ? | Près de toi, non nommé : isso.
Gosto ___ casa. | desta | de esta / nesta | J'aime cette maison. | De + esta = desta.
___ dia, choveu muito. | Nesse | Em esse / Desse | Ce jour-là, il a beaucoup plu. | Em + esse = nesse.
Lembras-te ___ professor de Matemática? | daquele | de aquele / naquele | Tu te souviens de ce professeur de maths ? | De + aquele = daquele.
Por ___ é que não vim. | isso | isto / esse | C'est pour ça que je ne suis pas venu. | Por isso : c'est pourquoi.
___ semana tenho muito trabalho. | Esta | Este / Isto | Cette semaine, j'ai beaucoup de travail. | Semana, féminin : esta.
Vamos ___ restaurante de que te falei. | àquele | a aquele / naquele | Allons dans ce restaurant dont je t'ai parlé. | A + aquele = àquele.
""",
"perifrasesA2PtExercises": """
Acabámos ___ jantar. | de | a / por | Nous venons de dîner. | Venir de : acabar de.
Ela voltou ___ ligar-me. | a | de / em | Elle m'a rappelé. | Re- : voltar a.
O meu pai deixou ___ beber café. | de | a / em | Mon père a arrêté de boire du café. | Arrêter de : deixar de.
Começou ___ nevar. | a | de / por | Il s'est mis à neiger. | Commencer à : começar a.
Continua ___ chover. | a | de / para | Il continue à pleuvoir. | Continuar a + infinitif.
Ando ___ pensar em mudar de casa. | a | de / em | Je pense en ce moment à déménager. | Andar a + infinitif.
Estava ___ sair quando telefonaste. | para | a / de | J'étais sur le point de sortir quand tu as téléphoné. | Estar para + infinitif.
O filme ___ de começar. | acabou | voltou / deixou | Le film vient de commencer. | Venir de : acabar de.
O Rui ___ a fumar depois das férias. | voltou | acabou / deixou | Rui s'est remis à fumer après les vacances. | Recommencer : voltar a.
Estou ___ ouvir-te, continua. | a | de / para | Je t'écoute, continue. | Estar a + infinitif.
""",
}
