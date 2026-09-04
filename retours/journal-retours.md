# Journal des retours de testeurs — Wortando

Ce que les testeurs ont signalé, et ce que l'app a changé en conséquence.
Reconstitué le 4 septembre 2026 à partir de l'historique git, qui a gardé la
trace de chaque correction : plusieurs messages de commit disent explicitement
« signalé par l'usager ».

**À quoi ça sert.** Le formulaire de demande d'accès à la production de Google
Play pose trois questions dont les réponses vagues sont le motif de refus le
plus fréquent : comment tu as recruté tes testeurs, quel a été leur engagement,
**quels retours tu as reçus et ce que tu as changé grâce à eux**. Ce fichier est
la matière première de la troisième — à résumer, pas à recopier.

**Les testeurs sont désignés par un numéro**, pas par leur nom : ce journal peut
donc être partagé ou versionné sans publier de données personnelles sur eux. La
correspondance numéro → personne est dans `retours/cle-testeurs.txt`, qui n'est
pas versionné.

⚠️ **La colonne « Qui » est à compléter.** L'historique git dit qu'un usager a
signalé le défaut, jamais lequel — je ne l'invente pas.

---

## Défauts signalés et corrigés

| Date | Version | Qui | Ce qui a été signalé | Ce qui a changé |
|---|---|---|---|---|
| 2026-08-26 | v214 | ? | Le bandeau annonçait la v213, mais « Recharger » laissait l'app en v212, indéfiniment — l'app paraissait cassée. | `version.json` était lu depuis raw.githubusercontent (à jour en secondes) alors que la page vient de GitHub Pages, qui doit redéployer. Le bandeau promettait une version qu'aucun rechargement ne pouvait livrer. |
| 2026-08-26 | v215 | ? | Le menu « Construire la phrase » affichait « A1 (990) » : lu de bonne foi, ça annonce 990 questions, alors que la série en tirait 12. | Le bouton porte maintenant « A1 / 12 phrases tirées de 990 ». Le bandeau de version, source du défaut ci-dessus, est retiré entièrement. |
| 2026-08-26 | v216 | ? | Demande : les séries de douze phrases étaient trop courtes. | Série portée de 12 à **75 phrases par niveau**. Le libellé du menu suit tout seul, il est construit depuis la constante. |
| 2026-08-26 | v217 | ? | Dans « Construire la phrase », toucher VÉRIFIER sans avoir placé tous les mots **ne produisait rien** — aucun message, l'app semblait ne pas répondre. | Un `return` nu refusait silencieusement d'évaluer une réponse incomplète. L'app dit maintenant qu'il manque des mots. |
| 2026-08-26 | v218 | ? | « Inviter un ami » s'affichait pour tout le monde, alors que l'inscription exige un code que seul l'admin peut créer. Un testeur qui partageait l'app créait une demande qu'il ne pouvait pas satisfaire. | Bouton réservé au compte administrateur. |
| 2026-08-27 | v225 | Regina | **Sortait de l'app pour consulter un dictionnaire.** Le retour qui compte le plus : il nomme le moment où le produit perd la personne. | Dictionnaire intégré à la recherche existante — une seule barre, deux blocs de résultats (cartes du cours d'abord, dictionnaire ensuite). 145 000 entrées WikDict, sans progression ni exercice, pour ne pas noyer les 3 400 mots du cours. |
| 2026-08-27 | v228 | ? (depuis un iPhone) | Chercher « Scherbe » ne donnait rien, alors que le dictionnaire contient bien le mot. | Il était sous le pli : la section Dictionnaire commençait à 910 px sur un écran de 844, derrière un bloc « aucun résultat » et six suggestions inutiles. Quand les cartes ne trouvent rien, le dictionnaire passe devant — 293 px au lieu de 910. |
| 2026-08-31 | v320 | ? | Un exercice proposait trois formes de *heissen* et, en quatrième tuile, « mache » — un verbe étranger à la question. | Défaut **structurel** : 77 verbes n'ont que trois formes distinctes au présent, et le générateur complétait avec n'importe quoi. Touchait 8 exercices sur 50. Nouvelle règle : moins de tuiles plutôt qu'une tuile fausse. |
| 2026-08-31 | v321 | ? | Codes d'invitation et testeurs disparaissaient du tableau de bord, puis revenaient seuls — ça se lisait comme une perte de données. | Rien n'était perdu : la requête partait avant que Firestore soit prêt (typique au démarrage à froid de l'app installée). L'écran distingue maintenant « il n'y a rien » de « je n'ai pas pu lire », et propose de réessayer. |
| 2026-09-01 | v347 | (constaté sur l'iPhone de test) | Une seule voix allemande disponible, de qualité de base ; les voix Siri sont fermées aux applications web. Chaque testeur aurait dû configurer son téléphone. | 5 260 fichiers de prononciation générés d'avance et déposés sur Firebase Hosting : tout l'allemand A1-A2 sort dans la même voix pour tout le monde, sans réglage. |
| 2026-09-02 | v374 | ? | Un onglet ouvert de longue date restait bloqué sur une vieille version, des semaines durant. | Le verrou anti-boucle testait la simple *présence* d'une clé de session : une fois rechargé, l'onglet ne relisait plus jamais `version.json`. |
| 2026-09-02 | v386 | ? | Dans l'épreuve de lecture, on relisait trois fois la même annonce, à la 3e, la 11e puis la 20e question. | Les questions d'un même texte étaient mélangées à plat. Le numéro du texte voyage maintenant avec la question : on répond d'affilée, comme à un vrai examen. |
| 2026-09-03 | v395 | (préparation Play Store) | Le service worker interceptait **toutes** les pages du domaine et servait l'app à leur place — la politique de confidentialité était inaccessible. | Interception restreinte à la page de l'app seule. Aucun testeur ne pouvait le voir : rien de ce qu'ils ouvrent n'est une autre page. |
| 2026-08-30 | v293 | Barbara | **Aucun moyen de revenir au recto d'une carte.** Une fois retournée, la seule sortie était de passer à la suivante : revoir le mot de départ — parce qu'on a retourné trop vite, ou pour vérifier qu'on l'avait bien lu — obligeait à refaire un tour de paquet entier. | Une bande de retour sur le quart droit du verso, assez large pour se toucher au pouce sans viser. |
| 2026-08-30 | v294 | (suite du précédent) | La bande étroite demandait encore de viser, alors que le geste se fait au pouce sans regarder. | Le verso se coupe **en deux moitiés** : gauche = revenir au recto, droite = carte suivante. Les deux phrases d'explication cèdent la place à deux signes `←` `→`, un par moitié, à l'endroit exact où il faut toucher — la rangée reproduit la géométrie du geste au lieu de la décrire. |
| 2026-09-04 | v402 | Barbara | Les flèches étaient un peu discrètes. | Flèches agrandies (17 → 24 px) et légèrement assombries. Pas de texte ajouté : la v294 l'avait retiré volontairement, et le signe placé là où l'on touche se comprend seul. |
| 2026-09-04 | v396-v400 | (trouvé en cherchant) | Impossible de savoir si un testeur était encore actif. En cherchant, découverte bien plus grave : **les sauvegardes dans le nuage échouaient en silence depuis des semaines.** | Firestore indexe automatiquement chaque champ et plafonne à 40 000 entrées par document ; la progression en générait davantage. Réparé par une exception d'index. La progression de tous les testeurs se sauvegarde à nouveau. |

---

## Retours reçus, pas encore traités

| Reçu | Qui | Ce qui est signalé | État |
|---|---|---|---|
| sept. 2026 | Barbara | Des entrées de dictionnaire à trois lettres qui **ne sont pas des mots allemands** — exemple donné : « gung », fragment du suffixe *-ung*. | À traiter. Vient vraisemblablement du découpage automatique des données WikDict. |

---

## Comment m'en servir le moment venu

1. **Compléter la colonne « Qui »** avec les numéros de `cle-testeurs.txt`.
2. **Continuer à l'alimenter** : chaque nouveau retour, une ligne — date, qui, ce qui a été dit, ce qui a changé, numéro de version. Trois minutes sur le moment, contre des heures de reconstitution plus tard.
3. **Pour le formulaire Google**, ne pas recopier ce tableau : en tirer trois ou quatre exemples où l'enchaînement *retour → diagnostic → correction → version publiée* est net. Les v217, v225, v228 et v320 sont les plus démonstratifs — un utilisateur signale, la cause s'avère plus profonde que le symptôme, et la correction est datée.

⚠️ Ce que ce journal **ne remplace pas** : le compteur des 12 testeurs pendant 14 jours consécutifs se mesure uniquement dans la Play Console, sur la piste de test fermé. Rien de ce qui précède n'y compte. Ce fichier ne sert qu'aux questions rédigées du formulaire — mais c'est là que se jouent les refus.
