# -*- coding: utf-8 -*-
"""Convertit les dictionnaires WikDict (SQLite) en paquets JSON servables.

    python espanol/dicc_construire.py            # les quatre paires
    python espanol/dicc_construire.py es-fr fr-es

DEMENAGE ICI LE 10 OCT. 2026 depuis le depot wortando-espanol (retraite) : les
paquets sont servis depuis espanol/dicc/. Les SQLite restent hors du depot
public (WIKDICT_SOURCE, sinon ../WortandoEspanol/dicc/fuente/). La paire
espagnol-francais est ajoutee le meme jour : un francophone n'avait que
l'espagnol-anglais.

Source : WikDict (Wiktionnaire via DBnary), **CC BY-SA 4.0**, telecharge depuis
https://download.wikdict.com/dictionaries/sqlite/ vers dicc/fuente/.

NE PAS changer de source a la legere. FreeDict publie les memes paires et sort
en premier quand on cherche, mais plusieurs de ses dictionnaires sont sous
AGPLv3 -- une licence ecrite precisement pour atteindre les applications
servies par reseau, soit l'inverse de ce qu'il faut a un produit payant. La
ligne d'attribution affichee sous les resultats est une obligation de la
licence, pas une decoration.

LE DECOUPAGE EST PAR TAILLE, pas par lettre initiale. Couper par prefixe de
deux lettres donnerait des centaines de fichiers pour le meme resultat ; ici il
y en a quelques dizaines, aucun au-dela de 120 Ko. index.json liste le premier
mot normalise de chaque paquet, et le client y cherche par dichotomie.

Avantage propre a l'espagnol : `lexentry` encode la classe ET le genre
(spa/casa__sustantivo_femenino__1), donc chaque nom sort avec son article.
Pour un anglophone c'est exactement ce qui manque -- "house" ne dit pas si on
dit el ou la.
"""
import io, json, os, re, sqlite3, unicodedata

AQUI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dicc")
FUENTE = os.environ.get("WIKDICT_SOURCE") or os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "WortandoEspanol", "dicc", "fuente")
TAM_PAQUETE = 120 * 1024
MAX_TRAD = 8          # au-dela, la fiche devient illisible

CLASES = [("sustantivo", "n"), ("verbo", "v"), ("adjetivo", "adj"),
          ("adverbio", "adv"), ("preposicion", "prep"), ("pronombre", "pron"),
          ("conjuncion", "conj"), ("interjeccion", "interj"),
          ("noun", "n"), ("verb", "v"), ("adjective", "adj"), ("adverb", "adv"),
          ("preposition", "prep"), ("pronoun", "pron"), ("conjunction", "conj"),
          ("interjection", "interj")]


def normalizar(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s)


def leer(par):
    """Reunit tous les sens d'un meme mot en une seule fiche."""
    db = sqlite3.connect(os.path.join(FUENTE, par + ".sqlite3"))
    fichas = {}
    for lexentry, escrito, traducciones, importancia in db.execute(
            "SELECT lexentry, written_rep, trans_list, importance FROM translation"):
        if not escrito or not traducciones:
            continue
        escrito = escrito.strip()
        if not escrito or len(escrito) > 40 or escrito.startswith("-"):
            continue
        f = fichas.setdefault(escrito, {"m": escrito, "t": [], "r": 0.0})
        for t in traducciones.split(" | "):
            t = t.strip()
            if t and t not in f["t"]:
                f["t"].append(t)
        f["r"] = max(f["r"], round(importancia or 0.0, 2))

        marca = (lexentry or "").lower()
        if "p" not in f:
            for largo, corto in CLASES:
                if largo in marca:
                    f["p"] = corto
                    break
        if "g" not in f and "sustantivo" in marca:
            # "masculino_y_femenino" porte les deux : on note el/la.
            m, h = "masculino" in marca, "femenino" in marca
            if m and h:   f["g"] = "el/la"
            elif m:       f["g"] = "el"
            elif h:       f["g"] = "la"
    db.close()
    for f in fichas.values():
        f["t"] = f["t"][:MAX_TRAD]
    return sorted(fichas.values(), key=lambda f: (normalizar(f["m"]), f["m"]))


def escribir(par, fichas):
    destino = os.path.join(AQUI, par)
    if os.path.isdir(destino):
        for v in os.listdir(destino):
            os.remove(os.path.join(destino, v))
    else:
        os.makedirs(destino)

    paquetes, actual, peso = [], [], 0
    for f in fichas:
        linea = json.dumps(f, ensure_ascii=False, separators=(",", ":"))
        if actual and peso + len(linea) > TAM_PAQUETE:
            paquetes.append(actual); actual, peso = [], 0
        actual.append(f); peso += len(linea) + 1
    if actual:
        paquetes.append(actual)

    bordes = []
    for i, p in enumerate(paquetes):
        bordes.append(normalizar(p[0]["m"]))
        io.open(os.path.join(destino, "%03d.json" % i), "w",
                encoding="utf-8", newline="\n").write(
            json.dumps(p, ensure_ascii=False, separators=(",", ":")))
    io.open(os.path.join(destino, "index.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps(bordes, ensure_ascii=False, separators=(",", ":")))

    peso = sum(os.path.getsize(os.path.join(destino, v)) for v in os.listdir(destino))
    mayor = max(os.path.getsize(os.path.join(destino, v)) for v in os.listdir(destino))
    con_genero = sum(1 for f in fichas if "g" in f)
    print("%-7s %6d mots  %3d paquets  %5.1f Mo  plus gros %5.1f Ko  %d avec genre"
          % (par, len(fichas), len(paquetes), peso / 1048576, mayor / 1024, con_genero))


def injertar_genero(fichas_en_es, fichas_es_en):
    """Note l'article de chaque traduction espagnole dans le sens en->es.

    Le genre est une propriete du mot ESPAGNOL : WikDict ne le fournit donc que
    dans la paire es-en. Sans cette greffe, un anglophone qui cherche "house"
    lit "casa" et ne sait toujours pas s'il faut dire el ou la -- soit
    exactement ce dont il a besoin. Ajoute comme liste `tg` alignee sur `t`,
    chaine vide la ou le genre est inconnu.
    """
    genero = {}
    for f in fichas_es_en:
        if "g" in f:
            genero.setdefault(f["m"].lower(), f["g"])
    tocadas = 0
    for f in fichas_en_es:
        arts = [genero.get(t.lower(), "") for t in f["t"]]
        if any(arts):
            f["tg"] = arts
            tocadas += 1
    print("        genre greffe sur %d fiches en-es" % tocadas)
    return fichas_en_es


if __name__ == "__main__":
    import sys
    voulu = set(sys.argv[1:]) or {"es-en", "en-es", "es-fr", "fr-es"}
    # Chaque sens « vers l'espagnol » recoit le genre greffe depuis le sens
    # « depuis l'espagnol » de la meme langue (voir injertar_genero).
    for depuis, vers in (("es-en", "en-es"), ("es-fr", "fr-es")):
        if depuis in voulu or vers in voulu:
            base = leer(depuis)
            if depuis in voulu:
                escribir(depuis, base)
            if vers in voulu:
                escribir(vers, injertar_genero(leer(vers), base))
