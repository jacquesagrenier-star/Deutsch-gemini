# -*- coding: utf-8 -*-
"""Pose l'anglais et l'arabe (langues d'interface) a cote du francais dans les conversations jouees. Gratuit.

    python visuel/conversation/traduire.py           # pose ce qui manque et dit ce qui n'a pas de traduction
    python visuel/conversation/traduire.py --verifier

Les traductions sont ecrites ici, une fois par phrase francaise : une phrase qui revient dans plusieurs conversations
(« Merci, au revoir. ») n'a qu'une ligne. Elles s'appliquent aux conversations de l'allemand et de l'espagnol (l'anglais
appris a une interface en francais seulement). L'arabe est a relire par un natif (retours/A-RELIRE-CONVERSATIONS.md).
"""
import glob, io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
DONNEES = os.path.join(os.path.dirname(ICI), "prototype", "conversation", "donnees")
PERSONNES = os.path.join(os.path.dirname(ICI), "prototype", "conversation")

T = {
 "Au contrôle des passeports": ("At passport control", "عند مراقبة الجوازات"),
 "Tu arrives à l'aéroport de Berlin. Le policier du contrôle te parle. Réponds avec les phrases de l'étape.":
  ("You arrive at Berlin airport. The police officer at passport control speaks to you. Answer with the sentences of this step.",
   "تصل إلى مطار برلين. يكلّمك الشرطي عند مراقبة الجوازات. أجب بجمل هذه المرحلة."),
 "Tu as passé le contrôle : tu as salué, montré ton passeport, dit d'où tu viens et que tu es touriste.":
  ("You got through passport control: you said hello, showed your passport, said where you come from and that you are a tourist.",
   "اجتزت المراقبة: سلّمت، وأظهرت جواز سفرك، وقلت من أين أنت وأنك سائح."),
 "Aéroport de Berlin. C'est ton tour au contrôle des passeports.": ("Berlin airport. It's your turn at passport control.", "مطار برلين. جاء دورك عند مراقبة الجوازات."),
 "Bonjour ! Votre passeport, s'il vous plaît.": ("Hello! Your passport, please.", "مرحبًا! جواز سفرك من فضلك."),
 "Bonjour. Voici mon passeport.": ("Hello. Here is my passport.", "مرحبًا. هذا جواز سفري."),
 "Un moment, s'il vous plaît. Voici mon passeport.": ("One moment, please. Here is my passport.", "لحظة من فضلك. هذا جواز سفري."),
 "Merci. D'où venez-vous ?": ("Thank you. Where do you come from?", "شكرًا. من أين أنت؟"),
 "Je viens du Canada.": ("I come from Canada.", "أنا من كندا."),
 "Je viens de France.": ("I come from France.", "أنا من فرنسا."),
 "Et vous êtes touriste ?": ("And you are a tourist?", "وهل أنت سائح؟"),
 "Oui, je suis touriste (un homme).": ("Yes, I'm a tourist (a man).", "نعم، أنا سائح (رجل)."),
 "Oui, je suis touriste (une femme).": ("Yes, I'm a tourist (a woman).", "نعم، أنا سائحة (امرأة)."),
 "Bien. Bienvenue en Allemagne !": ("Good. Welcome to Germany!", "جيد. أهلًا بك في ألمانيا!"),
 "Merci ! Au revoir !": ("Thank you! Goodbye!", "شكرًا! إلى اللقاء!"),
 "Tu arrives à l'aéroport de Madrid. Le policier du contrôle te parle. Réponds avec les phrases de l'étape.":
  ("You arrive at Madrid airport. The police officer at passport control speaks to you. Answer with the sentences of this step.",
   "تصل إلى مطار مدريد. يكلّمك الشرطي عند مراقبة الجوازات. أجب بجمل هذه المرحلة."),
 "Tu as passé le contrôle : tu as salué, demandé un moment, dit d'où tu viens et que tu es touriste.":
  ("You got through passport control: you said hello, asked for a moment, said where you come from and that you are a tourist.",
   "اجتزت المراقبة: سلّمت، وطلبت لحظة، وقلت من أين أنت وأنك سائح."),
 "Aéroport de Madrid-Barajas. C'est ton tour au contrôle des passeports.": ("Madrid-Barajas airport. It's your turn at passport control.", "مطار مدريد باراخاس. جاء دورك عند مراقبة الجوازات."),
 "Bonjour. Le passeport, s'il vous plaît.": ("Hello. Your passport, please.", "مرحبًا. جواز السفر من فضلك."),
 "Bonjour, monsieur. Un moment.": ("Hello, sir. One moment.", "مرحبًا يا سيدي. لحظة."),
 "Oui, un moment, s'il vous plaît.": ("Yes, one moment, please.", "نعم، لحظة من فضلك."),
 "Merci. D'où êtes-vous ?": ("Thank you. Where are you from?", "شكرًا. من أين أنت؟"),
 "Je suis du Canada.": ("I'm from Canada.", "أنا من كندا."),
 "Je suis de France.": ("I'm from France.", "أنا من فرنسا."),
 "Oui, je suis touriste.": ("Yes, I'm a tourist.", "نعم، أنا سائح."),
 "Très bien. Bon voyage !": ("Very good. Have a good trip!", "جيد جدًا. رحلة سعيدة!"),
 "Merci. Au revoir !": ("Thank you. Goodbye!", "شكرًا. إلى اللقاء!"),
 "Le petit-déjeuner au café": ("Breakfast at the café", "الفطور في المقهى"),
 "Premier matin à Berlin. Tu prends ton petit-déjeuner dans un café. Commande, puis paie.":
  ("First morning in Berlin. You have breakfast in a café. Order, then pay.", "أول صباح في برلين. تتناول فطورك في مقهى. اطلب، ثم ادفع."),
 "Tu as commandé ton petit-déjeuner, demandé l'addition et payé {a_payer}.":
  ("You ordered your breakfast, asked for the bill and paid {a_payer}.", "طلبت فطورك، وطلبت الحساب، ودفعت {a_payer}."),
 "Un petit café du quartier, le matin. La serveuse arrive.": ("A small neighbourhood café, in the morning. The waitress comes over.", "مقهى صغير في الحي، في الصباح. تأتي النادلة."),
 "Bonjour ! Qu'est-ce que vous désirez ?": ("Good morning! What would you like?", "صباح الخير! ماذا تريد؟"),
 "Je voudrais un café au lait, s'il vous plaît.": ("I'd like a coffee with milk, please.", "أريد قهوة بالحليب من فضلك."),
 "Pour moi, un jus d'orange, s'il vous plaît.": ("For me, an orange juice, please.", "لي عصير برتقال من فضلك."),
 "Volontiers. Et un petit pain ?": ("Of course. And a bread roll?", "بكل سرور. وخبزة صغيرة؟"),
 "Oui, un petit pain, s'il vous plaît.": ("Yes, a bread roll, please.", "نعم، خبزة صغيرة من فضلك."),
 "Ça arrive tout de suite !": ("Coming right up!", "حالًا!"),
 "Non, merci.": ("No, thank you.", "لا، شكرًا."),
 "Un peu plus tard. Tu as fini et tu veux payer.": ("A little later. You've finished and want to pay.", "بعد قليل. انتهيت وتريد أن تدفع."),
 "L'addition, s'il vous plaît.": ("The bill, please.", "الحساب من فضلك."),
 "Ça fait combien ?": ("How much is it?", "كم المبلغ؟"),
 "Ça fait {a_payer}.": ("That's {a_payer}.", "المبلغ {a_payer}."),
 "Par carte, s'il vous plaît.": ("By card, please.", "بالبطاقة من فضلك."),
 "Merci beaucoup ! Au revoir !": ("Thank you very much! Goodbye!", "شكرًا جزيلًا! إلى اللقاء!"),
 "Merci, au revoir.": ("Thank you, goodbye.", "شكرًا، إلى اللقاء."),
 "Merci ! Bonne journée !": ("Thank you! Have a nice day!", "شكرًا! يومًا سعيدًا!"),
 "Le petit-déjeuner au bar": ("Breakfast at the bar", "الفطور في المقهى"),
 "Premier matin à Madrid. Tu prends ton petit-déjeuner dans un bar du quartier. Commande, puis paie.":
  ("First morning in Madrid. You have breakfast in a neighbourhood bar. Order, then pay.", "أول صباح في مدريد. تتناول فطورك في مقهى الحي. اطلب، ثم ادفع."),
 "Un bar du quartier, le matin. La serveuse est derrière le comptoir.": ("A neighbourhood bar, in the morning. The waitress is behind the counter.", "مقهى في الحي، في الصباح. النادلة خلف المنضدة."),
 "Bonjour ! Qu'est-ce que vous voulez prendre ?": ("Good morning! What would you like to have?", "صباح الخير! ماذا تريد أن تتناول؟"),
 "Je veux un café au lait, s'il vous plaît.": ("I want a coffee with milk, please.", "أريد قهوة بالحليب من فضلك."),
 "Très bien. Et un sandwich ?": ("Very good. And a sandwich?", "جيد جدًا. وشطيرة؟"),
 "Oui, un sandwich, s'il vous plaît.": ("Yes, a sandwich, please.", "نعم، شطيرة من فضلك."),
 "Tout de suite !": ("Right away!", "حالًا!"),
 "C'est combien ?": ("How much is it?", "كم الثمن؟"),
 "Merci ! À plus tard !": ("Thank you! See you later!", "شكرًا! إلى اللقاء لاحقًا!"),
 "Merci à vous ! Au revoir !": ("Thank you! Goodbye!", "الشكر لك! إلى اللقاء!"),
 "À la réception de l'hôtel": ("At the hotel reception", "في استقبال الفندق"),
 "Tu arrives à ton hôtel de Berlin. Tu prends ta chambre, puis, le lendemain matin, tu signales un problème.":
  ("You arrive at your hotel in Berlin. You check in, then, the next morning, you report a problem.", "تصل إلى فندقك في برلين. تستلم غرفتك، ثم في صباح اليوم التالي تُبلغ عن مشكلة."),
 "Tu as pris ta chambre, posé une question, signalé un problème et obtenu une solution.":
  ("You checked in, asked a question, reported a problem and got a solution.", "استلمت غرفتك، وطرحت سؤالًا، وأبلغت عن مشكلة، وحصلت على حل."),
 "Le soir, à la réception d'un petit hôtel.": ("In the evening, at the reception of a small hotel.", "في المساء، في استقبال فندق صغير."),
 "Bonsoir ! Bienvenue à l'hôtel.": ("Good evening! Welcome to the hotel.", "مساء الخير! أهلًا بك في الفندق."),
 "Bonsoir. J'ai une réservation pour deux nuits.": ("Good evening. I have a reservation for two nights.", "مساء الخير. لدي حجز لليلتين."),
 "Bonsoir. Vous avez une chambre double ?": ("Good evening. Do you have a double room?", "مساء الخير. هل لديكم غرفة مزدوجة؟"),
 "Bonsoir. Je suis une réservation.": ("Good evening. I am a reservation.", "مساء الخير. أنا حجز."),
 "<b>« ich bin »</b>, c'est « je suis » ; <b>« ich habe »</b>, « j'ai ». Dis : « Ich habe eine Reservierung ».":
  ("<b>« ich bin »</b> means “I am”; <b>« ich habe »</b> means “I have”. Say: « Ich habe eine Reservierung ».",
   "<b>«ich bin»</b> تعني «أنا»، و<b>«ich habe»</b> تعني «لدي». قل: «Ich habe eine Reservierung»."),
 "Vous… êtes une réservation ?": ("You… are a reservation?", "أنت… حجز؟"),
 "Très bien. Votre chambre est au troisième étage. Voici la clé.": ("Very good. Your room is on the third floor. Here is the key.", "جيد جدًا. غرفتك في الطابق الثالث. هذا هو المفتاح."),
 "Merci. Excusez-moi, où est l'ascenseur ?": ("Thank you. Excuse me, where is the lift?", "شكرًا. عفوًا، أين المصعد؟"),
 "Juste ici, à gauche.": ("Right here, on the left.", "هنا تمامًا، على اليسار."),
 "Merci. Le petit-déjeuner est compris ?": ("Thank you. Is breakfast included?", "شكرًا. هل الفطور مشمول؟"),
 "Oui, le petit-déjeuner est compris.": ("Yes, breakfast is included.", "نعم، الفطور مشمول."),
 "Le lendemain matin, tu redescends à la réception.": ("The next morning, you go back down to reception.", "في صباح اليوم التالي، تنزل إلى الاستقبال."),
 "Bonjour ! Tout va bien ?": ("Good morning! Is everything all right?", "صباح الخير! هل كل شيء على ما يرام؟"),
 "La douche ne fonctionne pas.": ("The shower doesn't work.", "الدش لا يعمل."),
 "Oh, je suis désolée ! J'envoie quelqu'un tout de suite.": ("Oh, I'm sorry! I'll send someone right away.", "آه، أنا آسفة! سأرسل أحدًا حالًا."),
 "Il y a beaucoup de bruit dans la chambre.": ("It's very noisy in the room.", "هناك ضجيج كثير في الغرفة."),
 "Oh, je suis désolée ! Vous aurez une autre chambre.": ("Oh, I'm sorry! You'll get another room.", "آه، أنا آسفة! ستحصل على غرفة أخرى."),
 "Vous avez besoin d'autre chose ?": ("Do you need anything else?", "هل تحتاج إلى شيء آخر؟"),
 "Le petit-déjeuner, c'est à quelle heure ?": ("What time is breakfast?", "في أي ساعة الفطور؟"),
 "De sept heures à dix heures. Bon appétit !": ("From seven to ten. Enjoy your meal!", "من السابعة إلى العاشرة. بالهناء والشفاء!"),
 "Non, merci. Au revoir !": ("No, thank you. Goodbye!", "لا، شكرًا. إلى اللقاء!"),
 "Au revoir ! Bonne journée !": ("Goodbye! Have a nice day!", "إلى اللقاء! يومًا سعيدًا!"),
 "Tu arrives à ton hôtel de Madrid. Tu prends ta chambre, puis, le lendemain matin, tu signales un problème.":
  ("You arrive at your hotel in Madrid. You check in, then, the next morning, you report a problem.", "تصل إلى فندقك في مدريد. تستلم غرفتك، ثم في صباح اليوم التالي تُبلغ عن مشكلة."),
 "<b>« soy »</b>, c'est « je suis » ; <b>« tengo »</b>, « j'ai ». Dis : « Tengo una reserva ».":
  ("<b>« soy »</b> means “I am”; <b>« tengo »</b> means “I have”. Say: « Tengo una reserva ».",
   "<b>«soy»</b> تعني «أنا»، و<b>«tengo»</b> تعني «لدي». قل: «Tengo una reserva»."),
 "Merci. Pardon, où est l'ascenseur ?": ("Thank you. Sorry, where is the lift?", "شكرًا. عفوًا، أين المصعد؟"),
 "Oh, je suis désolée ! Je vous donne une autre chambre.": ("Oh, I'm sorry! I'll give you another room.", "آه، أنا آسفة! سأعطيك غرفة أخرى."),
 "Au marché": ("At the market", "في السوق"),
 "Samedi matin, au marché de ton quartier. Tu achètes des fruits ou des légumes, tu demandes un prix, tu paies.":
  ("Saturday morning, at your local market. You buy fruit or vegetables, ask a price and pay.", "صباح السبت، في سوق حيّك. تشتري فواكه أو خضارًا، وتسأل عن سعر، وتدفع."),
 "Tu as acheté au marché, demandé un prix et payé {a_payer}.": ("You shopped at the market, asked a price and paid {a_payer}.", "اشتريت من السوق، وسألت عن سعر، ودفعت {a_payer}."),
 "Samedi matin, au marché. Un marchand t'appelle derrière son étal.": ("Saturday morning, at the market. A stallholder calls out to you from his stall.", "صباح السبت في السوق. بائع يناديك من وراء بسطته."),
 "Un kilo de pommes, s'il vous plaît.": ("A kilo of apples, please.", "كيلو تفاح من فضلك."),
 "Un demi-kilo de tomates, s'il vous plaît.": ("Half a kilo of tomatoes, please.", "نصف كيلو طماطم من فضلك."),
 "Je voudrais un kilo de pommes (mot à mot : « de » pommes).": ("I'd like a kilo of apples (word for word: « of » apples).", "أريد كيلو تفاح (حرفيًا: كيلو «من» التفاح)."),
 "<b>Pas de « von » après une quantité</b>, contrairement au « de » français : « ein Kilo Äpfel », « eine Flasche Wasser ».":
  ("<b>No « von » after a quantity</b>, unlike English “of”: « ein Kilo Äpfel », « eine Flasche Wasser ».",
   "<b>لا تُستعمل «von» بعد الكمية</b>: «ein Kilo Äpfel»، «eine Flasche Wasser»."),
 "Un kilo… « von » pommes ?": ("A kilo… « von » apples?", "كيلو… «von» تفاح؟"),
 "Volontiers. Autre chose ?": ("Of course. Anything else?", "بكل سرور. شيء آخر؟"),
 "Non, c'est tout, merci.": ("No, that's all, thank you.", "لا، هذا كل شيء، شكرًا."),
 "Combien coûte le fromage ?": ("How much is the cheese?", "كم سعر الجبن؟"),
 "Le fromage ? Quatre euros.": ("The cheese? Four euros.", "الجبن؟ أربعة يورو."),
 "Bien, je le prends.": ("Good, I'll take it.", "حسنًا، سآخذه."),
 "C'est très cher. Non, merci.": ("That's very expensive. No, thank you.", "هذا غالٍ جدًا. لا، شكرًا."),
 "Vous avez un sac ?": ("Do you have a bag?", "هل لديك كيس؟"),
 "Oui, bien sûr. Voilà. Bon week-end !": ("Yes, of course. Here you are. Have a nice weekend!", "نعم، بالطبع. تفضّل. عطلة نهاية أسبوع سعيدة!"),
 "Merci, au revoir !": ("Thank you, goodbye!", "شكرًا، إلى اللقاء!"),
 "Merci ! Bon week-end !": ("Thank you! Have a nice weekend!", "شكرًا! عطلة نهاية أسبوع سعيدة!"),
 "Bonjour ! Qu'est-ce que je vous sers ?": ("Good morning! What can I get you?", "صباح الخير! ماذا أقدّم لك؟"),
 "Un demi-kilo de tomates (mot à mot : « un » demi-kilo).": ("Half a kilo of tomatoes (word for word: « a » half kilo).", "نصف كيلو طماطم (حرفيًا: «un» نصف كيلو)."),
 "<b>« medio » se dit sans « un »</b>, contrairement au français : « medio kilo », « media hora ».":
  ("<b>« medio » is said without « un »</b>: « medio kilo », « media hora ».", "<b>تُقال «medio» بدون «un»</b>: «medio kilo»، «media hora»."),
 "« Un » demi-kilo ? Un demi-kilo, non ?": ("« Un » half kilo? Half a kilo, right?", "«un» نصف كيلو؟ نصف كيلو، أليس كذلك؟"),
 "Très bien. Autre chose ?": ("Very good. Anything else?", "جيد جدًا. شيء آخر؟"),
 "Non, rien d'autre, merci.": ("No, nothing else, thank you.", "لا، لا شيء آخر، شكرًا."),
 "Très bien, je le prends.": ("Very good, I'll take it.", "جيد جدًا، سآخذه."),
}
NOMS = {"La serveuse": ("The waitress", "النادلة"), "Le voisin de table": ("The man at the next table", "جار الطاولة"),
        "Le policier": ("The police officer", "الشرطي"), "La réceptionniste": ("The receptionist", "موظفة الاستقبال"),
        "Le marchand": ("The stallholder", "البائع"), "La vendeuse": ("The sales assistant", "البائعة")}


def main():
    manque = set()

    def poser(o, cle_fr="fr"):
        """o : un objet {fr: ...} (titre, aide, recit) ou une replique / un choix (fr a cote de t)."""
        fr = o.get(cle_fr)
        if not fr:
            return
        if fr not in T:
            manque.add(fr); return
        o["en"], o["ar"] = T[fr]

    for f in sorted(glob.glob(os.path.join(DONNEES, "*.json"))):
        nom = os.path.basename(f)
        if nom.startswith(("index", "lot-")) or not nom.split(".")[1] in ("de", "es"):
            continue
        c = json.load(io.open(f, encoding="utf-8"))
        if c.get("parcours") != "premiers-pas":
            continue
        for k in ("titre", "intro", "bilan"):
            poser(c[k])
        for n in c["noeuds"].values():
            for r in n.get("dit", []):
                poser(r["recit"] if "recit" in r else r)
            for ch in n.get("choix", []):
                poser(ch)
                if ch.get("aide"):
                    poser(ch["aide"])
                for r in ch.get("puis", []):
                    poser(r)
        if "--verifier" not in sys.argv:
            io.open(f, "w", encoding="utf-8", newline="\n").write(json.dumps(c, ensure_ascii=False, indent=1) + "\n")
    for f in glob.glob(os.path.join(PERSONNES, "personnes*.json")):
        p = json.load(io.open(f, encoding="utf-8"))
        for k, v in p.items():
            if k.startswith("_"):
                continue
            fr = v["nom"]["fr"]
            if fr in NOMS:
                v["nom"]["en"], v["nom"]["ar"] = NOMS[fr]
            else:
                manque.add(fr)
        if "--verifier" not in sys.argv:
            io.open(f, "w", encoding="utf-8", newline="\n").write(json.dumps(p, ensure_ascii=False, indent=1) + "\n")
    for m in sorted(manque):
        print("  sans traduction :", m)
    print("  %d phrase(s) sans traduction" % len(manque))
    sys.exit(1 if manque else 0)


if __name__ == "__main__":
    main()
