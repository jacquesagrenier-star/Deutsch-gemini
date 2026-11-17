# -*- coding: utf-8 -*-
"""Les voix enregistrees des dialogues et de la grammaire de Wortando Pflege : un fichier par phrase dite.

    python pflege/outils/voix.py                                # a blanc : ce qui manque, ce que ca coute
    python pflege/outils/voix.py --pour-de-vrai --plafond 44300 # depenser (plafond obligatoire)
    python pflege/outils/voix.py --seulement soins_dlg_01        # un essai sur un dialogue ou un point

ACCORD DU CHEF, 14 nov. 2026 (devis de pflege/VOIX.md) : la variante « chemin modele » -- les repliques de la
conversation modele, les Redemittel, les questions d'ecoute et leurs choix, les exemples, tableaux et phrases de la
grammaire --, ElevenLabs multilingual v2 SEULEMENT (jamais Flash), plafond 44 300 credits. Les autres branches des
dialogues (fautes, variantes) attendent que Jacques ait entendu ce premier lot. Ne pas lancer avant le « d'accord » de
pflege-examen sur pflege/VOIX.md (les deux sessions partent ensemble).

LA FABRICATION EST CELLE DU DTZ ET DU TELC (visuel/prototype/dtz/outils/voix.py : la synthese de audio/generer.py,
la sonie de audio/normaliser.py), sans les modifier. Ce qui change :
  - un fichier par phrase, pas par piste : l'app rejoue une replique seule (jouer son role, remettre dans l'ordre)
    ou les enchaine (ecouter) ; une replique recoit la precedente en contexte (previous_text ; pas de next_text,
    qui coupait la fin) ;
  - la voix d'un personnage vient de pflege/sources/voix.json ; Aurora garde les reglages du cours, les
    personnages ceux du dialogue (stabilite 0,40, style 0,45) ;
  - la voix dit la « lecture » en lettres quand le texte a des chiffres ; ces lectures sont aussi versees dans
    audio/lectures/de.json (regle de CLAUDE.md), sans jamais en remplacer une ;
  - le nom du fichier est le sha1 de la voix, du texte dit et du modele (16 caracteres) : un texte corrige change de
    nom (les sons sont servis avec un cache d'un an) ;
  - les fichiers vont dans audio/mp3/pflege/ DU DEPOT PRINCIPAL ; le manifeste {cle: fichier} dans
    pflege/datos/sons.json (cle : « <id>/r/<n> » replique, « <id>/rm/<n> » Redemittel, « <id>/q/<n> » question,
    « <id>/q/<n>/c/<k> » choix, « <id>/ex/<n> » exemple, « <id>/tab/<n>/<k> » case, « <id>/s/<n> » phrase de la serie).
Ensuite : python audio/controler_sons.py --dossiers pflege (aucun SATURE, CLIC ni TRAINE), puis le depot sur Firebase
(audio/deposer.py), avec le chef.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
PFLEGE = os.path.dirname(ICI)
DEPOT = os.path.dirname(PFLEGE)
sys.path.insert(0, ICI)
import textes as T                                          # noqa: E402

spec = importlib.util.spec_from_file_location("voix_dtz", os.path.join(DEPOT, "visuel", "prototype", "dtz", "outils", "voix.py"))
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
SORTIE = os.path.join(V.PRINCIPAL, "audio", "mp3", "pflege")
MANIFESTE = os.path.join(PFLEGE, "datos", "sons.json")
LECTURES = os.path.join(DEPOT, "audio", "lectures", "de.json")
CHIFFRE = re.compile(r"\d")


def items(export):
    """[(cle, qui, texte affiche, texte dit, avant, apres)] : tout ce qui se dit, dans l'ordre."""
    out = []

    def ajoute(cle, qui, x, cle_de="de", avant=None, apres=None):
        de = x[cle_de]
        out.append((cle, qui, de, x.get("lecture") or de, avant, apres))

    for d in export["dialogues"]["dialogues"]:
        rep = d["repliques"]
        dits = [r.get("lecture") or r["de"] for r in rep]
        for i, r in enumerate(rep):
            ajoute("%s/r/%d" % (d["id"], i), r["qui"], r,
                   avant=dits[i - 1] if i else None, apres=dits[i + 1] if i + 1 < len(rep) else None)
        for i, r in enumerate(d["redemittel"]):
            ajoute("%s/rm/%d" % (d["id"], i), "aurora", r)
        for i, q in enumerate(d["questions"]):
            ajoute("%s/q/%d" % (d["id"], i), "aurora", q)
            for k, c in enumerate(q["choix"]):
                ajoute("%s/q/%d/c/%d" % (d["id"], i, k), "aurora", c)
    for c in export.get("redemittel", {}).get("cartes", []):
        if not c["dialogue"]:   # une carte de dialogue garde le son <dialogue>/rm/<n> ; les autres ont le leur
            ajoute(c["id"], "aurora", c)
    for p in export["grammaire"]["points"]:
        for i, e in enumerate(p["exemples"]):
            ajoute("%s/ex/%d" % (p["id"], i), "aurora", e)
        for i, ligne in enumerate(p["tableau"]):
            for k, c in enumerate(ligne):
                if isinstance(c, dict) and c.get("de"):
                    ajoute("%s/tab/%d/%d" % (p["id"], i, k), "aurora", c)
        for i, q in enumerate(p["serie"]):
            ajoute("%s/s/%d" % (p["id"], i), "aurora", q, cle_de="phrase")
    return out


def nom_fichier(voice_id, dit):
    cle = json.dumps([voice_id, dit, V.MODELE], ensure_ascii=False)
    return hashlib.sha1(cle.encode("utf-8")).hexdigest()[:16] + ".mp3"


def fabriquer_un(voice_id, aurora, dit, avant, apres, cle_api, dest):
    import tempfile, shutil
    tmp = tempfile.mkdtemp(prefix="pflege-voix-")
    try:
        V.generer.VOIX = voice_id
        reglages = V.generer.REGLAGES if aurora else V.DIALOGUE
        octets = V.generer.synthetiser(dit, V.MODELE, cle_api, avant, apres, reglages)
        brut = os.path.join(tmp, "brut.mp3")
        io.open(brut, "wb").write(octets)
        if not V.normaliser.normaliser(brut, dest, os.path.join(tmp, "inter.mp3")):
            raise RuntimeError("normalisation impossible")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def verser_lectures(liste):
    """Les lectures des textes a chiffres dans audio/lectures/de.json (ajouts seulement)."""
    table = json.load(io.open(LECTURES, encoding="utf-8")) if os.path.exists(LECTURES) else {}
    ajouts, conflits = 0, []
    for _, _, de, dit, _, _ in liste:
        if de == dit or not CHIFFRE.search(de):
            continue
        if de in table and table[de] != dit:
            conflits.append(de)
        elif de not in table:
            table[de] = dit
            ajouts += 1
    if ajouts:
        io.open(LECTURES, "w", encoding="utf-8", newline="\n").write(json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    return ajouts, conflits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pour-de-vrai", action="store_true", help="depenser reellement les credits")
    ap.add_argument("--plafond", type=int, default=0, help="credits au plus pour ce lancement")
    ap.add_argument("--seulement", default="", help="ne produire que les cles qui commencent ainsi (virgules)")
    a = ap.parse_args()
    cfg = json.load(io.open(os.path.join(PFLEGE, "sources", "voix.json"), encoding="utf-8"))
    res, manques = T.construire_tout(ecrire_fichiers=False)
    export = T.exporter(res)
    liste = items(export)
    if a.seulement:
        pref = tuple(a.seulement.split(","))
        liste = [x for x in liste if x[0].startswith(pref)]
    sans_voix = sorted({q for _, q, *_ in liste if q not in cfg["personnages"]})
    sans_lecture = sorted({de for _, _, de, dit, _, _ in liste if CHIFFRE.search(dit)})
    if sans_voix:
        print("Personnages sans voix (pflege/sources/voix.json) : " + ", ".join(sans_voix))
    if sans_lecture:
        print("Textes a chiffres sans lecture : " + " | ".join(sans_lecture))
    if sans_voix or sans_lecture:
        sys.exit(1)
    manifeste = json.load(io.open(MANIFESTE, encoding="utf-8")) if os.path.exists(MANIFESTE) else {}
    # un meme texte dit par une meme voix n'est produit qu'une fois
    a_faire, vus = [], set()
    for cle, qui, de, dit, avant, apres in liste:
        vid = cfg["voix"][cfg["personnages"][qui]]["voice_id"]
        f = nom_fichier(vid, dit)
        manifeste[cle] = f
        if f in vus or os.path.exists(os.path.join(SORTIE, f)):
            continue
        vus.add(f)
        a_faire.append((cle, qui, vid, dit, avant, apres, f))
    cout = sum(len(x[3]) for x in a_faire)
    print("Phrases dites : %d ; fichiers distincts a produire : %d ; environ %d credits (v2 : 1 credit par caractere)."
          % (len(liste), len(a_faire), cout))
    par_voix = {}
    for x in a_faire:
        v = cfg["personnages"][x[1]]
        par_voix[v] = par_voix.get(v, 0) + len(x[3])
    print("Par voix : " + ", ".join("%s %d" % kv for kv in sorted(par_voix.items())))
    if not a.pour_de_vrai:
        print("A blanc : rien n'est depense. Relancer avec --pour-de-vrai --plafond N.")
        return
    if not a.plafond:
        sys.exit("--plafond est obligatoire pour depenser.")
    ajouts, conflits = verser_lectures(liste)
    print("Lectures versees dans audio/lectures/de.json : %d ajouts%s" % (ajouts, (", %d conflits laisses tels quels : %s" % (len(conflits), " | ".join(conflits))) if conflits else ""))
    V.normaliser.FF = V.normaliser.ffmpeg()
    # depuis un worktree, la cle vit a la racine du depot principal (jamais copiee ni affichee)
    secret = os.path.join(V.PRINCIPAL, "elevenlabs.secret")
    if not os.environ.get("ELEVENLABS_API_KEY") and os.path.exists(secret):
        os.environ["ELEVENLABS_API_KEY"] = io.open(secret, encoding="utf-8").read().strip()
    cle_api = V.generer.cle_api()
    os.makedirs(SORTIE, exist_ok=True)
    depense = 0
    try:
        for cle, qui, vid, dit, avant, apres, f in a_faire:
            if depense + len(dit) > a.plafond:
                print("Plafond atteint (%d + %d > %d) : arret avant %s." % (depense, len(dit), a.plafond, cle))
                break
            try:
                # sans le texte suivant : avec next_text, 11 repliques sur 775 finissaient coupees net (CLIC,
                # lot du 14 nov.), la voix enchainant sur une suite qui n'est pas dans le fichier ; refaites sans,
                # toutes propres du premier coup
                fabriquer_un(vid, qui == "aurora", dit, avant, None, cle_api, os.path.join(SORTIE, f))
            except V.generer.TexteBloque as e:
                print("    REFUSE par ElevenLabs (%s) : %s" % (cle, e))
                continue
            depense += len(dit)
            print("  %-42s %4d car.  %s" % (cle, len(dit), f))
    finally:
        # le manifeste ne garde que les fichiers qui existent
        presents = {k: v for k, v in manifeste.items() if os.path.exists(os.path.join(SORTIE, v))}
        T.ecrire(MANIFESTE, {k: presents[k] for k in sorted(presents)})
        print("\nEnviron %d credits depenses. Fichiers : %s ; manifeste : %s (%d cles)"
              % (depense, SORTIE, os.path.relpath(MANIFESTE, DEPOT), len(presents)))


if __name__ == "__main__":
    main()
