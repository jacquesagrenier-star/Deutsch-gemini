# Les thèmes illustrés en russe : ce qu'un locuteur natif devrait relire

14 nov. 2026, lot 1 de l'alignement des thèmes (« Où est le chat ? » et « La journée »). Pour qui apprend l'allemand
avec l'interface en russe, la page montre désormais la phrase entière traduite, comme en français, en anglais et en
portugais. Il n'y a pas eu de relecture native. Une rétro-traduction à l'aveugle (vers le français, sans l'allemand)
n'a trouvé aucune faute.

- Les traductions ne sont pas écrites phrase par phrase : on traduit les morceaux que la page assemble.
  - « Où est le chat ? » : `visuel/gato/langues.py`, tables `RU` et `RU_PL` (les six cas de 16 noms), `lieu()` (la
    préposition selon « où » ou « vers où »), `POSTURE`, `MOUVEMENT`, `PHRASES`. On corrige là, puis
    `python visuel/gato/gato.py --json`.
  - « La journée » : `visuel/journee/langues.py`, `VERBES` (19 verbes aux cinq personnes), `SUJETS`, `FREQUENCES`.
    On corrige là, puis `python visuel/journee/journee.py --json`. L'heure (« в 7:15 ») et les mots de liaison
    (« Сначала… Потом… ») sont dans `visuel/prototype/journee.html` (`heureTrad`, `LIENS_TR`).
- Contrôle à l'écran : `python visuel/langues_themes.py verifier gato journee ru` (navigateur, verrou des parcours).

## Ce que le russe fait, et qui est voulu

Le russe distingue « où » et « vers où » comme l'allemand : на столе / на стол (auf dem / auf den Tisch), под
столом / под стол, в корзине / в корзину, за диваном / за диван. Le groupe allemand du mauvais choix est traduit
avec son cas : l'élève voit la différence qu'il a manquée. Après перед, рядом с, между, la forme est la même pour les
deux : seul le verbe change (сидит / садится).

## Points à confirmer

1. **« ans Fenster » → « садится у окна »**. « к окну » marquerait la direction, mais « садится к окну » sonne mal.
   Dans les groupes isolés, « am Fenster » = « у окна » et « ans Fenster » = « к окну ».
2. **« im Regal » → « на полке стеллажа »** (« лежит / прыгает на полку стеллажа ») : « в стеллаже » est rare.
   C'est le seul groupe à deux noms.
3. **« über » + accusatif → « через »** (« прыгает через коробку ») ; « über » + datif → « над ».
4. **« läuft hinter das Sofa » → « заходит за диван »**, « kriecht unter » → « залезает под », « klettert auf »
   → « забирается на ».
5. **Les noms** : Мориц, Мия (Мии, Мию, Мией), Катрин, Ян — comme dans les textes de la page.
6. **« kocht » → « готовит »**, sans complément.
7. **« Ben setzt die Katze auf den Tisch » → « Бен сажает кота на стол »**.

## Ajouté le 15 nov. (revue des traductions)

- **« Décrire une personne » : « glatt » (des cheveux) → « прямые (волосы) »**, au lieu de la glose du corpus (lisse, glissant).
  Elle vit dans `visuel/familia/gloses.py`, `SENS_CHEVEUX` ; on corrige là, puis `python visuel/familia/gloses.py`.

## Lot 2, 15 nov. : « La famille d'Anna »

La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia ru`. Il n'y a pas eu de relecture native.

1. **Les noms** : Хайнц, Гизела, Петер, Моника, Сабина (Sabine), Франк, Ян, Катрин et Софи (indéclinables), Анна,
   Лена, Феликс, Бен, Мия ; génitif (« отец Анны ») et accusatif après спрашивать (« спрашивает Бена »).
2. **Les beaux-parents selon le conjoint** : свёкор / свекровь pour la femme (Monika, Katrin), тесть / тёща pour le
   mari (Frank). Dans les paires sans personne : « тесть, свёкор → тёща, свекровь ».
3. **Les beaux-frères et belles-sœurs, lus dans l'arbre** : зять (le mari de la sœur : Frank pour Peter), шурин (le
   frère de la femme : Peter pour Frank), невестка (la femme du frère : Katrin pour Anna, Monika pour Sabine), золовка
   (la sœur du mari : Sabine pour Monika, Anna pour Katrin). Sont-ils encore compris, ou faut-il « муж сестры »,
   « брат жены » ?
4. **« мои сын и дочери »**, « мои двоюродный брат и двоюродные сёстры » : le possessif au pluriel devant des mots au
   singulier et au pluriel.
5. **Le point après la citation** : « Анна говорит: «Петер — мой отец». » ; rien après « ? ».

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **komisch** : « чудной » (la théière, le bruit), **seltsam** : « странный » (la chaise, la question) — les deux gloses disent « странный ».
2. **gut** : « Торт вкусный » pour le gâteau ; **schlecht** : « Яблоко испорченное ».
3. **Tür** : « дверь » au singulier, formes courtes pour l'état (« Дверь открыта »).

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js`. À relire :

1. **Bürgeramt** : « бюро обслуживания граждан » (indéclinable, neutre : « бюро … закрыто ») ; **Krankenkasse** : « больничная касса ».
2. **Le jour** : « в среду в 15:00 », « во вторник » ; le rendez-vous « Марк записан на вторник на 9:30 в … ».
3. **« Il faut »** accordé : « нужен паспорт », « нужна фотография », « нужно подтверждение от арендодателя ».
4. **Les noms** : Марк Гарнье, Монреаль, Берлин, « Гартенштрассе, 12 » ; familienstand « холост » (женат, разведён pour les leurres).

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js`. À relire :

1. **Le nombre** : « нужна тетрадь », « нужны две тетради », « нужно пять тетрадей ».
2. **Kita / Kindergarten** : « детский сад » et « садик ».
3. **Le mot d'absence** : « Бена не будет в школе в понедельник и во вторник, потому что он болен ».
4. **Sachunterricht** : « окружающий мир » (la matière de l'école primaire russe).

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js`. À relire :

1. **Les prénoms à l'accusatif et au génitif** : « приглашает Анну », « Сегодня у Анны день рождения » ; Софи, Катрин indéclinables.
2. **Le délai accordé** : « Анна должна / Феликс должен ответить до среды ».
3. **Silvester** : « новогодняя ночь », « С наступающим Новым годом! » ; « Феликс встречает Новый год ».
4. **Le possessif réfléchi** : « на свой праздник », « на своё новоселье ».
5. **Le double tiret de la découverte** : la phrase de la date porte son tiret (« Пасха — в марте или в апреле. »), qui tient lieu du verbe « être » ; la découverte la joint au souhait par un second « — ». Gardé ainsi (chef, 16 nov.).

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js`. À relire :

1. **Le magasin** : « в булочной / в булочную », « на рынке / на рынок », Metzgerei « мясная лавка ».
2. **Le besoin** : « Марку / Анне нужно купить колбасу » ; la commande « Дайте, пожалуйста, … ».
3. **Le nombre** : « Яблоки стоят », mais « Клубника стоит » (collectif singulier) ; « Клубника дороже, чем … ».
4. **La monnaie** : « Ему / Ей дают 0,80 € сдачи ».

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js`. À relire :

1. **Je et tu** : « Я собрал(а) свой чемодан », et « пошёл / пошла » quand la forme féminine n'ajoute pas seulement « а ».
2. **La famille au singulier** : « Семья поехала на машине на Балтийское море » ; « Бен и Мия построили замок из песка ».
3. **L'accueil** : « Здравствуйте, я забронировал(а) одноместный номер на две ночи ».
4. **Mark au port** : « прокатился на катере по порту ».

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js`. À relire :

1. **« Любит » + infinitif** : « Роза любит играть в футбол », « Феликс и Роза любят … ».
2. **Proposer** : « Хочешь играть в футбол? », « Давай вместе играть в футбол? ».
3. **Jamais** : « Феликс никогда не играет в футбол ».

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js`. À relire :

1. **L'accusatif** : « Анна обожает торт », « любит клубнику », « совсем не любит рыбу ».
2. **Le génitif après la quantité** : « Килограмм апельсинов », « 1 кг помидоров », « 2 пачки печенья ».
3. **Commander** : « Мне кофе, пожалуйста. » ; « Кармен берёт кофе и два чая. С вас 6,90 €. »
4. **Les figurants** : « мужчина с седыми волосами », « женщина с кудрявыми волосами ».

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **Le même mot pour les deux sexes** : « Она врач. », « Она хороший врач. » (l'adjectif s'accorde au nom masculin), mais « хорошая учительница ».
2. **La policière** : « сотрудница полиции » (d'après la glose du corpus) ; « Елена работает сотрудницей полиции. ».
3. **La paire** : « врач (мужчина) → врач (женщина) » quand le mot ne change pas.
4. **Le lieu** : « во врачебном кабинете » (Praxis), « в гостинице » (Hotel).

## Lot 12, 16 nov. : « La météo et les saisons »

La page traduit maintenant ses phrases (le temps qu'il fait, les activités de chaque saison, « j'ai froid », les mois et les degrés) : elles sont écrites dans `visuel/meteo/langues.py` et versées dans `meteo.json` par `meteo.py`. À relire :

1. **Sans sujet** : « Холодно. », « Жарко. » (heiß), « Тепло. » (warm), « Сейчас весна. ».
2. **« Идёт гроза. »** pour « Es gibt ein Gewitter. » (« Сегодня гроза. » avec heute).
3. **Les degrés accordés** : « 21 градус », « 22 градуса », « 12 градусов », « Сейчас минус 12 градусов. ».
4. **Le choix « Ich bin kalt. »** : « моё тело холодное на ощупь, или я холодный человек » (« человек » est masculin comme nom).
