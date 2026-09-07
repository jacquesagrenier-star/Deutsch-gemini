# -*- coding: utf-8 -*-
"""Contraste les cles d'interface d'une langue par TRADUCTION INVERSE.

    python tests/contraste_i18n.py --langue fa --moteur google --essai 40
    python tests/contraste_i18n.py --langue fa --moteur les-deux
    python tests/contraste_i18n.py --langue fa --rapport      # sans appeler

CE QU'IL FAIT, ET POURQUOI DANS CE SENS-LA.

On prend le persan de l'interface, on le fait retraduire EN FRANCAIS par un
moteur, et on compare au francais d'origine. Le moteur ne voit jamais ce
francais : il ne peut donc pas l'inventer. C'est le meme raisonnement que
contraste_deepl.py, qui fait ce travail sur le corpus de vocabulaire.

⚠️ VERS LE FRANCAIS, PAS VERS L'ALLEMAND. Pour le corpus, la source est
l'allemand. Pour l'INTERFACE, la source est le francais -- retraduire vers
l'allemand ajouterait une traduction de plus, donc de la derive, donc du bruit.

⚠️ CE N'EST PAS UNE LISTE DE FAUTES. Un moteur traduit, il ne juge pas. Si le
persan rend « Reviser » par un mot que le moteur retraduit en « Repasser », les
deux sont justes. Le rapport ne contient que les ecarts FRANCS, et aucun
verdict : c'est une liste a regarder, comme divergences-deepl.md.

⚠️ ET IL NE VOIT PAS LE REGISTRE. Le persan distingue تو et شما, l'ecrit
litteraire (کتابی) de l'oral (محاوره‌ای). Un aller-retour ne dira jamais si le
ton est juste pour une app d'apprentissage. Cette question-la reste entiere, et
elle demande un persanophone.

POURQUOI DEUX MOTEURS. Le persan est une langue a ressources moyennes : c'est
le regime ou les fournisseurs divergent vraiment. Plutot que de choisir sur
reputation, `--moteur les-deux` les fait tourner sur le meme echantillon et
compte ce que chacun signale, et ce qu'ils signalent ENSEMBLE. Un ecart vu par
les deux moteurs merite un regard ; un ecart vu par un seul est plus
probablement du bruit de traduction.

LES CLES. Une ligne par fichier, rien d'autre :

    C:/Users/jacqu/.wortando/google.secret     la cle API Google, restreinte
                                               a Cloud Translation
    C:/Users/jacqu/.wortando/azure.secret      ligne 1 la cle, ligne 2 la region

Le dossier du projet est cherche en second (convention `*.secret`, gitignoree),
mais il est synchronise par OneDrive : mieux vaut .wortando.
"""
import argparse
import difflib
import io
import json
import os
import re
import subprocess
import sys
import time
import unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTILS = os.environ.get("WORTANDO_OUTILS", "C:/Users/jacqu/.wortando")
LOT = 40                 # textes par appel
SEUIL = 0.42             # en dessous, l'ecart est franc

GABARIT = re.compile(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}")
BALISE = re.compile(r"<[^>]+>")


# ----------------------------------------------------------------- les cles

def lire_cle(nom):
    for dossier in (OUTILS, RACINE):
        chemin = os.path.join(dossier, nom)
        if os.path.exists(chemin):
            lignes = [l.strip() for l in io.open(chemin, encoding="utf-8").read().split("\n")]
            lignes = [l for l in lignes if l]
            if lignes:
                return lignes
    return None


# ------------------------------------------------------------------ moteurs

def google(textes, source, cible, cle):
    """Cloud Translation v2. Une cle API suffit, pas de compte de service."""
    import urllib.request
    url = "https://translation.googleapis.com/language/translate/v2?key=" + cle
    out = []
    for i in range(0, len(textes), LOT):
        corps = json.dumps({"q": textes[i:i + LOT], "source": source,
                            "target": cible, "format": "text"}).encode("utf-8")
        req = urllib.request.Request(url, data=corps,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=90) as r:
            rep = json.loads(r.read().decode("utf-8"))
        out.extend(t["translatedText"] for t in rep["data"]["translations"])
        if i + LOT < len(textes):
            time.sleep(0.3)
    return out


def azure(textes, source, cible, cles):
    """Translator 3.0. La REGION est obligatoire dans l'en-tete, sinon 401 --
    et le message d'erreur ne dit pas que c'est elle qui manque."""
    import urllib.request
    cle = cles[0]
    region = cles[1] if len(cles) > 1 else "global"
    url = ("https://api.cognitive.microsofttranslator.com/translate"
           "?api-version=3.0&from=%s&to=%s" % (source, cible))
    out = []
    for i in range(0, len(textes), LOT):
        corps = json.dumps([{"Text": t} for t in textes[i:i + LOT]]).encode("utf-8")
        req = urllib.request.Request(url, data=corps, headers={
            "Ocp-Apim-Subscription-Key": cle,
            "Ocp-Apim-Subscription-Region": region,
            "Content-Type": "application/json",
        })
        with urllib.request.urlopen(req, timeout=90) as r:
            rep = json.loads(r.read().decode("utf-8"))
        out.extend(t["translations"][0]["text"] for t in rep)
        if i + LOT < len(textes):
            time.sleep(0.3)
    return out


MOTEURS = {"google": ("google.secret", google), "azure": ("azure.secret", azure)}


# ---------------------------------------------------------------- comparaison

def nu(s):
    """Le texte, debarrasse de ce qu'un moteur n'a pas a traduire.

    Les gabarits et les balises passent souvent tels quels, parfois abimes, et
    leur presence fausse la comparaison dans les deux sens. On les retire des
    DEUX cotes : leur conservation est deja controlee par controle_i18n.py, ce
    n'est pas le travail de celui-ci.
    """
    s = GABARIT.sub(" ", BALISE.sub(" ", s or ""))
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def proximite(a, b):
    a, b = nu(a), nu(b)
    if not a or not b:
        return 1.0 if a == b else 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


# -------------------------------------------------------------------- donnees

def dump_i18n():
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js")],
                       capture_output=True, cwd=RACINE)
    if r.returncode:
        sys.exit("node n'a pas pu evaluer I18N :\n"
                 + r.stderr.decode("utf-8", "replace")[:600])
    return json.loads(r.stdout.decode("utf-8"))


def dossier_sortie(langue):
    d = os.path.join(RACINE, "relecture_" + langue)
    if not os.path.isdir(d):
        os.makedirs(d)
    return d


def chemin_cache(langue):
    return os.path.join(dossier_sortie(langue), "cache-contraste-i18n.json")


def lire_cache(langue):
    try:
        return json.load(io.open(chemin_cache(langue), encoding="utf-8"))
    except Exception:
        return {}


# --------------------------------------------------------------------- rapport

def ecrire_rapport(langue, moteur, lignes, examines):
    chemin = os.path.join(dossier_sortie(langue), "divergences-i18n-%s.md" % moteur)
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Ecarts de sens sur l'interface -- %s\n\n" % moteur)
        f.write("Produit par `python tests/contraste_i18n.py --langue %s "
                "--moteur %s`. **Aucune correction appliquee.**\n\n" % (langue, moteur))
        f.write("Le %s de l'interface a ete retraduit EN FRANCAIS, puis compare "
                "au francais d'origine. Le moteur ne voit jamais ce francais : "
                "il ne peut donc pas l'inventer.\n\n" % langue)
        f.write("**Ce n'est pas une liste de fautes.** Un moteur traduit, il ne "
                "juge pas : une formulation differente est souvent aussi juste. "
                "Et il ne voit RIEN du registre -- tutoiement, langue ecrite ou "
                "parlee -- qui reste a un relecteur humain.\n\n")
        f.write("%d cles examinees, %d ecarts francs (proximite < %.2f).\n\n"
                % (examines, len(lignes), SEUIL))
        for e in sorted(lignes, key=lambda x: x["proximite"]):
            f.write("### `%s`  (proximite %.2f)\n\n" % (e["cle"], e["proximite"]))
            f.write("| | |\n|---|---|\n")
            f.write("| francais d'origine | %s |\n" % e["fr"].replace("|", "\\|"))
            f.write("| %-6s ecrit | %s |\n" % (langue, e["cible"].replace("|", "\\|")))
            f.write("| retraduit | %s |\n\n" % e["retour"].replace("|", "\\|"))
    return chemin


# ------------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--moteur", default="les-deux",
                    choices=["google", "azure", "les-deux"])
    ap.add_argument("--essai", type=int, help="ne traiter que N cles, pour calibrer")
    ap.add_argument("--rapport", action="store_true",
                    help="relire le cache sans appeler aucun service")
    a = ap.parse_args()

    d = dump_i18n()
    fr, cible = d.get("fr", {}), d.get(a.langue, {})
    if not cible:
        sys.exit("aucune cle en %s" % a.langue)

    # Ce qui n'est traduit dans aucune langue n'a rien a faire ici.
    intraduits = {k for k, v in fr.items() if d.get("en", {}).get(k) == v}
    cles = [k for k in cible if k in fr and k not in intraduits]
    cles.sort()
    if a.essai:
        cles = cles[:a.essai]
    textes = [cible[k] for k in cles]
    caracteres = sum(len(t) for t in textes)

    moteurs = ["google", "azure"] if a.moteur == "les-deux" else [a.moteur]
    cache = lire_cache(a.langue)
    resultats = {}

    for m in moteurs:
        fichier, appel = MOTEURS[m]
        cache.setdefault(m, {})
        manquants = [k for k in cles if cache[m].get(k, {}).get("src") != cible[k]]
        if manquants and not a.rapport:
            cles_api = lire_cle(fichier)
            if not cles_api:
                print("⚠️ %s : %s introuvable (cherche dans %s puis %s) -- moteur saute."
                      % (m, fichier, OUTILS, RACINE))
                continue
            print("%s : %d cles a traduire (%d en cache), %d caracteres..."
                  % (m, len(manquants), len(cles) - len(manquants), caracteres))
            try:
                retours = appel([cible[k] for k in manquants], a.langue, "fr", cles_api)
            except Exception as e:
                detail = ""
                if hasattr(e, "read"):
                    try:
                        detail = e.read().decode("utf-8", "replace")[:400]
                    except Exception:
                        pass
                print("⚠️ %s a refuse : %s %s" % (m, e, detail))
                continue
            for k, r in zip(manquants, retours):
                cache[m][k] = {"src": cible[k], "retour": r}
            with io.open(chemin_cache(a.langue), "w", encoding="utf-8", newline="\n") as f:
                json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
        elif manquants and a.rapport:
            print("%s : %d cles absentes du cache, ignorees (--rapport)."
                  % (m, len(manquants)))

        lignes = []
        for k in cles:
            e = cache[m].get(k)
            if not e or e.get("src") != cible[k]:
                continue
            p = proximite(fr[k], e["retour"])
            if p < SEUIL:
                lignes.append({"cle": k, "fr": fr[k], "cible": cible[k],
                               "retour": e["retour"], "proximite": p})
        vus = sum(1 for k in cles if cache[m].get(k, {}).get("src") == cible[k])
        if not vus:
            continue
        resultats[m] = {k["cle"] for k in lignes}
        chemin = ecrire_rapport(a.langue, m, lignes, vus)
        print("  %-7s %3d ecarts francs sur %d cles  ->  %s"
              % (m, len(lignes), vus, os.path.relpath(chemin, RACINE)))

    if len(resultats) == 2:
        g, z = resultats["google"], resultats["azure"]
        print("\nCOMPARAISON DES DEUX MOTEURS")
        print("  signale par les deux    : %d  <-- a regarder en premier" % len(g & z))
        print("  google seulement        : %d" % len(g - z))
        print("  azure seulement         : %d" % len(z - g))
        print("\n⚠️ Un ecart vu par les DEUX moteurs merite un regard. Vu par un")
        print("   seul, c'est plus souvent du bruit de traduction qu'une faute.")
        communs = sorted(g & z)
        if communs:
            print("\n  " + "\n  ".join(communs[:20]))
            if len(communs) > 20:
                print("  ... et %d autres" % (len(communs) - 20))


if __name__ == "__main__":
    main()
