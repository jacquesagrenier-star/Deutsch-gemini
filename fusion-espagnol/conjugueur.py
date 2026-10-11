# -*- coding: utf-8 -*-
"""Conjugaison des verbes REGULIERS de l'espagnol (present, preterit,
imparfait, subjonctif present), avec les changements d'orthographe.

    python fusion-espagnol/conjugueur.py      # se mesure sur les 832 verbes de verbos.json

Sert a ajouter des verbes au corpus sans recopier leurs tableaux a la main.
Il ne connait PAS les verbes a diphtongue (pensar, poder), ni les
irreguliers (tener, ir), ni -uir, -iar / -uar accentues (envio, actuo), ni
les pronominaux : verbe_sur() refuse ceux-la. Pour ceux qu'il accepte, sa
regle a ete mesuree sur tout le corpus existant (main) : un verbe regulier
du corpus doit sortir identique, ou la regle est fausse.
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLES = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]
VOYELLES = "aeiouáéíóú"

PRES = {"ar": ["o", "as", "a", "amos", "áis", "an"], "er": ["o", "es", "e", "emos", "éis", "en"],
        "ir": ["o", "es", "e", "imos", "ís", "en"]}
PRET = {"ar": ["é", "aste", "ó", "amos", "asteis", "aron"], "er": ["í", "iste", "ió", "imos", "isteis", "ieron"],
        "ir": ["í", "iste", "ió", "imos", "isteis", "ieron"]}
IMPF = {"ar": ["aba", "abas", "aba", "ábamos", "abais", "aban"], "er": ["ía", "ías", "ía", "íamos", "íais", "ían"],
        "ir": ["ía", "ías", "ía", "íamos", "íais", "ían"]}
SUBJ = {"ar": ["e", "es", "e", "emos", "éis", "en"], "er": ["a", "as", "a", "amos", "áis", "an"],
        "ir": ["a", "as", "a", "amos", "áis", "an"]}


def devant_e(radical):
    """Le radical avant une terminaison en e (caqu, gagu, zac, guagü)."""
    if radical.endswith("c"):
        return radical[:-1] + "qu"
    if radical.endswith("gu"):
        return radical[:-2] + "gü"
    if radical.endswith("g"):
        return radical[:-1] + "gu"
    if radical.endswith("z"):
        return radical[:-1] + "c"
    return radical


def devant_a_o(radical, groupe, inf):
    """Le radical avant a / o pour -er / -ir (conocer -> conozco, coger -> cojo)."""
    if radical.endswith("c") and len(radical) > 1 and radical[-2] in VOYELLES and inf.endswith(("cer", "cir")):
        return radical[:-1] + "zc"
    if radical.endswith("g") and inf.endswith(("ger", "gir")):
        return radical[:-1] + "j"
    if radical.endswith("gu") and inf.endswith("guir"):
        return radical[:-2] + "g"
    return radical


def verbe_sur(inf):
    """Les cas que ce conjugueur sait traiter. Le reste : a la main."""
    if inf.endswith("se") or inf[-2:] not in ("ar", "er", "ir"):
        return False
    if inf.endswith(("uir", "eer", "aer", "oer", "iar", "uar")):
        return False
    return True


def conjuguer(inf):
    groupe, radical = inf[-2:], inf[:-2]
    if groupe == "ar":
        pres = [radical + f for f in PRES["ar"]]
        pret = [(devant_e(radical) if i == 0 else radical) + f for i, f in enumerate(PRET["ar"])]
        subj = [devant_e(radical) + f for f in SUBJ["ar"]]
    else:
        ao = devant_a_o(radical, groupe, inf)
        pres = [(ao if i == 0 else radical) + f for i, f in enumerate(PRES[groupe])]
        pret = [radical + f for f in PRET[groupe]]
        subj = [ao + f for f in SUBJ[groupe]]
    impf = [radical + f for f in IMPF[groupe]]
    return {"praesens": dict(zip(CLES, pres)), "preterito": pret, "imperfecto": impf, "subjuntivo": subj}


def mesurer():
    v = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "verbos.json"), encoding="utf-8"))
    tout = [x for n in v.values() for x in n]
    pris = [x for x in tout if verbe_sur(x["infinitif"])]
    justes, faux = 0, []
    for x in pris:
        c = conjuguer(x["infinitif"])
        if all(c[k] == x[k] for k in c):
            justes += 1
        else:
            faux.append(x["infinitif"])
    return len(tout), len(pris), justes, faux


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    n, pris, justes, faux = mesurer()
    print("%d verbes, %d dans le champ du conjugueur, %d identiques, %d differents" % (n, pris, justes, len(faux)))
    print("differents (irreguliers, diphtongues -- attendus) :", ", ".join(faux))
