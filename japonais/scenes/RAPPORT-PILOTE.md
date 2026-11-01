# Scènes de Camille — rapport du pilote (31 oct. 2026)

> Pour Jacques. Tout le japonais est un **brouillon** : il attend un natif.
> Planche des quatre images : `.claude/planche-scenes-camille-pilote.jpg`
> (dossier OneDrive du projet).

## Ce qui est fait

1. **La bible** : `japonais/scenes/HISTOIRE-CAMILLE.md` — Camille, les gens
   autour d'elle (ce que chacun a qui n'appartient qu'à lui), le niveau saison
   par saison (N5 → N3), les 35 scènes avec leur moment, leur lieu et le faux
   pas de Camille qui sert de ressort.
2. **Les 32 prompts manquants** (`visuel/scenes/<nom>.prompt.txt`), sur le
   modèle des prototypes : photo réelle, 9:16, bandes, « every surface is
   plain », aucune négation. **Les 32 passent `verifier_prompt.py` à 0 faute.**
   Camille entre toujours par ses images (`japonais/scenes/references.json` dit
   lesquelles, scène par scène).
3. **Les mots** : `japonais/scenes/mots-prevus.json` liste les objets de chaque
   scène, contrôlés contre le corpus N5-N3 par `verifier_mots.py` (0 faute).
4. **Le pilote payé** : une prise pour les scènes 1, 5, 6 et 7, Camille en
   référence. Puis zones (grille de 2,5 %), masques SAM 2 et lexique, comme les
   prototypes :

| Scène | Zones | Mots | Hors corpus | Remarques |
|---|---|---|---|---|
| 1 `kuukou` — 空港で | 31 | 36 | 0 | Camille reconnaissable, plan et journal en faux texte illisible ; l'avion vole au lieu d'être au sol |
| 5 `heya` — 部屋で | 34 | 40 | 0 | La photo encadrée montre deux visages asiatiques : sa mère est québécoise (détail, à reprendre si tu y tiens) |
| 6 `kuyakusho` — 区役所で | 36 | 39 | 1 (窓口) | La prise portait un **passeport japonais** (« JAPAN », chrysanthème) : repeint en bleu marine uni, en local et gratuit (`retoucher_kuyakusho.py`) ; le prompt est corrigé |
| 7 `hanami` — 花見 | 41 | 37 | 1 (レジャーシート) | Trois collègues au lieu de quatre ; l'appareil photo est posé sur la bâche |

Les masques ont été regardés sur un rendu des tracés : ils collent à leur
objet ; quelques bords approximatifs (l'escalator, le sac du vieux monsieur à
l'aéroport). ⚠️ **Rien n'a été essayé au doigt dans l'app** : les scènes ne
sont pas branchées (`construire_scenes.py` ne connaît que konbini, eki et
genkan), et rien n'a été publié.

## Coût

**0,60 $** (4 images à 0,15 $, une prise chacune, aucune reprise). Rien d'autre
n'a été payé.

## Ce qu'il faut décider

1. **Le style te convient-il ?** Si oui, les 28 autres images coûtent
   28 × 0,15 = **4,20 $**, plus 1 à 2 $ de reprises probables.
2. **Les visages des personnages qui reviennent** : Yui, Fumiko, Hiroshi,
   M. Sakamoto, Mme Kimura n'ont pas encore d'image. Sans elle, ils changeraient
   de visage d'une scène à l'autre (règle `personne-sans-reference`). Les faire
   comme Camille : environ **3 $** pour les cinq. Sans attendre ce choix, huit
   scènes n'ont besoin que de Camille (8, 9, 11, 12, 13, 16, 23, 28) :
   **1,20 $**.
3. **137 mots hors du corpus N5-N3** (`python japonais/scenes/verifier_mots.py`
   les liste) : le corpus n'a ni les objets du Japon (portique rouge, lanternes,
   yukata, kotatsu, ramen, feux d'artifice…) ni la plupart des fruits et
   légumes. Les ajouter au corpus japonais comme « vocabulaire des scènes »,
   comme on l'a fait en allemand ? Sinon, ces objets restent dans l'image sans
   zone.
4. **La scène 35** : qui arrive (proposé : un nouvel élève étranger du cours,
   que Camille accueille en japonais poli ; ou sa mère, ou Mark ?), et Camille
   rentre-t-elle à Montréal ou reste-t-elle ?
5. **Les trois prototypes** (eki, konbini, genkan) datent d'avant Camille : les
   garder tels quels, ou les refaire avec elle (0,45 $ et des zones à
   remesurer) ?
6. **Ce que j'ai proposé dans la bible** et que tu n'as pas décidé : les
   prénoms (Sylvie, Keiko, Daichi, Kenta, Lucas, Linh), le japonais de Kanazawa
   que Camille tient de son père, son ancien métier de barista, le carnet
   rouge et l'appareil photo de son père.

## L'humour (ajouté le 31 oct., à ta demande)

Chaque scène a maintenant un gag, montré dans l'image et pas seulement
raconté, plus six gags qui reviennent au fil de l'année (la révérence,
l'appareil photo du père, trop grand ou trop petit…) : bible, section
3 bis, et une ligne **Gag** sous chaque scène. Les 25 prompts qui n'en avaient
pas l'ont reçu ; les 32 passent toujours le vérificateur à 0 faute. Les quatre
images du pilote ne changent pas : leur gag passe par les questions. Coût : 0 $.

## Ce qui reste, une fois tes choix faits

- Générer, mesurer, détourer les scènes restantes (même méthode).
- Brancher les scènes dans l'app (essai admin japonais) : ajouter les noms à
  `construire_scenes.py`, les mots au corpus.
- Écrire les couches N4 et N3 (les questions), pour le japonais — elles ne se
  traduisent pas des autres langues.
- Faire relire le japonais par un natif.
