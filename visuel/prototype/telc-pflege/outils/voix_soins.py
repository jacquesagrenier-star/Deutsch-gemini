"""Les voix enregistrees de l'examen blanc telc Deutsch B1·B2 Pflege : une piste par texte entendu.

    python visuel/prototype/telc-pflege/outils/voix_soins.py                    # a blanc : ce qui manque, ce que ca coute
    python visuel/prototype/telc-pflege/outils/voix_soins.py --detail           # le compte par piste
    python visuel/prototype/telc-pflege/outils/voix_soins.py --pour-de-vrai --plafond N   # APRES l'accord du chef

AUCUNE DEPENSE SANS ACCORD (decision de Jacques du 14 nov. 2026, Q7 : chaque lot annonce au chef avec son cout avant
d'etre lance). ElevenLabs multilingual v2 SEULEMENT, jamais Flash (regle du 12 oct.).

LA FABRICATION EST CELLE DU DTZ ET DU TELC A2·B1, sans la modifier : visuel/prototype/dtz/outils/voix.py (fabriquer,
nom_fichier) -- une voix par personne, les repliques voisines en contexte, une demi-seconde entre deux repliques, la
piste entiere ramenee a la sonie du cours, le nom du fichier tire des voix et des textes. Ce qui change :
  - les pistes viennent de donnees/hoeren.json (consignes, exemples, textes) et sprechen.json (ce que disent
    la Pruferin et Elif a l'oral), avec les cles que lit pflege-examen.js (« s1-H1-consigne », « s1-n1 »,
    « s1-H2g1 », « s1-H3 », « s1-sp1a-0 », « s1-sp2b-<sujet>-0 » ; « s1 » = la serie 1) ;
  - les nombres sont ecrits en lettres dans les textes de l'audio : une replique a chiffres arrete le script ;
  - les fichiers vont dans audio/mp3/dtz/soins/ du depot principal (servis sous BASE_PISTES + « soins/… ») et le
    manifeste dans donnees/voix-soins.json.
Ensuite : python audio/controler_sons.py sur le dossier, puis le depot (avec le chef).
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
PFLEGE = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(PFLEGE)))
spec = importlib.util.spec_from_file_location("voix_dtz", os.path.join(DEPOT, "visuel", "prototype", "dtz", "outils", "voix.py"))
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
DONNEES = os.path.join(PFLEGE, "donnees")
SORTIE = os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", "soins")
MANIFESTE = os.path.join(PFLEGE, "donnees", "voix-soins.json")
# le prix : l'abonnement Pro, 99 $ pour 600 000 credits (DEVIS-VOIX-HOEREN.md du telc A2·B1)
DOLLARS_PAR_CREDIT = 99 / 600000


def charger(nom):
    chemin = os.path.join(DONNEES, nom + ".json")
    return json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else {}


def pistes(H, S):
    """{cle: [{wer, text}]} : tout ce que la page fait entendre, serie par serie, avec les cles de examen.js
    (« s1-H1-consigne », « s1-n1 », « s1-H2g1 », « s1-sp2b-schmerz-0 »…)."""
    out = {}
    for sh in H.get("series", []):
        ss = next((x for x in S.get("series", []) if x["id"] == sh["id"]), {})
        out.update(pistes_serie(sh, ss, "s%d-" % sh["id"]))
    return out


def pistes_serie(H, S, PREFIXE):
    out = {}
    for t in H.get("teile", []):
        out[PREFIXE + t["cle"] + "-consigne"] = t["audio_consigne"]
        if t.get("beispiel"):
            out[PREFIXE + t["beispiel"]["cle"]] = t["beispiel"]["audio"]
        if t.get("audio"):
            out[PREFIXE + t["cle"]] = t["audio"]
        for g in t.get("gespraeche", []):
            out[PREFIXE + g["cle"]] = g["audio"]
        for it in t.get("items", []):
            if it.get("audio"):
                out[PREFIXE + it["cle"]] = it["audio"]
    for t in S.get("taches", []):
        for j, tour in enumerate(t.get("tours", [])):
            if tour.get("dit"):
                out[PREFIXE + t["cle"] + "-" + str(j)] = tour["dit"]
        for th, tours in (t.get("tours_nach_thema") or {}).items():
            for j, tour in enumerate(tours):
                if tour.get("dit"):
                    out[PREFIXE + t["cle"] + "-" + th + "-" + str(j)] = tour["dit"]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pour-de-vrai", action="store_true", help="depenser reellement les credits")
    ap.add_argument("--plafond", type=int, default=0, help="credits au plus pour ce lancement")
    ap.add_argument("--detail", action="store_true", help="le compte par piste")
    ap.add_argument("--seulement", default="", help="ne produire que ces cles (separees par des virgules), pour un essai")
    a = ap.parse_args()
    H, S = charger("hoeren"), charger("sprechen")
    voix = dict(H.get("voix", {}))
    voix.update(S.get("voix", {}))
    tout = pistes(H, S)
    if a.seulement:
        tout = {k: v for k, v in tout.items() if k in a.seulement.split(",")}
    manifeste = json.load(io.open(MANIFESTE, encoding="utf-8")) if os.path.exists(MANIFESTE) else {}

    sans_voix = sorted({l["wer"] for ls in tout.values() for l in ls if not (voix.get(l["wer"]) or {}).get("voice_id")})
    a_chiffres = sorted({l["text"] for ls in tout.values() for l in ls if re.search(r"\d", l["text"])})
    if sans_voix:
        print("Voix sans identifiant : " + ", ".join(sans_voix))
    if a_chiffres:
        print("Repliques a chiffres (les ecrire en lettres) : " + " | ".join(a_chiffres))
    if sans_voix or a_chiffres:
        sys.exit(1)

    a_faire = []
    for cle, lignes in tout.items():
        f = "soins/" + V.nom_fichier(lignes, voix)
        if manifeste.get(cle) == f and os.path.exists(os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", f)):
            continue
        a_faire.append((cle, lignes, f, sum(len(l["text"]) for l in lignes)))
    cout = sum(x[3] for x in a_faire)
    par_voix = {}
    for _, lignes, _, _ in a_faire:
        for l in lignes:
            par_voix[l["wer"]] = par_voix.get(l["wer"], 0) + len(l["text"])
    if a.detail:
        for cle, lignes, f, c in a_faire:
            print("  %-22s %5d car.  %d replique(s)" % (cle, c, len(lignes)))
        print("Par voix : " + ", ".join("%s %d" % (w, n) for w, n in sorted(par_voix.items(), key=lambda x: -x[1])))
    print("Pistes : %d en tout, %d a produire, %d caracteres, soit environ %d credits (multilingual v2 : 1 credit par "
          "caractere), environ %.2f $ au prix du Pro." % (len(tout), len(a_faire), cout, cout, cout * DOLLARS_PAR_CREDIT))
    if not a.pour_de_vrai:
        print("A blanc : rien n'est depense. Relancer avec --pour-de-vrai --plafond N, apres l'accord du chef.")
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
        print("  %-22s %5d car.  %s" % (cle, c, f))
        try:
            V.fabriquer(lignes, voix, cle_api, os.path.join(V.PRINCIPAL, "audio", "mp3", "dtz", f))
        except V.generer.TexteBloque as e:
            print("    REFUSE par ElevenLabs : %s" % e)
            continue
        depense += c
        manifeste[cle] = f
        io.open(MANIFESTE, "w", encoding="utf-8", newline="\n").write(json.dumps(manifeste, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print("\nEnviron %d credits depenses. Fichiers : %s ; manifeste : %s" % (depense, SORTIE, os.path.relpath(MANIFESTE, DEPOT)))


if __name__ == "__main__":
    main()
