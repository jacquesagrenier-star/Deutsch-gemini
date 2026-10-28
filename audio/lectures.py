# -*- coding: utf-8 -*-
"""Ce que la voix DIT, quand ce n'est pas exactement ce qui est ecrit.

    python audio/lectures.py            # controle : tout texte a chiffres a-t-il sa lecture ?

LE DEFAUT QU'ON REPARE (28 oct. 2026). La professeure d'allemand de Jacques,
a Berlin : « die Zahlen kommen nicht gut raus » -- les prix et les heures
sortaient haches, interrompus. Les textes partaient TELS QUELS chez
ElevenLabs : « 3,90 € », « 11:30–14:30 », « am 12. Mai », « 3. Stock ». La
voix devine : la virgule et le point d'un ordinal deviennent des pauses, le
tiret et les deux-points se lisent au hasard.

LE REMEDE. L'ecrit ne change pas -- l'eleve doit lire « 3,90 € », c'est ce
qu'il verra en Allemagne. Seul ce qu'on ENVOIE a la voix change : une
lecture en toutes lettres, ecrite et relue a la main (« drei Euro neunzig »,
« am zwoelften Mai »). Le fichier garde son nom, sha1(texte ECRIT)[:16] :
l'app ne sait rien de la lecture.

UN FICHIER PAR LANGUE APPRISE : audio/lectures/<langue>.json, { ecrit: dit }.
Toute langue future (anglais, japonais...) en a un des sa premiere voix.

LA REGLE QUI EMPECHE LE RETOUR DU DEFAUT. Un texte prononce qui contient un
chiffre DOIT avoir sa lecture, et une lecture ne doit plus contenir de
chiffre. controler() le dit ; tests/verifier.py l'appelle avant chaque push,
et generer.py / generer_es.py passent par lecture() avant d'appeler la voix.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "audio", "lectures")
_CACHE = {}


def table(langue):
    if langue not in _CACHE:
        chemin = os.path.join(DOSSIER, langue + ".json")
        _CACHE[langue] = {}
        if os.path.exists(chemin):
            with io.open(chemin, encoding="utf-8") as f:
                _CACHE[langue] = json.load(f)
    return _CACHE[langue]


def lecture(langue, texte):
    """Le texte a envoyer a la voix : sa lecture s'il en a une, sinon lui-meme."""
    return table(langue).get(texte, texte)


def a_chiffres(texte):
    return bool(re.search(r"\d", texte))


def controler(langue, textes):
    """Renvoie (sans_lecture, lectures_chiffrees) pour ces textes prononces."""
    t = table(langue)
    sans = sorted({x for x in textes if a_chiffres(x) and x not in t})
    chiffrees = sorted(k for k, v in t.items() if a_chiffres(v))
    return sans, chiffrees


def textes_de():
    with io.open(os.path.join(RACINE, "audio", "manifest.json"), encoding="utf-8") as f:
        m = json.load(f)
    items = m if isinstance(m, list) else (m.get("textes") or m.get("items") or list(m.values()))
    if isinstance(items, dict):
        items = list(items.values())
    return [x if isinstance(x, str) else x.get("texte", "") for x in items]


def textes_es():
    sys.path.insert(0, os.path.join(RACINE, "audio"))
    import manifest_es
    out = set()
    for v in ("es", "latam"):
        for e in manifest_es.entrees(v):
            out.add(e["texte"] if isinstance(e, dict) else e)
    return sorted(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    probleme = False
    for langue, source in (("de", textes_de), ("es", textes_es)):
        sans, chiffrees = controler(langue, source())
        print("%s : %d lectures, %d textes a chiffres sans lecture, %d lectures encore chiffrees"
              % (langue, len(table(langue)), len(sans), len(chiffrees)))
        for x in sans[:20]:
            print("   SANS LECTURE :", x.replace("\n", " / ")[:100])
        for x in chiffrees[:20]:
            print("   LECTURE CHIFFREE :", x.replace("\n", " / ")[:100])
        probleme = probleme or bool(sans or chiffrees)
    sys.exit(1 if probleme else 0)


if __name__ == "__main__":
    main()
