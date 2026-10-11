# -*- coding: utf-8 -*-
"""L'imperatif de l'espagnol : la fiche et un jeu de 60.

    python fusion-espagnol/exos_imperativo.py

Deuxieme manque verifie de la relecture (10 oct. 2026) : l'imperatif
n'existait que dans les scenes. Il sert aussi la fonction « indiquer le
chemin » (gira a la derecha, siga todo recto), que Gemini signalait.

LES FORMES VIENNENT DES TABLEAUX VERIFIES (verbos.json) :
  - tu, affirmatif : la forme de « el » au present (habla, cierra, duerme),
    sauf huit irreguliers (di, haz, ve, pon, sal, se, ten, ven) ;
  - tu negatif, usted, ustedes, nosotros : le subjonctif present ;
  - une exception : « vamos » (et non vayamos) pour ir a l'affirmatif.
Pas de pronom soude dans les reponses a taper (siéntate, dímelo) : la fiche
l'explique, mais l'accent qu'il deplace ferait taper juste et compter faux.
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
TU_IRREG = {"decir": "di", "hacer": "haz", "ir": "ve", "poner": "pon", "salir": "sal",
            "ser": "sé", "tener": "ten", "venir": "ven"}
ETIQUETTE = {"tu": "tú", "tu_neg": "tú, négatif", "usted": "usted", "ustedes": "ustedes", "nosotros": "nosotros"}
ETIQUETTE_EN = {"tu": "tú", "tu_neg": "tú, negative", "usted": "usted", "ustedes": "ustedes", "nosotros": "nosotros"}


def forme(v, code):
    inf = v["infinitif"]
    if code == "tu":
        return TU_IRREG.get(inf) or v["praesens"]["er_sie_es"]
    if code == "nosotros" and inf == "ir":
        return "vamos"
    rang = {"tu_neg": 1, "usted": 2, "ustedes": 5, "nosotros": 3}[code]
    return v["subjuntivo"][rang]


RAISONS = {
 "tu": ("Impératif de tú : la forme de él au présent (habla, cierra, duerme).", "Tú imperative: the él form of the present (habla, cierra, duerme)."),
 "tu_irr": ("Impératif de tú, l'un des huit irréguliers à savoir par cœur : di, haz, ve, pon, sal, sé, ten, ven.", "Tú imperative, one of the eight irregulars to learn by heart: di, haz, ve, pon, sal, sé, ten, ven."),
 "tu_neg": ("À la forme négative, plus d'impératif : no + subjonctif présent (no hables, no digas).", "In the negative, no imperative: no + present subjunctive (no hables, no digas)."),
 "usted": ("Avec usted, la forme polie : le subjonctif présent (hable, coma, siga).", "With usted, the polite form: the present subjunctive (hable, coma, siga)."),
 "ustedes": ("Avec ustedes : le subjonctif présent, au pluriel (hablen, abran).", "With ustedes: the present subjunctive, plural (hablen, abran)."),
 "nosotros": ("« Faisons… » : le subjonctif présent de nosotros (hablemos, comamos) — sauf ir : ¡vamos!", "« Let's… »: the nosotros present subjunctive (hablemos, comamos) — except ir: ¡vamos!"),
}

LIGNES = [
 ("___ la ventana, por favor.", "abrir", "tu", "Ouvre la fenêtre, s'il te plaît.", "Open the window, please."),
 ("___ aquí, te estoy esperando.", "venir", "tu", "Viens ici, je t'attends.", "Come here, I'm waiting for you."),
 ("___ la verdad.", "decir", "tu", "Dis la vérité.", "Tell the truth."),
 ("___ los deberes antes de cenar.", "hacer", "tu", "Fais tes devoirs avant le dîner.", "Do your homework before dinner."),
 ("___ la mesa, que vamos a comer.", "poner", "tu", "Mets la table, on va manger.", "Lay the table, we're about to eat."),
 ("___ paciencia, ya llegamos.", "tener", "tu", "Patience, on arrive.", "Be patient, we're almost there."),
 ("___ bueno con tu hermana.", "ser", "tu", "Sois gentil avec ta sœur.", "Be nice to your sister."),
 ("___ a la farmacia, por favor.", "ir", "tu", "Va à la pharmacie, s'il te plaît.", "Go to the chemist's, please."),
 ("___ de casa temprano.", "salir", "tu", "Pars de chez toi tôt.", "Leave home early."),
 ("___ más despacio, no te entiendo.", "hablar", "tu", "Parle plus lentement, je ne te comprends pas.", "Speak more slowly, I don't understand you."),
 ("___ mucha agua.", "beber", "tu", "Bois beaucoup d'eau.", "Drink plenty of water."),
 ("___ la puerta, hace frío.", "cerrar", "tu", "Ferme la porte, il fait froid.", "Shut the door, it's cold."),
 ("___ un poco más, todavía es temprano.", "dormir", "tu", "Dors encore un peu, il est encore tôt.", "Sleep a little longer, it's still early."),
 ("___ este libro, es buenísimo.", "leer", "tu", "Lis ce livre, il est excellent.", "Read this book, it's brilliant."),
 ("___ con atención.", "escuchar", "tu", "Écoute attentivement.", "Listen carefully."),
 ("___ a tu abuela de vez en cuando.", "llamar", "tu", "Appelle ta grand-mère de temps en temps.", "Call your grandmother now and then."),
 ("___ el autobús número cinco.", "tomar", "tu", "Prends le bus numéro cinq.", "Take the number five bus."),
 ("___ a la derecha en la segunda calle.", "girar", "tu", "Tourne à droite dans la deuxième rue.", "Turn right at the second street."),
 ("___ todo recto hasta la plaza.", "seguir", "tu", "Continue tout droit jusqu'à la place.", "Go straight on to the square."),
 ("___ la luz al salir.", "apagar", "tu", "Éteins la lumière en sortant.", "Switch off the light when you leave."),
 ("No ___ tan rápido.", "hablar", "tu_neg", "Ne parle pas si vite.", "Don't speak so fast."),
 ("No ___ la ventana, hace frío.", "abrir", "tu_neg", "N'ouvre pas la fenêtre, il fait froid.", "Don't open the window, it's cold."),
 ("No ___ tarde.", "llegar", "tu_neg", "N'arrive pas en retard.", "Don't be late."),
 ("No ___ eso, no es verdad.", "decir", "tu_neg", "Ne dis pas ça, ce n'est pas vrai.", "Don't say that, it isn't true."),
 ("No ___ ruido, el bebé duerme.", "hacer", "tu_neg", "Ne fais pas de bruit, le bébé dort.", "Don't make any noise, the baby's asleep."),
 ("No ___ las llaves.", "olvidar", "tu_neg", "N'oublie pas les clés.", "Don't forget the keys."),
 ("No ___ miedo.", "tener", "tu_neg", "N'aie pas peur.", "Don't be afraid."),
 ("No ___ solo por la noche.", "salir", "tu_neg", "Ne sors pas seul la nuit.", "Don't go out alone at night."),
 ("No ___ los zapatos en la mesa.", "poner", "tu_neg", "Ne mets pas les chaussures sur la table.", "Don't put your shoes on the table."),
 ("No ___ a ese restaurante, es muy caro.", "ir", "tu_neg", "Ne va pas dans ce restaurant, il est très cher.", "Don't go to that restaurant, it's very expensive."),
 ("No ___ tanto café.", "beber", "tu_neg", "Ne bois pas autant de café.", "Don't drink so much coffee."),
 ("No ___ la puerta, por favor.", "cerrar", "tu_neg", "Ne ferme pas la porte, s'il te plaît.", "Don't shut the door, please."),
 ("___ usted, por favor.", "pasar", "usted", "Entrez, je vous en prie.", "Come in, please."),
 ("___ la segunda calle a la izquierda.", "tomar", "usted", "Prenez la deuxième rue à gauche.", "Take the second street on the left."),
 ("___ este documento antes de firmar.", "leer", "usted", "Lisez ce document avant de signer.", "Read this document before signing."),
 ("___ hondo, por favor.", "respirar", "usted", "Respirez profondément, s'il vous plaît.", "Breathe in deeply, please."),
 ("___ todo recto y luego a la derecha.", "seguir", "usted", "Continuez tout droit, puis à droite.", "Go straight on, then right."),
 ("___ aquí un momento, por favor.", "esperar", "usted", "Attendez ici un moment, s'il vous plaît.", "Wait here a moment, please."),
 ("___ una pastilla cada ocho horas.", "tomar", "usted", "Prenez un comprimé toutes les huit heures.", "Take one tablet every eight hours."),
 ("No ___ nada antes del análisis.", "comer", "usted", "Ne mangez rien avant la prise de sang.", "Don't eat anything before the blood test."),
 ("___ más despacio, por favor.", "hablar", "usted", "Parlez plus lentement, s'il vous plaît.", "Please speak more slowly."),
 ("___ la puerta, por favor.", "cerrar", "usted", "Fermez la porte, s'il vous plaît.", "Please shut the door."),
 ("___ su nombre aquí, por favor.", "escribir", "usted", "Écrivez votre nom ici, s'il vous plaît.", "Please write your name here."),
 ("___ mañana a las nueve.", "venir", "usted", "Venez demain à neuf heures.", "Come tomorrow at nine."),
 ("___ paciencia, el médico llega enseguida.", "tener", "usted", "Patientez, le médecin arrive tout de suite.", "Please be patient, the doctor will be right with you."),
 ("___ hasta el final de la calle.", "ir", "usted", "Allez jusqu'au bout de la rue.", "Go to the end of the street."),
 ("Niños, ___ la mesa, por favor.", "poner", "ustedes", "Les enfants, mettez la table, s'il vous plaît.", "Children, lay the table, please."),
 ("Señores, ___ por aquí.", "pasar", "ustedes", "Messieurs-dames, passez par ici.", "This way, please, ladies and gentlemen."),
 ("Chicos, ___ silencio, por favor.", "hacer", "ustedes", "Les jeunes, faites silence, s'il vous plaît.", "Quiet, please, everyone."),
 ("___ el libro en la página veinte.", "abrir", "ustedes", "Ouvrez le livre à la page vingt.", "Open your books at page twenty."),
 ("No ___ en el pasillo.", "correr", "ustedes", "Ne courez pas dans le couloir.", "Don't run in the corridor."),
 ("___ con atención, por favor.", "escuchar", "ustedes", "Écoutez bien, s'il vous plaît.", "Listen carefully, please."),
 ("¡___ a la playa!", "ir", "nosotros", "Allons à la plage !", "Let's go to the beach!"),
 ("___ un taxi, es tarde.", "tomar", "nosotros", "Prenons un taxi, il est tard.", "Let's take a taxi, it's late."),
 ("___ algo, tengo hambre.", "comer", "nosotros", "Mangeons quelque chose, j'ai faim.", "Let's eat something, I'm hungry."),
 ("No ___ más tiempo.", "perder", "nosotros", "Ne perdons plus de temps.", "Let's not waste any more time."),
 ("___ un poco antes de cenar.", "caminar", "nosotros", "Marchons un peu avant le dîner.", "Let's walk a bit before dinner."),
 ("___ del problema con calma.", "hablar", "nosotros", "Parlons du problème calmement.", "Let's talk about the problem calmly."),
 ("No ___ nada a nadie.", "decir", "nosotros", "Ne disons rien à personne.", "Let's not tell anyone."),
 ("___ la cuenta, por favor.", "pedir", "nosotros", "Demandons l'addition.", "Let's ask for the bill."),
]

FICHE = {
 "id": "imperativo",
 "titre": {"fr": "L'impératif", "en": "The imperative"},
 "resume": {"fr": "Donner un ordre, un conseil, un chemin", "en": "Orders, advice, directions"},
 "regle": {
  "fr": "Avec <b>tú</b>, l'impératif est la forme de él au présent : <b>habla</b>, <b>come</b>, <b>cierra</b>. Pour tout le reste — <b>usted</b>, <b>ustedes</b>, <b>nosotros</b> et toutes les formes <b>négatives</b> — on prend le <b>subjonctif présent</b> : <b>hable</b>, <b>no hables</b>.",
  "en": "With <b>tú</b>, the imperative is the él form of the present: <b>habla</b>, <b>come</b>, <b>cierra</b>. For everything else — <b>usted</b>, <b>ustedes</b>, <b>nosotros</b> and every <b>negative</b> — use the <b>present subjunctive</b>: <b>hable</b>, <b>no hables</b>."},
 "tableau": [
  ["", {"fr": "hablar · comer · abrir", "en": "hablar · comer · abrir"}],
  ["tú", {"fr": "habla · come · abre", "en": "habla · come · abre"}],
  ["tú (négatif)", {"fr": "no hables · no comas · no abras", "en": "no hables · no comas · no abras"}],
  ["usted", {"fr": "hable · coma · abra", "en": "hable · coma · abra"}],
  ["ustedes", {"fr": "hablen · coman · abran", "en": "hablen · coman · abran"}],
  ["nosotros", {"fr": "hablemos · comamos · abramos", "en": "hablemos · comamos · abramos"}],
  ["tú irréguliers", {"fr": "decir → di, hacer → haz, ir → ve, poner → pon, salir → sal, ser → sé, tener → ten, venir → ven",
                      "en": "decir → di, hacer → haz, ir → ve, poner → pon, salir → sal, ser → sé, tener → ten, venir → ven"}]
 ],
 "exemples": [
  ["Gira a la derecha y sigue todo recto.", {"fr": "Tourne à droite et continue tout droit.", "en": "Turn right and go straight on."}],
  ["Siga todo recto y tome la segunda calle.", {"fr": "Continuez tout droit et prenez la deuxième rue. (usted)", "en": "Go straight on and take the second street. (usted)"}],
  ["No hables tan alto.", {"fr": "Ne parle pas si fort. (négatif : le subjonctif)", "en": "Don't talk so loudly. (negative: the subjunctive)"}],
  ["Dímelo.", {"fr": "Dis-le-moi. (à l'affirmatif, les pronoms se soudent à la fin, et l'accent écrit garde la syllabe forte)", "en": "Tell me. (in the affirmative, pronouns attach to the end, and a written accent keeps the stress)"}],
  ["No me lo digas.", {"fr": "Ne me le dis pas. (au négatif, les pronoms repassent devant)", "en": "Don't tell me. (in the negative, pronouns go back in front)"}],
  ["¡Vamos!", {"fr": "Allons-y ! (ir avec nosotros : vamos, et non vayamos)", "en": "Let's go! (ir with nosotros: vamos, not vayamos)"}]
 ],
 "attention": {
  "fr": "Le piège du francophone : la forme négative n'est pas l'impératif avec « no ». « Ne parle pas » se dit <b>no hables</b>, jamais <i>no habla</i>. Et les pronoms changent de place : <b>siéntate</b> (assieds-toi), mais <b>no te sientes</b> (ne t'assieds pas).",
  "en": "The trap: the negative isn't the imperative plus « no ». « Don't speak » is <b>no hables</b>, never <i>no habla</i>. And pronouns move: <b>siéntate</b> (sit down), but <b>no te sientes</b> (don't sit down)."},
 "exercice": "startImperativoExercise"
}


def main():
    verbos = json.load(io.open(os.path.join(DATOS, "verbos.json"), encoding="utf-8"))
    idx = {x["infinitif"]: x for n in verbos.values() for x in n}
    assert len(LIGNES) >= 50 and len({l[0] for l in LIGNES}) == len(LIGNES)
    # Les formes sur lesquelles tout repose, verifiees une fois.
    attendu = {("hablar", "tu"): "habla", ("cerrar", "tu"): "cierra", ("dormir", "tu"): "duerme",
               ("seguir", "tu"): "sigue", ("apagar", "tu"): "apaga", ("decir", "tu"): "di",
               ("ir", "tu"): "ve", ("ser", "tu"): "sé", ("ir", "nosotros"): "vamos",
               ("decir", "tu_neg"): "digas", ("seguir", "usted"): "siga", ("pedir", "nosotros"): "pidamos",
               ("llegar", "tu_neg"): "llegues", ("ir", "usted"): "vaya", ("hacer", "ustedes"): "hagan"}
    for (inf, code), f in attendu.items():
        assert forme(idx[inf], code) == f, (inf, code, forme(idx[inf], code))
    out = []
    for q, inf, code, tfr, ten in LIGNES:
        assert q.count("___") == 1, q
        bonne = forme(idx[inf], code)
        cle = "tu_irr" if code == "tu" and inf in TU_IRREG else code
        rfr, ren = RAISONS[cle]
        out.append({
            "topic": "Imperativo", "question": q, "translation": tfr, "translation_en": ten,
            "hint": "(%s — %s)" % (inf, ETIQUETTE[code]), "hint_en": "(%s — %s)" % (inf, ETIQUETTE_EN[code]),
            "answers": [bonne], "correct": bonne,
            "explanation": "%s %s → %s." % (rfr, inf, bonne), "explanation_en": "%s %s → %s." % (ren, inf, bonne),
        })
    chemin = os.path.join(DATOS, "ejercicios.json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    d["jeux"]["imperativoExercises"] = out
    io.open(chemin, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    g = os.path.join(DATOS, "grammaire.json")
    gd = json.load(io.open(g, encoding="utf-8"))
    gd["fiches"] = [f for f in gd["fiches"] if f["id"] != FICHE["id"]]
    rang = next(i for i, f in enumerate(gd["fiches"]) if f["id"] == "futuro-condicional") + 1
    gd["fiches"].insert(rang, FICHE)
    io.open(g, "w", encoding="utf-8", newline="\n").write(json.dumps(gd, ensure_ascii=False, indent=1) + "\n")
    print("imperativoExercises %d, fiche imperativo" % len(out))


if __name__ == "__main__":
    main()
