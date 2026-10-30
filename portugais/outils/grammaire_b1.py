# -*- coding: utf-8 -*-
"""Les fiches de grammaire B1 du portugais (du Portugal), en francais, et leurs
series. SOURCE : on corrige ici, puis python portugais/outils/construire.py.
Meme format que grammaire_a1.py. BROUILLON : a faire relire par un lusophone.
"""

FICHES = [
{
"id": "conjuntivo-presente", "titre": "Le conjuntivo présent : espero que venhas", "resume": "après un souhait, un doute, un sentiment",
"regle": "Le <b>presente do conjuntivo</b> (subjonctif présent) suit les verbes de souhait, de demande, de doute ou de sentiment quand le sujet change : <b>Quero que venhas</b>, <b>Duvido que ele saiba</b>, <b>Tenho medo que chova</b>. Formation : la 1re personne du présent, sans le <b>-o</b>, plus <b>-e</b> (verbes en -ar) ou <b>-a</b> (-er, -ir) : <b>falo → fale</b>, <b>faço → faça</b>, <b>tenho → tenha</b>. Sept irréguliers : <b>ser</b> (seja), <b>estar</b> (esteja), <b>ir</b> (vá), <b>dar</b> (dê), <b>saber</b> (saiba), <b>querer</b> (queira), <b>haver</b> (haja).",
"tableau": [
 ["falar → fale, fales, fale, falemos, falem", "que je parle…", "Espero que fales com ela."],
 ["fazer (faço) → faça, faças, faça…", "que je fasse…", "Quero que faças isso hoje."],
 ["ter (tenho) → tenha · vir (venho) → venha", "que j'aie · que je vienne", "Espero que tenhas razão."],
 ["ser → seja · estar → esteja · ir → vá", "les irréguliers", "Oxalá seja verdade!"],
 ["querer que, pedir que, esperar que", "le souhait, la demande", "Peço-te que esperes."],
 ["duvidar que, não acreditar que", "le doute", "Não acredito que ele venha."],
],
"exemples": [
 ["Os meus pais querem que eu estude medicina.", "Mes parents veulent que j'étudie la médecine."],
 ["Espero que gostes do presente.", "J'espère que le cadeau te plaira."],
 ["Talvez ela chegue mais tarde.", "Peut-être qu'elle arrivera plus tard."],
],
"attention": "Si le sujet ne change pas, on garde l'infinitif : <b>Quero ir</b> (je veux y aller), mais <b>Quero que tu vás</b>. Et <b>acho que</b>, <b>penso que</b> (je pense que) prennent l'indicatif : <b>Acho que ele vem</b> ; à la forme négative, le conjuntivo : <b>Não acho que ele venha</b>.",
"serie": "conjuntivoPresentePtExercises", "kicker": "Le conjuntivo présent",
"questions": """
Espero que ___ boa viagem. | tenhas | tens / terás | J'espère que tu feras bon voyage. | Esperar que + conjuntivo : tenho → tenhas.
Quero que tu ___ comigo ao médico. | venhas | vens / vir | Je veux que tu viennes avec moi chez le médecin. | Querer que + conjuntivo : venho → venhas.
Duvido que ele ___ a verdade. | saiba | sabe / sabia | Je doute qu'il sache la vérité. | Le doute : conjuntivo ; saber → saiba.
Talvez ___ amanhã. | chova | chove / choverá | Peut-être qu'il pleuvra demain. | Talvez + conjuntivo.
Peço-te que ___ a porta quando saíres. | feches | fechas / fechares | Je te demande de fermer la porte quand tu sortiras. | Pedir que + conjuntivo : feches.
Oxalá ___ sol no fim de semana! | esteja | está / estará | Pourvu qu'il fasse soleil ce week-end ! | Oxalá + conjuntivo ; estar → esteja.
Acho que ele ___ razão. | tem | tenha / tivesse | Je pense qu'il a raison. | Achar que, à l'affirmatif : indicatif.
Não acho que ele ___ razão. | tenha | tem / terá | Je ne pense pas qu'il ait raison. | Não achar que : conjuntivo.
É importante que vocês ___ cedo. | cheguem | chegam / chegarem | Il est important que vous arriviez tôt. | É importante que + conjuntivo ; chegar → cheguem.
Os médicos aconselham que se ___ mais água. | beba | bebe / beber | Les médecins conseillent de boire davantage d'eau. | Aconselhar que + conjuntivo.
Tenho medo que o voo ___ atrasado. | esteja | está / estiver | J'ai peur que le vol soit en retard. | La peur : conjuntivo.
Quero ___ ao concerto. | ir | que vá / vá | Je veux aller au concert. | Même sujet : infinitif.
Ela não quer que nós ___ embora. | vamos | fomos / iremos | Elle ne veut pas que nous partions. | Ir au conjuntivo : vá, vás, vá, vamos, vão.
Espero que me ___ uma resposta hoje. | deem | dão / darem | J'espère qu'ils me donneront une réponse aujourd'hui. | Dar au conjuntivo : dê, deem (sans accent, AO 1990).
"""
},
{
"id": "conjuntivo-expressoes", "titre": "Embora, para que, antes que : le conjuntivo après une conjonction", "resume": "bien que, pour que, avant que, à condition que",
"regle": "Certaines conjonctions exigent toujours le conjuntivo : <b>embora</b> (bien que), <b>para que</b> (pour que), <b>antes que</b> (avant que), <b>sem que</b> (sans que), <b>a não ser que</b> / <b>a menos que</b> (à moins que), <b>desde que</b> (pourvu que, à condition que), <b>caso</b> (au cas où), <b>até que</b> (jusqu'à ce que). Les expressions impersonnelles aussi : <b>é possível que</b>, <b>é provável que</b>, <b>é bom que</b>, <b>é pena que</b>.",
"tableau": [
 ["embora + conjuntivo", "bien que", "Embora esteja cansado, vou sair."],
 ["para que · a fim de que", "pour que", "Falo devagar para que percebas."],
 ["antes que · até que", "avant que · jusqu'à ce que", "Vamos antes que comece a chover."],
 ["a não ser que · a menos que", "à moins que", "Vou a pé, a não ser que chova."],
 ["desde que · contanto que", "à condition que", "Podes ir, desde que voltes cedo."],
 ["caso + conjuntivo", "au cas où, si jamais", "Caso precises, liga-me."],
 ["é possível que · é pena que", "il est possible que · c'est dommage que", "É pena que não possas vir."],
],
"exemples": [
 ["Embora o hotel seja caro, vale a pena.", "Bien que l'hôtel soit cher, ça vaut la peine."],
 ["Deixo-te a chave para que possas entrar.", "Je te laisse la clé pour que tu puisses entrer."],
 ["Caso haja algum problema, avise-me.", "Au cas où il y aurait un problème, prévenez-moi."],
],
"attention": "<b>Desde que</b> a deux sens : « depuis que » avec l'indicatif (<b>Desde que chegou, não parou</b>) et « à condition que » avec le conjuntivo (<b>Desde que chegues a horas</b>). Et <b>porque</b> (parce que) prend l'indicatif.",
"serie": "conjuntivoExpressoesPtExercises", "kicker": "Bien que, pour que…",
"questions": """
Embora ___ frio, vamos à praia. | esteja | está / estava | Bien qu'il fasse froid, nous allons à la plage. | Embora + conjuntivo.
Falo devagar para que tu ___. | percebas | percebes / perceberes | Je parle lentement pour que tu comprennes. | Para que + conjuntivo.
Vamos sair antes que ___ a chover. | comece | começa / começar | Partons avant qu'il commence à pleuvoir. | Antes que + conjuntivo ; começar → comece.
Podes usar o carro, desde que o ___ amanhã. | devolvas | devolves / devolverás | Tu peux prendre la voiture, à condition de la rendre demain. | Desde que (condition) + conjuntivo.
Caso ___ alguma dúvida, telefone-me. | tenha | tem / tiver | Au cas où vous auriez une question, téléphonez-moi. | Caso + conjuntivo présent.
Vou de bicicleta, a não ser que ___. | chova | chove / choverá | J'y vais à vélo, à moins qu'il pleuve. | A não ser que + conjuntivo.
É pena que não ___ ficar mais tempo. | possas | podes / poderes | C'est dommage que tu ne puisses pas rester plus longtemps. | É pena que + conjuntivo ; poder → possas.
É provável que o comboio ___ atrasado. | venha | vem / vinha | Il est probable que le train arrive en retard. | É provável que + conjuntivo.
Saiu sem que ninguém o ___. | visse | vê / viu | Il est sorti sans que personne ne le voie. | Sem que au passé : conjuntivo imperfeito (visse).
Desde que ___ em Lisboa, ando sempre a pé. | moro | more / morar | Depuis que j'habite à Lisbonne, je marche toujours. | Desde que (depuis que) : indicatif.
Espera aqui até que eu ___. | volte | volto / voltar | Attends ici jusqu'à ce que je revienne. | Até que + conjuntivo.
Não fui à festa porque ___ doente. | estava | estivesse / esteja | Je ne suis pas allé à la fête parce que j'étais malade. | Porque : indicatif.
É possível que eles já ___ saído. | tenham | têm / tinham | Il est possible qu'ils soient déjà partis. | É possível que + conjuntivo composto (tenham saído).
"""
},
{
"id": "futuro-conjuntivo", "titre": "Le futur du subjonctif : quando chegares, se puderes", "resume": "un temps que le français n'a pas",
"regle": "Le <b>futuro do conjuntivo</b> s'emploie après <b>quando</b>, <b>se</b>, <b>assim que</b>, <b>logo que</b>, <b>enquanto</b>, <b>sempre que</b>, <b>como</b>, <b>onde</b>, <b>quem</b>, <b>o que</b>, pour une action future : <b>Quando chegares, telefona-me</b> (quand tu arriveras…), <b>Se puderes, vem</b> (si tu peux…). Le français met un futur ou un présent ; le portugais, ce temps. On le forme sur le perfeito, 3e personne du pluriel, sans <b>-am</b> : <b>falaram → falar, falares, falar, falarmos, falarem</b> ; <b>fizeram → fizer</b> ; <b>tiveram → tiver</b> ; <b>foram → for</b>.",
"tableau": [
 ["falar → falar, falares, falar, falarmos, falarem", "réguliers : comme l'infinitif", "Quando falares com ele, diz-lhe."],
 ["fazer (fizeram) → fizer, fizeres…", "", "Se fizer bom tempo, vamos à praia."],
 ["ter → tiver · estar → estiver · poder → puder", "", "Se tiveres tempo, passa cá."],
 ["ser / ir → for, fores, for, formos, forem", "", "Quando fores a Lisboa, avisa."],
 ["querer → quiser · saber → souber · vir → vier", "", "Se quiseres, posso ajudar."],
 ["ver → vir · pôr → puser · dizer → disser", "", "Quando o vires, dá-lhe um abraço."],
],
"exemples": [
 ["Assim que souber alguma coisa, digo-te.", "Dès que je saurai quelque chose, je te le dirai."],
 ["Se chover, ficamos em casa.", "S'il pleut, nous restons à la maison."],
 ["Faz como quiseres.", "Fais comme tu veux."],
],
"attention": "Ne pas confondre <b>vir</b> (venir, infinitif) et <b>vir</b> (futur du subjonctif de <b>ver</b>) : <b>Quando o vir, digo-lhe</b> = quand je le verrai. Celui de <b>vir</b> (venir) est <b>vier</b> : <b>Se ele vier</b> (s'il vient).",
"serie": "futuroConjuntivoPtExercises", "kicker": "Quando chegares…",
"questions": """
Quando ___ a casa, telefona-me. | chegares | chegas / chegarás | Quand tu arriveras à la maison, téléphone-moi. | Quando + action future : futuro do conjuntivo.
Se ___ bom tempo, vamos à praia. | fizer | faz / fará | S'il fait beau, nous irons à la plage. | Se + futur : fizer (de fizeram).
Se ___ tempo, passa cá em casa. | tiveres | tens / terás | Si tu as le temps, passe à la maison. | Ter : tiver, tiveres.
Assim que ___ alguma coisa, aviso-te. | souber | sei / saberei | Dès que je saurai quelque chose, je te préviens. | Saber : souber.
Quando ___ a Lisboa, visita o Mosteiro dos Jerónimos. | fores | vais / irás | Quand tu iras à Lisbonne, visite le monastère des Hiéronymites. | Ir : for, fores.
Se vocês ___, podem ficar para jantar. | quiserem | querem / querem-se | Si vous voulez, vous pouvez rester dîner. | Querer : quiser, quiserem.
Quando o ___, dá-lhe os meus parabéns. | vires | veres / vieres | Quand tu le verras, félicite-le de ma part. | Ver : vir, vires (et non « veres »).
Se ele ___, avisa-me. | vier | vir / vem | S'il vient, préviens-moi. | Vir (venir) : vier.
Faz como ___. | quiseres | queres / quererás | Fais comme tu veux. | Como + volonté future : futuro do conjuntivo.
Logo que ___ o trabalho, vou de férias. | acabar | acabo / acabarei | Dès que j'aurai fini le travail, je pars en vacances. | Réguliers : la forme de l'infinitif.
Enquanto ___ aqui, podes usar o meu quarto. | estiveres | estás / estarás | Tant que tu seras ici, tu peux utiliser ma chambre. | Estar : estiver, estiveres.
Quem ___ primeiro, ganha. | chegar | chega / chegará | Celui qui arrivera le premier gagne. | Quem + futur : futuro do conjuntivo.
Se ___ ajudar, diz. | puderes | podes / poderes | Si tu peux aider, dis-le. | Poder : puder, puderes.
Sempre que ___ ao Porto, como uma francesinha. | for | vou / ir | Chaque fois que j'irai à Porto, je mangerai une francesinha. | Sempre que + futur : for.
"""
},
{
"id": "condicional", "titre": "Le conditionnel : gostaria, poderia", "resume": "la politesse, l'hypothèse, le futur dans le passé",
"regle": "Le <b>condicional</b> se forme sur l'infinitif + <b>-ia, -ias, -ia, -íamos, -iam</b> : <b>falaria</b>, <b>comeria</b>. Trois irréguliers, comme au futur : <b>fazer → faria</b>, <b>dizer → diria</b>, <b>trazer → traria</b>. Il sert à la politesse (<b>Gostaria de reservar</b>), à l'hypothèse (<b>Eu não faria isso</b>) et au futur vu du passé (<b>Disse que viria</b>). À l'oral, au Portugal, l'<b>imperfeito</b> le remplace très souvent : <b>Gostava de reservar</b>, <b>Eu não fazia isso</b>.",
"tableau": [
 ["falar → falaria, falarias, falaria, falaríamos, falariam", "je parlerais…", "Falaria com ele, se fosse a ti."],
 ["fazer → faria · dizer → diria · trazer → traria", "les irréguliers", "O que farias no meu lugar?"],
 ["gostaria de · gostava de", "j'aimerais (soutenu · courant)", "Gostava de um quarto com vista."],
 ["poderia · podia", "pourrais-tu ?", "Podia ajudar-me, por favor?"],
 ["se + conjuntivo imperfeito, condicional", "l'hypothèse", "Se tivesse dinheiro, viajaria."],
 ["disse que + condicional", "le futur dans le passé", "Prometeu que ligaria."],
],
"exemples": [
 ["Gostaria de marcar uma consulta para quinta-feira.", "J'aimerais prendre rendez-vous pour jeudi."],
 ["No teu lugar, eu aceitava a proposta.", "À ta place, j'accepterais la proposition."],
 ["Ele disse que chegaria às nove.", "Il a dit qu'il arriverait à neuf heures."],
],
"attention": "Avec un pronom, le conditionnel littéraire coupe le verbe (mésoclise) : <b>dir-te-ia</b>, <b>far-se-ia</b>. À l'oral, on l'évite en prenant l'imperfeito : <b>dizia-te</b>, ou en mettant le pronom devant après un sujet : <b>Eu dir-te-ia</b> → <b>Eu dizia-te</b>.",
"serie": "condicionalPtExercises", "kicker": "Le conditionnel",
"questions": """
___ de reservar uma mesa para quatro. | Gostaria | Gostarei / Gosto-me | J'aimerais réserver une table pour quatre. | La politesse : le conditionnel.
O que ___ no meu lugar? | farias | fazerias / fazias-te | Que ferais-tu à ma place ? | Fazer → faria (radical far-).
Ele prometeu que ___ antes das dez. | chegaria | chegará / chegue | Il a promis qu'il arriverait avant dix heures. | Le futur dans le passé : conditionnel.
Se tivesse mais tempo, ___ mais. | leria | lerei / leio | Si j'avais plus de temps, je lirais davantage. | Hypothèse : se + conjuntivo imperfeito, conditionnel.
___ abrir a janela, por favor? | Podia | Pode-se / Podes-se | Vous pourriez ouvrir la fenêtre, s'il vous plaît ? | Politesse à l'oral : l'imperfeito (podia).
Eu não ___ isso, é perigoso. | faria | farei / faça | Moi, je ne ferais pas ça, c'est dangereux. | Hypothèse : conditionnel.
Disseram que ___ os documentos amanhã. | trariam | trazeriam / trarão | Ils ont dit qu'ils apporteraient les documents demain. | Trazer → traria (radical trar-).
Nós ___ de ir, mas não podemos. | gostávamos | gostámos / gostaremos | Nous aimerions y aller, mais nous ne pouvons pas. | L'imperfeito à la place du conditionnel (oral).
Eu ___-te a verdade se soubesse. | diria | direi / dizia-se | Je te dirais la vérité si je la savais. | Dizer → diria ; avec pronom, l'oral dit aussi « dizia-te ».
Quanto ___ um quarto duplo? | custaria | custará / custe | Combien coûterait une chambre double ? | Conditionnel de politesse.
A Ana disse que ___ ajudar-nos. | poderia | poderá / possa | Ana a dit qu'elle pourrait nous aider. | Futur dans le passé.
Seria melhor ___ mais cedo. | sairmos | saímos / sair-nos | Il vaudrait mieux que nous partions plus tôt. | Seria melhor + infinitif personnel (sairmos).
"""
},
{
"id": "mais-que-perfeito", "titre": "Le mais-que-perfeito : tinha feito", "resume": "le passé avant le passé",
"regle": "Pour une action antérieure à une autre action passée : <b>tinha</b> (imperfeito de ter) + participe passé : <b>Quando cheguei, o comboio já tinha partido</b>. Le participe ne s'accorde pas. Participes irréguliers à connaître : <b>feito</b> (fazer), <b>dito</b> (dizer), <b>escrito</b>, <b>visto</b> (ver), <b>vindo</b> (vir), <b>posto</b> (pôr), <b>aberto</b>, <b>coberto</b>, <b>ganho</b>, <b>gasto</b>, <b>pago</b>, <b>aceite</b> (au Portugal). La forme simple (<b>falara, fizera</b>) existe, mais seulement à l'écrit littéraire.",
"tableau": [
 ["tinha + participe", "j'avais + participe", "Eu já tinha jantado."],
 ["tinhas · tinha · tínhamos · tinham", "", "Eles tinham saído."],
 ["feito · dito · visto · posto", "participes irréguliers", "Ninguém me tinha dito nada."],
 ["aberto · escrito · vindo", "", "A loja ainda não tinha aberto."],
 ["pago · ganho · gasto · aceite", "les participes courts", "Já tinha pago a conta."],
 ["fizera, dissera", "forme simple, littéraire", "Ele dissera que voltaria."],
],
"exemples": [
 ["Quando chegámos à estação, o comboio já tinha partido.", "Quand nous sommes arrivés à la gare, le train était déjà parti."],
 ["Nunca tinha visto o mar antes daquela viagem.", "Je n'avais jamais vu la mer avant ce voyage."],
 ["Ela disse que tinha perdido as chaves.", "Elle a dit qu'elle avait perdu ses clés."],
],
"attention": "Le portugais n'emploie pas <b>ser</b> comme auxiliaire du passé : « elle était partie » se dit <b>ela tinha partido</b>, jamais « era partida ».",
"serie": "maisQuePerfeitoPtExercises", "kicker": "Le mais-que-perfeito",
"questions": """
Quando cheguei, eles já ___ jantado. | tinham | tiveram / têm | Quand je suis arrivé, ils avaient déjà dîné. | Le passé avant le passé : tinham + participe.
Nunca tinha ___ uma coisa assim. | visto | vido / vista | Je n'avais jamais vu une chose pareille. | Ver → visto ; le participe ne s'accorde pas.
Ela disse que já tinha ___ o trabalho. | feito | fazido / feita | Elle a dit qu'elle avait déjà fait le travail. | Fazer → feito.
O filme já tinha ___ quando entrámos. | começado | começo / começar | Le film avait déjà commencé quand nous sommes entrés. | Participe régulier : começado.
Ninguém me tinha ___ que a reunião era hoje. | dito | dizido / dita | Personne ne m'avait dit que la réunion était aujourd'hui. | Dizer → dito.
Eu já ___ pago a conta quando ele chegou. | tinha | tive / era | J'avais déjà payé l'addition quand il est arrivé. | Tinha + pago.
A loja ainda não tinha ___ quando passámos. | aberto | abrido / aberta | Le magasin n'avait pas encore ouvert quand nous sommes passés. | Abrir → aberto.
Nós ___ saído de casa quando começou a chover. | tínhamos | tivemos / tínhamos-nos | Nous étions sortis de la maison quand il a commencé à pleuvoir. | Tínhamos + participe (pas d'auxiliaire ser).
Ele contou que tinha ___ a lotaria. | ganho | ganhado / ganhou | Il a raconté qu'il avait gagné à la loterie. | Ganhar → ganho (le participe court est le courant).
O professor tinha ___ a proposta. | aceite | aceitado / aceito | Le professeur avait accepté la proposition. | Au Portugal : aceite.
Quando acordei, a minha mãe já tinha ___ a mesa. | posto | ponhado / pusto | Quand je me suis réveillé, ma mère avait déjà mis la table. | Pôr → posto.
Percebi que me tinha ___ das chaves. | esquecido | esquecer / esqueci | J'ai compris que j'avais oublié les clés. | Esquecer-se → tinha-me esquecido / me tinha esquecido (après que).
"""
},
{
"id": "passiva", "titre": "Le passif : foi construído, vendem-se casas", "resume": "ser + participe, et le se passif",
"regle": "Le passif se forme avec <b>ser</b> + participe passé, qui s'accorde avec le sujet : <b>A ponte foi construída em 1966</b>. L'agent se dit avec <b>por</b> (<b>pelo, pela</b>) : <b>O livro foi escrito por Saramago</b>. Pour un état, c'est <b>estar</b> + participe : <b>A porta está fechada</b>. Très courant aussi, le <b>se passif</b> : <b>Vendem-se casas</b> (maisons à vendre), <b>Aluga-se quarto</b>, où le verbe s'accorde avec le nom.",
"tableau": [
 ["ser + participe (accordé)", "être + participe", "A casa foi vendida."],
 ["por / pelo / pela + agent", "par", "Foi pintado por Amadeo."],
 ["estar + participe", "l'état, le résultat", "O museu está fechado à segunda."],
 ["verbe + -se + nom", "on (passif), à vendre", "Vendem-se apartamentos."],
 ["aluga-se · precisa-se", "à louer · on cherche", "Precisa-se de empregado."],
 ["vai ser feito · tem sido feito", "le passif à d'autres temps", "A estrada vai ser arranjada."],
],
"exemples": [
 ["O Mosteiro dos Jerónimos foi construído no século XVI.", "Le monastère des Hiéronymites a été construit au XVIe siècle."],
 ["Os resultados serão publicados amanhã.", "Les résultats seront publiés demain."],
 ["Aqui fala-se português e francês.", "Ici, on parle portugais et français."],
],
"attention": "Avec le <b>se</b> passif, le verbe s'accorde : <b>Vende-se uma casa</b>, mais <b>Vendem-se casas</b>. Et avec une préposition, il reste au singulier : <b>Precisa-se de empregados</b>.",
"serie": "passivaPtExercises", "kicker": "Le passif",
"questions": """
A ponte 25 de Abril foi ___ em 1966. | inaugurada | inaugurado / inaugurou | Le pont du 25 Avril a été inauguré en 1966. | Ser + participe accordé : a ponte → inaugurada.
O livro foi escrito ___ José Saramago. | por | pelo / de | Le livre a été écrit par José Saramago. | L'agent : por (pelo devant o).
Estas casas foram construídas ___ arquiteto famoso. | por um | pelo um / de um | Ces maisons ont été construites par un architecte célèbre. | Por + um : pas de contraction.
O museu ___ fechado às segundas-feiras. | está | é / foi | Le musée est fermé le lundi. | Un état : estar + participe.
___ apartamentos no centro. | Vendem-se | Vende-se / Vendem | Appartements à vendre dans le centre. | Le se passif s'accorde : vendem-se apartamentos.
___ quarto perto da universidade. | Aluga-se | Alugam-se / Aluga | Chambre à louer près de l'université. | Au singulier : aluga-se.
___ de empregados de mesa. | Precisa-se | Precisam-se / Precisa | On recherche des serveurs. | Avec une préposition : toujours au singulier.
Os resultados ___ publicados na próxima semana. | serão | estarão / vão | Les résultats seront publiés la semaine prochaine. | Passif au futur : serão + participe.
A carta foi ___ ontem. | enviada | enviado / enviou | La lettre a été envoyée hier. | Accord au féminin : enviada.
O ladrão foi preso ___ polícia. | pela | pelo / por a | Le voleur a été arrêté par la police. | Por + a = pela.
Aqui ___ muito bem. | come-se | comem-se / se come-se | Ici, on mange très bien. | Le se impersonnel, sans objet : come-se.
A reunião ___ adiada para amanhã. | foi | esteve / era | La réunion a été reportée à demain. | L'action : ser (foi).
"""
},
{
"id": "relativos", "titre": "Les relatifs : que, quem, onde, cujo, o qual", "resume": "qui, que, où, dont, lequel",
"regle": "<b>Que</b> est le relatif passe-partout, pour les personnes et les choses, sujet ou objet : <b>O livro que li</b>, <b>A senhora que mora aqui</b>. <b>Quem</b>, pour une personne après une préposition : <b>A pessoa com quem falei</b>. <b>Onde</b>, pour un lieu : <b>A cidade onde nasci</b>. <b>Cujo, cuja, cujos, cujas</b> (dont le, dont la) s'accorde avec ce qui suit : <b>O amigo cuja casa…</b>. <b>O qual, a qual, os quais</b>, après une préposition longue : <b>A empresa para a qual trabalho</b>.",
"tableau": [
 ["que", "qui, que", "O homem que está ali é o meu tio."],
 ["preposition + quem", "à qui, avec qui (personne)", "O colega com quem trabalho."],
 ["onde · em que", "où", "A rua onde moro é calma."],
 ["cujo, cuja, cujos, cujas", "dont le, dont la", "A aluna cujo pai é médico."],
 ["o qual, a qual, os quais", "lequel, laquelle", "A razão pela qual saí."],
 ["o que", "ce qui, ce que", "Não percebo o que dizes."],
],
"exemples": [
 ["A casa onde cresci já não existe.", "La maison où j'ai grandi n'existe plus."],
 ["É uma escritora cujos livros adoro.", "C'est une écrivaine dont j'adore les livres."],
 ["Não sei com quem ele foi.", "Je ne sais pas avec qui il est parti."],
],
"attention": "La préposition ne reste jamais à la fin : « la fille dont je t'ai parlé » = <b>a rapariga de quem te falei</b> (falar de). Et « dont » ne se traduit pas toujours par cujo : seul « dont le / dont la » (possession) le prend.",
"serie": "relativosPtExercises", "kicker": "Les relatifs",
"questions": """
O livro ___ estou a ler é muito interessante. | que | quem / onde | Le livre que je suis en train de lire est très intéressant. | Que : chose, objet.
A senhora com ___ falei é a diretora. | quem | que / qual | La dame avec qui j'ai parlé est la directrice. | Après une préposition, pour une personne : quem.
A cidade ___ nasci fica no norte. | onde | que / quem | La ville où je suis né se trouve dans le nord. | Un lieu : onde.
É o vizinho ___ filha estuda em Coimbra. | cuja | cujo / que a | C'est le voisin dont la fille étudie à Coimbra. | Cujo s'accorde avec ce qui suit : filha → cuja.
Não percebi ___ ele disse. | o que | que / quem | Je n'ai pas compris ce qu'il a dit. | Ce que : o que.
A empresa para a ___ trabalho é espanhola. | qual | que / quem | L'entreprise pour laquelle je travaille est espagnole. | Après une préposition longue : a qual.
O rapaz ___ ganhou o prémio é meu primo. | que | quem / qual | Le garçon qui a gagné le prix est mon cousin. | Sujet : que.
A rapariga de ___ te falei chega hoje. | quem | que / cuja | La fille dont je t'ai parlé arrive aujourd'hui. | Falar de alguém : de quem.
Os alunos ___ notas foram boas passaram. | cujas | cujos / que as | Les élèves dont les notes ont été bonnes sont passés. | Notas (fém. plur.) → cujas.
Esta é a razão pela ___ não vim. | qual | que / quem | Voilà la raison pour laquelle je ne suis pas venu. | Pela qual.
Tudo ___ precisas está na mala. | de que | que / do que | Tout ce dont tu as besoin est dans la valise. | Precisar de : de que.
O restaurante ___ jantámos era ótimo. | onde | que / quem | Le restaurant où nous avons dîné était excellent. | Un lieu : onde (ou em que).
"""
},
{
"id": "discurso-indireto", "titre": "Le discours indirect : disse que estava cansado", "resume": "rapporter ce qu'on a dit",
"regle": "Pour rapporter des paroles au passé, les temps reculent comme en français : présent → <b>imperfeito</b> (« Estou cansado » → <b>Disse que estava cansado</b>), perfeito → <b>mais-que-perfeito</b> (« Comprei » → <b>Disse que tinha comprado</b>), futur → <b>condicional</b> (« Vou » / « Irei » → <b>Disse que ia</b> / <b>iria</b>), impératif → <b>conjuntivo imperfeito</b> (« Vem! » → <b>Pediu que viesse</b>). Les repères changent aussi : <b>hoje → nesse dia</b>, <b>amanhã → no dia seguinte</b>, <b>aqui → ali</b>.",
"tableau": [
 ["« Estou cansado. » → disse que estava cansado", "présent → imperfeito", ""],
 ["« Comprei pão. » → disse que tinha comprado pão", "perfeito → mais-que-perfeito", ""],
 ["« Vou amanhã. » → disse que ia no dia seguinte", "futur → imperfeito / condicional", ""],
 ["« Fecha a porta! » → pediu-me que fechasse a porta", "impératif → conjuntivo imperfeito", ""],
 ["« Estás bem? » → perguntou se eu estava bem", "question oui/non → se", ""],
 ["hoje → nesse dia · ontem → na véspera", "les repères", ""],
],
"exemples": [
 ["A Maria disse que não podia vir à festa.", "Maria a dit qu'elle ne pouvait pas venir à la fête."],
 ["Perguntaram-me onde eu morava.", "Ils m'ont demandé où j'habitais."],
 ["O médico disse-me que descansasse.", "Le médecin m'a dit de me reposer."],
],
"attention": "Une consigne rapportée prend le conjuntivo, là où le français met « de + infinitif » : <b>Disse-me que esperasse</b> (il m'a dit d'attendre). On peut aussi garder l'infinitif : <b>Disse-me para esperar</b>.",
"serie": "discursoIndiretoPtExercises", "kicker": "Le discours indirect",
"questions": """
« Estou cansado. » → Ele disse que ___ cansado. | estava | está / esteve | Il a dit qu'il était fatigué. | Présent → imperfeito.
« Comprei os bilhetes. » → Ela disse que ___ comprado os bilhetes. | tinha | tem / teria | Elle a dit qu'elle avait acheté les billets. | Perfeito → mais-que-perfeito.
« Vou ao Porto. » → Disse que ___ ao Porto. | ia | vai / foi | Il a dit qu'il allait à Porto. | Présent / futur proche → imperfeito.
« Fecha a janela! » → Pediu-me que ___ a janela. | fechasse | feche / fechava | Il m'a demandé de fermer la fenêtre. | Impératif → conjuntivo imperfeito.
« Estás bem? » → Perguntou ___ eu estava bem. | se | que / como | Il a demandé si j'allais bien. | Question oui / non : se.
« Onde moras? » → Perguntou-me onde eu ___. | morava | moro / morei | Il m'a demandé où j'habitais. | Présent → imperfeito.
« Telefono amanhã. » → Disse que telefonava no dia ___. | seguinte | amanhã / depois | Il a dit qu'il téléphonerait le lendemain. | Amanhã → no dia seguinte.
« Chegarei às oito. » → Disse que ___ às oito. | chegaria | chegará / chegue | Il a dit qu'il arriverait à huit heures. | Futur → conditionnel.
« Não toquem em nada! » → Disse-nos que não ___ em nada. | tocássemos | tocamos / toquemos | Il nous a dit de ne toucher à rien. | Impératif → conjuntivo imperfeito.
« Já jantei. » → Disse que já ___ jantado. | tinha | tem / tinha-se | Il a dit qu'il avait déjà dîné. | Perfeito → mais-que-perfeito.
O médico disse-me ___ descansar uns dias. | para | que / de | Le médecin m'a dit de me reposer quelques jours. | Dizer para + infinitif : la consigne, à l'oral.
« Gosto muito deste sítio. » → Disse que gostava muito ___ sítio. | daquele | deste / desse | Il a dit qu'il aimait beaucoup cet endroit. | Este → aquele, au discours rapporté.
"""
},
{
"id": "infinitivo-pessoal", "titre": "L'infinitif personnel : para fazermos", "resume": "un infinitif qui se conjugue — une spécialité portugaise",
"regle": "Le portugais conjugue son infinitif quand il a son propre sujet : <b>para eu falar</b>, <b>para tu falares</b>, <b>para ele falar</b>, <b>para nós falarmos</b>, <b>para eles falarem</b>. On l'emploie après une préposition (<b>para, sem, antes de, depois de, até, ao</b>) ou une expression impersonnelle (<b>é melhor, é preciso, é importante</b>) quand le sujet diffère ou doit être précisé : <b>É melhor saíres já</b> (il vaut mieux que tu partes tout de suite). Il évite souvent le conjuntivo. Terminaisons : rien, <b>-es</b>, rien, <b>-mos</b>, <b>-em</b>, toujours sur l'infinitif (il est régulier, même pour <b>ser, ter, fazer</b>).",
"tableau": [
 ["para eu fazer · para tu fazeres", "pour que je fasse · que tu fasses", "Trouxe isto para tu veres."],
 ["para ele fazer · para nós fazermos", "", "Esperámos para jantarmos juntos."],
 ["para eles fazerem", "", "Falei alto para eles ouvirem."],
 ["é melhor + infinitif personnel", "il vaut mieux que…", "É melhor irmos embora."],
 ["ao + infinitif personnel", "en (au moment où)", "Ao chegarem, ligaram-me."],
 ["sem + infinitif personnel", "sans que", "Saíram sem pagarem."],
],
"exemples": [
 ["Deixei a chave debaixo do tapete para tu entrares.", "J'ai laissé la clé sous le paillasson pour que tu puisses entrer."],
 ["Antes de saírem, fechem as janelas.", "Avant de sortir, fermez les fenêtres."],
 ["É importante estarmos todos de acordo.", "Il est important que nous soyons tous d'accord."],
],
"attention": "L'infinitif personnel ne se forme pas sur le perfeito : <b>para eles fazerem</b> (de fazer), à ne pas confondre avec le futur du subjonctif <b>se eles fizerem</b>. Pour les verbes réguliers, les deux se ressemblent : <b>falarem</b>.",
"serie": "infinitivoPessoalPtExercises", "kicker": "L'infinitif personnel",
"questions": """
Trouxe o álbum para tu ___ as fotos. | veres | vires / vês | J'ai apporté l'album pour que tu voies les photos. | Infinitif personnel de ver : veres (pas vires).
É melhor ___ já, antes que chova. | irmos | ir-nos / vamos | Il vaut mieux que nous partions tout de suite, avant qu'il pleuve. | É melhor + infinitif personnel : irmos.
Falei devagar para eles ___. | perceberem | percebem / perceberam | J'ai parlé lentement pour qu'ils comprennent. | Para eles + -em.
Ao ___ a casa, os meninos foram logo dormir. | chegarem | chegaram / chegando | En rentrant à la maison, les enfants sont allés se coucher tout de suite. | Ao + infinitif personnel.
Antes de ___, apaguem as luzes. | saírem | sairem / saem | Avant de sortir, éteignez les lumières. | Sair + -em : saírem (accent sur le i).
É importante ___ todos de acordo. | estarmos | estamos / estejamos-nos | Il est important que nous soyons tous d'accord. | Expression impersonnelle + infinitif personnel.
Saíram sem ___ adeus. | dizerem | disserem / dizem | Ils sont partis sans dire au revoir. | Sem + infinitif personnel : dizerem (régulier, sur dizer).
Esperei para nós ___ juntos. | jantarmos | jantamos / jantámos | J'ai attendu pour que nous dînions ensemble. | Para nós + -mos.
Depois de ___ o jantar, fomos passear. | fazermos | fizermos / fazemos | Après avoir fait le dîner, nous sommes allés nous promener. | Depois de + infinitif personnel : fazermos (pas fizermos).
O professor deu-nos tempo para ___ o exercício. | acabarmos | acabamos / acabássemos | Le professeur nous a laissé le temps de finir l'exercice. | Para + -mos.
É preciso tu ___ mais. | descansares | descansas / descanses-te | Il faut que tu te reposes davantage. | É preciso + tu + -es.
Apesar de ___ cansados, continuaram a trabalhar. | estarem | estão / estivessem | Bien qu'ils soient fatigués, ils ont continué à travailler. | Apesar de + infinitif personnel.
"""
},
{
"id": "colocacao-pronominal", "titre": "Avant ou après le verbe ? La place du pronom", "resume": "dá-me, não me dês, que me dês, dar-te-ei",
"regle": "Au Portugal, le pronom se place normalement <b>après</b> le verbe (<b>Dá-me o sal</b>, <b>Levanto-me cedo</b>). Il passe <b>devant</b> (próclise) après : une négation (<b>não, nunca, ninguém, nada</b>), un mot interrogatif (<b>quem, onde, porque</b>), une subordonnée (<b>que, quando, se, porque, embora</b>), et certains adverbes (<b>já, ainda, também, sempre, só, bem, talvez, aqui</b>). Au futur et au conditionnel, sans déclencheur, le pronom se glisse <b>dans</b> le verbe (mésoclise) : <b>dar-te-ei</b>, <b>dir-se-ia</b> — à l'écrit soutenu ; à l'oral, on préfère <b>vou dar-te</b>.",
"tableau": [
 ["verbe + -pronom", "par défaut (ênclise)", "Chamo-me Rui. Sentem-se."],
 ["não / nunca + pronom + verbe", "négation", "Não me lembro."],
 ["que / quando / se + pronom + verbe", "subordonnée", "Acho que se enganou."],
 ["já / também / sempre + pronom + verbe", "certains adverbes", "Também te digo."],
 ["infinitif + -ar + pronom + -ei", "mésoclise (futur, soutenu)", "Telefonar-lhe-ei amanhã."],
 ["vou + infinitif-pronom", "le futur de l'oral", "Vou telefonar-lhe amanhã."],
],
"exemples": [
 ["Lembras-te do Rui? — Não me lembro dele.", "Tu te souviens de Rui ? — Je ne me souviens pas de lui."],
 ["Quando te vi, não te reconheci.", "Quand je t'ai vu, je ne t'ai pas reconnu."],
 ["Dir-se-ia que vai chover.", "On dirait qu'il va pleuvoir."],
],
"attention": "Jamais de pronom en tête de phrase au Portugal : <b>Me dá</b> est brésilien ; on dit <b>Dá-me</b>. Et le sujet seul ne déclenche rien : <b>Ele chama-se Rui</b> (et non « ele se chama »).",
"serie": "colocacaoPronominalPtExercises", "kicker": "La place du pronom",
"questions": """
___ Ana. | Chamo-me | Me chamo / Chamo me | Je m'appelle Ana. | En tête de phrase : le pronom après le verbe.
Não ___ do nome dele. | me lembro | lembro-me / lembro me | Je ne me souviens pas de son nom. | Après não : le pronom devant.
Ele ___ muito cedo. | levanta-se | se levanta / levanta se | Il se lève très tôt. | Le sujet ne déclenche rien : levanta-se.
Acho que ___ enganaste. | te | -te / te- | Je crois que tu t'es trompé. | Après que : le pronom devant (te enganaste).
Já ___ disse que não quero. | te | -te / lhe-te | Je te l'ai déjà dit, je ne veux pas. | Après já : devant.
Amanhã ___ a resposta. | dar-te-ei | te darei / darei-te | Demain, je te donnerai la réponse. | Au futur, sans déclencheur : mésoclise (soutenu).
Quem ___ contou isso? | te | -te / lhe | Qui t'a raconté ça ? | Après un mot interrogatif : devant.
Os convidados ___ à mesa. | sentaram-se | se sentaram / sentaram se | Les invités se sont assis à table. | Le sujet ne déclenche rien : sentaram-se.
Também ___ apetece um café. | me | -me / mim | Moi aussi, j'ai envie d'un café. | Après também : devant.
Nunca ___ vi tão contente. | o | -o / lo | Je ne l'ai jamais vu aussi content. | Après nunca : devant.
Se ___ perguntarem, diz que não sabes. | te | -te / ti | Si on te le demande, dis que tu ne sais pas. | Après se (si) : devant.
___ um pouco, por favor. | Espere-me | Me espere / Espera-me-se | Attendez-moi un peu, s'il vous plaît. | Impératif affirmatif : le pronom après.
Vou ___ amanhã. | telefonar-lhe | lhe telefonar / telefonar-lhe-ei | Je vais lui téléphoner demain. | À l'oral, le futur proche : vou + infinitif-pronom.
"""
},
]
