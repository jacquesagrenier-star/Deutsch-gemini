# Devis des voix : l'écoute du telc A2·B1 (Hören et Hören und Schreiben)

Préparé le 6 nov. 2026 par la session « telc : Écouter ». **Rien n'est généré sans l'accord écrit de Jacques dans
cette session.** D'ici là, la page parle avec la voix du téléphone.

## Ce qu'il y a à dire

Compté sur `donnees/hoeren.json` (la lecture en lettres `dit` quand une réplique a des chiffres) :

| lot | caractères |
|---|---|
| Hören, série 1 (Teil 1 à 4) | 5 106 |
| Hören, série 2 | 4 614 |
| Hören und Schreiben, série 1 (5 répondeurs) | 1 388 |
| Hören und Schreiben, série 2 | 1 353 |
| Consignes (Aurora) et « Nummer 42 » à « Nummer 46 » | 1 091 |
| **Total** | **13 552 caractères, 91 fichiers, environ 15 minutes de son** |

Modèle **multilingual v2** (jamais Flash) : 1 crédit par caractère, soit **≈ 13 600 crédits**.

## Les voix : 12 locuteurs, 6 femmes et 6 hommes, de 20 à 75 ans

| rôle | qui | voix | caractères |
|---|---|---|---|
| aurora | les consignes | Aurora, la voix du cours (`8HePnvwzEdJ614CQMPqF`) | 1 091 |
| mark | Mark, 25 ans | Mark-VD-03 (`J8ovlSvQ5WTDCCxIM8U0`) | 777 |
| anna | Anna, 30 ans (et l'annonce de l'aéroport) | Anna-VD-01 (`92qyovlOYJE0EVmWB0fA`) | 1 904 |
| brandt | Frau Brandt, la gérance, 55 ans | celle qui la joue au DTZ (`cDlEZdkTayS2jHnyaXx6`) | 888 |
| f_mittel | femme de 40-45 ans (voisine, mère, cabinet, musée…) | la Dame du DTZ (`N85Zhun98cg4usHJ1afQ`), à réécouter | 2 442 |
| m_mittel | homme de 45-50 ans (chef d'équipe, libraire, atelier…) | le Beamte du DTZ (`lwbCRuiP1VdfP1CRfjHk`), à réécouter | 1 775 |
| m_alt | homme de 65-70 ans (Herr Brückner, retraités) | le Nachbar du DTZ (`o66wtFhUpq7rflsMnh38`), à réécouter | 820 |
| f_jung | femme de 20-25 ans (étudiante, accueil) | **à choisir** | 1 109 |
| f_alt | femme de 70-75 ans (Gerda) | **à choisir** | 218 |
| m_jung | homme de 18-22 ans (l'apprenti, le livreur) | **à choisir** | 854 |
| radio_f | animatrice, annonces au supermarché | **à choisir** | 830 |
| radio_m | animateur, annonces à la gare, à la radio | **à choisir** | 844 |

Reprendre les voix du DTZ garde les mêmes personnes d'un bloc à l'autre (Frau Brandt a la même voix au DTZ et au
telc). Les cinq voix à choisir viennent de la bibliothèque d'ElevenLabs (voix allemandes natives) : je propose
trois candidates par rôle, une phrase chacune, à écouter à l'aveugle comme pour Aurora.

## Le coût

| poste | crédits |
|---|---|
| Les 91 fichiers | ≈ 13 600 |
| Reprises (une prise ratée sur quatre, au pire) | ≈ 3 400 |
| Échantillons à l'aveugle (5 rôles × 3 candidates) | ≈ 2 500 |
| **Plafond demandé** | **20 000 crédits** |

Pris sur le solde de l'abonnement Pro renouvelé le 4 nov. (600 000 crédits pour 99 $), aucun nouveau paiement :
**environ 3,30 $** au prix du Pro (3,60 $ au prix du Creator). Les voix de la bibliothèque ne coûtent rien de plus.

## Après la génération

1. `python audio/controler_sons.py --dossiers de` : aucun SATURE, CLIC ni TRAINE.
2. Les lectures `dit` recopiées dans `audio/lectures/de.json`.
3. Chaque réplique reçoit son champ `mp3` dans `hoeren.json` : la page joue le fichier, sinon le téléphone.
4. **L'hébergement** : Firebase Hosting est plein (erreur 429), rien n'y est déposé. Les voix de l'oral du DTZ vivent
   dans le dépôt (`visuel/prototype/dtz/voix/`) ; les nôtres feraient environ 15 Mo dans `visuel/prototype/telc/voix/`.
   Où les mettre : question posée au chef d'orchestre.
