# Collisions dans la langue cible — le controle mecanique

Produit par `python tests/relecture_langue.py --langue es --collisions`. **Aucune correction appliquee.**

Chaque ligne est un mot turc qui repond a PLUSIEURS mots allemands distincts de la meme categorie. La carte devient indecidable : quoi que l'apprenant reponde, il ne peut pas avoir raison.

Toutes ne sont pas des erreurs — deux quasi-synonymes allemands peuvent legitimement partager un mot turc si la langue n'en a pas deux. Mais chacune doit etre REGARDEE, et aucune relecture par lots ne peut les voir : le relecteur ne recoit qu'une centaine de cartes a la fois.


---

# Collisions acceptees, avec leur raison

Le turc n'a reellement qu'un mot la ou l'allemand en a deux : forcer une difference y produirait un contresens ou une tournure que personne ne dit. Chaque ligne porte sa justification, et vient de `collisions-acceptees.txt`.

- *adjectifs* — **chic, elegante** ← schick, chic
  - schick et chic sont le même mot allemand sous deux graphies ; l'espagnol n'a rien à distinguer
- *adjectifs* — **necesario** ← notwendig, nötig
  - notwendig et nötig sont synonymes ; « necesario » est le seul mot courant (« preciso » serait recherché)
- *adjectifs* — **nublado** ← wolkig, bewölkt
  - wolkig et bewölkt se disent tous deux « nublado » en Amérique latine ; « nuboso » est un mot de bulletin météo, rare à l'oral
- *noms* — **el abogado** ← der Anwalt, der Rechtsanwalt
  - Anwalt est la forme courte de Rechtsanwalt ; un seul métier, un seul mot
- *noms* — **el agente inmobiliario** ← der Makler, der Immobilienmakler
  - Makler est la forme courte de Immobilienmakler dans ce contexte (il fait visiter l'appartement)
- *noms* — **el apartamento compartido** ← die Wohngemeinschaft, die WG
  - WG est le sigle de Wohngemeinschaft ; même chose
- *noms* — **el apellido** ← der Nachname, der Familienname
  - Nachname et Familienname sont synonymes ; l'espagnol ne dit que « apellido »
- *noms* — **el ascensor, el elevador** ← der Aufzug, der Lift
  - Lift est le synonyme (Autriche, Suisse) de Aufzug ; répartir « ascensor » et « elevador » entre les deux serait arbitraire
- *noms* — **el estado civil** ← der Familienstand, der Personenstand
  - Familienstand et Personenstand désignent la même rubrique des formulaires ; « estado civil » est le seul terme
- *noms* — **el horno** ← der Ofen, der Backofen
  - Backofen est la forme précise de Ofen dans la cuisine ; « horno » dans les deux cas
- *noms* — **el lavavajillas** ← die Geschirrspülmaschine, die Spülmaschine
  - Spülmaschine est la forme courte de Geschirrspülmaschine
- *noms* — **el material** ← das Material, der Werkstoff
  - Werkstoff est le mot technique pour Material ; l'espagnol dit « material » dans les deux registres
- *noms* — **el mesero** ← der Kellner, der Ober
  - Ober est l'ancien mot pour Kellner (surtout pour l'appeler) ; « mesero » dans les deux cas
- *noms* — **el paraguas** ← der Schirm, der Regenschirm
  - Schirm est la forme courte de Regenschirm dans ce contexte (il pleut)
- *noms* — **el pollo** ← das Hähnchen, das Hühnchen
  - Hähnchen et Hühnchen sont deux variantes du même mot ; « pollo »
- *noms* — **el postre** ← der Nachtisch, das Dessert, die Nachspeise
  - Nachtisch, Dessert et Nachspeise sont trois synonymes ; l'espagnol ne dit que « postre »
- *noms* — **el promedio de notas** ← der Notendurchschnitt, der Notenschnitt
  - Notenschnitt est la forme courte de Notendurchschnitt
- *noms* — **el resultado** ← das Resultat, das Ergebnis
  - Resultat et Ergebnis sont synonymes ; « resultado »
- *noms* — **el retraso, la demora** ← die Verspätung, die Verzögerung
  - Verspätung et Verzögerung : « retraso » et « demora » sont interchangeables en espagnol, les attribuer chacun à un mot allemand serait arbitraire
- *noms* — **el sillón** ← der Sessel, das Fauteuil
  - Fauteuil est le synonyme (Autriche, Suisse) de Sessel ; « sillón »
- *noms* — **el sofá** ← das Sofa, die Couch
  - Couch et Sofa sont synonymes ; « sofá »
- *noms* — **el tranvía** ← die Straßenbahn, die Tram
  - Tram est la forme courte (sud, Suisse) de Straßenbahn ; « tranvía »
- *noms* — **la distancia** ← die Entfernung, die Distanz
  - Entfernung et Distanz sont synonymes ; « distancia » au propre comme au figuré
- *noms* — **la empresa** ← die Firma, das Unternehmen
  - Firma et Unternehmen sont synonymes dans l'usage courant ; « empresa »
- *noms* — **la entrevista de trabajo** ← das Bewerbungsgespräch, das Vorstellungsgespräch
  - Vorstellungsgespräch et Bewerbungsgespräch désignent le même entretien ; « entrevista de trabajo »
- *noms* — **la escalera** ← die Treppe, die Stiege
  - Stiege est le synonyme (Autriche, sud) de Treppe ; « escalera »
- *noms* — **la exportación** ← der Export, die Ausfuhr
  - Ausfuhr est le mot administratif pour Export ; « exportación » dans les deux registres
- *noms* — **la fecha de vencimiento, la fecha de caducidad** ← das Haltbarkeitsdatum, das Verfallsdatum
  - Haltbarkeitsdatum et Verfallsdatum : dans l'usage courant les deux se disent « fecha de vencimiento » ; « fecha de consumo preferente » est un terme d'étiquetage que presque personne n'emploie
- *noms* — **la fiesta** ← die Party, das Fest
  - Party et Fest : l'espagnol n'a que « fiesta » ; « festividad » est déjà la réponse de Feierlichkeit
- *noms* — **la guardería** ← die Kindertagesstätte, die Kita
  - Kita est l'abréviation de Kindertagesstätte
- *noms* — **la importación** ← der Import, die Einfuhr
  - Einfuhr est le mot administratif pour Import ; « importación » dans les deux registres
- *noms* — **la inmigración** ← die Einwanderung, die Zuwanderung
  - Zuwanderung est le synonyme administratif de Einwanderung ; « inmigración »
- *noms* — **la olla** ← der Topf, der Kochtopf
  - Kochtopf est la forme précise de Topf ; « olla »
- *noms* — **la peluquería** ← der Friseursalon, das Friseurgeschäft
  - Friseursalon et Friseurgeschäft sont le même commerce ; « peluquería »
- *noms* — **la realidad** ← die Realität, die Wirklichkeit
  - Realität et Wirklichkeit sont synonymes ; « realidad »
- *noms* — **la recepción** ← die Rezeption, der Empfang
  - Rezeption et Empfang désignent ici le même comptoir d'accueil ; « recepción »
- *noms* — **la rehabilitación** ← die Reha, die Rehabilitation
  - Reha est l'abréviation de Rehabilitation
- *noms* — **la relación** ← die Beziehung, das Verhältnis
  - Beziehung et Verhältnis (entre personnes) : « relación » dans les deux cas ; « trato » ou « vínculo » changeraient le sens
- *verbes* — **abrir** ← öffnen, aufmachen
  - öffnen et aufmachen : l'espagnol n'a que « abrir »
- *verbes* — **cerrar** ← schließen, zumachen
  - schließen et zumachen : l'espagnol n'a que « cerrar »
- *verbes* — **hacer** ← machen, tun
  - machen et tun : l'espagnol n'a que « hacer »
- *verbes* — **pagar** ← bezahlen, zahlen
  - bezahlen et zahlen : l'espagnol n'a que « pagar »

