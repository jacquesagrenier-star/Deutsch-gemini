// « Les démarches » dans les langues d'interface sans phrase traduite jusqu'ici (lot 4 de l'alignement des thèmes,
// 16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, l'arabe pour qui
// apprend l'espagnol.
//
// LE CHEMIN NATIF : la page fabrique ses phrases traduites à partir de morceaux (la démarche de Mark avec {L} pour le
// lieu, le lieu, le document, le champ du formulaire, l'avis, les heures, le rendez-vous). On donne ici ces morceaux
// dans chaque langue, rangés par clé (id de la démarche, du lieu, du document, du champ, de l'avis), et chaque langue
// assemble ses phrases avec sa grammaire : le genre du document qui accorde « нужен / нужна / нужно », le jour à
// l'accusatif (в среду, w środę, у пʼятницю), le suffixe turc après l'heure (saat 15.00'te, 9.30'da), l'accord de
// « ouvert / fermé » avec le lieu. Le champ du formulaire est un gabarit entier ({v} = la valeur), qui porte la
// tournure de chaque langue (« Mark'ın uyruğu … », « Гражданство Марка — … »).
//
// Les noms propres sont transcrits là où la langue n'a pas l'alphabet latin (Марк Гарнье, مارك غارنييه) ; les leurres
// (Marc, Max, Garnet…) restent tels quels et ne montrent pas de traduction.
// Points douteux : retours/A-RELIRE-THEMES-<LG>.md (à relire par un natif).

function installerLanguesDemarches(D){
  // ---------- les jours (lundi = 1) ----------
  const JOURS = {
    tr: ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"],
    uk: ["понеділок", "вівторок", "середа", "четвер", "пʼятниця", "субота", "неділя"],
    pl: ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"],
    ru: ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"],
    fa: ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"],
    ar: ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
  };
  // le jour à l'accusatif, après « в / у / w » (quand ?) et après « на » (pour quel jour ?)
  const QUAND = {
    uk: ["у понеділок", "у вівторок", "у середу", "у четвер", "у пʼятницю", "у суботу", "у неділю"],
    pl: ["w poniedziałek", "we wtorek", "w środę", "w czwartek", "w piątek", "w sobotę", "w niedzielę"],
    ru: ["в понедельник", "во вторник", "в среду", "в четверг", "в пятницу", "в субботу", "в воскресенье"]
  };
  const POUR = {
    uk: ["понеділок", "вівторок", "середу", "четвер", "пʼятницю", "суботу", "неділю"],
    ru: ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
  };
  const hm = h => Math.floor(h) + ":" + (h % 1 ? "30" : "00");
  // le turc : « saat 15.00'te », « saat 9.30'da » -- le suffixe suit le dernier mot lu (on beş, dokuz otuz)
  const SUF_TR = {7: "'de", 8: "'de", 9: "'da", 10: "'da", 11: "'de", 12: "'de", 13: "'te", 14: "'te", 15: "'te", 16: "'da", 17: "'de", 18: "'de", 19: "'da", 20: "'de"};
  const saatTr = h => "saat " + Math.floor(h) + "." + (h % 1 ? "30'da" : "00" + SUF_TR[Math.floor(h)]);
  const maj = s => s.charAt(0).toUpperCase() + s.slice(1);
  const ACCORD = {   // ouvert / fermé selon le genre du lieu (m, f, n)
    uk: {o: {m: "відчинений", f: "відчинена", n: "відчинене"}, f: {m: "зачинений", f: "зачинена", n: "зачинене"}},
    pl: {o: {m: "otwarty", f: "otwarta", n: "otwarte"}, f: {m: "zamknięty", f: "zamknięta", n: "zamknięte"}},
    ru: {o: {m: "открыт", f: "открыта", n: "открыто"}, f: {m: "закрыт", f: "закрыта", n: "закрыто"}},
    ar: {o: {m: "مفتوح", f: "مفتوحة"}, f: {m: "مغلق", f: "مغلقة"}}
  };
  const BESOIN = {   // « il faut » accordé avec le document
    uk: {m: "потрібен", f: "потрібна", n: "потрібне", pl: "потрібні"},
    pl: {m: "potrzebny jest", f: "potrzebna jest", n: "potrzebne jest", pl: "potrzebne są"},
    ru: {m: "нужен", f: "нужна", n: "нужно", pl: "нужны"}
  };

  // ---------- les phrases, langue par langue ----------
  const B = {
    tr: {
      nom: "Mark Garnier",
      doc: (k, t) => "Bu " + t + ".",
      avis: (p, k, t) => p + " " + t + " gerekiyor.",
      horaire: (lt, j, h, o) => JOURS.tr[j - 1] + " " + saatTr(h) + " " + lt[0] + " " + (o ? "açık" : "kapalı") + ".",
      termin: (lt, j, h) => "Mark'ın randevusu " + JOURS.tr[j - 1] + " günü " + saatTr(h) + ", " + lt[1] + "."
    },
    uk: {
      nom: "Марк Гарньє",
      doc: (k, t) => "Це " + t + ".",
      avis: (p, k, t, g) => p + " " + BESOIN.uk[g || "m"] + " " + t + ".",
      horaire: (lt, j, h, o) => maj(QUAND.uk[j - 1]) + " о " + hm(h) + " " + lt[0] + " " + ACCORD.uk[o ? "o" : "f"][lt[2] || "m"] + ".",
      termin: (lt, j, h) => "Марк записаний на " + POUR.uk[j - 1] + " на " + hm(h) + " " + lt[1] + "."
    },
    pl: {
      nom: "Mark Garnier",
      doc: (k, t) => "To " + t + ".",
      avis: (p, k, t, g) => p + " " + BESOIN.pl[g || "m"] + " " + t + ".",
      horaire: (lt, j, h, o) => maj(QUAND.pl[j - 1]) + " o " + hm(h) + " " + lt[0] + " jest " + ACCORD.pl[o ? "o" : "f"][lt[2] || "m"] + ".",
      termin: (lt, j, h) => "Mark ma wizytę " + QUAND.pl[j - 1] + " o " + hm(h) + " " + lt[1] + "."
    },
    ru: {
      nom: "Марк Гарнье",
      doc: (k, t) => "Это " + t + ".",
      avis: (p, k, t, g) => p + " " + BESOIN.ru[g || "m"] + " " + t + ".",
      horaire: (lt, j, h, o) => maj(QUAND.ru[j - 1]) + " в " + hm(h) + " " + lt[0] + " " + ACCORD.ru[o ? "o" : "f"][lt[2] || "m"] + ".",
      termin: (lt, j, h) => "Марк записан на " + POUR.ru[j - 1] + " на " + hm(h) + " " + lt[1] + "."
    },
    fa: {
      nom: "مارک گارنیه",
      doc: (k, t) => "این " + t + " است.",
      avis: (p, k, t) => p + "، " + t + " لازم است.",
      horaire: (lt, j, h, o) => JOURS.fa[j - 1] + " ساعت " + hm(h) + "، " + lt[0] + " " + (o ? "باز" : "بسته") + " است.",
      termin: (lt, j, h) => "وقت مارک " + JOURS.fa[j - 1] + " ساعت " + hm(h) + " " + lt[1] + " است."
    },
    ar: {
      nom: "مارك غارنييه",
      doc: (k, t, g) => (g === "f" ? "هذه " : "هذا ") + t + ".",
      avis: (p, k, t) => p + "، تحتاج إلى " + t + ".",
      horaire: (lt, j, h, o) => lt[0] + " " + ACCORD.ar[o ? "o" : "f"][lt[2] || "m"] + " يوم " + JOURS.ar[j - 1] + " في الساعة " + hm(h) + ".",
      termin: (lt, j, h) => "موعد مارك يوم " + JOURS.ar[j - 1] + " في الساعة " + hm(h) + " " + lt[1] + "."
    }
  };

  // ---------- les morceaux, pour qui apprend l'allemand ----------
  // lieux : [le lieu, « au lieu », genre] ; docs : [le document, genre] ; demarches : [phrase de Mark ({L} = le lieu),
  // phrase polie du guichet ou null] ; champs : [gabarit ({v}), libellé court, valeur juste traduite ou null], et les
  // leurres traduits (tf) ; avis : le début de la phrase (« Pour ouvrir un compte »).
  const DE = {
    tr: {
      lieux: {buergeramt: ["vatandaş hizmetleri bürosu", "vatandaş hizmetleri bürosunda"], bank: ["banka", "bankada"],
              krankenkasse: ["hastalık sigortası kurumu", "hastalık sigortası kurumunda"], praxis: ["muayenehane", "muayenehanede"]},
      docs: {pass: ["pasaport"], formular: ["form"], meldebescheinigung: ["ikamet belgesi"], versichertenkarte: ["sağlık sigorta kartı"],
             arbeitsvertrag: ["iş sözleşmesi"], mietvertrag: ["kira sözleşmesi"], foto: ["fotoğraf"], karte: ["banka kartı"], bestaetigung: ["ev sahibinin onay belgesi"]},
      demarches: {
        nummer: ["Mark{L} sıra numarası alıyor.", "Lütfen bir sıra numarası alın."],
        formular: ["Mark{L} formu dolduruyor.", "Lütfen formu doldurun."],
        anmelden: ["Mark{L} ikametini kaydettiriyor.", "Lütfen ikametinizi kaydettirin."],
        zeigen_pass: ["Mark{L} pasaportunu gösteriyor.", "Lütfen pasaportunuzu gösterin."],
        abholen: ["Mark{L} ikamet belgesini teslim alıyor.", "Lütfen ikamet belgenizi teslim alın."],
        bezahlen: ["Mark{L} harcı ödüyor.", "Lütfen harcı ödeyin."],
        konto: ["Mark{L} hesap açıyor.", null],
        geld: ["Mark{L} para çekiyor.", null],
        foto: ["Mark{L} bir fotoğraf teslim ediyor.", "Lütfen bir fotoğraf teslim edin."],
        termin: ["Mark{L} randevu alıyor.", "Lütfen randevu alın."],
        zeigen_karte: ["Mark{L} sağlık sigorta kartını gösteriyor.", "Lütfen sağlık sigorta kartınızı gösterin."],
        warten: ["Mark{L} bekliyor.", "Lütfen bekleme odasında bekleyin."],
        unterschreiben: ["Mark iş sözleşmesini imzalıyor.", "Lütfen buraya imza atın."],
        mitbringen: ["Mark iş sözleşmesini yanında getiriyor.", "Lütfen iş sözleşmenizi yanınızda getirin."]},
      champs: {
        familienname: ["Mark'ın soyadı {v}.", "Soyadı", null], vorname: ["Mark'ın adı {v}.", "Adı", null],
        geburtsdatum: ["Mark'ın doğum tarihi {v}.", "Doğum tarihi", null], geburtsort: ["Mark'ın doğum yeri {v}.", "Doğum yeri", null],
        staat: ["Mark'ın uyruğu {v}.", "Uyruğu", "Kanadalı", {französisch: "Fransız", amerikanisch: "Amerikalı"}],
        familienstand: ["Mark'ın medeni durumu {v}.", "Medeni durumu", "bekâr", {verheiratet: "evli", geschieden: "boşanmış"}],
        adresse: ["Mark'ın adresi {v}.", "Adres", null], plz: ["Mark'ın posta kodu {v}.", "Posta kodu", null],
        ort: ["Mark'ın şehri {v}.", "Şehir", null], telefon: ["Mark'ın telefon numarası {v}.", "Telefon numarası", null],
        beruf: ["Mark'ın mesleği {v}.", "Meslek", "stajyer", {Lehrer: "öğretmen", Arzt: "doktor"}],
        datum: ["Tarih {v}.", "Tarih", null], unterschrift: ["İmza {v}.", "İmza", null]},
      avis: {anmeldung: "İkamet kaydı için", konto: "Hesap açmak için", karte: "Sağlık sigorta kartı için", arzt: "İlk randevu için", aufenthalt: "Oturma izni için"}
    },
    uk: {
      lieux: {buergeramt: ["центр обслуговування громадян", "у центрі обслуговування громадян", "m"], bank: ["банк", "у банку", "m"],
              krankenkasse: ["лікарняна каса", "у лікарняній касі", "f"], praxis: ["кабінет лікаря", "у кабінеті лікаря", "m"]},
      docs: {pass: ["паспорт", "m"], formular: ["бланк", "m"], meldebescheinigung: ["довідка про реєстрацію", "f"], versichertenkarte: ["картка медичного страхування", "f"],
             arbeitsvertrag: ["трудовий договір", "m"], mietvertrag: ["договір оренди", "m"], foto: ["фотографія", "f"], karte: ["банківська картка", "f"],
             bestaetigung: ["підтвердження від орендодавця", "n"]},
      demarches: {
        nummer: ["Марк бере талон{L}.", "Візьміть, будь ласка, талон."],
        formular: ["Марк заповнює бланк{L}.", "Заповніть, будь ласка, бланк."],
        anmelden: ["Марк реєструється за місцем проживання{L}.", "Зареєструйтеся, будь ласка, за місцем проживання."],
        zeigen_pass: ["Марк показує свій паспорт{L}.", "Покажіть, будь ласка, ваш паспорт."],
        abholen: ["Марк забирає свою довідку про реєстрацію{L}.", "Заберіть, будь ласка, вашу довідку про реєстрацію."],
        bezahlen: ["Марк сплачує збір{L}.", "Сплатіть, будь ласка, збір."],
        konto: ["Марк відкриває рахунок{L}.", null],
        geld: ["Марк знімає гроші{L}.", null],
        foto: ["Марк здає фотографію{L}.", "Здайте, будь ласка, фотографію."],
        termin: ["Марк записується на прийом{L}.", "Запишіться, будь ласка, на прийом."],
        zeigen_karte: ["Марк показує свою картку медичного страхування{L}.", "Покажіть, будь ласка, вашу картку медичного страхування."],
        warten: ["Марк чекає{L}.", "Зачекайте, будь ласка, у приймальні."],
        unterschreiben: ["Марк підписує трудовий договір.", "Підпишіть, будь ласка, тут."],
        mitbringen: ["Марк приносить свій трудовий договір.", "Принесіть, будь ласка, ваш трудовий договір."]},
      champs: {
        familienname: ["Прізвище Марка — {v}.", "Прізвище", "Гарньє"], vorname: ["Імʼя Марка — {v}.", "Імʼя", "Марк"],
        geburtsdatum: ["Дата народження Марка — {v}.", "Дата народження", null], geburtsort: ["Місце народження Марка — {v}.", "Місце народження", "Монреаль"],
        staat: ["Громадянство Марка — {v}.", "Громадянство", "канадське", {französisch: "французьке", amerikanisch: "американське"}],
        familienstand: ["Сімейний стан Марка — {v}.", "Сімейний стан", "неодружений", {verheiratet: "одружений", geschieden: "розлучений"}],
        adresse: ["Адреса Марка — {v}.", "Адреса", "Гартенштрассе, 12"], plz: ["Поштовий індекс Марка — {v}.", "Поштовий індекс", null],
        ort: ["Місто Марка — {v}.", "Місто", "Берлін"], telefon: ["Номер телефону Марка — {v}.", "Номер телефону", null],
        beruf: ["Професія Марка — {v}.", "Професія", "стажист", {Lehrer: "учитель", Arzt: "лікар"}],
        datum: ["Дата — {v}.", "Дата", null], unterschrift: ["Підпис — {v}.", "Підпис", null]},
      avis: {anmeldung: "Для реєстрації за місцем проживання", konto: "Для відкриття рахунку", karte: "Для картки медичного страхування",
             arzt: "Для першого прийому", aufenthalt: "Для посвідки на проживання"}
    },
    pl: {
      lieux: {buergeramt: ["biuro obsługi mieszkańców", "w biurze obsługi mieszkańców", "n"], bank: ["bank", "w banku", "m"],
              krankenkasse: ["kasa chorych", "w kasie chorych", "f"], praxis: ["gabinet lekarski", "w gabinecie lekarskim", "m"]},
      docs: {pass: ["paszport", "m"], formular: ["formularz", "m"], meldebescheinigung: ["zaświadczenie o zameldowaniu", "n"], versichertenkarte: ["karta ubezpieczenia zdrowotnego", "f"],
             arbeitsvertrag: ["umowa o pracę", "f"], mietvertrag: ["umowa najmu", "f"], foto: ["zdjęcie", "n"], karte: ["karta bankowa", "f"],
             bestaetigung: ["zaświadczenie od wynajmującego", "n"]},
      demarches: {
        nummer: ["Mark pobiera numerek{L}.", "Proszę pobrać numerek."],
        formular: ["Mark wypełnia formularz{L}.", "Proszę wypełnić formularz."],
        anmelden: ["Mark melduje się{L}.", "Proszę się zameldować."],
        zeigen_pass: ["Mark pokazuje swój paszport{L}.", "Proszę pokazać paszport."],
        abholen: ["Mark odbiera swoje zaświadczenie o zameldowaniu{L}.", "Proszę odebrać zaświadczenie o zameldowaniu."],
        bezahlen: ["Mark uiszcza opłatę{L}.", "Proszę uiścić opłatę."],
        konto: ["Mark zakłada konto{L}.", null],
        geld: ["Mark wypłaca pieniądze{L}.", null],
        foto: ["Mark oddaje zdjęcie{L}.", "Proszę oddać zdjęcie."],
        termin: ["Mark umawia się na wizytę{L}.", "Proszę umówić się na wizytę."],
        zeigen_karte: ["Mark pokazuje swoją kartę ubezpieczenia zdrowotnego{L}.", "Proszę pokazać kartę ubezpieczenia zdrowotnego."],
        warten: ["Mark czeka{L}.", "Proszę zaczekać w poczekalni."],
        unterschreiben: ["Mark podpisuje umowę o pracę.", "Proszę podpisać tutaj."],
        mitbringen: ["Mark przynosi swoją umowę o pracę.", "Proszę przynieść umowę o pracę."]},
      champs: {
        familienname: ["Nazwisko Marka: {v}.", "Nazwisko", null], vorname: ["Imię Marka: {v}.", "Imię", null],
        geburtsdatum: ["Data urodzenia Marka: {v}.", "Data urodzenia", null], geburtsort: ["Miejsce urodzenia Marka: {v}.", "Miejsce urodzenia", "Montreal"],
        staat: ["Obywatelstwo Marka: {v}.", "Obywatelstwo", "kanadyjskie", {französisch: "francuskie", amerikanisch: "amerykańskie"}],
        familienstand: ["Stan cywilny Marka: {v}.", "Stan cywilny", "kawaler", {verheiratet: "żonaty", geschieden: "rozwiedziony"}],
        adresse: ["Adres Marka: {v}.", "Adres", null], plz: ["Kod pocztowy Marka: {v}.", "Kod pocztowy", null],
        ort: ["Miejscowość Marka: {v}.", "Miejscowość", null], telefon: ["Numer telefonu Marka: {v}.", "Numer telefonu", null],
        beruf: ["Zawód Marka: {v}.", "Zawód", "praktykant", {Lehrer: "nauczyciel", Arzt: "lekarz"}],
        datum: ["Data: {v}.", "Data", null], unterschrift: ["Podpis: {v}.", "Podpis", null]},
      avis: {anmeldung: "Do zameldowania", konto: "Do założenia konta", karte: "Do wyrobienia karty ubezpieczenia zdrowotnego",
             arzt: "Na pierwszą wizytę", aufenthalt: "Do zezwolenia na pobyt"}
    },
    ru: {
      lieux: {buergeramt: ["бюро обслуживания граждан", "в бюро обслуживания граждан", "n"], bank: ["банк", "в банке", "m"],
              krankenkasse: ["больничная касса", "в больничной кассе", "f"], praxis: ["врачебный кабинет", "во врачебном кабинете", "m"]},
      docs: {pass: ["паспорт", "m"], formular: ["бланк", "m"], meldebescheinigung: ["справка о регистрации", "f"], versichertenkarte: ["карта медицинского страхования", "f"],
             arbeitsvertrag: ["трудовой договор", "m"], mietvertrag: ["договор аренды", "m"], foto: ["фотография", "f"], karte: ["банковская карта", "f"],
             bestaetigung: ["подтверждение от арендодателя", "n"]},
      demarches: {
        nummer: ["Марк берёт талон{L}.", "Возьмите, пожалуйста, талон."],
        formular: ["Марк заполняет бланк{L}.", "Заполните, пожалуйста, бланк."],
        anmelden: ["Марк регистрируется по месту жительства{L}.", "Зарегистрируйтесь, пожалуйста, по месту жительства."],
        zeigen_pass: ["Марк показывает свой паспорт{L}.", "Покажите, пожалуйста, ваш паспорт."],
        abholen: ["Марк забирает свою справку о регистрации{L}.", "Заберите, пожалуйста, вашу справку о регистрации."],
        bezahlen: ["Марк оплачивает пошлину{L}.", "Оплатите, пожалуйста, пошлину."],
        konto: ["Марк открывает счёт{L}.", null],
        geld: ["Марк снимает деньги{L}.", null],
        foto: ["Марк сдаёт фотографию{L}.", "Сдайте, пожалуйста, фотографию."],
        termin: ["Марк записывается на приём{L}.", "Запишитесь, пожалуйста, на приём."],
        zeigen_karte: ["Марк показывает свою карту медицинского страхования{L}.", "Покажите, пожалуйста, вашу карту медицинского страхования."],
        warten: ["Марк ждёт{L}.", "Подождите, пожалуйста, в приёмной."],
        unterschreiben: ["Марк подписывает трудовой договор.", "Подпишите, пожалуйста, здесь."],
        mitbringen: ["Марк приносит свой трудовой договор.", "Принесите, пожалуйста, ваш трудовой договор."]},
      champs: {
        familienname: ["Фамилия Марка — {v}.", "Фамилия", "Гарнье"], vorname: ["Имя Марка — {v}.", "Имя", "Марк"],
        geburtsdatum: ["Дата рождения Марка — {v}.", "Дата рождения", null], geburtsort: ["Место рождения Марка — {v}.", "Место рождения", "Монреаль"],
        staat: ["Гражданство Марка — {v}.", "Гражданство", "канадское", {französisch: "французское", amerikanisch: "американское"}],
        familienstand: ["Семейное положение Марка — {v}.", "Семейное положение", "холост", {verheiratet: "женат", geschieden: "разведён"}],
        adresse: ["Адрес Марка — {v}.", "Адрес", "Гартенштрассе, 12"], plz: ["Почтовый индекс Марка — {v}.", "Почтовый индекс", null],
        ort: ["Город Марка — {v}.", "Город", "Берлин"], telefon: ["Номер телефона Марка — {v}.", "Номер телефона", null],
        beruf: ["Профессия Марка — {v}.", "Профессия", "стажёр", {Lehrer: "учитель", Arzt: "врач"}],
        datum: ["Дата — {v}.", "Дата", null], unterschrift: ["Подпись — {v}.", "Подпись", null]},
      avis: {anmeldung: "Для регистрации по месту жительства", konto: "Для открытия счёта", karte: "Для карты медицинского страхования",
             arzt: "Для первого приёма", aufenthalt: "Для вида на жительство"}
    },
    fa: {
      lieux: {buergeramt: ["ادارهٔ امور شهروندی", "در ادارهٔ امور شهروندی"], bank: ["بانک", "در بانک"],
              krankenkasse: ["صندوق بیمهٔ درمان", "در صندوق بیمهٔ درمان"], praxis: ["مطب", "در مطب"]},
      docs: {pass: ["گذرنامه"], formular: ["فرم"], meldebescheinigung: ["گواهی ثبت محل سکونت"], versichertenkarte: ["کارت بیمهٔ درمانی"],
             arbeitsvertrag: ["قرارداد کار"], mietvertrag: ["قرارداد اجاره"], foto: ["یک عکس"], karte: ["کارت بانکی"], bestaetigung: ["تأییدیهٔ صاحب‌خانه"]},
      demarches: {
        nummer: ["مارک{L} شمارهٔ نوبت می‌گیرد.", "لطفاً یک شمارهٔ نوبت بگیرید."],
        formular: ["مارک{L} فرم را پر می‌کند.", "لطفاً فرم را پر کنید."],
        anmelden: ["مارک{L} محل سکونتش را ثبت می‌کند.", "لطفاً محل سکونتتان را ثبت کنید."],
        zeigen_pass: ["مارک{L} گذرنامه‌اش را نشان می‌دهد.", "لطفاً گذرنامه‌تان را نشان دهید."],
        abholen: ["مارک{L} گواهی ثبت محل سکونتش را تحویل می‌گیرد.", "لطفاً گواهی ثبت محل سکونتتان را تحویل بگیرید."],
        bezahlen: ["مارک{L} هزینه را می‌پردازد.", "لطفاً هزینه را بپردازید."],
        konto: ["مارک{L} حساب باز می‌کند.", null],
        geld: ["مارک{L} پول برداشت می‌کند.", null],
        foto: ["مارک{L} یک عکس تحویل می‌دهد.", "لطفاً یک عکس تحویل دهید."],
        termin: ["مارک{L} وقت می‌گیرد.", "لطفاً وقت بگیرید."],
        zeigen_karte: ["مارک{L} کارت بیمهٔ درمانی‌اش را نشان می‌دهد.", "لطفاً کارت بیمهٔ درمانی‌تان را نشان دهید."],
        warten: ["مارک{L} منتظر می‌ماند.", "لطفاً در اتاق انتظار منتظر بمانید."],
        unterschreiben: ["مارک قرارداد کار را امضا می‌کند.", "لطفاً اینجا را امضا کنید."],
        mitbringen: ["مارک قرارداد کارش را با خود می‌آورد.", "لطفاً قرارداد کارتان را با خود بیاورید."]},
      champs: {
        familienname: ["نام خانوادگی مارک {v} است.", "نام خانوادگی", "گارنیه"], vorname: ["نام مارک {v} است.", "نام", "مارک"],
        geburtsdatum: ["تاریخ تولد مارک {v} است.", "تاریخ تولد", null], geburtsort: ["محل تولد مارک {v} است.", "محل تولد", "مونترال"],
        staat: ["ملیت مارک {v} است.", "ملیت", "کانادایی", {französisch: "فرانسوی", amerikanisch: "آمریکایی"}],
        familienstand: ["وضعیت تأهل مارک: {v}.", "وضعیت تأهل", "مجرد", {verheiratet: "متأهل", geschieden: "طلاق‌گرفته"}],
        adresse: ["نشانی مارک {v} است.", "نشانی", "گارتن‌اشتراسه، پلاک 12"], plz: ["کد پستی مارک {v} است.", "کد پستی", null],
        ort: ["شهر مارک {v} است.", "شهر", "برلین"], telefon: ["شمارهٔ تلفن مارک {v} است.", "شمارهٔ تلفن", null],
        beruf: ["شغل مارک {v} است.", "شغل", "کارآموز", {Lehrer: "معلم", Arzt: "پزشک"}],
        datum: ["تاریخ: {v}.", "تاریخ", null], unterschrift: ["امضا: {v}.", "امضا", null]},
      avis: {anmeldung: "برای ثبت محل سکونت", konto: "برای باز کردن حساب", karte: "برای کارت بیمهٔ درمانی", arzt: "برای اولین وقت پزشک",
             aufenthalt: "برای اجازهٔ اقامت"}
    },
    ar: {
      lieux: {buergeramt: ["مكتب خدمات المواطنين", "في مكتب خدمات المواطنين", "m"], bank: ["البنك", "في البنك", "m"],
              krankenkasse: ["صندوق التأمين الصحي", "في صندوق التأمين الصحي", "m"], praxis: ["العيادة", "في العيادة", "f"]},
      docs: {pass: ["جواز السفر", "m"], formular: ["الاستمارة", "f"], meldebescheinigung: ["شهادة تسجيل السكن", "f"], versichertenkarte: ["بطاقة التأمين الصحي", "f"],
             arbeitsvertrag: ["عقد العمل", "m"], mietvertrag: ["عقد الإيجار", "m"], foto: ["صورة شخصية", "f"], karte: ["البطاقة المصرفية", "f"],
             bestaetigung: ["إفادة المؤجِّر", "f"]},
      demarches: {
        nummer: ["يأخذ مارك رقم انتظار{L}.", "يُرجى أخذ رقم انتظار."],
        formular: ["يملأ مارك الاستمارة{L}.", "يُرجى ملء الاستمارة."],
        anmelden: ["يسجّل مارك عنوان سكنه{L}.", "يُرجى تسجيل عنوان سكنك."],
        zeigen_pass: ["يُظهر مارك جواز سفره{L}.", "يُرجى إظهار جواز سفرك."],
        abholen: ["يستلم مارك شهادة تسجيل سكنه{L}.", "يُرجى استلام شهادة تسجيل سكنك."],
        bezahlen: ["يدفع مارك الرسوم{L}.", "يُرجى دفع الرسوم."],
        konto: ["يفتح مارك حسابًا{L}.", null],
        geld: ["يسحب مارك نقودًا{L}.", null],
        foto: ["يسلّم مارك صورة شخصية{L}.", "يُرجى تسليم صورة شخصية."],
        termin: ["يحجز مارك موعدًا{L}.", "يُرجى حجز موعد."],
        zeigen_karte: ["يُظهر مارك بطاقة تأمينه الصحي{L}.", "يُرجى إظهار بطاقة تأمينك الصحي."],
        warten: ["ينتظر مارك{L}.", "يُرجى الانتظار في غرفة الانتظار."],
        unterschreiben: ["يوقّع مارك عقد العمل.", "يُرجى التوقيع هنا."],
        mitbringen: ["يُحضر مارك عقد عمله معه.", "يُرجى إحضار عقد عملك معك."]},
      champs: {
        familienname: ["اسم عائلة مارك {v}.", "اسم العائلة", "غارنييه"], vorname: ["الاسم الأول لمارك هو {v}.", "الاسم الأول", "مارك"],
        geburtsdatum: ["تاريخ ميلاد مارك {v}.", "تاريخ الميلاد", null], geburtsort: ["مكان ميلاد مارك {v}.", "مكان الميلاد", "مونتريال"],
        staat: ["جنسية مارك {v}.", "الجنسية", "كندية", {französisch: "فرنسية", amerikanisch: "أمريكية"}],
        familienstand: ["الحالة الاجتماعية لمارك: {v}.", "الحالة الاجتماعية", "أعزب", {verheiratet: "متزوج", geschieden: "مطلّق"}],
        adresse: ["عنوان مارك {v}.", "العنوان", "غارتن شتراسه 12"], plz: ["الرمز البريدي لمارك {v}.", "الرمز البريدي", null],
        ort: ["مدينة مارك {v}.", "المدينة", "برلين"], telefon: ["رقم هاتف مارك {v}.", "رقم الهاتف", null],
        beruf: ["مهنة مارك {v}.", "المهنة", "متدرّب", {Lehrer: "معلّم", Arzt: "طبيب"}],
        datum: ["التاريخ: {v}.", "التاريخ", null], unterschrift: ["التوقيع: {v}.", "التوقيع", null]},
      avis: {anmeldung: "لتسجيل السكن", konto: "لفتح حساب", karte: "للحصول على بطاقة التأمين الصحي", arzt: "للموعد الأول عند الطبيب",
             aufenthalt: "للحصول على تصريح الإقامة"}
    }
  };

  // ---------- pour qui apprend l'espagnol : l'arabe ----------
  const ES = {
    ar: {
      lieux: {oficina: ["مكتب البلدية", "في مكتب البلدية", "m"], banco: ["البنك", "في البنك", "m"], consulta: ["العيادة", "في العيادة", "f"]},
      docs: {pasaporte: ["جواز السفر", "m"], formulario: ["الاستمارة", "f"], certificado: ["شهادة تسجيل السكن", "f"], tarjeta_sanitaria: ["البطاقة الصحية", "f"],
             contrato: ["عقد العمل", "m"], contrato_alquiler: ["عقد الإيجار", "m"], foto: ["صورة شخصية", "f"], tarjeta: ["البطاقة المصرفية", "f"]},
      demarches: {
        nummer: ["يأخذ مارك رقم انتظار{L}.", "يُرجى أخذ رقم انتظار."],
        formular: ["يملأ مارك الاستمارة{L}.", "يُرجى ملء الاستمارة."],
        certificado: ["يطلب مارك شهادة تسجيل السكن{L}.", null],
        zeigen_pass: ["يُظهر مارك جواز سفره{L}.", "يُرجى إظهار جواز سفرك."],
        abholen: ["يستلم مارك شهادته{L}.", "يُرجى استلام شهادتك."],
        konto: ["يفتح مارك حسابًا{L}.", null],
        geld: ["يسحب مارك نقودًا{L}.", null],
        termin: ["يحجز مارك موعدًا{L}.", "يُرجى حجز موعد."],
        zeigen_karte: ["يُظهر مارك بطاقته الصحية{L}.", "يُرجى إظهار بطاقتك الصحية."],
        warten: ["ينتظر مارك{L}.", "يُرجى الانتظار هنا."],
        unterschreiben: ["يوقّع مارك عقد العمل.", "يُرجى التوقيع هنا."],
        mitbringen: ["يُحضر مارك عقد عمله معه.", "يُرجى إحضار عقد عملك معك."]},
      champs: {
        nombre: ["الاسم الأول لمارك هو {v}.", "الاسم الأول", "مارك"], apellidos: ["اسم عائلة مارك {v}.", "اسم العائلة", "غارنييه"],
        nacimiento: ["تاريخ ميلاد مارك {v}.", "تاريخ الميلاد", null],
        lugar: ["مكان ميلاد مارك {v}.", "مكان الميلاد", "مدينة مكسيكو", {Madrid: "مدريد", Guadalajara: "غوادالاخارا"}],
        nacionalidad: ["جنسية مارك {v}.", "الجنسية", "مكسيكية", {"española": "إسبانية", colombiana: "كولومبية"}],
        estado: ["الحالة الاجتماعية لمارك: {v}.", "الحالة الاجتماعية", "أعزب", {casado: "متزوج", divorciado: "مطلّق"}],
        direccion: ["عنوان مارك {v}.", "العنوان", "شارع لا لونا 12، الطابق 2، الشقة B"], cp: ["الرمز البريدي لمارك {v}.", "الرمز البريدي", null],
        municipio: ["البلدية: {v}.", "البلدية", "مدريد"], telefono: ["رقم هاتف مارك {v}.", "رقم الهاتف", null],
        fecha: ["التاريخ: {v}.", "التاريخ", null], firma: ["التوقيع: {v}.", "التوقيع", null]},
      avis: {padron: "لتسجيل السكن", cuenta: "لفتح حساب", sanitaria: "للحصول على البطاقة الصحية", medico: "للموعد الأول عند الطبيب",
             residencia: "للحصول على تصريح الإقامة"}
    }
  };

  // ---------- le branchement dans la donnée ----------
  const manque = [];
  const poser = (langue, table) => {
    for (const lg in table){
      const T = table[lg];
      D.jours[lg] = JOURS[lg];
      for (const k in D.lieux[langue]){ const x = T.lieux[k]; if (x) D.lieux[langue][k].trad[lg] = x; else manque.push(langue + " lieu " + k + " " + lg); }
      for (const k in D.docs[langue]){ const x = T.docs[k]; if (x){ D.docs[langue][k].trad[lg] = x[0]; (D.docs[langue][k].genreTrad = D.docs[langue][k].genreTrad || {})[lg] = x[1] || null; } else manque.push(langue + " doc " + k + " " + lg); }
      for (const d of D.demarches[langue]){
        const x = T.demarches[d.id]; if (!x){ manque.push(langue + " demarche " + d.id + " " + lg); continue; }
        d.t[lg] = x[0];
        if (d.ts) { if (x[1]) d.ts[lg] = x[1]; else manque.push(langue + " phrase polie " + d.id + " " + lg); }
      }
      for (const c in D.champs[langue]){
        const x = T.champs[c]; if (!x){ manque.push(langue + " champ " + c + " " + lg); continue; }
        D.champs[langue][c].t[lg] = [x[0], x[1], x[2]];
        if (x[3]) (D.champs[langue][c].tfl = D.champs[langue][c].tfl || {})[lg] = x[3];
      }
      for (const a of D.avis[langue]){ const x = T.avis[a.id]; if (x) a.t[lg] = x; else manque.push(langue + " avis " + a.id + " " + lg); }
    }
  };
  poser("de", DE);
  poser("es", ES);
  if (manque.length) console.error("demarches/langues.js : morceaux absents", manque);
  return B;
}
