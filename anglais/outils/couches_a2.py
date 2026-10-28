# -*- coding: utf-8 -*-
"""Brouillon des couches A2 des scenes anglaises (« Where is it? » -- les
prepositions de lieu), tire des FAITS de l'image deja etablis par la couche
A2 allemande (meme zone visee f, meme repere r).

    python anglais/outils/couches_a2.py            (ecrit les brouillons absents)

OUTIL A USAGE UNIQUE (27 oct. 2026). Il ecrit anglais/scenes/<scene>.json, qui
devient la SOURCE : on y corrige les questions a la main ; ce script refuse
d'ecraser un fichier existant. scenes.py fusionne ces couches dans
scene-<scene>.en.js.

Les questions enseignent l'anglais : une sur deux demande le lieu entier
(« Where is the pot? » -> « next to the frying pan »), l'autre la preposition
seule (« The clock is ___ the shelf. » -> above). La note dit la preposition
et son piege pour un francophone. Ce qui ne se traduit pas tout seul est
marque « ?? » et corrige a la main.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import scenes as S
import construire as C
import variante_niveaux as VN

DOSSIER = os.path.join(RACINE, "anglais", "scenes")

PREP = {"neben": "next to", "in": "in", "im": "in", "ins": "in", "unter": "under", "auf": "on",
        "über": "above", "vor": "in front of", "hinter": "behind", "zwischen": "between",
        "an": "on", "am": "on", "bei": "at", "beim": "at", "gegenüber": "across from", "mit": "with"}
# « an » : sur un mur, mais a une table, pres d'une fenetre.
AN_AUTRE = {"Tisch": "at", "Kasse": "at", "Theke": "at", "Schalter": "at", "Rezeption": "at", "Tresen": "at",
            "Fenster": "by", "Tür": "by", "Bett": "by", "Herd": "at", "Spüle": "at", "Strand": "on",
            "Ufer": "on", "Bushaltestelle": "at", "Haltestelle": "at", "Eingang": "at", "Ende": "at"}
NOTES = {
    "next to": "<b>next to</b> = à côté de.",
    "in": "<b>in</b> = dans : à l'intérieur de quelque chose.",
    "under": "<b>under</b> = sous.",
    "on": "<b>on</b> = sur, posé ou accroché (on the table, on the wall).",
    "above": "<b>above</b> = au-dessus de, sans toucher. Posé dessus, ce serait <b>on</b>.",
    "in front of": "<b>in front of</b> = devant. Attention : <b>front</b> seul n'est pas une préposition.",
    "behind": "<b>behind</b> = derrière.",
    "between": "<b>between</b> = entre (deux choses).",
    "at": "<b>at</b> = à, près de, pour un point précis (at the table, at the counter).",
    "by": "<b>by</b> = près de, au bord de (by the window).",
    "across from": "<b>across from</b> = en face de (en américain ; <b>opposite</b> en britannique).",
    "with": "<b>with</b> = avec.",
    "against": "<b>against</b> = contre (appuyé contre le mur).",
    "over": "<b>over</b> = par-dessus, posé en travers (over the chair).",
    "to the right of": "<b>to the right of</b> = à droite de.",
    "to the left of": "<b>to the left of</b> = à gauche de.",
}
PREPS_LIEU = ["in", "on", "under", "next to", "behind", "in front of", "above", "between"]


def mots_allemands():
    """mot allemand -> traduction anglaise, depuis le corpus allemand."""
    d = {}
    for t in C.charger("themes.json")["themes"]:
        for m in t["mots"]:
            d.setdefault(m["mot"], m.get("traduction_en"))
    return d


def anglais(nom_de, points, corpus_de, idx):
    """Nom allemand (peut-etre au datif pluriel) -> (mot anglais, pluriel) ou None."""
    for essai in (nom_de, nom_de[:-1], nom_de[:-2], nom_de + "e"):
        if not essai:
            continue
        p = points.get(essai)
        if p is None and essai in corpus_de:
            p = {"mot": essai, "en": corpus_de[essai]}
        if p is None and essai in S.MOTS:
            p = {"mot": essai}
        if p is not None:
            r = S.anglais_de(p, idx)
            if r:
                return r["mot"], r.get("pluriel")
    return None


# Le mot de la scene, quand le mot du corpus ne convient pas ici.
LOCAL = {"Bank": "bench", "Torte": "cake", "Haare": "hair"}
PRENOMS = {"Mark", "Anna", "Tom", "Lena"}
POSSESSIFS = {"seinem": "his", "seiner": "his", "seinen": "his", "sein": "his", "seine": "his",
              "ihrem": "her", "ihrer": "her", "ihren": "her", "ihr": "her", "ihre": "her"}


def nom_anglais(art, nom, points, corpus_de, idx, prep_de=""):
    if nom in PRENOMS:
        return nom
    if nom in LOCAL:
        mot, pl = LOCAL[nom], None
    else:
        r = anglais(nom, points, corpus_de, idx)
        if not r:
            return None
        mot, pl = r
    if prep_de and nom == "Decke" and prep_de in ("an", "am"):
        mot = "ceiling"
    pluriel = art in ("den", "seinen", "ihren") and prep_de not in ("ins",) and nom.endswith("n") and pl
    det = POSSESSIFS.get(art, "the")
    return det + " " + (pl if pluriel else mot)


def groupe(texte, points, corpus_de, idx, verbe=""):
    """« neben der Pfanne » -> ("next to", "the frying pan") ; None si on ne sait pas."""
    cote = ""
    m = re.match(r"^(rechts|links)\s+(.*)$", texte)
    if m:
        cote, texte = m.group(1), m.group(2)
    art_re = r"(?:(der|die|das|dem|den|des|einem|einer|einen|ein|eine|seinem|seiner|seinen|seine|ihrem|ihrer|ihren|ihre)\s+)?"
    m = re.match(r"^(\w+)\s+" + art_re + r"(?:[a-zäöüß]+\s+)*([A-ZÄÖÜ][\wäöüß-]*)(?:\s+und\s+" + art_re +
                 r"(?:[a-zäöüß]+\s+)*([A-ZÄÖÜ][\wäöüß-]*))?", texte)
    if not m:
        return None
    prep_de, art, nom = m.group(1).lower(), m.group(2), m.group(3)
    if prep_de not in PREP:
        return None
    lieu = nom_anglais(art, nom, points, corpus_de, idx, prep_de)
    if not lieu:
        return None
    if m.group(5):
        second = nom_anglais(m.group(4), m.group(5), points, corpus_de, idx)
        if not second:
            return None
        lieu += " and " + second
    prep = PREP[prep_de]
    if prep_de in ("an", "am"):
        if nom == "Himmel":
            prep = "in"
        elif nom == "Wand" and verbe != "hängt":
            prep = "against"
        elif verbe in ("hängt", "hängen"):
            prep = "on"
        else:
            prep = AN_AUTRE.get(nom, "by")
    elif prep_de in ("in", "im") and nom == "Regal":
        prep = "on"
    elif prep_de in ("bei", "beim"):
        prep = "with"
    elif prep_de == "über" and nom == "Stuhl" and verbe in ("hängt", "hängen"):
        prep = "over"
    elif prep_de == "auf" and nom in ("Wiese", "Gras"):
        prep = "in"
    if cote:
        prep = "to the %s of" % ("right" if cote == "rechts" else "left")
    if nom in ("See", "Meer") and prep_de in ("an", "am"):
        prep = "by"
    return prep, lieu


def brouillon(nom, idx, corpus_de):
    de = S.charger_scene(nom)
    a2 = de.get("couches", {}).get("A2")
    if not a2:
        return None
    points = {p["mot"]: p for p in de["points"]}
    par_id = {p.get("id"): p for p in de["points"]}
    qs = []
    for i, q in enumerate(a2.get("qs", [])):
        pf = par_id.get(q.get("f"))
        sujet = S.anglais_de(pf, idx) if pf else None
        mv = re.match(r"^Wo (\w+)\b", q["q"])
        verbe = mv.group(1) if mv else ""
        pluriel = verbe in ("liegen", "stehen", "sind", "hängen", "sitzen")
        prenom = next((p for p in PRENOMS if re.search(r"\b%s\?" % p, q["q"])), None)
        if prenom:
            s_txt = prenom
        elif sujet:
            mot = LOCAL.get(pf.get("mot"), sujet["mot"])
            s_mot = (sujet.get("pluriel") or C.pluriel(mot)) if pluriel else mot
            if mot in VN.PLURIEL_SEUL or mot in ("hair",):
                pluriel = mot in VN.PLURIEL_SEUL
            s_txt = "the " + s_mot
        else:
            s_txt = "??"
        etre = "are" if pluriel else "is"
        gs = [groupe(c, points, corpus_de, idx, verbe) for c in q["c"]]
        bon = gs[0]
        prep = bon[0] if bon else "??"
        lieu = (bon[0] + " " + bon[1]) if bon else "??"
        phrase = "%s %s %s." % (s_txt[:1].upper() + s_txt[1:], etre, lieu)
        a_paire = any(g and " and " in g[1] for g in gs)
        if i % 2 == 0 or not bon or a_paire:
            question = "Where %s %s?" % (etre, s_txt)
            choix = []
            for g in gs:
                c = (g[0] + " " + g[1]) if g else "??"
                if c not in choix or c == "??":
                    choix.append(c)
        else:
            question = "%s %s ___ %s." % (s_txt[:1].upper() + s_txt[1:], etre, bon[1])
            choix = [prep]
            for p in [g[0] for g in gs[1:] if g]:
                if p not in choix:
                    choix.append(p)
            for p in PREPS_LIEU:
                if len(choix) >= 3:
                    break
                if p not in choix:
                    choix.append(p)
            choix = choix[:3]
        e = {"q": question, "c": choix, "f": q.get("f")}
        if q.get("r"):
            e["r"] = q["r"]
        e.update({"phrase": phrase, "sens": q.get("sens", ""), "n": NOTES.get(prep, "??"),
                  "_de": q["q"] + " → " + q["c"][0]})
        qs.append(e)
    return {"_lisez_moi": "Couches A2-C1 de la scene « %s » en anglais, ECRITES pour l'anglais sur les faits de l'image "
                          "(memes zones f et reperes r que l'allemand). SOURCE : on corrige ici, puis "
                          "python anglais/outils/scenes.py. Le champ _de rappelle le fait allemand ; scenes.py ne le copie pas." % nom,
            "couches": {"A2": {"titre": "Where is it? — les prépositions de lieu", "qs": qs}}}


def main():
    os.makedirs(DOSSIER, exist_ok=True)
    idx = S.corpus()
    corpus_de = mots_allemands()
    n = inconnus = 0
    for nom in S.toutes():
        if nom in S.EXCLUES:
            continue
        p = os.path.join(DOSSIER, nom + ".json")
        if os.path.exists(p):
            print("  %s existe : on n'y touche pas" % nom)
            continue
        b = brouillon(nom, idx, corpus_de)
        if not b:
            continue
        qs = b["couches"]["A2"]["qs"]
        n += len(qs)
        inconnus += sum(1 for q in qs if "??" in json.dumps(q, ensure_ascii=False))
        io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(b, ensure_ascii=False, indent=1) + "\n")
    print("%d questions A2 ecrites, %d avec un « ?? » a corriger" % (n, inconnus))


if __name__ == "__main__":
    main()
