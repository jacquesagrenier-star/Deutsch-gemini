# -*- coding: utf-8 -*-
"""Entrees manuelles de triage.json (appliquees par verdicts.py --ecrire) :

1. Les reponses traduites absentes de « answers » (3 nov. 2026). L'ecran
   d'exercices affiche options<Langue> (valeurTraduite) mais juge la reponse
   contre ex.answers seul, qui ne porte que fr / en / tr : en uk, fa, pt, ar,
   pl et ru, la bonne option etait comptee fausse. On ajoute a answers les
   correct<Langue> qui y manquent, partout ou options<Langue> existe.
2. Les decisions de Jacques du 3 nov. (« toutes les recommandations ») :
   wissen / kennen (deux reponses), l'explication de kannte, schließlich = Zeit,
   « Du bist vielleicht ein Glückspilz » (deux reponses), la question
   « Ich gehe nicht, sondern ich bleibe » et ses traductions (voix en attente
   de l'accord de Jacques).

    python retours/qualite-es-de/decisions_3nov.py
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
LANGUES = ("En", "Tr", "Uk", "Fa", "Pt", "Ar", "Pl", "Ru")

T = json.load(io.open(os.path.join(ICI, "triage.json"), encoding="utf-8"))
J = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))["jeux"]


def manuel(fam, i, champ, apres, raison):
    T["manuel|exercices.json|jeux.%s[%d]|%s" % (fam, i, champ)] = {
        "decision": "appliquer", "avant": J[fam][i][champ], "apres": apres, "raison": raison}


def answers_avec(fam, i, ajouts):
    """answers + les ajouts absents (comparaison sans casse, comme l'app)."""
    a = list(J[fam][i]["answers"])
    vus = {str(x).lower() for x in a}
    for x in ajouts:
        if x and x.lower() not in vus:
            a.append(x)
            vus.add(x.lower())
    return a


# 2. Les decisions (avant le 1, pour que les answers enrichis s'y ajoutent)
D = "décision de Jacques du 3 nov. : « toutes les recommandations »"
SURPLUS = {}
for i, autre in ((13, "kennt"), (22, "kenne"), (33, "kennt"), (43, "weiß"), (44, "kennt")):
    SURPLUS[("wissenKennenExercises", i)] = [autre]
f, i = "wissenKennenExercises", 49
X = {"explanation": "« kennen » : une personne qu'on a déjà rencontrée (ici : ihn) ; au prétérit : kannte.",
     "explanation_en": "« kennen »: a person you have already met (here: ihn); in the simple past: kannte.",
     "explanation_tr": "« kennen » : daha önce tanıştığımız bir kişi (burada: ihn) ; Präteritum'da: kannte.",
     "explanation_uk": "« kennen » : людина, з якою вже знайомі (тут: ihn) ; у Präteritum: kannte.",
     "explanation_fa": "«kennen»: کسی که پیش‌تر با او آشنا شده‌ایم (اینجا: ihn)؛ در Präteritum: ‏kannte.",
     "explanation_pt": "“kennen”: uma pessoa que já conhecemos (aqui: ihn); no Präteritum: kannte.",
     "explanation_ar": "«kennen»: شخص سبق التعرّف إليه (هنا: ihn)؛ في الـPräteritum: ‏kannte.",
     "explanation_pl": "„kennen”: osoba, którą już znamy (tu: ihn); w Präteritum: kannte.",
     "explanation_ru": "«kennen»: человек, с которым уже знакомы (здесь: ihn); в Präteritum: kannte."}
for k, v in X.items():
    if k in J[f][i]:
        manuel(f, i, k, v, D + " -- l'explication parlait de wissen, la réponse est kannte")

f, i = "adverbienNuanceExercises", 46
for k in ("correct",) + tuple("correct" + L for L in LANGUES):
    if k in J[f][i]:
        manuel(f, i, k, "Zeit", D + " -- « schließlich » = finalement, un adverbe de temps")
SURPLUS[(f, i)] = ["Zeit"]
X = {"explanation": "« schließlich » situe ici dans le temps (finalement) -- Zeit.",
     "explanation_en": "« schließlich » here places the action in time (finally) -- Zeit.",
     "explanation_tr": "« schließlich » burada eylemi zamana yerleştirir (sonunda) — Zeit.",
     "explanation_uk": "« schließlich » тут вказує на час (зрештою) — Zeit.",
     "explanation_fa": "«schließlich» اینجا کنش را در زمان جای می‌دهد (سرانجام) — Zeit.",
     "explanation_pt": "“schließlich” situa aqui a ação no tempo (finalmente) -- Zeit.",
     "explanation_ar": "«schließlich» هنا يحدّد الزمن (أخيرًا) — Zeit.",
     "explanation_pl": "„schließlich” umieszcza tu czynność w czasie (w końcu) — Zeit.",
     "explanation_ru": "«schließlich» здесь указывает на время (в конце концов) — Zeit."}
for k, v in X.items():
    if k in J[f][i]:
        manuel(f, i, k, v, D)

f, i = "partikelnNuanceExercises", 49
e = J[f][i]
admir = "Surprise, emphase admirative"
j = e["options"].index(admir)
SURPLUS[(f, i)] = [admir] + [e["options" + L][j] for L in LANGUES if e.get("options" + L)]

f, i = "konnektorenExercises", 41
e = J[f][i]
R5 = D + " -- « sondern » oppose deux termes : « Ich gehe nicht, sondern ich bleibe » (voix en attente de l'accord de Jacques)"
for k in [c for c in e if c == "question" or c.startswith("question_")]:
    if "Ich kann nicht, sondern ich bleibe." in e[k]:
        manuel(f, i, k, e[k].replace("Ich kann nicht, sondern ich bleibe.", "Ich gehe nicht, sondern ich bleibe."), R5)
TR = {"translation": "Je ne pars pas, je reste.", "translation_en": "I'm not leaving, I'm staying.",
      "translation_tr": "Gitmiyorum, kalıyorum.", "translation_uk": "Я не йду, а залишаюся.",
      "translation_fa": "نمی‌روم، بلکه می‌مانم.", "translation_pt": "Eu não vou, eu fico.",
      "translation_ar": "لن أذهب، بل سأبقى.", "translation_pl": "Nie idę, tylko zostaję.",
      "translation_ru": "Я не ухожу, а остаюсь."}
for k, v in TR.items():
    if k in e:
        manuel(f, i, k, v, R5)

# 1. Les reponses traduites, plus les surplus des decisions
n = 0
for fam, liste in J.items():
    if not isinstance(liste, list):
        continue
    for i, e in enumerate(liste):
        if not isinstance(e, dict) or not isinstance(e.get("answers"), list):
            continue
        ajouts = list(SURPLUS.get((fam, i), []))
        for L in LANGUES:
            if e.get("options" + L):
                ajouts.append(e.get("correct" + L))
        # schließlich : la reponse devient Zeit dans toutes les langues
        if (fam, i) == ("adverbienNuanceExercises", 46):
            ajouts = ["Zeit"]
            a = ["Zeit"]
        else:
            a = answers_avec(fam, i, ajouts)
        if a != e["answers"]:
            manuel(fam, i, "answers", a,
                   "réponses acceptées : les réponses traduites (correct<Langue>) manquaient, la bonne option était jugée fausse hors fr / en / tr"
                   + (" ; " + D if (fam, i) in SURPLUS else ""))
            n += 1
json.dump(T, io.open(os.path.join(ICI, "triage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(n, "listes answers completees ; decisions posees")
