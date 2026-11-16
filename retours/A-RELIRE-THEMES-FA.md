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
