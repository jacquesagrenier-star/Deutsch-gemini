# -*- coding: utf-8 -*-
"""Couverture audio des TUILES de « Construis la phrase » en espagnol.

    python audio/couverture_tuiles_es.py            # rapport, deux voix
    python audio/couverture_tuiles_es.py --liste    # et les mots sans fichier

NE LE 24 OCT. 2026. Jacques : « Desayunamos se dit encore avec le son du
cellulaire ». Dans la seance, chaque tuile touchee dit son mot (v904), en
minuscules en espagnol (v919) : direAllemand(« desayunamos »). Or les fichiers
« tuiles » de manifest_es.py ne couvrent que les phrases de Premiers pas et
d'A1 voyage. La phrase de Jacques, « Desayunamos siempre en la cocina. », est
l'exemple de la carte « la cocina » (temas.json) : ses mots n'ont pas de
fichier a eux, et le telephone les dit.

LES PHRASES QUE LA SEANCE PEUT POSER A REMETTRE EN ORDRE (index.html) :
  - phraseDeCarte() : l'exemple d'une carte de nom, d'adjectif ou de verbe, de
    3 a 11 mots (mots_max du palier le plus large) -- sources « noms »,
    « adjetivos.json », « verbos.json » du manifeste ;
  - la feuille de conjugaison : la phrase d'un autre temps du verbe, 3 a 10
    mots -- source « verbos.temps » ;
  - Premiers pas et A1 voyage -- deja couverts (source « tuiles »).
Chaque mot y est decoupe comme dans l'app : aux espaces, ponctuation collee
retiree, minuscules ; un fichier par mot et par voix, sha1(mot)[:16].

Le cout est celui de la porteuse « Palabra. ... <mot> » (generer_es.py), un
credit par caractere en multilingual v2.
"""
import argparse, collections, hashlib, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import manifest_es   # noqa

PORTEUSE = "Palabra. ... %s"
SOURCES = {"noms": 11, "adjetivos.json": 11, "verbos.json": 11, "verbos.temps": 10,
           "premiers_pas": 99, "a1_voyage": 99}


def mot_de_tuile(m):
    """Ce que l'app dit quand on touche la tuile (cp-tuile, forme « ordre »)."""
    return re.sub(r'^[¿¡«"(]+|[.,;:!?»")]+$', "", m).lower()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--liste", action="store_true")
    a = p.parse_args()
    for variante, dossier in (("es", "es-es"), ("latam", "es-419")):
        base = os.path.join(RACINE, "audio", "mp3", dossier)
        a_un_fichier = lambda t: os.path.exists(os.path.join(base, hashlib.sha1(t.encode("utf-8")).hexdigest()[:16] + ".mp3"))
        phrases = {}
        for t, source, niveau in manifest_es.recolter(variante):
            n = len(t.split())
            if source in SOURCES and 3 <= n <= SOURCES[source]:
                phrases.setdefault(t, (source, niveau))
        manquants = collections.Counter()
        niveau_mot = {}
        completes = 0
        par_source = collections.Counter()
        for t, (source, niveau) in phrases.items():
            mots = [w for w in (mot_de_tuile(m) for m in t.split()) if re.search(r"\w", w)]
            trous = [w for w in mots if not a_un_fichier(w)]
            par_source[source] += 1
            if not trous:
                completes += 1
            for w in trous:
                manquants[w] += 1
                niveau_mot.setdefault(w, niveau)
        cout = sum(len(PORTEUSE % w) for w in manquants)
        print("%-7s %d phrases possibles (%s)" % (dossier, len(phrases),
              ", ".join("%s %d" % kv for kv in par_source.most_common())))
        print("        %d entierement couvertes, %d avec au moins un mot a la voix du telephone"
              % (completes, len(phrases) - completes))
        print("        %d mots distincts sans fichier, environ %d credits (porteuse, v2)"
              % (len(manquants), cout))
        par_niv = collections.Counter(niveau_mot[w] for w in manquants)
        print("        par niveau : %s" % ", ".join("%s %d" % kv for kv in sorted(par_niv.items())))
        print("        les plus frequents : %s" % ", ".join("%s (%d)" % kv for kv in manquants.most_common(15)))
        if a.liste:
            for w, k in manquants.most_common():
                print("   %-24s %4d  %s" % (w, k, niveau_mot[w]))
        print("        desayunamos : %s" % ("fichier present" if a_un_fichier("desayunamos") else "SANS FICHIER"))


if __name__ == "__main__":
    main()
