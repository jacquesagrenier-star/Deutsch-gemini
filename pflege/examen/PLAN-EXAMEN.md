# L'examen blanc telc Deutsch B1·B2 Pflege, modèle 1 : le plan

14 nov. 2026, session « pflege-examen ». Format et barème : [../FORMAT-TELC-PFLEGE.md](../FORMAT-TELC-PFLEGE.md).
Personnages : [../PERSONNAGES.md](../PERSONNAGES.md) (proposition en cours de validation : les noms se remplacent
dans les données sans toucher au code).

**Droits d'auteur** : le FORMAT du telc (parties, nombre de questions, durées, barème), jamais son contenu. Les sujets
ci-dessous ont été choisis pour **ne recouvrir aucun sujet du test modèle** (qui traite, entre autres, d'une
arthrite après une prothèse de hanche, d'une solution d'électrolytes, des mesures de contention, d'un groupe de
travail sur la documentation, d'un rapport de nuit en accueil temporaire, du travail en long séjour ou en soins
aigus, de la coopération entre collègues et avec les médecins, de la responsabilité dans les soins techniques, de la
distance dans les soins de base, d'une formation obligatoire sur les proches).

## Où vivent les fichiers

| fichier | rôle |
|---|---|
| `visuel/prototype/telc/pflege/pflege.html` | la page (accueil, entraînement par épreuve, examen blanc complet) |
| `visuel/prototype/telc/pflege/pflege-examen.js` | le module : questions, écrit, oral, enchaînement, verdict |
| `visuel/prototype/telc/pflege/bareme.js` | le calcul du niveau et du certificat, pur (lu aussi par le contrôle) |
| `visuel/prototype/telc/pflege/donnees/examen-1.json` | l'examen : allemand, plus le français et l'anglais des aides |
| `visuel/prototype/telc/pflege/donnees/interface.json` | les textes de l'interface, fr et en |
| `visuel/prototype/telc/pflege/donnees/langues/<l>.json` | tr, uk, fa, ar, pt, pl, ru : interface et aides |
| `visuel/prototype/telc/pflege/donnees/voix-pflege.json` | le manifeste des pistes enregistrées (vide tant que rien n'est produit) |
| `visuel/prototype/telc/pflege/outils/voix_pflege.py` | à blanc : le chiffrage ; `--pour-de-vrai` après accord |
| `tests/pflege_examen.py` | le contrôle |

**Réutilisé tel quel, sans rien y changer** : `../../dtz/commun.css` et `commun.js` (voix, pistes, lecteur unique iOS,
chronomètre, panneau, stockage, `parler()` vers l'app), `../telc-commun.js` (`textesTelc`, champs traduits),
`../langues/<l>.js` (les mots communs : Continuer, Fermer…), `../../dtz/outils/voix.py` (la fabrication des pistes
ElevenLabs v2, comme `../outils/voix_ecouter.py`). `examen-blanc.js` du telc A2·B1 n'est **pas** réutilisé : ses étapes et
son barème sont écrits en dur pour l'A2·B1 ; le modifier changerait l'A2·B1. Le module Pflege a son propre
enchaînement, sur les mêmes briques.

## Le déroulé de l'examen blanc

1. **Hören** (≈ 25 min, suit l'enregistrement, chaque texte une seule fois) : items 1-23.
2. **Lesen + Sprachbausteine** (60 min ensemble, dans l'ordre qu'on veut) : items 24-59.
3. **Schreiben** (30 min) : A ou B, 120-170 mots.
4. **Vorbereitung** (20 min) : les fiches des parties 2 et 3 de l'oral, notes permises.
5. **Sprechen** (≈ 16 min) : 1A, 1B, 2A, 2B, 3, avec la Prüferin et Elif comme partenaire.
6. **Les grilles** : l'écrit (contenu calculé sur la fiche, les trois autres critères à l'aide de descripteurs) et
   l'oral (tâches estimées sur ce qui a été dit, langue à l'aide de descripteurs), puis le **verdict** : les trois
   résultats partiels et le certificat (B2, B1 ou aucun ; l'oral décide).

## Les sujets

### Hören (23)

| partie | items | sujet |
|---|---|---|
| T1, exemple | 0 | Jonas laisse un message à Elif : son service de demain change |
| T1 | 1 | le laboratoire : la prise de sang de Herr Brandt est inutilisable, à refaire avant 10 h |
| T1 | 2 | la pharmacie de l'hôpital : une rupture de stock, un produit de remplacement et ce qu'on fait d'ici là |
| T1 | 3 | la fille de Frau Lehmann : elle ne vient pas aujourd'hui, ce qu'elle apportera, ce qu'elle demande |
| T1 | 4 | le transport sanitaire : le départ de Herr Brandt en rééducation déplacé, les papiers à préparer |
| T2, gespräch 1 | 5-6 | Dr. Sommer et Elif pendant la visite : la douleur de Herr Brandt, le traitement changé, la kiné |
| T2, gespräch 2 | 7-8 | Elif et Frau Lehmann : la glycémie avant le petit-déjeuner, la peur de la piqûre, le pansement du pied |
| T2, gespräch 3 | 9-10 | Olena et Herr Schulze (Haus Lindenhof) : il veut « aller au travail », elle l'accompagne sans le contredire |
| T2, gespräch 4 | 11-12 | Amira chez Frau Kowalski : le stylo à insuline, le réfrigérateur, une dose oubliée, le médecin de famille |
| T2, gespräch 5 | 13-14 | Yusuf appelle le médecin de garde la nuit (fièvre, tension) : ce qui est prescrit, quand il vient |
| T3 | 15-20 | réunion d'équipe (Frau Hoffmann, Jonas, Elif) : Herr Brandt et le risque de chute, une patiente en chambre d'isolement, la documentation sur tablette, la formation de mardi |
| T4, exemple + | 21-23 | quatre collègues (Jonas, Arun, Olena, Yusuf) : les proches doivent-ils aider aux soins à l'hôpital ? six phrases a-f, deux en trop |

### Lesen (18)

| partie | items | sujet |
|---|---|---|
| T1 | 24-27 | quatre courriels du Klinikum am Kanal (vaccin contre la grippe du personnel, souhaits pour le planning de décembre, nouveaux distributeurs de désinfectant, cours d'allemand au travail) et six objets, dont deux pièges |
| T2 | 28-32 | **plan de soins de Frau Lehmann selon les AEDL de Krohwinkel** (diabète de type 2, plaie au pied, mauvaise vue) : extrait du rapport d'admission, huit lignes a-h, cinq phrases dont une sans ligne (X) ⚕️ |
| T3 | 33-38 | trois textes : la notice d'un antalgique courant ; une note de service (gastro-entérite à norovirus : visites et hygiène des mains) ; une consigne sur le secret professionnel et les renseignements au téléphone ⚕️ |
| T4 | 39-41 | un texte d'information : le programme d'intégration des soignants venus de l'étranger (tutorat, cours, reconnaissance) |

### Sprachbausteine (18)

| partie | items | sujet |
|---|---|---|
| T1 | 42-49 | le rapport du matin sur Herr Brandt, 8 trous, 10 mots (connecteurs, adverbes, liens de temps et de cause) |
| T2 | 50-59 | le rapport du soir sur Frau Lehmann, 10 trous à trois choix : le vocabulaire des rapports de soins ⚕️ |

### Schreiben (20)

- **A, Aufnahmebericht** : Herr Brandt, 82 ans, admis en gériatrie après une prothèse de hanche posée à la suite d'une
  chute ; une fiche d'anamnèse cochée et annotée, rangée par AEDL (lunettes, appareil auditif d'un côté, orientation,
  déambulateur, aide partielle, boit peu, prothèse dentaire, se lève la nuit, dort mal à cause de la douleur, veuf, un
  fils loin, ses habitudes). ⚕️
- **B, Biografiebericht** : Herr Schulze, 87 ans, Haus Lindenhof, démence modérée ; une fiche biographique (enfance,
  quarante ans conducteur de tramway, sa femme, sa fille, le skat, les chansons, le jardin ouvrier, ses habitudes du
  matin, ce qu'il n'aime pas, l'agitation de fin d'après-midi).
- La fiche est découpée en informations avec leurs mots repères : le **contenu** se calcule (toutes reprises = 5 ; trois
  oubliées font perdre un cran) ; forme, correction et vocabulaire se notent avec les descripteurs du telc, reformulés,
  et un texte modèle montre ce qu'on attendait.

### Sprechen (100)

| partie | sujet |
|---|---|
| 1A | une photo : une soignante aide une résidente à marcher avec son déambulateur dans un couloir (fiche B : une soignante sert le repas à un résident en fauteuil) — **images à faire après la validation des personnages** ; d'ici là, une description écrite |
| 1B | « la mobilisation et la prévention des chutes » (fiche B : « boire et manger quand on est âgé ») ; questions B1 et B2 |
| 2A | au choix : « reconnaître la douleur chez une personne qui ne peut pas la dire » ou « le travail posté et la santé des soignants », mots-clés et trois photos décrites |
| 2B | une ou deux questions de la Prüferin sur l'exposé |
| 3 | discussion avec Elif : Haus Lindenhof veut accueillir un chien de thérapie ; phrases d'appui pour et contre |

L'app joue la Prüferin (Frau Neumann, un personnage de plus) et la partenaire (Elif, qui passe l'examen elle aussi).
Le micro écoute ce que l'apprenant dit (ou il l'écrit) ; les points de **tâche** s'estiment sur ce qui a été dit
(durée, plan annoncé, points traités, avis, questions posées à la partenaire…), ceux de **langue** à l'aide des
descripteurs. Un exposé lu ne dépasse pas A2 : l'app le rappelle, elle ne peut pas le voir.

## La voix

Les consignes (Aurora), les 23 items de l'écoute et ce que disent la Prüferin et Elif à l'oral. Chiffrage par
`outils/voix_pflege.py` à blanc, une fois les textes écrits ; **rien n'est produit avant l'accord du chef**. Les
voix : celles du telc A2·B1 déjà conçues (Aurora, f_jung, f_mittel, f_alt, m_jung, m_mittel, m_alt, radio_f,
radio_m, brandt), à harmoniser avec les voix que la session des dialogues donnera à Elif, Jonas et l'équipe.

## Ce qu'une infirmière devra valider (`relire: true`)

Tout ce qui est marqué ⚕️ ci-dessus, plus chaque rapport, la notice, les prescriptions du médecin de garde et les
descripteurs de l'écrit. Liste tenue dans `RELIRE-EXAMEN.md` (à venir).
