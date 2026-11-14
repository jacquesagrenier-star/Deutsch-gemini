# Wortando Pflege : phase 1, l'architecture (14 nov. 2026)

La section Soins existe dans l'app, **en essai admin**, ouverte compte par compte (décision de Jacques
du 14 nov.). Elle porte un premier thème de 31 mots. Rien ne change pour un compte sans l'essai.

## Ce qui est en place

| Morceau | Où | Ce qu'il fait |
|---|---|---|
| L'essai | `ESSAIS.soins` (`etat: "admin"`, `compte: "soins"`) dans `index.html` | allumé pour l'admin, et pour un compte dont `users/<uid>.essais` contient « soins » (mécanisme existant, `essaiActif`) |
| La garde | `soinsActifs()` | essai allumé **et** allemand appris ; tout le reste passe par elle |
| L'ouverture | bouton **« OUVRIR SOINS »** sur les lignes allemandes du tableau de bord admin | `basculerEssaiCompte(uid, "soins", …)`, la fonction déjà utilisée pour l'anglais et les examens ; **aucune règle Firestore à changer** (`essais` est déjà une clé réservée) |
| La tuile | « Soins » dans Tout le contenu, à côté de la préparation aux examens (`#tuileSoins`, `data-orbid="pflege"`, `orb-de`) | cachée sauf essai (`majTuileSoins`, appelée par `updateVhsKapitelTileVisibility`) ; jamais en espagnol, absente des listes blanches ja / en / pt |
| L'écran | `#soinsListe` | les thèmes des Soins, un rang de pastilles A2 / B1 / B2 avec « sus / total », qui ouvre les cartes (`startTheme`, retour à l'écran Soins) |
| Les données | `pflege/datos/themes.json`, **dérivé** de `pflege/sources/*.py` par `python pflege/outils/construire.py` | même format que `themes.json`, lu par la **même** fonction (`rangsDuMotDeTheme`, sortie de `loadThemesJson` sans changer une ligne) ; ids `soins_<thème>_<niveau>` |
| L'isolement | `themesSoins`, à part de `themes` | ni les pourcentages, ni les niveaux, ni `paquetDuNiveau` ne voient les Soins ; `themeParId` les trouve |
| La séance du jour | `ajouterSoinsASeance`, `melerNeufsSoins` | pour un compte ouvert : les mots de soins du niveau rejoignent le neuf, ceux déjà commencés reviennent à leur échéance ; **deux mots neufs sur trois** viennent des Soins tant qu'il en reste |
| Le site publié | `publication/construire_site.py` | `pflege/datos/` dans la liste blanche (sinon 404 en ligne) |
| Le contrôle | `python tests/pflege.py` | fichier dérivé à jour, ids, genre, pluriel, 9 traductions et 9 exemples, aucun chiffre dans un exemple, aucun doublon ; avertit d'un mot déjà au corpus |

**Le préfixe `soins_`, pas `pflege_`** : le corpus a déjà un thème `pflege_betreuung_c1` (« Pflege und
Betreuung », C1). Avec `pflege_`, ses mots auraient été pris pour des mots des Soins dans le mélange de
la séance. Trouvé à l'essai au navigateur, corrigé avant le commit.

## Le premier thème

« Vitalzeichen und Krankenbeobachtung » (les signes vitaux et la surveillance) : **31 noms**, A2 6,
B1 15, B2 10, tous absents du corpus général ; traductions et phrases d'exemple dans les 9 langues ;
5 points marqués ⚕️ pour l'infirmière (champ `relire`). Source : `pflege/sources/vitalzeichen.py`.

## Comment l'essayer

- **Jacques (admin)** : la tuile « Soins » apparaît dans Tout le contenu dès la version publiée.
- **Un autre compte** : tableau de bord admin → la ligne du compte → « OUVRIR SOINS ».
- **En local, sans compte** : servir le dossier, ouvrir `index.html?v=NNN`, puis dans la console
  `ESSAIS.soins.etat = "tous"; majTuileSoins(); ouvrirSoins();`.

## Vérifié

- Navigateur (local, sans compte) : sans l'essai, la tuile est cachée et `soinsActifs()` faux ; avec
  l'essai, la tuile paraît, l'écran liste le thème (A2 0/6, B1 0/15, B2 0/10), une pastille ouvre les
  cartes (« das Vitalzeichen », pluriel, traduction, exemple) et le retour mène à l'écran Soins ; aucun
  thème `soins_` dans `themes` ; le mélange donne bien deux mots de soins pour un mot général, et
  `pflege_betreuung_c1` reste un thème du corpus.
- `node tests/syntaxe.js` : OK. `python tests/pflege.py` : OK.
- `python tests/verifier.py` : ses seules erreurs sont celles d'un worktree sans les fichiers de voix
  (73 « sans voix d'Aurora », les voix espagnoles de la prononciation, `audio/manifest.json`) : aucune
  ne touche ce changement.
- Parcours `de` et `es-moteur` contre `de-v1189` / `es-v1189` : voir le bilan au chef.

## Ce que la phase 2 doit trancher

1. **Les verbes, adjectifs et expressions** des thèmes (*messen*, *erhöht*, « 130 zu 85 ») : le format
   des thèmes du corpus ne porte les traductions de ses `verben` et `adjektive` qu'en français et en
   anglais. Options : passer par `verbe.json` / `adjectif.json` (et leurs 9 langues), ou un format
   propre aux Soins. Je propose la première.
2. **Les mots déjà au corpus** (*der Blutdruck*, *der Puls*…) : les relier à leur fiche au lieu de les
   doubler (une progression par mot).
3. **Les textes de l'écran en 11 blocs d'I18N** (aujourd'hui en français, comme tout essai).
4. **Les voix** : aujourd'hui la voix du téléphone ; le lot ElevenLabs v2 des Soins sera annoncé au chef
   avec son coût avant d'être lancé.
5. **Le mode nuit** : les trois petits textes de l'écran Soins suivent la règle de nuit de
   `.theme-count` (même couleur claire) ; à mesurer avec `tests/audit-contraste.js` quand l'écran aura
   ses textes définitifs.
