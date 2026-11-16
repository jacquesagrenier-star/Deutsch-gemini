# -*- coding: utf-8 -*-
"""« Les contraires » dans les langues d'interface sans phrase traduite jusqu'ici (lot 3 de l'alignement des themes,
16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, et l'arabe pour qui
apprend l'espagnol.

LE CHEMIN NATIF : contrarios.py traduit deja chaque phrase de la page A LA MAIN, en francais, anglais et portugais
(TRAD_IMG, TRAD_ATTR, TRAD_PHRASES_DE, TRAD_PHRASES_ES, TRAD_DIT) : le theme n'est pas combinatoire (58 phrases en
allemand, 49 en espagnol). On ajoute donc les colonnes des six langues, phrase par phrase, au meme endroit. Les
adjectifs suivent les gloses du corpus (adjectif.json, adjetivos.json), que la page montre a cote : komisch / seltsam
gardent deux mots distincts la ou la langue en a deux (garip / tuhaf, чудной / странный, غریب / عجیب).

Points douteux : retours/A-RELIRE-THEMES-<LG>.md (a relire par un natif).
"""

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")


def _t(*v):
    return dict(zip(LANGUES, v))


# L'image et son mot : « Die Straße ist breit. » (allemand) ; l'arabe sert aussi a « La calle es ancha. » (espagnol)
IMG = {
    "calle-ancha":      _t("Cadde geniş.", "Вулиця широка.", "Ulica jest szeroka.", "Улица широкая.", "خیابان پهن است.", "الشارع عريض."),
    "calle-estrecha":   _t("Cadde dar.", "Вулиця вузька.", "Ulica jest wąska.", "Улица узкая.", "خیابان باریک است.", "الشارع ضيّق."),
    "puerta-abierta":   _t("Kapı açık.", "Двері відчинені.", "Drzwi są otwarte.", "Дверь открыта.", "در باز است.", "الباب مفتوح."),
    "puerta-cerrada":   _t("Kapı kapalı.", "Двері зачинені.", "Drzwi są zamknięte.", "Дверь закрыта.", "در بسته است.", "الباب مغلق."),
    "jarron-bonito":    _t("Vazo güzel.", "Ваза гарна.", "Wazon jest ładny.", "Ваза красивая.", "گلدان زیباست.", "المزهرية جميلة."),
    "jarron-feo":       _t("Vazo çirkin.", "Ваза потворна.", "Wazon jest brzydki.", "Ваза уродливая.", "گلدان زشت است.", "المزهرية قبيحة."),
    "pastel-bueno":     _t("Pasta lezzetli.", "Торт смачний.", "Ciasto jest dobre.", "Торт вкусный.", "کیک خوشمزه است.", "الكعكة لذيذة."),
    "comida-asquerosa": _t("Yemek iğrenç.", "Їжа огидна.", "Jedzenie jest obrzydliwe.", "Еда отвратительная.", "غذا چندش‌آور است.", "الطعام مقزّز."),
    "manzana-mala":     _t("Elma çürük.", "Яблуко зіпсоване.", "Jabłko jest zepsute.", "Яблоко испорченное.", "سیب خراب است.", "التفاحة فاسدة."),
    "tetera-rara":      _t("Çaydanlık garip.", "Чайник чудернацький.", "Imbryk jest dziwaczny.", "Чайник чудной.", "قوری غریب است.", "إبريق الشاي غريب."),
    "silla-extrana":    _t("Sandalye tuhaf.", "Стілець дивний.", "Krzesło jest dziwne.", "Стул странный.", "صندلی عجیب است.", "الكرسي عجيب."),
    "vista-preciosa":   _t("Manzara harika.", "Краєвид прекрасний.", "Widok jest przepiękny.", "Вид прекрасный.", "منظره دل‌انگیز است.", "المنظر رائع."),
    "maleta-grande":    _t("Bavul büyük.", "Валіза велика.", "Walizka jest duża.", "Чемодан большой.", "چمدان بزرگ است.", "الحقيبة كبيرة."),
    "maleta-pequena":   _t("Bavul küçük.", "Валіза маленька.", "Walizka jest mała.", "Чемодан маленький.", "چمدان کوچک است.", "الحقيبة صغيرة."),
    "bici-nueva":       _t("Bisiklet yeni.", "Велосипед новий.", "Rower jest nowy.", "Велосипед новый.", "دوچرخه نو است.", "الدراجة جديدة."),
    "bici-vieja":       _t("Bisiklet eski.", "Велосипед старий.", "Rower jest stary.", "Велосипед старый.", "دوچرخه کهنه است.", "الدراجة قديمة."),
    "vaso-lleno":       _t("Bardak dolu.", "Склянка повна.", "Szklanka jest pełna.", "Стакан полный.", "لیوان پر است.", "الكوب ممتلئ."),
    "vaso-vacio":       _t("Bardak boş.", "Склянка порожня.", "Szklanka jest pusta.", "Стакан пустой.", "لیوان خالی است.", "الكوب فارغ."),
}

# « Das ist ein großer Koffer. » (la terminaison, en allemand seulement)
ATTR = {
    "calle-ancha":      _t("Bu geniş bir cadde.", "Це широка вулиця.", "To szeroka ulica.", "Это широкая улица.", "این یک خیابان پهن است.", "هذا شارع عريض."),
    "calle-estrecha":   _t("Bu dar bir cadde.", "Це вузька вулиця.", "To wąska ulica.", "Это узкая улица.", "این یک خیابان باریک است.", "هذا شارع ضيّق."),
    "puerta-abierta":   _t("Bu açık bir kapı.", "Це відчинені двері.", "To otwarte drzwi.", "Это открытая дверь.", "این یک در باز است.", "هذا باب مفتوح."),
    "puerta-cerrada":   _t("Bu kapalı bir kapı.", "Це зачинені двері.", "To zamknięte drzwi.", "Это закрытая дверь.", "این یک در بسته است.", "هذا باب مغلق."),
    "jarron-bonito":    _t("Bu güzel bir vazo.", "Це гарна ваза.", "To ładny wazon.", "Это красивая ваза.", "این یک گلدان زیباست.", "هذه مزهرية جميلة."),
    "jarron-feo":       _t("Bu çirkin bir vazo.", "Це потворна ваза.", "To brzydki wazon.", "Это уродливая ваза.", "این یک گلدان زشت است.", "هذه مزهرية قبيحة."),
    "pastel-bueno":     _t("Bu lezzetli bir pasta.", "Це смачний торт.", "To dobre ciasto.", "Это вкусный торт.", "این یک کیک خوشمزه است.", "هذه كعكة لذيذة."),
    "comida-asquerosa": _t("Bu iğrenç bir yemek.", "Це огидна їжа.", "To obrzydliwe jedzenie.", "Это отвратительная еда.", "این یک غذای چندش‌آور است.", "هذا طعام مقزّز."),
    "manzana-mala":     _t("Bu çürük bir elma.", "Це зіпсоване яблуко.", "To zepsute jabłko.", "Это испорченное яблоко.", "این یک سیب خراب است.", "هذه تفاحة فاسدة."),
    "tetera-rara":      _t("Bu garip bir çaydanlık.", "Це чудернацький чайник.", "To dziwaczny imbryk.", "Это чудной чайник.", "این یک قوری غریب است.", "هذا إبريق شاي غريب."),
    "silla-extrana":    _t("Bu tuhaf bir sandalye.", "Це дивний стілець.", "To dziwne krzesło.", "Это странный стул.", "این یک صندلی عجیب است.", "هذا كرسي عجيب."),
    "vista-preciosa":   _t("Bu harika bir manzara.", "Це прекрасний краєвид.", "To przepiękny widok.", "Это прекрасный вид.", "این یک منظرهٔ دل‌انگیز است.", "هذا منظر رائع."),
    "maleta-grande":    _t("Bu büyük bir bavul.", "Це велика валіза.", "To duża walizka.", "Это большой чемодан.", "این یک چمدان بزرگ است.", "هذه حقيبة كبيرة."),
    "maleta-pequena":   _t("Bu küçük bir bavul.", "Це маленька валіза.", "To mała walizka.", "Это маленький чемодан.", "این یک چمدان کوچک است.", "هذه حقيبة صغيرة."),
    "bici-nueva":       _t("Bu yeni bir bisiklet.", "Це новий велосипед.", "To nowy rower.", "Это новый велосипед.", "این یک دوچرخهٔ نو است.", "هذه دراجة جديدة."),
    "bici-vieja":       _t("Bu eski bir bisiklet.", "Це старий велосипед.", "To stary rower.", "Это старый велосипед.", "این یک دوچرخهٔ کهنه است.", "هذه دراجة قديمة."),
    "vaso-lleno":       _t("Bu dolu bir bardak.", "Це повна склянка.", "To pełna szklanka.", "Это полный стакан.", "این یک لیوان پر است.", "هذا كوب ممتلئ."),
    "vaso-vacio":       _t("Bu boş bir bardak.", "Це порожня склянка.", "To pusta szklanka.", "Это пустой стакан.", "این یک لیوان خالی است.", "هذا كوب فارغ."),
}

# Les phrases sans image (allemand), telles que la page les affiche une fois completees
PHRASES_DE = {
    "Das ist ein breiter Fluss.":         _t("Bu geniş bir nehir.", "Це широка річка.", "To szeroka rzeka.", "Это широкая река.", "این یک رودخانهٔ پهن است.", "هذا نهر عريض."),
    "Das ist ein schmaler Weg.":          _t("Bu dar bir yol.", "Це вузька стежка.", "To wąska ścieżka.", "Это узкая тропинка.", "این یک راه باریک است.", "هذا طريق ضيّق."),
    "Das ist eine schmale Brücke.":       _t("Bu dar bir köprü.", "Це вузький міст.", "To wąski most.", "Это узкий мост.", "این یک پل باریک است.", "هذا جسر ضيّق."),
    "Das ist ein offenes Fenster.":       _t("Bu açık bir pencere.", "Це відчинене вікно.", "To otwarte okno.", "Это открытое окно.", "این یک پنجرهٔ باز است.", "هذه نافذة مفتوحة."),
    "Das ist ein geschlossenes Fenster.": _t("Bu kapalı bir pencere.", "Це зачинене вікно.", "To zamknięte okno.", "Это закрытое окно.", "این یک پنجرهٔ بسته است.", "هذه نافذة مغلقة."),
    "Das ist ein schöner Garten.":        _t("Bu güzel bir bahçe.", "Це гарний сад.", "To piękny ogród.", "Это красивый сад.", "این یک باغ زیباست.", "هذه حديقة جميلة."),
    "Das ist ein hässliches Hemd.":       _t("Bu çirkin bir gömlek.", "Це потворна сорочка.", "To brzydka koszula.", "Это уродливая рубашка.", "این یک پیراهن زشت است.", "هذا قميص قبيح."),
    "Das ist ein gutes Restaurant.":      _t("Bu iyi bir restoran.", "Це хороший ресторан.", "To dobra restauracja.", "Это хороший ресторан.", "این یک رستوران خوب است.", "هذا مطعم جيد."),
    "Das ist ein schlechter Film.":       _t("Bu kötü bir film.", "Це поганий фільм.", "To zły film.", "Это плохой фильм.", "این یک فیلم بد است.", "هذا فيلم سيّئ."),
    "Das ist ein ekliger Geruch.":        _t("Bu iğrenç bir koku.", "Це огидний запах.", "To obrzydliwy zapach.", "Это отвратительный запах.", "این یک بوی چندش‌آور است.", "هذه رائحة مقزّزة."),
    "Das ist ein komisches Geräusch.":    _t("Bu garip bir ses.", "Це чудернацький звук.", "To dziwaczny dźwięk.", "Это чудной звук.", "این یک صدای غریب است.", "هذا صوت غريب."),
    "Das ist eine seltsame Frage.":       _t("Bu tuhaf bir soru.", "Це дивне питання.", "To dziwne pytanie.", "Это странный вопрос.", "این یک سؤال عجیب است.", "هذا سؤال عجيب."),
    "Das ist ein wunderschöner Abend.":   _t("Bu harika bir akşam.", "Це прекрасний вечір.", "To przepiękny wieczór.", "Это прекрасный вечер.", "این یک شب دل‌انگیز است.", "هذا مساء رائع."),
    "Das ist ein großes Haus.":           _t("Bu büyük bir ev.", "Це великий будинок.", "To duży dom.", "Это большой дом.", "این یک خانهٔ بزرگ است.", "هذا بيت كبير."),
    "Das ist eine kleine Wohnung.":       _t("Bu küçük bir daire.", "Це маленька квартира.", "To małe mieszkanie.", "Это маленькая квартира.", "این یک آپارتمان کوچک است.", "هذه شقة صغيرة."),
    "Das ist ein neues Handy.":           _t("Bu yeni bir telefon.", "Це новий телефон.", "To nowy telefon.", "Это новый телефон.", "این یک گوشی نو است.", "هذا هاتف جديد."),
    "Das ist eine alte Kirche.":          _t("Bu eski bir kilise.", "Це стара церква.", "To stary kościół.", "Это старая церковь.", "این یک کلیسای قدیمی است.", "هذه كنيسة قديمة."),
    "Das ist ein voller Bus.":            _t("Bu dolu bir otobüs.", "Це повний автобус.", "To pełny autobus.", "Это полный автобус.", "این یک اتوبوس پر است.", "هذه حافلة ممتلئة."),
    "Das ist eine leere Flasche.":        _t("Bu boş bir şişe.", "Це порожня пляшка.", "To pusta butelka.", "Это пустая бутылка.", "این یک بطری خالی است.", "هذه زجاجة فارغة."),
    # la decouverte, prise au corpus
    "Die Straße ist sehr breit.":         _t("Cadde çok geniş.", "Вулиця дуже широка.", "Ulica jest bardzo szeroka.", "Улица очень широкая.", "خیابان خیلی پهن است.", "الشارع عريض جدًا."),
    "Die Gasse ist eng und schmal.":      _t("Ara sokak dar ve sıkışık.", "Провулок тісний і вузький.", "Uliczka jest ciasna i wąska.", "Переулок тесный и узкий.", "کوچه تنگ و باریک است.", "الزقاق ضيّق ومحصور."),
    "Der Kuchen schmeckt sehr gut.":      _t("Pasta çok lezzetli.", "Торт дуже смачний.", "Ciasto bardzo dobrze smakuje.", "Торт очень вкусный.", "کیک خیلی خوشمزه است.", "الكعكة لذيذة جدًا."),
}

# L'arabe pour qui apprend l'espagnol : les phrases sans image et celle de la decouverte (les images : IMG ci-dessus)
ES_AR = {
    "El pasillo es ancho.": "الممر عريض.",
    "Este río es muy ancho.": "هذا النهر عريض جدًا.",
    "La carretera es muy estrecha.": "الطريق ضيّق جدًا.",
    "El puente es estrecho.": "الجسر ضيّق.",
    "La tienda está abierta.": "المتجر مفتوح.",
    "La ventana está abierta.": "النافذة مفتوحة.",
    "El banco está abierto.": "البنك مفتوح.",
    "El museo está cerrado.": "المتحف مغلق.",
    "La farmacia está cerrada.": "الصيدلية مغلقة.",
    "La plaza es muy grande.": "الساحة كبيرة جدًا.",
    "El parque es grande.": "المنتزه كبير.",
    "El baño es pequeño.": "الحمّام صغير.",
    "La cocina es pequeña.": "المطبخ صغير.",
    "El autobús está lleno.": "الحافلة ممتلئة.",
    "La caja está llena.": "الصندوق ممتلئ.",
    "La botella está vacía.": "الزجاجة فارغة.",
    "El tren está vacío.": "القطار فارغ.",
    "La plaza es muy bonita.": "الساحة جميلة جدًا.",
    "El edificio es bastante feo.": "المبنى قبيح إلى حدٍّ ما.",
    "La casa es nueva.": "البيت جديد.",
    "El sofá es nuevo.": "الأريكة جديدة.",
    "El puente es muy viejo.": "الجسر قديم جدًا.",
    "La iglesia es muy vieja.": "الكنيسة قديمة جدًا.",
    "La playa es preciosa.": "الشاطئ رائع.",
    "El jardín es precioso.": "الحديقة رائعة.",
    "Este libro es muy raro.": "هذا الكتاب غريب جدًا.",
    "La situación es extraña.": "الوضع عجيب.",
    "La sopa está muy buena.": "الحساء لذيذ جدًا.",
    "La leche está mala.": "الحليب فاسد.",
    "El café de la máquina está asqueroso.": "قهوة الآلة مقزّزة.",
    # la decouverte, prise au corpus
    "La calle es muy estrecha.": "الشارع ضيّق جدًا.",
}
