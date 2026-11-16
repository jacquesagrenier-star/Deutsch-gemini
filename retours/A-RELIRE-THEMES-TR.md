# Les thèmes illustrés en turc : ce qu'un locuteur natif devrait relire

14 nov. 2026, lot 1 de l'alignement des thèmes (« Où est le chat ? » et « La journée »). Pour qui apprend l'allemand
avec l'interface en turc, la page montre désormais la phrase entière traduite, comme en français, en anglais et en
portugais. Il n'y a pas eu de relecture native. Une rétro-traduction à l'aveugle (vers le français, sans
l'allemand) n'a trouvé aucune faute de turc ; deux tournures ont été changées : « üzerinde asılı » au lieu de
« yukarısında », et « pijamalarımızı ».

- Les traductions ne sont pas écrites phrase par phrase : on traduit les morceaux que la page assemble.
  - « Où est le chat ? » : `visuel/gato/langues.py`, tables `TR` et `TR_PL` (nominatif, génitif, locatif, datif de
    16 noms), `TR_POST` (üstünde / üstüne…), `lieu()`, `POSTURE`, `MOUVEMENT`, `PHRASES`. On corrige là, puis
    `python visuel/gato/gato.py --json`.
  - « La journée » : `visuel/journee/langues.py`, `VERBES` (19 verbes aux cinq personnes, sans pronom sujet,
    l'heure avant le verbe), `SUJETS`, `FREQUENCES`. On corrige là, puis `python visuel/journee/journee.py --json`.
    L'heure et son suffixe (« saat 7'de », « saat 6.30'da », « saat 7.15'te ») sont dans
    `visuel/prototype/journee.html` (`heureTrad`).
- Contrôle à l'écran : `python visuel/langues_themes.py verifier gato journee tr`.

## Ce que le turc fait, et qui est voulu

« Où » et « vers où » comme l'allemand : masanın üstünde / üstüne (auf dem / auf den Tisch), altında / altına,
içinde / içine, arkasında / arkasına. Le présent en -iyor pour la journée qu'on raconte, l'aoriste pour les habitudes
(« Anna kahvaltısını her zaman evde yapar »).

## Points à confirmer

1. **« über » → « üzerinde »** (la lampe au-dessus de la table, sans contact) et **« über » + accusatif →
   « üzerinden »** (« Kedi kutunun üzerinden atlıyor ») ; « auf » → « üstünde ». La différence üstünde / üzerinde
   est-elle assez claire ?
2. **« an » → le nom seul au locatif ou au datif** : « Kedi pencerede oturuyor », « Kedi pencereye oturuyor ».
3. **« Kissen » → « kırlent »** (coussin de canapé), « Regal » → « kitaplık » (« kitaplığın rafında » pour « im
   Regal »), « Karton » → « kutu ».
4. **« legt sich in den Korb » → « Kedi sepetin içine yatıyor »**.
5. **« läuft hinter » → « arkasına geçiyor »**, « kriecht unter » → « altına giriyor ».
6. **« Ben und Mia » → « Ben ile Mia »**, verbe au pluriel (« uyanıyorlar ») dans la journée.
7. **Le suffixe de l'heure** suit le dernier nombre prononcé, sur 24 heures (« saat 22.30'da », « saat 18'de »).

## Ajouté le 15 nov. (revue des traductions)

- **« Décrire une personne » : « glatt » (des cheveux) → « düz (saç) »**, au lieu de la glose du corpus (lisse, glissant).
  Elle vit dans `visuel/familia/gloses.py`, `SENS_CHEVEUX` ; on corrige là, puis `python visuel/familia/gloses.py`.

## Lot 2, 15 nov. : « La famille d'Anna »

La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia tr`. Il n'y a pas eu de relecture native.

1. **Le côté de l'oncle et de la tante, lu dans l'arbre** : Sabine est la **hala** d'Anna (la sœur du père), Frank son
   **enişte** (le mari de la hala) ; Peter est le **dayı** de Felix et Sophie (le frère de la mère), Monika leur
   **yenge**. Dans les paires sans personne : « amca, dayı → hala, teyze ».
2. **La grand-mère** : **babaanne** du côté du père (Gisela pour Jan, Anna, Lena ; Monika pour Ben et Mia),
   **anneanne** du côté de la mère (Gisela pour Felix et Sophie).
3. **Les beaux-frères et belles-sœurs** : enişte (le mari de la sœur), kayınbirader (le frère de la femme), yenge (la
   femme du frère : Katrin pour Anna), görümce (la sœur du mari : Anna pour Katrin, Sabine pour Monika).
4. **« eşi » pour l'épouse**, « kocası » pour le mari (plutôt que « karısı »).
5. **« torun », « yeğen », « kuzen »** sans le sexe quand le prénom le dit (« Onların beş torunu var »).
6. **La citation** : « Anna şöyle diyor: “Peter benim babam.” », « Anna Ben'e soruyor: “Jan senin baban mı?” ».

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **gut** pour le gâteau : « Pasta lezzetli. » plutôt que « Pasta iyi. » (la glose du mot reste iyi) ; « Bu iyi bir restoran. » ailleurs.
2. **komisch / seltsam** gardent deux mots : garip (la théière, le bruit) et tuhaf (la chaise, la question), comme les gloses.
3. **Straße** : « Cadde » pour la rue large comme pour l'étroite (un seul nom pour la paire) ; « Die Gasse ist eng und schmal. » : « Ara sokak dar ve sıkışık. »
4. **wunderschön** : « harika » (la glose dit « göz alıcı », peu naturel dans « Manzara göz alıcı »).

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js`. À relire :

1. **Bürgeramt** : « vatandaş hizmetleri bürosu » (la glose du corpus) ; **Krankenkasse** : « hastalık sigortası kurumu » ; **Praxis** : « muayenehane ».
2. **L'heure et son suffixe** : « saat 15.00'te », « saat 9.30'da », « saat 7.00'de » (le suffixe suit la lecture : on beş, dokuz otuz, yedi).
3. **Le guichet** : « Lütfen … » à l'impératif poli (« Lütfen formu doldurun. ») ; « Lütfen buraya imza atın. » pour « Unterschreiben Sie bitte hier! ».
4. **Les champs** : « Mark'ın uyruğu Kanadalı. », « Mark'ın medeni durumu bekâr. », « Mark'ın şehri Berlin. » (Ort).

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js`. À relire :

1. **« Ben'e … lazım »** pour « Ben braucht » : le prénom Ben porte l'apostrophe (Ben'e, Ben'in, Ben'i), à ne pas lire comme le pronom « ben ».
2. **L'heure et le mois prennent le suffixe du dernier mot lu** : « saat 8.45'te », « saat 10.40'ta », « 28 Aralık'ta », « 1 Ocak'ta », « 3 Nisan'da ».
3. **Kita / Kindergarten** : « kreş » et « anaokulu » ; **Anna**, la tante paternelle de Mia : « halası ».
4. **Le mot d'absence** : « Ben Pazartesi ve Salı okula gelemiyor, çünkü hasta. »
