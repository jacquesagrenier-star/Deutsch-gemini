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

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js`. À relire :

1. **Les prénoms à l'accusatif et au génitif** : « Anna'yı », « Felix'i », « Sophie'yi », « Bugün Anna'nın doğum günü ».
2. **Le souhait de Silvester** : « İyi yıllar! » (« Bonne fin d'année ») ; de Neujahr « Mutlu yıllar! ».
3. **L'agenda** : « Pazartesi günü olmaz: çalışmam gerekiyor. Salı günü nasıl? » ; « Parti saat 19.00'da başlıyor ».
4. **La pendaison de crémaillère** : « yeni ev partisi » (Einweihungsparty).

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js`. À relire :

1. **Le magasin à cinq formes** : « fırın / fırında / fırına / fırından / Fırındayız » ; Drogerie « kozmetik mağazası » (à relire), Kiosk « büfe ».
2. **« Mark'ın ekmek alması gerekiyor »** pour « Mark braucht Brot » ; Wurst « salam ».
3. **Le dialogue** : « Ne arzu edersiniz? », « Sıradaki, lütfen! », « para üstü ».
4. **Comparer** : « Tereyağı peynirden daha pahalı » (l'ablatif écrit à la main pour chaque article).

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js`. À relire :

1. **« Ben ve Mia »** : le prénom Ben se lit aussi « je » (« Ben ve Mia kumdan bir kale yaptılar ») ; à relire, peut-être « Ben ile Mia ».
2. **Le possessif suit la personne** : « bavulumu / bavulunu / bavullarımızı topladık », « sırt çantamı / sırt çantasını ».
3. **La chambre** : « iki gece için tek kişilik bir oda », l'accueil « … ayırttım ».
4. **Le sujet sous-entendu dans une suite** : « Önce Anna bavulunu topladı. Sonra havalimanına gitti. »

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js`. À relire :

1. **L'aoriste pour l'habitude** : « Rosa futbol oynar », « Felix hiç futbol oynamaz », « futbol oynamayı sever ».
2. **Proposer** : « Futbol oynamak ister misin? », « Birlikte futbol oynayalım mı? » (mı / mi par l'harmonie).
3. **Les instruments** : « gitar / piyano / keman çalar » ; « dans eder », « şarkı söyler ».

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js`. À relire :

1. **L'accusatif de l'aliment** : « Anna pastayı çok sever », « Carmen limonu sevmez » ; « Lucas balığı hiç sevmez ».
2. **Amer et épicé** : « acı » pour l'amer (« Sade kahve acı »), « acılı » pour l'épicé (« Yemek acılı », « Çok acılı! ») — à relire.
3. **Le café** : « Kır saçlı adam garson. », « Carmen bir kahve ve iki çay alıyor. Toplam 6,90 €. »
4. **La livre allemande (Pfund)** se dit « ½ kg » (500 g), comme en Allemagne.

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **Le métier sans article** : « Diego doktor. », « O kuaför. » ; avec l'adjectif, « Diego iyi bir doktor. ».
2. **« Je suis »** : « Ben doktorum. », « Ben eczacıyım. », « Ben polis memuruyum. ».
3. **Le lieu** : « muayenehanede » (Praxis), « tamirhanede » (Werkstatt), « emniyette » (bei der Polizei), « dükkânda ».
4. **Un seul mot pour les deux sexes** : la paire dit « erkek doktor → kadın doktor », « erkek hemşire → kadın hemşire » (Krankenpfleger → Krankenschwester).

## Lot 12, 16 nov. : « La météo et les saisons »

La page traduit maintenant ses phrases (le temps qu'il fait, les activités de chaque saison, « j'ai froid », les mois et les degrés) : elles sont écrites dans `visuel/meteo/langues.py` et versées dans `meteo.json` par `meteo.py`. À relire :

1. **« Hava … »** pour le temps qu'il fait : « Hava soğuk. », « Hava çok sıcak. » (heiß), « Hava ılık. » (warm, « il fait bon ») : « ılık » est-il juste pour 20 à 26 degrés ?
2. **La saison seule** : « Mevsim ilkbahar. » pour « Es ist Frühling. » ; un natif dirait-il plutôt « İlkbahar. » ou « Şimdi ilkbahar. » ?
3. **Les mois** : « Ocak ayında Almanya'da kış olur. » ; et « Sıcakladım. » pour « Mir ist heiß. ».
4. **Les degrés** : « Hava eksi 12 derece. », « Hava 0 derece. » ; « Gök gürültülü fırtına var. » (Gewitter, d'après la glose du corpus).

## Lot 13, 16 nov. : « Les animaux »

La page traduit maintenant ses phrases (c'est un…, le pluriel, où il vit, ce qu'il mange, sa couleur, plus grand / plus petit que, la phrase de la découverte) et le lieu ou la couleur choisis : elles sont refaites par la grammaire de chaque langue dans `visuel/animales/langues.py`, versées dans `animales.json` par `animales.py`. À relire :

1. **Le singulier après un nombre** : « bir at, iki at » pour « ein Pferd, zwei Pferde » (le pluriel allemand n'a pas d'équivalent).
2. **La comparaison à l'ablatif** : « Sincap ayıdan küçüktür. », « Ayı japon balığından büyüktür. ».
3. **Les couleurs** : « Tilki turuncu. » (l'allemand dit orange ; un natif dirait-il « kızıl » ?), « İnek siyah beyaz. », « Kuş mavi ve sarı. ».
4. **La découverte** : « Kedi evde yaşar. Et yer. » (sans sujet dans la seconde phrase).

## Lot heure, 16 nov. : « L'heure et les dates »

Thème neuf. Ses phrases traduites sont fabriquées par `visuel/prototype/heure/dire.js` (une heure, une date ou un rendez-vous → la phrase, par la même règle que la langue apprise) ; l'heure y est en chiffres, à la manière de la langue. Tout se voit d'un coup dans `visuel/heure/banc.md` (`node tests/heure_banc.js`). À relire :

1. **Le suffixe de l'heure** : « Yoga dersi pazartesi saat 9.00'da. », « Konser saat 13.30'da başlıyor. », « Parti saat 20.00'de başlıyor. » — le suffixe suit le dernier nombre prononcé (dokuz → 'da, otuz → 'da, yirmi → 'de).
2. **Les jours** en minuscules hors d'une date : « Bugün salı. », « Dün pazartesiydi. », « Dün pazardı. ».
3. **Les mois** : « Doğum günüm 3 Mayıs'ta. », « Doğum günüm mayısta. », « Nisandan sonra mayıs gelir. », « Hazirandan önce mayıs gelir. ».
4. **Midi, minuit, l'agenda** : « Şu an öğle vakti. », « Şu an gece yarısı. », « Yoga dersi pazartesi günü. », « Yoga dersi saat 9.00 ile 11.00 arasında. », « Yoga dersi iki saat sürüyor. ».

## Lot 14, 16 nov. : « En ville : s'orienter »

La page traduit maintenant ses phrases (demander s'il y a un lieu, comment y aller, où il est, les itinéraires et les gestes au carrefour) et le groupe choisi : elles sont refaites par la grammaire de chaque langue dans `visuel/ciudad/langues.py`, versées dans `ciudad.json` par `ciudad.py`. Les noms des rues restent ceux du plan (Bergstraße, calle Mayor), comme en français. À relire :

1. **Les rues du plan avec leur suffixe** : « Bergstraße'de », « Bergstraße ile Lindenstraße'nin köşesinde », « Lindenstraße'yi ve Schulstraße'yi geçin ».
2. **Le vouvoiement** : « Birinci sokaktan sola dönün. », « İkinci kavşağa kadar gidin ve orada sola dönün. ».
3. **La photo** : « Burası okul. » pour « Das ist die Schule. » ; la fin « Otel sağ tarafta. », sans lieu « Sol tarafta. ».
4. **Les lieux** : « tren istasyonu », « belediye binası » (Rathaus), « karakol » (Polizei), « fırın » (Bäckerei).

## Lot 15, 16 nov. : « Le travail et l'emploi »

La page traduit maintenant ses phrases comme le français : annonces, qualités, entretien (la question puis la réponse), lettre, CV (« rubrique = traduction »), contrat, du ou Sie, l'appel où Mark se déclare malade, qui est qui et les papiers. Elles sont fabriquées par `visuel/travail/langues.py`, versées dans `travail.json` par `travail.py`. Les noms d'entreprise (Sonnenweg Reisen, Viajes Solano) restent en lettres latines, comme les rues du plan de la ville. À relire :

1. **Les titres** : « Schneider Hanım », « Lange Bey », avec le suffixe après l'apostrophe (« Başvuru Schneider Hanım'a gönderiliyor. », « Lange Bey'e ») ; la lettre « Sayın Schneider Hanım, », « Sayın Lange Bey, ».
2. **L'impersonnel des annonces** : « Haftada 40 saat çalışılıyor. », « Ayda 3.000 € kazanılıyor. », « İşe 1 Aralık'ta başlanıyor. », « Cana yakın olmak gerekiyor. ».
3. **Les qualités** : les mots de la glose du corpus, affichée sous le mot visé : dakik, güvenilir, « cana yakın » (freundlich), esnek, çalışkan, bağımsız, « derli toplu » (ordentlich), « takım çalışmasına yatkın » (teamfähig) ; « Dakik ve güvenilir biriyim. ».
4. **Du / Sie** : « Pazartesi başlayabilir misiniz? » / « Bana biraz yardım edebilir misin? », « Nerelisiniz? » / « Nerelisin? » ; « Bu ön yazı. » pour l'Anschreiben.
