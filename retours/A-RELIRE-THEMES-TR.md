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
