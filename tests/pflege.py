"""Controle des donnees de la section Soins (Wortando Pflege) : python tests/pflege.py

Ce qu'il refuse (ECHEC) :
  - pflege/datos/themes.json qui n'est pas la sortie de pflege/outils/construire.py (fichier derive) ;
  - un id sans le prefixe « soins_ » (« pflege_ » est pris par le corpus : pflege_betreuung_c1) ou sans son niveau (« _a2 » ... « _c1 ») ;
  - un mot sans genre der / die / das, sans pluriel, sans traduction ou sans exemple dans l'une des
    9 langues d'interface de l'allemand ;
  - un chiffre dans une phrase d'exemple allemande (la voix demanderait une lecture ecrite a la main) ;
  - un meme mot deux fois dans les Soins.
Ce qu'il signale (AVERTISSEMENT, sans echec) : un mot deja present dans le corpus general (themes.json),
que la phase 2 reliera a sa fiche au lieu de le doubler.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
DATOS = RACINE / "pflege" / "datos" / "themes.json"
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]


def main():
    problemes, avis = [], []
    r = subprocess.run([sys.executable, str(RACINE / "pflege" / "outils" / "construire.py"), "--verifier"],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        problemes.append((r.stdout or r.stderr).strip())
    if not DATOS.exists():
        print("ECHEC : pflege/datos/themes.json absent")
        return 1
    donnees = json.loads(DATOS.read_text(encoding="utf-8"))
    corpus = set()
    brut = json.loads((RACINE / "themes.json").read_text(encoding="utf-8"))
    for th in (brut if isinstance(brut, list) else brut.get("themes", [])):
        for m in th.get("mots", []):
            corpus.add((m.get("genre"), m.get("mot")))
    vus = set()
    total = 0
    for th in donnees.get("themes", []):
        tid = th.get("id", "")
        if not re.fullmatch(r"soins_[a-z0-9_]+_(a2|b1|b2|c1)", tid):
            problemes.append("id refuse : %r" % tid)
        if tid.split("_")[-1].upper() != th.get("niveau"):
            problemes.append("%s : niveau %r different de l'id" % (tid, th.get("niveau")))
        for m in th.get("mots", []):
            total += 1
            ou = "%s / %s" % (tid, m.get("mot"))
            sorte = m.get("sorte", "nom")
            if sorte not in ("nom", "verbe", "adjectif", "expression"):
                problemes.append(ou + " : sorte %r" % sorte)
            if sorte == "nom":
                if m.get("genre") not in ("der", "die", "das"):
                    problemes.append(ou + " : genre %r" % m.get("genre"))
                if not m.get("pluriel"):
                    problemes.append(ou + " : pluriel vide (« — » si aucun)")
            elif m.get("genre"):
                problemes.append(ou + " : un genre sur un(e) %s" % sorte)
            if sorte == "verbe" and not m.get("perfekt"):
                problemes.append(ou + " : verbe sans perfekt (« hat gemessen »)")
            if not m.get("exemple"):
                problemes.append(ou + " : exemple allemand vide")
            elif re.search(r"\d", m["exemple"]) and not m.get("lecture"):
                problemes.append(ou + " : chiffre dans l'exemple sans « lecture » (« %s »)" % m["exemple"])
            if re.search(r"\d", m.get("mot", "")) and not m.get("lecture"):
                problemes.append(ou + " : chiffre dans le mot sans « lecture »")
            for l in LANGUES:
                tr = m.get("traduction" if l == "fr" else "traduction_" + l)
                ex = m.get("exemple_" + l)
                if not tr or not ex:
                    problemes.append(ou + " : traduction ou exemple %s vide" % l)
            cle = (m.get("genre"), m.get("mot"))
            if cle in vus:
                problemes.append(ou + " : deux fois dans les Soins")
            vus.add(cle)
            if cle in corpus:
                avis.append(ou + " : deja au corpus general (a relier en phase 2)")
    for a in avis:
        print("AVERTISSEMENT :", a)
    for p in problemes:
        print("PROBLEME :", p)
    if problemes:
        print("ECHEC : %d probleme(s), %d mots" % (len(problemes), total))
        return 1
    print("OK : %d themes-niveaux, %d mots de soins, 9 langues" % (len(donnees.get("themes", [])), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
