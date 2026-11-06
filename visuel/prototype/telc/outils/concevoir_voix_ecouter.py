"""Les cinq voix a concevoir pour l'ecoute du telc (Voice Design, audio/concevoir_voix.py), et leur ecoute a l'aveugle.

    python visuel/prototype/telc/outils/concevoir_voix_ecouter.py              # a blanc : ce qui serait demande
    python visuel/prototype/telc/outils/concevoir_voix_ecouter.py --pour-de-vrai
    python visuel/prototype/telc/outils/concevoir_voix_ecouter.py --garder f_jung=B,f_alt=A,...

Accord de Jacques du 6 nov. 2026 (« Oui, lance les voix », devis DEVIS-VOIX-HOEREN.md : 2 500 credits d'echantillons
dans le plafond de 20 000). Trois apercus par voix, sur une VRAIE replique du role (regle de concevoir_voix.py), puis
un fichier par role : A, une seconde et demie de silence, B, puis C, pour que Jacques choisisse a l'oreille sans
savoir laquelle est laquelle. --garder enregistre les voix choisies dans le compte et ecrit leur voice_id dans
donnees/hoeren.json.

La cle ElevenLabs : ELEVENLABS_API_KEY, sinon elevenlabs.secret du depot principal ; jamais affichee.
"""
import argparse
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
PRINCIPAL = os.path.normpath(os.path.join(DEPOT, "..", "..", ".."))
if not os.path.exists(os.path.join(PRINCIPAL, "firebase.json")):
    PRINCIPAL = DEPOT
CONCEVOIR = os.path.join(DEPOT, "audio", "concevoir_voix.py")
DOSSIER = os.path.join(DEPOT, "audio", "a_ecouter_voix", "conception")
DONNEES = os.path.join(TELC, "donnees", "hoeren.json")

NEG = " Not robotic, not theatrical, not an advertising voice."
ROLES = {
    "f_jung": ("A native German woman of about twenty-two from Berlin, a university student, speaking natural everyday "
               "standard German: bright, relaxed and friendly, quick but clear, a light smile in the voice. Not childish, "
               "not breathy, not girlish, not a cheerful customer-service voice." + NEG,
               "Ich bin Studentin und jobbe jedes Wochenende in einem Café, auch sonntags. Ehrlich gesagt finde ich das "
               "ganz normal, und ich bekomme sogar mehr Geld pro Stunde."),
    "f_alt": ("A native German woman of about seventy-five, warm, calm and a little slow, clear and well articulated, "
              "standard German with a light Berlin colour, the voice of an alert retired grandmother. Not shaky, not "
              "sad, not frail, not a narrator voice." + NEG,
              "Seit mein Mann gestorben ist, wohne ich allein. Meine Katze Mimi ist für mich wie eine Freundin: Sie "
              "wartet auf mich, wenn ich nach Hause komme."),
    "m_jung": ("A native German young man of about nineteen, standard German, casual, friendly and relaxed, natural pace, "
               "a fully adult young voice. Not childish, not nasal, not mumbling, not an announcer voice." + NEG,
               "Touristen gibt es in Berlin genug, und die finden auch am Sonntag genug zu tun. Ein Tag ohne Einkaufen "
               "tut uns allen gut, finde ich."),
    "radio_f": ("A native German woman of about thirty-five, a professional radio presenter and in-store announcer, "
                "standard German, clear, warm, steady and confident, perfectly articulated, medium pace. Not breathy, "
                "not overly cheerful, not an audiobook narrator." + NEG,
                "Liebe Kundinnen und Kunden, ein Angebot für alle, die es eilig haben: Heute ab achtzehn Uhr bekommen "
                "Sie alle Brote und Brötchen aus unserer Bäckerei zum halben Preis."),
    "radio_m": ("A native German man of about forty, a professional announcer for railway stations and radio traffic news, "
                "standard German, calm, clear, neutral and reliable, medium-low voice, perfectly articulated. Not "
                "dramatic, not a deep movie-trailer voice, not bored." + NEG,
                "Achtung an Gleis sieben: Der I C E nach Hamburg, Abfahrt zehn Uhr fünfzehn, fährt heute ausnahmsweise "
                "von Gleis neun ab."),
}


def env():
    e = dict(os.environ)
    if not e.get("ELEVENLABS_API_KEY"):
        chemin = os.path.join(PRINCIPAL, "elevenlabs.secret")
        if os.path.exists(chemin):
            e["ELEVENLABS_API_KEY"] = io.open(chemin, encoding="utf-8").read().strip()
    if not e.get("ELEVENLABS_API_KEY"):
        sys.exit("Cle ElevenLabs absente.")
    e["PYTHONIOENCODING"] = "utf-8"
    return e


def ffmpeg():
    sys.path.insert(0, os.path.join(DEPOT, "audio"))
    import normaliser                                     # noqa: E402
    return normaliser.ffmpeg()


def ecoute(nom, ff):
    """A, silence, B, silence, C : un fichier par role, a ecouter d'un trait."""
    entrees = [os.path.join(DOSSIER, "telc-%s-%s.mp3" % (nom, l)) for l in "ABC"]
    entrees = [x for x in entrees if os.path.exists(x)]
    sortie = os.path.join(DOSSIER, "ECOUTER-telc-%s.mp3" % nom)
    args = [ff, "-hide_banner", "-nostats", "-y"]
    filtre, n = [], 0
    for k, x in enumerate(entrees):
        args += ["-i", x]
        filtre.append("[%d:a]aresample=44100,aformat=channel_layouts=mono,loudnorm=I=-16[a%d]" % (k, k))
    args += ["-f", "lavfi", "-t", "1.5", "-i", "anullsrc=r=44100:cl=mono"]
    sil = len(entrees)
    parts = []
    for k in range(len(entrees)):
        if k:
            parts.append("[s%d]" % k)
        parts.append("[a%d]" % k)
    splits = len(entrees) - 1
    if splits:
        filtre.append("[%d:a]asplit=%d%s" % (sil, splits, "".join("[s%d]" % (k + 1) for k in range(splits))) if splits > 1
                      else "[%d:a]anull[s1]" % sil)
    filtre.append("%sconcat=n=%d:v=0:a=1[out]" % ("".join(parts), len(parts)))
    args += ["-filter_complex", ";".join(filtre), "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "96k", sortie]
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print("  assemblage impossible pour %s : %s" % (nom, r.stderr[-300:]))
        return None
    return sortie


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pour-de-vrai", action="store_true")
    ap.add_argument("--garder", default="", help="f_jung=B,f_alt=A,... : les apercus retenus par Jacques")
    a = ap.parse_args()
    if a.garder:
        d = json.load(io.open(DONNEES, encoding="utf-8"))
        for paire in a.garder.split(","):
            nom, lettre = paire.split("=")
            final = "Wortando - telc %s" % nom
            r = subprocess.run([sys.executable, CONCEVOIR, "--nom", "telc-" + nom, "--garder", "--lequel", lettre, "--nom-final", final],
                               env=env(), capture_output=True, text=True, encoding="utf-8", errors="replace")
            print(r.stdout.strip() or r.stderr.strip())
            recu = json.load(io.open(os.path.join(DOSSIER, "telc-%s.json" % nom), encoding="utf-8"))
            vid = (recu.get("retenu") or {}).get("voice_id")
            if vid:
                d["voix"][nom]["voice_id"] = vid
                d["voix"][nom]["nom"] = d["voix"][nom]["nom"].split(" :")[0] + " : « %s », conçue le 6 nov. 2026, choix %s de Jacques" % (final, lettre)
        io.open(DONNEES, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("voice_id ecrits dans donnees/hoeren.json")
        return
    total = sum(len(t) for _, t in ROLES.values())
    print("5 voix, 3 apercus chacune ; textes d'essai : %d caracteres en tout." % total)
    if not a.pour_de_vrai:
        for nom, (desc, texte) in ROLES.items():
            print("  %-8s description %3d car., texte %3d car." % (nom, len(desc), len(texte)))
        print("A blanc : rien n'est demande. Relancer avec --pour-de-vrai.")
        return
    ff = ffmpeg()
    for nom, (desc, texte) in ROLES.items():
        r = subprocess.run([sys.executable, CONCEVOIR, "--nom", "telc-" + nom, "--description", desc, "--texte-essai", texte],
                           env=env(), capture_output=True, text=True, encoding="utf-8", errors="replace")
        print((r.stdout or "").strip() or (r.stderr or "").strip()[-400:])
        f = ecoute(nom, ff)
        if f:
            print("  a ecouter : %s" % f)


if __name__ == "__main__":
    main()
