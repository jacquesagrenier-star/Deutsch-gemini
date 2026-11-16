# Conversations jouées : ce qui attend une relecture native

Chaque lot, dans chaque langue, est relu par un locuteur natif avant la mise en ligne. Le relecteur vérifie que
chaque réplique est naturelle, au bon registre (Sie, usted, registre poli), et qu'une faute proposée est bien une
faute qu'on fait vraiment. Les textes sont dans `visuel/prototype/conversation/donnees/<id>.<langue>.json`. On les
joue à `visuel/prototype/conversation.html?c=<id>&apprendre=de|es|en`.

| Lot | Conversation | Allemand | Espagnol | Anglais |
|---|---|---|---|---|
| pp | pp1-pass (contrôle des passeports) | à relire | à relire | à relire (us, gb) |
| pp | pp2-cafe (petit-déjeuner) | à relire | à relire | à relire (us, gb) |
| a1-1 | cafe-voisin (le café, un voisin de table) | à relire | à écrire | à relire (us, gb) |
| pp | pp5-hotel (la réception de l'hôtel) | à relire | à relire | à relire (us, gb) |
| pp | pp6-achats (le marché ; en anglais, une boutique de vêtements) | à relire | à relire | à relire (us, gb) |

## Lot a2-3 (A2, troisième série), écrit le 16 nov. 2026

Allemand à Berlin, espagnol à Madrid, anglais à Boston (américain, britannique par `t_gb`). Registre : Sie / usted
/ poli, sauf Diego (ami : du, tú, familier) et Carmen (voisine : Sie à Berlin, avec un « Wollen wir uns nicht
duzen? » à la fin ; tú à Madrid ; familier à Boston).

| Lot | Conversation | Allemand | Espagnol | Anglais |
|---|---|---|---|---|
| a2-3 | a2-internet (la hotline) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-assurance (Haftpflicht ; seguro de hogar ; renters insurance) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-location-voiture (l'Ostsee ; Segovia ou Toledo ; Cape Cod) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-bagage-perdu (BER ; Barajas T4 ; Logan) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-taxi (Hauptbahnhof ; Atocha ; South Station) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-reserver-tel (réserver au téléphone) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-diner-voisins (chez Carmen, les compliments) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-vacances (raconter au passé, avec Diego) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-conseil-vendeur (le magasin de vélos) | à relire | à relire | à relire (us, gb) |
| a2-3 | a2-puces (Mauerpark ; Rastro ; South End) | à relire | à relire | à relire (us, gb) |

Points à regarder en priorité :
- **Le registre** : Carmen au Sie à Berlin (beaucoup se tutoieraient d'emblée) ; vendeuse de vélos et marchand du
  Rastro à l'usted (à Madrid, ils tutoieraient sans doute).
- **Les fautes proposées** : chacune doit être une faute qu'un francophone fait vraiment. Les moins sûres :
  « Guard the money! » (taxi, en), « Wem denn? » en réaction à « Fotos genommen » (vacances, de), « Ellos
  conducieron » (vacances, es).
- **Les détails locaux inventés** : les fournisseurs Spreenetz, Fibrasol et Harborline (vérifier qu'aucune vraie
  marque ne porte ces noms), le restaurant Harborlight Bistro, les hôtels Spreeblick, Arenal et Harbor Inn, les
  prix (assurances, location, taxi, vélos), les garanties des vélos (de : 2 ans / 1 an, es : 3 ans / 1 an,
  en : 1 an / 3 mois).
- **Les montants dits** : le moteur ne sait écrire en lettres que jusqu'à 99 ; au-delà, chaque total a son `dit`
  écrit à la main (location en allemand, vélos dans les trois langues). La location en espagnol et en anglais
  annonce un prix par jour.
- **L'anglais britannique** : contents insurance (pour renters insurance), hire, petrol, boot, car park, flat,
  holiday, mobile, guarantee, terrace.
