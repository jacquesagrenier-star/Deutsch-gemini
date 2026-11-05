# -*- coding: utf-8 -*-
"""Les 8 phrases de A-JACQUES-VOIX.md : leur texte change avec leur voix.
Accord de Jacques du 3 nov. 2026 (« Oui, fais les voix », decisions/DECISIONS.md).

Change le texte (phrase, question, options, sens et notes dans toutes les
langues) ; les voix se font ensuite :
  - allemand : python audio/manifest.py --ecrire, puis
    python retours/qualite-es-de/voix_relecture.py <manifeste-avant> --plafond 200
  - espagnol : python audio/generer_es.py --variante es|latam --niveaux A1,A2,B1,B2,C1
    --textes "<les sept textes>" (apres construire.py des trois scenes)

Deux ajustements a la table montree a Jacques, pour la coherence des scenes :
dans l'aeroport, Anna PART (« estuvo » la mettait au retour) -> « va a estar » ;
dans la chambre, c'est Anna qui fait sa valise (« cuando llegue Anna » n'allait
pas) -> « Mañana temprano todo tiene que estar ya guardado ».

    python retours/qualite-es-de/voix_jacques.py            # montre
    python retours/qualite-es-de/voix_jacques.py --ecrire   # applique
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
ECRIRE = "--ecrire" in sys.argv

# (fichier, q actuelle, {champ: (ancien, nouveau)}) ; « c » : {ancienne option: nouvelle}
QUESTIONS = [
    ("bibliothek.points.json", "___ wartest du? — Auf meine Freundin.", {
        "c": {"Worauf": "Auf wen", "Wofür": "Worauf", "Woran": "An wen"},
        "phrase": ("Worauf wartest du? — Auf meine Freundin.", "Auf wen wartest du? — Auf meine Freundin."),
        "sens": ("Qu'est-ce que tu attends ? — Mon amie.", "Qui attends-tu ? — Mon amie."),
        "n": ("Question sur une chose : <b>wo(r)</b> + préposition → wor<b>auf</b>.",
              "Question sur une personne : préposition + <b>wen</b> → <b>auf wen</b>. Pour une chose : wor<b>auf</b>."),
    }),
    ("espanol/familie.json", "La comida ___ en casa de los abuelos.", {
        "q": ("La comida ___ en casa de los abuelos.", "La fiesta ___ en casa de los abuelos."),
        "phrase": ("La comida es en casa de los abuelos.", "La fiesta es en casa de los abuelos."),
        "sens": ("Le repas a lieu chez les grands-parents.", "La fête a lieu chez les grands-parents."),
        "sens_en": ("The meal is at the grandparents' house.", "The party is at the grandparents' house."),
        "sens_pt": ("O almoço é na casa dos avós.", "A festa é na casa dos avós."),
        "sens_ar": ("الغداء في بيت الجدّين.", "الحفلة في بيت الجدّين."),
        "sens_de": ("Das Essen findet bei den Großeltern statt.", "Die Feier findet bei den Großeltern statt."),
        "n": ("Un événement a lieu → <b>ser</b> (« la comida es en… »).", "Un événement a lieu → <b>ser</b> (« la fiesta es en… »)."),
        "n_en": ("An event takes place → <b>ser</b> (“la comida es en…”).", "An event takes place → <b>ser</b> (“la fiesta es en…”)."),
        "n_pt": ("Um evento acontece → <b>ser</b> (“la comida es en…”).", "Um evento acontece → <b>ser</b> (“la fiesta es en…”)."),
        "n_ar": ("حدث يقع ← <b>ser</b> («la comida es en…»).", "حدث يقع ← <b>ser</b> («la fiesta es en…»)."),
        "n_de": ("Ein Ereignis findet statt → <b>ser</b> („la comida es en…“) — die Ausnahme bei Ortsangaben.",
                 "Ein Ereignis findet statt → <b>ser</b> („la fiesta es en…“) — die Ausnahme bei Ortsangaben."),
    }),
    ("espanol/flughafen.json", "Anna viaja a España ___ una semana.", {
        "q": ("Anna viaja a España ___ una semana.", "Anna va a estar en España ___ una semana."),
        "phrase": ("Anna viaja a España por una semana.", "Anna va a estar en España por una semana."),
        "sens": ("Anna part en Espagne pour une semaine.", "Anna va passer une semaine en Espagne."),
        "sens_en": ("Anna is travelling to Spain for a week.", "Anna is going to be in Spain for a week."),
        "sens_pt": ("Anna viaja para a Espanha por uma semana.", "Anna vai ficar na Espanha por uma semana."),
        "sens_ar": ("تسافر آنا إلى إسبانيا لمدّة أسبوع.", "ستبقى آنا في إسبانيا لمدّة أسبوع."),
        "sens_de": ("Anna reist für eine Woche nach Spanien.", "Anna wird eine Woche lang in Spanien sein."),
    }),
    ("espanol/flughafen.json", "El piloto ___ ese avión muchas veces.", {
        "q": ("El piloto ___ ese avión muchas veces.", "Este piloto ya ___ ese avión muchas veces."),
        "phrase": ("El piloto ha pilotado ese avión muchas veces.", "Este piloto ya ha pilotado ese avión muchas veces."),
        "sens": ("Le pilote a piloté cet avion de nombreuses fois.", "Ce pilote a déjà piloté cet avion de nombreuses fois."),
        "sens_en": ("The pilot has flown that plane many times.", "This pilot has already flown that plane many times."),
        "sens_pt": ("O piloto já pilotou esse avião muitas vezes.", "Este piloto já pilotou esse avião muitas vezes."),
        "sens_ar": ("قاد الطيّار تلك الطائرة مرّات كثيرة.", "قاد هذا الطيّار تلك الطائرة مرّات كثيرة من قبل."),
        "sens_de": ("Der Pilot hat dieses Flugzeug schon viele Male geflogen.", "Dieser Pilot hat dieses Flugzeug schon viele Male geflogen."),
        "n": ("Une expérience jusqu'à aujourd'hui (<b>muchas veces</b>) → pretérito perfecto.",
              "Une expérience jusqu'à aujourd'hui (<b>ya</b>, <b>muchas veces</b>) → pretérito perfecto."),
        "n_en": ("An experience up to today (<b>muchas veces</b>) → pretérito perfecto.",
                 "An experience up to today (<b>ya</b>, <b>muchas veces</b>) → pretérito perfecto."),
        "n_pt": ("Uma experiência até hoje (<b>muchas veces</b>) → pretérito perfecto.",
                 "Uma experiência até hoje (<b>ya</b>, <b>muchas veces</b>) → pretérito perfecto."),
        "n_ar": ("تجربة حتى اليوم (<b>muchas veces</b>) → pretérito perfecto.",
                 "تجربة حتى اليوم (<b>ya</b>، <b>muchas veces</b>) → pretérito perfecto."),
        "n_de": ("Eine Erfahrung bis heute (<b>muchas veces</b>) → pretérito perfecto.",
                 "Eine Erfahrung bis heute (<b>ya</b>, <b>muchas veces</b>) → pretérito perfecto."),
    }),
    ("espanol/geburtstag.json", "Las velas van a ___ apagadas enseguida.", {
        "q": ("Las velas van a ___ apagadas enseguida.", "Las velas van a ___ apagadas por Mark."),
        "phrase": ("Las velas van a ser apagadas enseguida.", "Las velas van a ser apagadas por Mark."),
        "sens": ("Les bougies vont être soufflées tout de suite.", "Les bougies vont être soufflées par Mark."),
        "sens_en": ("The candles are going to be blown out right away.", "The candles are going to be blown out by Mark."),
        "sens_pt": ("As velas vão ser apagadas agora mesmo.", "As velas vão ser apagadas pelo Mark."),
        "sens_ar": ("ستُطفأ الشموع حالاً.", "ستُطفأ الشموع على يد مارك."),
        "sens_de": ("Die Kerzen werden gleich ausgeblasen.", "Die Kerzen werden von Mark ausgeblasen."),
        "n": ("Passif d'action : <b>ser</b> + participe accordé (apagad<b>as</b>).",
              "Passif d'action, avec celui qui agit (<b>por Mark</b>) : <b>ser</b> + participe accordé (apagad<b>as</b>)."),
        "n_en": ("Action passive: <b>ser</b> + agreeing participle (apagad<b>as</b>).",
                 "Action passive, with the doer (<b>por Mark</b>): <b>ser</b> + agreeing participle (apagad<b>as</b>)."),
        "n_pt": ("Passiva de ação: <b>ser</b> + particípio concordado (apagad<b>as</b>).",
                 "Passiva de ação, com quem age (<b>por Mark</b>): <b>ser</b> + particípio concordado (apagad<b>as</b>)."),
        "n_ar": ("مبني للمجهول للفعل: <b>ser</b> + اسم المفعول بالمطابقة (apagad<b>as</b>).",
                 "مبني للمجهول للفعل مع الفاعل (<b>por Mark</b>): <b>ser</b> + اسم المفعول بالمطابقة (apagad<b>as</b>)."),
        "n_de": ("Vorgangspassiv: <b>ser</b> + angepasstes Partizip (apagad<b>as</b>) — wie „werden ausgeblasen“.",
                 "Vorgangspassiv mit Urheber (<b>por Mark</b>): <b>ser</b> + angepasstes Partizip (apagad<b>as</b>) — wie „werden von Mark ausgeblasen“."),
    }),
    ("espanol/schlafzimmer.json", "Todo tiene que ___ guardado hoy.", {
        "q": ("Todo tiene que ___ guardado hoy.", "Mañana temprano todo tiene que ___ ya guardado."),
        "phrase": ("Todo tiene que estar guardado hoy.", "Mañana temprano todo tiene que estar ya guardado."),
        "sens": ("Tout doit être rangé aujourd'hui.", "Demain matin, tout doit déjà être rangé."),
        "sens_en": ("Everything has to be packed away today.", "Early tomorrow, everything has to be packed away already."),
        "sens_pt": ("Tudo tem que estar guardado hoje.", "Amanhã cedo, tudo tem que já estar guardado."),
        "sens_ar": ("يجب أن يكون كل شيء محزوماً اليوم.", "صباح الغد يجب أن يكون كل شيء محزوماً."),
        "sens_de": ("Alles muss heute verstaut sein.", "Morgen früh muss alles schon verstaut sein."),
        "n": ("Le résultat attendu → <b>estar</b> + participe.", "Le résultat attendu (<b>ya</b>) → <b>estar</b> + participe."),
        "n_en": ("The expected result → <b>estar</b> + participle.", "The expected result (<b>ya</b>) → <b>estar</b> + participle."),
        "n_pt": ("O resultado esperado → <b>estar</b> + particípio.", "O resultado esperado (<b>ya</b>) → <b>estar</b> + particípio."),
        "n_ar": ("النتيجة المنتظرة ← <b>estar</b> + اسم المفعول.", "النتيجة المنتظرة (<b>ya</b>) ← <b>estar</b> + اسم المفعول."),
        "n_de": ("Das erwartete Ergebnis → <b>estar</b> + Partizip.", "Das erwartete Ergebnis (<b>ya</b>) → <b>estar</b> + Partizip."),
    }),
]

# Bibliotheque : la cle des traductions suit la phrase ; note (groupe questions) et sens
CLE_AVANT = "B1 | Worauf wartest du? — Auf meine Freundin."
CLE_APRES = "B1 | Auf wen wartest du? — Auf meine Freundin."
NOTE = {
    "en": "Asking about a person: preposition + <b>wen</b> → <b>auf wen</b>. For a thing: wor<b>auf</b>.",
    "pt": "Pergunta sobre uma pessoa: preposição + <b>wen</b> → <b>auf wen</b>. Para uma coisa: wor<b>auf</b>.",
    "ar": 'سؤال عن شخص: حرف الجر + <b>wen</b> ← <span lang="de"><b>auf wen</b></span>. وعن شيء: <span lang="de">wor<b>auf</b></span>.',
    "tr": "Bir kişi hakkında soru: edat + <b>wen</b> → <b>auf wen</b>. Bir şey için: wor<b>auf</b>.",
    "uk": "Питання про людину: прийменник + <b>wen</b> → <b>auf wen</b>. Про річ: wor<b>auf</b>.",
    "fa": 'پرسش دربارهٔ یک شخص: حرف اضافه + <b>wen</b> ← <span lang="de"><b>auf wen</b></span>. برای یک چیز: <span lang="de">wor<b>auf</b></span>.',
    "pl": "Pytanie o osobę: przyimek + <b>wen</b> → <b>auf wen</b>. O rzecz: wor<b>auf</b>.",
    "ru": "Вопрос о человеке: предлог + <b>wen</b> → <b>auf wen</b>. О предмете: wor<b>auf</b>.",
}
SENS = {
    "en": "Who are you waiting for? — For my friend.",
    "pt": "Quem você está esperando? — A minha amiga.",
    "ar": "من تنتظر؟ — أنتظر صديقتي.",
    "tr": "Kimi bekliyorsun? — Arkadaşımı.",
    "uk": "На кого ти чекаєш? — На свою подругу.",
    "fa": "منتظر چه کسی هستی؟ — منتظر دوستم.",
    "pl": "Na kogo czekasz? — Na moją przyjaciółkę.",
    "ru": "Кого ты ждёшь? — Свою подругу.",
}

# Donnees espagnoles : (fichier, ancien, nouveau), le texte doit y figurer une fois
DONNEES = [
    ("espanol/datos/temas.json", "Su contraargumento fue solido.", "Su contraargumento fue sólido."),
    ("espanol/vocabulario.json", "Su contraargumento fue solido.", "Su contraargumento fue sólido."),
    ("espanol/datos/adjetivos.json", "Guardaron una reunión secreta.", "Mantuvieron una reunión secreta."),
    ("espanol/vocabulario.json", "Guardaron una reunión secreta.", "Mantuvieron una reunión secreta."),
]

j = lambda v: json.dumps(v, ensure_ascii=False)


def main():
    raws, attendus, journal = {}, {}, []

    def charger(chemin):
        if chemin not in raws:
            raws[chemin] = io.open(chemin, encoding="utf-8", newline="").read()
            attendus[chemin] = json.loads(raws[chemin])
        return attendus[chemin]

    for f, q_avant, champs in QUESTIONS:
        chemin = os.path.join(PROTO, f)
        d = charger(chemin)
        qs = [q for c in d["couches"].values() if isinstance(c, dict) for q in c.get("qs", []) if q["q"] == q_avant]
        assert len(qs) == 1, (f, q_avant)
        q = qs[0]
        raw = raws[chemin]
        ancre = '"q": ' + j(q_avant)
        assert raw.count(ancre) == 1, (f, ancre)
        debut = raw.index(ancre)
        fin = raw.find('"q": ', debut + len(ancre))
        fin = len(raw) if fin < 0 else fin
        bloc = raw[debut:fin]
        for k, v in champs.items():
            if k == "c":
                for vieux, neuf in v.items():
                    assert vieux in q["c"], (f, k, vieux)
                q["c"] = [v.get(o, o) for o in q["c"]]
                # remplacements simultanes (Wofür -> Worauf ne doit pas etre repris)
                for n, (vieux, neuf) in enumerate(v.items()):
                    assert bloc.count(j(vieux)) == 1, (f, vieux)
                    bloc = bloc.replace(j(vieux), "\x00%d\x00" % n)
                for n, (vieux, neuf) in enumerate(v.items()):
                    bloc = bloc.replace("\x00%d\x00" % n, j(neuf))
                journal.append((f, "c", str(list(v)), str(q["c"])))
                continue
            vieux, neuf = v
            assert q[k] == vieux, (f, k, q[k])
            q[k] = neuf
            a, b = '"%s": %s' % (k, j(vieux)), '"%s": %s' % (k, j(neuf))
            assert bloc.count(a) == 1, (f, a[:60])
            bloc = bloc.replace(a, b)
            journal.append((f, k, vieux, neuf))
        raws[chemin] = raw[:debut] + bloc + raw[fin:]

    for l in NOTE:
        chemin = os.path.join(PROTO, "traductions", "bibliothek.%s.json" % l)
        d = charger(chemin)
        note, sens = d["questions"].pop(CLE_AVANT), d["sens"].pop(CLE_AVANT)
        raw = raws[chemin]
        for groupe, o, fr, trad in (("questions", note, QUESTIONS[0][2]["n"], NOTE[l]),
                                    ("sens", sens, QUESTIONS[0][2]["sens"], SENS[l])):
            assert o["fr"] == fr[0], (l, groupe, o["fr"])
            neuf = {"fr": fr[1], "trad": trad}
            vieux_bloc = "%s: {\n   \"fr\": %s,\n   \"trad\": %s\n  }" % (j(CLE_AVANT), j(o["fr"]), j(o["trad"]))
            neuf_bloc = "%s: {\n   \"fr\": %s,\n   \"trad\": %s\n  }" % (j(CLE_APRES), j(neuf["fr"]), j(neuf["trad"]))
            if vieux_bloc not in raw:
                vieux_bloc, neuf_bloc = (x.replace("\n", "\r\n") for x in (vieux_bloc, neuf_bloc))
            assert raw.count(vieux_bloc) == 1, (l, groupe)
            raw = raw.replace(vieux_bloc, neuf_bloc)
            journal.append(("bibliothek.%s" % l, groupe, o["trad"], trad))
        # l'ordre des cles est garde : on reconstruit l'attendu depuis le texte
        raws[chemin] = raw
        attendus[chemin] = None
        doc = json.loads(raw)
        assert doc["questions"][CLE_APRES] == {"fr": QUESTIONS[0][2]["n"][1], "trad": NOTE[l]}, l
        assert doc["sens"][CLE_APRES] == {"fr": QUESTIONS[0][2]["sens"][1], "trad": SENS[l]}, l
        assert CLE_AVANT not in raw, l

    for f, vieux, neuf in DONNEES:
        chemin = os.path.join(RACINE, f)
        charger(chemin)
        a, b = j(vieux), j(neuf)
        assert raws[chemin].count(a) == 1, (f, a)
        raws[chemin] = raws[chemin].replace(a, b)
        attendus[chemin] = None
        journal.append((f, "exemple", vieux, neuf))

    for chemin, raw in raws.items():
        doc = json.loads(raw)
        if attendus[chemin] is not None:
            assert doc == attendus[chemin], "le texte brut ne donne pas le document attendu : " + chemin
    for f, k, a, b in journal:
        print("%s %s\n   - %s\n   + %s" % (f, k, a[:110], b[:110]))
    print("\n%d changements dans %d fichiers" % (len(journal), len(raws)))
    if ECRIRE:
        for chemin, raw in raws.items():
            io.open(chemin, "w", encoding="utf-8", newline="").write(raw)
        print("ecrit. Puis : construire.py bibliothek familie flughafen geburtstag schlafzimmer")


if __name__ == "__main__":
    main()
