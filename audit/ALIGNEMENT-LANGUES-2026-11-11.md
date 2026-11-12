# Alignement des langues apprises — mesure du 11 nov. 2026 (v1159)

Demande de Jacques (11 nov., `decisions/DECISIONS.md`) : « Est-ce que tu t'assures que la version pour apprendre le portugais comme pour apprendre le japonais est parfaitement alignée […] ? » — « Oui, mesure l'écart ». Puis (chef, 11 nov.) : on alignera le portugais et le japonais sur l'allemand et l'espagnol, tout sauf les voix ElevenLabs.

**Ce document MESURE, il ne modifie rien.** Code lu : `index.html` v1159 (`origin/main`, commit `db2133f`), `visuel/prototype/`, les dossiers de données. Toutes les références `NNNNN` sans nom de fichier sont des lignes d'`index.html`.

Légende des cases :

| État | Sens |
|---|---|
| **présent** | la fonction marche dans cette langue (une précision entre parenthèses dit ce qui diffère) |
| **caché** | retiré exprès : liste blanche CSS `html[data-apprendre="xx"]` (3440-3580) ou garde JS |
| **absent** | le code laisserait passer, mais le contenu de la langue manque (la partie saute ou reste vide) |
| **allemand** | « retombe sur l'allemand » : un texte, une voix ou une donnée allemande servie à une autre langue — le défaut le plus grave |
| **inconnu** | pas tranché sans exécution |
| **sans objet** | n'a pas de sens dans cette langue (ex. les examens allemands) |

Méthode : lecture des gardes (`LANGUE_APPRISE ===` 206 fois, `!==` 27 fois, `data-apprendre` 129 fois), tri des 116 tests `=== "es"` / `!== "es"` (une branche « es sinon allemand » est-elle atteignable en en/pt/ja ?), contrôle des fichiers sur disque. **Pas d'exécution dans un navigateur** : la sonde prévue (section 5) n'a pas tourné, le verrou du navigateur étant réservé à d'autres travaux (consigne du chef, 11 nov.). Les cas « inconnu » et ceux marqués « à confirmer » restent à vérifier par les sessions des lots.

---

## 1. En bref

### 1.1 Les « retombe sur l'allemand » (du plus visible au plus caché)

| # | Ce qui sort | Langues | Où | Comment on y arrive |
|---|---|---|---|---|
| 1 | **La recherche propose des verbes allemands** : « helfen », « danken »… (9 verbes à cas fixe) et « stehen », « liegen »… (8 verbes de position). En japonais, aussi les listes allemandes **entières** de prépositions, conjonctions et particules | **es (production)**, en, pt ; ja (+ listes) | `buildSearchIndex` 48218, 48226-48231 indexe `kasusVerbTheme` (40841) et `positionsverbenTheme` (41038), écrits en dur sans branche de langue ; ja : `japonais/datos/fonctionnels.json` est rangé par niveau, pas par `praepositionen`/`konjunktionen`/`partikeln`, donc les listes allemandes 40871, 41612, 41750 restent | La loupe (es, en, pt) ; en ja la loupe est cachée (3466) mais « Chercher dans les mots » de Tout le contenu y mène (50398) |
| 2 | **Prononciation : « Lire l'allemand » / « L'allemand se lit presque toujours comme il s'écrit… »** en tête de l'écran | en, pt, ja | clés `pron_kicker`, `pron_intro` (13899, 13903) surchargées seulement par `I18N_ESPAGNOL` | Tuile Prononciation (sur la liste blanche des trois langues) |
| 3 | **« Ma façon d'apprendre » montre « der die das »** ; en anglais, aussi « Pour vivre en Allemagne » | en, pt, ja (+ en) | `ouvrirProfil` 36353 (aperçu `#pfApMots`, HTML 9863) ; `profil_r_vivre` 16364 non surchargé par `I18N_ANGLAIS` ; `profilAPoser()` (36339) ne teste pas la langue apprise | Lien « Ma façon d'apprendre › » de la séance, inscription, admin |
| 4 | **Bouton « Essai » de la voix : « Guten Tag! Ich lerne jeden Tag ein bisschen Deutsch. »** lu par la voix anglaise, portugaise ou japonaise ; la ligne française dit « J'apprends un peu d'allemand » | en, pt, ja | `testVoice()` 56700-56704 | Réglages → Son → Voix de lecture → Essai (et à chaque choix de voix) |
| 5 | **Le tableau portugais : « …d'un peintre du monde germanophone »** | pt | `mosaique_reste` (15255, lu à 63186), `mosaique_intro_texte` (15262 → 63151), `ip_tableau_1` (15928 → 11159), non surchargés par `I18N_PORTUGAIS` (en, ja, es les surchargent) | Tableau en plein écran ; carte « Comment lire ta progression » |
| 6 | **Radar « Progression par catégorie » : l'axe « Cas »** (déclinaisons allemandes, calculées sur le paquet allemand) ; en ja, les axes Prépositions et Particules lisent aussi les listes allemandes | en, pt, ja | `renderProgressRadar()` 46329, `getKasusMasteryPercent()` | Réglages → Ma progression |
| 7 | Écran avant l'abonnement : « 7 700 mots du A1 au C1 » (le compte allemand), « A2, B1 et DTZ » | en, pt, ja (admin seul aujourd'hui) | `abo_av_mots`, `abo_av_examens` 16433-16434, écran 50828 | Aperçu admin seulement (50772) ; deviendra visible avec l'abonnement |
| 8 | Administration : champ « ORAL : ESSAYER CETTE PHRASE » prérempli « Das macht drei Euro fünfzig. » | en, pt, ja (admin) | 52469 | Réglages → Administration |
| 9 | Donnée allemande **lue sans être affichée** : la scène de la séance en anglais lit `scene-<nom>.js` (allemand) au lieu de `.en.js` ; aucun mot ne correspond, donc **pas de scène dans la séance anglaise A1** (alors que la pilule l'annonce, 70104) | en (info) ; ja dans Premiers pas (67847, sans effet visible) | `motsVusDeScene` 69194 : suffixe `.es`/`.pt` seulement | Séance du jour en A1, escales de l'A1 voyage |

Latents (aucun chemin visible trouvé, à surveiller si on ouvre une porte) :
- `apprendreThemeIllustre()` (50616) envoie `apprendre=de` pour pt et ja : une page de thème ouverte en pt/ja **serait en allemand**. Fermé aujourd'hui par `themesIllustresOuverts()` (50611-50615) et `themeDuJour` (69357) ; trois fonctions contournent la table (`ouvrirThemeGato`, `ouvrirThemeLoisirs`, `ouvrirDescripcion`, 50695-50699), appelées depuis des écrans cachés en pt/ja (ex. bouton `praep_btn_gato`, 11768).
- Replis en cas d'échec réseau, allemands dans toutes les langues : `verbe.json` → « haben » (39349) ; `funktionswort.json` → prépositions, particules, conjonctions allemandes (visibles par les tuiles praep/konjunktionen en anglais).
- Anglais : `orbPanelData` (46800) ne prend le panneau anglais que si `TUILES_ANGLAISES` est déjà chargé (`chargerCours()`, asynchrone) ; un toucher trop tôt sur Pronoms, Nombres, Prépositions, Connecteurs ou Ordre des mots ouvre le panneau allemand (options en grande partie cachées).
- `rp_article` (66623) proposerait der/die/das pour un repère de genre en en/ja ; aucun `reperes.json` en/ja n'en a.
- Micro des pages en cadre fixé en `de-DE` (50679) : ne sert qu'à `dtz-oral.html` et `telc/oral.html`, allemandes.

### 1.2 Comptes par état

Sur les 81 lignes des tableaux de la section 2 (2.1 à 2.5), les thèmes illustrés comptés un par un, soit **101 cases par langue** :

| État | de | es | en | pt | ja |
|---|---|---|---|---|---|
| présent | 95 | 94 | 67 | 45 | 31 |
| caché | 1 | 2 | 15 | 43 | 55 |
| absent | 0 | 0 | 9 | 3 | 4 |
| **allemand** | 0 | **1** | 6 | 7 | 6 |
| inconnu | 0 | 0 | 0 | 0 | 2 |
| sans objet | 5 | 4 | 4 | 3 | 3 |

« Caché » en allemand = l'objectif quotidien, retiré pour tous le 8 nov. Le « allemand » de l'espagnol (en production) = la recherche (1.1 n° 1).

---

## 2. Tableau principal, fonction par fonction

### 2.1 La séance du jour et ce qui l'entoure

Assemblage : `entrerSeanceDuJour()` 45745 → `ouvrirSeanceDuJour()` 69458. Le japonais a sa séance à lui, réduite : `seanceJaponaise()` (69457) retire l'A1 voyage, les cartes-phrases, la scène, le regroupement en parties ; garde aussi l'objectif quotidien (60565).

| Fonction | de | es | en | pt | ja | Preuves |
|---|---|---|---|---|---|---|
| Assemblage de la séance | présent | présent | présent | présent | présent (réduite) | 69458 ; ja 69457 |
| Plan annoncé sur l'accueil (pilule) | présent | présent | présent (annonce en A1 une scène qui ne vient pas) | présent | caché (texte générique) | `planSeanceDuJour` 70044, 70045 (ja), 70104 |
| Nouveaux mots, révisions | présent | présent | présent | présent | présent | `cartesDeSeance`, `echeancesDeSeance` sans test de langue |
| Premiers pas | présent | présent | présent | présent | présent (6 étapes au lieu de 8, sans scène, seulement par 🌱) | `premiers-pas.json` ×5 ; 67683 ; révisions de Premiers pas absentes en ja (69489) |
| A1 voyage (12 escales, jalon, suite de 8) | présent | présent | présent (sans les arrêts de scène, voir « scène ») | présent | absent (pas de `japonais/datos/a1-voyage.json`) et caché | 69502-69503 |
| Repères (nombres, jours, mois…) | présent (11) | présent (10) | présent (8 : sans alphabet ni genre) | présent (11) | présent (9, avec les compteurs つ / 人) | `reperesPourMoi` 68454 ; 69535 |
| Scène du jour dans la séance | présent | présent | absent en A1 (lit la scène allemande, 0 mot trouvé) ; présent A2+ | présent | caché (et seulement 3 scènes japonaises) | `motsVusDeScene` 69194 ; `arretDeScene` 69305-69320 ; ja 69528 |
| Thème illustré du jour (1 jour sur 3) | présent | présent | présent (15 thèmes) | caché | caché | `themeDuJour` 69357 ; `themesIllustresOuverts` 50611 |
| Son du jour | présent | présent | présent | présent | présent | 68701-68715, 69537 ; `prononciation.json` ×5 |
| Feuille de conjugaison du jour | présent (A2-C1) | présent (A2-B2) | présent (dès A1, sans « verbe du jour » ni phrase à ordonner) | présent (idem en) | inconnu (A1-A2, rendu non vu) | `preparerFeuille` 69509 ; `champTempsFeuille` 68289 ; commentaire 69451 contraire au code |
| Cartes-phrases et grammaire en séance | présent | présent | présent (grammaire A1 seulement, à tous les niveaux) | présent (A1-C1) | caché | 69520 ; `COURS_GRAMMAIRE_PAR_LANGUE.en` 64977 (15 séries A1) ; `CONJUGAISON_PAR_NIVEAU` 65196 |
| Oral en séance (verdict) | présent | présent | présent | présent | présent (par le son du jour et les repères seulement) | langue de reconnaissance 66985-66988 ; `scoreOral` ja 65900 |
| Regroupement en parties, écrans de passage | présent | présent | présent (barre sans noms) | présent (barre sans noms) | caché en séance | 69541 ; `nomme = repereSeanceDispo()` 69952 |
| Repères de séance v1155-v1159 (noms sous la barre, paysages, `#seanceFond`, son du jour or) | présent | présent | caché | caché | caché | `repereSeanceDispo()` 69759 ; 69772 cache `#seancePaysage` et `#seanceFond` ; paysages en SVG inline (`PAYSAGES_SEANCE`), aucun fichier image à porter |
| « Ton ciel » (tuile, `ouvrirCiel`) | présent | présent | caché | caché | caché | `cielDisponible()` 61077 |
| Ciel et fête de l'étoile à l'écran de fin | présent | présent | présent (**incohérent** : la tuile du ciel est cachée) | présent (**incohérent**) | caché ; fin de Premiers pas : inconnu | `etoilesDeLaSeance()` 60973 n'exclut que ja ; `etatCielFin` 60983 |
| Objectif quotidien et anneau | caché (retiré le 8 nov.) | caché | caché | caché | présent (l'objectif retiré ailleurs survit en ja) | CSS 9108-9109 ; `objectifRetire()` 60565 |
| Première semaine progressive | sans objet | sans objet | sans objet | sans objet | présent | `getDailyGoalTarget` 45015 ; `tailleSeance` 60540 |
| Flamme | présent | présent | présent | présent | présent | aucune garde de langue |
| Écran de fin | présent (séance légère, ciel ou tableau) | présent | présent (tableau américain) | présent (tableau portugais) | présent (version « objectif », sans ciel ni tableau) | 71833 ; `rendreTableauFin` 61391 |
| Bilan de la semaine | présent | présent | présent (sans notions de grammaire) | présent (idem) | présent (idem) | `BILAN_JEUX` 45593 ne liste que des séries de/es ; filtre 45711 |
| Rappel actif dans les cartes | présent | présent | caché | caché | caché | `carteEligibleRappel` 55806 (de ou es) |
| Test de niveau (essai admin « placement ») | présent | présent | caché | caché | caché | `placementDisponible()` 51233 |
| Découverte guidée (premier lancement) | présent | présent | caché | caché | caché | `lancerDecouverte()` sort à 36684 hors de/es |
| « Ma façon d'apprendre » (profil) | présent | présent | **allemand** | **allemand** | **allemand** | 36353, 9863, 16364 (voir 1.1 n° 3) |

### 2.2 L'accueil

| Fonction | de | es | en | pt | ja | Preuves |
|---|---|---|---|---|---|---|
| Ruban « Explorer les scènes » | présent (39) | présent (39) | présent (33 : 6 écartées) | présent (38 : l'hiver écarté) | présent (3 scènes propres) | 64105-64156 ; `SCENES_ECARTEES_*` 63825-63829 ; `SCENES_JA` 64082 ; « N › » caché en ja (3463) |
| Panneau des scènes | présent | présent | présent | présent | caché (**panneau vide** : la tuile Scènes de la grille reste visible) | `.orb-opt` ja 3484 n'excepte pas `ouvrirScene` ; `tuilesProposees` 50224 |
| Ouverture d'une scène (`scene-<nom>.<langue>.js`) | présent | présent (43 fichiers) | présent (37 fichiers) | présent (42 fichiers) | présent (3 fichiers) | `langueSeuleDeScene` 64643-64653 ; `visuel/prototype/index.html:433-458` ; aucun repli allemand (un fichier manquant plante la page), aucun ne manque pour une scène atteignable |
| Ligne « Aujourd'hui : <scène> » | présent | présent | présent | présent | inconnu (à vérifier à l'écran) | `majAujourdhuiScene` 69414-69449 sans garde ja |
| Thèmes illustrés (pages) | présent (22) | présent (22) | présent (15) ; absent (7) | caché | caché | `THEMES_ILLUSTRES` 50588 ; pages `visuel/prototype/<thème>.html` ; sous-tableau 2.5 |
| Bloc « Thèmes illustrés » de l'accueil, tuile Thèmes | présent | présent | présent | caché | caché | 64172-64178 ; 50225 |
| Grille de l'accueil (tuiles) | présent | présent | présent | présent | présent (sans Thèmes, Écouter, Épisodes) | `majGrilleAccueil` 50234 ; 50219-50233 |
| Suggestions « Pour aller plus loin » | présent | présent | présent | présent (sans thème) | caché | 50291, 50309 |
| Ton tableau, galerie (mosaïque) | présent (65) | présent (66 + héritage allemand voulu) | présent (67) | **allemand** (textes « peintre du monde germanophone ») ; tableaux présents (66, Brésil inclus) | présent (60 ; `img/info.jpg` manque, la toile de « Comment lire ta progression » reste vide) | `MOSAIQUE_BASE` 61953 ; 63151, 63186, 11159 ; `japonais/mosaique/app/img/info.jpg` absent |
| Épisodes vidéo | présent | présent | caché (absent : `EPISODES` sans série en) | caché (absent) | caché (absent) | `EPISODES` 70574-70605 ; CSS 3465, 3510, 3554 |
| Écouter (ligne, tuile, menu) | présent | présent | présent | présent | caché | CSS 3464 ; grille 50226 |
| Recherche d'un mot | présent | **allemand** (verbes) | **allemand** (verbes) | **allemand** (verbes) | **allemand** (verbes + listes), loupe cachée | voir 1.1 n° 1 |
| Dictionnaire intégré (`dict/`) | présent | présent (`espanol/dicc`) | absent (`anglais/dicc` n'existe pas, la section s'efface) | absent (garde 49386) | absent | `urlDonnees` 15159 ; `DICT_BASE_URL` 49263 ; 49459 |
| Filtre de Tout le contenu | présent | présent | présent | présent | présent | `filtrerContenu` 50371 |
| Mis de côté | présent | présent | présent | présent | présent | 71724-71800 |
| Carnet de phrases | présent | présent | caché (le contenu existe) | caché (le contenu existe) | caché (absent) | `data-orbid="carnet"` 10837, sur aucune liste blanche |
| Flamme, version, signaler | présent | présent | présent | présent | présent | — |

### 2.3 Tout le contenu (tuiles et panneaux)

Tuiles visibles par langue (liste blanche CSS 3469, 3514, 3559 ; espagnol 3448, 3608, 8733-8739) :

| Tuile | de | es | en | pt | ja | Preuves |
|---|---|---|---|---|---|---|
| Par thème, Noms, Verbes, Adjectifs, Adverbes (parcourir) | présent | présent | présent | présent | présent | listes blanches |
| Fiches de grammaire | présent (tuiles Cas, Prépositions…) | présent (17 fiches, « Toutes les fiches ») | présent (66 fiches) | présent (56 fiches) | présent (13 fiches) | `grammaire.json` de chaque langue ; `abrirIndiceGramatica` |
| Tuiles de grammaire : Pronoms, Nombres, Prépositions, Connecteurs, Ordre des mots | présent | présent (en fiches : `FICHE_PAR_TUILE` 47268 ; Connecteurs caché 3608) | présent (données `tuiles` de `anglais/datos/grammaire.json`) | caché (pas de clé `tuiles`) | caché (pas de clé `tuiles`) | `orbPanelData` 46800 (`TUILES_ANGLAISES`) |
| Cas, zu + infinitif | présent | présent (fiches ser/estar, subjonctif) | caché | caché | caché | allemand par nature ; l'espagnol les remplace par des fiches |
| Feuilles de conjugaison | présent | présent | présent | présent | présent | `conjugaison.json` ×5 (ja : A1 8, A2 5 feuilles) |
| S'entraîner par temps | présent | présent | présent (12 séries) | présent (12 séries) | caché | `openVerbenTempsInfo` absent de la liste blanche ja (3484) |
| Écrire, Construire la phrase | présent | présent | présent | présent | caché | tuile `schreiben` hors liste ja |
| Expressions (familles, faux amis) | présent | présent | présent (`EXPRESSIONS_ANGLAISES`) | caché | caché | tuile `ausdruecke` hors listes pt/ja |
| Prononciation | présent | présent | **allemand** (en-tête) | **allemand** (en-tête) | **allemand** (en-tête) | 13899, 13903 |
| Kana | sans objet | sans objet | sans objet | sans objet | présent | `data-seulement-ja` |
| Mon vocabulaire | présent | présent | présent | caché | caché | `monvocab` hors listes pt/ja |
| Examens (Goethe, telc, DTZ) | présent | sans objet (caché) | sans objet (caché) | sans objet (caché) | sans objet (caché) | allemand par nature ; 3448 et listes blanches |
| Mon cours (VHS, admin) | présent (admin) | présent (admin, manuel d'espagnol) | caché | caché | caché | `vhskapitel` |
| Radar « Progression par catégorie » | présent | présent | **allemand** (axe Cas) | **allemand** (axe Cas) | **allemand** (Cas, Prépositions, Particules) | 46329 |

Options des panneaux de mots (filtre `.orb-opt[onclick*=…]`, 3484, 3519-3535, 3560-3573) :

| Option | de | es | en | pt | ja |
|---|---|---|---|---|---|
| Réviser les mots dus (Noms, Verbes, Adjectifs) | présent | présent | caché | présent (Noms seulement) | caché |
| Mots au hasard | présent | présent | caché | présent (Noms seulement) | caché |
| Par niveau, par thème | présent | présent | présent | présent | présent |
| Dictées (noms, verbes, adjectifs, adverbes) | présent | présent | présent | présent | caché |
| Quel article ? | présent | présent | sans objet | présent | sans objet |
| Règles du genre, terminaisons | présent | présent | caché | caché | caché |
| Faux amis | sans objet | présent | présent | absent | absent |
| Déclinaison des adjectifs, wissen/kennen | présent | caché | caché | caché | caché |
| Adverbes : la nuance, le thème Loisirs | présent | présent | caché | caché | caché |

### 2.4 Voix, oral, stockage, interface

| Fonction | de | es | en | pt | ja | Preuves |
|---|---|---|---|---|---|---|
| Voix enregistrée (ElevenLabs) | présent (Aurora) | présent (Lolita, Monica) | présent (Sarah, US A1-A2 ; GB absent) | absent (téléphone) | absent (téléphone) | `audio` 14456, 14478, 14529, 14560, 14503 ; repli 58680, 59513 |
| Voix du téléphone | présent | présent (es-MX peu favorisé, +2 contre +10 pour « Google ») | présent | présent (pt-PT / pt-BR) | présent (ja-JP) | `pickVoice`/`voicesForLang` 56588-56621, 56515 |
| Bouton « Essai » des voix | présent | présent | **allemand** | **allemand** | **allemand** | 56700-56704 |
| Voix des scènes | présent | présent | présent (téléphone, jamais Sarah) | présent (téléphone) | présent (téléphone) | `visuel/prototype/index.html:477, 867, 875, 960` |
| Voix des thèmes illustrés | présent | présent | présent (Sarah si connue, sinon téléphone) | caché | caché | `themes/voix.js:21-26` |
| Reconnaissance vocale (oral à verdict) | présent | présent | présent | présent | présent | 66985-66988, 67034, 67267 |
| Stockage local (préfixe propre) | présent | présent | présent | présent | présent | 14262-14265 ; flamme, ciel, mosaïque, épisodes préfixés |
| Progression Firestore (collections et règles) | présent | présent | présent (publication des règles : inconnu) | présent (publiées le 30 oct.) | présent (publication : inconnu) | 56431-56436 ; `firestore.rules:41-136` |
| Langues d'interface | 9 | 5 (fr, en, pt, ar, de) | 2 (fr, es) | 1 (fr) | 2 (fr, en) | `UI_LANGS` 14391 |
| Variante | sans objet | présent (Espagne / Amérique latine) | présent (US / GB) | présent (Portugal / Brésil) | sans objet | 14270-14340 |
| Ouverture à un compte | sans objet | sans objet | présent (champ `essais`) | caché (admin seul, voulu) | caché (admin seul, voulu) | `gardeEssaiJaponais` 15062 |
| Carte « Crédits » | présent | présent (sans crédit de voix) | présent (sans crédit Sarah) | présent (sans fréquence) | présent (JMdict) | 3444-3453, 3507-3509, 3550-3553 |
| Rappels locaux (notifications) | présent | présent | présent | présent | présent | 38176-38206, textes neutres |
| Écran avant l'abonnement | présent | présent | **allemand** (admin seul) | **allemand** (admin seul) | **allemand** (admin seul) | 16433-16434 |

### 2.5 Les thèmes illustrés, un par ligne

Comment une page choisit sa langue : 15 pages font `["de","en"].includes(q) ? q : "es"`, 7 pages (transportes, courses, vacances, travail, ecole, ciudad, fetes) font `q === "de" ? "de" : "es"` ; même règle dans `themes/voix.js:21`. Aucune page n'a d'objet PT ni JA. Phrases fabriquées depuis les données (règle des thèmes) : le portugais et le japonais demandent leur générateur de phrases, comme l'anglais a eu le sien.

| Thème | de | es | en | pt | ja |
|---|---|---|---|---|---|
| familia, descripcion, emociones, contrarios, gato, ropa, cuerpo, journee, manger, metiers, loisirs, animales, meteo, logement, demarches (15) | présent | présent | présent | caché | caché |
| transportes, courses, vacances, travail, ecole, ciudad, fetes (7) | présent | présent | absent | caché | caché |

### 2.6 Volume du contenu (données sur disque)

| Données | de | es | en | pt | ja |
|---|---|---|---|---|---|
| Noms A1 / A2 / B1 / B2 / C1 | 474 / 623 / 1807 / 449 / 948 | 528 / 557 / 517 / 236 / — | 610 / 705 / 1037 / 418 / 548 | 510 / 730 / 1134 / 462 / 686 | 404 / 369 / 815 / 55 / — |
| Verbes A1 → C1 | 111 / 236 / 515 / 180 / 272 | 123 / 274 / 314 / 162 / — | 145 / 311 / 385 / 182 / 175 | 120 / 322 / 443 / 191 / 138 | 108 / 153 / 153 / 30 / 0 |
| Adjectifs A1 → C1 | 106 / 153 / 338 / 104 / 291 | 90 / 161 / 261 / 101 / — | 123 / 203 / 396 / 124 / 213 | 92 / 221 / 396 / 130 / 152 | 82 / 44 / 64 / 9 / 0 |
| Thèmes de vocabulaire | 197 | 141 | 121 | 118 | 114 |
| Repères | 11 | 10 | 8 | 11 | 9 |
| Premiers pas (étapes) | 8 | 8 | 8 | 8 | 6 |
| A1 voyage (escales) | 12 | 12 | 12 | 12 | absent |
| Feuilles de conjugaison | A2-C1 (42) | A2-B2 (28) | A1-C1 (48) | A1-C1 (42) | A1-A2 (13) |
| Fiches de grammaire | (tuiles) | 17 | 66 | 56 | 13 |
| Scènes (fichiers de la langue) | 43 | 43 | 37 | 42 | 3 |
| Mosaïque (tableaux) | 65 | 66 | 67 | 66 | 60 |
| Fréquence, mots voisins | oui, oui | oui, non | oui, oui | non, oui | non, non |
| Dictionnaire | oui | oui | non | non | non |

L'espagnol s'arrête au B2 (choix existant) ; le japonais n'a presque rien au-delà du B1.

---

## 3. Portugais et japonais : chaque écart, ce qu'il faut pour le combler

Colonnes : **Voix ?** = l'écart dépend-il d'une voix enregistrée (exclu pour l'instant) ; **Moyen** = garde à élargir / texte à écrire / contenu à écrire (avec combien) / images ou scènes à adapter / décision de Jacques ; **Lot** = section 4.

### 3.1 Portugais

| Écart (pt) | Voix ? | Moyen | Lot |
|---|---|---|---|
| Recherche : verbes allemands (helfen…, stehen…) | non | garde : n'indexer `kasusVerbTheme` et `positionsverbenTheme` qu'en allemand (48218, 48226) — corrige aussi es et en | P1 |
| Prononciation : en-tête « Lire l'allemand » | non | texte : `pron_kicker`, `pron_intro` dans `I18N_PORTUGAIS` (et sa surcharge Brésil) — 2 clés | P2 |
| Profil : « der die das » | non | texte + garde : aperçu « o a » (36353), `profilAPoser` | P2 |
| Bouton Essai de la voix | non | texte : une phrase portugaise dans `testVoice` (56700) | P2 |
| Tableau : « peintre du monde germanophone » | non | texte : `mosaique_reste`, `mosaique_intro_texte`, `ip_tableau_1` dans `I18N_PORTUGAIS` — 3 clés | P2 |
| Radar : axe « Cas » | non | garde + **décision** : quel axe à la place (ex. Conjugaison) | P2 |
| Abonnement : « 7 700 mots », « DTZ » | non | texte : 2 clés (comptes pt calculés, pas d'examen) | P2 |
| Repères de séance (noms des parties, paysages, fond) | non | garde : `repereSeanceDispo()` 69759 ; les paysages sont en SVG, les noms des parties ont déjà leurs clés françaises | P1 |
| « Ton ciel » (et l'incohérence de l'écran de fin) | non | garde : `cielDisponible()` 61077 ; vérifier les constellations (étapes A1 voyage et Premiers pas pt existent) | P1 |
| Rappel actif | non | garde 55806 + table des fautes d'orthographe (`fautesOrthographe` 55660 retombe sur « de ») : quelques règles pt (accents, ç, nh/lh) | P1 |
| Test de niveau (admin) | non | garde 51233 (`niveauxPlacement` déjà générique) | P1 |
| Découverte guidée | non | garde 36684 + contenu de la démo (mots, `DEMO_TABLEAU` 37058) : une poignée de mots et un tableau portugais | P1 |
| Bilan de la semaine : notions de grammaire | non | contenu : séries pt dans `BILAN_JEUX` 45593 (les séries existent dans `exercices.json`) | P1 |
| Contraction « a o » au lieu de « ao » dans l'A1 voyage | non | garde : `contracterA1V` 67997 (pas de l'allemand, défaut pt) | P1 |
| Thèmes illustrés (22 pages) + thème du jour + bloc de l'accueil | non (téléphone pt-PT/pt-BR) | contenu : un objet PT par page et des phrases fabriquées pour le portugais (articles o/a, contractions do/da/no/na, possessifs), comme l'anglais (v1085) ; mots manquants au corpus pt ; `pt: true`, `themesIllustresOuverts`, `apprendreThemeIllustre` (50588-50616), `themes/voix.js` ; variante Brésil (Mom/Mum de l'anglais = mãe, ônibus/autocarro…) | P3 (15 thèmes) puis P4 (7) |
| Tuiles de grammaire (Pronoms, Nombres, Prépositions, Connecteurs, Ordre des mots, Adverbes) | non | contenu : une clé `tuiles` dans `portugais/datos/grammaire.json` (sur le modèle de `anglais/outils/tuiles_niveaux.py`), puis élargir à pt le test `LANGUE_APPRISE === "en" && TUILES_ANGLAISES` (46800) et la liste blanche | P5 |
| Expressions, Mon vocabulaire, Carnet de phrases | non | garde (liste blanche 3559) ; Expressions : vérifier `portugais/datos/expressions.json` contre l'écran, faux amis à écrire (≈ 20) | P5 |
| Options des panneaux (révision et hasard sur Verbes/Adjectifs, règles du genre, terminaisons, nuance des adverbes) | non | garde + contenu : règles du genre portugais (≈ 10 règles), terminaisons ; le reste est générique | P5 |
| Dictionnaire intégré pt-fr | non | contenu dérivé (WikDict, CC BY-SA, comme l'espagnol) + **accord de Jacques** pour le téléchargement | P6 |
| Fréquence (Leipzig pt) | non | contenu dérivé + **accord de Jacques** (comme l'anglais le 28 oct.) | P6 |
| Épisodes vidéo | oui (et vidéo) | **décision de Jacques** + dépense : il n'existe aucun épisode portugais | exclu |
| Voix enregistrée | oui | exclu (voix Google plus tard) | exclu |
| Langues d'interface (français seul) | non | **décision de Jacques** (anglais ? espagnol ?) puis textes | exclu tant que non décidé |
| Examens | — | sans objet (un examen portugais, CAPLE/CIPLE, serait une **décision**) | — |
| Scènes neuves de Lisbonne (30, décidées le 31 oct. / 1er nov.) | non | images hors de `main` (`portugais/lisbonne/`, rapport du pilote) : scènes à construire — chantier déjà ouvert, pas un écart du moteur | hors lots |

### 3.2 Japonais

Le japonais a, partout, sa propre branche (`seanceJaponaise()`, liste blanche la plus courte). L'aligner, c'est surtout **écrire du contenu** et **adapter des mécaniques à une langue sans espaces ni articles**. Données `japonais/datos/` **dérivées** : on corrige sur la branche `japonais` (dossier `C:/Users/jacqu/.wortando/wt-japonais`), jamais à la main sur `main`.

| Écart (ja) | Voix ? | Moyen | Lot |
|---|---|---|---|
| Recherche : verbes allemands + listes allemandes de prépositions, conjonctions, particules | non | garde (comme P1) + contenu : `fonctionnels.json` ja avec des clés propres (particules), sinon exclure ces listes de l'index | P1 + J4 |
| Prononciation, profil, Essai de la voix, radar, abonnement | non | textes dans `I18N_JAPONAIS` (pron ×2, profil, abo ×2), phrase japonaise dans `testVoice`, axes du radar (**décision**) | P2 |
| Panneau des scènes vide (tuile Scènes de la grille) | non | garde : ajouter `ouvrirScene` à la liste blanche ja (3484) ou retirer la tuile (50224) | P1 |
| `info.jpg` de la mosaïque manquant | non | image : copier un tableau de la collection (comme les autres langues) | P1 |
| Ligne « Aujourd'hui : <scène> » | non | à confirmer à l'écran ; garde si elle montre une scène allemande | P1 |
| Repères de séance, « Ton ciel », parties nommées | non | garde (`repereSeanceDispo`, `cielDisponible`, 69541) — **mais** dépend de la séance japonaise ci-dessous | J1 |
| Objectif quotidien encore présent (retiré le 8 nov. pour les autres) | non | **décision de Jacques** : retirer l'objectif en japonais aussi (passer à la séance légère) | J1 |
| Séance réduite : pas de cartes-phrases ni grammaire en séance | non | mécanique : les phrases à ordonner supposent des espaces (`melangerLaSuite` 65284) — découper en segments (bunsetsu) dans les données ; séries `exercices.json` ja à brancher | J2 |
| Scène dans la séance, Premiers pas sans scène | non | scènes à construire : 3 scènes en `main` ; les 35 scènes de Camille (décidées le 31 oct., images faites le 1er nov.) sont hors de `main` → `scene-<nom>.ja.js`, `SCENES_JA` ; puis lever la garde 69528 | J3 |
| A1 voyage absent | non | contenu : `japonais/datos/a1-voyage.json` (12 escales + jalon + 8 étapes, ≈ 100 phrases) et ses scènes d'escale (dépend de J3) | J3 |
| Thèmes illustrés (22) | non (téléphone ja-JP) | contenu : objet JA par page et générateur de phrases japonais (particules は/が/の, compteurs, politesse) ; après le portugais pour ne pas toucher les mêmes pages en même temps | J5 (après P3/P4) |
| Tuiles de grammaire (particules, nombres et compteurs, pronoms, connecteurs, ordre des mots, adverbes) | non | contenu : clé `tuiles` dans `grammaire.json` ja + élargir le test 46800 et la liste blanche | J4 |
| Écouter | non (téléphone) | garde (3464) + vérifier `ecouteLangues()` en ja (exemples ja présents ?) | J4 |
| S'entraîner par temps | non | contenu : clé `temps` (formes en ‑masu, passé, négatif, te‑form, potentiel…) | J4 |
| Écrire / Construire la phrase, dictées | non | mécanique + **décision de Jacques** : saisie en kana (clavier IME) ou choix parmi des segments | J4 |
| Expressions, Mon vocabulaire, Carnet, options des panneaux (révision, hasard) | non | garde + contenu (expressions ja) | J4 |
| Rappel actif, test de niveau, découverte guidée, bilan | non | garde + contenu (fautes typiques : kana voisins, chōon, sokuon) | J2 |
| Corpus B2-C1 presque vide (55 noms B2, 0 verbe C1) | non | contenu (centaines de mots) + **décision de Jacques** : s'arrêter au B1 comme l'espagnol au B2, ou viser le JLPT N2-N1 | J6 |
| Dictionnaire intégré, fréquence, mots voisins | non | contenu dérivé (JMdict déjà crédité ; fréquence à choisir) + **accord** | J6 |
| Épisodes, voix enregistrée | oui | exclu | exclu |
| Langues d'interface (fr, en) | non | **décision de Jacques** | exclu tant que non décidé |
| Examens (JLPT) | — | sans objet / **décision** | — |

---

## 4. Découpage proposé en lots indépendants

⚠️ Presque tout passe par `index.html`, un seul fichier. Des sessions parallèles y touchent des **zones disjointes** (lignes indicatives ci-dessous) ; git fusionne alors sans conflit, mais chaque lot garde ses changements dans sa zone, et la version ne monte qu'à la publication (le chef). Chaque lot passe `verifier.py`, `syntaxe.js` et les parcours de / es (**0 écart attendu** sauf P1, qui change la recherche espagnole : écart voulu à vérifier ligne à ligne).

| Lot | Contenu | Fichiers / zones | Dépend de |
|---|---|---|---|
| **P1 — Gardes et petits défauts (pt, et ja quand c'est une garde)** | recherche sans verbes allemands (de seul) ; `repereSeanceDispo`, `cielDisponible` + `etoilesDeLaSeance` cohérents ; rappel actif (+ fautes pt) ; test de niveau ; découverte guidée (démo pt) ; `BILAN_JEUX` pt ; contraction « ao » ; panneau des scènes vide en ja ; `info.jpg` ja ; ligne « Aujourd'hui » ja | `index.html` : 36684-37058, 45593-45711, 48218-48231, 51233, 55660-55830, 60965-61080, 67997, 69759, CSS 3484 ; `japonais/mosaique/app/img/info.jpg` | — |
| **P2 — Textes qui parlent d'allemand (pt et ja ; en au passage)** | `pron_kicker`/`pron_intro`, profil (36353, `profil_r_vivre`), `testVoice`, `mosaique_*`/`ip_tableau_1` pt, `abo_av_*`, phrase d'oral admin, axes du radar | `index.html` : blocs `I18N_JAPONAIS` 35042, `I18N_ANGLAIS` 35119, `I18N_PORTUGAIS` 35289 (+ surcharge Brésil), 36339-36360, 46329, 52469, 56700-56704 | décision radar |
| **P3 — Thèmes illustrés en portugais, les 15 déjà en anglais** | objet PT, générateur de phrases pt, mots au corpus pt, `pt: true` | `visuel/prototype/{familia,descripcion,emociones,contrarios,gato,ropa,cuerpo,journee,manger,metiers,loisirs,animales,meteo,logement,demarches}.html`, `visuel/prototype/themes/voix.js`, `portugais/outils/*` (corpus) ; `index.html` 50588-50616 | — |
| **P4 — Thèmes illustrés en portugais, les 7 autres** | idem (et ces 7 n'ont pas encore l'anglais) | `visuel/prototype/{transportes,courses,vacances,travail,ecole,ciudad,fetes}.html` | P3 (même branchement dans `index.html` et `voix.js`) |
| **P5 — Tout le contenu portugais** | tuiles de grammaire (clé `tuiles`), Expressions, Mon vocabulaire, Carnet, options des panneaux, règles du genre | `portugais/outils/tuiles_niveaux.py` (nouveau) → `portugais/datos*/grammaire.json` ; `index.html` : CSS pt 3550-3580, `orbPanelData` 46800-46990 | — |
| **P6 — Dictionnaire et fréquence portugais** | WikDict pt-fr, Leipzig pt, crédits | `portugais/datos*/dicc/`, `frequence.json`, outils ; `index.html` 49386, CSS crédits 3552 | **accord de Jacques** |
| **J1 — Séance japonaise alignée (mécanique)** | retirer les branches `seanceJaponaise()` qui ne tiennent qu'à l'objectif : parties nommées, repères de séance, ciel, séance légère | `index.html` : 60540-60650, 69457-69545, 69759, 69952, 70044, CSS 9108 | **décision objectif** ; après P1 (mêmes fonctions ciel/repères) |
| **J2 — Phrases et grammaire japonaises en séance** | segmentation des phrases, séries d'exercices, rappel actif, bilan | branche `japonais` (`japonais/datos/exercices.json`, outils) ; `index.html` 65223-65400, 69518-69522 | J1 |
| **J3 — Scènes japonaises et A1 voyage japonais** | 35 scènes de Camille en `scene-*.ja.js`, `SCENES_JA`, arrêts de scène, `a1-voyage.json` ja | `visuel/prototype/scene-*.ja.js`, branche `japonais`, `index.html` 64082-64110, 69528 | images déjà faites (à confirmer sur la branche) |
| **J4 — Tout le contenu japonais** | `fonctionnels.json` restructuré, tuiles de grammaire, temps, Écouter, Écrire/Construire, dictées, Expressions | branche `japonais` (outils → `japonais/datos/`) ; `index.html` CSS 3463-3485 | **décision saisie (kana)** |
| **J5 — Thèmes illustrés en japonais** | objet JA par page, générateur japonais | les 22 pages | P3 et P4 finis (mêmes fichiers) |
| **J6 — Corpus japonais B2-C1, dictionnaire, fréquence** | | branche `japonais` | **décision niveau visé** + accord |

Ordre conseillé : P1 et P2 d'abord (petits, visibles, et P1 corrige aussi l'espagnol en production) ; P3, P5 et P6 en parallèle ; P4 après P3 ; côté japonais, J1 (après décision) puis J2, J3, J4 en parallèle ; J5 après P4.

Pour information, l'anglais : seuls défauts propres, la scène A1 de la séance (`motsVusDeScene` 69194, ajouter `.en`), les 7 thèmes sans anglais, le carnet caché alors que son contenu existe, la révision et les « mots au hasard » cachés dans les panneaux, et la course au chargement des tuiles anglaises.

### 4.1 Trois clés allemandes qui dorment (vu par le lot P2, v1166, 11 nov.)

Trois textes de l'allemand n'ont **aucune surcharge** en pt, ja et en. Ils ne s'affichent nulle part aujourd'hui, donc on n'y a pas touché (décision du chef : pas de surcharge par précaution). **Chacun se réveille à une condition précise** : ce jour-là, il faut écrire le texte de la langue dans son bloc `I18N_*`, sinon il parlera d'allemand.

| Clé | Texte allemand (fr) | Pourquoi il ne s'affiche pas | Se réveille quand… |
|---|---|---|---|
| `credits_voix` | « Voix allemande : Aurora, générée avec ElevenLabs. » | la ligne des crédits est cachée par le CSS en es, ja, en et pt (`html[data-apprendre=…] [data-i18n="credits_voix"]`) | une langue reçoit sa ligne de crédits de voix (anglais : Sarah ; une voix pt ou ja enregistrée) et qu'on retire la règle qui la cache |
| `dec_t4_texte` | « …l'œuvre d'un grand peintre de langue allemande… » | la visite de découverte ne tourne qu'en de, es et pt (`lancerDecouverte()`) ; le portugais a son texte (`I18N_DECOUVERTE_PT`), l'espagnol le sien, sans nationalité (`I18N_ESPAGNOL`) | le japonais ou l'anglais reçoit sa visite (`contenuDecouverte()`, la garde de `lancerDecouverte()`) : écrire alors son `dec_t4_texte` et son `dec_t4_d5` (le tableau final) |
| `examen_aide_1` | « Trois référentiels d'allemand publient la liste du vocabulaire… » | l'écran `examenInfo` ne s'ouvre que par la clé « Essentiel » d'une carte (`marqueExamenCarte()`), qui exige une marque `pruefung` : `themes.json` en a 2 175, les données es, pt, en et ja aucune | une langue reçoit des marques d'examen dans ses données (`pruefung`) : écrire alors un `examen_aide_1` (et revoir `examen_aide_2`) qui nomme ses propres référentiels |

---

## 5. Sonde Playwright (lecture seule)

**Non lancée.** Le script est prêt, en lecture seule (aucune écriture Firestore, connexions à Google coupées) : il ouvre `index.html?apprendre=xx` pour les cinq langues, relève l'accueil, Tout le contenu, chaque panneau, l'entrée dans la séance, Écouter, le ciel, la galerie, la recherche (« aider », « helfen », « mit », « stehen », « obwohl »), le profil, et repère les mots allemands dans le texte visible. Il n'a pas tourné : le verrou du navigateur était pris, puis réservé à la maquette des quatre points (chef, 11 nov.).

À vérifier à l'écran par les sessions des lots (sous le verrou) :
- ja : la ligne « Aujourd'hui : <scène> » de la séance (`majAujourdhuiScene` 69414) montre-t-elle une scène allemande ?
- ja : le rendu de la feuille de conjugaison du jour (A1-A2) ;
- ja : le ciel à la fin de Premiers pas (`etatCielFin` 60983) ;
- es : chercher « aider » sort-il « helfen » ? ja : « mit » dans Tout le contenu → « Chercher dans les mots » ;
- pt : le tableau en plein écran dit-il « peintre du monde germanophone » ?
- en : aucune scène dans la séance A1.

---

## 6. Limites

- Les numéros de ligne valent pour `index.html` v1159 (`db2133f`).
- Le contenu (qualité des phrases, justesse des traductions) n'est pas jugé ici, seulement sa présence.
- Ni les règles Firestore publiées en console, ni le nombre de fichiers par dossier `audio/mp3/*` n'ont été vérifiés.
- Les écrans réservés à l'admin (essais, tableau de bord) n'ont été lus que dans le code.
