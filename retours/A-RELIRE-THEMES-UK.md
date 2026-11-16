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
