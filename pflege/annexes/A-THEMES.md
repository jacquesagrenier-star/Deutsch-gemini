# Annexe A — Les dix thèmes de vocabulaire des soins

Brouillon de la phase 0 (13 nov. 2026). Ce sont des **listes de travail** : elles fixent le
périmètre et le niveau de chaque mot, elles ne sont pas encore des données. En phase 2, chaque
entrée deviendra une ligne de `pflege/datos/themes.json` avec son article, son pluriel, une phrase
d'exemple en situation de soins et ses traductions dans les 9 langues d'interface.

Conventions :

- **Niveau** : A2, B1 ou B2 — le niveau auquel le soignant en a besoin **au travail**, pas le niveau
  du mot dans une liste générale. *der Blutdruck* est B1 ici (on le mesure dès la première semaine),
  alors qu'il n'apparaît dans aucune liste A2.
- **↔ corpus** : le mot existe déjà dans le corpus général de Wortando (`themes.json`, scènes). Il
  n'est pas dupliqué : le thème des soins le **reprend** (même fiche, même progression), avec une
  phrase d'exemple de soins en plus. Liste exacte à établir en phase 2 par un script de comparaison.
- **⚕️** : à faire valider par une infirmière ou un infirmier germanophone (terme technique, norme,
  abréviation, geste dont la description doit être exacte). Voir `../PLAN.md`, § 6.3.
- Les noms de personnes au métier se donnent **aux deux genres** dans les données
  (*die Pflegefachfrau / der Pflegefachmann*) ; ici, un seul pour alléger.
- Le français donné est le **terme de soins français** (« installer au lit », « escarre »), pas
  une traduction mot à mot. Les autres langues d'interface suivront le même principe : le mot que
  le soignant connaît de sa formation dans son pays.

Total : **430 entrées** (A2 104, B1 170, B2 156), soit près de 500 termes puisque certaines
lignes en portent deux (*hoch / niedrig*). 43 sont reprises du corpus, 78 portent ⚕️.

---

## 1. Der Körper, Schmerzen und Symptome — le corps, la douleur, les symptômes

**A2**
- der Kopf — la tête ↔ corpus
- der Hals — le cou, la gorge ↔ corpus
- die Schulter — l'épaule
- der Arm — le bras ↔ corpus
- die Hand — la main ↔ corpus
- der Rücken — le dos ↔ corpus
- der Bauch — le ventre ↔ corpus
- die Brust — la poitrine, le thorax
- das Bein — la jambe ↔ corpus
- das Knie — le genou
- der Fuß — le pied ↔ corpus
- das Herz — le cœur
- der Schmerz, die Schmerzen — la douleur
- wehtun (Es tut weh.) — faire mal
- die Kopfschmerzen (Pl.) — le mal de tête
- die Bauchschmerzen (Pl.) — le mal de ventre
- das Fieber — la fièvre
- husten / der Husten — tousser / la toux
- Mir ist übel. — J'ai la nausée.
- schwindelig — pris de vertiges
- müde — fatigué
- Wie geht es Ihnen? — Comment allez-vous ?

**B1**
- die Hüfte — la hanche
- das Gelenk — l'articulation
- der Knochen — l'os
- die Haut — la peau
- die Lunge — le poumon
- der Magen — l'estomac
- die Niere — le rein
- die Blase — la vessie
- stechend (ein stechender Schmerz) — en coup de poignard
- brennend — en brûlure
- dumpf — sourd
- ziehend — qui tire, tiraillant
- drückend — oppressant, en pression
- ausstrahlen (Der Schmerz strahlt in den Arm aus.) — irradier
- die Schmerzskala (von 0 bis 10) — l'échelle de la douleur ⚕️ (NRS, voir dialogue 2)
- Wo tut es Ihnen weh? — Où avez-vous mal ?
- Seit wann haben Sie die Schmerzen? — Depuis quand avez-vous mal ?
- die Atemnot — la gêne respiratoire, la dyspnée
- sich übergeben / erbrechen — vomir
- der Durchfall — la diarrhée
- die Verstopfung — la constipation
- jucken — démanger
- geschwollen / die Schwellung — enflé / le gonflement
- blass — pâle
- schwitzen — transpirer

**B2**
- das Symptom — le symptôme
- akut / chronisch — aigu / chronique
- die Schmerzintensität — l'intensité de la douleur
- der Schmerzcharakter — le type de douleur
- schmerzfrei — sans douleur
- die Schonhaltung — la position antalgique
- die Belastungsdyspnoe / Atemnot bei Belastung — la dyspnée d'effort ⚕️
- das Taubheitsgefühl — l'engourdissement
- kribbeln — fourmiller
- verwirrt / die Verwirrtheit — confus / la confusion
- desorientiert (zeitlich, örtlich, zur Person) — désorienté (dans le temps, l'espace, la personne) ⚕️
- das Ödem (Beinödeme) — l'œdème
- die Zyanose / bläulich verfärbt — la cyanose ⚕️
- die Schmerzeinschätzung bei Demenz (BESD) — l'évaluation de la douleur chez la personne démente ⚕️
- nonverbale Schmerzzeichen (Stöhnen, Grimassieren, Unruhe) — les signes non verbaux de douleur
- die Schmerzanamnese — l'anamnèse de la douleur ⚕️
- sich verschlechtern / sich bessern — s'aggraver / s'améliorer

## 2. Grundpflege — les soins de base (toilette, installation, mobilisation)

**A2**
- waschen / sich waschen — laver / se laver ↔ corpus
- duschen — se doucher ↔ corpus
- die Zähne putzen — se brosser les dents ↔ corpus
- kämmen — peigner
- rasieren — raser
- anziehen / ausziehen — habiller / déshabiller ↔ corpus
- das Handtuch — la serviette ↔ corpus
- der Waschlappen — le gant de toilette
- die Seife — le savon ↔ corpus
- das Bett — le lit ↔ corpus
- aufstehen / sich hinlegen — se lever / s'allonger
- sich hinsetzen — s'asseoir
- der Rollstuhl — le fauteuil roulant
- die Klingel — la sonnette d'appel
- Darf ich Ihnen helfen? — Puis-je vous aider ?

**B1**
- die Körperpflege — les soins d'hygiène
- die Ganzkörperwäsche — la toilette complète
- die Teilwäsche — la toilette partielle
- im Bett waschen — faire la toilette au lit
- am Waschbecken waschen — faire la toilette au lavabo
- die Mundpflege — les soins de bouche
- die Zahnprothese / das Gebiss — la prothèse dentaire, le dentier
- das Bett beziehen — changer les draps
- die Bettwäsche — le linge de lit
- lagern — installer, positionner (au lit)
- umlagern — changer de position
- die Seitenlage / die Rückenlage — le décubitus latéral / dorsal
- das Kopfteil hochstellen — relever la tête du lit
- mobilisieren / die Mobilisation — mobiliser / la mobilisation
- an die Bettkante setzen — asseoir au bord du lit
- der Rollator — le déambulateur à roulettes
- der Toilettenstuhl — la chaise percée
- die Inkontinenzeinlage — la protection pour incontinence
- eincremen — appliquer une crème
- selbstständig — autonome
- Unterstützung brauchen — avoir besoin d'aide
- die Gehhilfe — l'aide à la marche

**B2**
- die aktivierende Pflege — les soins qui stimulent l'autonomie
- die Ressourcen (des Patienten) — les capacités préservées du patient
- der Dekubitus — l'escarre ⚕️
- die Dekubitusprophylaxe — la prévention des escarres ⚕️
- die Druckentlastung — la décharge (de pression)
- die 30-Grad-Lagerung — le décubitus latéral à 30° ⚕️
- die Wechseldruckmatratze — le matelas à pression alternée ⚕️
- die Pneumonieprophylaxe — la prévention de la pneumonie ⚕️
- die Thromboseprophylaxe — la prévention de la thrombose ⚕️
- die Kompressionsstrümpfe (Pl.) — les bas de contention
- die Kontrakturenprophylaxe — la prévention des rétractions ⚕️
- die Sturzprophylaxe — la prévention des chutes
- der Transfer (vom Bett in den Rollstuhl) — le transfert
- rückenschonend arbeiten — travailler en ménageant son dos
- die Intimpflege — la toilette intime
- die Intimsphäre wahren — respecter l'intimité
- die Expertenstandards (DNQP) — les normes de bonne pratique allemandes ⚕️

## 3. Vitalzeichen und Krankenbeobachtung — les signes vitaux, la surveillance

**A2**
- messen — mesurer ↔ corpus
- die Temperatur — la température ↔ corpus
- das Fieberthermometer — le thermomètre
- der Puls — le pouls
- der Blutdruck — la tension artérielle
- wiegen / das Gewicht — peser / le poids
- die Waage — la balance
- hoch / niedrig — élevé / bas ↔ corpus
- Ich messe jetzt Ihren Blutdruck. — Je vais prendre votre tension.

**B1**
- die Vitalzeichen (Pl.) — les signes vitaux, les constantes
- das Blutdruckmessgerät — le tensiomètre
- die Manschette — le brassard
- der Blutzucker — la glycémie
- den Blutzucker messen — faire une glycémie capillaire
- das Blutzuckermessgerät — le lecteur de glycémie
- die Atmung / die Atemfrequenz — la respiration / la fréquence respiratoire
- die Sauerstoffsättigung — la saturation en oxygène
- das Pulsoximeter — l'oxymètre de pouls
- die Körpergröße — la taille
- erhöht / erniedrigt — augmenté / diminué
- der Wert, die Werte — la valeur, les valeurs
- regelmäßig / unregelmäßig — régulier / irrégulier
- die Kurve (Fieberkurve) — la feuille de surveillance ⚕️
- auffällig / unauffällig — anormal / sans particularité
- das Fieber senken — faire baisser la fièvre

**B2**
- systolisch / diastolisch — systolique / diastolique
- „130 zu 85“ (mmHg) — « 13/8,5 » : lecture allemande en mmHg, française en cmHg ⚕️
- die Hypertonie / die Hypotonie — l'hypertension / l'hypotension
- die Tachykardie / die Bradykardie — la tachycardie / la bradycardie
- die Hypoglykämie (die Unterzuckerung) — l'hypoglycémie
- die Hyperglykämie — l'hyperglycémie
- subfebril — subfébrile ⚕️
- die Bewusstseinslage — l'état de conscience
- ansprechbar / somnolent — réactif / somnolent ⚕️
- der Body-Mass-Index (BMI) — l'indice de masse corporelle
- die Flüssigkeitsbilanz — le bilan hydrique
- engmaschig kontrollieren — surveiller étroitement
- der Normbereich / der Grenzwert — les valeurs normales / le seuil
- den Arzt verständigen — prévenir le médecin
- die Vitalparameter überwachen — surveiller les paramètres vitaux
- das Frühwarnsystem (NEWS-Score) — le score d'alerte précoce ⚕️

## 4. Medikamente und Dosierung — les médicaments et les doses

**A2**
- das Medikament — le médicament ↔ corpus
- die Tablette — le comprimé ↔ corpus
- die Kapsel — la gélule
- die Tropfen (Pl.) — les gouttes
- die Salbe — la pommade
- die Spritze — la seringue, la piqûre
- einnehmen — prendre (un médicament)
- morgens, mittags, abends, zur Nacht — le matin, le midi, le soir, au coucher
- vor dem Essen / nach dem Essen — avant / après le repas
- einmal täglich / zweimal täglich — une fois / deux fois par jour
- die Apotheke — la pharmacie ↔ corpus

**B1**
- die Dosis / die Dosierung — la dose / la posologie
- der Medikationsplan — le plan de médication ⚕️
- das Rezept — l'ordonnance
- die ärztliche Anordnung — la prescription médicale
- verordnen — prescrire
- Medikamente stellen — préparer les médicaments (dans le pilulier)
- der Dispenser / die Medikamentenbox — le pilulier
- verabreichen — administrer
- „1-0-1“ — un le matin, rien à midi, un le soir ⚕️ (schéma des plans allemands)
- nüchtern — à jeun
- zerkleinern / mörsern — écraser (un comprimé)
- die Nebenwirkung — l'effet indésirable
- allergisch gegen … / die Allergie — allergique à … / l'allergie
- das Schmerzmittel — l'antalgique
- das Antibiotikum — l'antibiotique
- der Blutverdünner — l'anticoagulant (langage courant)
- das Insulin / der Insulinpen — l'insuline / le stylo à insuline
- bei Bedarf — si besoin
- die Packungsbeilage — la notice

**B2**
- die Bedarfsmedikation — le traitement « si besoin » ⚕️
- die Darreichungsform — la forme galénique
- oral / sublingual — par voie orale / sublinguale
- subkutan (s. c.) / intramuskulär (i. m.) / intravenös (i. v.) — sous-cutané / intramusculaire / intraveineux ⚕️
- die Infusion — la perfusion
- die Injektion — l'injection
- die Wechselwirkung — l'interaction médicamenteuse
- die Kontraindikation — la contre-indication
- die Unverträglichkeit — l'intolérance
- die 6-R-Regel — la règle des « 6 R » (patient, médicament, dose, voie, moment, documentation) ⚕️
- das Betäubungsmittel (BtM) — le stupéfiant ⚕️
- das BtM-Buch — le registre des stupéfiants ⚕️
- ansetzen / absetzen — instaurer / arrêter (un traitement)
- die Retardtablette — le comprimé à libération prolongée (ne pas écraser) ⚕️
- die Adhärenz / die Therapietreue — l'observance
- das Vier-Augen-Prinzip — le double contrôle ⚕️
- der Medikationsfehler — l'erreur médicamenteuse

## 5. Hygiene, Infektionsschutz und Wundversorgung — hygiène, prévention des infections, plaies

**A2**
- sauber / schmutzig — propre / sale ↔ corpus
- sich die Hände waschen — se laver les mains
- die Handschuhe (Pl.) — les gants
- die Maske — le masque
- der Mülleimer — la poubelle ↔ corpus
- desinfizieren — désinfecter
- das Pflaster — le pansement adhésif
- die Wunde — la plaie

**B1**
- die Händedesinfektion — la friction hydro-alcoolique
- das Desinfektionsmittel — le désinfectant
- der Spender — le distributeur
- der Schutzkittel — la surblouse
- steril / unsteril — stérile / non stérile
- die Infektion / sich anstecken — l'infection / être contaminé
- ansteckend — contagieux
- die Isolierung / das Isolierzimmer — l'isolement / la chambre d'isolement
- der Verband / den Verband wechseln — le pansement / refaire le pansement
- die Kompresse — la compresse
- gerötet — rougi
- Die Wunde nässt. — La plaie suinte.
- der Abwurfbehälter — le collecteur d'aiguilles
- die Flächendesinfektion — la désinfection des surfaces
- die Schmutzwäsche — le linge sale

**B2**
- die Händehygiene — l'hygiène des mains
- die fünf Indikationen der Händedesinfektion — les cinq moments de l'hygiène des mains (OMS) ⚕️
- der Hygieneplan — le plan d'hygiène
- multiresistente Erreger (MRE) / MRSA — les bactéries multirésistantes (BMR) / le SARM ⚕️
- die Kontaktisolierung — l'isolement contact ⚕️
- die nosokomiale Infektion — l'infection nosocomiale
- die Keimverschleppung — la transmission croisée des germes
- aseptisch / die Asepsis — aseptique / l'asepsie
- die Non-Touch-Technik — la technique sans contact ⚕️
- die Wundversorgung — les soins de plaie
- die Wunddokumentation — la traçabilité de la plaie ⚕️
- der Wundrand / der Wundgrund — le bord / le lit de la plaie ⚕️
- das Exsudat — l'exsudat ⚕️
- die Entzündungszeichen (Rötung, Schwellung, Überwärmung, Schmerz) — les signes d'inflammation
- die Nadelstichverletzung — l'accident d'exposition au sang ⚕️
- der Durchgangsarzt (D-Arzt) — le médecin des accidents du travail ⚕️

## 6. Ernährung, Flüssigkeit und Ausscheidung — alimentation, hydratation, élimination

**A2**
- essen / trinken — manger / boire ↔ corpus
- das Frühstück, das Mittagessen, das Abendessen — les trois repas ↔ corpus
- Hunger / Durst haben — avoir faim / soif ↔ corpus
- ein Glas Wasser — un verre d'eau ↔ corpus
- der Tee — le thé ↔ corpus
- die Toilette — les toilettes ↔ corpus
- auf die Toilette gehen — aller aux toilettes
- der Appetit — l'appétit

**B1**
- die Schonkost / die Diät — le régime
- die Diabeteskost — le régime diabétique ⚕️
- die pürierte Kost — l'alimentation mixée
- das Essen anreichen — aider à manger
- schlucken / die Schluckstörung — avaler / le trouble de la déglutition
- sich verschlucken — faire une fausse route
- der Schnabelbecher — le gobelet à bec
- das Trinkprotokoll — la feuille de surveillance des boissons
- die Trinkmenge — la quantité bue
- die Ausscheidung — l'élimination
- der Urin / Wasser lassen — l'urine / uriner
- der Stuhlgang — les selles
- inkontinent / die Inkontinenz — incontinent / l'incontinence
- die Bettpfanne / die Urinflasche — le bassin / l'urinal
- das Abführmittel — le laxatif
- Die Windel? Nein: die Einlage. — « couche » est vexant pour un adulte : on dit *Einlage* ou *Inkontinenzmaterial*

**B2**
- die Mangelernährung — la dénutrition
- die Exsikkose / die Dehydratation — la déshydratation ⚕️
- die Flüssigkeitszufuhr — les apports hydriques
- die Nahrungskarenz — le jeûne prescrit ⚕️
- die Aspiration / die Aspirationsgefahr — l'inhalation / le risque de fausse route ⚕️
- angedickte Getränke (das Andickungsmittel) — les boissons épaissies (l'épaississant)
- die PEG-Sonde / die Sondenkost — la sonde de gastrostomie / la nutrition entérale ⚕️
- der Blasenkatheter / der Dauerkatheter (DK) — la sonde urinaire / à demeure ⚕️
- der Urinbeutel — la poche à urine
- die Obstipationsprophylaxe — la prévention de la constipation ⚕️
- das Stoma — la stomie ⚕️
- die Ein- und Ausfuhr — les entrées et les sorties (bilan) ⚕️
- das Ernährungsprotokoll — la fiche alimentaire
- die Restharnbestimmung — la mesure du résidu post-mictionnel ⚕️

## 7. Notfälle und Stürze — urgences et chutes

**A2**
- Hilfe! — Au secours !
- der Notfall — l'urgence
- der Notarzt — le médecin urgentiste
- der Rettungswagen — l'ambulance (du SAMU allemand)
- die 112 — le numéro d'urgence
- hinfallen — tomber
- bluten — saigner
- atmen — respirer
- Bleiben Sie liegen! — Restez allongé !

**B1**
- der Sturz / stürzen — la chute / chuter
- Sind Sie gestürzt? — Êtes-vous tombé ?
- die Platzwunde — la plaie (par choc, souvent au cuir chevelu)
- die Prellung — la contusion
- der Bruch / die Fraktur — la fracture
- den Notruf wählen — appeler les urgences
- der Notrufknopf / die Notrufklingel — le bouton d'appel d'urgence
- bewusstlos — inconscient
- nicht ansprechbar — qui ne répond pas ⚕️
- die stabile Seitenlage — la position latérale de sécurité
- die Herzdruckmassage — le massage cardiaque
- die Wiederbelebung — la réanimation
- der Defibrillator (AED) — le défibrillateur
- Ruhe bewahren — garder son calme
- Hilfe holen — aller chercher de l'aide

**B2**
- das Sturzprotokoll — le rapport de chute ⚕️
- sturzgefährdet / das Sturzrisiko — à risque de chute / le risque de chute
- der Herz-Kreislauf-Stillstand — l'arrêt cardio-respiratoire
- der Schlaganfall — l'AVC
- der Herzinfarkt — l'infarctus
- der Krampfanfall — la crise convulsive
- die Vitalfunktionen prüfen — vérifier les fonctions vitales
- die Atemwege freimachen — libérer les voies aériennes
- das Reanimationsteam / der Notfallalarm — l'équipe de réanimation / l'alerte ⚕️
- der Notfallwagen — le chariot d'urgence
- die Oberschenkelhalsfraktur — la fracture du col du fémur
- das FAST-Schema (Face, Arms, Speech, Time) — le test « VITE » de l'AVC ⚕️
- „Keine Reanimation“ (laut Patientenverfügung) — « pas de réanimation » (directives anticipées) ⚕️
- Zeitpunkt und Umstände dokumentieren — consigner l'heure et les circonstances
- die Unfallmeldung — la déclaration d'accident

## 8. Team, Dienst und Station — l'équipe, les horaires, le service

**A2**
- der Kollege / die Kollegin — le / la collègue ↔ corpus
- der Arzt / die Ärztin — le médecin ↔ corpus
- die Pflegekraft — le / la soignant(e)
- das Krankenhaus / die Klinik — l'hôpital / la clinique ↔ corpus
- die Station — le service
- das Zimmer — la chambre ↔ corpus
- der Patient / die Patientin — le / la patient(e) ↔ corpus
- der Bewohner / die Bewohnerin — le / la résident(e) (en maison de retraite)
- die Pause — la pause ↔ corpus
- der Dienst — le service, le poste

**B1**
- der Frühdienst / der Spätdienst / der Nachtdienst — le poste du matin / de l'après-midi / de nuit
- der Dienstplan — le planning
- frei haben / der freie Tag — être de repos / le jour de repos
- die Schicht — l'équipe, le poste
- den Dienst tauschen — échanger un poste
- einspringen — remplacer au pied levé
- die Stationsleitung — le / la cadre de santé du service
- die Pflegedienstleitung (PDL) — la direction des soins ⚕️
- die Pflegefachfrau / der Pflegefachmann — l'infirmière / l'infirmier (titre de 2020)
- die Pflegehilfskraft / die Pflegeassistenz — l'aide-soignant(e) ⚕️
- der / die Auszubildende (Azubi) — l'élève, l'apprenti(e)
- die Visite — la visite médicale
- das Stationszimmer — le poste de soins
- sich krankmelden / die Krankmeldung — se déclarer malade / l'arrêt maladie
- die Überstunden (Pl.) — les heures supplémentaires
- die Probezeit — la période d'essai

**B2**
- die Bezugspflege / die Bereichspflege — les soins par référent / par secteur ⚕️
- zuständig sein / die Zuständigkeit — être responsable / la compétence
- die Delegation ärztlicher Tätigkeiten — la délégation d'actes médicaux ⚕️
- die Anordnungsverantwortung / die Durchführungsverantwortung — responsabilité de la prescription / de l'exécution ⚕️
- die Fallbesprechung — la réunion de synthèse
- die Fortbildung / die Weiterbildung — la formation continue / la spécialisation
- unterbesetzt sein — être en sous-effectif
- die Gefährdungsanzeige / Überlastungsanzeige — le signalement de surcharge ⚕️
- der Betriebsrat — le comité d'entreprise
- der Tarifvertrag (TVöD) — la convention collective
- die Anerkennung — la reconnaissance du diplôme
- die Berufsurkunde — l'autorisation d'exercer
- der Anpassungslehrgang / die Kenntnisprüfung — le stage d'adaptation / l'épreuve d'aptitude
- das interdisziplinäre Team (Physiotherapie, Ergotherapie, Logopädie, Sozialdienst) — l'équipe pluridisciplinaire

## 9. Pflegedokumentation und Übergabe — la documentation, la relève

**A2**
- aufschreiben — noter ↔ corpus
- das Formular — le formulaire ↔ corpus
- das Geburtsdatum — la date de naissance ↔ corpus
- die Uhrzeit / das Datum — l'heure / la date ↔ corpus
- unterschreiben / die Unterschrift — signer / la signature ↔ corpus

**B1**
- die Pflegedokumentation — le dossier de soins
- dokumentieren / eintragen — documenter / inscrire
- der Pflegebericht — les transmissions écrites
- die Übergabe / übergeben — la relève / transmettre
- die Pflegeplanung — la planification des soins
- die Patientenakte — le dossier du patient
- der Aufnahmebogen — la fiche d'admission
- abzeichnen / der Durchführungsnachweis — parapher / la feuille de traçabilité ⚕️
- die Beobachtung — l'observation
- der Allgemeinzustand — l'état général
- die Maßnahme — l'action, le soin
- unauffällig / o. B. (ohne Befund) — sans particularité ⚕️
- Pat. hat gut geschlafen. — Patient a bien dormi. (style des transmissions)

**B2**
- die Pflegeanamnese — le recueil de données
- der Pflegeprozess (Problem – Ressource – Ziel – Maßnahme – Evaluation) — la démarche de soins ⚕️
- die Strukturierte Informationssammlung (SIS) — le recueil structuré de l'Altenpflege ⚕️
- das Pflegeziel / die Evaluation — l'objectif de soins / l'évaluation
- AZ / EZ (Allgemein-, Ernährungszustand) — état général / nutritionnel ⚕️
- reduzierter AZ — état général altéré ⚕️
- objektiv / wertfrei formulieren — formuler de façon objective, sans jugement
- die Schweigepflicht — le secret professionnel
- der Datenschutz — la protection des données
- rechtssicher dokumentieren — documenter de façon juridiquement solide
- das SBAR-Schema (Situation, Background, Assessment, Recommendation) — la méthode SAED ⚕️
- das Entlassmanagement — la préparation de la sortie
- der Überleitungsbogen — la fiche de liaison
- die Pflegegrade (1 bis 5) — les degrés de dépendance (assurance dépendance allemande) ⚕️
- der Medizinische Dienst (MD) — le service médical de l'assurance ⚕️

## 10. Angehörige, Gefühle und Lebensende — familles, émotions, fin de vie

**A2**
- die Angehörigen (Pl.) — les proches
- der Besuch / die Besuchszeit — la visite / les heures de visite
- traurig — triste ↔ corpus
- Angst haben — avoir peur ↔ corpus
- weinen — pleurer
- trösten — consoler
- sterben / der Tod — mourir / la mort

**B1**
- sich Sorgen machen — s'inquiéter
- beruhigen — rassurer
- zuhören — écouter
- Das tut mir sehr leid. — J'en suis vraiment désolé(e).
- die Würde — la dignité
- der Wunsch — le souhait
- der Glaube / der Seelsorger — la foi / l'aumônier
- verstorben — décédé
- die Trauer / trauern — le deuil / être en deuil
- die Patientenverfügung — les directives anticipées ⚕️
- die Vorsorgevollmacht — la procuration de prévoyance ⚕️
- die gesetzliche Betreuung — la mesure de protection (curatelle, tutelle) ⚕️
- die Demenz / dement — la démence / dément

**B2**
- die Palliativpflege / palliativ — les soins palliatifs
- das Hospiz — l'unité de soins palliatifs / la maison de fin de vie
- die Sterbebegleitung — l'accompagnement de fin de vie
- die Symptomlinderung — le soulagement des symptômes
- die Lebensqualität — la qualité de vie
- Abschied nehmen — dire adieu
- die Rasselatmung — les râles agoniques ⚕️
- die Todeszeichen — les signes de la mort ⚕️ (le décès est constaté par le médecin)
- die Leichenschau — l'examen du corps par le médecin ⚕️
- die Versorgung des Verstorbenen — la toilette mortuaire ⚕️
- kultursensibel pflegen — soigner en tenant compte de la culture
- religiöse Rituale — les rites religieux
- das Angehörigengespräch — l'entretien avec la famille
- die Validation — la validation (méthode Feil, démence) ⚕️
- herausforderndes Verhalten — les troubles du comportement ⚕️

---

## Thèmes candidats, hors des dix

À proposer après le pilote, selon les retours :

- **Krankheitsbilder** — les maladies fréquentes (Diabetes mellitus, Herzinsuffizienz, COPD,
  Schlaganfall, Demenz, Parkinson) : ce que le soignant observe et dit, pas un cours de médecine.
  ⚕️ entièrement.
- **Demenz und Altenpflege** — si les Altenheime forment l'essentiel des acheteurs, la démence
  mérite son thème (Validation, Biografiearbeit, Tagesstruktur, Weglauftendenz).
- **Ambulante Pflege** — la tournée, le client, la clé, le Hausnotruf, la Pflegekasse.
- **Krankenhaus-Abteilungen** — die Chirurgie, die Innere, die Notaufnahme, der OP, die
  Intensivstation, die Geriatrie.
