"""Relecture croisée des phrases japonaises par plusieurs IA, à l'aveugle.

Chaque IA (GPT, Gemini, Claude…) reçoit les mêmes lots, sans jamais voir le
verdict d'une autre. On ne compare qu'à la fin. La leçon du 4 oct. 2026 : un
relecteur qui voit les réponses ne contrôle plus rien.

  python japonais/cartes/outils/relecture_croisee.py preparer
      -> relecture/lot-NN.md (à coller dans le chat) + relecture/cle.json

  python japonais/cartes/outils/relecture_croisee.py importer gpt REPONSE.txt
      -> relecture/reponses/gpt.json (cumulé, lot après lot)
      Signale les codes manquants ou en double : il faut alors redemander.

  python japonais/cartes/outils/relecture_croisee.py comparer
      -> relecture/pour-le-natif.md : tout désaccord, tout verdict autre que
         NATUREL + OUI, et un échantillon au hasard des phrases que tous
         jugent bonnes (c'est lui qui mesure si l'on peut croire les IA).

Les phrases viennent de japonais/cartes/phrases-n*.json (session cloud).
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

CARTES = Path(__file__).resolve().parents[1]
DOSSIER = CARTES / "relecture"
CLE = DOSSIER / "cle.json"
REPONSES = DOSSIER / "reponses"
TAILLE_LOT = 300
PART_ECHANTILLON = 0.10
GRAINE = 20261008

JAPONAIS = ["NATUREL", "RAIDE", "DOUTEUX", "FAUTIF"]
TRADUCTION = ["OUI", "APPROX", "NON"]

CONSIGNE = """Tu es un relecteur de japonais langue maternelle. Ces phrases serviront d'exemples sur des cartes de vocabulaire pour des francophones débutants (niveaux JLPT N5 à N3). Pour CHAQUE ligne, donne deux jugements :

1. Le japonais :
   NATUREL = un Japonais l'écrirait ou le dirait ainsi
   RAIDE   = correct, mais un Japonais le dirait autrement (tournure scolaire, datée, maladroite)
   DOUTEUX = tu hésites sur la grammaire, une particule, le registre
   FAUTIF  = faute de grammaire, de particule, de conjugaison ou de mot
2. La traduction française :
   OUI    = elle dit la même chose que le japonais
   APPROX = sens proche, mais une nuance est perdue ou ajoutée
   NON    = contresens, ou elle traduit autre chose

Réponds UNIQUEMENT par des lignes de cette forme, une par phrase, dans l'ordre, sans en sauter aucune :
CODE | JAPONAIS | TRADUCTION | remarque
La remarque est vide si NATUREL et OUI. Sinon, une phrase courte en français qui dit ce qui ne va pas et, si possible, la correction.
Si tu dois t'arrêter avant la fin, écris en dernière ligne : ARRÊT APRÈS CODE.

"""


def charger_phrases():
    phrases = []
    for f in sorted(CARTES.glob("phrases-n*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for e in d.get("entrees", d if isinstance(d, list) else []):
            ja = e.get("japonais") or (e.get("texte") or {}).get("ja")
            fr = e.get("francais") or (e.get("texte") or {}).get("fr")
            ja = ja.get("v") if isinstance(ja, dict) else ja
            fr = fr.get("v") if isinstance(fr, dict) else fr
            if not (e.get("id") and ja and fr):
                sys.exit(f"{f.name} : entrée illisible {json.dumps(e, ensure_ascii=False)[:200]}")
            phrases.append({"id": e["id"], "niveau": e.get("niveau"), "ja": ja, "fr": fr})
    if not phrases:
        sys.exit(f"Aucune phrase dans {CARTES}/phrases-n*.json")
    return phrases


def preparer(_):
    phrases = charger_phrases()
    vus = set()
    phrases = [p for p in phrases if not (p["id"] in vus or vus.add(p["id"]))]
    DOSSIER.mkdir(exist_ok=True)
    cle = {}
    for n, debut in enumerate(range(0, len(phrases), TAILLE_LOT), 1):
        lignes = []
        for i, p in enumerate(phrases[debut:debut + TAILLE_LOT], debut + 1):
            code = f"P{i:04d}"
            cle[code] = {**p, "lot": n}
            lignes.append(f"{code} | {p['ja']} | {p['fr']}")
        corps = CONSIGNE + f"Lot {n} : {len(lignes)} phrases, de {lignes[0][:5]} à {lignes[-1][:5]}.\n\n" + "\n".join(lignes) + "\n"
        (DOSSIER / f"lot-{n:02d}.md").write_text(corps, encoding="utf-8")
    CLE.write_text(json.dumps(cle, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(phrases)} phrases, {n} lots dans {DOSSIER}")


LIGNE = re.compile(r"^\W*(P\d{4})\s*\|\s*([A-ZÉ]+)\s*\|\s*([A-Z]+)\s*(?:\|\s*(.*))?$")


def importer(a):
    cle = json.loads(CLE.read_text(encoding="utf-8"))
    REPONSES.mkdir(parents=True, exist_ok=True)
    fichier = REPONSES / f"{a.modele}.json"
    deja = json.loads(fichier.read_text(encoding="utf-8")) if fichier.exists() else {}
    texte = Path(a.reponse).read_text(encoding="utf-8")
    lus, refus, doubles = {}, [], []
    for ligne in texte.splitlines():
        m = LIGNE.match(ligne.strip().replace("｜", "|"))
        if not m:
            continue
        code, ja, tr, rem = m.groups()
        if code not in cle or ja not in JAPONAIS or tr not in TRADUCTION:
            refus.append(ligne.strip())
            continue
        if code in lus:
            doubles.append(code)
        lus[code] = {"japonais": ja, "traduction": tr, "remarque": (rem or "").strip()}
    lots = {cle[c]["lot"] for c in lus}
    attendus = {c for c, v in cle.items() if v["lot"] in lots}
    manquants = sorted(attendus - set(lus))
    deja.update(lus)
    fichier.write_text(json.dumps(deja, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{a.modele} : {len(lus)} verdicts lus (lots {sorted(lots)}), {len(deja)} au total")
    for nom, liste in (("MANQUANTS, à redemander", manquants), ("en double", doubles), ("illisibles", refus)):
        if liste:
            print(f"  {len(liste)} {nom} : {', '.join(liste[:15])}{' …' if len(liste) > 15 else ''}")


def bon(v):
    return v["japonais"] == "NATUREL" and v["traduction"] == "OUI"


def comparer(_):
    cle = json.loads(CLE.read_text(encoding="utf-8"))
    juges = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(REPONSES.glob("*.json"))}
    if len(juges) < 2:
        sys.exit(f"Il faut au moins deux relecteurs dans {REPONSES} (trouvés : {list(juges)})")
    complets = [c for c in cle if all(c in j for j in juges.values())]
    a_voir, unanimes = [], []
    for c in complets:
        avis = {n: j[c] for n, j in juges.items()}
        (unanimes if all(bon(v) for v in avis.values()) else a_voir).append(c)
    echantillon = sorted(random.Random(GRAINE).sample(unanimes, round(len(unanimes) * PART_ECHANTILLON)))

    def ligne(c):
        p = cle[c]
        avis = "; ".join(f"{n} {j[c]['japonais']}/{j[c]['traduction']}" + (f" ({j[c]['remarque']})" if j[c]["remarque"] else "")
                         for n, j in juges.items())
        return "| " + " | ".join(t.replace("|", "/") for t in (c, p["ja"], p["fr"], avis)) + " |"

    tete = "| Code | Japonais | Français | Avis des IA |\n|---|---|---|---|"
    accord = {}
    for c in a_voir:
        cles_avis = {(j[c]["japonais"], j[c]["traduction"]) for j in juges.values()}
        accord["toutes d'accord" if len(cles_avis) == 1 else "désaccord"] = accord.get("toutes d'accord" if len(cles_avis) == 1 else "désaccord", 0) + 1
    md = [
        "# Phrases japonaises à faire relire par un natif",
        "",
        f"Relecteurs automatiques : {', '.join(juges)}. Phrases jugées par tous : {len(complets)} sur {len(cle)}.",
        f"Toutes les IA disent NATUREL + OUI : {len(unanimes)}. Au moins une réserve : {len(a_voir)} ({', '.join(f'{k} : {v}' for k, v in accord.items())}).",
        "",
        f"## 1. Échantillon de contrôle : {len(echantillon)} phrases que toutes les IA jugent bonnes",
        "",
        "Tiré au hasard. **Ce que le natif en dit mesure la confiance qu'on peut accorder aux IA** : s'il y trouve des fautes, les phrases « unanimes » ne sont pas sûres non plus.",
        "",
        tete, *map(ligne, echantillon),
        "",
        f"## 2. Les {len(a_voir)} phrases avec au moins une réserve",
        "",
        tete, *map(ligne, a_voir),
    ]
    sortie = DOSSIER / "pour-le-natif.md"
    sortie.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{sortie} : {len(echantillon)} en échantillon + {len(a_voir)} avec réserve, sur {len(complets)} jugées par tous")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("preparer").set_defaults(f=preparer)
    i = s.add_parser("importer")
    i.add_argument("modele", help="gpt, gemini, claude…")
    i.add_argument("reponse", help="fichier texte où l'on a collé la réponse")
    i.set_defaults(f=importer)
    s.add_parser("comparer").set_defaults(f=comparer)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
