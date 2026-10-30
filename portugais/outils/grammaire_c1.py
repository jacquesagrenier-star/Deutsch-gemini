# -*- coding: utf-8 -*-
"""Les fiches de grammaire C1 du portugais (du Portugal), en francais, et leurs
series. SOURCE : on corrige ici, puis python portugais/outils/construire.py.
Meme format que grammaire_a1.py. BROUILLON : a faire relire par un lusophone.
"""

FICHES = [
{
"id": "mesoclise", "titre": "La mésoclise : dir-se-ia, far-lhe-ei", "resume": "le pronom au milieu du verbe, à l'écrit soutenu",
"regle": "Au futur et au conditionnel, quand rien n'attire le pronom devant le verbe, il se place <b>à l'intérieur</b> du verbe, entre l'infinitif et la terminaison : <b>dar + te + ei → dar-te-ei</b>, <b>dizer + se + ia → dir-se-ia</b>. Les pronoms o, a deviennent lo, la et le r tombe : <b>fá-lo-ei</b>, <b>convidá-la-íamos</b>. C'est la norme écrite au Portugal (presse, courrier officiel, littérature). Après un déclencheur (não, que, já…), on revient à la próclise : <b>Não te darei</b>, <b>Acho que se diria</b>.",
"tableau": [
 ["dar-te-ei · dar-lhe-emos", "je te donnerai · nous lui donnerons", "Responder-lhe-ei amanhã."],
 ["far-se-á · dir-se-ia · trar-me-ão", "les radicaux courts (fazer, dizer, trazer)", "Dir-se-ia que vai nevar."],
 ["fá-lo-ei · convidá-la-íamos", "o, a → lo, la", "Fá-lo-ei com todo o gosto."],
 ["não te darei · que se diria", "après un déclencheur : devant", "Nunca o farei."],
 ["vou dar-te · vou fazê-lo", "l'équivalent oral", "Vou responder-lhe amanhã."],
 ["realizar-se-á · proceder-se-á", "la langue administrative", "A reunião realizar-se-á às 10h."],
],
"exemples": [
 ["A cerimónia realizar-se-á no salão nobre.", "La cérémonie aura lieu dans la salle d'honneur."],
 ["Ser-lhe-ia possível enviar-nos o documento?", "Vous serait-il possible de nous envoyer le document ?"],
 ["Se soubesse, dir-to-ia.", "Si je le savais, je te le dirais."],
],
"attention": "La mésoclise est bien vivante à l'écrit au Portugal, et pratiquement morte au Brésil. Dans la conversation, on l'évite naturellement avec <b>ir + infinitif</b> ou l'imperfeito (<b>dizia-te</b>).",
"serie": "mesoclisePtExercises", "kicker": "La mésoclise",
"questions": """
Amanhã ___ a resposta. | dar-te-ei | darei-te / te darei | Demain, je te donnerai la réponse. | Futur sans déclencheur : mésoclise.
___ que vai chover. | Dir-se-ia | Diria-se / Se diria | On dirait qu'il va pleuvoir. | Dizer → dir- ; dir-se-ia.
A reunião ___ às dez horas. | realizar-se-á | se realizará / realizará-se | La réunion aura lieu à dix heures. | Langue officielle : mésoclise.
O relatório? ___ até sexta-feira. | Fá-lo-ei | Farei-o / O farei | Le rapport ? Je le ferai d'ici vendredi. | Fazer : far- + o → fá-lo-ei.
Não ___ nada sem a tua autorização. | te direi | dir-te-ei / direi-te | Je ne te dirai rien sans ton autorisation. | Après não : próclise.
___ possível enviar-nos a fatura? | Ser-lhe-ia | Seria-lhe / Lhe seria | Vous serait-il possible de nous envoyer la facture ? | Ser + lhe + ia.
Se pudesse, ___ com prazer. | ajudá-lo-ia | ajudaria-o / o ajudaria | Si je pouvais, je l'aiderais avec plaisir. | -r tombe, o → lo : ajudá-lo-ia.
Acho que ___ melhor esperar. | se diria | dir-se-ia / diria-se | Je crois qu'on dirait qu'il vaut mieux attendre. | Après que : próclise.
Os convidados? ___ na entrada. | Recebê-los-emos | Receberemos-os / Os receberemos-emos | Les invités ? Nous les recevrons à l'entrée. | Receber + os → recebê-los-emos.
___ amanhã, sem falta. | Telefonar-lhe-ei | Telefonarei-lhe / Lhe telefonarei | Je vous téléphonerai demain, sans faute. | Telefonar + lhe + ei.
Nunca ___ isso. | o faria | fá-lo-ia / faria-o | Je ne ferais jamais ça. | Après nunca : próclise.
O documento ___ aos interessados. | entregar-se-á | se entregará-á / entregará-se | Le document sera remis aux intéressés. | Se passif + mésoclise.
"""
},
{
"id": "infinitivo-pessoal-c1", "titre": "L'infinitif personnel : les cas fins", "resume": "obligatoire, interdit ou au choix",
"regle": "L'infinitif personnel est <b>obligatoire</b> quand l'infinitif a un sujet exprimé différent de celui du verbe principal (<b>É altura de vocês decidirem</b>) ou pour lever une ambiguïté. Il est <b>exclu</b> après les verbes de perception et de causalité quand le sujet est un pronom complément (<b>Vi-os sair</b>, <b>Mandei-os entrar</b>), et avec les auxiliaires (<b>Podemos sair</b>, jamais « podemos sairmos »). Il est <b>libre</b> après une préposition quand le sujet est le même : <b>Saímos depois de jantar</b> ou <b>de jantarmos</b>. Le composé : <b>ter</b> à l'infinitif personnel + participe : <b>Obrigado por teres vindo</b>.",
"tableau": [
 ["sujet différent : obligatoire", "", "Esperei até eles chegarem."],
 ["auxiliaire (poder, dever, ir) : non", "", "Vamos sair. Devemos ir."],
 ["vi-os sair · mandei-os entrar", "perception, causalité + pronom : non", "Ouvi-os chegar."],
 ["vi os miúdos saírem", "avec un nom : possible", "Vi os vizinhos saírem."],
 ["même sujet après préposition : libre", "", "Depois de jantarmos / de jantar, saímos."],
 ["por teres feito · depois de termos chegado", "le composé", "Obrigado por teres vindo."],
],
"exemples": [
 ["Obrigado por terem vindo.", "Merci d'être venus."],
 ["É hora de os alunos entregarem os testes.", "C'est l'heure pour les élèves de rendre les contrôles."],
 ["Ouvimo-los cantar a noite toda.", "Nous les avons entendus chanter toute la nuit."],
],
"attention": "<b>Antes de o sol nascer</b> (avant que le soleil se lève) : à l'écrit soigné, la préposition ne se contracte pas avec l'article qui est le sujet de l'infinitif (<b>de o</b>, pas <b>do</b>). À l'oral, la contraction est courante.",
"serie": "infinitivoPessoalC1PtExercises", "kicker": "L'infinitif personnel (2)",
"questions": """
Obrigado por ___ vindo. | terem | tiverem / tinham | Merci d'être venus. | Le composé : ter à l'infinitif personnel + participe.
Esperámos até eles ___. | chegarem | chegarem-se / chegaram | Nous avons attendu qu'ils arrivent. | Sujet différent : infinitif personnel obligatoire.
Nós ___ sair mais cedo. | podemos | podermos / podemos-nos | Nous pouvons partir plus tôt. | Auxiliaire : pas d'infinitif personnel.
Vi-os ___ de casa. | sair | saírem / saíram | Je les ai vus sortir de la maison. | Perception + pronom complément : infinitif simple.
É altura de vocês ___. | decidirem | decidir-se / decidam | Il est temps que vous décidiez. | Sujet exprimé différent : -em.
Mandei-os ___ na sala. | entrar | entrarem / entraram | Je les ai fait entrer dans le salon. | Causalité + pronom : infinitif simple.
Depois de ___ chegado, fomos jantar. | termos | tivermos / temos | Après être arrivés, nous sommes allés dîner. | Composé : termos + participe.
Antes de ___ sol nascer, já estávamos na estrada. | o | do / ao | Avant que le soleil se lève, nous étions déjà sur la route. | Écrit soigné : de o (sujet de l'infinitif).
Apesar de ___ avisado, ninguém nos ouviu. | termos | tínhamos / tivéssemos | Bien que nous ayons prévenu, personne ne nous a écoutés. | Apesar de + infinitif personnel composé.
É natural os pais ___ preocupados. | estarem | estar-se / estão | Il est naturel que les parents soient inquiets. | Sujet exprimé : infinitif personnel.
Vamos ___ o jantar juntos. | fazer | fazermos / fazer-nos | Nous allons faire le dîner ensemble. | Ir + infinitif : pas de personne.
Fizeram-nos ___ duas horas. | esperar | esperarmos / esperámos | Ils nous ont fait attendre deux heures. | Causalité + pronom : infinitif simple.
"""
},
{
"id": "participios-duplos", "titre": "Aceite ou aceitado ? Les participes doubles", "resume": "ter + participe long, ser / estar + participe court",
"regle": "Certains verbes ont deux participes. Le <b>long</b>, régulier, va avec <b>ter</b> ; le <b>court</b> avec <b>ser</b> et <b>estar</b> : <b>Tinha acendido a luz</b> / <b>A luz estava acesa</b>. Mais plusieurs courts ont tout gagné et servent aussi avec ter : <b>ganho, gasto, pago</b>, et au Portugal <b>aceite</b> et <b>entregue</b> : <b>Tenho pago as contas</b>, <b>Já tinha entregue o trabalho</b>. Autres paires : <b>eleger</b> (elegido / eleito), <b>prender</b> (prendido / preso), <b>imprimir</b> (imprimido / impresso), <b>morrer</b> (morrido / morto), <b>limpar</b> (limpado / limpo), <b>salvar</b> (salvado / salvo).",
"tableau": [
 ["ter + acendido · estar + aceso", "allumer", "A vela está acesa."],
 ["ter + elegido · ser + eleito", "élire", "Foi eleito em 2021."],
 ["ter + prendido · ser + preso", "arrêter, attacher", "O ladrão foi preso."],
 ["ter / ser + pago, ganho, gasto", "court partout", "Já tinha pago."],
 ["ter / ser + aceite, entregue (Portugal)", "court partout", "A proposta foi aceite."],
 ["ter + morrido · estar + morto", "mourir", "Tinha morrido no ano anterior."],
],
"exemples": [
 ["O presidente foi eleito por maioria absoluta.", "Le président a été élu à la majorité absolue."],
 ["Quando cheguei, ela já tinha limpado a casa toda. A casa estava limpa.", "Quand je suis arrivé, elle avait déjà nettoyé toute la maison. La maison était propre."],
 ["A candidatura foi aceite.", "La candidature a été acceptée."],
],
"attention": "Au Brésil, on dit <b>aceito</b> (« foi aceito ») ; au Portugal, <b>aceite</b>. Et <b>entregado</b> survit à peine des deux côtés : <b>entregue</b> partout.",
"serie": "participiosDuplosPtExercises", "kicker": "Les participes doubles",
"questions": """
A luz ainda estava ___. | acesa | acendida / acendido | La lumière était encore allumée. | Estar + participe court : aceso, accordé.
Ela já tinha ___ a lareira. | acendido | acesa / aceso | Elle avait déjà allumé la cheminée. | Ter + participe long : acendido.
O novo presidente foi ___ ontem. | eleito | elegido / eleger | Le nouveau président a été élu hier. | Ser + participe court : eleito.
Os eleitores tinham ___ um novo parlamento. | elegido | eleito / elegeram | Les électeurs avaient élu un nouveau parlement. | Ter + participe long : elegido.
O suspeito foi ___ no aeroporto. | preso | prendido / prendeu | Le suspect a été arrêté à l'aéroport. | Ser + preso.
Já tinha ___ a conta quando chegaste. | pago | pagado / pagou | J'avais déjà payé l'addition quand tu es arrivé. | Pago sert aussi avec ter.
A proposta foi ___ por todos. | aceite | aceitado / aceito | La proposition a été acceptée par tous. | Au Portugal : aceite.
Tinha ___ o trabalho a tempo. | entregue | entregado / entregou | J'avais rendu le travail à temps. | Entregue, avec ter aussi.
O peixe estava ___. | morto | morrido / morrida | Le poisson était mort. | Estar + morto.
O avô tinha ___ no inverno. | morrido | morto / morreu | Le grand-père était mort en hiver. | Ter + morrido (le verbe intransitif).
A cozinha está ___. | limpa | limpada / limpado | La cuisine est propre. | Estar + participe court : limpo, limpa.
Gastámos mais do que tínhamos ___. | ganho | ganhado / ganhámos | Nous avons dépensé plus que nous n'avions gagné. | Ganho, avec ter aussi.
"""
},
{
"id": "realce", "titre": "Mettre en relief : é que, foi… que, o que… é", "resume": "c'est… que, ce que… c'est",
"regle": "Pour mettre un élément en valeur : <b>é que</b> après le mot (<b>Eu é que paguei</b> — c'est moi qui ai payé ; <b>Onde é que moras?</b>), <b>ser… que</b> qui encadre (<b>Foi a Ana que telefonou</b>, <b>Foi ontem que chegaram</b>), <b>o que… é</b> en tête (<b>O que eu quero é descansar</b>), <b>quem… é</b> (<b>Quem sabe é o Rui</b>). Le verbe <b>ser</b> s'accorde souvent en temps : <b>Foi em 1974 que…</b>, <b>É agora que…</b>. Dans les questions, <b>é que</b> est presque systématique au Portugal : <b>O que é que fazes?</b>",
"tableau": [
 ["X + é que", "c'est X qui / que", "Tu é que sabes."],
 ["ser + X + que", "c'est X que (temps accordé)", "Foi em Coimbra que nos conhecemos."],
 ["o que … é", "ce que …, c'est", "O que me preocupa é o preço."],
 ["quem … é", "celui qui …, c'est", "Quem decide és tu."],
 ["interrogatif + é que", "question de l'oral", "Quando é que chegas?"],
 ["é que … (en tête)", "c'est que (explication)", "É que estou com pressa."],
],
"exemples": [
 ["Foi em 1974 que a democracia chegou a Portugal.", "C'est en 1974 que la démocratie est arrivée au Portugal."],
 ["O que eu gostava mesmo era de viver junto ao mar.", "Ce que j'aimerais vraiment, c'est vivre près de la mer."],
 ["Desculpa, é que o trânsito estava horrível.", "Désolé, c'est que la circulation était horrible."],
],
"attention": "Avec <b>quem… é</b>, ser s'accorde avec ce qui suit : <b>Quem paga sou eu</b>, <b>Quem manda és tu</b>.",
"serie": "realcePtExercises", "kicker": "Mettre en relief",
"questions": """
Eu ___ paguei o jantar. | é que | foi que / que é | C'est moi qui ai payé le dîner. | Mise en relief : X + é que.
___ em Coimbra que nos conhecemos. | Foi | É / Era que | C'est à Coimbra que nous nous sommes rencontrés. | Ser au passé, accordé : foi… que.
O que me preocupa ___ o preço. | é | que é / foi que | Ce qui m'inquiète, c'est le prix. | O que… é.
Quem paga ___ eu. | sou | é / és | C'est moi qui paie. | Quem… ser s'accorde avec ce qui suit : sou eu.
Onde ___ moras? | é que | que é / és que | Où est-ce que tu habites ? | Question de l'oral : interrogatif + é que.
Desculpa o atraso, ___ o comboio avariou. | é que | foi que / porque é | Désolé pour le retard, c'est que le train est tombé en panne. | É que : l'explication.
Foi ontem ___ eles chegaram. | que | quando / é que | C'est hier qu'ils sont arrivés. | Ser… que.
O que eu queria ___ dormir uma semana. | era | é que / foi | Ce que je voudrais, c'est dormir une semaine. | Concordance : queria… era.
Quem manda aqui ___ tu. | és | é / sou | C'est toi qui commandes ici. | Quem… és tu.
O que é ___ vais fazer amanhã? | que | quê / o que | Qu'est-ce que tu vas faire demain ? | O que é que…
Não fui eu, foram eles ___ partiram o vidro. | que | quem é / é que | Ce n'est pas moi, ce sont eux qui ont cassé la vitre. | Ser accordé au pluriel : foram eles que.
É agora ___ temos de decidir. | que | é que / quando é | C'est maintenant que nous devons décider. | É… que.
"""
},
{
"id": "registo", "titre": "Le registre : formel ou courant", "resume": "adquirir ou comprar, efetuar ou fazer, o senhor doutor",
"regle": "Le portugais écrit et administratif a son vocabulaire : <b>adquirir</b> (comprar), <b>efetuar, proceder a</b> (fazer), <b>solicitar</b> (pedir), <b>residir</b> (morar), <b>deslocar-se</b> (ir), <b>informar</b> (dizer), <b>encontrar-se</b> (estar). La politesse portugaise est très codifiée : on s'adresse à quelqu'un par <b>o senhor / a senhora</b> + 3e personne, souvent avec le titre : <b>o senhor doutor</b>, <b>a senhora engenheira</b>. Dans une lettre : <b>Exmo. Senhor</b> (Excelentíssimo), <b>Com os melhores cumprimentos</b>. <b>Você</b>, au Portugal, est délicat : il peut paraître distant ou peu poli ; on l'évite en utilisant le prénom ou le titre.",
"tableau": [
 ["adquirir · comprar", "acquérir · acheter", "Pode adquirir o bilhete online."],
 ["efetuar · proceder a · fazer", "effectuer · procéder à · faire", "O pagamento deve ser efetuado até dia 5."],
 ["solicitar · pedir", "solliciter · demander", "Solicitamos a sua presença."],
 ["residir · morar", "résider · habiter", "Reside em Braga desde 2010."],
 ["o senhor doutor · a senhora engenheira", "monsieur / madame + titre", "O senhor doutor pode atender?"],
 ["Exmo. Senhor · Com os melhores cumprimentos", "Monsieur · Cordialement", ""],
],
"exemples": [
 ["Solicitamos que efetue o pagamento até ao final do mês.", "Nous vous prions d'effectuer le paiement d'ici la fin du mois."],
 ["A senhora doutora já pode atendê-lo.", "La docteure peut vous recevoir maintenant."],
 ["Informamos que os serviços se encontram encerrados ao sábado.", "Nous vous informons que les services sont fermés le samedi."],
],
"attention": "« Doutor » ne se limite pas aux médecins : au Portugal, toute personne diplômée d'université peut être appelée <b>senhor doutor</b> / <b>senhora doutora</b>, et un ingénieur <b>senhor engenheiro</b>. C'est de la politesse, pas de la flatterie.",
"serie": "registoPtExercises", "kicker": "Le registre",
"questions": """
(formel) Pode ___ o bilhete na bilheteira. | adquirir | comprar-se / pegar | Vous pouvez acquérir le billet au guichet. | Comprar, en langue soutenue : adquirir.
(formel) O pagamento deve ser ___ até dia 10. | efetuado | feito-se / pago-se | Le paiement doit être effectué d'ici le 10. | Fazer, en langue administrative : efetuar.
(formel) ___ a sua presença na reunião. | Solicitamos | Pedimos-lhe-se / Pegamos | Nous sollicitons votre présence à la réunion. | Pedir, soutenu : solicitar.
(formel) O requerente ___ em Lisboa. | reside | mora-se / vive-se | Le demandeur réside à Lisbonne. | Morar, soutenu : residir.
(formel) Os serviços ___ encerrados ao domingo. | encontram-se | estão-se / ficam-se | Les services sont fermés le dimanche. | Estar, soutenu : encontrar-se.
Bom dia, senhor ___, o seu doente já chegou. | doutor | médico-senhor / dom | Bonjour, docteur, votre patient est arrivé. | La politesse portugaise : senhor doutor.
(lettre) ___ Senhor Diretor, | Exmo. | Caro-se / Querido | Monsieur le Directeur, | En-tête formel : Exmo. (Excelentíssimo).
(lettre) Com os melhores ___, | cumprimentos | saudações-se / beijinhos | Cordialement, | Formule de fin : com os melhores cumprimentos.
O senhor ___ um café? | deseja | desejas / desejais | Monsieur désire un café ? | O senhor + 3e personne.
(formel) Para mais informações, ___ ao balcão. | dirija-se | vai-te / dirige-te | Pour plus d'informations, adressez-vous au guichet. | Ir, soutenu : dirigir-se (impératif formel).
(formel) Vimos por este meio ___ que o prazo terminou. | informar | dizer-se / falar | Nous vous informons par la présente que le délai est écoulé. | Vimos por este meio informar : formule de lettre.
(formel) Deverá ___ à secretaria com o documento. | deslocar-se | ir-se / andar | Vous devrez vous rendre au secrétariat avec le document. | Ir, soutenu : deslocar-se.
"""
},
{
"id": "conjuncoes-c1", "titre": "Conquanto, contanto que, porquanto, a fim de que", "resume": "les conjonctions de la langue soutenue",
"regle": "La langue soignée connaît des conjonctions plus rares : <b>conquanto</b> (bien que, + conjuntivo), <b>contanto que</b> (pourvu que, + conjuntivo), <b>porquanto</b> (puisque, + indicatif), <b>uma vez que</b> (puisque, + indicatif ; ou dès lors que), <b>visto que</b>, <b>dado que</b> (étant donné que, + indicatif), <b>a fim de que</b> (afin que, + conjuntivo), <b>à medida que</b> (à mesure que), <b>na medida em que</b> (dans la mesure où), <b>de modo a</b> / <b>de forma a</b> + infinitif (de façon à).",
"tableau": [
 ["conquanto + conjuntivo", "bien que (soutenu)", "Conquanto seja difícil, é possível."],
 ["contanto que + conjuntivo", "pourvu que", "Aceito, contanto que me paguem."],
 ["porquanto · visto que · dado que + indicatif", "puisque, étant donné que", "Dado que ninguém veio, fechámos."],
 ["a fim de que + conjuntivo · a fim de + infinitif", "afin que · afin de", "Escrevo a fim de esclarecer."],
 ["à medida que", "à mesure que", "À medida que o tempo passa…"],
 ["na medida em que", "dans la mesure où", "Na medida em que for possível…"],
],
"exemples": [
 ["Visto que o prazo terminou, a candidatura não foi aceite.", "Étant donné que le délai était écoulé, la candidature n'a pas été acceptée."],
 ["À medida que subíamos, o ar ficava mais frio.", "À mesure que nous montions, l'air devenait plus froid."],
 ["Organizámos tudo de modo a evitar atrasos.", "Nous avons tout organisé de façon à éviter les retards."],
],
"attention": "<b>Uma vez que</b> + indicatif = puisque (<b>Uma vez que estás aqui, ajuda</b>) ; + conjuntivo = dès lors que, une fois que (<b>Uma vez que acabes, podes sair</b>).",
"serie": "conjuncoesC1PtExercises", "kicker": "Les conjonctions soutenues",
"questions": """
Conquanto ___ difícil, o projeto é possível. | seja | é / for | Bien qu'il soit difficile, le projet est possible. | Conquanto + conjuntivo.
Aceito o trabalho, contanto que me ___ a horas. | paguem | pagam / pagarem | J'accepte le travail, pourvu qu'on me paie à temps. | Contanto que + conjuntivo.
Dado que ninguém ___, cancelámos a reunião. | apareceu | aparecesse / apareça | Étant donné que personne n'est venu, nous avons annulé la réunion. | Dado que + indicatif.
À medida que ___, o ar ficava mais frio. | subíamos | subíssemos / subirmos | À mesure que nous montions, l'air devenait plus froid. | À medida que + indicatif.
Escrevo-lhe a fim de ___ a situação. | esclarecer | esclareça / esclarecendo | Je vous écris afin de clarifier la situation. | A fim de + infinitif.
Explico outra vez, a fim de que todos ___. | percebam | percebem / perceberem | J'explique encore une fois, afin que tous comprennent. | A fim de que + conjuntivo.
Visto que ___ cansado, fica em casa. | estás | estejas / estiveres | Puisque tu es fatigué, reste à la maison. | Visto que + indicatif.
Organizámos tudo de modo a ___ atrasos. | evitar | evitarmos-nos / evitemos | Nous avons tout organisé de façon à éviter les retards. | De modo a + infinitif.
Uma vez que ___ aqui, ajuda-me. | estás | estejas / estiveres | Puisque tu es là, aide-moi. | Uma vez que (puisque) + indicatif.
Na medida em que ___ possível, ajudaremos. | for | é / seja-se | Dans la mesure où ce sera possible, nous aiderons. | Na medida em que + futur : futuro do conjuntivo.
Não pôde vir, porquanto ___ doente. | estava | estivesse / esteja | Il n'a pas pu venir, puisqu'il était malade. | Porquanto + indicatif.
Ficámos calados, de forma a não ___ o bebé. | acordar | acordarmos-o / acorde | Nous sommes restés silencieux, de façon à ne pas réveiller le bébé. | De forma a + infinitif.
"""
},
{
"id": "mais-que-perfeito-simples", "titre": "Fizera, dissera : le plus-que-parfait littéraire", "resume": "le temps des romans et des journaux",
"regle": "À côté de <b>tinha feito</b>, le portugais a un plus-que-parfait en un mot : <b>fizera</b>, <b>dissera</b>, <b>falara</b>, <b>chegara</b>. On le forme sur le perfeito, 3e personne du pluriel, en remplaçant <b>-ram</b> par <b>-ra</b> : <b>fizeram → fizera</b>, <b>falaram → falara</b>. Il vit dans la littérature (Eça, Saramago), la presse et quelques expressions figées : <b>Quem me dera!</b> (si seulement !), <b>Pudera!</b> (évidemment !), <b>Tomara que…</b> (pourvu que…).",
"tableau": [
 ["falar (falaram) → falara, falaras, falara, faláramos, falaram", "", "Nunca falara com ele."],
 ["fazer (fizeram) → fizera · dizer → dissera", "", "Dissera que voltaria."],
 ["ser / ir (foram) → fora", "", "Fora um dia longo."],
 ["ter (tiveram) → tivera · estar → estivera", "", "Estivera ali muitas vezes."],
 ["quem me dera! · pudera! · tomara que", "les expressions figées", "Quem me dera ter férias!"],
 ["= tinha + participe", "l'équivalent courant", "Fizera = tinha feito."],
],
"exemples": [
 ["Quando chegou, já o comboio partira.", "Quand il est arrivé, le train était déjà parti."],
 ["Quem me dera estar na praia!", "Si seulement j'étais à la plage !"],
 ["Ganhou o prémio? Pudera, trabalhou tanto!", "Il a gagné le prix ? Évidemment, il a tellement travaillé !"],
],
"attention": "À la 3e personne du pluriel, <b>falaram</b> peut être perfeito ou mais-que-perfeito : c'est le contexte qui tranche. À l'oral, on dit <b>tinham falado</b>.",
"serie": "maisQuePerfeitoSimplesPtExercises", "kicker": "Fizera, dissera",
"questions": """
Quando cheguei, ele já ___ (= tinha saído). | saíra | saiu / sairá | Quand je suis arrivé, il était déjà parti. | Saíram → saíra.
Ela ___ que voltaria (= tinha dito). | dissera | disse-ra / dizera | Elle avait dit qu'elle reviendrait. | Disseram → dissera.
___ um dia muito longo (= tinha sido). | Fora | Fôra / Ia | Ça avait été une très longue journée. | Foram → fora.
Nunca ___ tanta gente na praça (= tinha visto). | vira | viu / verá | Il n'avait jamais vu autant de monde sur la place. | Viram → vira.
Quem me ___ ter férias! | dera | deu / daria | Si seulement j'avais des vacances ! | Expression figée : quem me dera.
Ganhou? ___, treinou todos os dias! | Pudera | Pôde / Poderá | Il a gagné ? Évidemment, il s'est entraîné tous les jours ! | Pudera : évidemment.
O romance contava o que ___ naquela aldeia (= tinha acontecido). | acontecera | aconteceu-se / acontecerá | Le roman racontait ce qui s'était passé dans ce village. | Aconteceram → acontecera.
Nós já ___ aquele museu (= tínhamos visitado). | visitáramos | visitamos / visitaremos | Nous avions déjà visité ce musée. | 1re pers. du pluriel : visitáramos (accent).
___ que chova amanhã, os campos estão secos! | Tomara | Tomou / Toma | Pourvu qu'il pleuve demain, les champs sont secs ! | Tomara que + conjuntivo.
O jornal informou que o ministro ___ a demissão (= tinha apresentado). | apresentara | apresentou-se / apresentará | Le journal a annoncé que le ministre avait présenté sa démission. | Apresentaram → apresentara.
Ele ___ ali muitas vezes em criança (= tinha estado). | estivera | esteve-ra / estara | Il était venu là bien des fois enfant. | Estiveram → estivera.
Tudo era como ela ___ (= tinha imaginado). | imaginara | imaginou-se / imaginará | Tout était comme elle l'avait imaginé. | Imaginaram → imaginara.
"""
},
{
"id": "portugal-brasil", "titre": "Portugal ou Brésil ?", "resume": "reconnaître l'autre portugais",
"regle": "Vous apprenez le portugais du Portugal, mais vous entendrez souvent celui du Brésil (séries, musique, Internet). Les différences principales : <b>estou a fazer</b> (PT) / <b>estou fazendo</b> (BR) ; <b>chamo-me</b> (PT) / <b>me chamo</b> (BR) ; <b>tu fazes</b> (PT) / <b>você faz</b> (BR) ; <b>o meu carro</b> (PT) / <b>meu carro</b> (BR) ; <b>ter de</b> (PT) / <b>ter que</b> (BR). Le vocabulaire : <b>comboio / trem</b>, <b>autocarro / ônibus</b>, <b>pequeno-almoço / café da manhã</b>, <b>casa de banho / banheiro</b>, <b>telemóvel / celular</b>, <b>frigorífico / geladeira</b>, <b>sumo / suco</b>, <b>equipa / time</b>. L'orthographe : <b>facto / fato</b>, <b>económico / econômico</b>, <b>bebé / bebê</b>.",
"tableau": [
 ["estou a ler · estou lendo", "la forme progressive", ""],
 ["chamo-me · me chamo", "le pronom", ""],
 ["o meu livro · meu livro", "l'article devant le possessif", ""],
 ["comboio · trem", "le train", ""],
 ["pequeno-almoço · café da manhã", "le petit-déjeuner", ""],
 ["económico · econômico · facto · fato", "l'orthographe", ""],
],
"exemples": [
 ["(PT) Estou a beber um sumo no comboio. = (BR) Estou bebendo um suco no trem.", "Je bois un jus dans le train."],
 ["(BR) Você pegou o ônibus? = (PT) Apanhaste o autocarro?", "Tu as pris le bus ?"],
 ["(BR) Meu time ganhou! = (PT) A minha equipa ganhou!", "Mon équipe a gagné !"],
],
"attention": "Attention aux mots qui changent de sens : <b>rapariga</b> (fille, au Portugal) est grossier au Brésil, où l'on dit <b>moça, garota</b> ; <b>apelido</b> est le nom de famille au Portugal, le surnom au Brésil ; <b>propina</b> : frais de scolarité au Portugal, pot-de-vin au Brésil.",
"serie": "portugalBrasilPtExercises", "kicker": "Portugal ou Brésil ?",
"questions": """
Au Portugal, « je suis en train de manger » : estou ___. | a comer | comendo / comer-me | Je suis en train de manger. | PT : estar a + infinitif.
Au Portugal, « le train » : o ___. | comboio | trem / bonde | Le train. | BR : trem ; PT : comboio.
Au Portugal, « le bus » : o ___. | autocarro | ônibus / bonde | Le bus. | BR : ônibus ; PT : autocarro.
Au Portugal, « le petit-déjeuner » : o ___. | pequeno-almoço | café da manhã / desjejum | Le petit-déjeuner. | BR : café da manhã.
Au Portugal, « la salle de bain » : a ___. | casa de banho | banheiro / toalete | La salle de bain. | BR : banheiro.
Au Portugal, « le téléphone portable » : o ___. | telemóvel | celular / móvel | Le téléphone portable. | BR : celular.
Au Portugal, « je m'appelle » : ___. | chamo-me | me chamo / eu me chamo | Je m'appelle. | PT : le pronom après le verbe.
Au Portugal, « mon frère » : ___ irmão. | o meu | meu / mio | Mon frère. | PT : l'article devant le possessif.
Au Portugal, « le jus d'orange » : o ___ de laranja. | sumo | suco / jugo | Le jus d'orange. | BR : suco.
Au Portugal, « l'équipe » : a ___. | equipa | time / equipe | L'équipe. | BR : time, equipe.
Au Portugal, « le fait » : o ___. | facto | fato / feito | Le fait. | PT : facto ; BR : fato (qui veut dire « le costume » au Portugal).
Au Portugal, « le réfrigérateur » : o ___. | frigorífico | geladeira / refrigerador | Le réfrigérateur. | BR : geladeira.
Au Portugal, « je dois partir » : tenho ___ sair. | de | que de / a | Je dois partir. | PT : ter de ; BR : ter que.
Au Portugal, « le bébé » : o ___. | bebé | bebê / nenê | Le bébé. | PT : bebé ; BR : bebê.
"""
},
{
"id": "expressoes-idiomaticas", "titre": "Les expressions idiomatiques", "resume": "pôr-se a pau, ficar a ver navios, ir ao charco",
"regle": "Le portugais européen est riche en images. Quelques expressions courantes : <b>ficar a ver navios</b> (rester le bec dans l'eau), <b>pôr-se a pau</b> (se méfier, faire gaffe), <b>meter água</b> (faire une gaffe), <b>estar com os azeites</b> (être de mauvaise humeur), <b>ser pão-pão, queijo-queijo</b> (appeler un chat un chat), <b>custar os olhos da cara</b> (coûter les yeux de la tête), <b>chover a potes</b> (pleuvoir à verse), <b>andar com a cabeça nas nuvens</b> (avoir la tête dans les nuages), <b>dar com a língua nos dentes</b> (vendre la mèche), <b>tirar o cavalinho da chuva</b> (se faire une raison, ne pas y compter).",
"tableau": [
 ["ficar a ver navios", "rester le bec dans l'eau", "Esperou e ficou a ver navios."],
 ["pôr-se a pau", "faire gaffe, se méfier", "Põe-te a pau com ele."],
 ["meter água", "faire une gaffe", "Meti água na reunião."],
 ["custar os olhos da cara", "coûter les yeux de la tête", "O jantar custou os olhos da cara."],
 ["chover a potes", "pleuvoir à verse", "Está a chover a potes."],
 ["tirar o cavalinho da chuva", "ne pas y compter", "Podes tirar o cavalinho da chuva."],
],
"exemples": [
 ["Ele prometeu vir, mas ficámos a ver navios.", "Il avait promis de venir, mais nous sommes restés le bec dans l'eau."],
 ["Não dês com a língua nos dentes, é surpresa!", "Ne vends pas la mèche, c'est une surprise !"],
 ["O meu chefe hoje está com os azeites.", "Mon patron est de mauvaise humeur aujourd'hui."],
],
"attention": "Beaucoup de ces expressions sont propres au Portugal : <b>estar com os azeites</b> ou <b>pôr-se a pau</b> font sourire un Brésilien. C'est justement ce qui fait sonner « européen ».",
"serie": "expressoesIdiomaticasPtExercises", "kicker": "Les expressions",
"questions": """
Ele não apareceu e nós ficámos a ver ___. | navios | barcos / estrelas | Il n'est pas venu et nous sommes restés le bec dans l'eau. | Ficar a ver navios.
Põe-te a ___ com aquele vendedor. | pau | pé / pão | Méfie-toi de ce vendeur. | Pôr-se a pau : faire gaffe.
Disse o nome errado na reunião. Meti ___! | água | o pé / a pata | J'ai dit le mauvais nom à la réunion. J'ai fait une gaffe ! | Meter água.
Este carro custou os olhos da ___. | cara | cabeça / mão | Cette voiture a coûté les yeux de la tête. | Custar os olhos da cara.
Leva o guarda-chuva, está a chover a ___. | potes | cântaros / baldes de água | Prends le parapluie, il pleut à verse. | Chover a potes (PT).
Se esperas que ele pague, podes tirar o ___ da chuva. | cavalinho | gatinho / chapéu | Si tu attends qu'il paie, tu peux toujours courir. | Tirar o cavalinho da chuva.
Não contes a ninguém! Não dês com a língua nos ___. | dentes | lábios / olhos | Ne le dis à personne ! Ne vends pas la mèche. | Dar com a língua nos dentes.
Ele anda sempre com a cabeça nas ___. | nuvens | estrelas / árvores | Il a toujours la tête dans les nuages. | Andar com a cabeça nas nuvens.
Hoje não lhe fales, ele está com os ___. | azeites | óleos / vinagres | Ne lui parle pas aujourd'hui, il est de mauvaise humeur. | Estar com os azeites.
Comigo é pão-pão, ___-queijo. | queijo | vinho / manteiga | Avec moi, on appelle un chat un chat. | Ser pão-pão, queijo-queijo.
Esse problema é ___ de outro saco. | farinha | arroz / pão | Ce problème, c'est une autre paire de manches. | Ser farinha de outro saco.
Fiz o trabalho todo e ele levou os louros. Fiquei a ___. | chuchar no dedo | ver estrelas / ganhar | J'ai fait tout le travail et il a récolté les lauriers. Je me suis fait avoir. | Ficar a chuchar no dedo : se faire avoir.
"""
},
]
