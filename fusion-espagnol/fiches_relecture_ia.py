# -*- coding: utf-8 -*-
"""Cinq fiches nees de la relecture par Gemini et ChatGPT (10 oct. 2026).

    python fusion-espagnol/fiches_relecture_ia.py

Les manques VERIFIES dans le corpus (le reste de leurs remarques existait
deja) : les periphrases (ir a + infinitif : le futur des debutants), les
nombres et l'heure, les demonstratifs et possessifs, les prepositions a / en
/ de (et le « a » devant une personne), les connecteurs du B1-B2.
Idempotent : une fiche deja presente est remplacee.
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "espanol", "datos", "grammaire.json")


def fe(fr, en):
    return {"fr": fr, "en": en}


FICHES = [
 {
  "id": "perifrasis",
  "titre": fe("Les périphrases verbales", "Verb phrases"),
  "resume": fe("ir a, estar + gérondif, acabar de…", "ir a, estar + gerund, acabar de…"),
  "regle": fe(
   "Un verbe conjugué, puis un infinitif ou un gérondif, pour dire <b>quand</b> ou <b>comment</b> se passe l'action. La plus utile : <b>ir a + infinitif</b>, le futur proche, exactement comme « aller + infinitif ».",
   "A conjugated verb plus an infinitive or a gerund, to say <b>when</b> or <b>how</b> something happens. The most useful: <b>ir a + infinitive</b>, the near future, just like « going to »."),
  "tableau": [
   ["ir a + inf.", fe("futur proche : aller faire", "near future: going to"), "Voy a llamar a mi madre."],
   ["estar + gérondif", fe("être en train de", "to be doing"), "Estoy comiendo."],
   ["acabar de + inf.", fe("venir de", "to have just"), "Acabo de llegar."],
   ["volver a + inf.", fe("refaire, de nouveau", "to do again"), "Vuelve a llover."],
   ["seguir + gérondif", fe("continuer à", "to keep on"), "Sigo estudiando español."],
   ["tener que + inf.", fe("devoir (obligation personnelle)", "to have to"), "Tengo que trabajar."],
   ["hay que + inf.", fe("il faut (en général)", "one has to"), "Hay que reservar."],
   ["dejar de + inf.", fe("arrêter de", "to stop doing"), "Dejé de fumar."],
   ["empezar a + inf.", fe("commencer à", "to start to"), "Empieza a hacer frío."]
  ],
  "exemples": [
   ["Mañana voy a estudiar.", fe("Demain, je vais étudier.", "Tomorrow I'm going to study.")],
   ["¿Qué estás haciendo? — Estoy cocinando.", fe("Qu'est-ce que tu fais ? — Je cuisine. (une action en cours)", "What are you doing? — I'm cooking. (an action in progress)")],
   ["Acabamos de cenar.", fe("Nous venons de dîner. (« venir de » se dit acabar de)", "We've just had dinner.")],
   ["No vuelvas a hacerlo.", fe("Ne refais pas ça.", "Don't do it again.")],
   ["Hay que llegar temprano.", fe("Il faut arriver tôt.", "You have to arrive early.")]
  ],
  "attention": fe(
   "« Je viens de manger » se dit <b>acabo de comer</b> : <b>venir de</b> ne veut dire que « venir de quelque part ». Le gérondif : -ar → <b>-ando</b>, -er / -ir → <b>-iendo</b> (comiendo, viviendo), avec quelques formes à retenir : <b>leyendo</b>, <b>durmiendo</b>, <b>pidiendo</b>, <b>diciendo</b>, <b>yendo</b>.",
   "The gerund: -ar → <b>-ando</b>, -er / -ir → <b>-iendo</b> (comiendo, viviendo), with a few to learn: <b>leyendo</b>, <b>durmiendo</b>, <b>pidiendo</b>, <b>diciendo</b>, <b>yendo</b>. And Spanish uses estar + gerund only for what is happening right now, never for the future: « I'm leaving tomorrow » is <b>me voy mañana</b>.")
 },
 {
  "id": "numeros-hora",
  "titre": fe("Les nombres et l'heure", "Numbers and telling the time"),
  "resume": fe("De 16 à un million, et quelle heure il est", "From 16 to a million, and what time it is"),
  "regle": fe(
   "De 16 à 29, un seul mot : <b>dieciséis</b>, <b>veintiuno</b>, <b>veintitrés</b>. À partir de 31, trois mots avec <b>y</b> : <b>treinta y uno</b>, <b>cuarenta y cinco</b>. Les centaines s'accordent avec le nom : <b>doscientas personas</b>.",
   "From 16 to 29, one word: <b>dieciséis</b>, <b>veintiuno</b>, <b>veintitrés</b>. From 31, three words with <b>y</b>: <b>treinta y uno</b>, <b>cuarenta y cinco</b>. Hundreds agree with the noun: <b>doscientas personas</b>."),
  "tableau": [
   ["16 – 19", fe("dieciséis, diecisiete, dieciocho, diecinueve", "dieciséis, diecisiete, dieciocho, diecinueve")],
   ["21 – 29", fe("veintiuno, veintidós, veintitrés… veintinueve", "veintiuno, veintidós, veintitrés… veintinueve")],
   ["31, 45…", fe("treinta y uno, cuarenta y cinco (avec y)", "treinta y uno, cuarenta y cinco (with y)")],
   ["100", fe("cien — mais ciento uno, ciento veinte", "cien — but ciento uno, ciento veinte")],
   ["200 – 900", fe("doscientos, trescientos, cuatrocientos, quinientos, seiscientos, setecientos, ochocientos, novecientos", "doscientos, trescientos, cuatrocientos, quinientos, seiscientos, setecientos, ochocientos, novecientos")],
   ["1 000", fe("mil (jamais « un mil ») · dos mil", "mil (never « un mil ») · dos mil")],
   ["1 000 000", fe("un millón, dos millones (+ de devant un nom)", "un millón, dos millones (+ de before a noun)")],
   ["l'heure", fe("¿Qué hora es? — Es la una. · Son las tres.", "¿Qué hora es? — Es la una. · Son las tres.")],
   ["y cuarto…", fe("y cuarto (et quart) · y media (et demie) · menos cuarto (moins le quart)", "y cuarto (quarter past) · y media (half past) · menos cuarto (quarter to)")]
  ],
  "exemples": [
   ["Son las tres y cuarto.", fe("Il est trois heures et quart.", "It's a quarter past three.")],
   ["Es la una y media.", fe("Il est une heure et demie. (es la una : au singulier, une seule heure)", "It's half past one. (es la una: singular, one hour)")],
   ["Son las ocho menos diez.", fe("Il est huit heures moins dix.", "It's ten to eight.")],
   ["Nací en mil novecientos noventa y cinco.", fe("Je suis né en 1995. (les années se disent comme un nombre)", "I was born in 1995. (years are said as a number)")],
   ["Cuesta ciento cincuenta euros.", fe("Ça coûte cent cinquante euros.", "It costs a hundred and fifty euros.")],
   ["Hay quinientas personas.", fe("Il y a cinq cents personnes. (quinientas : au féminin, avec personas)", "There are five hundred people. (quinientas: feminine, with personas)")]
  ],
  "attention": fe(
   "Trois centaines sont irrégulières : <b>quinientos</b> (500), <b>setecientos</b> (700), <b>novecientos</b> (900). <b>cien</b> devient <b>ciento</b> devant un autre nombre. <b>uno</b> devient <b>un</b> devant un nom masculin : <b>veintiún años</b>. Et « à trois heures » se dit <b>a las tres</b>.",
   "Three hundreds are irregular: <b>quinientos</b> (500), <b>setecientos</b> (700), <b>novecientos</b> (900). <b>cien</b> becomes <b>ciento</b> before another number. <b>uno</b> becomes <b>un</b> before a masculine noun: <b>veintiún años</b>. And « at three o'clock » is <b>a las tres</b>.")
 },
 {
  "id": "demostrativos-posesivos",
  "titre": fe("Démonstratifs et possessifs", "Demonstratives and possessives"),
  "resume": fe("este, ese, aquel ; mi, mío", "este, ese, aquel; mi, mío"),
  "regle": fe(
   "Trois démonstratifs selon la distance : <b>este</b> (près de moi), <b>ese</b> (près de toi), <b>aquel</b> (loin des deux). Le possessif a deux formes : devant le nom, <b>mi, tu, su</b> ; après le nom ou seul, <b>mío, tuyo, suyo</b>.",
   "Three demonstratives by distance: <b>este</b> (near me), <b>ese</b> (near you), <b>aquel</b> (far from both). Possessives have two forms: before the noun, <b>mi, tu, su</b>; after the noun or alone, <b>mío, tuyo, suyo</b>."),
  "tableau": [
   ["este, esta", fe("ce… -ci, près de moi (estos, estas)", "this, near me (estos, estas)"), "este libro, esta mesa"],
   ["ese, esa", fe("ce… -là, près de toi (esos, esas)", "that, near you (esos, esas)"), "esa silla"],
   ["aquel, aquella", fe("ce… -là-bas, loin (aquellos, aquellas)", "that, over there (aquellos, aquellas)"), "aquella montaña"],
   ["esto, eso, aquello", fe("neutres : une chose qu'on ne nomme pas", "neuter: something not named"), "¿Qué es esto?"],
   ["mi, tu, su", fe("devant le nom : mon, ton, son / votre (mis, tus, sus)", "before the noun: my, your, his / her / your (mis, tus, sus)"), "mi casa, tus amigos"],
   ["nuestro, vuestro", fe("notre, votre — s'accordent : nuestra casa", "our, your — they agree: nuestra casa"), "nuestra casa"],
   ["mío, tuyo, suyo", fe("après le nom, ou seul : le mien, le tien…", "after the noun, or alone: mine, yours…"), "Es mío. · un amigo mío"]
  ],
  "exemples": [
   ["Este libro es mío.", fe("Ce livre est à moi.", "This book is mine.")],
   ["¿Qué es eso?", fe("Qu'est-ce que c'est, ça ? (neutre : on ne sait pas ce que c'est)", "What's that? (neuter: we don't know what it is)")],
   ["Aquella casa es de mis abuelos.", fe("Cette maison-là, là-bas, est à mes grands-parents.", "That house over there belongs to my grandparents.")],
   ["Un amigo mío vive en Lima.", fe("Un de mes amis vit à Lima.", "A friend of mine lives in Lima.")],
   ["¿Es tu bolso? — No, el mío es negro.", fe("C'est ton sac ? — Non, le mien est noir.", "Is that your bag? — No, mine is black.")],
   ["Su casa es grande.", fe("Sa maison (ou : votre maison) est grande. (su = de él, de ella, de usted, de ellos)", "His / her / your house is big. (su = de él, de ella, de usted, de ellos)")]
  ],
  "attention": fe(
   "<b>su</b> est ambigu : de lui, d'elle, d'eux, ou de vous (usted). En cas de doute, on précise : <b>la casa de ella</b>. Les neutres <b>esto, eso, aquello</b> ne vont jamais devant un nom. Et pas d'article devant le possessif : <b>mi casa</b>, jamais <i>la mi casa</i>.",
   "<b>su</b> is ambiguous: his, her, their, or your (usted). If in doubt, be explicit: <b>la casa de ella</b>. The neuters <b>esto, eso, aquello</b> never go before a noun.")
 },
 {
  "id": "preposiciones",
  "titre": fe("a, en, de : les prépositions de base", "a, en, de: the basic prepositions"),
  "resume": fe("Et le a devant une personne", "And the a before a person"),
  "regle": fe(
   "<b>a</b> marque la direction (voy a Madrid) et l'heure (a las tres). <b>en</b> marque le lieu où l'on est (estoy en Madrid) et le moyen de transport (en tren). <b>de</b> marque l'origine, la matière, l'appartenance (soy de Lyon, una mesa de madera, el libro de Ana). Et un <b>a</b> sans équivalent en français : devant une personne complément direct.",
   "<b>a</b> marks direction (voy a Madrid) and time (a las tres). <b>en</b> marks where you are (estoy en Madrid) and transport (en tren). <b>de</b> marks origin, material, ownership (soy de Lyon, una mesa de madera, el libro de Ana). And a special <b>a</b> before a person who is the direct object."),
  "tableau": [
   ["a", fe("direction, heure, « à » quelqu'un", "direction, time, « to » someone"), "Voy a casa. · A las ocho."],
   ["a (personnel)", fe("devant une personne, complément direct", "before a person as direct object"), "Veo a María. · Busco a mi hijo."],
   ["en", fe("lieu où l'on est, transport, moment", "where you are, transport, time"), "Estoy en casa. · Voy en tren. · En verano."],
   ["de", fe("origine, matière, possession, contenu", "origin, material, ownership, contents"), "Soy de Lyon. · un vaso de agua"],
   ["al · del", fe("a + el, de + el : toujours contractés", "a + el, de + el: always contracted"), "Voy al cine. · Vengo del trabajo."],
   ["con · sin", fe("avec · sans", "with · without"), "café con leche · sin azúcar"]
  ],
  "exemples": [
   ["Veo a mi hermana todos los días.", fe("Je vois ma sœur tous les jours. (a devant une personne)", "I see my sister every day. (a before a person)")],
   ["Veo la televisión.", fe("Je regarde la télévision. (une chose : pas de a)", "I watch television. (a thing: no a)")],
   ["Voy a Madrid en tren.", fe("Je vais à Madrid en train.", "I'm going to Madrid by train.")],
   ["Estoy en Madrid.", fe("Je suis à Madrid. (là où l'on est : en, pas a)", "I'm in Madrid. (where you are: en, not a)")],
   ["Llegamos a las nueve.", fe("Nous arrivons à neuf heures.", "We arrive at nine.")],
   ["Es un vaso de agua.", fe("C'est un verre d'eau.", "It's a glass of water.")]
  ],
  "attention": fe(
   "Le grand piège : « je suis à Madrid » se dit <b>estoy en Madrid</b> ; <b>a</b> ne sert qu'avec un mouvement (voy a Madrid). Et le <b>a</b> devant une personne n'a pas d'équivalent en français : <b>conozco a tu padre</b>, <b>llamo a mi madre</b> — mais <b>tengo dos hermanos</b> (tener ne le prend pas).",
   "The trap: the <b>a</b> before a person has no equivalent in English: <b>conozco a tu padre</b>, <b>llamo a mi madre</b> — but <b>tengo dos hermanos</b> (tener doesn't take it). And « in » + a city is <b>en</b>: <b>estoy en Madrid</b>; <b>a</b> is only for movement.")
 },
 {
  "id": "conectores",
  "titre": fe("Les connecteurs", "Linking words"),
  "resume": fe("Relier ses idées, du B1 au B2", "Linking ideas, from B1 to B2"),
  "regle": fe(
   "Pour passer de phrases juxtaposées à un discours qui s'enchaîne : ajouter, opposer, concéder, expliquer une cause, tirer une conséquence, poser une condition.",
   "To move from separate sentences to connected speech: adding, contrasting, conceding, giving a cause, drawing a conclusion, setting a condition."),
  "tableau": [
   ["ajouter", fe("además, también, incluso", "además, también, incluso"), "Además, es barato."],
   ["opposer", fe("pero, sin embargo, en cambio, no obstante", "pero, sin embargo, en cambio, no obstante"), "Es caro; sin embargo, vale la pena."],
   ["concéder", fe("aunque, a pesar de (que)", "aunque, a pesar de (que)"), "Aunque llueve, salgo."],
   ["cause", fe("porque, como, ya que, dado que", "porque, como, ya que, dado que"), "Como no tenía dinero, no fui."],
   ["conséquence", fe("así que, por eso, por lo tanto, por consiguiente", "así que, por eso, por lo tanto, por consiguiente"), "Estaba cansado, así que me fui."],
   ["organiser", fe("por un lado… por otro lado, en primer lugar, en definitiva", "por un lado… por otro lado, en primer lugar, en definitiva"), "Por un lado…, por otro lado…"],
   ["condition", fe("si, a menos que, siempre que", "si, a menos que, siempre que"), "Iré, a menos que llueva."]
  ],
  "exemples": [
   ["Como estaba cansado, me fui a casa.", fe("Comme j'étais fatigué, je suis rentré. (como en tête de phrase : la cause)", "As I was tired, I went home. (como at the start: the cause)")],
   ["Es caro; sin embargo, merece la pena.", fe("C'est cher ; pourtant, ça vaut la peine.", "It's expensive; however, it's worth it.")],
   ["Aunque llueva, saldremos.", fe("Même s'il pleut, nous sortirons. (aunque + subjonctif : une hypothèse)", "Even if it rains, we'll go out. (aunque + subjunctive: a hypothesis)")],
   ["Iremos a la playa, a menos que haga frío.", fe("Nous irons à la plage, à moins qu'il fasse froid.", "We'll go to the beach, unless it's cold.")],
   ["Por un lado es útil; por otro, es caro.", fe("D'un côté, c'est utile ; de l'autre, c'est cher.", "On the one hand it's useful; on the other, it's expensive.")]
  ],
  "attention": fe(
   "<b>aunque</b> + indicatif constate un fait (<b>aunque llueve</b> : bien qu'il pleuve — et il pleut) ; + subjonctif, il envisage une hypothèse (<b>aunque llueva</b> : même s'il pleut). Et <b>a menos que</b>, <b>siempre que</b> (pourvu que), <b>para que</b> veulent toujours le subjonctif.",
   "<b>aunque</b> + indicative states a fact (<b>aunque llueve</b>: although it is raining); + subjunctive, a hypothesis (<b>aunque llueva</b>: even if it rains). And <b>a menos que</b>, <b>siempre que</b> (provided that), <b>para que</b> always take the subjunctive.")
 }
]


EXERCICES = {"perifrasis": "startPerifrasisUebung", "numeros-hora": "startNumerosUebung",
             "demostrativos-posesivos": "startDemostrativosUebung", "preposiciones": "startPreposicionesUebung"}


def main():
    d = json.load(io.open(CHEMIN, encoding="utf-8"))
    ids = {f["id"] for f in FICHES}
    # Le bouton « M'entrainer » de quatre fiches (11 oct. 2026) : les jeux
    # viennent de exos_fiches.py. Sans cette ligne, relancer ce script-ci
    # effacerait le bouton.
    for f in FICHES:
        if f["id"] in EXERCICES:
            f["exercice"] = EXERCICES[f["id"]]
    d["fiches"] = [f for f in d["fiches"] if f["id"] not in ids] + FICHES
    io.open(CHEMIN, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("fiches :", ", ".join(f["id"] for f in d["fiches"]))


if __name__ == "__main__":
    main()
