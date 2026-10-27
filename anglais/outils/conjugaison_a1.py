# -*- coding: utf-8 -*-
"""Les feuilles de conjugaison A1 de l'anglais, au format de
espanol/datos/conjugaison.json : un tableau court, la forme entre [ ], le sens,
une astuce, et la serie d'exercices qui suit (grammaire_a1.py).
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

FEUILLES_A1 = [
 {"id": "be_present", "serie": "beEnExercises", "t": "To be au présent : I am, you are",
  "l": [["I [am] a student", "je suis étudiant"], ["you [are] late", "tu es en retard"],
        ["he · she [is] at home", "il · elle est à la maison"], ["we [are] friends", "nous sommes amis"],
        ["they [are] tired", "ils sont fatigués"], ["it [isn't] cold", "il ne fait pas froid"]],
  "a": "À l'oral, toujours contracté : I'm, you're, he's, we're, they're. La négation se colle : isn't, aren't. Avoir faim, froid, vingt ans : be hungry, be cold, be twenty."},
 {"id": "present_simple", "serie": "presentEnExercises", "t": "Le présent simple : I work, he works",
  "l": [["I [work] in Boston", "je travaille à Boston"], ["you [work] a lot", "tu travailles beaucoup"],
        ["he · she [works] at night", "il · elle travaille la nuit"], ["we [live] here", "nous habitons ici"],
        ["they [speak] English", "ils parlent anglais"], ["he [doesn't work] on Sundays", "il ne travaille pas le dimanche"]],
  "a": "Une seule terminaison : le -s de he, she, it. Négation et question avec do / does, et le verbe reste nu : I don't work, Does she work?"},
 {"id": "present_ing", "serie": "continuEnExercises", "t": "Le présent en -ing : I'm working",
  "l": [["I['m eating]", "je mange (en ce moment)"], ["you['re reading]", "tu lis (là, maintenant)"],
        ["he · she['s sleeping]", "il · elle dort"], ["we['re waiting]", "nous attendons"],
        ["they['re playing]", "ils jouent"], ["[Are] you [listening]?", "tu écoutes ?"]],
  "a": "Be + verbe en -ing, pour ce qui se passe maintenant. Le e muet tombe (make → making), certaines consonnes doublent (run → running). Pas de -ing avec like, want, know."},
 {"id": "can", "serie": "canEnExercises", "t": "Can : pouvoir, savoir faire",
  "l": [["I [can] swim", "je sais nager"], ["you [can] come", "tu peux venir"],
        ["he · she [can] drive", "il · elle sait conduire"], ["we [can't] stay", "nous ne pouvons pas rester"],
        ["they [can] help", "ils peuvent aider"], ["[Can] I sit here?", "je peux m'asseoir ici ?"]],
  "a": "Can ne change jamais : she can, sans -s. Le verbe qui suit reste nu, sans to : I can speak. Négation : can't."},
 {"id": "past_be", "serie": "passeEnExercises", "t": "To be au passé : was, were",
  "l": [["I [was] tired", "j'étais fatigué"], ["you [were] late", "tu étais en retard"],
        ["he · she [was] at home", "il · elle était à la maison"], ["we [were] in Boston", "nous étions à Boston"],
        ["they [were] happy", "ils étaient contents"], ["it [wasn't] cold", "il ne faisait pas froid"]],
  "a": "Deux formes seulement : was avec I, he, she, it ; were avec you, we, they. Négation : wasn't, weren't."},
 {"id": "past_simple", "serie": "passeEnExercises", "t": "Le prétérit : I worked, I went",
  "l": [["I [worked] yesterday", "j'ai travaillé hier"], ["you [played] tennis", "tu as joué au tennis"],
        ["he · she [went] home", "il · elle est rentré(e)"], ["we [saw] a movie", "nous avons vu un film"],
        ["they [had] lunch", "ils ont déjeuné"], ["I [didn't call] her", "je ne l'ai pas appelée"]],
  "a": "Réguliers : -ed (worked, played). Irréguliers à apprendre (went, saw, had). Une seule forme pour toutes les personnes. Négation et question avec did : I didn't go, Did you see it?"},
]
