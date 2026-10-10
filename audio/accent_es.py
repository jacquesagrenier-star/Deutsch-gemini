# -*- coding: utf-8 -*-
"""Espagne ou Amerique latine ? Mesure l'accent d'une voix ElevenLabs par le
son « th » (distincion) ou « s » (seseo), sans avoir a l'ecouter.

    python audio/accent_es.py VOICE_ID [VOICE_ID ...]

POURQUOI CETTE MESURE (10 oct. 2026). Jacques choisit les voix espagnoles
sans parler espagnol, et l'outil de conception d'ElevenLabs ne garantit pas
l'accent demande. Or une difference s'entend -- et se MESURE -- sans
comprendre la langue : en Espagne, le z et le c devant e/i se disent « th »
(caza = « katha ») ; en Amerique latine, « s » (caza = casa).

LA METHODE : des paires de mots qui ne different que par ce son.
  casa / caza, sien / cien, coser / cocer    (le second : « th » en Espagne)
Un « s » est un sifflement fort, concentre dans les aigus (4-10 kHz) ; un
« th » est un souffle faible et diffus. Pour chaque mot : l'energie des aigus
sur ses cinq trames les plus sifflantes, rapportee a son energie totale (pour
que le volume ne compte pas). Rapport R = mot en z/c divise par mot en s.
  - R nettement sous le TEMOIN -> le z/c siffle moins que le s : Espagne.
  - R proche du temoin          -> meme son : Amerique latine.
LE TEMOIN, propre a chaque voix : casa / masa, deux vrais « s ». Il dit ce
que vaut « le meme son » pour CETTE voix, et c'est contre lui qu'on juge.

Cout : environ 20 credits par voix (sept mots courts, modele Flash). Les sons
sont gardes dans audio/a_ecouter_voix/espagnol/accent/<voix>/ : relancer ne
redemande rien.
"""
import json, os, subprocess, sys, urllib.request
import numpy as np

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer  # noqa : la cle, le format, les reglages du corpus

PAIRES = [("casa", "caza"), ("sien", "cien"), ("coser", "cocer")]
TEMOIN = ("casa", "masa")
TAUX = 44100


def son(voix, mot):
    dossier = os.path.join(RACINE, "audio", "a_ecouter_voix", "espagnol", "accent", voix)
    os.makedirs(dossier, exist_ok=True)
    chemin = os.path.join(dossier, mot + ".mp3")
    if not os.path.exists(chemin):
        url = ("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s" % (voix, generer.FORMAT))
        # Le mot seul, avec un point : sans ponctuation, un mot isole est
        # parfois lu comme une interrogation.
        corps = json.dumps({"text": mot.capitalize() + ".", "model_id": generer.MODELES["flash"][0],
                            "voice_settings": generer.REGLAGES, "seed": generer.SEED}).encode("utf-8")
        req = urllib.request.Request(url, data=corps, method="POST", headers={
            "xi-api-key": generer.cle_api(), "Content-Type": "application/json", "Accept": "audio/mpeg"})
        with urllib.request.urlopen(req, timeout=120) as r:
            open(chemin, "wb").write(r.read())
    brut = subprocess.run(["ffmpeg", "-v", "quiet", "-i", chemin, "-f", "s16le", "-ac", "1",
                           "-ar", str(TAUX), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(brut, dtype=np.int16).astype(np.float64) / 32768.0


def sifflement(x):
    n, pas = 1024, 256
    fen = np.hanning(n)
    trames = [x[i:i + n] * fen for i in range(0, len(x) - n, pas)]
    spec = np.abs(np.fft.rfft(np.array(trames), axis=1)) ** 2
    f = np.fft.rfftfreq(n, 1.0 / TAUX)
    aigus = spec[:, (f >= 4000) & (f <= 10000)].sum(axis=1)
    total = spec.sum(axis=1)
    top = lambda v: np.sort(v)[-5:].mean()
    return top(aigus) / top(total)


def mesurer(voix):
    s = lambda mot: sifflement(son(voix, mot))
    temoin = s(TEMOIN[1]) / s(TEMOIN[0])
    rapports = [s(z) / s(ss) for ss, z in PAIRES]
    med = float(np.median(rapports))
    rel = med / temoin
    verdict = ("Espagne (distincion, « th »)" if rel < 0.5 else
               "Amerique latine (seseo, « s »)" if rel > 0.75 else "incertain : a ecouter")
    return temoin, rapports, rel, verdict


def main():
    for voix in sys.argv[1:]:
        temoin, rapports, rel, verdict = mesurer(voix)
        print("%s  temoin %.2f  paires %s  ->  %.2f du temoin  :  %s"
              % (voix, temoin, " ".join("%.2f" % r for r in rapports), rel, verdict))


if __name__ == "__main__":
    main()
