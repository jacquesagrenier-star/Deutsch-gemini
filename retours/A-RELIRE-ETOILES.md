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
