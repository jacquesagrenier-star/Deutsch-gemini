# -*- coding: utf-8 -*-
"""La variante BRESILIENNE : ce qui ne se convertit pas, ecrit a la main.

SOURCE (30 oct. 2026). bresil.py convertit le portugais ; les explications en
FRANCAIS qui opposent le Portugal au Bresil (« au Portugal, on dit estar a +
infinitif ») deviendraient fausses : elles sont reecrites ici. Chaque entree :
(debut du texte europeen, texte bresilien complet). Le debut suffit a la
retrouver ; si le texte europeen change au point de ne plus commencer ainsi,
construire.py le signale (« explication non reecrite »).

Aussi ici : la prononciation du Bresil (celle de Sao Paulo et Rio, la norme
des medias, qui remplace entierement celle de Lisbonne), les reperes de
prononciation des nombres, et les titres de scenes.

BROUILLON : a faire relire par un lusophone du Bresil.
"""

REECRITURES = [
# ---------------------------------------------------------------- A1 voyage
("Au Portugal, apanhar (attraper) un transport",
 "Prendre un transport : pegar (pegar o ônibus, pegar o metrô). Ir de : ir de metrô, ir de trem ; mais ir a pé, à pied."),
("Au guichet, on vous dit o senhor, a senhora",
 "Au guichet, on vous dit o senhor, a senhora, ou você ; le possessif devient o seu, a sua (votre). Le CPF (numéro fiscal) est demandé partout au Brésil."),
("Au Portugal, on décrit un logement par le nombre de chambres",
 "Au Brésil, on décrit un logement par le nombre de chambres : um apartamento de dois quartos. Le loyer : o aluguel."),
("Au Portugal, on « attrape » le bus",
 "Prendre le bus : pegar o ônibus (au Portugal, apanhar o autocarro). Le train se dit o trem, le tram o bonde. Ir de : ir de metrô, en métro."),
("Perfeito, 1re pers. du pluriel : visitámos",
 "Perfeito, 1re pers. du pluriel : visitamos (au Brésil, la même forme qu'au présent)."),
("Perceber : comprendre (au Portugal)",
 "Entender : comprendre (perceber veut plutôt dire remarquer). Escreve ! (écris !) : l'impératif de tu a la forme de ele ; avec você, escreva !"),
# ---------------------------------------------------------------- conjugaison
("La forme du Portugal pour ce qui se passe maintenant.",
 "Ce qui se passe maintenant : estar + le gérondif en -ndo (estou lendo, está chovendo). C'est la forme de tout le Brésil."),
("Un seul temps pour « j'ai parlé » et « je parlai ». Falámos",
 "Un seul temps pour « j'ai parlé » et « je parlai ». Au Brésil, nós falamos (passé) s'écrit comme le présent : le contexte tranche. Ser et ir ont le même passé : fui, foi."),
("Nós falámos, avec accent",
 "Nós falamos, sans accent au Brésil : le passé et le présent s'écrivent pareil, le contexte tranche. À la 1re personne, -car → -quei, -gar → -guei, -çar → -cei."),
("Deux terminaisons seulement : -ava (verbes en -ar) et -ia (-er, -ir). Quatre irréguliers",
 "Deux terminaisons seulement : -ava (verbes en -ar) et -ia (-er, -ir). Quatre irréguliers : ser (era), ter (tinha), vir (vinha), pôr (punha). À l'oral, il adoucit aussi une demande : eu queria um café."),
("Au Portugal, l'action en cours est estar a + infinitif",
 "L'action en cours : estar + gérondif (estou lendo). Andar + gérondif : une activité répétée ces temps-ci (ando estudando muito)."),
("L'infinitif + -ia, -ias, -ia, -íamos, -iam. Les trois mêmes radicaux courts",
 "L'infinitif + -ia, -ias, -ia, -íamos, -iam. Les trois mêmes radicaux courts qu'au futur : far-, dir-, trar-. C'est la forme polie de tous les jours : gostaria, poderia."),
("Ces participes courts sont les seuls en usage",
 "Ces participes courts sont les seuls en usage (pas de « fazido »). Au Brésil, on dit aceito (foi aceito)."),
("me + o = mo, te + a = ta",
 "me + o = mo, te + a = ta, lhe + o = lho : des formes de l'écrit littéraire. Au Brésil, à l'oral, on dit plutôt « me dá isso », « eu dei para ele »."),
("Le gérondif ne vit au Portugal qu'avec ir",
 "Le gérondif est partout au Brésil : l'action en cours (estou fazendo), la progression (vai melhorando), la manière (saiu correndo)."),
("Futur et conditionnel, sans déclencheur : le pronom au milieu",
 "Futur et conditionnel : au Brésil, le pronom passe devant le verbe (te darei, se diria). La forme au milieu (dar-te-ei) n'existe plus qu'à l'écrit très soutenu."),
("accepté · remis (court partout, au Portugal)", "accepté · remis (court partout)"),
# ---------------------------------------------------------------- titres de series
("Estar a + infinitif", "Estar + gérondif"),
("Le pronom après le verbe", "Le pronom devant le verbe"),
("O meu, a minha", "Meu, minha"),
("Tu, você, o senhor", "Você, tu, o senhor"),
# ---------------------------------------------------------------- mots
("S'il vous plaît. (au Portugal)", "S'il vous plaît."),
("vous (à éviter souvent au Portugal)", "vous, tu (le pronom de tous les jours au Brésil)"),
# ---------------------------------------------------------------- grammaire
("Le portugais du Portugal s'écrit presque comme il se lit",
 "Le portugais du Brésil s'écrit presque comme il se lit… à condition de savoir que te et de se disent « tchi » et « dji », et que le l final se dit « ou ». Ces règles couvrent ce qui surprend le plus un francophone. Touche un mot pour l'entendre."),
("Portugal ou Brésil ?", "Brésil ou Portugal ?"),
("Le portugais a deux verbes pour « être ».",
 "Le portugais a deux verbes pour « être ». <b>Ser</b> dit ce qu'on est : l'identité, l'origine, le métier, le caractère, l'heure (<b>Sou canadense</b>, <b>É professora</b>). <b>Estar</b> dit comment on est ou où l'on est en ce moment : un état passager, un lieu (<b>Estou cansado</b>, <b>Estou em casa</b>). Pour situer un lieu fixe (un bâtiment, une ville), on dit volontiers <b>ficar</b> : <b>O museu fica ali</b>."),
("L'article défini est <b>o</b> (masculin)",
 "L'article défini est <b>o</b> (masculin), <b>a</b> (féminin), <b>os</b>, <b>as</b> au pluriel. L'indéfini : <b>um</b>, <b>uma</b>, <b>uns</b>, <b>umas</b>. La plupart des noms en <b>-o</b> sont masculins, en <b>-a</b> féminins ; mais il y a des surprises : <b>o dia</b>, <b>o mapa</b>, <b>o problema</b>, <b>a mão</b>. Devant un prénom, l'article dépend des régions : <b>a Ana</b> à São Paulo, <b>Ana</b> tout court dans le Nord-Est."),
("Au Portugal, <b>tu</b> s'emploie entre amis",
 "Au Brésil, on tutoie et on vouvoie avec <b>você</b> : un seul mot, et le verbe à la forme de <b>ele</b> (<b>Você fala inglês?</b>). <b>Tu</b> existe aussi, surtout dans le Sud et le Nord-Est, souvent avec le verbe de ele (<b>tu vai</b>). Avec une personne âgée ou au guichet, on dit <b>o senhor</b>, <b>a senhora</b>. Au pluriel, <b>vocês</b> sert pour tout le monde."),
("Les villes n'ont souvent pas d'article",
 "Les villes n'ont souvent pas d'article (<b>em São Paulo</b>, <b>de Lisboa</b>), mais certaines en ont un : <b>no Rio de Janeiro</b>, <b>do Porto</b>. De même pour les pays : <b>em Portugal</b>, mais <b>no Brasil</b>, <b>no Canadá</b>, <b>na França</b>."),
("Le possessif s'accorde avec la chose possédée",
 "Le possessif s'accorde avec la chose possédée, comme en français : <b>meu livro</b>, <b>minha casa</b>, <b>meus amigos</b>, <b>minhas chaves</b>. Au Brésil, l'article devant est facultatif : <b>minha mãe</b> ou <b>a minha mãe</b>. Pour « son, sa », on dit le plus souvent <b>dele</b> (à lui) et <b>dela</b> (à elle), après le nom : <b>o carro dele</b> ; <b>seu</b> veut surtout dire « ton, votre » (à você)."),
("Pour dire ce qui se passe en ce moment, le Portugal emploie",
 "Pour dire ce qui se passe en ce moment, on emploie <b>estar</b> + le gérondif en <b>-ndo</b> : <b>Estou lendo</b> (je suis en train de lire), <b>Está chovendo</b> (il pleut). Le gérondif se forme sur l'infinitif : <b>-ar → -ando</b>, <b>-er → -endo</b>, <b>-ir → -indo</b>. Au Portugal, on dirait <i>estou a ler</i>."),
("Pour une habitude, le présent simple suffit",
 "Pour une habitude, le présent simple suffit : <b>Trabalho em São Paulo</b> (je travaille à São Paulo, en général) ≠ <b>Estou trabalhando</b> (là, maintenant)."),
("Au Portugal, le petit pronom (<b>me, te, se, nos, lhe, o, a</b>)",
 "Au Brésil, le petit pronom (<b>me, te, se, nos, lhe</b>) se place <b>devant</b> le verbe : <b>Eu me chamo Ana</b>, <b>Me levanto às sete</b>, <b>Te dou o meu número</b>. À l'écrit soigné, on évite de commencer une phrase par le pronom (<b>Chamo-me Ana</b>), mais à l'oral c'est la règle. Avec deux verbes, il se met entre les deux : <b>Vou me deitar</b>."),
("Une phrase portugaise ne commence jamais par le pronom",
 "<b>Me dá um café</b> est la façon normale de parler au Brésil ; à l'écrit très soigné, on écrit <b>Dê-me um café</b>. Au Portugal, on dirait <i>Dá-me um café</i>."),
("<b>Bom → melhor</b>, <b>mau → pior</b>, <b>grande → maior</b> : jamais",
 "<b>Bom → melhor</b>, <b>mau → pior</b>, <b>grande → maior</b>, <b>pequeno → menor</b> : jamais <i>mais bom</i>."),
("Au Portugal, <b>falámos</b> (passé) porte un accent",
 "Au Brésil, <b>falamos</b> sert au passé comme au présent : le contexte tranche (<b>Ontem falamos</b>). Et <b>fui</b> veut dire à la fois « je suis allé » et « j'ai été »."),
("<b>Há</b> (du verbe haver) veut dire « il y a »",
 "<b>Há</b> (du verbe haver) veut dire « il y a » et ne change jamais : <b>Há um café na esquina</b>, <b>Há muitas pessoas</b>. À l'oral, le Brésil dit très souvent <b>tem</b> : <b>Tem um café na esquina</b>. Pour le temps écoulé, toujours <b>há</b> (ou <b>faz</b>) : <b>Moro aqui há dois anos</b>, <b>Cheguei faz uma hora</b>."),
("Beaucoup de mots portugais ressemblent au français et veulent dire autre chose.",
 "Beaucoup de mots portugais ressemblent au français et veulent dire autre chose. <b>Apelido</b> est le surnom (le nom de famille se dit <b>sobrenome</b>). <b>Constipado</b> veut dire constipé ; enrhumé se dit <b>resfriado</b>. <b>Esquisito</b> : bizarre. <b>Puxar</b> : tirer (sur une porte !) et <b>empurrar</b> : pousser. <b>Propina</b> : un pot-de-vin."),
("Au Portugal, l'imperfeito remplace aussi très souvent le conditionnel",
 "À l'oral, l'imperfeito remplace souvent le conditionnel : <b>Eu queria um café</b> (je voudrais un café), <b>Se pudesse, ia</b> (si je pouvais, j'irais). <b>Gostaria</b> et <b>poderia</b> restent la forme polie la plus courante."),
("Pour comparer : <b>mais … (do) que</b>",
 "Pour comparer : <b>mais … (do) que</b> (plus … que), <b>menos … (do) que</b> (moins … que), <b>tão … quanto</b> (aussi … que). Le superlatif : <b>o / a mais …</b> (<b>a cidade mais bonita</b>). Quatre formes irrégulières : <b>bom → melhor</b>, <b>mau → pior</b>, <b>grande → maior</b>, <b>pequeno → menor</b>. Pour « très, extrêmement » : <b>muito caro</b>, ou le suffixe <b>-íssimo</b> (<b>caríssimo</b>)."),
("On ne dit jamais <b>mais bom</b> ni <b>mais grande</b>",
 "On ne dit jamais <b>mais bom</b> ni <b>mais grande</b> : c'est <b>melhor</b>, <b>maior</b>. Et pour « plus petit », <b>menor</b>."),
("Le complément direct (le, la, les) : <b>o, a, os, as</b>",
 "Le complément direct (le, la, les) : <b>o, a, os, as</b> ; le complément indirect (lui, leur) : <b>lhe, lhes</b>. À l'écrit, ils se placent devant le verbe (<b>Eu o vi ontem</b>) ou après, avec un trait d'union après un infinitif (<b>Vou comprá-lo</b>). À l'oral, le Brésil les remplace souvent par <b>ele, ela</b> ou les omet : <b>Vi ele ontem</b>, <b>Comprei</b> (je l'ai acheté). Pour lui : <b>Dei o livro para ele</b>."),
("Pour une demande polie, le Portugal préfère souvent une question",
 "Pour une demande polie, on préfère souvent une question à l'impératif : <b>Você pode fechar a janela?</b>, <b>Pode esperar um pouquinho?</b> (Vous pouvez attendre un instant ?)."),
("Au Portugal, l'obligation se dit surtout <b>ter de</b>",
 "L'obligation se dit surtout <b>ter que</b> + infinitif : <b>Tenho que trabalhar</b> (je dois travailler) ; <b>ter de</b> existe, plus soutenu. <b>Dever</b> + infinitif est plus doux, un conseil ou une probabilité : <b>Você deve descansar</b> (tu devrais te reposer), <b>Ele deve estar em casa</b> (il doit être chez lui). <b>É preciso</b> + infinitif : une obligation générale. <b>Precisar</b> : avoir besoin de (<b>Preciso de ajuda</b>, <b>Preciso sair</b>). L'interdiction : <b>não pode</b>, <b>é proibido</b>."),
("Le Brésil dit <b>ter que</b> ; le Portugal dit <b>ter de</b>.",
 "<b>Ter que</b> est la forme courante, <b>ter de</b> la forme soignée. Et <b>precisar</b> prend <b>de</b> devant un nom (<b>preciso de ajuda</b>), souvent rien devant un infinitif (<b>preciso sair</b>)."),
("Quelques verbes + préposition + infinitif disent où en est l'action",
 "Quelques verbes + préposition + infinitif disent où en est l'action : <b>acabar de</b> (venir de : <b>Acabei de chegar</b>), <b>voltar a</b> (refaire : <b>Voltou a chover</b>), <b>começar a</b> (se mettre à), <b>deixar de</b> (arrêter de : <b>Parei de fumar</b>), <b>estar para</b> (être sur le point de). L'action en cours se dit <b>estar</b> + gérondif, et ce qui dure, <b>andar</b> ou <b>continuar</b> + gérondif (<b>Ando lendo um livro ótimo</b>, <b>Continua trabalhando</b>)."),
("Le <b>condicional</b> se forme sur l'infinitif",
 "Le <b>condicional</b> se forme sur l'infinitif + <b>-ia, -ias, -ia, -íamos, -iam</b> : <b>falaria</b>, <b>comeria</b>. Trois irréguliers, comme au futur : <b>fazer → faria</b>, <b>dizer → diria</b>, <b>trazer → traria</b>. Il sert à la politesse (<b>Gostaria de reservar</b>), à l'hypothèse (<b>Eu não faria isso</b>) et au futur vu du passé (<b>Disse que viria</b>). À l'oral, l'<b>imperfeito</b> le remplace souvent : <b>Eu não fazia isso</b>."),
("Pour une action antérieure à une autre action passée",
 "Pour une action antérieure à une autre action passée : <b>tinha</b> (imperfeito de ter) + participe passé : <b>Quando cheguei, o trem já tinha partido</b>. Le participe ne s'accorde pas. Participes irréguliers à connaître : <b>feito</b> (fazer), <b>dito</b> (dizer), <b>escrito</b>, <b>visto</b> (ver), <b>vindo</b> (vir), <b>posto</b> (pôr), <b>aberto</b>, <b>coberto</b>, <b>ganho</b>, <b>gasto</b>, <b>pago</b>, <b>aceito</b>. La forme simple (<b>falara, fizera</b>) existe, mais seulement à l'écrit littéraire."),
("Au Portugal, le pronom se place normalement <b>après</b> le verbe",
 "Au Brésil, le pronom se place normalement <b>devant</b> le verbe (próclise) : <b>Me dá o sal</b>, <b>Eu me levanto cedo</b>. Avec deux verbes, il se met entre les deux, sans trait d'union : <b>Vou te ligar</b>, <b>Quero me deitar</b>. L'écrit soigné garde l'enclise en tête de phrase (<b>Levanto-me cedo</b>) et après un infinitif (<b>para ajudá-lo</b>). La mésoclise (<b>dar-te-ei</b>) n'existe plus qu'à l'écrit très soutenu."),
("Jamais de pronom en tête de phrase au Portugal",
 "À l'oral, la phrase commence volontiers par le pronom : <b>Me dá</b>, <b>Te ligo amanhã</b>. Et le sujet ne change rien : <b>Ele se chama Rui</b>. Au Portugal, on dirait <i>Dá-me</i>, <i>Ele chama-se Rui</i>."),
("<b>Afinal</b> ne veut pas seulement dire « finalement »",
 "<b>Afinal</b> ne veut pas seulement dire « finalement » : il marque souvent une surprise, ce qu'on découvre : <b>Afinal era você!</b> (Ah, c'est donc toi !). Et <b>de fato</b> (en fait) s'écrit sans c au Brésil."),
("Le gérondif portugais (<b>-ando, -endo, -indo</b>) vit au Portugal",
 "Le gérondif (<b>-ando, -endo, -indo</b>) est partout au Brésil : l'action en cours (<b>estou fazendo</b>), la progression (<b>vai melhorando</b>), et en tête de phrase (<b>Chegando em casa, te liguei</b>)."),
("Quand un pronom indirect (<b>me, te, lhe, nos, vos, lhes</b>) rencontre",
 "Quand un pronom indirect (<b>me, te, lhe</b>) rencontre un pronom direct (<b>o, a</b>), l'écrit littéraire les soude : <b>me + o = mo</b>, <b>lhe + o = lho</b>. Le Brésil a presque perdu ces formes : on dit <b>Me dá isso</b> (donne-le-moi), <b>Já te falei</b> (je te l'ai déjà dit), <b>Ela deu para ele</b> (elle le lui a donné). À connaître pour les lire, pas pour les dire."),
("<b>A gente</b> existe au Portugal, mais il est plus familier",
 "<b>A gente</b> (on, nous) est la forme de tous les jours au Brésil, avec le verbe au singulier : <b>A gente vai ao cinema</b>. À l'écrit et dans la conversation soignée, on préfère <b>nós</b>."),
("Certains mots portugais ressemblent à des mots français mais n'ont pas le même sens.",
 "Certains mots portugais ressemblent à des mots français mais n'ont pas le même sens. <b>Puxar</b> = tirer (sur une porte : <b>Puxe</b>), <b>empurrar</b> = pousser. <b>Esquisito</b> = bizarre (pas « exquis », qui se dit <b>delicioso, requintado</b>). <b>Propina</b> = pot-de-vin. <b>Constipado</b> = constipé (enrhumé se dit <b>resfriado</b>). <b>Borracha</b> = gomme. <b>Largo</b> = large, et aussi une place (<b>o Largo do Boticário</b>). <b>Apelido</b> = surnom ; nom de famille = <b>sobrenome</b>."),
("Au futur et au conditionnel, quand rien n'attire le pronom",
 "Au futur et au conditionnel, l'écrit très soutenu place le pronom à l'intérieur du verbe (mésoclise) : <b>dar-te-ei</b>, <b>dir-se-ia</b>. Au Brésil, cette forme a pratiquement disparu : on dit <b>te darei</b>, <b>se diria</b>, ou plus simplement <b>vou te dar</b>. À reconnaître dans un texte officiel ou un livre ancien, pas à employer."),
("La mésoclise est bien vivante à l'écrit au Portugal",
 "La mésoclise ne vit plus au Brésil qu'à l'écrit très soutenu ; elle est encore courante à l'écrit au Portugal. Dans la conversation, on l'évite avec <b>ir + infinitif</b> : <b>vou te dizer</b>."),
("Certains verbes ont deux participes.",
 "Certains verbes ont deux participes. Le <b>long</b>, régulier, va avec <b>ter</b> ; le <b>court</b> avec <b>ser</b> et <b>estar</b> : <b>Tinha acendido a luz</b> / <b>A luz estava acesa</b>. Mais plusieurs courts ont tout gagné et servent aussi avec ter : <b>ganho, gasto, pago</b>, et <b>aceito</b>, <b>entregue</b> : <b>Tinha pago as contas</b>, <b>Já tinha entregue o trabalho</b>. Autres paires : <b>eleger</b> (elegido / eleito), <b>prender</b> (prendido / preso), <b>imprimir</b> (imprimido / impresso), <b>morrer</b> (morrido / morto), <b>limpar</b> (limpado / limpo), <b>salvar</b> (salvado / salvo)."),
("ter / ser + aceite, entregue (Portugal)", "ter / ser + aceito, entregue"),
("Au Brésil, on dit <b>aceito</b> (« foi aceito »)",
 "Au Brésil, on dit <b>aceito</b> (« foi aceito ») ; au Portugal, <i>aceite</i>. Et <b>entregado</b> survit à peine : <b>entregue</b> partout."),
("Pour mettre un élément en valeur : <b>é que</b>",
 "Pour mettre un élément en valeur : <b>é que</b> après le mot (<b>Eu é que paguei</b> — c'est moi qui ai payé ; <b>Onde é que você mora?</b>), <b>ser… que</b> qui encadre (<b>Foi a Ana que telefonou</b>, <b>Foi ontem que chegaram</b>), <b>o que… é</b> en tête (<b>O que eu quero é descansar</b>), <b>quem… é</b> (<b>Quem sabe é o Rui</b>). Le verbe <b>ser</b> s'accorde souvent en temps : <b>Foi em 1974 que…</b>, <b>É agora que…</b>. Dans les questions, le Brésil dit volontiers <b>O que você faz?</b>, ou <b>O que é que você faz?</b>"),
("Le portugais écrit et administratif a son vocabulaire",
 "Le portugais écrit et administratif a son vocabulaire : <b>adquirir</b> (comprar), <b>efetuar, proceder a</b> (fazer), <b>solicitar</b> (pedir), <b>residir</b> (morar), <b>deslocar-se</b> (ir), <b>informar</b> (dizer), <b>encontrar-se</b> (estar). La politesse passe par <b>o senhor / a senhora</b> + 3e personne. Dans une lettre : <b>Prezado Senhor</b>, <b>Prezada Senhora</b>, et pour finir <b>Atenciosamente</b>. <b>Você</b> est le pronom de tous les jours, poli sans être distant."),
("« Doutor » ne se limite pas aux médecins",
 "« Doutor » ne se limite pas aux médecins : au Brésil, on l'emploie par respect pour un avocat, un médecin, un patron (<b>doutor Carlos</b>), parfois sans diplôme. C'est de la politesse, pas de la flatterie."),
("Vous apprenez le portugais du Portugal, mais vous entendrez souvent celui du Brésil",
 "Vous apprenez le portugais du Brésil, mais vous rencontrerez aussi celui du Portugal (et de l'Angola, du Mozambique). Les différences principales : <b>estou fazendo</b> (BR) / <b>estou a fazer</b> (PT) ; <b>me chamo</b> (BR) / <b>chamo-me</b> (PT) ; <b>você faz</b> (BR) / <b>tu fazes</b> (PT) ; <b>meu carro</b> (BR) / <b>o meu carro</b> (PT) ; <b>ter que</b> (BR) / <b>ter de</b> (PT). Le vocabulaire : <b>trem / comboio</b>, <b>ônibus / autocarro</b>, <b>café da manhã / pequeno-almoço</b>, <b>banheiro / casa de banho</b>, <b>celular / telemóvel</b>, <b>geladeira / frigorífico</b>, <b>suco / sumo</b>, <b>time / equipa</b>. L'orthographe : <b>fato / facto</b>, <b>econômico / económico</b>, <b>bebê / bebé</b>."),
("Attention aux mots qui changent de sens : <b>rapariga</b>",
 "Attention aux mots qui changent de sens : <b>rapariga</b> (jeune fille au Portugal) est grossier au Brésil, où l'on dit <b>moça, garota</b> ; <b>apelido</b> est le surnom au Brésil, le nom de famille au Portugal ; <b>propina</b> : pot-de-vin au Brésil, frais de scolarité au Portugal."),
("Beaucoup de ces expressions sont propres au Portugal",
 "Ces expressions sont celles du Portugal : un Brésilien les comprend souvent, mais en emploie d'autres (<b>ficar de olho</b> pour se méfier, <b>pisar na bola</b> pour faire une gaffe)."),
("Ce qu'on faisait d'habitude, le décor, l'âge, l'heure",
 "Ce qu'on faisait d'habitude, le décor, l'âge, l'heure, une action en cours dans le passé. <b>-ava</b> (-ar) et <b>-ia</b> (-er, -ir) ; irréguliers : era, tinha, vinha, punha. À l'oral, il adoucit aussi une demande : <b>queria</b>, <b>podia</b>.<br><em>Quando era criança, ia à praia todos os dias.</em> (Quand j'étais enfant, j'allais à la plage tous les jours.)"),
("Politesse, hypothèse, futur dans le passé. Infinitif",
 "Politesse, hypothèse, futur dans le passé. Infinitif + <b>-ia, -ias, -ia, -íamos, -iam</b> ; radicaux courts : faria, diria, traria. C'est la forme polie de tous les jours : <b>gostaria</b>, <b>poderia</b>.<br><em>Gostaria de reservar. Disse que viria.</em> (J'aimerais réserver. Il a dit qu'il viendrait.)"),
# ---------------------------------------------------------------- premiers pas
("« Premiers pas » en portugais du Portugal",
 "« Premiers pas » en portugais du Brésil (variante dérivée par bresil.py). Brouillon, à faire relire par un lusophone du Brésil."),
("Queria (je voudrais) est la forme polie",
 "Queria (je voudrais) est la forme polie qu'on entend partout. Quero (je veux) est direct. On ajoute volontiers por favor (s'il vous plaît)."),
("Pour un lieu fixe, le Portugal dit fica",
 "Pour un lieu fixe, on dit fica : Onde fica o museu? Pour savoir s'il y en a un : Tem uma farmácia aqui perto? (ou Há…, plus soigné)."),
("Ter est irrégulier : tenho, tens, tem.",
 "Ter est irrégulier : tenho, tem, temos. Avoir une réservation : ter uma reserva. Au Brésil, le rez-de-chaussée est o térreo, et le premier étage o primeiro andar."),
("« J'ai mal à la tête » se dit Dói-me a cabeça",
 "« J'ai mal à la tête » se dit Estou com dor de cabeça ou Minha cabeça dói ; au pluriel, Meus pés doem. « Je suis enrhumé » : estou resfriado (constipado veut dire constipé !)."),
("Le temps qu'il fait passe par estar",
 "Le temps qu'il fait passe par estar : está calor, está frio, está sol. La pluie en cours : está chovendo. « Je ne comprends pas » se dit não entendo."),
# ---------------------------------------------------------------- reperes
("Un et deux ont un féminin : um, uma ; dois, duas",
 "Un et deux ont un féminin : um, uma ; dois, duas (duas horas, deux heures). 16, 17 et 19 : dezesseis, dezessete, dezenove (au Portugal dezasseis, dezassete, dezanove). Au téléphone, on dit souvent meia (une demi-douzaine) pour six : meia, sete, oito."),
("Les couleurs s'accordent comme les adjectifs",
 "Les couleurs s'accordent comme les adjectifs : um carro vermelho, uma casa vermelha. Azul et verde ne changent qu'au pluriel (azuis, verdes). Rosa, laranja, cinza et marrom sont invariables (uma camisa cinza)."),
]

# Le Portugal ou Lisbonne dans un exemple, comme simple contenu : rien a reecrire.
CONTENU = ["Em Portugal", "Au Portugal, on porte", "Au Portugal, on cuisine", "Au Portugal, on vote",
           "Au Portugal, on mange", "Au Portugal, le droit de vote", "Au Portugal, on dîne", "Au Portugal, on sert",
           "La géographie du Portugal", "La radiodiffusion", "À Lisbonne, la piste", "brésilien", "Elle est brésilienne",
           "Je suis de Lisbonne", "C'est en 1974", "Chaque fois que je vais à Lisbonne", "le Portugal", "Portugal",
           "Le Brésil est plus grand", "Il est allé trois fois au Brésil", "du Portugal continental",
           "Portugal, sol", "Superlatif + de (Portugal"]


def reecriture(texte):
    for debut, br in REECRITURES:
        if texte.startswith(debut):
            return br
    return None


def contenu(texte):
    return any(texte.startswith(c) or c == texte for c in CONTENU)


# ---------------------------------------------------------------- prononciation
# Le Bresil des medias (Sao Paulo, Rio sans le s chuintant) : ce qui surprend
# un francophone. Meme format que prononciation_a1.py.
GROUPES_BR = [
("voyelles", [
 {"id": "voyelles-pleines", "graphie": "a · e · o", "api": "[a] · [e] · [o]",
  "court": "toutes les voyelles se disent",
  "explication": "Au Brésil, les voyelles ne s'avalent pas : chaque syllabe s'entend, ce qui rend le portugais du Brésil plus facile à suivre. telefone se dit « té-lé-FÔ-ni », pequeno « pi-KÉ-nou », noite « NOÏ-tchi ».",
  "exemples": "telefone | le téléphone\npequeno | petit\nnoite | la nuit\nsete | sept\ncasa | la maison\nobrigado | merci"},
 {"id": "e-o-final", "graphie": "e · o (fin de mot)", "api": "[i] · [u]",
  "court": "le e final se dit « i », le o final « ou »",
  "explication": "En fin de mot sans accent, e se dit « i » et o se dit « ou » : leite « LÉÏ-tchi », sete « SÉ-tchi », carro « KA-hou », obrigado « o-bri-GA-dou ».",
  "exemples": "leite | le lait\nsete | sept\nnome | le nom\ncarro | la voiture\nobrigado | merci\nfilho | le fils"},
 {"id": "nasales", "graphie": "ão · ã · õe · em · im · om · um", "api": "[ɐ̃w̃] · [ɐ̃] · [õj̃]",
  "court": "pão, mãe, põe : les nasales",
  "explication": "Le tilde (~) rend la voyelle nasale : ã comme « an » bref, ão comme « an » qui glisse vers « ou » (pão, não, mão), õe comme « on » qui glisse vers « i » (põe, lições). Une voyelle devant m ou n en fin de syllabe est nasale aussi : bem « bêïñ », sim, bom, um.",
  "exemples": "pão | le pain\nnão | non\nmãe | la mère\npõe | il met\nbem | bien\nsim | oui\num | un"},
 {"id": "accents", "graphie": "á · é · ó · â · ê · ô", "api": "[a] · [ɛ] · [ɔ] · [ɐ] · [e] · [o]",
  "court": "l'aigu ouvre, le circonflexe ferme",
  "explication": "L'accent marque la syllabe forte et le timbre : é et ó sont ouverts (café, avó), ê et ô fermés (você, avô). Le Brésil écrit ê et ô là où le Portugal écrit é et ó devant m ou n : econômico, tênis, Antônio.",
  "exemples": "café | le café\nvocê | vous, tu\navó | la grand-mère\navô | le grand-père\ntênis | les baskets\nônibus | l'autobus"},
]),
("consonnes", [
 {"id": "te-de", "graphie": "t · d (devant i, e final)", "api": "[tʃ] · [dʒ]",
  "court": "noite « noïtchi », cidade « sidadji »",
  "explication": "C'est le trait le plus frappant du Brésil : devant un i, ou un e final qui se dit « i », t devient « tch » et d devient « dj ». tia « TCHI-a », noite « NOÏ-tchi », dia « DJI-a », cidade « si-DA-dji ».",
  "exemples": "tia | la tante\nnoite | la nuit\ndia | le jour\ncidade | la ville\ntarde | l'après-midi\nleite | le lait"},
 {"id": "l-final", "graphie": "l (fin de syllabe)", "api": "[w]",
  "court": "Brasil « bra-ZIOU »",
  "explication": "En fin de syllabe, le l se dit « ou » : Brasil « bra-ZIOU », sol « SÔOU », azul « a-ZOU », mil « MIOU ». Mal (mal) et mau (mauvais) se disent donc pareil.",
  "exemples": "Brasil | le Brésil\nsol | le soleil\nazul | bleu\nmil | mille\nhotel | l'hôtel\nfutebol | le football"},
 {"id": "r", "graphie": "r · rr", "api": "[ɾ] · [h]",
  "court": "rua « hou-a », caro ≠ carro",
  "explication": "Entre deux voyelles, un r seul est battu, un petit coup de langue : caro, para, hora. En début de mot et quand il est doublé (rr), il se dit comme un h anglais soufflé : rua « HOU-a », carro « KA-hou », Rio « HI-ou ». En fin de mot, il est léger, parfois muet : falar « fa-LA ».",
  "exemples": "caro | cher\ncarro | la voiture\nhora | l'heure\nrua | la rue\nRio | Rio\nfalar | parler"},
 {"id": "s-final", "graphie": "s · z (fin de syllabe)", "api": "[s] · [z]",
  "court": "dois « doïs », três « trêïs »",
  "explication": "En fin de mot, s se dit « s », comme en français : dois, três, mais. Devant une voyelle, il se lie en « z » : os amigos « ou-za-MI-gous ». (À Rio, il se dit « ch », comme au Portugal.) Entre deux voyelles, un s seul se dit « z » : casa, mesa.",
  "exemples": "dois | deux\ntrês | trois\nmais | plus\ncasa | la maison\nmesa | la table\nfeliz | heureux"},
 {"id": "lh-nh", "graphie": "lh · nh", "api": "[ʎ] · [ɲ]",
  "court": "filho « filiou », vinho « vignou »",
  "explication": "lh se dit comme le « ill » de famille : filho, trabalho, olhar. nh se dit comme le « gn » de montagne : vinho, amanhã, senhor.",
  "exemples": "filho | le fils\ntrabalho | le travail\nolho | l'œil\nvinho | le vin\namanhã | demain\nsenhor | monsieur"},
 {"id": "ch-j-x", "graphie": "ch · j · g (e, i) · x", "api": "[ʃ] · [ʒ]",
  "court": "chave, já, gente : comme en français",
  "explication": "ch se dit « ch » (chave, chá), j et g devant e ou i se disent « j » (já, gente, hoje). Le x est capricieux : le plus souvent « ch » (caixa, baixo, peixe), parfois « z » (exame), « ks » (táxi) ou « s » (próximo).",
  "exemples": "chave | la clé\njá | déjà\nhoje | aujourd'hui\ngente | les gens\ncaixa | la caisse\ntáxi | le taxi"},
 {"id": "h-muet", "graphie": "h", "api": "—",
  "court": "hoje, hotel : le h ne se dit pas",
  "explication": "Le h ne se prononce jamais en début de mot : hoje « Ô-ji », hotel « o-TÉOU », homem. Il ne vit que dans ch, lh et nh.",
  "exemples": "hoje | aujourd'hui\nhotel | l'hôtel\nhomem | l'homme\nhora | l'heure\nhá | il y a"},
]),
]

INTRO_BR = ("Le portugais du Brésil s'écrit presque comme il se lit… à condition de savoir que te et de se disent "
            "« tchi » et « dji », et que le l final se dit « ou ».")


def prononciation_bresil():
    groupes = []
    for gid, regles in GROUPES_BR:
        rs = []
        for r in regles:
            rs.append({"id": r["id"], "graphie": r["graphie"], "api": r["api"], "court": {"fr": r["court"]},
                       "explication": {"fr": r["explication"]},
                       "exemples": [{"mot": l.split(" | ")[0], "traduction": l.split(" | ")[1]}
                                    for l in r["exemples"].split("\n")]})
        groupes.append({"id": gid, "regles": rs})
    return {"_note": "Derive de portugais/outils/bresil_textes.py (construire.py) : ne pas modifier a la main.",
            "groupes": groupes}


# Les nombres : ce qu'on entend au Bresil (Sao Paulo), en syllabes a la francaise.
NOMBRES_BR = {
    "zero": "ZÉ-rou", "um": "OUñ", "dois": "DOÏS", "três": "TRÊÏS", "quatro": "KOUA-trou", "cinco": "SIñ-kou",
    "seis": "SÉÏS", "sete": "SÉ-tchi", "oito": "OÏ-tou", "nove": "NÔ-vi", "dez": "DÉÏS", "onze": "Oñ-zi",
    "doze": "DÔ-zi", "treze": "TRÉ-zi", "catorze": "ka-TÔR-zi", "quatorze": "koua-TÔR-zi", "quinze": "KIñ-zi",
    "dezesseis": "dé-zi-SÉÏS", "dezessete": "dé-zi-SÉ-tchi", "dezoito": "dé-ZOÏ-tou", "dezenove": "dé-zi-NÔ-vi",
    "vinte": "VIñ-tchi", "vinte e um": "viñ-tchi-OUñ", "vinte e dois": "viñ-tchi-DOÏS", "trinta": "TRIñ-ta",
    "quarenta": "koua-RÊñ-ta", "cinquenta": "siñ-KOUÊñ-ta", "sessenta": "sé-SÊñ-ta", "setenta": "sé-TÊñ-ta",
    "oitenta": "oï-TÊñ-ta", "noventa": "no-VÊñ-ta", "cem": "SÊÏñ", "cento e um": "SÊñ-tou i OUñ",
    "duzentos": "dou-ZÊñ-tous", "trezentos": "tré-ZÊñ-tous", "quinhentos": "ki-GNÊñ-tous", "mil": "MIOU",
}

# Les titres des scenes : le Bresil n'a pas toujours le mot du Portugal.
TITRES_SCENES = {
    "bauernhof": "Na fazenda", "buergeramt": "Na repartição", "camping": "Acampamento no lago",
    "fahrradwerkstatt": "Na bicicletaria", "fruehstueck": "O café da manhã na padaria",
    "geburtstag": "Uma festa de aniversário", "heimwerken": "Consertos em casa", "park": "No parque",
    "sportplatz": "No campo de futebol", "ubahn": "No metrô", "zug": "No trem", "kreuzung": "No cruzamento",
}


# ---------------------------------------------------------------- series
# Les series qui enseignent un usage du Portugal (estar a, le pronom apres le
# verbe, la mesoclise...) se vident presque entierement dans la variante : celles-ci
# les remplacent, ecrites pour le Bresil. Format des fiches : question | bonne |
# fausses (/) | traduction | explication.
SERIES_BR = {
"estarAPtExercises": ("estar-a", """
Estou ___ um livro. | lendo | ler / a ler | Je suis en train de lire un livre. | Estar + gérondif : ler → lendo.
Está ___, leva o guarda-chuva. | chovendo | chover / chovido | Il pleut, prends le parapluie. | Chover → chovendo.
O que você está ___? | fazendo | fazer / feito | Qu'est-ce que tu es en train de faire ? | Fazer → fazendo.
As crianças estão ___ no parque. | brincando | brincar / brincado | Les enfants sont en train de jouer au parc. | -ar → -ando.
Nós estamos ___ agora. | jantando | jantar / jantamos | Nous sommes en train de dîner. | Estar + gérondif.
Ela está ___ com a mãe. | falando | falar / falou | Elle est en train de parler avec sa mère. | Falar → falando.
Eles estão ___ para a prova. | estudando | estudar / estudam | Ils sont en train de réviser pour l'examen. | Estudar → estudando.
Estou ___ a janela. | abrindo | abrir / aberto | J'ouvre la fenêtre (en ce moment). | -ir → -indo.
Ando ___ muito ultimamente. | trabalhando | trabalhar / trabalho | Je travaille beaucoup ces temps-ci. | Andar + gérondif : ce qui dure.
(en général) ___ em São Paulo. | Trabalho | Estou trabalhando / Trabalhando | (En général) je travaille à São Paulo. | Une habitude : le présent simple.
"""),
"atonosPtExercises": ("atonos", """
___ chamo Ana. | Me | Te / Se | Je m'appelle Ana. | À l'oral, le pronom se met devant le verbe : me chamo.
Não ___ lembro do nome dele. | me | se / te | Je ne me souviens pas de son nom. | Lembrar-se : eu me lembro.
Como você ___ chama? | se | te / me | Comment tu t'appelles ? | Você prend se : como você se chama?
Eu ___ levanto às sete. | me | se / te | Je me lève à sept heures. | Eu me levanto.
Nós ___ deitamos tarde. | nos | se / me | Nous nous couchons tard. | Nós nos deitamos.
Vou ___ ligar amanhã. | te | ti / tu | Je vais t'appeler demain. | Entre les deux verbes : vou te ligar.
Ela ___ olha no espelho. | se | lhe / me | Elle se regarde dans le miroir. | Ela se olha.
Ele ___ deu o número dele. | me | mim / eu | Il m'a donné son numéro. | Me (à moi), devant le verbe.
Quero ___ deitar cedo. | me | mim / eu | Je veux me coucher tôt. | Avec deux verbes, le pronom se met entre les deux.
"""),
"seImpessoalPtExercises": ("se-impessoal", """
Aqui ___ muito bem. | se come | se comem / comer | Ici, on mange très bien. | Sans nom pluriel : se + verbe au singulier.
___ apartamento. (un écriteau) | Aluga-se | Alugam-se / Aluga | Appartement à louer. | Sur les écriteaux, le Brésil garde aluga-se, vende-se.
___ apartamentos no centro. (un écriteau) | Vendem-se | Vende-se / Vendem | Appartements à vendre dans le centre. | À l'écrit, avec un nom pluriel, le verbe s'accorde.
No Brasil ___ muito arroz e feijão. | se come | se comem / come-me | Au Brésil, on mange beaucoup de riz et de haricots. | À l'oral : se + verbe, devant.
Aqui não ___ fumar. | se pode | se podem / pode-se não | Ici, on ne peut pas fumer. | Après não, le pronom est devant.
Como ___ diz isso em português? | se | si / lhe | Comment dit-on ça en portugais ? | Como se diz… ? : la question de tous les jours.
Na reunião ___ decidiu tudo. | se | si / lhe | À la réunion, on a tout décidé. | Se + verbe au singulier.
Hoje em dia ___ trabalha muito em casa. | se | si / lhe | Aujourd'hui, on travaille beaucoup chez soi. | Se impersonnel : « on ».
"""),
"portugalBrasilPtExercises": ("portugal-brasil", """
Au Brésil, « le train » : o ___. | trem | comboio / elétrico | Le train. | BR : trem ; PT : comboio.
Au Brésil, « le bus » : o ___. | ônibus | autocarro / bonde | Le bus. | BR : ônibus ; PT : autocarro.
Au Brésil, « le petit-déjeuner » : o ___. | café da manhã | pequeno-almoço / lanche | Le petit-déjeuner. | BR : café da manhã ; PT : pequeno-almoço.
Au Brésil, « la salle de bain » : o ___. | banheiro | casa de banho / quarto | La salle de bain. | BR : banheiro ; PT : casa de banho.
Au Brésil, « le portable » : o ___. | celular | telemóvel / telefone fixo | Le téléphone portable. | BR : celular ; PT : telemóvel.
Au Brésil, « le jus » : o ___. | suco | sumo / xarope | Le jus. | BR : suco ; PT : sumo.
Au Brésil, « je suis en train de manger » : estou ___. | comendo | a comer / comer | Je suis en train de manger. | BR : estar + gérondif ; PT : estar a + infinitif.
Au Brésil, « je dois partir » : tenho ___ sair. | que | a / em | Je dois partir. | BR : ter que (ter de, plus soigné).
Au Brésil, « le nom de famille » : o ___. | sobrenome | apelido / prenome | Le nom de famille. | BR : sobrenome ; au Portugal, apelido (au Brésil, apelido = surnom).
Au Brésil, « une jeune fille » : uma ___. | moça | rapariga / rapaz | Une jeune fille. | BR : moça, garota ; rapariga y est grossier.
Au Brésil, « l'équipe » (de football) : o ___. | time | equipa / clube | L'équipe. | BR : time ; PT : equipa.
Au Brésil, « la glace » (à manger) : o ___. | sorvete | gelado / bolo | La glace. | BR : sorvete ; PT : gelado.
"""),
}


# ---------------------------------------------------------------- fiches
# Les fiches qui enseignent un usage du Portugal : ce qui remplace leur titre,
# leur resume et leur tableau (en entier, ou ligne par ligne : « lignes »).
# Les lignes sont [portugais, francais, exemple] comme dans grammaire_a1.py.
FICHES_BR = {
"pronomes": {"titre": "Você, tu, o senhor : à qui l'on parle", "resume": "eu, você, ele, ela, nós, vocês, eles",
  "tableau": [["eu · você", "je · tu, vous", "Eu sou a Inês. E você?"],
              ["tu (Sud, Nord-Est)", "tu", "Tu vai ao cinema?"],
              ["ele · ela", "il · elle", "Ela é de Recife."],
              ["o senhor · a senhora", "vous (respect)", "A senhora precisa de ajuda?"],
              ["nós · a gente", "nous · on (courant)", "A gente se vê amanhã."],
              ["vocês · eles · elas", "vous (pluriel) · ils · elles", "Vocês são irmãos?"]],
  "exemples": [["Com licença, o senhor sabe onde fica a estação?", "Excusez-moi, monsieur, savez-vous où est la gare ?"],
               ["Rui, você vem jantar?", "Rui, tu viens dîner ?"],
               ["Você fala francês?", "Vous parlez français ?"]]},
"possessivos": {"titre": "Meu, minha : les possessifs", "resume": "meu, minha, meus, minhas — avec ou sans article",
  "lignes": {1: ["seu · sua · seus · suas", "ton, ta ; votre (à você)", "Esse é o seu celular?"],
             2: ["teu · tua", "ton, ta (avec tu)", "Gostei da tua casa."]}},
"estar-a": {"titre": "Estar + gérondif : en train de", "resume": "estou lendo, está chovendo",
  "tableau": [["estou + gérondif", "je suis en train de", "Estou trabalhando."],
              ["você está + gérondif", "tu es en train de", "Você está ouvindo?"],
              ["está chovendo", "il pleut (en ce moment)", "Leva o guarda-chuva, está chovendo."],
              ["estamos + gérondif", "nous sommes en train de", "Estamos jantando."],
              ["estão + gérondif", "ils sont en train de", "As crianças estão dormindo."],
              ["-ar → -ando · -er → -endo · -ir → -indo", "le gérondif", "falando, comendo, partindo"]],
  "exemples": [["O que você está fazendo? — Estou cozinhando.", "Qu'est-ce que tu fais ? — Je cuisine."],
               ["Não posso falar, estou dirigindo.", "Je ne peux pas parler, je conduis."],
               ["Está chovendo muito em São Paulo.", "Il pleut beaucoup à São Paulo."]]},
"pronomes-atonos": {"titre": "Me chamo, me levanto : le pronom devant le verbe", "resume": "eu me chamo, não me lembro, vou te ligar",
  "tableau": [["pronom + verbe", "dans une phrase simple", "Eu me chamo Rui. Me levanto cedo."],
              ["não + pronom + verbe", "après une négation", "Não me lembro."],
              ["você + se + verbe", "dans une question", "Como você se chama?"],
              ["verbe + pronom + infinitif", "avec deux verbes", "Vou te ligar amanhã."],
              ["nós nos levantamos", "nos devant le verbe, sans rien perdre", "Nós nos deitamos às onze."]],
  "exemples": [["Eu me chamo Paulo e sou de Montreal.", "Je m'appelle Paulo et je suis de Montréal."],
               ["Não me lembro do nome dele.", "Je ne me souviens pas de son nom."],
               ["Você me ajuda com a mala?", "Tu m'aides avec la valise ?"]]},
"falsos-amigos": {"resume": "o apelido, constipado, a propina…",
  "tableau": [["o apelido", "le surnom (le nom de famille : o sobrenome)", "O apelido dele é Zé."],
              ["constipado", "constipé (enrhumé : resfriado)", "Estou resfriado."],
              ["puxar · empurrar", "tirer · pousser", "PUXE (sur une porte) = tirez"],
              ["esquisito", "bizarre (pas exquis)", "Que sabor esquisito!"],
              ["a propina", "le pot-de-vin (pas le pourboire : a gorjeta)", "Ele recusou a propina."],
              ["o talher", "le couvert (pas le tailleur)", "Falta um talher na mesa."]],
  "exemples": [["Estou resfriada, estou com o nariz entupido.", "Je suis enrhumée, j'ai le nez bouché."],
               ["Puxe a porta, não empurre!", "Tirez la porte, ne poussez pas !"],
               ["Meu sobrenome é Martins.", "Mon nom de famille est Martins."]]},
"falsos-amigos-b2": {"resume": "puxar, esquisito, propina, constipado, borracha…",
  "tableau": [["puxar · empurrar", "tirer · pousser", "Puxe a porta."],
              ["esquisito", "bizarre", "Que sabor esquisito!"],
              ["constipado · resfriado", "constipé · enrhumé", "Estou resfriado."],
              ["a propina", "le pot-de-vin", "O fiscal aceitou propina."],
              ["a borracha", "la gomme", "Me empresta a borracha?"],
              ["o apelido · o sobrenome", "le surnom · le nom de famille", "Qual é o seu sobrenome?"],
              ["o largo", "la petite place", "A gente se encontra no largo."]]},
"perfeito-imperfeito": {"lignes": {2: ["estava + gérondif … quando + perfeito", "l'action interrompue",
                                       "Estava dormindo quando você chegou."]}},
"imperativo": {"lignes": {5: ["sente-se · se senta (oral)", "les pronoms", "Sente-se, por favor."]}},
"obrigacao": {"titre": "Ter que, dever, é preciso",
  "lignes": {0: ["ter que + infinitif", "devoir, être obligé de", "Temos que sair às oito."]}},
"perifrases-a2": {"lignes": {4: ["continuar + gérondif", "continuer à", "Continuo estudando à noite."],
                             5: ["andar + gérondif", "ces temps-ci", "Ando aprendendo a tocar violão."]}},
"perifrases-b2": {"titre": "Andar + gérondif, ir + gérondif, vir a, chegar a",
  "lignes": {0: ["andar + gérondif", "ces temps-ci, souvent", "Ando pensando em me mudar."],
             4: ["começar a + infinitif", "se mettre à", "Começou a rir."]}},
"colocacao-pronominal": {"resume": "me dá, não me dê, que me dê, vou te dar",
  "tableau": [["pronom + verbe", "par défaut à l'oral (próclise)", "Me chamo Rui. Se sentem."],
              ["não / nunca + pronom + verbe", "négation", "Não me lembro."],
              ["verbe + pronom + infinitif", "avec deux verbes", "Vou te ligar amanhã."],
              ["verbe-pronom", "l'écrit soigné, en tête de phrase", "Chamo-me Rui."],
              ["infinitif-lo, -la", "après un infinitif, à l'écrit", "Vou comprá-lo amanhã."],
              ["ele, ela (complément)", "à l'oral, au lieu de o, a", "Vi ele ontem."]],
  "exemples": [["Você se lembra do Rui? — Não me lembro dele.", "Tu te souviens de Rui ? — Je ne me souviens pas de lui."],
               ["Quando te vi, não te reconheci.", "Quand je t'ai vu, je ne t'ai pas reconnu."],
               ["A gente se fala amanhã.", "On se parle demain."]]},
"mesoclise": {"resume": "dar-te-ei = te darei : à reconnaître, pas à dire",
  "tableau": [["dar-te-ei → te darei", "je te donnerai", "Te respondo amanhã."],
              ["dir-se-ia → se diria", "on dirait", "Parece que vai chover."],
              ["fá-lo-ei → vou fazer isso", "je le ferai", "Vou fazer isso com todo o prazer."],
              ["vou te dar · vou fazer", "l'équivalent courant", "Vou te responder amanhã."],
              ["realizar-se-á → será realizada", "la langue administrative", "A reunião será realizada às 10h."]],
  "exemples": [["A cerimônia será realizada no salão nobre.", "La cérémonie aura lieu dans la salle d'honneur."],
               ["Seria possível nos enviar o documento?", "Vous serait-il possible de nous envoyer le document ?"],
               ["Se eu soubesse, te diria.", "Si je le savais, je te le dirais."]]},
"participios-duplos": {"titre": "Aceito ou aceitado ? Les participes doubles",
  "lignes": {4: ["ter / ser + aceito, entregue", "court partout", "A proposta foi aceita."]}},
"portugal-brasil": {"resume": "reconnaître le portugais du Portugal",
  "tableau": [["estou lendo · estou a ler", "la forme progressive (BR · PT)", ""],
              ["me chamo · chamo-me", "le pronom (BR · PT)", ""],
              ["meu livro · o meu livro", "l'article devant le possessif (BR · PT)", ""],
              ["trem · comboio", "le train (BR · PT)", ""],
              ["café da manhã · pequeno-almoço", "le petit-déjeuner (BR · PT)", ""],
              ["econômico · económico · fato · facto", "l'orthographe (BR · PT)", ""]],
  "exemples": [["(BR) Estou bebendo um suco no trem. = (PT) Estou a beber um sumo no comboio.", "Je bois un jus dans le train."],
               ["(BR) Você pegou o ônibus? = (PT) Apanhaste o autocarro?", "Tu as pris le bus ?"],
               ["(BR) Meu time ganhou! = (PT) A minha equipa ganhou!", "Mon équipe a gagné !"]]},
}
