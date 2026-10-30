# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » du portugais, B1 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python portugais/outils/construire.py (niveaux.py).
BROUILLON : a faire relire par un lusophone du Portugal.
"""

TEMPS = [
{
"id": "temps-conjuntivo-presente", "titre": "Presente do conjuntivo — que eu faça",
"texte": "Après un souhait, une demande, un doute, un sentiment (<b>quero que, espero que, duvido que, é pena que</b>), après <b>talvez, oxalá, embora, para que, antes que</b>. On part de la 1re personne du présent : <b>faço → faça</b>, <b>tenho → tenha</b>. Irréguliers : seja, esteja, vá, dê, haja, saiba, queira.<br><em>Espero que venhas. Talvez chova.</em> (J'espère que tu viendras. Il pleuvra peut-être.)",
"serie": "tempsConjuntivoPresentePtExercises", "kicker": "Le conjuntivo présent",
"questions": """
Quero que tu ___ (fazer) os trabalhos de casa. | faças | fazes / fizeres | Je veux que tu fasses tes devoirs. | Faço → faça, faças.
Espero que ___ (estar) tudo bem. | esteja | está / estiver | J'espère que tout va bien. | Estar → esteja.
Talvez eles ___ (vir) amanhã. | venham | vêm / vierem | Peut-être qu'ils viendront demain. | Venho → venha, venham.
É pena que não ___ (poder) ficar. | possas | podes / puderes | C'est dommage que tu ne puisses pas rester. | Posso → possa, possas.
Duvido que ela ___ (saber) a resposta. | saiba | sabe / souber | Je doute qu'elle sache la réponse. | Saber → saiba.
Oxalá ___ (fazer) sol amanhã! | faça | faz / fizer | Pourvu qu'il fasse soleil demain ! | Oxalá + conjuntivo.
Peço-lhe que ___ (ser) breve. | seja | é / for | Je vous demande d'être bref. | Ser → seja.
Embora ___ (ter) pouco tempo, vou ajudar-te. | tenha | tenho / tiver | Bien que j'aie peu de temps, je vais t'aider. | Embora + conjuntivo.
Fala alto para que todos te ___ (ouvir). | ouçam | ouvem / ouvirem | Parle fort pour que tous t'entendent. | Ouço → ouça, ouçam.
É melhor que nós ___ (ir) já. | vamos | iremos / formos | Il vaut mieux que nous partions tout de suite. | Ir → vá, vamos.
Não acredito que ele ___ (dizer) isso. | diga | diz / disser | Je ne crois pas qu'il dise ça. | Digo → diga.
Espero que me ___ (dar) uma resposta hoje. | dês | dás / deres | J'espère que tu me donneras une réponse aujourd'hui. | Dar → dê, dês.
Antes que ___ (chover), vamos para casa. | chova | chove / chover | Avant qu'il pleuve, rentrons. | Antes que + conjuntivo.
Prefiro que vocês ___ (chegar) cedo. | cheguem | chegam / chegarem | Je préfère que vous arriviez tôt. | Chegar → chegue (g → gu).
É importante que ___ (haver) água para todos. | haja | há / houver | Il est important qu'il y ait de l'eau pour tous. | Haver → haja.
Quero que ___ (conhecer) os meus pais. | conheças | conheces / conheceres | Je veux que tu connaisses mes parents. | Conheço → conheça.
Não quero que te ___ (preocupar). | preocupes | preocupas / preocupares | Je ne veux pas que tu t'inquiètes. | -ar → -e : preocupes.
Caso ___ (precisar) de alguma coisa, liga-me. | precises | precisas / precisares | Au cas où tu aurais besoin de quelque chose, appelle-moi. | Caso + conjuntivo présent.
"""
},
{
"id": "temps-futuro-conjuntivo", "titre": "Futuro do conjuntivo — quando puderes",
"texte": "Après <b>quando, se, assim que, logo que, enquanto, sempre que, como, onde, quem</b>, pour une action à venir : <b>Quando chegares, liga-me</b>. Sur le perfeito, 3e personne du pluriel sans <b>-am</b> : <b>fizeram → fizer</b>, <b>tiveram → tiver</b>, <b>foram → for</b>, <b>puderam → puder</b>. Pour les réguliers, il ressemble à l'infinitif.<br><em>Se puderes, vem. Faz como quiseres.</em> (Si tu peux, viens. Fais comme tu veux.)",
"serie": "tempsFuturoConjuntivoPtExercises", "kicker": "Quando puderes…",
"questions": """
Quando ___ (chegar) a Lisboa, telefona-me. | chegares | chegas / chegarás | Quand tu arriveras à Lisbonne, téléphone-moi. | Régulier : chegar, chegares.
Se ___ (ter) tempo, passo por tua casa. | tiver | tenho / tenha | Si j'ai le temps, je passe chez toi. | Ter → tiver.
Assim que ___ (saber) alguma coisa, aviso-te. | souber | sei / saiba | Dès que je saurai quelque chose, je te préviens. | Saber → souber.
Se vocês ___ (querer), podem vir connosco. | quiserem | querem / queiram | Si vous voulez, vous pouvez venir avec nous. | Querer → quiser, quiserem.
Quando ___ (ir) ao Porto, prova a francesinha. | fores | vais / vás | Quand tu iras à Porto, goûte la francesinha. | Ir → for, fores.
Se ___ (fazer) frio, levamos casacos. | fizer | faz / faça | S'il fait froid, nous prendrons des manteaux. | Fazer → fizer.
Logo que ___ (acabar) o curso, vou trabalhar. | acabar | acabo / acabe | Dès que j'aurai fini mes études, je vais travailler. | Régulier : acabar.
Se ele ___ (vir), diz-lhe que já saí. | vier | vir / vem | S'il vient, dis-lui que je suis déjà parti. | Vir → vier.
Quando o ___ (ver), dá-lhe um abraço. | vires | veres / vieres | Quand tu le verras, embrasse-le. | Ver → vir, vires.
Enquanto ___ (estar) em Portugal, aproveita! | estiveres | estás / estejas | Tant que tu seras au Portugal, profites-en ! | Estar → estiver, estiveres.
Quem ___ (chegar) primeiro, abre a porta. | chegar | chega / chegue | Celui qui arrivera le premier ouvrira la porte. | Quem + futur : chegar.
Se ___ (poder), ajuda-me amanhã. | puderes | podes / possas | Si tu peux, aide-moi demain. | Poder → puder, puderes.
Faz como ___ (achar) melhor. | achares | achas / aches | Fais comme tu penses que c'est le mieux. | Como + futur : achares.
Sempre que ___ (precisar), estou aqui. | precisares | precisas / precises | Chaque fois que tu en auras besoin, je suis là. | Sempre que + futur.
Se ___ (dizer) que sim, ficamos contentes. | disseres | dizes / digas | Si tu dis oui, nous serons contents. | Dizer → disser, disseres.
Quando nós ___ (ser) velhos, vamos viver no campo. | formos | somos / sejamos | Quand nous serons vieux, nous irons vivre à la campagne. | Ser → for, formos.
Se ___ (haver) algum problema, avisem. | houver | há / haja | S'il y a un problème, prévenez. | Haver → houver.
"""
},
{
"id": "temps-condicional", "titre": "Condicional — faria, gostaria",
"texte": "Politesse, hypothèse, futur dans le passé. Infinitif + <b>-ia, -ias, -ia, -íamos, -iam</b> ; radicaux courts : faria, diria, traria. À l'oral, au Portugal, l'imperfeito le remplace souvent : <b>gostava</b>, <b>podia</b>.<br><em>Gostaria de reservar. Disse que viria.</em> (J'aimerais réserver. Il a dit qu'il viendrait.)",
"serie": "tempsCondicionalPtExercises", "kicker": "Le conditionnel",
"questions": """
Eu ___ (gostar) de marcar uma consulta. | gostaria | gostarei / gostei | J'aimerais prendre rendez-vous. | Politesse : gostaria.
O que ___ (fazer) tu no meu lugar? | farias | fazerias / fazias-te | Que ferais-tu à ma place ? | Fazer → faria, farias.
Ele disse que ___ (vir) mais tarde. | viria | virá / venha | Il a dit qu'il viendrait plus tard. | Futur dans le passé.
Se tivesse dinheiro, ___ (comprar) uma casa. | compraria | comprarei / compre | Si j'avais de l'argent, j'achèterais une maison. | Hypothèse : conditionnel.
___ (poder) dizer-me as horas? | Poderia | Poderá / Pôde | Pourriez-vous me dire l'heure ? | Politesse : poderia.
Eu não ___ (dizer) isso ao chefe. | diria | dizeria / direi | Moi, je ne dirais pas ça au patron. | Dizer → diria.
Nós ___ (preferir) ficar em casa. | preferiríamos | preferimos / preferiremos | Nous préférerions rester à la maison. | Nós : -íamos.
Prometeram que ___ (trazer) o bolo. | trariam | trazeriam / trarão | Ils ont promis qu'ils apporteraient le gâteau. | Trazer → traria.
Sem ti, eu não ___ (conseguir). | conseguiria | conseguirei / consegui | Sans toi, je n'y arriverais pas. | Hypothèse : conseguiria.
___ (ser) melhor esperar. | Seria | Será / Foi | Il vaudrait mieux attendre. | Ser → seria.
Quanto ___ (custar) uma viagem aos Açores? | custaria | custará / custou | Combien coûterait un voyage aux Açores ? | Conditionnel : custaria.
Eles ___ (ficar) contentes com a notícia. | ficariam | ficarão / ficaram | Ils seraient contents de la nouvelle. | Eles : -iam.
(oral) Eu ___ (querer) um galão, por favor. | queria | quereria-me / quis | Je voudrais un galão, s'il vous plaît. | À l'oral : l'imperfeito de politesse.
Ela achava que ___ (haver) lugares. | haveria | haverá / houve | Elle pensait qu'il y aurait des places. | Futur dans le passé : haveria.
"""
},
{
"id": "temps-mais-que-perfeito", "titre": "Mais-que-perfeito — tinha feito",
"texte": "Le passé avant le passé : <b>tinha</b> + participe (<b>tinha feito, tinha visto, tinha saído</b>). Toujours <b>ter</b>, jamais ser. Participes courts : feito, dito, visto, posto, aberto, escrito, vindo, pago, ganho, gasto, aceite.<br><em>Quando cheguei, já tinham jantado.</em> (Quand je suis arrivé, ils avaient déjà dîné.)",
"serie": "tempsMaisQuePerfeitoPtExercises", "kicker": "Le mais-que-perfeito",
"questions": """
Quando chegámos, o filme já ___ (começar). | tinha começado | começou / começava | Quand nous sommes arrivés, le film avait déjà commencé. | Tinha + participe.
Eu nunca ___ (ver) o mar. | tinha visto | vi-o / tinha vido | Je n'avais jamais vu la mer. | Ver → visto.
Ela disse que ___ (fazer) o jantar. | tinha feito | fazia / fez-o | Elle a dit qu'elle avait fait le dîner. | Fazer → feito.
Eles já ___ (sair) quando telefonaste. | tinham saído | saíram / tinham-se saído | Ils étaient déjà partis quand tu as téléphoné. | Tinham + participe, pas de ser.
Percebi que ___ (esquecer-se) da carteira. | me tinha esquecido | tinha-me esquecida / esqueci-me | J'ai compris que j'avais oublié mon portefeuille. | Après que : me tinha esquecido.
Nós ___ (pagar) a conta antes de sair. | tínhamos pago | tínhamos pagado-a / pagámos-a | Nous avions payé l'addition avant de partir. | Pagar → pago.
Ninguém me ___ (dizer) nada. | tinha dito | disse-me / tinha dizido | Personne ne m'avait rien dit. | Dizer → dito.
A loja ainda não ___ (abrir). | tinha aberto | abriu-se / tinha abrido | Le magasin n'avait pas encore ouvert. | Abrir → aberto.
Contou-me que ___ (ganhar) o concurso. | tinha ganho | ganhou-o / tinha ganhou | Il m'a raconté qu'il avait gagné le concours. | Ganhar → ganho.
Quando acordei, já ___ (parar) de chover. | tinha parado | parou / parava | Quand je me suis réveillé, il avait déjà cessé de pleuvoir. | Tinha parado.
Eu já ___ (ler) esse livro. | tinha lido | li-o / tinha leído | J'avais déjà lu ce livre. | Ler → lido.
Ela ___ (pôr) a mesa antes de os convidados chegarem. | tinha posto | pôs-a / tinha ponhado | Elle avait mis la table avant que les invités arrivent. | Pôr → posto.
Eles ___ (vir) de propósito para a festa. | tinham vindo | vieram-se / tinham vido | Ils étaient venus exprès pour la fête. | Vir → vindo.
O professor ___ (aceitar) o trabalho. | tinha aceite | aceitou-o / tinha aceito | Le professeur avait accepté le travail. | Au Portugal : aceite.
"""
},
]
