# -*- coding: utf-8 -*-
"""Les 20 exemples qui manquaient aux cartes de Premiers pas (v884, 19 oct. 2026).

Jacques retourne « ¿A qué hora es la salida? » et ne trouve pas de phrase
d'exemple. tests/exemples.py en a trouve 10 par langue. Decide avec lui : la
boite vide disparait partout (index.html), et ces cartes recoivent un exemple
qui apporte quelque chose -- un usage pour les nombres, LA REPONSE pour les
questions, un petit contexte pour les exclamations.

Ecrit c[2] (l'exemple) et c[3] (sa traduction) des cartes qui n'en ont pas ;
ne touche a rien d'autre. Relancable : une carte deja completee est sautee.
    python tests/premiers_pas_exemples.py
"""
import io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DE = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
ES = ["fr", "en", "ar", "pt"]

def t(langues, *v):
    assert len(v) == len(langues)
    return dict(zip(langues, v))

EXEMPLES_DE = {
    "Was empfehlen Sie?": ("Was empfehlen Sie heute? – Den Fisch.", t(DE,
        "Que recommandez-vous aujourd'hui ? – Le poisson.", "What do you recommend today? – The fish.",
        "Bugün ne tavsiye edersiniz? – Balığı.", "Що ви порадите сьогодні? – Рибу.", "امروز چه پیشنهاد می‌کنید؟ – ماهی را.",
        "بماذا تنصحني اليوم؟ – بالسمك.", "O que o senhor recomenda hoje? – O peixe.", "Co pan poleca dzisiaj? – Rybę.",
        "Что вы посоветуете сегодня? – Рыбу.")),
    "Guten Appetit!": ("Das Essen ist da. Guten Appetit!", t(DE,
        "Le repas est servi. Bon appétit !", "The food is here. Enjoy your meal!", "Yemek geldi. Afiyet olsun!",
        "Їжа вже тут. Смачного!", "غذا آماده است. نوش جان!", "الطعام جاهز. بالهناء والشفاء!", "A comida chegou. Bom apetite!",
        "Jedzenie już jest. Smacznego!", "Еда готова. Приятного аппетита!")),
    "Prost!": ("Wir trinken zusammen. Prost!", t(DE,
        "Nous buvons ensemble. Santé !", "We're having a drink together. Cheers!", "Birlikte içiyoruz. Şerefe!",
        "Ми п'ємо разом. Будьмо!", "با هم می‌نوشیم. به سلامتی!", "نشرب معًا. في صحتك!", "Estamos bebendo juntos. Saúde!",
        "Pijemy razem. Na zdrowie!", "Мы пьём вместе. За здоровье!")),
    "eins · zwei · drei · vier · fünf": ("Ich möchte zwei Kaffee, bitte.", t(DE,
        "Je voudrais deux cafés, s'il vous plaît.", "I'd like two coffees, please.", "İki kahve istiyorum, lütfen.",
        "Мені дві кави, будь ласка.", "دو قهوه می‌خواهم، لطفاً.", "أريد قهوتين، من فضلك.", "Eu queria dois cafés, por favor.",
        "Poproszę dwie kawy.", "Мне два кофе, пожалуйста.")),
    "sechs · sieben · acht · neun · zehn": ("Der Zug fährt um acht Uhr.", t(DE,
        "Le train part à huit heures.", "The train leaves at eight o'clock.", "Tren saat sekizde kalkıyor.",
        "Потяг відправляється о восьмій.", "قطار ساعت هشت حرکت می‌کند.", "يغادر القطار في الساعة الثامنة.", "O trem sai às oito horas.",
        "Pociąg odjeżdża o ósmej.", "Поезд отправляется в восемь часов.")),
    "elf · zwölf": ("Das Museum öffnet um elf Uhr.", t(DE,
        "Le musée ouvre à onze heures.", "The museum opens at eleven o'clock.", "Müze saat on birde açılıyor.",
        "Музей відчиняється об одинадцятій.", "موزه ساعت یازده باز می‌شود.", "يفتح المتحف في الساعة الحادية عشرة.", "O museu abre às onze horas.",
        "Muzeum otwiera się o jedenastej.", "Музей открывается в одиннадцать часов.")),
    "Wann ist der Check-out?": ("Wann ist der Check-out? – Um elf Uhr.", t(DE,
        "À quelle heure faut-il libérer la chambre ? – À onze heures.", "What time is check-out? – At eleven o'clock.",
        "Odayı saat kaçta boşaltmak gerekiyor? – Saat on birde.", "О котрій треба звільнити номер? – Об одинадцятій.",
        "اتاق را ساعت چند باید تحویل داد؟ – ساعت یازده.", "متى يجب إخلاء الغرفة؟ – في الساعة الحادية عشرة.",
        "A que horas é preciso deixar o quarto? – Às onze horas.", "O której trzeba zwolnić pokój? – O jedenastej.",
        "Во сколько нужно освободить номер? – В одиннадцать.")),
    "Rufen Sie einen Krankenwagen!": ("Mein Freund ist krank. Rufen Sie einen Krankenwagen!", t(DE,
        "Mon ami est malade. Appelez une ambulance !", "My friend is ill. Call an ambulance!", "Arkadaşım hasta. Ambulans çağırın!",
        "Мій друг захворів. Викличте швидку!", "دوستم بیمار است. آمبولانس خبر کنید!", "صديقي مريض. اتصلوا بالإسعاف!",
        "Meu amigo está doente. Chame uma ambulância!", "Mój przyjaciel jest chory. Proszę wezwać karetkę!", "Моему другу плохо. Вызовите скорую!")),
    "Können Sie das bitte wiederholen?": ("Entschuldigung, ich verstehe nicht. Können Sie das bitte wiederholen?", t(DE,
        "Pardon, je ne comprends pas. Pouvez-vous répéter, s'il vous plaît ?", "Sorry, I don't understand. Can you repeat that, please?",
        "Affedersiniz, anlamıyorum. Tekrar edebilir misiniz, lütfen?", "Вибачте, я не розумію. Чи можете ви повторити, будь ласка?",
        "ببخشید، متوجه نمی‌شوم. می‌توانید تکرار کنید، لطفاً؟", "عذرًا، لا أفهم. هل يمكنك الإعادة من فضلك؟",
        "Desculpe, não entendo. O senhor pode repetir, por favor?", "Przepraszam, nie rozumiem. Czy może pan powtórzyć?",
        "Извините, я не понимаю. Можете повторить, пожалуйста?")),
    "Gute Reise!": ("Du fährst morgen nach Berlin? Gute Reise!", t(DE,
        "Tu pars demain à Berlin ? Bon voyage !", "You're going to Berlin tomorrow? Have a good trip!", "Yarın Berlin'e mi gidiyorsun? İyi yolculuklar!",
        "Ти завтра їдеш до Берліна? Щасливої дороги!", "فردا به برلین می‌روی؟ سفر خوش!", "ستسافر إلى برلين غدًا؟ رحلة سعيدة!",
        "Você vai para Berlim amanhã? Boa viagem!", "Jutro jedziesz do Berlina? Szczęśliwej podróży!", "Ты завтра едешь в Берлин? Счастливого пути!")),
}
EXEMPLES_ES = {
    "¿Qué me recomienda?": ("¿Qué me recomienda hoy? – El pescado.", t(ES,
        "Que me recommandez-vous aujourd'hui ? – Le poisson.", "What do you recommend today? – The fish.",
        "بماذا تنصحني اليوم؟ – بالسمك.", "O que o senhor me recomenda hoje? – O peixe.")),
    "¡Buen provecho!": ("La comida ya está aquí. ¡Buen provecho!", t(ES,
        "Le repas est servi. Bon appétit !", "The food is here. Enjoy your meal!", "الطعام جاهز. بالهناء والشفاء!", "A comida chegou. Bom apetite!")),
    "¡Salud!": ("Brindamos juntos. ¡Salud!", t(ES,
        "Nous trinquons ensemble. Santé !", "We raise our glasses together. Cheers!", "نرفع الكؤوس معًا. في صحتك!", "Brindamos juntos. Saúde!")),
    "uno · dos · tres · cuatro · cinco": ("Quiero dos cafés, por favor.", t(ES,
        "Je voudrais deux cafés, s'il vous plaît.", "I'd like two coffees, please.", "أريد قهوتين، من فضلك.", "Eu queria dois cafés, por favor.")),
    "seis · siete · ocho · nueve · diez": ("El tren sale a las ocho.", t(ES,
        "Le train part à huit heures.", "The train leaves at eight.", "يغادر القطار في الساعة الثامنة.", "O trem sai às oito.")),
    "once · doce": ("El museo abre a las once.", t(ES,
        "Le musée ouvre à onze heures.", "The museum opens at eleven.", "يفتح المتحف في الساعة الحادية عشرة.", "O museu abre às onze.")),
    "¿A qué hora es la salida?": ("¿A qué hora es la salida? – A las doce.", t(ES,
        "À quelle heure faut-il libérer la chambre ? – À midi.", "What time is check-out? – At twelve.",
        "متى يجب إخلاء الغرفة؟ – في الساعة الثانية عشرة.", "A que horas é preciso deixar o quarto? – Ao meio-dia.")),
    "¡Llame a una ambulancia!": ("Mi amigo está enfermo. ¡Llame a una ambulancia!", t(ES,
        "Mon ami est malade. Appelez une ambulance !", "My friend is ill. Call an ambulance!", "صديقي مريض. اتصلوا بالإسعاف!",
        "Meu amigo está doente. Chame uma ambulância!")),
    "¿Puede repetir, por favor?": ("Perdón, no entiendo. ¿Puede repetir, por favor?", t(ES,
        "Pardon, je ne comprends pas. Pouvez-vous répéter, s'il vous plaît ?", "Sorry, I don't understand. Can you repeat that, please?",
        "عذرًا، لا أفهم. هل يمكنك الإعادة من فضلك؟", "Desculpe, não entendo. O senhor pode repetir, por favor?")),
    "¡Buen viaje!": ("¿Te vas a Madrid mañana? ¡Buen viaje!", t(ES,
        "Tu pars à Madrid demain ? Bon voyage !", "You're going to Madrid tomorrow? Have a good trip!",
        "ستسافر إلى مدريد غدًا؟ رحلة سعيدة!", "Você vai para Madri amanhã? Boa viagem!")),
}

def completer(fichier, exemples):
    chemin = os.path.join(RACINE, fichier)
    d = json.loads(io.open(chemin, encoding="utf-8", newline="").read())
    faits = 0
    for etape in d["etapes"]:
        for c in etape["cartes"]:
            variante = c[-1] if c and isinstance(c[-1], dict) and "la" in c[-1] else None
            base = c[:-1] if variante else c
            if len(base) > 2 and isinstance(base[2], str) and base[2].strip():
                continue
            if base[0] not in exemples:
                continue
            ex, sens = exemples[base[0]]
            neuf = base[:2] + [ex, sens]
            c[:] = neuf + ([variante] if variante else [])
            faits += 1
    texte = json.dumps(d, ensure_ascii=False, indent=1).replace("\n", "\r\n") + "\r\n"
    with io.open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(texte)
    print("%s : %d cartes completees" % (fichier, faits))

completer("premiers-pas.json", EXEMPLES_DE)
completer(os.path.join("espanol", "datos", "premiers-pas.json"), EXEMPLES_ES)
