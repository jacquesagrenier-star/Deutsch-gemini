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
  | Fin de l'A1 (le voyage) | 5 ou 6 | |
  | A2 | 6 à 8 | |
  | B1 et plus | jusqu'à 10 | plus de branches |

- **Toujours une fin réussie.** Chaque réponse juste mène à une fin. Une faute (`faux`) ne fait pas perdre : la
  personne réagit dans la langue, son visage aussi, une ligne explique, on réessaie. La faute revient dans le bilan.
  Pas de faute avant l'étape 3 de Premiers pas.
- **Les nombres se disent en lettres** : le champ `dit`, ou `{a_payer:mots}`.
- **Les visages** : une expression par moment (`sourire`, `question`, `attentive`, `surprise`, `perplexe`,
  `amuse`). Celle qui manque retombe sur la plus proche. Les mêmes personnes en allemand et en espagnol.

## Les fichiers

- `visuel/prototype/conversation.html` : le moteur. `?c=<id>&apprendre=de|es` joue une conversation ; sans `c`, il
  montre la liste.
- `visuel/prototype/conversation/donnees/<id>.<langue>.json` : une conversation dans une langue. Ces textes sont
  écrits pour chaque langue, jamais traduits de l'allemand.
- `visuel/prototype/conversation/donnees/index.json` : la liste, dans l'ordre du parcours.
- `visuel/prototype/conversation/personnes.json` : les personnes, leur voix (f ou m) et leurs visages.
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

## Les lots

Chaque lot a son propre fichier par conversation et par langue, ses propres personnes, et une ligne dans
`index.json`. Ce sont les deux seuls endroits partagés : on y ajoute ses lignes sans toucher à celles des autres.

| Lot | Conversations | Langues | État |
|---|---|---|---|
| 0 | moteur, contrôle, café du voyage (escale « manger ») | de | fait (branche `conversation-cafe-a1`) |
| 1 | Premiers pas 1-2 : contrôle des passeports, petit-déjeuner | de, es | fait |
| 2 | Premiers pas 3-5 : demander son chemin, guichet du train, hôtel | de, es | à faire |
| 3 | Premiers pas 6-8 : le marché, la pharmacie, le voisin de banc | de, es | à faire |
| 4 | le branchement dans la séance, la scène et Tout le contenu (`index.html`) | de, es | file de publication et parcours |
| 5 | Voyage A1, escales 1-6 | de, es | à faire |
| 6 | Voyage A1, escales 7-12, puis « s'installer » (logement, Bürgeramt) | de, es | à faire |
| 7 | A2, puis B1 (plus longues), et les conversations « dans la peau de Mark » liées aux épisodes | de, es | plan à faire |

Les visages des lots 2 et 3 sont à chiffrer avant d'écrire : policier, passante, employé du guichet, réceptionniste,
vendeuse, pharmacienne. Chaque lot de textes passe en relecture par un germanophone et un hispanophone.
