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

### AUCUNE FRACTION À L'ACCUEIL — deux comptes, et c'est tout

Une étape intermédiaire a été proposée puis **écartée en cours de relecture**,
et elle mérite d'être racontée parce que l'erreur est instructive.

L'idée était de garder une barre, mais de changer son dénominateur : mesurer la
maîtrise non plus sur les 8 003 mots du corpus, mais sur **les seuls mots
commencés** — somme des paliers atteints ÷ (4 × mots commencés). Elle bougeait
dès la première séance et 100 % devenait atteignable.

**Un relecteur a produit l'arithmétique qui la tue.** 20 mots menés à 4/4 =
80/80 = 100 %. On ouvre 20 mots neufs : 80/160 = **50 %**. La barre s'effondre
de moitié le jour où l'utilisateur a le plus travaillé. Le problème du
dénominateur n'avait pas été résolu, seulement déplacé — et rendu plus violent,
puisque la chute est maximale quand la base est petite, c'est-à-dire pendant les
premières semaines, exactement la période qu'on cherche à réparer. (À 312 mots
commencés, la même dose de 20 ne coûte que 3 points ; à 20 mots commencés, elle
en coûte 50.)

**Mettre cette fraction en pixels ne la sauve pas** : un segment foncé qui
rétrécit alors qu'aucun mot n'a été perdu ment de la même façon.

**Conclusion retenue : l'accueil ne porte AUCUNE fraction.** Deux comptes, qui
ne se divisent par rien :

| | ce que c'est | premier mouvement |
|---|---|---|
| **mots commencés** | cartes uniques ayant reçu au moins une tentative | la 1ʳᵉ carte |
| **mots acquis** | cartes ayant les quatre succès | le 11ᵉ jour |

La barre n'existait que pour donner du mouvement avant le 11ᵉ jour. **« Mots
commencés » le donne déjà**, dès la première carte, et monte d'environ 20 par
séance. La fraction était une réponse à un problème que le premier compteur
résout mieux.

### ⚠️ Une question que le code tranche déjà à moitié : A ou B ?

Un relecteur demande si « acquis » veut dire **(A)** « a atteint 4/4 au moins
une fois » ou **(B)** « est actuellement à 4/4 ». **Vérifié dans le code, et
c'est B :** « Je ne savais pas » appelle `reviewAgain()`, qui remet
`srsHits = 0`, puis `scheduleReview()`, qui remet `mastered = false`. Un mot
maîtrisé qui rate son contrôle à 16 jours **perd sa maîtrise et repart à zéro**
— et le panneau d'aide le dit déjà à l'utilisateur.

La question ouverte n'est donc pas dans le calcul, elle est dans l'**affichage**
du compteur :

- **suivre le code (B)** : le compteur peut baisser, il est exact, et il baisse
  de quelques mots à la fois — pas de 50 points. Une relecture ajoute une
  condition qui coûte peu : **ne jamais décrémenter en silence**. Si « acquis »
  passe de 98 à 96, l'écran dit pourquoi — « 2 mots à reconsolider » — au lieu
  de laisser l'utilisateur découvrir un chiffre plus bas sans explication ;
- **afficher un cumul (A)** : il ne baisse jamais, mais il affirme une maîtrise
  qui n'est plus vraie.

Nous penchons pour **B**, par cohérence avec le principe de ce document. Mais
c'est un choix, et il est soumis à la relecture.

**Un troisième indicateur a été proposé, et refusé.** Deux relecteurs ont
suggéré d'ajouter une « consolidation actuelle » à côté des deux comptes. Sous
B elle est déjà égale à « mots acquis » ; sous A elle est un ratio dont le
dénominateur est le nombre de mots commencés — donc **exactement la fraction
qu'on vient de retirer**, sous un autre nom. Et la contrainte qui gouverne tout
ce chantier est venue de l'utilisateur lui-même : *« pour que ce soit simple et
clair pour l'étudiant »*. Trois nombres abstraits sur une carte d'accueil sont
le défaut qu'on répare, pas la réparation.

**Ce refus ne porte que sur l'accueil.** Si un relecteur juge qu'un état de
consolidation apporte une information utile, il a sa place dans le panneau ⓘ ou
dans un écran de détail — là où quelqu'un vient chercher une réponse précise,
et non là où il ouvre l'app pour savoir s'il a avancé.
- Elle reste **vraie** : elle dit « j'ai commencé à travailler ce mot », ce qui
  est un fait sur l'apprenant — pas un compteur d'activité.

La distinction **en cours ≠ acquis** doit rester visible : deux remplissages,
jamais un seul chiffre qui mélange les deux.

⚠️ **La règle qui sort de tout ceci, et qui vaut plus que le détail des
compteurs : aucun indicateur d'accueil ne doit se dégrader quand
l'utilisateur travaille.** C'est le critère qui a éliminé le pourcentage
global, puis la barre sur les mots commencés. Toute proposition future se juge
là-dessus d'abord.

**La nuance sans laquelle la règle a l'air violée, et un relecteur l'a
relevé :** « mots acquis » PEUT baisser, puisqu'il suit l'état réel (B
ci-dessus). Il n'y a contradiction qu'en apparence — la règle interdit qu'un
indicateur recule **en réponse à l'effort**, et c'est bien ce qui est obtenu :
ouvrir vingt mots neufs, se tromper sur une carte, ouvrir un niveau plus
difficile ne font baisser ni l'un ni l'autre des deux compteurs. La seule chose
qui retire un mot du compte « acquis » est **un oubli constaté au contrôle de
16 jours** — pas un geste de travail, mais un résultat de mémoire.

Cela dit, l'utilisateur ne fait pas cette distinction en regardant son écran :
il voit un nombre qui a baissé. **C'est précisément l'objet de la question 1(c)**,
et nous ne tranchons pas ici.

Raisonnement écarté : un compteur d'**effort** (cartes vues, minutes, XP)
monte tous les jours mais ne dit rien de ce qu'on sait ; un compteur de
**maîtrise** seule est vrai mais lointain et il recule.

### 4.2 Trois nombres sans dénominateur

Ils montent quelle que soit la porte choisie, et additionnent tous les niveaux
et tous les types :

| | monte quand | premier mouvement |
|---|---|---|
| **mots commencés** | il touche un mot neuf | la 1ʳᵉ carte |
| **mots acquis** | l'échelle se termine | le 11ᵉ jour |
| **jeux solides** (sur 40) | il réussit une série de grammaire | la 1ʳᵉ séance |

**« Mots commencés » est le chiffre d'accueil**, en gros caractères : c'est le
seul qui ne redescend jamais. « Mots acquis » est posé à côté, dans la même
taille de bloc mais sans emphase — il vaut zéro pendant onze jours, et un zéro
mis en vedette décourage.

⚠️ **« En cours » est un état interne, pas un compteur affiché.** Le §4.1 en a
besoin pour définir les trois états d'un mot ; l'accueil n'en montre pas le
total. Il se déduit d'ailleurs des deux autres, et un troisième nombre coûterait
plus en clarté qu'il ne rapporte.

Le pourcentage par niveau reste accessible, mais **dans le panneau ⓘ** et comme
**carte du territoire** — où j'en suis d'un niveau — non comme note
quotidienne. Il descend d'un rang à l'écran ; sa valeur n'est pas touchée.

**Vocabulaire.** Un relecteur a proposé « taux de consolidation » et « périmètre
engagé ». Écarté : le dossier garde les mots que l'écran affichera —
« commencés », « acquis » — pour qu'on ne relise pas une chose en en
construisant une autre.

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

**Non vérifié de notre côté**, et rapporté par un relecteur : la documentation
d'Anki indiquerait qu'une dose de 20 mots neufs par jour conduit à environ 200
révisions quotidiennes, et recommanderait de réduire si la charge devient
excessive ; et les applications grand public utiliseraient des doses plus
faibles (5 à 12 items neufs). **Nous n'avons pas vérifié ces deux points** — ils
sont ici pour être confirmés ou écartés, pas pour servir d'appui.

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

1. **Des comptes plutôt qu'un pourcentage.** Nous envisageons de retirer de
   l'accueil toute fraction, et de n'afficher que des nombres absolus :
   mots commencés, mots acquis, jeux de grammaire solides.
   (a) Ce découpage est-il plus compréhensible et plus motivant, pour un
   apprenant en autonomie, qu'un pourcentage — quel qu'en soit le
   dénominateur ?
   (b) Un nombre sans dénominateur prive l'apprenant de tout repère sur
   « combien il en reste ». Est-ce une perte réelle, ou le repère manquant
   est-il justement ce qui décourageait ?
   (c) « Acquis » doit-il suivre l'état réel (il peut baisser quand un mot est
   oublié) ou afficher un cumul qui ne baisse jamais mais surestime ?
   (d) Une barre qui avance dès la première tentative — **même ratée** —
   serait-elle motivante ou décevante pour un débutant ?
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
