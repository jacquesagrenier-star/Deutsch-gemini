# Wortando Pflege — plan de la phase 0

*Cadrage du 13 nov. 2026. Aucun code, aucune dépense. À valider par Jacques (via le chef
d'orchestre) avant la phase 1.*

Une **section « Soins »** dans l'app Wortando (allemand), ouverte par **licence**, vendue aux
agences de recrutement et aux employeurs de soignants étrangers, pour mener leurs recrues au
**B1-B2** et au **telc Deutsch B1·B2 Pflege**. C'est la piste 1 de la page « Trois pistes »
(https://claude.ai/artifact/5J6RVTSuFFUPf9GjtuPcSV).

Page de présentation pour Jacques (privée) : https://claude.ai/artifact/EBtWZGJwrKJ5Cto37Ctbdn

Annexes (le contenu, en listes réelles) :

- [A — les dix thèmes de vocabulaire](annexes/A-THEMES.md) : 430 entrées, niveau par niveau
- [B — les huit scènes et les personnages](annexes/B-SCENES.md)
- [C — les douze dialogues](annexes/C-DIALOGUES.md)
- [D — la grammaire du métier et l'écrit](annexes/D-GRAMMAIRE-ECRIT.md)

Convention : tout chiffre suivi d'une URL est sourcé (consulté le 13 nov. 2026) ; « estimation »
marque ce qui ne l'est pas ; ⚕️ marque ce qui demande la relecture d'une infirmière.

---

## ✦ Décisions de Jacques du 14 nov. 2026 (elles priment sur la suite du plan)

Consignées dans `decisions/DECISIONS.md` (« Wortando Pflege : les décisions de lancement »).

| Question | Décision | Ce que cela change ici |
|---|---|---|
| Q1 Test modèle | **Téléchargé** (ZIP et manuel, depuis telc.net, hors du dépôt) | Format et barème exacts : [FORMAT-TELC-PFLEGE.md](FORMAT-TELC-PFLEGE.md) ; le § 1.2 ci-dessous est dépassé |
| Q2 Personnages | De nouveaux soignants, d'après les pays qui recrutent **aujourd'hui**, **un personnage turc obligatoire** | Nouvelle distribution proposée : [PERSONNAGES.md](PERSONNAGES.md) (Elif, Amira, Arun, Yusuf, Olena), **à valider avant toute image** ; l'annexe B sera mise à jour après |
| Q3 MVP | **Pas de MVP : la grande version tout de suite** | § 7.2 abandonné ; nouveau calendrier ci-dessous |
| Q4 Licence | « On verra comment on va le gérer » : pendant le travail, **l'admin ouvre les Soins compte par compte** (`essais: ["soins"]`) | **Pas** de codes d'agence ni de Cloud Function pour l'instant (§ 4.3 points 2 et 3 en attente) ; le tableau de bord de la grande version vit d'abord **dans le tableau de bord admin** |
| Q5 Contenu lisible | (non tranché séparément : suit Q4) | les fichiers restent servis comme le reste |
| Q6 Langues | Les **9 langues d'interface actuelles** | pas d'espagnol d'interface pour l'instant |
| Q7 Dépenses | **Go** pour les images (fal) et les voix (ElevenLabs v2, jamais Flash) du plan | chaque lot **annoncé au chef avec son coût** avant d'être lancé ; une dépense hors plan, ou un lot qui dépasse son estimation de plus de 20 %, demande un nouvel accord ; l'infirmière relectrice et le juriste sont l'affaire de Jacques : profils dans [PROFILS-RELECTURE.md](PROFILS-RELECTURE.md) |
| Q8 Espagnol | Recommandation gardée : scènes neutres, l'espagnol médical américain plus tard | — |
| Validation par les agences | « Je le ferai sans l'avis de 2 ou 3 agences, j'irai de l'avant » | § 7.3 sans objet |

### Le calendrier de la grande version (estimation)

| Phase | Contenu | Durée | Après |
|---|---|---|---|
| 1 · Architecture | Ouverture par l'admin (`essais` « soins »), garde, tuile et panneau, chargement de `pflege/datos/`, séance, premier thème, contrôles | 1-2 sem. | — |
| 2 · Contenu texte | Les **10 thèmes** (430 entrées, phrases d'exemple, 9 langues), les **12 dialogues**, les **21 points** de grammaire et leurs séries, l'écrit (12 sujets) | 5-6 sem. | phase 1 |
| 3 · Scènes | Planche d'essai (3 images), puis les **8 scènes** et leurs couches ; personnages validés d'abord | 3-4 sem., en parallèle de la phase 2 | Q2 validée |
| 4 · Examen blanc | **Deux examens complets** au format exact (59 questions, écrit A / B, oral sur 100, calcul du certificat B1 / B2), audio des écoutes | 3-4 sem. | phase 2 avancée |
| 5 · Suivi | Dans le tableau de bord admin : la cohorte « Soins », progression, « prêt pour l'examen » (seuils du telc), alertes, export CSV ; l'accès d'une agence plus tard | 2 sem. | phases 1 et 4 |
| 6 · Relecture | Infirmière et langues, au fil des lots | continue | une relectrice trouvée par Jacques |

Fin estimée : **fin février 2027** si la phase 3 tourne en parallèle (une session à part, que je
proposerai au chef), **fin mars** sinon. Coût du plan complet inchangé : ≈ 30 $ d'images, ≈ 27 $ de
voix (§ 6).

---

## 0. En une page

**Le besoin est réel et payé par l'employeur.** L'Allemagne emploie 353 000 soignants étrangers
(20 % de la profession) et reconnaît environ 32 000 diplômes de soins étrangers par an. Pour
obtenir le titre d'infirmier (Berufsurkunde), **B2 est exigé dans tous les Länder** depuis 2023.
85 à 90 % des recrutements passent par des **agences privées**, et la loi fait payer la formation
linguistique par l'employeur. Les cours d'État (Berufssprachkurse du BAMF) sont **restreints en
2025-2026** faute de budget.

**Ce que vise la section** : le passage **B1 → B2 Pflege**, en Allemagne ou juste avant le départ,
là où l'apprenant travaille déjà et n'a que des bribes de temps. Wortando ne remplace pas le cours
(400 à 600 heures) : il est **le travail quotidien entre deux cours**, avec un suivi que l'agence
voit. C'est ce que ni les apps gratuites (Ein Tag Deutsch, vhs Pflege) ni les cours en direct
(Lingoda Healthcare, iQ Lingua) n'offrent ensemble.

**Ce qui existe déjà et sert tel quel** : le moteur de séance, la répétition espacée, les scènes à
toucher, les thèmes illustrés, l'oral à verdict, le module telc A2·B1 (examen blanc), les 9
langues d'interface, les codes d'invitation, le tableau de bord admin, l'ouverture d'un essai à un
compte (champ `essais`). 247 mots de santé sont déjà au corpus (Gesundheit, Körperteile, un thème
C1 « Pflege und Betreuung »), et trois scènes médicales (cabinet, pharmacie, examen).

**Ce qui manque** : le monde de l'hôpital (430 entrées de vocabulaire, 8 scènes, 12 dialogues, 21 points de
grammaire, l'écrit d'admission), l'examen blanc au format Pflege, la licence, le tableau de bord
de l'agence.

**Le MVP pour un pilote** (§ 7) : 3 scènes, 3 thèmes, 10 dialogues, 1 examen blanc partiel, le
tableau de bord minimal, relu par une infirmière. **Environ 9 à 11 semaines**, prêt fin janvier
2027 si les accords arrivent vite (estimation). Dépense du MVP : **≈ 15 $ d'images, ≈ 10 $ de voix,
400 à 1 000 € de relecture** (estimations, § 6).

**Et l'espagnol ?** (§ 8 bis) : l'Espagne recrute surtout des soignants qui parlent déjà
espagnol, le marché y est petit. L'« espagnol médical » pour les soignants américains est un vrai
marché, à prendre **en second**, avec la même mécanique.

**Accords demandés à Jacques** : voir § 9 (huit questions, dont le téléchargement du test modèle
telc, le choix des personnages et la place de l'espagnol).

---

## 1. L'examen : telc Deutsch B1·B2 Pflege

Sources officielles : page allemande https://www.telc.net/sprachpruefungen/zertifikatspruefung/deutsch/telc-deutsch-b1b2-pflege/
et anglaise https://www.telc.net/en/language-examinations/certificate-exams/german/telc-german-b1-b2-nursing/ ;
page de branche https://www.telc.net/deutsch-fuer-fachkraefte/branchenuebersicht/pflege/.

### 1.1 Le format

| Épreuve | Parties | Tâches | Durée | Source |
|---|---|---|---|---|
| **Hörverstehen** (écoute) | 4 | choix multiple, appariement | 25 min | telc |
| **Leseverstehen** (lecture) | 4 | choix multiple, appariement | 60 min **avec** les Sprachbausteine | telc |
| **Sprachbausteine** (éléments de langue) | 2 | appariement (cohérence de rapports) ; choix multiple de lexique (*non confirmé*) | (dans les 60 min) | telc ; détail non confirmé |
| **Schriftlicher Ausdruck** (écrit) | 1 | **au choix : un rapport d'admission (*Aufnahmebericht*) ou un rapport biographique (*Biografiebericht*)**, à partir d'une fiche | 30 min | telc |
| **Mündlicher Ausdruck** (oral) | 3 | 1. échange sur ses expériences ; 2. court exposé ; 3. discussion d'un sujet controversé | ≈ 16 min, en principe **à deux**, 20 min de préparation | telc |

- **Écrit : 1 h 55 sans pause** (25 + 60 + 30) — total donné par un centre d'examen
  (https://www.sprachenatelier-berlin.de/en/article/4028.telc-deutsch-b1-b2-pflege.html) ;
  oral le même jour après une pause, ou un autre jour.
- Examen sur papier, numérique ou hybride ; **pas d'examen partiel** (telc).
- **Détail de l'oral** selon un organisme de préparation, *non officiel*
  (https://aplora.org/de/blog/telc-pflege-b1-b2-sprechen-ueben/) : 1A décrire une photo du
  quotidien de soin (≈ 1 min), 1B questions de suivi, 2A exposé sur un sujet parmi deux
  (≈ 2 min), 2B questions, 3 discussion avec le partenaire (≈ 4 min).

### 1.2 Barème et niveaux : **à confirmer dans le test modèle**

Aucune page HTML de telc ne donne le barème. Ce qu'on en lit ailleurs est contradictoire :

- un organisme commercial (*non confirmé*) : écrit 165 points + oral 45 = 210, réussite à 60 % ;
  le niveau B1 ou B2 est attribué si l'oral et au moins une partie de l'écrit l'atteignent ; sous
  B1, un simple relevé de notes (https://deutsch-vorbereitung.com/en/pflege-telc-kurs-3.html) ;
- un centre de Munich qui cite le manuel telc : B2 = 75-100, B1 = 35-74,5 sur 100 (oral ou score
  converti ? *non confirmé*) (https://www.pet-sprachen.de/de/deutsch/deutsch-fuer-pflegekraefte/telc-pruefung-deutsch-b1-b2-pflege/).

Le certificat porte « telc Deutsch **B2** Pflege » ou « **B1** Pflege ». Prix : **190 à 199 €**
selon les centres (Berlitz Bielefeld 199 €, https://www.berlitz.com/de-de/erwachsene/sprachtests/deutsch/telc/pruefungstermine ;
Université de Mannheim 190 €, https://www.daf.uni-mannheim.de/en/?p=2181).

> **Accord demandé (§ 9, Q1)** : télécharger le **test modèle officiel** de telc, gratuit, pour
> relever le nombre d'items, les points et les seuils exacts de chaque partie :
> `https://www.telc.net/fileadmin/user_upload/mock_exams/Deutsch/telc_deutsch_b1-b2_pflege.zip`
> (Übungstest 1, avec l'audio) et/ou le manuel
> `https://www.telc.net/fileadmin/user_upload/pdfs/Handbuch_und_Tipps_fuer_Pruefungsvorbereitung/Deutsch_b1_b2_pflege_tipps_zur_Pruefungsvorbereitung.pdf`.
> Usage : **lire le format**, jamais recopier les textes (droits de telc). C'est un préalable à
> la phase 4 (examen blanc), pas aux phases 1 à 3.

### 1.3 Les examens voisins

- **Goethe-Test PRO Pflege** (B2) : lecture et écoute en ligne, adaptatives ; écrit de 75 min (un
  rapport d'admission + un message professionnel) ; oral à deux, dont **une transmission
  (Übergabe) simulée** ; B2 exigé dans les quatre parties (goethe.de, page en 403, lue par le
  moteur de recherche).
- **Fachsprachprüfung Pflege B2** : examen des Länder, né de la conférence des ministres de la
  Santé de 2019. **Berlin depuis juin 2024** (trois scénarios : entretien avec la personne
  soignée, rapport de soins ; telc et Goethe restent acceptés « jusqu'à nouvel ordre »,
  https://www.berlin.de/sen/wgp/presse/2024/pressemitteilung.1458029.php) ; Bavière annoncée
  comme alternative (https://www.lfp.bayern.de/specialist-language-test-healthcare-professions-bavaria/?lang=en).
  ⚠️ Tendance à surveiller : si les Länder passent à leur propre examen, la section doit préparer
  **aux situations** (entretien, admission, transmission) plus qu'au seul format telc. C'est le
  choix fait ici : les scènes et dialogues servent les trois examens ; seul l'examen blanc (§ 4.6)
  est propre à telc.

---

## 2. Le public et le marché

### 2.1 Qui recrute, qui paie

| Fait | Chiffre | Source |
|---|---|---|
| Salariés en soins | 1,76 M, dont **353 000 étrangers** (20 %) | BA, 8 mai 2026 : https://www.arbeitsagentur.de/presse/2026-16-tag-der-pflege-jede-fuenfte-pflegekraft-hat-auslaendische-staatsangehoerigkeit |
| Hôpitaux / soins aux personnes âgées | 734 000 (17 % d'étrangers) / 843 000 (24 %) | idem |
| Soignants étrangers par secteur | 41 % Altenpflege, 32 % Krankenpflege ; **48 % sont aides-soignants** (26 % chez les Allemands) | bpb 2025 : https://www.bpb.de/themen/migration-integration/kurzdossiers/581372/ |
| Canal | **85-90 % par des agences privées**, 10-15 % par la BA | BMG, 3 sept. 2026 : https://www.bundesgesundheitsministerium.de/themen/pflege/pflegekraefte/fachkraefteanwerbung-aus-drittstaaten |
| Triple Win (GIZ + BA) | > 8 000 placés depuis 2013, ≈ 400 établissements ; Inde, Indonésie, Philippines, Tunisie | GIZ, 23 oct. 2025 : https://www.giz.de/de/newsroom/storys/triple-win-pflegekraefte-deutschland |
| Label « Faire Anwerbung Pflege Deutschland » | ≥ 50 organisations (agences et établissements), dont Charité, MEDIAN, Caritas, Berlitz, Kolping | https://www.faire-anwerbung-pflege-deutschland.de/das-gütezeichen |
| Coût d'un recrutement Triple Win | 7 900 € TTC (8 495 € Kerala), cours jusqu'à B1 compris ; **+ ≈ 2 500 € pour le B2 en Allemagne** | brochure ZAV (PDF non ouvert, lu par extrait) |
| Coût total d'un recrutement privé | 10 000 à 15 000 € par soignant, dont 20-30 % de langue | **estimation** |

**Les acheteurs, par ordre de priorité proposé :**

1. **Les agences labellisées** (≈ 50) : elles portent la formation linguistique de dizaines à
   centaines de recrues par an et cherchent à réduire le taux d'échec au B2, qui retarde la
   Berufsurkunde (et le salaire plein).
2. **Les grands groupes hospitaliers et de soins aux personnes âgées** qui recrutent eux-mêmes
   (13 établissements labellisés en 2023, davantage aujourd'hui).
3. **Les écoles de langue partenaires** des agences, dans les pays d'origine et en Allemagne :
   Wortando en complément de leur cours, sous leur marque ou non.
4. **Les soignants eux-mêmes** (vente directe), plus tard : peu solvables avant le salaire
   allemand.

### 2.2 Les niveaux exigés

| Situation | Niveau | Source |
|---|---|---|
| Berufsurkunde Pflegefachfrau/-mann | **B2 dans tous les Länder** ; B2 général ou B2 Pflege, d'un membre de l'ALTE (telc, Goethe, ÖSD) | Bade-Wurtemberg : https://rp.baden-wuerttemberg.de/themen/bildung/ausbildung/seiten/faq-pflege-gesundheitsfachberufe/sprachkenntnisse/ ; Brême : https://www.service.bremen.de/dienstleistungen/anerkennung-als-pflegefachfrau-oder-pflegefachmann-mit-berufsqualifikation-aus-drittstaaten-beantragen-197554 |
| Hesse | B1 Pflege accepté **jusqu'au 1er janv. 2023**, B2 depuis | IQ Hessen 2022 (PDF, extrait) |
| Visa pour mesure d'adaptation (§ 16d AufenthG) | « suffisantes » : **A2 au minimum** | https://www.gesetze-im-internet.de/aufenthg_2004/__16d.html |
| Aide-soignant (§ 22a BeschV) | pas de niveau fédéral, droit des Länder | https://www.gesetze-im-internet.de/beschv_2013/__22a.html |

**Conséquence** : le parcours typique est **A0 → B1 dans le pays d'origine** (Triple Win et les
agences l'exigent avant le départ), puis **B1 → B2 en Allemagne**, en travaillant comme
assistant(e) pendant l'Anerkennung. Le telc B1·B2 Pflege est pensé pour ce second temps. D'où
les niveaux de la section : **A2 (rattrapage), B1 (cœur), B2 (objectif)**, C1 pour quelques
couches de scènes seulement.

### 2.3 Les cours existants et leur prix (nos concurrents et nos partenaires)

| Offre | Volume | Prix | Source |
|---|---|---|---|
| **Berufssprachkurs BAMF**, module spécial Gesundheitsfachberufe (vise B2, prépare telc Pflege et Goethe PRO Pflege) | 600 UE pour le module équivalent des professions académiques (*heures du module Pflege non trouvées*) | **gratuit** sous 33 462 € brut/an ; sinon **2,56 €/UE** (l'employeur peut en récupérer 50 %) | BA : https://www.arbeitsagentur.de/arbeitslos-arbeit-finden/sprachkurse ; tuenews, 5 août 2026 : https://tuenews.de/en/more-vocational-language-courses-starting-in-october/ |
| BAMF : restrictions 2025-2026 | plus d'A2, B1 rouvert au 1er oct. 2026 avec peu de places | — | idem |
| Goethe Philippines, super-intensif A1-B1 / B2 | 165 UE / 256 UE | 23 000 / 33 000 PHP | goethe.de (extrait) |
| Kerala, école privée en ligne, A1-B2 | 18-23 mois, ≈ 550-680 h | 35 000-50 000 INR + 15 500 INR d'examen par niveau | https://theplanbeta.com/blog/german-language-course-kerala-nurses-a1-b2-path-germany |
| Goethe Allemagne, « Deutsch in der Pflege » B1+ | 30 UE | 419 € (399 € en ligne) | goethe.de (extrait) |
| **Lingoda Healthcare** (B2B) | groupes de 5, 10 h en direct par module | sur devis | https://healthcare.lingoda.com/en/knowledge-base/onboarding-hub-für-pflegefachkräfte |
| **iQ Lingua** (B2B, cliniques et agences, assistant d'IA, centre telc) | — | sur devis | http://www.iq-lingua.de/en/company-offers/german-for-care-professionals/ |
| coLanguage Nursing A1-B2 | séances en direct | 30,90-36,90 € la séance | https://www.colanguage.com/course/german/nursing |
| Klett « Linie 1 Pflege B2 » numérique | manuel numérique | 29,99 € / 24 mois | https://www.klett-sprachen.de/linie-1-pflege-b2-digitale-ausgabe-allango/t-14/NP10060718300 |
| **Gratuits** : « Ein Tag Deutsch – in der Pflege » (IQ, B2), vhs Pflege (DVV), Commuio Health, Goethe « German for nursing care » (10 h) | — | 0 € | https://www.netzwerk-iq.de/en/offers/iq-good-practice/work-related-german-language-training/language-learning-app ; https://apps.apple.com/us/app/id6743324650 |

**Positionnement proposé** : ni un cours (on ne concurrence pas 600 heures d'enseignant), ni une
app gratuite de plus. **Le compagnon quotidien du cours, mesurable par l'employeur** : 15-20 min
par jour, l'oral et l'écoute que les cours n'ont pas le temps d'entraîner, l'examen blanc, et un
tableau de bord qui dit à l'agence qui décroche et qui est prêt. Prix de départ à tester : **10 à
30 € par apprenant et par mois** (page des trois pistes), à comparer aux ≈ 2 500 € du B2 en
Allemagne — c'est de l'ordre de **1 à 3 % du coût d'un recrutement**. Prix à valider en entretiens
(§ 7.3), **estimation**.

### 2.4 Les pays d'origine et leurs langues

| Fait | Chiffre | Source |
|---|---|---|
| Reconnaissances positives en soins | ≈ 32 500 (2024), ≈ 32 000 (2025) | Destatis, 19 août 2026 : https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/08/PD26_295_212.html |
| Demandes en soins par pays (2022, dernier détail en HTML) | Philippines 3 039, Tunisie 1 902, Inde 1 395 | https://www.zm-online.de/news/detail/gesundheitswesen-profitiert-am-meisten |
| En emploi, santé, sept. 2024 | Philippines 9 400, Inde 8 800 | https://mediendienst-integration.de/news/mehr-als-300000-auslaendische-pflegekraefte/ |
| Groupes de pays (BA, mai 2025) | pays Triple Win 52 000 (+10 000/an) ; Balkans occidentaux 51 000 (+4 000) | https://www.arbeitsagentur.de/presse/2025-21-tag-der-pflege-neue-pflegekraefte-kommen-vor-allem-aus-dem-ausland |
| Tendance 2025 (toutes professions) | demandes d'Égypte +88 %, du Maroc +45 % | BIBB : https://www.anerkennung-in-deutschland.de/html/de/pro/news-auswertung-anerkennungsstatistik-2025.php |
| Programme fédéral (terminé fin 2023) | surtout Mexique, Inde, Philippines | BMG (même page) |
| Besoin projeté | **280 000 à 690 000 soignants manquants en 2049** | Destatis : https://www.destatis.de/DE/Presse/Pressemitteilungen/2024/01/PD24_033_23_12.html |

Langues parlées (connaissance générale) : Philippines → anglais, filipino ; Inde → anglais,
malayalam, telugu ; Tunisie, Maroc → arabe et **français** ; Égypte, Jordanie, Syrie → arabe ;
Bosnie, Serbie → bosnien / serbe ; Albanie, Kosovo → albanais ; Turquie → turc ; Indonésie →
indonésien ; Vietnam → vietnamien ; Mexique, Colombie → **espagnol** ; Brésil → portugais.
Voir § 5 pour ce que cela implique.

**Taille du marché de la formation linguistique** : aucune étude publiée trouvée. Ordre de
grandeur : 25 000-35 000 personnes par an × 2 500-5 000 € de langue ≈ **60 à 175 M€ par an**
(**estimation**), aides-soignants non compris. Wortando n'en vise qu'une petite part : 1 000
apprenants payants à 15 €/mois pendant 8 mois ≈ 120 000 €/an (**estimation**, à titre d'échelle).

---

## 3. La carte du contenu

Le détail est dans les annexes ; ici, le périmètre et les chiffres.

| Bloc | Volume | A2 | B1 | B2 | Annexe |
|---|---|---|---|---|---|
| Thèmes de vocabulaire | 10 thèmes, 430 entrées (78 ⚕️) | 104 | 170 | 156 | A |
| Scènes illustrées | 8 scènes, ≈ 160 objets, 5 couches (A2, B1, B2, C1, Situation) | ✓ | ✓ | ✓ | B |
| Dialogues | 12 (+ 4 en réserve) | 2 | 6 | 4 | C |
| Grammaire du métier | 21 points, une fiche + une série de 10 chacun | 6 | 10 | 5 | D1 |
| Écrit | 6 genres, dont les 2 de l'examen ; 12 sujets pour commencer | — | ✓ | ✓ | D2 |
| Examen blanc telc Pflege | 2 examens complets (écoute, lecture, Sprachbausteine, écrit, oral) | — | ✓ | ✓ | § 4.6 |

**Les dix thèmes** : 1. le corps, la douleur, les symptômes ; 2. les soins de base ; 3. les signes
vitaux ; 4. les médicaments et les doses ; 5. l'hygiène et les plaies ; 6. l'alimentation et
l'élimination ; 7. les urgences et les chutes ; 8. l'équipe et le planning ; 9. la documentation
et la relève ; 10. les familles, les émotions, la fin de vie.

**Les huit scènes** : la chambre du patient, le poste de soins, la salle de bain, la relève au lit,
l'admission, la visite médicale, la maison de retraite, les soins à domicile.

**Les douze dialogues** : se présenter ; la douleur de 0 à 10 ; expliquer un soin ; le refus de
soin ; la famille ; la relève orale ; l'appel au médecin (SBAR) ; la chute ; aider à manger ;
expliquer un médicament ; échanger un poste ; un résident désorienté la nuit.

**Ce qu'on reprend du corpus général** (relevé par la cartographie du moteur) : les thèmes
*Gesundheit* (133 mots, A1-C1), *Körperteile* (100), *Pflege und Betreuung* C1 (14),
*Alter und Abschied* C1 (13), le chapitre VHS 6 (37 mots médicaux), les métiers (*Krankenschwester,
Pfleger, Altenpfleger*). Un mot déjà au corpus **n'est pas dupliqué** : le thème Soins le reprend
(même carte, même progression), avec une phrase d'exemple de soins en plus. Absents du corpus et
nécessaires : *Pflegekraft, Infusion, Körperpflege, Bettpfanne, Station* (au sens hospitalier),
entre autres — la liste exacte sortira d'un script de comparaison en phase 2.

**Les personnages** (annexe B) : des **nouveaux** — Maricel (Philippines), Arun (Kerala), Amira
(Tunisie), Mateo (Colombie, si l'espagnol vient), leur mentor Jonas, la cadre, la médecin, quatre
patients. Mark et Anna n'y figurent pas. Les thèmes illustrés photoréalistes ont déjà un
infirmier, **Lucas**, et deux médecins (`visuel/personnes.json`) : on les réemploie dans les pages
de thèmes Soins plutôt que d'en créer d'autres.

---

## 4. L'architecture dans le moteur

Rien n'est codé en phase 0. Ce qui suit est la proposition à valider ; les références
`index.html:N` viennent de la cartographie du 13 nov. (main à la v1184).

### 4.1 Principe : une section de l'allemand, pas une langue apprise

La section Soins **n'est pas** un `?apprendre=` de plus : c'est de l'allemand, appris par un
germaniste qui suit aussi le corpus général. Elle vit dans `LANGUE_APPRISE === "de"`, le stockage
`deutschAI_`, les collections `users` / `resumes`. Conséquences :

- un mot appris dans une scène de soins compte partout (même règle que les thèmes illustrés) ;
- **l'allemand sans licence ne doit pas bouger d'un pixel** : tout est derrière un garde
  (`essaiActif("soins")`) et le parcours `fusion-espagnol/parcours.py --app de` doit donner
  **0 écart** contre la référence à chaque livraison ;
- l'espagnol, l'anglais, le portugais, le japonais ne voient rien.

### 4.2 Les données

```
pflege/
  PLAN.md, annexes/              ← ce cadrage
  sources/                       ← ce qu'on écrit et corrige à la main (YAML ou .py, comme anglais/outils/)
  outils/construire.py           ← fait datos/ à partir de sources/ ; contrôles
  datos/                         ← DÉRIVÉ, jamais corrigé à la main
    themes.json                  ← même format que themes.json (ids pflege_*), 9 langues
    dialogues.json               ← répliques, Redemittel, exercices
    grammaire.json               ← 21 fiches + séries
    ecrit.json                   ← fiches sources, briques, corrigés
  examen/                        ← examens blancs (format visuel/prototype/telc/donnees)
visuel/prototype/pflege-<scène>.points.json   ← les 8 scènes, chaîne habituelle
```

- **Format des mots** : identique à `themes.json` (`mot, genre, pluriel, traduction,
  traduction_en … traduction_ru, exemple, exemple_fr … exemple_ru`), plus un champ `domaine:
  "pflege"` et, pour un mot repris du corpus, un renvoi vers sa fiche au lieu d'un doublon.
- **Les thèmes sont exclus des comptes publics**, exactement comme les chapitres VHS
  (`estChapitreVhs`, `themesComptes`, index.html:45927) : les « 7 700 mots » de l'app ne changent
  pas, et un compte sans licence ne voit jamais un thème `pflege_*`.
- **Les scènes** passent par `construire.py`, qui lit aujourd'hui le corpus `themes.json` : il
  devra lire aussi `pflege/datos/themes.json` (sinon « mot absent du corpus » l'arrête). Les
  variantes `.es/.en/.pt.js` ne sont **pas** produites pour les scènes de soins (allemand
  seulement).
- **Chargement** : les fichiers ne sont demandés que si la licence est ouverte.
- ⚠️ **Le contenu n'est pas secret** : servi depuis le site, un fichier est lisible par qui
  connaît l'URL, licence ou non (et le dépôt est encore public). La licence protège **l'accès
  dans l'app, le suivi et le tableau de bord**, pas les textes. Si Jacques veut protéger le
  contenu lui-même, il faut le servir depuis **Firebase Storage** avec une règle qui lit la
  licence du compte. Décision demandée (§ 9, Q5) ; je recommande d'**attendre** : la valeur vendue
  est le suivi, et le dépôt doit devenir privé (déménagement en cours).

### 4.3 La licence

Sur le modèle de l'essai anglais ouvert à un compte (`anglais/OUVRIR-A-UN-COMPTE.md`) :

1. **Pilote (phase 1)** : la licence est simplement `essais: ["soins"]` sur `users/<uid>`.
   **Aucun changement de règles Firestore** : `essais` est déjà une clé réservée
   (`accesReserves()` de `securite/firestore-corrige.rules`), que l'utilisateur ne peut pas
   s'écrire. L'admin l'ouvre par un bouton « OUVRIR SOINS » dans son tableau de bord
   (`basculerEssaiCompte`, index.html:55238), le compte la lit à la connexion
   (`loadVhsKapitelAccessFlag`, index.html:45626), et un registre `ESSAIS.soins = {etat:"admin",
   compte:"soins"}` (index.html:54080) allume la section.
2. **Vente (phase 5)** : deux clés réservées de plus, `agence` (l'agence du compte) et une
   échéance — `accesJusqua` existe déjà dans `accesReserves()` et peut servir. Ajouter une clé à
   `accesReserves()` coûte une comparaison de liste, pas un contrôle par champ : le budget de
   1 000 expressions des règles (« 10 de plus passent, 15 font refuser ») n'est presque pas
   touché.
3. **Les codes d'invitation en lot** : un code porte `agence`, `cohorte` et `licence: "soins"`.
   Le client ne peut pas recopier ces droits sur son compte (clés réservées) : il faut **soit**
   que l'admin les applique (un bouton « appliquer les licences des codes utilisés »),
   **soit** une **Cloud Function** qui, à la consommation du code, écrit `essais`, `agence` et
   `cohorte`. La seconde est la bonne pour la vente (rien à faire à la main, aucune règle
   élargie) ; le projet est passé au forfait Blaze, donc déployable. Génération en lot : un
   formulaire « 50 codes pour l'agence X, cohorte Y » et un export CSV des liens
   (`https://wortando.com/?code=…`).
4. **Fin de licence** : à l'échéance, la section se referme ; **la progression reste** (elle est
   à l'apprenant), et l'allemand général continue selon son propre abonnement.

### 4.4 La séance du jour

La séance (`ouvrirSeanceDuJour`, index.html:72120) assemble : nouveaux mots du niveau, révisions
dues, scène du jour, thème du jour, repères, son. Pour un compte licencié :

- **les nouveaux mots** sont tirés **d'abord des thèmes Soins** du niveau de la séance
  (`paquetDuNiveau`, index.html:63928), puis du corpus général : proposition **2/3 soins, 1/3
  général** au B1, **1/2 – 1/2** à l'A2 (le général manque plus) — à régler après le pilote ;
- **les révisions** ne changent pas : un mot est un mot ;
- **un arrêt « soins » par jour**, en rotation : une scène de soins, un dialogue, une série de
  grammaire du métier, un sujet d'écrit court — inséré comme le thème illustré
  (`insererThemeIllustre`, index.html:72036), avec une part `"soins"` dans `ORDRE_PARTS`
  (index.html:72284) ;
- une **raison d'apprendre « soigner »** dans le profil (sur le modèle de `SCENES_PAR_RAISON`,
  index.html:66308) oriente la scène du jour générale vers le cabinet, la pharmacie, l'examen.

### 4.5 L'entrée dans l'app

- Une tuile **« Soins »** dans Tout le contenu (`data-orbid="pflege"`), visible seulement avec la
  licence, qui ouvre un panneau à blocs sur le modèle de la préparation aux examens
  (`panneauBlocsExamens`, index.html:50153) : *Mots · Scènes · Dialogues · Grammaire du métier ·
  Écrire · Examen blanc*.
- Sur l'accueil d'un compte licencié, un bloc « Soins » sous la séance (comme le bloc des thèmes
  illustrés, `majExplorerThemes()`), avec la progression vers l'examen.

### 4.6 L'examen blanc telc Pflege

Le module telc A2·B1 existant (`visuel/prototype/telc/` : `telc-commun.js`, un module par partie,
`examen-blanc.js`, chronomètre, état dans `wortando_telc_blanc`) est **le gabarit**. On crée
`visuel/prototype/telc-pflege/` avec les mêmes briques et le format du test modèle (après Q1) :
écoute 4 parties / 25 min, lecture 4 parties + Sprachbausteine 2 parties / 60 min, écrit 30 min,
oral 3 parties. L'oral réutilise la mécanique de `oral.html` et du DTZ oral. Les textes sont
**écrits pour Wortando**, dans le style de l'examen, jamais copiés.

### 4.7 Questions techniques ouvertes (pour la phase 1)

1. **Juger l'écrit libre** : le module telc actuel corrige-t-il le texte libre, ou montre-t-il un
   modèle ? Une correction par modèle de langue demanderait un serveur et un coût par copie.
   Proposition : grille d'autocorrection + corrigé modèle au pilote ; correction automatique
   plus tard, si l'agence la paie.
2. **L'oral à deux** : l'examen se passe en binôme ; l'app joue le partenaire (répliques
   enregistrées), comme le DTZ oral.
3. **Les voix des dialogues** : plusieurs voix allemandes (soignante, patient âgé, médecin) —
   voir § 6.2.

### 4.8 Le tableau de bord de l'agence

Base : le tableau de bord admin (`openAdminDashboard`, `renderAdminUsersList`, index.html:54671 et
54978) — lignes par apprenant, état « actif / à relancer / jamais commencé », tri, `<details>`.

**Ce qu'il montre** (par cohorte) :

| Écran | Contenu |
|---|---|
| Cohortes | nom, date de début, date d'examen visée, nombre de licences utilisées / achetées |
| Apprenants | prénom, dernier jour actif, jours actifs sur 7 et sur 28, séances finies, mots Soins vus / maîtrisés, niveau de séance, scores du dernier examen blanc par partie |
| **Prêt pour l'examen** | un indicateur par apprenant : vert / orange / rouge, d'après la maîtrise des mots B1-B2 Soins, les deux derniers examens blancs par partie (au-dessus du seuil du test modèle) et la régularité. Formule exacte après Q1. |
| **Alertes** | 5 jours sans activité ; 3 séances abandonnées de suite ; examen blanc sous le seuil dans une partie ; licence qui expire |
| Codes | générer N codes pour une cohorte, les exporter en CSV, voir lesquels sont utilisés |
| Export | CSV par cohorte (pour les rapports de l'agence à ses clients hôpitaux) |

**Comment il lit, en sécurité** — recommandation : **l'agence ne lit jamais les documents des
apprenants.** Une Cloud Function quotidienne calcule, par agence, un **rapport** (`agences/{id}/
rapports/{date}` : une ligne par apprenant, seulement les chiffres ci-dessus) ; le gestionnaire
n'a le droit de lire que les rapports de son agence (`agences/{id}.gestionnaires` contient son
uid). Avantages : aucune règle sur `users` ou `resumes` à élargir, aucun contrôle de plus dans le
budget des règles de progression, et l'agence ne voit **que** ce qu'on a décidé de lui montrer
(ni les retours écrits, ni l'e-mail, ni le détail des cartes).

**Collections nouvelles** : `agences/{id}` (nom, gestionnaires, cohortes, licences ; écrit par
l'admin ou la fonction) et `agences/{id}/rapports/{date}` (écrit par la fonction seule). Règles :
lecture par les gestionnaires de l'agence et l'admin, écriture par personne côté client.

**Où il vit** : une page à part, `pflege/agence.html` (même origine, même authentification), et
non dans `index.html` : ses utilisateurs sont des gestionnaires sur ordinateur, pas des
apprenants, et l'app n'a pas à porter ce poids. À trancher en phase 5.

**Données personnelles (RGPD)** : l'agence devient destinataire de données d'apprentissage. Il
faut : une mention claire à l'inscription par code d'agence (« votre employeur verra votre
progression : … »), la mise à jour de `confidentialite.html`, et un **contrat de sous-traitance**
(AVV, art. 28 RGPD) avec chaque agence. À faire relire par un juriste avant la première vente
(§ 6.4).

### 4.9 Ce que la phase 1 livrera

La licence (pilote : `essais: ["soins"]`), le garde, la tuile et le panneau vides, le chargement
de `pflege/datos/`, le branchement de la séance, un premier thème de 30 mots pour éprouver toute
la chaîne, et les contrôles : `tests/verifier.py`, `node tests/syntaxe.js`, un `tests/pflege.py`
(données Soins), parcours `de` à 0 écart et `es` à 0 écart.

---

## 5. Les langues d'interface

**Aujourd'hui (allemand appris)** : fr, en, tr, uk, fa, ar, pt, pl, ru (`UI_LANGS`,
index.html:14629).

| Pays de recrutement | Langue | Couverte ? |
|---|---|---|
| Philippines, Inde (Kerala, Telangana) | anglais | ✓ |
| Tunisie, Maroc | arabe, français | ✓ ✓ |
| Égypte, Jordanie, Syrie | arabe | ✓ |
| Turquie | turc | ✓ |
| Brésil | portugais | ✓ |
| Ukraine | ukrainien | ✓ |
| Mexique, Colombie, Amérique latine | **espagnol** | ✗ |
| Bosnie, Serbie (Balkans : 51 000 en emploi) | bosnien / serbe / croate | ✗ |
| Albanie, Kosovo | albanais | ✗ |
| Indonésie (Triple Win) | indonésien | ✗ |
| Vietnam | vietnamien | ✗ |

**Recommandation** :

1. **Ajouter l'espagnol comme langue d'interface de l'allemand**, en premier : l'Amérique latine
   est un bassin de recrutement actif (Mexique et Colombie notamment), l'app a déjà des textes
   d'interface en espagnol (interface de l'anglais), et l'outillage des langues (chaînes turque,
   persane, ukrainienne) est rodé. ⚠️ Gros chantier à part : **tout** le corpus allemand en
   espagnol (≈ 7 700 entrées et leurs exemples), pas seulement la section Soins. À proposer comme
   **session séparée** au chef, indépendante de Pflege.
2. **Ne rien décider pour les Balkans, l'Indonésie et le Vietnam avant les entretiens** avec les
   agences (§ 7.3) : on ajoute la langue de la **première cohorte payante**, pas une langue
   hypothétique.
3. **Le contenu Soins, au pilote, dans les 9 langues** ou seulement dans celles de la cohorte ?
   La règle de Jacques est « toutes les langues au même niveau ». Proposition : **les 9 langues
   dès la phase 2**, traduites par Claude et contrôlées par la chaîne habituelle (relecture
   croisée) ; la **relecture humaine** par langue seulement pour celles des cohortes pilotes.
   Décision demandée (§ 9, Q6).
4. **Les termes de soins se traduisent par le terme du métier dans la langue cible**, pas mot à
   mot (« escarre », *pressure ulcer*, *bası yarası*…) : c'est ce que le soignant a appris dans sa
   formation. ⚕️ pour chaque langue : une relecture par un soignant de cette langue serait idéale
   (coût au § 6.3, à réserver aux langues des cohortes).

---

## 6. Les coûts et les accords à demander

**Aucune dépense sans l'accord de Jacques, transmis par le chef.** Toutes les quantités ci-dessous
sont des **estimations** ; chaque lot sera chiffré et annoncé avant d'être lancé.

### 6.1 Images (fal, nano-banana-pro, ≈ 0,15 $ l'image)

| Lot | Quantité | Coût |
|---|---|---|
| Planche d'essai (chambre, 3 images) | 3 | ≈ 0,45 $ |
| 8 scènes, avec reprises (≈ 6 essais par scène) et gros plans | ≈ 50 | ≈ 7,50 $ |
| Une image par dialogue (vignette), ×2 essais | ≈ 30 | ≈ 4,50 $ |
| Photos de l'oral (partie 1A : décrire une scène de soin), 2 examens | ≈ 30 | ≈ 4,50 $ |
| Thèmes illustrés Soins (personnes photoréalistes, détourage BiRefNet) | ≈ 80 | ≈ 12 $ |
| **Total** | **≈ 190** | **≈ 30 $** |
| *dont MVP* (planche, 3 scènes, 10 vignettes) | ≈ 45 | **≈ 7 $** |

### 6.2 Voix

Volume : mots et exemples ≈ 40 000 caractères, dialogues ≈ 15 000, couches des scènes ≈ 15 000,
séries de grammaire ≈ 15 000, écoute de 2 examens blancs ≈ 40 000 → **≈ 125 000 caractères**
(MVP ≈ 50 000).

| Option | Coût total | MVP | Remarque |
|---|---|---|---|
| ElevenLabs multilingual **v2** (jamais Flash), Aurora + 3-4 voix de dialogue | ≈ 21 $ (+30 % de reprises ≈ 27 $) | ≈ 10 $ | même voix que le reste de l'allemand ; volume 15 fois plus petit que celui écarté le 13 nov. pour les thèmes |
| Google Cloud TTS (voix choisies les 8-9 nov.) | ≈ 4 $ | ≈ 2 $ | en attente de la réponse de Google sur l'usage commercial |
| Voix du téléphone | 0 $ | 0 $ | inacceptable pour l'écoute d'examen et les dialogues |

Proposition : **ElevenLabs v2 pour le MVP** (≈ 10 $), contrôle `audio/controler_sons.py --dossiers
de`, nombres en lettres (`audio/lectures/de.json` : « 130 zu 85 », « 1-0-1 », « 0,5 mg » demandent
une lecture écrite à la main ⚕️).

### 6.3 Relecture

| Relecture | Volume | Coût | |
|---|---|---|---|
| **Infirmière ou infirmier germanophone** (justesse des soins, des procédures, des documents) | MVP : ≈ 10-15 h ; complet : ≈ 30-40 h | 40-70 €/h → MVP **400-1 000 €**, complet 1 200-2 800 € | **estimation**, indispensable avant tout pilote |
| Enseignant(e) de DaF Pflege (format d'examen, niveau, naturel de la langue) | ≈ 10-20 h | 400-1 200 € | **estimation** ; la professeure du réseau de Jacques est un premier avis, que Jacques sollicite lui-même |
| Relecture native par langue d'interface (soignant de cette langue) | ≈ 6-10 h par langue | 200-500 € par langue | **estimation**, seulement pour les langues des cohortes |

Le contenu médical est **la** condition de la vente : une erreur de procédure dans une app vendue
à un hôpital coûterait le client. Rien n'est publié à une agence avant la relecture infirmière.

### 6.4 Autres

| Poste | Coût | |
|---|---|---|
| Test modèle telc (téléchargement gratuit) | 0 € | accord demandé (Q1) |
| Matériel telc imprimé (Übungstest, Trainingseinheiten Pflege) | ≈ 20-40 € | **estimation**, facultatif |
| Juriste : CGV B2B, contrat de sous-traitance RGPD, mention d'inscription | 500-1 500 € | **estimation**, avant la première vente, pas avant le pilote gratuit |
| Cloud Functions (codes, rapports d'agence) | ≈ 0 € au volume d'un pilote | forfait Blaze déjà en place |
| Stores : licence vendue à une organisation hors de l'achat intégré | 0 € | ⚠️ à vérifier : la règle Apple 3.1.3(c) (« Enterprise Services ») semble le permettre ; Google Play a une règle voisine |

### 6.5 Récapitulatif

| | MVP (pilote) | Complet |
|---|---|---|
| Images | ≈ 7 $ | ≈ 30 $ |
| Voix | ≈ 10 $ | ≈ 27 $ |
| Relecture infirmière | 400-1 000 € | 1 200-2 800 € |
| Relecture DaF | (avis de la professeure) | 400-1 200 € |
| Juriste | — | 500-1 500 € |
| **Total** | **≈ 20 $ + 400-1 000 €** | **≈ 60 $ + 2 100-5 500 €** |

---

## 7. Le calendrier

### 7.1 Les phases

| Phase | Contenu | Durée | Dépend de |
|---|---|---|---|
| **0** Cadrage | ce plan | fait le 13 nov. | — |
| **1** Architecture et licence | § 4.9 : licence pilote, garde, tuile, chargement, séance, un thème d'essai, contrôles | 1-2 sem. | accord du plan |
| **2** Contenu texte | thèmes, dialogues, grammaire, écrit, en allemand + 9 langues | 3-4 sem. (MVP : 2) | phase 1 ; Q6 |
| **3** Scènes illustrées | planche d'essai, puis les scènes | 2-3 sem. (MVP : 1-2) | accord de dépense ; Q2 |
| **4** Examen blanc telc Pflege | les 5 épreuves, 2 examens | 3 sem. (MVP : 1 examen partiel) | **Q1** (test modèle) |
| **5** Tableau de bord de l'agence | cohortes, codes en lot, rapports, alertes, export ; Cloud Functions | 2-3 sem. (MVP : minimal) | phase 1 |
| **6** Relecture | infirmière, DaF, langues | en continu dès la phase 2 | accord de dépense ; une relectrice trouvée |

Estimation : **MVP prêt en 9 à 11 semaines**, soit vers **fin janvier 2027**, si les accords
arrivent au fil de l'eau et si une infirmière relectrice est trouvée d'ici la mi-décembre.

### 7.2 Le MVP du pilote

| Bloc | Contenu |
|---|---|
| 3 scènes | la chambre, le poste de soins, la salle de bain |
| 3 thèmes | 1. le corps et la douleur ; 3. les signes vitaux ; 9. la documentation et la relève (≈ 150 mots) |
| 10 dialogues | 1 à 8, plus l'admission (15) et la sortie (13) |
| Grammaire | les 8 points des dialogues du MVP |
| Écrit | 6 sujets (3 admissions, 3 biographies) |
| Examen blanc | écoute, lecture et écrit d'un examen ; l'oral en entraînement seulement |
| Tableau de bord | une cohorte, la liste des apprenants, « actif / à relancer », mots vus, séances, export CSV ; codes en lot ; **pas** encore d'indicateur « prêt » (il attend les seuils de Q1) |
| Licence | `essais: ["soins"]` ouvert par l'admin, ou par code d'agence si la Cloud Function est prête |

**Le pilote** : une cohorte de 15 à 20 apprenants, 8 semaines, gratuit ou à prix réduit, avec un
bilan chiffré (activité, mots maîtrisés, examens blancs au début et à la fin, avis des
apprenants et de l'agence). Ce bilan devient l'argument de vente.

### 7.3 En parallèle, sans code : valider

La page des trois pistes recommandait **dix entretiens d'acheteurs avant d'écrire du contenu**.
Ce plan ne s'y oppose pas : les phases 1 et 2 (architecture, texte) coûtent peu et rendent
l'entretien concret (« voici la chambre du patient, voici votre tableau de bord »). Mais les
phases 3 à 5 (images, examen, tableau de bord complet) gagnent à attendre **trois retours
d'agences**. Questions à leur poser : combien de recrues par an, à quel niveau elles partent et
arrivent, le taux d'échec au B2, ce qu'elles paient aujourd'hui, ce qu'elles veulent voir dans un
suivi, pays d'origine et langues. Les entretiens sont l'affaire de Jacques ; je peux préparer une
fiche d'entretien et une démo.

---

## 8. Les risques

| Risque | Parade |
|---|---|
| **Une erreur médicale** dans le contenu | ⚕️ partout ; relecture infirmière obligatoire avant tout pilote ; le soignant n'apprend jamais un geste de l'app, seulement la langue qui l'entoure (avertissement dans la section) |
| Le format telc change, ou les Länder passent à leur Fachsprachprüfung | contenu centré sur les situations, examen blanc isolé dans son module |
| Vente B2B lente | pilote gratuit d'abord ; phases chères après trois retours d'agences |
| L'allemand général dérive | garde de licence, parcours `de` / `es` à 0 écart à chaque livraison |
| Les règles Firestore au bord du budget d'expressions | rapports d'agence par Cloud Function, aucune règle de progression élargie |
| Données personnelles vues par l'employeur | rapport limité, consentement à l'inscription, contrat RGPD |
| Contenu lisible sans licence | assumé au pilote (§ 4.2) ; Firebase Storage si Jacques le veut |
| Droits d'auteur (telc) | on lit le format, on n'en copie aucun texte |
| Concurrence gratuite (IQ, vhs, Goethe) | ce qu'elles n'ont pas : la séance quotidienne, l'oral jugé, le suivi pour l'employeur |

---

## 8 bis. Et l'espagnol ? (question de Jacques, 13 nov.)

« Est-ce que ça s'applique aussi à l'Espagne ? » Deux marchés différents se cachent derrière la
question. Recherche du 13 nov. 2026, pages web seulement, aucun téléchargement.

### (a) L'espagnol des soins pour les soignants étrangers en Espagne

| Fait | Chiffre | Source |
|---|---|---|
| Pénurie d'infirmières | ≈ **100 000** manquantes (ministère de la Santé, 2024) ; 6,45 pour 1 000 habitants contre 8,12 dans l'UE | https://www.eldiario.es/sociedad/sanidad-calcula-deficit-100-000-enfermeras-29-anos-eliminarlo_1_11960409.html ; https://www.redaccionmedica.com/profesionales/enfermeria/20260701/espana-necesita-enfermeras-para-igualar-la-media-europea/313152_0.html |
| Infirmières étrangères entrées dans le système public | **726 en 2022** : Portugal 195, Colombie 113, Roumanie 76, Italie 70, puis Pérou, Cuba, Venezuela… ; ≈ 47 % non hispanophones (toutes de l'UE) | https://www.redaccionmedica.com/formacion/fse/20250917/solo-dos-enfermeras-extranjeras-obtuvieron-plaza-eir-en/249596_0.amp.html |
| Homologations de diplômes (toutes professions, 2025) | 30 303 favorables, demandeurs **à 63 % latino-américains** ; infirmières ≈ 2 450 (calcul d'après un cabinet) | https://www.ciencia.gob.es/en/Noticias/2026/abril/Morant-presenta-informe-homologaciones-2025.html |
| Recrutement actif d'infirmières non hispanophones hors UE (Philippines, Inde, Maroc) | **aucune trace** | — |
| Exigence de langue | **B2 d'espagnol** pour homologuer un diplôme d'infirmier ou de médecin d'un pays non hispanophone ; rien d'officiel pour l'UE ; rien pour les aides-soignantes | https://www.ciencia.gob.es/Universidades/validate/homologacion/enfermero.html |
| Langues co-officielles (secteur public) | catalan exigé pour les postes titulaires en Catalogne ; profil de basque au Pays basque ; supprimé aux Baléares (2023), atout réduit à Valence | https://theobjective.com/sanidad/2025-05-12/pinchan-cursos-catalan-medicos-segunda-edicion/ ; https://preparaoposiciones.com/blog/oposiciones/enfermeria/pais-vasco/ |
| Aides-soignantes et auxiliaires de vie | 261 000 à 639 000 de plus d'ici 2030 (estimation du ministère, citée par le secteur) ; 45 % des employées de maison déclarées sont étrangères ; régularisation de 2026 (≈ 500 000 personnes) | https://www.corresponsables.com/actualidad/aeste-alerta-falta-profesionales-limita-atencion-personas-dependencia/ ; https://maldita.es/migracion/20240330/mujeres-migrantes-trabajo-domestico-espana/ |
| Qui paierait | aucun programme employeur de recrutement à l'étranger trouvé ; seul levier : le crédit de formation **Fundae** des entreprises (53 % utilisé en 2024) | https://factorial.es/blog/fundae-empresas-formaciones/ |

- **Taille** (estimation) : environ **1 000 infirmières par an** auraient besoin d'apprendre
  l'espagnol (UE et hors UE non hispanophones), contre ≈ 32 000 reconnaissances par an en
  Allemagne. Le seul gros volume est celui des **aides-soignantes non hispanophones**
  (10 000 à 30 000 par an, estimation), payées ≈ 1 150 € par mois, pour qui **personne ne paie**
  de formation aujourd'hui.
- **Pourquoi c'est si différent de l'Allemagne** : l'Espagne recrute là où l'on parle déjà
  espagnol (Amérique latine). La langue n'y est pas l'obstacle ; elle l'est en Allemagne.
- **Ce que le moteur réutiliserait** : tout l'espagnol actuel (corpus, scènes, voix, séance,
  variantes Espagne / Amérique latine), plus les scènes de soins si on les dessine neutres
  (voir plus bas). Il manquerait les thèmes, les dialogues et la grammaire **écrits pour
  l'espagnol** (règle des scènes : on ne traduit pas les questions d'une langue à l'autre).
- **Recommandation** : **non**, pas de section « Espagne » maintenant. Le marché payant est trop
  petit et sans acheteur identifié. Deux idées à garder : une préparation au **B2 de
  l'homologation**, plus tard, et, hors sujet ici, le **catalan pour soignants** (les
  infirmières latino-américaines qui visent un poste titulaire en Catalogne), que personne ne
  propose en application.

### (b) L'« espagnol médical » pour soignants anglophones (États-Unis) et francophones

| Fait | Chiffre | Source |
|---|---|---|
| Hispanophones aux États-Unis | **44,9 M** parlent espagnol à la maison (2024), dont 41 % parlent anglais « moins que très bien » → **≈ 18,5 M** (calcul) | https://usafacts.org/answers/how-many-people-speak-spanish-at-home/country/united-states/ |
| Soignants qui parlent espagnol | infirmières ≈ 7 % (2022) ; médecins : 6 % hispaniques + 2 % de non-hispaniques | https://www.axios.com/2024/04/01/nurse-workforce-diverse ; https://aamc.org/news/united-states-needs-more-spanish-speaking-physicians |
| Effet de la barrière de langue | chez les patients ne parlant pas anglais, 49 % des événements indésirables causent un dommage physique, contre 30 % (Divi et al., 2007) | https://psnet.ahrq.gov/issue/language-proficiency-and-adverse-events-us-hospitals-pilot-study |
| Le droit (Section 1557, règle de 2024) | un soignant ne peut soigner en espagnol sans interprète que s'il est « qualified bilingual staff », **compétence démontrée** à l'établissement ; tests courants : CCLA (≈ 110 $), CanopyCredential | https://www.law.cornell.edu/cfr/text/45/92.4 ; https://altalang.com/language-testing/ccla/ |
| Incertitude | décret de 2025 faisant de l'anglais la langue officielle ; la règle 1557 reste en vigueur, son application fédérale pourrait faiblir | https://healthlaw.org/language-access-is-mission-critical-and-still-the-law/ |
| Concurrent principal | **CanopyLearn** : 36 leçons, 40 h, ≈ **595 $ par an**, **45 crédits de formation continue** (médecins et infirmières) par un partenaire accrédité ; licences d'établissements | https://info.withcanopy.com/en/knowledge/what-ce-credits-does-canopylearn-medical-spanish-offer |
| Autres offres | MOOC Coursera / edX (sans crédits, 29-239 $), cours en direct (997-1 994 $), immersion au Guatemala (≈ 300-350 $ par semaine), Babbel for Business (sur devis) ; **Duolingo n'a pas de module médical** | coursera.org/specializations/medicalspanish ; babbelforbusiness.com/us/industries/healthcare/ |
| Facultés de médecine | 78 % offrent de l'espagnol médical, 21 % seulement selon les normes de base (2019) | https://pubmed.ncbi.nlm.nih.gov/33835381/ |
| Soignants cibles | ≈ 6 M (infirmières 3,4 M, médecins 0,86 M, assistants médicaux 0,8 M, NP 0,3 M…), dont plus de 90 % ne parlent pas espagnol | bls.gov/ooh/healthcare |
| Crédits de formation continue | devenir organisme accrédité (ACCME) : ≈ 11 800 $ et 8-10 mois ; voie réaliste : **co-organisation** avec un organisme déjà accrédité, payée par activité (montant non publié) | https://accme.org/become-accredited |
| Québec, France | Montréal : l'espagnol est la première langue non officielle parlée à la maison, mais **aucune formation** structurée trouvée ; France : aucune action DPC | — |

- **Taille** (estimation, aucune étude publiée) : 2 à 5 % de 2,7 M de soignants non
  hispanophones dans les États à forte population hispanique, à 100-300 $ par an, soit **5 à
  40 M$ par an** pour le marché individuel, plus les licences d'hôpitaux (≈ 6 000) et de facultés.
- **Qui paie** : le soignant (son budget de formation continue), l'hôpital (son budget d'accès
  linguistique), l'école (licence pour ses étudiants). Le premier achète surtout **des crédits**,
  le second **la préparation au test** de bilinguisme.
- **Ce que le moteur réutiliserait** : presque tout. L'espagnol a **déjà l'interface anglaise**
  (et française), la **variante Amérique latine** (celle des patients américains, surtout
  mexicains et centraméricains), ses voix, ses scènes, la séance et l'oral jugé. Il manquerait le
  contenu médical écrit pour l'espagnol (thèmes, dialogues patient-soignant, anamnèse, douleur,
  consentement) et, pour vendre, les crédits et un tableau de bord d'établissement — c'est-à-dire
  **exactement la mécanique de la section Soins**.
- **Une précaution** : l'app ne doit jamais laisser croire qu'elle « qualifie » quelqu'un pour
  soigner sans interprète ; elle enseigne aussi quand appeler l'interprète.
- **Recommandation** : **oui, mais en second**, après le pilote allemand. C'est un vrai marché,
  établi, plus grand en valeur que l'Espagne, avec un seul concurrent sérieux (Canopy) et aucun
  produit de masse. Deux gestes **gratuits** dès maintenant :
  1. **Dessiner les 8 scènes de soins neutres** (un hôpital qui pourrait être allemand,
     espagnol ou américain, sans écriteau) : elles serviraient l'allemand puis l'espagnol, comme
     les scènes actuelles servent déjà les deux langues. Coût nul, décision à prendre avant la
     phase 3 (§ 9, Q8).
  2. **Garder la section Soins indépendante de la langue** dans l'architecture (`pflege/` pour
     l'allemand ; un futur `espanol/salud/` suivrait le même modèle).
  Avant d'investir : deux ou trois conversations avec des formatrices d'infirmières américaines
  et un devis de co-organisation de crédits. Le Québec et la France restent accessoires.

---

## 9. Les décisions et accords demandés à Jacques

1. **Q1 — Le test modèle telc** : autoriser le téléchargement gratuit du test modèle officiel
   (ZIP avec l'audio) et du manuel « Tipps zur Prüfungsvorbereitung » (PDF), pour en relever le
   format et le barème. Nécessaire avant la phase 4.
2. **Q2 — Les personnages** : valider la distribution de l'annexe B (Maricel, Arun, Amira, Mateo,
   Jonas…) et la règle « pas de Mark ni d'Anna, pas de famille d'Anna » dans les Soins.
3. **Q3 — Le MVP** : valider son contenu (§ 7.2) et l'idée d'un pilote gratuit de 8 semaines.
4. **Q4 — La licence** : pilote par `essais: ["soins"]` puis, pour la vente, codes d'agence et
   Cloud Function ; tableau de bord d'agence par rapports calculés (pas d'accès direct aux
   données).
5. **Q5 — Le contenu** : accepter qu'il reste lisible sans licence au pilote (ou le servir par
   Firebase Storage).
6. **Q6 — Les langues** : section Soins dans les 9 langues dès la phase 2 ; **l'espagnol comme
   langue d'interface de l'allemand** en chantier séparé (une session à part, que le chef
   lancerait).
7. **Q7 — Les dépenses du MVP**, lot par lot et sur annonce : ≈ 7 $ d'images, ≈ 10 $ de voix
   ElevenLabs v2, et l'idée de chercher une infirmière relectrice (400-1 000 €).
8. **Q8 — L'espagnol** (§ 8 bis) : pas de section « Espagne » ; l'espagnol médical pour les
   soignants américains **en second**, après le pilote allemand ; dès maintenant, dessiner les
   scènes de soins **neutres** pour qu'elles servent les deux langues.

Et une remarque pour le chef : l'entrée « Chantier Wortando Pflege » du 13 nov. n'est pas (encore)
dans `decisions/DECISIONS.md` sur `main` ni dans le dossier principal.

---

## Sources

Toutes consultées le 13 nov. 2026. « (extrait) » : lu dans le résumé du moteur de recherche, la
page refusant les robots ou étant un PDF non ouvert.

- telc : pages de l'examen (de, en), page de la branche Pflege — liens au § 1.
- Centres et organismes (non officiels) : Sprachenatelier Berlin, Aplora, deutsch-vorbereitung,
  PET-Sprachen, Berlitz, Université de Mannheim — liens au § 1.
- Goethe-Institut : Goethe-Test PRO Pflege, cours (extraits, pages en 403).
- Länder : Bade-Wurtemberg (RP), Brême, Berlin (SenWGP 2024), Bavière (LfP), Hesse (IQ, extrait).
- Bundesagentur für Arbeit (2025, 2026), BMG (2026), GIZ (2025), bpb (2025), Destatis (2024,
  2026), BIBB / Anerkennung in Deutschland (2024, 2025), Mediendienst Integration, zm-online,
  Gütezeichen Faire Anwerbung, Tagesspiegel Background.
- Lois : § 16d AufenthG, § 22a BeschV (gesetze-im-internet.de).
- Offres : Lingoda Healthcare, iQ Lingua, coLanguage, Klett, IQ « Ein Tag Deutsch », vhs Pflege,
  Plan Beta, tuenews.
- PDF repérés, **non ouverts** : test modèle et manuel telc, spécifications telc 2015, Merkblätter
  de Bavière et de Hesse, brochure ZAV Triple Win, factsheet Pflege 2026 du Mediendienst, fiche
  BIBB 2025.
