# -*- coding: utf-8 -*-
"""praepReconnaissanceExercises (50) : les prepositions et le cas qu'elles imposent."""
import io, json, os, re, sys

R = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
QSUF_FR = " — quel cas impose cette préposition ?"
QSUF_UK = " — якого відмінка вимагає цей прийменник?"
HINT_FR = "(certaines prépositions imposent toujours le même cas, d'autres non)"
HINT_UK = "(одні прийменники завжди вимагають того самого відмінка, інші — ні)"

# La traduction de chaque preposition. Les gloses francaises portent souvent
# deux sens separes par « / » : on garde la meme forme en ukrainien.
T = {
"pour":"для / за",
"avec":"з",
"à cause de":"через",
"sur":"на",
"à travers":"крізь / через",
"contre":"проти",
"sans":"без",
"autour de / à (heure)":"навколо / о (годині)",
"jusqu'à":"до",
"le long de":"уздовж",
"contre (littéraire)":"проти (книжне)",
"de / hors de":"з / із",
"chez / près de":"у (когось) / біля",
"après / vers":"після / до",
"depuis":"від / з",
"de (provenance)":"від / з",
"vers / à":"до",
"sauf / excepté":"крім / окрім",
"en face de":"навпроти",
"à partir de":"починаючи з",
"conformément à":"згідно з",
"près de":"поблизу",
"avec / y compris":"разом із",
"selon / d'après":"згідно з",
"pendant":"під час",
"malgré":"попри",
"au lieu de":"замість",
"à l'intérieur de":"усередині / в межах",
"à l'extérieur de":"поза межами",
"au-dessus de":"вище / над",
"au-dessous de":"нижче / під",
"en raison de":"з причини",
"face à / vu":"з огляду на",
"en deçà de":"по цей бік",
"au-delà de":"по той бік",
"au moyen de":"за допомогою",
"en vertu de":"на підставі",
"dans le but de":"з метою",
"non loin de":"неподалік",
"à / contre":"на / до",
"dans":"у / в",
"derrière":"позаду / за",
"à côté de":"поряд із",
"sous":"під",
"devant / avant":"перед",
"entre":"між",
}

CAS = {"Akkusativ": "Akkusativ", "Dativ": "Dativ", "Genitiv": "Genitiv"}


def traduire_explication(x):
    m = re.match(r"^« (.+?) » fait partie du groupe toujours (\w+) \((.+?)\)\.$", x)
    if m:
        return ("« %s » належить до групи, що завжди вимагає %s (%s)."
                % (m.group(1), CAS[m.group(2)], m.group(3)))
    m = re.match(r"^« (.+?) » est une Wechselpräposition : Dativ pour la position \(wo\), "
                 r"Akkusativ pour le mouvement \(wohin\)\.$", x)
    if m:
        return ("« %s » — Wechselpräposition: Dativ для положення (wo), "
                "Akkusativ для руху (wohin)." % m.group(1))
    m = re.match(r"^« (.+?) » impose l'Akkusativ \(souvent suivi d'une autre préposition : "
                 r"(.+?)\)\.$", x)
    if m:
        return ("« %s » вимагає Akkusativ (часто за ним іде інший прийменник: %s)."
                % m.groups())
    m = re.match(r"^« (.+?) » impose l'Akkusativ, souvent placée après le nom : (.+?)\.$", x)
    if m:
        return ("« %s » вимагає Akkusativ і часто стоїть після іменника: %s." % m.groups())
    m = re.match(r"^« (.+?) » \(registre soutenu\) impose l'Akkusativ : (.+?)\.$", x)
    if m:
        return "« %s » (книжний регістр) вимагає Akkusativ: %s." % m.groups()
    m = re.match(r"^« (.+?) » \(registre (soutenu|administratif)\) impose toujours "
                 r"le (\w+) : (.+?)\.$", x)
    if m:
        reg = "книжний" if m.group(2) == "soutenu" else "офіційний"
        return ("« %s » (%s регістр) завжди вимагає %s: %s."
                % (m.group(1), reg, CAS[m.group(3)], m.group(4)))
    m = re.match(r"^« (.+?) » \(registre (soutenu|administratif)\) impose toujours le (\w+)\.$", x)
    if m:
        reg = "книжний" if m.group(2) == "soutenu" else "офіційний"
        return "« %s » (%s регістр) завжди вимагає %s." % (m.group(1), reg, CAS[m.group(3)])
    m = re.match(r"^« (.+?) » impose toujours le (\w+) : (.+?)\.$", x)
    if m:
        return "« %s » завжди вимагає %s: %s." % (m.group(1), CAS[m.group(2)], m.group(3))
    m = re.match(r"^« (.+?) » impose toujours le (\w+)\.$", x)
    if m:
        return "« %s » завжди вимагає %s." % (m.group(1), CAS[m.group(2)])
    return None


d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
entrees, rates = [], []
for e in d["jeux"]["praepReconnaissanceExercises"]:
    fr, q, x, h = e["translation"], e["question"], e["explanation"], e.get("hint", "")
    if fr not in T: rates.append("GLOSE : " + fr); continue
    if not q.endswith(QSUF_FR): rates.append("QUESTION : " + q); continue
    if h != HINT_FR: rates.append("INDICE : " + h); continue
    expl = traduire_explication(x)
    if not expl: rates.append("EXPL : " + x); continue
    entrees.append({"question": q, "question_uk": q[:-len(QSUF_FR)] + QSUF_UK,
                    "translation_uk": T[fr], "hint_uk": HINT_UK,
                    "explanation_uk": expl})

if rates:
    print("REFUS : %d" % len(rates))
    for r in rates[:10]: print("   " + r)
    sys.exit(1)
io.open(os.path.join(R, "corrections_uk", "exos_praepReconnaissance.json"), "w",
        encoding="utf-8", newline="\n").write(
    json.dumps({"jeu": "praepReconnaissanceExercises", "entrees": entrees},
               ensure_ascii=False, indent=1) + "\n")
print("exos_praepReconnaissance.json : %d entrees" % len(entrees))
