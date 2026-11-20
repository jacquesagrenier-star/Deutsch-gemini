# Wortando Pflege : troisième avis sur les phrases médicales (19 nov. 2026)

Les 98 points « à nuancer » (96) et « pas tranché » (2) du second avis (`SECOND-AVIS.md`), sur les quatre chapitres en ligne, ont été soumis à deux autres modèles, ChatGPT et Gemini. Règle de la maison : on applique quand le premier relecteur, ChatGPT et Gemini s'accordent sur un fait (ACCORD ou ACCORD AVEC RETOUCHE) ; un désaccord, un « dépend de la maison » ou un « incertain » va à la soignante, les avis côte à côte.

⚠️ Trois modèles ne font pas une personne du métier. Rien de ceci ne remplace la relecture de la soignante : chaque ligne changée garde sa marque ⚕️ et reste dans les feuilles de relecture (`ch01_aufnahme.html`, `ch07_schmerz.html`, `ch08_uebergabe.html`, `ch10_telefon.html`).

## Le bilan

| Chapitre | Points | Appliqués | Confirmés sans changement | Pour la soignante |
|---|---|---|---|---|
| L'admission (ch. 1) | 21 | 16 | 3 | 2 |
| La douleur (ch. 7) | 27 | 22 | 2 | 3 |
| La relève (ch. 8) | 26 | 24 | 2 | 0 |
| Le téléphone (ch. 10) | 24 | 15 | 6 | 3 |
| **Total** | **98** | **77** | **13** | **8** |

- **Appliqué** : la source est corrigée (allemand, français, et les 9 autres langues). Certaines corrections ne touchent qu'une aide ou une note, quand l'allemand n'était pas en cause.
- **Confirmé sans changement** : les trois avis valident le texte, ou ne visent qu'une note déjà juste, ou proposent une donnée que le cas ne contient pas.
- **Pour la soignante** : non appliqué. Le chef d'orchestre en avait désigné 7 ; deux d'entre eux (l'appareil auditif, ch01-131e73 et ch01-fd3d6a) sont appliqués dans leur forme la plus courante et restent à lui signaler ; trois autres se sont ajoutés pendant l'application (ch01-ec373b, ch07-602397, ch10-5e1701).

Règles suivies : les sources seulement, jamais les fichiers dérivés ; la formulation la plus simple qui porte le fait commun ; **aucune donnée clinique inventée** (ni nombre de gouttes, ni débit, ni SpO2, ni dose totale, ni angle de tête de lit : chaque proposition qui en ajoutait a été écartée) ; les 10 langues à chaque phrase changée.

## Pour la soignante : 8 points non appliqués, les avis côte à côte

### ch01-ec373b — Dialogues · Die Neuaufnahme an die Ärztin übergeben · B2 · soignant(e) · réponse
- texte allemand : Sie geht mit einem Gehstock und trägt rechts den Verbandsschuh. Wegen der Polyneuropathie und weil sie nachts zweimal zur Toilette geht, ist ihr Sturzrisiko erhöht. Das Bett wurde ganz nach unten gestellt, die Klingel ist erklärt, und nachts bleibt ein Licht an.
- premier relecteur (NUANCER) : Facteurs de risque et mesures justes ; mais un « Verbandsschuh » loge un pansement, il ne décharge pas : si l'on veut dire « chaussure de décharge », le terme est « Vorfußentlastungsschuh » (ou « Entlastungsschuh »), et cette chaussure augmente elle-même le risque de chute. À trancher selon ce que porte la patiente. **Proposition :** « Sie geht mit einem Gehstock und trägt rechts den Vorfußentlastungsschuh. Wegen der Polyneuropathie und weil sie nachts zweimal zur Toilette geht, ist ihr Sturzrisiko erhöht. Das Bett wurde ganz nach unten gestellt, die Klingel ist erklärt, und nachts bleibt ein Licht an. »
- ChatGPT (ACCORD AVEC RETOUCHE) : « Verbandsschuh » désigne une chaussure permettant de porter un pansement, tandis que « Vorfußentlastungsschuh » désigne une chaussure de décharge de l'avant-pied. Le choix du terme dépend de l'équipement réellement porté. La chaussure de décharge peut elle-même modifier l'équilibre et contribuer au risque de chute. Texte proposé : « Sie geht mit einem Gehstock und trägt rechts einen Vorfußentlastungsschuh. Wegen der Polyneuropathie und weil sie nachts zweimal zur Toilette geht, ist ihr Sturzrisiko erhöht. Das Bett wurde ganz nach unten gestellt, die Klingel ist erklärt, und nachts bleibt ein Licht an. »
- Gemini (ACCORD) : Sur le plan technique, un « Verbandsschuh » est conçu pour accueillir un pansement volumineux, tandis qu'un « Vorfußentlastungsschuh » (ou « Entlastungsschuh ») vise la décharge de l'avant-pied et peut lui-même influencer l'équilibre/le risque de chute. La proposition du relecteur corrige ce point avec justesse. Texte proposé : « Sie geht mit einem Gehstock und trägt rechts den Vorfußentlastungsschuh. Wegen der Polyneuropathie und weil sie nachts zweimal zur Toilette geht, ist ihr Sturzrisiko erhöht. Das Bett wurde ganz nach unten gestellt, die Klingel ist erklärt, und nachts bleibt ein Licht an. »
- fichier : pflege/sources/dialogues/d45-aufnahme-arzt.json
- non appliqué : le sous-agent avait écrit « Vorfußentlastungsschuh » dans d45 ; la session d'architecture a remis « Verbandsschuh », parce que le cas de Frau Lehmann dit ce mot dans d25 (4 phrases), dans l'écrit e02 et sur la carte de vocabulaire « der Verbandsschuh », et que les avis disent eux-mêmes que le choix dépend de ce que porte la patiente.
- question : Frau Lehmann porte-t-elle un Verbandsschuh ou un Vorfußentlastungsschuh (le français dit partout « chaussure de décharge ») ? Si c'est une chaussure de décharge, changer le mot dans d45, d25, e02 et la carte, en une fois.

### ch01-4cc8d7 — Écrits · soins_ecrit_aufnahme_01
- texte allemand : Aufnahmebericht: Herr Brandt
- premier relecteur (NUANCER) : Les faits cités sont réalistes (ramipril 5 mg le matin, allergie, évaluation de la douleur, mobilisation sur prescription) ; texte complet non fourni : vérifier qu'avant l'opération il mentionne le repos au lit et les prophylaxies (escarre, thrombose), et pas un lever accompagné.
- ChatGPT (INCERTAIN) : Les informations fournies sont plausibles, mais le rapport complet n'est pas disponible. Il est impossible de vérifier si les consignes préopératoires, les prophylaxies contre la thrombose et les escarres, ainsi que les modalités de mobilisation sont correctement présentées. Il ne faut pas inventer des mesures sans connaître l'état clinique et les prescriptions.
- Gemini (ACCORD AVEC RETOUCHE) : Les éléments cités (ramipril 5 mg le matin, allergie à la pénicilline, évaluation de la douleur, mobilisation selon prescription) sont cohérents, et il est exact qu'en préopératoire d'une fracture du col du fémur / prothèse de hanche, l'immobilisation/repos au lit et les mesures préventives (prévention thromboembolique et escarres selon prescription) doivent être claires. Je propose une formulation de synthèse pour la rubrique des mesures prévues. Texte proposé : « Schmerzerfassung dreimal täglich, Bilanzierung, Thrombose- und Dekubitusprophylaxe sowie Mobilisation nach ärztlicher Anordnung. »
- fichier : pflege/sources/ecrit/e01-aufnahme-brandt.json (non modifié, décision du chef d'orchestre)
- texte : l'écrit « Aufnahmebericht: Herr Brandt » ; rubrique « Geplante Maßnahmen » : « Schmerzerfassung 3 x tägl.; Trinkprotokoll (Ziel 1,5 l/Tag); nach OP Mobilisation lt. Anordnung » ; rubrique « Mobilität » : « … jetzt Bettruhe ».
- premier relecteur (nuancer) : faits réalistes (ramipril 5 mg, allergie, évaluation de la douleur, mobilisation sur prescription) ; vérifier qu'avant l'opération le texte mentionne le repos au lit et les prophylaxies (escarre, thrombose), et pas un lever accompagné.
- ChatGPT (incertain) : plausible, mais sans le texte complet il ne tranche pas ; ne pas inventer de mesures sans connaître l'état clinique et les prescriptions.
- Gemini (accord avec retouche) : propose « Schmerzerfassung dreimal täglich, Bilanzierung, Thrombose- und Dekubitusprophylaxe sowie Mobilisation nach ärztlicher Anordnung. »
- ce que j'ai constaté sans rien changer : la fiche dit déjà « jetzt Bettruhe » et « nach OP Mobilisation lt. Anordnung » (pas de lever avant l'opération) ; les prophylaxies thrombose et escarre n'y sont pas.
- question pour la soignante : faut-il ajouter « Thrombose- und Dekubitusprophylaxe » aux mesures prévues avant l'opération ?

---

### ch07-602397 — Dialogues · Das Handgelenk am Tag danach · B1
- premier relecteur (NUANCER) : Froid enveloppé 20 min, pas de chaleur, bras surélevé, signes d'alerte, 116 117 et conseils de boisson : justes ; attendre lundi est une décision médicale qui se discute : chute, ostéoporose, douleur au mouvement, gonflement et hématome font soupçonner une fracture du radius, et beaucoup de maisons rappelleraient le service de garde le jour même pour une radio : à faire valider par un médecin.
- ChatGPT (ACCORD AVEC RETOUCHE) : Le froid protégé, la surélévation et la surveillance des doigts sont appropriés. En revanche, une chute chez une personne ostéoporotique, avec douleur au mouvement, gonflement et hématome, impose de transmettre rapidement la situation à la Pflegefachkraft et de demander un avis médical pour exclure une fracture ; attendre lundi ne doit pas être décidé par la soignante seule.
- Gemini (ACCORD AVEC RETOUCHE) : Le refroidissement bref avec protection cutanée, l'élévation du bras et la surveillance des signes d'alerte sont justes, mais chez une personne âgée ostéoporotique après chute avec douleur et gonflement, la nécessité d'une imagerie rapide relève d'une décision médicale sans attendre. Je propose une phrase claire sur le refroidissement et la surveillance. Texte proposé : « Wir kühlen das Handgelenk etwa zwanzig Minuten mit einem Tuch dazwischen und achten auf Schmerzen, Schwellung und die Finger. »
- fichier : pflege/sources/dialogues/d32-handgelenk.json (tout le dialogue)
- fait retenu : froid enveloppé une vingtaine de minutes, pas de chaleur, bras surélevé, signes d'alerte, 116 117 et
  conseils de boisson sont justes. Les deux retouches de texte sont aux points 5b698e et 2d8c48.
- POUR LA SOIGNANTE (ou un médecin) : chute, ostéoporose, douleur au mouvement, gonflement et hématome nouveau font
  soupçonner une fracture du radius ; peut-on attendre la médecin traitante le lundi (elle a été informée le
  vendredi, e10), ou faut-il un avis médical / une radio le jour même (service de garde) ? Les trois avis disent que
  ce n'est pas à la soignante de le décider seule et qu'un médecin doit trancher ; le dialogue dit déjà « Das
  entscheidet die Hausärztin » et « Die Hausärztin weiß Bescheid ». Réécrire la fin (appel du service de garde le
  samedi) changerait le cas : non appliqué, la question est déjà dans `relire_notes` (« À valider : peut-on attendre
  … »).
- écarté : la phrase de Gemini sur le froid (le dialogue l'a déjà).

### ch07-73db5a — Scènes · soins-zimmer · B2
- texte allemand : Das Bettgitter ___ nur mit Einwilligung des Patienten hochgezogen. ✓ wird (Das Bettgitter wird nur mit Einwilligung des Patienten hochgezogen.) ✗ ist ✗ hat
- premier relecteur (NUANCER) : Règle juste, à préciser : la barrière n'est une mesure privative de liberté que si elle retient un patient qui veut ou peut se lever ; sans capacité de consentir, il faut l'accord du Betreuer ou du mandataire ET l'autorisation du Betreuungsgericht (§ 1831 BGB, à vérifier), sauf urgence brève ; « Bettseitenteil » est le terme des textes professionnels ; vérifier aussi les choix, « wird » y est marqué faux alors que c'est la bonne réponse.
- ChatGPT (ACCORD AVEC RETOUCHE) : La réponse grammaticale « wird » est correcte au passif présent et ne doit surtout pas être marquée fausse. Sur le plan juridique, une barrière constituant une mesure privative de liberté relève du § 1831 BGB : l'autorisation du représentant légal et, en principe, celle du Betreuungsgericht sont nécessaires lorsque les conditions légales sont réunies ; le consentement libre et éclairé du patient capable de décider doit être respecté. « Bettseitenteil » est également employé dans le langage professionnel. Texte proposé : « Das Bettseitenteil wird nur mit Einwilligung des Patienten hochgezogen. »
- Gemini (INCERTAIN) : Le point 26 ne comporte pas de remarque ni de proposition du premier relecteur, et l'utilisation d'une barrière de lit (Bettgitter / Seitenteil) soulève des questions juridiques et cliniques de privation de liberté / risque de chute selon le consentement, la capacité de discernement et la réglementation en vigueur (notamment en Allemagne). Je préfère ne pas trancher unilatéralement sans le cadre complet de l'exercice et de la situation. Texte proposé : « Das Bettgitter wird nur mit Einwilligung des Patienten hochgezogen. »
- fichier : visuel/prototype/soins-zimmer.points.json (question B2, la barrière de lit)
- non appliqué : Gemini ne tranche pas. Question : « Bettgitter » ou « Bettseitenteil » ; et la règle du consentement (patient capable ; sinon Betreuer ou mandataire et Betreuungsgericht, § 1831 BGB à vérifier).
- note : la remarque « wird marqué faux » venait d'un défaut de la première feuille, corrigé depuis ; dans l'app, « wird » est bien la bonne réponse.

### ch07-510321 — Scènes · soins-zimmer · C1
- texte allemand : Er bekommt Sauerstoff über die Nasenbrille, es geht ihm gut. Was schreiben Sie? ✓ Sauerstoffgabe über Nasenbrille, Pat. atmet ruhig, keine Atemnot. ✗ Er kriegt Luft durch die Nase, alles okay. ✗ Nasenbrille drin, Pat. zufrieden, glaube ich.
- premier relecteur (NUANCER) : Formulation de dossier correcte, mais l'oxygène est un médicament : une entrée modèle porte le débit en l/min et la saturation. **Proposition :** « Sauerstoffgabe 2 l/min über Nasenbrille laut Anordnung, Pat. atmet ruhig, keine Atemnot, SpO2 94 %. »
- ChatGPT (ACCORD AVEC RETOUCHE) : La documentation de l'oxygénothérapie doit indiquer le débit prescrit en litres par minute et les observations pertinentes, notamment la saturation en oxygène lorsqu'elle est mesurée. Il ne faut toutefois pas inventer une valeur de débit ou de SpO2 : elles doivent provenir des données réelles du patient. Texte proposé : « Sauerstoffgabe laut ärztlicher Anordnung über Nasenbrille, Durchfluss: ___ l/min, SpO2: ___ %, Patient atmet ruhig, keine Atemnot. »
- Gemini : pas de réponse pour ce point.
- fichier : visuel/prototype/soins-zimmer.points.json (question C1, l'oxygène)
- non appliqué : Gemini n'a pas répondu à ce point. Le premier relecteur veut le débit et la saturation dans l'entrée modèle ; ChatGPT refuse qu'on invente ces valeurs. Question : écrire « laut ärztlicher Anordnung » sans chiffre, ou donner au cas un débit et une saturation ?

### ch10-5e1701 — Dialogues · Eine telefonische Anordnung · B2 · soignant(e) · réponse
- texte allemand : Einen Moment, ich schaue in der Kurve nach. … Um 18 Uhr hat er ein Gramm Paracetamol als Tablette bekommen, seitdem nichts. Laut Aufnahmebogen wiegt er 84 Kilo.
- premier relecteur (NUANCER) : « Kurve » est le bon mot ; pour une nouvelle dose, le médecin a besoin de la dernière prise et du total sur 24 heures (le chiffre de deux grammes est un exemple à accorder avec le cas). **Proposition :** « Einen Moment, ich schaue in der Kurve nach. … Um 18 Uhr hat er ein Gramm Paracetamol als Tablette bekommen, seitdem nichts; in den letzten 24 Stunden waren es insgesamt zwei Gramm. Laut Aufnahmebogen wiegt er 84 Kilo. »
- ChatGPT (ACCORD AVEC RETOUCHE) : Le médecin doit connaître la dernière prise, mais aussi la dose totale reçue pendant les dernières 24 heures avant de prescrire une nouvelle dose. Le total de deux grammes proposé ne doit être ajouté que s'il correspond réellement à la documentation du patient. Texte proposé : « Einen Moment, ich schaue in der Kurve nach. Um 18 Uhr hat er ein Gramm Paracetamol als Tablette bekommen, seitdem nichts. In den letzten 24 Stunden waren es insgesamt zwei Gramm. Laut Aufnahmebogen wiegt er 84 Kilo. »
- Gemini (ACCORD) : Indiquer la dernière prise et la dose cumulée sur 24 heures (en vérifiant la limite maximale journalière et l'intervalle minimal) est indispensable avant d'administrer ou de faire prescrire une nouvelle dose de paracétamol. La proposition du relecteur est claire et complète. Texte proposé : « Einen Moment, ich schaue in der Kurve nach. … Um 18 Uhr hat er ein Gramm Paracetamol als Tablette bekommen, seitdem nichts; in den letzten 24 Stunden waren es insgesamt zwei Gramm. Laut Aufnahmebogen wiegt er 84 Kilo. »
- fichier : pflege/sources/dialogues/d50-telefonische-anordnung.json (`noeuds.bisher.choix.0`)
- avant (de) : Einen Moment, ich schaue in der Kurve nach. … Um 18 Uhr hat er ein Gramm Paracetamol als Tablette bekommen, seitdem nichts. Laut Aufnahmebogen wiegt er 84 Kilo.
- après (de) : inchangé.
- fait retenu : avant une nouvelle dose, le médecin a besoin de la dernière prise ET du total de paracétamol sur 24 heures (dit par les trois avis).
- raison de ne pas appliquer : la phrase proposée ajoute « in den letzten 24 Stunden waren es insgesamt zwei Gramm ». Ce total n'existe pas dans le cas (le premier relecteur le donne comme « un exemple à accorder avec le cas », ChatGPT écrit qu'il « ne doit être ajouté que s'il correspond réellement à la documentation »). Le cas ne donne qu'une prise (1 g per os à 18 h) le jour d'une opération à 8 h : écrire « un gramme en tout » serait aussi inventer. À décider par la soignante (ou l'auteur du cas) : le total sur 24 heures de {pohl} à 1 h 40 ; une fois le chiffre fixé, la phrase du premier relecteur convient, et la question du médecin (« Hat er heute schon Paracetamol bekommen? ») peut rester.

### ch10-36ca1f — Mots · soins_dokumentation_b2
- texte allemand : die Rufbereitschaft Die Dialyse hat nachts Rufbereitschaft: Ich rufe die Pflegekraft zu Hause an, und in einer halben Stunde ist sie da.
- premier relecteur (NUANCER) : Terme et exemple plausibles (dialyse, bloc, endoscopie ont une astreinte de nuit) ; qui déclenche l'appel (souvent le médecin ou le standard, pas la soignante du service) et le délai d'arrivée dépendent de l'établissement.
- ChatGPT (DÉPEND DE LA MAISON) : « Rufbereitschaft » est le terme correct pour une astreinte pendant laquelle la personne reste joignable et doit pouvoir rejoindre l'établissement dans le délai fixé. Le délai d'une demi-heure et la personne qui déclenche l'appel dépendent de l'organisation locale ; l'exemple est plausible, mais ne doit pas être présenté comme une règle générale.
- Gemini (ACCORD AVEC RETOUCHE) : La « Rufbereitschaft » correspond bien à une astreinte à domicile avec délai d'intervention fixé par l'établissement (bloc, dialyse, endoscopie), et le déclenchement de l'appel suit l'organisation interne. Je propose une phrase claire pour l'exemple d'astreinte. Texte proposé : « Die Dialyse hat nachts Rufbereitschaft; bei Bedarf wird die Bereitschaft über den festgelegten Weg alarmiert. »
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `N("B2", "die Rufbereitschaft")`, inchangé
- allemand : Die Dialyse hat nachts Rufbereitschaft: Ich rufe die Pflegekraft zu Hause an, und in einer halben Stunde ist sie da.
- premier relecteur (NUANCER) : terme et exemple plausibles ; qui déclenche l'appel (souvent le médecin ou le standard,
  pas la soignante du service) et le délai d'arrivée dépendent de l'établissement.
- ChatGPT (DÉPEND DE LA MAISON) : terme correct ; la demi-heure et la personne qui appelle dépendent de l'organisation
  locale ; exemple plausible, à ne pas présenter comme une règle générale. Aucun texte proposé.
- Gemini (ACCORD AVEC RETOUCHE) : propose « Die Dialyse hat nachts Rufbereitschaft; bei Bedarf wird die Bereitschaft
  über den festgelegten Weg alarmiert. »
- question à la soignante : dans ta maison, qui appelle la dialyse d'astreinte la nuit (toi, le médecin, le standard), et
  en combien de temps doit-elle être là ?

### ch10-12317b — Thème illustré · soins-theme-telefon
- texte allemand : L'alphabet téléphonique : la forme traditionnelle de la DIN 5009 (Anton, Berta, Cäsar… Samuel, Zacharias), encore la plus entendue ; la norme de 2022 emploie des noms de villes (« A wie Aachen »). À confirmer avec une soignante.
- premier relecteur (NUANCER) : La table traditionnelle reste de loin la plus entendue et personne n'épelle avec les villes dans un service ; mais pour S et Z on entend surtout « Siegfried » et « Zeppelin » (versions exactes des normes à vérifier dans la DIN 5009). **Proposition :** « S wie Samuel (oft gehört: Siegfried), Z wie Zacharias (oft gehört: Zeppelin) »
- ChatGPT (INCERTAIN) : La coexistence de l'alphabet traditionnel et de la norme DIN 5009 révisée en 2022 est plausible, mais je ne peux pas confirmer sans consulter le texte exact de la norme quelles entrées officielles s'appliquent à S et Z ni la fréquence réelle de « Siegfried » et « Zeppelin » dans les services. Il vaut mieux distinguer explicitement l'alphabet traditionnel entendu à l'oral de la table normalisée actuelle.
- Gemini (ACCORD AVEC RETOUCHE) : Dans la pratique courante des services en Allemagne, on entend encore fréquemment l'alphabet traditionnel (avec variantes locales comme « Siegfried » ou « Zeppelin » selon les habitudes) plutôt que l'épellation par noms de villes. Je propose une note concise pour l'épellation de S et Z. Texte proposé : « S wie Samuel (häufig auch Siegfried), Z wie Zacharias (häufig auch Zeppelin). »
- fichier : pflege/outils/themes_soins/telefon.py (l'alphabet téléphonique)
- non appliqué : ChatGPT ne tranche pas sans le texte de la DIN 5009. Question : pour S et Z, « Samuel / Zacharias » (table traditionnelle) ou « Siegfried / Zeppelin » (ce qu'on entend le plus) ?

## À lui signaler aussi (points appliqués, question restée ouverte)

- **ch01-131e73, ch01-fd3d6a** (d41) : la prothèse dentaire se retire avant l'opération ; l'appareil auditif se garde « meistens », jusqu'à ce qu'on vienne chercher le patient pour le bloc. Gemini : « dépend de la maison ».
- **d28** (ch07-2173f8) : faut-il informer le cabinet du médecin traitant le jour même plutôt que le soir (7 sur 10 la nuit) ?
- **d30** (ch07-9ad21e) : avec une douleur nouvelle à 8 sur 10, le médecin de garde viendrait-il voir le patient ? La prescription par téléphone reste-t-elle l'exception ? Les constats ajoutés (« der Fuß ist warm und rosig », « Das Bein ist nicht verkürzt und nicht verdreht ») sont le texte commun des trois avis.
- **d32 et d36** : douleur ou gonflement qui augmentent = ärztlicher Bereitschaftsdienst ; doigts froids, pâles ou engourdis = le 112 tout de suite (les trois avis s'accordent dans d36 ; d32 a été aligné). Le premier relecteur voulait que l'infirmière tranche entre 112 et 116 117 en maison de retraite.
- **d39** : « Der Nachtdienst hat den Dienstarzt informiert » est un fait d'histoire ajouté ; ce que le médecin a décidé n'est pas dit.
- **d50** : « innerhalb der nächsten Stunde », jugé long par deux avis ; laissé.
- **Vocabulaire** : « Abdominalschmerzen » (les trois avis écrivent « Bauchschmerzen » dans la phrase ; le mot de la carte est gardé, sa traduction dit que le dossier écrit le plus souvent « Bauchschmerzen ») ; deux phrases écrites faute de texte commun (Bezugsperson, beidseits) ; « klagt über » reste dans quatre autres exemples.
- **Le jeûne** (d44, d34) : présenté comme la consigne de l'anesthésie pour ce patient, sans délai chiffré. « Ab Mitternacht » reste dit comme une règle générale dans quatre cartes de vocabulaire, une carte-phrase de la relève et deux fiches de grammaire (voir « Ce qui reste »).

## Appliqué : 77 points

### L'admission (ch. 1)

#### ch01-fa9956 — APPLIQUÉ — Dialogues · Das Aufnahmegespräch · B1
- fichier : pflege/sources/dialogues/d13-aufnahmegespraech.json (`noeuds.hilfsmittel.choix.0`, et `relire_notes`)
- avant (de) : Danke, den lege ich gleich zu Ihren Unterlagen. Brauchen Sie eine Brille oder ein Hörgerät? Und gehen Sie immer mit dem Stock?
- après (de) : Danke. Die Dosis übernehme ich aus dem Plan, und die Ärztin ordnet Ihre Medikamente für den Aufenthalt an. Brauchen Sie eine Brille oder ein Hörgerät? Und gehen Sie immer mit dem Stock?
- après (fr) : Merci. Je reprends la dose du plan, et la médecin prescrit vos médicaments pour le séjour. Avez-vous besoin de lunettes ou d'un appareil auditif ? Et marchez-vous toujours avec la canne ?
- `relire_notes` (fr) : ajout de « le plan sert à noter le traitement de la maison, que la médecin du service prescrit pour le séjour », de « (à noter avec son étendue : pour qui, sur quoi) » après la levée du secret, et « pansement refait et plaie regardée » (voir ch01-7e0e29).
- fait retenu : le plan de médicaments sert à reprendre le traitement de la maison ; ce qui est donné à l'hôpital doit être prescrit par la médecin du service.
- écarté : la phrase proposée était une réplique en plus ; je l'ai portée par la réplique qui suit la remise du plan (aucune unité ajoutée), avec « Ihre Medikamente » plutôt que « Hausmedikation » (on parle à la patiente). La phrase de ChatGPT sur le consentement pour la fille (« Ihre Einwilligung … dokumentiere ich ebenfalls ») n'est pas reprise dans le dialogue : un seul avis la propose, et la levée du secret est déjà dite par la patiente ; l'étendue (pour qui, sur quoi) est seulement portée dans la note.
- à savoir : cette réplique n'a pas de `"relire": true` (je n'en ai pas ajouté) ; le fait est dans la note du dialogue.

#### ch01-7e0e29 — APPLIQUÉ — Dialogues · Das Aufnahmegespräch · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d13-aufnahmegespraech.json (`noeuds.naechste.choix.0`)
- avant (de) : Gut. Gleich messe ich Ihren Blutzucker, und danach kommt die Ärztin zu Ihnen. Den Verband am Fuß sehen wir uns heute Nachmittag zusammen an.
- après (de) : Gut. Gleich messe ich Ihren Blutzucker, und danach kommt die Ärztin zu Ihnen. Den Verband am Fuß wechseln wir heute noch, dabei sehen wir uns die Wunde zusammen an.
- après (fr) : Bien. Tout à l'heure, je mesure votre glycémie, et ensuite la médecin passe vous voir. Le pansement du pied, nous le refaisons aujourd'hui encore, et nous regarderons la plaie ensemble à ce moment-là.
- fait retenu : à l'admission on regarde la plaie (pas le pansement), en refaisant le pansement ; cohérent avec d45, où à 12 h 30 la plaie est déjà photographiée et couverte.
- écarté : « heute Nachmittag » (contredit d45) ; la version de ChatGPT (« haben wir bereits angesehen und dokumentiert ») ne tient pas à ce moment de l'entretien ; « später » de Gemini est plus vague que le cas (ChatGPT demande de ne pas attendre). La première phrase, citée en `redemittel` et dans une `aide`, n'est pas touchée.

#### ch01-9250ab — APPLIQUÉ — Dialogues · Begrüßung und Vorstellung · A2
- fichier : pflege/sources/dialogues/d01-vorstellung.json (`noeuds.klingel.choix.1`)
- avant (de) : Hier ist Ihre Klingel. Bitte stehen Sie noch nicht allein auf, klingeln Sie lieber.
- après (de) : Hier ist Ihre Klingel. Bitte stehen Sie noch nicht allein auf, klingeln Sie lieber. Wir sagen Ihnen, wann Sie wieder allein aufstehen dürfen.
- après (fr) : Voici votre sonnette. S'il vous plaît, ne vous levez pas encore seul, sonnez plutôt. Nous vous dirons quand vous pourrez de nouveau vous lever seul.
- `relire_note` : « Après une prothèse de hanche, pas de durée fixe pour « ne pas se lever seul » : lever accompagné (soignant ou kinésithérapie), puis seul quand la kinésithérapie et la médecin l'autorisent, selon le protocole du service. Ici, trois jours après l'opération. »
- fait retenu : pas de durée fixe ; le lever se fait accompagné, et le patient se lève seul quand l'équipe (kinésithérapie, médecin) l'autorise.
- écarté : « Beim ersten Aufstehen ist die Physiotherapie oder eine Pflegekraft dabei » (premier relecteur, Gemini, ChatGPT en partie) : dans le cas, M. Brandt est opéré depuis trois jours (intro), le « premier lever » est passé ; les modèles n'avaient pas l'intro. J'ai gardé la seule phrase de ChatGPT qui tient à J+3.

#### ch01-131e73 — APPLIQUÉ (à signaler à la soignante) — Dialogues · Wertsachen und Armband · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d41-wertsachen.json (`noeuds.prothese.choix.0`, sa `relire_note`, et `relire_notes`)
- avant (de) : Danke, das ist wichtig. Für die Zahnprothese bekommen Sie eine Dose mit Ihrem Namen. Morgen früh vor der Operation müssen Sie sie herausnehmen, das Hörgerät auch.
- après (de) : Danke, das ist wichtig. Für die Zahnprothese bekommen Sie eine Dose mit Ihrem Namen. Morgen früh vor der Operation nehmen Sie sie bitte heraus. Das Hörgerät dürfen Sie meistens tragen, bis Sie in den OP abgeholt werden.
- après (fr) : Merci, c'est important. Pour votre dentier, vous recevez une boîte à votre nom. Demain matin, avant l'opération, enlevez-le, s'il vous plaît. L'appareil auditif, vous pouvez le plus souvent le garder jusqu'à ce qu'on vienne vous chercher pour le bloc.
- notes : `relire_note` et le passage de `relire_notes` disent maintenant « Retrait de la prothèse dentaire avant le bloc ; l'appareil auditif se garde le plus souvent jusqu'au départ pour le bloc, selon le protocole de la maison. »
- fait retenu : la prothèse dentaire se retire avant l'opération ; l'appareil auditif se garde le plus souvent jusqu'à ce qu'on vienne chercher le patient (décision du chef d'orchestre).
- écarté : « Bitte beachten Sie die Anweisungen des OP-Teams » (ChatGPT seul, une phrase de plus).
- à signaler à la soignante : Gemini classe le point « dépend de la maison » (certaines maisons font retirer l'appareil plus tôt) ; « meistens » porte cette réserve.

#### ch01-fd3d6a — APPLIQUÉ (à signaler à la soignante) — Dialogues · Wertsachen und Armband · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d41-wertsachen.json (`noeuds.prothese.choix.1`, sa `relire_note`)
- avant (de) : Gut, dass Sie es sagen. Ich hole Ihnen eine Prothesendose und schreibe Ihren Namen darauf. Vor der OP müssen die Prothese und das Hörgerät nämlich raus.
- après (de) : Gut, dass Sie es sagen. Ich hole Ihnen eine Prothesendose und schreibe Ihren Namen darauf. Vor der OP muss die Prothese nämlich raus. Das Hörgerät behalten Sie meistens, bis Sie abgeholt werden.
- après (fr) : Vous avez bien fait de le dire. Je vous apporte une boîte à prothèse et j'écris votre nom dessus. Car avant l'opération, le dentier doit être enlevé. L'appareil auditif, vous le gardez le plus souvent jusqu'à ce qu'on vienne vous chercher.
- fait retenu : le même que ch01-131e73, avec « meistens » dans les deux formulations justes (même fait dans tout le fichier).
- écarté : rien d'autre. La réplique du patient qui suit (« Raus, rein … Na schön ») tient toujours.
- à signaler à la soignante : même réserve de Gemini (« dépend de la maison »).

#### ch01-ea94a3 — APPLIQUÉ (en partie) — Dialogues · Die Pflegeanamnese · B2
- fichier : pflege/sources/dialogues/d42-pflegeanamnese.json (`but`, `relire_notes`)
- avant (fr, `but`) : Mener une anamnèse de soins structurée (les AEDL) : …
- après (fr, `but`) : Mener une anamnèse de soins structurée (ici selon les AEDL ; beaucoup de maisons utilisent aujourd'hui la SIS du Strukturmodell) : …
- `relire_notes` : « … selon le modèle AEDL (Krohwinkel) et leur ordre (beaucoup de maisons documentent aujourd'hui avec la SIS du Strukturmodell) » ; « boissons : ne jamais conseiller de ne plus boire le soir (déshydratation, vessie irritée), on garde la quantité de la journée et on la boit plus tôt ».
- allemand : aucune réplique changée par ce point (l'aide sur les boissons : voir ch01-70c008).
- fait retenu : les AEDL ne sont plus le modèle de toutes les maisons (SIS du Strukturmodell) ; pour les boissons, on ne réduit pas la quantité de la journée, on la répartit plus tôt.
- écarté : la phrase de Gemini (« Ich halte das in der Pflegedokumentation fest, damit alle Beteiligten gut informiert sind ») : une réplique de plus, et le dialogue dit déjà « Nur wer an Ihrer Pflege und Behandlung beteiligt ist, darf sie lesen ». Les protections « sur prescription médicale » : ChatGPT ne le confirme pas (« dépend des procédures ») ; « Einlagen bekommen Sie hier von uns » reste vrai pour la résidente : non changé, voir Doutes.

#### ch01-70c008 — APPLIQUÉ — Dialogues · Die Pflegeanamnese · B2 · soignant(e) · réponse fausse
- fichier : pflege/sources/dialogues/d42-pflegeanamnese.json (`noeuds.einlagen.choix.2.aide` ; la réponse fausse reste fausse, inchangée)
- allemand (inchangé, réponse fausse) : Dann trinken Sie abends am besten gar nichts mehr. Das machen Sie schon richtig.
- avant (fr, aide) : <b>N'encourage jamais une personne âgée à moins boire : elle se déshydrate vite.</b> Le manque d'eau donne confusion, vertiges et chutes, et irrite la vessie. Propose plutôt des protections, la sonnette la nuit, et d'en parler à la médecin traitante.
- après (fr, aide) : <b>Ne conseille jamais à une personne âgée de ne plus boire : elle se déshydrate vite.</b> Le manque d'eau donne confusion, vertiges et chutes, et irrite la vessie. Elle garde la quantité de la journée et la boit plus tôt, jusqu'au début de la soirée. Propose aussi des protections, la sonnette la nuit, et d'en parler à la médecin traitante.
- fait retenu : la faute est « gar nichts » et l'approbation ; boire plus tôt dans la journée n'est pas une erreur, tant que la quantité de la journée reste.
- écarté : la phrase allemande de Gemini (c'est une aide en français, pas une réplique).

#### ch01-81f963 — APPLIQUÉ — Dialogues · Aufnahme in der Nacht · B2
- fichier : pflege/sources/dialogues/d44-aufnahme-nachts.json (`relire_notes` ; le texte : voir ch01-e3ffce et ch01-80caa8)
- avant (fr, note) : … pas de chewing-gum (règle simplifiée : selon le protocole de l'anesthésie, des liquides clairs peuvent être permis jusqu'à 2 h avant) ; …
- après (fr, note) : … pas de chewing-gum (c'est la consigne de l'anesthésie pour ce patient, pas une règle universelle : manger et boire n'ont pas le même délai, le protocole de l'anesthésie fait foi) ; …
- fait retenu : la règle du jeûne vient de l'anesthésie ; « ab Mitternacht » est la consigne donnée dans ce cas, pas une règle universelle.
- écarté : tout délai chiffré (2 h, 6 h), retiré aussi de la note ; les médicaments du matin avec une gorgée d'eau et le jeûne immédiat pour une douleur abdominale aiguë (aucun texte commun, données que le dialogue ne contient pas) ; la phrase de Gemini (« Die genauen Nüchternzeiten richtet die Anästhesie ein … »), une réplique de plus.
- inchangé : la seconde formulation juste (« Ein paar Schlucke Wasser, ja, aber nur noch bis Mitternacht. Danach darf nichts mehr gegessen oder getrunken werden … »), la question d'écoute (« Ab wann … ? Ab Mitternacht. ») : elles restent vraies dans le cas.

#### ch01-e3ffce — APPLIQUÉ — Dialogues · Aufnahme in der Nacht · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d44-aufnahme-nachts.json (`noeuds.trinken.choix.0`, sa `relire_note` ; l'`aide` de `noeuds.trinken.choix.2`)
- avant (de) : Bis Mitternacht dürfen Sie noch ein paar Schlucke Wasser trinken. Aber ab Mitternacht müssen Sie nüchtern bleiben: Sie dürfen nichts mehr essen, nichts mehr trinken und auch keinen Kaugummi kauen.
- après (de) : Ein paar Schlucke Wasser dürfen Sie noch trinken, aber nur bis Mitternacht: So hat es die Anästhesie für Sie festgelegt. Ab Mitternacht müssen Sie nüchtern bleiben: Sie dürfen nichts mehr essen, nichts mehr trinken und auch keinen Kaugummi kauen.
- après (fr) : Vous pouvez encore boire quelques gorgées d'eau, mais seulement jusqu'à minuit : c'est ce que l'anesthésie a fixé pour vous. À partir de minuit, vous devez rester à jeun : vous ne devez plus rien manger ni boire, pas de chewing-gum non plus.
- `relire_note` : « Règle du jeûne avant l'anesthésie : la consigne de l'anesthésie pour ce patient (minuit), pas une règle universelle. »
- `aide` de la réponse fausse (la réponse reste fausse) : la citation devient « Ab Mitternacht dürfen Sie nichts mehr essen. » et l'aide ajoute « La règle vient de l'anesthésie : dis-la telle qu'elle a été fixée pour ce patient. »
- fait retenu : c'est l'anesthésie qui fixe jusqu'à quand on peut boire ; minuit est la consigne de ce patient.
- écarté : « Essen dürfen Sie ab jetzt nichts mehr » (les trois propositions) : le cas dit minuit pour manger aussi (question d'écoute « Ab Mitternacht », dont un leurre est « Ab sofort »), et « ab jetzt » serait une donnée nouvelle ; « bei uns » (règle de la maison) remplacé par « für Sie » (consigne du patient), selon la décision du chef d'orchestre.

#### ch01-cde2dc — APPLIQUÉ — Dialogues · Die Neuaufnahme an die Ärztin übergeben · B2
- fichier : pflege/sources/dialogues/d45-aufnahme-arzt.json (`relire_notes` ; le texte : voir les quatre points suivants)
- avant (fr, note) : … bord légèrement rouge … Peau sèche aux jambes, intacte ; échelle de Braden sans risque accru.
- après (fr, note) : … pourtour de la plaie légèrement rouge … Peau sèche aux jambes, intacte en dehors de l'ulcère ; risque d'escarre faible selon l'échelle de Braden, talons surveillés à cause de la polyneuropathie (l'échelle ne remplace pas le jugement clinique).
- fait retenu : l'échelle de Braden ne remplace pas le jugement clinique, les talons se surveillent à cause de la polyneuropathie ; la rougeur se dit du pourtour de la plaie ; la chaussure est une chaussure de décharge.
- écarté : profondeur, fond de la plaie, exsudat (les trois les souhaitent « si disponibles », le cas ne les donne pas) ; la phrase de synthèse de Gemini.

#### ch01-550ee2 — APPLIQUÉ — Dialogues · Die Neuaufnahme an die Ärztin übergeben · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d45-aufnahme-arzt.json (`noeuds.medikamente.choix.0`)
- avant (de) : … Sie selbst war bei der Insulindosis unsicher, deshalb habe ich mich an den Plan gehalten.
- après (de) : Ja, der Plan ihrer Hausärztin liegt in der Akte: Insulin morgens und abends, die Dosis wurde letzte Woche geändert, und eine Tablette gegen den Bluthochdruck. Sie selbst war bei der Insulindosis unsicher, deshalb habe ich die Dosis aus dem Plan übernommen. Angeordnet ist die Hausmedikation noch nicht.
- après (fr) : Oui, le plan de sa médecin traitante est dans le dossier : insuline matin et soir, la dose a été modifiée la semaine dernière, et un comprimé contre l'hypertension. Elle-même n'était pas sûre de sa dose d'insuline, c'est pourquoi j'ai repris la dose du plan. Le traitement personnel n'est pas encore prescrit.
- fait retenu : « mich an den Plan gehalten » peut se comprendre « j'ai donné selon le plan » ; on dit qu'on a repris la dose du plan et que le traitement de la maison reste à prescrire par la médecin.
- écarté : le nom du médicament et la dose (aucune donnée dans la source) ; la demande « Bitte ordnen Sie die Hausmedikation noch an » sous cette forme : elle est déjà la réplique du nœud « offen » (« Könnten Sie bitte die Hausmedikation und das Insulinschema anordnen und unterschreiben? »), et la médecin, ici, répond seulement « Gut, dass Sie den Plan genommen haben. Und der Fuß? » : une demande resterait sans réponse. La phrase dit le fait (pas encore prescrit), la demande reste à sa place.

#### ch01-62af32 — APPLIQUÉ — Dialogues · Die Neuaufnahme an die Ärztin übergeben · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d45-aufnahme-arzt.json (`noeuds.wunde.choix.0` ; pour la cohérence `noeuds.wunde.choix.1` et l'`aide` de `noeuds.wunde.choix.2`)
- avant (de) : Ein Ulkus am rechten Vorfuß, etwa zwei mal anderthalb Zentimeter. Der Wundrand ist leicht gerötet, kein Eiter, kein Geruch. Die Wunde wurde fotografiert und steril abgedeckt. Schmerzen hat sie kaum, eine Eins, weil sie die Füße wenig spürt.
- après (de) : Ein Ulkus am rechten Vorfuß, etwa zwei mal anderthalb Zentimeter. Die Wundumgebung ist leicht gerötet, kein Eiter, kein Geruch. Die Wunde wurde fotografiert und steril abgedeckt. Schmerzen hat sie kaum, eine Eins auf der Schmerzskala, weil sie die Füße wenig spürt.
- après (fr) : Un ulcère de l'avant-pied droit, d'environ deux centimètres sur un et demi. Le pourtour de la plaie est légèrement rouge, pas de pus, pas d'odeur. La plaie a été photographiée et couverte d'un pansement stérile. Elle n'a presque pas mal, un sur l'échelle de la douleur, parce qu'elle sent peu ses pieds.
- seconde formulation juste : « der Rand ist leicht gerötet » → « die Wundumgebung ist leicht gerötet » (fr : « son pourtour est légèrement rouge ») ; aide : « Taille, pourtour, pus, odeur : « Die Wundumgebung ist leicht gerötet, kein Eiter, kein Geruch. » »
- fait retenu : la rougeur se dit de la « Wundumgebung » ; « eine Eins » se rattache à l'échelle de la douleur.
- écarté : « kaum Exsudat » (Gemini), profondeur et fond (données absentes du cas) ; « mit Zustimmung der Patientin » (ChatGPT seul) : voir Doutes.

#### ch01-a6f77d — APPLIQUÉ — Dialogues · Die Neuaufnahme an die Ärztin übergeben · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d45-aufnahme-arzt.json (`noeuds.haut.choix.0` ; pour la cohérence `noeuds.haut.choix.1` et l'`aide` de `noeuds.haut.choix.2`)
- avant (de) : Die Haut ist trocken, vor allem an den Unterschenkeln, aber intakt. Kein Dekubitus, und nach der Braden-Skala hat sie kein erhöhtes Risiko.
- après (de) : Die Haut ist trocken, vor allem an den Unterschenkeln, aber bis auf das Ulkus intakt. Kein Dekubitus. Das Dekubitusrisiko schätze ich nach der Braden-Skala derzeit als gering ein. Die Fersen beobachten wir wegen der Polyneuropathie.
- après (fr) : La peau est sèche, surtout aux jambes, mais intacte en dehors de l'ulcère. Pas d'escarre. D'après l'échelle de Braden, j'estime le risque d'escarre faible pour l'instant. Nous surveillons les talons à cause de la polyneuropathie.
- seconde formulation juste : « Ein Dekubitusrisiko besteht laut Braden-Skala nicht. » → « Laut Braden-Skala ist das Dekubitusrisiko derzeit gering. Auf die Fersen achten wir wegen der Polyneuropathie. » ; aide : la citation devient « … aber bis auf das Ulkus intakt. »
- fait retenu : « pas de risque » est trop catégorique ; l'échelle appuie le jugement, et les talons se surveillent à cause de la polyneuropathie.
- écarté : « besonders » (ChatGPT) ; j'ai pris ses phrases courtes plutôt que le point-virgule.

#### ch01-d2c792 — APPLIQUÉ — Mots · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `R("B2", "Bezugsperson")` (exemple + note)
- avant (de) : Wer ist Ihre Bezugsperson, und dürfen wir sie im Notfall anrufen?
- après (de) : Wen dürfen wir im Notfall anrufen? Diese Person trage ich als Ihre Bezugsperson ein.
- après (fr) : Qui pouvons-nous appeler en cas d'urgence ? Je note cette personne comme votre proche référent.
- fait retenu : « Bezugsperson » est le mot du dossier, ambigu pour un patient (il évoque aussi la Bezugspflege) ; au
  patient, on pose la question simple « Wen dürfen wir im Notfall anrufen? » (texte identique du premier relecteur et de
  ChatGPT) ; cette personne n'a pas de pouvoir de décision (déjà dans la note, complétée).
- écarté : la phrase proposée seule, sans le mot : la carte est celle du mot « Bezugsperson », l'exemple doit le
  contenir, d'où la seconde phrase, qui montre que c'est le mot qu'on écrit. La question de Gemini sur la Vollmacht et
  la Betreuung : hors de la carte, plus longue.

#### ch01-80caa8 — APPLIQUÉ — Phrases du service · soins_rm_44_3
- fichier : pflege/sources/dialogues/d44-aufnahme-nachts.json (`redemittel.3`, la carte soins_rm_44_3, et sa `relire_note`)
- avant (de) : Ab Mitternacht dürfen Sie nichts mehr essen und nichts mehr trinken.
- après (de) : Ab Mitternacht dürfen Sie nichts mehr essen. Trinken dürfen Sie nur noch so lange, wie die Anästhesie es erlaubt hat.
- après (fr) : À partir de minuit, vous ne devez plus rien manger. Vous pouvez boire seulement aussi longtemps que l'anesthésie l'a permis.
- `relire_note` : « Règle du jeûne avant l'anesthésie : fixée par l'anesthésie, manger et boire n'ont pas le même délai. »
- fait retenu : la phrase ne s'enseigne pas comme une règle fixe ; pour boire, c'est l'anesthésie qui décide.
- écarté : aucun délai chiffré. C'est la phrase commune aux trois avis.

#### ch01-b7991b — APPLIQUÉ — Scènes · soins-aufnahme · SIT
- fichier : pflege/sources/dialogues/d05-angehoerige.json (noeuds.sorgen.choix.0), d'où la scène soins-aufnahme tire sa situation
- avant (de) : Ich kann gut verstehen, dass Sie sich Sorgen machen. Heute ist Ihre Mutter wach und gut orientiert.
- après (de) : Ich kann gut verstehen, dass Sie sich Sorgen machen. Heute ist Ihre Mutter wach und gut orientiert. Dass sie gestern am Telefon durcheinander war, gebe ich an die Ärztin weiter.
- après (fr) : … Je transmets à la médecin qu'elle était perdue hier au téléphone.
- fait retenu : une confusion nouvelle, rapportée par la fille, se transmet à la médecin (ChatGPT et Gemini donnent la même phrase).

### La douleur (ch. 7)

#### ch07-a0be31 — APPLIQUÉ — Dialogues · Schmerzen erfragen · B1
- fichier : pflege/sources/dialogues/d02-schmerzen.json (`redemittel.7`, `noeuds.zurueck.choix.0`,
  `noeuds.zurueck.choix.1`, `noeuds.lage.dit.0.recit`, `relire_notes` ; et les `relire_note` de ces unités et du
  récit de `noeuds.mittel`)
- avant (de) : « Ich komme in einer halben Stunde wieder und frage noch einmal nach. » · « Ich komme in einer halben
  Stunde wieder und frage Sie noch einmal nach den Schmerzen. » · « In 30 Minuten schaue ich wieder nach Ihnen. Dann
  sagen Sie mir wieder eine Zahl. »
- après (de) : « Ich komme in dreißig bis sechzig Minuten wieder und frage noch einmal nach. » · « Ich komme in
  dreißig bis sechzig Minuten wieder und frage Sie noch einmal nach den Schmerzen. » · « In 30 bis 60 Minuten schaue
  ich wieder nach Ihnen. Dann sagen Sie mir wieder eine Zahl. » (`dit` : « In dreißig bis sechzig Minuten … »)
- après (fr) : « Je reviens dans 30 à 60 minutes et je vous redemande. » · « Je reviens dans 30 à 60 minutes et je
  vous redemande pour la douleur. » · « Dans 30 à 60 minutes, je repasse vous voir. Vous me redonnerez un chiffre. »
- récit du nœud `lage` (français seul, pas d'allemand) : avant « {elif} revient avec le comprimé. {brandt} l'avale et
  soupire. … » ; après « {elif} prévient {jonas}, l'infirmier : il vérifie la prescription et lui remet le comprimé.
  Elle revient auprès de {brandt}, qui avale le comprimé et soupire. Il est mal installé, de travers dans son lit. »
- `relire_notes` : « … antalgique « bei Bedarf » donné seulement s'il est prescrit ; une assistante de soins en cours
  de reconnaissance ne décide pas seule de le donner : elle prévient l'infirmier, qui vérifie la prescription
  (délégation selon l'établissement) ; délai de réévaluation (30 à 60 min après une prise orale, selon le médicament
  et le standard de la maison). »
- fait retenu : après un antalgique oral on réévalue entre 30 et 60 minutes, selon le médicament et le standard de
  la maison ; donner un médicament « si besoin » revient à la Pflegefachkraft, une soignante en cours de
  reconnaissance ne le fait que sur délégation.
- écarté : « in etwa dreißig bis vierzig Minuten » (Gemini : fourchette que les deux autres ne donnent pas) ; aucune
  réplique allemande nouvelle pour la délégation (les sons de d01-d12 sont enregistrés : seul le récit français dit
  qu'Elif passe par Jonas, la solution que l'auteur prévoyait déjà dans sa note « Sinon, prévoir qu'elle prévienne
  Jonas »). Les répliques « Soll ich es Ihnen holen? » et « Ich hole sie Ihnen gleich » restent : elles ne disent pas
  qui décide.

#### ch07-110ab6 — APPLIQUÉ — Dialogues · Angst vor der Untersuchung · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d15-angst-vor-untersuchung.json (`noeuds.ehrlich.choix.0`)
- avant (de) : … Genau dafür ist die Untersuchung. Die Ärztin bespricht das Ergebnis heute noch mit Ihnen.
- après (de) : … Genau dafür ist die Untersuchung. Die Ärztin bespricht das Ergebnis mit Ihnen, sobald es da ist.
- après (fr) : … C'est justement pour ça qu'on fait l'examen. La médecin vous expliquera le résultat dès qu'il sera là.
- fait retenu : la soignante ne promet pas un délai (« aujourd'hui même ») à la place de la médecin. Texte identique
  dans les trois avis.
- écarté : rien.

#### ch07-2173f8 — APPLIQUÉ (en partie) + une question POUR LA SOIGNANTE — Dialogues · Das Knie tut weh · A2
- fichier : pflege/sources/dialogues/d28-knieschmerzen.json (`noeuds.arzt.choix.0`, `relire_notes`)
- avant (de) : Heute Abend komme ich wieder. Wenn es dann nicht besser ist, rufe ich Ihren Hausarzt an.
- après (de) : Ich sage heute im Pflegedienst Bescheid. Heute Abend komme ich wieder. Wenn es dann nicht besser ist,
  rufe ich Ihren Hausarzt an.
- après (fr) : Je préviens le service de soins aujourd'hui. Je reviens ce soir. Si ça ne va pas mieux, j'appelle
  votre médecin traitant.
- `relire_notes` : « … ; la soignante prévient son service (Pflegefachkraft) le jour même ; appel au médecin traitant
  si ça ne va pas mieux le soir (à valider : avec 7 sur 10 la nuit, plutôt le jour même ?) ; … »
- fait retenu : mesures justes (froid enveloppé, jambe surélevée, aucun antidouleur non prescrit) ; une douleur à
  7 sur 10 la nuit avec un genou gonflé chez une diabétique âgée se signale le jour même à la Pflegefachkraft (au
  service).
- POUR LA SOIGNANTE : faut-il informer le cabinet du médecin traitant le jour même, au lieu d'attendre le soir ?
  Les avis penchent pour le jour même mais sans le poser en règle (« beaucoup de services », « sans attendre
  nécessairement le soir », et la phrase proposée par Gemini garde « on surveille, et si ça augmente on informe la
  médecin »). Je n'ai donc pas réécrit la fin du dialogue (le redemittel « Wenn es heute Abend nicht besser ist,
  rufe ich Ihren Hausarzt an », la réponse « Dann warte ich bis heute Abend », l'aide de la réponse fausse et la
  question d'écoute restent).
- écarté : la phrase de Gemini (une seule longue phrase, niveau B1, pour un dialogue A2).

#### ch07-a195a6 — APPLIQUÉ — Dialogues · Das Knie tut weh · A2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d28-knieschmerzen.json (`noeuds.arzt.choix.1`)
- avant (de) : Noch nicht. Aber wenn das Knie rot oder heiß wird, rufen Sie uns bitte sofort an. Dann rufe ich Ihren
  Hausarzt an.
- après (de) : Noch nicht. Aber wenn das Knie rot, heiß oder dicker wird oder wenn Sie Fieber bekommen, rufen Sie uns
  bitte sofort an. Dann rufe ich Ihren Hausarzt an.
- après (fr) : Pas encore. Mais si le genou devient rouge, chaud ou plus gonflé, ou si vous avez de la fièvre,
  appelez-nous tout de suite, s'il vous plaît. Alors j'appellerai votre médecin traitant.
- fait retenu : aux signes d'alerte (rougeur, chaleur) s'ajoutent le gonflement qui augmente et la fièvre.
- écarté : « impossibilité d'appuyer » (un avis sur trois, et la phrase devenait trop longue pour l'A2) ; la
  suppression de « Noch nicht » (ChatGPT seul ; liée à la question « le jour même ? » ci-dessus) ; « sagen Sie uns
  gleich Bescheid » au lieu de « rufen Sie uns sofort an » (Gemini seul).

#### ch07-9ad21e — APPLIQUÉ (par les quatre points suivants) + deux questions POUR LA SOIGNANTE — Dialogues · Nachts Schmerzen: den Dienstarzt anrufen · B2
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`relire_notes` ; le détail aux points b032e0,
  c95da4, eab98c, 42868d, bffd23)
- `relire_notes`, trois retouches : « contrôles infirmiers (pansement sec, pied chaud et rose, orteils mobiles,
  sensibilité, jambe ni raccourcie ni tournée) » ; « dose UNIQUE (forme et voie à valider ; nombre de gouttes selon
  la concentration du produit, non chiffré) » ; « réévaluation à 30 minutes, dans la fourchette de 30 à 60 min selon
  le médicament et le standard de la maison (douleur et tension …) ».
- fait retenu : après une prothèse de hanche on rapporte aussi la position de la jambe ; le nombre de gouttes dépend
  de la concentration du produit ; la relecture se dit « Ich wiederhole ».
- le délai de 30 minutes de ce dialogue n'est PAS changé dans les répliques (« In einer halben Stunde frage ich noch
  einmal nach der Schmerzstärke und messe den Blutdruck », « in dreißig Minuten », l'aide, la question d'écoute) :
  aucun des trois avis ne le met en cause ici (« contrôle à 30 min avec la tension » jugé cohérent, la phrase de
  Gemini garde « in dreißig Minuten »), c'est un plan annoncé au médecin et accepté par lui, et 30 minutes est dans
  la fourchette. À changer si le chef veut la même formule partout (voir « Doutes »).
- POUR LA SOIGNANTE (1) : avec une douleur NOUVELLE à 8 sur 10 sur une hanche opérée, le médecin de garde
  viendrait-il voir le patient au lieu de prescrire par téléphone ? Les trois avis l'évoquent (« beaucoup
  attendraient », « à envisager », « souvent »). C'est la décision du médecin, pas un geste du soignant : texte
  laissé (« das klingt nicht nach einer Komplikation »).
- POUR LA SOIGNANTE (2) : la prescription téléphonique n'est admise que par exception, selon la règle de la maison :
  le dialogue la documente et la fait signer, mais ne dit pas « par exception ».
- écarté : « also 40 Tropfen » (voir eab98c).

#### ch07-b032e0 — APPLIQUÉ — Dialogues · Nachts Schmerzen: den Dienstarzt anrufen · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`noeuds.werte.choix.0`, avec son `dit` ; et la
  citation de l'aide `noeuds.werte.choix.2.aide`)
- avant (de) : … Der Verband ist trocken, das Bein ist warm, er kann die Zehen bewegen und spürt alles.
- après (de) : … Der Verband ist trocken, der Fuß ist warm und rosig, er kann die Zehen bewegen und spürt alles. Das
  Bein ist nicht verkürzt und nicht verdreht.
- après (fr) : … Le pansement est sec, le pied est chaud et rose, il bouge les orteils et il sent tout. La jambe
  n'est ni raccourcie ni tournée.
- aide de la réponse fausse : la citation devient « Blutdruck 150 zu 85, Puls 96 … Der Verband ist trocken, der Fuß
  ist warm und rosig. »
- fait retenu : « das Bein ist warm » est ambigu (circulation ou infection) ; on décrit le pied (chaud, rose) et,
  après une prothèse de hanche, la position de la jambe (ni raccourcie ni tournée). Même texte dans les trois avis.
- écarté : rien. Remarque : « rosig » et « nicht verkürzt, nicht verdreht » sont des constats normaux de plus, mais
  ce sont ceux des trois avis, et ils vont avec la réponse du médecin (« das klingt nicht nach einer Komplikation »).

#### ch07-c95da4 — APPLIQUÉ — Dialogues · Nachts Schmerzen: den Dienstarzt anrufen · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`noeuds.werte.choix.1`, avec son `dit`)
- avant (de) : … Verband trocken, Durchblutung, Motorik und Gefühl in Ordnung.
- après (de) : … Verband trocken, Durchblutung, Motorik und Sensibilität in Ordnung.
- après (fr) : inchangé (« … circulation, mobilité et sensibilité normales »). Les 9 traductions gardées, seul
  l'allemand de référence est mis à jour dans les fichiers de traduction.
- fait retenu : le contrôle DMS se dit « Durchblutung, Motorik, Sensibilität ». Trois avis identiques.
- écarté : rien.

#### ch07-eab98c — APPLIQUÉ — Dialogues · Nachts Schmerzen: den Dienstarzt anrufen · B2 · kraemer
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`noeuds.problem.choix.0.puis.0` et
  `noeuds.problem.choix.1.puis.0`, la même réplique du médecin ; `relire_note` complétée)
- avant (de) : Ach so, da fehlt die Dosis. Dann geben Sie ihm jetzt einmalig ein Gramm Metamizol als Tropfen. Die
  Bedarfsanordnung soll morgen {sommer} bei der Visite festlegen. Ich komme gegen sieben vorbei und unterschreibe die
  Anordnung.
- après (de) : Ach so, da fehlt die Dosis. Dann geben Sie ihm jetzt einmalig ein Gramm Metamizol als Tropfen. Die
  Tropfenzahl richtet sich nach der Konzentration des Präparats. Die Bedarfsanordnung soll morgen {sommer} bei der
  Visite festlegen. Ich komme gegen sieben vorbei und unterschreibe die Anordnung.
- après (fr) : Ah, la dose manque. Alors donnez-lui maintenant, une seule fois, un gramme de métamizole en gouttes. Le
  nombre de gouttes dépend de la concentration du produit. La prescription « si besoin », {sommer} la fixera demain à
  la visite. Je passe vers sept heures et je signe la prescription.
- fait retenu : la dose unique d'un gramme en gouttes est plausible ; le nombre de gouttes dépend de la
  concentration du produit (notice) et ne se devine pas.
- écarté : « also 40 Tropfen » (premier relecteur) : nombre que le cas ne contient pas, refusé par les deux autres
  avis (il ne vaut que pour une concentration). La phrase de Gemini (« bitte genau nach der Tropfenanzahl für unsere
  Lösung ») : même idée, moins claire.

#### ch07-42868d — APPLIQUÉ — Dialogues · Nachts Schmerzen: den Dienstarzt anrufen · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`noeuds.zuruecklesen.choix.0` ; citation de
  l'aide `noeuds.zuruecklesen.choix.2.aide`)
- avant (de) : Ich lese zurück: einmalig ein Gramm Metamizol als Tropfen, jetzt. Die Bedarfsanordnung legt {sommer}
  morgen fest, und Sie unterschreiben die Anordnung gegen sieben.
- après (de) : Ich wiederhole: einmalig ein Gramm Metamizol als Tropfen, jetzt. Die Bedarfsanordnung legt {sommer}
  morgen fest, und Sie unterschreiben die Anordnung gegen sieben.
- après (fr) : Je répète : une seule fois un gramme de métamizole en gouttes, maintenant. La prescription « si
  besoin », {sommer} la fixe demain, et vous signez la prescription vers sept heures.
- aide de la réponse fausse : la citation devient « Ich wiederhole: einmalig ein Gramm Metamizol als Tropfen. » (le
  reste de l'aide, « On relit une prescription orale mot pour mot », est gardé).
- fait retenu : la relecture est la bonne pratique ; dans un service on dit « Ich wiederhole », « Ich lese zurück »
  est un calque. ChatGPT et Gemini donnent le même texte.
- écarté : « also 40 Tropfen » (comme ci-dessus). L'intro et le but du dialogue gardent « relis-la mot pour mot »
  (ils décrivent le geste, pas la formule) ; la clé du nœud `zuruecklesen` n'est pas renommée.

#### ch07-5b698e — APPLIQUÉ — Dialogues · Das Handgelenk am Tag danach · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d32-handgelenk.json (`noeuds.toilette.choix.1` et sa réponse
  `noeuds.toilette.choix.1.puis.0`)
- avant (de) : … Trinken Sie lieber bis zum Nachmittag, und nachts bleibt jetzt das kleine Licht an. · (réponse)
  Bis zum Nachmittag mehr, abends weniger. Das kann ich mir merken.
- après (de) : … Trinken Sie lieber tagsüber mehr und abends etwas weniger, und nachts bleibt jetzt das kleine Licht
  an. · (réponse) Tagsüber mehr, abends weniger. Das kann ich mir merken.
- après (fr) : … Buvez plutôt plus dans la journée et un peu moins le soir, et la nuit, la petite lumière reste
  allumée maintenant. · (réponse) Plus dans la journée, moins le soir. Ça, je peux le retenir.
- fait retenu : « bis zum Nachmittag » peut se comprendre « ne plus boire ensuite » ; on répartit la boisson dans la
  journée, sans priver. Même texte dans les trois avis. La réponse de Mme Weber est alignée (elle devient la même
  que sur l'autre chemin).
- écarté : rien.

#### ch07-2d8c48 — APPLIQUÉ — Dialogues · Das Handgelenk am Tag danach · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d32-handgelenk.json (`noeuds.aerztin.choix.1`)
- avant (de) : Gute Frage. Die Hausärztin weiß Bescheid und kommt am Montag. Wenn es vorher schlimmer wird, rufen wir
  den ärztlichen Bereitschaftsdienst.
- après (de) : Gute Frage. Die Hausärztin weiß Bescheid und kommt am Montag. Wenn die Schmerzen oder die Schwellung
  vorher zunehmen oder die Finger kalt werden, rufen wir den ärztlichen Bereitschaftsdienst.
- après (fr) : Bonne question. La médecin traitante est au courant, elle passe lundi. Si la douleur ou le gonflement
  augmentent avant, ou si les doigts deviennent froids, on appelle le service médical de garde.
- fait retenu : « schlimmer » est trop vague ; les signes concrets sont la douleur ou le gonflement qui augmentent
  et les doigts froids.
- écarté : « blass oder blau », « kribbeln », « informieren wir sofort die Pflegefachkraft », « Bei einem Notfall
  wählen wir die 112 » (un avis chacun ; phrase trop longue ; le fourmillement est déjà dans la dernière réplique du
  dialogue). Le choix d'attendre lundi : voir ch07-602397.

#### ch07-8d52d7 — APPLIQUÉ — Dialogues · „Niemand tut etwas!“ · B2 · soignant(e) · réponse fausse
- fichier : pflege/sources/dialogues/d33-tochter-schmerzen.json (`noeuds.erklaeren.choix.2.aide`)
- avant (de) : réponse fausse inchangée (« Darüber darf ich Ihnen leider gar nichts sagen. Das ist
  Schweigepflicht. ») : elle reste fausse.
- après (de) : inchangé.
- après (fr), l'aide : « <b>Le secret ne vaut pas contre une proche que la patiente a autorisée.</b> Ici, la levée du
  secret est au dossier : tu peux dire ce qui a été fait pour la douleur. Sans cette autorisation, ta réponse serait
  la bonne. Le diagnostic et le choix du traitement, eux, reviennent à la médecin. »
- fait retenu : la réponse n'est fausse que parce que la mère a levé le secret pour sa fille ; sans cette
  autorisation, ce serait la bonne réponse. L'aide le dit maintenant en clair.
- écarté : les deux phrases allemandes proposées (ChatGPT, Gemini) : ce sont d'autres répliques, pas l'aide ; la
  bonne réponse du dialogue dit déjà « Ihre Mutter hat erlaubt, dass wir Sie informieren ».

#### ch07-c7ffa3 — APPLIQUÉ — Mots · soins_koerper_b1
- fichier : pflege/sources/vocabulaire/t01_koerper.py — `R("B1", "wirken")` (exemple, 10 langues, note)
- avant (de) : Das Schmerzmittel wirkt nach etwa einer halben Stunde: Dann frage ich noch einmal nach.
- après (de) : Das Schmerzmittel wirkt nach etwa einer halben bis einer Stunde: Dann frage ich noch einmal nach.
- après (fr) : L'antalgique agit au bout d'une demi-heure à une heure environ : je repasse alors vous demander.
- fait retenu : un antalgique oral agit en 30 à 60 minutes selon la substance et la forme ; la demi-heure n'est pas un
  délai systématique, la réévaluation suit le standard de la maison.
- écarté : la phrase de Gemini (« braucht meist eine Weile ») : elle retire toute durée, alors que deux avis donnent la
  même fourchette.

#### ch07-9f2178 — APPLIQUÉ — Mots · soins_koerper_b2
- fichier : pflege/sources/vocabulaire/t01_koerper.py — `N("B2", "die Schmerzeinschätzung")` (exemple, 10 langues, note)
- avant (de) : Weil er nicht mehr sprechen kann, machen wir die Schmerzeinschätzung mit der BESD.
- après (de) : Weil er wegen seiner Demenz nicht mehr sagen kann, ob er Schmerzen hat, machen wir die Schmerzeinschätzung mit der BESD.
- après (fr) : Comme sa démence l'empêche de dire s'il a mal, nous évaluons la douleur avec l'échelle BESD.
- fait retenu : la BESD vaut pour les personnes démentes, pas pour toute personne qui ne parle plus ; c'est la version
  allemande de la PAINAD ; Algoplus et Doloplus sont des échelles voisines, pas des équivalents (note réécrite).
- écarté : la variante de Gemini (« schätzen wir die Schmerzen … ein ») : elle perd le mot de la carte.

#### ch07-c7ef8d — APPLIQUÉ — Mots · soins_koerper_b2
- fichier : pflege/sources/vocabulaire/t01_koerper.py — `N("B2", "die Schmerzanamnese")` (exemple, 10 langues, note ajoutée)
- avant (de) : Bei der Aufnahme erhebt {Elif} eine ausführliche Schmerzanamnese.
- après (de) : Bei der Aufnahme erhebt die Pflegefachkraft eine ausführliche Schmerzanamnese.
- après (fr) : À l'admission, l'infirmière diplômée recueille une anamnèse détaillée de la douleur.
- fait retenu : le recueil du besoin en soins, dont l'anamnèse de la douleur, revient à la Pflegefachkraft ; une aide
  observe et transmet. Traductions avec les termes de la paire « die Schwester → die Pflegefachkraft » (registered
  nurse, diplomalı hemşire, enfermera titulada…).
- écarté : la phrase de Gemini (« … und ich unterstütze sie dabei und gebe meine Beobachtungen weiter ») : plus longue.

#### ch07-2e4f09 — APPLIQUÉ — Mots · soins_koerper_b2
- fichier : pflege/sources/vocabulaire/t01_koerper.py — `N("B2", "die Hüft-TEP")` (exemple, 10 langues, note)
- avant (de) : {Herr Brandt} hat seit Montag eine Hüft-TEP rechts und darf heute zum ersten Mal mit dem Rollator gehen.
- après (de) : {Herr Brandt} hat seit Dienstag eine Hüft-TEP rechts und darf heute zum ersten Mal mit dem Rollator gehen.
- après (fr) : M. Brandt a une prothèse totale de hanche droite depuis mardi et peut marcher aujourd'hui pour la première fois avec le déambulateur.
- fait retenu : le jour de l'opération doit être celui du reste du lot ; d06 et d07 disent « am Dienstag operiert »,
  e01 et d38 le 10.11. (un mardi en 2026). TEP = Totalendoprothese (note corrigée) ; le premier lever dépend de la
  clinique et de la prescription (note).
- écarté : la phrase de Gemini (« nach ärztlicher Anordnung und mit Unterstützung mobilisiert werden ») : elle retire le
  jour et le déambulateur ; le changement d'un seul mot suffit.

#### ch07-675c2d — APPLIQUÉ (le mot de la paire est gardé : voir « Doutes ») — Paires patient / service · soins_sprache_b1
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B1", "das Bauchweh", "die Abdominalschmerzen")` (exemple du
  service, traduction du service, note)
- avant (de) : {Herr Schulze} klagt seit dem Morgen über Abdominalschmerzen.
- après (de) : {Herr Schulze} gibt seit dem Morgen Abdominalschmerzen an.
- après (fr) : M. Schulze signale des douleurs abdominales depuis le matin. — et la traduction du mot : « les douleurs
  abdominales (au dossier, le plus souvent « Bauchschmerzen ») », dans les 10 langues.
- fait retenu : « Abdominalschmerzen » existe mais reste rare, la documentation soignante écrit « Bauchschmerzen » ;
  « gibt … an » est plus neutre que « klagt über ».
- écarté : la phrase commune aux trois avis telle quelle (« … gibt seit dem Morgen Bauchschmerzen an ») : elle retire de
  l'exemple le mot que la carte enseigne. Changer le mot de la paire lui-même aurait touché des fichiers hors de ma
  mission (`chapitres_mots.py`, le thème illustré de la douleur, `FORMAT-DONNEES.md`).

#### ch07-5d3f60 — APPLIQUÉ (note seule) — Paires patient / service · soins_sprache_b1
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B1", "spucken (sich übergeben)", "erbrechen")`
- avant / après (de) : {Herr Schulze} hat nachts zweimal erbrochen, ohne Blutbeimengung. (inchangé)
- après (note) : … « spucken » au sens de vomir est familier. (« , surtout dans le nord » retiré)
- fait retenu : aucun des trois avis ne confirme la précision régionale.
- écarté : la phrase allongée de Gemini (« ohne sichtbare Blutbeimengung; Menge und Verlauf werden weiter beobachtet ») :
  l'allemand n'est pas en cause.

#### ch07-dc1b0f — APPLIQUÉ — Paires patient / service · soins_sprache_b1
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B1", "Es zieht bis in den Arm.", "ausstrahlende Schmerzen")`
  (exemple du service, 10 langues, note, `LECTURES`)
- avant (de) : Der Patient hat Brustschmerzen, die in den linken Arm ausstrahlen: sofort den Arzt rufen.
- après (de) : Der Patient hat Brustschmerzen, die in den linken Arm ausstrahlen: sofort den Arzt rufen, im Pflegeheim und in der ambulanten Pflege den Notruf 112.
  (lecture : « … den Notruf eins eins zwei. », au style de « die 112 » du thème des urgences)
- après (fr) : Le patient a des douleurs dans la poitrine qui irradient dans le bras gauche : appeler tout de suite le médecin ; en maison de retraite et à domicile, le 112.
- fait retenu : à l'hôpital on prévient le médecin, en maison de retraite et à domicile on appelle le 112 ; on ne
  laisse pas le patient seul (dans la note).
- écarté : les phrases de ChatGPT et de Gemini (deux phrases, « Notfallstandard einleiten », « Notfallteam ») : plus
  longues, au-dessus du B1 de la paire.

#### ch07-43e351 — APPLIQUÉ — Paires patient / service · soins_sprache_b2
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B2", "Es kribbelt in den Fingern.", "die Parästhesien")`
  (exemple du service, 10 langues, note)
- avant (de) : Die Patientin gibt seit dem Morgen Parästhesien in der rechten Hand an; Kraft und Sprache sind unauffällig.
- après (de) : Die Patientin gibt seit dem Morgen Parästhesien in der rechten Hand an; Kraft und Sprache sind unauffällig, der Arzt ist informiert.
- après (fr) : La patiente signale des paresthésies de la main droite depuis le matin ; force et parole normales, médecin prévenu.
- fait retenu : des fourmillements nouveaux d'un seul côté se signalent au médecin, même sans faiblesse ni trouble de la
  parole.
- écarté : « aktuell unauffällig, ich gebe das direkt an den Arzt weiter » (Gemini) : même fait, plus long.

#### ch07-bffd23 — APPLIQUÉ — Phrases du service · soins_rm_30_5
- fichier : pflege/sources/dialogues/d30-schmerz-nachts-arzt.json (`redemittel.5`, la carte soins_rm_30_5)
- avant (de) : Ich lese zurück: einmalig ein Gramm Metamizol als Tropfen.
- après (de) : Ich wiederhole: einmalig ein Gramm Metamizol als Tropfen.
- après (fr) : Je répète : une seule fois un gramme de métamizole en gouttes.
- fait retenu : « Ich wiederhole » est la formule du service. Trois avis identiques.
- écarté : rien.

#### ch07-4dd0a9 — APPLIQUÉ — Écrits · soins_ecrit_schmerz_01
- fichier : pflege/sources/ecrit/e13-schmerzprotokoll-brandt.json (`relire_notes`, `pieges.1`, `pieges.2`)
- avant (de) / après (de) : aucun texte allemand changé. La fiche, les points et le modèle gardent leurs heures
  (10:05 la prise, 10:35 le contrôle : 30 minutes, dans la fourchette) et « Metamizol 1 g oral nach
  Bedarfsanordnung ».
- après (fr), `pieges.1` : « Le médicament se note avec la dose, la voie et la raison : « Metamizol 1 g oral nach
  Bedarfsanordnung ». L'indication, la dose par prise, l'intervalle minimal et la dose maximale par 24 heures
  figurent dans la prescription. »
- après (fr), `pieges.2` : « Sans contrôle, la note est incomplète : écris l'heure et la valeur de la réévaluation
  (« 10:35 Uhr: NRS 3 »). Après une prise orale, le contrôle se fait 30 à 60 minutes plus tard, selon le médicament
  et le standard de la maison. »
- `relire_notes` : « … (métamizole 1 g si douleur au-dessus de 3, dialogue 18 ; l'indication, la dose par prise,
  l'intervalle minimal et la dose maximale par 24 h figurent dans la prescription, non chiffrés ici), réévaluation
  30 à 60 min après une prise orale, selon le médicament et le standard de la maison (ici 30 min) ; … »
- fait retenu : une Bedarfsanordnung complète porte l'indication, la dose par prise, l'intervalle minimal et la dose
  maximale par 24 h ; le contrôle après une prise orale se fait entre 30 et 60 minutes selon le médicament et le
  standard de la maison.
- écarté : tout chiffre d'intervalle ou de dose maximale (le cas n'en contient pas) ; l'extrait de documentation de
  Gemini (« Schmerzstärke aktuell 4/10 … ohne Ausstrahlung ») : valeurs qui contredisent la fiche (7 au repos,
  irradiation jusqu'au genou).

---

### La relève (ch. 8)

#### ch08-d6d7ec — APPLIQUÉ — Thème illustré · soins-theme-uebergabe
- fichier : pflege/outils/themes_soins/uebergabe.py (la feuille de relève de Frau Weber) et pflege/sources/themes_soins/uebergabe/<langue>.json
- avant (de) : Röntgen li. Handgelenk um 11:00 / Um elf Uhr wird das linke Handgelenk geröntgt.
- après (de) : Hausärztin kommt am Montag / Am Montag kommt die Hausärztin und sieht sich das Handgelenk an.
- après (fr) : Lundi, la médecin traitante passe et regarde le poignet.
- fait retenu : la radio à 11 h contredisait les dialogues d32 et d36 (la médecin traitante passe lundi et décide). Chaque feuille porte déjà son lieu en titre (« Übergabe · Haus Lindenhof », « Übergabe · Station 4B ») : les résidents et les patients de l'hôpital ne sont pas sur une même liste.

#### ch08-189040 — APPLIQUÉ — Dialogues · Die Übergabe · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d06-uebergabe.json (`noeuds.bedarf.choix.0`)
- avant (de) : Ja, um zehn hat er sein Schmerzmittel bei Bedarf bekommen. Eine halbe Stunde später lag er bei drei.
- après (de) : Ja, um zehn hat er seine Bedarfsmedikation gegen die Schmerzen bekommen. Eine halbe Stunde später lag er bei drei.
- après (fr) : Oui, à dix heures il a eu son traitement si besoin contre la douleur. Une demi-heure plus tard, il était à trois.
- fait retenu : le mot du service est « Bedarfsmedikation », pas « Schmerzmittel bei Bedarf bekommen ».
- écarté : nommer le médicament et la dose (les trois le souhaitent pour une vraie relève, mais le cas de d06 ne les
  donne pas : donnée inventée) ; « lag der Schmerz bei drei » (ChatGPT, Gemini) : « er lag bei drei » est le parler du
  service employé ailleurs (d27, d37) et n'est pas en cause.

#### ch08-b37e63 — APPLIQUÉ — Dialogues · Die Übergabe am Abend · B1
- fichier : pflege/sources/dialogues/d27-abenduebergabe.json (tout le dialogue : `redemittel.4`,
  `noeuds.ergebnis.choix.0`, `.choix.1`, `.choix.2.aide`, `relire_notes`)
- avant (de) : … Wenn er noch über 6 ist, ruf bitte den Dienstarzt an. / … Ist der Wert noch über 6, informierst du den Dienstarzt.
- après (de) : voir ch08-b43dc3 et ch08-722f29 ; second choix juste : « Noch nicht. Schau bitte um 22 Uhr nach. Laut
  ärztlicher Anordnung: Ist der Wert noch über 6, informierst du sofort den Dienstarzt. » (`dit` mis à jour)
- après (fr) : « Pas encore. Regarde à 22 h, s'il te plaît. Selon la prescription médicale : si la valeur est encore
  au-dessus de 6, tu préviens tout de suite le médecin de garde. » ; aide du mauvais choix : la phrase citée prend
  « sofort », plus « La limite, c'est la médecin qui l'a prescrite. » ; `relire_notes` : « appeler tout de suite le
  médecin de garde si la valeur reste au-dessus de 6 (seuil fixé par la prescription de la médecin) ».
- fait retenu : le seuil d'appel vient de la prescription médicale, pas de la soignante, et l'appel est immédiat ; le
  métamizole 1 g au plus tôt toutes les six heures est confirmé (rien changé).
- écarté : un ECG et un contrôle plus rapproché que huit heures à 6,2 mmol/l (le premier relecteur dit lui-même « à
  faire confirmer par un médecin » ; le cas ne les contient pas : voir Doutes) ; « Kaliumwert … liegt » (ChatGPT) : le
  mot « Wert » du dialogue suffit ; la valeur 6 et les heures (20 h, 22 h) restent celles du cas.

#### ch08-b43dc3 — APPLIQUÉ — Dialogues · Die Übergabe am Abend · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d27-abenduebergabe.json (`noeuds.ergebnis.choix.0`)
- avant (de) : Das Ergebnis ist noch nicht da. Bitte schau um 22 Uhr nach dem Laborwert. Wenn er noch über 6 ist, ruf bitte den Dienstarzt an.
- après (de) : Das Ergebnis ist noch nicht da. Bitte schau um 22 Uhr nach dem Laborwert. Wenn er noch über 6 ist, ruf bitte sofort den Dienstarzt an. Das hat die Ärztin so angeordnet.
- après (fr) : Le résultat n'est pas encore arrivé. Regarde la valeur du labo à 22 h, s'il te plaît. Si elle est encore au-dessus de 6, appelle tout de suite le médecin de garde. C'est ce que la médecin a prescrit.
- fait retenu : le seuil est une prescription de la médecin ; au-dessus, on appelle tout de suite.
- écarté : rien ; j'ai pris la forme en deux phrases (ChatGPT) plutôt que « …, so hat es die Ärztin angeordnet »
  (premier relecteur, Gemini) : même fait, phrases plus courtes pour un B1. `relire_note` : « Seuil d'appel du médecin
  de garde, fixé par la prescription de la médecin. »

#### ch08-dce28e — APPLIQUÉ — Dialogues · Die Übergabe am Morgen: nachfragen · A2
- fichier : pflege/sources/dialogues/d34-morgenuebergabe.json (tout le dialogue : `noeuds.nuechtern.choix.0.puis.0` et
  `.choix.1.puis.0`, `noeuds.nuechtern.choix.2.aide`, `noeuds.lehmann.choix.0.puis.0` et `.choix.1.puis.0`,
  `noeuds.notizen.choix.0` et `.choix.1`, `relire_notes`)
- avant (de) : Er darf nichts essen und nichts trinken. Und nicht rauchen. Bis zur Operation. / Fünf Komma vier. Das Ergebnis war um zweiundzwanzig Uhr da. Und sie hat gut geschlafen.
- après (de) : Er darf nichts essen und nichts trinken. Und nicht rauchen. Bis zur Operation. Das hat die Anästhesie so angeordnet. / Fünf Komma vier. Das Ergebnis war um zweiundzwanzig Uhr da. Das ist noch etwas zu hoch: Sag es bitte heute Morgen der Ärztin. Und sie hat gut geschlafen. / notes relues par Elif : « … {lehmann}: Kalium fünf Komma vier, der Ärztin sagen. … » et « … Zimmer 14, Kalium fünf Komma vier, Ärztin informieren. … » (`dit` mis à jour)
- après (fr) : Il ne doit rien manger et rien boire. Et ne pas fumer. Jusqu'à l'opération. C'est l'anesthésie qui l'a prescrit. / Cinq virgule quatre. Le résultat est arrivé à vingt-deux heures. C'est encore un peu trop haut : dis-le à la médecin ce matin, s'il te plaît. Et elle a bien dormi. / aide : « … À partir de quelle heure exactement, c'est l'anesthésie qui le fixe pour chaque patient. … »
- fait retenu : (1) le jeûne avant l'anesthésie suit la consigne de l'anesthésie et le protocole de la maison, ce
  n'est pas une règle générale ; (2) une kaliémie de contrôle à 5,4 après 6,2 reste au-dessus de la norme et se
  transmet à la médecin le matin même.
- écarté : « des liquides clairs jusqu'à deux heures avant » (premier relecteur, ChatGPT) : un délai que le cas ne
  donne pas, et d44 (hors mission) dit « nichts mehr trinken ab Mitternacht » ; la phrase longue de Gemini pour
  Mme Lehmann (« Kontroll-Kalium … wird der Ärztin gemeldet ») : trop longue pour un A2, le fait est porté par deux
  phrases courtes. Les notes relues à la fin reprennent la consigne, sinon « Perfekt. Alles richtig. » aurait validé
  des notes incomplètes. `relire_notes` mises à jour sur ces deux faits.

#### ch08-6ae5ce — APPLIQUÉ — Dialogues · Die Übergabe im Lindenhof · B1
- fichier : pflege/sources/dialogues/d36-uebergabe-altenheim.json (tout le dialogue : `redemittel.3`,
  `noeuds.aerztin.choix.1`, `relire_notes`)
- avant (de) : Wenn die Schmerzen vorher stärker werden oder die Finger kalt werden, ruf bitte den ärztlichen Bereitschaftsdienst an.
- après (de) : voir ch08-8965fb et ch08-23f6f9
- après (fr) : `relire_notes` : « appel du service médical de garde (116 117) si la douleur augmente ; le 112 tout de
  suite si les doigts deviennent froids, pâles ou engourdis (trouble de la circulation). »
- fait retenu : douleur qui augmente = service médical de garde ; doigts froids, pâles ou engourdis après un
  traumatisme = trouble de la circulation, urgence (112).
- écarté : rien sur le plan de boisson : la phrase dit déjà « Laut Trinkplan soll sie 1500 Milliliter … », l'objectif
  y est donc celui du plan de la résidente (les trois avis demandent seulement qu'il soit individuel) ; « attendre
  lundi seulement si une fracture est écartée » (premier relecteur seul) : relève de d32, voir Doutes.

#### ch08-8965fb — APPLIQUÉ — Dialogues · Die Übergabe im Lindenhof · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d36-uebergabe-altenheim.json (`noeuds.aerztin.choix.1`)
- avant (de) : Am Montag kommt die Hausärztin. Wenn die Schmerzen vorher stärker werden oder die Finger kalt werden, ruf bitte den ärztlichen Bereitschaftsdienst an.
- après (de) : Am Montag kommt die Hausärztin. Wenn die Schmerzen vorher stärker werden, ruf bitte den ärztlichen Bereitschaftsdienst an. Wenn die Finger kalt, blass oder taub werden, ruf sofort die 112. (`dit` ajouté : « … die eins eins zwei », comme dans d25)
- après (fr) : Lundi, la médecin traitante passe. Si la douleur augmente avant, appelle le service médical de garde, s'il te plaît. Si les doigts deviennent froids, pâles ou engourdis, appelle tout de suite le 112.
- fait retenu : séparer les deux signes ; les doigts froids, pâles ou engourdis sont une urgence.
- écarté : « plötzlich kalt, blass oder blau … oder taub sind, muss die Hand sofort ärztlich untersucht werden »
  (ChatGPT) : plus long, et ChatGPT donne lui-même « ruf bitte sofort die 112 » pour la phrase du service ; « blau »
  n'est que chez lui. Deux phrases au lieu du point-virgule, pour un B1. `relire_note` mise à jour.

#### ch08-748563 — APPLIQUÉ — Dialogues · Die Übergabeliste · B2
- fichier : pflege/sources/dialogues/d38-uebergabeliste.json (`intro`)
- avant (de) : (pas d'allemand : texte d'introduction)
- après (de) : (aucun allemand changé pour ce point)
- après (fr) : « … écrite en style télégraphique : des abréviations, des chiffres, pas de verbes. Ces abréviations sont celles de ce service : elles changent d'une maison à l'autre. Entre collègues, on se dit « du ». … »
- fait retenu : les abréviations de la liste sont réelles mais varient d'un établissement à l'autre (surtout « Mob.
  n. AO »).
- écarté : expliciter « n. AO » : le dialogue le fait déjà (Elif le demande, Jonas confirme, et « Er wird nach
  ärztlicher Anordnung mobilisiert » est une phrase du service) ; la ligne type de Gemini (« Z. n. Hüft-TEP re., VB
  tr., Mob. n. AO, BZ nach Schema ») : mélange deux patients. La sonde urinaire gardée trois jours : le fait est dans
  d17 (hors mission), d38 dit seulement qu'il a une sonde le jour de l'opération : rien changé, voir « À harmoniser ».

#### ch08-8d17f3 — APPLIQUÉ — Dialogues · Die Übergabeliste · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d38-uebergabeliste.json (`noeuds.lehmann.choix.1`)
- avant (de) : … Der Verband wurde heute gewechselt, die Wunde sieht ruhig aus.
- après (de) : … Der Verband wurde heute gewechselt, die Wunde sieht unauffällig aus. (`dit` mis à jour ; le reste de la phrase, glycémie 162 à onze heures et demie, est inchangé)
- après (fr) : … Le pansement a été changé aujourd'hui, la plaie n'a rien de particulier.
- fait retenu : « ruhig » n'est pas le mot du service pour une plaie ; on dit « unauffällig » (ou « reizlos », déjà
  dans l'autre choix juste).
- écarté : rien. `relire_note` : « Glycémie et insuline selon schéma ; « unauffällig » pour la plaie. »

#### ch08-31c966 — APPLIQUÉ — Dialogues · Die Teambesprechung am Morgen · B2
- fichier : pflege/sources/dialogues/d39-teambesprechung.json (`noeuds.pohl.choix.0`, `.choix.1`, `relire_notes`)
- avant (de) : … Die Blutkulturen von Samstag sind bisher negativ. / … Blutkulturen von Samstag bisher negativ.
- après (de) : … Die Blutkulturen von Samstag sind bisher negativ. Der Nachtdienst hat den Dienstarzt informiert. / … Blutkulturen von Samstag bisher negativ. Dienstarzt in der Nacht informiert. (`dit` mis à jour ; valeurs 38,3, pouls 96, douleur 5 sur 10 inchangées)
- après (fr) : … Les hémocultures de samedi sont négatives pour l'instant. L'équipe de nuit a prévenu le médecin de garde. / … Hémocultures de samedi négatives pour l'instant. Médecin de garde prévenu dans la nuit.
- fait retenu : une fièvre nouvelle à 4 h avec douleur abdominale chez un opéré se signale au médecin de garde par
  l'équipe de nuit, et le dialogue doit dire si cela a été fait ; l'ordre de priorité est confirmé.
- écarté : « quelle conduite a été décidée » (ChatGPT) : ce serait inventer une prescription ; la phrase de Gemini
  (« wir messen sofort die Vitalzeichen und informieren die Ärztin ») redit le nœud suivant. Voir Doutes : c'est un
  fait d'histoire ajouté, noté « à valider » dans `relire_note` et `relire_notes`.

#### ch08-f45a7d — APPLIQUÉ — Mots · soins_team_b2
- fichier : pflege/sources/vocabulaire/t08_team.py — `X("B2", "die Bezugspflege / die Bereichspflege")` (exemple, 10 langues, note)
- avant (de) : In der Bezugspflege bleibt ein Patient während des ganzen Aufenthalts bei derselben Pflegekraft, in der Bereichspflege übernimmt jede Pflegekraft pro Schicht die Zimmer eines Bereichs.
- après (de) : In der Bezugspflege ist eine feste Pflegekraft während des ganzen Aufenthalts für einen Patienten verantwortlich, in der Bereichspflege übernimmt jede Pflegekraft pro Schicht die Zimmer eines Bereichs.
- après (fr) : Dans les soins par référent, un même soignant est responsable du patient pendant tout son séjour ; dans les soins par secteur, chaque soignant prend en charge, à chaque poste, les chambres d'un secteur.
- fait retenu : la soignante référente est responsable du patient, elle n'est pas présente à chaque poste (texte
  identique du premier relecteur et de Gemini).
- écarté : « eines bestimmten Bereichs » et la coupe en deux phrases (ChatGPT) : sans effet sur le fait.

#### ch08-983227 — APPLIQUÉ — Paires patient / service · soins_sprache_b2
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B2", "blaue Lippen", "die Zyanose")` (exemple du service, 10 langues, note)
- avant (de) : Der Patient zeigt eine zentrale Zyanose der Lippen; die Sauerstoffsättigung ist gemessen, der Arzt sofort informiert.
- après (de) : Der Patient zeigt eine Lippenzyanose; die Sauerstoffsättigung ist gemessen, der Arzt sofort informiert.
- après (fr) : Le patient présente une cyanose des lèvres ; saturation mesurée, médecin prévenu immédiatement.
- fait retenu : des lèvres bleues ne suffisent pas à dire « centrale » (c'est la langue et la muqueuse qui la
  distinguent) ; la soignante décrit ce qu'elle voit, elle ne classe pas. Note réécrite dans ce sens.
- écarté : « Die Lippen wirken bläulich » (Gemini) : perd le mot de la carte.

#### ch08-0a0a74 — APPLIQUÉ (note seule) — Paires patient / service · soins_sprache_b2
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B2", "Er läuft die ganze Nacht herum.", "die nächtliche Unruhe")`
- avant / après (de) : Ausgeprägte nächtliche Unruhe: Der Bewohner hat mehrmals versucht, den Wohnbereich zu verlassen. (inchangé)
- après (note) : le « Sundowning » désigne l'agitation de fin d'après-midi et de soirée ; une mesure qui enferme ou
  attache repose sur le consentement du résident, ou sur la décision du Betreuer ou du mandataire avec l'accord du
  Betreuungsgericht (§ 1831 BGB, à vérifier), pas sur la seule décision du médecin.
- fait retenu : la phrase allemande est juste (les trois) ; la note donnait deux choses inexactes.
- écarté : l'ajout de Gemini à la phrase (« wir prüfen mögliche Ursachen und achten auf seine Sicherheit »).

#### ch08-1a6000 — APPLIQUÉ (note seule) — Abréviations · soins_dokumentation_b1
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B1", "BZ (= Blutzucker)")`
- avant / après (de) : Der BZ war vor dem Frühstück zweihundertzehn, ich habe nach Schema gespritzt. (inchangé)
- après (note) : la valeur est « le plus souvent » en mg/dl, « mais certains établissements travaillent en mmol/l » ;
  « nach Schema » = le schéma d'insuline prescrit.
- fait retenu : « BZ » et « nach Schema » sont justes ; les mg/dl dominent sans être la seule unité.
- écarté : « surtout dans les Länder de l'Est » (premier relecteur seul, ChatGPT le déconseille) ; « bei 210 mg/dl »
  (Gemini) : des chiffres dans une phrase dite.

#### ch08-bce4b0 — APPLIQUÉ — Abréviations · soins_dokumentation_b1
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B1", "bds. (= beidseits)")` (exemple, 10 langues, note)
- avant (de) : Die Unterschenkel sind beidseits geschwollen, die Beine bitte hochlagern.
- après (de) : Die Unterschenkel sind beidseits geschwollen, ich informiere die Ärztin; die Beine lagern wir nur nach Anordnung hoch.
- après (fr) : Les jambes sont gonflées des deux côtés, je préviens la médecin ; nous ne les surélevons que sur prescription.
- fait retenu : des œdèmes bilatéraux nouveaux se signalent au médecin ; surélever les jambes n'est pas une consigne
  universelle (insuffisance cardiaque décompensée, artériopathie : dans la note).
- écarté : les deux phrases proposées (ChatGPT : « informieren Sie die Pflegefachkraft », Gemini : « ich gebe das weiter
  und lagere nach Anordnung ») ne s'accordent pas entre elles ; la mienne ne porte que ce qu'elles ont en commun. À faire
  relire (voir « Doutes »).

#### ch08-c991d9 — APPLIQUÉ (l'allemand et la note ; les traductions tiennent encore) — Abréviations · soins_dokumentation_b1
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B1", "Z.n. (= Zustand nach)")`
- avant (de) : Die Bewohnerin ist Zustand nach Schlaganfall, der rechte Arm ist noch schwach.
- après (de) : Die Bewohnerin, Zustand nach Schlaganfall, der rechte Arm ist noch schwach.
- après (fr) : La résidente a un antécédent d'AVC : le bras droit est encore faible. (inchangé)
- fait retenu : « ist Zustand nach » sonne faux, même en jargon ; à l'oral l'abréviation vient en apposition. La note,
  qui disait la tournure « correcte à la relève », est corrigée.
- écarté : « Frau Weber, Zustand nach Schlaganfall, … » (premier relecteur, Gemini) : Frau Weber est la résidente de la
  chute du dialogue 8, lui donner un AVC serait une donnée que le cas ne contient pas ; « Frau Weber hatte einen
  Schlaganfall » (ChatGPT) : perd l'abréviation. Les 10 traductions disaient déjà « a un antécédent d'AVC », « is status
  post stroke »… : elles correspondent toujours, je ne les ai pas touchées.

#### ch08-06893c — APPLIQUÉ — Abréviations · soins_dokumentation_b1
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B1", "OK (= Oberkörper)")` (exemple, 10 langues, note)
- avant (de) : Wegen der Atemnot bitte den Oberkörper hochlagern, das Kopfteil auf dreißig Grad.
- après (de) : Wegen der Atemnot bitte den Oberkörper hochlagern, möglichst aufrecht.
- après (fr) : À cause de l'essoufflement, surélevez le buste, s'il vous plaît, le plus droit possible.
- fait retenu : pour une dyspnée, trente degrés ne suffisent pas, on redresse davantage, jusqu'à la position assise
  selon la tolérance ; « OK hoch » est courant, « OKH » dépend de la maison (note).
- écarté : « mindestens auf fünfundvierzig Grad » (premier relecteur et Gemini) : ChatGPT refuse un angle fixe, et c'est
  une valeur que la source ne donnait pas (règle 3). Voir « Doutes ».

#### ch08-65abea — APPLIQUÉ — Abréviations · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B2", "PVK (= peripherer Venenkatheter)")` (exemple, 10
  langues, note, `LECTURES`)
- avant (de) : Der PVK, also die Braunüle am linken Handrücken, liegt seit drei Tagen, bitte heute kontrollieren.
- après (de) : Der PVK, also die Braunüle am linken Handrücken, liegt seit drei Tagen, die Einstichstelle ist reizlos.
- après (fr) : Le cathéter périphérique sur le dos de la main gauche est posé depuis trois jours, le point de ponction ne montre aucune irritation.
- fait retenu : le point de ponction se contrôle régulièrement, pas « aujourd'hui parce que c'est le troisième jour » ;
  le changement suit le protocole de la maison.
- écarté : « Flexüle à l'Est » (premier relecteur seul) ; « Bitte kontrollieren Sie heute die Einstichstelle »
  (ChatGPT) : garde l'idée d'un contrôle ce jour-là seulement.

#### ch08-da8dad — APPLIQUÉ — Abréviations · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B2", "Hb (= Hämoglobin)")` (exemple, en / tr / fa / ar /
  pl retouchés, note, `LECTURES`)
- avant (de) : Der Hb-Wert ist auf sieben Komma acht gefallen, die Ärztin bestellt zwei Blutkonserven.
- après (de) : Der Hb-Wert ist auf sieben Komma acht gefallen, die Ärztin bestellt zwei EKs. (lecture : « … zwei E-Kas. »)
- après (fr) : L'hémoglobine est descendue à sept virgule huit, la médecin commande deux culots globulaires. (inchangé :
  le français, le portugais, l'ukrainien, le russe et l'espagnol disaient déjà « culots globulaires » ; l'anglais, le
  turc, le persan, l'arabe et le polonais disaient « unités de sang » et disent maintenant le concentré de globules
  rouges)
- fait retenu : dans le service on dit « zwei EKs » (Erythrozytenkonzentrate) plutôt que « Blutkonserven » ; certains
  laboratoires rendent l'Hb en mmol/l (note).
- écarté : « auf 7,8 g/dl », « hat … angefordert » (Gemini) : des chiffres, et un temps changé sans raison.

#### ch08-1870b0 — APPLIQUÉ (la traduction du mot dans les 10 langues, et la note ; l'exemple ne change pas) — Abréviations · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B2", "KH (= Krankenhaus)")`
- avant / après (de) : Die Bewohnerin ist gestern Abend ins Krankenhaus eingewiesen worden, der Überleitungsbogen ist mitgegangen. (inchangé)
- après (fr, le mot) : l'hôpital (en diabétologie, « KH » = Kohlenhydrate, les glucides)
- fait retenu : « KH » peut se confondre avec Kohlenhydrate ; « eingewiesen » suppose une décision médicale (note).
- écarté : « mitgegeben worden » au lieu de « mitgegangen » (Gemini) : retouche de style, hors du fait.

#### ch08-722f29 — APPLIQUÉ — Phrases du service · soins_rm_27_4
- fichier : pflege/sources/dialogues/d27-abenduebergabe.json (`redemittel.4`, la phrase du service soins_rm_27_4)
- avant (de) : Wenn der Wert noch über 6 ist, ruf bitte den Dienstarzt an.
- après (de) : Laut ärztlicher Anordnung: Wenn der Wert noch über 6 ist, ruf bitte sofort den Dienstarzt an. (`dit` : « … über sechs … »)
- après (fr) : Selon la prescription médicale : si la valeur est encore au-dessus de 6, appelle tout de suite le médecin de garde, s'il te plaît.
- fait retenu : le seuil se présente comme une prescription médicale, et l'appel est immédiat.
- écarté : « Kaliumwert … liegt » (ChatGPT) : la carte reste proche de la phrase du dialogue. « Laut ärztlicher
  Anordnung » plutôt que « Laut Anordnung » seul : c'est la formule demandée par la mission.

#### ch08-23f6f9 — APPLIQUÉ — Phrases du service · soins_rm_36_3
- fichier : pflege/sources/dialogues/d36-uebergabe-altenheim.json (`redemittel.3`, la phrase du service soins_rm_36_3)
- avant (de) : Wenn die Finger kalt werden, ruf bitte den ärztlichen Bereitschaftsdienst an.
- après (de) : Wenn die Finger kalt, blass oder taub werden, ruf bitte sofort die 112. (`dit` ajouté : « … die eins eins zwei. »)
- après (fr) : Si les doigts deviennent froids, pâles ou engourdis, appelle tout de suite le 112, s'il te plaît.
- fait retenu : des doigts froids, pâles ou engourdis après un traumatisme du poignet signent un trouble de la
  circulation : urgence, le 112 et non le 116 117.
- écarté : « plötzlich … oder blau … » (ChatGPT) : plus long, pas commun aux trois. `relire_note` mise à jour.

#### ch08-4d6433 — APPLIQUÉ — Écrits · soins_ecrit_pflegebericht_01
- fichier : pflege/sources/ecrit/e09-pflegebericht-lehmann.json (`fiche.rubriques.1.valeur`, `points.1`, `modele`,
  `relire_notes`)
- avant (de) : fiche « VW re. Vorfuß: Wunde reizlos, kleiner als gestern; Pat. gut mitgemacht » ; point « 9 Uhr: Verbandswechsel, Wunde reizlos und kleiner, Patientin hat gut mitgemacht » ; modèle « Die Wunde ist reizlos und kleiner als gestern. »
- après (de) : fiche « VW re. Vorfuß: Wunde reizlos, Größe s. Wunddoku; Pat. gut mitgemacht » ; point « 9 Uhr: Verbandswechsel, Wunde reizlos, Größe siehe Wunddokumentation, Patientin hat gut mitgemacht » ; modèle « Die Wunde ist reizlos. Die Größe steht in der Wunddokumentation. »
- après (fr) : point « 9 h : pansement, plaie calme, taille : voir la documentation de la plaie, la patiente a bien collaboré » ; modèle « La plaie est calme. Sa taille est notée dans la documentation de la plaie. »
- fait retenu : « plus petite » d'un jour à l'autre est une impression ; la taille d'une plaie se note en mesures
  dans la Wunddokumentation.
- écarté : toute mesure chiffrée et les unités d'insuline (le cas ne les donne pas ; les trois disent seulement
  qu'elles figurent sur la courbe) ; la ligne de Gemini (« BZ 180 morgens, 140 mittags nach Schema … ») : style
  télégraphique, alors que la consigne demande des phrases complètes, et elle dit l'insuline « à midi », ce que le
  cas ne dit pas. Les valeurs (180 à 7 h, 140 à midi, ¾, deux verres) et les heures sont inchangées ; aucune unité
  ajoutée ni retirée, `modele.couvre` reprend toujours les cinq points.

---

#### ch08-7e466d — APPLIQUÉ — Scènes · soins-uebergabe · B2
- fichier : visuel/prototype/soins-uebergabe.points.json (question B2) et ses 9 traductions
- avant (de) : Das Kissen, auf dem der Fuß liegt, soll so bleiben.
- après (de) : Das Kissen, auf dem der Fuß liegt, soll nach Anordnung so bleiben.
- après (fr) : Le coussin sur lequel repose le pied doit rester ainsi, selon la prescription. Note : « La position du pied suit la prescription ».
- fait retenu : pour un pied diabétique, la surélévation n'est pas une règle (décharge d'abord, contre-indiquée en cas d'artériopathie) ; ChatGPT et Gemini donnent la même phrase.

### Le téléphone (ch. 10)

#### ch10-a8cd74 — APPLIQUÉ — Dialogues · Den Arzt anrufen (SBAR) · B2
- fichier : pflege/sources/dialogues/d07-sbar.json (`noeuds.wiederholen.choix.1`)
- avant (de) : Also: zwei Liter Sauerstoff über die Nasenbrille und den Oberkörper hoch. Ich dokumentiere die Anordnung. Bis gleich.
- après (de) : Also: zwei Liter Sauerstoff über die Nasenbrille und den Oberkörper hoch. Danach kontrolliere ich die Sättigung noch einmal. Ich dokumentiere die Anordnung. Bis gleich.
- après (fr) : Donc : deux litres d'oxygène aux lunettes et le buste relevé. Ensuite, je recontrôle la saturation. Je note la prescription. À tout de suite.
- fait retenu : après la mise sous oxygène, la soignante recontrôle la saturation (dit par les trois avis). Le reste du dialogue (valeurs du cas, rubriques SBAR, prescription répétée, notée, signée ensuite) est confirmé tel quel.
- écarté : la cible de saturation (92-96 %, plus basse si risque d'hypercapnie) : valeur que le cas ne contient pas, et « à vérifier dans le standard de la maison » ; « mit Uhrzeit und Ihrem Namen » (ChatGPT) : pas commun aux trois pour ce dialogue, et déjà porté par d50 ; la phrase de Gemini (« das könnte auf ein pulmonales Problem hinweisen ») : traitée au point suivant, en plus simple ; « la prescription téléphonique ne se reçoit que par une Pflegefachkraft » : nuance d'organisation, aucune phrase du dialogue ne dit le contraire (Yusuf se présente comme « Pflegekraft », terme générique) : voir « Doutes ».

#### ch10-602273 — APPLIQUÉ — Dialogues · Den Arzt anrufen (SBAR) · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d07-sbar.json (`noeuds.einschaetzung.choix.0`)
- avant (de) : Ich mache mir Sorgen. Sein Zustand hat sich in der letzten Stunde deutlich verschlechtert. Ich habe Angst, dass es etwas mit der Lunge ist.
- après (de) : Ich mache mir Sorgen. Sein Zustand hat sich in der letzten Stunde deutlich verschlechtert. Ich vermute, dass es etwas mit der Lunge ist.
- après (fr) : Je suis inquiet. Son état s'est nettement aggravé depuis une heure. Je soupçonne quelque chose aux poumons.
- fait retenu : face au médecin, un soupçon se dit comme un soupçon (« ich vermute »), pas comme une peur, et jamais comme un diagnostic.
- écarté : « Ich befürchte, dass eine Ursache in der Lunge liegen könnte » (ChatGPT) : plus long, même fait.

#### ch10-be1a64 — APPLIQUÉ — Dialogues · Am Telefon: Labor und Apotheke · B2 · aksoy
- fichier : pflege/sources/dialogues/d19-telefon.json (`noeuds.wert.choix.0.puis.0` et `noeuds.wert.choix.1.puis.0`, la même réplique)
- avant (de) : Richtig. {aksoy}, Zentrallabor. Die Probe ist nicht hämolysiert, der Wert ist also echt.
- après (de) : Richtig. {aksoy}, Zentrallabor. Die Probe ist nicht hämolysiert, an einer Hämolyse liegt der hohe Wert also nicht.
- après (fr) : C'est ça. {aksoy}, laboratoire central. L'échantillon n'est pas hémolysé, la valeur élevée ne vient donc pas d'une hémolyse.
- fait retenu : l'absence d'hémolyse écarte cette cause-là de fausse hyperkaliémie, pas les autres ; on ne conclut pas « la valeur est vraie ». Texte identique dans les trois avis.
- écarté : la liste des autres causes (garrot prolongé, transport tardif, bras perfusé) : hors du dialogue.

#### ch10-924cb2 — APPLIQUÉ — Dialogues · Angehörige am Telefon: die Schweigepflicht · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d23-schweigepflicht.json (`noeuds.anruf.choix.0`)
- avant (de) : Guten Abend, {lehmann_tochter}. Hier ist {elif} von der {station}. Bevor ich Ihnen etwas sage: …
- après (de) : Guten Abend, {lehmann_tochter}. Hier ist {elif} von der Pflege, {station}. Bevor ich Ihnen etwas sage: Können Sie mir bitte das Kennwort nennen, das bei der Aufnahme vereinbart wurde? (`dit` mis à jour avec `{station:dit}`)
- après (fr) : Bonsoir, {lehmann_tochter:voc}. Ici {elif}, de l'équipe soignante, {station}. Avant de vous dire quoi que ce soit : pouvez-vous me donner le mot de passe convenu à l'admission, s'il vous plaît ?
- fait retenu : avec une proche, on dit sa fonction en plus de son prénom et du service ; le mot de passe reste la méthode du cas (selon la maison). Texte identique dans les trois avis.
- écarté : rien. Le second choix du nœud (« Hier spricht {elif} von der {station} ») n'est pas visé par le point : laissé (voir « Doutes »).

#### ch10-546726 — APPLIQUÉ — Dialogues · Angehörige am Telefon: die Schweigepflicht · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d23-schweigepflicht.json (`noeuds.nachbar.choix.0`)
- avant (de) : … Aber über andere Patienten darf ich Ihnen leider nichts sagen. Das gilt für alle, auch für Ihre Mutter.
- après (de) : Das ist nett, dass Sie fragen. Aber über andere Patienten darf ich Ihnen leider nichts sagen. Genauso geben wir anderen auch keine Auskunft über Ihre Mutter.
- après (fr) : C'est gentil de demander. Mais je ne peux malheureusement rien vous dire sur les autres patients. De la même façon, nous ne donnons aucune information sur votre mère à d'autres personnes.
- fait retenu : la phrase d'origine pouvait se comprendre « je ne vous dis rien non plus sur votre mère » ; le secret vaut dans les deux sens (on ne parle pas de sa mère aux autres).
- écarté : « geben wir auch **niemandem** Auskunft über Ihre Mutter » (premier relecteur, Gemini) : faux à la lettre, puisque Elif vient d'en donner à la fille (ChatGPT le relève) ; j'ai gardé leur tournure avec « anderen » au lieu de « niemandem ». « Genauso schützen wir auch die persönlichen Informationen Ihrer Mutter » (ChatGPT) : plus abstrait.

#### ch10-e1bef2 — APPLIQUÉ (une aide, en français ; l'allemand n'est pas en cause) — Dialogues · Die Tochter ruft an · B1
- fichier : pflege/sources/dialogues/d48-tochter-ruft-an.json (`noeuds.pruefen.choix.2.aide`)
- avant (fr) : … Regarde d'abord dans le dossier qui peut recevoir des informations, puis pose une question de contrôle. Et « wie immer » est un jugement, pas une information.
- après (fr) : <b>Au téléphone, aucune nouvelle avant de savoir qui appelle.</b> N'importe qui peut se dire « la fille ». Regarde d'abord dans le dossier qui peut recevoir des informations, puis vérifie qui appelle comme le prévoit ta maison : une question de contrôle, un mot de passe ou un rappel au numéro du dossier. Et « wie immer » est un jugement, pas une information.
- après (de) : inchangé (« Danke, Sie stehen bei uns in der Akte. Zur Sicherheit noch eine Frage: Können Sie mir das Geburtsdatum Ihres Vaters sagen? »).
- fait retenu : vérifier d'abord au dossier que l'appelante est autorisée (essentiel, confirmé), puis l'identifier selon la procédure de la maison ; la date de naissance seule est un contrôle faible. L'aide ne présente plus la question de contrôle comme la seule règle ; même liste que l'aide de d23.
- écarté : remplacer la date de naissance par un mot de passe dans le dialogue : aucun avis ne le demande (« démarche conforme à la pratique en Altenheim »), et ce serait réécrire le cas (la date 12.03.1939 vient de l'écrit e05) ; la phrase de Gemini (« Ich habe den Anruf dokumentiert … ») : un seul avis ; les droits du Betreuer : hors du cas.

#### ch10-698397 — APPLIQUÉ (l'intro, en français ; l'allemand n'est pas en cause) — Dialogues · Sich krankmelden · B1
- fichier : pflege/sources/dialogues/d49-krankmeldung.json (`intro`)
- avant (fr) : … Elle appelle {hoffmann} avant le début du service, comme le veut la règle du {station}. …
- après (fr) : … Le thermomètre affiche 39,1. Elle appelle {hoffmann} sans attendre, avant le début du service : une maladie se signale dès qu'on sait qu'on ne pourra pas travailler. Tu joues {elif} : …
- après (de) : inchangé.
- fait retenu : la maladie se signale « unverzüglich », dès qu'on le sait, et pas seulement avant le début du poste (§ 5 EntgFG, dit par les trois avis). Le reste est confirmé : arrêt exigible dès le premier jour si l'employeur le demande (ce que dit la cadre), eAU transmise par le cabinet à la caisse et consultée par l'employeur, la salariée prévient elle-même (l'aide dit « tu préviens, et tu dis la durée »).
- écarté : changer l'heure de l'appel (5 h 30 pour 6 h) : c'est le cas, et le dialogue reconnaît déjà le court délai (« so früh », « so kurzfristig Ersatz suchen ») ; la phrase-règle de ChatGPT (« Ich muss meinen Arbeitgeber unverzüglich informieren … ») : une règle récitée, pas une réplique d'appel ; la phrase de Gemini : équivalente au redemittel existant ; les exceptions à l'eAU (assurance privée, médecin sans convention, étranger) et l'exemplaire papier gardé par la salariée : justes, hors du cas. La `relire_notes` (« Prévenir l'employeur avant le début du service ») reste vraie : laissée.

#### ch10-1a717e — APPLIQUÉ — Dialogues · Eine telefonische Anordnung · B2 · kraemer
- fichier : pflege/sources/dialogues/d50-telefonische-anordnung.json (`noeuds.bisher.choix.0.puis.0`, `noeuds.bisher.choix.1.puis.0` ; par cohérence les deux relectures `noeuds.zuruecklesen.choix.0` et `.choix.1`)
- avant (de) : Gut. Dann nehmen Sie bitte zwei Paar Blutkulturen ab, aus zwei verschiedenen Venen. Danach bekommt er ein Gramm Paracetamol als Kurzinfusion. …
- après (de) : Gut. Dann nehmen Sie bitte zwei Paar Blutkulturen ab, aus zwei verschiedenen Punktionsstellen. Danach bekommt er ein Gramm Paracetamol als Kurzinfusion. Ich komme innerhalb der nächsten Stunde und sehe ihn mir an.
- après (fr) : Bien. Alors prélevez deux paires d'hémocultures, à deux points de ponction différents. Ensuite, il reçoit un gramme de paracétamol en perfusion courte. Je viens dans l'heure qui suit et je l'examine.
- aussi : `zuruecklesen.choix.0` « … abgenommen, aus zwei verschiedenen Punktionsstellen. … » (fr : « à deux points de ponction différents ») ; `zuruecklesen.choix.1` « zwei Paar Blutkulturen aus zwei Punktionsstellen » (fr : « à deux points de ponction »).
- fait retenu : deux paires d'hémocultures se prélèvent à deux points de ponction distincts, on ne dit pas « deux veines » (les trois avis). La `relire_notes` disait déjà « deux ponctions veineuses différentes ».
- écarté : l'ordre des mots de ChatGPT (« an zwei verschiedenen Punktionsstellen ab ») : même fait ; qui prélève (délégation) : note, pas de phrase.

#### ch10-4e3c8e — APPLIQUÉ — Dialogues · Eine telefonische Anordnung · B2 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d50-telefonische-anordnung.json (`noeuds.doku.choix.0`)
- avant (de) : Fünfzehn Minuten; anrufen bei über 39,5 Grad, Blutdruck unter 100 oder Verwirrtheit. Ich trage das als telefonische Anordnung ein, mit Uhrzeit und Ihrem Namen. Bitte zeichnen Sie sie ab, wenn Sie auf Station sind.
- après (de) : Ich wiederhole: zwei Paar Blutkulturen aus zwei verschiedenen Punktionsstellen, danach ein Gramm Paracetamol als Kurzinfusion über fünfzehn Minuten; anrufen bei über 39,5 Grad, Blutdruck unter 100 oder Verwirrtheit. Ich trage das als telefonische Anordnung ein, mit Uhrzeit und Ihrem Namen. Bitte zeichnen Sie sie ab, wenn Sie auf Station sind. (`dit` mis à jour : « neununddreißig Komma fünf », « hundert »)
- après (fr) : Je répète : deux paires d'hémocultures à deux points de ponction différents, ensuite un gramme de paracétamol en perfusion courte sur quinze minutes ; rappeler au-dessus de 39,5 °C, tension sous 100 ou confusion. Je l'inscris comme prescription téléphonique, avec l'heure et votre nom. Merci de la signer quand vous serez dans le service.
- fait retenu : la prescription par téléphone se répète en entier à voix haute (une fois complétée par la durée et les seuils), se note tout de suite avec l'heure et le nom du médecin, puis le médecin la signe. Texte du premier relecteur, repris mot pour mot par Gemini ; aucune dose, durée ni valeur qui ne soit déjà dans le dialogue.
- écarté : la version de ChatGPT (« der systolische Blutdruck unter 100 fällt … », quatre phrases) : plus longue, même contenu ; la mention « v. u. g. » (vorgelesen und genehmigt), citée par les trois comme usage du dossier mais dans aucun texte proposé : non ajoutée (elle pourrait aller dans une aide si la soignante la confirme) ; « le délai de signature dépend de l'établissement » : la phrase dit « wenn Sie auf Station sind », cohérent.
- non touché : le second choix du nœud (« Verstanden: Laufzeit fünfzehn Minuten … »), le redemittel « Ich trage das als telefonische Anordnung ein. … » et l'aide : ils ne sont pas en cause.

---

#### ch10-7b15aa — APPLIQUÉ (traductions et note ; l'allemand ne change pas) — Mots · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `N("B2", "die Schweigepflichtentbindung")`
- avant / après (de) : Ohne Schweigepflichtentbindung geben wir der Tochter am Telefon keine Auskunft. (inchangé)
- après (fr) : le mot : « la levée du secret professionnel (accord du patient, le plus souvent écrit) » au lieu
  d'« (autorisation écrite du patient) », dans les 10 langues ; l'exemple : « Sans levée du secret professionnel, … »
  (« écrite » retiré en fr, en, tr, fa, ar, où la traduction ajoutait un mot que l'allemand n'a pas).
- fait retenu : l'accord n'a pas à être écrit selon la loi ; l'écrit sert de preuve et il est d'usage.
- écarté : le sort du Betreuer et du mandataire : le premier relecteur dit « informé sans cette levée », ChatGPT « pas
  automatiquement, selon ses pouvoirs » : pas d'accord, la note le signale pour la soignante. Les deux phrases
  allemandes proposées (ChatGPT sans le mot, Gemini avec « oder entsprechende Vollmacht »).

#### ch10-ecec8c — APPLIQUÉ — Mots · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `N("B2", "der Hintergrunddienst")` (exemple, 10 langues, note)
- avant (de) : Wenn der diensthabende Arzt Hilfe braucht, ruft er den Hintergrunddienst an; der kommt dann von zu Hause in die Klinik.
- après (de) : Wenn der diensthabende Arzt Hilfe braucht, ruft er den Hintergrunddienst an; der berät ihn am Telefon und kommt bei Bedarf von zu Hause in die Klinik.
- après (fr) : Quand le médecin de garde a besoin d'aide, il appelle le senior d'astreinte, qui le conseille au téléphone et vient de chez lui à l'hôpital si nécessaire.
- fait retenu : il conseille d'abord par téléphone et ne se déplace que si nécessaire (même texte dans les trois avis).
- écarté : rien. Les équivalents tr, fa, pt, pl, es du terme restent à confirmer par des natifs du métier (les trois
  avis le disent ; la note le disait déjà).

#### ch10-75fee8 — APPLIQUÉ — Mots · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `N("B2", "der kritische Wert")` (exemple, 10 langues, note)
- avant (de) : Bei einem kritischen Wert ruft das Labor sofort auf der Station an; ich wiederhole den Wert laut und informiere die Ärztin.
- après (de) : Bei einem kritischen Wert ruft das Labor sofort auf der Station an; ich wiederhole den Wert laut, notiere Uhrzeit und Namen und informiere sofort die Ärztin.
- après (fr) : En cas de valeur critique, le labo appelle aussitôt le service ; je répète la valeur à voix haute, je note l'heure et le nom, et je préviens tout de suite le médecin.
- fait retenu : on note l'heure et le nom, on prévient le médecin tout de suite ; synonymes : « Alarmwert »,
  « Panikwert », alors que « Notfallwert » peut désigner une analyse demandée en urgence (note corrigée : elle donnait
  « Notfallwert » comme synonyme).
- écarté : « Extremwert » (premier relecteur seul) ; la phrase de Gemini, qui retire l'appel du laboratoire.

#### ch10-3aea7a — APPLIQUÉ — Mots · soins_dokumentation_b2
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `N("B2", "die telefonische Anordnung")` (exemple, 10 langues, note)
- avant (de) : Eine telefonische Anordnung dokumentiere ich sofort; die Ärztin zeichnet sie bei der nächsten Visite gegen.
- après (de) : Eine telefonische Anordnung lese ich der Ärztin noch einmal vor und dokumentiere sie sofort; die Ärztin zeichnet sie so bald wie möglich ab.
- après (fr) : Une prescription téléphonique, je la relis à voix haute au médecin et je la note tout de suite ; le médecin la signe dès que possible.
- fait retenu : la relecture à voix haute manquait ; la signature vient dès que possible, selon le délai de la maison
  (même texte dans les trois avis) ; « abzeichnen » et « gegenzeichnen » se disent tous deux (note).
- écarté : « souvent sous 24 heures » (premier relecteur seul) : un délai que la source ne donne pas.

---

#### ch10-b8bee9 — APPLIQUÉ — Phrases du service · soins_rm_07_2
- fichier : pflege/sources/dialogues/d07-sbar.json (`redemittel.2`)
- avant (de) : Die Sauerstoffsättigung liegt bei 88 Prozent.
- après (de) : Die Sauerstoffsättigung liegt bei 88 Prozent bei Raumluft. (`dit` : … achtundachtzig Prozent bei Raumluft.)
- après (fr) : La saturation en oxygène est à 88 % à l'air ambiant.
- fait retenu : une saturation se transmet avec sa condition (air ambiant ou débit d'oxygène) ; texte identique dans les trois avis.
- écarté : rien. Les deux choix du nœud `situation` portaient déjà la condition (« ohne Sauerstoff », « bei Raumluft ») : non touchés.

#### ch10-22e9c2 — APPLIQUÉ (une aide, en français ; l'allemand n'est pas en cause) — Scènes · soins-telefon · SIT
- fichier : pflege/sources/dialogues/d07-sbar.json (noeuds.empfehlung.choix.2.aide), d'où la scène soins-telefon tire sa situation
- après (fr) : … Et ne donne pas de médicament sans prescription : demande ce que tu dois faire en attendant. Les gestes de soins, eux, n'attendent pas : relever le buste, rester près du patient, reprendre les constantes.
- fait retenu : les mesures de soins sans prescription se font tout de suite ; la bonne réponse ne change pas.
- écarté : « Soll ich ihm bis dahin Sauerstoff geben? » (ChatGPT) : l'oxygène n'est pas dans cette réplique du cas.

## Confirmé sans changement : 13 points

### L'admission (ch. 1)

#### ch01-7d83c5 — SANS CHANGEMENT — Dialogues · Das Biografiegespräch · B2
- fichier : pflege/sources/dialogues/d43-biografiegespraech.json (non modifié)
- fait commun : avec une démence, la personne consent elle-même autant que possible, sinon la personne munie d'une procuration ou le représentant légal, pas n'importe quel proche ; la biographie est lue aussi par l'accompagnement et les thérapeutes.
- pourquoi rien n'est changé : le premier relecteur et ChatGPT ne proposent aucun texte ; le dialogue dit déjà « die Mitarbeitenden, die an seiner Pflege und Betreuung beteiligt sind ». Dire qui consent demanderait une donnée que le cas ne contient pas (la fille a-t-elle une Vorsorgevollmacht ?).
- écarté : la phrase de Gemini (« Ihre Angaben helfen nicht nur der Pflege, sondern auch der Betreuung und den Therapeuten … ») : un seul avis, une réplique de plus.
- pour la soignante : voir Doutes (procuration de la fille).

#### ch01-fc393a — SANS CHANGEMENT — Paires patient / service · soins_sprache_b1
- fichier : pflege/sources/vocabulaire/t12_sprache.py — `P("B1", "nichts essen und trinken dürfen", "nüchtern bleiben")`
- avant / après (de) : Der Patient bleibt ab Mitternacht nüchtern, die Operation ist für morgen früh geplant.
- fait retenu : la paire et la phrase sont justes (premier relecteur, ChatGPT) ; les délais différents pour manger et
  pour boire, fixés par l'anesthésie, sont déjà dits dans la note de l'entrée.
- écarté : la phrase de Gemini (« nach Vorgabe der Anästhesie ») : seul avis à toucher au texte.

#### ch01-16abe3 — SANS CHANGEMENT — Thème illustré · soins-theme-aufnahme
- fichier : pflege/outils/themes_soins/aufnahme.py (la fiche de Frau Weber)
- fait retenu : la simplification « Medikamente: gegen Bluthochdruck » est acceptable ; la vérification demandée est faite : l'hypertension figure dans les diagnostics de l'écrit e03.
- écarté : « 1 Tablette …, morgens » (premier relecteur, ChatGPT) et « Blutdruckmittel nach Plan, morgens » (Gemini) : e03 ne donne ni dose ni horaire, ce serait les inventer.

### La douleur (ch. 7)

#### ch07-155abb — SANS CHANGEMENT — Dialogues · Angst vor der Untersuchung · B1
- fichier : pflege/sources/dialogues/d15-angst-vor-untersuchung.json (tout le dialogue)
- fait retenu : l'information sur les risques du produit de contraste et le résultat reviennent à la médecin ; la
  soignante demande et transmet ; le jeûne dépend du service. Le dialogue le fait déjà : Elif pose la question de la
  réaction antérieure et transmet (« das sage ich dem Team im CT auch », « das gebe ich weiter »), ne parle pas du
  jeûne, renvoie le résultat à la médecin. Le seul texte en cause (« heute noch ») est corrigé au point suivant.
- écarté : la phrase de Gemini (« Haben Sie schon einmal auf ein Kontrastmittel oder Medikamente reagiert? Das gebe
  ich direkt weiter. ») : le dialogue a déjà cette question en deux variantes.

#### ch07-fdcc00 — SANS CHANGEMENT — Dialogues · Schmerzen, die keiner ausspricht · B2
- fichier : pflege/sources/dialogues/d29-schmerz-demenz.json (tout le dialogue)
- fait retenu : la description de la BESD est juste (cinq rubriques, 0 à 2, total 10, au repos et en mouvement) ; le
  seuil d'interprétation n'est pas universel (notice de l'outil, standard de la maison) ; 6 sur 10 en mouvement
  justifie une évaluation et un avis médical. Le dialogue ne donne aucun seuil (« sechs von zehn Punkten. Das ist
  deutlich. »), appelle le cabinet le jour même et réévalue une heure après : rien à changer. La `relire_notes`
  demande déjà de valider l'interprétation du score.
- écarté : la phrase de Gemini sur la réévaluation après une heure : le dialogue l'a déjà (« In einer Stunde machen
  wir die BESD noch einmal »).

### La relève (ch. 8)

#### ch08-6d83a4 — SANS CHANGEMENT — Dialogues · Die Übergabe am Abend · B1 · soignant(e) · réponse
- fichier : pflege/sources/dialogues/d27-abenduebergabe.json (`noeuds.kalium.choix.0`)
- avant (de) : Heute Mittag war ihr Kalium zu hoch, 6,2. Die Ärztin hat ein Medikament angeordnet, und um 20 Uhr wurde noch einmal Blut abgenommen.
- après (de) : inchangé
- après (fr) : inchangé
- fait retenu : les trois jugent « ein Medikament » acceptable au B1 ; aucun texte commun n'est proposé.
- écarté : nommer la mesure prescrite (perfusion, résine, diurétique) : le cas ne la donne pas, et ChatGPT écrit qu'il
  ne faut pas l'inventer ; « eine Therapie » (Gemini seul) n'est pas plus précis que « ein Medikament ».

#### ch08-b5a610 — SANS CHANGEMENT — Dialogues · Nachfragen bei der Übergabe · B2
- fichier : pflege/sources/dialogues/d37-uebergabe-nachfragen.json (tout le dialogue)
- avant (de) : (tout le dialogue)
- après (de) : inchangé
- après (fr) : inchangé
- fait retenu : les trois jugent le cas cohérent (résultat annoncé par la médecin seule, premier pansement au 2e jour
  selon le protocole, refus documenté, rien « bei Bedarf » le mercredi midi).
- écarté : avancer le début de l'antibiotique au mercredi 11 (premier relecteur) : ChatGPT écrit qu'on ne peut pas
  l'affirmer sans la prescription, il n'y a donc pas de fait commun ; d37 ne parle d'ailleurs pas de l'antibiotique.
  La date (jeudi 12) n'est pas changée : voir Doutes et « À harmoniser ailleurs ». La phrase proposée par Gemini
  (« Die feste Schmerzmedikation wurde um 8 Uhr verabreicht, im Moment ist keine Bedarfsmedikation angesetzt ») redit
  ce que le dialogue dit déjà (`noeuds.kurve`).

### Le téléphone (ch. 10)

#### ch10-cdf848 — SANS CHANGEMENT — Thème illustré · soins-theme-telefon
- fichier : pflege/outils/themes_soins/telefon.py (les notes d'appel)
- fait retenu : données d'exemple plausibles ; la cohérence demandée est vérifiée : « fünf Insulinpens, Lieferung vor vierzehn Uhr » est mot pour mot dans d19 ; les numéros 412 et 287 n'apparaissent dans aucun dialogue.

#### ch10-213c88 — SANS CHANGEMENT — Dialogues · Am Telefon: Labor und Apotheke · B2
- fichier : pflege/sources/dialogues/d19-telefon.json (tout le dialogue)
- fait retenu : les trois avis confirment le cas (potassium 6,2 mmol/l transmis tout de suite, relu, nom noté ; insuline lispro 100 E/ml en stylo ; un comprimé retard ne s'écrase pas, la question à la pharmacie est la bonne conduite). Le seuil d'appel « dépend du laboratoire » : le dialogue ne donne aucun seuil, seulement la valeur du cas ; la `relire_notes` dit déjà « seuil d'appel du laboratoire ». La seule phrase en cause (« der Wert ist also echt ») est le point suivant.
- écarté : la question reformulée par Gemini (« Darf man dieses retardierte Präparat mörsern oder teilen, oder brauchen wir eine andere Darreichungsform? ») : proposée par un seul avis ; la question du dialogue nomme déjà le médicament et la forme.

#### ch10-65cc63 — SANS CHANGEMENT — Dialogues · Angehörige am Telefon: die Schweigepflicht · B2
- fichier : pflege/sources/dialogues/d23-schweigepflicht.json (tout le dialogue)
- fait retenu : aucune information, même de soins, sans l'accord du patient et sans identification selon la règle de la maison. Le dialogue fait exactement cela : la levée du secret est au dossier (intro), Elif vérifie le mot de passe avant tout, renvoie les résultats à la médecin et ne dit rien du voisin. L'aide dit déjà « le mot de passe convenu, ou on rappelle au numéro du dossier ».
- écarté : la phrase de Gemini (« … prüfe ich die Schweigepflichtentbindung beziehungsweise die Vollmacht … ») : un seul avis, et l'intro pose déjà la levée du secret ; les droits du Betreuer / mandataire et « l'accord n'a pas à être écrit mais documenté » : justes, mais hors du cas. La `relire_notes` parle d'« assistante de soins » et de ce qu'elle « peut dire » : note pour la soignante, laissée (règle 6).

#### ch10-a11136 — SANS CHANGEMENT — Dialogues · Eine Nachricht am Telefon · A2
- fichier : pflege/sources/dialogues/d46-telefonnotiz.json (tout le dialogue)
- fait retenu : prendre un message sans rien dire de la patiente est correct, ne pas promettre l'heure du rappel aussi. La précision commune (confirmer à un inconnu qu'une personne est hospitalisée est déjà couvert par le secret) ne vise que la `relire_notes` : dans le dialogue, c'est l'appelante qui nomme sa mère et la chambre, Elif ne confirme rien et ne donne aucune nouvelle.
- écarté : la phrase de Gemini (« Ich nehme gern eine Nachricht für die Station oder die Ärztin auf … ») : un seul avis, et « Kann ich ihr etwas ausrichten? » dit la même chose au niveau A2.

#### ch10-957bf9 — SANS CHANGEMENT (à ce niveau ; voir les trois points suivants) — Dialogues · Eine telefonische Anordnung · B2
- fichier : pflege/sources/dialogues/d50-telefonische-anordnung.json (tout le dialogue)
- fait retenu : cas cohérent pour les trois avis (hémocultures avant l'antipyrétique, deux paires, paracétamol 1 g en perfusion courte sur 15 minutes, seuils de rappel, prescription relue, notée avec l'heure et le nom, signée ensuite). Les corrections de texte sont portées par 1a717e et 4e3c8e.
- écarté : « le médecin vient dans l'heure » jugé limite haute (premier relecteur, ChatGPT ; Gemini ne le dit pas) : pas commun aux trois, et changer ce délai serait inventer une donnée du cas (voir « Doutes ») ; qui prélève les hémocultures (délégation selon la maison) et « reçue seulement par une Pflegefachkraft » : déjà dans la `relire_notes`, aucune phrase à changer ; la phrase de Gemini est reprise dans 4e3c8e.

#### ch10-264c08 — SANS CHANGEMENT — Mots · soins_dokumentation_b1
- fichier : pflege/sources/vocabulaire/t09_dokumentation.py — `X("B1", "Mit wem spreche ich, bitte?")`
- avant / après (de) : Bevor ich Ihnen etwas über einen Patienten sage: Mit wem spreche ich, bitte?
- fait retenu : la question est correcte et usuelle ; qu'un nom donné au téléphone ne prouve rien, et qu'il faut la
  règle de la maison (mot de passe, rappel au numéro connu), la note de l'entrée le dit déjà.
- écarté : la phrase de Gemini (« Wie ist Ihr Name, und wie stehen Sie zu dem Patienten? ») : elle retire l'expression
  de la carte.

## Ce qui a été harmonisé en plus

- **d32** (le poignet le lendemain) aligné sur d36 : le 112 pour les doigts froids, pâles ou engourdis (réplique et note de relecture, 10 langues).
- **Le thème illustré de la relève** : la radio de 11 h retirée de la feuille de Frau Weber (voir ch08-d6d7ec).
- **Les scènes** : leurs situations parlées sont reprises mot pour mot des dialogues (`situations_scenes.py`) ; les scènes de l'admission, du poste de soins, du téléphone, de la relève et du lever suivent donc les dialogues corrigés. La reconstruction a aussi ajouté aux 12 scènes de soins les traductions espagnoles des mots, présentes dans le vocabulaire depuis le 16 nov. et que les scènes n'avaient pas encore reprises.
- **Les dérivés** refaits : `pflege/datos/` (dialogues, écrit, cartes-phrases, vocabulaire, chapitres), les quatre thèmes illustrés, les 14 feuilles de relecture.

## Ce qui reste (non touché)

- **« Verbandsschuh » ou « Vorfußentlastungsschuh »** pour Frau Lehmann : question à la soignante (ch01-ec373b). La carte « der Wundrand » (« Der Wundrand ist leicht gerötet ») garde aussi l'ancien mot, alors que d45 dit maintenant « Wundumgebung ».
- **« Ab Mitternacht » comme règle générale** : `vocabulaire/t06_ernaehrung.py`, `t09_dokumentation.py`, `t12_sprache.py` (2 phrases), `redemittel/releve.json`, fiches g17 et g18. Hors des 98 points.
- **d17 (la visite)**, hors des quatre chapitres : sonde urinaire retirée au 3e jour (jugée longue), antibiotique commencé le jeudi 12 pour un diagnostic du mercredi 11 ; d35, d38 et d39 citent ces dates.
- **d06** : pas de date, mais les faits de Frau Lehmann sont ceux de l'écrit e09, daté du 13.11. ; s'il est du vendredi 13, Herr Brandt y a 7 sur 10 et refuse la mobilisation alors qu'il s'est levé le jeudi 12 (d27). Et « schon etwas kleiner » reste à l'oral dans d06 alors qu'e09 ne le dit plus.
- **La note de la carte « vorlesen »** (`t09_dokumentation.py`) demande encore « vorlesen, zurücklesen, wiederholen ? » ; les trois avis répondent « Ich wiederhole ».
- **Les voix** : aucune voix n'est en jeu (décision du 19 nov. : pas de voix des soins avant Azure). Les phrases changées de d01, d02, d06 et d07 et 18 exemples de vocabulaire n'ont plus de fichier son à leur nom : la voix du téléphone les dit. `pflege/sources/voix-accent.json` cite encore l'ancienne phrase de d07 (phrase d'essai de voix, pas montrée).
- **L'anglais** : les phrases réécrites sont en américain ; « paraesthesia », « ward », « haemoglobin », « oedema » restent britanniques ailleurs dans le vocabulaire.
- **Les traductions** des phrases changées sont faites par retouche des traductions existantes, par des modèles : à faire relire par des natifs avec le reste (termes nouveaux : « point de ponction », « von der Pflege », « chaussure »).
- **Les brouillons de l'interface espagnole** (`interface-es/sources/` et `lots/`, scènes 07 et 08) gardent l'ancienne clé de la question du coussin ; le fichier servi (`visuel/prototype/traductions/soins-uebergabe.es.json`) est à jour.

## La méthode

Les fichiers envoyés aux deux modèles et leurs réponses sont hors du dépôt. Chaque identifiant des réponses a été vérifié contre les fichiers : aucun inventé ; Gemini a seulement oublié ch07-510321. L'application a été faite par chapitre (dialogues, cartes-phrases, écrits), puis pour le vocabulaire, puis pour les scènes et les thèmes illustrés ; chaque changement de l'allemand a été relu ensuite. Contrôles : `tests/pflege_dialogues.py` (0 erreur), `tests/pflege_vocabulaire.py`, `tests/pflege_examen.py`, `tests/pflege.py`, `tests/themes_soins.py`, `node tests/pflege_certificat.js`, `pflege/outils/construire_scenes.py --toutes`.
