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

Chaque chiffre affiché est **une fraction d'un très grand tout fixe** que
l'utilisateur n'a pas choisi et ne finira probablement jamais. Quelle que soit
la porte d'entrée, il voit une part minuscule. Tant que la progression est une
fraction, elle décourage — indépendamment de tout découpage en blocs.

---

## 4. Ce qui est proposé

### 4.1 Mesurer la COUVERTURE plutôt que la maîtrise ou l'effort

Trois états par mot au lieu de deux :

| état | signification |
|---|---|
| jamais touché | — |
| **en cours** | l'échelle est entamée, pas terminée |
| **acquis** | les quatre succès sont faits |

Une seule barre, deux remplissages : le foncé = acquis, le clair = en cours.

- Elle **avance dès la première carte**, sans attendre onze jours.
- Elle **ne redescend jamais** : un échec fait repartir l'échelle, mais le mot
  reste « en cours ».
- Elle reste **vraie** : elle dit « j'ai commencé à travailler ce mot », ce qui
  est un fait sur l'apprenant — pas un compteur d'activité.

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

### 4.5 Ordre proposé

1. la mémoire de la grammaire (le seul point qui n'existe pas du tout) ;
2. les compteurs de couverture du vocabulaire ;
3. le plafond de mots neufs.

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

1. **Couverture contre maîtrise.** Une barre qui avance dès qu'on effleure un
   mot est-elle motivante ou trompeuse ? Existe-t-il des résultats publiés sur
   ce choix dans les applications d'apprentissage ?
2. **Le recul du pourcentage.** Faut-il vraiment qu'un « Je ne savais pas »
   fasse reculer un chiffre visible ? Quelles applications le font, et avec
   quel effet mesuré sur l'abandon ?
3. **Le plafond de mots neufs.** 20/jour est le défaut d'Anki, repris sans
   mesure de notre côté. Y a-t-il une base pour un autre nombre, ou pour le
   faire varier selon l'utilisateur ?
4. **Ce qui rend un jeu de grammaire « solide ».** Deux séries à 80 % ? Une à
   100 % ? Nous n'avons aucune donnée pour trancher.
5. **Le mélange des niveaux.** Une révision qui sert un mot C1 juste après un
   mot A1 : problème réel, ou faux problème ?
6. **Ce qu'on n'a pas vu.** Y a-t-il, dans ce qui précède, un défaut de
   conception plus grave que ceux listés ?

⚠️ **Précision méthodologique.** Tout ce document raisonne sur des chiffres et
sur le code. **Aucun de ces compteurs n'a été montré à un utilisateur.** Un
avis qui s'appuierait sur des résultats publiés ou sur des tests réels vaut
mieux qu'un avis de plausibilité — et nous ne retiendrons que ce qui est
vérifiable.
