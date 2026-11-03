# -*- coding: utf-8 -*-
"""Decision de Jacques du 3 nov. 2026 (« corrige ») : « Serían las diez » est un
conditionnel de PROBABILITE (une supposition sur le passe : « il devait etre
dix heures »), pas un « conditionnel passe ». L'explication commune aux
exercices compuestosExercises [2], [6] et [9] est reecrite dans toutes les
langues d'interface. Entrees manuelles de triage.json, appliquees par
verdicts.py --ecrire.

    python retours/qualite-es-de/serian_las_diez.py
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
F = "espanol/datos/ejercicios.json"

NEUF = {
    "explanation": "Le futur antérieur sert aussi à deviner le passé récent : « Habrá salido » = il a dû sortir. Pour deviner un passé plus lointain, on prend le conditionnel de probabilité : « Serían las diez » = il devait être dix heures ; « Habría salido » = il avait dû sortir.",
    "explanation_en": "The future perfect is also used to guess about the recent past: “Habrá salido” = he must have gone out. To guess about a more distant past, Spanish uses the conditional of probability: “Serían las diez” = it must have been ten o'clock; “Habría salido” = he must have gone out (earlier).",
    "explanation_pt": "O futuro perfeito também serve para supor o passado recente: “Habrá salido” = ele deve ter saído. Para supor um passado mais distante, usa-se o condicional de probabilidade: “Serían las diez” = deviam ser dez horas; “Habría salido” = ele devia ter saído.",
    "explanation_ar": "يُستعمل المستقبل التام أيضًا لتخمين ماضٍ قريب: «Habrá salido» = لا بدّ أنه خرج. ولتخمين ماضٍ أبعد يُستعمل شرطي الاحتمال: «Serían las diez» = لا بدّ أن الساعة كانت العاشرة؛ «Habría salido» = لا بدّ أنه كان قد خرج.",
    "explanation_de": "Das Futuro perfecto dient auch der Vermutung über die jüngste Vergangenheit: „Habrá salido“ = er wird wohl weggegangen sein. Für eine fernere Vergangenheit steht der Condicional der Wahrscheinlichkeit: „Serían las diez“ = es war wohl zehn Uhr; „Habría salido“ = er war wohl weggegangen.",
}
R = ("décision de Jacques du 3 nov. (« corrige ») : « Serían las diez » est un conditionnel "
     "de probabilité (supposition sur le passé), pas un conditionnel passé")

T = json.load(io.open(os.path.join(ICI, "triage.json"), encoding="utf-8"))
J = json.load(io.open(os.path.join(RACINE, F), encoding="utf-8"))["jeux"]["compuestosExercises"]
n = 0
for i in (2, 6, 9):
    for k, v in NEUF.items():
        if k in J[i]:
            T["manuel|%s|jeux.compuestosExercises[%d]|%s" % (F, i, k)] = {
                "decision": "appliquer", "avant": J[i][k], "apres": v, "raison": R}
            n += 1
for k, t in T.items():
    if k.startswith("1235|") and t.get("decision") == "trancher":
        t["decision"] = "fait"
        t["raison"] += " -- tranché par Jacques le 3 nov. (« corrige »), voir serian_las_diez.py"
json.dump(T, io.open(os.path.join(ICI, "triage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(n, "explications posees")
