# -*- coding: utf-8 -*-
"""Deuxieme passe des signalements de scenes (relecture complete, 3 nov. 2026) :
ceux que scenes_relecture.py laissait « a la main », tries un par un.

Ne change AUCUNE phrase espagnole ni allemande (elles ont une voix) : seulement
des options d'exercice (un distracteur qui donnait une seconde phrase juste
devient une forme fautive), des notes, des sens et des traductions.
Les cas qui demandent une phrase nouvelle, donc une voix, restent a Jacques
(decision « voix » dans triage.json).

    python retours/qualite-es-de/scenes_relecture2.py            # montre
    python retours/qualite-es-de/scenes_relecture2.py --ecrire   # applique
Puis construire.py <scene> pour chaque scene touchee.
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
ECRIRE = "--ecrire" in sys.argv

# --- Espagnol : (scene, niveau, rang, champ, ancien, nouveau) ---------------
# champ « c » : l'ancien et le nouveau sont une option de la liste.
FUTUR = {
    "n": ("supposition sur le présent", "Ici, le <b>futur</b> annonce ce qui va se passer, avec une idée de probabilité."),
    "n_en": ("guess about the present", "Here the <b>future</b> says what is going to happen, with a sense of probability."),
    "n_pt": ("suposição sobre o presente", "Aqui o <b>futuro</b> anuncia o que vai acontecer, com uma ideia de probabilidade."),
    "n_ar": ("افتراض بشأن الحاضر", "هنا يعلن <b>المستقبل</b> ما سيحدث، مع معنى الاحتمال."),
    "n_de": ("Vermutung über die Gegenwart", "Hier kündigt das <b>futuro</b> an, was geschehen wird — mit einer Vermutung, wie „wird wohl …“ im Deutschen."),
}
# Les C1 dont la phrase parle de l'AVENIR (« en dos días », « hasta mañana »…)
# alors que la note enseignait une supposition sur le present.
SCENES_FUTUR = ("apotheke", "buergeramt", "fahrradwerkstatt", "geburtstag", "schlafzimmer", "waschsalon", "winter")

ES = [
    # prep. + que sans article est admis (RAE) : « que » etait une 2e reponse juste
    ("bibliothek", "B2", 2, "c", "que", "lo que"),
    ("buero", "B2", 2, "c", "que", "lo que"),
    ("schlafzimmer", "B2", 5, "c", "que", "lo que"),
    ("strand", "B2", 2, "c", "que", "lo que"),
    ("buero", "B1", 5, "c", "llama", "llamar"),          # usted : juste aussi
    ("camping", "B1", "¿___ a apagar el fuego luego?", "c", "Va", "Vaya"),
    ("friseur", "B1", 4, "c", "su", "la"),               # « se pone su abrigo » juste
    ("friseur", "B1", 4, "c", "un", "lo"),
    ("klassenzimmer", "C1", 0, "c", "quieren", "tienen de"),
    ("kreuzung", "C1", 2, "c", "cruzaría", "habrá cruzado"),
    ("restaurant", "B2", 1, "c", "el", "los"),           # « el dulce » existe
    ("schlafzimmer", "B1", 7, "c", "hace", "hizo"),      # « Mañana hace calor » juste
    ("stadtplatz", "B1", 1, "c", "cerca", "encima"),
    ("ubahn", "B1", 5, "c", "pero", "sino"),             # « no canta, pero toca » juste
    ("waschsalon", "B1", 4, "c", "usa", "usando"),       # quizás + indicatif admis
    ("waschsalon", "B1", 4, "c", "usará", "usado"),
    ("buergeramt", "B2", 2, "c", "llegó", "llegara"),    # « llegó antes que » juste
    ("buergeramt", "B2", 2, "n", "Antériorité (<b>antes que</b>) → pluscuamperfecto.",
     "Arrivée avant un autre moment du passé → <b>pluscuamperfecto</b> : había llegado."),
    ("buergeramt", "B2", 2, "n_en", "Anteriority (<b>antes que</b>) → pluscuamperfecto.",
     "Arrived before another point in the past → <b>pluscuamperfecto</b>: había llegado."),
    ("buergeramt", "B2", 2, "n_pt", "Anterioridade (<b>antes que</b>) → pluscuamperfecto.",
     "Chegada antes de outro momento do passado → <b>pluscuamperfecto</b>: había llegado."),
    ("buergeramt", "B2", 2, "n_ar", "الأسبقية (<b>antes que</b>) → pluscuamperfecto.",
     "وصول قبل لحظة أخرى في الماضي → <b>pluscuamperfecto</b>: había llegado."),
    ("buergeramt", "B2", 2, "n_de", "Vorzeitigkeit (<b>antes que</b>) → pluscuamperfecto.",
     "Ankunft vor einem anderen Zeitpunkt der Vergangenheit → <b>pluscuamperfecto</b>: había llegado."),
    # « Debe ser de uno de los invitados » est juste (deber = probabilite)
    ("wohnzimmer", "C1", 1, "c", "Debe", "Sabe"),
    ("wohnzimmer", "C1", 1, "n", "<b>podría</b> = c'est possible, sans preuve. <b>debe</b> serait une certitude.",
     "<b>podría</b> = c'est possible, sans preuve."),
    ("wohnzimmer", "C1", 1, "n_en", "<b>podría</b> = it's possible, with no proof. <b>debe</b> would be a certainty.",
     "<b>podría</b> = it's possible, with no proof."),
    ("wohnzimmer", "C1", 1, "n_pt", "<b>podría</b> = é possível, sem prova. <b>debe</b> seria uma certeza.",
     "<b>podría</b> = é possível, sem prova."),
    ("wohnzimmer", "C1", 1, "n_ar", "<b>podría</b> = ممكن، بلا دليل. أما <b>debe</b> فتكون يقيناً.",
     "<b>podría</b> = ممكن، بلا دليل."),
    ("wohnzimmer", "C1", 1, "n_de", "<b>podría</b> = möglich, ohne Beweis. <b>debe</b> wäre eine Gewissheit.",
     "<b>podría</b> = möglich, ohne Beweis."),
    # sens
    ("waschsalon", "C1", 2, "sens", "Il doit être prêt dans une heure.", "Elle sera sans doute prête dans une heure."),
    ("waschsalon", "C1", 2, "sens_ar", "على الأرجح يجهز خلال ساعة.", "على الأرجح ستكون جاهزة خلال ساعة."),
    ("schlafzimmer", "C1", 2, "sens", "Elle doit partir demain tôt.", "Elle partira sans doute demain tôt."),
    ("kleidergeschaeft", "C1", 0, "sens_pt", "Ela deve ter gostado do suéter.", "Ela deve gostar do suéter."),
]

# --- Traductions des scenes allemandes : (fichier, cle, ancien, nouveau) -----
# Remplacement d'un MORCEAU du champ « trad » (ou « fr ») de la paire <cle>.
TR = [
    ("bauernhof.fa", "alt", "trad", "عمویش بستهٔ کاهی را می‌برد", "عمویش بسته‌ای کاه می‌برد"),
    ("bibliothek.ru", "B1 | Worauf wartest du? — Auf meine Freundin.", "trad", "Чего ты ждёшь?", "Кого ты ждёшь?"),
    ("bibliothek.tr", "B1 | Worauf wartest du? — Auf meine Freundin.", "trad", "Neyi bekliyorsun?", "Kimi bekliyorsun?"),
    ("bibliothek.uk", "B1 | Worauf wartest du? — Auf meine Freundin.", "trad", "На що ти чекаєш?", "На кого ти чекаєш?"),
    ("geburtstag.tr", "alt", "trad", "bir kız arkadaşı alkışlıyor", "bir kadın arkadaşı alkışlıyor"),
    ("markt-obst-sued.fa", "C1 | Hätte Anna mehr Zeit, würde sie eine Ananas kaufen und schälen.", "trad",
     "می‌خرید و پوست می‌کند.", "می‌خرید و آن را پوست می‌کرد."),
    ("museum.uk", "alt", "trad", "в музеї дощової неділі в Берліні", "в музеї в Берліні в дощову неділю"),
    ("park.fa", "alt", "trad", "مردی که روی نیمکت روزنامه می‌خواند", "مردی که روی نیمکت مطالعه می‌کند"),
    ("stadtplatz.ar", "alt", "trad", "الكنيسة القرميدية", "الكنيسة المبنيّة بالآجر"),
    ("stadtplatz.ru", "alt", "trad", "маленькой рыжей собачкой", "маленькой коричневой собачкой"),
    ("stadtplatz.uk", "alt", "trad", "маленького рудого песика", "маленького коричневого песика"),
    ("umzug.ar", "alt", "trad", "فيه مطرقة ومثقاب وبيتزا في علبتها وعلبتا مشروب حمراوان",
     "فيه مطرقة ومثقاب، وبيتزا في علبتها، وعلبتا مشروب حمراوان"),
    ("weihnachtsmarkt.tr", "alt", "trad", "simit tezgâhı", "pretzel tezgâhı"),
]
# « Das Mädchen zeigt auf das Regal — es muss Schokolade haben wollen » :
# deduction au PRESENT ; le sens francais et ses huit traductions etaient au passe.
CHOCO = "C1 | Es muss Schokolade haben wollen."
CHOCO_FR = ("Elle a dû vouloir du chocolat.", "Elle doit vouloir du chocolat.")
CHOCO_TR = {
    "ar": ("لا بدّ أنها أرادت شوكولاتة.", "لا بدّ أنها تريد شوكولاتة."),
    "en": ("She must have wanted chocolate.", "She must want chocolate."),
    "fa": ("او حتماً شکلات می‌خواسته است.", "او حتماً شکلات می‌خواهد."),
    "pl": ("Musiała chcieć czekolady.", "Ona na pewno chce czekolady."),
    "pt": ("Ela deve ter querido chocolate.", "Ela deve querer chocolate."),
    "ru": ("Она, должно быть, хотела шоколада.", "Она, должно быть, хочет шоколада."),
    "tr": ("Çikolata istemiş olmalı.", "Çikolata istiyor olmalı."),
    "uk": ("Вона, мабуть, хотіла шоколаду.", "Вона, мабуть, хоче шоколаду."),
}
for l, (a, b) in CHOCO_TR.items():
    TR.append(("supermarkt." + l, CHOCO, "fr", CHOCO_FR[0], CHOCO_FR[1]))
    TR.append(("supermarkt." + l, CHOCO, "trad", a, b))

# Decision de triage par fichier et champ (les autres « scene » passent a « fait »)
ECARTES = {
    ("arztpraxis.json", "couches.B1.qs[7].c"): "la scène montre Mark pieds nus et la note le dit : « puesto » est exclu par l'image",
    ("camping.json", "couches.B1.qs[1].c"): "la scène montre les deux campeurs et la note dit « Eux » : va et vamos sont exclus par l'image",
}
VOIX = {
    "familie.json": "« La comida es en casa… » : « está » reste juste ; seule une phrase nouvelle (voix) garde la leçon ser/estar",
    "flughafen.json": "por/para et pilotaba : seule une phrase nouvelle (voix) lève l'ambiguïté en gardant la leçon",
    "geburtstag.json": "ser/estar apagadas : seule une phrase nouvelle (voix) garde la leçon",
    "schlafzimmer.json|couches.B2.qs[4]": "ser/estar guardado : seule une phrase nouvelle (voix) garde la leçon",
}
A_TRANCHER = {"musik.ar.json": "l'arabe rend Akkord par « وتر » (corde) dans toute la scène : le terme juste (تآلف ? كورد ?) demande un arabophone"}


def anchor(raw, q):
    a = '"q": ' + json.dumps(q["q"], ensure_ascii=False)
    assert raw.count(a) == 1, "question introuvable ou repetee : " + a[:60]
    return raw.index(a)


def main():
    touches, journal, raws, docs = set(), [], {}, {}

    def charger(chemin):
        if chemin not in raws:
            raws[chemin] = io.open(chemin, encoding="utf-8", newline="").read()
            docs[chemin] = json.loads(raws[chemin])
        return docs[chemin]

    def remplacer_apres(chemin, debut, vieux, neuf):
        raw = raws[chemin]
        p = raw.index(vieux, debut)
        raws[chemin] = raw[:p] + neuf + raw[p + len(vieux):]

    es = list(ES)
    for s in SCENES_FUTUR:
        q = json.load(io.open(os.path.join(PROTO, "espanol", s + ".json"), encoding="utf-8"))["couches"]["C1"]["qs"][2]
        for k, (marque, neuf) in FUTUR.items():
            assert marque in q[k], (s, k, q[k])
            es.append((s, "C1", 2, k, q[k], neuf))
    for s, niv, i, champ, vieux, neuf in es:
        chemin = os.path.join(PROTO, "espanol", s + ".json")
        d = charger(chemin)
        qs = d["couches"][niv]["qs"]
        if isinstance(i, str):
            i = [n for n, q in enumerate(qs) if q["q"] == i][0]
        q = qs[i]
        debut = anchor(raws[chemin], q)
        if champ == "c":
            assert vieux in q["c"] and neuf not in q["c"], (s, niv, i, q["c"])
            q["c"][q["c"].index(vieux)] = neuf
            remplacer_apres(chemin, debut, json.dumps(vieux, ensure_ascii=False), json.dumps(neuf, ensure_ascii=False))
        else:
            assert q[champ] == vieux, (s, niv, i, champ, q[champ])
            q[champ] = neuf
            remplacer_apres(chemin, debut, '"%s": %s' % (champ, json.dumps(vieux, ensure_ascii=False)),
                            '"%s": %s' % (champ, json.dumps(neuf, ensure_ascii=False)))
        touches.add(chemin)
        journal.append({"fichier": "visuel/prototype/espanol/%s.json" % s, "champ": "couches.%s.qs[%d].%s" % (niv, i, champ),
                        "avant": vieux, "apres": neuf})

    for f, cle, champ, vieux, neuf in TR:
        chemin = os.path.join(PROTO, "traductions", f + ".json")
        d = charger(chemin)
        o = d["champs" if cle == "alt" else "sens"][cle]  # le sens, pas la question
        assert o[champ].count(vieux) == 1, (f, cle, champ, o[champ][:80])
        avant = o[champ]
        o[champ] = avant.replace(vieux, neuf)
        a, b = json.dumps(avant, ensure_ascii=False), json.dumps(o[champ], ensure_ascii=False)
        assert raws[chemin].count(a) == 1, (f, a[:60])
        raws[chemin] = raws[chemin].replace(a, b)
        touches.add(chemin)
        journal.append({"fichier": "visuel/prototype/traductions/%s.json" % f, "champ": "%s.%s" % (cle, champ),
                        "avant": avant, "apres": o[champ]})

    chemin = os.path.join(PROTO, "supermarkt.points.json")
    d = charger(chemin)
    q = [q for q in d["couches"]["C1"]["qs"] if q.get("phrase") == CHOCO.split(" | ")[1]][0]
    assert q["sens"] == CHOCO_FR[0]
    q["sens"] = CHOCO_FR[1]
    a, b = '"sens": ' + json.dumps(CHOCO_FR[0], ensure_ascii=False), '"sens": ' + json.dumps(CHOCO_FR[1], ensure_ascii=False)
    assert raws[chemin].count(a) == 1
    raws[chemin] = raws[chemin].replace(a, b)
    touches.add(chemin)
    journal.append({"fichier": "visuel/prototype/supermarkt.points.json", "champ": "couches.C1.sens", "avant": CHOCO_FR[0], "apres": CHOCO_FR[1]})

    for chemin in touches:
        assert json.loads(raws[chemin]) == docs[chemin], "le texte brut ne donne pas le document attendu : " + chemin
    for j in journal:
        print("%s %s\n   - %s\n   + %s" % (j["fichier"].split("/")[-1], j["champ"], str(j["avant"])[:110], str(j["apres"])[:110]))
    print("\n%d corrections dans %d fichiers" % (len(journal), len(touches)))
    if not ECRIRE:
        return
    for chemin in touches:
        io.open(chemin, "w", encoding="utf-8", newline="").write(raws[chemin])

    sys.argv = sys.argv[:1]
    sys.path.insert(0, ICI)
    import verdicts as V
    T = json.load(io.open(os.path.join(ICI, "triage.json"), encoding="utf-8"))
    vs = {v["cle"]: v for v in V.verdicts(os.environ["TEMP"] + "/claude/qualite/complet")}
    compte = {}
    for cle, t in T.items():
        if t.get("decision") != "scene":
            continue
        v = vs.get(cle, {})
        base, champ = os.path.basename(v.get("fichier", "")), v.get("champ", "")
        dec, raison = "fait", "corrigé à la source de la scène (scenes_relecture2.py)"
        for (b, c), r in ECARTES.items():
            if base == b and champ.startswith(c):
                dec, raison = "ecarter", r
        for k, r in VOIX.items():
            b, _, c = k.partition("|")
            if base == b and champ.startswith(c):
                dec, raison = "voix", r
        if base in A_TRANCHER:
            dec, raison = "trancher", A_TRANCHER[base]
        if "Worauf wartest du" in champ:
            raison += " -- la phrase allemande elle-même (« Worauf » pour une personne) reste à Jacques : voix"
        t["decision"] = dec
        t["raison"] = (t.get("raison") or "") + " -- " + raison
        compte[dec] = compte.get(dec, 0) + 1
    json.dump(T, io.open(os.path.join(ICI, "triage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    p = os.path.join(ICI, "corrections-scenes.json")
    ancien = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else []
    json.dump(ancien + journal, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("triage :", compte)
    print("scenes a reconstruire :", " ".join(sorted({os.path.basename(c).split(".")[0] for c in touches})))


if __name__ == "__main__":
    main()
