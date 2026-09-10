# Progression et motivation — dossier pour relecture externe
### Wortando, 10 septembre 2026

Ce document est autonome : il ne suppose aucun accès au code. Il décrit
**comment ça marche aujourd'hui**, **ce que ça pose comme problème**, et **ce
qui est proposé**. Les questions posées à la fin sont celles sur lesquelles un
avis extérieur serait utile.

---

## 0. Le contexte en cinq lignes

Wortando est une application web d'apprentissage de l'allemand, destinée à des
adultes francophones (interface aussi en anglais, turc, ukrainien, persan).
Elle contient deux choses très différentes :

- **du vocabulaire** — environ **8 000 cartes** (noms, verbes, adjectifs,
  adverbes, expressions, mots-outils), réparties par niveau CECR A1 à C1 ;
- **de la grammaire** — **1 682 exercices** répartis en **40 jeux** (Perfekt,
  Konjunktiv II, prépositions, ordre des mots, déclinaison de l'adjectif…).

L'utilisateur choisit librement où il va : une tuile par type de mot, une par
famille d'exercices, et un sélecteur de niveau.

---

## 1. Comment la progression fonctionne AUJOURD'HUI

### 1.1 L'échelle de mémorisation (vocabulaire)

Chaque carte porte trois champs : `mastered`, `due` (une date), `srsDailyStreak`.

À chaque carte, l'utilisateur répond par un seul geste — **« Encore »**,
**« Je savais »**, ou **« Je le sais déjà »**. L'application en déduit
l'échéance :

| succès consécutifs | prochaine apparition |
|---|---|
| 1er « Je savais » | **+10 minutes** |
| 2e | **+1 jour** |
| 3e | **+3 jours** |
| 4e | **maîtrisé** |

- Un mot maîtrisé revient tous les **16 jours** pour vérification, sans cesser
  d'être compté.
- **« Encore »** remet le compteur à zéro et replace la carte quelques rangs
  plus loin dans la même séance.
- **« Je ne savais pas » retire la maîtrise** : le pourcentage **redescend**.
- **« Je le sais déjà »** marque le mot maîtrisé immédiatement.

Quatre pastilles sous la carte montrent les succès consécutifs (●●●○).

### 1.2 Comment une séance est constituée

À l'ouverture d'un paquet (par exemple « Noms au hasard, niveau A1 ») :

```
si des cartes sont ÉCHUES  →  la séance = ces cartes-là
sinon                      →  la séance = TOUTES les cartes non maîtrisées
```

**Point capital : un mot jamais vu est considéré comme échu.** Le test est
« la date d'échéance est-elle absente ou passée ? », et un mot neuf n'a pas de
date. Il n'existe donc **aucune distinction entre « nouveau » et « à
revoir »**.

Conséquence directe : à la première ouverture de « Noms A1 », la séance
contient **les 462 cartes d'un coup**. Elle n'a pas de fin.

### 1.3 Ce qui est affiché

Sur l'écran d'accueil, une carte porte quatre repères :

- 🔥 **jours** — jours consécutifs avec au moins une carte faite ;
- ◯ **un cercle** — le pourcentage de mots **maîtrisés** du niveau affiché
  (un seul niveau à la fois, on en change en touchant le cercle) ;
- 📈 **cette semaine** — mots devenus maîtrisés sur les **sept derniers jours
  glissants** ;
- 🎯 **objectif du jour** — cartes et exercices faits aujourd'hui, quelle que
  soit la réponse (cible réglable, 30 par défaut).

### 1.4 Les exercices de grammaire

**Ils ne laissent aucune trace.** Les résultats d'une série vivent en mémoire
le temps de la séance et sont effacés au départ suivant. Rien n'est écrit sur
disque : pas d'historique, pas de score par jeu, pas de « vu la dernière fois
le… ». Ils font avancer l'objectif du jour, et rien d'autre.

---

## 2. Les chiffres

**Le vocabulaire, par niveau (noms seulement) :**

| niveau | noms |
|---|---|
| A1 | **462** |
| A2 | 570 |
| B1 | 1 784 |
| B2 | 445 |
| C1 | 948 |
| total noms | 4 209 |

Vocabulaire complet, tous types : **8 003 entrées**.

**Sur les seuls noms A1 :**

- le cercle avance de **0,22 %** par mot maîtrisé ;
- il faut **1 848 réponses « Je savais »** pour atteindre 100 % ;
- **le premier mot maîtrisé ne peut pas arriver avant le 11ᵉ jour**
  (10 min + 1 j + 3 j + 7 j). Aucun découpage, aucun réglage d'interface ne
  change ce chiffre : c'est l'échelle elle-même.

**La grammaire :** 1 682 exercices, 40 jeux, **0 octet conservé**.

---

## 3. Les problèmes constatés

### 3.1 La séance n'a pas de fin

462 cartes d'affilée, sans unité de travail achevable. L'écran de fin de
séance existe mais n'arrive jamais en pratique.

### 3.2 Le pourcentage ne peut pas bouger, et il peut reculer

À 0,22 % par mot et 11 jours avant le premier acquis, le cercle affiche 0 %
pendant une semaine et demie quoi que fasse l'utilisateur. Et quand il bouge,
il peut **redescendre** — un « Je ne savais pas » honnête fait reculer le
chiffre.

**Formulation plus juste, venue d'une première relecture :** le problème n'est
pas que l'algorithme soit trop lent. C'est qu'on **demande à un indicateur de
maîtrise de jouer le rôle d'un indicateur de progression quotidienne**. Les
deux ne peuvent pas être le même nombre — et c'est ce qui ferme la tentation
d'assouplir l'échelle pour rendre le cercle plus gratifiant.

### 3.3 L'utilisateur se déplace, les compteurs non

Il peut faire les noms lundi, les adverbes mardi, les exercices mercredi ; A1
un jour, C1 le lendemain. Chaque paquet a sa propre file d'échéances, et rien
nulle part ne dit **combien de mots attendent, tous paquets confondus**. Les
échéances ne se perdent pas (elles sont attachées au mot), mais elles sont
invisibles tant qu'on n'ouvre pas le bon paquet.

### 3.4 On mesure ce qui bouge lentement, et pas ce qui bougerait vite

Le vocabulaire — 8 000 cartes, 0,22 % par mot — est mesuré au mot près.
La grammaire — 40 jeux, une échelle courte et atteignable — n'est pas mesurée
du tout. Deux semaines de travail sur la grammaire affichent **0 %**.

### 3.5 Le fond du problème : le dénominateur

Chaque chiffre affiché est **une fraction d'un très grand tout fixe** dont
l'échéance d'achèvement est très lointaine. Quelle que soit la porte d'entrée,
l'utilisateur voit une part minuscule. Tant que la progression est une
fraction, elle décourage — indépendamment de tout découpage en blocs.

---

## 4. Ce qui est proposé

### 4.1 ⚠️ CHANGEMENT DE CONCEPT — un chemin fermé, et non un buffet ouvert

**Cette section a été entièrement réécrite le 10 septembre 2026, après six
relectures de la version précédente.** Elle ne la corrige pas : elle la
remplace. Le raisonnement écarté est conservé au §4.2 bis, parce qu'il est plus
instructif que la conclusion.

Aujourd'hui, l'application est un **buffet** : l'utilisateur choisit un niveau,
puis un type (noms, verbes, adjectifs, adverbes, expressions), puis un thème ou
« au hasard ». Toutes les portes sont ouvertes en permanence, sur 8 003 entrées.

**Proposition : fermer les portes et servir.** L'application distribue des
**étapes fermées d'environ 30 items**, mélangeant noms, verbes et adjectifs.
Quand l'étape est acquise, la suivante s'ouvre. L'utilisateur ne choisit ni
niveau, ni type, ni thème — il n'a qu'une séance devant lui.

Ce que ça règle, et qu'aucun compteur n'avait réglé :

- **La fatigue de décision disparaît.** Plus rien à choisir avant de commencer.
- **Le dénominateur écrasant disparaît réellement**, au lieu d'être déplacé :
  les 8 003 mots existent, ne sont jamais affichés, et ne se choisissent pas.
- **La variété devient une propriété du contenu, pas un choix de l'utilisateur.**
  L'étape mélange les types d'elle-même. C'était l'objection de l'auteur :
  *« je ne suis pas sûr que les étudiants s'intéressent à un thème en
  particulier ; de réflexe, je pense qu'ils vont vouloir varier. »*
- **Le cadre de référence, qui manquait à tout le reste, existe enfin :**
  l'étape EST le comparateur (§4.6). « Étape 7 » se comprend sans explication ;
  « 98 mots acquis » ne se compare à rien.

**L'étape s'affiche seule, sans total.** « Étape 7 », jamais « étape 7 sur 27 ».
Un relecteur a proposé « étape 3 / 12 du niveau A1 » : le chiffre est faux — le
niveau A1 compte **797 entrées** (462 noms, 111 verbes, 104 adjectifs, 52
adverbes, 68 expressions), soit **27 étapes de 30** — et surtout il réintroduit
le dénominateur qu'on vient de retirer.

⚠️ **Et « Étape 7 » n'est pas un rang de jeu.** La distinction est essentielle,
parce que la critique la mieux établie contre les tableaux de bord
d'apprentissage vise exactement les rangs et les XP : des mesures d'engagement
déguisées en mesures de compétence. Ici le 7 n'est pas un score attribué pour de
l'activité — c'est **210 mots réellement passés par les quatre paliers**. Le
nombre ne peut pas monter sans que la mémoire ait suivi.

**Trois trous à boucher avant d'écrire une ligne de code :**

1. **Le mot récalcitrant.** Vingt-neuf mots acquis, un qui retombe à zéro tous
   les trois jours, et l'étape ne se ferme jamais — l'infini recréé en plus
   petit. Il faut une porte de sortie : l'étape se ferme au bout de N jours et
   le mot têtu passe à l'étape suivante.
2. **L'apprenant qui a déjà des bases** se retrouverait à l'étape 1 devant des
   mots qu'il connaît. La soupape existe déjà dans le code — « je le sais
   déjà » (`markKnownAlready`) saute les quatre paliers d'un coup — mais elle
   devient centrale au lieu d'être un raccourci.
3. **L'ordre des étapes.** Voir §4.2.

**Ce que ça coûte, et il faut le dire :** c'est la façon dont l'auteur lui-même
utilise l'application qui disparaît. Il révise en « mots au hasard » après avoir
choisi son niveau — précisément la porte qu'on ferme. C'est peut-être la bonne
décision (il connaît l'app par cœur, il n'est pas l'utilisateur type), mais
c'est une décision prise contre un usage réel et observé.

### 4.2 L'ordre des étapes — ce qu'on voudrait, et ce qu'on a

L'intention est de servir **les mots les plus utiles d'abord**. ⚠️ **Vérifié :
il n'existe aucune donnée de fréquence dans la base** — zéro champ de ce type
sur les 4 209 noms, ni sur les verbes, ni sur les adjectifs. « Les 30 mots les
plus utilisés » n'est pas calculable aujourd'hui.

Ce que nous avons en revanche : **les listes officielles d'examen**, déjà dans
le dépôt — Goethe A2 (1 092 mots), Goethe B1 (2 779), DTZ (2 439). Pour des
apprenants qui préparent ces épreuves, c'est un meilleur critère que la
fréquence brute : ce ne sont pas les mots les plus fréquents de la langue, ce
sont ceux qu'on leur demandera. Manquent la liste A1, et tout ordre à
l'intérieur des listes, qui sont alphabétiques.

**Décision de méthode : ne pas attacher le concept à cette donnée.** La question
posée n'est pas « quel est le meilleur ordre » mais « un chemin fermé vaut-il
mieux qu'un buffet ouvert ». L'ordre actuel suffit pour y répondre. Lier les
deux, c'est ne rien pouvoir essayer avant qu'un projet de données aboutisse — et
il peut échouer sur une licence, comme nous l'avons frôlé avec le dictionnaire.

### 4.2 bis Le raisonnement écarté, conservé parce qu'il est instructif

Avant le chemin, trois modèles ont été proposés puis abandonnés, dans cet ordre.
Chacun échoue pour une raison différente, et un lecteur extérieur jugera mieux
la proposition finale en voyant ce qu'elle remplace.

**1. Le pourcentage par niveau (l'existant).** 0,22 % par mot, rien avant le
11ᵉ jour, et il recule quand on oublie. Écarté : il demande à un indicateur de
maîtrise de jouer le rôle d'un indicateur de progression quotidienne.

**2. Une barre sur les mots commencés.** Mesurer la maîtrise non plus sur les
8 003 mots mais sur le sous-ensemble ouvert : somme des paliers ÷ (4 × mots
commencés). Écarté par l'arithmétique d'un relecteur : 20 mots menés à 4/4 font
80/80 = 100 % ; on ouvre 20 mots neufs et l'on tombe à 80/160 = **50 %**. La
barre s'effondre le jour où l'utilisateur a le plus travaillé, et la chute est
maximale quand la base est petite — donc pendant les premières semaines,
exactement la période qu'on cherchait à réparer. **Le problème du dénominateur
n'avait pas été résolu, seulement déplacé — et rendu plus violent.**

**3. Deux comptes absolus** — « mots commencés » et « mots acquis », sans
aucune fraction. Corrects, honnêtes, et **insuffisants** : c'est le verdict de
l'auteur, et il est juste. 98 mots acquis sur un total non dit reste 98 sur
l'infini. Retirer le dénominateur retire la douleur ; ça n'apporte pas la
satisfaction, parce qu'il manque toujours **quelque chose qui se termine**.

⚠️ **La règle née de ces trois échecs, et qui gouverne le reste : aucun
indicateur d'accueil ne doit se dégrader quand l'utilisateur travaille.** C'est
elle qui a éliminé le pourcentage global puis la barre. Le chemin la respecte :
franchir une étape ne peut rien faire reculer.

**Ce qui survit au changement de concept :** un mot est **acquis** après quatre
succès, et il peut ressortir du compte s'il est oublié au contrôle de 16 jours —
c'est ce que le code fait (`reviewAgain()` remet `srsHits` à 0, puis
`scheduleReview()` remet `mastered` à `false`). La question de savoir si
l'affichage doit suivre cette baisse ou afficher un cumul reste entièrement
ouverte : voir question 1(c), et le précédent de Duolingo au §4.6.

### 4.3 Donner une mémoire à la grammaire — par JEU, jamais par exercice

Conserver, pour chacun des 40 jeux : la dernière fois, le nombre de séries, le
taux de réussite.

**Par jeu et non par exercice** : réussir « Ich habe gegessen » ne prouve pas
qu'on sait le Perfekt, et reservir cette phrase-là testerait la mémoire d'une
phrase, pas d'une règle. Une règle se planifie ; un exemplaire se tire au sort.

⚠️ **« Solide » n'est pas encore défini, et c'est délibéré.** Deux séries sans
erreur (piste suggérée par l'étude de Serfaty, §4.6), une série à 100 %, ou
plusieurs réussites espacées : le critère sera fixé **après** cette relecture,
pas avant (question 4). Tant qu'il ne l'est pas, le compteur « jeux solides »
est une intention, pas une spécification.

### 4.4 Plafonner les mots NEUFS par jour — désormais une conséquence, plus un mécanisme

La séance devient : *tout ce qui est réellement échu* + *au plus N nouveaux*,
N valant pour l'application entière et non par paquet.

⚠️ **Le chemin du §4.1 rend ce plafond presque automatique** : les mots neufs ne
peuvent venir que de l'étape en cours, donc on ne peut plus ouvrir 20 noms,
20 adverbes et 20 verbes le même jour. Le plafond ne sert plus à empêcher la
dispersion — il sert seulement à **doser le rythme à l'intérieur d'une étape**,
et c'est là que le chiffre d'Anki compte (§4.6 : 20 neufs/jour mènent à environ
200 révisions quotidiennes).

Dans l'ancien modèle, sans plafond d'aucune sorte, on pouvait introduire 20 noms
+ 20 adverbes + 20 verbes le même jour : soixante mots qui reviendraient tous
demain, et c'est le compteur d'échéances lui-même qui finissait par
décourager.

À 20 par séance, présenter tout l'A1 demande **24 séances**, soit trois à
quatre semaines — un horizon réel. Le plafond guide sans interdire : un bouton
« encore 20 » sur l'écran de fin.

**Trois affinements proposés par un relecteur, non mesurés, à discuter :**

- **Un plafond dynamique plutôt que fixe.** Si la journée porte déjà 50
  échéances, y ajouter 20 mots neufs crée un goulot. Le nombre de neufs
  dépendrait alors de la charge du jour. ⚠️ **Hypothèse, pas intention** : un
  plafond qui varie tout seul est plus difficile à comprendre qu'un nombre
  fixe, et rien ne sera implémenté ici sans données d'usage.
- **Trois régimes au choix** : soutenu (20 neufs/jour), modéré (10), entretien
  (0 — seules les échéances sont traitées).
- **Déclarer la séance « complétée »** plutôt que simplement terminée : une fin
  qui se voit, avec « continuer quand même » toujours possible. La différence
  n'est pas cosmétique — c'est ce qui transforme une liste qui s'épuise en
  objectif atteint.

### 4.5 Ordre proposé

1. la mémoire de la grammaire (le seul point qui n'existe pas du tout) ;
2. les compteurs de couverture du vocabulaire ;
3. le plafond de mots neufs.

---

## 4.6 Ce que la littérature dit déjà — vérifié à la source

Trois résultats publiés touchent directement les questions ci-dessous. Ils sont
donnés **comme éléments de décision, pas comme prescriptions** : aucun ne porte
sur Wortando.

**Une barre de progression motive sans faire apprendre.** Une étude sur
**166 adultes** apprenant du vocabulaire avec récupération adaptative a comparé
une version sans gamification à des versions avec points, puis points et barres
de progression. Les points et les barres ont augmenté le sentiment de
compétence, le plaisir et la valeur attribuée à la tâche — **sans améliorer le
rappel différé à 2-3 jours**.
*Gamified feedback in adaptive retrieval practice: Points and progress-bars
enhance motivation but not learning*, Computers in Human Behavior, nov. 2025.

C'est exactement la distinction que ce document défend : **un indicateur de
motivation n'est pas un indicateur d'apprentissage**. La barre peut avoir une
fonction motivante — à condition de ne pas se déguiser en mesure de maîtrise.

**Pour la grammaire, ce sont les séances SANS ERREUR qui comptent, pas un
pourcentage.** Une étude de 2024 (119 participants, langue artificielle,
séances de réapprentissage sur jours consécutifs, test à 14 jours) : la
connaissance productive est nettement meilleure avec trois ou quatre séances de
réapprentissage. Et l'analyse individuelle montre qu'une connaissance
productive durable est associée à **deux séances sans erreur**, quel que soit
le nombre total de séances effectuées.
*Serfaty, « Practice Makes Perfect, but How Much Is Necessary? The Role of
Relearning in Second Language Grammar Acquisition »*, Language Learning, 2024.

Cela déplace notre question sur les « jeux solides » : le critère naturel
serait **deux séries sans faute**, plutôt qu'un seuil de pourcentage dans une
seule série.

**20 mots neufs par jour mènent à environ 200 révisions par jour — vérifié dans
le manuel officiel d'Anki.** Le manuel donne les deux chiffres ensemble : 20
cartes neuves par jour est bien le réglage par défaut, et « si vous ajoutez 20
cartes neuves chaque jour, vous pouvez vous attendre à ce que les révisions
quotidiennes montent, dans les premiers temps, autour de 200 cartes par jour ».
Il ajoute qu'apprendre trop de cartes neuves d'un coup rend les révisions
accablantes et fait réoublier la matière.
*Anki Manual, « Getting Started » et « Deck Options », docs.ankiweb.net,
consulté le 10 septembre 2026.*

C'est le chiffre qui donne sa force au plafond de §4.4 — et il vient d'un
manuel d'outil, pas d'une étude : c'est une pratique établie, pas une dose
optimale démontrée.

**Un chiffre ne veut rien dire sans cadre de référence.** La littérature sur les
tableaux de bord d'apprentissage (*learning analytics dashboards*) travaille
cette notion depuis dix ans : un indicateur n'a de sens que rapporté à un
comparateur, et il en existe trois — **soi dans le temps**, **les autres**, **un
objectif**. Le résultat le mieux établi y est négatif, et il porte sur la
comparaison aux autres : anxiété sociale, atteinte au sentiment d'efficacité.
*Jivet et coll., et travaux ultérieurs — voir notamment « Students' Use of a
Learning Analytics Dashboard and Influence of Reference Frames », Journal of
Computer Assisted Learning, 2025.*

Wortando n'a pas de comparaison sociale, donc pas ce risque-là. Mais le cadrage
éclaire notre problème : **nos compteurs n'ont aucun cadre de référence**, et
c'est une explication possible du fait que « 98 mots acquis » ne procure aucun
sentiment de progression.

**La motivation augmente quand le but se rapproche (effet de gradient de but).**
L'étude de référence porte sur des cartes de fidélité de café : une carte de 12
cases dont 2 sont déjà tamponnées est complétée par **34 %** des clients, contre
**19 %** pour une carte de 10 cases vides — effort réel identique.
*Kivetz, Urminsky, Zheng, « The Goal-Gradient Hypothesis Resurrected »,
Journal of Marketing Research, 2006.*

**Ce que font deux outils de référence — vérifié, et l'un des deux contredit
notre penchant.**

*Anki sépare trois piles sur son écran d'accueil* : New, Learning, To Review,
par paquet et pour la journée. C'est précisément la séparation qui manque à
Wortando (§3.1) — chez nous un mot jamais vu compte comme dû, d'où les 462
cartes servies d'un coup.
*Anki Manual, « Studying », docs.ankiweb.net.*

*Duolingo a RETIRÉ son indicateur qui recule.* Les compétences « fêlées » —
une compétence dont la dorure se craquelait quand elle n'était plus pratiquée —
ont disparu avec la refonte du parcours, déployée jusqu'en novembre 2022 : la
révision est désormais intégrée au chemin lui-même. Et les niveaux
« légendaires » ne se cassent plus une fois obtenus.
*Duolingo, « A new home screen design », blog.duolingo.com, 2022.*

⚠️ **C'est un précédent qui joue CONTRE notre penchant pour l'option B**
(§4.2 bis).
Le plus gros acteur du domaine a rencontré la même question — faut-il montrer
la dégradation ? — et a répondu non : il a supprimé l'affichage qui recule et
déplacé la révision ailleurs. Ce n'est pas une preuve, c'est une décision de
produit sans résultat publié. Mais elle mérite d'être connue avant qu'on
tranche la question 1(c).

⚠️ **Toujours pas vérifié** : que les applications grand public utilisent des
doses plus faibles (5 à 12 items neufs par jour) ; et qu'aucune n'affiche de
pourcentage calculé sur l'ensemble d'une langue.

---

## 4.7 ⚠️ Ce que quatre relectures par IA ont donné — et n'ont pas donné

Ce dossier a été soumis quatre fois à des modèles de langue (ChatGPT, Gemini,
Copilot) avant d'atteindre un lecteur humain. Le bilan est utile à qui le lira
ensuite.

**Ce qu'elles ont apporté, et qui a été intégré :** le mot « couverture », qui
surpromettait ; le recadrage du 11ᵉ jour ; l'arithmétique qui a tué la barre sur
les mots commencés (§4.1) ; la nuance de la règle d'or ; la séparation
découverte/révision (question 5) ; la décrémentation non silencieuse.

**Ce qu'elles n'ont pas apporté : une seule fois, la question 8 a produit un
défaut que nous n'avions pas déjà écrit.** Les trois « angles morts » les plus
souvent cités — pas de distinction entre carte neuve et carte échue, séances
sans fin, grammaire sans trace — sont les §3.1, §1.2 et §3.4 de ce document,
que les relecteurs venaient de lire. **Elles nous renvoient nos propres
constats comme des découvertes.**

⚠️ **Conséquence pour le lecteur suivant.** Si vous êtes un praticien ou un
chercheur : la valeur que nous cherchons n'est pas une validation de la
cohérence interne — quatre modèles l'ont déjà confirmée, et c'est le genre de
chose qu'ils confirment bien. C'est **le désaccord** qui nous intéresse, et
tout particulièrement un désaccord appuyé sur des données d'usage ou des
résultats publiés que nous n'avons pas.

**Deux affirmations sont revenues plusieurs fois sans que nous puissions les
vérifier**, et elles restent hors du raisonnement : que 20 mots neufs par jour
conduisent à 120-200 révisions quotidiennes après trois ou quatre semaines
(plusieurs relecteurs, chiffres voisins, aucune source) ; et que les
applications grand public ne font jamais baisser un score global à l'accueil
(plausible, invérifié). Si l'une des deux est établie quelque part, le dire
serait plus utile que tout le reste de cette section.

---

## 5. Contraintes à respecter

- **Ne pas assouplir l'échelle à quatre succès.** C'est elle qui fait tenir la
  mémoire ; l'assouplir rendrait le pourcentage plus rapide **et plus faux**.
- **Ne pas contraindre le parcours.** On ne conçoit pas contre les choix de
  l'apprenant adulte : rendre le bon geste visible et bon marché, pas
  obligatoire.
- **Ne pas transformer la progression en compteur d'activité.** Le chiffre doit
  rester une affirmation vraie sur l'apprenant.

---

## 6. Ce sur quoi un avis extérieur serait utile

1. **Le chemin fermé contre le buffet ouvert — c'est LA question du dossier.**
   Nous envisageons de retirer tous les choix (niveau, type, thème, « au
   hasard ») et de servir des étapes fermées d'une trentaine d'items mélangés,
   la suivante s'ouvrant quand la précédente est acquise (§4.1).
   (a) Pour un adulte en autonomie, un parcours imposé est-il plus soutenable
   qu'un accès libre — ou le sentiment de perdre le contrôle coûte-t-il plus
   cher que la fatigue de décision qu'il évite ?
   (b) Existe-t-il des résultats comparant les deux modèles à rétention égale,
   plutôt qu'à engagement égal ?
   (c) « Acquis » doit-il suivre l'état réel (il peut baisser quand un mot est
   oublié) ou afficher un cumul qui ne baisse jamais mais surestime ? Voir le
   précédent de Duolingo au §4.6, qui a supprimé son indicateur qui recule.
   (d) Un chemin imposé rend-il l'application inutilisable pour quelqu'un qui
   a déjà des bases, si la seule échappatoire est « je le sais déjà » ?
   (e) Nous supprimons au passage la façon dont l'auteur lui-même utilise
   l'application. Est-ce un signal d'alarme, ou la marque normale d'un produit
   qui cesse d'être conçu pour son concepteur ?
2. **Le recul du pourcentage — et la question se dédouble.**
   (a) Est-ce **pédagogiquement exact** ? « Ma maîtrise mesurée de ce corpus a
   diminué » est une affirmation vraie.
   (b) Est-ce **soutenable comme indicateur principal** ? Faut-il lisser la
   baisse, ou la laisser refléter l'oubli exactement ? Quelles applications le
   font, et avec quel effet mesuré sur l'abandon ?
3. **Le plafond de mots neufs.** 20/jour est le défaut d'Anki, et son manuel
   dit lui-même qu'à ce rythme les révisions montent autour de **200 par jour**
   (§4.6, vérifié à la source). C'est une pratique établie, pas une dose
   optimale démontrée. Existe-t-il des données reliant le nombre d'items neufs
   introduits chaque jour à la rétention, à la charge de révision et à
   l'abandon ? Justifient-elles un nombre **fixe** ou **adaptatif** — et 200
   révisions quotidiennes sont-elles seulement soutenables pour un adulte qui
   suit un cours du soir ?
   Existe-t-il des données reliant le nombre d'items neufs introduits chaque
   jour à la rétention, à la charge de révision et à l'abandon ? Ces données
   justifient-elles un nombre **fixe** ou **adaptatif** ?
4. **Ce qui rend un jeu de grammaire « solide ».** Deux séries à 80 %, une
   série à 100 %, ou plusieurs réussites espacées ? L'étude de Serfaty (§4.6)
   associe la connaissance productive durable à **deux séances sans erreur**,
   indépendamment du nombre total de séances. Ce résultat se transpose-t-il à
   nos 40 jeux — dont les exercices sont tirés d'un réservoir, non répétés à
   l'identique — ou faut-il mesurer autrement ?
   ⚠️ Un relecteur a reformulé ce résultat en « deux séries **consécutives** à
   100 % ». L'étude n'exige pas la consécutivité, et la version vérifiée à la
   source est celle du §4.6 : deux séances sans erreur, quel que soit
   l'intervalle. Merci de ne pas raisonner sur la version renforcée.
5. **Le mélange des niveaux.** Une révision qui présente un mot C1 juste après
   un mot A1 est-elle réellement problématique, ou seulement intuitivement
   inconfortable ? Deux effets connus tirent en sens contraire, et c'est ce
   qu'on aimerait voir arbitré : la littérature sur l'**entrelacement**
   suggère que mélanger des catégories améliore l'apprentissage, mais l'effet
   dépend de leur **similarité** — or un mot A1 concret et un mot C1 abstrait
   ne sont pas des catégories proches, et un relecteur avance à l'inverse un
   **coût de bascule attentionnelle**. Faut-il conserver le mélange global, et
   n'introduire une contrainte de niveau que si les données d'usage montrent
   un problème ?
   Une piste proposée en relecture, qui réconcilie les deux effets : **séparer
   les niveaux en DÉCOUVERTE, ne les mélanger qu'en RÉVISION**. L'entrelacement
   porterait alors sur ce qu'on revoit, jamais sur ce qu'on rencontre pour la
   première fois. Est-ce le bon partage ?
6. **Le plafond peut-il agacer ?** Bloquer l'entrée de mots neufs quand la
   charge de révision est lourde risque-t-il d'exaspérer quelqu'un qui veut
   « avancer dans le programme » à tout prix ?
7. **Le seuil d'« acquis ».** Quatre succès étalés sur onze jours : est-ce le
   bon compromis pour du vocabulaire A1/A2, ou trop exigeant ?
8. **Ce qu'on n'a pas vu.** Parmi tous les mécanismes décrits ici —
   progression, mémorisation, constitution des séances, entrée des mots neufs,
   grammaire, mélange des niveaux — voyez-vous un défaut de conception
   **plus important que ceux que nous avons identifiés** ? Cette question est
   une invitation explicite à répondre « votre problème principal n'est pas
   celui que vous croyez ».

⚠️ **Ce document a déjà subi deux relectures externes.** La première a
corrigé deux choses, intégrées ci-dessus : le mot « couverture », qui
surpromettait, et le cadrage du 11ᵉ jour. La seconde a proposé les affinements
du plafond (§4.4) — et a par ailleurs **inventé de toutes pièces une fin de
document** qui n'a jamais existé, en la présentant comme le texte réel. Inutile
donc de retrouver les deux premières corrections ; et prière de ne citer que ce
qui figure réellement ici.

⚠️ **Précision méthodologique.** Ce document raisonne sur des chiffres et sur
le fonctionnement actuel du code. **Aucun de ces compteurs n'a encore été
montré à un utilisateur.** Nous distinguons donc trois choses : les **faits
vérifiés**, les **résultats publiés** (§4.6) et les **hypothèses de
conception**. Un avis fondé sur des résultats publiés ou sur des tests
utilisateurs réels vaut mieux qu'un jugement de plausibilité. **Nous ne
transformerons pas une hypothèse en fait sans élément vérifiable** — et les
citations rapportées par un relecteur sont vérifiées à la source avant d'entrer
ici.
