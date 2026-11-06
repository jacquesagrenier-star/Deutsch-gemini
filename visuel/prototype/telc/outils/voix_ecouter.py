"""Les voix enregistrees de l'ecoute du telc (Hoeren et Hoeren und Schreiben) : une piste par texte entendu.

    python visuel/prototype/telc/outils/voix_ecouter.py                      # a blanc : ce qui manque, ce que ca coute
    python visuel/prototype/telc/outils/voix_ecouter.py --pour-de-vrai --plafond 17500 [--sauter-sans-voix]

ACCORD DE JACQUES, 6 nov. 2026 (« Oui, lance les voix », devis DEVIS-VOIX-HOEREN.md) : ElevenLabs multilingual v2
SEULEMENT (jamais Flash), plafond 20 000 credits en tout, dont environ 2 500 pour concevoir les cinq voix
manquantes (outils/concevoir_voix_ecouter.py).

LA FABRICATION EST CELLE DU DTZ, sans le modifier : visuel/prototype/dtz/outils/voix.py (fabriquer, nom_fichier) --
une voix par personne, les repliques voisines en contexte, une demi-seconde entre deux repliques, la piste entiere
ramenee a la sonie du cours, le nom du fichier tire des voix et des textes (cache d'un an). Ce qui change :
  - les pistes viennent de donnees/hoeren.json et hoeren-schreiben.json, avec les cles que lisent hoeren.js et
    hoeren-schreiben.js (telcH1-T1, telcH1-42, telcH1-T4-intro, telcHS1-52, telc-consigne-T1, telc-nummer-42…) ;
  - la voix recoit « dit », la lecture en lettres ecrite a cote de chaque replique a chiffres (les memes lectures
    sont versees dans audio/lectures/de.json par outils/lectures_ecouter.py) ;
  - les fichiers vont dans audio/mp3/dtz/telc/ du depot principal (servis sous BASE_PISTES + « telc/… ») et le
    manifeste dans donnees/voix-ecouter.json.
Ensuite : python audio/controler_sons.py --dossiers dtz (ou le dossier telc), puis le depot (voir avec le chef).
"""
import argparse
import importlib.util
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
spec = importlib.util.spec_from_file_location("voix_dtz", os.path.join(DEPOT, "visuel", "prototype", "dtz", "outils", "voix.py"))
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
SORTIE = os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", "telc")
MANIFESTE = os.path.join(TELC, "donnees", "voix-ecouter.json")
NOMBRES = {42: "zweiundvierzig", 43: "dreiundvierzig", 44: "vierundvierzig", 45: "fünfundvierzig", 46: "sechsundvierzig"}


def pistes(H, HS):
    """{cle: [{wer, text, dit?}]} : tout ce que la page fait entendre."""
    out = {}
    for t, c in H["consignes"].items():
        out["telc-consigne-" + t] = [{"wer": c["wer"], "text": c["text"], "dit": c.get("dit")}]
    out["telc-consigne-HS"] = [{"wer": HS["consigne"]["wer"], "text": HS["consigne"]["text"], "dit": HS["consigne"].get("dit")}]
    for nr, mot in NOMBRES.items():
        out["telc-nummer-%d" % nr] = [{"wer": "aurora", "text": "Nummer %d." % nr, "dit": "Nummer %s." % mot}]
    for s in H["series"]:
        c = "telcH%s-" % s["id"]
        out[c + "T1"] = s["T1"]["audio"]
        out[c + "T2"] = s["T2"]["audio"]
        for a in s["T3"]:
            out[c + str(a["nr"])] = a["audio"]
        out[c + "T4-intro"] = s["T4"]["intro"]
        for p in s["T4"]["personen"]:
            out[c + str(p["nr"])] = p["audio"]
    for s in HS["series"]:
        for m in s["nachrichten"]:
            out["telcHS%s-%s" % (s["id"], m["nr"])] = m["audio"]
    return out


def dit(l):
    return l.get("dit") or V.lectures.lecture("de", l["text"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pour-de-vrai", action="store_true", help="depenser reellement les credits")
    ap.add_argument("--plafond", type=int, default=0, help="credits au plus pour ce lancement")
    ap.add_argument("--sauter-sans-voix", action="store_true", help="laisser de cote les pistes dont une voix n'est pas choisie")
    ap.add_argument("--seulement", default="", help="ne produire que ces cles (separees par des virgules), pour un essai")
    a = ap.parse_args()
    H = json.load(io.open(os.path.join(TELC, "donnees", "hoeren.json"), encoding="utf-8"))
    HS = json.load(io.open(os.path.join(TELC, "donnees", "hoeren-schreiben.json"), encoding="utf-8"))
    voix = H["voix"]
    tout = pistes(H, HS)
    if a.seulement:
        tout = {k: v for k, v in tout.items() if k in a.seulement.split(",")}
    manifeste = json.load(io.open(MANIFESTE, encoding="utf-8")) if os.path.exists(MANIFESTE) else {}

    sans_voix = sorted({l["wer"] for ls in tout.values() for l in ls if not (voix.get(l["wer"]) or {}).get("voice_id")})
    sans_lecture = sorted({l["text"] for ls in tout.values() for l in ls if re.search(r"\d", dit(l))})
    if sans_voix and a.sauter_sans_voix:
        ecartees = [k for k, ls in tout.items() if any(l["wer"] in sans_voix for l in ls)]
        tout = {k: v for k, v in tout.items() if k not in ecartees}
        print("Pistes en attente de leur voix (%s) : %d" % (", ".join(sans_voix), len(ecartees)))
        sans_voix = []
    if sans_voix:
        print("Voix sans identifiant (bloc « voix » de hoeren.json) : " + ", ".join(sans_voix))
    if sans_lecture:
        print("Repliques a chiffres sans lecture : " + " | ".join(sans_lecture))
    if sans_voix or sans_lecture:
        sys.exit(1)

    a_faire = []
    for cle, lignes in tout.items():
        f = "telc/" + V.nom_fichier(lignes, voix)
        if manifeste.get(cle) == f and os.path.exists(os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", f)):
            continue
        a_faire.append((cle, lignes, f, sum(len(dit(l)) for l in lignes)))
    cout = sum(x[3] for x in a_faire)
    print("Pistes : %d en tout, %d a produire, environ %d credits (multilingual v2 : 1 credit par caractere)."
          % (len(tout), len(a_faire), cout))
    if not a.pour_de_vrai:
        print("A blanc : rien n'est depense. Relancer avec --pour-de-vrai --plafond N.")
        return
    if not a.plafond:
        sys.exit("--plafond est obligatoire pour depenser.")
    V.normaliser.FF = V.normaliser.ffmpeg()
    cle_api = (os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    for racine in (V.PRINCIPAL, DEPOT):
        chemin = os.path.join(racine, "elevenlabs.secret")
        if not cle_api and os.path.exists(chemin):
            cle_api = io.open(chemin, encoding="utf-8").read().strip()
    if not cle_api:
        sys.exit("Cle ElevenLabs absente.")
    os.makedirs(SORTIE, exist_ok=True)
    depense = 0
    for cle, lignes, f, c in a_faire:
        if depense + c > a.plafond:
            print("Plafond atteint (%d + %d > %d) : arret avant %s." % (depense, c, a.plafond, cle))
            break
        print("  %-18s %5d car.  %s" % (cle, c, f))
        # la voix dit la lecture en lettres ; le nom du fichier vient du texte affiche
        dites = [{"wer": l["wer"], "text": dit(l)} for l in lignes]
        try:
            V.fabriquer(dites, voix, cle_api, os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", f))
        except V.generer.TexteBloque as e:
            print("    REFUSE par ElevenLabs : %s" % e)
            continue
        depense += c
        manifeste[cle] = f
        io.open(MANIFESTE, "w", encoding="utf-8", newline="\n").write(json.dumps(manifeste, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print("\nEnviron %d credits depenses. Fichiers : %s ; manifeste : %s" % (depense, SORTIE, os.path.relpath(MANIFESTE, DEPOT)))


if __name__ == "__main__":
    main()
