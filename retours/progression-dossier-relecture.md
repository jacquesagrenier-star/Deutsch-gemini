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

### 4.1 Mesurer ce qui est COMMENCÉ et ce qui est ACQUIS

Trois états par mot au lieu de deux :

| état | définition exacte |
|---|---|
| jamais touché | aucune tentative |
| **en cours** | **au moins une tentative sur ce mot**, l'échelle n'est pas terminée |
| **acquis** | les **quatre** succès consécutifs sont faits |

⚠️ **Le mot « couverture » a été écarté après une première relecture**, et la
critique était juste : quelqu'un qui ouvre un mot, répond « Encore » et ne le
revoit jamais n'a rien « couvert ». « Commencé » est une affirmation vraie — on
ne prétend pas qu'il connaît le mot, on constate qu'il a commencé. C'est
exactement le principe que ce document se donne, et que la première version
enfreignait.

Une seule barre, deux remplissages : le foncé = acquis, le clair = en cours.

- Elle **avance dès la première carte**, sans attendre onze jours.
- Elle **ne redescend jamais** : un échec fait repartir l'échelle, mais le mot
  reste « en cours ».
- Elle reste **vraie** : elle dit « j'ai commencé à travailler ce mot », ce qui
  est un fait sur l'apprenant — pas un compteur d'activité.

La distinction **en cours ≠ acquis** doit rester visible : deux remplissages,
jamais un seul chiffre qui mélange les deux.

Raisonnement écarté : un compteur d'**effort** (cartes vues, minutes, XP)
monte tous les jours mais ne dit rien de ce qu'on sait ; un compteur de
**maîtrise** seule est vrai mais lointain et il recule.

### 4.2 Trois nombres sans dénominateur

Ils montent quelle que soit la porte choisie, et additionnent tous les niveaux
et tous les types :

| | monte quand | premier mouvement |
|---|---|---|
| **mots en cours** | il touche un mot neuf | la 1ʳᵉ carte |
| **mots acquis** | l'échelle se termine | le 11ᵉ jour |
| **jeux solides** (sur 40) | il réussit une série de grammaire | la 1ʳᵉ séance |

Le pourcentage par niveau reste affiché, mais comme **carte du territoire** —
où j'en suis d'un niveau — et non comme note quotidienne.

### 4.3 Donner une mémoire à la grammaire — par JEU, jamais par exercice

Conserver, pour chacun des 40 jeux : la dernière fois, le nombre de séries, le
taux de réussite.

**Par jeu et non par exercice** : réussir « Ich habe gegessen » ne prouve pas
qu'on sait le Perfekt, et reservir cette phrase-là testerait la mémoire d'une
phrase, pas d'une règle. Une règle se planifie ; un exemplaire se tire au sort.

### 4.4 Plafonner les mots NEUFS par jour, globalement

La séance devient : *tout ce qui est réellement échu* + *au plus N nouveaux*,
N valant pour l'application entière et non par paquet.

Sans plafond, on peut introduire 20 noms + 20 adverbes + 20 verbes le même
jour : soixante mots qui reviendront tous demain, et c'est le compteur
d'échéances lui-même qui finit par décourager.

À 20 par séance, présenter tout l'A1 demande **24 séances**, soit trois à
quatre semaines — un horizon réel. Le plafond guide sans interdire : un bouton
« encore 20 » sur l'écran de fin.

**Trois affinements proposés par un relecteur, non mesurés, à discuter :**

- **Un plafond dynamique plutôt que fixe.** Si la journée porte déjà 50
  échéances, y ajouter 20 mots neufs crée un goulot. Le nombre de neufs
  dépendrait alors de la charge du jour.
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

**Non vérifié de notre côté**, et rapporté par un relecteur : la documentation
d'Anki indiquerait qu'une dose de 20 mots neufs par jour conduit à environ 200
révisions quotidiennes, et recommanderait de réduire si la charge devient
excessive ; et les applications grand public utiliseraient des doses plus
faibles (5 à 12 items neufs). **Nous n'avons pas vérifié ces deux points** — ils
sont ici pour être confirmés ou écartés, pas pour servir d'appui.

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

1. **« Commencé » contre « acquis ».** Une barre qui avance dès la première
   tentative — **même ratée** — est-elle motivante ou décevante pour un
   débutant ? Existe-t-il des résultats publiés sur ce choix ?
2. **Le recul du pourcentage — et la question se dédouble.**
   (a) Est-ce **pédagogiquement exact** ? « Ma maîtrise mesurée de ce corpus a
   diminué » est une affirmation vraie.
   (b) Est-ce **soutenable comme indicateur principal** ? Faut-il lisser la
   baisse, ou la laisser refléter l'oubli exactement ? Quelles applications le
   font, et avec quel effet mesuré sur l'abandon ?
3. **Le plafond de mots neufs.** 20/jour est le défaut **actuellement utilisé
   par Anki**, qui ne le présente pas comme une dose optimale universelle.
   Existe-t-il des données reliant le nombre d'items neufs introduits chaque
   jour à la rétention, à la charge de révision et à l'abandon ? Ces données
   justifient-elles un nombre **fixe** ou **adaptatif** ?
4. **Ce qui rend un jeu de grammaire « solide ».** Deux séries à 80 %, une
   série à 100 %, ou plusieurs réussites espacées ? L'étude de Serfaty (§4.6)
   associe la connaissance productive durable à **deux séances sans erreur**,
   indépendamment du nombre total de séances. Ce résultat se transpose-t-il à
   nos 40 jeux — dont les exercices sont tirés d'un réservoir, non répétés à
   l'identique — ou faut-il mesurer autrement ?
5. **Le mélange des niveaux.** Une révision qui présente un mot C1 juste après
   un mot A1 est-elle réellement problématique, ou seulement intuitivement
   inconfortable ? La littérature sur l'**entrelacement** suggère que mélanger
   des catégories peut améliorer l'apprentissage, l'effet dépendant de leur
   similarité. Faut-il conserver le mélange global, et n'introduire une
   contrainte de niveau que si les données d'usage montrent un problème ?
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
