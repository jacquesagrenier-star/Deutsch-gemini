# -*- coding: utf-8 -*-
"""Controle du VOCABULAIRE des Soins (Wortando Pflege), en plus de tests/pflege.py.

    python tests/pflege_vocabulaire.py          # code 0 si tout va bien, 1 sinon
    python tests/pflege_vocabulaire.py --detail # et la liste des entrees a relire

tests/pflege.py controle le FORMAT que l'app charge (pflege/datos/themes.json). Celui-ci lit les
SOURCES de chaque theme (pflege/sources/<theme>.py, la liste THEMES de pflege/outils/construire.py),
qui gardent ce que le fichier derive laisse tomber (homographes, lectures du mot), et verifie :
  1. pflege/datos/themes.json est a jour (construire.py --verifier) ;
  2. chaque entree : niveau A2 / B1 / B2 (C1 pour les scenes), sorte nom | verbe | adjectif | paire |
     expression, genre der / die / das + pluriel + article_fr pour un nom, perfekt pour un verbe,
     traduction et exemple dans les 9 langues d'interface ;
  3. aucun doublon entre deux entrees des Soins (meme mot, meme sorte) ;
  4. aucun doublon NON DECLARE avec le corpus general (themes.json, verbe.json, adjectif.json,
     adverbe.json, redewendung.json, funktionswort.json) : un mot qui y est deja est une REPRISE
     ("corpus": True, regle du plan : meme carte, une phrase de soins en plus), ou un homographe dans
     un autre sens qui le dit (sens_distinct) ; et une entree "corpus": True doit y etre vraiment ;
  5. aucun {Personnage} non remplace ;
  6. les nombres en lettres (CLAUDE.md, audio/lectures/) : un exemple allemand a chiffres a sa
     "lecture", un mot a chiffres sa "lecture_mot" (ou "lecture"), et une lecture n'a plus de chiffre ;
  7. l'ecriture de chaque langue : cyrillique en uk et ru (sans les lettres de l'autre), ecriture arabe
     en ar et fa (lettres persanes ی ک en fa, jamais en ar), apostrophe ukrainienne ʼ, « ؟ » en ar et
     fa, une espace avant « ? » et « ! » en francais ; en espagnol (10e langue, 16 nov.), l'alphabet latin et
     « ¿ … ? », « ¡ … ! » ;
  8. le chapitre (« chapitre », 16 nov.) : un id de pflege/sources/chapitres.py.
L'espagnol n'est pas encore exige partout : le bilan dit combien d'entrees l'ont.
"""
import importlib.util
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "pflege", "outils"))
import corpus  # noqa: E402

LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
NIVEAUX = {"A2", "B1", "B2", "C1"}
SORTES = {"nom", "verbe", "adjectif", "expression", "paire"}
CLASSE = {"nom": "nom", "verbe": "verbe", "adjectif": "adj", "adverbe": "adj", "expression": "expr", "mot-outil": "expr"}
CLASSE_SORTE = {"nom": "nom", "verbe": "verbe", "adjectif": "adj", "expression": "expr", "paire": "paire"}

CYR = re.compile(r"[Ѐ-ӿ]")
ARABE = re.compile(r"[؀-ۿ]")
SEUL_RU = re.compile(r"[ыэъёЫЭЪЁ]")
SEUL_UK = re.compile(r"[іїєґІЇЄҐ]")
PERSAN = re.compile(r"[پچژگیک]")
ARABE_SEUL = re.compile(r"[يك]")


def charger_construire():
    spec = importlib.util.spec_from_file_location("construire_pflege", os.path.join(RACINE, "pflege", "outils", "construire.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def en_dict(ligne):
    """Une ligne de MOTS (tuple de la phase 1 ou dictionnaire) -> dictionnaire."""
    if isinstance(ligne, dict):
        return ligne
    niveau, genre, mot, pluriel, article_fr, trad, exemple_de, relire = ligne
    return {"niveau": niveau, "sorte": "nom", "mot": mot, "genre": genre, "pluriel": pluriel,
            "article_fr": article_fr, "trad": trad, "exemple": exemple_de, "relire": relire, "corpus": False}


def ecritures(echecs, ou, lang, champ, val):
    if "{" in val or "}" in val:
        echecs.append("%s : %s garde un personnage non remplace : %s" % (ou, champ, val))
    if lang == "uk":
        if not CYR.search(val):
            echecs.append("%s : %s uk n'est pas en cyrillique" % (ou, champ))
        if SEUL_RU.search(val):
            echecs.append("%s : %s uk a une lettre russe : %s" % (ou, champ, val))
        if "'" in val or "’" in val:
            echecs.append("%s : %s uk : apostrophe ukrainienne attendue (ʼ) : %s" % (ou, champ, val))
    elif lang == "ru":
        if not CYR.search(val):
            echecs.append("%s : %s ru n'est pas en cyrillique" % (ou, champ))
        if SEUL_UK.search(val):
            echecs.append("%s : %s ru a une lettre ukrainienne : %s" % (ou, champ, val))
    elif lang in ("fa", "ar"):
        if not ARABE.search(val):
            echecs.append("%s : %s %s n'est pas en ecriture arabe" % (ou, champ, lang))
        if "?" in val:
            echecs.append("%s : %s %s : « ؟ » attendu : %s" % (ou, champ, lang, val))
        if lang == "fa" and ARABE_SEUL.search(val):
            echecs.append("%s : %s fa : ي ou ك arabes (ی, ک attendus) : %s" % (ou, champ, val))
        if lang == "ar" and PERSAN.search(val):
            echecs.append("%s : %s ar : lettre persane : %s" % (ou, champ, val))
    elif lang == "es":
        if CYR.search(val) or ARABE.search(val):
            echecs.append("%s : %s es n'est pas en alphabet latin : %s" % (ou, champ, val))
        if "?" in val and "¿" not in val:
            echecs.append("%s : %s es : « ¿ » attendu : %s" % (ou, champ, val))
        if "!" in val and "¡" not in val:
            echecs.append("%s : %s es : « ¡ » attendu : %s" % (ou, champ, val))
    elif lang == "fr" and re.search(r"\S[?!]", val):
        echecs.append("%s : %s fr : espace attendue avant ? ou ! : %s" % (ou, champ, val))


def main():
    detail = "--detail" in sys.argv
    echecs, avert, a_relire = [], [], []

    p = subprocess.run([sys.executable, os.path.join(RACINE, "pflege", "outils", "construire.py"), "--verifier"],
                       capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        echecs.append((p.stdout + p.stderr).strip().splitlines()[-1])

    C = charger_construire()
    spec = importlib.util.spec_from_file_location("chapitres_src", os.path.join(RACINE, "pflege", "sources", "chapitres.py"))
    CH = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(CH)
    ids_chapitres = {c["id"] for c in CH.CHAPITRES}
    avec_es = 0
    vus = {}
    comptes = {}
    for nom in C.THEMES:
        src = C.charger(nom)
        base = src.THEME.get("base", "")
        if not base.startswith("soins_"):
            echecs.append("%s : base %r sans le prefixe soins_" % (nom, base))
        if not src.THEME.get("svg"):
            echecs.append("%s : svg absent" % nom)
        tt = src.THEME.get("nom_theme_trad") or {}
        if sorted(tt) != sorted(LANGUES) or not all(tt.values()):
            echecs.append("%s : nom_theme_trad sans ses 9 langues" % nom)
        for ligne in src.MOTS:
            d = en_dict(ligne)
            mot, sorte, niv = d.get("mot", ""), d.get("sorte", "nom"), d.get("niveau")
            ou = "%s_%s / %s" % (base, str(niv).lower(), mot)
            if niv not in NIVEAUX:
                echecs.append("%s : niveau %r" % (ou, niv))
            if sorte not in SORTES:
                echecs.append("%s : sorte %r" % (ou, sorte))
            if sorte == "nom":
                if d.get("genre") not in ("der", "die", "das"):
                    echecs.append("%s : genre %r" % (ou, d.get("genre")))
                if not d.get("pluriel"):
                    echecs.append("%s : pluriel vide" % ou)
                if "article_fr" not in d:
                    echecs.append("%s : article_fr absent" % ou)
            if sorte == "verbe" and not d.get("perfekt"):
                echecs.append("%s : verbe sans perfekt" % ou)
            trad = d.get("trad") or {}
            for l in LANGUES:
                t = trad.get(l)
                if not t or len(t) != 2 or not t[0] or not t[1]:
                    echecs.append("%s : traduction ou exemple %s vide" % (ou, l))
                    continue
                ecritures(echecs, ou, l, "traduction", t[0])
                ecritures(echecs, ou, l, "exemple", t[1])
            ecritures(echecs, ou, "de", "exemple", d.get("exemple", ""))
            if trad.get("es"):
                avec_es += 1
                t = trad["es"]
                if len(t) != 2 or not t[0] or not t[1]:
                    echecs.append("%s : traduction ou exemple es vide" % ou)
                else:
                    ecritures(echecs, ou, "es", "traduction", t[0])
                    ecritures(echecs, ou, "es", "exemple", t[1])
                if sorte == "paire" and not (d.get("trad_patient") or {}).get("es"):
                    echecs.append("%s : l'espagnol d'un cote de la paire seulement" % ou)
            if d.get("chapitre") and d["chapitre"] not in ids_chapitres:
                echecs.append("%s : chapitre inconnu %r" % (ou, d["chapitre"]))
            if sorte == "paire":
                # le cote du patient : memes exigences que le cote du service
                if not d.get("patient") or not d.get("exemple_patient"):
                    echecs.append("%s : paire sans « patient » ou « exemple_patient »" % ou)
                tp = d.get("trad_patient") or {}
                for l in LANGUES + (["es"] if tp.get("es") else []):
                    t = tp.get(l)
                    if not t or len(t) != 2 or not t[0] or not t[1]:
                        echecs.append("%s : traduction ou exemple du patient %s vide" % (ou, l))
                        continue
                    ecritures(echecs, ou, l, "traduction du patient", t[0])
                    ecritures(echecs, ou, l, "exemple du patient", t[1])
                ecritures(echecs, ou, "de", "exemple du patient", d.get("exemple_patient", ""))
                if re.search(r"\d", d.get("exemple_patient", "")) and not d.get("lecture_patient"):
                    echecs.append("%s : chiffre dans l'exemple du patient sans « lecture_patient »" % ou)
                if re.search(r"\d", d.get("patient", "")) and not d.get("lecture_mot_patient"):
                    echecs.append("%s : chiffre dans le mot du patient sans « lecture_mot_patient »" % ou)
                if corpus.cle(d.get("patient", "")) == corpus.cle(mot):
                    echecs.append("%s : les deux cotes de la paire sont le meme mot" % ou)
            if not d.get("exemple"):
                echecs.append("%s : exemple allemand vide" % ou)
            # chiffres
            if re.search(r"\d", d.get("exemple", "")) and not d.get("lecture"):
                echecs.append("%s : chiffre dans l'exemple sans « lecture »" % ou)
            if re.search(r"\d", mot) and not (d.get("lecture_mot") or d.get("lecture")):
                echecs.append("%s : chiffre dans le mot sans « lecture_mot »" % ou)
            for k in ("lecture", "lecture_mot", "lecture_patient", "lecture_mot_patient"):
                if d.get(k) and re.search(r"\d", d[k]):
                    echecs.append("%s : %s encore chiffree : %s" % (ou, k, d[k]))
            # doublons dans les Soins
            cl = (corpus.cle(mot, garder_sich=True), CLASSE_SORTE.get(sorte))
            if sorte == "paire":  # une paire est un LIEN : deux paires peuvent partager un cote, pas les deux
                cl = (corpus.cle(mot, garder_sich=True) + " | " + corpus.cle(d.get("patient", ""), garder_sich=True), "paire")
            if cl in vus:
                echecs.append("%s : deux fois dans les Soins (deja dans %s)" % (ou, vus[cl]))
            vus[cl] = base
            # doublons avec le corpus general
            # une paire relie deux registres, souvent deja au corpus chacun : pas de controle de doublon
            hits = [] if sorte == "paire" else [h for h in corpus.chercher(mot) if CLASSE.get(h["type"]) == CLASSE_SORTE.get(sorte)]
            if d.get("corpus"):
                if not hits:
                    echecs.append("%s : marque corpus, mais absent du corpus general" % ou)
            elif hits and not d.get("sens_distinct"):
                echecs.append("%s : deja au corpus (%s %s, « %s ») : reprise (corpus: True) ou sens_distinct"
                              % (ou, hits[0]["fichier"], hits[0]["ou"], hits[0]["traduction"]))
            elif d.get("sens_distinct") and not hits:
                echecs.append("%s : sens_distinct, mais le mot n'est pas au corpus" % ou)
            if d.get("relire"):
                a_relire.append("%s · %s" % (ou, d["relire"]))
            c = comptes.setdefault(nom, {}).setdefault(niv, [0, 0])
            c[0] += 1
            c[1] += 1 if d.get("corpus") else 0

    total = sum(c[0] for t in comptes.values() for c in t.values())
    repris = sum(c[1] for t in comptes.values() for c in t.values())
    print("Vocabulaire des Soins : %d entrees, dont %d reprises du corpus ; %d a relire ; %d avec l'espagnol"
          % (total, repris, len(a_relire), avec_es))
    for nom in C.THEMES:
        ligne = "  %-14s" % nom
        for niv in ("A2", "B1", "B2"):
            c = comptes.get(nom, {}).get(niv, [0, 0])
            ligne += "  %s %3d (%2d repr.)" % (niv, c[0], c[1])
        print(ligne)
    par = {n: sum(t.get(n, [0, 0])[0] for t in comptes.values()) for n in ("A2", "B1", "B2")}
    print("  total           A2 %d · B1 %d · B2 %d" % (par["A2"], par["B1"], par["B2"]))
    if detail:
        print("A relire (%d) :" % len(a_relire))
        for x in a_relire:
            print("   " + x)
    for a in avert:
        print("  avertissement : " + a)
    if echecs:
        for e in echecs[:200]:
            print("ECHEC : " + e)
        print("%d echec(s)" % len(echecs))
        return 1
    print("aucun probleme")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
