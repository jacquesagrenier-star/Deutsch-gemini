# -*- coding: utf-8 -*-
"""Des questions de temps tirees de NOS phrases d'exemple (30 oct. 2026), pour
allonger les series « par temps » et les fiches de temps vers le volume de
l'anglais, sans ecrire des centaines de phrases inventees.

Le principe : dans chaque phrase d'exemple A2-C1 (cartes de verbes, de noms,
d'adjectifs...), irreguliers.py cherche un verbe conjugue dont la forme
n'appartient qu'a UN temps ; on le remplace par ___ avec son infinitif entre
parentheses ; les mauvaises reponses sont le meme verbe, a la meme personne,
aux temps qu'on confond avec lui (perfeito / imperfeito / presente...). La
traduction est celle de la carte. Rien n'est ecrit a la main ici : on corrige
la phrase dans sa source, et la question suit.

    supplements(jeu) -> {serie: [questions au format des series]}

Appele par niveaux.py apres les fiches et les series par temps.
"""
import re

import irreguliers as I

# temps -> (series qui le recoivent, temps des mauvaises reponses, nom pour l'explication)
TEMPS = {
    "perfeito": (["tempsPerfeitoPtExercises", "perfeitoImperfeitoPtExercises"], ["imperfeito", "presente"], "perfeito"),
    "imperfeito": (["tempsImperfeitoPtExercises", "imperfeitoPtExercises"], ["perfeito", "presente"], "imperfeito"),
    "futuro": (["tempsFuturoPtExercises"], ["condicional", "presente"], "futuro"),
    "condicional": (["tempsCondicionalPtExercises", "condicionalPtExercises"], ["futuro", "imperfeito"], "condicional"),
    "conj_presente": (["tempsConjuntivoPresentePtExercises", "conjuntivoPresentePtExercises"], ["presente", "conj_imperfeito"], "conjuntivo présent"),
    "conj_imperfeito": (["tempsConjuntivoImperfeitoPtExercises", "conjuntivoImperfeitoPtExercises"], ["conj_presente", "imperfeito"], "conjuntivo imparfait"),
}
PERSONNES = ["eu", "tu", "ele/ela", "nós", "vós", "eles/elas"]
MAX_PAR_SERIE = 45
# Le mais-que-perfeito composto se repere a son auxiliaire : tinha + participe.
AUX_MQP = ["tinha", "tinhas", "tinha", "tínhamos", "tínheis", "tinham"]
SERIES_MQP = ["tempsMaisQuePerfeitoPtExercises", "maisQuePerfeitoPtExercises"]
MOTS_OUTILS = set("""a o as os um uma de do da em no na que se e é são há foi era ser estar ter ir para por com
não mais muito já ainda""".split())


class Index:
    """forme -> {(infinitif, temps, personne)} pour tous les verbes connus."""
    def __init__(self, infinitifs):
        self.formes = {}
        self.tables = {}
        for inf in infinitifs:
            base = inf.split(" ")[0].replace("-se", "")
            if base in self.tables or not re.match(r"^[a-zà-úç]+(ar|er|ir|or|ôr)$", base):
                continue
            try:
                t = I.conjuguer(base)
            except Exception:
                continue
            self.tables[base] = t
            for temps in list(TEMPS) + ["presente"]:
                for p, f in enumerate(t[temps]):
                    if f and f != "-" and " " not in f:
                        self.formes.setdefault(f, set()).add((base, temps, p))
        # une forme qui est aussi l'infinitif ou le participe d'un verbe n'est pas sure
        for base, t in self.tables.items():
            for f in (base, t["participio"], t["gerundio"]):
                if f in self.formes:
                    self.formes[f].add((base, "autre", -1))

    def analyser(self, mot):
        r = self.formes.get(mot.lower())
        if not r:
            return None
        verbes = {x[0] for x in r}
        temps = {x[1] for x in r}
        if len(verbes) != 1 or len(temps) != 1 or "autre" in temps:
            return None
        base, tps, _ = next(iter(r))
        personnes = sorted({x[2] for x in r})
        return base, tps, personnes


# Devant un nom, jamais devant un verbe conjugue : « no verão », « um monte ».
DETERMINANTS = set("""o a os as um uma uns umas no na nos nas do da dos das ao à aos às pelo pela pelos pelas
num numa dum duma este esta estes estas esse essa esses essas aquele aquela deste desta neste nesta
meu minha teu tua seu sua nosso nossa cada outro outra muito muita pouco pouca""".split())
# Les contractions qui ressemblent a un subjonctif de dar (desse, deste...).
PAS_VERBES = set("""desse dessa desses dessas deste destes nesse nessa naquele naquela leve leves verão monte
montes controle controles via vias cria crias pena penas sede cedo ponte pontes saia saias pare corte cortes
fecho base bases nota notas""".split())


def interdits(jeu):
    """Les mots qui sont aussi des noms, des adjectifs, des adverbes ou des
    mots-outils de nos listes : on ne les prend pas pour des verbes."""
    s = set(PAS_VERBES)
    for t in jeu["themes.json"]["themes"]:
        for m in t["mots"]:
            for x in (m["mot"], m.get("pluriel") or ""):
                s.update(w.lower() for w in re.findall(r"[A-Za-zÀ-úç]+", x))
    for f in ("adjectifs.json", "adverbes.json"):
        for l in jeu.get(f, {}).values():
            for m in l:
                s.update(w.lower() for w in re.findall(r"[A-Za-zÀ-úç]+", m["mot"]))
                for v in (m.get("formes") or {}).values():
                    s.update(w.lower() for w in re.findall(r"[A-Za-zÀ-úç]+", v or ""))
    for l in jeu.get("fonctionnels.json", {}).values():
        for m in l:
            s.update(w.lower() for w in re.findall(r"[A-Za-zÀ-úç]+", m["mot"]))
    return s


def question_mqp(phrase, fr, idx):
    """« tinha feito » -> « ___ (fazer) » ; fausses : perfeito et imperfeito."""
    m = re.search(r"\b(tinha|tinhas|tínhamos|tinham)( (?:me|te|se|nos|lhe|lhes|o|a|os|as))? ([a-zà-úç]+)\b", phrase, re.I)
    if not m:
        return None
    aux, pron, part = m.group(1), m.group(2) or "", m.group(3).lower()
    bases = [b for b, t in idx.tables.items() if t["participio"] == part]
    if len(bases) != 1:
        return None
    base = bases[0]
    t = idx.tables[base]
    p = AUX_MQP.index(aux.lower())
    # « tinha » sert a eu et a ele : ele, sauf si « eu » precede.
    if aux.lower() == "tinha" and not re.search(r"\beu\b", phrase[:m.start()], re.I):
        p = 2
    bonne = "%s%s %s" % (aux, pron, part)
    fausses = [t["perfeito"][p], t["imperfeito"][p]]
    if bonne in fausses or len(set(fausses)) < 2:
        return None
    q = phrase[:m.start()] + "___ (" + base + ")" + phrase[m.end():]
    expl = "Le passé avant le passé : %s + participe (%s)." % (aux.lower(), part)
    return "mais_que_perfeito", (q, bonne, fausses, fr, expl)


def question(phrase, fr, idx, bannis=frozenset()):
    """La premiere forme verbale sans ambiguite de la phrase -> question, ou None."""
    mqp = question_mqp(phrase, fr, idx)
    if mqp:
        return mqp
    mots = list(re.finditer(r"[A-Za-zÀ-úç]+", phrase))
    for i, m in enumerate(mots):
        mot = m.group(0)
        if mot.lower() in MOTS_OUTILS or len(mot) < 3 or mot.lower() in bannis:
            continue
        if i > 0 and mots[i - 1].group(0).lower() in DETERMINANTS:
            continue
        a = idx.analyser(mot)
        if not a:
            continue
        base, tps, personnes = a
        if tps not in TEMPS:
            continue
        personnes = [x for x in personnes if x != 4]  # pas de « vós »
        if not personnes:
            continue
        if tps == "conj_presente" and i == 0:  # un imperatif poli, pas un subjonctif
            continue
        p = personnes[0]
        t = idx.tables[base]
        bonne = t[tps][p]
        fausses = []
        for autre in TEMPS[tps][1]:
            f = t[autre][p]
            if f and f != bonne and f not in fausses and " " not in f:
                fausses.append(f)
        if len(fausses) < 2:
            continue
        if mot[0].isupper():
            bonne, fausses = bonne[0].upper() + bonne[1:], [f[0].upper() + f[1:] for f in fausses]
        q = phrase[:m.start()] + "___ (" + base + ")" + phrase[m.end():]
        qui = " / ".join(PERSONNES[x] for x in personnes)
        expl = "%s, %s : %s." % (TEMPS[tps][2].capitalize(), qui, bonne.lower())
        return tps, (q, bonne, fausses, fr, expl)
    return None


def phrases_du_jeu(jeu, niveaux):
    """(niveau, phrase, traduction) de toutes les cartes A2-C1, dans l'ordre."""
    out = []
    for t in jeu["themes.json"]["themes"]:
        if t.get("niveau") in niveaux:
            out += [(t["niveau"], m["exemple"], m["exemple_fr"]) for m in t["mots"]]
    for f in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        for niv in niveaux:
            out += [(niv, m["exemple"], m["exemple_fr"]) for m in jeu.get(f, {}).get(niv, [])]
    return out


def supplements(jeu, niveaux, deja_vues):
    """{serie: [(q, bonne, fausses, trad, expl)]}, au plus MAX_PAR_SERIE par serie,
    sans reprendre une question deja dans la serie."""
    infs = [m["infinitif"] for niv in ["A1"] + list(niveaux) for m in jeu.get("verbes.json", {}).get(niv, [])]
    idx = Index(infs)
    bannis = interdits(jeu)
    out = {}
    for niv, phrase, fr in phrases_du_jeu(jeu, niveaux):
        if not phrase or not fr or "___" in phrase:
            continue
        r = question(phrase, fr, idx, bannis)
        if not r:
            continue
        tps, q = r
        for serie in (SERIES_MQP if tps == "mais_que_perfeito" else TEMPS[tps][0]):
            l = out.setdefault(serie, [])
            if len(l) < MAX_PAR_SERIE and q[0] not in deja_vues.get(serie, set()) and q[0] not in {x[0] for x in l}:
                l.append(q)
    return out
