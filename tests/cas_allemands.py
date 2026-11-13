# -*- coding: utf-8 -*-
"""Les cas allemands apres une preposition portent leur nom allemand (lot 90, 13 nov. 2026).

En polonais, ukrainien et russe, appeler le Dativ « celownik / давальний / дательный » apres une
preposition fait croire a une equivalence fausse : « in dem Haus » se dit « w domu » (miejscownik),
« mit » prend le narzednik / орудний / творительный, « von, aus, zu, seit, bei » le genitif... On ecrit
donc « in + Dativ », et pour le lieu (Wo?) on donne entre parenthèses le vrai cas de la langue :
« (po polsku tu miejscownik: w domu) ». Le cas local reste juste pour l'objet indirect (komu? / кому?),
les verbes qui regissent le Dativ (helfen, danken...) et les pronoms (mir, dir : « мне больно »).

    python tests/cas_allemands.py     controle des fichiers servis ; code 1 s'il reste « preposition + cas
                                      local » ou « Wo? ... cas local »

Appele par tests/verifier.py. Ce qui est juste malgre le motif s'ecrit, avec sa raison, dans
tests/cas_allemands_acceptes.txt (« texte exact | raison »).
"""
import io
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "publication"))
sys.path.insert(0, os.path.join(RACINE, "tests"))
ACCEPTES = os.path.join(RACINE, "tests", "cas_allemands_acceptes.txt")

CAS_LOCAL = r"(celownik\w*|давальн\w*|дательн\w*)"
PREPS = (r"(in|an|auf|bei|mit|nach|aus|zu|von|seit|gegenüber|über|unter|vor|hinter|neben|zwischen|ab|außer|"
         r"entgegen)")
AUTRES_CAS = r"(biernik\w*|dopełniacz\w*|знахідн\w*|родов\w*|винительн\w*|родительн\w*)"
PREPS_AKK_GEN = r"(für|durch|gegen|ohne|um|bis|entlang|wegen|während|trotz|statt|anstatt|innerhalb|außerhalb|" + PREPS[1:]
MOTIFS = [
    # meme regle pour l'Akkusativ et le Genitiv (decision du chef du 13 nov.) : « für + biernik » -> « für + Akkusativ »
    re.compile(r"\b" + PREPS_AKK_GEN + r"\b(</b>)?[”“\"]?\s*(\(\w+\))?\s*\+\s*(<b>)?\s*" + AUTRES_CAS, re.I),
    # « mit + celownik », « „sich beschäftigen mit” + celownik », « an</b> + <b>дательный »
    re.compile(r"\b" + PREPS + r"\b(</b>)?[”“\"]?\s*(\(\w+\))?\s*\+\s*(<b>)?\s*" + CAS_LOCAL, re.I),
    # le lieu : « Wo? odpowiada się celownikiem », « без руху: давальний », « Місце перебування вимагає давального »
    re.compile(r"(Wo\s*\?|Gdzie\s*\?|Де\s*\?|Где\s*\?|Wechselpr\w*|без руху|bez ruchu|без движения|"
               r"місце перебування)[^.]{0,60}?" + CAS_LOCAL, re.I),
    re.compile(CAS_LOCAL + r"[^.]{0,40}?(Wo\s*\?|без руху|bez ruchu|без движения)", re.I),
]


def acceptes():
    if not os.path.exists(ACCEPTES):
        return set()
    lignes = io.open(ACCEPTES, encoding="utf-8").read().splitlines()
    return {l.split(" | ")[0].strip() for l in lignes if l.strip() and not l.startswith("#")}


def relever():
    """[(fichier, extrait, texte)] des textes servis qui donnent le cas local apres une preposition."""
    import construire_site
    import genre_lecteur
    sortie = subprocess.run(["git", "grep", "-l", "-z", "-i", "-E", "celownik|давальн|дательн|biernik|dopełniacz|знахідн|родов|винительн|родительн"], cwd=RACINE,
                            capture_output=True).stdout.decode("utf-8")
    fichiers = [f for f in sortie.split("\0")
                if f and f.endswith((".json", ".js", ".html")) and construire_site.publie(f)]
    ok = acceptes()
    res = []
    for f in fichiers:
        for t in set(genre_lecteur.chaines(f)):
            if t.strip() in ok:
                continue
            for m in MOTIFS:
                x = m.search(t)
                if x:
                    res.append((f, x.group(0), t))
                    break
    return res


def main():
    res = relever()
    for f, x, t in res:
        print("%s | %s | %s" % (f, x, t[:140].replace("\n", " ")))
    print("%d texte(s) avec le cas local apres une preposition" % len(res))
    return 1 if res else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
