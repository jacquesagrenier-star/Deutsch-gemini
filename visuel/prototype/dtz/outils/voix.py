"""Les voix enregistrees du DTZ, Hoeren : une piste par annonce, conversation ou avis, plus les consignes.

    python visuel/prototype/dtz/outils/voix.py                       # a blanc : ce qui manque et ce que ca couterait
    python visuel/prototype/dtz/outils/voix.py --pour-de-vrai --plafond 20000

ACCORD DE JACQUES, 4 nov. 2026 (« Oui, les deux ») : ElevenLabs multilingual v2 SEULEMENT (Flash interdit, regle du
12 oct.), environ 82 000 credits pour les six series, plafond 90 000. --plafond borne chaque lancement ; le script
s'arrete avant de le depasser.

UNE PISTE = PLUSIEURS REPLIQUES, UNE VOIX PAR PERSONNE. Chaque replique est dite par la voix de son « wer »
(donnees/hoeren.json, bloc « voix »), avec ses voisines en contexte (previous_text / next_text, comme les scenes :
sans elles, une phrase courte isolee se fait repeter). Les repliques sont mises bout a bout avec une demi-seconde
de silence, puis LA PISTE ENTIERE est ramenee a la sonie du cours (audio/normaliser.py) : les ecarts entre deux
personnes d'une meme conversation restent ceux que les voix ont produits.

LES REGLAGES. Les consignes (Aurora) gardent ceux du cours (stabilite 0,75) : c'est la voix qui enseigne. Les
personnes des textes prennent ceux du dialogue (audio/scene_audio.py : stabilite 0,40, style 0,45), sinon une
annonce de gare et une conversation dans l'escalier sonneraient pareil.

LES NOMBRES SE DISENT EN LETTRES : chaque replique passe par audio/lectures.py ; une replique a chiffres sans
lecture arrete le script avant toute depense (outils/lectures_dtz.py les verse).

LE NOM DU FICHIER VIENT DE CE QUI EST DIT (sha1 des voix et des textes, 16 caracteres) : les sons sont servis avec un
cache d'un an (firebase.json), un texte corrige apres la relecture doit donc changer de nom. Les fichiers vont dans
audio/mp3/dtz/ DU DEPOT PRINCIPAL (le dossier que Firebase Hosting publie), le manifeste dans donnees/voix-hoeren.json :
{cle de la piste: fichier}. La page lit ce manifeste ; une piste absente passe par la voix du telephone.
Le depot sur Firebase (audio/deposer.py) se fait depuis le depot principal, apres audio/controler_sons.py.
"""
import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
DTZ = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(DTZ)))
PRINCIPAL = os.path.normpath(os.path.join(DEPOT, "..", "..", ".."))
if not os.path.exists(os.path.join(PRINCIPAL, "firebase.json")):
    PRINCIPAL = DEPOT                                     # lance depuis le depot principal lui-meme
sys.path.insert(0, os.path.join(DEPOT, "audio"))
import generer                                            # noqa: E402
import lectures                                           # noqa: E402
import normaliser                                         # noqa: E402

SORTIE = os.path.join(PRINCIPAL, "audio", "mp3", "dtz")
MANIFESTE = os.path.join(DTZ, "donnees", "voix-hoeren.json")
MODELE = "eleven_multilingual_v2"
DIALOGUE = {"stability": 0.40, "similarity_boost": 0.75, "style": 0.45, "use_speaker_boost": True}
SILENCE = 0.5

# les petites phrases que l'enregistrement de l'examen dit entre les textes ; ecrites en lettres, elles n'ont pas
# besoin de lecture
NOMBRES = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
           "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig"]


def pistes(H):
    """{cle: [{wer, text}]} : tout ce que l'examen fait entendre."""
    out = {}
    for t, c in H["consignes"].items():
        out["consigne-" + t] = [{"wer": c["wer"], "text": c["de"]}]
    out["beispiel"] = [{"wer": "aurora", "text": "Beispiel."}]
    for n in range(1, 21):
        out["nummer-%d" % n] = [{"wer": "aurora", "text": "Nummer %s." % NOMBRES[n]}]
    for s in H["series"]:
        for t in ("T1", "T2", "T3"):
            for it in s[t]:
                if it.get("audio"):
                    out["%s-%s-%s" % (s["id"], t, it["nr"])] = it["audio"]
                    paire = [x["nr"] for x in s[t] if x.get("gleiches_audio") == it["nr"]]
                    if paire:
                        out["nummer-%d-%d" % (it["nr"], paire[0])] = [
                            {"wer": "aurora", "text": "Nummer %s und %s." % (NOMBRES[it["nr"]], NOMBRES[paire[0]])}]
        out["%s-T4-intro" % s["id"]] = s["T4"]["intro"]
        for a in s["T4"]["aussagen"]:
            out["%s-T4-%s" % (s["id"], a["nr"])] = a["audio"]
    return out


def nom_fichier(lignes, voix):
    cle = json.dumps([[voix[l["wer"]]["voice_id"], l["text"]] for l in lignes] + [MODELE], ensure_ascii=False)
    return hashlib.sha1(cle.encode("utf-8")).hexdigest()[:16] + ".mp3"


def silence(chemin):
    subprocess.run([normaliser.FF, "-hide_banner", "-nostats", "-y", "-f", "lavfi", "-i",
                    "anullsrc=r=44100:cl=mono", "-t", str(SILENCE), "-c:a", "libmp3lame", "-b:a", "64k", chemin],
                   capture_output=True, check=True)


def fabriquer(lignes, voix, cle_api, dest):
    tmp = tempfile.mkdtemp(prefix="dtz-voix-")
    try:
        morceaux = []
        pause = os.path.join(tmp, "pause.mp3")
        silence(pause)
        for i, l in enumerate(lignes):
            generer.VOIX = voix[l["wer"]]["voice_id"]
            reglages = generer.REGLAGES if l["wer"] == "aurora" else DIALOGUE
            avant = lectures.lecture("de", lignes[i - 1]["text"]) if i else None
            apres = lectures.lecture("de", lignes[i + 1]["text"]) if i + 1 < len(lignes) else None
            octets = generer.synthetiser(lectures.lecture("de", l["text"]), MODELE, cle_api, avant, apres, reglages)
            m = os.path.join(tmp, "%02d.mp3" % i)
            io.open(m, "wb").write(octets)
            if morceaux:
                morceaux.append(pause)
            morceaux.append(m)
        liste = os.path.join(tmp, "liste.txt")
        io.open(liste, "w", encoding="utf-8").write("".join("file '%s'\n" % p.replace("\\", "/") for p in morceaux))
        brut = os.path.join(tmp, "brut.mp3")
        r = subprocess.run([normaliser.FF, "-hide_banner", "-nostats", "-y", "-f", "concat", "-safe", "0", "-i", liste,
                            "-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "64k", brut],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode:
            raise RuntimeError("assemblage impossible : " + r.stderr[-300:])
        if not normaliser.normaliser(brut, dest, os.path.join(tmp, "inter.mp3")):
            raise RuntimeError("normalisation impossible")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pour-de-vrai", action="store_true", help="depenser reellement les credits")
    ap.add_argument("--plafond", type=int, default=0, help="credits au plus pour ce lancement")
    ap.add_argument("--serie", default="", help="seulement les pistes de cette serie (S1...) et les communes")
    ap.add_argument("--sauter-sans-voix", action="store_true", help="laisser de cote les pistes dont une voix n'est pas choisie")
    a = ap.parse_args()

    H = json.load(io.open(os.path.join(DTZ, "donnees", "hoeren.json"), encoding="utf-8"))
    voix = H["voix"]
    tout = pistes(H)
    if a.serie:
        tout = {k: v for k, v in tout.items() if k.startswith(a.serie + "-") or not re.match(r"S\d+-", k)}
    manifeste = json.load(io.open(MANIFESTE, encoding="utf-8")) if os.path.exists(MANIFESTE) else {}

    # avant toute depense : une voix sans identifiant, une replique a chiffres sans lecture
    sans_voix = sorted({l["wer"] for ls in tout.values() for l in ls if not (voix.get(l["wer"]) or {}).get("voice_id")})
    sans_lecture = sorted({l["text"] for ls in tout.values() for l in ls
                           if re.search(r"\d", lectures.lecture("de", l["text"]))})
    if sans_voix and a.sauter_sans_voix:
        # les pistes qui attendent une voix pas encore choisie (la radio) restent a la voix du telephone
        ecartees = [k for k, ls in tout.items() if any(l["wer"] in sans_voix for l in ls)]
        tout = {k: v for k, v in tout.items() if k not in ecartees}
        print("Pistes en attente de leur voix (%s) : %s" % (", ".join(sans_voix), ", ".join(ecartees)))
        sans_voix = []
    if sans_voix:
        print("Voix sans identifiant (bloc « voix » de hoeren.json) : " + ", ".join(sans_voix))
    if sans_lecture:
        print("Repliques a chiffres sans lecture (outils/lectures_dtz.py) :")
        for t in sans_lecture:
            print("  - " + t)
    if sans_voix or sans_lecture:
        sys.exit(1)

    a_faire = []
    for cle, lignes in tout.items():
        f = nom_fichier(lignes, voix)
        if manifeste.get(cle) == f and os.path.exists(os.path.join(SORTIE, f)):
            continue
        a_faire.append((cle, lignes, f, sum(len(lectures.lecture("de", l["text"])) for l in lignes)))
    cout = sum(x[3] for x in a_faire)
    print("Pistes : %d en tout, %d a produire, environ %d credits (multilingual v2 : 1 credit par caractere)."
          % (len(tout), len(a_faire), cout))
    if not a.pour_de_vrai:
        print("A blanc : rien n'est depense. Relancer avec --pour-de-vrai --plafond N.")
        return
    if not a.plafond:
        sys.exit("--plafond est obligatoire pour depenser.")

    normaliser.FF = normaliser.ffmpeg()
    # la cle : la variable d'environnement, sinon elevenlabs.secret du depot principal (le worktree n'en a pas) ;
    # elle n'est jamais affichee
    cle_api = (os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    for racine in (PRINCIPAL, DEPOT):
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
        try:
            fabriquer(lignes, voix, cle_api, os.path.join(SORTIE, f))
        except generer.TexteBloque as e:
            print("    REFUSE par ElevenLabs : %s" % e)
            continue
        depense += c
        manifeste[cle] = f
        io.open(MANIFESTE, "w", encoding="utf-8", newline="\n").write(json.dumps(manifeste, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print("\nEnviron %d credits depenses. Fichiers : %s ; manifeste : %s" % (depense, SORTIE, os.path.relpath(MANIFESTE, DEPOT)))
    print("Ensuite : python audio/controler_sons.py (dossier dtz), puis audio/deposer.py depuis le depot principal.")


if __name__ == "__main__":
    main()
