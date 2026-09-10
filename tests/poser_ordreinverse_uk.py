# -*- coding: utf-8 -*-
"""ordreInverseExercises (54) : retourner une phrase, principale d'abord.

DEUX MOULES, PAS UN -- ET C'EST LE GARDE-FOU QUI L'A DIT. Je n'en avais releve
qu'un : « la subordonnee passe derriere ». Le refus a montre les quatorze
phrases qui vont dans l'AUTRE sens, ou la subordonnee passe DEVANT et ou le
verbe conjugue de la principale la suit. Deux consignes, deux explications ;
les confondre aurait enseigne la regle a l'envers a quatorze exercices.

Ce qui change dans un moule est la paire d'exemples ALLEMANDS citee a la fin,
et la conjonction citee dans l'indice. Ni l'une ni l'autre ne se traduit --
c'est de l'allemand, et c'est ce que l'exercice montre.

LE VRAI TRAVAIL EST AILLEURS : les 54 phrases d'exemple. Aucun moule ne les
couvre, elles sont traduites une par une, depuis l'ALLEMAND et non depuis le
francais -- le francais est deja une traduction, et traduire une traduction
fait deriver deux fois.

⚠️ LA CLE EST LA QUESTION ALLEMANDE, et elle est unique dans ce jeu (verifie).
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HINT = re.compile(r"^\(la même phrase, en commençant par la principale — "
                  r"(« .+? ») passe dans la seconde moitié\)$")
HINT_UK = "(те саме речення, але почни з головного — %s переходить у другу половину)"

# LE JEU VA DANS LES DEUX SENS, et le garde-fou l'a montre : quatorze phrases
# commencent DEJA par la principale, et l'exercice demande alors de faire
# passer la subordonnee devant. Autre consigne, autre moule.
HINT2 = re.compile(r"^\(la même phrase, en commençant par (« .+? »)\)$")
HINT2_UK = "(те саме речення, але почни з %s)"

EXPL = re.compile(r"^La subordonnée est passée derrière : la principale reprend son "
                  r"ordre normal — sujet, puis verbe\. L'inversion n'apparaît que "
                  r"lorsque la subordonnée occupe la première place\. Comparez : (.+)$")
EXPL_UK = ("Підрядне речення перейшло назад: головне повертає свій звичайний "
           "порядок — підмет, потім присудок. Інверсія з'являється лише тоді, "
           "коли підрядне стоїть на першому місці. Порівняй: %s")

EXPL2 = re.compile(r"^La subordonnée est passée devant : elle occupe la première "
                   r"place, donc le verbe conjugué de la principale la suit "
                   r"immédiatement et le sujet passe derrière\. Comparez : (.+)$")
EXPL2_UK = ("Підрядне речення перейшло вперед: воно стоїть на першому місці, "
            "тому відмінюване дієслово головного йде одразу за ним, а підмет — "
            "після дієслова. Порівняй: %s")

# Les 54 phrases, traduites depuis l'allemand. La cle est la question.
T = {
"Seitdem ich in Berlin wohne, spreche ich jeden Tag Deutsch.":
    "Відколи я живу в Берліні, я щодня розмовляю німецькою.",
"Weil es heute regnet, bleiben wir zu Hause.":
    "Оскільки сьогодні йде дощ, ми залишаємося вдома.",
"Wenn du Zeit hast, rufe ich dich an.":
    "Якщо ти матимеш час, я тобі зателефоную.",
"Obwohl er müde ist, arbeitet er weiter.":
    "Хоча він втомлений, він працює далі.",
"Nachdem wir gegessen haben, sind wir spazieren gegangen.":
    "Після того як ми поїли, ми пішли на прогулянку.",
"Seitdem sie umgezogen ist, haben wir uns nicht gesehen.":
    "Відколи вона переїхала, ми не бачилися.",
"Obwohl es geregnet hat, sind wir spazieren gegangen.":
    "Хоча йшов дощ, ми пішли на прогулянку.",
"Nachdem ich das Buch gelesen hatte, habe ich es verschenkt.":
    "Після того як я прочитав книжку, я її подарував.",
"Wenn du morgen kommst, werden wir zusammen kochen.":
    "Якщо ти прийдеш завтра, ми готуватимемо разом.",
"Weil er umgezogen ist, wird er jeden Tag früher aufstehen.":
    "Оскільки він переїхав, він щодня вставатиме раніше.",
"Bevor wir essen, waschen wir die Hände.":
    "Перш ніж їсти, ми миємо руки.",
"Während ich koche, deckst du den Tisch.":
    "Поки я готую, ти накриваєш на стіл.",
"Seit ich hier arbeite, habe ich weniger Zeit.":
    "Відколи я тут працюю, у мене менше часу.",
"Als ich klein war, habe ich in Wien gewohnt.":
    "Коли я був малим, я жив у Відні.",
"Weil ich zu viel gegessen habe, bin ich früh ins Bett gegangen.":
    "Оскільки я забагато з'їв, я рано ліг спати.",
"Nachdem ich die Prüfung bestanden hatte, habe ich meine Eltern angerufen.":
    "Після того як я склав іспит, я зателефонував батькам.",
"Obwohl wir früh losgefahren sind, haben wir den Zug verpasst.":
    "Хоча ми виїхали рано, ми запізнилися на потяг.",
"Als wir in Wien angekommen sind, hat es stark geregnet.":
    "Коли ми прибули до Відня, ішов сильний дощ.",
"Ich habe das Paket nicht bekommen, weil der Bote nicht geklingelt hat.":
    "Я не отримав посилки, бо кур'єр не подзвонив у двері.",
"Wir sind zu Fuß gegangen, obwohl es geschneit hat.":
    "Ми пішли пішки, хоча йшов сніг.",
"Sie hat mir geschrieben, nachdem sie nach Hause gekommen war.":
    "Вона написала мені після того, як повернулася додому.",
"Bevor ich eingeschlafen bin, habe ich noch ein Kapitel gelesen.":
    "Перш ніж заснути, я прочитав ще один розділ.",
"Er ist zur Arbeit gefahren, obwohl er schlecht geschlafen hat.":
    "Він поїхав на роботу, хоча погано спав.",
"Weil der Bus nicht gekommen ist, sind wir zu spät angekommen.":
    "Оскільки автобус не приїхав, ми прибули запізно.",
"Seitdem sie das Buch gelesen hat, spricht sie von nichts anderem.":
    "Відколи вона прочитала цю книжку, вона говорить тільки про неї.",
"Wenn ich Zeit habe, werde ich dich besuchen.":
    "Якщо я матиму час, я тебе відвідаю.",
"Ich werde früher aufstehen, damit ich den Zug nicht verpasse.":
    "Я встану раніше, щоб не запізнитися на потяг.",
"Sobald der Regen aufhört, werden wir spazieren gehen.":
    "Щойно дощ припиниться, ми підемо на прогулянку.",
"Obwohl es teuer ist, werde ich das Auto kaufen.":
    "Хоча це дорого, я куплю цю машину.",
"Wir werden zu Hause bleiben, bis der Arzt anruft.":
    "Ми залишатимемося вдома, доки не зателефонує лікар.",
"Nachdem ich umgezogen bin, werde ich eine Party machen.":
    "Після того як я переїду, я влаштую вечірку.",
"Er wird uns helfen, weil er morgen frei hat.":
    "Він нам допоможе, бо завтра він вільний.",
"Wenn du mir schreibst, werde ich sofort antworten.":
    "Якщо ти мені напишеш, я відразу відповім.",
"Ich werde dir alles erklären, wenn wir uns sehen.":
    "Я тобі все поясню, коли ми побачимося.",
"Während du kochst, werde ich den Tisch decken.":
    "Поки ти готуєш, я накрию на стіл.",
"Ich rufe dich an, wenn ich zu Hause bin.":
    "Я тобі телефоную, коли я вдома.",
"Bis der Bus kommt, warten wir im Café.":
    "Доки не приїде автобус, ми чекаємо в кафе.",
"Damit du mich verstehst, spreche ich langsam.":
    "Щоб ти мене розумів, я говорю повільно.",
"Wenn er nach Hause kommt, macht er zuerst das Fenster auf.":
    "Коли він приходить додому, він спершу відчиняє вікно.",
"Seit ich in Wien wohne, fahre ich jeden Tag mit der U-Bahn.":
    "Відколи я живу у Відні, я щодня їжджу метром.",
"Wir gehen ins Kino, obwohl der Film schon angefangen hat.":
    "Ми йдемо в кіно, хоча фільм уже почався.",
"Da es schon spät ist, gehen wir nach Hause.":
    "Оскільки вже пізно, ми йдемо додому.",
"Da ich kein Auto habe, fahre ich mit dem Rad.":
    "Оскільки я не маю машини, я їжджу велосипедом.",
"Wir bleiben drinnen, da es stark regnet.":
    "Ми залишаємося всередині, оскільки йде сильний дощ.",
"Falls es morgen regnet, bleiben wir zu Hause.":
    "Якщо раптом завтра піде дощ, ми залишаємося вдома.",
"Falls du Zeit hast, werden wir zusammen essen.":
    "Якщо раптом ти матимеш час, ми поїмо разом.",
"Solange es regnet, bleiben wir im Café.":
    "Поки йде дощ, ми залишаємося в кафе.",
"Du darfst hier bleiben, solange du willst.":
    "Ти можеш залишатися тут, скільки хочеш.",
"Solange ich hier wohne, fahre ich mit dem Bus.":
    "Поки я тут живу, я їжджу автобусом.",
"Sobald ich zu Hause bin, rufe ich dich an.":
    "Щойно я буду вдома, я тобі зателефоную.",
"Wir fangen an, sobald alle da sind.":
    "Ми починаємо, щойно всі зберуться.",
"Ich höre Musik, während ich koche.":
    "Я слухаю музику, поки готую.",
"Als der Film zu Ende war, sind wir nach Hause gegangen.":
    "Коли фільм закінчився, ми пішли додому.",
"Seit er in Wien wohnt, sehen wir ihn selten.":
    "Відколи він живе у Відні, ми бачимо його рідко.",
}


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["ordreInverseExercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        mh, mh2 = HINT.match(h), HINT2.match(h)
        mx, mx2 = EXPL.match(x), EXPL2.match(x)
        if q not in T:
            rates.append("TRAD : " + q)
            continue
        if not mh and not mh2:
            rates.append("INDICE : " + h)
            continue
        if not mx and not mx2:
            rates.append("EXPL : " + x)
            continue
        # UNE CONSIGNE ET SON EXPLICATION DOIVENT ALLER DANS LE MEME SENS.
        # Un indice « commence par la principale » avec une explication « la
        # subordonnee passe devant » serait contradictoire, et rien ne
        # l'attraperait a la relecture : les deux phrases sont justes prises
        # separement.
        if bool(mh) != bool(mx):
            rates.append("SENS CONTRAIRE : " + q)
            continue
        entrees.append({"question": q, "translation_uk": T[q],
                        "hint_uk": (HINT_UK % mh.group(1) if mh
                                    else HINT2_UK % mh2.group(1)),
                        "explanation_uk": (EXPL_UK % mx.group(1) if mx
                                           else EXPL2_UK % mx2.group(1))})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_ordreInverse.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "ordreInverseExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_ordreInverse.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
