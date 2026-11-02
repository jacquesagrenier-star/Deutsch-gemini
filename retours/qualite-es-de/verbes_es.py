# -*- coding: utf-8 -*-
"""Espagnol : les tableaux de conjugaison se recoupent-ils entre eux ?

Aucune liste de verbes irreguliers n'est supposee juste : on confronte les
temps les uns aux autres, la ou la grammaire impose une relation.

  perfecto     = he/has/ha/hemos/habeis/han + UN SEUL participe
  condicional  = radical du futur + ia, ias, ia, iamos, iais, ian
  futuro       = un radical + e, as, a, emos, eis, an (le meme pour les six)
  imperfecto   = regulier sauf ser, ir, ver
  subjuntivo   = radical du « yo » du present (+ e / a), sauf les six connus
  imperativo   usted = subjonctif 3e sg ; ustedes = subjonctif 3e pl ;
               vosotros = infinitif sans r + d ; tu = present 3e sg sauf huit
  preterito    3e pl en -ron
  regulier     un verbe en -ar/-er/-ir sans changement de radical : chaque
               forme du present et du preterit doit etre la forme reguliere

    python retours/qualite-es-de/verbes_es.py [sortie.json]
"""
import json
import re
import sys
import unicodedata

from commun import charger

HABER = ["he", "has", "ha", "hemos", "habéis", "han"]
SUBJ_IRR = {"ser", "ir", "saber", "haber", "estar", "dar"}
IMPF_IRR = {"ser", "ir", "ver"}
TU_IRR = {"decir": "di", "hacer": "haz", "ir": "ve", "poner": "pon", "salir": "sal",
          "ser": "sé", "tener": "ten", "venir": "ven"}


def sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def nu(f):
    """La forme sans pronom reflechi."""
    f = f.strip()
    return re.sub(r"^(me|te|se|nos|os) ", "", f)


def base(inf):
    inf = inf.split()[0]
    return inf[:-2] if inf.endswith("se") else inf


def main():
    VE = charger("espanol/datos/verbos.json")
    out = []

    def sig(ou, v, code, detail):
        out.append({"ou": ou, "mot": v["mot"], "code": code, "detail": detail})

    n = 0
    for niv, lst in VE.items():
        for i, v in enumerate(lst):
            n += 1
            ou = "verbos.%s[%d]" % (niv, i)
            inf = base(v["infinitif"])
            if " " in v["mot"].strip() and not v["mot"].endswith("se"):
                continue    # locution (deber dinero) : le tableau porte le complement
            pres = [nu(x) for x in (v.get("praesens") or {}).values()]
            pret = [nu(x) for x in (v.get("preterito") or [])]
            impf = [nu(x) for x in (v.get("imperfecto") or [])]
            subj = [nu(x) for x in (v.get("subjuntivo") or [])]
            perf = [nu(x) for x in (v.get("perfecto") or [])]
            fut = [nu(x) for x in (v.get("futuro") or [])]
            cond = [nu(x) for x in (v.get("condicional") or [])]
            imp = v.get("imperativo") or {}
            for nom, tab in (("praesens", pres), ("preterito", pret), ("imperfecto", impf),
                             ("subjuntivo", subj), ("perfecto", perf), ("futuro", fut),
                             ("condicional", cond)):
                if len(tab) != 6 or any(not x for x in tab):
                    sig(ou, v, "incomplet", nom)
            if len(perf) == 6:
                aux = [p.split()[0] for p in perf]
                parts = {p.split()[-1] for p in perf}
                if aux != HABER:
                    sig(ou, v, "perfecto_aux", perf)
                if len(parts) != 1:
                    sig(ou, v, "perfecto_participe", perf)
                part = perf[0].split()[-1]
                if not re.search(r"(ado|ido|ído|to|cho|so)$", part):
                    sig(ou, v, "participe_forme", part)
            if len(fut) == 6:
                fins = ["é", "ás", "á", "emos", "éis", "án"]
                rad = {f[:-len(e)] for f, e in zip(fut, fins) if f.endswith(e)}
                if len(rad) != 1 or not all(f.endswith(e) for f, e in zip(fut, fins)):
                    sig(ou, v, "futuro", fut)
                elif len(cond) == 6:
                    r = rad.pop()
                    att = [r + e for e in ["ía", "ías", "ía", "íamos", "íais", "ían"]]
                    if cond != att:
                        sig(ou, v, "condicional", {"a": cond, "attendu": att})
            if inf not in IMPF_IRR and len(impf) == 6:
                r = inf[:-2]
                if inf.endswith("ar"):
                    att = [r + e for e in ["aba", "abas", "aba", "ábamos", "abais", "aban"]]
                else:
                    att = [r + e for e in ["ía", "ías", "ía", "íamos", "íais", "ían"]]
                if impf != att:
                    sig(ou, v, "imperfecto", {"a": impf, "attendu": att})
            if len(subj) == 6 and inf not in SUBJ_IRR and pres and pres[0].endswith("o"):
                r = pres[0][:-1]
                voy = "e" if inf.endswith("ar") else "a"
                # changements orthographiques c->qu, g->gu, z->c, gu->gü
                if voy == "e":
                    r = re.sub(r"c$", "qu", r)
                    r = re.sub(r"gu$", "gü", r) if r.endswith("gu") else re.sub(r"g$", "gu", r)
                    r = re.sub(r"z$", "c", r)
                if sans_accent(subj[0]) != sans_accent(r + voy):
                    sig(ou, v, "subjuntivo_yo", {"presente_yo": pres[0], "subj": subj[0], "attendu": r + voy})
                if subj[0] != subj[2]:
                    sig(ou, v, "subjuntivo_1_3", subj)
            if imp and len(subj) == 6:
                enc = lambda f: sans_accent(re.sub(r"(se|nse|me|te|nos|os)$", "", f)) if v["infinitif"].endswith("se") else sans_accent(f)
                if imp.get("usted") and enc(imp["usted"]) != sans_accent(subj[2]) and enc(imp["usted"]) + "n" != sans_accent(subj[2]):
                    sig(ou, v, "imperativo_usted", {"usted": imp["usted"], "subj3": subj[2]})
                if imp.get("ustedes") and enc(imp["ustedes"]) not in (sans_accent(subj[5]), sans_accent(subj[5])[:-1]):
                    sig(ou, v, "imperativo_ustedes", {"ustedes": imp["ustedes"], "subj6": subj[5]})
                vos = imp.get("vosotros")
                if vos and not v["infinitif"].endswith("se") and inf != "ir" and sans_accent(vos) != sans_accent(inf[:-1] + "d"):
                    sig(ou, v, "imperativo_vosotros", {"vosotros": vos, "attendu": inf[:-1] + "d"})
                tu = imp.get("tu")
                if tu and not v["infinitif"].endswith("se"):
                    irr = [k for k in TU_IRR if inf == k or (len(k) > 3 and k not in ("ser",) and inf.endswith(k))]
                    att = (inf[:-len(irr[0])] + TU_IRR[irr[0]]) if irr else pres[2]
                    if sans_accent(tu) != sans_accent(att):
                        sig(ou, v, "imperativo_tu", {"tu": tu, "attendu": att})
            if len(pret) == 6 and not pret[5].endswith("ron"):
                sig(ou, v, "preterito_3pl", pret)
            # nosotros du present = infinitif - r + mos (toujours, sauf ser/ir/haber)
            if len(pres) == 6 and inf not in ("ser", "ir", "haber"):
                att = inf[:-1] + "mos"
                if sans_accent(pres[3]) != sans_accent(att) and not inf.endswith("ír"):
                    sig(ou, v, "presente_nosotros", {"a": pres[3], "attendu": att})
                attv = inf[:-2] + {"ar": "áis", "er": "éis", "ir": "ís", "ír": "ís"}.get(inf[-2:], "")
                if sans_accent(pres[4]) != sans_accent(attv) and inf not in ("ser", "ir", "dar", "ver", "haber"):
                    sig(ou, v, "presente_vosotros", {"a": pres[4], "attendu": attv})
    print("verbes :", n, "signalements :", len(out))
    for o in out:
        print(o["code"], o["ou"], o["mot"], "|", json.dumps(o["detail"], ensure_ascii=False)[:150])
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
