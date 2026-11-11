# À relire par un natif : les étoiles de la séance légère

La fête de la nouvelle étoile (essai admin « seance_legere », 7 nov. 2026) affiche trois textes qui n'ont été relus par personne dont c'est la langue. Ils sont tous dans `etoiles/outils/figures.py` ; après correction, lancer `python etoiles/outils/construire.py`, qui refait `etoiles/ciel.json`.

## 1. La distance (`TEXTES_DISTANCE`)

« à 34 années-lumière », « à environ 1 400 années-lumière ». Le pluriel est choisi par le navigateur (`Intl.PluralRules`, clés one / few / many / other), et les chiffres sont formatés par lui aussi. Toutes nos distances dépassent 20 années-lumière.

| Langue | Exemple (34) | Arrondie (environ 1 400) | Ce qu'il faut regarder |
|---|---|---|---|
| en | 34 light-years away | about 1,400 light-years away | |
| de | 34 Lichtjahre entfernt | etwa 1.400 Lichtjahre entfernt | |
| pt | a 34 anos-luz | a cerca de 1.400 anos-luz | portugais du Brésil, langue d'interface |
| tr | 34 ışık yılı uzakta | yaklaşık 1.400 ışık yılı uzakta | |
| pl | 34 lata świetlne stąd | około 1400 lat świetlnych stąd | « stąd » ou « od Ziemi » ? |
| ru | 34 световых года от Земли | около 1 400 световых лет от Земли | |
| uk | 34 світлові роки від Землі | близько 1 400 світлових років від Землі | |
| ar | على بعد 34 سنةً ضوئية | على بعد نحو 1,400 سنة ضوئية | l'accord du nombre (3-10 au pluriel, 11-99 au singulier accusatif) |
| fa | در فاصلهٔ ۳۴ سال نوری | در فاصلهٔ حدود ۱٬۴۰۰ سال نوری | |

## 2. Les noms des constellations (`FIGURES`, champ `noms`)

Les trois figures de l'A1 (la Grande Ourse, les Gémeaux, Orion) ont leur nom dans les 11 langues ; les 12 autres en français, allemand, espagnol et anglais seulement. À regarder en particulier :
- la Grande Ourse : en anglais « the Big Dipper » (la figure dessinée est le chariot, pas toute la constellation), en allemand « der Große Wagen », en russe « Большой Ковш », en ukrainien « Великий Віз », en polonais « Wielki Wóz » ;
- Orion : en turc « Avcı », en arabe « الجبار », en persan « شکارچی » ;
- les Gémeaux : en arabe « التوأمان », en persan « دوپیکر ».

## 3. Les étoiles sans nom propre (`SANS_NOM`, `LETTRES`, `GENITIFS`, `USAGE_SANS_NOM`)

Règle validée par Jacques le 7 nov. : la lettre grecque en toutes lettres et la constellation, selon l'usage de chaque langue.
- **français** : « Tau des Gémeaux », « Zêta de la Lyre », « Êta du Cygne », « Thêta de la Couronne boréale » ;
- **anglais, allemand, portugais, polonais, turc** : le génitif latin, « Tau Geminorum », « Zeta Lyrae » ;
- **espagnol** : le génitif latin, avec « Épsilon » accentué ;
- **russe** : « Тау Близнецов », « Дзета Лиры » ; **ukrainien** : « Тау Близнят », « Дзета Ліри » ;
- **arabe et persan** : la forme latine pour l'instant. Un natif dira s'il faut la lettre et le nom dans la langue.

Les 19 étoiles concernées : tau, iota et kappa des Gémeaux ; epsilon, zêta et delta de la Lyre ; êta du Cygne ; bêta, delta et gamma de la Flèche ; thêta, gamma, delta et epsilon de la Couronne boréale ; iota et zêta de Céphée ; gamma et delta du Dauphin ; delta de la Croix du Sud.

## 4. « Ton ciel » : la page de la constellation (9 nov. 2026)

Cinq textes de l'interface, traduits par Claude et relus par personne dont c'est la langue (`ciel_tuile`, `ciel_total`, `ciel_complete`, `ciel_a_venir`, `ciel_premiere`). **À regarder d'abord : le mot arabe pour « Ton ciel » (« سماؤك »)**, demandé par Jacques.

| Langue | Ton ciel | Étoiles allumées : N | Constellation complète | À venir | Ta première étoile |
|---|---|---|---|---|---|
| en | Your sky | Stars lit: N | Constellation complete | Coming up | Your first star |
| de | Dein Himmel | Leuchtende Sterne: N | Sternbild vollständig | Kommt noch | Dein erster Stern |
| es | Tu cielo | Estrellas encendidas: N | Constelación completa | Por venir | Tu primera estrella |
| pt | Seu céu | Estrelas acesas: N | Constelação completa | Em breve | Sua primeira estrela |
| tr | Gökyüzün | Yanan yıldızlar: N | Takımyıldızı tamamlandı | Sırada | İlk yıldızın |
| pl | Twoje niebo | Zapalone gwiazdy: N | Konstelacja ukończona | Przed tobą | Twoja pierwsza gwiazda |
| ru | Твоё небо | Зажжённых звёзд: N | Созвездие завершено | Впереди | Твоя первая звезда |
| uk | Твоє небо | Запалених зірок: N | Сузір'я завершено | Попереду | Твоя перша зірка |
| ar | سماؤك | النجوم المضيئة: N | اكتملت الكوكبة | قادمة | نجمتك الأولى |
| fa | آسمان تو | ستاره‌های روشن: N | صورت فلکی کامل شد | در پیش است | نخستین ستاره‌ات |

## 5. Le ciel jusqu'au C1 : les noms des 57 constellations (11 nov. 2026)

42 constellations de plus (`etoiles/outils/voyage.py`) et les noms qui manquaient aux 15 premières (`NOMS_EXISTANTES`), dans les 12 langues : celles de l'interface et celles qu'on apprend (le japonais pour le nom de la figure dans la langue apprise). Écrits par Claude, comparés aux titres de Wikipedia (`python etoiles/outils/controle.py`), relus par personne dont c'est la langue.

**À regarder d'abord :**
- **turc** : les noms turcs usuels (Aslan, Başak, Kahraman pour Persée, Erboğa pour le Centaure, Irmak pour l'Éridan, Karina pour la Carène, Suyılanı pour l'Hydre) ; la Wikipedia turque n'emploie que les noms latins, elle n'a donc rien vérifié ;
- **les astérismes** : la Petite Ourse est dessinée comme « petit chariot », d'où « der Kleine Wagen », « Mały Wóz », « Малый Ковш », « Малий Віз », « the Little Dipper », sur le modèle de la Grande Ourse existante ;
- **arabe et persan** : repris des titres de Wikipedia, sauf la Croix du Sud (« الصليب الجنوبي », « صلیب جنوبی », plus parlants que « نعيم » et « چلیپا ») et le Grand Carré de Pégase (« مربع الخريف », « مربع پاییزی ») ;
- **japonais** : « 北斗七星 » pour la Grande Ourse (le chariot), « すばる » pour les Pléiades, « ペガススの大四辺形 » pour le Grand Carré.

Les étoiles sans nom propre des nouvelles figures suivent la règle du 7 nov. (lettre grecque et constellation) ; les lettres ajoutées sont dans `LETTRES_VOYAGE` (en espagnol « Alfa », « Ómicron », « Ípsilon », « Fi », « Ji » ; en français « Rhô », « Khi », « Oméga »), les génitifs dans `GENITIFS_VOYAGE`.

| # | fr | de | es | en | pt | ja | tr | pl | ru | uk | ar | fa |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | la Grande Ourse | der Große Wagen | el Carro | the Big Dipper | a Ursa Maior | 北斗七星 | Büyük Ayı | Wielki Wóz | Большой Ковш | Великий Віз | الدب الأكبر | دب اکبر |
| 2 | les Gémeaux | die Zwillinge | Géminis | Gemini | Gêmeos | ふたご座 | İkizler | Bliźnięta | Близнецы | Близнята | التوأمان | دوپیکر |
| 3 | Orion | Orion | Orión | Orion | Órion | オリオン座 | Avcı | Orion | Орион | Оріон | الجبار | شکارچی |
| 4 | la Lyre | die Leier | la Lira | Lyra | a Lira | こと座 | Çalgı | Lutnia | Лира | Ліра | القيثارة | شلیاق |
| 5 | le Cygne | der Schwan | el Cisne | Cygnus | o Cisne | はくちょう座 | Kuğu | Łabędź | Лебедь | Лебідь | الدجاجة | ماکیان |
| 6 | la Flèche | der Pfeil | la Flecha | Sagitta | a Flecha | や座 | Ok | Strzała | Стрела | Стріла | السهم | پیکان |
| 7 | les Pléiades | das Siebengestirn | las Siete Cabrillas | the Pleiades | as Plêiades | すばる | Ülker | Plejady | Плеяды | Плеяди | الثريا | پروین |
| 8 | la Couronne boréale | die Nördliche Krone | la Corona Boreal | Corona Borealis | a Coroa Boreal | かんむり座 | Kuzey Tacı | Korona Północna | Северная Корона | Північна Корона | الإكليل الشمالي | تاج شمالی |
| 9 | le Cocher | der Fuhrmann | el Cochero | Auriga | o Cocheiro | ぎょしゃ座 | Arabacı | Woźnica | Возничий | Візничий | ممسك الأعنة | ارابه‌ران |
| 10 | Cassiopée | das Himmels-W | Casiopea | Cassiopeia | Cassiopeia | カシオペヤ座 | Kraliçe | Kasjopeja | Кассиопея | Кассіопея | ذات الكرسي | ذات‌الکرسی |
| 11 | Céphée | Kepheus | Cefeo | Cepheus | Cefeu | ケフェウス座 | Kral | Cefeusz | Цефей | Цефей | قيفاوس | قیفاووس |
| 12 | le Corbeau | der Rabe | el Cuervo | Corvus | o Corvo | からす座 | Karga | Kruk | Ворон | Ворон | الغراب | کلاغ |
| 13 | le Dauphin | der Delfin | el Delfín | Delphinus | o Golfinho | いるか座 | Yunus | Delfin | Дельфин | Дельфін | الدلفين | دلفین |
| 14 | le Grand Carré de Pégase | das Herbstviereck | el Cuadrado de Pegaso | the Great Square of Pegasus | o Grande Quadrado de Pégaso | ペガススの大四辺形 | Pegasus'un Büyük Karesi | Wielki Kwadrat Pegaza | Большой квадрат Пегаса | Великий квадрат Пегаса | مربع الخريف | مربع پاییزی |
| 15 | la Croix du Sud | das Kreuz des Südens | la Cruz del Sur | the Southern Cross | o Cruzeiro do Sul | みなみじゅうじ座 | Güney Haçı | Krzyż Południa | Южный Крест | Південний Хрест | الصليب الجنوبي | صلیب جنوبی |
| 16 | la Petite Ourse | der Kleine Wagen | la Osa Menor | the Little Dipper | a Ursa Menor | こぐま座 | Küçük Ayı | Mały Wóz | Малый Ковш | Малий Віз | الدب الأصغر | دب اصغر |
| 17 | le Lion | der Löwe | Leo | Leo | Leão | しし座 | Aslan | Lew | Лев | Лев | الأسد | شیر |
| 18 | le Taureau | der Stier | Tauro | Taurus | Touro | おうし座 | Boğa | Byk | Телец | Телець | الثور | گاو |
| 19 | le Bouvier | der Bärenhüter | el Boyero | Boötes | o Boieiro | うしかい座 | Çoban | Wolarz | Волопас | Волопас | العواء | گاوران |
| 20 | Andromède | Andromeda | Andrómeda | Andromeda | Andrômeda | アンドロメダ座 | Andromeda | Andromeda | Андромеда | Андромеда | المرأة المسلسلة | آندرومدا |
| 21 | Persée | Perseus | Perseo | Perseus | Perseu | ペルセウス座 | Kahraman | Perseusz | Персей | Персей | حامل رأس الغول | برساوش |
| 22 | Hercule | Herkules | Hércules | Hercules | Hércules | ヘルクレス座 | Herkül | Herkules | Геркулес | Геркулес | الجاثي | زانوزده |
| 23 | le Dragon | der Drache | el Dragón | Draco | o Dragão | りゅう座 | Ejderha | Smok | Дракон | Дракон | التنين | اژدها |
| 24 | l'Aigle | der Adler | el Águila | Aquila | a Águia | わし座 | Kartal | Orzeł | Орёл | Орел | العقاب | عقاب |
| 25 | le Triangle | das Dreieck | el Triángulo | Triangulum | o Triângulo | さんかく座 | Üçgen | Trójkąt | Треугольник | Трикутник | المثلث | سه‌سو |
| 26 | la Vierge | die Jungfrau | Virgo | Virgo | Virgem | おとめ座 | Başak | Panna | Дева | Діва | العذراء | دوشیزه |
| 27 | le Scorpion | der Skorpion | Escorpio | Scorpius | Escorpião | さそり座 | Akrep | Skorpion | Скорпион | Скорпіон | العقرب | کژدم |
| 28 | le Sagittaire | der Schütze | Sagitario | Sagittarius | Sagitário | いて座 | Yay | Strzelec | Стрелец | Стрілець | الرامي | کمان |
| 29 | le Grand Chien | der Große Hund | el Can Mayor | Canis Major | o Cão Maior | おおいぬ座 | Büyük Köpek | Wielki Pies | Большой Пёс | Великий Пес | الكلب الأكبر | سگ بزرگ |
| 30 | le Bélier | der Widder | Aries | Aries | Áries | おひつじ座 | Koç | Baran | Овен | Овен | الحمل | بره |
| 31 | le Cancer | der Krebs | Cáncer | Cancer | Câncer | かに座 | Yengeç | Rak | Рак | Рак | السرطان | خرچنگ |
| 32 | la Balance | die Waage | Libra | Libra | Libra | てんびん座 | Terazi | Waga | Весы | Терези | الميزان | ترازو |
| 33 | le Capricorne | der Steinbock | Capricornio | Capricornus | Capricórnio | やぎ座 | Oğlak | Koziorożec | Козерог | Козоріг | الجدي | بزغاله |
| 34 | le Verseau | der Wassermann | Acuario | Aquarius | Aquário | みずがめ座 | Kova | Wodnik | Водолей | Водолій | الدلو | دلو |
| 35 | les Poissons | die Fische | Piscis | Pisces | Peixes | うお座 | Balıklar | Ryby | Рыбы | Риби | الحوت | ماهی |
| 36 | Ophiuchus | der Schlangenträger | Ofiuco | Ophiuchus | Ofiúco | へびつかい座 | Yılancı | Wężownik | Змееносец | Змієносець | الحواء | مارافسای |
| 37 | le Lièvre | der Hase | la Liebre | Lepus | a Lebre | うさぎ座 | Tavşan | Zając | Заяц | Заєць | الأرنب | خرگوش |
| 38 | la Baleine | der Walfisch | la Ballena | Cetus | a Baleia | くじら座 | Balina | Wieloryb | Кит | Кит | قيطس | نهنگ |
| 39 | l'Hydre | die Wasserschlange | la Hidra | Hydra | a Hidra | うみへび座 | Suyılanı | Hydra | Гидра | Гідра | الشجاع | مار باریک |
| 40 | la Coupe | der Becher | la Copa | Crater | a Taça | コップ座 | Kupa | Puchar | Чаша | Чаша | الباطية | پیاله |
| 41 | la Colombe | die Taube | la Paloma | Columba | a Pomba | はと座 | Güvercin | Gołąb | Голубь | Голуб | الحمامة | کبوتر |
| 42 | l'Éridan | der Eridanus | Erídano | Eridanus | Erídano | エリダヌス座 | Irmak | Erydan | Эридан | Ерідан | النهر | جوی |
| 43 | le Centaure | der Zentaur | el Centauro | Centaurus | o Centauro | ケンタウルス座 | Erboğa | Centaur | Центавр | Центавр | قنطورس | قنطورس |
| 44 | la Carène | der Kiel des Schiffs | la Quilla | Carina | a Quilha | りゅうこつ座 | Karina | Kil | Киль | Кіль | الجؤجؤ | شاه‌تخته |
| 45 | les Voiles | das Segel des Schiffs | la Vela | Vela | a Vela | ほ座 | Yelken | Żagiel | Паруса | Вітрила | الشراع | بادبان |
| 46 | la Poupe | das Achterdeck des Schiffs | la Popa | Puppis | a Popa | とも座 | Pupa | Rufa | Корма | Корма | الكوثل | کشتی‌دم |
| 47 | le Loup | der Wolf | el Lobo | Lupus | o Lobo | おおかみ座 | Kurt | Wilk | Волк | Вовк | السبع | گرگ |
| 48 | l'Autel | der Altar | el Altar | Ara | o Altar | さいだん座 | Sunak | Ołtarz | Жертвенник | Жертовник | المجمرة | آتشدان |
| 49 | la Couronne australe | die Südliche Krone | la Corona Austral | Corona Australis | a Coroa Austral | みなみのかんむり座 | Güney Tacı | Korona Południowa | Южная Корона | Південна Корона | الإكليل الجنوبي | تاج جنوبی |
| 50 | le Triangle austral | das Südliche Dreieck | el Triángulo Austral | Triangulum Australe | o Triângulo Austral | みなみのさんかく座 | Güney Üçgeni | Trójkąt Południowy | Южный Треугольник | Південний Трикутник | المثلث الجنوبي | مثلث جنوبی |
| 51 | le Paon | der Pfau | el Pavo | Pavo | o Pavão | くじゃく座 | Tavuskuşu | Paw | Павлин | Павич | الطاووس | طاووس |
| 52 | la Grue | der Kranich | la Grulla | Grus | o Grou | つる座 | Turna | Żuraw | Журавль | Журавель | الكركي | درنا |
| 53 | le Phénix | der Phönix | el Fénix | Phoenix | a Fênix | ほうおう座 | Anka | Feniks | Феникс | Фенікс | العنقاء | سیمرغ |
| 54 | le Poisson austral | der Südliche Fisch | el Pez Austral | Piscis Austrinus | o Peixe Austral | みなみのうお座 | Güney Balığı | Ryba Południowa | Южная Рыба | Південна Риба | الحوت الجنوبي | ماهی جنوبی |
| 55 | le Toucan | der Tukan | el Tucán | Tucana | o Tucano | きょしちょう座 | Tukan | Tukan | Тукан | Тукан | الطوقان | توکان |
| 56 | la Mouche | die Fliege | la Mosca | Musca | a Mosca | はえ座 | Sinek | Mucha | Муха | Муха | الذبابة | مگس جنوبی |
| 57 | l'Hydre mâle | die Kleine Wasserschlange | la Hidra Macho | Hydrus | a Hidra Macho | みずへび座 | Küçük Suyılanı | Wąż Wodny | Южная Гидра | Південна Гідра | حية الماء | آبمار |
