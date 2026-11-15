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
