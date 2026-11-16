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

## Lot 6, 16 nov. : « Fêtes et invitations »

La page assemble maintenant ses phrases traduites (la fête et sa date, le souhait, qui apporte quoi, la réponse selon l'agenda, la contre-proposition, l'ordre des mots, la carte d'invitation) à partir de morceaux posés dans `visuel/prototype/fetes/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le verbe accordé avec qui agit** : « تدعو / يدعو », « تُحضر آنا / يُحضر مارك », « تبدأ الحفلة / يبدأ الغداء ».
2. **Le souhait de Silvester** : « كل عام وأنتم بخير! » ; Neujahr « سنة سعيدة! ».
3. **Le délai** : « على آنا أن ترد قبل يوم الأربعاء » (« avant » mercredi, pour « bis Mittwoch »).
4. **Pour qui apprend l'espagnol** : « عيد الملوك المجوس » (Día de Reyes), « أسبوع الآلام » (Semana Santa), « يوم الموتى (في المكسيك) ».

## Lot 7, 16 nov. : « Faire les courses »

La page assemble maintenant ses phrases traduites (où acheter quoi, qui est où, le dialogue au comptoir, les prix, comparer, la monnaie rendue, commander, les emballages) à partir de morceaux posés dans `visuel/prototype/courses/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le verbe accordé avec Mark ou Anna** : « يشتري / تشتري », « يدفع / تدفع » ; « يقول البائع / تقول البائعة ».
2. **Le prix** : « سعر الزبدة 1,29 € » ; comparer « الزبدة أغلى من الجبن » (comparatif invariable).
3. **Metzgerei** : « الملحمة » ; Drogerie « متجر مواد التجميل والتنظيف » (à relire).
4. **Pour qui apprend l'espagnol** : le jambon de la boucherie, « الجامون ».

## Lot 8, 16 nov. : « Les vacances et le voyage »

La page raconte maintenant chaque étape des voyages dans la langue, à la personne que pose la question (je, tu, nous ou le sujet de l'étape), et la suite d'un voyage, la météo, les objets, la chambre réservée ; tout est dans `visuel/prototype/vacances/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le verbe avant le sujet et accordé** : « حزمت آنا », « حزم مارك », « ذهبت العائلة » ; Ben et Mia « بنى بن وميا » (verbe au singulier devant le sujet).
2. **Le sujet sous-entendu dans une suite** : « ثم ذهبت إلى المطار », et le duel pour Ben et Mia : « ثم سبحا في البحر ».
3. **Je et tu** distingués par la voyelle : « حزمتُ / حزمتَ » (le tu au masculin).
4. **Les nuits** : « لليلة واحدة / لليلتين / لخمس ليالٍ » ; Málaga « مالقة ».

## Lot 9, 16 nov. : « Les loisirs »

La page traduit maintenant ses phrases (qui fait quoi, qui aime quoi, à quelle fréquence, proposer une sortie et répondre) avec les formes de chaque activité, posées dans `visuel/prototype/loisirs/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le verbe devant le sujet, accordé** : « تلعب روزا كرة القدم », « يلعب فيليكس » ; à deux, au singulier devant les sujets (« يحب فيليكس وروزا »).
2. **Aimer + nom verbal** : « تحب روزا لعب كرة القدم », « أحب الرقص كثيرًا ».
3. **Jamais** : « لا يلعب فيليكس كرة القدم أبدًا » ; proposer « هل تريد أن تلعب …؟ », « هل نلعب … معًا؟ ».

## Lot 10, 16 nov. : « Manger et goûter »

La page traduit maintenant ses phrases (les goûts, ce qu'on dit en goûtant, les saveurs, les quantités, la liste de courses, le café, la commande et l'addition) par `visuel/prototype/manger/langues.js` (et pour qui apprend l'espagnol). À relire :

1. **Le verbe accordé à qui aime ou goûte** : « تعشق آنا الكعكة », « يحب مارك … », « تتذوّق آنا شيئًا حلوًا ».
2. **La commande** : « تطلب كارمن قهوة وكوبين من الشاي. المبلغ 6,90 € » (le duel des boissons).
3. **Les figurants** : « الرجل ذو الشعر الرمادي هو النادل », « المرأة ذات الشعر المجعد هي النادلة ».
4. **Pour qui apprend l'espagnol** : le jambon de la liste, « لحم مقدد ».

## Lot 11, 16 nov. : « Les métiers »

La page traduit maintenant ses phrases (le métier, « je suis … », où chacun travaille, ce qu'il fait, « travaille comme … », le masculin et le féminin) : elles sont fabriquées par `visuel/metiers/langues.py` dans `metiers.json`. À relire :

1. **Le verbe d'abord, accordé** : « يعمل دييغو في عيادة. », « تعمل إينيس في صالون تصفيف الشعر. » ; avec le pronom seul, « تعمل في عيادة. ».
2. **L'accusatif d'état** : « يعمل طبيبًا », « تعمل طبيبةً », « يعمل موظّفَ استقبال ».
3. **Coiffeur / coiffeuse** : « حلّاق » / « مصفّفة شعر » (les deux gloses du corpus).
4. **Pour qui apprend l'espagnol** : « Soy policía. » et « Es policía. » se disent pour Elena comme pour Tomás ; l'arabe garde le masculin (« أنا شرطي. »), comme le français (« Je suis policier. »). « en la comisaría » : « في مركز الشرطة ».

## Lot 12, 16 nov. : « La météo et les saisons »

La page traduit maintenant ses phrases (le temps qu'il fait, les activités de chaque saison, « j'ai froid », les mois et les degrés) : elles sont écrites dans `visuel/meteo/langues.py` et versées dans `meteo.json` par `meteo.py`. À relire :

1. **Les degrés sans accord du nom** : « درجة الحرارة 30. », « درجة الحرارة 12 تحت الصفر. » (le chiffre seul, pour éviter l'accord de « درجة » avec le nombre).
2. **Les saisons** : « نحن في الربيع. » pour « Es ist Frühling. » / « Es primavera. ».
3. **Les mois** : « في شهر يناير، يكون الشتاء في ألمانيا. » ; pour l'espagnol, « في إسبانيا، يناير شهر من أشهر الشتاء. » (noms de mois يناير، فبراير… comme les autres thèmes).
4. **Pour qui apprend l'espagnol** : « Hace sol. » = « هناك شمس. » (il y a du soleil) et « Hace calor. » = « الجو حارّ. », distincts de « الشمس مشرقة. » et « الجو حارّ جدًا. » de l'allemand (Die Sonne scheint, Es ist heiß).

## Lot 13, 16 nov. : « Les animaux »

La page traduit maintenant ses phrases (c'est un…, le pluriel, où il vit, ce qu'il mange, sa couleur, plus grand / plus petit que, la phrase de la découverte) et le lieu ou la couleur choisis : elles sont refaites par la grammaire de chaque langue dans `visuel/animales/langues.py`, versées dans `animales.json` par `animales.py`. À relire :

1. **Le verbe d'abord, accordé** : « تعيش البقرة في المزرعة. », « يعيش الكلب في البيت. » ; au pluriel (animaux, non humains) le féminin singulier : « تعيش الكلاب في البيت. ».
2. **La poule au pluriel** : « الدجاجات » plutôt que le collectif « الدجاج » (qui est masculin : « يعيش الدجاج »).
3. **Le duel** : « بقرة واحدة، بقرتان », « سمكة ذهبية واحدة، سمكتان ذهبيتان ».
4. **Pour qui apprend l'espagnol** : les mêmes phrases (« la oveja » = « الخروف », masculin) ; la couleur choisie suit le genre espagnol de l'animal de la question (« gris|1 » = « رمادية »).

## Lot heure, 16 nov. : « L'heure et les dates »

Thème neuf. Ses phrases traduites sont fabriquées par `visuel/prototype/heure/dire.js` (une heure, une date ou un rendez-vous → la phrase, par la même règle que la langue apprise) ; l'heure y est en chiffres, à la manière de la langue. Tout se voit d'un coup dans `visuel/heure/banc.md` (`node tests/heure_banc.js`). À relire :

1. **L'heure en chiffres latins** : « الساعة 14:30. », « يوم الاثنين الساعة 9:00. ».
2. **Les mois** : يناير … ديسمبر (et non كانون الثاني …) ; « عيد ميلادي في 3 مايو. », « بعد أبريل يأتي مايو. ».
3. **L'accord du verbe** : « تبدأ الحفلة الساعة 20:00. » (féminin), « يبدأ درس اليوغا … » ; « تنتهي الحفلة عند منتصف الليل. ».
4. **Les durées à l'accusatif** : « يستغرق درس اليوغا ساعتين. », « … ساعة ونصفًا. », « … خمسًا وأربعين دقيقة. » ; et « أمس كان الاثنين. ».
