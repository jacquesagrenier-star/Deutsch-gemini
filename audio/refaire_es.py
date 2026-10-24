# -*- coding: utf-8 -*-
"""Refait des fichiers ESPAGNOLS defectueux, sous leur nom d'origine.

    python audio/refaire_es.py                          # a blanc : ce qui serait fait
    python audio/refaire_es.py --renormaliser s.json    # GRATUIT : les SATURE du controle
    python audio/refaire_es.py --assembler              # GRATUIT : les paires « a · b »
    python audio/refaire_es.py --payer                  # PAYANT : REFAITS, en porteuse

Les trois gestes, du moins cher au plus cher. Le controle qui trouve les
defauts est audio/controler_sons.py ; on le relance APRES pour le voir a zero.

POURQUOI UN SCRIPT A PART. generer_es.py ne refait que ce qui MANQUE : un
fichier present est un fichier fait. Ici le fichier existe, il est servi, et
il est faux. Le nom ne change pas (c'est l'empreinte du texte AFFICHE, que
l'app recalcule) : seul ce qu'on fait DIRE a la voix change.

1. RENORMALISER (24 oct. 2026). « a » et « qué » sortaient en creneau sature :
   sous 400 ms, normaliser.py mesurait une sonie de -inf et poussait un gain
   infini (corrige dans normaliser.mesurer). La prise d'ElevenLabs, gardee
   dans audio/mp3_original/, etait saine : on la renormalise, sans un credit.

2. ASSEMBLER (24 oct. 2026). « once · doce » disait « once » a l'anglaise. Les
   paires de Premiers pas contiennent des espaces, donc generer_es.py les a
   envoyees SANS porteuse -- sur deux mots courts, le modele devine mal la
   langue (« a pie » la veille). Chaque mot existe deja seul, fait EN
   porteuse : on met bout a bout les deux prises brutes, avec une pause, et on
   normalise le tout. Seulement si chaque partie est un mot seul deja fait.

3. EN PORTEUSE (23 oct. 2026), PAYANT. « ¿Hay…? » : les points de suspension
   faisaient trainer la voix, « hayyyyy » -- on fait dire « ¿Hay? ». « a pie » :
   lu comme l'anglais (une tarte) -- on le fait dire dans la porteuse. La
   porteuse est celle des refus du 22 oct. (« Palabra. ... gracias ») : le
   point puis les points de suspension imposent une vraie pause, que
   recouper.py sait trouver. Pas d'ancien fichier en reference : l'ancien est
   justement faux.

LES ANCIENS FICHIERS sont mis de cote dans ~/.wortando/audio-es-avant-<date>/
avant d'etre remplaces. Apres : python audio/deposer.py, puis incrementer
AUDIO_REVISION dans index.html -- sans quoi les telephones gardent l'ancien
son douze mois.
"""
import argparse, datetime, io, json, os, shutil, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                       # noqa : cle, reglages, modeles
import manifest_es                   # noqa : identifiant(), entrees()
import normaliser as N               # noqa
from generer_es import VOIX, VITESSE_PORTEUSE, appeler   # noqa
from recouper import recouper, Refus  # noqa

PORTEUSE = "Palabra. ... %s"
# (texte affiche, donc nom du fichier ; texte dit dans la porteuse ; voix, ou
# None pour les deux). Faits le 23 oct. : ("¿Hay…?", "¿Hay?"), ("a pie", "a pie").
# Le 24 oct., les deux mots que controler_sons.py dit TRAINE -- dans UNE voix.
REFAITS = [
    ("pues", "pues", "es-es"),
    ("minutos", "minutos", "es-419"),
]
PAUSE_PAIRE = 0.30      # s de silence entre « once » et « doce »
ARCHIVE = os.path.join(os.path.expanduser("~"), ".wortando",
                       "audio-es-avant-%s" % datetime.date.today().strftime("%d-%m"))


def chemins(dossier, ident):
    return (os.path.join(RACINE, "audio", "mp3", dossier, ident + ".mp3"),
            os.path.join(N.SOURCE, dossier, ident + ".mp3"))


def mettre_de_cote(dossier, ident):
    os.makedirs(os.path.join(ARCHIVE, dossier), exist_ok=True)
    for ancien, nom in zip(chemins(dossier, ident), ("mp3", "original")):
        garde = os.path.join(ARCHIVE, dossier, "%s.%s.mp3" % (ident, nom))
        if os.path.exists(ancien) and not os.path.exists(garde):
            shutil.copy2(ancien, garde)


def poser(dossier, ident, prise):
    """La prise brute devient l'original, puis la version normalisee."""
    cible, original = chemins(dossier, ident)
    mettre_de_cote(dossier, ident)
    if os.path.abspath(prise) != os.path.abspath(original):
        os.makedirs(os.path.dirname(original), exist_ok=True)
        shutil.copy2(prise, original)
    tmp = cible + ".norm.mp3"
    if not N.normaliser(original, tmp, intermediaire=tmp + ".t1.mp3"):
        return False
    os.replace(tmp, cible)
    return True


def renormaliser(fichier, payer):
    suspects = [s for s in json.load(io.open(fichier, encoding="utf-8"))
                if "SATURE" in s["defauts"] and s["dossier"] in ("es-es", "es-419")]
    print("renormaliser : %d fichiers satures (gratuit)" % len(suspects))
    rates = 0
    for s in suspects:
        original = chemins(s["dossier"], s["id"])[1]
        if not os.path.exists(original):
            print("  SANS ORIGINAL %s %s %s" % (s["dossier"], s["id"], s["texte"]))
            rates += 1
            continue
        if payer and not poser(s["dossier"], s["id"], original):
            print("  RATE %s %s" % (s["dossier"], s["texte"]))
            rates += 1
    return rates


def paires(variante):
    entrees = manifest_es.entrees(variante)
    ids = {e["texte"]: e["id"] for e in entrees}
    vues = set()
    for e in entrees:
        if "·" not in e["texte"] or e["id"] in vues:
            continue
        parts = [p.strip() for p in e["texte"].split("·")]
        if all(" " not in p and p in ids for p in parts):
            vues.add(e["id"])
            yield e, [ids[p] for p in parts]


def assembler(payer):
    rates = faits = 0
    for variante, (_, dossier) in sorted(VOIX.items()):
        for e, morceaux in paires(variante):
            sources = [chemins(dossier, m)[1] for m in morceaux]
            if not all(os.path.exists(s) for s in sources):
                print("  PARTIE ABSENTE %s %s" % (dossier, e["texte"]))
                rates += 1
                continue
            faits += 1
            if not payer:
                continue
            tmp = os.path.join(RACINE, "audio", "mp3", dossier, e["id"] + ".paire.mp3")
            entrees, filtres = [], []
            for i, s in enumerate(sources):
                entrees += ["-i", s]
                filtres.append("[%d:a]aresample=44100,aformat=channel_layouts=mono[a%d]" % (i, i))
            silence = "anullsrc=r=44100:cl=mono,atrim=0:%.2f" % PAUSE_PAIRE
            suite = "".join("[a%d]%s" % (i, "[p%d]" % i if i < len(sources) - 1 else "")
                            for i in range(len(sources)))
            graphe = ";".join(filtres + ["%s[p%d]" % (silence, i) for i in range(len(sources) - 1)]
                              + ["%sconcat=n=%d:v=0:a=1[o]" % (suite, 2 * len(sources) - 1)])
            r = subprocess.run([N.FF, "-v", "error", "-y"] + entrees
                               + ["-filter_complex", graphe, "-map", "[o]",
                                  "-c:a", "libmp3lame", "-b:a", "96k", "-f", "mp3", tmp],
                               capture_output=True, text=True)
            if r.returncode != 0 or not poser(dossier, e["id"], tmp):
                print("  RATE %s %s %s" % (dossier, e["texte"], r.stderr[:200]))
                rates += 1
            if os.path.exists(tmp):
                os.remove(tmp)
    print("assembler : %d paires (deux voix), gratuit" % faits)
    return rates


def en_porteuse(payer):
    modele, taux = generer.MODELES["v2"]
    cout = int(sum(len(PORTEUSE % dit) * (1 if v else len(VOIX)) for _, dit, v in REFAITS) * taux)
    print("en porteuse : %d textes, %r, %s : environ %d credits"
          % (len(REFAITS), PORTEUSE, modele, cout))
    for affiche, dit, v in REFAITS:
        print("  %s  %-8s %-7s <- %r" % (manifest_es.identifiant(affiche), affiche,
                                         v or "les deux", PORTEUSE % dit))
    if not payer:
        return 0
    cle = generer.cle_api()
    rates = 0
    for variante, (voix, dossier) in sorted(VOIX.items()):
        bruts = os.path.join(RACINE, "audio", "bruts_es", dossier, "refaits")
        os.makedirs(bruts, exist_ok=True)
        for affiche, dit, v in REFAITS:
            if v and v != dossier:
                continue
            ident = manifest_es.identifiant(affiche)
            brut = os.path.join(bruts, ident + ".mp3")
            if not os.path.exists(brut):
                son = appeler(voix, PORTEUSE % dit, dict(generer.REGLAGES, speed=VITESSE_PORTEUSE), modele, cle)
                open(brut, "wb").write(son)
            coupe = brut + ".coupe.mp3"
            try:
                recouper(brut, coupe, texte=dit)
            except Refus as err:
                print("  REFUS %s %s : %s" % (dossier, affiche, err))
                rates += 1
                continue
            if not poser(dossier, ident, coupe):
                print("  NORMALISATION RATEE %s %s" % (dossier, affiche))
                rates += 1
            os.remove(coupe)
            print("  %s %-8s %.2f s" % (dossier, affiche, N.duree(chemins(dossier, ident)[0])))
    return rates


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--renormaliser", default="", help="le JSON de controler_sons.py --json")
    p.add_argument("--assembler", action="store_true")
    p.add_argument("--payer", action="store_true", help="appelle ElevenLabs pour REFAITS")
    a = p.parse_args()
    N.FF = N.ffmpeg()
    agir = bool(a.renormaliser or a.assembler or a.payer)
    rates = 0
    if a.renormaliser or not agir:
        if a.renormaliser:
            rates += renormaliser(a.renormaliser, True)
    if a.assembler or not agir:
        rates += assembler(a.assembler)
    if a.payer or not agir:
        rates += en_porteuse(a.payer)
    print("fait, %d rate(s)" % rates if agir else "(a blanc -- rien n'a ete touche)")


if __name__ == "__main__":
    main()
