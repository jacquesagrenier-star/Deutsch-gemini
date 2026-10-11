# -*- coding: utf-8 -*-
"""Trois fiches pour les debutants, et la relecture des sept fiches existantes.

    python fusion-espagnol/fiches_debutants.py

Demande de Jacques (10 oct. 2026), avant d'annoncer l'espagnol a des amis
qui l'ont etudie quatre ans a l'universite : « tres, tres solide ». Il
manquait ce qu'un debutant rencontre en premier :
  - presente      : -ar / -er / -ir, et les grands irreguliers ;
  - hay-preguntas : hay ou esta, et les mots interrogatifs ;
  - pronominales  : llamarse, levantarse...
La relecture des sept fiches corrige surtout l'anglais (des mises en garde
amputees de moitie) et deux oublis du francais (les adjectifs en -or ont un
feminin ; tous les -ma ne sont pas masculins).

IDEMPOTENT : une fiche deja presente est remplacee, pas doublee.
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "espanol", "datos", "grammaire.json")


def fe(fr, en):
    return {"fr": fr, "en": en}


NOUVELLES = [
 {
  "id": "presente",
  "titre": fe("Le présent", "The present tense"),
  "resume": fe("Trois terminaisons, quelques grands irréguliers", "Three endings, a few big irregulars"),
  "regle": fe(
   "On enlève <b>-ar</b>, <b>-er</b> ou <b>-ir</b> et on ajoute la terminaison de la personne. Le pronom sujet tombe le plus souvent : la terminaison suffit — <b>hablo</b> = je parle.",
   "Drop <b>-ar</b>, <b>-er</b> or <b>-ir</b> and add the ending for the person. The subject pronoun is usually left out: the ending is enough — <b>hablo</b> = I speak."),
  "tableau": [
   ["", fe("hablar · comer · vivir", "hablar · comer · vivir")],
   ["yo", fe("hablo · como · vivo", "hablo · como · vivo")],
   ["tú", fe("hablas · comes · vives", "hablas · comes · vives")],
   ["él, ella, usted", fe("habla · come · vive", "habla · come · vive")],
   ["nosotros", fe("hablamos · comemos · vivimos", "hablamos · comemos · vivimos")],
   ["vosotros (Espagne)", fe("habláis · coméis · vivís", "habláis · coméis · vivís")],
   ["ellos, ellas, ustedes", fe("hablan · comen · viven", "hablan · comen · viven")]
  ],
  "exemples": [
   ["Soy de Montreal, pero estoy en Madrid.",
    fe("Je suis de Montréal, mais je suis à Madrid. (ser : soy, eres, es, somos, sois, son · estar : estoy, estás, está, estamos, estáis, están)",
       "I'm from Montreal, but I'm in Madrid. (ser: soy, eres, es, somos, sois, son · estar: estoy, estás, está, estamos, estáis, están)")],
   ["Tengo veinte años.",
    fe("J'ai vingt ans. (tener : tengo, tienes, tiene, tenemos, tenéis, tienen — l'âge se dit avec tener)",
       "I'm twenty. (tener: tengo, tienes, tiene, tenemos, tenéis, tienen — age takes tener)")],
   ["Voy al mercado.",
    fe("Je vais au marché. (ir : voy, vas, va, vamos, vais, van)",
       "I'm going to the market. (ir: voy, vas, va, vamos, vais, van)")],
   ["Quiero un café, pero no puedo pagar.",
    fe("Je veux un café, mais je ne peux pas payer. (e → ie : quiero · o → ue : puedo — sauf avec nosotros et vosotros : queremos, podemos)",
       "I want a coffee, but I can't pay. (e → ie: quiero · o → ue: puedo — except nosotros and vosotros: queremos, podemos)")],
   ["Hago la cena y salgo a las ocho.",
    fe("Je fais le dîner et je sors à huit heures. (-go à la 1re personne : hago, salgo, pongo, tengo, vengo, digo)",
       "I make dinner and go out at eight. (-go in the first person: hago, salgo, pongo, tengo, vengo, digo)")],
   ["¿Habla usted francés?",
    fe("Parlez-vous français ? (usted, le vouvoiement, se conjugue comme él)",
       "Do you speak French? (usted, the polite « you », takes the él form)")]
  ],
  "attention": fe(
   "Le pronom sujet n'est pas obligatoire : <b>hablo</b> suffit, et <b>yo hablo</b> insiste (moi, je parle). <b>usted</b> (vous de politesse) prend la forme de él. Et en Amérique latine, <b>ustedes</b> remplace vosotros pour tout le monde : <b>¿Ustedes hablan español?</b>",
   "The subject pronoun is optional: <b>hablo</b> is enough, and <b>yo hablo</b> stresses it (I speak). <b>usted</b> (polite « you ») takes the él form. And in Latin America, <b>ustedes</b> replaces vosotros for everyone: <b>¿Ustedes hablan español?</b>")
 },
 {
  "id": "hay-preguntas",
  "titre": fe("hay ou está, et les questions", "hay vs está, and questions"),
  "resume": fe("Il y a, se trouver, et comment demander", "There is, being somewhere, and how to ask"),
  "regle": fe(
   "<b>hay</b> (il y a) présente quelque chose de <b>nouveau</b> : un, une, des, un nombre, rien. <b>está / están</b> situe quelque chose de <b>déjà connu</b> : le, la, les, mon, ce, un prénom.",
   "<b>hay</b> (there is / there are) introduces something <b>new</b>: a, some, a number, nothing. <b>está / están</b> locates something <b>already known</b>: the, my, this, a name."),
  "tableau": [
   ["hay", fe("un, una, unos, dos, mucho, ningún…", "a, some, two, a lot of, no…"), "Hay un banco en la plaza."],
   ["está / están", fe("el, la, los, las, mi, este, un prénom", "the, my, this, a name"), "El banco está en la plaza."],
   ["qué", fe("quoi, que, quel", "what, which"), "¿Qué quieres?"],
   ["quién / quiénes", fe("qui", "who"), "¿Quién es?"],
   ["dónde · adónde", fe("où · où (avec un mouvement)", "where · where to"), "¿Dónde vives? · ¿Adónde vas?"],
   ["cuándo", fe("quand", "when"), "¿Cuándo llegas?"],
   ["cómo", fe("comment", "how"), "¿Cómo te llamas?"],
   ["cuánto(s), cuánta(s)", fe("combien (s'accorde avec le nom)", "how much, how many (agrees with the noun)"), "¿Cuántos años tienes?"],
   ["cuál / cuáles", fe("lequel, quel (parmi plusieurs)", "which (one), what"), "¿Cuál es tu número?"],
   ["por qué", fe("pourquoi — la réponse : porque", "why — the answer: porque"), "¿Por qué no vienes? — Porque estoy cansado."]
  ],
  "exemples": [
   ["Hay una farmacia cerca de aquí.",
    fe("Il y a une pharmacie près d'ici. (hay : une chose qu'on annonce)", "There's a chemist's near here. (hay: something you're introducing)")],
   ["La farmacia está al lado del banco.",
    fe("La pharmacie est à côté de la banque. (está : une chose déjà connue)", "The chemist's is next to the bank. (está: something already known)")],
   ["¿Hay leche? — No, no hay.",
    fe("Il y a du lait ? — Non, il n'y en a pas. (hay ne change jamais : hay un libro, hay dos libros)", "Is there any milk? — No, there isn't. (hay never changes: hay un libro, hay dos libros)")],
   ["¿Cuál es tu color favorito?",
    fe("Quelle est ta couleur préférée ? (devant es, « quel » se dit cuál, pas qué)", "What's your favourite colour? (before es, « what » is cuál, not qué)")],
   ["No sé dónde está.",
    fe("Je ne sais pas où il est. (le mot interrogatif garde son accent dans une question indirecte)", "I don't know where it is. (the question word keeps its accent in an indirect question)")]
  ],
  "attention": fe(
   "Jamais <i>hay el</i> ni <i>la farmacia hay</i> : avec un article défini, c'est <b>estar</b>. <b>hay</b> ne s'accorde jamais : <b>hay muchas personas</b>. Les mots interrogatifs portent toujours un accent écrit, même sans point d'interrogation : <b>no sé qué hacer</b>. Et une question s'ouvre par <b>¿</b> : <b>¿Dónde estás?</b>",
   "Never <i>hay el</i> or <i>la farmacia hay</i>: with « the », use <b>estar</b>. <b>hay</b> never agrees: <b>hay muchas personas</b>. Question words always carry a written accent, even without a question mark: <b>no sé qué hacer</b>. And a question opens with <b>¿</b>: <b>¿Dónde estás?</b>")
 },
 {
  "id": "pronominales",
  "titre": fe("Les verbes pronominaux", "Reflexive verbs"),
  "resume": fe("Comme « se lever » en français… ou pas tout à fait", "Verbs with se"),
  "regle": fe(
   "Le pronom change avec la personne — <b>me, te, se, nos, os, se</b> — et se place devant le verbe conjugué, comme en français : <b>me levanto</b> = je me lève.",
   "The pronoun changes with the person — <b>me, te, se, nos, os, se</b> — and goes before the conjugated verb: <b>me levanto</b> = I get up."),
  "tableau": [
   ["", fe("levantarse (se lever)", "levantarse (to get up)")],
   ["yo", fe("me levanto", "me levanto")],
   ["tú", fe("te levantas", "te levantas")],
   ["él, ella, usted", fe("se levanta", "se levanta")],
   ["nosotros", fe("nos levantamos", "nos levantamos")],
   ["vosotros (Espagne)", fe("os levantáis", "os levantáis")],
   ["ellos, ellas, ustedes", fe("se levantan", "se levantan")]
  ],
  "exemples": [
   ["Me llamo Ana.", fe("Je m'appelle Ana.", "My name is Ana.")],
   ["Me levanto a las siete y me ducho.",
    fe("Je me lève à sept heures et je prends une douche. (ducharse est pronominal en espagnol)", "I get up at seven and have a shower. (ducharse takes se in Spanish)")],
   ["Voy a acostarme.",
    fe("Je vais me coucher. (à l'infinitif, le pronom se soude au verbe — ou : me voy a acostar)", "I'm going to bed. (with an infinitive, the pronoun can be attached — or: me voy a acostar)")],
   ["¡Siéntate!",
    fe("Assieds-toi ! (à l'impératif affirmatif, le pronom se soude aussi)", "Sit down! (in the affirmative imperative, the pronoun is attached too)")],
   ["Me lavo las manos.",
    fe("Je me lave les mains. (l'article, comme en français — pas « mis manos »)", "I wash my hands. (the article, not « mis manos »)")],
   ["Me voy.",
    fe("Je m'en vais. (ir = aller ; irse = partir, s'en aller)", "I'm leaving. (ir = to go; irse = to leave)")]
  ],
  "attention": fe(
   "Certains verbes sont pronominaux en espagnol mais pas en français : <b>ducharse</b> (prendre une douche), <b>quedarse</b> (rester), <b>casarse con</b> (épouser). Et le pronom change parfois le sens : <b>dormir</b> / <b>dormirse</b> (dormir / s'endormir), <b>ir</b> / <b>irse</b> (aller / partir), <b>acordar</b> / <b>acordarse de</b> (convenir / se souvenir de).",
   "Some verbs take se in Spanish but not in English: <b>ducharse</b> (to shower), <b>quedarse</b> (to stay), <b>casarse con</b> (to marry). And se sometimes changes the meaning: <b>dormir</b> / <b>dormirse</b> (to sleep / to fall asleep), <b>ir</b> / <b>irse</b> (to go / to leave), <b>acordar</b> / <b>acordarse de</b> (to agree / to remember).")
 }
]


def relire(fiches):
    """Les corrections des sept fiches existantes."""
    f = {x["id"]: x for x in fiches}
    # ser / estar : l'anglais avait perdu la regle du lieu.
    f["ser-estar"]["attention"]["en"] = (
        "Some adjectives change meaning outright: <b>ser listo</b> = to be clever, <b>estar listo</b> = to be ready. "
        "Same for <b>aburrido</b> (boring / bored) and <b>rico</b> (wealthy / tasty). And location takes <b>estar</b>, "
        "even when it never changes: <b>Madrid está en España</b> — except for an event: <b>la fiesta es en mi casa</b>.")
    # por / para : « por correr » est flou ; l'anglais avait perdu « por = par ».
    for e in f["por-para"]["exemples"]:
        if e[0] == "Me multaron por correr.":
            e[0] = "Me multaron por exceso de velocidad."
    f["por-para"]["attention"]["en"] = (
        "If you can replace « for » with « in order to », it's <b>para</b>. If you can replace it with « because of », "
        "it's <b>por</b>. And <b>por</b> also means « through », « by » or « in »: <b>por la ventana</b> (through the window), "
        "<b>por la mañana</b> (in the morning).")
    # Le genre : tous les -ma ne sont pas masculins ; -umbre manquait.
    for l in f["genero"]["tableau"]:
        if l[0] == "-ma (grec)":
            l[1] = fe("masculin (les mots savants, d'origine grecque)", "masculine (learned words, from Greek)")
    if not any(l[0] == "-umbre" for l in f["genero"]["tableau"]):
        f["genero"]["tableau"].append(["-umbre", fe("toujours féminin", "always feminine"), "la costumbre, la legumbre"])
    f["genero"]["attention"]["fr"] = (
        "Les pièges du francophone : <b>el color</b>, <b>el dolor</b>, <b>el calor</b> (la couleur, la douleur, la chaleur), "
        "<b>la leche</b>, <b>la sal</b>, <b>la sangre</b>, <b>la nariz</b> (le lait, le sel, le sang, le nez). Tous les mots en "
        "-ma ne sont pas masculins : <b>la cama</b>, <b>la forma</b>. Et les mots qui commencent par un <b>a-</b> accentué "
        "prennent <b>el</b> mais restent féminins : <b>el agua fría</b>, jamais <i>frío</i>.")
    f["genero"]["attention"]["en"] = (
        "Not every -ma word is masculine: <b>la cama</b>, <b>la forma</b>. And words starting with a stressed <b>a-</b> take "
        "<b>el</b> but stay feminine: <b>el agua fría</b>, never <i>frío</i>. Same for hambre, aula, alma.")
    # L'accord : les adjectifs en -or ont un feminin.
    tab = f["concordancia"]["tableau"]
    if not any(l[0] == "-or → -ora" for l in tab):
        tab.insert(1, ["-or → -ora", fe("les adjectifs en -or ont un féminin", "adjectives in -or have a feminine"),
                       "trabajador → trabajadora"])
    for l in tab:
        if l[0] == "-e, -ista, -al":
            l[0] = "-e, -ista, -l, -z"
            l[2] = "grande, realista, natural, feliz"
    f["concordancia"]["attention"]["en"] = (
        "Mixed group? Masculine plural wins: <b>Juan y Ana están cansados</b>. Adjectives nearly always come <b>after</b> "
        "the noun: <b>una casa grande</b>. Placed before, some change meaning: <b>un gran hombre</b>, a great man.")
    # Les pronoms : « os » n'existe qu'en Espagne.
    for l in f["pronombres"]["tableau"]:
        if l[0] == "me / te / nos / os":
            l[1] = fe("me, te, nous, vous (os : Espagne seulement)", "me, you, us (os: Spain only)")


def main():
    d = json.load(io.open(CHEMIN, encoding="utf-8"))
    ids = {x["id"] for x in NOUVELLES}
    d["fiches"] = [x for x in d["fiches"] if x["id"] not in ids]
    # Le present d'abord : c'est la premiere fiche d'un debutant.
    d["fiches"] = [NOUVELLES[0]] + d["fiches"] + NOUVELLES[1:]
    relire(d["fiches"])
    io.open(CHEMIN, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("fiches :", ", ".join(x["id"] for x in d["fiches"]))


if __name__ == "__main__":
    main()
