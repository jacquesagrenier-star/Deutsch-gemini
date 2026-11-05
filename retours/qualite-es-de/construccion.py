# -*- coding: utf-8 -*-
"""verbos.json : les 33 notes « construccion » des verbes espagnols etaient en
anglais, et s'affichaient telles quelles dans toutes les langues d'interface.
Recommandation de la relecture appliquee le 4 nov. 2026 (« le controle de la
qualite, tu peux continuer ») : construccion_fr, _en, _pt, _ar, _de.

Le champ nu « construccion » garde l'anglais : c'est ce qu'affiche une page
qui ne connait pas encore les champs par langue. L'app choisit la langue par
texteTraduit(card, "construccion") (index.html, meme publication ou suivante).

Pour ahondar, incidir et aludir, la note ne donnait que la construction : le
sens est ajoute dans toutes les langues, l'anglais compris.

    python retours/qualite-es-de/construccion.py            # montre
    python retours/qualite-es-de/construccion.py --ecrire   # applique
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
F = os.path.join(RACINE, "espanol", "datos", "verbos.json")

# mot : (fr, pt, ar, de[, en remplace])
NOTES = {
    "traer": ("traer = vers celui qui parle ; llevar = en s'éloignant de lui.",
              "traer = em direção a quem fala; llevar = para longe dele.",
              "traer نحو المتكلّم، وllevar بعيدًا عنه.",
              "traer = zum Sprecher hin; llevar = vom Sprecher weg."),
    "acabar": ("acabar DE + infinitif = venir de faire quelque chose.",
               "acabar DE + infinitivo = ter acabado de fazer algo.",
               "acabar DE + المصدر = فعل الشيء للتوّ.",
               "acabar DE + Infinitiv = gerade etwas getan haben."),
    "acostumbrarse": ("acostumbrarse A algo — le a est obligatoire.",
                      "acostumbrarse A algo — o a é obrigatório.",
                      "acostumbrarse A algo — حرف a إلزامي.",
                      "acostumbrarse A algo — das a ist Pflicht."),
    "apetecer": ("Comme gustar : la chose désirée est le SUJET — me apetece un café, pas yo apetezco.",
                 "Como gustar: a coisa desejada é o SUJEITO — me apetece un café, não yo apetezco.",
                 "مثل gustar: الشيء المرغوب فيه هو الفاعل — me apetece un café، وليس yo apetezco.",
                 "Wie gustar: Das Gewünschte ist das SUBJEKT — me apetece un café, nicht yo apetezco."),
    "bastar": ("Impersonnel : basta CON + nom ou infinitif.",
               "Impessoal: basta CON + substantivo ou infinitivo.",
               "غير شخصي: basta CON + اسم أو مصدر.",
               "Unpersönlich: basta CON + Nomen oder Infinitiv."),
    "dejar": ("dejar DE + infinitif = arrêter de faire quelque chose.",
              "dejar DE + infinitivo = parar de fazer algo.",
              "dejar DE + المصدر = التوقّف عن فعل شيء.",
              "dejar DE + Infinitiv = mit etwas aufhören."),
    "faltar": ("Comme gustar : ce qui manque est le SUJET — me falta tiempo.",
               "Como gustar: o que falta é o SUJEITO — me falta tiempo.",
               "مثل gustar: الشيء الناقص هو الفاعل — me falta tiempo.",
               "Wie gustar: Das Fehlende ist das SUBJEKT — me falta tiempo."),
    "fijar": ("fijarse EN algo = remarquer quelque chose.",
              "fijarse EN algo = reparar em algo.",
              "fijarse EN algo = أن يلاحظ شيئًا.",
              "fijarse EN algo = etwas bemerken."),
    "ocupar": ("ocuparse DE algo = s'occuper de quelque chose.",
               "ocuparse DE algo = cuidar de algo.",
               "ocuparse DE algo = أن يهتمّ بشيء.",
               "ocuparse DE algo = sich um etwas kümmern."),
    "soler": ("soler + infinitif remplace l'adverbe « d'habitude ». Seulement au présent et à l'imparfait : soler n'a pas de passé simple.",
              "soler + infinitivo substitui o advérbio « geralmente ». Só no presente e no imperfeito: soler não tem pretérito perfeito.",
              "soler + المصدر يحلّ محلّ ظرف «عادةً». في المضارع والماضي الناقص فقط: لا ماضي تامًّا لـ soler.",
              "soler + Infinitiv ersetzt das Adverb „gewöhnlich“. Nur im Präsens und im Imperfekt — soler hat kein Pretérito."),
    "tratar": ("tratar DE + nom = parler de, porter sur ; tratar DE + infinitif = essayer de.",
               "tratar DE + substantivo = tratar de (um assunto); tratar DE + infinitivo = tentar.",
               "tratar DE + اسم = يتناول موضوعًا؛ tratar DE + مصدر = يحاول.",
               "tratar DE + Nomen = von etwas handeln; tratar DE + Infinitiv = versuchen, etwas zu tun."),
    "alegrar": ("alegrarse DE algo = se réjouir de quelque chose.",
                "alegrarse DE algo = alegrar-se com algo.",
                "alegrarse DE algo = أن يفرح بشيء.",
                "alegrarse DE algo = sich über etwas freuen."),
    "atreverse": ("atreverse A + infinitif. Jamais sans le pronom.",
                  "atreverse A + infinitivo. Nunca sem o pronome.",
                  "atreverse A + المصدر. لا يُستعمل أبدًا بلا الضمير.",
                  "atreverse A + Infinitiv. Nie ohne das Pronomen."),
    "gustar": ("La chose aimée est le SUJET : me gustan los libros, jamais yo gusto. La personne est un complément d'objet indirect.",
               "A coisa de que se gosta é o SUJEITO: me gustan los libros, nunca yo gusto. A pessoa é objeto indireto.",
               "الشيء المحبوب هو الفاعل: me gustan los libros، وليس أبدًا yo gusto. والشخص مفعول به غير مباشر.",
               "Das Gemochte ist das SUBJEKT: me gustan los libros, nie yo gusto. Die Person ist indirektes Objekt — wie „mir gefallen die Bücher“."),
    "interesar": ("Même construction que gustar : me interesa el tema.",
                  "Mesma construção de gustar: me interesa el tema.",
                  "البناء نفسه كما في gustar: me interesa el tema.",
                  "Gleiche Konstruktion wie gustar: me interesa el tema."),
    "temer": ("temer que + SUBJONCTIF quand la crainte est réelle.",
              "temer que + SUBJUNTIVO quando o medo é real.",
              "temer que + الـ subjuntivo حين يكون الخوف حقيقيًّا.",
              "temer que + SUBJUNTIVO, wenn die Befürchtung echt ist."),
    "acordarse": ("acordarse DE algo. Sans le pronom, acordar veut dire se mettre d'accord sur quelque chose — un autre verbe.",
                  "acordarse DE algo. Sem o pronome, acordar significa combinar algo — outro verbo.",
                  "acordarse DE algo. ومن دون الضمير يعني acordar الاتّفاق على شيء — وهو فعل آخر.",
                  "acordarse DE algo. Ohne Pronomen heißt acordar „etwas vereinbaren“ — ein anderes Verb."),
    "sugerir": ("sugerir que + SUBJONCTIF : sugiero que hablemos.",
                "sugerir que + SUBJUNTIVO: sugiero que hablemos.",
                "sugerir que + الـ subjuntivo: sugiero que hablemos.",
                "sugerir que + SUBJUNTIVO: sugiero que hablemos."),
    "asegurar": ("asegurarse DE que + indicatif = s'assurer que.",
                 "asegurarse DE que + indicativo = certificar-se de que.",
                 "asegurarse DE que + صيغة الإخبار = أن يتأكّد من أنّ.",
                 "asegurarse DE que + Indikativ = sich vergewissern, dass."),
    "consistir": ("Toujours consistir EN, jamais de.",
                  "Sempre consistir EN, nunca de.",
                  "دائمًا consistir EN، وليس de أبدًا.",
                  "Immer consistir EN, nie de."),
    "convencer": ("convencer A ALGUIEN DE algo, ou de que + subjonctif.",
                  "convencer A ALGUIEN DE algo, ou de que + subjuntivo.",
                  "convencer A ALGUIEN DE algo، أو de que + الـ subjuntivo.",
                  "convencer A ALGUIEN DE algo, oder de que + Subjuntivo."),
    "merecer": ("merecer la pena = valoir la peine.",
                "merecer la pena = valer a pena.",
                "merecer la pena = يستحقّ العناء.",
                "merecer la pena = sich lohnen."),
    "valer": ("valer la pena = valoir la peine ; ¿vale? = d'accord ?",
              "valer la pena = valer a pena; ¿vale? = combinado?",
              "valer la pena = يستحقّ العناء؛ ¿vale? = اتّفقنا؟",
              "valer la pena = sich lohnen; ¿vale? = okay?"),
    "agradecer": ("agradecer ALGO A ALGUIEN — pas de préposition devant la chose : agradezco la ayuda, pas por la ayuda.",
                  "agradecer ALGO A ALGUIEN — sem preposição antes da coisa: agradezco la ayuda, não por la ayuda.",
                  "agradecer ALGO A ALGUIEN — بلا حرف جرّ قبل الشيء: agradezco la ayuda، وليس por la ayuda.",
                  "agradecer ALGO A ALGUIEN — keine Präposition vor der Sache: agradezco la ayuda, nicht por la ayuda."),
    "impedir": ("impedir que + SUBJONCTIF : impidió que saliéramos.",
                "impedir que + SUBJUNTIVO: impidió que saliéramos.",
                "impedir que + الـ subjuntivo: impidió que saliéramos.",
                "impedir que + SUBJUNTIVO: impidió que saliéramos."),
    "permitir": ("permitir que + SUBJONCTIF : permite que entren.",
                 "permitir que + SUBJUNTIVO: permite que entren.",
                 "permitir que + الـ subjuntivo: permite que entren.",
                 "permitir que + SUBJUNTIVO: permite que entren."),
    "rogar": ("rogar que + SUBJONCTIF. Se ruega… est la formule habituelle des avis au public.",
              "rogar que + SUBJUNTIVO. Se ruega… é a fórmula habitual dos avisos ao público.",
              "rogar que + الـ subjuntivo. وSe ruega… هي الصيغة المعتادة في الإعلانات العامّة.",
              "rogar que + SUBJUNTIVO. Se ruega… ist die übliche Formel auf öffentlichen Aushängen („Es wird gebeten …“)."),
    "contar": ("contar CON alguien = compter sur quelqu'un.",
               "contar CON alguien = contar com alguém.",
               "contar CON alguien = أن يعتمد على أحد.",
               "contar CON alguien = auf jemanden zählen."),
    "dedicarse": ("¿A qué te dedicas? est la façon habituelle de demander à quelqu'un son métier.",
                  "¿A qué te dedicas? é o jeito habitual de perguntar a profissão de alguém.",
                  "¿A qué te dedicas? هي الطريقة المعتادة للسؤال عن مهنة أحدهم.",
                  "¿A qué te dedicas? ist die übliche Frage nach dem Beruf."),
    "rendir": ("rendirse = abandonner, se rendre ; rendir cuentas = rendre des comptes.",
               "rendirse = desistir, render-se; rendir cuentas = prestar contas.",
               "rendirse = يستسلم؛ rendir cuentas = يقدّم الحساب.",
               "rendirse = aufgeben; rendir cuentas = Rechenschaft ablegen."),
    "ahondar": ("ahondar en algo = approfondir quelque chose.",
                "ahondar en algo = aprofundar algo.",
                "ahondar en algo = يتعمّق في شيء.",
                "ahondar en algo = etwas vertiefen.",
                "ahondar en algo = to go deeper into something."),
    "incidir": ("incidir en algo = insister sur quelque chose.",
                "incidir en algo = insistir em algo.",
                "incidir en algo = يُلحّ على شيء، يركّز عليه.",
                "incidir en algo = etwas betonen, auf etwas eingehen.",
                "incidir en algo = to stress something, to dwell on it."),
    "aludir": ("aludir a algo = faire allusion à quelque chose.",
               "aludir a algo = fazer alusão a algo.",
               "aludir a algo = يُلمّح إلى شيء.",
               "aludir a algo = auf etwas anspielen.",
               "aludir a algo = to allude to something."),
}

raw = io.open(F, encoding="utf-8", newline="").read()
d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + "\n" == raw, "mise en forme inattendue"
vus = set()
for niv, liste in d.items():
    if not isinstance(liste, list):
        continue
    for v in liste:
        if not v.get("construccion"):
            continue
        n = NOTES[v["mot"]]
        vus.add(v["mot"])
        fr, pt, ar, de = n[:4]
        en = n[4] if len(n) > 4 else v["construccion"]
        if len(n) > 4:
            v["construccion"] = en
        v["construccion_fr"], v["construccion_en"], v["construccion_pt"] = fr, en, pt
        v["construccion_ar"], v["construccion_de"] = ar, de
        print("%-14s %s\n%-14s %s" % (v["mot"], en, "", fr))
assert vus == set(NOTES), set(NOTES) - vus
print("\n%d notes, cinq langues" % len(vus))
if "--ecrire" in sys.argv:
    io.open(F, "w", encoding="utf-8", newline="").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("ecrit")
