# Fabriquer un épisode — la procédure complète
### Établie le 12 septembre 2026, sur l'épisode 1 « Ankunft in Berlin »

Ce fichier est le mode d'emploi. Il dit **quoi faire, dans quel ordre**, et
surtout **ce qu'il ne faut pas refaire** — chaque avertissement ici a coûté
une prise, une heure, ou une conclusion fausse.

---

## La chaîne, en une phrase

**Artlist** fabrique les images de départ → **ElevenLabs** les voix →
**OmniHuman 1.5** (BytePlus) anime l'image avec la voix → nos scripts
montent, sonorisent et sous-titrent.

⚠️ **Il n'y a plus d'étape de lip-sync.** sync.so ne sert plus : OmniHuman
fabrique la bouche à partir du son, dans la même passe que l'image.
L'abonnement sync.so à 19 $/mois n'a plus d'objet.

---

## Ce qu'il faut avoir avant de commencer

| | où |
|---|---|
| la scène, dialogue + 6 langues | `scenes/<scene>.json` |
| les voix, une par réplique | `audio/scenes/<scene>/NN-<locuteur>.mp3` |
| les images de départ | `video/episode-<scene>/01-images/` |
| les plans de décor | `video/episode-<scene>/03-final/` |
| la feuille de tournage | `video/episode-<scene>/A-REFAIRE.txt` |

⚠️ **La feuille qui fait foi pour l'image d'un plan est `A-REFAIRE.txt`**,
pas `A-REFAIRE-AUDIO.txt`. Les deux ont un bloc « PLAN 13 » et ce ne sont pas
le même plan : la scène compte **vingt** plans, le 13 ne dit que « Nehmen Sie
die S-Bahn » et le **20** enchaîne — mais le montage les a fondus en un seul
clip. Se tromper de feuille envoie la mauvaise image, **et rien ne s'en
plaint** : le modèle obéit, le fichier arrive, et la scène change de cadrage
au milieu.

---

## Étape 1 — préparer les paniers

```bash
python video/preparer_avatar.py --carte
python video/preparer_avatar.py --plan 5 6 8 9 10 11 12 13 14 15 16 17
```

`--carte` imprime plan / image / réplique côte à côte. **Relis-la avant la
série.** Une correspondance qu'on ne relit pas est une correspondance qu'on
suppose.

Chaque panier sort dans `_a-televerser/` : l'image en JPEG **à sa résolution
d'origine**, et la piste extraite du clip monté.

⚠️ **Ne pas réduire la taille de l'image.** Leur fiche dit *« the clearer the
input image, the better the generation effect »*. Le 12 septembre j'ai ramené
toutes les images à 1080 de large parce qu'**une seule** dépassait le plafond
de 5 Mo — appliquant au reste une contrainte qui ne valait que pour elle. Un
PNG est sans perte : ses mégaoctets paient l'exactitude, pas la finesse. Un
JPEG de qualité 2 à la même résolution tient dans le cinquième du poids.

⚠️ **Ne pas raccourcir la piste pour économiser.** Le silence final est la
marge dont la bouche a besoin pour se refermer — mesuré sur le plan 16, elle
met environ 1,4 s à redescendre après le dernier mot. Quelques dizaines de
cents contre une prise à refaire.

⚠️ **Et la ligne de base doit avoir la FORME de ce qu'on lui compare.** Une
base mesurée sur 5,04 s contre un essai de 2,12 s a fait passer la **même**
prise d'une LSE-D de 6,49 à 12,55. C'est pourquoi la piste vient du clip
monté, jamais d'une piste de tournage.

---

## Étape 2 — nettoyer les pistes

```bash
python video/nettoyer_queue.py --appliquer
```

Deux saletés de fin de phrase, et elles ne se cherchent pas pareil :

- le **« tss »** — un souffle aigu isolé après le dernier mot (plan 11 : le
  *t* final de « Bürgeramt » relâché tout seul, 90 ms après). Sa signature
  est la **couleur** : son énergie est dans l'aigu.
- le **« toc »** — une impulsion brève (plans 09 et 14). Sa signature est le
  **rapport crête/énergie** : la voix tient autour de 2 à 5, un clic dépasse
  25.

⚠️ **Un clic ne se voit pas à 16 kHz.** Un sous-échantillonnage lisse les
transitoires brefs et les fait disparaître — j'ai écrit « aucune coupure
nette » sur la foi d'une analyse à 16 kHz alors qu'à 44,1 kHz la fenêtre
montrait une crête de 9 226 pour une énergie de 257.

⚠️ **Et deux seuils ne peuvent pas être le même.** Celui qui *identifie* le
souffle et celui qui *ferme* la parole doivent différer, sinon une fenêtre du
souffle à 0,99 compte encore comme de la voix et repousse la recherche après
ce qu'on cherche.

---

## Étape 3 — générer, plan par plan

**BytePlus → Vision AI Studio → Dreamina Omnihuman 1.5.**

Réglages : **1080p**, **Fast mode éteint**, **Seed fixe** (note-la).

⚠️ **Le sélecteur de modèle revient au 1.5 à chaque ouverture.** On croit
choisir le 1.0 et on obtient le 1.5. Ça ne nuit pas — le 1.5 est celui de
l'essai gratuit — mais **ne jamais étiqueter une prise d'un numéro de modèle
qu'on n'a pas vérifié**. Une étiquette plus précise que la connaissance finit
par être citée comme un fait.

Pour chaque plan : l'image, la piste, le prompt. Une fois `Générer` appuyé,
le travail part chez eux — **tu peux enchaîner le suivant sans attendre**.

⚠️ **Les liens de téléchargement expirent au bout d'une heure.** En lot,
télécharge au fur et à mesure : un lien mort se **régénère**, donc se repaie.

⚠️ **Nomme le fichier par son plan** — et l'outil vérifiera quand même.

**Compter** : environ **2 min 20** par plan de 5 s en 1080p (leur RTF vaut
27). L'épisode entier, douze plans parlants, fait **63 s de vidéo = 7,50 $**
à 0,12 $/s — ou **zéro** sur les 100 s de l'essai gratuit.

---

## Étape 4 — importer, en vérifiant l'identité

```bash
python video/importer_prise.py
```

⚠️ **NE JAMAIS SE FIER AU NOM DU FICHIER.** Deux fois le 12 septembre, un
fichier portait le nom d'un autre plan. La première a produit une mesure
plausible, un verdict lisible, et **une conclusion spectaculaire entièrement
fausse** — j'ai relevé les seuils de bruit, réécrit le journal et poussé le
commit avant de m'en apercevoir. **Un fichier mal nommé est une mesure fausse
qui se présente bien : rien dans le résultat n'avertit.**

L'identité se lit dans le son : OmniHuman renvoie la piste inchangée
(corrélation 1,0000), donc on la corrèle aux douze pistes téléversées. Trente
secondes de calcul contre une journée de conclusions fausses.

L'importateur **repose systématiquement notre piste** sur la prise — sinon un
simple ré-import écrase les corrections de l'étape 2, en silence.

---

## Étape 5 — mesurer, sans lui donner le dernier mot

```bash
python video/essai_avatar.py --plan 13 --mesurer <la prise>
python video/cote_a_cote.py --plan 13
```

Ce qu'on mesure est **LSE-C**, la confiance de SyncNet. Repères :

| | |
|---|---|
| de vraies images filmées | **10,1** |
| une bonne prise avatar | 4,5 à 7,5 |
| seuil de bruit | **0,25** en confiance, 0,30 en distance |

⚠️ **Sous le seuil, la mesure ne conclut rien** — et le seuil lui-même n'est
pas étalonné : il s'appuie sur **une** paire de tirages du même prompt (plan
10 : 4,982 et 4,894, soit 0,088). Pour la vraie dispersion il faudrait trois
prises **à graine fixe**.

⚠️ **Un comparateur qui désigne toujours un vainqueur finit par en inventer
un.** Le script a écrit « l'avatar gagne » pour +0,045.

⚠️ **Et la mesure ne voit pas la vie.** Le mouvement moyen du visage : la
prise que Jacques a jugée la plus naturelle **bouge 30 % de moins** que les
autres. L'agitation n'est pas l'expressivité. Cette mesure sert à constater
qu'une chose a changé, **jamais à arbitrer une prise**.

**Ce que l'épisode 1 a donné**, base → avatar en LSE-C :

| gagne | | perd | |
|---|---|---|---|
| 13 | 5,50 → **7,46** | 06 | 4,94 → 4,23 |
| 16 | 1,02 → **2,42** | 11 | 5,77 → 5,33 |
| 12 | 2,73 → **3,81** | 08 | 5,70 → 5,22 |
| 17 | 4,04 → **4,68** | 15 | 5,78 → 4,60 |
| 10 | 4,94 → **5,52** | 05 | 5,47 → 4,20 |

**Sous 5,0 l'avatar répare ; au-dessus de 5,4 il perd un peu.** Le 13 fait
exception — et c'est la réplique deux fois plus longue que les autres.

⚠️ **On ne peut pas panacher les deux chaînes** : le détail du visage diffère
d'un facteur **2,8** entre Seedance et l'avatar (480p natif remonté en
1080p), et chaque raccord se verrait. C'est tout l'un ou tout l'autre.

---

## Étape 6 — monter

```bash
python video/monter_avatar.py
```

⚠️ **Les plans de décor n'ont aucune piste sonore, et leur voix vit
ailleurs** (`audio/scenes/<scene>/NN-erzaehler.mp3`). Y mettre du silence a
fait perdre la narration de **sept plans sur dix-neuf** — et un plan
silencieux au montage ne signale rien, il passe pour une respiration voulue.
C'est ce qui a fait dire à Jacques « il manque un plan » : le plan 07
existait, il était muet.

⚠️ **Tout segment doit sortir avec une piste sonore, même muette.** Le concat
exige le même nombre de flux partout ; un seul segment sans audio fait perdre
le son de **tout** l'épisode, sans un avertissement.

Le montage écrit `_montage-avatar/_plans.json` — l'instant de chaque plan.
⚠️ **Les sous-titres le lisent ; ils ne les recalculent pas.** Recalculer
« avec les mêmes règles » ailleurs, c'est se garantir qu'ils divergeront le
jour où l'une des deux change.

---

## Étape 7 — sonoriser

```bash
python video/ambiance.py --clip <le montage> \
  --lit audio/ambiance/hall.mp3@0 \
  --lit audio/ambiance/tapis.mp3@27.3 \
  --lit audio/ambiance/hall.mp3@31.1 \
  --lit audio/ambiance/sortie.mp3@64.7 \
  --annonce audio/ambiance/annonce-paris-de.wav --a 6.0
```

**Un lit par LIEU**, enchaînés en fondu de 0,8 s. Un lit unique sur tout
l'épisode contredit le montage : *« quand il change d'endroit, le son devrait
changer ».*

Les lits se génèrent dans **ElevenLabs → Sound Effects** : boucle **On**,
durée **22 s**, influence du prompt **60 %**, amélioration **Off**.
⚠️ L'amélioration réécrit le prompt et peut gommer le *« no intelligible
speech »* — la clause qui empêche des voix de se glisser dans le fond.
⚠️ La clé API du projet n'a **pas** la permission `sound_generation` : soit on
l'ajoute dans le tableau de bord, soit on passe par l'interface.

**Niveaux, mesurés et non devinés** : le lit à **−24 dB** sous le dialogue,
l'annonce à **−20**. ⚠️ Ce n'est pas une convention de goût : c'est le critère
**WCAG 1.4.7**. Pour une app d'apprentissage la raison est plus forte encore
— un apprenant qui décode de l'allemand n'a aucune attention à dépenser sur
un fond trop présent.

⚠️ **L'ambiance ne va JAMAIS dans la piste qu'on téléverse.** OmniHuman
fabrique la bouche à partir du son : une annonce dans le mp3 ferait articuler
le personnage sur elle.

⚠️ **Et rien de ce que le personnage demande ne sort du haut-parleur.** Ni
Gepäckausgabe, ni S-Bahn, ni billets, ni centre-ville. Un panneau lisible
rendrait absurde la question du plan 5 ; une annonce a le même pouvoir. Un
embarquement pour Paris ne renseigne personne.

L'annonce se fabrique avec une **voix Windows locale** (`faire_annonce.ps1`,
voix Katja / Stefan / Hedda) : après le filtre téléphone, la réverbération et
20 dB d'atténuation, une voix gratuite est indiscernable d'une voix neurale.
Autant garder les crédits pour ce qui s'entend.

---

## Étape 8 — sous-titrer

```bash
python video/sous_titres.py --incruster
python video/sous_titres.py --langue en --incruster
```

L'allemand mot à mot — **seul le mot en cours s'allume**, en ambre — et la
traduction en dessous, fixe.

⚠️ **Ne pas utiliser le tag `\k` du karaoké.** Il garde colorés les mots déjà
dits, donc la phrase se remplit de gauche à droite : l'œil voit une barre de
progression, pas un mot. Il faut **une ligne par mot**.

⚠️ **Un tag `\c` en ligne veut SIX chiffres** (`&Hbbggrr&`), pas huit. Les
huit sont la forme des styles. libass abandonne une balise mal formée **sans
un mot**, et le texte reste blanc.

⚠️ **`WrapStyle`, et les trois valeurs veulent dire trois choses** :
`2` = aucun retour à la ligne, le texte déborde de l'écran ;
`0` = coupe en **équilibrant**, donc élargir les marges n'y change rien ;
`1` = remplit la ligne du haut — **le seul qui utilise la largeur**.

⚠️ **La narration aussi se surligne.** Je l'avais exclue « parce qu'elle n'en
a pas besoin » : c'est elle qui porte le plus de texte, donc celle où le
repère sert le plus.

⚠️ **Le calage mot à mot est une estimation.** ElevenLabs sait rendre des
repères par caractère, mais seulement en **régénérant** l'audio — et le son
est figé, la bouche a été fabriquée dessus. On répartit donc au prorata des
syllabes puis on fait glisser chaque frontière vers le creux d'énergie le
plus proche (±120 ms). Sur 1,5 à 4,6 s ça tient ; sur une longue phrase
l'erreur s'accumule.

---

## Étape 9 — sortir le fichier de OneDrive

```bash
cp video/episode-XX/EPISODE-XX-...-st.mp4 C:/Users/jacqu/Videos/Wortando/
```

⚠️ **Le dossier du projet est synchronisé.** Un rendu de 50 Mo déclenche un
téléversement, et le lecteur répond `0xC00D36D6 — we can't get to your
storage`. `C:\Users\jacqu\Videos` n'est pas synchronisé.

---

## Ce qu'on a appris sur les PROMPTS

L'ordre recommandé par le guide propre à OmniHuman :

> **[mouvement de caméra] + [émotion] + [état de parole] + [actions]**

1. **CAMÉRA** — taille de plan, mouvement, et « garder la position et la
   distance de l'image ».
2. **ÉMOTION** — précise. *« She appears genuinely delighted »* vaut mieux
   que *« she looks happy »*.
3. **PAROLE** — ⚠️ **un vrai verbe de parole**, en position d'interprétation.
   *« Unnatural lip movements: add explicit speaking verbs. »* C'est leur
   remède pour exactement ce qu'on mesure, et nos premiers prompts le
   disaient en dernière ligne comme une contrainte technique.
   Plus : *« Let his face follow the voice »* — le son porte déjà
   l'interprétation.
4. **ACTIONS** — en séquence marquée : *First… Then… Finally*.
5. **APRÈS LA PAROLE** — ⚠️ sans ce bloc l'avatar retombe en poker-face,
   c'est documenté. La formule qui marche : *« listens intently without
   speaking »*, plus ce qui vit : respire, cligne, déglutit.
6. **CONTINUITÉ** — l'interlocuteur hors champ, les figurants.

### Les cinq pièges, chacun payé d'une prise

**a) Un verbe fort sans plafond est sur-joué.** *« she lifts one hand »* → la
main part en l'air. Nommer l'amplitude avec le geste.

**b) Des qualificatifs empilés sont sous-joués.** *« a small, gentle,
closed-lipped smile… nothing broad »* → presque rien. **Le modèle obéit aux
modificateurs plus qu'au verbe.** Décrire l'état d'arrivée, pas des limites.

**c) Un avertissement de tiers ne devient pas une règle permanente.** Un
comparatif reprochait à OmniHuman *« a lot of teeth »* ; j'en ai fait une
interdiction générale des dents, et **il a fallu desserrer le sourire trois
fois** avant d'obtenir le remerciement demandé. Le défaut décrit était le
sourire *constant et décroché de la réplique*, pas le sourire.

**d) La queue du plan a besoin d'une intention**, pas seulement de gestes. Un
visage qui attend trois secondes sans rien vouloir se lit comme froid.

**e) ⚠️ Minimal negation.** Le guide OmniHuman met *« clarity,
non-contradiction, and minimal negation »* en tête de ses principes — et nos
prompts alignaient **quatorze** négations, dont cinq d'affilée sur
l'arrière-plan, précisément le passage qui échouait. Un modèle qui doit se
représenter « personne ne s'avance » doit d'abord se représenter quelqu'un
qui s'avance. Leurs propres exemples d'arrière-plan sont positifs : *« The
leaves in the background sway. »*

### Ce qu'il ne faut PAS écrire

⚠️ **Rien de ce que l'image porte déjà** — ni l'apparence, ni la lumière, ni
l'optique. *« Do not describe static visual details already visible in the
input image. »* J'avais ajouté *« soft overhead terminal lighting, shallow
depth of field, 50mm »* sur la foi d'un guide **générique de texte-vers-
vidéo** ; il est juste pour son cas, où rien n'existe avant le prompt. Ici
l'image existe.

⚠️ **Et aucune fenêtre de parole en secondes.** C'était la panne de Seedance :
il recevait des chiffres et faisait ce qu'il voulait — de +0,11 à +1,96 s
d'écart. Chez un modèle piloté par l'audio, les réintroduire referait le
défaut qu'on cherche à supprimer.

---

## Les figurants, et les trois façons dont ils s'imposent

Le paragraphe qui marche, en positif :

> *Behind him, the arrivals hall goes on with its own life, far in the
> distance: travellers cross the back of the frame at that depth, small and
> soft in the background blur, each of them continuing on their way. They
> stay back there for the whole shot, and the space between him and them
> remains open.*

Trois choses à couvrir, et il a fallu trois prises pour les trouver toutes :
**l'espace intermédiaire reste vide**, **aucun visage de figurant ne devient
lisible**, **personne ne passe entre le personnage et l'objectif**.

---

## Ce qui reste ouvert

- ⚠️ **Les droits.** Ticket **I-2026091223400001** en cours. Voir
  `video/DROITS-omnihuman.md`. **Jusqu'à la réponse : on monte, on ne diffuse
  pas publiquement.**
- **Le compte BytePlus** : prendre **Business**, pas Personal — leur tableau
  d'accès produits ne liste pas OmniHuman pour Personal, et le choix est
  irréversible, le pays aussi.
- **La finesse du visage** : plafond du modèle, rien à régler.
- **Le plan 17 part de la même image que le 13** — même pose de départ, ça se
  voit au raccord. Les 200 générations d'images gratuites de Dreamina
  règleraient ça.
- **Les rendus devraient sortir hors de OneDrive par défaut**, pas y être
  écrits puis copiés.


---

## Étape 8 — le montage vitrine

⚠️ **Chaque épisode a DEUX montages, et le second est presque gratuit** : il ne
réutilise que des plans déjà tournés et déjà synchronisés. Aucun crédit, aucune
prise neuve.

| | montage cours | montage vitrine |
|---|---|---|
| ouvre sur | le décor, la narration | **la chute** |
| durée | ~75 s | 25 à 40 s |
| suppose | les épisodes précédents | **rien** |
| sert | à installer le vocabulaire | à faire venir des gens |

**Ce qui l'a rendu nécessaire.** Mesure sur l'épisode 1 : Mark ne parle pas
avant **20,65 s**, soit 28 % de l'épisode. Vingt secondes de patience demandées
à quelqu'un qui en accorde une. Ce n'est pas un défaut du montage cours — c'est
un autre métier.

```bash
python video/monter_avatar.py --vitrine
python video/sous_titres.py --langue fr     --clip video/episode-01-ankunft-berlin/EPISODE-01-vitrine.mp4     --feuille video/episode-01-ankunft-berlin/_montage-avatar/_plans-vitrine.json     --incruster
```

`--ordre 8,9,10,11` remplace la liste `VITRINE` pour essayer un autre montage
sans toucher au fichier.

### La vitrine se sonorise aussi, et l'ordre compte

⚠️ **Sonoriser AVANT d'incruster, une seule fois.** Sinon on grave les
sous-titres sur une vidéo sèche, puis on refait tout — c'est exactement l'erreur
commise le 13 septembre : les deux premières vitrines livrées n'avaient ni hall,
ni tapis, ni annonce, parce qu'elles avaient été montées depuis les prises
avatar brutes et non depuis la version sonorisée.

```bash
python video/ambiance.py --clip .../EPISODE-01-vitrine.mp4     --lit audio/ambiance/hall.mp3@0     --sortie .../EPISODE-01-vitrine-sonorise.mp4
```

⚠️ **LES INSTANTS DE LIT NE SE RECOPIENT PAS DEPUIS LE MONTAGE COURS.** Ils sont
donnés en secondes ; un montage qui garde sept plans sur dix-neuf n'a plus les
mêmes. Pour la vitrine de l'épisode 1 la réponse est simple — elle ne quitte
jamais le comptoir, donc un seul lit, `hall@0` — mais c'est une lecture du
montage, pas une règle générale.

⚠️ **ET PAS D'ANNONCE DANS UNE VITRINE.** L'annonce de haut-parleur ne tient que
parce qu'elle se pose là où personne ne parle — à 6,0 s dans le montage cours,
sous la narration. Une vitrine n'a aucun trou : chaque seconde porte du
dialogue, et l'annonce y deviendrait une troisième couche par-dessus la parole.
Sa justification tombe avec le silence qui l'accueillait.

### Le plan de carte — dessiné, jamais généré

⚠️ **C'est le seul type de plan où l'outillage bat le modèle génératif à tous
les coups.** Les cartes, les noms de villes et les traits de côte sont
exactement ce que ces modèles ratent : on obtient un « MONTRÉÁL » approximatif
sur un continent qui n'existe pas, et il faut vingt essais pour s'en
apercevoir. `video/carte_vol.py` le dessine : zéro crédit, zéro essai, le trait
au pixel près.

```bash
python video/carte_vol.py --sortie .../00-carte.mp4 --ffmpeg <chemin>
python video/monter_avatar.py --vitrine --tete .../00-carte.mp4
```

⚠️ **ET C'EST `--tete` QUI LE POSE, PAS UN CONCAT À LA MAIN.** Prépendre trois
secondes de carte décale **tout ce qui suit** : une feuille non corrigée dirait
que Mark parle à 0,00 s alors qu'il parle à 2,96, et chaque mot se surlignerait
trois secondes trop tôt. Le montage est le seul à savoir où commence chaque
plan — c'est donc lui qui pose la tête et qui écrit la feuille décalée.

⚠️ **Ce qu'on ne dessine pas, et c'est un choix** : pas de carte du monde. Sans
fond cartographique juste, une côte approximative se lit comme une faute — et
un apprenant qui vient d'un de ces pays la voit. On garde l'abstraction
honnête : deux points nommés, un arc, une grille de méridiens. Personne ne peut
y trouver d'erreur de géographie parce qu'on n'en affirme aucune.

La distance est **calculée** (haversine sur les coordonnées réelles des deux
aéroports), pas inventée : 6 025 km. Un nombre faux sur un plan de trois
secondes est une faute qui dure tout l'épisode.

⚠️ **UNE FEUILLE PAR MONTAGE.** La vitrine écrit `_plans-vitrine.json`, le cours
garde `_plans.json`. Sous-titrer la vitrine avec la feuille du cours placerait
chaque mot au mauvais endroit, **et rien ne s'en plaindrait** : les deux
fichiers sont valides, ils ne décrivent simplement pas la même vidéo.

⚠️ **ET UN PLAN FONDU SE DÉCLARE.** Le plan 20 est la seconde moitié du 13 :
il porte `"fondu_dans": 13` dans la scène. La règle d'avant — « un plan absent
du montage est rattaché au précédent » — marchait pour une fusion et cassait
pour une **sélection** : la vitrine ne garde que sept plans, et cette règle lui
aurait collé les sous-titres des plans 14, 15 et 16 sur le clip du 13.


---

## La continuité du décor — l'image de référence vient du plan précédent

### 16 septembre 2026, demandé par Jacques

⚠️ **Le modèle invente le décor, et il l'invente DIFFÉREMMENT à chaque plan.**
Observé sur l'épisode 2 : dans un plan, le fonctionnaire cherche à son
ordinateur, avec un panier à feuilles à sa gauche ; deux plans plus loin, **ni
ordinateur ni panier** sur le même bureau. Même pièce, même personnage, même
minute de récit.

Ce n'est pas un défaut de rendu : c'est que chaque plan part d'une **image
maîtresse différente**, et que rien n'oblige deux images générées séparément à
meubler la pièce pareil.

**La règle, dans les mots de Jacques :** *« prendre un print screen du dernier
décor, puis le mettre comme image de référence pour le second. Comme ça on ne
change rien de ce qu'il y a sur le bureau. »*

En pratique, trois niveaux, du plus sûr au plus risqué :

1. **Une seule image maîtresse par personnage ET par valeur de plan**, réutilisée
   par tous les plans de ce lieu. C'est déjà ce que font 04, 07, 09, 11, 15 et
   17 — tous nés de `beamter-moyen` — et c'est pour ça qu'ils s'accordent.
2. **Une image dérivée d'une IMAGE de la prise précédente** quand il faut un
   autre cadrage ou un accessoire en main : on extrait une image du clip
   accepté et on ne demande au modèle d'images que le changement voulu. Le
   décor, lui, est déjà là et ne se réinvente pas.
3. **Une image générée à part** — ce qui a produit la dérive. À n'utiliser que
   pour un lieu qu'on ne reverra pas.

⚠️ **Et ce n'est pas seulement le mobilier.** Le même jour, un formulaire est
passé du jaune vif (plans 13, 14, 17) au crème (12) au blanc (18, 19). Un objet
qui change de couleur d'un plan à l'autre casse la croyance plus sûrement qu'un
défaut technique : le spectateur ne se dit pas « tiens, une incohérence », il se
dit que ce n'est pas le même papier. `video/papier_blanc.py` répare après coup,
mais la vraie place de la correction est **en amont, dans l'image**.

## L'INTENTION S'ECRIT AVANT LE PROMPT, ET LES DEUX AVANT DE PAYER

Regle posee par Jacques le 16 septembre 2026, apres la journee du plan 12 :
**six versions, cinq payees, 0,75 $ sur une plaque de cinq secondes.**

> « Avant de lancer le prompt, je te demanderai de m'ecrire l'intention et le
> prompt, puis on va le revalider avec Jimmy, juste pour faire un double
> check. »

Donc, pour toute image ou toute prise facturee :

1. **L'INTENTION**, en francais, et elle repond a quatre questions :
   - a quoi sert ce plan dans l'episode ?
   - qu'est-ce qui doit etre LISIBLE dedans, sans le son et sans sous-titre ?
   - qu'est-ce qui s'y ajoutera ensuite (voix, sous-titre, incrustation) ?
   - qu'est-ce qui a deja rate ici, et pourquoi ?
2. **LE PROMPT EXACT**, celui que l'outil enverra -- pas une paraphrase.
   `--montrer` le donne gratuitement, c'est lui qu'on colle.
3. **LA RELECTURE CROISEE** par un autre modele, avant l'appel.
4. Seulement ensuite, la depense.

⚠️ CE QUE CETTE REGLE CORRIGE, ET CE N'EST PAS DE L'ETOURDERIE. Le plan 12 a
   brule cinq images parce que je defendais une exigence -- un partage 50/50 --
   que je n'avais JAMAIS justifiee. Il a suffi que Jacques demande « qu'est-ce
   que tu cherches a faire exactement ? » pour qu'elle tombe : personne
   n'apprend mieux parce que les bandes sont egales, et pendant que je
   poursuivais ca, le vrai defaut restait entier (l'image illustrait « Rot fuer
   Raeder » et rien de « Grau fuer Menschen »).

   Ecrire l'intention AVANT le prompt oblige a dire a quoi sert le plan. Une
   exigence qui ne survit pas a cette phrase ne merite pas qu'on la paie.
