# -*- coding: utf-8 -*-
"""Theme 11, hors des dix de l'annexe A — Die Dinge der Pflege : les objets que montrent les scenes
de soins et qui manquent ailleurs (demande de la session des scenes, 14 nov. 2026).

Une scene ne pointe que des mots du corpus ou des Soins : chaque liste de scene envoyee par la session
des scenes ajoute ici ses mots manquants, A LA FIN (l'ordre publie ne change plus).
Scene 1, la chambre du patient (soins-zimmer).
"""
from commun import N

THEME = {
    "cle": "szenen",
    "numero": 11,
    "nom_theme": "Die Dinge der Pflege",
    "titre": "les objets des soins | everyday care equipment | bakım malzemeleri | речі для догляду | وسایل مراقبت | أدوات الرعاية | os objetos dos cuidados | przedmioty w opiece | предметы ухода",
}

MOTS = [
    # ── scene 1 : la chambre du patient ───────────────────────────────
    N("A2", "das Wasserglas", "Wassergläser",
      "le verre d'eau | water glass | su bardağı | склянка для води | لیوان آب | كوب ماء | copo d'água | szklanka na wodę | стакан для воды",
      "Ich stelle Ihnen das Wasserglas auf den Nachttisch. | Je vous pose le verre d'eau sur la table de nuit. | I'll put the water glass on your bedside table. | Su bardağını komodinin üzerine koyuyorum. | Я ставлю вам склянку з водою на тумбочку. | لیوان آب را روی میز کنار تختتان می‌گذارم. | سأضع لك كوب الماء على الطاولة بجانب السرير. | Vou deixar o copo d'água na mesinha de cabeceira. | Stawiam Panu szklankę z wodą na szafce nocnej. | Я ставлю вам стакан с водой на тумбочку."),
    N("A2", "das Hörgerät", "Hörgeräte",
      "l'appareil auditif | hearing aid | işitme cihazı | слуховий апарат | سمعک | سمّاعة أذن طبية | aparelho auditivo | aparat słuchowy | слуховой аппарат",
      "Haben Sie Ihr Hörgerät schon drin? | Avez-vous déjà mis votre appareil auditif ? | Have you put your hearing aid in yet? | İşitme cihazınızı taktınız mı? | Ви вже вставили слуховий апарат? | سمعکتان را گذاشته‌اید؟ | هل وضعت سمّاعتك بالفعل؟ | O senhor já colocou o aparelho auditivo? | Czy ma Pan już założony aparat słuchowy? | Вы уже вставили слуховой аппарат?"),
    N("A2", "die Bettdecke", "Bettdecken",
      "la couverture, la couette | duvet, blanket | yorgan | ковдра | پتو | لحاف، غطاء السرير | cobertor, edredom | kołdra | одеяло",
      "Ist Ihnen kalt? Ich hole Ihnen eine zweite Bettdecke. | Vous avez froid ? Je vais vous chercher une deuxième couverture. | Are you cold? I'll get you a second blanket. | Üşüyor musunuz? Size ikinci bir yorgan getireyim. | Вам холодно? Я принесу вам ще одну ковдру. | سردتان است؟ یک پتوی دیگر برایتان می‌آورم. | هل تشعر بالبرد؟ سأحضر لك لحافًا آخر. | Está com frio? Vou buscar outro cobertor. | Jest Panu zimno? Przyniosę drugą kołdrę. | Вам холодно? Я принесу вам второе одеяло."),
    N("A2", "der Hausschuh", "Hausschuhe",
      "le chausson, la pantoufle | slipper | terlik | капець, домашній тапок | دمپایی (روفرشی) | خُفّ، شبشب منزلي | chinelo, pantufa | kapeć | тапочка",
      "Ziehen Sie bitte feste Hausschuhe an, bevor Sie aufstehen. | Mettez des chaussons bien fermés avant de vous lever, s'il vous plaît. | Please put on sturdy slippers before you get up. | Kalkmadan önce lütfen sağlam terlikler giyin. | Перш ніж вставати, взуйте, будь ласка, зручні закриті капці. | لطفاً قبل از بلند شدن، دمپایی محکم بپوشید. | من فضلك البس خُفًّا ثابتًا قبل أن تنهض. | Calce chinelos firmes antes de se levantar, por favor. | Proszę założyć stabilne kapcie, zanim Pan wstanie. | Пожалуйста, наденьте устойчивые тапочки, прежде чем вставать."),
    N("B1", "das Pflegebett", "Pflegebetten",
      "le lit médicalisé | hospital bed, care bed | hasta yatağı | функціональне ліжко | تخت بیمارستانی | سرير طبي | cama hospitalar | łóżko rehabilitacyjne (szpitalne) | функциональная кровать",
      "Das Pflegebett fahren wir für die Körperpflege auf Arbeitshöhe. | Pour la toilette, on monte le lit médicalisé à hauteur de travail. | For personal care, we raise the hospital bed to working height. | Vücut bakımı için hasta yatağını çalışma yüksekliğine getiriyoruz. | Для гігієнічних процедур ми піднімаємо функціональне ліжко на робочу висоту. | برای شست‌وشو، تخت بیمارستانی را تا ارتفاع کار بالا می‌بریم. | نرفع السرير الطبي إلى ارتفاع العمل من أجل العناية الشخصية. | Para a higiene, subimos a cama hospitalar até a altura de trabalho. | Do toalety podnosimy łóżko na wysokość roboczą. | Для гигиенических процедур мы поднимаем функциональную кровать на рабочую высоту."),
    N("B1", "das Bettgitter", "Bettgitter",
      "la barrière de lit (ridelle) | bed rail | yatak kenarlığı | бокові поручні ліжка | نردهٔ کنار تخت | حاجز السرير | grade da cama | barierka łóżka | боковое ограждение кровати",
      "Ein Bettgitter ist eine freiheitsentziehende Maßnahme: Es braucht die Einwilligung des Patienten oder eine richterliche Genehmigung. | Une barrière de lit est une mesure de contention : il faut le consentement du patient ou l'autorisation d'un juge. | A bed rail is a restraint: it requires the patient's consent or a court's approval. | Yatak kenarlığı özgürlüğü kısıtlayan bir önlemdir: hastanın onayı ya da mahkeme izni gerekir. | Бокові поручні — це захід обмеження свободи: потрібна згода пацієнта або дозвіл суду. | نردهٔ کنار تخت یک اقدام محدودکنندهٔ آزادی است: رضایت بیمار یا اجازهٔ دادگاه لازم است. | حاجز السرير إجراء يقيّد الحرية: يحتاج إلى موافقة المريض أو إذن من المحكمة. | A grade da cama é uma medida de contenção: exige o consentimento do paciente ou autorização judicial. | Barierka łóżka to środek ograniczający wolność: wymaga zgody pacjenta albo zgody sądu. | Боковое ограждение — это мера ограничения свободы: нужно согласие пациента или разрешение суда.",
      relire=True, note="Freiheitsentziehende Maßnahme (§ 1831 BGB) : consentement de la personne capable, sinon de son représentant avec l'autorisation du tribunal ; la phrase simplifie, à valider."),
    N("B1", "das Kopfteil", "Kopfteile",
      "la tête de lit (le dossier du lit) | head of the bed, backrest | yatağın baş kısmı | узголівʼя ліжка | قسمت سر تخت | رأس السرير | cabeceira da cama | wezgłowie łóżka | изголовье кровати",
      "Mit dem Kopfteil etwas höher bekommt sie besser Luft. | Avec la tête de lit un peu plus haute, elle respire mieux. | With the head of the bed a little higher, she can breathe more easily. | Yatağın baş kısmı biraz daha yüksek olunca daha rahat nefes alıyor. | Коли узголівʼя трохи вище, їй легше дихати. | وقتی قسمت سر تخت کمی بالاتر باشد، راحت‌تر نفس می‌کشد. | عندما يكون رأس السرير أعلى قليلًا تتنفس بسهولة أكبر. | Com a cabeceira um pouco mais alta, ela respira melhor. | Z wezgłowiem trochę wyżej łatwiej jej oddychać. | Когда изголовье чуть выше, ей легче дышать."),
    N("B1", "die Prothesendose", "Prothesendosen",
      "la boîte à prothèse dentaire | denture box | protez kabı | контейнер для зубного протеза | جعبهٔ دندان مصنوعی | علبة طقم الأسنان | caixinha da prótese dentária | pojemnik na protezę zębową | контейнер для зубного протеза",
      "Die Zahnprothese liegt über Nacht in der Prothesendose mit seinem Namen. | La nuit, la prothèse dentaire est rangée dans sa boîte, à son nom. | At night, the denture is kept in the denture box labelled with his name. | Gece boyunca diş protezi, üzerinde adı yazan protez kabında duruyor. | На ніч зубний протез лежить у підписаному контейнері. | دندان مصنوعی شب‌ها در جعبه‌ای می‌ماند که نامش روی آن است. | يُحفظ طقم الأسنان ليلًا في علبته التي تحمل اسمه. | À noite, a prótese dentária fica na caixinha com o nome dele. | Na noc proteza leży w pojemniku podpisanym jego nazwiskiem. | На ночь зубной протез лежит в подписанном контейнере."),
    N("B1", "der Infusionsständer", "Infusionsständer",
      "la potence (à perfusion) | drip stand, IV pole | serum askısı | штатив для крапельниці | پایهٔ سرم | حامل المحلول الوريدي | suporte de soro | stojak na kroplówkę | штатив для капельницы",
      "Schieben Sie den Infusionsständer mit, wenn Sie zur Toilette gehen. | Poussez la potence avec vous quand vous allez aux toilettes. | Push the drip stand along with you when you go to the toilet. | Tuvalete giderken serum askısını yanınızda itin. | Коли йдете до туалету, котіть штатив для крапельниці з собою. | وقتی به دستشویی می‌روید، پایهٔ سرم را هم با خودتان ببرید. | ادفع حامل المحلول معك عندما تذهب إلى الحمام. | Leve o suporte de soro com você quando for ao banheiro. | Proszę zabrać stojak na kroplówkę ze sobą, idąc do toalety. | Когда пойдёте в туалет, везите штатив для капельницы с собой."),
    N("B1", "der Desinfektionsmittelspender", "Desinfektionsmittelspender",
      "le distributeur de solution hydro-alcoolique | hand sanitiser dispenser | dezenfektan dispenseri | дозатор антисептика | دستگاه مایع ضدعفونی | موزّع المطهّر | dispensador de álcool em gel | dozownik środka dezynfekcyjnego | дозатор антисептика",
      "Der Desinfektionsmittelspender hängt direkt neben der Tür. | Le distributeur de solution hydro-alcoolique est juste à côté de la porte. | The hand sanitiser dispenser hangs right next to the door. | Dezenfektan dispenseri kapının hemen yanında asılı. | Дозатор антисептика висить просто біля дверей. | دستگاه مایع ضدعفونی درست کنار در نصب شده است. | موزّع المطهّر معلّق بجانب الباب مباشرة. | O dispensador de álcool em gel fica bem ao lado da porta. | Dozownik środka dezynfekcyjnego wisi tuż przy drzwiach. | Дозатор антисептика висит прямо у двери."),
    N("B1", "das Patientenarmband", "Patientenarmbänder",
      "le bracelet d'identification | patient ID wristband | hasta kimlik bilekliği | ідентифікаційний браслет пацієнта | دستبند شناسایی بیمار | سوار تعريف المريض | pulseira de identificação | opaska identyfikacyjna pacjenta | идентификационный браслет пациента",
      "Vor jeder Gabe prüfe ich den Namen auf dem Patientenarmband. | Avant chaque administration, je vérifie le nom sur le bracelet d'identification. | Before each dose, I check the name on the patient wristband. | Her ilaç vermeden önce bileklikteki ismi kontrol ediyorum. | Перед кожним введенням ліків я звіряю імʼя на браслеті пацієнта. | قبل از دادن هر دارو، نام روی دستبند بیمار را بررسی می‌کنم. | قبل كل إعطاء للدواء أتحقق من الاسم على سوار المريض. | Antes de cada administração, confiro o nome na pulseira de identificação. | Przed każdym podaniem leku sprawdzam nazwisko na opasce pacjenta. | Перед каждым введением лекарства я сверяю имя на браслете пациента."),
    N("B1", "der Sichtschutz", "—",
      "le paravent | privacy screen | paravan | ширма | پاراوان (پردهٔ جداکننده) | حاجز الخصوصية | biombo | parawan | ширма",
      "Bevor ich Sie wasche, stelle ich den Sichtschutz auf. | Avant de faire votre toilette, j'installe le paravent. | Before I wash you, I'll put up the privacy screen. | Sizi yıkamadan önce paravanı kuruyorum. | Перш ніж вас мити, я поставлю ширму. | پیش از شست‌وشوی شما، پاراوان را می‌گذارم. | قبل أن أغسّلك سأضع حاجز الخصوصية. | Antes de dar o banho, coloco o biombo. | Zanim Pana umyję, ustawię parawan. | Прежде чем вас мыть, я поставлю ширму."),
    N("B2", "die Nasenbrille", "Nasenbrillen",
      "les lunettes à oxygène | nasal cannula | nazal kanül | носова канюля | کانول بینی | قُنية أنفية | cateter nasal tipo óculos | wąsy tlenowe (kaniula donosowa) | носовая канюля",
      "Die Nasenbrille sitzt nicht richtig, deshalb ist die Sättigung gefallen. | Les lunettes à oxygène sont mal placées, c'est pour ça que la saturation a baissé. | The nasal cannula isn't sitting properly, that's why the saturation has dropped. | Nazal kanül düzgün yerleşmemiş, bu yüzden satürasyon düştü. | Носова канюля стоїть неправильно, тому сатурація знизилася. | کانول بینی درست قرار نگرفته، برای همین اشباع اکسیژن پایین آمده است. | القُنية الأنفية ليست في مكانها الصحيح، لذلك انخفض التشبّع. | O cateter nasal não está bem colocado, por isso a saturação caiu. | Wąsy tlenowe są źle założone, dlatego saturacja spadła. | Носовая канюля стоит неправильно, поэтому сатурация упала.",
      relire=True),
    N("B2", "der Sauerstoff", "—",
      "l'oxygène | oxygen | oksijen | кисень | اکسیژن | أكسجين | oxigênio | tlen | кислород",
      "Er bekommt Sauerstoff nach ärztlicher Anordnung, zwei Liter pro Minute. | Il reçoit de l'oxygène sur prescription médicale, deux litres par minute. | He receives oxygen as prescribed by the doctor, two litres per minute. | Doktor istemine göre dakikada iki litre oksijen alıyor. | Він отримує кисень за призначенням лікаря, два літри на хвилину. | طبق دستور پزشک، دقیقه‌ای دو لیتر اکسیژن می‌گیرد. | يتلقى الأكسجين حسب وصفة الطبيب، لترين في الدقيقة. | Ele recebe oxigênio por prescrição médica, dois litros por minuto. | Dostaje tlen zgodnie ze zleceniem lekarza, dwa litry na minutę. | Он получает кислород по назначению врача, два литра в минуту.",
      relire=True, note="Débit donné à titre d'exemple ; il ne doit pas passer pour une consigne."),
]
