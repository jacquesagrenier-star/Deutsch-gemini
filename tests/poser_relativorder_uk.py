# -*- coding: utf-8 -*-
"""relativOrderExercises (70) : deux explications pour 70 exercices."""
import io, json, os, sys

RACINE = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
QUK = "Постав слова в правильному порядку:"
E = {
 "Le verbe (conjugué, ou le bloc participe+auxiliaire au Perfekt) va à la toute fin de la relative.":
 "Дієслово (дієвідмінюване або блок дієприкметник+допоміжне у Perfekt) іде в самий кінець підрядного означального речення.",
 "La relative (avec son verbe à la fin) vient après la virgule.":
 "Підрядне означальне речення (з дієсловом у кінці) іде після коми.",
}
T = {
"Je connais l’homme qui habite ici.":"Я знаю чоловіка, який тут живе.",
"C’est la femme qui travaille ici.":"Це жінка, яка тут працює.",
"Nous voyons l’enfant qui joue là.":"Ми бачимо дитину, яка там грається.",
"J’aime les gens qui habitent ici.":"Мені подобаються люди, які тут живуть.",
"Elle connaît le garçon qui joue au foot.":"Вона знає хлопця, який грає у футбол.",
"Il salue la femme qui est assise à côté de lui.":"Він вітає жінку, яка сидить поруч із ним.",
"Nous cherchons la maison qui se trouve là.":"Ми шукаємо будинок, який стоїть там.",
"J’appelle l’ami qui m’aide.":"Я дзвоню другові, який мені допомагає.",
"C’est le professeur qui enseigne l’allemand.":"Це вчитель, який викладає німецьку.",
"Nous aimons la musique qui joue ici.":"Нам подобається музика, яка тут грає.",
"Je connais la médecin qui travaille là.":"Я знаю лікарку, яка там працює.",
"Elle aime le chien qui est si fidèle.":"Вона любить собаку, який такий вірний.",
"Nous saluons les enfants qui jouent dans le jardin.":"Ми вітаємо дітей, які граються в саду.",
"Je lis le livre qui est très passionnant.":"Я читаю книжку, яка дуже захоплива.",
"C’est le chanteur qui chante ce soir.":"Це співак, який співає сьогодні ввечері.",
"Nous connaissons la famille qui habite à côté.":"Ми знаємо родину, яка живе поруч.",
"J’aime le film qui passe en ce moment.":"Мені подобається фільм, який зараз показують.",
"Elle rend visite à la tante qui habite à Bonn.":"Вона провідує тітку, яка живе в Бонні.",
"Nous entendons l’oiseau qui chante si joliment.":"Ми чуємо птаха, який так гарно співає.",
"Je rencontre le collègue qui est toujours ponctuel.":"Я зустрічаю колегу, який завжди пунктуальний.",
"C’est la fille qui dessine si bien.":"Це дівчина, яка так гарно малює.",
"Nous voyons les étoiles qui brillent fort aujourd’hui.":"Ми бачимо зорі, які сьогодні яскраво сяють.",
"Je connais le boulanger qui fait du pain frais.":"Я знаю пекаря, який пече свіжий хліб.",
"Elle aime le chat qui dort toujours.":"Вона любить кота, який завжди спить.",
"Nous connaissons le médecin qui est très patient.":"Ми знаємо лікаря, який дуже терплячий.",
"Je connais l’homme qui passe ici tous les jours.":"Я знаю чоловіка, який тут щодня проходить.",
"C’est la femme qui m’aide souvent.":"Це жінка, яка мені часто допомагає.",
"Nous connaissons l’enfant que j’aide parfois.":"Ми знаємо дитину, якій я іноді допомагаю.",
"J’aime les gens en qui j’ai vraiment confiance.":"Мені подобаються люди, яким я справді довіряю.",
"Elle connaît le garçon que tous les enfants aiment.":"Вона знає хлопця, якого люблять усі діти.",
"Il salue la femme qu’il écoute souvent.":"Він вітає жінку, яку часто слухає.",
"Nous cherchons la maison qui appartient à ma famille.":"Ми шукаємо будинок, який належить моїй родині.",
"J’appelle l’ami en qui j’ai toujours confiance.":"Я дзвоню другові, якому завжди довіряю.",
"C’est le professeur que presque tous les élèves aiment.":"Це вчитель, якого люблять майже всі учні.",
"Nous aimons la musique que nos parents écoutent.":"Нам подобається музика, яку слухають наші батьки.",
"Je connais la médecin à qui je confie ma santé.":"Я знаю лікарку, якій довіряю своє здоров'я.",
"Elle aime le chien à qui elle donne à manger tous les jours.":"Вона любить собаку, якого щодня годує.",
"Nous saluons les enfants à qui nous faisons souvent signe.":"Ми вітаємо дітей, яким часто махаємо.",
"Je lis le livre que ma sœur recommande.":"Я читаю книжку, яку радить моя сестра.",
"C’est le chanteur que tous les fans écoutent.":"Це співак, якого слухають усі фанати.",
"Nous connaissons la famille que nous aidons souvent.":"Ми знаємо родину, якій часто допомагаємо.",
"J’aime le film que mon frère recommande.":"Мені подобається фільм, який радить мій брат.",
"Elle rend visite à la tante à qui elle écrit chaque semaine.":"Вона провідує тітку, якій пише щотижня.",
"Nous entendons l’oiseau que nos voisins nourrissent.":"Ми чуємо птаха, якого годують наші сусіди.",
"Je rencontre le collègue à qui je réponds cette semaine.":"Я зустрічаю колегу, якому цього тижня відповідаю.",
"C’est la fille en qui ma fille a confiance.":"Це дівчина, якій довіряє моя донька.",
"Nous voyons les étoiles que tous les astronomes observent.":"Ми бачимо зорі, які спостерігають усі астрономи.",
"Je connais le boulanger en qui toute la rue a confiance.":"Я знаю пекаря, якому довіряє вся вулиця.",
"Elle aime le chat à qui mon père donne du lait.":"Вона любить кота, якому мій батько дає молоко.",
"Nous connaissons le médecin en qui tous les patients ont confiance.":"Ми знаємо лікаря, якому довіряють усі пацієнти.",
"C’est le vin que nous avons commandé hier.":"Це вино, яке ми вчора замовили.",
"Je connais la médecin à qui j’ai écrit récemment.":"Я знаю лікарку, якій нещодавно написав.",
"Nous rendons visite à l’ami que nous avons aidé la semaine dernière.":"Ми провідуємо друга, якому допомогли минулого тижня.",
"C’est la robe que ma mère a cousue.":"Це сукня, яку пошила моя мама.",
"Elle aime les fleurs que son mari lui a offertes.":"Вона любить квіти, які подарував їй чоловік.",
"Je connais l’auteur dont j’ai lu le livre.":"Я знаю автора, чию книжку прочитав.",
"Nous remercions la femme qui nous a aidés gentiment.":"Ми дякуємо жінці, яка люб'язно нам допомогла.",
"Ce sont les amis qui nous ont invités à la fête.":"Це друзі, які запросили нас на свято.",
"Je lis l’article qu’un journaliste connu a écrit.":"Я читаю статтю, яку написав відомий журналіст.",
"Elle connaît l’homme dont la voiture a été volée hier.":"Вона знає чоловіка, чиє авто вчора вкрали.",
"Nous visitons le musée que beaucoup de touristes ont recommandé.":"Ми відвідуємо музей, який рекомендували багато туристів.",
"Je remercie le professeur qui m’a beaucoup appris.":"Я дякую вчителеві, який мене багато чого навчив.",
"C’est le gâteau que ma grand-mère a préparé pour nous.":"Це торт, який спекла для нас моя бабуся.",
"Nous connaissons la famille dont la maison a brûlé l’année dernière.":"Ми знаємо родину, чий будинок торік згорів.",
"J’aime le roman que ma professeure nous a recommandé.":"Мені подобається роман, який нам порадила вчителька.",
"Elle rencontre la collègue à qui elle a écrit un courriel hier.":"Вона зустрічає колегу, якій учора написала електронного листа.",
"Nous saluons le voisin que nous avons aidé le mois dernier.":"Ми вітаємо сусіда, якому допомогли минулого місяця.",
"C’est l’élève dont l’essai la professeure a félicité.":"Це учень, чий твір похвалила вчителька.",
"Je connais la famille dont le fils s’est marié l’année dernière.":"Я знаю родину, чий син торік одружився.",
"Nous félicitons le joueur qui a marqué le but décisif.":"Ми вітаємо гравця, який забив вирішальний гол.",
}

d = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))
entrees, rates = [], []
for e in d["jeux"]["relativOrderExercises"]:
    fr = e["translation"]
    if fr not in T: rates.append("PHRASE : " + fr); continue
    if e["explanation"] not in E: rates.append("EXPL : " + e["explanation"][:60]); continue
    entrees.append({"question": e["question"], "cle_translation": fr,
                    "question_uk": QUK, "translation_uk": T[fr],
                    "explanation_uk": E[e["explanation"]]})
if rates:
    print("REFUS : %d cas" % len(rates))
    for r in rates[:8]: print("   " + r)
    sys.exit(1)
io.open(os.path.join(RACINE, "corrections_uk", "exos_relativOrder.json"), "w",
        encoding="utf-8", newline="\n").write(
    json.dumps({"jeu": "relativOrderExercises", "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
print("exos_relativOrder.json : %d entrees" % len(entrees))
