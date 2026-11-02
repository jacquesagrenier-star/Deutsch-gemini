# -*- coding: utf-8 -*-
"""Pose l'ESPAGNOL des textes de l'anglais appris HORS corpus (2 nov. 2026).

    python anglais/es/poser_autres.py controle [nom ...]   # lit les lots, n'ecrit rien
    python anglais/es/poser_autres.py pose [nom ...]       # ecrit

Copie de espanol/de/poser_autres.py. Les sources sont dans
anglais/es/sources/<nom>.json (faites par extraire.py), les traductions dans
anglais/es/lots/<nom>.es.json -- pour les noms marques *, tous les
lots/<nom>-*.es.json reunis (un gros fichier se rend en morceaux).

Ou va l'espagnol :
  i18n *         index.html, bloc « es: » de I18N, juste avant sa fermeture (apres de)
  surcharge-en   index.html, bloc « "es" » de I18N_ANGLAIS, juste apres « "fr" »

⚠️ « es » DESIGNE AUSSI L'ESPAGNOL APPRIS (LANGUE_APPRISE === "es", les
tables par langue apprise « es: { A1: [...] } », scene-*.es.js) : on ne cherche
jamais « es: { » dans tout le fichier, seulement dans le dictionnaire vise
(voir anglais/es/AVANCEMENT.md, section 1).

Garde-fous : chaque id de la source a sa traduction (et aucune en trop) ; aucun
texte ne recopie le francais ; les {marques} et les balises HTML sont celles du
francais. Une faute arrete tout, rien n'est ecrit.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.environ.get("ESSAI_RACINE") or os.path.dirname(os.path.dirname(ICI))   # essai sur une copie
LOTS = os.environ.get("ESSAI_LOTS") or os.path.join(ICI, "lots")
INDEX = os.path.join(RACINE, "index.html")
NOMS = ["i18n", "surcharge-en"]
EN_MORCEAUX = {"i18n"}
MARQUE = re.compile(r"\{[a-zA-Z_0-9]+\}")
BALISE = re.compile(r"</?([a-zA-Z]+)[^>]*>")

# Ce qui ne peut etre que du francais oublie : des mots qui n'existent pas en
# espagnol (« le », « les », « sur », « tu », « un » en existent : exclus) et
# les lettres que l'espagnol n'a pas.
MOTS_FRANCAIS = re.compile(r"(?<![\w'’])(des|du|et|est|avec|pour|dans|pas|ton|tes|vous|aux|cette|ces|ici|mais|sont|leur|chaque|plus|tout|toute)(?![\w'’])", re.I)
LETTRES_FRANCAISES = re.compile(r"[çèêëàâîïôûùœÇÈÊÀÂÎÔÛ]")


def lire(chemin):
    return io.open(chemin, encoding="utf-8", newline="").read()


def ecrire(chemin, texte):
    io.open(chemin, "w", encoding="utf-8", newline="").write(texte)


def sources(nom):
    return json.load(io.open(os.path.join(ICI, "sources", nom + ".json"), encoding="utf-8"))


def lots(nom):
    chemins = [os.path.join(LOTS, nom + ".es.json")]
    if nom in EN_MORCEAUX:
        chemins = sorted(glob.glob(os.path.join(LOTS, nom + "-*.es.json"))) + \
            [c for c in chemins if os.path.exists(c)]
    out = {}
    for c in chemins:
        if not os.path.exists(c):
            raise SystemExit("%s : lot absent (%s)" % (nom, c))
        for k, v in json.load(io.open(c, encoding="utf-8")).items():
            if k in out and out[k] != v:
                raise SystemExit("%s : %s traduit deux fois, differemment" % (nom, k))
            out[k] = v
    return out


def balises(t):
    return sorted(m.group(0).split()[0].rstrip(">").lower() for m in BALISE.finditer(t))


def sans_balises(t):
    return re.sub(r"<[^>]+>", " ", t)


def doute_espagnol(es, fr, en):
    """Une raison de croire que le texte n'est pas de l'espagnol, ou None."""
    nu, fr_nu = sans_balises(es), sans_balises(fr)
    # Identique au francais : une faute, sauf si ce « francais » n'est fait que
    # d'exemples anglais (« big · bigger · the biggest »), qui se recopient.
    francais = MOTS_FRANCAIS.search(fr_nu) or LETTRES_FRANCAISES.search(fr_nu) \
        or re.search(r"(?<![\w'’])(le|la|les|un|une|de|en|à|ou|qui|que)(?![\w'’])", fr_nu, re.I)
    if es == fr and len(fr) > 12 and francais and fr != en:
        return "identique au francais"
    # Un mot francais ou une lettre francaise, absents du francais cite ?
    # (un exemple francais recopie tel quel dans le texte source reste permis)
    m = MOTS_FRANCAIS.search(nu)
    if m and not re.search(r"(?<![\w'’])%s(?![\w'’])" % re.escape(m.group(1)), en or "", re.I):
        return "mot francais « %s »" % m.group(1)
    m = LETTRES_FRANCAISES.search(nu)
    if m and m.group(0) not in (en or ""):
        return "lettre francaise « %s »" % m.group(0)
    if en and es == en and len(en) > 20 and en != fr:
        return "identique a l'anglais"
    return None


def verifier_texte(nom, id_, fr, en, es, fautes, avis):
    if not isinstance(es, str) or not es.strip():
        if fr.strip():
            fautes.append("%s %s : vide" % (nom, id_))
        return
    d = doute_espagnol(es, fr, en)
    if d:
        (fautes if d == "identique au francais" else avis).append("%s %s : %s : %s" % (nom, id_, d, es[:70]))
    if sorted(MARQUE.findall(es)) != sorted(MARQUE.findall(fr)):
        fautes.append("%s %s : marques %s au lieu de %s" % (nom, id_, MARQUE.findall(es), MARQUE.findall(fr)))
    if balises(es) != balises(fr) and balises(es) != balises(en):
        avis.append("%s %s : balises %s (fr %s)" % (nom, id_, balises(es), balises(fr)))
    if re.search(r"(?<![\w])vosotr|(?<![\w])os(?![\w])|\b(?:habéis|tenéis|sabéis|podéis|queréis)\b", es):
        avis.append("%s %s : vosotros ? : %s" % (nom, id_, es[:70]))


def controler(nom):
    src, trad = sources(nom), lots(nom)
    fautes, avis = [], []
    ids = [e["id"] for e in src]
    for k in sorted(set(trad) - set(ids)):
        fautes.append("%s : id inconnu %s" % (nom, k))
    for e in src:
        es = trad.get(e["id"])
        if es is None:
            fautes.append("%s : %s non traduit" % (nom, e["id"]))
            continue
        verifier_texte(nom, e["id"], e["fr"], e["en"], es, fautes, avis)
    return src, trad, fautes, avis


# ---------------------------------------------------------------- index.html

def poser_i18n(src, trad, html):
    """Le bloc « es: » de I18N, juste avant sa fermeture (apres de).
    Recherche bornee au dictionnaire I18N : « es: { » existe ailleurs, au
    sens de l'espagnol APPRIS (series, socle des phrases)."""
    deb = html.index("const I18N = {")
    fin = html.index("\n};", deb)
    if re.search(r"\n    es: \{", html[deb:fin]):
        raise SystemExit("i18n : I18N a deja un bloc es")
    avant = html[:fin].rstrip()
    if not avant.endswith(","):
        avant += ","
    lignes = "".join('\n        %s: %s,' % (e["id"], json.dumps(trad[e["id"]], ensure_ascii=False)) for e in src)
    entete = ("\n    // L'ESPAGNOL, langue d'interface de l'ANGLAIS appris seulement (2 nov. 2026,"
              "\n    // anglais/es/AVANCEMENT.md). Pose par anglais/es/poser_autres.py.")
    return avant + entete + "\n    es: {" + lignes.rstrip(",") + "\n    }" + html[fin:]


def relire_i18n(src, trad):
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js"), "es"], capture_output=True, cwd=RACINE)
    if r.returncode:
        raise SystemExit("i18n : node ne relit pas le bloc I18N :\n" + r.stderr.decode("utf-8", "replace")[:800])
    relu = json.loads(r.stdout.decode("utf-8")).get("es", {})
    ecarts = [e["id"] for e in src if relu.get(e["id"]) != trad[e["id"]]]
    if ecarts or len(relu) != len(src):
        raise SystemExit("i18n : %d ecart(s) a la relecture (%s), %d cles relues" % (len(ecarts), ecarts[:5], len(relu)))
    print("  i18n           %d cles, relues par node a l'identique" % len(relu))


def poser_surcharge_en(src, trad, html):
    debut = html.index("const I18N_ANGLAIS = {")
    fin_table = html.index("\n};", debut)
    if re.search(r'\n    "es": \{', html[debut:fin_table]):
        raise SystemExit("surcharge-en : I18N_ANGLAIS a deja un bloc es")
    fr = html.index('\n    "fr": {', debut)
    fin = html.index("\n    }", fr)
    lignes = ['        %s: %s' % (json.dumps(e["id"]), json.dumps(trad[e["id"]], ensure_ascii=False)) for e in src]
    bloc = '\n    },\n    "es": {\n' + ",\n".join(lignes)
    return html[:fin] + bloc + html[fin:]


POSEURS = {"i18n": poser_i18n, "surcharge-en": poser_surcharge_en}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("controle", "pose"):
        raise SystemExit(__doc__)
    mode, veut = sys.argv[1], sys.argv[2:] or NOMS
    resultats, total_fautes = {}, 0
    for nom in veut:
        src, trad, fautes, avis = controler(nom)
        resultats[nom] = (src, trad)
        total_fautes += len(fautes)
        print("%-14s %5d textes, %d faute(s), %d avis" % (nom, len(src), len(fautes), len(avis)))
        for f in fautes[:40]:
            print("  FAUTE", f)
        for a in avis[:40]:
            print("  avis ", a)
    if mode == "controle":
        return
    if total_fautes:
        raise SystemExit("Des fautes : rien n'est ecrit.")
    html = lire(INDEX)
    for nom in veut:
        html = POSEURS[nom](*resultats[nom], html)
    ecrire(INDEX, html)
    if "i18n" in veut:
        relire_i18n(*resultats["i18n"])
    print("Ecrit :", INDEX)


if __name__ == "__main__":
    main()
