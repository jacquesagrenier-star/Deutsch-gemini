# -*- coding: utf-8 -*-
"""Les temps qui manquaient a la carte de verbe espagnole (13 oct. 2026) :
preterito perfecto, futuro, condicional, imperativo -- et une phrase
d'exemple par temps, traduite en fr / en / pt.

    python fusion-espagnol/tiempos.py                 # calcule, verifie, n'ecrit rien
    python fusion-espagnol/tiempos.py --ecrire        # pose les formes dans verbos.json
    python fusion-espagnol/tiempos.py --ejemplos      # pose les phrases des lots
    python fusion-espagnol/tiempos.py --etat          # ou en est chaque niveau

POURQUOI. Jacques (13 oct. 2026) : « quand je clique sur verbe, je ne vois pas
tous les temps de verbe, chose qu'on a avec l'allemand ». La carte allemande
montre Prasens, Perfekt, Prateritum, Konjunktiv II et Imperativ, avec une
phrase par temps ; la carte espagnole n'avait que le present, le preterit,
l'imparfait et le subjonctif, et une seule phrase.

LES FORMES SONT CALCULEES A PARTIR DES TABLEAUX DEJA VERIFIES de verbos.json
(present, subjonctif), jamais tapees :
  - preterito perfecto : he / has / ha / hemos / habeis / han + participe ;
    participe regulier -ado / -ido, -ido accentue apres voyelle forte
    (leido, oido, caido, traido), et la liste des irreguliers (dicho, hecho,
    puesto, visto, vuelto, escrito, abierto, muerto, roto, cubierto, resuelto,
    frito, impreso), composes compris (deshecho, devuelto, expuesto) ;
  - futuro / condicional : l'infinitif entier + terminaison, et les douze
    radicaux irreguliers (tendr-, pondr-, vendr-, saldr-, valdr-, podr-,
    sabr-, cabr-, habr-, har-, dir-, querr-), composes compris ; bendecir
    reste regulier ;
  - imperativo : tu = la forme de el au present (huit irreguliers : di, haz,
    ve, pon, sal, se, ten, ven, et leurs composes : manten, propon) ; usted
    et ustedes = le subjonctif ; vosotros = l'infinitif, -r -> -d. Un verbe
    pronominal soude son pronom (lavate, lavese, lavaos, lavense) et recoit
    l'accent que le deplacement de la syllabe tonique exige (sientate,
    pongase) : la regle est ecrite dans souder(), et VERIFS la controle.
    Pas d'imperatif pour les verbes qui n'en ont pas (poder, soler, llover,
    gustar...) : la carte ne montre alors rien, comme l'allemand pour les
    modaux.
VERIFS est la liste des irreguliers controles a la main : le script refuse
d'ecrire si l'un d'eux sort faux. Un verbe ajoute a cette liste est un verbe
de plus que personne n'a a relire sur une carte.

LES PHRASES vivent dans espanol/ajouts/ejemplos-tiempos/<niveau>-<lot>.txt :
    # vivir
    preterito | Viví tres años en Madrid. | J'ai vécu... | I lived... | Morei...
    (un temps par ligne : preterito, imperfecto, perfecto, futuro,
     condicional, subjuntivo ; quatre textes : es | fr | en | pt)
--ejemplos les lit toutes, et REFUSE une phrase dont aucun mot n'est une
forme du temps annonce (une phrase au preterit sous « subjuntivo » ne passe
pas), un verbe incomplet, un texte vide. C'est le seul controle mecanique
qu'on ait sur 5 000 phrases ecrites a la main : il ne juge pas le naturel,
mais il attrape le temps faux.
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "espanol", "datos", "verbos.json")
LOTS = os.path.join(RACINE, "espanol", "ajouts", "ejemplos-tiempos")

PRONOMS = ["me", "te", "se", "nos", "os", "se"]
HABER = ["he", "has", "ha", "hemos", "habéis", "han"]
FUT = ["é", "ás", "á", "emos", "éis", "án"]
COND = ["ía", "ías", "ía", "íamos", "íais", "ían"]
TEMPS_PHRASE = ["preterito", "imperfecto", "perfecto", "futuro", "condicional", "subjuntivo"]
LANGUES = ["fr", "en", "pt"]

# Futur / conditionnel : radicaux irreguliers, par la FIN de l'infinitif
# (composes : obtener, proponer, intervenir, deshacer). decir et querer
# seuls : bendecir est regulier (bendecire).
IRREG_FIN = [("tener", "tendr"), ("poner", "pondr"), ("venir", "vendr"), ("salir", "saldr"),
             ("valer", "valdr"), ("poder", "podr"), ("saber", "sabr"), ("caber", "cabr"),
             ("haber", "habr"), ("hacer", "har")]
IRREG_EXACT = {"decir": "dir", "querer": "querr", "satisfacer": "satisfar"}
# Participes irreguliers, par la fin de l'infinitif ; « decir » et « ver »
# exacts (bendecir -> bendecido ; prever -> previsto est liste a part).
PARTICIPE_FIN = [("abrir", "abierto"), ("cubrir", "cubierto"), ("escribir", "escrito"),
                 ("hacer", "hecho"), ("satisfacer", "satisfecho"), ("morir", "muerto"),
                 ("poner", "puesto"), ("solver", "suelto"), ("volver", "vuelto"),
                 ("romper", "roto"), ("freír", "frito"), ("imprimir", "impreso"),
                 ("pudrir", "podrido")]
PARTICIPE_EXACT = {"decir": "dicho", "ver": "visto", "prever": "previsto", "proveer": "provisto"}
# Imperatif de tu : les huit irreguliers, par la fin (manten, propon,
# preven, deshaz) ; decir, ir, ser exacts (bendecir -> bendice).
TU_FIN = [("tener", "tén"), ("poner", "pón"), ("venir", "vén"), ("salir", "sal"), ("hacer", "haz")]
TU_EXACT = {"decir": "di", "ir": "ve", "ser": "sé", "tener": "ten", "poner": "pon", "venir": "ven",
            "satisfacer": "satisfaz"}
# Les verbes sans imperatif : modaux, impersonnels, verbes « comme gustar »
# (la chose aimee est le sujet : on n'ordonne pas a un livre de plaire).
SANS_IMPERATIVO = {"poder", "soler", "haber", "llover", "nevar", "gustar", "encantar", "apetecer",
                   "doler", "faltar", "caber", "costar", "valer", "importar", "interesar", "ocurrir",
                   "suceder", "amanecer", "anochecer", "sobrar", "bastar", "convenir", "deber dinero",
                   "molestar", "existir", "parecer"}
# soler est defectif : present, imparfait, et le perfecto (« ha solido », RAE) ;
# ni futur ni conditionnel. Et son preterit, que verbos.json porte deja,
# n'a pas de phrase : « solió » ne se dit pas, on n'en invente pas une.
SANS_FUTURO = {"soler"}
SANS_PHRASE = {("soler", "preterito")}

# ------------------------------------------------------------------ syllabes

VOY_FORTES = "aeoáéó"
VOY_FAIBLES = "iuíúü"
VOYELLES = VOY_FORTES + VOY_FAIBLES
ACCENT = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"}


def noyaux(mot):
    """Les noyaux vocaliques du mot : liste de (debut, fin), un par syllabe.
    Un « u » muet (que, qui, gue, gui) n'en fait pas partie ; deux voyelles
    fortes se separent (le-a) ; une faible accentuee se separe (gra-dú-a)."""
    out, i = [], 0
    while i < len(mot):
        c = mot[i]
        if c in VOYELLES and not (c == "u" and i > 0 and mot[i - 1] in "qg" and i + 1 < len(mot) and mot[i + 1] in "eiéí"):
            j = i
            while j + 1 < len(mot) and mot[j + 1] in VOYELLES:
                a, b = mot[j], mot[j + 1]
                if a in VOY_FORTES and b in VOY_FORTES:
                    break          # hiatus : le-a, estro-pe-a
                if a in "íú" or b in "íú":
                    break          # faible accentuee : gra-dú-a, re-í-mos
                j += 1
            out.append((i, j + 1))
            i = j + 1
        else:
            i += 1
    return out


def tonique(mot, nx):
    """L'indice du noyau tonique."""
    for k, (a, b) in enumerate(nx):
        if any(c in "áéíóú" for c in mot[a:b]):
            return k
    if len(nx) == 1:
        return 0
    return len(nx) - 2 if mot[-1] in "aeiouns" else len(nx) - 1


def accentuer_noyau(mot, a, b):
    seg = mot[a:b]
    if any(c in "áéíóú" for c in seg):
        return mot
    # Diphtongue : l'accent va sur la forte ; « ui » / « iu » : sur la seconde.
    pos = next((k for k, c in enumerate(seg) if c in "aeo"), len(seg) - 1)
    return mot[:a + pos] + ACCENT[seg[pos]] + mot[a + pos + 1:]


def souder(forme, pronom):
    """Soude un pronom enclitique : lava + te -> lávate, pon + te -> ponte."""
    nx = noyaux(forme)
    k = tonique(forme, nx)
    depuis_fin = len(nx) - k + len(noyaux(pronom))
    mot = forme + pronom
    if depuis_fin >= 3:
        a, b = nx[k]
        mot = accentuer_noyau(mot, a, b)
    return mot


# ------------------------------------------------------------------ formes

def decouper(inf):
    """(verbe, complement, pronominal) : « reciclarse profesionalmente » ->
    (« reciclar », « profesionalmente », True)."""
    verbe, _, comp = inf.partition(" ")
    pron = verbe.endswith("se") and verbe[-4:-2] in ("ar", "er", "ir", "ír")
    if pron:
        verbe = verbe[:-2]
    return verbe, comp, pron


def radical_futur(verbe):
    r = IRREG_EXACT.get(verbe)
    if not r:
        for fin, rad in IRREG_FIN:
            if verbe.endswith(fin):
                r = verbe[: -len(fin)] + rad
                break
    if not r:
        r = verbe[:-2] + "ir" if verbe.endswith("ír") else verbe
    return r


def participe(verbe):
    p = PARTICIPE_EXACT.get(verbe)
    if not p:
        for fin, part in PARTICIPE_FIN:
            if verbe.endswith(fin):
                p = verbe[: -len(fin)] + part
                break
    if not p:
        groupe, rad = verbe[-2:], verbe[:-2]
        if groupe == "ar":
            p = rad + "ado"
        elif groupe == "ír":
            p = rad + "ído"                     # oír -> oído, reír -> reído
        else:
            p = rad + ("ído" if rad and rad[-1] in "aeo" else "ido")   # leído, caído ; vivido
    return p


def tu_imperativo(verbe, el_presente):
    if verbe in TU_EXACT:
        return TU_EXACT[verbe]
    for fin, f in TU_FIN:
        if verbe.endswith(fin):
            return verbe[: -len(fin)] + f
    return el_presente


def formes(v):
    """Les quatre nouveaux temps d'un verbe de verbos.json."""
    inf = v["infinitif"]
    verbe, comp, pron = decouper(inf)
    suffixe = (" " + comp) if comp else ""

    def ligne(forme, i):
        return (PRONOMS[i] + " " if pron else "") + forme + suffixe

    rad = radical_futur(verbe)
    futuro = [ligne(rad + f, i) for i, f in enumerate(FUT)]
    condicional = [ligne(rad + f, i) for i, f in enumerate(COND)]
    part = participe(verbe)
    perfecto = [ligne(h + " " + part, i) for i, h in enumerate(HABER)]

    imperativo = None
    if inf not in SANS_IMPERATIVO and (comp or verbe not in SANS_IMPERATIVO):
        nu = lambda f: f.split(" ")[-1] if pron else f     # « se lava » -> « lava »
        sans_comp = lambda f: f.replace(suffixe, "") if comp else f
        el = nu(sans_comp(v["praesens"]["er_sie_es"]))
        usted, ustedes = nu(sans_comp(v["subjuntivo"][2])), nu(sans_comp(v["subjuntivo"][5]))
        tu = tu_imperativo(verbe, el)
        if pron:
            groupe = verbe[-2:]
            vos = "idos" if verbe == "ir" else verbe[:-2] + {"ar": "aos", "er": "eos", "ir": "íos", "ír": "íos"}[groupe]
            imperativo = {"tu": souder(tu, "te"), "usted": souder(usted, "se"),
                          "vosotros": vos, "ustedes": souder(ustedes, "se")}
        else:
            vos = verbe[:-1] + "d"
            imperativo = {"tu": tu, "usted": usted, "vosotros": vos, "ustedes": ustedes}
        if comp:
            imperativo = {k: f + suffixe for k, f in imperativo.items()}
    if verbe in SANS_FUTURO:
        futuro = condicional = None
    return {"perfecto": perfecto, "futuro": futuro, "condicional": condicional, "imperativo": imperativo}


# Les irreguliers verifies a la main (RAE, Diccionario panhispanico de dudas).
# Chaque entree : (temps, formes attendues, separees par des espaces ; pour
# l'imperatif : tu usted vosotros ustedes).
VERIFS = {
    "ser": {"perfecto": "he sido has sido ha sido hemos sido habéis sido han sido",
            "futuro": "seré serás será seremos seréis serán",
            "condicional": "sería serías sería seríamos seríais serían",
            "imperativo": "sé sea sed sean"},
    "ir": {"perfecto": "he ido has ido ha ido hemos ido habéis ido han ido",
           "futuro": "iré irás irá iremos iréis irán",
           "imperativo": "ve vaya id vayan"},
    "estar": {"futuro": "estaré estarás estará estaremos estaréis estarán",
              "imperativo": "está esté estad estén"},
    "tener": {"perfecto": "he tenido has tenido ha tenido hemos tenido habéis tenido han tenido",
              "futuro": "tendré tendrás tendrá tendremos tendréis tendrán",
              "condicional": "tendría tendrías tendría tendríamos tendríais tendrían",
              "imperativo": "ten tenga tened tengan"},
    "hacer": {"perfecto": "he hecho has hecho ha hecho hemos hecho habéis hecho han hecho",
              "futuro": "haré harás hará haremos haréis harán",
              "condicional": "haría harías haría haríamos haríais harían",
              "imperativo": "haz haga haced hagan"},
    "decir": {"perfecto": "he dicho has dicho ha dicho hemos dicho habéis dicho han dicho",
              "futuro": "diré dirás dirá diremos diréis dirán",
              "condicional": "diría dirías diría diríamos diríais dirían",
              "imperativo": "di diga decid digan"},
    "poner": {"perfecto": "he puesto has puesto ha puesto hemos puesto habéis puesto han puesto",
              "futuro": "pondré pondrás pondrá pondremos pondréis pondrán",
              "imperativo": "pon ponga poned pongan"},
    "venir": {"perfecto": "he venido has venido ha venido hemos venido habéis venido han venido",
              "futuro": "vendré vendrás vendrá vendremos vendréis vendrán",
              "condicional": "vendría vendrías vendría vendríamos vendríais vendrían",
              "imperativo": "ven venga venid vengan"},
    "salir": {"futuro": "saldré saldrás saldrá saldremos saldréis saldrán",
              "condicional": "saldría saldrías saldría saldríamos saldríais saldrían",
              "imperativo": "sal salga salid salgan"},
    "caber": {"futuro": "cabré cabrás cabrá cabremos cabréis cabrán",
              "condicional": "cabría cabrías cabría cabríamos cabríais cabrían",
              "perfecto": "he cabido has cabido ha cabido hemos cabido habéis cabido han cabido"},
    "saber": {"futuro": "sabré sabrás sabrá sabremos sabréis sabrán",
              "condicional": "sabría sabrías sabría sabríamos sabríais sabrían",
              "imperativo": "sabe sepa sabed sepan"},
    "querer": {"futuro": "querré querrás querrá querremos querréis querrán",
               "condicional": "querría querrías querría querríamos querríais querrían",
               "imperativo": "quiere quiera quered quieran"},
    "poder": {"futuro": "podré podrás podrá podremos podréis podrán",
              "condicional": "podría podrías podría podríamos podríais podrían",
              "perfecto": "he podido has podido ha podido hemos podido habéis podido han podido"},
    "valer": {"futuro": "valdré valdrás valdrá valdremos valdréis valdrán",
              "condicional": "valdría valdrías valdría valdríamos valdríais valdrían"},
    "ver": {"perfecto": "he visto has visto ha visto hemos visto habéis visto han visto",
            "futuro": "veré verás verá veremos veréis verán",
            "imperativo": "ve vea ved vean"},
    "dar": {"futuro": "daré darás dará daremos daréis darán",
            "imperativo": "da dé dad den"},
    "volver": {"perfecto": "he vuelto has vuelto ha vuelto hemos vuelto habéis vuelto han vuelto",
               "futuro": "volveré volverás volverá volveremos volveréis volverán",
               "imperativo": "vuelve vuelva volved vuelvan"},
    "devolver": {"perfecto": "he devuelto has devuelto ha devuelto hemos devuelto habéis devuelto han devuelto"},
    "escribir": {"perfecto": "he escrito has escrito ha escrito hemos escrito habéis escrito han escrito",
                 "imperativo": "escribe escriba escribid escriban"},
    "abrir": {"perfecto": "he abierto has abierto ha abierto hemos abierto habéis abierto han abierto",
              "imperativo": "abre abra abrid abran"},
    "morir": {"perfecto": "he muerto has muerto ha muerto hemos muerto habéis muerto han muerto",
              "imperativo": "muere muera morid mueran"},
    "romperse": {"perfecto": "me he roto te has roto se ha roto nos hemos roto os habéis roto se han roto",
                 "imperativo": "rómpete rómpase rompeos rómpanse"},
    "leer": {"perfecto": "he leído has leído ha leído hemos leído habéis leído han leído",
             "imperativo": "lee lea leed lean"},
    "oír": {"perfecto": "he oído has oído ha oído hemos oído habéis oído han oído",
            "futuro": "oiré oirás oirá oiremos oiréis oirán",
            "imperativo": "oye oiga oíd oigan"},
    "traer": {"perfecto": "he traído has traído ha traído hemos traído habéis traído han traído",
              "imperativo": "trae traiga traed traigan"},
    "reír": {"perfecto": "he reído has reído ha reído hemos reído habéis reído han reído",
             "futuro": "reiré reirás reirá reiremos reiréis reirán",
             "imperativo": "ríe ría reíd rían"},
    "freír": {"perfecto": "he frito has frito ha frito hemos frito habéis frito han frito",
              "futuro": "freiré freirás freirá freiremos freiréis freirán"},
    "huir": {"perfecto": "he huido has huido ha huido hemos huido habéis huido han huido",
             "imperativo": "huye huya huid huyan"},
    "construir": {"perfecto": "he construido has construido ha construido hemos construido habéis construido han construido",
                  "imperativo": "construye construya construid construyan"},
    "resolver": {"perfecto": "he resuelto has resuelto ha resuelto hemos resuelto habéis resuelto han resuelto"},
    "deshacer": {"perfecto": "he deshecho has deshecho ha deshecho hemos deshecho habéis deshecho han deshecho",
                 "futuro": "desharé desharás deshará desharemos desharéis desharán",
                 "imperativo": "deshaz deshaga deshaced deshagan"},
    "bendecir": {"perfecto": "he bendecido has bendecido ha bendecido hemos bendecido habéis bendecido han bendecido",
                 "futuro": "bendeciré bendecirás bendecirá bendeciremos bendeciréis bendecirán",
                 "imperativo": "bendice bendiga bendecid bendigan"},
    "mantener": {"futuro": "mantendré mantendrás mantendrá mantendremos mantendréis mantendrán",
                 "imperativo": "mantén mantenga mantened mantengan"},
    "obtener": {"imperativo": "obtén obtenga obtened obtengan"},
    "proponer": {"perfecto": "he propuesto has propuesto ha propuesto hemos propuesto habéis propuesto han propuesto",
                 "futuro": "propondré propondrás propondrá propondremos propondréis propondrán",
                 "imperativo": "propón proponga proponed propongan"},
    "suponer": {"imperativo": "supón suponga suponed supongan"},
    "intervenir": {"futuro": "intervendré intervendrás intervendrá intervendremos intervendréis intervendrán",
                   "imperativo": "intervén intervenga intervenid intervengan"},
    "prevenir": {"imperativo": "prevén prevenga prevenid prevengan"},
    "prever": {"perfecto": "he previsto has previsto ha previsto hemos previsto habéis previsto han previsto",
               "imperativo": "prevé prevea preved prevean"},
    "seguir": {"imperativo": "sigue siga seguid sigan"},
    "conducir": {"imperativo": "conduce conduzca conducid conduzcan"},
    "pensar": {"imperativo": "piensa piense pensad piensen"},
    "dormir": {"imperativo": "duerme duerma dormid duerman"},
    "pedir": {"imperativo": "pide pida pedid pidan"},
    "jugar": {"imperativo": "juega juegue jugad jueguen"},
    "empezar": {"imperativo": "empieza empiece empezad empiecen"},
    "buscar": {"imperativo": "busca busque buscad busquen"},
    "llegar": {"imperativo": "llega llegue llegad lleguen"},
    "elegir": {"imperativo": "elige elija elegid elijan"},
    "convencer": {"imperativo": "convence convenza convenced convenzan"},
    "conocer": {"imperativo": "conoce conozca conoced conozcan"},
    # Pronominaux : le pronom soude, l'accent qui suit la syllabe tonique.
    "lavarse": {"perfecto": "me he lavado te has lavado se ha lavado nos hemos lavado os habéis lavado se han lavado",
                "futuro": "me lavaré te lavarás se lavará nos lavaremos os lavaréis se lavarán",
                "condicional": "me lavaría te lavarías se lavaría nos lavaríamos os lavaríais se lavarían",
                "imperativo": "lávate lávese lavaos lávense"},
    "levantarse": {"imperativo": "levántate levántese levantaos levántense"},
    "sentarse": {"imperativo": "siéntate siéntese sentaos siéntense"},
    "acostarse": {"imperativo": "acuéstate acuéstese acostaos acuéstense"},
    "dormirse": {"imperativo": "duérmete duérmase dormíos duérmanse"},
    "vestirse": {"imperativo": "vístete vístase vestíos vístanse"},
    "ponerse": {"perfecto": "me he puesto te has puesto se ha puesto nos hemos puesto os habéis puesto se han puesto",
                "futuro": "me pondré te pondrás se pondrá nos pondremos os pondréis se pondrán",
                "imperativo": "ponte póngase poneos pónganse"},
    "despertarse": {"imperativo": "despiértate despiértese despertaos despiértense"},
    "peinarse": {"imperativo": "péinate péinese peinaos péinense"},
    "afeitarse": {"imperativo": "aféitate aféitese afeitaos aféitense"},
    "graduarse": {"imperativo": "gradúate gradúese graduaos gradúense"},
    "situarse": {"imperativo": "sitúate sitúese situaos sitúense"},
    "cuidarse": {"imperativo": "cuídate cuídese cuidaos cuídense"},
    "preocuparse": {"imperativo": "preocúpate preocúpese preocupaos preocúpense"},
    "estropearse": {"imperativo": "estropéate estropéese estropeaos estropéense"},
    "tranquilizarse": {"imperativo": "tranquilízate tranquilícese tranquilizaos tranquilícense"},
    "rendirse": {"imperativo": "ríndete ríndase rendíos ríndanse"},
    "esforzarse": {"imperativo": "esfuérzate esfuércese esforzaos esfuércense"},
    "llamarse": {"imperativo": "llámate llámese llamaos llámense"},
    "sentirse": {"imperativo": "siéntete siéntase sentíos siéntanse"},
    "quitarse": {"imperativo": "quítate quítese quitaos quítense"},
    "irse": {"imperativo": "vete váyase idos váyanse"},
    "reciclarse profesionalmente": {"imperativo": "recíclate profesionalmente recíclese profesionalmente reciclaos profesionalmente recíclense profesionalmente",
                                    "futuro": "me reciclaré profesionalmente te reciclarás profesionalmente se reciclará profesionalmente nos reciclaremos profesionalmente os reciclaréis profesionalmente se reciclarán profesionalmente"},
    "juzgar moralmente": {"imperativo": "juzga moralmente juzgue moralmente juzgad moralmente juzguen moralmente",
                          "perfecto": "he juzgado moralmente has juzgado moralmente ha juzgado moralmente hemos juzgado moralmente habéis juzgado moralmente han juzgado moralmente"},
}


def charger():
    brut = io.open(CHEMIN, encoding="utf-8", newline="").read()
    return json.loads(brut), ("\r\n" if "\r\n" in brut else "\n")


def ecrire(d, fin):
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    io.open(CHEMIN, "w", encoding="utf-8", newline="").write(texte.replace("\n", fin))


def verifier_formes(tout):
    """Les VERIFS contre le calcul ; les verbes absents du corpus sont
    controles sur un verbe fictif (irse et oír ne sont pas dans le corpus)."""
    par_inf = {v["infinitif"]: v for v in tout}
    erreurs = []
    for inf, attendu in VERIFS.items():
        v = par_inf.get(inf)
        if v is None:
            if inf == "irse":
                v = {"infinitif": "irse", "praesens": {"er_sie_es": "se va"},
                     "subjuntivo": ["me vaya", "te vayas", "se vaya", "nos vayamos", "os vayáis", "se vayan"]}
            elif inf == "oír":
                v = {"infinitif": "oír", "praesens": {"er_sie_es": "oye"},
                     "subjuntivo": ["oiga", "oigas", "oiga", "oigamos", "oigáis", "oigan"]}
            else:
                erreurs.append("%s : absent du corpus" % inf)
                continue
        f = formes(v)
        for temps, chaine in attendu.items():
            obtenu = f[temps]
            if temps == "imperativo":
                obtenu = " ".join(obtenu[k] for k in ("tu", "usted", "vosotros", "ustedes")) if obtenu else ""
            else:
                obtenu = " ".join(obtenu)
            if obtenu != chaine:
                erreurs.append("%s %s :\n    attendu %s\n    obtenu  %s" % (inf, temps, chaine, obtenu))
    return erreurs


# ------------------------------------------------------------------ phrases

def sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def mots(phrase):
    return set(re.findall(r"[a-záéíóúüñ]+", sans_accent(phrase)))


def formes_du_temps(v, temps):
    """Les mots qui prouvent le temps dans une phrase : la forme conjuguee
    (sans pronom ni complement) ; pour le perfecto, le participe."""
    _, comp, pron = decouper(v["infinitif"])
    liste = v[temps] if temps in v else formes(v)[temps]
    out = set()
    for f in liste:
        f = f.replace(" " + comp, "") if comp else f
        f = f.split(" ")[-1] if (pron or temps == "perfecto") else f
        out.add(sans_accent(f))
    return out


def lire_lots():
    """{infinitif: {temps: [es, fr, en, pt]}} et les erreurs de forme."""
    phrases, erreurs = {}, []
    for chemin in sorted(glob.glob(os.path.join(LOTS, "*.txt"))):
        nom, inf = os.path.basename(chemin), None
        for n, ligne in enumerate(io.open(chemin, encoding="utf-8"), 1):
            ligne = ligne.rstrip("\r\n")
            if not ligne.strip():
                continue
            if ligne.startswith("#"):
                inf = ligne[1:].strip()
                if inf in phrases:
                    erreurs.append("%s:%d : %s en double" % (nom, n, inf))
                phrases[inf] = {}
                continue
            champs = [c.strip() for c in ligne.split("|")]
            if inf is None or len(champs) != 5 or champs[0] not in TEMPS_PHRASE or not all(champs):
                erreurs.append("%s:%d : ligne mal formee" % (nom, n))
                continue
            if champs[0] in phrases[inf]:
                erreurs.append("%s:%d : %s %s en double" % (nom, n, inf, champs[0]))
            phrases[inf][champs[0]] = champs[1:]
    return phrases, erreurs


def verifier_phrases(tout, phrases):
    par_inf = {v["infinitif"]: v for v in tout}
    erreurs = []
    for inf, par_temps in phrases.items():
        v = par_inf.get(inf)
        if v is None:
            erreurs.append("%s : pas dans verbos.json" % inf)
            continue
        f = formes(v)
        attendus = [t for t in TEMPS_PHRASE if (v.get(t) if t in ("preterito", "imperfecto", "subjuntivo") else f[t])
                    and (inf, t) not in SANS_PHRASE]
        manque = [t for t in attendus if t not in par_temps]
        if manque:
            erreurs.append("%s : sans %s" % (inf, ", ".join(manque)))
        for t in par_temps:
            if t not in attendus:
                erreurs.append("%s : une phrase pour %s, que ce verbe n'a pas" % (inf, t))
        for temps, textes in par_temps.items():
            es = textes[0]
            if not mots(es) & formes_du_temps(v, temps):
                erreurs.append("%s %s : aucune forme du temps dans « %s »" % (inf, temps, es))
            if temps == "perfecto" and not mots(es) & {"he", "has", "ha", "hemos", "habeis", "han"}:
                erreurs.append("%s perfecto : sans auxiliaire dans « %s »" % (inf, es))
            if len(set(textes)) < 4:
                erreurs.append("%s %s : deux textes identiques" % (inf, temps))
            if not es.rstrip().endswith((".", "?", "!")):
                erreurs.append("%s %s : ponctuation finale manquante" % (inf, temps))
    return erreurs


def etat(tout, phrases):
    for niv in ("A1", "A2", "B1", "B2"):
        verbes = [v for v in tout if v["_niveau"] == niv]
        faits = [v for v in verbes if all(v.get("exemple_" + t) or not v.get(t) or (v["infinitif"], t) in SANS_PHRASE
                                          for t in TEMPS_PHRASE)]
        en_lots = [v for v in verbes if v["infinitif"] in phrases]
        print("%s : %d verbes, %d avec leurs six phrases dans verbos.json, %d dans les lots"
              % (niv, len(verbes), len(faits), len(en_lots)))
        reste = [v["infinitif"] for v in verbes if v["infinitif"] not in phrases]
        if reste and len(reste) <= 40:
            print("   reste :", ", ".join(reste))


def main():
    d, fin = charger()
    tout = []
    for niv, liste in d.items():
        for v in liste:
            v["_niveau"] = niv
            tout.append(v)
    erreurs = verifier_formes(tout)
    if erreurs:
        print("FORMES FAUSSES (%d) :" % len(erreurs))
        print("\n".join(erreurs))
        sys.exit(1)
    print("formes : %d verifications a la main, toutes justes" % sum(len(x) for x in VERIFS.values()))
    phrases, erreurs = lire_lots()
    erreurs += verifier_phrases(tout, phrases)
    if erreurs:
        print("PHRASES REFUSEES (%d) :" % len(erreurs))
        print("\n".join(erreurs))
        sys.exit(1)
    print("phrases : %d verbes complets dans les lots" % len(phrases))

    if "--etat" in sys.argv:
        etat(tout, phrases)
    if "--ecrire" in sys.argv:
        n = 0
        for v in tout:
            f = formes(v)
            for k in ("perfecto", "futuro", "condicional", "imperativo"):
                if v.get(k) != f[k]:
                    n += 1
                v[k] = f[k]
        print("formes posees sur %d verbes (%d champs changes)" % (len(tout), n))
    if "--ejemplos" in sys.argv:
        n = 0
        for v in tout:
            for temps, textes in phrases.get(v["infinitif"], {}).items():
                for cle, texte in zip(["exemple_" + temps] + ["exemple_%s_%s" % (temps, l) for l in LANGUES], textes):
                    if v.get(cle) != texte:
                        n += 1
                    v[cle] = texte
        print("phrases posees : %d champs changes" % n)
    for v in tout:
        del v["_niveau"]
    if "--ecrire" in sys.argv or "--ejemplos" in sys.argv:
        ecrire(d, fin)
        print("ecrit :", CHEMIN)


if __name__ == "__main__":
    main()
