# -*- coding: utf-8 -*-
"""La conjugaison du portugais d'Europe (A2-C1) : les regles et les verbes
irreguliers. SOURCE : c'est ici qu'on corrige une forme.

    conjuguer("fazer") -> {"presente": [6], "perfeito": [6], "imperfeito": [6],
        "mais_que_perfeito": [6] (composto : tinha feito), "futuro": [6],
        "condicional": [6], "conj_presente": [6], "conj_imperfeito": [6],
        "conj_futuro": [6], "perfeito_composto": [6] (tenho feito),
        "imperativo": {"tu", "voce", "nos", "vos", "voces"},
        "participio", "gerundio", "irregulier": bool}

Les six personnes : eu, tu, ele/ela/você, nós, vós, eles/elas/vocês. Le « vós »
est donne pour etre complet (il vit encore dans le Nord et a l'eglise) ;
l'ecran peut le cacher. Le portugais d'EUROPE : « falámos » (passe, avec
accent) face a « falamos » (present) ; « aceite » participe de aceitar ;
« facto », « receção »... (accord orthographique de 1990).

    python portugais/outils/irreguliers.py fazer pôr incluir   (affiche)
"""
import re

PERSONNES = ["eu", "tu", "ele/ela", "nós", "vós", "eles/elas"]

# ------------------------------------------------------------------ les irreguliers
# Pour chaque verbe : ce qui ne suit pas la regle. « pres » et « pret » : les
# six formes ; « imp » : l'imperfeito s'il est irregulier ; « fut » : le
# radical du futur et du conditionnel ; « conj » : le radical du subjonctif
# present (sinon : la 1re personne du present, moins -o) ; « part » : le
# participe ; « imper_tu » : l'imperatif de tu s'il n'est pas le present moins -s.
IRREG = {
    "ser": dict(pres="sou és é somos sois são", pret="fui foste foi fomos fostes foram",
                imp="era eras era éramos éreis eram", conj6="seja sejas seja sejamos sejais sejam",
                part="sido", imper_tu="sê", imper_vos="sede"),
    "ir": dict(pres="vou vais vai vamos ides vão", pret="fui foste foi fomos fostes foram",
               conj6="vá vás vá vamos vades vão", part="ido", imper_tu="vai", imper_vos="ide"),
    "estar": dict(pres="estou estás está estamos estais estão", pret="estive estiveste esteve estivemos estivestes estiveram",
                  conj6="esteja estejas esteja estejamos estejais estejam", part="estado", imper_tu="está"),
    "ter": dict(pres="tenho tens tem temos tendes têm", pret="tive tiveste teve tivemos tivestes tiveram",
                imp="tinha tinhas tinha tínhamos tínheis tinham", conj="tenh", part="tido", imper_tu="tem", imper_vos="tende"),
    "haver": dict(pres="hei hás há havemos haveis hão", pret="houve houveste houve houvemos houvestes houveram",
                  conj="haj", part="havido", imper_tu="há"),
    "vir": dict(pres="venho vens vem vimos vindes vêm", pret="vim vieste veio viemos viestes vieram",
                imp="vinha vinhas vinha vínhamos vínheis vinham", conj="venh", part="vindo", ger="vindo",
                imper_tu="vem", imper_vos="vinde"),
    "fazer": dict(pres="faço fazes faz fazemos fazeis fazem", pret="fiz fizeste fez fizemos fizestes fizeram",
                  fut="far", part="feito", imper_tu="faz"),
    "dizer": dict(pres="digo dizes diz dizemos dizeis dizem", pret="disse disseste disse dissemos dissestes disseram",
                  fut="dir", part="dito", imper_tu="diz"),
    "trazer": dict(pres="trago trazes traz trazemos trazeis trazem", pret="trouxe trouxeste trouxe trouxemos trouxestes trouxeram",
                   fut="trar", part="trazido", imper_tu="traz"),
    "poder": dict(pres="posso podes pode podemos podeis podem", pret="pude pudeste pôde pudemos pudestes puderam",
                  part="podido"),
    "querer": dict(pres="quero queres quer queremos quereis querem", pret="quis quiseste quis quisemos quisestes quiseram",
                   conj="queir", part="querido", imper_tu="quer"),
    "saber": dict(pres="sei sabes sabe sabemos sabeis sabem", pret="soube soubeste soube soubemos soubestes souberam",
                  conj="saib", part="sabido"),
    "ver": dict(pres="vejo vês vê vemos vedes veem", pret="vi viste viu vimos vistes viram",
                part="visto", imper_tu="vê", imper_vos="vede"),
    "dar": dict(pres="dou dás dá damos dais dão", pret="dei deste deu demos destes deram",
                conj6="dê dês dê demos deis deem", part="dado", imper_tu="dá"),
    "pôr": dict(pres="ponho pões põe pomos pondes põem", pret="pus puseste pôs pusemos pusestes puseram",
                imp="punha punhas punha púnhamos púnheis punham", fut="por", conj="ponh", part="posto",
                ger="pondo", imper_tu="põe", imper_vos="ponde"),
    "ler": dict(pres="leio lês lê lemos ledes leem", pret="li leste leu lemos lestes leram",
                conj="lei", part="lido", imper_tu="lê", imper_vos="lede"),
    "crer": dict(pres="creio crês crê cremos credes creem", pret="cri creste creu cremos crestes creram",
                 conj="crei", part="crido", imper_tu="crê", imper_vos="crede"),
    "rir": dict(pres="rio ris ri rimos rides riem", pret="ri riste riu rimos ristes riram",
                imp="ria rias ria ríamos ríeis riam", part="rido", imper_tu="ri", imper_vos="ride"),
    "ouvir": dict(pres="ouço ouves ouve ouvimos ouvis ouvem", part="ouvido"),
    "pedir": dict(pres="peço pedes pede pedimos pedis pedem", part="pedido"),
    "medir": dict(pres="meço medes mede medimos medis medem", part="medido"),
    "perder": dict(pres="perco perdes perde perdemos perdeis perdem", part="perdido"),
    "valer": dict(pres="valho vales vale valemos valeis valem", part="valido"),
    "caber": dict(pres="caibo cabes cabe cabemos cabeis cabem", pret="coube coubeste coube coubemos coubestes couberam",
                  part="cabido"),
    "sair": dict(pres="saio sais sai saímos saís saem", part="saído"),
    "cair": dict(pres="caio cais cai caímos caís caem", part="caído"),
    "construir": dict(pres="construo constróis constrói construímos construís constroem", part="construído"),
    "destruir": dict(pres="destruo destróis destrói destruímos destruís destroem", part="destruído"),
    "odiar": dict(pres="odeio odeias odeia odiamos odiais odeiam", conj="odei", part="odiado", imper_tu="odeia"),
    "requerer": dict(pres="requeiro requeres requer requeremos requereis requerem", conj="requeir", part="requerido"),
    "reaver": dict(pres="- - - reavemos reaveis -", pret="reouve reouveste reouve reouvemos reouvestes reouveram",
                   part="reavido"),
    "prover": dict(pres="provejo provês provê provemos provedes proveem", part="provido"),
    "polir": dict(pres="pulo pules pule polimos polis pulem", part="polido"),
    "aderir": dict(pres="adiro aderes adere aderimos aderis aderem", part="aderido"),
    "frigir": dict(pres="frijo freges frege frigimos frigis fregem", part="frito"),
}
# Les composes : le prefixe + la conjugaison du verbe simple.
COMPOSES = {
    "ter": "conter obter manter deter reter entreter suster ater abster",
    "vir": "convir intervir provir advir sobrevir",
    "fazer": "desfazer refazer satisfazer perfazer contrafazer",
    "dizer": "contradizer bendizer maldizer predizer",
    "pôr": "propor compor dispor impor supor expor opor repor depor pressupor decompor sobrepor transpor antepor recompor",
    "ver": "prever rever antever entrever",
    "trazer": "",
    "sair": "",
    "cair": "recair decair",
    "pedir": "despedir expedir impedir",
    "medir": "",
    "valer": "equivaler desvaler",
    "rir": "sorrir",
    "ouvir": "",
    "haver": "",
    "crer": "descrer",
}

# Les alternances de l'-ir : e -> i (1re pers. et subjonctif) ; o -> u ; u -> o.
E_I = set("""sentir consentir ressentir pressentir mentir desmentir preferir referir conferir transferir inferir
interferir ferir sugerir digerir ingerir gerir vestir revestir investir despir servir seguir conseguir perseguir
prosseguir repetir competir refletir divertir advertir converter? convergir divergir discernir""".replace("?", "").split())
E_I_FORT = set("progredir agredir transgredir prevenir denegrir".split())  # aussi tu, ele, eles
O_U = set("dormir cobrir descobrir encobrir recobrir tossir engolir".split())
U_O = set("subir fugir sacudir acudir consumir cuspir sumir bulir".split())
# -iar qui se conjuguent comme -ear (odeio) : M-A-R-I-O-
IAR_EAR = set("ansiar incendiar mediar remediar intermediar".split())

# Les participes irreguliers (le regulier, s'il existe aussi, sert avec ter).
PARTICIPES = {
    "abrir": "aberto", "reabrir": "reaberto", "entreabrir": "entreaberto", "cobrir": "coberto", "descobrir": "descoberto",
    "encobrir": "encoberto", "recobrir": "recoberto", "escrever": "escrito", "descrever": "descrito",
    "inscrever": "inscrito", "prescrever": "prescrito", "reescrever": "reescrito", "subscrever": "subscrito",
    "transcrever": "transcrito", "ganhar": "ganho", "gastar": "gasto", "pagar": "pago", "aceitar": "aceite",
    "entregar": "entregue", "morrer": "morto", "imprimir": "impresso", "suspender": "suspenso",
    "expulsar": "expulso", "eleger": "eleito", "prender": "preso", "acender": "aceso", "limpar": "limpo",
    "salvar": "salvo", "soltar": "solto", "envolver": "envolvido", "frigir": "frito", "fritar": "frito",
    "matar": "morto", "romper": "roto",
}


def _six(s):
    return s.split()


# ------------------------------------------------------------------ l'orthographe
def _devant_e(radical, inf):
    """Le radical d'un verbe en -ar devant -e (subjonctif, passe 1re pers.) :
    ficar -> fiqu, pagar -> pagu, começar -> comec."""
    if inf.endswith("car"):
        return radical[:-1] + "qu"
    if inf.endswith("gar"):
        return radical + "u"
    if inf.endswith("çar"):
        return radical[:-1] + "c"
    return radical


def _devant_a_o(radical, inf):
    """Le radical d'un verbe en -er / -ir devant -a / -o : conhecer -> conheç,
    proteger -> protej, distinguir -> disting, erguer -> erg."""
    if inf.endswith(("cer", "cir")):
        return radical[:-1] + "ç"
    if inf.endswith(("ger", "gir")):
        return radical[:-1] + "j"
    if inf.endswith(("guer", "guir")):
        return radical[:-1]
    return radical


def _accent_tonique(stem):
    """La voyelle avant -ssemos prend l'accent : fala -> falá, fize -> fizé,
    come -> comê, parti -> partí, fo -> fô."""
    return stem


def _subj_imparfait(pret3pl, inf, base_reg):
    """falaram -> falasse... ; fizeram -> fizesse, fizéssemos."""
    st = pret3pl[:-3]  # « fala », « fize », « parti », « fo »
    der = st[-1]
    if der == "a":
        acc = st[:-1] + "á"
    elif der == "i":
        acc = st[:-1] + "í"
    elif der == "o":
        acc = st[:-1] + "ô"
    elif der == "e":
        # regulier en -er (comeram, leram, creram) : ê ; parfait fort : é
        acc = st[:-1] + ("ê" if base_reg else "é")
    else:
        acc = st
    ci = [st + "sse", st + "sses", st + "sse", acc + "ssemos", acc + "sseis", st + "ssem"]
    cf = [st + "r", st + "res", st + "r", st + "rmos", st + "rdes", st + "rem"]
    return ci, cf


def _hiatus(radical):
    return radical[-1:] in "aou" and radical[-2:] not in ("gu", "qu")


# ------------------------------------------------------------------ la conjugaison
def conjuguer(inf):
    inf = inf.strip()
    # Une locution (tomar conta de, dar-se bem com) : le premier mot se
    # conjugue, la suite reste.
    if " " in inf:
        tete, reste = inf.split(" ", 1)
        t = conjuguer(tete)

        def suite(f):
            return f if f in ("-", "") else f + " " + reste
        out = {}
        for k, v in t.items():
            if isinstance(v, list):
                out[k] = [suite(f) for f in v]
            elif isinstance(v, dict):
                out[k] = {kk: suite(vv) for kk, vv in v.items()}
            elif k in ("participio", "gerundio"):
                out[k] = v
            else:
                out[k] = v
        out["infinitif"] = inf
        return out
    pronominal = inf.endswith("-se")
    if pronominal:
        inf = inf[:-3]
    simple, prefixe = inf, ""
    if inf not in IRREG:
        for base, liste in COMPOSES.items():
            for c in liste.split():
                if inf == c:
                    simple, prefixe = base, c[:len(c) - len(base)] if c.endswith(base) else None
                    if prefixe is None:  # pôr -> propor : « pro » + « por »
                        prefixe = c[:-3]
        # Tout verbe en -or est un compose de pôr (contrapor, justapor...).
        if not prefixe and inf.endswith("or") and len(inf) > 3:
            simple, prefixe = "pôr", inf[:-3]
    t = _conjuguer_simple(simple)
    if prefixe:
        t = _prefixer(t, prefixe, simple)
    t["infinitif"] = inf + ("-se" if pronominal else "")
    if pronominal:
        t = _pronominal(t)
    return t


def _prefixer(t, prefixe, simple):
    def p(f):
        if f in ("-", ""):
            return f
        if simple == "pôr":
            f = f.replace("pôr", "por")
        # Les accents des composes : contém, obtém, convém, mantém (« tem » -> « tém »)
        f2 = prefixe + f
        f2 = re.sub(r"(t|v)em$", r"\1ém", f2) if simple in ("ter", "vir") else f2
        f2 = re.sub(r"(t|v)ens$", r"\1éns", f2) if simple in ("ter", "vir") else f2
        if simple == "pôr" and f2.endswith("pôs"):
            pass
        return f2
    out = {}
    for k, v in t.items():
        if isinstance(v, list):
            out[k] = [" ".join(p(x) if i == len(f.split()) - 1 else x for i, x in enumerate(f.split())) for f in v]
        elif isinstance(v, dict):
            out[k] = {kk: p(vv) for kk, vv in v.items()}
        elif isinstance(v, str):
            out[k] = p(v)
        else:
            out[k] = v
    # « tem » (3e sing.) -> contém ; « têm » (3e plur.) reste contêm ; « vem » -> convém
    if simple == "ter":
        out["presente"][2] = prefixe + "tém"
        out["imperativo"]["tu"] = prefixe + "tém"
    if simple == "vir":
        out["presente"][2] = prefixe + "vém"
        out["imperativo"]["tu"] = prefixe + "vém"
    if simple == "ver":
        pass
    return out


def _conjuguer_simple(inf):
    irr = IRREG.get(inf, {})
    if inf == "pôr":
        groupe, radical = "er", "p"
    else:
        groupe, radical = inf[-2:], inf[:-2]
    ear = inf.endswith("ear") or inf in IAR_EAR
    hiatus = groupe == "ir" and _hiatus(radical)  # sair, incluir, construir

    # --- present
    if "pres" in irr:
        pres = _six(irr["pres"])
    elif groupe == "ar":
        if ear:
            r = radical[:-1] if inf.endswith("ear") else radical[:-1]
            r = radical[:-1] if inf.endswith("ear") else radical[:-1] + "e"
            r1 = (radical[:-1] + "ei") if inf.endswith("ear") else (radical[:-1] + "ei")
            pres = [r1 + "o", r1 + "as", r1 + "a", radical + "amos", radical + "ais", r1 + "am"]
        else:
            pres = [radical + "o", radical + "as", radical + "a", radical + "amos", radical + "ais", radical + "am"]
    elif groupe == "er":
        r0 = _devant_a_o(radical, inf)
        pres = [r0 + "o", radical + "es", radical + "e", radical + "emos", radical + "eis", radical + "em"]
    else:
        r0 = _devant_a_o(radical, inf)
        if hiatus:
            pres = [radical + "o", radical + "is", radical + "i", radical + "ímos", radical + "ís", radical + "em"]
        else:
            pres = [r0 + "o", radical + "es", radical + "e", radical + "imos", radical + "is", radical + "em"]
        if inf in E_I or inf in E_I_FORT:
            i = radical.rfind("e")
            ri = radical[:i] + "i" + radical[i + 1:]
            pres[0] = _devant_a_o(ri, inf) + "o"
            if inf in E_I_FORT:
                pres[1], pres[2], pres[5] = ri + "es", ri + "e", ri + "em"
        if inf in O_U:
            i = radical.rfind("o")
            pres[0] = radical[:i] + "u" + radical[i + 1:] + "o"
        if inf in U_O:
            i = radical.rfind("u")
            ro = radical[:i] + "o" + radical[i + 1:]
            pres[1], pres[2], pres[5] = ro + "es", ro + "e", ro + "em"
            pres[0] = _devant_a_o(radical, inf) + "o"

    # --- perfeito
    if "pret" in irr:
        pret = _six(irr["pret"])
    elif groupe == "ar":
        r = _devant_e(radical, inf)
        pret = [r + "ei", radical + "aste", radical + "ou", radical + "ámos", radical + "astes", radical + "aram"]
    elif groupe == "er":
        pret = [radical + "i", radical + "este", radical + "eu", radical + "emos", radical + "estes", radical + "eram"]
    else:
        if hiatus:
            pret = [radical + "í", radical + "íste", radical + "iu", radical + "ímos", radical + "ístes", radical + "íram"]
        else:
            pret = [radical + "i", radical + "iste", radical + "iu", radical + "imos", radical + "istes", radical + "iram"]

    # --- imperfeito
    if "imp" in irr:
        imp = _six(irr["imp"])
    elif groupe == "ar":
        imp = [radical + x for x in ("ava", "avas", "ava", "ávamos", "áveis", "avam")]
    else:
        i_ = "í" if (hiatus or (groupe == "er" and radical[-1:] in "aeo" and inf not in ("ler", "crer"))) else "i"
        imp = [radical + i_ + "a", radical + i_ + "as", radical + i_ + "a", radical + "íamos", radical + "íeis", radical + i_ + "am"]

    # --- futuro, condicional
    fut_r = irr.get("fut", inf if inf != "pôr" else "por")
    futuro = [fut_r + x for x in ("ei", "ás", "á", "emos", "eis", "ão")]
    cond = [fut_r + x for x in ("ia", "ias", "ia", "íamos", "íeis", "iam")]

    # --- conjuntivo presente
    if "conj6" in irr:
        cp = _six(irr["conj6"])
    else:
        if "conj" in irr:
            rc = irr["conj"]
        elif groupe == "ar":
            rc = _devant_e(radical, inf)
            if ear:
                rc = radical[:-1] + "ei" if inf.endswith("ear") else radical[:-1] + "ei"
        else:
            rc = pres[0][:-1] if pres[0] not in ("-",) else radical
        v = "e" if groupe == "ar" else "a"
        cp = [rc + v, rc + v + "s", rc + v, rc + v + "mos", rc + v + "is", rc + v + "m"]
        if groupe == "ar" and ear:
            r = _devant_e(radical, inf)
            cp[3], cp[4] = r + "emos", r + "eis"
        if groupe == "ar" and not ear:
            r = _devant_e(radical, inf)
            cp = [r + "e", r + "es", r + "e", r + "emos", r + "eis", r + "em"]

    # --- conjuntivo imperfeito et futuro, a partir du passe (3e plur.)
    base_reg = "pret" not in irr and groupe == "er" or inf in ("ler", "crer", "ver", "prover")
    ci, cf = _subj_imparfait(pret[5], inf, base_reg)
    if inf in ("ser", "ir"):
        ci = ["fosse", "fosses", "fosse", "fôssemos", "fôsseis", "fossem"]
    if hiatus:  # incluísse, saísse ; incluíres, saíres
        st = radical + "í"
        ci = [st + "sse", st + "sses", st + "sse", st + "ssemos", st + "sseis", st + "ssem"]
        cf = [radical + "ir", radical + "íres", radical + "ir", radical + "irmos", radical + "irdes", radical + "írem"]

    # --- participe, gerondif
    part = irr.get("part") or PARTICIPES.get(inf)
    if not part:
        part = radical + ("ado" if groupe == "ar" else ("ído" if hiatus else "ido"))
    ger = irr.get("ger") or (radical + {"ar": "ando", "er": "endo", "ir": "indo"}[groupe] if inf != "pôr" else "pondo")

    # --- imperatif
    tu = irr.get("imper_tu") or (pres[1][:-1] if pres[1].endswith("s") else pres[2])
    if "imper_tu" not in irr and groupe != "ar" and not hiatus:
        tu = pres[2]
    vos = irr.get("imper_vos") or (pres[4][:-1] if pres[4].endswith("s") else pres[4])
    if groupe == "ir" and not hiatus and "imper_vos" not in irr:
        vos = radical + "i"
    if hiatus and "imper_vos" not in irr:
        vos = radical + "í"
    imper = {"tu": tu, "voce": cp[2], "nos": cp[3], "vos": vos, "voces": cp[5]}

    ter_imp = IRREG["ter"]["imp"].split() if "imp" in IRREG["ter"] else None
    ter_pres = IRREG["ter"]["pres"].split()
    return {
        "presente": pres, "perfeito": pret, "imperfeito": imp,
        "mais_que_perfeito": [a + " " + part for a in ter_imp],
        "perfeito_composto": [a + " " + part for a in ter_pres],
        "futuro": futuro, "condicional": cond,
        "conj_presente": cp, "conj_imperfeito": ci, "conj_futuro": cf,
        "imperativo": imper, "participio": part, "gerundio": ger,
        "irregulier": bool(irr) or inf in PARTICIPES or inf in E_I or inf in O_U or inf in U_O or inf in E_I_FORT,
    }


PRONOMS = ["me", "te", "se", "nos", "vos", "se"]


def _pronominal(t):
    """lembrar-se : lembro-me, lembras-te... ; futur : lembrar-me-ei (mesoclise)."""
    def encl(formes):
        out = []
        for f, p in zip(formes, PRONOMS):
            if f == "-":
                out.append(f)
                continue
            if p == "nos" and f.endswith("mos"):
                f = f[:-1]
            out.append(f + "-" + p)
        return out

    def meso(formes):
        out = []
        for f, p in zip(formes, PRONOMS):
            m = re.match(r"^(.*r)(ei|ás|á|emos|eis|ão|ia|ias|íamos|íeis|iam)$", f)
            out.append(m.group(1) + "-" + p + "-" + m.group(2) if m else f + "-" + p)
        return out

    def comp(formes):  # tinha-se lembrado
        return [f.split(" ")[0] + "-" + p + " " + f.split(" ")[1] if p != "nos" or not f.split(" ")[0].endswith("mos")
                else f.split(" ")[0][:-1] + "-nos " + f.split(" ")[1] for f, p in zip(formes, PRONOMS)]

    def procl(formes, mot):  # subjonctif : que eu me lembre
        return [mot + " " + p + " " + f for f, p in zip(formes, PRONOMS)]

    out = dict(t)
    for k in ("presente", "perfeito", "imperfeito"):
        out[k] = encl(t[k])
    for k in ("futuro", "condicional"):
        out[k] = meso(t[k])
    for k in ("mais_que_perfeito", "perfeito_composto"):
        out[k] = comp(t[k])
    out["conj_presente"] = procl(t["conj_presente"], "que")
    out["conj_imperfeito"] = procl(t["conj_imperfeito"], "se")
    out["conj_futuro"] = procl(t["conj_futuro"], "quando")
    im = t["imperativo"]
    out["imperativo"] = {"tu": im["tu"] + "-te", "voce": im["voce"] + "-se", "nos": im["nos"][:-1] + "-nos",
                         "vos": im["vos"] + "-vos", "voces": im["voces"] + "-se"}
    return out


def est_irregulier(inf):
    return conjuguer(inf)["irregulier"]


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    for v in sys.argv[1:] or ["falar", "comer", "partir", "fazer", "pôr", "propor", "manter", "incluir", "passear",
                              "conhecer", "ficar", "seguir", "dormir", "subir", "lembrar-se", "sair", "ler", "aceitar"]:
        t = conjuguer(v)
        print("==", t["infinitif"], "(irr)" if t["irregulier"] else "")
        for k in ("presente", "perfeito", "imperfeito", "futuro", "condicional", "conj_presente", "conj_imperfeito",
                  "conj_futuro", "mais_que_perfeito"):
            print("  %-18s %s" % (k, ", ".join(t[k])))
        print("  %-18s %s" % ("imperativo", t["imperativo"]))
        print("  %-18s %s / %s" % ("part. / ger.", t["participio"], t["gerundio"]))
