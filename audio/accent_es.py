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
# Le modele : Flash par defaut (le moins cher) ; --v2 pour mesurer dans celui
# du corpus. Les prises sont rangees par modele. En v2, le mot est dit dans
# la porteuse du corpus (« Palabra: casa. ») : seul, v2 devine mal la langue
# (mesure aberrante le 10 oct. 2026, temoin a 5,42). « Palabra » n'a ni s ni
# z : les trames les plus sifflantes restent celles du mot.
MODELE = "v2" if "--v2" in sys.argv else "flash"


def son(voix, mot):
    dossier = os.path.join(RACINE, "audio", "a_ecouter_voix", "espagnol", "accent", voix,
                          "" if MODELE == "flash" else MODELE)
    os.makedirs(dossier, exist_ok=True)
    chemin = os.path.join(dossier, mot + ".mp3")
    if not os.path.exists(chemin):
        url = ("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s" % (voix, generer.FORMAT))
        # Le mot seul, avec un point : sans ponctuation, un mot isole est
        # parfois lu comme une interrogation.
        corps = json.dumps({"text": (("Palabra: %s." % mot) if MODELE == "v2" else mot.capitalize() + "."), "model_id": generer.MODELES[MODELE][0],
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
    # LE VERDICT SE FAIT SUR LES PAIRES BRUTES (corrige le 10 oct. 2026). Le
    # rapporter au temoin semblait plus rigoureux ; en v2, le temoin de Monica
    # est sorti a 2,52 (un « s » de casa moins appuye que celui de masa) et a
    # fait classer « Espagne » une voix dont deux paires sur trois valaient
    # 0,96 et 1,38. Un vrai « th » met les TROIS paires vers 0,05 (Lolita :
    # 0,02 a 0,05, en Flash comme en v2). Le temoin reste affiche, et signale
    # quand il s'ecarte de 1 : c'est alors la mesure qui vacille.
    verdict = ("Espagne (distincion, « th »)" if med < 0.2 else
               "Amerique latine (seseo, « s »)" if med > 0.6 else "incertain : a ecouter")
    if not (0.5 <= temoin <= 2.0):
        verdict += "  [temoin instable : %.2f]" % temoin
    return temoin, rapports, rel, verdict


# DEUX ACCENTS A ECARTER, AJOUTES LE 10 OCT. 2026. Le « s » dit Amerique
# latine, pas QUELLE Amerique latine. Deux accents que le cours ne veut pas se
# mesurent de la meme facon, par rapport au « s » de casa :
#   - l'argentin : « calle » dit « caché », le ll devient un sifflement fort
#     (un ll standard est un son voise, presque sans aigus) ;
#   - les Caraibes : le s devant consonne s'aspire, « este » dit « ehte »
#     (un s standard y siffle autant que dans casa).
# Pas de seuil absolu ici : faute de voix argentine ou caribeenne pour
# etalonner, on compare a une voix connue pour etre standard (la reference).
EXTRAS = (("ll de calle", "calle"), ("s de este", "este"))


def extras(voix):
    base = sifflement(son(voix, "casa"))
    return {nom: sifflement(son(voix, mot)) / base for nom, mot in EXTRAS}


def main():
    voix_liste = [v for v in sys.argv[1:] if not v.startswith("--")]
    for voix in voix_liste:
        temoin, rapports, rel, verdict = mesurer(voix)
        print("%s  temoin %.2f  paires %s  ->  mediane %.2f  :  %s"
              % (voix, temoin, " ".join("%.2f" % r for r in rapports), float(np.median(rapports)), verdict))
    print("\nLes deux accents a ecarter (rapport au « s » de casa) :")
    print("  ll de calle : haut = « ch » argentin ;  s de este : bas = s aspire des Caraibes")
    for voix in voix_liste:
        e = extras(voix)
        print("  %s  %s" % (voix, "   ".join("%s %.2f" % (k, v) for k, v in e.items())))


if __name__ == "__main__":
    main()
