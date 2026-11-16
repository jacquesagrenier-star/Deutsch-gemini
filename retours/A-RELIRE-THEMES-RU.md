# Les thèmes illustrés en russe : ce qu'un locuteur natif devrait relire

14 nov. 2026, lot 1 de l'alignement des thèmes (« Où est le chat ? » et « La journée »). Pour qui apprend l'allemand
avec l'interface en russe, la page montre désormais la phrase entière traduite, comme en français, en anglais et en
portugais. Il n'y a pas eu de relecture native. Une rétro-traduction à l'aveugle (vers le français, sans l'allemand)
n'a trouvé aucune faute.

- Les traductions ne sont pas écrites phrase par phrase : on traduit les morceaux que la page assemble.
  - « Où est le chat ? » : `visuel/gato/langues.py`, tables `RU` et `RU_PL` (les six cas de 16 noms), `lieu()` (la
    préposition selon « où » ou « vers où »), `POSTURE`, `MOUVEMENT`, `PHRASES`. On corrige là, puis
    `python visuel/gato/gato.py --json`.
  - « La journée » : `visuel/journee/langues.py`, `VERBES` (19 verbes aux cinq personnes), `SUJETS`, `FREQUENCES`.
    On corrige là, puis `python visuel/journee/journee.py --json`. L'heure (« в 7:15 ») et les mots de liaison
    (« Сначала… Потом… ») sont dans `visuel/prototype/journee.html` (`heureTrad`, `LIENS_TR`).
- Contrôle à l'écran : `python visuel/langues_themes.py verifier gato journee ru` (navigateur, verrou des parcours).

## Ce que le russe fait, et qui est voulu

Le russe distingue « où » et « vers où » comme l'allemand : на столе / на стол (auf dem / auf den Tisch), под
столом / под стол, в корзине / в корзину, за диваном / за диван. Le groupe allemand du mauvais choix est traduit
avec son cas : l'élève voit la différence qu'il a manquée. Après перед, рядом с, между, la forme est la même pour les
deux : seul le verbe change (сидит / садится).

## Points à confirmer

1. **« ans Fenster » → « садится у окна »**. « к окну » marquerait la direction, mais « садится к окну » sonne mal.
   Dans les groupes isolés, « am Fenster » = « у окна » et « ans Fenster » = « к окну ».
2. **« im Regal » → « на полке стеллажа »** (« лежит / прыгает на полку стеллажа ») : « в стеллаже » est rare.
   C'est le seul groupe à deux noms.
3. **« über » + accusatif → « через »** (« прыгает через коробку ») ; « über » + datif → « над ».
4. **« läuft hinter das Sofa » → « заходит за диван »**, « kriecht unter » → « залезает под », « klettert auf »
   → « забирается на ».
5. **Les noms** : Мориц, Мия (Мии, Мию, Мией), Катрин, Ян — comme dans les textes de la page.
6. **« kocht » → « готовит »**, sans complément.
7. **« Ben setzt die Katze auf den Tisch » → « Бен сажает кота на стол »**.

## Ajouté le 15 nov. (revue des traductions)

- **« Décrire une personne » : « glatt » (des cheveux) → « прямые (волосы) »**, au lieu de la glose du corpus (lisse, glissant).
  Elle vit dans `visuel/familia/gloses.py`, `SENS_CHEVEUX` ; on corrige là, puis `python visuel/familia/gloses.py`.

## Lot 2, 15 nov. : « La famille d'Anna »

La page fabrique la traduction avec les mêmes choix que la phrase allemande (les mêmes personnes, le même lien, le même possessif) : on corrige dans `visuel/prototype/familia/langues.js`, pas phrase par phrase. Contrôle à l'écran : `python visuel/langues_themes.py verifier familia ru`. Il n'y a pas eu de relecture native.

1. **Les noms** : Хайнц, Гизела, Петер, Моника, Сабина (Sabine), Франк, Ян, Катрин et Софи (indéclinables), Анна,
   Лена, Феликс, Бен, Мия ; génitif (« отец Анны ») et accusatif après спрашивать (« спрашивает Бена »).
2. **Les beaux-parents selon le conjoint** : свёкор / свекровь pour la femme (Monika, Katrin), тесть / тёща pour le
   mari (Frank). Dans les paires sans personne : « тесть, свёкор → тёща, свекровь ».
3. **Les beaux-frères et belles-sœurs, lus dans l'arbre** : зять (le mari de la sœur : Frank pour Peter), шурин (le
   frère de la femme : Peter pour Frank), невестка (la femme du frère : Katrin pour Anna, Monika pour Sabine), золовка
   (la sœur du mari : Sabine pour Monika, Anna pour Katrin). Sont-ils encore compris, ou faut-il « муж сестры »,
   « брат жены » ?
4. **« мои сын и дочери »**, « мои двоюродный брат и двоюродные сёстры » : le possessif au pluriel devant des mots au
   singulier et au pluriel.
5. **Le point après la citation** : « Анна говорит: «Петер — мой отец». » ; rien après « ? ».
