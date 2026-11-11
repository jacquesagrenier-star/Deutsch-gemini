# -*- coding: utf-8 -*-
"""Les tuiles de grammaire du portugais (11 nov. 2026, lot P5 de
audit/ALIGNEMENT-LANGUES-2026-11-11.md) : ce que chaque panneau propose, sur le
modele de anglais/outils/tuiles_niveaux.py. Lu par niveaux.tuiles(), qui les
range dans grammaire.json (cle « tuiles ») ; index.html dessine le panneau
(panneauTuileAnglaise, commun a l'anglais et au portugais).

Une option est l'une de trois choses :
  {"fiche": id}        ouvre une fiche de grammaire portugaise (A1-C1, ou une des FICHES ci-dessous)
  {"vocab": fonction}  lance un vocabulaire de mots-outils deja dans l'app (fonctionnels.json)
  {"serie": nom, ...}  une serie dediee, dont les questions sont dans tuiles_series.py

La tuile « genero » n'a pas de tuile sur la grille : ses options sont ajoutees
au panneau des Noms (regles du genre, terminaisons, faux amis).

Les REGLES DU GENRE sont des donnees : niveaux.py mesure leur taux sur nos noms
(A1-C1) et l'ecrit dans le tableau de la fiche « genero », et tire de nos noms
la serie « Deviner le genre par la terminaison ».

SOURCE : on corrige ici, puis python portugais/outils/construire.py.
BROUILLON : a faire relire par un lusophone du Portugal.
"""
import tuiles_series as S

Q = S.Q


def serie(nom, id, titre, desc, niveau, kicker):
    return {"serie": nom, "id": id, "titre": titre, "desc": desc, "niveau": niveau,
            "kicker": kicker, "questions": Q[nom]}


# ------------------------------------------------------------------ les regles du genre
# (terminaison, genre, exemples, exceptions connues). Le taux est MESURE sur nos
# noms par niveaux.py ; l'ordre est celui de la fiche. Une terminaison plus
# longue l'emporte (-ção avant -ão).
REGLES_GENRE = [
    ("-ção", "a", ["a canção", "a estação", "a informação"], ["o coração"]),
    ("-são", "a", ["a decisão", "a televisão", "a profissão"], []),
    ("-dade", "a", ["a cidade", "a verdade", "a idade"], []),
    ("-gem", "a", ["a viagem", "a garagem", "a paisagem"], ["o personagem (aussi a)"]),
    ("-eza", "a", ["a beleza", "a certeza", "a tristeza"], []),
    ("-ema", "o", ["o problema", "o sistema", "o tema"], []),
    ("-ume", "o", ["o legume", "o perfume", "o costume"], []),
    ("-or", "o", ["o calor", "o amor", "o elevador"], ["a cor", "a dor", "a flor"]),
    ("-o", "o", ["o livro", "o carro", "o copo"], ["a tribo", "a foto", "a moto"]),
    ("-a", "a", ["a casa", "a mesa", "a janela"], ["o dia", "o mapa", "o sofá"]),
    ("-ão", "o", ["o pão", "o avião", "o feijão"], ["a mão"]),
]

FICHES = [
{
"id": "genero", "niveau": "A2", "titre": "O ou a ? Les règles du genre", "resume": "-ção, -dade, -gem : féminin ; -ema, -or : masculin",
"regle": "Le genre d'un nom portugais se devine souvent à sa fin. <b>-o</b> est presque toujours masculin, <b>-a</b> presque toujours féminin ; <b>-ção</b>, <b>-são</b>, <b>-dade</b>, <b>-gem</b>, <b>-eza</b> sont féminins ; les mots grecs en <b>-ema</b> (<b>o problema</b>) et les noms en <b>-or</b>, <b>-ume</b> sont masculins. Les noms en <b>-e</b>, <b>-l</b>, <b>-z</b> ne suivent aucune règle : il faut les apprendre avec leur article (<b>o leite</b>, <b>a ponte</b>, <b>o sal</b>, <b>a luz</b>). Le pourcentage indique la part de nos noms qui suivent la règle.",
"tableau": [],
"exemples": [
 ["O problema da cidade é o trânsito.", "Le problème de la ville, c'est la circulation."],
 ["A viagem foi longa, mas a paisagem era linda.", "Le voyage a été long, mais le paysage était magnifique."],
 ["O dia está bonito e a cor do mar é incrível.", "La journée est belle et la couleur de la mer est incroyable."],
],
"attention": "Plusieurs noms changent de genre entre le français et le portugais : <b>o leite</b> (le lait), <b>a árvore</b> (l'arbre), <b>o sangue</b> (le sang), <b>a ponte</b> (le pont), <b>o mel</b> (le miel), <b>a viagem</b> (le voyage), <b>a dor</b> (la douleur), <b>o nariz</b> (le nez). Et le Brésil et le Portugal ne s'accordent pas toujours : <b>o ecrã</b> / <b>a tela</b>.",
"serie": "terminaisonsPtExercises", "kicker": "Deviner le genre",
"questions": "",
},
{
"id": "numeros", "niveau": "A1", "titre": "Les nombres, l'heure et les dates", "resume": "um, uma · dois, duas · são três horas · dia 5 de maio",
"regle": "<b>Um</b> et <b>dois</b> s'accordent au féminin : <b>uma casa</b>, <b>duas casas</b> ; les centaines aussi : <b>duzentos euros</b>, <b>duzentas pessoas</b>. Cent seul se dit <b>cem</b>, suivi d'un autre nombre <b>cento</b> (<b>cento e vinte</b>). L'heure : <b>é uma hora</b>, puis <b>são duas, são três…</b> ; <b>e meia</b> (et demie), <b>menos um quarto</b> (moins le quart), <b>ao meio-dia</b>, <b>à meia-noite</b>. Les dates : <b>dia 5 de maio de 2026</b>, avec le nombre simple (sauf <b>dia primeiro</b>, possible pour le 1er).",
"tableau": [
 ["um, uma · dois, duas", "un, une · deux", "um café, uma bica, dois pastéis, duas águas"],
 ["cem · cento e…", "cent · cent…", "cem euros · cento e cinquenta"],
 ["duzentos, duzentas", "deux cents (accordé)", "duzentas pessoas"],
 ["é uma hora · são duas", "il est une heure · deux heures", "São três e meia."],
 ["às oito · à uma", "à huit heures · à une heure", "O comboio parte às oito."],
 ["primeiro, segundo, terceiro", "les ordinaux (accordés)", "a segunda vez, o terceiro andar"],
 ["dia 5 de maio", "le 5 mai", "Faço anos no dia 5 de maio."],
],
"exemples": [
 ["São duas e um quarto.", "Il est deux heures et quart."],
 ["O bilhete custa cento e vinte euros.", "Le billet coûte cent vingt euros."],
 ["Moro no segundo andar.", "J'habite au deuxième étage."],
],
"attention": "On dit <b>um milhão de pessoas</b>, avec <b>de</b>, mais <b>mil pessoas</b> sans. Et au téléphone, les Portugais disent souvent les chiffres deux à deux : 21 345 67 89 → <b>vinte e um, trezentos e quarenta e cinco…</b>",
"serie": "numerosFichePtExercises", "kicker": "Les nombres",
"questions": """
Tenho ___ filhas. | duas | dois / doas | J'ai deux filles. | Dois → duas au féminin.
___ três horas. | São | É / Estão | Il est trois heures. | Dès deux heures : são.
O pão custa ___ cêntimos. | cinquenta | cinquento / cinquentas | Le pain coûte cinquante centimes. | Les dizaines ne s'accordent pas.
Moro no ___ andar. | quinto | cinco / quinta | J'habite au cinquième étage. | L'ordinal : quinto.
A sala tem ___ lugares. | trezentos | trezentas / três cem | La salle a trois cents places. | Lugares (masc.) : trezentos.
""",
},
{
"id": "preposicoes", "niveau": "A1", "titre": "Les prépositions : em, de, a, por, para", "resume": "no, na, do, da, ao, à, pelo, pela",
"regle": "Les prépositions <b>em</b> (dans, sur, à), <b>de</b> (de), <b>a</b> (à) et <b>por</b> (par) se soudent à l'article : <b>no, na, nos, nas</b> ; <b>do, da, dos, das</b> ; <b>ao, à, aos, às</b> ; <b>pelo, pela</b>. Elles se soudent aussi à <b>um</b> (<b>num, numa</b>), aux démonstratifs (<b>neste, desse, àquele</b>) et aux pronoms (<b>nele, dela</b>). Pour le lieu : <b>em</b> où l'on est (<b>estou em casa</b>), <b>a</b> ou <b>para</b> où l'on va (<b>vou ao Porto</b>, <b>vou para casa</b>). Pour le temps : <b>às oito</b>, <b>na segunda-feira</b>, <b>em maio</b>, <b>há dois anos</b>, <b>desde 2020</b>, <b>daqui a uma hora</b>.",
"tableau": [
 ["em + o, a → no, na", "dans le, dans la", "no carro, na rua"],
 ["de + o, a → do, da", "du, de la", "a casa do Rui"],
 ["a + o, a → ao, à", "au, à la", "Vou ao cinema e à praia."],
 ["por + o, a → pelo, pela", "par le, par la", "Passámos pela ponte."],
 ["em + um → num, numa", "dans un, dans une", "Moro numa casa antiga."],
 ["há · desde · daqui a", "il y a · depuis · dans", "Cheguei há uma semana."],
],
"exemples": [
 ["Estou na esplanada do café.", "Je suis à la terrasse du café."],
 ["Vamos à praia no sábado.", "Allons à la plage samedi."],
 ["Moro em Lisboa há três anos.", "J'habite à Lisbonne depuis trois ans."],
],
"attention": "Les villes n'ont pas d'article (<b>em Lisboa</b>, <b>de Braga</b>), sauf <b>o Porto</b> : <b>no Porto</b>, <b>do Porto</b>. Les pays en ont souvent un : <b>em Portugal</b> (sans), mais <b>no Brasil</b>, <b>na França</b>, <b>nos Estados Unidos</b>.",
"serie": "preposicoesFichePtExercises", "kicker": "Les prépositions",
"questions": """
Estou ___ cozinha. | na | em a / à | Je suis dans la cuisine. | Em + a = na.
Vou ___ Porto amanhã. | ao | a o / no | Je vais à Porto demain. | A + o Porto = ao Porto.
Moro ___ Portugal. | em | no / na | J'habite au Portugal. | Portugal n'a pas d'article : em Portugal.
Ela é ___ Brasil. | do | de / da | Elle vient du Brésil. | De + o Brasil = do Brasil.
O avião passa ___ cidade. | pela | por a / pelo | L'avion passe au-dessus de la ville. | Por + a = pela.
""",
},
{
"id": "adverbios", "niveau": "A2", "titre": "Les adverbes", "resume": "-mente, bem, mal · sempre, já, ainda · aqui, ali, lá",
"regle": "Beaucoup d'adverbes se forment en ajoutant <b>-mente</b> au féminin de l'adjectif : <b>rápida → rapidamente</b>, <b>feliz → felizmente</b> (l'accent écrit tombe : <b>prático → praticamente</b>). <b>Bom</b> et <b>mau</b> donnent <b>bem</b> et <b>mal</b>. Les adverbes de temps (<b>sempre, nunca, já, ainda, logo</b>) attirent le pronom devant le verbe : <b>Já te disse</b>. Le lieu a trois degrés, comme les démonstratifs : <b>aqui</b> (ici), <b>aí</b> (là, près de toi), <b>ali / lá</b> (là-bas) ; <b>cá</b> avec un mouvement vers moi (<b>vem cá</b>).",
"tableau": [
 ["rápida → rapidamente", "-mente sur le féminin", "Respondeu rapidamente."],
 ["bom → bem · mau → mal", "bien · mal", "Dormi mal."],
 ["sempre · nunca · às vezes", "toujours · jamais · parfois", "Às vezes vou a pé."],
 ["já · ainda · já não", "déjà · encore · ne… plus", "Já não fumo."],
 ["aqui · aí · ali · lá · cá", "ici · là · là-bas", "Vem cá! O café é ali."],
 ["muito · pouco · demais · bastante", "très · peu · trop · assez", "Comi demais."],
],
"exemples": [
 ["Felizmente, o comboio chegou a horas.", "Heureusement, le train est arrivé à l'heure."],
 ["Ela fala português muito bem.", "Elle parle très bien portugais."],
 ["Vem cá, quero mostrar-te uma coisa.", "Viens ici, je veux te montrer quelque chose."],
],
"attention": "Avec deux adverbes en -mente coordonnés, seul le dernier garde la terminaison : <b>clara e lentamente</b> (clairement et lentement).",
"serie": "adverbiosFichePtExercises", "kicker": "Les adverbes",
"questions": """
Ela conduz ___. (cuidadoso) | cuidadosamente | cuidadosomente / cuidadosa | Elle conduit prudemment. | -mente sur le féminin : cuidadosa → cuidadosamente.
Hoje dormi ___. (bom) | bem | bom / boamente | Aujourd'hui, j'ai bien dormi. | Bom → bem.
___ te disse que não! | Já | Ainda / Nunca já | Je t'ai déjà dit que non ! | Já + pronom devant.
O restaurante fica ___, do outro lado. | ali | aqui / cá | Le restaurant est là-bas, de l'autre côté. | Là-bas : ali.
""",
},
{
"id": "ordem-das-palavras", "niveau": "A2", "titre": "L'ordre des mots", "resume": "sujet, verbe, complément · l'adjectif après le nom · la négation",
"regle": "L'ordre de base est celui du français : <b>sujet, verbe, complément</b> (<b>A Ana come uma maçã</b>). Le sujet pronom tombe souvent, la terminaison du verbe suffit : <b>Como uma maçã</b>. L'adjectif suit en général le nom (<b>uma casa branca</b>) ; quelques-uns le précèdent et changent alors de sens (<b>um grande homem</b> / <b>um homem grande</b>). La négation <b>não</b> se met devant le verbe, et le portugais accumule les négations : <b>Não vi ninguém</b>, <b>Não comprei nada</b>. Dans les questions, l'oral ajoute <b>é que</b> : <b>Onde é que moras?</b>",
"tableau": [
 ["sujet + verbe + complément", "l'ordre de base", "O Rui lê o jornal."],
 ["(sujet sous-entendu)", "le pronom tombe", "Leio o jornal todos os dias."],
 ["nom + adjectif", "l'adjectif suit", "um vinho tinto, uma rua estreita"],
 ["não + verbe + nada / ninguém", "la double négation", "Não sei nada."],
 ["interrogatif + é que", "question de l'oral", "O que é que queres?"],
 ["verbe + -pronom", "le pronom après le verbe", "Chamo-me Ana."],
],
"exemples": [
 ["Compramos pão fresco todas as manhãs.", "Nous achetons du pain frais tous les matins."],
 ["Não conheço ninguém em Faro.", "Je ne connais personne à Faro."],
 ["Porque é que não vieste?", "Pourquoi n'es-tu pas venu ?"],
],
"attention": "Pour répondre « oui », le Portugal reprend volontiers le verbe : <b>Gostaste? — Gostei.</b> (Tu as aimé ? — Oui.) ; <b>Já comeste? — Já.</b>",
"serie": "ordemFichePtExercises", "kicker": "L'ordre des mots",
"questions": """
Não comprei ___. | nada | algo / tudo | Je n'ai rien acheté. | Não… nada : double négation.
Tenho um carro ___. | vermelho | vermelha / vermelhos | J'ai une voiture rouge. | L'adjectif suit le nom (o carro : masculin).
Onde é que ___? | trabalhas | trabalhas tu / é trabalhas | Où est-ce que tu travailles ? | Après é que : l'ordre direct.
Já jantaste? — ___. | Já | Sim já / Jantaste | Tu as déjà dîné ? — Oui. | Já : oui (c'est fait).
""",
},
]


TUILES = {
"pronomen": {"sous_titre": "eu, me, mim, comigo, o meu", "options": [
    {"fiche": "pronomes", "titre": "Tu, você, o senhor", "desc": "À qui l'on parle — la fiche A1"},
    {"fiche": "pronomes-complemento", "titre": "Vi-o, dei-lhe", "desc": "Les pronoms compléments — la fiche A2"},
    {"fiche": "colocacao-pronominal", "titre": "Avant ou après le verbe ?", "desc": "chamo-me, não me chamo — la fiche B1"},
    {"fiche": "relativos", "titre": "Les relatifs", "desc": "que, quem, onde, cujo — la fiche B1"},
    serie("pronomesTonicosPtExercises", "pronomes-tonicos", "Mim, ti, comigo, connosco", "après une préposition · A1", "A1", "Mim, ti, comigo"),
    serie("possessivosTuilePtExercises", "possessivos-tuile", "O meu, a tua, dele, dela", "l'article devant le possessif · A1", "A1", "Les possessifs"),
    {"vocab": "startPronomenVokabular", "titre": "Vocabulaire · pronoms", "desc": "Les cartes des pronoms"},
    {"vocab": "startArtikelwoerterVokabular", "titre": "Vocabulaire · déterminants", "desc": "o, um, este, o meu, todo…"},
]},
"zahlen": {"sous_titre": "um, dois, primeiro, e meia", "options": [
    {"fiche": "numeros", "titre": "Comprendre les nombres", "desc": "L'heure, les prix, les dates — la fiche"},
    serie("horasDatasPtExercises", "horas-datas", "L'heure et les dates", "são duas e meia, às oito · A1", "A1", "L'heure et les dates"),
    serie("numerosConcordanciaPtExercises", "numeros-concordancia", "Accords, centaines, ordinaux", "duas, duzentas, o segundo, cem / cento · A2", "A2", "Accords et ordinaux"),
    {"vocab": "startZahlenVokabular", "titre": "Vocabulaire · nombres", "desc": "Les grands nombres et les ordinaux"},
]},
"praep": {"sous_titre": "em, de, a, por, para", "options": [
    {"fiche": "preposicoes", "titre": "Comprendre les prépositions", "desc": "no, na, do, da, ao, à — la fiche"},
    {"fiche": "contracoes", "titre": "No, na, do, da, ao, à", "desc": "Les contractions — la fiche A1"},
    {"fiche": "por-para", "titre": "Por ou para ?", "desc": "La fiche A2"},
    serie("prepContracoesPtExercises", "prep-contracoes", "Les contractions", "no Porto, à praia, pela ponte · A1", "A1", "Les contractions"),
    serie("prepLugarTempoPtExercises", "prep-lugar-tempo", "Le lieu et le temps", "há, desde, daqui a, debaixo de · A2", "A2", "Lieu et temps"),
    serie("verbosPrepPtExercises", "verbos-prep", "Verbes à préposition", "gostar de, pensar em, sonhar com · B1", "B1", "Verbes à préposition"),
    {"vocab": "startPraepVokabular", "titre": "Vocabulaire · prépositions", "desc": "Les cartes des prépositions"},
]},
"konjunktionen": {"sous_titre": "e, mas, porque, embora, quando", "options": [
    {"fiche": "conectores", "titre": "Comprendre les connecteurs", "desc": "aliás, ou seja, portanto — la fiche B2"},
    {"fiche": "conjuntivo-expressoes", "titre": "Embora, para que, antes que", "desc": "Le conjuntivo après une conjonction — la fiche B1"},
    {"fiche": "concessivas", "titre": "Embora, mesmo que, por mais que", "desc": "La concession — la fiche B2"},
    serie("porqueEmboraPtExercises", "porque-embora", "Porque ou embora ?", "et como, pois, apesar de · A2", "A2", "Porque ou embora"),
    serie("quandoEnquantoPtExercises", "quando-enquanto", "Quando, enquanto, assim que, até", "les liens du temps · B1", "B1", "Quando, enquanto"),
    serie("seCasoPtExercises", "se-caso", "Se, caso, desde que, a não ser que", "la condition · B1", "B1", "Se, caso"),
    {"vocab": "startKonjunktionenVokabular", "titre": "Vocabulaire · connecteurs", "desc": "Les cartes des conjonctions"},
    {"vocab": "startPartikelnVokabular", "titre": "Vocabulaire · mots de l'oral", "desc": "pois, olha, pronto, se calhar"},
]},
"wortstellung": {"sous_titre": "sujet, verbe, complément", "options": [
    {"fiche": "ordem-das-palavras", "titre": "Comprendre l'ordre des mots", "desc": "La fiche A2"},
    {"fiche": "perguntas", "titre": "Poser une question", "desc": "o que, onde, porquê — la fiche A1"},
    serie("ordemAdjetivoPtExercises", "ordem-adjetivo", "La place de l'adjectif", "um carro novo, um grande homem · A2", "A2", "La place de l'adjectif"),
    serie("negacaoPtExercises", "negacao", "La négation", "não… nada, nunca, nem, ninguém · A2", "A2", "La négation"),
    serie("perguntasOrdemPtExercises", "perguntas-ordem", "Les questions de l'oral", "onde é que…? — Gostei. · A2", "A2", "Les questions"),
    {"fiche": "realce", "titre": "Mettre en relief", "desc": "é que, foi… que — la fiche C1"},
]},
"adverbien": {"sous_titre": "sempre, bem, já, ainda", "options": [
    {"fiche": "adverbios", "titre": "Comprendre les adverbes", "desc": "-mente, bem, mal, aqui, ali — la fiche A2"},
    {"fiche": "ja-ainda", "titre": "Já, ainda, já não", "desc": "La fiche A2"},
    serie("adverbiosMentePtExercises", "adverbios-mente", "Former un adverbe en -mente", "rapidamente, felizmente, bem · A2", "A2", "Les adverbes en -mente"),
    serie("adverbiosFamiliaPtExercises", "adverbios-familia", "Temps, lieu, manière, quantité", "às vezes, ali, cá, demais · A2", "A2", "La famille des adverbes"),
    {"vocab": "openAdverbienVokabular", "titre": "Vocabulaire", "desc": "Les adverbes par niveau"},
    {"vocab": "startDicteeAdverbes", "titre": "Dictée", "desc": "Écouter et écrire"},
]},
# Pas de tuile sur la grille : ces options s'ajoutent au panneau des Noms.
"genero": {"sous_titre": "o ou a ?", "options": [
    {"fiche": "genero", "titre": "Les règles du genre", "desc": "-ção, -dade, -gem, -ema, -or : o ou a ?"},
    {"serie_fiche": "terminaisonsPtExercises", "titre": "Deviner le genre par la terminaison", "desc": "un nom jamais vu : o ou a ?"},
    serie("falsosAmigosTuilePtExercises", "falsos-amigos-tuile", "Les faux amis", "acordar, presunto, polvo, chato, fato… · A2", "A2", "Les faux amis"),
]},
}
