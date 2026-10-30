# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » du portugais, A2 : une serie par temps.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python portugais/outils/construire.py (niveaux.py).
BROUILLON : a faire relire par un lusophone du Portugal.
"""

TEMPS = [
{
"id": "temps-perfeito", "titre": "Pretérito perfeito — le passé terminé",
"texte": "Une action finie, à un moment passé (ontem, no sábado, em 2019, há dois anos). C'est aussi le passé composé français : <b>Já comeste?</b> Réguliers : <b>-ei, -aste, -ou, -ámos, -aram</b> ; <b>-i, -este, -eu, -emos, -eram</b> ; <b>-i, -iste, -iu, -imos, -iram</b>. Irréguliers : fiz, tive, estive, fui, pude, disse, trouxe, pus, vi, vim, dei, soube, quis.<br><em>Ontem fui ao cinema. Comprámos pão. Já viste?</em> (Hier je suis allé au cinéma. Nous avons acheté du pain. Tu as déjà vu ?)",
"serie": "tempsPerfeitoPtExercises", "kicker": "Le perfeito",
"questions": """
Ontem ___ (jantar) num restaurante italiano. | jantámos | jantamos / jantávamos | Hier, nous avons dîné dans un restaurant italien. | Nós, perfeito en -ar : jantámos (avec accent).
No sábado eu ___ (fazer) um bolo. | fiz | fazi / fazia | Samedi, j'ai fait un gâteau. | Fazer → fiz.
Eles ___ (chegar) às dez. | chegaram | chegavam / chegam | Ils sont arrivés à dix heures. | -ar, eles : -aram.
Tu ___ (ver) o jogo ontem? | viste | vês / vias | Tu as vu le match hier ? | Ver → vi, viste.
A Rita ___ (ter) um bebé em março. | teve | tinha / tive | Rita a eu un bébé en mars. | Ter → tive, teve.
Eu ___ (estar) em Paris o ano passado. | estive | estava / esteve | J'ai été à Paris l'an dernier. | Estar → estive.
Nós ___ (ir) a Sintra no domingo. | fomos | íamos / vamos | Nous sommes allés à Sintra dimanche. | Ir → fui, fomos.
Ele não ___ (poder) vir à festa. | pôde | pode / pude | Il n'a pas pu venir à la fête. | Poder, 3e personne : pôde (accent).
Quem te ___ (dizer) isso? | disse | dizeu / dizia | Qui t'a dit ça ? | Dizer → disse.
Eu ___ (pagar) a conta. | paguei | paguéi / pagei | J'ai payé l'addition. | -gar : g → gu devant e (paguei).
Eu ___ (começar) a trabalhar às oito. | comecei | começei / começava | J'ai commencé à travailler à huit heures. | -çar : ç → c devant e (comecei).
Vocês ___ (trazer) o vinho? | trouxeram | trazeram / traziam | Vous avez apporté le vin ? | Trazer → trouxe, trouxeram.
Onde ___ (pôr) as chaves? Não as encontro. | puseste | pões / pusiste | Où as-tu mis les clés ? Je ne les trouve pas. | Pôr → pus, puseste.
Eu ___ (ficar) em casa todo o dia. | fiquei | ficei / ficava | Je suis resté à la maison toute la journée. | -car : c → qu devant e (fiquei).
O filme ___ (acabar) muito tarde. | acabou | acabava / acaba | Le film s'est terminé très tard. | -ar, ele : -ou.
Eles ___ (vir) de comboio. | vieram | vinham / viram | Ils sont venus en train. | Vir → vim, vieram (viram vient de ver).
Eu ___ (saber) a notícia pelo jornal. | soube | sabi / sabia | J'ai appris la nouvelle par le journal. | Saber au perfeito : soube (= j'ai appris).
Ela ___ (sair) às sete. | saiu | saía / sai | Elle est sortie à sept heures. | Sair → saí, saiu.
Nós ___ (beber) um café na esplanada. | bebemos | bebíamos / bebêmos | Nous avons bu un café en terrasse. | -er, nós : -emos (comme le présent).
Tu ___ (dar) o presente à avó? | deste | dás / davas | Tu as donné le cadeau à grand-mère ? | Dar → dei, deste.
Eu ___ (querer) telefonar-te, mas não tive tempo. | quis | queri / queria-te | J'ai voulu te téléphoner, mais je n'ai pas eu le temps. | Querer → quis.
O avião ___ (partir) com atraso. | partiu | partia / parte | L'avion est parti en retard. | -ir, ele : -iu.
"""
},
{
"id": "temps-imperfeito", "titre": "Pretérito imperfeito — le décor et l'habitude",
"texte": "Ce qu'on faisait d'habitude, le décor, l'âge, l'heure, une action en cours dans le passé. <b>-ava</b> (-ar) et <b>-ia</b> (-er, -ir) ; irréguliers : era, tinha, vinha, punha. Au Portugal, il sert aussi de conditionnel poli : <b>queria</b>, <b>podia</b>, <b>gostava</b>.<br><em>Quando era criança, ia à praia todos os dias.</em> (Quand j'étais enfant, j'allais à la plage tous les jours.)",
"serie": "tempsImperfeitoPtExercises", "kicker": "L'imperfeito",
"questions": """
Antigamente eu ___ (morar) em Braga. | morava | morei / moro | Autrefois, j'habitais à Braga. | Une situation passée : imperfeito (-ava).
Quando eu ___ (ser) pequeno, tinha medo do escuro. | era | fui / sou | Quand j'étais petit, j'avais peur du noir. | Ser → era.
Todos os verões nós ___ (ir) ao Algarve. | íamos | fomos / vamos | Tous les étés, nous allions en Algarve. | Ir à l'imperfeito : ia, íamos.
O meu avô ___ (contar) histórias à noite. | contava | contou / conta | Mon grand-père racontait des histoires le soir. | Une habitude : -ava.
___ (ser) cinco horas quando acordei. | Eram | Foram / Eram-se | Il était cinq heures quand je me suis réveillé. | L'heure, au passé : eram.
Ela ___ (ter) vinte anos quando se casou. | tinha | teve / tem | Elle avait vingt ans quand elle s'est mariée. | L'âge : tinha.
Eu ___ (querer) um quarto com vista, por favor. | queria | quis / quero-me | Je voudrais une chambre avec vue, s'il vous plaît. | La politesse : queria.
Enquanto ela ___ (ler), eu cozinhava. | lia | leu / lê | Pendant qu'elle lisait, je cuisinais. | Deux actions qui durent : imperfeito.
Antes não ___ (haver) metro no Porto. | havia | houve / há | Avant, il n'y avait pas de métro à Porto. | Haver → havia.
A casa ___ (ficar) perto do rio. | ficava | ficou / fica | La maison se trouvait près de la rivière. | La description : ficava.
Vocês ___ (vir) sempre de autocarro? | vinham | vieram / vêm | Vous veniez toujours en bus ? | Vir → vinha, vinham.
O meu pai ___ (pôr) a mesa todos os domingos. | punha | pôs / põe | Mon père mettait la table tous les dimanches. | Pôr → punha.
Nós ___ (sair) muito à noite. | saíamos | saímos / sairemos | Nous sortions beaucoup le soir. | Sair : saía, saíamos (accent).
Tu ___ (gostar) de vir connosco? | gostavas | gostaste / gostas-te | Tu aimerais venir avec nous ? | L'imperfeito à la place du conditionnel.
___ (estar) um dia lindo. | Estava | Esteve / Está-se | C'était une belle journée. | Le décor : estava.
As crianças ___ (brincar) no jardim. | brincavam | brincaram / brincam | Les enfants jouaient dans le jardin. | -ar, eles : -avam.
Eu ___ (poder) ajudar-te amanhã, se quiseres. | podia | pude / pôde | Je pourrais t'aider demain, si tu veux. | Imperfeito = conditionnel oral.
Naquele tempo, ninguém ___ (ter) carro. | tinha | teve / tem | À cette époque-là, personne n'avait de voiture. | Ter → tinha.
"""
},
{
"id": "temps-futuro", "titre": "Le futur — vou fazer et farei",
"texte": "À l'oral, le futur se dit <b>ir</b> au présent + infinitif : <b>vou sair</b>, <b>vamos jantar</b>. Le <b>futuro simples</b> (infinitif + <b>-ei, -ás, -á, -emos, -ão</b>) est plus écrit, ou solennel ; il sert aussi à la supposition : <b>Onde estará ele?</b> (où peut-il bien être ?). Radicaux courts : farei, direi, trarei.<br><em>Amanhã vou trabalhar. Voltaremos em breve.</em> (Demain je vais travailler. Nous reviendrons bientôt.)",
"serie": "tempsFuturoPtExercises", "kicker": "Le futur",
"questions": """
Amanhã eu ___ visitar a minha tia. | vou | irei a / vá | Demain, je vais rendre visite à ma tante. | À l'oral : ir + infinitif.
Nós ___ jantar fora no sábado. | vamos | iremos de / íamos-nos | Nous allons dîner dehors samedi. | Ir, nós : vamos.
O avião ___ às dez horas. (futuro simples) | partirá | partirei / parte-se | L'avion partira à dix heures. | Partir + á.
Eu ___ o trabalho até sexta. (futuro simples, fazer) | farei | fazerei / fazei | Je ferai le travail d'ici vendredi. | Fazer → far- : farei.
Prometo que te ___ a verdade. (futuro simples, dizer) | direi | dizerei / disse | Je promets que je te dirai la vérité. | Dizer → dir- : direi.
Vocês ___ ao concerto? | vão | vais / ides-se | Vous allez au concert ? | Ir, vocês : vão.
Onde ___ o Rui a esta hora? | estará | estaria / está-se | Où peut bien être Rui à cette heure-ci ? | Le futur de supposition.
Eles ___ o vinho. (futuro simples, trazer) | trarão | trazerão / trouxeram | Ils apporteront le vin. | Trazer → trar- : trarão.
Tu ___ gostar deste filme. | vais | vai / vás | Tu vas aimer ce film. | Ir, tu : vais.
___ muita gente na festa. (futuro simples, haver) | Haverá | Haveram / Há-de | Il y aura beaucoup de monde à la fête. | Haver → haverá (singulier).
Daqui a dez anos, ___ em Lisboa? (futuro simples, viver) | viverás | vivirás / vives | Dans dix ans, vivras-tu à Lisbonne ? | Viver + ás.
A loja ___ abrir às nove. | vai | vão / vá | Le magasin va ouvrir à neuf heures. | Ir, ele : vai.
Nós ___ em contacto. (futuro simples, ficar) | ficaremos | ficarmos / ficámos | Nous resterons en contact. | Ficar + emos.
Amanhã ___ chover. | vai | vá / irá a | Demain, il va pleuvoir. | Ir + infinitif, impersonnel : vai chover.
"""
},
{
"id": "temps-imperativo", "titre": "L'impératif — fala, fale, não fales",
"texte": "Avec <b>tu</b> : la forme de <b>ele</b> au présent (<b>fala</b>, <b>come</b>) ; au négatif, le subjonctif (<b>não fales</b>). Avec <b>o senhor, a senhora, você</b> et <b>vocês</b> : le subjonctif (<b>fale</b>, <b>falem</b>). Irréguliers avec tu : sê, vai, faz, diz, vem, põe, tem.<br><em>Abre a janela! Não abras a porta. Abra, por favor.</em> (Ouvre la fenêtre ! N'ouvre pas la porte. Ouvrez, s'il vous plaît.)",
"serie": "tempsImperativoPtExercises", "kicker": "L'impératif",
"questions": """
(tu) ___ a porta, por favor. | Fecha | Feche / Fechas | Ferme la porte, s'il te plaît. | Tu, affirmatif : fecha.
(tu) Não ___ tanto! | comas | comes / come | Ne mange pas autant ! | Tu, négatif : não comas.
(o senhor) ___ à direita. | Vire | Vira / Viras | Tournez à droite. | O senhor : le subjonctif (vire).
(vocês) ___ depressa! | Venham | Vêm / Vinde | Venez vite ! | Vocês : venham.
(tu) ___ cá! | Vem | Venha / Vens | Viens ici ! | Vir, tu : vem.
(tu) ___ calma, vai correr bem. | Tem | Tenha / Tens | Garde ton calme, ça va bien se passer. | Ter, tu : tem.
(tu) Não ___ a ninguém! | digas | dizes / diz | Ne le dis à personne ! | Dizer, négatif : não digas.
(a senhora) ___ um momento, por favor. | Espere | Espera / Esperes | Attendez un instant, s'il vous plaît. | La senhora : espere.
(tu) ___ o casaco, está frio. | Põe | Ponha / Pões | Mets ton manteau, il fait froid. | Pôr, tu : põe.
(vocês) Não ___ barulho! | façam | fazem / fazei | Ne faites pas de bruit ! | Fazer, vocês : façam.
(tu) ___ simpático com a tua irmã. | Sê | És / Seja | Sois gentil avec ta sœur. | Ser, tu : sê.
(o senhor) ___ aqui, por favor. | Assine | Assina / Assinas | Signez ici, s'il vous plaît. | O senhor : assine.
(tu) ___-te, que vamos chegar atrasados! | Despacha | Despache / Despachas | Dépêche-toi, nous allons être en retard ! | Tu : despacha-te.
(tu) Não te ___! | esqueças | esqueces / esquece | N'oublie pas ! | Négatif : não te esqueças.
"""
},
]
