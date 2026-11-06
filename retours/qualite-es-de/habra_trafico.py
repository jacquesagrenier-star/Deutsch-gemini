# -*- coding: utf-8 -*-
"""Suite de serian_las_diez.py (4 nov. 2026, « le controle de la qualite, tu
peux continuer ») : l'explication commune des compuestosExercises disait
encore « conditionnel passé » pour « Serían las diez » dans neuf exercices.

  - [17] « Todavía no ha llegado. Habrá tráfico. » est un FUTUR SIMPLE de
    probabilite (une supposition sur le present) : explication propre.
  - [13] [21] [25] [29] [33] [37] [41] [45] prennent le texte que Jacques a
    tranche le 3 nov. pour [2] [6] [9] (conditionnel de probabilite).

Entrees manuelles de triage.json, appliquees par verdicts.py --ecrire.

    python retours/qualite-es-de/habra_trafico.py
"""
import ast
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
F = "espanol/datos/ejercicios.json"

# Le texte tranche par Jacques, pris tel quel dans serian_las_diez.py
arbre = ast.parse(io.open(os.path.join(ICI, "serian_las_diez.py"), encoding="utf-8").read())
NEUF = [ast.literal_eval(n.value) for n in arbre.body
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "NEUF"][0]

TRAFICO = {
    "explanation": "Le futur simple sert aussi à deviner le présent : « Habrá tráfico » = il doit y avoir des bouchons (en ce moment). Pour deviner le passé récent, on prend le futur antérieur : « Habrá salido » = il a dû sortir.",
    "explanation_en": "The simple future is also used to guess about the present: “Habrá tráfico” = there must be traffic (right now). To guess about the recent past, Spanish uses the future perfect: “Habrá salido” = he must have gone out.",
    "explanation_pt": "O futuro simples também serve para supor o presente: “Habrá tráfico” = deve ter trânsito (agora). Para supor o passado recente, usa-se o futuro perfeito: “Habrá salido” = ele deve ter saído.",
    "explanation_ar": "يُستعمل المستقبل البسيط أيضًا لتخمين الحاضر: «Habrá tráfico» = لا بدّ أن هناك زحامًا (الآن). ولتخمين ماضٍ قريب يُستعمل المستقبل التام: «Habrá salido» = لا بدّ أنه خرج.",
    "explanation_de": "Das einfache Futur dient auch der Vermutung über die Gegenwart: „Habrá tráfico“ = es wird wohl Stau geben (gerade jetzt). Für die jüngste Vergangenheit steht das Futuro perfecto: „Habrá salido“ = er wird wohl weggegangen sein.",
}
R17 = "« Habrá tráfico » est un futur simple de probabilité (supposition sur le présent), pas un futur antérieur"
R = "même explication fautive que [2] [6] [9] : le texte tranché par Jacques le 3 nov. (conditionnel de probabilité)"

T = json.load(io.open(os.path.join(ICI, "triage.json"), encoding="utf-8"))
J = json.load(io.open(os.path.join(RACINE, F), encoding="utf-8"))["jeux"]["compuestosExercises"]
ANCIEN = J[13]["explanation"]
assert "conditionnel passé" in ANCIEN
n = 0
for i in (13, 17, 21, 25, 29, 33, 37, 41, 45):
    assert J[i]["explanation"] == ANCIEN, i
    for k, v in (TRAFICO if i == 17 else NEUF).items():
        T["manuel|%s|jeux.compuestosExercises[%d]|%s" % (F, i, k)] = {
            "decision": "appliquer", "avant": J[i][k], "apres": v, "raison": R17 if i == 17 else R}
        n += 1
for k, t in T.items():
    if k.startswith("1236|") and t.get("decision") == "trancher":
        t["decision"] = "fait"
        t["raison"] += " -- réécrit le 4 nov. (habra_trafico.py)"
json.dump(T, io.open(os.path.join(ICI, "triage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(n, "explications posees")
