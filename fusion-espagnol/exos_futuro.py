# -*- coding: utf-8 -*-
"""Le futur et le conditionnel de l'espagnol : la fiche et deux jeux.

    python fusion-espagnol/exos_futuro.py

Le plus gros manque releve par la relecture de Gemini (10 oct. 2026), et
verifie : ni fiche, ni exercice, et verbos.json n'a meme pas ces deux temps.

LES FORMES SONT CALCULEES, PAS RECOPIEES. Le futur et le conditionnel sont
les temps les plus reguliers de l'espagnol : l'infinitif ENTIER + une
terminaison, la meme pour -ar, -er, -ir. Seuls douze verbes (et leurs
composes) changent de radical. conjuguer() le fait, et VERIFS controle les
cas qui piegeraient une regle trop simple (reir, obtener, bendecir...).

Meme format et memes regles d'ecriture que exos_temps.py : un declencheur
par phrase, une vraie traduction, la personne dans l'indice.
"""
import io, json, os, unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
PERSONNES = {1: (0, "yo"), 2: (1, "tú"), 3: (2, "él, ella"), 4: (3, "nosotros"), 6: (5, "ellos, ellas")}
FUT = ["é", "ás", "á", "emos", "éis", "án"]
COND = ["ía", "ías", "ía", "íamos", "íais", "ían"]
PRONOMS = ["me", "te", "se", "nos", "os", "se"]
# Radicaux irreguliers : par la FIN de l'infinitif, pour attraper les
# composes (obtener, proponer, convenir, deshacer). decir et querer seuls :
# bendecir et maldecir sont reguliers (bendeciré).
IRREG_FIN = [("tener", "tendr"), ("poner", "pondr"), ("venir", "vendr"), ("salir", "saldr"),
             ("valer", "valdr"), ("poder", "podr"), ("saber", "sabr"), ("caber", "cabr"),
             ("haber", "habr"), ("hacer", "har")]
IRREG_EXACT = {"decir": "dir", "querer": "querr", "satisfacer": "satisfar"}


def sans_accent_final(inf):
    # reír, oír, freír : l'accent de l'infinitif tombe (reiré, oiría).
    if inf.endswith("ír"):
        return inf[:-2] + "ir"
    return inf


def conjuguer(inf, temps):
    pron = inf.endswith("se") and inf[-4:-2] in ("ar", "er", "ir", "ír")
    base = inf[:-2] if pron else inf
    radical = IRREG_EXACT.get(base)
    if not radical:
        for fin, r in IRREG_FIN:
            if base.endswith(fin):
                radical = base[: -len(fin)] + r
                break
    if not radical:
        radical = sans_accent_final(base)
    fins = FUT if temps == "futuro" else COND
    formes = [radical + f for f in fins]
    return [p + " " + f for p, f in zip(PRONOMS, formes)] if pron else formes


VERIFS = {
    ("hablar", "futuro"): "hablaré hablarás hablará hablaremos hablaréis hablarán",
    ("comer", "condicional"): "comería comerías comería comeríamos comeríais comerían",
    ("tener", "futuro"): "tendré tendrás tendrá tendremos tendréis tendrán",
    ("decir", "condicional"): "diría dirías diría diríamos diríais dirían",
    ("hacer", "futuro"): "haré harás hará haremos haréis harán",
    ("querer", "futuro"): "querré querrás querrá querremos querréis querrán",
    ("obtener", "futuro"): "obtendré obtendrás obtendrá obtendremos obtendréis obtendrán",
    ("reír", "futuro"): "reiré reirás reirá reiremos reiréis reirán",
    ("bendecir", "futuro"): "bendeciré bendecirás bendecirá bendeciremos bendeciréis bendecirán",
    ("levantarse", "futuro"): "me levantaré te levantarás se levantará nos levantaremos os levantaréis se levantarán",
    ("salir", "condicional"): "saldría saldrías saldría saldríamos saldríais saldrían",
    ("poder", "condicional"): "podría podrías podría podríamos podríais podrían",
}

FICHE = {
 "id": "futuro-condicional",
 "titre": {"fr": "Le futur et le conditionnel", "en": "The future and the conditional"},
 "resume": {"fr": "L'infinitif entier, plus une terminaison", "en": "The whole infinitive, plus an ending"},
 "regle": {
  "fr": "Pas de radical à chercher : on garde l'<b>infinitif entier</b> et on ajoute <b>-é, -ás, -á, -emos, -éis, -án</b> (futur) ou <b>-ía, -ías, -ía, -íamos, -íais, -ían</b> (conditionnel), les mêmes pour -ar, -er et -ir. Comme en français : « je parlerai », <b>hablaré</b> ; « je parlerais », <b>hablaría</b>.",
  "en": "No stem to find: keep the <b>whole infinitive</b> and add <b>-é, -ás, -á, -emos, -éis, -án</b> (future) or <b>-ía, -ías, -ía, -íamos, -íais, -ían</b> (conditional), the same for -ar, -er and -ir: <b>hablaré</b> (I will speak), <b>hablaría</b> (I would speak)."},
 "tableau": [
  ["", {"fr": "futur · conditionnel", "en": "future · conditional"}],
  ["yo", {"fr": "hablaré · hablaría", "en": "hablaré · hablaría"}],
  ["tú", {"fr": "hablarás · hablarías", "en": "hablarás · hablarías"}],
  ["él, ella, usted", {"fr": "hablará · hablaría", "en": "hablará · hablaría"}],
  ["nosotros", {"fr": "hablaremos · hablaríamos", "en": "hablaremos · hablaríamos"}],
  ["vosotros (Espagne)", {"fr": "hablaréis · hablaríais", "en": "hablaréis · hablaríais"}],
  ["ellos, ustedes", {"fr": "hablarán · hablarían", "en": "hablarán · hablarían"}],
  ["irréguliers", {"fr": "tener → tendr-, poner → pondr-, salir → saldr-, venir → vendr-, poder → podr-, saber → sabr-, querer → querr-, haber → habr-, decir → dir-, hacer → har-",
                   "en": "tener → tendr-, poner → pondr-, salir → saldr-, venir → vendr-, poder → podr-, saber → sabr-, querer → querr-, haber → habr-, decir → dir-, hacer → har-"},
   "tendré · haría · diremos"]
 ],
 "exemples": [
  ["Mañana lloverá.", {"fr": "Demain, il pleuvra.", "en": "It will rain tomorrow."}],
  ["Te llamaré cuando llegue.", {"fr": "Je t'appellerai quand j'arriverai. (après cuando, le subjonctif : jamais « cuando llegaré »)", "en": "I'll call you when I arrive. (after cuando, the subjunctive: never « cuando llegaré »)"}],
  ["¿Podrías ayudarme?", {"fr": "Pourrais-tu m'aider ? (le conditionnel adoucit une demande, comme en français)", "en": "Could you help me? (the conditional softens a request)"}],
  ["Yo que tú, hablaría con ella.", {"fr": "À ta place, je lui parlerais.", "en": "If I were you, I'd talk to her."}],
  ["Si tuviera tiempo, viajaría más.", {"fr": "Si j'avais le temps, je voyagerais plus. (après si : le subjonctif imparfait, jamais le conditionnel)", "en": "If I had time, I'd travel more. (after si: the imperfect subjunctive, never the conditional)"}],
  ["¿Dónde estará Juan? — Estará en casa.", {"fr": "Où peut bien être Juan ? — Il doit être chez lui. (le futur sert aussi à supposer)", "en": "Where can Juan be? — He's probably at home. (the future also expresses a guess)"}]
 ],
 "attention": {
  "fr": "Après <b>si</b>, jamais le futur ni le conditionnel : <b>si llueve, no iré</b> ; <b>si lloviera, no iría</b>. Et pour un projet, l'oral préfère souvent le futur proche <b>voy a + infinitif</b> : <b>voy a viajar a México</b>.",
  "en": "After <b>si</b>, never the future or the conditional: <b>si llueve, no iré</b>; <b>si lloviera, no iría</b>. And for plans, speech often prefers <b>voy a + infinitive</b>: <b>voy a viajar a México</b>."},
 "exercice": "startFuturoExercise"
}

FUTURO = [
 ("Mañana ___ a mis abuelos.", "visitar", 1, "Demain, je rendrai visite à mes grands-parents.", "Tomorrow I'll visit my grandparents.", "moment"),
 ("El año que viene ___ en Barcelona.", "vivir", 4, "L'année prochaine, nous vivrons à Barcelone.", "Next year we'll live in Barcelona.", "moment"),
 ("¿Qué ___ este fin de semana?", "hacer", 2, "Que feras-tu ce week-end ?", "What will you do this weekend?", "moment"),
 ("Te lo prometo: ___ a tiempo.", "llegar", 1, "Je te le promets : j'arriverai à l'heure.", "I promise: I'll be on time.", "promesse"),
 ("La semana que viene ___ el examen.", "tener", 4, "La semaine prochaine, nous aurons l'examen.", "Next week we'll have the exam.", "moment"),
 ("Dentro de dos horas ___ la película.", "empezar", 3, "Le film commencera dans deux heures.", "The film will start in two hours.", "moment"),
 ("Mañana ___ sol en todo el país.", "hacer", 3, "Demain, il fera beau dans tout le pays.", "Tomorrow it'll be sunny across the country.", "prevision"),
 ("En 2050 los robots ___ muchas tareas de casa.", "hacer", 6, "En 2050, les robots feront beaucoup de tâches ménagères.", "In 2050 robots will do lots of housework.", "prevision"),
 ("El próximo verano ___ a Perú.", "ir", 4, "L'été prochain, nous irons au Pérou.", "Next summer we'll go to Peru.", "moment"),
 ("Mañana te ___ la verdad.", "decir", 1, "Demain, je te dirai la vérité.", "Tomorrow I'll tell you the truth.", "moment"),
 ("No te preocupes, ___ todo lo posible.", "hacer", 1, "Ne t'inquiète pas, je ferai tout mon possible.", "Don't worry, I'll do everything I can.", "promesse"),
 ("¿___ venir a la cena del sábado?", "poder", 2, "Tu pourras venir au dîner de samedi ?", "Will you be able to come to dinner on Saturday?", "moment"),
 ("Mañana ___ las fotos en la web.", "poner", 1, "Demain, je mettrai les photos sur le site.", "Tomorrow I'll put the photos on the website.", "moment"),
 ("Esta noche ___ tarde del trabajo.", "salir", 1, "Ce soir, je sortirai tard du travail.", "Tonight I'll leave work late.", "moment"),
 ("Mis primos ___ en Navidad.", "venir", 6, "Mes cousins viendront à Noël.", "My cousins will come at Christmas.", "moment"),
 ("Pronto ___ los resultados.", "saber", 4, "Bientôt, nous connaîtrons les résultats.", "We'll soon know the results.", "moment"),
 ("El mes que viene ___ treinta años.", "tener", 1, "Le mois prochain, j'aurai trente ans.", "Next month I'll be thirty.", "moment"),
 ("¿Cuánto ___ el viaje del año que viene?", "costar", 3, "Combien coûtera le voyage de l'année prochaine ?", "How much will next year's trip cost?", "moment"),
 ("Algún día ___ a hablar español perfectamente.", "aprender", 1, "Un jour, j'apprendrai à parler espagnol parfaitement.", "One day I'll learn to speak Spanish perfectly.", "moment"),
 ("Mañana ___ en la playa todo el día.", "estar", 4, "Demain, nous serons à la plage toute la journée.", "Tomorrow we'll be at the beach all day.", "moment"),
 ("Después de clase ___ la cena.", "preparar", 1, "Après les cours, je préparerai le dîner.", "After class I'll make dinner.", "moment"),
 ("Te ___ en cuanto llegue.", "llamar", 1, "Je t'appellerai dès que j'arriverai.", "I'll call you as soon as I arrive.", "cuando"),
 ("Si estudias, ___ buenas notas.", "tener", 2, "Si tu étudies, tu auras de bonnes notes.", "If you study, you'll get good marks.", "si"),
 ("Si llueve, no ___ a la playa.", "ir", 4, "S'il pleut, nous n'irons pas à la plage.", "If it rains, we won't go to the beach.", "si"),
 ("Si me ayudas, ___ antes.", "terminar", 4, "Si tu m'aides, nous finirons plus tôt.", "If you help me, we'll finish sooner.", "si"),
 ("Creo que mañana ___.", "llover", 3, "Je crois qu'il pleuvra demain.", "I think it'll rain tomorrow.", "prevision"),
 ("Seguro que lo ___ muy bien en la entrevista.", "hacer", 2, "Je suis sûr que tu t'en sortiras très bien à l'entretien.", "I'm sure you'll do very well in the interview.", "prevision"),
 ("El año que viene mi hermana ___ la universidad.", "empezar", 3, "L'année prochaine, ma sœur commencera l'université.", "Next year my sister will start university.", "moment"),
 ("¿Dónde ___ Juan a estas horas?", "estar", 3, "Où peut bien être Juan à cette heure-ci ?", "Where can Juan be at this time?", "supposition"),
 ("No sé qué hora es; ___ las once.", "ser", 6, "Je ne sais pas quelle heure il est ; il doit être onze heures.", "I don't know what time it is; it must be about eleven.", "supposition"),
 ("Tu padre ___ unos cincuenta años, ¿no?", "tener", 3, "Ton père doit avoir dans les cinquante ans, non ?", "Your father must be about fifty, right?", "supposition"),
 ("Mañana ___ el autobús de las seis.", "tomar", 1, "Demain, je prendrai le bus de six heures.", "Tomorrow I'll take the six o'clock bus.", "moment"),
 ("La próxima vez ___ más cuidado.", "tener", 1, "La prochaine fois, je ferai plus attention.", "Next time I'll be more careful.", "moment"),
 ("En el futuro los humanos ___ en Marte.", "vivir", 6, "À l'avenir, les humains vivront sur Mars.", "In the future humans will live on Mars.", "prevision"),
 ("El sábado ___ una fiesta en mi casa.", "hacer", 4, "Samedi, nous ferons une fête chez moi.", "On Saturday we'll have a party at my place.", "moment"),
 ("Mañana ___ de compras con mi madre.", "ir", 1, "Demain, j'irai faire les courses avec ma mère.", "Tomorrow I'll go shopping with my mother.", "moment"),
 ("¿Me ___ con la mudanza?", "ayudar", 2, "Tu m'aideras pour le déménagement ?", "Will you help me with the move?", "moment"),
 ("Dentro de un año ___ hablar con fluidez.", "poder", 2, "Dans un an, tu pourras parler couramment.", "In a year you'll be able to speak fluently.", "moment"),
 ("Esta tarde ___ mis amigos.", "venir", 6, "Cet après-midi, mes amis viendront.", "My friends will come this afternoon.", "moment"),
 ("Mañana no ___ tiempo.", "tener", 1, "Demain, je n'aurai pas le temps.", "I won't have time tomorrow.", "moment"),
 ("Te ___ un mensaje cuando salga.", "mandar", 1, "Je t'enverrai un message quand je partirai.", "I'll send you a message when I leave.", "cuando"),
 ("El próximo lunes ___ a trabajar.", "volver", 1, "Lundi prochain, je reprendrai le travail.", "Next Monday I'll go back to work.", "moment"),
 ("Algún día ___ la verdad.", "saber", 2, "Un jour, tu sauras la vérité.", "One day you'll know the truth.", "moment"),
 ("No ___ nada a nadie, te lo juro.", "decir", 1, "Je ne dirai rien à personne, je te le jure.", "I won't tell anyone, I swear.", "promesse"),
 ("Este verano ___ mucho calor, según la tele.", "hacer", 3, "Cet été, il fera très chaud, d'après la télé.", "It'll be very hot this summer, according to the TV.", "prevision"),
 ("Mañana ___ la habitación, lo prometo.", "limpiar", 1, "Demain, je rangerai la chambre, c'est promis.", "I'll clean my room tomorrow, I promise.", "promesse"),
 ("Dentro de poco ___ las vacaciones.", "empezar", 6, "Les vacances commenceront bientôt.", "The holidays will start soon.", "moment"),
 ("¿___ tiempo para tomar un café mañana?", "tener", 2, "Tu auras le temps de prendre un café demain ?", "Will you have time for a coffee tomorrow?", "moment"),
 ("La semana que viene ___ la casa nueva.", "ver", 4, "La semaine prochaine, nous verrons la nouvelle maison.", "Next week we'll see the new house.", "moment"),
 ("Cuando seas mayor, lo ___.", "entender", 2, "Quand tu seras grand, tu comprendras.", "When you're older, you'll understand.", "cuando"),
 ("Si vienes, ___ paella.", "cocinar", 1, "Si tu viens, je cuisinerai une paella.", "If you come, I'll make paella.", "si"),
 ("Mañana ___ veinte grados.", "hacer", 3, "Demain, il fera vingt degrés.", "It'll be twenty degrees tomorrow.", "prevision"),
 ("Supongo que ___ cansado después del viaje.", "estar", 2, "Je suppose que tu seras fatigué après le voyage.", "I suppose you'll be tired after the trip.", "supposition"),
 ("El año próximo ___ dos idiomas nuevos.", "estudiar", 1, "L'année prochaine, j'étudierai deux nouvelles langues.", "Next year I'll study two new languages.", "moment"),
 ("Mañana les ___ la noticia a mis padres.", "dar", 1, "Demain, j'annoncerai la nouvelle à mes parents.", "Tomorrow I'll break the news to my parents.", "moment"),
 ("Pronto ___ el invierno.", "llegar", 3, "L'hiver arrivera bientôt.", "Winter will soon be here.", "moment"),
 ("¿Para cuándo ___ el informe?", "terminar", 2, "Pour quand auras-tu fini le rapport ?", "When will you finish the report?", "moment"),
 ("Nunca ___ este viaje.", "olvidar", 1, "Je n'oublierai jamais ce voyage.", "I'll never forget this trip.", "promesse"),
 ("Mañana ___ a correr al parque.", "salir", 4, "Demain, nous sortirons courir au parc.", "Tomorrow we'll go out for a run in the park.", "moment"),
 ("Dentro de diez años, ¿dónde ___?", "vivir", 2, "Dans dix ans, où vivras-tu ?", "In ten years, where will you be living?", "moment"),
]

# (phrase, infinitif, personne, fr, en, cle, options) -- options : « sujet »
# remplace l'etiquette de personne (me gustaria), « aussi » ajoute une autre
# reponse juste (querria / quisiera).
CONDICIONAL = [
 ("¿___ abrir la ventana, por favor?", "poder", 2, "Pourrais-tu ouvrir la fenêtre, s'il te plaît ?", "Could you open the window, please?", "politesse", {}),
 ("___ un café, por favor.", "querer", 1, "Je voudrais un café, s'il vous plaît.", "I'd like a coffee, please.", "politesse", {"aussi": ["quisiera"]}),
 ("¿Te ___ ayudarme un momento?", "importar", 3, "Ça te dérangerait de m'aider un moment ?", "Would you mind helping me for a moment?", "politesse", {"sujet": "te … : 3e personne"}),
 ("¿___ usted repetir, por favor?", "poder", 3, "Pourriez-vous répéter, s'il vous plaît ?", "Could you repeat that, please?", "politesse", {"sujet": "usted"}),
 ("Yo que tú, ___ con ella.", "hablar", 1, "À ta place, je lui parlerais.", "If I were you, I'd talk to her.", "conseil", {}),
 ("Yo en tu lugar, no lo ___.", "hacer", 1, "À ta place, je ne le ferais pas.", "In your place, I wouldn't do it.", "conseil", {}),
 ("___ descansar más.", "deber", 2, "Tu devrais te reposer davantage.", "You should rest more.", "conseil", {}),
 ("Con más dinero, ___ por todo el mundo.", "viajar", 1, "Avec plus d'argent, je voyagerais dans le monde entier.", "With more money, I'd travel all over the world.", "hypothese", {}),
 ("Si tuviera tiempo, ___ un libro.", "escribir", 1, "Si j'avais le temps, j'écrirais un livre.", "If I had time, I'd write a book.", "si", {}),
 ("Si fuera rico, ___ una casa en la playa.", "comprar", 1, "Si j'étais riche, j'achèterais une maison à la plage.", "If I were rich, I'd buy a house by the beach.", "si", {}),
 ("Si pudiera, ___ en Madrid.", "vivir", 1, "Si je pouvais, je vivrais à Madrid.", "If I could, I'd live in Madrid.", "si", {}),
 ("Si hablaras más despacio, te ___ mejor.", "entender", 1, "Si tu parlais plus lentement, je te comprendrais mieux.", "If you spoke more slowly, I'd understand you better.", "si", {}),
 ("Si no lloviera, ___ a la playa.", "ir", 4, "S'il ne pleuvait pas, nous irions à la plage.", "If it weren't raining, we'd go to the beach.", "si", {}),
 ("Si tuvieras hambre, ¿qué ___?", "comer", 2, "Si tu avais faim, qu'est-ce que tu mangerais ?", "If you were hungry, what would you eat?", "si", {}),
 ("Dijo que ___ a las ocho.", "venir", 3, "Il a dit qu'il viendrait à huit heures.", "He said he would come at eight.", "futurpasse", {}),
 ("Me prometiste que me ___.", "llamar", 2, "Tu m'avais promis que tu m'appellerais.", "You promised you'd call me.", "futurpasse", {}),
 ("Pensaba que ___ más caro.", "ser", 3, "Je pensais que ce serait plus cher.", "I thought it would be more expensive.", "futurpasse", {}),
 ("Sabía que lo ___.", "entender", 2, "Je savais que tu comprendrais.", "I knew you'd understand.", "futurpasse", {}),
 ("Cuando llegué, ___ las diez.", "ser", 6, "Quand je suis arrivé, il devait être dix heures.", "When I arrived, it must have been about ten.", "supposition", {}),
 ("No contestó; ___ dormido.", "estar", 3, "Il n'a pas répondu ; il devait dormir.", "He didn't answer; he must have been asleep.", "supposition", {}),
 ("Me ___ conocer México.", "gustar", 3, "J'aimerais connaître le Mexique.", "I'd like to see Mexico.", "politesse", {"sujet": "me … : 3e personne"}),
 ("¿Qué ___ tú en mi lugar?", "hacer", 2, "Qu'est-ce que tu ferais à ma place ?", "What would you do in my place?", "conseil", {}),
 ("Sin ti, no ___ terminar el proyecto.", "poder", 1, "Sans toi, je ne pourrais pas finir le projet.", "Without you, I couldn't finish the project.", "hypothese", {}),
 ("Yo que tú, ___ antes.", "salir", 1, "À ta place, je partirais plus tôt.", "If I were you, I'd leave earlier.", "conseil", {}),
 ("¿___ ustedes esperar un momento?", "poder", 6, "Pourriez-vous attendre un moment ?", "Could you wait a moment?", "politesse", {"sujet": "ustedes"}),
 ("En tu lugar, yo ___ la verdad.", "decir", 1, "À ta place, je dirais la vérité.", "In your place, I'd tell the truth.", "conseil", {}),
 ("Si tuviera un perro, lo ___ al parque todos los días.", "llevar", 1, "Si j'avais un chien, je l'emmènerais au parc tous les jours.", "If I had a dog, I'd take it to the park every day.", "si", {}),
 ("Si ganara la lotería, no ___ más.", "trabajar", 1, "Si je gagnais au loto, je ne travaillerais plus.", "If I won the lottery, I wouldn't work any more.", "si", {}),
 ("Si vivieras aquí, ___ el mar todos los días.", "ver", 2, "Si tu vivais ici, tu verrais la mer tous les jours.", "If you lived here, you'd see the sea every day.", "si", {}),
 ("Me dijeron que ___ un poco tarde.", "llegar", 6, "Ils m'ont dit qu'ils arriveraient un peu en retard.", "They told me they'd be a bit late.", "futurpasse", {}),
 ("Creía que ___ más tiempo.", "tener", 4, "Je croyais que nous aurions plus de temps.", "I thought we'd have more time.", "futurpasse", {}),
 ("¿Me ___ la sal, por favor?", "pasar", 2, "Tu me passerais le sel, s'il te plaît ?", "Would you pass me the salt, please?", "politesse", {}),
 ("___ mejor salir temprano.", "ser", 3, "Il vaudrait mieux partir tôt.", "It would be better to leave early.", "conseil", {}),
 ("Con un poco de suerte, ___ a tiempo.", "llegar", 4, "Avec un peu de chance, nous arriverions à l'heure.", "With a bit of luck, we'd arrive on time.", "hypothese", {}),
 ("Si supiera cocinar, ___ para todos.", "cocinar", 1, "Si je savais cuisiner, je cuisinerais pour tout le monde.", "If I could cook, I'd cook for everyone.", "si", {}),
 ("Si me lo pidieras, te ___.", "ayudar", 1, "Si tu me le demandais, je t'aiderais.", "If you asked me, I'd help you.", "si", {}),
 ("Nos aseguró que ___ todo.", "pagar", 3, "Il nous a assuré qu'il paierait tout.", "He assured us he'd pay for everything.", "futurpasse", {}),
 ("Ella sabía que el examen ___ difícil.", "ser", 3, "Elle savait que l'examen serait difficile.", "She knew the exam would be hard.", "futurpasse", {}),
 ("¿Qué ___ de mí sin ti?", "ser", 3, "Que deviendrais-je sans toi ?", "What would become of me without you?", "hypothese", {}),
 ("Yo no ___ eso.", "decir", 1, "Moi, je ne dirais pas ça.", "I wouldn't say that.", "conseil", {}),
 ("Si yo fuera tú, ___ al médico.", "ir", 1, "Si j'étais toi, j'irais chez le médecin.", "If I were you, I'd go to the doctor.", "si", {}),
 ("En ese caso, ___ que cambiar el plan.", "tener", 4, "Dans ce cas, nous devrions changer le plan.", "In that case, we'd have to change the plan.", "hypothese", {}),
 ("¿___ un café conmigo?", "tomar", 2, "Tu prendrais un café avec moi ?", "Would you have a coffee with me?", "politesse", {}),
 ("Me ___ saber la verdad.", "gustar", 3, "J'aimerais savoir la vérité.", "I'd like to know the truth.", "politesse", {"sujet": "me … : 3e personne"}),
 ("Si no tuviera que trabajar, ___ todo el día.", "dormir", 1, "Si je ne devais pas travailler, je dormirais toute la journée.", "If I didn't have to work, I'd sleep all day.", "si", {}),
 ("Prometió que ___ más.", "estudiar", 3, "Il a promis qu'il étudierait davantage.", "He promised he'd study more.", "futurpasse", {}),
 ("Imaginé que ___ en casa.", "estar", 2, "J'imaginais que tu serais à la maison.", "I imagined you'd be at home.", "futurpasse", {}),
 ("Si estuviéramos en verano, ___ en el río.", "nadar", 4, "Si c'était l'été, nous nagerions dans la rivière.", "If it were summer, we'd swim in the river.", "si", {}),
 ("¿Me ___ decir la hora?", "poder", 3, "Pourriez-vous me dire l'heure ?", "Could you tell me the time?", "politesse", {"sujet": "usted"}),
 ("Yo que tú, no ___ tanto.", "comer", 1, "À ta place, je ne mangerais pas autant.", "If I were you, I wouldn't eat so much.", "conseil", {}),
 ("Si tuviéramos más tiempo, ___ el museo.", "visitar", 4, "Si nous avions plus de temps, nous visiterions le musée.", "If we had more time, we'd visit the museum.", "si", {}),
 ("Con este tiempo, ___ genial ir a la playa.", "ser", 3, "Avec ce temps, ce serait génial d'aller à la plage.", "With this weather, it'd be great to go to the beach.", "hypothese", {}),
 ("Si me quisieras, me lo ___.", "decir", 2, "Si tu m'aimais, tu me le dirais.", "If you loved me, you'd tell me.", "si", {}),
 ("Nos dijo que ___ la casa.", "vender", 3, "Il nous a dit qu'il vendrait la maison.", "He told us he'd sell the house.", "futurpasse", {}),
 ("Si fuera más joven, ___ a bailar.", "aprender", 1, "Si j'étais plus jeune, j'apprendrais à danser.", "If I were younger, I'd learn to dance.", "si", {}),
 ("¿Cuántos años ___ cuando se casó?", "tener", 3, "Quel âge pouvait-il avoir quand il s'est marié ?", "How old would he have been when he got married?", "supposition", {}),
 ("Si hiciera buen tiempo, ___ un paseo.", "dar", 4, "S'il faisait beau, nous ferions une promenade.", "If the weather were nice, we'd go for a walk.", "si", {}),
 ("Juré que nunca ___ a ese restaurante.", "volver", 1, "J'ai juré que je ne retournerais jamais dans ce restaurant.", "I swore I'd never go back to that restaurant.", "futurpasse", {}),
 ("Si tuvieras que elegir, ¿qué ___?", "elegir", 2, "Si tu devais choisir, que choisirais-tu ?", "If you had to choose, what would you choose?", "si", {}),
 ("¿Qué ___ sin internet?", "hacer", 4, "Que ferions-nous sans internet ?", "What would we do without the internet?", "hypothese", {}),
]

RAISONS = {
 "futuro": {
  "moment": ("Un moment à venir (mañana, el año que viene, dentro de…) → futur.", "A time to come (mañana, el año que viene, dentro de…) → future."),
  "promesse": ("Une promesse → futur.", "A promise → future."),
  "prevision": ("Une prévision ou une prédiction → futur.", "A forecast or prediction → future."),
  "si": ("si + présent, puis le futur dans l'autre partie : une condition réelle.", "si + present, then the future in the other clause: a real condition."),
  "cuando": ("cuando / en cuanto + subjonctif, puis le futur dans la principale.", "cuando / en cuanto + subjunctive, then the future in the main clause."),
  "supposition": ("Le futur exprime aussi une supposition sur le présent : estará = il doit être.", "The future also expresses a guess about the present: estará = he's probably."),
 },
 "condicional": {
  "politesse": ("Le conditionnel adoucit une demande ou un souhait, comme en français.", "The conditional softens a request or a wish."),
  "conseil": ("Un conseil (yo que tú, en tu lugar, deberías) → conditionnel.", "Advice (yo que tú, en tu lugar, deberías) → conditional."),
  "si": ("si + subjonctif imparfait, puis le conditionnel : une hypothèse irréelle.", "si + imperfect subjunctive, then the conditional: an unreal condition."),
  "hypothese": ("Une situation imaginée → conditionnel.", "An imagined situation → conditional."),
  "futurpasse": ("Le futur vu du passé (dijo que, pensaba que…) → conditionnel, comme en français.", "The future seen from the past (dijo que, pensaba que…) → conditional."),
  "supposition": ("Le conditionnel exprime aussi une supposition sur le passé : serían las diez = il devait être dix heures.", "The conditional also expresses a guess about the past: serían las diez = it must have been about ten."),
 },
}


def construire(lignes, temps, nom_fr, nom_en, topic, idx):
    out = []
    for l in lignes:
        q, inf, pers, tfr, ten, cle = l[:6]
        opt = l[6] if len(l) > 6 else {}
        assert q.count("___") == 1, q
        assert inf in idx, "verbe absent du corpus : " + inf
        formes = conjuguer(inf, temps)
        rang, sujet = PERSONNES[pers]
        sujet = opt.get("sujet", sujet)
        bonne = formes[rang]
        rfr, ren = RAISONS[temps][cle]
        liste = " · ".join(f for i, f in enumerate(formes) if i != 4)
        out.append({
            "topic": topic, "question": q, "translation": tfr, "translation_en": ten,
            "hint": "(%s — %s)" % (inf, sujet), "hint_en": "(%s — %s)" % (inf, sujet),
            "answers": [bonne] + opt.get("aussi", []), "correct": bonne,
            "explanation": "%s %s de « %s » : %s." % (rfr, nom_fr, inf, liste),
            "explanation_en": "%s %s of « %s »: %s." % (ren, nom_en, inf, liste),
        })
    return out


def main():
    for (inf, temps), attendu in VERIFS.items():
        assert " ".join(conjuguer(inf, temps)) == attendu, (inf, temps, conjuguer(inf, temps))
    verbos = json.load(io.open(os.path.join(DATOS, "verbos.json"), encoding="utf-8"))
    idx = {x["infinitif"]: x for n in verbos.values() for x in n}
    for nom, lignes in (("futur", FUTURO), ("conditionnel", CONDICIONAL)):
        assert len(lignes) >= 50 and len({l[0] for l in lignes}) == len(lignes), nom
    chemin = os.path.join(DATOS, "ejercicios.json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    d["jeux"]["futuroExercises"] = construire(FUTURO, "futuro", "Futur", "Future", "Futuro", idx)
    d["jeux"]["condicionalExercises"] = construire(CONDICIONAL, "condicional", "Conditionnel", "Conditional", "Condicional", idx)
    io.open(chemin, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    g = os.path.join(DATOS, "grammaire.json")
    gd = json.load(io.open(g, encoding="utf-8"))
    gd["fiches"] = [f for f in gd["fiches"] if f["id"] != FICHE["id"]]
    rang = next(i for i, f in enumerate(gd["fiches"]) if f["id"] == "pasados") + 1
    gd["fiches"].insert(rang, FICHE)
    io.open(g, "w", encoding="utf-8", newline="\n").write(json.dumps(gd, ensure_ascii=False, indent=1) + "\n")
    print("futuroExercises %d, condicionalExercises %d, fiche futuro-condicional" % (len(FUTURO), len(CONDICIONAL)))


if __name__ == "__main__":
    main()
