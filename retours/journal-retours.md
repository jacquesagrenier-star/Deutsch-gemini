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
