# -*- coding: utf-8 -*-
"""Les corrections du controle de qualite du 2 nov. 2026, sur les fichiers SOURCES.

    python retours/qualite-es-de/corriger.py            # montre ce qui changerait
    python retours/qualite-es-de/corriger.py --ecrire   # ecrit

Chaque correction verifie la valeur ACTUELLE avant d'ecrire : si le fichier a
bouge depuis le controle, elle refuse au lieu d'ecraser. Relancer apres
--ecrire ne change plus rien (tout est deja fait).

Le texte de la langue apprise (allemand, espagnol) n'est JAMAIS touche ici :
chaque phrase a sa voix enregistree, nommee par l'empreinte du texte ; la
changer la rendrait muette. Ces cas-la sont dans le rapport, a trancher.
"""
import io
import json
import os
import re
import sys

from commun import RACINE

FORMAT = {  # (indent, separateurs, fin de fichier) : ceux du fichier dans git
    "exercices.json": (None, (",", ":"), ""),
    "themes.json": (2, (",", ": "), "\n"),
    "verbe.json": (2, (",", ": "), "\n"),
    "pruefung.json": (1, (",", ": "), "\n"),
    "espanol/datos/grammaire.json": (1, (",", ": "), "\n"),
    "espanol/datos/ejercicios.json": (1, (",", ": "), "\n"),
}
ECRIRE = "--ecrire" in sys.argv
JOURNAL = []
DOC = {}


def doc(f):
    if f not in DOC:
        DOC[f] = json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))
    return DOC[f]


def poser(f, obj, cle, avant, apres, ou):
    act = obj.get(cle)
    if act == apres:
        return
    if act != avant:
        raise SystemExit("REFUS %s %s.%s : valeur actuelle %r, attendue %r" % (f, ou, cle, act, avant))
    obj[cle] = apres
    JOURNAL.append((f, ou + "." + cle, avant, apres))


# ------------------------------------------------ 1. turc reste en anglais
TR_PHRASES = {
    "Since I've been living in Berlin, I speak German every day.": "Berlin'de yaşadığımdan beri her gün Almanca konuşuyorum.",
    "Because it's raining today, we're staying home.": "Bugün yağmur yağdığı için evde kalıyoruz.",
    "If you have time, I'll call you.": "Vaktin varsa seni ararım.",
    "Although he's tired, he keeps working.": "Yorgun olmasına rağmen çalışmaya devam ediyor.",
    "I speak German every day since I've been living in Berlin.": "Berlin'de yaşadığımdan beri her gün Almanca konuşuyorum.",
    "We're staying home because it's raining today.": "Bugün yağmur yağdığı için evde kalıyoruz.",
    "After we had eaten, we went for a walk.": "Yemek yedikten sonra yürüyüşe çıktık.",
    "I went to bed early because I was tired.": "Yorgun olduğum için erken yattım.",
    "Since she moved, we haven't seen each other.": "O taşındığından beri birbirimizi görmedik.",
    "Although it rained, we went for a walk.": "Yağmur yağmasına rağmen yürüyüşe çıktık.",
    "We waited until the rain had stopped.": "Yağmur dinene kadar bekledik.",
    "If you come tomorrow, we'll cook together.": "Yarın gelirsen birlikte yemek yapacağız.",
    "I'll call you as soon as I've arrived.": "Varır varmaz seni arayacağım.",
    "We'll stay home because it's going to rain.": "Yağmur yağacağı için evde kalacağız.",
    "Before we eat, we wash our hands.": "Yemek yemeden önce ellerimizi yıkıyoruz.",
    "He takes the bus although he has a car.": "Arabası olmasına rağmen otobüse biniyor.",
    "Since I've been working here, I have less time.": "Burada çalıştığımdan beri daha az vaktim var.",
    "I don't know if he's coming today.": "Bugün gelip gelmeyeceğini bilmiyorum.",
    "When I was little, I lived in Vienna.": "Küçükken Viyana'da yaşadım.",
}
TR_EXPL = {
    "The subordinate clause holds first place: the main clause's verb follows it immediately, and the subject comes after.":
        "Yan cümle birinci yeri tutar: ana cümlenin fiili hemen onu izler, özne ise fiilden sonra gelir.",
    "In the subordinate clause the verb goes to the end (regnet). In the main clause it comes right after the comma.":
        "Yan cümlede fiil sona gider (regnet). Ana cümlede fiil virgülün hemen ardından gelir.",
    "Separable verb: « rufe » takes its slot after the comma, « an » stays at the end.":
        "Ayrılabilir ön ekli fiil: « rufe » virgülden sonraki yeri alır, « an » sonda kalır.",
    "Same pattern with « obwohl »: it isn't the meaning that decides the order, it's the position.":
        "« obwohl » ile de aynı kalıp: sırayı anlam değil, konum belirler.",
    "In the perfect, the auxiliary is the conjugated verb: it closes the subordinate clause (haben) and opens the main clause (sind).":
        "Perfekt'te çekimli fiil yardımcı fiildir: yan cümleyi kapatır (haben) ve ana cümleyi açar (sind).",
    "Two perfects: « ist » closes the subordinate clause, « haben » opens the main clause, and « gesehen » ends it.":
        "İki Perfekt: « ist » yan cümleyi kapatır, « haben » ana cümleyi açar, « gesehen » da onu bitirir.",
    "In a subordinate clause in the perfect, the auxiliary goes BEHIND the participle: geregnet hat.":
        "Perfekt'teki bir yan cümlede yardımcı fiil sıfat-fiilin ARKASINA gider: geregnet hat.",
    "« nachdem » calls for one tense back: pluperfect in the subordinate clause, perfect in the main one.":
        "« nachdem » bir zaman geriye gitmeyi ister: yan cümlede Plusquamperfekt, ana cümlede Perfekt.",
    "In the future, « werden » is the conjugated verb: it takes the slot right after the comma, the infinitive stays at the end.":
        "Gelecek zamanda çekimli fiil « werden »dir: virgülün hemen ardındaki yeri alır, mastar sonda kalır.",
    "Fronted subordinate clause: « wird » follows the comma, and the infinitive (aufstehen) closes the main clause.":
        "Yan cümle başta: « wird » virgülü izler, mastar (aufstehen) ana cümleyi kapatır.",
    "« bevor » opens the sentence: the main clause's verb right after the comma.":
        "Cümleyi « bevor » açar: ana cümlenin fiili virgülün hemen ardından gelir.",
    "Here « seit » is a conjunction: it opens a subordinate clause, so the verb goes to the end (arbeite).":
        "Burada « seit » bir bağlaçtır: yan cümle açar, bu yüzden fiil sona gider (arbeite).",
    "Fronted subordinate clause in the past, main clause in the perfect: the auxiliary (habe) follows the comma, the participle closes the sentence.":
        "Geçmiş zamanda yan cümle başta, ana cümle Perfekt'te: yardımcı fiil (habe) virgülü izler, sıfat-fiil cümleyi kapatır.",
}


def turc_anglais():
    j = doc("exercices.json")["jeux"]
    for jeu, champ, ref in (("blocsConnecteursExercises", "question_tr", "question_en"),
                            ("ordreInverseExercises", "translation_tr", "translation_en")):
        for i, e in enumerate(j[jeu]):
            if e.get(champ) and e.get(champ) == e.get(ref) and e[ref] in TR_PHRASES:
                poser("exercices.json", e, champ, e[champ], TR_PHRASES[e[ref]], "%s[%d]" % (jeu, i))
    for i, e in enumerate(j["blocsConnecteursExercises"]):
        t = e.get("explanation_tr", "")
        for en, tr in TR_EXPL.items():
            if t.startswith(en + " "):
                poser("exercices.json", e, "explanation_tr", t, tr + t[len(en):],
                      "blocsConnecteursExercises[%d]" % i)


# ------------------------------------------- 2. « Ça dépend » des prepositions
DEPEND = {"Tr": "Duruma göre (Wechselpräposition)",
          "Uk": "Залежить від ситуації (Wechselpräposition)",
          "Fa": "بستگی دارد (Wechselpräposition)",
          "Ar": "حسب السياق (Wechselpräposition)",
          "Pt": "Depende (Wechselpräposition)",
          "Pl": "To zależy (Wechselpräposition)",
          "Ru": "Зависит от ситуации (Wechselpräposition)"}
FR_DEPEND = "Ça dépend (Wechselpräposition)"


def prepositions():
    for i, e in enumerate(doc("exercices.json")["jeux"]["praepReconnaissanceExercises"]):
        if e.get("options") != ["Akkusativ", "Dativ", "Genitiv", FR_DEPEND]:
            continue
        for suf, txt in DEPEND.items():
            opts = ["Akkusativ", "Dativ", "Genitiv", txt]
            if "options" + suf not in e:
                e["options" + suf] = opts
                JOURNAL.append(("exercices.json", "praepReconnaissanceExercises[%d].options%s" % (i, suf), None, opts))
            cor = txt if e["correct"] == FR_DEPEND else e["correct"]
            if "correct" + suf not in e:
                e["correct" + suf] = cor
                JOURNAL.append(("exercices.json", "praepReconnaissanceExercises[%d].correct%s" % (i, suf), None, cor))
            if e["correct"] == FR_DEPEND and txt.lower() not in e["answers"]:
                e["answers"].append(txt.lower())


# ------------------------------------------- 3. une explication persane en francais
def persan_francais():
    e = doc("exercices.json")["jeux"]["konjunktiv2Exercises"][17]
    poser("exercices.json", e, "explanation_fa",
          "Konjunktiv II فعل «können» در دوم‌شخص: du könntest — forme polie pour une demande.",
          "Konjunktiv II فعل «können» در دوم‌شخص: du könntest — شکل مؤدبانه برای یک درخواست.",
          "konjunktiv2Exercises[17]")


# ------------------------------------------- 4. indices turcs des infinitifs
def indices_infinitif():
    for i, e in enumerate(doc("exercices.json")["jeux"]["infinitivExercises"]):
        h, t = e.get("hint", ""), e.get("hint_tr", "")
        m = re.match(r"^\(le verbe conjugué est déjà à l'infinitif : « (\w+) », après le verbe modal « (\w+) »\)$", h)
        if m and t == "(çekimli fiil « %s »)" % m.group(1):
            poser("exercices.json", e, "hint_tr", t,
                  "(fiil zaten mastar hâlinde: « %s », « %s » kip fiilinden sonra)" % m.groups(),
                  "infinitivExercises[%d]" % i)
        m = re.match(r"^\(verbe à particule séparable : « (.+) »\)$", h)
        if m and t.startswith("(çekimli fiil « "):
            poser("exercices.json", e, "hint_tr", t, "(ayrılabilir ön ekli fiil: « %s »)" % m.group(1),
                  "infinitivExercises[%d]" % i)


# ------------------------------------------- 5. der-/ein-Woerter : l'exemple rendu en tr, uk, fa
def der_ein():
    for i, e in enumerate(doc("exercices.json")["jeux"]["derEinExercises"]):
        segs = re.findall(r"«\s*([^»]+?)\s*»", e.get("explanation", ""))
        if not 1 <= len(segs) <= 2:
            continue
        for l in ("tr", "uk", "fa"):
            t = e.get("explanation_" + l, "")
            if not t or "«" in t or "." not in t:
                continue
            if l == "fa":
                ajout = "«%s»" % segs[0] if len(segs) == 1 else "«%s» ← «%s»" % (segs[0], segs[1])
            else:
                ajout = "« %s »" % segs[0] if len(segs) == 1 else "« %s » → « %s »" % (segs[0], segs[1])
            k = t.index(".")
            poser("exercices.json", e, "explanation_" + l, t, t[:k] + ": " + ajout + t[k:],
                  "derEinExercises[%d]" % i)


# ------------------------------------------- 6. article francais des noms (themes.json)
ARTICLE = {  # mot : (article actuel, article juste) ; "" = la traduction porte deja le sien
    "Person": ("la ", ""), "Gericht": ("le ", ""), "Patient": ("le ", ""), "Rose": ("la ", ""),
    "Profi": ("le ", ""),
    "Ehegatte": ("l'", "le "), "Selbstständige": ("l'", "le "), "Aushilfe": ("l'", "le "),
    "Leichtsinn": ("l'", "la "), "Beilage": ("l'", "la "),
    "Kollegium": ("le ", "l'"), "Ferienwohnung": ("la ", "l'"), "Tour": ("la ", "l'"),
    "Reiseleiter": ("le ", "l'"), "Förderung": ("la ", "l'"), "Achtsamkeit": ("la ", "l'"),
    "Durchführung": ("la ", "l'"), "Handschrift": ("la ", "l'"), "Wohnraum": ("le ", "l'"),
    "Tilgung": ("le ", "l'"), "Fürsorglichkeit": ("la ", "l'"), "Missgunst": ("la ", "l'"),
    "Seegang": ("la ", "l'"), "Pflegeheim": ("la ", "l'"), "Bebauung": ("le ", "l'"),
    "Tierhaltung": ("la ", "l'"),
}
TRAD_ATTENDUE = {"Tour": "excursion, sortie"}  # Tour a deux sens : on ne touche que celui-ci


def articles():
    for t in doc("themes.json")["themes"]:
        for i, m in enumerate(t["mots"]):
            if m["mot"] in ARTICLE:
                av, ap = ARTICLE[m["mot"]]
                if m["mot"] in TRAD_ATTENDUE and m["traduction"] != TRAD_ATTENDUE[m["mot"]]:
                    continue
                if m.get("article_fr") in (av, ap):
                    poser("themes.json", m, "article_fr", m.get("article_fr") if m.get("article_fr") == ap else av,
                          ap, "%s[%d]" % (t["id"], i))


# ------------------------------------------- 7. nombres en lettres en portugais (exercice des nombres espagnols)
PT_NOMBRES = {
    "O castelo tem setecentos anos.": "O castelo tem 700 anos.",
    "A ponte mede novecentos metros.": "A ponte mede 900 metros.",
    "A prova é no dia vinte e três de maio.": "A prova é no dia 23 de maio.",
    "O filme dura noventa minutos.": "O filme dura 90 minutos.",
}


def nombres_pt():
    for i, e in enumerate(doc("espanol/datos/ejercicios.json")["jeux"]["numerosExercises"]):
        t = e.get("translation_pt")
        if t in PT_NOMBRES:
            poser("espanol/datos/ejercicios.json", e, "translation_pt", t, PT_NOMBRES[t],
                  "numerosExercises[%d]" % i)


# ------------------------------------------- 8. fiches espagnoles : l'anglais ampute
EN_ATTENTION = {
    "pasados": ("English “I ate” can be either. Ask yourself: is this <i>what happened</i>, or <i>what things were like</i>?",
                "English “I ate” can be either. Ask yourself: is this <i>what happened</i>, or <i>what things were like</i>? "
                "“I was eating”, “I used to eat” → <b>comía</b>; “I ate (once, and it's over)” → <b>comí</b>. "
                "The trap: in Spain, <b>he comido</b> is used for anything still connected to the present "
                "(<i>hoy he comido paella</i>); in Latin America, people mostly say <b>comí</b> in both cases."),
    "subjuntivo": ("English keeps one fossil of it: “I suggest he <b>be</b> told”, not “is”. That's the same mood.",
                   "English keeps one fossil of it: “I suggest he <b>be</b> told”, not “is”. That's the same mood. "
                   "The big trap: after <b>cuando</b> pointing to the future, English uses the present "
                   "(“when I arrive”), Spanish the subjunctive — <b>cuando llegue</b>, never <i>cuando llegaré</i>. "
                   "Same after <b>espero que</b>: “I hope you come” is <b>espero que vengas</b>."),
    "pronombres": ("With an infinitive or a gerund you may attach the pronoun to the end instead — both orders are correct.",
                   "With an infinitive or a gerund you may attach the pronoun to the end instead — both orders are correct. "
                   "With a positive command it MUST be attached: <b>explícamelo</b> (explain it to me). "
                   "And the order is always “to whom”, then “what” — <b>le</b> becomes <b>se</b> before lo / la: "
                   "<b>se lo doy</b>, I give it to him."),
}


def fiches_en():
    for k, f in enumerate(doc("espanol/datos/grammaire.json")["fiches"]):
        if f["id"] in EN_ATTENTION:
            av, ap = EN_ATTENTION[f["id"]]
            poser("espanol/datos/grammaire.json", f["attention"], "en", av, ap, "fiches[%d].attention" % k)


# ------------------------------------------- 9. une faute de francais (examen)
def francais():
    for i, e in enumerate(doc("pruefung.json")["hoeren"]):
        t = e.get("erkl_fr", "")
        if "mais de la débat sur elle" in t:
            poser("pruefung.json", e, "erkl_fr", t, t.replace("mais de la débat sur elle", "mais du débat à son sujet"),
                  "hoeren[%d]" % i)


# ------------------------------------------- 10. auffallen : un fait ponctuel, pas une duree
# (signale par le relecteur ; pt, ar, pl et ru disaient deja « j'ai remarque »)
AUFFALLEN = {
    "fr": ("Je remarquais que tu étais fatigué.", "J'ai remarqué que tu étais fatigué."),
    "en": ("I was noticing that you were tired.", "I noticed that you were tired."),
    "tr": ("Yorgun olduğun dikkatimi çekiyordu.", "Yorgun olduğun dikkatimi çekti."),
    "uk": ("Я помічав, що ти був втомлений.", "Я помітив, що ти був втомлений."),
    "fa": ("به چشمم می‌آمد که خسته بودی.", "متوجه شدم که خسته بودی."),
}


def auffallen():
    VB = doc("verbe.json")
    for i, v in enumerate(VB["B1"]):
        if v["infinitif"] == "auffallen" and v.get("praeteritum") == "Mir fiel auf, dass du müde warst.":
            for l, (av, ap) in AUFFALLEN.items():
                poser("verbe.json", v, "praeteritum_" + l, av, ap, "B1[%d]" % i)


def main():
    for f in (auffallen, turc_anglais, prepositions, persan_francais, indices_infinitif, der_ein, articles,
              nombres_pt, fiches_en, francais):
        f()
    for f, ou, av, ap in JOURNAL:
        print("%-32s %-58s %s" % (f, ou, json.dumps(ap, ensure_ascii=False)[:90]))
    print(len(JOURNAL), "changements")
    if ECRIRE:
        for f, d in DOC.items():
            ind, sep, fin = FORMAT[f]
            with io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="\n") as h:
                h.write(json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin)
        json.dump([{"fichier": f, "ou": ou, "avant": av, "apres": ap} for f, ou, av, ap in JOURNAL],
                  io.open(os.path.join(RACINE, "retours", "qualite-es-de", "corrections.json"), "w",
                          encoding="utf-8"), ensure_ascii=False, indent=1)
        print("ecrit.")


if __name__ == "__main__":
    main()
