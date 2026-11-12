# Les conversations jouées : mode d'emploi

Proposition 9 de la revue d'usage, décisions de Jacques du 11 nov. 2026 :
- « Les conversations, c'est excellent » ;
- « Faudrait que ça commence à 1 » ;
- des visages expressifs (option A) ;
- un grand chantier, en allemand et en espagnol.

L'apprenant ne répète pas une phrase écrite : il **répond**, au micro ou en touchant une réponse, et la conversation
suit son choix. Les embranchements sont écrits à l'avance, sans intelligence artificielle.

## Les règles

- **La famille « toi ».** L'apprenant joue son propre rôle, au Sie (usted en espagnol), face aux gens du quartier :
  serveuse, policier, réceptionniste, voisin. **Ni Anna ni Mark à l'A1** : dans la série, ils ne se connaissent pas
  encore (`video/EPISODES-SUIVANTS.md`). Les conversations « dans la peau de Mark » s'ouvriront avec les épisodes,
  au Sie jusqu'à l'épisode du « du ».
- **Les répliques de l'apprenant viennent de ce qu'il a appris.** En Premiers pas, ce sont les 9 phrases et les
  cartes de l'étape et des étapes précédentes (`premiers-pas.json`). La personne en face parle court ; quelques mots
  nouveaux sont permis chez elle, jamais dans une réponse juste.
- **La longueur**, en échanges, c'est-à-dire en réponses de l'apprenant :

  | Niveau | Échanges | Branches |
  |---|---|---|
  | Premiers pas | 3 ou 4 (environ une minute) | une au plus |
  | A1 (voyage, s'installer, vie quotidienne) | 4 à 6 | |
  | A2 | 6 à 8 | |
  | B1 et plus | jusqu'à 10 | plus de branches |

- **Toujours une fin réussie.** Chaque réponse juste mène à une fin. Une faute (`faux`) ne fait pas perdre : la
  personne réagit dans la langue, son visage aussi, une ligne explique, on réessaie. La faute revient dans le bilan.
  Pas de faute avant l'étape 3 de Premiers pas.
- **Les nombres se disent en lettres** : le champ `dit`, ou `{a_payer:mots}`.
- **Les visages** : une expression par moment (`sourire`, `question`, `attentive`, `surprise`, `perplexe`,
  `amuse`). Celle qui manque retombe sur la plus proche. Les mêmes personnes en allemand et en espagnol.

## Les fichiers

- `visuel/prototype/conversation.html` : le moteur. `?c=<id>&apprendre=de|es|en` (`&variante=gb` pour l'anglais britannique) joue une conversation ; sans `c`, il
  montre la liste.
- `visuel/prototype/conversation/donnees/<id>.<langue>.json` : une conversation dans une langue. Ces textes sont
  écrits pour chaque langue, jamais traduits de l'allemand.
- `visuel/prototype/conversation/donnees/index.json` : la liste des lots ; `lot-<lot>.json` : les conversations d'un lot, dans l'ordre.
- `visuel/prototype/conversation/personnes.json` (et `personnes-<lot>.json`) : les personnes, leur voix (f ou m) et leurs visages.
- `visuel/conversation/visages.py` : fabrique les expressions. C'est **facturé** (0,15 $ l'image) : un devis par lot,
  et l'accord de Jacques dans la session qui dépense.
- `tests/conversations.py` : le contrôle. Il vérifie les chemins, la longueur, le registre, les nombres, les mots
  vus et la liste. **Il doit passer avant tout push.**

## Le format d'une conversation

```json
{
 "id": "pp2-cafe", "langue": "de", "niveau": "A1", "parcours": "premiers-pas", "etape": 2, "registre": "Sie",
 "titre": {"fr": "…"}, "intro": {"fr": "…"}, "bilan": {"fr": "… {a_payer}."},
 "personnes": ["kellnerin"],
 "debut": "bestellen",
 "prix": {"kaffee": 320}, "panier": ["boisson"],
 "textes": {"boisson_fr": {"cle": "boisson", "kaffee": "ton café"}},
 "noeuds": {
  "bestellen": {
   "dit": [
    {"recit": {"fr": "Un petit café, le matin."}},
    {"qui": "kellnerin", "air": "sourire", "t": "Guten Morgen! Was möchten Sie?", "fr": "Bonjour ! …"}
   ],
   "choix": [
    {"t": "Einen Kaffee, bitte.", "fr": "…", "pose": {"boisson": "kaffee"}, "va": "zahlen",
     "puis": [{"qui": "kellnerin", "air": "sourire", "t": "Kommt sofort!", "fr": "…"}]},
    {"faux": true, "t": "Gib mir einen Kaffee.", "fr": "…", "puis": […], "aide": {"fr": "<b>…</b> …"}},
    {"repete": true, "t": "Wie bitte?", "fr": "…", "puis": […]}
   ]
  }
 }
}
```

- `t` : le texte dans la langue apprise. `fr` : sa traduction. `dit` : ce que dit la voix, si ce n'est pas `t`
  (les nombres).
- `va` : le nœud suivant. `null` termine la conversation.
- `pose` : ce que la réponse retient (`{"boisson": "kaffee"}`). `si` : une réplique ou un choix qui ne vaut que si
  l'état dit ceci (`{"markt": "oui"}`).
- Les gabarits : `{a_payer}` est la somme des `prix` des valeurs retenues dans `panier`, écrite en chiffres dans la
  langue du champ. `{a_payer:mots}` l'écrit en lettres. `{arrondi}` et `{arrondi:mots_maj}` donnent le montant
  arrondi pour le pourboire. `{x}` renvoie un texte de `textes`, selon la valeur de sa `cle`.

## La place dans l'app (à brancher)

1. **Dans la séance du jour** : la conversation suit la scène de son étape, le jour où l'étape se termine. Le thème
   illustré reste la dernière partie. La partie « Conversation » est prévue dès le début de la séance (barre stable).
2. **Sur la scène de l'étape** : un bouton « Jouer la conversation » à la fin.
3. **Dans Tout le contenu**, rubrique PARLER : « Conversations », rangées par étape.

La page parle comme une scène (`postMessage` : `bonne`, `exercice`, `fini`, `fermer`). Une bonne réponse fait
avancer les mots, comme dans les scènes.

## Les lots (décisions de Jacques du 11 nov. 2026)

Pour chaque langue (allemand, espagnol, anglais) : **Premiers pas 3 ou 4**, **A1 20**, **A2 une trentaine**, **B1 une
trentaine**. On y ajoute les conversations « dans la peau de Mark », qui s'ouvrent avec les épisodes. Les longueurs
suivent le tableau des règles : 3-4 échanges en Premiers pas, 4-6 à l'A1, 6-8 à l'A2, jusqu'à 10 au B1. Une
**tuile « Conversations »** dans Tout le contenu les range par niveau. Celles avec Anna n'apparaissent qu'après leur
épisode.

**Comment plusieurs sessions travaillent sans se marcher dessus.** Un lot = un fichier `donnees/lot-<lot>.json` (sa
liste de conversations, dans l'ordre), ses fichiers `donnees/<id>.<langue>.json` et, s'il crée des personnes,
`conversation/personnes-<lot>.json`. Une session n'écrit que dans ces fichiers-là. `donnees/index.json` (la liste des
lots) ne change que par le chef. `tests/conversations.py` refuse :
- une conversation dans deux lots ;
- une personne définie deux fois ;
- un fichier qui n'est dans aucun lot.

Une session peut prendre un lot dans une langue (10 fichiers) ou un lot dans les trois langues. Les textes sont
écrits pour chaque langue, jamais traduits.

**Les adaptations par langue.** L'allemand se passe à Berlin, l'espagnol à Madrid, l'anglais à Boston (dollars,
variante britannique par `t_gb`). Une démarche qui n'existe pas dans un pays prend son équivalent :
- l'Anmeldung au Bürgeramt devient l'empadronamiento à Madrid et la carte de bibliothèque à Boston ;
- l'Ausländerbehörde devient la extranjería à Madrid et le DMV à Boston.

En anglais, une conversation n'utilise pas les six scènes écartées (`SCENES_ECARTEES_ANGLAIS`).

| Lot | Niveau | Conversations (identifiants) | État |
|---|---|---|---|
| `pp` | Premiers pas | `pp1-pass` (contrôle des passeports, étape 1), `pp2-cafe` (petit-déjeuner, étape 2), `pp5-hotel` (la réception, étape 5), `pp6-achats` (le marché en de et es, la boutique de vêtements en en, étape 6) | 1-2 faits (de, es, en) |
| `a1-1` | A1 | `cafe-voisin` (fait en de et en), `a1-restaurant` (réserver, le plat du jour), `a1-boulangerie`, `a1-marche` (le kilo, le prix), `a1-chemin` (demander son chemin), `a1-ticket` (le ticket de bus ou de métro), `a1-gare` (aller-retour, le quai), `a1-vetements` (essayer, la taille), `a1-supermarche` (la caisse, le sac), `a1-pharmacie` | 1 fait |
| `a1-2` | A1 | `a1-medecin-rdv` (l'accueil du cabinet), `a1-objet-perdu`, `a1-poste` (un colis), `a1-laverie`, `a1-voisine` (se présenter sur le palier), `a1-parc` (l'heure, le temps qu'il fait), `a1-musee` (billets, réduction), `a1-appartement` (la visite), `a1-mairie` (Anmeldung, empadronamiento, carte de bibliothèque), `a1-cours` (s'inscrire à un cours) | à faire |
| `a2-1` | A2 | `a2-annuler-rdv` (au téléphone), `a2-coiffeur`, `a2-reclamation-resto`, `a2-echanger` (rapporter un article), `a2-banque` (ouvrir un compte), `a2-colis-voisin`, `a2-bruit` (le voisin, poliment), `a2-panne` (le chauffage, le propriétaire), `a2-correspondance` (train en retard), `a2-hotel-probleme` | à faire |
| `a2-2` | A2 | `a2-premier-jour` (au travail), `a2-pause` (entre collègues), `a2-invitation` (accepter, refuser), `a2-sortie` (planifier à deux, comme au DTZ), `a2-symptomes` (chez le médecin), `a2-ordonnance`, `a2-ecole-absence`, `a2-creche`, `a2-club-sport`, `a2-bibliotheque` | à faire |
| `a2-3` | A2 | `a2-internet` (la hotline), `a2-assurance`, `a2-location-voiture`, `a2-bagage-perdu`, `a2-taxi`, `a2-reserver-tel`, `a2-diner-voisins` (compliments), `a2-vacances` (raconter au passé), `a2-conseil-vendeur`, `a2-puces` (marchander) | à faire |
| `b1-1` | B1 | `b1-entretien` (d'embauche), `b1-candidature-tel`, `b1-loyer` (négocier), `b1-reunion-parents`, `b1-titre-sejour` (Ausländerbehörde, extranjería, DMV), `b1-aide-emploi` (Jobcenter, SEPE, Social Security), `b1-specialiste`, `b1-sinistre` (dégât des eaux), `b1-facture` (réclamation), `b1-debat` (donner son avis, comme l'oral du telc) | à faire |
| `b1-2` | B1 | `b1-conflit-voisin`, `b1-horaires` (au travail), `b1-malentendu` (collègue), `b1-fete-quartier`, `b1-conseil-ami`, `b1-pret` (banque), `b1-garage`, `b1-plainte` (vol, à la police), `b1-resilier` (un contrat), `b1-demenageurs` | à faire |
| `b1-3` | B1 | `b1-soiree` (bavarder), `b1-mon-pays` (le présenter), `b1-actualite`, `b1-vol-annule`, `b1-urgences`, `b1-orientation` (l'école d'un enfant), `b1-benevolat`, `b1-location-vacances`, `b1-livraison` (réclamation), `b1-stage` (entretien) | à faire |
| `mark` | avec les épisodes | de : `m-ep1-flughafen` (Mark au guichet d'Anna, Sie), `m-ep2-buergeramt`, `m-ep3-radweg`, `m-ep4-schrippe` (« Sind Sie nicht…? »), `m-ep5-vhs` (les prénoms, toujours Sie) ; es : `m-es01` à `m-es05` (Ana au usted) ; en : aucune (pas de série) | après les épisodes publiés |

Le registre est celui de la situation. Le Sie, l'usted ou le registre poli s'appliquent partout à l'A1. À partir de
l'A2, des collègues ou des amis peuvent se tutoyer : le champ `registre` vaut alors `du`, `tú` ou `familier`. Anna et
Mark restent au Sie / usted jusqu'à l'épisode du « du ».

**Les visages.** Les lots écrivent avec les visages qui existent déjà (`personnes.json`, les personnes des thèmes
illustrés) et notent ceux qui manquent. Les expressions nouvelles se fabriquent dans la session des conversations,
par lot, avec un devis approuvé par Jacques (`visuel/conversation/visages.py`).

**La relecture.** Chaque lot, dans chaque langue, passe par un locuteur natif avant la mise en ligne. La liste des
lots à relire est tenue dans `retours/A-RELIRE-CONVERSATIONS.md`.
