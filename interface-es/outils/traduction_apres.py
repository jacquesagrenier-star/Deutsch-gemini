# -*- coding: utf-8 -*-
"""La traduction espagnole ne doit jamais donner la reponse (regle du chef, 15 nov. 2026).

    python interface-es/outils/traduction_apres.py [--ecrire]

Dans trois series, le francais ne distingue pas ce que l'allemand oppose, et l'espagnol, lui,
le distingue : wann / wenn (quand / quand ; cuándo / cuando), aber / sondern (mais / mais ;
pero / sino), wenn / ob (si / si ; cuando / si). Montree avant la reponse, la traduction
espagnole la donnerait. Ces exercices recoivent `traductionApres_es: true` (exercices.json),
et index.html ne montre leur traduction, en interface espagnole, qu'une fois la reponse donnee
(loadExercise / checkAnswer). Les autres langues ne changent pas.
"""
import io, json, os, sys
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES = ["wennWannExercises", "aberSondernExercises", "wennObExercises"]

# 1. Les donnees.
p = os.path.join(RACINE, "exercices.json")
brut = io.open(p, encoding="utf-8", newline="").read()
d = json.loads(brut)
assert json.dumps(d, ensure_ascii=False, separators=(",", ":")) == brut, "exercices.json : aller-retour"
n = 0
for s in SERIES:
    for e in d["jeux"][s]:
        if not e.get("traductionApres_es"):
            e["traductionApres_es"] = True
            n += 1
print("%d exercices marques (%s)" % (n, ", ".join(SERIES)))

# 2. Le code.
q = os.path.join(RACINE, "index.html")
src = io.open(q, encoding="utf-8", newline="").read()
nl = "\r\n" if "\r\n" in src else "\n"


def r(avant, apres):
    global src
    avant, apres = avant.replace("\n", nl), apres.replace("\n", nl)
    if src.count(avant) != 1:
        sys.exit("index.html : introuvable ou en double : %r" % avant[:80])
    src = src.replace(avant, apres)


r('''    const tradEl = document.getElementById("questionTranslation");
    tradEl.textContent = translation ? tf("question_translation_label", { translation }) : "";
    tradEl.classList.toggle("hidden", !translation);''',
  '''    const tradEl = document.getElementById("questionTranslation");
    // LA TRADUCTION NE DONNE PAS LA REPONSE (15 nov. 2026, interface-es/outils/traduction_apres.py) :
    // en espagnol, cuándo / cuando, pero / sino trahiraient wann / wenn, aber / sondern, que le
    // francais ne distingue pas. Ces exercices ne montrent leur traduction qu'apres la reponse.
    const tradApres = uiLang === "es" && !!ex.traductionApres_es;
    tradEl.textContent = (translation && !tradApres) ? tf("question_translation_label", { translation }) : "";
    tradEl.classList.toggle("hidden", !translation || tradApres);''')
r('''    answered = true;
    const enRattrapage = !!ex.estRattrapage;''',
  '''    answered = true;
    // La traduction gardee pour apres la reponse (voir loadExercise).
    if(uiLang === "es" && ex.traductionApres_es){
        const tradApres = texteTraduit(ex, "translation");
        const tradEl = document.getElementById("questionTranslation");
        if(tradApres && tradEl){
            tradEl.textContent = tf("question_translation_label", { translation: tradApres });
            tradEl.classList.remove("hidden");
        }
    }
    const enRattrapage = !!ex.estRattrapage;''')

if "--ecrire" in sys.argv:
    io.open(p, "w", encoding="utf-8", newline="").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))
    io.open(q, "w", encoding="utf-8", newline="").write(src)
    print("ecrit")
else:
    print("a blanc : rien n'est ecrit")
