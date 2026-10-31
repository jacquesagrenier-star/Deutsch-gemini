# -*- coding: utf-8 -*-
"""Remplit la table `lexique` d'une scene japonaise depuis le corpus N5-N3.

    python japonais/scenes/lexique.py kuukou heya ...

Pour chaque mot de visuel/prototype/<nom>.points.json (champ `mot` et
`aussi` de chaque zone) : lecture, traduction francaise, id JMdict et niveau,
pris dans origin/japonais-cartes:japonais/cartes/mots-n5|n4|n3.json. Un mot
absent du corpus prend sa lecture et sa traduction dans `hors_corpus` de
japonais/scenes/mots-prevus.json (niveau « hors N5-N3 »). Quand le corpus N3
n'a pas de glose francaise, la traduction vient de `gloses_manuelles`
ci-dessous (fr_source « manuel »), comme pour les prototypes du 12 oct.

Un mot qu'on ne trouve nulle part arrete le script : on ne publie pas une
etiquette sans lecture. Brouillon : le japonais attend un natif.
"""
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))
PROTO = os.path.join(RACINE, "visuel", "prototype")

# Gloses francaises des mots N3 que le corpus n'a pas encore traduits
# (memes choix que les prototypes du 12 oct. quand le mot y etait).
GLOSES_MANUELLES = {
    "床": "sol ; plancher", "袋": "sac (en plastique, en papier)", "瓶": "bouteille",
    "かご": "panier", "ジュース": "jus (de fruits)", "広告": "publicité ; affiche",
    "ベンチ": "banc", "ホーム": "quai", "乗客": "passager ; voyageur",
    "列車": "train", "屋根": "toit", "植物": "plante", "居間": "salon ; pièce à vivre",
    "毛布": "couverture", "鍋": "casserole ; marmite", "皿": "assiette ; plat",
    "ビール": "bière", "桜": "cerisier ; fleur de cerisier", "パスポート": "passeport",
    "書類": "documents ; papiers officiels", "機械": "machine", "券": "ticket ; billet",
    "タオル": "serviette", "酒": "alcool ; saké", "グラス": "verre (à pied)",
    "カード": "carte", "弁当": "repas en boîte (bento)", "スープ": "soupe",
    "ソファー": "canapé", "硬貨": "pièce de monnaie", "列": "file ; rang",
    "波": "vague", "岩": "rocher", "松": "pin", "墓": "tombe", "帯": "ceinture (de kimono)",
    "肩": "épaule", "氷": "glace (eau gelée)", "布": "tissu", "包み": "paquet",
    "土産": "souvenir (cadeau)", "アルバム": "album", "黒板": "tableau noir",
    "茶": "thé", "灰": "cendre", "スイッチ": "interrupteur", "信号": "feu (de circulation)",
    "塀": "mur de clôture", "座席": "siège ; place assise", "両替": "change (de monnaie)",
}


def corpus():
    index = {}
    for n in ("5", "4", "3"):
        brut = subprocess.run(
            ["git", "show", "origin/japonais-cartes:japonais/cartes/mots-n%s.json" % n],
            cwd=RACINE, capture_output=True, check=True).stdout.decode("utf-8")
        for e in json.loads(brut)["entrees"]:
            for k in ("kanji", "kana"):
                v = (e["ecritures"].get(k) or {}).get("v")
                if v:
                    index.setdefault(v, e)
    return index


def main():
    idx = corpus()
    prevus = json.load(open(os.path.join(ICI, "mots-prevus.json"), encoding="utf-8"))
    hors = {}
    for k, s in prevus.items():
        if not k.startswith("_"):
            hors.update(s.get("hors_corpus", {}))
    for nom in sys.argv[1:]:
        chemin = os.path.join(PROTO, nom + ".points.json")
        d = json.load(open(chemin, encoding="utf-8"))
        mots = []
        for p in d["points"]:
            for m in [p["mot"]] + p.get("aussi", []):
                if m not in mots:
                    mots.append(m)
        lex = {}
        for m in mots:
            if m in idx:
                e = idx[m]
                fr = ((e["gloses"].get("fr") or {}).get("affichee") or {}).get("v") or ""
                x = {"jmdict": e["id"], "niveau": e["niveau"], "mot": m,
                     "kana": e["ecritures"]["kana"]["v"], "fr": fr}
                if not fr:
                    if m not in GLOSES_MANUELLES:
                        sys.exit("  %s : %s sans glose francaise (GLOSES_MANUELLES)" % (nom, m))
                    x["fr"], x["fr_source"] = GLOSES_MANUELLES[m], "manuel"
            elif m in hors:
                x = {"jmdict": None, "niveau": "hors N5-N3", "mot": m,
                     "kana": hors[m][0], "fr": hors[m][1], "fr_source": "manuel"}
            else:
                sys.exit("  %s : %s introuvable (corpus et hors_corpus)" % (nom, m))
            lex[m] = x
        d["lexique"] = dict(sorted(lex.items(), key=lambda kv: (
            {"N5": 0, "N4": 1, "N3": 2}.get(kv[1]["niveau"], 3), kv[1]["kana"])))
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_hors = sum(1 for v in lex.values() if v["niveau"] == "hors N5-N3")
        print("  %-12s %2d zones, %2d mots (%d hors corpus)" % (nom, len(d["points"]), len(lex), n_hors))


if __name__ == "__main__":
    main()
