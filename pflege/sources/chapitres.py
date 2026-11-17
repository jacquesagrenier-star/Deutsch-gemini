# -*- coding: utf-8 -*-
"""Les 14 chapitres de « Ma journée au service » (décision de Jacques du 16 nov. 2026, 923aa49 ; plan :
pflege/PLAN-CHAPITRES.md). SOURCE écrite à la main ; la sortie pflege/datos/chapitres.json est DÉRIVÉE par
pflege/outils/chapitres.py, qui contrôle chaque renvoi.

Un chapitre réunit, dans l'ordre d'une journée : une scène, un thème illustré (les mots en images), des conversations
et un écrit. Ici on ne range que ce qui se range à la main : scènes, dialogues, écrits, thème illustré. Les mots, les
paires, les abréviations et les cartes-phrases se rangent par leur PROPRE champ « chapitre » (posé par la session qui
les tient) ; à défaut, par la table THEME_DEFAUT (mots) ou GROUPE_DEFAUT (cartes-phrases sans dialogue) ; une carte-
phrase de dialogue suit son dialogue. La grammaire suit les dialogues (leur champ « grammaire »).

Règles :
  - chaque dialogue et chaque écrit est rangé dans UN chapitre (« dialogues », « ecrits ») ; un renvoi vers un autre
    chapitre va dans « voir_aussi » ;
  - « theme_illustre » est le nom de la page dans visuel/prototype/ (convention : soins-theme-<cle>.html), None tant
    qu'elle n'existe pas ;
  - un id de chapitre ne change jamais (l'avancement d'un compte s'y rattache).
Titres et sous-titres : français d'abord, puis les 8 autres langues d'interface de l'allemand (à relire par un natif,
comme tout texte d'interface : retours/A-RELIRE-CHAPITRES-SOINS.md).
"""

# Les 10 langues d'interface de l'allemand : l'espagnol depuis la v1205 ; décision de Jacques du 16 nov. : tout le
# contenu des Soins dans toutes les langues retenues, « dont l'espagnol » (titres espagnols : ES, en fin de fichier).
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru", "es"]

CHAPITRES = [
    {
        "id": "ch01_aufnahme", "cle": "aufnahme", "de": "Die Aufnahme",
        "titre": {"fr": "L'admission", "en": "Admission", "tr": "Hasta kabulü", "uk": "Прийом пацієнта",
                  "fa": "پذیرش بیمار", "pt": "A admissão", "ar": "استقبال المريض", "pl": "Przyjęcie pacjenta",
                  "ru": "Поступление пациента"},
        "sous_titre": {"fr": "Accueillir, questionner, noter", "en": "Welcome, ask, record",
                       "tr": "Karşılamak, sormak, kaydetmek", "uk": "Зустріти, розпитати, записати",
                       "fa": "استقبال، پرسیدن، ثبت کردن", "pt": "Acolher, perguntar, registrar",
                       "ar": "الترحيب، السؤال، التسجيل", "pl": "Przywitać, zapytać, zapisać",
                       "ru": "Встретить, расспросить, записать"},
        "scenes": ["soins-aufnahme"],
        "dialogues": ["d13-aufnahmegespraech", "d01-vorstellung"],
        "ecrits": ["soins_ecrit_aufnahme_01", "soins_ecrit_aufnahme_02", "soins_ecrit_aufnahme_03",
                   "soins_ecrit_aufnahme_04"],
        "theme_illustre": None,
    },
    {
        "id": "ch02_morgenpflege", "cle": "morgenpflege", "de": "Die Morgenpflege",
        "titre": {"fr": "Les soins du matin", "en": "Morning care", "tr": "Sabah bakımı", "uk": "Ранковий догляд",
                  "fa": "مراقبت صبحگاهی", "pt": "Os cuidados da manhã", "ar": "الرعاية الصباحية",
                  "pl": "Poranna pielęgnacja", "ru": "Утренний уход"},
        "sous_titre": {"fr": "Laver, habiller, expliquer", "en": "Wash, dress, explain",
                       "tr": "Yıkamak, giydirmek, açıklamak", "uk": "Помити, одягнути, пояснити",
                       "fa": "شستن، لباس پوشاندن، توضیح دادن", "pt": "Lavar, vestir, explicar",
                       "ar": "الغسل، الإلباس، الشرح", "pl": "Umyć, ubrać, wyjaśnić",
                       "ru": "Помыть, одеть, объяснить"},
        "scenes": ["soins-bad", "soins-zimmer-nachttisch"],
        "dialogues": ["d03-verbandswechsel", "d04-ablehnung"],
        "ecrits": [],
        "voir_aussi": {"ecrits": ["soins_ecrit_pflegebericht_01"]},
        "theme_illustre": None,
    },
    {
        "id": "ch03_mobilisation", "cle": "mobilisation", "de": "Die Mobilisation",
        "titre": {"fr": "Bouger et se lever", "en": "Moving and getting up", "tr": "Hareket ve kalkma",
                  "uk": "Рух і вставання", "fa": "حرکت و برخاستن", "pt": "Movimentar-se e levantar",
                  "ar": "الحركة والنهوض", "pl": "Ruch i wstawanie", "ru": "Движение и подъём"},
        "sous_titre": {"fr": "Aider à se lever, à marcher, à s'installer", "en": "Help to stand, walk, settle in",
                       "tr": "Kalkmaya, yürümeye, yerleşmeye yardım etmek",
                       "uk": "Допомогти встати, ходити, влаштуватися",
                       "fa": "کمک به برخاستن، راه رفتن، جاگیر شدن",
                       "pt": "Ajudar a levantar, andar, se acomodar",
                       "ar": "المساعدة على النهوض والمشي والجلوس", "pl": "Pomóc wstać, chodzić, usiąść",
                       "ru": "Помочь встать, ходить, устроиться"},
        "scenes": ["soins-zimmer-aufstehen"],
        "dialogues": ["d14-mobilisation"],
        "ecrits": [],
        "theme_illustre": None,
    },
    {
        "id": "ch04_essen", "cle": "essen", "de": "Essen und Trinken",
        "titre": {"fr": "Les repas et boire", "en": "Meals and drinking", "tr": "Yemek ve içmek",
                  "uk": "Їжа й пиття", "fa": "غذا و نوشیدن", "pt": "As refeições e a hidratação",
                  "ar": "الطعام والشراب", "pl": "Posiłki i picie", "ru": "Еда и питьё"},
        "sous_titre": {"fr": "Aider à manger, faire boire, noter", "en": "Help with eating, encourage drinking, record",
                       "tr": "Yemeğe yardım etmek, sıvı aldırmak, kaydetmek",
                       "uk": "Допомогти поїсти, дати попити, записати",
                       "fa": "کمک به غذا خوردن، دادن مایعات، ثبت کردن",
                       "pt": "Ajudar a comer, oferecer líquidos, registrar",
                       "ar": "المساعدة على الأكل، تقديم السوائل، التسجيل",
                       "pl": "Pomóc w jedzeniu, podać do picia, zapisać",
                       "ru": "Помочь поесть, дать попить, записать"},
        "scenes": ["soins-altenheim"],
        "dialogues": ["d09-essen-anreichen"],
        "ecrits": [],
        "theme_illustre": None,
    },
    {
        "id": "ch05_medikamente", "cle": "medikamente", "de": "Die Medikamente",
        "titre": {"fr": "Les médicaments", "en": "Medication", "tr": "İlaçlar", "uk": "Ліки", "fa": "داروها",
                  "pt": "Os medicamentos", "ar": "الأدوية", "pl": "Leki", "ru": "Лекарства"},
        "sous_titre": {"fr": "Préparer, donner, expliquer, redemander", "en": "Prepare, give, explain, double-check",
                       "tr": "Hazırlamak, vermek, açıklamak, tekrar sormak",
                       "uk": "Підготувати, дати, пояснити, перепитати",
                       "fa": "آماده کردن، دادن، توضیح دادن، دوباره پرسیدن",
                       "pt": "Preparar, administrar, explicar, confirmar",
                       "ar": "التحضير، الإعطاء، الشرح، الاستيضاح",
                       "pl": "Przygotować, podać, wyjaśnić, dopytać",
                       "ru": "Подготовить, дать, объяснить, переспросить"},
        "scenes": ["soins-stationszimmer", "soins-ambulant"],
        "dialogues": ["d10-medikamente", "d18-unklare-anordnung"],
        "ecrits": [],
        "theme_illustre": None,
    },
    {
        "id": "ch06_visite", "cle": "visite", "de": "Die Visite",
        "titre": {"fr": "La visite du médecin", "en": "The doctor's round", "tr": "Doktor vizitesi",
                  "uk": "Лікарський обхід", "fa": "ویزیت پزشک", "pt": "A visita médica", "ar": "جولة الطبيب",
                  "pl": "Obchód lekarski", "ru": "Врачебный обход"},
        "sous_titre": {"fr": "Présenter un patient, noter les ordres", "en": "Present a patient, note the orders",
                       "tr": "Hastayı sunmak, talimatları not almak",
                       "uk": "Представити пацієнта, записати призначення",
                       "fa": "معرفی بیمار، یادداشت دستورها",
                       "pt": "Apresentar um paciente, anotar as prescrições",
                       "ar": "تقديم المريض، تدوين التعليمات",
                       "pl": "Przedstawić pacjenta, zanotować zlecenia",
                       "ru": "Представить пациента, записать назначения"},
        "scenes": ["soins-visite"],
        "dialogues": ["d17-visite"],
        "ecrits": [],
        "theme_illustre": None,
    },
    {
        "id": "ch07_schmerz", "cle": "schmerz", "de": "Schmerzen",
        "titre": {"fr": "La douleur", "en": "Pain", "tr": "Ağrı", "uk": "Біль", "fa": "درد", "pt": "A dor",
                  "ar": "الألم", "pl": "Ból", "ru": "Боль"},
        "sous_titre": {"fr": "Demander, évaluer, noter", "en": "Ask, assess, record",
                       "tr": "Sormak, değerlendirmek, kaydetmek", "uk": "Запитати, оцінити, записати",
                       "fa": "پرسیدن، سنجیدن، ثبت کردن", "pt": "Perguntar, avaliar, registrar",
                       "ar": "السؤال، التقييم، التسجيل", "pl": "Zapytać, ocenić, zapisać",
                       "ru": "Спросить, оценить, записать"},
        "scenes": ["soins-zimmer"],
        "dialogues": ["d02-schmerzen", "d15-angst-vor-untersuchung"],
        "ecrits": ["soins_ecrit_schmerz_01"],
        "theme_illustre": None,
    },
    {
        "id": "ch08_uebergabe", "cle": "uebergabe", "de": "Die Übergabe",
        "titre": {"fr": "La relève", "en": "Handover", "tr": "Nöbet devri", "uk": "Передача зміни",
                  "fa": "تحویل شیفت", "pt": "A passagem de plantão", "ar": "تسليم المناوبة",
                  "pl": "Przekazanie dyżuru", "ru": "Передача смены"},
        "sous_titre": {"fr": "Transmettre l'essentiel, à l'oral", "en": "Pass on what matters, out loud",
                       "tr": "Önemli olanı sözlü aktarmak", "uk": "Усно передати головне",
                       "fa": "انتقال شفاهی نکات مهم", "pt": "Transmitir o essencial, em voz alta",
                       "ar": "نقل الأهم شفهيًا", "pl": "Ustnie przekazać to, co najważniejsze",
                       "ru": "Устно передать главное"},
        "scenes": ["soins-uebergabe"],
        "dialogues": ["d06-uebergabe", "d27-abenduebergabe"],
        "ecrits": ["soins_ecrit_pflegebericht_01"],
        "theme_illustre": None,
    },
    {
        "id": "ch09_dokumentation", "cle": "dokumentation", "de": "Die Dokumentation",
        "titre": {"fr": "La documentation", "en": "Documentation", "tr": "Dokümantasyon", "uk": "Документація",
                  "fa": "مستندسازی", "pt": "A documentação", "ar": "التوثيق", "pl": "Dokumentacja",
                  "ru": "Документация"},
        "sous_titre": {"fr": "Écrire juste, court et daté", "en": "Write it accurately, briefly, with the date",
                       "tr": "Doğru, kısa ve tarihli yazmak", "uk": "Писати точно, коротко й з датою",
                       "fa": "نوشتن دقیق، کوتاه و با تاریخ", "pt": "Escrever com precisão, de forma breve e com data",
                       "ar": "كتابة دقيقة وموجزة ومؤرَّخة", "pl": "Pisać dokładnie, krótko i z datą",
                       "ru": "Писать точно, кратко и с датой"},
        "scenes": ["soins-stationszimmer"],
        "dialogues": ["d21-beinahe-fehler"],
        "ecrits": ["soins_ecrit_biografie_01", "soins_ecrit_biografie_02", "soins_ecrit_biografie_03",
                   "soins_ecrit_biografie_04"],
        "theme_illustre": None,
    },
    {
        "id": "ch10_telefon", "cle": "telefon", "de": "Am Telefon",
        "titre": {"fr": "Le téléphone", "en": "On the phone", "tr": "Telefonda", "uk": "Телефон",
                  "fa": "پشت تلفن", "pt": "Ao telefone", "ar": "على الهاتف", "pl": "Przy telefonie",
                  "ru": "Телефон"},
        "sous_titre": {"fr": "Appeler le médecin, le labo, la famille", "en": "Call the doctor, the lab, the family",
                       "tr": "Doktoru, laboratuvarı, aileyi aramak",
                       "uk": "Подзвонити лікареві, в лабораторію, родині",
                       "fa": "تماس با پزشک، آزمایشگاه، خانواده",
                       "pt": "Ligar para o médico, o laboratório, a família",
                       "ar": "الاتصال بالطبيب والمختبر والعائلة",
                       "pl": "Zadzwonić do lekarza, laboratorium, rodziny",
                       "ru": "Позвонить врачу, в лабораторию, родственникам"},
        "scenes": ["soins-telefon"],
        "dialogues": ["d07-sbar", "d19-telefon", "d23-schweigepflicht"],
        "ecrits": ["soins_ecrit_telefon_01"],
        "theme_illustre": None,
    },
    {
        "id": "ch11_angehoerige", "cle": "angehoerige", "de": "Die Angehörigen",
        "titre": {"fr": "La famille du patient", "en": "The patient's family", "tr": "Hastanın ailesi",
                  "uk": "Родина пацієнта", "fa": "خانواده بیمار", "pt": "A família do paciente",
                  "ar": "عائلة المريض", "pl": "Rodzina pacjenta", "ru": "Родственники пациента"},
        "sous_titre": {"fr": "Informer, rassurer, garder le secret", "en": "Inform, reassure, keep confidentiality",
                       "tr": "Bilgilendirmek, rahatlatmak, sırrı korumak",
                       "uk": "Інформувати, заспокоїти, зберегти таємницю",
                       "fa": "اطلاع دادن، آرام کردن، حفظ راز",
                       "pt": "Informar, tranquilizar, manter o sigilo",
                       "ar": "الإعلام، الطمأنة، حفظ السر", "pl": "Informować, uspokajać, zachować tajemnicę",
                       "ru": "Сообщить, успокоить, сохранить тайну"},
        # Pas de scène à elle (un couloir, un salon des familles) : la maison de retraite en attendant.
        "scenes": ["soins-altenheim"],
        "scene_provisoire": True,
        "dialogues": ["d05-angehoerige", "d24-beschwerde", "d26-lebensende"],
        "ecrits": [],
        "voir_aussi": {"dialogues": ["d23-schweigepflicht"]},
        "theme_illustre": None,
    },
    {
        "id": "ch12_notfall", "cle": "notfall", "de": "Der Notfall",
        "titre": {"fr": "L'urgence", "en": "Emergencies", "tr": "Acil durum", "uk": "Невідкладна ситуація",
                  "fa": "وضعیت اورژانسی", "pt": "A emergência", "ar": "الحالة الطارئة", "pl": "Nagły wypadek",
                  "ru": "Неотложная ситуация"},
        "sous_titre": {"fr": "Alerter, agir, rendre compte", "en": "Raise the alarm, act, report",
                       "tr": "Alarm vermek, müdahale etmek, rapor vermek", "uk": "Підняти тривогу, діяти, доповісти",
                       "fa": "اعلام خطر، اقدام، گزارش دادن", "pt": "Dar o alarme, agir, relatar",
                       "ar": "إطلاق الإنذار، التصرف، الإبلاغ", "pl": "Zaalarmować, działać, zdać relację",
                       "ru": "Поднять тревогу, действовать, доложить"},
        # Le chariot d'urgence et le défibrillateur sont au poste (soins-telefon).
        "scenes": ["soins-telefon"],
        "dialogues": ["d16-notfall", "d08-sturz", "d12-nachts-demenz"],
        "ecrits": ["soins_ecrit_sturz_01"],
        "theme_illustre": None,
    },
    {
        "id": "ch13_entlassung", "cle": "entlassung", "de": "Die Entlassung",
        "titre": {"fr": "La sortie du patient", "en": "Discharge", "tr": "Taburculuk", "uk": "Виписка",
                  "fa": "ترخیص بیمار", "pt": "A alta do paciente", "ar": "خروج المريض", "pl": "Wypis",
                  "ru": "Выписка"},
        "sous_titre": {"fr": "Préparer le retour à la maison", "en": "Prepare the return home",
                       "tr": "Eve dönüşü hazırlamak", "uk": "Підготувати повернення додому",
                       "fa": "آماده کردن بازگشت به خانه", "pt": "Preparar a volta para casa",
                       "ar": "التحضير للعودة إلى المنزل", "pl": "Przygotować powrót do domu",
                       "ru": "Подготовить возвращение домой"},
        # Le retour à la maison : chez Frau Kowalski (soins à domicile).
        "scenes": ["soins-ambulant"],
        "dialogues": ["d25-entlassung"],
        "ecrits": [],
        "theme_illustre": None,
    },
    {
        "id": "ch14_pause", "cle": "pause", "de": "Im Pausenraum",
        "titre": {"fr": "La salle de pause", "en": "The break room", "tr": "Dinlenme odası",
                  "uk": "Кімната відпочинку", "fa": "اتاق استراحت", "pt": "A sala de descanso",
                  "ar": "غرفة الاستراحة", "pl": "Pokój socjalny", "ru": "Комната отдыха"},
        "sous_titre": {"fr": "L'équipe, le planning, les échanges", "en": "The team, the rota, swapping shifts",
                       "tr": "Ekip, nöbet çizelgesi, vardiya değişimi", "uk": "Команда, графік, обмін змінами",
                       "fa": "تیم، برنامه شیفت، جابه‌جایی شیفت", "pt": "A equipe, a escala, as trocas de plantão",
                       "ar": "الفريق، جدول المناوبات، تبادل المناوبات", "pl": "Zespół, grafik, zamiana dyżurów",
                       "ru": "Команда, график, обмен сменами"},
        "scenes": ["soins-pause"],
        "dialogues": ["d11-dienst-tauschen", "d20-praxisanleitung", "d22-kritik-im-team"],
        "ecrits": ["soins_ecrit_nachricht_01", "soins_ecrit_nachricht_02"],
        "theme_illustre": None,
    },
]

# Les mots sans champ « chapitre » : le chapitre de leur thème (base de l'id, sans le niveau). « soins_sprache »
# (les paires) et « soins_szenen » (les objets des scènes) n'ont pas de chapitre par défaut : ils se rangent mot par
# mot (session vocabulaire). Une abréviation (« RR (= Blutdruck) ») va par défaut à la relève, où on la dit.
THEME_DEFAUT = {
    "soins_koerper": "ch07_schmerz",
    "soins_grundpflege": "ch02_morgenpflege",
    "soins_hygiene": "ch02_morgenpflege",
    "soins_ernaehrung": "ch04_essen",
    "soins_medikamente": "ch05_medikamente",
    "soins_vitalzeichen": "ch06_visite",
    "soins_dokumentation": "ch09_dokumentation",
    "soins_team": "ch14_pause",
    "soins_angehoerige": "ch11_angehoerige",
    "soins_notfaelle": "ch12_notfall",
}
ABREVIATIONS_DEFAUT = "ch08_uebergabe"

# Les cartes-phrases sans dialogue (pflege/sources/redemittel/<groupe>.json) : le chapitre de leur groupe.
GROUPE_DEFAUT = {
    "patient": "ch07_schmerz",
    "famille": "ch11_angehoerige",
    "collegues": "ch14_pause",
    "negociation": "ch14_pause",
    "telephone": "ch10_telefon",
    "sbar": "ch10_telefon",
    "releve": "ch08_uebergabe",
    "visite": "ch06_visite",
}

# Ce qu'un chapitre doit réunir pour être « complet » (montré pendant l'essai ; l'app cache les autres, ou les
# montre « bientôt » si Jacques le préfère : un seul drapeau dans index.html).
# Décision de Jacques du 16 nov. : « un minimum de 8 conversations par thème ». Un seuil plus bas pour le premier jour
# (« 4 au premier jour, 8 ensuite ») se règlerait ici seulement, et Jacques seul le décide.
COMPLET = {"scenes": 1, "theme_illustre": 1, "dialogues": 8, "ecrits": 1, "mots": 20}

# L'espagnol d'interface (Amérique latine, comme celui de l'anglais appris : champEs) : titre, sous-titre.
ES = {
    "ch01_aufnahme": ("La admisión", "Recibir, preguntar, anotar"),
    "ch02_morgenpflege": ("Los cuidados de la mañana", "Asear, vestir, explicar"),
    "ch03_mobilisation": ("Moverse y levantarse", "Ayudar a levantarse, a caminar, a acomodarse"),
    "ch04_essen": ("Las comidas y la hidratación", "Ayudar a comer, dar de beber, anotar"),
    "ch05_medikamente": ("Los medicamentos", "Preparar, administrar, explicar, volver a preguntar"),
    "ch06_visite": ("La visita médica", "Presentar a un paciente, anotar las indicaciones"),
    "ch07_schmerz": ("El dolor", "Preguntar, evaluar, anotar"),
    "ch08_uebergabe": ("El cambio de turno", "Transmitir lo esencial, de viva voz"),
    "ch09_dokumentation": ("La documentación", "Escribir con precisión, breve y con fecha"),
    "ch10_telefon": ("Al teléfono", "Llamar al médico, al laboratorio, a la familia"),
    "ch11_angehoerige": ("La familia del paciente", "Informar, tranquilizar, guardar el secreto"),
    "ch12_notfall": ("La urgencia", "Dar la alarma, actuar, informar"),
    "ch13_entlassung": ("El alta del paciente", "Preparar el regreso a casa"),
    "ch14_pause": ("La sala de descanso", "El equipo, los turnos, los cambios de turno"),
}
for _c in CHAPITRES:
    if _c["id"] in ES:
        _c["titre"].setdefault("es", ES[_c["id"]][0])
        _c["sous_titre"].setdefault("es", ES[_c["id"]][1])
