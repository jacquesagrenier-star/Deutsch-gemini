# -*- coding: utf-8 -*-
"""La conjugaison portugaise (du Portugal), pour construire.py.

Six personnes, dans l'ordre du moteur : eu, tu, ele/ela/voce, nos, vos,
eles/elas/voces. Vos est calcule (il existe dans les grammaires) mais le
moteur le cache : il est sorti de l'usage courant au Portugal.

Temps : presente, perfeito (preterito perfeito simples), imperfeito, futuro,
condicional, conjuntivo (presente do conjuntivo), imperativo (tu, voce, voces).

Ce qui distingue le Portugal du Bresil, et que ces tables suivent :
  - perfeito, 1re personne du pluriel des verbes en -ar : falAmos (accent),
    qui la distingue du present falamos ;
  - les pronominaux : le pronom apres le verbe, avec trait d'union (levanto-me,
    levantamo-nos -- le s tombe devant nos) ; au conjuntivo, avant (que eu me
    levante) ; pas de futur ni de conditionnel affiches pour eux (la mesoclise,
    levantar-me-ei, attendra le B1).
Orthographe de l'Accord de 1990 : veem, leem, deem (sans accent circonflexe).
"""
import re

PERSONNES = ["eu", "tu", "ele", "nós", "vós", "eles"]

# ---------------------------------------------------------------- irreguliers
# Chaque entree remplace le temps calcule ; un temps absent reste regulier.
IRR = {
 "ser": {
  "presente": "sou és é somos sois são",
  "perfeito": "fui foste foi fomos fostes foram",
  "imperfeito": "era eras era éramos éreis eram",
  "conjuntivo": "seja sejas seja sejamos sejais sejam",
  "imperativo": ("sê", "seja", "sejam")},
 "estar": {
  "presente": "estou estás está estamos estais estão",
  "perfeito": "estive estiveste esteve estivemos estivestes estiveram",
  "conjuntivo": "esteja estejas esteja estejamos estejais estejam",
  "imperativo": ("está", "esteja", "estejam")},
 "ter": {
  "presente": "tenho tens tem temos tendes têm",
  "perfeito": "tive tiveste teve tivemos tivestes tiveram",
  "imperfeito": "tinha tinhas tinha tínhamos tínheis tinham",
  "conjuntivo": "tenha tenhas tenha tenhamos tenhais tenham",
  "imperativo": ("tem", "tenha", "tenham")},
 "ir": {
  "presente": "vou vais vai vamos ides vão",
  "perfeito": "fui foste foi fomos fostes foram",
  "conjuntivo": "vá vás vá vamos vades vão",
  "imperativo": ("vai", "vá", "vão")},
 "vir": {
  "presente": "venho vens vem vimos vindes vêm",
  "perfeito": "vim vieste veio viemos viestes vieram",
  "imperfeito": "vinha vinhas vinha vínhamos vínheis vinham",
  "conjuntivo": "venha venhas venha venhamos venhais venham",
  "imperativo": ("vem", "venha", "venham")},
 "fazer": {
  "presente": "faço fazes faz fazemos fazeis fazem",
  "perfeito": "fiz fizeste fez fizemos fizestes fizeram",
  "futuro": "farei farás fará faremos fareis farão",
  "condicional": "faria farias faria faríamos faríeis fariam",
  "conjuntivo": "faça faças faça façamos façais façam",
  "imperativo": ("faz", "faça", "façam")},
 "dizer": {
  "presente": "digo dizes diz dizemos dizeis dizem",
  "perfeito": "disse disseste disse dissemos dissestes disseram",
  "futuro": "direi dirás dirá diremos direis dirão",
  "condicional": "diria dirias diria diríamos diríeis diriam",
  "conjuntivo": "diga digas diga digamos digais digam",
  "imperativo": ("diz", "diga", "digam")},
 "trazer": {
  "presente": "trago trazes traz trazemos trazeis trazem",
  "perfeito": "trouxe trouxeste trouxe trouxemos trouxestes trouxeram",
  "futuro": "trarei trarás trará traremos trareis trarão",
  "condicional": "traria trarias traria traríamos traríeis trariam",
  "conjuntivo": "traga tragas traga tragamos tragais tragam",
  "imperativo": ("traz", "traga", "tragam")},
 "poder": {
  "presente": "posso podes pode podemos podeis podem",
  "perfeito": "pude pudeste pôde pudemos pudestes puderam",
  "conjuntivo": "possa possas possa possamos possais possam",
  "imperativo": None},
 "querer": {
  "presente": "quero queres quer queremos quereis querem",
  "perfeito": "quis quiseste quis quisemos quisestes quiseram",
  "conjuntivo": "queira queiras queira queiramos queirais queiram",
  "imperativo": None},
 "saber": {
  "presente": "sei sabes sabe sabemos sabeis sabem",
  "perfeito": "soube soubeste soube soubemos soubestes souberam",
  "conjuntivo": "saiba saibas saiba saibamos saibais saibam",
  "imperativo": ("sabe", "saiba", "saibam")},
 "ver": {
  "presente": "vejo vês vê vemos vedes veem",
  "perfeito": "vi viste viu vimos vistes viram",
  "conjuntivo": "veja vejas veja vejamos vejais vejam",
  "imperativo": ("vê", "veja", "vejam")},
 "ler": {
  "presente": "leio lês lê lemos ledes leem",
  "conjuntivo": "leia leias leia leiamos leiais leiam",
  "imperativo": ("lê", "leia", "leiam")},
 "dar": {
  "presente": "dou dás dá damos dais dão",
  "perfeito": "dei deste deu demos destes deram",
  "conjuntivo": "dê dês dê demos deis deem",
  "imperativo": ("dá", "dê", "deem")},
 "pôr": {
  "presente": "ponho pões põe pomos pondes põem",
  "perfeito": "pus puseste pôs pusemos pusestes puseram",
  "imperfeito": "punha punhas punha púnhamos púnheis punham",
  "futuro": "porei porás porá poremos poreis porão",
  "condicional": "poria porias poria poríamos poríeis poriam",
  "conjuntivo": "ponha ponhas ponha ponhamos ponhais ponham",
  "imperativo": ("põe", "ponha", "ponham")},
 "ouvir": {
  "presente": "ouço ouves ouve ouvimos ouvis ouvem",
  "conjuntivo": "ouça ouças ouça ouçamos ouçais ouçam"},
 "pedir": {
  "presente": "peço pedes pede pedimos pedis pedem",
  "conjuntivo": "peça peças peça peçamos peçais peçam"},
 "perder": {
  "presente": "perco perdes perde perdemos perdeis perdem",
  "conjuntivo": "perca percas perca percamos percais percam"},
 "sair": {
  "presente": "saio sais sai saímos saís saem",
  "perfeito": "saí saíste saiu saímos saístes saíram",
  "imperfeito": "saía saías saía saíamos saíeis saíam",
  "conjuntivo": "saia saias saia saiamos saiais saiam",
  "imperativo": ("sai", "saia", "saiam")},
 "doer": {
  "presente": "doo dóis dói doemos doeis doem",
  "perfeito": "doí doeste doeu doemos doestes doeram",
  "imperfeito": "doía doías doía doíamos doíeis doíam",
  "imperativo": None},
 "subir": {
  "presente": "subo sobes sobe subimos subis sobem",
  "imperativo": ("sobe", "suba", "subam")},
 "dormir": {"presente": "durmo dormes dorme dormimos dormis dormem"},
 "sentir": {"presente": "sinto sentes sente sentimos sentis sentem"},
 "vestir": {"presente": "visto vestes veste vestimos vestis vestem"},
 "servir": {"presente": "sirvo serves serve servimos servis servem"},
 "repetir": {"presente": "repito repetes repete repetimos repetis repetem"},
 "conduzir": {"presente": "conduzo conduzes conduz conduzimos conduzis conduzem",
              "imperativo": ("conduz", "conduza", "conduzam")},
 "chover": {"presente": "— — chove — — —", "perfeito": "— — choveu — — —",
            "imperfeito": "— — chovia — — —", "futuro": "— — choverá — — —",
            "condicional": "— — choveria — — —", "conjuntivo": "— — chova — — —", "imperativo": None},
 "nevar": {"presente": "— — neva — — —", "perfeito": "— — nevou — — —",
           "imperfeito": "— — nevava — — —", "futuro": "— — nevará — — —",
           "condicional": "— — nevaria — — —", "conjuntivo": "— — neve — — —", "imperativo": None},
}

# Les verbes en -ear prennent un i aux formes accentuees sur le radical.
def _ear(radical, finales):
    return [radical + ("i" if i in (0, 1, 2, 5) else "") + f for i, f in enumerate(finales)]


def _liste(s):
    return s.split() if isinstance(s, str) else list(s)


# ---------------------------------------------------------------- reguliers
def _graphie_a(rad, e_suit):
    """Le radical d'un verbe en -ar devant e (ficar -> fiqu-e, chegar -> chegu-e,
    comecar -> comec-e)."""
    if not e_suit:
        return rad
    if rad.endswith("c"):
        return rad[:-1] + "qu"
    if rad.endswith("g"):
        return rad[:-1] + "gu"
    if rad.endswith("ç"):
        return rad[:-1] + "c"
    return rad


def _graphie_er_ir(rad, a_o_suit):
    """Le radical d'un verbe en -er / -ir devant a ou o (conhecer -> conheç-o,
    dirigir -> dirij-o, seguir -> sig-o)."""
    if not a_o_suit:
        return rad
    if rad.endswith("c"):
        return rad[:-1] + "ç"
    if rad.endswith("gu"):
        return rad[:-1]
    if rad.endswith("g"):
        return rad[:-1] + "j"
    return rad


def regulier(inf):
    rad, fin = inf[:-2], inf[-2:]
    t = {}
    if fin == "ar":
        if inf.endswith("ear"):
            r = inf[:-3] + "e"
            t["presente"] = _ear(r, ["o", "as", "a", "amos", "ais", "am"])
            t["conjuntivo"] = _ear(r, ["e", "es", "e", "emos", "eis", "em"])
        else:
            t["presente"] = [rad + f for f in ["o", "as", "a", "amos", "ais", "am"]]
            e = _graphie_a(rad, True)
            t["conjuntivo"] = [e + f for f in ["e", "es", "e", "emos", "eis", "em"]]
        t["perfeito"] = [_graphie_a(rad, True) + "ei"] + [rad + f for f in ["aste", "ou", "ámos", "astes", "aram"]]
        t["imperfeito"] = [rad + f for f in ["ava", "avas", "ava", "ávamos", "áveis", "avam"]]
    else:
        v = fin[0]
        o = _graphie_er_ir(rad, True)
        t["presente"] = [o + "o"] + [rad + f for f in
                                     (["es", "e", "emos", "eis", "em"] if v == "e" else ["es", "e", "imos", "is", "em"])]
        t["conjuntivo"] = [o + f for f in ["a", "as", "a", "amos", "ais", "am"]]
        t["perfeito"] = [rad + f for f in
                         (["i", "este", "eu", "emos", "estes", "eram"] if v == "e" else ["i", "iste", "iu", "imos", "istes", "iram"])]
        t["imperfeito"] = [rad + f for f in ["ia", "ias", "ia", "íamos", "íeis", "iam"]]
    t["futuro"] = [inf + f for f in ["ei", "ás", "á", "emos", "eis", "ão"]]
    t["condicional"] = [inf + f for f in ["ia", "ias", "ia", "íamos", "íeis", "iam"]]
    return t


def conjuguer(inf):
    """{temps: [6 formes]}, imperativo = {tu, voce, voces} ou None."""
    base = inf[:-3] if inf.endswith("-se") else inf
    t = regulier(base if base != "pôr" else "por")
    irr = IRR.get(base, {})
    for temps, formes in irr.items():
        if temps != "imperativo":
            t[temps] = _liste(formes)
    # Un present irregulier (durmo, sinto, peco) refait le conjuntivo s'il
    # n'est pas donne : il part de la 1re personne du present.
    if "presente" in irr and "conjuntivo" not in irr and t["presente"][0] != "—":
        r = t["presente"][0][:-1]
        voy = "e" if base.endswith("ar") else "a"
        t["conjuntivo"] = [r + f for f in ([voy, voy + "s", voy, voy + "mos", voy + "is", voy + "m"]
                                           if voy == "a" else ["e", "es", "e", "emos", "eis", "em"])]
    if "imperativo" in irr:
        imp = irr["imperativo"]
        t["imperativo"] = None if imp is None else {"tu": imp[0], "voce": imp[1], "voces": imp[2]}
    else:
        t["imperativo"] = {"tu": t["presente"][2], "voce": t["conjuntivo"][2], "voces": t["conjuntivo"][5]}
    if inf.endswith("-se"):
        t = pronominal(t)
    return t


# ---------------------------------------------------------------- pronominaux
PRONOMS = ["me", "te", "se", "nos", "vos", "se"]


def _enclise(forme, i):
    """levanto + me -> levanto-me ; levantamos + nos -> levantamo-nos."""
    if forme == "—":
        return forme
    if i == 3 and forme.endswith("s"):
        forme = forme[:-1]
    return forme + "-" + PRONOMS[i]


def pronominal(t):
    out = {}
    for temps in ("presente", "perfeito", "imperfeito"):
        out[temps] = [_enclise(f, i) for i, f in enumerate(t[temps])]
    # Le conjuntivo suit « que » : le pronom passe devant.
    out["conjuntivo"] = [PRONOMS[i] + " " + f for i, f in enumerate(t["conjuntivo"])]
    out["futuro"] = None
    out["condicional"] = None
    imp = t.get("imperativo")
    out["imperativo"] = None if not imp else {
        "tu": imp["tu"] + "-te", "voce": imp["voce"] + "-se", "voces": imp["voces"] + "-se"}
    return out


def praesens(t):
    """Le present sous les cles du moteur (ich, du, er_sie_es...)."""
    return dict(zip(["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"], t["presente"]))


def irregulier(inf):
    base = inf[:-3] if inf.endswith("-se") else inf
    return base in IRR and base not in ("chover", "nevar")


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for v in sys.argv[1:] or ["falar", "comer", "partir", "ficar", "conhecer", "passear", "dormir", "ter",
                              "levantar-se", "chegar", "começar", "subir", "pôr", "ler", "doer"]:
        c = conjuguer(v)
        print(v)
        for k, f in c.items():
            print("   %-12s %s" % (k, f))
