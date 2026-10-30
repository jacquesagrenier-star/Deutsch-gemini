# -*- coding: utf-8 -*-
"""Les fiches de grammaire B2 du portugais (du Portugal), en francais, et leurs
series. SOURCE : on corrige ici, puis python portugais/outils/construire.py.
Meme format que grammaire_a1.py. BROUILLON : a faire relire par un lusophone.
"""

FICHES = [
{
"id": "conjuntivo-imperfeito", "titre": "Le conjuntivo imparfait : se eu tivesse", "resume": "fosse, tivesse, fizesse — le souhait et l'hypothèse",
"regle": "Le <b>pretérito imperfeito do conjuntivo</b> se forme sur le perfeito, 3e personne du pluriel, sans <b>-ram</b>, plus <b>-sse</b> : <b>falaram → falasse</b>, <b>fizeram → fizesse</b>, <b>foram → fosse</b>. Il suit les mêmes déclencheurs que le conjuntivo présent quand la phrase principale est au passé ou au conditionnel (<b>Queria que viesses</b>), et surtout <b>se</b> dans une hypothèse peu probable : <b>Se eu fosse rico…</b>. Aussi après <b>como se</b> (comme si) et <b>quem me dera que</b> (si seulement).",
"tableau": [
 ["falar (falaram) → falasse, falasses, falasse, falássemos, falassem", "", "Se falasses mais devagar…"],
 ["ter (tiveram) → tivesse · fazer → fizesse", "", "Se tivesse tempo, ia."],
 ["ser / ir (foram) → fosse, fosses, fosse, fôssemos, fossem", "", "Se fosse a ti, aceitava."],
 ["querer → quisesse · poder → pudesse · saber → soubesse", "", "Se soubesse, dizia-te."],
 ["queria que · pedi que + imperfeito do conjuntivo", "concordance au passé", "Pedi-lhe que esperasse."],
 ["como se · quem me dera que", "comme si · si seulement", "Fala como se soubesse tudo."],
],
"exemples": [
 ["Se tivesse mais dinheiro, comprava uma casa no Alentejo.", "Si j'avais plus d'argent, j'achèterais une maison dans l'Alentejo."],
 ["A minha mãe queria que eu estudasse Direito.", "Ma mère voulait que j'étudie le droit."],
 ["Ele fala como se fosse o dono da empresa.", "Il parle comme s'il était le patron de l'entreprise."],
],
"attention": "Après <b>se</b>, trois temps selon la probabilité : <b>Se chover</b> (futuro do conjuntivo, possible), <b>Se chovesse</b> (imperfeito, peu probable ou irréel), <b>Se tivesse chovido</b> (irréel du passé). Jamais de conditionnel après « se ».",
"serie": "conjuntivoImperfeitoPtExercises", "kicker": "Se eu tivesse…",
"questions": """
Se eu ___ rico, viajava pelo mundo. | fosse | for / sou | Si j'étais riche, je voyagerais dans le monde entier. | Hypothèse irréelle : se + imperfeito do conjuntivo.
Se ___ tempo, ajudava-te. | tivesse | tiver / tenho | Si j'avais le temps, je t'aiderais. | Ter → tivesse.
A professora pediu que nós ___ o livro. | lêssemos | lemos / lermos | La professeure nous a demandé de lire le livre. | Concordance au passé : ler → lêssemos.
Queria que tu ___ à minha festa. | viesses | vieres / vens | J'aimerais que tu viennes à ma fête. | Vir → viesse, viesses.
Se ___ a verdade, não estaria tão calmo. | soubesse | souber / sabia | S'il savait la vérité, il ne serait pas si calme. | Saber → soubesse.
Ele fala como se ___ tudo. | soubesse | sabe / saiba | Il parle comme s'il savait tout. | Como se + imperfeito do conjuntivo.
Quem me dera que ___ sexta-feira! | fosse | seja / era | Si seulement on était vendredi ! | Quem me dera que + imperfeito do conjuntivo.
Se nós ___ mais cedo, apanhávamos o comboio. | saíssemos | sairmos / saímos | Si nous partions plus tôt, nous attraperions le train. | Sair → saíssemos.
Era importante que vocês ___ a horas. | chegassem | chegam / cheguem | Il était important que vous arriviez à l'heure. | Principale au passé : chegassem.
Se ___ fazer alguma coisa, fazia. | pudesse | puder / posso | Si je pouvais faire quelque chose, je le ferais. | Poder → pudesse.
Se fosse a ti, não ___ isso. | fazia | faça / fizesse | À ta place, je ne ferais pas ça. | Dans la principale : conditionnel ou imperfeito (oral).
Duvidei que ele ___ razão. | tivesse | tenha / tem | J'ai douté qu'il ait raison. | Doute au passé : tivesse.
Se ___ bom tempo amanhã, vamos à praia. | fizer | fizesse / faz | S'il fait beau demain, nous irons à la plage. | Une possibilité réelle : futuro do conjuntivo.
Embora ___ cansada, foi trabalhar. | estivesse | esteja / estava | Bien qu'elle soit fatiguée, elle est allée travailler. | Embora au passé : estivesse.
"""
},
{
"id": "condicionais-irreais", "titre": "Si j'avais su : se tivesse sabido, teria vindo", "resume": "le regret, l'irréel du passé",
"regle": "Pour l'irréel du passé, <b>se</b> + <b>tivesse</b> + participe, et dans la principale <b>teria</b> + participe (ou, à l'oral, <b>tinha</b> + participe) : <b>Se tivesse sabido, teria vindo</b> / <b>tinha vindo</b>. On peut mélanger les époques : <b>Se tivesse estudado, agora tinha um bom emprego</b> (passé → présent). <b>Se não fosse</b> / <b>se não tivesse sido</b> + nom : sans… (<b>Se não fosses tu, eu perdia-me</b>).",
"tableau": [
 ["se + tivesse + participe", "si j'avais + participe", "Se tivesse visto, tinha avisado."],
 ["teria + participe", "j'aurais + participe", "Teria gostado de ir."],
 ["tinha + participe (oral)", "j'aurais (courant)", "Tinha ficado contente."],
 ["se tivesse… agora + imperfeito", "regret passé, effet présent", "Se tivesse poupado, agora tinha dinheiro."],
 ["se não fosse…", "sans…, n'était…", "Se não fosse a chuva, íamos."],
 ["devia ter + participe", "j'aurais dû", "Devias ter dito."],
],
"exemples": [
 ["Se tivesses telefonado, eu teria ido buscar-te.", "Si tu avais téléphoné, je serais allé te chercher."],
 ["Se não fosse o GPS, ainda andávamos perdidos.", "Sans le GPS, nous serions encore perdus."],
 ["Devia ter saído mais cedo.", "J'aurais dû partir plus tôt."],
],
"attention": "« J'aurais dû, j'aurais pu » se dit <b>devia ter</b>, <b>podia ter</b> + participe (ou <b>deveria ter</b>, <b>poderia ter</b>) : <b>Podias ter avisado!</b> (Tu aurais pu prévenir !).",
"serie": "condicionaisIrreaisPtExercises", "kicker": "Si j'avais su…",
"questions": """
Se ___ sabido, tinha vindo mais cedo. | tivesse | tivera / tinha | Si j'avais su, je serais venu plus tôt. | Irréel du passé : se + tivesse + participe.
Se tivesses estudado, ___ passado no exame. | terias | tinhas-te / tiveste | Si tu avais étudié, tu aurais réussi l'examen. | Principale : teria + participe.
Se não ___ a chuva, tínhamos ido à praia. | fosse | for / era | Sans la pluie, nous serions allés à la plage. | Se não fosse : sans…
Devias ___ dito a verdade. | ter | de ter / tido | Tu aurais dû dire la vérité. | J'aurais dû : devia ter + participe.
Se tivéssemos saído mais cedo, não ___ perdido o avião. | teríamos | tivemos / temos | Si nous étions partis plus tôt, nous n'aurions pas raté l'avion. | Teríamos + participe.
Se ele tivesse poupado, agora ___ dinheiro. | tinha | teria tido / tivesse | S'il avait économisé, il aurait de l'argent maintenant. | Regret passé, effet présent : imperfeito.
Podias ter ___! | avisado | avisar / avisaste | Tu aurais pu prévenir ! | Podia ter + participe.
Se não fosses tu, eu ___-me. | perdia | perdera / perder | Sans toi, je me perdrais. | Se não fosse… + imperfeito.
Se tivesse visto o sinal, ___ travado. | teria | tivesse / tenho | Si j'avais vu le panneau, j'aurais freiné. | Teria + participe.
Ela ___ gostado de ir, mas estava doente. | teria | tivesse / terá | Elle aurait aimé y aller, mais elle était malade. | Le regret : teria gostado.
Se o médico tivesse chegado a tempo, ___ salvo o doente. | tinha | tivesse / tem | Si le médecin était arrivé à temps, il aurait sauvé le malade. | Oral : tinha + participe.
Se eu ___ ouvido, não te teria perguntado. | tivesse | tinha / teria | Si j'avais entendu, je ne t'aurais pas demandé. | Dans la subordonnée : tivesse.
"""
},
{
"id": "tempos-compostos", "titre": "Tenho feito, terei feito, teria feito", "resume": "les temps composés et leurs pièges",
"regle": "Le <b>pretérito perfeito composto</b> (<b>tenho feito</b>) ne correspond PAS au passé composé français : il dit une action répétée ou continue jusqu'à maintenant : <b>Tenho trabalhado muito</b> (je travaille beaucoup ces derniers temps). Pour une action finie, c'est le perfeito simples : <b>Trabalhei muito ontem</b>. Le <b>futuro composto</b> (<b>terei feito</b>) : ce qui sera fini à un moment futur, ou une supposition sur le passé (<b>Terá esquecido?</b> — il aura oublié ?). Le <b>condicional composto</b> (<b>teria feito</b>) : ce qui aurait été, et l'information non confirmée (<b>O ladrão teria fugido de carro</b>).",
"tableau": [
 ["tenho + participe", "ces derniers temps (répété, continu)", "Tem chovido muito."],
 ["perfeito simples", "action finie (= passé composé)", "Choveu muito ontem."],
 ["terei + participe", "futur antérieur", "Às oito já terei acabado."],
 ["terá + participe ?", "supposition sur le passé", "Onde terá ido?"],
 ["teria + participe", "conditionnel passé", "Teria preferido ficar."],
 ["teria + participe (presse)", "information non confirmée", "O suspeito teria fugido."],
],
"exemples": [
 ["Ultimamente tenho dormido mal.", "Ces derniers temps, je dors mal."],
 ["Quando chegares, já terei feito o jantar.", "Quand tu arriveras, j'aurai déjà fait le dîner."],
 ["O Rui não veio. Terá ficado doente?", "Rui n'est pas venu. Il serait tombé malade ?"],
],
"attention": "« J'ai vu ce film » = <b>Vi este filme</b>, jamais « tenho visto este filme » (qui voudrait dire « je regarde ce film régulièrement ces temps-ci »).",
"serie": "temposCompostosPtExercises", "kicker": "Les temps composés",
"questions": """
Ultimamente ___ muito. | tenho trabalhado | trabalhei / tinha trabalhado | Ces derniers temps, je travaille beaucoup. | Répété jusqu'à maintenant : perfeito composto.
Ontem ___ muito. | trabalhei | tenho trabalhado / trabalhava-me | Hier, j'ai beaucoup travaillé. | Action finie : perfeito simples.
Já ___ este filme duas vezes. | vi | tenho visto / via | J'ai déjà vu ce film deux fois. | Action finie, comptée : perfeito simples.
Este mês ___ muito. | tem chovido | choveu-se / tinha chovido | Ce mois-ci, il pleut beaucoup. | Continu jusqu'à maintenant : tem chovido.
Às nove horas já ___ o relatório. | terei acabado | acabarei / tinha acabado | À neuf heures, j'aurai déjà fini le rapport. | Futur antérieur : terei + participe.
O João não atende. ___ adormecido? | Terá | Teria / Tem | João ne répond pas. Il se serait endormi ? | Supposition sur le passé : terá + participe.
Eu ___ preferido ficar em casa. | teria | terei / tinha-me | J'aurais préféré rester à la maison. | Conditionnel passé : teria + participe.
Segundo a polícia, o ladrão ___ fugido de carro. | teria | terá / tem | Selon la police, le voleur se serait enfui en voiture. | Information non confirmée : condicional composto.
Nas últimas semanas ___ pouco. | temos saído | saímos-nos / tínhamos saído | Ces dernières semaines, nous sortons peu. | Perfeito composto : temos saído.
Quando chegares, eles já ___. | terão saído | sairão / tinham saído | Quand tu arriveras, ils seront déjà partis. | Futur antérieur.
Como ___ ela sabido? | terá | teria / tem | Comment l'aura-t-elle su ? | Supposition : terá + participe.
A minha avó ___ melhor desde que começou o tratamento. | tem estado | esteve-se / estivera | Ma grand-mère va mieux depuis qu'elle a commencé le traitement. | Un état qui dure jusqu'à maintenant.
"""
},
{
"id": "conjuntivo-composto", "titre": "Que tenha feito, se tiver feito", "resume": "le conjuntivo des temps composés",
"regle": "Le conjuntivo a ses temps composés, avec <b>ter</b> : <b>tenha feito</b> (passé du conjuntivo : <b>Espero que tenhas gostado</b>), <b>tivesse feito</b> (plus-que-parfait : <b>Se tivesse sabido…</b>), <b>tiver feito</b> (futur antérieur : <b>Quando tiveres acabado, avisa</b>). On les emploie avec les mêmes déclencheurs que les temps simples, quand l'action est déjà accomplie.",
"tableau": [
 ["que + tenha + participe", "que j'aie + participe", "Espero que tenham chegado bem."],
 ["se + tivesse + participe", "si j'avais + participe", "Se tivesse visto, dizia."],
 ["quando / se + tiver + participe", "quand j'aurai + participe", "Quando tiveres lido, empresta-mo."],
 ["talvez + tenha + participe", "peut-être que … a", "Talvez se tenha enganado."],
 ["embora + tenha + participe", "bien que … ait", "Embora tenha estudado, chumbou."],
 ["duvido que + tenha + participe", "je doute que … ait", "Duvido que ele tenha percebido."],
],
"exemples": [
 ["Espero que tenhas gostado do jantar.", "J'espère que le dîner t'a plu."],
 ["Quando tiveres terminado, podes sair.", "Quand tu auras terminé, tu pourras sortir."],
 ["Talvez ele já tenha saído.", "Peut-être qu'il est déjà parti."],
],
"attention": "Comme au mais-que-perfeito, l'auxiliaire est toujours <b>ter</b>, jamais <b>ser</b> : <b>que ela tenha saído</b> (qu'elle soit partie).",
"serie": "conjuntivoCompostoPtExercises", "kicker": "Que tenha feito…",
"questions": """
Espero que ___ gostado da viagem. | tenhas | tens / tiveres | J'espère que le voyage t'a plu. | Espero que + tenha + participe.
Quando ___ acabado, avisa-me. | tiveres | tenhas / tivesses | Quand tu auras fini, préviens-moi. | Quando + futur antérieur : tiver + participe.
Talvez ele já ___ saído. | tenha | tem / tiver | Peut-être qu'il est déjà parti. | Talvez + tenha + participe.
Embora ___ estudado muito, chumbou no exame. | tenha | tem / tivera | Bien qu'il ait beaucoup étudié, il a échoué à l'examen. | Embora + tenha + participe.
Duvido que eles ___ percebido. | tenham | têm / tiverem | Je doute qu'ils aient compris. | Duvidar que + tenha + participe.
Se ___ terminado antes das cinco, vem ter connosco. | tiveres | tenhas / tens | Si tu as terminé avant cinq heures, rejoins-nous. | Se + futur : tiver + participe.
Não acredito que ela ___ dito isso. | tenha | tem / tinha | Je ne crois pas qu'elle ait dit ça. | Não acreditar que + tenha.
É possível que o comboio já ___ partido. | tenha | tem / tiver | Il est possible que le train soit déjà parti. | Auxiliaire ter, jamais ser.
Logo que ___ recebido a resposta, telefono-te. | tiver | tenha / tivesse | Dès que j'aurai reçu la réponse, je te téléphone. | Logo que + tiver + participe.
Lamento que não ___ podido vir. | tenhas | tens / tiveres | Je regrette que tu n'aies pas pu venir. | Lamentar que + tenha.
Se ___ chegado a tempo, teríamos visto o início. | tivéssemos | tivermos / tenhamos | Si nous étions arrivés à temps, nous aurions vu le début. | Se irréel : tivesse + participe.
Quem ___ terminado pode sair. | tiver | tenha / tem | Celui qui aura terminé peut sortir. | Quem + futur antérieur : tiver.
"""
},
{
"id": "concessivas", "titre": "Embora, ainda que, mesmo que, por mais que", "resume": "bien que, même si, avoir beau",
"regle": "Pour concéder : <b>embora</b>, <b>ainda que</b>, <b>mesmo que</b>, <b>se bem que</b>, <b>por mais que</b>, <b>por muito que</b> + conjuntivo : <b>Mesmo que chova, vou</b> (même s'il pleut, j'y vais), <b>Por mais que tente, não consigo</b> (j'ai beau essayer…). Avec un nom ou un infinitif : <b>apesar de</b> (<b>Apesar da chuva</b>, <b>Apesar de estar cansado</b>). Et en début de phrase pour opposer : <b>no entanto</b>, <b>contudo</b>, <b>todavia</b>, <b>mesmo assim</b>.",
"tableau": [
 ["embora · ainda que + conjuntivo", "bien que", "Embora seja tarde, ainda trabalho."],
 ["mesmo que + conjuntivo", "même si", "Mesmo que me peças, não vou."],
 ["por mais que · por muito que + conjuntivo", "avoir beau", "Por mais que estude, esqueço tudo."],
 ["apesar de + nom / infinitif", "malgré, bien que", "Apesar do frio, saímos."],
 ["mesmo assim · ainda assim", "quand même", "Estava cansado, mas mesmo assim foi."],
 ["no entanto · contudo · todavia", "cependant, pourtant", "É caro; no entanto, vale a pena."],
],
"exemples": [
 ["Mesmo que ganhe a lotaria, não deixo de trabalhar.", "Même si je gagne à la loterie, je n'arrête pas de travailler."],
 ["Por mais que corresse, não apanhou o autocarro.", "Il a eu beau courir, il n'a pas attrapé le bus."],
 ["Apesar de ser domingo, a loja estava aberta.", "Bien que ce soit dimanche, le magasin était ouvert."],
],
"attention": "« Même si » se dit <b>mesmo que</b> + conjuntivo, et non « mesmo se ». Et <b>apesar de</b> se contracte : <b>apesar do</b>, <b>apesar da</b>.",
"serie": "concessivasPtExercises", "kicker": "Bien que, même si…",
"questions": """
Mesmo que ___, vamos sair. | chova | chove / chover | Même s'il pleut, nous sortirons. | Mesmo que + conjuntivo présent.
Por mais que ___, não consigo perceber. | tente | tento / tentar | J'ai beau essayer, je n'arrive pas à comprendre. | Por mais que + conjuntivo.
___ do frio, fomos passear. | Apesar | Embora / Mesmo | Malgré le froid, nous sommes allés nous promener. | Apesar de + nom (do frio).
Embora ___ tarde, a loja ainda estava aberta. | fosse | era / for | Bien qu'il soit tard, le magasin était encore ouvert. | Embora au passé : imperfeito do conjuntivo.
Estava doente; ___, foi trabalhar. | mesmo assim | mesmo que / embora | Il était malade ; il est quand même allé travailler. | Quand même : mesmo assim.
O hotel é caro; ___, a localização é ótima. | no entanto | embora / mesmo que | L'hôtel est cher ; cependant, l'emplacement est excellent. | Cependant : no entanto.
Ainda que ___ razão, não devias gritar. | tenhas | tens / tiveres | Même si tu as raison, tu ne devrais pas crier. | Ainda que + conjuntivo.
Apesar de ___ cansados, terminámos o trabalho. | estarmos | estamos / estejamos | Bien que nous soyons fatigués, nous avons fini le travail. | Apesar de + infinitif personnel.
Por muito que ___, nunca chegava a horas. | corresse | corria / correr | Il avait beau courir, il n'arrivait jamais à l'heure. | Por muito que au passé : imperfeito do conjuntivo.
Mesmo que me ___, não te empresto o carro. | peças | pedes / pedires | Même si tu me le demandes, je ne te prête pas la voiture. | Pedir → peças.
O exame era difícil; ___, todos passaram. | contudo | embora / apesar | L'examen était difficile ; pourtant, tous l'ont réussi. | Pourtant : contudo.
Se bem que ___ um pouco cedo, podemos começar. | seja | é / for | Bien qu'il soit un peu tôt, nous pouvons commencer. | Se bem que + conjuntivo.
"""
},
{
"id": "conectores", "titre": "Les connecteurs : aliás, ou seja, portanto, pelo contrário", "resume": "articuler un discours",
"regle": "Pour enchaîner les idées : <b>além disso</b>, <b>aliás</b> (d'ailleurs, du reste), <b>ou seja</b> (c'est-à-dire), <b>isto é</b>, <b>portanto</b>, <b>por isso</b> (donc, c'est pourquoi), <b>pelo contrário</b> (au contraire), <b>em vez de</b> (au lieu de), <b>por um lado… por outro</b>, <b>afinal</b> (finalement, en fin de compte, en fait), <b>de facto</b> (en effet), <b>enfim</b> (bref), <b>quer… quer</b> (soit… soit, que… ou que).",
"tableau": [
 ["além disso · aliás", "en plus · d'ailleurs", "É caro; aliás, nem é bom."],
 ["ou seja · isto é", "c'est-à-dire", "Chego dia 3, ou seja, sexta-feira."],
 ["portanto · por isso · logo", "donc", "Estava a chover, por isso fiquei."],
 ["pelo contrário · em vez de", "au contraire · au lieu de", "Em vez de ires, telefona."],
 ["afinal · de facto · na verdade", "en fin de compte · en effet · en réalité", "Afinal, ele tinha razão."],
 ["quer… quer · tanto… como", "soit… soit · aussi bien… que", "Quer chova quer faça sol, vou."],
],
"exemples": [
 ["Não estou cansado; pelo contrário, sinto-me ótimo.", "Je ne suis pas fatigué ; au contraire, je me sens très bien."],
 ["Afinal, o concerto foi cancelado.", "Finalement, le concert a été annulé."],
 ["Por um lado, gosto da cidade; por outro, é muito cara.", "D'un côté, j'aime la ville ; de l'autre, elle est très chère."],
],
"attention": "<b>Afinal</b> ne veut pas seulement dire « finalement » : il marque souvent une surprise, ce qu'on découvre : <b>Afinal és tu!</b> (Ah, c'est donc toi !). Et <b>de facto</b> s'écrit avec un c au Portugal.",
"serie": "conectoresPtExercises", "kicker": "Les connecteurs",
"questions": """
Estava a chover, ___ ficámos em casa. | por isso | aliás / pelo contrário | Il pleuvait, c'est pourquoi nous sommes restés à la maison. | La conséquence : por isso.
Chego no dia 5, ___, numa sexta-feira. | ou seja | aliás / afinal | J'arrive le 5, c'est-à-dire un vendredi. | C'est-à-dire : ou seja.
Não estou triste; ___, estou muito contente. | pelo contrário | portanto / ou seja | Je ne suis pas triste ; au contraire, je suis très content. | Au contraire : pelo contrário.
O restaurante é caro; ___, a comida nem é boa. | aliás | portanto / em vez de | Le restaurant est cher ; d'ailleurs, la nourriture n'est même pas bonne. | D'ailleurs : aliás.
___ de ires de carro, vai de comboio. | Em vez | Por isso / Aliás | Au lieu d'y aller en voiture, prends le train. | Au lieu de : em vez de.
Pensei que era o Rui, mas ___ era o irmão dele. | afinal | aliás / portanto | Je pensais que c'était Rui, mais en fait c'était son frère. | La découverte : afinal.
___ chova ___ faça sol, o jogo vai realizar-se. | Quer / quer | Ou / ou | Qu'il pleuve ou qu'il fasse beau, le match aura lieu. | Quer… quer + conjuntivo.
Por um lado, o trabalho é interessante; por ___, paga mal. | outro | outra / outro lado | D'un côté, le travail est intéressant ; de l'autre, il paie mal. | Por um lado… por outro.
Disseste que ele vinha e, de ___, chegou às oito. | facto | fato / feito | Tu as dit qu'il viendrait et, en effet, il est arrivé à huit heures. | De facto (au Portugal, avec c).
Penso, ___, existo. | logo | aliás / afinal | Je pense, donc je suis. | Donc (logique) : logo.
Fala ___ inglês como francês. | tanto | quer / tão | Il parle aussi bien anglais que français. | Tanto… como.
Tivemos vários problemas; ___, correu tudo bem. | enfim | aliás / em vez de | Nous avons eu plusieurs problèmes ; bref, tout s'est bien passé. | Bref, pour conclure : enfim.
"""
},
{
"id": "perifrases-b2", "titre": "Andar a, ir + gérondif, vir a, chegar a", "resume": "les périphrases qui nuancent l'action",
"regle": "Le portugais nuance l'action par des périphrases : <b>andar a</b> + infinitif (faire ces temps-ci, de façon répétée : <b>Anda a estudar muito</b>), <b>ir</b> + gérondif (progression lente : <b>A situação vai melhorando</b>), <b>vir a</b> + infinitif (finir par, en arriver à : <b>Veio a saber-se a verdade</b>), <b>chegar a</b> + infinitif (aller jusqu'à : <b>Chegou a chorar</b>), <b>estar para</b> (être sur le point de), <b>pôr-se a</b> (se mettre à), <b>tornar a</b> (refaire), <b>costumar</b> (avoir l'habitude de).",
"tableau": [
 ["andar a + infinitif", "ces temps-ci, souvent", "Ando a pensar mudar de casa."],
 ["ir + gérondif", "peu à peu", "O tempo vai passando."],
 ["vir a + infinitif", "finir par, en venir à", "Veio a ser presidente."],
 ["chegar a + infinitif", "aller jusqu'à", "Cheguei a pensar que não vinhas."],
 ["pôr-se a + infinitif", "se mettre à", "Pôs-se a rir."],
 ["costumar + infinitif", "avoir l'habitude de", "Costumo jantar cedo."],
],
"exemples": [
 ["Ando a ler um livro sobre a história de Lisboa.", "Je lis en ce moment un livre sur l'histoire de Lisbonne."],
 ["Os convidados foram chegando ao longo da tarde.", "Les invités sont arrivés peu à peu au cours de l'après-midi."],
 ["Cheguei a ter medo de não encontrar o caminho.", "J'ai même eu peur de ne pas trouver le chemin."],
],
"attention": "Le gérondif portugais (<b>-ando, -endo, -indo</b>) vit au Portugal surtout avec <b>ir</b> (progression) et en tête de phrase (<b>Chegando a casa, liguei-te</b>). Pour l'action en cours, c'est <b>estar a</b> + infinitif, jamais « estou fazendo ».",
"serie": "perifrasesB2PtExercises", "kicker": "Les périphrases",
"questions": """
Ultimamente ___ a dormir mal. | ando | vou / venho | Ces temps-ci, je dors mal. | Une répétition récente : andar a.
A situação ___ melhorando aos poucos. | vai | anda a / está a | La situation s'améliore peu à peu. | Progression lente : ir + gérondif.
Com o tempo, ___ a perceber que ela tinha razão. | vim | fui / andei | Avec le temps, j'ai fini par comprendre qu'elle avait raison. | Finir par : vir a.
Estava tão nervoso que ___ a chorar. | chegou | veio / andou | Il était si nerveux qu'il est allé jusqu'à pleurer. | Aller jusqu'à : chegar a.
De repente, ela ___ a rir. | pôs-se | foi-se / andou-se | Tout à coup, elle s'est mise à rire. | Se mettre à : pôr-se a.
___ jantar por volta das oito. | Costumamos | Andamos / Vamos a | Nous avons l'habitude de dîner vers huit heures. | Costumar + infinitif.
Os alunos foram ___ um a um. | saindo | sair / a sair | Les élèves sont sortis un par un. | Ir + gérondif.
O telefone ___ a tocar. Não atendes? | está | anda-se / vai | Le téléphone sonne. Tu ne réponds pas ? | L'action en cours : estar a.
Ele ___ a ser um grande escritor. | veio | chegou-se / andou | Il est devenu un grand écrivain. | Vir a ser : finir par devenir.
Cheguei ___ pensar que não vinhas. | a | de / para | J'ai même cru que tu ne viendrais pas. | Chegar a + infinitif.
Ela anda ___ aprender a tocar piano. | a | de / em | Elle apprend en ce moment à jouer du piano. | Andar a + infinitif.
O comboio está ___ partir, corre! | para | a / de | Le train est sur le point de partir, cours ! | Sur le point de : estar para.
"""
},
{
"id": "pronomes-contraidos", "titre": "Mo, to, lho : deux pronoms en un", "resume": "dá-mo, já to disse, deu-lho",
"regle": "Quand un pronom indirect (<b>me, te, lhe, nos, vos, lhes</b>) rencontre un pronom direct (<b>o, a, os, as</b>), ils se soudent : <b>me + o = mo</b>, <b>te + a = ta</b>, <b>lhe + o = lho</b>, <b>nos + os = no-los</b>, <b>lhes + as = lhas</b>. <b>Dá-mo</b> (donne-le-moi), <b>Já to disse</b> (je te l'ai déjà dit), <b>Ela deu-lho</b> (elle le lui a donné). C'est très vivant au Portugal, à l'oral comme à l'écrit ; le Brésil l'a presque perdu.",
"tableau": [
 ["me + o, a, os, as → mo, ma, mos, mas", "me le, me la, me les", "Empresta-mo, por favor."],
 ["te + o… → to, ta, tos, tas", "te le, te la", "Já to disse."],
 ["lhe / lhes + o… → lho, lha, lhos, lhas", "le lui, le leur", "Dei-lho ontem."],
 ["nos + o… → no-lo, no-la", "nous le, nous la", "Explicou-no-lo bem."],
 ["vos + o… → vo-lo, vo-la", "vous le, vous la", "Mando-vo-lo amanhã."],
 ["não mo dês · não lho digas", "devant, après une négation", "Não ma tires!"],
],
"exemples": [
 ["Gostas do livro? Ofereço-to.", "Tu aimes le livre ? Je te l'offre."],
 ["A carta? Já lha entreguei.", "La lettre ? Je la lui ai déjà remise."],
 ["Se precisares das chaves, eu empresto-tas.", "Si tu as besoin des clés, je te les prête."],
],
"attention": "<b>Lho</b> sert pour « le lui » et « le leur » : <b>Dei-lho</b> peut vouloir dire « je le lui ai donné » ou « je le leur ai donné ». Le contexte tranche.",
"serie": "pronomesContraidosPtExercises", "kicker": "Mo, to, lho",
"questions": """
Esse livro é meu. Dá-___! | mo | me o / mo-o | Ce livre est à moi. Donne-le-moi ! | Me + o = mo.
Já ___ disse mil vezes. | to | te o / lho | Je te l'ai déjà dit mille fois. | Te + o = to ; après já, devant le verbe.
A chave? Dei-___ ontem. | lha | lhe a / ta | La clé ? Je la lui ai donnée hier. | Lhe + a = lha.
As fotos? Mando-___ amanhã. | tas | te as / tos | Les photos ? Je te les envoie demain. | Te + as = tas.
Os documentos? Ele entregou-___ ontem. | mos | me os / mas | Les documents ? Il me les a remis hier. | Me + os = mos.
Não ___ digas a ninguém. | lho | lhe o / lo | Ne le lui dis à personne. | Lhe + o = lho ; après não, devant.
A notícia? Contaram-___ ontem. | ma | me a / mo | La nouvelle ? Ils me l'ont racontée hier. | Me + a = ma.
O dinheiro? Devolvo-___ amanhã. | to | te o / lo | L'argent ? Je te le rends demain. | Te + o = to.
O problema? O professor explicou-___ bem. | no-lo | nos o / nolo | Le problème ? Le professeur nous l'a bien expliqué. | Nos + o = no-lo.
Gostas desta camisola? Ofereço-___. | ta | te a / to | Tu aimes ce pull ? Je te l'offre. | Te + a = ta (camisola est féminin).
Os bolos? Os avós deram-___ aos netos. | lhos | lhes os / los | Les gâteaux ? Les grands-parents les ont donnés à leurs petits-enfants. | Lhes + os = lhos.
Quem ___ deu? | to | -to / te o | Qui te l'a donné ? | Après quem, devant : to.
"""
},
{
"id": "se-impessoal", "titre": "Le se impersonnel et le se passif", "resume": "diz-se, vive-se bem, alugam-se quartos",
"regle": "<b>Se</b> + verbe à la 3e personne remplace le « on » français. Sans complément direct, il reste au singulier (<b>se impessoal</b>) : <b>Vive-se bem aqui</b>, <b>Come-se muito bem no Minho</b>, <b>Precisa-se de ajuda</b>. Avec un complément direct, le verbe s'accorde avec lui (<b>se passivo</b>) : <b>Vendem-se casas</b>, <b>Ouvem-se vozes</b>. Il suit la règle de placement : <b>Diz-se</b>, mais <b>Não se diz</b>, <b>Aqui não se fuma</b>.",
"tableau": [
 ["verbe + -se (singulier)", "on (sans complément)", "Trabalha-se muito aqui."],
 ["verbe pluriel + -se + nom pluriel", "on (passif, accordé)", "Fazem-se chaves."],
 ["verbe + -se + de + nom", "toujours au singulier", "Precisa-se de cozinheiros."],
 ["não / aqui / onde + se + verbe", "le se passe devant", "Onde se compra o bilhete?"],
 ["diz-se que · sabe-se que", "on dit que · on sait que", "Diz-se que vai chover."],
 ["a gente (oral, familier)", "on (= nous)", "A gente vê-se amanhã."],
],
"exemples": [
 ["Em Portugal janta-se mais tarde do que em França.", "Au Portugal, on dîne plus tard qu'en France."],
 ["Vendem-se bilhetes na bilheteira.", "Les billets sont vendus au guichet."],
 ["Como se diz isto em português?", "Comment dit-on cela en portugais ?"],
],
"attention": "<b>A gente</b> existe au Portugal, mais il est plus familier qu'au Brésil ; à l'écrit et dans la conversation soignée, on préfère <b>nós</b> ou le <b>se</b> impersonnel.",
"serie": "seImpessoalPtExercises", "kicker": "On : le se",
"questions": """
Aqui ___ muito bem. | come-se | comem-se / se come | Ici, on mange très bien. | Sans complément : singulier, pronom après le verbe.
___ apartamentos no centro. | Vendem-se | Vende-se / Se vendem | Appartements à vendre dans le centre. | Avec un nom pluriel : le verbe s'accorde.
___ de empregados para o verão. | Precisa-se | Precisam-se / Precisa | On recherche des employés pour l'été. | Avec de : toujours au singulier.
Como ___ isto em português? | se diz | diz-se / dizem-se | Comment dit-on cela en portugais ? | Après como, le se passe devant.
Aqui não ___. | se fuma | fuma-se / se fumam | Ici, on ne fume pas. | Après não : devant.
___ que o novo museu vai abrir em maio. | Diz-se | Dizem-se / Se diz | On dit que le nouveau musée va ouvrir en mai. | Diz-se que : singulier.
Nesta loja ___ chaves. | fazem-se | faz-se / se fazem | Dans ce magasin, on fait des clés. | Chaves (pluriel) : fazem-se.
Onde ___ os bilhetes? | se compram | compram-se / se compra | Où achète-t-on les billets ? | Après onde, devant ; accordé avec bilhetes.
Em Portugal ___ tarde. | janta-se | jantam-se / se janta | Au Portugal, on dîne tard. | Sans complément : janta-se.
De manhã ___ os pássaros. | ouvem-se | ouve-se / se ouvem | Le matin, on entend les oiseaux. | Os pássaros : ouvem-se.
Já não ___ cartas como antigamente. | se escrevem | escrevem-se / se escreve | On n'écrit plus de lettres comme autrefois. | Après já não : devant ; accordé avec cartas.
___ bem nesta cidade. | Vive-se | Vivem-se / Se vive | On vit bien dans cette ville. | Vive-se, en tête de phrase.
"""
},
{
"id": "falsos-amigos-b2", "titre": "Les faux amis (2)", "resume": "puxar, esquisito, propina, constipado, borracha…",
"regle": "Certains mots portugais ressemblent à des mots français mais n'ont pas le même sens. <b>Puxar</b> = tirer (sur une porte : <b>Puxe</b>), <b>empurrar</b> = pousser. <b>Esquisito</b> = bizarre (pas « exquis », qui se dit <b>delicioso, requintado</b>). <b>Propina</b> = frais de scolarité (au Portugal). <b>Constipado</b> = enrhumé. <b>Borracha</b> = gomme. <b>Largo</b> = large, et aussi une place (<b>o Largo do Carmo</b>), alors que « large » au sens de « long » n'existe pas. <b>Apelido</b> = nom de famille.",
"tableau": [
 ["puxar · empurrar", "tirer · pousser", "Puxe a porta."],
 ["esquisito", "bizarre", "Que sabor esquisito!"],
 ["constipado · a constipação", "enrhumé · le rhume", "Estou constipado."],
 ["a propina", "les frais de scolarité", "As propinas subiram."],
 ["a borracha", "la gomme", "Empresta-me a borracha?"],
 ["o apelido", "le nom de famille", "Qual é o seu apelido?"],
 ["o largo", "la petite place", "Encontramo-nos no largo."],
],
"exemples": [
 ["Este queijo tem um cheiro esquisito.", "Ce fromage a une drôle d'odeur."],
 ["Estou constipado, não vou trabalhar.", "Je suis enrhumé, je ne vais pas travailler."],
 ["Para abrir, puxe; para fechar, empurre.", "Pour ouvrir, tirez ; pour fermer, poussez."],
],
"attention": "D'autres faux amis fréquents : <b>a data</b> (la date), <b>o talho</b> (la boucherie), <b>a firma</b> (l'entreprise), <b>a cave</b> (le sous-sol), <b>o escritório</b> (le bureau), <b>a secretária</b> (la secrétaire, ET le bureau, le meuble).",
"serie": "falsosAmigosB2PtExercises", "kicker": "Les faux amis",
"questions": """
Para abrir a porta, tem de ___. | puxar | pusar / empurrar | Pour ouvrir la porte, il faut tirer. | Puxar = tirer.
Este iogurte tem um sabor ___. Já passou do prazo? | esquisito | delicioso / requintado | Ce yaourt a un goût bizarre. La date est dépassée ? | Esquisito = bizarre.
Estou ___: tenho o nariz entupido. | constipado | preso / constipação | Je suis enrhumé : j'ai le nez bouché. | Constipado = enrhumé.
Na universidade pública as ___ são baixas. | propinas | gorjetas / pontas | À l'université publique, les frais de scolarité sont bas. | A propina = les frais de scolarité.
Enganei-me na palavra. Tens uma ___? | borracha | goma / apagadora | Je me suis trompé de mot. Tu as une gomme ? | A borracha = la gomme.
Qual é o seu ___? — Silva. | apelido | sobrenome / alcunha | Quel est votre nom de famille ? — Silva. | Au Portugal : o apelido.
Comprei carne no ___. | talho | açougue / carniceria | J'ai acheté de la viande à la boucherie. | Au Portugal : o talho.
Deixei os papéis em cima da ___. | secretária | escritório / mesa de escritório | J'ai laissé les papiers sur le bureau. | A secretária = le bureau (le meuble), ou la secrétaire.
O jantar estava ___, parabéns ao cozinheiro! | delicioso | esquisito / exquisito | Le dîner était exquis, bravo au cuisinier ! | Exquis = delicioso ; esquisito = bizarre.
Para fechar, ___ a porta com força. | empurre | puxe / pouse | Pour fermer, poussez la porte avec force. | Empurrar = pousser.
Qual é a ___ de hoje? — Dia 12. | data | dada / dia de hoje | Quelle est la date d'aujourd'hui ? — Le 12. | A data = la date.
A ___ onde trabalho tem cem empregados. | firma | fazenda / quinta | L'entreprise où je travaille a cent employés. | A firma = l'entreprise.
"""
},
]
