# -*- coding: utf-8 -*-
"""Les mots : genre, pluriel, phrase d'exemple, coherence d'un fichier a l'autre.

    python retours/qualite-es-de/mots.py [sortie.json]

Allemand (themes.json et les listes de mots) et espagnol (espanol/datos/) :
  incoherent      le meme mot (meme sens francais) a deux genres, deux pluriels
                  ou deux traductions dans une langue, selon le theme
  exemple_sans    la phrase d'exemple ne contient pas le mot enseigne
  article_fr      « le » / « la » devant une voyelle, ou article contredit ailleurs
  de_genre        espagnol : l'article de traduction_de contredit le corpus allemand
  es_genre        espagnol : el/la contredit WikDict (sens recoupe)
  es_pluriel      espagnol : le pluriel n'est pas celui de la regle, ni de WikDict
"""
import collections
import io
import json
import os
import re
import sys

from commun import RACINE, charger, norm

sortie = sys.argv[1] if len(sys.argv) > 1 else None
S = []


def sig(code, **kw):
    kw["code"] = code
    S.append(kw)


# ------------------------------------------------------------------ allemand
TH = charger("themes.json")["themes"]
LDE = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]


def trad(m, l):
    return m.get("traduction" if l == "fr" else "traduction_" + l)


par_mot = collections.defaultdict(list)
for t in TH:
    for i, m in enumerate(t["mots"]):
        par_mot[m["mot"]].append((t["id"], i, m))

for mot, occ in par_mot.items():
    if len(occ) < 2:
        continue
    # meme sens = meme traduction francaise ; sinon homographe (Bank, See...)
    sens = collections.defaultdict(list)
    for o in occ:
        sens[norm(o[2]["traduction"])].append(o)
    for fr, oo in sens.items():
        if len(oo) < 2:
            continue
        for champ in ["genre", "pluriel"] + ["traduction_" + l for l in LDE[1:]]:
            vals = {o[2].get(champ) for o in oo}
            if len(vals) > 1:
                sig("incoherent", app="de", mot=mot, champ=champ, fr=oo[0][2]["traduction"],
                    valeurs={"%s[%d]" % (o[0], o[1]): o[2].get(champ) for o in oo})
    gen = {o[2]["genre"] for o in occ}
    if len(sens) > 1 and len(gen) > 1:
        sig("homographe_genre", app="de", mot=mot,
            valeurs={"%s[%d]" % (o[0], o[1]): (o[2]["genre"], o[2]["traduction"]) for o in occ})


def contient_de(phrase, formes):
    p = phrase.lower()
    for f in formes:
        f = f.lower().strip()
        if not f:
            continue
        racine = f[:max(4, len(f) - 2)] if len(f) > 5 else f
        if racine in p:
            return True
    return False


VOYELLE = re.compile(r"^[aeiouyàâäéèêëîïôöûüœæh]", re.I)
H_ASPIRE = ("hach", "haie", "hall", "hamac", "hamster", "hanche", "handic", "hangar",
            "harc", "hareng", "haric", "harpe", "hasard", "hauss", "haut", "hér",
            "hibou", "hiér", "hock", "homard", "honte", "hors", "hublot", "huit",
            "hutte", "hêtre", "hache", "haine", "halte", "hamburger", "hand",
            "haché", "hurl", "huée", "hold", "hippie", "hip-hop", "hit", "hockey",
            "houx", "housse", "hotte", "hublot", "hall")

art_fr = collections.defaultdict(set)
for t in TH:
    for i, m in enumerate(t["mots"]):
        ou = "%s[%d]" % (t["id"], i)
        if m["genre"] in ("der", "die", "das") and m["mot"][:1].islower():
            sig("minuscule", app="de", ou=ou, mot=m["mot"])
        formes = [m["mot"], m.get("pluriel", "")]
        if not contient_de(m["exemple"], formes):
            sig("exemple_sans", app="de", ou=ou, mot=m["mot"], exemple=m["exemple"],
                fr=m["traduction"])
        a = m.get("article_fr")
        tr = m["traduction"]
        if a in ("le ", "la ") and VOYELLE.match(tr) and not tr.lower().startswith(H_ASPIRE):
            sig("article_fr", app="de", ou=ou, mot=m["mot"], article=a, fr=tr)
        if a in ("l'",) and not VOYELLE.match(tr):
            sig("article_fr", app="de", ou=ou, mot=m["mot"], article=a, fr=tr)
        if a:
            art_fr[norm(tr)].add(a.strip())
for tr, arts in art_fr.items():
    if len(arts & {"le", "la"}) > 1:
        sig("article_fr_double", app="de", fr=tr, articles=sorted(arts))

# verbes, adjectifs, adverbes, expressions, mots-outils : l'exemple contient-il le mot ?
VB = charger("verbe.json")
for niv, lst in VB.items():
    for i, v in enumerate(lst):
        formes = [v["infinitif"]] + list(v.get("praesens", {}).values())
        inf = v["infinitif"]
        base = inf[:-2] if inf.endswith("en") else inf[:-1]
        # verbes separables : la particule part a la fin
        formes.append(base.split("|")[-1])
        for champ in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
            ph = v.get(champ, "")
            radical = re.sub(r"^(sich |ab|an|auf|aus|bei|ein|mit|nach|vor|weg|zu|zurück|fest|los|her|hin|um|durch|über|unter|wieder)", "", inf.replace("sich ", ""))
            r = radical[:3].lower()
            if ph and not contient_de(ph, formes) and r not in ph.lower():
                sig("exemple_sans", app="de", ou="verbe.%s[%d].%s" % (niv, i, champ),
                    mot=inf, exemple=ph, fr=v.get(champ + "_fr"))

for fich in ("adjectif.json", "adverbe.json", "redewendung.json"):
    d = charger(fich)
    for niv, lst in d.items():
        for i, a in enumerate(lst):
            mot = a["mot"]
            mm = [w for w in re.findall(r"\w+", mot) if len(w) > 2 and w.lower() not in
                  ("etwas", "jemand", "jemandem", "jemanden", "sich", "einen", "eine", "den", "dem", "der", "die", "das")]
            if not mm:
                continue
            p = a["exemple"].lower()
            # une expression : au moins la moitie de ses mots porteurs
            ok = sum(w.lower()[:max(3, len(w) - 2)] in p for w in mm)
            if ok < max(1, len(mm) // 2):
                sig("exemple_sans", app="de", ou="%s.%s[%d]" % (fich, niv, i), mot=mot,
                    exemple=a["exemple"], fr=a.get("traduction"))

# ------------------------------------------------------------------ espagnol
TE = charger("espanol/datos/temas.json")["themes"]


def dicc(paire):
    d = os.path.join(RACINE, "espanol", "dicc", paire)
    out = collections.defaultdict(list)
    for n in sorted(os.listdir(d)):
        if n == "index.json" or not n.endswith(".json"):
            continue
        for e in json.load(io.open(os.path.join(d, n), encoding="utf-8")):
            if e.get("p") == "n":
                out[e["m"]].append(e)
    return out


ESFR = dicc("es-fr")

# genres du corpus allemand, pour juger traduction_de
GENRE_DE = collections.defaultdict(set)
for t in TH:
    for m in t["mots"]:
        for g in m["genre"].replace(" (Pl.)", "").split("/"):
            GENRE_DE[m["mot"]].add(g)


def pluriel_regle(s):
    """Pluriel espagnol attendu par la regle ; None quand la regle ne tranche pas."""
    if " " in s:
        return None
    n = norm(s)
    if s[-1] in "aeiouáéó":
        return s + "s"
    if s[-1] in "íú":
        return None                       # esquí -> esquís / esquíes
    if s.endswith("z"):
        return s[:-1] + "ces"
    if s.endswith(("s", "x")) and not re.search(r"[áéíóú]", s[-3:]) and \
            len(re.findall(r"[aeiouáéíóú]+", s)) > 1:
        return s                          # el lunes -> los lunes, la crisis
    accents = str.maketrans("áéíóú", "aeiou")
    # -ón, -és, -án : l'accent tombe au pluriel
    m = re.search(r"([áéíóú])([nsl])$", s)
    if m:
        return s[:-2] + m.group(1).translate(accents) + m.group(2) + "es"
    # -en paroxyton : l'accent apparait (examen -> examenes avec accent)
    return s + "es" if not s.endswith(("en", "n")) or re.search(r"[áéíóú]", s) else None


ACCENTUER = {"examen": "exámenes", "joven": "jóvenes", "origen": "orígenes",
             "imagen": "imágenes", "volumen": "volúmenes", "crimen": "crímenes",
             "resumen": "resúmenes", "orden": "órdenes", "margen": "márgenes",
             "virgen": "vírgenes", "certamen": "certámenes", "dictamen": "dictámenes",
             "germen": "gérmenes", "polen": "pólenes", "abdomen": "abdómenes",
             "carácter": "caracteres", "régimen": "regímenes", "espécimen": "especímenes"}

par_es = collections.defaultdict(list)
for t in TE:
    for i, m in enumerate(t["mots"]):
        ou = "%s[%d]" % (t["id"], i)
        par_es[m["mot"]].append((ou, m))
        mot, g, pl = m["mot"], m.get("genre", ""), m.get("pluriel")
        # l'exemple contient-il le mot ?
        formes = [mot] + ([pl] if pl else [])
        if not any(norm(f.split()[0] if " " in f and len(f.split()[0]) > 3 else f)[:max(3, len(f) - 2)]
                   in norm(m["exemple"]) for f in formes if f):
            sig("exemple_sans", app="es", ou=ou, mot=mot, exemple=m["exemple"], fr=m["traduction"])
        if g not in ("el", "la"):
            continue
        # pluriel
        if pl:
            att = ACCENTUER.get(mot) or pluriel_regle(mot)
            if att and norm(att) == norm(pl) and att != pl:
                sig("es_pluriel_accent", app="es", ou=ou, mot=mot, pluriel=pl, attendu=att)
            elif att and att != pl:
                sig("es_pluriel", app="es", ou=ou, mot=mot, pluriel=pl, attendu=att)
        # genre contre WikDict, sens recoupe par la traduction francaise
        fr = norm(re.sub(r"^(le |la |les |l'|un |une )", "", m["traduction"]))
        frs = {norm(x) for x in re.split(r"[,;/()]", fr) if x.strip()}
        ent = [e for e in ESFR.get(mot, []) if e.get("g") in ("el", "la")]
        if ent:
            ok = [e for e in ent if {norm(re.sub(r"^(le |la |les |l')", "", x)) for x in e["t"]} & frs]
            genres = {e["g"] for e in (ok or ent)}
            if g not in genres and ok:
                sig("es_genre", app="es", ou=ou, mot=mot, genre=g, wikdict=sorted(genres),
                    fr=m["traduction"])
        # l'article allemand de traduction_de
        tde = m.get("traduction_de", "")
        mm = re.match(r"^(der|die|das) (\S+)$", tde.strip())
        if mm and mm.group(2) in GENRE_DE:
            art, nom = mm.groups()
            if art not in GENRE_DE[nom] and not (art == "die" and m.get("pluriel") is None):
                sig("de_genre", app="es", ou=ou, mot=mot, traduction_de=tde,
                    corpus=sorted(GENRE_DE[nom]))
        # l'article francais : « la maison » pour « el » est permis (genres differents),
        # mais pas « le » devant une voyelle.
        tfr = m["traduction"]
        if re.match(r"^(le|la) [aeiouyàâéèêîôûœ]", tfr, re.I) and not \
                re.sub(r"^(le|la) ", "", tfr).lower().startswith(H_ASPIRE):
            sig("article_fr", app="es", ou=ou, mot=mot, fr=tfr)

for mot, occ in par_es.items():
    if len(occ) < 2:
        continue
    sens = collections.defaultdict(list)
    for o in occ:
        sens[norm(o[1]["traduction"])].append(o)
    for fr, oo in sens.items():
        if len(oo) < 2:
            continue
        for champ in ("genre", "pluriel", "traduction_en", "traduction_pt", "traduction_ar", "traduction_de"):
            vals = {o[1].get(champ) for o in oo}
            if len(vals) > 1:
                sig("incoherent", app="es", mot=mot, champ=champ, fr=oo[0][1]["traduction"],
                    valeurs={o[0]: o[1].get(champ) for o in oo})

# verbes espagnols : l'exemple de chaque temps contient-il une forme du verbe ?
VE = charger("espanol/datos/verbos.json")
TEMPS = {"exemple": "praesens", "exemple_preterito": "preterito", "exemple_imperfecto": "imperfecto",
         "exemple_perfecto": "perfecto", "exemple_futuro": "futuro",
         "exemple_condicional": "condicional", "exemple_subjuntivo": "subjuntivo"}
for niv, lst in VE.items():
    for i, v in enumerate(lst):
        for champ, temps in TEMPS.items():
            ph = v.get(champ)
            if not ph:
                continue
            tab = v.get(temps)
            formes = list(tab.values()) if isinstance(tab, dict) else list(tab or [])
            p = " " + norm(re.sub(r"[¿¡.,;:!?«»\"]", " ", ph)) + " "
            # pronoms colles (levantarse -> me levanto) et formes composees
            trouve = any((" " + norm(f.split()[-1]) + " ") in p or
                         (" " + norm(f.split()[-1])) in p for f in formes if f)
            if not trouve:
                sig("temps_sans", app="es", ou="verbos.%s[%d].%s" % (niv, i, champ), mot=v["mot"],
                    temps=temps, exemple=ph, fr=v.get(champ + "_fr"))

for fich in ("adjetivos.json", "adverbios.json", "expresiones.json", "funcionales.json"):
    d = charger("espanol/datos/" + fich)
    for niv, lst in d.items():
        for i, a in enumerate(lst):
            mot = a["mot"]
            formes = [mot] + ([a["feminin"]] if a.get("feminin") else [])
            mm = [w for f in formes for w in re.findall(r"\w+", f) if len(w) > 2]
            if not mm:
                continue
            p = norm(a["exemple"])
            if not any(norm(w)[:max(3, len(w) - 2)] in p for w in mm):
                sig("exemple_sans", app="es", ou="%s.%s[%d]" % (fich, niv, i), mot=mot,
                    exemple=a["exemple"], fr=a.get("traduction"))

c = collections.Counter((s["app"], s["code"]) for s in S)
for k, v in sorted(c.items()):
    print("  %-3s %-20s %5d" % (k[0], k[1], v))
if sortie:
    json.dump(S, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
