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
| 2026-09-04 | v403 | Kirsty | La carte **montre** la forme du pluriel mais ne permet pas de l'**entendre**, alors que le mot au singulier a son haut-parleur juste au-dessus. Ajoute qu'elle trouve l'app vraiment utile, et que l'absence de cette fonction ne nuirait pas à sa commercialisation — mais qu'elle serait utile. | Un second haut-parleur, plus petit, sur la ligne du pluriel. Il ne prononce que la forme (« die Tische »), jamais l'étiquette traduite « Pluriel : » — sinon la voix dirait « Pluriel di Tische ». Absent sur les 810 noms sans pluriel : un bouton qui ne produit rien se lit comme une panne. |
| 2026-09-04 | v402 | Barbara | Les flèches étaient un peu discrètes. | Flèches agrandies (17 → 24 px) et légèrement assombries. Pas de texte ajouté : la v294 l'avait retiré volontairement, et le signe placé là où l'on touche se comprend seul. |
| 2026-09-04 | v396-v400 | (trouvé en cherchant) | Impossible de savoir si un testeur était encore actif. En cherchant, découverte bien plus grave : **les sauvegardes dans le nuage échouaient en silence depuis des semaines.** | Firestore indexe automatiquement chaque champ et plafonne à 40 000 entrées par document ; la progression en générait davantage. Réparé par une exception d'index. La progression de tous les testeurs se sauvegarde à nouveau. |
| 2026-09-05 | v408 | Jacques | Dans les résultats du dictionnaire, certains mots portent un **« + »** — l'invitation à en faire une carte — mais le toucher répond que le mot **est déjà dans l'application**. Le « + » fait donc croire que l'app ne connaît pas un mot qu'elle enseigne. | Le bouton ne consultait que « Mon vocabulaire », jamais le cours : le refus n'arrivait qu'après le clic. Mesuré : **1 210 entrées du seul dictionnaire de→fr** (verbes et adjectifs comptés seuls) affichaient un « + » impossible. Le cours est maintenant interrogé **au rendu**, et le bouton change de rôle : une **flèche ambre → qui ouvre la vraie carte du cours**. Un clic mort devient un raccourci. |
| 2026-09-05 | v408 | Barbara | Des entrées de dictionnaire **qui ne sont pas des mots allemands** — exemple donné : « gung ». | « gung » n'existe nulle part dans les données : l'exemple était inexact, **le défaut ne l'était pas**. Ce que WikDict publie comme des mots, ce sont les **affixes** : `-heit`, `-keit`, `-bar`, `-chen`, `anti-`, `bio-`… Comptés : **732 sur les quatre dictionnaires** (150 de→fr, 268 de→en, 314 en→de, 0 fr→de). Retirés, index des paquets refait. Contrôle strict : hors affixes, les 153 paquets touchés sont identiques mot pour mot à l'ancien. |
| 2026-09-05 | v409 | Jacques | **Demande une tuile complète pour les connecteurs** — *obwohl, weil, wenn, trotzdem, dass, deshalb* — leurs différences d'emploi, **la place du verbe**, et des exercices. Puis, décisif : **« Je ne vois pas de tuile conjonction. »** | Il avait raison, et le défaut était pire que la demande. **Tout le contenu existait — et personne ne pouvait le trouver.** Écran d'explication, 45 exercices, 18 cartes, panneau à six portes : aucune tuile ne le portait à l'accueil. On n'y arrivait que par *Expressions & tournures → « Relations entre les idées »*, qui ouvrait directement l'écran d'explication — **le panneau ne se voyait qu'en appuyant sur « Retour »**. Une tuile **Connecteurs** est posée à l'accueil, après Structure. Renommée au passage : « Conjonctions · und · weil · aber » excluait *deshalb* et *trotzdem*, qui n'en sont pas — c'est devenu **« Connecteurs · weil · deshalb · obwohl »**, et l'entrée d'Expressions ouvre désormais le panneau, pas l'écran seul. ⚠️ **Reste à faire** : la troisième classe (connecteurs adverbiaux : *deshalb, trotzdem, dennoch, deswegen, außerdem, sonst*) n'a **aucune carte de vocabulaire**, et les exercices plafonnent à 45 là où les autres jeux en comptent 50 à 70. |
| 2026-09-05 | v410 | Jacques | Demande deux exercices de **choix par le sens**, comme dans son cahier : *weil* ou *obwohl*, puis *deshalb* ou *trotzdem*. | Aucune série ne le faisait : celles qui existaient demandaient **où va le verbe**, jamais **ce que les deux moitiés se disent**. Deux séries de 28, bâties sur les **mêmes quatorze situations** — une fois en subordonnée (verbe à la fin), une fois en principale (inversion). Dans chaque duo l'ordre des mots est identique pour les deux réponses : **seul le sens tranche**, ce qui est exactement l'exercice demandé. Les connecteurs des exercices passent de **45 à 101**. ⚠️ Défaut attrapé en cours de route : la traduction s'affiche **avant** la réponse, et « parce que » contre « bien que » donnait la solution sans lire l'allemand. La traduction porte désormais **le même trou** que la phrase allemande ; la phrase complète est passée dans l'explication, qui n'arrive qu'après. Et six indices d'autres séries disaient « compare avec la phrase précédente » alors que les séries sont **mélangées au lancement** — cette phrase-là n'existait plus. Rendus autonomes. |
| 2026-09-05 | v411 | Barbara | L'écran de recherche disait seulement « Rechercher un mot » : **rien n'indiquait qu'on peut chercher en français**, pas seulement en allemand. | C'était écrit à un seul endroit — le texte gris du champ, « Allemand ou français… » — qui s'efface dès la première lettre. Le **titre** le dit maintenant (« Chercher un mot allemand ou français »), et la phrase d'accueil le répète en gras. Les trois langues d'interface suivent : anglais → « German or English », turc → « Almanca veya Türkçe ». |
| 2026-09-05 | v412 | Jacques | Demande d'autres duos de connecteurs, « pour une façon pédagogique ». | Mesuré d'abord : **aucun** des duos candidats n'existait — zéro exercice où l'on choisit entre *wenn/ob*, *wenn/wann*, *aber/sondern*, *weil/denn*, *damit/um…zu*, *als/wie*. Trois séries de 28 écrites, choisies sur un fil précis : **un mot français, deux mots allemands**. *si* → wenn/ob, *quand* → wenn/wann, *mais* → aber/sondern. Ce ne sont pas des subtilités allemandes, ce sont des pièges que **la langue de départ** tend : un germanophone ne s'y trompe jamais. Effet secondaire heureux : la traduction affichée **peut rester naturelle**, puisque le mot français y est ambigu des deux côtés — elle montre le piège au lieu de le trahir. Sur *aber/sondern*, cinq phrases portent une négation et prennent quand même *aber* : sans elles, on retient la règle fausse « négation donc sondern ». Connecteurs : **101 → 185 exercices**. ⚠️ Reste proposé : *weil/denn* (la place du verbe, miroir des précédentes), *damit/um…zu*, *weil/wegen* et *obwohl/trotz*. |
| 2026-09-05 | v413 | Barbara (relayé par Jacques) | **Voir les synonymes sur la carte**, « surtout lorsqu'on arrive dans les niveaux B1 ou C1 ». Avec sa propre réserve : ne pas surcharger la carte. | **Fait, et sa remarque sur les niveaux était exacte** : B1 368, C1 145, B2 97 contre A1 64 et A2 79. Règle : deux mots sont voisins s'ils partagent une traduction **en français ET en anglais** — le contrôle croisé écarte 1 278 paires et n'en garde que 753 (*voler* réunissait fliegen et stehlen). Puis 92 exclusions de forme : féminins, réfléchis, pluriels, verbes à préfixe (*anrufen/rufen* — on téléphone, on ne crie pas) et **raccourcis**. Ce dernier mot vient de la **partenaire de Jacques, germanophone**, qui a tranché les 17 paires que j'avais gardées : *Reha/Rehabilitation*, *Backofen/Ofen*, *Anwalt/Rechtsanwalt* abrègent le même mot, ils n'en nomment pas un autre. C'est devenu une règle, pas une liste, pour que les suivantes tombent seules. Résultat : **1 006 cartes, 1 312 liens, 30 ko**, chargés à la première carte. Affichage : une ligne « AUSSI » en bas du verso, sous la phrase d'exemple. Sa réserve se règle d'elle-même — **83 % des cartes ne changent pas**. ⚠️ Les mots ne sont **pas touchables** : ouvrir la carte du voisin remplacerait le paquet en cours par une séance d'une carte, et perdrait la révision commencée. À faire le jour où l'on saura revenir au paquet. |
| 2026-09-05 | v414 | Jacques | Cherche **Wandel**, qui a pourtant un voisin (*Veränderung*) : **la ligne n'apparaît pas**. | Défaut de la v413, trouvé le jour même. Le fichier des voisins se charge **à la première carte** — mais la carte est déjà dessinée quand il arrive, et **rien ne la redessinait**. Conséquence exacte : une carte ouverte **seule depuis la recherche** n'affichait jamais sa ligne, puisqu'il n'y avait pas de carte suivante pour en profiter. C'est précisément le geste que je venais de lui demander de faire pour vérifier. Le chargement rappelle maintenant l'affichage de la carte en cours, et la carte reprend sa hauteur. |
| 2026-09-05 | v416 | Jacques, pour Barbara | Demande une **tuile temporaire** où Barbara pourra cocher les paires de synonymes qui ne sont pas acceptables. | Faite. La relecture se passe **dans l'app**, pas sur une page à part : elle l'a déjà installée, il n'y a ni lien à ouvrir ni compte à créer. Les 658 paires, groupées par niveau, avec la traduction sous chaque paire et un seul geste — « pas un synonyme ». Rien de neuf n'est téléchargé : les paires viennent de `synonymes.json`, déjà chargé pour la ligne du verso, et les traductions de l'index de recherche. Les réponses partent dans Firestore **en une seule chaîne** — pas un tableau, dont Firestore indexerait chaque entrée : c'est ce plafond-là qui avait fait échouer les sauvegardes en silence (v396-v400). Un bouton « copier ma liste » reste le chemin garanti vers WhatsApp. ⚠️ **La tuile n'est visible que pour l'admin** pour l'instant : elle s'ouvrira à Barbara par une **empreinte** de son adresse, jamais par l'adresse elle-même — le dépôt est public, et c'est exactement ce que `cle-testeurs.txt` évite en restant gitignoré. À retirer quand la relecture sera faite. |
| 2026-09-05 | v419 | Barbara, en pleine relecture | Tombe sur **Swimmingpool**, puis sur **parkieren** : ces mots ne lui semblent pas allemands. | **Ni l'un ni l'autre n'est retiré, et les deux constats étaient justes à leur façon.** *Swimmingpool* est dans le Duden (*der Swimmingpool*), un anglicisme installé. *parkieren* est **suisse** — pas autrichien — et l'app le savait déjà : sa fiche porte le registre `schweizerisch`. Ce qui manquait, c'est que **la ligne des synonymes montrait le mot nu**. Jacques a tranché mieux que la suppression : marquer la région entre parenthèses. **38 mots des paires portent une marque** (17 autrichiens, 17 suisses, 4 de registre écrit) et affichent désormais `(A)` ou `(CH)` — les abréviations des listes officielles. *Karotte → Rüebli (CH)*, *Kellner → Ober (A)*, et la paire où les deux sont marqués : *Metzger (CH) ⇄ Fleischhauer (A)*. Sans ça, un apprenant croyait tenir deux mots interchangeables partout. ⚠️ Écarté en chemin : retirer un nom du cours **décale la progression des suivants** — elle est indexée par position pour tout sauf les verbes. La suppression de *Swimmingpool* aurait fait hériter quatre mots de Sport B1 de la progression de leur voisin, en silence. |
| 2026-09-05 | v421-v422 | Jacques | Deux demandes liées. (1) **Ne pas changer la façon d'expliquer d'une carte à l'autre** : reprendre « surtout en Suisse » de la carte plutôt qu'inventer une abréviation. (2) Un **ⓘ** pour comprendre **quand un mot reviendra** — « la règle des quatre dates » — mais surtout **pas sur la carte**, où il se lirait comme un indice. | (1) La marque régionale reprend désormais les clés `usage_autriche` / `usage_suisse` de la carte. Une même information écrite de deux façons se lit comme deux informations différentes — et « surtout » porte une nuance que le nom de pays seul perdait : le mot n'est pas interdit ailleurs, il est d'usage là-bas. (2) Le ⓘ vit **dans le bloc des boutons de jugement**, qui n'apparaît qu'après le retournement : sa réserve se règle d'elle-même. Le panneau donne la règle réelle, lue dans le code : **10 min → 1 jour → 3 jours → maîtrisé**, « Encore » remet à zéro et ramène le mot 3 cartes plus loin, et un mot maîtrisé revient une fois 16 jours après. ⚠️ Le texte est **construit à partir des constantes**, jamais recopié : `SRS_PREMIERE_MINUTES` a été nommée pour ça. Un chiffre recopié dans une explication finit toujours par mentir. |
| 2026-09-05 | v423-v426 | Jacques | Suite de l'aide : **une section par bouton**, avec le nom du bouton en gras ; **des couleurs** pour distinguer les trois ; et surtout — « au lieu de *nouveau mot* sur Je savais, mettre **10 minutes, 1 jour, 3 jours, maîtrisé** ». | **Les trois boutons disent maintenant ce qu'ils font.** Le bouton *Encore* annonçait déjà son échéance ; *Je savais* affichait le palier atteint (« nouveau mot »), que les pastilles disaient déjà — il annonce désormais **ce que ce clic programme** : 10 min → demain → 3 j → maîtrisé ✓ · 16 j. Découverte en le faisant : les quatre libellés `echeance_*` **existaient dans les trois langues sans aucun emploi**, restes d'une version où le bouton le disait. Et *« Je connais déjà ce mot — ne plus me le montrer »* était **faux** : le mot revient dans 16 jours. Il le dit. ⚠️ **Refusé, avec raison donnée** : le dégradé jaune → orange → vert d'un bouton à l'autre. L'orange sur la bonne réponse apprend le mauvais réflexe, et le vert sur *Je connais déjà* ferait du raccourci le choix le plus désirable — alors que c'est le seul geste qui abîme la révision en silence. Les sections portent donc **la couleur de leur bouton**, et la progression est teintée là où elle existe : les quatre étapes. |
| 2026-09-05 | v427-v428 | Jacques | (1) Retirer « maîtrisé ✓ » du bouton et montrer la maîtrise **autrement — un trophée sur la carte**. (2) « J'ai vu une dictée apparaître puis disparaître : c'est quoi la règle ? » | (1) Les quatre étapes deviennent **quatre délais** — 10 min → demain → 3 j → 16 j. Le mot « maîtrisé » n'apprenait rien de plus : les quatre pastilles pleines le disent, les confettis le fêtent, et un **trophée** reste ensuite sur la carte (au verso seulement — sur le recto il dirait « tu sais celui-là » avant qu'on ait cherché). (2) **La règle était : fin de paquet, et paquet de noms uniquement.** Conséquence qu'il ne pouvait pas voir : en « Mots au hasard », son mode habituel, le paquet compte jusqu'à **1 840 cartes et ne finit jamais** — la dictée lui était donc invisible. Même défaut que la tuile Connecteurs ce matin : une fonction complète derrière une porte que personne n'emprunte. Une entrée **🎧 Dictée — 20 noms** est posée dans le panneau Noms. La dictée n'a pas changé, seulement le chemin pour y arriver. |
| 2026-09-05 | v429-v431 | Jacques | (1) « La dictée devrait s'appliquer **aux adjectifs, aux adverbes, aux verbes** ». (2) *« Basé sur la répétition espacée »* — **« pour les gens, ça ne veut rien dire »**. | (1) Une seule ligne bloquait tout : le constructeur lisait `card[0]` et `"nomen"` en dur. Il prend le mode ; **verbes, adjectifs, adverbes et expressions marchaient déjà**, personne ne le leur avait demandé. Portes ajoutées dans les quatre panneaux, et le bouton de fin de paquet n'est plus réservé aux noms. (2) La ligne dit maintenant **combien de cartes attendent** — 3 577, 1 314, 981 — au lieu de nommer la méthode. ⚠️ **Deux défauts trouvés en testant.** `sansDoublons()` prenait `item.word[0]` comme clé : juste pour un nom (tableau), `undefined` pour un verbe (objet) — **les 1 314 verbes s'écrasaient en une seule entrée**, une carte au lieu de vingt, sans la moindre erreur. Et le panneau, ouvert avant la fin du chargement, annonçait **« rien à revoir »** au lieu de « je n'ai pas encore pu compter » : exactement le défaut de la v321. Il affiche « Un instant, je compte… » et se redessine quand le cours arrive. |
| 2026-09-05 | v432 | Jacques | « **3 577, c'est un peu décourageant.** Pédagogiquement, qu'est-ce qu'on pourrait faire ? » | Il avait raison, et **le chiffre cachait un défaut plus grave**. Un mot **jamais vu** n'a pas d'échéance : il compte donc comme « dû ». Personne n'a 3 577 révisions en retard — il y a une poignée de mots qui reviennent, et un immense réservoir de mots pas encore rencontrés. La ligne annonce désormais **la séance**, bornée à 30 : *« Une séance de 30 cartes »*, et *« · 12 à revoir »* seulement quand il y a une vraie dette. ⚠️ **Le défaut sous le chiffre** : la séance mélangeait tout et prenait 30 cartes **au hasard** dans le réservoir. Une carte due en retard avait donc **0,8 % de chances** d'y figurer — il fallait en moyenne **119 séances** pour la revoir, alors que c'est exactement le mot qu'il fallait travailler. Les révisions passent maintenant **en premier** : vérifié, les 12 mots dus occupent les 12 premières places de la séance. |
| 2026-09-05 | v433-v434 | Jacques | (1) Les quatre échéances devraient se lire **« dans 10 minutes »**, pas « 10 min ». (2) **Le trophée n'apparaît qu'au retour de la carte** — le montrer tout de suite, avec un petit feu d'artifice. (3) Dans la barre de recherche de l'accueil, **« il y a un clic de trop »**. | (1) Fait : *dans 10 minutes → demain → dans 3 jours → dans 16 jours*. Sous un bouton qu'on s'apprête à toucher, on ne lit pas une durée, on lit quand ça revient. (2) Le trophée arrivait **seize jours plus tard**, quand plus personne ne se souvient de l'avoir mérité. Il se pose maintenant au clic — la carte attendait déjà 1 250 ms — avec une couronne d'étincelles. (3) **La barre était un `<button>`.** Sur iOS, le clavier ne s'ouvre que dans le geste de l'utilisateur : le `focus()` différé de l'écran suivant arrivait trop tard, d'où la deuxième touche. C'est un vrai champ de saisie, et ce qui a pu être tapé avant la bascule est repris. ⚠️ Deux phrases fausses trouvées en chemin : le message de maîtrise disait encore « reviendra **une fois** dans 16 jours » (il revient tous les 16 jours), et « aucun résultat » annonçait un cours **« du niveau A1 au B2 »** alors que le C1 existe depuis longtemps — la borne est désormais lue dans `LEVELS`. |
| 2026-09-05 | v438-v439 | Jacques | (1) Introduire **seitdem**, **seit**, **bis** — et la règle : subordonnée en tête → verbe, puis sujet. (2) « Les exercices pour ce genre de situation sont très importants » : des **blocs à placer un à un**, au présent, au parfait et au futur. | (1) Deux manques confirmés avant d'écrire : *seit* et *seitdem* étaient **absents** du vocabulaire (bis, bevor, nachdem, während y étaient), et la règle n'était **écrite nulle part** — « subordonnée en tête », « première place » : zéro occurrence dans tout `index.html`. Série de 24 : 14 subordonnées en tête, **6 groupes circonstanciels** (*Seit zwei Jahren lerne ich…* — la règle parle de la première place, pas des subordonnées) et **4 phrases retournées** sans inversion, le contraste sans lequel on retient « avec weil, on inverse ». *seit* y figure dans ses deux rôles, conjonction et préposition. (2) Le mécanisme des blocs existait mais tirait ses phrases du vivier général : rien ne garantissait qu'une seule porte un connecteur. 24 phrases écrites pour ça — 13 Präsens, 7 Perfekt, 4 Futur — sans leurres lexicaux : la seule question est la position. ⚠️ Au passage, la ligne « Traduction : » s'affichait vide sur ces exercices ; elle se masque désormais quand il n'y a rien à y mettre. |

---

## Retours reçus, pas encore traités

| Reçu | Qui | Ce qui est signalé | État |
|---|---|---|---|
| 2026-09-04 | Stelios | **Ajouter des langues de traduction** pour élargir le public : *« many people that learn German do not speak English so it would be a good idea to add more languages to translate to »*. | ⚠️ **Confirme une direction déjà engagée, qu'il ignore.** L'app a déjà **quatre** langues d'interface : français, anglais et **turc complets** (1 017 clés chacun), ukrainien à 12 % (120 clés). L'outillage d'ajout d'une langue existe et a été rodé sur le turc. À lui répondre — et lui demander **laquelle** il voudrait : une demande nommée vaut mieux qu'un principe. |
| 2026-09-04 | Shashwat | A répondu **oui** pour Android, mais pas à la question sur ce qu'il faudrait améliorer. | Relance légère envoyée. Noté comme testeur Android — voir `cle-testeurs.txt`. |
| 2026-09-04 | Kirsty | *« Honestly I think it's already a lot better for someone like me than multiple others out there. »* Et : elle attend de savoir **quand ce sera compatible Android** pour l'installer sur le téléphone de Peter. | ⚠️ **Malentendu à lever, pas un défaut** : l'app tourne déjà sur Android — c'est une app web, elle s'ouvre dans n'importe quel navigateur et s'installe sur l'écran d'accueil depuis la v258. Rien à attendre. Ce qui viendra plus tard, c'est la version du Play Store. Si une utilisatrice croit devoir attendre, d'autres le croient aussi : **à dire explicitement dans les prochains messages**. Action : générer un code d'invitation pour Peter. |
| 2026-09-04 | Kirsty | Va utiliser l'app tout le week-end et revenir avec ses remarques. | À relancer lundi si rien n'arrive. |

| Reçu | Qui | Ce qui est signalé | État |
|---|---|---|---|
| 2026-09-04 | Jacques (iPhone, puis portable) | **Aucun son sur les deux premières cartes** en entrant dans l'app. Ça ne démarre qu'à partir de la troisième. Sur le portable, cliquer explicitement sur le haut-parleur débloque le reste de la séance. Se produit sur les **deux** plateformes. | **Diagnostic partiel.** Le journal audio de l'app montre que les mots sans fichier basculent vers la voix du navigateur : `das Tablet` (A2) → `BASCULE, fichier absent` → `SYNTHESE`. Contrôle du manifeste contre le disque : **953 textes de A1-A2 n'ont aucun fichier** (63 en A1, 890 en A2 — un quart du niveau), plus la totalité de B1-C1, jamais générée. Comme Jacques révise en « Mots au hasard », qui pioche dans tous les niveaux, **l'essentiel de ses cartes passe par la synthèse**. **Confirmé par Jacques : vraiment aucun son, pas un son faible.** Le moteur de synthèse est donc muet à froid, alors que le journal montre l'énoncé parti avec la bonne voix — aucune erreur, aucun événement, ce qui rend le défaut invisible. **Corrigé pour de bon en v406**, après deux fausses pistes. Ce n'était ni le volume, ni un moteur froid : **c'est une carte sur deux**, selon qu'elle a un fichier enregistré ou non. Confirmé deux fois par Jacques — muet une carte sur deux en « Mots au hasard », et **parfait dès la première carte en A1**, le seul niveau entièrement généré. Cause : quand le fichier manque, la voix du téléphone est lancée **depuis le gestionnaire d'erreur**, donc hors du geste — et iOS ne l'autorise que pendant un geste. Ce qui la rendait insaisissable : au deuxième appui, le fichier est déjà en liste noire, l'app ne le tente plus et parle dans le geste, donc « ça marche ». v406 sonde le fichier **au moment où la carte s'affiche**, avant le retournement : la réponse est connue quand le geste arrive. ⚠️ Au passage, la v404 a cassé toute l'app une heure durant — `let syntheseAmorcee` déclaré deux fois, erreur de syntaxe, plus une seule tuile ne répondait ; `verifier.py` a dit « aucun problème » car il ne parse pas le JavaScript. Écarté en chemin : le volume 0,5 de la synthèse n'est pas un défaut, il aligne délibérément la voix système sur les fichiers, masterisés à −14 LUFS. |
| 2026-09-04 | (suite de la v403) | Le bouton du pluriel existe, mais les pluriels **ne sont pas dans le manifeste audio** : c'est la voix du navigateur qui parle, pas la voix enregistrée. Sur iPhone, où une seule voix allemande existe, la différence s'entend. | Chiffré : 2 852 formes uniques, **39 467 crédits** pour tous les niveaux, dont **9 063 pour A1-A2 seuls**. Peu, comparé aux 424 922 crédits que représente encore B1-C1. À faire en même temps que la prochaine génération, pas avant. |
| 2026-09-05 | v440-v441 | Jacques | Deux précisions sur les exercices de blocs, à un jour d'écart. (1) « **Un bloc pour le sujet, un bloc pour le verbe** » — des blocs qu'on assemble, pas des mots isolés. (2) « Naturellement, lorsqu'on est en Perfekt, il faut **séparer l'auxiliaire** du verbe. » | (1) Sa découpe est meilleure que la mienne, et pour une raison précise : **la subordonnée devient un seul bloc**. La règle dit qu'elle compte pour **un** élément — c'est ce qui explique l'inversion quand elle passe devant. Mot à mot elle en comptait cinq, et la règle restait une affirmation ; en un bloc, on la voit occuper la première place. 202 blocs → 107, soit 4 à 5 par phrase au lieu de 7 à 10 — et quatre tuiles tiennent sur une rangée de téléphone, dix non. (2) Il a raison sur le fond : `haben`/`sein` et le participe **ne vont pas au même endroit** — deuxième place et fin de phrase dans la principale, fin de phrase et **après le participe** dans la subordonnée. Collés en un bloc, ces deux règles sont invisibles et l'exercice ne demande rien. Même traitement pour `werden` + infinitif et pour la particule séparable. La série passe de **24 à 60** exercices (19 Perfekt, 27 Präsens, 14 Futur), et accueille les connecteurs qui manquaient — *deshalb*, *trotzdem*, *danach*, *dass*, plus *aber* et *sondern* pour la raison **inverse** : ils ne bougent rien, et il faut l'avoir vu pour ne pas inverser partout. ⚠️ Contrôle en double saisie : chaque phrase est écrite deux fois, en blocs et entière, et le script refuse d'écrire si le recollage ne redonne pas la phrase à la lettre. Un espace de trop rendrait l'exercice **impossible à réussir sans que rien ne le signale**. Corrigé en chemin : *« Seitdem er hier arbeitet, wird er jeden Tag früher aufstehen »* mêlait un ancrage passé et un futur — un germanophone l'aurait relevée. |
| 2026-09-05 | v442 | Jacques | « Il y a des exercices qu'on faisait en classe : certains connecteurs sont **en paire**, on peut les utiliser à l'inverse en changeant la phrase de côté. » | L'exercice existe dans son cahier, pas dans l'app : *Ich bleibe zu Hause, **weil** es regnet* → *Es regnet, **deshalb** bleibe ich zu Hause*. Mêmes faits, deux moitiés échangées, et le connecteur **change de nature** — subordonnant d'un côté, adverbe de l'autre. **C'est le seul exercice qui met les deux régimes sur la même phrase.** Rencontrés séparément — une tuile pour *weil*, une autre pour *deshalb* — ils passent pour deux vocabulaires appris l'un après l'autre ; ici on voit une seule idée dite de deux façons qui n'obéissent pas aux mêmes règles. 32 transformations, trois familles et **les deux sens à chaque fois** (savoir aller de *weil* vers *deshalb* ne dit pas qu'on sait revenir) : cause *weil↔deshalb* (10) et *weil↔denn* (6), concession *obwohl↔trotzdem* (9) et *obwohl→aber* (3), temps *nachdem/bevor→danach* (4). *denn* et *aber* y sont pour la raison **inverse** des autres : ils ne bougent rien. Sans eux on retient « connecteur = inversion » et on inverse partout. ⚠️ Deux contrôles avant écriture : le recollage des blocs doit redonner la phrase à la lettre, **et** le connecteur nommé par la consigne doit figurer parmi les blocs — une consigne qui demande *deshalb* sans qu'aucun bloc ne le porte donnerait un exercice impossible, en silence. |
| 2026-09-05 | v443 | Jacques | « Je vois le logo, après ça je vois une vidéo, **il y a comme des flashs**. » Demande aussi de **simplifier** l'ouverture. | **Trois causes, toutes mesurées.** (1) La vidéo **repartait en arrière** : un `<video>` reste affiché sur sa **dernière** image. On découvrait donc l'écran sur la fin de l'animation — le logo d'encre — et le rembobinage qui suivait le faisait sauter à sa version de verre avant de rejouer. Mesuré : après la première ouverture `currentTime` reste à **3,00 s**, et `couvrir()` remontrait cette image-là. Corrigé en rembobinant **avant** de découvrir, et dès que l'écran est caché — où personne ne le voit. `jouer()` n'a donc plus à rembobiner : une ligne de moins, et l'ordre devient impossible à inverser. (2) **L'image de lancement iOS montrait un autre logo** : elle date du 28 août et reproduit la première image de l'**ancienne** vidéo (W plat, bleu encre), remplacée en v372-v373 par une vidéo qui commence sur un W de **verre**. iOS montrait le logo fini, puis la page peignait le logo de verre. (3) **Et pas le bon crème** : `#F2EEE2` dans le générateur, `#EFEEE1` dans la feuille de style. ⚠️ La correction de fond : **le générateur ne recopie plus rien**. Il lit dans `index.html` la vidéo (depuis le base64), la couleur de fond, la règle `width:min(..vw, ..vh, ..px)` et le fondu radial, et s'arrête si l'une change de forme plutôt que de produire une image fausse en silence. Une image de lancement qui garde sa propre copie de la vérité finit toujours par mentir — c'est ce qui s'est produit. Au passage, le fondu des bords **manquait complètement** dans le générateur : sur l'ancienne vidéo au fond uni ça ne se voyait pas ; sur celle-ci, dont les coins sont à `#D2CDCA`, on aurait collé un rectangle gris. **Non simplifié volontairement** : le filet CSS à 4 100 ms reste, c'est la seule chose qui débloque l'app si le script d'ouverture cassait — la v404 a montré qu'une erreur de syntaxe là ne se voit nulle part. |
| 2026-09-05 | v444 | Jacques | Sur l'exercice **weil / obwohl** : « l'une des deux moitiés devrait empêcher l'autre. **Je ne comprends pas.** » | **Il a raison deux fois, et la seconde est plus grave.** (1) La formule est une **affirmation déguisée en question** : elle annonce l'obstacle avant qu'on ait choisi, donc on ne sait plus si c'est une piste ou la réponse. C'est ce qu'il décrit. (2) **C'en était la réponse.** La série portait **deux** indices, un par réponse : les 14 *weil* avaient le leur, les 14 *obwohl* l'autre. Reconnaître l'indice suffisait — la phrase allemande devenait décorative et l'exercice ne mesurait plus rien. Même moule, même défaut sur *deshalb/trotzdem*, écrite le même jour. Le contrôle écrit pour l'occasion en a trouvé **deux autres, plus anciennes** : `kasusReconnaissance` (la question demande le cas, l'indice en donnait la définition française — « à qui ? objet indirect », c'est-à-dire Dativ, sans regarder l'allemand) et `praepReconnaissance` (« regarde bien le groupe » n'apparaissait que sur les 9 Wechselpräpositionen). Un seul indice par série désormais, qui pose la question sans la trancher. ⚠️ **Ce qu'aucune relecture ne pouvait voir** : chaque exercice, pris seul, avait un indice juste — la fuite n'existe qu'à l'échelle de la série. `verifier.py` la cherche maintenant : dans un choix fermé (2 à 4 réponses), un indice partagé par ≥ 3 exercices qui ne va **jamais** qu'avec une seule réponse est une erreur. Vérifié en réintroduisant le défaut d'origine — il ressort. Les 4 séries de pronoms relatifs sont exemptées nommément : là, l'indice donne le cas et le genre, c'est l'**énoncé** du drill, pas une fuite. |
| 2026-09-05 | v445 | Jacques | « **J'aime beaucoup** l'exercice où on laisse l'étudiant faire les deux moitiés avec des blocs, avant et après la virgule. J'aimerais qu'on en ajoute pour **tous** les connecteurs. » | Relevé connecteur par connecteur **avant** d'écrire : la série couvrait **la moitié** de ce qu'elle prétendait couvrir. Cinq connecteurs du vocabulaire de l'app n'y figuraient **pas du tout** (*und, oder, denn, da, sodass*), quatre n'avaient qu'un seul exercice (*aber, sondern, dass, danach*), et sept adverbes de liaison manquaient (*deswegen, darum, dennoch, außerdem, dann, also, vorher*) alors qu'ils sont tous dans le vocabulaire des adverbes. **60 phrases ajoutées, 60 → 120** : au moins trois exercices pour chacun des **34** connecteurs, dans les deux dispositions et sur quatre temps. Ce qui entre avec eux et compte autant : les familles qui ne bougent **rien** — *und*/*oder* (pas de place, pas de virgule) et *denn*/*aber*/*sondern*. Une série qui n'aurait montré que *weil* et *deshalb* enseignerait « connecteur = inversion », et l'élève inverserait partout. **La fuite dans l'autre sens**, trouvée par le même relevé : *sobald*, *falls* et *solange* étaient déjà **testés** par les exercices alors que l'app ne les enseignait nulle part — trois cartes ajoutées au vocabulaire des conjonctions, gloses séparées de leurs voisines, en **fin** de liste (la progression est indexée par position). ⚠️ Deux contrôles avant écriture, et le second a servi tout de suite : le recollage des blocs doit redonner la phrase à la lettre, **et** chacun des 34 connecteurs doit atteindre trois exercices. Le premier jet en laissait **douze** sous la barre — c'est le compteur qui les a nommés, pas une relecture. |
| 2026-09-05 | v446 | Jacques | « Peut-être que ce qui serait intéressant, c'est de **mettre la virgule dans un bloc**. Qu'est-ce que tu en penses ? » | **Meilleure idée qu'elle n'en a l'air, et la seconde raison n'est pas celle qu'on voit d'abord.** (1) Collée, la virgule **donnait la réponse** : un bloc « zu Hause, » annonce qu'il ferme la première moitié, donc on n'avait pas à savoir où la proposition s'arrête — la ponctuation le disait. (2) **Et surtout, elle rend testable le cas où il n'en faut pas.** *und* et *oder* ne prennent pas de virgule, une règle qu'aucun exercice ne pouvait poser tant qu'elle était soudée au texte. Les 6 phrases concernées reçoivent une virgule **en leurre** : elle est dans le banc, elle doit y rester. Vérifié à l'écran — poser la virgule dans *Er steht früh auf und geht joggen.* fait échouer la réponse, et l'explication dit pourquoi. Sans ce cas-là, la série enseignerait « il y a toujours une virgule », ce qui est faux. Le moteur n'a rien demandé : il compare les blocs posés un à un et compte combien il en faut. 152 phrases, deux séries. ⚠️ Le recollage change de règle — espace entre les blocs, **sauf** la virgule qui se colle au précédent — et c'est ce contrôle qui tourne avant l'écriture. Effet de bord réglé : une tuile ne descend plus sous **44 px**, la cible tactile d'Apple ; la virgule seule en faisait 29, et *ich*, *es*, *an* n'en étaient pas loin. La règle vaut pour **toutes** les tuiles — singulariser la virgule reviendrait à la désigner. |
| 2026-09-05 | v447 | Jacques | Sur *Wenn er nach Hause kommt, macht er zuerst das Fenster auf* : « **une bonne réponse serait aussi** *Er macht zuerst das Fenster auf, wenn er nach Hause kommt*. » Puis : « qu'on lui **montre** qu'on pourrait l'écrire à l'inverse. Ou que dans un **deuxième temps**, on lui demande de commencer par l'autre moitié de la phrase. » | **Son allemand est juste**, les deux phrases sont correctes. Et ce qui l'empêchait n'était même pas la grammaire : la tuile « Wenn » porte une **majuscule**, elle ne peut donc ouvrir que la phrase, et il n'y a pas de « Er » majuscule au banc. L'exercice n'avait bien qu'une réponse — mais c'est l'**orthographe** qui tranchait une question d'ordre des mots. Il ne l'a pas vue, et personne ne la verrait : **un garde-fou qu'on ne remarque pas passe pour un bogue.** Ses deux idées faites toutes les deux. (1) **Montrer** : l'explication des 54 exercices retournables nomme désormais l'autre ordre en toutes lettres, après la réponse. (2) **Demander** : série nouvelle « Retourner la phrase », 54 exercices — 40 qui font passer la subordonnée derrière, 14 qui la font passer devant. C'est le **seul endroit où l'inversion se voit apparaître et disparaître sur la même phrase** ; ailleurs on rencontre les deux formes séparément et rien ne dit que c'est la même phrase. Non retournés, et pourquoi : *dass* et *ob* (fronter la complétive est grammatical mais marqué, et *Es freut mich, dass…* perd son *es* en route), *sodass* (jamais en tête), l'impératif, les adverbes et les coordonnants — 66 des 120 écartés. ⚠️ La transformation est mécanique mais **relue une par une** avant écriture, et c'est comme ça que *« Falls du Hilfe brauchst, mich ruf an »* est sorti : l'impératif n'a pas de sujet et *Ruf* portait la majuscule initiale. Le garde-fou exige maintenant un vrai sujet. Second contrôle : les deux phrases doivent porter exactement les **mêmes blocs**, à la casse du premier mot près — sinon ce n'est plus la même phrase retournée. |
| 2026-09-05 | (données) | Jacques | « Continue la traduction vers l'ukrainien, **sans arrêt pendant les deux prochaines heures**. Ça ne me fait aucune demande. » | L'interface était à 100 % depuis le matin, le **corpus à 8,8 %**. Relevé d'abord, et il a corrigé deux idées fausses : il y a **six** fichiers de données, pas trois (7 701 entrées, pas ~6 100), et **A1, annoncé complet, ne l'était que pour trois d'entre eux** — 0 adverbe sur 52, 0 mot-outil sur 161, 0 expression sur 68. **677 → 5 040 entrées (65 %)** : **A1, A2 et B1 entiers** — les six fichiers ET les quatre phrases d'exemple de chaque carte de verbe. Les 161 mots-outils au complet. ⚠️ **Le défaut que mon propre compteur cachait** : il comptait `traduction_uk` et annonçait « verbes B1 : 515/515 ». Vrai de ce qu'il mesurait, faux comme affirmation — une carte de verbe porte **quatre** phrases d'exemple (Präsens, Perfekt, Präteritum, Konjunktiv II) et je n'en posais que deux champs sur cinq. Trouvé en lançant `tests/relecture_langue.py --langue uk --suspects`, l'outil du dépôt, **qui compte les champs et non les entrées** : 4 513 champs perdus là où mon tableau disait 862 verbes faits. C'est mot pour mot le défaut décrit dans la mémoire turque — un contrôle de PRÉSENCE qui passe à côté d'une dimension entière. Réparé pour A2 (708 phrases en cinq lots) et le compteur affiche désormais la ligne manquante. Chaque lot passe le même aller-retour : le lot renvoie le mot allemand, l'outil refuse d'écrire si le numéro ne correspond pas, puis relit le fichier depuis le disque. Aucun décalage n'est passé. |
| 2026-09-05 | (donnees) | Jacques | Suite du meme mandat : « **B2 et C1, go** », apres avoir demande « qu'est-ce qu'il reste ». | **Termine : 7 701 / 7 701 entrees, 100 %.** Les six fichiers de donnees sont entierement traduits en ukrainien — 4 206 noms, 1 314 verbes, 981 adjectifs, 470 adverbes, 161 mots-outils, 569 expressions — et chaque carte de verbe porte bien ses **quatre** temps (3 942 phrases de temps posees, dont 1 356 ce soir). Total reel : **19 344 champs**. Le B2 est le niveau ou un mot allemand cesse de decrire une chose et decrit un **raisonnement** (*plausibel*, *fragwuerdig*, *ausschlaggebend*, *mithin*, *gleichwohl*) ; le C1 y ajoute le registre administratif ecrit, et les formules de lettre (*Sehr geehrte Damen und Herren*, *Hochachtungsvoll*) ont ete rendues par les formules ukrainiennes reellement employees, pas traduites mot a mot. ⚠️ **Le controle qui compte, et son etalon.** Poser une traduction ne dit rien de sa qualite : ce qui casse une carte, c'est qu'un meme mot ukrainien reponde a **deux** mots allemands differents — quoi que l'apprenant reponde, il ne peut pas avoir raison. Mesure sur les six fichiers : **155** traductions ukrainiennes partagees, contre **197** en francais et **266** en anglais. L'ukrainien est donc **moins** ambigu que les deux langues deja en ligne, et ce qui reste vient des quasi-synonymes allemands eux-memes (*leise/still*, *oft/haeufig*, *eindrucksvoll/beeindruckend*) — le francais colle exactement au meme endroit. Un chiffre seul n'aurait rien voulu dire ; c'est la **comparaison avec l'existant** qui le rend lisible. Second controle, celui qui aurait pu tout perdre en silence : les cinq noms de champs ecrits (`traduction_uk`, `exemple_uk`, `perfekt_uk`, `praeteritum_uk`, `konjunktiv2_uk`) ont ete confrontes un a un a ceux que `index.html` **lit** reellement — c'est le piege nomme dans la memoire turque, poser la donnee sous un nom que personne ne relit. Les cinq sont lus. |
| 2026-09-05 | v448 | Jacques | En mode Ecoute : « **le son ne se declenche pas pour le francais**. Si j'arrete le mode ecoute puis je repars, le son va commencer en francais. Par contre a ce moment-la, **les phrases debutent avec un volume plus bas, puis a peu pres au milieu de la phrase le son devient beaucoup plus fort, plus fort que tout le reste**. » | **Deux defauts distincts, et la meme fenetre les explique tous les deux** : celle ou l'element `<audio>` qui vient de dire l'allemand tient encore la session sonore d'iOS. **(1) Le francais muet.** `ecouteSyntheseMuette` etait un **booleen**, leve par une sonde de 800 ms. Or la branche qui saute l'etape rend la main **avant** de creer l'enonce — donc `u.onstart`, le seul endroit du code qui rabaissait ce drapeau, n'avait plus **aucune chance** de s'executer. Un seul faux verdict condamnait le francais jusqu'a la fin de la seance, et seul un geste sur Pause/Lecture (qui passe par `amorcerSynthese`) le relevait. Il decrit ce chemin **exactement**. Remplace par un **compteur** : deux verdicts d'affilee avant de commencer a sauter, et meme alors **une tentative sur quatre passe** — c'est le seul chemin par lequel `onstart` peut encore detromper le code. Mesure sur l'arithmetique reelle : avec un faux verdict isole, les six etapes suivantes parlent toutes ; avant, aucune. **(2) Le volume qui monte au milieu.** `son.onended` ne **relachait** pas l'element : `pause()` arrete le son, il ne rend pas la session. iOS **attenue** alors la synthese qui demarre ensuite, puis cesse de l'attenuer quand la session retombe — en plein milieu de la phrase. Une phrase longue traverse la transition, **un mot court finit avant** : c'est pour ca que ca s'entend sur les phrases et pas sur les mots. L'element est desormais relache des sa fin (`removeAttribute` + `load()`, verifie : `networkState` repasse a 3), et un **souffle de 280 ms** laisse la session retomber avant qu'on parle. La meme fenetre expliquant les deux, la sonde passe de 800 a **1800 ms** dans les 3 s qui suivent un fichier — la ou un enonce lent a demarrer se faisait prendre pour un enonce avale. ⚠️ **Le piege evite au passage.** La sonde annule maintenant l'enonce declare mort, pour qu'il ne parle pas par-dessus l'etape suivante. Mais `cancel()` **declenche `onend`**, et `onend` vaut ici `avancer` : sans detacher les gestionnaires d'abord, la sequence avancait **deux fois** et deux voix se chevauchaient. Le jeton de sequence, qui protege partout ailleurs, ne rattrape pas ce cas-la — il n'a pas encore change a cet instant. Le defaut etait deja decrit en commentaire dans le fichier ; c'est ce commentaire qui l'a evite. ⚠️ **Ce qui n'est PAS regle, et comment on le saura.** Le volume **plateau** peut rester trop fort : le code previent depuis la v353 que « plusieurs versions de Safari ignorent purement et simplement `volume` sur un enonce ». S'il entend encore le francais **uniformement** plus fort que l'allemand apres v448, c'est ce cas-la — le reglage a 0,5 qui existe pour rejoindre les fichiers Nadja (-14 LUFS) est ignore, et il n'y a pas de remede par le volume puisque les fichiers sont deja au plafond. Le journal de diagnostic porte desormais `volume demande 0.5 -> retenu X` sur **chaque** enonce du mode Ecoute, et pas seulement sur les cartes : le prochain retour tranchera. |
| 2026-09-06 | v449 | Jacques | **Le meme retour, apres la v448 : « c'est toujours la meme chose. »** En mode Ecoute : « on entend juste le mot allemand ainsi que la phrase en allemand. Ca continue de cette facon, il semble pour toujours, ca change de carte. Quand je pese sur pause, puis je recommence, a ce moment-la le francais embarque. » Et, une fois le francais revenu : « lorsque **la phrase en allemand** arrive, le niveau de son est plus bas au debut, puis a peu pres **au quart de la phrase**, ca devient tres tres fort. » | **La v448 avait cru corriger le francais muet ; elle en a pose la vraie cause.** Sa sonde, apres avoir constate un enonce avale, appelait `speechSynthesis.cancel()` pour le retirer de la file. Or les deux lignes juste au-dessus venaient de prouver que le moteur etait **au repos** (`speaking` et `pending` tous deux faux) : il n'y avait rien a retirer, et ce fichier **documente deja**, dans `direAllemand`, ce que fait `cancel()` sur un moteur au repos -- « il le laisse dans un etat ou l'enonce suivant part sans qu'aucun son n'en sorte ». Le remede cassait donc le moteur qu'il venait de declarer mort. **Boucle qui se nourrit d'elle-meme** : un enonce avale (cela arrive apres un fichier) fait tirer la sonde, la sonde casse le moteur, l'enonce suivant est muet **pour cette raison-la**, la sonde tire encore. Le compteur de la v448 retentait bien une fois sur quatre, mais **sur un moteur que sa propre tentative precedente venait de casser** -- rien ne pouvait plus sortir, et seul un geste sur Pause/Lecture, qui repasse par `amorcerSynthese`, remettait la voix en marche. Il decrit ce chemin mot pour mot. **Mesure sur les deux versions, meme banc** : un seul enonce avale, le moteur se reparant 100 ms plus tard. v448 -> **3 etapes francaises parlees sur 6**, puis SAUTE partout, moteur encore casse a la fin. v449 -> **6 sur 6**, un seul MUET, moteur sain. Le `cancel()` est retire (detacher les gestionnaires suffit) ; `ecouteArreterSon` recoit la meme precaution, il cassait la voix a chaque pause tombant dans un silence. **Le volume : la v448 n'avait vu que la moitie de la frontiere.** Elle laissait retomber la session du `<audio>` **avant de parler**. Mais la sequence traverse la frontiere **dans les deux sens** -- le mot francais est suivi immediatement du mot allemand -- et c'est ce sens-la qu'il entend : iOS attenue le **fichier** qui demarre pendant que la session de la synthese finit de retomber, puis cesse de l'attenuer en cours de lecture. Ce n'est pas un volume qui derape, c'est une attenuation qui s'arrete. Souffle symetrique de 280 ms ajoute avant le fichier, remis a zero par `amorcerSynthese` pour que la regle « aucune attente entre le geste et `play()` » tienne toujours. ⚠️ **Ce qui reste a trancher** : il decrit aussi le **mot francais** comme plus bas que le reste. C'est peut-etre le reglage voulu (`VOLUME_SYNTHESE = 0,5`, qui existe pour rejoindre les fichiers Nadja a -14 LUFS) et non un defaut -- il n'est pas touche. Si l'ecart le gene une fois les deux corrections en place, c'est un chiffre a revoir, pas un bogue a chercher. |
| 2026-09-06 | v450 | Jacques | **Toujours pareil apres la v449.** Puis, de lui-meme, l'observation qui vaut toutes les analyses : « si j'active l'application a partir de **l'ecran d'accueil de mon iPhone**, ca fonctionne. Si je le fais a partir **du lien dans mon application Notes**, ca ne fonctionne pas. » Et sa question : « est-ce qu'on devrait se servir du **journal** pour voir ce qui se passe ? » | **Oui, et il avait raison plus tot que moi.** La memoire du projet porte cette phrase depuis le 2 septembre : « devant un defaut de voix rapporte depuis le telephone, demander le journal AVANT d'ecrire une ligne de code ». J'ai ecrit deux versions sans le demander. Les deux corrigeaient un defaut **reel** du code -- la v449 a bien trouve que le remede de la v448 etait sa propre cause, un `cancel()` sur un moteur au repos -- mais aucune ne s'attaquait a ce qu'il entend, parce que personne n'avait etabli **quel** silence c'etait. **Son observation tranche la question que le code ne pouvait pas trancher** : meme version des deux cotes, sonore depuis la tuile, muet depuis le lien. Ce n'est donc ni une version perimee ni la sequence -- c'est que Safari en **onglet** et l'app **installee** n'accordent pas les memes droits de parole. Le contre-piege est deja decrit dans la memoire du 2 septembre, et l'amorce de la v371 etait censee le couvrir : elle ne le couvre pas, ou plus. **Le journal etait inutilisable pour ca, et c'est repare.** Il gardait **20 lignes** -- une carte en produit six a huit, on ne voyait donc que les trois dernieres, jamais le moment ou ca bascule. Il horodatait a la **seconde**, la ou tout se joue en dizaines de millisecondes. Il fallait le **recopier a la main** depuis un iPhone. Et surtout il notait qu'on avait DEMANDE la parole, jamais si elle avait ete **accordee**. Desormais : **400 lignes**, l'ecart en ms depuis la ligne precedente, l'etat du moteur (`parle/file/PAUSE`) **avant et apres** chaque demande, une ligne **DEBUT** quand la voix commence pour de vrai, **FIN** ou **ERREUR** quand elle s'arrete, le **mode de lancement** (TUILE ou LIEN) en en-tete, et trois boutons : VOIR, **COPIER**, VIDER. Le journal survit a un redemarrage (localStorage) : iOS peut suspendre puis recharger l'app sans rien dire, et il serait vide au moment meme ou l'on va le lire. **Ce que la ligne APRES rend visible et qu'aucune version ne distinguait** : un enonce refuse sans le dire laisse le moteur AU REPOS juste apres `speak()` ; un enonce accepte puis avale le laisse a `parle` ou `file`. Deux causes, deux remedes opposes, un seul et meme silence. Verifie sur banc : les deux cas produisent bien deux traces differentes. ⚠️ **Une seule modification de comportement**, et elle suit son observation : l'amorce etait posee `once` -- un seul geste dans toute la vie de la page, sur l'hypothese ecrite en commentaire que « le droit, une fois accorde, vaut pour toute la page ». C'est cette hypothese que la tuile et le lien contredisent. **Chaque** geste rearme desormais. |
| 2026-09-06 | v451-v452 | Jacques | « Dans l'administration, pour la voix francaise du mode Ecoute, j'ai **Amelie ou Thomas**. » Puis il a fourni **le premier journal reel de ce defaut**, depuis Chrome sur son portable. | **Le journal a montre autre chose que ce que je cherchais depuis trois versions.** Extrait : `ENONCE fraise \| voix Google francais (fr-FR, DISTANTE)` / `APRES \| moteur parle/-/-` / `BLOQUE \| aucune fin apres 5765 ms` -- **six etapes de suite**, de cinq a dix secondes chacune, puis enfin `DEBUT` apres **2 334 ms** d'attente. **(1) La voix distante, et c'est NOUS qui l'avions choisie.** `voiceQualityScore` accordait **+3** a une voix `localService === false`, au motif qu'une voix distante est presque toujours neurale. Vrai, et sans importance a cote du reste : elle doit **aller chercher son audio sur un serveur**, et quand la requete traine, l'enonce ne sort pas. Une voix qui ne parle pas est pire que n'importe quelle voix qui parle. Le bonus devient un **malus de 100** : une voix distante n'est retenue que s'il n'existe **aucune** voix locale pour la langue. Sur Android les voix Google sont locales, elles ne sont pas touchees. **(2) La sonde s'effacait devant le cas le plus long.** Elle rendait la main des que le moteur se disait occupe -- « il travaille, laissons-le ». Or c'est exactement l'autre panne : le moteur passe a « parle » a l'appel et n'en sort jamais. Elle rend desormais **deux verdicts** : moteur AU REPOS = `MUET`, enonce refuse sans le dire, **on n'annule rien** (lecon de la v449) ; moteur OCCUPE = `ENLISE` apres 3 500 ms, et **la cancel() est legitime ET necessaire**, il y a vraiment quelque chose a retirer. Le seuil sort du journal lui-meme -- 2 334 ms pour un demarrage reel, donc on attend nettement plus avant de declarer mort. **(3) Le blocage se propageait.** Le chien de garde avancait en laissant l'enonce mort dans le moteur : l'etape suivante se mettait **en file derriere un mort**, ce que le journal montre noir sur blanc (`ENONCE petit ... moteur parle/-/-` puis `APRES : parle/file`). Il libere maintenant le moteur avant d'avancer. Verifie sur banc, deux moteurs simules : enlise -> `ENLISE` a 3 514 ms au lieu du chien a 5 765 ms, etape suivante repartant « au repos » ; refusant -> `MUET` a 814 ms et **cancel() appele zero fois**. ⚠️ **Ce que ce journal ne dit pas, et il faut le dire** : il vient du **portable**, pas de l'iPhone. Le defaut du lien des Notes n'est **pas** etabli par ces lignes -- une voix distante n'existe pas sur iPhone, toutes les voix d'Apple y sont locales. Amelie est fr-CA, Thomas fr-FR, et le classement ne favorise la variante standard que pour l'allemand et l'anglais : pour le francais c'est l'ordre alphabetique qui tranche. Le journal ecrit maintenant `Amelie (fr-CA, locale)` au lieu de `Amelie`, et un fichier qui bloque note son `readyState`, son `networkState` et sa position -- **trois fichiers allemands ont bloque dans ce meme journal** et rien ne dit encore s'ils telechargeaient ou s'ils etaient arretes. |
| 2026-09-06 | v453 | Jacques | **Le journal de l'iPhone**, depuis le lien des Notes -- celui qui manquait depuis le debut. | **Une ligne que personne n'avait regardee, et c'est la premiere de la seance :** `AMORCE (amorce) \| droit de parler demande dans le geste, moteur -/-/-`. Ce `-/-/-` est releve **apres** l'appel a `speak()`. Un moteur qui accepte un enonce le met en file : il devrait afficher `parle` ou `file`. Il est **au repos**. **L'amorce elle-meme n'a donc jamais ete mise en file** -- a un instant ou l'on est dans le geste de l'utilisateur et ou **aucun fichier audio n'a encore joue**. **Ce que ca elimine, et c'est le plus utile** : ni la session sonore de l'element `<audio>` (rien n'avait joue), ni le geste depense ailleurs (on est dedans). Les deux pistes suivies depuis la **v371**, et encore par les v448 et v449, visaient a cote. **Ce qui reste** : WebKit laisse tomber un enonce dont le texte ne contient **rien a prononcer**. Le notre etait **une espace**. Si c'est cela, l'amorce est **inerte depuis le premier jour**, et tout s'explique d'un coup -- l'app installee n'exige pas de geste et parle ; l'onglet Safari l'exige, ne l'obtient jamais, se tait. C'est mot pour mot l'ecart entre sa tuile et le lien de ses notes. L'amorce prononce desormais une **vraie lettre**, volume zero, vitesse maximale : inaudible, mais ce n'est plus « rien ». ⚠️ **Et on verifie au lieu de supposer.** Le journal notait qu'on avait DEMANDE le droit de parler, jamais s'il avait ete **accorde** -- la meme cecite a coute deux versions. L'amorce porte maintenant ses propres evenements : `AMORCE-OK` (elle a reellement parle), `AMORCE-FIN`, `AMORCE-ERR` avec le nom de l'erreur, et `AMORCE-250` pour l'etat du moteur un tour plus tard. **Si `AMORCE-OK` n'apparait pas, l'hypothese est fausse** et il faudra chercher ailleurs -- mais on le saura au lieu de le deduire. **Ce que le meme journal confirme par ailleurs** : la v452 a redresse le choix de la voix -- `Thomas (fr-FR, locale)` et non plus une voix distante, **aucun `ENLISE`**, tous les refus sont des `MUET` moteur au repos, et **les six fichiers allemands jouent sans un seul `BLOQUE`**. Le defaut du portable et celui de l'iPhone etaient bien **deux defauts differents**, ce qu'aucune oreille ne pouvait distinguer. |
| 2026-09-06 | v454 | Jacques | Second journal iPhone (v453), puis **la phrase qui a tout retourne** : « en passant, quand je pesais sur pause et que la voix revenait, ce n'etait pas la voix de **Thomas**, c'etait **la voix de la femme**. » | **Mon hypothese de la v453 est fausse, et le journal le dit sans detour.** L'amorce prononce desormais un texte reel : elle est **toujours** laissee tomber -- pas de `AMORCE-OK`, pas de `AMORCE-ERR`, moteur au repos encore 250 ms plus tard. Le contenu du texte n'y etait pour rien. **Et sa remarque designe la vraie piste** : ce qui a parle n'etait **pas la voix que nous assignons**. Sur iOS, `getVoices()` liste des voix qui ne sont pas toutes reellement installees ; en assigner une absente fait **disparaitre l'enonce sans erreur** -- exactement ce que les deux journaux montrent (`moteur au repos`, ni `start`, ni `end`, ni `error`). Ce que je cherchais depuis la v371 -- le droit de parler hors geste -- n'etait pas le sujet. **Le remede ne demande pas de savoir quelle voix est mauvaise** : sur un verdict `MUET`, l'etape est refaite **une fois sans imposer la voix**, en ne posant que la langue. Si elle parle alors, la lecon est **retenue pour la seance** (`VOIX-MORTE`) et les etapes suivantes ne repayent pas la seconde et demie de la sonde. **Mesure sur banc**, moteur simulant l'iPhone (tout enonce a voix imposee est laisse tomber sans un mot) : avant **0 etape francaise sur 4** ; avec la retentative **4 sur 4** mais 9 552 ms pour deux cartes ; avec la memoire **4 sur 4 en 4 117 ms**, seule la premiere etape paye. Temoin sur un moteur normal : 4 sur 4, aucun `SANS-VOIX`, aucun `VOIX-MORTE`. **Trois autres choses des memes journaux.** (1) L'amorce n'etait accrochee qu'a `pointerdown` -- or **WebKit n'accorde pas son activation utilisateur sur pointerdown/touchstart**, il l'accorde sur `touchend` et `click`. Les trois sont accroches, chacun se nomme dans le journal, `AMORCE-OK` dira lequel obtient le droit. (2) `syntheseAmorcee` ne disait que « on a appele speak() une fois », ce qui ne prouve rien : on s'arrete maintenant sur `onstart`, seule preuve qui vaille. (3) **Le bouton d'essai des Reglages appelait `cancel()` sans condition** -- il pouvait donc se rendre muet lui-meme (lecon de la v449, cette ligne l'ignorait encore). Repare, et il ecrit au journal : c'est le **seul enonce de l'app qui parte directement d'un clic**, donc s'il se tait aussi, la question du geste ne se pose plus. ⚠️ **La lecon de methode, et elle a coute six versions** : j'ai enchaine v448, v449, v453 sur des hypotheses tirees du code, toutes plausibles, toutes fausses. Ce sont **deux observations de Jacques** qui ont tranche -- « tuile oui, lien non », puis « ce n'etait pas Thomas ». Un defaut de son ne se lit pas dans le code : il se mesure sur l'appareil, ou il s'entend. |
| 2026-09-06 | v454 (confirmation) | Jacques | « **Oui, maintenant ca fonctionne.** Je n'ai pas change la voix, j'ai garde comme c'etait -- et **c'est la voix de Thomas** que j'entends. » | **Regle en v454, apres six versions.** Mais quelque chose ne colle pas avec l'explication que j'ai retenue, et il vaut mieux l'ecrire que de la laisser passer : **il entend Thomas**. Or la retentative « sans voix imposee » fait parler la voix **par defaut** du systeme -- si c'etait elle qui avait debloque la situation, il entendrait la voix de femme, comme la derniere fois. **L'autre changement de la v454 devient donc le candidat principal** : l'amorce n'etait accrochee qu'a `pointerdown`, et WebKit n'accorde pas son activation utilisateur sur `pointerdown`/`touchstart` -- il l'accorde sur `touchend` et `click`. Les trois sont accroches depuis la v454. Si c'est cela, la piste d'origine (le droit de parler hors geste, v371) etait la **bonne depuis le debut**, et elle echouait sur un detail d'implementation : le mauvais evenement. ⚠️ **Ce qui reste a etablir, et pourquoi ca compte** : la v454 porte DEUX corrections qui peuvent chacune expliquer le retour du son. Tant qu'on ne sait pas laquelle a agi, on ne sait pas laquelle on a le droit de retirer ni laquelle il faudra defendre a la prochaine regression. Le journal tranche en trois lignes : `AMORCE-OK` nommant `click` ou `touchend` = c'est le geste ; `SANS-VOIX` puis `VOIX-MORTE` = c'est la voix. **Journal demande.** ⚠️ **La lecon de methode, et elle a coute six versions** : v448, v449 et v453 ont toutes corrige un defaut **reel** du code, sur des hypotheses plausibles tirees de la lecture -- et aucune n'a touche le probleme. Ce sont **deux observations de Jacques** qui ont tranche : « tuile oui, lien non », puis « ce n'etait pas Thomas ». La memoire du projet portait deja la regle depuis le 2 septembre -- demander le journal AVANT d'ecrire du code. Je ne l'ai pas suivie. |
| 2026-09-06 | v455 | Jacques | Journal complet de l'iPhone en v454, puis : « j'ai change pour la voix d'**Amelie**, ca fonctionne aussi. Mais **je ne suis pas certain que ce soit la voix d'Aurora** pour l'allemand. » | **La cause est etablie, et le journal la porte en trois lignes consecutives, sur le meme toucher, a 74 ms d'intervalle** : `AMORCE sur pointerdown -> moteur -/-/-` ; `AMORCE sur touchend -> moteur parle` ; `AMORCE-OK : l'amorce a REELLEMENT parle par touchend`. Apres cette ligne, **toutes** les etapes francaises parlent (`DEBUT` entre 11 et 22 ms), **sur deux voix differentes** puisqu'il a change de Thomas a Amelie en cours de seance. **WebKit n'accorde pas son activation utilisateur sur `pointerdown`/`touchstart`** -- il l'accorde sur `touchend` et `click`. L'amorce de la v371 n'etait accrochee qu'a `pointerdown` : **la piste etait juste depuis le debut**, et elle echouait sur le choix de l'evenement, que rien dans le code ne trahissait. **Ce qu'on retire du coup** : la v454 portait deux corrections, on sait maintenant que l'autre n'a pas agi -- l'hypothese de la voix « listee mais pas installee » est **fausse**, Thomas parle et le bouton d'essai confirme Amelie. La retentative sans voix imposee reste comme filet, **une seule fois par etape** ; la memoire de seance est **retiree**, car elle abandonnait en silence le choix de voix de l'utilisateur pour toute la seance sur la foi d'un seul verdict passager. **Sa seconde question, verifiee cote serveur** : oui, c'est bien Aurora. Le journal ne montre que des lignes `FICHIER` pour l'allemand -- aucun `BASCULE`, aucun `SYNTHESE`, aucun `IGNORE` : **tout l'allemand vient des fichiers**, pas de la voix du telephone. Et les fichiers servis portent tous la date du **4 septembre 2026, 16:39 GMT**, soit le depot de la v407. Controle pousse plus loin, parce qu'un doute merite mieux qu'une date : six mp3 tires de son propre journal et de niveaux **B1 et C1** (`der Cousin`, `die Behauptung` -- des mots qui **n'avaient aucun fichier avant la v407**) repondent tous **200**, avec **six ETags distincts**. Deux d'entre eux ont exactement la meme taille en octets, ce qui m'a fait douter une minute : c'est une coincidence de debit constant, les empreintes different. `firebase.json` ne contient **aucune reecriture**, donc un fichier absent renverrait 404 et non un substitut. ⚠️ **La lecon de methode, et elle a coute six versions** : v448, v449 et v453 corrigeaient toutes un defaut **reel**, sur des hypotheses plausibles tirees de la lecture du code, et **aucune n'a touche le probleme**. Ce sont trois observations de Jacques qui ont tranche -- « tuile oui, lien non », « ce n'etait pas Thomas », et le journal lui-meme. La memoire du projet portait deja la regle depuis le 2 septembre : demander le journal **avant** d'ecrire une ligne de code. Un defaut audio sur iPhone offre toujours une hypothese plausible dans le code -- c'est precisement ce qui rend l'exercice dangereux. |
| 2026-09-06 | v456 | Jacques | Une fois la voix francaise revenue : « **depuis la tuile de l'ecran d'accueil, tout est normal.** Depuis le lien, ca fonctionne, mais **sur la phrase en allemand le niveau sonore est plus bas au debut et remonte a peu pres au milieu**. » | **Le dernier defaut de la serie, et il est enfin circonscrit** : l'onglet et non la tuile, la phrase et non le mot. C'est l'attenuation d'iOS qui n'a pas fini de se relacher quand le fichier demarre et qui cesse **en cours de lecture** -- une phrase longue traverse la transition, un mot court finit avant. Le souffle existe depuis la v449 et vaut **280 ms** ; le journal montre qu'il est bien applique (281 ms entre la ligne `FIN` et le `FICHIER` suivant). Il suffit dans l'app installee, pas dans l'onglet. **280 -> 700 ms, mais seulement dans l'onglet** : faire payer ce delai a l'app installee ajouterait un demi-silence par carte a quelqu'un qui n'a pas le defaut -- et c'est de la que Jacques revise le plus souvent. `estAppInstallee()` est extrait de `modeLancement()`. ⚠️ **Ce chiffre est empirique et le commentaire le dit** : aucun evenement ne signale « la session est relachee ». S'il en reste quelque chose a l'oreille, le seul geste est de l'augmenter, et **l'ecart reel se lit dans le journal**, colonne des millisecondes, entre `FIN` et le `FICHIER` qui suit. C'est la premiere fois de cette serie qu'on peut regler un chiffre en le mesurant au lieu de le deviner. |
| 2026-09-06 | v457 | Jacques | A 700 ms : « **j'entends toujours l'augmentation du niveau sonore au milieu de la phrase allemande. Peut-etre un peu moins.** » | « Un peu moins » dit que **la direction est bonne et la quantite insuffisante** -- c'est un retour plus utile qu'un oui ou un non. Son « au milieu » situe la fin de l'attenuation vers **1,5 a 2 s** apres la fin de l'enonce francais : 700 ms n'en couvraient que la moitie. **700 -> 1600 ms, toujours dans l'onglet seulement** ; l'app installee reste a 280 ms, elle n'a pas le defaut et ne doit pas payer le remede. **C'est un vrai silence et il s'entendra** -- il tombe au moins la ou il gene le moins, entre la traduction francaise et la phrase allemande. **Le souffle s'ecrit desormais au journal** (ligne `SOUFFLE` : valeur appliquee, contexte, cible) : c'est le seul chiffre de toute cette serie qu'on puisse regler **en le mesurant** plutot qu'en le devinant, encore faut-il pouvoir le lire. ⚠️ **La piste suivante est ecrite dans le fichier, pas faite.** `relacherLecteur()` a ete ajoute en v448 sur une theorie depuis **dementie** (on croyait que l'element retenant la session attenuait la synthese ; la vraie cause du francais muet etait l'amorce sur `pointerdown`). Or relacher l'element oblige a **rouvrir la session sonore a chaque fichier**, et c'est precisement a cette reouverture qu'iOS attenue. Le garder charge pendant la sequence pourrait supprimer l'attenuation et **rendre inutile le silence de 1,6 s**. **Pas fait dans la meme version, expres** : le silence est sur, il ne peut rien casser ; l'autre changement pourrait faire revenir le francais muet. Les enchainer rendrait le journal illisible -- c'est exactement l'erreur de la v454, qui portait deux corrections et ne disait pas laquelle avait agi. |
| 2026-09-06 | v457 (confirmation) | Jacques | « **Ca fonctionne.** » | **Le son du mode Ecoute est regle, depuis le lien comme depuis la tuile.** Fin d'une serie de dix versions en une journee (v448 a v457). **Les deux causes reelles, pour memoire, et aucune des deux n'etait celle que je cherchais** : (1) l'amorce de la synthese etait accrochee a `pointerdown`, or **WebKit n'accorde son activation utilisateur que sur `touchend` et `click`** -- d'ou le francais muet dans l'onglet et sonore dans l'app installee ; (2) iOS **attenue** le fichier allemand pendant que la session de la synthese se relache, et cesse de l'attenuer en cours de lecture -- d'ou le volume qui monte au milieu de la phrase. Corrige par un silence de **1,6 s dans l'onglet** seulement (280 ms dans la tuile, qui n'a pas le defaut). ⚠️ **Ce qui reste ouvert, et assume** : ce silence de 1,6 s **s'entend**, et il pourrait etre inutile -- `relacherLecteur()` oblige a rouvrir la session sonore a chaque fichier, ce qui est precisement le moment ou iOS attenue. La piste est ecrite dans `index.html`, a cote de la fonction, **pas faite** : elle pourrait faire revenir le francais muet, et on ne touche pas a ce qui marche sans une raison et un journal. Second point ouvert : le `-14 LUFS` derriere `VOLUME_SYNTHESE = 0,5` a ete mesure sur le corpus de **Nadja**, pas sur celui d'Aurora -- c'est probablement la que se trouve le « mot francais plus bas que le reste » signale plus tot dans la journee. |
| 2026-09-06 | v458 | Un usager, via Jacques | **Demande, pas defaut.** Sur le verso allemand d'une carte : entendre **le singulier avec son article PUIS le pluriel** enchaines, plutot que d'avoir a toucher le haut-parleur du pluriel. Et : **faut-il aussi dire la phrase d'exemple ?** « La personne peut la lire, mais je pense que de l'entendre, ca aiderait la retention. » Puis : « si c'est une bonne idee, est-ce qu'on devrait mettre dans la configuration qui peut l'enlever ou le remettre ? » | **Releve avant de repondre, et il change la reponse.** (1) **La moitie de la demande existe deja** : `flipCard()` appelle `speakWord()`, donc le singulier avec son article se dit **automatiquement** au retournement. Ce qui manque, c'est l'enchainement du pluriel. (2) **Aucun credit de generation n'est necessaire** : `audio/manifest.py` genere deja `"die " + pluriel` (source `nomen.pluriel`, ajoute a la demande de Kirsty) **et** la phrase d'exemple de chaque nom. Verifie cote serveur sur six fichiers (`der Vater` / `die Vaeter` / `Mein Vater arbeitet viel.` et le trio de `die Mutter`) : tous **200**, tous dans la voix d'Aurora. (3) **Couverture** : 3 396 noms sur 4 206 ont un pluriel (810 n'en ont pas -- massifs et indenombrables), et **4 206 sur 4 206 ont une phrase d'exemple**. **Mon avis pedagogique.** Le pluriel : **oui, sans hesiter**, et c'est exactement l'argument qui justifie deja de dire l'article -- un nom allemand ne s'apprend pas sans son genre NI son pluriel, les deux sont imprevisibles et doivent etre stockes avec le mot. Surtout, **la valeur est dans le contraste**, et un contraste n'existe que si les deux sont **adjacents** : `der Vater / die Vaeter`, l'inflexion s'entend ; lue, c'est un trema qu'on survole ; separee par un appui sur un bouton, la paire ne se forme jamais. La phrase : **l'intuition est juste sur la valeur, mais le cout n'est pas le meme** -- elle double a peu pres la duree, et le retournement est le moment du **verdict** sur un essai de rappel ; un verdict doit etre court. Le mode Ecoute fait deja mot + phrase, sans les mains. ⚠️ **Sur le reglage** : un seul, et **ordonne**, pas deux cases a cocher -- deux cases font quatre etats dont un absurde (la phrase sans le pluriel). **SUITE DE L'ECHANGE.** Jacques ajoute deux choses. (a) Reprendre le **surlignage du mode Ecoute** : l'article et le mot s'eclairent pendant qu'on les dit, puis le pluriel s'eclaire a son tour. **Bonne idee, et elle fait plus que decorer** -- elle aligne DANS LE TEMPS le son et la forme ecrite, ce qui est exactement ce qui manque quand on lit `die Vaeter` en silence. Une adaptation s'impose : en mode Ecoute les lignes inactives tombent a **32 %** d'opacite, ce qui convient a un ecran d'ecoute passive ; le verso d'une carte est une surface de **lecture** ou l'on doit voir l'ensemble pour se juger -- il faut relever la ligne active sans ecraser les autres. (b) Son reflexe : **ne pas dire le pluriel quand il est identique au singulier**. ⚠️ **Le comptage le contredit pour 430 mots sur 451.** 451 noms ont une forme de pluriel identique -- mais **430 d'entre eux changent d'ARTICLE** (`der Onkel -> die Onkel`, `das Maedchen -> die Maedchen`) : le pluriel S'ENTEND, il est simplement porte par l'article seul, et **ce sont precisement les cas que l'apprenant rate** en inventant une terminaison. Se taire la enseignerait implicitement « pluriel = le mot change ». **C'est exactement le raisonnement de la v445** : la serie des connecteurs a du inclure les familles qui ne changent RIEN (*und*/*oder*), sinon elle aurait enseigne « connecteur = inversion ». Seuls **21** noms sont identiques a l'oreille, article compris (`die Eltern`, `die Geschwister`, `die Nudeln` -- des pluralia tantum) : ceux-la, se taire ne coute rien. **La regle doit porter sur ce qui S'ENTEND, pas sur la forme ecrite.** (c) Sur l'option pour la phrase : la phrase est **deja affichee au verso avec son propre haut-parleur** (un seul appui), et le mode Ecoute couvre le besoin mains libres. Recommandation : **pas de reglage pour l'instant** -- on l'ajoutera si une deuxieme personne le demande, et on saura alors ce qu'elle veut vraiment. **FAIT EN v458, ET DEUX DECISIONS DE JACQUES CONTRE MON AVIS, TOUTES DEUX SUIVIES.** (1) **Le pluriel se dit meme quand il est identique**, y compris pour les 21 mots ou rien ne change a l'oreille : « ca integre pour l'etudiant que c'est un pluriel pareil », et « on est aussi consistant pour l'application ». Il a raison sur les deux points -- entendre deux fois la meme forme APPREND que ce mot ne change pas, et une regle sans exception se tient partout. (2) **Le reglage pour la phrase existe**, defaut NON, alors que je proposais de ne pas l'ajouter avant qu'une deuxieme personne le demande. Son exigence : « il faut que ce soit parfaitement clair, qu'est-ce qu'on est en train de faire » -- l'etiquette dit donc aussi ce que le reglage **coute** (deux a trois secondes par carte) et que sans lui la phrase reste affichee avec son haut-parleur. Quatre langues. **Le surlignage est adapte, pas copie** : attenuation a **55 %** et non 32 %, et **seulement pendant la chaine** -- une carte a une seule etape n'est pas attenuee du tout, l'ancien comportement reste identique. **Cinq scenarios au banc**, dont les deux qui pouvaient casser en silence : une carte **sans pluriel affiche** (un verbe apres un nom) ne dit **pas** le pluriel de la carte precedente -- `texteAudioPluriel` n'est remis a zero par aucune des six branches qui ne le posent pas, defaut latent contourne en lisant l'etat REEL du DOM ; et **revenir au recto en cours de chaine** ne laisse passer aucune etape en retard. **Corrige au passage** : le commentaire de `speakPlural()` affirmait que « les pluriels ne sont pas encore dans le manifeste audio » -- faux, ils y sont, et verifie cote serveur. |
| 2026-09-06 | v459-v460 | Jacques | « **Visuellement, ca ne fonctionne pas.** Il faudrait que lorsqu'on arrive au verso, le mot au singulier soit **plus pale**, puis qu'au moment ou c'est dit il devienne **plus fonce** ; que pendant ce temps le pluriel soit plus pale, et qu'il fonce quand on le nomme. » Puis, spontanement : « je ne voyais jamais le pluriel en pale » -- **et il s'est corrige lui-meme apres verification** : « non non, le pluriel etait ok. » | **Deux causes, et je me suis trompe sur la seconde avant qu'il ne me detrompe.** **(1) Le singulier n'etait JAMAIS pale** : il est la premiere etape de la chaine, donc il passait a pleine encre du premier instant. La seule chose qui bougeait a l'ecran etait la petite ligne du pluriel. Le verso s'ouvre desormais **attenue**, et chaque ligne s'eclaire au moment ou on la dit, le singulier compris -- c'est exactement ce qu'il decrivait. **(2) Ma premiere explication du reste etait « 55 % ne se voit pas », et j'ai baisse a 35 %. Fausse** : il a verifie et le pluriel etait bien visible en pale. **Le chiffre est revenu a 55 %** -- changer un reglage qu'il venait de valider, sur une premisse qu'il venait de demolir, aurait ete la faute meme que cette journee a payee dix fois. **La vraie seconde cause n'a rien a voir avec l'opacite** : la bascule de la carte dure **550 ms** (`transition: transform .55s` sur `.flashcard`), et j'eclairais a **220 ms** -- en plein retournement, quand la carte est encore **de profil** et que le verso n'est pas lisible. L'etat pale existait ; personne ne pouvait le voir. La lumiere attend maintenant que la carte soit posee. ⚠️ **Ce qui ne peut PAS attendre, c'est le son** : sur iOS l'element audio n'a le droit de jouer que dans le prolongement direct du geste. Le fichier part donc toujours immediatement -- c'est la **lumiere** qui se decale, jamais la voix. `DELAI_BASCULE` est une constante nommee avec la consigne de suivre le CSS : en dur, elle aurait cesse d'etre juste **en silence** le jour ou la duree de la transition change. |
| 2026-09-06 | (revue) | Jacques | **Demande de fond, pas un defaut.** « Il reste un mois d'abonnement, il faudrait optimiser l'utilisation. Repense a travers tout le projet avec une **approche pedagogique**, comme expert : ce qu'on a oublie, ce qui est mal structure, ce qu'on devrait ajouter ou regrouper. Et regarde aussi l'aspect **legal** : droits d'auteur sur le contenu, sur les sons, sur l'approche ; risque de plagiat ou d'elements sous licence. » | **Revue complete publiee** (artefact). **La question des credits a une reponse chiffree et inattendue** : le corpus allemand est **complet** (25 298 / 25 300), il n'y a rien a generer *dans ce que le manifeste regarde*. Le chantier est dans ce qu'il ne regarde pas -- `manifest.py` n'enumere ni `pruefung.json` ni `exercices.json`. Consequence : **toute l'epreuve d'ecoute de l'examen est lue par la voix robotique du telephone**, la seule epreuve ou le son EST la competence evaluee. Total de ce qui n'a aucune voix : **75 354 caracteres = 37 677 credits Flash, soit 31 % d'un mois**. Hoeren seul : 4 359. **Pedagogie -- le manque structurel** : l'app n'exige **jamais** de produire une phrase. Tout est reconnaissance (choisir parmi quatre) ou reassemblage (blocs) -- et les blocs **donnent les mots**. Remede a cout de contenu nul : la meme phrase, mais **tapee**, les blocs reveles apres un premier essai. Autres trous : **rien entre le mot entendu et l'examen** (un exercice « ecoute la phrase » se batirait sur de l'audio deja produit) ; **aucune production orale** alors que l'examen en comporte une ; **`uk` absent de `LANGUE_TAG` et `VOICE_PREFEREES`** ; et le risque de **decouvrabilite** (40 ecrans, 40 jeux, 17 formats -- le precedent de la v409, 45 exercices sans aucune tuile). Point fort confirme et mesure : la couverture grammaticale vise les vraies difficultes (cas 50, relatives 211, ordre des mots 160, connecteurs 298). ⚠️ **Juridique -- six points, dont deux a traiter.** (1) Les **listes officielles d'examen** (Goethe A2/B1, DTZ) ont servi a choisir du vocabulaire : `manquants.txt` 489 mots, `palier1` 476, `palier2` 641. Un mot ne s'approprie pas, mais une liste peut relever du **droit *sui generis* des bases de donnees** (UE, 15 ans) -- et le depot EUIPO rend ce droit pertinent. **Ce qui protege deja** : ni les PDF ni les `.txt` ne sont suivis par git, et le vocabulaire livre est un **sur-ensemble** reorganise avec ses propres traductions et phrases. A ne jamais assouplir. (2) **24 videos publiees, aucune provenance ecrite nulle part** -- le seul point que personne ne pourra reconstituer plus tard. (3) `dict/` redistribue 24 Mo de WikDict **sans le texte de la licence** CC BY-SA (l'attribution a l'ecran, elle, est faite et bien faite). (4) Trois **marques** nommees sans clause de non-affiliation. (5) **Pas de conditions d'utilisation**, seulement une politique de confidentialite. (6) Voix et contenu d'examen : sous controle. |
| 2026-09-06 | v476 | Une usagere, via Jacques | « Dans la configuration, pour le son de la phrase : **par defaut on mettrait pluriel et singulier, mais il faudrait pouvoir enlever le son sur le pluriel, ou sur le singulier.** » | **Elle a raison, et elle designe une asymetrie que je n'avais pas vue.** Le reglage de la v458 ne savait qu'AJOUTER une etape (la phrase), jamais en retirer -- c'etait la moitie d'une idee. Or les besoins reels vont dans les deux sens : quelqu'un qui connait deja ses genres n'a pas besoin d'entendre l'article a chaque carte, et quelqu'un qui travaille ses pluriels veut peut-etre le **pluriel seul**. La carte de reglages devient donc **« Ce que la carte prononce »**, avec trois interrupteurs : le mot avec son article, le pluriel, la phrase d'exemple. **Les defauts ne changent pas** -- mot et pluriel oui, phrase non : le retournement est le moment du verdict, et un verdict doit rester court. ⚠️ **Ce qu'on retire n'est jamais perdu**, et le texte du reglage le dit : la forme retiree reste **affichee**, et son haut-parleur repond toujours au doigt. Un reglage de son qui ferait disparaitre une information serait un piege. Detail d'ecriture : chaque bouton affiche son etat **en toutes lettres** (✓ / — et « non ») plutot qu'une coche seule -- devant un bouton, on ne doit pas avoir a se demander si l'on regarde l'etat actuel ou l'action qu'il declenche. Quatre langues. |
| 2026-09-06 | (decision) | Jacques | « **Est-ce que ca cause probleme ?** » -- a propos du detail par liste (`a2`/`b1`/`dtz`) encore publie mot par mot dans les JSON. Puis : « **ok on la fait avant la mise en vente**. » | **Chiffre plutot qu'impression.** Ce qui est reconstituable depuis les fichiers publics : **1 047** marques `a2`, **2 917** `b1`, **2 529** `dtz` -- soit environ **44 %, 34 % et 38 %** de chaque liste officielle. C'est une « partie substantielle » au sens du droit europeen des bases de donnees, et le depot EUIPO place le projet dans cette juridiction. **Ce qui rend le risque modeste aujourd'hui** : ces listes sont publiees gratuitement par le Goethe-Institut *pour que les enseignants concoivent des cours*, ce qui est exactement l'usage ; et ce qui est publie n'est pas la liste mais son **intersection** avec un vocabulaire qui est une selection propre. **Ce qui change tout, c'est la vente** : douze camarades de cours, personne ne regarde ; un produit vendu qui republie un tiers d'une liste protegee, c'est une autre conversation. ⚠️ **Et j'avais propose un mauvais remede** : « descendre le detail dans `examens/` » aurait sorti une donnee du controle de version pour la laisser sur un seul disque. Inutile -- la marque est **calculee**, c'est l'intersection entre `examens/*.txt` et le vocabulaire du cours. Il suffira de remplacer le tableau par `true` dans les fichiers publies ; un script de `tests/` recalculera le detail quand il faudra mesurer la couverture. Rien ne se perd, rien ne sort du depot. **Decision : avant la mise en vente, pas maintenant.** Consigne a trois endroits pour ne pas dependre de cette conversation : un commentaire dans `index.html` la ou le rang 14 est construit, la memoire de preparation au Play Store, et cette ligne. |
| 2026-09-06 | v477 | Jacques | « Dans l'administration, il y a une erreur : **ecriture refusee, invalid-argument**. » Puis le message complet, copie du tableau de bord. | **Le diagnostic pose en v396-v400 a fait exactement son travail** : il a nomme la cause au lieu de la faire deviner -- `Unsupported field value: undefined (found in field streak)`, et sa propre ligne `undefined trouve : .streak`. **La cause**, dans `getStreakCount()` : `return streak ? streak.count : 0` se protege de `null` mais **pas d'un objet de serie sans `count`** -- auquel cas il rend `undefined`. Et Firestore rejette **le document entier** pour une seule valeur undefined : la progression de Jacques ne se sauvegardait plus du tout dans le cloud, pour un champ de compteur. Un objet sans `count` n'a rien de theorique : c'est ce que laisse un ancien format ou une ecriture interrompue. La fonction rend desormais **toujours un nombre fini**. ⚠️ **Et le meme accident ne doit plus pouvoir emporter tout le document.** Avant d'ecrire, les valeurs undefined sont retirees a tous les niveaux -- objets, sous-objets ET tableaux -- et les cles retirees sont **retenues puis affichees** dans le tableau de bord : les laisser disparaitre sans trace remplacerait une panne visible par une panne invisible, ce qui serait pire. L'ecriture se faisant avec `merge`, une valeur deja stockee survit a un calcul rate. **Deux pieges evites, tous deux trouves au banc et non par relecture** : les sentinelles Firestore (`serverTimestamp`) sont des objets opaques qu'il ne faut pas parcourir -- on ne descend que dans les objets nus ; et un `map` sur un tableau **laissait passer** l'element undefined, que Firestore refuse tout autant. ⚠️ **Ce que le diagnostic signale en plus, et qui n'est pas regle** : **45 695 champs** dans le document, pour un plafond d'index de **40 000**. La sauvegarde passe grace a l'exception posee en console lors du defaut precedent, mais le compte continue de monter -- et le mur suivant, la taille, est a 510 ko sur 1 024. A surveiller. |
| 2026-09-06 | v478 | Des usagers, via Jacques | « Avoir un endroit dans l'application, **facilement accessible**, ou on peut donner du feedback sur des erreurs rencontrees. Je pense que c'est une tres bonne suggestion. » | **Elle repare un desequilibre que ce journal illustre mieux que tout** : l'application demande beaucoup de retours et n'offrait aucun endroit pour en donner. Un testeur qui rencontrait un defaut devait ecrire a Jacques, hors de l'app, en se souvenant de ce qu'il faisait -- donc la plupart ne disaient rien, et les retours consignes ici viennent presque tous de la meme personne. ⚠️ **Le contexte est joint TOUT SEUL** : version, ecran, langue, et si l'app a ete ouverte par la tuile ou par un lien. C'est exactement ce qui a manque toute la journee pour diagnostiquer le son -- il a fallu deux echanges rien que pour etablir la version et le chemin d'ouverture. Personne ne pense a noter ca, et personne ne devrait avoir a le faire. **Deux contraintes techniques qui ont decide de la forme.** (1) **Une seule chaine, pas un tableau** : Firestore indexe chaque entree d'un tableau, et le document en compte deja **45 695** pour un plafond de 40 000 -- un index de plus par retour serait le prochain defaut. (2) **Dans le document de l'usager**, pas dans une collection separee : une collection demanderait une regle de securite de plus dans la console Firebase, et un envoi refuse en silence vaudrait moins qu'un stockage un peu moins elegant. Le texte est ecrit d'abord sur l'appareil, puis part avec la sauvegarde suivante : reseau absent, rien n'est perdu. Les retours s'affichent sous chaque testeur dans le tableau de bord. Quatre langues. |
| 2026-09-06 | v479-v480 | Jacques | **Commande de travail, suite de la revue.** « Commence par le Hören dans la voix d'Aurora, mais … je vais avoir **cent exercices** en tout … en fait, **quarante aussi pour C1**, donc ça va être équilibré. Ensuite tu continues avec **tout le reste de l'examen et les exercices**. Puis après ça, on va discuter pour les prochains points. » | **Hören : 40 → 120 exercices, 40 par niveau.** La répartition d'avant était déséquilibrée ; son correctif — quarante aussi pour C1 — la rend uniforme. Les 80 nouveaux sont passés par `ajouter_pruefung.py` : **0 refusé**. **120 fichiers produits en voix d'Aurora**, 11 555 crédits Flash, puis normalisés. ⚠️ **Deux vérifications ont changé le résultat, et aucune n'était dans la commande.** (1) Les fichiers sortaient d'ElevenLabs **3,5 dB trop bas** (−18,6 LUFS contre −14,7 pour le vocabulaire). Déposés bruts, les passages d'examen auraient sonné nettement plus faibles que le reste — sur **la seule épreuve où le son EST la compétence évaluée**. Après normalisation : −15,7, soit exactement ce que la règle prescrit pour un passage long (cible −14,50 au-delà de 2,5 s contre −13,67 à 2 s) — l'écart de 0,9 dB avec le vocabulaire est **voulu**, pas un défaut. (2) Chaque fichier brut a été archivé dans `audio/mp3_original/` **avant** normalisation : sans ça, une seconde passe repartirait du fichier déjà traité et empilerait les encodages. **Point resté ouvert depuis la v457 et refermé au passage** : le corpus d'Aurora **est** bien à −14,7 LUFS — `VOLUME_SYNTHESE = 0,5` n'est donc pas calibré sur un corpus disparu. **LE RESTE DE L'EXAMEN — et ce que le relévé a trouvé avant de dépenser un crédit.** Générer d'abord aurait produit **10 657 crédits de fichiers que rien ne joue** : Sprechen, Schreiben et Lesen n'avaient **aucun son du tout** — pas même celui du téléphone, aucun bouton nulle part. Les grammaires non plus : un exercice se terminait sur une phrase allemande juste qu'on pouvait **lire sans jamais l'entendre**, ce qui est la moitié manquante — « dem Mann » ne s'apprend pas seulement à l'œil. **La v480 pose donc le bouton d'abord**, un seul, sous le retour d'exercice, et **seulement après la réponse**. ⚠️ **Trois décisions pédagogiques qui tiennent le bouton debout, et qui ne sont pas des détails.** (a) **Jamais avant la réponse** : pour Lesen, entendre le texte avant de répondre transformerait une épreuve de **lecture** en épreuve d'écoute. (b) **Lesen dit le texte SEUL** : la question qui l'accompagne est rédigée dans la langue de l'usager, et une voix allemande en ferait du charabia. (c) **Sprechen dit la question de l'examinateur PUIS la réponse modèle** — dans un oral, les deux s'entendent, et c'est l'enchaînement qu'on apprend à reconnaître ; une épreuve d'expression orale sans modèle entendu manquait sa compétence exactement comme Hören manquait la sienne. **Aucune devinette** : trois cas seulement produisent une phrase (un `audioDe` posé par les données, des blocs remis dans l'ordre juste, ou un blanc rempli par la bonne forme) — un énoncé de type « Quel cas ? », rédigé en français, n'a **pas** de bouton. Mieux pas de bouton qu'un bouton qui déraille. **86 fichiers à produire, 10 657 crédits.** ⚠️ **Ce qui reste, et pourquoi il attend** : les **1 370 phrases des exercices de grammaire** coûtent **29 261 crédits** à elles seules — le solde du mois ne les porte pas après les 11 555 du Hören. Le bouton, lui, **est déjà en place pour elles** : le jour où les fichiers existent, rien ne sera à recoder, et d'ici là elles sortent par la voix du téléphone au lieu de se taire. |
| 2026-09-06 | v481-v483 | Jacques | **Commande de travail, la suite de la revue, « sans t'arrêter » :** exercice « écoute la phrase », la phrase à taper, la production orale, relévé des chemins d'accès. | ⚠️ **UN DES QUATRE ÉTAIT DÉJÀ FAIT, ET MA REVUE SE TROMPAIT.** « La phrase à taper » existe depuis longtemps : tuile **Écrire**, on lit le français, on tape l'allemand, la comparaison tolère accents et ponctuation, et **une phrase ratée au clavier est redonnée en tuiles** (`rattrapage`) sans que le ratage soit racheté. J'avais écrit dans la revue que « l'app n'exige jamais de produire une phrase » : c'est faux, et je le dis plutôt que de construire un doublon. **LE RELÉVÉ DES CHEMINS — `tests/chemins.py`, et il a trouvé trois trous.** Le vérificateur répondait à « la cible existe-t-elle ? », jamais à « peut-on y ARRIVER ? ». La différence avait déjà coûté la v409. Le script parcourt le graphe pour de bon — accueil, `onclick` (argument compris), `showScreen`, panneaux, actions, jeux — et a sorti **8 cibles sans aucun chemin**, en trois défauts. (1) **Les particules** : une leçon, **50 exercices**, un paquet de cartes. La seule entrée était le bouton « Retour » de la page d'explication, **elle-même inatteignable** : on n'y arrivait qu'en ouvrant les cartes depuis Expressions puis en revenant en arrière. Mot pour mot le défaut de la v409. Expressions ouvre désormais le panneau, dont ces cartes sont la troisième option — rien n'est perdu. (2) **Le génitif des relatives** (`dessen`, `deren`) : une leçon et **59 exercices**, dans un panneau que rien n'ouvrait ; passé dans « Pronoms », où l'on prend déjà les relatives. (3) **Deux panneaux morts** (`relativ`, `possessiv`) qui dupliquaient « Pronoms » : retirés. Du code mort qui ressemble à du code vivant est un piège — on serait allé corriger une leçon dans le panneau que personne ne voit. **Le contrôle entre dans `verifier.py`** : 98 cibles, 0 sans chemin, à chaque push. Les entrées hors clic (l'écran de configuration au premier lancement) sont déclarées **avec leur raison**, pour que cette liste ne devienne pas l'endroit où l'on fait taire le script. **« COMPRENDRE À L'OREILLE » (v482) — l'échelon qui manquait.** L'app faisait entendre des MOTS (la dictée) et faisait passer un EXAMEN d'écoute ; entre les deux, rien. Une phrase est dite, jamais écrite ; on choisit ce qu'elle veut dire ; elle s'affiche ensuite, et le bouton de la v480 la rejoue pendant qu'on la lit. **Aucun crédit** : 5 186 phrases d'exemple ont déjà leur fichier en voix d'Aurora et leur traduction (100 % fr/en, 96,5 % tr/uk). ⚠️ **Deux détails décident de la valeur de l'exercice.** Les **leurres viennent du même thème** — tirés au hasard dans tout le corpus, ils parlent d'autre chose et la bonne réponse se devine sans avoir rien compris, il suffit d'attraper un mot (les 80 thèmes ont tous au moins quatre phrases). Et les **réponses sont dans la langue de l'usager** : un turcophone qui doit choisir entre quatre phrases françaises ne fait plus un exercice d'écoute, il fait un exercice de français. ⚠️ **Pas d'adjectifs dans le vivier, délibérément** : ils existent sous **deux dispositions** — dans un thème la phrase allemande est au rang 3, dans le paquet autonome au rang 2, le rang 3 y portant le NIVEAU. Les confondre ferait lire « A1 » à voix haute comme une phrase, **sans la moindre erreur nulle part**. **« S'ENTENDRE LE DIRE » (v483) — la production orale.** Ce qui manquait n'était pas la consigne de parler : le mode Écoute fait déjà écouter puis répéter dans le silence. Ce qui manquait, c'est de **rendre la voix** — on n'entend pas son propre accent en parlant, on l'entend en se réécoutant. ⚠️ **Aucune note, et c'est un choix, pas une facilité** : faire juger la prononciation par une reconnaissance vocale est techniquement possible (`webkitSpeechRecognition` existe sur Safari) et pédagogiquement mauvais — ces moteurs sont entraînés sur des locuteurs natifs et refusent régulièrement une phrase correcte dite avec un accent français. Un « faux » injustifié, **sur la compétence où l'on est déjà le plus vulnérable**, décourage plus qu'il n'enseigne. ⚠️ **Rien ne sort de l'appareil** : pas de téléversement, pas de stockage, l'URL du blob est révoquée dès la phrase suivante. Le micro se relâche à l'arrêt, au changement de phrase, au retour **et quand la page passe en arrière-plan** — verrouiller le téléphone ne doit pas laisser le témoin d'enregistrement allumé. Trois refus possibles sont **nommés** plutôt que de laisser un bouton inerte. ⚠️ **À ESSAYER SUR L'IPHONE, DEPUIS LA TUILE** : `getUserMedia` a longtemps été refusé aux applications ajoutées à l'écran d'accueil, et c'est justement le chemin qu'il utilise. |
| 2026-09-07 | v484 | Jacques (par le bouton, **premiers retours arrivés par ce chemin**) | Trois retours envoyés depuis l'app : (1) le dictionnaire sort `Abwart` avant `Hausmeister` pour « concierge », alors qu'`Abwart` est un helvétisme ; (2) « la réponse être au Perfect » ; (3) « lorsque le mot est choisi, sa traduction devrait être ajoutée à la phrase française ». Puis, en les lisant : **le contexte joint ne dit pas où on était.** | ⚠️ **LE DÉFAUT ÉTAIT DANS L'OUTIL DE RETOUR LUI-MÊME, et c'est lui qu'on a réparé d'abord (v484).** La v478 promettait — et le texte de l'interface le promet toujours — que « l'écran où tu étais » est joint automatiquement. La ligne portait la date, la version, la langue et le mode de lancement. **Pas l'écran.** Les retours (2) et (3) sont inexploitables pour cette raison exacte : lequel des 1 682 exercices ? ⚠️ **L'ajouter naïvement n'aurait rien donné** : le formulaire vit dans `<section id="settings">`, donc l'écran actif à l'envoi est TOUJOURS `settings` — on aurait écrit « réglages » sur tous les retours, ce qui a l'air d'une information. On retient le dernier écran **quitté**. Et l'écran seul ne suffit pas : le contexte porte désormais le jeu, le numéro (7/28) et le début de la question ; sur une carte, le mode et le mot ; dans un panneau, son nom. **Outil de lecture** : `node tests/retours.js`, lancé au début de chaque session (consigne dans `CLAUDE.md`) — sinon un retour attend qu'on pense à ouvrir le tableau de bord. Clé de service en **lecture seule** (rôle « Lecteur Cloud Datastore ») : une écriture serait refusée par Google, pas par la prudence du code. **Reste à traiter** : (1) l'ordre du dictionnaire, (2) et (3) à re-signaler depuis l'app maintenant que le contexte suit. |
| 2026-09-07 | v485-v487 | Jacques | **Deux demandes.** (1) « Corrige le dictionnaire, Hausmeister avant Abwart, et pour tous les mots qui auraient un synonyme suisse ou autrichien. » (2) « Commence la traduction de l'application en persan. » | **(1) LE MOT SIGNALÉ N'EXISTAIT PAS DANS LE DICTIONNAIRE.** `Abwart` est absent ; ce qu'il a vu est `concierge → Concierge · Hausmeister · Hauswart`, où le terme suisse est **`Hauswart`** et où la tête est prise par l'emprunt `Concierge`. La demande tenait quand même, et 55 entrées étaient dans ce cas (janvier → Jänner, tomate → Paradeiser, bicyclette → Velo). ⚠️ **Trois règles automatiques essayées, toutes rejetées, mesures à l'appui.** Trier par la fréquence du mot allemand change la tête de **28 %** des 46 313 entrées et en casse une bonne part (`alène → Ort`, `aliénation → Wahnsinn`, `à la française → à la française`). Reléguer l'emprunt identique au mot cherché touche 778 entrées et donne `clown → Trottel`, `audit → kontrollieren`. La fréquence d'un mot allemand ne dit rien du **sens** qui correspond au mot français. ⚠️ **Les homographes sont le vrai piège** : `Stelze` (échasse), `Estrich` (chape), `Stiege` (vingtaine), `Finken` (pinsons), `Occasion` (aubaine) — les marquer « (AT) » aurait été une faute nouvelle. Hors liste, volontairement, avec le commentaire sur place. **Résultat (v485)** : liste vérifiée à la main, les mots régionaux passent à la fin **et portent leur zone** — `Hauswart (CH)`, `Jänner (AT)`. Rien n'est supprimé : les cacher priverait qui part vivre à Zurich du mot qu'il entendra tous les jours. Les données WikDict ne sont pas touchées, tout se joue au rendu. **(2) LE PERSAN S'ÉCRIT DE DROITE À GAUCHE, donc la mise en page passe AVANT la traduction (v486)** — sinon on produit 1 134 chaînes persanes dans une mise en page à l'envers. Sur 105 ko de CSS, **26 déclarations** seulement dépendent du sens de lecture : passées en propriétés logiques (`inset-inline-start`, `text-align:start`…), identiques en français, retournées par le navigateur en persan. Les centrages `left:50%` sont de la géométrie et n'ont pas été touchés. **Chaîne complète (v487)** : `i18n_dump.js` (évalue le bloc avec node, là où mon extracteur par expression régulière comptait 809 clés au lieu de 899), `cles_langue.py`, `fusion_langue.py` **qui relit ce qu'il vient d'écrire**. ⚠️ **La relecture a servi dès le premier lot** : le dernier bloc de langue se ferme sans virgule, l'outil a écrit un bloc `fa:` parfaitement formé **hors de I18N**, 1 150 lignes plus bas — `node --check` passait, `verifier.py` passait. **État : 109 clés sur 1 134.** Le drapeau reste hors du choisisseur jusqu'à 1 134/1 134 — la leçon ukrainienne (« si je clique sur le drapeau, tout est en anglais »). ⚠️ **DeepL ne traduit pas le persan** : la relecture croisée par traduction inverse ne servira pas ici. |
| 2026-09-07 | v486-v497 | Jacques | « Commence la traduction de l'application en langue persane », puis « continue ». | **TERMINÉ : 1 134 clés sur 1 134**, cinquième langue d'interface, drapeau ouvert dans les deux choisisseurs. ⚠️ **La mise en page est passée AVANT la traduction (v486)** — traduire d'abord aurait produit 1 134 chaînes persanes dans une mise en page à l'envers. Sur 105 ko de CSS, **26 déclarations** seulement dépendent du sens de lecture ; passées en propriétés logiques, identiques en français et retournées par le navigateur en persan. Vérifié dans un navigateur, dans les deux sens. ⚠️ **Cinq explications de grammaire ont dû être RÉÉCRITES, pas traduites** : « pas de -ment à ajouter » (le persan fait déjà pareil → c'est un appui, pas une difficulté), « jeder est singulier contrairement au français » (idem en persan), « man, le « on » français » (le persan n'a pas de « on »), « comme je/me/moi » (**le persan ne décline pas ses pronoms — c'est la plus grosse différence du chantier, et le français la cachait**), « comme le sujet vide de il pleut » (le persan supprime le sujet). Et **trois des quatre duos de connecteurs annonçaient un piège que le persan n'a pas** (wenn/ob, wenn/wann, aber/sondern, wissen/kennen) — als/wenn, lui, reste vrai. Une difficulté annoncée qui n'existe pas use la confiance dans toutes les autres. **Outils versionnés** : `i18n_dump.js`, `cles_langue.py`, `fusion_langue.py`, `fusion_grammaire.py`, `controle_i18n.py`, `contraste_i18n.py`. Les deux fusions **relisent ce qu'elles viennent d'écrire** — et ça a servi dès le premier lot (bloc `fa:` écrit HORS de I18N, que `node --check` et `verifier.py` laissaient passer). ⚠️ **RESTE À FAIRE : la relecture par un persanophone.** DeepL ne traduit pas le persan ; la mesure faite avec Google Cloud Translation (projet séparé `wortando-traduction`, coût réel 0 $) a montré que l'aller-retour **discrimine mal sur des chaînes d'interface** — 91 signalements dont 74 sur des chaînes de moins de 28 signes, et aucune vraie faute. Le registre (تو / شما, écrit / parlé) n'est vérifiable par aucune machine. |

---

## Comment m'en servir le moment venu

1. **Compléter la colonne « Qui »** avec les numéros de `cle-testeurs.txt`.
2. **Continuer à l'alimenter** : chaque nouveau retour, une ligne — date, qui, ce qui a été dit, ce qui a changé, numéro de version. Trois minutes sur le moment, contre des heures de reconstitution plus tard.
3. **Pour le formulaire Google**, ne pas recopier ce tableau : en tirer trois ou quatre exemples où l'enchaînement *retour → diagnostic → correction → version publiée* est net. Ce qui se démontre là n'est pas qu'on corrige des bogues, c'est qu'**un retour d'usager change le produit dans la semaine**. Les plus parlants :

   - **v225 — Regina.** Elle sortait de l'app pour consulter un dictionnaire. Le dictionnaire est entré dans l'app : 145 000 entrées, dans la barre de recherche qui existait déjà. Le retour nomme le moment où le produit perd la personne.
   - **v320.** Un exercice proposait une quatrième tuile étrangère à la question. La cause était structurelle — 77 verbes n'ont que trois formes distinctes au présent — et touchait **8 exercices sur 50**. Le symptôme signalé était plus petit que le défaut.
   - **v409 — Jacques.** « Je ne vois pas de tuile conjonction. » Il avait raison : l'écran d'explication, **45 exercices** et 18 cartes existaient depuis des mois, et **aucune tuile ne les portait**. On n'y arrivait qu'en appuyant sur « Retour » depuis un écran de passage. Aucun test automatique ne voit ça — seul un usager qui cherche quelque chose et ne le trouve pas.
   - **v408 puis v411 — Barbara.** Deux retours de la même personne, deux corrections publiées le même jour. (1) Des entrées de dictionnaire « qui ne sont pas des mots allemands » : son exemple était inexact, le défaut non — 732 **affixes** (`-heit`, `-bar`, `anti-`) retirés des quatre dictionnaires. (2) L'écran de recherche ne disait nulle part qu'on peut chercher **en français** : c'était écrit dans le texte gris du champ, qui s'efface à la première lettre. Le titre le dit maintenant.
   - **v410 — Jacques, demande et non défaut.** Il voulait l'exercice de son cahier : choisir entre *weil* et *obwohl*. Deux séries de 28 ont été écrites, et les connecteurs sont passés de 45 à 101 exercices. Utile pour montrer que le journal recueille aussi ce que les gens **veulent apprendre**, pas seulement ce qui casse.

⚠️ Ce que ce journal **ne remplace pas** : le compteur des 12 testeurs pendant 14 jours consécutifs se mesure uniquement dans la Play Console, sur la piste de test fermé. Rien de ce qui précède n'y compte. Ce fichier ne sert qu'aux questions rédigées du formulaire — mais c'est là que se jouent les refus.

## 7 septembre 2026 — Persan : la traduction complete de l'application

**Demande de Jacques (avant de partir pour quatre heures) :** « tu prendras le
drapeau iranien.. je te demande mainetant de continuer sans arret la traduction
en persan de toute l application. »

**Fait, en trois chantiers.**

1. **Le corpus de vocabulaire** — 7 701 / 7 701 cartes (v497). Le C1 restait :
   291 adjectifs, 52 adverbes, 100 expressions. Zero collision a l'arrivee.

2. **Les lecteurs** (v498) — LE POINT QUI COMPTE. Le corpus persan etait complet
   dans les JSON, et AUCUN lecteur de index.html ne lisait un champ `_fa` :
   RANGS_CARTE connaissait deja les rangs persans, les six chargeurs ne les
   posaient jamais. Le piege deja nomme pour le turc et l'ukrainien, une
   troisieme fois. Poses au passage : les libelles de categorie, l'index de
   recherche, `LANGUE_TAG` (fa-IR), l'ecoute de phrases. L'ukrainien manquait
   aussi dans la recherche pour les noms et les adjectifs : ajoute.

3. **Les exercices de grammaire** — 170 phrases d'articles dans index.html
   (v499), puis les 1 682 exercices de `exercices.json` (v500). Nouvel outil
   `tests/lot_exos.py`, sur le modele de lot_langue.py.

**Etat : le persan est la langue la plus completement servie apres le francais.**
Ni le turc ni l'ukrainien n'ont les trois — l'ukrainien n'a aucun exercice de
grammaire, le turc n'a pas les categories de mots-outils.

**Ce qui reste, et que je ne peux pas faire :** un relecteur persanophone. Aucun
controle mecanique ne juge le registre (تو / شما, ecrit contre parle) ni le
naturel d'une tournure. C'est le meme manque que pour le turc et l'ukrainien.

## 7 septembre 2026 — Hatice : l'objectif du jour n'a pas l'air d'avancer

**Retour de Hatice, rapporte par Jacques, qui le constate aussi.** Deux plaintes
distinctes dans la meme phrase :

1. **Cote usager** : la barre « Objectif du jour » ne semble pas bouger quand on
   travaille. Ce n'est pas motivant. Sa question : est-ce que ca ne compte que
   lorsqu'un mot est MAITRISE ?
2. **Cote Jacques** : le tableau de bord admin ne lui donne pas de visibilite sur
   l'utilisation reelle.

**La regle, verifiee dans le code (v500) — reponse a sa question : NON.**

`recordDailyActivity()` n'a que trois appelants :

- `scheduleReview()` — **toute** carte repondue, quel que soit le bouton :
  « Encore », « Je savais » (1re, 2e, 3e reussite). +1 a chaque fois.
- `markMastered()` — la 4e reussite, et « Je le sais deja ». +1.
- `checkAnswer()` — les exercices, **uniquement si la reponse est bonne**, et
  hors rattrapage de fin de serie.

Donc en flashcards la maitrise n'est PAS requise : chaque clic compte. Son
intuition est fausse, mais le fait qu'elle l'ait eue est le vrai probleme —
rien dans l'ecran ne le dit.

**Deux trous reels trouves en verifiant :**

- Le mode **« Parler »** (production orale, v483) ne compte **rien**. On
  s'enregistre, on se reecoute, la barre ne bouge pas d'un cran. C'est
  probablement une part directe de ce qu'elle ressent.
- `dailyActivityToday` et `dailyActivityDate` **sont deja envoyes dans
  Firestore** a chaque sauvegarde — et le tableau de bord admin ne les affiche
  nulle part. Il ne montre que « X/Y mots maitrises · serie de N jour(s) » et
  « derniere sauvegarde il y a... ». La donnee dort, exactement comme
  `updatedAt` dormait avant d'etre affichee.

Et « mots maitrises » monte lentement par construction (quatre « Je savais »
d'affilee) : c'est le seul chiffre du tableau de bord, et c'est le plus lent de
tous. Quelqu'un qui travaille tous les jours y parait immobile.

**Etat : regle etablie et rapportee a Jacques. Aucune modification encore —
il a demande la regle d'abord.**

**Precision demandee par Jacques le meme jour :** « Encore » et « Je savais »
font tous deux exactement +1, sans aucune difference. Ce qui change entre eux,
c'est l'echeance de retour du mot et son pourcentage de maitrise, jamais le
compteur du jour. Et comme « Encore » remet la carte dans la file de la MEME
seance, le meme mot peut compter plusieurs fois : la barre compte des REPONSES,
pas des mots distincts. « 30/30 » ne veut donc pas dire trente mots differents.

## 7 septembre 2026 — Hatice : les verbes et adjectifs des chapitres VHS ne sont pas traduits

**Retour de Hatice, rapporte par Jacques.** Dans la tuile « Chapitres VHS », les
NOMS sont traduits, mais pas les verbes ni les adjectifs.

**Verifie : elle a raison, et c'est pire que le turc seul.** Sur les 16 chapitres
de `themes.json` :

| liste       | total | manquants tr / uk / fa |
|-------------|-------|------------------------|
| mots (noms) |   500 |    0    0    0         |
| verben      |   184 |  184  184  184         |
| adjektive   |   115 |  115  115  115         |

299 entrees sans **aucune** des trois langues. Avec les exemples et les temps
(perfekt, praeteritum, konjunktiv2), cela fait 3 450 champs.

**LA CAUSE, et c'est elle qui compte.** `patch_langue.py` et `lot_langue.py` ne
lisent qu'une seule des trois listes d'un theme :

    for m in t.get("mots", []):

`verben` et `adjektive` ne sont VUS PAR AUCUN OUTIL. Le compteur annoncait donc
« 7 701/7 701, 100 % » en toute bonne foi, sur un corpus dont il ignorait 299
entrees. C'est le meme motif que le piege des lecteurs `_fa` de la v498 : la
donnee existe, personne ne la regarde. Ici c'est l'inverse -- la donnee manque,
et personne ne le voit.

**Ajoute : `tests/trous_langue.py`**, qui balaye TOUS les fichiers de donnees au
lieu des cinq que connaissait lot_langue.py. Sa regle : un champ est du a la
traduction quand son FRANCAIS et son ANGLAIS existent tous deux -- l'anglais
sert de preuve que le champ est traduisible, sans quoi l'outil reclamait 470
traductions pour « kategorie » d'adverbe.json, dont la valeur est « Zeit », un
identifiant et non du texte.

**Ce que le balayage a trouve d'autre** (etat au 7 sept. 2026, avant correction) :

- `funktionswort.json` : 130 categories sans ukrainien.
- `exercices.json` : l'ukrainien n'a **rien** (1 682 exercices) ; le turc et le
  persan ont chacun 152 a 494 champs manquants selon le champ.
- `pruefung.json` : ni ukrainien ni persan (542 champs par langue). Le turc l'a.
- `verbe.json`, `adjectif.json`, `adverbe.json`, `redewendung.json`,
  `grammaire.json`, `synonymes.json` : complets.

**TRAITE (v501, 7 sept. 2026).** Les 299 entrees sont traduites dans les TROIS
langues : 115 adjectifs + 184 verbes, 3 450 champs. `themes.json` est complet,
et `lot_langue.py --etat` affiche desormais 8 000 cartes au lieu de 7 701 --
100 % en turc, en ukrainien et en persan.

Trois corrections d'outillage au passage, chacune sur un defaut qui ne pouvait
pas se voir :

1. `patch_langue.py` et `lot_langue.py` lisent les TROIS listes d'un theme.
2. `patch_langue.py` accepte `cle_exemple` pour viser une occurrence precise.
   « halten » figure trois fois dans les chapitres -- arreter le ballon,
   considerer, tenir un discours -- et l'index rendait les trois pour une seule
   entree : « annehmen » du chapitre 15 avait deja recu la phrase du chapitre 1.
   Repare, et l'outil REFUSE maintenant une entree ambigue au lieu d'ecraser en
   silence.
3. `tests/trous_langue.py` balaye tous les fichiers de donnees.

Controle de non-regression : compare a l'etat d'avant, mon travail avait
introduit quatre collisions -- « sakin » et « teknik » en turc, « آینده » et
« گردشگری » en persan. Toutes levees. Zero collision nouvelle dans les trois
langues.

## Ce que le balayage a trouve ailleurs — A DECIDER PAR JACQUES

Etat au 7 septembre 2026, apres la correction des chapitres VHS :

| fichier | ce qui manque |
|---------|---------------|
| `exercices.json` | l'ukrainien n'a **rien** : 1 682 exercices, ~6 500 champs |
| `pruefung.json` | ni ukrainien ni persan : 542 champs par langue (le turc les a) |
| `exercices.json` | turc et persan : 152 a 494 champs selon le champ |
| `funktionswort.json` | 130 categories sans ukrainien |

Le reste est complet : `themes.json`, `verbe.json`, `adjectif.json`,
`adverbe.json`, `redewendung.json`, `grammaire.json`, `synonymes.json`.

**Autre chose, non demandee mais trouvee en verifiant :** le turc porte 219
collisions preexistantes dans themes.json, l'ukrainien 81 (le persan zero).
Elles sont anterieures a ce travail. C'est le meme controle qui a servi pour le
persan -- `relecture_langue.py --collisions` -- et personne ne l'a jamais passe
sur le turc ni sur l'ukrainien.

---

## 7 septembre 2026 — Les collisions turques et ukrainiennes, corrigees

Demande de Jacques, suite directe du releve ci-dessus : « Corrige les 219
collisions turques et les 81 ukrainiennes. » Le compte reel etait de 184 pour
le turc en noms (219 toutes categories confondues, dont adjectifs, adverbes,
verbes et expressions deja traites plus haut) et de 167 pour l'ukrainien.

**Resultat : zero collision dans les deux langues, sur les cinq categories.**
Huit groupes sont acceptes et inscrits avec leur raison -- deux en turc,
six en ukrainien.

### Ce qu'une collision coute a l'usager

Deux mots allemands differents qui rendent la meme reponse : la carte devient
indecidable. On voit « garson » et on ne peut pas savoir si l'attendu etait
Kellner, Ober ou Kellnerin. L'usager se trompe sans avoir tort.

### La methode, et pourquoi elle n'est pas celle d'avant

Le troisieme verdict de relecture turque (2 septembre) avait montre que la
passe de collisions precedente remplacait des mots JUSTES par des mots rares
ou faux, pour la seule raison qu'il fallait deux reponses differentes. Ici :

- le mot naturel reste, et une parenthese departage -- « kayısı (Avusturya) »
  pour Marille, « сірник (Австрія) » pour Zuendholz. C'est deja la convention
  du corpus : « krem şanti (Avusturya) », « dil (organ) » ;
- quand les deux mots allemands sont reellement distincts, deux mots courants
  de la langue cible, jamais un mot rare tire pour ecarter l'autre ;
- quand ils ne le sont pas, la collision est ACCEPTEE et ecrite, pas maquillee.

### Trois choses que ce travail a mises au jour

1. **Trente des collisions turques n'etaient que des paires de genre.**
   « Zuhoerer » et « Zuhoererin » se disent tous deux « dinleyici » -- le turc
   n'a pas de genre grammatical. L'ukrainien, lui, a des formes feminines
   propres : il n'en avait aucune. `tests/lot_collisions.py` gagne
   `--genre seules|sans` pour separer les deux populations.

2. **Le corpus turc portait DEUX conventions pour la meme marque de genre** :
   « kadın patron » posee en A2 lors d'une passe precedente, et « doktor
   (kadın) ». Deux mots avaient recu chacune une fois -- « Enkelin » etait a
   la fois « torun (kız) » et « kadın torun ». Tout est ramene a la
   parenthese, qui est le mecanisme de precision du reste du corpus.

3. **Corriger une collision en cree d'autres.** « Folge » avait recu
   « netice », qui appartenait deja a « Ergebnis » ; « festnehmen » avait recu
   « заарештовувати », deja pris par « verhaften ». Trois passes pour les noms
   turcs, deux pour l'ukrainien. Le compte est verifie apres chacune, et la
   boucle tourne jusqu'a zero -- pas une fois.

### Ce qui reste

Le **persan** porte 14 collisions preexistantes (non demandees, non touchees).
Elles sont anterieures a ce travail, comme l'etaient celles du turc et de
l'ukrainien avant aujourd'hui.

---

## 7 septembre 2026 (soir) — Le chantier vidéo : ce qui marche, ce qui coûte

Jacques veut des scènes filmées avec des personnages qui bougent dans des
lieux réels, à la manière d'un compte Instagram allemand qu'il m'a montré.
Une journée entière d'essais. Voici l'état, sans arrondir.

### La chaîne, validée de bout en bout

**Artlist Studio** (personnages, lieux, images, mise en mouvement) →
**ElevenLabs** (les voix, depuis NOTRE compte) → **sync.so** (le lip-sync) →
**le lecteur Wortando** (surlignage, six langues).

Le test décisif est passé : un personnage GÉNÉRÉ, une voix fabriquée par nos
scripts, et la bouche tombe juste sur `Gepäckausgabe` — composé de quatre
syllabes, umlaut, groupe `ck`, choisi exactement parce que c'est là que ça
casse.

**HeyGen est écarté.** Ses avatars ne savent pas bouger dans un lieu, ce qui
était toute la demande. Son lip-sync existe mais est enfoui sous « traduire
une vidéo », et sync.so fait le même travail à 0,04 $/s avec une API.

### Ce qui est acquis, et qui ne se repaiera pas

Mark et Anna existent comme personnages réutilisables. Le hall d'arrivée
aussi. La voix de Mark est arrêtée (`Mark-VD-03`). L'épisode 1 est écrit,
traduit en six langues, avec 26 entrées de lexique. Les 19 répliques audio
sont générées et égalisées d'un bloc. Douze segments vidéo sont taillés.

### Ce qui bloque

**sync.so plafonne le gratuit à 3 générations par mois.** Deux plans sur
douze sont synchronisés. Finir l'épisode demande un abonnement : Hobbyist
à 5 $/mois + 2 $ d'usage, ou Creator à 19 $ si Hobbyist pose un filigrane —
à vérifier sur les deux clips livrés.

### Et le vrai sujet : le coût

**Jacques a épuisé presque tout son mois d'Artlist en une journée, sans
un seul épisode fini.** Sa réserve est légitime.

Une part du gaspillage vient de MA méthode, et il faut l'écrire : j'ai fait
itérer six portraits de Mark, puis des corrections, puis tous les angles,
puis Anna, puis deux cadres repris plusieurs fois — chaque passage a coûté
des crédits, alors que l'abonnement inclut des générations ILLIMITÉES sur
certains modèles. La discipline à tenir : **chercher sur l'illimité, ne
sortir les crédits que pour la prise qu'on garde.**

L'autre part est structurelle : trois abonnements pour un produit (Artlist,
sync.so, ElevenLabs), et une facture qui monte avant le premier épisode.

### La question laissée ouverte pour demain

Le lecteur audio fonctionne déjà — texte allemand surligné mot à mot,
traduction en six langues, chaque réplique rejouable. **Il n'a rien coûté.**

Je disais le matin même que la vidéo ajoute l'immersion, pas la
compréhension, puis j'ai passé la journée à construire de la vidéo sans y
revenir. Le geste le moins cher et le plus informatif reste de montrer la
version audio au groupe cette semaine : ce qu'ils en diront décidera si
l'immersion vidéo mérite trois abonnements.

### Détails techniques à ne pas redécouvrir

- Cloudflare refuse la signature d'`urllib` (403, code 1010) : un en-tête
  d'agent ordinaire suffit.
- Artlist n'accepte AUCUN fichier audio : sa voix automatique ou celle du
  personnage, rien d'autre. La synchronisation se fera toujours dehors.
- Mes estimations de durée étaient DEUX fois trop longues. L'audio mesuré
  fait 55,8 s là où j'avais écrit 107. Ne jamais tourner sur une durée
  estimée.
- Deux clips de 5 s suffisent pour douze plans : aller-retour et découpage.
- On duplique des PLANS, jamais des personnages — un second Mark n'est pas
  Mark.

---

## 8 septembre 2026 — La journée où le lip-sync a marché, et où on a compris pourquoi il ne suffit pas

### Ce qui a été livré

L'épisode 1 a été **monté pour la première fois** : 19 plans, les voix posées,
88,8 secondes. Puis remonté quatre fois dans la journée, chaque fois parce que
Jacques avait vu quelque chose.

Le lip-sync **fonctionne de bout en bout**. La chaîne complète — Artlist →
ElevenLabs → sync.so → ffmpeg — a produit un plan dont les lèvres disent
vraiment l'allemand. Verdict de Jacques sur le plan 5 : « définitivement
mieux ».

### Trois choses qu'il a vues et que je n'avais pas vues

**Les deux valises.** Le narrateur disait « Mark kommt mit zwei Koffern an »,
l'image montrait un bagage cabine. J'avais défendu le texte la veille : il
arrive *à Berlin* avec deux valises, en soute, il ne les porte pas. Sur le
papier c'est tenable ; à l'écran, non. Une lecture qu'il faut expliquer pour
la sauver n'est pas une lecture. La réplique dit maintenant « Mark ist endlich
da ».

**Le narrateur au mauvais endroit.** Anna envoie Mark chercher son billet en
bas, la voix du narrateur nous y emmène — puis on remonte au comptoir lui
parler encore quatre fois. Ce n'était pas un problème de répliques mais de
géographie. Le plan est passé après l'au revoir : comptoir, hall, dehors.

**La bouche qui s'ouvre sur du silence.** Sur le plan 5 synchronisé : « la
bouche s'ouvre une dernière fois après avoir terminé de parler ». C'est la
trouvaille de la journée, et elle a demandé trois mesures pour être comprise.

### La cause, et pourquoi personne ne l'a trouvée sans les fichiers

| mesure | résultat |
|---|---|
| l'audio à cet instant | **-91 dB**, du silence numérique |
| `lipsync-2-pro`, même plan | ouvre la bouche **aux mêmes images** |
| le clip **d'origine** | les ouvre aussi : 3,10 s, 3,20 s, 3,70 s |

**Le lip-sync repeint les lèvres. La mâchoire, le menton et les joues restent
ceux du clip source.** Seedance faisait parler Mark pendant quatre secondes ;
il continue de mastiquer sous des lèvres refaites, et aucun modèle ne peut
défaire ça — ce n'est pas dans les lèvres.

D'où la règle, qui vaut pour les 29 épisodes à venir : **le personnage parle au
début du plan, puis ferme la bouche et ne la rouvre plus.** La mâchoire bouge
où l'oreille entend une voix.

### Trois modèles consultés, et ce qu'ils valent

Jacques a soumis le problème à ChatGPT, Gemini et Copilot.

**Les trois se trompent sur la cause.** Tous l'attribuent à un écart de durée :
sync ignorerait que la fin du plan est du silence. Il ne l'ignore pas — on lui
envoie -91 dB. Leur raisonnement s'arrête une couche au-dessus du problème,
faute d'avoir les fichiers.

**ChatGPT a raison contre moi**, et c'est le meilleur apport de la journée :
ne pas chercher une bouche complètement figée, qui risque l'effet collé. Ce
qu'il faut retirer n'est pas la parole, c'est la parole *pendant le silence*.
Ma première règle allait trop loin ; elle a été réécrite.

**Gemini apporte l'économie** : couper le clip *avant* l'envoi. Sync facture à
l'image ; la queue de silence, c'est payer pour synchroniser des images qu'on
jettera. 2,52 $ deviennent 1,96 $.

**Copilot n'apporte rien de neuf**, et une idée à écarter : ajouter des mots
neutres à la fin du texte pour remplir le plan. Non. Le dialogue de cette série
n'est pas de la bande-son, c'est la matière du cours — chaque mot arrive dans
les sous-titres, le lexique et six traductions. **La contrainte technique
s'incline devant la leçon, jamais l'inverse.**

Aucun des trois ne pouvait savoir que **Seedance 2.0 Mini ne descend pas sous
4 secondes** alors que nos répliques font 1,5 à 2,7 s. C'est ce plancher qui
rend le surplus structurel, et qui condamne leur solution commune — générer un
clip à la longueur de la phrase.

### Deux mesures qui remplacent deux croyances

**`speed` n'existe pas sous `eleven_v3`.** Même voix, même phrase, même seed :
`multilingual_v2` passe de 2,60 s à 3,25 s (+25 %, l'effet attendu), `v3` reste
à 2,32 s. Le champ est **accepté sans erreur** dans les deux cas. C'est le pire
des cas : on croit régler un débit, on ne règle rien, et rien ne détrompe.

**Sync facture à l'image, pas à la seconde.** Le tarif était codé en dur à
0,04 $/s — le prix du forfait Scale, à 249 $/mois, que nous n'avons pas. Et
l'affichage à la seconde suppose 25 im/s ; nos clips sont à 24.

### Ce qui a été décidé

**Forfait sync.so Creator, 19 $/mois.** Une seule ligne le justifie :
« no watermark », absent de Hobbyist à 5 $. Pour des vidéos destinées à l'app
et à TikTok, un filigrane est éliminatoire.

**Le montage serré.** Combler le silence en ralentissant la voix demanderait
un ×0,40 à ×0,64 selon les plans — une diction d'endormi. On coupe donc chaque
plan parlant une demi-seconde après la réplique : 88,8 s deviennent 76,1 s,
sans un crédit ni un clip refait. Aucun mot n'est perdu, les 7 plans de décor
sont intacts.

C'est un pansement, et il faut le dire : si les douze plans sont retournés avec
la bouche qui se ferme, le silence redevient utilisable et le rythme aéré
redevient possible.

### Ce que la journée a coûté

| | |
|---|---|
| crédits Artlist | **zéro** |
| sync.so | ~2,50 $ d'usage + 19 $/mois |
| ElevenLabs | ~1 000 caractères |

**Contraste voulu avec la veille**, où un mois d'Artlist était parti en une
journée. La discipline tenue aujourd'hui : mesurer avant de dépenser, un plan
d'essai avant les douze, et l'essai à blanc par défaut sur chaque script qui
facture.

Les 0,19 $ du premier envoi ont été perdus — sync avait rendu 2,25 s pour un
clip de 4,04. Ils ont acheté la découverte que `cut_off` est son mode par
défaut, ce qui valait bien plus.

### Une erreur de méthode à ne pas refaire

Pour lui faire juger la coupe, je lui ai montré le **plan 16 — qui n'a jamais
été passé au lip-sync**. Les lèvres y disent forcément n'importe quoi. Il a
répondu, à juste titre, qu'on ne voyait rien de ce qu'on lui demandait de
juger. Une comparaison ne vaut que si elle isole la variable qu'on teste ;
celle-là en mélangeait deux.

### Ce qui reste

- **Les 12 plans à retourner** sous la nouvelle règle : 2 400 crédits, aucune
  image à refaire. La feuille est prête (`scenes/refaire.py --muets`).
- **Le plan 17 n'a pas de variante d'image propre** — il repartirait de celle
  du plan 13 au pixel près, et la position identique se voit.
- **Les sous-titres mot à mot.** `POST /v1/forced-alignment` prend un audio
  existant et son texte, et rend chaque mot minuté : les prises validées ne
  sont pas à regénérer. Reste le lecteur dans l'app, qui n'existe pas encore.
- **Trois retours de testeurs non traités**, en attente depuis ce matin.
- **La question d'hier est toujours ouverte** : montrer la version audio au
  groupe. Elle n'a rien coûté et personne ne l'a encore vue.

### Détails techniques à ne pas redécouvrir

- Sync **coupe la vidéo à la longueur de l'audio** (`cut_off` par défaut). On
  cale donc l'audio nous-mêmes sur la durée exacte du clip : amorce, voix,
  silence. La durée est bonne parce que nous l'avons faite.
- **Le numéro de plan est une clé d'identité**, pas une position : il nomme le
  clip, la voix, les prises, l'image de décor, la ligne du manifeste et
  l'entrée de mise en scène. Le déplacer dans le seul fichier de scène ferait
  lire au montage le mauvais clip, sans erreur et sans avertissement.
- **Un déplacement de plan forme un cycle** (14 vers 18, mais 18 vers 17…) :
  renommer dans l'ordre écraserait un fichier à chaque pas.
- Un fichier de scène qui annonce `chronometrage: elevenlabs` alors qu'aucun
  plan ne porte de mots minutés est **pire qu'une estimation**.
- `ankommen` est sorti du lexique le jour où plus personne ne le prononçait.
  Une entrée pour un mot jamais dit est du décor.

---

## 8 septembre 2026, la soirée — quatre défauts que rien n'aurait signalés

L'entrée précédente s'arrête à la découverte de la mâchoire. Tout ce qui suit
a été trouvé après, et chaque fois par l'œil ou l'oreille de Jacques sur un
fichier que tous les contrôles automatiques avaient laissé passer.

### 1. La phrase d'Anna amputée de quatre dixièmes

Le plan 13 dure 7,04 s, sa réplique 7,08. Avec l'amorce de 0,35 s, la piste
calée envoyée à sync faisait 7,43 s — **coupée à 7,04**, et le lip-sync s'est
fait sur une phrase tronquée.

`montage.py` savait ça depuis toujours : l'amorce tombe dès que la voix ne
rentre plus. `lipsync.py` ne le savait pas. **Deux scripts, deux règles, et
aucune alerte.** Même calcul dans les deux maintenant, et le script l'annonce
à l'écran quand il retire l'amorce.

### 2. La voix avait dix secondes d'avance à la fin

Jacques : *« la discussion arrive plusieurs secondes avant que Marc arrive au
comptoir »*.

Une réplique de 2,4 s dans un plan de 5 s laissait une piste audio **plus
courte que l'image**. Le démultiplexeur `concat` assemble les deux flux
séparément : chaque trou d'audio remonte tout ce qui suit.

    plan 01   image 5,04   son 4,04   cumul +1,0
    plan 04   image 5,04   son 2,76   cumul +4,6   <- le comptoir
    plan 19   image 5,04   son 3,64   cumul +9,9

**Le défaut était dans TOUS les montages de la journée**, y compris ceux qu'il
avait jugés. ffmpeg ne s'en plaint pas, la durée totale est juste, et le
tableau à l'écran montrait dix-neuf plans normaux.

Chaque piste est désormais complétée par du silence jusqu'à la dernière image
(`apad`), et **un contrôle mesure image et son sur chaque segment avant le
collage** : plus de 0,05 s d'écart et le montage s'arrête.

Ce contrôle a attrapé un second défaut dans la foulée : `-c:v copy` ne coupe
pas à la milliseconde, il garde des paquets entiers. L'image tombait à 2,83 s
pendant que l'audio était coupé net à 2,73. **La durée d'un plan est celle du
FICHIER, mesurée après coupe, et l'audio se cale dessus — jamais l'inverse.**

### 3. Ma mesure donnait la meilleure note au plan défectueux

`video/controler_bouche.py` corrèle le mouvement de la bouche avec l'énergie
de la voix. Sur les douze plans synchronisés : de 0,53 à **-0,31** — une
corrélation négative veut dire que la bouche bouge quand la voix se tait.

Puis trois prises du plan 5, même voix, même image de départ, même lip-sync :

    0,53   Seedance parle du début à la fin -- LA PRISE DÉFECTUEUSE
    0,40   trois phases minutées
    0,09   bouche fermée dès la fin de la réplique

**Celle dont Jacques avait vu le défaut gagne.** La raison est mécanique : une
bouche très agitée pendant que la voix porte corrèle bien avec l'enveloppe
sonore, même quand elle articule un charabia. Une bouche calme a peu de signal.

Je l'avais écrit dans le script le matin même — *« une bouche immobile donnerait
une corrélation basse elle aussi »* — sans en tirer les conséquences quand les
chiffres sont tombés.

**Une mesure qui n'a jamais été confrontée à un cas connu-bon et à un
connu-mauvais ne peut pas arbitrer.** Elle reste bonne pour comparer une série
à elle-même et pour dire QUAND la bouche s'ouvre ; pas pour juger la qualité.

### 4. Quinze durées audio sur dix-neuf étaient fausses

Découvert en branchant les prompts Seedance sur `duree_audio`. Le plan 13 était
faux de **1,60 s**.

La feuille aurait demandé à Seedance une fenêtre de parole trop courte d'une
seconde et demie, **sur douze plans**, et personne ne s'en serait aperçu avant
de regarder les prises — 200 crédits chacune.

Les dix-neuf sont recalées sur les fichiers. Et surtout : `refaire.py` **et**
`production.py` mesurent désormais les mp3 au lieu de croire le scénario. Le
champ ne sert plus que de dernier recours, quand le fichier n'existe pas encore.

### Ce qu'on a appris sur Seedance, et qui vaut pour les 29 épisodes

**Il obéit à un minutage explicite.** C'était la question ouverte de la journée.
Quatre prises du plan 5, mesurées image par image :

- « la première moitié du plan » est une **mauvaise formule** : elle suit la
  durée du clip, pas celle de la voix. La réplique fait 2,27 s quoi qu'il
  arrive.
- des **secondes absolues** marchent : demandé « fermée 0-1 s, parle 1-3,5 s,
  fermée ensuite » sur un clip de 4 s, le pic tombe à 0,96 s et l'amplitude
  retombe après 3,6 s.
- **la durée du clip change l'obéissance** : même consigne à 6 s, il ne
  commence qu'à 1,9 s. Jacques : *« le mouvement d'ouverture de bouche dure un
  petit peu trop longtemps »*. À 4 s il démarre à l'heure mais la fenêtre est
  étroite. **Cinq secondes**, choisi à l'œil.
- **la fin est bonne dans tous les cas.** C'est le début qui se règle.

L'idée du **silence au début** vient de Jacques, et elle valait mieux que la
mienne : un silence initial se vérifie d'un coup d'œil, une fermeture finale
demande de comparer des courbes.

### Six consultations de modèles, et ce qu'elles ont donné

ChatGPT, Gemini et Copilot, plusieurs tours chacun.

**Aucun n'a trouvé la cause.** Tous parlent d'un écart de durée entre vidéo et
audio ; on envoie -91 dB sur la portion silencieuse depuis le matin. Leur
raisonnement s'arrête une couche au-dessus du problème, faute d'avoir les
fichiers.

**Ce qu'ils ont apporté :**
- ChatGPT, contre moi : ne pas figer complètement la bouche — un lip-sync
  travaille mieux sur un visage qui porte déjà du mouvement de parole. Ma
  première règle allait trop loin, elle a été réécrite.
- Gemini : couper le clip **avant** l'envoi. Sync facture à l'image ; la queue
  de silence, c'est payer pour synchroniser des images qu'on jettera.
  2,52 $ → 1,96 $.
- Annoncer la durée totale en tête du bloc de minutage.

**Ce qu'on a refusé, et pourquoi :**
- *Allonger une réplique avec des mots neutres pour remplir un plan.* Le
  dialogue est la matière du cours, pas de la bande-son. Chaque mot arrive dans
  les sous-titres, le lexique et six traductions. **La contrainte technique
  s'incline devant la leçon, jamais l'inverse.**
- *Stocker `debut_parole`, `fin_parole`, `duree_video` dans la scène.* Ce sont
  des valeurs **dérivées**, et `duree_audio` en était une aussi — quinze avaient
  dérivé du fichier sans que rien ne le signale. La leçon n'est pas « mieux
  stocker », c'est **« mesurer le fichier à chaque fois »**.
- *`mutagen` / `pydub` pour lire une durée.* ffmpeg est déjà là pour le montage
  et le lip-sync. Deux paquets de plus à installer sur chaque machine pour une
  capacité qu'on a déjà.
- *Générer un clip à la longueur de la phrase.* Conseillé quatre fois par trois
  modèles. Seedance ne descend pas sous 4 s et nos répliques font 1,5 à 2,7 s :
  **il n'y a aucune durée à choisir.**
- *Le freeze frame sur la fin du plan.* 1,7 s d'arrêt sur image devant un fond
  d'aéroport vivant se voit comme une panne.

### Le coût de la journée

    crédits Artlist        200 (une prise d'essai) + 200 (une seconde)
    sync.so                ~3,00 $ d'usage + 19 $/mois (forfait Creator)
    ElevenLabs             ~1 100 caractères

Le forfait Creator a été pris pour **une seule ligne** : « no watermark »,
absent du forfait à 5 $. Pour des vidéos destinées à l'app et à TikTok, un
filigrane est éliminatoire.

Les 2,66 $ de lip-sync des douze plans sont perdus — ils seront à refaire après
le re-tournage. Ils ont acheté la certitude qu'il fallait retourner, au lieu de
la découvrir après trente épisodes.

### Ce qui reste, au 8 septembre au soir

- **Les 12 plans à retourner**, 2 400 crédits, aucune image à refaire. La
  feuille porte pour chaque plan sa durée à générer et sa fenêtre de parole en
  secondes, mesurées sur son mp3. Faire le plan 5 en premier et le regarder :
  c'est le seul dont on connaisse quatre versions.
- **Le plan 17 n'a pas de variante d'image propre** — il repartirait de celle du
  plan 13 au pixel près. 130 crédits donnent quatre images.
- **Les sous-titres mot à mot.** `POST /v1/forced-alignment` prend un audio
  existant et son texte : les prises validées ne sont pas à regénérer. Reste le
  lecteur dans l'app, qui n'existe pas.
- **Trois retours de testeurs** non traités depuis le matin.
- **La question du 7 septembre est toujours ouverte** : montrer la version
  audio au groupe. Elle n'a rien coûté et personne ne l'a encore vue.

### La règle qui résume la journée

**Ce qui n'est pas mesuré sur le fichier lui-même finira par mentir.** La durée
d'une réplique, la longueur d'une piste dans un segment, le moment où une
bouche s'ouvre : chaque fois qu'une valeur a été écrite une fois puis relue,
elle avait dérivé. Chaque fois qu'on a ouvert le fichier, on a eu le bon
chiffre.

Et son corollaire, plus dur : **un contrôle automatique ne remplace pas un
regard.** Les quatre défauts de la soirée ont tous été vus par Jacques d'abord,
et mesurés ensuite. La mesure sert à comprendre et à ne pas répéter — pas à
détecter.

---

## 9 septembre 2026 — cinq retours mis à l'abri, et le mécanisme qui en perd

**Pourquoi cette section existe avant tout correctif :** Jacques signale qu'il a
envoyé **plus de retours qu'il n'en arrive**. Les cinq ci-dessous sont donc
recopiés ici *avant* toute nouvelle synchronisation — le champ Firestore qui les
porte est réécrit en entier à chaque sauvegarde, et rien ne garantissait qu'ils
survivent à la manipulation suivante.

Horodatage **tel qu'enregistré, donc en UTC** (voir le défaut 2 plus bas) :

| Enregistré (UTC) | Version | Écran | Ce qui est signalé |
|---|---|---|---|
| 2026-09-06 12:56 | v478 | (lien) | *Hausmeister* devrait sortir en premier — *Abwart* est suisse. |
| 2026-09-06 20:07 | v483 | (lien) | « La réponse être au Perfekt. » |
| 2026-09-06 20:23 | v483 | (lien) | Quand le mot est choisi, sa traduction devrait être ajoutée à la phrase française. |
| 2026-09-09 03:50 | v501 | adverbienVokabular | Plusieurs touchers sur « encore » sans effet ; puis retour au W de l'ouverture, puis retour au mot en cours. |
| 2026-09-09 03:51 | v501 | adverbienVokabular | Les quantités par niveau sont décentrées. |

**Aucun n'est corrigé à ce stade.** Ils restent non marqués (`--vu` n'a pas été
lancé).

### Défaut 1 — des retours écrits sur l'appareil n'arrivent jamais

`envoyerRetour()` écrit dans `localStorage` **immédiatement**, puis appelle
`scheduleCloudSync()`, qui **diffère la sauvegarde de 4 secondes** et remet ce
délai à zéro à chaque nouvel appel :

```js
clearTimeout(cloudSyncTimer);
cloudSyncTimer = setTimeout(syncProgressToCloud, 4000);
```

Sur l'app installée, **iOS suspend sans émettre `blur`, `pagehide` ni
`visibilitychange`** (voir la note de projet sur les tests iPhone). Un retour
écrit juste avant de poser le téléphone laisse donc un `setTimeout` qui ne se
déclenche jamais. C'est structurellement **le dernier retour d'une série** qui
se perd — celui qu'on écrit avant de fermer l'app.

Le retour de 03:50 décrit d'ailleurs un retour au splash en pleine session :
tout rechargement dans cette fenêtre de 4 s a le même effet.

**Ce qui est rassurant, et qui n'a pas encore été vérifié sur l'appareil :**
`setItem` étant synchrone et antérieur au minuteur, **les retours perdus
devraient être encore dans le `localStorage` du téléphone**. Une sauvegarde
réussie depuis ce même contexte les enverrait tous.

### Défaut 2 — l'heure enregistrée n'est pas l'heure qu'il était

```js
"[" + new Date().toISOString().slice(0, 16) + " | v" + APP_VERSION
```

`toISOString()` rend toujours de l'UTC. Les 03:50 et 03:51 ci-dessus ont été
écrits vers 05:50 heure locale — Jacques l'a relevé de lui-même. Un horodatage
qu'il faut corriger de tête pour situer un incident est une aide à moitié.

### Défaut 3 — le champ de retours est remplacé, jamais fusionné

`retoursUsager` part à chaque sauvegarde comme **la valeur complète** du
`localStorage` local. L'app installée et le lien Safari ayant **des conteneurs
de données séparés**, une sauvegarde depuis l'un écrase les retours envoyés
depuis l'autre. Un `localStorage` purgé par Safari (ce qu'il fait après environ
sept jours sans visite) écraserait le tout par une chaîne vide.

Ce défaut n'explique **pas** les manquants du 9 septembre — ils viennent du même
formulaire, du même contexte et de la même minute que les deux qui sont arrivés.
Il reste une perte à venir, à corriger indépendamment.

### Ce que la mesure a écarté, puis trouvé (9 septembre 2026, v502)

**Trois hypothèses tirées de la lecture du code, toutes fausses**, et c'est la
mesure qui les a tuées à chaque fois :

1. *Le conflit tuile / lien.* `contexteEcran()` renvoie l'écran **de fond**, pas
   le panneau : les retours envoyés depuis les Réglages portent le nom de
   l'écran d'où l'on vient. Les manquants sortent du même formulaire, du même
   contexte et de la même minute que ceux qui sont arrivés.
2. *Le minuteur de 4 secondes.* `updatedAt` mesuré à deux minutes près : la
   sauvegarde **part et réussit**.
3. *Le coût de la sauvegarde.* Chronométré sur les vraies données — 390 groupes,
   11 290 mots, 527 Ko : `0,6 ms` de comptage, `3,3 ms` de `sansIndefinis`,
   `2,2 ms` de `JSON.stringify`. Une trentaine de millisecondes sur un iPhone.
   Ça ne gèle rien.

**Ce que la mesure a trouvé, et qui n'était dans aucune de mes hypothèses :**

    documents dans users : 12
    poids TOTAL telecharge par le tableau de bord : 2,53 Mo
    dont le seul champ `progress` : 2,53 Mo  (100 %)

`collection("users").get()` ramène les documents **entiers**, et le SDK web ne
sait pas projeter de champs. Le tableau de bord affiche l'adresse, deux
compteurs et les retours — **il télécharge 2,53 Mo de `progress` qu'il n'affiche
jamais**, et que le cache du SDK garde ensuite en mémoire pour la suite de la
session.

Ça concorde avec les trois observations de Jacques : jamais au démarrage,
après un moment d'usage, et **dans l'administration** précisément. Le volume
croît avec chaque testeur et chaque jour de progression : c'est un mur qui
avance tout seul.

**Le filet posé en v502 (et ce qu'il n'est pas).** Le brouillon du formulaire de
retour est écrit dans `localStorage` à chaque frappe et restauré à l'ouverture
des Réglages. Ce **n'est pas** un correctif du gel — la cause reste à établir
sur l'appareil. C'est le refus de continuer à perdre, à chaque incident, le
rapport du défaut le plus grave.

**Reste à décider :** sortir `progress` de ce que le tableau de bord lit. La
piste la moins risquée est un document de résumé léger écrit en même temps que
la sauvegarde (adresse, compteurs, retours), le tableau de bord ne lisant plus
que celui-là. Additif, réversible, sans migration.

### Trois demandes du 9 septembre, traitées en v503

**1. L'app débordait de l'écran après un envoi de retour.** « Je dois prendre mes
deux doigts pour rapetisser l'écran. » Ce n'était pas une mise en page trop
large : **Safari iOS zoome automatiquement sur tout champ de saisie dont la
police fait moins de 16 px, et ne dézoome jamais après.** Le défaut était déjà
connu et corrigé — pour un seul champ, `#wordSearchInput`, avec une note à côté
qui signalait même que `.filters-bar input` restait à 14 px.

Les trois champs restés sous la barre sont passés à 16 px : la zone de retour
(14), la barre de filtres (14) et la note d'un code d'invitation dans le tableau
de bord (13). La note en marge dit maintenant que la règle vaut pour **tout**
champ à naître. Corriger par `maximum-scale` sur le viewport reste exclu : ça
retirerait le zoom manuel à ceux qui en ont besoin pour lire.

**2. Un « i » sur la carte de progression.** Demande : « qu'on puisse comprendre
qu'est-ce qui fait bouger la progression ». L'explication se déplie **dans la
carte**, sous l'anneau, en cinq langues. Elle dit ce que le code fait vraiment :
le pourcentage compte les mots maîtrisés sur tous les mots du niveau affiché
(thèmes + verbes + adjectifs) ; un mot est maîtrisé après **quatre « Je savais »
d'affilée** (revu dans la séance, puis à 1, 3 et 7 jours) ou d'un coup par « Je
le sais déjà » ; « Je ne savais pas » retire la maîtrise et **le pourcentage
redescend** ; un mot maîtrisé revient tous les 16 jours sans cesser d'être
compté.

**3. « Est-ce que le pourcentage marche ailleurs qu'en A1 ? »** Oui — vérifié en
recalculant l'anneau hors de l'app, sur les vraies données et la vraie
progression :

| niv | maîtrisés | total | % | (verbes / adjectifs / thèmes) |
|---|---|---|---|---|
| A1 | 106 | 677 | 16 % | 97 / 0 / 9 |
| A2 | 7 | 951 | 1 % | 2 / 0 / 5 |
| B1 | 5 | 2 136 | 0 % | 0 / 0 / 5 |
| B2 | 2 | 729 | 0 % | 0 / 0 / 2 |
| C1 | 0 | 1 511 | 0 % | 0 / 0 / 0 |

Aucun niveau n'est mort : les totaux sont justes partout, C1 compris. Ce qui ne
bougeait qu'en A1, c'est simplement que les verbes déjà maîtrisés sont des
verbes A1.

⚠️ **Au passage, une anomalie qui n'était pas cherchée : la colonne adjectifs
est à zéro pour les onze testeurs.** Personne n'a jamais maîtrisé un seul
adjectif. Soit personne n'ouvre ce paquet, soit la maîtrise ne s'y enregistre
pas. **Non élucidé.**

⚠️ **Et une seconde, dans la progression des verbes :** `cleMot()` range les
verbes par lemme, mais **retombe sur la position quand `verbeTheme.words` n'est
pas encore chargé**. Résultat : 450 entrées fantômes sous des clés numériques
chez Jacques (600 chez un autre, 450 chez deux autres), invisibles pour le
compte et jamais relues. Elles ne faussent pas le pourcentage — toutes à
`mastered:false` — mais elles gonflent le document, et **un mot marqué maîtrisé
pendant cette fenêtre serait perdu**. **Non corrigé.**

### v504 — le tableau de bord ne télécharge plus la progression de personne

**Le défaut, mesuré :** `collection('users').get()` ramenait **2,53 Mo pour douze
testeurs, dont 100 % de `progress`**, un champ que le tableau n'affiche jamais.
Le SDK web ne sait pas projeter de champs — la seule façon de ne pas télécharger
`progress` est de **ne pas le mettre dans le document qu'on lit**.

**Ce qui change :** chaque sauvegarde écrit désormais, en plus du document
complet, un résumé de quelques kilo-octets dans `resumes/{uid}` — les dix
champs que le tableau affiche réellement (adresse, prénom, deux compteurs,
série, retours, mots demandés, synonymes écartés, date). Le tableau de bord lit
cette collection.

Trois pièges traités en chemin :

- **`vhsChaptersEnabled` n'est pas écrit par la sauvegarde de la personne.** Il
  appartient à l'admin ; l'inclure l'aurait effacé à chaque synchronisation.
  `toggleUserVhsAccess()` écrit maintenant dans les deux documents.
- **Le prénom vient de `user.displayName`**, posé à l'inscription par
  `updateProfile()` — donc disponible sans aucune lecture Firestore.
- **Un écran vide ne veut plus dire la même chose.** Avant, il signifiait « les
  écritures échouent ». Il peut maintenant signifier « les résumés ne sont pas
  encore construits ». Le message nomme les deux causes au lieu d'en supposer
  une.

**La migration est un bouton, pas un chargement.** « Reconstruire les résumés »
est le seul endroit de l'app qui télécharge encore les documents complets : une
opération lourde qu'on assume une fois, au lieu de la subir à chaque ouverture.
Elle recopie `updatedAt` du document d'origine, pas l'heure de la
reconstruction — sinon tous les testeurs paraîtraient actifs à l'instant.

⚠️ **Une règle Firestore est nécessaire pour `resumes`** : sans elle, l'écriture
du résumé échoue (en silence, sans gêner la sauvegarde) et le tableau reste
vide.

### L'élargissement de l'écran, deuxième couche — v506

Signalé une deuxième fois **après** le correctif de la v503 : « l'écran perd son
format, sa grosseur aussi ». La v503 était juste mais incomplète, et la raison
mérite d'être retenue.

**Ce que la v503 avait corrigé** : trois champs dont la taille écrite était sous
16 px. **Ce qu'elle ne pouvait pas voir** : un champ dont la taille n'est écrite
nulle part. Le sélecteur de voix des Réglages est créé par JavaScript **sans
aucun style**, et un `<select>` nu **n'hérite ni de la taille ni de la police du
body** — il prend celles du navigateur. Mesuré sur banc d'essai :

```
select de voix : 13.3333px, police Arial
zone de retour : 16px  (corrigée en v503)
```

13,33 px : Safari iOS zoome au premier toucher et ne dézoome jamais. Et il est
dans les Réglages, **juste au-dessus du formulaire de retour** — sur le chemin
exact de la personne qui vient signaler quelque chose.

**Aucune recherche de texte ne pouvait trouver ce défaut : il n'y avait rien à
chercher.** C'est ce qui a rendu la v503 incomplète, et c'est pourquoi la v506
répond autrement — par une règle de base sur `input, textarea, select`, la
spécificité la plus faible possible, qui pose un plancher pour tout ce qui n'a
rien demandé sans toucher aux règles existantes (`.answer` à 18 px reste à 18).

**Demande explicite de Jacques : « il faudrait s'assurer que la règle s'applique
pour tous les champs qu'on crée ».** D'où un contrôle dans `tests/verifier.py`,
qui refuse désormais un `push` si :

- un champ porte une taille écrite sous 16 px ;
- **ou la règle de base a disparu** — sans elle, le prochain champ créé sans
  style repart à 13 px, en silence.

Les deux régressions ont été **fabriquées et vues échouer** avant d'être
gardées : un filet qu'on n'a pas vu attraper quelque chose n'est pas un filet.
La première tentative de contrôle laissait d'ailleurs passer le cas (a) — c'est
la régression fabriquée qui l'a montré, pas la relecture.

**Vérifié sur banc d'essai après correction** : sélecteur de voix à 16 px dans
la police de l'app, **aucun champ sous 16 px dans les 42 écrans**, et aucun
écran ne déborde à 375 px de large.

### Les quatre retours du matin, et le champ qui allait déborder

Retrouvés le 9 septembre : ils avaient été écrits sur l'appareil mais n'étaient
jamais montés (voir le défaut 1 plus haut). Une sauvegarde les a emportés depuis.

| Enregistré (UTC) | Version | Écran | Ce qui est signalé |
|---|---|---|---|
| 03:59 | v501 | carte adverbien 48/71 « meistens » | « Parfois sans raison il retourne au vidéo d'ouverture et revient ensuite dans l'écran où j'étais. » |
| 04:05 | v501 | carte adverbien 26/32 « also » | « Système gèle, je clique plusieurs fois sur une carte et rien ne se passe. Ensuite retour au vidéo d'accueil et revient à la carte. » |
| 04:07 | v501 | carte adverbien 26/32 « also » | « Surtout quand je soulève un problème et que je clique sur envoyer. Ensuite l'écran devient comme plus gros, je dois rabaisser avec mes doigts ; ça devrait toujours revenir au format de mon cellulaire. » |
| 04:09 | v501 | adverbienVokabular | « Lorsque je clique sur le retour, ça devrait toujours me ramener exactement où je me trouvais avant, mais ce n'est pas toujours le cas. » |

**État :** 03:59 et 04:05 décrivent le gel attaqué en v504. **04:07 est corrigé**
(v503 puis v506 — voir plus bas). **04:09 n'est pas traité** : c'est un défaut
de navigation distinct, et le seul des retours du matin qui reste entier.

### Le champ des retours pouvait se dévorer lui-même

Mesuré le 9 septembre : **3 462 caractères sur un plafond de 4 000**, et le champ
garde la FIN. Encore un peu et les retours du 6 septembre disparaissaient.

La cause n'est pas le volume normal : Jacques a collé son propre historique de
retours dans le champ de retour, trois fois de suite, pour me le transmettre.
Chaque collage a réécrit les anciens retours à l'intérieur du champ — quatre
copies de certains.

**Deux défauts réels que ce geste a mis au jour :**

1. **Un texte collé casse le découpage.** `tests/retours.js` sépare les entrées
   sur un horodatage **en début de ligne**. Un texte qui en contient est donc
   débité en faux retours : 25 entrées lues pour 13 envois réels. Ce n'est pas
   une bizarrerie de lecteur — c'est le format qui n'a aucune défense contre son
   propre motif.
2. **Rien ne prévient de l'approche du plafond**, et le silence est total : les
   plus anciens retours sont coupés sans le moindre signe. Le lecteur, lui, ne
   peut pas savoir qu'il manque quelque chose.

## 9 septembre 2026 — le turc était fini, l'ukrainien ne l'était pas

**Le turc est complet**, vérifié sur les trois plans le même jour : corpus
8 003/8 003, exercices 1 682/1 682, interface 911/911, zéro gabarit perdu, zéro
balise cassée, zéro chaîne restée en français. Ce que mes notes disaient
manquer — les libellés de catégorie des mots-outils — était fait depuis.

**L'ukrainien, non**, et l'écart ne se voyait sur aucun compteur d'entrées :

| | corpus | interface | exercices | catégories des mots-outils |
|---|---|---|---|---|
| turc | 8 003 ✔ | 911 ✔ | 1 682 ✔ | 161 ✔ |
| **ukrainien** | 8 003 ✔ | 911 ✔ | **152 / 1 682** | **0 / 161** |

Un ukrainophone ouvrant un exercice de grammaire voyait l'anglais, **sans que
rien ne le signale** : le champ manquant, l'app replie en silence. C'est le
piège déjà nommé pour le turc, l'ukrainien et le persan — rencontré cette fois
non pas sur le câblage des lecteurs, mais sur **une catégorie de contenu
entière que personne ne comptait**.

### Ce qui est fait

- **Les 161 catégories de mots-outils**, plus 31 libellés anglais qui étaient
  présents mais vides — ce qu'aucun compteur d'entrées ne voit non plus.
- **1 037 exercices sur 1 682 (62 %)**, en dix-neuf jeux.

### La méthode, et pourquoi elle tient

Les explications d'un jeu ne sont presque jamais uniques : ce sont quelques
**moules** avec des trous. Les 145 exercices du Perfekt tiennent en **huit**
moules ; les 70 de relativOrder en **deux**. On traduit les moules une fois, un
script lit les trous dans le français et remplit. Recopier 145 fois la même
règle à la main l'aurait fait finir dite de huit façons différentes.

Seules les **phrases d'exemple** sont traduites une par une : aucun moule ne
les couvre, et c'est là qu'est le vrai travail.

### Le garde-fou, et les trois choses qu'il a trouvées

Chaque script **refuse d'écrire** s'il reste du français dans le résultat. Une
explication à moitié traduite passerait tous les contrôles existants — le champ
existe et n'est pas vide. Il a servi trois fois :

1. **Il refusait les 140 explications, toutes correctes** : sa liste de mots
   français contenait « du » et « le », et il prenait le « du warst » allemand
   pour du français. *Un filet qui attrape tout n'attrape rien* — il liste
   désormais des mots **distinctifs**.
2. **Trois suffixes manqués par mon relevé** (« forme polie pour une
   demande »), sur quatre exercices du Konjunktiv II.
3. **Un fragment remplacé avant celui qui le contient** : « + infinitif »
   mangeait l'intérieur d'un suffixe plus long, qui repartait à moitié en
   français.

Aucune des trois n'aurait été vue à la relecture.

### Choix de langue assumés

L'ukrainien **distingue** ce que le français confond : `wenn`/`ob` donne
« якщо »/« чи », `aber`/`sondern` donne « але »/« а ». La traduction fidèle
donne donc la réponse. Choix assumé, le même qu'en persan : mieux vaut montrer
à quelqu'un que sa langue fait déjà la distinction que l'allemand demande,
plutôt qu'une tournure tordue pour préserver un piège qui n'est pas le sien.
En revanche `wenn`/`wann` se disent tous deux « коли » : **ce piège-là reste
entier**, et l'effacer par symétrie serait la faute inverse.

### Ce qui reste — 645 exercices, onze jeux

`blocsConnecteurs` (120), `possessiv` (70), `ordreInverse` (54),
`relativGenitivReconnaissance` (51), `adjektiveDeklination` (50), `exercises`
(50), `kasusReconnaissance` (50), `partikelnNuance` (50),
`praepReconnaissance` (50), `praepWoWohin` (50), `wortstellungNicht` (50).

`blocsConnecteurs` est le plus difficile : ses 120 explications sont faites de
**blocs recombinés**, pas d'un moule unique — il en faudra une douzaine, plus
une vingtaine d'explications qui ne servent qu'une fois.

⚠️ **Ce qu'aucun de ces contrôles ne juge, ici comme pour le turc et le
persan : un relecteur ukrainophone.** Le registre, le naturel d'une tournure.
Une phrase peut être exacte, cohérente, bien câblée, et sonner comme une
traduction.

⚠️ **Anomalie trouvée en chemin, non corrigée** : dans TeKaMoLo, la tuile de
réponse vaut « temporel », « causal », « modal » — **en français, pour toutes
les langues**. `correctEn`, `correctTr`, `correctFa` sont tous absents. Le trou
est en amont de l'ukrainien.

### Quatre retours de plus, en v507

| Enregistré (UTC) | Écran | Ce qui est signalé | État |
|---|---|---|---|
| 06:25 | exercice kicker_kasus_art_dat | « Quand on écoute la phrase, ce n'est pas la voix Aurora, c'est la voix de l'iPhone. » | **non traité** |
| 06:27 | home | « Si je suis dans adjectif et que je clique sur administration, une fois le retour envoyé je ne reviens pas sur l'adjectif. » | **non traité** — même défaut que le 04:09 |
| 06:32 | exercice kicker_zuinf | « Le i information n'apparaît pas dans le rectangle de progression. » | **corrigé en v508** |
| 07:03 | écoute | « Une lettre du mot déborde sur une autre ligne. » | **non traité** |

**Le « i » invisible, et ce que ça dit de ma méthode.** Le bouton était dans le
DOM depuis la v503 — mais posé dans `.home-level-hint`, que le CSS masque par
`display:none !important`. Cette ligne d'aide ne sert qu'une fois ; ses éléments
ne restent dans le DOM que pour que le JS puisse y écrire sans planter. Personne
ne pouvait donc l'ouvrir pendant **cinq versions**.

J'avais vérifié la syntaxe, le vérificateur, les clés de traduction dans les
cinq langues — **et jamais le rendu**. Le `CLAUDE.md` le demande en toutes
lettres, et le banc d'essai existait depuis la v506. Le défaut n'était pas
subtil : il suffisait de regarder l'écran.

**La coupe annoncée a servi le jour même.** Le champ de retours a affiché
`[COUPE] 160 caractères plus anciens ont été retirés, faute de place` — la
troncature qui, la veille encore, aurait emporté ces 160 caractères en silence.

### Les quatre retours de la v507, traités (v508 → v511)

| Signalé | Cause trouvée | Version |
|---|---|---|
| Le « i » n'apparaît pas | Le bouton était dans `.home-level-hint`, masqué par `display:none !important` — depuis la v503 | **v508** |
| Ce n'est pas la voix Aurora | Les 120 exercices d'articles sont **fabriqués par le code**, pas dans `exercices.json` : le manifeste audio ne les voyait pas, aucun mp3 n'existait | **v509** + manifeste |
| Le Retour ne ramène pas où j'étais | Le bouton appelait `goHome()` ; l'écran de départ était déjà connu mais ne servait qu'à étiqueter les retours | **v510** |
| Une lettre déborde sur une autre ligne | `overflow-wrap:anywhere` coupe n'importe où : 177 mots sur 1 385 laissaient ≤ 3 lettres seules | **v511** |

**Sur la voix, la moitié seulement est réglée.** La phrase lue est désormais
correcte — elle ne dit plus « Ich glaube dem Arzt, der Arzt, Dativ », la
parenthèse d'indication étant écartée par le champ `audioDe`, qui existait déjà
et que personne ne posait ici. Mais **la voix reste celle du téléphone** tant
que les 146 fichiers manquants ne sont pas générés : 3 769 caractères, 3,1 %
d'un mois de forfait Creator.

Le manifeste demande maintenant ces phrases **au code lui-même** (node évalue
`index.html`, même procédé que `tests/i18n_dump.js`) plutôt que de les recopier,
et **s'arrête si node échoue** — un manifeste amputé de 146 phrases se
regénérerait sans un mot et laisserait ces exercices muets une seconde fois.

**Ce que le « i » invisible dit de ma méthode.** J'avais vérifié la syntaxe, le
vérificateur, les clés dans les cinq langues — **et jamais le rendu**, que le
`CLAUDE.md` demande en toutes lettres. Le banc d'essai existait depuis la v506.
Le défaut n'était pas subtil : il suffisait de regarder l'écran. Les quatre
correctifs ci-dessus ont tous été vus à l'écran avant d'être poussés, et deux
d'entre eux ont changé à cause de ce qu'on y a mesuré — le plancher du mode
Écoute est passé de 20 à 19 px parce que deux mots tenaient à 19.

## 9 septembre 2026 — le re-tournage est validé sur un plan

**La question posée au plan 05 :** la mâchoire se ferme-t-elle quand la voix
s'arrête ? Elle n'a rien à voir avec les lèvres — sync.so les repeint de toute
façon, mais **il ne peut pas refermer une mâchoire**, c'est écrit dans
`lipsync.py` depuis le 8 septembre.

**Réponse mesurée**, une image tous les 0,2 s entre 2,7 s et 3,7 s :

| | 2,7 s | 2,9 s | 3,1 s | 3,3 s | 3,5 s |
|---|---|---|---|---|---|
| ancienne prise | ouverte | ouverte | ouverte | ouverte | ouverte |
| **nouvelle** | ouverte | ouverte | entrouverte | se ferme | **fermée** |

La consigne fonctionne, avec **environ 0,6 s de latence** : la fermeture
demandée à 2,8 s se produit vers 3,4 s. Seedance ne prend pas les chiffres au
pied de la lettre, mais il comprend l'intention — et c'est ce qui manquait
entièrement avant.

**Verdict de Jacques, sur les vidéos synchronisées :** la version à 5 s a trop
d'air, l'ancienne à 4 s est mauvaise (la bouche continue), **celle coupée à
3,52 s est la bonne**.

### Les deux réglages qui en découlent

- **Générer à 5 secondes**, toujours. L'air en trop n'est pas un défaut : c'est
  la marge dont Seedance a besoin pour refermer la bouche. Générer à 3,5 s
  donnerait une bouche qui parle encore à la coupe.
- **Couper au montage avec `--queue 0.9`** : 0,35 d'amorce + la réplique + 0,9.

### Mon erreur de méthode, et ce qu'elle a appris

J'ai d'abord envoyé les prises **brutes** en disant « avec la voix posée, comme
au montage ». Jacques : « la voix n'est pas du tout synchronisée. » Il avait
raison — un clip Seedance fait articuler des mots INVENTÉS, et je sautais
l'étape sync.so. Ce qu'il jugeait n'était pas ce que le test devait démontrer.

**Deux étapes distinctes, que j'avais confondues :** la mâchoire vient de la
génération, les lèvres du lip-sync. Le re-tournage ne sert qu'à la première.

### ⚠️ Un piège qui aurait coûté 200 crédits pour rien

`etat.json` marquait le plan 05 `COMPLETED` et `04-lipsync/` gardait l'ancienne
version — alors que `03-final/` venait de recevoir la nouvelle prise. Une
relance aurait **sauté le plan en silence**, et le montage aurait repris la
vieille version, après un re-tournage payé pour rien.

`lipsync.py` compare désormais les dates : une source plus récente que le
résultat rend le travail **périmé**, et il le dit au lieu de sauter. Il
n'efface rien tout seul — une génération payée ne se jette pas sans qu'on le
dise. Vérifié : le garde-fou se déclenche sur le plan 05.

## 10 septembre 2026 — le gel, et ce que l'app faisait d'elle-même

**Signalé le 9 septembre (v512, carte nomen 33/55 « Fertiggericht ») :**
« L'application gèle encore et reviens au vidéo d'ouverture pour ensuite
revenir à l'application. » Déjà dit deux fois le 9 en v501, sur d'autres
cartes. Précision donnée le 10 : **« c'est arrivé alors que j'étais très
actif, sans pause ».**

### Le retour au vidéo d'ouverture n'était pas un redémarrage

Le pouls de l'écran d'ouverture (v259) estampille l'heure toutes les 300 ms et
lit tout trou de cinq secondes comme une mise en veille. **Un fil principal
bloqué laisse exactement le même trou** : un minuteur ne tourne pas davantage
quand l'app travaille que quand elle dort. Les deux états étaient
indiscernables, et l'app rejouait son ouverture à chaque gel de 5 s. Le
« retour à la carte où j'étais » n'était pas une restauration : la page
n'avait jamais bougé.

**Le pouls bat maintenant dans un fil séparé** (un Worker dédié — pas un
service worker, il n'a pas de portée et ne touche pas à celui des
notifications). Il continue de battre quand le fil principal est pris, et il
s'arrête avec l'app quand iOS la suspend. Les deux états se distinguent enfin :

| | ouvrier | verdict |
|---|---|---|
| fil principal bloqué | a battu tout du long, messages en attente | gel — pas d'ouverture |
| app suspendue | dormait aussi | absence — on rejoue l'ouverture |

Mesuré au banc : 7 s de fil bloqué, l'ouverture ne revient plus, et le retard
des battues donne **6 766 ms**.

### Le gel lui-même : un suspect, et un instrument

« Très actif, sans pause » écarte la sauvegarde Firestore, qui part quatre
secondes après la **dernière** carte — donc jamais quand on enchaîne. Ce qui
tourne à chaque carte jugée, lui, c'est `saveProgress()` : un `JSON.stringify`
de **toute** la progression suivi d'un `localStorage.setItem`, synchrones. Le
coût ne dépend pas du mot qu'on vient de juger mais de tout ce qui a été
appris avant. C'est le piège de la v100 (`getWordState` en O(n²)) une seconde
fois : un travail proportionnel à la progression posé dans un geste répété.

L'écriture est **différée de 800 ms**, avec vidage sur `pagehide`, `freeze` et
passage en arrière-plan. Le cache mémoire reste la vérité immédiate : aucun
lecteur ne voit de retard. ⚠️ Ce qui est mis en jeu : une page qui mourrait
pendant le délai perdrait **la dernière carte jugée**, pas davantage.

**Mais je ne sais toujours pas si c'était la cause**, et ce défaut a déjà été
deviné trois fois. D'où le **journal du gel**, dans la carte admin « Journal
audio », qui survit au redémarrage et se copie d'un bouton : une ligne par
blocage d'au moins 1,5 s, avec sa durée, l'écran, et **le nom du travail en
cause quand il s'est annoncé**. Deux travaux s'annoncent (`progression ->
localStorage`, `progression -> Firestore`) ; un gel qui sort `?` vient
d'ailleurs, et c'est justement l'information qui manquait.

### Ce qu'il faut pour clore

Une séance de cartes en v513, puis COPIER LE JOURNAL. Si les lignes disent
`progression -> localStorage`, c'était bien ça et le différé l'a réglé. Si
elles disent `?`, la cause est ailleurs et le journal dira où — sans avoir à
deviner une quatrième fois.

## 10 septembre 2026 — l'ukrainien, cette fois pour de bon

**État au début de la journée** : les exercices à 67,6 %, et `pruefung.json`
— les quatre épreuves de l'examen — à **zéro**.

| | corpus | interface | exercices | examen |
|---|---|---|---|---|
| turc | 8 003 ✔ | 911 ✔ | 1 682 ✔ | 542 ✔ |
| **ukrainien, ce matin** | 8 003 ✔ | 911 ✔ | **1 137 / 1 682** | **0 / 542** |
| **ukrainien, ce soir** | 8 003 ✔ | 911 ✔ | **1 682 ✔** | **542 ✔** |

L'ukrainien est désormais à **parité exacte avec le turc** sur tous les
fichiers de données. Ce qui manque encore dans `exercices.json` manque
identiquement en turc et en persan : ce n'est pas un trou ukrainien.

### Les neuf jeux d'exercices, et ce que le garde-fou a trouvé

Neuf jeux, 545 exercices. Méthode inchangée : on traduit les **moules** une
fois, un script lit les trous et remplit ; seules les phrases d'exemple se
traduisent une par une, **depuis l'allemand** — traduire une traduction fait
dériver deux fois.

Chaque script refuse d'écrire si quelque chose ne colle pas. Il a servi trois
fois, et **aucune des trois n'aurait été vue à la relecture** :

1. **`ordreInverse` allait dans les deux sens.** J'avais relevé un seul moule
   (« la subordonnée passe derrière »). Le refus a montré **quatorze phrases
   qui font l'inverse**. Le script vérifie maintenant que l'indice et
   l'explication vont dans le même sens — les deux phrases sont justes prises
   séparément, rien d'autre ne les aurait attrapées.
2. **`partikelnNuance` répond par une étiquette, pas par un mot allemand.**
   Sans `optionsUk`, l'ukrainophone choisissait entre treize étiquettes
   **françaises** sur un écran par ailleurs entièrement ukrainien. Le champ
   `options` existait et n'était pas vide : invisible à tout compteur.
3. **`blocsConnecteurs` : 120 explications posées, 36 exercices toujours « à
   faire ».** Il manquait **deux indices sur six** — les seuls qui portent une
   phrase, les quatre autres n'étant que des noms de temps allemands.

### L'examen : 542 champs, et un contrôle qui refusait du travail juste

`pruefung.json` n'a aucun moule : ce sont des consignes, des traductions et
des explications d'examen, traduites une par une. Le garde-fou repris du turc
compare longueur et nombre de phrases avec le français, pour attraper une
explication qui aurait perdu sa seconde phrase — celle qui dit ce que l'erreur
coûte.

**Il a refusé trois traductions correctes**, chaque fois pour une raison de
typographie et jamais de traduction :

- l'**espace française avant « ? » et « » »** faisait compter deux phrases là
  où il y en a une, citée ;
- le **rapport de longueur de 0,55**, calibré sur des explications amputées,
  mesurait la compacité d'une langue sur une question de six mots ;
- le **point d'abréviation** : « Que doit faire M. Sow… » se coupait après
  « M. », et ce fragment fait dix-sept signes.

Ce qui a été corrigé, c'est le **compteur**, jamais le seuil. La tentation
était de rallonger l'ukrainien pour passer le contrôle : c'est exactement
ainsi qu'un contrôle devient décoratif.

### ⚠️ Et le défaut le plus grave de la journée n'était pas dans la traduction

Une fois les 542 champs posés, **ils n'atteignaient aucun écran**. Les quatre
lecteurs de `pruefung.json` recopiaient chacun `_en` et `_tr` à la main, et
rien d'autre. L'ukrainophone voyait du **français** sur les quatre épreuves.

Le fichier de données était complet, la traduction juste, le vérificateur
passait. **C'est le même défaut que pour le turc, puis pour le persan** —
troisième fois, et troisième fois trouvé en allant regarder plutôt qu'en
comptant.

Ajouter « uk » à quatre endroits aurait laissé le piège entier pour la langue
suivante : les cinq langues se construisent maintenant d'un coup
(`champsPruefung`), et ajouter une langue est **une entrée dans une liste**.
Les champs vides d'une épreuve sont posés dans toutes les langues, sans quoi
`texteTraduit` remonte la chaîne de repli et sert le français — un champ vide
qui se remplit tout seul de la mauvaise langue.

Vérifié à l'écran, pas au compteur : les quatre lecteurs rendent de
l'ukrainien en langue `uk` et du français en langue `fr`.

### Ce qui reste, et que je ne peux pas juger

**Un relecteur ukrainophone.** Le registre, le naturel d'une tournure. Une
phrase peut être exacte, cohérente, bien câblée — et sonner comme une
traduction. C'est vrai ici comme pour le turc et le persan, et aucun de ces
contrôles ne le voit.

**Le persan**, lui, n'a toujours rien de `pruefung.json` : 542 champs. Le
câblage, en revanche, l'attend désormais — il suffira de poser la donnée.

## 10 septembre 2026 — « un morceau trop gros, inatteignable »

**Demande de Jacques, en plusieurs temps :** les 462 noms d'A1 avant qu'un mot
revienne quatre fois, *« ça risque de ne jamais arriver »* ; puis l'usager
peut aller sur les noms, les adverbes ou les exercices ; puis A1 lundi et C1
mardi ; et pour finir : *« ça peut paraître comme un morceau trop gros,
inatteignable au niveau des objectifs de progression »*.

**Rien n'a été code.** L'analyse et la proposition sont dans
`retours/proposition-progression.md`. Trois choses mesurées qui méritent
d'être ici :

- **Un mot jamais vu compte comme « dû ».** `cartesEchues()` renvoie vrai sur
  `!st.due`, et un mot neuf a `due: 0` : la première séance sert donc les 462
  cartes d'un coup. Il n'y a **aucune distinction entre neuf et à revoir**.
- **⚠️ Les exercices ne laissent aucune trace.** `exerciseResults` vit en
  mémoire, remis à zéro à chaque départ. Rien n'est écrit sur disque : deux
  semaines de grammaire donnent 0 % de progression, et ce n'est pas une
  impression.
- **Le premier mot maîtrisé ne peut pas arriver avant le 11ᵉ jour** (10 min,
  1 j, 3 j, 7 j). Aucun découpage en blocs ne change ce chiffre.

**Le diagnostic** : le problème n'est pas la porte choisie, c'est le
**dénominateur**. Tant que la progression est une fraction d'un très grand
tout fixe, elle décourage. La proposition remplace ça par trois nombres sans
dénominateur — mots en cours, mots acquis, jeux solides — et garde le
pourcentage par niveau comme carte, pas comme note.

**Ordre proposé** : la mémoire de la grammaire d'abord (par JEU, jamais par
exercice), les compteurs de vocabulaire ensuite, le plafond de mots neufs en
dernier.

---

## 10 septembre 2026 — la grammaire a une mémoire (v519)

**Demande, de Jacques :** *« oui fais-le »*, après la proposition de commencer
par le chantier le plus débloqué des trois.

**Ce qui existait :** rien. `exerciseResults` vivait en mémoire et repartait à
zéro à chaque série. 1 682 exercices, 40 jeux, et pas une ligne écrite sur le
disque — pas d'historique, pas de score, pas de « vu la dernière fois le… ».

**Ce qui a été fait :** un magasin `deutschAI_grammaire_v1`, écrit à la fin de
chaque série dans `showResults()`, qui garde **par jeu** : le nombre de séries,
la date de la dernière, le dernier pourcentage, le meilleur, les totaux cumulés
(questions / justes) et le **nombre de séries sans aucune faute**.

⚠️ **Par jeu, jamais par exercice** — réussir « Ich habe gegessen » ne prouve
pas qu'on sait le Perfekt. L'identité du jeu manquait : `startExerciseSet()`
écrase son paramètre `list` dès qu'il l'a chargé, si bien que le nom était perdu
avant la première question. D'où `exerciseJeuNom`, capturé avant l'écrasement, et
laissé à `null` pour les séries construites à la volée (dictée, rektion) — elles
ne font pas partie des 40 jeux.

⚠️ **On range des faits, on ne décide pas encore.** Ce que « solide » veut dire
n'est pas tranché (question 4 du dossier de relecture). `sansFaute`, `meilleur`
et les totaux vivent côte à côte pour que le critère se choisisse plus tard sur
des données réelles, sans redemander à personne de tout refaire.

**Le nuage :** envoyé comme **une seule chaîne**, à côté de `retoursUsager` et
`synonymesEcartes` — Firestore indexe chaque entrée d'un objet, et le plafond
des 40 000 a déjà fait échouer des sauvegardes en silence (v396-v400). Et
restauré par **fusion jeu par jeu**, jamais par écrasement : ouvrir l'app sur un
second appareil aurait sinon effacé les séries faites sur le premier.
`GRAMMAIRE_KEY` rejoint aussi la liste de `resetAllConfirm()`.

**Vérifié :** `tests/essai_grammaire.js` (nouveau) exerce le vrai code extrait
d'`index.html` — 22 contrôles, dont le stockage illisible, la série vide, les
deux sens de la fusion et le champ distant corrompu. Plus `tests/verifier.py`,
14 012 contrôles.

**Reste à faire :** rien n'affiche encore cet historique. C'est délibéré —
l'écran dépend du critère « solide », qui n'est pas fixé.

---

## 10 septembre 2026 — les mots classés par fréquence d'usage (v520)

**Demande, de Jacques :** *« cherche une liste de mots par fréquence, libre de
droits »*, pour ordonner les étapes du chemin.

**La source retenue :** Leipzig Corpora Collection, sous **CC BY** — usage
commercial permis, et **pas de partage à l'identique**, donc moins contraignant
que le CC BY-SA de WikDict que le dépôt porte déjà. Deux corpus, ramenés chacun
à une fréquence par million avant d'être additionnés : `mixed-typical_2011`
(registre équilibré) et `news_2023` (vocabulaire d'aujourd'hui). Écarté :
`hermitdave/FrequencyWords`, en CC BY-SA et tiré de sous-titres de films.

**Le piège central :** ces listes comptent des **formes**, pas des lemmes. La
fréquence de *gehen* est portée par *geht*, *ging*, *gegangen* — l'infinitif
lui-même est rare. Un appariement naïf faisait descendre tous les verbes et
tous les adjectifs face aux noms.

**Trois corrections, toutes mesurées avant d'être adoptées :**

- **Les verbes** : on additionne l'infinitif et les six personnes du présent,
  que nos fiches portent déjà.
- **Les pronominaux** : `sich erinnern` s'écrit en deux mots, infinitif comme
  présent — **aucune** forme n'était trouvée. Retirer le pronom a fait tomber
  les verbes muets de 124 à 21.
- **Les séparables** : `anrufen` se dit *rufe an*. On ne peut pas retirer la
  particule (*rufe* donnerait la fréquence de *rufen*), donc on va chercher le
  **participe** dans la phrase d'exemple du parfait. Il restait un biais — rang
  médian 872 contre 553 — corrigé par un facteur **×2,82** estimé sur le
  rapport des médianes.
- **Les adjectifs** : les formes déclinées d'abord, la forme nue seulement en
  dernier recours **et signalée** (`approx`). Compter la forme nue hissait
  « zu » au premier rang des adjectifs — la fréquence de la préposition.

⚠️ **Une piste écartée après mesure.** Fondre séparables et non-séparables par
**percentile** égalisait parfaitement les rangs médians (657 contre 656) mais
cassait la tête du classement : *annehmen* et *anbieten* passaient devant
*haben* et *können*. Le percentile suppose deux distributions de même forme ; le
sommet de la fréquence allemande est tenu par des auxiliaires sans équivalent
séparable. Le facteur multiplicatif préserve la forme de la distribution.

**La couverture obtenue :** noms 98,4 %, adverbes 98,3 %, adjectifs 98,0 %,
verbes 98,4 %, mots-outils 87,6 %. **Les expressions : 20,9 %** — une suite de
mots n'est dans aucune liste de fréquence, et elles sont rangées en queue par
ordre alphabétique plutôt que de recevoir un rang inventé.

⚠️ **Ce que le chiffre ne dit pas, et qui compte pour la suite :** la fréquence
d'un corpus **écrit** n'est pas l'utilité pour un apprenant. `duschen` et
`putzen` finissent derniers des verbes A1. C'est un argument de plus pour que le
**niveau CECR reste l'organisateur principal**, la fréquence n'étant qu'un
affinage à l'intérieur d'un niveau — ce qui est exactement le chemin décidé.

**Livré :** `tests/frequence.py` (le script, seule source lisible) et
`frequence.json` (282 ko, 7 704 entrées, dérivé). L'attribution CC BY est dans
la carte « Crédits » des réglages, **dans les cinq langues**. Rien ne consomme
encore ce fichier.

---

## 10 septembre 2026 — la séance a enfin une fin (v521)

**Demande, de Jacques :** *« je prendrais comme tu proposes 15 par jour… avec
possibilité d'ajouter s'il passe les 15 et qu'il veut une nouvelle série de
15 »*.

**Le défaut corrigé :** `cartesEchues()` renvoyait vrai sur `!st.due`, et un mot
jamais touché a `due: 0`. Ouvrir « Noms A1 » servait donc **les 462 cartes d'un
coup**. Ce n'était pas un choix de conception, c'était la conséquence d'une
valeur par défaut — et c'est la cause mécanique du « la séance n'a pas de fin ».

**Ce qui a été fait :** `cartesDeSession()` sépare désormais les cartes **jamais
vues** des cartes **réellement échues**, sert toutes les échéances (jamais
plafonnées — perdre ce qu'on a appris coûte plus cher que d'avancer d'un jour)
et au plus **15 mots neufs par jour**, comptés au moment de la **première
réponse**, jamais au moment où la carte est servie.

⚠️ **Le plafond n'est pas une précaution de confort.** Le manuel d'Anki donne
les deux chiffres ensemble : 20 cartes neuves par jour est son défaut, et à ce
rythme les révisions quotidiennes montent « autour de 200 cartes par jour ».
15 place l'A1 (797 entrées) à une cinquantaine de jours pour une charge plus
basse. Le bouton **« Encore 15 mots nouveaux »** sur l'écran de fin ouvre une
série de plus, **pour aujourd'hui seulement**.

⚠️ **Deux pièges rencontrés, et tous deux auraient rendu le plafond décoratif :**

- **Dix écrans remplaçaient une séance vide par TOUT le paquet**
  (`if(currentCards.length === 0) currentCards = allItems;`). Il aurait suffi
  d'avoir tout révisé pour que les 462 cartes reviennent. Le repli sert
  maintenant `cartesCommencees()` : ce que l'apprenant a **déjà entamé** et pas
  encore maîtrisé — jamais vide pour quelqu'un qui a travaillé, et sans un seul
  mot neuf.
- **Cinq écrans annonçaient « tous les mots sont maîtrisés »** quand la séance
  ressortait vide. Avec le plafond, c'est faux une fois sur deux : la dose du
  jour est simplement faite. `toastSeanceVide()` distingue les deux cas et dit
  combien de mots restent dans le paquet.

**Vérifié :** `tests/essai_plafond.js` (nouveau), 18 contrôles sur le vrai code
extrait d'`index.html` — dont les 462 cartes ramenées à 15, la priorité des
échéances, la dose qui se consomme, « encore 15 » qui n'ouvre qu'une série et
que le lendemain oublie, et le repli qui ne rouvre pas la vanne. Plus
`verifier.py`, 14 028 contrôles.

⚠️ **Portée : partout.** Toutes les portes actuelles (Noms, Verbes, Adjectifs,
thèmes, Mots au hasard) passent par `cartesDeSession()`. Les testeurs verront le
changement dès demain, sans message d'annonce — la question de la portée avait
été posée et laissée sans réponse ; c'est la seule option qui corrige le défaut
là où il fait mal.

---

## 10 septembre 2026 — un mot su ne revient plus à vie (v522)

**Remarque de Jacques :** *« si c'est un mot comme Hallo, même après seize
jours, tu ne veux pas le revoir »*.

**Le défaut :** `markMastered()` remettait `due` à `SRS_MAINTENANCE_DAYS`
**à chaque contrôle réussi**. Un mot maîtrisé revenait donc tous les 16 jours
**pour toujours** — `Hallo` serait revenu vingt-trois fois par an, à vie.

**La réponse retenue, et celle qui a été écartée.** Un bouton « plus jamais »
demande une décision définitive sur une chose incertaine, et il se regrette.
C'est l'**intervalle** qui devait grandir : `SRS_ENTRETIEN_JOURS = [16, 35, 90,
180, 365, 730]`. Chaque confirmation éloigne le mot davantage ; trois « oui » et
`Hallo` ne revient plus que deux fois par an, cinq et c'est une fois tous les
deux ans. Il disparaît de fait, sans qu'on ait eu à le décider. Un échec remet
`entretiens` à zéro avec le reste — un mot réoublié doit revenir vite, pas dans
un an.

**Les libellés suivent l'état réel de la carte**, au lieu d'afficher 16 en dur :
le bouton annonce 16 jours, puis 35, puis 90.

⚠️ **Trois textes devenaient faux et ont été réécrits dans les cinq langues** —
`mastery_toast`, `carte_maitrise_titre`, `srs_aide_apres` promettaient un retour
« tous les {n} jours ». Les laisser aurait fait mentir l'app sur son propre
fonctionnement, exactement ce qu'on reproche à un bouton qui promet trop.

**Et les libellés des trois boutons sont devenus concrets**, à sa demande :
« retour dans 2 minutes », « retour dans 10 minutes », puis **« sort du paquet ·
demain »**. L'ancien « dans quelques cartes » était exact sans être clair : rien
ne disait si le mot revenait **aujourd'hui**. C'est la seule chose que
l'apprenant ne peut pas deviner, et c'est maintenant la seule que le libellé
affirme.

⚠️ **Correction d'une idée reçue au passage :** « Je savais » ne fait pas
toujours sortir le mot du paquet. À la **première** réussite il revient dix
minutes plus tard, dans la même séance — c'est le palier d'apprentissage. Ce
n'est qu'à partir de la deuxième qu'il part vraiment, et les libellés le disent
désormais chacun à leur tour.

**Vérifié :** `tests/essai_plafond.js` porte 6 contrôles de plus (24 au total) —
l'échelle d'entretien, son plafonnement au dernier barreau, et le fait qu'elle
ne redescende jamais. Plus `verifier.py`, 14 033 contrôles.

**Reste ouvert :** le NOM du troisième bouton. Il s'appelle encore « Je connais
déjà ce mot », qui se confond avec « Je savais ». Proposé : « Je le sais par
cœur », ou « Trop facile ». Non tranché.

---

## 10 septembre 2026 — l'absence ne punit plus (v523)

**Ce qui a déclenché ça :** *« ça peut nous mener à décourageant, parce qu'après
plusieurs jours le paquet est vraiment gros »*. J'ai mesuré au lieu d'en
discuter — `tests/charge.py`, nouveau : après 30 jours de travail régulier sur
l'A1, **une semaine d'absence laisse 285 cartes échues**, deux semaines en
laissent 390, et au-delà ça plafonne à 405 (tout ce qui est commencé). Trente-
cinq minutes sans respirer : c'est le mur qui fait fermer l'application.

⚠️ **Au passage, la même mesure a corrigé un chiffre que j'avais avancé au doigt
mouillé.** J'avais annoncé « 120 à 150 cartes par jour en régime établi » sur
l'A1. C'est faux : la journée la plus chargée fait **75 cartes** (jour 28), et
la moyenne après le premier mois tombe à **24**. L'écart avec les 200 cartes
d'Anki s'explique : leur avertissement vise un paquet **sans fin**, alors qu'un
niveau est fini — l'A1 s'épuise au 54ᵉ jour à 15 mots neufs. **Le chemin par
niveau ne rend pas seulement la progression lisible : il plafonne la charge par
construction.**

**La solution retenue est celle de Jacques, et elle vaut mieux que la mienne.**
Je proposais un plafond de révisions ; lui a déplacé la question : *« augmenter
le paquet seulement lorsque je viens, et non automatiquement quand on ne se
connecte pas pendant quelques jours »*. Mécaniquement, **l'échéance cesse d'être
une quantité pour devenir un ordre de priorité**. La séance fait toujours
40 cartes, qu'on revienne après un jour ou après un mois. Le nombre 285
n'apparaît jamais.

- `cartesDeSession()` sert les échues **les plus en retard d'abord**, plafonnées
  à 40, puis complète avec des mots neufs **seulement s'il reste de la place**.
- `retardEnAttente()` compte ce qui n'est pas entré. ⚠️ **Ce nombre ne va pas à
  l'accueil** — c'est exactement le chiffre qui punit. Il est destiné au ⓘ.
- « **En faire 20 de plus** » sur l'écran de fin, avec la même priorité : le
  retard d'abord, les mots neufs seulement s'il n'y en a plus. Éponger du retard
  ne consomme pas la dose du jour — ce sont des mots déjà rencontrés.

⚠️ **Et les libellés ont dû changer de nature, sur une remarque de Jacques.**
Avec une séance plafonnée, l'app **ne peut plus promettre « demain »** : un mot
échu demain peut ne pas passer s'il y a 40 cartes plus en retard devant lui. La
date n'est plus une promesse, c'est un **plancher** — d'où « pas avant 3 jours »,
et « **pas avant la prochaine séance** » au palier de +1 jour, qui parle en
séances comme l'apprenant les vit. Aux paliers suivants, « prochaine séance »
serait faux : la séance de demain ne verra pas un mot programmé à 7 jours.

**Vérifié :** `tests/essai_plafond.js` porte 31 contrôles — dont les 300 cartes
en retard ramenées à 40, l'ordre du plus en retard d'abord, le supplément qui ne
resert pas ce qui vient d'être vu, et le fait qu'il bascule sur des mots neufs
quand le retard est épongé. Plus `verifier.py`, 14 033 contrôles.

---

## 10 septembre 2026 — parler en séances, et un bouton qui ne se confond plus (v524)

**Ce que cette version règle, c'est la question laissée ouverte deux heures plus
tôt** (entrée v522) : le nom du troisième bouton. Il s'appelait « Je connais
déjà ce mot », qui se confond avec « Je savais » — les deux disent *je sais*. La
distinction à porter est un **degré**, pas un fait. Il s'appelle désormais
« **Je le sais par cœur** » dans les cinq langues.

**Et les paliers d'apprentissage parlent en séances.** Les échéances de 3 et
7 jours s'annoncent « dans quelques séances » : l'apprenant vit des séances, pas
un calendrier. ⚠️ **Le libellé est VAGUE à dessein** — un compte précis serait
faux, « pas avant 3 séances » tombant dès qu'on saute deux jours et qu'on revient
à la deuxième séance. Ce qu'il perd, la différence entre 3 et 7 jours, les
pastilles le disent déjà.

⚠️ **L'entretien garde les jours.** « Dans quelques séances » pour un mot
programmé à deux ans serait un mensonge, pas une approximation.

---

## 10 septembre 2026 — « 40 est trop bas » : simuler ce que la séance SERT

**Une mesure qui corrige la mesure de la veille.** `charge.py` simulait la
**demande** : il annonçait « A1 fini au 54ᵉ jour » en supposant que tout était
traité le jour même. Faux depuis la v523 — la séance est plafonnée à 40, donc le
surplus attend. `tests/charge_plafond.py` (nouveau) simule ce que la séance
**sert** : à 15 mots neufs par jour, l'A1 demande **107 jours et non 54**, et la
séance est **pleine 88 jours sur 107**.

⚠️ **Et augmenter la dose de mots neufs ne sert presque à rien** : de 10 à 25 par
jour, on gagne quatorze jours sur cent quinze. Ce n'est plus la dose qui
commande, c'est le plafond — les révisions mangent la séance. Le vrai levier est
la **taille de la séance** : 30 cartes → 147 jours ; 60 → 70 ; 80 → 54 jours,
zéro journée pleine, zéro carte en attente.

Le plafond devait protéger du retour d'absence (285 cartes). À 40 il freine tous
les jours au lieu de ça. **Réglage à revoir — décision de Jacques**, qui a
tranché à la v534 en le liant à l'objectif du jour.

⚠️ **Au passage, un défaut dans mon lecteur, pas dans la donnée.**
`funktionswort.json` est rangé par famille grammaticale, mais chaque entrée
porte son niveau CECR. Mon lecteur les rangeait sous leur **famille**, ce qui a
fait croire qu'ils n'en avaient aucun — et failli les verser tous en A1, alors
qu'« obwohl », « sodass » et « indem » y sont à juste titre en B1. Corrigé,
`frequence.json` régénéré. Le vrai compte : A1 860, A2 1 198, B1 2 980,
B2 1 003, C1 1 663 — **7 704 entrées**.

---

## 10 septembre 2026 — une porte unique pour le vocabulaire (v525)

**L'accueil comptait dix-sept tuiles**, chacune ouvrant un panneau où il fallait
encore choisir un niveau puis un mode. Un rectangle pleine largeur, sous la carte
de progression, donne désormais la séance directement : **aucun choix avant de
travailler**. Les dix-sept tuiles restent en dessous.

**L'assembleur est le vrai morceau.** Chaque catégorie range son niveau
ailleurs : les noms dans `themes.json` par thème ET par niveau, les verbes en
objets avec `.niveau`, les adjectifs en tableaux case 3, les adverbes,
expressions et six familles de mots-outils en case 8. Une **table déclarative**
plutôt que dix `if`, pour qu'ajouter une catégorie demain soit une ligne et qu'on
ne puisse pas en oublier une en silence.

Les mots neufs sortent par **fréquence** (`frequence.json`, chargé à la demande :
la séance marche sans lui). ⚠️ On compare des positions **relatives** dans chaque
catégorie, jamais deux rangs bruts.

⚠️ **Et les mots neufs n'arrivent pas par thème par défaut.** Sur treize études
recensées, six concluent que grouper des mots sémantiquement proches à la
première rencontre **freine** l'apprentissage (Tinkham, Waring, Erten & Tekin) ;
aucune ne montre que le thème aide à ce moment-là. C'est un coût, pas un danger —
le thème reste une porte secondaire.

---

## 10 septembre 2026 — le bandeau, sept fois repris (v526 à v533)

**Sept versions en une soirée sur un seul bloc de quarante pixels**, presque
toutes parties d'une remarque de Jacques. Elles se lisent mieux ensemble.

**v526 — le niveau est libre, et les révisions traversent.** Le vocabulaire n'est
pas cumulatif comme la grammaire : on peut suivre un cours de B1 sans connaître
tout l'A1, et imposer l'A1 demanderait vingt-deux séances pour **écarter** des
mots déjà sus. ⚠️ **Le défaut signalé par Jacques** : les révisions étaient
enfermées dans le niveau choisi — un mois de travail sur l'A1 aurait disparu de
la séance le jour du passage à l'A2, l'oubli par changement de menu.
`cartesDeSeance()` lit désormais **deux paquets** : les échéances de tous les
niveaux, les mots neufs du niveau choisi seulement. ⚠️ **La dose de mots neufs
reste GLOBALE** — un compteur par niveau permettrait d'en prendre soixante-quinze
en passant de A1 à C1.

**v527 puis v528, v529 — la pastille disait moins que ce qu'elle décide.** « A1 »
seul laissait croire que toute la séance était de ce niveau. Trois versions pour
trouver la phrase : « 40 cartes · mots nouveaux en A1 », puis « Nouveau
vocabulaire : A1 », puis la phrase entière — « **Nouveau vocabulaire en
provenance du niveau** ». Elle est longue, mais c'est la seule chose que
l'étudiant ne peut pas deviner. **Deuxième fois dans la journée qu'un libellé
promettait autre chose que ce que le code fait.**

**v528 — trois reproches, tous fondés.** L'icône de gauche coûtait de la hauteur
sans rien dire de plus que le titre : retirée. Les « petites barres » du thème
obligeaient à cliquer pour savoir où elles menaient — **un pictogramme seul est
une devinette**, remplacé par le mot « Par thème ».

**v530 — « ça prend presque la moitié de la page ».** ⚠️ La cause n'était pas le
padding : la classe `.orb` impose `aspect-ratio:1`, ce qui convient à une tuile
d'un tiers de largeur ; étendue aux trois colonnes, elle en faisait un **carré de
la largeur de la page**. Aucun réglage de marge ne pouvait le rattraper — je
réduisais les marges d'un carré dont la hauteur se calculait sur sa largeur.

**v531 — « un encadré rouge ».** Pas de rouge : dans les conventions d'interface
il code l'erreur et la suppression, donc l'employer pour l'action à faire envoie
le signal inverse ; et pour les 8 % d'hommes daltoniens au rouge-vert la
distinction disparaît. Le signal fiable est le **remplissage** — un seul bloc
plein par écran, tout le reste en contour. `#2f62d6` et non `#3b6fe0` : le blanc
sur ce bleu passe le seuil AA de 4,5:1 à 12 px.

**v532 — le mode nuit effaçait ce remplissage.** `body[data-theme="dark"] .orb` a
une spécificité plus forte que `.orb-seance` : la surface sombre gagnait et le
bandeau redevenait une tuile parmi les autres.

**v533 — « Ma séance du jour · 0 carte » à l'ouverture.** Signalé par Jacques, et
c'est le **même défaut que l'anneau de progression avait déjà eu** : le bandeau
se dessinait avant l'arrivée de `themes.json` et des autres. Rappel à la fin de
`loadThemesJson()`, **aux deux sorties, succès et échec**. Tant que les données
manquent, le bandeau affiche sa phrase d'attente — ⚠️ **un zéro erroné est pire
qu'une absence de chiffre.**

---

## 11 septembre 2026 — un seul nombre commande la journée (v534)

⚠️ **Deux nombres se contredisaient**, et c'est Jacques qui l'a vu. La v523
posait une séance de 40 en dur, à côté d'un objectif quotidien réglable que l'app
affichait déjà : quelqu'un dont l'objectif était à 100 voyait « 7 / 100 » sur une
séance qui s'arrêtait à 40. **L'app fixait une cible et empêchait de
l'atteindre.**

La séance prend désormais **le solde de l'objectif du jour**. Le dénominateur
affiche donc toujours ce que la séance contient vraiment, et « en faire 20 de
plus » **allonge la barre** au lieu d'éloigner la cible. Un plafond dur à 140
subsiste, pour qu'un réglage extrême ne remette pas le mur du retour d'absence.

**Et la grammaire sort de la barre du jour.** *« Exercice de grammaire, c'est un
plus, ce n'est pas une obligation à chaque jour. »* Sinon une journée de
grammaire remplissait une barre qui annonce des cartes, et **raccourcissait la
séance du lendemain**.

⚠️ **Mais la série de jours compte toujours la grammaire** : quelqu'un qui a
passé une heure sur le Perfekt a travaillé, et lui casser sa série pour avoir
choisi l'autre porte serait une punition. `recordDailyActivity()` prend un
paramètre — `false` alimente la série sans toucher à l'objectif.

**Vérifié :** `tests/essai_plafond.js`, 36 contrôles.

---

## 11 septembre 2026 — la carte de progression cesse d'accueillir par une fraction (v535)

Trois échelles de temps, et aucune fraction du dictionnaire : la **barre du
jour** (« 7 / 100 », remise à zéro chaque matin), la **série**, et les **cumuls**
— mots rencontrés · mots maîtrisés · exercices de grammaire.

⚠️ **« 7 / 100 » est le cadre de référence qui manquait à tous les compteurs
essayés avant lui** : il se comprend sans explication, là où « 98 mots » ne se
compare à rien. C'est aussi le seul dénominateur qui a le droit d'être là —
petit, proche, et il ne mémorise rien.

⚠️ **RIEN N'A ÉTÉ SUPPRIMÉ, TOUT A ÉTÉ DÉPLACÉ.** `updateHomeStatsPanel()` écrit
toujours dans `globalRingFill`, `globalRingLevel`, `globalRingNum` et
`weeklyMomentumChip` : les retirer aurait cassé la mise à jour **en silence**, et
le fichier portait déjà cet avertissement. Le cercle « A1 · 12 % » passe **dans**
le panneau ⓘ — sa valeur est juste, c'est sa place qui était fausse : il avance
de 0,22 % par mot et ne bouge pas avant le 11ᵉ jour. « Cette semaine » est
masqué : il mesure une **vitesse**, donc il s'effondre après des vacances alors
que rien n'a été perdu.

**Les libellés évitent le vocabulaire interne.** Ni « acquis » (acquis quoi ?),
ni « jeux solides ». Et « **exercices de grammaire** » plutôt que « règles » — on
peut lire une règle sans rien faire, ce sont les exercices qui comptent, remarque
de Jacques.

**Reste indéfini :** « solide ». Le critère provisoire est deux séries sans
erreur (Serfaty 2024), et le magasin v519 range assez de faits pour en changer
sans redemander à personne de tout refaire.

---

## 11 septembre 2026 — le vocabulaire quitte les tuiles (v536)

Ce qui part, c'est la **révision générique** de vocabulaire : « Réviser mes
mots », « par niveau », « au hasard », et les sept boutons « VOCABULAIRE : … »
des écrans de leçon. La séance du jour est désormais la porte unique.

⚠️ **RIEN N'EST SUPPRIMÉ.** Tout passe par `VOCAB_DANS_TUILES` : une ligne à
remettre à `true` et les dix-huit portes reviennent à l'identique. **Demande
explicite de Jacques**, et prudence élémentaire — l'assembleur des dix catégories
n'a pas encore tourné une semaine, et ces portes sont le filet.

Les **dictées ne sont pas filtrées** : une dictée est un exercice, pas une
révision générique. Les leçons non plus.

⚠️ **Et les sept boutons des écrans de leçon ne passent pas par
`renderOrbPanel()`** : le filtre des options ne les voyait pas, et c'est par là
que les flashcards des nombres restaient accessibles. **Signalé par Jacques.**

---

## 11 septembre 2026 — la légende décrivait une carte qui n'existe plus (v537)

Elle nommait quatre repères — la flamme, le cercle, la courbe, la cible. Depuis
la v535 la carte porte une barre du jour, une série et trois comptes cumulatifs.
Quelqu'un qui ouvrait le ⓘ n'y reconnaissait plus rien.

Six entrées, **dans l'ordre de lecture de la carte** : une légende qui énumère
dans un autre ordre que ce qu'elle explique oblige à chercher, et personne ne
cherche. Chacune dit aussi ce qui n'est pas devinable — que le cercle ne bouge
pas avant le 11ᵉ jour et que c'est normal, que « mots rencontrés » ne redescend
jamais, que « mots maîtrisés » peut en perdre un si un mot est oublié à son
contrôle.

**`tests/cles_langues.py` (nouveau)** vérifie que chaque clé existe dans les
**cinq** langues. `verifier.py` ne comparait que le français et l'anglais : le
turc, l'ukrainien et le persan sont arrivés plus tard, et rien ne disait qu'une
clé posée aujourd'hui y arrivait aussi. ⚠️ **Une clé manquante ne casse rien** —
`t()` renvoie la clé elle-même, et l'écran affiche `compte_rencontres` à un
lecteur ukrainien. Verdict : 937 clés, cinq langues, aucune manquante.

⚠️ **L'analyseur a dû être corrigé deux fois avant qu'on puisse le croire** : il
laissait le bloc persan courir jusqu'à la fin du fichier (135 fausses absences)
puis ne lisait que la première clé des lignes qui en portent deux (90 autres).
**Un contrôle qui accuse à tort est pire que pas de contrôle.**

---

## 11 septembre 2026 — un texte d'aide citait un bouton renommé (v538)

**Trouvé en rattrapant ce journal**, pas à l'usage. La v524 a renommé le
troisième bouton « Je le sais par cœur » dans les cinq langues — mais
`progress_info_deja`, le paragraphe du panneau ⓘ de la progression, citait encore
l'ancien nom **dans les cinq langues** : « Je le sais déjà », « I already know
this », « Bunu zaten biliyorum », « Я вже це знаю », et son équivalent persan.

C'est exactement le défaut de la v537 — une aide qui décrit un écran disparu — et
il a survécu treize versions parce qu'un renommage cherche le **libellé**, jamais
les textes qui le **citent**. `verifier.py` ne peut pas le voir : les deux
chaînes sont valides, elles ne se contredisent que pour un lecteur.

⚠️ **Ce qui rendrait le contrôle possible** : qu'un texte d'aide ne recopie
jamais un libellé mais le compose depuis sa clé, comme la v535 l'a fait en
réutilisant `srs_aide_echelle` mot pour mot. Non fait ici — cinq langues à
recomposer pour une phrase — mais c'est la règle à suivre au prochain texte
d'aide écrit.

---

## 11 septembre 2026 — « je vois seulement dictée » : ce que la v536 avait vidé (v539)

**Le retour, mot pour mot :** *« Peux-tu me rappeler les sections qu'on avait
dans les noms ? Parce que là maintenant, je vois seulement dictée. »* Puis la
même question pour les verbes et les adverbes.

C'était exact, et c'était un **effet secondaire de la v536**. La tuile « Noms »
avait cinq entrées ; le filtre en a masqué quatre. Il restait **une dictée seule
sous un titre qui en promet beaucoup plus** — et Noms était la plus exposée des
tuiles, parce qu'elle n'a ni leçon ni exercice propre pour amortir le retrait.

### Ce que Jacques a demandé, puis corrigé

**Premier tour :** rendre à Noms « Parcourir par niveau » et « Parcourir par
thème », garder masqués « Réviser mes mots » et « Mots aléatoires ». Sa
formulation de la distinction : *« ce n'est pas un simple retour en arrière,
c'est une correction UX de l'effet secondaire de v536 — v536 a correctement
retiré les actions génériques, mais n'a pas vérifié si chaque tuile conservait
suffisamment d'actions propres à son domaine »*.

⚠️ **Deuxième tour, et c'est lui qui a eu raison contre ma mise en œuvre :**
*« c'est un peu inconsistant de le faire seulement pour les noms et pas les
verbes, les adjectifs et les adverbes »*. J'allais réparer **une tuile**, ce qui
aurait laissé les mêmes portes fermées ailleurs **sans raison qu'on puisse dire
à voix haute** — le pire des états, parce qu'il se défend au cas par cas et
jamais dans son ensemble.

### La ligne de partage, et elle était déjà écrite dans le code

En classant les dix-huit actions masquées, la frontière s'est révélée exacte et
sans exception : **les six `open…` ouvrent un SOMMAIRE**, un écran où l'on
choisit (les niveaux, les 197 thèmes, les huit familles d'adverbes) ; **les
douze `start…` posent une carte** devant l'apprenant tout de suite.

**Un sommaire n'est pas une révision générique.** Ce que la séance du jour
remplace, c'est le paquet qu'on se sert sans avoir rien choisi — pas la
consultation. `ACTIONS_VOCABULAIRE` ne contient donc plus que les douze
`start…`, et **`verifier.py` refuse maintenant qu'un `open…` y entre**.

État final des cinq tuiles de vocabulaire : Noms (par niveau · par thème ·
dictée), Verbes (par niveau · dictée · par temps · wissen ou kennen), Adjectifs
(par niveau · dictée · déclinaison), Adverbes (les quatre, inchangée),
Expressions (leçon · vocabulaire — elle était tombée à une seule entrée elle
aussi, ce que personne n'avait vu).

### Les deux règles qu'il a demandé d'inscrire

**1. Toute modification de `ACTIONS_VOCABULAIRE` se juge sur l'ÉTAT FINAL DE
CHAQUE TUILE, jamais sur la constante seule.** La constante se lit d'un coup
d'œil ; ce qu'elle laisse dans chaque panneau ne se lit pas. `verifier.py` porte
désormais ce contrôle : il reconstruit les seize panneaux, applique le filtre, et
échoue si l'un descend sous deux entrées.

⚠️ **Il a trouvé « Expressions » à la première exécution** — une tuile vidée que
ni Jacques ni moi n'avions remarquée, alors qu'on parlait précisément de ça.
C'est la justification de ce genre de contrôle en une ligne.

⚠️ **Et il dit qui a vidé la tuile.** « Nombres » et « Ordre des mots » n'ont
qu'une entrée **depuis toujours** : les compter comme des victimes de la v536
lui ferait porter des défauts qu'elle n'a pas commis. Ils sortent en
avertissement — *un menu d'un seul élément est un bouton déguisé* — et restent
un chantier ouvert, pas une régression.

**2. Un renommage doit chercher les textes qui CITENT le libellé, pas seulement
la clé qui le produit.** C'est le défaut de la v538, trouvé la même heure :
`progress_info_deja` citait « Je le sais déjà » treize versions après que le
bouton eut été renommé. `verifier.py` ne peut pas le voir — les deux chaînes sont
valides, elles ne se contredisent que pour un lecteur. ⚠️ **La parade n'est pas
un contrôle, c'est une habitude** : composer la citation depuis la clé, comme la
v535 l'a fait en réutilisant `srs_aide_echelle` mot pour mot, plutôt que de
retaper le libellé dans cinq langues.

**Vérifié :** `verifier.py`, 14 149 contrôles, 2 avertissements (les deux tuiles
à une seule entrée, connues).

---

## 11 septembre 2026 — « Quel article ? », la première activité propre des Noms (v540)

**D'où vient la demande :** *« Qu'est-ce qu'on pourrait ajouter comme contenu
pédagogique pour les noms ? »*, après que la v539 eut rendu à la tuile ses
parcours. La question était juste : Noms **n'avait aucune activité à elle**.
C'est exactement pourquoi la v536 l'avait vidée — il n'y avait rien à garder
quand on retirait le vocabulaire générique.

Cinq pistes proposées, **deux retenues**, et le tri s'est fait sur des faits
plutôt que sur des goûts.

### Ce que la donnée permettait déjà

⚠️ **`genre` et `pluriel` sont présents sur les 4 209 noms, à 100 %.** Formes
complètes, pas des suffixes : `Vater → Väter`. L'exercice ne demandait donc
**aucune nouvelle donnée** — et c'est toujours la donnée qui coûte, jamais
l'exercice. L'atelier existait aussi : `startExerciseSet()` prend un tableau, et
les 170 exercices d'articles du Kasus sont eux-mêmes *générés* par
`construireExercicesArticles()`.

### Le défaut qu'on a évité : un score qui félicite l'ignorance

⚠️ **Nos noms se répartissent en die 2 048 · der 1 380 · das 771.** Sur un
tirage naturel, **répondre « die » à toutes les questions donne 48,8 %** — et
l'app annoncerait « la moitié » à quelqu'un qui ne sait rien. C'est le même
mensonge que le bandeau « 0 carte », en plus flatteur.

**Le tirage est donc en tiers égaux : dix `der`, dix `die`, dix `das`.** Le
plancher redescend à 33 %, le hasard réel d'un choix à trois, et le score
redevient une mesure. `tests/essai_article.js` vérifie les deux chiffres sur les
vraies données, pour que la prochaine « simplification » du tirage se fasse voir.

L'ordre de préférence reste celui de `cartesDeSession()` — ce que la personne
travaille en ce moment passe devant — **puis** l'équilibre se prend dedans : la
familiarité d'abord, l'équilibre par-dessus.

### Ce qu'on n'a PAS ajouté, et pourquoi

⚠️ **« Décliner le nom dans la phrase » existe déjà** : 170 exercices dans la
tuile Kasus, 30 par cas plus un mélange de 50. Le remettre dans Noms aurait été
la duplication que la v481 a dû défaire — deux copies d'une leçon, et personne
ne sait plus laquelle corriger.

**La frontière propre est ailleurs, et elle est nette :** Kasus enseigne à
**décliner un genre déjà connu** (`der Mann` → `den Mann`) ; savoir **que Mann
est masculin** est un autre fait, et aucun exercice ne l'enseignait. C'est la
seule connaissance qui appartienne au nom lui-même, donc à cette tuile et à
aucune autre.

**Sur l'idée adaptative** — pratiquer `Mann + Akkusativ` plutôt que `Mann` —
elle est la meilleure du lot, mais elle ne tient pas sur le mot : avec 4 209
noms, la preuve par couple (mot × cas) ne s'accumulerait jamais. Ce qui est
mesurable, c'est le **patron** (masculin + Akkusativ), soit douze cases au lieu
de 16 836. À faire seul, plus tard, sur le magasin de la v519.

### Le défaut trouvé à l'écran, et pas par un contrôle

⚠️ **« Das Baby » s'affichait avec une majuscule** juste au-dessus d'une
explication qui dit « das Baby » et de tuiles qui disent « das ». La règle
existante est juste — un blanc qui ouvre une **phrase** prend la capitale,
`___ Mann ist alt.` attend `Der Mann ist alt.` — mais `___ Baby` n'est pas une
phrase : c'est une entrée de dictionnaire. **Sur l'écran dont le sujet EST
l'article, ce désaccord s'apprend.**

`enonceEstUnePhrase()` affine la règle aux quatre endroits qui la portaient.
**Vérifié avant de la changer** : sur les 1 682 questions d'`exercices.json`,
les 103 qui commencent par le blanc contiennent toutes un point — le correctif
ne touche donc rien d'existant. Le banc d'essai tient les deux cas dans la même
main, parce qu'ils vivent dans la même ligne de code.

### Vérifié

- `tests/essai_article.js` (nouveau) : 21 contrôles sur les **vraies** données —
  l'équilibre, les cinq langues sur chaque question, la bonne réponse comparée
  au genre réel, le pluriel dans l'explication, le tiret des noms qui n'en ont
  pas, les cinq genres doubles écartés, et la majuscule.
- Essayé **dans la vraie page**, l'exercice lancé pour de bon : « ___ Freundin »
  → « die Freundin · Pluriel : die Freundinnen ».
- `verifier.py` 14 167 contrôles, `cles_langues.py` 940 clés × 5 langues.

---

## 11 septembre 2026 — quatre cartes de progression, proposées (rien de décidé)

**La demande :** *« propose-moi visuellement et conceptuellement d'autres
tableaux de progression qui sont plus significatifs, en gardant à l'esprit
qu'ils doivent être simples et intuitifs et gratifiants et encourageants. »*

**Proposition publiée, avec maquettes :**
https://claude.ai/code/artifact/fce8202b-c54d-4f11-9c79-4e90c855f034

⚠️ **Rien n'est décidé et rien n'est codé.** Cette entrée existe pour que le
lien ne se perde pas et que le diagnostic ne soit pas refait dans six semaines.

### Le diagnostic, qui vaut plus que les quatre cartes

Les trois mesures problématiques de la carte actuelle partagent **un seul
défaut** : elles mesurent **l'état du savoir**, qui fluctue et qu'on ne contrôle
pas directement.

- le cercle « A1 · 12 % » avance de 0,22 % par mot — invisible avant le 11ᵉ jour ;
- « cette semaine » mesure une **vitesse**, donc s'effondre après des vacances ;
- « mots maîtrisés » peut **redescendre** quand un mot est oublié à son contrôle.

**Ce qu'une carte doit refléter à la place :** ce que la personne **a fait**
(qui ne redescend jamais) et ce qu'elle **vient de terminer** (qui arrive assez
souvent pour être ressenti).

### Les quatre règles à appliquer à toute mesure future

1. **Ça ne redescend pas.** Une mesure qui baisse pendant des vacances mesure une
   vitesse : sa place est dans le ⓘ, pas sur la carte.
2. **Le dénominateur s'atteint.** 17 mots, 1 850 mots avec une date : oui. Une
   fraction du dictionnaire : non.
3. **Ça bouge le jour même.** 0,22 % n'est pas un signe.
4. **Ça se lit sans légende.** Si le ⓘ est nécessaire au sens principal, c'est le
   libellé qu'il faut réécrire.

### Les quatre cartes, et leur coût réel

- **A · Les thèmes qui se remplissent.** Le dénominateur passe de 4 209 à **17**
  (taille médiane d'un thème) : un thème se finit en trois ou quatre séances,
  donc l'app a quelque chose à annoncer chaque semaine. 197 thèmes.
  **Données prêtes.** Rend au passage un usage aux thèmes, qui ne servent presque
  plus depuis que la séance du jour est la porte unique.
- **B · « Ce que tu peux dire maintenant ».** Des capacités concrètes plutôt que
  des noms de thèmes, avec « encore 9 mots » sur celles qui approchent. La plus
  forte des quatre. ⚠️ **Le risque est dans la promesse** : un énoncé trop large
  se paie à la première tentative réelle. **Demande du contenu neuf** — environ
  40 énoncés pour A1-A2, dans cinq langues.
- **C · Le mur.** Un carré par mot rencontré, aucun dénominateur : la carte ne
  peut que grandir. ⚠️ Canvas au-delà de 2 000 à 3 000 carrés, et une vignette
  des derniers plutôt que 4 209 poussières sur un téléphone. **Données prêtes.**
- **D · L'examen visé.** Le champ `pruefung` porte déjà **628 mots A2, 1 850 B1,
  1 541 DTZ**. Le seul grand dénominateur légitime, parce qu'il vient de
  l'examen que la personne a décidé de passer. Le plus proche de nos testeurs :
  la date d'examen organise leur année. **Données prêtes.**

**Ordre recommandé :** A tout de suite ; D quand un examen est choisi dans les
réglages (sans examen choisi, la carte ne s'affiche pas) ; C dans le ⓘ à la
place du cercle ; B plus tard, une fois les énoncés écrits et relus.

---

## 11 septembre 2026 — la carte D est retenue, et la semaine est retirée

**Décision de Jacques :** *« Je crois qu'on a la carte D. Je garderais juste le
premier rectangle en haut. Pour la semaine, il faudrait y repenser. »* Plus, sur
la structure : un petit rectangle d'objectif et **une vignette en mosaïque** sur
l'accueil, qui ouvre une vue par niveau puis par thème.

⚠️ **Toujours rien de codé.** Maquette à jour, même lien :
https://claude.ai/code/artifact/fce8202b-c54d-4f11-9c79-4e90c855f034

### ⚠️ Correction d'un chiffre que j'avais donné deux fois

J'annonçais « 628 mots A2, 1 850 B1, 1 541 DTZ » : **ce ne sont que les noms.**
Le champ `pruefung` est posé sur **toutes** les catégories. Les vrais
dénominateurs de la carte D sont **A2 1 093 · B1 2 998 · DTZ 2 601**.

### La semaine en sept carrés enfreignait la règle qu'on venait d'écrire

Jacques l'a vue le premier. Trois défauts, aucun réparable par le dessin :

- **le lundi matin elle s'effondre** — six carrés allumés redeviennent un, un
  jour où rien n'a changé ;
- **une fenêtre glissante ne récompense plus rien** — soixante jours et sept
  jours donnent la même image ;
- ⚠️ **elle rend l'absence visible sous forme de trous.** Une rangée à trois
  cases vides est un bulletin — exactement ce que la v523 avait cessé de faire.

**Ce qui la remplace :** « **34 jours travaillés** », un cumul qui ne redescend
jamais, avec **la série en petit et à droite**, et seulement quand elle est
vivante. Au retour de vacances le grand chiffre est intact et la petite mention
a disparu sans commentaire.

**La règle #1 est donc affinée :** non pas « ça ne redescend jamais » mais
« **ça ne redescend pas pour une raison qu'on ne peut pas nommer** ». Une série
cassée se comprend ; « cette semaine −40 % » après des vacances, non.

### Deux réserves sur le défilement au tap

- **Des pastilles plutôt qu'un défilement.** Avancer d'un niveau à chaque tap
  cache l'état et demande quatre gestes pour atteindre C1. **La v527 a déjà coûté
  trois versions sur ce point exact.** Les pastilles du bandeau de séance
  existent déjà.
- ⚠️ **Le niveau et l'examen sont deux axes.** « B1 le niveau » = 1 784 noms ;
  « B1 l'examen » = 2 998 mots toutes catégories. Les faire défiler dans le même
  rectangle recréerait la confusion de la v527 : l'examen se choisit **une fois**,
  dans les réglages.

### Ce que la structure de Jacques règle

**197 thèmes n'entrent pas sur une carte d'accueil, mais entrent dans un écran
entier.** La vignette ouvre : les cinq bandes de niveau, puis les tuiles de
thèmes du niveau ouvert. La carte A n'a donc plus besoin de place sur l'accueil —
et la carte B trouvera la sienne sous les thèmes, plus tard.

---

## 11 septembre 2026 — « finir ce thème », et le vocabulaire d'examen (v541)

**Demande de Jacques :** *« ajoute le bouton "finir ce thème" avec la carte D »*.

### ⚠️ La carte D a dû changer de forme : la v470 l'interdisait telle quelle

La maquette proposait « Objectif B1 · 486 / 2 998 », l'examen choisi dans les
réglages. **C'est exactement ce que la v470 a retiré**, et `cartesParMarque()`
porte l'avertissement en toutes lettres : elle savait filtrer par liste
(« Goethe A2 », « Goethe B1 et le DTZ »), elle a **perdu ce paramètre**, et le
commentaire dit *« ne pas remettre le paramètre »*. Extraire une liste
officielle, c'est reproduire une base que quelqu'un a constituée ; en offrir la
progression pas à pas, c'est la republier.

**La carte est donc bâtie sur l'AGRÉGAT** — les mots qu'au moins un programme
retient, **3 056** toutes catégories — qui ne reconstitue aucune liste en
particulier. Elle motive pareil : le dénominateur reste un chiffre qu'on ne
choisit pas soi-même, et il bouge à chaque mot neuf quel que soit son thème.

Affichage : « 400 / 3 056 », une piste à deux segments (sus · en cours), et
« 160 sus · 240 en cours · 2 656 à rencontrer ». **En contour, pas en plein** :
le seul bloc plein de l'accueil reste le bandeau de séance (v531).

### « Finir ce thème » : ce que la simulation a rendu possible

Le bouton n'apparaît que sur un niveau à **trois mots ou moins** de la fin.
Au-delà, ce serait un « travailler ce thème » de plus — il y en a déjà un, c'est
la pastille juste au-dessus. Ce qui rend celui-ci utile, c'est que le compte est
petit : « encore 1 mot » se lit comme une course de trente secondes.

⚠️ **Il ne passe PAS par `cartesDeSession()`, et c'est le point du bouton.** Le
tirage du jour plafonne les mots neufs à quinze : un jour où la dose est
épuisée, il renverrait zéro carte et le bouton ne ferait rien. On sert
exactement les un à trois mots qui manquent. La journée reste comptée juste :
`noterMotNeuf()` se déclenche à la première **réponse**, pas au tirage.

⚠️ **Et ça ne contredit pas la v525** : sa recherche porte sur les **premières
rencontres** groupées par sens. Aller chercher les deux derniers mots d'un thème
parcouru depuis un mois est un achèvement décidé, pas un groupement.

### Vérifié dans la vraie page

- La carte compte **3 056** mots marqués — le même chiffre que le comptage
  Python sur les fichiers, doublons écartés.
- Le bouton « Finir A2 · encore 3 mots » sur Familie sert exactement
  `Zwilling`, `Schwiegermutter`, `Schwiegervater` — les trois qui manquaient.
- ⚠️ **Le service worker sert `index.html` depuis le cache** : un simple
  rechargement montrait l'ancienne page et l'élément semblait absent. `?v=NNN`
  est le geste, comme prévu.
- `verifier.py` 14 190 contrôles, `cles_langues.py` 944 clés × 5 langues.

---

## 11 septembre 2026 — « Vocabulaire », qui se déplie par niveau (v542)

**Demande de Jacques :** appeler la ligne **« Vocabulaire »** plutôt que
« Vocabulaire d'examen », lui donner une flèche pour la déplier, et reprendre
les trois couleurs à chaque niveau — **vert ce qui est su, bleu ce qui est en
cours, le reste à rencontrer**.

### ⚠️ Et l'argument de droits est le sien, il est juste

*« Les mots qu'on a dans le vocabulaire, c'est une combinaison de Goethe puis
d'autres propositions. Donc au niveau des droits on est ok, parce qu'on ne
s'alimente pas seulement avec une école ou une orientation de pensée. »*

C'est exact, et ça règle la question pour les niveaux : **nos niveaux CECR sont
notre synthèse**, pas la liste de quelqu'un. Afficher « A1 612 / 860 » ne
reconstitue rien.

⚠️ **L'argument ne s'étend PAS aux marques `a2` / `b1` / `dtz`** : chacune *nomme*
un programme, et c'est précisément ce qui les isole — la combinaison qui protège
les niveaux n'existe pas pour elles. C'est d'ailleurs pourquoi la v470 laissait
passer l'agrégat : l'union des trois *est* une combinaison. La ligne de la v470
reste donc où elle est, et la carte d'examen garde sa forme agrégée.

**Distinction que j'avais écrasée**, et qu'il faut garder au clair pour la
prochaine fois : un **paquet** filtré par examen livre la liste mot par mot ;
un **compteur** par examen ne divulgue qu'un nombre. Ce ne sont pas la même
chose. La v470 a supprimé le paquet ; elle a aussi refusé le compteur, en toutes
lettres — et c'est ce refus-là qui reste à trancher si on veut « Objectif B1 ».

### La ligne repliée montre le NIVEAU, pas le total

⚠️ **« 486 sur 7 704 » aurait réintroduit la fraction du dictionnaire entier**,
exactement ce que la carte de la v535 avait chassé. Repliée, la ligne montre le
niveau courant — 860 mots en A1, une fin qui existe. Dépliée, les cinq niveaux,
qui totalisent bien 7 704 : rien n'est caché, c'est la mise en avant qui change.

**Trois états et pas deux**, à sa demande, et la raison tient : « su » seul ne
bouge pas avant le 11ᵉ jour. « En cours » bouge dès la première carte, et c'est
lui qui dit qu'il se passe quelque chose.

**Vérifié dans la vraie page :** « Vocabulaire · A1 · 612 / 860 », la flèche qui
pivote, les cinq lignes et la légende. `verifier.py` 14 213 contrôles,
`cles_langues.py` 948 clés × 5 langues.

---

## 11 septembre 2026 — la mosaïque : spécifiée, et cent deux tableaux candidats

⚠️ **Rien de codé.** Planche de sélection publiée, avec une démo réglable :
https://claude.ai/code/artifact/5fb458be-64cf-4824-8746-e4a05ce62f3f

### La spécification, telle que Jacques l'a arrêtée

- **Un carreau par carte traversée** — jugée, balayée, ou simplement passée.
  ⚠️ **Pas « par mot neuf »**, et la raison est mesurée : après quelques
  semaines la plupart des séances sont des révisions, et une image adossée aux
  mots neufs calerait des jours entiers — précisément quand l'étudiant travaille
  le plus.
- **Mille carreaux par image**, pas 500 : à 40 cartes/jour, une image tous les
  25 jours, soit **une vingtaine** sur une traversée A1→C1 de dix-sept mois.
  500 en demanderait 41. C'est la seule variable qui décide si le projet est
  finissable.
- **La couleur est libérée de tout sens** — c'est le déblocage, et il est de
  Jacques. Tant qu'elle codait « maîtrisé / en cours », l'image était
  impossible ; un carreau porte désormais le morceau d'image qu'il cache.
- **L'image se forme sur tous les niveaux confondus**, pas par niveau : ça suit
  la séance, qui traverse déjà tous les niveaux depuis la v526.
- ⚠️ **Plafond de 80 carreaux par jour.** Ce n'est pas de la police
  anti-triche : sans lui, mille cartes balayées en un quart d'heure terminent
  une image d'un coup et la collection entière y passe en une semaine. Il
  protège le rythme de la récompense, donc l'intérêt du dispositif.
- **Ordre de révélation éparpillé et figé**, tiré une fois puis mémorisé.

### Le cycle de vie, demandé par Jacques

Terminée → **elle reste quelques jours** à l'accueil → **annoncée une fois**
(trois notifications seraient du harcèlement) → **rangée dans la galerie**, qui
est ce qui porte la motivation sur la durée : une vingtaine de cases, gagnées en
couleur, les autres en silhouette.

### Le premier jour : du verre dépoli

⚠️ **Le problème qu'il a vu : une grille vide n'invite personne.** Sa
proposition — montrer le tableau en filigrane — tuerait la curiosité qu'il avait
lui-même nommée comme moteur. Le compromis retenu : **le carreau fermé est du
verre dépoli** (`backdrop-filter`), pas un cache opaque. On distingue les masses
et les couleurs, on ne reconnaît rien. Plus un **cadre** et un cartouche de
musée « Tableau 1 sur 20 » : un cadre vide se regarde, une grille vide non.

### Les images : la règle, et les deux pièges

**Ni vieux maîtres ni XVIIᵉ-XVIIIᵉ** — demande de Jacques : impressionnisme et
après. Cent deux candidats de vingt peintres du monde germanophone, de
l'impressionnisme allemand (Liebermann, Corinth, Slevogt) au Blaue Reiter, à Die
Brücke, au Jugendstil viennois.

⚠️ **Règle unique et vérifiable : peintre mort avant 1956** (plus de 70 ans),
ce qui couvre l'Europe, le Canada et le Royaume-Uni d'un seul critère. Münter
(2033) et Nolde (2027) sont écartés pour ça, malgré leur place au Blaue Reiter.

⚠️ **Deuxième piège, moins connu :** l'arrêt allemand Reiss-Engelhorn (2018) a
jugé qu'une **photo de musée** peut créer un droit neuf, même sur une œuvre du
domaine public. D'où : ne prendre que des images qu'une institution publie
elle-même en domaine public / CC0.

⚠️ **Et une leçon d'outillage :** l'Art Institute of Chicago a une belle API
mais son serveur d'images renvoie 403 à tout ce qui n'est pas un navigateur ; le
Met répond, mais sa collection est **vide** sur l'expressionnisme allemand (zéro
résultat pour Marc, Macke, Klee, Kandinsky, Kirchner, Beckmann). Wikimedia
Commons est la source qui marche — et il faut passer par son **API** pour
obtenir l'URL d'une vignette, la deviner renvoie 400.

**Je ne suis pas juriste** : la règle des 70 ans et la source institutionnelle
sont solides, mais une vérification de Jacques sur les images finalement
retenues reste la bonne prudence.

---

## 11 septembre 2026 — demande en attente : les règles de genre des noms

**Demande de Jacques, non commencée :** *« dans la partie noms, ce qui est
intéressant, c'est qu'il y a des règles — par exemple les noms qui finissent par
`-ung` sont toujours féminins. Donc indiquer les différentes règles, puis faire
des exercices avec les règles, et mélanger. Que ça soit accessible dans la tuile
Noms. »*

C'est le complément naturel de « Quel article ? » (v540) : celui-ci fait
mémoriser un genre à la fois, les règles font **deviner un genre jamais
rencontré**. `-ung`, `-heit`, `-keit`, `-schaft`, `-ion`, `-tät` sont féminins
sans exception utile ; `-chen` et `-lein` neutres ; `-er` d'agent masculin.

⚠️ **Et la remarque de Jacques sur `-e` est exactement le piège à traiter :**
« la majorité du temps c'est féminin » — donc `der Name`, `das Auge`, `der Käse`
existent. Une règle énoncée comme absolue alors qu'elle a des exceptions
enseigne une fausse certitude. Les règles doivent **porter leur taux** et leurs
contre-exemples, sinon elles nuisent.

**À vérifier avant d'écrire quoi que ce soit :** on a les 4 209 noms avec leur
genre — le taux réel de chaque terminaison est **mesurable sur nos propres
données**, pas à recopier d'une grammaire. C'est par là qu'il faut commencer.

---

## 11 septembre 2026 — le choix des images : trois planches, et deux erreurs rattrapées par la mesure

Trois planches publiées, 421 œuvres proposées en tout :

1. https://claude.ai/code/artifact/5fb458be-64cf-4824-8746-e4a05ce62f3f — 102 tableaux, la démo réglable de la mosaïque, le cycle de vie
2. https://claude.ai/code/artifact/cc2e6628-de30-4204-b635-00ee03b06578 — 118 de plus, classés par couleur mesurée
3. https://claude.ai/code/artifact/077d84a4-0e7e-4228-8d0f-36b6c1f34335 — 118 autres dont 26 Liebermann, plus 83 photochromes, et le sélecteur d'intensité

### Ce qui est décidé

- **Pas de vieux maîtres** : impressionnisme et après. Demande de Jacques.
- **Liebermann en quantité** — j'avais compris l'inverse au premier tour
  (« plus de Liebermann » entendu comme « fini Liebermann », parce que sa
  palette sourde collait mal à « j'aime quand c'est très coloré »). Corrigé :
  26 dans la troisième planche.
- **Intensité : « vif »** — autocontrast franc, +12 % de luminosité,
  **+45 % de saturation**, +10 % de contraste.
- ⚠️ **La retouche est CUITE dans le fichier**, pas appliquée en CSS : un
  filtre sur mille carreaux coûterait du GPU à chaque rendu sur téléphone.
  L'original reste sur Commons si on veut refaire le dosage.
- **Sélection de la planche 2, 22 images** : 202, 203, 212, 225, 232, 236, 241,
  257, 260, 261, 278, 281, 291, 301, 306, 307, 309, 311, 314, 315, 316, 317.

### ⚠️ La mesure de couleur a attrapé deux fautes que l'œil aurait laissées passer

La métrique de Hasler & Süsstrunk — écart-type et moyenne des oppositions
rouge-vert et jaune-bleu — a été introduite pour classer. Elle a surtout servi
de **garde-fou** :

- **34 « tableaux » étaient des gravures en noir et blanc**, ramenées par les
  catégories de Commons avec les peintures. Indice proche de zéro.
- ⚠️ **Et les 264 premiers « photochromes » l'étaient tous.** J'avais pris la
  collection Photoglob-Wehrli de la Bibliothèque nationale suisse, rangée sous
  `CH-NB-Photographs of X` : ce sont les photographies **d'atelier**, pas les
  photochromes. **Zéro n'a passé le plancher.** Sans la mesure, je publiais une
  planche grise en l'annonçant colorée.

Les vrais photochromes sont ceux de la Library of Congress, sous
`X on photochrome prints` et `Photochrom prints collection (X)`.

**Leçon générale, pas seulement pour les images :** un plancher qui rejette est
plus utile qu'un classement qui ordonne. Le classement m'aurait fait montrer les
images grises en dernier ; le plancher les a fait disparaître.

### L'outillage, pour la prochaine fois

- **Art Institute of Chicago** : belle API, mais le serveur d'images renvoie
  **403** à tout ce qui n'est pas un navigateur. Inutilisable en script.
- **Met Museum** : les images se téléchargent, mais la collection est **vide**
  sur l'expressionnisme allemand — zéro résultat pour Marc, Macke, Klee,
  Kandinsky, Kirchner, Beckmann.
- **Wikimedia Commons** : la source qui marche. ⚠️ Il faut passer par son
  **API** pour obtenir l'URL d'une vignette — deviner l'URL du thumb renvoie 400.
  Et l'en-tête `User-Agent` doit être descriptif, sinon refus.

---

## 12 septembre 2026 — les mosaïques sont en ligne (v543)

**Décisions de Jacques, toutes prises en cours de route et toutes gardées :**

- **un carreau par carte traversée** — jugée, balayée, ou simplement passée ;
- **700 carreaux** par image (la grille s'ajuste au format : 29 × 24 = 696 pour
  la première) ;
- **l'image se forme sur tous les niveaux confondus**, pas par niveau ;
- **le cadre est visible dès le premier jour** ;
- **trois séances** de trophée, et le nom qui apparaît ;
- **on peut toucher l'image pour l'avoir en grand** ;
- **la galerie garde ce qui a été atteint** ;
- **65 images, puis retour à la première.**

⚠️ **« Un carreau par carte traversée » et non « par mot neuf »** : après
quelques semaines la plupart des séances sont des révisions, et une image
adossée aux mots neufs calerait des jours entiers — précisément quand
l'étudiant travaille le plus.

⚠️ **La couleur libérée de tout sens est ce qui rend l'image possible.** Tant
qu'un carreau codait « maîtrisé » ou « en cours », il ne pouvait pas porter un
morceau de tableau. C'est le déblocage, et il est de Jacques.

### Le cartouche en trois temps

L'année à 40 %, le peintre à 70 %, le titre à la fin. Révéler un titre lettre
par lettre ne donnerait que du bruit — **un demi-mot allemand n'apprend rien**,
alors qu'on peut deviner un peintre avant de deviner un titre, et qu'il reste
une phrase entière à lire au moment de la récompense.

### Le verre dépoli

⚠️ **Le carreau fermé n'est pas un cache opaque.** Jacques proposait de montrer
le tableau en filigrane dès le départ ; ça aurait tué la curiosité qu'il avait
lui-même nommée comme moteur. Un cache opaque, lui, donne un écran mort. Le
`backdrop-filter` laisse voir **qu'il y a quelque chose** — au jour zéro, un
jardin vert derrière une vitre — et rien de plus.

### Deux défauts trouvés à l'essai, pas par un contrôle

⚠️ **Le trophée disparaissait avant sa première séance.** En remettant le
compteur à zéro dès l'achèvement, `fini` redevenait faux au rendu suivant. Le
compteur continue maintenant de monter, et c'est `seanceMosaiqueTerminee()` qui
le ramène en soustrayant la taille de l'image.

⚠️ **Et ce report est ce qui rend la récompense gratuite** : les carreaux posés
pendant les trois séances démarrent la mosaïque suivante. Vérifié : 50 carreaux
posés sous le trophée, la suivante ouvre à 50. Sans ça l'étudiant paierait trois
séances de progression pour avoir gagné quelque chose.

### Les images

65 tableaux, 9,6 Mo, dans le dépôt — chargés depuis GitHub raw comme
`themes.json`, donc le push qui publie les données publie les images. Rangs 1 à
23 dans l'ordre de Jacques, 24 à 65 mélangés à graine fixe.

⚠️ **Deux images ont dû être remplacées** : Commons n'avait le *Portrait Maria
Marc* qu'en 239 px et le *Landschaft am Meer* de Macke qu'en 270 px — plus petit
qu'un écran de téléphone. Remplacées par *Mädchen mit Katze II* (2139 px) et
*Three girls in yellow straw hats* (5929 px). ⚠️ Et **pas par *Sonniger
Garten***, pourtant proposé : il est déjà dans les 65 et serait revenu en
doublon.

**Vérifié dans la vraie page** : le cartouche aux quatre paliers, le cycle
complet du trophée sur trois séances avec report, la galerie à trois tableaux,
et le plein écran. `verifier.py` 14 254 contrôles, `cles_langues.py` 954 clés ×
5 langues.

---

## 12 septembre 2026 — la carte allégée, le glacis réglé (v545)

**Quatre remarques de Jacques, toutes justes, toutes appliquées.**

### « Trop d'informations dans le rectangle de progression »

Vrai, et il y avait pire qu'un encombrement : **un doublon**. « Aujourd'hui
0 / 30 » et « Objectif du jour 0 / 30 » affichaient **le même chiffre deux fois
dans la même carte**. Masqué.

Et les trois cumuls — mots rencontrés · maîtrisés · exercices — passent derrière
le ⓘ. ⚠️ Ils ne sont pas faux, ils sont **de trop à cet endroit** : la ligne
« Vocabulaire » juste dessous dit la même chose par niveau, avec un dénominateur
qu'on peut atteindre. Même traitement que l'anneau à la v535.

La carte tient maintenant en quatre blocs : le jour, les jours travaillés, le
vocabulaire, la mosaïque.

### « Ce n'est pas une image cachée en glacis, c'est la peinture en plus pâle »

⚠️ **J'avais confondu deux réglages qui font deux choses différentes.** Le
**flou** détruit la **forme** — c'est lui qui empêche de reconnaître le sujet.
Le **voile blanc** détruit la **couleur**. J'avais trop peu flouté et trop lavé :
on reconnaissait le tableau, en délavé.

Première correction : j'ai poussé les deux — et obtenu **un cadre blanc**, ce qui
est pire que tout, puisqu'une grille vide n'invite personne. Le bon réglage est
**flouter beaucoup, laver peu**, et même **rehausser** la saturation : on voit
des masses de couleur franches sans aucun dessin. C'est ça, du verre dépoli.

### « Le bleu, plus pâle, pour un meilleur contraste »

Le vert reste `#0F6E56` comme il l'a demandé ; c'est le bleu qui s'éclaircit à
`#6A9BEE`. Le contraste entre les deux segments passe de **1,13 à 2,23**, en
plus de la séparation de 2 px posée à la v544.

### « Dix carreaux d'avance, pour qu'on se dise qu'on construit quelque chose »

⚠️ **Une grille intacte se lit comme un départ à zéro ; dix carreaux ouverts se
lisent comme un chantier déjà commencé.** C'est une différence de nature, pas de
degré. Offerts une seule fois, à la création de l'état.

### Deux défauts trouvés à l'écran

- **Le ⓘ recouvrait « Ta galerie »** : il est en absolu au coin de la carte, et
  la mosaïque finit désormais là. Réserve de 34 px à droite.
- **« 1 jours travaillés »** : le pluriel se décide sur le nombre, et le mot vit
  dans cinq langues — d'où deux clés, pas un « s » ajouté à la main.

### Et le cumul de jours a remplacé la série

⚠️ **La série repartait à zéro dès qu'on saute un jour : elle punit l'absence**,
exactement ce que la v523 avait cessé de faire. « 34 jours travaillés » ne
redescend jamais. La série reste, en petit et à droite, et seulement à partir de
deux — « 1 d'affilée » n'est pas une série, c'est aujourd'hui.

⚠️ **Le compteur s'amorce depuis la série** pour les comptes déjà ouverts :
afficher « 0 jour travaillé » à quelqu'un qui en est à trente d'affilée serait
faux et décourageant. La série sous-estime, elle ne surestime jamais.

**Reste à faire :** les 22 textes de peintres, demandés et pas encore écrits.

---

## 12 septembre 2026 — quatre défauts signalés à l'usage (v546-v547)

⚠️ **Aucun des quatre n'aurait pu être trouvé par un contrôle.** Tous viennent
de Jacques regardant l'écran.

### 1. Le glacis n'existait pas sur son appareil

Le plus grave. Le verre dépoli reposait sur `ctx.filter = "blur(...)"`. **Safari
ne connaît cette propriété qu'à partir d'iOS 16.4 — et là où elle manque, elle
ne lève aucune erreur : elle est ignorée.** La « copie floue » devenait une copie
nette, et **toute la mosaïque s'affichait en clair dès le premier jour**. Le
mécanisme entier ne servait plus à rien, sans le moindre signe.

⚠️ **Invisible en développement, parce que mon navigateur, lui, l'avait.**

La parade ne dépend de rien : on dessine l'image dans une vignette de vingt
pixels, puis on la retire en grand — le lissage du navigateur fait le flou,
partout, depuis toujours.

### 2. « › » était le mauvais signe

Le chevron de la ligne « Vocabulaire » est un chevron de **navigation** : il
annonce qu'on quitte l'écran. Or la ligne se **déplie sur place**. ⚠️ **Un
mauvais signe est pire qu'un signe discret** — il promet autre chose. Remplacé
par un chevron vers le bas qui pivote, posé sur une pastille : un caractère
seul, même bien choisi, ne se lit pas comme un bouton.

### 3. Le zoom iOS qui s'ouvre tout seul

Deux touches rapprochées sur le « − » de l'objectif quotidien sont lues comme un
**double-tap**, et Safari zoome ; il faut ensuite pincer pour revenir. C'est le
même genre de piège que le plancher de 16 px des champs de saisie : une
commodité iOS qui se retourne contre l'app. `touch-action:manipulation` sur les
**contrôles seulement** — le défilement et le zoom volontaire restent intacts.

### 4. L'objectif changé ne changeait rien

Objectif mis à 40 dans les réglages, retour à l'accueil : toujours « / 100 ».
`updateGlobalProgress()` ne touche ni la carte du jour ni le bandeau, et rien ne
les rappelait avant le prochain démarrage. ⚠️ **Le bandeau était le plus grave
des deux** : depuis la v534 la taille de la séance **est** le solde de
l'objectif, donc il annonçait un nombre de cartes qui n'était plus le bon.

### Au passage, un cache qui mémorisait un échec

`chargerPeintres()` posait `PEINTRES = {}` **avant** le fetch. Après un seul
échec — réseau coupé, ou fichier pas encore publié — la garde renvoyait cet
objet vide pour le reste de la session. **Un cache qui retient un échec est pire
que pas de cache.**

### Et la mise en page comprimée

Image à gauche sur 42 %, cartouche et galerie à droite, jours travaillés remontés
sur la ligne de la barre du jour. La carte gagne une soixantaine de pixels.

**Les 22 notices de peintres sont en ligne** — une par artiste, affichée au
trophée, en plein écran et dans la galerie, jamais sur la carte d'accueil.

---

## 12 septembre 2026 — cinq encombrements retirés (v548)

**Tout vient de Jacques regardant l'écran, et les cinq sont des retraits.**

⚠️ **« On voit beaucoup trop l'image. »** Le glacis était trop fin : on devinait
le sujet. La finesse se règle à un seul endroit — la taille de la vignette
intermédiaire. De `L/34` à `L/90` : la vignette passe d'une trentaine de pixels
à une dizaine, et il ne reste que la répartition des masses de couleur.

⚠️ **« Chercher un mot » promettait une saisie qui n'arrive jamais.** Toucher
cette barre ouvre un **autre écran** — on n'y tape rien sur place. Un grand
champ pour un simple lien : hauteur réduite de moitié.

⚠️ **Le cumul de jours n'a rien à faire sur la ligne du jour.** C'est une mesure
de **fond** — elle bouge d'une unité par jour au mieux — posée sur la ligne qui
change à chaque carte. Passée derrière le ⓘ, avec les cumuls de la v545.

⚠️ **Et le bandeau répétait le compte de la carte.** « 2 / 40 » au-dessus,
« 38 cartes » en dessous : la même chose dite deux fois dans le même écran. On
garde le seul endroit où le chiffre est **complet** — celui qui montre aussi ce
qui est déjà fait — et le bandeau redevient ce qu'il est, une porte. Le libellé
du niveau reste : il n'est ailleurs nulle part.

⚠️ **Le chevron était un caractère, pas un dessin.** « ⌄ » se pose où sa police
décide : il tombait haut dans la pastille, et aucun calage vertical ne le
centrait d'une police à l'autre. Un SVG occupe exactement sa boîte — il se
centre par construction et grossit sans devenir flou.

**Note sur l'objectif quotidien** : il n'a jamais été figé par jour.
`getDailyGoalTarget()` lit le réglage à chaque appel ; c'était bien l'absence de
rafraîchissement de l'accueil, corrigée en v547.

---

## 12 septembre 2026 — l'accueil réduit à l'essentiel (v549-v550)

**Une longue série de remarques de Jacques, toutes à l'écran, toutes des retraits
ou des déplacements.** La carte de progression est passée de six blocs à deux.

### Ce qui a bougé

- **Le compte du jour quitte la carte pour le bandeau** : « Ma séance du jour
  0 / 40 ». Il n'a de sens qu'au moment de travailler, et c'est là qu'on le voit
  monter. Sa barre disparaît avec lui.
- **La recherche monte sur la ligne du salut.** Elle occupait une ligne entière
  pour un geste qui mène ailleurs.
- **Le ⓘ ouvre un ÉCRAN**, plus un panneau qui se déplie. Déplié dans la carte,
  il fallait retrouver le ⓘ et le retoucher pour refermer — un geste que
  personne ne devine. Et il contient désormais les règles de la séance.
- **L'étiquette de version passe en pied de page.** Calée en absolu au coin de
  la carte, elle s'est retrouvée **par-dessus le tableau** quand la mosaïque est
  arrivée.
- **Le tableau a un vrai cadre** : coins carrés, filet sombre, liseré clair —
  un passe-partout, pour quatre pixels.

### ⚠️ Trois défauts que j'ai créés en corrigeant

**1. J'ai cassé la carte en déplaçant les cumuls.** Pour sortir le bloc, j'avais
cherché sa fin avec `s.index("        </div>\n", debut)` — qui trouve la
fermeture du **premier enfant**, pas celle du conteneur. Résultat : l'ouverture
et un enfant sont partis dans le ⓘ, deux enfants et un `</div>` surnuméraire
sont restés, et ce `</div>` de trop fermait la carte **avant** le vocabulaire et
la mosaïque — qui se sont retrouvés hors du cadre.
**Ne jamais découper du HTML à l'index de caractère.**

**2. Les v545 et v548 disaient « ils passent derrière le ⓘ » — je les avais
seulement masqués.** Ils n'étaient plus nulle part. Une correction à moitié
faite est une perte de fonction, pas un allégement.

**3. Le ⓘ était positionné en absolu** au coin bas de la carte. Quand la carte a
grandi, il est parti à **1071 px** — hors de l'écran. Un élément calé sur un
conteneur dont la hauteur varie se déplace sans qu'on touche à son code. Il vit
maintenant dans le flux, à côté de « Ta galerie ».

### ⚠️ Et un défaut que le vérificateur a arrêté net

Pour faire tenir « Chercher un mot » à côté du salut, j'ai réduit la police du
champ à 12,5 px. **`verifier.py` l'a refusé dans la seconde** : sous 16 px,
Safari iOS zoome dès qu'on touche le champ et ne dézoome pas — c'est-à-dire
exactement le défaut que Jacques venait de signaler sur l'objectif quotidien.
**C'est le libellé qui raccourcit, jamais la police.**

### La contradiction entre deux compteurs, expliquée plutôt que masquée

⚠️ **La barre du jour ne compte que les cartes JUGÉES ; la mosaïque compte
chaque carte traversée.** Jacques a vu « 2 / 40 » figé alors qu'il tournait des
cartes — et comme il n'atteignait jamais 40, la célébration de l'objectif ne
pouvait pas se déclencher non plus. **Une seule cause pour ses deux
observations.**

Les deux mesures restent différentes, parce qu'elles mesurent deux choses
différentes : **l'objectif mesure du travail, la mosaïque mesure la présence**.
Mais le ⓘ le dit maintenant en toutes lettres, parce que rien d'autre ne permet
de le deviner.

---

## 12 septembre 2026 — la séance revient chez elle, et le silence s'explique (v551)

**Trois remarques de Jacques, et les trois portent sur des choses que l'app
faisait sans le dire.**

### La séance ne revenait pas à l'accueil

⚠️ `ouvrirSeanceDuJour()` **ne fixait aucun écran de retour**. `handleFlashcardBack()`
retombait donc sur ce qui traînait — le panneau des noms, ou l'écran d'un thème
ouvert une heure plus tôt. Le défaut ne se voit qu'en enchaînant : quelqu'un qui
n'a fait que sa séance ne le rencontre jamais.

La séance part de l'accueil et y revient : c'est là que se trouvent le tableau,
le compte du jour et la porte suivante.

### L'objectif atteint ne se disait pas

L'écran de fin proposait « en faire de plus » **sans jamais annoncer que
l'objectif était atteint**. Rien ne félicitait, et rien ne disait que la suite
était facultative. Deux phrases, selon le cas : « Objectif du jour atteint —
40 cartes. La suite est pour le plaisir. » ou « Encore 28 cartes pour ton
objectif du jour. »

### Et le plafond de la mosaïque ressemblait à une panne

⚠️ **Passé 80 carreaux dans la journée, le tableau cesse d'avancer — sans un
mot.** Le plafond est là pour protéger le rythme de la collection : sans lui,
mille cartes balayées en un quart d'heure terminent une image d'un coup et les
soixante-cinq y passent en une semaine. Mais un mécanisme qui s'arrête en
silence ne se distingue pas d'un mécanisme cassé.

« Le tableau a avancé au maximum pour aujourd'hui. Il reprendra demain. »

---

## 12 septembre 2026 — le regard en arrière, et un « Suivant » construit puis défait (v553)

**Le besoin, dit par Jacques :** *« je peux vouloir juste tout de suite regarder
c'était quoi le mot en français, puis revenir à la carte »* — mais aussi, deux
messages plus loin : *« j'aime bien le principe que ça revienne dans deux
minutes, donc on voit d'autres cartes en attendant »*.

⚠️ **J'avais construit la mauvaise réponse.** Un bouton « Suivant » qui séparait
juger d'avancer : la carte jugée restait à l'écran jusqu'à ce qu'on la congédie.
Ça répondait à la première phrase et contredisait la seconde — et ça coûtait un
geste sur quarante.

**La bonne réponse ne touche pas au flux.** Ce qui manquait n'était pas de
**retenir** la carte, c'était de pouvoir la **regarder** après coup. Un bouton
discret « Revoir le mot précédent » ouvre le mot qu'on vient de quitter, avec sa
traduction et sa phrase d'exemple, puis se referme.

⚠️ **En lecture seule.** La carte précédente est déjà jugée et programmée : la
rejuger la compterait deux fois, dans la dose du jour comme dans l'échelle de
mémorisation.

**Ce qui reste de la version défaite :** le balayage ne saute plus. C'était une
décision à part, et la bonne — une carte traversée sans réponse ne dit rien au
planificateur, et c'était la cause des deux compteurs qui se contredisaient.

⚠️ **Et un défaut attrapé à l'essai :** la phrase d'exemple s'affichait **en
français**. `texteCarte(..., "exemple")` suit la langue de l'interface — il
renvoyait « Mon père travaille beaucoup » à quelqu'un qui voulait revoir un mot
**allemand**. Le rang nu porte l'allemand ; les rangs par langue portent ses
traductions. Les deux s'affichent maintenant, l'allemand d'abord.

**Leçon à garder :** j'ai codé la première demande sans attendre la seconde. Deux
phrases qui se complètent valaient mieux qu'une phrase prise seule — et c'est en
demandant son avis avant de pousser que la deuxième est arrivée.

---

## 12 septembre 2026 — les règles de genre, et une régression que j'ai poussée (v555)

### ⚠️ D'abord la régression, parce qu'elle était en ligne

*« Je suis pris dans l'écran vide. »* La v553 avait fait appeler
`passerAuSuivant()` par le balayage ; la v553b a **supprimé cette fonction** en
défaisant le bouton « Suivant » — et l'appel est resté. Le balayage levait une
erreur, la carte ne bougeait plus, l'écran restait bloqué.

⚠️ **`verifier.py` ne pouvait pas le voir** : il vérifie les `onclick` du HTML,
pas les appels à l'intérieur du JavaScript. Le contrôle manquant est ajouté —
`verifier_appels_internes()`, qui lit les lignes ne contenant qu'un
`nomDeFonction();` et exige que la fonction existe. **135 appels surveillés.**

⚠️ **Le motif est volontairement étroit.** Un motif large — tout `nom(` —
ramènerait les fonctions locales, les paramètres, les méthodes et les globales
du navigateur : un contrôle qui accuse à tort est pire que pas de contrôle
(v537). Étroit, il n'attrape pas tout, mais il attrape exactement la faute
commise et n'accuse jamais à tort.

**La leçon :** ne jamais supprimer une fonction sans chercher qui l'appelle.

### Les règles de genre des noms

**Demande de Jacques, en attente depuis la v540.** Vingt et une terminaisons,
une leçon et un exercice, dans la tuile Noms.

⚠️ **Les taux sont MESURÉS sur nos 4 199 noms** (`tests/genres.py`), pas
recopiés d'une grammaire. Une grammaire dit « les noms en -ung sont féminins »
sans dire si c'est 100 % ou 94 % — or la différence décide de la formulation, et
une règle énoncée comme absolue alors qu'elle a des exceptions enseigne une
fausse certitude. C'est Jacques qui l'avait signalé à propos de `-e` : « la
majorité du temps, c'est féminin ». **C'est 90,1 %, et on l'écrit.**

**Dix terminaisons sans une seule exception** dans nos données : `-keit` (78
mots), `-tion` (53), `-heit` (49), `-age` (38), `-schaft` (37), `-tät`, `-ität`,
`-sion`, `-anz`, `-enz`.

⚠️ **Et la mesure a révélé un piège que je n'attendais pas.** Plusieurs
« exceptions » n'en sont pas : `der Kuchen` ne porte pas le suffixe *-chen*,
`der Sprung` ne porte pas *-ung*. Ce sont des **homographes de terminaison** —
la règle du suffixe est exacte, c'est le test sur les lettres qui ne distingue
pas. La leçon le dit, parce que c'est précisément ce qui fait douter d'une règle
juste.

**L'exercice tire en tiers égaux**, comme celui de la v540 et pour la même
raison — en pire ici : **quinze des vingt et une règles donnent « die »**. Un
tirage naturel se réussirait à plus de 80 % en répondant « die » à tout.

**Ce qu'il apprend et que « Quel article ? » n'apprend pas :** deviner le genre
d'un mot **jamais rencontré**. L'un fait mémoriser un à un, l'autre fait
généraliser.

### Trois ajustements visuels

- **« Ta galerie » et le ⓘ s'alignent sur le bas du tableau** : la colonne de
  droite était en `flex-start`, elle s'arrêtait à son contenu et `margin-top:auto`
  n'avait rien à pousser.
- **Le troisième bouton passe en colonne** : à 13 px, l'échéance ne s'alignait
  plus à côté d'un libellé de dix-neuf caractères.
- **Le cadre suit l'œuvre en plein écran** : le tableau y flottait sans bord,
  alors que c'est là qu'on le regarde vraiment.

---

## 12 septembre 2026 — la zone morte temporelle, deux fois (v556)

### ⚠️ Ce qui était cassé en ligne

*« Plein de choses qui ne sont plus là. »* Plus de tableau, plus de bandeau de
séance, la moitié de l'accueil disparue.

**La cause tient en une ligne.** La v555 déclarait :

```
const REGLES_GENRE_URL = MOSAIQUE_BASE.replace("mosaique/", "") + "…";
```

`MOSAIQUE_BASE` est déclaré **7 650 lignes plus bas**. Un `const` n'est pas
remonté comme une fonction : le lire avant sa ligne lève une `ReferenceError`.
Et comme tout le script est au même niveau, **rien de ce qui suit ne s'exécute**.

⚠️ **Le fichier portait déjà cet avertissement**, posé après un accident
identique sur des `let` : *« si ces `let` étaient déclarées plus bas, un appel
précoce tombait dans leur zone morte temporelle et plantait tout le script »*.
Je l'ai refait quelques milliers de lignes plus haut.

**La règle :** dans un fichier de 26 000 lignes, une constante du sommet ne
dépend jamais d'une autre. On met le littéral, ou on calcule dans la fonction.

### Le contrôle qui manquait

`verifier_zone_morte()` relève les 251 constantes de premier niveau et refuse
qu'une initialisation en lise une déclarée plus bas. **Vérifié en réintroduisant
la faute dans une copie : le contrôle l'attrape.**

⚠️ Il ne regarde que le cas net — `const X = NOM…` où `NOM` est une autre
constante de premier niveau. Ni les appels de fonction (celles-là sont
remontées), ni l'intérieur des fonctions. Étroit, mais il attrape exactement la
faute commise, deux fois maintenant.

### Et l'écran ⓘ, réécrit

Troisième réécriture de cette légende (v537, v549, v556), toujours pour la même
raison : **elle décrivait un écran qui avait changé sans elle**. Il avait grossi
par accumulation — chaque version y poussait ce qu'elle retirait de la carte, et
personne ne relisait l'ensemble. Un titre qui parlait d'une « carte » devenue un
écran, un paragraphe sur « ce qui fait bouger ce pourcentage » alors que le
pourcentage n'est plus en tête, et un `<ul>` imbriqué par erreur dans le bloc
des cumuls.

**Trois parties, dans cet ordre** : ce qu'on voit sur l'accueil · ce qui est
rangé ici · comment un mot s'installe.

## 12 septembre 2026 — cinq réglages d'écran, tous signalés sur son appareil (v557-v561)

Jacques a lu l'accueil ligne à ligne sur son iPhone. Rien ici n'a été trouvé par
un test : **chaque défaut vient de son œil, et la plupart sont des restes** — du
texte, un geste ou un cadre qui décrivaient un état antérieur de l'écran.

- **v557 — l'anneau disait la même chose que la barre, en moins lisible.** Le
  grand anneau de pourcentage et la barre de vocabulaire mesuraient la même
  chose. J'ai gardé la barre, qui distingue *su · en cours · à rencontrer* ;
  l'anneau ne savait donner qu'un nombre. ⚠️ Le balisage de l'anneau reste dans
  la page, caché : `updateHomeStatsPanel()` y écrit toujours, et le retirer
  aurait cassé la mise à jour en silence.
- **v558 — deux indications décrivaient un geste disparu.** Une flèche « → »
  au bout de « 223/860 » et une phrase d'aide sous la carte pointaient un
  balayage qui n'existait plus depuis deux versions. *« Ce n'est pas évident
  qu'on peut agrandir »* : ce n'était pas évident parce que ce n'était plus vrai.
- **v559 — les trois boutons de jugement prenaient le tiers de l'écran.** Une
  rangée de trois échéances (10 minutes · demain · trois jours) était juste, mais
  elle repoussait le mot lui-même hors du regard. Ramenés à deux, l'échéance en
  gros.
- **v560 — trois natures de contrôle dans un seul bandeau.** *« Il faut que je
  fasse attention »* : le bandeau portait une **action** (commencer — mais il
  fallait deviner qu'on touche le fond), un **réglage** (d'où viennent les mots
  neufs) et une **seconde action** (par thème) mêlée aux pastilles du réglage.
  Une nature par ligne, et un vrai bouton pour l'action.
- **v561 — le cadre contrastait avec le tableau, pas avec la page.** Le cadre de
  la mosaïque était noir sur fond clair *et* sur fond sombre. Sur le noir, il
  disparaissait. Noir de jour, gris pâle la nuit : **un cadre se détache de ce
  qui l'entoure, jamais de ce qu'il contient.**

**Ce qui revient :** quand un geste ou une mesure disparaît, **son texte reste**.
Deux contrôles attrapent maintenant le *code* mort (`verifier_appels_internes`,
`verifier_zone_morte`) ; le texte périmé n'a encore d'autre détecteur que lui.

## 12 septembre 2026 — la séance ne servait que des verbes (v562)

Retour le plus grave du lot : *« là, c'est tous des verbes que j'ai dans ma
séance du jour. Il faudrait que ça soit mélangé, verbe, nom, adjectif,
adverbe. »*

`ordonnerParFrequence()` triait **à plat**, tous les mots mélangés, par rang de
fréquence — exactement ce que l'avertissement écrit au-dessus de la fonction
interdit : *« le classement ne vaut qu'à l'intérieur d'une catégorie, jamais
entre deux »*. Les listes Leipzig comptent des formes et non des lemmes ; à plat,
une catégorie rafle le haut du classement et occupe toute la séance.

Remplacé par un **tourniquet** : un panier par catégorie, chacun trié par son
propre rang, puis on sert un mot de chaque à tour de rôle. La fréquence continue
de décider *quel* verbe vient en premier ; elle ne décide plus *si* on voit un
verbe. ⚠️ L'avertissement était déjà là, au-dessus du code qui le violait — un
commentaire ne protège de rien tout seul.

### Et cinq réglages demandés dans la foulée

- **La flèche « revoir le mot précédent » rentre dans le cadre du verso.** Elle
  était tout en bas, sous les trois boutons : loin du regard au moment précis où
  l'on se dit « c'était quoi déjà ». ⚠️ `event.stopPropagation()` est
  indispensable — sans lui, la toucher **retournerait** la carte, puisque toute
  la surface du verso sert à ça.
- **« Je le sais par cœur · pas avant 16 jours » revient sur une ligne.** Il
  était passé en colonne à la v555 parce que l'échéance à 13 px ne tenait plus ;
  à 12 px elle tient à côté, séparée par un point médian, et le bouton reprend la
  moitié de sa hauteur.
- **La galerie passe du bleu au gris charbon.** Dans cette app le bleu veut dire
  *action*. Autour d'un tableau, il tirait l'œil vers un bouton secondaire.
- **Le bouton « Commencer » s'aligne sur les pastilles de niveau** — il commence
  où commence A1, finit où finit C1 — et perd la moitié de sa hauteur. Ce n'est
  pas une largeur recopiée : la colonne est en `max-content`, donc **ajouter un
  niveau demain déplacera les deux ensemble**.

### L'écran ⓘ, quatrième réécriture — et la dernière raison de le refaire

*« Je trouve que c'est peu visuel… puis on ne parle pas du tableau, comment il
grandit, comment ça fonctionne. »* Les deux reproches sont justes. C'était une
liste à puces décrivant des éléments qu'on ne voyait pas à côté, et **la mosaïque
— la seule chose vraiment nouvelle de l'app — n'y était pas mentionnée du tout**.

Chaque explication est maintenant collée à un **échantillon** de ce qu'elle
décrit : le compte de séance en pastille, la barre de vocabulaire avec sa
légende, et une grille miniature pour le tableau.

⚠️ **Les nombres viennent des constantes, jamais du texte traduit.** « 700
carreaux », « 80 par jour », « 3 séances » sont écrits par `majInfoProgression()`
depuis `MOSAIQUE_CARREAUX`, `MOSAIQUE_PLAFOND` et `MOSAIQUE_SEANCES_TROPHEE`. Un
chiffre recopié dans cinq traductions se met à mentir dès qu'on change la
constante, et personne ne le voit — **c'est exactement ce qui est arrivé trois
fois à cette légende.**

## 12 septembre 2026 — deux fautes d'echappement, et le controle qui manquait (v563)

Le vrai sujet de cette version n'est pas ce qu'elle ajoute, c'est ce qu'elle a
failli casser.

### L'app entiere est morte deux fois, et le verificateur a dit « aucun probleme »

Les scripts de construction passaient par un **heredoc** (`cat > f <<'PY'`).
Ce shell y **reduit les doubles antislashs, meme entre quotes simples**. Deux
lignes en sont sorties transformees :

| ecrit | arrive dans le fichier |
|---|---|
| `content:"\00a0\2022"` | `content:"<NUL>a0<0x82>2"` |
| `choisirNiveauVocab(\'' + niv + '\')` | `choisirNiveauVocab('' + niv + '')` |

Dans les deux cas, le `<script>` principal a cesse de s'analyser. Pas degrade :
**mort** — plus une seule fonction definie, plus d'accueil, plus de mosaique.
Et `verifier.py` a repondu **« OK, 14 650 controles passes »** les deux fois :
il cherche des cles et des `onclick` par expressions regulieres, et un octet
NUL ne l'en empeche pas. **Seul le navigateur le disait.**

### Deux gardes, et la preuve qu'elles attrapent

- **`node tests/syntaxe.js`** (nouveau) demande a un moteur JavaScript si les
  `<script>` d'`index.html` s'analysent. Il n'execute rien : `new Function(corps)`
  lit le texte et s'arrete la. Sur la copie cassee : *« ECHEC `<script>` ligne
  7555 : Unexpected string »* — le message exact du navigateur.
- **`verifier_octets_de_controle()`** refuse tout octet sous 0x20 hors
  tabulation et saut de ligne. Sur la copie cassee : *« 1 octet de controle
  interdit »*.

**Verifie en reintroduisant les deux fautes dans deux copies : chaque controle
attrape la sienne.** Et la regle est maintenant dans `CLAUDE.md` : les scripts
de construction s'ecrivent dans un vrai fichier, jamais par heredoc.

### Ce que la version apporte, une fois cela regle

**« Su » devient « maitrise ».** Demande de Jacques : *« on sait que la
maitrise, ca peut changer, mais au moins sur le coup, c'est plutot maitrise que
su »*. Et l'app disait deja **« mots maitrises »** dans les cumuls : deux mots
pour un meme etat, c'etait la vraie incoherence.

**« Jours travailles » ne part plus de zero.** Signale deux fois. Le compteur
s'amorcait sur la **serie**, qui vaut zero des qu'on a saute hier — exactement
le cas de quelqu'un qui travaille trois jours sur quatre depuis un an. Il
s'amorce desormais sur le **nombre de jours distincts du journal de
memorisation** (soixante jours d'horodatages), ou sur la serie si elle est plus
grande. ⚠️ Et il **s'ecrit immediatement** : sans cela l'amorce se recalculerait
a chaque ouverture, et comme la fenetre du journal glisse, le nombre pourrait
**redescendre**. « Il ne redescend jamais » est la seule promesse de ce
compteur.

**On peut enfin choisir le niveau affiche.** Question de Jacques : *« on montre
A1 ; ceux qui savent plus voudraient A2, B1… qu'est-ce qu'on pourrait faire
pour le changer ? »*

⚠️ **Le reglage existait deja — il etait seulement invisible la.** La carte suit
`niveauSeance()`, c'est-a-dire les pastilles du bandeau ; mais ces pastilles
sont annoncees comme « la provenance des mots nouveaux », donc personne ne
devine qu'elles commandent aussi cette barre. Plutot qu'un **second** reglage —
deux commandes pour un meme etat, la porte ouverte a l'incoherence — les lignes
que le depliement montre deja sont devenues **cliquables** : on ouvre la
fleche, on voit les cinq niveaux, on touche celui qu'on veut. Meme cle, meme
consequence que la pastille.

## 12 septembre 2026 — le zoom qui s'ouvre tout seul, troisieme signalement (v564)

*« Il y a toujours un probleme : dans certains ecrans, si je clique a un
mauvais endroit, l'ecran va s'expandre. Je suis oblige de le reduire avec mes
deux doigts. Donc il faudrait s'assurer partout dans l'application. »*

**Troisieme fois.** Les deux premieres, la parade avait ete posee sur une
**liste** d'elements interactifs — `button, .orb, .theme-item, .level-pill,
.judge-button…` — ce qui revenait a promettre de n'en jamais oublier un. La
promesse a tenu deux versions. Et le mot decisif de son message est **« a un
mauvais endroit »** : justement **a cote** d'un bouton, sur la carte, sur le
fond, sur un texte — partout ou la liste ne s'appliquait pas.

La regle est desormais sur la **racine**. `touch-action` ne s'herite pas, mais
le navigateur **intersecte** les valeurs de l'element touche et de ses
ancetres : `manipulation` sur `html` retire le double-tap de toute la page. La
flashcard garde son `pan-y`, plus restrictif — l'intersection la laisse gagner
pour elle-meme.

### La tentation suivante, et pourquoi on ne la prend pas

`user-scalable=no` dans le `<meta viewport>` reglerait tout d'un coup. Ce
serait une **faute d'accessibilite** (WCAG 1.4.4) : on retirerait alors le zoom
**voulu**, celui dont a besoin qui voit mal. On enleve un geste **accidentel**,
jamais un geste volontaire.

`verifier_zoom_involontaire()` garde **les deux moities de cette phrase** :
il echoue si la regle disparait de `html`, et il echoue aussi si le viewport se
met a interdire le pincement. **Verifie dans les deux sens, sur deux copies
cassees.**

### Et un vrai tableau dans l'ecran ⓘ

*« Pour l'explication d'un tableau en information, j'en mettrai un — peut-etre
en prendre un qui est apres les soixante-cinq, qui avait beaucoup de couleurs,
puis je le mettrai presque complet avec seulement une vingtaine de carreaux qui
ne sont pas termines. Je pense que ca donne une bonne idee. »*

Le quadrillage abstrait de la v562 montrait **une grille**. Une toile a vingt
carreaux pres montre **ce que la grille fait** — c'est la difference, et il a
raison.

**Franz Marc, _Blaues Pferd I_ (1911), Lenbachhaus** : la 66e toile, **hors
collection**. Illustrer avec l'une des 65 reviendrait a la devoiler avant
qu'elle soit meritee — c'est le sens de son « apres les soixante-cinq ». Grands
aplats de bleu, de jaune et de rouge : elle reste lisible avec vingt carreaux
manquants, ce que la demonstration doit justement montrer. Marc mort en 1916,
domaine public, meme traitement « vif » que les autres.

⚠️ Elle est dessinee par **`dessinerMosaique()`**, la fonction meme qui dessine
la vraie. La demonstration ne peut donc pas mentir sur ce a quoi le glacis
ressemble : si le rendu change, elle change avec lui.

## 12 septembre 2026 — la fleche descend dans la zone du pouce (v565)

*« Quand on veut retourner, que la fleche soit en bas au lieu d'en haut dans le
rectangle : sur le cellulaire, c'est plus pratique de l'avoir dans le bas.
Puisqu'on avait indique a cote "retour", ou quelque chose, je ne sais pas. »*

Deux corrections dans une seule phrase, et la seconde il l'a formulee en
hesitant — c'est souvent la qu'il a raison.

### En bas, parce qu'un telephone se tient d'une main

La fleche etait dans le coin **haut** gauche du verso depuis la v562. Le haut
d'un telephone tenu d'une main demande de changer de prise ; le bas non. Ce
n'est pas une question de gout, c'est la zone du pouce.

⚠️ **`margin-top:auto` plutot que `position:absolute`.** Le verso defile
(`overflow-y:auto`) : une fleche calee en `bottom:10px` se decrocherait du bas
**visible** des que la carte est longue. En flux, poussee par la marge
automatique, elle est au bas quand il reste de la place et apres le texte quand
il n'y en a plus. Mesure sur la carte reelle : 24 px du bas, 24 px du bord
gauche, a l'interieur du cadre.

### Et elle reprend son mot

Nue, une fleche ronde dans un coin peut se lire **« annuler »**, **« revenir au
recto »** ou **« carte precedente »** — trois gestes differents, et c'est la
troisieme qui est vraie. Jacques s'en est souvenu tout seul : *« on avait
indique a cote retour »*. C'etait le cas avant la v562, et le retirer etait une
perte que personne n'avait pesee.

Une cle **courte** — `flash_revoir_court`, « Precedent » — et non
`flash_revoir`, qui fait une phrase entiere et reprendrait toute la largeur.
⚠️ La phrase entiere reste comme **etiquette d'accessibilite** : le lecteur
d'ecran garde « Revoir le mot precedent », l'oeil n'a besoin que du mot.

## 12 septembre 2026 — les peintres parlent cinq langues, et les tuiles rouvrent leur porte (v566)

### Les 22 notices, traduites

Elles etaient en francais seul depuis la v543. `peintres.json` porte maintenant
`fr`, `en`, `tr`, `uk`, `fa` pour chacun des vingt-deux peintres — quatre-vingt-
huit textes. Aucun code a changer : `noticePeintre()` parcourait deja
`langueEtRepli()`.

⚠️ **Et c'est precisement ce qui rendait le defaut invisible.** Une notice
absente ne casse rien : elle se rabat sur le francais, sans erreur et sans
trace. Le manque n'est donc visible que par quelqu'un qui lit le turc —
c'est-a-dire par personne, ici. **C'est le meme mecanisme que les quatre
lecteurs de la chaine turque**, qui cassaient en silence quand on posait juste
la donnee.

`verifier_notices_peintres()` refuse desormais une notice vide dans l'une des
cinq langues, **et** un tableau dont le peintre n'a pas de notice du tout —
ajouter une toile d'un peintre inconnu donnerait un trophee muet. 22 notices
x 5 langues, 65 tableaux : zero trou.

### Les quatre tuiles de vocabulaire retrouvent leur porte

*« Dans le nom, l'adjectif, le verbe, l'adverbe — vers les flashcards. »*

`VOCAB_DANS_TUILES` reste `false`, et c'est voulu : il ferme les portes de
vocabulaire des tuiles de **grammaire** — pronoms, conjonctions, prepositions,
particules, nombres — ou elles faisaient doublon avec la seance du jour. Mais
une tuile qui s'appelle **« Noms »** et d'ou l'on ne peut pas atteindre une
carte de nom promet ce qu'elle ne tient pas.

Une liste nommee, `TUILES_AVEC_VOCABULAIRE`, exempte les quatre. Verifie sur
les six tuiles a la fois : *nomen*, *verben* et *adjektive* retrouvent leurs
deux portes ; *pronomen* et *konjunktionen* n'en ont toujours aucune.

⚠️ **L'adverbe n'avait rien a restaurer** : sa porte
(`openAdverbienVokabular`) n'a jamais figure dans `ACTIONS_VOCABULAIRE`, donc
n'a jamais ete filtree. Il est nomme dans la liste quand meme — pour qu'elle
dise l'intention et pas seulement l'effet.

## 12 septembre 2026 — j'avais compris l'inverse, et je l'avais publie (v567)

### La correction

*« Je crois qu'on s'est mal compris. Ce que je disais, c'est d'enlever toutes
les flashcards pour les tuiles de nom, verbes, adjectifs et adverbes. Par
exemple pour les noms : enlever "reviser les mots", enlever "parcourir par
niveau", enlever "parcourir par theme", enlever "mots aleatoires". Donc il n'y
a plus de traces de flashcards, sauf a partir de ma seance du jour, ou par
theme, ou par niveau. »*

Sa phrase de la v566 etait : *« dans le nom, l'adjectif, le verbe, l'adverbe —
vers les flashcards »*. J'ai lu **« remets-y une porte »** ; il disait
**« retire celles qui restent »**. Deux lectures possibles d'une meme phrase,
et j'ai pris la mienne sans le dire.

⚠️ **Ce qui aurait du m'alerter**, et qui etait sous mes yeux : la v566
consistait a **defaire** une decision de la v536 prise a sa demande, et le
commentaire de l'interrupteur le disait mot pour mot — *« c'est la demande de
Jacques »*. Quand une modification revient sur une decision que la personne a
elle-meme demandee, ce n'est pas le moment d'interpreter : c'est le moment de
demander.

### Ce qui change

`TUILES_AVEC_VOCABULAIRE` est **supprimee, pas videe** — une liste vide se
remplit toute seule un jour.

Et cinq portes rejoignent `ACTIONS_VOCABULAIRE` : `openNomen`,
`openNomenNiveau`, `openVerbenNiveau`, `openAdjektive`,
`openAdverbienVokabular`. La liste ne retenait jusqu'ici que les entrees qui
servent un paquet **sans qu'on ait rien choisi** ; « parcourir par niveau » en
demande un, mais elle mene au meme endroit — des flashcards. Il les a nommees
une a une.

Etat final, mesure et non suppose :

| tuile | ce qu'il reste |
|---|---|
| Noms | Dictee · Quel article ? · Les terminaisons qui trahissent le genre · Deviner par la terminaison |
| Verbes | Dictee · S'entrainer par temps · wissen ou kennen ? |
| Adjectifs | Dictee · Declinaison des adjectifs |
| Adverbes | Comprendre les adverbes · Reconnaitre la famille · Dictee |

⚠️ **Le filtre ne touche que les panneaux de tuile.** `renderOrbPanel()` en est
le seul lecteur : la seance du jour, son « ou par theme » et ses pastilles de
niveau appellent d'autres fonctions et continuent de servir des cartes — c'est
exactement ce qu'il demande de garder.

### Un controle qui interdisait ce qu'on voulait faire

`verifier_tuiles_non_vides()` refusait tout `open…` dans
`ACTIONS_VOCABULAIRE` : masquer un sommaire, disait-il, ferme une consultation
et non une revision. C'etait un **raccourci**. Ce qu'on voulait vraiment
empecher — vider une tuile — est verifie juste en dessous, directement, sur
l'etat final de chaque panneau.

**Un controle qui repose sur une convention de nommage plutot que sur l'effet
mesure finit par interdire ce qu'on veut faire.** La regle du prefixe est
retiree ; le seuil de deux entrees reste, et il passe.

### Et cent carreaux dans l'ecran d'information

*« Pour la peinture que tu as mise dans information, mets une centaine de
carreaux qui ne sont pas encore devoiles. »*

Il avait dit « une vingtaine » la veille, et c'etait juste sur le principe. Mais
vingt sur sept cents, dans une vignette de 136 px, ne se voyaient plus du tout :
la demonstration montrait une toile intacte et n'expliquait plus rien. A cent,
les carreaux fermes se comptent encore du regard et le mecanisme redevient
lisible **a cette taille-la** — c'est la vignette qui decide, pas le principe.

## 12 septembre 2026 — l'avatar piloté par l'audio, mesuré sur un plan

*« prépare l'essai du plan 16 »*, puis *« oui, prépare la piste »*.

L'essai préparé le 10 septembre n'avait jamais été lancé. Les deux autres
chemins étaient fermés de toute façon : il reste **460 crédits** Artlist, le
re-tournage MUET en demande 2 400, et le mode référence les brûle en 3,8 s.

### Ce que BytePlus a corrigé de mes notes

**0,12 $/s, pas 0,16 $.** Ma note du 10 septembre donnait BytePlus à 0,16 $ sur
la foi d'un comparatif ; leur propre fiche produit dit 0,12 $. **L'API
officielle de ByteDance est donc aussi la moins chère**, à égalité avec
WaveSpeed — il n'y a plus d'arbitrage à faire. Corrigé dans `essai_avatar.py`,
tarif et prose.

**Et leur catalogue dit ce que disait le papier.** Sur la page Vision AI :
Omnihuman 1.0 — *« High-Realism avatar, precise Audio-Driven sync »* ;
Omnihuman 1.5 — *« Advanced cognitive avatar, semantic understanding »*. C'est
exactement la lecture des tableaux du 10 septembre : **le 1.0 est celui du
lip-sync, le 1.5 celui des gestes.** Le catalogue pousse vers le numéro le plus
élevé ; on a pris le 1.0.

### ⚠️ Un défaut dans mon protocole, vu grâce à une ligne de spécification

La fiche annonce une sortie à 30 im/s. En vérifiant que ça ne biaisait rien
(non : SyncNet ramène tout à 25 im/s), j'ai vu autre chose.

**La ligne de base portait sur les 5,04 s entières de `plan16.mp4` — dont trois
de bouche fermée — et l'essai allait faire 2,12 s de parole presque pure.** J'ai
recoupé la prise actuelle à longueur égale pour mesurer ce que ça changeait :

| | LSE-D | LSE-C |
|---|---|---|
| prise actuelle, 5,04 s | 6,493 | 1,017 |
| **la même, recoupée à 2,12 s** | **12,548** | 1,219 |

**Sur 53 images la distance double, sur les mêmes images.** La confiance tient,
la distance non. J'allais faire comparer un essai court à une base longue et
appeler ça un résultat.

Réparé en générant **la piste pleine** — l'audio du plan tel qu'il est monté,
même voix, même placement de la parole, même longueur. 0,61 $ au lieu de 0,25 $.
**Trente-cinq cents pour que le chiffre qui décide de douze plans veuille dire
quelque chose.**

⚠️ **Et une règle plus générale : une ligne de base ne vaut que si elle a la
forme de ce qu'on lui compare.** Ce n'est pas une précaution de méthode, c'est
la différence entre une mesure et un chiffre.

### Deux choses que la doc disait et qui étaient fausses

- *« Input Parameters : Image + Audio »* — la fiche du 1.0 Quick Mode, datée
  d'octobre 2025, ne liste **aucun champ texte**. La console en propose un, et
  **il a été suivi** : le prompt interdisait le sourire continu et les dents, et
  Jacques, en regardant la prise : « il n'y a pas de sourire ». La doc était
  périmée.
- *« best results […] face in a FRONT-FACING position. Other types of images may
  yield poor results. »* Notre cadrage est un trois-quarts — Mark regarde hors
  champ, comme toute la série. **Ça n'a rien dégradé.**

### Le résultat

| | offset | LSE-D | LSE-C |
|---|---|---|---|
| Seedance + sync.so | **+40 ms** | 6,493 | 1,017 |
| **OmniHuman 1.0** | **−40 ms** | **5,565** | **2,444** |

**La confiance plus que double.** C'est l'axe qui pendait — celui qui disait
« bouche plausiblement dans le temps, dont le réseau doute qu'elle dise ces
mots-là ».

**Et le signe du décalage s'inverse, ce qui vaut mieux que le chiffre.** Le
+40 ms était du **son en avance sur l'image**, détectable dès 45 ms : on était à
la limite. Le −40 ms est de l'image en avance, toléré jusqu'à −125 ms. On passe
du bord du détectable au milieu de la marge.

### Où la bouche bouge, et où couper

Jacques a d'abord dit « au début et à la fin », puis s'est corrigé : « plutôt à
la fin ». La courbe lui donne raison.

| temps | |
|---|---|
| 0,00 → 0,60 | bouche calme |
| 0,66 → 1,78 | **la réplique** — le mouvement suit la voix, pic à 1,48 |
| 1,88 → 3,20 | mouvement résiduel moyen |
| **3,30 → 4,60** | **bouche calme, le creux le plus net** |
| 4,68 → 5,16 | elle rouvre — l'ouverture parasite |

**Coupe de 0,31 à 3,30** et le défaut sort du montage : 1,3 s de bouche calme
juste avant. ⚠️ `controler_bouche.py` mesure dans un rectangle calé sur du
**720×1280** ; la prise fait 1088×1920 et doit être ramenée d'abord, sinon le
cadre tombe à côté du menton.

Le vrai résultat est là-dedans : **pendant la réplique, le mouvement et la voix
montent et descendent ensemble.** La prise Seedance faisait l'inverse —
corrélation −0,31, la bouche s'agitait quand la voix se taisait.

### Ce qui n'est pas prouvé

**Une prise ne fait pas une preuve, et c'est celle où le gain était le plus
disponible** : le plan 16 partait de 1,017, le pire de l'épisode. Le contrôle
qui manque est **le plan 10**, dont la base est déjà correcte (4,937) — si
l'avatar l'améliore aussi, la piste tient partout ; s'il le dégrade, le gain
d'aujourd'hui n'était qu'un rattrapage sur un cas défaillant. Sa ligne de base
est en boîte depuis le 10 septembre, l'essai coûte 0,61 $.

Et **la confiance reste à 2,444 contre 10,1 sur de vraies images filmées.**
C'est une piste qui gagne, pas un problème résolu.

### Une question ouverte, posée en passant

Devant les exemples de la console, Jacques : *« Est-ce qu'on ne peut pas avoir
un format plutôt dessin animé ? »* Leur fiche annonce « un certain degré de
généralisation » pour l'anime et le dessin animé — non mesuré.

**Ce n'est pas qu'un choix de style : c'est une autre solution au même
problème.** Mâchoire décalée, dents, expression qui ne colle pas — ce sont des
défauts de vallée dérangeante, qui existent parce qu'un visage photoréaliste
promet une précision que le modèle ne tient pas. Un personnage dessiné ne fait
pas cette promesse. Contre : dix-neuf plans et les images d'identité seraient à
refaire (mais il reste 29 épisodes — changer maintenant coûte bien moins que
changer à l'épisode 5), le registre change le produit, et **dans un cours de
langue la bouche est un support d'apprentissage** : une bouche stylisée infidèle
aux phonèmes enseigne moins, voire mal sur `ü` et `ö`.

Décision reportée, volontairement : la question de l'essai — un modèle piloté
par l'audio supprime-t-il le décalage — est un comportement du modèle, pas du
style. La réponse vaut pour les deux registres.

## 12 septembre 2026 — le contrôle répond « égalité », et le sourire manquait

### Le plan 10 : ni mieux, ni moins bien

| | offset | LSE-D | LSE-C |
|---|---|---|---|
| Seedance + sync.so | +0 ms | 6,045 | 4,937 |
| OmniHuman 1.0 | −40 ms | 5,778 | **4,982** |

**+0,045 de confiance. C'est zéro.** Le plan 16 avait bougé de +1,427 ; de
vraies images filmées donnent 10,1. Quarante-cinq millièmes ne sont pas un
gain.

**Le contrôle a donc fait son travail, et la réponse est nuancée :**

- plan **défaillant** (16, base 1,017) → l'avatar le **répare** ;
- plan **sain** (10, base 4,937) → **jeu égal**, sans dégrader.

Le gain d'hier était bien un rattrapage sur un cas cassé. Ce qui reste acquis :
l'avatar ne casse rien, et le décalage d'attaque disparaît par construction.

### ⚠️ Un comparateur qui désigne toujours un vainqueur finit par en inventer un

`essai_avatar.py` a écrit « l'avatar gagne » pour +0,045. Il comparait des
**signes**. Corrigé : deux planchers, `BRUIT_C = 0,25` et `BRUIT_D = 0,30`, en
dessous desquels il écrit « égalité — sous le bruit, on ne conclut pas ».

⚠️ **Et les seuils disent eux-mêmes qu'ils ne sont pas étalonnés** : on n'a pas
de série de mesures répétées du même clip pour connaître la dispersion réelle.
Ce sont des planchers de bon sens. Le jour où l'on mesure trois fois la même
prise, on les remplacera par la dispersion observée. C'est la même faute que la
mesure en dB, qui s'est trompée quatre fois faute d'étalon.

### La voix est intacte, vérifié

*« Est-ce que tu as gardé l'intonation de la voix d'ElevenLabs ? »*

| | envoyé | revenu | corrélation | décalage |
|---|---|---|---|---|
| plan 10 | 5,06 s | 5,06 s | **1,0000** | 0 ms |
| plan 16 | 5,06 s | 5,06 s | **1,0000** | 0 ms |

**OmniHuman ne touche pas au son, il le laisse passer** — échantillon pour
échantillon. Aurora est exactement celle d'ElevenLabs.

### ⚠️ J'avais supprimé le sourire que la scène demandait

*« ce n'est vraiment pas intéressant à regarder sans sourire »*, puis, sur le
plan 10 : *« on voit moins de sourire dans ses yeux […] il manque un petit peu
de vie ».*

La feuille de tournage du plan 16 disait pourtant : **« Warm and genuine. A real
smile at the end. »** J'avais lu l'avertissement des praticiens — sourire
permanent, beaucoup de dents — et j'en avais fait une interdiction générale :
*« small and closed-lipped »*, *« never show rows of teeth »*.

**Le défaut à éviter est le sourire CONSTANT ET DÉCROCHÉ DE LA RÉPLIQUE, pas le
sourire.** Les deux feuilles sont corrigées : on demande un sourire qui
construit et finit franc, jusqu'aux yeux ; on interdit seulement celui qui
arrive déjà large à la première image et ne bouge plus.

⚠️ **Et une mesure qui passe avant le lip-sync : une série que personne n'a
envie de regarder n'a pas de problème de synchronisation.**

⚠️ **Le plan 16 est à refaire** avec son vrai sourire de remerciement. Sa prise
a répondu à la question posée ; elle n'est pas bonne pour le montage.

### Ce que « il manque de la vie » désigne, et qui a un chiffre

Ce n'est pas une impression : c'est **HKV**, la dynamique gestuelle du papier.

| | HKV |
|---|---|
| OmniHuman **1.0** | 47,6 |
| OmniHuman **1.5** | **72,1** (+52 %) |

**Toute la contribution du 1.5 est là** : un modèle de langue lit le *sens* de
la réplique et planifie l'interprétation — les gestes, le regard, ce qui vit
entre les mots. J'avais écarté le 1.5 parce qu'il est un cheveu sous le 1.0 en
lip-sync sur le portrait (5,053 contre 5,199).

**Ce cheveu ne coûte plus rien, maintenant qu'on sait que le lip-sync fait jeu
égal de toute façon.** Prochain essai : le plan 10 avec le 1.5, même image, même
piste, même prompt.

⚠️ **Retenir le renversement** : le 10 septembre, le classement Sync-C disait de
prendre le 1.0. C'était juste sur la donnée disponible, et faux sur la décision
— parce que l'axe qui départage les deux modèles ne départage rien chez nous.
**Un classement ne choisit que si l'écart qu'il mesure compte pour ce qu'on
fait.**

### L'offre gratuite change l'échelle

95 s offertes. Les 12 plans parlants font **62,48 s** bout à bout ; les 7 plans
sans parole (01, 02, 03, 04, 07, 18, 19) sont déjà tournés et ne passent pas par
l'avatar. **L'épisode 1 se termine à zéro dollar**, avec ~27 s de marge — cinq
reprises, pas cinquante. Et à 7,50 $ l'épisode hors gratuité, les 29 restants
coûteraient environ **220 $** en génération.

⚠️ Leur FAQ : **« Video URLs are valid for 1 hour »**. En lot, télécharger au fur
et à mesure — un lien expiré se repaie.

### Où se créent les images, puisque la question s'est posée

**OmniHuman ne compose rien** : il anime une image finie. Les images de départ
viennent d'**Artlist**, générées depuis @Mark et @Anna **avec une image
existante en référence de décor** — c'est ce qui garde le comptoir et la
lumière. Les quatre autres cadrages sont des recadrages ffmpeg, zéro crédit.
Les 460 crédits Artlist restants ne servent donc plus à la vidéo mais aux
images : environ trois séries de quatre poses. Piste non vérifiée : `Seedream
5.0` chez BytePlus, qui annonce une « cohérence de référence améliorée ».
