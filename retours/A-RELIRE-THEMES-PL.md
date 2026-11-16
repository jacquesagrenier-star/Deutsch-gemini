# Les thèmes illustrés en polonais : ce qu'un locuteur natif devrait relire

14 nov. 2026, lot 1 de l'alignement des thèmes (« Où est le chat ? » et « La journée »). Pour qui apprend l'allemand
avec l'interface en polonais, la page montre désormais la phrase entière traduite, comme en français, en anglais et
en portugais. Il n'y a pas eu de relecture native. Une rétro-traduction à l'aveugle (vers le français, sans
l'allemand) a relevé deux points, corrigés : « zakładamy / zakładają piżamy » au pluriel, « Anna wkłada kota do
kosza ».

- Les traductions ne sont pas écrites phrase par phrase : on traduit les morceaux que la page assemble.
  - « Où est le chat ? » : `visuel/gato/langues.py`, tables `PL` et `PL_PL` (les six cas de 16 noms), `lieu()`,
    `POSTURE`, `MOUVEMENT`, `PHRASES`. On corrige là, puis `python visuel/gato/gato.py --json`.
  - « La journée » : `visuel/journee/langues.py`, `VERBES` (19 verbes aux cinq personnes, sans pronom sujet),
    `SUJETS`, `FREQUENCES`. On corrige là, puis `python visuel/journee/journee.py --json`. L'heure (« o 7:15 ») et
    les mots de liaison sont dans `visuel/prototype/journee.html`.
- Contrôle à l'écran : `python visuel/langues_themes.py verifier gato journee pl`.

## Ce que le polonais fait, et qui est voulu

« Où » et « vers où » comme l'allemand : na stole / na stół, pod stołem / pod stół, w koszu / do kosza, za kanapą /
za kanapę. Après przed, obok, między, nad, la même forme pour les deux (« siada przed kanapą »).

## Points à confirmer

1. **« ans Fenster » → « siada przy oknie »** ; groupes isolés : « am Fenster » = « przy oknie », « ans Fenster » =
   « do okna ».
2. **« Ben setzt die Katze auf den Tisch » → « Ben sadza kota na stole »** (locatif, habituel avec sadzać ; « na
   stół » marquerait la direction comme l'allemand).
3. **« legt sich in den Korb » → « kładzie się do kosza »**.
4. **« przed » et « między » à l'instrumental pour la direction** (« siada między poduszkami ») ; l'accusatif
   (« między poduszki ») est possible mais littéraire.
5. **« kriecht unter / in » → « wchodzi pod / do »**, « läuft hinter » → « wchodzi za », « springt » →
   « wskakuje ».
6. **« joggen gehen » → « idzie pobiegać »**.
7. **« Bild » → « obraz »**, « Regal » → « regał » (« na półce regału » pour « im Regal »), « Korb » → « kosz ».

## Ajouté le 15 nov. (revue des traductions)

- **« Décrire une personne » : « glatt » (des cheveux) → « proste (włosy) »**, au lieu de la glose du corpus (lisse, glissant).
  Elle vit dans `visuel/familia/gloses.py`, `SENS_CHEVEUX` ; on corrige là, puis `python visuel/familia/gloses.py`.

## Lot 2, 15 nov. : « La famille d'Anna »

La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia pl`. Il n'y a pas eu de relecture native.

1. **« Peter jest ojcem Anny »** (być + instrumental), et dans les citations « Peter jest moim ojcem », « Czy Jan jest
   twoim ojcem? » ; « Anna mówi: „…”. ».
2. **Les noms** : Anny / Annę, Giseli / Giselę, Moniki / Monikę, Leny / Lenę, Mii / Mię, Petera, Heinza, Franka, Jana,
   Felixa, Bena ; Sabine, Katrin et Sophie indéclinables.
3. **Le neveu selon le frère ou la sœur** : bratanek / bratanica (l'enfant du frère : Sabine et Frank pour Jan, Anna,
   Lena ; Anna et Lena pour Ben et Mia), siostrzeniec / siostrzenica (l'enfant de la sœur : Peter et Monika pour Felix
   et Sophie). Pour Frank et Monika (le côté du conjoint), le même mot : juste ?
4. **wujek / ciocia** (familier) plutôt que stryj / wuj / ciotka.
5. **Les nombres** : « dwóch wnuków i trzy wnuczki », « ma kuzyna i dwie kuzynki ».

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **komisch** : « dziwaczny » (imbryk, dźwięk), **seltsam** : « dziwny » (krzesło, pytanie).
2. **Teekanne** : « imbryk » ; **Handy** : « telefon » ; **schlecht** pour le film : « zły film » (« słaby film » serait plus courant ?).
3. **Der Kuchen schmeckt sehr gut** : « Ciasto bardzo dobrze smakuje. »

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js`. À relire :

1. **Bürgeramt** : « biuro obsługi mieszkańców » (à relire : « urząd meldunkowy » ?) ; **Krankenkasse** : « kasa chorych ».
2. **Anmelden** : « Mark melduje się w … » ; le guichet « Proszę się zameldować. ».
3. **« Il faut »** : « Do zameldowania potrzebny jest paszport », « potrzebna jest karta… », « potrzebne jest zdjęcie ».
4. **Les champs** au style d'un formulaire : « Nazwisko Marka: Garnier. », « Stan cywilny Marka: kawaler. ».

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js`. À relire :

1. **Kita et Kindergarten** donnent tous deux « przedszkole » (à relire : un mot pour la Kita ?).
2. **« Ben potrzebuje » + génitif** : « zeszytu », « dwóch zeszytów », « pięciu linijek ».
3. **La matière à l'accusatif** : « Ben ma matematykę / plastykę / muzykę / przyrodę ».
4. **Les vacances** : « 28 grudnia Ben ma wolne od szkoły » (ni « ferie » ni « wakacje », qui dépendent de la saison).

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js`. À relire :

1. **Les prénoms à l'accusatif** : « zaprasza Annę / Feliksa / Lenę », Sophie et Katrin indéclinables.
2. **Fest / Feier / Einweihungsparty** : « przyjęcie », « uroczystość », « parapetówka ».
3. **« Dziś Anna ma urodziny »** ; Silvester « sylwester » (minuscule).
4. **Le délai** : « Anna musi odpowiedzieć do środy ».

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js`. À relire :

1. **Le magasin** : « w piekarni / do piekarni », « na targu / na targ », Metzgerei « sklep mięsny ».
2. **Le besoin** : « Mark musi kupić kiełbasę » ; la commande « Poproszę … » à l'accusatif.
3. **Comparer** : « Masło kosztuje więcej / mniej niż ser » (pas de comparatif à accorder).
4. **Le dialogue** : « Potrzebuje pan torebki? », « Następna osoba, proszę! » (le vendeur vouvoie au masculin : à relire).

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js`. À relire :

1. **La personne dans le verbe** : « spakowałem / spakowałam », « spakowałeś / spakowałaś », « spakowaliśmy » ; « poszedłem / poszłam ».
2. **Le sujet sous-entendu dans une suite** : « Najpierw Anna spakowała swoją walizkę. Potem pojechała na lotnisko. »
3. **Mark au port** : « popłynął statkiem po porcie » (Hafenrundfahrt) ; la famille « nad Bałtyk ».
4. **Les nuits** : « na jedną noc / na dwie noce / na pięć nocy ».

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js`. À relire :

1. **« Lubi » + infinitif** : « Rosa lubi grać w piłkę nożną », pluriel « lubią ».
2. **Proposer** : « Masz ochotę grać w piłkę nożną? », « Może razem zagramy w piłkę nożną? » (un futur perfectif par activité, à relire : « poćwiczymy », « ugotujemy coś »).
3. **Jamais** : « nigdy nie gra ».

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js`. À relire :

1. **Le génitif après la négation** : « nie lubi cytryn », « w ogóle nie lubi ryb », « Nie lubię zupy ».
2. **Goûter** : « próbuje czegoś słodkiego » (génitif) ; « Za słodkie! ».
3. **La liste** : « 1 opakowanie makaronu », « 2 opakowania ciastek », « ½ kg ziemniaków ».
4. **Le café** : « Poproszę kartę. », « To dla pani. » (le pourboire à la serveuse : à relire).

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **L'instrumental après « jest »** : « Diego jest lekarzem. », « Ona jest dobrą lekarką. » ; mais « pracuje jako lekarka » (nominatif après « jako »).
2. **Les féminins** : « mechaniczka », « sprzedawczyni », « farmaceutka », « recepcjonistka ».
3. **Le pronom gardé** : « Ona jest lekarką. » (l'allemand dit « Sie ist Ärztin. ») ; un natif dirait souvent « Jest lekarką. ».
4. **« pracuje w policji »** pour « arbeitet bei der Polizei ».

## Lot 12, 16 nov. : « La météo et les saisons »

La page traduit maintenant ses phrases (le temps qu'il fait, les activités de chaque saison, « j'ai froid », les mois et les degrés) : elles sont écrites dans `visuel/meteo/langues.py` et versées dans `meteo.json` par `meteo.py`. À relire :

1. **« Jest … »** : « Jest zimno. », « Jest gorąco. » (heiß), « Jest ciepło. » (warm), « Jest wiosna. ».
2. **« Jest mi zimno. »** / « Jest mi gorąco. » pour « Mir ist kalt / heiß ».
3. **Les degrés accordés** : « Jest 2 stopnie. », « Jest 21 stopni. », « Jest minus 12 stopni. ».
4. **« Dziś dużo pada. »** pour « Heute gibt es viel Regen. » ; « Pogoda jest brzydka. » pour « Das Wetter ist schlecht. ».

## Lot 13, 16 nov. : « Les animaux »

La page traduit maintenant ses phrases (c'est un…, le pluriel, où il vit, ce qu'il mange, sa couleur, plus grand / plus petit que, la phrase de la découverte) et le lieu ou la couleur choisis : elles sont refaites par la grammaire de chaque langue dans `visuel/animales/langues.py`, versées dans `animales.json` par `animales.py`. À relire :

1. **La comparaison** : « Wiewiórka jest mniejsza od niedźwiedzia. », « Pies jest większy od myszy. ».
2. **Les couleurs accordées** : « Krowa jest czarno-biała. », « Lis jest rudy. » (l'allemand dit orange, comme le français « roux »).
3. **La découverte sans pronom** : « Kot żyje w domu. Je mięso. ».
4. **« na farmie »** pour « auf dem Bauernhof » (plutôt que « w gospodarstwie » ?) ; « Niedźwiedź je ryby. ».

## Lot heure, 16 nov. : « L'heure et les dates »

Thème neuf. Ses phrases traduites sont fabriquées par `visuel/prototype/heure/dire.js` (une heure, une date ou un rendez-vous → la phrase, par la même règle que la langue apprise) ; l'heure y est en chiffres, à la manière de la langue. Tout se voit d'un coup dans `visuel/heure/banc.md` (`node tests/heure_banc.js`). À relire :

1. **Le jour avec sa préposition** : « Lekcja jogi jest we wtorek o 9:00. », « w środę », « w niedzielę ».
2. **Hier** : « Wczoraj był poniedziałek. », « Wczoraj była środa. ».
3. **Les mois** : « Po kwietniu jest maj. », « Przed czerwcem jest maj. », « Moje urodziny są 3 maja. », « … we wrześniu. ».
4. **Les mots** : « wizyta u lekarza », « trening piłki nożnej trwa dwie godziny », « Jest południe. », « Jest północ. ».

## Lot 14, 16 nov. : « En ville : s'orienter »

La page traduit maintenant ses phrases (demander s'il y a un lieu, comment y aller, où il est, les itinéraires et les gestes au carrefour) et le groupe choisi : elles sont refaites par la grammaire de chaque langue dans `visuel/ciudad/langues.py`, versées dans `ciudad.json` par `ciudad.py`. Les noms des rues restent ceux du plan (Bergstraße, calle Mayor), comme en français. À relire :

1. **La forme polie en « proszę »** : « Proszę skręcić w pierwszą ulicę w lewo. », « Potem na trzecim skrzyżowaniu proszę skręcić w prawo. ».
2. **Les cas** : « obok banku », « naprzeciwko poczty », « między piekarnią a bankiem », « jak dojść do apteki ».
3. **La fin** : « Dworzec jest po lewej stronie. », sans lieu « To jest po lewej stronie. ».
4. **Les lieux** : « komisariat policji », « kawiarnia » (Café), « przystanek » (Haltestelle).
