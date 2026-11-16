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
