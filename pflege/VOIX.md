# Wortando Pflege : la liste unique des voix

Tenue par la session « dialogues, grammaire, écrit » (demande du chef, 14 nov. 2026). **Rien n'est
généré** : choix et chiffrage seulement, à valider par le chef avant toute dépense. Toutes les voix sont
des voix **ElevenLabs déjà retenues dans le projet**, modèle **multilingual v2, jamais Flash** (règle de
Jacques du 12 oct.). Les noms des personnages : `pflege/sources/noms.json` (la liste unique des noms).

## Les voix disponibles (aucune voix nouvelle)

Reprises du telc A2·B1 (`visuel/prototype/telc/donnees/hoeren.json`, bloc `voix`), où elles ont été
conçues ou choisies par Jacques le 6 nov. 2026, plus Aurora, la voix de tout le corpus allemand.

| Clé | Voix | voice_id | Sexe, âge |
|---|---|---|---|
| `aurora` | Aurora – Warm Narrator (le corpus, les consignes) | `8HePnvwzEdJ614CQMPqF` | f, 35 |
| `f_jung` | « Wortando - telc f_jung » | `KdxIdEwcPWzvsuKFEGL2` | f, 20-25 |
| `f_mittel` | la Dame du DTZ (épisode 03) | `N85Zhun98cg4usHJ1afQ` | f, 40-45 |
| `f_reif` | Frau Brandt du DTZ (clé `brandt` au telc) | `cDlEZdkTayS2jHnyaXx6` | f, 55 |
| `f_alt` | « Wortando - telc f_alt » | `VTPbgxY1fFa6FwTfzLEB` | f, 70-75 |
| `radio_f` | « Wortando - telc radio_f » | `eynqyfGtOX7SMOw161Ca` | f, 35 |
| `m_jung` | « Wortando - telc m_jung » | `YsKUFZvQZDgRvcfwUT4X` | m, 18-22 |
| `radio_m` | « Wortando - telc radio_m » | `KMSBmY3yNdCjbnsEvXc6` | m, 40 |
| `m_mittel` | le Beamte du DTZ (épisode 02) | `lwbCRuiP1VdfP1CRfjHk` | m, 45-50 |
| `m_alt` | Herr Brückner, le Nachbar du DTZ (épisode 05) | `o66wtFhUpq7rflsMnh38` | m, 65-70 |

Écartées : les voix de **Mark** (`J8ovlSvQ5WTDCCxIM8U0`) et d'**Anna** (`92qyovlOYJE0EVmWB0fA`), personnages
d'une autre série que l'apprenant connaît ; et la clé telc `brandt` est renommée ici `f_reif`, pour ne pas la
confondre avec **Herr Brandt**, le patient.

## La règle du partage

Quatorze personnages pour dix voix : **une voix peut servir à deux personnages qui ne se croisent jamais**,
parce qu'ils vivent dans des lieux différents (l'hôpital, la maison de retraite, le domicile). Deux
personnages d'un même lieu, ou d'une même pièce d'examen, ont toujours deux voix différentes.

## Les personnages de la série

| Personnage (id de `noms.json`) | Lieu | Voix | Partagée avec (autre lieu) |
|---|---|---|---|
| **Elif** (`elif`), 29 ans, l'héroïne | Klinikum | `f_jung` | — (à elle seule) |
| **Jonas** (`jonas`), 38 ans, tuteur | Klinikum | `radio_m` | Arun (Lindenhof) |
| **Frau Hoffmann** (`hoffmann`), 52 ans, cadre | Klinikum | `f_reif` | — |
| **Dr. Sommer** (`sommer`), 40 ans, **une femme** | Klinikum | `radio_f` | Amira (domicile) |
| **Dr. Krämer** (`kraemer`), médecin de garde, un homme | Klinikum (nuit, téléphone) | `m_mittel` | — |
| **Yusuf** (`yusuf`), 34 ans | Klinikum (nuit) | `m_jung` | — |
| **Herr Brandt** (`brandt`), 82 ans | Klinikum | `m_alt` | Herr Schulze (Lindenhof) |
| **Frau Lehmann** (`lehmann`), 74 ans | Klinikum | `f_alt` | Frau Weber (Lindenhof), Frau Kowalski (domicile) |
| **Frau Krüger** (`lehmann_tochter`), sa fille, ≈ 50 ans | Klinikum | `f_mittel` | Olena (Lindenhof) |
| **Arun** (`arun`), 31 ans | Haus Lindenhof | `radio_m` | Jonas (Klinikum) |
| **Olena** (`olena`), 44 ans | Haus Lindenhof | `f_mittel` | Frau Krüger (Klinikum) |
| **Herr Schulze** (`schulze`), 87 ans | Haus Lindenhof | `m_alt` | Herr Brandt (Klinikum) |
| **Frau Weber** (`weber`), 81 ans | Haus Lindenhof | `f_alt` | Frau Lehmann, Frau Kowalski |
| **Amira** (`amira`), 26 ans | soins à domicile | `radio_f` | Dr. Sommer (Klinikum) |
| **Frau Kowalski** (`kowalski`), 79 ans | domicile | `f_alt` | Frau Lehmann, Frau Weber |
| *Redemittel, questions d'écoute, grammaire* | — | `aurora` | comme tout le corpus |

Défaut connu : Yusuf (34 ans) sur une voix de 18-22 ans, et Amira (26 ans) sur une voix de 35 ans. Si
l'oreille de Jacques le juge gênant, une voix « m, 30-35 » et une « f, 25-30 » se conçoivent comme celles du
telc (le 6 nov.) ; ce serait alors un petit lot à part, annoncé au chef.

## Les rôles propres à l'examen (proposés par pflege-examen, à valider)

| Rôle | Proposition de l'examen | Ma recommandation |
|---|---|---|
| la Prüferin de l'oral (« Frau Neumann ») | `f_reif` | **`aurora`** : `f_reif` est Frau Hoffmann, qui parle aussi dans l'écoute de l'examen ; Aurora, la voix neutre des consignes, convient à une examinatrice |
| le médecin de garde au téléphone (`kraemer`) | `radio_m` | **`m_mittel`** : c'est le Dr. Krämer de la série (dialogue 7) ; `radio_m` est Jonas |
| la fille de Frau Lehmann (« Sabine Wendt ») | `f_reif` | **`f_mittel`**, et le nom de la série : **Frau Krüger**, id `lehmann_tochter` (nom validé par le chef) |
| Dr. Sommer | `m_mittel`, en homme | **`radio_f`** : **Dr. Sommer est une femme** (« die Ärztin ») |
| le laboratoire (`aksoy`), la pharmacie (`richter`), le transport (`lorenz`) | `f_mittel`, `m_mittel`, `m_jung` | d'accord, **sauf** dans une pièce où parle aussi Frau Krüger / Olena (`f_mittel`), Dr. Krämer (`m_mittel`) ou Yusuf (`m_jung`) : prendre alors une voix libre de la pièce |
| les consignes | `aurora` | d'accord |

## Le chiffrage (dialogues et grammaire de cette session)

Caractères allemands **distincts** à dire, nombres déjà en lettres (`python tests/pflege_dialogues.py
--chars`) ; 1 caractère = 1 crédit en v2. Coût d'après le tarif retenu au PLAN § 6.2 (≈ 21 $ pour
125 000 caractères, soit ≈ 0,17 $ les 1 000), plus 30 % de reprises.

| Voix | Toutes les branches | Chemin modèle + Redemittel + écoute |
|---|---|---|
| `f_jung` (Elif) | 11 688 | 5 265 |
| `radio_m` (Jonas 874 + Arun 3 131) | 4 005 | 1 996 |
| `f_reif` (Hoffmann) | 437 | 355 |
| `radio_f` (Sommer 0 en dialogue + Amira 1 432) | 1 432 | 706 |
| `m_mittel` (Krämer) | 586 | 302 |
| `m_jung` (Yusuf) | 1 839 | 804 |
| `m_alt` (Brandt 2 609 + Schulze 1 320) | 3 929 | 2 392 |
| `f_alt` (Lehmann 733 + Weber 464 + Kowalski 580) | 1 777 | 1 342 |
| `f_mittel` (Krüger 786 + Olena 1 428) | 2 214 | 1 197 |
| `aurora` (Redemittel et écoute 7 353 + grammaire 12 362) | 19 715 | 19 715 |
| **Total** | **47 622** | **34 074** |
| Coût (+ 30 % de reprises) | ≈ 8,0 $ (≈ 10,4 $) | ≈ 5,7 $ (≈ 7,4 $) |

- « Toutes les branches » fait entendre chaque réponse, juste ou fausse, et chaque réaction ; « chemin
  modèle » ne fait entendre que la conversation modèle (écouter, remettre dans l'ordre, jouer son rôle),
  les autres branches restant écrites.
- Le PLAN (§ 6.2) prévoyait ≈ 15 000 caractères de dialogues et ≈ 15 000 de grammaire, soit 30 000 : la
  variante « chemin modèle » dépasse de 14 % (dans la marge de 20 %), **« toutes les branches » de 59 %**,
  ce qui demande un nouvel accord (règle Q7).
- Recommandation : **« chemin modèle » d'abord**, puis les autres branches si l'usage le justifie.
- Avant toute génération : les lectures des nombres (`"lecture"` dans `pflege/datos/`) versées dans
  `audio/lectures/de.json`, puis `python audio/controler_sons.py --dossiers de` après la génération.

## Ce qui est fait (14 nov. 2026)

Lot « chemin modèle » généré : 775 fichiers, 845 clés (`pflege/datos/sons.json`), ≈ 34 504 crédits v2.
547 fichiers sont dits par Aurora (questions d'écoute et leurs choix, Redemittel, toute la grammaire) ;
les personnages ne parlent que dans les clés `r/…`. Fichiers par voix (hauteur médiane mesurée) :
`m_alt` 55 (113 Hz), `radio_m` 32 (130 Hz), `m_mittel` 8 (144 Hz), `m_jung` 7 (110 Hz) ; `f_jung` 58,
`f_alt` 33, `f_mittel` 20, `radio_f` 8, `f_reif` 7 ; `aurora` 547 (211 Hz). Les voix d'homme sont bien des
voix d'homme. Planche d'écoute (une réplique par personnage) : `Downloads/pflege/voix-personnages/`.

## L'accent d'origine des soignants (décision de Jacques du 14 nov., en préparation)

« Les personnes doivent parler avec leur accent d'origine » → « Oui, vas-y avec l'accent léger ». Les cinq
soignants venus d'ailleurs parlent un allemand clair et correct, avec un accent **léger mais audible** :
Elif (turc), Yusuf (arabe syrien), Amira (arabe tunisien), Arun (malayalam, Kerala), Olena (ukrainien).
L'équipe allemande, les patients et l'examen blanc gardent leurs voix, sans accent.

**Le soignant est le rôle de l'apprenant** dans chaque dialogue : 98 de ses 100 répliques du chemin
modèle sont aussi des phrases que l'apprenant choisit et redit. D'où **deux fichiers pour ces répliques** :
- la voix **neutre** déjà faite, gardée pour « à répéter » et « jouer son rôle » (clé `<id>/r/<n>`) ;
- la voix **à accent**, nouvelle, pour écouter la conversation (clé `<id>/ra/<n>`, à ajouter au contrat
  avec l'architecture).

Voix : **conçues par Voice Design** (`audio/concevoir_voix.py`), comme celles du telc, et non prises dans
la bibliothèque (une voix conçue n'appartient à personne ; la clé du projet ne lit d'ailleurs pas la
bibliothèque, erreur 401). Une description par personnage, texte d'essai = une vraie réplique de lui ; trois
aperçus, choix à l'oreille par Jacques, puis la voix gardée dans le compte et un essai en multilingual v2.

| Personnage | Clé prévue | Texte d'essai (réplique réelle) |
|---|---|---|
| Elif | `elif_tr` | d01 : « Guten Morgen, Herr Brandt. Mein Name ist Elif, … Wie haben Sie heute Nacht geschlafen? » |
| Yusuf | `yusuf_ar` | d07 : « Ich mache mir Sorgen. Sein Zustand hat sich in der letzten Stunde deutlich verschlechtert. … » |
| Amira | `amira_ar` | d10 : « Ein hoher Blutdruck ist schlecht für das Herz. Die Tablette senkt den Blutdruck … » |
| Arun | `arun_ml` | d12 : « Das klingt schön. Wissen Sie, jetzt ist noch mitten in der Nacht. … » |
| Olena | `olena_uk` | d09 : « Heute gibt es Kartoffelsuppe und danach Hähnchen mit Püree. … » |

Chiffrage :
- **essais** : 5 conceptions (trois aperçus chacune, sur 104 à 139 caractères) puis 5 répliques en v2,
  environ 500 à 1 500 crédits (le prix des aperçus se mesure au premier) ;
- **refonte** : les 100 répliques à accent des cinq soignants (Elif 58, Arun 17, Olena 10, Amira 8,
  Yusuf 7), **8 819 caractères, soit ≈ 8 800 crédits** (≈ 1,5 $), les fichiers neutres restant tels quels.
Rien n'est lancé sans l'autorisation de Jacques écrite dans la session.

## Les 14 dialogues de plus, d13 à d26 (mandat B, chiffrage du 15 nov. 2026)

Mesuré à blanc par `python pflege/outils/voix.py` (rien n'est dépensé), sur le même périmètre que le premier
lot : chemin modèle, Redemittel et questions d'écoute, nombres en lettres, fichiers déjà faits déduits.

| Ce qui est dit | Caractères |
|---|---|
| Répliques du chemin modèle (`r/…`) | 24 769 |
| Redemittel (`rm/…`, Aurora) | 5 627 |
| Questions d'écoute et leurs choix (`q/…`, Aurora) | 5 037 |
| **Total à produire** : 529 fichiers distincts | **≈ 35 300 crédits** |
| Coût | **≈ 6,0 $** (≈ 7,8 $ avec 30 % de reprises ; le premier lot en a demandé 2 %) |

- Par voix : `f_jung` (Elif) 12 456, `aurora` 10 555, `f_reif` (Hoffmann, Frau Aksoy, Monika Schulze)
  2 457, `f_mittel` (Frau Krüger, Olena) 2 456, `radio_m` (Jonas, Arun) 2 407, `radio_f` (Dr. Sommer) 1 403,
  `f_alt` (Frau Lehmann) 1 315, `m_alt` (Herr Brandt, Herr Schulze) 1 118, `m_jung` (Yusuf) 730,
  `m_mittel` (Herr Richter) 427.
- **Plus que les ≈ 4 $ du plan** (« la moitié du chemin modèle ») : les dix dialogues B2 ont des
  répliques plus longues (la visite, le téléphone, la sortie), et le lot est en fait de la taille du
  premier (≈ 34 500 crédits). C'est au-delà des 20 % de l'estimation : **nouvel accord nécessaire** (règle 9).
- Trois rôles de l'examen parlent hors de l'examen, avec une voix déjà au compte : Frau Aksoy (labo) et
  Monika Schulze en `f_reif`, Herr Richter (pharmacie) en `m_mittel` (`pflege/sources/voix.json`). Aucune
  des deux ne croise l'autre voix `f_reif` (Frau Hoffmann) dans un même dialogue. À aligner avec l'examen
  blanc s'il leur a donné d'autres voix.
- **Si l'accent des soignants est retenu** (section précédente), leurs répliques de d13-d26 demandent en plus
  leur fichier à accent (`ra/…`) : Elif 12 456, Olena 1 479, Arun 1 047, Yusuf 730 caractères, soit
  **≈ 15 700 crédits (≈ 2,7 $)**, et 0 pour Amira (absente de d13-d26). Les fichiers neutres restent
  nécessaires (« à répéter », « jouer son rôle ») : la part à accent s'ajoute, elle ne remplace rien.
- Rien n'est lancé : ni le lot, ni sa part à accent. C'est le chef qui le présente à Jacques.
