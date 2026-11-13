# Annexe B — Les huit scènes illustrées des soins

Brouillon de la phase 0 (13 nov. 2026). Mécanique **identique** aux 43 scènes actuelles
(`visuel/prototype/<scène>.points.json` → `construire.py` → `scene-<scène>.js`) : une image,
des objets à toucher (`points` : `mot`, `boite`, `sur`, `aussi`), puis des **couches** A1-C1
(`couches.<niveau>.titre` + `qs` : question, choix, `f` l'objet visé, `r` l'objet de repère,
`phrase`, `sens`, `n` la note de grammaire). Exemple lu : `arztpraxis.points.json`.

Différences voulues avec les scènes générales :

1. **Pas de couche A1** : le public arrive au moins en A2 (il en faut un pour le visa, voir
   `../PLAN.md` § 2). La première couche est A2.
2. **Les couches portent la grammaire du métier** (annexe D) et non la grammaire générale : la
   couche B1 de la chambre fait travailler l'impératif poli, pas *stehen / stellen*.
3. **Une couche « Situation » en plus** (B1-B2) : une question de jugement professionnel
   (« Que faites-vous d'abord ? »). C'est ce que le telc Pflege évalue, et ce qu'aucune scène
   actuelle ne fait. Nouveau type de question : à concevoir en phase 1 (champ `type: "situation"`).
4. **Les mots touchables sont ceux des thèmes de l'annexe A** : une scène n'introduit pas un mot
   absent des thèmes (même règle que le corpus général : « mot manquant au corpus, donc absent de
   la scène »).

## Les personnages (nouveaux)

Les soignants sont de **nouveaux personnages**. Mark et Anna n'apparaissent pas dans la section
Soins (Mark est en stage, Anna à l'aéroport : ni l'un ni l'autre n'est soignant). Noms inventés,
choisis pour être prononçables dans les neuf langues d'interface et ne désigner personne.

| Rôle | Personnage | Fiche |
|---|---|---|
| Héroïne (nouvelle arrivée) | **Maricel**, 29 ans | Infirmière formée aux Philippines, 6 ans de métier ; en Anerkennung, travaille comme Pflegeassistentin en attendant. Parle anglais et tagalog. |
| Nouvel arrivant | **Arun**, 31 ans | Infirmier formé au Kerala (Inde), en Altenheim. |
| Nouvelle arrivée | **Amira**, 26 ans | Infirmière formée en Tunisie, en soins à domicile. Parle arabe et français. |
| Nouveau venu | **Mateo**, 27 ans | Infirmier formé en Colombie, en chirurgie. (Seulement si l'espagnol devient langue d'interface, voir PLAN § 5.) |
| Mentor | **Jonas**, 38 ans | Pflegefachmann allemand, Praxisanleiter : il accueille et corrige, avec patience et humour. |
| Cadre | **Frau Hoffmann**, 52 ans | Stationsleitung. Exigeante, juste. |
| Médecin | **Dr. Aydın**, 40 ans | Stationsärztin, Innere Medizin / Geriatrie. |
| Patient | **Herr Brandt**, 82 ans | Hospitalisé après une chute (fracture du col du fémur opérée). Bougon, drôle, attachant. |
| Patiente | **Frau Lehmann**, 74 ans | Diabète de type 2, plaie au pied ⚕️. Sa fille passe tous les jours. |
| Résident | **Herr Schulze**, 87 ans | Altenheim, démence modérée, ancien conducteur de tramway. |
| Cliente | **Frau Kowalski**, 79 ans | Soins à domicile : insuline, bas de contention, chat. |

Lieux : un hôpital inventé de **Berlin** (« Klinikum am Kanal », service de médecine gériatrique),
une maison de retraite (« Haus Lindenhof ») et un service de soins à domicile du même quartier.
Berlin garde la cohérence avec le reste de l'app ; un nom d'établissement inventé évite de
désigner un lieu réel.

> **À décider par Jacques** : faut-il un pont avec l'histoire de Mark et Anna (par exemple la
> grand-mère d'Anna résidente du Haus Lindenhof) ? Par défaut, **non** : la section Soins se vend
> à des employeurs, elle doit tenir seule. Règle des scènes : mettre Anna ou sa famille dans une
> scène est une décision de Jacques.

Ton : celui de la série (`ton-serie-mark-in-berlin`) — personnages attachants, sourires, aucune
caricature de patient âgé, aucune scène humiliante (toilette, incontinence : montrées avec pudeur,
jamais de nudité ; draps et serviettes couvrent).

---

## 1. Das Patientenzimmer — la chambre du patient ✦ MVP

Maricel entre chez Herr Brandt au début du Frühdienst. Jour, chambre double (second lit vide).

**Objets à toucher (24)** : das Pflegebett, das Bettgitter ⚕️, das Kopfteil, die Fernbedienung
(des Betts), die Klingel / der Rufknopf, der Nachttisch, das Wasserglas, der Schnabelbecher, die
Brille, das Hörgerät, die Zahnprothese (dans sa boîte), der Infusionsständer, die Infusion, die
Nasenbrille (Sauerstoff) ⚕️, der Urinbeutel (accroché au lit, couvert) ⚕️, das Kissen, die
Bettdecke, der Rollator, der Rollstuhl, die Hausschuhe, der Desinfektionsmittelspender, das
Patientenarmband, der Sichtschutz (Paravent), das Fenster.

**Couches**
- **A2 — Wo? Les prépositions au lit du patient.** « Wo liegt die Brille? » → *auf dem
  Nachttisch* ; « Wo steht der Rollator? » → *neben dem Bett*.
- **B1 — L'impératif poli (Sie).** « Herr Brandt soll sich aufsetzen. Was sagt Maricel? » →
  *Setzen Sie sich bitte auf.* / *Drücken Sie bitte die Klingel, wenn Sie Hilfe brauchen.*
- **B2 — Le passif des soins.** « Das Bettgitter ___ nur mit Einwilligung hochgezogen. » →
  *wird* ; « Die Infusion muss um 10 Uhr gewechselt ___. » → *werden*.
- **C1 — Le style des transmissions.** « Pat. lehnt Mobilisation ab → ? » → *Mobilisation
  aufgrund von Schmerzen abgelehnt, Arzt informiert.*
- **Situation (B2)** : « Herr Brandt will allein zur Toilette gehen. Er ist sturzgefährdet. Was
  tun Sie zuerst? » → *Ich bleibe bei ihm und gebe ihm den Rollator.* ⚕️

⚕️ L'**Bettgitter** est une **mesure privative de liberté** (freiheitsentziehende Maßnahme) :
elle demande le consentement du patient ou une autorisation (tribunal, sauf urgence). La question
B2 doit le dire juste : relecture obligatoire.

## 2. Das Stationszimmer — le poste de soins ✦ MVP

Le poste de soins vers 13 h 30, juste avant la relève. Jonas prépare les médicaments, Frau
Hoffmann au téléphone.

**Objets (22)** : der Dienstplan (au mur), die Stationstafel (Belegung), der Computer, die
elektronische Patientenakte (l'écran), das Telefon, der Medikamentenschrank, der BtM-Schrank
(verrouillé) ⚕️, der Medikamentenwagen, die Dispenser, der Kühlschrank (Medikamente), das
Blutzuckermessgerät, das Blutdruckmessgerät, das Fieberthermometer, die Handschuhe (boîte), der
Abwurfbehälter, der Notfallwagen, der Defibrillator, die Übergabeliste, das Klemmbrett, die
Kaffeetasse, die Uhr, der Drucker.

**Couches**
- **A2 — Les heures officielles.** « Wann beginnt der Spätdienst? » → *um 13:30 Uhr* (« dreizehn
  Uhr dreißig ») ; les jours de la semaine dans le Dienstplan.
- **B1 — Les verbes à particule du service.** « Jonas ___ die Tabletten für den Abend ___. » →
  *stellt … bereit* ; *einspringen, abzeichnen, eintragen, nachfüllen*.
- **B2 — Les modaux de la règle.** « Betäubungsmittel ___ nur im verschlossenen Schrank
  aufbewahrt werden. » → *dürfen* ; *müssen / sollen / dürfen nicht*.
- **C1 — Le Konjunktiv I des consignes et des transmissions.** « Der Arzt sagte, die Patientin
  ___ nüchtern bleiben. » → *solle*.
- **Situation (B1)** : « Das Telefon klingelt: ein Angehöriger fragt nach der Diagnose. » →
  *Ich darf am Telefon keine Auskunft geben. Ich verbinde Sie mit dem Arzt.* ⚕️ (secret
  professionnel, règles de la maison)

## 3. Das Bad — la salle de bain, la toilette ✦ MVP

Maricel aide Frau Lehmann à faire sa toilette au lavabo, assise sur une chaise de douche. Pudeur :
peignoir et serviette.

**Objets (20)** : das Waschbecken, der Spiegel, die Waschschüssel, der Waschlappen, das Handtuch,
die Seife (Waschlotion), die Hautcreme, die Zahnbürste, die Zahnpasta, die Prothesendose, der
Kamm, der Rasierer, der Duschstuhl, der Haltegriff, die Notrufschnur, die Antirutschmatte, die
Toilettensitzerhöhung, der Wäschesack, die Handschuhe, der Bademantel.

**Couches**
- **A2 — Les verbes réfléchis.** « Frau Lehmann ___ sich die Hände. » → *wäscht* ; *sich
  kämmen, sich abtrocknen, sich setzen*.
- **B1 — Annoncer et demander la permission.** « Bevor Maricel den Rücken wäscht, sagt sie: » →
  *Ich wasche jetzt Ihren Rücken. Ist das in Ordnung?*
- **B2 — Les subordonnées de temps.** « ___ die Haut abgetrocknet ist, cremt Maricel sie ein. »
  → *Nachdem* ; *bevor, während, sobald*.
- **C1 — Le style nominal.** « Die Patientin wurde gewaschen. Sie hat dabei geholfen. » →
  *Ganzkörperwäsche am Waschbecken unter Anleitung, Patientin übernimmt Oberkörper selbstständig.*
- **Situation (B1)** : « Frau Lehmann ist schwindelig. » → *Ich setze sie hin, bleibe bei ihr
  und klingle.* ⚕️

## 4. Die Übergabe — la relève au lit du patient

Relève du matin à l'après-midi, au lit (Übergabe am Patientenbett) : Maricel transmet à Jonas,
devant Frau Lehmann, qui écoute et ajoute son mot.

**Objets (16)** : das Tablet (Akte), die Fieberkurve, das Pulsoximeter, die Wunde (le pansement
au pied), der Verband, das Kissen (Lagerung), das Trinkprotokoll, der Schnabelbecher, die
Insulinpen, die Uhr, der Kalender, die Klingel, das Fenster, die Tochter (visiteuse), die
Blumen, die Brille.

**Couches**
- **A2 — Le passé composé courant.** « Frau Lehmann ___ gut geschlafen. » → *hat*.
- **B1 — Perfekt et Präteritum.** « Sie ___ heute Morgen 1,5 Liter getrunken. » ; *war, hatte,
  wurde* au Präteritum, le reste au Perfekt (l'usage oral réel).
- **B2 — La subordonnée relative en relève.** « Die Patientin, ___ Wunde heute verbunden wurde,
  hat keine Schmerzen. » → *deren*.
- **C1 — Hiérarchiser une transmission (SBAR).** Remettre dans l'ordre : Situation → Hintergrund
  → Einschätzung → Empfehlung.
- **Situation (B2)** : « Was gehört NICHT in die Übergabe am Bett? » → *eine Bemerkung über die
  Tochter* (objectivité, discrétion devant le patient).

## 5. Die Aufnahme — l'admission

Herr Brandt arrive aux urgences puis dans le service. Maricel remplit la fiche d'admission avec
lui et sa fille.

**Objets (20)** : der Aufnahmebogen, die Gesundheitskarte (Versichertenkarte), der
Einweisungsschein, der Medikationsplan, der Allergiepass, die Patientenverfügung (le document), der
Koffer, der Wertsachenbeutel, die Brille, das Hörgerät, die Zahnprothese, der Gehstock, die Waage,
die Messlatte, das Patientenarmband, das Blutdruckmessgerät, der Kugelschreiber, das Tablet, der
Schrank, die Angehörige (la fille).

**Couches**
- **A2 — Les questions W.** « ___ heißen Sie? Wann sind Sie geboren? » ; les données
  personnelles.
- **B1 — Les questions indirectes.** « Können Sie mir sagen, ___ Sie Allergien haben? » → *ob*.
- **B2 — Les questions d'anamnèse.** « Seit wann / Wie oft / Unter welchen Umständen … ? »
- **C1 — Reformuler pour vérifier.** « Habe ich Sie richtig verstanden, dass … ? »
- **Situation (B1)** : « Herr Brandt hat eine Patientenverfügung. Was machen Sie damit? » →
  *Ich kopiere sie für die Akte und informiere den Arzt.* ⚕️ (procédure de la maison)

## 6. Die Visite — la visite médicale

Dr. Aydın fait la visite avec Maricel. Le chariot de visite, l'ordinateur, le patient au lit.

**Objets (18)** : der Visitenwagen, der Laptop, die Kurve, der Befund, das Röntgenbild, das
Stethoskop, die Ärztin, die Pflegefachfrau, der Patient, die Drainage ⚕️, die Wunde, der Verband,
die Infusion, das Medikament, der Notizblock, der Kittel, die Brille, das Bett.

**Couches**
- **A2 — Comprendre une consigne.** « Was soll der Patient heute machen? » → *aufstehen und
  laufen*.
- **B1 — Les verbes de la prescription.** *anordnen, absetzen, ansetzen, erhöhen, reduzieren* —
  « Die Ärztin ___ das Schmerzmittel ___. » → *setzt … ab*.
- **B2 — Rapporter une consigne (Konjunktiv I / dass).** « Die Ärztin hat gesagt, der Patient
  ___ ab morgen mobilisiert werden. » → *solle*.
- **C1 — Demander une clarification avec tact.** « Entschuldigung, darf ich kurz nachfragen: …
  ? »
- **Situation (B2)** : « Die Anordnung ist unklar: „Metoprolol 1-0-?“ » → *Ich frage bei der
  Ärztin nach, bevor ich das Medikament gebe.* ⚕️

## 7. Das Altenheim — la maison de retraite

Le salon commun du Haus Lindenhof, l'après-midi : café, gâteau, gymnastique assise. Arun avec Herr
Schulze.

**Objets (22)** : der Aufenthaltsraum, der Esstisch, der Kuchen, die Kaffeekanne, die
Trinkstation, der Rollator, der Pflegerollstuhl, der Handlauf, die große Uhr, der Kalender (date du
jour, orientation), das Fotoalbum, die Zeitung, das Puzzle, der Ball (Sitzgymnastik), die
Hüftprotektoren ⚕️, das Hörgerät, die Brille, die Pflanze, das Fenster, die Betreuungskraft, der
Bewohner, die Bewohnerin.

**Couches**
- **A2 — Les dates et l'orientation.** « Welcher Tag ist heute? » (la grande horloge, le
  calendrier) — les questions qui orientent un résident.
- **B1 — Le passé raconté (Biografiearbeit).** « Herr Schulze ___ 40 Jahre Straßenbahn
  gefahren. » → *ist*.
- **B2 — Reformuler sans contredire (validation).** « Herr Schulze will zur Arbeit. Was sagen
  Sie? » → *Sie waren gern Straßenbahnfahrer, nicht wahr?* ⚕️
- **C1 — Nuancer.** *eher, ziemlich, zunehmend, kaum* dans une observation.
- **Situation (B2)** : « Herr Schulze steht auf und will das Haus verlassen. » → la réponse juste
  ⚕️ (procédure de la maison, Weglauftendenz).

## 8. Die ambulante Pflege — les soins à domicile

Amira chez Frau Kowalski, au 3e étage d'un immeuble ancien, à 8 h. Le chat, la cuisine, la boîte à
clé.

**Objets (20)** : die Schlüsselbox, der Hausschlüssel, das Diensthandy (Tourenplan), die
Pflegemappe, der Medikamentendispenser, der Insulinpen, der Kühlschrank, das Blutzuckermessgerät,
die Kompressionsstrümpfe, die Anziehhilfe, das Pflegebett, der Hausnotruf (le bracelet), die
Treppe, der Treppenlift, der Rollator, die Katze, die Kaffeemaschine, das Telefon, die Tasche
(Pflegetasche), die Uhr.

**Couches**
- **A2 — L'heure et la tournée.** « Um wie viel Uhr kommt Amira? » → *um acht Uhr*.
- **B1 — Les conseils (sollten).** « Sie ___ die Strümpfe morgens vor dem Aufstehen anziehen. »
  → *sollten* ⚕️
- **B2 — Le téléphone au cabinet du médecin traitant.** Formules : *Ich rufe wegen … an.*
- **C1 — Documenter un refus.** « Klientin lehnt … ab, wurde über mögliche Folgen aufgeklärt. »
- **Situation (B1)** : « Frau Kowalski öffnet die Tür nicht. » → *procédure* ⚕️ (appeler,
  Hausnotruf, Pflegedienstleitung, jamais forcer seul).

---

## Production des images

Même chaîne que les scènes actuelles (`visuel/generer_scene.py`, fal nano-banana-pro, découpage
des objets, `detourer.py`, masques), avec les leçons consignées (`continuite-du-decor-video`,
`placer-quelqu-un-dans-une-image`, `icone-dessinee-pas-demandee`). Règles propres aux soins :

- **Exactitude du matériel** : un lit médicalisé allemand, une potence, un chariot, un tensiomètre
  tels qu'on les voit en Allemagne (pas d'hôpital américain). Chaque image vérifiée par l'IA
  **contre une liste d'objets** puis, pour le MVP, par l'infirmière relectrice.
- **Neutres, si Jacques retient Q8** (PLAN § 8 bis) : aucun écriteau, aucun signe propre à
  l'Allemagne, pour que la même image serve plus tard l'espagnol médical, comme les scènes
  actuelles servent déjà les deux langues.
- **Pudeur** : aucune nudité, ni corps dénudé, ni excréments. Toilette, change et intimité sont
  suggérés (serviette, paravent, porte entrouverte).
- **Une planche d'essai d'abord** (phase 3) : trois images d'une même scène (chambre), dont on
  juge le style, la justesse du matériel et la cohérence des personnages, avant de produire les
  autres. Coût : ≈ 1-2 $.
