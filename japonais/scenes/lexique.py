# -*- coding: utf-8 -*-
"""Remplit la table `lexique` d'une scene japonaise depuis le corpus.

    python japonais/scenes/lexique.py kuukou heya ...

Pour chaque mot de visuel/prototype/<nom>.points.json (champ `mot` et
`aussi` de chaque zone) : lecture, traduction francaise, id JMdict et niveau,
pris dans japonais/cartes/mots-n5..n1.json de cette branche, puis dans
japonais/cartes/scenes.json (les mots des scenes hors listes JLPT, niveau
« hors JLPT », 1er nov. 2026). Un mot absent des deux prend sa lecture et sa
traduction dans `hors_corpus` de japonais/scenes/mots-prevus.json (niveau
« hors corpus »). Quand la fiche n'a pas de glose francaise (le N2 et le N1
n'en ont pas encore), la traduction vient de `gloses_manuelles` ci-dessous
(fr_source « manuel »), comme pour les prototypes du 12 oct.

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
    "煙": "fumée", "舌": "langue (organe)",
    "塀": "mur de clôture", "座席": "siège ; place assise", "両替": "change (de monnaie)",
    # N2 et N1 (1er nov. 2026) : dans le corpus, pas encore traduits en francais.
    "盆": "plateau",
    "丼": "grand bol",
    "櫛": "peigne",
    "窓口": "guichet", "扇風機": "ventilateur", "ロッカー": "casier", "垣根": "clôture ; haie", "チョーク": "craie",
    "秤": "balance", "エプロン": "tablier", "面接": "entretien d'embauche", "鈴": "clochette", "ストロー": "paille",
    "新幹線": "shinkansen (train à grande vitesse)", "座布団": "coussin de sol", "縁側": "véranda (engawa)",
    "ろうそく": "bougie", "包丁": "couteau de cuisine", "流し": "évier", "墓地": "cimetière",
    "浴衣": "kimono d'été (yukata)", "金魚": "poisson rouge", "太鼓": "tambour", "うちわ": "éventail rond",
    "花火": "feu d'artifice", "貝": "coquillage", "バケツ": "seau", "鳥居": "portique de sanctuaire (torii)",
    "杖": "canne", "杉": "cèdre du Japon", "紅葉": "érable rouge", "床の間": "alcôve (tokonoma)",
    "障子": "cloison de papier (shōji)", "竹": "bambou", "滝": "cascade", "薬局": "pharmacie", "マスク": "masque",
    "マフラー": "écharpe", "包帯": "bandage", "リボン": "ruban", "制服": "uniforme", "校庭": "cour d'école",
    "鉄棒": "barre fixe", "こたつ": "table chauffante (kotatsu)", "ブーツ": "bottes",
}


def corpus():
    """Le corpus N5-N1 de cette branche (japonais/cartes/mots-n*.json), par
    forme ECRITE : le kanji quand la fiche en a un, sinon le kana. Jusqu'au
    1er nov. 2026 on lisait le seul N5-N3 de origin/japonais-cartes, et un mot
    se trouvait aussi par sa lecture : 銭湯 tombait sur 戦闘 (« combat »), 線香
    sur 専攻, 炭 sur 隅. Une lecture ne dit pas quel mot c'est."""
    index = {}
    for n in ("5", "4", "3", "2", "1"):
        chemin = os.path.join(RACINE, "japonais", "cartes", "mots-n%s.json" % n)
        for e in json.load(open(chemin, encoding="utf-8"))["entrees"]:
            ec = e["ecritures"]
            v = (ec.get("kanji") or {}).get("v") or ec["kana"]["v"]
            index.setdefault(v, e)
    # Les mots des scenes hors listes JLPT (japonais/cartes/scenes.json, 1er nov.
    # 2026), au format d'une fiche pour ce qu'on en lit ici.
    chemin = os.path.join(RACINE, "japonais", "cartes", "scenes.json")
    for a in json.load(open(chemin, encoding="utf-8"))["mots"]:
        index.setdefault(a["mot"], {
            "id": a["id"], "niveau": "hors JLPT", "jlpt_estime": a["jlpt"],
            "ecritures": {"kana": {"v": a["lecture"]}},
            "gloses": {"fr": {"affichee": {"v": a["fr"]}}}})
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
                x = {"jmdict": None, "niveau": "hors corpus", "mot": m,
                     "kana": hors[m][0], "fr": hors[m][1], "fr_source": "manuel"}
            else:
                sys.exit("  %s : %s introuvable (corpus et hors_corpus)" % (nom, m))
            lex[m] = x
        d["lexique"] = dict(sorted(lex.items(), key=lambda kv: (
            {"N5": 0, "N4": 1, "N3": 2, "N2": 3, "N1": 4, "hors JLPT": 5}.get(kv[1]["niveau"], 6), kv[1]["kana"])))
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_hors = sum(1 for v in lex.values() if v["niveau"] == "hors corpus")
        print("  %-12s %2d zones, %2d mots (%d hors corpus)" % (nom, len(d["points"]), len(lex), n_hors))


if __name__ == "__main__":
    main()
