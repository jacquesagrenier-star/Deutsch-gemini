# -*- coding: utf-8 -*-
"""Les exercices : reponse attendue, distracteurs, explication, traductions.

    python retours/qualite-es-de/exercices.py [sortie.json]

  hors_options     la reponse n'est pas parmi les options
  hors_answers     « correct » n'est pas dans « answers »
  options_double   deux options identiques
  options_langue   optionsXx n'a pas la longueur de options, ou la bonne
                   reponse traduite n'est pas au meme rang (decalage)
  sans_trou        question sans « ___ » alors que l'exercice est a trou
  explication      l'explication cite une autre option et jamais la bonne
  morceaux         les morceaux a ordonner ne redonnent pas la bonne phrase
  forme_es         espagnol : la reponse n'est pas la forme du tableau de
                   conjugaison pour le verbe et la personne de l'indice
"""
import collections
import json
import re
import sys

from commun import charger, norm, SUFFIXE

CH = {"fr": "", "en": "En", "tr": "Tr", "uk": "Uk", "fa": "Fa", "pt": "Pt", "ar": "Ar",
      "pl": "Pl", "ru": "Ru", "de": "De"}
LANG = {"de": ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"], "es": ["en", "pt", "ar", "de"]}


def mots_de(s):
    return sorted(re.findall(r"\w+", s.lower()))


def main():
    S = []

    def sig(app, jeu, i, code, **kw):
        kw.update({"app": app, "ou": "%s[%d]" % (jeu, i), "code": code})
        S.append(kw)

    # tableaux espagnols, pour juger les formes attendues
    VE = charger("espanol/datos/verbos.json")
    TAB = {}
    for niv, lst in VE.items():
        for v in lst:
            TAB.setdefault(v["mot"], v)
            TAB.setdefault(v["infinitif"], v)
    PERS = {"yo": 0, "tú": 1, "él": 2, "ella": 2, "usted": 2, "él, ella": 2, "nosotros": 3,
            "nosotras": 3, "vosotros": 4, "ellos": 5, "ellas": 5, "ustedes": 5}

    for app, fich in (("de", "exercices.json"), ("es", "espanol/datos/ejercicios.json")):
        jeux = charger(fich)["jeux"]
        total = 0
        for jeu, lst in jeux.items():
            for i, e in enumerate(lst):
                total += 1
                opts = e.get("options")
                cor = e.get("correct")
                ans = e.get("answers") or []
                if isinstance(opts, list) and cor is not None:
                    if cor not in opts:
                        sig(app, jeu, i, "hors_options", correct=cor, options=opts)
                    if len(set(opts)) != len(opts):
                        sig(app, jeu, i, "options_double", options=opts)
                    for l in LANG[app]:
                        ol = e.get("options" + CH[l])
                        cl = e.get("correct" + CH[l])
                        if ol is None:
                            continue
                        if not isinstance(ol, list) or len(ol) != len(opts):
                            sig(app, jeu, i, "options_langue", langue=l, options=opts, traduites=ol)
                            continue
                        if cl is not None and cor in opts and cl in ol and \
                                ol.index(cl) != opts.index(cor):
                            sig(app, jeu, i, "options_langue", langue=l, options=opts, traduites=ol,
                                correct=cor, correct_l=cl)
                        if cl is not None and cl not in ol:
                            sig(app, jeu, i, "hors_options", langue=l, correct=cl, options=ol)
                if cor and ans and isinstance(ans, list) and cor not in ans and not e.get("chunks"):
                    sig(app, jeu, i, "hors_answers", correct=cor, answers=ans)
                q = e.get("question", "")
                if (e.get("hint") is not None or isinstance(opts, list)) and ans and not e.get("chunks") \
                        and "___" not in q and "…" not in q and "_" not in q and len(cor or "") < 25:
                    sig(app, jeu, i, "sans_trou", question=q, correct=cor)
                # l'explication cite une autre option et pas la bonne
                ex = e.get("explanation", "")
                if isinstance(opts, list) and cor and ex and len(opts) > 1:
                    def cite(o):
                        return re.search(r"(?<!\w)" + re.escape(o.lower()) + r"(?!\w)", ex.lower())
                    autres = [o for o in opts if o != cor and len(o) > 2 and cite(o) and
                              o.lower() not in cor.lower()]
                    if autres and not cite(cor) and len(cor) > 1:
                        sig(app, jeu, i, "explication", correct=cor, cite=autres, explication=ex,
                            question=q)
                # morceaux a ordonner
                ch = e.get("chunks")
                if isinstance(ch, list) and cor and isinstance(cor, str):
                    morceaux = " ".join(c if isinstance(c, str) else str(c) for c in ch)
                    if mots_de(morceaux) != mots_de(cor) and not any(
                            mots_de(morceaux) == mots_de(a) for a in ans if isinstance(a, str)):
                        sig(app, jeu, i, "morceaux", chunks=ch, correct=cor, answers=ans)
                # espagnol : la forme de l'indice
                if app == "es":
                    h = e.get("hint", "")
                    m = re.match(r"^\((\w+)\s*—\s*([^)]+)\)$", h.strip())
                    if m and m.group(1) in TAB and cor:
                        v = TAB[m.group(1)]
                        formes = set()
                        for k in ("praesens", "preterito", "imperfecto", "subjuntivo", "perfecto",
                                  "futuro", "condicional"):
                            t = v.get(k)
                            if isinstance(t, dict):
                                formes |= set(t.values())
                            elif t:
                                formes |= set(t)
                        formes |= set((v.get("imperativo") or {}).values())
                        # derives : subjonctif imparfait (du preterit 3e pl), participe et temps composes
                        pret = v.get("preterito") or []
                        if len(pret) == 6 and pret[5].endswith("ron"):
                            r = re.sub(r"^(se) ", "", pret[5])[:-3]
                            acc = r[:-1] + {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"}.get(r[-1:], r[-1:])
                            for f in ("ra", "ras", "ra", "rais", "ran", "se", "ses", "seis", "sen"):
                                formes.add(r + f)
                            formes.add(acc + "ramos")
                            formes.add(acc + "semos")
                        perf = v.get("perfecto") or []
                        if perf:
                            p = perf[0].split()[-1]
                            parts = {p, p[:-1] + "a", p + "s", p[:-1] + "as"}
                            formes |= parts
                            HAB = ["he", "has", "ha", "hemos", "habéis", "han", "había", "habías",
                                   "habíamos", "habíais", "habían", "habré", "habrás", "habrá",
                                   "habremos", "habréis", "habrán", "habría", "habrías",
                                   "habríamos", "habríais", "habrían", "haya", "hayas", "hayamos",
                                   "hayáis", "hayan", "hubiera", "hubieras", "hubiéramos",
                                   "hubierais", "hubieran", "hube", "hubiese"]
                            formes |= {h + " " + p for h in HAB}
                        formes = {re.sub(r"^(me|te|se|nos|os) ", "", f) for f in formes}
                        bonnes = [a for a in ([cor] + ans) if a in formes or
                                  re.sub(r"^(me|te|se|nos|os) ", "", a) in formes]
                        if not bonnes and len(cor.split()) <= 3:
                            sig(app, jeu, i, "forme_es", verbe=m.group(1), personne=m.group(2),
                                correct=cor, question=q, topic=e.get("topic"))
        print(app, fich, "exercices :", total)
    c = collections.Counter((s["app"], s["code"]) for s in S)
    for k, v in sorted(c.items()):
        print("  %-3s %-16s %5d" % (k[0], k[1], v))
    if len(sys.argv) > 1:
        json.dump(S, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
