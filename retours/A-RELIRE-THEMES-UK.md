# Les thèmes illustrés en ukrainien : ce qu'un locuteur natif devrait relire

14 nov. 2026, lot 1 de l'alignement des thèmes (« Où est le chat ? » et « La journée »). Pour qui apprend l'allemand
avec l'interface en ukrainien, la page montre désormais la phrase entière traduite, comme en français, en anglais et
en portugais. Il n'y a pas eu de relecture native. Une rétro-traduction à l'aveugle (vers le français, sans
l'allemand) a relevé un seul point, corrigé : « одягаємо / одягають піжами » au pluriel.

- Les traductions ne sont pas écrites phrase par phrase : on traduit les morceaux que la page assemble.
  - « Où est le chat ? » : `visuel/gato/langues.py`, tables `UK` et `UK_PL` (les six cas de 16 noms), `lieu()`,
    `POSTURE`, `MOUVEMENT`, `PHRASES`, et `_uk_v()` (у / в selon le mot d'avant), `_zi()` (із / зі). On corrige là,
    puis `python visuel/gato/gato.py --json`.
  - « La journée » : `visuel/journee/langues.py`, `VERBES` (19 verbes aux cinq personnes), `SUJETS`, `FREQUENCES`.
    On corrige là, puis `python visuel/journee/journee.py --json`. L'heure (« о 7:15 », « об 11:00 ») et les mots de
    liaison sont dans `visuel/prototype/journee.html` (`heureTrad`, `LIENS_TR`).
- Contrôle à l'écran : `python visuel/langues_themes.py verifier gato journee uk`.

## Ce que l'ukrainien fait, et qui est voulu

« Où » et « vers où » comme l'allemand : на столі / на стіл, під столом / під стіл, у кошику / в кошик, за диваном
/ за диван. Après перед, поруч із, між, біля, la même forme pour les deux. L'apostrophe est ʼ (règle de la v1187),
aucune phrase de ce lot n'en a.

## Points à confirmer

1. **« ans Fenster » → « сідає біля вікна »** ; groupes isolés : « am Fenster » = « біля вікна », « ans Fenster » =
   « до вікна ».
2. **« neben » → « поруч із / зі »**, pour garder « біля » à « an » (« біля вікна »).
3. **« im Regal » → « на полиці стелажа »**.
4. **« mit der U-Bahn zur Arbeit fahren » → « їде на роботу метро »**.
5. **« sich duschen » → « приймає душ »**, « den Schlafanzug anziehen » → « одягає піжаму » (« надягає » ?).
6. **« joggen gehen » → « йде на пробіжку »** (й partout, même après une consonne).
7. **Les noms** : Моріц, Мія (Мії, Мію, Мією), Катрін, Ян.
8. **« Ben setzt die Katze auf den Tisch » → « Бен садить кота на стіл »**.

## Ajouté le 15 nov. (revue des traductions)

- **« Décrire une personne » : « glatt » (des cheveux) → « пряме (волосся) »**, au lieu de la glose du corpus (lisse, glissant).
  Elle vit dans `visuel/familia/gloses.py`, `SENS_CHEVEUX` ; on corrige là, puis `python visuel/familia/gloses.py`.

## Lot 2, 15 nov. : « La famille d'Anna »

La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia uk`. Il n'y a pas eu de relecture native.

1. **Les noms** : Гайнц, Гізела, Петер, Моніка, Сабіна, Франк, Ян, Катрін et Софі (indéclinables), Анна, Лена,
   Фелікс, Бен, Мія ; génitif (« батько Анни ») et accusatif après питати (« питає Бена »).
2. **« В Анни »** en début de phrase (devant une voyelle), « У Яна » ailleurs.
3. **« онучка »** pour la petite-fille (le corpus dit « онука », dont le pluriel « онуки » se confond avec celui
   d'« онук » : « два онуки і три онучки »).
4. **Les beaux-parents selon le conjoint** : свекор / свекруха pour la femme, тесть / теща pour le mari.
5. **Les beaux-frères et belles-sœurs** : зять (le mari de la sœur), шурин (le frère de la femme), невістка (la femme
   du frère), зовиця (la sœur du mari). Compris de tous ?
6. **« пʼять »** avec l'apostrophe ukrainienne.

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **komisch** : « чудернацький » (la théière, le bruit), **seltsam** : « дивний » (la chaise, la question), pour garder deux mots.
2. **Tür** : « двері », toujours au pluriel (« Двері відчинені », « Це відчинені двері »).
3. **gut** : « Торт смачний » pour le gâteau, « хороший ресторан » (la glose dit « добрий »).
4. **klein** : « маленька валіза » (la glose dit « малий »).

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js`. À relire :

1. **Bürgeramt** : « центр обслуговування громадян » (la glose dit « муніципальний офіс ») ; **Praxis** : « кабінет лікаря ».
2. **Le jour** : « у середу о 15:00 » ; le rendez-vous « Марк записаний на вівторок на 9:30 у … ».
3. **Ouvert / fermé** accordés avec le lieu : « центр … відчинений », « лікарняна каса зачинена ».
4. **« Il faut »** accordé avec le document : « потрібен паспорт », « потрібна довідка про реєстрацію », « потрібне підтвердження від орендодавця ».
5. **Les noms** : Марк Гарньє, Монреаль, Берлін, « Гартенштрассе, 12 ».

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js`. À relire :

1. **Le nombre** : « потрібен зошит », « потрібні два зошити / дві лінійки », « потрібно пʼять зошитів » ; les ciseaux « дві пари ножиць » (la page n'en compte qu'une).
2. **Kita / Kindergarten** : « дитсадок » et « дитячий садок » (deux noms proches pour deux mots allemands proches).
3. **Le mois au génitif** : « 28 грудня у Бена канікули ».
4. **L'emploi du temps** : « У понеділок на третьому уроці в Бена математика ».

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js`. À relire :

1. **Les prénoms à l'accusatif** : « запрошує Анну / Фелікса » ; Sophie et Katrin indéclinables (« Софі », « Катрін »).
2. **Le possessif réfléchi** : « на своє свято », « на свій день народження », « на своє новосілля ».
3. **Silvester** : « новорічна ніч », le souhait « З наступаючим Новим роком! » ; Felix « зустрічає Новий рік ».
4. **« J'ai le temps »** neutre (« в мене є час ») plutôt que « я вільний / вільна », la personne pouvant être une femme.
5. **Le double tiret de la découverte** : la phrase de la date porte son tiret (« Великдень — у березні або у квітні. »), qui tient lieu du verbe « être » ; la découverte la joint au souhait par un second « — ». Gardé ainsi (chef, 16 nov.).

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js`. À relire :

1. **Le magasin** : « у пекарні / до пекарні », « на ринку / на ринок » ; Metzgerei « мʼясна крамниця », Drogerie « магазин побутової хімії ».
2. **Le besoin** : « Маркові / Анні треба купити ковбасу » (l'infinitif évite l'accord de « потрібен »).
3. **Comparer** : « Масло коштує більше, ніж сир » (plutôt qu'un comparatif accordé).
4. **La monnaie** : « Йому / Їй дають 0,80 € решти » ; la commande « Дайте, будь ласка, … ».

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js`. À relire :

1. **Je et tu, dont le genre n'est pas connu** : les deux formes, « Я зібрав / зібрала свою валізу » (le français écrit « allé(e) »).
2. **Le possessif réfléchi** à toutes les personnes : « свою валізу », « свій рюкзак » (« Ми зібрали свою валізу » : un seul objet, comme le français).
3. **La famille** : « Родина поїхала машиною до Балтійського моря » ; Ben et Mia « Бен і Мія збудували замок із піску ».
4. **Les nuits** : « на одну ніч / на дві ночі / на пʼять ночей ».

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js`. À relire :

1. **« Любить » + infinitif** : « Роза любить грати у футбол », « Фелікс і Роза люблять … ».
2. **Proposer** : « Хочеш грати у футбол? », « Давай разом грати у футбол? ».
3. **Jamais** : « Фелікс ніколи не грає у футбол ».

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js`. À relire :

1. **L'accusatif** : « Анна обожнює торт », « любить полуницю », « зовсім не любить рибу ».
2. **Le génitif après la quantité** : « Кілограм апельсинів », « 1 кг помідорів », « 2 пачки печива ».
3. **Trop …** : « Занадто солодко! » (adverbe neutre) ; goûter « куштує щось солодке ».
4. **Le café** : « Чоловік із сивим волоссям — офіціант », « Кармен бере каву і два чаї. З вас 6,90 €. »

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **Le tiret** entre le prénom et le métier : « Дієго — лікар. », mais « Вона лікарка. » avec le pronom.
2. **L'instrumental** après « працює » : « працює лікаркою », « працює продавчинею », « працює механікинею ».
3. **Les féminins** : « механікиня », « продавчиня », « фармацевтка », « адміністраторка » (receptionist d'hôtel).
4. **Le lieu** : « у лікарському кабінеті » (Praxis, d'après la glose du corpus).
