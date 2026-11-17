# Wortando Pflege : l'accueil Soins et « Ma journée au service » (plan, 16 nov. 2026)

Décisions de Jacques du 16 nov. (`decisions/DECISIONS.md`, 923aa49), maquette « Accueil Pflege »
(https://claude.ai/artifact/R5aVDYuLmfdncJj2N7uqBm) :

1. un interrupteur « Soins / Allemand général » en haut de l'accueil d'un compte Soins ;
2. la séance Soins du jour, avec deux portes, « Je commence » (A2-B1) et « Je prépare l'examen » (telc Pflege B1-B2), au
   lieu de A1-C1 : des mots du service (les dus d'abord), une paire patient / service, une abréviation, puis un dialogue
   pour finir, tirés du chapitre du jour ;
3. le contenu rangé en **14 chapitres** dans l'ordre d'une journée, chacun avec une scène, un thème illustré, des
   conversations et un écrit ;
4. le reste de Wortando dans Tout le contenu.

**Plan seulement : aucun code, aucun push, aucune dépense.** Chiffres mesurés sur la v1203 (96bc141).

## (a) La carte : ce qui existe et ce qui manque, chapitre par chapitre

Ce qui existe déjà, au total :

| Contenu | Quantité | Remarque |
|---|---|---|
| Dialogues | 26 | 12 avec leurs voix, 14 sans |
| Mots | 778, en 12 thèmes | dont 124 paires et 35 abréviations |
| Scènes | 10, soit 12 vues | |
| Cartes-phrases | 185 | 8 groupes |
| Écrits | 12 sujets | aucun écran ne les montre encore |
| Points de grammaire | 21 | |
| Thème illustré | 0 | |

Les mots sont comptés par thème de départ ; un mot peut changer de chapitre au moment du marquage (voir (c) 1).

| # | Chapitre | Scène (existe) | Conversations (existent) | Mots (thème de départ) | Cartes-phrases | Écrit (existe) | Manque |
|---|---|---|---|---|---|---|---|
| 1 | L'admission | **soins-aufnahme** | **d13** entretien d'admission, d01 se présenter | ≈ 25 (aufnahme : papiers, allergies, prothèses ; pris dans dokumentation et szenen) | patient | **4** rapports d'admission | thème illustré |
| 2 | Les soins du matin | **soins-bad**, soins-zimmer-nachttisch | d03 expliquer un soin, d04 le refus | grundpflege ≈ 50 + hygiene 48 | patient | **pflegebericht_01** (le service du matin) | thème illustré |
| 3 | Bouger et se lever | **soins-zimmer-aufstehen** | **d14** mobilisation | grundpflege (mobilisation) ≈ 20 | patient | — | thème illustré, écrit (plan de positionnement / mobilisation), 2e conversation |
| 4 | Les repas et boire | **soins-altenheim** (station à boissons, tables) | **d09** aider à manger | ernaehrung 52 | patient | — | thème illustré, écrit (protocole d'hydratation), 2e conversation |
| 5 | Les médicaments | soins-stationszimmer (armoire), soins-ambulant | **d10** à quoi sert ce comprimé, **d18** prescription floue | medikamente 63 | patient, negociation | — | thème illustré, écrit (plan de médication / message) |
| 6 | La visite du médecin | **soins-visite** | **d17** la visite | vitalzeichen 58 | visite 7 | — | thème illustré, écrit (notes de visite, ordres) |
| 7 | La douleur | soins-zimmer | **d02** la douleur de 0 à 10, d15 rassurer | koerper 69 + paires du corps (≈ 40) | patient | — | thème illustré, écrit (documentation de la douleur) |
| 8 | La relève | **soins-uebergabe** | **d06** la relève orale | dokumentation (transmissions) ≈ 30 + abréviations 35 | releve 7 | **pflegebericht_01** | thème illustré, 2e conversation |
| 9 | La documentation | soins-stationszimmer (ordinateur, Übergabeliste) | d21 presque-incident (signalement écrit) | dokumentation ≈ 55 | — | **4** rapports biographiques | thème illustré, une conversation propre (dicter, corriger une entrée) |
| 10 | Le téléphone | **soins-telefon** | **d07** SBAR, **d19** labo et pharmacie, **d23** secret professionnel, d11 se déclarer malade | (vocabulaire de l'appel, dans team et dokumentation) ≈ 20 | telephone 8, sbar 7 | — | thème illustré, écrit (note d'appel) |
| 11 | La famille du patient | (couloir : aucune ; soins-altenheim faute de mieux) | **d05** parler à la famille, **d24** plainte, **d26** fin de vie, d23 | angehoerige 48 | famille 29 | — | thème illustré, écrit (réponse à une plainte / information aux proches), scène (couloir, salon des familles) |
| 12 | L'urgence | soins-telefon (chariot d'urgence, défibrillateur) | **d16** urgence et réanimation, **d08** la chute, d12 désorienté la nuit | notfaelle 49 | — | **sturz_01** (rapport de chute) | thème illustré, scène propre (facultative) |
| 13 | La sortie du patient | soins-ambulant (le retour à la maison) | **d25** la sortie | ≈ 10 (Entlassbrief, AHB… parmi les 47 de d13-d26) | patient, famille | — | thème illustré, écrit (lettre de transfert / sortie), mots (≈ 20 de plus), 2e conversation |
| 14 | La salle de pause | **soins-pause** | **d11** échanger un poste, **d20** le tuteur, **d22** la critique | team 66 | collegues 35, negociation 14 | **nachricht_01**, **nachricht_02** | thème illustré |

En gras, ce qui appartient clairement au chapitre ; sans gras, un contenu partagé avec un autre chapitre. Les 44 mots de
« szenen » (objets des scènes) suivent la scène de leur chapitre. Les 21 points de grammaire se rattachent aux chapitres
par leurs dialogues : par exemple, g13, g19 et g20 (style des rapports) vont à la documentation, g09 (questions
indirectes) à la douleur.

**Ce qui manque, en bref :**
- les **14 thèmes illustrés** (il n'en existe aucun) ;
- **8 écrits**, pour les chapitres 3, 4, 5, 6, 7, 10, 11 et 13 ;
- **5 conversations**, pour les chapitres 3, 4, 8, 9 et 13 ;
- **une scène** pour la famille (11), et en option une scène propre pour l'urgence (12) ;
- **environ 20 mots** pour la sortie (13).

## (b) Les chapitres à rendre complets d'abord

Je retiens les chapitres qui ont déjà leur scène, au moins deux conversations et leur vocabulaire, et dont l'écrit
existe ou s'écrit en une heure :

| Rang | Chapitre | Il lui manque | Pourquoi d'abord |
|---|---|---|---|
| 1 | **7. La douleur** | thème illustré, écrit | c'est le chapitre que montre la maquette ; d02 a ses voix ; les paires du corps ; l'abréviation NRS |
| 2 | **8. La relève** | thème illustré, 2e conversation (la relève du soir, courte) | scène, d06 avec ses voix, transmissions écrites, abréviations ; c'est le cœur de l'examen |
| 3 | **1. L'admission** | thème illustré | scène, d13, d01 avec ses voix, 4 écrits |
| 4 | **10. Le téléphone** | thème illustré, écrit (note d'appel) | scène, 4 conversations dont SBAR, 15 cartes-phrases |
| 5 | **2. Les soins du matin** (si le temps le permet) | thème illustré | scène du bain, d03 et d04 avec leurs voix, 98 mots, transmissions |

Les neuf autres viendront ensuite, un chapitre par version, dans l'ordre de la journée.

Pour la première soignante, la séance Soins ne tire que des chapitres complets. Les autres apparaissent dans
« Ma journée au service » avec la mention « bientôt », ou n'apparaissent pas du tout : c'est à Jacques de choisir.

## (c) Le branchement dans le moteur

Tout ce qui suit ne vaut que si `soinsActifs()` est vrai. Pour tout autre compte, l'accueil reste celui d'aujourd'hui,
ligne pour ligne : les parcours de et es doivent donner 0 écart à chaque version.

1. **Une seule source pour les chapitres : `pflege/datos/chapitres.json`**, dérivée par `pflege/outils/chapitres.py`.
   - Ce qu'elle porte, pour chaque chapitre : l'id (`ch01_aufnahme` … `ch14_pause`), le titre et le sous-titre en 9
     langues, la ou les scènes, les dialogues dans l'ordre, les écrits, le thème illustré (sa page), les points de
     grammaire, les groupes de cartes-phrases.
   - Les mots, les paires, les abréviations et les cartes-phrases ne sont pas recopiés : ils portent un champ
     `chapitre` dans leur source, posé par la session qui les tient.
   - Le contrôle (`tests/pflege.py`) refuse un mot ou un dialogue sans chapitre, et un chapitre vide marqué « prêt ».
2. **L'état Soins / Général** : `PREFIXE_STOCKAGE + "modeAccueil"`, qui vaut « soins » ou « general ».
   - Par défaut « soins » pour un compte ouvert aux Soins ; rien pour les autres.
   - Il reste sur l'appareil, comme `vocabDeplie` (v1202), et n'a donc pas besoin de règle Firestore.
   - L'interrupteur, en haut de l'accueil, est un contrôle à deux segments, en 9 langues (plus l'espagnol au lot 7 de
     cette session).
   - « Allemand général » montre l'accueil d'aujourd'hui, sans rien changer. « Soins » remplace la carte de la séance et
     la grille par l'accueil de la maquette.
3. **L'accueil Soins** (une fonction `majAccueilSoins()`, un bloc HTML à côté de celui de la séance) :
   - la carte « Ma séance Soins », avec le titre du chapitre du jour, environ 10 minutes, le compteur sur 15, les deux
     portes, les quatre lignes de son contenu et « Commencer la séance » ;
   - le ruban « Ma journée au service », qui dit N chapitres et ouvre l'écran du chapitre ;
   - « Écouter, répéter : les phrases du service » (les cartes-phrases) ;
   - le bloc telc Pflege (examen blanc, « prochaine étape »), repris de l'écran Soins actuel ;
   - l'écran Soins actuel (la liste des thèmes) reste, ouvert depuis Tout le contenu.
4. **Les deux portes** remplacent la rangée A1-C1 sur la carte Soins seulement.
   - « Je commence » prend les niveaux A2 et B1 ; « Je prépare l'examen », B1 et B2.
   - Le choix est retenu sous `PREFIXE_STOCKAGE + "porteSoins"`, sur l'appareil.
   - Le niveau général du compte (`niveauSeance`) ne bouge pas : il garde son sens dans « Allemand général ».
5. **La séance Soins** (`ouvrirSeanceSoins()`) réutilise la mécanique de la séance : paquet, parties, barre, écran de fin
   et reprise. Elle a son propre constructeur, comme Premiers pas. Environ 15 cartes, dans cet ordre :
   - les mots du chapitre du jour, ceux qui sont dus d'abord, puis des nouveaux du niveau de la porte (environ 11) ;
   - une paire patient / service, sur une carte à deux sens à créer : le patient dit ↔ le service dit, selon le format
     § 1 bis de la session vocabulaire ;
   - une abréviation, lue par `lecture_mot` (« Er-Er, Blutdruck ») ;
   - pour finir, le dialogue du chapitre (`conv_arret`, `soins`, `c=<id>` choisi), en partie Conversations.

   **Le chapitre du jour** est le premier chapitre complet que l'on n'a pas encore fait, dans l'ordre de la journée ;
   quand tous sont faits, on repart du plus ancien. L'avancement des chapitres reste sur l'appareil pour la première
   soignante. Le passer dans la sauvegarde demandera une clé et donc les règles de Jacques, comme `soinsExamensJson`.
6. **L'écran d'un chapitre** (une section `soinsChapitre`) montre :
   - la scène ;
   - le thème illustré (sa page dans le cadre, comme `ouvrirThemeIllustre`) ;
   - les conversations (le lecteur des dialogues, `?soins=1&c=`) ;
   - l'écrit ;
   - ses mots, ses paires et ses cartes-phrases, en paquets.
   Chaque élément revient à cet écran par « fermer ».
7. **L'écrit** : la page d'entraînement à l'écrit de pflege-examen (`telc-pflege`, partie Schreiben), ouverte sur un
   sujet (`?sujet=<id>`) qu'elle lit dans `pflege/datos/ecrit.json`. Aucun lecteur nouveau : le contrat est à convenir
   avec pflege-examen.

**Ce qui touche `index.html`** : les points 2 à 6. Il faut donc une version à chaque lot, avec les parcours de et es
(0 écart attendu), la sonde Soins Playwright et une **sonde WebKit iPhone** (320 et 375 px, Safari), ce qui demande une
ligne de file et le verrou.
- `conversation.html` et la page de l'écrit sont des pages en cadre (contrôles propres, sans version si `index.html` ne
  change pas).
- `chapitres.json` et les champs `chapitre` sont des données (sans version).

## (d) Heures et dépenses, par étape

| Étape | Qui | Heures | Dépense |
|---|---|---|---|
| E1. `chapitres.json`, son outil, son contrôle ; les champs `chapitre` sur les mots, les paires et les abréviations | architecture + vocabulaire | 3 h + 3 h | — |
| E2. L'interrupteur, l'accueil Soins, les deux portes (9 langues) | architecture | 6-8 h | — |
| E3. La séance Soins, la carte de paire à deux sens, la lecture des abréviations | architecture | 8-10 h | — |
| E4. L'écran du chapitre | architecture | 3-4 h | — |
| E5. La page de l'écrit ouverte sur un sujet | pflege-examen | 3-5 h | — |
| E6. Les 5 thèmes illustrés des premiers chapitres (le modèle de `visuel/THEMES-ILLUSTRES.md` : les personnes déjà faites, ≈ 10-15 images par thème) | scènes (+ une session de plus, à décider par le chef) | 5-7 h chacun, ≈ 30 h | ≈ 1,50-2,25 $ par thème, **≈ 8-11 $** |
| E7. Les écrits manquants de la douleur et du téléphone (9 langues) | dialogues | 3 h | — |
| E8. La 2e conversation de la relève | dialogues | 1,5 h | voix ≈ 0,50 $ |
| E9. Les voix : d13-d26 (531 fichiers) | dialogues | 1-2 h | ≈ 6 $ (+ 2,70 $ pour l'accent) |
| E10. Les voix des mots et des exemples des 5 chapitres (≈ 350 mots + exemples) | vocabulaire / voix | 2 h | ≈ 6-7 $ (≈ 12-14 $ pour les 778) |
| E11. Les 5 visages manquants | scènes | 1 h | ≈ 0,75-1,50 $ |
| E12. Les sondes, dont WebKit iPhone, et les versions | architecture | 3-4 h, **lignes de file** | — |
| E13. La relecture médicale des 5 chapitres | personne du métier | externe | décision de Jacques (bilan du 16 nov., § 3) |

**Pour les 5 premiers chapitres** :
- environ 25-32 h d'architecture ;
- environ 30 h de thèmes illustrés, à répartir entre deux sessions ;
- environ 10 h de contenu (vocabulaire, dialogues, examen) ;
- **environ 23-29 $** en tout : ≈ 8-11 $ d'images, ≈ 6 $ + 2,70 $ pour les voix de d13-d26, ≈ 6-7 $ pour les voix des
  mots, ≈ 1 $ de visages.

En une semaine, c'est tenable pour 4 chapitres (douleur, relève, admission, téléphone) si les thèmes illustrés
avancent en parallèle de l'architecture. Le 5e (les soins du matin) si le temps le permet.

**Les 9 autres chapitres** ensuite :
- 9 thèmes illustrés, ≈ 14-20 $ et ≈ 55 h ;
- 6 écrits, ≈ 9 h ;
- 4 conversations, ≈ 6 h et ≈ 2 $ de voix ;
- la scène de la famille, ≈ 0,90 $ et 5 h ;
- les mots de la sortie, ≈ 2 h.

## La répartition proposée (le chef la donne)

| Session | Ce qu'elle fait | Ses fichiers |
|---|---|---|
| **architecture** (moi) | E1 (structure), E2, E3, E4, E12 ; l'intégration | `index.html`, `pflege/datos/chapitres.json`, `pflege/outils/chapitres.py`, `tests/pflege.py` |
| **pflege-vocabulaire** | le champ `chapitre` sur les 778 mots ; les mots de la sortie ; E10 avec l'accord de Jacques | `pflege/sources/*.py`, `pflege/sources/vocabulaire/` |
| **pflege-dialogues** | le champ `chapitre` sur les dialogues, les écrits et les cartes-phrases ; E7, E8 ; E9 avec l'accord de Jacques | `pflege/sources/dialogues/`, `ecrit/`, `redemittel*` |
| **pflege-scenes** | E6 pour la douleur, la relève et l'admission ; E11 | `visuel/prototype/<chapitre>.html` (thèmes Pflege), `visuel/soins-themes/`, `pflege/scenes/` |
| **une session de plus** (si le chef le juge utile) | E6 pour le téléphone et les soins du matin | ses propres pages de thèmes |
| **pflege-examen** | E5, la page de l'écrit ouverte sur un sujet | `visuel/prototype/telc-pflege/` |

Ordre : d'abord E1, pour que chacun pose les champs `chapitre` sur le même découpage. Ensuite tout le reste en
parallèle. Une version par lot dans `index.html` : E2 et E4 ensemble, puis E3.

⚕️ Le contenu des 5 chapitres reste à relire par une personne du métier avant toute ouverture (bilan du 16 nov.).
