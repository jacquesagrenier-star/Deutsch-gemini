# -*- coding: utf-8 -*-
"""Les fiches tirees de l'ancien module anglais (aout 2026, masque depuis la
v727) : phrasal verbs, pieges, expressions de conversation, americain et
britannique. Ses listes sont recopiees dans anglais/outils/ancien/ -- ce sont
desormais des SOURCES : on corrige la (l'ancien module, lui, attend d'etre
retire). Les questions des pieges sont ecrites a la main (pieges_niveaux.py),
les autres se tirent des listes.

Appele par niveaux.py : ancien_module.construire(us, question, en_us).
"""
import json, os, random, re

import construire as C
import mots_a1
import pieges_niveaux

ICI = os.path.dirname(os.path.abspath(__file__))
ORDRE = ["A1", "A2", "B1", "B2", "C1"]


def lire(nom):
    with open(os.path.join(ICI, "ancien", nom), encoding="utf-8") as f:
        return json.load(f)


def tirer(graine, groupes, n, exclus):
    """n distracteurs, toujours les memes pour une meme question. Les groupes
    passent dans l'ordre (le plus proche d'abord : meme verbe, meme categorie),
    melanges chacun a part."""
    vus, out = set(x.lower() for x in exclus), []
    for i, g in enumerate(groupes):
        g = [c for c in dict.fromkeys(g) if c.lower() not in vus]
        random.Random(graine + str(i)).shuffle(g)
        for c in g:
            vus.add(c.lower())
            out.append(c)
    return out[:n]


# ---------------------------------------------------------------- phrasal verbs
PARTICULES = ["up", "down", "in", "out", "on", "off", "away", "back", "over", "around", "through", "into", "after", "for", "about", "across", "by", "from"]


def formes(verbe):
    f = {verbe}
    irr = mots_a1.IRREGULIERS.get(verbe)
    # Les formes irregulieres, parfois imbriquees (variantes americaine et
    # britannique) : on prend toutes les chaines.
    pile = list(irr or [])
    while pile:
        x = pile.pop()
        if isinstance(x, str):
            f.update(x.split("/"))
        else:
            pile.extend(x)
    f.add(verbe + ("es" if re.search(r"(sh|ch|x|o)$", verbe) else "s"))
    base = verbe[:-1] if verbe.endswith("e") else verbe
    f.update({base + "ing", base + "ed", verbe + verbe[-1] + "ing", verbe + verbe[-1] + "ed", verbe + "d"})
    return f


def trou_particule(mot, phrase):
    """La phrase avec la particule en blanc, et la particule telle qu'ecrite.
    None si on ne la retrouve pas (objet trop long, mot intercale)."""
    mots = mot.split()
    verbe, reste = mots[0], [m.lower() for m in mots[1:]]
    jetons = [(m.group(0), m.start(), m.end()) for m in re.finditer(r"[A-Za-z']+", phrase)]
    fv = formes(verbe)
    for i, (j, _, _) in enumerate(jetons):
        if j.lower() not in fv:
            continue
        suite = [x[0].lower() for x in jetons[i + 1:i + 1 + len(reste)]]
        if suite == reste:
            debut, fin = jetons[i + 1][1], jetons[i + len(reste)][2]
            return phrase[:debut] + "___" + phrase[fin:], phrase[debut:fin]
        if len(reste) == 1:
            for k in range(i + 2, min(i + 5, len(jetons))):
                if jetons[k][0].lower() == reste[0]:
                    return phrase[:jetons[k][1]] + "___" + phrase[jetons[k][2]:], jetons[k][0]
    return None


def series_phrasal(niv, liste, toutes, question, en_us):
    qs = []
    for e in liste:
        mot, fr, en = e["mot"], e["traduction"], en_us(e["exemple"])
        verbe, reste = mot.split()[0], " ".join(mot.split()[1:])
        t = trou_particule(mot, en)
        if t:
            phrase, bonne = t
            n = len(reste.split())
            memes = [" ".join(x.split()[1:]) for x in toutes if x.split()[0] == verbe and len(x.split()) == n + 1]
            autres = [" ".join(x.split()[1:]) for x in toutes if len(x.split()) == n + 1]
            if n == 1:
                # Une particule contre des particules : pas le « it » de make it.
                groupes = [[m for m in memes if m in PARTICULES], PARTICULES]
            else:
                groupes = [memes, autres]
            fausses = tirer(phrase, groupes, 2, [bonne])
            qs.append(question("phrasal-" + niv.lower(), phrase, bonne, fausses, e["exemple_fr"],
                               "« %s » = %s." % (mot, fr)))
        memes = [x for x in toutes if x.split()[0] == verbe]
        fausses = tirer(mot, [memes, toutes], 2, [mot])
        qs.append(question("phrasal-" + niv.lower(), "« %s » → ___" % fr, mot, fausses, e.get("traduction_en", ""),
                           "%s : %s" % (mot, en)))
    return qs


# ---------------------------------------------------------------- expressions
def coeur(mot):
    return re.sub(r"\s*\(.*\)$", "", mot).rstrip(".…!? ")


def casse(n, majuscule):
    """La casse de la reponse, pour qu'une majuscule ne trahisse pas la bonne.
    Le pronom I reste en majuscule."""
    if majuscule:
        return n[0].upper() + n[1:]
    return n if re.match(r"I[\s']", n) else n[0].lower() + n[1:]


def enonce(fr):
    return ("%s → ___" if fr.startswith("«") else "« %s » → ___") % fr


def series_expressions(niv, liste, question, en_us):
    qs = []
    oral = lambda x: x["kategorie"] == "Anglais parlé réel"
    for e in liste:
        mot, fr, en = e["mot"], e["traduction"], en_us(e["exemple"])
        # Les formes relachees (wanna, gonna) ne se melangent qu'entre elles.
        voisins = [x for x in liste if oral(x) == oral(e)]
        meme_cat = [x for x in voisins if x["kategorie"] == e["kategorie"]]
        c = coeur(mot)
        i = en.lower().find(c.lower())
        if i >= 0:
            bonne = en[i:i + len(c)]
            phrase = en[:i] + "___" + en[i + len(c):]
            groupes = [[casse(coeur(x["mot"]), bonne[0].isupper()) for x in g] for g in (meme_cat, voisins)]
            fausses = tirer(phrase, groupes, 2, [bonne])
            qs.append(question("converser-" + niv.lower(), phrase, bonne, fausses, e["exemple_fr"],
                               "« %s » = %s" % (mot, fr)))
        fausses = tirer(fr, [[x["mot"] for x in meme_cat], [x["mot"] for x in voisins]], 2, [mot])
        qs.append(question("converser-" + niv.lower(), enonce(fr), mot, fausses, e.get("traduction_en", ""),
                           "%s : %s" % (mot, en)))
    return qs


# ---------------------------------------------------------------- americain / britannique
def paire(mot):
    gb, us = [x.strip() for x in mot.split("/")]
    return gb.replace("🇬🇧", "").strip(), us.replace("🇺🇸", "").strip()


def series_usgb(niv, liste, question):
    qs = []
    paires = [paire(e["mot"]) for e in liste]
    for e, (gb, us) in zip(liste, paires):
        fr = e["traduction"]
        if "Orthographe" in e["kategorie"]:
            qs.append(question("us-gb-" + niv.lower(), "🇺🇸 « %s » s'écrit en Grande-Bretagne : ___" % us, gb, [us],
                               fr, "Orthographe britannique : %s ; américaine : %s." % (gb, us)))
            qs.append(question("us-gb-" + niv.lower(), "🇬🇧 « %s » s'écrit aux États-Unis : ___" % gb, us, [gb],
                               fr, "Orthographe américaine : %s ; britannique : %s." % (us, gb)))
            continue
        # Les distracteurs viennent d'abord de la meme categorie (la maison, les
        # transports...), jamais des mots d'orthographe.
        mots = [(x["kategorie"], p) for x, p in zip(liste, paires) if "Orthographe" not in x["kategorie"] and p != (gb, us)]
        proches = [p for k, p in mots if k == e["kategorie"]]
        autres = [p for k, p in mots]
        qs.append(question("us-gb-" + niv.lower(), "🇺🇸 « %s » se dit en Grande-Bretagne : ___" % us, gb,
                           tirer(us, [[p[0] for p in proches], [p[0] for p in autres]], 2, [gb, us]), fr,
                           "%s 🇬🇧 = %s 🇺🇸 : %s." % (gb, us, fr)))
        qs.append(question("us-gb-" + niv.lower(), "🇬🇧 « %s » se dit aux États-Unis : ___" % gb, us,
                           tirer(gb, [[p[1] for p in proches], [p[1] for p in autres]], 2, [gb, us]), fr,
                           "%s 🇺🇸 = %s 🇬🇧 : %s." % (us, gb, fr)))
    return qs


# ---------------------------------------------------------------- les fiches
FICHES = {
"phrasal": {
 "A2": ("phrasal-a2", "Les phrasal verbs du quotidien", "get up, put on, turn off — un verbe et une petite particule",
        "Un <b>phrasal verb</b> est un verbe suivi d'une particule (<b>up</b>, <b>off</b>, <b>on</b>, <b>back</b>…) qui en change le sens : <b>get</b> (obtenir) → <b>get up</b> (se lever), <b>get off</b> (descendre). On les apprend comme des mots entiers. La particule se place après le verbe, ou après un court complément : <b>turn off the light</b> ou <b>turn the light off</b>.",
        "Avec un pronom, la particule passe toujours après lui : <b>turn it off</b>, jamais <i>turn off it</i>.",
        "phrasalListeA2EnExercises", "Phrasal verbs (liste A2)"),
 "B1": ("phrasal-b1", "Phrasal verbs : la liste B1", "get over, put off, come up with — 42 de plus",
        "Au niveau B1, la particule ne se devine plus : <b>put off</b> veut dire reporter, <b>turn down</b> refuser, <b>come across</b> tomber sur. Certains ont trois mots et prennent un complément : <b>put up with</b> (supporter), <b>look forward to</b> (attendre avec impatience), <b>run out of</b> (être à court de).",
        "Après <b>look forward to</b> et <b>get used to</b>, le verbe prend <b>-ing</b> : <b>I'm looking forward to seeing you</b>.",
        "phrasalListeB1EnExercises", "Phrasal verbs (liste B1)"),
 "B2": ("phrasal-b2", "Phrasal verbs : la liste B2", "turn out, bring about, make up for — le registre soutenu",
        "Les phrasal verbs du B2 servent aussi à l'écrit : <b>bring about</b> (provoquer), <b>set out</b> (exposer), <b>turn out</b> (s'avérer). Plusieurs ont deux sens, un concret et un figuré : <b>put down</b> (poser ; rabaisser), <b>take on</b> (accepter une tâche ; embaucher).",
        "<b>Turn out</b> se construit avec <b>to</b> + verbe ou <b>that</b> : <b>It turned out to be easy</b>, <b>It turned out that he was right</b>.",
        "phrasalListeB2EnExercises", "Phrasal verbs (liste B2)"),
},
"pieges": {
 "A2": ("pieges-a2", "Pièges : faux amis et mots confondus (A2)", "actually, library, lend / borrow, say / tell",
        "Deux sortes de pièges. Les <b>faux amis</b> ressemblent à un mot français mais n'en ont pas le sens : <b>actually</b> veut dire « en fait », pas « actuellement ». Les <b>mots confondus</b> traduisent un seul mot français : <b>lend</b> (prêter) et <b>borrow</b> (emprunter), <b>say</b> et <b>tell</b> (dire).",
        "<b>Tell</b> prend toujours une personne : <b>tell me</b>. <b>Say</b> n'en prend pas directement : <b>say something to me</b>.",
        "piegesA2EnExercises", "Pièges (A2)"),
 "B1": ("pieges-b1", "Pièges : faux amis et mots confondus (B1)", "eventually, sensible, remember / remind",
        "Les faux amis du B1 trompent jusque dans les journaux : <b>eventually</b> (finalement), <b>to pretend</b> (faire semblant), <b>a lecture</b> (un cours magistral). Et l'anglais distingue ce que le français réunit : <b>teach</b> / <b>learn</b> (apprendre), <b>bring</b> / <b>take</b> (apporter, emporter), <b>steal</b> / <b>rob</b> (voler).",
        "<b>Advice</b> est indénombrable : <b>some advice</b>, <b>a piece of advice</b>, jamais <i>an advice</i>.",
        "piegesB1EnExercises", "Pièges (B1)"),
 "B2": ("pieges-b2", "Pièges : faux amis et mots confondus (B2)", "sympathetic, hazard, affect / effect, raise / rise",
        "Au B2, les faux amis sont souvent des mots savants : <b>comprehensive</b> (complet), <b>formidable</b> (redoutable), <b>hazard</b> (danger). Les paires confondues se jouent à une lettre : <b>affect</b> / <b>effect</b>, <b>beside</b> / <b>besides</b>, <b>economic</b> / <b>economical</b>.",
        "<b>Raise</b> a toujours un complément (<b>raise your hand</b>) ; <b>rise</b> n'en a jamais (<b>the sun rises</b>).",
        "piegesB2EnExercises", "Pièges (B2)"),
},
"converser": {
 "A2": ("converser-a2", "Converser : réagir et relancer (A2)", "It depends · No worries · By the way…",
        "Les petites phrases qui font vivre une conversation : réagir (<b>That makes sense</b>, <b>I don't mind</b>), nuancer (<b>It depends</b>, <b>I'm not sure</b>), relancer (<b>By the way…</b>, <b>What do you mean?</b>), rester poli (<b>No worries</b>, <b>Here you go</b>).",
        "<b>I don't mind</b> veut dire « ça m'est égal, ça ne me dérange pas » — pas « je n'ai pas d'avis ».",
        "converserA2EnExercises", "Converser (A2)"),
 "B1": ("converser-b1", "Converser : nuancer et donner son avis (B1)", "Fair enough · It's up to you · gonna, wanna",
        "Au B1, on nuance (<b>As far as I know…</b>, <b>Let me think about it</b>), on accepte ou on refuse sans brusquer (<b>Fair enough</b>, <b>I'm afraid not</b>), et on comprend l'anglais parlé réel : <b>gonna</b>, <b>wanna</b>, <b>gotta</b>, <b>kinda</b>.",
        "<b>Gonna</b>, <b>wanna</b> et <b>gotta</b> s'entendent partout, mais s'écrivent <b>going to</b>, <b>want to</b>, <b>have got to</b> dans un texte soigné.",
        "converserB1EnExercises", "Converser (B1)"),
 "B2": ("converser-b2", "Converser : concéder et objecter (B2)", "I'll give you that · Don't get me wrong…",
        "Les tournures du B2 servent à débattre avec tact : concéder (<b>I'll give you that</b>, <b>I take your point, but…</b>), recadrer (<b>That's beside the point</b>), adoucir une critique (<b>Don't get me wrong…</b>).",
        "<b>I'm on the fence</b> : on hésite encore, on n'a pas tranché.",
        "converserB2EnExercises", "Converser (B2)"),
},
"usgb": {
 "A2": ("us-gb-a2", "Américain ou britannique ? (A2)", "apartment / flat, elevator / lift, color / colour",
        "L'anglais de cette app est <b>américain</b> (Boston), mais on croisera l'anglais britannique dans les films, les livres et en voyage. Les différences sont surtout de <b>vocabulaire</b> (<b>apartment</b> / <b>flat</b>, <b>fries</b> / <b>chips</b>) et d'<b>orthographe</b> (<b>color</b> / <b>colour</b>, <b>center</b> / <b>centre</b>). La grammaire est presque la même.",
        "<b>Chips</b> n'a pas le même sens des deux côtés : des croustilles aux États-Unis, des frites en Grande-Bretagne (où les croustilles sont des <b>crisps</b>).",
        "usGbA2EnExercises", "Américain ou britannique (A2)"),
 "B1": ("us-gb-b1", "Américain ou britannique ? (B1)", "drugstore / chemist, trunk / boot, realize / realise",
        "Au B1, les différences touchent la vie pratique (<b>drugstore</b> / <b>chemist</b>, <b>zip code</b> / <b>postcode</b>, <b>trunk</b> / <b>boot</b>) et l'orthographe : <b>-ize</b> / <b>-ise</b>, <b>-er</b> / <b>-re</b>, <b>-se</b> / <b>-ce</b>, et la consonne doublée du britannique (<b>traveled</b> / <b>travelled</b>).",
        "Les étages ne se comptent pas pareil : le rez-de-chaussée est le <b>first floor</b> aux États-Unis, le <b>ground floor</b> en Grande-Bretagne.",
        "usGbB1EnExercises", "Américain ou britannique (B1)"),
},
}


def ligne_tableau(sorte, e, en_us):
    if sorte == "usgb":
        gb, us = paire(e["mot"])
        return [us + " 🇺🇸 · " + gb + " 🇬🇧", e["traduction"], e["exemple"]]
    sens = e["traduction"] + (" — " + e["piege"] if e.get("piege") else "")
    return [e["mot"], sens, en_us(e["exemple"])]


def construire(us, question, en_us):
    fiches = us["grammaire.json"]["fiches"]
    jeux = us["exercices.json"]["jeux"]
    textes = us["grammaire.json"]["textes"]["fr"]
    donnees = {"phrasal": lire("phrasal_verbs.json"), "pieges": lire("english_pitfalls.json"),
               "converser": lire("english_expressions.json"), "usgb": lire("english_britam.json")}
    tous_phrasal = [e["mot"] for l in donnees["phrasal"].values() for e in l]
    nf = nq = 0
    for sorte, par_niveau in FICHES.items():
        for niv, (fid, titre, resume, regle, attention, serie, kicker) in par_niveau.items():
            liste = donnees[sorte][niv]
            if sorte == "phrasal":
                qs = series_phrasal(niv, liste, tous_phrasal, question, en_us)
            elif sorte == "converser":
                qs = series_expressions(niv, liste, question, en_us)
            elif sorte == "usgb":
                qs = series_usgb(niv, liste, question)
            else:
                qs = []
                for cols in C.lignes(pieges_niveaux.QUESTIONS[niv]):
                    q, bonne, fausses, trad, expl = cols[:5]
                    qs.append(question(fid, q, bonne, [x.strip() for x in fausses.split("/")], trad, expl))
            assert serie not in jeux, "serie en double : " + serie
            vues = set()
            for q in qs:
                assert q["question"] not in vues, "question en double : " + q["question"]
                vues.add(q["question"])
            exemples = [[en_us(e["exemple"]), e["exemple_fr"]] for e in liste[:3]]
            fiches.append({"id": fid, "titre": titre, "resume": resume, "regle": regle,
                           "tableau": [ligne_tableau(sorte, e, en_us) for e in liste],
                           "exemples": exemples, "attention": attention,
                           "exercice": "exercicesFicheEn_" + fid.replace("-", "_"), "serie": serie,
                           "niveau": niv, "statut": "brouillon"})
            jeux[serie] = qs
            textes["kicker_" + serie] = kicker
            nf += 1
            nq += len(qs)
    # Chaque fiche a son palier : la liste des fiches met un intertitre a chaque
    # changement de niveau, les nouvelles se rangent donc avec leur niveau.
    fiches.sort(key=lambda f: ORDRE.index(f.get("niveau", "A1")))
    return nf, nq
