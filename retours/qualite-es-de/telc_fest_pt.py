# -*- coding: utf-8 -*-
"""telc, l'oral : les 10 reponses modeles de la planification « une fete de fin
de cours » (PLAN.fest.tours) en portugais du Bresil, reprises de la table relue
du cahier « Preparar-se para o telc » (Wortando-Ebooks/preparer-telc-fr/textes/
pt.json, app.oral.PLAN.fest.tours). Ajoutees au dictionnaire anglais -> pt de
l'app (visuel/prototype/telc/langues/pt.json), cle = le texte anglais de oral.html.
Puis : node outils/langues.js construire pt (dans visuel/prototype/telc).

    python retours/qualite-es-de/telc_fest_pt.py
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(os.path.dirname(os.path.dirname(ICI)), "visuel", "prototype", "telc", "langues", "pt.json")

PT = {
    "Yes, good idea. After class everyone has time.":
        "Sim, boa ideia. Depois da aula, todo mundo tem tempo.",
    "The last day of the course is good, but after class a lot of people are tired. How about Friday evening? Then everyone can stay longer.":
        "O último dia do curso é bom, mas depois da aula muita gente está cansada. Que tal sexta à noite? Assim todo mundo pode ficar mais tempo.",
    "I'd rather go to the café. It's nice.":
        "Eu prefiro ir ao café. É bonito.",
    "A café is cosy, but for so many people it's expensive. I suggest we stay in the classroom. We can listen to music there too.":
        "Um café é aconchegante, mas para tanta gente é caro. Sugiro que a gente fique na sala de aula. Lá a gente também pode ouvir música.",
    "I'll bring a cake. I like baking.":
        "Eu levo um bolo. Gosto de fazer bolo.",
    "Agreed, everyone brings something. I'll bake a cake. But we should make a list, so that not everyone brings salad.":
        "Combinado, cada um leva alguma coisa. Eu faço um bolo. Mas a gente devia fazer uma lista, para que nem todo mundo leve salada.",
    "Music is good. A game is fun too.":
        "Música é bom. Um jogo também é divertido.",
    "I think music is great. We could also do a little quiz about our course, that would definitely be fun. Do you fancy writing the questions with me?":
        "Música, eu acho ótimo. A gente também poderia fazer um pequeno quiz sobre o nosso curso, com certeza vai ser divertido. Você topa escrever as perguntas comigo?",
    "Yes, flowers are good. I'll buy them.":
        "Sim, flores são uma boa ideia. Eu compro.",
    "I think flowers and a card are nice. I can buy the card, and everyone writes something in it. Will you collect the money for the flowers?":
        "Flores e um cartão, acho bonito. Eu posso comprar o cartão, e todo mundo escreve alguma coisa nele. Você junta o dinheiro para as flores?",
}

src = {e["en"] for e in json.load(io.open(os.path.join(os.path.dirname(F), "source.json"), encoding="utf-8"))}
assert set(PT) <= src, set(PT) - src
d = json.load(io.open(F, encoding="utf-8"))
n = 0
for en, pt in PT.items():
    if d.get(en) != pt:
        assert en not in d, en
        d[en] = pt
        n += 1
json.dump(d, io.open(F, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
io.open(F, "a", encoding="utf-8", newline="\n").write("\n")
print(n, "reponses ajoutees au dictionnaire pt")
