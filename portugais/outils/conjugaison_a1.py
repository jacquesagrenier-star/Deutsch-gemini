# -*- coding: utf-8 -*-
"""Les feuilles de conjugaison A1 du portugais, au format de
espanol/datos/conjugaison.json : un tableau court, la forme entre [ ], le sens,
une astuce, et la serie d'exercices qui suit (grammaire_a1.py).
SOURCE : on corrige ici, puis python portugais/outils/construire.py.
"""

FEUILLES_A1 = [
 {"id": "ser_estar", "serie": "serEstarPtExercises", "t": "Ser et estar au présent",
  "l": [["eu [sou] · eu [estou]", "je suis"], ["tu [és] · tu [estás]", "tu es"],
        ["ele · ela [é] · [está]", "il · elle est"], ["nós [somos] · [estamos]", "nous sommes"],
        ["eles · vocês [são] · [estão]", "ils sont · vous êtes"], ["[Está] frio.", "il fait froid"]],
  "a": "Ser pour ce qu'on est (origine, métier, caractère, l'heure), estar pour comment ou où l'on est en ce moment. Le temps qu'il fait passe par estar."},
 {"id": "presente_ar", "serie": "presentePtExercises", "t": "Le présent des verbes en -ar : falar",
  "l": [["eu [falo]", "je parle"], ["tu [falas]", "tu parles"], ["ele · você [fala]", "il parle · vous parlez"],
        ["nós [falamos]", "nous parlons"], ["eles · vocês [falam]", "ils parlent · vous parlez"],
        ["[Moro] em Lisboa.", "j'habite à Lisbonne"]],
  "a": "La terminaison dit qui parle : on omet souvent le pronom (Falo português). Você et o senhor prennent la forme de ele."},
 {"id": "presente_er_ir", "serie": "presentePtExercises", "t": "Le présent en -er et -ir : comer, partir",
  "l": [["eu [como] · [parto]", "je mange · je pars"], ["tu [comes] · [partes]", "tu manges · tu pars"],
        ["ele [come] · [parte]", "il mange · il part"], ["nós [comemos] · [partimos]", "nous mangeons · partons"],
        ["eles [comem] · [partem]", "ils mangent · partent"], ["A loja [abre] às dez.", "le magasin ouvre à dix heures"]],
  "a": "-er et -ir ne diffèrent qu'à nós : comemos, partimos. Le reste est commun."},
 {"id": "ter_ir", "serie": "irregularesPtExercises", "t": "Ter et ir : avoir et aller",
  "l": [["eu [tenho] · eu [vou]", "j'ai · je vais"], ["tu [tens] · tu [vais]", "tu as · tu vas"],
        ["ele [tem] · ele [vai]", "il a · il va"], ["nós [temos] · [vamos]", "nous avons · allons"],
        ["eles [têm] · [vão]", "ils ont · ils vont"], ["[Tenho] fome.", "j'ai faim"]],
  "a": "Têm (ils ont) porte un accent qui le distingue de tem (il a) ; ils se prononcent presque pareil. Avoir faim, soif, froid : ter fome, ter sede, ter frio."},
 {"id": "estar_a", "serie": "estarAPtExercises", "t": "Estar a + infinitif : en train de",
  "l": [["[estou a ler]", "je suis en train de lire"], ["[estás a ouvir]?", "tu écoutes ?"],
        ["[está a chover]", "il pleut"], ["[estamos a jantar]", "nous dînons"],
        ["[estão a dormir]", "ils dorment"], ["O que [estás a fazer]?", "qu'est-ce que tu fais ?"]],
  "a": "La forme du Portugal pour ce qui se passe maintenant. Estou lendo (avec -ndo) est brésilienne : on la comprend, mais à Lisbonne on dit estou a ler."},
 {"id": "perfeito", "serie": "perfeitoPtExercises", "t": "Le passé (perfeito) : falei, comi, parti",
  "l": [["eu [falei] · [comi]", "j'ai parlé · mangé"], ["tu [falaste] · [comeste]", "tu as parlé · mangé"],
        ["ele [falou] · [comeu]", "il a parlé · mangé"], ["nós [falámos] · [comemos]", "nous avons parlé · mangé"],
        ["eles [falaram] · [comeram]", "ils ont parlé · mangé"], ["[Fui] a Sintra.", "je suis allé à Sintra"]],
  "a": "Un seul temps pour « j'ai parlé » et « je parlai ». Falámos (passé) porte un accent au Portugal. Ser et ir ont le même passé : fui, foste, foi."},
]
