# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » du portugais, C1 : tous les temps melanges.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python portugais/outils/construire.py (niveaux.py).
BROUILLON : a faire relire par un lusophone du Portugal.
"""

TEMPS = [
{
"id": "temps-mistura", "titre": "Tous les temps — choisir le bon",
"texte": "Le C1 mélange tout : perfeito ou imperfeito, indicatif ou conjuntivo (et lequel des trois), infinitif personnel, mésoclise. Une seule question à se poser : qu'est-ce qui commande le verbe ? Un moment précis, une conjonction (<b>quando, se, embora</b>), un verbe de souhait, une préposition ?<br><em>Se tivesse sabido que vinhas, ter-te-ia esperado.</em> (Si j'avais su que tu venais, je t'aurais attendu.)",
"serie": "tempsMisturaPtExercises", "kicker": "Tous les temps",
"questions": """
Quando ___ (chegar) ao Porto, liga-me. | chegares | chegas / chegasses | Quand tu arriveras à Porto, appelle-moi. | Quando + futur : futuro do conjuntivo.
Embora ___ (estar) cansado, acabou o trabalho. | estivesse | estava / esteja | Bien qu'il soit fatigué, il a fini le travail. | Embora, au passé : imperfeito do conjuntivo.
Se ___ (saber) que vinhas, ter-te-ia esperado. | tivesse sabido | soubesse / tiver sabido | Si j'avais su que tu venais, je t'aurais attendu. | Irréel du passé.
A reunião ___ (realizar-se) amanhã às dez. (écrit) | realizar-se-á | se realizará / realizará-se | La réunion aura lieu demain à dix heures. | Futur sans déclencheur : mésoclise.
É altura de vocês ___ (decidir). | decidirem | decidam / decidiram | Il est temps que vous décidiez. | Infinitif personnel.
Quando era estudante, ___ (trabalhar) num bar. | trabalhava | trabalhei-me / trabalhasse | Quand j'étais étudiant, je travaillais dans un bar. | Une habitude passée : imperfeito.
Nunca ___ (ver) nada assim antes daquela viagem. | tinha visto | vi / tenho visto | Je n'avais jamais rien vu de tel avant ce voyage. | Le passé avant le passé.
Ultimamente ___ (andar) muito cansada. | tenho andado | andei / ando-me | Ces derniers temps, je suis très fatiguée. | Continu jusqu'à maintenant.
Duvido que eles já ___ (chegar). | tenham chegado | chegaram / tivessem chegado | Je doute qu'ils soient déjà arrivés. | Doute sur le passé récent : tenha + participe.
Por mais que ___ (insistir), ele não mudou de ideias. | insistíssemos | insistimos / insistamos | Nous avons eu beau insister, il n'a pas changé d'avis. | Por mais que, au passé : imperfeito do conjuntivo.
Obrigado por ___ (vir). | terem vindo | virem-se / vieram | Merci d'être venus. | Infinitif personnel composé.
O suspeito ___ (fugir) para Espanha. (presse, non confirmé) | teria fugido | terá fugido / fugiu-se | Le suspect se serait enfui en Espagne. | Information non confirmée : teria + participe.
Se ___ (fazer) sol amanhã, vamos à praia. | fizer | fizesse / faça | S'il fait beau demain, nous irons à la plage. | Se + possibilité future : futuro do conjuntivo.
Ela pediu-me que ___ (ficar) mais um dia. | ficasse | fique / ficar | Elle m'a demandé de rester un jour de plus. | Concordance au passé.
Assim que ___ (receber) a resposta, telefono-te. | tiver recebido | recebi / tenha recebido | Dès que j'aurai reçu la réponse, je te téléphone. | Futur antérieur du conjuntivo.
Antes de ___ (sair), fechem as janelas. | saírem | sairem / saiam | Avant de sortir, fermez les fenêtres. | Antes de + infinitif personnel.
Não acho que ___ (valer) a pena. | valha | vale / valer | Je ne pense pas que ça vaille la peine. | Não achar que + conjuntivo.
Acho que ___ (valer) a pena. | vale | valha / valer | Je pense que ça vaut la peine. | Achar que, affirmatif : indicatif.
Disse que ___ (telefonar) no dia seguinte. | telefonaria | telefonará / telefone | Il a dit qu'il téléphonerait le lendemain. | Futur dans le passé.
Caso ___ (haver) atrasos, avisaremos. | haja | houver / há | Au cas où il y aurait des retards, nous préviendrons. | Caso + conjuntivo présent.
Quem me dera ___ (ter) mais tempo! | ter | tivesse-me / tenha | Si seulement j'avais plus de temps ! | Quem me dera + infinitif (même sujet).
Era como se ninguém ___ (dar) por nós. | desse | dê / der | C'était comme si personne ne nous remarquait. | Como se + imperfeito do conjuntivo.
"""
},
{
"id": "temps-registo-escrito", "titre": "Le temps des textes — fizera, far-se-á",
"texte": "L'écrit soutenu a ses temps : le <b>mais-que-perfeito simples</b> (<b>fizera, dissera</b>) dans les récits, la <b>mésoclise</b> (<b>far-se-á, dir-se-ia</b>) au futur et au conditionnel, le <b>conditionnel composé</b> de la presse (<b>teria fugido</b>). Les reconnaître, c'est lire la presse et les romans portugais.<br><em>Quando chegou, já o comboio partira.</em> (Quand il est arrivé, le train était déjà parti.)",
"serie": "tempsEscritoPtExercises", "kicker": "L'écrit soutenu",
"questions": """
Quando chegou, o comboio já ___ (= tinha partido). | partira | partiu / partiria | Quand il est arrivé, le train était déjà parti. | Mais-que-perfeito simples : partiram → partira.
Ele ___ que voltaria (= tinha dito). | dissera | dizera / diria | Il avait dit qu'il reviendrait. | Disseram → dissera.
O resultado ___ amanhã. (anunciar, se passif, écrit) | anunciar-se-á | se anunciará / anunciará-se | Le résultat sera annoncé demain. | Mésoclise : anunciar-se-á.
___ que o verão chegou mais cedo. (dizer, se, conditionnel) | Dir-se-ia | Se diria / Diria-se | On dirait que l'été est arrivé plus tôt. | Dir-se-ia.
Segundo a polícia, os assaltantes ___ por uma janela. | teriam entrado | terão entrado / entraram-se | Selon la police, les cambrioleurs seraient entrés par une fenêtre. | Conditionnel composé de la presse.
Nunca ___ tanta gente (= tinha visto). | vira | viu / veria | Il n'avait jamais vu autant de monde. | Viram → vira.
Se pudesse, ___ (ajudar + o, écrit). | ajudá-lo-ia | ajudaria-o / o ajudá-ia | S'il le pouvait, il l'aiderait. | Mésoclise avec o : ajudá-lo-ia.
___ (= tinha sido) um inverno difícil. | Fora | Foi-se / Seria | Ç'avait été un hiver difficile. | Foram → fora.
O Governo ___ novas medidas (= vai anunciar, écrit). | anunciará | anunciaria / anunciara | Le gouvernement annoncera de nouvelles mesures. | Futuro simples, à l'écrit.
Tudo acontecera como ela ___ (= tinha previsto). | previra | previu / preveria | Tout s'était passé comme elle l'avait prévu. | Preveram → previra.
"""
},
]
