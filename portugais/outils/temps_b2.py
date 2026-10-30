# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » du portugais, B2 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python portugais/outils/construire.py (niveaux.py).
BROUILLON : a faire relire par un lusophone du Portugal.
"""

TEMPS = [
{
"id": "temps-conjuntivo-imperfeito", "titre": "Imperfeito do conjuntivo — se eu pudesse",
"texte": "L'hypothèse peu probable ou irréelle (<b>se eu fosse…</b>), <b>como se</b>, <b>quem me dera que</b>, et la concordance quand la principale est au passé ou au conditionnel (<b>queria que viesses</b>). Sur le perfeito, 3e pers. du pluriel : <b>fizeram → fizesse</b>, <b>foram → fosse</b> ; nós : <b>fizéssemos, fôssemos, falássemos, comêssemos</b>.<br><em>Se tivesse tempo, ia contigo.</em> (Si j'avais le temps, j'irais avec toi.)",
"serie": "tempsConjuntivoImperfeitoPtExercises", "kicker": "Se eu pudesse…",
"questions": """
Se eu ___ (ter) dinheiro, viajava mais. | tivesse | tiver / tenha | Si j'avais de l'argent, je voyagerais davantage. | Ter → tivesse.
Se ___ (ser) mais cedo, ainda apanhávamos o comboio. | fosse | for / seja | S'il était plus tôt, nous attraperions encore le train. | Ser → fosse.
Ela queria que eu ___ (ir) com ela. | fosse | for / vá | Elle voulait que j'aille avec elle. | Ir → fosse.
Pediram-nos que ___ (esperar) lá fora. | esperássemos | esperemos / esperarmos | Ils nous ont demandé d'attendre dehors. | Nós : esperássemos.
Ele fala como se ___ (saber) tudo. | soubesse | sabe / saiba | Il parle comme s'il savait tout. | Como se + imperfeito do conjuntivo.
Se ___ (poder), ajudava-te. | pudesse | puder / posso | Si je pouvais, je t'aiderais. | Poder → pudesse.
Quem me dera que ___ (fazer) bom tempo! | fizesse | faça / fizer | Si seulement il faisait beau ! | Fazer → fizesse.
Se nós ___ (vir) mais cedo, víamos tudo. | viéssemos | viermos / venhamos | Si nous venions plus tôt, nous verrions tout. | Vir → viesse, viéssemos.
Era preciso que vocês ___ (estar) presentes. | estivessem | estejam / estiverem | Il fallait que vous soyez présents. | Estar → estivesse.
Se eles ___ (querer), podiam ficar. | quisessem | quiserem / queiram | S'ils voulaient, ils pourraient rester. | Querer → quisesse.
Embora ___ (chover), fomos passear. | chovesse | chova / chover | Bien qu'il pleuve, nous sommes allés nous promener. | Concordance au passé : chovesse.
Se tu ___ (dizer) a verdade, ninguém se zangava. | dissesses | disseres / digas | Si tu disais la vérité, personne ne se fâcherait. | Dizer → dissesse.
Disse-lhe que ___ (pôr) o casaco. | pusesse | ponha / puser | Je lui ai dit de mettre son manteau. | Pôr → pusesse.
Se nós ___ (ser) ricos, comprávamos uma quinta. | fôssemos | formos / sejamos | Si nous étions riches, nous achèterions une ferme. | Nós : fôssemos (accent circonflexe).
Ninguém acreditava que ele ___ (conseguir). | conseguisse | consiga / conseguir | Personne ne croyait qu'il y arriverait. | Conseguiram → conseguisse.
Se ___ (haver) mais tempo, falávamos disso. | houvesse | houver / haja | S'il y avait plus de temps, nous en parlerions. | Haver → houvesse.
"""
},
{
"id": "temps-compostos", "titre": "Les temps composés — tenho feito, terei feito, teria feito",
"texte": "<b>Tenho feito</b> : répété ou continu jusqu'à maintenant (ce n'est pas le passé composé !). <b>Terei feito</b> : ce qui sera fini, ou une supposition (<b>terá esquecido?</b>). <b>Teria feito</b> : le conditionnel passé, ou l'information non confirmée. Et au conjuntivo : <b>tenha / tivesse / tiver feito</b>.<br><em>Tenho dormido mal. Às oito terei acabado. Teria gostado de ir.</em>",
"serie": "temposCompostosTempsPtExercises", "kicker": "Les temps composés",
"questions": """
Ultimamente ___ (ler) muito. | tenho lido | li / tinha lido | Ces derniers temps, je lis beaucoup. | Continu jusqu'à maintenant : perfeito composto.
Ontem ___ (ler) o jornal inteiro. | li | tenho lido / lia-o | Hier, j'ai lu tout le journal. | Action finie : perfeito simples.
Às dez horas já ___ (acabar) o exame. | terei acabado | acabarei / tinha acabado | À dix heures, j'aurai déjà fini l'examen. | Futur antérieur.
A Ana não chegou. ___ (perder) o comboio? | Terá perdido | Teria perdido / Tem perdido | Ana n'est pas arrivée. Elle aurait raté le train ? | Supposition : terá + participe.
Eu ___ (gostar) de ir, mas estava doente. | teria gostado | terei gostado / tenho gostado | J'aurais aimé y aller, mais j'étais malade. | Conditionnel passé.
Espero que ___ (correr) tudo bem. | tenha corrido | tem corrido / tivesse corrido | J'espère que tout s'est bien passé. | Espero que + tenha + participe.
Se ___ (saber), teria vindo. | tivesse sabido | tiver sabido / tinha sabido | Si j'avais su, je serais venu. | Se + tivesse + participe.
Quando ___ (terminar), avisa-me. | tiveres terminado | tenhas terminado / tivesses terminado | Quand tu auras terminé, préviens-moi. | Quando + tiver + participe.
Este mês ___ (chover) imenso. | tem chovido | choveu-se / terá chovido | Ce mois-ci, il pleut énormément. | Tem chovido.
Segundo os jornais, o ministro ___ (mentir). | teria mentido | terá mentido / tem mentido | Selon les journaux, le ministre aurait menti. | Information non confirmée : teria + participe.
Nós ___ (estar) muito ocupados nas últimas semanas. | temos estado | estivemos-nos / teremos estado | Nous sommes très occupés ces dernières semaines. | Temos estado.
Talvez ele já ___ (sair). | tenha saído | tem saído / tiver saído | Peut-être qu'il est déjà parti. | Talvez + tenha + participe.
Daqui a um ano, ___ (mudar) de casa. | teremos mudado | mudámos / tínhamos mudado | Dans un an, nous aurons déménagé. | Futur antérieur : teremos mudado.
Se ___ (chegar) a tempo, tínhamos visto o início. | tivéssemos chegado | tivermos chegado / tínhamos chegado | Si nous étions arrivés à temps, nous aurions vu le début. | Se + tivesse + participe.
"""
},
]
