# -*- coding: utf-8 -*-
"""Controle mecanique des cles d'interface d'une langue. Aucun service externe.

    python tests/controle_i18n.py --langue fa

ETAPE 1 DE LA RELECTURE, celle qui ne demande l'avis de personne. Elle ne juge
pas la qualite d'une traduction -- elle attrape ce qui n'en est pas une.

LA LECON DU TURC : le 2 septembre 2026, 673 entrees portaient UN SEUL caractere
en guise de traduction. Le champ existait, n'etait pas vide, et tous les
compteurs annoncaient « fait ». Ce qui les a vues n'est pas DeepL mais un
controle de plausibilite local. Celui-ci fait la meme chose pour l'interface.

CE QU'IL VERIFIE
  1. Les GABARITS sont conserves : {n}, {mot}, {pct}... Un gabarit perdu
     affiche « {n} » en clair ou, pire, un texte ampute sans rien dire.
  2. Les BALISES sont conservees : <strong>, <br>, <td ...>. Une balise
     ouverte non refermee deforme tout l'ecran, pas seulement sa ligne.
  3. La chaine est bien DANS L'ECRITURE de la langue -- pour le persan,
     l'alphabet arabo-persan. Attrape le francais laisse en place, qu'aucun
     compteur ne distingue d'une traduction.
  4. ⚠️ PERSAN : les sosies ARABES. « ي » (U+064A) et « ك » (U+0643) au lieu
     de « ی » (U+06CC) et « ک » (U+06A9). Invisible a l'oeil dans la plupart
     des polices, mais ce sont d'AUTRES caracteres : la recherche ne trouve
     plus le mot, et le rendu casse sur certains appareils. C'est le defaut
     le plus courant d'un texte persan copie depuis une source arabe.
  5. La longueur est plausible par rapport au francais.
"""
import argparse, json, os, re, subprocess, sys, unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ecritures attendues, par langue. (nom, intervalle Unicode)
ECRITURES = {
    "fa": ("arabo-persane", (0x0600, 0x06FF)),
    "ar": ("arabe",         (0x0600, 0x06FF)),
    "uk": ("cyrillique",    (0x0400, 0x04FF)),
}
# Caracteres arabes a ne PAS employer en persan -> leur equivalent persan.
SOSIES_ARABES = {"\u064a": "\u06cc (ی)", "\u0643": "\u06a9 (ک)",
                 "\u0629": "\u0647 (ه)", "\u0649": "\u06cc (ی)"}

GABARIT = re.compile(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}")
BALISE  = re.compile(r"<[^>]+>")

def dump():
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js")],
                       capture_output=True, cwd=RACINE)
    if r.returncode:
        sys.exit("node n'a pas pu evaluer I18N :\n" + r.stderr.decode("utf-8", "replace")[:600])
    return json.loads(r.stdout.decode("utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--montrer", type=int, default=12)
    a = ap.parse_args()

    d = dump()
    fr, cible = d.get("fr", {}), d.get(a.langue, {})
    if not cible: sys.exit("aucune cle en %s" % a.langue)

    ecriture = ECRITURES.get(a.langue)
    pb = {"gabarits": [], "balises": [], "ecriture": [], "sosies": [], "longueur": [], "identique": []}

    # ⚠️ CE QUE PERSONNE NE TRADUIT N'EST PAS UN OUBLI. « Verben »,
    # « Adjektive », « Phrasal verbs », les phrases-exemples allemandes :
    # elles restent telles quelles dans TOUTES les langues. Le signal, c'est
    # que le francais et l'anglais portent DEJA la meme chaine -- pas besoin
    # d'une liste d'exceptions a tenir a jour. Sans cette regle l'outil sortait
    # 55 faux positifs sur l'ukrainien, et un outil bruyant ne sert personne.
    intraduits = {k for k, v in fr.items() if d.get("en", {}).get(k) == v}

    for k, v in cible.items():
        src = fr.get(k)
        if k in intraduits: continue
        if src is None:
            pb["gabarits"].append((k, "cle absente du francais", v)); continue
        if set(GABARIT.findall(src)) != set(GABARIT.findall(v)):
            pb["gabarits"].append((k, " ".join(sorted(set(GABARIT.findall(src)))), v))
        if [b.split()[0].rstrip(">") for b in BALISE.findall(src)] != \
           [b.split()[0].rstrip(">") for b in BALISE.findall(v)]:
            pb["balises"].append((k, src[:60], v[:60]))
        # Une chaine faite QUE de symboles, chiffres ou noms propres latins est
        # legitime (« GB / US », « flat · apartment ») : on n'exige l'ecriture
        # que si le francais, lui, portait des lettres.
        if ecriture and re.search(r"[A-Za-zÀ-ÿ]{3}", src):
            lo, hi = ecriture[1]
            if not any(lo <= ord(c) <= hi for c in v):
                pb["ecriture"].append((k, ecriture[0], v[:60]))
        if a.langue == "fa":
            trouves = sorted({SOSIES_ARABES[c] for c in v if c in SOSIES_ARABES})
            if trouves: pb["sosies"].append((k, " ".join(trouves), v[:60]))
        if len(src) >= 12 and (len(v) < len(src) * 0.35 or len(v) > len(src) * 2.6):
            pb["longueur"].append((k, "fr %d / %s %d" % (len(src), a.langue, len(v)), v[:50]))
        if v.strip() and v.strip() == src.strip() and re.search(r"[A-Za-zÀ-ÿ]{4}", src):
            pb["identique"].append((k, "identique au francais", v[:60]))

    total = sum(len(x) for x in pb.values())
    print("%s : %d cles sur %d\n" % (a.langue, len(cible), len(fr)))
    ETIQ = {"gabarits": "GABARITS perdus ou ajoutes", "balises": "BALISES qui ne correspondent pas",
            "ecriture": "PAS DANS L'ECRITURE attendue", "sosies": "SOSIES ARABES au lieu des lettres persanes",
            "longueur": "LONGUEUR invraisemblable", "identique": "IDENTIQUE au francais (non traduit ?)"}
    for cle, lignes in pb.items():
        print("  %-42s %d" % (ETIQ[cle], len(lignes)))
    for cle, lignes in pb.items():
        if not lignes: continue
        print("\n== %s ==" % ETIQ[cle])
        for k, info, v in lignes[:a.montrer]:
            print("  %-34s %s\n      %s" % (k, info, v))
        if len(lignes) > a.montrer: print("  ... et %d autres" % (len(lignes) - a.montrer))
    print("\n%s" % ("AUCUN PROBLEME MECANIQUE." if total == 0 else "%d POINTS A REGARDER." % total))
    sys.exit(1 if total else 0)

if __name__ == "__main__":
    main()
