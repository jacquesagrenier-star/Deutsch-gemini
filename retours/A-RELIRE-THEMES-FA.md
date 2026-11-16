# Les thèmes illustrés en persan : ce qu'un locuteur natif devrait relire

## Lot 2, 15 nov. : « La famille d'Anna »

Pour qui apprend l'allemand avec l'interface en persan, la page de la famille montre désormais la phrase entière
traduite (« پتر پدر آنا است. »), au lieu du seul mot du corpus. La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia fa`. Il n'y a pas eu de relecture native.

1. **Les noms** : هاینتس, گیزلا, پتر (Peter à l'allemande), مونیکا, زابینه, فرانک, یان, کاترین, آنا, لنا, فلیکس,
   سوفی, بن, میا (comme dans les pages du telc).
2. **L'ezafe** n'est écrite qu'après ا / و (« عموی آنا ») et après le h muet (« عمهٔ آنا »).
3. **Le côté de l'oncle et de la tante, lu dans l'arbre** : Sabine est la عمه d'Anna, Frank son شوهرعمه ; Peter est
   le دایی de Felix et Sophie, Monika leur زن‌دایی ; les cousins پسرعمه / دخترعمه (Felix et Sophie pour Anna),
   پسردایی / دختردایی (Jan, Anna, Lena pour Felix).
4. **Le neveu** : برادرزاده (l'enfant du frère), خواهرزاده (l'enfant de la sœur) ; pour Frank et Monika, du côté du
   conjoint, le même mot (« برادرزادهٔ همسر » serait plus exact : à trancher).
5. **Les beaux-parents et beaux-frères** : پدرشوهر / مادرشوهر (Monika, Katrin), پدرزن / مادرزن (Frank) ;
   شوهرخواهر, برادرزن, زن‌برادر, خواهرشوهر.
6. **« همسر »** pour l'épouse, « شوهر » pour le mari ; « آیا … توست؟ » pour la question ; les chiffres latins de l'âge
   (« او 61 سال دارد »), comme les autres pages.
7. **Les paires** avec la flèche « ← » (de droite à gauche).

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **komisch** : « غریب » (la théière, le bruit), **seltsam** : « عجیب » (la chaise, la question), comme les gloses.
2. **gut** pour le gâteau : « کیک خوشمزه است » ; **Abend** : « شب » (« این یک شب دل‌انگیز است »).
3. **L'ezafe ecrite** : « منظرهٔ دل‌انگیز », « دوچرخهٔ نو », « پنجرهٔ باز », « غذای چندش‌آور » ; ailleurs sans signe.
4. **Die Gasse ist eng und schmal** : « کوچه تنگ و باریک است ».

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js`. À relire :

1. **Bürgeramt** : « ادارهٔ امور شهروندی » ; **Krankenkasse** : « صندوق بیمهٔ درمان » ; **Praxis** : « مطب ».
2. **Le guichet** : « لطفاً … » (« لطفاً فرم را پر کنید. »).
3. **L'heure** en chiffres latins : « ساعت 15:00 » (comme les autres pages).
4. **Les noms** : مارک گارنیه, مونترال, برلین, « گارتن‌اشتراسه، پلاک 12 » ; « نام مارک مارک است. » (le prénom de Mark est Mark).

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js`. À relire :

1. **Kita / Kindergarten / Grundschule** : « مهدکودک », « کودکستان », « دبستان ».
2. **Anna**, tante paternelle de Mia : « عمه‌اش » ; « کاترین, مادرش » garde la virgule latine de la page (à remplacer par « ، » ?).
3. **L'emploi du temps** : « دوشنبه، زنگ سوم، بن ریاضی دارد ».
4. **La date** : « روز 28 دسامبر، بن در تعطیلات است » (mois du calendrier grégorien).

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js`. À relire :

1. **Les prénoms** : آنا، لنا، فلیکس، سوفی، یان، کاترین، گیزلا، هاینتس.
2. **L'invitation** : « مهمانی » pour die Party, « جشن » pour die Feier, « ناهار » pour le repas de Noël des grands-parents.
3. **Le défini avec « را »** : « مارک کیک را می‌آورد » / l'indéfini « مارک یک کیک می‌آورد ».
4. **Le souhait de la fête des Mères** : « روز مادر مبارک، مامان! ».

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js`. À relire :

1. **Le magasin** : « در نانوایی / به نانوایی / از نانوایی » ; Kiosk « دکهٔ روزنامه‌فروشی », Drogerie « فروشگاه لوازم بهداشتی ».
2. **Le prix** : « قیمت کره 1,29 € است » ; comparer « کره از پنیر گران‌تر است ».
3. **La commande** : « یک نان می‌خواهم » ; la monnaie « 0,80 € باقی پول می‌گیرد ».
4. **Le dialogue** : « چه میل دارید؟ », « نفر بعدی، لطفاً! ».

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js`. À relire :

1. **Une forme par personne** : « چمدانم را بستم / چمدانت را بستی / چمدان‌هایمان را بستیم / آنا چمدانش را بست ».
2. **La famille au singulier, Ben et Mia au pluriel** : « خانواده … رفت », « بن و میا … ساختند ».
3. **La chambre** : « یک اتاق یک‌تخته / دوتخته برای دو شب ».
4. **Mark au port** : « با قایق در بندر گشت زد ».

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js`. À relire :

1. **Le subjonctif après « دوست دارد »** : « روزا دوست دارد فوتبال بازی کند », pluriel « دوست دارند … کنند ».
2. **Proposer** : « دوست داری فوتبال بازی کنی؟ », « با هم فوتبال بازی کنیم؟ ».
3. **Les verbes** : گیتار زدن، عکس گرفتن، آواز خواندن، رقصیدن، دویدن.

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js`. À relire :

1. **Le « را » de l'aliment** : « آنا کیک را خیلی دوست دارد ».
2. **Goûter** : « آنا چیزی شیرین می‌چشد ».
3. **Le café** : « مرد موجوگندمی پیشخدمت است », « زن موفرفری » ; « لطفاً منو را بیاورید ».
4. **La quantité** : « یک کیلو پرتقال », « کمی شکر » ; la liste « 1 کیلو گوجه‌فرنگی ».

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **Le métier** : « دیه‌گو پزشک است. » ; avec l'adjectif « پزشک خوبی است », « نانوای خوبی است » (le « ی » après la voyelle finale).
2. **« travaille comme »** : « به‌عنوان پزشک کار می‌کند ».
3. **Un seul mot pour les deux sexes** : la paire dit « پزشک مرد → پزشک زن ».
4. **Le lieu** : « در پلیس کار می‌کند » pour « bei der Polizei ».

## Lot 12, 16 nov. : « La météo et les saisons »

La page traduit maintenant ses phrases (le temps qu'il fait, les activités de chaque saison, « j'ai froid », les mois et les degrés) : elles sont écrites dans `visuel/meteo/langues.py` et versées dans `meteo.json` par `meteo.py`. À relire :

1. **« ماه مه »** pour le mois de mai, jamais « مه » seul : c'est aussi le brouillard, dans un thème sur la météo.
2. **heiß et warm** : « هوا خیلی گرم است. » (heiß) et « هوا گرم است. » (warm).
3. **« سردم است. »** / « گرمم است. » pour « Mir ist kalt / heiß » ; « باد می‌وزد. » pour « Es ist windig. ».
4. **Les degrés** en chiffres latins comme les prix des autres thèmes : « دما منفی 12 درجه است. ».

## Lot 13, 16 nov. : « Les animaux »

La page traduit maintenant ses phrases (c'est un…, le pluriel, où il vit, ce qu'il mange, sa couleur, plus grand / plus petit que, la phrase de la découverte) et le lieu ou la couleur choisis : elles sont refaites par la grammaire de chaque langue dans `visuel/animales/langues.py`, versées dans `animales.json` par `animales.py`. À relire :

1. **Le singulier après un nombre** : « یک اسب، دو اسب ».
2. **La comparaison** : « سنجاب از خرس کوچک‌تر است. ».
3. **L'ezafe** : « این یک گربهٔ سیاه و سفید است. ».
4. **La découverte sans sujet** : « گربه در خانه زندگی می‌کند. گوشت می‌خورد. » ; « ماهی قرمز نارنجی است. » (le poisson rouge est orange, comme en français).

## Lot heure, 16 nov. : « L'heure et les dates »

Thème neuf. Ses phrases traduites sont fabriquées par `visuel/prototype/heure/dire.js` (une heure, une date ou un rendez-vous → la phrase, par la même règle que la langue apprise) ; l'heure y est en chiffres, à la manière de la langue. Tout se voit d'un coup dans `visuel/heure/banc.md` (`node tests/heure_banc.js`). À relire :

1. **Les chiffres persans** pour l'heure et la date : « ساعت ۱۴:۳۰ است. », « امروز ۳ مه است. ».
2. **Le week-end** : « شنبه و یکشنبه تعطیلات آخر هفته‌اند. » traduit l'allemand (en Iran, le week-end est le vendredi) ; la tournure est-elle claire ?
3. **Les mois grégoriens** : ژانویه، فوریه … دسامبر ; « بعد از آوریل، مه می‌آید. ».
4. **L'agenda** : « کلاس یوگا دوشنبه ساعت ۹:۰۰ است. », « کلاس یوگا دو ساعت طول می‌کشد. », « وقت دکتر » pour le rendez-vous chez le médecin.
