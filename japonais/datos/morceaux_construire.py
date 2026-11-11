# -*- coding: utf-8 -*-
"""Decoupe les phrases d'exemple japonaises en MORCEAUX : japonais/datos/morceaux.json.

    python japonais/datos/morceaux_construire.py

POURQUOI (lot J4, decision de Jacques du 11 nov. 2026). Dans Ecrire,
Construire la phrase et les dictees, l'apprenant du japonais CHOISIT DES
MORCEAUX au lieu de taper au clavier japonais. Le moteur coupe les autres
langues a leurs espaces ; le japonais n'en a pas : le decoupage vient d'ici.

Deux decoupages par phrase :
  - « b » (bunsetsu) : un mot plein et ce qui s'y accroche (particule, copule,
    terminaison) -- 私は / 日本語を / 勉強します. Pour Construire la phrase ;
  - « m » (mots) : chaque mot a part, particules comprises -- 私 / は / 日本語 /
    を / 勉強します. Pour Ecrire, plus fin donc plus exigeant.

SOURCE : les index de Tatoeba (jpn_indices.csv, CC BY 2.0 FR), qui donnent
le decoupage mot par mot des phrases japonaises du corpus de Tanaka -- nos
phrases d'exemple viennent de Tatoeba et portent leur numero
(exemple_source.tatoeba.jpn). L'index saute parfois un morceau (un nombre, un
nom propre) : on recale chaque mot sur le texte, et ce qui reste entre deux
mots devient un morceau. Une phrase dont le recalage echoue est laissee de
cote : mieux vaut pas d'exercice qu'un exercice faux.

Archive locale (hors depot) :
  C:/Users/jacqu/.wortando/japonais-phrases/japonais/phrases/brut/jpn_indices.csv
"""
import io
import json
import os
import re
import sys
from collections import OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
INDICES = os.path.expanduser("~/.wortando/japonais-phrases/japonais/phrases/brut/jpn_indices.csv")
FICHIERS = ["themes", "verbes", "adjectifs", "adverbes", "expressions", "fonctionnels"]

# Ce qui s'accroche au mot d'avant (un bunsetsu ne commence jamais par eux).
PARTICULES = set("""は が を に へ で と の も や か ね よ な わ さ ぞ ぜ
    から まで より だけ しか ばかり など とか って けど けれど けれども ので のに し ながら たり だり
    ずつ ほど くらい ぐらい ごろ ころ には では とは にも でも へは からは までに として について
    による によって にとって って じゃ なんて なら ば ても でも かな かしら っけ ね え""".split())
AUXILIAIRES = set("""だ です である ます た だ ない ぬ ん れる られる せる させる たい そう よう
    らしい みたい う まい でしょう だろう 御座る ござる じゃ される 為れる させる 為せる""".split())
# Apres une forme en て / で : ces verbes forment une seule unite (降っている).
APRES_TE = set("""いる 居る ある 有る おく 置く しまう 仕舞う くる 来る いく 行く みる 見る
    くれる 呉れる もらう 貰う あげる 上げる 下さい ください 頂く いただく""".split())
SUFFIXES = set("さん ちゃん くん 君 様 さま たち 達 方 がた 屋 中 ちゅう じゅう 的 目".split())
PREFIXES = set("お 御 ご".split())
PONCTUATION = "。、！？!?「」『』（）()・…〜～ 　.,"
CHIFFRES = re.compile(r"^[0-9０-９一二三四五六七八九十百千万〇]+$")


def lire_token(t):
    """« 思う{思って} », « 妻(#1294330)[01] », « 此の{この} » -> (lemme, surface)."""
    t = t.rstrip("~")
    surface = None
    m = re.search(r"\{([^}]*)\}", t)
    if m:
        surface = m.group(1)
    lemme = re.split(r"[\(\[\{|~]", t)[0]
    return lemme, (surface if surface is not None else lemme)


def recaler(phrase, tokens):
    """Les mots de l'index places sur le texte : [(texte, lemme ou None)], ou None."""
    pos, out = 0, []
    for lemme, surf in tokens:
        if not surf:
            continue
        k = phrase.find(surf, pos)
        if k < 0:
            return None
        if k > pos:
            trou = phrase[pos:k]
            out.append((trou, None))
        out.append((surf, lemme))
        pos = k + len(surf)
    if pos < len(phrase):
        out.append((phrase[pos:], None))
    return out


def est_dependant(lemme, texte, precedent):
    if lemme is None:
        return False
    if lemme in PARTICULES or texte in PARTICULES or lemme in AUXILIAIRES or texte in AUXILIAIRES:
        return True
    if lemme in SUFFIXES or texte in SUFFIXES:
        return True
    if precedent and precedent[-1] in "てで" and (lemme in APRES_TE or texte in APRES_TE):
        return True
    return False


def decouper(phrase, tokens):
    """-> (bunsetsu, mots) sans la ponctuation finale, ou None."""
    corps = phrase.strip()
    while corps and corps[-1] in "。！？!?.":
        corps = corps[:-1]
    if any(c in corps for c in "「」『』"):
        return None
    pieces = recaler(corps, tokens)
    if not pieces:
        return None
    # Les mots : chaque piece, la ponctuation interne collee a la precedente.
    mots = []
    for texte, lemme in pieces:
        net = texte.strip(" 　")
        if not net:
            continue
        if all(c in PONCTUATION for c in net) and mots:
            mots[-1] += net
            continue
        mots.append(net)
    # Les bunsetsu.
    b = []
    prefixe = ""
    for texte, lemme in pieces:
        net = texte.strip(" 　")
        if not net:
            continue
        if all(c in PONCTUATION for c in net):
            if b:
                b[-1] += net
            continue
        if lemme in PREFIXES and texte in PREFIXES:
            prefixe += net
            continue
        if b and not prefixe and est_dependant(lemme, net, b[-1]):
            b[-1] += net
            continue
        # Un nombre que l'index a saute colle au compteur qui le suit.
        if b and CHIFFRES.match(b[-1]) and lemme is not None:
            b[-1] += prefixe + net
        else:
            b.append(prefixe + net)
        prefixe = ""
    if prefixe:
        return None
    if "".join(b) != corps.replace(" ", "").replace("　", "") or "".join(mots) != "".join(b):
        return None
    return b, mots


def phrases_du_corpus():
    out = OrderedDict()
    for nom in FICHIERS:
        with io.open(os.path.join(ICI, nom + ".json"), encoding="utf-8") as f:
            d = json.load(f)
        if "themes" in d:
            listes = [m for t in d["themes"] for m in t.get("mots", [])]
        else:
            listes = [m for v in d.values() if isinstance(v, list) for m in v]
        for m in listes:
            j = ((m.get("exemple_source") or {}).get("tatoeba") or {}).get("jpn")
            if j and m.get("exemple"):
                out[str(j)] = m["exemple"]
    return out


def main():
    if not os.path.exists(INDICES):
        sys.exit("Index Tatoeba absent : " + INDICES)
    voulues = phrases_du_corpus()
    sortie, rates = OrderedDict(), 0
    with io.open(INDICES, encoding="utf-8") as f:
        for ligne in f:
            p = ligne.rstrip("\n").split("\t")
            if len(p) < 3 or p[0] not in voulues:
                continue
            phrase = voulues[p[0]]
            if phrase in sortie:
                continue
            r = decouper(phrase, [lire_token(t) for t in p[2].split(" ") if t])
            if not r:
                rates += 1
                continue
            b, mots = r
            if len(mots) >= 2:
                sortie[phrase] = {"b": b, "m": mots}
    chemin = os.path.join(ICI, "morceaux.json")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"_lisez_moi": "Derive de japonais/datos/morceaux_construire.py (index Tatoeba, CC BY 2.0 FR) : "
                                 "ne pas modifier a la main. b = bunsetsu (Construire la phrase), m = mots (Ecrire).",
                   "phrases": sortie}, f, ensure_ascii=False, indent=0)
        f.write("\n")
    print("%d phrases decoupees, %d laissees de cote, %d sans index -> %s"
          % (len(sortie), rates, len(voulues) - len(sortie) - rates, os.path.relpath(chemin)))


if __name__ == "__main__":
    main()
