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
