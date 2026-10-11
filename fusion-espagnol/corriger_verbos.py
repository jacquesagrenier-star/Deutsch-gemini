# -*- coding: utf-8 -*-
"""Corrige les conjugaisons fausses de verbos.json (trouvees le 10 oct. 2026).

    python fusion-espagnol/corriger_verbos.py

COMMENT ELLES ONT ETE TROUVEES. conjugueur.py (une regle pour les verbes
reguliers) a ete mesure sur les 832 verbes : 558 identiques, 127 differents.
Presque tous les differents sont de vrais irreguliers, justes dans les
donnees. Mais la lecture un par un en a trouve de faux, et une lecture des
verbes hors du champ du conjugueur (-iar, -uar, pronominaux) d'autres :
  - les FAUX COMPOSES : le generateur d'origine prenait tout verbe en
    -estar / -andar pour un compose de estar / andar -> « manduve »,
    « contestuve », « prestuve », « molestuve », « protestuve » ;
  - l'ACCENT ECRIT des -iar / -uar qui le portent (envio -> envío,
    continuo -> continúo) : 17 verbes ;
  - acordarse (me acordo -> me acuerdo), oponer (opono -> opongo),
    cocer (cuezco -> cuezo), bendecir (bendezco -> bendigo) ;
  - trois verbes SANS conjugaison : intercambiar, auxiliar, desafiar.
Le preterit de criar et guiar suit l'orthographe de la RAE de 2010 : crie,
crio ; guie, guio (monosyllabes, sans accent).

Idempotent : relancer reecrit les memes formes.
"""
import io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conjugueur as C  # noqa

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "espanol", "datos", "verbos.json")
CLES = C.CLES
PRON = ["me", "te", "se", "nos", "os", "se"]

ACCENT = ["enviar", "ampliar", "confiar", "desconfiar", "criar", "vaciar", "guiar", "variar",
          "situar", "situarse", "actuar", "evaluar", "graduarse", "interactuar", "devaluar",
          "continuar", "desafiar"]
SANS_ACCENT = ["intercambiar", "auxiliar"]          # -iar reguliers (auxilio, intercambio)
FAUX_COMPOSES = ["mandar", "contestar", "prestar", "molestar", "protestar"]


def regulier_ar(inf):
    """-ar regulier, sans la garde de verbe_sur (les -iar sans accent y entrent)."""
    rad = inf[:-2]
    return {"praesens": dict(zip(CLES, [rad + f for f in C.PRES["ar"]])),
            "preterito": [(C.devant_e(rad) if i == 0 else rad) + f for i, f in enumerate(C.PRET["ar"])],
            "imperfecto": [rad + f for f in C.IMPF["ar"]],
            "subjuntivo": [C.devant_e(rad) + f for f in C.SUBJ["ar"]]}


def accentue(inf):
    """-iar / -uar qui portent l'accent : envío, envías, envía, enviamos, enviáis, envían."""
    pron = inf.endswith("se")
    base = inf[:-2] if pron else inf
    c = regulier_ar(base)
    rad = base[:-2]
    tonique = rad[:-1] + {"i": "í", "u": "ú"}[rad[-1]]
    pres = [tonique + f if i in (0, 1, 2, 5) else rad + f for i, f in enumerate(C.PRES["ar"])]
    subj = [tonique + f if i in (0, 1, 2, 5) else rad + f for i, f in enumerate(C.SUBJ["ar"])]
    c["praesens"] = dict(zip(CLES, pres))
    c["subjuntivo"] = subj
    if base in ("criar", "guiar"):
        c["preterito"][0] = rad + "e"      # crie, guie
        c["preterito"][2] = rad + "o"      # crio, guio
    if pron:
        c = {"praesens": {k: p + " " + v for (k, v), p in zip(c["praesens"].items(), PRON)},
             "preterito": [p + " " + v for p, v in zip(PRON, c["preterito"])],
             "imperfecto": [p + " " + v for p, v in zip(PRON, c["imperfecto"])],
             "subjuntivo": [p + " " + v for p, v in zip(PRON, c["subjuntivo"])]}
    return c


MAIN = {
 "acordarse": {
  "praesens": dict(zip(CLES, ["me acuerdo", "te acuerdas", "se acuerda", "nos acordamos", "os acordáis", "se acuerdan"])),
  "subjuntivo": ["me acuerde", "te acuerdes", "se acuerde", "nos acordemos", "os acordéis", "se acuerden"]},
 "oponer": {
  "praesens": dict(zip(CLES, ["opongo", "opones", "opone", "oponemos", "oponéis", "oponen"])),
  "subjuntivo": ["oponga", "opongas", "oponga", "opongamos", "opongáis", "opongan"]},
 "cocer": {
  "praesens": dict(zip(CLES, ["cuezo", "cueces", "cuece", "cocemos", "cocéis", "cuecen"])),
  "subjuntivo": ["cueza", "cuezas", "cueza", "cozamos", "cozáis", "cuezan"]},
 "bendecir": {
  "praesens": dict(zip(CLES, ["bendigo", "bendices", "bendice", "bendecimos", "bendecís", "bendicen"])),
  "subjuntivo": ["bendiga", "bendigas", "bendiga", "bendigamos", "bendigáis", "bendigan"]},
}

VERIFS = {"enviar": ("envío", "envíe"), "continuar": ("continúo", "continúe"), "situarse": ("me sitúo", "me sitúe"),
          "desafiar": ("desafío", "desafíe"), "auxiliar": ("auxilio", "auxilie"), "mandar": ("mando", "mande")}


def main():
    d = json.load(io.open(CHEMIN, encoding="utf-8"))
    idx = {x["infinitif"]: x for n in d.values() for x in n}
    faits = []
    for inf in ACCENT:
        if inf in idx:
            idx[inf].update(accentue(inf)); faits.append(inf)
    for inf in SANS_ACCENT:
        if inf in idx:
            idx[inf].update(regulier_ar(inf)); faits.append(inf)
    for inf in FAUX_COMPOSES:
        if inf in idx:
            idx[inf]["preterito"] = regulier_ar(inf)["preterito"]; faits.append(inf)
    for inf, champs in MAIN.items():
        if inf in idx:
            idx[inf].update(champs); faits.append(inf)
    for inf, (pres, subj) in VERIFS.items():
        x = idx[inf]
        assert x["praesens"]["ich"] == pres and x["subjuntivo"][0] == subj, (inf, x["praesens"]["ich"], x["subjuntivo"][0])
    assert idx["mandar"]["preterito"][0] == "mandé" and idx["criar"]["preterito"][2] == "crio"
    io.open(CHEMIN, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("%d verbes corriges : %s" % (len(faits), ", ".join(faits)))


if __name__ == "__main__":
    main()
