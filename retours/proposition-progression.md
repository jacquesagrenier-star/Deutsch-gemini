# Le sentiment de progression — ce que j'ai mesuré, et ce que je propose
### 10 septembre 2026 · proposition, rien n'est implémenté

Point de départ, tes mots : *« avant que je passe les quatre cent cinquante
mots quatre fois, ça risque de ne jamais arriver »*, puis *« ça peut paraître
comme un morceau trop gros, inatteignable »*.

Ce document sépare ce qui est **mesuré** de ce qui est **proposé**. Rien ici
n'a été codé.

---

## 1. Ce que j'ai vérifié dans le code

### Un mot jamais vu compte comme « dû »

`cartesEchues()` renvoie vrai quand `!st.due` — et un mot jamais touché a
`due: 0`. Donc à l'ouverture de « Noms au hasard » niveau A1, `cartesDeSession()`
te sert **les 462 cartes d'un coup**. Il n'existe aujourd'hui **aucune
distinction entre « nouveau » et « à revoir »**.

C'est la cause mécanique du « la séance n'a pas de fin ». Ce n'est pas un choix
de conception : c'est la conséquence d'une valeur par défaut.

### Les nombres

| niveau | noms |
|---|---|
| A1 | **462** |
| A2 | 570 |
| B1 | 1 784 |
| B2 | 445 |
| C1 | 948 |
| **total noms** | **4 209** |

Et pour l'ensemble du vocabulaire (noms, verbes, adjectifs, adverbes,
expressions, mots-outils) : **8 003 entrées**.

Sur les seuls noms A1 :

- le cercle bouge de **0,22 %** par mot maîtrisé ;
- il faut **1 848 « Je savais »** pour atteindre 100 %.

### Le premier mot maîtrisé ne peut pas arriver avant le 11ᵉ jour

L'échelle est 10 min → 1 jour → 3 jours → 7 jours. **Aucun découpage en blocs
ne change ce chiffre.** Le cercle est donc condamné à afficher 0 % pendant une
semaine et demie, quoi qu'on fasse. C'est la mémoire, pas le paquet.

### ⚠️ Les exercices ne laissent AUCUNE trace

`exerciseResults` apparaît à quatre endroits, tous en mémoire, remis à zéro à
chaque départ de série. **Rien n'est jamais écrit sur disque** : pas
d'historique, pas de score, pas de « vu la dernière fois le… ».

Quelqu'un qui travaille la grammaire deux semaines voit **0 %**. Ce n'est pas
une impression : il n'y a rien à voir. Les exercices font avancer l'objectif du
jour, et rien d'autre.

    vocabulaire   ~8 000 cartes   mesuré au mot près   0,22 % par mot
    grammaire     1 682 exercices, 40 jeux   RIEN

**On mesure la seule chose qui ne peut pas bouger vite, et on ne mesure pas du
tout celle qui le pourrait.**

### Deux choses qui marchent déjà, et qu'il ne faut pas refaire

- **Quand tu ouvres « Noms », les échéances passent déjà en premier.**
  `cartesDeSession()` renvoie les cartes échues dès qu'il y en a. Le trou n'est
  pas *dans* un paquet, il est **entre** les paquets.
- **Un paquet peut déjà mélanger les types.** `loadFlashcard()` honore
  `item.mode` : une carte qui porte son propre mode l'impose au rendu. Un
  paquet de révision mêlant noms, verbes et adverbes n'est donc pas une
  réécriture.
- Et tout l'état vit dans **un seul magasin** (`deutschAI_progress_v4`), le
  niveau étant dans la clé du thème. Une vue globale — tous types, tous niveaux
  — est un simple parcours. Ce sont les **portes** qui sont par paquet, pas les
  données.

---

## 2. Le diagnostic

Tu as soulevé trois obstacles, et ils n'en font qu'un.

1. *« 450 mots avant qu'ils reviennent »* → la séance n'a pas de fin.
2. *« il peut aller sur les noms, puis les adverbes, puis les exercices »* → chaque porte a son compteur.
3. *« A1 lundi, C1 mardi »* → et chaque niveau aussi.

**Le point commun n'est pas la porte, c'est le dénominateur.** Chaque chiffre
affiché est une fraction d'un très grand tout fixe, que l'usager n'a pas choisi
et ne finira probablement jamais. Quelle que soit l'entrée, il voit une part
minuscule — et le cercle n'en montre qu'un niveau à la fois, donc trois
niveaux travaillés donnent trois petits pourcentages, tous coincés.

**Tant que la progression est une fraction, elle décourage — quel que soit le
découpage en blocs.**

---

## 3. Ce que je propose

### D'abord : trois nombres SANS dénominateur

Ils montent quoi qu'il fasse et où qu'il aille.

| | monte quand | premier mouvement |
|---|---|---|
| **mots en cours** — commencés, pas encore acquis | il touche un mot neuf | la 1ʳᵉ carte |
| **mots acquis** — les quatre succès faits | l'échelle se termine | le 11ᵉ jour |
| **jeux solides** — sur 40 | il réussit une série de grammaire | la 1ʳᵉ séance |

Aucun n'a 8 000 au dénominateur. Aucun ne dépend de la porte choisie. Et ils
additionnent A1, C1, noms, adverbes et grammaire dans le même compte — parce
que c'est ce qu'il a **réellement construit**.

Le pourcentage par niveau reste, mais comme **une carte du territoire**, pas
comme une note. Il dit où l'on en est d'un niveau ; il ne peut pas porter la
motivation quotidienne.

### Ensuite, dans cet ordre

**Étape 1 — donner une mémoire à la grammaire.** C'est le seul des trois qui
n'existe pas du tout, celui qui bouge le plus vite pour l'usager, et il ne
touche à rien : un fichier de plus.

⚠️ **Par JEU, jamais par exercice.** Réussir « Ich habe gegessen » ne prouve pas
qu'on sait le Perfekt, et reservir cette phrase-là testerait la mémoire d'une
phrase, pas d'une règle. **Une règle se planifie ; un exemplaire se tire au
sort.** Le champ existe déjà : chaque exercice porte son `topic`.

À garder par jeu : la dernière fois, le nombre de séries, le taux de réussite.
Quarante jeux, c'est une échelle atteignable — « Perfekt : solide »,
« Konjunktiv II : à revoir ».

**Étape 2 — les deux compteurs de vocabulaire.** Les données sont déjà là ;
c'est un parcours du magasin, pas une nouvelle structure.

**Étape 3 — le plafond de mots neufs par jour, et il doit être GLOBAL.** La
séance devient : *tout ce qui est vraiment échu* + *au plus N nouveaux*, N
valant pour l'app entière et non par paquet. Sans plafond, on peut introduire
20 noms + 20 adverbes + 20 verbes dans la même journée : soixante mots qui
reviendront tous demain, et c'est le compteur d'échéances lui-même qui finit
par décourager.

À 20 par séance, présenter tout l'A1 prend **24 séances** — trois à quatre
semaines. C'est un horizon réel, contre « jamais » aujourd'hui.

Le plafond guide, il n'interdit pas : un bouton **« encore 20 »** sur l'écran de
fin, sans quoi celui qui a vingt minutes se fait renvoyer chez lui.

---

## 4. Ce que je ne toucherais pas

- **L'échelle à quatre succès.** C'est elle qui fait tenir la mémoire.
  L'assouplir rendrait le pourcentage plus rapide **et plus faux**.
- **Le calcul du pourcentage par niveau.** Il est juste ; c'est sa place à
  l'écran qui est discutable, pas sa valeur.
- **Le fait que l'usager choisisse sa porte.** On ne conçoit pas contre les
  choix de l'apprenant. L'app rend le bon geste visible et bon marché — elle ne
  le rend pas obligatoire.

---

## 5. Ce qui reste ouvert

- **Le nombre N.** 20 est le défaut d'Anki, pas une mesure faite ici. Il
  devrait vivre à côté de l'objectif du jour dans les réglages.
- **Ce qui rend un jeu « solide ».** Deux séries à 80 % ? Une seule à 100 % ?
  Aucune donnée pour trancher — il faudra le poser, l'essayer, puis le
  corriger. Le dire d'avance vaut mieux que de le figer en silence.
- **Le mélange des niveaux dans une révision globale.** Un mot C1 à côté d'un
  mot A1 : « Mots au hasard » le fait déjà quand on choisit tous les niveaux,
  mais ça n'a jamais été jugé à l'usage.
- **Ce qu'un testeur en pense.** Tout ce document raisonne sur des chiffres et
  du code. Aucun de ces trois compteurs n'a été montré à qui que ce soit.
