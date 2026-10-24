# -*- coding: utf-8 -*-
"""Controle TOUS les fichiers audio, sans les ecouter : saturation, clics,
mots trop courts pour la normalisation, voyelles tenues.

    python audio/controler_sons.py                   # espagnol, deux voix
    python audio/controler_sons.py --dossiers de     # l'allemand (audio/mp3/)
    python audio/controler_sons.py --json suspects.json

NE LE 24 OCT. 2026, DE DEUX PLAINTES DE JACQUES SUR L'ESPAGNOL :
  - « son agressant » en touchant les tuiles « a » et « qué ». Les fichiers
    sortis d'ElevenLabs etaient sains (-18 dB RMS). C'est NORMALISER.PY qui les
    a detruits : sous 400 ms, la fenetre de mesure EBU R128, ffmpeg rend une
    sonie de « -inf », le gain calcule est infini, et le fichier ressort en
    creneau sature -- crete au-dessus de 0 dBFS, RMS a -1,7 dB, contre -11 a
    -16 pour tout le reste. Ce defaut-la est MECANIQUE : il se mesure sans
    doute possible, d'ou ce controle.
  - « hayyyy » la veille (« ¿Hay…? », voyelle tenue 0,97 s) : la duree de
    parole rapportee au nombre de lettres le trahit, pour les mots seuls.

CE QU'IL NE VOIT PAS : un mot dit dans la mauvaise langue (« a pie » lu en
anglais, « once » comme le mot anglais). Le son est propre, seule l'oreille
juge. On liste donc a part les textes A RISQUE -- courts, avec une espace, donc
generes SANS porteuse (generer_es.py ne la met qu'aux textes sans espace) --
pour les refaire en porteuse ou les faire ecouter.

LES SEUILS (mesures le 24 oct. sur le corpus) : un fichier sain a sa crete
vers -1,2 dBFS (normaliser.py vise -1,5 dBTP) et son RMS entre -11 et -17 dB.
"""
import argparse, io, json, os, re, subprocess, sys, unicodedata
from concurrent.futures import ThreadPoolExecutor
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))

SR = 22050
RMS_MAX = -8.0          # dB ; le corpus sain est entre -11 et -17, les satures a -1,5
# Une crete vers 0 dBFS seule n'est PAS le defaut : 35 fichiers allemands et
# une vingtaine d'espagnols y sont, RMS normal -- un depassement d'encodage mp3,
# inaudible. Les creneaux, eux, montent de +1,8 a +6,7 dBFS.
CRETE_MAX = 1.0         # dBFS
DUREE_MIN = 0.40        # s ; sous la fenetre EBU R128, la sonie ne se mesure pas
BORD_MAX = -20.0        # dB sous le maximum, aux 5 premieres / dernieres ms ; une
                        # phrase qui commence sur une voyelle est vers -29, sans defaut
# Mot seul : parole <= socle + pente x lettres. « ¿Hay…? » de Monica (0,97 s
# pour 3 lettres) depasse ; les mots sains du corpus restent dessous.
TRAINE_SOCLE, TRAINE_PENTE = 0.40, 0.10
ARTICLES = {"el", "la", "los", "las", "un", "una", "unos", "unas"}

DOSSIERS = {"es": ["es-es", "es-419"], "de": [""]}


def pcm(chemin):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", chemin, "-ac", "1", "-ar", str(SR),
                        "-f", "f32le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)


def mesurer(chemin):
    x = pcm(chemin)
    if len(x) < SR // 50:
        return None
    fen = int(0.010 * SR)
    env_db = 10 * np.log10(np.convolve(x * x, np.ones(fen) / fen, mode="same") + 1e-12)
    haut = env_db.max()
    parle = np.where(env_db > haut - 40)[0]
    d0, d1 = parle[0], parle[-1]
    bord = int(0.005 * SR)
    niv = lambda s: 10 * np.log10(np.mean(s * s) + 1e-12)
    return {
        "duree": round(float(len(x) / SR), 3),
        "parole": round(float((d1 - d0) / SR), 3),
        "crete": round(float(20 * np.log10(np.max(np.abs(x)) + 1e-9)), 1),
        "rms": round(float(niv(x[d0:d1 + 1])), 1),
        "tete": round(float(niv(x[:bord]) - haut), 1),
        "queue": round(float(niv(x[-bord:]) - haut), 1),
    }


def lettres(texte):
    return sum(1 for c in unicodedata.normalize("NFD", texte) if c.isalpha())


def defauts(m, texte):
    d = []
    if m["crete"] > CRETE_MAX or m["rms"] > RMS_MAX:
        d.append("SATURE")
    if m["duree"] < DUREE_MIN:
        d.append("COURT")
    if m["tete"] > BORD_MAX or m["queue"] > BORD_MAX:
        d.append("CLIC")
    if texte and " " not in texte.strip() and lettres(texte):
        if m["parole"] > TRAINE_SOCLE + TRAINE_PENTE * lettres(texte):
            d.append("TRAINE")
    return d


def a_risque(texte):
    """Court, avec une espace, sans article : genere sans porteuse."""
    mots = re.findall(r"[^\W\d_]+", texte.lower())
    return (" " in texte.strip() and 2 <= len(mots) <= 3 and lettres(texte) <= 12
            and not (mots[0] in ARTICLES))


def textes_es():
    import manifest_es
    out = {}
    for variante, dossier in (("es", "es-es"), ("latam", "es-419")):
        for e in manifest_es.entrees(variante):
            out.setdefault(dossier, {})[e["id"]] = e
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dossiers", default="es", choices=sorted(DOSSIERS))
    p.add_argument("--json", default="")
    p.add_argument("--travailleurs", type=int, default=8)
    a = p.parse_args()
    textes = textes_es() if a.dossiers == "es" else {}
    suspects = []
    for dossier in DOSSIERS[a.dossiers]:
        base = os.path.join(RACINE, "audio", "mp3", dossier)
        fichiers = sorted(f for f in os.listdir(base) if f.endswith(".mp3"))
        connus = textes.get(dossier, {})
        def un(f):
            m = mesurer(os.path.join(base, f))
            return f, m
        with ThreadPoolExecutor(max_workers=a.travailleurs) as ex:
            resultats = list(ex.map(un, fichiers))
        nb = {}
        for f, m in resultats:
            ident = f[:-4]
            e = connus.get(ident)
            texte = e["texte"] if e else ""
            d = ["ILLISIBLE"] if m is None else defauts(m, texte)
            if e and a_risque(texte):
                d.append("SANS_PORTEUSE")
            for x in d:
                nb[x] = nb.get(x, 0) + 1
            if d:
                suspects.append(dict(dossier=dossier or "de", id=ident, texte=texte,
                                     source=e["source"] if e else "", defauts=d, **(m or {})))
        print("%-7s %6d fichiers   %s" % (dossier or "de", len(fichiers),
              "  ".join("%s %d" % kv for kv in sorted(nb.items())) or "rien"))
    graves = [s for s in suspects if set(s["defauts"]) & {"SATURE", "CLIC", "TRAINE", "ILLISIBLE"}]
    for s in graves[:60]:
        print("  %-7s %s %-22s %-24s crete %5.1f rms %5.1f dur %.2f parole %.2f" % (
            s["dossier"], s["id"], ",".join(s["defauts"]), s["texte"][:24],
            s.get("crete", 0), s.get("rms", 0), s.get("duree", 0), s.get("parole", 0)))
    if len(graves) > 60:
        print("  ... %d de plus" % (len(graves) - 60))
    if a.json:
        json.dump(suspects, io.open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sys.exit(1 if graves else 0)


if __name__ == "__main__":
    main()
