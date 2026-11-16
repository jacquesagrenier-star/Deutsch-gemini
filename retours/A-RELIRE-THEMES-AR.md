# Les thèmes illustrés en arabe : ce qu'un locuteur natif devrait relire

## Lot 2, 15 nov. : « La famille d'Anna »

Pour qui apprend l'allemand (et l'espagnol) avec l'interface en arabe, la page de la famille montre désormais la
phrase entière traduite (« بيتر هو والد آنا. »), au lieu du seul mot du corpus. La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia ar`. Il n'y a pas eu de relecture native.

1. **Les noms** : هاينتس, غيزيلا, بيتر, مونيكا, زابينه, فرانك, يان, كاترين, آنا, لينا, فيليكس, صوفي, بن, ميا.
2. **والد / والدة** plutôt que أب / أم ; **أخو آنا**, **أخي, أخوك, أخوه** ; devant un prénom dans un mot composé,
   **شقيق** (« ابن شقيق آنا », « زوجة شقيق آنا ») pour ne pas écrire « ابن أخي آنا », mais « ابن أخي », « زوجة أخيك »
   avec un pronom.
3. **Le côté de l'oncle et du cousin, lu dans l'arbre** : عمة / زوج عمة pour Anna, خال / زوجة خال pour Felix ;
   ابن عمة / ابنة عمة, ابن خال / ابنتا خال.
4. **Le neveu** : ابن أخ / ابن أخت ; pour Frank et Monika, du côté du conjoint, le même mot (« ابن أخي زوجتي » serait
   plus exact : à trancher).
5. **Les beaux-parents** décrits : والد زوجي / والدة زوجي (Monika, Katrin), والد زوجتي (Frank) ; صهر et كنّة pour le
   gendre et la belle-fille ; زوج أختي, شقيق زوجتي, زوجة أخي, شقيقة زوجي pour les beaux-frères et belles-sœurs.
6. **Le duel** : « أختا يان », « أختاي », « عمتان », « ابنتا خال », « لديهما حفيدان وثلاث حفيدات » (le nombre au genre
   inverse) ; « والداي » pour « mes parents ».
7. **L'âge** : « عمره 61 سنة », « عمرها 7 سنوات » (chiffres latins, comme les autres pages).
8. **Les paires** avec la flèche « ← » ; le mot général avec l'article (« العم، الخال ← العمة، الخالة »).

## Lot 3, 16 nov. : « Les contraires »

La page traduit maintenant chaque phrase (58 en allemand appris, 49 en espagnol appris), écrite à la main dans `visuel/contrarios/langues.py`, à côté du français, de l'anglais et du portugais. À relire :

1. **komisch** : « غريب » (الإبريق، الصوت), **seltsam** : « عجيب » (الكرسي، السؤال، الوضع), pour garder deux mots.
2. **Die Gasse ist eng und schmal** : « الزقاق ضيّق ومحصور » (à relire : « eng » et « schmal » n'ont qu'un mot naturel).
3. **gut** pour le gâteau et la soupe : « لذيذة » ; **schlecht** pour la pomme et le lait : « فاسدة / فاسد ».
4. **L'accord du demonstratif** : « هذه مزهرية », « هذه حقيبة », « هذا كوب ».
5. **Pour qui apprend l'espagnol** (49 phrases) : « المنتزه كبير » (el parque), « المبنى قبيح إلى حدٍّ ما » (bastante feo).

## Lot 4, 16 nov. : « Les démarches »

La page assemble maintenant ses phrases traduites (les démarches de Mark, la phrase polie du guichet, les documents, les avis, les heures d'ouverture, le rendez-vous, les champs du formulaire) à partir de morceaux posés dans `visuel/prototype/demarches/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Bürgeramt** : « مكتب خدمات المواطنين » ; pour l'espagnol, **la oficina** : « مكتب البلدية ».
2. **Le guichet** au style administratif : « يُرجى … » (« يُرجى ملء الاستمارة. »), plutôt qu'un impératif.
3. **L'avis** : « لفتح حساب، تحتاج إلى جواز السفر. » (« tu as besoin de »), qui évite d'accorder « يلزم » avec le document.
4. **Les heures** : « مكتب خدمات المواطنين مغلق يوم الأربعاء في الساعة 15:00. » (le lieu d'abord, l'adjectif accordé : العيادة مفتوحة).
5. **Les noms** : مارك غارنييه, مونتريال, برلين, « غارتن شتراسه 12 » ; pour l'espagnol « شارع لا لونا 12، الطابق 2، الشقة B ».

## Lot 5, 16 nov. : « L'école et la garderie »

La page assemble maintenant ses phrases traduites (les fournitures comptées, où vont Ben et Mia, le mot d'absence, la réunion de parents, les vacances, qui va chercher Mia, l'emploi du temps) à partir de morceaux posés dans `visuel/prototype/ecole/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le nombre** : « دفترين », « ثلاثة دفاتر », « ثلاث مساطر » (accord inversé du nombre) ; « مماحٍ » pour les gommes.
2. **Le verbe accordé avec qui va chercher Mia** : « تصطحب كاترين / آنا », « يصطحب يان / مارك ».
3. **Les mois** : « يناير … ديسمبر » (et non « كانون الثاني … ») ; « في 28 ديسمبر، يكون بن في العطلة ».
4. **Pour qui apprend l'espagnol** : la matière « Lengua » est « الإسبانية » ; « ترسم ميا في الحضانة ».
